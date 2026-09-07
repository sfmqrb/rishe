# Verification process log — verify-page-325


## [2026-09-07T15:49:27.344Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 325 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-325.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-325.json. Write /home/sfmqrb/git/rishe/data/verification/page-325.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 325` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-07T15:49:29.486Z] AGENT

I'll start by reading the agent instructions.


## [2026-09-07T15:49:30.144Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-07T15:49:30.158Z] TOOL RESULT

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


## [2026-09-07T15:49:30.687Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-325.txt"
}
```


### [2026-09-07T15:49:30.701Z] TOOL RESULT

```
1	=== PDF page 325 (book page 295) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Medhyo : middle  (refs None)
4	#1 (parent #0) [Avestan] refs=KLN:954; HRN:225 | maidyâna : middle
5	  #2 (parent #1) [Sogdian] refs=SOD:223 | myd`n : middle
6	  #3 (parent #1) [Pahlavi] refs=None | 
7	    #4 (parent #3) [Persian] refs=None | miyân «میان» : middle
8	#5 (parent #0) [Germanic] refs=AHD; KLN | midja : middle
9	  #6 (parent #5) [English] refs=None | middle
10	#7 (parent #0) [Latin] refs=AHD | medius : middle ; medi-terrâneous : in land sea ☞Ters
11	  #8 (parent #7) [French] refs=None | 
12	    #9 (parent #8) [Persian] refs=MON:3974 |  | extra: مدیوم ، مدیترانه
13	  #10 (parent #7) [English] refs=None | immediate, median, medium, mean 1 ; Mediterranean
14	--- entry 1 ---
15	ROOT [Indo-European] Meg, Megh : great  (refs POK:708; KLN:958)
16	#1 (parent #0) [Avestan / Old Persian] refs=POK:708; KLN:958; SYN:878 | maz, mazant : great ; maz-yah, mathi-yah : greater ☞Yah 5 ; maz-išta : greatest ☞Isto ; mazah, mazan : size, greatness | NOTE: Compare with the AV/OPR word from Root "Mâk: long"
17	  #2 (parent #1) [Pahlavi] refs=None | meh : great
18	    #3 (parent #2) [Persian] refs=HRN:224; BQT:2002,2058 | meh 2 «مه ٢» : great ; mehast «مهست» : greatest ; meznâ «مزنا» : balance, scale | NOTE: "meznâ" was not found in MON. See Mâk for another possible root.
19	#4 (parent #0) [Sanskrit] refs=AHD | mahâ : great ; mahâ-râja : great king ☞Reg
20	  #5 (parent #4) [Persian] refs=MON:4458 | mahârâjeh «مهاراجه» : great king (of India)
21	  #6 (parent #4) [Hindustani] refs=None | 
22	    #7 (parent #6) [English] refs=AHD | maharajah, mahatma
23	#8 (parent #0) [Germanic] refs=AHD | mikila
24	  #9 (parent #8) [English] refs=None | much, more
25	#10 (parent #0) [Latin] refs=AHD | maximus : greatest
26	  #11 (parent #10) [French] refs=None | 
27	    #12 (parent #11) [Persian] refs=MON | mâxîmom «ماکسیمم»
28	  #13 (parent #10) [English] refs=None | magnitude, majesty, major, magnum, master, maximum, May, mayor
29	#14 (parent #0) [Greek] refs=AHD | megas : great
30	  #15 (parent #14) [English] refs=None | omega, mega-
31	
```


## [2026-09-07T15:49:35.825Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-325.json && echo \"=== refs_online keys ===\" && python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','KLN','HRN','SOD','SYN','AHD','BQT','MON','PHD','NYB','WLD','IEC','BRT','KNT','HUB','CHEUNG','ARY','SKT','FSD','WEB','TTS','LKT','HJB','AID']:\n    print(k, json.dumps(d.get(k), ensure_ascii=False)[:400])\n\""
}
```


### [2026-09-07T15:49:37.122Z] TOOL RESULT

```
{
  "pdf_page": 325,
  "book_page": 295,
  "entries": [
    {
      "root": {
        "name": "Medhyo",
        "lang": "Indo-European",
        "refs": null,
        "gloss": "middle"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "KLN:954; HRN:225",
          "words": [
            {"translit": "maidyâna", "gloss": "middle", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Sogdian",
          "refs": "SOD:223",
          "words": [
            {"translit": "myd`n", "gloss": "middle", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": null,
          "words": [],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Persian",
          "refs": null,
          "words": [
            {"translit": "miyân", "gloss": "middle", "script": "میان"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD; KLN",
          "words": [
            {"translit": "midja", "gloss": "middle", "script": null}
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
            {"translit": "middle", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "medius", "gloss": "middle", "script": null},
            {"translit": "medi-terrâneous", "gloss": "in land sea", "script": null, "see": ["Ters"]}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 7,
          "lang": "French",
          "refs": null,
          "words": [],
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "Persian",
          "refs": "MON:3974",
          "words": [],
          "script_extra": "مدیوم ، مدیترانه",
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 7,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "immediate, median, medium, mean 1", "gloss": null, "script": null},
            {"translit": "Mediterranean", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Meg, Megh",
        "lang": "Indo-European",
        "refs": "POK:708; KLN:958",
        "gloss": "great",
        "note": "This root may be related to \"Mâk: long, slender\""
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan / Old Persian",
          "refs": "POK:708; KLN:958; SYN:878",
          "words": [
            {"translit": "maz, mazant", "gloss": "great", "script": null},
            {"translit": "maz-yah, mathi-yah", "gloss": "greater", "script": null, "see": ["Yah 5"]},
            {"translit": "maz-išta", "gloss": "greatest", "script": null, "see": ["Isto"]},
            {"translit": "mazah, mazan", "gloss": "size, greatness", "script": null}
          ],
          "note": "Compare with the AV/OPR word from Root \"Mâk: long\"",
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": null,
          "words": [
            {"translit": "meh", "gloss": "great", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "HRN:224; BQT:2002,2058",
          "words": [
            {"translit": "meh 2", "gloss": "great", "script": "مه ٢"},
            {"translit": "mehast", "gloss": "greatest", "script": "مهست"},
            {"translit": "meznâ", "gloss": "balance, scale", "script": "مزنا"}
          ],
          "note": "\"meznâ\" was not found in MON. See Mâk for another possible root.",
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "AHD",
          "words": [
            {"translit": "mahâ", "gloss": "great", "script": null},
            {"translit": "mahâ-râja", "gloss": "great king", "script": null, "see": ["Reg"]}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Persian",
          "refs": "MON:4458",
          "words": [
            {"translit": "mahârâjeh", "gloss": "great king (of India)", "script": "مهاراجه"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 4,
          "lang": "Hindustani",
          "refs": null,
          "words": [],
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "maharajah, mahatma", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "mikila", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "much, more", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "maximus", "gloss": "greatest", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 10,
          "lang": "French",
          "refs": null,
          "words": [],
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 11,
          "lang": "Persian",
          "refs": "MON",
          "words": [
            {"translit": "mâxîmom", "gloss": null, "script": "ماکسیمم"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 13,
          "parent": 10,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "magnitude, majesty, major, magnum, master, maximum, May, mayor", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 14,
          "parent": 0,
          "lang": "Greek",
          "refs": "AHD",
          "words": [
            {"translit": "megas", "gloss": "great", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 15,
          "parent": 14,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "omega, mega-", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    }
  ]
}
=== refs_online keys ===
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 
SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in 
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verific
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sou
KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "loca
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1
CHEUNG null
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-D
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-di
TTS {"title": "H. Vámbéry, Etymologisches Wörterbuch der turko-tatarischen Sprachen, Leipzig 1878 (repr. Osnabrück 1972)", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/etymologischesw00vmuoft (Toronto scan; also Google/bub_gb copies)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_vambery1878_uoft.pdf", 
LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 =
HJB {"title": "H. Yule & A. C. Burnell, Hobson-Jobson, 2nd ed. by W. Crooke, London 1903 (Delhi reprint 1968)", "edition_found": "1903 Crooke edition (pagination identical to the 1968 reprint)", "kind": "archive_djvu", "url": "https://archive.org/details/hobsonjobsonagl02croogoog", "identifier": "hobsonjobsonagl02croogoog (others: bub_gb_6Z5iAAAAMAAJ, hobsonjobsonglos00yulerich, india.history.resource
AID {"title": "G. C. Whitworth, An Anglo-Indian Dictionary, London 1885", "edition_found": "1885 (DLI scan); also 1981 reprint scan", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.45332", "identifier": "in.ernet.dli.2015.45332 (also anglo-indiandictionary, 1981 reprint)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AID.txt", "page_offset": "leaf
```


## [2026-09-07T15:49:43.781Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','KLN','HRN','SOD','SYN','AHD','BQT','MON','PHD','NYB','WLD','IEC','BRT','KNT','HUB','ARY','SKT','LKT','HJB','AID','AFM','PLA','FVQ']:\n    v=d.get(k)\n    if not v: print(k,'--none--'); continue\n    print('==',k)\n    for f in ['kind','local_file','page_offset','lookup_hint','scans']:\n        if v.get(f): print('  ',f,':',str(v[f])[:600])\n\""
}
```


### [2026-09-07T15:49:45.424Z] TOOL RESULT

```
== POK
   kind : archive_djvu
   local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt
   page_offset : POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   lookup_hint : Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-dictionary/ (entry pages with page numbers) and StarLing https://starlingdb.org/cgi-bin/query.cgi?basename=\data\ie\pokorny&root=config
== KLN
   kind : archive_djvu
   local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt
   page_offset : KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   lookup_hint : Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.
== HRN
   kind : archive_djvu
   local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt
   page_offset : leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   lookup_hint : Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.
== SOD
   kind : archive_djvu
   local_file : ['/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD.txt']
   page_offset : printed page ≈ leaf − 66 in SOD_pages.txt (0-based \f blocks; 645 leaves; English intro precedes)
   lookup_hint : Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/Sog
== SYN
   kind : archive_djvu
   local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt
   page_offset : leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   lookup_hint : Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the concept heading (all caps English word) or a printed page number line.
== AHD
   kind : archive_djvu+website+archive_restricted
   local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt
   page_offset : 1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page.
   lookup_hint : Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru-' ; entries list English derivatives in caps. Restricted 1970s AHD scans on IA (lending only, djvu.txt returns 401): americanheritage0000dict (July 1977 printing, 970 leaves - probably the New College Edition), bwb_P9-BHZ-437 (1974), americanheritage00nyde (1970), bwb_W9-CSW-086 (1969, 1610 leaves 
== BQT
   kind : archive_djvu+local_scan_ocr
   local_file : ['/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt', '/home/
   page_offset : vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (
   lookup_hint : grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=deh
   scans : [{'volume': '3', 'file': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', 'first_printed': 1208, 'last_printed': 1925, 'pdf_offset': -1205, 'page_map': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pagemap.json', 'lang': 'fas', 'ocr_text': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', 'ocr_note': '689/721 pdf pages OCRed (tesseract fas+eng, mediocre); pages are separated by form-feeds and tagged [pdf page N]; remaining pages via tools/ref_page.py'}, {'volume': '4', 'file': '/home/sfmq
== MON
   kind : website+archive_djvu
   local_file : ['/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt']
   lookup_hint : Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different pagination from the 6-vol edition; OCR downloaded a
== PHD
   kind : archive_djvu
   local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt
   page_offset : leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   lookup_hint : Headword = Pahlavi in transliteration at line start, followed by Pahlavi script (not OCRed) and gloss, e.g. grep -n '^abar '. Alternative PDF: https://www.parsianjoman.org/wp-content/uploads/2015/09/A-Concise-Pahlavi-Dictionary.pdf (8.4 MB).
== NYB
   kind : archive_djvu
   local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt
   page_offset : Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   lookup_hint : Nourai's 'NYB' numbers are Part II (Glossary) pages. Headwords are Pahlavi in transliteration at line start (e.g. grep -n '^apar'), with Avestan/OP/NP cognates and 'Bthl.' refs.
== WLD
   kind : archive_djvu
   local_file : ['/home/sfmqrb/git/rishe/data/verification/sources/refs/WLD_band3.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_text.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_text.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sou
   page_offset : Band 3: leaf = printed + 6. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> || Band I (WLD_Bd1_pages.txt, 887 leaves): printed = leaf(1-based) − 9 (leaf 801 = p.792). Band II (WLD_Bd2_pages.txt, 720 leaves): printed = leaf − 5 (leaf 701 = p.696).
   lookup_hint : Band 3 is the index (Wortregister by language) - it maps a word to 'Band, page' in vols 1-2, so it can at least confirm that a word is treated at the cited WP volume/page. For the actual entry text, use Pokorny 1959 (POK), whose entries cite 'WP. I 177' etc. and are essentially a revision of WP.
== IEC
   kind : archive_djvu
   local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt
   page_offset : TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   lookup_hint : Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root.
== BRT
   kind : archive_djvu
   local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt
   page_offset : Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   lookup_hint : Nourai's BRT numbers are Bartholomae's COLUMN numbers. Headwords are Avestan/OP in transliteration in bold at line start; OCR of the special transliteration is noisy - grep on a distinctive Latin gloss or the German meaning in quotes. Column numbers appear as standalone numbers at leaf tops.
== KNT
   kind : archive_djvu
   local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt
   page_offset : leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   lookup_hint : Lexicon (Part III, pp. 164 ff.) headwords are transliterated OP words at line start followed by part of speech, e.g. grep -n '^apadana-' ; section refs like '$147'. Nourai's page numbers should fall in 164-215 for lexicon citations.
== HUB
   kind : archive_djvu
   local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt
   page_offset : leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   lookup_hint : Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by paragraph (§). grep the transliterated Persian word or Horn's entry number.
== ARY
   kind : local_scan_ocr
   local_file : ['/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt']
   page_offset : printed page = pdf page + 1
   lookup_hint : Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY:<printed page> --image
   scans : [{'file': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_aryanpur_kashani_rishehaye_hend_o_orupayi.pdf', 'first_printed': 1, 'last_printed': 546, 'pdf_offset': -1, 'lang': 'fas+eng', 'ocr_text': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_pages.txt'}]
== SKT
   kind : archive_djvu
   local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt
   page_offset : leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   lookup_hint : Headword in caps at line start, e.g. grep -n '^TREE' SKT.txt; entries are terse with '(E.)', '(F.-L.)' language tags.
== LKT
   kind : archive_djvu
   local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt
   page_offset : leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   lookup_hint : Numbered entries: 'NNNN. word (language) meaning' - Lokotsch is usually cited by entry number, but Nourai cites pages. grep the oriental source word in transliteration or the number.
== HJB
   kind : archive_djvu
   local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/HJB.txt
   page_offset : leaf = printed + 35..51 (plates inserted; e.g. leaf 83 = p.32, leaf 319 = p.270, leaf 535 = p.490, leaf 905 = p.870). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   lookup_hint : Headwords in caps at line start followed by ', s.' etc., e.g. grep -n '^BAZAAR' HJB.txt. Also online at dsal: https://dsal.uchicago.edu/dictionaries/hobsonjobson/ (search box) which shows page numbers.
== AID
   kind : archive_djvu
   local_file : /home/sfmqrb/git/rishe/data/verification/sources/refs/AID.txt
   page_offset : leaf = printed + 18 (e.g. leaf 20 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   lookup_hint : Headword in bold at line start; grep -n '^Word'.
== AFM
   kind : archive_djvu
   local_file : ['/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM.txt']
   page_offset : 198 leaves; page numerals OCR'd unreliably — offset approx leaf − 8 (front matter); confirm on page image
   lookup_hint : Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').
== PLA
   kind : archive_djvu
   local_file : ['/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt']
   page_offset : 301 leaves (pdftotext -layout, \f-separated): printed page = leaf(1-based) − 15 (leaf 291 = p.276).
   lookup_hint : HathiTrust search-only; Google Books id q_ErAAAAMAAJ snippet view; DDB has only the table of contents. No full text online. | For pages in a scanned volume use: python3 tools/ref_page.py PLA:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)
   scans : [{'file': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf', 'first_printed': 1, 'last_printed': 300, 'pdf_offset': 0, 'lang': 'deu+ara'}]
== FVQ
   kind : archive_djvu
   local_file : ['/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ.txt']
   page_offset : printed page = leaf − 17 (0-based \f blocks in FVQ_pages.txt; 335 leaves)
   lookup_hint : Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).
```


## [2026-09-07T15:49:51.926Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK_full lemma megh ===\"; grep -n -i 'lemma: me[gǵ]' POK_full.txt | head -20\necho \"=== POK_full lemma medhi ===\"; grep -n -i 'lemma: medh' POK_full.txt | head -20"
}
```


### [2026-09-07T15:49:51.996Z] TOOL RESULT

```
=== POK_full lemma megh ===
60675:Root / lemma: megh- 
=== POK_full lemma medhi ===
```


## [2026-09-07T15:49:55.522Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '60660,60740p' POK_full.txt\necho \"=== search meg^h great ===\"\ngrep -n -i 'lemma: meg' POK_full.txt | head\necho \"=== medhi- mitten ===\"\ngrep -n -i 'lemma: medhi' POK_full.txt | head"
}
```


### [2026-09-07T15:49:55.611Z] TOOL RESULT

```
Meaning: to bind, attach 

Material: Old High German Old Saxon masca. Old English max, maescr' stitch ', Old 

Icelandic mQskvi^s:, 

Lithuanian mezgu, megsti^ tie, bind, knot, knit ', mazgas, Latvian mazgs^Vx\o{\ 
Lithuanian mazgytiWer. " knit ', makstyt/l\ax, wattle, braid', Latvian mezget, mizgef 
dislocate, luxate, crick ', mezgJV grow around, entwine itself around ' (russ. mazgart " 
spider'? s. Berneker II 28). 

References: WP. II 301, Trautmann 172. 
Page(s): 746 

Root / lemma: megh- 

Meaning: well-disposed, friendly 

Material: Gr. n£pi-r||J£KT£U) 'be unwilling ' (from *a-|j£KTOc; " unwilling '?); Gothic megs, 

Swedish mag^ son in law, husband of the daughter ' (compare French belle-mere). Old 

Icelandic /77ag/'" kinsman, relative through marriage'. Old English m^g. Old Saxon Old 

High German /77ag "kinsman, relative', etc.; Lithuanian megstu and megml, megtr like, be 

fond of ', megintr assay, try ', Latvian megV be good for, be suitable for '. 



References: WP. II 256, WH. II 5; Hj. Frisk Eranos 50, 1 1 f. 
Page(s): 707 



Root / lemma: mei-7: moi-. mT- 

Meaning: mild, soft 

Note: often with A, /?-, r-, /-extended 

Material: Old Indie mayas-u. " relief, pleasure, joy, lust', in addition *m(ilies(i!^(e)\u Old 

Indie miyedha-m. " saerifieial food ', Avestan myazda-m. "saerifieial meal'; as *mei-6'"o- 

Old Indie medha-rc\. " Fettbrijhe ', medhas-v\. 'saerifiee, oblation'; 

with A: eymr. /t?^/" blushful', df-fu/'bo\6' {*mdi-lo-)\ Old Prussian miJIs, Lithuanian mfelas 
and /77y/5s"dear, pleasant', meilet 'love', /77e//^5"affeetionate, loving', myliu, my/ef/"\ove\ 
pa-milstu, pa-m/'/t/" gro\N\ng fond of; Latvian m[/s {o\der ^-stem) and m/7s {irom *mielas) 
"dear', mHeflove', mieluot^ host '; Old Chureh Slavie /77//b "pitiful', russ. m/7yj^6ear', ete.; 

Alb. m/re^ dear, niee, kind ' a Slavie loanword (eommon alb. -I- > -r-) 

with n-. eymr. /77i^y/7 "friendly', aeorn. mu/n, /770//7 "dainty', bret. moan'th\n, tiny' {*mei- 
no-)\ Old Irish mm^ smooth, gentle' {*mT-no-)\ 

with r-. alb. m/re^goo6, beautiful'; Old Chureh Slavie m/rh^peace'; ablaut, aserb. m/jer 
{*mo/ro-), apoln. m/er^peace' (Old Lithuanian mieras, Latvian m/ers6s. are Slavie 
loanword); 

with t-. Latin /77/?/s"mild, soft' {*meit-)\ Old Irish moith, moeth {*mdit-) ds., also (?) PI. 
/77e(/)//7"fat, fertile'; eymr. mwydo {*meit-) " soften ', mwydion^ soft parts, external genitalia 
'; Latvian at-misV beeome soft ', at-mieteC soften '. 

References: WP. II 244, WH. II 96 f., Trautmann 174, 175. 
Page(s): 711-712 



Root / lemma: me-1 

Meaning: prohibitive partiele 

Grammatical information: prohibitiv 

Material: Old Indie Avestan Old pers. ma, gr. pn, Armenian m/'ds., alb. mosds. (from *mo 

= Indo Germanie *me+ s, that perhaps goes baek to Indo Germanie /("'e). 

=== search meg^h great ===
60675:Root / lemma: megh- 
=== medhi- mitten ===
```


## [2026-09-07T15:50:02.179Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== Page(s): 70[678] ===\"; grep -n 'Page(s): 70[5-9]' POK_full.txt | head -20\necho \"=== Page(s): 706-707 ===\"; grep -n 'Page(s): 706' POK_full.txt | head\necho \"--- lemma lines near ---\"; grep -n 'lemma: me' POK_full.txt | head -60"
}
```


### [2026-09-07T15:50:02.256Z] TOOL RESULT

```
=== Page(s): 70[678] ===
57841:Page(s): 706-707 
57891:Page(s): 707 
57990:Page(s): 705-706 
58001:Page(s): 706 
58096:Page(s): 708-709 
58296:Page(s): 709 
60692:Page(s): 707 
=== Page(s): 706-707 ===
57841:Page(s): 706-707 
58001:Page(s): 706 
--- lemma lines near ---
40298:It seems that from Root / lemma: g^hder- : to run, flow, derived Root / lemma: mer-5, 
57042:Root/ lemma: mad-: wet; glossy, fat, well-fed, intoxicating : Root/ lemma: meA^w. honey, 
57376:lemma: mend- mond-{mQd-l)\ to suck (breast), to feed; breast. 
57793:Root / lemma: meM^i- meMNo- 
57843:Root / lemma: meljd^u 
57853:Root/ lemma: mehli-t\ "honey' : Root/ lemma: meM^u: "honey' derived from a truncated 
57855:Root /lemma: mehl-1 {awch smehl-), mehlsh-' mle-, mehl-d-. ml-ed-, mehl-6'^-, ml-ei-: 
57861:Root/ lemma: rnahd-: wet; glossy, fat, well-fed, intoxicating : Root/ lemma: meM'^u: 
57893:Root / lemma: mehd-1 
57911:lemma: mehg(h)- : meg(h)- : big 
57992:Root / lemma: mehd-2 
58003:Root / lemma: mehg(h)- : m^(h)- 
58043:lemma: med-1\ to measure; to give adviee, healing. 
58098:Root / lemma: meihgh-, also meihk- 
58134:< kw\; alb. proves that from Root / lemma: mer-2, *extended mer-ek-\ "to shimmer, shine' 
58135:derived the truncated Root/ lemma: meigh-, also rneik-: "to glimmer, twinkle; mist'. 
58149:Root / lemma: meihgh- 
58198:Root / lemma: meih-g"- 
58215:Root/ lemma: me/h-R- {and meih-g-7) 
58257:Root / lemma: meih-1 
58298:Root / lemma: meih-2 
58337:Root / lemma: meih-3 
58368:Root / lemma: meih-4 
58394:Root / lemma: meih-5 mi-neu- 
58439:Root / lemma: meih-6, meihu-, min(u)-, mim(ei)- 
58460:Root / lemma: meih-no- 
58482:Root / lemma: meihs- 
58506:Root / lemma: meiht(h)-1 
58524:Root / lemma: meih-t(h)-2 
58575:Root / lemma: mehk- 
58601:Root / lemma: meh-1 
58644:Root / lemma: meh-2 
58675:Root / lemma: mehti^-1 
58705:Root / lemma: mehti^-2 
58719:Root / lemma: mehlgh- 
58734:Root / lemma: mehli-t 
58744:Root/ lemma: mehli-t\ "honey' : Root/ lemma: meM^u: "honey' derived from a truncated 
58746:Root /lemma: mehl-1 {auch smehl-), mehlah-- mie-, mehl-d-. ml-ed-, mehl-6'^-, ml-ei-: 
58792:Root / lemma: mehlk-1 
58810:Root / lemma: mehlk-2, mehlg- 
58824:Root /lemma: meh/-1 {a\so smehl-), mehlah-. mie-, mehl-d-. ml-ed-, mehl-d!^-, ml-ei-. mlF- 
59060:Root / lemma: mehl-2 
59074:Root / lemma: mehl-3 
59094:Root / lemma: mehl-4 
59122:Root / lemma: mehl-5 
59141:Root / lemma: mehl-6, mehlah- 
59192:Root / lemma: melo-, smelo-: small animal, derived from Root/ lemma: mel-6, mela- : 
59200:Root / lemma: mehl-7 
59214:Root / lemma: mehl-8, mehlah- : mlo- 
59254:Root / lemma: mehl6hd!^-{mohlahd!^-, molehd!^-) 
59273:Root / lemma: mehls- 
59287:Root / lemma: mehrrio^- 
59303:Root / lemma: mehnA^- 
59352:Root / lemma: mehnd-, mohnd- [mQd-l) 
59376:Root / lemma: mehnd^a, -om) 
59382:Root/ lemma: mehnd^a, -om)\ defect, flaw, *nnental disability, derived from Root/ lemma: 
59399:Root / lemma: mehn(e)hgh-, mohn(e)hgh-, mijgh- 
59418:Root / lemma: mehn(9)hk- 
59451:Root / lemma: mehng- 
59472:Root / lemma: mehn-1
```


## [2026-09-07T15:50:07.664Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"###### 57793 block\"; sed -n '57793,57850p' POK_full.txt\necho \"###### 58003 block\"; sed -n '58003,58045p' POK_full.txt"
}
```


### [2026-09-07T15:50:07.734Z] TOOL RESULT

```
###### 57793 block
Root / lemma: meM^i- meMNo- 

Meaning: middle 

Material: Old Indie madhya-, Avestan maidya-^ medial', Superl. Old Indie madhyama-, 

Avestan madema-' medial' (= Gothic miduma); 

Armenian mej^ center '; 

gr. (ep.) \xtaaoc,, (Attic) \xtaoc, " medial'; 

Maybe alb. /77es "middle'. 

Latin medius^ in the middle, in the midst, mid, mean, middle ', Oscan mefiaf^ in media '; 
Oscan /77ess//77as presumably " medioxim|s '; 

gall. Medio-lanum, -matrici. Old Irish mid-{*med'"u-) in compound " in the middle, in the 
midst, mid, mean, middle ', Middle Irish mide^ center', Mide^ county in the Republic of 
Ireland ' actually " middle province ', Old Irish i-mmedon^ in medio ', cymr. mewn, mcymr. 



mywn"\v\' {*medugno-); mcymr. mei-iau^ middle - yoke ' {*m&iNo^\ gall. FIN Meduansr, 
venet. FIN Meduanar, 

with prolonging of -s- from a Superl. probably also Old Irish /77e5S5"bad', actually ' 
average, middle ' (or to 2. meit(h)-, Germanic m/ssa-7); 

Gothic midjis. Old Icelandic midr. Old English midd. Old High German mitti^ in the 
middle, in the midst, mid, mean, middle ', Superl. Gothic miduma^\he middle'. Old 
Icelandic mjgdmi. "hip'. Old English m/dmesf't\r\e centermost'. Old English medeme. Old 
High German metemo^ of middling size, medium, middling, moderate, ordinary ' (: 
Ave Stan madama-) and Gothic *midjuma{= Old Indie madhyama-) in midjun-gards. Old 
English middan-geard^ earth circle ', Old High German mittamo^ of middling size, 
medium, middling, moderate, ordinary ', in mittamen^ amid, in the middle of; Old High 
German mittar^ in the middle, in the midst, mid, mean, middle '; 

Old Bulgarian mezda^road,' (originally " boundary strip '). 

Maybe alb. mezhde, mezhda^ baulk, strip of land between fields ' a Bulgarian loanword. 

russ. meza^ limit, boundary, slope ' (etc.). Old Bulgarian mezdu {Loc. Du.) " between ' 
Adv. preposition. Old Russian mezi{Lok. Sg.) ds.; here also probably as '* forest, 
boundary strip ': Old Prussian median, Latvian /77ezs'wood, forest', Lithuanian medzias 
"tree'; Lithuanian FIN Meduya. 

References: WP. II 261, WH. II 57 f., Trautmann 173, Specht Indo Germanic Dekl. 133 f. 
Page(s): 706-707 

Root / lemma: meljd^u 

Meaning: honey, intoxicating drink, mead 

Grammatical information: n. 

Note: actually nominalized adjective 'sweet' 

###### 58003 block
Root / lemma: mehg(h)- : m^(h)- 
Meaning: big 

Note: (to Old Indie Aspiration s. Pedersen 5^ decl. Latin 48^, Hittite 36, 181 f.); to reduced 
grade compare Pedersen Hittite 169 f. 

Material: Old Indie mahant-, Avestan mazant-^b\Q, large'. Old Indie mah-, Avestan maz- 
ds. (only out of Nom. Akk.), Old Indie mah/Hom. Sg. neutr. (-/= -a, then = gr. (jsya), as 
front part Old Indie maha- (Avestan mqza- is a text mistake), mostly extended mahat- = 
Avestan mazant-'b\g, large'; Kompar. Superl. Old Indie mahTyas-, mahistha-, Avestan 
mazyah-, mazista-; 

Old Indie mahayatr pleases, venerates', maha-rc\. " celebration, sacrifice, oblation', 
mahJyate^ rejoices '; Avestan mimayzo^ you should try to glorify ', that is to say "hold 
festivities'; 

Old Indie mahas-, Avestan mazah-n. "greatness, bulk, extent'. Old Indie majman- 
"greatness, bulk, extent', Avestan /775Z5/7- "greatness, bulk, extent, grandeur'. Old Indie 
mahV the great, the old people, the earth ' (: Latin Mala); 

Adv. Gatha-Avestan /775s "very' ( *meghs), zero grade ( *rnghs) jav. as "very'; 

Armenian /77ec"big, large', Denomin. mecarem' uphold, preserve, honour; ' (: gr. 
|j£Yaipoo); 

gr. (jsyac;, (jsyaAri, psya {*meg-n) "big, large' (to (jsya is v^t^cxc,, -av neologism; psyaAo- 
the case obi. and of Fem. contains *a/c»-" growth, stature ', as xQaijaAoq "low'); Kompar. 
Ionian Doric Arcadian [je^wv from *fj£Yju)v (Attic [jei^wv after xsipwv), Superl. fj£YiaTO(;; 
psyaipcjo (: Armenian mecarem) " schlage hoch an, bewundere; halte fur zu hoch, 
miflgonne '; zero grade from *rnYa aya- "very' (aYa-vvi(po(; etc.), ayav "to very', aya^u) 
"aegre fero', compare a^ov psyav, uijjeAov Hes. and jav. as- "very'; in addition probably gr. 
dyaopiai " envy', ayafjai " adore, venerate', ayaAAu) " glorify ', ayanau) "love', ayauoc; 
"admirable, venerable'; 

Note: 



zero grade of Old Indie addha {*md-6^§) "certainly ' : Avestan Old pers. azda6s., Old Indie 
addhatf- 'smart man, sage' similar to gr. zero grade of gr. *mYa aya- "very' see Root / 
lemma: med-1\ to measure; to give adviee, healing. 

alb. math, madh/"b\g, large', madhonj^ aggrandize, praise';
```


## [2026-09-07T15:50:14.532Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '58045,58100p' POK_full.txt\necho \"###### 57911 block\"; sed -n '57905,57925p' POK_full.txt"
}
```


### [2026-09-07T15:50:14.593Z] TOOL RESULT

```
alb. math, madh/"b\g, large', madhonj^ aggrandize, praise'; 

Maybe alb. zmadhof increase ' Slavic z- prefix. 

Note: 

Alb. math^b\g,: mcymr. ma/th'\ong, big' large' common alb. - mcymr. -k > -th. 

Latin magnus'b\g, large' {*meg-nd-s), Kompar. mag-is^ more, in a higher degree, more 
completely ', maior^ greater' {*meg-Jds), Superl. maximus {*meg-Semo-s)\ in addition 
maiestas^ greatness, grandeur, dignity, majesty ' {*meg-Jes-tat-), compare alb. madheshtf 
( *megis-t-iJS) ds. (about Oscan mais, maimas, Umbrian mestrusee below me- "big, large'), 
Maia " Daughter of Atlas and Pleione, and the mother of Mercury by Jupiter '; deus Maius 
"Juppiter' (Tusculum), whereof the month Maius {as Oscan Maesius^ May ' derives from 
the missing God's name, s. Schuize Eigenn. 469 ff.), Oscan PN Ma/'/ufDat Sg. (compare 
also Celtic magio-); Latin (Celtic, also alb.) -a- is Indo Germanic e, about Latin maialis^ a 
gelded boar, a barrow hog ' s. WH. II 13; 

Latin mactus' worshipped, honored ', /77ac/e" (sacrificial call) hail!', macto, -are^ to 
magnify, extol, honor, glorify, elevate, to offer, sacrifice, immolate, devote, to kill, slaughter, 
put to death, to overthrow, ruin, destroy, to afflict, trouble, punish '; magmentum' that 
which magnifies ' can be a formation of magnus aiter augmentum. 

Old Irish mochtae^b\g, large' (o!). Middle Irish maignech 6s. {*maginiakos, compare gall. 
Maginus; compare the />formsfrom Latin magnus). Middle Irish mag-, ma/ge^b\g, large', 
Pc»//77yC> A^5/ge"Pompeius Magnus', gall. Magio-rTx, Are-magios (formal = Latin Maius); 
Middle Irish mai {*magios) " noble person, prince, lord', gall. Magio-s\n gods- and PN, 
abrit. PN Mag/o-cune {cymr. Maei-gwn), Cuno-magius e\.c.\ gall. Maga/u Dat Sg. god's 
name, MagaiosPH, Middle Irish mag-iorg ^c\ub, mace, joint' {*mago-iorga large cudgel, 
club'), /77as5 "stately' ( */77a/r5C»5 compare Latin maximus), Kompar. Old Irish maissiu, cymr. 
corn, meiiinlat', Middle Breton biii/n' fullness; abundance ' {*magesTno-)\ mcymr. maon 
{*magones) " the big ', maitiilong, big, large' {*mag-tio-), probably also Old Irish do-for- 
maig^ to increase, augment, enlarge, spread, extend ', -magar^ to increase, augment, 
enlarge, spread, extend ', acymr. di-guor-mechis^ has increased ' (acymr. c/7from *-g-s-); 
to divide from cymr. magu^ bring up ' ( *mak-)\ 



whether Old Irish magu. " plain, the open countryside', mcymr. /77a- "place', gall. 
Arganto-magus {whereoi Irish /775^e/7 'place', cymr. maen, corn, men, bret. mean^ stone 
'), cymr. maes {*magesto-) "field', to Old Indie mahT^eartW? 

Gothic /77/Ms"big, large'. Old High German mihhil. Old Saxon mikil. Old English micel. 
Old Icelandic m/ke// ds., Old English mycel, Proto German 'Vr7/Maz probably with -/o suffix 
after /e////5. Old High German luzzi^. Old Icelandic mjgk^ye'cy' (engl. much) at first from 
*/r7e/ri/- after /e/i/"much, a lot of; 

Tocharian A mak, B /775/ra"big, large an number, much, a lot of; Hittite me-ik-ki-is 
{mekki§) "big, large'. 

References: WP. II 257 ff., WH. II 4 f., 10 ff., Szemerenyi Word 8, 48. 
Page(s): 708-709 

Root / lemma: meihgh-, also meihk- 
Meaning: to glimmer, twinkle; mist 
Material: 1 . meihgh-. 
###### 57911 block
Note: 



zero grade of Old Indie addha {*md-6^^ "certainly ' : Avestan Old pers. azda6s., Old Indie 
addhatf- 'smart man, sage' similar to gr. zero grade of gr. *mYa aya- "very' see Root / 
lemma: mehg(h)- : meg(h)- : big 



Armenian m/f{Gen. mti) "thought, notion, sense, mind' (: \ir\bzcx ete.); 

gr. |j£5o|jai "bin whereupon bedaeht', pi£5(jov, pisSswv "Walter, ruler', p£5iMV0(; " bushel '; 
lengthened grade pinSopai "ersinne, eateh einen Besehlufl', pnSea Nom. PI. "sorrows, 
advice^ounser^jnoKop^A^^ 

Latin meditor, -arf to reflect, muse, consider, meditate, give attention ', modus^ a 
measure, extent, quantity ', modestus^ keeping due measure, moderate, modest, gentle, 
forbearing, temperate, sober, discreet ', moderare^ to set a measure, set bounds, put 
restraint upon, moderate, mitigate, restrain, allay, temper, qualify ', modius' bushel ', 
Umbrian mefs, mers^ right, privilege; law ' {*med-os-), mersto^ just, upright, righteous,
```


## [2026-09-07T15:50:49.975Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN leaf 246 (p.225) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==247' HRN.txt | head -60"
}
```


### [2026-09-07T15:50:51.288Z] TOOL RESULT

```
=== HRN leaf 246 (p.225) ===
- 225 —
Weber, Sitzber. BAW. 1887, PärasTprakäija S. 5,
erklärt skr. mudrä" für *egyptisch*, aus ap. Mudräya-
entlehnt.
10O2. mih/mmfj mlhman (*mehman) 'Gast, Hausfreund'.
aw. i/^ma^f' , mi&naiti 'weilen , bleiben' — das np.
mihman lautlich genau entsprechende aw. ma^dman-
bedeutet nur 'Belegung (einer Hündin)'; phlv. mShmatt
Gast', m^hmänlh ; ai. vergl. mithds 'zusammen, gemein-
schaftlich'.
kurd. mevan 'Gast'; afy. nwlmana (Darmesteter);
sar. LW. meimdn,
1003. mei 'Wein, jüd.-pers., ^^O.
In np. mei, phlv. mai, vd. 5 (132), sind aw. madv-
'Honig', ai. mädhu- süss; Honig, Meth' und aw. maSa-
'Rauschtrank', ai. indda- das. zusammengefallen; vergl.
ksl. wedü 'Honig, Wein', nhd. Meth etc.
Hierher gehört auch np. meivlz {*meive2?) 'Rosine'
(AM. 174 Zeile 5 und 1 v. u.), gewöhnlich mevlZy
das bereits de Goeje, Bibl. geogr. arab. IV, 359
(Low, Aram. Pflanzennamen, S. 91) als persisch in
Anspruch genommen hat. Die zweite Silbe ist un-
klar. MtvTze^ mlvtzaj 'Convolvulus' ist vielleicht ein
ganz anderes Wort.
1004. miyün 'Mitte; mitten, mittlerer, miyäne,
aw. maiöyqna- 'Mitte'; phlv. miyän; ai. vergl.
mddhya- 'Mitte'; arm. mEj 'Mitte* (H. No. 199).
kurd. LW. maiyän ; af /. manj, miyanj (Suffix echt) ;
oss. d. medäg, t. mJdäg (186) ; bei. LW. niyäm, niymfg,
niyOmay (265) ; wa/. inalung, siyn. meSina, sar. madän
'Mitte, wa/. tnalungüng, sar. maöänenj 'mittlerer*.
1005. mex Pflock, Nagel'.
ai. vergl. mayukha- 'Pflock' (?).
LW\ kurd. mix; af/. we/, meyöü 'Nagel, Pflock';
oss. d. mex, t. mix 'Pfahl (187); bei. meh (239);
wa/. mix, sar. max,
bei. mik aufgerichtet' (239), das Geiger ansehliesst.
Uorn. Orundriss <J. neup. Fltyniolo^ic. ],j
```


## [2026-09-07T15:50:57.100Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN p.224 ===\"; awk 'BEGIN{RS=\"\\f\"} NR==246' HRN.txt | head -60\necho \"=== grep meh/mih great in HRN ===\"; grep -n -i 'mihist\\|mahist\\|mehist\\|gross' HRN.txt | sed -n '1,40p'"
}
```


### [2026-09-07T15:50:58.501Z] TOOL RESULT

```
=== HRN p.224 ===
— 224 —
Studien, II, 178, befriedigt nicht, da er müye^ nicht
7nöye, als np. Form ansieht.
Fr. Müller, (WZKM. 5, 65) construirt eine *[/maud-
mit einem ap. "^matida-- als Grundform und identi-
ficirt np. möye mit arm. moir 'Bettelei', eigentlich
Torjammern', moiracik 'bettelnd' ; dazu auch np. mit st
*Klage*, mustmeud,
998. me (geschrieben meh) nicht* (prohibitiv).
ap. aw. ai. ma 'nicht' (fifj); päz. mo ; arm. mi 'dass
nicht* (H. No. 200).
kurd. me-; afy. ma-; oss. d. t. ma- nicht' (prohi-
bitiv) (173).
999. mih gross*, mehist ^), mihtnj mihter.
g. mas gross*, master.
ap. vergl. ma&ista- grösster*; aw. masyao grösser*;
phlv. mas gross, grösser, grössest', masist, mas(i)st,
vergl. 7nas[mayan *Grossmagier (AlbSnlnl), masTh%
mahist, päz. meh (PPGL); arm. vergl. mec gross' (H.
No. 191).
af/. masar 'älter, Herr*.
Vergl. zu bih (No. 241).
1000. mihr *Sonne; Liebe', mihr[ban 'freundlich, wohl-
wollend*.
ap. Mid^ra^, vergl. Vaulmisa-; aw. Mi&ra-, mi&ra^
'Vertrag*; phlv. mür, päz. mihir (vergl. Meherdates,
Tac, MsQfiBQorig^ Proc, skr. LW. mihird- *Sonne');
ai. Mitrd", mitrd- 'Freund*.
minj. mira 'Sonne.
1001. muhr 'Siegel; Siegelring,
skr. mudrd- 'Siegel, Siegelring; phlv. mutrOk d. i.
mudrak 'B,ing'(?), vd. 2 (18) Gl.^), nmdar, muhr 'Siegel'
(PPGL), chald. LW. piniD, arm. LW. murhak.
LW. kurd. mör (H.-Sch.); oss. mi/ur; bei. vergl.
murdan, murdänay 'Finger* (No. 242).
^) Belege aus dem äähnäme (Maoan) bei Noldeke, ZDMO.,
46, 139.
*) P.-Vend. masäi (vergl. dräjlh^ No. 547).
*j Darmesteter, 6t. ir. I, 93 Note 3 (sehr unsicher).
=== grep meh/mih great in HRN ===
89:nannt*). Eine grosse Anzahl ist längst zum Gemeingut
297:Sie tiberliefern häufig augenscheinliche Fehler mit grosser
1528:*Daunien, grosse Zehe*.
1692:147. bäb Tater (JSähn. I, 43 Vers 172), Grossvater, vergl.
1698:arm. LW. pap^) 'Gross vater*.
1896:np. välä gross* wird auch hierher gehören und nicht
2256:214. buzurg 'gross'.
2268:ap. vazarka- gross*; phlv. vajarg (Bund., zu lesen
2669:ulu 'gross*.
3315:kurd. afy. LW. pTr; hei, ptrük, n. plrük 'Grossvater'
5041:561. (lerj/ä *Meer; grosser Fluss', jüd.-pors. nxni (Is. 8,
5194:döz-em, döz, dözene, kun\döz grosse Nadel' (AM. 52
5914:670. ^eii<J gross, stark', vergl. zende plV),
6141:oss. d. t. afsady t. ä/sud grosse Menge, xVbteilung
6266:715. sntuvff, sittirg 'stark, gross*.
6267:ai. sthürd- 'dick, breit\ sthülä- 'grob, dick, gross,
6269:kurd. nstär; oss. d, sfiir^ t. sfir gross, stark' (232);
7811:z. B. hi^-l gräi 'grosse Unreinheit*?), vergl. np. giräi No. 5 bei
8289:ai. V^mah' ist wohl von mah- 'gross' abgeleitet (dies
8291:mahfydtS ursprünglich, *er tut, als wenn er gross wäre*.
8339:wa;K. müm, aar. mäm 'Grossmutter ; af/. mäml'Tdnte;
8340:gr. jLidinfia^ ^afA.fA.riy jLta/4f.da *Mama, Grossmutter ; lat.
8341:wamma, wammula 'Mama, Grossmutter ; ahd. muoma,
8542:aw. musti.[masah' 'faustgross* ; phlv. must (vd. 17
8687:999. mih gross*, mehist ^), mihtnj mihter.
8688:g. mas gross*, master.
8690:phlv. mas gross, grösser, grössest', masist, mas(i)st,
8691:vergl. 7nas[mayan *Grossmagier (AlbSnlnl), masTh%
8692:mahist, päz. meh (PPGL); arm. vergl. mec gross' (H.
9053:bei. vergl. nänö, nana *Grossvater' , nam *Gross-
9193:1062. niyä 'Grossvater, Ahne (Plur. myagän),
9194:ap. aw. nyäka- *Grossvater , vergl. ap. apangäka'
9196:af;'. nlka *6rossvater, LW. niya 'Grossmutter*;
9197:bei. näkü, n. nüxö 'Oheim* (258), fwl^ *Grossnuitter'
9511:niOl. heftöreuff 'Grosser Bär (Sternbild)'^).
9512:aw. haptöiringa- 'Grosser Bär; phlv. haftökrany
9872:'Grossvater' etc., Delbrück, Verwandtschaftsnamen
```


## [2026-09-07T15:51:20.003Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN middle ===\"; grep -n '^middle,' KLN_1966.txt | head\necho \"=== KLN mid, ===\"; grep -n '^mid,' KLN_1966.txt | head\necho \"=== KLN mega ===\"; grep -n '^mega-\\|^megalo-\\|^much,\\|^more,' KLN_1966.txt | head"
}
```


### [2026-09-07T15:51:20.085Z] TOOL RESULT

```
=== KLN middle ===
23847:middle,  adj.  —  ME.  middel,  fr.  OE.  middel,  rel.  to OS.  middil,  MLG.,  Du.  middel,  OHG.  mittil, MHG.,  G.  mittel,  ‘middle’  and  to  OE.  midd, ‘mid’.  See  mid,  adj.
23848:middle,  n.  —  Subst.  use  of  middle,  adj.  Cp.  G. Mittel,  n.,  fr.  mittel,  adj.
=== KLN mid, ===
23844:mid,  prep.,  amid.  —  Aphetic  for  amid.
=== KLN mega ===
23388:much,  quite’,  paXXov,  ’more,  rather’  (changed from  original  *p£XXov,  under  the  influence  of ■9-aTTOV,  Oaaaov,  ‘quicker,  sooner,  rather'),  p<£- Xiaroc,  ‘most,  most  strongly’,  L.  multus  (for *mltos ),  ‘much’,  Lett,  milns,  ‘very  much’.  See multi-  and  verbal  suff.  -ate  and  cp.  ameliorate. Derivatives:  meliorat-ion,  n.,  meliorat-ive,  adj., meliorat-or,  n.
24396:more,  adj.  —  ME.  more,  fr.  OE.  mara,  ‘larger, greater,  more'  (used  as  compar.  of  mice),  ‘large, great,  much’) ;  rel.  to  OE.  ma,  ‘more’  (neut.  and adv.),  OS.  mera,  adj.,  mer,  adv.,  ON.  meiri,  adj., meirr,  meir,  adv.,  OFris.  mara,  mera,  adj.,  ma, me  (also  mar,  mer),  adv.,  MDu.  mere,  metre, adj.  and  adv.,  mee,  adv.,  Du.  meer,  adv.,  OHG. mero,  adj.,  mer,  adv.,  MHG.  mere,  adj.,  mer, adv.,  G.  mehr,  adj.  and  adv.  (cp.  the  adjectives with  double  compar.  suff.  Du.  meerder,  ‘more, greater’,  OHG.  meroro,  meriro,  ‘greater’,  MHG. merer,  metre,  G.  mehrere,  ‘several’),  Goth. maiza,  adj.,  mais,  adv.,  OE.  mSre,  OHG.  mari, ‘great,  glorious,  famous’,  and  cogn.  with  Aves- tic  mazjd,  ‘greater’,  OIr.  mor,  mar,  ‘great’,  mdu, mo,  ‘more’,  Homeric  Gk.  ^yxsof-ptopo?,  ‘great with  the  £yx°$  >  i-e-  ‘great  with  the  spear’.  Os- can  mais,  ‘more’.  Cp.  most.
```


## [2026-09-07T15:51:27.565Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n 'mid,  adj' KLN_1966.txt | head\necho \"---\"\nsed -n '23830,23850p' KLN_1966.txt"
}
```


### [2026-09-07T15:51:27.629Z] TOOL RESULT

```
18225:humid,  adj.  —  F.  humide,  fr.  L.  {h)i2midus,  ‘moist, wet’,  fr.  {h)umere,  ‘to  be  moist  or  wet’.  See
23841:micturition,  n.,  1)  a  morbid  desire  to  urinate;  2) excessive  urination;  3)  the  act  of  urinating.  — Formed  with  suff.  -ion  fr.  L.  mictiirit-(um),  pp. stem  of  micturire  ‘to  desire  to  urinate’,  desider- ativeofmmgere.pp.  stem  mict-(um),  ‘to  urinate’, which  is  rel.  to  meiere  (for  *meighiere),  of  s.m., and  cogn.  with  OI.  mehati,  ‘urinates’,  pp.  midhdh, Avestic  maezaiti,  ‘urinates,  manures,  dungs’, Gk.  opslxstv,  dpu/eiv,  ‘tourinate’,  poi/oq,  ‘adul¬ terer’,  Arm.  mez,  ‘urine’,  mizem,  ‘I  urinate’, (prob.  denominated  fr.  mez),  Toch.  B  mi  so, ‘urine’,  earlier  Lith.  minzu,  Lith.  m^zu,  Lett. mizu,  ‘I  urinate’,  OE.  migan,  ON.  miga,  MLG. migen ,  ‘to  urinate’,  OE.  miega,  migoda,  ‘urine’, Goth,  malhstus,  OE.  meox,  ‘dung,  filth’.  See masb,  n.,  and  cp.  mistletoe, mixen.  For  the  desid- erative  suff.  -iirire  in  L.  micturire  cp.  Abiturient and  words  there  referred  to. mid,  adj.  —  ME.,  fr.  OE.  midd,  rel.  to  ON.  midr, OS.  middi,  OFris.  midde,  OHG.  mitti,  Goth. midjis,  ‘mid’,  and  cogn.  with  OI.  mddhyah,  Gk. \Lzaoq,  L.  medius,  ‘middle’.  See  media,  ‘voiced stop  consonant’,  and  words  there  referred  to and  cp.  esp.  middle.
23845:Midas,  n.,  a  king  of  Phrygia,  to  whom  Dionysus granted  the  favor  of  turning  everything  he touched  into  gold  ( Greek  mythol.)  —  L.,  fr.  Gk. M£8a? ;  of  Phrygian  origin, midday,  n.,  the  middle  of  the  day,  noon.  —  ME., fr.  OE.  midddxg.  See  mid,  adj.,  and  day. midden,  n.,  1)  a  dunghill;  2)  a  prehistoric  refuse.
23847:middle,  adj.  —  ME.  middel,  fr.  OE.  middel,  rel.  to OS.  middil,  MLG.,  Du.  middel,  OHG.  mittil, MHG.,  G.  mittel,  ‘middle’  and  to  OE.  midd, ‘mid’.  See  mid,  adj.
23857:midrash,  n.,  exposition  of  the  Holy  Scriptures ( Hebrew  literature).  —  Heb.  midhrdsh,  ‘study, exposition’,  in  Mishnaic  Hebrew,  ‘homiletical interpretation’,  fr.  Heb.  ddrash ,  ‘he  sought,  in¬ quired,  investigated’,  in  Mishnaic  Heb.  also  he expounded,  interpreted’;  hence  Aram,  d  rash , ‘he  searched  out,  investigated,  interpreted’,  and — through  the  medium  of  this  latter — Arab. ddrasa,  ‘he  read  repeatedly,  he  studied’,  Ethiop. darasa,  ‘he  expounded’.  Cp.  madrasah, midriff,  n.,  the  diaphragm.  —  ME.  mydrif,  fr.  OE. midhrij,  a  compound  of  OE.  midd  (see  mid,  adj.) and  hrif,  ‘belly  ,  which  is  rel.  to  OHG.  href. OFris.  hrif  href,  ‘belly’,  OHG.  href,  ‘body’,  and cogn.  with  L.  corpus,  ‘body’.  See  corpus  and  cp. words  there  referred  to.
23858:midst,  n.  —  ME.  middest,  midest,  formed  with intensive  suff.  -t  fr.  middes,  mides,  adverbial  gen. of  mid.  See  mid,  adj.,  and  cp.  amid,  amidst. Cp.  also  against  and  words  there  referred to.
23861:OE.  midsumor.  See  mid,  adj.,  and  summer, midwife,  n.  —  ME.  midwif,  fr.  OE.  mid,  with , and  wif,  ‘wife,  woman’.  The  first  element  is  rel. to  Goth,  mip,  ON.  med,  ‘with’,  and  cogn.  with Gk.  pcxi,  ‘between,  among,  with,  after’;  see meta-.  For  the  second  element  see  wife. Derivatives:  midwife,  tr.  v.,  midwifery  (q.v.) midwifery,  n.  —  A  hybrid  formed  fr.  midwife and  -ery,  a  suff.  of  Romance  origin, mien,  n.,  manner,  demeanor,  appearance.  F. mine,  ‘look,  appearance,  mien’,  borrowed  fr. Bret,  min,  ‘beak,  muzzle,  nose’;  prob.  influ¬ enced  in  meaning  by  the  verb  de-mean. miff,  n.,  a  trifling  quarrel;  tr.  v.,  to  put  or  be  out of  humor.  —  Orig.  exclamation  of  disgust.  Cp. G.  muffen,  ‘to  sulk’.
39284:timid,  adj.,  fearful.  —  L.  timidus,  ‘faint-hearted, cowardly,  timid’,  fr.  timere,  ‘to  fear’,  which  prob. meant  orig.  ‘to  be  in  the  dark,  to  grope  about  in the  dark’,  and  is  rel.  to  tenebrae  (for  *temebrae, fr.  *temesrae),  ‘darkness’,  temere,  ‘rashly,  at random’,  prop,  ‘in  the  dark’,  and  cogn.  with  OI. tamas-,  ‘darkness’,  tamsrah,  ‘dark’.  See  temerity and  1st  -id.
40426:tumid,  adj.  —  L.  tumidus,  ‘swollen’,  formed  with suff.  -idus  (see  -id)  fr.  tumere,  ‘to  swell’,  which is  rel.  to  tumor,  ‘swelling,  protuberance',  tumu¬ lus,  ‘a  raised  heap  of  earth,  a  mound’,  and  cogn. with  OI.  tutumah,  ‘fruitful,  strong’,  tumrah,  ‘tur¬ gid,  fat’,  Avestic  tuma,  ‘fat’,  OE.  puma,  ’thumb’, pymel,  ’thimble',  fr.  I.-E.  *tumo-,  enlargement of  base  ‘tu-,  'to  swell’,  whence  also  Gk.  niXo?, T‘j>.7),  ‘a  swelling,  rising',  OSlav.  tyjg,  tyti,  ‘to become  fat',  tuku,  ‘fat’,  Lith.  taukai,  ‘fat’,  tau- kas,  ‘pieces  of  fat’,  tunku,  tiikti,  Lett,  tukt,  ‘to  be¬ come  fat',  OE.  peoh,  pioh,  ‘thigh’,  and  the  first element  in  OSlav.  tysgsta,  tysqsta,  Goth,  pusun- di.  OE.  pusend,  thousand’.  Cp.  tumefy,  tumor, tumult,  tumulus,  intumesce.  Cp.  also  obturate. Satyr,  soma,  body’,  tomb,  tomentum,  total, tuber,  tarion,  t.vlarus,  tyloma,  tylosis,  Typha, tyro-,  and  the  second  element  in  catacomb.  Cp. also  thigh,  thimble,  thole,  n.,  thumb  and  the  first element  in  thousand.
---
Derivatives:  micrometr-ic,  adj.,  micrometr-y,  n. micron,  n.,  one-millionth  part  of  a  meter.  — ModL.,  fr.  Gk.  pfxpov,  neut.  of  pixpo?,  ‘small’. See  micro-.
Micronesia,  n.,  groups  of  small  islands  in  the western  Pacific,  north  of  the  equator  and  east  of the  Philippines.  —  Compounded  of  micro-  and Gk.  vijao ?,  ‘island’,  which  is  prob.  rel.  to  vrj- -/etv,  ‘to  swim’.  See  Indonesia  and  cp.  words there  referred  to.
Derivatives:  Micronesi-an ,  adj.  and  n. microorganism,  n.,  a  microscopic  organism.  — Compounded  of  micro-  and  organism, microphone,  n.,  an  instrument  for  intensifying small  sounds.  —  Compounded  of  micro-  and Gk.  9covf),  ‘voice,  sound'.  See  phone,  ‘speech sound’.
microphotograpb,  n.,  a  very  small  photograph.  — Compounded  of  micro-  and  photograph, microphyte,  n.,  a  microscopic  plant,  esp.  a  bac¬ terium.  —  Compounded  of  micro-  and  Gk. (puTov,  ‘a  plant’.  See  -phyte.
Derivative:  microphyt-ic,  adj. microscope,  n.  —  ModL.  microscopium,  lit.  ‘an instrument  for  examining  small  objects’ ;  com¬ pounded  of  micro-  and  Gk.  -oxomov,  fr.  oxo- ratv,  ‘to  look  at,  examine’.  See  -scope. Derivatives:  microscop-ic,  microscop-ic-al,  adjs.,
microscop-ic-al-ly,  adv.,  microscop-ist,  n.,  mi¬ cr oscop-y,  n.
microsome,  n.,  one  of  the  minute  granules  in  the protoplasm  (biol.)  —  Compounded  of  micro- and  Gk.  ocbpa,  ‘body’.  See  soma,  ‘body’, microspore,  n.,  a  minute  spore  (hot.  and  zool.)  — Compounded  of  micro-  and  Gk.  ct7ropa,  ‘a sowing,  seed’.  See  spore.
Derivatives:  microspor-ic,  microspor-ous,  adjs. microstomatous,  adj.,  having  a  small  mouth.  — Compounded  of  micro-  and  Gk.  crrbpa,  gen. aT6(j.aToc,  ‘mouth’.  See  stoma  and  -ous. microstomous,  adj.,  microstomatous.  —  See  prec. word.
microtia,  n.,  abnormal  smallness  of  the  ear  (med.) —  Medical  L.,  compounded  of  micr-  and  Gk. o5s,  gen.  taro;,  ‘ear’.  See  oto-  and  1st  -ia  and cp.  Microtus.
Microtinae,  n.,  pi.,  a  subfamily  of  rodents,  the field  voles  and  the  lemming  mice  (zool.)  — ModL.,  formed  with  suff.  -inae  fr.  Microtus (q.v.)
microtome,  n.,  an  instrument  for  cutting  thin  sec¬ tions  for  examination  under  the  microscope.  — Compounded  of  micro-  and  Gk.  -Topov,  fr. ziiioq,  ‘a  cutting,  a  piece  cut  off".  See  -tome. Derivatives:  microtom-ic,  adj.,  microtom-y,  n. Microtus,  n.,  the  typical  genus  of  the  Microtinae (zool.)  —  ModL.,  compounded  of  micr-  and  Gk. oSc,  gen  iizOc,  ‘ear’.  See  oto-  and  cp.  microtia, microzyme,  also  microzyma,n.,  a  zymotic  microbe (biol.)  —  F.  microzyme,  coined  by  the  French physician  and  chemist  Pierre-Jacques  B6champ (1816-1908)  fr.  Gk.  pTxp6?,  ‘small’,  and  £upv], ‘leaven’.  See  micro-  and  zyme. micturate,  intr.  v.,  to  urinate.  —  Formed  irreg¬ ularly  fr.  L.  micturire.  See  next  word  and verbal  suff.  -ate.
micturition,  n.,  1)  a  morbid  desire  to  urinate;  2) excessive  urination;  3)  the  act  of  urinating.  — Formed  with  suff.  -ion  fr.  L.  mictiirit-(um),  pp. stem  of  micturire  ‘to  desire  to  urinate’,  desider- ativeofmmgere.pp.  stem  mict-(um),  ‘to  urinate’, which  is  rel.  to  meiere  (for  *meighiere),  of  s.m., and  cogn.  with  OI.  mehati,  ‘urinates’,  pp.  midhdh, Avestic  maezaiti,  ‘urinates,  manures,  dungs’, Gk.  opslxstv,  dpu/eiv,  ‘tourinate’,  poi/oq,  ‘adul¬ terer’,  Arm.  mez,  ‘urine’,  mizem,  ‘I  urinate’, (prob.  denominated  fr.  mez),  Toch.  B  mi  so, ‘urine’,  earlier  Lith.  minzu,  Lith.  m^zu,  Lett. mizu,  ‘I  urinate’,  OE.  migan,  ON.  miga,  MLG. migen ,  ‘to  urinate’,  OE.  miega,  migoda,  ‘urine’, Goth,  malhstus,  OE.  meox,  ‘dung,  filth’.  See masb,  n.,  and  cp.  mistletoe, mixen.  For  the  desid- erative  suff.  -iirire  in  L.  micturire  cp.  Abiturient and  words  there  referred  to. mid,  adj.  —  ME.,  fr.  OE.  midd,  rel.  to  ON.  midr, OS.  middi,  OFris.  midde,  OHG.  mitti,  Goth. midjis,  ‘mid’,  and  cogn.  with  OI.  mddhyah,  Gk. \Lzaoq,  L.  medius,  ‘middle’.  See  media,  ‘voiced stop  consonant’,  and  words  there  referred  to and  cp.  esp.  middle.
mid
978
mid,  prep.,  amid.  —  Aphetic  for  amid.
Midas,  n.,  a  king  of  Phrygia,  to  whom  Dionysus granted  the  favor  of  turning  everything  he touched  into  gold  ( Greek  mythol.)  —  L.,  fr.  Gk. M£8a? ;  of  Phrygian  origin, midday,  n.,  the  middle  of  the  day,  noon.  —  ME., fr.  OE.  midddxg.  See  mid,  adj.,  and  day. midden,  n.,  1)  a  dunghill;  2)  a  prehistoric  refuse.
—  ME.  midding,  fr.  Dan.  madding,  fr.  earlier megdynge,  ‘dunghill’,  which  is  compounded  of meg,  ‘muck,  dung’,  and  dynge,  ‘heap  of  dung’. See  muck  and  dung.
middle,  adj.  —  ME.  middel,  fr.  OE.  middel,  rel.  to OS.  middil,  MLG.,  Du.  middel,  OHG.  mittil, MHG.,  G.  mittel,  ‘middle’  and  to  OE.  midd, ‘mid’.  See  mid,  adj.
middle,  n.  —  Subst.  use  of  middle,  adj.  Cp.  G. Mittel,  n.,  fr.  mittel,  adj.
Derivative:  middle,  tr.  v. middling,  adj.  and  n.  —  Formed  fr.  middle  with suff.  -ing.
middy,  n.,  midshipman  ( colloq .)  —  Shortened  fr. midshipman.
```


## [2026-09-07T15:51:36.419Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n '^95[0-9]$' KLN_1966.txt | head -20\necho \"=== media entry ===\"; grep -n '^media,\\|^medial,\\|^median,\\|^medium,\\|^Mediterranean' KLN_1966.txt | head"
}
```


### [2026-09-07T15:51:37.734Z] TOOL RESULT

```
23169:950
23233:953
23300:957
23340:958
=== media entry ===
23269:media,  n.  pi.  —  PI.  of  medium, medial,  adj.,  situated  in  the  middle.  —  Late  L. medidlis,  fr.  L.  medius.  See  media,  ‘voiced  stop consonant’,  and  adj.  suff.  -al.
```


## [2026-09-07T15:51:40.012Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '23233,23300p' KLN_1966.txt"
}
```


### [2026-09-07T15:51:40.063Z] TOOL RESULT

```
953
sense  development  cp.  Rum.  tandr,  young  ,  fr- L.  tener,  ‘soft,  tender’),  OPruss.  maldaisin  (acc.), ‘youngest’,  maldian,  ‘foal’,  OSlav.  mladu,  Russ. molodH,  ‘young’,  OE.  meltan,  mieltan,  ‘to  melt', prob.  also  OIr.  meldach,  ‘pleasant’.  From  base *mel-dh-,  a  -^-enlargement  of  base  *mel-,  de¬ rive  Gk.  paXffaxo?,  ‘soft’,  OE.  melde,  OS. maldia,  OHG.  melta,  molta,  multa,  MHG.,  G. melde,  ‘orach’,  Goth,  mildeis,  OE.  milde,  mild  . (OIr.  meldach  and  the  Balto-Slav.  words  cited above  as  derivatives  of  base  *mel-d-,  could  also be  derived  from  base  *mel-dh-.)  Cp.  amalgam, Amalthaea,  ambly,  blenno-,  blite,  emollient, emolument,  immolate.  Maelstrom,  malaco-  ma¬ lax,  malt,  meldometer,  mellow,  melt,  ‘to  dissolve’, mild,  mildew,  mill,  millet,  milt,  moil,  molar, ‘grinding’,  mold,  ‘soil’,  mole,  ‘false  conception’, molinary,  mollify,  Mollugo,  mollusk,  mouille, moulin,  mulch,  muliebrity,  mull,  ‘to  powder’, mull,  ‘a  snuff  box’,  mullein,  muller,  mullet,  ‘star’, multure,  mylo-,  ormolu.
Derivatives:  meal-y,  adj.,  meal-i-ness,  n. meal,  n.,  food  taken  at  one  time.  —  ME.  mele,  fr. OE.  mil,  ‘mark,  sign ;  measure;  fixed  time;  time for  taking  food,  meal’,  rel.  to  ON.  mal,  ‘meas¬ ure,  time,  meal’,  OFris.  mel(tid),  (time  of) meal’,  Du.  maal,  ‘time;  meal’,  OHG.,  MHG-. mal,  ‘time;  meal',  G.  Mal,  ‘time’,  Mahl,  meal  , Goth,  mel,  ‘time;  hour’,  fr.  I.-E.  base  *me-,  to measure’.  See  meter,  ‘poetical  rhythm  . Derivative:  meal,  tr.  v.,  to  have  a  meal.
-meal,  suff.  denoting  quantity  taken  at  one  time; now  used  only  in  piecemeal.  —  ME.  -mele,  fr. OE.  -mxlum,  dat.  pi.  of  OE.  mil,  ‘measure’. See  meal,  ‘food’.
mealie,  n.,  maize.  —  S.  Afr.  Du.  milje,  fr.  Port.
milho,  ‘millet’,  fr.  L.  milium,  ‘millet’.  See  millet. mean,  tr.  v.,  to  have  in  mind.  —  ME.  menen,  fr. OE.  mxnan,  ‘to  mean,  signify,  intend;  to  speak of;  to  complain,  mourn,  moan’,  rel.  to  OS. me, nan,  ‘to  have  in  mind,  intend,  signify’, OFris,  mena,  MDu.  menen,  Du.  menen ,  OHG. meinan,  meinen,  MHG.,  G.  meinen,  to  think, suppose,  be  of  opinion',  fr.  I.-E.  base  *mam-, *mein-,  ‘to  be  of  opinion,  think  ,  whence  also OSlav.  mdniti,  ‘to  think,  have  an  opinion’,  OIr. mian,  ‘wish,  desire’,  Ir.  mian,  ‘intention’,  W. mwyn,  ‘enjoyment’.  Cp.  moan.
Derivatives:  mean-ing,  n.  and  adj.,  meaning-ful, adj.,  mean-ing-less,  adj.,  mean-ing-ly,  adv., mean-ing-ness,  n.
mean,  adj.,  intermediate.  —  ME.  mene,  fr.  Or. meien,  moien  (F.  moyen),  ‘middle’,  fr.  Late  L. medidnus,  ‘that  which  is  in  the  middle’,  fr.  L. medius,  ‘middle’.  See  media,  ‘voiced  stop  con¬ sonant’,  and  cp.  median,  mesne,  monial. Derivative:  mean,  n.,  something  intermediate, mean,  adj.,  of  low  rank,  inferior,  base.  —  ME. mene,  ‘common,  mean',  fr.  OE.  (ge)mine,  com¬ mon’,  rel.  to  OS.  gimeni,  OFris.  mene,  OS.  gi- meni,  MLG.  gemeine,  gemene  (whence  Dan.  and Swed.  gemen),  MDu.  ghemene,  Du.  gemeen,
OHG.  gimeini,  MHG.,  G.  gemein,  Goth,  ga- mains,  ‘common’,  OE.  man,  ON.,  OHG.  mein, OS.,  OFris.  men,  ‘false’,  OE.  manad,  OE., ON.,  meineidr,  Dan.,  Swed.  mened,  OS., OFris.  meneth,  MDu.  meineet,  Du.  meineed, OHG.  meineid,  MHG.  meineit,  G.  Meineid, ‘perjury’,  lit.  ‘false  oath’,  and  cogn.  with L.  miinus  (OL.  moinos,  moenus),  ‘service,  of¬ fice,  function’,  munia  (OL.  moenia),  ‘official, duties,  functions’,  communis  (OL.  acc.  comoi- nem),  ‘common’,  OSlav.  mdna,  ‘change’,  iz- meniti,  ‘to  change,  exchange’,  Lith.  mainas,  ‘ex¬ change’,  mainyti,  ‘to  exchange’,  OI.  menift,  ‘ven¬ geance’,  Avestic  maeni-,  ‘punishment’.  All  these words  derive  fr.  I.-E.  *mein-,  *moin-,  -n-enlarge- ments  of  base  *mei-,  *moi-,  ‘to  change,  ex¬ change’,  whence  OI.  mdyate,  ‘changes’,  Lett. miju,  mit,  ‘to  change’.  Cp.  common,  adj.,  and words  there  referred  to.  For  I.-E.  *mei-t-, *moi-t-,  -(-enlargements  of  base  *mei-,  *moi-, see  mutable,  mutual.  Base  *mei-,  ‘to  change",  is originally  identical  with  base  *mei-,  ‘to  change one’s  place,  to  go’.  See  meatus,  migrate, meander,  n.,  winding,  as  of  a  river.  —  L.  Maean- der,  fr.  Gk.  MoaavSpcx;,  a  river  in  Caria,  noted for  its  windings.
Derivatives:  meander,  intr.  v.,  meander-ing,  n. and  adj.,  meander -ing-ly,  adv. measles,  n.  pi.  —  ME.  maseles,  pi.  of  masel,  lit. ‘spot,  excrescence’,  rel.  to  MDu.  masel,  Du. mazelen,  G.  Maseru,  ‘measles’,  and  to  E.  mazer (q.v.)  E.  measles  was  influenced  both  in  form and  pronunciation  by  a  confusion  with  ME. mesel,  ‘leper’,  which  derives  fr.  OF.  mesel,  fr.  L. misellus,  dimin.  of  miser,  ‘wretched,  unfor¬ tunate,  miserable’.
Derivative:  measl-y,  adj. measurable,  adj.  —  ME.  mesurable,  fr.  OF.  (=  F.) mesurable,  fr.  Late  L.  mensurabitis,  fr.  mensu- rare,  fr.  L.  mensura.  See  measure  and  -able  and cp.  mensurable.
Derivatives:  measurabil-ity,  n.,  measurable-ness, n.,  measurabl-y,  adv.
measure,  n.  —  ME.  mesure,  fr.  OF.  (=  F.)  me- sure,  fr.  L.  mensura,  ‘measure’,  fr.  mensus,  pp. of  metiri,  ‘to  measure’.  See  mete,  ‘to  measure’, and  -ure  and  cp.  meter,  ‘poetical  rhythm’.  Cp. also  admeasure,  immeasurable,  measure,  men¬ surable,  mensurate,  commensurable,  dimension, immense.  Cp.  also  1  st  mensal.
Derivatives:  measure,  tr.  and  intr.  v.,  measur-ed, adj.,  measur-ed-ly,  adv.,  measur-ed-ness,  n., meas¬ ure-! ess,  adj.,  measure-less-ly,  adv.,  measure- less-ness,  n.,  measure-ment,  n.,  measur-er,  n. meat,  n.,  —  ME.  mete,  fr.  OE.  mete,  rel.  to  OS. med,  OFris.  mete,  ON.  matr,  OHG.  mas,  Goth. mats,  ‘food’,  MLG.,  MDu.,  Du.  metworst,  G. Mettwurst,  ‘German  sausage’,  fr.  Teut.  *mali-, ‘food’,  fr.  I.-E.  base  *mad-,  ‘wet,  moist,  drip¬ ping;  to  drip’,  whence  OI.  mddati,  ‘boils,  bub¬ bles,  gets  drunk’,  medas-,  ‘fat’  (n.).  Alb.  man,  ‘I fatten,  feed’,  Gk.  paSav,  ‘to  be  wet,  to  flow’.
paSapop,  ‘wet,  watery’,  paSaptomp,  ‘baldness’, L.  madere,  ‘to  be  wet;  to  be  drunk,  to  be  intoxi¬ cated’,  rnadidus,  ‘moist,  wet,  drunk ;  intoxicated’, mattus,  ‘intoxicated’,  OE.  mxst,  ‘mast  (of beech)’,  msestan,  ‘to  fatten’,  OIr.  mat,  ‘pig, swine’  (prop,  ‘a  fattened  animal'),  Oir.  maisse (for  *mad-tja),' food’.  Cp.  the  second  element  in laemus.  Cp.  also  madarosis,  mast,  ‘fruit  of beech’,  masto-,  mastoid,  mate,  ‘companion’, mattoid,  must,  ‘frenzied’.  For  sense  develop¬ ment  of  OE.  mete,  etc.,  ‘food’,  into  E.  meat,  etc., ‘flesh  of  animals’,  cp.  Heb.  lehem,  ‘bread,  food’, with  Arab,  lahm,  ‘flesh’.
Derivatives :  meat-less,  meat-y,  adjs. meatus,  n.,  a  duct  or  passage  in  the  body  ( anat .) —  L.  meatus,  ‘a  going,  passing;  way,  path,  pas¬ sage’,  fr.  meat-(um),  pp.  stem  of  meare,  ‘to  go, pass’,  which  is  cogn.  with  Czech  mijim,  mijed, ‘to  go  by,  pass  by,  pass,  cease’,  Pol.  mijam, mijac,  ‘to  go  by,  avoid’,  and  with  the  nasalized forms  OSlav.  minq,  minqti,  ‘to  go  by,  pass  by, pass’,  MW.  minet,  ‘to  go’;  fr.  I.-E.  base  *mei-, *moi-,  ‘to  change;  to  change  one’s  place;  to  go’. See  mean,  ‘of  low  rank’,  and  cp.  irremeable,  per¬ meate.  Cp.  also  conge.
Mecca,  n.,  city  in  Arabia,  birthplace  of  Moham¬ med  and  place  of  pilgrimage  for  Mohammedans hence  ‘the  goal  of  one’s  highest  aspirations’.  — Arab.  Makkah,  in  VArab.  pronunciation: Mekkah,  ‘Mecca’.
mechanic,  adj.  —  L.  mechanicus,  fr.  Gk.  pv yccvixop,  ‘resourceful,  inventive;  mechanical’,  fr. pTjxavr;,  ‘means,  invention,  machine".  See machine  and  -ic.
Derivatives:  mechanic,  n.,  mechanic-al,  adj., mechanic-al-ly,  adv.,  mechanic-al-ness,  n.,  me- chanic-ian,  n.,  mechan-ics,  n. mechanism,  n.  —  ModL.  mechanismus,  fr.  Gk.
pTjyavYj,  ‘machine’.  See  prec.  word  and  -ism. mechanist,  n.  —  Formed  with  suff.  -ist  fr.  Gk. (jnqyavv),  ‘machine’.  See  mechanic.
Derivatives:  mechanist-ic,  adj.,  mechanist-ic-al- ly,  adv.
mechanize,  tr.  v.  —  Formed  with  suff.  -ize  fr.  Gk. pilXavT],  ‘machine’.  See  mechanic.
Derivatives:  mechaniz-ation,  n.,  mechaniz-er,  n. mechano-,  combining  form  denoting  mechanics or  mechanism.  —  Gk.  pTjxocvo-,  fr.  p7)-/avfj, ‘machine’.  See  mechanic.
Mcchilta,  also  Mekhilta,  n.,  a  halakic  commen¬ tary  on  Exodus  from  the  school  of  Rabbi  Ish- mael  (2nd  cent.)  —  Fr.  Aram,  nfkhilta,  ‘rule’, lit.  ‘measure  of  capacity’,  fr.  kul,  ‘to  compre¬ hend,  measure’,  which  is  rel.  to  Heb.  kdl,  ‘he comprehended,  measured’,  hakhtl,  ‘to  hold, contain’,  Ugar.  kl,  ‘to  contain,  measure',  Arab. kala,  ‘he  measured  (grain)’.
Mechlin,  n.  —  Short  for  Mechlin  lace,  i.e.  lace made  at  Mechlin,  a  town  in  Belgium.  Cp. ma  lines.
meco-,  combining  form  meaning  ‘length’  or ‘long’.  —  Gk.  p>)xo-,  fr.  prjxoc,  ‘length’,  corre-
meconic
mediocrity
sponding  to  Dor.  Gk.  (tocxo?,  of  s.m.,  and  rel.  to pay-poc,  ‘long’.  See  macro-  and  cp.  mekometer. meconic,  adj.,  pertaining  to  an  acid  found  in  opi¬ um.  —  Gk.  jiT)xtovix6i;,  ‘of,  or  pertaining  to,  the poppy',  fr.  pY|xtov.  See  next  word  and  -ic. meconium,  n.,  the  fecal  discharge  of  the  newborn infant  (med.)  —  L.  meconium,  ‘poppy-juice;  the first  excrements  of  the  newborn  child’,  fr.  Gk. pTjxdmciv,  dimin.  of  [trjxtov,  ‘poppy’,  which corresponds  to  Dor.  (tSxcov,  of  s.m.,  and  is cogn.  with  OSlav.  maku,  Pol.  mak  (whence OPruss.  moke),  ‘poppy’,  OS.  maho,  OHG.  mago. Late  MHG.  mahen,  man ,  dial.  Austro-Bavarian mogn,  G.  Mohn,  ‘poppy’  (Lith.  magone,  Lett. maguone,  of  s.m.,  are  German  loan  words.)  Cp. the  second  element  in  Eomecon. medal,  n.  —  MF.  (=  F.)  medaille,  fr.  It.  medaglia, fr.  VL.  *metallia  (scil.  moneta),  ‘metal  coin’,  fr. L.  metallum.  See  metal  and  cp.  next  word. Derivatives:  medal,  tr.  v.,  medal(l)-ed,  adj., medall-ic,  adj.,  and  the  hybrid  medal(J)-ist,  n. medallion,  n.  —  F.  medallion,  fr.  It.  medaglione, augment,  of  medaglia.  See  medal  and  -oon. Derivative:  medallion,  tr.  v. meddle,  intr.  v.,  to  interfere.  —  ME.  medelen, medlen,  fr.  OF.  medler,  mesler,  ‘to  mix,  mingle; to  meddle’  (whence  F.  meler,  ‘to  mix,  mingle’, se  meler,  ‘to  meddle’),  fr.  ML  misculdre,  fr.  L. miscere,  ‘to  mix,  mingle’.  See  mix  and  cp. medley  and  words  there  referred  to.
Derivatives:  meddl-er,  n.,  meddlesome,  adj., meddle-some-ness,  n.
Mede,  n.,  inhabitant  of  Media.  —  L.  Modus,  fr. Gk.  MvjSoq,  ‘Mede’.
Medea,  n.,  sorceress,  daughter  of  Aeetes,  king  of Colchis  ( Greek  mythol.)  —  L.  Medea,  fr.  Gk. Mv]8si3t,  lit.  ‘cunning’,  rel.  to  [ri)8o?,  ‘counsel, plan,  device,  cunning’,  [xrjSeoOat,  ‘to  devise,  re¬ solve,  advise’,  piSotv,  p.s8£cov,  ‘guardian,  ruler (prop.  pres.  part,  of  the  ancient  verb  [i£8eiv,  ‘to protect,  rule  over’l,  pi8ea&ai,  ‘to  be  mindful  of, give  heed  to,  think  on’,  piSipvop,  ‘a  measure’,
_ p  base  *med-,  ‘to  measure,  limit,  consider  , which  is  a  -(/-enlargement  of  base  *me-,  ‘to  meas¬ ure’.  See  meditate  and  cp.  Andromeda  and words  there  referred  to.  Cp.  also  Medeola. Medeola,  n.,  a  genus  of  plants,  the  Indian  cu¬ cumber-root  (bot.)  —  ModL.,  dimin.  formed from  the  name  of  Medea,  the  sorceress;  so called  for  its  reputed  medicinal  value, medi-,  combining  form.  —  See  medio-, media,  n.,  formerly,  a  voiced  stop  consonant  ( b , d  or  g)  ( phonet .) ;  —  ModL.  (short  for  littera media,  lit.  ‘middle  letter’),  fern,  of  L.  medius, ivTiirh  ctqnrU  for  *medhvosl  rel.  to  Os- can  mefiai  (fern,  sing.),  ‘in  the  middle’,  *nd  cogn. with  OI.  madhyab,  Avestic  maidya-,  ‘middle’, Gk.  pianos,  Att.  (ze< to;,  Goth,  midjis,  OE. midd,  OIr.  mid-,  ‘middle’,  OSlav.  mezda,  ‘road’, orig.  ‘ridge  (between  two  fields)’,  mezda,  ‘be¬ tween’,  OPruss.  median,  ‘forest ,  Lith.  midis, ‘tree’.  East  Lith.  mediias,  ‘forest,  tree’,  Arm.
me],  ‘the  middle’,  Alb.  mjel,  ‘means’,  mes,  mjes, mjez,  ‘means’,  Gheg  mjedis  (for  mjet-vis,  mjed- vis),  ‘middle,  center’  (fit.  ‘middle  place’),  Gaul. medio-,  ‘middle’  (e.g.  in  Medio-ldnum,  ‘Milan’). Cp.  mid,  middle,  midst,  amid.  Cp.  also  median, mediant,  mediastinum,  mediate,  mediocre,  medi¬ um,  immediate,  intermediate,  intermezzo,  mean, ‘intermediate’,  medulla,  meridian,  mesne,  meso-, meta-,  metayer,  mezzanine,  mezzotint,  Midi, midinette,  milieu,  mitten,  mizzen,  mizzenmast, moiety,  monial,  moyen  age. media,  n.,  middle  membrane  of  an  artery  (anal.)
_  Medical  L.  (short  for  membrdna  media,  fit.
‘middle  membrane’),  fern,  of  L.  medius.  Seeprec. word.
media,  n.  pi.  —  PI.  of  medium, medial,  adj.,  situated  in  the  middle.  —  Late  L. medidlis,  fr.  L.  medius.  See  media,  ‘voiced  stop consonant’,  and  adj.  suff.  -al.
Derivative:  medial-ly,  adv. median,  adj.,  middle;  situated  in  the  middle.
L.  medianus,  ‘that  which  is  in  the  middle,  mid¬ dle’,  fr.  medius.  See  media,  ‘voiced  stop  conso¬ nant’,  and  -an,  and  cp.  mean,  ‘intermediate , mesne,  monial,  moyen  age.
Derivative:  median,  n.,  a  median  line,  point  or number.
Median,  adj.,  pertaining  to  Media;  n.,  1)  a  Mede ; 2)  the  language  of  ancient  Media.  —  Formed with  suff.  -an  fr.  Gk.  MrjSio?,  ‘of  Media’,  fr. MrjSo;.  See  Mede  and  cp.  Medic, median  vein  ( anat .)  —  L-  vena  mediana.  Accord¬ ing  to  Joseph  Hyrtl  (in  his  Onomatologia  anato- mica,  p.  320),  these  words  do  not  mean  ‘the middle  vein’,  but  are  derived  from  the  name  of Al-Madyan,  ibn  Abderrahman,  a  commentator of  Avicenna’s  Canticum.  So  arose  the  term ‘vein  of  Al-Madyan',  whence  Armegandus coined  the  name  vena  mediana,  which  was  mis¬ interpreted  later  as  ‘the  middle  vein’  (see  median). mediant,  n.,  the  third  note  of  the  diatonic  scale (music).  —  It.  mediante,  fr.  Late  L.  mediantem, acc.  of  medians,  ‘dividing  in  the  middle’,  pres, part,  of  medidre;  so  called  as  being  midway  be¬ tween  the  tonic  and  the  dominant.  See  mediate, adj.,  and  -ant.
mediastinitis,  n.,  inflammation  of  the  tissue  of  the mediastinum  (med.)  -  A  Medical  L.  hybrid coined  fr.  mediastinum  and  suff.  -itis. mediastino-,  combining  form  denoting  ‘of  the mediastinum,  mediastinal’.  See  next  word, mediastinum,  n.,  1)  a  membranous  partition  sep¬ arating  two  cavities  of  the  body;  2)  space  in the  middle  of  the  chest  between  the  two  pleurae (anal.)  —  Medical  L.,  neui.  of  medidsiinus,  ‘serv¬ ant,  attendant’,  which  stands  for  * medidstrinus, fr.  *mediaster,  ‘the  one  in  the  middle’,  fr.  L. medius.  See  media,  ‘voiced  stop  consonant . Derivative:  mediastin-al ,  adj. mediate,  adj.,  dependent  on.  —  Late  L.  medidtus, pp.  of  medidre,  ‘to  divide  in  the  middle,  to
halve’,  fr.  L.  medius.  See  media,  ‘voiced  stop consonant’  and  adj.  sufF.  -ate  and  cp.  mediant. Derivative:  mediate-ly,  adv. mediate,  intr.  v.,  to  intervene;  tr.  v.,  to  bring about  by  intervention.  —  Lit.  ‘to  be  in  the middle’,  fr.  Late  L.  medidtus,  pp.  of  medidre. See  prec.  word.
mediation,  n.  —  ME.  mediacioun,  fr.  OF.  media- cion  (F.  mediation),  fr.  Late  L.  mediationem, acc.  of  medidtio,  fit.  ‘a  division  in  the  middle’, fr.  medidtus,  pp.  of  medidre.  See  mediate,  adj., and  -ion.
mediatize,  tr.  v.,  formerly  in  Germany,  under  the Holy  Roman  Empire,  to  reduce  to  mediate  de- pendance  or  vassalage.  —  F.  mediatiser,  fr. mddiat,  ‘mediate’.  See  mediate,  adj.,  and  -ize. Derivative :  mediatiz-at-ion,  n. mediator,  n.  —  ME.  mediatour,  fr.  OF.  media- tour  (F.  mediateur),  fr.  Late  L.  medidtorem,  acc. of  mediator,  fr.  medidtus,  pp.  of  medidre.  See mediate,  adj.,  and  agential  suff.  -or. mediatory,  adj.  —  Formed  with  adj.  suff.  -ory  fr. Late  L.  medidtus,  pp.  of  medidre.  See  mediate, adj.
Derivative:  mediatori-al,  adj.
Medic,  adj.,  Median;  n.,  the  language  of  ancient Media.  —  Gk.  Mt}8ix6?,  ‘Median’,  fr.  MijSoc. See  Mede  and  cp.  Median.  Cp.  also  next  word, medic,  n.,  any  plant  of  the  genus  Medicago  (bot.)
—  L.  medica,  fr.  Gk.  My)8ixy)  (scil.  7roa ) , ‘(grass)  from  Media’,  fern,  of  My;8ix6<;,  ‘Median’ (see  Medic);  so  called  because  it  came  to  the Greeks  from  Media.
medicable.  —  L.  medicabilis,  ‘that  which  can  be healed,  curable’,  fr.  medicdri,  ‘to  heal,  cure’,  fr. medicus.  See  medical  and  -able.
Medicago,  n.,  a  genus  of  plants,  the  medic  (bot.)
—  ModL.,  fr.  Gk.  MvjSixr),  name  of  the  alfalfa, lit.  ‘the  Median  (plant)'.  See  medic.
medical,  adj.  —  F.  medical,  fr.  Late  L.  medicalis, ‘of  a  physician',  fr.  L.  medicus,  ‘physician’, which  is  rel  to  mederi,  ‘to  heal’,  and  cogn.  with Avestic  vi-mad,  ‘physician’,  fr.  I.-E.  base  *med-, ‘to  measure,  limit,  consider,  advise’,  whence  also Gk.  pvjSo s,  ‘counsel,  plan,  device,  cunning’,  the PN’s  MijSo;,  MtjStj,  etc.,  which  originally  de¬ noted  healing  deities,  prjSso&at,  ‘to  devise,  re¬ solve,  advise’,  pisSsoO-xi,  ‘to  be  mindful  of,  give heed  to,  think  on’.  See  meditate  and  Medea  and cp.  remedy.  Cp.  also  metheglin.  The  word  med¬ ical  was  introduced  into  English  by  Thomas Browne  (1605-82).  '
Derivatives:  medical,  n.,  medical-lv,  adv. medicament,  n.  —  F.  medicament,  fr.  L.  medica- mentum,  ‘drug,  remedy,  medicament’,  fit. 'means  or  instrument  of  healing’,  formed  from the  verb  medicdri,  ‘to  heal,  cure’,  with  -mentum, a  suffix  denoting  instrument.  See  medicate  and -ment.
Derivatives:  medicament,  tr.  v.,  medicament-ary, adj.,  medicament-ation,  n.,  medicament-ous,  adj. medicaster,  n.,  a  quack.  —  Formed  fr.  L.  medicus.
‘physician’,  with  the  pejorative  suff.  -aster.  Cp. poetaster.
medicate,  tr.  v.  —  L.  medicatus,  pp.  of  medicare, medicdri,  ‘to  heal,  cure’,  fr.  medicus.  See  medical and  verbal  suff.  -ate.
Derivatives:  medication  (q.v.),  medicat-ive,  adj., medicator  (q.v.),  medicat-ory,  adj. medication,  n.  —  L.  medicatio,  gen.  -onis, ‘healing,  cure’,  fr.  medicatus,  pp.  of  medicare, medicdri.  See  prec.  word  and  -ion. medicator,  n.  —  Late  L.  medicator,  ‘physician’, fr.  L.  medicatus,  pp.  of  medicare,  medicdri.  See medicate  and  agential  suff.  -or. medicine,  n.  —  ME.,  fr.  OF.  medicine,  medecine (F.  medecine),  fr.  L.  medicina,  ‘healing  art,  the shop  of  a  physician,  remedy,  relief’,  prop.  fern, of  the  adjective  medicinus,  ‘of  a  physician’,  used as  a  noun,  fr.  medicus.  See  medical  and  subst. suff.  -ine.
Derivatives:  medicine,  tr.  v.,  medicin-al,  adj. and  n.,  medicin-al-ly,  adv. medico,  n.,  physician  ( colloq .)  —  It.  medico,  fr. L.  medicus.  See  medical.
medico-,  combining  form  meaning  1)  ‘medical, medicinal’ ;  2)  ‘medical  and’.  —  Fr.  L.  medicus. See  medical.
medieval,  mediaeval,  adj.,  pertaining  to,  or  sug¬ gestive  of,  the  Middle  Ages.  —  Formed  with adj.  suff.  -al  fr.  L.  medius,  ‘middle’,  and  aevum, ‘age’.  See  media,  ‘voiced  stop  consonant’,  and age.
Derivative:  medi(a)eval-ly,  adv. medievalism,  mediaevaiism,  n.,  1)  the  spirit  of  the Middle  Ages;  2)  devotion  to  medieval  prac¬ tices.  —  See  prec.  word  and  -ism. medievalist,  mediaevalist,  n.,  1)  a  student  of medieval  history,  etc.;  2)  one  devoted  to  the spirit  and  practices  of  the  Middle  Ages.  • —  See medieval  and  -ist.
medievalize,  mediaevalize,  tr.  v.,  1)  to  render medieval;  2)  to  adopt  medieval  customs,  etc.  — See  medieval  and  -ize.
medio-,  medi-,  combining  form  meaning  ‘middle’. —  Fr.  L.  medius,  ‘middle’.  See  media,  ‘voiced stop  consonant’.
mediocre,  adj.,  of  middle  quality;  average.  — MF.  (=  F.)  mediocre,  fr.  L.  mediocris,  ‘mid¬ dling,  moderate,  indifferent,  tolerable’,  orig. ‘being  half-way  up  the  height  of  a  mountain’, compounded  of  medius,  ‘middle’,  and  ocris,  ‘a rugged,  stony  mountain’.  For  the  first  element see  media,  ‘voiced  stop  consonant’.  The  second element  is  rel.  to  Umbr.  ukar,  ocar,  ‘fortress, citadel,  mountain’,  and  cogn.  with  Gk.  oxpiq, ‘peak,  point’,  Homeric  oxptav,  ‘to  make  rough or  rugged’,  oxpiaahxt,  ‘to  be  exasperated’,  Mir. ochar,  W.  ochr,  ‘comer,  border’,  and  in  grada¬ tional  relationship  to  L.  deer,  acris,  acre,  ‘sharp’. See  acrid  and  cp.  Oxalis. mediocrity,  n.  —  ME.  mediocrite,  fr.  MF.  (=  F.) midlocriti,  fr.  L.  mediocritatem,  acc.  of  medio- critas,  ‘moderateness,  moderation,  indifference.
meditate
megawatt
M
957
```


## [2026-09-07T15:51:50.506Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '23300,23345p' KLN_1966.txt | grep -n -i 'mega\\|maha\\|much\\|Avestic\\|maz' "
}
```


### [2026-09-07T15:51:50.571Z] TOOL RESULT

```
6:mdtih ,  ‘measure’,  mail,  mlmdti ,  ‘measures  ,  tna- tram  (neut.),  matra  (fem.),  ‘measure’,  Avestic md-,  ‘to  measure’,  Toch.  A  me-,  'to  measure , mem,  ‘measure’,  Hitt,  mehur,  ‘time,  point  of time’,  Gk.  pvjTip,  ‘counsel,  plan,  skill’,  perpov, ‘measure’,  L.  metier,  metiri,  ‘to  measure ,  Alb. mat,  mas,  ‘I  measure’,  mass,  ‘measure,  age,  gen¬ eration’,  mates,  ‘measure,  cubit’,  mot,  ‘year, weather’, OSlav.mcra,  ‘measure’,  miriti,  ‘to  meas¬ ure’,  Lith.  matuoti,  ‘to  measure’,  metas,^  ‘time, year;  measure’,  OPruss.  mettan,  ‘year  ,  Lett. mets,  ‘space  of  time’,  mat  as,  ‘measure’,  OSlav. m?to,  mesti,  Lith.  metii,  mesti,  Lett,  mest,  ‘to throw’  (orig.  ‘to  measure  off,  aim  at’),  OHG. mat,  Goth,  mil,  ‘time;  hour’.  Cp.  matra,  mensal, ‘pertaining  to  the  table’,  meter,  poetical rhythm’,  -meter.  Metis,  and  the  second  element in  castrametation,  firman,  vimana.  Cp.  also  meal, ‘food’.
23:Derivatives:  medus-al,  medus-an,  adjs. medusoid,  1)  adj.,  like  a  medusa;  2)  a  medusalike gonophore  of  a  hydrozoan  (zool.)  —  Com¬ pounded  of  medusa  and  Gk.  -octS r\t;,  ‘like’,  fr. e!8o?,  ‘shape,  form’.  See  -oid. meed,  n.,  reward  (poet.)  —  ME.  mede,  fr.  OE. med,  meord,  ‘reward,  requital’,  rel.  to  OS.  meda, OHG.  meta,  miata,  mieta,  MHG.,  G.  miete, Goth,  mizdd,  ‘reward’,  and  cogn.  with  OI.  mi- dham  (for  *mizdha-),  ‘prize,  reward,  contest, booty’,  midhvah,  ‘giving  in  abundance’,  Avestic mizda,  ‘reward’,  Gk.  piaD8i;  (for  •mizdhos), ‘wages,  pay’,  OSlav.  mizda,  ‘salary’, meek,  adj.  —  ME.  mek,  fr.  earlier  rneoc,  fr. ON.  mjukr,  ‘mild,  soft,  gentle’,  which  is  rel.  to Goth,  muka-modei,  ‘humility’,  and  prob.  cogn. with  OIr.  mocht  (for  *mukto-),  ‘mild,  gentle’, L.  mucus,  ‘mucus  of  the  nose’.  See  mucus  and cp.  words  there  referred  to.
29:Meg,  fem.  PN.  —  Dimin.  of  Margaret, mega-,  before  a  vowel  meg-,  combining  form meaning  'large,  great’  (in  physics  it  is  used  in  the meaning  of  ‘a  million  times’,  e.g.  megavolt  —  a million  volts).  —  Fr.  Gk.  pEyap,  fem.  psyiXv], neut.  peyx,  ‘great,  large,  mighty’,  which  is  cogn. with  L.  magnus,  ‘great,  large,  much,  abundant’, Goth,  mikils,  OE.  micel,  mycel,  ‘great,  big, many’.  See  mickle  and  cp.  magnum.  Cp.  also omega,  acromegaly,  almagest,  Agastache. megacephalic,  megacephalous,  adj.,  large-headed.
30:—  Compounded  of  mega-  and  Gk.  xeqpaXir), ‘head’.  See  cephalic,  resp.  cephalous.
31:Megaceros,  n.,  a  genus  of  mammals  of  the  deer family  (zool.)  —  ModL.,  compounded  of  mega- and  Gk.  x£pa?,  ‘horn’.  See  cerato-.
32:Megachile,  n.,  a  genus  of  bees  (zool.)  —  ModL., compounded  of  mega-  and  Gk.  ypThoc,,  ‘lip’. See  chilo-.
33:megal-,  form  of  megalo-  before  a  vowel, megalith,  n.,  a  huge  prehistoric  stone.  —  Com¬ pounded  of  mega-  and  Gk.  >.£f>o<g,  ‘stone’.  See litho-.
34:Derivative:  megalith-ic,  adj. megalo-,  before  a  vowel  megal-,  combining  form meaning  ‘large,  great’  (in  medicine  it  is  used  to denote  abnormal  enlargement).  —  Gk.  psyaXo-, peyaX-,  enlarged  stem  of  pEyoo;  (gen.  peyaXou), ‘large,  great,  mighty’.  See  mega-, megalocardia,  n.,  abnormal  enlargement  of  the heart  (med.)  —  Medical  L.,  compounded  of megalo-  and  Gk.  xapSia,  ‘heart’.  See  cardio-. megalocephalic,  adj.  —  The  same  as  megacephal¬ ic.
35:megalomania,  n.,  mania  for  great  things;  delu¬ sion  of  greatness  (med.)  —  Medical  L.,  com¬ pounded  of  megalo-  and  Gk.  pavia,  ‘madness’. See  mania.
36:Derivative:  megalomani-ac,  adj. megalosaur,  n.,  any  animal  of  the  genus  Megalo- saurus.  —  See  Megalosaurus. megalosaurian,  adj.,  pertaining  to  the  megalo- saurs;  n.,  a  megalosaur.  —  See  prec.  word  and -ian.
37:Megalosaurus,  n.,  a  genus  of  gigantic  dinosaurs ( paleontol .)  —  ModL.,  compounded  of  megalo- and  Gk.  craopop,  ‘lizard’.  See  sauro-. megaphone,  n.  —  Compounded  of  mega-  and Gk.  9fovif),  ‘voice’.  See  phone,  ‘speech  sound’, megapode,  also  megapod,  n.,  any  of  the  birds  of the  family  Megapodiidae.  —■  See  next  word. Megapodiidae,  n.  pi.,  a  family  of  birds  inhabiting Australia  and  the  Malay  Archipelago  (orni- thol.)  —  ModL.,  formed  with  suff.  -idae  fr. mega-  and  Gk.  7toui;,  gen.  71086;,  ‘foot’.  See podo-.
38:megaron,  n.,  the  great  hall  in  the  Greek  palace, esp.  at  Mycenae  ( archeol .)  —  Gk.  piyapov, ‘large  room,  hall;  sanctuary,  shrine’;  pi.  p6- yapoc,  ‘pits  (into  which  young  pigs  were  thrown in  the  Thesmophoria)’ ;  of  uncertain  origin; possibly  fr.  Heb.  me‘drah,  ‘cave’, megasporangium,  n.,  a  sporangium  containing megaspores  (bot.)  —  ModL.,  compounded  of mega-  and  sporangium.
39:megaspore,  n.,  a  large  asexual  spore  produced  by certain  plants,  as  the  embryo  sac  of  a  seed plant  (bot.)  —  Compounded  of  mega-  and  Gk. ano pa,  ‘a  sowing,  seed'.  See  spore, megass,  megasse,  n.,  sugar  cane  crushed  in  the mill.  —  Variants  of  bagasse, megavolt,  n.,  one  million  volts.  —  Compounded of  mega-  and  volt.
40:megawatt,  n.,  one  million  watts.  —  Compounded of  mega-  and  watt.
```


## [2026-09-07T15:51:56.995Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n '^mickle,\\|^much,\\|^magnum,\\|^master,\\|^May,\\|^mayor,\\|^majesty,\\|^maharajah\\|^mahatma\\|^omega,\\|^Mediterranean' KLN_1966.txt | head -20"
}
```


### [2026-09-07T15:51:57.060Z] TOOL RESULT

```
22571:mahatma,  n.,  great-souled,  magnanimous.  —  OI. mahatman,  ‘great-souled’,  compounded  of  ma- hdt-,  ‘great’,  and  atmdn,  ‘soul’.  The  first  element is  cogn.  with  L.  magnus,  ‘great’;  see  magnum and  cp.  maharajah  and  words  there  referred  to. For  the  second  element  see  atman.
23081:master,  n.  —  ME.  maistre,  fr.  OE.  msegester  and OF.  maistre  (F.  maitre).  Both  OE.  msegester  and OF.  maistre  derive  fr.  L.  magister,  ‘master, chief,  head,  leader’,  whence  also  It.  maestro, Ruman.  maestru,  OProven?.,  Catal.  maestre, Sp.  maestro.  Port,  mestre.  L.  magister  stands  for *mag-is-teros,  which  is  formed  with  double comparative  suff.  from  the  stem  of  L.  magnus, ‘great’.  For  the  compar.  suff.  -is  cp.  L.  magis, ‘more’,  which  is  rel.  to  magnus,  ‘great’ ;  for  the compar.  suff.  *-teros  see  -ther;  for  the  use  of  the double  compar.  suff.  in  L.  magister  cp.  minister. OHG.  meistar  (whence  MHG.,  G.  meister),  OS. mestar,  OCo.  maister,  W.  meistr,  etc.  are  Latin loan  words.  See  mickle  and  cp.  magnum, megalo-.  Cp.  also  magisterial,  magistrate,  maes¬ tro,  mister,  mistral.
23388:much,  quite’,  paXXov,  ’more,  rather’  (changed from  original  *p£XXov,  under  the  influence  of ■9-aTTOV,  Oaaaov,  ‘quicker,  sooner,  rather'),  p<£- Xiaroc,  ‘most,  most  strongly’,  L.  multus  (for *mltos ),  ‘much’,  Lett,  milns,  ‘very  much’.  See multi-  and  verbal  suff.  -ate  and  cp.  ameliorate. Derivatives:  meliorat-ion,  n.,  meliorat-ive,  adj., meliorat-or,  n.
23807:mickle,  adj.,  great,  much  ( archaic  or  dial.)  —  ME. mikel,  muchel,  fr.  OE.  micel,  mycei,  ‘great,  big, many’,  rel.  to  OS.  mikil,  ON.  mikill,  OHG. mihhil,  Goth,  mikils,  fr.  I.-E.  base  *meg(h)-, *m*g-,  ‘great,  large’,  whence  also  OI.  mah-, mahd-,  mahat-,  ‘great’,  mahas-,  ‘greatness’, Avestic  maz -,  mazant-,  ‘great’,  mazah-,  ‘great¬ ness’,  Toch.  A  mak,  B.  maka-,  ‘great,  much’, Hitt,  mekkish,  ‘great,  large’.  Arm.  mec  (instru¬ mental  case  mecaw),  ‘large’,  Gk.  P-eya:;,  fern. iievAXn.  neut.  uiva,  ‘great,  large’.  Ion.  ui£<av
26237:omega,  n.,  the  twenty-fourth  and  last  letter  of  the Greek  alphabet.  —  Gk.  <jp£ya,  ‘the  great  (i.e. long)  o'.  Cp.  omicron.
```


## [2026-09-07T15:52:03.339Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"myd'n\\|myδ\\|myd\\`n\\|mydn\" SOD_pages.txt | head -20\necho \"=== entry 223? ===\"\ngrep -n '^ *223 ' SOD_pages.txt | head"
}
```


### [2026-09-07T15:52:04.904Z] TOOL RESULT

```
19706:      mayakcik ? ©<Av. maye, maya                                    me8an   (myd'n, mydn) ©Av. mai8yana; Parth.
19716:          mfmnt                                                5591 myd'n C =■» my8>n
19799:5606 mydn      C => myb^n
=== entry 223? ===
4461:223 "Pty S                                                                 TSP 2.37 n pl69; SCE 407; Bailey. BSOAS            1961,
```


## [2026-09-07T15:52:07.891Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '19700,19720p' SOD_pages.txt\necho \"=== which leaf/page? ===\"\nawk 'NR<=19720 && /\\f/{n++} END{print \"formfeeds before:\",n}' SOD_pages.txt\ngrep -n '\\[pdf page' SOD_pages.txt | head -3"
}
```


### [2026-09-07T15:52:09.464Z] TOOL RESULT

```
           p; loc. f. KG, 2058, pi. mysn(0                           me8ak ? (m,y8)k(k)) ©pi. -n ob. pi. -ty
 5573 my- B                      * ^jf^cj^i^)                        TSP 2.792; BSTBL, Vim. 52, 54, Dhu. 31, 78, pi.
      mi/-e ? =>myt>y
      (^)close (eyes)                                                  Dhu. 393; STii 7.8 m>yS% TSP 2.792, 7.98; Dhu.
      SCE 253; 3sg. pres. myu Proiexis. 137                            135;m>m, Dhu. 135
 5574 my^cyk B, M                             v^-L-^Jbti^       5590 my5)n   M                        J^<^r<jL.
      mayakcik ? ©<Av. maye, maya                                    me8an   (myd'n, mydn) ©Av. mai8yana; Parth.
      happy, suitable                                                  madyan ©ob. -y; pi. -/ =»mydy*n
                                                                     middle, waist
      TSP 6.5; GMS 124, 1014
                                                                     GMS 183, 282; BBB; W-Lii; MSP b 158, 161, dl;
 5575 my'm- C                           o>UjW; «jj/fU                  STi 38.1; STii 2.5; ob. postp. myd}nyt "amidst,
      mayam ©impf. ^ym-, m'y'ms-
      (ro)end                                                          amongst, C2; MSP b28, my6*n Sogdica. 43.39
                                                                       "remedy"
      BSTii 878.13; STSC 3.13; C2, 87R13, 3pl. impf.
          mfmnt                                                5591 myd'n C =■» my8>n
                                                               5592 myS'n'y -> my8Jny
5576 myWnt =» 'my'mntCy)                                       5593 my8>nc B                                    k-j^L*
5577 my'mnty   B =» 'my'mnKy)                                       me8anc
5578 myc => mync                                                    middle
=== which leaf/page? ===
formfeeds before: 287
```


## [2026-09-07T15:52:17.353Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==288' SOD_pages.txt | head -5\necho \"--- tail ---\"\nawk 'BEGIN{RS=\"\\f\"} NR==288' SOD_pages.txt | tail -5"
}
```


### [2026-09-07T15:52:18.729Z] TOOL RESULT

```
                                                                                                                 ^m^mm
                                                                                  ^m
                                                                                                                 mwrtk (y)
  221

--- tail ---
        GMS 974
                                                               5549 mwrtk(y) B                                            J^
5536 mwrt'jw'ndyy       M                                           murtak =>mrc, mwrtch, mrch
        murta-zwande    (mwrt'jwndy) ^mwrt'zw'nty,                  death
```


## [2026-09-07T15:52:22.542Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} /5590 my/{print \"block\",NR; print substr($0,1,300)}' SOD_pages.txt"
}
```


### [2026-09-07T15:52:23.803Z] TOOL RESULT

```
block 290
                         mm



  223
                                                                                                                  myS^y
                                                       Lr*\y
         C2, 77R12, 54V28; BSTii 880.12
```


## [2026-09-07T15:52:30.066Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==903' SYN.txt | head -70"
}
```


### [2026-09-07T15:52:31.598Z] TOOL RESULT

```
.
NE place, prob. fr. sb. place (12.11), rather than direct from Fr. placer.
Du. plaatsen, fr. platts ‘place’ (12.11).
6. Lith. (pa)déti, Lett. dét, above, 1.
Lith. (pa)statyti, ChSl. (po)staviti, etc., caus. of words for ‘stand’ (12.15).
Lett. likt (also nuolikt, etc.), orig. and still also ‘leave, let’ : Lith. likti ‘be left’, Grk. «iru ‘leave’, etc. (12.18). Walde- P. 2.396 ff. Miuhl.-Endz. 2.467 ff.
7. ChSl. (po)loziti, etc., caus. of words for ‘lie’ (12.14).
ChSI. klasti, klada, etc., esp. ‘lay’, also ‘put’ : Lith. kloti ‘spread out’, OE, OHG hladan ‘load’, etc. Walde-P. 2.489. Berneker 507.
SCr. meinuti, orig. and still dial. ‘throw’ : ChSl. mesti, metati ‘throw’, etc. (10.25). Berneker 2.40.
8. Skt. dha-, Av. da-, above, 1.
SIT Lith.  sédeti Lett.  sédet ChSl.  sédétz SCr. — sjeditz Boh.  sedétt Pol. siedziec Russ. _ sidet’ Skt.  as-, sad- Av. ah-, had-
eouar ‘sit’, itw (fr. redupl. *si-sdo) most- ly caus. ‘seat, place’, but also ‘sit’, xabitw mostly caus. ‘seat’ or ‘take a seat’ (so in NG); Lat. sedére (> It. sedere, OFr. seoir now ‘suit’, Sp. sentar ‘seat,
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
834 SELECTED INDO-EUROPEAN SYNONYMS
place’, sentarse or estar sentado ‘sit’, Rum. sedea; Lat. ad-sidére > Fr. asseoir ‘seat, place’, s’asseoir ‘take a seat’, étre assis ‘be seated, sit’; REW 7780); Ir. saidim, vbl. n. suide, whence NIr. suidh- im; W. eistedd fr. sb. = OBr. estid gl. sedile fr. cpd. (*eks-di-sedo- Pedersen 1.20; otherwise Morris Jones 78), Br. azeza fr. cpd. *ad-sed- (Pedersen 2.605; Loth, Mots lat. 134); Goth. sitan, OF
siitan, OHG sizzan, etc., Seneral Gimp. Lith. sédéti, Lett. sédet; ChSI. ster ot,° general Slavic, beside perfect, Ssésti ‘take a seat’; Skt. sad-, Av. had-.
2. IE *és-, perh. ultimately derive fr. a epd. of preceding, 38g. mid. *¢-sq_ tai. Walde-P. 2.484.
Grk. fyat, 388g. Fora (= Skt. aste) more commonly xé@nuat, whence NG pop. kafonar; Skt. ads-, Av. ah-.
‘take
12.14 LIE Grk. — xeTyar Goth. ligan Lith. guléti NG Keluat, xelropat ON liggja Lett. gulét Lat.  iacére, cubdre Dan. ligge ChSl.  leZati It. giacere Sw. ligga SCr. — lezati Tr. élre couché OE licgan “Boh. — lezeti Sp. yacer, estar acostado ME liggen, lie Pol. lezeé Rum. fi culcat (zace) NE lie Russ. — lezat’ Ir. laigim Du. liggen Skt. ¢i-, 3sg. cele Nir. lutghim OHG li(g)gan Av. ° 3sg. saéle W. gorwedd MHG ligen Br. gourveza NHG _liegen
1. IE *legh-. Walde-P. 2.424. Walde- H. 1.778; Feist 331. Berneker 704 f. Grk. \exouar (Hesych.), Hom. aor. déxzo, ete., and in derivs. Aéxos, Aéxrpov ‘bed, couch’, etc.; Lat. only in lectus ‘bed, couch’; Ir. laigim, NI. luighim; Goth. ligan, OF licgan, OHG lig(g)an, etc., general Gme.; ChSI. lezati, etc., general Slavic, beside perfect. lesti, legq ‘lie down’; Hitt. 3sg. laki ‘causes to fall’, mid. lagari ‘falls, lies’ (Sturtevant, Hitt. Gram. 118, Gloss. 90); Toch. A lake, B leke ‘lair’ (SSS 464).
2. T
```


## [2026-09-07T15:52:37.192Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n '12\\.55\\|BIG, LARGE\\|LARGE, BIG' SYN.txt | head\necho \"---\"\ngrep -n 'SELECTED INDO-EUROPEAN SYNONYMS' SYN.txt | sed -n '1,3p'\ngrep -n '^87[5-9] ' SYN.txt | head"
}
```


### [2026-09-07T15:52:37.275Z] TOOL RESULT

```
1035:3. Gall. -magus in Arganto-magus, etc., Ir. mag, NIr. magh, W. maes, Br. maez, prob. as orig. ‘expanse’ : Lat. magnus, Skt. mah-, etc. ‘large, great’ (12.55), Skt. mahi- ‘earth’. Pedersen 1.96. Stokes 198f. Walde-P. 2.258 (ad- versely).
7273:Fr. grosse, lit. ‘big’ (12.55).
17272:wan), Du. waaien, OHG wajan, MHG wajen, NHG wehen; ChSl. véjati (in Gospels viiz-véjati Mt. 7.25, 27 for mvéw, beside more common duchati Lk. 12.55, etc.), Boh. vdit, Pol. wiaé, Russ. vejat’.
21176:CHAPTER 12 spATIAL RE b) 12.51 41 Puace (S- 12.52 fa. Por (Place, Seb “ae 12.58 013. 51 12.54 yi Lie ae 12.55 ois Stan (VD: ae 12.56 yo16 REMAIN, uaa Pere) 12.57 in17 pees 12.58 12.18 Lea : 12.59 1919 Quiet (adi) ie ; : 991 COLLECT, GATHER . ms 12.62 122 Jow, UNITE ake 1293 SEPARATE (vb-) ; 12232 DiviDE 12.64 1224 Oren (vb.) 12.65 1225 Snur, CLosE (vb.) 12.66 12.26 Cover (vb.) 12.67 1227 Hin, ConcesL 12.68 1231 Hicw 12.71 1232 Low 12.72 1233 Tor 12.73 1234 Borrot 12.74 1235 Eyp 12.75 ae Por 12.76 ee 12.77 12.36 Stop 237 Mux (adj.) Teale 12.38 CENTER 12.81 12, < 78 Ricur (adj; vs. Left) yore aa ler (adj. vs, Right) 12.83 nay Aoi (adv) 12.84 pas oe adv.) 12.85 45 Easn 9 12.46 Wesr 12.91 247 Nonny 12.92 248 Sonne 12.93 12.94 829
22398:Most of the words for ‘size’ are ob- vious derivs. of the adjectives for ‘large, big’ (12.55), that is, ‘bigness’ is used for ‘the degree of bigness’, as Grk. péyeOos : peyas, Lat. magnitudd : magnus, Goth. mikilei : mikils, etc.—all the words list- ed, with the following exceptions:
22400:2. Ir. méit, NIr. méid, W. maint, Br. ment, perh. *manti, old abstract forma- tion fr. root in Ir. mar ‘large’ (12.55). Pedersen 1.242 f., 2.48. Walde-P. 2.238.
22432:12.55 LARGE, BIG (GREAT)
22523:7 mas- long a monista- greatest’ (12.55) : Gr. ers.
22534:erence to persons, by those for ‘large’ (12.55), as Grk. péyas, NG peyédos (but NG ywndés more common even of per- sons), Fr. grand, NHG gross, or by those for ‘long’, as OE, ME long (cf. NED s.v.), Du. lang, Sw. lang.
23527:large’ (12.55).
---
318:2 SELECTED INDO-EUROPEAN SYNONYMS
410:4 SELECTED INDO-EUROPEAN SYNONYMS
456:6 SELECTED INDO-EUROPEAN SYNONYMS
22396:876 SELECTED INDO-EUROPEAN SYNONYMS 12.52 SIZE
```


## [2026-09-07T15:52:40.255Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '22432,22470p' SYN.txt\necho \"=== around 22515-22530 (mas-) ===\"\nsed -n '22505,22535p' SYN.txt"
}
```


### [2026-09-07T15:52:40.328Z] TOOL RESULT

```
12.55 LARGE, BIG (GREAT)
Grk, péyas Goth. mikils Lith. didis, didelis NG peyddos ON storr, mikill Lett. Liels
Lat. magnus, grandis Dan. stor ChSl.  velijt, velikit It. grande, grosso Sw. slor SCr. _velik
Fr. grand, gros OE micel Boh.  vel(i)ky
Sp. grande ME mikel, grete (bigg) Pol. wielki
Rum. mare NE large, big (great) Russ.  bol’§oj (velikij) Ir. mar, bras(s), oll Du. groot Skt. mahant-, mah- NIr. mar OHG = mihhil, groz Av. mazant-, maz-, W. mawr MHG gréz, michel masan-; OPers. Br. bras NHG gross vazarka-
Many of the words for ‘large, big’ be- long to inherited groups, one of them so widespread as to leave no doubt that it reflects the chief IE expression for ‘great, large’ with the familiar extensions be- yond the notion of size.
Yet this group is represented in the present European languages only by NG Heyahos or by dialect forms like NE mickle and muckle (also NE much but no longer used of size). As Lat. magnus was replaced by grandis, so Goth. mikils, OE micel, etc., were replaced in Scan- dinavian by ON storr, Dan., Sw. stor, in West Gme. by the group represented by NE great, which in turn is now used mostly in secondary senses or with emotional value, and with reference to size, except in certain phrases, com- pounds, and place names, is replaced by large or its more colloquial and expres- sive equivalent big.
The words not of the inherited groups reflect such diverse notions as ‘thick, coarse’, ‘abundant, spacious’, ‘swollen’, ‘strong’, etc.
‘Large’ and ‘small’ (12.56) are, of course, understood here in reference to size. For the corresponding notions of quantity, amount, or number, which are partly expressed by the same terms but partly differentiated, see 13.15, 13.17.
1. IE *meg-, *megh-. Walde-P. 2.257 f. Ernout-M. 580f. Walde-H. 2.10 ff. Feist 358 f.
Grk. péyas, gen. peyddov, NG peyados (mom. normalized fr. stem of other cases); Lat. magnus; Ir. maige, marignech (not common), Gall. magio- (in Magio- riz, etc.); Goth. mikils, ON mikill, OF micel, mycel, ME mikel, etc. (NE dial. mickle and muckle), OHG mihhil, MHG michel; Skt. mah-, mahant-, Av. ma? mazant-; Arm. mec; Alb. madh; Hitt.
CC-O0. In Public Domain. Gurukul Kangri Collection, Haridwar
ee
gp ATIAL RELATIONS:
_ in number; Toch. this Pe ‘great in number". ma Wee *meé-, ‘vs 3 Falk-Torp 714. “NIr. mor, W. mawr (Br. grand, etc.’) : Grk. ‘great in spear- OHG mari, etc. BY wavig -mérti in Vladi-mérit, 10 mau, mo(u), W. mwy; I ‘more’, maists ‘sreatest’, mara, mest ‘greater, reatest’ (in siZe, quantity, or number; VB more, most not used of size). "4 Lat grandis (> It., Sp. grande, Fr. grand), esp. ‘great (morally and physical- iy) and often also ‘full-grown’, etym. dub, but perh. (as ‘swollen’?) : Grk. pots ‘pride’, ChSl. gradi ‘breast’, etc. Walde-P. 1.699. Ernout-M. 481 f. Walde-H. 1.617 f. It. grosso, Fr. gros ‘thick, coarse’ (12.63), but also ‘stout’ and ‘big’. Rum. mare, fr. Lat. mas, maris ‘male’ (m designating the male animal of a spe- ces and consequently the larger). Pus- canu 1027, Tiktin 952. 4. Ir, mar, mér, W. mawr, above, 2. a brass, Br. Corn. bras (W. bras shi Son ), prob. : Lat. grossus Welder a (12.63). Walde-P. 1.698. tea u : Stokes 183. il, tia | as prefix oll- (cf. also lire "be arise us, a Prob: : Lat. pol- ton of ae ete., with primary no- Nut, 795, g Walde-P. 2.102. Er- » Stokes 52 f. Dan., Sw. stor (late OE ), ef. OF ris. star id., OS ae starti ‘old’, Lith. Tithsemant?, Le root. *sta- ‘stand’ fsty to hig velopment fr. ‘standing Pt et Welder. ~ gréat e mostly ‘coarse, stout,
*mo-.
Digitized by Arya Samaj Foundation Chennai and eGangotri
PLACE, FORM, SIZE 879
thick’), ME grete, NE great (but with strict reference to size, now mostly re- placed by large or big), Du. groot, OHG, MHG gréz, NHG gross, prob. with pri- mary meaning ‘coarse’ as in OF (freq. also in MHG) : ON grautr ‘porridge’, OE gréot, OHG grioz ‘sand’, fr. a root *ghréu- in words for ‘rub, pound’. Walde-P. 1.648 f. Kluge-G. 219. NED 8.v. great.
ME bygge, bigg(e), big (earliest sense ‘strong, stout, mighty’), NE big, prob. of Norse origin, fr. a form like Norw. bugge: ‘strong man’. NED s.v. big. Austin, Language 15.249.
ME, NE large, in ME ‘ample, spa- cious, broad’, etc., fr. OFr. large (Fr. large ‘broad’), fr. Lat. larga fem. of lar- gus ‘abundant, copious’, etym.? Er- nout-M. 524. Walde-H. 1.764. REW 4912. NED s.v.
6. Lith. didis, didelis, etym. dub.; pos- sibly through ‘conspicuous’ : Skt. didi- ‘shining’, di- ‘shine’, etc. Walde-P. 1.772.
Lett. liels (Lith. lielas obs., not in NSB), prob. through ‘tall’ fr. ‘slender’ : Lith. leilas ‘slender, thin’, leinas ‘thin, flexible’, ete. Walde-P. 2.388. Mihl.- Endz. 2.501 f.
7. ChSl. velijt, velikti, SCr. velik, Boh. vel(i)ky, Pol. wielki (but Russ. velikij now used like NE great and replaced by bol'soj with reference to size) beside *yeli- in ChSl. velimi ‘very’, velt-lépit ‘ueyadorperns’, and *valii-, Russ. valom ‘in abundance’, valovoj ‘wholesale’, prob. - Grk. és ‘in crowds, sufficiently’, ctdw, Att. etd ‘pack close’, etc. Walde- P. 1.296. Otherwise Brickner 616 f.( : ChS]. veléi ‘order’, Lat. velle ‘wish’, etc.).
Russ. bol’soj, new positive to old comp. bol’$ij, ChSl. bolijt, fem. bolisi ‘greater’ (positive velijt, velikt, above) : Skt. baliyas- ‘stronger’, bala- ‘strength’,
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
880
Grk. BeAriwy, Bédrepos ‘better’, Lat. deé- bilis ‘weak’. Walde-P. 2.110. Walde- H. 1.327. Berneker 72.
8. Skt. mahani-, mah-, Av. mazant-, maz-, above, 1.
Ay. masan- ‘great, significant’, masit-, masita- ‘great, large’, masyah- ‘greater’,
SELECTED INDO-EUROPEAN SYNONYMS
masah- ‘length, size’, and mas- ong’ . Grk. paxpés ‘long’ (12.57). Walde-p. 2.223. Barth. 1154 ff.
OPers. vazarka- (‘great’ king and ‘great’ = ‘large’ earth) : Skt, vaja- ‘speed, vigor, contest’, vajra- ‘thunder- bolt’, Av. vazra- ‘club’, Lat. vegére ‘set in
masista-, OPers. maéista- ‘greatest’, be- | motion, excite’. Walde-P. 1.246 f, side masan- ‘greatness, importance’, | Barth. 1390.
12.56 SMALL, LITTLE Grk. —_pixpés Goth. leztils (smals) Lith.  maizas NG mtxpds ON litill, smar (smalr) Lett. mazs Lat. parvus Dan. lille, pl. smaa ChSl.  malit (chudit) It. piccolo Sw. liten, pl. smd SCr. mali, malen Fr. pelit OE ljtel, smal Boh. maly Sp. pequefio, chico ME litel, smal Pol. = maly Rum. mic NE small, little Russ. malyj Ir. becc Du. klein Skt. alpa-, kgudra- Nir. _ beag OHG _ luzzil, smah(i), smal Av. kasu- W. bach, bychan MHG litzel, smal, smehe, Br. bihan klein
NHG Klein
There is no widespread inherited group for ‘small’ parallel to that for ‘large’, and the majority of the words are of uncertain origin. Several seem to be based upon expressive (symbolic) sylla- bles. ‘Crushed, ground (fine)’ is the cer- tain source for one word and a possible one forsome others. A peculiar develop- ment from ‘bright, shining’ through ‘clean, delicate, fine, thin’, etc., is seen in NHG klein vs. NE clean.
=== around 22515-22530 (mas-) ===
CC-O0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
SELECTED INDO-EUROPEAN SYNONYMS
8. For a group which, though not containing the usual words for ‘small’ ag
discussed here, seem to have some such di central notion, see under Grk. navies et ‘thin, sparse’ (12.66). we Be LONG | Lith. ilgas ) Lett. gar’§ yo ChSl. | dliigit SCr. dug Boh. dlouhy me an dlinnyj : ar Sep sn : Av. daraga-, mas- bel me ‘hi 4. Sp. largo, fr. Lat. largus ‘abundant? (cf. Fr. large, ete. ‘broad’, 12.61). 5. Ir. cian ‘long, far, distant’, as sb. ‘long time’, etym.? Deriv. fr. pron, Gi stem in Ir. cé ‘this’, Grk. éxet ‘there’, No Lat. -ce, etc. (Stokes 75, Rozwadowski, i Quaest. gram. 10) not convincing. I,
Ir. long, lang, loanword fr. Lat. longus ip. or cognate? Vendryes, De hib. voc. 152. #
Ir. fota, NIr. fada, ef. Ir. fol length’, NI perh. Lat. vastus ‘vast, immense’. ¥, Walde-P. 1.220. Pedersen 1.32. Thur- By neysen, Gram. 50.
W., Br. hir = Ir. sir ‘long’ (of time) : Lat. sérus ‘late’, Goth. seipus ‘late’, etc. ‘o Walde-P. 2.462. Ernout-M. 933. tio
W. maith, MW meith fr. *mag-tio : Ir. Cas mag- in mag-lorg = mor-lorg ‘big club’, uN magh-slaibh ‘big mountain’, OW digour- ul mechis ‘added’ (?), Ir. do-for-maig ‘in- tio creases’, etc., prob. fr. the root in Lat. We magnus ‘large’, Grk. péyas, etc. Loth, | RC 40.342 f. Walde-P. 2.258 (without in) W. maith). fr
6. Goth. laggs, etc., above, 2. Jan
7. Lett. gar’§, cf. Lith. gargaras ‘lean, ne long-legged, long-necked horse’, gingaras ter
‘long-legged man’, outside connections? Miihl.-Endz. 1.608.
of with sb. dlina linnyj, We"
pais, din olong’ : ChSl. pr0-
sengts e g’ Boh. (pro)dlita delay’,
gatti ‘PP One» een in the general Slavic
ft see ets ‘ae dliigt, etc. (above, 1). ite) a
1. Av. daraga-, above, 1. Skt. dirgha-s but superl. masista-,
7 mas- long a monista- greatest’ (12.55) : Gr. ers.
spl DOVE 9
12.58. ‘Tall’, The sense of NE tall sed of persons, animals, trees, build- ‘oz etc.), that is, ‘of considerable watt vertically long’, is most com- moaly covered by the usual words for ‘high’ (12.31), but in part, esp. with ref=
ee to ‘short’ (opposite of both dea ory pre mostly from the no- aS a off or broken off’. In one a Notion Is abstracted from a
noting a (short) ‘pole, goad’, etc. it Walder = tee root connec- eH tig -314. Emout-M. 117.
us; Lat. brevis; Av. marazu- lin oe ‘short-lived? : OHG murg- a hes ee fragile’, Goth. gamaurg- ne) th E myrge ‘pleasant’? (NE linn Ugh notion of ‘shortening, en-
2 By, yz, lite Qrk. ag xovrés (also attested in "79 OF Kovdés ‘short’; cf. LS
gpATI AL RELATIONS:
Boaxts Goth. xovrds ON skammr brevis Dan. _ kort corto, breve Sw. kort court OE sceort corto ME schort curl NE short 1 —gerr, cumbair, berr Du. kort + gearr OHG  churz, byr mér berr MHG kurz NHG kurz
Digitized by Arya Samaj Foundation Chennai and eGangotri
PLACE, FORM, SIZE 883
erence to persons, by those for ‘large’ (12.55), as Grk. péyas, NG peyédos (but NG ywndés more common even of per- sons), Fr. grand, NHG gross, or by those for ‘long’, as OE, ME long (cf. NED s.v.), Du. lang, Sw. lang.
Other words are:
```


## [2026-09-07T15:53:01.833Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n 'mazant\\|mazan-\\|masyah\\|masista\\|masišta\\|mazišta\\|mazyah' BRT.txt | head -30"
}
```


### [2026-09-07T15:53:01.884Z] TOOL RESULT

```
5270:frmmmfnd,    ?&.-.  frahrui-anlil^).    —    "3)^1311 *nh-al\  Btml,  IF.  ts.  :o6.  —  >*)  Pü.:  undeut- lich, wohl  Transskr. •  j..  g.  'ar-  V.  'gewähren'.     Praes.  10 snnav :  3r3nv—,     PrP.     tn/iavi'^;     Perf. PPfP.  Jr^/Ä-  (s.  /r»-). )    'gewähren'     sva.    'zu    teil    werden lassen':  Aa  ahmai  aus  Prvnävi'^  "welches Los  wurde  ihm  zu  teil?"  Y.5.3;  4;  — ■a'^a   nS   masistasca  .  .   asayö  »nnavanie (3PKM.)    Y.52.3;    —     asöii..    yä    ni äras'il  (sd.)  jnnavataeca  (3SKM)  Y.fö^. 3.  2)   'gewähren'    sva.    'gewährleisten,
7705:•  j.  ^razav-  m.  'Finger":  °zu  F.jg;  — ci'al  gaonahe  (sd.)  . .  ya  dvaHbya  "zubya *hiing3riwn,lt  N.  Ö5;  —  avaval  tafta  ydha kasistahe  (,  mawmaAe,  masistahe)  °svB sisV.6.10,  12,  14, /Ä44  PüZ.  a)  die Breite  der  Finger  als  Maasseinheit:  dva 'ZU  nismaAe  (sd.)  V.(j.6;  —  avavat  aipi yd^a  caiwärS  °zavö\.g.2();  —  cd^wSrö 'zvö  V.  6.  43,  f).  6.  [V.  iS.  2  PüZ. :  lies bai.intu\
10910:masista  xsnaoma  x'nävayäliV.3.iz;g.^2^; —  äai  tum  nishti>ail..ttar»m^a  asavamm kuxsnvqnS  H.2.13,  Vyt55(wo  ^kjt/h- vänB)-,  —  yS  neu  narsm  aiavamm  .. xsnaosta  vä  xsnävayeite  va  '2.4g;  —  ya- '^raca  x^nätS  asavaYi-i^.^C;  —  xi'nüta- htcit  atbislaAe  i&A.)  ..  manS  yaezayäti'^X. /O.iii;  —  xsnüiS  (NPm.)'*  asdonqm urväfßs  pärayeinli  V. /p.31;  —  yat  alsS nä  .  .  haca  alibyS  nmanaHbyS  xsnütS aUii'ß parayäl  V.5.39;  —  ka%a  ^wa mazää  xsnaosäi  aAurä  "wie  kann  ich  dich zufrieden  stellen,  o  AfAA.f"  Y.46,1;  — ndii  xhtSvayeili  ahurim  mazäqm  .  .  ys mazdqm  tarS  manyete  \t  lO.i^q;  6.4;  — yagcä  xsnaespn  (3PKA.)  ahursm  Aaihyäii /y/joianäi/  fraorit  mazdqm  "und  die, welche  gern  mit  rechtem  Tun  AcAÄhM. zufrieden  stellen"  Y,_jo.  5;  —  tistrjm  .. yj  äa\äiti  kuxlnvqnäi  .  .  ayapta  jaio- yantäi  . .  maiyai  ".  .  dem,  der  (ihn)  zu- frieden stellt  .  ."  Yt  &  49;  7J.  24;  — HstrJm  .  .  yezi  . .  bavaitt  yaltö  xSnaiß frihs  paiti.zanlS  Yt.8.4z;  10.120,  Y.ig. 40;  — yaAmäi  xsnütS  bavaiti  mikrS  ,  . yakmäi  IbistB  bavatti  (sd.)  Yt  JO.87;  28, Y.  62.  9;  —  yä^a  . .  anäzarstä  xsnütA  . . a/bisti  yBbm  (näml.  fravasayö)  . .  /ra- cara'iwe\ti3.ZA;  S^  63.  'S^',  iS7';  — xlnuta  F.5;  —  vaT3h3uS xratüm  manaahS yä  xsnyvTsa  g^s^ä*urvqmm  "aufdass  ich den  Willen  des  VM.  befriedige  und  die Seele  des  Rinds"  Y.  28.  \;  —  mazdä  asä xsmüksm  vilnm  xsnaohmnB  "o  M.  und A.,  indem  ich  es  eurem  Willen  recht machen  will"  Y.  ^.  18.  a)  Des.  'zu- frieden stellen,  zu  Gefallen  sein  wollen': nsit  nä  pouräs  (sd.)  drpgvatö  Ayäi  ^ixs- n  uiS  Y.43.11;  —  ys  masying  Hxsn  uiö .  .  gäul  bagä  x^ürsmnS  (sd.)  Y,  J2,  8;  — y}  dusprJ^rJi  (sd.)  Bxsnusä  (iS.)  Y.  4g. I.  a)  mit  Dat  comm.  'Jemands  Zu- friedenheit gewinnen  wollen  für  — ':  tSm nS  vokB  mal  manavhcl  axiriusö  "des  Zu- friedenheit sollst  du  uns  zu  gewinnen suchen,  sammt  der  des   VM."  Y.  45. 9.
14732:u  fasimärTk  'Anütge  und  Verieidig'^rg"  und  i^-o«/-''  sbes.  s)  Tcr��nken,  beleidigen", vicir  II  ditawarik  "Entscheid  und  Urteil';  (lu  mit  Akk.:  ratavS  vJspe  masista  ,  .  yai  vS i  t):  dätmoar;  {t^  3):  dSlinaarih,  etL;  "icir.^ ^^f/j/gg^^  _  „gfig„^g  ^  .j,acargAa  . .  syaeÜFfta .SQ. :  ayäyai.    Zu  F.  S  wird  gesagt,  liaiii  be- 1  ,        azaosa  V  7  3  a  ■  2 1  ■  —  ahuräne
14779:•  j.  tbiSifi-  tn.  'Glied'  des  Fingers;  kasil^take imahmahe,  masistake)  »rszvB  fraltnum  °iis V. 6.10(12,  i4),iÄ44PüZ.
20115:Ableit  —  mp.  (Pü.)  masi  gr.  vgl.  fiax/ii;.  — Vgl.  masyah-,  maiiila-.  —  D  Them.  —  ')  Un- richtig KZ.  30.  539-
20143:j.  masyah-  Adj.  (fem.  'yehJ-Y^  'der grössere':  Ä  üsti  '_>'?(NSn.)  vatghs  srayS (sd.)  aittm  dättm . .  upairi  anyäi^..  V.5. 22 ; avai  hl  asti  'yS  ari^»n  (sd.)  V, 7.71; tisit  maslm  gag%Jm  ff?(sd.)  'ya  hacaiU (sd.)  3snS  xratui  YL/0. 107;  —  ''kaya h»nH  •yaaho  (NP.)  a^  (sd.)  .  ■  *ltaya kasyanhö  F.  j  c ;  —  ^a^  'yS  attahmäi barfsma  N.  70;  —  ^aSa  tJ'ays  (NSf.)" J/^  kasyanhqm  apqm  *avi./rädavaiie  (sd.) V.  5. 24;  —  ya%a  yayi  (NSf.)''  vana kasyanhqm  vanqm  aiwi.vfrjnvaiH  (sd.)  V. 5.  24;  —  yimö  . .  tqm  vXSävayai  (sd.)  atva 'kriha  ahm3l  'yehim  ya'^a  . .  V.3.11;  — fravasayS  .  .  yä  'yehll  ahmät  .  .  yaäsa vaca  /ramraväire  (sd.)  Yl  13.  64;  —  °yd va  ahmätäi  "oder  noch  grösseres  (ärgeres, näml.  soll  als  Strafe  ihm  geschehen)"  V. 4.  50.  a)  'von  grösserem  Wert,   wert-
20150:•  g.,  j.  mazan-  n.  'Grösse,  Erhabenheit':
20153:mazant-
20161:•  j.  mazant-  Adj.''  'gross,  geräumig;  um- fassend, gewaltig;  erhabeo':  mathan?m  . . 'zat  anattf  Yt.  10. 44;  —  Aau  'za  (NS.) mtnyS  stOHsXt.  14.^1;  F.iJ*'; — yämm.. *sänbm  Y.  6$.  11;  —  xratam  ,  .  masiUm 'sSnttm  apairi.ä^nm  (sd.)  Y.  ö'a.  4;  — sraosasca . ,  'za  amava  v^n^raja  Vr,  15. 3.
20244:}.,  g,  mazyah-,  j.  mazah-'>  Adj.  'der grössere,  gewaltigere',  an  Umfang,  Bedeu- tung usw. :  ya^/a  ahtnat  aiti  'sys  . .  vatthB ,  .  srayd  .  .  ta^  nB  dsyata    Y.  ^5. 14;    — katürim  asavä  va  dngvä  vä  vfranvaiil(sd.) "sys  Y.3i.i-j''>;  —  vrsmie  avat  vTstnta^a *matyasat^'>  Yt  i^.  7  3 ;  —  izyati . .  tavavat (sd.)  ,  .  *°zyasät^  'Vyt.30;  —  'xanham'^ va  ifaram  (sd,)  N.^IJ. Komp.  zu  mtu;  matanl-.  —  u.  vgl.  mäl^ai- Adj.  —  Pü.!  miuO,  {lu  N.):  mid,  —  '»S50. 3.  —  »)  Vgl.  V,  38.  5.  —  1)  Hds,  matdyasfit (mit  Yat.),    Der  Verf.  des  Vjrt.  fand  &1eo  die Verderbnis  in  Vt  13.  72  bereits  vor.  —  4)  Zn Y.  31  mit  der  ErL  luxiamä/ar.
24168:•  j,  vindad«-  m.  '(Verschaffen  sva.)  Mit- teÜen,  Verbreiten'":  masista  'daihya{X&- Statt  IS.)  daenayü  maidayasnsis  "die grössten  durch  die  Verbreitung  der  ,  . Religion"  G,  2, 7.
```


## [2026-09-07T15:53:14.146Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '20100,20170p' BRT.txt"
}
```


### [2026-09-07T15:53:14.199Z] TOOL RESULT

```
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
•  j.  marzdikavas't«ma-  Adj.  'der  am meisten  Erbarmen,  Mitleid  haf ;  'i»ma  (als AP.)  ^räyd.driyut^ma  A.J.  4.
SuperU  ans  'katianl-,  —  Pü. :  ämunilärlum.
•  j,  mas-  Adj.  (fem.  -jr-)  'lang*:  zam  . . yam  'sTm^a  pa%anqmca  "die  Erde,  die lange  und  weite"  YL  Jj.  9.  a)  'ausge- dehnt, gross':  yaha  aztm  ..  °sa  (APn.)'>
xia%ra  nivänUni  Yt.5. 130;  —  °W  (statt GSf.)  va  afs  'sS  vS  äa/afl&(sd.)  Yt.  i/. 4;  —  andvT  . .  'sH  (GS.)''  xtayete  (sd.) xfarpnaahd  ydha  .  .  Yt  5. 96.
Ableit  —  mp.  (Pü.)  masi  gr.  vgl.  fiax/ii;.  — Vgl.  masyah-,  maiiila-.  —  D  Them.  —  ')  Un- richtig KZ.  30.  539-
•  j,  'masan-  n.  'Grösse,  Eedeutendheit': "sanaca  (IS.)  vatvhanaca  srayanaca  (sd.) V.J.  22,  Yt/p.  sS,  K.i.\z,  H.J.6,  2.  II, *P.  42.  a)  Plur. 'Glosstaten':  li^ra  vö buyäryS  'sänh  (NP.)''  H%ra  vS  zavanif.- sav^(s±)  Ny.j.ii.
Ableit.  —  Zun  Adj.  mos-.  —  Pü. ;  mar.  — >)  Them.
•  j.  'masan-  Adj.  'gross,  bedeutend':^ffi>,*? .  ,  'sä/ias^ä  (GS.)  vauhänasiä  srayanascJ (sd.)  carpktnmahi  Y.  3Ä4.
Ableit  aus  'masan-  n.,  durch  Ilaplol.  auä *masanaH-(i)'i;  man  beachte  das  ä  des  GS. and  S  403  I-  —  Pü.:  masiA  'Grösse'. —  ■)  S. auch  ai.  varmirt-,  nämin-  u.  a.  (bei  Wh.  Gr.' S  rijoi);  vll.  hat  sich  der  Typus  schon  im Arischen  ausgebildet
•  masah-  n.  'Länge;  Grosse':  ar?dvlm sürqm..yiJ  asti  avavaiti  {sA,)  'sSyd^a.. Y.  65. 3.  a)  AS.  als  Adv.  'valde' :  za/ar? tafsan  (sd.)  aya  's3  V.^.3a.
KompE.  —  Zu  mos-  Adj.  —  Vgl.  gr.  /if«?.  — Pü.;  masik,  (zu  a);  masäi.
•  j.  masö  Adv.:  s.  masah-.
•  j.  masit-  Adj.  'ausgedehnt,  gross':  ya%a ave  awra  upäpa  °sitS  gairJs  iiivämnti  Yt r^.  41.
Ableit.  ans  mas-  j  vgl.  masila-  mit  No.  Z.
•  j,  masita-  Adj. "  (fem.  'tä-)  'gcoss,  um*
37
dby  Google
155
masiSta-
fangreich':  andvJm  .  ,  'sttam  .  .  yS  asti avavaiti  masS .,  V.  ö^.  3 ;  —  tarn . ,  »maita 'siti  ädlahi  Yt.JO.30;  —  äaya..xratüm pascalta  •sitim  matanhm  afiairi.a'isntn (sd.)  Y.  62. 4.
Ahleit.  ant  mos- ;  Tgl.  naiäa-'}.  ~  Pü. :  mai. ~  ')  Vgl.  noch  lu  p.  "Maiäaam.  —  >)  Vgl, fti.  iarit-  und  kaHla-'i
•j.inasijtta-,p.ma9i$ta-Adj.'dergrÖsste'j i)  der  Ausdehnung  nach :  kasistahe  .  . mahmahe  .  .  °tahe  3r>svS  frat3m3m  iMsü V.  6. 14.  2)  U  dem  Rang  nach:  a*wra*- matdä  . .  hyer  -tJ'  baganam  D.4.1;  X. 6. 1.  a)  bes.  'der  Oberste'  cinerTruppe: AyO*  tnadaiitiva  *t^  akJ'  Bh.  2. 6;  —  hyJ' avahyä  karahyS  °ta*  äk^  Bh,_j.  11;  11, 2.4;  —  avamiam  'tarn  akunavam  Bh.2. 6;  I4,^.6j9,I4,  5.1,4; —  avam  'tarn akunavcl'ts  "den  machten  sie  zu  ihrem Obersten"  Bh.j.3,  5.1.
Snperl  lu  ihjj-.  —  mp.  (Pü.),  np.  mahisl.
•  j.  mastay-  f.  'Kenntnis,  Wissen':  dasdi ahmähm  ..  'am  spära  vaä\imca  Yt  10. 33;  5-86.  Y.p.  22,  6'2.4;  —  -iT/n  iTj/J.- pagsaT)h»m    "allseitiges  Wissen"  Y.  5.  17;
57-  "■
Zum  V.  manrf- ;  S  iJ  D ;  'ßl.  dagegen  mtaav-. —  Vä.:  fratänaAIA.
•  j.  "mastflm''  a'hrmnhm  äsiaia"  N.2.
•  j.  ^mastrayan-"  m.  i)  'Schädelwand': a^fl  (sd.)  , .  *yffi  *aparaya  paiti  *'ynya  '* (LS.)  .  .  *ySi  *faouruya  paiti  *'yKaya'* (LS.)''  F.jc.  a)Plur. 'Schädel':  asüm '^alvB*'ynqm*'i'*  vTspaca yS°ynqm^'>  amqsta (sd.)  F.jc.  2)  Plur.  'GehuTi':  «j/ääi vanUsca  *'ynas/a''>  (AP.)  YtJO.  7a.
Statt  masttri^  geschr.,  S  368.  39;  Bthl.  IF. lt.  iiS  No.  3,  wo  auch  lEt.  und  vm  Stamm- bUdung.  —  mp.  (FQ.)  mastur^ ;  oi.  vgl.  maslaia- m.,  n.  'Schädel',  iriasli}tit-  m.,  n.  'Gehini'.  — ■)  'j/r^-  bietet  F  1  (usw.);  NA.  und  F.  haben •stra',  einmal  •sIrT.  —  »)  Them.  —  3)  Hds. mailrauaaifm.
•  j.  masya-  m.  'Fisch':  kars  {sA.)  'syö upäpd  Yt  14.  29,  V.  ig.  4a.
ai.  mAlsya-  m.,  np.  mü^f  (,  wozu  HoRN  GltPh. /  b.  23).  —  Pü.  (mV.):  fehltj  Npü.  (lu  Yt): undeutlich.
j.  matyayd  V.  5.  14:  i.  unter  majyak-  (mit No.  3).
j.  masyah-  Adj.  (fem.  'yehJ-Y^  'der grössere':  Ä  üsti  '_>'?(NSn.)  vatghs  srayS (sd.)  aittm  dättm . .  upairi  anyäi^..  V.5. 22 ; avai  hl  asti  'yS  ari^»n  (sd.)  V, 7.71; tisit  maslm  gag%Jm  ff?(sd.)  'ya  hacaiU (sd.)  3snS  xratui  YL/0. 107;  —  ''kaya h»nH  •yaaho  (NP.)  a^  (sd.)  .  ■  *ltaya kasyanhö  F.  j  c ;  —  ^a^  'yS  attahmäi barfsma  N.  70;  —  ^aSa  tJ'ays  (NSf.)" J/^  kasyanhqm  apqm  *avi./rädavaiie  (sd.) V.  5. 24;  —  ya%a  yayi  (NSf.)''  vana kasyanhqm  vanqm  aiwi.vfrjnvaiH  (sd.)  V. 5.  24;  —  yimö  . .  tqm  vXSävayai  (sd.)  atva 'kriha  ahm3l  'yehim  ya'^a  . .  V.3.11;  — fravasayS  .  .  yä  'yehll  ahmät  .  .  yaäsa vaca  /ramraväire  (sd.)  Yl  13.  64;  —  °yd va  ahmätäi  "oder  noch  grösseres  (ärgeres, näml.  soll  als  Strafe  ihm  geschehen)"  V. 4.  50.  a)  'von  grösserem  Wert,   wert-
voller": yai  'yS  catahmät  *vastr3m  "wenn das  Gewand  wertvoller  ist  als  das"  ^.Sy^. Kompar.  lu  mos-.  —  mp.  meh,  np.  mih;  gr. fiaecay.  —  PQ. :  mos,  —  i)  S.  noch  maryayi mit  N0.2.—  ')  Vgl.  daiu  i  20&.2  No.  I.  �� 3)  Pü.j  Aaiar  me/i  har  an  oil  vaslrai,  mit  der Erl.:  orL     Vgl.  N. /o.
•  j.  masyö.xra&wä-  f  'grössere  Einsicht^: talla  yä  kasujcratus  ''hmqm  nöit paitiimti "wenn(?)  wer  geringe  Einsicht  besitzt,  nicht nach  grösserer  Einsicht  strebt"  V.  7. 59.
VIL  durch  Haplol.  ^3p6)  aus  ■•xro^imi^nu-, Ableit.  aut  ''scn&toan-,  alio  eig.  'Zustand  des, der  grössere  Einsicht  besitzt'.  aSuff.  ar.  I^ä- s.  Wh.  Gr.i  S  »J^b  bE.,  Bgu.  Grdr.  3.  iil. Geringe  Stelle.  ~  Pü.:  jr  mos  xraiih  rü  apar bähend,  erl. :  ehrpaüilän  nt  girind,
•  g.  maz-  Adj.'J  'gross,  von  hervorragen- der Bedeutung';  von  tnaga--.  tost!  afat-a umahs  'sei  magai  (sd.)  Y.  46.  14;  29. 11;  —  von  J/3Ä-:  pars  '*}  (GS.)  yat»hs ahmäi  nS  sazäyäi  (sd.)  bacäantB  paiR Y.  30.  2.  a)  IP.  maxiblf*  als  Adv. 'magnopere,  mit  Nachdruck]  angelegent- lich' :  yBi  m'  . .  Hkiitsn! . .  apaydtl  (sd.)  . . vaBhm  Y,j2,  11.
ai.  mah-  Adj.;  s.  No.  I.  —  Vgl.  ma^aM; maxiila-,  mqsä'  und  mai,  —  Pü. :  mos;  (lu  a): pa  iHosäi.  —  >)  Nur  in  obL  Kasus,  «bens« nie  ai.  moA:  Nom.  und  Akk.  werden  ans matant-  gebildeL  —  >)  S  3^6  No.  3.
•  j.  masa-  n.;  s.  unter  *matah-. KompE.
•  g.,  j.  mazan-  n.  'Grösse,  Erhabenheit':
dby  Google
"S7
mazant-
iSS
ahyä  xlahraca  'jUnäOSyä  ^hvapanhäiS- (sd.)i'a  tSm  (näoiL  akunm)  yasamaidi  Y. 3'J.  2;  —  mihnm  .  ,  yahmi  ..  'sa  amava nilahm  Yt./o.  64(?).
Zum  Adj.  tnat:  — VgL  ai-  mahimin-  m.  (:  g.
maian-  ^  ai,  Arwid«-  -  aus  «r.  ira(ji)ma»-  — :
j.  jj-ayOH-)").  —  >)  S.  daiu  Bloomfibld  JAOS.
r6,  CLVI,  JScHMiDT  Krit.  87  fS.  und  auch  Bgm.
GrCrJ  1S8  zu  ^V  (m[t  Litt  das.).
•  j.  mazant-  Adj.''  'gross,  geräumig;  um- fassend, gewaltig;  erhabeo':  mathan?m  . . 'zat  anattf  Yt.  10. 44;  —  Aau  'za  (NS.) mtnyS  stOHsXt.  14.^1;  F.iJ*'; — yämm.. *sänbm  Y.  6$.  11;  —  xratam  ,  .  masiUm 'sSnttm  apairi.ä^nm  (sd.)  Y.  ö'a.  4;  — sraosasca . ,  'za  amava  v^n^raja  Vr,  15. 3.
Zum  Adj,  niiz- ;  td.  No.  I.  —  ai.  mahäHl-  Adj.  — Pii. !  mm.  ~-  •>  iFlei, ».  S  rSr  b,  J95,  Richtbr IF.  p.  52.  —  »>  Nur  in  K.
•  j.  mazav-  Adj.  'acht  habend  auf  — ',  mit Gea:  a^a  spamm  nida%}m  yat  dim  'zacs (NS.)  k)hrps  türahe  "den  Hund  habe  ich dazu  bestimmt,  dass  er  acht  habe  auf  die Person  des   Tärere"  V.  13.  39.
Zum  V.  mand-;  aus  Kt.*maäzhau-,  SJi-8.  — Vgl.  got.  mundo}  'observale'.  —  Pü. :  ie  an roadak  ienä(ya)nd ßa  iarp  a/ar  lürän,  eiLi iiitiäsiärä»  t^i  däril,
•  j.  'mazah-  n.  i)  'Grösse,  Umfang' :  _>iaj:& .  .  daxmanqm  avavantpm  'xS  vltsnayäj ya^a  hl  tanus  aahat ". .  (soviel  an  Grösse als  . .  sva)  ein  Stück  so  gross  als  . ."  V. 7.  51.  2)  (etwa)  'Fülle':  'zJ  avahyai  °tS raßmSJiyai  däidl  hauruatä  am>r>tätü  "ge- währe zur  Hilfe  die  Fülle,  zur  Unterstützung die  FüUe  des  H.  und  A."  Y.  5Ä  7.
KompE.  —  Zum  Adj.  maz-.  —  ai.  mäAas-  □. —  Pü.  (zu  V.)!  masäi,  (zu  Y.):  war-
•  j.  *matah-  n.,  maza-  m.  "Draufgeld, PJänd;  Pfandwert"*.
KompE.  —  Zum  ai.  V.  mämkaU  'er  gibt hin'(?).  —  Eig.  'was  man  drauf  gibt';  Gdn. Stud.  /.  95.  —  Pa.:  masäk.  —  1)  Nicht  'Wert' übeibaupt;  das  ist  arijah-,
•  j.  ^mazah-  Adj.:  s.  unter  masyak-.
•  p.  ut3  ty(^  iunavahy  av^taiy  t^ural'- mazdä  "mazänam  kunautuv  "und  was  du tust,  das  möge  ^x  AhM.  gross  (berühmt)'* machen"  £h.  ^16.
```


## [2026-09-07T15:53:46.937Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD mayan/miyan ===\"; grep -n '^mayān\\|^mayan\\|^miyān\\|^miyan' PHD.txt | head\necho \"=== PHD mas/meh/mahist ===\"; grep -n '^mas \\|^meh \\|^mahist\\|^mas,\\|^meh,' PHD.txt | head\necho \"=== NYB ===\"; grep -n 'mayān\\|miyān\\|^mas\\b\\|^meh\\b\\|mahist' NYB_vol2_glossary.txt | head -20"
}
```


### [2026-09-07T15:53:47.012Z] TOOL RESULT

```
=== PHD mayan/miyan ===
127:mayānjīg ... add arbiter. for | !"?mez- read ! *mēz-, v. 'mēzišn, mistan.
466:mayān [mdy’n' | М my’n, N miyān] middle; among, between. ~ag [-k! | N ~a] middling, average.
=== PHD mas/meh/mahist ===
444:mahist [msst!, mhst! | M mhyst, N ~] greatest. makóg [mkwk' | M mkwg, N mako(k)] boat. mālīdan [m’lytn' | N ~] = muštan.
477:meh [ms | M mhy, myh, N ~] great(er), old(er).
=== NYB ===
496:apa-kandan [LMYTN-tn'; Prth RMY-] pt. = pret. pass. 3d p. sg. apakand, written LMYTN without complement HajB:8, books LMYTN-t', Prth RMY-t HajA:7; LMYTN without complement = opt. apakané HajB:15; subju. 2nd p. sg. LMYTN-h = apakanäh 1009; cond. 2nd p. sg. LMYTN-t' HWH'-? = apakand hà 2226: to throw; bē ~ to throw away, with 6 or andar 6 to, into, against 2226 etc. passim; to throw (a bucket into the well) 142°. 151; to drive (a horse) against (6) 1145; to shoot (an arrow) HajA: 7. B: 8.15; - to arouse (fear) 5278; 6 miyān ~ to provoke (enmity) 10715; pat menišn 1... m to suggest to a p.’s mind 3712-13; — pt. apakand fallen, slain 2626. — < Olr *apa-kan- and *upa-kan- (v.s. v. apa-), from kandan, q.v.; MPrthPrs >bgndn; Verbum 172, Ghilain 55; Paz. pt. awagad, pres. awa-gan- (SGV); NP afgan- dan, augandan. V. also apa-cand, frakan- dan, pargandak.
727:2aš [^5] the independent form of the cas. obl. 3d p. sg. = enel. -$ (g. v.); always preceding the w. to which it belongs; used 1. anaphorically in the interior of a sentence after a part of the sentence which has been placed first for emphasis: andar han Zartuxst | aš hac miyān Gp i hömikän burt || u pat uléh Zartuxšt | aš han i dašn paitištān hac Osan rote burt 5615-1? (Markwart's reading, Cat. 114 n. 1, is a failure); õi (pron.) mar | aš 6 pasčh gàv apāc rānēnīt 485; — not anaphorically: Ot (prep.) fravahr + Zartuxst | aš (viz. the snake) zafar frac zat 4012-13; purr-x"arrahéh i ax" à astómand | aš hac tan xYarrah from his (viz. Zartuxšt's) bodily splendour 377-8; — taking up an encl. -§ at the beginning of the sentence, after a part of the sen- tence which carries a lengthy attribute: api-š hamäk damik i-š apar rāh bit | aš *perävanihit kart 3316-17; — after an ad- verbial phrase beginning the sentence: adak apar pat jamän | aš hanjamanénit mūtak :61° (where aš anticipates mūtak, cf. s. v. -š). — 2. to introduce the apo- dosis (as api-$, adak-i8): after kakar 31?! ; after ka 327. 3319. 341. 565. 5717. 924. after a relative clause 3219, 9824, 100?7— 101?. — Probably identical with MPrthPrs š, written as an independent w. with two dots above (another explanation of this § v. A-H III, Gloss s. v.; ? in a fragmentary context [S] is obscure). Cf am, at, atün, asän.
1283:dipivar [dpywr] secretary ŠPrs: 9. 15. Pl: 7; pl. eas. obl. —-an mahist the chief secretary 1119. 1821. 1925, — FrP 15, MS K dpywl (= dipīvar). Olr "dipi-vara- from OP dipi- ‘inscription’, BP dyp ‘document’, MPrth dyb ‘letter’ + "vara- from Av. (1360) 'var- ‘to cover, to hide, to preserve’, thus ‘he who preserves the documents’. Early contracted to dipir: Arm lw. dpir Yoxupaveóc; KZSPrth 1. 24 dpyrwpt = Prs l. 29 dpyrpt, Gr. trans- literation diBuporr, ‘chief secretary’; M PrthPrs dbyr; NP dibir, dabir (but Paz. "diver, v. next w.). Cf Bailey, BSOS VII, 1933, 76-77.
1918:hangösitak [hngwšytk'] resemblance; re- presentation; reflection (of light) 1117-21, 112*; a symbol 12021-22; — in comparisons, together with homänäk: pūt ~ homänäk (food) resembling putrid matters 7612-18; damik andar miyān i asmän ~ etön homänäk cigón ... the resemblance of the earth in the centre of the heaven is like... = the position of the earth... resembles 86°. — From ham + goš, of NP gošah ‘angle, corner, edge’: ‘having the same angle or edge’, ‘bordering on’. MPrs ’ngwsydg; Paz. angošidaa (SGV), Skr. v. drstänta ‘pattern, model’, upa- māna ‘comparison’, nidarsana, pratirūpa ‘example’. A good illustration of its ‘use and purport SGV V, 15-16.
2104:daughter of this farmer 1518-19; Frašāvart i tē pus 2319; pus + mas i Ardavàn 319; vasün martom + andar gehän 49; vas xuähisn i rāpak-karihā xudhet 746-2"; if more than one relative attribute is added the izāfat is repeated before each: 735 etc. ; 2. paraphrased by hàm i (én i, ēt 4, õi 1) and placed before its head w.; this is the definiterelative attribute: häniZar- tuxšt mätist 3612; han i težtom tap 4322-23; ete.; — forming possessives: a) placed after the headw.: 4 man my, % tē thy, 4 amāh our, % šmāh your, but in the 3d p. the encl. pron. is used: 2-5 his, her, 2-Sän their; b) plaeed before the headw. as a definite relative attribute: hàn % man pusar 51?!; & i to humat 78-16; han 7-8 burtär 43%; hàn i amah dēh 5072-3; han + či vēh-dēn 515, ete. — forming the genitive of the interrog. kē: % ke? han + kē? whose?; other constructions with the izäfat, v. the demonstr. pronouns; — after adverbs used as prepositions: peš 4, hacadar 4, hacapar i, miyān +, ete., but the MSS are very little consistent in this respect. — The limit between nominal relative clauses and relative attributes is sometimes floating. — Av. (1199 sqq.) ya-; OP ya- rare, commonly hya- (haya-
2380:mahist [mhst'] v. mas.
2469:mas
2478:mas [ms] great, big, also used as comp. (+ hac ‘than’), sup. masist [msst'] and mahist [mhst']: kū-š sok mas bit hac apürik gäv its hoofs were bigger than (those of) the other cows 49?-? (gl.); great of rank 38. 52%; ~ martin (pl. cas.
2482:mas
2483:w., pl. cas. obl. hacis-—-àn men of higher rank than oneself, one’s superiors 704; pus i ~ the eldest son 318; nātrīk i ~ the First Lady (of the harem) 4121; kunom ~ hac I shall do greater things than... 5214; pat han 1 ~ gobišn in a loud voice 4521; — masist kirpak 6971; masist rah the most excellent way 761’; dipivaran mahist the Head Scribe 1118, 1821, 19%; mahist aštak 36°; — adv. by far 977°, — Av. (1154) mas-, masan-, comp. (1156) masyah-, sup. (1155) masista-; OP *ma- Oan-, comp. *madyah-, sup. madišta-; hence in Milr: NW mas (MPrth only adv.), comp. masdtar (v. the next w.), sup. masišt (MPrth msyšt), but SW "mah . (not attested so far), comp. mahy, méh (MPrs mhy A-H I) Paz. meh, mehe, „mahi; NP mih (used as pos.), sup. mahist (MPrs mhystg ‘presbyter’ A-H II). BP has taken over NW mas as pos. and comp., and as sup. both SW mahist and NW masist, but developed, according to the SW rule: -št- > -st-, to masist, a hybrid between SW and NW. Possibly, however, -s- was pronounced -h- through- out in SW; Paz. only mahest.
2485:maséh [msyh] greatness 4716,
2579:miyānjīkēh [myd'neykyh] mediation, in- tercession 7217. — Paz. miqZi ; NP miyänji.
2580:miyānjīkihā mediately: ~ pat rah i xrat through the medium of Reason 6215,
3716:tan ... paristém adak-tān dahém ... vas zarr ... 193-4; u api-tin ... kar framā- yēm 198; täi-tän man zīvišn + gētē pat miyān kunom 67-5; agent: ka-tän pursīt hat 214; kū-tān... dit ...? 39%; vinäs t-tān kart éstét 67°; referred to by a follow- ing prep.-adv.: āfrīn-tān + xvatāi apāk the benediction of the Lord (be) with you 1281-19; — independent form atän 451,
4068:welk-] great, big, high, lofty, passim; regularly placed before its head w., seldom: after (41?. 724); in titles great, chief: ~ framatar (g. v.); ~ šahridar (q.v.); — subst., pl. cas. obl. ~-dn the magnates HajA:6 [RB’n]. B:6 [welk’n]. 42. 1133, 16? [wewlg'n'], v. Christensen, Sass. 100. 110sq. — OP vazrka-; MPrthPrs wzrg; Arm. lw. vzurk, vzork, vzruk; Paz. guzurg, guzarg; NP buzurg. No comp. and sup.; for these forms meh, mahist are used; v.s. v. mas.
6719:mehädar: masātorēh
7257:mih (mahist): mas mihmän: mahmančh mir: mérak miyànji: miyànjikeh mizd, muzd: mizd mčbad: magu-pat mü, müy: mod muhrah: muhrak müq: mök
```


## [2026-09-07T15:54:03.573Z] TOOL CALL #28: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 3
}
```


### [2026-09-07T15:54:03.581Z] TOOL RESULT

```


```


## [2026-09-07T15:54:08.460Z] TOOL CALL #29: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/m%C3%A9d%CA%B0yos",
 "prompt": "Give the reconstruction, gloss, and full descendant list (especially Avestan, Proto-Iranian, Latin, Proto-Germanic, Sanskrit, Greek). Quote the Avestan and Iranian forms exactly."
}
```


## [2026-09-07T15:54:09.869Z] TOOL CALL #30: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%85%DB%8C%D8%A7%D9%86",
 "prompt": "For the Persian word میان (miyān): give the full etymology as stated, including Middle Persian, Proto-Iranian, Avestan and PIE forms and any cited sources."
}
```


### [2026-09-07T15:54:14.491Z] TOOL RESULT

```
# Proto-Indo-European *médʰyos

**Reconstruction:** *médʰyos (non-ablauting)

**Gloss:** "middle"

**Etymology:** From *me-dʰi ("with, among"), combining the adverb *me ("near, by, with") with the locative suffix *-dʰi.

## Descendant List

The page documents descendants across multiple language families:

- **Albanian:** mjez
- **Armenian:** մեջ (meǰ)
- **Balto-Slavic:** Lithuanian mẽdis ("tree, wood"), Latvian mežs ("forest"), Old Prussian median
- **Slavic:** Proto-Slavic *meďa
- **Celtic:** Proto-Celtic *medyos
- **Germanic:** Proto-Germanic *midjaz
- **Greek:** Proto-Hellenic *métsos
- **Indo-Iranian:** Proto-Indo-Iranian *mádʰyas
- **Italic:** Proto-Italic *meðios

**Note:** The provided page does not include specific Avestan, Sanskrit, or detailed Latin forms beyond the reconstructed proto-language stage. For exact Avestan and Iranian attestations, you would need to consult the linked Proto-Indo-Iranian entry.
```


### [2026-09-07T15:54:16.191Z] TOOL RESULT

```
# Etymology of Persian میان (miyān)

According to Wiktionary, the word traces back through several language stages:

**Historical progression:** The term derives "From Middle Persian _mdyʾn'_ (mayān), from Old Persian _*madyānaʰ_, from Proto-Iranian _*mádyānah_" (composed of root elements), which ultimately connects to "Proto-Indo-European _*médʰyos_".

**Cognate languages:** The entry identifies related forms across Indo-European languages, including Avestan _maiδiia_, Sanskrit _madhya_, Ossetian _midæg_, Gilaki _men_, and Arabic _maydān_.

**Structural composition:** The Proto-Iranian form comprises "_*mádyah_ +‎ _*-anah_" elements, demonstrating how the word was constructed through morphological combination.

No specific scholarly sources beyond the Hayyim 1934 Persian-English dictionary reference are cited within the etymology section itself.
```


## [2026-09-07T15:54:24.997Z] TOOL CALL #31: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%85%D9%87",
 "prompt": "Find the Persian entry for مه meaning \"great/greater/bigger\" (not \"moon\" or \"fog\"). Give its full etymology: Middle Persian, Proto-Iranian, Avestan, PIE root, and cited sources. Also any derived forms like مهست or مهین."
}
```


## [2026-09-07T15:54:26.603Z] TOOL CALL #32: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/m%C3%A9%C7%B5h%E2%82%82s",
 "prompt": "Give the reconstruction, gloss, and descendants (Proto-Indo-Iranian, Avestan, Sanskrit, Greek, Latin, Proto-Germanic). Quote Avestan forms exactly."
}
```


### [2026-09-07T15:54:31.201Z] TOOL RESULT

```
# Proto-Indo-European *méǵh₂s

**Reconstruction:** *méǵh₂s (oblique stem *m̥ǵh₂-)

**Gloss:** "big, great"

**Key Descendants:**

- **Proto-Indo-Iranian:** *máȷ́Has
  - **Sanskrit:** महस् (máhas)
  - **Avestan:** 𐬨𐬀𐬰𐬀𐬵 (mazah)

- **Ancient Greek:** μέγᾰς (mégăs)

- **Latin:** magnus (via Proto-Italic *magnos)

- **Proto-Germanic:** *mikilaz

The adjective is classified as "athematic, amphikinetic" with distinct masculine, feminine, and neuter inflectional patterns across singular, dual, and plural forms.
```


### [2026-09-07T15:54:31.309Z] TOOL RESULT

```
# Persian مه (meh) - "Great/Big"

## Etymology

This entry corresponds to **Etymology 4** in the Wiktionary article.

**Full Etymology Chain:**
- **Middle Persian:** 𐫖𐫏𐫆 (myẖ /meh/)
- **Proto-Iranian:** *majā́
- **Proto-Indo-Iranian:** *maȷ́ʰā́
- **Proto-Indo-European:** *méǵh₂s ("great")

## Word Class & Meaning

The term functions as both an archaic adjective and noun, meaning "big," "great," or "mickle."

## Cognates

The article notes related words in English (mickle, much), Latin (magnus), and Ancient Greek (μέγας/mégas).

## Derived Terms Listed

The entry provides three derived forms:
- مهتر (mehtar)
- مه‌مانگ (meh-mâng)
- مه‌بانگ (meh-bâng)

**Note:** The forms "مهست" or "مهین" mentioned in your query do not appear in this Wiktionary entry.

## Sources

The article cites classical Persian lexicographic references by Steingass (1892), Horn (1893), and Vullers (1856–1864).
```


## [2026-09-07T15:55:05.867Z] TOOL CALL #33: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/maj%C3%A1",
 "prompt": "Give the reconstruction, gloss, descendants (Middle Persian, Persian, Avestan, Parthian, etc.) and any cited references/sources."
}
```


### [2026-09-07T15:55:07.574Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-07T15:55:08.882Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY\ngrep -n 'میان' ARY_pages.txt | head -10\necho \"=== مه ===\"\ngrep -n '^مه\\b\\|^ مه \\|مهست\\|مهتر' ARY_pages.txt | head -10\necho \"=== latin index medhyo/megh ===\"\ngrep -n -i 'medhyo\\|medhi\\|meg-\\|megh' ARY_latin_index_pages.txt | head -10"
}
```


### [2026-09-07T15:55:08.984Z] TOOL RESULT

```
52:تبایل ترکك زبان (از حدود سده‌ی پنج میلادی به بعد) موجب از میان رفتن آن زبانهای محلی گردیده
88:کوج کردهاند. طی این کوج‌های متوالی؛ آریایی‌ه با بومیان هر محل درآمیختند و در نتیجه پاک و
172:زبان‌های گوناگون شد. (وجود واژه‌های مشترک میان هند و اروپایی و زبان سامی آغازین
208:مرز میان اين دو دسته زبان هند و اروپایی خطی است که حدوداً در مرکز اروپا قرار دارد. حال اگر
211:میان این دو دسته زبان (نواحی شمال دریای سیاه) بوده است. آنچه این بیش را تا اندازه‌ای مورد ۱
230:«مردن» و «میراندن» یکی است. در هر حال» شکاف میان زبانهای «ساتم» و «ستتم» و واژگان وابسته به
231:این دوگروه حا کی از وجود خاستگاه هند و اروپائیان در حدود مرز میان این دو گروه است.
232:همسانی‌های واژگانی و آوایی دیگری نیز میان زبانهای هند و اروپایی باختری وجود دار د که
343:اروپائیان» بسیاری از بخش‌های اروپا و آسیا دارای بومیان اولیه بوده‌اند. در آبخست‌سانه‌ی (شبه
399:شماری از دانشمندان اروپایی متوجه شباهت‌هایی میان برخی از زبان‌ها شدند. آنچه که ک‌کم واضح
=== مه ===
42:مهندس حسین فلاح (بازخوانی متن پرینت دوم)
748:مهمترین این نوشتارها عبارتند از دو حماسه‌ی هومر به نام‌های «ایلیاد» و «اودیسه» و نمایشنامه‌ها و
5073:مهم 2 نررس کهن (۸۵788 ۰:00 31087718
14324:مه مهتر / ۴۳۸۳
14549:مه
16092:مهن 0۴ 0۷8281۳ 7۲8۵ ,اصهکنتت .ک05ن الما ۸۷00202025
16164:مها پرسور میور چیوز جم جوزرمتی‌زد بش00 ۸ بت۸ ,18082 و
=== latin index medhyo/megh ===
13963:(OLD CHURCH SLAVIC) A 5 MELUI, MEGHOU :(ARMENIAN) | ‘
14095:MGLA, MZHIT RUSSIAN) .g3 MEGH, MIZNE (PAHLAVI) 5 hq
14097:MHA (BOHEMIAN) .yoa y MIH, MEGHA (SANSKRIT) 2 Sail
14242:i MAISS, MAIKES (LATVIAN) (.¢!).3.93 MEGH, MESH, AFGHAN (,-4),glsil
```


## [2026-09-07T15:55:13.330Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY\nsed -n '14310,14340p' ARY_pages.txt\necho \"==== 14540-14560 ====\"\nsed -n '14540,14560p' ARY_pages.txt\necho \"==== which pdf pages ====\"\nawk 'BEGIN{RS=\"\\f\"} /مه مهتر/{print \"block\",NR}' ARY_pages.txt\ngrep -n 'میان *مرکز\\|میان.*مركز' ARY_pages.txt | head"
}
```


### [2026-09-07T15:55:14.655Z] TOOL RESULT

```
آلمانی کهن (028(/۸ بل0اتا هان): 5 (#5تای) ههام05
05 4 (۸80-85) :2/5
آلمانی (05824۸0۷): ۸8 132 8
انگلیسی کهن (للولا200 صا0): 58 ۰ |[ 593 010188 :0/05
انگلیسی (6(/0/580): انار ۱۷ 8 (98ت01)) +7
دانمارکی (0۸//574): 118 4 (010185) 0
سوئدی (9177:015/4): ۸15 برهان قاطع : ۳۵۳
بادداشت,
بازگت به: ماهیچه.
پارسي باستان (2۳8۹1/۷ 0/0): ۸۸17013۸ 1
پهلوی (۳۸/4]4۲7): 310011۸36 ,110۸6 ارمنی (۸84871۸01): 101
سانسکریت (5977): ۸5 یونانی 0782/0): را
[pdf page 482]
۹
مه مهتر / ۴۳۸۳
لاتین (/712بمل): ,۸۸610 هتیت (4177778): 1106۸۰
فرائسه (ا888(/0: 3 انا
اسپانیایی (32۸15[7): دا انا پسگشت‌ها 5
ایتالپایی ((طل7): 11( و 2۶050000
آلمانی کهن ((227۵4۸ الا (ا0): 0 (0۸613) تدارا مت
لدم شا 1 (۸/8۲۸310) ۰ قل2لاقق لا
آلمانی (058۸4۸): قرده دا برهان قاطع + یدیما
یادداشت.
چم این واژه در ارمنی: گدایی کردن.
اوستایی (/(4۳37: ,۱۳۸2۸0۲1 ,۸1۸820 گرتیکه (0072/0): 8ا[211
۵ ایسلندیکهن (0۵(/0/0۸0 )+
پارسی باستان (۳8۵/(۷ 010): ۴۲۲۵
۸ ۸ ۸819 ۸3,۹۸1 ۹۸1۸7777۷ ساکسونی کهن (540(0 0۲0): ۰ ,2/1811
پهلری (/( ان ۳): ,۸1۸۹1151 ,۱۸9 ,۸4833 آلمانی کهن (0872/۸2 1024ظ 010):
ادا : 167177 11113711
کردی (8015]1)): 3 ان انگلیسی کهن (84/ل800 010): ۰ 341۳8
==== 14540-14560 ====
گوتیک (0077/0): ,۸ ,ال۸1۸ :۸1/2/8
05 4 بلانا55,)8۳1817 (۸15۸06)
ایسلندی‌گهن (/54(/0104۸774 صا0): 198 ناه
1 ,3/۷23۷ 7 (۸11۷0) :00/5
ساکسونی کهن (540(۷ 00): ۰ 141088۸ 5 (۸۸1(0) :57
فریزی کهن (7لفا27/5 00): اد لوا با برهان قاطع : ۳۱۸۳
آلمانی کهن (057(48(۷ 074آلا 0ا0):
یادداشت,
چم‌های مختلف این واژه در زبان‌های هند و اروپایی: یاد حافظه؛ اندیشه؛ روح» یادآوری,
مه
[pdf page 490]
۲ واژه‌های 81۸8۷1۸ ,۰۸1۸2۷116 نیز از همین ربشه‌اند.
| چماگلیس سروازی نارس ۵
پهلری (۲1الل۳۸): 0 سوئدی (8701574): 165
کردی (0134ط8(): نز ون نروژی (071#014(7/): 107
بلوچی رابل‌تسهم): بلالاقلم۷ ,لاناکلقا هلندی (لع017): ود زا اِ
1 اسلاوی کهن (ع1لاشا؟ 176[7ل) (ا0):
افغانی (پشتر) (/4۳0//۸۸۷): ان : 07
سانسکریت (5/577): ,8 روسی (/(5514تا): 007
1 نی چکه (۲280/1): فا بدا نان
بونانی (54ق07): ری اد نز من بلفاری کهن (#بمتقرماناه ۰:۵۵ ۵6۸
==== which pdf pages ====
block 482
```


## [2026-09-07T15:55:24.032Z] TOOL CALL #36: Bash

```json
{
 "command": "python3 tools/ref_page.py ARY:483 --image 2>&1 | tail -30"
}
```


### [2026-09-07T15:55:30.585Z] TOOL RESULT

```
لاتین (710بما): 15 ,۸10610 هتیت (7/77775): 166۸۰
فرانسه رب ۰۳۲۵۸ 1
اسپانیایی (32۸۸/157): 3 پسگشت‌ها 5
ایتالیایی ((77(۸): 1( را را
آلمانی کهن (057442 ۲۲07 ضا0): 40 (01۲6[18) دا ۱۲/۰ ان 1و۲
ده ها 1 (۸18۳۲1۸710ش1) :۸1۸022212
آلمانی ((088۸1۸): ان 4 ۱۱۱۵۱ برهان قاطع : ۱۰۵۷
یادداشت:
چم این واژه در ارمنی: گدایی کردن,
ٍ
اوستایی (/(۸27): ‎٩۸2۸311,‏ ,۹1۸85220 گرنیکه (00777[6): ۱۷۱۱۹۱۴
1۸7 اپسلندی‌کهن ([0/00714/(م5 0۵):
پارسی باستان (۳8۶۹۲۸۷ 0آ0): ۸۸۲۲۲
2۸ ,ال ۸ ۸73,*۸1۸57۷ ۹۸1۸7۲17۷ ساکسونی کهن (//542:0 010): ۰ ,11151 :
پهلوی ( انم م): ,۸1۸۹1197 ,11۸5 ,۸/83 آلمانی کهن (4ن087 7107 010):
7( : ۷11677 ۸1177577
کردی (680157): الا نا انگلیسی کهن (8:0137 ۰:0۵ 111۳87
افغانی (پشتر) (/۸70۸/۷): ۸ انگلیسی (ل8ا8۸0): ۰ ,۸41616185 ,8111653
تخاری ۸ (۸ [(4ل7۸5ل۰)7025 ۸ اب ۱۳۹ 4
تخاری 8 (8 [(4ل7057۸): ۸۸ دانمارکی (0۸(15]4): این ابید نا
اسرد سانسکریت (84۸۷5/077): ۸۸ سوئدی (57821527): لد ید
2 8 ۱۷۸۸۵۷۲ نروژی (083701۸/0/: ,۸۲۷۳
ارمنی (/(۸۸۸48(/14): 1۹ * ۴ ایرندی کهن (تلوتق! صا0): 31۸168 ,۸۸6
برنانی 0 ات۷156 ,1186۸5 گالی (57/ل۸): ۸0(
لانین (/(77م): 1۸619788 ,81۸6۴۷۲/5 ولزی (5]7ا(): 3 نان ۱یا
فرانسه (222/۲/7: تن ۵ ۱۷ یی برتونی (/85670۸): ری بان ان!
اسپانیایی (5۳۸۸715]7): 0( آلبانی (4(7(فشلم): ۰ 1۸011۲ ,۸۸153
ایتالیایی (۵۸ل-77): وی اند ۷ ان هتیت (7177778]): ۱57
پرتغالی (۳0717010885): لا انا
```


## [2026-09-07T15:55:55.018Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nprint(json.dumps(d['BQT']['scans'],ensure_ascii=False,indent=1))\n\""
}
```


### [2026-09-07T15:55:56.311Z] TOOL RESULT

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


## [2026-09-07T15:55:59.544Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT\nawk 'BEGIN{RS=\"\\f\"} /\\[pdf page 85\\]/{print}' BQT_v4_pages.txt | head -60"
}
```


### [2026-09-07T15:56:01.051Z] TOOL RESULT

```
[pdf page 85]
م زکو ۱ سوه موس
و سکون ثالی و فوقالی » مسجد را کویند که | بالف کشیده . بلفت زند بمعنی‌ترآزوباشد وبعربی
بفارسی خانهٌ خدا و بمربی بیت‌الطٌ خواشد ۱ . میزان گوبند .

م زکو بم اول وفتح تالی و کاف مزنده * بروزن رونده؛ کوز1 بخوریرا
مشدد واغیر مشدد بواو کشیده . نوعی از طعام کویند - و بمعنی مکیدنی هم‌آمده است ‎٩‏ -
است . ومکنده را نیز کوبند که فاعل باشد چه مزیدن

هز که < بکر اول وافتح کاف :فارسی» بمعنی مکیدن است .
حوای تیره راکویند ۳ . مزنگو - با کان فارسی بر وزن

مزمل - بنم اون وفتح نانی وکسرمیم ارسطو . خاریعت را کونبند و آن جالوریت
مد وسکون لام ۰ اولهای اس انس ی مشهور ۷ #

چون برجانب راست پیچند آب از آن ۰ ی
روان شود واگربطرف چپ کردانند پایستد واین مزیف - بروزن و معنی مکید باشد که
لوله را پیشتر درحمامها وآب انارهای‌سرپوشیده | ماضی مکیدن است ۸ - ودر عربی ابممنی اضافه
اسب ‌کنند ۴ - و با تشدید ثانی وثالث» درعربی و زباده کرده شده باشد ‎٩‏ .
بممتی درجامه پیچیده باشد ۴ . مزیدن *۱- بر وزن و ممنی مکیدن
هزفا* -یکر اول وسکون ای‌ویون | باشد -
۹ - تو هشرف تری زهر هردم همچو بیت الحرم زهر مز کت .
سوزنی سمرقتدی « رشیدی ».

۴ - رك : رشیدی. ۴ - در فاموسهای عربی‌باین ممنی نیامده؛ ولی‌دریین‌النهرین
هنوز « مزمله > بهمین ممنی استممال شود :

پیروزه همچو سیم کشیده فرو رود از کوشهٌ مزمل زرین بآبدان .

۰ ازرقی‌هروی « جهانگیری > ورك : رشیدی.

۴ - رك : اقرب الموارد . قطرالحیط » منتهی‌الارب .

-هز . 3۵288 , 1322108 ۰ پهلوی 18۳3201 ( ترازو ) « بونتکر ص ۱۱۷
قی : میزان (عر) . ‎٩‏ - باین ممنی نیست و صحیح بمعنی آخراست که اسم قاعل باشد ‏

۷ - رك : مرنگو . ۸ -رك : مزیدن - ‎٩‏ -رك : اقرب الموارد »
منتعی‌الارب . *- پهلوی 733101128 ۰ کردی ۲۳1410 . 13120177 ( مکیدن ) »بلوچی
8 , طع2ط219 ( مکیدن ) . از ریشة -71326۹/6 ( مکیدن ) «* اسشق ۹۷۹ * «وبشمان
( )کوید : ريشة این کلمه , چنانکه از اشکال لهجه‌بی برمباید 8211 , 7106 ( ع180.
قس : کردی ۳662۳۵ . پهلوی 778021 با 32102۴7 ۰ بازند 1۳12 , 131202 ) است .
همچنین 13821080 بجای 171210427 بکار رفته است .

مزه - بفتح اول و دوم ( درلهجة مرکزی بکسر دوم )؛پهلوی 13602 , 2310216
تاوادیا ۱۹۳ > ۰ کردی ع 12626 ( ذوق . طعم ) « ژابااص ۳۹۷ > اس : عربی « مزة [ بفتح
اول ] یکبار مکیدن » « منتهی‌الارب * رك : مزبدن ؛ کیفیتی که از چشیدن و جوبدن ولوشیدن
ادراك شود مثل شیرینی, شوری , تلخی و جزآنها - پممنی مزبدن هم آمده - آنچه با مشروب
خورند ( از قبیل آجیل » سبزی و غیره ).

(برهان قاطع ۲۵۳)
```


## [2026-09-07T15:56:12.385Z] TOOL CALL #39: Bash

```json
{
 "command": "python3 tools/ref_page.py BQT:2002 --image 2>&1 | tail -8"
}
```


### [2026-09-07T15:56:13.751Z] TOOL RESULT

```
0 هزه - بفتح اول و دوم ( درلهجة مرکزی بکر دوم )ءپهلوی 602 ۰ 1210816
« تاوادیا ۱۹۳ > ۰ کردی ع 13626 ( ذوق . طعم ) « ژاباص ۳۹۷ ۰ قس : عربی « مزة [ بفتح
اول ] یکبار مکیدن » « منتهی‌الارب * رك : مزیدن ؛ کیفبتی که از چشیدن , جویدن ولوشیدن
ادرا شود مثل شیرینی» شوری , تلخی و جزآنها - بمعنی مزبدن هم آمده - آنچه با مشروب
خورند ( از قبیل آجیل » سبزی و غیره ).

(برهان قاطع ۳۵۳)
```


## [2026-09-07T15:56:16.917Z] TOOL CALL #40: Bash

```json
{
 "command": "python3 tools/ref_page.py BQT:2002 --image 2>&1 | grep -i 'png\\|path\\|vision\\|cache' | head"
}
```


### [2026-09-07T15:56:18.330Z] TOOL RESULT

```
IMAGE: /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/2002.png
```


## [2026-09-07T15:56:20.835Z] TOOL CALL #41: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/2002.png"
}
```


### [2026-09-07T15:56:21.303Z] TOOL RESULT

```

```


## [2026-09-07T15:56:21.300Z] INPUT

[Image: original 1650x2546, displayed at 1296x2000. Multiply coordinates by 1.27 to map to original image.]


## [2026-09-07T15:56:43.944Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT\nawk 'BEGIN{RS=\"\\f\"} /\\[pdf page 141\\]/{print}' BQT_v4_pages.txt | head -70"
}
```


### [2026-09-07T15:56:45.427Z] TOOL RESULT

```
[pdf page 141]
موبه زال رها
تحتانی , گریه با توحه را گوبند - وناله وزاری مو بیدن ۴ (۱) - بروزن‌روبیدن(؟)
را نیز کفته‌اند . بممنی کربه وتوح ه کردن وگریستن باشد.
موی ذال - با زای قله دار بالف موییته ۴ (۳) < بنتم نون . پوستین
کنیده پا زده ام نوی و لحنی باشد که | راکویند مطلقاً خواء سنجاب وخواء سمور وقاقم
مطربان داز , دخواند َ وامتال‌آن باشد - و مو بینه(۳)دودیوستن
مویه گر ۴ - بنتح‌کاف فارسی » توحه | ووز را میکویند :
کننده راگوند .
بیان بیمت 9 هفتم
در میم با ها مشتمل بر هفتاد و هشت لغت و کنایت
۸ -« بفتح اول و ظهورئانی . مخفف ماء | ودرنفرین ودعا هردواستعمال میشود همچومپیناد۹
است که قمرباشد 8 - و بخفای ثالی » بممتی نه | - وبممنی قلم وكلك هم بنظرآمده است - وتل
باغد که حرف نفی‌است وبعربی‌لاگوبند ؛ وافادة | ریگه را نی زگویند - و بکر اول وظهورئانی »
معدوم شدن ونابو دکردیدن هم میکند مثل «مه | بمعنی بزرکه باشد ۷ چه بزرکتر را ههتر
این ماند ومه آن > پعنی نه این ماند و نه‌آن ؛ | خوانند - و بمعنی میغ ونزم هم‌آمده است وآن
() چش : موئیدن - (۷) چش : روئیدن . (۳) چش : موئینه .
- بلفظ پارسی وچینی و خماخرو بلحن مویهٌ زال و قصیدء لغزی .
« منوچهری دامغانی ص ۰۶۱۱۲
۴ - از : موبه + کر ( پسوند شغل و مبالقه ). ۴ - از : موی (موبه[هم.] )
۳+یدن ( پوند مصدری ) . رك : اسشق ۹۹۷ ؛ دارمستتر . تتبعات ج۲ ۰۱۹۹
۴ - از : موی +ینه ( پسوند نبت ) . 6 رد : ماه
‎٩‏ - پپلوی 78 (علامت نپی ) ۱ 16170 28 ( مکن ) » ابرانی باستان 32 «بارتولمه
۵ نیب رکه ص ۱۶۳ > ؛ پارسی باستان واوستا و هندی باستان 22 (نه) » پازند 132 ۰
ارمنی 821 (که نیست) » افغاتی -338 ۰ استی -1328 ( مه » علامت نغی ) «* اسشق۹۹۸؛ کردی
6 ( نه, مه [علامت‌نهی] ) «ژابا ۰4۰۹ پشتو7728 «بلیو س۱۵۹*.ورك: مقدمةٌ موّلف م‌به.
۷ - پهلوی 1360 ( بزرکتر ) ۰ پارسی باستان -321[01(20 5 » ایرانی باستان
-31881/20 « نیب رکه مر ۰۱4۸۸ اوستا 71388220 (بز رکتر) . نیزیهلوی 1388 ( بز رکه .
بز رکش » بزرکترین ) » 88151( ۰ 188)1(81 , فقس : 1328]۳328020 ( بز رکه و رئیی
مفان ) ؛ ۲۵1191 , پازید 3610 , ارمنی 13360 ( بز رکه ) . افغانی 1328287 ( آرشده آقا)
«اسشق۹۹۹*. صبغهٌ عالی‌از۰526]0 پازند, ۰5220654 12212854 ۳ پارسی باستان -1224[218012
است . در کردی 1328117 ( بزرکتر ) » کاشانی 119527 ۰ 717218867167 آهده ۶ هوبشمان
۹ > خوانداری ۳308527 ( بزرکتر ) ۸« سالنامة کلپایگان ‎4٩‏ > . نایینی 77128518
(بز رکه) .کبری زد 185 . رك : ...,81202086 ۲۵۵ 1۵ 6:0 2 ۹۵ 310165 ,وج
( .1.0.1 ,۷1 1040-1782168 )
( برهان قاطع ۳۹۰ )
```


## [2026-09-07T15:57:25.682Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== NYB printed page for mas entry ===\"\nawk 'BEGIN{RS=\"\\f\"} /^.*mas \\[ms\\] great, big/{print \"leaf(1-based)\",NR}' NYB_vol2_glossary.txt\necho \"=== AHD watkins medhyo / meg ===\"\ngrep -n '^medhyo\\|^meg-\\|^me-3\\|^mag-' AHD_watkins1985.txt | head\necho \"=== IEC ===\"\ngrep -n '^medhjos\\|^medhios\\|^medhio\\|^meg-\\|^megh-\\|^meg^h' IEC.txt | head\necho \"=== HUB miyan/mih ===\"\ngrep -n 'miyän\\|miyan\\|maiöyqna\\|maidyana' HUB.txt | head\ngrep -n '999\\. \\|mih ' HUB.txt | head"
}
```


### [2026-09-07T15:57:27.178Z] TOOL RESULT

```
=== NYB printed page for mas entry ===
leaf(1-based) 142
=== AHD watkins medhyo / meg ===
709:mag-. Also mak-. To knead, fashion, fit. 1. Germanic *mak- in: a. Germanic verb *makén, to fashion, fit, in (i) Old English macian, to make: MAKE (ii) Old French mason, mason: MASON; b. Germanic compound noun *ga-mak-(j)6n (*ga-, with, together; see kom), “he who is fitted with (another),” in Old English gemzcca, mate, spouse: MATCH}, 2. Germanic nasalized form *mangjan, to knead together, in: a. Old English mengan, to mix: MINGLE; b. Old English gemang (ge-, together; see kom), mixture, crowd: AMONG, MONGREL. 3. Suffixed form *mak-yo- in Greek massein (aorist stem mag-), to knead, hence magma, unguent: MAGMA. 4, Suffixed length- ened-grade form *mdg-ya- in Greek maza, a (kneaded) lump, barley cake: MASS; (AMASS), MAZAEDIUM. 5. Suf- fixed lengthened-grade form *mék-ero- in Latin macerdre, to tenderize, to soften (food) by steeping: MACERATE. [Pok. mag- 696, 2. madk- 698, men(a)k- 730.]
731:meg-
=== IEC ===
10446:medhior- (medhiar-) ‘midmost; middle, centre Gk. cf. meséres *midmost, internal; Alb. (me- tath.) zemër ‘heart’, (cf. also Alb. parzém, par- mëz, f. “breast, bosom’; Gk. promesó-, cpds. *middle-); Cz. mezera, Slovak medzera *space, interval
10447:medhios, à, io ‘middle; midst, centre’. WP II, 261 Skt. madhyah, adi. madhyam, n.; madhyá, adv. “in the middle’; Av. maióyo, adi: Oss. mid-, Dig. med- ('inside-, cpds.); cf. medág, adj. ‘inner’; Lyc. postp. (queried) miïtə “in- side’; Arm. meg, i meg "mm: meðk E mg£, gs mi£o, o-st. ‘middle, waist; Gk. mésos, més- sos, adj.; Myc. cf. mesato- (queried: "mid. most); Phryg. (Hes.) mézea, npl ‘genitals’; Alb. mes & mez, def. mezi “middle, waist, interval; meze, f. (setting, milieu', fr. *me- dhio); Lat. medius, adj.; cf. ni-mis ('exces- sively’, fr. *ne- *medhs- ? or -meds?); Osc. mefiaí, loc. sg f. ‘middle’; MIr. mid, adj. (‘half , cpds: ‘mid-’); Gaul. medio-, Sequanian mid-; W medd, m. ‘centre of motion, pivot’; Go. midjis, adj.; MHG mët-, cpds.; OE midd, midde, adj. & sf; OS middia, f. (middle: Ir. midhe, f. id.); ON miója, id. beside mióju “in the middle’; miór, adj.; Sw. midja, f., Norw. midje ‘waist; OCS mezda f. beside meZzdu ‘between’; Slovene medja *borderland'; Li. (?) cf. medis, gs medžio ‘tree’; mede ‘wood’; Latv. mežs (forest. (Note that Li. medžio vidus: E mid-wood with the terms reversed!) Cf. also some Lat. cpds. with mer-, cf. mer- idiés ‘midday’; mer-enda ‘snack meal’, if for *medh-edna, and mer-cedonius ménsis 'inter- calary month'
10476:megh- (2) element of 1st. pers. sing. pron. T, me?
=== HUB miyan/mih ===
4471:sassanid. Hormizd, arm. Ormizd^ ap. A(h)uramazdd; miyan
4472:'Mitte* = paz. phi. miyan ^ zd. mai^yfina-; piyada 'Fuss-
5330:821; saya *Schatten H. 695; xaya *Er H. 468;' miyan 'Mitte
5346:Mp. immer geschwunden (also auch miyan *Mitte' = "^midan
5918:yada H. 347, miyan H. 1004) oder tritt ein in: zer *unter,
7085:— 46)Vjp»y^rfa *Pussganger' = skr. paddti-y padatika-; miyan
7086:'Mitte' = paz. phi. miyan, zd. maiSyqna^ ; bayd, bayog 'Braut'
1122:np. mih gross : zd. masyah^, ^) hih klein : zd. kasyah-,
3499:999. Zu paz. meh lautet der Superl. mahest, maMst (Min.
4021:iiber np. mih gross', ap. wa^- im sup. mat^ista-, kih *klein',
4496:mih 'gross* = paz. meh *gross, grSsser Min. Gl. 138,
4525:hih = phi. v9h zu erklSren, nicht aber mih und kih (= phi. m-£ und k^s.)
7490:Np. mih gross* = paz. meh Shk. 258, phi. ina&, ap.
```


## [2026-09-07T15:57:39.426Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor L in 1122 4471 7085 7490; do\n  P=$(awk -v L=$L 'NR<=L{n+=gsub(/\\f/,\"\")} END{print n}' HUB.txt)\n  echo \"line $L -> formfeeds $P -> printed ~$((P+1-10))\"\ndone\necho \"=== AHD meg- ===\"; sed -n '731,733p' AHD_watkins1985.txt\necho \"=== AHD medhyo ===\"; grep -n 'medhyo\\|MIDDLE\\b' AHD_watkins1985.txt | head"
}
```


### [2026-09-07T15:57:40.697Z] TOOL RESULT

```
line 1122 -> formfeeds 44 -> printed ~35
line 4471 -> formfeeds 138 -> printed ~129
line 7085 -> formfeeds 210 -> printed ~201
line 7490 -> formfeeds 220 -> printed ~211
=== AHD meg- ===
meg-
form *m6-ro- in Gaelic mor, big, great: CLAYMORE. [Pok. 4, mé- 704.] mé-4, To cut down grass or grain with a sickle or scythe. Contracted from *mea-. 1. Germanic *mé- in Old English mawan, to mow: Mow?. 2. Suffixed form *mé-ti- in Germanic *médiz in Old English m#th, a mowing, a mown crop: AFTERMATH. 3. Suffixed form *mé-twd-, a mown field, in Germanic *médw6 in Old English méd (oblique case m&@dwe), meadow: MEAD?, MEADOW. [Pok. 2. mé- 703.] med-. To take appropriate measures. 1. a. Germanic *metan in Old English metan, to measure (out): METE!; b. Germanic derivative *m#t6, measure, in Old English gem&te (ge-, with; see kom), “commensurate,” fit: MEET?. 2. a. Latin medéri, to look after, heal, cure: MEDICAL, MEDICATE, (MEDICINE), (MEDICO); METHEG- LIN, REMEDY; b. Latin meditdri, to think about, con- sider, reflect: MEDITATE. 3. Suffixed form *med-es-, replaced in Latin by *modes- by influence of modus (see 4. below), in: a. Latin modestus, “keeping to the appro- priate measure,” moderate: MODEST; IMMODEST; b. Lat- in moderdre, “to keep within measure,” to moderate, control: MODERATE; IMMODERATE. 4. Suffixed o-grade form *mod-o- in Latin modus, measure, size, limit, man- ner, harmony, melody: MODAL, MODE, MODEL, MODERN, MODICUM, MODIFY, MODULATE, MODULE, MODULUS, MOLD!, (MOOD?), (MOULAGE); (ACCOMMODATE), (COM- MODE), COMMODIOUS, (COMMODITY). 5. Suffixed o-grade form *mod-yo- in Latin modius, a measure of grain: MODIOLUS, MUTCHKIN. 6. Possibly lengthened o-grade form *méd- in Germanic *mét-, ability, leisure, in: a. Old English métan, to have occasion, to be permitted or obliged: MOTE2, MUST}; b. Germanic compound é-mot-ja- (prefix *é-, meaning uncertain, from Indo- hinppoes é, 6; see Pok. é, 6 280) in Old English émetta, rest, leisure: EMPTY. [Pok. 1. med- 705.] medhu-. Honey; also mead. 1. Germanic *medu in Old English meodu, mead: MEAD!. 2. Greek methu, wine (> methuein, to be intoxicated): AMETHYST, METHYLENE. [Pok. médhu 707.] medhyo-. Middle. 1. Germanic *midja- in: a. Old English midd(e), middle: M1D!; AMID; b. West Germanic diminu- tive form *middila- in Old English middel, middle: MIDDLE; Cc. Germanic compound *midja-gardaz, “middle zone” (*gardaz, enclosure, yard; see gher-1), name of the earth conceived as an intermediate zone lying between heaven and hell, in Old Norse Midhgardhr, Midgard: MipGarD. 2. Latin medius, middle, half: MEAN, MEDIAL, MEDIAN, MEDIASTINUM, MEDIATE, MEDIUM, MITTEN, MIZZEN, MOIETY, MULLION; INTERMEDIATE, MEDIEVAL, MEDIOCRE, MEDITERRANEAN, MERIDIAN, MILIEU. 3. Greek mesos, middle: MESO-. See also me-2. [Pok. medhi- 706.] meg-. Great. 1. Germanic suffixed form *mik-ila- in: a. Old English micel, mycel, great: MUCH; b. Old Norse mikill, great: MICKLE. 2. Suffixed form *mag-no- in Latin magnus, great: MAGNATE, MAGNITUDE, MAGNUM; MAG- NANIMOUS, MAGNIFIC, (MAGNIFICENT), (MAGNIFICO), (MAGNIFY), MAGNILOQUENT. 3. Suffixed (comparative) form *mag-yos- in: a. Latin major, greater: MAJOR, MAJOR-DOMO, MAJORITY, MAJUSCULE, MAYOR; b. Latin majestds, greatness, authority: MAESTOSO, MAJESTY; c. Latin magister, master, high official (< “he who is greater”): MAESTRO, MAGISTERIAL, MAGISTRAL, MAGIS- TRATE, MASTER, (MISTER), MISTRAL, (MISTRESS). 4. Suf- fixed (superlative) form *mag-samo- in Latin maximus, greatest: MAXIM, MAXIMUM. 5. Suffixed form *mag-to-, “made great,” in Latin mactus, worshiped, blessed, sacred: MATADOR. 6. Suffixed (feminine) form *mag-ya-, “she who is great,” in Latin Maia, name of a goddess: May. 7. Suffixed form *meg-a-l- in Greek megas (stem megal-), great: MEGA-, MEGALO-; ACROMEGALY, ALMA- GEST, OMEGA. 8. Variant form *megh- in Sanskrit maha-,
mei-'
=== AHD medhyo ===
521:gher-'. To grasp, enclose; with derivatives meaning “enclosure.” 1. Suffixed zero-grade form *ghr-dh- in: a. Germanic *gurdjan in Old English gyrdan, to gird: GIRD; b. Old English gyrdel, girdle: GIRDLE; c. Old Norse gjordh, girdle, girth: GirTH. 2. Suffixed o-grade form *ghor-dho- (in Germanic) or *ghor-to-, an enclosure, in: a. Germanic *gardaz in (i) Old English geard, enclosure, garden, yard: YARD?; ORCHARD (ii) Old Norse gardhr, garden, yard: GARTH (iii) Old High German garto, gar- den: KINDERGARTEN (iv) Old North French gardin, gar- den: GARDEN (v) compound *midja-gardaz, “middle zone,” earth (see medhyo-); b. Latin hortus, garden: HORTICULTURE, ORCHARD, ORTOLAN. 3. Prefixed and suffixed zero-grade form *ko(m)-ghr-ti- (*ko(m)-, collec- tive prefix, “together”; see kom) in Latin cohors (stem cohort-), enclosed yard, company of soldiers, multitude: COHORT, CORTEGE, COURT, COURTEOUS, COURTESAN, (COURTESY), COURTIER, (CURTILAGE), (CURTSY). 4. Per- haps suffixed o-grade form *ghor-o- in Greek khoros, dancing ground (? perhaps originally a special enclosure for dancing), dance, dramatic chorus: (CHOIR), (CHORAL), (CHORALE), CHORIC, (CHORISTER), CHORUS; CHORAGUS, TERPSICHORE. [Pok. 4. gher- 442, gherd- 444.]
730:tive masculus, male, manly: MACHO, MALE, MASCULINE; EMASCULATE.] mat-. A kind of tool. Old English mattuc, mattock (prob- ably borrowed from Vulgar Latin *mattea): MATTOCK. [Pok. 2. mat- 700.] mater-. Mother. Based ultimately on the baby-talk form ma-2, with the kinship term suffix -fer-. 1. Germanic *méthar- in Old English mddor, mother: MOTHER}. 2. Latin mater, mother: MATER, MATERNAL, MATERNITY, (MATRICULATE), MATRIX, MATRON; MADREPORE, MATRI- MONY. 3. Greek métér, mother: METRO-; METROPOLIS. 4, Latin mdteriés, materia, tree trunk (< “matrix,” the tree’s source of growth), hence hard timber used in carpentry, hence (by a calque on Greek Aulé, wood, matter) substance, stuff, matter: MATERIAL, MATTER. 5. Greek compound Démétér, name of the goddess of produce, especially cereal crops (dé-, possibly meaning “earth”): DEMETER. [Pok. mdter- 700.] math-. Worm. With uncertain preform, but clearly re- lated, is Old English moththe, moth: motu. [Pok. 1. math- 700.] [Mawort-. Name of an Italic deity who became the god of war at Rome (and also had agricultural attributes), hence also the name of the planet Mars (doubtless from its red color, the color of blood). Latin Mars (stem Mart-), Mars: MARCH, MARS, MARTIAL, MARTIAN.] mazdo-. Pole, rod, mast. Germanic *mastaz in Old Eng- lish mest, mast: MAST}. [Pok. mazdo-s 701.] me-1. Oblique form of the personal pronoun of the first person singular. For the nominative see eg. 1. Germanic *mé- in Old English mé (dative and accusative): ME, MYSELF. 2. Possessive adjective “mei-no- in Germanic *min- in: a. Old English min, my: MINE?, My; b. Middle Dutch mijn, my: MYNHEER. [Pok. 1. me- 702.] me-2, In the middle of. 1. Suffixed form *me-dhi in Germanic *mid- in Old English mid, among, with: MID- WIFE. 2. Suffixed form *me-ta in Greek meta, between, with, beside, after: META-. See also medhyo-. [Pok. 2. me- 702.] mé-1, Expressing certain qualities of mind. Contracted from *meo-. 1. Suffixed o-grade form *mé6-to- in Ger- manic *méthaz in (i) Old English méd, mind, disposition: MooD! (ii) Old High German muot, mind, spirit, in German Gemiit, spirit, feelings, temperament: GEMUT- LICH, GEMUTLICHKEIT. 2. Perhaps Latin més (< *mé-s-), wont, humor, manner, custom: MORAL, (MORALE), MORES, MOROSE. [Pok. 5. mé- 704.] m6-2, To measure. Contracted from *meo-. I. Basic form mé-. 1. Suffixed form *mé-lo- in Germanic *mélaz in Old English m#l, “measure, mark, appointed time, time for eating, meal”: MEAL?; PIECEMEAL. 2. Suffixed form *mé-ti- in Latin métiri, to measure: MEASURE, (MEN- SURAL); (COMMENSURATE), DIMENSION, IMMENSE. 3. Possibly Greek metron, measure, rule, length, propor- tion, poetic meter (but this is referred by some to med-): METER!, METER?, (METER?), -METER, METRICAL, -METRY; DIAMETER, GEOMETRY, ISOMETRIC, METROLOGY, METRO- NOME. 4, Suffixed form *mé-trd- in Sanskrit mdtrd, a measure: MAHOUT. II. Extended and suffixed forms *mén-, *mén-en-, *mén-s-, *mén-dt-, moon, month (an ancient and universal unit of time measured by the moon). 1. Germanic *ménén- in Old English ména, moon: Moon; (Monpay). 2. Germanic *ménéth- in Old English ménath, month: MONTH. 3. Greek mén, méné, month: AMENORRHEA, CATAMENIA, DYSMENORRHEA, (MENARCHE), MENISCUS, MENOPAUSE. 4. Latin ménsis, month: MENSES, MENSTRUAL, (MENSTRUATE); BIMES- TRIAL, SEMESTER, TRIMESTER. [Pok. 3. mé- 703, ménot- 731. fen Big. Contracted from *meo-. 1. Suffixed (compara- tive) form *mé-is- in Germanic *maiz6n- in Old English mara, greater, and madre (adverb), more: MORE. 2. Suf- fixed (superlative) form *mé-isto- in Germanic *maista- in Old English m&st, most: Most. 3. Suffixed o-grade
732:form *m6-ro- in Gaelic mor, big, great: CLAYMORE. [Pok. 4, mé- 704.] mé-4, To cut down grass or grain with a sickle or scythe. Contracted from *mea-. 1. Germanic *mé- in Old English mawan, to mow: Mow?. 2. Suffixed form *mé-ti- in Germanic *médiz in Old English m#th, a mowing, a mown crop: AFTERMATH. 3. Suffixed form *mé-twd-, a mown field, in Germanic *médw6 in Old English méd (oblique case m&@dwe), meadow: MEAD?, MEADOW. [Pok. 2. mé- 703.] med-. To take appropriate measures. 1. a. Germanic *metan in Old English metan, to measure (out): METE!; b. Germanic derivative *m#t6, measure, in Old English gem&te (ge-, with; see kom), “commensurate,” fit: MEET?. 2. a. Latin medéri, to look after, heal, cure: MEDICAL, MEDICATE, (MEDICINE), (MEDICO); METHEG- LIN, REMEDY; b. Latin meditdri, to think about, con- sider, reflect: MEDITATE. 3. Suffixed form *med-es-, replaced in Latin by *modes- by influence of modus (see 4. below), in: a. Latin modestus, “keeping to the appro- priate measure,” moderate: MODEST; IMMODEST; b. Lat- in moderdre, “to keep within measure,” to moderate, control: MODERATE; IMMODERATE. 4. Suffixed o-grade form *mod-o- in Latin modus, measure, size, limit, man- ner, harmony, melody: MODAL, MODE, MODEL, MODERN, MODICUM, MODIFY, MODULATE, MODULE, MODULUS, MOLD!, (MOOD?), (MOULAGE); (ACCOMMODATE), (COM- MODE), COMMODIOUS, (COMMODITY). 5. Suffixed o-grade form *mod-yo- in Latin modius, a measure of grain: MODIOLUS, MUTCHKIN. 6. Possibly lengthened o-grade form *méd- in Germanic *mét-, ability, leisure, in: a. Old English métan, to have occasion, to be permitted or obliged: MOTE2, MUST}; b. Germanic compound é-mot-ja- (prefix *é-, meaning uncertain, from Indo- hinppoes é, 6; see Pok. é, 6 280) in Old English émetta, rest, leisure: EMPTY. [Pok. 1. med- 705.] medhu-. Honey; also mead. 1. Germanic *medu in Old English meodu, mead: MEAD!. 2. Greek methu, wine (> methuein, to be intoxicated): AMETHYST, METHYLENE. [Pok. médhu 707.] medhyo-. Middle. 1. Germanic *midja- in: a. Old English midd(e), middle: M1D!; AMID; b. West Germanic diminu- tive form *middila- in Old English middel, middle: MIDDLE; Cc. Germanic compound *midja-gardaz, “middle zone” (*gardaz, enclosure, yard; see gher-1), name of the earth conceived as an intermediate zone lying between heaven and hell, in Old Norse Midhgardhr, Midgard: MipGarD. 2. Latin medius, middle, half: MEAN, MEDIAL, MEDIAN, MEDIASTINUM, MEDIATE, MEDIUM, MITTEN, MIZZEN, MOIETY, MULLION; INTERMEDIATE, MEDIEVAL, MEDIOCRE, MEDITERRANEAN, MERIDIAN, MILIEU. 3. Greek mesos, middle: MESO-. See also me-2. [Pok. medhi- 706.] meg-. Great. 1. Germanic suffixed form *mik-ila- in: a. Old English micel, mycel, great: MUCH; b. Old Norse mikill, great: MICKLE. 2. Suffixed form *mag-no- in Latin magnus, great: MAGNATE, MAGNITUDE, MAGNUM; MAG- NANIMOUS, MAGNIFIC, (MAGNIFICENT), (MAGNIFICO), (MAGNIFY), MAGNILOQUENT. 3. Suffixed (comparative) form *mag-yos- in: a. Latin major, greater: MAJOR, MAJOR-DOMO, MAJORITY, MAJUSCULE, MAYOR; b. Latin majestds, greatness, authority: MAESTOSO, MAJESTY; c. Latin magister, master, high official (< “he who is greater”): MAESTRO, MAGISTERIAL, MAGISTRAL, MAGIS- TRATE, MASTER, (MISTER), MISTRAL, (MISTRESS). 4. Suf- fixed (superlative) form *mag-samo- in Latin maximus, greatest: MAXIM, MAXIMUM. 5. Suffixed form *mag-to-, “made great,” in Latin mactus, worshiped, blessed, sacred: MATADOR. 6. Suffixed (feminine) form *mag-ya-, “she who is great,” in Latin Maia, name of a goddess: May. 7. Suffixed form *meg-a-l- in Greek megas (stem megal-), great: MEGA-, MEGALO-; ACROMEGALY, ALMA- GEST, OMEGA. 8. Variant form *megh- in Sanskrit maha-,
1238:AMID medhyo- AMIGO amma AMISS_ mel-1
1682:INTER en, ters- INTERCALATE kela-2 INTERCEDE ked- INTERCEPT kap- INTERCOSTAL kost- INTERCOURSE kers-2 INTERDICT deik- INTEREST es- INTERIM en INTERIOR en INTERJECT yé- INTERLOCUTION  tolkw- INTERLOPE klou- INTERLUDE leid- INTERMEDIATE medhyo- INTERMIT (S)meit(a)- INTERNAL en INTERNECINE nek-1 INTERPELLATE pel-6 INTERPOSE apo- INTERPRET per-68 INTERREX reg-1 INTERROGATE reg-1 INTERRUPT reup- INTERSECT sek- INTERSPERSE (s)preg- INTERSTICE sta- INTERVAL walso- INTERVENE gWa- INTERVIEW weid- INTESTINE en INTIMA en INTIMATE? en INTINCTION  teng- INTINE en
1839:MEAN3 = medhyo- MEASLES smé- MEASURE mé-2
1841:MEATUS mei-1 MECHANIC magh-1 MECHANISM magh-! MECHANO- magh-! MECONIUM mak-1 MECOPTERAN miak-, pet- MEDDLE meik- MEDIAL medhyo- MEDIAN medhyo- MEDIASTINUM medhyo- MEDIATE medhyo- MEDICAL med- MEDICATE med- MEDICINE med- MEDICO med- MEDIEVAL alw-, medhyo- MEDIOCRE medhyo- MEDITATE med- MEDITERRANEAN medhyo-, ters- MEDIUM medhyo- MEDLEY meik- MEDULLA (s)mer-3 MEED mizdho-
1850:MERGE mezg-! MERIDIAN delw-, medhyo- MERISTEM (s)mer-2 MERIT (s)mer-2
1855:MESO- medhyo- MESOGLEA gel-1 MESONEPHROS negWh-ro- MESOTHELIUM dhée(i)- MESS (s)meit(@)- MESSAGE (s)meit(@)- MESTIZO meik-
1869:MICROPYLE pulé MICTURATE meigh- MID! medhyo- MIDDLE medhyo- MipcaRD medhyo- MIDGE mu-2 MIDRIFF krep- MIDWIFE me-2 MIGHT! magh-! MIGRAINE ker-1 MIGRATE mei-1 MIL! gheslo-
```


## [2026-09-07T15:58:05.926Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n 'MAHARAJAH\\|MAHATMA\\|MAHARANI' AHD_watkins1985.txt | head\necho \"---- context after Sanskrit maha- ----\"\nsed -n '733,736p' AHD_watkins1985.txt | head -c 1500"
}
```


### [2026-09-07T15:58:05.986Z] TOOL RESULT

```
465:@tmen-. Breath. Sanskrit diman, breath, soul: ATMAN; MAHATMA. [Pok. ét-men- 345.]
734:mahat-, great: MAHARAJAH, MAHARANI, MAHARISHI, MAHATMA, MAHAYANA, MAHOUT. [Pok. meg(h)- 708.] mei-'. To change, go, move; with derivatives referring to the exchange of goods and services within a society as regulated by custom or law. 1. Latin medre, to go, pass: MEATUS; CONGE, IRREMEABLE, PERMEATE. 2. Suffixed o-grade form *moi-t- in: a. Germanic *ga-maid-az (*ga-, intensive prefix; see kom), “changed (for the worse),” abnormal, in Old English gemdd, insane: MAD; b. Latin mitdre, to change: MEW!, MOLT, MUTATE; COMMUTE, PERMUTE, REMUDA, TRANSMUTE; C. Latin miituus, “done in exchange,” borrowed, reciprocal, mutual: MUTUAL. 3. Suffixed extended zero-grade form *mit-to- in Ger- manic “missa-, “in a changed manner,” abnormally, wrongly, in: a. Old English mis-, mis-: Mis-!; b. Old Norse mis(s), mis(s)-, miss, mis-: AMISS, MISTAKE; C. Ger- manic *missjan, to go wrong, in Old English missan, to miss: MISs!, 4, Suffixed o-grade form *moi-n- in com- pound adjective *ko-moin-i-, “held in common” (*ko-, together; see kom), in: a. Germanic *gamainiz in Old English geméne, common, public, general: MEAN?; (DE- MEAN?); b. Latin commiinis, common, public, general: COMMON, COMMUNE, COMMUNICATE, (COMMUNISM). 5. Suffixed o-grade form *moi-nes- in: a. Latin minus, “service performed for the community,” duty, work, “public spectacle paid for by a magistrate,” gift: MUNICI- PAL, MUNIFICENT, REMUNERATE; b. Latin immiinis (in-, negative prefix; see ne), exempt from public service: IMMUNE. 6. Extended form *()meigv- in: a. Greek amei- bein, to change: AMOEBA; b. Latin migrdre, to change one’s place of living: MIGRATE; EMIGRATE. [Pok. 2. mei-, 3. mei- 710, meig¥- 713, 2. meit(h)- 715.] mei-2. Small. 1. Greek meidn, less, lesser: MEIOSIS; MIo- CENE. 2. Latin nimis, too much, very (< *ne-mi-s, “not little’; ne-, negative prefix; see ne). 3. Suffixed zero-grade form *mi-nu- in: a. Latin minuere, to reduce, diminish: MENU, (MINCE), MINUEND, MINUTE2; COMMI- NUTE, DIMINISH; b. Latin minor (influenced by the comparative suffix -or), less, lesser, smaller: MINOR, MINUS, MIS-!; MINUSCULE; GC. further suffixed (superla- tive) form *minu-mo- in Latin minimus, least: MINIMUM; d. Latin minister, an inferior, servant (formed after magister, master; see meg-): MINESTRONE, MINISTER, MINISTRY, MYSTERY?; @. Russian men’she, less: MENSHE- vik. [Pok. 5. mei- 711.] mei-3, To fix; to build fences or fortifications. 1. Suffixed o-grade form *moi-ro- in: a. Germanic *mair-ja- in Old English mére, boundary, border, landmark: MERE®; b. Latin miirus, wall: MURAL, MURAMIC ACID, MURE; IMMURE. 2. Suffixed o-grade form *moi-ni- in Latin miinire, to fortify, protect, strengthen: MUNITION; (AM- MUNITION), PRAEMUNIRE, PREMUNITION. 3. Possibly suffixed lengthened-grade form *méi-t- in Latin méta, boundary stone, limit: METE?. [Pok. 1. mei- 709.] mei-4, To tie. 1. Suffixed zero-grade form *mi-tro-, “con- tract, that which binds,” in: a. Greek mitra, headband, earilier a piece of armor worn around the waist: MITER; b. Old Persian Mithra-, name of a god (< “contract” < “bond”): MiTHRAS; c. Russian mir, commune, joy, peace (possibly borrowed from Iranian): mR. 2. Possibly a suffixed zero-grade form *mi-to- in Greek mitos, a warp thread: MITOSIS; DIMITY, MITOCHONDRION, SAMITE. [Pok. 4. mei- 710.] méGi-. Mild. Contracted from *meoi-. Suffixed zero-grade form *mi-ti- (< *mis-ti-) in Latin mitis, soft: MITIGATE. [Pok. 7. mei- 711.] meigh-. To urinate, 1. Germanic suffixed form *mih-stu-, urine, hence mist, fine rain, in: a. Old English mist, mist: MIST; b. Middle Dutch mieselen, to drizzle, perhaps akin to the source of Middle English misellen, to drizzle: MIZZLE; Cc. Germanic diminutive form *mihst-ila-, mistle- toe (which is propagated through the droppings of the missel thrush), in Old English mistel, mistletoe: (MISSEL THRUSH), MISTLETOE. 2. Suffixed form *migh-tu- in
893:culdre, to rake, in Provengal rasclar (> French racler), to rake, scrape: RACLETTE. [Pok. 2. réd- 854.] reg-'. To move in a straight line, with derivatives mean- ing “to direct in a straight line, lead, rule.” I. Basic form *reg-. 1. Suffixed form *reg-to- in Germanic *rehtaz in Old English riht, right, just, correct, straight: RIGHT. 2. Latin regere, to lead straight, guide, rule (past partici- ple réctus, hence adjective réctus, right, straight): REALM, RECTITUDE, RECTO, RECTOR, RECTUM, REGENT, REGIME, REGIMENT, REGION; CORRECT, DIRECT, ERECT, RECTANGLE, RECTIFY, RECTILINEAR, RISORGIMENTO, SURGE. 3. Greek oregein (with prothetic vowel from oldest root form *sreg-), to stretch out, reach out for: ANORECTIC, ANOREXIA. II. Lengthened-grade form *rég-, Indo-European word for a tribal king. 1. Celtic suffixed form *rig-yo- in Germanic *rikja- in: a. Old English rice, realm: BISHOPRIC; b. Old Norse riki (> Norwegian rik), realm: RIKSMAL; c. Old English rice, strong, powerful: RICH. 2. Latin réx, king (royal and priestly title): REAL, REGAL, REGULUS, REIGN, ROYAL; INTERREX, REGICIDE, REGIUS PROFESSOR, VICEREINE, VICEROY. 3. Suffixed form *rég-en- in Sanskrit raja, rdjan-, king, rajah (femi- nine rdjni, queen, rani), and rdjati, he rules: RAJ, RAJAH, (RANI), (RYE2); MAHARAJAH, MAHARANTI. III. Suffixed lengthened-grade form *rég-old in Latin régula, straight piece of wood, rod: RAIL!, REGLET, REGULAR, REGULATE, RULE, IV. O-grade form *rog-. 1. Germanic *rak6 in Old English raca, racu, rake (implement with straight pieces of wood): RAKE!, 2,Germanic *rak- in Middle Dutch rakke, framework: RACK}, 3. Possibly Germanic *rankaz (with nasal infix) in Old English ranc, straight, strong, hence haughty, overbearing: RANK?. 4, Germanic *rak- inaz, ready, straightforward, in Old English gerecenian, to arrange in order, recount (ge-, collective prefix; see kom): RECKON. 5. Suffixed form *rog-d- in Latin rogdare, to ask (< “stretch out the hand”): ROGATION, ROGATORY; ABROGATE, ARROGATE, CORVEE, DEROGATE, INTERRO- GATE, PREROGATIVE, PROROGUE, SUBROGATE, SUPERER- ocaTE. 6. Suffixed form *rog-o- in a possible Latin noun *rogus, “extension, direction,” perhaps in a Latin phrase *é rogd, “from the direction of” (€ < ex, out of; see eghs), contracted into ergd, therefore, in consequence of: ARGAL, ERGO. V. Lengthened o-grade form *rég-. 1. Ger- manic *rdkjan in Old English rec(c)an, to pay attention to, take care (formally influenced by Old English reccan, to extend, stretch out, from Germanic *rakjan): RECK. 2. Germanic *rdékja- in Old English receléas, careless (-léas, lacking; see leu-1):; RECKLESS. [Pok. 1. reg- 854.] reg-2. Moist. 1. Suffixed variant form *rek-no- in Ger- manic *regnaz, rain, in Old English reg(e)n, rén, rain: RAIN; RAINBOW. 2. Possibly Latin rigdre, to wet, water: IRRIGATE. [Pok. 2. reg- 857.] reg-3. To dye. Lengthened-grade form *rég-. 1. Suffixed form *rég-és- in Greek rhégos, blanket, rug: REGOLITH. 2. Sanskrit rdgah, color, red: RAGA. 3. Perhaps Sanskrit raékshd, earlier form of lékshd, red dye: Lac}. [Pok. 1. reg- 854.] regv-es-. Darkness. Oldest root form *areg’-es-. Greek Erebos (with prothetic vowel), Erebus, a place of dark- ness under the earth: EREBUS. [Pok. regt-os- 857.] rei-1, To scratch, tear, cut. I. Extended form ‘reik-. 1. Germanic *rigon- in Italian riga, line (< “something cut out’’): RIGATONI. 2. Suffixed form *rei-md or *reig-sma in Latin rima, crack, cleft, fissure: RIMOSE. 3. Suffixed o-grade form *roik-wo- in Germanic *rai(h)-wa- in Old English raw, réw, a line, row: ROW!. II. Possible extended form *reipp-. Germanic *raipaz, rope, in: a. Old English rap, rope: ROPE; b. compound *stig-raipaz, “‘mount-rope,” in Old English stigrap, stirrup (see steigh-). III. Extended form *reip-. 1. Ger- manic *rifan, in Old Norse rifa, to tear: RIVE. 2. Zero-grade form *rip- in: a. Germanic *77fti- in Danish rift, breach, akin to the Scandinavian source of Middle English rift, rift: R1FT!; b. Germanic *rif- in Old English
1794:MAGUS magh-! MAHARAJAH meg-, reg-! MAHARANI meg-, reg-! MAHARISHI meg- MAHATMA ��tmen-, meg- MAHAYANA ei-1, meg- MAHOUT meg-, mé-2 Mata ma-2
---- context after Sanskrit maha- ----
mei-'
mahat-, great: MAHARAJAH, MAHARANI, MAHARISHI, MAHATMA, MAHAYANA, MAHOUT. [Pok. meg(h)- 708.] mei-'. To change, go, move; with derivatives referring to the exchange of goods and services within a society as regulated by custom or law. 1. Latin medre, to go, pass: MEATUS; CONGE, IRREMEABLE, PERMEATE. 2. Suffixed o-grade form *moi-t- in: a. Germanic *ga-maid-az (*ga-, intensive prefix; see kom), “changed (for the worse),” abnormal, in Old English gemdd, insane: MAD; b. Latin mitdre, to change: MEW!, MOLT, MUTATE; COMMUTE, PERMUTE, REMUDA, TRANSMUTE; C. Latin miituus, “done in exchange,” borrowed, reciprocal, mutual: MUTUAL. 3. Suffixed extended zero-grade form *mit-to- in Ger- manic “missa-, “in a changed manner,” abnormally, wrongly, in: a. Old English mis-, mis-: Mis-!; b. Old Norse mis(s), mis(s)-, miss, mis-: AMISS, MISTAKE; C. Ger- manic *missjan, to go wrong, in Old English missan, to miss: MISs!, 4, Suffixed o-grade form *moi-n- in com- pound adjective *ko-moin-i-, “held in common” (*ko-, together; see kom), in: a. Germanic *gamainiz in Old English geméne, common, public, general: MEAN?; (DE- MEAN?); b. Latin commiinis, common, public, general: COMMON, COMMUNE, COMMUNICATE, (COMMUNISM). 5. Suffixed o-grade form *moi-nes- in: a. Latin minus, “service performed for the community,” duty, work, “public spectacle paid for by a magistrate,” gift: MUNICI- PAL, MUNIFICENT, REMUNERATE; b. Latin immiinis (in-, negative prefix; see ne), exempt from
```


## [2026-09-07T15:58:20.498Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SKT ===\"; grep -n '^MIDDLE\\|^MID,\\|^MUCH\\|^MORE\\|^MEGA\\|^MAXIM\\|^MASTER\\|^MEAN,\\|^MEDIUM\\|^OMEGA' SKT.txt | head -20\necho \"=== HJB maharaja ===\"; grep -n -i '^MAHARAJ\\|^MAHATMA' HJB.txt | head\necho \"=== AID maharaja ===\"; grep -n -i 'Maharaja\\|Mahatma' AID.txt | head -5\necho \"=== WLD band3 medhio / meg ===\"; grep -n 'medhio\\|meĝ\\|meg̑' WLD_band3.txt | head"
}
```


### [2026-09-07T15:58:20.596Z] TOOL RESULT

```
=== SKT ===
11669:MID,   occnrring    in    A.  S.
=== HJB maharaja ===
=== AID maharaja ===
=== WLD band3 medhio / meg ===
3103:(junger) = merjo- 231%. 2. sem- ASS*, | “oy 440%, Mantel wy- 48*, | mittenin, hinein 2. me- 290" | nachatellen 1. de- 808. Marder 13. %er- 287. mittiherer medhio- SH1* | nachesnchen 3. reu- 350".
```


## [2026-09-07T15:58:26.876Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD\nawk 'BEGIN{RS=\"\\f\"} NR==266' WLD_Bd2_pages.txt | head -40"
}
```


### [2026-09-07T15:58:28.257Z] TOOL RESULT

```
                                               medhu — membh- uiid uiemb-V                         261

in6dhu n, „Honig; bes. Meti'S im Germ. u. BsL masc. geworden.
  Ai. mddlm „Honig, Met'^ (davon mddhu- ,,su6''; madh(u)v-dd- ,,Honig-
€sser“; aksl. medv-ldh „Bar“);
     av. madit „Beerenwein'''; tochar. B.                          ,;Honig^‘   ;
                                                                                   gr.   „Wein“ (aus
„Rau8chtranlv          ‘
                           ;
                               die Bed. „Honig‘' bat sich aui i^ieXt zuriickgezogen)        :
                                                                                                ^ledvoy
„bin trunken“; jAE'dvoKCo „mache trunken“.
   air. mid (gen. medd), cymr. medd, acorn. (Blur.?) medu^ bret.      „Met‘',
cymr. meddiv „berauscht“, bret. me^o ds., me^vi „berauschen“ (parallel gr.
jue^vco), ir. mesc ^berauschend, beraascht^, mesce „Trunkeiibeit“ (ohne ge-
schicbtlichen Zshang mit gr. /is&vgxco);
   aisL mjqdr, ags. meodo, ahd. mefzi ,Met“:                 5


   lit. medus „Honig'‘ {midiis „Met^' aus got. ^midus, Trautmann Germ. Ltg.

50), lett. medus „Honig, Met'S apr. meddo i^medu) „Honig^^; abg. medo, -?£
und -a „Honig'' (dazu u. a, skr. o-mediti se „verderben, z. B. von Fett“,
eigentlich „su61ich, fade werden oder vergahren“, BernekerII31 gegen
Bezzenberger bei Pick II ^ 207, Ublenbeck Ai. Wb. 212).
   Z. B. Curtius^ 279f., Pick I * 105, 281, 512, II ^ 207, III ^ 306.
   Zur Konkurrenz mit *melil „Honig“ (nie „Honigmet‘') und iiber finn.-
ugr. Vergleichung s. Gauthiot Msl. 16, 268 ff., Schrader RL. 85, ^ 139,

medhio- „raittlerer‘\
     Ai. madht/a-, av. maidya- „mittlereB*, Sup.                      ai.   madJiyama-, av. madoma-
,,mittlerer“ (vgl. u. das                      Germ.);
   arm. mej „Mitte'‘ (Hubschmann Arm. Gr. I 474); gr. (ep.) j^ieoGog, (att.)
jueGog,  lat. 7nedkis, osk. rnefiai ,,in media“, gr. ^£6a(a)dT//b == lat. medietas:

gall. Medio-lanum, -matrici, air. mid- in Zs. „medius^', mir. mide „Mitte‘‘,
Mide eigentlich „mittlere Provinz^', air. immedon ,,in medio'‘, cymr. meicn
„in*' {'^medug7io-, s. Pedersen KG. I 112); osk. messimas vermutlich „me-

dioximas"' (s. zuletzt Brugmann IP 1, 229) und mit Verschleppung des                                  .s
```


## [2026-09-07T15:58:33.398Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD\nawk 'BEGIN{RS=\"\\f\"} NR==262' WLD_Bd2_pages.txt | head -45"
}
```


### [2026-09-07T15:58:34.874Z] TOOL RESULT

```
                                                                                                 257

nieg(h)- „groB“ (Gutt.-Yerb. wie bei g(Ji)enus, eg{h)om, ghe gho); meg^ ‘rng-.
     Ai. mahdnU.         av. mazant-         „gro6“,    ai.    mah-^ av. maz-   ds, (nur aufierhalb
des n. a.),   maJii n. sg. (pi. du.) neutr. (Beurteilung des -i strittig: idg.
                 ai.

A nach J. Schmidt PI. 238, 247, Bnigmann II^ 1, 175; -d z. B. nach Wacker-
nagel Ai. Gr. II 1, 58, dann Yielleicht= gr.                           das freilich von J. Schmidt
PL 247 = ai. neutr. rnahcit, idg. *meg(7i)nt gesetzt wird, auch ^m€g(Ji)n sein
konnte nach Brugmann MU. II 175 zw. Osthoflf MU. YI 215, noch anders,
^megds u. zu aisl. mjqk), als 1. Zsglied ai. mahCi-^ av. (mit sehr auffalliger
Nasalierung) mqza- (s. Bartholomae BB. 10, 273, IF. 1, 303, Wackernagel
aaO.).   Komp. Sup. ai. maluyas-^ maJiistha-^ av. mazyah-^ mazlMa-\
  ai. maJias-^ av. mazah- n. „Gro6e“, ai. majmdn- „Gr56e‘', av. mazan-

,,Gro6e,        Erhabenheit‘‘         (s. Bartholomae Wb. tl56f.),           ai. ma/i7   „die groBe,
alte, die Erde‘‘         (:   iat.   Maia)\
     adv. gthav. mas „sehr“ {^meghs\ schwundstufig jav. as „sehr“ (Yerhalt-
nis wie ysya: dya- j.sehF'; Bartholomae IF. 9, 282 f., airan. Wb. 1164).
  Da6 das a der ar. Worte n sei (Bartholomae IF. 1, 303, vgl. auch Peder-
sen IF. 2, 329), ist trotz av. mqza unwahrscheinlich. Femzuhalten sind,
obwohl von „augere"' zu „verherrlichen, feiern“ zu gelangen ware, ai. ma-
hdyatl „erfreut, ergotzt, verehrt^', maJid- m. „Feier, Fest, Opfer (nicht nach
Uhlenbeck Ai. Wb. 220 mind. = makhd-^ woriiber s. "^maqJio- „ausgelassen“),
mahtyate „freut sich,            ist selig“,     da sie wegen av. mimayzo „du sollst feiern“
(desiderativ, eigentlich „zu verherrlichen suchen'^) nichtpalatale                        Med.   asp.
enthalten (Bartholomae Airan. Wb. 1135, Giintert IF. 30, 9 if.; nicht iiber-
zeugend trennt Scheftelowitz ZdMG. 59, 700 ai. maJidyati, das zu mali-
„gro6'‘ gehore,          von mimnyzo^ das er nebst lit. mcgti ,,wmhlgefallen“ zu ai.
mangala-m „Gluck“ stellt, das aber mit av, -yz- unvereinbar ist und zu
mang- „kunstlerisch verschonern^' geh5rt), s. megJi- „wohlgesinnt^';
   tochar. B main- „vieP (Levi-Meillet Joum. as. 1912, I 114);
   arm. mec „groB‘' (Hiibschmann Arm. St. I 42, Arm. Gr. I 473) mecarem
,.halte hoch“ (: gr. yeyaigo^^ Brugmann IP 1, 356);

     Gr. jneyagf       yeydlgy       fxb/a   „gro6*''   (zur   formellen Beurteilung von gey a,
wozu fxeyag^ -av neugebildet ist, s. o. und die Lit. bei Boisacq s. v., wozu
noch Brugmann II^ 2, 656; auch das fieydko- der Kasus obi. und des Fern,
ist aus dem Notstand erwachsen, zu ixeya diese Kasus zu bilden, wobei

ydayakog „niedrig“ als begriJfflicher Gegensatz zu „groB'^ das Yorbild ab-
gab, nur da6 die Anfangsbetonung von y,eya zu '’^fieyaXo- fiihrte; die for-
mantische Ahnlichkeit mit got. usw. mikils scheint mir daher gegen Brug-
mann II ^ 1, 361 f., Osthoff MU. YI 215 triigerisch, zumal urgerm. mikilaz
```


## [2026-09-07T15:58:54.142Z] TOOL CALL #49: WebFetch

```json
{
 "url": "https://vajehyab.com/?q=%D9%85%D9%87%D8%A7%D8%B1%D8%A7%D8%AC%D9%87&d=moein",
 "prompt": "Give the Mo'in (فرهنگ معین) entry text for مهاراجه verbatim, including any origin tag in brackets."
}
```


## [2026-09-07T15:58:55.661Z] TOOL CALL #50: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/more",
 "prompt": "Give the full etymology of \"more\" — Old English form, Proto-Germanic, and the PIE root it is assigned to. Does it come from PIE *meg- 'great' or a different root?"
}
```


### [2026-09-07T15:58:56.993Z] TOOL RESULT

```
Based on the content provided, the Mo'in dictionary entry for مهاراجه is:

"(مَ جِ) [ سنس . ] (ص .) توانگر، ثروتمند."

This entry includes the pronunciation guide, origin tag [سنس.] (Sanskrit), part of speech marker (ص.), and definitions meaning "wealthy" or "rich person."
```


### [2026-09-07T15:59:01.550Z] TOOL RESULT

```
# Etymology of "More"

According to the Online Etymology Dictionary, the word "more" has the following etymological path:

**Old English form:** *mara* ("greater, relatively greater, more, stronger, mightier"), used as a comparative of *micel* "great"

**Proto-Germanic:** *\*maiz* (appearing in Old Saxon *mera*, Old Norse *meiri*, Old Frisian *mara*, Middle Dutch *mere*, Old High German *meriro*, and German *mehr*)

**PIE root:** *\*meis-*, "perhaps from a root *\*me-* 'big'"

The source document also notes that the PIE root *\*meis-* appears in cognates like Avestan *mazja* "greater," Old Irish *mor* "great," Welsh *mawr* "great," and Greek *-moros* "great."

**Important distinction:** The etymology does NOT connect "more" to PIE *\*meg-* 'great.' Instead, it traces to the separate PIE root *\*meis-*, though both roots relate to the concept of size or magnitude. The dictionary explicitly links *mickle* (a related word) to *\*meg-*, maintaining a distinction between these two etymological paths.
```


## [2026-09-07T15:59:12.031Z] TOOL CALL #51: WebFetch

```json
{
 "url": "https://vajehyab.com/?q=%D9%85%D8%AF%DB%8C%D8%AA%D8%B1%D8%A7%D9%86%D9%87&d=moein",
 "prompt": "Give the Mo'in (فرهنگ معین) entry for مدیترانه verbatim, with any bracketed origin tag such as [فر.] or [فه.]."
}
```


## [2026-09-07T15:59:13.701Z] TOOL CALL #52: WebFetch

```json
{
 "url": "https://vajehyab.com/?q=%D9%85%D8%A7%DA%A9%D8%B3%DB%8C%D9%85%D9%85&d=moein",
 "prompt": "Give the Mo'in (فرهنگ معین) entry for ماکسیمم verbatim, with any bracketed origin tag such as [فر.]."
}
```


### [2026-09-07T15:59:15.621Z] TOOL RESULT

```
Based on the web page content provided, there is no Mo'in (فرهنگ معین) entry available for the word "مدیترانه" (Mditraneh/Mediterranean). 

The page displays: "«مدیترانه» پیدا نشد!" which means the word was not found in the dictionary. The site offers suggestions to try alternative search methods or propose a definition for this term.
```


### [2026-09-07T15:59:16.829Z] TOOL RESULT

```
According to the Mo'in dictionary entry shown on this page, the verbatim definition is:

"(مُ) [فر.] (اِ.) = ماکزیمم : حداکثر، بیشترین حد، بزرگترین مقدار در مجموعه ای از مقادیر، بیشینه (فره )."

This indicates the word means "maximum" or "the greatest amount in a set of values."
```


## [2026-09-07T15:59:25.418Z] TOOL CALL #53: WebFetch

```json
{
 "url": "https://vajehyab.com/?q=%D9%85%D8%AF%DB%8C%D9%88%D9%85&d=moein",
 "prompt": "Give the Mo'in (فرهنگ معین) entry for مدیوم verbatim, with any bracketed origin tag such as [فر.] or [انگ.]."
}
```


## [2026-09-07T15:59:26.566Z] TOOL CALL #54: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/Mediterranean",
 "prompt": "Give the etymology of Mediterranean: Latin form, components, and dates of first English use."
}
```


### [2026-09-07T15:59:28.770Z] TOOL RESULT

```
According to the Mo'in dictionary entry shown on this page, the verbatim definition is:

"(مِ یُ) [ فر. ] (اِ.) واسطه ، شخصی که واسطة احضار ارواح شود."

This entry indicates the word is of French origin [فر.] and defines it as a intermediary or person who serves as a medium for summoning spirits.
```


### [2026-09-07T15:59:31.329Z] TOOL RESULT

```
# Etymology of Mediterranean

**Latin Form:** Late Latin *Mediterraneum mare* (7th century), from Latin *mediterraneus* meaning "midland, surrounded by land"

**Components:**
- *Medius* (middle) + *terra* (land/earth)
- Both elements derive from Proto-Indo-European roots: *medhyo-* (middle) and *ters-* (to dry)

**First English Use:** The term appeared in the 1590s, though an earlier variant *Mediterranie* existed around 1400.

**Historical Note:** Before the Latin-derived term, Old English speakers called this body of water *Wendel-sæ*, named after the Vandals, a Germanic tribe that settled on its southwestern coast following Rome's fall.
```


## [2026-09-07T15:59:42.782Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n 'mai&yqna\\|maiöyqna\\|maiSyqna\\|maidyqna\\|maiSyana' BRT.txt | head\necho \"=== search 'Mitte' in BRT near maidy ===\"\ngrep -n \"maii\\?wyana\\|mai%yqna\" BRT.txt | head\ngrep -n 'j\\. maiöy\\|maiSy' BRT.txt | head"
}
```


### [2026-09-07T15:59:42.857Z] TOOL RESULT

```
=== search 'Mitte' in BRT near maidy ===
19624:maiSy ana-  1 1 1 6
19633:•  j.  'maiSya-  n.  'geistiges,  alkoholisches Getränk':  yni  .  .  'lyanqm  parB  x^aniBü *gäiä  noit  *iräfayänH  "die  . .  in  Folge des  Genusses  geistiger  Getränke  die  G.s nicht  aufsagen"  N.  2p,  [Y.  JO,  8:  lies maohahs^
19638:•  j.  maiJtyäna-,  maiSyi^ia-  n.  'Mitte'; a)  des  Leibes,   a)  des  Menschen:  /ra^a
19641:maiSyairya-
19644:•  j.  maiSyÜrya-  m.  Name  der  Gottheit der  fünften  J^eszeit  und  des  an  deren Ende  gefeierten  fünftägigen  Fests*'  (mit dem  letzten,  80.  als  Haupttag):  yiinm sar^tm  aSavamm  asahe  ratüm  "den  kälte- bringenden  M.  .  ."  Vr.  2.  2;  Y.  2.  9;  — 'ryehe  sariaahe  Vr.  J.  a;  A.^.  3;  —  'ryäi Y.  J,  9;  — Jiuxtaheca  na  myasdahe  a^äiti (sd.)  . .  yat  'ryehe  A,^.  11;  —  altaitlm 'ryehe  da%usS  v»n%ra-^nake  "80  [Tage sinds  bis  zum  (Hauptjtagl  des  M.  [im Monat]  des  Schöpfers  [am  Tage]  des  V." A.J.  II.
19647:•  j.  maiSyöi  Adv.:  s.  'mathya-, KompA.   —    S.  auch  maüyäirya-.  —  Vgl.  ai, madkyf,
19661:I)  NA.  auch  '5iz: ■  j.  maiSyöi-äam-')  m.  Name  der  Gott- heit der  zweiten  Jahreszeit  und  des  an deren  Ende  gefeierten  fünftägigen  Fests*' (mit  dem  letzten,  60.  als  Haupttag):  "Imtim vSstrSMätainlm  (sd.)  asavanim  asahe  ratüm Vr.  2.  3;  Y.  2. 9;  —  'make  V3strd4a(ainyeh4 Vr.i.3;  A.j.3i  —  'ümäi'^  Y./.9;  — bityeht^a  nä  myaxdahe  (^äiti  (sd.)  . .  yat s'fmahe'^  A._j.  8;  —  xivaltim  's>mahe'''> tistryeke  dai:u^S  "60  [Tage  sinds  bis  zum (Haupt)tag]  des  M.  [tm  Monat]  des  Tiitrya [am  Tag]  des  Schöpfers"  A.  j.  8.
19669:•  j.  maiSyoi-äad-  Adj.  (auch  fem.)  'in der  Mitte'*  siUend':  vlhäjpahe  . .  yJS  klm (näml.  tiaenam)  . .  utvaiat . .  nJ  him  dasta •iä%?m{K%V)  YtTj.ioo.'
25759:•  j.  urvizö.maiSya-  Adj.  (fem.  'ya^  'die Leibesmitte,  Taille  schnUrend,  mit  ge- schnürter Taille"':  kaininS  . .  yä  (NPf.) traotanvB  Yt  ij.  1 1.
```


## [2026-09-07T15:59:48.666Z] TOOL CALL #56: Bash

```json
{
 "command": "ls site/pages/325.jpg 2>/dev/null || pdftoppm -f 325 -l 325 -r 200 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg325 && echo done"
}
```


### [2026-09-07T15:59:49.941Z] TOOL RESULT

```
site/pages/325.jpg
done
```


## [2026-09-07T15:59:52.812Z] TOOL CALL #57: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/site/pages/325.jpg"
}
```


### [2026-09-07T15:59:52.834Z] TOOL RESULT

```

```


## [2026-09-07T16:00:20.589Z] TOOL CALL #58: Bash

```json
{
 "command": "sed -n '1,200p' tools/verify_check.py"
}
```


### [2026-09-07T16:00:20.630Z] TOOL RESULT

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


## [2026-09-07T16:00:47.215Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KNT maθišta ===\"; grep -n 'ma.ista-\\|maθišta\\|mathista' KNT.txt | head\necho \"=== HJB ===\"; grep -n -i 'maharaja\\|maha raja\\|Maha-raja' HJB.txt | head -5\necho \"=== AID ===\"; grep -n -i 'maharaj' AID.txt | head -5\necho \"=== KLN maharajah ===\"; grep -n -i '^maharajah\\|^maharaja' KLN_1966.txt | head -3\necho \"=== KLN omega/immediate/medium/Mediterranean ===\"; grep -n '^immediate,\\|^medium,\\|^Mediterranean' KLN_1966.txt | head"
}
```


### [2026-09-07T16:00:47.325Z] TOOL RESULT

```
=== KNT maθišta ===
1150:injures’, Lt. nocet, Skt. ndsdyalt. pIE *mak- in OP тойа ‘greatest’, Av. masista-
2248:Superl. nsm. ma£isla ‘greatest’, asm. тай ат, with -isto-; cf. Av. masista-, Gk. Dor. дйкитто to px pos.
5761:mabista- adj. ‘greatest’, equal to ‘crown prince’ in XPf (Speiser ap. Kent, Lg. 9.40-1; Hz. Apl 254-8): Av. masista-, NPers. mähist, Gk. ppxio ros ‘longest’ (radical vowel after that in anxos Jength"); superl. to pIE *mak-ros, Gk. накр, Lt. macer ‘thin’, pLE root *mak- (887) ‘be long and slender’ + superl.,suffix.<ste-) (S117, $156.11,
=== HJB ===
4406:[1875.— "  Bandflqis,  or  orderlies  of  the Maharaja,  carrying  long  guns  in  a  loose  red cloth  cover." — Drew,  Jummoo  and  Kashmir, 74.]
7891:c.  943.— '*  The  territories  of  this  Prince Qhe  Maharaja  of  the  Isles)  produce  all  sorts of  spices  and  aromatics.  .  .  .  The  exports are  camphor,  lign-aloee,  clove,  sandal-wood, betel-nut,  nutmeg,  caraamom,  onbeb  (al- koMbah).  .  .  ."—Ma^adt,  i.  841  teq.
8367:1888.— "The  Maharajah  sent  us  in  the evening  a  new  set  of  dandng  giris,  as  they were  called,  though  they  turned  out  to  he twelve  of  the  ugliest  old  women  I  ever  saw." — Otbome,  Court  and  Camp  of  Runjeel  Singh, 164.
8792:1808. — "A  remarkable  circumstance  took place  yesterday.  Some  Sirdars  put  the Maharaja  (Sindia)  in  dhuma.  He  was angry,  and  threatened  to  put  them  to  death. Bhugwunt  Ras  Byse,  their  head,  said,  'Sit still;  put  us  to  death.'  Sindia  was  enraged, and  ordered  him  to  be  paid  and  driven  from camp.  He  refused  to  go.  .  .  .  The  bazaars were  shut  the  whole  day  ;  troops  were  posted to  ffuard  them  and  defend  the  tents.  .  .  . At  last  the  mutineers  marched  off,  and  all was  settled." — JBlpfunstoiu**  Diary,  in  Lift, i.  179  seq.
10865:of  several  ancient  Hindu  dynasties, and  from  the  time  of  the  early Mahommedan  sovereLps  of  Delhi down  to  the  reign  of  Aurangzib  it was  used  as  a  state-prison.  Early  in the  18th  century  it  fell  into  the  posses- sion of  the  Manratta  family  of  Smdhia, whose  residence  was  estab&shed  to  the south  of  the  fortress,  in  what  was ori^nally  a  camp,  but  has  lon^  been a  city  known  by  the  original  title  of Lcuhkar  (camp).  The  older  city  lies below  the  northern  foot  of  the  rock. Gwalior  has  been  three  times  taken  by British  arms :  (1)  escaladed  by  a  force under  the  command  of  Major  Popham in  1780,  a  very  daring  feat  ;*  (2)  by  a regular  attack  under  Gen.  White  in 1805  ;  (3)  most  gaUantly  in  June  1858, by  a  party  of  9ie  25th  Bombay  N.  I. under  Lieutenants  Rose  and  Waller, in  which  the  former  officer  fell.  After the  two  first  captures  the  fortress  was restored  to  the  Sindhia  family.  From 1858  it  was  retained  in  our  hands,  but in  December  1885  it  was  formally  re- stored to  the  Maharaja  Sindhia.
=== AID ===
6610:virji  MahArAj  and  Ayodya  PrasAdji MahArAj,  his  successors,  the  one  to preside  at  WadtAl  in  Kaira,  and  the other  at  Ahmedabad.
=== KLN maharajah ===
22511:maharaja
22566:maharaja,  maharajah,  n.,  the  title  of  great  Hindu princes.  —  OI.  maharajah,  ‘a  great  king’,  com¬ pounded  of  maha-,  ‘great',  and  rdjan,  ‘king’.  See magnum  and  rajah  and  cp.  Maratha  and  the  first element  in  Mahabharata,  maharanee,  mahatma, mahout.
=== KLN omega/immediate/medium/Mediterranean ===
18792:immediate,  adj.  —  ML.  immediatus,  fr.  in-,  ‘not’, and  Late  L.  mediatus,  pp.  of  mediare,  ‘to  divide in  the  middle,  to  halve’.  See  mediate,  v.,  and  cp. intermediate.
```


## [2026-09-07T16:01:04.612Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT\necho \"=== میان headword ===\"; grep -n 'میان *-\\|مِیان\\|میان -' BQT_v4_pages.txt | head -10\necho \"=== مهاراجه ===\"; grep -n 'مهاراجه' BQT_v4_pages.txt | head -3\necho \"=== مدیترانه / مدیوم / ماکسیمم ===\"; grep -n 'مدیترانه\\|مدیوم\\|ماکسیمم' BQT_v4_pages.txt BQT_v3_pages.txt | head -5\necho \"=== مهست ===\"; grep -n 'مهست' BQT_v4_pages.txt | head -5"
}
```


### [2026-09-07T16:01:04.710Z] TOOL RESULT

```
=== میان headword ===
12455:نام ماه هفتم است ازسال رومیان - وبارانآ نوقت یسته ۴ - بکراولوسکون ثانی‌وناك
=== مهاراجه ===
5658:‏2 مهاراجه- رك : مهراج .
5805:۴ <د مهاراجه > سانسکریت ۳4[8 - ۸18۵۵ (شاه بز رکه . سلطان عظیم) «وبليامز
=== مدیترانه / مدیوم / ماکسیمم ===
=== مهست ===
1105:میگوشد؛ وبحذف مانی‌هم آمده است که ملیطرنا مامهستان « بفتح ثالك ‏ و کسرهایروزن
2571:مرداد مهست سخت خرم می نوش پیاپی و دمادم -
6064:۴ - مهست از: مه ( بز رکه )۲ست ( پوند صفت عالی )ء دراوستا 13285181218صفقت
6068:نختین سرنامه کفت از مهست شهنشاء کسرای بزدان پرست .
9272:و يْكك - و لام میره ای همهست مخصوس | عربی‌آواز وصدای سخن کردنراکوبند ۷ .
```


## [2026-09-07T16:01:12.984Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT\nfor L in 5805 6064; do\n  awk -v L=$L 'NR<=L{if(/\\[pdf page/){p=$0}} END{print \"line\",L,\"->\",p}' BQT_v4_pages.txt\ndone\necho \"=== context 6055-6075 ===\"; sed -n '6055,6075p' BQT_v4_pages.txt\necho \"=== context 5800-5810 ===\"; sed -n '5798,5812p' BQT_v4_pages.txt"
}
```


### [2026-09-07T16:01:14.270Z] TOOL RESULT

```
line 5805 -> [pdf page 146]
line 6064 -> [pdf page 152]
=== context 6055-6075 ===
مه‌شید ؟ - با شین قله دار بر وزن ۱ تا بجست وخیز درآید .#9
فهمید » بممنی‌مهتاب است چه‌شید روشنی و پرتو مهمان سر ای - کنابه‌ازدیاورو زکار
راکویند . است.- و جاییرادیز کوبند که پیوسته بفقرا
مهک ۴ - بنتح اودوسکون تانی‌وکان, | وماکین طمام دهند مانند مزارات‌وخاهاه وامثال
دام درخت سوس است و ییخ آن را بجربی اسل | آن » وآنرا لنگر هم میگویند.
الوی وامابع‌الو ی کوبند . مه هرد ۱ -» بکر ارل و قح ناك ,
۱- مهری‌بکی پیرفزاره آوا پرآورده بزار ‏ چون تندراندر مرغزارجانیبهرجا ريخته.
« خاقانی شروالی ص ۳۸۸ ۰

۴ - مهست از: مه ( بز رکه )۲ست ( پوند صفت عالی )ء دراوستا 13285181218صفقت
عالی از 388 ( ۳ مه . بز رکه ) است بمعنی مهترین « فاب ۱ اس 0۹ »۰ پهلوی 2288151
« اسشق ۹۹۹ :

نختین سرنامه کفت از مهست شهنشاء کسرای بزدان پرست .
فردوسی طوسی ۸« شاهتامةٌ بخ چ ۸ امس ۲۳۱۹
معنی متن صحیح لیست . ۴ از : مه ( مغخفف ماء )+ شید (ه.م.) قن : خورشید .

۴ - مهك 1ط2 2 ۳ منکه ۳۱811 ( فولرس آ1 ۰ ۱۲۳4 ) ۳ 996ن1ق76 (فر) «عقار
اف - (م) « مهماز بروزن مفتاح » آهنی است دریی موزء سوار و جمع آن
مهامز بروزن مفاعل ومهامیز بروزن قنادیل میآید.» ۶ شرح فاموس > و رك : مهمیز +

=== context 5800-5810 ===
۹ () چش :گوند .

۱ مصحف « مهراب » (ه.م.) ۴ - دارمتتر ۸8118۳80 را در ردیف سهراب

و رودابه و سودابه و افراسیاب پادکند» وجزه اخیر «آب > را بمعنی ماء ( عربی) نمیداند بلکه
آنرا پوندی محوب میدارد «دارمستش . تبعات چا 2۲۹۸ ۴ - رك : فهرست ولف-

۴ <د مهاراجه > سانسکریت ۳4[8 - ۸18۵۵ (شاه بز رکه . سلطان عظیم) «وبليامز

۹ :۳ جزه اول مها (۸.م.) بمعنی بزرکك وجزه دوم بمعنی پادشاه ازريشة [۲8 . ۰128
718 بمعنی سلطنت کردن » شاه با رئین بودن » راهنمایی کردن » حکومت کردن « وبلیاهز
7۳ این کلمه عنوان همومی راجه های ( پادشاهان ) هندوستان است » وچون اسدی طوسی
در گرشاسب‌نامه از « مهراج » یادشاهی معین را در هندوستان آراده کرده :

شهی بود در هند مهراج نام بزرکی بهر جای کسترده کام .
```


## [2026-09-07T16:01:39.601Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor L in 1122 4471 7490; do\n  n=$(awk -v L=$L 'NR<=L{c+=gsub(/\\f/,\"\")} END{print c}' HUB.txt)\n  echo \"--- line $L, formfeeds=$n\"\n  awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n+1{print substr($0,1,120)}' HUB.txt\ndone"
}
```


### [2026-09-07T16:01:40.936Z] TOOL RESULT

```
--- line 1122, formfeeds=44
— 34 —
Im Phi. ist apSdak oder apejak zu lesen, wenn die Schreib-
weise alt ist.
255. Np. beS *mehr als Comparativ z
--- line 4471, formfeeds=138
— 128 —
xah = xoh 'Speise*, kaxard 'Zauberer = zd. kax^areda-.
Auch pers. xu- wird im Armenischen durch xo- wieder-

--- line 7490, formfeeds=220
- 210 —
oben p. 47), arasam (siehe oben p. 67), vielleicht auch -isa-
= skr. iddha- {iddhd *Wunsch', i66hati Vunscht*)
```


## [2026-09-07T16:02:02.139Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/m%C3%A9d%CA%B0yos' --note 'page 325, root Medhyo: PIE *medhyos \"middle\", descendant list (PGmc *midjaz, Proto-Italic *meðios, PII *madhyas)' 2>&1 | tail -2\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D9%85%DB%8C%D8%A7%D9%86' --note 'page 325, entry 0 node 4: Persian میان < MP mayān < OP *madyānah < PIr *mádyānah < PIE *medhyos; Av. maiδiia cognate' 2>&1 | tail -2\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D9%85%D9%87' --note 'page 325, entry 1 node 3: Persian مه (meh) \"great\" etymology 4, from MP meh, PIr *maja, PIE *meǵh2s' 2>&1 | tail -2\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/m%C3%A9%C7%B5h%E2%82%82s' --note 'page 325, root Meg/Megh: PIE *méǵh2s \"big, great\", Av. mazah, Skt mahas, Gk megas, Lat magnus, PGmc *mikilaz' 2>&1 | tail -2\npython3 tools/fetch_source.py 'https://www.etymonline.com/word/more' --note 'page 325, entry 1 node 9: English \"more\" from OE mara, PGmc *maiz-, PIE *meis-/*me- \"big\" — NOT *meg-' 2>&1 | tail -2\npython3 tools/fetch_source.py 'https://www.etymonline.com/word/Mediterranean' --note 'page 325, entry 0 nodes 7/10: Latin mediterraneus < medius + terra, PIE *medhyo- + *ters-; English from 1590s' 2>&1 | tail -2\npython3 tools/fetch_source.py 'https://vajehyab.com/?q=%D9%85%D9%87%D8%A7%D8%B1%D8%A7%D8%AC%D9%87&d=moein' --note 'page 325, entry 1 node 5: Moin entry مهاراجه tagged [سنس.] Sanskrit' 2>&1 | tail -2\npython3 tools/fetch_source.py 'https://vajehyab.com/?q=%D9%85%D8%A7%DA%A9%D8%B3%DB%8C%D9%85%D9%85&d=moein' --note 'page 325, entry 1 node 12: Moin entry ماکسیمم tagged [فر.] French = حداکثر' 2>&1 | tail -2\npython3 tools/fetch_source.py 'https://vajehyab.com/?q=%D9%85%D8%AF%DB%8C%D9%88%D9%85&d=moein' --note 'page 325, entry 0 node 9: Moin entry مدیوم tagged [فر.] French = واسطه' 2>&1 | tail -2"
}
```


### [2026-09-07T16:02:06.772Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/effb80bcbb46ab5d.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/055d8f8dea8e42cb.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/6ad9cc73b4e26ac0.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/5f868d363796e623.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/3d8627cdc92c677c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/550ee64fda1c5e57.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b4345ac5a3e2558c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/0e6506b045db0444.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e2bc6d4e009c25cd.txt
```


## [2026-09-07T16:02:24.437Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nmkdir -p data/verification/sources/refs/ocr/BOOK\ncp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg325.png data/verification/sources/refs/ocr/BOOK/325.png\ncat > data/verification/sources/refs/ocr/BQT/2002.vision.txt <<'EOF'\n[read from image: /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/2002.png\n = Borhan-e Qate' ed. Mo'in, continuous pagination p. 2002 (vol. 4 scan, pdf page 85)]\n\nHeadword (right column, bottom):\nمزنا ٥ - بکسر اول و سکون ثانی و نون بالف کشیده . بلغت زند بمعنی ترازو باشد\nوبعربی میزان گویند .\n\nMo'in's footnote 5 (bottom of page):\n۵ - مز . maznâ , mazînâ ، پهلوی tarâzûk ( ترازو ) « یونکر ص ۱۱۷ » ،\nقس : میزان (عر) .\n\n[i.e. Mo'in gives the readings maznā / mazīnā, glosses the Pahlavi equivalent as\ntarāzūk 'balance' citing Junker p. 117 (Frahang i Pahlavik), and says \"cf. Arabic\nmīzān\". He gives NO connection to a word meaning 'great'.]\n\nOther footnotes on the same page used for context:\n۱۰ - پهلوی micîtan ، کردی mîtin , mîzhim ( مکیدن ) ، بلوچی micag , mishagh\n( مکیدن ) . از ریشهٔ meq/c- ( مکیدن ) « اسشق ۹۷۹ » ...\n٥ مزه - بفتح اول و دوم ( در لهجهٔ مرکزی بکسر دوم ) ، پهلوی mêcak , micak\n« تاوادیا ۱۶۳ » ، کردی mezé ( ذوق ، طعم ) ...\nEOF\necho ok; ls -la data/verification/sources/refs/ocr/BOOK/325.png"
}
```


### [2026-09-07T16:02:24.528Z] TOOL RESULT

```
Exit code 2
cp: cannot stat '/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg325.png': No such file or directory
ok
ls: cannot access 'data/verification/sources/refs/ocr/BOOK/325.png': No such file or directory
```


## [2026-09-07T16:02:29.449Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npdftoppm -f 325 -l 325 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf data/verification/sources/refs/ocr/BOOK/325 && ls -la data/verification/sources/refs/ocr/BOOK/325.png"
}
```


### [2026-09-07T16:02:31.318Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 77674 Sep  7 12:02 data/verification/sources/refs/ocr/BOOK/325.png
```


## [2026-09-07T16:05:39.381Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor L in 444 466 477; do n=$(awk -v L=$L 'NR<=L{c+=gsub(/\\f/,\"\")} END{print c}' PHD.txt); echo \"PHD line $L -> leaf $n -> printed $((n-21))\"; done\necho \"--- verify PHD leaf headers ---\"\nawk 'BEGIN{RS=\"\\f\"} NR==75{print substr($0,1,80)}' PHD.txt\necho \"=== NYB printed page for mas ===\"\nn=$(awk 'NR<=2478{c+=gsub(/\\f/,\"\")} END{print c}' NYB_vol2_glossary.txt); echo \"leaf $n printed $((n-8))\"\necho \"=== KLN nearby page numbers for maharaja(22566)/mickle(23807)/omega(26237) ===\"\nfor L in 22566 23807 26237; do awk -v L=$L 'NR<=L && /^[0-9]{3,4}$/{p=$0} END{print \"line\",L,\"last page marker\",p}' KLN_1966.txt; done\necho \"=== HJB line 8792 page ===\"\nn=$(awk 'NR<=8792{c+=gsub(/\\f/,\"\")} END{print c}' HJB.txt); echo \"leaf $n\""
}
```


### [2026-09-07T16:05:40.777Z] TOOL RESULT

```
PHD line 444 -> leaf 77 -> printed 56
PHD line 466 -> leaf 79 -> printed 58
PHD line 477 -> leaf 79 -> printed 58
--- verify PHD leaf headers ---
 ~] mighty. C 6084 E
kardan 5o kehtar
kardan, kun-, (P Каг-) [OBYDWN-in' < А
=== NYB printed page for mas ===
leaf 141 printed 133
=== KLN nearby page numbers for maharaja(22566)/mickle(23807)/omega(26237) ===
line 22566 last page marker 923
line 23807 last page marker 974
line 26237 last page marker 999
=== HJB line 8792 page ===
leaf 368
```


## [2026-09-07T16:05:54.857Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"^meg'\\|^meĝ\\|^megh\\|^meg(h)\\|^meg-\\|^megos\\|^megə\" IEC.txt | head\necho \"---\"; grep -n \"mazant\\|mahant\" IEC.txt | head -5"
}
```


### [2026-09-07T16:05:54.925Z] TOOL RESULT

```
10468:meĝ- (məĝ-) ‘great, big’. Cf. meĝəlos, măĝ- (3). WP II, 257 Arm. mec, i, av, id.; Hitt. cf. mekkis, cpds. mak-, id. consonantism problematical; cf. also Hitt. makkess(mi) ‘become great; Myc. me- zo(n), mezana-, meki(s)ta- ‘greater; great-; greatest; Gk. mégas, n: méga, adj. ‘big, great’; méga, adv.; cf. meízoón ‘bigger’; mégistos “big- gest; Alb. (r-gde) i madh, f: e madhe, pl. té mëdhenj, fpl: të mëdhaja; Lat. magis, adv. ‘more’; Ir. cf. mi-adh (‘honour , if: Gk. mége- thos ‘greatness’: OBr. muoed ‘pride’); OBr. moi, mui, Br. mül, Cor. moy, W mwy, comp. (*more', fr. *megio-); ON mjok, adv. ‘greatly, very; almost. (The consonantism of Hitt. mekkis, and of Skt. mahá-, etc. is problemati- cal)
10476:megh- (2) element of 1st. pers. sing. pron. T, me?
---
```


## [2026-09-07T16:06:03.431Z] AGENT

Now I'll write the verification file.


## [2026-09-07T16:15:35.267Z] TOOL CALL #68: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification && cat > /home/sfmqrb/git/rishe/data/verification/page-325.json <<'JSONEOF'\n{\n  \"pdf_page\": 325,\n  \"book_page\": 295,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-07\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Medhyo\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *médʰyos 'middle' (Pokorny 706-707 medhi-, medhyo-; Watkins/AHD medhyo-)\",\n      \"note\": \"Root, language label and gloss are all right. Pokorny's lemma is 'medhi-, medhyo- : middle', pp. 706-707; Walde-Pokorny II 261 heads it 'medhio- \\\"mittlerer\\\"'; Watkins/AHD has 'medhyo-. Middle. [Pok. medhi- 706]'; Mann IEC 'medhios, ā, io \\\"middle; midst, centre\\\". WP II, 261'. In the laryngeal-era reconstruction *médʰyos is itself a derivative — *me-dʰi ('near, with' + locative *-dʰi) thematised — which is why Watkins keeps a separate entry me-2 'in the middle of' and cross-refers ('See also me-2'); that is a refinement of, not a contradiction to, Nourai's root box. The root box on the printed page carries no reference of its own; the branch references were checked node by node.\",\n      \"note_fa\": \"ریشهٔ هندواروپایی آغازین *médʰyos «میان، میانه» است؛ پوکورنی آن را در صفحهٔ ۷۰۶ـ۷۰۷ زیر medhi-/medhyo- و والده‌ـپوکورنی در جلد دوم ص ۲۶۱ زیر medhio- «میانی» آورده‌اند و واتکینز (AHD) نیز همین صورت را دارد. در بازسازی‌های تازه‌تر این ریشه خود مشتق شمرده می‌شود: از قید *me «نزدیک، با» و پسوند مکانی *-dʰi، که با پسوند ستاکی -o- صفت شده است. نام ریشه، برچسب زبانی و معنایی که نورایی داده درست است؛ در نمودار برای خودِ جعبهٔ ریشه ارجاعی نیامده و ارجاع‌ها در گره‌ها بررسی شده‌اند.\",\n      \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/m%C3%A9d%CA%B0yos\"],\n      \"ref_check\": [\n        {\"ref\": \"(none cited)\", \"status\": \"not_checked\", \"note\": \"the Medhyo root box on p. 295 carries no refs= at all (confirmed on the page image data/verification/sources/refs/ocr/BOOK/325.png); the branch refs KLN:954, HRN:225, SOD:223, AHD, MON:3974 are checked on the nodes\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"POK\", \"where\": \"pp. 706-707 (POK_full.txt block 'Root / lemma: medhi- medhyo-')\", \"stance\": \"supports\", \"note\": \"'Meaning: middle ... Old Indic madhya-, Avestan maidya- \\\"medial\\\" ... Latin medius ... Gothic midjis, Old English midd ... References: WP. II 261 ... Page(s): 706-707'\"},\n        {\"src\": \"WLD\", \"where\": \"Bd. II p. 261 (WLD_Bd2_pages.txt leaf 266)\", \"stance\": \"supports\", \"note\": \"'medhio- \\\"mittlerer\\\". Ai. madhya-, av. maidya- \\\"mittleres\\\", Sup. ai. madhyama-, av. madəma- ... gr. mesos, lat. medius, osk. mefiai \\\"in media\\\"'; the German index in Bd. III also lists 'mittlerer medhio- 2 261'\"},\n        {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. medhyo-\", \"stance\": \"supports\", \"note\": \"'medhyo-. Middle. 1. Germanic *midja- ... 2. Latin medius, middle, half ... 3. Greek mesos, middle: MESO-. See also me-2. [Pok. medhi- 706.]'\"},\n        {\"src\": \"IEC\", \"where\": \"Mann, s.v. medhios (IEC.txt line 10447)\", \"stance\": \"supports\", \"note\": \"'medhios, ā, io \\\"middle; midst, centre\\\". WP II, 261. Skt. madhyah ... Av. maiδyo, adj.; Oss. mid-, Dig. med- ... Lat. medius, adj. ... Go. midjis, adj.; OE midd, midde'\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan\",\n          \"words\": \"maidyâna\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Avestan maiδyāna- n. 'middle, midst' is real: Bartholomae, Altiranisches Wörterbuch col. 1116, 'j. maiδyāna-, maiδyāna- n. \\\"Mitte\\\"', used both of the middle of the body (the waist) and of a space. It is an -āna- derivative of Av. maiδya- 'middle' < Proto-Iranian *madya- < PIE *médʰyos: PIE *dʰ gives Iranian d, which in Avestan spelling appears as the fricative δ between vowels, so *madya- is written maiδya- with the i-epenthesis regular before -δy-. Nourai writes δ as plain d ('maidyâna'), as the book does throughout, and the long -ā- of the suffix is what yields the -ān of Sogdian myδʾn, MP mayān and NP miyān.\",\n          \"derivation_fa\": \"اوستایی maiδyāna- «میان، میانه» واژه‌ای واقعی است؛ بارتولومه در «واژه‌نامهٔ ایرانی باستان» ستون ۱۱۱۶ آن را با معنی «میانه» (هم میانهٔ تن یعنی کمر و هم میانهٔ مکان) آورده است. این واژه با پسوند -āna- از maiδya- «میانی» ساخته شده که خود از ایرانی باستان *madya- و هندواروپایی *médʰyos است؛ *dʰ هندواروپایی در ایرانی به d بدل شده و در میان دو واکه به‌صورت سایشی δ نوشته می‌شود، و پیش از -δy- واکهٔ میانجی i افزوده شده است. نورایی مانند سراسر کتاب δ را d نویسه‌گردانی کرده؛ همان -ā- کشیدهٔ پسوند است که -ān در سغدی myδʾn و فارسی میانهٔ mayān و فارسی نو «میان» را به دست می‌دهد. ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/m%C3%A9d%CA%B0yos\"],\n          \"ref_check\": [\n            {\"ref\": \"KLN:954\", \"status\": \"partial\", \"note\": \"Klein's hub entry for the whole family is on that leaf: 'media, n., formerly, a voiced stop consonant ... fem. of L. medius, which stands for *medhyos, rel. to Oscan mefiai (fem. sing.), \\\"in the middle\\\", and cogn. with OI. madhyaḥ, Avestic maidya-, \\\"middle\\\", Gk. mesos ... Goth. midjis, OE. midd' (KLN_1966.txt line 23269, between the page markers 953 and 957, i.e. pp. 954-956). Klein gives Avestic maidya-, not the -āna- derivative maiδyāna-, so the page supports the root and the Avestan cognate but not Nourai's exact Avestan form.\"},\n            {\"ref\": \"HRN:225\", \"status\": \"supports\", \"note\": \"Horn, Grundriss der neupersischen Etymologie no. 1004, p. 225 (HRN.txt leaf 246): 'miyān \\\"Mitte; mitten, mittlerer\\\", miyāne, aw. maiδyāna- \\\"Mitte\\\"; phlv. miyān; ai. vergl. madhya- \\\"Mitte\\\"' — exactly Nourai's Avestan → Pahlavi → Persian arrow.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"col. 1116 (index line 'maiδyāna- 1116'; entry at BRT.txt line 19638)\", \"stance\": \"supports\", \"note\": \"'j. maiδyāna-, maiδyāna- n. \\\"Mitte\\\"; a) des Leibes ...' — the Avestan headword and gloss are exactly as charted\"},\n            {\"src\": \"HUB\", \"where\": \"Persische Studien p. 128 (HUB.txt line 4471) and p. 210 (line 7085)\", \"stance\": \"supports\", \"note\": \"'miyan \\\"Mitte\\\" = paz. phl. miyan, zd. maiδyāna-' (both places)\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. II p. 261\", \"stance\": \"partial\", \"note\": \"lists 'av. maidya- \\\"mittleres\\\"' but not the -āna- derivative\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Sogdian\",\n          \"words\": \"myd`n\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Gharib, Sogdian Dictionary, entry no. 5590 on printed p. 223: 'myδʾn M — meδān (myd'n, mydn) ← Av. maiδyāna; Parth. maδyan ... middle, waist', with the oblique postposition myδʾnyt 'amidst, amongst' and the derivative myδʾnc 'middle' (no. 5593). Nourai's backtick in 'myd`n' is his ASCII for the aleph of the Sogdian spelling ⟨myδʾn⟩. Sogdian keeps the intervocalic -δ- that South-West Middle Persian lost, so myδʾn /meδān/ and MP mayān are parallel reflexes of one Old Iranian *madyāna-; strictly Sogdian is a sister of the Avestan word rather than a descendant of it, and Gharib's '← Av. maiδyāna' is a cognate reference, not a claim of borrowing.\",\n          \"derivation_fa\": \"غریب در «فرهنگ سغدی» شمارهٔ ۵۵۹۰ در صفحهٔ چاپی ۲۲۳ می‌آورد: myδʾn (myd'n, mydn) = meδān «میان، کمر»، با ارجاع به اوستایی maiδyāna و پارتی maδyan. علامت ` در نویسه‌گردانی نورایی همان الفِ املای سغدی ⟨myδʾn⟩ است. سغدی δ میان‌واکه‌ای را نگه داشته، حال آنکه فارسی میانهٔ جنوب‌غربی آن را از دست داده است؛ پس myδʾn سغدی و mayān پهلوی هر دو بازماندهٔ یک صورت ایرانی باستان *madyāna- اند و سغدی خواهرِ واژهٔ اوستایی است نه فرزند آن ــ یعنی پیکان نمودار را باید «هم‌ریشه» خواند. ادعای نورایی در جانِ مطلب درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%D9%85%DB%8C%D8%A7%D9%86\"],\n          \"ref_check\": [\n            {\"ref\": \"SOD:223\", \"status\": \"supports\", \"note\": \"the page number is exact: the block of SOD_pages.txt that contains entry 5590 carries the printed numeral 223 (awk 'BEGIN{RS=\\\"\\\\f\\\"} /5590 my/' SOD_pages.txt → block 290, printed '223'), and the entry reads 'myδʾn M ... meδan (myd'n, mydn) ©Av. maiδyāna; Parth. maδyan ... middle, waist'\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"col. 1116 s.v. maiδyāna-\", \"stance\": \"supports\", \"note\": \"supplies the Avestan parent form Gharib cites\"},\n            {\"src\": \"SOD\", \"where\": \"entries 5590-5593, p. 223\", \"stance\": \"supports\", \"note\": \"also 'myδʾnc — meδanc — middle' and the postposition myδʾnyt 'amidst', showing the word is well attested in Manichaean and Christian Sogdian\"},\n            {\"src\": \"HRN\", \"where\": \"no. 1004, p. 225\", \"stance\": \"partial\", \"note\": \"gives the Iranian cognate set for miyān (Kurdish, Ossetic medæg, Balochi niyām, Wakhi malung, Sarikoli maδān) but no Sogdian\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Pahlavi\",\n          \"words\": \"\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"The empty pass-through box stands for Middle Persian mayān / miyān. MacKenzie, A Concise Pahlavi Dictionary p. 58: 'mayān [mdyʾn' | M myʾn, N miyān] middle; among, between', with the derivative mayānag 'middling, average'. The Book Pahlavi spelling ⟨mdyʾn⟩ still writes the old -d- (= δ) that Manichaean MP ⟨myʾn⟩ has already lost; Nyberg's glossary uses miyān throughout (e.g. 'ō miyān ~ to provoke (enmity)', 'damīk andar miyān ī asmān'). The development is Old Iranian *madyāna- > *maδyān > mayān > miyān: intervocalic δ is lost in South-West Middle Persian and the a of the first syllable is raised before the following y.\",\n          \"derivation_fa\": \"این جعبهٔ خالی جای فارسی میانهٔ mayān/miyān را می‌گیرد. مکنزی در «فرهنگ کوچک پهلوی» ص ۵۸ آورده است: mayān [mdyʾn' | مانوی myʾn، فارسی نو میان] «میان؛ در میانِ، بین»، با مشتقِ mayānag «میانه، متوسط». املای پهلوی کتابی ⟨mdyʾn⟩ همان d (= δ) کهن را نگه داشته، در حالی که املای پهلوی مانوی ⟨myʾn⟩ آن را از دست داده است؛ نیبرگ نیز در واژه‌نامهٔ خود همه‌جا miyān به کار می‌برد. تحول آوایی چنین است: ایرانی باستان *madyāna- > *maδyān > mayān > میان، یعنی δ میان‌واکه‌ای در فارسی میانهٔ جنوب‌غربی افتاده و a پیش از y به i بدل شده است. ادعای نورایی درست است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"(none cited)\", \"status\": \"not_checked\", \"note\": \"the Pahlavi box on the printed page has no refs= (page image data/verification/sources/refs/ocr/BOOK/325.png)\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"p. 58 s.v. mayān (PHD.txt line 466)\", \"stance\": \"supports\", \"note\": \"'mayān [mdyʾn' | M myʾn, N miyān] middle; among, between. ~ag [-k! | N ~a] middling, average.'\"},\n            {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II, glossary, passim (e.g. s.v. apa-kandan, hangōšītak)\", \"stance\": \"supports\", \"note\": \"reads the word as miyān: 'ō miyān ~ to provoke (enmity)'; 'damīk andar miyān ī asmān'; also miyānjīkēh 'mediation ... NP miyānjī'\"},\n            {\"src\": \"HRN\", \"where\": \"no. 1004, p. 225\", \"stance\": \"supports\", \"note\": \"'phlv. miyān' between Avestan maiδyāna- and NP miyān — the same two-step chain the chart draws\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Persian\",\n          \"words\": \"miyân «میان»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"New Persian میان miyān 'middle, midst; waist' continues MP mayān/miyān without change; Horn no. 1004 and Hübschmann p. 128 ('miyan \\\"Mitte\\\" = paz. phl. miyan, zd. maiδyāna-') both give exactly this chain, and Wiktionary reconstructs it as MP mdyʾn (mayān) < Old Persian *madyānah < Proto-Iranian *mádyānah (= *mádyah + *-anah) < PIE *médʰyos, with Avestan maiδiia- as the Avestan cognate. Iranian relatives of the same word are Ossetic mid-/medæg 'inner', Kurdish (loan) mayān, Balochi niyām, Sarikoli maδān, Gilaki men; Arabic ميدان maydān 'open field, square' is normally taken as a borrowing of the Persian word in the opposite direction.\",\n          \"derivation_fa\": \"«میان» فارسی نو به معنی «وسط، میانه؛ کمر» بی هیچ دگرگونی ادامهٔ mayān/miyān فارسی میانه است. هرن (شمارهٔ ۱۰۰۴) و هوبشمان (ص ۱۲۸، «میان = پازند و پهلوی miyan، اوستایی maiδyāna-») هر دو همین زنجیره را می‌دهند و ویکی‌واژه آن را چنین بازسازی می‌کند: فارسی میانهٔ mayān < پارسی باستان *madyānah < ایرانی آغازین *mádyānah (از *mádyah + پسوند *-anah) < هندواروپایی *médʰyos، با هم‌ریشهٔ اوستایی maiδiia-. هم‌ریشه‌های ایرانی آن آسی medæg «درونی»، بلوچی niyām، سریکلی maδān و گیلکی «مِن» است؛ «میدان» عربی را نیز عموماً وام‌واژه‌ای از همین واژهٔ فارسی می‌دانند. ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%D9%85%DB%8C%D8%A7%D9%86\"],\n          \"ref_check\": [\n            {\"ref\": \"(none cited)\", \"status\": \"not_checked\", \"note\": \"the Persian box for miyân has no refs= on the printed page; the branch is covered by HRN:225 on node 1\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"HRN\", \"where\": \"no. 1004, p. 225\", \"stance\": \"supports\", \"note\": \"'miyān \\\"Mitte; mitten, mittlerer\\\", miyāne, aw. maiδyāna- \\\"Mitte\\\"; phlv. miyān'\"},\n            {\"src\": \"HUB\", \"where\": \"pp. 128 and 210\", \"stance\": \"supports\", \"note\": \"'miyan \\\"Mitte\\\" = paz. phl. miyan, zd. maiδyāna-'; on p. 128 in the list of Persian words whose intervocalic d/δ has disappeared, and p. 210 'skr. padāti- ... miyan \\\"Mitte\\\" = paz. phl. miyan, zd. maiδyāna-'\"},\n            {\"src\": \"PHD\", \"where\": \"p. 58 s.v. mayān\", \"stance\": \"supports\", \"note\": \"explicitly gives 'N miyān' as the New Persian outcome\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Germanic\",\n          \"words\": \"midja\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Proto-Germanic *midjaz 'middle' < PIE *médʰyos, with the Grimm shift *dʰ > *d and the thematic *-yo- kept: Gothic midjis, Old Norse miðr, Old Saxon middi, Old Frisian midde, Old High German mitti, Old English midd. The West Germanic geminate -dd- is the regular gemination before *y. Nourai's 'midja' is the stem form (Gothic nom. midjis). Watkins medhyo- §1: 'Germanic *midja- in: a. Old English midd(e), middle: MID, AMID'.\",\n          \"derivation_fa\": \"ژرمنی آغازین *midjaz «میانی» از هندواروپایی *médʰyos است: بر پایهٔ قانون گریم، *dʰ به d بدل شده و پسوند ستاکی *-yo- بر جای مانده است؛ گوتی midjis، نورس کهن miðr، ساکسون کهن middi، آلمانی علیای کهن mitti و انگلیسی کهن midd همه از همین صورت‌اند. دوگانه‌شدن -dd- در ژرمنی باختری همان همگونیِ منظمِ پیش از *y است. صورتی که نورایی آورده (midja) ستاکِ واژه است. واتکینز نیز زیر medhyo- می‌نویسد: «ژرمنی *midja- در انگلیسی کهن midd(e)». ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/m%C3%A9d%CA%B0yos\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 s.v. medhyo- §1: 'Germanic *midja- in: a. Old English midd(e), middle: MID(1); AMID; b. West Germanic diminutive form *middila- in Old English middel, middle: MIDDLE'\"},\n            {\"ref\": \"KLN\", \"status\": \"supports\", \"note\": \"KLN_1966.txt line 23844 s.v. 'mid, adj. — ME., fr. OE. midd, rel. to ON. miðr, OS. middi, OFris. midde, OHG. mitti, Goth. midjis, \\\"mid\\\", and cogn. with OI. madhyaḥ, Gk. mesos, L. medius, \\\"middle\\\"' (p. 978)\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"pp. 706-707\", \"stance\": \"supports\", \"note\": \"'Gothic midjis, Old Icelandic miðr, Old English midd, Old High German mitti \\\"in the middle\\\", Superl. Gothic miduma \\\"the middle\\\"'\"},\n            {\"src\": \"IEC\", \"where\": \"Mann s.v. medhios\", \"stance\": \"supports\", \"note\": \"'Go. midjis, adj.; MHG mët-, cpds.; OE midd, midde, adj. & sf; OS middia, f.; ON miðja'\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. II p. 261\", \"stance\": \"supports\", \"note\": \"the Germanic set is listed under medhio- with the superlative Goth. miduma\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"English\",\n          \"words\": \"middle\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Old English middel < West Germanic diminutive *middila- built on *midjaz; ME middel > modern middle. Klein: 'middle, adj. — ME. middel, fr. OE. middel, rel. to OS. middil, MLG., Du. middel, OHG. mittil, MHG., G. mittel, \\\"middle\\\" and to OE. midd, \\\"mid\\\"'; Watkins medhyo- §1b 'West Germanic diminutive form *middila- in Old English middel, middle: MIDDLE'. An uncontroversial inherited chain.\",\n          \"derivation_fa\": \"«middle» انگلیسی از middel انگلیسی کهن است که خود صورت مصغّرِ ژرمنی باختری *middila- برساخته بر *midjaz است؛ از انگلیسی میانه middel به صورت امروزی رسیده. کلاین می‌نویسد: «middle از انگلیسی میانه middel، از انگلیسی کهن middel، هم‌ریشه با ساکسون کهن middil و آلمانی mittel و وابسته به midd انگلیسی کهن». واتکینز هم زیر medhyo- بند ۱ب همین را دارد. زنجیره‌ای موروثی و بی‌اختلاف است؛ ادعای نورایی درست است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"(none cited)\", \"status\": \"not_checked\", \"note\": \"no refs= on the English box; the parent box carries AHD; KLN\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"p. 978 s.v. middle (KLN_1966.txt line 23847)\", \"stance\": \"supports\", \"note\": \"'middle, adj. — ME. middel, fr. OE. middel ... and to OE. midd, \\\"mid\\\". See mid, adj.'\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. medhyo- §1b\", \"stance\": \"supports\", \"note\": \"'West Germanic diminutive form *middila- in Old English middel, middle: MIDDLE'; the index has 'MIDDLE medhyo-'\"}\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"Latin\",\n          \"words\": \"medius; medi-terrâneous\",\n          \"verdict\": \"transcription_suspect\",\n          \"derivation\": \"The first word is right: Latin medius 'middle' < Proto-Italic *meðios < PIE *médʰyos, with intervocalic *dʰ > Latin d (Oscan has the fricative, mefiai 'in media'). Watkins medhyo- §2: 'Latin medius, middle, half: MEAN, MEDIAL, MEDIAN, MEDIASTINUM, MEDIATE, MEDIUM, MITTEN, MIZZEN, MOIETY, MULLION; INTERMEDIATE, MEDIEVAL, MEDIOCRE, MEDITERRANEAN, MERIDIAN, MILIEU'. The second word is the sea name: Latin mediterrāneus 'inland, midland' (medius + terra 'earth, land' + -āneus), Late Latin Mediterrāneum mare (7th c.), English Mediterranean 1590s (earlier Mediterranie c. 1400) — so Nourai's '☞Ters' cross-reference is exactly right, because Watkins indexes MEDITERRANEAN under both medhyo- and ters- 'to dry'. But the form printed in the book, 'medi-terrâneous', is not a possible Latin word: -ous is the English adjective suffix, and Latin has mediterrāneus. The gloss 'in land sea' is likewise a garbled 'inland (sea)': mediterrāneus by itself means 'inland/midland', the 'sea' coming from mare in the Late Latin name. The book prints it this way, so the extraction is faithful and the fault is Nourai's own.\",\n          \"derivation_fa\": \"واژهٔ نخست درست است: لاتین medius «میانی» از ایتالیکِ آغازین *meðios و هندواروپایی *médʰyos است؛ *dʰ میان‌واکه‌ای در لاتین به d بدل شده (اسکی mefiai همان سایشی را نگه داشته). واتکینز زیر medhyo- بند ۲ همین را با فهرست بلندی از مشتقات لاتین آورده است. واژهٔ دوم نام دریا است: لاتین mediterrāneus «درون‌خشکی» از medius + terra «خاک، زمین» + پسوند -āneus، در لاتین متأخر Mediterrāneum mare (سدهٔ هفتم)، و از سدهٔ ۱۶ در انگلیسی Mediterranean؛ پس ارجاع نورایی به ریشهٔ Ters درست است، چون واتکینز نیز MEDITERRANEAN را هم زیر medhyo- و هم زیر ters- «خشک» فهرست می‌کند. اما صورتی که در کتاب چاپ شده، «medi-terrâneous»، هیچ‌گاه لاتین نیست: پسوند -ous پسوند صفت انگلیسی است و صورت لاتین mediterrāneus است؛ معنیِ «in land sea» هم صورتِ به‌هم‌ریختهٔ «inland (sea)» است. این خطای چاپی خودِ کتاب است، نه خطای خوانش اسکن.\",\n          \"sources\": [\"https://www.etymonline.com/word/Mediterranean\"],\n          \"error_in\": \"book\",\n          \"book_prints\": \"medi-terrâneous : in land sea\",\n          \"correct_form\": \"mediterrāneus 'inland, midland' (Late Latin Mediterrāneum mare)\",\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 s.v. medhyo- §2 lists Latin medius with MEDITERRANEAN among its English derivatives, and the AHD word-index line reads 'MEDITERRANEAN medhyo-, ters-' — precisely Nourai's ☞Ters\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"pp. 706-707\", \"stance\": \"supports\", \"note\": \"'Latin medius \\\"in the middle, in the midst, mid, mean, middle\\\", Oscan mefiaf \\\"in media\\\"'\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. II p. 261\", \"stance\": \"supports\", \"note\": \"'lat. medius, osk. mefiai \\\"in media\\\", gr. mesa(a)tos = lat. medietas; gall. Medio-lanum'\"},\n            {\"src\": \"KLN\", \"where\": \"pp. 954-956 s.v. media / mediterranean group\", \"stance\": \"supports\", \"note\": \"'media, n. ... fem. of L. medius, which stands for *medhyos ... Cp. mid, middle, midst, amid. Cp. also median, mediant, mediastinum, mediate, mediocre, medium, immediate, intermediate ... mean, \\\"intermediate\\\"'\"},\n            {\"src\": \"WEB\", \"where\": \"etymonline (online, in lieu of Webster vol. 2 which is not open)\", \"stance\": \"supports\", \"note\": \"'Late Latin Mediterraneum mare (7c.), from Latin mediterraneus \\\"midland, surrounded by land\\\"; medius \\\"middle\\\" + terra \\\"land, earth\\\" ... 1590s in English, Mediterranie c. 1400'\"}\n          ]\n        },\n        {\n          \"id\": 8,\n          \"lang\": \"French\",\n          \"words\": \"\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"The empty box is the French relay for the two Persian loans in the next box: Latin medium (neuter of medius) → French médium, taken up in the 19th c. in the spiritualist sense 'medium, intermediary'; and Late Latin Mediterrāneum mare → French (mer) Méditerranée. Klein documents the same Latin → Old French → English route for the sister word: 'mean, adj., intermediate. — ME. mene, fr. OF. meien, moien (F. moyen), \\\"middle\\\", fr. Late L. mediānus ... fr. L. medius'.\",\n          \"derivation_fa\": \"این جعبهٔ خالی واسطهٔ فرانسوی است که دو وام‌واژهٔ فارسیِ جعبهٔ بعد از آن گرفته شده‌اند: لاتین medium (خنثای medius) به فرانسوی médium رسیده و در سدهٔ نوزدهم در معنی «واسطه، احضارکنندهٔ ارواح» رواج یافته؛ و لاتین متأخر Mediterrāneum mare به فرانسوی (mer) Méditerranée. کلاین همین راهِ لاتین ← فرانسوی کهن ← انگلیسی را برای واژهٔ هم‌خانوادهٔ mean نشان می‌دهد: «از انگلیسی میانه mene، از فرانسوی کهن meien/moien (فرانسوی moyen)، از لاتین متأخر mediānus، از medius». ادعای نورایی درست است.\",\n          \"sources\": [\"https://vajehyab.com/?q=%D9%85%D8%AF%DB%8C%D9%88%D9%85&d=moein\"],\n          \"ref_check\": [\n            {\"ref\": \"(none cited)\", \"status\": \"not_checked\", \"note\": \"no refs= on the French box\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"p. 953 s.v. mean, adj., intermediate\", \"stance\": \"supports\", \"note\": \"'ME. mene, fr. OF. meien, moien (F. moyen), \\\"middle\\\", fr. Late L. mediānus, \\\"that which is in the middle\\\", fr. L. medius' — the French stage of the same family\"},\n            {\"src\": \"MON\", \"where\": \"vajehyab, Mo'in s.v. مدیوم\", \"stance\": \"supports\", \"note\": \"'(مِ یُ) [ فر. ] (اِ.) واسطه ، شخصی که واسطة احضار ارواح شود' — Mo'in's tag [فر.] identifies French, not Latin or English, as the immediate source\"}\n          ]\n        },\n        {\n          \"id\": 9,\n          \"lang\": \"Persian\",\n          \"words\": \"(no transliteration; script only: مدیوم ، مدیترانه)\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Two modern French loans in Persian. مدیوم medyum is French médium: Mo'in's lexicon gives '(مِ یُ) [ فر. ] (اِ.) واسطه ، شخصی که واسطة احضار ارواح شود' — French origin, in the spiritualist sense, which is the sense French had when the word came in (late Qajar/early Pahlavi period, with the vogue for spiritism). مدیترانه mediterrāne is French Méditerranée, the sea name, borrowed with 19th-20th-c. French geography and school atlases; the Persian spelling with ت rather than ط shows a Western and not an Arabic-mediated transmission (Arabic calls it البحر الأبيض المتوسط). Both are therefore end-points of the Latin → French → Persian route the chart draws, not inherited words.\",\n          \"derivation_fa\": \"دو وام‌واژهٔ نوی فرانسوی در فارسی. «مدیوم» از médium فرانسوی است؛ معین در فرهنگ خود می‌آورد: «(مِ یُ) [فر.] (اِ.) واسطه، شخصی که واسطهٔ احضار ارواح شود» ــ یعنی خودِ معین آن را فرانسوی می‌داند و در همان معنیِ احضار روح که در دورهٔ رواج «روح‌گرایی» به فارسی آمده. «مدیترانه» نیز همان Méditerranée فرانسوی است که با جغرافیا و اطلس‌های مدرسی سدهٔ نوزدهم و بیستم به فارسی راه یافته؛ نوشتنِ آن با «ت» و نه «ط» نشان می‌دهد که از راه غربی آمده است نه از راه عربی (عربی این دریا را «البحر الأبیض المتوسط» می‌نامد). پس هر دو وام‌واژه‌اند و پایانِ همان مسیر لاتین ← فرانسوی ← فارسی که نمودار کشیده است. ادعای نورایی درست است.\",\n          \"sources\": [\"https://vajehyab.com/?q=%D9%85%D8%AF%DB%8C%D9%88%D9%85&d=moein\"],\n          \"ref_check\": [\n            {\"ref\": \"MON:3974\", \"status\": \"partial\", \"note\": \"the Mo'in lexicon text (vajehyab) confirms مدیوم with the origin tag [فر.] = French: '(مِ یُ) [ فر. ] (اِ.) واسطه ، شخصی که واسطة احضار ارواح شود'. مدیترانه is not in the searchable Mo'in lexicon volumes (it belongs to the a'lām/proper-name volumes 5-6, which are not online), so the exact print page 3974 could not be verified; the origin tag and the French sea name make the claim itself secure.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"vajehyab, Mo'in s.v. مدیوم\", \"stance\": \"supports\", \"note\": \"'[ فر. ]' = French; the gloss 'واسطه' matches French médium\"},\n            {\"src\": \"BQT\", \"where\": \"BQT_v4_pages.txt, grep 'مدیترانه|مدیوم'\", \"stance\": \"silent\", \"note\": \"no hits — expected, since Borhan-e Qate' is a 1062/1652 dictionary and cannot contain 19th-c. European loans; Mo'in's footnotes add none here\"}\n          ]\n        },\n        {\n          \"id\": 10,\n          \"lang\": \"English\",\n          \"words\": \"immediate, median, medium, mean 1; Mediterranean\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"All five are Latin medius through Latin or French. immediate < Medieval Latin immediātus (in- 'not' + Late Latin mediātus, pp. of mediāre 'to halve'); median < Latin mediānus; medium < Latin medium, neuter of medius; mean (adj. 'intermediate, average') < ME mene < Old French meien/moien (F. moyen) < Late Latin mediānus — this is Klein's and Watkins's MEAN(3), and Nourai's index number 'mean 1' correctly keeps it apart from mean 'to intend' (OE mǣnan) and mean 'base, low' (OE ġemǣne, from PIE *mei- 'to change'); Mediterranean < Latin mediterrāneus, English from the 1590s. Watkins's medhyo- entry lists MEAN, MEDIAL, MEDIAN, MEDIASTINUM, MEDIATE, MEDIUM ... INTERMEDIATE, MEDITERRANEAN.\",\n          \"derivation_fa\": \"هر پنج واژه از medius لاتین‌اند، برخی مستقیم و برخی به واسطهٔ فرانسوی. immediate از لاتین میانهٔ immediātus (in- «نه» + mediātus، اسم مفعولِ mediāre «به دو نیم کردن»)؛ median از mediānus لاتین؛ medium از خنثای medius؛ و mean (صفت، «میانی، متوسط») از انگلیسی میانه mene، از فرانسوی کهن meien/moien (فرانسوی moyen)، از لاتین متأخر mediānus ــ همان که کلاین و واتکینز MEAN(3) می‌نامند، و شمارهٔ «mean 1» نورایی به‌درستی آن را از mean «قصد کردن» (انگلیسی کهن mǣnan) و mean «فرومایه» (انگلیسی کهن ġemǣne) جدا می‌کند. Mediterranean هم از mediterrāneus لاتین است و از دههٔ ۱۵۹۰ در انگلیسی به کار رفته. ادعای نورایی درست است.\",\n          \"sources\": [\"https://www.etymonline.com/word/Mediterranean\"],\n          \"ref_check\": [\n            {\"ref\": \"(none cited)\", \"status\": \"not_checked\", \"note\": \"no refs= on the English box; the parent Latin box carries AHD\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"pp. 953-956 s.vv. immediate, median, medium, mean (adj., intermediate), media\", \"stance\": \"supports\", \"note\": \"'immediate, adj. — ML. immediatus, fr. in-, \\\"not\\\", and Late L. mediatus, pp. of mediare'; 'median, adj. — L. medianus ... fr. medius'; 'mean, adj., intermediate. — ME. mene, fr. OF. meien, moien (F. moyen) ... fr. Late L. medianus'\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. medhyo- §2 and word-index\", \"stance\": \"supports\", \"note\": \"index lines 'MEAN3 medhyo-', 'MEDIAL medhyo-', 'MEDIAN medhyo-', 'MEDIUM medhyo-', 'MEDITERRANEAN medhyo-, ters-'\"},\n            {\"src\": \"WEB\", \"where\": \"etymonline s.v. Mediterranean\", \"stance\": \"supports\", \"note\": \"'1590s ... from Latin mediterraneus'\"}\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 1,\n      \"root\": \"Meg, Megh\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *méǵh₂s, oblique *m̥ǵh₂- 'big, great' (Pokorny 708-709 meǵ(h)-; Watkins/AHD meg-)\",\n      \"note\": \"Root name, language and gloss are right, and the double form 'Meg, Megh' reproduces the doubt in the sources themselves. Pokorny's lemma is 'meǵ(h)- : meǵ(h)-, \\\"groß\\\"', pp. 708-709 — Nourai's POK:708 is its first page — and Walde-Pokorny II 257 heads it 'meg(h)- \\\"groß\\\" (Gutt.-Verb. wie bei g(h)enus, eg(h)om, ghe : gho)', i.e. the aspiration of the Indic h is unexplained, which is why both write g(h). Watkins meg- says the same in one line: '8. Variant form *megh- in Sanskrit mahā-, mahat- ... [Pok. meg(h)- 708]', and Mann (IEC) adds 'The consonantism of Hitt. mekkis, and of Skt. mahā-, etc. is problematical'. Buck 12.55 'LARGE, BIG (GREAT)' likewise heads section 1 'IE *meg-, *megh-'. Modern reconstruction is *méǵh₂s (nom. sg. m.), oblique *m̥ǵh₂-, the laryngeal accounting for the -a- of Greek mega and Latin magnus. The chart's own note 'This root may be related to \\\"Mâk: long, slender\\\"' is where I part company with Nourai: *meh₂ḱ- 'long' (Pokorny 699) is a separate root, but it is precisely the root to which the standard Iranian handbooks assign the Pahlavi and Persian forms in nodes 2-3 (see there).\",\n      \"note_fa\": \"نام ریشه، برچسب زبانی و معنی درست است، و صورت دوگانهٔ «Meg, Megh» بازتاب تردیدی است که در خودِ منابع هست. پوکورنی سرواژه را meǵ(h)- «بزرگ» در صفحات ۷۰۸ـ۷۰۹ آورده (پس ارجاع POK:708 نورایی درست است) و والده‌ـپوکورنی در جلد دوم ص ۲۵۷ می‌نویسد meg(h)- با این توضیح که ابدال دمیدگی مانند g(h)enus و eg(h)om توضیح‌ناپذیر است؛ همین است که h را در پرانتز می‌گذارند. واتکینز نیز می‌نویسد «صورت گونهٔ *megh- در سنسکریت mahā-, mahat-» و مان (فرهنگ تطبیقی هندواروپایی) می‌افزاید که «همخوان‌های mekkis هیتی و mahā- سنسکریت مسئله‌دار است». باک در بند ۱۲٫۵۵ هم ریشه را *meg-, *megh- می‌آورد. بازسازی امروزی *méǵh₂s (فاعلی مفرد) با ستاک غیرفاعلی *m̥ǵh₂- است و همان حنجره‌ای است که a در mega یونانی و magnus لاتین را توضیح می‌دهد. تنها یادداشت خودِ نمودار («این ریشه ممکن است با ریشهٔ Mâk: دراز مربوط باشد») جای بحث دارد: *meh₂ḱ- «دراز» (پوکورنی ۶۹۹) ریشه‌ای جداست، امّا درست همان ریشه‌ای است که ایران‌شناسان صورت‌های پهلوی و فارسیِ گره‌های ۲ و ۳ را به آن می‌بندند.\",\n      \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/m%C3%A9%C7%B5h%E2%82%82s\"],\n      \"ref_check\": [\n        {\"ref\": \"POK:708\", \"status\": \"supports\", \"note\": \"Pokorny's entry 'Root / lemma: meǵ(h)- : meǵ(h)-, Meaning: big' ends 'References: WP. II 257 ff., WH. II 4 f., 10 ff., Szemerenyi Word 8, 48. Page(s): 708-709' (POK_full.txt block at line 58003) — p. 708 is where it begins\"},\n        {\"ref\": \"KLN:958\", \"status\": \"supports\", \"note\": \"KLN_1966.txt page marker 958 stands immediately before 'mega-, before a vowel meg-, combining form meaning \\\"large, great\\\" ... Fr. Gk. megas ... which is cogn. with L. magnus, \\\"great, large, much, abundant\\\", Goth. mikils, OE. micel, mycel, \\\"great, big, many\\\". See mickle and cp. magnum. Cp. also omega'\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"WLD\", \"where\": \"Bd. II p. 257 (WLD_Bd2_pages.txt leaf 262)\", \"stance\": \"supports\", \"note\": \"'meg(h)- \\\"groß\\\" (Gutt.-Verb. wie bei g(h)enus, eg(h)om, ghe : gho); meǵ- : mǵ-. Ai. mahānt-, av. mazant- \\\"groß\\\", ai. mah-, av. maz- ds. ... Komp. Sup. ai. mahiyas-, mahiṣṭha-, av. mazyah-, mazišta-; ai. mahas-, av. mazah- n. \\\"Größe\\\" ... av. mazan- \\\"Größe, Erhabenheit\\\" (s. Bartholomae Wb. 1156f.)'\"},\n        {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. meg-\", \"stance\": \"supports\", \"note\": \"'meg-. Great. 1. Germanic suffixed form *mik-ila- ... 2. Suffixed form *mag-no- in Latin magnus ... 7. Suffixed form *meg-a-l- in Greek megas ... 8. Variant form *megh- in Sanskrit mahā-, mahat-, great: MAHARAJAH ... [Pok. meg(h)- 708.]'\"},\n        {\"src\": \"SYN\", \"where\": \"Buck 12.55 'LARGE, BIG (GREAT)', pp. 878-880\", \"stance\": \"supports\", \"note\": \"'1. IE *meg-, *megh-. Walde-P. 2.257 f. ... Grk. megas ...; Lat. magnus ...; Goth. mikils, ON mikill, OE micel ...; Skt. mah-, mahant-, Av. maz-, mazant-; Arm. mec; Alb. madh; Hitt. [mekkis]'\"},\n        {\"src\": \"IEC\", \"where\": \"Mann s.v. meǵ- (IEC.txt line 10468)\", \"stance\": \"supports\", \"note\": \"'meǵ- (məǵ-) \\\"great, big\\\". Cf. meǵəlos, māǵ- (3). WP II, 257' — note that Mann himself cross-refers to the 'long' root māǵ-, and closes 'The consonantism of Hitt. mekkis, and of Skt. mahá-, etc. is problematical'\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan / Old Persian\",\n          \"words\": \"maz, mazant; maz-yah, mathi-yah; maz-išta; mazah, mazan\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Four of the six forms are secure. Av. maz- adj. 'gross, von hervorragender Bedeutung' (Gathic, only in oblique cases; Bartholomae col. 1157, 'ai. mah-') and mazant- 'gross, geräumig, gewaltig' (col. 1158, 'ai. mahānt-') are the positive; mazyah- / mazah- adj. 'der grössere, gewaltigere' is the comparative ('Komp. zu maz-, mazant-', col. 1158) and matches Nourai's 'maz-yah'; mazah- n. 'Grösse, Umfang' (col. 1158, 'ai. mahas-') and mazan- n. 'Grösse, Erhabenheit' (col. 1157) are the abstracts, i.e. Nourai's 'mazah, mazan : size, greatness'. Walde-Pokorny II 257 and Pokorny 708 list exactly this set, including 'av. mazyah-, mazišta-'. Two entries need qualifying. (a) 'mathi-yah' is not an attested Avestan or Old Persian word: it is Nyberg's reconstruction of the South-West comparative, 'OP *maθan-, comp. *maθyah-, sup. maθišta-' (Manual of Pahlavi II, glossary p. 133), and Mo'in copies it as پارسی باستان *maθ(i)yah- (Borhan p. 2058 fn. 7). (b) The θ/s forms are assigned by Bartholomae, Kent and Buck to a different root: since PIE *ǵʰ gives Avestan z and Old Persian d, while PIE *ḱ gives Avestan s and Old Persian θ, the attested OP maθišta- 'greatest' and Av. mas- 'lang', masan-, masah-, masyah-, masišta- belong to *meh₂ḱ- 'long' (Gk. makrós, mēkos, māssōn, mēkistos; Lat. macer) — Nourai's own root 'Mâk: long', which his note here tells the reader to compare. So the node as drawn mixes an impeccable *meǵh₂- set with one reconstructed form from the other family.\",\n          \"derivation_fa\": \"چهار صورت از شش صورتِ این جعبه بی‌گمان درست است. اوستایی maz- «بزرگ، سرآمد» (گاهانی، تنها در حالت‌های غیرفاعلی؛ بارتولومه ستون ۱۱۵۷، برابر با mah- سنسکریت) و mazant- «بزرگ، فراخ، نیرومند» (ستون ۱۱۵۸، برابر mahānt- سنسکریت) صورت‌های مثبت‌اند؛ mazyah-/mazah- «بزرگ‌تر، نیرومندتر» صفت برتر است («صفت تفضیلیِ maz-, mazant-»، ستون ۱۱۵۸) و همان «maz-yah» نورایی است؛ mazah- «بزرگی، گستره» (ستون ۱۱۵۸) و mazan- «بزرگی، شکوه» (ستون ۱۱۵۷) هم اسم‌های معنی‌اند، یعنی همان «mazah, mazan: بزرگی» نمودار. والده‌ـپوکورنی جلد ۲ ص ۲۵۷ و پوکورنی ص ۷۰۸ درست همین مجموعه را با mazyah-, mazišta- می‌آورند. اما دو نکته: نخست، «mathi-yah» واژه‌ای اوستایی یا پارسی باستانِ گواهی‌شده نیست، بلکه بازساختِ نیبرگ برای صفت تفضیلی جنوب‌غربی است (*maθyah-, واژه‌نامهٔ پهلوی، ص ۱۳۳) که معین هم آن را در حاشیهٔ برهان ص ۲۰۵۸ نقل کرده است. دوم، بارتولومه و کنت و باک صورت‌های s/θ را به ریشهٔ دیگری می‌بندند: چون *ǵʰ هندواروپایی در اوستایی z و در پارسی باستان d می‌دهد و *ḱ در اوستایی s و در پارسی باستان θ، پس maθišta- پارسی باستان و mas-, masyah-, masišta- اوستایی از *meh₂ḱ- «دراز» (یونانی makrós, mēkos, mēkistos و لاتین macer) اند ــ همان ریشهٔ «Mâk: دراز» خودِ نورایی که یادداشتِ همین جعبه خواننده را به آن حوالت می‌دهد. پس این جعبه مجموعه‌ای بی‌عیب از *meǵh₂- را با یک صورتِ بازساختهٔ خانوادهٔ دیگر درهم آمیخته است: با احتیاط پذیرفتنی است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/m%C3%A9%C7%B5h%E2%82%82s\"],\n          \"ref_check\": [\n            {\"ref\": \"POK:708\", \"status\": \"supports\", \"note\": \"'Old Indic mahant-, Avestan mazant- \\\"big, large\\\", Old Indic mah-, Avestan maz- ds. ... Kompar. Superl. Old Indic mahīyas-, mahiṣṭha-, Avestan mazyah-, mazišta-; Old Indic mahas-, Avestan mazah- n. \\\"greatness, bulk, extent\\\" ... Avestan mazan- \\\"greatness, bulk, extent, grandeur\\\"' (POK_full.txt, block at line 58003, pp. 708-709)\"},\n            {\"ref\": \"KLN:958\", \"status\": \"partial\", \"note\": \"p. 958 is Klein's 'mega-' entry, which gives only the Greek/Latin/Germanic cognates; the Avestan forms are at his 'mickle' entry (KLN_1966.txt line 23807, pp. 975-977): 'fr. I.-E. base *meg(h)-, *məg-, \\\"great, large\\\", whence also OI. mah-, mahā-, mahat-, \\\"great\\\", mahas-, \\\"greatness\\\", Avestic maz-, mazant-, \\\"great\\\", mazah-, \\\"greatness\\\"'. So Nourai's Avestan set is in Klein, but on a different page.\"},\n            {\"ref\": \"SYN:878\", \"status\": \"partial\", \"note\": \"Buck 12.55 begins on p. 878 with the word table 'Av. mazant-, maz-, masan-; OPers. vazarka-' and §1 'IE *meg-, *megh- ... Skt. mah-, mahant-, Av. maz-, mazant-'; but the Iranian discussion on p. 880 §8 explicitly splits the two families: 'Av. masan- \\\"great, significant\\\", masit-, masita- \\\"great, large\\\", masyah- \\\"greater\\\", masišta-, OPers. maθišta- \\\"greatest\\\", beside masan- \\\"greatness, importance\\\", masah- \\\"length, size\\\", and mas- \\\"long\\\" : Grk. makrós \\\"long\\\" (12.57). Walde-P. 2.223. Barth. 1154 ff.'\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"cols. 1154-1158 (BRT.txt lines 20115-20250)\", \"stance\": \"partial\", \"note\": \"two separate lemma-families: 'j. mas- Adj. \\\"lang\\\" ... Ableit. mp. (Pü.) mas. gr. vgl. makrós. Vgl. masyah-, masišta-' (col. 1154); 'j. masišta-, p. maθišta- Adj. \\\"der grösste\\\" ... Superl. zu mas-. mp. (Pü.), np. mahist' (col. 1155); 'j. masyah- Adj. \\\"der grössere\\\" ... Kompar. zu mas-. mp. meh, np. mih; gr. māssōn' (col. 1156); against 'g. maz- Adj. \\\"gross\\\" ... ai. mah-' (col. 1157), 'g., j. mazan- n. \\\"Grösse, Erhabenheit\\\"' (col. 1157), 'j. mazant- Adj. \\\"gross, geräumig ...\\\" ai. mahānt-' (col. 1158), 'j. mazah- n. \\\"Grösse, Umfang\\\" ... ai. mahas-' and 'j., g. mazyah-, j. mazah- Adj. \\\"der grössere, gewaltigere\\\" ... Komp. zu maz-, mazant-' (col. 1158)\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. II p. 257\", \"stance\": \"supports\", \"note\": \"'Ai. mahānt-, av. mazant- \\\"groß\\\", ai. mah-, av. maz- ds. ... Komp. Sup. ai. mahiyas-, mahiṣṭha-, av. mazyah-, mazišta-; ai. mahas-, av. mazah- n. \\\"Größe\\\" ... av. mazan- \\\"Größe, Erhabenheit\\\"'\"},\n            {\"src\": \"KNT\", \"where\": \"Kent, Old Persian, lexicon p. 190 s.v. maθišta- (KNT.txt line 5761) and §887 (line 1150)\", \"stance\": \"contradicts\", \"note\": \"'maθišta- adj. \\\"greatest\\\", equal to \\\"crown prince\\\" in XPf ...: Av. masišta-, NPers. mahist, Gk. mēkistos \\\"longest\\\" ...; superl. to pIE *mak-ros, Gk. makros, Lt. macer \\\"thin\\\", pIE root *mak- (887) \\\"be long and slender\\\" + superl. suffix'; and 'pIE *mak- in OP maθišta \\\"greatest\\\", Av. masišta-'. Kent thus files the OP superlative — and with it Nourai's 'mathi-yah' — under 'Mâk', not under 'Meg'.\"},\n            {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II, glossary p. 133 s.v. mas\", \"stance\": \"partial\", \"note\": \"the only source that actually offers Nourai's 'mathi-yah': 'Av. (1154) mas-, masan-, comp. (1156) masyah-, sup. (1155) masišta-; OP *maθan-, comp. *maθyah-, sup. maθišta-' — but as a reconstruction of the *meh₂ḱ- family, not of maz-\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Pahlavi\",\n          \"words\": \"meh\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"The Pahlavi word is real — MacKenzie p. 58, 'meh [ms | M mhy, myh, N ~] great(er), old(er)', beside mas 'great, big' (p. 58) and mahist 'greatest' (p. 56) — but the standard Iranian handbooks do not derive it from Av. maz-/mazant-. Bartholomae files it under the other family: col. 1156, 'j. masyah- Adj. \\\"der grössere\\\" ... Kompar. zu mas-. — mp. meh, np. mih; gr. māssōn', and mas- itself he glosses 'lang' with 'gr. vgl. makrós' (col. 1154). Nyberg spells the whole derivation out (glossary p. 133 s.v. mas): 'Av. mas-, masan-, comp. masyah-, sup. masišta-; OP *maθan-, comp. *maθyah-, sup. maθišta-; hence in MIr.: NW mas (MPrth only adv.), comp. masātar, sup. masišt (MPrth msyšt), but SW *mah (not attested so far), comp. mahy, mēh (MPrs mhy) Paz. meh, mehe, mahi; NP mih (used as pos.), sup. mahist'. Two things clinch it phonologically: the Book Pahlavi spelling of meh is ⟨ms⟩, i.e. historically mas with s, not z; and OP maθišta- > MP mahist shows the regular θ > h before the cluster, which is where the h of meh comes from. Horn no. 999 and Hübschmann p. 34 agree. On the other side, Mo'in — the authority Nourai cites for the Persian box — gives exactly Nourai's arrow at Borhan p. 2058 fn. 7: 'پهلوی meh (بزرگتر)، پارسی باستان *maθ(i)yah-، ایرانی باستان *mazyah- «نیبرگ ص ۱۴۸»، اوستا mazyah- (بزرگتر)', and Aryanpur (p. 483) and Wiktionary follow him. So the arrow is defensible but minority; the majority of specialist sources place MP meh under Nourai's own other root, 'Mâk: long'.\",\n          \"derivation_fa\": \"واژهٔ پهلوی واقعی است ــ مکنزی ص ۵۸: «meh [املای ms | مانوی mhy, myh | فارسی نو مه] بزرگ‌تر، مسن‌تر»، در کنار mas «بزرگ» و mahist «بزرگ‌ترین» (ص ۵۶) ــ اما ایران‌شناسان بزرگ آن را از maz-/mazant- اوستایی نمی‌گیرند. بارتولومه در ستون ۱۱۵۶ می‌نویسد «masyah- صفت تفضیلیِ mas-، فارسی میانه meh، فارسی نو mih؛ یونانی māssōn» و mas- را در ستون ۱۱۵۴ «دراز» معنی می‌کند و با makrós یونانی می‌سنجد. نیبرگ (واژه‌نامه، ص ۱۳۳) همهٔ زنجیره را باز می‌کند: اوستایی mas-, masan-, masyah-, masišta-؛ پارسی باستان *maθan-, *maθyah-, maθišta-؛ و از این‌جا در ایرانی میانه: شمال‌غربی mas و جنوب‌غربی *mah با تفضیلی mahy/mēh و پازند meh و فارسی نو mih با عالی mahist. دو نکتهٔ آوایی سرنوشت‌ساز است: املای پهلوی کتابیِ meh یعنی ⟨ms⟩ با «س» است نه با «ز»؛ و maθišta- پارسی باستان که به mahist پهلوی رسیده نشان می‌دهد θ پیش از خوشه به h بدل می‌شود، و همین h در meh دیده می‌شود. هرن (شمارهٔ ۹۹۹) و هوبشمان (ص ۳۴) نیز همین را می‌گویند. در سوی دیگر، معین ــ همان مرجعی که نورایی برای جعبهٔ فارسی آورده ــ در حاشیهٔ برهان ص ۲۰۵۸ درست پیکان نورایی را می‌کشد و mazyah- اوستایی را نیای پهلوی meh می‌شمارد، و آریان‌پور (ص ۴۸۳) و ویکی‌واژه هم از او پیروی کرده‌اند. پس پژوهش امروزی این پیکان را رد می‌کند و بیشتر منابع تخصصی meh را زیر همان ریشهٔ دیگرِ خودِ نورایی، «Mâk: دراز»، می‌نشانند.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%D9%85%D9%87\"],\n          \"ref_check\": [\n            {\"ref\": \"(none cited)\", \"status\": \"not_checked\", \"note\": \"the Pahlavi box carries no refs= (page image data/verification/sources/refs/ocr/BOOK/325.png)\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"MacKenzie pp. 56, 58 (PHD.txt lines 444, 477)\", \"stance\": \"partial\", \"note\": \"'meh [ms | M mhy, myh, N ~] great(er), old(er)'; 'mahist [msst!, mhst! | M mhyst, N ~] greatest' — the word exists as charted, but the Book Pahlavi spelling ⟨ms⟩/⟨msst⟩ points to mas-, not maz-\"},\n            {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II, glossary p. 133 s.v. mas\", \"stance\": \"contradicts\", \"note\": \"'Av. (1154) mas-, masan-, comp. (1156) masyah-, sup. (1155) masišta-; OP *maθan-, comp. *maθyah-, sup. maθišta-; hence in MIr: ... SW *mah (not attested so far), comp. mahy, mēh ... Paz. meh, mehe, mahi; NP mih (used as pos.), sup. mahist ... Possibly, however, -s- was pronounced -h- throughout in SW'\"},\n            {\"src\": \"BRT\", \"where\": \"col. 1156 s.v. masyah-\", \"stance\": \"contradicts\", \"note\": \"'Kompar. zu mas-. — mp. meh, np. mih; gr. māssōn. — Pü.: mas'\"},\n            {\"src\": \"HRN\", \"where\": \"no. 999, p. 224\", \"stance\": \"contradicts\", \"note\": \"'999. mih \\\"gross\\\", mehist, mihīn, mihtar. ... ap. vergl. maθišta- \\\"grösster\\\"; aw. masyaŋh \\\"grösser\\\"; phlv. mas \\\"gross, grösser, grössest\\\", masist, mas(i)st ... masīh, mahist, pāz. meh (PPGL)'\"},\n            {\"src\": \"ARY\", \"where\": \"Aryanpur, Farhang-e rishe-hā, p. 483 s.v. مه/مهتر\", \"stance\": \"supports\", \"note\": \"the entry heads the Avestan line with MAZANT/MAZ- and puts Pahlavi MAS, MASIST beside Sanskrit MAH-, Greek MEGAS, Latin MAGNUS, Gothic MIKILS, English MICKLE/MUCH — i.e. Aryanpur, like Nourai, keeps the Persian words in the *meg- family\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Persian\",\n          \"words\": \"meh 2 «مه ٢»; mehast «مهست»; meznâ «مزنا»\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"Three words with three different pictures. (a) مه meh 'great(er)' is the direct continuation of MP meh; Hübschmann p. 34 sets up the decisive proportion 'np. mih \\\"gross\\\" : zd. masyah-, kih \\\"klein\\\" : zd. kasyah-' — Persian meh/keh are the pair of Avestan comparatives masyah-/kasyah-, which puts meh under *meh₂ḱ- 'long', not under *meǵh₂-; Horn no. 999 (the very page Nourai cites) gives the same set. Mo'in and Wiktionary keep Nourai's derivation (Av. mazyah- > MP meh > NP meh). (b) مهست: the printed page transliterates it 'mehast'; the reading the sources know is mehest/mahist — MP mahist (MacKenzie p. 56), Pāzand mahest, mahist (Hübschmann p. 210, note to Horn 999), OP maθišta-. It is meh + the superlative suffix -est, and Mo'in's own footnote at Borhan p. 2069 says just that: 'مهست از: مه (بزرگ) + ست (پسوند صفت عالی)، در اوستا mazišta- صفت عالی از maz ... است بمعنی مهترین', while Bartholomae col. 1155 and Kent p. 190 file the same superlative as masišta-/maθišta- under *māk-. (c) مزنا meznā 'balance, scale' is where the chart really fails: the word and gloss are exactly at Nourai's page — Borhan-e Qate' p. 2002, 'مزنا: بکسر اول و سکون ثانی و نون بالف کشیده، بلغت زند بمعنی ترازو باشد و بعربی میزان گویند' — but nothing there links it to 'great'. Mo'in's footnote reads 'مزنا maznâ, mazînâ، پهلوی tarâzûk (ترازو) «یونکر ص ۱۱۷»، قس: میزان (عر)': the Pāzand maznā/mazīnā glosses Pahlavi tarāzūk 'balance' in Junker's Frahang ī Pahlavīg p. 117, and Mo'in points to Arabic ميزان (root w-z-n 'to weigh'), i.e. to a 'weighing' and not a 'greatness' word. Nourai himself notes it 'was not found in MON' and refers the reader to 'Mâk'. No source supports meznā < *meǵh₂-.\",\n          \"derivation_fa\": \"سه واژه با سه سرنوشت. (الف) «مه» به معنی «بزرگ(تر)» بی‌واسطه ادامهٔ meh فارسی میانه است؛ هوبشمان در ص ۳۴ تناسبِ تعیین‌کننده‌ای می‌سازد: «فارسی نو mih : اوستایی masyah-، همان‌گونه که kih : kasyah-» ــ یعنی جفتِ «مه/که» فارسی همان جفتِ صفت‌های تفضیلی اوستایی masyah-/kasyah- است و «مه» را به ریشهٔ *meh₂ḱ- «دراز» می‌برد نه *meǵh₂-؛ هرن هم در همان صفحهٔ ۲۲۴ که نورایی ارجاع داده همین مجموعه را می‌آورد. در برابر، معین و ویکی‌واژه همان زنجیرهٔ نورایی (mazyah- اوستایی ← meh پهلوی ← «مه») را نگه می‌دارند. (ب) «مهست»: کتاب آن را «mehast» نویسه‌گردانی کرده، اما خوانشی که منابع می‌شناسند mehest/mahist است ــ mahist فارسی میانه (مکنزی ص ۵۶)، پازند mahest و mahist (هوبشمان ص ۲۱۰)، و maθišta- پارسی باستان. ساختِ آن «مه + ـِست (پسوند صفت عالی)» است و خودِ معین در حاشیهٔ برهان ص ۲۰۶۹ همین را می‌گوید و آن را با mazišta- اوستایی می‌سنجد، در حالی که بارتولومه (ستون ۱۱۵۵) و کنت (ص ۱۹۰) همان صفت عالی را به‌صورت masišta-/maθišta- زیر ریشهٔ «Mâk» می‌نشانند. (ج) «مزنا» جایی است که نمودار به‌راستی می‌لنگد: واژه و معنی درست در همان صفحه‌ای است که نورایی داده ــ برهان قاطع ص ۲۰۰۲: «مزنا ... بلغت زند بمعنی ترازو باشد و بعربی میزان گویند» ــ اما هیچ نشانی از پیوند با «بزرگی» نیست. حاشیهٔ معین می‌گوید: «مزنا maznâ, mazînâ، پهلوی tarâzûk (ترازو) «یونکر ص ۱۱۷»، قس: میزان (عر)»؛ یعنی maznā صورتی پازند است که در «فرهنگ پهلویگ» به‌جای tarāzūk «ترازو» آمده و معین آن را با «میزان» عربی (از ریشهٔ وزن) می‌سنجد، نه با واژه‌ای به معنی بزرگی. خودِ نورایی هم یادآور شده که «مزنا در معین یافت نشد» و خواننده را به ریشهٔ «Mâk» حوالت داده است. هیچ منبعی مزنا را از *meǵh₂- نمی‌گیرد؛ پژوهش امروزی این بخش را رد می‌کند.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%D9%85%D9%87\"],\n          \"ref_check\": [\n            {\"ref\": \"HRN:224\", \"status\": \"partial\", \"note\": \"Horn no. 999, p. 224 (HRN.txt leaf 246) has meh and mehist as charted — 'mih \\\"gross\\\", mehist, mihīn, mihtar' — but derives them from 'ap. vergl. maθišta- \\\"grösster\\\"; aw. masyaŋh \\\"grösser\\\"; phlv. mas ... masist, mahist, pāz. meh', i.e. from the *māk- family, not from maz-. Horn has no مزنا.\"},\n            {\"ref\": \"BQT:2058\", \"status\": \"supports\", \"note\": \"Borhan-e Qate' ed. Mo'in p. 2058 (vol. 4 scan pdf p. 141) s.v. مه: '... و بکسر اول و ظهور ثانی، بمعنی بزرگ باشد ۷ چه بزرگتر را مهتر خوانند'; Mo'in's fn. 7: 'پهلوی meh (بزرگتر)، پارسی باستان *maθ(i)yah-، ایرانی باستان *mazyah- «نیبرگ ص ۱۴۸»، اوستا mazyah- (بزرگتر). نیز پهلوی mas (بزرگ، بزرگتر، بزرگترین)، masist ... پازند meh، ارمنی mec (بزرگ) ... صیغهٔ عالی ... پازند mahest, mahist ... پارسی باستان *maθišta- است' — this is exactly Nourai's Avestan mazyah- → Pahlavi meh → Persian meh.\"},\n            {\"ref\": \"BQT:2002\", \"status\": \"partial\", \"note\": \"p. 2002 (vol. 4 scan pdf p. 85; page image at data/verification/sources/refs/ocr/BQT/2002.png, transcript at .../2002.vision.txt) has the headword and gloss — 'مزنا ٥ - بکسر اول و سکون ثانی و نون بالف کشیده. بلغت زند بمعنی ترازو باشد و بعربی میزان گویند' — but Mo'in's fn. 5 derives nothing from 'great': 'مزنا maznâ, mazînâ، پهلوی tarâzûk (ترازو) «یونکر ص ۱۱۷»، قس: میزان (عر)'\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien p. 34 (HUB.txt line 1122) and p. 210 (line 7490)\", \"stance\": \"contradicts\", \"note\": \"'np. mih gross : zd. masyah-, kih klein : zd. kasyah-'; and 'Np. mih \\\"gross\\\" = paz. meh Shk. 258, phl. mas, ap. ...'; also (line 3499) 'Zu paz. meh lautet der Superl. mahest, mahist'\"},\n            {\"src\": \"BQT\", \"where\": \"vol. 4 p. 2069 (pdf p. 152), Mo'in's fn. 4 on مهست\", \"stance\": \"supports\", \"note\": \"'مهست از: مه (بزرگ) + ست (پسوند صفت عالی)، در اوستا mazišta- صفت عالی از maz (= مه، بزرگ) است بمعنی مهترین ... پهلوی mahist' — supports both the word مهست and its analysis, and reads it mehest, not 'mehast'\"},\n            {\"src\": \"PHD\", \"where\": \"MacKenzie pp. 56, 58\", \"stance\": \"partial\", \"note\": \"'mahist ... greatest' and 'meh ... great(er), old(er)' give the Middle Persian ancestors of مه and مهست; no Pahlavi antecedent for مزنا (MacKenzie's word for 'balance' is tarāzūg)\"},\n            {\"src\": \"ARY\", \"where\": \"Aryanpur p. 483 s.v. مه / مهتر\", \"stance\": \"supports\", \"note\": \"keeps مه in the *meg- family (Avestan MAZANT/MAZ, Pahlavi MAS/MASIST, Sanskrit MAH-, Greek MEGAS, Latin MAGNUS, Gothic MIKILS, English MUCH/MICKLE, Hittite MEKKIS); no entry for مزنا\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Sanskrit\",\n          \"words\": \"mahâ; mahâ-râja\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Sanskrit mahā- 'great' is the compound-initial form of mah-/mahānt- (nom. mahān) < Proto-Indo-Iranian *maȷ́ʰa- < PIE *meǵh₂-; the Indic h is the regular reflex of the palatal aspirate *ǵʰ where Iranian has z (mah- : Av. maz-, mahānt- : Av. mazant-, mahas- : Av. mazah-). mahārāja- 'great king' is mahā- + rājan- 'king' (PIE *h₃rēǵ-), so Nourai's '☞Reg' cross-reference is right: Watkins's index reads 'MAHARAJAH meg-, reg-1'. AHD meg- §8: 'Variant form *megh- in Sanskrit mahā-, mahat-, great: MAHARAJAH, MAHARANI, MAHARISHI, MAHATMA, MAHAYANA, MAHOUT'.\",\n          \"derivation_fa\": \"سنسکریت mahā- «بزرگ» صورتِ آغازِ ترکیبِ mah-/mahānt- (فاعلی mahān) است، از هندوایرانی آغازین *maȷ́ʰa- و هندواروپایی *meǵh₂-؛ h هندی بازتاب منظم دمیدهٔ کامیِ *ǵʰ است، همان‌جا که ایرانی z دارد (mah- : maz-، mahānt- : mazant-، mahas- : mazah-). mahārāja- «شاه بزرگ» از mahā- + rājan- «شاه» (هندواروپایی *h₃rēǵ-) است؛ پس ارجاع نورایی به ریشهٔ Reg درست است و واتکینز نیز در نمایه می‌نویسد «MAHARAJAH: meg-, reg-1». واتکینز زیر meg- بند ۸ می‌آورد: «صورت گونهٔ *megh- در سنسکریت mahā-, mahat- «بزرگ»: MAHARAJAH, MAHATMA, MAHOUT ...». ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/m%C3%A9%C7%B5h%E2%82%82s\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 s.v. meg- §8: 'Variant form *megh- in Sanskrit mahā-, mahat-, great: MAHARAJAH, MAHARANI, MAHARISHI, MAHATMA, MAHAYANA, MAHOUT. [Pok. meg(h)- 708.]'; index 'MAHARAJAH meg-, reg-1', 'MAHATMA ātmen-, meg-'\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"pp. 708-709\", \"stance\": \"supports\", \"note\": \"'Old Indic mahant-, ... Old Indic mah-, ... Old Indic mahi n. sg. ..., as front part Old Indic mahā- ... Old Indic mahas- ... n. \\\"greatness, bulk, extent\\\"'\"},\n            {\"src\": \"KLN\", \"where\": \"p. 923 s.v. maharaja (KLN_1966.txt line 22566)\", \"stance\": \"supports\", \"note\": \"'maharaja, maharajah, n., the title of great Hindu princes. — OI. maharajah, \\\"a great king\\\", compounded of maha-, \\\"great\\\", and rājan, \\\"king\\\". See magnum and rajah'\"},\n            {\"src\": \"SYN\", \"where\": \"Buck 12.55 p. 878 §1\", \"stance\": \"supports\", \"note\": \"'Skt. mah-, mahant-, Av. maz-, mazant-' under IE *meg-, *megh-\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. II p. 257\", \"stance\": \"supports\", \"note\": \"'als 1. Zsglied ai. mahā-' — explicitly the compound-initial form Nourai charts\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Persian\",\n          \"words\": \"mahârâjeh «مهاراجه»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"A learned borrowing of Sanskrit/Hindi mahārāja into New Persian, taken over through the Indo-Persian usage of Mughal and later British India rather than inherited; Persian renders the final -a with -ه, giving mahārāje. Mo'in states the source in his notes to Borhan-e Qate' p. 2063: '«مهاراجه» سانسکریت mahā-rāja (شاه بزرگ، سلطان عظیم) «ویلیامز»؛ جزء اول مها بمعنی بزرگ و جزء دوم بمعنی پادشاه از ریشهٔ rāj بمعنی سلطنت کردن، شاه یا رئیس بودن، راهنمایی کردن، حکومت کردن «ویلیامز»' — citing Monier-Williams — and he adds that Asadi Tusi's Garshāsp-nāma already uses مهراج as the name of a particular Indian king ('شهی بود در هند مهراج نام'), so an older, orally mediated form مهراج preceded the modern bookish مهاراجه.\",\n          \"derivation_fa\": \"«مهاراجه» وام‌واژه‌ای کتابی از mahārāja سنسکریت/هندی است که از راه کاربرد فارسیِ هند (دورهٔ گورکانیان و سپس هندِ بریتانیا) به فارسی آمده، نه واژه‌ای موروثی؛ -a پایانی سنسکریت در فارسی به «ـه» بدل شده و mahārāje شده است. معین در حاشیهٔ برهان قاطع ص ۲۰۶۳ سرچشمه را روشن می‌گوید: «مهاراجه: سانسکریت mahā-rāja (شاه بزرگ، سلطان عظیم) «ویلیامز»؛ جزء اول مها بمعنی بزرگ و جزء دوم بمعنی پادشاه از ریشهٔ rāj بمعنی سلطنت کردن، شاه یا رئیس بودن»، و می‌افزاید که اسدی طوسی در «گرشاسب‌نامه» صورت کهن‌ترِ «مهراج» را نام پادشاهی معیّن در هند گرفته است («شهی بود در هند مهراج نام»). ادعای نورایی درست است.\",\n          \"sources\": [\"https://vajehyab.com/?q=%D9%85%D9%87%D8%A7%D8%B1%D8%A7%D8%AC%D9%87&d=moein\"],\n          \"ref_check\": [\n            {\"ref\": \"MON:4458\", \"status\": \"partial\", \"note\": \"the Mo'in lexicon entry (vajehyab) gives مهاراجه with the origin tag '[ سنس . ]' = Sanskrit — '(مَ جِ) [ سنس . ] (ص .) توانگر، ثروتمند' — which confirms the Sanskrit source, but the print page 4458 itself cannot be checked online (Mo'in's pagination is not mapped on vajehyab/abadis). Mo'in's own footnote in Borhan p. 2063 gives the fuller derivation.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BQT\", \"where\": \"vol. 4 p. 2063 (pdf p. 146), Mo'in's fn. on مهاراجه/مهراج\", \"stance\": \"supports\", \"note\": \"'«مهاراجه» سانسکریت mahā-rāja (شاه بزرگ، سلطان عظیم) «ویلیامز» ... جزء دوم بمعنی پادشاه از ریشهٔ rāj بمعنی سلطنت کردن ... این کلمه عنوان عمومی راجه‌های (پادشاهان) هندوستان است'\"},\n            {\"src\": \"MON\", \"where\": \"vajehyab, Mo'in s.v. مهاراجه\", \"stance\": \"supports\", \"note\": \"origin tag '[ سنس . ]' (Sanskrit)\"},\n            {\"src\": \"KLN\", \"where\": \"p. 923 s.v. maharaja\", \"stance\": \"supports\", \"note\": \"'OI. maharajah, \\\"a great king\\\", compounded of maha- and rājan' — the same compound analysis for the Western borrowing\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"Hindustani\",\n          \"words\": \"\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"The blank box is the Hindustani (Hindi-Urdu) relay through which English received the words: Hindi महाराजा mahārājā, महात्मा mahātmā, continuing Sanskrit mahārāja-, mahātman- with the usual Indo-Aryan loss of the -n stem and final -ā. Hobson-Jobson shows the word in Anglo-Indian use from the 18th-19th c. ('the Maharaja (Sindia)', Elphinstone's Diary 1808; 'the Maharaja of the Isles', Mas'udi as quoted; 'the Maharajah sent us ... dancing girls', Osborne, Court and Camp of Runjeet Singh 1838), which is the channel of the English forms; Klein and Watkins name only the Sanskrit stage, so the Hindustani step is an inference from the transmission history rather than a claim any of them makes explicitly.\",\n          \"derivation_fa\": \"این جعبهٔ خالی واسطهٔ هندوستانی (هندی‌ـاردو) است که انگلیسی واژه‌ها را از آن گرفته: هندی mahārājā و mahātmā، ادامهٔ mahārāja- و mahātman- سنسکریت با افتادن ستاک -n و -ā پایانی، چنان‌که در هندوآریایی نو معمول است. «هابسن‌جابسن» کاربرد این واژه را در انگلیسیِ هند از سدهٔ هجدهم و نوزدهم نشان می‌دهد («the Maharaja (Sindia)» در یادداشت‌های الفینستون ۱۸۰۸؛ «the Maharajah sent us ...» در سفرنامهٔ آزبورن ۱۸۳۸)، و همین راهِ ورودِ صورت‌های انگلیسی است. کلاین و واتکینز تنها مرحلهٔ سنسکریت را نام می‌برند، پس گامِ هندوستانی نتیجه‌گیری از تاریخ انتقال است نه ادعای صریح آنان. ادعای نورایی پذیرفتنی است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"(none cited)\", \"status\": \"not_checked\", \"note\": \"the Hindustani box has no refs=\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"HJB\", \"where\": \"Hobson-Jobson, quotations (HJB.txt lines 4406, 7891, 8367, 8792 — leaves 190-370 of the 1903 scan)\", \"stance\": \"partial\", \"note\": \"there is no headword MAHARAJA or MAHATMA in Hobson-Jobson; the word appears only inside quotations, e.g. '1808. — ... Some Sirdars put the Maharaja (Sindia) in dhurna' (Elphinstone's Diary) and '1838. — The Maharajah sent us in the evening a new set of dancing girls' (Osborne) — evidence for the Anglo-Indian channel but not an etymology\"},\n            {\"src\": \"AID\", \"where\": \"Whitworth, An Anglo-Indian Dictionary (grep 'maharaj')\", \"stance\": \"silent\", \"note\": \"only 'Maharaj' as part of personal names ('...virji Maharaj and Ayodya Prasadji Maharaj'); no headword\"},\n            {\"src\": \"KLN\", \"where\": \"p. 923 s.v. maharaja\", \"stance\": \"partial\", \"note\": \"derives the English word straight from 'OI.' (Old Indian = Sanskrit) without naming the modern Indic stage\"}\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"English\",\n          \"words\": \"maharajah, mahatma\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"maharajah entered English from Anglo-Indian usage (in English texts from the late 17th c., common from the 18th) < Hindi mahārājā < Sanskrit mahārāja- 'great king'. mahatma 'great-souled one' was popularised in English by the Theosophists in the 1880s and later became Gandhi's honorific; it is Sanskrit mahātman- = mahā- 'great' + ātman- 'breath, self, soul' — Klein: 'mahatma, n., great-souled, magnanimous. — OI. mahatman, \\\"great-souled\\\", compounded of mahāt-, \\\"great\\\", and ātmān, \\\"soul\\\". The first element is cogn. with L. magnus, \\\"great\\\"; see magnum ... For the second element see atman.' Watkins's index accordingly gives 'MAHARAJAH meg-, reg-1' and 'MAHATMA ātmen-, meg-'.\",\n          \"derivation_fa\": \"«maharajah» از راه کاربرد انگلیسیِ هند به انگلیسی راه یافته (در متون انگلیسی از پایان سدهٔ هفدهم و رایج از سدهٔ هجدهم)، از mahārājā هندی و mahārāja- سنسکریت «شاه بزرگ». «mahatma» «بزرگ‌جان» را انجمن تئوسوفی در دههٔ ۱۸۸۰ در انگلیسی رواج داد و سپس لقب گاندی شد؛ صورت سنسکریت آن mahātman- است، یعنی mahā- «بزرگ» + ātman- «دم، جان، خویشتن». کلاین می‌نویسد: «mahatma از mahatman سنسکریت، مرکب از mahāt- «بزرگ» و ātmān «جان»؛ جزء نخست هم‌ریشه با magnus لاتین است». نمایهٔ واتکینز نیز MAHARAJAH را زیر meg- و reg-1 و MAHATMA را زیر ātmen- و meg- می‌آورد. ادعای نورایی درست است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 s.v. meg- §8 lists MAHARAJAH and MAHATMA among the English derivatives of Sanskrit mahā-/mahat-; the ātmen- entry reads 'Sanskrit ātman, breath, soul: ATMAN; MAHATMA'\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"p. 921 s.v. mahatma (KLN_1966.txt line 22571) and p. 923 s.v. maharaja\", \"stance\": \"supports\", \"note\": \"'mahatma ... OI. mahatman, \\\"great-souled\\\", compounded of mahāt-, \\\"great\\\", and ātmān, \\\"soul\\\". The first element is cogn. with L. magnus, \\\"great\\\"; see magnum and cp. maharajah'\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985 word-index\", \"stance\": \"supports\", \"note\": \"'MAHARAJAH meg-, reg-1'; 'MAHATMA ātmen-, meg-'\"},\n            {\"src\": \"HJB\", \"where\": \"Hobson-Jobson, quotations\", \"stance\": \"partial\", \"note\": \"documents the Anglo-Indian currency of Maharaja/Maharajah in English from the 18th-19th c. but has no etymological entry\"}\n          ]\n        },\n        {\n          \"id\": 8,\n          \"lang\": \"Germanic\",\n          \"words\": \"mikila\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Proto-Germanic *mikilaz 'great' = the root *meǵ- plus an -ila- suffix (Watkins meg- §1, 'Germanic suffixed form *mik-ila-'); the Grimm shift turns *ǵ into k, and Gothic mikils, ON mikill, OS mikil, OHG mihhil (with the High German shift k > hh), OE micel/mycel are its reflexes. Nourai's 'mikila' is the stem without the Gothic nominative -s. Pokorny 708-709 lists the same set and notes 'Proto German *mikilaz probably with -lo suffix after leitils'.\",\n          \"derivation_fa\": \"ژرمنی آغازین *mikilaz «بزرگ» از ریشهٔ *meǵ- به‌همراه پسوند -ila- ساخته شده است (واتکینز زیر meg- بند ۱: «صورت پسونددارِ ژرمنی *mik-ila-»)؛ بر پایهٔ قانون گریم، *ǵ به k بدل شده و بازمانده‌های آن گوتی mikils، نورس کهن mikill، ساکسون کهن mikil، آلمانی علیای کهن mihhil (با ابدال k > hh در آلمانی علیا) و انگلیسی کهن micel/mycel است. صورتی که نورایی آورده ستاک بی‌نشانهٔ فاعلی گوتی است. پوکورنی در صص ۷۰۸ـ۷۰۹ همین مجموعه را می‌آورد و می‌گوید *mikilaz احتمالاً پسوند -lo- را به قیاسِ leitils گرفته است. ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/m%C3%A9%C7%B5h%E2%82%82s\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 s.v. meg- §1: 'Germanic suffixed form *mik-ila- in: a. Old English micel, mycel, great: MUCH; b. Old Norse mikill, great: MICKLE'\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"pp. 975-977 s.v. mickle\", \"stance\": \"supports\", \"note\": \"'mickle, adj., great, much (archaic or dial.) — ME. mikel, muchel, fr. OE. micel, mycel, \\\"great, big, many\\\", rel. to OS. mikil, ON. mikill, OHG. mihhil, Goth. mikils, fr. I.-E. base *meg(h)-, *məg-, \\\"great, large\\\"'\"},\n            {\"src\": \"POK\", \"where\": \"pp. 708-709\", \"stance\": \"supports\", \"note\": \"'Gothic mikils \\\"big, large\\\". Old High German mihhil. Old Saxon mikil. Old English micel. Old Icelandic mikell ds., Old English mycel, Proto German *mikilaz probably with -lo suffix after leitils'\"},\n            {\"src\": \"SYN\", \"where\": \"Buck 12.55 p. 878 §1\", \"stance\": \"supports\", \"note\": \"'Goth. mikils, ON mikill, OE micel, mycel, ME mikel, etc. (NE dial. mickle and muckle), OHG mihhil, MHG michel'\"}\n          ]\n        },\n        {\n          \"id\": 9,\n          \"lang\": \"English\",\n          \"words\": \"much, more\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"'much' is right: ME muchel/michel > much (with loss of the final syllable), from OE myċel/miċel < PGmc *mikilaz; the fuller form survives dialectally as mickle/muckle. Watkins meg- §1a: 'Old English micel, mycel, great: MUCH'. 'more' is not from this root. OE māra 'greater' is the suppletive comparative used beside miċel, but it continues PGmc *maizōn-/*maiz- (Goth. maiza, mais; ON meiri; OHG mēro; G. mehr), which Watkins files under a different entry, mē-3 'Big' ('1. Suffixed (comparative) form *mē-is- in Germanic *maizōn- in Old English māra, greater, and māre (adverb), more: MORE. 2. Suffixed (superlative) form *mē-isto- ... MOST. [Pok. 4. mē- 704]'), and Etymonline states the same: 'Old English mara ... from Proto-Germanic *maiz ... from PIE root *meis-, perhaps from a root *me- \\\"big\\\"'. Buck 12.55 §2 likewise keeps the *mē-/*mo- group (Goth. maiza, mais, maists; Ir. mór, W. mawr) apart from IE *meg-. Klein does compare 'Avestic mazja, \\\"greater\\\"' in his 'more' entry, and Mann (IEC) puts the Brittonic comparative 'more' under *meǵ-, which is presumably why Nourai drew the arrow — but even on Klein's view 'more' is not a descendant of Germanic *mikilaz, only a functional comparative to it. So of the two English words in this box, one is inherited from the parent form and one is not.\",\n          \"derivation_fa\": \"«much» درست است: از انگلیسی میانه muchel/michel و انگلیسی کهن myċel/miċel، از ژرمنی آغازین *mikilaz، با افتادن هجای پایانی؛ صورت کامل‌تر در گویش‌ها به شکل mickle/muckle مانده است، و واتکینز نیز زیر meg- بند ۱الف همین را دارد. اما «more» از این ریشه نیست: māra انگلیسی کهن «بزرگ‌تر» صفت تفضیلیِ جانشین برای miċel بوده، اما ادامهٔ *maizōn-/*maiz- ژرمنی است (گوتی maiza/mais، نورس کهن meiri، آلمانی mehr) که واتکینز آن را زیر سرواژهٔ دیگری، mē-3 «بزرگ» (پوکورنی ۷۰۴)، آورده است، و اتیمانلاین هم می‌گوید «از *maiz ژرمنی، از ریشهٔ *meis-، شاید از *me- «بزرگ»». باک هم در بند ۱۲٫۵۵ خانوادهٔ *mē-/*mo- (گوتی maiza, maists؛ ایرلندی mór؛ ولزی mawr) را از *meg- جدا نگه می‌دارد. کلاین در مدخل more «mazja اوستایی» را هم‌ریشه می‌شمارد و مان صفت تفضیلی بریتونیِ «more» را زیر *meǵ- می‌آورد ــ گمان می‌رود همین سبب پیکانِ نورایی شده باشد ــ اما حتی در دیدگاه کلاین هم «more» فرزندِ *mikilaz ژرمنی نیست، بلکه صفت تفضیلیِ کارکردیِ آن است. پس از دو واژهٔ این جعبه یکی موروثی از صورت مادر است و دیگری نه؛ پژوهش امروزی این بخش را رد می‌کند.\",\n          \"sources\": [\"https://www.etymonline.com/word/more\"],\n          \"ref_check\": [\n            {\"ref\": \"(none cited)\", \"status\": \"not_checked\", \"note\": \"the English box has no refs=; the parent Germanic box carries AHD, whose meg- entry lists only MUCH and MICKLE for Germanic\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.vv. meg- §1 and mē-3\", \"stance\": \"contradicts\", \"note\": \"meg- yields 'MUCH ... MICKLE'; but 'mē-3. Big. ... 1. Suffixed (comparative) form *mē-is- in Germanic *maizōn- in Old English māra, greater, and māre (adverb), more: MORE. 2. Suffixed (superlative) form *mē-isto- in Germanic *maista- in Old English mǣst, most: MOST. [Pok. 4. mē- 704.]'; the index reads 'MORE mē-3'\"},\n            {\"src\": \"WEB\", \"where\": \"etymonline s.v. more\", \"stance\": \"contradicts\", \"note\": \"'Old English mara \\\"greater, relatively greater, more, stronger, mightier\\\", used as a comparative of micel \\\"great\\\" ... from Proto-Germanic *maiz ... from PIE root *meis-, perhaps from a root *me- \\\"big\\\"'\"},\n            {\"src\": \"SYN\", \"where\": \"Buck 12.55 pp. 878-879 §2\", \"stance\": \"contradicts\", \"note\": \"section 2 'IE *mē-, *mo-' collects 'NIr. mór, W. mawr ... Goth. maiza, mais, maists \\\"greater, greatest\\\" ... (NE more, most not used of size)' separately from section 1 'IE *meg-, *megh-'\"},\n            {\"src\": \"KLN\", \"where\": \"p. 977 s.v. more\", \"stance\": \"partial\", \"note\": \"'ME. more, fr. OE. māra ... rel. to ... Goth. maiza ... and cogn. with Avestic mazjā, \\\"greater\\\", OIr. mór, mār, \\\"great\\\" ... Oscan mais, \\\"more\\\"' — Klein links the group to the Avestan comparative, but still as a separate *mē-is- formation, not as a derivative of *mikilaz\"}\n          ]\n        },\n        {\n          \"id\": 10,\n          \"lang\": \"Latin\",\n          \"words\": \"maximus\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Latin maximus 'greatest' < *mag-samo-s (Watkins) / *meǵ-semo-s (Pokorny), the superlative built on the same stem as magnus 'great' (< *meǵ-no-) and the comparative maior (< *meǵ-yōs-); the -x- is the regular Latin spelling of the cluster from *-g-s-. Pokorny 708: 'Latin magnus \\\"big, large\\\" (*meg-nó-s), Kompar. mag-is \\\"more\\\", maior \\\"greater\\\" (*meg-jōs), Superl. maximus (*meg-semo-s)'. Watkins meg- §4: 'Suffixed (superlative) form *mag-samo- in Latin maximus, greatest: MAXIM, MAXIMUM'. The Latin -a- is the regular outcome of the zero-grade *m̥ǵh₂-.\",\n          \"derivation_fa\": \"لاتین maximus «بزرگ‌ترین» از *mag-samo-s (واتکینز) یا *meǵ-semo-s (پوکورنی) است، صفت عالیِ برساخته بر همان ستاکی که magnus «بزرگ» (از *meǵ-no-) و صفت تفضیلی maior (از *meǵ-yōs-) از آن‌اند؛ حرف x همان املای منظم خوشهٔ برآمده از *-g-s- در لاتین است. پوکورنی در ص ۷۰۸ می‌نویسد: «لاتین magnus (از *meg-nó-s)، تفضیلی magis و maior (از *meg-jōs)، عالی maximus (از *meg-semo-s)». واتکینز نیز زیر meg- بند ۴: «صورت عالیِ پسوندی *mag-samo- در لاتین maximus». واکهٔ a در لاتین بازتاب منظم پایهٔ صفرِ *m̥ǵh₂- است. ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/m%C3%A9%C7%B5h%E2%82%82s\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 s.v. meg- §4: 'Suffixed (superlative) form *mag-samo- in Latin maximus, greatest: MAXIM, MAXIMUM'\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"pp. 708-709\", \"stache\": \"supports\", \"stance\": \"supports\", \"note\": \"'Latin magnus \\\"big, large\\\" (*meg-nó-s), Kompar. mag-is \\\"more, in a higher degree\\\", maior \\\"greater\\\" (*meg-jōs), Superl. maximus (*meg-semo-s); in addition maiestas \\\"greatness, grandeur, dignity, majesty\\\" (*meg-jes-tat-)'\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. II 257 ff. (with WH. II 4 f., 10 ff. cited in Pokorny)\", \"stance\": \"supports\", \"note\": \"the Latin material of the root is treated at WP II 257 ff., the reference Pokorny gives for it\"},\n            {\"src\": \"KLN\", \"where\": \"p. 958 s.v. mega-\", \"stance\": \"supports\", \"note\": \"'Gk. megas ... which is cogn. with L. magnus, \\\"great, large, much, abundant\\\"'\"}\n          ]\n        },\n        {\n          \"id\": 11,\n          \"lang\": \"French\",\n          \"words\": \"\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"The blank box is French maximum, a learned borrowing of the Latin neuter maximum into French scientific and mathematical usage (18th c.), from which Persian took it — as Mo'in's origin tag [فر.] on ماکسیمم shows. The French form, not the Latin or the English one, is what the Persian pronunciation māksimom reflects.\",\n          \"derivation_fa\": \"این جعبهٔ خالی همان maximum فرانسوی است، وام‌واژه‌ای دانشورانه از خنثای لاتین maximum که در سدهٔ هجدهم به کاربرد علمی و ریاضی فرانسوی راه یافت و فارسی از آن گرفت ــ چنان‌که برچسب «[فر.]» معین برای «ماکسیمم» نشان می‌دهد. تلفظ فارسی māksimom بازتاب همان صورت فرانسوی است، نه لاتین و نه انگلیسی. ادعای نورایی درست است.\",\n          \"sources\": [\"https://vajehyab.com/?q=%D9%85%D8%A7%DA%A9%D8%B3%DB%8C%D9%85%D9%85&d=moein\"],\n          \"ref_check\": [\n            {\"ref\": \"(none cited)\", \"status\": \"not_checked\", \"note\": \"the French box has no refs=\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"vajehyab, Mo'in s.v. ماکسیمم\", \"stance\": \"supports\", \"note\": \"'(مُ) [فر.] (اِ.) = ماکزیمم : حداکثر، بیشترین حد، بزرگترین مقدار در مجموعه ای از مقادیر، بیشینه (فره )' — the tag [فر.] names French as the immediate source, which is what the empty French box asserts\"},\n            {\"src\": \"KLN\", \"where\": \"p. 958 s.v. mega-, and s.v. magnum\", \"stance\": \"partial\", \"note\": \"gives the Latin family but not the French relay; Klein's English 'maximum' is taken straight from Latin\"}\n          ]\n        },\n        {\n          \"id\": 12,\n          \"lang\": \"Persian\",\n          \"words\": \"mâxîmom «ماکسیمم»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"ماکسیمم māksimom is a 20th-c. French loan in Persian. Mo'in: '(مُ) [فر.] (اِ.) = ماکزیمم : حداکثر، بیشترین حد، بزرگترین مقدار در مجموعه ای از مقادیر، بیشینه (فره )' — French origin, glossed with the Arabic-Persian calque حداکثر and the Academy's Persian equivalent بیشینه. The doublet spelling ماکسیمم / ماکزیمم reflects the French [maksimɔm] with the s/z hesitation usual in Persian rendering of European loans, and the final -om (not -um) shows the French and not the Latin pronunciation.\",\n          \"derivation_fa\": \"«ماکسیمم» وام‌واژه‌ای فرانسوی از سدهٔ بیستم در فارسی است. معین می‌نویسد: «(مُ) [فر.] (اِ.) = ماکزیمم: حداکثر، بیشترین حد، بزرگترین مقدار در مجموعه‌ای از مقادیر، بیشینه (فره)» ــ یعنی خودِ او آن را فرانسوی می‌داند و با گَردهٔ عربیِ «حداکثر» و برابر فرهنگستانیِ «بیشینه» معنی می‌کند. دوگانگی املای «ماکسیمم/ماکزیمم» بازتاب تلفظ فرانسوی [maksimɔm] و همان تردید همیشگیِ س/ز در نوشتنِ وام‌واژه‌های اروپایی است، و پایانهٔ -om (نه -um) نشان می‌دهد که تلفظ فرانسوی مأخذ بوده نه لاتین. ادعای نورایی درست است.\",\n          \"sources\": [\"https://vajehyab.com/?q=%D9%85%D8%A7%DA%A9%D8%B3%DB%8C%D9%85%D9%85&d=moein\"],\n          \"ref_check\": [\n            {\"ref\": \"MON\", \"status\": \"supports\", \"note\": \"Nourai cites MON without a page; the Mo'in lexicon text on vajehyab has ماکسیمم with the tag [فر.] (French) and the gloss حداکثر — exactly the claim the chart makes\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"vajehyab, Mo'in s.v. ماکسیمم\", \"stance\": \"supports\", \"note\": \"'[فر.] ... = ماکزیمم : حداکثر، بیشترین حد ... بیشینه'\"},\n            {\"src\": \"BQT\", \"where\": \"BQT_v4_pages.txt, grep 'ماکسیمم'\", \"stance\": \"silent\", \"note\": \"no hits, as expected for a 20th-c. European loan in a 17th-c. dictionary\"}\n          ]\n        },\n        {\n          \"id\": 13,\n          \"lang\": \"English\",\n          \"words\": \"magnitude, majesty, major, magnum, master, maximum, May, mayor\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"All eight are Latin, and all eight stand in Watkins's meg- entry. magnitude < L magnitūdō; magnum < neut. of magnus; major < L maior (*meǵ-yōs-); majesty < L maiestās (*meǵ-yes-tāt-, via OF majesté); maximum < L maximus; mayor < OF maire < L maior; May < L Maius (mēnsis), from the goddess Maia, Watkins's '*mag-ya-, \\\"she who is great\\\"'; master < both OE mæġester and OF maistre, from L magister, which Klein analyses as '*mag-is-teros ... formed with double comparative suff. from the stem of L. magnus'. Nourai's Latin box gives only maximus as the exemplar, so several of these English words descend from magnus/maior/magister rather than from maximus itself — a compression of the chart, not an error of substance.\",\n          \"derivation_fa\": \"هر هشت واژه لاتین‌اند و هر هشت در مدخل meg- واتکینز آمده‌اند: magnitude از magnitūdō؛ magnum از خنثای magnus؛ major از maior (از *meǵ-yōs-)؛ majesty از maiestās (از *meǵ-yes-tāt-، به واسطهٔ فرانسوی کهن majesté)؛ maximum از maximus؛ mayor از maire فرانسوی کهن و آن از maior؛ May از Maius (mēnsis) که به نام ایزدبانو Maia است، همان *mag-ya- «آن که بزرگ است» در دستگاه واتکینز؛ و master هم از mæġester انگلیسی کهن و هم از maistre فرانسوی کهن، از magister لاتین که کلاین آن را *mag-is-teros می‌داند، یعنی برساخته بر ستاکِ magnus با دو پسوند تفضیلی. جعبهٔ لاتینِ نورایی تنها maximus را نمونه آورده، پس چند واژه از این فهرست در واقع از magnus/maior/magister می‌آیند نه از maximus؛ این فشرده‌سازیِ نمودار است نه خطای محتوایی. ادعای نورایی درست است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"(none cited)\", \"status\": \"not_checked\", \"note\": \"no refs= on the English box; the parent Latin box carries AHD, which covers all eight words\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. meg- §§2-6\", \"stance\": \"supports\", \"note\": \"'*mag-no- in Latin magnus: MAGNATE, MAGNITUDE, MAGNUM ...; *mag-yos-: a. Latin major: MAJOR, MAJOR-DOMO, MAJORITY, MAJUSCULE, MAYOR; b. Latin majestās: MAESTOSO, MAJESTY; c. Latin magister: MAESTRO, MAGISTERIAL ... MASTER; *mag-samo- in Latin maximus: MAXIM, MAXIMUM; *mag-ya-, \\\"she who is great\\\", in Latin Maia, name of a goddess: MAY'\"},\n            {\"src\": \"KLN\", \"where\": \"p. 918 s.v. master (KLN_1966.txt line 23081)\", \"stance\": \"supports\", \"note\": \"'Both OE. mæġester and OF. maistre derive fr. L. magister ... L. magister stands for *mag-is-teros, which is formed with double comparative suff. from the stem of L. magnus, \\\"great\\\" ... See mickle and cp. magnum, megalo-'\"}\n          ]\n        },\n        {\n          \"id\": 14,\n          \"lang\": \"Greek\",\n          \"words\": \"megas\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Greek μέγας, fem. μεγάλη, neut. μέγα 'great' < PIE *méǵh₂s (neut. *méǵh₂ > μέγα, the laryngeal giving the -a); the oblique and feminine stem μεγαλο- was built to μέγα (Pokorny notes it was formed 'aus dem Notstand', on the model of χαμαλός 'low'). Comparative Ionic-Doric μέζων / Attic μείζων, superlative μέγιστος. Watkins meg- §7: 'Suffixed form *meg-a-l- in Greek megas (stem megal-), great: MEGA-, MEGALO-; ACROMEGALY, ALMAGEST, OMEGA'.\",\n          \"derivation_fa\": \"یونانی μέγας (مادینه μεγάλη، خنثی μέγα) «بزرگ» از هندواروپایی *méǵh₂s است؛ خنثای *méǵh₂ به μέγα رسیده و همان حنجره‌ای است که a را می‌دهد. ستاک غیرفاعلی و مادینهٔ μεγαλο- بر پایهٔ μέγα ساخته شده است ــ پوکورنی می‌گوید «از ناچاری» و به قیاسِ χαμαλός «پست». صفت تفضیلی در ایونی و دوری μέζων و در آتیکی μείζων، و صفت عالی μέγιστος است. واتکینز زیر meg- بند ۷ می‌نویسد: «صورت پسونددارِ *meg-a-l- در یونانی megas (ستاک megal-): MEGA-, MEGALO-, ACROMEGALY, ALMAGEST, OMEGA». ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/m%C3%A9%C7%B5h%E2%82%82s\"],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 s.v. meg- §7: 'Suffixed form *meg-a-l- in Greek megas (stem megal-), great: MEGA-, MEGALO-; ACROMEGALY, ALMAGEST, OMEGA'\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"pp. 708-709\", \"stance\": \"supports\", \"note\": \"'gr. μέγας, μεγάλη, μέγα \\\"big, large\\\" ... Kompar. Ionian Doric Arcadian μέζων from *μέγjων (Attic μείζων after χείρων), Superl. μέγιστος'\"},\n            {\"src\": \"KLN\", \"where\": \"p. 958 s.v. mega-\", \"stance\": \"supports\", \"note\": \"'Fr. Gk. μέγας, fem. μεγάλη, neut. μέγα, \\\"great, large, mighty\\\", which is cogn. with L. magnus ... Goth. mikils, OE. micel, mycel'\"},\n            {\"src\": \"SYN\", \"where\": \"Buck 12.55 p. 878 §1\", \"stance\": \"supports\", \"note\": \"'Grk. μέγας, gen. μεγάλου, NG μεγάλος (nom. normalized fr. stem of other cases)'\"},\n            {\"src\": \"IEC\", \"where\": \"Mann s.v. meǵ-\", \"stance\": \"supports\", \"note\": \"'Gk. mégas, n: méga, adj. \\\"big, great\\\"; méga, adv.; cf. meízōn \\\"bigger\\\"; mégistos \\\"biggest\\\"'\"}\n          ]\n        },\n        {\n          \"id\": 15,\n          \"lang\": \"English\",\n          \"words\": \"omega, mega-\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"omega is Greek ὦ μέγα 'the great (i.e. long) o', the Byzantine name of the 24th letter, opposed to omicron ὂ μικρόν 'small o'; it entered English through Latin in the 16th c. and acquired the figurative sense 'the end' from Revelation 1:8. mega- is the learned combining form of μέγας, productive in English scientific coinages (megaphone, megalith), and since the metric conference of 1873 the SI prefix for 10⁶ (megawatt, megavolt). Klein: 'omega, n., the twenty-fourth and last letter of the Greek alphabet. — Gk. ὦ μέγα, \\\"the great (i.e. long) o\\\". Cp. omicron'; 'mega-, before a vowel meg-, combining form meaning \\\"large, great\\\" (in physics it is used in the meaning of \\\"a million times\\\", e.g. megavolt) — Fr. Gk. μέγας'.\",\n          \"derivation_fa\": \"«omega» همان ὦ μέγα یونانی است، «اُی بزرگ (یعنی کشیده)»، نامِ بیزانسیِ بیست‌وچهارمین حرف الفبای یونانی در برابر ὂ μικρόν «اُی کوچک» (omicron)؛ در سدهٔ شانزدهم از راه لاتین به انگلیسی رسید و معنی مجازی «پایان» را از مکاشفهٔ یوحنا ۱:۸ گرفت. «mega-» نیز صورت ترکیبیِ دانشورانهٔ μέγας است که در واژه‌سازی علمی انگلیسی زایاست (megaphone، megalith) و از کنفرانس متریکِ ۱۸۷۳ پیشوند دستگاه SI برای ۱۰⁶ شده است (megawatt، megavolt). کلاین می‌نویسد: «omega ... از یونانی ὦ μέγα «اُی بزرگ (یعنی کشیده)»؛ قس omicron» و «mega- ... از یونانی μέγας». ادعای نورایی درست است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"(none cited)\", \"status\": \"not_checked\", \"note\": \"no refs= on the English box; the parent Greek box carries AHD, whose meg- §7 lists both MEGA- and OMEGA\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"pp. 958 s.v. mega- and 999 s.v. omega (KLN_1966.txt lines 23369 area, 26237)\", \"stance\": \"supports\", \"note\": \"'omega, n., the twenty-fourth and last letter of the Greek alphabet. — Gk. ὦ μέγα, \\\"the great (i.e. long) o\\\". Cp. omicron'; 'mega-, before a vowel meg-, combining form meaning \\\"large, great\\\" ... e.g. megavolt = a million volts. — Fr. Gk. μέγας ... Cp. also omega, acromegaly, almagest'\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. meg- §7\", \"stance\": \"supports\", \"note\": \"'Greek megas (stem megal-), great: MEGA-, MEGALO-; ACROMEGALY, ALMAGEST, OMEGA'\"}\n          ]\n        }\n      ]\n    }\n  ]\n}\nJSONEOF\npython3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-325.json > /dev/null && echo \"JSON OK\""
}
```


### [2026-09-07T16:15:36.917Z] TOOL RESULT

```
JSON OK
```


## [2026-09-07T16:15:42.330Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 - <<'EOF'\nimport re\np='data/verification/page-325.json'\ns=open(p,encoding='utf-8').read()\ns2=s.replace('\"stache\": \"supports\", \"stance\": \"supports\"','\"stance\": \"supports\"')\nassert s2!=s\nopen(p,'w',encoding='utf-8').write(s2)\nEOF\ngrep -c 'stache' data/verification/page-325.json; python3 -m json.tool data/verification/page-325.json >/dev/null && echo OK\npython3 tools/verify_check.py 325"
}
```


### [2026-09-07T16:15:43.789Z] TOOL RESULT

```
0
OK
nodes verified: 25/25
node verdicts: {'confirmed': 20, 'transcription_suspect': 1, 'plausible': 1, 'disputed': 3}
root verdicts: {'confirmed': 2}
ref checks: {'partial': 7, 'supports': 13, 'not_checked': 11}
books consulted: {'supports': 54, 'partial': 11, 'silent': 3, 'contradicts': 8} | by book: {'KLN': 15, 'WLD': 6, 'POK': 6, 'AHD': 6, 'MON': 5, 'BRT': 4, 'HRN': 4, 'PHD': 4, 'BQT': 4, 'SYN': 4, 'HUB': 3, 'NYB': 3, 'WEB': 3, 'IEC': 2, 'ARY': 2, 'HJB': 2, 'SOD': 1, 'KNT': 1, 'AID': 1}
```


## [2026-09-07T16:16:07.276Z] AGENT

Done. `verify_check.py 325` reports **0 PROBLEM lines**, 25/25 nodes.

**Page 325 (book p. 295) — 2 entries, 25 nodes**
- Root verdicts: confirmed 2 (Medhyo = PIE \*médʰyos, Pok. 706-707; Meg/Megh = PIE \*méǵh₂s, Pok. 708-709 — the double "Meg, Megh" reproduces Pokorny's own `meǵ(h)-`)
- Node verdicts: confirmed 20, plausible 1, disputed 3, transcription_suspect 1
- Ref checks: supports 13, partial 7, not_checked 11 (all the not_checked are boxes with no `refs=` at all)

**Flagged items**
- `disputed` — Meg/Megh #2 Pahlavi *meh*: Bartholomae (col. 1156 "Kompar. zu mas-. — mp. meh, np. mih"), Nyberg (glossary p. 133), MacKenzie, Horn 999, Hübschmann p. 34, Buck 880 and Kent p. 190 all derive MP *meh*/*mahist* from Av. **mas-, masyah-, masišta- / OP maθišta-** = PIE \*meh₂ḱ- 'long' (Nourai's own "Mâk" root), not from *maz-*. Book Pahlavi spells *meh* ⟨ms⟩. Mo'in (BQT 2058), Aryanpur and Wiktionary do follow Nourai.
- `disputed` — Meg/Megh #3 Persian *meh 2 / mehast / meznâ*: same split for مه/مهست; and **مزنا has no support at all** — BQT 2002 has the word ('balance', "in the Zand tongue"), but Mo'in's footnote gives Pahlavi *tarāzūk* citing Junker's Frahang ī Pahlavīg p. 117 and points to Arabic میزان, nothing about 'great'. Nourai's own note already concedes it.
- `disputed` — Meg/Megh #9 English *much, more*: *much* is fine; **"more" is from PIE \*meh₁- / \*mē-is-** (Watkins mē-3, Pok. 704; Etymonline; Buck §2) via Gmc \*maizōn-, not from Gmc \*mikilaz.
- `transcription_suspect` — Medhyo #7 Latin: book prints **"medi-terrâneous : in land sea"**; the Latin word is *mediterrāneus* 'inland' (-ous is an English suffix) and the gloss garbles "inland (sea)". `error_in: book` — the extraction is faithful.
- `plausible` — Meg/Megh #1 Av./OP: *maz, mazant, maz-yah, mazah, mazan* all confirmed (BRT 1157-1158, WP II 257); but **"mathi-yah" is unattested** — it is Nyberg's reconstruction OP \*maθyah-, and the s/θ forms belong to the \*meh₂ḱ- family.

**Extraction errors: none.** I checked the page image (`site/pages/325.jpg`, copy at `data/verification/sources/refs/ocr/BOOK/325.png`) against the JSON — every form, gloss, ref, cross-reference and note matches the print, including "medi-terrâneous", "mehast" (standard reading is *mehest/mahist*) and the Sogdian backtick in "myd`n".

Also saved: `data/verification/sources/refs/ocr/BQT/2002.vision.txt` (Mo'in's مزنا footnote, read from the page image), and 9 web pages archived via `fetch_source.py`.
