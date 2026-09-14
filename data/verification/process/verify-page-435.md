# Verification process log — verify-page-435


## [2026-09-14T01:24:55.439Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 435 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-435.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-435.json. Write /home/sfmqrb/git/rishe/data/verification/page-435.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 435` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-14T01:24:56.424Z] AGENT

I'll start by reading the instructions.


## [2026-09-14T01:24:57.259Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-14T01:24:57.279Z] TOOL RESULT

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


## [2026-09-14T01:24:57.774Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-435.txt"
}
```


### [2026-09-14T01:24:57.819Z] TOOL RESULT

```
1	=== PDF page 435 (book page 405) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Sed : to sit, to place; also to place a step, to go  (refs POK:884,887; KLN:1075)  PART 1
4	#1 (parent #0) [Avestan] refs=POK:884-887; FFD:78 | had, hd, zd, šas 2 : to sit ; šâdayeiti : sits ; ni-šâdaiti : sits down ☞Nî 1 ; ni-šasti : mating ☞Nî 1
5	  #2 (parent #1) [Persian] refs=BQT:2145-7; HRN:231 | nešastan «نشستن ( نشین )» : to sit down ; našim «نَشیم ( نشیمن )» : place where birds sit down, nest
6	#3 (parent #0) [Avestan] refs=HRN:71; FFD:43 | sad, sand : settlement, agreement ; upa-sad : (good for) agreement ☞Upo ; avara-sad : settle down, satisfy ☞Au 2
7	  #4 (parent #3) [Persian] refs=BQT:406 | pasandîdan «پسندیدن» : to admire, select ; p s n d, d l p s n d ; xorsand «خرسند» : satisfied, happy
8	#5 (parent #0) [Avestan] refs=POK:886-887 | nazdyô : sat very close, near ; nazd-îštâ, nazdištâ : closest, first ☞Isto ; âsna : near ; âsnaoiti : to get close to
9	  #6 (parent #5) [Persian] refs=BQT:2117-33; HRN:230 | nazd «نزد ( نزدیک )» : near ; naxost «نخست» : closest, first
10	#7 (parent #0) [Avestan] refs=POK:885-887 | hastra : assembly, meeting ; hadiš : residence, palace ; pasuš-hasta : ? ; apo-had : to put away ☞Apo
11	#8 (parent #0) [Avestan] refs=POK:885-887 | syazd : to step back ; sîždyamna : recess ; sîždyô : to give up ; sîždra : shy
12	#9 (parent #0) [Old Persian] refs=KNT:212,213 | had : to sit ; had-iš : seat, palace ; ni-had : set down, established ☞Nî 1
13	#10 (parent #0) [Greek] refs=AHD | hodos : way, path ; ana-hodos : up way (for electric charges), anode ; kata-hodos : down way (for electric charges), cathode ; met-hodos : (path) for proceeding, method ; epi-eis-hodos : going in besides, episode ☞En
14	  #11 (parent #10) [French] refs=None | 
15	    #12 (parent #11) [Persian] refs=MON:2782,3797 | ânod «آند» : "up way" ; kâtod «کاتد» : "down way" ; metod «متد» : "proceeding way"
16	  #13 (parent #10) [English] refs=None | anode, cathode, method, episode, period
17	
```


## [2026-09-14T01:25:00.593Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-435.json",
 "description": "Read source JSON for page 435"
}
```


### [2026-09-14T01:25:00.632Z] TOOL RESULT

```
{
  "pdf_page": 435,
  "book_page": 405,
  "entries": [
    {
      "root": {
        "name": "Sed",
        "lang": "Indo-European",
        "refs": "POK:884,887; KLN:1075",
        "gloss": "to sit, to place; also to place a step, to go"
      },
      "part": 1,
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:884-887; FFD:78",
          "words": [
            {"translit": "had, hd, zd, šas 2", "gloss": "to sit", "script": null},
            {"translit": "šâdayeiti", "gloss": "sits", "script": null},
            {"translit": "ni-šâdaiti", "gloss": "sits down", "script": null, "see": ["Nî 1"]},
            {"translit": "ni-šasti", "gloss": "mating", "script": null, "see": ["Nî 1"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT:2145-7; HRN:231",
          "words": [
            {"translit": "nešastan", "gloss": "to sit down", "script": "نشستن ( نشین )"},
            {"translit": "našim", "gloss": "place where birds sit down, nest", "script": "نَشیم ( نشیمن )"}
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "که ای بلند نظر شاهباز سدره نشین - نشیمن تو نه این کنج محنت آباد است",
            "poet": "Hâfez"
          }
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Avestan",
          "refs": "HRN:71; FFD:43",
          "words": [
            {"translit": "sad, sand", "gloss": "settlement, agreement", "script": null},
            {"translit": "upa-sad", "gloss": "(good for) agreement", "script": null, "see": ["Upo"]},
            {"translit": "avara-sad", "gloss": "settle down, satisfy", "script": null, "see": ["Au 2"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Persian",
          "refs": "BQT:406",
          "words": [
            {"translit": "pasandîdan", "gloss": "to admire, select", "script": "پسندیدن"},
            {"translit": "p s n d, d l p s n d", "gloss": null, "script": null},
            {"translit": "xorsand", "gloss": "satisfied, happy", "script": "خرسند"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:886-887",
          "words": [
            {"translit": "nazdyô", "gloss": "sat very close, near", "script": null},
            {"translit": "nazd-îštâ, nazdištâ", "gloss": "closest, first", "script": null, "see": ["Isto"]},
            {"translit": "âsna", "gloss": "near", "script": null},
            {"translit": "âsnaoiti", "gloss": "to get close to", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "Persian",
          "refs": "BQT:2117-33; HRN:230",
          "words": [
            {"translit": "nazd", "gloss": "near", "script": "نزد ( نزدیک )"},
            {"translit": "naxost", "gloss": "closest, first", "script": "نخست"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:885-887",
          "words": [
            {"translit": "hastra", "gloss": "assembly, meeting", "script": null},
            {"translit": "hadiš", "gloss": "residence, palace", "script": null},
            {"translit": "pasuš-hasta", "gloss": "?", "script": null},
            {"translit": "apo-had", "gloss": "to put away", "script": null, "see": ["Apo"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:885-887",
          "words": [
            {"translit": "syazd", "gloss": "to step back", "script": null},
            {"translit": "sîždyamna", "gloss": "recess", "script": null},
            {"translit": "sîždyô", "gloss": "to give up", "script": null},
            {"translit": "sîždra", "gloss": "shy", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 0,
          "lang": "Old Persian",
          "refs": "KNT:212,213",
          "words": [
            {"translit": "had", "gloss": "to sit", "script": null},
            {"translit": "had-iš", "gloss": "seat, palace", "script": null},
            {"translit": "ni-had", "gloss": "set down, established", "script": null, "see": ["Nî 1"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 0,
          "lang": "Greek",
          "refs": "AHD",
          "words": [
            {"translit": "hodos", "gloss": "way, path", "script": null},
            {"translit": "ana-hodos", "gloss": "up way (for electric charges), anode", "script": null},
            {"translit": "kata-hodos", "gloss": "down way (for electric charges), cathode", "script": null},
            {"translit": "met-hodos", "gloss": "(path) for proceeding, method", "script": null},
            {"translit": "epi-eis-hodos", "gloss": "going in besides, episode", "script": null, "see": ["En"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 10,
          "lang": "French",
          "refs": null,
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 11,
          "lang": "Persian",
          "refs": "MON:2782,3797",
          "words": [
            {"translit": "ânod", "gloss": "\"up way\"", "script": "آند"},
            {"translit": "kâtod", "gloss": "\"down way\"", "script": "کاتد"},
            {"translit": "metod", "gloss": "\"proceeding way\"", "script": "متد"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 13,
          "parent": 10,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "anode, cathode, method, episode, period", "gloss": null, "script": null}
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


## [2026-09-14T01:25:01.371Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-14T01:25:01.457Z] TOOL RESULT

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


## [2026-09-14T01:25:38.622Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','KLN','HRN','BQT','KNT','MON','FFD','AHD','BRT','PHD','NYB','HUB','CHEUNG','WLD','IEC','SYN','ARY']:\n    v=d.get(k)\n    print('==',k,json.dumps(v,ensure_ascii=False)[:600])\n\""
}
```


## [2026-09-14T01:25:39.213Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"sed-\" POK_full.txt | head -40"
}
```


### [2026-09-14T01:25:39.738Z] TOOL RESULT

```
== POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_
== KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h
== HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 
== BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118
== KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt", "page_offset": "leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \\
== MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په
== FFD {"title": "Mohsen Abolghasemi, Fe'l-ha-ye Farsi-ye Dari, Qoqnus, Tehran 1374/1995", "kind": "local_scan_ocr", "url": "https://asmaneketab.ir/product/کتاب-ماده-های-فعلهای-فارسی-دری-محسن-اب/ -> https://dl.eliteraturebook.com/app/public/attachments/6925d29630b83.PDF (free PDF site; grey)", "lookup_hint": "Searched archive.org (Persian/Latin titles, author), ketabnak, noorlib, general web (pdf/download): nothing; only a related paid e-book 'واژگان زبان فارسی دری' (fidibo). ketabnak.com/book/45024 is a different book (فهرست فعلهای فارسی).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/s
== AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,
== BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1
== PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-
== NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf
== HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) fol
== CHEUNG null
== WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039
== IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 
== SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves
== ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it
```


### [2026-09-14T01:25:39.789Z] TOOL RESULT

```
5600:the movement, Avestan na-zdyah-. Old Indie nedJyas- " closer '(' * moved near '); root sed- 
29104:Mitganger ', to root sed-, as also Indo Germanic *ozdos, gr. 6^o<; "bough' as " ansitzendes 
29449:the Asper after £5- {*sed-)7 
62325:unavoidable! compulsory! inevitable; a natural law; true ' see below sed-. 
63051:See also: see below sed-. 
64353:sitting in the trunk ', s. prefix e-, d-and sed-^s\\!. 
72366:Root / lemma: sed- 
72392:Wissmann Nom. postv. 112, 1); Old Irish sa(i)did {*se(i)did), 'sitzt', Fut. seiss{*sed-s-ti), 
72404:Lithuanian *sedm/and sedziu, sedime{*sed-). Inf. sedet/'s'\t', participle Perf. sed^s {as 
72427:*sed-to-\'r\ Old Indie sa//a- "gesessen', Avestan pasus-hasta-m. " hurdle (*settlement) 
72430:bench '; *sed-t/"\n Old Indie satt/-'6as Sitzen', n/-satt/-'6as Sitzen, seat', Avestan ni-sasti- 
72443:noun actionis sed-'\n: Old Indie Akk. sadam, Dat. sade, with ©-extension in Latin sedes 
72447:"idle' = Old Irish de/dds. (/-inflection secondary), to deess^ sluggishness ' {*de-sed-ta); 
72478:lok. eAAq KoGsSpa Hes. = Latin selia {*sed-ia) 'stool, seat', gall, sedion 'seat', Gothic 
72479:sitis, Old English setin.; Old High German sezzaim. ' seat' {*sed-io-y, Lower Serbian 
72488:from *sedu-io-n.; besides (in Aryan geneuertes = renamed, has changed???) *sed-tiom\n 
72534:servant' from *o-zdos "*Beisitzer'; or rather to B. *sed-7 
72539:B. *sed-\v\ the meaning "go', from connection with Prafixen originated. 
72560:Root / lemma: sed-: (to sit) derived from Root/ lemma: es-: (to sit). 
81278:derived from Root / lemma: sed- : (to sit). 
88989:see Root / lemma: sed- : to sit.
```


## [2026-09-14T01:25:44.960Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '72360,72570p' POK_full.txt"
}
```


### [2026-09-14T01:25:45.017Z] TOOL RESULT

```
See also: s. also sano-s. 

Page(s): 876 



Root / lemma: sed- 

Meaning: to sit 

Grammatical information: originally only aoristisch, punctual "sich place' (Old Indie), later 

as duratives stative verb with e-suffix "sit' (Latin Germanic Balto-Slavic) 



Material: 1 . Old Indie sad-{satsi, asadat, Pf. sasada, sedima, sedivas-, compare Avestan 
hazdya-t 0^t)\ 

Avestan ap. had- (with Praverbien) 'sich place' {n/safjhast/ ior *nisasti)\ Kaus. 
(lengthened grade) Old Indie sadayati^ places ', Avestan ni-sadayeiti ^ aWows niedersitzen, 
places low, base', ap. n/yasadayaml setzte'; 

Armenian nst/m's\t, put myself (perhaps„/b-Praes. *ni-zdjd)\ hecanim^s\\. auf, reite' {c 
from d+ aor. -s); 

gr. E^opai 'sit, put myself (Aor. elaa Hom., saoai Pind.); Kaus. oSsTv, 65c(v ' sell ', 
actually 'place' (Specht KZ. 62, 51); 

Latin sedeo, -ere, sed/^sW (present due to of originally aufterpras. stem sede-; Perf. 
from *se-zd-ai), Umbrian sers/tu ^ se6etd' , ze/e/'sedens', a/7o'e/"sesi/s/'intersiderit', Latin 
sedo, -are' calm, appease ' (perhaps = Middle Low German saten' calm, appease ', 
Wissmann Nom. postv. 112, 1); Old Irish sa(i)did {*se(i)did), 'sitzt', Fut. seiss{*sed-s-ti), 
adsu/d/'sc\r\\ebt auf, verzogert, halt auf (Kaus. *sodeJet, otherwise through Denom. 
suidigud 'place' verdrangt); cymr. seddu'sW; 

Maybe alb. Geg me sh/te'to sell in a place' 

Old Icelandic s/t, Inf. s/f/a, Old Saxon s/ff/u, Old High German s/zzu 's\t' (= s^opai, ni- 
£^u); Gothic sitan\s probably reshuffling from *sitjan\ Praet. sat, setum), Kaus. Gothic 
satjan. Old Icelandic setia. Old High German sezzen 'place' {*sodeJd); 

Maybe alb. shet/t'\Na\k slowly over a place' 

Lithuanian *sedm/and sedziu, sedime{*sed-). Inf. sedet/'s'\t', participle Perf. sed^s {as 
Old Prussian 5/(yo/7s'sitzend', Old Church Slavic sedb). Old Church Slavic sezdg, sedeti 
'sit'; besides ein Old Czech sedeti {: Latin sedere); Lithuanian sedu, sesti, Latvian sest 
{*sestei) 'sich place'. Old Church Slavic sesti 6s. (present s§dg, see below), Kaus. saditi 
{*sddejd) 'place, pflanzen', Lithuanian sodinu sodinti'p\ace, pflanzen'; 

Maybe alb. sodit 'observe, watch from a place' 

Old Prussian with {*d) saddinna 'p\aces'; Old Church Slavic sgdg'put myself (Inf. sesti) 
based on auf secondary nasalization of *sedg{= Lithuanian sedu); also Old Prussian 
syndens, sinda (nj ts ' s\tzend' shows nasalization; s. Kuiper Nasalpras. 192 f., where Old 
Indie asandl"seat' to as/e 'sitzt' (above S. 342 f.) placed wird; 



2. forms with /-reduplication: 

Old Indie 5/0(3// "sitzf (for *sTdati\xov(\ redupl. *si-zd-ati, with replacement from p'through 
o' after sad-)\ Avestan h/6a/t/' s\tzt'; gr. T^u) 'put' = Latin s/dd'put myself ( *si-zdd), Umbrian 
s/s/i/ 'consTdito', 5/7ofe/'5/5/^'*intersTdito' {*si-zd-etdd)\ 

3. nominal formation: 

*sed-to-\'r\ Old Indie sa//a- "gesessen', Avestan pasus-hasta-m. " hurdle (*settlement) 
for small cattle', Latin ob-sessus etc., Old Icelandic Old English sessm. "seat', compare 
also Lithuanian participle sestas and Lithuanian sostasm. "seat'. Old Prussian sostoi. " 
bench '; *sed-t/"\n Old Indie satt/-'6as Sitzen', n/-satt/-'6as Sitzen, seat', Avestan ni-sasti- 
"Begattung', Latin sess/o"Sitzung', from *sessis. Old Indie sattar-m. the "Sitzer', Latin ad-, 
ob-, possessor, 

maybe alb. {*sess), shesh'p\a\r\, flatness, square'. 

Old Indie sadas-n. "seat, place, abode, residence', gr. zboq n. "seat'; Avestan Old pers. 
/7ao''/5-"Wohnsitz, palace' (Indo Germanic -as or -/is); lengthened grade Old Icelandic ssefr 
{*satiz) n. "seat, Sommersitz, Aim'; Old Irish s/o'"peace', originally n. es-stem, identical with 
sTdu. es-stem "dwelling gottlicher creature ' (compare engl. settlement); 

o-grade: Old Irish suideu. {*sod/om) "seat, sit' = Latin sc»//^/77 "throne'; 

noun actionis sed-'\n: Old Indie Akk. sadam, Dat. sade, with ©-extension in Latin sedes 
f. "seat' {sedibus= Lithuanian Inf. sede-ti-A PI. sedi-me), Umbrian sersi^\v\ sede'; noun 
agentis as 2. compound part: Old Indie apsu-sad-^\he in den Wassern dwells ', Avestan 
mai5ydi-sa5am (Akk.) "the in the middle dwells '; Latin prae-ses "Vorsitzender', de-ses 
"idle' = Old Irish de/dds. (/-inflection secondary), to deess^ sluggishness ' {*de-sed-ta); 
with Latin 5i//?s/(:y/i//77"Unterstutzung' compare Old Irish fothaem. n. "base' from *upo- 
sodjom, to Old Irish suide; 

Old Icelandic se/n. " enlarged bottom', PI. syl?/ "dwelling'. Old English se/n. "seat, lair, 
stall, sundown, sunset, descent of the sun ', Old High German sezu. "seat, seat, buttocks, 
Belagerung'; 

cymr. seddi. "seat' {*seda); heddm. "peace' {*sedos); Middle Breton hezafr cease' , 
mcorn. hathyds.; gor-sedd' throne, hill'; eistedd^S\\2.ev\\ abret. estid^ that may be sat on, 
a seat, bench, stool, chair ' ( *eks-dT-sedo-), gall, essedum, -a " 2-wheeled war chariot ' 



(with *en-, compare gr. £v-£5pov, £v-£5pa " ambush, lurking place, hideout ', Old Irish in- 
dess/'d' to sit in, settle on '; skyth. VN 'Eaar|56v£c;); 

Albanian karrige : Bolognese canga : Bresciano cadrega : Paduan carega : Piemontese 
cadrega: Portuguese cadeira: Provengal cadiero: Sardinian (Limba Sarda Unificada) 
cadrea : Sardinian Campidanesu cadira : Sardinian Logudoresu cadrea ; catrea : Scots 
Gaelic cathair: Irish cathaoir: Welsh cadair: Breton kador: Triestino carega: Valencian 
cadira : Venetian carega : Zeneize carega : Catalan cadira : Corsican carrega ; carrea : 
Furlan (^^oV'ee (common Slavic alb. -e- > -Je-, -a- > -Ja-, ) : Galician cadeira : Modern 
Greek Kap£KAa : Latin cathedra : Lombardo Occidentale cadrega : Occitan carrea : Greek 
£5pa; Ka9£5pa ' chair'. 

gr. £5pa " sitting-place, seat, abode, freq. in pi., etc.; esp. of the gods, sanctuary, 
temple, in pi., quarters of the sky in which omens appear, sitting, session of a council, etc., 
when he rose from the sitting, seat, breech, fundament, Hp. Aph.5.22, etc.; of birds and 
animals, rump ' Old Icelandic setru. 'seat ': 

lok. eAAq KoGsSpa Hes. = Latin selia {*sed-ia) 'stool, seat', gall, sedion 'seat', Gothic 
sitis, Old English setin.; Old High German sezzaim. ' seat' {*sed-io-y, Lower Serbian 
sedio'seat'; but Old Church Slavic seoVo 'saddle' is *sedbio, compare Old Church Slavic 
o-sedbiafi 'satte\n', Armenian e// 'place' (in addition auch/e//"place'); 

Old Saxon sethalxw. 'Sitzen, seat', Dat. sedie'{to) sundown, sunset, descent of the sun 
', Old High German setiial, sedaiu. m. 'seat, Wohnsitz, site' (Indo Germanic *5e//c»- from 
*sedtlo)\ therefrom Old High German s/ic/z/o 'agricola'. Middle High German sidilen 
'siedein'; Germanic *sadula-\v\: Old Icelandic sgduil. Old English sadoi. Old High German 
satui, s5/5/'saddle' is East Indo Germanic loanword (?); compare above Slavic *sedhlo 
from *sedu-io-n.; besides (in Aryan geneuertes = renamed, has changed???) *sed-tiom\n 
Avestan iiasfra-n. 'congregation, meeting' = Old Indie sattra-n. ' celebration, festival'. 

Maybe alb. s/o/'throne' : Latin soiium' throne'. 

lengthened gradee formations: Old Indie sada- m. ' das Sitzen ', sao'//7-'(aufsitzend =) 
reitend, equestrian ' (compare also russ. vsadnik' equestrian '), Old Icelandic satt 
'Hinterhalt', Old English 5^/ds., Old High German -saza{\n place names) 'Wohnsitz', 
Middle High German sazei. 'seat, domicile, Hinterhalt', yioAdj. Old Icelandic s^tr' 
suitable to seat ', see above whereof 5^//under 'seat, hay heap ' = Old High German 
gisazi'seat, buttocks '; Proto Baltic *sdsta-'seat' {*sdd-to-) in Lithuanian sostasm. 'seat'. 



Old Prussian sostoi. " bench ', compare Old Icelandic sessn. "seat' above S. 885; Old 
Church Slavic pre-seda^ a snare, trap '; 

with d/cymr. /75M/ofa'' light' = corn, hueth^ peaceful ' (Loth RC 36, 162); 

cymr. san/oto'" depth, Absinken'; 

Old Icelandic Old English so/'smut' ("Angesetztes'); 

Lithuanian suodziaiP\., Latvian suddrej/" smut', Bulgarian sazdat, Czech saze {*sddJo-) 
unclear Old Irish sOidei., cymr. huddygl, bret. huzeF srwui'; Old Church Slavic sadh 
"Pflanzung' {*sddu-)\ 

4. More or less verdunkelte compositions: 

Old Indie nedJyas-^ nearer, closer', nedistha-^ uachsV = Avestan nazdyoadv. '(spacial) 
nearer, closer an-', nazd/sta-'t\r\e nachste', Avestan asna-M]. " near' {*6-zd-na-, 
participle Perf. Pass., compare full grade Old Indie asanna-^ near '). (under the influence 
of common Celtic -ns-, -nt- > -nn-). 

ni-zd-os, -o/77'nest' (prefix /?/■ "low, base', or 'ein-' as "place zum Nieder- or Einsitzen'): 
Old Indie n/da-m. n. 'Ruheplatz, lair', Armenian n/st^ position, seat, Residenz', Latin 
nldus'nest', Middle Irish net^nest', cymr. nyth^nest, dwelling', corn, ne/d, bret. nez, neiz 
ds.. Old High German Old English nestn. "nest'; 

Maybe zero grade of alb. Geg ( *ne/d) me ndejt'to sit' : corn, ne/d'nest'. 

with popular etymology Umgestaltungen Lithuanian lizdas, Latvian ligzda. Old Church 
Slavic ^/7ezo'c»"nest'; identical prefix in Old Indie nisTdati^ places sich', Avestan nishidaiti, 
ap. niyasadayam, Armenian nstim, see above; 

o-zato5"(ansitzender) twig, branch, bough', see there {ozcfo-s), also gr. o^oc; " fellow, 
servant' from *o-zdos "*Beisitzer'; or rather to B. *sed-7 

pi-s(ejd- ^darauis\\.zen = press': Old \nd'\c pFdayat/ {*p/-zd-e/d) "presses, oppressed, 
afflicts' (Perf. pipTde, pTda^Dxuck, pain'), gr. nis^u) "push, press' (*ni-a£5ju)). 

B. *sed-\v\ the meaning "go', from connection with Prafixen originated. 

Old Indie ^-sao'- "hintreten, hingehen, reach ', ^/-55o'-"sich zurSeite begeben, 
disappear', Avestan ^^^(^^/^///"verscheucht (makes go away, pass over'), Avestan apa- 



had-'s\c\\ wegsetzen, dodge ', asnaoiti{ *d-zd-neu-tl) "geht heran' (see 886 asna-); gr. 
oSoq 'way', 65iTr|<; 'Wanderer', 65£uu) 'wandere'; Old Church Slavic chodt ' gait ', choditi 
'go'; ablaut, sbdb^ gone, departed, left; dead; lost '; Slavic ch-irovc\ Indo Germanic s- 
probably at first behind pri- and u- originated. 

Maybe alb. {*ouda) alb. i/o'/7e"way, journey', udhetof travel ', udhetar^ wanderer, traveller 



Here perhaps as compound with one to Pron. Ro-, Rio- {above S. 609) respective Adv. 
*Rje-: Avestan syazo'- 'zuriJcktreten vor, abandon ', sTzdyamna^ zuriJckweichende ', sizdyo 
'aufgebend', sTzdra-^ shy' and Latin cedo {*Re-zd-d) 'schreite einher; retreat, give after', as 
well as /7ecesse'notwendig', whether (?) from *ne-Rezd-t/-s'es is kein Ausweichen'. 

Root / lemma: sed-: (to sit) derived from Root/ lemma: es-: (to sit). 

References: WP. II 483 ff., WH. II 507 ff., 511, EM2 917 ff., Trautmann 248, 258 ff., 273. 
Page(s): 884-887 

Root / lemma: seg-1 

Meaning: to sow 

Note: only Latin and Celtic
```


## [2026-09-14T01:26:10.335Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT had ===\" && grep -n \"pasuš\\|pasus\\.hasta\\|hastra\\|haδiš\\|hadiš\" BRT.txt | head -30 && echo \"=== BRT syazd ===\" && grep -n \"syazd\\|sīžd\\|sizd\" BRT.txt | head -20 && echo \"=== BRT nazdyō ===\" && grep -n \"nazdyō\\|nazdišta\\|nazdyo\" BRT.txt | head -20"
}
```


### [2026-09-14T01:26:10.429Z] TOOL RESULT

```
=== BRT had ===
14708:•  j.  ^SriS-hastra-'*  n.  'Versammlung  von dreien':  yä  bii.hastrim  sravayeiä  . .  *rsm
29673:enüassen':  "anya.tkaliais^)  näirika pairi      "='"'  Etymologie  bringt  Dst.  ZA.  /.  «3- xsudra  fraipharTsaiW^  Nik.  7.  •  j.hastra- n. 'Versammlung' uzw.  solcher,
=== BRT syazd ===
5383:•  j.,  g-  auruna-  'wild,  fenis,  saevus': maSsahe  kihrpa  'na^e  Yt.  l4- 23;  —  'na/a gairisiicö  sizdraca  ravascarätö  "die  wilden (Tiere),  die  in  den  Bergen  hausen,  und die  scheuen,  die  in  den  Ebenen  streifen" Yt.  ^36;  —  alityS  mos  aia  syasdal{sA.) yavaf  ahmal  'nä  xra/strä  ".  .  soweit  als vor  uns  die  wilden  Raubtiere"  \.34. 9.
5487:•  j.,  g.  'araS-a-  n.  'Sache'  usw.  i)  in  altem Sinn  'Rechtsstreit'  (nur  Ableit).  2)  'woran einem  gelegen  ist,  Angelegenheit,  Anliegen': -liJil  vöizdyäi  (sd.)  kamahya  tJm  mSt  data  .. Y.4;.i3;  —  fr3  mUl  /ravsizdsm  -Ja  ia ya  voha  ^yavSi  manaaha  "nehmt  wahr meine  Angelegenheiten,  die  ich  betreibe, O  VM."  "^.33.8;  —  avat  hl  asli  masyö *i?m  yal . .  "das  ist  fiir  sie  das  grössere Anliegen,  dass  , ,"  V.7.71.  3)  'was einem     obliegt,     gebührt,     Obliegenheit,
6925:i_fj  'mäi  gam  .  .  hSmJalat  at  höi  vSstrüi (sd.)  ..  Y.  47.35»;  —  'aeibyo  mal  as,i syazdat  yavqt  'mat  aurutiä  (sd.)  xra/strä Y.J4.9**; —  uzgpuniayeinti  zaslS  'mak^m ,  (GS.)  avaähe  yüsmäk>m  yasnahe  YL  13. 1 147;  —  s.  noch  unter  a,  a  a,  2)  vor I  einer  erläuternden  oder  ergänzenden  Bei- fügung; haxaya  •mäktm  saosyantqm  Yt. //.  17;  F.  7,  Vyt  J7; —  däyata  . .  mäva- yaca  zagere yaziinnai  'mäksmca  (statt  Dat) matdayasnanqm  fräyaztmnanqm  Y.  68.1 2; Vr. /2.  s;  —  haca  ahmät  nmätiift  "mä- kiiiua  mazdayasnanqm  "aus  dem  Haus hier  und  aus  (je)dem  von  uns,  der  M." Yt./_j.57;  —  s.  1.  a)  mit  relativischem .  Anschluss:  aom  narfm  .  .  yü  kasiSt?m  .  . \frSyatat  (sd.)  *°ma  (Akk.)  ^j-a"  atnisS sp?ntS  Yt  /.  24;  —  yUsmäk>m  yasmiica  . . \yqt  am^sanqm  .  .  'mäJhi/i  havaiiuhüua  ,  . ^yat  laesyatäam  Y.  14.  i,  Vr.  5.  i ;  Yt.  J.  i  f., I  FrVV.  I.  2 ;  -  's.  1 .  3)  sonst;  a)  D  im  Ap.
9493:•  j.,  g.,  p.  käma-  m.  'Verlangen,  Wunsch': haväi  °maua  zaosai'a\t.i^.2y,  —  aeiby:! p^r^na  äpansis  (sd.)  "m^m  Y.  2(V.  10;  — arii;ä  vsizdyäi  (sd.)  °mahy3  ^.43. 13.  a)  mit  Akk.  des  Verlangten": /^..-/y- xat  (sd.)  "///?..  dBtVm  ". .  im  Verlangen !  ^'^'''5,^ nach  der  Botschaft"  V.J.M3.  b)  mit'  "?  -' Akk.  des  Verlangenden^':  II  ya>3  mäm 'ina*  ä/ta*  "wie  es  mein  Verlangen  war" D.tf.4;Bh.4  4.
11719:tä  äpS  .  .  vlbaxi'aiti  Yt  8.  33  f. ;  —  vairlm äcaraiti  ..;  upäca  tä  äpS  yaozqyeiti  YL 8.&.  b)  substantivisch;  a)  im  gAw.: AvB  nä  .  .  at  köi  .  .  ahmäi  .  ,;  tSm  vS als  TnShmaidl  hushaxäim  (sd.)  Y. 46^113; 4S-  8;  —  dr?gva  .  .  yastsm  xsä^rät  .  . möihat  (sd.)  .,  Y.  4Ö'.  4;  6;  —  ahur^m mazdqm  .  .;  ahyä  xia'hräcä  .  .  tSm  at  .  . yasamaide  Y,_y".  if.;  3^;  —  gavSi  v>rtx- yätqm  (sd.);  tqm  rP  :x^aryh3i /suyS  (sd.) Y.48.S;  —  aväi/  (Sp.  167  u.)  aiit  yJttg ..tsi  ädyä  iai/yäntllsd.)  ..  Y.J2. 15;  — dngvats  . .;  al  tSi . .  angrSng  (sd.)  *asin>f0 ädarS  Y.  43. 15;  —  akmäksttg  .  .  urunS pastikanqmcä . .ya^byascä  isi  ä  (Sp.300  m.) yalcä  aUbyS  ä  anhm  Y.3g.i;  —  aj  tut (Sp,  619  m.) . .  ysi  . .  tsi  zJ  data,  hamae- stärs  {%d.)  *ais?mahyä  Y.4S.12;  —  »lii- d?m  . .;  tal  zl  vairlm  . .  däiä  Y.J4.14; —  vohä  xsa^r»m  .  .;  tat  .  .  vaniäm  Y. 5/.  i;  —  syaoüanäii;  paityaogil  (sd.)  tä (NPn.)  ahm��i  jassit..  Y.46.8;  —  vaMstH sravsscä  fyao%aftacä  vao^ä,  tä  (APn.)  tu  . . Y.J4-1S;  —  a%a  hat  voAa,  tat  Stada (sd.)  v^rPzyStB^ä ..Y.3§.6 ;  —  asJ  .  .  ^main- y}us  ä  vahiltäi . .,  tä  (ADm.)  tBi  *isyS  .  . dar/täiscd  (sd.)  Y.33.6;  — poura  aini  .  . yezx  täiS  aiä  ..  Y.32.6;  —  ASn.  in kollektivem  Sinn:  masJa  yasmmiä  voA- ntpmcä  . .  gSuscä  väitr>nt,  tat  at  vS  vms- yämakJY.3^.T,  —  mit  Numeruswechscl": kasclt  aia  huzSntus  (sd.),  täÜcä  vlspäif ^wahmT  xid^rBt  ahurä  ".  .  und  mit denen  allen  —  in  deinem  Reich,  o  Ah.T  Y, 4:5.5*'.  a)  zugleich  vorausweisend; a)  auf  ein  Relativum  als  dessen  Korrelat: arf^ä  vsizdyäi  (sd.)  Mämakyä;  tSm  mSt data  y}m  vä  *natäs  dänlt  ÜE  (sd.)  Y. 43- 13;  —  ahm  tu  andräi^  (sd.)  idi  .  . taisysng  usvakT. .  Y.  4ß.  \  6.  ß)  auf  eine nominale  Ergänzung:  ahmät  *mainy3ui .  .; läcä  (Sp.  613  m.)  sp?tttä  mainyU  . .;  tä (IS.)  da  sp}fUä  mainya  Y.  47.  4-6; —  ta (Sp.  618  u.)  mainyü  .  .;  alcä  hyat  tä (NDm.)  hsm  tnainyü  jasaettm  Y.30. 3f.;  — parltSm  zT  hwä  yahanä  tat  Smavatqm  (sd.) "rogatum  enim  a  te  veluti  id  potentium" Y.4^.10.  B)imjAw.:  vprt'irayntm ..; ttm  yazata  .  .  zara'iustrj  Yt.  14  28;  J0.6, g.  18,  75.  j,  3a,  ig.  44;  —  kascii  mai- yänqm..;  t>m  hacäi  asif..  tsm  ..  Yt  ig. I  53  f-; ^7' (als ASn.),  96; — yämm  vSyisämi
14632:Ableit.  aus  *'^riiiaiaii  indeliL  Zw.  '13'.  — Pü. :  sizdahum.  —  »)  Aber  bL  IriyoJaia,  np. shdaA  {».  Hbm.  PSi.  78).
19413:—  ariäa  vsizdyäi  kämahyä  \iSm  mSi data  Y.  4j.  13;  —  tarn  mSi  dqst- vam  (sd.)  .  .  frävaoca  Y.  46.  7 ;  —  aim msi  idä  viiis  ys  ..y.2g.Z;  —  ka^ä möi  yqm  yaoi  damqm  *yaosdam  \.  44. 9;  —  a%a  mffi  sqstä  (sd.)  voAs  västryä Y.  25.  i;  —  «?jV  mdi  västä  {sA.)  xlmat anyS  Y.  25. 1 ;  —  am  si  raförai  saving (sd.)  jasatä  Y.2Ä3;  4:3.1;  —  us  möi uzär)sva  (sd.)  aAura  Y.  33.  i  a ;  —  JrS  m  Bi fravoizdüm  artha  (sd.)  . .  '^.33. 8 ;  —  gaidl m  Bi  ä  möi  arapa  Y.  4g.  i;  48.2;  ^i.Ji  — dBiia  mBi  istöis{s±)  xsahr^m  Y.  5J.  a; 33. 13;  —  sraotä  möi  m>r3sdät3  möi ^•33- '^i  —  ^"J  ^J?^  P'risa  \3r3i  möi vaeca  aAura  Y.44.i~i9;  4^.9;  —  Säirä möi  dam  *akümMLraiüm  Azdi  Y.44-'i6;
23789:mit  aiwi  '(das  Haupt)  erheben,  hoch tragen':  malyehe  . .  aiwi.vsizdayantakt*^ kamirio>m  ". .  der  das  Haupt  hoch  trägt" Y.p.31.
25192::(sd.)ni  galriisä  sizdraca  'rätS  ".  .  und die  scheuen  (Tiere),  die  in  den  Ebenen streifen"  Yt&36.
26348:i)  'zurücktreiben':  vlstäsf^m  .  .  yat imqm  dainqm  ästaota  dulmainyäm  sisdyl äatvqn  apa  "alavatt  (sd.)  Yt./5.84.  2)  'zu Tückweichen,  sich  entfernen  von  — '  (Abi.): ma^ä  .  .  vattlaul  sizdyamnS  mananhö .  .  ahurahyä  xratsus  nasyantS  (sd.)  a/J- atca  ",  .  die  sich  entfernen  vom  guten Denken  . ."  Y.J2.4.
26349:Vgl.  lyasda-  und  «äfra-.  —  El.?')  ar.  "iiH^aidlfif :j(iy5rf:4*.  — Pü.!  aiän  -.-akuman  +/t£r/ (Trans - skr.)'),  ttX.:  kuiän  hal dür;  Sü.:  iiUamam  sida- yiUi  manah  ,  erl- :  . .  tifäm  dekäl  gvaAnattah düri  äste.  '—  D  Ohne  Wert  S  139-  —  '>  Am Ende  mit  t  statt  d  geschrieben.  S.  lu  syazdal und  zu  siidra:
26350:•  j.  sizdyant-  Adj,,  PPA.:  S.  sisdya-.
26351:•  g.  sizdyamna-  Adj.,  PPM.:  &.st;dya-
26352:•  j.  Sizdra-  Adj.  'scheu':  spsnim  slidr?» .  .  yim  var?hapartm  "den  scheuen  Hund V.  (Igel)"  V.  13.  z;—  auruna{sA.ya  gairi- säcB  sizdra^a  ravascarats  Yt  8.  36.
26353:Zq  syaa^a-,  siidya-;  vgl.  lEl.  Gdn.  KZ.  2^.407, zBild.  ni^dra-  und  ai.  nudhirä-  mit  IF.  7.  57,  — Pü.i  +jarf(Transskr.)'>,  erl.:  k^Jlk —  0  S.  za  sildya-  nod  syazdal,
27129:syazda-
27176:•  g.  syazda-  Praes.  18  a  'zurück- weichen'.
27177:mit  Abi.  'vor  — ':  ySi  , .  armaitlm  . . b>nxtqm  (sd.)  . ,  avatatai  . .  alifye  mai' ala  syazdai  yava^  ahmat  aurunH  xrafstra ".  .  vor  denen  weicht  Asa  gar  sehr  zu- rück, so  weit  als  vor  uns  die  wilden  Raub- tiere" Y,j4.  9.
=== BRT nazdyō ===
18845:nazdyo
```


## [2026-09-14T01:26:12.202Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== CHEUNG sad/sand ===\" && grep -n \"^\\*sand\\|^\\*sad\\|sand.*seem\\|pasand\" CHEUNG.txt | head -30 && echo \"=== CHEUNG had/sed ===\" && grep -n \"^\\*had\\|nišastan\\|\\*sad \" CHEUNG.txt | head -20"
}
```


### [2026-09-14T01:26:12.282Z] TOOL RESULT

```
=== CHEUNG sad/sand ===
21769:*sand ‘to appear, seem (good)’ 
21771:*AVESTAN: Av. sand- ‘to appear, seem (good)’ — Liste: 61 
21802:*sad-), especially when the corresponding caus. formation *sandaja- is well attested 
21815:*sand 333 
21844:*NWIR: Zaz. 4-sayis/a-sen- ‘to appear’ || (+ *pati-) NP pasandidan/passand- ‘to 
22317:*sad 341 
41266:pasandidan/passand-, 
57773:*sand 
57816:*sad 
=== CHEUNG had/sed ===
8914:*had 125 
8937:*had ‘to sit, be seated’ 
22317:*sad 341 
55508:*had, *HaHh 
57486:*graH, *sad 
57816:*sad 
57834:*had, *HaHh
```


## [2026-09-14T01:26:14.999Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '21760,21870p' CHEUNG.txt"
}
```


### [2026-09-14T01:26:15.057Z] TOOL RESULT

```
Lubotsky, Early Contacts: 314 considers the root a borrowing from a "substrate" 
language. 

*PIE — => LIV: 324 | Pok.: — 

*REFERENCES: TFL II: 540a; GMS: $543, 577; Abaev, Slovar’ I: 189; Andreev — PeSéereva: 318a, 320b; 
EVS: 74a, 116b; EVS: 419a; Klingenschmitt 1982: 226; Steblin-Kamenskij 1999: 307 


*sand ‘to appear, seem (good)’ 

*AVESTAN: Av. sand- ‘to appear, seem (good)’ — Liste: 61 

Pres. aja-: IND. 15р. YAv. saóaiiemi (H 2.12), 25р. YAv. saóaiiehi (H 2.11, AZ 1), 3sg. YAv. saóaiieiti 
(H, Vyt), INJ. 3sg. YAv. sadaiiat (F 522), 3р1. YAv. saióin (Yt 14.56), SUBJ. 3sg. Y Av. sadaiiät (V 
2.24); Aor. s-: INJ. 2sg. OAv. sas (Y 46.19), 3sg. OAv. sas (Y 43.11), IMPV. 2pl. OAv. sastä (Y 29.1); 
Caus.: IMPV. med. 25р. YAv. sondaiian‘ha (Vr 8.1) 


*OLD PERSIAN: @ad- ‘to seem’ = Kent: 187b 

Pres. aja-: INJ. 35р. 0adaya <0-d-y> (DNa 58, DNb 53), SUBJ. med. 35р. 0adayataiy <@d-y-a-[t]-[i]-[y]> 
(DB 4.49, DSj 6), <0-d-y-a-t-i-y> (DSa 5) 

*MIDDLE PERSIAN: MMP shyn ‘apparent; prominent, splendid’ || (+ *pati-) MMP 
psyn-, psn-, BMP psnd- /passand-/ ‘to approve’ = DMMPP: 307a, 284a 

(+ *pati-) Pres.: IND. 3sg. BMP psndyt /passanded/; Partic.: perf. pass. BMP psndyt /passandid/ 
*PARTHIAN: ? swnd- ‘to slander’, swnd’g ‘slanderer’, swnd’dyft ‘deceptive talk’ (< 
Sogd., see below) || (+ *pati-) psynd- (old caus.) ‘to take a liking to” = Ghilain: - | 
DMMPP: 310b, 284b 

Pres.: IND. 3pl. swndynd {hapax} || (+ *pati-) Pres.: IND. 3pl. psyndynd {hapax} 

*KHOTANESE: OKh. sad- (sai-, sei-, sas-) ‘to appear, seem’ || (+ *pati-) pasad- (pasai-, 
pasas-) ‘to seem good’ => SGS: 130 f., 78 

*SOGDIAN: SSogd. sy-, BSogd. sy-, CSogd. sy-, MSogd. syy- ‘to seem, appear, 
show’, CSogd. syd ‘to appear, seem’, BSogd. swntk, swnt’y, CSogd. swnty ‘liar, 
deceitful’, MSogd. swndyh ‘liar’ (GMS: §966) || (+ *pati-) SSogd. ptsynt, BSogd. 
pts’ynt ‘to approve’, CSogd. ptsynt ‘to consent’, MSogd. ptsynd ‘to agree, be 
pleased’. Ó It is difficult to separate BSogd. sy- from the root *sand- (zero grade: 
*sad-), especially when the corresponding caus. formation *sandaja- is well attested 
in Sogd. The apparent absence or loss of the dental needs an explanation though. 
Perhaps, this is the result of a simplification which occurred after the development 
of a secondary cluster *sö-. This cluster would have risen after the shift of the accent 
(due to the workings of the Rhythmic Law): zero grade Plr. *sadia- > *sóiá- 
(simplification of initial só- > s(s)-, with possible prothesis oss- {’s-} ?), or 
(monophth.) *sóé- > se written in MSogd. as syy- (GMS: $494). Note that Sogd. 
forms with initial cluster sö- or zö- (vel sim.) are not found, with the possible 
exception of the borrowing zöxh ‘serpent, dragon’ (cf. MMP ’zdh’g, BMP ’cydh’k). 
The coexisting form CSogd. syd (heavy stem) may have been abstracted from 
prefigated formations, cf. notably (caus.) BSogd. pts’ynt ‘to approve’, CSogd. ptsynt 


*sand 333 


‘to consent’: * saóaja- or *-sáóaja- > (epenthesis) *saióa- > seó(a)-. || A different 
solution has been advocated by Yakubovich 2002: 547 f., who suggests a connection 
with Germanic (Engl. to shine, NHG scheinen), Slav. *ssjati. This is a formally 
attractive suggestion, but the Sogdian forms would not by supported by other (Dr. 
cognate forms though. | The Sogd. forms of swnd? are probably connected, the 
meaning is due to specialisation: ‘having the appearance of good(ness)’ > ‘feigning 
goodness’ > ‘duplicitous, deceitful’. On the stem vowel /-u-/ « *-a-, cf. BSogd. 
Swnk ‘mussel’ < Skt. sankhä-, GMS: $113. Parthian swnd- is probably a borrowing 
from Sogd. 

Pres. {1}: IND. 3sg. BSogd. syt, BSogd. sy’ty, SUBJ. 2sg. BSogd. ’sy’y, OPT. 3sg. SSogd. sy’y, SSogd. 
syy, 1р1. BSogd. sy’ym, IMPV. 2sg. BSogd. ву”, BSogd. sy’, CSogd. sy’; Impf.: IND. 35р. BSogd. ’sy’, 
CSogd. -sy’, BSogd. syt, 3pl. BSogd. sy'nt; Partic.: pres. BSogd. sy’yn’y; Inf.: BSogd. ’sy’y, pret. 
CSogd. зу” Pres. {2}: IND. 3sg. dur. CSogd. sydtq || (+ *pati-) Partic.: pres. caus. MSogd. (pl.) 
“ptsyndnyt; Caus.: pres. IND. 2sg. BSogd. pts’ynt’y, 3sg. SSogd. ptsynt, 2р1. MSogd. ptsynd’skwn, impf. 
IND. 3sg. BSogd. pt’ys’ynt, fut. IND. 2sg. CSogd."ptsyntyq' 

*CHORESMIAN: т/ѕсу- ‘to appear’, ? 'snCY- (denomin. ?) ‘to praise’, end ‘praise’ (= 
Skt. chändas- ‘song of praise’) || (+ *abi-) m/fsncy- ‘to give, make enough’ || (+ 
*pati-) psnd- (caus.-iter.) ‘to be content, please’. 0 The voiceless -су- instead of the 
expected voiced -zy- is due to assimilation to s-. > Samadi: 161 f., 70 f., 184 
*BACTRIAN: Otvdo ‘wish’, “ayt-o1vdo ‘dissatisfied’ || (+ *hu-) vo-o1vdapo, 
vo-o1ıvönıo ‘pleased’ || (+ *hu-ni-) DVo-vacoıvönuo, vo-vootvóo ‘content, satisfied’ || 
(+ *hua-) xoo-ouvóoo, xo-ouvóo ‘acting willingly, acting freely in accordance with 
one’s own wishes’ = S-W, Bact.: 223b, 177b, 229a 

*NWIR: Zaz. 4-sayis/a-sen- ‘to appear’ || (+ *pati-) NP pasandidan/passand- ‘to 
approve; cherish’, Abz. pesändowa/pesänd- ‘to agree’, Gz. pisánd-/pisánda, Ham. 
pesändayän/pesänd-, Khuns. pisend-/pisendä ‘to approve’ 

*NEIR: Wa. sodbry-, ѕыа(ы)у-/ѕәаоуа-, sodoyd, sodoyd ‘to appear, seem’ || (+ *pati-) 
Sarig. püsan-d ‘to approach, match, suit, correspond to, be equal, come up to’ 
*SANSKRIT: chand ‘to appear, please’ (RV+), chändas- (n.) ‘hymn of praising’, 
chándu- ‘pleasant, agreeable’ = EWAia I: 528 

9 This root is widely attested in Ir. 

«PIE ? *(s)Kend- ‘to agree, approve; to appear, seem (to agree)’. © Cf. Hoffmann 
1965: 165 ff. Note that the meaning ‘to shine’ is absent in Iranian *sand. The Khot. 
form cadana- ‘shining’, with atypical c- (rather than regular tc- < Ir. *C-), is most 
likely a borrowing from BSkt. = LIV: 546 | Pok.: — 

*IE COGNATES: Lat. censeo ‘I approve, judge, am of the opinion’, Gr. кёкос|цол, 
кекоёрёуос ‘to excel’, ? OCS sets ‘inquit. 0 Lat. censeo has -s- from ppp. (?), cf. 
scandö/scänsus ‘to climb, rise’, or rather from *Kens- (s.v. *sanh) ? 


334 *sanh 


*REFERENCES: TFL П: 539; Abrahamian 1936: 118; EVS: 61b; WIM I: 71; WIMII/1: 81; DKS: 418b f., 
224b; Werba 1997: 185; Paul 1998: 291b; Steblin-Kamenskij 1999: 320; Kümmel 2000: 181 ff.; Lecoq 
2002: 124
```


## [2026-09-14T01:26:15.651Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '8930,9010p' CHEUNG.txt"
}
```


### [2026-09-14T01:26:15.704Z] TOOL RESULT

```
*IE COGNATES: Gr. ё&летол, Lat. sequitur, Olrish sechithir ‘follows’, Lith. sékti ‘to 


follow, go after’, Latv. sekt ‘to follow, to go after’ 
*REFERENCES: КРЕТ. 243b; Werba 1997: 249; Lecoq 2002: 134 


*had ‘to sit, be seated’ 

*AVESTAN: hiö- ‘to sit, be seated’ || (+ *abi-) ‘to be seated on (a horse)’ || (+ *ni-) ‘to 
sit down’ — Liste: 71 

Pres. them. red.: IND. 3sg. YAv. nishióaiti (Y 10.15), SUBJ. 3sg. Y Av. nishióat (V 16.1), OPT. 2sg. 
Y Av. nishiööis (Н 2.13, Vyt 59), 3sg. Y Av. nishióoit (V 9.29), med. 3sg. Y Av. nishióaeta (V 8.11, V 9.33 
ff., V 16.8 f£); Perf.: ОРТ. 3sg. YAv. ni hazdiiat (Yt 13.13); Inf.: ҮАУ. aiBi.Sasta; Caus.: IND. 35р. YAv. 
"nisaóaiieiti (FrA 24), INJ. 35р. YAv. nisaóaiiat (Y 9.24), OPT. 2sg. Y Av. nisaóaiiois (H 2.14); Desid.: 
INJ. 3sg. OAv. hisasat (Y 32.13) 

*OLD PERSIAN: (+ *ni-) ni-sad- (caus.) ‘to establish’ = Kent: 212 

Caus.: impf. IND. 1sg. niyasadayam <n-i-y-S-a-d-y-m> (DNa 36), niSadayam <n-i-8-a-d-y-m> (XPh 34) 
*MIDDLE PERSIAN: (+ *ni- MMP nsyy- ‘to sit down, settle oneself’, MMP ns’y-, 
BMP n3’n- (caus.) ‘to place, settle, ground, establish = DMMPP: 245b f. 

Pres.: IND. 3sg. MMP nsyyd, SUBJ. 3р1. MMP *nsyy’nd, IMPV. 2sg. nsyd; Partic.: perf. pass. MMP nšst, 
etc. 

*PARTHIAN: (+ *ni-) nšyd- ‘to sit (down), settle oneself’, also nšyl- (< Bact./Sogd. ?). 
= Ghilain: 50 | DMMPP: 245b f. 

Pres.: IND. 3sg. nsydyd, 3р1. nSylynd; Partic.: perf. pass. nšst; Inf.: "nsstn 

*KHOTANESE: (+ *ati-) tva’y- (ttuva’-) ‘to bring across’ || (+ *abi-) bvai(’)- ‘to 
mount; ride’ || (+ *ni-) nät- ‘to sit down’, näta’s- (na’s-) (inch.) ‘to end’ = SGS: 39, 
102, 53 f., 57 

*SOGDIAN: (+ *pati-) BSogd. ’pc’t ‘time, instant’ || (+ *pari-) SSogd. prsyö (old 
caus.) ‘to sit through, out’ || (+ *ni-) BSogd. пуб, CSogd. пуа, MSogd. пуб ‘to sit 
down’, BSogd. n(y)s’y6, BSogd. nysyö, CSogd. nsyd (caus.) ‘to plant; establish’ 

(+ *pari-) Impf.: IND. 2sg. SSogd. prysyöy || (+ *ni-) Well attested: Pres.: IND. 3sg. BSogd. nyöt, 3pl. 
BSogd. nyö’nt, SUBJ. 3sg. BSogd. nyö’t, etc. 

*CHORESMIAN: (+ *ni-) ny0- ‘to sit; to be, become’, m/nh’zy- (caus.) ‘to place’ 
c» Samadi: 127 


126 *hah 


*BACTRIAN: (+ *ni-) vipoApo, мролцо ‘seat (of the gods), throne, dwelling’. 0 Cf. 
Pth. nsdm, MMP nëm, BMP nsdm ‘seat’. = S-W, Bact.: 208b 

*NWIR: (+ *4-) Abz. avad/av-, Abyan. aya(y)-/ay-, Qohr. aha(d)-/ah-, Ard. axo/ax-, 
Tr. axa(y)-/ax-, Nn. āšis-/āš- ‘to become seated’ (influenced by *HaHh ‘to be seated, 
sit’ ?) || (+ *ni-) Widely attested: NP niSastan/nisin-, Bal. nist/nind-, Kurd. nistin, 
Zaz. ro-nistis/ro-sen-, Awrom. nistáy/-nis-, Tt. (Esh.) ansin/ansest, Gz. ni(y)-/nist, 
Gil. (Rsht.) nistaen/nisin-, Gur. (Kand.) nist-/-nisan-, Ham. he-nistän/ he-i-ni-, Semn. 
nia- ‘to sit’, Sang. -nést-/ neeroen-, Shamerz. -nist-am-/näsin-am-, Sorkh. -niäst-, 
(supplet. ?) nin-, Lasg. -nest-/nieroen-, Isfah. nišdän (supplet. ?) niy-, Sist. rsin-, Siv. 
rsin-/nist ‘to sit down’ (with dissim. n- > r-), Gz. nan-/nast (caus.) ‘to make to sit 
down’. 9 The intervocalic -r- attested in some modern dialects is perhaps the result 
of a "Parthian-like" development: *-d-> *-6-> -г- ?, cf. Sorkh. -sust-/Sur- ‘to wash’, 
s.v. *xSaud. 

*NEIR: (+ *8-) Sh. yä0 (m.), Bart. y00, Sariq. yo0, Yzgh. ya ‘nest’ || (+ *upa-) Oss. 
I. badyn/badt, D. badun/badt ‘to sit’ || (+ *ni-) Pash. näst ‘seated, sitting’, Sh. n10-/ 
nust, Rosh. ni0-/nost, Bart. ni0-/nóst, Yzgh. ni0-/noyüst, Sangl. nió-, Yi. nix-/niast-, 
M. nix-/nidst-, Yghn. nid-, Wa. nbizd-, nazd-/nayn- ‘to sit down’, (caus.) Sh. näö-/ 
näöd, Rosh. n&ó-/neód, Rosh. n&ö-/nüst, Bart. noó-/nóst, Sariq. nalaóon-/nalaóond, 
Yzgh. nidon-/nidont ‘to make to sit down’, Wa. nid(1)v-/nidovd-, niö(bI)v-/nidovd 
‘to place, give a seat’ 

*MISC: (+ *ni-) Orm. n-/nustuk, nastak ‘to sit down’ = ney-/nöstök, nóstok, nostok, 
Orm. naw- (orig. caus.) ‘to cause to sit down’ = naw-/nawok 

*SANSKRIT: sad ‘to sit’ (RV+) = EWAia П: 692 

9 The apparent loss of the expected ruki *š (after *ni-), cf. YAv. nishiöa-, Pth. nsyd-, 
Skt. ni-sida-, in several (esp. East) Iranian languages is strange: replaced by 
(simplex) *hida- ? Also the appearance of voiceless -0- in some languages needs an
```


## [2026-09-14T01:26:31.833Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for p in 71 230 231; do echo \"######## HRN printed p.$p (leaf $((p+21))) ########\"; awk -v n=$((p+21+1)) 'BEGIN{RS=\"\\f\"} NR==n' HRN.txt; done"
}
```


### [2026-09-14T01:26:33.181Z] TOOL RESULT

```
######## HRN printed p.71 (leaf 92) ########
- 71 -
g. pur, Semn. i>lr; Käs. pur, pur.
ap. aw. pud^ra- 'Sohn ; phlv. pusar, pus, Säh]puhr;
ai. putrd-,
kurd. pisir, pes[mamy püer (H.-Sch.); oss. d. furf,
t. firf (294) ; bei. n. pusay (304) ; wa/. /?6Y/', ^iyn, piic^
sar. /?öc', minj. pur; arabisirt für in fayfiir, takfür ^),
i'm- (N. pr.).
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
häufig (kurd. fayfürl, farfürl etc. bedeuten dann sogar ^Porzellan*).
Fayfür (Kaiser von Byzanz) v. Hammer, Geschichte der schönen
Redekünste Persiens, S. 94; takfür, Maqrizi II, 2, 190 (Quatremere),
de Lagarde, Nachr. der GGG. 1891, S. 164, Armen. Stud. No. 835.
2) Vergl. Geldner, BB. 14, 28.
») Ein Belegvers bei SF.
######## HRN printed p.230 (leaf 251) ########
230 —
V
1025. neberd "Kampf, newerd, neberde 'tapfer (Sahn. I, 93
Vers 586).
aw. *ni -r l/^parU^ peretente sie kämpfen'; phlv.
n{i)part "Kampf (AV.).
Vergl. np. äwerd "Kampf (Sahn. I, 218 Vers 1506),
äwerdgäh (häufig), äweriden,
1025*»*« nebld, nebtd 'Fruchtsaft, Wein »).
ap. ^nipita- 'Trank', vergl. ai. pltd- etc. (Nöldeke,
mündliche Mitteilung) 2).
nehire "Enkel' siehe unter newade (No. 1047).
1026. ner, nerr (AM.) "Mann; männlich', nere [nerre), nenne
"männlich*.
aw. naV' "Mann ; phlv. war; ai. när-,
kurd. ner 'männlich'; afy. nar\ oss. d. nale, t. nal
'Männchen von Tieren' (197) ; bei. nar 'männlich'
(258); sangl. narak.
1027. nirx, nerx "Preis, Wert' (z. B. Schefer, Chresto-
mathie persane I, 99)^).
kurd. ni/ir, nir/ "Wert, Taxe'.
Nöldeke (mündliche Mitteilung) stellt das Wort
zu np. /erlden "kaufen .
1028. nerm "weich, sanft', nerml,
ai. namrd' "sich biegend, unterwürfig, ehrfurchts-
voll ergeben; aw. namra.vä/ä (7jPQI,)?; phlv. narm
'weich, sanft*.
LW. kurd. nertn, zaza nemr "weich, sanft*; afy.
bei. (178) wa;^. narm.
1029. ne^^d "nahe', nezdik^ nezdiki,
aw. nazda- "nahe ; phlv. nazdik, nazdist; ai. nedl-
yas-, nedisfha-.
kurd. nizüky nezTk "nahe*; af/. nizde, nizde; bei.
nazlk, n. nazl/, nazi (256) ; sar. nizd.
*) Reimt auf niskerid, Öähn. I, 166 Vers 675.
2) Rücke rt hatte ZDMG. 8, 286 an ai. pidr (d. i. *pizd') ^drücken,
pressen' gedacht.
^) Die BelegstcUe vordanke ich Herrn Prof. Nöldeke.
######## HRN printed p.231 (leaf 252) ########
MI
— 231 -
WSO, niiad 'Geschlecht, Abstammung, Adel' *), nizade 'von
adeliger Abstammung 2).
aw. ^nizäti", vergl. skr. Jati-.
1031. uiS&iidy nezend niedergeschlagen (trop.); elend,
niedrig*.
ap. *ni -h l/yaw- niederschlagen*, also etwa ein ap.
*/ii/a«/M- 'niederschlagbar voraussetzend, vergl. indische
Bildungen auf -tti- bei B. Lind n er, Altindische Nomi-
nalbildung, 8 54, Ib (S. 80).
Unsicher.
1032. niSästen 'sich setzen lassen', Praos. uisän-em,
nisänden.
Causativ zu nisesten (No. 1083); phlv. n(i)sastan (vd.
16 (17) ÖL), n(i)sanet (M6n.).
1033. nisesten 'sitzen*, Praes. nisln-em,
g. senastmün 'sich setzen'.
ap. m + [/^had-, Caus. niyasädayam; aw. ni -\-
l^had-, mshiSaiti 'sitzen, sich setzen', Caus. niSädayöis;
phlv. n(i)sastan, n(i)$fnet (vd. 16 (1)) ; ai. ni + [/^sad-,
stdati,
kurd. LW. nisin 'sich setzen'; bei. nindag^ n. nin-
day^ Causat. nistainay (264).
Der Nasal der Wurzelsilbe in np. nism-em ist auf-
fallig (er findet sich auch in bei. nindag, ksl. sedq
(sösti), apr. midMs, ist also wohl alt), ebenso das
lange f. Vergl. Bartholomae, Studien II, 97, 98,
der eine Erklärung für die iranischen Formen allein
versucht. Np. nisäxten 'sich setzen lassen* (z. B. Vis
und Rämin, Seite 24 Vers 7) ist eine Analogiebildung.
1034. niseb Unteres; unten'.
aw. *mxsvaepa-, vergl. x^^^W^' (No. 799) ; phlv.
n(i)Sep (AV.), n(i)sepitan^ n(i)sepmd 'sie gehen unter*
(Salemaifn, Mel. asiat. IX, 238), vergl. v(i)seft, 'Ver-
lorenes Sprachgut*, No. 229.
>) VergL Rückert, ZDMa. 10, 138.
2J Vergl. besonders äähn. II, 765 Vers 11 ; auch II, 611 Vers 1601.
```


## [2026-09-14T01:26:55.162Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN naxust ===\" && grep -n \"nu/ust\\|nu\\(/\\|x\\)ust\\|nuxust\\|naxust\\|nu.ust 'der erste\\|erste'\" HRN.txt | head -20 && echo \"=== HRN nesim/nasim ===\" && grep -n \"nesim\\|nesem\\|nasim\\|našim\\|nisēm\\|nesim\" HRN.txt | head"
}
```


### [2026-09-14T01:26:55.252Z] TOOL RESULT

```
=== HRN naxust ===
=== HRN nesim/nasim ===
```


## [2026-09-14T01:26:56.461Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KNT 212-213 (leaf=printed+15) ===\" && awk -v n=$((212+15+1)) 'BEGIN{RS=\"\\f\"} NR==n' KNT.txt | head -60"
}
```


### [2026-09-14T01:26:57.448Z] TOOL RESULT

```
=== KNT 212-213 (leaf=printed+15) ===
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
maskd- sb. ‘(inflated) skin’; NPers. mask, АКК. mas-ku-u ‘skin’, Aram. maškā: borrowed from Semitic ($99, $109, §117, §148.IV; see MB Gr. 5101). такаа lpf. (872) DB 1.86.
müha- sb. ‘month’: Skt. mása-, pIE *méso-; extension ($143.II) of pIE *més-, seen in Av. mah-, NPers. mah, Skt. mäs-, cf. also Lt. ménsis, Gk. шу, Gt. тепа, ОНС mano, Lith. ménuo, all mean- ing ‘moon’ or ‘month’. mdhyd gsm. DB 1.371, 42, 56, 89, 96; 2.26, 36, 41, 47, 56, 61f, 69, 98; 3.8, 18, 39, 46f, 08, 68, 88 (for *mahahyé, with con- traction of- ähah- to -ah-, with Gray, AJP 21.13-4; rather than the usual interpretation as ism. to stem mah-; $131, $165.n1, $185.IV).
miðah- sb. ($156.П) ‘evil’, the opposite of rüila-: Av. mibahya- ‘evil’, mi6aoxia- ‘falsely spoken’, Skt. mith- ‘to meet (as friend or antago- nist), engage in altercation’; cf. Hz. ApI 259-61, Kent Lg. 15.169-70, and hamigiya-. тиба asn. DNb 7, 9, 11.
Mié6ra- sb. ‘friend’; as deity, ‘Mithras’: El. т1-14-5а, Akk. mi-i-ri; Av. mibra-, NPers. mihr ‘sun’, Skt. mitrd- ‘friend’ (§9.VI, $33, §49c, $78, 5148.11). Cf. Vaumisa- and probably hamigzya-. Міга} nsm. АНЬ; Mitra (822) A’Sd 4, A?Ha 6; Ма А?а 5, А?Ра 25. Аз gen. ($818.П), M'tra A?Ha 5°, M‘éra A’Sa 4.
mub- vb., see maub-.
M udràya- adj. ‘Egyptian’; pl., al
```


## [2026-09-14T01:27:02.625Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"hadiš\\|hadis-\\|niyašādayam\\|niyasadayam\" KNT.txt | head -20"
}
```


### [2026-09-14T01:27:02.677Z] TOOL RESULT

```
518:I. Apparently -iya- in the interior of words contracted to --; there are the following ex- amples: niyasadayam DNa 36, and nisàdayam XPh 34t. niyasidya DSn 1, XPh 50, XV 21, and nislaya
845:A’Se 4f [тат (asf. for asn. ima) hadiš; 6 tya (for asf. уйт) afagainàm.
911:Н. pIE ә was the reduction of ë or 6 or à; it became 7 in pAr., but a in all other ЕЕ branches.! *noté|r] father’, OP рий, Skt. рий, Gk. татр. *sedos, ОР hadiš ‘abode’, but *sedos, Gk. os
1635:(2-3) pAr. split of pIE s into s š A, and plr. split of pAr. s into s and A (8115): stanam avas- layam niyašiāyam ачоіа; hadiš niy-asddayam; afaham 6asianaty; nom. ending in baga-" pasti- ріти-&.
2196:III. Apparently there was also a nt. suffix -as-, not varying within the paradigm nor in the corre- sponding masc. formation: type Skt. kravís ‘Taw flesh’, Gk. xpéas. OP nom.-ace. hadiš from *sed- as, cf. ОК. éðos from *sed-os; ace. abicaris *pasture- land’, see Lex. s.v. In names, Hazd-manis, Ardu- mants, perhaps I-mami$; late gen. Haxdmanis- ahyd adds the gen. ending of -o- stems to the nom. as stem.!
2503:OP imf. niyasadayam ‘I set down’ (on -&-, 5117). pAr. *aí&-aja- in Skt. egayati; OP imf. fraiSayam
4105:28 : Katpatuka : Sparda : Yauna : бака : {уау : pa 29 radraya :Skudra : Yauna : takabarà : Рибу 30 à : Каўуя : Maciya : Karka : дану : D 31 drayavaus : xšāyaðiya : Auramazda : ya 32 & : avaina : imàm : bümim : yaudatem : 33 pasávadim : manā : frábara : mam : 28d 34 уадуат :akunaus : adam : x&àyatiya 85 :amiy.:.vasnd : Auramazdahd : a 30 damSim : gafava : niyašādayam : tyašā 37 m : adam : afaham : ava : akunava : yabā : mam: 38 Ката : aha : yadipatiy : maniyáhaty : t 39 ya :ciyakaram.: dha : ava : dahyiva 40 :tyà : Darayavaus : xSayafiya 4] :adáraya : patikarà : didiy : tyaiy : g 42 àfum : baratiy : vadā : xSnasahy : 43 adataiy : azdà : bavatiy : Pārsahyā : 44 martiyahyà : diraiy : artes : pa 45 ràgmatà : adataiy : azdà : bavāti 46 y :Parsa :martiya : dürayapiy : hacà : Pa 47 rsà : partaram : patiyajata : 6itiy : Da 48 rayavauS : xSdyafiya : aita : буа : karta 49 m :ava :visam : vasnà : Auramazdaha : ak 50 unavam : Àuramazdá(ma)iy : upastàm : aba 51 ra : yütà : kartam : akunavam : mém:A 52 uramazdà : pàtuv : аса : gasid : utama 53 iy : vitam : uta : imàm : dahyàum : aita : ada 54 m : Auramazdam : jadiyámiy : aitama 55 iy : Auramazda : dadatuv : 56 martiya : hyà : Auramazdah 57 & : framana : hauvtaty : gas 58 tā : ma : adaya : раб : .. 50 {уаш : ristim : mà 60 : avarada : mà : stabava Nores то DNa: The text of DNa now rests upon the photographs of F. Stolze (Persepolis: Berlin, 1882) and of А. Sevruguin (accessible in Wb. Grab, Plates 2-3). The following readings, which either replace older wrong readings or confirm older doubted readings, are assured by the photographs; the restorations agree with the length of the gaps: ^? framatà- | ram; ™ düraiapty; 9 patiyazsayaty; 9^? aba[ra]- | ha; * adáraiya (for nor- malization, ef. $48); 25 haumavargá ; * akunava; * yadi- patiy : maniy|ühaty : t]- | ya (for -haiy, cf. note on DB 4.39); * {aha} Wb.; “ no space for [mand] before ga6um; £ a[va]dà; **düraiy; 4 dárayapiy; ® Auramazda(ma)ty, with omission of те; 6 ga(sta], see Lex. s.v. (not sero+). Other textual notes: 3° [ра]- | radraya, after other oc- currences, see Lex. s.v.; not [ta]- | radraya. *^* Put- (älyä, after other occurrences, see Lex. svt; not Put[i]yà. 2 yauldatim] ВЕ, sée Lex: ву. yaud-; hardly yaufdinim],
4685:D'Sb = Darius IT, Sesa B. 1 айат: Dárayasaus : XS : vazraka : XŠ : XSyanam : XŠ : DHyünàm XŠ : а 2 hydyd : Вуй: Artazsagahyá : XShyá : puça : Haxamanisiya : 3 batiy : Dürayavaus : XS : ima : hadiš : Arlaxíacü : paranam : akunaus : 4 hya : mand : pilà : ima : hadis : pasava : vasnà : ÁMha : adam : akunavam Notes то D'Sb: Вга. WZKM 39.85-7, after the Akk., restored ? [apara]m ‘upper part’ = ‘part at the top of the slope’, and * [adaram] ‘lower part’ = ‘part lower on the hill’; but Hinz, ZDMG 91.251-2, restores [paranalm and [pasava], in temporal sense, which is preferable. *akunas in copy b. TRANSLATION OF D'Sb: $1. 1-2. ... (= DNa 8-12, with one omission), son of Artaxerxes the King, an Achaemenian. §2. 3-4. Saith Darius the King: This palace Artaxerxes previously built, who was my father; this palace, by the favor of Ahuramazda, I after- wards built (to completion).
```


## [2026-09-14T01:27:04.002Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AHD sed ===\" && grep -n \"^sed-\\|sed-\\. To sit\\|hodos\\|anode\\|cathode\" AHD_watkins1985.txt | head -20"
}
```


### [2026-09-14T01:27:04.060Z] TOOL RESULT

```
=== AHD sed ===
910:sed-', To sit. 1. Suffixed form *sed-yo- in Germanic *sitjan in: a. Old English sittan, to sit: sit; b. Old High German sizzen, to sit (> German Sitz, act of sitting): sITz BATH, SITZKRIEG, SITZMARK. 2. Suffixed (causative) o-grade form *sod-eyo- in Germanic *satjan, to cause to sit, set, in: a. Old English settan, to place: sET’; b. Old High German sezzan, to set, in irsezzan, to replace: ERSATZ. 3. Suffixed form *sed-lo-, seat, in Germanic *setlaz in Old English setl, seat: SETTLE. 4. O-grade form *sod- in Germanic *sadulaz, seat, saddle, in Old English sadol, saddle: SADDLE. 5. Suffixed lengthened o-grade form *séd-o- in Germanic *sétam in Old English sét, soot (< “that which settles”): soot. 6. Suffixed lengthened-
912:grade form *séd-yo- in Germanic *(ge)sétjam, seat (*ge-, *ga-, collective prefix; see kom), in Old Norse szti, seat: SEAT. 7. Form *sed-é- in Latin sedére, (third person plural perfect indicative sédérunt), to sit: SEANCE, SED- ENTARY, SEDERUNT, SEDILIA, SEDIMENT, SESSILE, SES- SION, SEWER?, SIEGE; ASSESS, ASSIDUOUS, DISSIDENT, HOSTAGE, (INSESSORIAL), OBSESS, POSSESS, PRESIDE, RESIDE, (SUBSIDY), SUPERSEDE. 8. Reduplicated form *si-zd- in: a. Latin sidere, to sit down, settle: SUBSIDE; b. Greek hizein, to sit down, settle down: SYNIZESIS. 9. Lengthened-grade form séd- in Latin sédés, seat, residence: SEE?. 10. Lengthened-grade form *séd-d- in Latin séddre, to settle, calm down: SEDATE!. 11. Suffixed o-grade form *sod-yo- in Latin solium, throne, seat: SOIL}. 12. Suffixed form *sed-rd- in Greek hedra, seat, chair, face of a geometric solid: -HEDRON; CATHEDRA, (CHAIR), EPHEDRINE, EXEDRA, SANHEDRIN, TETRAHE- DRON. 13. Prefixed and suffixed form *pi-sed-yo-, to sit upon (*pi-, on; see epi), in Greek piezein, to press tight: PIEZO-; ISOPIESTIC. 14. Basic form *sed- in: a. Greek edaphos, ground, foundation (with Greek suffix -aphos): EDAPHIC; b. Sanskrit sad- in upanigad, Upanishad: UPANISHAD. 15. Suffixed form *sed-G-, seat, in Welsh sedd, seat: EISTEDDFOD. See also compound root nizdo-. [Pok. sed- 884.] sed-?. To go. Suffixed o-grade form *sod-o- in Greek hodos, way, journey: -ODE; ANODE, CATHODE, EPISODE, EXODUS, HYATHODE, METHOD, ODOGRAPH, ODOMETER, PERIOD, STOMODEUM, SYNOD. [Pok. sed- 887.] segh-. To hold. 1. Suffixed form *segh-es- in Germanic *sigiz, victory (< “a holding or conquest in battle”), in Old High German sigu, sigo, victory: SIEGFRIED. 2. Greek ekhein, to hold, possess, be in a certain condi- tion (> hexis, habit): HECTIC; CACHEXIA, ECHARD, EN- TELECHY, EUNUCH, OPHIUCHUS. 3. O-grade form *sogh- in Greek epokhé, “a holding back,” pause, cessation, position in time (epi-, on, at; see epi): EPOCH. 4. Zero-grade form “sgh- in: a. Greek skhéma, “a hold- ing,” form, figure: SCHEME; b. Greek skhoié, “a holding back,” stop, rest, leisure, employment of leisure in dispu- tation, school: (SCHOLAR), SCHOLASTIC, SCHOLIUM, SCHOOL/. 5. Reduplicated form *si-sgh- in Greek iskhein, to keep back: ISCHEMIA. [Pok. segh- 888.] seib-. To pour out, sieve, drip, trickle. 1. Basic form in Germanic “sipon in Old English sipian, sypian, to drip, seep: SEEP. 2. Suffixed o-grade form *soib-on- in Ger- manic *saipén-, “dripping thing,” resin, in: a. Old Eng- lish sdpe, soap (originally a reddish hair dye used by Germanic warriors to give a frightening appearance): SOAP; b. Latin sdp6, soap: SAPONATE, SAPONIFY, SAPO- NIN, SAPONITE; SAPONACEOUS. 3. Variant Germanic form *sib- in: a. Old English sife, a filter, sieve: SIEVE. b. Old English siftan, to sieve, drain: sirt. [Pok. seip- 894.] seikw-. To flow. Extended expressive zero-grade form *sikko- in Latin siccus, dry (probably < “flowed out”): SACK3, SECCO, SICCATIVE; DESICCATE, EXSICCATE. [Pok. seiku- 893.] sek-. To cut. 1. Germanic *segithd, sickle, in Old English sithe, sigthe, sickle: SCYTHE. 2. Suffixed o-grade form *sok-d- in Germanic *sag6, a cutting tool, saw, in Old English sagu, sage, saw: SAW. 3. Suffixed o-grade form *sok-yo- in Germanic *sagjaz, “sword,” plant with a cutting edge, in Old English secg, sedge: SEDGE. 4. Suf- fixed o-grade form *sok-so- in Germanic *sahsam, knife, sword, traditionally (but quite doubtfully) regarded as the source of West Germanic tribal name *Saxon-, Saxon (as if “warrior with knives”), in Late Latin Sax6 (plural Saxonés), a Saxon: Saxon. 5. Extended root *skend-, to peel off, flay, in Germanic *skinth- in Old Norse skinn, skin: SKIN. 6. Basic form “sek- in Latin secdre, to cut: SECANT, -SECT, SECTILE, SECTION, SECTOR, SEGMENT; DISSECT, EXSECT, INSECT, INTERSECT, NOTCH, RESECT, (TRANSECT). 7. Lengthened-grade form *sék- in Latin
```


## [2026-09-14T01:27:15.289Z] TOOL CALL #17: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['KLN','BQT','FFD','MON','POK']:\n    print('==',k); print(json.dumps(d[k],ensure_ascii=False,indent=1))\n\" | head -80"
}
```


### [2026-09-14T01:27:16.355Z] TOOL RESULT

```
== KLN
{
 "title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67",
 "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein",
 "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt",
 "page_offset": "KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.",
 "notes": "Other 1966 IA copies (comprehensiveety01klei/02klei etc.) are lending-only (401/403). local_files: /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt (paginated by leaf); /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1971.txt (plain djvu.txt, no page marks)",
 "local_files": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1971.txt"
 ],
 "cites": "page number, continuous across the two volumes (1966–67)"
}
== BQT
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
== FFD
{
 "title": "Mohsen Abolghasemi, Fe'l-ha-ye Farsi-ye Dari, Qoqnus, Tehran 1374/1995",
```


## [2026-09-14T01:27:22.449Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && python3 - <<'EOF'\nimport re\nt=open('BQT_v4_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\ndef find(n):\n    for p in pages:\n        m=re.search(r'\\[pdf page (\\d+)\\]',p)\n        if m and int(m.group(1))==n: return p\n    return None\nfor printed in (2145,2146,2147):\n    pdf=printed-1917\n    p=find(pdf)\n    print('##### printed',printed,'pdf',pdf,'#####')\n    print(p[:2500] if p else 'MISSING')\nEOF"
}
```


### [2026-09-14T01:27:23.538Z] TOOL RESULT

```
##### printed 2145 pdf 228 #####
[pdf page 228]
ستنذها شکرد کازران
حال داری هم هست. نشخود ؟* - با وار معدوله بر وزن
نشخار ۱ » بنم اول و خای نقطله دار | کشور » بممنی نششوار است که کفته شد وینی
بالف کشیده برا وزن هشیار , آنچه شتر وکاز | مکررخاییدن وچانه برهم‌زدن شتران و کوسفندان
وگوسفند وامثال آن خورده باشند و باز از ممدم | را لیزگفته‌اند فرو بردة خود را ۰
بدهنآورند وبخایند وفروبرند وآثرا بعرهی جره نشرخ * طفلان - آنچه با زغران
کوبند - وبقید‌کاه وعلفیر| نیز کویند که ازدواب | وغیره پر روی تشنة اطفال تویسند .4
بازماند وآنرا بعربی تشوار خوانند ؛ وبکر اول نك ‎٩‏ « بفتح اول ‎)٩(‏ بروزن اغك.
هم‌آمده است . «رخت سنوبر وکاج راگویند .
نشخو‌ار ؟ - با راو معدوله . پمعنی نشکرد گازران ۷ (۷)- بممنی
نشغار است که نیم خوردة علف متوران و ا زکلو | اسفنج است که ابر مرده باشد و آن چیزی است
برآورده وخابيدة شتران وامثال آن باشد ۴ . ماشد نمد کرم خورده وآ ترا بعربی‌هرشفه ورغوة
() خم۱:- بفتح اول + () چش : کازران .
۱ - اسح « نشخوار » (ه.م.) است . ۴ - از : ند (نوش ()) )+ خوار(خوردن)
۳ شخور « رشیدی > قی : نشغار (ه.م.) نوششوار , نوششور (ه.م.) , نشخور , نشوار (معرب)
* فولرس ]1 ۰۱۳۹۷ ۰۱۳۲۰
۴ شش سال بکام دل وآسانی خوردند باید زدن امروز چو آشتر همه شخوار.
« فرخی سیستائی ض ۱۵۹ ۰
۴ «شخوار (هم.) - (عر) ۵ نشره بنم اول اقولی است که علاج کرده
میشود باو دیوانه و بیمار .» « شرح قاموی > . ۹« شك . درخت با («.م.) باشد .
رودکی ( سمرقندی کوید
آن که شك آفرید و سرو سهی وان که بید آفرید و لار و بهی.»
« لفت فری ی ۰۲۹۶
۷ -رك : گازر.
۰ نشتی - بکر اول وافتح دوم (در لهجهٌ مرکزی بکسر دوم ) و فتح چهارم » پارسمی
باستان - 83-۳۳24 . متمدی 737883248270 ؛ ارستا - 186 + 51 . 891002141
( شتن ) . متمدی تا8082(/818 ون . یخلوی 8)1(9025430 ۰ 1)1(8[17261 , هندی
باستان - 81920 . 514241 ۰ بلوچی 810028 . 812427 ۰ دی 81501012880 .
ر4 : اسشق ۱۶۳۳ ؛ زمان حال « تشینم » از ل(68151010820(1 ناشی‌است چنانکه « شکنم »از
ل(ص 09۵00 ۲ , اففنی 325421 - ( تن ) «هوبشمان۱۰۳۳*» کردی 1315010 (شتن)
« ژابا ی 2۲۰ ۰ نیز کردی 02-815[18 ( شتن ) «ژابااس۲:۱۷۲ »کیلکی 0180122 ۰
دراراك ( سلطان]آباد ) یز 8158128 * مکی‌نژاد » ؛ متعدی‌آن شاستن (ه.م.) » شاختن (ه.م.).
شاندن (ه.م.) ؛ فرا رگرفتن . مستقر شدن جاندار بر روی کفل وسرین خود برجایی - جا کرفتن
چیزی درچیزی (همچون تیربرشانه) - منزل کردن - جلوی برتخت سلطنت وامارت : «ایوالمپای
الممتند یال ... بامیری اشت وآنرو ز که پدر مرد معتند محبوی بود » چون بنشت اول چیزی
آن فرمود ... » « تاریخ سیستان ص ۲۸۹ >

##### printed 2146 pdf 229 #####
[pdf page 229]
شکرده -۱4۹-
الحجامین گوبند . ماهی را کویند ۴ - و بمعنی دو چیز را بر هم
تشگرده ۱ (۱)- یک اول و کاف | دوختنوچبانیدن‌ودوچیزدا باهم کوفتن- و کرفتن
فارسی وسکون ثانی ورای قرشت وفتح‌دال آبین, | و آویختن9 - و امرپاین معالی‌باشد یمنی دوچیز
افزاری است صحافان و کقش دوزان و سراجان را باهم بدوزویچیان وبکوب ویگیر وبیاویز ۵
راکه بدان پوست را ببرندوبتراشند وآثر! شفره - و بمعنی چنگه در زدن وچبیدن ودرآوبختن
ی زگوبند و بجربی ازمیل (۲) خوانند ؛ و بفتح بچیزی هم هست که عریان تثبت کوبنده .۹
کاف فارسی هم آمده است . نشمن ‎٩‏ - بکر اول و میم واسکون
نشکنج ۲ - بکر اول و ضم کاف | ثانی ودون , بلغت زند و پازند (۳) خویش وتبار
وسکون نالی ونون وجیم ۰ گرفتن اعا باشد با | راگوبند .
دو سرانگشت يا دو سرناخن دست چنانکه بدرد نش ۷ - بنم اول وانانی بوا وکشیده .
آید وآفرا بعربی قرض و بتر کی‌چمدك خوانند. | یمعتی‌همواروسای وسادهوترم ولفزنده وبی‌خفوت
نشکنجیدن ۴ < بکراول وش‌کاق, | ودرشتی باشد .
بمعنی لشکنج گرفتن باشد:که گرفتن اعضا است نشوه ۸ - بفنح اول وواو . بمعتی‌مستی
با دو سرانگشت چنانکه بدرد آید. باشد که درمقابل هشیاری است.
فشل « بنتح اول وثانی‌وسکون لام,قلاب نشوی - بقتح اول وواوبتحتانی کشید..
() چش : اشکرده - () چش : ارمیل . (۳) چك : ژند و پاژند -
۹ - « شکرده , دست افزار کفش دوز وموزه دوز بود. کالی(مروزی ) گوید :
آمروز باسلیق هرا ترسا بگمود بانداد به اشکرده . >
لغت فری ص ۰۵*۷
۴ - امروزه 81801600 و 1880808 کوبند . « شکنج » بناخن کرفتن بود . عنصری
( بلخی) گفت :
آن صنم راز گاز وز نشکنج ‏ . تن بنفشه شد و دو لب لارنج .>
«لت فرزی س۵۹ .۰
۴ - از : شکنج (هم.)۳ایدن ( پسوند مصدری ). ۴ -اظ . مصحف « سپیل»
(«م) 9 -ر4 : نفلیین.  ‎٩‏ - مسحف هز.2:0)8(50۳022 ۰ 8(8) 622 822)8(5.
پپلوی 35۷8515 ( خوش ) « یوتکرص ۸-۷۷ . ۷ -رك : دور
۸ - شوة بمعنی مستی عربی است . رك : شرح قاموی » محیط المحیط .
نشلیدن - بفتح اول و ینجم » از : نشل (ه.م.) +ایدن ( پسوند مصدری ) ؛ چنگه
در زدن و درآوبختن بود بچیزی وآلرأ بتازی شبت کوبند « جهانگیری »:
گر توخواهیش وکرنه ( خواهی واگرنه ) پتو اندرشلد
زر او چون پدر خانهٌ اوی رگذری.
« فرخی سیستانی ص ۶*۱ *.
جهانگیری نیز همین بیت را شاهد آورده؛ وسروری گوید : در موید ( الفطلاء ) و نخهٌ میرزا
( ایراهیم ) بمعنی دو چیز باشد که پریکدیگر دوزند.»
( برهان قاطع ۳۷۱ )

##### printed 2147 pdf 230 #####
[pdf page 230]
-۱۸۷- ات
نام غهر خچوان اس ‎٩‏ . شتن‌است مطلفاً - وآشیان مرغ را لی زکویند.
نشیب ؟ - یکر اول و ثانی و سکون لشیمن دیق - کنابه از دنیا و عالم
تحتانی‌وبای ابجد » نفیضش فرازاست پعنی‌ت ۴ | است .
- وفروخزیده را نی زکوبند ۴ . نشیمه - بنتح اول بروزن جربمه,پوست
شید * - بکس اول و نانی و سکوت | ر باس خام پیراسته راکوبند ۸ که ازآن بند
تحتانی مجهول ودال » بمعنی سرود وخوانند کی کارد وامثال آن سازند -
تشون ‎٩‏ - یک اول رای »مخت 5 نُشَهِن - بروزن نگین . قطب را کوبند
اشانیدن بمعنی نهادن باشد . و آن نقطه‌ایت از فلك - و پوست درون مقعد
نشیم ۷ - بکر اول و تحتانی مجهول را هم کفته‌اند ‎٩‏ - و امن بنشستن هم هت‌پمنی
بروزن گلیم » بمعنی یمن باشد که جا و مقام | بنشین *۱.
۱- در قاموی نیز نشوی آورده ‏ وگفته که عوام نخچوان گوبند . « رشیدی >:
بار دیگر چنانکه میخواهم پرسالم بخطةٌ آنشوی .
صحاح الفری « فرهنگه نظام » ورك : نخجوان .
؟ - اوستا -0۳1811۷2608 , قی - 55۳0۷8602 ( رك : شیب )ءپپلوی8)1(5[087.
(فرود شدن) « اسشق ۰۱۰۳۸ پهلوی 81906021 (غروب [ آفتاب ومام] )»
پازند 21908۷۷۵ برای ۷888208 ( بهی ز که ) » کردی ع 0۷ 53۳ ( برگفته [ سر
بیایین] ) «هوبشمان ۰۶۱۰۳۶ کردی نیز ۵1980۷ ۰ 5[01#ف8 (شیب يك تیه ) ۰ 831۷ (دره)»
۷ ( پایین ) . 06983600 ( دره ) ‎٩‏ ژابا ی ۸۲۰ >.
۴ کی نه بیند فرو شده به شیب هر که را خواجه برکشد بفراز:.
فرخی سیستالی اس ۲۰۳ ۰
۴ -قی : عیبا (هم.) - (عر) ۵ شید بروزن امیر ‏ بلند کردن آواز است
وشعرست که درجواب با هم خوانده باشند . > « شرح قاموی > + ی
- اکر استعمال شده باشد بمعنی نشتن (۸.م.) است ۳ تن (۸.م.) و متمدی آن
نشاسدن * تشادن ( نهادن ) . ۷ - شیم طاطوند فارسی 1020-7۳ تطقاهه رك :
اسشق ۱۰۳۸ قاط ؛ فی : یمن , از« شتن» (هم.) . سانسکریت ع 816170888
( 433 310۰ , ۷۷/۵۳۵۶ . 60 ۰ 3278510۳) ۵ هوبشمان ۱۰۳۶ 5اطظ >.
۸ - ر4 : جهانگیری . درخراسان « مشیم > پوست بز دباغی کرده‌است «فرهنکه نظام».
‎٩‏ - نهرانی 8188170 (کون . سوراخ مقعد ) . در اراك ( سلطانآباد ) شین ( سوراخ
کون ) « مکی نژاد > ازه نشتن > و۵ شین >. *- رك : تن - ولیز آسم فاعل مرخم
درکلمات مر کب : صدر شین ؛ بالاشین » کرایه شین .
5 نصبی - رك : لغات متفرقهةٌ پایان کناب .
5 فضاره - رك4 : لغات متفرقةٌ پایان کتاب .
۵ نطاف - رك : لغأت متفرقهٌ پایان کناب .
نظارگی - رك : لغات متفرقهٌ پابان کناب +
```


## [2026-09-14T01:27:33.831Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && python3 - <<'EOF'\nimport re\nt=open('BQT_v4_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nidx={}\nfor p in pages:\n    m=re.search(r'\\[pdf page (\\d+)\\]',p)\n    if m: idx[int(m.group(1))]=p\nfor pdf in range(200,217):\n    p=idx.get(pdf,'')\n    if 'نخست' in p or 'نزد' in p:\n        print('##### printed',pdf+1917,'pdf',pdf,'#####')\n        # print lines containing\n        for ln in p.split('\\n'):\n            if 'نخست' in ln or 'نزد' in ln or 'نزدیک' in ln:\n                print(ln)\nEOF"
}
```


### [2026-09-14T01:27:35.141Z] TOOL RESULT

```
##### printed 2123 pdf 206 #####
جهانگیری کوید : «لخر با اول مضموم بثانی‌زده بممتی نخست باشد , و نخری لخستین راکویند.»
##### printed 2127 pdf 210 #####
در شاهنامه در عنوان * اندر فرستادن رای هند شطرنج را نزد نوشین روان > ( شاهنامة بخ ج ۸
##### printed 2128 pdf 211 #####
ار دکه(ه.م.) [ر43:رد]؛ میلهای چوبی با فلزی نزديك یکدیگرشانده ۰ وا اس
##### printed 2133 pdf 216 #####
- ر4: ترزديك اوستا -88242 (نزديك). هندی باستان -8641[85: ۰86619018
چو نزد ده و دو رسانیداسال برافراخت یال بلی پور ژال +
نیب رکه ص ۱۵۵ ؛ نیز پپلوی 832415 «اسشق ۱۰۲۹ «اوتوالا ۵۹» ؛کردی 2120 (نزديك»
```


## [2026-09-14T01:27:41.047Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && python3 - <<'EOF'\nimport re\nt=open('BQT_v4_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor p in pages:\n    m=re.search(r'\\[pdf page (\\d+)\\]',p)\n    if not m: continue\n    n=int(m.group(1))\n    if 190<=n<=206 and ('نخست' in p):\n        print('##### printed',n+1917,'pdf',n,'#####')\n        print(p[:1800])\nEOF"
}
```


### [2026-09-14T01:27:42.236Z] TOOL RESULT

```
##### printed 2123 pdf 206 #####
[pdf page 206]
-۳چ ۱ اس
نخچیل ۱ - بر وزن تحوبل ‏ بمتی | بممتی اول و ابتدا باشد ‎٩‏ و تین بممنی
شچل است که کوفتن اندام باشد با دوسن ناخن | اولین - وبفتح اول وثالی» یعنی ریش و جراحت
دست با دو انگفت چنالکه بدرد آید. لکرد چه‌ختن بمعنی‌رش کردن وجراحت نمودن
نخراز ۲ < جم اول وسکون‌الی‌ورای باشد ۷ .
بی‌نقطه بالف کشیده و بزای نقطه‌دار زده » پزبرا نَخْشب ۸ - بنتح اول و شین نقطه دار
کوبند که پیشر و کله ورمةٌ کوسفند باشد وعربان ) بروزن عقرب » لام شهرست از ترکستان که آنرا
کراز خوانند #۰ بترکی قرشی ‎٩‏ کوبند بفتح قاف » وحکیم بن
نخری ؟ « بفتح اول و کر ای | عطاکه بمقنم اشتهار دارد مدت دو ماء از چاهی
و رای قرشت و سکون تحتالی , فرزند اولین را | که درئواحی آست بحر وشنده‌ماهی برمیآورد
کوبند - که تا قرب چهار فرسنگه روشنایی میداد *۱.
نز *۴ - بفتح اول و شم ثانی وسکون نحشه - بفتح اول وشین قرغت وسکون
زای نقطه‌دار» بممنی نت باشد که اول و ایتدا ثالی » بمعنی حجت و برهان باشد ۱۱
است و لخزین ‎٩‏ بممنی فختین . نَخَکله - بفتح اول وکاف ولام وسکون
نذُخحت - بنم اول وئانی بروزن درست. | ثانی » کردکالیرا کوبند که مخت باشد و زود
۱ یل (هم.) ۳ کلپایگانی 202782 « قاسمی > » قن : لخری » نپاز +
سپه دشمن او را رمه‌ای دا ن که درو به چراننده شبات وله ره جو نخراز.
قرخی سیستانی « رشیدی » « انجمن‌آرا >
۴ -کردی 8751 ( بچهٌ اول , ارشد) « ژابا ص 2۱۸ > » اسفهانی 387271 (نختن).
جهانگیری کوید : «لخر با اول مضموم بثانی‌زده بممتی نخست باشد , و نخری لخستین راکویند.»
قی : راز . ۴ - مصحف « خر > رك : فخری- 6 - مصحف «خری» (ه.م.)
‎٩‏ - پازند 8871051 ( پپلوی 382151 ۰ اوستا 3221151018 ) « باروچا صس ۳۷۳ *.
۷ -رك : خستن. ۸ - 313280830 . شپری ببغارا که جغرافی نوسان اسلامی
آرا دف > هم نامیده‌اند ( قی: تحول مشابه نخچوان - داوه ) [ر4 : سع 1 . این "
عهردردرة کشکه دربا( < کكشك رود که بموازات زرافان (رود سمرقند ) بوی جنوب جارست »
و بسوی آمو دربا جربان دارد, ولی پیش از الحاق بدان در شن‌فرو میرود ) قرار داشته . نغعب
در جادة بخارا به بلخ ( بسافت چ
```


## [2026-09-14T01:27:55.801Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PHD ===\" && grep -n \"naxust\\|nišast\\|nišīn\\|nazdīk\\|nazd \\|nišēm\\|nišēm\" PHD.txt PHD_mackenzie.txt | head -20 && echo \"=== NYB ===\" && grep -n \"naxust\\|nišast\\|nazdīk\\|nišēm\" NYB_vol2_glossary.txt | head -20"
}
```


### [2026-09-14T01:27:55.883Z] TOOL RESULT

```
=== PHD ===
PHD_mackenzie.txt:3681:naxust [nhwst ' I M nxwst, N --] first.
PHD_mackenzie.txt:3691:nazd [nzd I = M, N --] near.
PHD_mackenzie.txt:6579:feel mardan, sohistan.                     first ahy, fradom, naxust, nazdist.
PHD_mackenzie.txt:10121:nazd                        ..s,    windaoan                   \\~"
PHD_mackenzie.txt:10361:Wastar                           \~,              naxust
PHD.txt:507:naxust [nhwst' | M nxwst, N ~} first.
PHD.txt:510:~ pazd- : blow, play the flute. *nāydāģ [nywt’k'] deep, unfordable, navigable. nayestàn [KN Y Ast^n! | N ~] reed-bed, cane-brake. nāyīzaģ [»vck! | N ~a] small reed, straw. nay-sray [rds d] flautist. nazd [nzd | = M, N ~] near. nazdik [nzdyk! | = M, N ~] near. ~ih: proximity. nazdist [x3dst'] first. nàzišn [x*cšn! | N nāsi$] 1. boasting; 2. kindness. nàzuk [n’cwk! | (M wzwg), N ~] tender, gentle; fickle. né [L4 < AP | M ny, N na] no, not. nék [nywk! | M nyk, N ~] good, beautiful. ~th: goodness. nék-góhr [nywk gwhl] good-natured, virtuous. ~ih: goodness, virtue. nēkēģ [nywhkwk! | M nyyquiw!, IN neho] == пёк. nem [PRG < А plg; nym | = M, N —] half. ~ag [nymk! | N ~a] half, side, direction. ~-аѕр [5р] centaur; astr. Sagittarius. ~-rōz [-lwe | M -rwe, N ~] midday, south. ~-tan [-tn' | N ~] middle of the body. nérang [nylng | N <] incantation, charm, spell. пёгӧб [nylwk! | M nyrwg, N nero] strength, power. ~omand [-’wmnd] strong, powerful.
PHD.txt:514:nihuftan, nihumb- [zhwptn', nhwmb- | = M, N <) cover, hide, conceal, clothe, nihumbidan [nhwmbytn'] = nihuftan. *nikóhidan, nikóh- [nkwh-ytn' | N ~] blame, execrate. ~išn: blame. ~išnīg : blameworthy, execrable. nil [nyl | N ~] indigo. nilópal [nylw(k)pl | N ~, nilēfar] lotus, water-lily. nimüdan, nimāy- [nmwtn', nmd- | M nmwdn, nm’y-, N ~] show, guide. nirfs- [nlps-] wane, decrease. ~išn: decrease, diminution. nirmad [nylmt'] profit, interest. ~ӧтапа [-’wmnd] profitable. P nisag [nys’k' | P nys’g] bright, splendid. niš- [nyi- | M nyyš-ydn, J ~] see, observe. nišān-, v. nišāstan. nīšān [ny$*x! | = M, N nisàn] sign, mark, banner. nišast [nsst! | N ~] association. nišastan, nišīn- [Y TY BWN-stn! < A V у; пт! | M nist, (nfyy-), N ~] sit. nišāstan, nišān- [Y TY BWN.stn!, 2n-; nP?stn!, nP?n- | M nf?st, (nP5y-), N ~] set, seat, plant, found. nišāyišn [n£ din! | M n$?y-, v. niSástan] foundation. nišēb [niyp | N ~] declivity; astr. dejection. ~ig [-yk'] declining. nišēm (nidm | M nšym, N ~an] seat, perch. ~ag [-k'] residence, abode. niSin-, v. niSastan. niwāģ [nw k! | M ng, N nawa] music, song, melody. *niwé [nwyk! | (N nuwéd)] good news. *niwéy-, -išn, v. niwistan, *niwéyénidan [nwykyn-ytn'] = niwistan. niwistan, *niwéy- [nwstn', nwyd- | nwyk-] announce, consecrate. —išn(ih): announcement. nixwār- [nswb’l- | M nyxw’r-] hasten. -išn: haste. niyübag [nyd’pk' | M ny’bg] becoming, fitting, suitable. ~th: suitability. niyāģ [nyd?k! | M nyg, N niya] grandfather, ancestor. niyāyišn [xyd?dšn! | N ~if] prayer, praise. niyāz [nyd?c | M ny’z, N ~] need, want, misery. —ómand [2wmnd | N ~mand] needy. ~6mandih: poverty. niyē(x)šidan, niyē(x)š- [n(y)duhš-ytn! | M nywi-, N niyófidan] hear. ~išn: hearing. І nizār [nz?l | (P nyz?*wr), N ~] weak, feeble.
PHD.txt:698:abode šāwarišn,  bunag, nišēmag; (daevic) dwārišn.
PHD.txt:871:assoctation hamīh, nišast.
PHD.txt:1778:enthroned, be ~ abar nišastan. |
PHD.txt:1956:first ahy, fradom, naxust, nazdist.
PHD.txt:3084:perch nišēm.
PHD.txt:3188:posterior nišēm.
PHD.txt:3402:residence nišēmag; v. dwelling.
PHD.txt:3546:seat (n.) nišēm; foremost — pēšgāh.
PHD.txt:3547:seat (v.) (abar) nišastan.
PHD.txt:3675:sit (abar) nišastan.
PHD.txt:5118:ašnawišnt ašnūdan! nišast nišastan waštīh 1-2waštan waštagīh waštag xwar-! xwardant widaxtan wadxém widār widār- widārīdan widārdan widūz- widazih- widāzīhistan wadbaxt
PHD.txt:5136:wišādan nišēm nisémag nišēb nišēbīg wišūb- wišūbišnīg wišēbišn wišuftan wišūdan wišūdag wiškīdan wašag wiškin(n)- wiskof- wiškūfag wiškuftan wiškin(n)išn wiskar
=== NYB ===
491:?apak [LWTH] 1. a) adv. together: (ka- nicak virtual dat.) andar ham Sap ~ bit in that same night he was together with the girl 16!-?; referring back to an encl. pron.: sih (restore the reading “30”, v. 28th) 4-$ ~ pat asp which was with him on the horse 8? (v.s.v. i and ef andar); Sih-& ... —-aš pat asp nišast estat 89: as prepositions do not govern an encl. pron. ~ must be the adv., and -aš refer to the following pat asp or to the whole sentence. — b) prep. together with, with, in all its senses, passim; in spite of 118; ~ man 5?*; ~ amäh 19, ~ smäh 1918, ~ disin 82; ēvak ~ dit with each other 7818. 799. 1071, — 2. adj. prostrate, knocked down, lying on one’s back: čvak apar, ~ dit, apar ēstūt hend o en kar they set about this act (making coition), the one above, the other lying on her back 4314-4; ka Ahriman ~ A. being knocked down (lying senseless) 914 (the enel. -4 after ~ belongs to the following, taking up the preceding subj. Ohurmazd which begins the period), a wordplay — not understood by the Pazandist — with — hämöden yazdan u amahraspandän |. 5—6, the first
1529:(someone) to read P2:4; — 3. by an inf. which may a) precede ~: 1171. 3726-27 etc.; b) be put after ~: 923, 101? ete.; in this case ~ must immediately precede the inf., separating it from its obj., adjuncts and preverbs: äkäh framäi kartan 11”; šahristān-ē ... framüt kartan 1278-2? and passim (but framüt . . . pairäyenitan with a long series of dir. objects between 120” sqq.); bé nisastan: be framäyet nišastan 141%; apar kartan: pat dar apar jramāyēm kartan 208 ; andar kartan : andar framit kar- tan 11423, and the like; similar construction of apäyet (g. v.); e) be introduced by ki, through contamination with no. 2: fra- mit ku ... kartan 121719; 4518; (+220). — Av. (1166) fra-mäy- ; MPrth frm’dn frm’y-, MPrs prm’dn prm’y-; Paz. far-midan, farmäyastan farmä-; NP farmudan far- may-.
1987:hēšm [hyšm, hšm] wrath, anger: Artax- šer ~ grift A. was seized by anger 37; ~ kartan to become angry 154. 6815; ke ~ 6 tan nē hilét who leaves no room for anger 8414; ~ vas quick to anger 10?!; ~ rād dāšt persisted in his anger 101°; tāi bē nišastan à ~ until the anger sub- sides 6817-18; the work of Ahriman is ~ u kén u anästeh 7822; ~ u ken räd 14%; - personified as a demon, one of the chief evil powers: ~ dev 6123: equal to Ahri- man 68%; in company with Az 103°;
2655:nax®ist [nhwst'] the first 3512. 1114; adv. 1163. — MPrth nxwst; MPrs nxwst; Paz. naxust; NP nuzust; sup. of the pre- ceding w. l
2762:nišast [nást'; YTYBWN-st'] dwelling- place, residence 8). 8611,
2763:nišastan [YTYBWN-stn', seldom nšstn'] nšin- to sit, to dwell, to reside, to seat oneself, to be seated; to be situated 4716; 6 asp ~ 434; api-§ andar o [KN] nisinet and he will reside in it 348; apar ~ to mount on horseback 261%; apar bärak i Zarer nišīnēt mounts the steed of Z. 295; hac asp bē ~ to dismount 272; bē ~ to make a halt 141%, to cease 2024-25, 2522, 6817-18, — Av. (1754) ni-šad- < ni-had- = OP (caus. ni-Sädaya-); Ps. nšstny nšyd- (for nišiy-); MPrth. nšstn nšyl- (!); MPrs nšstn nšyy-; but Paz. NP nišastan nišin-. Ghilain 50; Verbum 169.
2768:nišēm [nšdm] a bird's nest 2018. — < *atšadman, v. nišastan; Paz. nišim, na- šim ‘a resting-place' (Mx), nišāmī (SGV); NP nišim.
3253:rasit [lsyt'] subst. the coming 357-12, — From rasitan; of the same type as nišast ‘seat’, srot ‘rumor’ ete.; ef s. v. raft- čnitan.
6746:naxust: naxlist
```


## [2026-09-14T01:27:57.531Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HUB 1036/1038 ===\" && grep -n \"nišīm\\|nasīm\\|nešīm\\|naxust\\|nuxust\" HUB.txt | head -20; echo \"=== ARY ===\"; grep -n \"نشستن\\|نخست\\|نزد\" incoming/ARY/ARY_pages.txt | head -20"
}
```


### [2026-09-14T01:27:57.609Z] TOOL RESULT

```
=== HUB 1036/1038 ===
=== ARY ===
33:1 و مخبد معین) است. ولی شمار واژه‌هایی که توسط خودم پیگری و برای نخستین بار
157:نزدیکه بودند. علت محدود بودن گستره‌ی آنها این است که طبق اصل «پیشینه‌ی گستره‌ی مجاز»,
206:«ساتم نخستین وات واژه‌ی «صد» سایشی (۳12۸71۷72) یعنی «کو پا «جله است. در زبانهای «ستتم»
398:در سده‌های شانزدهم و هفدهم میلادی که طی آن آموزش زبانهای خارجی رونق گرفته بود»
428:نزدیک شرق ر غرب در هند برخورد انگلیسی‌ها با نوشتارهای کهن هندی به ویژه سانسکریت بود. ."
439:زیر که اعداد از یک تا ده و سپس صد را در چندین زبان نشان می‌دهد نخستین بار توسط پارسوئز .. .
635:محسوب می‌شوند. خویشی نزدیکه زبانهای هندی با زبان‌های ایرانی موجب شده است که در برخی"
691:نخستین اشاره به اقوام ایرانی (مادها و پارس‌ها) در متون آسودی وابسته به قرن نهم پیش از
712:۱ کهن ترین نوشتار به زبان‌های ایرانی» بخش نخست اوستا یعنی «گاتهاه است. برخی این کتاب
719:نزدبکك واژگان گانها با واژگان کناب هندوان (ودا ۷80۸5) نیز می‌تواند حا کی از این باشد که اقوام
807:در گذشته تصور می‌شد که زبان ارمنی همبسته‌ی نزدیکك زبانهای ایرانی است ولی امروزه
811:یونانی خویشی نزدیکتری دارد تا با زبانهای ایرانی,
816:ولی درگذشته‌ی نزدیکك بخش بزرگی از شمال خاوری ترکیه هم ارمنی نشین بود.
841:از خاستگاه نخستین اسلاوها اطلاع قطعی در دست نیست. حدس این است که آنها در شمال و
847:زبان‌های اسلاوی با زبان‌های ایرانی خویشی نسباً نزدیکی دارند. بسیاری از واژه‌های
929:که مفاهیم وابسته به این واژه‌ها در زبان هند و اروپایی نخستین هم وجود داشته و هویت فرهنگك
948:و اروپائیان نخستین نیز هرکسی که گرگ خوانده می‌شد به نحوی منفور قییله بوده است.
968:نهادهای بنیادین هند و اروپائیان نخستین
1009:واژه‌ای وابسته به «خانه» و «خانواده» در زبان هند و اروپایی نخستین 203" بود. سر پرست يا.
1015:است: هند و اروپایی نخستین: 7 سانسکریت: ۸1۸77۸7 اوستابی ‎٩1۸3۸7‏ لانین:
```


## [2026-09-14T01:28:04.623Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '2645,2660p' NYB_vol2_glossary.txt"
}
```


### [2026-09-14T01:28:04.707Z] TOOL RESULT

```
napa ;
narm [nlm] soft 472°. — V. also s. v. *a- namr-tom.
Narsah [nrshy] n. pr. masc. P 1:7 (twice). — Av. (1054) Natryē.saņha-; MPrth nrysf- yzd; MPrs nrysh-yzd (A-H I); Arm Nerseh.
nasäi [ns’y] corpse 6021. 727. 942%. — Av. (1057) nasu-, ace. nasāum, pl. nom. na- sāvē; MPrth ns’w; MPrs ns’h (A-H I); NP nasā ‘dead’.
Nasibin [*ns(y)byn'] Nisibis. (syr Nsibin) 11425.
: nask [nsk] properly ‘bundle, bunch’, the name of each of the 21 “books” or collection of texts forming together the Sassanian Avesta 1091’. — Av. naska- in (1060) nasko.frasa- ‘one who devotes himself to the study of the nasks’.
Navizak [nw’ck'] a town in Bactria 113%. — Cat. 34.
naxcir [nhcyl] hunting 3!*-!? etc. - MPrth nacyr ‘game, prey’ (MHC); KZŠPrth 1. 24 nhšyr(-pty) = Prs 1. 30 nhcyr(-pt); MPrs nheyhr (S, A-H I); NP naxeir ; borrowed: Arm naxčir-k* ‘massacre’; Syr nahšira, etc., v. Telegdi 228; Bailey, BSOAS XI, 1943, 774; XIII, 1949, 122. Asmussen, AO XXX, 1961, 1-20.
| side of 5716, 7418; pat han i...
Nax"-Ohurmazd [nhw ’whrmzdy] n. pr. masc. P 1:6. - MPrthPrs nwx ‘beginning, the first of anything’; ~ ‘foremost is O'.
nax®ist [nhwst'] the first 3512. 1114; adv. 1163. — MPrth nxwst; MPrs nxwst; Paz. naxust; NP nuzust; sup. of the pre- ceding w. l
Nayāzem [Paz.] one of Zartuxšt's fore- fathers 471. — This form with an initial n- (quite unmistakable in the Dk MS) is also found in Vicarkart i dénik 28 (Na- yazem); in other sources (also Arab.) without n-: BdA p. 235! Ayazim, BdJ 79' Ayazemni, etc.
nayitan [DBYLWN-tn, DBLWN-tn'] nay- to conduct, to bring, to lead; ideogr. + x, for pres. 3d p. pl. nayénd 6515; ideogr. + x, for pt. pass. = pret. 3d p. nayit 122°. 515. 5717. 11719. — Av. (1042) nay-; MPrs inf. nyydn (A—H I), pt. nyyd (A-H II); FrP 20 DBLWN-tn' = (K) nytn' read nayičan; (Sı) nyytn' read nyaičan (for nayióan) ; (S,) ideogr. + NP nayidan; P ideogr. + NP na’idan; only one MS (O) has Phl nytn', Paz. ničan.
The pres. forms given in Paz. are: (K)
naió naim; (P) NP na’id nym; (S,) NP n@id nym, but (Paz.) nyid nyem; Paz. Mx 7423 nied, 9017 niend.
nazd [nzd] 1. adj. near: — bäm daybreak 53; without bam, subst. daybreak 6°, cas. obl. nazdéh 4413, — 2. adv. ~ 6 near, short- ly before 10513. — 3. prep. near to 50°; with 5627. — Av. (1061) comp. nazdyö; MPrs nzd (S, A-H IT); NP nazd.-
```


## [2026-09-14T01:28:27.487Z] TOOL CALL #24: Bash

```json
{
 "command": "ls site/pages/435.jpg 2>/dev/null; pdftoppm -f 435 -l 435 -r 300 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg435 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg435.png"
}
```


### [2026-09-14T01:28:29.720Z] TOOL RESULT

```
site/pages/435.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb 89932 Sep 13 21:28 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg435.png
```


## [2026-09-14T01:28:31.615Z] TOOL CALL #25: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg435.png"
}
```


### [2026-09-14T01:28:32.447Z] TOOL RESULT

```

```


## [2026-09-14T01:28:32.429Z] INPUT

[Image: original 2550x3300, displayed at 1546x2000. Multiply coordinates by 1.65 to map to original image.]


## [2026-09-14T01:28:45.456Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg435.png')\nprint(im.size)\nim.crop((580,540,1100,740)).resize((1560,600)).save('pg435-n1.png')\nim.crop((1330,880,1990,1010)).resize((1980,390)).save('pg435-n4.png')\n\""
}
```


### [2026-09-14T01:28:46.892Z] TOOL RESULT

```
(2550, 3300)
```


## [2026-09-14T01:28:49.081Z] TOOL CALL #27: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg435-n1.png"
}
```


### [2026-09-14T01:28:49.161Z] TOOL RESULT

```

```


## [2026-09-14T01:29:04.166Z] TOOL CALL #28: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg435-n4.png"
}
```


### [2026-09-14T01:29:04.198Z] TOOL RESULT

```

```


## [2026-09-14T01:29:24.034Z] TOOL CALL #29: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg435.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/435.png && echo copied"
}
```


### [2026-09-14T01:29:24.113Z] TOOL RESULT

```
copied
```


## [2026-09-14T01:29:25.531Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT nazdyo ctx ===\" && sed -n '18840,18860p' BRT.txt && echo \"=== BRT asna ===\" && grep -n \"āsna-\\|asna-  *Adj\\|asnaoiti\\|āsnaoiti\" BRT.txt | head"
}
```


### [2026-09-14T01:29:25.612Z] TOOL RESULT

```
=== BRT nazdyo ctx ===
VgL  in  nasurtj-.  —    Bed.  nach  Pu.    —   Pn.:  ^         ,    ■'■'  .  '    ,     .      j    -,  _„
naräi  niiäna,   «L  flu  V.  j):   in  dinlt  tu:  ^  ätnm  'tat  hoia  däitlm  giitUm  ovt  avo,-
tiaiäi  niiämh  til  apäyrl  karian,  ape  fain  däril   baroiti  *^KI  FeUCT  VOm  nächstbesten  (Ott)
ob,Google
io6i
nazdyo
1063
weg*  zum  , .  Ort  . ."  V.  8. 9g.  a)  mit Ab\.:y6 AsaaAat {S f.  1060.)  "t^m  nmän^m utdasta  V.  15.21.
KompE.  —  Snpetl.  ta  ^niadyah-  •propior'  und zu  üsna-  'propinquus'.  —  ai.  nidkfha-  Adj., iDp.  nazdht.  —  zEt.  (ar.  *ncaäiil/ia-  tu  einem Praes.  3  *nä-tda-li,  lum  V.  »Airf-)  »gl.  ZDMG. 50.  686,  Bgu.  Grdr.»  /.  735.  —  Pfl.:  nazdist, (zu  Y.  33):  natäli.  —  ')  Hdi.  maidilla;  Pü.: fehlt.  —  ')  Abgesehen  von  den  luvor  aus- drucklich genannten.  PiiErl. :  afil  i  iapastän 'ram  Ort  der  Nacht  weg',  daher  DST.  ZA. 3.  142  >Ie  feu  du  campement';  s.  auch  Sp. Komm.  I.  367.
•  j.  nazdyö  Adv.  '(räumlich)  näher  zu  — , an  -'  (Akk.) :  w  mqm  upaMSia  "tritt  näher zu  mir  heran"  Yt.  27.  31;  21;  —  ..Aisvasca .  .  *ra%wyff.varsH  (sd.)  'yS  ahmt  aztm  yS ahurS . .  vlspahe  awhsus  astvaiB  *manasca *vacäsca  ^iyaeiina^a  yaSia  , .  ". .  bin  ich  . . den  Gedanken  und  Worten  und  Taten der  gesammten  Menschheit  näher  als  . ."
P.2Ä
ASn.  aus  'ntaäyoÄ-  Adj.,  Kompar.  zu  naidisla- IfiA.).  —  ai.  n/diyah  Adv.;  np.  »aji/ 'nahe'. — Pü. :  naxdiilar.
•  j.  naSta-  Adj.,  PPfP.:  s.  *nas: KompA.,  E.
•  j,  "^naStlLzamanä- ''  Adj.  (mask,  °na-) '(der  seinen  Verdienst  verloren  hat  sva.) der  sein  Brod  nicht  mehr  verdienf,  vom Hund:  yal  sünil  para.tri^ynti  'nasca pairistajcsudrasca  V.  ij.  50.
Pü. :  ha  miai'),  erl. :  o  änÜ  tu  ariit.  —  i)  So L4.  NA.  nisid',  worin  ich  eine  Ausgleichung mit  dem  folgenden  Wort  sehe.  —  ')  DsT.s Bemetkung  ZA.  3.  20E  No.  73  ist  mir  un- verständlich.
•  j.  "nahaowf^  N.<^:  -?-,
Pü.:  fehlt
•  j.  "lüuiti  As  aSe  ysi  mafyäAa  ^aranti framanyäe  V.  7.  55 :  —  ?  — .
Pü. :  ivnöi  hit  imäk  ic  martum  ha  -  iSi  dänel -  j^artt  frä/ea  msnii  bardtnm;  s,  daiu  Sp.
Komm.  I.  32Ö,  DsT.  ZA.  3.  110.
•  j.  näuma-  Adj.;  s.  unter  navama-.
=== BRT asna ===
3224:•  j.  a-daevayasna-  Adj.  'der  kein  Da^a- Verehrer  ist',  sva.  tnazdayasna-":  jahi  .  . yö  .xrudrä  fiam.ras^waydti  . .  da^'ayasna- nqm  -nanqmca  \. 18.62.
4148:vergänghchc.di.  materielle  Dasein,  Leben': kaaa  ns  iaa  .  .  agatJ  i^yejauhatat  haca °f»haot  ai'kyejanhsm  ahüm  a  V.  7p.  3 1 ; 7.52;  —  hai:a  apajäsö  .  .  i'iyejatuthata^ haca  'fihaot  atiryejanhutäitn  avi  °hü?n H.  2, 16.  2)  mit  a)  manahya-  Adj.  oder manauhs  GS.,  b)  datbitya-  Adj.,  c)  parS.- asna-  Adj.,  d)  ai>y0ah-  oder  ai'hyejakvant-
7476:•  j.  äsu.yasna-  Adj.  'der  den  Y.  rasch vollziehen  kann' :  haomS  .  .  ytm  zaotänm slayata  ahurB  mazdh  °n?m  bsrizi^ä^r^m; yazata  zaota  "rtö  Yt  lo.  89.
7828:m\i paiti  '(mit  einer  Waffe)  treffen':  yat dim  aZnö.manatiha  paiti.asnaoiti  aetat  lis andus  (sd.)  V.  4. 1 7.
12483:•  j.  daeva-yasna-  Adj.  'der  die  Dalva verehrt,  anbetet';  überhaupt  'ungläubig"*: ye^he  .  .  näirika  avayi  xfudrä  Aqm.- rafktoayeiti  mazdayasnanqm  'nanqmca N.  77'';  ~  kalärö  paurvB  ämayante  (sd.) maidayasna/ibyB  va  'nalibyB  vä  V.  7.  36; 37;  —  drvafäB  'naahdYt.  5.  94;  —  huma- yak»m  'n>m  drvanttmca  ..Y\..^.\\y,  109, 5.37;  —  drvatam  'nanqm  Y.ig.  26,41, Yt5.68,  ;;.  4,6;'  —  dusmainys .'. 'n^iAP.) A.  7,  11;  —  daffnqm  'nanam  Y,  72. 1 1 ;  —
15495:•  ].  paro-asna-  Adj.  "künftig  seiend,  kunf-  {  ^_  ,g|.  ^„^^v««-  Adj. tig":   'näi  aiiuhe pas^a  astttsca  haoaatffiaica  ■   *      t^L-.v
20201:•  j.  'mazda-yasna-  Adj.  'der  den  Matdäh verehrt,  anbetet;  Anhänger  der  MatJäh- religion';  ya^. .  balsazäi  (sd.)  fratiazsnte.. (taet'ayasnaö&yS  paurvö  ämayayania  ya%a '•naiifyasätV.j.$6i;z6;-^yaiAe..°»atiqm näiriia  avaya  xhtärä  hqm.ras%wayeüi 'nanqtnca  //agvayasnartqm/aH.ii; — naisml daWoS  fravaranS  'nS  tara%usfril  vJäalv5 V.  12.  1;  ö,  8,  Yt  13.  89;  —  fi-ä  gave vtrindyäi  -na  zara'hustrayS  Vr.  4.  2 ;  15.1;
24106:•  j.  vidui.yasna-  Adj.  'der  den  Yasna'} kennt':  nanm  .  .  vldul.gaiim  -mm  V, 7«  5..
```


## [2026-09-14T01:29:40.744Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT haδiš ===\" && grep -n \"haSii-\\|haiii-\\|hadiS\\|haöiS\\|haSil\" BRT.txt | head -10; echo \"=== BRT 'Wohnsitz' ===\" && grep -n \"Wohnstätte\\|Wohnsitz\" BRT.txt | head -8; echo \"=== BRT hazd/hid ===\"; grep -n \"hazdya\\|hiSaiti\\|hiöaiti\\|hi6aiti\\|nUhiSaiti\\|nishidaiti\" BRT.txt | head -10"
}
```


### [2026-09-14T01:29:40.847Z] TOOL RESULT

```
=== BRT haδiš ===
=== BRT 'Wohnsitz' ===
5583:•  j.  airyö.sayana-  n. 'arischer  Wohnsitz,  .j^g. aurvant-, aourvant-" Adj. 'schnell; W.  der  Arier':  vJspjm  .  .  'fvm  Yt  10.  13.  tapfer,  Held':  '7-at"  F.  7;  —  /laomo  aeibis
10175:•  j.  gav-a'äayana-  Adj.  'die  Wohnstätte [  der  Rinder  bildend,  von  Rindern  bewohnt':
10176:avi  imitt  karh-arf  yat  x^anira%3m  ..  'tum ' .  .  mi^r^  .  .  ädmäiti  Yt.  lo.  15, '  •  j.  gav-a'äitay-  f.  'Wohnstätte  der  Rin- der': avi  imai  karrvar>  yat  x''anira>:>m.. gavasayaramisA.)  'lliiica  bassatyqm  mi^rö . .  ädi'jiiiti  Yt  10. 15.
12854:—  *h^l>nte  amt^ä  spinta  sfannS  dära- yänii ..  ^antiS  baxi»nti  YL  7.3;  —  s.  noch InC  dindyäl  und  II  däray<^'.  a)  D  mili- tärisch 'besetzt  halten':  karJ'  .  .  tigram adärayt^  avadä  *a*iäatä  (sd.)  Bh.  /. 18.  7)  '(mit  den  Sinnen)  auffassen, vernehmen':  s.  Int  darfhräi.  8)  absolut 'sich  aufhalten,  weilen' :  s.  AbsoL  a)  bes. '(wo)  seinen  festen  Wohnsitz  haben':  Auga- naia  nämc^  vardanam  ..  avadä  adäraya* Bh.2. 3;  ^.5.  9)  labsol.  'sich  halten, Stand  halten',  militärisch:  Aya^  mudaisuvä ma%tft<^  aht^  kami . .  naiy  adsrayi^  Bh. 2.6.
12877:Komp.).  a)  'Aufenthaltsort,  Wohnsitz, Schlupfwinkel'":  gaus  .  .  ya  •rwuÄK" mi^röjintjqm  ma^änam  .  . /raxarsta  (sd.) "das  Rind  . .,  das  zu  den  Schlupfwinkeln der  .  -  fortgezerrt  wird"  Yt  lo.  38.
13408:•  j.,  g.  'däman-,  d^man-''  n."  i)  im gAw.  'Stätte,  Wohnstatte'  in  eschato- logischcm  Sinn,  Plur.:  ai  hsi  'mqm  (NP.) ^■uiaAmT  a  dam  (Sp.  684  o.)  ahurä  Y. 4(9.  7  j  —  drüjh  kvS  -man  (AP.)  *haB>!ahy<'t gät  (sd.)  ".  .  zu  den  Wohnstätten  derer, die3>  .  ."  ^.46.(>.  2)  im  jAw.  'Ge- schöpf, geschatfenes  Wesen';  Sing,  und Du.  auch  kollektiv  von  der  Gesammtheit des  Geschaffenen,  'Schöpfung';  pauaSa  . . yat    mainyü    'man  (AP.)    dakU?m  yasta
15090:•  j.  paiti-stä-  f.  'Standort,  Wohnstätte': äha  .  .  nava.cil  mainyava  yazata  atjkava astvainti  paili.drqm  nStt  'stqm  vfn^nti "dann  finden  . .  durchaus  keinen  Aufent- haltsort und  keine  Wohnstätte  mehr"  Yt.
15095:•  j.  paiti-ätäna-,  "stana-**  n.  i)  'Stand- ort, \V'ohnstätte':  h5  imqm  dalnam  .  ./ra- pinaoiti  sattm  *°i'tananqm{G?.)''' hazannm faiti.daranqm  "der  bringt  diese  Religion zum  Gedeihen,  hundert  (neue)  Wohnstätten, tausend  (neue)  Aufentlialtsorte  (sinds  die er  ihr  schafft)"  V.^.3i)>.  2)  '(Gestell sva.)  Bein',  vom  Fuss  bis  zur  Hüfte:  'stäna F.Jg;  —  maihySi  'slUne  xräidisme  maiöyöi nars  vandusme  "bis  zur  Mitte  des  Beins (der  Beinhöhe)  in  hartem,  bis  zur  (Leibes)- mitte  eines  Mannes  in  weichem  Erdboden" V,Ä8;  *H.86.
=== BRT hazd/hid ===
```


## [2026-09-14T01:29:42.275Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk -v n=$((1075/2+12+1)) 'BEGIN{RS=\"\\f\"} NR>=n-1 && NR<=n+1 {print \"----LEAF \"NR\"----\"; print substr($0,1,1200)}' KLN_1966.txt"
}
```


### [2026-09-14T01:29:43.340Z] TOOL RESULT

```
----LEAF 549----
d  fr  prec.  word  with  suff.  -aceae. myricaceous,  adj.  —  See  prec.  w'ord  and  -aceous. myring-,  form  of  myringo-  before  a  vowel, myringa,  n.,  the  tympanic  membrane  ( anat .)  — ModL.,  fr.  ML.  miringa,  dissimilated  fr.  Late  L. meninga,  mininga,  fr.  Gk.  [xrjviyp,  gen.  [xv;- vtyyo c,  ‘membrane’.  See  meninx. myringitis,  n.,  inflammation  of  the  tympanic membrane  (med.)  —  A  Medical  L.  hybrid  coin¬ ed  fr.  myringa  and  -itis,  a  suff.  of  Greek  ori¬ gin.
myringo-,  before  a  vowel  myring-,  combining form  denoting  the  tympanic  membrane.  —  See
myringa.
Myriophyllum,  n.,  a  genus  of  plants,  the  wrater milfoil  (bot.)  —  ModL.,  fr.  Gk.  ixGpi6<?u>./.ov, ‘the  water  milfoil’,  which  is  compounded  of uupiop.  ‘numberless’,  and  cuXXov,  ‘leaf’  (see myriad  and  phyllo-);  so  called  in  allusion  to  the countless  divisions  of  the  leaves, myriorama,  n.,  a  large  picture  made  up  of  a  num¬ ber  of  small  pictures.  —  Compounded  of  myri- and  Gk.  op  a jxa,  ‘that  which  is  seen,  view,  sight’,
fr.  opav,  ‘to  see'.  See  cosmorama  and  cp.  words there  referre
----LEAF 550----
l  cured  of  leprosy  by  Elisha.  —  Heb. Na'aman,  lit.  ‘pleasantness’,  from  the  stem  of na'em  ‘was  pleasant  or  lovely’,  whence  also na'tm,  ‘pleasant,  lovely’,  nd'am,  ‘pleasantness, loveliness’,  and  the  PN’s  Na‘dmdh,  No‘dmt ;  rel. to  Arab,  na'ima,  ‘was  easy  or  pleasant’,  an'ama, ‘he  granted  a  favor,  favored’.  Cp.  cnam,  Naomi. Cp.  also  anemone.
Naassenes,  n.,  pi.,  a  sect  of  Gnostics  who  regarded the  serpent  as  the  symbol  of  wisdom.  They  were called  also  Ophites.  —  Fr.  Heb.  nahash,  ‘ser¬ pent’,  which  is  rel.  to  Arab,  hanash,  ‘serpent, viper’.
nab,  tr.  v.,  to  seize,  catch.  —  Prob.  a  var.  of  dial. E.  nap,  ‘to  seize’,  which  is  of  Scand.  origin ;  cp. Dan.  nappe,  ‘to  pinch’,  Swed.  and  Norw.  nappa, ‘to  snatch’.  Cp.  also  the  second  element  in kidnap.  Cp.  also  nobble.
Derivative:  nabb-er,  n.
Nabataean,  Nabatean,  n,,  1)  a  member  of  an  an¬ cient  people  of  Arabia;  2)  the  Aramaic  dialect spoken  by  this  people.  —  Formed  with  suff.  -an fr.  L.  Nabataeus,  fr.  Gk.  NaflaTcaog,  fr.  Arab. Nabatu,  which  is 
----LEAF 551----
 B  hem,  Hitt,  laman  (formed  with  dissim¬ ilation  fr.  *naman),  Arm.  a  mm  (gen.  anuan),  Gk. ovop.a  (dial,  form  ovup.a),  Alb.  emen,  L.  no- men,  OSlav.  ime  (gen.  imene,  imeni),  OPruss. emmens,  emnes,  OIr.  ainm,  OW.  anu  (pi.  enueiri), W.  enw,  Co.  hanow,  ‘name’.  Outside  Indo- European  cp.  Lapp,  namma,  Finn,  nime-.  Hung. nev,  ‘name’.  Cp.  agnomen,  allonym,  anonymous, antonomasia,  antonym,  cognomen,  cryptonym, denominate,  eponym,  Evonymus,  homonym, ignominy,  Jerome,  metonymy,  metronymic,  mis¬ nomer,  nom,  nomen,  nomenclator,  nomenclature, nominal,  nominate,  nominative,  noun,  nuncupa¬ tive,  onomastic,  onomato-,  paronomasia,  paro- nymous,  patronymic,  polyonymous,  praenomen, pseudonym,  renown,  synonym,  toponym,  trino- minal.
Derivatives:  name,  v.  (q.v.),  name-less,  adj., name-ly,  adv.
name,  tr.  v.  —  ME.  namen,  fr.  OE.  namian,  fr. nama,  ‘name’.  See  name,  n.
Derivatives:  name-able,  nam-able,  adjs.,  name- abil-ity,  n.,  nam-abil-ity,  n.,  nam-er,  n.
namesake,  n.,  a  person  having  the  same  name  as an  other.  —  Contraction  of  name's  sake.  Name¬ sake  lit.  denote
```


## [2026-09-14T01:30:02.529Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i,l in enumerate(leaves):\n    if re.search(r'\\*sed-|base sed-|sed-,\\s*.to sit', l):\n        print('leaf',i,'approx pages',2*(i-12),2*(i-12)+1)\n        for m in re.finditer(r'.{200}\\*sed-.{200}', l, re.S):\n            print('   ...',m.group(0).replace('\\n',' ')[:420])\n        print('---')\nEOF"
}
```


### [2026-09-14T01:30:03.747Z] TOOL RESULT

```
leaf 145 approx pages 266 267
   ... r-ed,  cedar-n,  adjs. cede,  tr.  v.  —  L.  cedere  (pp.  cessus),  ‘to  go,  go away,  yield,  give  up,  withdraw’,  prob.  for  *ce- zdere,  from  the  demonstr.  particle  ce-  and T.-E.  base  *sed-,  ‘to  go’,  whence  also  Gk.  6869, ‘way’,  OSlav.  chodu,  ‘a  walking,  going’,  choditi, ‘to  walk,  go’,  OI.  d-sad-,  ‘to  go,  approach’,  ut- sad-,  ‘to  step  aside,  disappear’.  See  he 
   ... ase, exceed,  excess,  intercede,  intercession,  necessary, precede,  predecessor,  procedure,  proceed,  pro¬ cess,  procession,  recede,  retrocede,  secede,  suc¬ ceed,  success.  —  I.-E.  base  *sed-,  ‘to  go’,  is  prob. identical  with  *sed-,  ‘to  sit’,  the  original  sense  of the  base  having  been  ‘to  place  (either  the  seat  in order  to  sit  down,  or  the  foot  upon  the  groun
---
leaf 150 approx pages 276 277
   ... Gk.  xxDaSpa, ‘seat,  chair,  pulpit’,  formed  fr.  xxtx,  ‘down’  (see cata-),  and  eSpa,  ‘seat’,  which  is  rel.  to  e^eaftxi, ‘to  sit’,  fr.  Gk.  base  *s8-,  corresponding  to I.-E.  base  *sed-,  ‘to  sit',  whence  L.  sedere, ‘to  sit’.  See  sedentary  and  cp.  cathedra,  cathe¬ dral.  Cp.  also  chaise,  which  is  a  doublet  of  chair. Derivative:  chair,  tr.  v. chair,  n.,  flesh 
---
leaf 272 approx pages 520 521
   ...  — Formed  with  suff.  -ic  fr.  Gk.  cSaipoc,  ‘soil; floor’,  which  was  probably  dissimilated  fr. ‘sSaipog  and  is  rel.  to  sSog,  ‘seat,  base,  foun¬ dation’,  fr.  stem  *kS-  (=  I.-E.  *sed-),  ‘to  sit’, and  cogn.  with  L.  sedere,  ‘to  sit’.  See  sedentary and  cp.  next  word. edaphology,  n..  the  study  of  soils.  —  Compoun¬ ded  of  Gk.  gSacpog,  ‘soil’,  and  -Xoyia,  fr. 
---
leaf 479 approx pages 934 935
---
leaf 557 approx pages 1090 1091
   ...  W. nyth,  Co.  neid,  Bret,  nez,  neiz,  ‘nest’.  I.-E.  *niz- do-,  stands  for  *ni-zd-o-  and  lit.  means  ‘a  place to  sit  down  in’,  fr.  *ni-,  ‘down’,  and  zero  degree of  I.-E.  base  *sed-,  ‘to  sit"  [cp.  OI.  ni-satsuh, ‘sitting’,  ni-sidati,  ‘sits  down,  settles’,  and  Gk. 6^05  (metathesis  for  *oz-d-os),  ‘branch’.  Arm. ost,  Goth,  asts,  OHG.,  MHG.,  OS.  ast,  MDu. aesl
---
leaf 575 approx pages 1126 1127
   ... dograph,  n.,  an  instrument  recording  the  dis¬ tance  traveled.  —  Compounded  of  Gk.  886?, ‘way’,  and  -yp X90?,  fr.  ypd^Eiv,  ‘to  write’.  The first  element  derives  fr.  I.-E.  base  *sed-,  ‘to  go’, whence  also  OSlav.  chodu,  ‘a  walking,  going’, choditi,  ‘to  walk,  go’.OI.  a-sad-,  ‘to  go, approach’, ut-sad,  ‘to  step  aside,  disappear’,  L.  cedere (for  *ce-zdere),  ‘to 
   ...   yield’.  Cp.  -ode, ‘way’,  and  anode,  cathode,  Diodia,  electrode, episode,  exodus,  hexode,  method,  parodos,  period, stomodeum,  synod.  I.-E.  base  *sed-,  ‘to  go’,  is identical  with  *sed-,  ‘to  sit’,  the  original  sense of  the  base  having  been  ‘to  place  (either  the seat  in  order  to  sit  down,  or  the  foot  on  the ground  in  order  to  go)’.  See  sedentary  and  cp.
---
leaf 632 approx pages 1240 1241
   ... m££etv,  ‘to  press’,  which is  cogn.  with  OI.  piddyati,  ‘presses,  oppresses', fr.  I.-E.  *pi-s{e)d-,  ‘to  sit  upon,  to  press’,  fr. *pi-,  short  form  of  *epi,  ‘on’  (see  epi-),  and  *sed-, ‘to  sit’,  whence  OI.  sidati,  ‘sits',  Gk.  Eqcadai, L.  sedere,  ‘to  sit’.  See  sedentary, piezometer,  n.,  an  instrument  for  measuring  the pressure  of  liquids  or  gases.  —  Compound
---
leaf 729 approx pages 1434 1435
   ... . zadel,  OHG.  satal,  satul,  MHG.  satel,  G.  Sattel, ‘saddle’,  OS.  *sadul  (whence  saduleri,  ‘saddler’). These  words  orig.  meant  ‘a  place  to  sit  upon’, and  derive  fr.  I.-E.  base  *sed-,  ‘to  sit’,  whence also  L.  sedere.  Cp.  L.  sella  (for  *sed-Ia),  ‘seat, chair’,  OSlav.  sedlo,  ‘saddle’,  and  see  sedentary. Cp.  also  sell,  ‘seat,  throne’, saddle,  tr.  v.  —  ME.  s
---
leaf 748 approx pages 1472 1473
   ... G.  saze,  MDu. seaward secure gesaete,  ‘seat’,  OHG.  gisdyi,  MHG.  gesiige, ‘seat;  siege;  situation;  buttocks’,  G.  Gesd.fi,  ‘but¬ tocks',  fr.  Teut.  base  *set-,  corresponding  to I.-E.  *sed-,  ‘to  sit’.  See  sit. Derivatives:  seat,  tr.  v.,  seat-ed,  adj.,  seat-er ,  n., seat-ing,  n.,  seat-less,  adj. seaward,  adj.  and  n.  —  Compounded  of  sea  and -ward. seaward,  seawards,
---
leaf 749 approx pages 1474 1475
   ...   mi¬ gratory  (said  of  birds).  —  F.  sedentaire,  fr.  L. sedentarius,  ‘pertaining  to  sitting,  sedentary’,  fr. sedens,  gen.  -ends,  pres.  part,  of  sedere,  ‘to  sit’, fr.  I.-E.  base  *sed-,  ‘to  sit’,  whence  also  OI.  d- sadat,  ‘sat  down’,  sidati,  ‘sits’,  Avestic  had-,  'to sit  down’,  Gk.  (for  *sezesthai ),  ‘to  sit’, ESpa  (for  *  sedra),  ‘seat’,  OIr.  suide,  ‘seat,
   ... ,  sedi¬ ment,  see,  n.,  sejant,  sell,  ‘seat’,  sessile,  session, sewer,  ‘servant’,  siege,  sizar,  size,  subsellium, subsidy,  supersede,  surcease,  synizesis,  tetrahe¬ dron.  I.-E.  base  *sed-,  ‘to  sit’,  is  identical  with base  *sed-,  ‘to  go’.  See  cede. Derivatives:  sedentary,  n.,  sedentari-Iy ,  adv., sedentari-ness,  n. Seder,  n.,  the  home  service  on  the  two  first  ni
---
leaf 751 approx pages 1478 1479
   ... len. Derivatives:  sell-er,  n.,  sell-ing,  n. sell,  n.,  1)  a  seat,  throne  ( obsol .);  2)  a  saddle (archaic).  —  ME.  selle,  fr.  MF.  (=  F.)  selle,  fr. L.  sella,  which  stands  for  *sed-la,  fr.  sedere,  ‘to sit’.  See  settle,  n.,  and  cp.  saddle, sellenders,  n.  —  A  var.  of  sallenders. Seltzer  water,  also  seltzer,  aerated  mineral  water. —  Contraction  of  G.  Selter
---
leaf 757 approx pages 1490 1491
   ...   *sedla),  ‘seat’,  L. sella  (for  *sedla ),  ‘seat,  chair’,  OSlav.  sedlo, ‘saddle’,  Arm.  etl,  ‘place’,  teli,  of  s.m.,  OE. sadol,  ‘saddle’.  I.-E.  *sedla-  is  an  enlargement of  base  *sed-,  ‘to  sit’.  See  sit,  sedentary  and  cp. saddle  and  sell,  ‘seat’. settle,  tr.  and  intr.  v.  —  ME.  set  ten,  settlen,  fr. OE.  setlan,  fr.  setl,  ‘a  seat’,  rel.  to  OHG.  gisi- dal
---
leaf 770 approx pages 1516 1517
   ... iltian,  ON.  sitja,  Swed.  sitta,  Dan. sidde,  OFris.  sitta,  MDu.  sitten,  Du.  zitten, OHG.  sizzan,  MHG.,  G.  sitzen,  Goth,  sitan,  fr. Teut.  base  *set-,  corresponding  to  I.-E.  base *sed-,  ‘to  sit’,  whence  OI.  sidati,  ‘he  sits’,  Gk. E^Eaffai  (for  *sedyesthai),  ‘to  sit’,  s8px  (for *sedra),  ‘seat’,  L.  sedere,  ‘to  sit’,  sedes,  ‘seat’.  See sedentary  and  cp.  words 
---
leaf 782 approx pages 1540 1541
   ...  sukrah,  ‘bright’, soot,  n.  —  ME.  sot,  soot,  fr.  OE.  sot,  rel.  to  ON. sot,  ODu.  soet,  lit.  ‘that  which  settles’,  fr.  Teut. base  *set-,  ‘to  sit,  set’,  corresponding  to  I.-E- *sed-,  ‘to  sit’,  whence  OSlav.  sazda,  Lith.  sudd- ziai  (pi.),  OIr.  suide,  W.  huddyl,  Bret,  huzel, ‘soot’.  See  sedentary.  For  sense  development  cp. sediment. Derivatives:  soot,  tr.  v.
---
leaf 814 approx pages 1604 1605
   ... h  suff.  -ive  fr.  L. subscriptus,  pp.  of  subscribere.  See  subscribe. Derivative:  subscriptive-ly,  adv. subsellium,  n.,  a  low  bench.  —  L.,  ‘bench,  seat’, fr.  sub-  and  sella  (for  *sed-ld-),  from  the  base  of sedere,  ’to  sit’.  See  sedentary  and  cp.  seat,  settle. Cp.  also  the  second  element  in  Limosella. subsequence,  n.  —  Late  L.  subsequentia,  ‘the  act of  fol
---
```


## [2026-09-14T01:30:28.886Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i in (548,549,550,551,552,747,748,749):\n    l=leaves[i]\n    print('leaf',i,'| head:',repr(l[:120]),'| tail:',repr(l[-120:]))\nEOF"
}
```


### [2026-09-14T01:30:30.086Z] TOOL RESULT

```
leaf 548 | head: "d  fr  prec.  word  with  suff.  -aceae. myricaceous,  adj.  —  See  prec.  w'ord  and  -aceous. myring-,  form  of  myr" | tail: '.  Mydaus.  For  the second  element  see  stoma.\nN\nNaaman,  1)  masc.  PN.;  2)  in  the  Bible,  an  Ara- mean  genera'
leaf 549 | head: "l  cured  of  leprosy  by  Elisha.  —  Heb. Na'aman,  lit.  ‘pleasantness’,  from  the  stem  of na'em  ‘was  pleasant  " | tail: 'namo.\n‘name’,  fr.  I.-E.  base  *enomen,  *onomen,  *no- men,  whence  also  OI.  nama,  Avestic  nama,  Toch. A  hom, '
leaf 550 | head: ' B  hem,  Hitt,  laman  (formed  with  dissim¬ ilation  fr.  *naman),  Arm.  a  mm  (gen.  anuan),  Gk. ovop.a  (dial,  ' | tail: 'h,  of  s.m.,  which  is  of  uncertain, possibly  Dravidian,  origin;  so  called  because orig.  narghiles  were  made'
leaf 551 | head: '  of  coconut  shells, narial,  adj.,  pertaining  to  the  nares.  —  Formed fr.  nares  with  suff.  -ial.\nI\nnark,n., ' | tail: "ci,  fr.  I.-E.  *gn-, zero  degree  of  base  *gen-,  *gene-,  'to  beget,  bear, bring  forth’,  whence  also  L.  gen"
leaf 552 | head: 'us,  ‘birth,  des¬ cent,  origin,  race,  sort,  kind,  class’.  See  genus and  words  there  referred  to  and  cp.  e' | tail: 'ail,  set  sail’,  lit.  ‘to  drive  a  ship’, fr.  *navigus,  for  *nav-agos,  ‘driving  a  ship’, which  is  compounde'
leaf 747 | head: '  ON.  skarpr, OE.  scearp ,  ‘sharp’  (see  sharp).  Cp.  Dan.  skurv, Swed.  skorv,  MDu.  scorf(t),  Du.  schurft,  O' | tail: ',  season-ed,  adj.,  season-er,  n.,  season-ing,  n., season-less,  adj.\nseat,  n.  —  ME.  sete,  fr.  ON.  sxti,  wh'
leaf 748 | head: 'ence  also Swed.  sate,  Dan.  sxde;  rel.  to  OHG.  saze,  MDu.\nseaward\nsecure\ngesaete,  ‘seat’,  OHG.  gisdyi,  MHG. ' | tail: "  ‘the  second'.  See second,  adj.\nsecundum,  prep.,  according  to.  — ■  L.,  ‘according to’,  fr.  secundus,  ‘the  "
leaf 749 | head: "second'.  See  second,  adj. securable,  adj.  —  Formed  fr.  the  verb  secure  (see next  word)  with  suff.  -able, " | tail: 'Derivatives:  seethe,  n.,  seeth-ing,  adj.,  seeth-ing- ly,  adv.\nsegar,  n.  —  An  obsolete  variant  of  cigar, seg'
```


## [2026-09-14T01:30:40.199Z] TOOL CALL #35: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'));print(json.dumps(d['FFD'],ensure_ascii=False,indent=1))\""
}
```


### [2026-09-14T01:30:41.292Z] TOOL RESULT

```
{
 "title": "Mohsen Abolghasemi, Fe'l-ha-ye Farsi-ye Dari, Qoqnus, Tehran 1374/1995",
 "kind": "local_scan_ocr",
 "url": "https://asmaneketab.ir/product/کتاب-ماده-های-فعلهای-فارسی-دری-محسن-اب/ -> https://dl.eliteraturebook.com/app/public/attachments/6925d29630b83.PDF (free PDF site; grey)",
 "lookup_hint": "Searched archive.org (Persian/Latin titles, author), ketabnak, noorlib, general web (pdf/download): nothing; only a related paid e-book 'واژگان زبان فارسی دری' (fidibo). ketabnak.com/book/45024 is a different book (فهرست فعلهای فارسی).",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_asmaneketab.pdf",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_pages_faseng.txt"
 ],
 "page_offset": "115 leaves (PDF pages); printed page = PDF page − 5 (PDF 40 = p.35). 2nd printing 1385 of the same Qoqnus setting (ISBN 964-311-015-X).",
 "covers_etymology": true,
 "notes": "Actual title is «ماده‌های فعل‌های فارسی دری» (Qoqnus). Open scan downloaded (image-only) and OCRed. Image-only scan OCRed locally with tesseract 5 (fas.traineddata from github.com/tesseract-ocr/tessdata_fast, stored in incoming/_tessdata). *_pages.txt = 'fas' model (best for Persian); *_pages_faseng.txt = 'fas+eng' model (better for the Latin-script Pahlavi/Avestan etyma, worse for Persian). Pages separated by \\f; leaf N = N-th \\f-block 0-based = PDF page N+1. Search with short substrings and tolerate OCR errors. Entries: headword, then 'فارسی میانه ... < ایرانی باستان *...' with Latin transliterations (best read in *_pages_faseng.txt or on the page image). | OCR text, printed = pdf-5"
}
```


## [2026-09-14T01:30:44.413Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD && python3 - <<'EOF'\nfor f in ('FFD_pages.txt','FFD_pages_faseng.txt'):\n    t=open(f,encoding='utf-8',errors='replace').read().split('\\f')\n    for printed in (43,78):\n        pdf=printed+5\n        p=t[pdf-1]\n        print('#####',f,'printed',printed,'pdf',pdf,'#####')\n        print(p[:1600])\nEOF"
}
```


### [2026-09-14T01:30:45.535Z] TOOL RESULT

```
Exit code 1
##### FFD_pages.txt printed 43 pdf 48 #####
[pdf page 48]
ماده‌های ماضی و مضارع فارسی دری ‏ ی ۴۳
پژمردن
در پهلوی اشکانی ۰2۲ از ایرانی باستان ۹-2۵7-2*ء به معنی «پژمردن» آمده
است. 8 نشانه‌ای بوده است برای ساختن مادهٌ مضارع از ربشه. ۷ پیشوند فعلی است.
ريشةٌ 2027 به معنی «پژمردن» است. از ۷۷781۲ پهلوی اشکانی «پژمر» به وجود آمده
است. «پژمرد» باید در پهلوی اشکانی به صورت ۷۷1-21۵۲۵ بوده باشد. از ۷,1-20۳-1۵*
ایرانی باستان. برای 2۵ > آراست. 7 صورت ضعیف ريشةٌ 27027 است.
پژوهیدن
«پژوهید» مادة ماضی جعلی است» در فارسی میانه ۷12581 آمده است.
پژوه < فارسی میانه ۷328.
پسندیدن
پسندید < فارسی میانه 02820676. 02820670 ماد ماضی جعلی است و از ماده
مضارع ساخته شده است.
پسند + فارسی میانه 028300 < ایرانی باستان 0211-8200-8*. برای 2 آرای. 030
پیشوند فعلی است. ريشةٌ ۶224 به معنی «به نظرآمدن» است.
پنداشتن
«پنداشتن» بازماندةٌ ۳هاققل 27 024 فارسی میانه است. 020: به» 5 اين» 43318:
داشتن» روی هم به معنی «به چیزی شمردل).
پوزیدن
«پوزید» مادهٌ ماضی جعلی است و از مادهٌ مضارع ساخته شده است.
پوز < فارسی میانه 062 < ایرانی باستان 2-[0۵0*. برای 2 + آرای. 8 صورت
اصلی [۳۵ است» [به جای 8 آمده است. مادهٌ ماضی 052 در فارسی میانه :00 بوده

##### FFD_pages.txt printed 78 pdf 83 #####
[pdf page 83]
۸ فعلهای فارسی دری
برای 1۵ -> آراست. 11 پیشوند فعلی است. ۸34 که صورت بالاندةٌ ريش 144 است.
صورت اصلی 538 است. 1 پس از آبه 5 بدل و 4 پیش از 1 به 8 بدل شده است.
تشان <ج فارسی میانه 81530. 8827 که در فارسی میانهٌ ترفانی مادةٌ مضارع 215291
است» صورت درست مادةٌ مضارع است. از ایرانی باستان ۸1-334-2*. برای 2 > آرای.
«آمدن» 2 به جای در 2538 ظاهراً به قیاس با 2518 و 315281 بوده است.
«نشاخت؛در فارسی‌دری به‌وجود آمده‌است. 134 صورت بالانده در معنی واداری به
کاررفته‌و 40 اصورت افزوده درمعنی لازمی.از 1124(«نشستن) به وجو د آمده‌است-> نشستن.
نبشتن» نوشتن
نبشت. نوشت + فارسی میانه 80151 < ایرانی باستان 19-18م-81*. برای 18 ->
آراست. 8 پیشوند فعلی است. 8 صورت ضعیف ريشهٌ هم به معتی «آراستن» است.
نبیس, نویس < فارسی میانه 118088 «- ایرانی باستان 81-0215-8*. برای 2 آرای.
نشست.۰
نشست << فارسی میانه 215281 < ایرانی باستان 81-5۵8-1*. برای ۵ > آراست. نط
پیشوند فعلی است. 124 صورت اصلی 888 است. 8 پس از آبه 8 بدل و 4 پیش از ۲آبه 5
بدل شده است.
تشین + فارسی میانه 21870 < ایرانی باستان ۸1-320-23*. 83 نشانه‌ای بوده است که
برای ساختن مادهٌ مضارع از ريشه به کار می‌رفته و 2 پیشوند فعلی است. 146 در معنی
لازمی و 234 در معنی واداری به کار رفته است > نشاستن.
نگاردن, نگاشتن ۱
نگارد < فارسی میانه 818370 < ایرانی باستان 81-137-1۵*. برای 1۵ > آراست. 2
پیشوند فعلی است. 137 صورت بالاندةٌ ريشه 127 به معنی «فکر کردن» است. نگاشت به
قیاس با 37و 1 به وجود آمده است.
نگار < فارسی میانه 21837 < ایرانی باستان 21-137-۵". برای 2 -> آرای.

Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
FileNotFoundError: [Errno 2] No such file or directory: 'FFD_pages_faseng.txt'
```


## [2026-09-14T01:30:56.583Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(len(t))\nfor i,p in enumerate(t):\n    if 600<i<680 and ('پسندید' in p or 'خرسند' in p):\n        print('#### leaf',i,'approx printed',i-224,'####')\n        for ln in p.split('\\n'):\n            if 'پسند' in ln or 'خرسند' in ln: print('   ',ln.strip()[:300])\nEOF"
}
```


### [2026-09-14T01:30:57.808Z] TOOL RESULT

```
777
```


## [2026-09-14T01:31:02.478Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nhits=[(i,p) for i,p in enumerate(t) if 'پسند' in p]\nprint('pages with پسند:',[i for i,_ in hits][:40])\nhits2=[i for i,p in enumerate(t) if 'خرسند' in p]\nprint('خرسند:',hits2[:20])\n# show leaf sample text to gauge OCR quality\nprint(repr(t[630][:500]))\nEOF"
}
```


### [2026-09-14T01:31:03.502Z] TOOL RESULT

```
pages with پسند: [500, 599, 630, 639]
خرسند: [57, 493]
'پربچه ی ۱ ۱ وت\nمخنور " مخذف پسواندو است که پسر ژن باشد\nاز شوهر دبگر با پسر شوهر باشد اززن دمگو»\nو بکس اول بروزن سکندر همآمده\u200cاست.\nبسنده؟ سٍ بروزن\u200cدهنده مخفف بند نده\nباشد که بمعنی بر گزیده است .* .\nپستگاگ* - بتتح اول و شالی و کاف\nفارسی و سکون ثالث وکاف » بیعنی تگراك وژاله\nباشد .\nپر یچ ۱ ح بارای\u200cترشت وتحتالی\nمجهول و جیم فارسی بروزن سرخیجه . بسران\nبدکاره - ومردم سفله را گویند .\nپس سر نمودن \u200f کنابه از دو\nکرداتیدن بخجالت باشد.. و کی را که مخل\nطبمت باشد بلطایف الحیل ازسروا کردن.\nپی شام - بائین قطه دار'
```


## [2026-09-14T01:31:08.391Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (629,630,631):\n    print('####### leaf',i,'#######')\n    print(t[i][:2500])\nEOF"
}
```


### [2026-09-14T01:31:09.428Z] TOOL RESULT

```
####### leaf 629 #######
حمشوق است.
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
پهلوی ۳)(5020 و ۳15428 , حتدی‌باستان - 81888, ارمنی
هناد .انبانی 5)20ا0 < اسعق ۰۰۳۱۷ کیلکی ۳540 ؛
غده‌های بزر که برسينةٌ جانوران که از آنها شیری فراود . دوغده
بزر که برسيتة آدمی که فزه وتا در کتر است و از آنها شیز
مقطح مت
یرون میا بد:
تهی‌دید پستان کاوش زشیر دل میزبان جوان کشت پیر .
فردوسی طوسی. «لفت نامه».
۵ پستاقك - بکسر اول وفتح پنجم ( از: منان ۵ پوند شباحت) »
ظرفی ازبلور با غیر آن شبیه بستان که مادران بی‌شیر» شیرحیوان با زنی دیگر
پتانك در آن‌کنند وبدهان طفل هند . * لفت نامه *.
۵ پسه ‏ بکر اول وشتح سوم» درتازی فستق ازآرامی فتفا (بکسراول), چه معا آن
شام ( سوربه ) است و بونانی نقل شد ۳۱50۵108 و از آن
بدیگر زبانهای ارویابی داخن شد . در ابتالیابی نمی 5)2ز۳ هه
«لفس» ؛ درختی است میوه دار که درآب و هوای معتدل واراضی --
سيك خوب میروید . مهمترین نوع آن همان یسته معمولی تک
( ۷۵۲2 ۱582012 ) است . مراکز مهم یس ابران کرمان,
آذرباجان» داعفان وفزوناست.رگ: فرهنگه روستابی۲۷۵ بعد بسله
وثابتی ۱۷۰ و کل کلاب ۰۲۱۷ ۱
۵ پسر - بکس اول وفتح دوم (درلهجةٌ مر کری) » در پارسی باستان واوستا ۳09072 ؛
پهلوی ۳فکنا۳ و کنام [ رك و ره سیون , کردی 15 . استی +5
واع1] , بلوچی 0۱1528 , وخی 0۵4۲ : شغنی 0۷6 . سربکلی ۳4: عنجی ۳۲ » ممرب
آن قور در قنفور؛ امه ها ور مه راک ممصص :ریات
#9" , نطنزی ۳0۲ <2 . ۱ص ۸۵ ۰ ۰ سمثانی ۳1۳ ۶ مشگکری و نرخةٌ
ولاسگردی0ا۳» شهمیرزاوی ۳6526۲ 4 ,۲ صس ۱۸۷ در فارسی نیز پس ویور؛ فرژند فرینه
این . ولد .
####### leaf 630 #######
پربچه ی ۱ ۱ وت
مخنور " مخذف پسواندو است که پسر ژن باشد
از شوهر دبگر با پسر شوهر باشد اززن دمگو»
و بکس اول بروزن سکندر همآمده‌است.
بسنده؟ سٍ بروزن‌دهنده مخفف بند نده
باشد که بمعنی بر گزیده است .* .
پستگاگ* - بتتح اول و شالی و کاف
فارسی و سکون ثالث وکاف » بیعنی تگراك وژاله
باشد .
پر یچ ۱ ح بارای‌ترشت وتحتالی
مجهول و جیم فارسی بروزن سرخیجه . بسران
بدکاره - ومردم سفله را گویند .
پس سر نمودن ‏ کنابه از دو
کرداتیدن بخجالت باشد.. و کی را که مخل
طبمت باشد بلطایف الحیل ازسروا کردن.
پی شام - بائین قطه دار بر وزن
بدتلم» بمعنی سحورباشد» وآن .طعامی‌است که در
ایام رمتان تردمك بصح‌خور نف.
سغده با عن نقطه دار ودأل بی نفطه: بسو ده بروزن نبوده» ممعنی‌دست‌زده
ودست زسثه و دست‌هالمده باشدب وسوراخ کرده را
یز گویند؟ .*
پسها نت۷ - باهای هوز و نون وتای
فرشت بروزن صفراشکن ۰ بلغت‌زند و باز ند )۱(
بمشی افثاندن پاشد و پسهانمی بممنی افثانم .
و پسهانید بعنی بیفشانید .8
برودت طقحه: ماده وعهیا ساخته باشد۴ ۴
پ ی گوش افکندن ۰ کنابه از
قراموش کردن بانشد .
پسند؟ - بر ون سمند ؛ قبول کرده
ویترقه باشد - و قبو ل کننده رانیز گوند.
پسنالر - ینم اول و فتح دال بر وزن
٩‏ سپس + یچه ( ابچك پهلوی علامت تسفیر و تحقیر ) . ۴ رك : فده
و مدیدن . ۴ - پارسی باستان -80) +۰ 11۳2 ۵ : اوستا 584 ( شستن) , قس :»
حندی‌باستان 28004 (سندلی) «امشق ۳۱۹). نبرک کلمُ‌پهلوی4ظ2598را از284عاه0ه
لز ۵0۵12-59002 (بنظر آمدن) داسته . فی : خرمند «یی رکه 4۳-۱۷۲ .
۴ از: بسن (ه م) + ه (شبت) :
آنچیست زکردار پسد که توالت آن‌چیست زنیکوبی وخوبی که‌نداری؟
فرخی سیستانی . «لفت نامه».
۵ - ظاهر! مسحف کلم مك « لفت‌نامه » با بشکك است. ۹
۴ 4 : پاتن . . .
6 پستدشی - بفتح أول ودوم وششم 1 از: بنند (ه .م) (-بدن (پسوند مصدر) [ بپلوی
093780 «ارنوالا 0۷۶» : «کفتم ( احمدبن ابی‌دواد) : اف ان با امپرالمومنین ! که ان
خولی است وایزد عزذکرء نسندد.» «تارئخ بیهقی ۰۱۷۳ . ۱
۵ پسووی - جتح اول وچهارم. رك: سودن. ۵ پسوند - بفتح اول وسوم» ره :
ملواف ‏ ۶ پسیی - بفتح اول. مر کب از: پس - بن (پسوند شبت) ویهلوی 82418
(فز یی آینده)؛ آخرین, اخیر؛ خلاف ختی :
ت اضف 9 ۱ بقبه درصفحعه 1۰۷
####### leaf 631 #######
ییان سیزدهم
در بای فارسی باشین نقطه دار مشتمل برشصت لغت د کداهت
کزر با زای نقطه دار ۰ وا اعلمه .
دشت عم یشم أول بر وزن مشت» معروف
است‌و رین یر ع رات ۱ ویناه و یشتیبانب
و بیرون هرچیز را نیز کوبند - ونلم پلدماست
در نواحی تیشابور مشتمل بردوست وست‌دخش
قربه وچون این‌بنده بمنزلة پشتی باشد نیشاپوررا
بدین تلم خواننه ۷ - و تلم ۳ج
از ولات‌بادغیی در خراسان۸ - وحیزومختت‌را
پیز گوند .
شتاده - بی وزن رخساره ». مخقف
پشتواره است وآن مفداری باشد از هر چیز که
به پشت نوان برداشت* .
پش « بفتح ارل و سکون ثالی » موی
کردن وک کل اسب راگونند! - وطره‌ای که بر
سردستار و کم رگذارند و فش معرب آئست -
و نات وفرومایه از هرچیز باشد - وشبیفونظیر
و ماشدرا نیز کفته‌ادد ۴ - و بضم اول جفد را.
کونند ۴ وآن پرندم‌ایست نامبارگ و بکراول
مخف پیش باشد؟ .
بشام - بر وزن سلام ؛ هر چیز نیره
رتکه راگوشد ۱
یشان » بنتم اول » بررزن و عمنی‌چشان
ی
نوشته بودند بانال تقطه‌دار. ودر دوفرهنگهدیگی
- کفلهاتی گرد و یش و دم دراز بر وبال فریی و لاغر یفن
پوربپای جامی. «لنت نلمه» .
؟ ‏ رك : فتي ور : ص له از ده مولف. ۴ - ر: پشكه .
ط وق شقن  »‏ ظاعراً ميچيك از درسنی که صاحب برعان بهیتان داده
صحیم لیست چمخود اودر کلمهُ اعزار جشان» بعنی کرمةالبیناه میگوید معنی آن هزار کزاست
چدچشان بمعنی «کزه , باشد واگر اين دعوی صاحب پرها که میگوبد پثان « شان» است‌سحیح
اشدنلةکذرن لظکزر يچيك ستبکه هرد مسحفه کزه است وااملزت نم
, اوستا ۳2۳۵/04 ( پشت ) , پپلوی ۳۷15۳۸ . هندی باستانی ات۳۲5 , (قطاطویم‎ . ٩
۰ ۳۷۲۱ کردی ۳1994 . زازا 2251 ء افتانی ۳0۵1۵6 » بلوچی کی ۷ « استق‎
کربرمن ۹۷ ۰ . کیلکی )نکنام . ۷ - مرب آن به بشت بضم اول » شهری منواحی‎ +
یخاپود وان کوومایت که قمیةٌ آن طیبئیث ( نرهیز) است وگو یشک مدین تلم‌خوانده شده زرا‎
آن بمتر له به بشت است نبشابور را و شامل ۲۲۹ قربه است ت از جمله کندر که ابرضر کندری وزیر‎
ر4 : مشتو‎ ٩ . مدان متسوب است. «معجم البلدان» . ۸ مراد بست است. رك: بت‎
4۰5٩ ها زصنحهٌ‎
شین فطرت پسین شمار توبی, خوبشتن را ببازی مدار . فرنوسی طوسی .
- مایین ظهر وغروب وصر .« از ملخص اللفات حسن خطیب کرمالی ». نم سین +
نمازعصر.«لهت نامه», درف یز ندی و نطنزی حصلحاکزن, مر لین 0 (ظهی) دك. :اص ۰۲۸4 در
لهج اطراف اسفهان ۳۵/۸1۳ (صر) . درخواداری 00عام «سالنامة فرهنگه کثیابکان 4۷*.
```


## [2026-09-14T01:31:36.909Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== NYB passand/xwarsand ===\" && grep -n \"passand\\|pasand\\|hu-sand\\|xvarsand\\|x^varsand\\|sand-\" NYB_vol2_glossary.txt | head -20"
}
```


### [2026-09-14T01:31:36.960Z] TOOL RESULT

```
=== NYB passand/xwarsand ===
1236:dätistän [d'tst'n'; DYN?] decision 451. 68 title. 818. 1054; judgment 7274; as opposed to passand (g. v.): a judgment which exceeds the formal prescriptions of the law, the utmost rigour of the law 70! [in other cases also: favour awarded above the formal prescriptions of the law]; ménóyé ~ the Heavenly Justice (personified) 7712; kar um (as a hendiadys) proper use 41%; lawful, righteous deeds
2067:hu-passandakéh [hwpsndkyh]: pat dat ~ in accordance with good equitableness in legal matters 64!’, v.s. v. passand.
2970:passand
2987:passand [psnd] lenity, in a juridical sense: reduction of what the law formally pre- scribes in any special case, as opposed to dätistän (g. v.), 701. — passand and dätistän are symmetrically opposed juridical terms, defined and exemplified in the Syriac Corpus iuris of I$6*boxt (Syrische Rechtsbūcher, ed. by Sachau, III, 1914, 12-14): — Suppose a man owes a sum and equally as much in interest fallen due, but cannot pay the sum total be- cause of poverty, illness, or the like; if then, at his request, the creditor remits the interest and rests content with the capital, this is passand. On the other
2989:passand
2990:side: though according to law a daughter only inherits half as much as her brother, yet, in order to prevent the fatality that she, as a poor maid, must remain at home and suffer the contumely of not being married, she may be given the same share in the inheritance as her brother: this is beh-dädastäneh (Phl: veh-dätistäneh) ‘surplus award’. — Paz. NP pasand; < *pat-sand-, v. next w.
2991:passand- [psnd-] pres. to approve: Ohur- maed ... hec vattarēh u drēžanēh ne pas- sandét 7954. — < *pat-sand- from pati + Av. (1559 sq.) tsand-, cf sahistan. MPrth psynd- ‘appreciate’, Ghilain 55.
3008:homänäk, pat mānākēh similar(ly); pat nazdikéh i 7418 (pat han + fraškart nazdikéh 106%); apar pat han jaman ka 4123, adak apar pat jamān 61°; pat yuvat hac; — frame prep.: pat... rād (g. v.). — ll. in composition with a subst., forming adjectives with the sense of ‘provided, connected with’: yam i pat-göhr set with jewels 6°; (murvdn i) pat-àp aquatic 93°; zan i pat-göhr a woman of good birth 69%; cigon andar hindükän pat-vicin but high of station 11819-11; — enlarged with the adj. ending -ömand: ka krisäsp pat-tanómand u (pat-)janomand ne bit hah if K. had not been endowed with body (pat-tan) and life (pat-jān) 342. — B. adv. (rare): in addition, moreover 96%; u pat-ic and furthermore 904. The proper adv. be- longing to pat is patiš (g. v.). - OIr *patt (Skr prati), Av. (822 sqq.) pasti, OP patiy; MPrthPrs pd, pt; Paz. pa. In all prob- ability this pa was since old in common use alongside of pač as its sandhi form (cf passaxt, passand etc.), and on it the spelling of the prep. was based by analogy with the Semitic prepositions b-, k-, l-. As however, contrary to the Sem. ws., it maintained its character of an independ- ent w., and independent ona-consonantic
3373:not grieve! 359; hakar šmah bagän sahet if it please Your Majesty 19-27, passim; - governing a clause with ki: apt-mān eton sahist ku it seemed to us that 86-7; 3812-13, 569-9. 7834, — Av. (1559) Isand-, pres. sadaya-; OP pres. 0adaya-; MPrs pt. shyd, Verbum 171; the Pazandists (Mx, SGV) give for MDMHn- the equivalent Sthastan ših- (of obscure etymology).
4318:xuan-sand [hwnsnd] contented, happy with what one possesses, ‘‘not jealous of other people's greater prosperity" (cf FrP 30), magnanimous 1312, 3725, 661. — MPrth hwnsnd-yft (S); MPrs hwnsnd (BBB). From z"an- = xtar- ‘sun’ (v. s. v. axvar-xšēt) and (Av. 1559) sand- ‘to be, become visible’, v. s. v. sahistan and pas- sand, thus ‘having a sunny look’, ‘of sunny disposition’ (Benveniste). Also xtar-sand = Paz. NP.
5320:lsand-: passand
6769:patmoxtan pašsār: patisär padvazed: pat-vac- padyavand- patiyavand pšč: pad paēdā, paidà: paitäk pačma(n): patman pačvand: patvand pačvastan: patvastan pahalim, pahlum : pahlom paharčxtan, paharčž-: pahrčxtan parastidan: paristätan pardazašn: pardaxtan pasand: passand pasaxt: passaxt päsux: passaxu paščman, -màni: pašč- mančh patit: patit patkàr: ~ päya: pädak péda: paitäk pédabar: paitäm-bar pčrož: pérdz pēš: ~
```


## [2026-09-14T01:31:38.536Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== MON metod/anod/katod ===\" && grep -c \"\" MON_part1.txt MON_part2.txt; grep -n \"متد\\b\" MON_part1.txt MON_part2.txt | head -5; grep -n \"کاتد\\|آند (\\|آنُد\" MON_part1.txt MON_part2.txt | head -5"
}
```


### [2026-09-14T01:31:38.736Z] TOOL RESULT

```
=== MON metod/anod/katod ===
MON_part2.txt:94500
MON_part1.txt:99339
MON_part1.txt:288:متداول در فارسی؛ لغات اروپائی که بتدریج در فارسی وارد شده و اعلام 
MON_part1.txt:377:۱ -فرهنگ بزرگ معین شامل کلية لغات متداول در فارسی که مزایای زیر را 
MON_part1.txt:716:عهد صفویه متداول بوده.) صائا - صائب 
MON_part1.txt:3927:پا کستان و هندوستان هنوز متداول است.) 
MON_part1.txt:5665:متداول» مرسوم. . شیوه» آهنگ. صفت. 
MON_part1.txt:4690:یک نمک محلول نقره در کاتد رسوب
```


## [2026-09-14T01:31:51.492Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^آنُد\\|آند\\b\" MON_part1.txt | head -10; echo ---; grep -n \"کاتد\" MON_part1.txt MON_part2.txt | head -10; echo ---; grep -n \"متد \" MON_part2.txt | head -10; echo \"--- page markers ---\"; head -5 MON_part1.txt; grep -c $'\\f' MON_part1.txt MON_part2.txt"
}
```


### [2026-09-14T01:31:52.570Z] TOOL RESULT

```
1285:خادمان و ستوران آنداری در دستگاه 
5052:آندون: (ی.) آنجا؛ سق. ایدون» 
10208:دهد؛ آندام. 
16473:در دل آنداختن. (سصل) در دل افتادن. 
17746:آندوهگسار: 2.۲ [- اندهکسار] (افا.) 
28634:کردن» چیزی آندار را از الک و مانند آن 
39999:ترغیب: دآندا [ع. (مسصع.) خواهان 
56385:آندوختن. 
58093:خوشاب: (-2۵5 (ص مر .) سیر آت؛ آندار 
58899:ترکیب گاه به معنی «دارنده» آید: آندار. نیز 
---
MON_part1.txt:4690:یک نمک محلول نقره در کاتد رسوب 
---
1518:آن بیماریی ممتد آرد و گاه منجر به هلاکت 
18389:و جلو ممتد است.) در قاعده کاسه سر 
23200:چیزی به سب کشیده شدن دو سر آن. ممتد 
23746:کشش). (مصع.) امتداد دادن» ممتد کردن 
23770:مستقیم و ممتد بلند و دراز. . (.) (عم.) سیلی» 
44804:مستد نه: (۵-)- ۱2200۸06 [ع. ممتد ثه ] (افا.) 
58467:مصحف: آعطاقعمتد [ع.] (افا.) کسی که در 
81618:نیز سابقه‌ای ممتد دارد. اعراب سازی بادی 
83285:وسیع. . طل وارف: سایه دراز و ممتد (ارب 
92220:صدای بلند و ممتد برای اظهار شادی و 
--- page markers ---
0 
2 


چم 
MON_part2.txt:0
MON_part1.txt:0
```


## [2026-09-14T01:31:58.047Z] TOOL CALL #43: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-14T01:31:58.058Z] TOOL RESULT

```


```


## [2026-09-14T01:32:01.925Z] TOOL CALL #44: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%86%D8%AE%D8%B3%D8%AA",
 "prompt": "Give the full etymology section for Persian نخست (naxost) 'first' — Middle Persian form, Proto-Iranian reconstruction, any cognates and whether it is connected to nazd/nazdišta."
}
```


## [2026-09-14T01:32:03.822Z] TOOL CALL #45: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AE%D8%B1%D8%B3%D9%86%D8%AF",
 "prompt": "Give the etymology of Persian خرسند (xorsand) 'content, satisfied' in full: Middle Persian form, the elements it is analysed into, and the root."
}
```


### [2026-09-14T01:32:06.236Z] TOOL RESULT

```
# Etymology of Persian نخست (naxost)

**Middle Persian form:** nxwst (naxwist, "first")

**Proto-Iranian reconstruction:** *naxwist- ("first"), derived from *naxu- ("first, in front, high")

**Cognates:** Northern Kurdish nexrî ('first-born'); Old Armenian նախ (nax), which is "an Iranian borrowing"

**Origin note:** The Proto-Iranian root is "of uncertain origin, with no known cognates outside Iranian."

**Regarding nazd/nazdišta:** The provided content makes no mention of any connection between نخست and nazd or nazdišta, so I cannot address that relationship based on this source.
```


### [2026-09-14T01:32:07.632Z] TOOL RESULT

```
# Etymology of Persian خرسند (xorsand)

According to the Wiktionary entry, this adjective is "Inherited from Middle Persian \[script needed\] (hwnsnd /⁠hunsand⁠/, 'happy, contented')."

The entry provides the Middle Persian form **hwnsnd** with the phonetic value **/hunsand/**, but unfortunately does not break down the word into its constituent morphological elements or identify an underlying root. The etymological information given is limited to establishing the direct descent from the Middle Persian ancestor form without further analysis of how that form itself may have been constructed.
```


## [2026-09-14T01:32:14.835Z] TOOL CALL #46: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%BE%D8%B3%D9%86%D8%AF%DB%8C%D8%AF%D9%86",
 "prompt": "Give the etymology of Persian پسندیدن (pasandidan): Middle Persian form, Proto-Iranian root, prefix analysis, and the PIE root if given."
}
```


## [2026-09-14T01:32:15.848Z] TOOL CALL #47: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/anode",
 "prompt": "Give the etymology of anode, and any mention of cathode, Greek hodos, Faraday/Whewell coinage date."
}
```


### [2026-09-14T01:32:19.077Z] TOOL RESULT

```
# Etymology of Persian پسندیدن (pasandidan)

**Middle Persian Form:**
"From Middle Persian [script needed] (psnd-ytn' /⁠passandīdan⁠/)"

**Proto-Iranian Components:**
The word combines two Proto-Iranian roots:
- *pati-* meaning "towards" 
- *sand* meaning "to seem good"

**PIE Roots:**
- *pati-* derives from Proto-Indo-European "*préti*"
- *sand* derives from PIE "*(s)kand-*" and is cognate with Sanskrit *cand* ("to gladden")

The verb ultimately means to approve, endorse, like, choose, or select—essentially expressing the notion of something appearing good or pleasant.
```


### [2026-09-14T01:32:20.322Z] TOOL RESULT

```
# Etymology of Anode

**Origin and Meaning:**
The term "anode" was coined in 1834 from Greek *anodos*, meaning "way upward." It combines *ano* ("upward") and *hodos* ("a way"). The word references "the path the electrical current was thought to take."

**Coinage:**
Rev. William Whewell, an English polymath, proposed the term, and English chemist-physicist Michael Faraday published it in 1834.

**Related Term - Cathode:**
Cathode, also from 1834, derives from Greek *kathodos* ("a going down, a way down"), combining *kata* ("down") and the same *hodos* root. It represents "the negative pole of an electric current" and was similarly proposed by Whewell and published by Faraday, named for the opposite current path.

**Note on Hodos:**
The Greek word *hodos* itself has "uncertain origin," though etymologists have proposed various Indo-European connections.
```


## [2026-09-14T01:32:30.001Z] TOOL CALL #48: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/method",
 "prompt": "Give the etymology of method (Greek methodos, meta + hodos), and also anything on episode and period on this page."
}
```


## [2026-09-14T01:32:31.074Z] TOOL CALL #49: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/episode",
 "prompt": "Give the etymology of episode: Greek epeisodion, its analysis into epi + eis + hodos, and the semantic history."
}
```


### [2026-09-14T01:32:33.924Z] TOOL RESULT

```
# Etymology of Method

**Method** derives from Latin *methodus*, which came from Greek *methodos*, meaning "scientific inquiry" or "method of inquiry." The Greek term combines two elements:

- *Meta*: "in pursuit or quest of"
- *Hodos*: "a method, system; a way or manner," literally "a path, track, road"

The word entered English in the "early 15c." with the sense of "regular, systematic treatment of disease," and gradually expanded to mean "any way of doing anything" (1580s) and "orderliness, regularity" (1610s).

---

**Regarding Episode and Period:** The page provided contains no information about these words. Only the etymology of *method* and related terms like *methodical*, *methodist*, and *methodology* are documented on this resource.
```


### [2026-09-14T01:32:35.604Z] TOOL RESULT

```
# Etymology of Episode

**Greek Origin**: The word "episode" comes from Greek *epeisodion*, meaning "an episode" or literally "an addition."

**Structural Analysis**: This Greek term breaks down into three components:
- *epi*: "in addition"
- *eis*: "into"
- *hodos*: "a way, path; a journey; a method, system"

**Semantic Development**: The word initially referred to "commentary between two choric songs in a Greek tragedy" and "an incidental narrative or digression within a story" (1670s). Its meaning later expanded to denote an "outstanding incident, experience" (first recorded in English in 1773), and eventually applied to individual broadcasts of serial radio programs by the 1930s.

The ultimate source of *hodos* remains uncertain, though it may relate to Sanskrit and Avestan words meaning "to go" or "to tread."
```


## [2026-09-14T01:32:39.689Z] TOOL CALL #50: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D9%85%D8%AA%D8%AF/",
 "prompt": "Quote the فرهنگ معین (Mo'in) entry for متد — including any bracketed origin tag such as [فر.] and the meaning given."
}
```


## [2026-09-14T01:32:41.025Z] TOOL CALL #51: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%DA%A9%D8%A7%D8%AA%D8%AF/",
 "prompt": "Quote the فرهنگ معین (Mo'in) entry for کاتد — including any bracketed origin tag such as [فر.] and the meaning given. Also any entry for آند."
}
```


### [2026-09-14T01:32:42.758Z] TOOL RESULT

```
# Farhangi Mo'in Entry for متد

According to the Farhangi Mo'in dictionary included on this page:

"(مِ تُ ) \[ فر. \] (اِ. ) روش ، قاعده ."

This entry indicates the word derives from French and defines it as "method" and "rule" in Persian.
```


### [2026-09-14T01:32:45.868Z] TOOL RESULT

```
# فرهنگ معین Entry for کاتد

According to Farhang-e Mo'in:

"(تُ ) [ فر. ] (اِ. ) ۱ - قطب منفی لامپ الکترونی که بر اثر گرما الکترون گسیل می کند. ۲ - پایانه یا الکترود منفی"

This translates to the negative pole of an electron tube that emits electrons through heat, or a negative terminal/electrode.

## Entry for آند

The dictionary does not provide a separate فرهنگ معین entry for آند on this page. However, the general encyclopedia section describes it as the counterpart to کاتد in electrical systems, where positive ions move toward the کاتد while negative ions move toward the آند.
```


## [2026-09-14T01:32:59.618Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Hürde\\|Hurde\\|Pferch\" BRT.txt | head -10; echo \"--- hastra ctx ---\"; sed -n '29670,29680p' BRT.txt"
}
```


### [2026-09-14T01:32:59.730Z] TOOL RESULT

```
15884:•  j.  pasuä.hasta-m,,'hastay-m  'Hürde, Pferch    für    Kleinvieh,    Schafe":    mai\ySi
18643:•  j.  nava.n3mata-  Adj.  'mit  neun  (als Scheidewände  dienenden)  Hürden  aus  Rei- sig' :  nmätum  gävayatum  nava.hä'i  rim 't»m  "einen  Rinderstall  mit  neun  Pferchen und  neun  Reisigscheidewänden" ''  V.  i4'  1 4.
18644:Pü. :  g  namat.  —  ')  Um  neun  Pferche  von einander  zn  trennen,  genügten  allerdings  acht Zwischenwände.     Aber  -.
18660:•  j.  nava.häftra-  Adj.  'mit  neun  Abtei- lungen, Pferchen':  n/nämm  gävayamm ''!hrvm  nava.n^mafym  (sd.)  V.  74.  14.
18947:•  j.  n«mata-"  m,  1)  'Reisig':  nasui  tga- 'kaite  .  ,  7flä(i  .  .  'tS  tarS  yan  "die  A''. verschwindet . .  wie  übers  Jahr  das  (dürre) Reisig"  V.p.  46'';  —  avi  Um  spayUt  . . vJspaca  avi  tiyra  *-ia  ".  .  und  auf  lauter spitzes  (dorniges)  Reisig"  V.J.35; — katgAus .  .  äraasca  *'taheca  ayanheca  "die  Nutz- niessung  von  Holz  und  Reisig  und  Eisen- gerät"  V.5.38.  2)  'Geflecht  aus  Reisig, Hürde'  (nur  Komp.),
29824:•  j.   häBra-  n.   1)  'Abteil,  Pferch'  (nur
--- hastra ctx ---
V.  14.  4=^>  Vt.  J.63;  — M^a-ra^ff  ..pairi.- '  ''supetl.  au»  ^kani-t).  —  ai.  .tflK<J«a-  Adj.  -
anhariiäbyB  Yt5.8.  '       Yv..:kandäxtärtumit;rpaahTäkih,  Sü.:  laglm-
mit    /mW    und  fra    '(SaraenflUssigkeit)  '       haHalaniam  punyma  iaslrena.  —  ')  Eine  greu-
enüassen':  "anya.tkaliais^)  näirika pairi      "='"'  Etymologie  bringt  Dst.  ZA.  /.  «3- xsudra  fraipharTsaiW^  Nik.  7.  •  j.hastra- n. 'Versammlung' uzw.  solcher,
mit/^j  i)'(eineWaffe)schwingen,schleu-  die  fUr  sich  einen  gemeinsamen  Gotics- dern(od.dgl.)':  s.  y^flwÄawl'a-.  2)  absol. :  dienst  abhalten  lassen'':  yS  *bil.hastnm 'Samen (flüssigkeit)  ergiessen,  begatten',  von  srävayäti  ratufryS^'>  *%ris.hastnm  srä- 1\tXGa:  y6{ri3.xsiLuströ)  arsnam/rauÄ3r>-  vaysnii^''  ivat  nitimsm  'rtm  aiskai  *ratu- sintqm    mazi^btn    aejS    übaraiti    Vt  14.  fritH  '^ri/*>  "wer  für  eine  Versammlung
BAiTüai-aHAi,  Attüu.  Wh.  57
dby  Google
I79S
haz-
hazanra-
1796
```


## [2026-09-14T01:33:17.970Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== WLD Bd2 sed ===\"; grep -n \"sed-\" incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt | head -15; echo \"=== WLD band3 ===\"; grep -n \"nazdyo\\|nazdišta\\|pasuš\\|syazd\" WLD_band3.txt | head"
}
```


### [2026-09-14T01:33:18.045Z] TOOL RESULT

```
=== WLD Bd2 sed ===
515:und Wz. sed- bei Kluge® s. v. aus; noch andere Deutungen von fest verz. 
19467:stufiges Praes. (vgl. lit. sed-mi, ed~mi), vgl. ai. marsti: mrjdnti; daraus 
21859:Ygl. idg. '^ni-’Zdos unter sed- „sitzen“. Als „heruTiterinachen‘‘ 
29969:"^sed- „sitzen'' gehdrige sedi- „Entkraftung, Yerkoramenheit“ yergleicht); 
29971:Zuteilung dieser kelt. \Ydrter fiir „Friede‘' zur \Yz. ^sed- „sitzen“ durch 
31299:sed- 
31318:sed- „sitzeD“, z. T, mit einer Basis sede\i \ : sedl-. 
31387:se{i)d-^ wozu sed- Ablautsneuhildung sein miiBte. Ygl. Osthoff Pf. 414f., 
31431:sed- 
31466:setJialj sedal n. m. „Sitz, Wohnsitz, Ruhesitz, Statte'^ (idg. ^seilo- aus ^sed- 
31470:Koreen Ltl. 200; Falk-Torp u. sadel)\ daneben (im ar. geneuertes?) "^sed-iloni 
31502:sed- 
31533:B. ^sed- in der Bed. „gehn^; 
32636:„fundus, Dorf'* (verschieden von dem zu sed- „sitzen** gehorigen sloven. 
32659:„Sohle**; aber lat. solium s. u. sed- „sitzen**; iiber abg. slcnie „Balken**: lit. 
=== WLD band3 ===
```


## [2026-09-14T01:33:19.910Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SYN sit ===\"; grep -n \"sed-, 'sit'\\|sedeo\\|OP hadiš\\|Av. had-\" SYN.txt | head -10; echo \"=== IEC sed ===\"; grep -n \"sedō\\|sedo 'I sit'\\|hodos\" IEC.txt | head -10"
}
```


### [2026-09-14T01:33:19.997Z] TOOL RESULT

```
=== SYN sit ===
21290:siitan, OHG sizzan, etc., Seneral Gimp. Lith. sédéti, Lett. sédet; ChSI. ster ot,° general Slavic, beside perfect, Ssésti ‘take a seat’; Skt. sad-, Av. had-.
22197:Av. asne, loc. sg. of adj. *asna- (fr. *a- zd-na- pple.) fr. root *sed- ‘sit’ (Skt. sad-, Av. had-, etc.). Walde-P. 2.485. Barth. 220.
=== IEC sed ===
```


## [2026-09-14T01:33:27.334Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '31299,31320p' incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt; echo \"......\"; sed -n '31400,31440p' incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt; echo \".....\"; sed -n '31525,31560p' incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt"
}
```


### [2026-09-14T01:33:27.433Z] TOOL RESULT

```
sed- 


483 


Hochzeitsbrauch die Frau des Manaes Hand ergreift (Bruckner KZ. 45, 
318), aruss. sjagnufh, posjagath ,,yafieip'' und unnasaliert (vgL s^dq :sadz) 
aksl. sagati posaqati^ posaqnqti „nubere“, posng^ „Hochzeif cech. 

posah „dos‘‘ usw. Uhlenbeck Ai. Wb. 325 (gegen Verb, von sqgnqti mifc 
seg- „heften", die z. B. bei Pick 137, 324, HP 428, Brgm. IF. 32, 320 f.). 

Dazu wahrscheinlich gr. od'hog n. „Kraft^^ (Bolling [AJPh. 21, 316], Brgm. 
BSGW. 1906, 176 a 1, gegen Sommers GrLtst. 65 ff Deufcung als nach uevog 
erfoigter Umbildung eines '^o^dvog aus *ora-ovog : ai, sthd-snu- ^unbeweg- 
lich, aushaltend“, Wz. sta- „stehn“); zum Formans von ^zg^h-mo-s- vgL 
Brugmannll^ 1, 268, 526. 

sed- „sitzeD“, z. T, mit einer Basis sede\i \ : sedl-. 

Ai. sad- {sdtsi, dsadat, Pf. sasada^ scdima^ sedivas-, vgl. av. hazdya-t opt.); 
......
ap. hadis- yjWohnsitz, Palast“ (idg. ss oder “is); dehnstufig anord. satr 
(^setiz) n. ^Soinmerweide des Yiehs, Alm“ (air. sid „Priede^ ursprgl. n. es-St. 
wohl zu *sc(^) „nachlassen“; Stokes KZ. 28, 292 will auch das von Thur- 
neysen KZ. 28, 153 mit lat. sldus verglichene ir. s~id n. es-St. ^Wohnung 
gottlicher Wesen^ damit gleichsetzen) ; 

air. suide n. {^sodiom) „Sitz, sitzen“ — lat. solium „Thron“ (s. Yf. LEWb.^ 
m. Lit.; nicht zu lit. sUlas ^'Bank^ u. dgl. trotz J. Schmidt KZ. 36, 102 undPerssons 
Beitr. 379 f. neuerlicher Yerteidigung, s. auch Sommer Hdb.^ 176, Kretschmer 
Gl.6,345; iiber die fernzuhaltenden lat. solea^ solum s.Yf. LEWb.^ s. v.); lat. 
praesidnon, insidiae {consilium^, s. Yf. LEWb.^ s. v.; in der Bed. ahnlich 
ware arm. atean ^Yersammlung“, Meillet Msl. 8, 154; Pedersen KZ. 38, 198). 

lat. sedes ^Sitz*' (: sMi-bus ^Wt. Inf. sedt-ti: 1. pi. scdi-rne, Brugmann II^ 
220; kaum besser aus dem alten es-St. "^sedes- herzuleiten, wie z. B. Sommer 
Hdb.^ 371, wo Lit., vorzieht; sedile kann allerdings nicht als innerlateinische 
Stiitze der Wzf. sedT- gelten, da Ponnans -lei- enthaltend); vgl, an weiteren 
dehnstufigen Bildungen ai. sadd- m. „das Sitzen^, sadin- „(aufsitzend =) 
reitend, Reiter^ (vgl. auch russ. vsddnik ,, Reiter^), anord. sat f. „Hinter- 
halt“, ags. s^t ds., ahd. -sa^a (in Ortsnamen) „Wohnsitz“, mhd. sa^e f. 
„Sitz, Wohnort, Hinterhalt, Belagerung, Lebensweise^, io-Adj. anord. s^r 
„zum Sitzen geeignet^, wovon sMi n. „Sitz, Heuhaufe^ = ahd. gisa^i „Sitz, 
Gesa6“; aksl. presMa „insidiae^: 

mit 0 anord. ags. sot „RuB^ („angesetztes^; daB ahd. ruoz^ mnd. rot 
„Ru8“, s. Bugge und Noreen Lti. 136, etwa in Zsetzungen wie HerdruB 
s- zu r- entwickelf haben sollen, ist ganz unwahrscheinlich; kaum besser 
aber Weigand-Hirt: = got. hrdt „Dach^). 



sed- 


4S5 


aksl. sazda^ lit. siiodziai pL, lett. suodri „Ku6“ (aber fernzuhalten, da mit 
nicht aus o lautgesetzlich herleitbarem Vokalismus, air. sidde f., cymr. 
htiddygl., bret. Jmzel „Ru6“, s. Pedersen KGr. I 71, 183 und Thurneysen 
lA. 26, 26); 
.....

ai. as^e = gr. rjOTai ^sitzt^^, 3. pi. asafc^hom. eiaxat (besser ^arai\ ygl. 
av. Inf. aste „sitzen^, mlidnte „sie sitzen^^; vgl. bes. den Akzent xadrja§at 
(von zwei Praeverbien tragt das zweite den Ton). Altere Lit.: Curtius^ 
377 f., Osthoff Pf. 170ff., Pick IMS, 174, 366, II ^ 23 (wo mit Unrecht ir. 
a, d. pi. aaib „exibus“, als ^asa „Sitz, Kutsche“ angereiht ist); zu den gr. 
Pormen s. noch Boisacq u. 7]jLiai (und iavog Nachtrag). 

B. ^sed- in der Bed. „gehn^; 

Ai. a-sad- „hintre ten, hingehn, gelangen^, id-sad- „sieh zur Seite be- 
geben, sich entziehen, verschwinden^^, av. pazdayeiti „verscheucht (macht 
weggehn^ ; Bartholomae ZdMG. 50, 686), av. apa-Jmd- „sich wegsetzen, 
wegriicken, ausweichen^^, asnaoiti i^o-zd-neu-ti) ^jgcht heran‘^ uuch 

oben dsna~y ai. vitdlyas- usw., die zwar wohl auf der Vorstellung des Heran- 
riickens beim Sitzen beruhn, aber doch schon die Yorstellung der Heran- 
bewegung durchfiihlen lassen), av, anvy-d-sti- „Bahn, Zuriicklegung des 
Wegs^" {-sd-ti-; Bartholomae IP. 12, 119); gr. bdog „Weg«, 6dhr}g „Wan- 
derer^ odsvco „wandere^, aksl. chodz „incessus, pddioiJ,a^\ choditi „incedere, 
gehn“, shd?, PPfA. „gegangen“ (^ = idg. s. Giintert Abl. 88; ch- aus idg. 
5 - wohl zunachst in Zs. mit pri- und ti- entstanden, Pedersen IP. 5, 62, 
Berneker 392, trotz Bruckner KZ. 45, 24). 

Vgl. Curtius ^ 241, Pedersen aaO., Brugmann IP. 13, 85f. Die Bed. 
j,gehn“ ist aus „sitzen“ in Verbindung mit Praefixen herleitbar, vgl. dt. 
„setz dich zu mir her^^, was ein erst herankommen voraussetzt, und die 
obgenannten Bed. „ wegriicken — weggehn^ (Pedersen; weniger diirfte an 
das Aufsetzen des Pubes beim Gehn zu denken sein, Brugmann); diese 
Bed.-Entwicklung mu6 aber wegen 6d6g = c}wd^ bereits ursprachlich be- 
gonnen haben. Hieher vielleicht als Zs. mit einem zum Pron. ho-^ Icio^ 
gehorigen Adv. ^kie- av. syazd- ^zuriicktreten vor, aufgeben^^, slzdyamna 
„zuruckweichende“, sxMyd ^aufgebend^, sudra- ^scheu*^ und lat. cMo 
„8chreite einher; weiche, gebe nach“ (s. Brugmann IP. 13, 84 ff., Thurneysen 
IP. 14, 131, Vf. LEAVb.2 u. cedo; ir. cet heifit dagegen nach K. Meyer 
SBBerl. Ak. 1914,939 m'sprgl. nicht ^Erlaubnis^, sondern „es ist erlaubt^
```


## [2026-09-14T01:33:43.771Z] TOOL CALL #56: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/period",
 "prompt": "Give the etymology of period: Greek periodos, peri + hodos, Latin periodus, Old French, and the sense development."
}
```


### [2026-09-14T01:33:48.852Z] TOOL RESULT

```
# Etymology of Period

**Origin Path:** The word "period" entered English in the early 15c. from Old French *periode* and Medieval Latin *periodus*, ultimately deriving from Greek *periodos*.

**Greek Roots:** The Greek term literally means "a going around," combining *peri* ("around") with *hodos* ("a going, traveling, journey; a way, path, road").

**Sense Development:** The meaning evolved from denoting a "course or extent of time; a cycle of recurrence" toward describing "repeated cycles of events" and then "intervals of time." By the 1600s, it referred to "a dot marking end of a sentence," based on the earlier sense of a complete sentence as a full pause. Later applications include menstruation (1829), classroom lessons (1876), and sports divisions (1898).

**Latin Transmission:** Latin *periodus* preserved the meaning of "a complete sentence" and "cycle of the Greek games" before the term's journey into Romance languages and eventually English.
```


## [2026-09-14T01:33:52.482Z] TOOL CALL #57: Bash

```json
{
 "command": "for u in \"https://en.wiktionary.org/wiki/%D9%86%D8%AE%D8%B3%D8%AA|page 435 Sed node 6: Persian naxost etymology (MP naxwist < PIr *naxu-), checks Nourai's derivation from Av. nazdišta\" \"https://en.wiktionary.org/wiki/%D8%AE%D8%B1%D8%B3%D9%86%D8%AF|page 435 Sed node 4: Persian xorsand < MP hunsand, checks Nourai's avara-sad analysis\" \"https://en.wiktionary.org/wiki/%D9%BE%D8%B3%D9%86%D8%AF%DB%8C%D8%AF%D9%86|page 435 Sed node 4: pasandidan < *pati-sand- 'to seem good', PIE *(s)kend-, not *sed-\" \"https://www.etymonline.com/word/anode|page 435 Sed node 10/13: anode/cathode from Greek hodos, Whewell/Faraday 1834\" \"https://www.etymonline.com/word/method|page 435 Sed node 10/13: method < Gk methodos = meta + hodos\" \"https://www.etymonline.com/word/episode|page 435 Sed node 10/13: episode < Gk epeisodion = epi + eis + hodos\" \"https://abadis.ir/fatofa/%D9%85%D8%AA%D8%AF/|page 435 Sed node 12: Mo'in entry for متد tagged [فر.] French\" \"https://abadis.ir/fatofa/%DA%A9%D8%A7%D8%AA%D8%AF/|page 435 Sed node 12: Mo'in entry for کاتد tagged [فر.] French\"; do url=\"${u%%|*}\"; note=\"${u#*|}\"; python3 tools/fetch_source.py \"$url\" --note \"$note\" 2>&1 | tail -2; done"
}
```


### [2026-09-14T01:33:58.422Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/203b1b8383bf49e6.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/1c9d4814c23c853b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/19da7fae7aa72867.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/46c5fbca7145af01.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e274fb515b3c1444.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/7fb4547d723e4c89.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/cf2071e50395cde4.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/174c1691ed7c0a72.txt
```


## [2026-09-14T01:34:00.886Z] TOOL CALL #58: Bash

```json
{
 "command": "python3 tools/fetch_source.py \"https://www.etymonline.com/word/period\" --note \"page 435 Sed node 13: period < Gk periodos = peri + hodos\" 2>&1 | tail -2"
}
```


## [2026-09-14T01:34:01.839Z] TOOL CALL #59: Bash

```json
{
 "command": "sed -n '1,40p' tools/verify_check.py; ls data/verification/page-434.json data/verification/page-436.json 2>/dev/null"
}
```


### [2026-09-14T01:34:02.258Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/24728caadc6c5cdc.txt
```


### [2026-09-14T01:34:02.304Z] TOOL RESULT

```
Exit code 2
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
```


## [2026-09-14T01:34:04.727Z] TOOL CALL #60: Bash

```json
{
 "command": "sed -n '40,140p' tools/verify_check.py"
}
```


### [2026-09-14T01:34:04.777Z] TOOL RESULT

```
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


## [2026-09-14T01:34:50.995Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"upa\\.sad\\|upasad\\|avara\\.sad\\|avara-sad\" BRT.txt | head; echo \"=== KNT had ===\"; grep -n \"had- vb\\|hadiš- sb\\|hadiS- sb\\|^had-\\|hadis- sb\" KNT.txt | head"
}
```


### [2026-09-14T01:34:51.067Z] TOOL RESULT

```
=== KNT had ===
```


## [2026-09-14T01:34:51.647Z] TOOL CALL #62: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:2123 --image 2>&1 | tail -25"
}
```


### [2026-09-14T01:35:00.002Z] TOOL RESULT

```
نز ؟ - بفتح اول و شم ثالی وسکون نخشه - بنتح اول وشین قرشت وسکون
زای نقطه‌دار» بمعنی نخت باشد که اول و ابتدا | ثانی , بمعنی حجت و برهان باشد ۱۱
است و لخزین 9 بمعنی لخستین . نخَکله - بنتح اول وکاف ولاء وسکون
نخحت - بنم اول وئالی بروزن درست. | ثالی » کردکانیر! کوبند که مخت باشد و ژود
۱ < یل (ه.م.) ۳ کلپایگانی 207787 « قاسمی » » قی : خری » نهاز +
سیه دشمن او را رمه‌ای دان که درو له چراننده شباست وله ره جو نخراز.
فرخی سیستالی « رشیدی » « انجمن‌آرا ».
۴ -کردی 31731 ( بچهٌ اول » ارشد) « ژابا ص 2۱۸ > » اصفهانی 3372۳1 (نختن).
جهالگیری کوید : «لخر با اول مضموم بثانی‌زده بمعتی نخست باشد , و نخری نخستین راکویند.»
ی : راز . ۴ - مصحف « خر » رك : دخری. 8 - مصحف «خری» (خ.م.)
‎٩‏ - پازند 3251051 ( پپلوی 182151 ۰ اوستا 3220151318 ) « باروچا س ۳۲۹۳ >.
۷ -رك : خستن. 31235880-۸ ۰ شپری بیغارا که جغرافی نوبان اسلامی
آرا دف > هم نامیده‌اند ( قی: تحول مشابه نشچوان - داوه ) [ر4 : تفت . این "
شهردردرة کشکه دربا( ** كشك رود که بموازات زرافشان (رود سمرقند ) بسوی جنوب جارست »
و بسوی آمو دریا جربان داردء ولی پیش از الحاق بدان در شن‌فرو میرود ) قرار داشته . لخشب
در جادة بخارا به بلخ ( بمافت چهار روزه راه از بخارا او هشت روزه ازبلخ ) واقع بوده است .
ر4 : دائرة المعارف اسلام : نشب بقلم مینورسکی؛ ورك: ممجْم‌البلدان. ‎٩‏ -اطنه0
(رك : دائرة‌الممارف اسلام : نخشب ) . *- رك : ماه سیام » ماه‌کش » ماه فغشب .
۱- هدایت کوید : ۶« دربرهان بمعتی حجت وبرهان آورده » ولی برهان ندارد تحت
باشد . در فرهنگها نیافتم # انجمن آرا » برساختهٌ دساثیر است ۶ فرهنگه دساثیر صس 4۲۹۹
۵ لخرازی - از : راز (ه.م.) ی ( حاصل مصدر . ام معنی ) پیشروی بز بر سر
کله و رمه » مانند راز عمل کردن :
شیر اسهم نو بر فکنده یکره گر که و قصاب را به نخرازی .
اپوالفرج رون « رشپدي » « انچین‌آرا » ۰
```


## [2026-09-14T01:35:02.766Z] TOOL CALL #63: Bash

```json
{
 "command": "ls -la data/verification/sources/refs/ocr/BQT/ 2>/dev/null | head"
}
```


### [2026-09-14T01:35:02.815Z] TOOL RESULT

```
total 62688
drwxrwxr-x  2 sfmqrb sfmqrb   16384 Sep 13 21:34 .
drwxrwxr-x 13 sfmqrb sfmqrb    4096 Sep  7 13:51 ..
-rw-rw-r--  1 sfmqrb sfmqrb  368375 Sep  4 13:39 0001.png
-rw-rw-r--  1 sfmqrb sfmqrb    1684 Sep  4 13:39 0001.txt
-rw-rw-r--  1 sfmqrb sfmqrb  534367 Sep  4 13:39 0049.png
-rw-rw-r--  1 sfmqrb sfmqrb    2677 Sep  4 13:39 0049.txt
-rw-rw-r--  1 sfmqrb sfmqrb    1076 Sep  4 15:27 103.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb    1325 Sep  7 16:52 1074.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb  330101 Sep  6 17:59 1092.jpg
```


## [2026-09-14T01:35:05.098Z] TOOL CALL #64: Bash

```json
{
 "command": "ls -la data/verification/sources/refs/ocr/BQT/ | grep 2123"
}
```


### [2026-09-14T01:35:05.153Z] TOOL RESULT

```
-rw-rw-r--  1 sfmqrb sfmqrb    2123 Sep  6 11:45 1689.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb  426006 Sep 13 21:34 2123.png
-rw-rw-r--  1 sfmqrb sfmqrb    4155 Sep 13 21:34 2123.txt
```


## [2026-09-14T01:35:11.809Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && python3 -c \"\nfrom PIL import Image\nim=Image.open('/home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/2123.png'); print(im.size)\nw,h=im.size\nim.crop((0,int(h*0.52),w,int(h*0.66))).resize((int(w*1.6),int(h*0.14*1.6))).save('bqt2123-fn-435.png')\n\""
}
```


### [2026-09-14T01:35:13.314Z] TOOL RESULT

```
(1650, 2546)
```


## [2026-09-14T01:35:15.282Z] TOOL CALL #66: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/bqt2123-fn-435.png"
}
```


### [2026-09-14T01:35:15.483Z] TOOL RESULT

```

```


## [2026-09-14T01:35:15.480Z] INPUT

[Image: original 2640x570, displayed at 2000x432. Multiply coordinates by 1.32 to map to original image.]


## [2026-09-14T01:35:35.746Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && cat > ocr/BQT/2123.vision.txt <<'EOF'\nBorhan-e Qate' (ed. Mo'in), printed p. 2123 = BQT_v4 pdf page 206 — read from the page image\n(data/verification/sources/refs/ocr/BQT/2123.png), footnotes at the foot of the page:\n\n۴ - کردی nuxrî ( بچهٔ اول ، ارشد ) « ژابا ص ۴۱۸ » ، اصفهانی naxrî (نخستین).\nجهانگیری گوید : «نخر با اول مضموم بثانی‌زده بمعنی نخست باشد ، و نخری نخستین را گویند.»\n\n۶ - پازند naxust ( پهلوی nazîst ، اوستا nazdishta ) « باروچا ص ۳۲۳ ».\n\n۷ - رك : خستن.   ۸ - Naxshab ، شهری بیخارا که جغرافی‌نویسان اسلامی آنرا «نسف» هم نامیده‌اند …\n\n(Headword column, same page: «نخست - بضم اول و ثانی بروزن درست … بمعنی اول و ابتدا باشد»,\n«نخستین بمعنی اولین».)\nEOF\ngrep -n \"abode.: Av\\|hadiš- sb\\|hadis-\" KNT.txt | head -5; grep -n \"‘abode’\" KNT.txt | head -8"
}
```


### [2026-09-14T01:35:36.686Z] TOOL RESULT

```
911:Н. pIE ә was the reduction of ë or 6 or à; it became 7 in pAr., but a in all other ЕЕ branches.! *noté|r] father’, OP рий, Skt. рий, Gk. татр. *sedos, ОР hadiš ‘abode’, but *sedos, Gk. os
5207:wadd- sb. ‘abode’, vriddhi-form to Skt. svadha- ‘innate character’, from wa- ‘own’ + dhà- ‘make’ ($142; OP wa- + ?dà-) ; in PaiSiyduvdda-, q.v.
5621:PaiSiyd'uvdda- sb. ‘Paishtyauvada’: АКК. pi- &-"-hu-ma-du. Perhaps, with Justi, IFA 17.107, ‘Pasargadae’, from paisiyd- ‘writing’ + "wüdá- ‘abode’ (572, §89, §126, $127, $142, §166, 5160.1): ‘Home of the Archives and Sacred Writings’ (on Pasargadae, ef. also Kónig, RuID 66; but Hz. ApI 275-6, modifying his view ш AMI 1.86n, takes prior element to be pati-, pati- becoming pa&-, with epenthesis; Bthl. AiW 907-8 normal- izes Piši- after the Akk., but gives no etymology). Paisiydwddim asf. DB 3.42. Parsilydluvadayd absf. DB 1.36f.
```


## [2026-09-14T01:35:52.436Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"hadi\\|Sad- vb\\|šad- vb\\|sad- vb\" KNT.txt | head -20"
}
```


### [2026-09-14T01:35:52.499Z] TOOL RESULT

```
845:A’Se 4f [тат (asf. for asn. ima) hadiš; 6 tya (for asf. уйт) afagainàm.
846:Аа 3 imam (asf. for nsn. ima) hadi’.
911:Н. pIE ә was the reduction of ë or 6 or à; it became 7 in pAr., but a in all other ЕЕ branches.! *noté|r] father’, OP рий, Skt. рий, Gk. татр. *sedos, ОР hadiš ‘abode’, but *sedos, Gk. os
1635:(2-3) pAr. split of pIE s into s š A, and plr. split of pAr. s into s and A (8115): stanam avas- layam niyašiāyam ачоіа; hadiš niy-asddayam; afaham 6asianaty; nom. ending in baga-" pasti- ріти-&.
2196:III. Apparently there was also a nt. suffix -as-, not varying within the paradigm nor in the corre- sponding masc. formation: type Skt. kravís ‘Taw flesh’, Gk. xpéas. OP nom.-ace. hadiš from *sed- as, cf. ОК. éðos from *sed-os; ace. abicaris *pasture- land’, see Lex. s.v. In names, Hazd-manis, Ardu- mants, perhaps I-mami$; late gen. Haxdmanis- ahyd adds the gen. ending of -o- stems to the nom. as stem.!
2711:A. With hada, to denote accompaniment either friendly or hostile: DB 2.21f pasdva haw Vidarna hada kärä ašiyava ‘after that this Hydarnes with the army marched forth’; DB 2.23 avadé hamar- anam akunaus hadi Müdaibi$ ‘there he made battle with the Medes’.
2841:upariy ‘over’, with slight idea of motion, shading down to ‘according to’ (DB 4.64); once placed as second word after its object (DNb 49, vari- ant of 46).
2987:8295. THe CONJUNCTION yaéd has the meanings ‘as’ (marked by the correlative алабӣ, once mis- written avd; sometimes no correlative with yofá mim Гата аһа); ‘when’, shading into ‘after’ (which is marked by the correlative pasdva ‘after
3540:ii айа = ооа sr : ds -hadi 21 І muti : тат : hamaranam :
4248:21 ya : adam : akunavam : visam : vašnā : Auramazdáha : 22 akunavam : ima : hadis : tya : QüsAyà : akunavam : 28 haring > аа саа а jfrava
4252:27 nā : upariy : avàm : каш : hadis : frásahya.
4315:4 m : тат : АМ : daustá : dha : tya : akunavam : avamaiy : visam : ucüram : cha : 0a 5 tiy : Dàrayavaus XS : vašnā AMha : һуа : ima : hadi$ : vaindliy : tya : mand : ka 6 riam : visahy& : frašam : üaday&lazy : тт : AM : ріш : ulamaiy : DHum
4481:XPc = XERXES, PERSEPOLIS C. 1 Бара : vazraka : Auramazda : hya : пойт : bümim : 2 ада : hya : avam : asmànam : ada : һуа : marti 3 yam : ada : һуа : Siyátim ; ada : martiyahyà 4 : һуа : Xšayāršām : XS8m : akunaus : aivam : pa 5 rūnām : XSm : aivam : pariinam : framátàram 6 :adam : XSayarsa : XS : vazraka : XŠ : XSanam : XS: 7 dahyünàm : paruv : zandndm : XS : аһуйуй : b 8 ümiyà : vazrakiya : düraiy : apiy : Darayava 9 haus : XShya : puça : Haxāmanišiya : 6atiy : X 10 šayāršā : XS : vazraka : vašnā : Aurahya Mazdaha : i 11 ma ; hadis : Dárayavaus : XS : akunaus : hya : manā : 12 pità : mim : Auramazda : pátuv : hada : baga 13 ibis : utd : tyamaty : kartam : uta : tyamaiy : 14 pica : Darayavahau’ : XShyá : камат : avaSely 15 : Auramazda : pátuv : hada : bagaibis
4634:1 бабу : XSayar8a : xšāyaðiya : vasna : Auramazdaha : ima : 2 hadi’ : Darayavaus : xšāyaðiya : akunaus : hya : mana : pita Nores to XSa: This is the line-division of Scheil’s copy; the other copy divides before ima. Scheil’s hand- drawn copy has ak“un*uus+, against Wb's normal aktuntus. TRANSLATION OF Ха: ... (= XPe 9-12, with slight omissions).
4637:3 шу: Xšayäršā : хдйуабїуа : ima : hadis : akunàm : разара : yabà : adam : z$àya
4668:3 m : asmünam : adà : hya : marti 4 yam : add : hya : siydtim : ad 5 à : martiyahyd : hya : Arlazsag 6 Gm : х$йуайшат : akunaus : а 7 wam : parünüm, : x3dyabiyam : 8 ашат : parünüm : framátüram 9 : adam : Artazšaçã : x$ayabuya. 10 : vazraka : zšãyaðiya : х$йуай 11 yànàm : z$àyabiya : dahyind 12 m : paruzanànüm : ssdyadiya : 13 ahyáyà : bümiyā : vazrak 14 aya : düraty : apiy : XSay 15 àrsahyá : х$йуайшаһуй : ри 16 са : Dárayavahaus : парӣ 17 :98ty : Artazšaçã : xš 18 yafliya : vazraka : va$nà : Au 19 ramazdaha : ima : hadi$ : XSayd 20 r&à : xSdyahiya : hya : mand : pr 21 tā : frataram : pasdva : adam : aku 22 navam : mam: Auramazdd : pat 23 uv : hada : bagaibis : utamary : 24 xkacam : щй : tyamary : kartam
4682:3 vaum : Хт : AM pàtuv : hadi : BGibis
4685:D'Sb = Darius IT, Sesa B. 1 айат: Dárayasaus : XS : vazraka : XŠ : XSyanam : XŠ : DHyünàm XŠ : а 2 hydyd : Вуй: Artazsagahyá : XShyá : puça : Haxamanisiya : 3 batiy : Dürayavaus : XS : ima : hadiš : Arlaxíacü : paranam : akunaus : 4 hya : mand : pilà : ima : hadis : pasava : vasnà : ÁMha : adam : akunavam Notes то D'Sb: Вга. WZKM 39.85-7, after the Akk., restored ? [apara]m ‘upper part’ = ‘part at the top of the slope’, and * [adaram] ‘lower part’ = ‘part lower on the hill’; but Hinz, ZDMG 91.251-2, restores [paranalm and [pasava], in temporal sense, which is preferable. *akunas in copy b. TRANSLATION OF D'Sb: $1. 1-2. ... (= DNa 8-12, with one omission), son of Artaxerxes the King, an Achaemenian. §2. 3-4. Saith Darius the King: This palace Artaxerxes previously built, who was my father; this palace, by the favor of Ahuramazda, I after- wards built (to completion).
4698:A’Sc = Artaxerxes II, Susa c. 0 Dérayavausahya : XShya : puça : 0 Dérayavausahya : V'Staspahya : puça 1 : Haxamanisiya : дану : Artaxsaga : 2 xSayabiya : vazraka : rSayafiya : х 9 šāyaðiyanām : xSdyafiya : dahyün 4 äm : xšāyaðiya : ahydya : bumiyd : 1 5 mam : hadis : uta : imam : usta 6 сапат : tya : afagainám : ta +++++4 ООА : Auramazdà :
4704:3 vasnd : AMhà : imam : hadis : tya : j'vadiy : paradayadàm : adam : akunavam : AM : Anah 4 ita : uta : Mitra : mam : pàtuv : hacd : vispà : gastà : utamaiy : kartam Nores то À'Sd: Text according to the line-divisions of copy da. ‘af... de; ahydya db; ahyd de. ? Hazámanikiya db; Harémaniya da, de. 3 akul... da; аштайт db; akuvanašāša de. *hacá da; lost in db; ha Xà de. * vispá da, de; »*dspa db. * gástà da, db; gastü dc. * uta... da; utamaty db; ufamay de. TRANSLATION ОЕ А284: 61. 1-2. ... (= A’Sa 1), an Achaemenian. $2. 2-4. Saith Artaxerxes the King: By the favor of Ahuramazda this is the palace which T built in my lifetime as a pleasant retreat. May Ahuramazda, Anaitis, and Mithras protect me from all evil, and my building.
```


## [2026-09-14T01:36:01.796Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR>=237 && NR<=239 {print \"=== NR \"NR\" ===\"; print substr($0,1,1500)}' KNT.txt"
}
```


### [2026-09-14T01:36:02.878Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T01:36:05.404Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} END{print NR}' KNT.txt; grep -n \"LEXICON\" KNT.txt | head -20"
}
```


### [2026-09-14T01:36:06.496Z] TOOL RESULT

```
232
44:GRAMMAR TEXTS LEXICON
128:PART HI. LEXICON
4908:PART III. LEXICON
4932:LEXICON
4971:LEXICON
5017:LEXICON
5062:LEXICON
5105:LEXICON
5153:LEXICON
5201:LEXICON
5246:LEXICON
5305:LEXICON
5351:LEXICON
5403:LEXICON
5448:LEXICON
5504:LEXICON
5546:LEXICON
5589:LEXICON
5636:LEXICON 195
5678:LEXICON
```


## [2026-09-14T01:36:08.815Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>5636 && /LEXICON/ {print NR\": \"$0}' KNT.txt | head -25"
}
```


### [2026-09-14T01:36:09.883Z] TOOL RESULT

```
5678: LEXICON
5712: LEXICON 199
5744: LEXICON
5783: LEXICON 203
5833: LEXICON | 205
```


## [2026-09-14T01:36:12.946Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '5833,5900p' KNT.txt | grep -n \"hadi\\|šad\\|sad-\\|nišādaya\\|nišadaya\" | head; echo \"=== tail of lexicon ===\"; sed -n '5860,5920p' KNT.txt | cut -c1-400"
}
```


### [2026-09-14T01:36:13.024Z] TOOL RESULT

```
=== tail of lexicon ===
rasa- present stem of vb., see ar-.
rüsla- adj. ‘straight, right, true’, with nt. as Sb.; ріс. of ?^rad-: Av. réSta-, Turfan РЫ. тай ‘true’, Lt. réctus ‘straight’, pIE *rékto- (593, §93.- n1-2, $106, $122, 5126, $24211). Cf. arštā-. таӣз- iam asf. DNa 59. rdstam usn. DNb 11; asn. DNb 7.
‚ .. rlaryary, see vart-.
Labandna- (or Labnàna-) sb. ‘Lebanon’ (§6, §107), 2 mountain in Syria famous for its cedars. Labanéna nsm. DSf 31.
-vä encl. conj. ‘or’ (8133, $291.11); -vā .. -vä ‘either... or...’: Av. và, Skt. và, pIE *ue, ef. Lt. -ve.  z$apa-ü rawca-paíi-a DB 1.20. hya-»à DB 4.68. imai-vä DB 4.71, 78, 77. yadi- vä DNb 25, 29.
vaina- present stem of vb. ‘see (mid.) seem’: Av. vaéna-, NPers. bindd, Skt. véda ‘knows’, vinddte ‘finds’, Lt. videt ‘sees’, videtur ‘seems’; pAr. *uaid- na-, plr. *yaina- ($69, 588.1, $130, $210.III; Reichelt, Aw. Ер. $157). See also Vidafarnah-. vainümiy lst sg. (4226.1) DNb 36, 36f, 39, 40. avaina imf. DB 2.76, 90; DNa 32. vainataiy mid. as pass. (8235.1) DNb 2; XPa 16
vau- adj. ‘good’ ($11, §153.1); nt. as sb. ‘the good, (religious) goodness’: Av. nsm. vaphus, nsn. vohu, Skt. nsm. vásuş, nsn. vdsu, pIE *yesu-; in Dérayavau-, Vaumisa-, Vahauka-, Vahyazdata-.
Va'umisa- sb. ‘Vaumisa’, a Persian officer of Darius: Elam. ma-u-mi-i8-8a, АКК. ti-mi-is-st, Gk. (Plutarch) Rutens; cpd. of vatu- and mifra- ‘friend’ (849c, $78, $148.ILD): ‘Friend of the Good’ §160.- Ib; cf. MB Gr. $51). Vaumisa nsm. DB 2.49, 51, 62. Vaumisam asm. DB 2.53, 58.
vaz$- vb. ‘grow’, see (Луах${та-.
Waj- vb. ‘be strong’: Skt. vaj-, бјаз- ‘strength’, Av. aof
```


## [2026-09-14T01:36:18.109Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && tail -25 KNT.txt | cut -c1-600"
}
```


### [2026-09-14T01:36:18.161Z] TOOL RESULT

```
raucah- sb. ‘day’: Av. raocah- ‘light’, Phi. rüé, NPers. róz, Skt. rócas- ‘light’, pIE *leugos ($70, $107, $156.ID, ef. Gk. Xexó-s adj. ‘ight’. тамса nsn. ($119, $1851) DB 3.8. rauca-pati-và
(899, $133) asn. DB 1.20. raucabiš ipn. ($119, 51851) DB 1.38, 42, 56, 89f, 96; 2.26, 36, 42, 47, 56, 691, 98^; 3.181, 39, 47, 63, 68, 88f.
ташіаћ- sb. ‘river’ ($166): NPers. ra8, Skt. srólas- ‘current, river’, pIE *sreutos (5118.1, $156.П) to root *sreu- ‘flow’; perhaps same as Av. 6raotah-, with sandhi initial (Bthl. Саг. IP 1.§87.- n2, AW 800). rauta nsn. anacoluthic in naming phrase (wrongly gen.-abl. to stem таш-, Mt. MSLP 19.56-7, MB Gr. $167, $316) DZc 9.
Razé- sb. ‘Rakha’, а town m Persia: Elam. rak-qa-an (S100). Ваха nsf. DB 3.34.
тахйайш! DNb 60, imv. of vb. of unknown etymology and uncertain meaning (§76.II, V, $103.IIT, $213, $237.II), perhaps ‘inflict punish- ment upon’, cf. АКК. version (Lg. 15.174; see also Hz. ApI 284-5).
ra”ga- sb. ‘speed, haste’: Av. rang- "leicht, flink werden’ (Bthl. AiW 1511), Skt. rdhale ‘has- tens, speeds’, rahas- nt. ‘speed, quickness’ (for fur- ther connections, see Uhlenbeck, Wrtb. d. altind. Sprache 241). ragam asn. (or asm.?) as adv. (§143.1, $191.IIT) DB 4.44, perhaps with develop- ment to ‘eagerly’ or ‘confidently’.
Raga- sb. ‘Rhages’, a district in Media: Elam. rak-qa-an, АКК. ra-ga-’, Gk. ‘Payys, now Rai near Teheran. kagä nsf. DB 2.71f. Ваду absf. DB 8.2.
гада- sb. ‘wagon’ (570.11, $148.11), see urata-.
Irad- vb. ‘leave’: Skt. rah-, pres. rahati 'sep- arates, leaves’, to pIE *regh-, Av. razah- 5isola- tion’, or to pIE *redh-, NPers. (through Ars. РЫ.) rähäð ‘he gets free from’; Fr. Müller, WZKM 11.208-4; Foy, KZ 37.564-5; Bthl. AiW 1505; MB Gr. $192.
ava- + rad- ‘leave, abandon’: avarada 2d sg. inj. (5213, $224, $227.11, $237) РМа 60.
?rad- vb. ‘direct’ Ау. raz-, Skt. rdj- ‘reign’, Lt. rego ‘I direct, rule’, pIE *reg-; in uradana-, тазіа-.
rādiy postpos. ($133) ‘on account of’, with gen.: NPers. тё, enel. postpos. as in &-rà ‘why’, also particle of various uses, often affixed to direct object for elarity; also OCS radi, postpos. with gen., “оп account of’; 10е, sgoof räd- (5188111), io root in Ski. radh- ‘effect; complete! (not to
206
"rad-, pIE *rej-, with Hz. ApI 280). DB 4.54; DNb 9, 10f; also in avahyarádiy, q.v.
ram- vb. ‘be at peace’, with prefix d, in Arüjyüramna-, q.v.
rasa- present stem of vb., see ar-.
rüsla- adj. ‘straight, right, true’, with nt. as Sb.; ріс. of ?^rad-: Av. réSta-, Turfan РЫ. тай ‘true’, Lt. réctus ‘straight’, pIE *rékto- (593, §93.- n1-2, $106, $122, 5126, $24211). Cf. arštā-. таӣз- iam asf. DNa 59. rdstam usn. DNb 11; asn. DNb 7.
‚ .. rlaryary, see vart-.
Labandna- (or Labnàna-) sb. ‘Lebanon’ (§6, §107), 2 mountain in Syria famous for its cedars. Labanéna nsm. DSf 31.
-vä encl. conj. ‘or’ (8133, $291.11); -vā .. -vä ‘either... or...’: Av. và, Skt. và, pIE *ue, ef. Lt. -ve.  z$apa-ü rawca-paíi-a DB 1.20. hya-»à DB 4.68. imai-vä DB 4.71, 78, 77. yadi- vä DNb 25, 29.
vaina- present stem of vb. ‘see (mid.) seem’: Av. vaéna-, NPers. bindd, Skt. véda ‘knows’, vinddte ‘finds’, Lt. videt ‘sees’, videtur ‘seems’; pAr. *uaid- na-, plr. *yaina- ($69, 588.1, $130, $210.III; Reichelt, Aw. Ер. $157). See also Vidafarnah-. vainümiy lst sg. (4226.1) DNb 36, 36f, 39, 40. avaina imf. DB 2.76, 90; DNa 32. vainataiy mid. as pass. (8235.1) DNb 2; XPa 16. vaináhy 2d sg. subj. ($37, $222.11, $227.1) DB 4.70, 73, 77; DNb 29. vaindtiy subj. ($222.11) DS} 5°. vainātaiy subj. mid. as pass. ($222.П) DNb 35.
vau- adj. ‘good’ ($11, §153.1); nt. as sb. ‘the good, (religious) goodness’: Av. nsm. vaphus, nsn. vohu, Skt. nsm. vásuş, nsn. vdsu, pIE *yesu-; in Dérayavau-, Vaumisa-, Vahauka-, Vahyazdata-.
Va'umisa- sb. ‘Vaumisa’, a Persian officer of Darius: Elam. ma-u-mi-i8-8a, АКК. ti-mi-is-st, Gk. (Plutarch) Rutens; cpd. of vatu- and mifra- ‘friend’ (849c, $78, $148.ILD): ‘Friend of the Good’ §160.- Ib; cf. MB Gr. $51). Vaumisa nsm. DB 2.49, 51, 62. Vaumisam asm. DB 2.53, 58.
vaz$- vb. ‘grow’, see (Луах${та-.
Waj- vb. ‘be strong’: Skt. vaj-, бјаз- ‘strength’, Av. aof
```


## [2026-09-14T01:36:34.986Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== IEC ===\"; grep -n \"sedeo\\|sédo\\|sedō\\|sed-,\\|sedmi\" IEC.txt | head -8; echo \"=== SYN ctx 21290 ===\"; sed -n '21280,21295p' SYN.txt | cut -c1-300; echo \"=== SYN ctx 22190 ===\"; sed -n '22190,22200p' SYN.txt | cut -c1-300"
}
```


### [2026-09-14T01:36:35.081Z] TOOL RESULT

```
=== IEC ===
2508:drütos (1) “wooden, of oak, of hardwood; solid, firm, strong’. WP I, 804 Per. durüd ‘timber, plank’; Arm. cf. artuc Cjuniper, fr. *drutio-); Gk. drútë ‘wooden bowl, wooden coffin’; Alb. i drutë ‘wooden’; Lat. cf. in-druticare Clusurate fr. Gaul.); Mir druit (€compression', but cf. drudh-); Gaul. drutos (sturdy, brisk’, substr. in Fr. dru); Li. drūtas “thick, solid, strong’. Cf. also dru- in Gk. dru-pepés ‘ripened on the tree’; drü-ppà ‘olive’. (The source of Gk. hi- drütós “set, established" is uncertain, perh. fr. *sed-, *síséd-)
13586:pró-sed-, cf. pro-, séd- Skt. pra-sadabh, m. “high seat; palace’; -sadi- kah, adj. ‘friendly’; Gk. (hapax) pro-edikós, adj. “landed, ground-; OCS pro-sédati, v. ‘penetrate’
14359:qusoitos (1) “bright, red? Av. xSaeto “bright; Per. Said (2), id. beside sed-, cpds. (“bay” of a horse); (LW in) Arm. ašxęt, adj. (“bay” of horse); Arm. xajt, i-st. *dapple, speckled’; Oss. áxsid, Dig. àxsed (cred Of sky)
15044:sédàio “seat; be seated'. WP II, 483 Skt. sadayami, tr. ‘seat’; Lat. sedo, are, f. ‘allay’; OHG, MHG sazen, tr. ‘set, settle, oc- cupy'; OE s&tian, v. *waylay'; OCS sédajo, ati, v. intr. “sit, settle’; Li. cf. (for *séd-) sedóm, sédomis, adv. 'seated'
15060:séd-mi (sédó, sedio, sedeio) ‘sit’. WP IT, 483 Athematic types: Skt. aor. subj. 3s. satsi: MIr. seiss, 3s. *will sit; OLi. sédmi, 3s: sésti. Other- wise Skt. sádami, v. (sit; Ober Av. sad-; Hom. hézomai; Lat. sedeo, ere; W heddu, inf. ‘pacify’; Cor. hedhy, inf. ‘cease’; Br. cf. az-eza, inf. (^seat, sit", fr. *ad-sed-); Go. sitan, sv. 5; OHG sizzen (fr. stan < *sedjo); OE sittan; ON sitja, sv. 5. ‘sit beside sæta: OE sætlan, v. *waylay'; Vedic sadáyami, v. “make sit; afflict’; cf. Lat. sedo, are, v. ‘allay’; OCS cf. sedo, sésti, v. ‘sit; séZdo, sédéti, v. "be seated' (and com. Sl1.); Li. sédZiu, sēdēti, v. *sit, be seated"; Latv. sezu and sedu, inf: sedet,
15372:síséd-, redup. of type sed-, q.v. Cf. sisdos above. WP II, 484 Skt. sidàmi, v. “sit down’; Av. nis-hióai(mi), v. id.; Arm. cf. (?) n-stim, v. ‘settle’; Gk. hizo, V. ‘seat, establish"; Lat. sido, ére, v. “perch, settle, sink?
=== SYN ctx 21290 ===
7. ChSl. (po)loziti, etc., caus. of words for ‘lie’ (12.14).
ChSI. klasti, klada, etc., esp. ‘lay’, also ‘put’ : Lith. kloti ‘spread out’, OE, OHG hladan ‘load’, etc. Walde-P. 2.489. Berneker 507.
SCr. meinuti, orig. and still dial. ‘throw’ : ChSl. mesti, metati ‘throw’, etc. (10.25). Berneker 2.40.
8. Skt. dha-, Av. da-, above, 1.
SIT Lith.  sédeti Lett.  sédet ChSl.  sédétz SCr. — sjeditz Boh.  sedétt Pol. siedziec Russ. _ sidet’ Skt.  as-, sad- Av. ah-, had-
eouar ‘sit’, itw (fr. redupl. *si-sdo) most- ly caus. ‘seat, place’, but also ‘sit’, xabitw mostly caus. ‘seat’ or ‘take a seat’ (so in NG); Lat. sedére (> It. sedere, OFr. seoir now ‘suit’, Sp. sentar ‘seat,
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
834 SELECTED INDO-EUROPEAN SYNONYMS
place’, sentarse or estar sentado ‘sit’, Rum. sedea; Lat. ad-sidére > Fr. asseoir ‘seat, place’, s’asseoir ‘take a seat’, étre assis ‘be seated, sit’; REW 7780); Ir. saidim, vbl. n. suide, whence NIr. suidh- im; W. eistedd fr. sb. = OBr. estid gl. sedile fr. cpd. (*eks-di-sedo-
siitan, OHG sizzan, etc., Seneral Gimp. Lith. sédéti, Lett. sédet; ChSI. ster ot,° general Slavic, beside perfect, Ssésti ‘take a seat’; Skt. sad-, Av. had-.
2. IE *és-, perh. ultimately derive fr. a epd. of preceding, 38g. mid. *¢-sq_ tai. Walde-P. 2.484.
Grk. fyat, 388g. Fora (= Skt. aste) more commonly xé@nuat, whence NG pop. kafonar; Skt. ads-, Av. ah-.
‘take
12.14 LIE Grk. — xeTyar Goth. ligan Lith. guléti NG Keluat, xelropat ON liggja Lett. gulét Lat.  iacére, cubdre Dan. ligge ChSl.  leZati It. giacere Sw. ligga SCr. — lezati Tr. élre couché OE licgan “Boh. — lezeti Sp. yacer, estar acostado ME liggen, lie Pol. lezeé Rum. fi culcat (zace
1. IE *legh-. Walde-P. 2.424. Walde- H. 1.778; Feist 331. Berneker 704 f. Grk. \exouar (Hesych.), Hom. aor. déxzo, ete., and in derivs. Aéxos, Aéxrpov ‘bed, couch’, etc.; Lat. only in lectus ‘bed, couch’; Ir. laigim, NI. luighim; Goth. ligan, OF licgan, OHG lig(g)an, etc., general Gme.; C
=== SYN ctx 22190 ===
Skt. rta- ‘fitting, right’, etc., fr. the root in Grk. dpaptoxw ‘fit, join together’ Walde-P. 1.72.
Lett. twou, fr. adj. tuvs ‘near’ : Lith. tuvt ‘at once’, OPruss. tawischan (ace. sg.) ‘the nearest’, etym. dub. Miuhl.,- Endz. 4.276 f.
6. ChSI. blizt, blizt, SCr. blizu, Boh, blizko, Pol., Russ. blizko, beside adj. ChSl. blizini, ete. : Lett. blaizit ‘press together, crush, beat’, Lat. fligere ‘beat, strike down’, Grk. ¢AlBw ‘press, crush’, Walde-P. 2.217. Berneker 61 f.
» ete,
7. Skt. samipam, beside adj. samipa-, prob. : sam-dp- ‘obtain’, cpd. of Gp- ‘reach’. Uhlenbeck 329.
Skt. antikam, beside antika- ‘vicinity, presence’, fr. anti ‘opposite, before’ (: Grk. évri ‘opposite’, etc.).
Skt. nikatam, beside nikata- adj. ‘near, at one side’, apparently epd. with ni- ‘down(wards)’, but last member ob- scure. Uhlenbeck 147.
Av. asne, loc. sg. of adj. *asna- (fr. *a- zd-na- pple.) fr. root *sed- ‘sit’ (Skt. sad-, Av. had-, etc.). Walde-P. 2.485. Barth. 220.
12.44 FAR (adv.)
Grk. praxptv, réppw, THe Goth. fairra Lith.  toli NG poxptd, &\Adpya ON  fiarri, langt Lett. tdlu Lat. procul, longé Dan. _langt, fjernt ChSl. dalet&e It. lontano, lunge Sw. ldngt, fidrran SCr.  daleko Fr. loin OE Seor Boh.  daleko Sp. lejos ME fer Pol. daleko Rum. departe NE far Russ. daleko Ir. 
Br. pell NHG fern, weit
```


## [2026-09-14T01:38:58.371Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for f in BQT_v1_pages.txt BQT_v2_pages.txt incoming/BQT/BQT_v3_pages.txt incoming/BQT/BQT_v4_pages.txt; do echo -n \"$f: \"; grep -c \"کاتد\\|آند\\b\\|متد\\b\" \"$f\" 2>/dev/null || echo 0; done; echo \"--- KLN anode ---\"; grep -n \"^anode,\\|^cathode,\\|^episode,\\|^period,\" KLN_1966.txt | head"
}
```


### [2026-09-14T01:38:59.520Z] TOOL RESULT

```
BQT_v1_pages.txt: 78
BQT_v2_pages.txt: 56
incoming/BQT/BQT_v3_pages.txt: 32
incoming/BQT/BQT_v4_pages.txt: 49
--- KLN anode ---
2868:anode,  n.,  positive  electric  pole.  —  Gk.  avo8o;, ‘way  up’,  fr.  oiva  (see  ana-)  and  oS6^,  way  . See  odograph  and  cp.  words  there  referred  to. The  term  anode  was  introduced  into  electricity by  the  English  physicist  and  chemist  Michael Faraday  (1791-1867);  cp.  cathode,  electrode. Derivatives:  anod-al,  anod-ic,  adjs.,  anod-ic- al-ly,  adv.
6813:cathode,  kathode,  n.,  negative  electric  pole  (phy¬ sics  and  chem.)  —  Gk.  xxfloSop,  ‘way  down, descent’,  fr.  xot ti  (see  cata-)  and  6S6p,  ‘way’. See  odograph  and  cp.  words  there  referred  to. The  term  cathode  was  introduced  into  electricity by  the  English  physicist  and  chemist  Michael Faraday  (1791-1867);  cp.  anode,  electrode. Derivatives:  cathod-al,  cathod-ic,  adjs.,  cathod- ic-al-ly,  adv.
28170:period,  n.  —  ME.  pariode,  fr.  MF.  (=  F .)  periode, fr.  L.  periodus,  fr.  Gk.  raptoSo?,  ‘circuit,  com¬
```


## [2026-09-14T01:39:20.969Z] AGENT

Now I'll write the verification file.


## [2026-09-14T01:45:14.147Z] TOOL CALL #76: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-435.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\n\nW_NAX = \"https://en.wiktionary.org/wiki/%D9%86%D8%AE%D8%B3%D8%AA\"\nW_XOR = \"https://en.wiktionary.org/wiki/%D8%AE%D8%B1%D8%B3%D9%86%D8%AF\"\nW_PAS = \"https://en.wiktionary.org/wiki/%D9%BE%D8%B3%D9%86%D8%AF%DB%8C%D8%AF%D9%86\"\nE_ANO = \"https://www.etymonline.com/word/anode\"\nE_MET = \"https://www.etymonline.com/word/method\"\nE_EPI = \"https://www.etymonline.com/word/episode\"\nE_PER = \"https://www.etymonline.com/word/period\"\nA_MET = \"https://abadis.ir/fatofa/%D9%85%D8%AA%D8%AF/\"\nA_KAT = \"https://abadis.ir/fatofa/%DA%A9%D8%A7%D8%AA%D8%AF/\"\n\nnodes = []\n\nnodes.append({\n \"id\": 1, \"lang\": \"Avestan\",\n \"words\": \"had, hd, zd, šas 2; šâdayeiti; ni-šâdaiti; ni-šasti\",\n \"verdict\": \"transcription_suspect\",\n \"derivation\": \"The Avestan verb is had- 'to sit' < PIE *sed-, with a reduplicated present hiδaiti / nišhiδaiti 'sits down' (< *si-zd-), a perfect stem hazd- (opt. 3sg. ni hazdiiāt, Yt 13.13), a causative (ni-)šaδaiieiti 'makes sit down, installs', an infinitive aiβi.šasta- and the action noun ni-šasti- 'mating' (Cheung 2007: 125 s.v. *had; Pokorny 885 'Avestan ni-sasti- \\\"Begattung\\\"'). After the preverb ni- the Iranian *s of *sad- becomes š by the ruki rule and *d+t gives st, whence ni-šas-ti-. The derivation from *sed- is not in doubt, but three of the four root shapes as printed are not Avestan words: 'hd' and 'zd' are truncations of the present stem hiδ- and the perfect stem hazd-, and 'šas 2' is the numbered homonym-stem šas- of the dictionaries; 'šâdayeiti : sits' is in fact the causative šaδayeiti 'makes sit', and 'ni-šâdaiti' conflates the present nišhiδaiti 'sits down' with the causative nišaδayeiti. The printed page (pdf 435) shows exactly these forms, so the extraction is faithful and the shorthand is the book's own.\",\n \"derivation_fa\": \"ریشهٔ اوستایی had- «نشستن» بازماندهٔ *sed- هندواروپایی است؛ ستاک حال آن به صورت دوگان‌ساخته hiδaiti / nišhiδaiti «می‌نشیند»، ستاک کامل hazd-، ستاک سببی (ni-)šaδayeiti «می‌نشاند» و اسم مصدر ni-šasti- «آمیزش» به‌کار رفته است (چونگ ۲۰۰۷: ۱۲۵؛ پوکورنی ۸۸۵). پس از پیشوند ni- آوای s ایرانی بنا بر قاعدهٔ «روکی» به š بدل می‌شود و خوشهٔ d+t به st می‌انجامد؛ از این‌روست که همهٔ صورت‌های پیشوندی š دارند. خودِ اشتقاق درست است، اما صورت‌های «hd» و «zd» در چاپ کتاب واژهٔ اوستایی نیستند و کوته‌نوشت hiδ- و hazd- هستند، و «šâdayeiti: می‌نشیند» در واقع صورت سببی «می‌نشاند» است. تصویر صفحهٔ چاپی نشان می‌دهد که خطا از کتاب است نه از استخراج.\",\n \"error_in\": \"book\",\n \"book_prints\": \"had, hd, zd, šas 2 : to sit / šâdayeiti : sits / ni-šâdaiti : sits down / ni-šasti : mating\",\n \"correct_form\": \"had- (pres. hiδ-, perf. hazd-, stem šas-); (ni-)šaδayeiti 'makes sit down'; nišhiδaiti 'sits down'; ni-šasti- 'mating'\",\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"POK:884-887\", \"status\": \"supports\", \"note\": \"POK_full.txt l.72366-72440 (Pokorny 884-887 s.v. sed-): 'Avestan ap. had- (with Praverbien) \\\"sich setzen\\\" (nišaŋhasti for *nisasti); Kaus. Old Indic sadayati, Avestan ni-sadayeiti \\\"allows niedersitzen\\\"' and '*sed-ti- ... Avestan ni-sasti- \\\"Begattung\\\"' — exactly the forms and senses of the node.\"},\n   {\"ref\": \"FFD:78\", \"status\": \"supports\", \"note\": \"Abolqasemi, Fe'l-ha-ye Farsi-ye Dari p.78 (FFD_pages.txt pdf 83): «نشست < فارسی میانه nišast < ایرانی باستان *ni-šad-ta … ni پیشوند فعلی است. šad صورت اصلی sad است. s پس از i به š بدل و d پیش از t به s بدل شده است» (Latin forms garbled by OCR, the Persian is clear) — the same *ni-šad- base.\"}\n ],\n \"consulted\": [\n   {\"src\": \"CHEUNG\", \"where\": \"p.125 s.v. *had 'to sit, be seated'\", \"stance\": \"supports\", \"note\": \"'AVESTAN: hiδ- \\\"to sit, be seated\\\" (+ *ni-) \\\"to sit down\\\" … Perf.: OPT. 3sg. YAv. ni hazdiiāt (Yt 13.13); Inf.: YAv. aiβi.šasta; Caus.: IND. 3sg. YAv. nisaδaiieiti' — the real shapes behind the book's 'hd, zd, šas'.\"},\n   {\"src\": \"IEC\", \"where\": \"Mann s.v. sísed- (WP II 484)\", \"stance\": \"supports\", \"note\": \"'síséd-, redup. of type sed- … Av. nis-hiδai(mi), v. id.' — the reduplicated present is the one the book abbreviates as 'hd'.\"},\n   {\"src\": \"BRT\", \"where\": \"Altiranisches Wb., had-/hazd- section\", \"stance\": \"partial\", \"note\": \"The local OCR of Bartholomae is too damaged at the had- columns to grep (searches for hiδaiti/hazdya returned nothing), but the derived forms quoted elsewhere in the same file (hastra-, pasuš.hasta-, ni-šasti-) presuppose exactly this root.\"}\n ]\n})\n\nnodes.append({\n \"id\": 2, \"lang\": \"Persian\",\n \"words\": \"nešastan «نشستن ( نشین )»; našim «نَشیم ( نشیمن )»\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"NP نشستن nešastan / نشین nešīn- continues MP nišastan, nišīn- (MacKenzie 1971: 59 'nišastan, nišīn- [YTYBWN-stn' …] sit'), from Old Iranian *ni-šad-: the past stem *ni-sad-ta- > *ni-šas-ta- (ruki *s > š after ni-, *d+t > st) > MP nišast, and the present stem from *ni-šad-na-/*ni-šīd- > nišīn-. Horn (no. 1033) already set out 'ap. ni + √had-, Caus. niyasādayam; aw. ni + √had-, nišhiδaiti; phlv. n(i)šastan, n(i)šīnet', and flagged the surprising nasal and long ī of nišīn-em as old (cf. Balochi nindag, OCS sędǫ). نشیم/نشیمن 'perch, nest' is MP nišēm 'seat, perch, bird's nest' (MacKenzie 59; Nyberg II s.v. nišēm '[nšδm] a bird's nest … < *ni-šadman'), i.e. the instrument noun *ni-šad-man- 'place of sitting down', with -δm- > -m- and compensatory ē; نشیمن adds the MP suffix -an. Both words are therefore straight descendants of node #1.\",\n \"derivation_fa\": \"«نشستن / نشین» از فارسی میانهٔ nišastan, nišīn- است و آن از ایرانی باستان *ni-šad-؛ ستاک گذشته از *ni-sad-ta- ساخته شده که در آن s پس از پیشوند ni- به š و خوشهٔ d+t به st بدل گشته و nišast به دست آمده است (مکنزی ۱۹۷۱: ۵۹؛ ابوالقاسمی، فعل‌های فارسی دری ۷۸). هرن (شمارهٔ ۱۰۳۳) همین سلسله را با صورت‌های اوستایی nišhiδaiti و پارسی باستان niyašādayam آورده و به «ن» و «ی» کشیدهٔ نشینم به‌عنوان کهنگی اشاره کرده است. «نشیم/نشیمن» بازماندهٔ nišēm فارسی میانه از *ni-šad-man- «جای نشستن» است (نیبرگ، واژه‌نامه، ذیل nišēm) و حاشیهٔ معین بر برهان قاطع (ص ۲۱۴۷) نیز آن را «از نشستن» می‌داند. ادعای نورایی درست است.\",\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"BQT:2145-7\", \"status\": \"supports\", \"note\": \"Borhan-e Qate' ed. Mo'in p.2145 (BQT_v4_pages.txt pdf 228), footnote on نشستن: «پارسی باستان -ni-šad… اوستا … (نشستن) … پهلوی … هندی باستان … بلوچی …» (Latin forms OCR-garbled) and p.2147 footnote 7 on نشیم: «نشیم … قس: نشیمن، از «نشستن» … هوبشمان ۱۰۳۶» — both words derived from the ni-šad- verb exactly as drawn.\"},\n   {\"ref\": \"HRN:231\", \"status\": \"supports\", \"note\": \"Horn, Grundriss p.231 no.1033: 'nišesten \\\"sitzen\\\", Praes. nišīn-em. ap. ni + √had-, Caus. niyasādayam; aw. ni + √had-, nišhiδaiti \\\"sitzen, sich setzen\\\", Caus. nišāδayōis; phlv. n(i)šastan, n(i)šīnet; ai. ni + √sad-, sīdati.'\"}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"MacKenzie p.59\", \"stance\": \"supports\", \"note\": \"'nišastan, nišīn- [YTYBWN-stn' …| M nšst, (nšyy-), N ~] sit'; 'nišēm [nšδm | M nšym, N ~an] seat, perch'.\"},\n   {\"src\": \"NYB\", \"where\": \"Glossary s.vv. nišastan, nišēm\", \"stance\": \"supports\", \"note\": \"'nišastan … — Av. (1754) ni-šad- < ni-had- = OP (caus. ni-šādaya-) … Paz. NP nišastan nišīn-'; 'nišēm [nšδm] a bird's nest — < *niśadman … NP nišīm'.\"},\n   {\"src\": \"CHEUNG\", \"where\": \"p.126 s.v. *had, NWIR section\", \"stance\": \"supports\", \"note\": \"'(+ *ni-) Widely attested: NP nišastan/nišīn-, Bal. nist/nind-, Kurd. nistin …'.\"}\n ]\n})\n\nnodes.append({\n \"id\": 3, \"lang\": \"Avestan\",\n \"words\": \"sad, sand; upa-sad; avara-sad\",\n \"verdict\": \"disputed\",\n \"derivation\": \"Avestan does have a stem sand-/sad-, but it means 'to appear, to seem (good)' (pres. saδaiieiti, OAv. s-aor. sas, caus. sandaiiaŋha; Cheung 2007: 333 s.v. *sand; Bartholomae 1559 sand-), matched by OP θad- 'to seem' (Kent 187b) and Skt. chand- 'to seem, please'; its PIE source is *(s)ḱend-, and Cheung explicitly notes 'Pok.: —', i.e. Pokorny has no such root and does not file it under *sed-. The glosses 'settlement, agreement' are read back from Persian pasand/xorsand and are not Avestan meanings. Neither *upa.sad- nor *avara.sad- is an Avestan word: grepping Bartholomae for upa.sad / avara.sad yields nothing; 'avara-sad' is Nourai's own segmentation of xorsand (as if 'down' + 'sit'), which no source supports (see node #4). Nourai's source Horn (p.71) is the origin of the confusion: Horn derives pesend from *pati + √sad- and adds in parentheses that the root sad- 'sitzen' also occurs with an infixed nasal (āsandī, sędǫ) — a remark about a homonym that Nourai turned into an identification.\",\n \"derivation_fa\": \"در اوستایی ستاک sand-/sad- هست، اما معنای آن «پدیدار شدن، به نظر (خوش) آمدن» است نه «نشستن» (چونگ ۲۰۰۷: ۳۳۳؛ بارتولومه ستون ۱۵۵۹؛ پارسی باستان θad- «به نظر آمدن»، کنت ۱۸۷). ریشهٔ هندواروپایی آن *(s)ḱend- است و چونگ به‌صراحت می‌نویسد که پوکورنی چنین ریشه‌ای ندارد؛ پس پیوند دادن آن به *sed- «نشستن» ریشه‌شناسی عامیانه است. صورت‌های «upa-sad» و «avara-sad» نیز واژهٔ اوستایی نیستند و در فرهنگ بارتولومه یافت نمی‌شوند؛ «avara-sad» تجزیهٔ شخصی نورایی از «خرسند» است. سرچشمهٔ خطا حاشیهٔ هرن (ص ۷۱) است که پس از آوردن *pati-sad- در پرانتز یادآور می‌شود ریشهٔ همنام sad- «نشستن» هم با نون میانوند به کار می‌رود؛ نورایی این یادآوری را یکی‌انگاری دو ریشه گرفته است. پژوهش امروزی این گره را می‌گشاید و دو ریشه را جدا می‌داند.\",\n \"sources\": [W_PAS],\n \"ref_check\": [\n   {\"ref\": \"HRN:71\", \"status\": \"partial\", \"note\": \"Horn p.71 no.319: 'pesend \\\"zufrieden, angenehm\\\", pesendīden. ap. *pati + √sad-; aw. √sad- (Geldner √sad-, KZ. 27, 242) … (auch √sad- \\\"sitzen\\\" kommt mit infligirtem Nasal vor, vergl. ai. āsandī- \\\"Sessel\\\", ksl. sedǫ)'. Horn gives *pati-sad- but his √sad- is the 'seem' root; the 'sit' root appears only in a parenthetical aside.\"},\n   {\"ref\": \"FFD:43\", \"status\": \"partial\", \"note\": \"Abolqasemi p.43 (FFD_pages.txt pdf 48): «پسند ← فارسی میانه passand < ایرانی باستان *pati-sand-a … ریشهٔ sand به معنی «به نظر آمدن» است» — supports the *pati-sand- analysis, but glosses the root 'to appear', not 'settlement/agreement', and does not connect it to *sed-.\"}\n ],\n \"consulted\": [\n   {\"src\": \"CHEUNG\", \"where\": \"pp.333-334 s.v. *sand\", \"stance\": \"contradicts\", \"note\": \"'*sand \\\"to appear, seem (good)\\\" … PIE ? *(s)Kend- \\\"to agree, approve; to appear, seem\\\" … LIV: 546 | Pok.: —'; the Iranian root is kept apart from *had 'to sit' (p.125).\"},\n   {\"src\": \"NYB\", \"where\": \"Glossary s.v. passand-\", \"stance\": \"contradicts\", \"note\": \"'passand- [psnd-] pres. to approve … < *pat-sand- from pati + Av. (1559 sq.) √sand-, cf sahistan' — sand-, not sad- 'sit'.\"},\n   {\"src\": \"BRT\", \"where\": \"search for upa.sad- / avara.sad-\", \"stance\": \"silent\", \"note\": \"No such compounds in the Altiranisches Wörterbuch OCR (grep 'upa.sad', 'avara.sad', 'upasad' → no hits); Bartholomae's sand- is glossed 'erscheinen, scheinen'.\"},\n   {\"src\": \"POK\", \"where\": \"884-887 s.v. sed-\", \"stance\": \"silent\", \"note\": \"Pokorny's sed- article lists no sand-/sad- 'agreement' material at all.\"}\n ]\n})\n\nnodes.append({\n \"id\": 4, \"lang\": \"Persian\",\n \"words\": \"pasandîdan «پسندیدن»; p s n d, d l p s n d; xorsand «خرسند»\",\n \"verdict\": \"disputed\",\n \"derivation\": \"The words are real, but their parent is not *sed-. پسندیدن < MP passandīdan [psnd-ytn'], a secondary past stem built on the present passand- < *pati-sand-a- 'to seem good, be approved' (Nyberg, Glossary: 'passand- … < *pat-sand- from pati + Av. √sand-'; Abolqasemi 43; Wiktionary: *pati- + *sand 'to seem good', PIE *(s)kand-), with Parthian pasēnd- and Sogd. pts'ynt 'to approve' beside it. خرسند < MP hunsand (hwnsnd, also Pth. hwnsnd-yft), i.e. *hu-sanda- 'appearing good' (so Wiktionary; Nyberg s.v. xᵛansand takes the first element as xᵛan-/xᵛar- 'sun', after Benveniste, 'of sunny disposition'); on either analysis the second member is *sand- 'to seem' and the first is *hu-/*xᵛar-, never *avara- 'down'. The second line of the box, printed in italics as 'p s n d, d l p s n d', is the bare consonant skeleton of پسند pasand and دل‌پسند delpasand — a typesetting lapse in the book itself (the page image shows it exactly so), not an extraction error.\",\n \"derivation_fa\": \"هر سه واژه واقعی‌اند، اما پدرشان *sed- نیست. «پسندیدن» از فارسی میانهٔ passandīdan است که ماده‌ای جعلی بر پایهٔ ستاک حال passand- < *pati-sand-a- «خوش‌آیند نمودن» است (نیبرگ ذیل passand؛ ابوالقاسمی ۴۳؛ ویکی‌واژه). «خرسند» از hunsand فارسی میانه (hwnsnd) یعنی *hu-sanda- «نیک‌نما» است؛ نیبرگ به پیروی از بنونیست جزء نخست را xᵛan-/xᵛar- «خورشید» می‌گیرد، اما در هر دو تحلیل جزء دوم همان sand- «نمودن» است و جزء نخست هرگز *avara- «فرود» نیست. خطِ دوم جعبه که به صورت «p s n d , d l p s n d» چاپ شده، تنها اسکلت بی‌واکهٔ «پسند» و «دل‌پسند» است و لغزش حروف‌چینی خودِ کتاب است نه خطای خوانش اسکن. نتیجه: واژه‌ها درست‌اند ولی پیوند آن‌ها با ریشهٔ «نشستن» را پژوهش امروزی رد می‌کند.\",\n \"sources\": [W_PAS, W_XOR],\n \"ref_check\": [\n   {\"ref\": \"BQT:406\", \"status\": \"partial\", \"note\": \"Borhan-e Qate' ed. Mo'in p.406 (BQT_v1_pages.txt leaf 630, identified by the catch-line «بقیه در صفحهٔ ۴۰۷»), footnote on پسند: «پارسی باستان *pati-…؛ اوستا √sad (نشستن)، قس: هندی باستان āsandī … «اسشق ۳۱۹». نیبرگ کلمهٔ پهلوی passand را از *pati-sand- (بنظر آمدن) دانسته. قس: خرسند «نیبرگ ۱۷۲، ۴۳»» (Latin forms OCR-garbled). Mo'in's note carries BOTH the old 'sit' connection Nourai draws and Nyberg's 'to seem' derivation, which modern scholarship follows.\"}\n ],\n \"consulted\": [\n   {\"src\": \"NYB\", \"where\": \"Glossary s.vv. passand-, xᵛansand\", \"stance\": \"contradicts\", \"note\": \"'passand- … < *pat-sand- from pati + Av. (1559 sq.) √sand-'; 'xᵛansand [hwnsnd] contented … From xᵛan- = xᵛar- \\\"sun\\\" and (Av. 1559) sand- \\\"to be, become visible\\\" … (Benveniste). Also xᵛar-sand = Paz. NP.'\"},\n   {\"src\": \"CHEUNG\", \"where\": \"p.333 s.v. *sand, NWIR section\", \"stance\": \"contradicts\", \"note\": \"'(+ *pati-) NP pasandidan/passand- \\\"to approve; cherish\\\"' listed under *sand 'to appear, seem (good)', with MMP psyn-, BMP psnd- /passand-/.\"},\n   {\"src\": \"FFD\", \"where\": \"p.43\", \"stance\": \"partial\", \"note\": \"«پسندید < فارسی میانه passandīd … پسند ← *pati-sand-a-؛ ریشهٔ sand به معنی «به نظر آمدن» است» — same analysis, different root meaning.\"}\n ]\n})\n\nnodes.append({\n \"id\": 5, \"lang\": \"Avestan\",\n \"words\": \"nazdyô; nazd-îštâ, nazdištâ; âsna; âsnaoiti\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Av. nazdiiō 'nearer' is the acc. sg. nt. of the comparative *nazdyah-, and nazdišta- is its superlative 'nearest'; they answer exactly to Skt. nédīyas-, nédiṣṭha-. Bartholomae (col. 1061-3) analyses them as Indo-Iranian *nazdištha- belonging 'to a present *ni-zda-ti, to the root √sad-', i.e. the zero grade *zd- of *sed- with ni- 'down' — the same *ni-zd- that gives *nizdos 'nest'. āsna- 'near' is the past participle *ā-zd-na- 'brought close' (Buck, Selected Synonyms 12.43: 'Av. asne, loc. sg. of adj. *asna- (fr. *ā-zd-na- pple.) fr. root *sed- \\\"sit\\\" … Walde-P. 2.485. Barth. 220'), and āsnaoiti 'gets close to' is the nu-present *ā-zd-neu-ti (Walde-Pokorny II 489). The box prints the superlative twice, once segmented (nazd-îštâ) and once whole (nazdištâ); 'sat very close' for nazdyō is Nourai's paraphrase of 'nearer'.\",\n \"derivation_fa\": \"nazdiiō اوستایی صورت برتر (تفضیلی) *nazdyah- «نزدیک‌تر» و nazdišta- صورت برترین «نزدیک‌ترین» است و دقیقاً با nédīyas- و nédiṣṭha- سنسکریت برابر می‌افتد. بارتولومه (ستون ۱۰۶۱–۱۰۶۳) این‌ها را به ستاک حال *ni-zda-ti از ریشهٔ √sad- بازمی‌گرداند، یعنی همان *ni-zd- «فرونشستن» که «آشیانه» (*nizdos) نیز از آن است. āsna- «نزدیک» اسم مفعول *ā-zd-na- و āsnaoiti «نزدیک می‌شود» ستاک nu-دار *ā-zd-neu-ti است (والده-پوکورنی ۲/۴۸۹؛ باک، مترادف‌های هندواروپایی ۱۲٫۴۳). بنابراین هر چهار صورت به‌درستی زیر ریشهٔ *sed- جای می‌گیرند و ادعای نورایی درست است.\",\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"POK:886-887\", \"status\": \"supports\", \"note\": \"Pokorny 886f. (POK_full.txt l.72510): '4. More or less verdunkelte compositions: Old Indic nédīyas- \\\"nearer\\\", nedistha- \\\"nächst\\\" = Avestan nazdyō adv. \\\"(spacial) nearer\\\", nazdišta- \\\"the nächste\\\", Avestan asna- Adj. \\\"near\\\" (*ā-zd-na-, participle Perf. Pass.)' — all four forms of the node.\"}\n ],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"cols. 1061-1063 s.vv. nazdišta-, nazdyō\", \"stance\": \"supports\", \"note\": \"'Superl. zu *nazdyah- \\\"propior\\\" und zu āsna- \\\"propinquus\\\". — ai. nedištha- … zEt. (ar. *nazdištha- zu einem Praes. *ni-zda-ti, zum √ sad-)'; 'nazdyō Adv. \\\"(räumlich) näher zu\\\" … ai. nédīyah Adv.; np. nazd \\\"nahe\\\"'.\"},\n   {\"src\": \"SYN\", \"where\": \"Buck 12.43 'near', p.854\", \"stance\": \"supports\", \"note\": \"'Av. asne, loc. sg. of adj. *asna- (fr. *ā-zd-na- pple.) fr. root *sed- \\\"sit\\\" (Skt. sad-, Av. had-, etc.). Walde-P. 2.485. Barth. 220.'\"},\n   {\"src\": \"WLD\", \"where\": \"Walde-Pokorny II 485, 489\", \"stance\": \"supports\", \"note\": \"'asnaoiti (*ā-zd-neu-ti) \\\"geht heran\\\" (auch oben āsna-, ai. nédīyas- usw., die … auf der Vorstellung des Heranrückens beim Sitzen beruhn)'.\"}\n ]\n})\n\nnodes.append({\n \"id\": 6, \"lang\": \"Persian\",\n \"words\": \"nazd «نزد ( نزدیک )»; naxost «نخست»\",\n \"verdict\": \"disputed\",\n \"derivation\": \"نزد nazd 'near' (with نزدیک nazdīk) is confirmed: MP nazd, nazdīk (MacKenzie 58), from Av. nazda-/nazdyō (Horn no.1029: 'nezd \\\"nahe\\\", nezdīk. aw. nazda- \\\"nahe\\\"; phlv. nazdīk, nazdist; ai. nedīyas-, nediṣṭha-'), so it does descend from node #5. نخست naxost 'first' does not. MP is naxust/naxwist, written nhwst' (Pth. nxwst), which Nyberg (Glossary s.v. naxᵛist) calls the superlative of MPrth./MPrs. nwx 'beginning, the first of anything', and Wiktionary reconstructs PIr. *naxwist- from *naxu- 'first, in front' (cf. Kurd. nexrî 'first-born', Arm. nax, an Iranian loan). MP already has a separate regular superlative of nazd, namely nazdist 'first' (MacKenzie 58), which would have given NP *nazdist, not naxust: the -x- and the -w- of nhwst' are unaccountable from *nazdišta-. The equation naxust = Av. nazdišta- that Nourai draws is the old Parsi/Pazand tradition, still printed by Mo'in (Barucha) in the footnote of Borhan p.2123, and it is what modern Iranian philology has given up.\",\n \"derivation_fa\": \"«نزد (نزدیک)» تأییدشده است: فارسی میانه nazd و nazdīk از اوستایی nazda-/nazdyō (هرن شمارهٔ ۱۰۲۹؛ حاشیهٔ معین بر برهان، ص ۲۱۳۳: «اوستا nazda- (نزدیک)، هندی باستان nedīyas-, nediṣṭha-، پهلوی nazdīk»). اما «نخست» از این خانواده نیست: صورت فارسی میانه naxust/naxwist نوشتهٔ nhwst' است و نیبرگ آن را صفت برترین nwx «آغاز، نخستین چیز» می‌داند و ویکی‌واژه آن را از ایرانی باستان *naxu- «پیش، جلو» بازمی‌سازد (قس کردی nexrî، ارمنی nax وام‌واژهٔ ایرانی). افزون بر این، صورت برترین قاعده‌مند nazd در فارسی میانه nazdist است که در فارسی نو باید *نزدیست می‌شد، نه «نخست»؛ خ و واو nhwst' از *nazdišta- توجیه‌پذیر نیست. برابرنهادن «نخست» با nazdišta- سنت کهن پارسیان (باروچا) است که معین در حاشیهٔ ص ۲۱۲۳ برهان نقل کرده و پژوهش امروزی آن را کنار گذاشته است.\",\n \"sources\": [W_NAX],\n \"ref_check\": [\n   {\"ref\": \"BQT:2117-33\", \"status\": \"supports\", \"note\": \"Both halves of the range are in Mo'in's footnotes and both say what Nourai draws: p.2133 (BQT_v4 pdf 216) s.v. نزدیک «اوستا nazda- (نزدیک)، هندی باستان nediyas-, nediṣṭha- … پهلوی nazdīk»; p.2123 (pdf 206) footnote 6 s.v. نخست, read off the page image (saved as ocr/BQT/2123.vision.txt): «۶ - پازند naxust ( پهلوی nazîst ، اوستا nazdishta ) «باروچا ص ۳۲۳»».\"},\n   {\"ref\": \"HRN:230\", \"status\": \"partial\", \"note\": \"Horn p.230 no.1029 covers nezd/nezdīk only ('aw. nazda- \\\"nahe\\\"; phlv. nazdīk, nazdist; ai. nedīyas-, nediṣṭha-'); Horn's Grundriss has no entry for naxust at all (grep of HRN.txt for naxust/nuxust → no hits), so the reference does not support the second word.\"}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"MacKenzie pp.58-59\", \"stance\": \"partial\", \"note\": \"Lists 'nazd [nzd] near', 'nazdīk … near', 'nazdist [nzdst'] first' AND, separately, 'naxust [nhwst' | M nxwst, N ~] first' — two different words, so NP naxost continues the second, not the first.\"},\n   {\"src\": \"NYB\", \"where\": \"Glossary s.v. naxᵛist\", \"stance\": \"contradicts\", \"note\": \"'naxᵛist [nhwst'] the first … MPrth nxwst; MPrs nxwst; Paz. naxust; NP nuxust; sup. of the preceding w[ord]' — the preceding entry is Naxᵛ-Ohurmazd, 'MPrthPrs nwx \\\"beginning, the first of anything\\\"'.\"},\n   {\"src\": \"HRN\", \"where\": \"no.1029, p.230\", \"stance\": \"supports\", \"note\": \"Supports nazd/nazdīk from Av. nazda-.\"}\n ]\n})\n\nnodes.append({\n \"id\": 7, \"lang\": \"Avestan\",\n \"words\": \"hastra; hadiš; pasuš-hasta; apo-had\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"All four are genuine and all four are *sed- formations with the regular Iranian treatment of *d before *t (*-d-t- > -st-). hastra- n. 'assembly' = Skt. sattra-, from *sed-tlom/*sad-tra- (Pokorny 885: 'besides … *sed-tlom in Avestan hastra- n. \\\"congregation, meeting\\\" = Old Indic sattra-'; Bartholomae: 'hastra- n. \\\"Versammlung\\\" und zwar solcher, die für sich einen gemeinsamen Gottesdienst abhalten lassen'). haδiš- 'dwelling, palace' is the s-stem *sed-as- (Pokorny 885: 'Avestan Old Pers. haδiš- \\\"Wohnsitz, palace\\\"'), the Avestan counterpart of OP hadiš (node #9). pasuš-hasta- is not obscure, as the book's '?' suggests: Bartholomae glosses it 'Hürde, Pferch für Kleinvieh, Schafe' (pen for small cattle), literally 'sheep-sitting', with the participle *sed-to-; Pokorny 885 lists it under '*sed-to-' as 'hurdle (*settlement) for small cattle'. apa-had- 'to move away, get out of the way' belongs to the 'go' branch of the root (Walde-Pokorny II 489: 'av. apa-had- \\\"sich wegsetzen, wegrücken, ausweichen\\\"').\",\n \"derivation_fa\": \"هر چهار صورت اوستایی و همگی ساخته‌های ریشهٔ *sed-اند، با تحول قاعده‌مند ایرانی d+t > st. واژهٔ hastra- «انجمن، گردهمایی» برابر sattra- سنسکریت و از *sad-tra- است (پوکورنی ۸۸۵؛ بارتولومه: «hastra- n. Versammlung»). haδiš- «خانه، کاخ» ستاک -as دار *sed-as- است و همتای hadiš پارسی باستان. pasuš-hasta- که نورایی معنایش را با علامت پرسش گذاشته، در فرهنگ بارتولومه «آغل و جایگاه گوسفند و دام کوچک» (Hürde, Pferch für Kleinvieh) معنی شده و تحت‌اللفظ «جای نشستن گوسفند» است. apa-had- «کناره گرفتن، پس رفتن» به شاخهٔ معنایی «رفتن» همین ریشه تعلق دارد (والده-پوکورنی ۲/۴۸۹). ادعای نورایی درست است و تنها معنای pasuš-hasta- را می‌توان از بارتولومه تکمیل کرد.\",\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"POK:885-887\", \"status\": \"supports\", \"note\": \"Pokorny 885 (POK_full.txt l.72427-72440): '*sed-to- in … Avestan pasuš-hasta- m. \\\"hurdle (*settlement) for small cattle\\\"'; 'Avestan Old pers. haδiš- \\\"Wohnsitz, palace\\\"'; '*sed-tlom in Avestan hastra- n. \\\"congregation, meeting\\\" = Old Indic sattra-'; p.887 'Avestan apa-had- \\\"sich wegsetzen, dodge\\\"'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"cols. ~1385 and ~1795\", \"stance\": \"supports\", \"note\": \"'pasuš.hasta- m., °hastay- m. \\\"Hürde, Pferch für Kleinvieh, Schafe\\\"' (l.15884 of BRT.txt); 'hastra- n. \\\"Versammlung\\\" uzw. solcher, die für sich einen gemeinsamen Gottesdienst abhalten lassen' (l.29673).\"},\n   {\"src\": \"WLD\", \"where\": \"Walde-Pokorny II 485, 489\", \"stance\": \"supports\", \"note\": \"'ap. hadiš- \\\"Wohnsitz, Palast\\\" (idg. -es oder -is)'; 'av. apa-had- \\\"sich wegsetzen, wegrücken, ausweichen\\\"'.\"},\n   {\"src\": \"KNT\", \"where\": \"Kent, Old Persian §242 (morphology)\", \"stance\": \"supports\", \"note\": \"'OP nom.-acc. hadiš from *sed-as, cf. Gk. hedos from *sed-os' — the same s-stem as the Avestan haδiš-.\"}\n ]\n})\n\nnodes.append({\n \"id\": 8, \"lang\": \"Avestan\",\n \"words\": \"syazd; sîždyamna; sîždyô; sîždra\",\n \"verdict\": \"plausible\",\n \"derivation\": \"The four forms are genuine Avestan: syazd- 'to withdraw, step back before (abl.)' (Y 34.9 aēibyō … aša syazdat 'from them Aša withdraws'), the participles sīzdyamna- 'withdrawing' (Y 32.4) and sīzdyō 'giving up', and sīzdra- 'shy' (of the hedgehog, V 13.2; of animals of the plain, Yt 8.36) — Bartholomae s.vv. syazda-, sīzdya-, sīzdra-. Their attachment to *sed- is the standard view but an avowedly uncertain one: Pokorny 887 introduces them with 'Hieher vielleicht als Zusammensetzung mit einem zum Pron. ḱe-, ḱio- gehörigen Adv. *ḱe-: av. syazd- … und lat. cēdō (*ḱe-zd-ō)', i.e. *ḱe- 'hence' + the zero grade *zd- of *sed- 'to go', the exact counterpart of Latin cēdō; Bartholomae himself marks the etymology 'Et.?'. So the node is right in substance but rests on a reconstructed preverb, and 'recess' / 'to give up' are loose glosses for participles.\",\n \"derivation_fa\": \"هر چهار صورت اوستایی‌اند: syazd- «پس نشستن، کناره گرفتن از» (یسنه ۳۴٫۹)، صفت فاعلی sīzdyamna- «کناره‌گیرنده» (یسنه ۳۲٫۴)، sīzdyō «واگذارنده» و sīzdra- «رمنده، ترسو» (وندیداد ۱۳٫۲؛ یشت ۸٫۳۶) — بارتولومه ذیل همین مدخل‌ها. پیوند آن‌ها با *sed- دیدگاه رایج است اما خودِ پوکورنی (ص ۸۸۷) آن را با قید «شاید» می‌آورد: *ḱe- (قید برگرفته از ضمیر ḱe-/ḱio-) + صورت صفر *zd- از ریشهٔ «رفتن»، درست همانند cēdō لاتین از *ḱe-zd-ō؛ بارتولومه نیز در برابر ریشه‌شناسی علامت پرسش گذاشته است. بنابراین این گره «با احتیاط پذیرفتنی» است: واژه‌ها اصیل‌اند و تحلیل رایج همین است، ولی بر پیشوندی بازسازی‌شده تکیه دارد.\",\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"POK:885-887\", \"status\": \"partial\", \"note\": \"Pokorny 887 (POK_full.txt l.72553): 'Here perhaps as compound with one to Pron. ḱo-, ḱio- respective Adv. *ḱe-: Avestan syazd- \\\"zurücktreten vor, abandon\\\", sīzdyamna \\\"zurückweichende\\\", sīzdyō \\\"aufgebend\\\", sīzdra- \\\"shy\\\" and Latin cēdō (*ḱe-zd-ō)'. The forms are exactly Nourai's, but Pokorny's 'vielleicht' makes the filiation tentative.\"}\n ],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"s.vv. syazda-, sīzdya-, sīzdra-\", \"stance\": \"partial\", \"note\": \"'syazda- Praes. 18a \\\"zurückweichen\\\"; mit Abl. \\\"vor —\\\": aēibyō … aša syazdat yavat ahmat aurunā xrafstra' and 'sīzdra- Adj. \\\"scheu\\\": spānǝm sīzdrǝm … \\\"den scheuen Hund (V. Igel)\\\" V.13.2'; Bartholomae's etymology line for sīzdya- reads only 'Et.?'.\"},\n   {\"src\": \"WLD\", \"where\": \"Walde-Pokorny II 489\", \"stance\": \"partial\", \"note\": \"'Hieher vielleicht als Zs. mit einem zum Pron. ḱo-, ḱio- gehörigen Adv. *ḱe- av. syazd- \\\"zurücktreten vor, aufgeben\\\", sīzdyamna \\\"zurückweichende\\\", sīzdyō \\\"aufgebend\\\", sīzdra- \\\"scheu\\\" und lat. cēdō'.\"}\n ]\n})\n\nnodes.append({\n \"id\": 9, \"lang\": \"Old Persian\",\n \"words\": \"had; had-iš; ni-had\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Old Persian continues *sed- as had- (PIr. *s- > OP h-), attested in the noun hadiš- 'abode, palace' (DNa, XPc 11 ima hadiš …, A²Sd) — an -as-stem *sed-as-, Kent: 'OP nom.-acc. hadiš from *sed-as, cf. Gk. hedos from *sed-os' — and in the prefixed causative niy-a-šādayam 'I set (it) down, I established' (DNa 36) / ni-šādayam (XPh 34), where the preverb *ni- triggers the ruki change *s > š; Kent uses the pair 'hadiš : niy-ašādayam' as his textbook illustration of that split (§115). Cheung 2007: 125 cites Kent p.212 for 'OP (+ *ni-) ni-šad- (caus.) \\\"to establish\\\"'. Nourai's bare 'had : to sit' is an abstracted root, not an attested Old Persian word form; 'ni-had' likewise stands for the attested causative niyašādaya-.\",\n \"derivation_fa\": \"در پارسی باستان ریشهٔ *sed- به صورت had- بازمانده است (s ایرانی باستان در آغاز واژه به h بدل شده). گواه آن نام hadiš- «خانه، کاخ» است که ستاک -as دار *sed-as- است و کنت آن را با hedos یونانی از *sed-os می‌سنجد؛ و نیز صورت سببی پیشونددار niy-a-šādayam «فرو نشاندم، برپا کردم» (نقش رستم، بند ۳۶) که در آن s پس از پیشوند ni- بنا بر قاعدهٔ روکی به š بدل شده است. کنت همین جفت (hadiš در برابر niyašādayam) را نمونهٔ کلاسیک این دوگانگی آورده و چونگ (۲۰۰۷: ۱۲۵) برای ni-šad- به کنت ص ۲۱۲ ارجاع می‌دهد. «had» و «ni-had» در نمودار، ریشهٔ انتزاعی‌اند نه صورت گواهی‌شدهٔ پارسی باستان. ادعای نورایی درست است.\",\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"KNT:212,213\", \"status\": \"supports\", \"note\": \"The local OCR of Kent breaks off inside the Lexicon before the h- entries, so pp.212-213 themselves could not be read; but Cheung 2007: 125 cites precisely 'Kent: 212' for 'OP (+ *ni-) ni-šad- (caus.) \\\"to establish\\\": niyašādayam <n-i-y-š-a-d-y-m> (DNa 36), nišādayam (XPh 34)', and Kent's grammar in the same file gives 'OP nom.-acc. hadiš from *sed-as, cf. Gk. hedos from *sed-os' and 'OP imf. niyašādayam \\\"I set down\\\"'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"CHEUNG\", \"where\": \"p.125 s.v. *had, Old Persian section\", \"stance\": \"supports\", \"note\": \"'*OLD PERSIAN: (+ *ni-) ni-šad- (caus.) \\\"to establish\\\" = Kent: 212. Caus.: impf. IND. 1sg. niyašādayam (DNa 36), nišādayam (XPh 34)'.\"},\n   {\"src\": \"POK\", \"where\": \"884\", \"stance\": \"supports\", \"note\": \"'Avestan ap. had- (with Praverbien) \\\"sich setzen\\\" … ap. niyašādayam \\\"setzte\\\"'; p.885 'Avestan Old pers. haδiš- \\\"Wohnsitz, palace\\\"'.\"},\n   {\"src\": \"KNT\", \"where\": \"§115 and §242.III\", \"stance\": \"supports\", \"note\": \"'(2-3) pAr. split of pIE s into s š h … hadiš niy-ašādayam'; 'OP nom.-acc. hadiš from *sed-as, cf. Gk. hedos from *sed-os'.\"}\n ]\n})\n\nnodes.append({\n \"id\": 10, \"lang\": \"Greek\",\n \"words\": \"hodos; ana-hodos; kata-hodos; met-hodos; epi-eis-hodos\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Gk. ὁδός 'way, road, journey' goes back to the o-grade *sod-o-, with the regular Greek change of initial *s- before a vowel to h- (Watkins, AHD: 'sed-². To go. Suffixed o-grade form *sod-o- in Greek hodos, way, journey … [Pok. sed- 887]'); Pokorny and Walde-Pokorny file it with OCS chodъ 'gait', choditi 'to go', Skt. ā-sad- 'to approach' and Lat. cēdō. The compounds are all real: ἄνοδος anodos 'way up', κάθοδος kathodos 'way down' (kata- with the -t- aspirated before the h- of hodos), μέθοδος methodos 'pursuit of knowledge, method' (meta- 'in quest of'), and ἐπεισόδιον epeisodion 'that which comes in besides' (epi- + eis + hodos), the Greek term for the part of a tragedy between two choral songs, whence 'episode'; περίοδος periodos 'a going around' supplies 'period'. Nourai's 'epi-eis-hodos' is the underlying stem, not an attested noun *epeisodos. Beekes and Etymonline call the origin of ὁδός 'uncertain', but Pokorny, Walde-Pokorny, Klein and Watkins are unanimous for *sed-.\",\n \"derivation_fa\": \"واژهٔ یونانی ὁδός «راه، سفر» از صورت o-دار *sod-o- است و s آغازین هندواروپایی در یونانی پیش از واکه به h (روح شدید) بدل شده است (واتکینز، پیوست ریشه‌های هندواروپایی فرهنگ AHD ذیل sed-² «رفتن»؛ پوکورنی ۸۸۷). پوکورنی و والده-پوکورنی آن را با chodъ/choditi اسلاوی کهن، ā-sad- سنسکریت و cēdō لاتین هم‌ریشه می‌دانند. ترکیب‌ها همگی واقعی‌اند: anodos «راه بالا»، kathodos «راه پایین» (که در آن t پیشوند kata- پیش از h دمیده شده)، methodos «در پی چیزی رفتن، روش» و epeisodion «آنچه افزون بر آن درمی‌آید» که نام بخش میان دو سرود همسرایان در تراژدی یونانی است. تنها نکته آنکه «epi-eis-hodos» صورت گواهی‌شده نیست بلکه ستاک زیرین epeisodion است. بیکس و Etymonline خاستگاه ὁδός را «نامطمئن» می‌خوانند، ولی پوکورنی، کلاین و واتکینز همداستان‌اند. ادعای نورایی درست است.\",\n \"sources\": [E_ANO, E_MET, E_EPI, E_PER],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins, AHD Appendix of IE Roots (AHD_watkins1985.txt l.912): 'sed-². To go. Suffixed o-grade form *sod-o- in Greek hodos, way, journey: -ODE; ANODE, CATHODE, EPISODE, EXODUS, HYPOTHODE, METHOD, ODOGRAPH, ODOMETER, PERIOD, STOMODEUM, SYNOD. [Pok. sed- 887.]' — the node's word list, root and all.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"s.v. odograph (p. ~1123) and s.vv. anode, cathode\", \"stance\": \"supports\", \"note\": \"'The first element derives fr. I.-E. base *sed-, \\\"to go\\\", whence also OSlav. chodŭ … Cp. -ode, \\\"way\\\", and anode, cathode, Diodia, electrode, episode, exodus, hexode, method, parodos, period, stomodeum, synod. I.-E. base *sed-, \\\"to go\\\", is identical with *sed-, \\\"to sit\\\"'; 'anode, n., positive electric pole. — Gk. ἄνοδος, \\\"way up\\\", fr. ἀνά and ὁδός'.\"},\n   {\"src\": \"POK\", \"where\": \"887, section B\", \"stance\": \"supports\", \"note\": \"'B. *sed- in the meaning \\\"go\\\" … gr. ὁδός \\\"way\\\", ὁδίτης \\\"Wanderer\\\", ὁδεύω \\\"wandere\\\"; Old Church Slavic chodъ \\\"gait\\\", choditi \\\"go\\\"'.\"},\n   {\"src\": \"WLD\", \"where\": \"Walde-Pokorny II 489\", \"stance\": \"supports\", \"note\": \"'gr. ὁδός \\\"Weg\\\", ὁδίτης \\\"Wanderer\\\", ὁδεύω \\\"wandere\\\", aksl. chodъ … Die Bed. \\\"gehn\\\" ist aus \\\"sitzen\\\" in Verbindung mit Praefixen herleitbar … diese Bed.-Entwicklung muß aber wegen ὁδός = chodъ bereits ursprachlich begonnen haben.'\"}\n ]\n})\n\nnodes.append({\n \"id\": 11, \"lang\": \"French\",\n \"words\": \"\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"An empty relay box: it marks the French stage through which the Greek words reached Persian. Fr. méthode (< Lat. methodus, in French since the 16th c.) and épisode are learned Greco-Latin borrowings, while anode and cathode were coined for electrochemistry by William Whewell and published by Faraday in 1834 and passed at once into French as anode and cathode. Persian took its electrical and scientific vocabulary from French (not English) in the late Qajar and early Pahlavi period, so drawing Persian ânod/kâtod/metod off a French node rather than directly off Greek is correct — and the Persian shapes prove it (see node #12). The box carries no words and no reference in the book.\",\n \"derivation_fa\": \"این جعبهٔ تهی تنها ایستگاه فرانسوی را نشان می‌دهد؛ یعنی راهی که واژه‌های یونانی از آن به فارسی رسیده‌اند. méthode (از methodus لاتینی، در فرانسه از سدهٔ شانزدهم) و épisode وام‌واژه‌های عالمانهٔ یونانی-لاتینی‌اند، حال آنکه anode و cathode را ویوئل ساخت و فارادی در ۱۸۳۴ منتشر کرد و بی‌درنگ به فرانسه راه یافتند. واژگان برق و روش‌شناسی در فارسی اواخر قاجار و اوایل پهلوی از فرانسه وام گرفته شده است، پس کشیدن پیکان از فرانسه به فارسی درست است و شکل آوایی واژه‌های فارسی (متد نه *متد انگلیسی) نیز همین را گواهی می‌کند. این جعبه در کتاب نه واژه دارد و نه ارجاع.\",\n \"sources\": [E_ANO, A_MET],\n \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the node carries no reference in the book (refs=None)\"}],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"s.vv. anode, cathode, method, episode\", \"stance\": \"supports\", \"note\": \"Klein: 'anode … The term anode was introduced into electricity by … Michael Faraday (1791-1867); cp. cathode, electrode'; 'method, n. — F. méthode, fr. L. methodus, fr. Gk. μέθοδος' — French is the vehicle for the learned words.\"},\n   {\"src\": \"MON\", \"where\": \"Mo'in s.vv. متد، کاتد (via abadis.ir)\", \"stance\": \"supports\", \"note\": \"Mo'in tags both words '[فر.]' = French: «متد (مِ تُ) [فر.] (اِ.) روش، قاعده»; «کاتد (تُ) [فر.] (اِ.) ۱ - قطب منفی لامپ الکترونی …» — the French relay is Mo'in's own analysis.\"}\n ]\n})\n\nnodes.append({\n \"id\": 12, \"lang\": \"Persian\",\n \"words\": \"ânod «آند»; kâtod «کاتد»; metod «متد»\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Twentieth-century technical borrowings from French: آند ānod < Fr. anode, کاتد kātod < Fr. cathode, متد metod < Fr. méthode. Mo'in's dictionary marks them French: «کاتد (تُ) [فر.] (اِ.) ۱ - قطب منفی لامپ الکترونی که بر اثر گرما الکترون گسیل می‌کند» and «متد (مِ تُ) [فر.] (اِ.) روش، قاعده». The Persian shapes reflect French, not English or Greek, pronunciation: متد metod (not *metād / *method), and the final -ode of anode/cathode rendered -od with a short vowel. Semantically they preserve Faraday's 1834 electrochemical senses ('the way up/down' for the current) and the Greek 'pursuit, way of proceeding' for method, which is what the glosses in the box record.\",\n \"derivation_fa\": \"این سه واژه وام‌گیری‌های فنی سدهٔ بیستم از فرانسه‌اند: «آند» از anode، «کاتد» از cathode و «متد» از méthode. معین در فرهنگ خود هر دو واژهٔ «کاتد» و «متد» را با نشان «[فر.]» یعنی فرانسوی آورده است: «متد (مِ تُ) [فر.] (اِ.) روش، قاعده» و «کاتد (تُ) [فر.] (اِ.) قطب منفی لامپ الکترونی…». شکل آوایی فارسی نیز فرانسوی است نه انگلیسی: «متد» با تاء مفتوح و «ــد» پایانی در برابر -ode فرانسوی. معناها همان معناهایی است که فارادی در ۱۸۳۴ برای مسیر جریان برق به کار برد. ادعای نورایی درست است.\",\n \"sources\": [A_MET, A_KAT],\n \"ref_check\": [\n   {\"ref\": \"MON:2782,3797\", \"status\": \"supports\", \"note\": \"The content is confirmed from Mo'in's own entries (read via abadis.ir, which reproduces فرهنگ معین): «متد (مِ تُ) [فر.] (اِ.) روش، قاعده» and «کاتد (تُ) [فر.] (اِ.) ۱ - قطب منفی لامپ الکترونی…» — French origin, as Nourai's arrow says. The page numbers themselves could not be checked: volumes 3-6 of Mo'in are not available on disk with pagination (only the 2-vol Adena OCR, which has no page marks).\"}\n ],\n \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"s.vv. متد، کاتد (abadis.ir, section فرهنگ معین)\", \"stance\": \"supports\", \"note\": \"Both entries tagged [فر.] (French); no separate Mo'in entry for آند on that page, the encyclopaedic section describing it only as the counterpart of کاتد.\"},\n   {\"src\": \"KLN\", \"where\": \"s.vv. anode, cathode\", \"stance\": \"supports\", \"note\": \"Klein confirms the ultimate Greek source and the 1834 Faraday coinage that the Persian words borrow through French; he is silent on Persian.\"}\n ]\n})\n\nnodes.append({\n \"id\": 13, \"lang\": \"English\",\n \"words\": \"anode, cathode, method, episode, period\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"All five are hodos-words. Anode (1834) and cathode (1834) were proposed by William Whewell and published by Michael Faraday, from Gk. anodos 'way up' and kathodos 'way down', named for the supposed path of the current (Etymonline; Klein s.vv.). Method (early 15c.) comes through Lat. methodus from Gk. methodos 'scientific inquiry', meta 'in pursuit of' + hodos. Episode (1670s, 'commentary between two choric songs in a Greek tragedy') is Gk. epeisodion, epi 'in addition' + eis 'into' + hodos. Period (early 15c., from OFr. periode, ML. periodus) is Gk. periodos 'a going around', peri + hodos, whence 'cycle of time' and, from the sense 'complete sentence', the full stop. Watkins lists exactly this set under sed-² [Pok. 887].\",\n \"derivation_fa\": \"هر پنج واژهٔ انگلیسی از خانوادهٔ hodos «راه»‌اند. anode و cathode را ویلیام ویوئل پیشنهاد کرد و فارادی در ۱۸۳۴ منتشر ساخت، از anodos «راه بالا» و kathodos «راه پایین»، به نام مسیر پنداشتهٔ جریان برق. method از راه methodus لاتینی از methodos یونانی (meta «در پی» + hodos) است. episode از epeisodion یونانی (epi + eis + hodos) و در آغاز به معنی «بخش میان دو سرود همسرایان در تراژدی» بوده است. period از periodos «گردش، دور» (peri + hodos) از راه فرانسهٔ کهن و لاتین میانه به انگلیسی رسیده و از معنای «جملهٔ کامل» به معنای «نقطهٔ پایان جمله» رسیده است. واتکینز همین مجموعه را زیر sed-² فهرست کرده است؛ ادعای نورایی درست است.\",\n \"sources\": [E_ANO, E_MET, E_EPI, E_PER],\n \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the node carries no reference in the book (refs=None); the Greek parent node cites AHD, which lists exactly these English words.\"}],\n \"consulted\": [\n   {\"src\": \"AHD\", \"where\": \"Watkins s.v. sed-²\", \"stance\": \"supports\", \"note\": \"'-ODE; ANODE, CATHODE, EPISODE, EXODUS, HYPOTHODE, METHOD, ODOGRAPH, ODOMETER, PERIOD, STOMODEUM, SYNOD.'\"},\n   {\"src\": \"KLN\", \"where\": \"s.vv. anode, cathode, period, odograph\", \"stance\": \"supports\", \"note\": \"'cathode … Gk. κάθοδος, \\\"way down, descent\\\", fr. κατά and ὁδός … The term cathode was introduced into electricity by … Faraday'; 'period, n. — ME. pariode, fr. MF. (= F.) periode, fr. L. periodus, fr. Gk. περίοδος, \\\"circuit, …\\\"'.\"}\n ]\n})\n\nentry = {\n \"entry\": 0,\n \"root\": \"Sed\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *sed- 'to sit' (with the prefixed branch 'to go'), Pokorny 884-887\",\n \"note\": \"Root name, language label and gloss are all right: Pokorny 884-887 s.v. sed- 'to sit', which includes at p.887 a section 'B. *sed- in der Bedeutung \\\"gehn\\\", from connection with Prefixes originated' (Gk. hodos, OCS choditi, Lat. cēdō, Av. apa-had-). Nourai's double gloss 'to sit, to place; also to place a step, to go' paraphrases Klein's formulation ('the original sense of the base having been \\\"to place (either the seat in order to sit down, or the foot upon the ground in order to go)\\\"'), but not from the page he cites. Of the 13 nodes, 9 are confirmed; the weak points are the Avestan sad/sand box (#3) with its Persian derivatives (#4), where Nourai has merged the root *sand- 'to seem (good)' with *sed- 'to sit', and the word naxost in #6.\",\n \"note_fa\": \"نام ریشه، برچسب زبانی و معنای آن درست است: پوکورنی ۸۸۴–۸۸۷ ریشهٔ *sed- «نشستن» را می‌آورد و در ص ۸۸۷ بخشی با عنوان «*sed- به معنی رفتن، که از پیوند با پیشوندها پدید آمده» دارد که hodos یونانی، choditi اسلاوی، cēdō لاتین و apa-had- اوستایی را دربر می‌گیرد؛ پس معنای دوگانه‌ای که نورایی برای ریشه آورده پذیرفتنی است و در واقع بازگفت عبارت کلاین است. از سیزده گره این صفحه نُه گره تأیید می‌شود؛ نقطه‌های ضعف یکی جعبهٔ اوستایی sad/sand (گرهٔ ۳) و مشتقات فارسی آن (گرهٔ ۴) است که در آن ریشهٔ *sand- «به نظر (خوش) آمدن» با *sed- «نشستن» یکی گرفته شده، و دیگری واژهٔ «نخست» در گرهٔ ۶ که از *naxu- «پیش» است نه از nazdišta-.\",\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"POK:884,887\", \"status\": \"supports\", \"note\": \"Pokorny 884-887: 'Root/lemma: sed-, Meaning: to sit … Material: 1. Old Indic sad-, Avestan ap. had- …' and, on p.887, 'B. *sed- in the meaning \\\"go\\\", from connection with Prefixen originated … gr. ὁδός \\\"way\\\"'. Both cited pages are exactly on point.\"},\n   {\"ref\": \"KLN:1075\", \"status\": \"not_found\", \"note\": \"Klein 1966 p.1075 falls in the range Naaman–namesake (KLN_1966.txt leaves 549-551, calibrated against the known leaf 748 = p.1469); there is nothing about *sed- there. Klein does treat the base at 'cede' (p. ~266: 'I.-E. base *sed-, \\\"to go\\\", is prob. identical with *sed-, \\\"to sit\\\", the original sense of the base having been \\\"to place (either the seat in order to sit down, or the foot upon the ground in order to go)\\\"' — the very wording Nourai's root gloss paraphrases), at 'odograph' (p. ~1123) and at 'sedentary' (p. ~1471). The cited page number appears to be wrong.\"}\n ],\n \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Walde-Pokorny II 483-489\", \"stance\": \"supports\", \"note\": \"'sed- \\\"sitzen\\\", z. T. mit einer Basis sedē- : sedī-' (II 483) and 'B. *sed- in der Bed. \\\"gehn\\\"' (II 489) — the source Pokorny abridges.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins s.vv. sed-¹, sed-²\", \"stance\": \"supports\", \"note\": \"'sed-¹. To sit … [Pok. sed- 884.]'; 'sed-². To go … [Pok. sed- 887.]' — the same two-sense root, split into two numbered entries.\"},\n   {\"src\": \"IEC\", \"where\": \"Mann s.vv. sēd-mi, sēdāio, sísed-\", \"stance\": \"supports\", \"note\": \"'sēd-mi (sēdō, sedio, sedeio) \\\"sit\\\". WP II, 483 … Ober Av. sad-; Hom. hézomai; Lat. sedeo'; 'síséd-, redup. of type sed- … Av. nis-hiδai(mi)'.\"},\n   {\"src\": \"SYN\", \"where\": \"Buck 12.13 'sit', pp.833-834\", \"stance\": \"supports\", \"note\": \"'…OE sittan, OHG sizzan, etc., general Gmc.; Lith. sėdėti, Lett. sēdēt; ChSl. sěděti, general Slavic, beside perfective sěsti \\\"take a seat\\\"; Skt. sad-, Av. had-.'\"},\n   {\"src\": \"KLN\", \"where\": \"s.vv. cede, sedentary\", \"stance\": \"supports\", \"note\": \"'I.-E. base *sed-, \\\"to sit\\\", whence also OI. ā-sadat \\\"sat down\\\", sīdati \\\"sits\\\", Avestic had-, \\\"to sit down\\\", Gk. hézesthai, hedra, OIr. suide …; I.-E. base *sed-, \\\"to sit\\\", is identical with base *sed-, \\\"to go\\\". See cede.'\"}\n ],\n \"nodes\": nodes\n}\n\nout = {\n \"pdf_page\": 435,\n \"book_page\": 405,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-13\",\n \"entries\": [entry]\n}\n\nwith open('/home/sfmqrb/git/rishe/data/verification/page-435.json','w',encoding='utf-8') as f:\n    json.dump(out, f, ensure_ascii=False, indent=2)\nprint(\"written\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-435.py && python3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-435.json > /dev/null && echo \"valid json\" && python3 /home/sfmqrb/git/rishe/tools/verify_check.py 435"
}
```


### [2026-09-14T01:45:15.618Z] TOOL RESULT

```
written
valid json
nodes verified: 13/13
node verdicts: {'transcription_suspect': 1, 'confirmed': 8, 'disputed': 3, 'plausible': 1}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 10, 'partial': 5, 'not_checked': 2}
books consulted: {'supports': 24, 'partial': 5, 'contradicts': 5, 'silent': 2} | by book: {'CHEUNG': 5, 'BRT': 5, 'NYB': 4, 'WLD': 4, 'KLN': 4, 'POK': 3, 'PHD': 2, 'KNT': 2, 'MON': 2, 'IEC': 1, 'FFD': 1, 'SYN': 1, 'HRN': 1, 'AHD': 1}
```


## [2026-09-14T01:45:38.796Z] AGENT

Done — `/home/sfmqrb/git/rishe/data/verification/page-435.json` written; `verify_check.py 435` reports 13/13 nodes, **0 PROBLEM lines**.

**PDF page 435 (book p. 405), root "Sed" (PIE \*sed-), 1 entry, 13 nodes**
- Root: confirmed. Node verdicts: 8 confirmed, 3 disputed, 1 plausible, 1 transcription_suspect. Ref checks: 10 supports, 5 partial, 2 not_checked (empty-ref nodes); 36 `consulted` entries across 14 books.

Flagged items:
- **disputed #3** (Av. `sad, sand` "settlement, agreement") — Av. sand-/sad- means "to appear, seem (good)" (Cheung 333, PIE *(s)ḱend-, "Pok.: —"), a different root from \*sed-. `upa-sad`/`avara-sad` are not in Bartholomae; "avara-sad" is Nourai's own segmentation of xorsand. Horn p.71's parenthesis about the homonymous root sad- "sitzen" is the likely source of the merger.
- **disputed #4** (`pasandîdan`, `xorsand`) — real words, wrong parent: MP passandīdan < \*pati-sand-, MP hunsand < \*hu-sand- (Nyberg: xʷan-/xʷar- + sand-), never \*avara-. Mo'in's own footnote at BQT:406 records Nyberg's "to seem" derivation beside the old "sit" one.
- **disputed #6** (`naxost`) — nazd is confirmed, but MP naxust/naxwist [nhwst'] is the superlative of nwx "beginning" (Nyberg) / PIr \*naxu- (Wiktionary); MP nazdist is a separate word. Nourai follows the old Parsi view Mo'in quotes from Barucha (BQT:2123, read off the page image, saved as `ocr/BQT/2123.vision.txt`).
- **transcription_suspect #1** — book prints "had, hd, zd, šas 2"; "hd"/"zd" are impossible Avestan forms (truncations of hiδ-/hazd-), and "šâdayeiti : sits" is really the causative. `error_in: book` — the printed page (image saved to `ocr/BOOK/435.png`) matches the JSON exactly.
- **plausible #8** (syazd-, sīzdyamna-…) — forms genuine, but Pokorny 887 and WP II 489 attach them to \*sed- only with "vielleicht" (\*ḱe-zd-, like Lat. cēdō); Bartholomae marks "Et.?".

Bad reference in the book (not an extraction error): **KLN:1075** at the root box — Klein p.1075 is the Naaman–namesake range; his \*sed- discussion is s.v. *cede* (~p.266) and *sedentary* (~p.1471), whose wording Nourai's root gloss actually paraphrases.

No extraction errors found: every checked form in the JSON matches the printed page, including the italic "p s n d, d l p s n d" line in node #4 (the book's own consonant-skeleton rendering of پسند / دل‌پسند). MON:2782,3797 content verified via Mo'in on abadis.ir ([فر.] = French) but the page numbers are unverifiable locally (Mo'in vols 3–6 not on disk paginated).
