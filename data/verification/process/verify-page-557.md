# Verification process log — verify-page-557


## [2026-10-17T00:00:15.906Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 557 only. Chart text: /home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-557.txt; source JSON: /home/sfmqrb/git/rishe-private/data/extracted/batch/page-557.json. Write /home/sfmqrb/git/rishe-private/data/verification/page-557.json, run `python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py 557` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-10-17T00:00:15.971Z] INPUT

<system-reminder>
Your final report is delivered through SubagentHandback: when your work is complete, call SubagentHandback({message: <your full report>}). The call ends your run, so make it your last step. Only a SubagentHandback call reaches your caller as your result; plain text you write at the end is not delivered.
</system-reminder>


## [2026-10-17T00:00:27.905Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-10-17T00:00:27.926Z] TOOL RESULT

```
1	# Etymology verification task — instructions
2	
3	You are verifying the etymological derivations from Ali Nourai's *An Etymological
4	Dictionary of Persian, English and other Indo-European Languages* (1999), which this
5	repository (`/home/sfmqrb/git/rishe-private`) turned into JSON (`data/extracted/batch/page-<pdf>.json`).
6	Compact text renderings of the charts are in
7	`/home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-<pdf>.txt`.
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
52	  offsets and lookup hints: `/home/sfmqrb/git/rishe-private/data/verification/sources/refs_online.json`
53	  (keys = abbreviations; `kind`, `url`, `lookup_hint`, `local_file`, `page_offset`, `scans`, `cites`).
54	- If `local_file` is set, the OCR text of that book is on disk under
55	  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/`: grep it for the headword (try
56	  several spellings — OCR of diacritics is noisy; e.g. `grep -n -i 'barak' …`) and, if a page
57	  offset is given, locate the cited page (pages are separated by form-feeds; `_pages.txt`
58	  files also carry `[pdf page N]` tags; use `awk 'BEGIN{RS="\f"} NR==<n>' file` to print one
59	  page). Read the entry and judge whether it actually says what Nourai's arrow says.
60	- **Scanned references without full OCR text** (Borhan-e Qate' vols 3–5 = BQT pages
61	  ~1208–2475, Farahvashi's Iranvij = IRN, Aryanpur = ARY, any entry with a `scans` list): do
62	  NOT OCR whole books. Fetch only the cited page:
63	  `python3 /home/sfmqrb/git/rishe-private/tools/ref_page.py BQT:918 --image`
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
103	`/home/sfmqrb/git/rishe-private/data/verification/sources/SOURCE_MATRIX.md`. Minimum per node:
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
140	with `pdftoppm -f <pdf page> -l <pdf page> -r 300 -png -singlefile /home/sfmqrb/git/rishe-private/EtymologicalDictionary-persian-english.pdf /tmp/pg<pdf page>`
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
187	  `python3 /home/sfmqrb/git/rishe-private/tools/fetch_source.py '<URL>' --note '<page N, root X, what you used it for>'`
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
224	Write `/home/sfmqrb/git/rishe-private/data/verification/page-<pdf>.json` (UTF-8, no BOM):
225	
226	Several agents run at the same time and share the scratchpad and `/tmp`, so every temporary
227	file you create must carry your page number in its name (e.g. `e0-363.json`, `pg363.png`,
228	`draft-363.json`), never a bare `e0.json` or `entry.json` — another agent will overwrite it.
229	
230	In the shell, `ls` is aliased to `eza`, which can hang without a terminal and leave your
231	command stuck. List files with `command ls` or `find` instead.
232	
233	```json
234	{
235	  "pdf_page": 126,
236	  "book_page": 96,
237	  "verified_by": "claude-opus-5",
238	  "verified_on": "2026-09-05",
239	  "entries": [
240	    {
241	      "entry": 0,
242	      "root": "Dheigh, Dhigha",
243	      "verdict": "confirmed",
244	      "modern_form": "PIE *dʰeyǵʰ- 'to knead, form (clay)'",
245	      "note": "Pokorny 244 dheiĝh-; AHD dheigh-. Root, language label and gloss all correct.",
246	      "note_fa": "ریشهٔ هندواروپایی آغازین *dʰeyǵʰ- «خمیر کردن، شکل دادن (گِل)» … ادعای نورایی درست است.",
247	      "sources": ["https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/dʰeyǵʰ-"],
248	      "ref_check": [{"ref": "POK:244", "status": "supports", "note": "…"}],
249	      "consulted": [{"src": "WLD", "where": "Bd. I 833", "stance": "supports", "note": "…"}],
250	      "nodes": [
251	        {
252	          "id": 6,
253	          "lang": "Avestan",
254	          "words": "pairi-daeza",
255	          "verdict": "confirmed",
256	          "derivation": "Av. pairi-daēza- 'walled enclosure' = pairi 'around' (PIE *per-) + daēza- 'wall' …",
257	          "derivation_fa": "«پردیس» … اوستایی pairi-daēza- «دیوارکشیده، باغِ محصور» از pairi «پیرامون» و daēza- «دیوار» …",
258	          "sources": ["https://en.wiktionary.org/wiki/pairidaēza"],
259	          "ref_check": [{"ref": "POK:244", "status": "supports", "note": "…"}],
260	          "consulted": [{"src": "BRT", "where": "col. 866", "stance": "supports", "note": "…"}]
261	        }
262	      ]
263	    }
264	  ]
265	}
266	```
267	
268	Rules:
269	- Include EVERY node of every non-redirect entry on the page (even empty-word pass-through
270	  nodes like `[Latin] refs=None |` — give them a one-line derivation and a verdict).
271	- `words` = the transliterations of the node joined by "; " (copy from the chart).
272	- `derivation` must be specific: forms, sound changes, dates/eras, texts or peoples,
273	  semantic shifts. 1–5 sentences. No hand-waving like "derived regularly".
274	- Keep `note` on the entry for root-level comments and for anything cross-cutting.
275	- If a node lists several words, cover each word; if they differ in verdict, use the worst
276	  verdict for the node and explain per word in `derivation`.
277	- Where the chart's own NOTE already records a dispute, evaluate it: say which side modern
278	  scholarship takes.
279	- Every node has `ref_check` (array, may contain a single `not_checked` item) AND `consulted`
280	  (array) AND `derivation_fa` (string); every entry has `note_fa`.
281	- Valid JSON only. Test it with `python3 -m json.tool` before finishing, then run
282	  `python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py <pdf page>` — it must show 0 PROBLEM lines.
283	- When done, reply with a SHORT summary (≤ 15 lines): counts of verdicts per page, and a
284	  bullet per `disputed` / `transcription_suspect` item (root, word, one-line reason), plus
285	  any extraction errors (JSON differs from the printed page) the owner must fix.
286	  Do not paste the JSON back into your reply.
287	
```


## [2026-10-17T00:00:28.381Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-557.txt"
}
```


### [2026-10-17T00:00:28.406Z] TOOL RESULT

```
1	=== PDF page 557 (book page 527) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Wreg 1 : to push, drive  (refs POK:1181)
4	#1 (parent #0) [Sanskrit] refs=POK:1181 | vrâj : to walk, go
5	  #2 (parent #1) [Persian] refs=HRN:200; BQT:1781 | gorâzîdan «گرازیدن» : to walk proudly, stride
6	#3 (parent #0) [Germanic] refs=AHD | wrekjan : wreck ; wrakjo : exile
7	  #4 (parent #3) [French] refs=KLN:640,642 | garcon : waiter ; garcette : waitress
8	    #5 (parent #4) [Persian] refs=MON:3164 | gârson «گارسن»
9	    #6 (parent #4) [English] refs=None | gasket
10	#7 (parent #0) [Latin] refs=AHD | urgere : to urge
11	  #8 (parent #7) [English] refs=None | urge
12	--- entry 1 ---
13	ROOT Wreg 2 -> redirect to Wer 3
14	--- entry 2 ---
15	ROOT Wrei -> redirect to Wer 2
16	--- entry 3 ---
17	ROOT Wrg -> redirect to Wer 3
18	--- entry 4 ---
19	ROOT Wrod -> redirect to Wrdho
20	--- entry 5 ---
21	ROOT Wropal -> redirect to Wer 2
22	--- entry 6 ---
23	ROOT [Arabic] W.s.m : to mark  (refs KLN:1000)
24	#1 (parent #0) [Arabic] refs=KLN:1000 | wasama : he marked ; mousim : marking of the year, season
25	  #2 (parent #1) [Persian] refs=FVA:430; MON:5026 | vasm «وسم» : mark, brand ; vasmeh «وَسمه» : eyebrow makeup, the plant used in producing it ; semat «سِمَت» : marking, rank, position ; mowsem «موسم» : season
26	  #3 (parent #1) [Portuguese] refs=KLN:1000; AHD:850 | mončâo : season
27	    #4 (parent #3) [Dutch] refs=KLN:1000; AHD:850 | monssoen : seasonal winds (obsolete)
28	      #5 (parent #4) [English] refs=KLN:1000; AHD:850; OXF:269 | monsoon : the seasonal winds of the Indian ocean
29	
```


## [2026-10-17T00:00:28.988Z] TOOL CALL #3: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/extracted/batch/page-557.json"
}
```


### [2026-10-17T00:00:29.018Z] TOOL RESULT

```
1	{
2	  "pdf_page": 557,
3	  "book_page": 527,
4	  "entries": [
5	    {
6	      "root": {
7	        "name": "Wreg 1",
8	        "lang": "Indo-European",
9	        "refs": "POK:1181",
10	        "gloss": "to push, drive"
11	      },
12	      "nodes": [
13	        {
14	          "id": 1,
15	          "parent": 0,
16	          "lang": "Sanskrit",
17	          "refs": "POK:1181",
18	          "words": [
19	            {"translit": "vrâj", "gloss": "to walk, go", "script": null}
20	          ],
21	          "note": null,
22	          "quote": null
23	        },
24	        {
25	          "id": 2,
26	          "parent": 1,
27	          "lang": "Persian",
28	          "refs": "HRN:200; BQT:1781",
29	          "words": [
30	            {"translit": "gorâzîdan", "gloss": "to walk proudly, stride", "script": "گرازیدن"}
31	          ],
32	          "note": null,
33	          "quote": {"text": "نوازنده بلبل به باغ اندرون - گرازنده آهو به راغ اندرون", "poet": "Ferdowsî"}
34	        },
35	        {
36	          "id": 3,
37	          "parent": 0,
38	          "lang": "Germanic",
39	          "refs": "AHD",
40	          "words": [
41	            {"translit": "wrekjan", "gloss": "wreck", "script": null},
42	            {"translit": "wrakjo", "gloss": "exile", "script": null}
43	          ],
44	          "note": null,
45	          "quote": null
46	        },
47	        {
48	          "id": 4,
49	          "parent": 3,
50	          "lang": "French",
51	          "refs": "KLN:640,642",
52	          "words": [
53	            {"translit": "garcon", "gloss": "waiter", "script": null},
54	            {"translit": "garcette", "gloss": "waitress", "script": null}
55	          ],
56	          "note": null,
57	          "quote": null
58	        },
59	        {
60	          "id": 5,
61	          "parent": 4,
62	          "lang": "Persian",
63	          "refs": "MON:3164",
64	          "words": [
65	            {"translit": "gârson", "gloss": null, "script": "گارسن"}
66	          ],
67	          "note": null,
68	          "quote": null
69	        },
70	        {
71	          "id": 6,
72	          "parent": 4,
73	          "lang": "English",
74	          "refs": null,
75	          "words": [
76	            {"translit": "gasket", "gloss": null, "script": null}
77	          ],
78	          "note": null,
79	          "quote": null
80	        },
81	        {
82	          "id": 7,
83	          "parent": 0,
84	          "lang": "Latin",
85	          "refs": "AHD",
86	          "words": [
87	            {"translit": "urgere", "gloss": "to urge", "script": null}
88	          ],
89	          "note": null,
90	          "quote": null
91	        },
92	        {
93	          "id": 8,
94	          "parent": 7,
95	          "lang": "English",
96	          "refs": null,
97	          "words": [
98	            {"translit": "urge", "gloss": null, "script": null}
99	          ],
100	          "note": null,
101	          "quote": null
102	        }
103	      ]
104	    },
105	    {
106	      "root": {"name": "Wreg 2", "redirect": "Wer 3"},
107	      "nodes": []
108	    },
109	    {
110	      "root": {"name": "Wrei", "redirect": "Wer 2"},
111	      "nodes": []
112	    },
113	    {
114	      "root": {"name": "Wrg", "redirect": "Wer 3"},
115	      "nodes": []
116	    },
117	    {
118	      "root": {"name": "Wrod", "redirect": "Wrdho"},
119	      "nodes": []
120	    },
121	    {
122	      "root": {"name": "Wropal", "redirect": "Wer 2"},
123	      "nodes": []
124	    },
125	    {
126	      "root": {
127	        "name": "W.s.m",
128	        "lang": "Arabic",
129	        "refs": "KLN:1000",
130	        "gloss": "to mark"
131	      },
132	      "nodes": [
133	        {
134	          "id": 1,
135	          "parent": 0,
136	          "lang": "Arabic",
137	          "refs": "KLN:1000",
138	          "words": [
139	            {"translit": "wasama", "gloss": "he marked", "script": null},
140	            {"translit": "mousim", "gloss": "marking of the year, season", "script": null}
141	          ],
142	          "note": null,
143	          "quote": null
144	        },
145	        {
146	          "id": 2,
147	          "parent": 1,
148	          "lang": "Persian",
149	          "refs": "FVA:430; MON:5026",
150	          "words": [
151	            {"translit": "vasm", "gloss": "mark, brand", "script": "وسم"},
152	            {"translit": "vasmeh", "gloss": "eyebrow makeup, the plant used in producing it", "script": "وَسمه"},
153	            {"translit": "semat", "gloss": "marking, rank, position", "script": "سِمَت"},
154	            {"translit": "mowsem", "gloss": "season", "script": "موسم"}
155	          ],
156	          "note": null,
157	          "quote": {"text": "کس نتواند گرفت دامن دولت بزور - کوشش بیفایده است وسمه بر ابروی کور", "poet": "Sa`dî"}
158	        },
159	        {
160	          "id": 3,
161	          "parent": 1,
162	          "lang": "Portuguese",
163	          "refs": "KLN:1000; AHD:850",
164	          "words": [
165	            {"translit": "mončâo", "gloss": "season", "script": null}
166	          ],
167	          "note": null,
168	          "quote": null
169	        },
170	        {
171	          "id": 4,
172	          "parent": 3,
173	          "lang": "Dutch",
174	          "refs": "KLN:1000; AHD:850",
175	          "words": [
176	            {"translit": "monssoen", "gloss": "seasonal winds (obsolete)", "script": null}
177	          ],
178	          "note": null,
179	          "quote": null
180	        },
181	        {
182	          "id": 5,
183	          "parent": 4,
184	          "lang": "English",
185	          "refs": "KLN:1000; AHD:850; OXF:269",
186	          "words": [
187	            {"translit": "monsoon", "gloss": "the seasonal winds of the Indian ocean", "script": null}
188	          ],
189	          "note": null,
190	          "quote": null
191	        }
192	      ]
193	    }
194	  ]
195	}
196	
```


## [2026-10-17T00:00:35.441Z] TOOL CALL #4: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification; cat sources/SOURCE_MATRIX.md | head -80; command ls sources/refs/ | head -100; python3 -c \"\nimport json;d=json.load(open('sources/refs_online.json'))\nfor k in ['POK','AHD','HRN','BQT','KLN','MON','FVA','OXF','WLD','IEC','SYN','HUB','CHEUNG','ARY','SKT','FSD','WEB','FVQ','AFM','PLA','LKT','HJB','DEV','PHN','DOZ','LAM']:\n  print(k, json.dumps(d.get(k),ensure_ascii=False)[:400])\n\""
}
```


## [2026-10-17T00:00:36.176Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification; command ls page-5*.json | tail -5; cat /home/sfmqrb/git/rishe-private/tools/verify_check.py | head -80"
}
```


### [2026-10-17T00:00:36.715Z] TOOL RESULT

```
# Source matrix — which local books to grep for each kind of node

All files are OCR text; pages are separated by form-feeds (`\f`) and, in the `_pages.txt` files, tagged `[pdf page N]`. Print one page with `awk 'BEGIN{RS="\f"} NR==<n>' file`. Grep several spellings (OCR of diacritics is noisy; Persian OCR is rough — try short substrings). Full titles, page offsets and what a cited number means: data/verification/sources/refs_online.json.

ARY (Aryanpur) is alphabetical by Persian headword; grep the Persian word in ARY_pages.txt or the Latin-caps transliteration in ARY_latin_index_pages.txt, note the [pdf page N] tag, and quote from that page (printed page = pdf page + 1).


## Indo-European roots (any IE node, root boxes)

- **POK** — J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/POK_01.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/POK_02.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/POK_03.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/POK_full.txt`
- **WLD** — A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-3
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/WLD_band3.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_text.pdf`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd1_pages.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_text.pdf`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd2_pages.txt`
- **AHD** — W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appe
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/AHD_watkins1985.txt`
- **IEC** — S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/IEC.txt`
- **SYN** — C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SYN.txt`
- **KLN** — E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KLN_1966.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KLN_1971.txt`
- **SKT** — W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SKT.txt`
- **LEW** — A. Walde (& J. B. Hofmann), Lateinisches etymologisches Wörterbuch, 3rd ed., Heidelberg 1938-56
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/LEW_1910.txt`
- **LAT** — A. Ernout & A. Meillet, Dictionnaire étymologique de la langue latine, 3rd ed., Paris 1951
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/LAT.txt`
- **ARY** — Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپای
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY/ARY_pages.txt`

## Iranian: Avestan / Old Persian / Pahlavi / Sogdian / Khotanese / New Persian

- **BRT** — C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BRT.txt`
- **KNT** — R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KNT.txt` (truncated before the lexicon's h–z section, ~p. 208 on)
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KNT_full.txt` (complete archive.org djvu text — use this for lexicon pages 208–215: haumavarga-, siyamam, etc.)
- **PHD** — D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/PHD.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/PHD_mackenzie.txt`
- **NYB** — H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/NYB_vol1.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/NYB_vol2_glossary.txt`
- **HRN** — P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HRN.txt`
- **HUB** — H. Hübschmann, Persische Studien, Strassburg 1895
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HUB.txt`
- **CHEUNG** — CHEUNG
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/CHEUNG.txt`
- **SOD** — Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SOD.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SOD_pages.txt`
- **SNS** — Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SNS.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SNS_pages.txt`
- **BQT** — Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/19
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_alt_v1.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_dli_part1.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v1.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v1_pages.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v2.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v2_pages.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf`
- **MON** — Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols
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
KNT_full.txt
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
SKT_dli_revised.txt
SKT.txt
SNS_pages.txt
SNS.txt
SOD_pages.txt
SOD.txt
SPG_keilinschriften1881.txt
SYN.txt
TAD_pages.txt
TAD.txt
tessdata
TLM.txt
UNV.txt
WEB_vol1.txt
WLD_band3.txt
ZAP.txt
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
FVA {"title": "S.M. Nahvi, Farhang-e Vazheha-ye Arabi dar Farsi (dakhil), Tohi/Azadi 1368/1989", "kind": "catalog", "url": "https://openlibrary.org/works/OL4602367W (edition OL2012991M: Intisharat-i Islami 1368/1989, 582 pp)", "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: no digital copy found.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 202
OXF {"title": "J. Speake, Oxford Dictionary of Foreign Words and Phrases, New York 1997", "edition_found": "1997 (lending-only)", "kind": "archive_restricted", "url": "https://archive.org/details/oxforddictionary00spea ; isbn_9780965016070 (lending) ; Google Nvu17oLIQNgC = 2008 2nd ed. preview only", "identifier": "oxforddictionary00spea (also isbn_9780965016070)", "local_file": null, "page_offset": n
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/source
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 
CHEUNG null
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-D
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-di
FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.t
AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_page
PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf",
LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. l
HJB {"title": "H. Yule & A. C. Burnell, Hobson-Jobson, 2nd ed. by W. Crooke, London 1903 (Delhi reprint 1968)", "edition_found": "1903 Crooke edition (pagination identical to the 1968 reprint)", "kind": "archive_djvu", "url": "https://archive.org/details/hobsonjobsonagl02croogoog", "identifier": "hobsonjobsonagl02croogoog (others: bub_gb_6Z5iAAAAMAAJ, hobsonjobsonglos00yulerich, india.history.resource
DEV {"title": "L. M. Devic, Dictionnaire étymologique des mots français d'origine orientale, Paris 1876", "edition_found": "1876", "kind": "archive_djvu", "url": "https://archive.org/details/dictionnairety00devi", "identifier": "dictionnairety00devi (also dictionnairetym02devigoog, fr105comparative41)", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/DEV.txt", "page_offset
PHN {"title": "A. P. Pihan, Dictionnaire étymologique des mots de la langue française dérivés de l'arabe, du persan ou du turc, Paris 1866", "edition_found": "1866", "kind": "archive_djvu", "url": "https://archive.org/details/dictionnairetym01pihagoog", "identifier": "dictionnairetym01pihagoog (others: bub_gb_QnsSAAAAIAAJ, dictionnairetym00pihagoog)", "local_file": "/home/sfmqrb/git/rishe-private/data
DOZ {"title": "R. Dozy, Oosterlingen: Verklarende lijst der Nederlandsche woorden die uit het Arabisch, Hebreeuwsch, Chaldeeuwsch, Perzisch en Turksch afkomstig zijn, Leiden 1867", "edition_found": "1867", "kind": "archive_djvu", "url": "https://archive.org/details/oosterlingenver00dozygoog", "identifier": "oosterlingenver00dozygoog (also ...01dozygoog, ...02dozygoog)", "local_file": "/home/sfmqrb/git
LAM {"title": "H. Lammens, Remarques sur les mots français dérivés de l'arabe, Beyrouth 1890", "edition_found": "1890", "kind": "archive_djvu", "url": "https://archive.org/details/remarquessurles00lammgoog", "identifier": "remarquessurles00lammgoog", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/LAM.txt", "page_offset": "leaf = printed + 57 (e.g. leaf 59 = p.2). local fi
```


### [2026-10-17T00:00:36.783Z] TOOL RESULT

```
page-55.json
page-56.json
page-57.json
page-58.json
page-59.json
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


## [2026-10-17T00:01:04.820Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; python3 -c \"\nimport json;d=json.load(open('../refs_online.json'))\nfor k in ['POK','AHD','HRN','KLN','MON','BQT','CHEUNG','PHD','NYB','BRT']:\n  v=d.get(k) or {}\n  print(k, v.get('page_offset'), '|', (v.get('lookup_hint') or '')[:500]);print()\n\"; grep -n -i 'wreg' POK_full.txt | head; grep -n -i 'vraj' POK_full.txt | head"
}
```


### [2026-10-17T00:01:05.397Z] TOOL RESULT

```
POK POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-dictionary/ (entry pages with page numbers) and StarLing https://starlingdb.org/cgi-bin/query.cgi?bas

AHD 1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page. | Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru-' ; entries list English derivatives in caps. Restricted 1970s AHD scans on IA (lending only, djvu.txt returns 401): americanheritage0000dict (July 1977 printing, 970 leaves - probably the New Colleg

HRN leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.

KLN KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.

MON None | Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Aden

BQT vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...'). | grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf imag

CHEUNG None | 

PHD leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Headword = Pahlavi in transliteration at line start, followed by Pahlavi script (not OCRed) and gloss, e.g. grep -n '^abar '. Alternative PDF: https://www.parsianjoman.org/wp-content/uploads/2015/09/A-Concise-Pahlavi-Dictionary.pdf (8.4 MB).

NYB Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Nourai's 'NYB' numbers are Part II (Glossary) pages. Headwords are Pahlavi in transliteration at line start (e.g. grep -n '^apar'), with Avestan/OP/NP cognates and 'Bthl.' refs.

BRT Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Nourai's BRT numbers are Bartholomae's COLUMN numbers. Headwords are Avestan/OP in transliteration in bold at line start; OCR of the special transliteration is noisy - grep on a distinctive Latin gloss or the German meaning in quotes. Column numbers appear as standalone numbers at leaf tops.

39870:Note: alb. grua : Breton gwreg: Welsh gwraig^m^e, woman'. 
45776:shirt', gwregys {iw *gwe-grysirorc\ *gwo-grys) 'belt, girdle', acorn, kreis^ shirt ', grugis 
91147:Material: Old Indie vraja-m. " hurdle, Umhegung', vrjana-m. "Umhegung, Einfriedigung, 
91153:168f.); Avestan varaz- ^absperren'; oss. aerudez{*wraza-= Old Indie vraja-) " herd, 
93313:Material: Old Indie perhaps uraya// "schreitet, goes', pra-vrajayati ^ aWo^s wandern, 
93337:Icelandic rac^ pursuit ', A^Ar'verwerflich', rgekja{: Old Indie vrajayati) ' reject, vertreiben' =
```


## [2026-10-17T00:01:20.839Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 93300,93370p POK_full.txt"
}
```


### [2026-10-17T00:01:21.252Z] TOOL RESULT

```
but Old Church Slavic u-raz/f/ 'percuiere', russ. raz^meaV, Czech raz'b\o\N, knock' etc. 
belong probably rather to *yreg-. 

References: WP. I 318 f., Vasmer 2, 484. 
Page(s):1181 

Root / lemma: ureg- (and uerg-1) {*hauerg-) 

Meaning: to push, drag, drive 

Material: Old Indie perhaps uraya// "schreitet, goes', pra-vrajayati ^ aWo^s wandern, 

verbannt', pa/aK/y- 'Verstoftener'; Persson Beitr. 501 seeks against it in ihnen ein with 

*uer-g-^\uxv\'' (see 1154) nachstverwandtes *ure-g-, basic meaning "sich drehend 

bewegen'; 

Latin urged {bes\6es early, but originally urgued), -e/'e'urge, press, push, beset, press' 
{*urgeido'c *urgeid)\ 

Gothic wrikan^ pursue ', Old Icelandic Ae/ra 'drive, push, hunt, chase, pursue, throw, 
reject ', Old English wrecan^ wxo^q, press, push, drive, push, avenge ' (and 'vorwarts 
march, step, stride, strut', see above). Old Frisian wreka'dme, push, avenge ', Old Saxon 
wrecan' avenge, punish, curse', Old High German rehhands., wreh^ex\}\\ Gothic wraks' 
pursuer', wrakjan' pursue ', Old English wracu^ revenge, vengeance, punishment, 
woefulness ', wrsecu. " banishment, woefulness ', wrecc(e)an^a\}ivc\\}v\{erv\, set in motion, 
waken, arouse, revive', wrecca^e\n Verbannter, Elender, foreigner, stranger'. Old Saxon 
wrekkio. Old High German (w)reck(e)o^\av\6esi\udc\WQe'c hero ', Modern High German (new 
from dem Middle High German aufgenommen) Recke; Old English wraec^ banishment, 
woefulness ', Norwegian Aa/r'umhertreibender object, debris or kelp ' (hence Middle Low 
German H^Aa/r 'Wrack'), with ealso isl. /le/r'auf dem Wasser treibender object '; 
lengthened grade Gothic wrekeT pursuit ', Old Frisian wreke. Old Saxon wraka^ 
punishment, revenge, vengeance ', Old High German rahha 'revenge, vengeance ' Old 
Icelandic rac^ pursuit ', A^Ar'verwerflich', rgekja{: Old Indie vrajayati) ' reject, vertreiben' = 
Old Frisian wreka. Old English wrsecan^6r\\e, push, urge, press, push'; 

Balto Slavic *uerg- in compatible meaning: Lithuanian vergas, Latvian i/e/ys 'slave'; 
ablaut. Lithuanian i/a/yas'need, woefulness ', i/aTyZ/'need to suffer, bear, endure'. Old 
Prussian wargan f\Vk. Sg. m. ' evil, wickedness, affliction, danger', Lithuanian vargus^ 
heavy, beschwerlich, woeful, wretched, miserable ', Latvian vargs^ woeful, wretched, 
miserable, siech'. Old Prussian wargs^evW, bad'; Old Church Slavic ura^b 'fiend', poln. 
wrog^ wickedness, evil, harm; the Bose, devil; Verhangnis'; 



yet Balto Slavic words also are compatible with Germanic warga-{see S. 11 54 under 
*uer-gh-, *i/e/'-"turn'). 

References: WP. I 319 f., WH. II 839 f., Trautmann 342, Vasmer 1, 228. 
Page(s):1181 

Root / lemma: ureik-, uereik- {*hauerk^ 

Meaning: " heath, heather, any of a number of low evergreen shrubs bearing clusters of 

purple flowers ' 

See also: see above S. 1 155 under uergh-. 

Page(s):1182 

Root / lemma: urek- {*hauei1(-) 

Meaning: ' talk, shout ' 

References: WP. I 318, II 343, 362, Trautmann 243, Vasmer 2, 508 f.
```


## [2026-10-17T00:01:29.604Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n '^wreg' AHD_watkins1985.txt; grep -n -A12 '^wreg-' AHD_watkins1985.txt | head -30; echo ===HRN; grep -n -i 'gur[aâā]z' HRN.txt | head; echo ===HUB; grep -n -i 'gur[aâā]z\\|guraz' HUB.txt | head; echo ===CH; grep -n -i 'r[aā]z\\b\\|urāz\\|wrāz\\|u̯rāz' CHEUNG.txt | head -20"
}
```


### [2026-10-17T00:01:29.939Z] TOOL RESULT

```
Exit code 1
(eval):1: ==HRN not found
```


## [2026-10-17T00:01:36.184Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i 'wreg' AHD_watkins1985.txt | head; echo \"== HRN\"; grep -n -i 'gur[aâā]z' HRN.txt | head; echo \"== HUB\"; grep -n -i 'gur[aâā]z' HUB.txt | head; echo \"== CH\"; grep -n -i 'wrāz\\|urāz\\|u̯rāz\\|gurāz' CHEUNG.txt | head -20"
}
```


### [2026-10-17T00:01:36.492Z] TOOL RESULT

```
1172:*wer-ald., “life or age of man” (*-ald-, age; see al-3), in Old English weorold, world: woRLD; c. Frankish *wer- wulf, “man-wolf” (*wulf, wolf; see wikvo-), in French garou, werewolf: LOUP-GAROU. 2. Latin vir, man: VI- RAGO, VIRILE, VIRTUE, (VIRTUOSA), (VIRTUOSO); DECEM- VIR, DUUMVIR, TRIUMVIR. 3. Possibly Latin ciria, curia, court, if regarded as from *co-vir, “men together” (co-, together; see kom): CURIA. [Pok. uiro-s 1177.] wleik-. To flow, run. Zero-grade form *wlik-. 1. Adjective *wlik-u-, wet, in: a. suffixed form *wlik-w-d- in Latin liquare, to dissolve: LIQUATE; b. suffixed form *wlik-w-é- in Latin liquére, to be liquid: LIQUESCENT, LIQUID, LIQUOR; DELIQUESCE, LIQUEFY. 2. Suffixed form *wlik-s- in: a. Latin lixa, lye: LIXIVIATE; b. Latin prélixus, poured forth, stretched out in front, extended (pro-, forth; see per’): PROLIX. [In Pok. leiku- 669.] wlkwo-. Wolf. 1. Germanic *wulfaz in: a. Old English wulf, wolf: WOLF; b. Middle Dutch wolf, wulf, wolf: AARDWOLF; Cc. Old High German wolf, wolf, in German Wolfram, tungsten: WOLFRAM; d. Frankish *wulf, wolf (see wi-ro-). 2. Taboo variant */upo- in Latin lupus, wolf: LOBO, LUPINE!, LUPINE?; LOUP-GAROU. 3. Taboo variant *luko- in: a. Greek lukos, wolf: LYCANTHROPE, LYCOPO- piuM; b. Suffixed form */uk’-ya in Greek lussa, martial rage, madness, rabies (“wolf-ness”): LYTTA; ALYSSUM. [Pok. ulkvos 1178.] wip-6-. Fox. 1. Latin vulpés, fox: VULPINE. 2. Taboo variant *slépek- in Greek alépéx, fox: ALOPECIA. [Pok. ulp-, lup- 1179.] wogYh-ni-. Plowshare, wedge. 1. Probably Germanic *wagjaz in Old English wecg, wedge: WEDGE. 2. Prob- ably Latin vdmer, plowshare: vOMER. [Pok. wog¢hni-s 1179.] wokso-. Wax. Related to weg-!. Germanic *wahsam in Old English wex, weax, wax: WAX!. [Pok. uokso- 1180.] wopsa. Wasp. Metathesized form *wospd. 1. Germanic *wosp- in Old English wesp, weps, wasp: wAsP. 2. Latin vespa, wasp: VESPIARY. [Pok. yobhsd 1179.] wos. You (plural). Latin vds (> Old French vous), you: RENDEZVOUS. [In Pok. 1. iu- 513.] wrad-. Branch, root. I. Basic form *wrdd- in Germanic *wrét- in Old Norse rét, root: ROOT!; RUTABAGA. II. Zero-grade form *wred-. 1. Germanic *wurtiz in: a. Old English wyrt, plant, herb: wort; b. German Wurzel (< *wurzwala, rootstock; *-wala, a roll, round stem; see wel-3), root: MANGELWURZEL. 2. Latin rddix, root: RACE3, RADICAL, RADICLE, RADISH, RADIX; DERACI- NATE, ERADICATE. 3. Suffixed form *wrod-mo- in Latin rdmus, branch: RAMOSE, RAMUS; RAMIFY. 4. Suffixed reduced form *wr(e)d-ya perhaps in Greek rhiza, root: RHIZO-, RHIZOME; COLEORHIZA, LICORICE, MYCORRHIZA. [Pok. ufe)rad- 1167.] wragh-. Thorn, tip. Greek rhakhis, ridge, spine: RACHIS. [Pok. 1. uragh- 1180.] wreg-. To push, shove, drive, track down. I. Basic form *wreg- in Germanic *wrekan in: a. Old English wrecan, to drive, expel: WREAK; b. Old Norse rek (older form urek), wreckage, akin to the Scandinavian source of Anglo-Norman wrec, wreck: WRECK. II. O-grade form *wrog-. 1. Germanic *wrakjén-, “pursuer, one pursued,” in: a. Old English wrecca, exile: WRETCH; b. Frankish *wrakjo, “one pursued, an exile,” perhaps in French garce, a girl: GASKET. 2.Germanic *wrakaz in: a. Old English wrzc, exile, punishment, and Middle Dutch wrak, wreckage: WRACK}; b. Swedish rak, wreckage, akin to the source of Middle English rak, mass of driven clouds: RackK®. III. Zero-grade form “wrg-eyo-, “urg-eyo- in Latin urgére, to urge, drive: URGE. [Pok. ureg- 1181.] wrég-. To break. Suffixed form *wrég-nu- in Greek rhégnunai, to burst forth: -RRHAGIA. [Pok. urég- 1181.] [wrod-. Rose. A word (not common Indo-European) of unknown origin. 1. Suffixed form *wrod-o- in Greek rhodon, rose: RHODO-; (RHODIUM). 2. Suffixed form *wrod-ya- (perhaps via Etruscan) in Latin rosa, rose:
1556:GASH gher-4 GASKET wreg- GasP_ ghai-
2160:RABBET battuere RABBLE? reu-2 RABID rebh-1 RABIES rebh-1 RACE? ers-1 RACES wrad- RACHIS wragh- RACK! reg-1 RACK3 wreg- RACLETTE réd- RADDLE! reidh- RADICAL wrad- RADICLE wrad- RADIOSONDE swem- RADISH wrad- RADIX wrad- RADULA réd- RAFT! rép-2 RAFTER rép-2 RAG! reu-2 RAGA reg-3 RAGE rebh-1 RAGOUT geus- RAID reidh- RAIL! reg-1 RAIN reg-2 RAINBOW reg-2 RAISE risan RAJ reg-1 RAJAH_ reg-! RAKE! reg-1 RALLENTANDO lento- RALLY leig-1 RAMBUNCTIOUS reudh-1 RAMEKIN reugh-men- RAMIFY wrad- RAMOSE wrad- RAMP2  skerbh- RAMPART pere-1 RAMPION rap- RAMSON krem- RAMUS wrad- RANCH sker-3 RANGE sker-3 RANI reg-1 RANK!  sker-3 RANK? reg-1 RANKLE derk- RANSACK sag- RANSOM em- RAPACIOUS rep- RAPE! rep- RAPE? rap- RAPHE wer-3 RAPHIDE wer-3 RAPID rep- RAPPORT per-2 RAPPROCHEMENT per! RAPT rep- RARE! era-2
2437:UNITY oi-no- UNIVERSE 0i-no-, wer-3 UNIVOCAL wekw- UNKEMPT gembh- UNTIL ant- UNWITTING weid- UP upo UPANISHAD sed-1, upo UPBRAID bherek- UPROAR kere-, upO UPSILON bhes-! URCHIN ghers- UREDO eus- URETER wers-2 URETHRA wers-2 URETIC wers-2 URGE wreg- -URGY werg- -URIA wers-2 URINE wér- URO-! wers-2 URO-2 ors- URONIC wers-2 -UROUS ors- URSINE rtko-
== HRN
== HUB
4393:arm. varz, phi. vazr^ zd. vazra-; guraz *Eber' (neben Baraz
5567:gurazldan *sich wiegend gehn, einherschreiten', skr.
5586:Up. guraz *Eber' (s. oben § 47) ; Vard N. pr., vgl. ap. Arta-
5608:= li^.^bad; varaz *Eber (Eznik 66 u. s. w.) = np. guraz;
5957:*gehe* (inf. raftan), Vgl. auch Gurazm bei Firdusi fiir
6159:birinj — gurinj *Reis* aus *virinj = *vrinjii' und bei gurazldan
7979:= zd. a^sma-, aus *aidhsmO'?, vgl. gr. ai&w; Gurazm bei
== CH
```


## [2026-10-17T00:01:42.625Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 5560,5575p HUB.txt; echo; sed -n 6155,6163p HUB.txt; echo \"== HRN leaf 221\"; awk 'BEGIN{RS=\"\\f\"} NR==222' HRN.txt | grep -n -i -B2 -A8 'gur\\|wieg\\|schreit' | head -60"
}
```


### [2026-10-17T00:01:43.235Z] TOOL RESULT

```
phyl. p. 167, jiid. pers. mit gu anlautend {gmmurdan\ also
aus mp. ^'viSnmrdan (oben p. 41); arab. Bistdm aus np. Bis-
tahm neben Gustahm = phi. Vistaxm Tab. 96; Bindoi =
arm. Vndoy, zu ap. Vindafarnah- u. s. w. Vgl. baskarl
oben p. 30.
§ 50. Ap. V im Anlaut vor r wird im Np. zu gii-
oder bi'i
gurazldan *sich wiegend gehn, einherschreiten', skr.
vraj 'schreiten, gehn ; birinj = gurinj (Muwaffaq p. 6,
14; 7, 3, 4 u. s. w.) 'Reis', semn. varinjf, afgh. vrize, skr.
vrlhi-j also ap. *vrinjii'?
Zur Geschichte des anlautenden v,
§ 51. Ap. V im Anlaut blieb erhalten im alteren
Pehlevi. Demgemass liaben die alteren armenischen
Lehnworter durchweg v:
Vahagn = phi. Varahran der Sassanideninschriften

anl. sp, st, sk etc. geblieben ist 2) (vgl. Spandaramet, Span-
daratj Spandiat^ Spram, Stahr u. s. w.); pazend durust
gesund' Shk. 242, Min. Gl. 66 = np. durust (s. oben p. 61).
Aus alterer Zeit scheint mir auch der Vokaleinschub bei
birinj — gurinj *Reis* aus *virinj = *vrinjii' und bei gurazldan
einherschreiten' aus *viraz — skr. vraj zu stammen.
B. Vokaleinschab im Inlant
fand statt zur Vermeidung iiberlanger Silben (auf kurzen
Vokal + drei Eonsonanten oder langen Vokal + zwei
== HRN leaf 221
13-Krätze' (69) ; vergl. nslov. gar je *Krätze', garjaOj garat
14-^kratzen' (Miklosich, Denkschr. WAW. Band 37, 40).
15:896. guräz *Eber .
16-aw. varäza- 'Eber ; phlv. varOz (geschrieben varoc),
17-arm. LW. varaz, vgl. Varazdat, Baoa^rj^, OvuQoiCfjg
18-(Armenier); ai. varähd- *Eber'.
19-kurd. heräz,
20-V
21-np. veraz *Eber' wird im FS (Vullers) durch einen
22-V
23-angeblichen Sähnämevers belegt, der aber des Metrums
24-halber kein solcher sein kann.
25:897. geräziden 'schreiten .
26:ai. V^vra}', vrdjati schreiten, gehen, fortgehen'
27-(Rückert, ZDMG. 10, 165).
28-898. girun 'schwer.
29:Kä§. gerün, gurun^ guro.
30-Vergl. aw. gouru- (d. i. garii-) ^) in gouru.zaodra-
31-unlustiger Opferer' (Geldner); phlv. gar an 'schwer ^);
32:ai. gurü' 'schwer, vergl. Comp, gdrtyas-^ Sup. gdrisfha-.
33-Die Grundform hatte einen r- Vokal.
34:899. gurd 'Held'.
35-[/^var- 'beschützen, wehren', vergl. ai. vft- 'Heer ;
36:phlv. gurt 'Held' (AV.), gurtlh vd. 20 (21).
37-*) Bartholomae, Handbuch § 8.
38-*) Gehört hierher auch das rätselhafte phlv. grM (vd. 5 (48) GH.,
39-z. B. hi^-l gräi 'grosse Unreinheit*?), vergl. np. giräi No. 5 bei
40-Vullers?
```


## [2026-10-17T00:01:48.082Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i 'g[uo]r[aā]z\\|wr[aā]z\\|\\*u̯raz\\|uraz-\\|vraj' CHEUNG.txt | head -20; grep -n -i 'wr[aā]z\\|wl[aā]c' PHD.txt PHD_mackenzie.txt NYB_vol2_glossary.txt | head; grep -n 'vrā[zj]\\|urvāz\\|urvaz' BRT.txt | head"
}
```


### [2026-10-17T00:01:48.455Z] TOOL RESULT

```
1016:Tati dialect of Owrazani 
13444:(Kand.) -uraz-, (impv.) viraz- ‘to sew, attach’ 
28306:*SANSKRIT: vraj” ‘to stride’ (RV+) > EWAia II: 594 
43114:-uraz-, viraz-, 198 
51926:vraj”, 438 
25689:urvaz-  I 544
25730:1 S4S  urvaza-
25732:•  g.  urväzä-  f.  Treude,  Wonne,  Selig- keit': Aumqsdrä  (sd.)  ala  yeca  yä  rao^bli dansatä  'za  (NS.)  Y.^.  i;  —  urvazUlS (sd.)  AvB  nä  . .  paitl.Jamyä  . .  urv&eütahyä 'zyä  (IS.)  Y.^.  2.
```


## [2026-10-17T00:01:53.243Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 28270,28320p CHEUNG.txt"
}
```


### [2026-10-17T00:01:53.739Z] TOOL RESULT

```
(Zor.) résta ‘handmade noodles, macaroni; dough rolled thin then rolled up and cut 
thin into strings’, NP arvis, arvis ‘a hair rope’ (LW) || (+ *abi-) Bal. (b)resag ‘to 
spin’, NP abrésum ‘silk’ || (+ *ui-) Kurd. (Sor.) guris ‘rope, string’ 

*NEIR: Pash. réSal ‘to spin’, Yghn. riwes-/riwesta ‘to twine, spin’ || (+ *abi-) Oss. I. 
elvisyn/elvest, D. elvesun/elvist ‘to spin’, Pash. wresol ‘to spin’, (LW) Pash. 
wresam, Sh. virexum, Sariq. varaxim, Yi. forgomé ‘silk’ 

*MISC: Orm. ras-/rasök ‘to spin’ = ris-/risók 


438 *uraj 


*SANSKRIT: vrési- name of waters (VS) = EWAia II: 598 
«PIE *ureik- ‘to turn around, wind’ — LIV: 699 | Pok.: 1158 f. 
*IE COGNATES: OE wrigian ‘to tend, incline’, Engl. wry (etc.), Lith. risti ‘to bind, tie 


up’ 

*REFERENCES: КРЕТ: 141a; EVP: 64, 90; IFL I: 405b f.; КРЕП: 202; IFL II: 209a; Lambton 1938: 42a; 
Abaev, Slovar’ I: 132; Andreev — PeSéereva: 314a Ё; MacKenzie 1966: 106; EVS: 86a; WIM I: 72; WIM 
H/1: 81; WIM III: 115; Werba 1997: 238 f.; Cabolov 1997: 72; Cabolov 2001: 406; Cheung 2002: 159; 
Lecoq 2002: 121, 123, 126 (passim); Vahman — Asatrian 2002: 79; Kiefer 2003: 205; Shahbakhsh: rés-; 
Korn 2005: 134 f., 151, 313, 379 


*uraj ‘to go forth’ 

*AVESTAN: uruuaj- ‘to go forth’ — Liste: 60 

Aor. s-: IND. 3pl. OAv. uruuaxsat (Y 34.13), SUBJ. 3sg. OAv. uruuaxsat (Y 44.8), ? Y Av. uruuasaiti (Yt 
44) 


*SANSKRIT: vraj” ‘to stride’ (RV+) > EWAia II: 594 

9 No further Ir. cognates are known. 

«PIE *ureg- ‘to pursue, trace’ = LIV: 697 | Pok.: 1181 

*IE COGNATES: Hitt. /urki-/ ‘trace, trail’, Lat. urgére ‘to urge’, Goth. wrikan “pursue, 


persecute’, OE wrecan ‘to drive, avenge’, Engl. to wreak, etc. 
*REFERENCES: Humbach 1957: 43; Lehmann 1986: 410; Werba 1997: 379 


*urad ‘to become enthousiastic, joyous ?’ 
*AVESTAN: Y Av. uruuad- ‘to become enthousiastic’, OAv. uruuädah- (n.) ‘joy, bliss’
```


## [2026-10-17T00:02:06.516Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n '\\*ura[zž]\\|\\*uraz\\|uruuaz\\|gu?raz\\|guraz' CHEUNG.txt | head; grep -n -i 'garçon\\|garcon\\|^gasket\\|^garcette' KLN_1966.txt | head; grep -n -i '^monsoon\\|^urge,' KLN_1966.txt"
}
```


### [2026-10-17T00:02:06.871Z] TOOL RESULT

```
28040:sa-formation. Cf. *urad vs *uraz, on which see Kümmel 2000: 623. 
28330:© This apparently Пг. root has no further Ir. cognate forms. See also *uraz. 
28334:*uraz ‘to be proud, haughty / to entertain, regale ?’ 
28336:*AVESTAN: uruuaz- ‘to be proud, haughty / to entertain, regale’ || Kellens — Pirart II: 
28343:Pres. them.: IND. 15р. ? OAv. uruuaza (Y 30.1), med. 3pl. YAv. uruuazonte (FrD 7); Perf.: IND. 35р. 
28344:Y Av. vaoraza (N 84), SUBJ. 2pl. OAv. vaoraza0a (Y 50.5); Partic.: pres. med. YAv. uruuazomna- (Yt 
28348:© The evidence for an Ir. root *uraz is limited to Av. No (possible) IE cognates can 
28349:be cited. According to Kümmel 2000: 623, Av. uruuaz- may be connected to *urad, 
28770:with ingressive *s-suffix *xad-z, cf. *urad vs *uraz (Kümmel 2000: 623) ? An IE 
33833:uruuaz-, 438 
24343:monsoon,  n.,  the  trade  wind  of  the  Indian  Ocean.
40872:urge,  tr.  v.  —  L.  urgere,  ‘to  press,  drive,  urge", cogn.  with  Goth,  wrikan,  ‘to  persecute’,  OE.
```


## [2026-10-17T00:02:15.276Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i '^gar.on\\|^gasket\\|^garce' KLN_1966.txt | head; sed -n 24343,24352p KLN_1966.txt; sed -n 40872,40878p KLN_1966.txt"
}
```


### [2026-10-17T00:02:15.828Z] TOOL RESULT

```
15794:garce,  n.,  a  measure  of  capacity  in  India.  — Telugu  garisa  (cp.  Tamil  karisai),  fr.  OI.  gariyas, ‘very  heavy’,  superl.  of  guruh,  ‘heavy,  weighty, venerable’,  which  is  cogn.  with  Gk.  ^apug,  L. gravis,  ‘heavy’.  See  grave,  ‘weighty’,  and  cp. guru.
15795:gargon,  n. —  F.,  ‘boy,  waiter’,  orig.  objective  case of  OF.  gars  (this  latter  is  still  used  as  a  provin¬ cial  word,  pronounced  go);  prob.  fr.  Frankish *wrakjo,  which  is  rel.  to  the  OHG.  PN.  Wrac- chio  and  to  OS.  wrekkio,  OHG.  recko,  ‘a  banish¬ ed  person,  exile’,  MHG.,  G.  recke,  ‘renowned warrior,  hero’,  and  to  E.  wretch  (q.v.)  Cp.  gos¬ soon.  Cp.  also  gasket.
monsoon,  n.,  the  trade  wind  of  the  Indian  Ocean.
—  MDu.  monssoen,  fr.  Port,  monfdo,  fr.  Arab. mdusim  (written  mousirri),  ‘time  of  the  year, season’,  fr.  wasama,  ‘he  marked  with  a  brand, he  marked'.  The  final  letters  -im  (in  Arab. mdusim)  were  misread  as  -un  (whence  Du.  -oen,
E.  -oon).  Cp.  the  word  zenith,  which  owes  its form  to  a  similar  misreading.
monster,  n.  —  ME.  monstre,  fr.  OF.  (=  F.) monstre,  fr.  L.  monstrum,  ‘an  evil  omen,  por¬ tent,  monster’,  for  *mone-strom,  lit.  ‘that  which serves  as  a  warning’,  fr.  monere,  ‘to  remind, warn,  advise,  instruct’.  L.  monstrare,  ‘to  show, point  out,  indicate’,  is  a  derivative  of  monstrum. See  monition  and  cp.  monstrance,  monstrous, demonstrate,  premonstrate,  remonstrate.  Cp.  also muster.
monstrance,  n.,  a  receptacle  in  which  the  conse¬ crated  host  is  shown  ( R .  C.  Ch.)  —  MF.,  fr. Eccles.  L.  monstrantia,  fr.  L.  mdnstrdns,  gen. -antis,  pres.  part,  of  monstrare.  See  monster  and -ance;  and  cp.  remonstrance, monstrosity,  n.,  the  quality  of  being  monstrous.
—  Late  L.  monstrositas,  ‘strangeness,  unnatural¬ ness',  fr.  L.  monstrosus,  a  collateral  form  of monstrudsus  (whence  F.  monstruositd).  See  next word  and  -ity.
monstrous,  adj.,  enormous;  horrible.  —  MF.  (=
F. )  monstrueux  (fern,  monstrueuse),  fr.  L.  mon- struosus,  ‘strange,  unnatural,  monstrous’,  fr. monstrum.  See  monster  and  -ous.
Derivatives:  monstrous-ly,  adv.,  monstrous-ness, n.
montage,  n.,  the  process  of  making  a  composite picture.  —  F.,  lit.  ‘a  mounting,  putting  togeth¬
urge,  tr.  v.  —  L.  urgere,  ‘to  press,  drive,  urge", cogn.  with  Goth,  wrikan,  ‘to  persecute’,  OE.
urgence
UbUIIUU
wrecan ,  "to  drive,  expel;  to  avenge'.  See  wreak. Derivatives:  urge,  n.,  urgent  (q.v.),  urg-er,  n. urgence,  n.  —  MF.  (=  F.),  fr.  Late  L.  urgentia.
See  next  word  and  -ce.
urgency,  n.  —  Late  L.  urgentia,  fr.  L.  urgens,  gen. -entis.  See  next  w'ord  and  -cy. urgent,  adj.  —  ME.,  fr.  MF.  (=  F.)  urgent,  fr.  L. urgentem,  acc.  of  urgens,  pres.  part,  of  urgere. See  urge  and  -ent.
Derivatives:  urgent-ly,  adv.,  urgent-ness,  n.
```


## [2026-10-17T00:02:22.430Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i '^gasket' KLN_1966.txt; grep -n -i 'gasket' KLN_1966.txt | head -3; python3 - <<'E'\nt=open('KLN_1966.txt').read().split('\\f')\nfor i,p in enumerate(t):\n    for w in ['garçon,','gargon,','gasket,','monsoon,','urge,  tr']:\n        if w in p: print(w,i)\nE\ngrep -n -i 'gasket\\|garcette\\|garçon' SKT.txt | head; grep -n -i 'monsoon' SKT.txt HJB.txt LKT.txt DOZ.txt | head"
}
```


### [2026-10-17T00:02:23.079Z] TOOL RESULT

```
15795:gargon,  n. —  F.,  ‘boy,  waiter’,  orig.  objective  case of  OF.  gars  (this  latter  is  still  used  as  a  provin¬ cial  word,  pronounced  go);  prob.  fr.  Frankish *wrakjo,  which  is  rel.  to  the  OHG.  PN.  Wrac- chio  and  to  OS.  wrekkio,  OHG.  recko,  ‘a  banish¬ ed  person,  exile’,  MHG.,  G.  recke,  ‘renowned warrior,  hero’,  and  to  E.  wretch  (q.v.)  Cp.  gos¬ soon.  Cp.  also  gasket.
15828:Derivatives:  gasifi-ablc,  adj.,  gasifi-er,  n. gasket,  n.,  a  piece  of  rope  ( naut .)  —  F.  garcette, dimin.  of  garce ,  ‘wench’,  femin.  to  gargon,  ‘boy’ ; used  only  in  a  figurative  sense.  See  gargon. gasoline,  gasolene,  n. —  A  hybrid  coined  fr.  gas, -ol  (fr.  L.  oleum,  ‘oil’)  and  chem.  suff.  -ine, resp.  -ene.
gargon, 346
gargon, 347
gasket, 347
monsoon, 536
urge,  tr 679
urge,  tr 745
urge,  tr 891
SKT.txt:11840:Monsoon,  a  periodical  wind.  (Ital.** Mulny.  —  .\r»b.)  Ital.  mcnjone  ■■  Mnla^f milsim,  a  season,  monsoon,  year.  — Arab. mawsim,  a  time,  season.  —  Arab,  -uxum (root  wasamd)^  marking.
LKT.txt:3333:'Jahreszeil',  z.  B.  für  die  jährliche  Pil- gerfahrt nach  Mekka,  auch  schon  bei den  ar.  Seeleuten  zur  Bezeichnung  der Zeit  «ebräui  hlicb,  die  günstig  war,  um mit  dem  Winde,  den  wir  heutzutage Westmousun  nennen,  nach  Indien  zu gelangen;  hieraus  pg.  mongäo,  mougäo, sp.  monzon,  frz.  mousson,  it.  monsone, mussone;  engl,  monsoon,  ndl.  monsoen, dtsch  Monsun.  [DE  317/319.  Eguilaz 458    ML  5439.
HJB.txt:2453:1872.—'*.  .  .  .  Badgixi  or  windcatchers. You  see  on  every  roof  these  diminutive screens  of  wattle  and  dab,  forming  acute angles  with  the  hatches  over  whidi  they project.  Some  are  moveable,  so  aa  to  m turned  to  the  S.W.  between  March  and  the end  of  July,  when  the  monsoon  sets  in  from that  quarter." — BvTUm*t  Sind  Revieited,  254.
HJB.txt:3313:1711.— "Ships  may  ride  secure  from  the South  West  Monsoon  at  Batte  Cove  (qu. BATTECOLE  ?),  and  the  River  is  navigable for  the  largest,  after  they  have  once  got  in." — Lockyer,  272.
HJB.txt:7879:properly  Karachi,  the  sea-port  and chief  town  of  the  province  of  Sind, which  is  a  creation  of  the  British  rule, no  town  appearing  to  have  existed  on the  site  Mtore  1725.  In  As  Suyuti's Htttary  of  the  Caliphs  (E.T.  p.  229)  the capture  of  Kirakh  or  Kiraj  is  men- tioned. Sir  H.  M.  Elliot  thinks  that this  place  was  probably  situated  in  if not  named  from  Kachh.  Jarrett  (Ain, ii.  344,  note)  supposes  this  to  be Karachi,  whicn  Elliot  identified  with the  Krokala  of  Arrian.  Here,  accord- ing to  Curtius,  dwelt  the  Aiabioi  or ArabitaL  The  harbour  of  Karachi  was possibly  the  Porus  Alexandri,  where Nearchus  was  detained  by  the  monsoon for  twenty-four  days  (see  McOrindUy Ancient  India,  167,  262).
HJB.txt:9372:bt.  8.  A  name  given,  originally  by the  Portugaese,  to  violent  storms occurring  at  the  termination,  though some  travellers  describe  it  as  at  tne aetting-in,  of  the  Monsoon.  [The Portngnese,  however,  took  the  name from  the  H.  haJOtiyO^  Skt.  hoM^  the 13th  lunar  Asterism,  connected  with huUny  an  elephant,  and  hence  some- times called  'tne  sign  of  the  elephant.' The  haithiyd  is  at  the  close  of  the Bains.]
HJB.txt:9379:[1690. — "The  Mussoaos  (Monsoon)  are rude  and  Boisterous  in  their  departure,  as well  as  at  their  coming  in,  which  two seasons  are  called  the  uephiuit  in  India, and  just  before  their  breaking  up,  take their  farewell  for  the  most  part  in  very ragged  pnfBng  weather."— Ovmptoa,  187].
HJB.txt:9639:1880.— "Harbingbbs  of  thb  Monsoon. — One  of  the  surest  indications  of  the  ap> proach  of  the  monsoon  is  the  spectacle  pre- sented nightlv  in  the  Mawul  taluka,  that is,  at  Ehandalla  and  Lanoli,  where  the  trees are  filled  with  myriads  of  flrvfliei,  which flash  their  phosphoric  light  simultaneously. Each  tree  suddenly  flashes  from  bottom  to top.  Thousands  of  trees  presenting  this appearance  simultaneously,  afford  a  spectacle beautiful,  if  not  grand,  beyond  conception. This  little  insect,  the  female  of  its  Idnd, only  appears  and  displays  its  brilliant  light immediately  before  the  monsoon." — Doxan Herald.    (From  Pioneer  Mail^  June  17).
HJB.txt:11244:1644.  —  "The  other  important  voyage which  used  to  be  made  from  Cochim  was that  to  Bengalla,  when  the  port  and  town of  Ugolim  were  still  standing,  and  much more  when  we  had  the  Porto  wande  (q.v.) and  the  town  of  Diangd;  this  used  to  be made  by  so  many  ships  that  often  in  one monsoon  there  came  80  or  more  from  Ben- galla to  Coohim,  all  laden  with  rice,  sugar, lac,  iron,  salt-petre,  and  many  kinds  of cloths  both  of  grass  and  cotton,  ghee {manteyga),  long  pepper,  a  great  quantity of  wax,  besides  wheat  and  many  things besides,  such  as  ouilts  and  rich  bedding; so  that  every  ship  Drought  a  capital  of  more than  20,000  zerafins.  But  since  these  two possessions  were  lost,  and  the  two  ports  were closed,  there  go  barely  one  or  two  vessels  to Orixa^^—Bocano,  MS.,  f.  816.
HJB.txt:12967:1644. — ^'And  as  it  is  between  monsoon and  monsoon  {^aumtom^  the  wind  is  quite uncertain  only  at  the  begixming  of  summer. The  N.W  prevails  more  than  an^  other  wind .  .  .  and  at  the  end  of  it  begin  the  land wlnda  (^errenAM)  from  midnight  to  about noon,  and  .these  are  E.  wincU." — BoeamL MS.
```


## [2026-10-17T00:02:31.966Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; python3 - <<'E'\nimport re\nt=open('KLN_1966.txt').read().split('\\f')\nfor i in [346,347,536]:\n    nums=re.findall(r'^\\s*(\\d{3,4})\\s*$',t[i],re.M)\n    print(i,nums[:6], t[i][:150].replace('\\n',' | '))\nE\ngrep -n -A25 '^Monsoon\\|^monsoon\\|Monsoon, s\\.' HJB.txt | head -40"
}
```


### [2026-10-17T00:02:32.408Z] TOOL RESULT

```
346 ['640'] ect,  rule  over’),  p.t- SecrUai,  ‘to  be  mindful  of,  give  heed  to,  think on’,  piSiiivos,  ‘a  measure’,  fr.  I.-E.  base ‘to  measure,  lim
347 [] .  OF.  guaroc, ‘shaft  of  the  cross-bow’  (with  change  of  suff.  -oc to  -ot,  owing  to  the  identical  pronunciation  of these  suffixes  in 
536 ['1000'] nd  L. nomen,  ‘name’ ;  see  mono-  and  nominal  and  cp. binomial,  trinomial,  multinomial.  The  contrac¬ tion  of  * mononome  into  *mo-nome  i
```


## [2026-10-17T00:02:38.318Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n 'MONSOON\\|mausim\\|mau-sim' HJB.txt | head; grep -n -i 'wasma\\|وسمه\\|wasm' FVQ_pages.txt AFM_pages.txt PLA*.txt 2>/dev/null | head; grep -n -i 'mons[ou]on\\|mousson\\|monção\\|mongao' DEV.txt PHN.txt LAM.txt DOZ.txt | head"
}
```


### [2026-10-17T00:02:39.020Z] TOOL RESULT

```
14511:MONSOON.
14518:MONSOON,  8.  The  name  given  to the  periodical  winds  of  the  Indian seas,  and  of  the  seasons  which  they affiect  and  characterize.  The  original word  is  the  Ar.  mavMm,  'season,' which  the  Portuguese  corrupted  into monfdo,  and  our  people  into  monsoon. Dictionaries  (except  Dr.  Badger's)  do not  apparently  give  the  Arabic  word maustm  the  technical  sense  of  monsoon. But  there  can  be  no  doubt  that  it  had that  sense  among  the  Arab  pilots  from 2  0
14519:whom  the  Portuguese  adopted  the word.  This  is  shown  by  the  quota- tions from  the  Turkish  Admiral  Sidi 'Ali.  "The  rationale  of  the  term  is well  put  in  the  Beirut  MoJuU,  which says :  *  Maiusim  is  used  of  anything that  comes  round  but  once  a  year,  like the  festivals.  In  Lebanon  the  mausim is  the  season  of  working  with  the  silk,' — which  is  the  important  season  there, as  the  season  of  navigation  is  in Yemen."    {IV.  R.  S.)
14525:MONSOON.
(eval):1: no matches found: PLA*.txt
LAM.txt:693:avec n (5) : Zénith, albotin, mousselin, mousson, semoun,
LAM.txt:718:langa) ; avecm : sumbul, ambre, mousson. «La langue portu-
LAM.txt:938:Uj : goum, mousseline, mousson, muse, musacée, ben-
LAM.txt:5489:Mousson. Esp : monzon. Ptg: mouçaô. Il .-mussone de
LAM.txt:5496:de mausel. — h Mousson, mot qui vient de l'arabe et signifie saison parce
LAM.txt:9518:Mousson
PHN.txt:7709:MOUSSON, s. f. (a.)
PHN.txt:7718:sone, les Portugais monçao, et les Anglais monsoon.
PHN.txt:10750:Mousson , s. f. (a.) 976
DEV.txt:1800:Mousson.  On  a  dit  aussi  nionson.  Esp.  monzon,  portug. monçào,  ital.  mussone.  De  l'arabe  rt\*,y>  mausim ,  époque  fixe, fête,  foire,  et  aussi  ç^ saison  favorable  pour  le  voyage  des Indes  ^.??  Les  habitants  de  l'archipel  Indien  prononcent moûsim  et  emploient  le  mot  dans  le  sens  de  saison,  comme dans  cet  exemple  que  je  prends  dans  le  Makota  radja,  un des  ouvrages  les  plus  estimés  de  la  littérature  malaise  :
```


## [2026-10-17T00:02:44.435Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; timeout 300 python3 tools/ref_page.py BQT:1781 --image 2>&1 | tail -60"
}
```


## [2026-10-17T00:02:46.171Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n 'گرازید' incoming/ARY/ARY_pages.txt | head; grep -n -i 'GORAZ\\|GORÂZ\\|GORĀZ' incoming/ARY/ARY_latin_index_pages.txt | head; grep -n -i 'monssoen\\|moesson\\|monsoen' DOZ.txt | head; grep -n 'گرازید' incoming/BQT/BQT_v3_pages.txt | head"
}
```


### [2026-10-17T00:02:46.506Z] TOOL RESULT

```
IMAGE: /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT/1781.png
REF: BQT:1781  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 578  OCR-lang: fas

-۱۷۸۱- کران‌پشت
گرا رد۱ < بروز ن کدازد » بمنی‌جلوه گراشیدن* » بروزنومعنی‌خراشیدن
کند واز روی از وتکیر بخرامد وبراه رود . باشد- وبمعنی پربشان شدن وکردن هم آمده
گر از نده۲ - بروزن گدازنده, ازروی | است .
تاز وتکبر خرامنده وبراه رونده راآکوبند . گرامی۱۰ * بر وزن نظامی » بمه‌نی
گراذه؟۴ - بنم اول وفتح رابع »۰ نام عزیز ومکرم ومحبوب وبز رکه باشد -
پهلوانی است ایرانی که در جنکه دوازده رخ گر ان - بکر اول بروزن نشان. نقیل
سبامك رابقتل آوردگ - وخوك‌نررا هم‌میگوبند | وسنگین باشد که در مقابل‌خفیف وسبك‌است۹۱-
که کراز باشد ۴ . ودر مقابل ارزان هم هت؟۴٩‏ - وضم اول دستهة
گر از یدن* * بروزن شماریدن, بناز کندم وجودرو کرده را گوبند که‌باخوشه‌باشد۹۴.
وتکبی وغمزه براه رفتن وخرامیدن باشد. گر آن‌باد - بابای‌ابجد پروزن‌نشانداره
گر اس۱ < بفتح اول بر وزن هراس , | بمعنی باردار وبازور باشد اعم از درخت وحیوان
بممنی تکه ونواله باشد وبعریی لقمه کوبند۷ . | وانان - وشخصی را نیز کویند که مال واسباب
گراش۸ - بروزن ومعنی خرائی باشد وبته وغنایم بسبار داشته باشد - وکنابه‌ازاسان
که ازخراشیدن‌است - وبمعتی پریشان‌وپرا کنده وحیوان آبتن هم هت .
هم هست. . گران پشت - بکر اول و ضم بای
۱ - مضارع از «گرازیدن» (هم.) . ۴ - اسم فاعل از «گرازیدن > ۰
۳ < کراز (هم.) . ۴ - وی ازخاندان کیو بود" رك: فهرست ولف ۰
8 - از : کراز میدن (پسوند مصدری ) ؛ هندی باستان - [۷۳۵ , ۷۲۸[811 ( قدم
نهادن ۰ رفتن) «اسشق 2۸۹۷ ورك : هوبشمان » اس ۰
باغ ملك ترا مباد خزان تا درو چون بهار بگرازی .
آ#وری آبیوردی «رشیدی» .
‎٩‏ - در خراسان کراسه ( با ضم اول ) بمعنی باقی مانده طمام است .
۷ - جمله‌نستهای الوان بهشت يك کرای ازخوان اسان تونیست.
غنایری رازی «جهانگیری » .
۸ - ر4 : خراش * غراش » ورك : کراش . ‎٩‏ - رك : خراعیدن * غراشیدن +
ورك : کراشیدن ۰ ۰ در پهلوی 82۳2016 ( عزیز» معزز ) از : 8872:
پذیره فزستاد خرو سوار کرانمایگان کرامی هزار .
فردوسی طوسی «شاهنامةٌ بخ ج٩‏ ص ۰4۲۷۹۳
رك : اضافه بقلم نگارنده چ ۱ پایان کتاب ص نله بیعد .
۱- پهلوی 82728 (سنگین . تقیل) » ازاوستا - 801۲1 از- 8871 «بارتولمهع ۰۵۱
۶ انیب رکه ص ۷۸ پارسی باستان 7 - 87382 5 « هوبشمان ۸۹۸ ورك : اسشق۸۹۸؛
کردی 8101138 ( نقیل کران » سخت ) « ژابا ۳۵۸ > : « فی‌الجمله بانواع عقوبت کرفتار
آمدم , تا درین اهفته که مژدة سلامت حجاج برسید » از بند کرام خلاس کرده ( ملك ) .>
«کلتان ص ۳۸ . ۴- کیلکی81۳28. :
۴- بك کران از کشت زارخوشتن بهتر از صد خرمن مال کان.
غضابری رازی «رشیدی» .
```


### [2026-10-17T00:02:46.657Z] TOOL RESULT

```
168:beteekenis hebben ontvangen, zooals moesson, soebatten,
42153:۱- مصدر ‎OT‏ «گرازیدن» است .
42258:۱ - منارع از « گرازیدن» («م.) .
```


## [2026-10-17T00:02:59.224Z] TOOL CALL #20: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT/1781.png"
}
```


### [2026-10-17T00:03:00.026Z] TOOL RESULT

```

```


## [2026-10-17T00:03:00.023Z] INPUT

[Image: original 1650x2546, displayed at 1296x2000. Multiply coordinates by 1.27 to map to original image.]


## [2026-10-17T00:03:10.165Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; cat > data/verification/sources/refs/ocr/BQT/1781.vision.txt <<'E'\n[BQT p. 1781, vol. 3, pdf page 578 — read from the image]\nگرازد(۱) - بروزن گدازد، یعنی جلوه کند و از روی ناز و تکبر بخرامد و براه رود.\nگرازنده(۲) - بروزن گدازنده، از روی ناز و تکبر خرامنده و براه رونده را گویند.\nگرازه(۳) - بضم اول و فتح رابع، نام پهلوانی است ایرانی که در جنگ دوازده رخ سیامک را بقتل آورد(۴) - و خوک نر را هم میگویند که گراز باشد(۳).\nگرازیدن(۵) - بروزن شماریدن، بناز و تکبر و غمزه براه رفتن و خرامیدن باشد.\nFootnotes:\n۱ - مضارع از «گرازیدن» (ه.م.). ۲ - اسم فاعل از «گرازیدن».\n۵ - از: گراز + یدن (پسوند مصدری)؛ هندی باستان vraj ، vrájati (قدم نهادن، رفتن) «اسفق ۸۹۷» ورك: هوبشمان، ایضاً.\n  باغ ملك ترا مباد خزان / تا درو چون بهار بگرازی. انوری ابیوردی «رشیدی».\nE\nfor u in 'https://en.wiktionary.org/wiki/%DA%AF%D8%B1%D8%A7%D8%B2%DB%8C%D8%AF%D9%86' 'https://en.wiktionary.org/wiki/gar%C3%A7on' 'https://www.etymonline.com/word/gasket' 'https://www.etymonline.com/word/monsoon' 'https://www.etymonline.com/word/urge' 'https://en.wiktionary.org/wiki/%D9%85%D9%88%D8%B3%D9%85' 'https://en.wiktionary.org/wiki/%D9%88%D8%B3%D9%85%D9%87' 'https://en.wiktionary.org/wiki/%D8%B3%D9%85%D8%AA' 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/wreg-' 'https://en.wiktionary.org/wiki/garcette' 'https://en.wiktionary.org/wiki/%DA%AF%D8%A7%D8%B1%D8%B3%D9%86' 'https://en.wiktionary.org/wiki/mon%C3%A7%C3%A3o'; do timeout 90 python3 tools/fetch_source.py \"$u\" --note 'page 557, roots Wreg 1 / W.s.m: etymology check' 2>&1 | tail -2; done"
}
```


### [2026-10-17T00:03:15.231Z] TOOL RESULT

```
/home/sfmqrb/git/rishe-private/data/verification/sources/web/b79160d3397a7d06.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/1e8df2be392896a3.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/88e7661aa3d3a312.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/1e388e942131bc9f.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/3a1dbe9141356c5b.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/276bb36e60250a37.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/16ba8e40a09ea1b2.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/140845579911c711.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/229baeef0ea14b44.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/56f9da152582c714.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/05169134579d75e2.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/7d14394b4dd3bc8e.txt
```


## [2026-10-17T00:03:18.554Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; for f in b79160d3397a7d06 1e8df2be392896a3 88e7661aa3d3a312 1e388e942131bc9f 3a1dbe9141356c5b 276bb36e60250a37 16ba8e40a09ea1b2 140845579911c711 229baeef0ea14b44 56f9da152582c714 05169134579d75e2 7d14394b4dd3bc8e; do echo \"##### $f $(wc -c <$f.txt)\"; grep -i -m8 -A3 'etymology\\|from \\|borrowed' $f.txt | head -30; done"
}
```


### [2026-10-17T00:03:19.127Z] TOOL RESULT

```
##### b79160d3397a7d06 2214
 Etymology 

 1.2 
 Verb 
--
 From Wiktionary, the free dictionary

 Persian
 [ edit ] 
--
 Etymology
 [ edit ] 

 Cognate with Sanskrit व्राज ( vrāja , “ motion, going, movement ” ) .
--
 Retrieved from " https://en.wiktionary.org/w/index.php?title=گرازیدن&oldid=46967781 "

 Categories : Persian lemmas 
 Persian verbs 
##### 1e8df2be392896a3 14821
 Etymology 

 1.3 
 Pronunciation 
--
 Etymology 

 2.2 
 Pronunciation 
--
 Etymology 

 3.2 
 Noun 
--
 Etymology 

 4.2 
 Pronunciation 
--
 Etymology 

 5.3 
 Pronunciation 
--
 Etymology 

 6.3 
 Noun 
--
##### 88e7661aa3d3a312 133
##### 1e388e942131bc9f 134
##### 3a1dbe9141356c5b 131
##### 276bb36e60250a37 11330
 Etymology 

 1.2 
 Pronunciation 
--
 Etymology 

 2.2 
 Pronunciation 
--
 Etymology 

 3.2 
 Pronunciation 
--
 Etymology 

 4.2 
 Noun 
--
 From Wiktionary, the free dictionary

 Arabic
 [ edit ] 
--
 Etymology
 [ edit ] 

 From a root meaning "to become suitable, fitting," compare Hebrew מזומן ( “ currency ” ) , סיוון ( “ Sivan ” ) , Arabic وسم ( “ to mark ” ) . [ 1 ] 

##### 16ba8e40a09ea1b2 3343
 Etymology 

 2.2 
 Pronunciation 
--
 From Wiktionary, the free dictionary

 See also: وسمة and وسمہ 

--
 Etymology
 [ edit ] 

 Borrowed from Arabic وَسْمَة ( wasma ) .

 Pronunciation
 [ edit ] 
--
 Retrieved from " https://en.wiktionary.org/w/index.php?title=وسمه&oldid=88097929 "

 Categories : Azerbaijani variant lemmas 
 Azerbaijani terms in Arabic script 
 Persian terms borrowed from Arabic 
 Persian terms derived from Arabic 
 Persian terms with IPA pronunciation 
 Rhymes:Persian/a 
 Rhymes:Persian/a/2 syllables 
##### 140845579911c711 9820
 Etymology 1 

 1.1.1 
 Noun 
--
 Etymology 2 

 1.2.1 
 Verb 
--
 Etymology 3 

 1.3.1 
 Verb 
--
 Etymology 4 

 1.4.1 
 Verb 
--
 Etymology 5 

 1.5.1 
 Verb 
--
 Etymology 

 2.2 
 Pronunciation 
--
##### 229baeef0ea14b44 6885
 From Wiktionary, the free dictionary

 This Proto-Indo-European entry contains reconstructed terms and roots . As such, the term(s) in this entry are not directly attested , but are hypothesized to have existed based on comparative evidence.

--
 Terms derived from the Proto-Indo-European root *wreg- (30 c, 0 e) 

 *wrég-e-ti ( thematic root present ) [ 2 ] [ 5 ] [ 7 ] 
 Proto-Balto-Slavic: [ 8 ] 
--
 ↑ 10.0 10.1 Adams, Douglas Q. ( 1999 ), “ werke* ”, in A dictionary of Tocharian B (Leiden Studies in Indo-European; 10 ), Amsterdam, Atlanta: Rodopi, →ISBN , page 664 : “ PTch *werke (as if) from a PIE *worKo- ” 

 Retrieved from " https://en.wiktionary.org/w/index.php?title=Reconstruction:Proto-Indo-European/wreg-&oldid=92078946 "

 Categories : Proto-Indo-European lemmas 
 Proto-Indo-European roots 
##### 56f9da152582c714 2901
 Etymology 

 2.2 
 Noun 
--
 From Wiktionary, the free dictionary

 English
 [ edit ] 
--
 ( historical ) A French women's hairstyle from the 16th century where the hair was pulled back over the forehead.

 ( historical ) A whip made of braided rope.

--
 Etymology
 [ edit ] 

 Inherited from Middle French garcette ( “ gasket ” ) , from Old French garce ( “ young woman ” ) , a feminization of garçon .

 Noun
 [ edit ] 
--
 Retrieved from " https://en.wiktionary.org/w/index.php?title=garcette&oldid=79291288 "

 Categories : English lemmas 
 English nouns 
--
 French terms inherited from Middle French 
 French terms derived from Middle French 
##### 05169134579d75e2 156
##### 7d14394b4dd3bc8e 4658
 Etymology 

 1.3 
 Pronunciation 
--
 From Wiktionary, the free dictionary

 See also: monçaõ and Monção 

--
 Etymology
 [ edit ] 

 Borrowed from Arabic مَوْسِم ( mawsim ) . [ 1 ] [ 2 ] 

 Pronunciation
 [ edit ] 
--
 → Norwegian: ( or borrowed directly from Portuguese ) monsun Norwegian Bokmål: monsun Norwegian Nynorsk: monsun 
 → Punjabi: Gurmukhi script: ਮੌਨਸੂਨ ( maunsūn ) , ਮਾਨਸੂਨ ( mānsūn ) Shahmukhi script: مَون سُون ( maun sūn ) 
 → Polish: monsun 
 → Serbo-Croatian: Latin script: mònsūn Cyrillic script: мо̀нсӯн 
--
 → Norwegian: ( or borrowed through English ) monsun 
 Norwegian Bokmål: monsun 
 Norwegian Nynorsk: monsun 

--
 Retrieved from " https://en.wiktionary.org/w/index.php?title=monção&oldid=92190994 "
```


## [2026-10-17T00:03:23.316Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; grep -n -i 'wrakj\\|frankish\\|gars' 1e8df2be392896a3.txt | head; grep -n -i 'vraj\\|urge\\|wrak\\|uruuaj\\|Iranian' 229baeef0ea14b44.txt | head -20; grep -n -i 'وسم\\|mawsim\\|season' 140845579911c711.txt | head; grep -n -i 'وسم\\|wasama\\|Arabic' 276bb36e60250a37.txt | head; grep -n -i 'Arabic\\|سمة' 140845579911c711.txt | head -5; cat 05169134579d75e2.txt"
}
```


### [2026-10-17T00:03:23.648Z] TOOL RESULT

```
329: Proto-Germanic *wrakjô 
330: Frankish *wrakkjō bor. 
337: From French garçon   m (1788), from Old French garçon , oblique case of gars ( “ servant ” ) , from Medieval Latin garciō   m , from Frankish *wrakkjō ( “ servant, boy ” ) , from Proto-Germanic *wrakjô ( “ exile, driven one ” ) , from Proto-Indo-European *wreg- ( “ to drive ” ) . Doublet of garson and wretch .
371: Georgian: გარსონი ( garsoni ) , ოფიციანტი ( opicianṭi ) 
375: Russian: гарсо́н   (ru)   m ( garsón ) 
448: Inherited from Middle French garçon , from Old French garçon , garçun   m ( “ servant, boy ” ) , from Early Medieval Latin garciōnem , accusative of garciō   m ( “ mercenary, servant, boy ” ) , from Frankish *wrakkjō ( “ servant, boy ” ) , from Proto-Germanic *wrakjô ( “ exile, driven one ” ) . Cognate with Modern German Recke ("warrior"), Old English wreċċa ( “ exile, outcast ” ) , whence Modern English wretch .
515: Guianese Creole: garson 
519: Mauritian Creole: garson 
521: Réunion Creole French: garson 
523: Seychellois Creole: garson 
157: Proto-Indo-Iranian: *wráǰati 
162: Proto-Indo-Iranian: *Háwrākšat 
163: Proto-Iranian: *Háwrāxšat 
167: Proto-Germanic: *wrakjaną ( see there for further descendants )
169: Proto-Indo-Iranian: *wrāǰáyati 
175: > ? Latin: urgeō ( “ to urge, pressure ” ) ( disputed [ 9 ] ) ( see there for further descendants )
208: ^ Lubotsky, Alexander ( 2011 ), “vraj”, in The Indo-Aryan Inherited Lexicon (in progress) (Indo-European Etymological Dictionary Project), Leiden University, page 596 : “ Proto-Indo-Iranian: (H)uarg- / (H)uarǰ- ” 
210: ↑ 9.0 9.1 De Vaan, Michiel ( 2008 ), “ urgeō ”, in Etymological Dictionary of Latin and the other Italic Languages (Leiden Indo-European Etymological Dictionary Series; 7), Leiden, Boston: Brill, →ISBN , page 644 
4:TITLE: موسم - Wiktionary, the free dictionary
6:موسم - Wiktionary, the free dictionary 
57: Arabic 
59: Toggle Arabic subsection 
138: موسم 
217: Arabic
229: From a root meaning "to become suitable, fitting," compare Hebrew מזומן ( “ currency ” ) , סיוון ( “ Sivan ” ) , Arabic وسم ( “ to mark ” ) . [ 1 ] 
457: Borrowed from Arabic مَوْسِم ( mawsim ) .
498: موسم • ( mawsim / mowsem ) ( plural ممواسم ( mawāsim / mavâsem ) , Tajik spelling мавсим ) 
527: Urdu: مَوسَم ( mausam ) → Ushojo: موسم ( mōsam ) 
57: Arabic 
59: Toggle Arabic subsection 
190: Arabic
193: Arabic Wikipedia has an article on: سمت 
200: From Aramaic סֵימִטָא ( sēmiṭā ) from Latin sēmĭta , but later reanalysed as deriving from an Arabic root س م ت ( s m t ) which contains only denominal verbs however.
URL: https://en.wiktionary.org/wiki/%DA%AF%D8%A7%D8%B1%D8%B3%D9%86
FETCHED: 2026-10-17T00:03:14Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 404: Not Found
```


## [2026-10-17T00:03:30.039Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; sed -n 215,260p 276bb36e60250a37.txt | grep -v '^\\s*$' | head -30; grep -n -i 'persian' -A12 140845579911c711.txt | grep -i -v '^\\S*-\\s*$' | sed -n 1,60p | grep -i 'sima\\|سمة\\|rank\\|position\\|borrowed\\|semat' "
}
```


### [2026-10-17T00:03:30.585Z] TOOL RESULT

```
 From Wiktionary, the free dictionary
 Arabic
 [ edit ] 
 Root 
 و س م ( w s m ) 
 13 terms 
 Etymology
 [ edit ] 
 From a root meaning "to become suitable, fitting," compare Hebrew מזומן ( “ currency ” ) , סיוון ( “ Sivan ” ) , Arabic وسم ( “ to mark ” ) . [ 1 ] 
 Pronunciation
 [ edit ] 
 IPA ( key ) : /maw.sim/ 
 ( Moroccan ) IPA ( key ) : /muː.sim/ , /maw.sim/ 
 Noun
 [ edit ] 
 مَوْسِم • ( mawsim )  m ( plural مَوَاسِم ( mawāsim ) ) 
 season 
 festive season (especially, the hajj period)
 festival , holiday 
 fair 
 fixed date , deadline 
 harvest 
 ( broadcasting , television ) season ( of a program ) 
 Declension
 [ edit ] 
 Declension of noun مَوْسِم ( mawsim )
486- Borrowed from Arabic سَمْت ( samt ) .
547- Arabic terms borrowed from Aramaic 
559: Persian terms borrowed from Arabic
```


## [2026-10-17T00:03:33.750Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; for w in سمت وسمه وسم موسم گارسن گارسون گرازیدن; do u=\"https://vajehyab.com/moein/$(python3 -c \"import urllib.parse,sys;print(urllib.parse.quote(sys.argv[1]))\" $w)\"; timeout 90 python3 tools/fetch_source.py \"$u\" --note \"page 557: Mo'in entry for $w\" 2>&1 | tail -1; done"
}
```


### [2026-10-17T00:03:37.218Z] TOOL RESULT

```
/home/sfmqrb/git/rishe-private/data/verification/sources/web/1e4d8cd4606ffa79.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/b29af2106f0c8df7.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/7ee1e1643f368f66.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/0f9f2182c4f33305.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/a16f3c7b9419a4c1.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/6aa6a4c2060884ce.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/05c260dc1b3dade1.txt
```


## [2026-10-17T00:03:40.238Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; for f in 1e4d8cd4606ffa79 b29af2106f0c8df7 7ee1e1643f368f66 0f9f2182c4f33305 a16f3c7b9419a4c1 6aa6a4c2060884ce 05c260dc1b3dade1; do echo \"##### $f\"; head -3 $f.txt | tail -1; grep -n 'معین\\|\\[ع\\|\\[فر\\|\\[ په\\|(اِ\\|(مص' $f.txt | head -8; done"
}
```


### [2026-10-17T00:03:41.299Z] TOOL RESULT

```
##### 1e4d8cd4606ffa79
STATUS: 200
4:TITLE: معنی سمت | فرهنگ انتشارات معین | واژه یاب
6:معنی سمت | فرهنگ انتشارات معین | واژه یاب 
16: فرهنگ انتشارات معین
17: (سَ) [ ع . ] 1 - (مص ل .) راهی را در پیش گرفتن . 2 - به راه درست و میانه راه رفتن . 3 - (اِ.) راه ، روش . 4 - قصد. 5 - طرف ، جانب . ج . سموت .
##### b29af2106f0c8df7
STATUS: 200
4:TITLE: معنی وسمه | فرهنگ انتشارات معین | واژه یاب
6:معنی وسمه | فرهنگ انتشارات معین | واژه یاب 
16: فرهنگ انتشارات معین
17: (وَ مِ) [ ع . وسمة ] (اِ.) گیاهی است با برگ هایی شبیه برگ مورúد که پس از رسیدن سیاه می شود و از آن برای رنگ کردن ابرو استفاده می کردند.
##### 7ee1e1643f368f66
STATUS: 200
4:TITLE: معنی وسم | فرهنگ انتشارات معین | واژه یاب
6:معنی وسم | فرهنگ انتشارات معین | واژه یاب 
16: فرهنگ انتشارات معین
17: (وَ) [ ع . ] 1 - (اِ.) داغ و نشان . 2 - (مص م .) داغ کردن ، نشان کردن .
##### 0f9f2182c4f33305
STATUS: 200
4:TITLE: معنی موسم | فرهنگ انتشارات معین | واژه یاب
6:معنی موسم | فرهنگ انتشارات معین | واژه یاب 
16: فرهنگ انتشارات معین
17: (مَ س ) [ ع . ] (اِ.) 1 - زمان ، هنگام . 2 - فصل .
##### a16f3c7b9419a4c1
STATUS: -1
##### 6aa6a4c2060884ce
STATUS: 200
4:TITLE: معنی گارسون | فرهنگ انتشارات معین | واژه یاب
6:معنی گارسون | فرهنگ انتشارات معین | واژه یاب 
16: فرهنگ انتشارات معین
17: (سُ) [ فر. ] (اِ.)= گارسن :پیشخدمت در رستوران ها.
##### 05c260dc1b3dade1
STATUS: 200
4:TITLE: معنی گرازیدن | فرهنگ انتشارات معین | واژه یاب
6:معنی گرازیدن | فرهنگ انتشارات معین | واژه یاب 
16: فرهنگ انتشارات معین
17: (گُ دَ) (مص ل .) خرامیدن ، به ناز راه رفتن .
```


## [2026-10-17T00:03:44.701Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; grep -n 'سِ\\|سمة\\|مقام\\|عنوان' 1e4d8cd4606ffa79.txt | head; cd /home/sfmqrb/git/rishe-private; timeout 90 python3 tools/fetch_source.py \"https://vajehyab.com/dehkhoda/$(python3 -c \"import urllib.parse;print(urllib.parse.quote('سمت'))\")\" --note \"page 557: Dehkhoda سمت (semat < Ar. sima)\" | tail -1"
}
```


### [2026-10-17T00:03:45.680Z] TOOL RESULT

```
/home/sfmqrb/git/rishe-private/data/verification/sources/web/ea542420ebde35a1.txt
```


## [2026-10-17T00:03:47.136Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; grep -n 'سِ\\|سمة\\|مقام\\|عنوان\\|وسم' ea542420ebde35a1.txt | head -15"
}
```


### [2026-10-17T00:03:47.489Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-17T00:03:50.091Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; head -30 ea542420ebde35a1.txt; cd ..; cd /home/sfmqrb/git/rishe-private; timeout 90 python3 tools/fetch_source.py \"https://abadis.ir/fatofa/$(python3 -c \"import urllib.parse;print(urllib.parse.quote('سمت'))\")/\" --note \"page 557: abadis سمت (Mo'in/Dehkhoda; semat < Ar. sima)\" | tail -1"
}
```


### [2026-10-17T00:03:51.778Z] TOOL RESULT

```
URL: https://vajehyab.com/dehkhoda/%D8%B3%D9%85%D8%AA
FETCHED: 2026-10-17T00:03:45Z
STATUS: 200
TITLE: معنی سمت | لغت‌نامه دهخدا | واژه یاب

معنی سمت | لغت‌نامه دهخدا | واژه یاب 

 26 فرهنگ 

 همه دیکشنری مترادف طیفی آزاد + 

 همه دقیق مترادف متضاد مشابه آوا متن آغاز قافیه 

 سمت

 لغت‌نامه دهخدا
 سمت . [ س َ م َ ] (اِ) سَمَد. نامی که در طوالش و اطراف رشت به اوجا دهند. رجوع به اوجا شود. (یادداشت بخط مؤلف ).

 سمت در فرهنگ‌های دیگر
 معنی سمت در فرهنگ انتشارات معین 
 معنی سمت در فرهنگ فارسی عمید / قربان‌زاده 
 معنی سمت در دیکشنری عربی به فارسی 
 معنی سمت در دیکشنری فارسی به عربی 
 معنی سمت در دیکشنری فارسی به انگلیسی 
 معنی سمت در دیکشنری فارسی به ترکی 
 معنی سمت در واژه‌های مصوب فرهنگستان 
 معنی سمت در فرهنگ مترادف و متضاد 
 معنی سمت در فرهنگ سره 
 معانی دیگر سمت
 سمت (2) 
/home/sfmqrb/git/rishe-private/data/verification/sources/web/ada3ebf7dc6b1632.txt
```


## [2026-10-17T00:03:53.480Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; grep -n 'سِ\\|سمة\\|مقام\\|عنوان\\|وسم\\|نشان' ada3ebf7dc6b1632.txt | head -20"
}
```


### [2026-10-17T00:03:54.171Z] TOOL RESULT

```
13: مترادف سمت : جانب، جهت، سو، طرف، ناحیه، صورت، فرم، هیئت | شغل، عنوان، مقام، منصب، نشان، علامت، اثر داغ، داغ جا
14: برابر پارسی : پایه، رده، جاه، سو، سوی، پایگاه، راستا، راسته، رو | ( سِمت ) پایگاه، پایه، جاه، رده
21: سمت. [س َ ] ( ع اِ ) طرف. سوی. ( ناظم الاطباء ) : نه راه سوی مقصدی بیرون توانستم برد و نه بر سمت راه حق دلیلی و نشان یافتم. ( کلیله و دمنه ). || نزد. || جانب و کنار. ( ناظم الاطباء ). جانب. ( غیاث ) ( آنندراج ). || ناحیه. ولایت. کشور. محله. وطن. || راه. طریق. ( از ناظم الاطباء ). راه و روش نیکو. ( منتهی الارب ). راه راست و روش نیکو. ( غیاث ) ( از آنندراج ). || ( اصطلاح نجوم ) زاویه ای که حاصل میشود از تلاقی دایره نصف النهاربا سطح عمودی کوکبی. ( ناظم الاطباء ) ( از تعریفات ).
25: سمت. [ س ِ م َ ] ( ع اِ ) سمة. قرابت و خویشی. ( ناظم الاطباء ). || رتبه. مقام : و دانستیم رأی هند که این جمع بنام او کرده اند سمت پادشاهی است. ( کلیله و دمنه ).
29:|| راه و روش. ( ناظم الاطباء ) : اگر شما بر سمت تدبیر من نروید سخن مرا نامؤثر شناسید، بشما همان رسد که ببوزینگان رسید. ( سندبادنامه ص 80 ). و از سمت راستی بیفتند. ( سندبادنامه ص 5 ). || داغ. نشان. ( غیاث ) ( آنندراج ) : شمس المعالی قابوس بسمت عدل و رأفت و انصاف و معدلت آراسته بود. ( ترجمه تاریخ یمینی ). خود را بسمت قصور و تقصیر منسوب و موسوم نگردانم. ( ترجمه تاریخ یمینی ). رجوع به سمة شود. بیشتر بخوانید ... 
33: نشان، علامت، اثرداغ، عنوان، سمات جمع، راه وروش، میانه راه، طریق، طرف وجانب، سموت جمع
34:( اسم ) ۱ - نشان داغ . ۲ - علامت نشانه جمع : سمات . ۳ - عنوان . ۴ - مقام : به سمت ریاست منصوب شد .
35:سمه قرابت و خویشی . یا رتبه و مقام 
40: (س مَ ) [ ع . ] (اِ. ) ۱ - نشان داغ . ۲ - علامت ، نشانه . ۳ - عنوان . ۴ - مقام . 
44: ۱. شغل، عنوان.
45:۲. علامت، نشان.
84: پست، تعجیل، مسئولیت، منصب، سمت، موقعیت، مسند، مقام، شغل، چاپار، صندوق پست، بسته پستی، پستخانه، ارسال سریع، سیستم پستی، تیر تلفن و غیره، پست نظامی، مجموعه پستی، تیردگل کشتی و امثال آن
90: راه، عنوان، سیاق، سمت، خط، سبک، جاده، رسم، مسیر، روش، طرز، طریقه، طریق، سان، طور، مسلک، نحو
100: جانب , شغل , عنوان ، اِتِّجاهٌ 
104: سِمَت: 1 - پیشه 2 - جایگاه
106: سِمَت: جایگاه، پیشه
108: " داشتن سِمَت ": حفظ سمت . 
109:" با داشتن سِمَت ": باحفظ سمَت .
132: پست و مقام
134: سِمـَت: عیب
```


## [2026-10-17T00:04:20.030Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; command ls site/pages/557.* ; timeout 90 python3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/gasket\" --note \"page 557: gasket < F garcette\" | tail -1; timeout 90 python3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/urgeo\" --note \"page 557: Latin urgeo etymology (de Vaan)\" | tail -1; timeout 90 python3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/monsoon\" --note \"page 557: monsoon < Du monssoen < Pt monção < Ar mawsim\" | tail -1"
}
```


### [2026-10-17T00:04:22.106Z] TOOL RESULT

```
site/pages/557.jpg
/home/sfmqrb/git/rishe-private/data/verification/sources/web/420e542873e1867e.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/49fa73711ce44cfc.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/139c15225e606316.txt
```


## [2026-10-17T00:04:24.370Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; grep -n -i 'garcette\\|uncertain\\|origin' 420e542873e1867e.txt | head -5; grep -n -i -A3 '^ Etymology' 49fa73711ce44cfc.txt | head -12; grep -n -i 'monssoen\\|monção\\|mawsim' 139c15225e606316.txt | head -5"
}
```


## [2026-10-17T00:04:24.738Z] TOOL CALL #33: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/site/pages/557.jpg"
}
```


### [2026-10-17T00:04:24.821Z] TOOL RESULT

```

```


### [2026-10-17T00:04:24.876Z] TOOL RESULT

```
188: Perhaps from Middle French garcette ( “ gasket ” ) , from Old French garce ( “ young woman ” ) , feminization of garçon . [ 1 ] 
235: French: garcette   (fr)   f 
65: Etymology 
66-
67- 1.3 
68- Pronunciation 
--
161: Etymology
162- [ edit ] 
163-
164- Disputed.
182: Borrowed from Portuguese monção and Dutch moesson , from Arabic مَوْسِم ( mawsim , “ season ” ) , from وَسَمَ ( wasama , “ to mark , to brand ” ) . [ 1 ] [ 2 ] 
281: Arabic: رِيَاح مَوْسِمِيَّة   pl   f ( riyāḥ mawsimiyya ) 
324: Portuguese: monção   (pt)   f 
393: Portuguese: monção   (pt)   f 
431: Portuguese: monção   (pt)   f
```


## [2026-10-17T00:04:29.172Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i 'urgeo\\|urgueo' incoming/WLD/WLD_Bd1_pages.txt | head -5; grep -n -i 'vrajati\\|vräjati' incoming/WLD/WLD_Bd1_pages.txt | head -5; grep -n -i 'urgeo\\|wrikan' IEC.txt | head -5; grep -n -i '^urge\\|^gasket\\|^wreck' SKT.txt | head; grep -n -i 'gasket' SKT.txt | head -3"
}
```


### [2026-10-17T00:04:29.705Z] TOOL RESULT

```
27457:urgeo s. u. yreg- „stoBen". Eber lit. verziii (Prelhvitz 2 335) s. vielmehr u.
30429:   Lat. urgeo (daneben friih, aber unurspriinglich urgueo), -ere ,, drangen,
30460:mann Apr. 457, Yf. LEWb. 2 u. urgeo; doch sind die bsl. Worter auch mit
67045:Yerstopfen von Wunden“ (s. bes. Solmsen IF. 26, 112 f.) turgeo -ere „auf-                  ;     ,
3511:ekKskétros, à ‘dragon, sea-monster Tokh. A (?) arsal *poison-snake'; Lat. excetra; Ir. (?) eascar, m. ‘enemy’; OCS jasterü ‘lizard’ beside jesetrü ‘sturgeon’. (Doublets also in OCz ještěr, jeSCer & jeseter; R jàščerica & osëtr); Srb. jesetra ‘sturgeon’; Li. eškētras, erškētras, eršketas & arškētas, m. id.; OPr. esketres, id.
8552:Skt. sale, mp. ‘shine’; Cz. sálat, inf. ‘shine, glow’. An uncertain variant in Lat. caleó, ere ‘be hot! is isolated, but see next entry Kaləd- (Kalod-, Kald-) ‘summer, year. (A form limited to Indo-Íran. Lat. equivalent uncertain). Cf. WP I, 429 Skt. Sarád, f. ('autumn'; in pl. 'years); Av. saroóo, m. ‘year’; Oss. sárd ‘summer’; Per. sal ‘year’; Lydian sardis, id. Uncertainly to Lat. calidus (“hot', an adj. extn. of caleo. See Kàl-) (Kalmos, is, variant of type KImos, q. v. Am- big. in OCS slama, R solóma, H szalma; MHG halm, sm. ‘stalk, haulm'; Du. helm, f. ‘bentgrass’; OE healm as MHG) Kam- "do act, toil, languish’. Cf. kam- (1) and cf. WP I, 387. (Gk. ambig.) Skt. Samyami "be active, toil; Gk. (ambig.) kámno, adj: kmetós (Doric -a-) (make; toil; languish’. Two wds? See kam- (1)); Mod. Gk. kámo ‘do’; Lat. cf. (?) camillus, -a “serving youth or maid at sacrifice) beside (?) camena *poetry, song” (speculations in WH:LEW & EM DELL). (Li. kamuoti, v. ‘weary, bother’ indicates *kam-) Kamios, io “peg, crook, yoke-peg, pintle'. See next Skt. Sámyà, f., yuga-Samyám, n. *yoke-peg'; Arm. sami, -vo, -vov ‘pole, rudder, beam’; samik, pl. form “yoke-peg'; Gk. cf. kámax, -akos “stake, pole, shaft ' Kamos, us (1) “with crumpled or broken horn'. Cf. WP I, 386 and Kamios above Skt. śámah ‘hornless’; Lat. camus, camur & camurus ‘with bent horn’; cf. Gallo-Lat. camox ‘chamois’. (For Lat. camur see WP I, 349) Kamos (2) ‘a fish’ W cf. cem-yw, pl. -ywion, m. ‘male salmon’; G cf. Ham-butte ‘halibut: R som “silure, sheat’; Li. šamas, id.; Latv. sams, id.; Finn. LW cf. sampi ‘sturgeon’ (?) (Kan- (1), variant of type kan-, see kanið and cf. kon-. Gk. ambig. Av. san- ‘destroy’; Gk. kaíno, fut. kanó ‘kill’. Ambig. cf. kanið in view of Cz. kon-, etc.) Kan- (2) ‘sing, hum, bark, echo’. Cf. WP I, 351 Tokh. A. kan ‘melody, rhythm’; Gk. cf. ei-
12330:orsó, ið (1) ‘thrust, stab’. Cf. rs-, rstis Skt. cf. cpd. an-arsàmi, v. (2) ‘thrust, stab, kill beside rsami, id.; Av. arəš-, v. ‘stab’; Arm. cf. h-arem (thrust in, fix, stab', fr. *en-ors-), cf. also v-arsem, v. id. (initial cons. of obscure origin); Hitt. arsai(mi), arse(mi), v. “plant; arsis, s. ‘plantation’; Cz. raSit, v. ‘burgeon’; Srb. (alleged) ra3iti se, v. ‘mate
14918:rà- Skt. cf. rjáb, adj. ‘rapid’; Gk. argós, adj. id.; Lat. cf. urgeo, ere, beside urgueo, ere (press, urge, hasten’. Ambig. cf. ur&-); EME to irk, v. (ambig., cf. ON orka & yrkja, v. ‘work, per- form’, fr. *ur&-, but semantics obscure)
19067:trug- (1) “press; pressure' (also: 'desicca- tion'?). Cf. WP I, 731, 761; II, 642 Gk. trügo, v. ‘dry’; trüge, f. “dried fruit or grain’; Ir. trogh, m. ‘incipient pang at birth"; W trw, m. (2) 'pervasion'; OHG druc, m. *pres- sure’ beside drucken, v. squeeze, hurt; OS thrukkian, id.; OE broc, m. (2) 'socket of plowshare'; pryccan, v. “crush, oppress’; EME to thrutch, tr. ‘press — cheese’; Du. drukken, v. ‘press’; druk, m. ‘pressure’; cf. also Gk. trüx, gs: trugós, f. ‘lees; Lat. turgeo, ere, v. ‘be full. Variant in Icel. brüga, f. (2) *wine- press; grape’. See trügh-
3748:Urge  lUioe.     Der.  t^hstal,
```


## [2026-10-17T00:04:32.958Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 30418,30436p incoming/WLD/WLD_Bd1_pages.txt; awk 'NR<30429 && /\\[pdf page/ {l=$0} END{print l}' incoming/WLD/WLD_Bd1_pages.txt; grep -n -i 'wrikan\\|wrecan\\|wrekan' IEC.txt | head -3; sed -n 3745,3750p SKT.txt"
}
```


### [2026-10-17T00:04:33.635Z] TOOL RESULT

```
von ags. ivrecan „schreiten, gehn“ wohl aus „treiben" in intrans. AYendung
erklarbar; Persson Beitr. 501 sucht dagegen in ihnen ein mit *uer-g-
„drehen“ niiclistverwandtes *urc-g-, Gdbed. „sicli dreliend bewegen". Uber
ir. drebraing ,.ging“, Fick II
                                4
                                  287, s. Zupitza KZ. 36, 57 Anm. 1, Pedersen
 KG. II 368j.
   Lat. urgeo (daneben friih, aber unurspriinglich urgueo), -ere ,, drangen,
 drangend fortstoBen, treiben, stoBen" (obwohl auch ,.an sich pressen, uin-
 armem' kanm besser zu *uer[gh-] ,.drehen" nach Persson Beitr. 506 f. und
 friiherem            s.   Yf. LEWb. 2 s. v.).
      Got. wrihan „verfolgen", anord. rclai „treiben. jagen, verfolgen, vverfen,
 verwerfen", ags. w recan ,. drangen, treiben, raclien" (und ,,vorwarts schreiten".
320                                 (ureth:) uroth-, urath-   — uren-
s. o.).    afries.   tvreka „treiben, raehen",          as. icrecan         „rachen, strafen", ahd.

•  >Kof^,  a   summit ;
»i:^iiin{^     jttroke.       Allied    to
ktida ;  sre  Colocyuth.
Urge  lUioe.     Der.  t^hstal,
th*  tune  as  ioiostium,  a  large «t  Kome,  in  which  stouc)  a of  Ncra     The  Ital  word  is
r  (F.-L.)     M.  E-fflAwr-O.  F.
```


## [2026-10-17T00:04:35.053Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 30400,30418p incoming/WLD/WLD_Bd1_pages.txt"
}
```


### [2026-10-17T00:04:35.420Z] TOOL RESULT

```
j-ifioya rnit diss. Silbenschwund im langern Worte fortsetzen, gegen Bechtel
aaO.).    Man sucht Yermittlung mit fgijyvvfu unter Berufung auf frango:
ai.   bhanaJcfi, so            Brugmann II 2 3, 294 (zw.l unter der Annahme von Fern-
            der Figura etymologica; docli ist auch der Ablaut von ayrvui
diss. bes. in
anders als der von ggyvvfu und ist bei der Yerwandtschaft von „biegen
                                                                                                                    ‘



                                                          4
mit ..brechen" Zugehorigkeit zu ud-, uug- „biegen" (Fick 1 123, 541) noch
immer zu erwagen.

ureg- iund nerg-?) „stoBen, drangen, puffen, treiben, feindselig verfolgen".
   Ai. vielleicht vr&jati „schreitet, geht". pravrujdynti „liiBt wandern. ver-
bannt", paravrj- „YerstoBener" die Bed. von vrdjuti ist ebenso wie die
                                                         i
```


## [2026-10-17T00:06:43.813Z] TOOL CALL #37: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad; cat > /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/build-557.py <<'EOF'\nimport json\nW=\"https://en.wiktionary.org/wiki/\"\nPIE=W+\"Reconstruction:Proto-Indo-European/wreg-\"\nGORAZ=W+\"%DA%AF%D8%B1%D8%A7%D8%B2%DB%8C%D8%AF%D9%86\"\nGARCON=W+\"gar%C3%A7on\"; GARCETTE=W+\"garcette\"; GASKET=W+\"gasket\"; URGEO=W+\"urgeo\"\nMAWSIM=W+\"%D9%85%D9%88%D8%B3%D9%85\"; WASMA=W+\"%D9%88%D8%B3%D9%85%D9%87\"; SAMT=W+\"%D8%B3%D9%85%D8%AA\"\nMONCAO=W+\"mon%C3%A7%C3%A3o\"; MONSOON=W+\"monsoon\"\nV=\"https://vajehyab.com/moein/\"\nM_SAMT=V+\"%D8%B3%D9%85%D8%AA\"; M_WASMA=V+\"%D9%88%D8%B3%D9%85%D9%87\"; M_WASM=V+\"%D9%88%D8%B3%D9%85\"; M_MAWSIM=V+\"%D9%85%D9%88%D8%B3%D9%85\"\nM_GARSON=V+\"%DA%AF%D8%A7%D8%B1%D8%B3%D9%88%D9%86\"; M_GORAZ=V+\"%DA%AF%D8%B1%D8%A7%D8%B2%DB%8C%D8%AF%D9%86\"\nABADIS_SAMT=\"https://abadis.ir/fatofa/%D8%B3%D9%85%D8%AA/\"\n\nPOKq={\"src\":\"POK\",\"where\":\"p. 1181 (POK_full.txt l. 93306ff.)\",\"stance\":\"supports\",\"note\":\"'ureg- (and uerg-1) to push, drag, drive. Material: Old Indic perhaps vrajati \\\"schreitet, goes\\\"... Latin urgeo... Gothic wrikan pursue, ... Gothic wrakjan, OE wrecca \\\"exile\\\"'\"}\nWLDq={\"src\":\"WLD\",\"where\":\"Bd. I pp. 319-320 (WLD_Bd1_pages.txt l. 30416-30436)\",\"stance\":\"supports\",\"note\":\"'ureg- (und uerg-?) \\\"stoßen, drängen, puffen, treiben, feindselig verfolgen\\\". Ai. vielleicht vrájati \\\"schreitet, geht\\\"... Lat. urgeo... Got. wrikan \\\"verfolgen\\\"'\"}\nAHDq={\"src\":\"AHD\",\"where\":\"Watkins 1985 s.v. wreg- (AHD_watkins1985.txt l. 1172)\",\"stance\":\"supports\",\"note\":\"'wreg-. To push, shove, drive, track down... Germanic *wrekan... Frankish *wrakjo, \\\"one pursued, an exile,\\\" perhaps in French garce, a girl: GASKET... Latin urgēre, to urge, drive: URGE. [Pok. ureg- 1181.]'\"}\n\ne0={\"entry\":0,\"root\":\"Wreg 1\",\"verdict\":\"confirmed\",\n \"modern_form\":\"PIE *wreǵ- / *wreg- 'to push, drive, pursue, track down' (Pokorny 1181 ureg-; LIV 697; Watkins wreg-)\",\n \"note\":\"Root, label and gloss are correct (Pokorny 1181 'to push, drag, drive'; AHD 'to push, shove, drive, track down'). Cheung 2007 *u̯raj 'to go forth' sets it under PIE *u̯reg- 'pursue, trace' with Av. uruuaj- and Skt. vraj-. The Latin and Indo-Iranian members are the weaker links (Latin urgeō disputed by de Vaan; Pokorny and WP say 'vielleicht' for vrajati); the Germanic set is secure.\",\n \"note_fa\":\"ریشهٔ هندواروپایی آغازین *wreg- «راندن، هل دادن، دنبال کردن» در پوکورنی (ص ۱۱۸۱)، والده‌ـ‌پوکورنی و واتکینز با همین معنا آمده و چونگ نیز ستاک ایرانی *u̯raj «پیش رفتن» (اوستایی uruuaj-، سنسکریت vraj-) را به آن می‌برد. پس ریشه و برچسب و معنای نورایی درست است؛ تنها پیوند لاتین urgēre و پیوند فارسی «گرازیدن» محل بحث‌اند که در گره‌ها توضیح داده شده.\",\n \"sources\":[PIE],\n \"ref_check\":[{\"ref\":\"POK:1181\",\"status\":\"supports\",\"note\":\"POK_full.txt 'Root / lemma: ureg- (and uerg-1) ... Meaning: to push, drag, drive ... Page(s):1181' — exactly Nourai's root and gloss.\"}],\n \"consulted\":[WLDq,AHDq,{\"src\":\"CHEUNG\",\"where\":\"p. 438 s.v. *u̯raj (CHEUNG.txt l. 28296-28316)\",\"stance\":\"supports\",\"note\":\"'*uraj to go forth. AVESTAN: uruuaj-... SANSKRIT: vraj- to stride (RV+) ... PIE *ureg- to pursue, trace — LIV: 697 | Pok.: 1181 ... Lat. urgēre, Goth. wrikan, OE wrecan'\"},{\"src\":\"IEC\",\"where\":\"s.v. rǝg- (IEC.txt l. 14918)\",\"stance\":\"partial\",\"note\":\"Mann puts 'Lat. cf. urgeo, ere, beside urgueo \\\"press, urge, hasten\\\". Ambig. cf. urǵ-' under a separate root — no wreg- headword found (grep 'wrikan|wrecan' silent)\"}],\n \"nodes\":[\n {\"id\":1,\"lang\":\"Sanskrit\",\"words\":\"vrâj\",\"verdict\":\"confirmed\",\n  \"derivation\":\"Skt. vraj-, vrájati 'to walk, proceed, go' (RV+) continues Proto-Indo-Iranian *wráǰati < PIE *wreg-/*wreǵ- (the e-grade *wreg-e- with palatalisation of *g before *e > IIr. *ǰ > Skt. j; *e > a). The sense shift is 'drive, push on' → 'move on, go'. Pokorny and Walde-Pokorny hedge ('vielleicht'), but Cheung (with LIV 697) and Lubotsky's Indo-Aryan Inherited Lexicon (via Wiktionary) accept the connection, with Av. uruuaj- 'go forth' as the Iranian cognate.\",\n  \"derivation_fa\":\"سنسکریت vraj- / vrájati «گام برداشتن، رفتن» از هندوایرانی *wráǰati و آن از ریشهٔ هندواروپایی *wreg- «راندن» است؛ g پیش از e در هندوایرانی به ǰ (ج) کامی شده و e به a بدل گشته است. معنا از «پیش راندن» به «پیش رفتن» گراییده. پوکورنی و والده با «شاید» آورده‌اند ولی چونگ (با هم‌ریشهٔ اوستایی uruuaj-) و ویکی‌واژه آن را می‌پذیرند؛ ادعای نورایی درست است.\",\n  \"sources\":[PIE],\n  \"ref_check\":[{\"ref\":\"POK:1181\",\"status\":\"supports\",\"note\":\"'Old Indic perhaps vrajati \\\"schreitet, goes\\\", pra-vrājayati \\\"läßt wandern, verbannt\\\"' (POK_full.txt l. 93313) — supports with Pokorny's own 'perhaps'.\"}],\n  \"consulted\":[WLDq,{\"src\":\"CHEUNG\",\"where\":\"p. 438 s.v. *u̯raj\",\"stance\":\"supports\",\"note\":\"'SANSKRIT: vraj- to stride (RV+) > EWAia II: 594 ... PIE *ureg-'\"},{\"src\":\"AHD\",\"where\":\"s.v. wreg-\",\"stance\":\"silent\",\"note\":\"Watkins lists only Germanic and Latin derivatives; no Sanskrit form\"}]},\n {\"id\":2,\"lang\":\"Persian\",\"words\":\"gorâzîdan\",\"verdict\":\"plausible\",\n  \"derivation\":\"NP gorāzīdan / gurāzīdan 'to strut, walk proudly' (Ferdowsi: garāzande āhu be rāgh andarun). Horn (no. 897) and Hübschmann (§50, p. 1xx: 'gurāzīdan sich wiegend gehn, einherschreiten, skr. vraj schreiten') derive it from OIr. *wrāz- = Skt. vraj-, with Old Persian initial *vr- giving NP gur- via an anaptyctic vowel (*viraz- > gurāz-, like birinj/gurinj 'rice' < *vrinji-); IIr. *ǰ > SW Iranian z is regular (cf. *ǰan- > zadan). Mo'in (BQT 1781 n.5) repeats this (gurāz + -īdan; Skt. vraj, vrájati). However, no Middle Persian form is cited, and Cheung 2007 under *u̯raj states 'No further Ir. cognates are known', i.e. does not accept the NP verb; semantically 'strut proudly' could equally point to Av. uruuaz- 'to be proud, haughty' (Cheung *uraz). The traditional derivation is thus phonetically sound but not endorsed by the most recent verb dictionary.\",\n  \"derivation_fa\":\"«گرازیدن» (گُرازیدن) «با ناز و تکبر خرامیدن»؛ هرن (شمارهٔ ۸۹۷)، هوبشمان و معین در حاشیهٔ برهان (ص ۱۷۸۱) آن را از ایرانی باستان *wrāz- هم‌ریشه با سنسکریت vraj- «گام برداشتن» می‌دانند: vr- آغازی ایرانی با افزودن واکه به gur- رسیده (مانند «برنج/گرنج» از *vrinji-) و ج هندوایرانی در جنوب‌غربی ایران به z بدل شده است. اما صورت فارسی میانه‌ای گواهی نشده و چونگ زیر *u̯raj تصریح می‌کند که «هم‌ریشهٔ ایرانی دیگری شناخته نیست»؛ از نظر معنا پیوند با اوستایی uruuaz- «سرفراز و نازان بودن» هم ممکن است. پس ادعای نورایی با احتیاط پذیرفتنی است.\",\n  \"sources\":[GORAZ,M_GORAZ],\n  \"ref_check\":[{\"ref\":\"HRN:200\",\"status\":\"supports\",\"note\":\"Horn p. 200 (leaf 221) no. 897: 'geräziden \\\"schreiten\\\". ai. √vraj, vrájati \\\"schreiten, gehen, fortgehen\\\" (Rückert, ZDMG 10, 165).'\"},\n   {\"ref\":\"BQT:1781\",\"status\":\"supports\",\"note\":\"BQT vol. 3 p. 1781 (pdf 578; read from image, saved as ocr/BQT/1781.vision.txt): 'گرازیدن - بناز و تکبر و غمزه براه رفتن و خرامیدن باشد'; n.5: 'از: گراز + یدن (پسوند مصدری)؛ هندی باستان vraj، vrájati (قدم نهادن، رفتن) «اسفق ۸۹۷» ورك: هوبشمان'.\"}],\n  \"consulted\":[{\"src\":\"HUB\",\"where\":\"§50 (HUB.txt l. 5565-5568, 6159-6160)\",\"stance\":\"supports\",\"note\":\"'Ap. v im Anlaut vor r wird im Np. zu gu- oder bi-: gurāzīdan \\\"sich wiegend gehn, einherschreiten\\\", skr. vraj \\\"schreiten, gehn\\\"'; and 'Vokaleinschub bei ... gurāzīdan einherschreiten aus *viraz — skr. vraj'\"},\n   {\"src\":\"CHEUNG\",\"where\":\"p. 438 s.v. *u̯raj (CHEUNG.txt l. 28304-28308)\",\"stance\":\"contradicts\",\"note\":\"'*uraj to go forth. AVESTAN: uruuaj- ... SANSKRIT: vraj- ... No further Ir. cognates are known.' — the NP verb is not admitted; cf. *uraz 'to be proud, haughty' (Av. uruuaz-, l. 28334), 'evidence ... limited to Av.'\"},\n   {\"src\":\"MON\",\"where\":\"vajehyab s.v. گرازیدن\",\"stance\":\"silent\",\"note\":\"'(گُ دَ) (مص ل.) خرامیدن، به ناز راه رفتن' — meaning confirmed, no etymology online\"},\n   {\"src\":\"ARY\",\"where\":\"ARY_pages.txt / ARY_latin_index_pages.txt\",\"stance\":\"silent\",\"note\":\"grep 'گرازید' and 'GORAZ' found nothing\"},\n   {\"src\":\"PHD\",\"where\":\"PHD.txt, PHD_mackenzie.txt\",\"stance\":\"silent\",\"note\":\"grep 'wrāz|wlʾc' found no Pahlavi antecedent\"}]},\n {\"id\":3,\"lang\":\"Germanic\",\"words\":\"wrekjan; wrakjo\",\"verdict\":\"plausible\",\n  \"derivation\":\"Proto-Germanic *wrekaną 'to drive, pursue, avenge' (Goth. wrikan 'persecute', OE wrecan 'drive, expel, avenge' > wreak; ON rek 'drift, wreckage' > Anglo-Norman wrec > wreck) is the e-grade of PIE *wreg-; the o-grade gives *wrakjô 'one driven out, exile' (OE wrecca 'exile' > wretch; OS wrekkio; Frankish *wrakkjō 'servant, boy'). Both words and meanings are right in substance, but 'wrekjan' is not a standard reconstruction: it blends *wrekaną with the causative *wrakjaną (Goth. wrakjan 'pursue'); 'wreck' is a later English descendant, not the Germanic meaning.\",\n  \"derivation_fa\":\"ژرمنی آغازین *wrekaną «راندن، دنبال کردن، کین کشیدن» (گوتی wrikan، انگلیسی کهن wrecan که wreak و از راه نورس کهن rek «لاشهٔ کشتی» واژهٔ wreck از آن آمده) بالانْد e ریشهٔ *wreg- است و از بالانْد o آن *wrakjô «رانده‌شده، تبعیدی» (انگلیسی کهن wrecca > wretch، فرانکی *wrakkjō) ساخته شده. محتوای گفتهٔ نورایی درست است ولی صورت «wrekjan» آمیزه‌ای از *wrekaną و *wrakjaną است، نه بازسازی معیار؛ پس با احتیاط پذیرفتنی است.\",\n  \"sources\":[PIE,GARCON],\n  \"ref_check\":[{\"ref\":\"AHD\",\"status\":\"supports\",\"note\":\"'Germanic *wrekan in OE wrecan, to drive, expel: WREAK; b. Old Norse rek ... WRECK. II. O-grade *wrog-. 1. Germanic *wrakjōn-, \\\"pursuer, one pursued,\\\" in OE wrecca, exile: WRETCH; b. Frankish *wrakjo' (Watkins 1985 s.v. wreg-) — supports; Watkins writes *wrekan, not *wrekjan.\"}],\n  \"consulted\":[POKq,WLDq,{\"src\":\"KLN\",\"where\":\"p. 640 s.v. garçon\",\"stance\":\"supports\",\"note\":\"'prob. fr. Frankish *wrakjo, which is rel. to ... OS. wrekkio, OHG. recko, \\\"a banished person, exile\\\" ... and to E. wretch'\"}]},\n {\"id\":4,\"lang\":\"French\",\"words\":\"garcon; garcette\",\"verdict\":\"plausible\",\n  \"derivation\":\"Frankish *wrakkjō 'exile, servant' was latinised as Medieval Latin garciō (Germanic w- > Romance gu-/g-, as in guerre < *werra), giving OF gars (nominative) / garçon (oblique, -ōnem) 'servant, boy'; modern French garçon 'boy' and, from the 18th c., 'waiter' (garçon de café). Garcette is a diminutive of OF garce 'girl' (fem. of gars): 'little girl' (archaic), then nautical 'small plaited rope' and a 16th-c. hairstyle. The derivation is right, but the gloss 'waitress' for garcette is wrong — no French dictionary gives that sense (waitress = serveuse).\",\n  \"derivation_fa\":\"فرانکی *wrakkjō «تبعیدی، خدمتکار» در لاتین میانه garciō شده (w ژرمنی در زبان‌های رومی به gu-/g- بدل می‌شود، مانند guerre از *werra) و از آن فرانسوی کهن gars و حالت غیرفاعلی garçon «پسر، خدمتکار» آمده که از سدهٔ ۱۸ معنای «پیشخدمت کافه» نیز گرفته است. garcette مصغّر garce «دختر» (مؤنث gars) است به معنای «دخترک» و در دریانوردی «طناب باریک بافته». ریشه‌شناسی درست است، ولی معنای «پیشخدمت زن» که نورایی برای garcette داده نادرست است.\",\n  \"sources\":[GARCON,GARCETTE],\n  \"ref_check\":[{\"ref\":\"KLN:640,642\",\"status\":\"supports\",\"note\":\"KLN_1966 leaf 346 (p. 640): 'garçon, n. — F., \\\"boy, waiter\\\", orig. objective case of OF. gars ... prob. fr. Frankish *wrakjo'; p. 642 s.v. gasket: 'F. garcette, dimin. of garce, \\\"wench\\\", femin. to garçon, \\\"boy\\\"' — Klein glosses garcette via 'wench', not 'waitress'.\"}],\n  \"consulted\":[AHDq,{\"src\":\"DEV\",\"where\":\"DEV.txt\",\"stance\":\"silent\",\"note\":\"grep 'garçon|garcette' — not an Oriental word, not treated\"},{\"src\":\"SKT\",\"where\":\"SKT.txt\",\"stance\":\"silent\",\"note\":\"grep 'garçon|garcette|gasket' found no readable entry (OCR noisy)\"}]},\n {\"id\":5,\"lang\":\"Persian\",\"words\":\"gârson\",\"verdict\":\"confirmed\",\n  \"derivation\":\"NP gārson / gārsun 'waiter (in a restaurant)' is a 20th-century loan from French garçon (de café), entering Persian with the Qajar–Pahlavi era Europeanisation of urban hospitality; French nasal -on is rendered -on/-un.\",\n  \"derivation_fa\":\"«گارسن/گارسون» به معنای «پیشخدمت رستوران» وام‌واژه‌ای از فرانسوی garçon است که در سدهٔ بیستم همراه با رواج کافه و رستوران به شیوهٔ اروپایی به فارسی آمده؛ واکهٔ خیشومی پایانی فرانسوی به «ـن/ـون» برگردانده شده است. معین آن را با نشان [فر.] آورده؛ ادعای نورایی درست است.\",\n  \"sources\":[M_GARSON,GARCON],\n  \"ref_check\":[{\"ref\":\"MON:3164\",\"status\":\"supports\",\"note\":\"page not accessible; Mo'in's entry online (vajehyab s.v. گارسون): '(سُ) [فر.] (اِ.) = گارسن: پیشخدمت در رستوران‌ها' — same entry Nourai cites.\"}],\n  \"consulted\":[{\"src\":\"MON\",\"where\":\"vajehyab s.v. گارسون\",\"stance\":\"supports\",\"note\":\"'[فر.] ... پیشخدمت در رستوران‌ها'\"},{\"src\":\"KLN\",\"where\":\"p. 640\",\"stance\":\"supports\",\"note\":\"'garçon, n. — F., \\\"boy, waiter\\\"' (source of the loan)\"},{\"src\":\"ARY\",\"where\":\"ARY_pages.txt\",\"stance\":\"silent\",\"note\":\"not an IE-root headword in Aryanpur (French loan)\"}]},\n {\"id\":6,\"lang\":\"English\",\"words\":\"gasket\",\"verdict\":\"plausible\",\n  \"derivation\":\"English gasket (1620s 'gassit', 'small cord securing a furled sail to a yard'; later 'packing ring') is usually taken from French garcette 'small rope', diminutive of garce 'girl' (< gars, ultimately Frankish *wrakkjō). The r-loss and -et ending are not fully explained, so Klein, Watkins ('perhaps') and Wiktionary ('Perhaps from Middle French garcette') give it with reservation.\",\n  \"derivation_fa\":\"انگلیسی gasket (از دههٔ ۱۶۲۰ «طناب کوچک برای بستن بادبان»، بعدها «واشر») را معمولاً از فرانسوی garcette «طناب باریک»، مصغّر garce «دختر»، می‌دانند. افتادن r و پایانهٔ -et کاملاً روشن نیست و واتکینز و ویکی‌واژه با «شاید» آورده‌اند؛ پس ادعای نورایی پذیرفتنی ولی نه قطعی است.\",\n  \"sources\":[GASKET,GARCETTE],\n  \"ref_check\":[{\"ref\":\"None\",\"status\":\"not_checked\",\"note\":\"node carries no reference; Nourai's KLN:642 on the parent node gives 'gasket, n., a piece of rope (naut.) — F. garcette, dimin. of garce'\"}],\n  \"consulted\":[{\"src\":\"KLN\",\"where\":\"p. 642 (KLN_1966 l. 15828)\",\"stance\":\"supports\",\"note\":\"'gasket, n., a piece of rope (naut.) — F. garcette, dimin. of garce, \\\"wench\\\", femin. to garçon'\"},AHDq,{\"src\":\"SKT\",\"where\":\"SKT.txt\",\"stance\":\"silent\",\"note\":\"grep 'gasket' — no hit\"}]},\n {\"id\":7,\"lang\":\"Latin\",\"words\":\"urgere\",\"verdict\":\"plausible\",\n  \"derivation\":\"Latin urgeō, urgēre (early also urgueō) 'to press, drive, push, urge' is traditionally a zero-grade stative *wr̥g-ēye- of *wreg- (Pokorny, Walde-Pokorny, Watkins, Klein, Cheung). De Vaan 2008 (cited at Wiktionary) marks the link 'disputed': PIE *wr̥- should give Latin vor-/vr- rather than ur-, and the old by-form urgueō suggests a labiovelar, so the etymology is formally uncertain; Mann even files it under another root. The meaning fits perfectly.\",\n  \"derivation_fa\":\"لاتین urgeō/urgēre «فشار آوردن، راندن» را پوکورنی، والده، واتکینز، کلاین و چونگ از بالانْد صفر ریشهٔ *wreg- می‌دانند. اما دو وان (۲۰۰۸) این پیوند را مشکوک می‌شمارد، زیرا r هجایی پس از w در لاتین باید vor- بدهد نه ur-، و صورت کهن urgueō به همخوان لبی‌ـ‌نرم‌کامی اشاره دارد. پس سخن نورایی پذیرفتهٔ سنتی است ولی امروز با احتیاط پذیرفتنی است.\",\n  \"sources\":[URGEO,PIE],\n  \"ref_check\":[{\"ref\":\"AHD\",\"status\":\"supports\",\"note\":\"'III. Zero-grade form *wrg-ēyo- in Latin urgēre, to urge, drive: URGE. [Pok. ureg- 1181.]'\"}],\n  \"consulted\":[POKq,WLDq,{\"src\":\"IEC\",\"where\":\"IEC.txt l. 14918\",\"stance\":\"partial\",\"note\":\"'Lat. cf. urgeo, ere, beside urgueo, ere \\\"press, urge, hasten\\\". Ambig.' — under rǝg-, not wreg-\"},{\"src\":\"KLN\",\"where\":\"s.v. urge\",\"stance\":\"supports\",\"note\":\"'urge — L. urgere, \\\"to press, drive, urge\\\", cogn. with Goth. wrikan, \\\"to persecute\\\", OE. wrecan'\"}]},\n {\"id\":8,\"lang\":\"English\",\"words\":\"urge\",\"verdict\":\"confirmed\",\n  \"derivation\":\"English urge (1550s, 'to press, insist') is borrowed directly from Latin urgēre 'press, drive'; urgent, urgency come via Middle French urgent and Late Latin urgentia.\",\n  \"derivation_fa\":\"انگلیسی urge (سدهٔ ۱۶) مستقیماً از لاتین urgēre «فشار آوردن، راندن» گرفته شده و urgent و urgency از راه فرانسوی میانه و لاتین متأخر آمده‌اند. ادعای نورایی درست است.\",\n  \"sources\":[URGEO],\n  \"ref_check\":[{\"ref\":\"None\",\"status\":\"not_checked\",\"note\":\"node carries no reference; checked Klein instead (see consulted)\"}],\n  \"consulted\":[{\"src\":\"KLN\",\"where\":\"KLN_1966 l. 40872 s.v. urge\",\"stance\":\"supports\",\"note\":\"'urge, tr. v. — L. urgere, \\\"to press, drive, urge\\\", cogn. with Goth. wrikan'\"},AHDq]}\n ]}\n\nLKTq={\"src\":\"LKT\",\"where\":\"LKT.txt l. 3333 s.v. mausim\",\"stance\":\"supports\",\"note\":\"'Jahreszeit ... auch schon bei den ar. Seeleuten ... hieraus pg. monção, mouçāo, sp. monzon, frz. mousson ... engl. monsoon, ndl. moesson'\"}\nKLNm={\"src\":\"KLN\",\"where\":\"p. 1000 (KLN_1966 l. 24343)\",\"stance\":\"supports\",\"note\":\"'monsoon — MDu. monssoen, fr. Port. monção, fr. Arab. máusim ... \\\"time of the year, season\\\", fr. wasama, \\\"he marked with a brand\\\". The final letters -im ... were misread as -un'\"}\ne6={\"entry\":6,\"root\":\"W.s.m\",\"verdict\":\"confirmed\",\n \"modern_form\":\"Arabic root و س م w-s-m 'to brand, mark'\",\n \"note\":\"Root and gloss correct: wasama 'to brand, mark'; mawsim (maf'il noun of place/time) 'appointed time, season, fair'. Wiktionary's Arabic مَوْسِم page adds a speculative comparison with Hebrew m-z-m-n, but Arabic lexicography (and Klein, Lokotsch, Devic) files mawsim under w-s-m.\",\n \"note_fa\":\"ریشهٔ عربی «و س م» به معنای «داغ نهادن، نشان کردن» است؛ «وَسَمَ» فعل آن و «مَوْسِم» (اسم زمان/مکان بر وزن مَفْعِل) «زمانِ نشان‌دار، هنگام معیّن، فصل» است. کلاین، لوکوچ و دویک همین را می‌گویند؛ ادعای نورایی درست است.\",\n \"sources\":[MAWSIM,MONSOON],\n \"ref_check\":[{\"ref\":\"KLN:1000\",\"status\":\"supports\",\"note\":\"KLN_1966 leaf 536 (p. 1000) s.v. monsoon: 'Arab. máusim ... \\\"time of the year, season\\\", fr. wasama, \\\"he marked with a brand, he marked\\\"'\"}],\n \"consulted\":[LKTq,{\"src\":\"DEV\",\"where\":\"DEV.txt l. 1800 s.v. mousson\",\"stance\":\"supports\",\"note\":\"'De l'arabe mausim, époque fixe, fête, foire, et aussi saison favorable pour le voyage des Indes'\"}],\n \"nodes\":[\n {\"id\":1,\"lang\":\"Arabic\",\"words\":\"wasama; mousim\",\"verdict\":\"confirmed\",\n  \"derivation\":\"Arabic وَسَمَ wasama 'he branded, marked' (verbal noun وَسْم wasm, also سِمَة sima 'mark'); مَوْسِم mawsim (Nourai's 'mousim' renders the colloquial diphthong) is the mafʿil noun of time/place: 'the marked/appointed time' — of the Mecca pilgrimage fair, of markets, and among Arab pilots of the season of favourable winds to India. Hobson-Jobson quotes the Muḥīṭ: 'mausim is used of anything that comes round but once a year'.\",\n  \"derivation_fa\":\"«وَسَمَ» در عربی یعنی «داغ نهاد، نشان کرد» (مصدر «وَسْم» و «سِمَة» به معنای نشان). «مَوْسِم» بر وزن مَفْعِل اسم زمان است: «هنگامِ نشان‌دار و معیّن»، یعنی هنگام حج و بازارها و نزد دریانوردان عرب فصل بادهای موافق برای سفر به هند. ادعای نورایی درست است.\",\n  \"sources\":[MAWSIM],\n  \"ref_check\":[{\"ref\":\"KLN:1000\",\"status\":\"supports\",\"note\":\"'Arab. máusim (written mousim), \\\"time of the year, season\\\", fr. wasama, \\\"he marked with a brand, he marked\\\"' — Nourai's wording verbatim.\"}],\n  \"consulted\":[LKTq,{\"src\":\"HJB\",\"where\":\"s.v. Monsoon (HJB.txt l. 14518-14519)\",\"stance\":\"supports\",\"note\":\"'The original word is the Ar. mausim, \\\"season,\\\" ... Mausim is used of anything that comes round but once a year, like the festivals'\"},{\"src\":\"PHN\",\"where\":\"PHN.txt l. 7709 s.v. Mousson\",\"stance\":\"supports\",\"note\":\"Pihan derives mousson from Arabic mausim; '... les Portugais monçao, et les Anglais monsoon'\"}]},\n {\"id\":2,\"lang\":\"Persian\",\"words\":\"vasm; vasmeh; semat; mowsem\",\"verdict\":\"confirmed\",\n  \"derivation\":\"All four are Arabic loans of the w-s-m family: vasm < Ar. wasm 'brand, mark' (Mo'in: [ع.] 'داغ و نشان'); vasmeh < Ar. wasma 'woad/indigo leaves used to dye the eyebrows' (Mo'in [ع. وسمة]; Sa'di's line 'وسمه بر ابروی کور'), named from its marking/colouring use; semat (سِمَت, with kasra) < Ar. sima (سِمَة) 'mark, sign', the tā' marbūṭa written as ت in Persian, with the Persian sense shift 'title, rank, office' (Dehkhoda: 'سمت [سِ مَ] (ع اِ) سمة ... رتبه، مقام'); it must be kept apart from homographic samt (سَمْت) 'direction' (Ar. samt, ultimately Aramaic < Latin sēmita), which is unrelated; mowsem < Ar. mawsim 'season' (Mo'in [ع.] 'زمان، هنگام؛ فصل').\",\n  \"derivation_fa\":\"هر چهار واژه وام‌واژه‌های عربی از ریشهٔ «و س م»اند: «وَسم» از عربی وَسْم «داغ و نشان»؛ «وَسمه» از عربی وَسْمَة، گیاهی که برگش را برای رنگ کردن ابرو به کار می‌بردند (سعدی: «کوشش بی‌فایده است وسمه بر ابروی کور»)؛ «سِمَت» از عربی سِمَة «نشان، علامت» که تای گرد آن در فارسی «ت» نوشته شده و معنای «عنوان، مقام» یافته است — و نباید آن را با «سَمت» به معنای «جهت» (از عربی سَمْت) که هم‌ریشه نیست یکی گرفت؛ «موسم» از عربی مَوْسِم «هنگام، فصل». ادعای نورایی درست است.\",\n  \"sources\":[M_WASM,M_WASMA,WASMA,ABADIS_SAMT,M_MAWSIM,MAWSIM,SAMT],\n  \"ref_check\":[{\"ref\":\"FVA:430\",\"status\":\"not_checked\",\"note\":\"Nahvi's Farhang-e vazheha-ye Arabi: no digital copy (refs_online.json)\"},\n   {\"ref\":\"MON:5026\",\"status\":\"partial\",\"note\":\"print page not accessible; Mo'in's entries online: وسم '(وَ) [ع.] ۱- داغ و نشان'; وسمه '[ع. وسمة] گیاهی ... برای رنگ کردن ابرو'; سمت '(سِ مَ) [ع.] ۱- نشان داغ ۲- علامت ۳- عنوان ۴- مقام' (abadis); موسم '[ع.] زمان، هنگام، فصل' — all marked Arabic, consistent with Nourai (MON:5026 itself is in the proper-names volume range, so the page number is doubtful).\"}],\n  \"consulted\":[{\"src\":\"MON\",\"where\":\"vajehyab/abadis s.v. وسم، وسمه، سمت، موسم\",\"stance\":\"supports\",\"note\":\"'وسمه (وَ مِ) [ع. وسمة]'; 'سمت (سِ مَ) [ع.] ... ۴- مقام: به سمت ریاست منصوب شد'\"},\n   {\"src\":\"DEH\",\"where\":\"Dehkhoda via abadis s.v. سمت\",\"stance\":\"supports\",\"note\":\"'سمت. [سِ مَ] (ع اِ) سمة ... رتبه. مقام' and separately 'سمت. [سَ] (ع اِ) طرف. سوی'\"},\n   {\"src\":\"AFM\",\"where\":\"AFM_pages.txt\",\"stance\":\"silent\",\"note\":\"grep 'وسمه|wasma' — not treated (native Arabic words, not Persian loans into Arabic)\"},\n   {\"src\":\"FVQ\",\"where\":\"FVQ_pages.txt\",\"stance\":\"silent\",\"note\":\"grep 'wasma|wasm' — not a Qur'anic foreign word\"}]},\n {\"id\":3,\"lang\":\"Portuguese\",\"words\":\"mončâo\",\"verdict\":\"confirmed\",\n  \"derivation\":\"Portuguese monção (16th c., older mouçāo) was taken by Portuguese navigators in the Indian Ocean (after Vasco da Gama, 1498) from Arab pilots' mawsim 'sailing season'; the -im was assimilated to the Portuguese -ão (< -ōnem) noun ending and n-insertion before ç is secondary. Nourai's 'mončâo' is his transliteration of monção (č for ç); the printed page has exactly this.\",\n  \"derivation_fa\":\"پرتغالی monção (سدهٔ ۱۶، کهن‌تر mouçāo) را دریانوردان پرتغالی پس از واسکو دو گاما (۱۴۹۸) از راهنمایان عرب در اقیانوس هند گرفتند: «مَوْسِم» به معنای «فصل دریانوردی»؛ پایانهٔ -im با پسوند پرتغالی -ão همانند شده است. «mončâo» در کتاب نویسه‌گردانی نورایی از monção است. ادعای نورایی درست است.\",\n  \"sources\":[MONCAO,MONSOON],\n  \"ref_check\":[{\"ref\":\"KLN:1000\",\"status\":\"supports\",\"note\":\"'MDu. monssoen, fr. Port. monção, fr. Arab. máusim'\"},{\"ref\":\"AHD:850\",\"status\":\"not_checked\",\"note\":\"1976 AHD main-dictionary page not available; Watkins appendix has no Semitic entry for w-s-m\"}],\n  \"consulted\":[LKTq,{\"src\":\"DEV\",\"where\":\"DEV.txt l. 1800\",\"stance\":\"supports\",\"note\":\"'Mousson ... Esp. monzon, portug. monção, ital. mussone. De l'arabe mausim'\"},{\"src\":\"LAM\",\"where\":\"LAM.txt l. 5489\",\"stance\":\"supports\",\"note\":\"'Mousson. Esp: monzon. Ptg: mouçaõ ... mot qui vient de l'arabe et signifie saison'\"}]},\n {\"id\":4,\"lang\":\"Dutch\",\"words\":\"monssoen\",\"verdict\":\"confirmed\",\n  \"derivation\":\"Early Modern Dutch monssoen (16th–17th c., VOC usage) from Portuguese monção, with the Portuguese nasal -ão rendered -oen; the modern Dutch form is moesson (so 'monssoen' is indeed obsolete). English took the word from Dutch.\",\n  \"derivation_fa\":\"هلندی کهن monssoen (سده‌های ۱۶ و ۱۷، در زبان کمپانی هند شرقی هلند) از پرتغالی monção گرفته شده و پایانهٔ خیشومی -ão به -oen برگشته است؛ صورت امروزی هلندی moesson است، پس «منسوخ» بودن آن درست است. ادعای نورایی درست است.\",\n  \"sources\":[MONSOON],\n  \"ref_check\":[{\"ref\":\"KLN:1000\",\"status\":\"supports\",\"note\":\"'monsoon — MDu. monssoen, fr. Port. monção'\"},{\"ref\":\"AHD:850\",\"status\":\"not_checked\",\"note\":\"1976 AHD page not available\"}],\n  \"consulted\":[{\"src\":\"DOZ\",\"where\":\"DOZ.txt l. 168\",\"stance\":\"partial\",\"note\":\"Dozy lists 'moesson' among Dutch words of Eastern origin (the modern form), no 'monssoen'\"},LKTq]},\n {\"id\":5,\"lang\":\"English\",\"words\":\"monsoon\",\"verdict\":\"confirmed\",\n  \"derivation\":\"English monsoon (1580s, 'seasonal wind of the Indian Ocean') from early modern Dutch monssoen < Portuguese monção < Arabic mawsim 'season'; Klein notes the final -im was rendered -un/-oon. The sense moved from 'sailing season' to the wind itself and then to the rainy season it brings.\",\n  \"derivation_fa\":\"انگلیسی monsoon (دههٔ ۱۵۸۰، «باد فصلی اقیانوس هند») از هلندی کهن monssoen، از پرتغالی monção و سرانجام از عربی «مَوْسِم» است. معنا از «فصل دریانوردی» به خودِ «باد فصلی» و سپس «فصل باران‌های موسمی» گسترش یافته است. ادعای نورایی درست است.\",\n  \"sources\":[MONSOON],\n  \"ref_check\":[KLNm|{\"ref\":\"KLN:1000\",\"status\":\"supports\"} if False else {\"ref\":\"KLN:1000\",\"status\":\"supports\",\"note\":\"KLN_1966 p. 1000: 'monsoon, n., the trade wind of the Indian Ocean. — MDu. monssoen, fr. Port. monção, fr. Arab. máusim'\"},{\"ref\":\"AHD:850\",\"status\":\"not_checked\",\"note\":\"1976 AHD page not available\"},{\"ref\":\"OXF:269\",\"status\":\"not_checked\",\"note\":\"Oxford Dictionary of Foreign Words: lending-only scan\"}],\n  \"consulted\":[KLNm,{\"src\":\"SKT\",\"where\":\"SKT.txt l. 11840\",\"stance\":\"partial\",\"note\":\"'Monsoon ... Ital. monsone ... Malay musim ... Arab. mawsim, a time, season ... (root wasama) marking' — same Arabic source, routes via Italian/Malay\"},{\"src\":\"HJB\",\"where\":\"s.v. Monsoon\",\"stance\":\"supports\",\"note\":\"'the Ar. mausim, \\\"season,\\\" which the Portuguese corrupted into monção, and our people into monsoon'\"}]}\n ]}\n\nout={\"pdf_page\":557,\"book_page\":527,\"verified_by\":\"claude-opus-5.5\",\"verified_on\":\"2026-10-16\",\"entries\":[e0,e6]}\njson.dump(out,open('/home/sfmqrb/git/rishe-private/data/verification/page-557.json','w'),ensure_ascii=False,indent=1)\nEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/build-557.py && python3 -m json.tool /home/sfmqrb/git/rishe-private/data/verification/page-557.json >/dev/null && python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py 557"
}
```


### [2026-10-17T00:06:44.433Z] TOOL RESULT

```
nodes verified: 13/13
node verdicts: {'confirmed': 8, 'plausible': 5}
root verdicts: {'confirmed': 2}
ref checks: {'supports': 11, 'not_checked': 7, 'partial': 1}
books consulted: {'supports': 27, 'silent': 10, 'contradicts': 1, 'partial': 3} | by book: {'KLN': 6, 'AHD': 4, 'WLD': 3, 'MON': 3, 'SKT': 3, 'LKT': 3, 'CHEUNG': 2, 'ARY': 2, 'POK': 2, 'DEV': 2, 'HJB': 2, 'HUB': 1, 'PHD': 1, 'IEC': 1, 'PHN': 1, 'DEH': 1, 'AFM': 1, 'FVQ': 1, 'LAM': 1, 'DOZ': 1}
```


## [2026-10-17T00:06:47.697Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; sed -i 's/(§50, p\\. 1xx: /(§50: /' data/verification/page-557.json /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/build-557.py; grep -c '1xx' data/verification/page-557.json; python3 -m json.tool data/verification/page-557.json >/dev/null && python3 tools/verify_check.py 557 | grep -c PROBLEM"
}
```


### [2026-10-17T00:06:48.331Z] TOOL RESULT

```
0
0
```


## [2026-10-17T00:06:55.961Z] TOOL CALL #39: SubagentHandback

```json
{
 "message": "I verified PDF page 557 (book page 527) and wrote /home/sfmqrb/git/rishe-private/data/verification/page-557.json. `verify_check.py 557` reports 13/13 nodes verified and 0 PROBLEM lines. The page has two real entries, Wreg 1 and W.s.m; the 5 redirect entries were skipped.\n\n- **Roots:** 2 confirmed (Wreg 1 = PIE *wreg- in Pokorny p. 1181; W.s.m = Arabic root \"to brand, mark\").\n- **Nodes:** 8 confirmed, 5 plausible, 0 disputed, 0 transcription_suspect.\n- **Plausible items:**\n  - Wreg 1 #2 gorâzîdan: Horn no. 897, Hübschmann §50 and Mo'in (Borhan p. 1781, note 5) derive it from Sanskrit vraj-. Cheung 2007 says \"No further Ir. cognates are known\" under *u̯raj, so he does not accept it. The sense \"strut proudly\" could also point to Avestan uruuaz- \"be proud\".\n  - Wreg 1 #3 wrekjan: not a standard reconstruction. It blends Proto-Germanic *wrekaną with *wrakjaną.\n  - Wreg 1 #4 garcette: the derivation is right, but the gloss \"waitress\" is wrong. It means \"little girl\" or a small nautical rope; \"waitress\" in French is serveuse.\n  - Wreg 1 #6 gasket < garcette: the sources give it only as \"perhaps\".\n  - Wreg 1 #7 Latin urgere < *wreg-: de Vaan 2008 disputes the link.\n- **Other notes:**\n  - semat «سِمَت» (rank, position) is correctly from Arabic sima \"mark\". It is a different word from samt «سَمت» (direction).\n  - Klein's pages 640, 642 and 1000 match exactly what Nourai cites.\n  - Borhan p. 1781 was read from the page image and saved as data/verification/sources/refs/ocr/BQT/1781.vision.txt.\n- **Extraction errors:** none. The printed page matches the JSON, including \"wrekjan\", \"garcette : waitress\" and \"mončâo\".\n- **Etymonline:** all three page fetches failed, so Etymonline is not cited."
}
```


### [2026-10-17T00:06:56.308Z] TOOL RESULT

```
{"success":true,"message":"Report delivered to your caller."}
```
