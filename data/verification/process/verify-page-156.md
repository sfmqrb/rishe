# Verification process log — verify-page-156


## [2026-09-05T20:27:37.800Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 156 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-156.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-156.json. Write /home/sfmqrb/git/rishe/data/verification/page-156.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 156` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-05T20:27:39.159Z] AGENT

I'll start by reading the instructions.


## [2026-09-05T20:27:39.890Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-05T20:27:39.904Z] TOOL RESULT

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


## [2026-09-05T20:27:40.498Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-156.txt"
}
```


### [2026-09-05T20:27:40.514Z] TOOL RESULT

```
1	=== PDF page 156 (book page 126) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Er 1, Or : to set in motion, excite  (refs POK:327)  PART 1
4	#1 (parent #0) [Avestan / Old Persian] refs=POK:327; BRT:184,368; FSF:105 | ar, ra 1 : to move ; ras 1, rasa : to come, arrive ; paity-âra : against progress, ugly ☞Per 3 ; pati-ara : challenge, fight ☞Per 3
5	  #2 (parent #1) [Persian] refs=HRN:137; BQT:374,950; FSF:107; FFD:56 | resîdan «رسیدن» : to arrive, to ripe ; patyâreh «پتیاره ، پتیره» : enemy, ugly ; pazîreh «پذیره» : to challenge an enemy, fight | extra: رس ، نورسیده
6	#3 (parent #0) [Avestan / Old Persian] refs=POK:331; IRN:112; KNT:170 | aurva, aurvant : swift, fast ; auruma : wildly ; aurvat-aspa : (with) fast horses ☞Ekwos
7	  #4 (parent #3) [Persian] refs=BQT:111,160,1918; IRN:114 | Arvand «اروند» : Tigris river ; Alvand «الوند» : name of a mountain with many springs ; Lohrâsp «لهراسپ» : "with fast horses", a male name | NOTE: "Arvand:swift" is a translation of "Dejleh:swift". See Root "Steig"
8	#5 (parent #0) [Sanskrit] refs=POK:330 | rad, radati : scrapes, scratches
9	  #6 (parent #5) [Persian] refs=MON:964; HRN:138 | randîdan «رندیدن» | extra: رنده
10	#7 (parent #0) [Avestan] refs=BQT:987; SYN:278; HRN:142 | rî, rae, raec 1 : to release, discharge, defecate
11	  #8 (parent #7) [Pahlavi] refs=HRN:142; BQT:987; SNS:235 | rîtan : to defecate ; rěman : dirty discharges from eyes etc.
12	    #9 (parent #8) [Persian] refs=HRN:142; BQT:987,990 | rîdan «ریدن» : defecate ; rîm «ریم ، ریمن ، ریمه» : dirt, evil; dirty discharge from the eye
13	#10 (parent #0) [Avestan / Sanskrit] refs=WLD1:136; AEF:20 | ari, arika, araeka : enemy, hostility, hatred
14	  #11 (parent #10) [Persian] refs=BQT:33; AEF:20,21 | ârîğ «آریغ» : hostility, hatred ; rîğ «ریغ» : animosity, also hated, enemy, dung | extra: أریغ
15	#12 (parent #0) [Avestan] refs=POK:327-331 | arati : energy ; aranu, ham-aranu : hostile coincidence, fight, competition ☞Sem 1 ; ham-ara, ham-aratha : opponents ☞Sem 1 ; râna 1 : fighter ; artha : affair
16	#13 (parent #0) [Latin] refs=AHD | oriri : to appear, rise (sun) ; rivus : stream
17	  #14 (parent #13) [English] refs=None | orient, origin, abort, rival, derive
18	#15 (parent #0) [Germanic] refs=AHD | ri-nwan : to run ; art : to be
19	  #16 (parent #15) [English] refs=None | run, are
20	
```


## [2026-09-05T20:27:43.559Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-156.json",
 "description": "Read source JSON page 156"
}
```


### [2026-09-05T20:27:43.607Z] TOOL RESULT

```
{
  "pdf_page": 156,
  "book_page": 126,
  "entries": [
    {
      "root": {
        "name": "Er 1, Or",
        "lang": "Indo-European",
        "refs": "POK:327",
        "gloss": "to set in motion, excite"
      },
      "part": 1,
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan / Old Persian",
          "refs": "POK:327; BRT:184,368; FSF:105",
          "words": [
            {"translit": "ar, ra 1", "gloss": "to move", "script": null},
            {"translit": "ras 1, rasa", "gloss": "to come, arrive", "script": null},
            {"translit": "paity-âra", "gloss": "against progress, ugly", "script": null, "see": ["Per 3"]},
            {"translit": "pati-ara", "gloss": "challenge, fight", "script": null, "see": ["Per 3"]}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "HRN:137; BQT:374,950; FSF:107; FFD:56",
          "words": [
            {"translit": "resîdan", "gloss": "to arrive, to ripe", "script": "رسیدن"},
            {"translit": "patyâreh", "gloss": "enemy, ugly", "script": "پتیاره ، پتیره"},
            {"translit": "pazîreh", "gloss": "to challenge an enemy, fight", "script": "پذیره"}
          ],
          "script_extra": "رس ، نورسیده",
          "note": null,
          "quote": {"text": "پذیره شدش دیو را جنگجوی - سپه را چو روی اندر آمد به روی", "poet": "Ferdowsî"}
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Avestan / Old Persian",
          "refs": "POK:331; IRN:112; KNT:170",
          "words": [
            {"translit": "aurva, aurvant", "gloss": "swift, fast", "script": null},
            {"translit": "auruma", "gloss": "wildly", "script": null},
            {"translit": "aurvat-aspa", "gloss": "(with) fast horses", "script": null, "see": ["Ekwos"]}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Persian",
          "refs": "BQT:111,160,1918; IRN:114",
          "words": [
            {"translit": "Arvand", "gloss": "Tigris river", "script": "اروند"},
            {"translit": "Alvand", "gloss": "name of a mountain with many springs", "script": "الوند"},
            {"translit": "Lohrâsp", "gloss": "\"with fast horses\", a male name", "script": "لهراسپ"}
          ],
          "note": "\"Arvand:swift\" is a translation of \"Dejleh:swift\". See Root \"Steig\"",
          "quote": {"text": "اگر پهلوانی ندانی زبان - بتازی تو اروند را دجله خوان", "poet": "Ferdowsî"}
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "POK:330",
          "words": [
            {"translit": "rad, radati", "gloss": "scrapes, scratches", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "Persian",
          "refs": "MON:964; HRN:138",
          "words": [
            {"translit": "randîdan", "gloss": null, "script": "رندیدن"}
          ],
          "script_extra": "رنده",
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 0,
          "lang": "Avestan",
          "refs": "BQT:987; SYN:278; HRN:142",
          "words": [
            {"translit": "rî, rae, raec 1", "gloss": "to release, discharge, defecate", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 7,
          "lang": "Pahlavi",
          "refs": "HRN:142; BQT:987; SNS:235",
          "words": [
            {"translit": "rîtan", "gloss": "to defecate", "script": null},
            {"translit": "rěman", "gloss": "dirty discharges from eyes etc.", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "Persian",
          "refs": "HRN:142; BQT:987,990",
          "words": [
            {"translit": "rîdan", "gloss": "defecate", "script": "ریدن"},
            {"translit": "rîm", "gloss": "dirt, evil; dirty discharge from the eye", "script": "ریم ، ریمن ، ریمه"}
          ],
          "note": null,
          "quote": {"text": "او را ز ریمنی گهر پاک بازداشت - ممکن نباشد از گهر پاک ریمنی", "poet": "Manûchehrî"}
        },
        {
          "id": 10,
          "parent": 0,
          "lang": "Avestan / Sanskrit",
          "refs": "WLD1:136; AEF:20",
          "words": [
            {"translit": "ari, arika, araeka", "gloss": "enemy, hostility, hatred", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 10,
          "lang": "Persian",
          "refs": "BQT:33; AEF:20,21",
          "words": [
            {"translit": "ârîğ", "gloss": "hostility, hatred", "script": "آریغ"},
            {"translit": "rîğ", "gloss": "animosity, also hated, enemy, dung", "script": "ریغ"}
          ],
          "script_extra": "أریغ",
          "note": null,
          "quote": {"text": "جهان و ویژه کردم به برّنده تیغ - چرا دارد ازمن به دل شاه ریغ", "poet": "Ferdowsî"}
        },
        {
          "id": 12,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:327-331",
          "words": [
            {"translit": "arati", "gloss": "energy", "script": null},
            {"translit": "aranu, ham-aranu", "gloss": "hostile coincidence, fight, competition", "script": null, "see": ["Sem 1"]},
            {"translit": "ham-ara, ham-aratha", "gloss": "opponents", "script": null, "see": ["Sem 1"]},
            {"translit": "râna 1", "gloss": "fighter", "script": null},
            {"translit": "artha", "gloss": "affair", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 13,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "oriri", "gloss": "to appear, rise (sun)", "script": null},
            {"translit": "rivus", "gloss": "stream", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 14,
          "parent": 13,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "orient, origin, abort, rival, derive", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 15,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "ri-nwan", "gloss": "to run", "script": null},
            {"translit": "art", "gloss": "to be", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 16,
          "parent": 15,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "run, are", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    }
  ]
}
```


## [2026-09-05T20:27:44.467Z] TOOL CALL #4: Bash

```json
{
 "command": "ls data/verification/ | head -50 && echo ---- && cat tools/verify_check.py | head -80",
 "description": "List verification dir and check script"
}
```


### [2026-09-05T20:27:44.514Z] TOOL RESULT

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
page-129.json
page-130.json
page-131.json
page-133.json
page-135.json
page-137.json
page-138.json
page-144.json
page-146.json
page-311.json
page-31.json
page-32.json
page-33.json
page-345.json
page-34.json
page-35.json
page-36.json
page-37.json
page-38.json
page-39.json
page-40.json
page-41.json
----
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


## [2026-09-05T20:27:49.286Z] TOOL CALL #5: Bash

```json
{
 "command": "sed -n '80,200p' tools/verify_check.py",
 "description": "Rest of verify_check.py"
}
```


### [2026-09-05T20:27:49.337Z] TOOL RESULT

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


## [2026-09-05T20:27:49.635Z] TOOL CALL #6: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-05T20:27:49.674Z] TOOL RESULT

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


## [2026-09-05T20:28:47.115Z] TOOL CALL #7: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','BRT','FSF','HRN','BQT','FFD','IRN','KNT','MON','SYN','SNS','WLD','WLD1','AEF','AHD','PHD','NYB','CHEUNG','ARY','IEC','LEW','KLN','SKT','HUB']:\n    v=d.get(k)\n    print('===',k, json.dumps(v,ensure_ascii=False)[:700] if v else 'MISSING')\n\"",
 "description": "Dump refs_online entries"
}
```


## [2026-09-05T20:28:47.445Z] TOOL CALL #8: Bash

```json
{
 "command": "head -c 3000 data/verification/page-146.json",
 "description": "Look at an example verification file"
}
```


### [2026-09-05T20:28:48.888Z] TOOL RESULT

```
=== POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index 
=== BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \\f between 
=== FSF {"title": "Abdolhossein Noushin, Vazhe-namak: Farhang-e Vazheha-ye Doshvar-e Shahnameh (Farhang-e Shahnameh), Donya 1363/1984", "kind": "archive_djvu", "url": "https://archive.org/details/20220809_20220809_1444", "lookup_hint": "grep the headword in FSF_pages.txt (alphabetical glossary); use inside.php search for leaf numbers. Also https://archive.org/details/nooshinshahnameh is a different Noushin book (گزارشی چند درباره شاهنامه).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF.txt"], "page_offset": "484 leaves; edition/printing of this scan not identified — determine offset from printed page 
=== HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or grep the 
=== BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.c
=== FFD {"title": "Mohsen Abolghasemi, Fe'l-ha-ye Farsi-ye Dari, Qoqnus, Tehran 1374/1995", "kind": "local_scan_ocr", "url": "https://asmaneketab.ir/product/کتاب-ماده-های-فعلهای-فارسی-دری-محسن-اب/ -> https://dl.eliteraturebook.com/app/public/attachments/6925d29630b83.PDF (free PDF site; grey)", "lookup_hint": "Searched archive.org (Persian/Latin titles, author), ketabnak, noorlib, general web (pdf/download): nothing; only a related paid e-book 'واژگان زبان فارسی دری' (fidibo). ketabnak.com/book/45024 is a different book (فهرست فعلهای فارسی).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_asmaneketab.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/ref
=== IRN {"title": "Bahram Farahvashi, Iranvij, Tehran University Press 1368/1989", "kind": "local_scan_ocr", "url": "https://asmaneketab.ir/product/کتاب-ایرانویج-بهرام-فره-وشی/ -> https://dl.eliteraturebook.com/storage/img/ایرانویج.pdf (free PDF site; grey) ; Google Books kP8bAAAAIAAJ (1368 ed., no view)", "lookup_hint": "archive.org 'Iranvej' item is a radio programme, not the book; nothing on ketabnak/noorlib. | For pages in a scanned volume use: python3 tools/ref_page.py IRN:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/IRN/IRN_eliteraturebook.pdf", "/home/sfmqrb/git/rishe/data/verific
=== KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt", "page_offset": "leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archiv
=== MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol 
=== SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<i
=== SNS {"title": "Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/VajnameShayest", "lookup_hint": "grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php search (see BQT) for better hit-to-leaf mapping.", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS.txt"], "page_offset": "242 leaves; page offset not determined (OCR too poor to read printed numbers) — 
=== WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.39015066210397 (browser only from this host)", "identifier": "in.gov.ignca.20339 (Band 3); also in.ernet.dli.2015
=== WLD1 MISSING
=== AEF {"title": "Jalal Khaleqi Motlaq, Asas-e Eshteqaq-e Farsi, vol. I (آ–خ), Bonyad-e Farhang-e Iran 1356/1977 — this is the Persian TRANSLATION of Paul Horn's Grundriss der neupersischen Etymologie (HRN) with Hübschmann's Persische Studien (HUB) notes and added Persian/Pahlavi evidence", "kind": "catalog", "url": "https://openlibrary.org/works/OL38785552W (vol. 1, 1356) ; 2015 complete ed. «فرهنگ ریشه‌شناسی فارسی» (مهرافروز) print-only: https://www.gisoom.com/book/11154690/ ; German original: https://archive.org/details/grundrissderneu00horngoog", "lookup_hint": "Not online (searched archive.org, ketabnak, noorlib, web; only bookshop listings). Because it is a translation of Horn/Hübschmann, ver
=== AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only", "identifie
=== PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<ident
=== NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Nourai's 'NYB' nu
=== CHEUNG MISSING
=== ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY:<printed page> --image", "local_file": ["/home/sfmqrb/git/rishe/
=== IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Reconstruct
=== LEW {"title": "A. Walde (& J. B. Hofmann), Lateinisches etymologisches Wörterbuch, 3rd ed., Heidelberg 1938-56", "edition_found": "2nd ed. 1910 (open); 3rd ed. 1938 vol. 1 is lending-only (lateinischesetym0000awal)", "kind": "archive_djvu", "url": "https://archive.org/details/lateinischesetym0000aloi", "identifier": "lateinischesetym0000aloi (1910); restricted 1938: lateinischesetym0000awal", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LEW_1910.txt", "page_offset": "1910 ed.: leaf = printed + 12 (e.g. leaf 15 = p.3). Page numbers of the 3rd ed. differ. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.o
=== KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt", "page_offset": "KLN_1966: TWO pri
=== SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<i
=== HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by parag
```


### [2026-09-05T20:28:48.941Z] TOOL RESULT

```
{
  "pdf_page": 146,
  "book_page": 116,
  "verified_by": "claude-opus-5",
  "verified_on": "2026-09-05",
  "note": "This page contains no charts. Both entries are cross-reference stubs: 'Dyě  see root: Dei' and 'Dyeu  see root: Dei'. Per the verification instructions redirect entries are skipped, so this file carries no entries. Checked against the printed page (site/pages/146.jpg, book p. 116): the page shows exactly two headword boxes with 'see root: Dei' in italics and nothing else, so the extraction in data/extracted/batch/page-146.json is faithful. The redirect target is real: the root box 'Dei, Deiw, Dyeu, Dyě' stands on PDF page 112 (verified in data/verification/page-112.json), and it explicitly lists both Dyě and Dyeu among its variant spellings, so both pointers resolve correctly. Nourai's variants correspond to the standard PIE root *dyew- / *dei̯H- 'to shine; sky, day, god' (Pokorny 183-187 dei-, deia-, di-, deía-).",
  "note_fa": "این صفحه هیچ نموداری ندارد؛ هر دو مدخل آن تنها ارجاع‌دهنده‌اند: «Dyě» و «Dyeu» هر دو به ریشهٔ «Dei» ارجاع داده شده‌اند. بر پایهٔ دستورالعمل ارزیابی، مدخل‌های ارجاعی بررسی نمی‌شوند، پس این پرونده بدون مدخل است. تصویر صفحهٔ چاپی (صفحهٔ ۱۱۶ کتاب) با دادهٔ استخراج‌شده مطابقت کامل دارد و خطای خوانش در کار نیست. ریشهٔ مقصد نیز واقعی است: جعبهٔ «Dei, Deiw, Dyeu, Dyě» در صفحهٔ ۱۱۲ پی‌دی‌اف آمده و هر دو صورت را در خود جای داده است؛ این صورت‌ها همان ریشهٔ شناخته‌شدهٔ هندواروپایی آغازین *dyew- / *dei̯H- «درخشیدن؛ آسمان، روز، خدا» (پوکورنی، صفحات ۱۸۳–۱۸۷) هستند.",
  "entries": []
}
```


## [2026-09-05T20:28:52.806Z] TOOL CALL #9: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/page-124.json'))\ne=d['entries'][0]\nprint(json.dumps(e['nodes'][0],ensure_ascii=False,indent=1)[:3000])\n\"",
 "description": "Sample node from page 124"
}
```


### [2026-09-05T20:28:54.489Z] TOOL RESULT

```
{
 "id": 1,
 "lang": "Avestan",
 "words": "ma[n]dz-dha; ahura-mazdha",
 "verdict": "confirmed",
 "derivation": "The Avestan words are mazdā- / mazdah- n. 'memory, wisdom' and the divine name ahura- mazdā- 'Lord Wisdom' (Ahura Mazda). The second member really is this root: the compound is Proto-Indo-Iranian *mns-dʰeh₁- 'to set (something) in mind, commit to memory', i.e. *men- 'think' + *dʰeh₁- 'put'; Pokorny treats it under mendʰ- (Page(s): 730): 'Avestan mazda, mazdah- n. „Gedächtnis“, mazdah- m. name of the highest God (*mazdʰa from *mn̥dʰ-ta)'. Nourai's odd transliteration 'ma[n]dz-dha / ahura-mazdha' is copied letter for letter from Klein s.v. Ormazd ('ma(n)dzdha-, ‘wise’, which is a compound formed from the I.-E. bases *men-dh- and *dhe- ‘to put, place’'); the actually attested Avestan spelling is mazdā-, so the -dh- here is Klein's etymologising respelling, not an Avestan form. The gloss 'done learning, wise' and the cross-reference to Men 1 are both correct.",
 "derivation_fa": "واژهٔ اوستایی mazdā- / mazdah- به معنی «خرد، یاد» و نام ایزدی ahura-mazdā- «سرورِ خرد» از ترکیب هندوایرانی آغازین *mns-dʰeh₁- «در یاد نهادن» ساخته شده است؛ یعنی ستاک *men- «اندیشیدن» به علاوهٔ همین ریشهٔ *dʰeh₁- «نهادن». پوکورنی این واژه را در صفحهٔ ۷۳۰ ذیل mendʰ- آورده (نه در صفحهٔ ۲۳۵ که نورایی ارجاع داده). املای غریبِ «ma[n]dz-dha» عیناً از کلاین (ذیل Ormazd) گرفته شده و صورت اوستایی واقعی mazdā- است. در مجموع ادعای نورایی درست است.",
 "sources": [
  "https://en.wiktionary.org/wiki/Ahura_Mazda",
  "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/d%CA%B0eh%E2%82%81-"
 ],
 "ref_check": [
  {
   "ref": "POK:235",
   "status": "partial",
   "note": "POK_full.txt lines 22276-22510: the lemma at 'Page(s): 235-239' is 'dʰe-2, Meaning: to put, place, say' and it does NOT mention mazdā anywhere. Pokorny discusses mazdā s.v. mendh- at 'Page(s): 730' (line 59307: 'Avestan mazda, mazdah- n. \"Gedächtnis\", mazdah- m. name of the highest God (*mazdʰa from *mn̥dʰ-ta)'). The -dhā element is this root, so the claim holds, but the cited page is the wrong one."
  }
 ],
 "consulted": [
  {
   "src": "POK",
   "where": "p.730 s.v. mendh- (POK_full.txt line 59307)",
   "stance": "supports",
   "note": "'Avestan mazda, mazdah- n. \"Gedächtnis\", mazdah- m. name of the highest God (*mazdʰa from *mn̥dʰ-ta)' — the compound of *men-dh- + *dhē-."
  },
  {
   "src": "KLN",
   "where": "p.1096 s.v. Ormazd (KLN_1966.txt leaf 586)",
   "stance": "supports",
   "note": "'fr. Avestic Ahuramazda, lit. \"wise lord\", a compound of ahura- ... and ma(n)dzdha-, \"wise\", which is a compound formed from the I.-E. bases *men-dh- ... and *dhe-, \"to put, place\"' — Nourai's spelling and analysis come from here."
  },
  {
   "src": "BRT",
   "where": "Altiranisches Wörterbuch, passim (e.g. BRT.txt line 10715)",
   "stance": "supports",
   "note": "OCR of the headword column is unreadable, but the god's name is spelt mazdā / mazdå throughout the quoted Gāthā passages ('ahurō mazdā', 'ta
```


## [2026-09-05T20:29:09.565Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Page(s): 32[6-9]\\|Page(s): 33[0-2]\" POK_full.txt | head -40",
 "description": "Find Pokorny pages 326-332"
}
```


### [2026-09-05T20:29:09.619Z] TOOL RESULT

```
27913:Page(s): 326 
28431:Page(s): 326-332 
28468:Page(s): 332 
28527:Page(s): 332-333
```


## [2026-09-05T20:29:12.038Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '27900,28470p' POK_full.txt",
 "description": "Print Pokorny er-3 entry"
}
```


### [2026-09-05T20:29:12.096Z] TOOL RESULT

```
Armenian erinj^ young cow, heifer, calf, young bull, an ox, a bull, a cow '; gr. spicpoc; 
( *eri-b^o-) m. f. 'kid, young goat'; 
In a- grade: 

Latin aries, -e//5 'Aries, a ram; a battering ram; a prop, beam ' [for the kindr. forms arvix 
and harvix , in Varr. and Fest.; v. arvix; poet, aries] (5 after aper, caper); Umbrian erietu^ 
arietem '; russ.-Church Slavic 75/7/75 'wool', etc.. Common /7->y- Slavic Albanian; h->J-, y- 
Old Indie Tocharian. 

Old High German irah^ he-goat; billy goat ' etc. is borrowed from Latin hircus^a he- 
goat'. 

References: WP. I 135 f., WH. I 67, Trautmann 70. 
Page(s): 326 

Root / lemma: er-3 : or- : r- : {*her-3) 

Meaning: to move *stir, animate, fight, struggle, rise; to spring up, be born 

Note: originally athematic root with terminative aspect. Basic forms er-, ere-, ere- (7), ere/-, 

ereu- and (under besond. article) eres- 

Note: 

Root/ lemma: ar-l', themat. (ajre-, heavy basis are-, re- and /-Basis {ajn-, rei-\ "to move, 

pass' 



and Root / lemma: er-3\ or-: r-\ 'to move *stir, animate, fight, struggle, rise; to spring up, 
be born' derived from the same root Root/ lemma: er-1, or-\ "eagle'. 
Material: Conclusions by Persson Beitr. 281 ff., 636 ff., 767 ff., 836 ff. 

a. Basic forms er-, ere- (including paradigmatic with it combined /-and ^-forms): 

Old Indie redupl. present fy-ar-ti, iyarti^ sets in motion ', Med. Trie {*i-er-)\ Gatha- 



Avestan TratO' he should rise '; Old Indie intensive present alartr, from ereu-{see below S. 
2>'i^) rnotirnvati^ rises, moves, animates ' (gr. opvupi 'urge on, incite, make to arise, call 
forth, move, stir oneself, awaken, arouse from sleep'), a/fa (compare wpro), arata 
(compare wpsTo; themat. as rante, ranta), Perf. ara: op-wpa, Fut. arisyatf, participle „/fa- 
[Trna- " moved, excited ' with separation of /"from Trta or or real form of a heavy base); 



Nostratic etymology: 

Proto-IE: *ela- <PIH *H-> 

Nostratic: 

Meaning: to move, to drive 

Hittite: halai- (II) 'in Bewegung setzen' (nach unten?) (Tischler 126); halija- (I) 'niederknien, 

niederfallen', caus. halinu- (Tischler 130) 

Old Indie: iyarti "to go, move', med.Trte "to go, move, rise, go away, retire' 

Avestan: gath. Tratu " he should rise ' 

Amnenian: elanem " come out, go up ', e+anim " become, turn into - ' 

Greek: iailo, aor. iaiaj " send, stretch '; *elami (arg. pot-elato, ko. elanto), elao, elauno, aor. 

elas(s)aj, pf, med. elalaka, aor. pass. ela(s)the'^naj " float, bump, forge ', elasi-s " train, 

army train, ride ', ? elatro-n " flat cake ', elater " driver, car driver ', " flat cake ', elata-s " 

driver ', elato- " pliant, driven ' 

Proto: *ala 

Nostratic: 

English meaning: space below smth., below 

Finnish: ala ' place, field, area ', alia (postp.) ' under, below ' 

Estonian: ala ' math, subspace; reason, origin '. all (postp.) ' under, below ' 

Saam (Lapp): vuolle ~ vuolle -I- 'down; (in comp.) 'space or part under smth...' (N), -vuolle ' 

the place below or close, base ' (L), vTille (T) ' the lower ', vTJne, vTiln (T), vGiln (Kid.), vueiln 

(Not.), voiln (Not.) (adv., postp.) ' under, below ' 

Mordovian: al (E M) ' lower, located below ', alo (E), ala (M) ' under, below ' 



Mari (Cheremis): iJI- (KB, B), ijlo-, iJI- (U) ' the lower, the under- ', ulna (KB), ijlno (U, B) 

(adv. postp.) ' under, below ' 

Udmurt (Votyak): ul (S) 'lower part, lower section, bottom , unterspace, bottom', ulen (K) ' 

under, below ', ul (G) ' math, subspace, bottom ', ufin (G) 'under' 

Komi (Zyrian): -ul (S), -jv (P) in 303-ul, 3e3-jv ' Space, cellar under the floor ', uNn (S), uvjn 

(P) ' under, below ', ul (PO) ' the lower ', ulon (PO) ' low, below, under ' 

Khanty (Ostyak):jl (V), it (DN), il (O) ' low, down ',jl9n (V), iten (DN), ilen (O) 'under' 

Mansi (Vogul): jale k (TJ), jalx (KU), jalk (P), jolik (So.) ' the lower ', jale-n (TJ), j5ln (KU), 

jalen (P), jolen (So.) 'under', jil (TJ) ' down; downwards ' 

Hungarian: al- ' under-; lower part; litter ', alatt (adv. post.) ' under, below ' 

Nenets (Yurak): nilna (O) ' under, below ', nil? ' downwards, down ' 

Enets (Yen): '\do (Ch.), iro (B) 'Ground', idone (Ch.) 'under' 

Nganasan (Tawgi): nilea ' the lower ' 

Selkup: mI (Ta.), Tl (Ke.), Tl, T I ' Ground, the lower ', nl (Ta.), ille (N) ' there under ' 

Kamass: jilde ' there below ', jilgen 'under' 

Janliunen's version: (38) *i6la 

Sammalaliti's version: *i6la 

Yukagliir parallels: -al ' under, below ' 

References: FUV; SKES; K3CK5R; MUSz. 728; MSzFgrE; TESz.; EtSz.; SzofSz.; Donn. 

VglWb. II, 116; Paas. Beitr. 38; \ABn9\ 212; Collinder JukUr. 75 

Maybe alb. u/^ lower ', u/em' sit down ', u/et' low, base, vulgar ' : Mari (Cheremis): iJI- 

(KB, B), iJlo-, iJI- (U) ' the lower, the under- ', ulna (KB), iJIno (U, B) (adv. postp.) ' under, 

below ' : Udmurt (Votyak): ul (S) 'lower part, lower section, bottom , unterspace, bottom', 

ul§n (K) ' under, below ', ul (G) ' math, subspace, bottom ', ulln (G) 'under' : Komi (Zyrian): 

-ul (S), -jv (P) in 303-ul, 3e3-jv ' Space, cellar under the floor ', uNn (S), uvJn (P) ' under, 

below ', ul (PO) ' the lower ', ul0 n (PO) ' low, below, under ' 



Avestan a/"- "(be) set in motion, arrive at, reach', present-stem ar-: are-, iyar-: ir- (as 
Old Indie fyarti : Trta), Kaus. araya-, participle -areta-, 

s^opresent Old \v\6\c rcchati^ bumps into something, encounters, reaches ', next to 
which *re-sRd\v\ Old pers. rasaf/y' comes, arrives at ', np. rasadds.; 

The following cognates are compounds of Root/ lemma: sem-2: one + Root/ lemma: er-3 

: or-. r-\ "to move *stir, animate, fight, struggle, rise; to spring up, be born' = [fight 
together]: 



Old Indie sam-ara-m., sam-arana-n. "fight, struggle, contention ', Avestan ham-arana-, 
Old pers. ham-arana- v^. " hostile encounter, fight, struggle ', Avestan hamara-m. (and with 
th- formants hamara&a-m.) " adversary, rival, enemy'; Old Indie frya- " vigorous, strong, 
energetic ' (could belong to /-basis), /r/n-\ast, grand, violent, forcible ', arfha-n. m. 
"(*wherefore one arrives at )' " affair, thing, business; blessing, fortune, benefit, advantage', 
Avestan ar^a-n. "thing, affair, incumbency, litigation '; 

Maybe gr. 6p6q " one and the same, common, joint, unite ' > gr. opspoq: TucpAoq, Hsch.(cf. 
"Opripoc;)- m. " a pledge for the maintenance of unity, a surety, a hostage ' : Old Indie sam- 
ara-m., sam-arana-n. "fight, struggle, contention ', Avestan ham-arsna-. Old pers. ham- 
arana-w. " hostile encounter, fight, struggle ', Avestan hamara-m. (and with //> formants 
hamsra&a-xw.) " adversary, rival, enemy'; Hence Homer\Nas not a bard. The Old Persian 
compound meant "war (of llion)'. Actually the main theme of the iliad is the fury of Achilles 
and the maintenance of unity. 

Old lndic„/f/-, ///-f. "attack, fight', Avestan -arsti-^ energy ' (compare Old Bulgarian ratb); 

Old Indie arta-^ afflicted, injured, hurt, disabled, pressed, ailing ', arti-i. " mischief, 
affliction ' {*a-rta-, -rti-)\ 

Old Indie arna- " flowing, surging, flooding ', m. " surge, tide, flood ', arnas- n. " flowing 
flood ' (formal = gr. £pvo(; n.; compare S. 328 Old High German runs), arnava- " billowing, 
surging '; m. "flood, surging sea' {uo- further formations to arna-? or in older formant 
relationship io rnotR The latter is sure for:) Avestan aranu-m. "fight, struggle, contest ' (: 
Old High German ernustS. 331); 

from the themat. root form (e)re-0\6 Indie rana-m. n. "fight, struggle' (versch. from 
rana- m. "lust') = Avestan rsna-n. "action, struggle, fight'; Avestan rana-, rqna-m. " fighter, 
combatant '; 

Armenian y-arnem^ I stand up, I am lifted '; after Pisani Armen. 4 in addition ore-ar 
"people' (see below Latin orioi); with -d^- (compare S. 328 spsGw, spsGi^oj, opo-Guvw): y- 
ordor^ fast ', yordorem^ encourage, arouse, irritate '; a/777 "roof (: 6p|j£vo(;); ordi. Gen. 
ordvoy " son ' ( *orA '^//d) ; 

gr. opvupi "urge on, incite, make to arise, call forth, move, stir oneself, awaken, arouse 
from sleep' (: Old \r\d'\crnotr, compare Schwyzer Gr. Gr. I 696p; das o after 6p£0|jai?), Aor. 
(Lpaa, wpopov, opaoj, Med. opvupai, wpro " aroused, animated, uplifted ', Fut. opouijai, 
thematic Aor.wpsro, participle oppevog, Perf. opwpa " have been excited '; with op- as 



iterative vocalism 6p£-o|jai, -ovto "sally, burst forth, rushed forth', with e/"- still spero 
cbpfjriGri Hes., spaso SiEysipou Hes., spap oppnap (which then permeated through wpsTO, 
opaso forms); a present *ipvu|ji (as KipvpiJi) follows from Cretan Zsuc; "EnipvuTiO(; 
(Schwyzer Gr. Gr. I 695); -opTO(; in v£opT6(; "new born', 9£opTO(; " celestial, heavenly ', etc.; 
Kuv-, AuK-opTQc;, Aa-£pTr|<;; hom. oupoq " favorable sailing wind ' (*6pFoc;, "navigating the 
ship'), 6po(; m. " actuation, drive '; 

with ^r^extension epxopai " start, set out, come or go, come to, arrive at ' (only present), 
opxeopai "dances' (Schwyzer Gr. Gr. I 702); see below Old Irish regaid, 

6pM£V0(; " shoot, sprout, or stem, stalk ', about 6papvo(; "twig, branch', 6^6ba\\yoc„ 
pa5apvo(; ds., s. Schwyzer Gr. Gr. I 3132; 

er-\x\ spvoq (£pvo(;, Schwyzer Gl. 5, 193) "sprout, twig, branch' ("*shot up ', as 
Norwegian runne, rune't\N\g, branch': formal = Old Indie arnas- n.); £p£a(;T£Kva. 0£aaaAoi 
Hes., £p£9u), £p£9i^u) " agitate, perturb, irritate ' (opoGuvu) " enrage, encourage, cheer, 
irritate '); 

From an es-stem *e/"os "elevation' from: Old Indie /si/a- "high', gr. 6po(; n. "mountain' (the 
vocalism after 6pvu|ji, partly changed perhaps also after 6ppo(;); about oupo(; = 6po(; s. 
esp. Schuize Qunder ep. 407 ff.; is Doric wpoq and Attic 'Qp£i0uia with ^\xoc, from *dmsos 
to compare and lead back to (reshuffled after an Adj. *ors-os or *ors-uos : Old Indie /5i/a-) 
*6paoc;?; gr. opaoOupn " back door ' (probably as high escape door, emergency exit??), by 
Hes. £ip£eupr| opaoOupa; 

about gr. 6ppo(; " buttocks ' see below ers-, (common Italic rs- > rr-) 

Phrygian £ipoi " children ' (Jokl Eberts Reallex. 10, 151a); 

alb. ye/777" frenzied, phrenetic, wild ' {*er-mo-)\ about perrua' riverbed, stream ' (see 
below); 

Maybe alb. ye/777" be angry ' derived in -m- suffix : russ. 6\a\. jeretftbsa 'be angry, quarrel, 
squabble' see below. Common /7->y- Slavic Albanian; h->j-, y-0\6 Indie Tocharian. 

Maybe alb. o/'a "mountain nymph'. 

Latin or/or, -Jn, ortus sum " to rise; to spring up, be born, proceed from a source or 
cause ' {ortus = Old \v\6\crta-\ oof 0/70/' either from o/Yi/s or from Aor.-stem, EM^ 713), 
ortus, -us' rising ', orfgo' origin, source, beginning; an ancestor' (could be based as or/or 



on the /-basis), Umbrian ortom'have risen', urtas'have been risen, arisen', urtes'ansen, 
stirred, agitated'; 

Old Irish Imper. e/rg'goV {*ergh-e), Fut. regaid {* rigati, Indo Germanic *rgh-)\ see above 
gr. spxepai; Celtic or- in mcymr. cyf-orm. ' troop ', oy-^yf-o/' 'elevation', ad-orth^ 
excitement, help'(*a//-c»/'-/o), etc. (Loth RC 40, 355); compare also Ifor Williams RC 43, 
271 (about Middle Irish ort 'bank, border, shore' s. Pedersen KG. I 206 f.); 

Germanic *ermana-, */rm/no'b\g, large' (: 6p[jizvoq, Church Slavic ramenb, s. Bruckner 
KZ. 45, 107) in Old High German /rm/n-deot etc. (see above S. 58); Old Icelandic ern 
{*am/a-) 'proficient, energetic ', Gothic arn/baa6v. 'certainly' (but Old Icelandic arna, -ada 
'go, drive, run' secondary from gerna^ Gothic airinon). Old High German e/77i/s/ 'fight, 
struggle, seriousness ', Old English eornosV seriousness, eagerness ' (: Avestan arenu- 
'fight, struggle'); with similarl meaning gr. £p£a(;T£Kva Hes., perhaps Proto Norse erilar. 
Old Icelandic ya/"/. Old English eorl. Old Saxon e/y'noble man, husband' (see below er- 
'eagle') ; Old Icelandic /a^a 'fight' i^era); 

Note: 

Proto Norse erilar. Old Icelandic ya/"/. Old English eorl. Old Saxon e/y'noble man, husband' 
: Lithuanian erelis, dial, arelis. Old Prussian arelie (lies arelis), Latvian erglis (aus erdlis) 
'eagle'; Baltic basic form *erelja-, derived from Root / lemma: er-1, or- : 'eagle'. Hence the 
original meaning of those cognates was 'eagle men'. Celtic people called themselves after 
the sacred bird of the sky god. Hence the eagle was a war god that is why eagle bones are 
found in Stonehenge monuments. Clearly the Celtic cognate derived from Baltic 
languages. 

Gothic rinnan, /'a/7/7'rush, run' {*re-nu-d), urr/nnan'nse, from the sun'. Old Icelandic 
rinnal\o\N, run'. Old High German Old Saxon r/nnanl\o\N, swim, run', (under the influence 
of common Celtic -ns-, -nt- > -nn-). Old English rinnan an6 iernan, arn ds.; Kaus. Gothic 
urrannjan^ allow to rise ', Old Icelandic renna' make run ', Old Saxon renniands.. Old 
High German Middle High German rennen, rante'run' (ein after /7/7/7a/7 with /?/? provided 
*roneid= Slavic /to/?/// under S. 329); 

zero grade Gothic runsm. (/-stem). Old English rynem. 'run, flow, river'. Old Icelandic 
runn. 'rivulet, brook', Gothic garunjd^ inundation, flood ', Old High German runs, runsa 
'run, flow of water, river', runsti. ' the runnel, flowing, riverbed '; Gothic garuns {siexw 
garunsh) f. 'road, market ' (actually ' the place where the people gather '; Germanic runs-: 
Old Indie arnas-). In the use of shooting up, growth the plants (compare £pvo(;, 6pp£vo(;) 



Old Icelandic rinna' sprout, grow', Norwegian runne, rune'W\g, branch' and Swedish dial. 
rana " shoot upwards, take off into the air ', Norwegian rane ' shaft, pole ', Middle High 
German ran (a) ' slim, thin ', Old High German rono'tree stem, clot, chunk, chip, splinter'; " 
exaltation, elevation ' generally in Norwegian dial, rane'cusp, peak, projecting rocks, ridge 
', Old Icelandic ran/" snout, proboscis '; 

Old Irish rind {* rend/-) 'cusp, peak'; for ot;/7)-extension see below; 

This root form *re-n- (maybe grown from a present *re-neu-mi, *re-nu-d) one also seeks 
in alb. perrua, perroi^ riverbed, brook bed ' {per-ren-, lengthened grade), prrua, PI. perrenj 
"spring' {*prer-rua^ effluence ') and in Old Bulgarian izroniti {BaWo Slavic *raneid) ' pour 
out, pour forth, shed, spread abroad ', russ. ronitb 'make or let fall ', serb. roniti^ shed 
tears, melt, urinate ', Gothic -rannjan; compare Trautmann 236 f.; 

Maybe alb. {*ke-ronJ) kroi, krua, PI. kroje^ stream' : pe-rrua, pe-rroi^ riverbed, brook bed '. 

Maybe alb. Geg (/77e) as' to fall, strike, hit', rrah {* ra-sko) ' hit', reshje^ rainfall', re^ cloud', 
perrua, perroT riverbed, brook bed ' {perrua, pe-rnua 'spring' from a prefix pe-, pe- 
common Hittie Slavic Albanian prefix + alb. * /to/?/ "running water', 

in -^r^ suffix: 

Maybe alb. rrjedheu. ' spring', rrjedhv. ' springs' common alb. -gh> -dh. 

d(h)-eyXev\s\ov\ in Lithuanian participle nusirendant, nus/rendus/'kom the setting sun', 
r/nda ' gully, runnel ' {stogo r ' gutter '), ' crib, manger ', Latvian randa ' dent where the 
water runs off; 

Old Bulgarian ratb, russ. ratb, Serbo-Croatian Aa/'fight' {*or(a)ti-). Old Bulgarian retb6s. 
' an assiduous striving to equal or excel another in any thing, emulation, jealousy, envy, 
malevolence ', russ. retb 'quarrel, strife ', Old Bulgarian retiti\o strain, stretch, exert; of 
missiles, to shoot, cast; intransit., to strive, strain, exert oneself, hasten; of statement, to 
assert with confidence, maintain. In relation to another: transit., to compare, contrast; 
intransit., to compete', russ. retovatbsa^ be angry ', retfvyj^keeu, eager, stormy, hot 
tempered, violent, fiery' (goes back to thematic {e)re- or *er-ti-, has been supported by 
russ. d\a\.jeret/tbsa^be angry, quarrel, squabble'); about Church Slavic ramenbsee above 
S. 58 under 328. Common /7->y- Slavic Albanian; h->j-, y-0\6 Indie Tocharian. 

Maybe in *-sA'aformant alb. /ra/7 'strike', rrih em ^quarre\, fight' {*ra-skd) [common alb. /? < 
sk\ 



From Hittite here (Pedersen Hittite 5 f., 45, 91 f., 122) ar- in 

1. a-ra-a-i{arai) "uplifts', besides a-ra-iz-zi(is., preterit 3. PI. {a\-ra-a-ir, 

2. 5-/7' comes ' (previous Perf.), preterit a-ar-ta {arta) or ir-ta\ 

3. Med. present ar-ta-ri^ stands, it is placed upright ' (compare gr. opwpa : Latin orioi), 
3. Sg. Preterit a-ar-as (ars) "went over, looked over'; 

4. iterative a-ar-as-ki-it {arskit) " reached repeatedly ' (compare above Old \'r\6\c rcchati); 

5. causative (compare above S. 61) ar-nu-uz-zi {arnuzi) " bring to, set in motion' (r-nu-\ 
compare above Old \v\6\c rnoti); Imper. 2. Sg. ar-nu-ut{arnut} = gr. 6pvu-9i, verbal noun a- 
ar-nu-mar ( arnumar) ; 

Hittite: arsana'h, arsanaija- (II) ' envy, be angry ' (Tischler 67-68) (but cf. also harsallant- 
'angry', Tischler 182-184 without etymology) 

to what extent Tocharian A ar-, B er- " produce, cause, bring forth ', with sk- Kaus. ars-, 
ers- ds., after Meillet (MSL. 19, 159) belong here, is doubtful; certainly remain far off AB 
ar-, ar- "cease', with s/r-Kaus. ars-, ars- " abandon ' (inaccurate Van Windekens Lexique 6, 
22). 

b. extension er-ed- (o'-present?): s. ered-^ deliquesce ', Old Indie ardati, rdati^ flows 
etc.', also " perturbed, agitated '; with Kaus. ardayati^ makes i\o^; throngs, presses, 
afflicts, slays ' was equatable Old Icelandic erta {*artjan) " incite, provoke, banter', yet is 
connection with "a/ToV- "cusp, peak, sting, prick' (above S. 63) at least equivalent; a 
dissyllabic form in apa^ouai spsGi^ouaiv Hes., apa5o(; " excitement '; 

further here or to er-50\6 Indie radati' scratches, digs, hacks, scarifies ', vf-radati^ 
cleaves, splits apart, opens '; 

perhaps also Old Prussian redo "furrow' (Persson Beitr. 667). 

c. extension er-ed'^-.'see above S. 327 EpsGu) etc. under under S. 339. 

d. basis erei-, and reia-. n-\ rqio-s, n-ti-^ flux '. 

Old Indie frya- see above S. 327; 

Old Indie rinati, rfnvati {arinvan) " allows to flow, run away, escape, dismisses, releases 
', rJyate' gerat ins Flieften, lost sich auf ', rJna-^ in Fluft geraten, flieftend ', rJti- " stream. 



run, line; run of the things, l<ind, way ' (latter meaning also in Middle Irish nan'\Ndiy, 
manner'), n't- " escaping ', raya-xr\. 'current, stream, run, flow, haste, hurry, vehemency', 
retas-n. ' downpour, stream, seed, sperm ', renu-m. "dust' (: Old Russian rent 
"sandbank'); to ^-suffix compare under Latin nvus, 

Maybe zero grade in alb. /r/(*/77/)"stay, stand'. 

Armenian ar/'get up, stand up!' (Persson Beitr. 769) To y-arnem, S. 327; 

gr. Lesbian oplvu), (*6pi:-viu)) "set in motion, excite, irritate to the rage '; spit;, -xboc, "fight, 
strife, quarrel, contention ' (perhaps in /to our root form, whether not better after Schwyzer 
Gl. 12, 17 to £p£i5u) " support, stem, bump, press, poke, push'); Arcadian spivusiv "be 
angry with' from 'EpTvu(; actually " the angry soul of the victim pursuing the murderer ' (??); 

alb. Geg /77e "humid, wet, damp', actually "* flowing ' {*rinete: Old Indie rinati, Slavic 
ringtl); 

Latin orior, ongosee above; nvus {*rei-uo-s) "stream, brook'; in Old Bulgarian rbvbn-b " 
rival ' corresponding meaning change rMnus and nva//s' rival in the love' (latter form 
reshuffling after aequalis, sodalis), actually " one who lives near a brook '; 

probably here irntare^ excite, exasperate, anger, provoke ', prorTtare^ to incite, entice, 
allure, tempt, provoke, cause, or produce by irritation ', (probably intensive to an *ir-n-re)\ 

Irish nan'sea' and (compare Old Indie nf/-) " kind, way ', gall. Renos {*reinos) "Rhein 
(large river)' (whether also after Stokes KZ. 37, 260 Irish n'asc'a marsh', nm "bad weather 
'??), cymr. rh/d/o " go or come together, to meet, assemble, collect together, go or come 
together in a hostile manner, to encounter ' (: Old English rid, Old Indie nt/-h), Old Irish 
n'athor, cymr. rhaiadr, a cymr. rea///'" waterfall' {*rlia-tro-)\ 

Old English rTdrc\. f., ndei. "stream, brook'. Old Saxon nthm. "burning hot, rushing, 
torrential ', Middle Low German r/dei. "stream, brook, watercourse'. Modern High German 
-reid(e)\v\ place names; Dimin. {*nt^uldn) ndd. /7//e "furrow after rainwater, gully'; further 
Old English a-/"^/77a/7 "raise, uplift, soar, rise'. Middle English rgmen, engl. roam^ wander', 
Old Icelandic reimudr^ wandering around ', reimir^ sv\ake\ ^ar er reimV there it is scary, 
haunts ', reima^ annoy, disturb, infest ' (meaning as Old Bulgarian /'^a//"bump, poke'). 
About rinnansee above. 

With Germanic s-extension: Gothic urre/san 'nse'; 



Old Icelandic rJsa, Old English Old Saxon nsanWse', Old High German nsan, Middle High 
German /75e/7 "ascend, fall'; Old High German re/'sa' departure, migration, campaign, 
journey', Gothic urraisjan^ make rise, uplift, set up, awake, animate'. Old Icelandic reisa 
ds.. Old English raeran^ raise, uplift, set up, erect'. Old High German reren' make fall, 
make pour down, pour '; 

Maybe alb. re 'cloud, rain', alb. Geg A^'fall', Aes/ye 'rainfall, downpour' : diminutive Middle 
High German riselvn. 'rain'. 

ndd. reren^ia\\\ Middle High German r/se/en^6np, rain'. Modern High German riesein. 
Middle High German riselxw. 'rain'. Old Icelandic blod-risa. Middle High German bluotvise^ 
blood-spattered ', Old Frisian blodrisne^ bleeding wound'; from 'fall' becomes ' dropped, 
fallen' in Old English (^e')/7S5/7 'befit'. Old High German garJsan^ approach, suit, fit ' 
(compare s-extension Old Bulgarian ristati). Middle High German risch^ spry, quick, fast ' 
(compare Old Bulgarian riskanije); 

Lithuanian ry-tas ' morning ' ('*sunrise', compare Gothic urreisan), Latvian rietu, -eju, -et 
" break out, rise (e.g., from the day), burst forth ', riete 'milk in the brisket ' (compare formal 
Old Indie reta-)\ 

Slavic *raja- m. 'current' (: above Old Indie raya-hrc\. 'stream, run, flow') in Old 
Bulgarian izrojb^ ejaculation of semen ', sb/io/i. 'confluence', naroj^x\^s\\\ /ry'swarm of 
bees' ( *roJo-s)\ in addition reka ( *roi-ka) 'river'; 

Maybe alb. re, /le "cloud' : Rumanian /r*/ "swarm, hive, cluster, cloud'; a loanword from 
Proto-Slavic form: rojb; See also: rejati; reka; ringti; Russian: /ry"swarm' [m jo]; Polish: roj 
"swarm' [m jo], /'cy^[Gens]; Serbo-Croatian: /Toy "swarm' [m jo]; Slovene: /'(9y"swarm' [m jo] 
Maybe alb. reja "cloud' from alb. rufeja "thunderbolt' < Bulgarian 

Also alb. /re/re "current' from Proto-Slavic form: reka See also: rejati; ringti; rojb; Old 
Church Slavic: reka "river' [f a]; Russian: reka "river' [f a]; Czech: reka "river' [f a]; Slovak: 
rieka "river' [f a]; Polish: rzeka "river' [f a]; Serbo-Croatian: rijeka "river' [f a]; Slovene: reka 
"river' [fa] 

Slavic */'(f/d"poke, push' in Old Church Slavic rejq, rejati^i\o\N' (New Slavic) and "bump, 
poke, urge, press, push' (as oplvw "budge'); in addition the changing by ablaut Old Church 
Slavic vyringti^ e^ooGsTv ', ringtisg^ to fall with violence, rush down, fall down, tumble down, 
go to ruin '; Old Russian rent "sandbank'; kir. nh "sand, river detritus, pebbles ' (compare 
Old Indie renu-); in other meaning (see above to Latin rfvTnus) Old Bulgarian rbvbn-b " rival ' 



rbven/je 'stnie, quarrel, debate, contention ', Czech fevnitr compete ', poln. rzewnic 
"move, stir, agitate'. 

Maybe in -s/ro formant alb. rrah {ra-sko) " quarrel' [common alb. -sk> -/?]. 

With 5-extension Balto Slavic *re/st/d\n Old Bulgarian r/stg, r/stat/^run', r/skan/je' to run, 
move quickly, hasten ', Lithuanian ra/stas {'run time' =) ' rutting ', Latvian r/'ests ds., 
Lithuanian /v's/as 'quick, fast', r/sc/a \ns\.r. Sg. ' in gallop '. 

e. basis ereu-\ er-nu-' contest ', or-t/o- 'hasty'. 

Old Indie //7o//(Perf. ara but Indo Germanic *dra), arnava-, Avestan aranu- see above S. 
327; 

Maybe alb. PN Rinas, lllyrian rinotR 

Old Indie arvan-, a/v5/7/- 'hurrying, rusher, racer', Avestan aurva-, aurvant- 'quick, fast, 
valiant'; perhaps Avestan auruna-'wM, cruel, savage, from animals'; very doubtful Old 
Indie ru-ra-' stormy, hot tempered, of fever'; 

Note: 

Old Indie arvan-, arvant- : Messapic FIN /l/"i/d prove lllyrian displayed satem character : 
gall.-brit. FIN *Arva, engl. Arrow, French Erve, Auve{*rua); Messapic FIN Arvo. 

gr. 6pv0-|ji, ou^oc, see above; previous causative opouu) ' overthrow me, outleap ', 
avopouu) ' jump up ' (probably as *opou[a]u) zur 5-extension, see below); compare 
Schwyzer Gr. Gr. I 683; 

Latin rud, -ere'ruu, hurry, storm along'; 

Middle Irish rOathar{*reu-tro-) 'onrush', cymr. rhuthrds.. Old Irish ru{a)e' hero, demigod 
' ( *reu-io-); here gall.-brit. FIN *Arva, engl. Arrow, French Erve, Auve {*rua); Messapic FIN 
Arvo; 

Old Saxon aru. Old English earu' swift, ready, quick ', Old Icelandic p/r'rash, hasty, 
generous, ( *arwa- = Avestan aurva-; here as originally ' generous ' perhaps also Gothic 
arwjo' gratuitous, free ', Old English earwunga. Old High German ar(a)wun' free, for 
nothing, in deception, in error ', arod' forceful, agile'; Old High German ernusts. S. 328. 



Old English /■eon/ "agitated, stormy, wild, rough', Gothic unmana-riggws^\NM, cruel, 
savage'. 

extension reus-: 

Old Indie rosati, rusat/"\s sullen', rusita-, rusta-^ irritated '; 

Swedish /x7ss 'storm from there, hurry'. Middle Low German mse/7"dash, rage, clamor, 
rant, roister', rusch^ intoxication ', Old Icelandic rosi^ Sturmbo ', raust\o\ce', Old Swedish 
ruska'storm ahead, hurry'; 

[but Gothic rausn., with gramm. variation Old Icelandic reyrrm., Old High German ror' 
reed ', rorea "duct, tube, pipe' {*rauzidn), with stem stress (as Gothic) Swedish rysja. Old 
High German russa, rusa, riusai. 'baskey for catching fish, snare, trap', other formations 
with /r-suffix Old English rysci.. Middle High German rusch{e) f. ' bulrush', probably remain 
far off]; 

Lithuanian ruosus' diligent, active ', Latvian ruoss ds., Lithuanian ruosiu, ruosiau, rudsti 
' provide ', reflex. ' take care '; 

Slavic *ruchh'\n russ. /z/c/7 "restlessness, movement', ruchnu ft 'turr\b\e, fall', poln. 
Czech Ai/c/? 'movement', ablaut, cech. rychfy' quick, fast ', in addition causative Slavic 
*rusiti^ overturn, upset ' in Old Church Slavic razdrus/t/" destroy' , russ. rus/fb ds., etc. 

Maybe alb. Geg zcfroj, Tosc /rezo/T/'tumble, fall' : Old Church Slavic razdrus/t/" destroy' . 

References: WP. I 136 ff., Schwyzer Gr. Gr. I 516 b, 694, 702, 719, 740, 749, Trautmann 
240 f., 242, 243, 246, WH. I 64 f., 416 f., 719, II 222 f. 
Page(s): 326-332 

Root / lemma: er-4{er-t- er-u^ [*herg''h^ 

Meaning: Earth 

Note: 

Root/ lemma: er-4{er-t-, er-u^ [*herg''h^ earth' derived from Root/ lemma: er-3. or-, r- 

: to move *stir, animate, fight, struggle, rise; to spring up, be born' 

Material: Gr. spa 'earth', spa-^s 'to earth' (perhaps therefrom spau), see below S. 336; with 
common extension of probably noAur|po(; noAuapoupo(;, nAouaiO(; Hes.); svspoi, see 
above S. 312; zpzo\-[}tipr\ ysajpETpiav Hes.; 

Germanic *erf^d\n Gothic a/rf^a, Old Norse yiprd. Old High German (etc.) erda 'eartW; 



Maybe TN lllyhan Ardiaei {* er-g"'he) [common lllyhan-alb. -gh->d\ 

Germanic *erd\(\ Old High German e/r* "earth'; 

£/o-extension in Old Hoxsq jgrvi {*erwan^ "sand, sandbank', and cymr. erw\. "field', PI. 
erwi, erwydd, corn, erw, ereu6s., abret. Middle Breton eru, nbret. ero "furrow' {*erui-)\ 

Note: 

Those cognates derived from Old Indie arvan-, arvant-: Messapic FIN /I/'ko prove lllyrian 
displayed satem character; there is proof lllyrian belonged to the Celtic family gall.-brit. FIN 
*Arva, engl. Arrow, French Erve, Auve {*rua)\ Messapic FIN Arvo. [see above] 

perhaps Armenian erkir^ earVc\' (Pedersen KZ. 38, 197), if for*^/^- (Indo Germanic *eru-) 
after erkin "sky, heaven'. 

References: WP. I 142, Finzenhagen Terminol. 6, Schwyzer Gr. Gr. I 424. 
Page(s): 332 

Root / lemma: er-5, era-, thematic (e)r-e-
```


## [2026-09-05T20:29:53.185Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AHD er-1 ===\" && grep -n \"^er-1\\|^er-2\\|er-1\\.\" AHD_watkins1985.txt | head -20 && echo \"=== AHD grep rinw ===\" && grep -n \"ri-nw\\|rinw\" AHD_watkins1985.txt | head && echo \"=== AHD reia ===\" && grep -n \"^rei\\|reia-\\|rivus\" AHD_watkins1985.txt | head -20",
 "description": "Grep AHD Watkins"
}
```


### [2026-09-05T20:29:53.254Z] TOOL RESULT

```
=== AHD er-1 ===
333:bher-1. To carry; also to bear children. 1. a. Germanic *beran in (i) Old English beran, to carry: BEAR! (ii) Old English forberan, to bear, endure (for-, for-; see per’): FORBEAR; b. Germanic *bérd in Old English bér, ber, bier: BIER; c. Germanic *bér- in Old Norse bdra, wave, billow: BORE’. 2. a. Germanic *barnam in Old English bearn, child: BAIRN; b. Germanic *barwdn- in Old Eng- lish bearwe, basket, wheelbarrow: BARROW!, 3. a. Ger- manic *burthinja in Old English byrthen, burden: BURDEN}; b. Germanic *burthiz in Old Norse burdhr, birth, akin to the source of BIRTH; C. Germanic *burja- perhaps in Old Norse byrr, favorable wind: BIRR}. 4. Compound root *bhrenk-, to bring (< *bher- + *enk-, to reach; see nek-2), in Germanic *brengan in Old English bringan, to bring: BRING. 5. Latin ferre, to carry: -FER, FERTILE; AFFERENT, CONFER, DEFER!, DEFER®, DIFFER, EFFERENT, INFER, OFFER, PREFER, PROFFER, REFER, SUFFER, TRANSFER, VOCIFERATE. 6. Latin pro- brum, a reproach (< “pro-bhr-o-, “something brought before one”; pro-, before; see per'): OPPROBRIUM. 7. Lengthened o-grade form *bhor- probably in Latin far, thief: FERRET!, FURTIVE, FURUNCLE; (FURUNCULOSIS). 8. Greek pherein, to carry: -PHORE, -PHORESIS, -PHO- ROUS; AMPHORA, ANAPHORA, DIAPHORESIS, EUPHORIA, METAPHOR, PERIPHERY, PHEROMONE, TELPHER, TOCOPH- EROL. 9. Greek pherné, dowry (“something brought by a bride”): PARAPHERNALIA. [Pok. 1. bher- 128.]
377:dapper, heavy, strong; later quick, nimble: DAPPER. [Pok. dheb- 239.] dhegvh-. To burn, warm. Suffixed o-grade form *dhogvh- eye- in Latin fovére, to warm, cherish, foment (> fomen- tare, to foment, and fomes, tinder): FOMENT, FOMITE. [Pok. dhegth- 240.] dh@(i)-. To suck. Contracted from *dheoa(i)-. 1. Suffixed reduced form *dhé-mnd- in Latin fémina, woman (< “she who suckles”): FEMALE, FEMININE; EFFEMINATE. 2. Suf- fixed reduced form *dhé-to- in Latin fétus, pregnancy, childbearing, offspring: FAWN, (FETAL), FETUS; EFFETE, (FETICIDE), SUPERFETATE. 3. Suffixed reduced form *dhé-kundo- in Latin fécundus, fruitful: FECUND. 4. Suf- fixed reduced form *dhé-no- in Latin fénum, faenum, hay ( < “produce”): FENNEL, FINOCHIO; (FENUGREEK), SAIN- FOIN. 5. Perhaps suffixed zero-grade form *dhi-lyo- (< *dhia-lyo-) in Latin filius, son, and filia, daughter (but these are equally possibly from the root bheue-): FILIAL, FILIATE; AFFILIATE, HIDALGO. 6. Suffixed reduced form *dhé-lo- in Latin fél(are, to suck: FELLATIO. 7. Suffixed reduced form *dhé-l-ik- in Latin félix, fruitful, fertile, lucky, happy: FELICITATE, FELICITY; FELICIFIC, INFELIC- Ty. 8. Suffixed reduced form *dhé-ld- in Greek thélé, nipple: ENDOTHELIUM, EPITHELIUM, (MESOTHELIUM). 9. Suffixed reduced form *dhé-l-u- in Greek thélus, female: THEELIN. [Pok. dhéi)- 241.] dheia-. To see, look. Variant form *dhyd- (< *dhyag-) in: a. suffixed form *dhyd-mn in Greek sémeion and séma (stem sémat-), sign: SEMANTIC, SEMATIC; SEMAPHORE, SEMASIOLOGY, SEMEME, SEMIOLOGY, SEMIOTIC; b, San- skrit dhydti, he meditates (< “he observes mentally”): ZEN BUDDHISM. [Pok. dheis- 243.] dheigh-. To form, build. 1. Germanic *daigjén in Old English d%ge, bread kneader: DAIRY. 2. Germanic *-dig- in Old English compound Aléfdige, mistress of a house- hold (< “bread kneader”; Al#f, bread, loaf): LADY. 3. Ex- tended o-grade form *dhoigho- in Germanic *daigaz in: a. Old English dag, dough: pouGH; b. Old High German teic, dough: TEIGLACH. 4. Suffixed zero-grade form *dhigh-ird, in Latin figira, form, shape (< “result of kneading”): FIGURE; CONFIGURATION, DISFIGURE, PRE- FIGURE, TRANSFIGURE. 5. Nasalized zero-grade form *dhi-n-gh- in Latin fingere, to shape: (FAINT), FEIGN, (FEINT), FICTILE, FICTION, FIGMENT; EFFIGY. 6. Nasal- ized zero-grade form *dhi-n-g(h)- in Greek thinganein, to touch: THIGMOTAXIS, THIXOTROPY. 7. Suffixed o-grade form *dhoigh-o- in Avestan daéza-, wall (originally made of clay or mud bricks): PARADISE. [Pok. dheigh- 244.] dhel-. A hollow. 1. Germanic *daljé in Old English dell, valley: DELL. 2. Germanic *dalam in Old English del, valley: DALE. 3. Germanic *del- in Old Norse dzla, wooden gutter on a ship: DALLES. [Pok. 1. dhel- 245.] dhelbh-. To dig, excavate. Germanic *de/ban in Old English de/fan, to dig: DELVE. [Pok. dhelbh- 246.] dhembh-. To bury. Suffixed zero-grade form *dhmbh-o- in Greek taphos (< *thaphos), tomb: CENOTAPH, EPI- TAPH. [Pok. (dhembh-), dhmbh- 248.] dhen-'. To run, flow. Suffixed o-grade form *dhon-ti- in Latin fons (stem font-), spring, fountain: FONT!, FOUN- TaIN. [Pok. 1. dhen- 249.] dhen-2. Palm of the hand. Suffixed form *dhen-r in Greek thenar, palm of the hand: THENAR. [Pok. 2. dhen- 249.] dher-1. To make muddy; darkness. 1. Suffixed form *dher-g- in Germanic *derk- in Old English deorc, dark: DARK. 2. Suffixed zero-grade form *dhr-egh- in: a. Ger- manic ‘suffixed form *drah-sta- in Old English drés, dregs: pross; b. Germanic *dragj6 in Old Norse dregg, dregs: DREGS. 3. Suffixed extended zero-grade form *dhro-bh- in Germanic *drab- in: a. Old English dreflian, to drivel: DRIVEL; b. probably Low German drabbelen, to paddle in water or mire, draggle, akin to the Low German source of Middle English drabelen, to draggle: DRABBLE; C. Middle Irish drab, dregs, probably akin to the Celtic source of DRAB2. 4. Suffixed extended
447:er-1, To move, set in motion. 1. Probably Germanic *ar-, *or-, *art(a), to be, exist, in Old English eart and aron, second person singular and plural present of béon, to be:
451:er-2, Earth, ground. Extended form “*erf- in Germanic *erthé in: a. Old English eorthe, earth: EARTH; b. Middle Dutch aerde, eerde, earth (> Afrikaans aarde): AARD- VARK, AARDWOLF. [Pok. 4. er- 332.]
618:ker-1. Horn, head; with derivatives referring to horned animals, horn-shaped objects, and projecting parts. I. Zero-grade form *kr-. 1. Suffixed form *kr-n- in: a. Ger- manic *Aurnaz in (i) Old English horn, horn: HORN, (HORNBEAM) (ii) German Horn, horn: ALPENHORN, ALT- HORN, FLUGELHORN, HORNBLENDE; Db. Latin cornd, horn: CORN2, CORNEA, CORNEOUS, CORNER, CORNET, CORNICULATE, CORNU; BICORN, CADUCICORN, CAPRI- CORN, CLAVICORN, CORNIFICATION, LAMELLICORN, LON- GICORN, TRICORN, UNICORN. 2. Suffixed and extended form *krs-n- in Germanic *hurznuta in Old English hyrnet, hornet: HORNET. 3. Suffixed form *kr-ei- in: a. Germanic *hraina- in Old Norse hreinn, reindeer: REINDEER; b. Germanic *hrinda- in Old High German hrind, ox (> German Rinder, cattle): RINDERPEST. 4. Suffixed extended form *kros-no- in Greek kranion, skull, upper part of the head: CRANIUM; MIGRAINE, OLECRANON. 5. Suffixed form *kr-a- in: a. Greek karé, kara, head: CHARIVARI; CHEER; b. Greek karoun, to stupefy, be stupefied (< “to feel heavy-headed”): ca- ROTID; c. Greek kardton, carrot (from its hornlike shape): CARROT. 6. Possibly extended form *kri- in Greek krios, ram: CRIOSPHINX. II. Suffixed form *ker-wo-. 1. Latin cervus, deer: CERVINE, SERVAL. 2. Latin cervix, neck: CERVIX. III. Extended and suffixed form *keru-do- in Germanic *herutaz in: a. Old English heorot, hart, stag: HART; b. Dutch hart, deer, hart: HARTEBEEST. IV. Extended form *keras-. 1. Greek keras, horn: CARAT, CERASTES, KERATO-; CERATODUS, (CERATOID), CHELIC- ERA, CLADOCERAN, KERATIN, RHINOCEROS, TRICERA- Tops. 2. Persian sar, head: SIRDAR. 3. Suffixed form *keras-ro- in Latin cerebrum, brain: CEREBELLUM, CERE- BRUM, SAVELOY. V. Extended o-grade form *koru-. 1. Greek Rorumbos, uppermost point (< “head”): CoR- yMB. 2. Greek koruphé, head: CORYPHAEUS. 3. Suffixed form *koru-do- in Greek korudos, crested lark: coRY- DALIS. 4. Suffixed form *koru-ndé in Greek koruné, club, mace: CORYNEBACTERIUM. [Pok. 1. ker- 574.]
947:skribh-. To cut, separate, sift. Extension of sker-1. 1. Latin scribere, to scratch, incise, write: SCRIBBLE, SCRIBE, SCRIPT, SCRIPTORIUM, SCRIPTURE, SERIF, SHRIVE; ASCRIBE, CIRCUMSCRIBE, CONSCRIPT, DESCRIBE, INSCRIBE, MANUSCRIPT, POSTSCRIPT, PRESCRIBE, PRO- SCRIBE, RESCRIPT, SUBSCRIBE, SUPERSCRIBE, TRAN- SCRIBE. 2. Greek skariphos, scratching, sketch, pencil: SCARIFY}, [Pok. 4. sker-, Section II. 945.]
1023:(s)ter-n-. Name of thorny plants. Extension of ster-1. Suffixed zero-grade form *tr-n-u- in Germanic *thurnu-, thorn, in Old English thorn, thorn: THORN. [Pok. 7. (s)ter-n- 1031.]
=== AHD grep rinw ===
895:ryfe, abundant: RIFE. 3. Suffixed form *reip-d- in Latin ripa, bank (< “that which is cut out by a river”): RIPARIAN, RIVAGE, RIVER; ARRIVE. IV. Extended form *reib- in Germanic *rip-. 1. Germanic *ripja- in Old English ripe, ripe, ready for reaping: RIPE. 2. Germanic *ripan in Old English ripan, to reap: REAP. 3. Middle Low German repelen, to remove seeds, akin to the source of Middle English ripelen, to remove seeds: RIPPLE? [Pok. 1. rei- 857.] rei-2. Striped in various colors, flecked. Suffixed o-grade form *roi-ko- in Germanic *raihaz in Old English rd, raha, deer: ROE*. [Pok. 2. rei- 859.] rei-3, To flow, run. 1. Suffixed zero-grade form *7i-nu- in: a. Germanic *ri-nw-an, whence *rinnan, to run, in Old English rinnan, to run, and Old Norse rinna, to run: RUN, RUNNEL; b. secondary Germanic derivative *runiz in Old English ryne, a running: EMBER DAY. 2. Suffixed zero-grade form *ri-l- in Germanic *ril- in Dutch ril and Low German rille, running stream: RILL. 3. Suffixed form *rei-wo- in Latin rivus, stream: RIVAL, RIVULET; DERIVE. [Pok. 3. er- 326.] reidh-. To ride. I. Basic form *reidh-. 1. Germanic *ridan in: a. Old English ridan, to ride: RIDE; b. Middle Dutch riden, to ride (> ridder, rider, knight): RITTER. 2. Celtic *vo-réd- in Latin verédus, post horse (*vo-, under; see upo): PALFREY. II. O-grade form *roidh-. 1. Germanic *raid- in: a. Old English rdd, a riding, road: RAID, ROAD; b. possibly Middle High German reidel, rod between upright stakes (< “wooden horse”): RADDLE!. 2. Prob- ably Germanic *raid-ja- in Old English réde, geréde, ready (< “prepared for a journey’): READY. 3. Germanic *raidjan in Vulgar Latin *arrédare, to arrange: ARRAY. [Pok. reidh- 861.] reig-'. To bind. 1. Germanic *rigg- (the -gg- is anoma- lous) in Norwegian rigga, to bind, akin to the Scandina- vian source of Middle English riggen, to rig: RIG. 2. Zero-grade form *rig- in Latin corrigia (probably borrowed from Gaulish), thong, shoelace (cor-, from com-, together; see kom): SCOURGE. [Pok. reig- 861.] reig-2. To reach, stretch out. 1. O-grade form “roig- in Germanic *raikjan in Old English récan, to stretch out, reach: REACH. 2. Possibly suffixed (stative) zero-grade form “rig-é- in Latin rigére, to be stiff (? < “be stretched out”): RIGID, RIGOR. [Pok. (reig-) 862.] rendh-. To tear up. 1. Germanic *randjan in Old English rendan, to tear: REND. 2. Germanic *rind- in Old English rinde), rind (< “thing torn off”): RIND. [Pok. rendh- 865.] rep-. To snatch. Suffixed zero-grade form *rap-yo- in Latin rapere, to seize: RAPACIOUS, RAPE!, RAPID, RAPT, RAVEN?, RAVIN, RAVISH; EREPSIN, SURREPTITIOUS. [Pok. rep- 865.] rép-'. To creep, slink. Latin répere, to creep: REPENT?, REPTILE; SUBREPTION. [Pok. 1. rép- 865.] rép-2, Stake, beam. Suffixed variant form *rap-tro- in Germanic *raf-tra- in: a. Old English refter, rafter: RAFTER; b. Old Norse raptr, beam: RAFT!. [Pok. 2. rép- 866.] ret-. To run, roll. 1. Prefixed form *to-vo-ret-, “a running up to” (to-, to; vo, under, up, up from under; see upo), in Old Irish toir, pursuit: Tory. 2. Suffixed o-grade form *rot-d- in Latin rota, wheel: RODEO, ROLL, ROTA, RO- TARY, ROTATE, ROTUND, (ROTUNDA), ROULETTE, ROUND!, ROWEL; BAROUCHE, CONTROL, PRUNE?, ROTIFORM, ROTO- GRAVURE. [Pok. ret(h)- 866.] rét-. Post. O-grade form *rdt- in Germanic *réd- in Old English réd, rod, cross: ROOD. [Pok. rét+ 866.] reu-'. To bellow. 1. Extended form *reud- in Germanic *rauton in Old Norse rauta, to roar (akin to the Scandi- navian source of ROTE?): ROUT’. 2. Suffixed extended form *reum-os- in Latin riimor, rumor, “common talk”: RUMOR. 3. Extended form *reug- in Latin rigire, to roar: RIOT, RUT’. 4. Variant *rau-ko- in Latin raucus, hoarse: RAUCOUS. [Pok. 1. reu- 867.]
=== AHD reia ===
839:parative) form *pro-tero- in Greek proteros, before, former: HYSTERON PROTERON, PROTEROZOIC. VI. Exten- ded forms *prai-, *prei-. 1. Latin prae, before: PRE-; PRETERIT. 2. Suffixed (comparative) form *prei-yos- in Latin prior, former, higher, superior: PRIOR2. 3. Suffixed form *prei-wo- in: a. Latin privus, single, alone (< “standing in front,” “isolated from others”): PRIVATE, PRIVILEGE, PRIVITY, PRIVY; DEPRIVE; b. Latin proprius, one’s own, particular (< pré priv6, in particular, from the ablative of privus, single): PROPER, PROPERTY; APPRO- PRIATE, PROPRIOCEPTION, PROPRIOCEPTOR. 4. Extended form *preis- in: a. suffixed (superlative) form *preis-mo in (i) Latin primus (< *prismus; ablative plural primis), first, foremost: PREMIER, PRIMAL, PRIMARY, PRIMATE, PRIME, PRIMITIVE, PRIMO, PRIMUS; IMPRIMIS, PRIMA FACIE, PRIMAVERA, PRIMEVAL, PRIMIPARA, PRIMOGENI- TOR, PRIMOGENITURE, PRIMORDIAL (ii) Latin compound princeps, “he who takes first place” (-ceps, “-taker”; see kap-), leader, chief, emperor: PRINCE, PRINCIPAL, PRIN- CIPLE; b. suffixed form *preis-tano- in Latin pristinus, former, earlier, original: PRISTINE. VII. Extended form *pres- in compound “*pres-g“u-, “going before” (*gvu-, to go; see gWa-), in Greek presbus, old, old man, elder: PRESBYTER, (PRIEST); PRESBYOPIA. VIII. Extended form *proti in Greek pros, against, toward, near, at: PROS-; PROSOPOPEIA. Other possibly related forms are grouped under per-2, per-3, per-4, per-5, and per-’. [Pok. 2. A. per 810.] per-?. To lead, pass over. A verbal root belonging to the group of per’. I. Full-grade form *per-. 1. Suffixed form *per-tu-s in Germanic “*ferthuz, place for crossing over, ford, in Old Norse fjérdhr, an inlet, estuary: FIRTH, FJORD. 2. Suffixed form *per-ond in Greek peroné, pin of a brooch, buckle (< “that which pierces through”): PERONEAL. II. O-grade form *por-. 1. Germanic *faran, to go, in: a. Old English faran (> Middle English faren), to go on a journey, get along: FARE; WAYFARER, WAY- FARING, (WELFARE); b. Old High German faran, to go, travel: GABERDINE. 2. Suffixed form *por-o-, passage, journey, in Greek poros, journey, passage: PORE”; EMPO- RIUM, POROMERIC. 3. Suffixed (causative) form *por- eyo-, to cause to go, lead, conduct, in Germanic *farjan, to ferry, in Old English ferian, to transport: FERRY. 4. Lengthened-grade form *pdér- in: a. Germanic suffixed form *f6r-ja- in Old English (ge)féra, “fellow-traveler,” companion (ge-, together, with; see kom): FERE; b. Ger- manic suffixed (causative) form *fér-jan in Old High German fuoren, to lead: FUHRER. 5. Possibly suffixed form *por-no-, feather, wing (< “that which carries a bird in flight”), in: a. Germanic *farnd, feather, leaf, in Old English fearn, fern (having feathery fronds): FERN; b. Sanskrit parnam, leaf, feather: PAN2. III. Zero-grade form pr-. 1. Suffixed form *pr-tu-, passage, in: a. Ger- manic *furdu- in Old English ford, shallow place where one may cross a river: FORD; b. Latin portus, harbor (< “passage”): PORT!; IMPORTUNE, OPPORTUNE. 2. Suffixed form *pr-té in Latin porta, gate (> Old French porte, door): PORCH, PORT’, PORTAL, PORTCULLIS, PORTE-CO- CHERE, PORTER®, PORTICO, PORTIERE, PORTULACA. 3. Suffixed (denominative) form *pr-to- in Latin portdre, to carry: PORTS, PORTABLE, PORTAGE, PORTAMENTO, PORTATIVE, PORTER}; COMPORT, DEPORT, EXPORT, IM- PORT, (IMPORTANT), PORTFOLIO, PURPORT, RAPPORT, REPORT, (SPORT), SUPPORT, TRANSPORT. [Pok. 2. B. per 816.]
895:ryfe, abundant: RIFE. 3. Suffixed form *reip-d- in Latin ripa, bank (< “that which is cut out by a river”): RIPARIAN, RIVAGE, RIVER; ARRIVE. IV. Extended form *reib- in Germanic *rip-. 1. Germanic *ripja- in Old English ripe, ripe, ready for reaping: RIPE. 2. Germanic *ripan in Old English ripan, to reap: REAP. 3. Middle Low German repelen, to remove seeds, akin to the source of Middle English ripelen, to remove seeds: RIPPLE? [Pok. 1. rei- 857.] rei-2. Striped in various colors, flecked. Suffixed o-grade form *roi-ko- in Germanic *raihaz in Old English rd, raha, deer: ROE*. [Pok. 2. rei- 859.] rei-3, To flow, run. 1. Suffixed zero-grade form *7i-nu- in: a. Germanic *ri-nw-an, whence *rinnan, to run, in Old English rinnan, to run, and Old Norse rinna, to run: RUN, RUNNEL; b. secondary Germanic derivative *runiz in Old English ryne, a running: EMBER DAY. 2. Suffixed zero-grade form *ri-l- in Germanic *ril- in Dutch ril and Low German rille, running stream: RILL. 3. Suffixed form *rei-wo- in Latin rivus, stream: RIVAL, RIVULET; DERIVE. [Pok. 3. er- 326.] reidh-. To ride. I. Basic form *reidh-. 1. Germanic *ridan in: a. Old English ridan, to ride: RIDE; b. Middle Dutch riden, to ride (> ridder, rider, knight): RITTER. 2. Celtic *vo-réd- in Latin verédus, post horse (*vo-, under; see upo): PALFREY. II. O-grade form *roidh-. 1. Germanic *raid- in: a. Old English rdd, a riding, road: RAID, ROAD; b. possibly Middle High German reidel, rod between upright stakes (< “wooden horse”): RADDLE!. 2. Prob- ably Germanic *raid-ja- in Old English réde, geréde, ready (< “prepared for a journey’): READY. 3. Germanic *raidjan in Vulgar Latin *arrédare, to arrange: ARRAY. [Pok. reidh- 861.] reig-'. To bind. 1. Germanic *rigg- (the -gg- is anoma- lous) in Norwegian rigga, to bind, akin to the Scandina- vian source of Middle English riggen, to rig: RIG. 2. Zero-grade form *rig- in Latin corrigia (probably borrowed from Gaulish), thong, shoelace (cor-, from com-, together; see kom): SCOURGE. [Pok. reig- 861.] reig-2. To reach, stretch out. 1. O-grade form “roig- in Germanic *raikjan in Old English récan, to stretch out, reach: REACH. 2. Possibly suffixed (stative) zero-grade form “rig-é- in Latin rigére, to be stiff (? < “be stretched out”): RIGID, RIGOR. [Pok. (reig-) 862.] rendh-. To tear up. 1. Germanic *randjan in Old English rendan, to tear: REND. 2. Germanic *rind- in Old English rinde), rind (< “thing torn off”): RIND. [Pok. rendh- 865.] rep-. To snatch. Suffixed zero-grade form *rap-yo- in Latin rapere, to seize: RAPACIOUS, RAPE!, RAPID, RAPT, RAVEN?, RAVIN, RAVISH; EREPSIN, SURREPTITIOUS. [Pok. rep- 865.] rép-'. To creep, slink. Latin répere, to creep: REPENT?, REPTILE; SUBREPTION. [Pok. 1. rép- 865.] rép-2, Stake, beam. Suffixed variant form *rap-tro- in Germanic *raf-tra- in: a. Old English refter, rafter: RAFTER; b. Old Norse raptr, beam: RAFT!. [Pok. 2. rép- 866.] ret-. To run, roll. 1. Prefixed form *to-vo-ret-, “a running up to” (to-, to; vo, under, up, up from under; see upo), in Old Irish toir, pursuit: Tory. 2. Suffixed o-grade form *rot-d- in Latin rota, wheel: RODEO, ROLL, ROTA, RO- TARY, ROTATE, ROTUND, (ROTUNDA), ROULETTE, ROUND!, ROWEL; BAROUCHE, CONTROL, PRUNE?, ROTIFORM, ROTO- GRAVURE. [Pok. ret(h)- 866.] rét-. Post. O-grade form *rdt- in Germanic *réd- in Old English réd, rod, cross: ROOD. [Pok. rét+ 866.] reu-'. To bellow. 1. Extended form *reud- in Germanic *rauton in Old Norse rauta, to roar (akin to the Scandi- navian source of ROTE?): ROUT’. 2. Suffixed extended form *reum-os- in Latin riimor, rumor, “common talk”: RUMOR. 3. Extended form *reug- in Latin rigire, to roar: RIOT, RUT’. 4. Variant *rau-ko- in Latin raucus, hoarse: RAUCOUS. [Pok. 1. reu- 867.]
```


## [2026-09-05T20:29:53.948Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT aurva ===\" && grep -n \"aurva\\|auruna\\|auruua\" BRT.txt | head -30",
 "description": "Grep Bartholomae for aurva"
}
```


### [2026-09-05T20:29:54.003Z] TOOL RESULT

```
=== BRT aurva ===
2461:—  ahmi  atskvö  yat  astvainti  V,  5.  Sprecher  vorgeschwebt:  jaji-a..  7rfJ»aVfl/ 39;  —  ai^hS  zimo  yat  faianaya  Yt  w.  poHbm  hl  matw  .  .  nöit  zT  ahmi  paiti 95;  — ■  anhqm  dämanqm  yat  ahurake  .  ..nairi  .  .  V.  7.51  f.;  _j.zi;  —  ^aei  iskata dätarasca  ,  .  Yl  ig.^Si  —  ar>zahiby5  sa- '  .*aoi  spita.gaona  gairi  aat  äkva  paurva- vahUyB  .,  aheca  iarsvanf  yat  :i^anira-)tähva..\.lo.ii{.; — *unäAva..raBsayaca  aal '^ahe  Vr.  70. 1 ;  — yat  ahmi  nmSm  yal^  ähva'  iyar»^ähva' {^'^  V.iy.zi.;  —  vasö »»äaÄy(MHÄ/(Stverz.)  "wenn  hier  im  Hause '/fljc'äö'fl  mazdayasna  aits  pa'^h  frayqn  . . eines  M.  .  ."  V. 5. 4 5 ;  usw. ;  — ■  aitihä  dae-  ahe  nmänahe  myasd»m  dai'^yärys  V.  S.xz; naya yat  ähuröHY .60.1;  Yt  jj.gg;  Y.  Ä  7  ■  10;  —  asfmacrjS  ,  .  yS  altahmi  aahvS  .. {•MO  yä  ahairU).  b)  substantivisch,  am  faitiMiuaiti  a  dim  näii  apivatäite  . .  para gAw.,  von  dem,  der  so  bekannt  ist,  dass  ns  ahmai^  atat?halca  soi'iraatca  ..\.g. ein  'er"  genügt,  ihn  zu  bezeichnen  ('Er'J,|52f,;  — yasca  ..  imat  ..  i<acS  fravaoc^ von  AaraMainyav :  yl  ml  nä  manxiaiti\ .  .  nsit  dim  yava  aii'ihe  ayqn  nöit  airika anyä>ä  (sd.)  ahmjt  Y.5/.10.  II)  iu'.xsafS  ..  Yt.ii.^t^^,  —  y/üse  mq>rahe schwachdeiktischemSinn 'dieser,  der,  er":  a^,;  ar  «ä  *sravat?hs . .  N.22;  —  vispim 1)  auf  Vorhergenanntes,  Vorausgehendes:,,  aya  ratu/rita  (näml.  Y.55.1— 5;  LS. (Wort  oderSatz)  zurückweisend;  i)  auf|  als  Instr.)  hvävayanh>m  .  .  paiti.barähi ein  Substantiv  oder  subsL  Pronomen;  a)  ad- ;  Y.  55.4.  o)  Das  adjekL  Pron.  steht,  wo jektivisch:  spinti  mainyü  .  .  ahyl'  *main-'AKi  Römer  die  Gen.  von  is  brauchte  (s. yius..ahm3t*mainyiusM.4y.i—^;  —  vaa-\  I  aaa,  23  aa):  aSe  mazdayasna  ..  atarj- hius  ivistl  manatshö  .  .  ahyä  vaahiul  tqm  aSoAmiti  naire  frabäraytn  .  .  yai manaahd  Y.  34-  9  f. ;  —  alnaahqm  . .  aisqm  ,  also  nä  . .  haca  aiibyö  nm3nalibyS  xsnütö alnaahqtn\.^2.it.;  —  tä ..  mainyü  {ai).)\.  .  pärayät  ",.  ex  eorutn  domis  . ."  V,^. ,,  ayä  *mainivä  ..  ayä  Y._J0.4— 6;  —  Äa-\  39;  —  yat  baväni  aiwi.vanyä  tq'irya- zaignm  yaexäinqm  .  .  balaar»  döi^ranqm  \  vant^m  . .  ahmt  gal^e  piianlhu  "dass  ich .  .    aal  äbyS  dei'iräbyB    ai-uiyasca    (DPf.)  [  Sieger  werde  über  den   7:  .  .  im  Kampf
2475:—  dr3gvä..ahya  fyao^anäis  akut  *3  fyqs  a^a^ara(sd.)  aya'^^  ra/u/risN.54;  — _>■« manatfhö  Y.47.5;  —  y^  •■  ^^yi^  zaohng  .tanup^rt^ah^  apa.rao^tmnaAe  (sd)  *a)a- usus  vann^ng {sd.)  Aa/aiteY.4S.4; — yimö\yaurva  *aya'^^'^'>  ralv/ris  Vi. $4.  b)  Das ..  yal  kirgnaot  airihe  x/a'iritoa  .,  Y.^.  4;  j  (subst)  Pron.  dem.  steht  an  Stelle  des  rel.
2497:b)  substantivisch:  *ydhä  *i}is'^^ iiä  varsiaiis  yä  dälä  atihius  paouruyehyä ralüs  ^■ao^anä  razUtä  (sd.)  "velut  (est) secundum  eas  (leges)  . .  quae  (sunt)  leges vitae  prioris"  Y.  33. 1 ;  —  Aaemö  aiibis (ab  Dat)  yöi  aurvantö  Atta  taxüsti
2550:äJffj  ti  'take  paiti  ..  V.22.2f.;  —  Da.'  aoAvo  (Stvetx.)  yal  as/tainti  Y.i^.6  \isw.; in  Verbindung  mit  anya-  Du.  (s.  i  b):  —  'tagsam  sünam  ..yimpasuiJiaurvamca.. asUm^mastrrfttqm  vispacayö*>nastr?inqm  i  V./^J.S;  —  'farahqm  urvaranqm  yat  ätri.- amqsta  fsd.)  ''i^arö.cikaya  *°le  anye  cika- ■  ciirranqm  V,4',75;  —  'ttm  ratümca  .. yatö  "wenn  einer  ,  .  und  wenn  einer  ,  .  \yim  maiaydhanmaim  A.j.3(?).  b)  sub- vcrletzt,  so  sollen  sie  dies  und  jenes  . ."  stasA\v\&c\\- 'ta(^T>.)äb3r3ta*sraosiivariza F,_jc  b)  adjektivisch:  j'iT/fl/ire'a/ara.-  vicarayaDm  "die  beiden,  der  .^.  und  der iri^yeiti  kva  "tarn  xsapan»m  . .  *vanAaiti  Sr.  .  ."  N.  jcf ;  —  cval  'te  (ADn.)  stai- "wenn  ein  Gläubiger  stirbt,  wo  weilt  asi\tiüa  bar>iis^a  ..  nasus  .,  fräsnaoiti dem  Tä^  (des  Todes)  . ."  H.  2.  i;  — yö  "..  die  beiden,  das  Bett  und  das  Polster .." . .  upairi  kunanm  (sdL)  manö  baräi  i-up^m  V.  7.9;  — ■  azim  °ta  (APn.)  zaota  zlsJi  (sd.) 'tfm  paiti  zmämm  aUariin  uri'a  kllayäi  ..  /rasrao^r?mca  /ragl>r>mca  . .  Vr._j.7; (sd.)  "wenn  einer  . .,  so  . .  während  der  —  't^m  nitamim  As'>rjm  '^rivacahim  (sd.) ganzen  Zelt  (seiner  Cberhebung)  .  ."P.  "id  minimum  Aj^/um:  triverbe"  F.  27b; J7.  a)  wo    wir   'solch'   brauchen:  yö  —  haomü  kutö  .  .  ava    'te  ahuta  .  .  "ge-
2686:*zamarigusa    avazat   vXspe   daifa    Yt /<?.       AbleiV  aus  ■arr'OB.u'ajflZw. 'elf;  vgl.  tF,  S  ?/o 81 ;  —  yahmai  . .  aurvantö  . .  v3sa  '^an-  ■     aK  und  IF.  p.  245.  —  Pü. :  yHdahum. }aianie   °va   caxra  (sd.)    Yt  10.136;    —  •  j-    aeväkam    Adv.    'zugleich' (?):    aiv aim  .  .  yß  t0  °ve  säsnä   (sd.)  gäsatä    Y.   narqm  asaonqm  ahunvitim  ga^qm  frasrä- ^9.8;  YtJ7.i9,2i;    —  yö  nö  °v6  at  U  vay'nti  Vd. /2.
3194:•  j.  "ataurvayö  i'ja  ßityant>m  västrlm vasByaanai  intam  hmSnhin^  Yt/0.60.
3368:—  yaisa  ni  d.ltl  . .  ''i^a  nä  >rJedüm  V. 5^-5>35-^'> — yit^ä  iä^aca  dahms  staota yesnya  haurva  daoaiti  '%a  ratu/rii  N. 3~;  —  yd^a  . .  nminopaitlm  paiti  tard.- pi'iw>m  dai'hyat  'ia  astryäH  "als  ob  er
3383:•  j.  ad-auruna-  n.  'priesterliche  Funktion, Priesterdienst':  Äa/  nä  a%rava  (sd.)  *ngm
3386:aS-aurvan-
3394:Ableit.  ans  lAaurvan-.  —  ai.  vgl.  äihmvatfä-
3397:•  j.  aihaurvan- '':a^a«r»n-,  äSravan-'' m,  'Priester'  im  Al!g e meinen ,  von  dem, der  Priestetqualität  besitzt  und  priester- liche Funktion  verrichten  kann  und  darf: uUa  nS  zlte  -va  .,  zara^uslrS  YLi_y.94;
3480:mit  avi  'einholen':  yest  ahi  paurva.- nafmät  aal  "lam  avi  nmänaya  (sd.)  yezt paskät  aai  ma'm  avi  apaya^sS.)  Yt.i&.a.
3583:—  ma%rym  spmttm  . .  pmrumca  . .  'r^mca V.  4.45;  45;  —  ahun?m  vairJm  . .  Tim sraoidyehya  (^^  frasrüiti  Y.  5. 14;  — apanmta  tiais^mi&A.)  G.3.T, —  'raheca yamahe  haplanhatdis  Vr.2/.o;  0,4^;  — ranuhlsla  a'A  .  .  hupaurva  (sd.)  vahehiS Ti/"  räsaintü  ¥.52.3;  —  aiwiea  'rim patiia  'rym  apsca  paurvalibya  "und  (man soll)  einen  zweiten  (Rüden)  und  dann noch  einen  weiteren  (zulassen)  und  zwar (soll  man  ihn)  gesondert  von  den  beiden ersten  (halten)"  V.  i^.  48.  3)  '>  der  Zeit nach 'der  spätere,  kUnftige'rja^a  mä  'racil (NPm.)  saoiyanis  stavqn  V.9.  2;  — yastä datrSMg  °rö  .  .  tarS.mqstä  "wer  darum künftighin  (eig.  posterior)^  den  D.  ..  auf- sagen wird"  V.  4:5. 11;  —  huzantSus  paiti •raya  YL  13. 134.  a)  mit  ayan-  n.  'der spätere  Teil  des  Tags,  Nachmittag':  */ra- \aire  ayqn  bavaiiii^A.)  hubar,rS  ..  a',a  "re ayqrt  duWirjm  ". .  dann  am  Nachmittag (kommt)  das  Unglück"  Aog.jJ.  A)  ASn. 'r?m,  'ram  und  IS.  °ra  als  Adv.  'postea, später,  künftig' :  yezi  nairyS  aukat  pasca hl  pourum  (sd.)  paiti.hin£öi^  paitisa  "r^m V.ÄSS;  v,%;  —  \mätyi^hy(r'ramimam dipim  patiparsiltiy  .  ,  BL4.8;6,  15,  ^.y,
3777:gaikaAü  tanusi^ä  Y.^J.  7-       2)  Praev.  (mit 'ak;gam-,  'bar;y/th-,  valn-  usw.).        a)  bei Ellipse  des  Verbums:   "wi?a  aparpm  (sd.) paiica    aparam    apnca  paurvaäbya    V.  75, 48;  —  asäaüä  haiä  van/iSus^il  mananhs vankyuscS   xla>rilt  staotäis  '^Tnifl  ahum staotSibyö  °bT  ux'o/l    '^wüt  uxüSibyS  yasnH %wät  yasnsibyd  "und  um  des  ASa  willen und  des    VM.  und  des   guten  XS.:    Lob- gesänge (häufen  wir)  nunmehr,  o  Ah.^  auf Lobgesänge  und  Sprüche  auf  Sprüche  und Gebete  auf  Gebete"  V.^j,.  10";  —  huxsa- %rSJ»m!li  (sd.)    .  .    xsa'inm    ahmai   hya^ 'bii^  dadsmahica  .  .  Y._Jv5. KompA-i  Ableit. —  aLiiM/,  mp..rai*,  np.a/". —  Vgl.  laii,  aei.  —  Pü. :  afar;  (in Komp.  auch): d/f  und  wepgelassen.  —  ')  S.  lu  aiiaiwülay- No.  I.   —    ')  Man  kann  aus   dem   vorherg. Ahsatzdad3maideetgiaT.Ka.  Gdn.n  Übersetzung GlrPb.   3.  32    ist    mir   unverständlich.     Pä.: släyisn  i  IS  öhrmatd  am  haf  släyi'snän  apar,  Sü. : ilulih    te    a-ämin    slulibhya^    utirflalarä.      — ))  Man  erwartete  die  selbe  Redensart  wie  V.
3896:*)  Die  vom  Beginn  der  Abenddämmerung  bia MiUernaclit  reicht  und  in  zwei  Abscbnille  ler- ßllt:    hü  fräimöMlay  -and  irizaurvaiia..     Vgl.
4081:•  j.  afsman-  n.  'Verazeae  (der  Gä^rJs)'": tiSranqm  kaurvafaoiryanam  . .  haitilca "manaca  (AP.)  '^  vacas^a  vacastastlmla  (sd.) Vr. /J.3; — vfsp?m^a  'man^m{Pi&y  yasa- maide  Y.  Ji.^;  —  aitatca  vacö  .  .  %ri.- afsm»m  (sd.)  . .  kais  Al  'man  (NP.)  ". .  wel- ches sind  seine  (des  AAunaVairya)  Vcrs- zeilen?"  Y,  19.16.
4115:FrW.  4.3;  —  'rahe  mainySus  dämanam ^'^  '5'  3i  —  y^t  titarat  °rS  matnyus dähim  alahe  .  .  antan  pairi.aväit^m  (sd.) fokuca  mattö  atarsca  /J  hg  taurvayatsm tba^ä  °rahe  mainySus  drvats  Yt  7_J,  7  7  f. ; 13;  — yint  nöit  tiurr/pttte  'rS  mainym nsit  yatavS  fairikssca  Vt  1^.44;  —  ailm dahakim..yqm..  drujim  fraca  k>rmlat  'rS mainyus  Y.(?.8;  —  aal  ahe  paityarim  frä- ijrMiat  'rö  mainyus . .V.l. 2;  'J0.3,Aog.2^; —  pairiAä  .  .  yä  uzdtihat  'rS  mainyuS  .  , paiHj>r)tSe  Yt,  A",  39;  —  taxm?m  urupi  .  . yat  barata  'tvm  mainyBm  framitim  (sd.) aspake  JaArpa  ^risatjm  aiwi.gämanam Vt./^.  29;  — paiti.psrme  'nm  mainyBm V, /o.  5;  —  fränämiliti  duhjarstavari'  °r3 mainyus  ax^amanS  Yt/p.  96;  3.^;  — naiHs  xsayät  °rö  mainyus  duzdalnS  FrW. 4.  a ;  —  xsnagiira  akurahe  mazdä  tarSidlti 'raAe  mainyius  Yt.  i.  o;  —  daxstanam  ydi Amli  'rahe  ntainySus  daxstim  V.  2.  29;  P, 2-2,  Y,  7i>,  11;  —  apayafUamah^a  'rahe mainyius  xrafstra  Yt.  21.1;  —  'rif  mainyus . .  dtävanam  daivS  V.  ig.\;  —  vJspB.mahr- käatca  pairi  drvatat  yat  -rst  mainyaot VL/_j.7i;  /0.118,  Y.2-j~-i,  V.'/o.ie;  — ai  duida  °ra  mainyS  V.ii).^;  g,  1,44,  lt. 10,  Yt//.  19; —  iaÖx  dusda  'ra  mainyö V.  i^,  1 2 ;  —  *'rahe ''  *mainy9us  duzdamanH Y.  Ö/.  2;  V. /p.6;  —  skutara  "ra  mainyö V.  79. 3;  —  "rS  mainyus  pouru.mahrkS (Stveri.)  Yt  10. 97 ;  usw.
4190:•  '].  a-ohvä-,  g.  a-hvä-"  f.  i)  'Antrieb des  Willens,  Schaffensdrang,  Lebenskraft' : pairika  yä  duzyäirya  vlspahe  atiksui  .  . ' faröit pairi'in^misA.)  anhvqm  avaAisiiyät\ (sd.)  Yt.Ä54;  —  ava  m!  3zis  .  .  par5it\ fairrbnpm  (sd.)  arihvqm  ava.d}nnqn  sada- 1 yäfi  (sd.)  V.  i5. 19.  2)  'Antrieb  derl Seele,  innerlicher  — ,  Gemütsdrang,  Ge-j müt'"':  kal..*manS  asti  vT/aymii'tfm{s±) anhvqm  vjmar3zist?m  (sd.)  VL  /.  2 ;  —  ' virtzvatca  (sd.)  mat^  vansvatica  attuAa  j 'W.  62,10;  —  ye  kvam  ankvam  yaozdaite\ humatsilia  .  .  V.  ^.2i^>;  si  *PÜZ.,  lO.  19  I PüZ.;  —  dusx'arpnä  . .  asH5  asti  auuhaya  \ (LS.)  ".  .  ist  unfroh  in  seinem  Gemüt"  j YLJO.105;  —  aibl  ahväha  daxst^m  dilvOi\ (sd.)  Y.5/,9;  —  yatära  vä  dim  paurva frayasäiti  fraor^t  fraxsni  avi  manö  (sd.) zrazdälöii  ar^huyal*^  (oder  avuhyat)  i>  haca ". .  gern  in  sorglichem  Sinn  aus  gläubigem Gemüt"  Yt  /o.  9;  —  fora  vi  räki  am?sä spmtn  yasmmcä  rahmtmcä  firä  mana»hä ..  vaiaahä  ..  syat>^anä  ..  dw^iy«  (IS.) » Y.7/.18.
4241:•  j.  an-aoäa-  Adj.  'dem  kein  Verderben droht,  unsterblich':  aurvantö .  .  mainyus.- ii^ar?^a  'shihs  Yt  70.125.
4698:\)amm  Y.$4.2,  G,  j.6; — yä  {ar?ävi) 'vaiti fratalaili  Y.  Ö5. 3 ;  Yt.  5. 1 5 ;  —  a^tn  vatau- hlm  .  .  hrpsailTm  'vattTm  Y.  3. 14;  Yt /J. I,  7;  —  drvaspqm  . .  'vaitlm  YL9.2;  — fravaiayö  .  .  yä  'vaifli  Yt  13.  29;  —  at töi  atrjm  . .  *asXsttin  'vanhm  Y.j^4;  — tiiirim  .  .  'vant?m  YtÄ4;  —  vatianttm 'vant»m  Yt  21.  i;  —  °vatS  amai  'vatÖ virp^raynäi  'vat^yO.  »rütyi  'vai'iya aiöii  'vai^ya  astdil  'vaüyä  paurvatälo 'vai'i'yB  uparatälö  'va^byä  yazatoAbyö  Vr. g.i,.  b)  sonst;  uströ . ,  b)r?zB  "vä  Yt i.^.  1 2 ;  —  srlra  urusta  'vaiti  (VSf.)  .  . UfTaireY.it^.iB,Vyt22; — srayarfhö  vouru- ka?ahe  'vatö  Yt.<S.46;  —  vasnm..  zaröil ayanhö  frahixt»m  'vatö  \L  10.96;  —  'vat iimäfum  Y.  57. 10;  —  ptiüm . .  yim  aiwatö 'vantim  Vyt.^;  —  'vaitlm  sitiqin  dävöi (sd.)  dr»gvasa  Y.  44. 14.  —  IstJm  . .  pouru.- sarioam  'vaitlm  Y.  65. 1 1 ;  —  hazö  "vat  Y. jj^.  iz;  —  yahmi  maza  'va  (NSn.l')J' '  iiiäälpm  Yt  10. 64  (?) ;  —  *°vata  vaca  F.3  e. AbleiL  —  ai.  dmm-ant-  Adj.;  vgl.  mp.  (PS.) amäz-nnd.  —  ')  %  jg4.  —  •)  Zur  Zusammen- Stellung  von  amai'aaf-  mit  ^'/ri^ravan ,  viri- %rasan-  s.  'amn-  2.-3)  Wenn  richtig,  wohl Neubildung  lum  NSm.  'va  nach  der  n-Dekt.
4752:F.  ff;  —  :^ahe  gayehe  :^airvats{5A^  "sähe Y.5.1,  Yt-Äii.  a)  von  der  Sonne: hvan^ail>m  'hm  raim  aurvat.asp»m  Yt. 6.\,  4,  6; —  hvar>.xsaitahe  'sähe  ra^ahe Yt-ö-o,  Y.22.24J  —  paurva.naemäi  °hhe hä  yaf  aurvat.aspahe  Yt.  10. 1 3.  A)  ins- bes.  von  den  dem  AhuraMazdäh  nächst- stehenden Gottheiten*':  yaia  vahm>m 'iaiibyS  Y.  21.2;  —  -saHi  . .  avarshe  ismti masyäkänAs  Aog.  41.  a)  sonst  in  Ver- bindung mit  spitUa-  Adj.  'heilig',  das  in GHapL'vor-,  sonst  nachsteht:  *vyäX3mca kanjamanimca  (sd.)  yat  as  'sanqm  sp?nta- nqm  banlnvS  *avarihe  as/0  y?mat^m  (sd.)
4758:nqm  Yt.  J7.2;  —  yö  . .  yazata  ahunm mazdqm  yazata  -/J  spmts  Yt.  J".  1 8,  Y.57.Z ; 2/.2,'Vr./j.  1, 18.1,  ig.i,  23.1,  V.  ig.  19, N,  70;  —  aAur?m  mazdqm  .  .  'sit  sp^ntit yazamaidl  Y.jj.i;  2.2,  25.4,  77.4;  — ii^mS  afturäi  mazdäi . .  'salibyff  spantaAbyS V./p.2s;Ny./.  i,Yt<?.3s,  io.  89. /^.  157, J5.44,  S, /.  i;  —  nsit  xsnävayeiti  ahunm mazdqm  tßit  anye  °^a  sp?nta  Yt.  10. 139; 139;— ^i7/'J  nmätttm  mathantm  ahurahe mazdh  ..  'sanqm  spuntanam  V.  79.32;  32, Y.y.i,  4.7,  22.1.  29.2,  27.2,  Vr.9,6, A.  2. 1 ;  — bsrijayat  ahurd  mazdä  bgry/ay^n sp?ntfi  Yt. /o.  90;  —  yazaite  ahurtm 'IS  sputts  .  .  haom  urvänim Yx.6.\;  —  ahuräi  mazdai  ..  'laAbyS spmtaMyS  .  ,  aiwyS  vanuhibyS  Vr.  Ii.  i ; —  ahurahe  mazdl  .  .  "sanqm  sp>ntanqm sraofahe  asythe  . .  ähr5  Y.  22, 4;  —  ahu- rsica  mazdsi  sraosäica  .  .  rasnvaica  . . mi^räica  .  .  '/aeibyasca  sp>ntaHbyS  . .  Vr. II.  6 ;  Y.  4. 2;  —  ahurahe  mazda  . .  'Sanqm spmlanam  mü-rahe . ,  rUmanasca  ^ästrahe Y.22.23;  (JÄ22,  Yt.7.1.  b)  von  ein- zelnen Göltern:  ahm  at  vahiStfm  . .  hyat sra!st?m  hyat  sp>nt}m  'hm  Y.J7.4;  — astm  vahÜt)m  sra!st?m  °hm  sppnt>m  Yt. j.  18*;  S.  2. 3;  —  ahre  ..  ya^ustsmäi 'Sanqm  spinlanqm  "dem  Ä.,  dem  geschäf- tigsten der  ASp."  Y.I.2;  —  vahu  manS 'hm  sp3nt}m  S.  2.  2;  —  xlfdrtm  vairjm 'hm  sp^trm  S.  2.4;  —  haurvatätim  'hm spintam  S.2.6;  YX. 4-\<i' -j^ amgrsfatätim 'hm  spuntsm  S.  2.7.  ['s'a  spunta  Yt.Ä 38  ist  Einschiebsel,  s.  an-  No.  3.]
4775:•j.,g.am»rBta'^t-,  amarBtlt-'T.'Unsterb- lichkeit.  Ewigkeif;"'  tit  d^hnaotä  maslm hujyiH5is{sA)  "ntstascä  Y._j2. 5 ;  —  'rstSitl *a^aonö  urvä  also  (sd.)  utayütä , ,  Y.  43. 7 ; 48. 1 ;  —  yä  fyat/^an/t . .  -ntäbm  astmcä *taibyO  danhä  (sd.)  .  .  xs^nm^a  haurva- tätö  Y.34-^i  —  ahmäi  aahat  vahiihm yi  möi  vtdva  vaolat  hai~ilm  mq^r^m  yim haurvatatö  alahyä  'ritatasca  "dem  soll das  Beste  zu  Teil  werden,  der  mir,  ein: Wissender,  ktmd  tut  das  rechte  Wort  Aia^ von  der  Wohlfahrt  und  Unsterblichkeit" Y._3/.6.  a)  bes.  in  Dual  Verbindung  mit
4776:kaurvatüt-,  xlaisröi  hU  haurvüta  'ntäla
4777:ahmst  sISi  dqn  (sd.)  trvjh  utayüitl  Y.  4I5. 10;  57.7,  44.18,  47.1;  —  0,a  haurvaia "rstäta  ySi  slö  /nlzd»n  asaonqm  parSMsti jasmtqm  Yt.  1.25;  —  mazS  (sd.)  avaKyai .  .  daidl  Aaurväd  Titätä  (GD.)  V.  5Ä 7.  a)  als  Bezeichnung  fiir  die  Speise der  Seligen*;'*  at  löi  ubl  haurvassa 3^ar?%äi  3  'r^atasca  (NS.)**  "und  deine beiden  werden  zur  Nahrung  dienen,  der Wohlfahrtstrank  und  die  Unsterbltchkeits- speise"  Y.,?4.  n.  A)  als  Gottheit  {Amasa Spmtd),  der  die  Sorge  für  die  nützUchen Pflanzen  anvertraut  ist  (SüErL:  vanas- patipatiliySi  aya  damaya  fraonnta  akurd .  .  vohu  manu  .  .  a£>m  . .  xsa%rpm  .  . ärmaitil  frä  kaurvatas  fra  'r>tatils  Y.57. 24;  —  vanät  haurvasca  °rstas^a  (NS.)" •wa  sUMtttca  farsmmla  Yt  ig.  96 ;  96 ;  — armaitfm  ..  haurvaiat^m  ..  'rsiatatsm  yaza- maide  Y.16.%;  JI.12,  S,  2.6f.;  —  mazdii dadat  akurö  haurvatö  'riiatascä  .-.  sarS Y. 31.21;  —  data  vj  'rjtSscä (NS.  als VS.)i> utaySitT {%A.)  kaurvatas  draonsY.33.9,;  — iaurvatas^a  'r)tatasca\t.4.i(f)  a)bes. i  in  Dualverbindung  mit  Aaurvatät-:  aya I  damaya  fraornnta  ahurd  masdä  .  .  fra ,  sp^nta  *armaitis/ra  haurvaia  °rHäta  (ND.) Yt.  JO.92;  —  sarBi  bszdyai  (&d.)  haurräiä I  "niaia  (ND.) . .  j?.  .  Y.44.17;  —  upa.- ßm^ti  (sd.)  haurvatä  °r>talä  (AD.)  Y.  45, .  5;  —  sp)ntayai  ärmatSe  haurvalbya  -ntat- '  bya  Yt.  7. 2 ;  H.  i.  7 ;  —  yS  spsntaya  arma- töis  yä  haurvatä  'ntata  (GD.)  Y.  70. 3 ; .  —  kaurvatasca  nö  'ritats,'''^ gTusca  tasiiö.. I  Vr.  g.  5,  a)  amir>tät5  (näml.  ayar?) heisst  der  7.  Monatstag:  S.  7.7;  vgl, 2. 7, ,  V.  7tt.3,  A  1)  als  Bezeichnung  für  die
4778:;von  Arn.  geschützten  Pflanzen",  in  Dual- verbindung mit  haurvatat-  (sva.  Wasser): 3^ar3%3m  myasdam  haurvatä  °r)tata  gäus huha  haomitnca para.haomamid Y.8.i;j.i, 4.1,  6.1T,  7.26.
4803:mit  upa  i)  'hinzugehen,  kommen  zu—' (Akk.):  upa  tqm  vanqm  asiü  V.5.2;  — aS?m  . .  asisi>m  zaurvan>m  (sd.)  upaitt'^ yal  spatiS  Y.ij.28.  a)  spez.  'in  die Schule  gehen  zu  — ':  Jt^m  *afm  at  (sd., No.  6)  afirapaitim  upayat  (3SKA.)  "zu welchem  Lehrer  soll  er  dann  in  die  Schule gehen?"  N.  r2.  2)  I!  'gelangen  nach  — ',
4918:•  g.  ay^m '',  j.,  g.  aem '',  p.  iyam  '>,  j.  im  ^ NSm.  und  f.,  Fron, dem. 'dieser';  I)  in  stark- deiktischer  Verwendung,  'der  hier',  von dem  gebraucht,  was  dem  Sprechenden nahe  liegt;  i)  adjektivisch:  ya'i:a  Tm  zä astica  tm  z-j  avaiti  bqzö .  .Y.jg.T,  F.  4a, V,  2.8,  9;  —  yö  imqm  zqm  aiwi.vjtrtzyäti .  .  Hat  aoxia  Tm  sJ  V.^.z6;  24;  — pu%rjm (sd.)  a^n  narö  varäa  "..hicce  hoino.."  V. ^5-1 3; —  \adam  niyastäyam  tmämyuviyam ha"lanaiy  . .  iyam  }'umyä  akäniy  D.  i-j;  — iyam  dahyäuS parsi^  . .  D.  4. 3  !.  a)  zu- gleich auf  ein  Relativum  vorausweisend: kuda'jaSm  vJtö  viliti  (sd.)  yim  . .  Atibaoioit?- m»m  jigaurvaH.2.Z;  26.  t)  substan- tivisch: aZmca  ahe  ci'i iB.daxsli  atihat  a!m ciirBpäiti.dayB  V.  i.  14  GL  (?);  —  in Kongruenz  mit  demPraedikai:  '\iyam  gai4' mila''  hya''  magtd adunijiya*  ava^a  a'^a- ha''  "das  (auf  dem  Bild)  hier  ist  G.,  der M.;  erlog;  sosagteer"  Bh  b;c-k;  —  iyam maciyii  D.io(f)*'\.  a)  zugleich  auf  ein Nomen  voraus  weisend;  aim  möi  ida  visiS (sd.)  .  .  zara^usIrB  Y.  2p.  8.  U)  in schwachdeiktischera  Sinn,  substantivisch 'dieser,  der,  er';  1)  auf  ein  Nomen  zurück- weisend:   iatärJm    a    angr/i  vä   hvS  vä
4977:Yt.  10.  46.  a)  mit  relativischeni.  An- schluss:  °vä  (APn.)  j>ä  näiryi-  yä  fu'irahe "das  der  Frau  .  ."  N.  5^;  —  'v3.  (APf.) ^1  anyä  srävaydij  "die  andern  (näml. Gä'^Ss)  .  ."  N.46;  —  naicis  "vat  y3  spsn- iahe  Yt.i5.3t?).  3)  auf  ein  Relativum als  dessen  Korrelat,  a)  adjektivisch:  dva aurvanta  . .  aom  .  .  aurvanhm  yS  anhat äsus. .  aom  ,  .  aurvanhm  yö  , .  urvaisayat YL5.131;  /.24,  14-^9',  —  i^y  '^"J  ^'"^^ 3s  .  .  yat  mS  fravaocö  .  .  Y.ig.i;  Yt  5. 41,  Vr.  20.  i  f.*,  G.  2.8;  —  xfä^r^meä  'val .  .  yä  .  .  rämqmcä  (sd.)  dät  Y.2p.  10; °va  (IS.)  daxita  daxstavanta  yä  nditpom ßra{sA.)/raäaxsta\t.5.')^;  —  'vä(lS.)i^ wanarthii  yä  .  .  manta  .  .  Y.  33.  6 ; 'vaiiiha  drüjB  .  .  yä  .  .  upa.dvqsaiti  V, 17;  17;  —  Aaca  'vai/ihai  Jahikayäi  .  . yä  .  .  upa.baraiti  (sd.)  Yt.  17. 58;  —  nsU 'va  (APf.)  zaoira  ..  yä  ..  framthar>nii Yt5.93;  I4.\i\  —  *'va}ika  (APf.)  > va^ays  .  .  yä  .  .  anhan  Y.  2j.  1 ;  —  •; (APn.)  dämqn  . .  yi  A^nti  . .  Vr.  7.4;  — •w7(/  uroaikis  (sd.)  ya  ta  . .  didirszd  Y. 44--ii;—''*'vä  (NPf.)  dakyäve^  tyä  dura- yt^v<^uS  adärayj'  \i.6.ä,;  —  mat  'vaby5 (DP.)  daxstäbyö  ydäsa  aHrai'a  "mit  den Zeichen,  wie  ein  Priester  (sie  hat)"  V.  /j. 22.  a)  das  Substantiv  ist  aus  dem Relativsatz  heraus  zu  ergänzen:  yä  tu haßi  (sd.)  'vi  (APf'>,  näml.  asll)  yä  da alis..\.43.\.  b)  substantivisch:  'tat yäsqs  hyal  vS  istä  (sd.)  vakishm  Y.  4g. 12;  —  've  (als  AP.)  aifi  (sd.)  dat^ants . .  ysi  . .  dniihiti  Yt.  10.4s ;  45;  "*  °z'J»V aibt  ySng  dainll  nSit  Jyatius  (sÄ). .  Y.  J2. 15;  —  'valsqmca  päi^B  paniö  yim  (statt AP.)  isMiH  mhmJrufdYK.  /O.45,  4)  auf den  Inhalt  eines  Konjunktions-  oder  Re- lativsatzes, a)  adjektivisch:  'va^  ayapl>m dazdi  mi  .  .  ydha  azgm  häcayene  . .  Yt.5. 18;  130,  p.i7f.,  75.3,  77.25;—  'vaÄeca paiti  yqiiahe  ya^  he  da%ai  .  .  Yt  16. 6 f.  b)    substantivisch:    'val   h!   as/t
5333:•  j.  araska-  m.  'Neid"':  ttsit  zaurva  . . m?r?hyul  nöit  'k3  daSfö.äatS  Y.p.5.
```


## [2026-09-05T20:30:01.592Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '447,450p' AHD_watkins1985.txt",
 "description": "Print AHD er-1 entry"
}
```


### [2026-09-05T20:30:01.787Z] TOOL RESULT

```
er-1, To move, set in motion. 1. Probably Germanic *ar-, *or-, *art(a), to be, exist, in Old English eart and aron, second person singular and plural present of béon, to be:
ARE!, ART?. 2, Perhaps in Germanic suffixed form “er- n-os-ti- in Old English eornoste, zealous, serious: EAR- NEsT!. 3. Suffixed form *or-yo- in Latin oriri, to arise,
eu-!
appear, be born: ORIENT, ORIGIN, ORIGINAL; ABORT. [Pok. 3. er- 326; ergh- 339.]
```


## [2026-09-05T20:30:10.247Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^• *[jgp]\\..*aurv\\|^• *[jgp]\\..*auru\\|aurvat.asp\\|aurvai\\.asp\" BRT.txt | head -20; echo \"=== hamar ===\"; grep -n \"hamar>na\\|hamarana\\|hamaripa\\|ham?r\\|hamara\" BRT.txt | head -20",
 "description": "Grep BRT headwords"
}
```


### [2026-09-05T20:30:10.376Z] TOOL RESULT

```
3194:•  j.  "ataurvayö  i'ja  ßityant>m  västrlm vasByaanai  intam  hmSnhin^  Yt/0.60.
3199:•  j.  'aiti  ind.  Adj.  'so  viele':  "//  j^  Aaitn (sd.)  ya>a  a>auruiie  V.  /j.4S;  45-48'.
3383:•  j.  ad-auruna-  n.  'priesterliche  Funktion, Priesterdienst':  Äa/  nä  a%rava  (sd.)  *ngm
3397:•  j.  aihaurvan- '':a^a«r»n-,  äSravan-'' m,  'Priester'  im  Al!g e meinen ,  von  dem, der  Priestetqualität  besitzt  und  priester- liche Funktion  verrichten  kann  und  darf: uUa  nS  zlte  -va  .,  zara^uslrS  YLi_y.94;
3539:•  j.  apa.dis-  Adj.  —  ?  — :  ar>zS.saman>m ,  .  °s>ni  ny^idauru  YX.ig.\i.
4081:•  j.  afsman-  n.  'Verazeae  (der  Gä^rJs)'": tiSranqm  kaurvafaoiryanam  . .  haitilca "manaca  (AP.)  '^  vacas^a  vacastastlmla  (sd.) Vr. /J.3; — vfsp?m^a  'man^m{Pi&y  yasa- maide  Y.  Ji.^;  —  aitatca  vacö  .  .  %ri.- afsm»m  (sd.)  . .  kais  Al  'man  (NP.)  ". .  wel- ches sind  seine  (des  AAunaVairya)  Vcrs- zeilen?"  Y,  19.16.
4241:•  j.  an-aoäa-  Adj.  'dem  kein  Verderben droht,  unsterblich':  aurvantö .  .  mainyus.- ii^ar?^a  'shihs  Yt  70.125.
4380:•  j.  aii-a'haxta-'>  Adj.  'der  nicht  berech- tigt (geeigenschaflet  und  ermächtigt)  ist {etwas  zu  tun)':  yS  anyahe  ^apynnäyüka ^'lä'^  a'^aurufiTttt  paraahacäiti  "wenn einer  eines  andern  Kind  unberechtigt  3'  zu priesterlichem  Dienst  mit  sich  wegfiihrt" N.7;  6;  —  'tö.  .  ahaxts  (sd,)  N.tf;  — haxts . .  'ts  N.  6-,  — yasta  aSlalsam  mazda- yasnanqm  tnyazdavanam  aüanhqm  yat myazdanam  "ts  parabaraiH  nsit  täyul ,  . bavat  .  ,  ainyi}  kasat  .  .  "und  wer  von den  ,  .  M.  etwas  von  den  My.  wegnimmt, auch  ohne  berechtigt  zu  sein,  der  , . ;  aber irgend  ein  andrer  .  ."  N.  6^;  —  yezt^a *aile  ratavö  *'ta*^  *para.iyayanH  "und wenn  die  R.,  weil  (zu  ihrem  Amt)  nicht qualifizirt,  weggehen"  N.  ^o;  —  zaota  (sd.) *-ßS)  parayat  N,  So.
4403:•  j.  an-äxrviäa.dÖiSxa-"'  Adj.  'des  Augen nicht  —  ?  —  sind':  vayul aurvS  .  .  "re ya'ia anyasäi  xsa'irät  xsayamna  .  .  YL  ij.  54.
4540:•  j.  an-uz'var^-  Adj.  'nicht  wieder  gut gemacht':  astunim  .  ,  syaoh?nanqm  v»r>- zimmm  'tai paiH paurvät  "..ohne  dass  die frühere  (Tat)  wieder  gut  gemacht  ist"  V. 4.2a;  —  syaokna  varsta  . . /ralla  apatita 'ta  (APn.)  V.75.2.
4701:•  j.  a-marant-  Adj.  (ohne  Obj.)  '(die  vor- geschriebenen Gebete)  sich  nicht  ins  Ge- dächtais zurückrufend,  nicht  in  Gedanken wiederholend':  yö  saite  haurvqm  taras^a xsapaiigm   ayaztmnö  asrilvayamnS  'rS  V.
4752:F.  ff;  —  :^ahe  gayehe  :^airvats{5A^  "sähe Y.5.1,  Yt-Äii.  a)  von  der  Sonne: hvan^ail>m  'hm  raim  aurvat.asp»m  Yt. 6.\,  4,  6; —  hvar>.xsaitahe  'sähe  ra^ahe Yt-ö-o,  Y.22.24J  —  paurva.naemäi  °hhe hä  yaf  aurvat.aspahe  Yt.  10. 1 3.  A)  ins- bes.  von  den  dem  AhuraMazdäh  nächst- stehenden Gottheiten*':  yaia  vahm>m 'iaiibyS  Y.  21.2;  —  -saHi  . .  avarshe  ismti masyäkänAs  Aog.  41.  a)  sonst  in  Ver- bindung mit  spitUa-  Adj.  'heilig',  das  in GHapL'vor-,  sonst  nachsteht:  *vyäX3mca kanjamanimca  (sd.)  yat  as  'sanqm  sp?nta- nqm  banlnvS  *avarihe  as/0  y?mat^m  (sd.)
4775:•j.,g.am»rBta'^t-,  amarBtlt-'T.'Unsterb- lichkeit.  Ewigkeif;"'  tit  d^hnaotä  maslm hujyiH5is{sA)  "ntstascä  Y._j2. 5 ;  —  'rstSitl *a^aonö  urvä  also  (sd.)  utayütä , ,  Y.  43. 7 ; 48. 1 ;  —  yä  fyat/^an/t . .  -ntäbm  astmcä *taibyO  danhä  (sd.)  .  .  xs^nm^a  haurva- tätö  Y.34-^i  —  ahmäi  aahat  vahiihm yi  möi  vtdva  vaolat  hai~ilm  mq^r^m  yim haurvatatö  alahyä  'ritatasca  "dem  soll das  Beste  zu  Teil  werden,  der  mir,  ein: Wissender,  ktmd  tut  das  rechte  Wort  Aia^ von  der  Wohlfahrt  und  Unsterblichkeit" Y._3/.6.  a)  bes.  in  Dual  Verbindung  mit
4905:•  j.  a-yaz9mna-  Adj.  'nicht  betend':  y^ saSte  haurvqm  tarüsca  xsapamm  °«5| ". .  ohne  zu'beten"  V.JÄs;—  mitAkk. 'zu  -':  yüi  °na  am>Ss  sp>nl!"ä\t  nicht  zu den  ASp.  beten"  Vyt  12.
4918:•  g.  ay^m '',  j.,  g.  aem '',  p.  iyam  '>,  j.  im  ^ NSm.  und  f.,  Fron, dem. 'dieser';  I)  in  stark- deiktischer  Verwendung,  'der  hier',  von dem  gebraucht,  was  dem  Sprechenden nahe  liegt;  i)  adjektivisch:  ya'i:a  Tm  zä astica  tm  z-j  avaiti  bqzö .  .Y.jg.T,  F.  4a, V,  2.8,  9;  —  yö  imqm  zqm  aiwi.vjtrtzyäti .  .  Hat  aoxia  Tm  sJ  V.^.z6;  24;  — pu%rjm (sd.)  a^n  narö  varäa  "..hicce  hoino.."  V. ^5-1 3; —  \adam  niyastäyam  tmämyuviyam ha"lanaiy  . .  iyam  }'umyä  akäniy  D.  i-j;  — iyam  dahyäuS parsi^  . .  D.  4. 3  !.  a)  zu- gleich auf  ein  Relativum  vorausweisend: kuda'jaSm  vJtö  viliti  (sd.)  yim  . .  Atibaoioit?- m»m  jigaurvaH.2.Z;  26.  t)  substan- tivisch: aZmca  ahe  ci'i iB.daxsli  atihat  a!m ciirBpäiti.dayB  V.  i.  14  GL  (?);  —  in Kongruenz  mit  demPraedikai:  '\iyam  gai4' mila''  hya''  magtd adunijiya*  ava^a  a'^a- ha''  "das  (auf  dem  Bild)  hier  ist  G.,  der M.;  erlog;  sosagteer"  Bh  b;c-k;  —  iyam maciyii  D.io(f)*'\.  a)  zugleich  auf  ein Nomen  voraus  weisend;  aim  möi  ida  visiS (sd.)  .  .  zara^usIrB  Y.  2p.  8.  U)  in schwachdeiktischera  Sinn,  substantivisch 'dieser,  der,  er';  1)  auf  ein  Nomen  zurück- weisend:   iatärJm    a    angr/i  vä   hvS  vä
5026:•  j.  ava.Jastay-  f.  'Bitte':  °/Tm  paurvqm
5333:•  j.  araska-  m.  'Neid"':  ttsit  zaurva  . . m?r?hyul  nöit  'k3  daSfö.äatS  Y.p.5.
5383:•  j.,  g-  auruna-  'wild,  fenis,  saevus': maSsahe  kihrpa  'na^e  Yt.  l4- 23;  —  'na/a gairisiicö  sizdraca  ravascarätö  "die  wilden (Tiere),  die  in  den  Bergen  hausen,  und die  scheuen,  die  in  den  Ebenen  streifen" Yt.  ^36;  —  alityS  mos  aia  syasdal{sA.) yavaf  ahmal  'nä  xra/strä  ".  .  soweit  als vor  uns  die  wilden  Raubtiere"  \.34. 9.
5386:•  j.  auruäa-  Adj.  'weiss',  1)  von  Tieren: pttsüm  .  .  'hm  vH  vohu.gaon^m  vä  "ein weisses  oder  schwarzes  Schaf  Yt.ÄsS; —  aspa/ie  ktkrpa  'iahe .  .  aspahe  kihrpa sämahe  "in  Gestalt  eines  weissen  Rosses . .  in  Gestalt  eines  schwarzen  Rosses"  Vt. Ä  18-21";  —  aurvants  'la  raoxsna  fnl- ä)r»sra  Y. 57, 37;  YL  JO.  136.  z)  sonst: srlra  i-a  auhtn  blzava  'h  (ND.)  Yt.5.7;
5397:•  j.  auru5a.bäzav-    Adj.    (auch   : 'weissarmiß':  kaininö  kihrpa  . .  "Zfh  \^o.,  .  ^  ,,     ,
=== hamar ===
4817:—  pasäva^  vistäsp<^  hada  kärä  hyJ*  anu- siys'  paräya"  Bh.2. 16  (P)^».  aa)  mkpatii' und  Akk.  'gegen . .'  und  mit  Inf :  pasäva^ /iami>''iya  *Aa"gmatä  {sd.)  paraita(KP.) paiis  . .  hamaraiiam  cartanaiy  Bh.  2. 7 ; 8-11,^.10.11      b)  mit  haca  und  Abi.  'von
5043:I  'iilsam    hamaranam   kartam     .  .  da  (zur •  j.  avaitet  Adv.  'von  dorther":  ft'Ä/-r»i..  jangegebenen  Zeit)  wurde  von  ihnen  die
6012:ni/antlni  Ytß.  54;  18,  22',  26,  30,  42,  50, 54,  lOS,  117,  130,  p.4,  9f.s,  18,  22,  26, 72.2,  74- 58',  75.3,  28,  32,  Vytao»,  21, 4ß;  —  da%äni  ti .  ,  kazannm  .  .  uta  Ig 'S3m  äfrinäni  ..  Y.22.4L;  YL5.63;  — j/ai  mam  iura  paedayanta  .  .  äai  'stm tanüm  aguze  .  .  äai  tnam  fraguzayania  . . Yti^-SS;  56;  —  kü^a  tl  'um  varsm i?rjnavane  V.  2.  $t ;  lff.12,  22.6',  Ytij. 57;  —  't?m  II  g<K%ä  frähoyeni  'z?m  .  . 'Z3m  V. 2.5;  27.6,  7,  Vr.j.7;  —  \valnä a''ur(^mazdäha''  'dam  xsäya%iya^  amiy . . 'damsäm  xs'äya^iyi^  aham  Bh.  7. 5!;  — iyam  gaumätJ'  ,  .  avahä  a%ak(r  'dam baräiy^  amiy  . ,  'dam  xl3ya%iye^  amiy Bh.b;  c-j",  7.11,  13,  i6',  2.3,  s,  14,  J-S. 13;  1^2^;  —  ima'  tya'  'dam  akunavatn vasnä  J'ur^mazdäha'  ah/^ ..pasavJ' ya%ä x^aydiiiyJ'  abavam  'dam  19  hamaranä akunavam  vasnä  t^un^mazdäht^  'dam- säm ajanatn  uta  9  xssyaHyä  agarbäyam Bh..^.  2;  — pasäv^  'dam  t^urt^tnazdäm patiyävahaiy  a^urJ'matdämaiy  upastsm abar(^  .  .  avähä  'dam  . .  gaumätam  .  . aväjanam  . .  avadasim  aväjanam  x/a- %''amHm  °dam  adrnam  vasnä  a^urc^maz- dähc^  'dam  xsilya'^iyaf'  abavam  J'ur^- mazdä  x/ä^^am  manS  Jrsbara^  Bh.  J.  13; 14';  —  'damsaiy  uta  ftaham  .  .  frajanam ,  .  pasävJ'  'dam  .  .  uzmayapaiiy  akuna- vam Bh.  2. 13;  — pasävtrsaiy  'dam  ulä näham  .  .  fräjanam  ,  .  pasäve^sim  ,  ,  ut- mayäpatiy  akunavam  fih.2. 14;  —  °dam (s.  I  b)  xläya%iy^  amiy  vasna  c^urt^- mazdäha/"  'damsim  *g'a^avä  niya/ädayam tya^/äm  'dam  a%akam  avc^  .  .  D.  ö.  4 ; 3'.  5>  4-1,  5-2.  ^7-3^  Bh.  j.is,  16,  17', 18I,  19',  2.1',  2,  4,  6',  7,  9,  10,  II,  12*, 13,  Bh.^.  I,  2,  6,  8,  13,  14,  4.4,  6,  8, 12,  IS,  18,  5.1%  X.7.3,  ^.311.  Die Übrigen  Siog.-Kasus  des  Fron.  i.  Fers. s.  unter  ^ma-.  [¥.4:^.14;  lies  a&;  — Yt.  7.29:  lies  zamarf.'j
7948:;  —  \  da/iyävc^  . .  <i'iar  °ml  dahyäv^ Bh.  7.7f.;  8;  —  nämSnTs  ..  'mä  nUminr/ Yti.j$f.;  —  l'maiy  9  xiäya'^iyä  adam agarbäyam  ti'tar  °mil  (APn.)  hamaraiiS "diese  (genannten)  9  Könige  habe  ich  in diesen  (bezeichneten)  Schlachten  gefangen genommen"  Bh.4-3.  2)  substantivisch, auf  einen  Satz  (,  direkte  Rede,  Aufzählung) : °mat  vS  SpB  jai'yani  "darum  (in  S  '  i) bitte  ich  euch,  ihr  Wasser"  Y. (jj.  12; 13",  Yt.4.3';  —  'mal  a^rff  äfri- <m  "so  (wie  vorher)  lautet  des  Feuers Segenswunsch"  Y.62.10;  —'^ya'^ä  °mt/' kasiyam  naiy  duruxlam  (sd.)  adam  akuna- Bh.^.  7 ;  —  II  °wa*  ly^  maitä  kartam par'iavaiy  "das  (wars),  was  ich  in  P.  tat" Bh,_y. 2;  4,  12,  2.15,  4-^;  —  in  Kon- gruenz mit  dem  Fraedikat:  1  'ma  dakySvJ^ lya  mann  paliyaila"  "das  (in  S  6)  sind die  Länder,  die  . ."  Bh.J.  7;  —  'nie  aste vala  yöi  hinti  ..  sna'ä^m  V.  fo.  16;  17; —  "mas)  U  haoma  gä%a  Y,  10. 18;  iS-J, i9(?).  a)  in  Verbindung  mit  la-,  a)  ad- jektivisch: *vlsqs  (sd.)  *l'lca  °ma  niJmJnls parslasca  .  .  vTsante  Yt. /.  19.  ß)    sub-
9150:—  vupim  ä  ahiHilt  '^rä^r^m  k}r?navat yal  .  .  V.  jj.  15;  —  yai  tum  atnim arain^is  sao:a\a/a  kinnav  antem^>\ H.  2.  13;  13,  Vyt.  _J9  (wo  hrmvö'*;\ aSPrA.?;;  — .iaÄ-y  k?r.maoiti  yat  avSstrim  1 V.  j;.  51;  —  I  ..  ^■akata  aiii^  avairä\ hantaranain  akuma  Uli.  X.  18,  ig',  i'.  iz;l 1  z ;  —  avadä  hamaranam  aktmaus  hadä  ' hamtk''iyaibii  Bh._j.i;  3,  2.6,  14,  5.1;  — -j avadii  hamaranam  akunava"  Bh.j.6,7,9,1 10,  2.  7  — 11,16;  —  avaiäsäm  hamaranam  , kar  tarn  Bh.  2.  6-1 1,  i6,_y.  1,3, 6, 7, 9, 10;  l
10068:mit  harn  i)  '(mit  einander)  zosammen- konunen,  -treffen  (auch  feindlich),  sich  zu- sammenfinden', Akt.undMed.:  yim  aiwits (sd.)  paoiris  apö  hqm  . .  jasßn/s{^PIA.)"i Yl.ifi.66; —  Aya^  hSm  spadä  aiiaocanhä (sd.)  jamactl  (3DKM.)  Y.  ^.  15;  —  yal spfl'ja  hanjasäiiU  (statt  Du.)  YL/4.43;  V.  7. 44;  —  atcS  hyat  13  kSm  mainya  jasaügm "und  als  diese  beiden  Geister  zusammen- trafen" Y.  30.  4 ;  —  yat  atima  *Aanja- sante'^^  pouru  gaonalie  (sd.)  u^akeca  N. ^5\  —  yi  pairi  barasma  kanjasrnte  N. 6'2(?),  3)  D  'sich  sammeln'  (miltärisch) : pasiU-e^  hami^''iyä  *ha''gmatä  (PPfP.)"' paraitn  .  .  hamaranam  {fartanaiy  "drauf sammelten  sich  die  Aufruhrer,  ste  zogen aus  ..  eine  Schlacht  zu  liefern"  Bh.  2.7, 10;  Äci,  II,  _j.  lo**'.  3)'zumAbschlüss
11238:Zum  V.  'iar:  —  Pü.:  kattäraii.  —  0  So  nach Pü.;  das  Wort  könnte  aus  einem  Komp.  los- geschält sein;  vgl.  zu  'aril:     Unsicher. ■  p.  £artanaiy  Inf.  'zu  machen',  nur  mit hamaranam  'praellum  facere':  hauv  kära^ aliyavJ' . .  hamaranam  c°  . .  avada  hama- ranam akunavc^ . .  avdhäsäm  hamaranam kartam  Bh.j.9;  6,  7,  10,  J.  19,  2.7-12*. Zum  V.  >to-.     Vgl.    (gegenüber   WZKM.  g. 166}  IF.  4-  128,  KZ.  35.  61.
18888:Appellativ    folgt:    *parg<^    'mii'    kauft^ avadä  , .  Bh,j,  7;  7. 11;  —  tOzäm^  'mii' vardanam  Bh,  7. 19;  2.3,  6,  12,  16,^.1,  5. 6,  8,  2.  7;   —  AaÜa  piravJ'  •««"  rauür D.77. 3".        7)  ohne  Appellativ;  wir  über- setzen dann  'einer  namens  , .'  oder  'ein  ge- wisser"*': kt^baßya*  °»w"  kärausptth^^ .. püruvam  ida  lüäya^iyi^  aAi/'  'Bh.i.io;  — taxmaspad^  'md'  mSd(^  manä  b(^dakt^ Bh.2.i4;io,j.3,6,q,  i4,^i8*,S.7.      Ohne Wert:     darayj'vcTus     vistaspakya     'mi^ /«ä'a*    Ao.  7.  2;   2.        b)    nätm/*;    das Appellativ  folgt:  hauv  udapatalä  habiraav dubali^  -ff/j"  äahyaus  haca  avadasa^  Bh. J-»3;3.  5.  »o.  ^-»S-i-ö,  10, 11, 13;— /«fra* -Ma"  dida  arminiyaiy  avadä  hamaranam akunav<i'  Bb.2,8;  9,   7.13, _j. 9,  11. KompA.  (n^iH'),  E.  —  tä.  tUiman-  n.,  np.  nän. —  P6,i  näm;  s.  nOch  No.  3.  —  >>  Nur  in  nfiu, aber  hier  stets.  —  >)  So  alle  Hds.,  mit  jinei Ausnahme,   J  3,   wonach  NA.  'oif  bietet  — 3)    Fü.:    nndeaüichi    a/ä^i  addpnark  ann (Jamaspji  Gloss.  569  u.)  paakann.  —   1)  S. No.  6.  —  5)  Von  dem  es  nur  durch  ein  Ed- klitikum  getrennt  sein  kann.  — ')  Die  Frage, wie     ap.    t^amf    beim     mask.    nnd     neutr., rfiamt^  beim  fem.  Appellativum   formal   and syntaktisch    zu    fassen    sei,    ist    noch  nicht gelöstj  luletit  darüber  FoY  IF.  la.  171,   wo weitre  Litt.  —    7)  S.  No.  9.-8)  Vgl.  FOV aO.   174.  -^  9)  Fovs  Fassung  von  ßiräva*  aU Abi.,  aO.  176  halte  ich  nicht  für  richtig;  ich verlange  auch  hier  den  Nom.j   s.  Sp.  907  o.
23377:•  p.  vaNjmtsa-  m.  EN.  eines  Persers, Heerfilhrers/Ja^WL, 'ß/^f'iT^f;  -ja*  nSmd* mann  bd'daka^  Bh.2.9;  10,  11;  —  palis *sam  hamaranam  cartanaiy  Bh.  2. 10,  11.
24441:•  p.  vispa'^izatay-  f.  Name  einer  Stadt in  Parthien:  'tis  näma^  vardanam  paria- vaiy  avadä  hamaranam  akunavt^  Bb. 2.16.
28518:kauv  kära^  asiyavJ'  .  .  hamaranam  ear- tanaiy    Bh.  ^.  9.  2)    mit    Zielangabe
28645:—  femer  N.j',  Vyt.p,  23,  28,31,  4y,  Vd. 2  ff.  (oft).  [N.  43  aE.:  lies  yär).drä- jehim.]  hl  als  Part  sbes.  II)  Gen.- Abl.  p.  /a*,  j.  hB;  a)  im  Ap.;  nur (zuiück weisend)  in:  hatä  avadasa^,  sd. (Sp,  1 70  u.).  b)  im  jAw.;  nur  (zurück- weisend) in:  ja/.,  malyäka  ..  usi  pairi.- därayeiitli  dalma  hs  (näml.  gSul;_  fem.) pairi.urvtTisayei'iti  Yt.  14-  5Ö.  III)  nur im  Ap.  Gen.-Dat  Plur.  säm'^^\  zurück- weisend: avahs  hamaranam  akunatis hadä  hamih^iyaibii  .  .  avahäsäm  hama- ranam karfam  Bh.j.  i;  3,  6,  7,  9,  10, 2.6—10',  14,  16;  —  imä  dahyäva*  .. tyJ'säm  (fem.)  hacäm^  ahahyer  Bh./.?, D,  5.  3,  4;  Bh. /,  8  (wo  ydhäsäm);  — h(tram  . .  Uta  sä  m  '*'  /  martiyam  ma'histam akunaus    avahäiäm^''''    ahahc^    Bh._J.  9;
28646:—  adam  karam  frSisayam  . .  avähasSm '°' ähaham  Bh-_J.  14;  2.  6;  —  ''uvajtyS  avam martiyam  agarbaya"  hya^i/lm  mahista* 3ha*  uiäsim  av3jan<f  Bh.  2,  4; —  käram ..fräiiayam  taxmasp3dc^  . .  avamlam^"'' mahiiiam  akunavam  avahäsätn  ahahain Bh.  2. 14;^.  6,  5.  i;  —  ima  dahyavc^  .. adam/äm  (fem,)  x/aya'hiya*  3ham  Bh.  i.  6; D.6'.  3.  A)  der  Gen.-Dat  vertritt  den Akk.Ml;  das  Nomen  ist  zuvor  nicht  genannt, aber  es  ist  aus  dem  Zusammenhang  er- kenntlich; adam  ig  hamarana  akunavam vaina  a''ura''matd3he^  adamiäm  (zu  ß) ajanam  uta  9  xsaya%iya  agarbayam  Bh. 4.2.
29421:Zum  V.  "a»--.  —  ai.  Samara-  m.  'Kampr.  — VgL  hatnarana-  und  hamirAa-.  —  ')  S.  lu ^gan-  mit  fatiy.  Ei  geht  nicht  an  in  Qber- aeUen,  als  ob  die  letilen  Worte  hamaranä aiunau!  wären  (wie  Bh.  4.  i).  So  will  aller- dings Ali.;  aber  Eü.  weicht  ab.
29452:•  p.  hami^iya-  Adj,  (fem.  yä-)  'auf- rührerisch, abtrUnnig':  bäbirus  °y<^  abava* Bh.  j.  16;  —  parhava''  utä  varksnc^  °yä (NDm.)  ahavi"  Bh.  2. 16;  — /»iwaeia*  "uva- jiyS  °_>'5(NFm.)  abava"  abiy  avam  ä^''inam aiiyav^  ".  .  wurden  die  Suser  abtrünnig, zu  jenem  Ä.  gingen  sie  über"  Bh. /.  16; —  avam  k3ram  tyam  'yam  "Rh.  2.  6—11'', t4.  3-^,  3.  9i  10;  —  kära"  hya'^  °yt^ man3  naiy  gaubataiy  "das  Heer,  das  auf- rührerisch mir  den  Gehorsam  verweigert" Bh.2.  7,  10;  14;  — pasävJ'  'yä  ha"gmata (Sp.  501  m.)  paraitä  . .  hamaranatn  iaria- 1 naiy  Bh.2. 7,  lo,  _J.  10;  2. 8,  9,  11;  —  hauTj\ pärsam    'yam   akunaui  Bb.4:.3';  3*;    — |
```


## [2026-09-05T20:30:12.134Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -c . BRT.txt; grep -n \"paityära\\|paityara\\|paitiiara\\|paityar\" BRT.txt | head -10; echo \"=== col markers ===\"; grep -n \"^ *184 *$\\|^ *368 *$\" BRT.txt | head",
 "description": "Grep BRT for paityara and column markers"
}
```


### [2026-09-05T20:30:14.038Z] TOOL RESULT

```
30725
4115:FrW.  4.3;  —  'rahe  mainySus  dämanam ^'^  '5'  3i  —  y^t  titarat  °rS  matnyus dähim  alahe  .  .  antan  pairi.aväit^m  (sd.) fokuca  mattö  atarsca  /J  hg  taurvayatsm tba^ä  °rahe  mainySus  drvats  Yt  7_J,  7  7  f. ; 13;  — yint  nöit  tiurr/pttte  'rS  mainym nsit  yatavS  fairikssca  Vt  1^.44;  —  ailm dahakim..yqm..  drujim  fraca  k>rmlat  'rS mainyus  Y.(?.8;  —  aal  ahe  paityarim  frä- ijrMiat  'rö  mainyus . .V.l. 2;  'J0.3,Aog.2^; —  pairiAä  .  .  yä  uzdtihat  'rS  mainyuS  .  , paiHj>r)tSe  Yt,  A",  39;  —  taxm?m  urupi  .  . yat  barata  'tvm  mainyBm  framitim  (sd.) aspake  JaArpa  ^risatjm  aiwi.gämanam Vt./^.  29;  — paiti.psrme  'nm  mainyBm V, /o.  5;  —  fränämiliti  duhjarstavari'  °r3 mainyus  ax^amanS  Yt/p.  96;  3.^;  — naiHs  xsayät  °rö  mainyus  duzdalnS  FrW. 4.  a ;  —  xsnagiira  akurahe  mazdä  tarSidlti 'raAe  mainyius  Yt.  i.  o;  —  daxstanam  ydi Amli  'rahe  ntainySus  daxstim  V.  2.  29;  P, 2-2,  Y,  7i>,  11;  —  apayafUamah^a  'rahe mainyius  xrafstra  Yt.  21.1;  —  'rif  mainyus . .  dtävanam  daivS  V.  ig.\;  —  vJspB.mahr- käatca  pairi  drvatat  yat  -rst  mainyaot VL/_j.7i;  /0.118,  Y.2-j~-i,  V.'/o.ie;  — ai  duida  °ra  mainyS  V.ii).^;  g,  1,44,  lt. 10,  Yt//.  19; —  iaÖx  dusda  'ra  mainyö V.  i^,  1 2 ;  —  *'rahe ''  *mainy9us  duzdamanH Y.  Ö/.  2;  V. /p.6;  —  skutara  "ra  mainyö V.  79. 3;  —  "rS  mainyus  pouru.mahrkS (Stveri.)  Yt  10. 97 ;  usw.
5971:mit  ä  dnwS,  4  a;  yezi  näil  paitiiaraiti *%rl  vs  äsäiti  ayar»jiräjö  (sd.)  vä  vastryä£ N.  69;  ^2,  43,  <V?,  log'''.
6368:°v3  iJsrävayatgil'^S  aAuminxs  paityarmB Yt.ÄS9,  /4.S1;  Ä60,  74.52.
8506:•  j.  usad-  f.'J  — ?— I  eine  Landplage Baktriens:  bäxöim  .  .  äat  ake  paityar»m fräkimitai   atfrö   mainyuS^  . .  bravarjmca
16988:—  tä  (aimi. /ravasays)  el  starsta^  'möhu saoyä  Yt.  y.  a  7 ;  —  ys  'maca  ^frastfrinte gSulca  paitiiaraiti  ti.6o;6o;  —  %risum 'ma  frastjritmyA  paitila  hü  a^wansm  Yt. 12.  3;  —  ys  .  .  rapiUwiftfin  . .  fräyasäite
18975:•  j,  'n«inah-  n.  'Darlehen':  yS  natre  n»- mataAgnte  nBit  'mS  paitiiaraiti  täyus 'mariAs  bavaiti  AazaaAa  ivms.baraA£  "wer einem  Darleiher  das  Darlehen  nicht  wieder- gibt, wird  zu  einem  Dieb  des  Darlehens, zu  einem  Räuber  am  Darlehnsgeber"  V, 4.1.
27402:''  m.  'Träne, Weinen':  aal  ahe (näml.  haraevahe)  paityar^m  fräk^rmtal anr3  mainyus..  *'k?m^a  ifria'ii3(sd.ya  V. 7.8.
=== col markers ===
```


## [2026-09-05T20:30:30.250Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for p in \"hamsr\" \"ham3r\" \"hamir\" \"h a m\" \"aurvant-\" \"aurva-\" \"'ar\" \"ras-\" \"araeka\" \"araika\" \"ar>ka\" \"arjti\" \"ar3ti\" \"arinu\" \"ar>nu\" \"rana-\" \"rqna\" \"ar>%a\" \"ar^a-\"; do echo \"--- $p ---\"; grep -n \"^• *[jgp][.,].*$p\" BRT.txt | head -6; done",
 "description": "Grep BRT headword lines"
}
```


### [2026-09-05T20:30:37.010Z] TOOL RESULT

```
--- hamsr ---
5034:•  p.  ava'dä  {'da')  '\  j.  ava'8a  Adv.  i)  'dort, da':  \ patigrabanä  näma"  vardanam  . .  "da kamaranam  akunaus  Bh,  j.  ij  7,  9,  10, 2.6— 11^  16; — imaiy  martiyä  tyaiy  *ada- kly(sA.)  'da  aha''ta  Bh.4. 18;  j.  18',  2.  3, 6,J.4, 11,5.4;  —  didä  ..  'dasim  aväjanam Bh,  /.  13;  5. 1,  J.8'';  II  —  kva  .  .  °äa  bä  , . asne  hamsrihät  "wo  .  .  ?  .  .  dort  . ."  H.  2. 20,  *Vyt.54;  Yt6'.47>  Jp- 93>  N./5,  2^'; —  ''ha  agtaha  altahe  syao%nahe  ,  .  V.  4. 50.  a)  II  halä  avadas<^'''>  'von  da  aus': kami  udapatalä  bäbirauv  dubälJ"  namä" dahyäu/  halä  av  hauv  udapatata  Bh._j. 13;  J,  11;  —  hauv  . .  aÜyavaf"  paisiya- ^uvSdiim  haiä  av'  käram  *äyasatä  hyä''- param  *aif..  Bh.j.7  I ,  a)  'dorthin,  da- hin': U  raxa  rtSma!'  vardanam . .  'da  hauv .  .  *ä//Bh._y.6;  1. 19,  2.13;  — fravaSayS
--- ham3r ---
--- hamir ---
23978:•  j.  'vitar-  m.  i)  'der  nachjagt,  Verfolger' (mit  Akk.) :  'tartm  paskäi  hamirik»m  Jan- 1 iar?m  (sd.)  parö  dusmainyäm  "der  den Gegner  von  hinten  her  verfolgt .  ."  Yt  17. , la;  —  °ta  nama  ahmi  Yt /.  13.  j
--- h a m ---
--- aurvant- ---
5583:•  j.  airyö.sayana-  n. 'arischer  Wohnsitz,  .j^g. aurvant-, aourvant-" Adj. 'schnell; W.  der  Arier':  vJspjm  .  .  'fvm  Yt  10.  13.  tapfer,  Held':  '7-at"  F.  7;  —  /laomo  aeibis
6455:•  j.  *asta.aurvant-''  m.  EN.  eines  Gegners des  Viitäspa:  tarn  yazata  i'TsiOspS  .  . yaisa azäni  pplana  (sd.)    'vantö  (GS.)  Vt.fJ.jo.
28258:•  j.  '''zbaiirvataDa-''  patr.  Adj.  'von Ziaurvant-  abstammend,  dessen  Nach- komme': karsnahe  •tanake  Yt  13. 106.
28260:•  j.  zbaurvant-  m.  EN.  eines  Gläubigen: •pais  osaBTtB  Yt/J.  106.
--- aurva- ---
4775:•j.,g.am»rBta'^t-,  amarBtlt-'T.'Unsterb- lichkeit.  Ewigkeif;"'  tit  d^hnaotä  maslm hujyiH5is{sA)  "ntstascä  Y._j2. 5 ;  —  'rstSitl *a^aonö  urvä  also  (sd.)  utayütä , ,  Y.  43. 7 ; 48. 1 ;  —  yä  fyat/^an/t . .  -ntäbm  astmcä *taibyO  danhä  (sd.)  .  .  xs^nm^a  haurva- tätö  Y.34-^i  —  ahmäi  aahat  vahiihm yi  möi  vtdva  vaolat  hai~ilm  mq^r^m  yim haurvatatö  alahyä  'ritatasca  "dem  soll das  Beste  zu  Teil  werden,  der  mir,  ein: Wissender,  ktmd  tut  das  rechte  Wort  Aia^ von  der  Wohlfahrt  und  Unsterblichkeit" Y._3/.6.  a)  bes.  in  Dual  Verbindung  mit
12030:•  j.,  g.,  p.  'tar-  V.  'hinübergelangen  über  -'. Praes-S  /i/ar-,  2 ^taraya-, 20-^ x^taurva- ya-,  5  +  30  (Int.)  iitärqya-.  —  PPfP.  (W) t)r»ia'\  Jnf.  'tantayae-^a.  VgL  noch fratarta''.
14783:•  j.  (bisyant-,  g.  daibisyant-**  Adj.  'feind- lich, fcind,  inimtcus':  rapantl  .  .  at  .  . -yanti  zastäi/täi/ (sd.) . .  Y.34. 4;  —  aei'qm *°yafitqm ''>  . .  tbaesä  \t.jo.'j6;  —  aurva- 'äianqm  'yantqnt  Y.57.  a6,  Yt  J^.  31,  *Vyt. i^";  Yt  74.34,  ^■57-''f>\  —  aurvahafiiyS pars  'yanbys  Yt.  13.  69,  Y.  68.  13;  Yt.  10. 75,75.31;  — -  vlspim  aurvd^jm  °yanttm vXspfm  ay)m  °yant>m  A.  7,  10;  —  vanä{ vupe  'yantö  Yt  75.54; — pala  nS  'yantat pairi  SrB.5.
15718:•  j.  paourva  Adv.:  s.  paurva-  unter  I und  2.
15719:•  j.  paurva-"',  paourva-'',  pourva-'', p.  paruva- Adj.  (fem.  'va-)  'prior';  I)  dem Ort  nach,  r)  'der  vordere';  banlhBm  At vay&an?m  (sd.)  'rum'^  paiti.hincBa  V.S, 40;  41;  —  yaf  nä  'rva  (AD.)^  ß-aida (sÄ)  jrabdB.dräje  /rama&aiti  V.  i8.  40; — fra  mi  gahaa  tazayqn  nisbinla  (sd.)  . . 'rvaäbya*^  {riinA.  pataäbya)  V.  6".  37;  — aparaya  ..*'ruya*'>^  (LS.)  paüi  *mastrr]- naya  F.  9c;  —  *yatB  (sd.)  °rvatibya^'>  ya%a rdhaeää  V.ij.  45;  48.  a)  ISn.  paourva undASf.  paurvqn''^  als  Adv,  'vorn,  voraus'; mä  apama  *paourvitvaySit  (d.  L  'rva-\- avay*)    "wir    wollen    (ihm)    nicht    nach*
15747:•  j,  paurva-naema-"  m.  'die  vordere Seite';  nur  Abi.  'mal  'von  der  Vorderseite her,  an  der  Vorderseite'  sva,  1}  'vom,  vor- aus', a)  absolut:^«!  aM  °mät..ym paskät Yt.iS.2.  h)  mitG^a.: yeAAe  °m3t  vazaiU jvnihraynS  "welchem  voraus  fährt.."  Yt. 10,  Jo; —  ms^r)m..y5  tarU harqm  asnaoiii °tiist  amisahe  hü  ".  .  voraus  vor  der  ud- sterblichen  Sonne"  Vt./o.  13;  —  auirmja- yais  aom  srum  °mäl  ahe  gr-avaAe  "üa  soVisX befestigen  das  Blei(gefäss)  vom  an  dem Stock"  V.  §.  1 4.  a)  'kopfüber'  (?) :  'mät  '> paiai  dyaos^S^.  761  u.)  ..  artrö  mainyus Yt.,?.  13-
--- 'ar ---
3742:•  j.  apiäma.x'ar-  Adj.  'blindlings  essend': 'rS  (NSm.",  näml.  'ist  der  Hund')  yaia  |     "'  '  '■ t3yus  V.  /J.47;  47-  I  •  j-  aipy-öxSay-  f  'Hineinsprechen,  Ein-
4303:•  j.  an-aiwi5.x''ar«8'a-  Adj.  (fem,  -iJa-) 'zum  Genuss  ungeeignet,  ungeniessbar' : vtsprm  ä  ahmät  alsa  ä/s  ayaoidya  (sd.) ";jo  yavat  aisa  nasus  niibtrsta  V. Ö.31.
4389:•  j.  ana.x'arad'a-  Adj.  'ohne  Speise,  Nah- rung'; yal  at)hat  aitihä  zmiö  vi.äpö.- ttnumca  (sd.)  vi.urvarSi3minKa  ''^a  (ND.) ^pasu  vira  "wo  es  . ,  am  meisten  . .  man- gelt —  '>Tiere  und  Menschen  finden  keine Nahrung  — "  V. /o.  18.
5197:•  j.  avo.x'ar^na-  n.Tränke':  gaeyaoitis^a maSianyhsca  -näsca  Y.  2. 16;  — gaoyaoili- nqm^a  magiananqmla  "itanqm^a  Y.  7.  ifi.
5283:•  j.  'ara-  m.  EN.  eines  Gläubigen:  hr^- ziihao^  "rahe .  .  kasupitJus  "rake  "des  B. (AT.),  Sohns  des  A"  Yt.  13.110.
5303:•  j.  'ara-  Adj.  'mit  einem  bestimmten Gebrechen  behaftet':  andäsiit  kar?tMsca .  .  'rasca  (NP.)  YL5.93.
--- ras- ---
4251:•  j.  anaiKm  Adv.  'in  der  Quere':  cvat. . äps  yat  frätal,car}tayä  .  .  druxi .  .  /ras- naoilit .  .  ^rigäim  nyäpim  navagaim  pait- ySp}m  xsvas^aim  an'  ".  .  drei  Schritte stromabwärts,  neun  stromaufwärts,  sechs quer  über  den  Strom"  V.  tf.40.
14002:•  p.  duvitiya-  Adj.:  s.  unter  h()>a-.  ij^^jg^,.    ^^  ^-^.^^  aiwUruiaiti  ks  ras-
15831:•  j.,  g.  -paräU-  Adj.,  PPfP.:  s./ras-. KompA.,  E.
19229:•  j.  Diunizdö.t9ma-  Adj.  'der  (physisch) am  meisten  heruntergekommen  ist*:  dras-
25432:•  j.  räÖta-  Adj.,  PPfP.:  s.  ras-.  a)  ASn. •ttm  als  Adv.  'in  gerader  Richtung,  ge- rades Wegs':  r°  ahmäi  naire ..  tniisrU  maE- haium  (sd.)  äcaraiti  Yt.  so.  1 37 ;  F.  ly.
26639:•  j.,  g.  ^star-  m.  'Stern':  tainm  (sd.) httraihya  . .  yat . .  aiwits  urvisntti  staras- (NP.)'V'ä  mäsca  kvartla  Yt.  J2.  25;  V. '  2.  40;  —  slrfus{A2.)ca  mänhfmca  hvarna raocä  yazamaide  G.^.  6;  Y.  2.  11,  yi.<), Vtio.  145,  *V.  7.  52  (äs  Nom.)'>;  —  kuka . . yaosda'iäni . . ku%a  *strSus'* . . mänh>m . . hvart  V.  11.  \;  1  (als  Nom.),  10  (statt Abi.);  ~  kasnä  :^'Sng  *s/rfm(,GP.)äca  däl adväfam  (sd.)  Y.  44-  3 ;  —  ankam  (näml. fravasinqm)  raya  . .  hvan  . .  mh  . .  stärS ava  pdka  yänti  Yt.  i_j.  16;  FrBy.;  — fra- va^ayB  .  .  yä  strqm  mStthS  kür5  anayra- nqm  rao^anhqm  pa%S  dalsay»n~^\..i3.$T; V.l.  16;  —  Ääu  ma..  ave  stärö  V.9.41; Yt.  Ä  i;  —  tistrJm  ..yim  ratBm  ..vlspaisqm stärqm  Yt.  S.  44;  —  nittmalit  avaüqm stärqm  ya'ka  nars  malmyehe  va-^'hangm "selbst  die  kleinsten  jener  Sterne  (sind  so gross)  wie  der  Kopf  eines  mittelgrossen Manns"  'S. 4^;  —  ha(a  avaibyü  st>r^yS Ytj.  85;  —  slärqmia  sptntB.mainya'vanqm
--- araeka ---
5285:•  j.  araeka-  Adj.  -  ?  -,  Bez.  einer  Ameisen- art: maoirinqm  'kanam  kutakanqm  duzai- ninqm  V.  74. 5.
--- araika ---
--- ar>ka ---
--- arjti ---
--- ar3ti ---
--- arinu ---
28314:•  j.  zrayana-  Adj.  (fem,  °«J-)  'marinus': äp^m  xayanqtn  .  .  itffm  'nqm  ".  .  das Meerwasser"  Yt.  6.  2,
--- ar>nu ---
--- rana- ---
5329:•  p.  arana-,i.ar;>/ia-a.  'Sichbewegen'
5859:•  j.  asparana-  m.  Name  einer  Münze*>: °nS  F.  7;  —  duye  AazaaraAe  'nam  nidmat Vd.  6.
6900:•  j.  ahurana-  m.  Name  eines  Bergs  oder Gebirgs:  ahmat  haca  garayS  fraoxSyqn  .. 'nasca  Yt.  ly.  {.
7721:•  j.  «rszifyö.parana-  Adj.  'mit  Adler- fedem  besetzt":  isavasca  'na  V.  77.9;  Yt. /0.39,   lOI.
9242:•  j.  'karana-  m.  'Ende';  i)  räumlich:  "des  gläubigen  H.,  (aus  der  Familie)  der 'Grenze,  Rand;  Ufer;  Flügel  (des  Heeres)';  A'."  YL/j.ia?.
9332:•  j.    'karana-  m.    Ohr',   uzw.  rfnÄ^ischer       haben;  vgl.  Yt.  ,0.  125.-»)  Anders  freilich Wesen":    lai  drvalö   drvatyiisca    asi    usi ■     Dk.  /.  4.  44  (SBE.  47.  59). 'na{Kp.)gava*dvari>mzafar»..pairi.-\^    .     ^^^3-    V.    'ausschütten'.    Praes.    2 urvalit^m  (sd.)  Yt.//.2.  ,_(.^„^._  _  pp^p^  ^^„y^._
--- rqna ---
26373:•  j.,  g.  suxra-  Adj.  'rot',  vom  Feuer:  äal he  Jm  zh  bvat  pirane  .  .  ährqmca  'rqm  " saoantqm  "voll . .  und  von  roten  flammen- den Feuern"  V.  2. 8;  —  Sica  S'hrS  'rä (IS.)  .  .  vaahau  vidäta  rqnayä  (sd.)  Y. 5/.  r9;5/.9.
--- ar>%a ---
--- ar^a- ---
2966:•  g.  aoz-  V.  'achten'.     Praes.  i  uz-.       \     näml.  Kavay  Vi,,»-,  vgl.  Dst.  ZA.  j.  39. 'achten  für  -',  mit  dopp.  Aklc. :  ki  kvö  ,  j.  ao§ö.tara-  Adj.  'der  verderblichere,
3097:•  j.  a;'rae'ra9^-  m.  EN.  eines  Gläubigen, eines  Bruders  Franrasyan%:  "'^aAe  nara- vahe  alaonö  Yt/^.  131;  —  puirS  kaoia (sd.)  syävarsänai  .  .  ""^ake^a  naravaht ".  .  und  (als  Rächer  des  Ä. . ."  YLf?.i8,
3244:•  j.  aSara  Adv.:  s.  t^ara-.
3245:•  j,  aSara-  Adj.  i)  'der  untere,  unten  be- findlich':   'rO  F.jg;  —  -rat  naimlt  "an
3251:•  j.  aüara-naema-  m.  'die  untere  Seite'; nur   Abi.   °mit  'von   unten   her,   unten':
3255:•  j.  ajlaram  Adv.:  s.  t^ara-.
```


## [2026-09-05T20:30:52.961Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '5280,5345p' BRT.txt",
 "description": "Print BRT ar- region"
}
```


### [2026-09-05T20:30:53.015Z] TOOL RESULT

```
frsrtnaol  Sl.  //.  6Z.;  —  //  abys  frpr^la (sd.) !  udapiUat.
/rSr?nvainH*'> . .  fravaUbyS  Yl  JJ-  46 ;  —  \       karir maiiraca  spftita  . .  yim  zarakuilrö  frSre-  .3-  ^3-
aratufri-  1 86
•  j.  'ara-  m.  EN.  eines  Gläubigen:  hr^- ziihao^  "rahe .  .  kasupitJus  "rake  "des  B. (AT.),  Sohns  des  A"  Yt.  13.110.
Wohl  Kurin.,  ob  für  •aruma/a»- (ä™-)?   Vgl luSaämailya  Vi.  /J.  139,  %rasdälöii  YL  rj.  II5.
•  j.  araeka-  Adj.  -  ?  -,  Bez.  einer  Ameisen- art: maoirinqm  'kanam  kutakanqm  duzai- ninqm  V.  74. 5.
Pä.:  iik;  Transslcr.? p.  arakadris:  lies  aria'.
•  p.  araxa-'}  m.  EN.  eines  Armeniers, der  sich  gegen  Darius  I.  empörte:  °xe^
arminiye^  hülditahya  pui:''^  hauv babirauv  Bh.j,i3;  4.t,  Bh.i; .  abiy  avam  °xam  aUyavJ'  Bh,
naet"!^  kv3vant3m  (sd.)  anhve  asfvaite  Yt. y.  146.  2)   'gewährleisten,   zusichern,
zusagen';    yeAhe     *nisritlm    (sd.)    fr3rit (jSPfA.)   *ä  ki  *anitritlm  {slaryäü)  yai
denken verbietet  die  DifTereni  x-k'. j.  a-ratav-  Adj,  'der  keinen  Ratav  (sd.) aifmaoyanqm  .
.   anahunam  'tunam
äat  hensit  ^msritlm/rära  nöit  ÜinuritTm  '  ^^.'ß-  '°)i  "  *"«««'"''•?  (sd.)  'ivö  (GS.) "  ......         ^  lasfsm  duzatihavo  V.14.
Pü.:  aranh.
astrydti  "wenn  er  seine  (des  Knaben) Anvertrauung  zugesagt  hat,  so  begeht  er Sünde,  wenn  er  ihn  (dann)  nicht  anver- traut; wenn  er  aber  seine  Anvertrauung nicht  zugesagt  hat,  so  begeht  er  durch Verweigerung  keine  Sünde"  N. /ü**.
gT.  äpia/iai  leb  verächafle  mir'^),  arm.  afnuni Ich  nehme'7);  ai. /-fiartt?).  —  PQ.  (zu  SimpL  1): iartait,  (la  SimpL  3):  iavamlai«},  (za  Y.  //): /ranäß(i),  (lu  N.  lo):  /rä!  dakil.  _  i)  S  154-  - »)  NA.  aröi;  s.  aber  Pt4  und  BB.  /J,  150, — J)  Pil. :  bttvandai  an  i  hadänäk  ie  fa  kan'isf iArmazJ  S  Smäi  tut.  —  4)  S  3O4  II.  a8.  — s)  S.  «St  Bthl,  IF,  12.  114,  —  6)  Eig.  'ich lasi«  mir  in  teil  werden';  s.  No.  5.  —  n  Aus dem  Medium,  s.  No.  4.   VgL  ai.  däJämi  und
-  »)  S.  :
•  j.  ^ar-V.  'figerc'.  Fraes.  2  ara-.      PPfP.
Med.  'sich  festsetzen,  stecken  bleiben': yaica  alte  asti  datahva  arinle  gar>mskva (sd.)  vfoänte  V.  s^.  4.
mit  aipi  'defigere,  fest  bestimmen': s,  *aipijr?i3.'.
mit  aiwi  dn.:  s.  aiwi.>r>i!!.'.
Vgl.  gr.  Apapatia,  ai.  orfiyati  'infigit'.  —  Pü. (in  V.  /j)t  lisst  das  Wort  aus;    s,  noch  die
•  j.  'ara-  Adj.  'mit  einem  bestimmten Gebrechen  behaftet':  andäsiit  kar?tMsca .  .  'rasca  (NP.)  YL5.93.
El?')  —  DsT.  ZA.  2.  389  'ladte';  Gdn.  KZ. ^5-  395  'Knicker'  (was  schlecht  passt),  — ')  Es könnte  HaptoL  vorKegen.
j.  araßJiiri&inö  F.  /:  lies  arilS.kar>%iiö.
•  j.  a-ratu'xSaSra-  Adj.  (fem.  'ra-)  'dem Ratav  nicht  Untertan,  ungehorsam':  jahi- kayni  .  .  -rayäi  H.  2.36.
Pü. :  aral  lyaläi.
•  j.  a-ratu'fri-  Adj.  'der  nicht  r.  ist,  die Ratav  nicht  befriedigt,  es  ihnen  nicht  zu Dank  macht,  gegen  ihren  Willen  ver- stösst':  äahms  zaota  dahmS  upa.sraolärü vispe  ratu/ryö  tanupirii^ö  zaota  tarnt- p>r3%5  upü.sraotltrS  vupe  '/ryüti.^i);  — yai  ig  däiti  dalätH  ^rafufrÜ . .  yesi  aal hSnDit  däiti  daoäiti  '/ris'ü.io^;  wo,  loi'^, S03, 104,55,  *55  ■';  — yi  ^ri/*Aa>räricS yätayeinle  ratufryS  yai  Hat  (ä-ri/)  nSii *Aa>r.'rtci>  yataytinti  'fryO  N.  S8;  gj,  gi, 9-',  93>  95;  —  y^i  •  ■  »o  ratu/ryö  yezi *aai  .  .  uva  -/ryJ  (ND.)  ü.$4;  —  yai arastnm  (sd.)  .  .  pairi.iioa  .  .  °/rya  pasca vä  pars  vä  pairi.ä6a  °/ryS  ii.32;  —  yä yastam  *yazfnti..  nva  *ratu/rya  Aam.srul.- väcayala  (sd.)  ^yax^nti  *«va  *'fiya  (ND.)'' N.  24',  — yö  aiwyänhayäiti  kar>tSsca  °/ryS pasca  aiitiySstim  nitaohydti  ratufrys  N. tV^.  a)  mit  Gen.  dessen,  wodurch  (und wofür)  man  ar.  ist  oder  wird:  yasnahe advakt  (sd.)  ratu/ris  'frii gä'iianqm  N.22; —  kaithqm  ml  gä'^anqm  srutanqm  °/rii3 yä  ^maizö  vä  . .  *srävayeiti  aetaesqm  vacqm "fris  "mit  welchen  aufgesagten  G.  verstbsst
dby  Google
i87
"araityato
man  gegen  den  Willen  der  Ä./i'  Was' man  pissend  oder .  .  rezitirt,  mit  solchen Sprüchen  verstösst  man  gegen  den  Willen der  H."  N.J7;  —  aSaisam  vacqm  *'/ryO N-  33-  [N.  25,  103  2.  St,  105  I,  St.,
loft':  lies  ratujr'  statt  aratu/r*.
Pü.!  aral'ihä.  —  0  Hds.  artn/r-,  —  ")  So  T. —  3)  Dh,  'wie  darf  man  die  G.  nicht  auf- sagen, wenn  man  nicht  gegen  den  Willen  der fi.  Verstössen  will?'.
•  j.  "araityatö 'J  Vyt.5.
Pü.:  hae  iavandai.  —  ')  Mit  Var.
•  j.  a-ra9Twya-  'unzeitig;  unangemessen, ungebührlich':  'wya  daxsta  "wimla  gar)- m3um  V. /.  18;  17;  —  ra%wyanqm  .  . syaohnanqm  . .  aoäityanqm  •wyanqm  dui- varstanam  iyao^nanam  Vr.  15.1;  —  °wya Vyt.47'-(?),  4^C?)-  '
KompA.  —  Pü. :  afiiröii,  (zu  V.  /)  erL niailat,  (^garmVi)  i  freh  hac  palmän  bav
•  j.  a'raS'wyö.b^rste  Inf,  'ungebührlich zu  behandeln':  *äri-jümea  drtvim^a  ar°'' barjmne  (sd.)  "den  Armen  und  die  Anne, die  ungebührlich  behandelt  werden"  P.  26".
Zum  V. 'Air-.  —  Pö. :  kilänpa  apärön  bariinih buri  estinä.  —  ')  Vgl.  lAusdr.  unter  hubiriß.
•  j.  a'rad'wyö.manah-  Adj.  'ungebühr- liches denkend':  vTsp^m  ay?m  . .  'nanhsm A./.io;  —  drvatqm  'nattkqm  Y.ö'/,4.
•  j.  a'ra9'wyö.va£ah- Adj.  'ungebührliches sprechend':  vfsp?m  aytm  . .  °^anh)m  A. 7,10;  —  drvatqm  ,  .  .  caahqm  Y.hi.^.
Fü. :  aparön  g&aiiin, j.  art&wytS.varlli  P.  28:  lies  riA-aiy'.
•  j.  a'ra9wyo.Syao9tia-'>  Adj.  'ungebühr- lich handelnd':  vJsp?m  offm  . .  °'in»m  A. i.lo;  • —  drvatqm..  ''kmartqm  \.6i.4.
Pü,:  apärön  kuniht.  —  O  Y.  61.  4  '%iaa'.
•  p.  arabäya-   m.  Name   eines   Lands,
'Arabien':  imH  dahyavc^  tyä  adam  agar- bäyam , ,  'y^  0,6.3;  5-'i  Bh.r.6.
j,  araiih(\m  dürc-paitim^m  Vyt.  2  stall;    ra i^hifm  dürafpjrqm ;  s.  Ai.  4.
•  p.  arana-,i.ar;>/ia-a.  'Sichbewegen'
KompE.  —  Zum  V.  'ar-.  —  ai.  arana-  n.
•  j.  aravaoätra-  m.  £N.  eines  Gläubigen: •ra^e  prjzavalö  asaond  Yt  jy.  124.
Komp.;  'a-rafa--\-iiiliii-,  eig.  'unflinke,  träge Kamele  besitzend';  Bthl.  IF.  S-  358.
•  j.  araska-  m.  'Neid"':  ttsit  zaurva  . . m?r?hyul  nöit  'k3  daSfö.äatS  Y.p.5.
lEt,  t.  ai-jsytint:  —  mp.  (Pü.),  np.  ariitk.  — 'I    Trad.    und   Et.   weisen    auf  'Neid',    aber
•  j.  arastram  Adv,  vll.  'unebeomässig, stockend,   bald  rasch  bald  langsam':  yS
srSvayanti  yat  "rym  ^pairi.aoxta pairiMa  va  ", .  wenn  einer  sie  beim  Vor- trag stockend  aufsagt"  N.j3.
Et.  und  Bed.?  —  Wohl  AvyVioTap.  mit  >a'.  — Pü.  X  hakar  tuvätt  üfie  g^wisn  ape  gffivZt  (?).
•  j.  a-rätay-  i)  f.)  '(Nichtschenken,)  Geiz': vainit .  .  räitis  'rsiffm  Y,  60. 5.  z)  Adj. 'geizig;  Knicker':  paitUtatse  . .  'rälSisca fag^B.m»r»neyanaAe  Vty.  137.
ai.  ärälay-  f.  —  Pü.:  nirätih.
j.  a-t^itiVant-  Adj,  'geizig,  Knicker": yU  °tivä  . .  Um  aoi  ibaää  paityantu  Y.
ai.  TgL   aräthiän-   Adj.    'feindselig'.    —    Pü. :
•  j.  arä^av-  m.  Name  des  vor  dem Zaotar  stehenden  Steintisches,  der  den Morser  und  andre  Opfei^eräte  trägt*': jautorj  (sd.)  däitys  gätui . .  mat?mäi  °raet apa-sritd  N.jS.
*)  Auf  dem  Plan  der  NA.  lu  Vr.  3  luhrt  er den  Namen  urz-is  (s.  dazu  DsT.ZA.  /.  LXIU  und SWienAW.  fy.  837.21:  urvti  gSk  Jät  i  yadiit gäh,  846-  8 1  sang  i  urvü  sang  i  yaziin  gäk  ki J/ät  i  yaäsn  bar  ü  nihand',  jetil  heisst  er  laxt i  äläi  'Gerät etiscb';  s.  noch  Pü.  Die  darauf ruhenden  Gegenstände  verzeichnet  DsT.  aO., Haitc  Essays*  3^.
Et.?    (Ob    richtig    überliefert?)   —    Pü.:    «Ä/
diu. j.  *ar5t  niümät  N,  ^l  T:  lies  anlaräi  «*.
```


## [2026-09-05T20:31:05.753Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^ *[0-9]\\{3\\} *$\\|^i8[0-9] *$\\|^ *18[0-9]$\" BRT.txt | sed -n '1,5p'; echo \"--- headers near 5150-5285 ---\"; sed -n '5180,5285p' BRT.txt | grep -n \"^[0-9i][0-9]*\\|  1[0-9][0-9]\" | head -20",
 "description": "Find BRT column headers"
}
```


## [2026-09-05T20:31:06.901Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=5100 && NR<=5285' BRT.txt | grep -n \"ar-\\|'in  Bewegung\\|Bewegung  setzen\" | head -20",
 "description": "Find Avestan verb ar- in BRT"
}
```


### [2026-09-05T20:31:07.607Z] TOOL RESULT

```
4136:107
4150:109
4407:113
4410:124
4533:130
--- headers near 5150-5285 ---
14:•  g.  avöi  Inteij.  'wehe!',  als  SubsL:  asifyj affhlu^  177'°  ari/ial  apsmim  "denen  wird Wehe  werden  am  letzten  Ende  des  Lebens" V.45-3-
17:i)  Nach  Gdk.  KZ.  28.   187   und  Dst.  ZA.  2. 671  wire  avö  Praev. j.  aviirisyäl:  S.  un-ti^s-.
19:'Eig.  (aU  Adj.)  'WässerCm-'oA-jgcnuss  bietend'. Vgl,  GON.  KZ.  2S.  186  (gegen  Hbu,  PSt,  5). —  Pü.!  äp  j^ar,  Sü. :  i'OT-iiw  t«M/(i  (wozu Sp.  Komm.  2.  68).
23:i.  flj'ff'
24:•  j.  avi,  aoi  I)  Praen.  1)  mitAkk.;  a)  'auf —  zu,  hin  zu  —  (auf  — ),  advcrsus',  a)  bes. bei  Wörtern  der  Bewegung:  tiltrim  . .  yö .  .  vazsite  'i-i  zrayS  .  .  ya>a  tifrii  yim anhat  irsxsö  .  .  airyd.x^ii>a(  ka>a  garöit x^anvanhtn  'vt  gairjm  YLÄ6;  H.  2.  i6^ Yt.5.85  ('oi),  132J  ('ei),  Ä33',  70.151, ;p.8z  2.  St.,  V,7.i8  PüZ.,  5,19',  <.V.i03, Y.  6^.  3  (°oiy,  —  nä  tai  frasusaiti  haca /qfnavö  raonqm  'vi  bansiiavS  gairinqm V.5.2;  i';  —  ^J  .  .  vTjasnt  vlspais  ''vi karh-qn  Yt/0.89;  64,  72.4*,  7^.94,  Y, O5.I  (Vi),  0,5.5  ('<»■>;  —para.aki  upa.- vazat3uha  °vi  nmärum  ..  V.  22, 7;  13, Y.57.23,  24,  Yt70.3o;  —  urvänB pärayänli '  °i7  ahurahi  .  ,  "vi  atmsanqm  .  ,  °vi'^ \gätvS  .  .  'i'i  gars   nmätam  Y.  1^.32;  —
26:i8i
29:183
35:9. 1 1.  d)  'in,  bei'  (auf  die  Frage  wo?) :
59:fialmänak.  —  ')  NA.  getrennt. •  j,  avi.mi9Tanya-  Adj,  (fem."_va-)  ^Mi>ra- feindlich':  yat  a'^ra  para./asaili  ..  ya%rii daiAMvü  'nyä  Ytro.  101.
66:Zam  V.  vaia..  —  PB.:  afttr  vamit  (3S,),  di die  Erl.:  hUr  (oder)  nasäk.  —  »)  And deHarüz  BB,  2J.  191.
70:Zum  V.  ray;  —  Vgl.  airilay-.  —  Pü. ;  apar tiyil  (3S.;.  —  0  Anders  (filseh)  deHaklez BB.  25.  191.
73:i)!'hingelangen, hinkommen  zu —'(Akk.): yätä  adam  arasam  misdam  "bis  ich  nach Medien  kam"  Bh.  2. 6,  9,  11.  a)  absol. 'kommen';  yätä  adam  arasam  "bis  ich kam"  Bh.  /.  13.  II  2)  'etwas  hingelangen lassen  zu-  (Akk,),  bringen  über  -':  Jratu^' r/  dvafsS  (sd.)  hvö  d^ritl  *fn?r}xhyaosX.
83:-  'ar-  184
94:i85  *ar-  mit  wj
105:Wohl  Kurin.,  ob  für  •aruma/a»- (ä™-)?   Vgl luSaämailya  Vi.  /J.  139,  %rasdälöii  YL  rj.  II5.
```


### [2026-09-05T20:31:09.804Z] TOOL RESULT

```
26:•  g.  avar-  n.  'Hilfe',  mit  Akk.  verb. : ahurä  na  na  -varS  "o  AIi.^  nun  werde uns  (den  Rindern)'»  Hufe"  Y.2J..  11.
41:Komp.;  aiar-  oder  a<:ar>\*%,nl.ak.  n.  (vll,  zu  | abvmr.  trdi  'Wohnung'  usw.);  eig.  Bed.?  — , II  SBE.  47-  Sjf..  37-  30;  das  Wo«  ist  aus «iner  nicht  mehr  vorhandenen  Aw. -Stelle ' tierüberge  nomm  en.
66:KompE.;  Ablelt.  —  Zum  V.  aw-;  s.  avar-.  — ai.  äi/as-  n.  —  Pü. :  ayäuiänh ').  —  ■)  Die hier  (oleenden  DS.  in  infinitivischer  Verwen- dung. Vgl.  iB.  ai.  Az/fl>ä™  .  .  flj'o«  RV.  /. 35.  i.  —  >)  Zu  Y.  so.  I  nndeullich.
88:Pü. ;  atiarüHr,  erl. :  aht  inö-j. j.  aväiltyata,  'ye'ilf  \  s.  'slar-.
152:•  j'  %■>  P-  '^"  '(sich)  in  Bewegung  setzen'. Praes.  i  ar-:in-,  5  /ya/^'' :  i^r-'>  14b. rasa-,  30  (Kaus.)  araya-.  —  PPfP.  "»nta-, Inf.  ^"irndyäi'^y  'Ire,  'gntJe,  'tntöU.
162:m\X  frä  i/rö)  1)  'herankommen':  iadä .  .  yöi  uxsän^  (sd.)  asnam  aahsus  dar»- ^räi  frö  alahyä  frartm  (3PKM.);"'  Y. 46. Z'         2)  Kaus.  'in  Bewegung  setzen:
163:-  'ar-  184
168:ai.  Srta-.raiUa,  iyatti :  irle,  fcchati;  np.  rasaii 'er  kommt'.  —  Pü.;  verschieden,  s.  No.  4,  5, 8-11,  14.  —  ')  S  I03  I.  1  c,  ii6.  IF.  3.  69. Statt  'yiit°,  d.  i-  iyar-,  wird  auch  "ayar"  und •yS.r'  geschrieben,  S  afirf.  11,  57.  —  »)  Statt fr*.  S  sö'if.  1.  K  I,  L4  haben  anch  V.  21.  5 («ira.  — J>Them.— 4>Pü.!  S/tctid,  ?,\i.:  falatili.
169:—  ä  Statt  z-I-yar-,  them.  —  *)  ä-\-arrm.  Pü.: bavandnk-,  vgL  arim.  —  7)  Them.;  doch  s. L4,  K  I,  wonach  vU.  'riti  zu  lesen.  Vgl. "«=>'».  —  ^Vü.i  iu/anJ  ii^an.  Vgl.  'ay-Ko.lJ.
171:frmmmfnd,    ?&.-.  frahrui-anlil^).    —    "3)^1311 *nh-al\  Btml,  IF.  ts.  :o6.  —  >*)  Pü.:  undeut- lich, wohl  Transskr. •  j..  g.  'ar-  V.  'gewähren'.     Praes.  10 snnav :  3r3nv—,     PrP.     tn/iavi'^;     Perf. PPfP.  Jr^/Ä-  (s.  /r»-). )    'gewähren'     sva.    'zu    teil    werden lassen':  Aa  ahmai  aus  Prvnävi'^  "welches Los  wurde  ihm  zu  teil?"  Y.5.3;  4;  — ■a'^a   nS   masistasca  .  .   asayö  »nnavanie (3PKM.)    Y.52.3;    —     asöii..    yä    ni äras'il  (sd.)  jnnavataeca  (3SKM)  Y.fö^. 3.  2)   'gewähren'    sva.    'gewährleisten,
174:i85  *ar-  mit  wj
```


## [2026-09-05T20:31:19.471Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"  36[6-9]$\\|^36[6-9]$\\|  36[6-9]  \\|36 8\" BRT.txt | head -20",
 "description": "Find BRT column 368"
}
```


### [2026-09-05T20:31:21.287Z] TOOL RESULT

```
4116:KompA. ;  Ableit.  —  Aus  ar.  *aira-,  lu  einer  ar. Basis  'ans-;  s.  qita-,  ariia-,  ahifrailay-  und Bthl.  BB.  S.  22o;  S  2^  No.  1,  woiu  noch Wilhelm  Mus.  8. 123.  —  rop.  ahraman,  arm. LW.  arhmn;  s.  dazu  Hbh.  AGr.  /.  26.3)  — Pü. :  dnnak,  bei  den  Paisen  ^a»ä  gelesen; ich  lese  versuchsweise  niräj,  IF.  /2. 93i  Sale- MANH  GliPh.  I.  366  will  anräk.  Sij. :  hanlä. —  I)  Vgl.  No.  Z.  —  ")  NA.  angr';  s.  Var.  — J(  ^p.aArT/nan,  gt.'Apnnävnf  setieo  eine  urir. Nebenfoini  *ahri}it-  Toraus.
7889:365  iätt  —  ifrra  366
11375:—  aiatcjt  haca  Y.2p.  6,  27. 13;  j4. 13;  — hurayasHl  aoa  . .  daidyal . .  astmanqmcit ' . . K.3.4V,  —  aiwi.niticit  .,  span:>m  ..  aisa druxs  .  .  apadvqsaiH  V.  Ä  16;  —  tut  RS ttäcit  vansansY.51.1;  —  zusammen  mit U  (Sp.  367  o.,  586  o.):  f<M:"J«(sd.)  ..ya zl  vävfnzöi  pairl.cihlt  .  .  yScä  var?saiti aipT.ä^Tt  Y.  2g.  4;  —  bei  Zahlwör- tern: spiimm  zairitpm  .  .  xsvaiayacit  .  . vTväoayantu  \ .  8.  IT,  iS'^';  —  puxhmHl nä  arydu/qm  tanBm  ptrydte  V,  4. 17;  — para  mS  .  .  'hrifSt"^  vahista  .  ,  vlsata (sd.)  P.  J5; —  %risHi"'>  ..  hamahe  ayqn Vyt  41;  —  bes.  beim  Pron.  pers.  und dem.:  haxsaya  azsmat ys zara'kustm /ra- timq  .  .  anumatayaica  ..  Y.8.  7;  — pairi ml  tümcit  dayä  kaoma  . .  vahistptn  ahQm Y.ii.\o;  jo.  I9(?),  Vytj;  —  tun  vaimlit yazamaide  YL75.  i;  1;  —  ciknm  bsil yüi>mcil  :^armS . .  ääyaia  Ny.  J.  1 1 ;  VyL •S';  —  Aasat  va  nsit  vä  "der  (kanns)  oder (es  geht)  gar  nicht"  Yt/^- 20;  —  Jrä Mmat  nidar^zaypn  V.  J^.  31; —  tanu.mas5 (sd.)  zX  *altqmcit  alayqm  *pqfre  yat  ,  , P,  i8\    —    mä    ml   aetayasa£    tao^rayä
12430:V.  18.  \;  —  axstaäta  'naya  vaca framrü  Y.J.  i;  —  zara'ku/trahe  'nqm  .  . lannsmca  tka^jmca  Y.iÖ.a;  —  vaehä •nyä  FrB.;  —  'nqm'^  ..  dät>m  vTdsyBm  V. /p.  16;  —  mq'hraAe  spmtahe  .  .  'nayä  .  . staolanam  yesnyanqm  "Vt-O-T,  —  'nayä .  ,  dhaurunqs^  rähaßtäs^ä  västryqscä fhtyantd  Y,  y,  3 ;  Vr.  J.  5 ;  —  ytzi  'nyä  . . ai»Aai  (Sp.  270  o.)  Nik.  /;  2;  —  AäyaoidA yä  'na  V.5.21;  j.42,  Yt  JI.  3,  Vyt^j; —  °na  . .  nars  aiaonS  fram>maiti  vUpim dulmatimca  . ,  V.  j,  42;  —  'na  . .  p3r?näyul cihqm  %wfnsaiti  W.j.  41  (?).  a)  meist mit  einem  bestimmenden  Dem.-Proa  oder Adj.;  n)  'a-,  ^ada-,  ima-,  Y.  S.  7,  g.  31, 60.  2,  Vr.5. 3.  Yt  y.  99  (Sp.  2  u.,  3  0-); N.  ji  (Sp.  32  «.);  V.J.  30,  Yt  S.  59  (Sp. 368  u.,  369  u.).  ß)  ähuray-  und  sara-
12958:nidanzayen  "an  ihm  (dem  Maul)  sollen sie  es  (das  Stück  Holz,  Sp.  367  o.)  fest- machen" V.  y.  31.  b)  mit  Dat  'fest- machen gegen  —  hin  sva.  davon  ab- sperren'; paoiryäi  (näml.  sBni)  nidan- taysn  apirmayükim  ava%a  atrftn  "von dem  ersten  (Hund)  soll  man  die  Kinder absperren,  de^Ieichen  das  Feuer"  V. 0--48'".
14017:üTöya  *druianti^>  ,  -  /'"'»»"■fW-r/i  (sd.)  xhronpratendenten  und  Empörer,  also ■  AavaAe  untn5  dnäaite  N.S4;  —  II  Aau7'\  j^it  politischem  Anstrich'':  'ge^dis  hami- adurujiyä'  ava>a  diahi^  Bh.4.2';  Bh.!\'-,yi  akunaus  /ru*  imaiy  (Sp.  369  m.) b-j9;  _  vlspim  vamaiti  (naml.  7in>r&)  käram  adurußraitT  "die  Lüge  machte  sie druziiiüm  Yt  10.  loy.  a)  I! 'Jemandem  .  abtrünnig,    weil  .  ,"  Bh.  4,  4;    —    *ga*'^
17171:—  ')  zKonstr.  s.  'aA-  Sp.  369  n. ;  (aUch  KZ, SS-  los;  iSt.  a.  Vr.  7.  9,  a.  11.
19043:V'5'55;  —  "°  f^'"*  ■•  oi^he  ayqn  tv  yl  hsi  n'  vTdaitl  (sd.)  Y.^i.6;3i.9]  — ai^ha  xiapS .  .  avasyäi^'*  n°  akav5  n"^ ..  a£  yastSm  n°  nä  isimnS  ayJt  (Sp.  150  m.) Yt.7.18;  —  «*  gähahe . .  tbaisö  frqstiSna  Y.46.6;  —  ysi  im  fJ  «°  i^a  mq%rtm (Sp.  595  o.)  /rasftuyat''*  Yt  11.  S;  §';  —  vanfyfii:  (sd.)  Y.45.3;  —  mit  Ellipse  von yäii  tl  ml  nöit  äaioTi ..  n°  mZ  ita  *ärihäi.-  astl:  yaT  aÜ  n°  urväta  (sd.)  advä  aibi.- fom'^  (Sp.  369  o.)  *pasu  vira  .  .  n'  pas-  dtnita  vahyiX.Sl.i;  —  es  ist  die  Verbal- c<^a  .  .  upa.dayafi^  aarS  mainyu/  Yt  form  des  vorhergehenden  positiven  Satzes /^.  izf.  zu  I  a);  mit  indikativischen  zu  ergäDzen:>J  m  ^^J/^i?^(5d.)^JV^/(sd.)
20800:dehung    ist    ungenau :    avaisqmca    pa%0 pinis    yim     issnti     mt'krö.drujB     Yl  10. 4S".       ß)  adjektivisch;  nur  NSm.  mit  nä (Sp.  1200  o.):    aom  nar»m  .  .  yS  nä  ma- zistim  yasn>m  yazäile  YL  /.  24.        i)  ima- (Sp.  369  m.,  371  0.);  das  Relativ  ist  sub- stantivisch; a)  im  gAw.;  zu  2);  imqm.. .  .  ya  nä  baraiti  Y.jÄ  i;  verwendet Y.13.1.        B)  imjAw.:  imqm  tanUm  yä ml  vagnaite   huraoia    Y. /o.  14;  —   tme :a  .  .  ySi   hfnli  .  .  bisämrata  V.io.  2'; *imqm    va^S  ySi  anhin  .  .  V.  5.  27;
21103:ai-^uV;;  S2J2.Ä  —  Vgl-  '>^:i'-  —  Pö.  (furj'-  a): cc  haiar»),  Npü.;  eirä  a,i;ar.  Sä,:  ya/B  yai/i. — O  Siels  mit  folgendem  n".  —  ')  So  auch  -  at statt  «m  t  -  Yt.  6. 3  lU  lesen?  —  3)  Unsicher; s.  aber  j'fl^J,  Sp.  1245  o. •  j.  ya'S'a,  j.,  g.,  p.  ya&ä  Adv.  imd  Konjn. Die  korrelativen  Demonstrativa  (Stverz.), die  im  Übergeordneten  Satz  erscheinen, ferner  °cit,  "fVj' (Stverz.  Sp.  590),  das  hinter y,  und  miinay)n  {ahe  oder  bä;  Stven. Sp.  1123  m.),  das  in  Verbindung  damit ■  id  durch  Sperrdruck  hervorge- hoben. I)  vergleichend;  I)  die  Aus- sage des  ^y'-Satzes  gilt  als  wirklich:  'wie, so  wie,  gerade  wie,  entsprechend  dem wie,  in  dem  Masse  wie;  als';  dabei  kann die  Aussage  im  y-  und  im  übergeordneten Satz  i)  verschieden,  2)  gleich  sein,  in welchem  Fall  das  Praedikat  meist  nur einmal  gesetzt  ist  a)  im  Ap.;  zu  i)  tyJ'säm adam  a'haham  ava''  *akunavayc^tä  y mäm  kSmJ'  skJ*  "was  .  .,  das  taten  sie, so  wie  es  mein  Wille  war"  D.  ff.4;  /?.  3; —  '^SsiJm  kacSm^  a'^oAyc^  ava'hä ^aiunavaya'tä  Bh.  7.  8;  —  y  mClm  kämi^ ava^a  dis  akunavam  Bh.  4. 4;  —  iyam yux'iya  (sd.)  akäniy  *ava%a  *y  adam niyastäyam  D.  //.  3;  —  adam  käram *gaiava  avastäyam  y'  paruvamciy  (nämt. ähefi)  ava%a  Bh,  i.  14;  l4^  zu  2): availäm  tiaiy  astiy  kariam  y  manä  (i^mL (tstiy  kartam)  Bh.<^.9.  b)  im  gAw.;  zu i):  kä  tsth'(sd.)  fyao'hanäi..y  *7'a  *haxmT \y :  dakyJusmaiy  duruvS  ahatty  Bh.  4-  \  (sd.)  Y. 34.  5 ;  —  a%S  nS  at?kat  y  hvö S-  a)  mit  OpL;  a)  die  Annahme  wird  wuja/  (sd.)  Y.2(j,4;  —  ydi  Jm  v!  nsit ab  künftig  möglich  hingestellt;  im  Nach-  i%3  mq'irfm  vartSintt  (sd.)  y  Tm  mSitiii^ä salz  steht  der  Opt.:  'oi  zT  ma  masyäka..  vaocacä  Y.i^5.3;  — yBt  it  a%ä  vtriwyqn yazayanta  .  .  fiä  s'usuyam  Yt  S,  1 1,  10.  y  Tl  (Sp,  367  0.)  aitl  Y.^ß.  6;  —  y  /a 55  (*'^0.  74i  —  •'^'  «f  >"S  ma^.lka  .  .  f  .  ,  mSngftScä  vaocascä  .  .  yä  vsha  ahs yazayanta  ..  api  niqm  ari.bint'ryqm  ..  tni  dadiWiahT '^.^g.^;  35.6;  —  *y  *aii aop  \t.8.2^.        b)  die  Aussage  geht  auf  I  (Sp.  9  u.)  i'kä  vansaia  yi  data  ofahsus
23346:ya  hatqm  (Sp.  368  o.)  yyad^ananqm •tä  hyai  übdifyä  ahubya  Y.^jj.  3;  8  (Sp. 718  o.).  a)  bes.  in  eschatologischem Sinn:  hyai  äamä  *tl yajsn  (sd.)  mlidl  Y. 49-  9;  —  .iflSa  avA}u/  'takyä  paourvTm ka%s  (^t.)  saidyai  Y.44.2;  —  yahaca
25269:•  g.  raäah-  n.  'Schädigung,  Schaden',  ins- bes.  der  im  andern  Leben":  ^itica  smits (Sp.  367  m.)  Ayalca  dar?gSm  *drs^-6jbbyi 'Is  savaUa  aiavabyS  "..  der  lange  Schaden für  die  Z>n/^enossen  und  der  Nutzen  für die  v^/aanhänger"  Y.  ^o.  11.
25270:Zum  V.  rai-.  —  au  räi^as-  n.  —  Pü.:  m, erl. :  ha!  an  pasäxt  {s.  lü  Snilay-,  Sp.  367  U.).  - ■}  Vgl.  rüayeAhi  a  und  PüErl.
26755:*vTspqm.hujyäitTm  "in  seinen  Lagerräumen bringt  er  nach  Belieben  in  reicher  Fülle unter    alles    was    zum   Wohlleben    dient" Yt5.i30'). Zum  V.  islar:    —    1)    Bei    DST.   ZA.  3.  369
28616:—  dainayii  vanhuyai  yam  hsi  isyam  (sd.) datB  . .  masdä  alahya  äzdyai  (sd.)  gimdlm Y.5J.  17;  —  das  Nomen  ist  nicht  genannt, aber  durch  den  Zusammenhang  hinreichend deutlich:  kadsyava  AvB  aaAaf  {Sp.  369  0.) yS  Affi  (näml.  gavSi)  dadat  tastaz/at  (sd.) avSY.2g.  9.  2)  auf  ein  Nomen  voraus- weisend:  al^  hsi  (mask.;  zu  a)  scaniu ..  xsttüm  (sd.)  mazdä  vahmät  a  Y.  55.  2;
```


## [2026-09-05T20:31:27.525Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=7880 && NR<=8010' BRT.txt | grep -n \"36[5-9]\\|^• \" | head -40",
 "description": "Print BRT around column 368"
}
```


### [2026-09-05T20:31:29.167Z] TOOL RESULT

```
3:•  ]-.  g-  '*«  I"f-  '2"  gehen'.  3.^2;  —  sraosasca  *''oö'>  rtjft*  ahurahe..
8:•  j.  'i'8a  Adv.  'jetzt,  nun':  abdaca  (sd.)  Ivd  darrja  akarsta  saaa  ..  '6a  i'amiti  .. ila  sadayäj  ya^  "Sa  ..  pdo?m  vamaite'^.yä  darrja  apu'^ ra  *a?i(i  V.J.24.  3)  Es 2.24;  —  fitfii  mi  'oa  *affAäJJ^m  ''^f» .  dient  dazu,  ein  oder  mehr  vorangehende vtra  Yl/J.13;  Ä54;  —  äaj  vai^uAi  'oa  Wörter  als  Zitat  zu  kennzeichnen*';  das .  ,  artdvl  sare  .  .  az'at  äyaptun  yüsämiVlJSsx  ist  dann  Subjekt  des  Satzes:  yetiAe Yt.  5.130;  131;  —  'ta  irUlanqm  urvanS  ^'oa  mazdä  yasritm  a»as/i  "ye/>Ae  \chit  die yazamaide  Y.26".7;  2,  4,  7,  Vr. /(».  i,  2',  j  Anbetung  des  .(y."Y.  2  j.i; — ya»kqm  'oa Yt.Jj.9S,  148'; — frä  U  zq'ismca . .  azsm 'alaoninqm  ärmaiH.paoiryanqm  yasmm •oa /rasnayeiiiy.21.6;'],  VytiJ; —  kaAepara.ciiiasti{zi.)\.2i.2; — ya%a  frä  'oa n5  'oa  nqma  äyatryaf  (sd.)  Yt  ZJ,  50; —   ämraot  yal  ..    'lyaSJa  sagt  aus,  dass  . ."
10:365  iätt  —  ifrra  366
16:•  j.  iääf*  Adv.  'hier';  "öa/Ä  aini'oai^a 'fiatca  vlspqmca  atpi  imam  zam  Y.57. 33;
19:•  j.,  g.  ii^^  Adv.  1)  'so,  auf  diese  Weise, ita',  voraus-  und  zurückweisend:  "ä«  main-
28:•  j.  i^:zitirt  Y.^7,  das  damit  beginnt, zB.  N.  2^].
29:•  j.  iÖ-e  (indekl.):  (/ranrase  ..  ayqm daoPirim  daomnS)  i°  i^a  ya^na  ahmäi Yt.i^.57;  —  i' i^a  ya^na  ahmäi  ai>ae%a i^a  ya'ina  kahmät  Yt/5.61;  —  1°  fia ya'^'ia  ahmäi  ava^e  i^a  ya'ina  ahmai ävSya  i'ka  ya'kna  ahmfli  ¥1/^,63.  Sinn- lose Fluchworte".
32:•  j.  i'^a  Adv.  'hier;  hierher':  ^asttm  (sd.) frai^annia    pasvasca    .  .    V.  2. 1 1 ;    —
39:•  j.  "iöriäüm  änhat  ukftn  sadayat  fi.63. Var.iVfl/*;  wohl  JfJaoi  in  lesen.  —  Pä. :  fehlt.
41:•  j.  it,  g.  it  enkl.  Part  der  Hervorhebung; 1)  hinter  Rcl.:    eis/a    caräitis  ahi  yam  ii
44:•  j,  inja'>  Adv.  'zurUck';  i'  m!  urvtsyattm (sd.)Yt/().8j;  —  i°  ava^  kandazsayat»uha Yt  /().48.
46:•  j.  intay-">  (,  j.  initay-\  g.  5nitay-">  f. i)  'Vergewaltigung,  Kränkung':  ks  'iwqm
49:KompE.  (».  aiHilay).  —  Zum  V.  aen-.  —  Pü.: (luV.);  Mi,  (zu  Y.):  Unklar;  s.  •).  —  >)  Durch Dekomposilion,  s.  IF.  7.  70.  —  >)  Statt  iitil' geschi.,  S  368.  g.  —  3)  fh/aniivaV.aiap. 10.  »67  ;  j^Sl/J  .  .  hyaliä  'et . .  et  . .'  .
50:•  j.  '"alaurvayö  i'6a  ßuyanfftn  vHstrTtn vasöyaonäi  intern  hmauh?»^  Yt./o.6o.
52:•  j.  indra-  m.  Name  eines  Dafva*'>: i>aiti.p}r?ne  'r?m  . .  saurum  . ,  iiänAatiilm
56:•  j.  im  NSf.:  s.  unter  aySm.
83:•  p.  imaima-')  m.  EN.  eines  Susiers,  der sich  gegen  Darius /.  empörte:  »*dahyaus hauv  haciim<^'  hami^t'iyä  abavJ'  1  mar- tiyc^'  "Ma*  nilmt^  **m<ajiy^  avam  mä^t- itam  akuiiav^  Bh.5,  i".
85:•  p.  imanil-  m.  EN.:  so  nannte  sich  der Perser  Martiya,  als  er  sich  in  Susa  gegen Darius   I.    empörte :    /    martiya''    näiaa" ,
88:•  p.  iyam:  s.  unter  aySm.
90:•  j.,  g.  ira-  n.  i)  'Anlauf;  Aa^cilCi /rava- says . .  ya  * afrö.urvisvat  (sd.)  k?miavainii '/■3m  Yt.  rj.  26;  —  yahmya  säslärS  .. paoiris  °rä'>  räzaymte  ".  .  die  vielen  An- griffe ordnen"  YL/o.  14.  2)  'Energie, Tatkraft';  tatca  mazdä  'i:wahmT  *ä  dam (sd.)  nipuaks  .  .  *mqziijcsa'irä  vazdanhä *av}m  *ira'^  "..  dass  du  darüber  wachest, grossmächtiger,  mit  beständiger  Tatkraft" Y.  4:9.  10.
94:•  ').  isa-  Adj.  i)  'verlangend  nach  -'. —  2)  'nachstellend'.
96:•  j.  isat-västra'  m.  EN.  des  ältesten  Sohns ZaraHuäras  (aus  erster  Ehe)*':  'rahe zara>uitröis  asaons  Yt. /y.98,  Y.sö.  5;2j. 2;  —  'raAe  ^arai^ultröis  rumS  N._yi'>.
98:•  j.  isant-  Adj.,  PPA.:  s.  ^aii-.
100:•  j.  isav-  Adj.  'frostig,  eisig";  pasia  "saos Z3mö  aiwi.gaitTm  "nach  Eintritt  des  eisigen Winters"  V.9.6.
102:•  ).  isäna-  Adj.,  PPM.:  s.  als-.
103:•  j.  isv-KSadra-  Adj.  'nach  der  Herrschaft
111:•  j.  is3^§a3Työ.'t«ma-  Adj.  'der  am meisten  nach  der  Herrschaft  verlangt'; is>jxsairS  nama  ahmi  'mS  nama  afimi VL/.,3">.
113:•  ].,  g.  is«mna-  Adj.  (fem.  -«J-),  PPM.  : s.  'u?/-.
119:•  g,  isvan- Adj,  1) 'verfügend,  Herr  über-' (Gen.):  kasSuic'U  n3  aiilunS  ia^^  (sd.) avAal  'väcJl  Aas  paraol  "ob  man  über weniges,  ob  man  über  vieles  Herr  ist,  man soll . ,"  ¥..^7,4''.  a)  'der  (es)  vermag': hyat  na  fryai  vaEäamnS  °va  daidU  .  . fräxsn^mm  rafirü^  ".  .  Unterstützung,  wie sie  ein  Wissender,  wenn  er  es  vermag, dem  Freund  gewähren  soll"  y.415.14.
121:•  j.  tsvant-  m.  EN.  eines  Gläubigen": 'vatü  varilzake  (sd.)  alaons  Yt  13. 96.
124:•  p.  izitav-"  £  Name  einer  Landschaft in  Assyrien:  'tus  namä"  äahyäus  aiiuräyä Bh.  2. 10.
131:•  j.  iSa  Adv,  sva.  isar»  (sd.)"':  fy/n  aot Ibaesa  paifyantu  (sd.)  J°  ys  l  daoa  Y. 0-5.8.
```


## [2026-09-05T20:31:41.199Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=7880 && NR<=8120' BRT.txt | grep -nE \"^ *[0-9]{3}[^0-9]|[0-9]{3} *$\" | head -30",
 "description": "Find running headers 366-372"
}
```


### [2026-09-05T20:31:42.738Z] TOOL RESULT

```
10:365  iätt  —  ifrra  366
74:371
77:372
105:373
108:374
143:375  iäan.ätaitya
158:376
170:377
177:iia-  I  a  378
193:379
195:380
```


## [2026-09-05T20:32:10.703Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for L in 158 159 163; do echo \"=== leaf $L (printed p.$((L-21))) ===\"; awk -v n=$L 'BEGIN{RS=\"\\f\"} NR==n+1' HRN.txt; done",
 "description": "Print Horn pages 137,138,142"
}
```


### [2026-09-05T20:32:12.389Z] TOOL RESULT

```
=== leaf 158 (printed p.137) ===
- 137 —
Pärsenhandschrift 68, 10), röd(i)sn bezw. röy(i)sn; ai.
rödli' rodliati (KröA-, röltati).
bei. rtiday, n. ruday (319).
Zur i/^rödfi- vergl. Bartliolomae, ZDMG. 44, 553
No. 332.
615. resen 'Strick'.
ai. ragandr 'Strick, Riemen, Zügel, Gurt'; arm. LW.
apa\rasan zügellos*, erasan, erasanak 'Zügel' (Hübsch-
mann, No. 96).
arab. hebr. LW. rasan, bezw. JD^.
616. restden 'ankommen, erreichen', Praes. res-em^
resänTden,
g. rasadmün.
ap. i/^ras' 'kommen, gelangen', arusam^); phlv.
rasltan, ras(i)§n (AV.), rasmitan,
LW. afy. rasedal; bei. rasa(/ (313).
617. risten 'spinnen, Praes. res-efn, riste, resulen, resmän,
rismän, vergl. ebresum (No. 65).
g. risbün *Zwirn .
ai. i/^reg-, rigäte 'rupfen, abreissen.
bei. resag^ n. resay 'spinnen, flechten' (318), üresarj
'spinnen' (40) ; oss. alunjssin, d. alwiessun (bei Geiger).
resk s. eresk (No. 71).
618. risk 'Lauseei, Nisse' (AM. 141 Zeile 11, 191 Zeile 7).
ai. liksd' 'Ei einer Laus, Nisse' (Nöldeke bei
Hübschmann, Oss. Etym., S. 46).
kurd. LW. risk ; af/. riya ; bei. LW. rask, risk 'Läuse'
(217); oss. t. llsk, d. liskä 'Nisse' (170).
619. reften 'gehen, weggehen', Praes. rew-em, reftar, retvä
(arab. LW. rawäj), rewän, rewäne, retvis'^),
aw. y^rap' 'gehen' in rap<ö-.(?)3); phlv. raftafi, rapet^
rawad (3. Sing., geschr. ra/d)^ rawäk, räwäkth^
Aw. rasaintl' (y. 52, 1, 3) gehört nicht hierher nach liartho-
lomae, Indog. Forsch. II, 264.
*) BeilAufig bemerkt, ist die Aussprache rös in dem bei Vullers
aus Bh. 8. V. citirten öahnämeverse falscl^; derselbe steht I, 8 Vers 131.
') Yd. 13, 45. Aber ganz annoher.
=== leaf 159 (printed p.138) ===
- 138 -
raw(i)sn; vergl. lat. repö, lit. replioti, lett. rayt
'kriechen*.
kurd. rewin ; bei. LW. röag, rowag, n. raway (o22) ;
\va/. vä-refsam, sar. va-rafsam.
Gehört hierher auch np. ram eilend, fliegend' (Pfeil)
aus "raiman- (vergl. BB. 18, 298), z. B. Sahn. I, 195
Vers 1196 (Vullers druckt s. v. in seinem Wörter-
buche das unsinnige jsefer 'Sieg des FS statt ^efer
'Rachen* ganz unbefangen ab)?
620. rem, reme *Heerde'.
phlv. ramak *Heerde*, arm. LW. eram, eramak
(Iltibschmann, No. 96')), syr. LW. 101, hebr. LW.
D^?OT (Esther 8, 10).
LW. (?) af/. ramma *Heerde*; bei. ramag, n. ramay
(311).
Wohl zu [/'ram- *ruhen'.
621. rund, runde In Reisfeldern lebender Vogel*.
ap. f>ov8d%7j^' OQvi&iov (.ny.oov , /iieysd^og loov (oot'
Qvvödy.rjv (falsch Qvvöuy,^rjv) IlsQGai ro oQviSiov ytuXovai,
Ktesias bei Photius 44*^ 3, 4. ylrtvai fuy.oov hv üe^öaig
(lovidiov, (o 71 i^fUTTio aar og ovdti' ianv, dkk^ aXov diuTiXeMv
TnjusXijg rce svrog' yccxi vo/iuLovniv avs/tKO aal ^oooot T{)b-
(fjtod^ai ro C(pov' ovouaCsvai Jt ^vvräxtjg Plut. Artox.
19, 3. QVvödy.Tj rj'kiy.ov nsQiövsQa Hesych.
de Lagarde, Ges. Abh. 225; zuerst Reland,
Dissertatio de reliquiis veteris linguae persicae.
622. rendlden 'schaben, kratzen*, rende.
ai. [/'rad', rddati 'kratzen, ritzen'; phlv. randUan
(AV.).
kurd. renin; bei. randag *kämmen' (312).
623. {\)reny 'Farbe*.
skr. rafiga- 'Farbe*; arm. LW. erafig 'Farbe* (H.,
. No. 96).
LW. kurd. renk, reng; af/. rang; bei. rang (216).
') Audi uriu. rum 'Meiisclicnliuui'u .
=== leaf 163 (printed p.142) ===
— 142 —
639. rlden *kacken', Praes. rii/^em, rtsten, rtm *), rime.
aw. l/^raf-, avi dim irita *kackt darauf (vd. 5, 1);
phlv. }*ttan, reman, remamh; ai. l/^re-, riyäti *frei
lassen, laufen lassen .
kurd. rltin *kacken'; oss. d. liyun, t. Hin (168); bei.
rii/ay (315).
610. vis (*m) *Bart', rese *Haai'\
aw. ra^sa- zweifelhaft (Hörn, ZDMG. 43, 33,
Jackson, Amer. Journ. of Philology, Vol. XI, 88);
phlv. res *Bart' (AV.), resak *Haar (vd. 7 (28) Gl).
kurd. ruh, ri *Bart'; afy. ^Ira (aus *riSa) bezw.
^ire; oss. d. re/e, t. rt/T (213); wa/. reyis, i^itr. ri/is,
rikis, minj. yarzd,
Vergl. Bartholomae, Studien II, 54, 55.
641. veH') 'Wunde, Geschwür, rese, resTde,
aw. ra^sah' 'Wunde', [/^rars-, ra^ayat 'verwunden ;
phlv. res, resiian ; ai. l^reS-, resat^ reHyati *versehrt
werden ; beschädigen'.
LW. kurd. m; bei. res 'Wunde' (225).
642. reg \Sand' (AM. 242 Zeile 9), rez (Käs. Z. ryz).
LW. (?) kurd. rik^ rig; afy. reg; bei. rek^ n.
re/ (317).
Bartholomae (ZDMG. 46, 301 No. XIX) stellt die
iranischen Worte zu ai. sikata- 'Sand', während sie
Geiger an aw. l/^rafx- (No. 638) anschliessen wollte.
643. rew 'Betrug, List* (Sahn. II, 735 Vers 939), rewäs,
reimen, rlmen 'betrügerisch'^).
ai. rip' 'Betrug* (l/"rep-, lep- 'anschmieren').
Vergl. fireften (No. 829).
») *liem', LW. kurd. afy. rim *Eiter*, bei rgm 'Eiter* (224), wa/.
rim *Schmutz\
2) Der Mftihülvokul ist bezeichnet AM. 231 Zeile 3.
*) *Repmetiy vergl. * Verlorenes Sprachgut* No. 83. Die Volks-
otyraologie macht das Wort zu einer Verkürzung von Ahrlmen. Da die
Bedeutung 'sclimutzig, unrein* dem Worte nach der Überlieferung nicht
zukommt, so wird man os nicht zu phlv. reman^ np. rim (oben No. 039)
zi(5licn dürfen.
```


## [2026-09-05T20:32:33.217Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for w in \"ras-\" \"rasīdan\" \"rasid\" \"patyārag\" \"patyarag\" \"padīrag\" \"padirag\" \"rēdan\" \"redan\" \"rēman\" \"reman\" \"randīdan\" \"randidan\" \"arwand\" \"arvand\" \"rēm \" \"rīm\"; do echo \"--- $w ---\"; grep -n \"$w\" PHD.txt | head -4; done",
 "description": "Grep MacKenzie PHD"
}
```


### [2026-09-05T20:32:35.645Z] TOOL RESULT

```
--- ras- ---
384:ёгбһ [glwh | N guroh] group, crowd. gubrág [gwpl’k'] awake, alert, vigilant. ģubrās- [gwp/”s-] = wigras-, v. wigrádan. ģuftan, $0(w)- [YMRRWN-, YMLLWN-tn! < A ymlwn, V тЇ; gwptn', gwb- | M gwptn, gw-, N ~, gā(y)-] say, speak. ~išn: speech. ģuftār [gwpt?] | N ~] speaker. ~ih: (power of) speech. gugiin- [gwk’n- | M gwg^n-] destroy. gugar(i)dan, gugar- [gwk”/-(y)tn! | N guwár-idan] digest. tuģāy [gwk*dy | M gwg'y, N guwah] witness. ~ih: testimony. ģūh [gwh | N —] dung, excrement. guhrayénidan, guhrayén- [gw AP yn-ytn!] waken, arouse. gul [gwl | N ~] flower, rose. ботап [gwnmn! | = M, N ~] doubt. ~par [-A/] casting doubt. ~ig [-yk'] doubtful. ~ih, ~igih: doubt. gumardag [gwmltk'] appointee, deputy. ģumārdan, gumār- [gwm’l-tn' | М gwm'r-dn, N gumāštan, gumar-] appoint, commission, entrust. gumbad [gwmbt' | N ~] dome, fire-temple. £umég [gwmyk! | M gwmyg] mixture. guméxtan, gumēz- [gx”myhtn!, gwmyc- | M gwmyxtn, gwmyz-] mix. ~išn: mixing, mixture; = gumézagih. gumëzag [gwmyck'] mixture. ~th: the Mixture, (the duration of) this material world. Jgund [gwnd | = P] army, troop; group, gathering. *gund [gwnd | N ~] testicle. gung [g(w)ng | N ~] dumb. ģurbaģ [gwibk! | N ~a] cat. Бита [gwlt! | P gwrd, N ~] hero. lih: heroism, bravery. gurdag [gwltk! | N ~a] kidney. *gurdih [ewityh] (some piece of) armour. gurdwār [gwltw’!] befitting a hero. ёпгр [gwlg | N ~] wolf. gurganig [gw/g”nyk! | N ~i] of (the province) Gurgan. gursag [ewlsk] | N gurusna !] hungry. «ЛЬ: hunger. Suën [gvfn! | N ~] male. gusnag [gwšnk! | J gušna] hungry. Gušnasp [gwšn(*)sf] the second major Fire of Sasanian Eran, that of warriors. £yà$ [gyw'k! | M gy'g, N jay] place.
557:ranjwar [Incwl | (M rnzwr), N ranjūr] troubled, distressed. rapihwin [/pys-, Ipyt-pyn!, -wyn' = Av. rapiüfina-] the afternoon gah; south. ~tar [-tl] southern. rasan [/sn' | N ~] rope. rasénidan, rasén- [/syn-yin'] bring. rasidan, ras- [YHMTWN-tn' < А yhmtwn, V mt^; ls-ytn! | M rs-ydn, N ~] arrive, mature. raspig [Pspyk!] second officiating priest. rast [Pst! | M rst, N ~] true, straight, direct. ~ih: truth, rastaģ [lstk! | N rasta] series, row, progression; element, газап, rah- [Istn', Ї(?)А- | N ~] escape. rastarih [/st?/y%] escape. rasüg [/swk! | (N rāsū)] weasel. Rašn [/@! | M ri, N ~] god of Justice; cal. 18th day. ra&tan, *raz- [/ftn'] colour, dye. raw-, v. raftan. rawag [/wP^k! | N rawá] current. ~ih: currency. rawügenidan, rawagén- [/zob)hyn-ytn!] set in motion, propagate. rawénidan, rawén- [SGYTWNyn-ytn', v. raftan] cause to go, extend. rawišn [lwbin', SGYTWNsn', v. raftan | N rawif] going, motion. ^h : behaviour; as a suffix, forms abstract nouns. ray [Pd | M ry, N ra] postposition, for, for the sake of. rāyēnāģ [Pdym bi | M r’yn’g] arranger. rayénidan, rāyēn- [Pdyn-ytn! | M r'yn-ydn] lead, direct, arrange, organize. ~išn: action, function; arrangement. rāyēnīdārīh [/”*dynyt?lyh | M r!ynyd?ryh] direction, organization, rāyišn [”dsn'] order, arrangement. rāyomand [Pd^wmnd] rich, majestic. raz [/c, lz | N ~] vine; vineyard. raz [Pc | M Pz, N ~] secret, mystery. ~ig [-yk'] secret. rāz-kirrēģ [Pc kylwk' | M г qrwg] architect, builder. razm [/cm | M rzm, N —] battle. —--$àh [-g's | P -g’h, (M rzm?h), N ~] battlefield. razor [lcw] | M rzwr] forest. rédak [lytk' | N ~] lad, page. тёр [/yā! | N ~] sand. rëm [lym | M rym, N —] dirt, filth, purulence. réman [lymn' | M rymn, N ~] dirty, filthy, purulent. ^b : filth. 1r€§ []yf | N ~] wound, sore. *rēš [/yf | N —] beard.
651:wénig [wynyk! | M wynyg, N bini] nose. wénO£ [wynwk' | N bunü] lentil. wēš [zoy£ | = M, N béf] more. wé&ag [wysR! | N beta] thicket, wood. --estün [-st?n'] woodland. ~ig [-yk'] silvan. wēwag [wdpk! | N béwa] widow. 1wéxtan, wez- [NSSHWN-tn! < А V nsh; wyhtn', wyc- | P wyxt-, N bextan, béz-] sift, select, choose, separate, cleanse, purify, winnow. ~išn: selection. *wēxtan, wēz- [wyhtn!, wyc-] swing, brandish, throw, pour out. Wīdadafš [wydtpš = Av. wīdašafšū-| the south-western continent of the earth. widang [wtng | P wdng] trouble, distress, constraint. widār [xt' | N gudár] passage, entrance. widarag [wtlg | M wdr, N guàar] path, passage. widardan, wider- [wtitn!, wt(y)l- | M wd(y)r-, N guóar-] pass (by, away), cross, die. : ~išn(īh): passage, crossing, death. ~i$nig : transient. widārdan, widār- [xwt?/-tn! | M wyd’r-, N guóárdan] let pass, transport; endure, suffer. widārīdan [w?lytn'] = widardan. widaštan [wtstn' | N gušaštan] = widardan. widāxtan, widāz- [wt’hin', wtc- | (P wd’c-), N gudaxtan, gudāz-| melt, dissolve. widāzīhistan, widazih- [wt’cyh-stn'] be melted, dissolved. wider- , -išn(-īģ, -ih), v. widardan. widerān [wt(y)?n! | N guóarán) transient, dying. widest [zot(y)st! | N bidast] (hand) span (9 in.). ~ig [-yk'] span-sized, midget. widimās [wtym’s | (M wyd’m’s)] wonder, miracle. ~ig [-уА!] wonderful. ~ih: miracle. widimušt [wtymust | M wd(y)mwšt] astonished. ~ih: astonishment. *widwar [wytwl] contented, resigned, consoled. ~ih: contentment, resignation, consolation. wiftag [wyptk'] passive sodomite. wigrad [zogPt! | N bīdār] awake, alert. wigradan, wigras- [zog tn, wgl’s- | M wygr'd, wygr’s-] awaken, rouse. ~i$n(ih): awakening. wih-, v. wistan. wihan(ag) [zh?n(k)', (b-) | M wl?ng, N bahāna] cause, reason. wihēz- [wyhyc- | M twhyz-] move, progress. wihéz(ag) [wyhyc(k')] movement, progression.
4913:rag атат, sīhom” hazārag* larz- larzīdan ram abgan-! abgandan! ramag ras- rascn- rasenidan rahig rasidan rastarih rastan rastag
--- rasīdan ---
848:arrive rasīdan,
--- rasid ---
161:a- P- | M ?-] privative prefix, un-, Jess, а D] then (generally with a suffixed pronoun, e.g. 8-š). ab [M YA < А my';?p | M >b, N ~] water. B Soy 277 abad рр? | M Ра, N ~] populous, thriving, prosperous. ~ih: prosperity. ābādān [f*?t?*n' | N ~] thriving, prosperous, cultivated. ~ih: prosperity, cultivation. abādixšā(y) 'P?th? (d), v. pādixšā(y)] without authority, powerless. ~ih: powerlessness; anarchy. abādyāwand Pf?tyd”wnd | J ?b’dywn<d>] powerless, weak. ~ih: powerlessness, weakness. арар [LW TE < A lwt-h | M?Pg, N (a)bā] with. ~ih Dë kuk) company, assistance. abāgēnīdan, abāģēn- [^P'kyn-ytn!] accompany. a-bahr РРА] portionless, deprived. abām Pf?m | P ?bmyh, N (a)wàm] loan, debt. Abàn PPn! | M'0x, N ~] cal. 8th month; roth day. aband (nd, v. рапа | M ?bnd] erring. “АҺ: error. 'abar [ODM < А дат; bl | M "be, N bar] up; on, over. ~ āmadan: rise (sun). ~ āxistan: rise up. ~ āxrāmīdan: step up. — burdan : undertake. ~ madan: cope with, comprehend. ~ nigeridan: consider. ~ nihumbidan: conceal. ~ niSastan: sit, be enthroned. ~ nišāstan: seat, install. ~ rasidan: come to, upon. ~ rasidan б: attain. tabar Dél higher, superior. ~ag [-g | MP brg] superior. ~agan(ag) [-k’n(k)'] superior. --dar [-t, Zenit | M ?brdr] higher. ~dom [-twm | M ?brdwm] highest. —domih [-twmyh] superiority. abargar [5/21 god, divinity. abarig(àn) ['Bblyk( ny] = abarag. abarig DPryk! | M ?Pryg, J ?Pry] other.
557:ranjwar [Incwl | (M rnzwr), N ranjūr] troubled, distressed. rapihwin [/pys-, Ipyt-pyn!, -wyn' = Av. rapiüfina-] the afternoon gah; south. ~tar [-tl] southern. rasan [/sn' | N ~] rope. rasénidan, rasén- [/syn-yin'] bring. rasidan, ras- [YHMTWN-tn' < А yhmtwn, V mt^; ls-ytn! | M rs-ydn, N ~] arrive, mature. raspig [Pspyk!] second officiating priest. rast [Pst! | M rst, N ~] true, straight, direct. ~ih: truth, rastaģ [lstk! | N rasta] series, row, progression; element, газап, rah- [Istn', Ї(?)А- | N ~] escape. rastarih [/st?/y%] escape. rasüg [/swk! | (N rāsū)] weasel. Rašn [/@! | M ri, N ~] god of Justice; cal. 18th day. ra&tan, *raz- [/ftn'] colour, dye. raw-, v. raftan. rawag [/wP^k! | N rawá] current. ~ih: currency. rawügenidan, rawagén- [/zob)hyn-ytn!] set in motion, propagate. rawénidan, rawén- [SGYTWNyn-ytn', v. raftan] cause to go, extend. rawišn [lwbin', SGYTWNsn', v. raftan | N rawif] going, motion. ^h : behaviour; as a suffix, forms abstract nouns. ray [Pd | M ry, N ra] postposition, for, for the sake of. rāyēnāģ [Pdym bi | M r’yn’g] arranger. rayénidan, rāyēn- [Pdyn-ytn! | M r'yn-ydn] lead, direct, arrange, organize. ~išn: action, function; arrangement. rāyēnīdārīh [/”*dynyt?lyh | M r!ynyd?ryh] direction, organization, rāyišn [”dsn'] order, arrangement. rāyomand [Pd^wmnd] rich, majestic. raz [/c, lz | N ~] vine; vineyard. raz [Pc | M Pz, N ~] secret, mystery. ~ig [-yk'] secret. rāz-kirrēģ [Pc kylwk' | M г qrwg] architect, builder. razm [/cm | M rzm, N —] battle. —--$àh [-g's | P -g’h, (M rzm?h), N ~] battlefield. razor [lcw] | M rzwr] forest. rédak [lytk' | N ~] lad, page. тёр [/yā! | N ~] sand. rëm [lym | M rym, N —] dirt, filth, purulence. réman [lymn' | M rymn, N ~] dirty, filthy, purulent. ^b : filth. 1r€§ []yf | N ~] wound, sore. *rēš [/yf | N —] beard.
886:attain abar rasidan 6, ayāftan.
1286:andar ámadan; ~ to, upon abar rasidan; ~ to an end 6 ham madan.
--- patyārag ---
--- patyarag ---
--- padīrag ---
--- padirag ---
519:6š 62 padiragih
536:pa(č)čēn [pcgn!] copy. *pa(č)čībāg [pcyp k', PWNe- | N *pajiw] *deceptive. ^h : deceit, hypocrisy. *pa(č)čībāy- [pcyp'd-, PWNc-] deceive. pad [PWN, for *pty | M pd, N pa] to, at, in, on. pad- [pt- | M *pd-) fall. padam [pd”m | (IN pandm)] mask for the mouth, worn by a celebrating priest. !Ipádan, pày- (UIN TLWN-tn! < А V ntr; Ptn, pd- | M pd, p’y-, N páyidan] protect, watch, defend. *pádan, pāy- [N TLWN-tn!, etc.] stand, wait. pādāšn [p?td?fn! | M p’d’syn, N pàdàs] reward, retribution. padēx [ptyhw'] flourishing, prosperous. ~ih: prosperity. padéxénidan, padéxén- [ptyhwyn-ytn'] make flourish, prosper. pādēz [p'tyc | M p'dyz, N pāyēz] autumn. pad-góhr [PW Ngwhl] т. jewelled; 2. of good stock, well-born. padifrah [p’tpl’s | M p'dypr?h, N *pādafrāh] punishment, retribution. padir-, ~išn, v. padiriftan. padirag [ptylk' | M pdyrg, N paóira] towards, against, counter-. (6) — madan: come to mect. ~ih: meeting, opposition.
749:against padirag.
1415:counter- padirag.
--- rēdan ---
--- redan ---
--- rēman ---
1684:doubt gumān(īh), warēmandih; cast- ing — gumangar.
4955:pay" rem rēmanīh
4956:rēman
--- reman ---
188:~ih : immortality. ahr Phl] dread, fury. ahrüftan, ahram- P4Pftn', *hm- | M hr’ рїп, ? hr? m-] raise, lead up. Ahreman ['Al(y)mn! | М ?hrmyn, N ~] the Evil Spirit. >
1815:evil (a.) akēmand, апар, druwand, wad(ag), wattar, duš-; ~ deed dušxwaršt; ~ eye aš, dujdoys?rih; ~ rule dušpādixšāyīh; ~ ruler dušpādixšā(y); — speech dušēwāz- ih, dušhüxt; — spirit Ahreman, gannág mēnēg; ~ thought duš(hu)- mat; of ~ behaviour duškunišn; of — religion agdén, dujdén; of — speech duš-gēwišn; of — thought dušmenišn.
4387:Ahreman Akóman Arzür Astwihad
--- randīdan ---
701:abrade randīdan.
--- randidan ---
555:rabih [/pyh | M rbyh] noon, midday (heat). rad [/t! | N —] (spiritual) chief, master. АҺ: office of rad. rad [Pu | P rd, N ~] generous, liberal. ~ih: generosity, liberality. radag [itk! | M rdg, N rada] line, rank, row. radómand [/t?^wmnd] having a rad. rad-passag [/tps’k'] ceremonies of the gáhanbar festivals. radunay [/twny = Av. ratunaya-] one under the guidance of a rad. raftan, raw- [SGY TWN-tn! < А V sg’; lwb- | M rptn, rw-, N ~] go, move, proceed. ~išn, v. rawišn. raftār [/pt?] | N ~] goer. rag А! | M rg, N ~] vein. «ЛЬ: disposition, character. ray [/gy | P rg] quick, swift. ray [Pg | N —] meadow, plain. rah [/s, lh, [hy | M rh(y)] chariot, wagon. rah-, у. rastan. rah [Ps | M rh, N ~] road, way. rahag [/hk! | P rhg] = rag. rāh-dār [lsd] | N ~] brigand, highway robber. ~ih: brigandage. rahig [/syk!, Ikyk' | M rhyg, N rahi] child, page. ~ih: childhood. rāh-nimāy [Psnm?d | (M r’-hnmwd’r), № ~numa] guide. ram [Pm | М әт, N ~] peace; cal. 21st day. ram(ag) [/m(k') | P rm, N ram(a)] herd, flock. ráménidan, rāmēn- [Pmyn-ytn! | M ?myn-] give peace, pleasure. rāmišn [P min! | M rmyfn, N rāmi$] peace, ease, pleasure. ~ig [-vk! | N —z#] peaceful, at ease. ran [Рп! | N ~] thigh. P rān- [/^n-] fight. randidan, rand- [/nd-ytn! | N —] scratch, grate, abrade. rang [/ng | M rng, N —] colour, dye. ranj [Inc | P rnj, (M rnz), N ~] toil, trouble. ~ag [-k' | N —a] troubled. ranjénidan, ranjén- [/ncyn-ytn'] trouble.
2139:grate randidan.
3536:scratch randidan.
4922:róvan, royén randidan pes
--- arwand ---
214:a-pus [' BRE] without a son, childless. ár-, v. árdan. 5 āranj "Inc | N ~] elbow.. 9-43. "Ant *a-rāst Prst'] untruth. ārāstan, ārāy- [Pstn!,^Pd- | N ~] prepare, arrange, adorn. ~ién: arrangement, adornment. a-rawüg [”/wbk!] immobile. Ard р | M?yrd, N ~] a goddess; cal. 25th day. ard [KHM A < А gm; п | N ~] flour. агаа [py | (M rd?w)] righteous, truthful. ardan, ār- [THNN-tn' < А V thn; ?l-tn'] grind, mill. ardāyīh ['i?dyh | M?rd?yyh] righteousness, rectitude. ardig [/tyk! | M ?rdyg] battle. ardikkar рук], -kl | M?rdyqr] warlike, warrior. ~ith: doing battle. arduš [”ldwš = Av. aroduš-] a degree of sin. Ardwahišt Prtwhst' | M ?rdywhyst, (N urdībihist)] Right, the second Amahraspand, guardian of fire; cal. 2nd month; 3rd day. arešk [lysk' | M ()rysk, N rašk] envy, jealousy. ~én [-yn'] envious, jealous. ārešn Pim! | M ”7ysn-, N (a)rif] cubit. aryand [?/епа | N ~] horrible. arģawān [*/gwk'*n! | N aryawān] purple. armēšt ["/myst'] inactive, infirm. ~ih: infirmity. armēšt-ģāh [-g’s] secluded place for the infirm. агбуї&п [/wdšn'] growth. ~ig [-y&!] growing, vegetable. ars Dis | M?rs, N ~] tear (drop). artēštār УЯ? | N artēšdār!] warrior. „īh: warriorhood. arus [2/00] white. arwand [wnd] swift, valiant; river Orontes. ~ih: swiftness, valour. arwés [lwys | M ?rwys, N ~] rope. arz [KSP! < А Ар; с | N ~] worth, value. Arzah [Iz h == Av. arazahi-] the eastern continent of the earth. arzan [PE < А prg’; len! | N <) millet. arzàn Plen | M *rz'n, N ~] valuable, worthy. ~ig [-yk'] worthy. ~igih: value, worth, worthiness. arzidan, arz- [?/с-уїп! | N ~] be worth. ~išn: value, worth. arziz (сус | M ?rzyz, N ~] tin, lead. —ën [-yn'] tin, leaden. ārzōg Picwk! | M'wrzwg, N àrzó] desire, lust,
542:~ AZ: free (oneself) from. pargandan, pargan- [plkn-, plgn-dn! | (P pr'gnd, N parāgandan)] scatter, distribute, disperse. pargast [plgst' | N ~] let it not happen! Heaven forbid! pargüd [plgwt' | P prgwdg], ~ az: free, exempt from. parig [plyk' | M pryg, N pari] witch. paristag [pistk! | N pirista] servant. ~th: service; worship. paristar [plsť] | N parastár] maidservant. paristidan, parist- [plst-ytn' | M pryst-, N parastidan] serve, worship. ~išn: service, worship. paristog/k [plstwk' | P prstwg, N piristū(k)] swallow. рагпабап [pinyE?n! | M prng?n, N parniyān] polychrome damask. parr [pl | M pr, N ~] feather, wing. parrag [plk', pig | P prg, N ~a] wing. ~ig [-vk'] winged. parréxtan, parréz- [plyhin', plyc-] remain over, be superfluous. parrón [plwn' | M prwn] hence, away. parrwar [plwl | M prwr] winged. parsig [p’lsyk' | N pārsī] Persian. pars [5/f] spotted, speckled. parwāl [plwl | (P prwrz)] refreshment, nourishment. parwal- [plw���l- | (P prwrz'dn)) foster, nourish, -išn: nourishment. parwanag [phonk! | M prw’ng, N ~a] guide, leader. ^h : guidance, leadership. parwand [plwnd | N —] enclosure, comprehension. parwand-, v. parwastan. P parwānģāh [*plw?ng’s] throne. parwār [plyw?l | N ~] citadel; circumvallation; suburb, surroundings. parwardan, parwar- [plwl-tn' | M prwrdn, N ~) foster, nourish, cherish, educate. ~išn: nourishment, fostering, education. parwast [plwst'] enclosure. parwastan, parwand- [plwstn', plwnd-] surround, enclose, contain, comprise. parwāz [plw’c | N ~] flight. parzin [picyn' | M prcyn, J przyn, (N parčīn)] fence, hedge. pas [AHL < A?hr; BATL < Ab2tr; ps| = M, N ~] then, afterwards, behind. ~ az: after. ~ih: rear. pas [p’s | = M, N ~] guard, watch. ~ dāštan: keep watch, guard. pāsbān [p’sp’n' | M p’sb’n, N ~] guardian, watcher. ~ih: defence, protection.
1316:comprehension ayabagih; parwand.
1760:enclosure parwand, parwast, war.
--- arvand ---
--- rēm  ---
--- rīm ---
```


## [2026-09-05T20:32:51.216Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"adversity\\|patyār\\|patyar\\|ptyd?\" PHD.txt | head -6; echo \"=== NYB ===\"; grep -n \"patyārak\\|patyarak\\|patkār\\|padīrak\\|padirak\\|arvand\\|arwand\\|rēman\\|rytn\\|rīm\\b\" NYB_vol2_glossary.txt | head -10",
 "description": "Grep PHD patyarag and Nyberg"
}
```


### [2026-09-05T20:32:51.279Z] TOOL RESULT

```
=== NYB ===
656:arvand [lwnd] swift 228. — Av. (200) aurvant-.
658:arvandéh valour, gallantry 55’.
2241:äyet do ye proclaim that every man shall come to King V.’s court 205-6; Dahäk hàn and zaman ‘BYDWN-x, cand ... to D. as long a time will be assigned as (to allow him to...) 997; ristäxez etón kind ka he will determine the Resurrection at the time when ... 3422; atän hàn 4 kart axtäyisneh (q. v.) dahet he will create un- willingness with regard to what is in- stituted by you 451; of the marriage contract: mart u zan évak apäk dit kämak bavēt, räyenend u ‘BY DWN-x, man and woman will fall in love, become engaged (v. räyenitan) and contract marriage 1044-25; zan kartan u patvand i geteh rayénitan to marry a woman and settle his family ties in this world 631%; PLK?... pat čip $ banjak kart éstat the axe was enchanted (dedicated to Hell) by means of banjak (q. v.)-water 2516-17, 284; Sah- puhr ... āpān xānak kart Sh. founded (instituted) a temple for the Waters 10914-15; the same meaning undoubtedly also in the expression šahristčin kart 113— 116; šahristan ... pat Sapistan kart was declared a harem-city 116?4-?5, — Av. (448) 2kar- ‘to recollect, to mention, to com- mend’ [from which in all probability ham + the caus. in the set phrase nivaé- čayemi hankčirayemi ‘I consecrate, I de- dicate’ (not from !kar- as Bthl. has 1t)]. First proposed by Pagliaro, RSO XXIII, 1948, 67-68 (v.s. v. ?kartak); followed up by A. Périkhanian, REA, N.S. V, 1968, 22, VI, 1969, 8, quoting the Arm. lw. &ar [< *éarna-] ‘festival oration, ho- mily’. Of course in BP as we now have it BYDWN- has always been read as kun-, but the original pres. must have been kar-, as the NW pres. of kartan ‘to make'.— V .?kartak, kartäreh (1), hangartan, nikerdi, nikeritan, patkārītan, uskärtan.
3060:patkär [ptk?l], pitkär [pytk'l] quarrel, controversy, dispute 4519-12 [pit-]. 70". 1081. — MPrs phyk?r (A-H II; meaning: quite clear); Paz. patkür; NP patkār; v. ?kartan and uskartan.
5025:aurvant-: arvand
6530:d(a)rog: drog darma(n): darman daru: darok daruand, darvand: druvand daruandi: druvandéh daryäv: drayäp daryös: drigūš dasti: apastčh dastur: dastavar daša(a): daxšak dašt: daštan, dar-: dawar: davr davar: dätavar deh: déh
```


## [2026-09-05T20:32:59.799Z] TOOL CALL #27: Bash

```json
{
 "command": "sed -n '1,40p' tools/fetch_source.py",
 "description": "Inspect fetch_source.py"
}
```


### [2026-09-05T20:32:59.838Z] TOOL RESULT

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
```


## [2026-09-05T20:33:05.928Z] TOOL CALL #28: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/%D8%B1%D8%B3%DB%8C%D8%AF%D9%86\" \\\n \"https://en.wiktionary.org/wiki/%D9%BE%D8%AA%DB%8C%D8%A7%D8%B1%D9%87\" \\\n \"https://en.wiktionary.org/wiki/%D8%A7%D8%B1%D9%88%D9%86%D8%AF\" \\\n \"https://en.wiktionary.org/wiki/%D8%B1%DB%8C%D8%AF%D9%86\" \\\n \"https://en.wiktionary.org/wiki/%D8%B1%DB%8C%D9%85\" \\\n \"https://en.wiktionary.org/wiki/%D8%B1%D9%86%D8%AF%D9%87\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 156, root Er 1/Or: Persian derivatives\" ; done",
 "description": "Archive Wiktionary Persian pages"
}
```


### [2026-09-05T20:33:11.376Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/3b677fedca88e1e7.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ae8e233cc00a67a7.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/6f0141dc3b1429c3.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/0c3fecc789de9f07.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ee07a89e54c2641f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e72d6beda051ecaa.txt
```


## [2026-09-05T20:33:14.543Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in 3b677fedca88e1e7 ae8e233cc00a67a7 6f0141dc3b1429c3 0c3fecc789de9f07 ee07a89e54c2641f e72d6beda051ecaa; do echo \"########## $f\"; grep -n -A25 \"^Persian\" $f.txt | head -60; done",
 "description": "Extract Persian sections"
}
```


### [2026-09-05T20:33:16.214Z] TOOL RESULT

```
########## 3b677fedca88e1e7
########## ae8e233cc00a67a7
########## 6f0141dc3b1429c3
########## 0c3fecc789de9f07
########## ee07a89e54c2641f
########## e72d6beda051ecaa
```


## [2026-09-05T20:33:19.359Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in 3b677fedca88e1e7 ae8e233cc00a67a7 6f0141dc3b1429c3 0c3fecc789de9f07 ee07a89e54c2641f e72d6beda051ecaa; do echo \"########## $f\"; wc -c $f.txt; grep -n -i \"etymolog\" $f.txt | head -3; done",
 "description": "Check fetched content"
}
```


### [2026-09-05T20:33:21.289Z] TOOL RESULT

```
########## 3b677fedca88e1e7
11373 3b677fedca88e1e7.txt
62: Etymology 
149: Etymology
628: ^ Cheung, Johnny ( 2007 ), Etymological Dictionary of the Iranian Verb (Leiden Indo-European Etymological Dictionary Series; 2), Leiden, Boston: Brill, →ISBN , pages 163-5 
########## ae8e233cc00a67a7
162 ae8e233cc00a67a7.txt
########## 6f0141dc3b1429c3
6065 6f0141dc3b1429c3.txt
62: Etymology 
76: Etymology 
156: Etymology
########## 0c3fecc789de9f07
10485 0c3fecc789de9f07.txt
62: Etymology 
146: Etymology
613: ^ Cheung, Johnny ( 2007 ), “ *HraiH ”, in Etymological Dictionary of the Iranian Verb (Leiden Indo-European Etymological Dictionary Series; 2), Leiden, Boston: Brill, →ISBN , page 188 
########## ee07a89e54c2641f
2085 ee07a89e54c2641f.txt
62: Etymology 
134: Etymology
########## e72d6beda051ecaa
6206 e72d6beda051ecaa.txt
73: Etymology 
90: Etymology 
230: Etymology
```


## [2026-09-05T20:33:24.449Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in 3b677fedca88e1e7 6f0141dc3b1429c3 0c3fecc789de9f07 ee07a89e54c2641f e72d6beda051ecaa; do echo \"########## $f\"; sed -n '140,200p' $f.txt; done",
 "description": "Print etymology sections"
}
```


### [2026-09-05T20:33:26.159Z] TOOL RESULT

```
########## 3b677fedca88e1e7

 move to sidebar 
 hide 

 From Wiktionary, the free dictionary

 Persian
 [ edit ] 

 Etymology
 [ edit ] 

 From Middle Persian 𐭫𐭮𐭩𐭲𐭭 ( rasīdan ) , from Old Persian [script needed] ( rasa- /⁠rs(s)a-⁠/ , “ to move ” ) , from Proto-Iranian *Har- ( “ to go towards, reach ” ) , from Proto-Indo-European *h₁er- ( “ to move, go ” ) . [ 1 ] Cognate with Northern Kurdish rizîn ( “ to rot ” ) and herrîn (as in herre ( “ go! ” ) ), Central Kurdish ڕزان ( rizan , “ to rot ” ) , Zazaki resayene ( “ to reach ” ) , Sanskrit ऋ ( ṛ , “ to go, rise ” ) , Ancient Greek ἔρχομαι ( érkhomai , “ to go, come ” ) , and Albanian erdha ( “ to have come, originated ” ) (the latter two via a derivative *h₁ergʰ- ( “ to move ” ) ).

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /ra.siː.ˈdan/ 

 ( Dari, formal ) IPA ( key ) : [rä.siː.d̪än] 

 ( Dari, formal ) IPA ( key ) : [rä.siː.d̪än] 
 ( Kabuli ) IPA ( key ) : [rä.siː.d̪än] 

 ( Hazaragi ) IPA ( key ) : [rä.si.d̪än] 

 ( Iran, formal ) IPA ( key ) : [ɹæ.siː.d̪æn] 

 ( Iran, formal ) IPA ( key ) : [ɹæ.siː.d̪æn] 
 ( Tehrani ) IPA ( key ) : [ɹe.siː.d̪æn] 

 ( Tajik, formal ) IPA ( key ) : [ɾä.si.d̪än] 

 Rhymes: -an 

 Readings

 Classical reading ? 

 rasīdan

 Dari reading ? 

 rasīdan

 Iranian reading ? 

 rasidan

 Tajik reading ? 

 rasidan

 Verb
 [ edit ] 

 رسیدن • ( rasīdan  / rasidan ) ( present stem رس ( ras ) , Tajik spelling расидан ) 

 Dari

 رسیدن 
########## 6f0141dc3b1429c3
 Create a book 
 Download as PDF 
 Printable version 

 In other projects

 Appearance

 move to sidebar 
 hide 

 From Wiktionary, the free dictionary

 Ottoman Turkish
 [ edit ] 

 Etymology
 [ edit ] 

 Borrowed from Persian اروند ( arvand ) .

 Proper noun
 [ edit ] 

 اروند • ( Ervend ) 

 Tigris (a river in the Middle East )
 Synonym: دجله ( Dicle ) 

 Elvend (a mountain in Iran , near Hamadan )

 Further reading
 [ edit ] 

 Kélékian, Diran ( 1911 ), “ اروند ”, in Dictionnaire turc-français ‎ [2] (in French), Constantinople: Mihran, page 70 

 Redhouse, James W. ( 1890 ), “ اروند ”, in A Turkish and English Lexicon ‎ [3] , Constantinople: A. H. Boyajian, page 75 

 Persian
 [ edit ] 

 Etymology
 [ edit ] 

 Inherited from Middle Persian [Book Pahlavi needed] ( ʾlwnd /⁠arwand⁠/ , “ swift, valiant; name of a river (literally "swift river"), perhaps the Tigris ” ) , from Proto-Indo-Iranian *Hárwants ( “ fast, quick; a racehorse, courser ” ) , from Proto-Indo-European *h₃ér-went-s , from *h₃er- ( “ to move (swiftly), to spring ” ) . Cognate with Sanskrit अर्वन्त् ( árvant ) , Avestan 𐬀𐬎𐬭𐬎𐬎𐬀𐬧𐬙 ( a u ruuaṇt ) .

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /ʔar.ˈwand/ 

 ( Dari, formal ) IPA ( key ) : [ʔäɾ.wán̪d̪] 

 ( Dari, formal ) IPA ( key ) : [ʔäɾ.wán̪d̪] 
 ( Kabuli ) IPA ( key ) : [ʔäɾ.wán̪d̪] 

 ( Hazaragi ) IPA ( key ) : [ʔäɾ.wán̪d̪̥] 

 ( Iran, formal ) IPA ( key ) : [ʔæɹ.vǽn̪d̪̥] 

 ( Tajik, formal ) IPA ( key ) : [ʔäɾ.ván̪d̪] 
########## 0c3fecc789de9f07

 See also: زيدن 

 Persian
 [ edit ] 

 Etymology
 [ edit ] 

 From Middle Persian [script needed] ( lytn /⁠rīdan⁠/ , “ to defecate ” ) (root [script needed] ( ld- /⁠riy-⁠/ ) ), from Old Persian , from Proto-Iranian *HriHyátī ( “ to defecate ” ) , from Proto-Indo-Iranian *HriHyáti , from Proto-Indo-European *h₃riH-yé-ti ( “ to flow ” ) . [ 1 ] Cognate with Northern Kurdish rîtin , Northern Luri ڕیێ ( rryı ) , Sanskrit रीयते ( rī́yate , “ to flow ” ) . See more at Old Armenian երիվար ( erivar ) .

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /riː.ˈdan/ 

 ( Dari, formal ) IPA ( key ) : [riː.d̪án] 

 ( Dari, formal ) IPA ( key ) : [riː.d̪án] 
 ( Kabuli ) IPA ( key ) : [riː.d̪án] 

 ( Hazaragi ) IPA ( key ) : [ri.d̪án] 

 ( Iran, formal ) IPA ( key ) : [ɹiː.d̪ǽn] 

 ( Tajik, formal ) IPA ( key ) : [ɾi.d̪án] 

 Rhymes: -an 

 Readings

 Classical reading ? 

 rīdan

 Dari reading ? 

 rīdan

 Iranian reading ? 

 ridan

 Tajik reading ? 

 ridan

 Verb
 [ edit ] 

 ریدن • ( rīdan  / ridan ) ( present stem رین ( rin ) , Tajik spelling ридан ) ( vulgar ) 

 to shit 
 Synonym: غایط کردن ( ġâyet kardan ) 

 to fuck up , to screw up , to mess up 
 Synonym: گند زدن ( gand zadan ) 

 Conjugation
 [ edit ] 

########## ee07a89e54c2641f
 [ edit ] 

 ریم • ( rim ) 

 filth 

 Retrieved from " https://en.wiktionary.org/w/index.php?title=ریم&oldid=91752967 "

 Categories : Persian lemmas 
 Persian nouns 

 Hidden categories: Pages with entries 
 Pages with 1 entry 

 This page was last edited on 30 July 2026, at 18:13.

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

 ریم 

 3 languages 

 Add topic########## e72d6beda051ecaa

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

 See also: ژنده and زنده 

 Azerbaijani
 [ edit ] 

 Noun
 [ edit ] 

 رنده ( rəndə ) ( definite accusative رنده‌نی ( rəndəni ) , plural رنده‌لر ( rəndələr ) ) 

 Arabic spelling of rəndə 

 Declension
 [ edit ] 

 Declension of رنده 

 singular

 plural

 nominative

 رنده 

 رنده‌لر 

 definite accusative

 رنده‌نی 

 رنده‌لری
```


## [2026-09-05T20:33:45.134Z] TOOL CALL #32: Bash

```json
{
 "command": "grep -n -i \"persian\" data/verification/sources/web/e72d6beda051ecaa.txt | head; echo \"=== fetch more ===\"; for u in \\\n \"https://en.wiktionary.org/wiki/%D9%84%D9%87%D8%B1%D8%A7%D8%B3%D8%A8\" \\\n \"https://en.wiktionary.org/wiki/%D8%A7%D9%84%D9%88%D9%86%D8%AF\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%83er-\" \\\n \"https://en.wiktionary.org/wiki/%E0%A4%B0%E0%A4%A6\" \\\n \"https://www.etymonline.com/word/rival\" \\\n \"https://www.etymonline.com/word/run\" ; do python3 tools/fetch_source.py \"$u\" --note \"page 156, root Er 1/Or\"; done",
 "description": "Fetch more sources"
}
```


### [2026-09-05T20:33:51.233Z] TOOL RESULT

```
85: Persian 
87: Toggle Persian subsection 
233: From Persian رنده ( randa ) .
273: Persian
279: From Middle Persian *randag , found also in early Classical Arabic as  رَنْدَج ( randaj ) , derivative to the verb رَندیدَن ( randidan , “ to grate, to scrape ” ) .
284: ( Classical Persian ) IPA ( key ) : /ran.ˈda/ 
324: Iranian Persian
365: Ottoman Turkish terms borrowed from Persian 
366: Ottoman Turkish terms derived from Persian 
371: Persian terms inherited from Middle Persian 
=== fetch more ===
/home/sfmqrb/git/rishe/data/verification/sources/web/9e8dfad3cf93e844.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ec8db32a1def647f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/74fc390769b5e5e7.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e27a2b27b24b878b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a3de197a826362e1.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/704467a24d42db61.txt
```


## [2026-09-05T20:33:55.144Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in 9e8dfad3cf93e844 ec8db32a1def647f e27a2b27b24b878b; do echo \"########## $f\"; wc -c $f.txt; sed -n '55,140p' $f.txt | grep -v \"^ *$\" | head -40; done",
 "description": "Inspect Lohrasp, Alvand, rad"
}
```


### [2026-09-05T20:33:56.920Z] TOOL RESULT

```
########## 9e8dfad3cf93e844
162 9e8dfad3cf93e844.txt
########## ec8db32a1def647f
156 ec8db32a1def647f.txt
########## e27a2b27b24b878b
3605 e27a2b27b24b878b.txt
 1 
 Varhadi 
 Toggle Varhadi subsection 
 1.1 
 Etymology 
 1.2 
 Adjective 
 1.3 
 Further reading 
 Toggle the table of contents 
 रद 
 3 languages 
 हिन्दी 
 Русский 
 संस्कृतम् 
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
```


## [2026-09-05T20:34:03.669Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"### h3er\"; wc -c 74fc390769b5e5e7.txt; grep -n -A40 \"Proto-Indo-European\" 74fc390769b5e5e7.txt | sed -n '1,80p' | grep -v \"^[0-9]*- *$\" | head -50",
 "description": "Inspect PIE h3er page"
}
```


### [2026-09-05T20:34:05.522Z] TOOL RESULT

```
### h3er
6505 74fc390769b5e5e7.txt
1:URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%83er-
2-FETCHED: 2026-09-05T20:33:48Z
3-STATUS: 200
4:TITLE: Reconstruction:Proto-Indo-European/h₃er- - Wiktionary, the free dictionary
6:Reconstruction:Proto-Indo-European/h₃er- - Wiktionary, the free dictionary 
8- Jump to content 
10- Main menu 
12- Main menu
14- move to sidebar 
15- hide 
17- Navigation
19- Main page 
20- Community portal 
21- Requested entries 
22- Recent changes 
23- Random entry 
24- Help 
25- Glossary 
26- Contact us 
27- Special pages 
29- Search 
31- Search 
33- Appearance 
35- Donations 
37- Create account 
39- Log in 
41- Personal tools 
43- Donations 
45- Create account 
--
57: Proto-Indo-European 
59: Toggle Proto-Indo-European subsection 
61- 1.1 
62- Root 
64- 1.1.1 
65- Extensions 
67- 1.1.2 
68- Descendants 
70- 1.1.3 
71- Derived terms 
73- 1.1.4 
74- Alternative reconstructions 
76- 1.2 
77- See also 
79- 1.3 
80- References 
82- Toggle the table of contents 
84: Reconstruction:Proto-Indo-European/ h₃er- 
86- Add languages 
88- Reconstruction
```


## [2026-09-05T20:34:08.530Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && sed -n '120,230p' 74fc390769b5e5e7.txt | grep -v \"^ *$\"",
 "description": "Print h3er root content"
}
```


### [2026-09-05T20:34:10.153Z] TOOL RESULT

```
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
 *h₃er- ( perfective ) [ 1 ] [ 2 ] [ 3 ] 
 to move , to stir 
 to rise , to spring 
 Extensions
 [ edit ] 
 *h₃er-dʰ- 
 *h₃r-ey-H- 
 *h₃r-ew- 
 Descendants
 [ edit ] 
 Proto-Tocharian: *er- ( “ to evoke, bring forth, produce ” ) [ 4 ] 
 Tocharian A: ar- 
 Tocharian B: er- 
 Proto-Indo-Iranian: 
 Proto-Indo-Aryan: 
 Sanskrit: ऋ ( ṛ ) , अर् ( ar ) , इर् ( ir ) , ईर् ( īr ) 
 Derived terms
 [ edit ] 
 Terms derived from the Proto-Indo-European root *h₃er- (86 c, 0 e) 
 *h₃r̥tó ~ *h₃rn̥tó ( mediopassive athematic root aorist ) 
 *h₃r̥-néw-ti ~ *h₃r̥-nw-énti ( new-present ) 
 *h₃r-oi- ~ *h₃r-i- [ 5 ] 
 Proto-Anatolian: 
 Hittite: 𒀀𒊏𒀀𒄿 ( a-ra-a-i , “ to arise; lift, raise ” ) 
 *h₃r̥-yé-ti ( yé-present ) or *h₃ér-ye-ti ( ye-present ) 
 Proto-Italic: *oriōr ( “ to rise ” ) ( see there for further descendants )
 *h₃i-h₃ér-ti ~ *h₃i-h₃r-énti ( reduplicated present ) 
 Proto-Indo-Iranian: *HiHárti 
 Proto-Indo-Aryan: *HiHárti 
 Sanskrit: इय॑र्ति॒ ( íyarti ) , इ॒यर्ति॑ ( iyárti ) 
 Proto-Iranian: *HiHárti 
 Old Avestan: 𐬍𐬭𐬀𐬙𐬏 ( īratū , 3sg.impv. ) 
 *h₃ér-os ~ *h₃ér-es-os 
 Hellenic:
 Ancient Greek: ὄρος ( óros ) 
 *h₃réwnos 
 Anatolian:
 Hittite: 𒀀𒊒𒈾𒀸 ( a-ru-na-aš ) 
 > ? *h₃érō ( “ eagle ” ) ( see there for further descendants )
 Unsorted formations 
 Armenian:
 Old Armenian: արմն ( armn ) , արմ ( arm ) 
 Armenian: արմ ( arm ) 
 ( perhaps ) > ? Old Armenian: արթ- ( artʻ- ) 
 Proto-Balto-Slavic: 
 Proto-Slavic: *ortь ( see there for further descendants )
 > ? Proto-Germanic: *arniz 
 ⇒ ? Proto-Germanic: *ernustuz ( see there for further descendants )
 Hellenic:
 Ancient Greek: ὀρῑ́νω ( orī́nō ) 
 Ancient Greek: ὄρμενος ( órmenos ) , ὅρμενος ( hórmenos ) → Latin: ormenos 
 Ancient Greek: ὀροθῡ́νω ( orothū́nō ) 
 > ? Proto-Tocharian: *ār- [ 6 ] 
 Tocharian A: ār- 
 Tocharian B: ār-
```


## [2026-09-05T20:34:19.205Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"radati\" POK_full.txt | head -10; echo \"=== er-5 ===\"; sed -n '28527,28600p' POK_full.txt | head -40",
 "description": "Pokorny radati and er-5"
}
```


### [2026-09-05T20:34:19.269Z] TOOL RESULT

```
1917:and *akusi\\aye maybe derived according to Zupitza GG. 89 from a gradating *aguesT: 
2558:(j)agnbcb "lambkins' contain full gradation. Or is placed Indo Germanic *og"(h)no- : to 
3276:secondary Germanic vowel gradation a: i/ or from *aRu/<o- with assimilation a in i/?) 
3728:(with unclear sound gradation); (common Celtic -ns- > -nn-), Lithuanian a/rs//s following 
5901:ff., Kretschmer Gl. 18, 205 here AnsAAwv, AnoAAwv, with vocal gradation Thessalian 
6448:with o gradation 0/777' wall, mural ' {*ork-mo-?)\ 
6497:As form mit ogradation (or at most with or= j) covers Latin Orcus " Orcus, the infernal 
7778:that combined 6- gradation Perf. wohsio the paradigm; see Brugmann IF. 32, 180, 189); 
10334:Latin (*bhargh"eh2-to-) barbatus. Old Church Slavic bradati,, Lithuanian barzdotas 
10821:ni-s, or with o-gradation as gr. cpajvn?); Old English M/5/7'brag, boast' (as Latin forirovn 
=== er-5 ===
Page(s): 332-333 

Root / lemma: ers- : orsos 

Meaning: behind; tail 

Material: Armenian or" buttocks ' (mostly PI. or-k\ /-stem); 

gr. oppoq m. " buttocks ' (in addition oupa: f. "tail' from *orsJa) = 

Old High German ars. Old English earsm., Old Icelandic ars, rass' buttocks' = 

Hittite a-ar-ra-as {arras), Dat. ar-ri-is-si {arrisi); whose -s/enclitic pronoun; 



e-grade Old Irish err{ *ersS) f. 'tail, end' (also of chariot), therefrom eirr^ chariot 
combatant ' ( *ers-et-s). Gen. erred. 

References: WP. I 138, Couvreur H 98, Pedersen KG. II 101. 

See also: it is often placed 'elevation, protrusion, preceding body part ' to e/"-5(above S. 

326). 

Page(s): 340 

Root / lemma: es-en-, os-en-, -er-{*hek"'-en-\n centum languages) 

Meaning: harvest time, *summer, *autumn 

Note: 

Root /lemma: es-en-, os-en-, -er-\ harvest time, *autumn' : Root /lemma: ues-f. spring'. 

Note: in Germanic also from the harvest- and generally Feldarbeit and the earnings out of 

it 

Material: With a relationship as between Lithuanian vasaraan6 vasara' summer' : Old
```


## [2026-09-05T20:34:19.740Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && ls; grep -n \"\\[pdf page\" WLD_Bd1_pages.txt | sed -n '130,150p'",
 "description": "Locate WLD Bd1 page 136"
}
```


### [2026-09-05T20:34:19.798Z] TOOL RESULT

```
WLD_Bd1_1930_dli_70244_djvu.txt
WLD_Bd1_1930_dli_70244_text.pdf
WLD_Bd1_pages.txt
WLD_Bd2_1927_dli_106624_djvu.txt
WLD_Bd2_1927_dli_106624_text.pdf
WLD_Bd2_pages.txt
```


## [2026-09-05T20:34:26.224Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"scarifies\" POK_full.txt | head; echo \"=== er-5 lemma ===\"; sed -n '28468,28530p' POK_full.txt | head -50",
 "description": "Find radati and er-5 in Pokorny"
}
```


### [2026-09-05T20:34:26.297Z] TOOL RESULT

```
27433:influence of likhati' scarifies '); 
28261:further here or to er-50\6 Indie radati' scratches, digs, hacks, scarifies ', vf-radati^ 
69975:reik(h)-. Old Indie rikhati, likhati^ scarifies ', rekha, lekha^crack, line, line'; gr. spsiKU) 
79858:man sich reiftt, scarifies '), ocpaAa^, aacpaAa^, anaAa^, aanaAa^ ' mole ' ('die Erde 
=== er-5 lemma ===
Page(s): 332 

Root / lemma: er-5, era-, thematic (e)r-e- 

Meaning: rare, loose, crumbly 

Material: Old Indie //e with Abl., Akk. " with exclusion of, without, except, besides' (Lok. a 

participle *rta- " separated, secluded '), nirrti-h' resolution, decay, downfall, ruin'; ar-ma- 

Pl. " debris, ruins ', armaka-^ trijmmerhaft ' or n. " TriJmmerstatte ' (meaning somewhat 

doubtful); Va-in /?/77a- "wound'; themat. *{e)r-e- in v/ra/a-' standing apart, leaky, rare '; 

Maybe zero grade in alb. {*era/a-) ra/fe'rare'. 

gr. £pr|po(;, Attic spHMO'^ lonely '; 

quite doubtful Latin Aams "having wide interstices between its parts, of a loose texture, 
not thick or dense, thin, loose, scattered, scanty, far apart; milit. in loose order; in gen. 
rare, infrequent; sometimes extraordinary, distinguished. Adv. raro, rare, seldom, rarely ' 
( *er9-rd-s), rather credible rete'net, thread' (compare under Lithuanian ret/s, Latvian refa); 

maybe alb. {*rete) rrJete'neV 

Lithuanian yru, Irt/" separate, resolve, distinguish', pa/ras' lax, loose '; ret/s m. " phloem 
sieve ' (with unoriginal second accent, as often in /-stems), Latvian reta, rete'scar', rem' 
rudzi^ leaking standing rye '; Lithuanian ertas^w\6e, far, spacious ' ("*standing apart '); 



from the light basis retas'\h'\n, spacious, seldom' (from the themat. root form *(e)r-e-, as 
also:) /lesi/^s 'seldom, thin', paresvis^ sparse '; 

Old Church Slavic 0/7// "dissolve, overthrow, destroy' (Kaus. *ore/d'make break up'), 
Serbo-Croatian Oit'd/'/// "prostrate, throw down', Czech obor/t/" destroy' , russ. razonfbds. 

Maybe alb. rrezonj'bnng down' : russ. razorftb 

Old Indie /o'/7a/r" especially, peculiar, particular', ardha-h^ part, side, half, ardha-^\\a\f, 
n. "part, half; 

Lithuanian ardali, -///"separate, split' (Kaus., as Church Slavic oriti) ; erdvas^\N\6e, 
capacious', Latvian ardaws, ifdens^ lax, friable', e/r/s" lax, commodious (capacious '), 
ifdi't, /?d/nat loosen, separate', erzu, erdu, eAs/ "separate'. 

re-dh_. 

Old Church Slavic redhk-b "seldom' (probably shifted stress, compare Czech ridky, 
sloven, redak, in spite of serb.-kroat. rijedkT, rtdkl);
```


## [2026-09-05T20:34:35.585Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for p in 329 330 331; do L=$((p+8)); echo \"=== POK p.$p (leaf $L) ===\"; awk -v n=$L 'BEGIN{RS=\"\\f\"} NR==n+1' POK_01.txt | head -50; done",
 "description": "Print Pokorny scanned pages 329-331"
}
```


### [2026-09-05T20:34:37.727Z] TOOL RESULT

```
=== POK p.329 (leaf 337) ===
t.  Suffix  in  dvej-öpas  , zweifach'  usw.,  sowie das  Suffix  in  illyr.  VN  Hadriopes,  JeggloTTsg,  usw.  (??);
hierher  auch  die  slav.  Präpos.  o  ,um,  an'  (*op);  zum  Zusammenfall  mit idg.  obhi  s.  oben  S.  287,  Meillet  Slave  commun^  155  f.,  Trautmann  1;
über  hitt.  appa  usw.  s.  oben  S.  53;  in  der  Bedeutung  entspricht  es  eher dem  gr.  iTti  als  dem  gr.  d/rd;
325
das  Lyk.  kennt  nur  die  erweiterten  Formen  epn-,  epüte  ,nach* ;
über  die  toch.  Gen.-Endung  A  -äp,  B  -epi,  die  man  hierher  stellen  könnte (auch  im  Lit.  wird  der  Gen.  durch  epi  verstärkt),  s.  auch  Pedersen  Toch.  50  ff.
WP.  I  122  f.,  Pedersen  Lyk.  und  Hitt.  23,  Schwyzer  Gr.  Gr.  I  325 550',  620,  628,  63P,  Trautmann  1.
gp/.  , Gefährte,  Kamerad,  traut'.
Ai.  dpi-  , Freund,  Bundesgenosse',  äpyam  »Freundschaft,  Genossenschaft';
gr.  ^TCLog  , freundlich,  mild;  beistehend'.
Vielleicht  zu  *epi  ,nahe  hinzu,  J/r/',  so  daß  *epi-s  (und  *epi-os)  den ,nahe  bei  einem  weilenden,  den  hilfreichen  Gefährten'  bezeichnet  hätte, -^voraus  auch  , traut'.
Zu  ^jffLog  aus  dem  Gr.  noch  ^Ttdof^ac  ursprüngl.  (?)  ,heile'  (vgl.  f/'/rta (paof.iayi(x  TtdoGsiv)  und  daraus  ,flicke'  ?
WP.  I  121  f.
epop,  opop  Ruf  des  Wiedehopfs.
Arm.  popopf  npers.  püpü  , Wiedehopf* ;
gr.  irtOTtoL  noTtono  Ruf  des  Wiedehopfs,  ^^Ttoxp,  -onoq  ,Wiedehopf', ertcjTza'  dXsxrgvöva  äyoLov  Hes.  (-wtt-  wohl  durch  Anlehnung  an  -a>i//); artacpog'  ertoxp^  rd  oqveov  (assimiliert  aus  ^STtacpog^  das  im  Ausgang  nach dem  Tiernamensuffix  -acpog  umgebildet  ist);
lat.  upupa  , Wiedehopf ' ;
ndd.  Hupphupp  u.  dgl. ;  nhd.  Wiedehopf,  ahd.  wituhopfo,  as.  widohoppa ist  eine  Umdeutung  nach  germ.  widu-  (idg.  uidhu-)  ,Baum,  Holz'  und mhd.   hopfen  , hüpfen' ;
lett.  puppukis  , Wiedehopf.
Ähnlich,  aber  unredupliziert,  osorb.  hupak,  poln.  hupek  , Wiedehopf, osorb.  hupac  ,wie  ein  Wiedehopf  schreien',  vgl.  auch  allgemeiner  slovak. hüpati  , schreien',  russ.  alt  chupsti  sja  ,sich  rühmen'.
WP.  I  123  f..  Kluge  11  S.  689.
eph'  jkochen'.    Nur  Gr.  un(l  Arm.
Arm.  epem  , koche' ;
gr.  sipü)  , koche',  Fut.  ixfjT^aco,  Partiz.  ecpS-ög  (erweist  an  sich  nicht  idg.  ph, da  auch  *S7t(7TÖg  zu  ecpd-og  führen  mußte);  doch  wird  sxpu)  5o-Präs.  sein (vgl.  deipo)  :  öecpo))  und  arm.  p  ein  idg.  ph  fortsetzen.
WP.  I  124,    Schwyzer  Gr.  Gr.  I  326,  706.
i.  er-,  or-  ,Adler^,  arm.  gr.  /größerer)  Vogel  überhaupt^ Arm.  oror,  urur  ,Möwe,  Weihe'; gr.  })Qvxg,  -i&og,  dor.  -ixog  , Vogel;  Hahn^  Henne',  Hqveov  ,Vogel';
326
f
air.  irar,  mir.  auch  ilary  cymr.  eryVj  mbret.  erer  (nbret.  corn.  er  durcK Haplologie,  kaum  =  lit.  eras)  , Adler^  {^eriir-) ;
got.  ara,  aisl.  ari,  gm  (aus  *arnuz),  ags.  earn,  ahd.  aro,  aru  ,Aar,  Adler' mhd.  adel-ar  , edler  Aar',  nhd.  Adler -^  urgerm.  "^aran- =  hitt.  aran--^
lit.  erelis,  dial.  arelisj  apr.  areZie  (lies  arelis),  lett.  ^?'^Z25  (aus  ^rci/^x ,Adler^;
=== POK p.330 (leaf 338) ===
  "halt.  Grundform  *ereUa-,  vgl.  lit.  eras,  äras  , Adler'  (ob  alt?)-
abg.  orhh  (*arila-)  ,Adler^,  russ.  orel,  Gen.  orid;
ob  um.  erilaRj  aisl.  jarl,  ags.  eo?'Z,  as.  erl  ,Mann^,  bes.  ;Vornebmer Mann^,  damit  zu  verbinden  sei  nach  Maßgabe  von  aisl.  jqfurr  , Fürst' eigentlich  ,Eber^,  ist  unsicher;
hitt.  ha-a-ra-as  (haras),  Gen.  ha-ra-na-as  (haranas),  n-St.  , Adler',  wie got.  ara.
WP.  I  135,  Trautmann  13,  Pedersen  Hitt.  41,  Specht  Dekl.  47.
2,  er-,  eri-  ,Bock;  Schaf,  Kuh,  Damtier*^;  vielleicht  ursprünglich  ,Horntier'.    "^
Arm.  or-oj  (assimil.  aus  *er-oj)  ,agnus,  agna',  e^nnj  ,d6:ficxXigj  vitula iuvenca,  bos' ;
gr.  €Qiq)og  (*eri-bho-)  m.  f.  ,Böcldein,  junge  Ziege*^;
lat.  ariesj  -etis  ,Widder^  Mauerbrecher'  (a  nach  a'per,  caper);  umbr. erietu  ,arietem';
air.  heirp  (*erbhl-)  f.  ,dama,  capra',  erh(b)  ,Kuh'  (*erhhä),  mir.  (mit  sekun- därem /-)  ferh(b)  ds.,  nir.  earh,  fearb  f.  ,Rotwild,  Kuh',  schott.-gäl.  earh  ■ f.  ,Reh' ;    zu   kelt.  *erhä  :  Igicpog   vgl.   gr.    oiqcpoq  :  oeqLcpog   ,Insekt' ;    nach Kleinhans  (Et.  Gelt.  1,  173)  hierher  mir.  reithe  ,Widder'  aus  *ri-{o-tio-]         .    ■;
in  apr.  eristian  ,Lämmchen',  lit.  {j)erasj  lett.  jers  ,Lamm^,  litt,  mend  ^ , Lammfleisch'  =  russ.-ksl.  jarina  ,Wolle',  usw.,  sind  wohl  bsl.  *eTO': ,Bock'  und  *jörä-  ,Jahr'  (s.  oben  S.  297)  vermischt  worden;
ahd.  irah  ,Bock'  usw.  ist  aus  lat.   hircus  entlehnt.
WP.  I  135  f.,  WH.  I  67,   Trautmann  70.  ^]
5-  er-  :  or- :  r-,  ursprünglich  athematische  Wurzel  mit  terminativem  Aspekt:  M ,sich  in  Bewegung  setzen,  erregen  (auch  seelisch,  ärgern,  reizen);  in  ST, die  Höhe  bringen  (Erhebung,  hochwachsen),  z.  T.  auch  von  Bewegung nach   abwärts';    Basenformen    er-,    ere-,    er3-(?),   erei-,    ereu-  und     •• (unter   besond.    Artikel)   eres-j    eros-   ,Erhebung',   ernos-  ,Empor-     'j geschossenes',  Partiz.  or-meno-,  r-to-. Zusammenfassungen  bei  Persson  Beitr.  281  ff.,  636  ff.,  767ff._,  836  ff. a.  Basis  formen   er-,    ere-   (einschließlich   paradigmatisch    damit    ver-  ■ einigter  i-  und  w-Formen):  ::   ""
Ai.  redupl.  Präs.  iy-ar-ti  ,setzt  in  Bewegung',  Med.  Irte  (*i-,r-);  gthav.  , iratü  ,er  soll  sich  erheben';  ai.  intensives  Präs.  dlarti]  von  ereu-  (s.  unten
327
S.  331)  rnöti  rnvdti  .erhebt  sich,  bewegt  sich^  (ih'Qvv^L),  ärta  (vgl.  Jjqto), ärata  (vgl.  djqexo]  themat.  wie  rante,  ranta),  Perf.  ära :  bg-cuga,  Fut! arisijati,  Partiz.  rtd-  {irnd-  .bewegt,  erregt^  mit  Verschleppung  des  l  aus irta  oder  echte  Form  einer  schweren  Basis);
av.  ar-  .(sich)  in  Bewegung  setzen,  hingelangen'.  Präs.-St.  ar-:dr9-j iyar-:ir-  (wie  ai.  iyarti-.irta),  Kaus.  araya-,  Partiz.  -drdta--,
5Ä:o-Präs.  ai.  fcchdti  .stößt  auf  etwas,  erreicht',  woneben
=== POK p.331 (leaf 339) ===
  *re-skö  in  apers. rasatiy  .kommt,  gelangt',  np.  rasad  ds. ;
ai.  sam-ard-  m..  sam-drana-  n.  .Kampf.  Wettstreit',  av.  liam-ardna-,  apers. Jiam-arana-  n.  .feindliches  Zusammentreffen.  Kampf,  av.  hamara-  m.  (und mit  th-Forma-ns  hamdvdd-a-  m.)  .Gegner.  Widersacher';  ai.  irya-  ,rührig. kräftig,  energisch'  (kann  zur  z-Basis  gehören),  irin-  .gewaltig,  gewaltsam'. drtha-  n.  m.  .(*wozu  man  gelangt)'  .Angelegenheit.  Sache.  Geschäft;  Gut, Vermögen.  Vorteil',  av.  ard^a-  n.  .Sache.  Angelegenheit.  Obliegenheit. Rechtsstreit' ;
ai.  ft^-,  fti'  f.  .Angriff.  Streit',  av.  -drdti-  .Energie'  (vgl.  abg.  rath)]
ai,  arta-  .betroffen,  versehrt,  bedrängt,  leidend',  ärti-  f.  .Unheil.  Leiden' {^ä-xta-,  -rti-))
ai.  drna-  .wallend,  wogend,  flutend',  m.  ,Woge.  Flut',  dimas-  n.  .wallende Flut'  (formell  =  gr.  eqvog  n. ;  vgl.  S.  328  ahd.  runs)^  arnavd-  .wallend, wogend';  m.  .Flut,  wogende  See'  (wo- Weiterbildung  zu  drna-?  oder  in alter  formantischer  Beziehung  zu  j-nöti?  Letzteres  ist  sicher  für:)  av. ardnu-  m.  .Kampf.  Wettkampf'  ( :  ahd.  ernust  S.  331) ;
von  der  themat.  Wurzelf.  (e)re-  ai.  rdiia-  m.  n.  .Kampf  (versch.  von rana-  m.  .Lust')  =  av.  rdna-  n.  .Treffen.  Kampf.  Streit';  av.  räna-^  rqna-  m. .Streiter.  Kämpfer';
arm.  y-arnem  .erhebe  mich,  stehe  auf;  nach  Pisani  Armen.  4  dazu  ore-ar .Leute'  (s.  unten  lat.  orior)]  mit  -dh-  (vgl.  S.  328  igs-S^w,  igsd^i^ü),  dgo- -^vvoi) :  y-ordor  .pronto'.  yordorem  .ermuntere,  wecke,  reize';  arm  .Wurzel' ( :  ^Qi-iEvog) ;  ordi,  Gen.  ordvoy  .Sohn'  (*ordhno) ;
gr.  ogvV(j,i  .errege,  bewege'  (:  ai.  T'^öti]  vgl.  Schwyzer  Gr.  Gr.  I  696/?; das  0  nach  dgso^ac?),  Aor.  (hgoa,  ^gogov,  h'gGo),  Med.  })gwf.iai^  d)gTO  .erhob sich'.  Fut.  dgov{.iai,  them.  Aor.  djgsTO,  Partiz.  bg^evog^  Perf.  Ugwga  .bin erregt';  mit  og-  als  Iterativvokalismus  ögs-oi-iai,  -ovro  .aufbrechen',  mit er-  noch  egero '  wgurjd^T]  Hes..  egoeo '  ÖLsyslgov  Hes..  sgffr] '  ögfirjcr]  (die  dann durch  öjgsro,  b'gaeo  verdrängten  Formen);  ein  Präs.  *l'QWfiL  (wie  xLgvrji.iL) folgt  aus  dem  kret.  Zevg  "'EnigvvTLog  (Schwyzer  Gr.  Gr.  I  695);  -ogvog in  vsogTÖg  .neugeboren'. d-eogrog  .himmlisch',  usw.;  Kvv-,  ^vY,-6gTag, ^ä-igrrjg] hom.  o-ögog  .günstiger  Fahrwind'  {*ögJ^og,  .das  Schiff  treibend'),  ^gog  m. ;Antrieb';
328
•  ':^
mit  g"22-Erweiterung  eQXO^at  ,komme^  (nur  Präs.),  dgx
```


## [2026-09-05T20:34:52.215Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for L in 341 342; do echo \"=== leaf $L ===\"; awk -v n=$L 'BEGIN{RS=\"\\f\"} NR==n+1' POK_01.txt | head -60; done",
 "description": "Pokorny leaves 341-342"
}
```


### [2026-09-05T20:34:53.983Z] TOOL RESULT

```
=== leaf 341 ===
it'  (*era) ;
got.  rinnarij  rann  ,rennen,  laufen'  (^re-mi-o),  urrlnnan  ,auf gehen,  von der  Sonne',  aisl.  rinna  ,fließen,  rennen',  ahd.  as.  rinnan  ,fließen,  schwimmen, laufen',  ags.  rinnan  und  iernan,  am  ds.;  Kaus.  got.  urrannjan  ,aufgehen lassen',  aisl.  renna  ,laufen  machen',  as.  rennian  ds.,  ahd.  mhd.  rennen^ rante  ,rennen'  (ein  nach  rinnan  mit  nn  ausgestattetes  *roneiö  =  slav. .    roniti  unten  S.  329) ;
schwundstufig  got.  runs  m.  (^-St.),  ags.  ryiie  m.  ,Lauf,  Fluß^,  aisl.  run
329
n.  ^Flüßchen^,  got.  garunjö  .Überschwemmung^,  ahd.  runs,  ruma  ,Lauf des  Wassers,  Fluß^,  runst  f.  ,das  Rinnen,  Fließen,  Flußbett^;  got.  garuns (St.  garunsi-)  f.  ,Straße,  Markt^  (eig.  ,Ort,  wo  das  Volk  zusammenläuft^ ; germ.  runs-\  ai.  drnas-).  In  der  Anwendung  auf  das  Hochkommen' Wachstum  der  Pflanzen  (vgl.  EQvog,  ÜQfxevog)  aisl.  rinna  .emporschießen, wachsen^,  norw.  runne,  rune  ,Zweig^  und  schwed.  dial.  rana  ,in  die  Höhe schießen',  norw.  rane  ,Stange',  mhd.  ran  (ä)  ,schlank,  schmächtig',  ahd.  rono ^Baumstamm,  Klotz,  Span';  ,Erhebung'  überhaupt  in  norw.  dial.  rane ^Spitze,  hervorragender  Felsen,  Bergrücken',  aisl.  rani  ,Schnauze,  Rüssel';
air.  rind  (■^■rendi-)  ,Spitze';  zur  c?(Ä) -Erweiterung  s.  unten;
Diese  Wurzelform  *re-n-  (vielleicht  aus  einem  Präs.  ""re-neu-mi,  *re-nu-o erwachsen)  sucht  man  auch  in  alb.  ferrua  ,Flußbett,  Bachbett'  (per-ren-, Dehnstufe),  prrua  ,Quelle'  {*prer-rua  ,Ausfluß')  und  in  abg.  izroniti  (bsl. *raneiö)  ,effundere',  russ.  ronith  ,fallen  machen  oder  -lassen',  serb.  roniti ,Tränen  vergießen,  schmelzen,  harnen',  got.  -rannjan-^  vgl.  Trautmann  236  f. ;
c?(i2)- Erweiterung  im  lit.  Partiz.  nusirendant,  nusirendusi  von  der  unter- gehenden Sonne,  rindä  ,Rinne'  (stögo  r.  ,Dachrinne'),  ,Krippe',  lett.  randa ,yertiefung,  wo  das  Wasser  abläuft' ;
abg.  rath,  russ.  rath,  skr.  rät  ,Streit'  (*or(9)^i-),  abg.  reth  ds.  ,aemulatio', russ.  reth  ,Zank,  Hader',  abg.  retiti  ,contendere',  russ.  retovathsa  ,sich ärgern',  retivyj  ,eifrig,  hitzig,  heftig,  feurig'  (auf  thematisches  {e)re-  oder *er-ti-  zurückgeführt,  was  durch  russ.  äial.jeretithsa  ,sich  ärgern,  zanken' gestützt  wird);  über  ksl.  ram^m  s.  oben  S.  58  u.  328.
Aus  dem  Hitt.  hierher  (Pedersen  Hitt.  5  f.,  45,  91  f.,  122)  ar-  in
1.  a-ra-a-i  (arai)  ,erhebt  sich',  daneben  a-ra-iz-zl  ds.,  Prät.  3,  PL [a\-ra-a-ir ;
2.  a-i-i  ,kommt'  (altes  Perf.),  Prät.  a-ar-ta  (arta)  oder  ir-ta ;
3.  Med.  Präs.  ar-ta-ri  ,stellt  sich,  steht'  (vgl.  gr.  b'gajga  :  lat.  orior),  3.  Sg. Prät.  a-ar-as  (ars)  ,kam  an';
4.  It
=== leaf 342 ===
erativ  a-ar-as-ld-it  (arsJcit)  ,gelangte  wiederholt'  (vgl.  oben  ai. rcchdti) ;
5.  Kausativ  (vgl.  oben  S.  61)  ar-nu-uz-zi  (^arnuzi)  ,bringt  wohin,  setzt in  Bewegung'  (j-nu-]  vgl.  oben  ai.  rnöti)\  Imper.  2.  Sg.  ar-nu-ut  (arnut) =  gr.  oovv-d-i,  Verbaln.  a-ar-nu-mar  (arnumar) ;
inwieweit  toch.  A  ar-,  B  er-  ,hervor bringen,  verursachen',  mit  sÄ-Kaus. ars-,  ers-  ds.,  nach  Meillet  (MSL.  19,  159)  hierher  gehören,  ist  unsicher ; sicher  fern  bleiben  AB  ar-,  är-  ,aufhören',  mit  s/:-Kaus.  ars-,  ärs-  .verlassen' (ungenau  Van  Windekens  Lexique  6,  22).
h.  Erweiterung  er-ed-  (c?-Präsens ?) :  s.  ered-  .zerfließen',  ai.  drdati, rddti    ,fließt   usw.',  auch    ,beunruhigt' ;    mit   dem   Kaus.    arddyati    ,macht
330  ^
fließen;    bedrängt,    quält,   tötet'    wäre  aisl.  erta  {*artjan)  ^aufstacheln^  an reizen,  necken'   gleichsetzbar,    doch   ist  Verknüpfung   mit   *ardi-   ,Spit2A Stachel'  (oben   S.  63)  mindestens  gleichwertig;    eine   zweisilbige  Form  i' ägaC^ovai'  ige^i^ovaiv  Hes.,  IxQaöog  , Erregung';
weiter   hierher   oder   zu   5.  er-   ai.   rddati   ,kratzt,    ritzt,   gräbt,   hackt^ vi-radati  , zertrennt,  eröffnet';
vielleicht  auch  apr.  redo  ,Furche'  (Persson  Beitr.  667).
c.  Erweiterung  er-edh-:  s.  oben  S.  327  ige-d-cj  usw.   u.  unten  S.  339
d,  Basis  erei-]  und  reis- :ri-}-rolo-s,  ri-ti-  ,Fließen'. Ai.  irya-  s.  oben  S.  327 ; ai.  rinätiy  rinvati  (drinvan)   ,läßt  fließen,  entlaufen,  entläßt',  rlyate    o-q.
rät  ins  Fließen,  löst  sich  auf,  rina-  ,in  Fluß  geraten,  fließend',  rlti-  ,Strom Lauf,  Strich;  Lauf  der  Dinge,  Art,  Weise'  (letztere  Bed.  auch  in  mir. rlan  ,wa7,  manner'),  rit-  ,entrinnend',  raya-  m.  ,Strömung,  Strom,  Lauf Eile,  Heftigkeit',  retas-  n.  ,Guß,  Strom,  Same',  renn-  m.  ,Staub'  (:  aruss, renh  ,Sandbank');  zum  w-Suffix  vgl.  unten  \a.t.  ilvus;
arm.  ari  ,stehe  auf!'  (Persson  Beitr.  769)  Zu  y-afnem,  S.  327;  ^^^^
gr.  lesb.  dgtvcüj  (*dQl-viüj)  ,setze  in  Bewegung,  errege,  reize  zum  Zorn'1* egig,    -löog  ,Streit'    (vielleicht   im   i   zu    unserer   Wurzelform,   falls  nicht i- besser  nach  Schwyzer  Gl.  12,  17  zu  igstdo)  , stütze,  stemme,  stoße,  drängeO^r* ark.   igivvsiv  ,zürnen'  aus  ^Egivvg  eig.  ,die  den  Mörder  verfolgende,  ztiivj nende  Seele  des  Ermordeten'  (??) ;  ''**S'
alb.    geg.   rite    , feucht,    naß',    eig.   ,*fließend'    (*ri
```


## [2026-09-05T20:35:01.731Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==344' POK_01.txt | head -60",
 "description": "Pokorny leaf 343 (printed 331)"
}
```


### [2026-09-05T20:35:03.473Z] TOOL RESULT

```
nete  :  ai.    rindti,  8\&y,'h rinoti) ;  "^
lat.   oriorj    ongo   s.  oben;   rlvus   (*rei-uo-s)   ,Bach';    in    dem   abg.  rtvhUh ,Nebenbuhler'     entsprechender     Bedeutungswendung    rlvlnus    und    rivälU ,Nebenbuhler    in    der    Liebe'    (letztere   Form    Umbildung    nach    aequalis,' södälis),  eigentlich  ,Bachnachbar' ;
wahrscheinlich  hierher  irrltäre  ,erregen,  aufbringen,  erbittern',  jpron^flr«  n^^ ,hervorreizen,  durch  Reiz  hervorbringen,  anreizen,  anlocken',  (wohl  Intensiva zu  einem  *ir-ri-re) ;  '  -
ir.   rlan   ,Meer'   und    (vgl.  ai.  r'iti-)    ,Art,  Weise',   gall.    Renos   (*reinos)^4 ,Rhein'  (ob  auch  nach  Stokes  KZ.  37,  260  ir.  riasc  ,a  marsb',  rzm  ,schlechte8  j^ Wetter'??),  cymr.  rhidio  ,coire'  (:  ags.  rld^  ai.  riti-h),  air.  riathorj  cymr rhaiadr,  acymr.  reatir  ,Wasserfall'  {*riia-tro-)]
ags.  rid  m.  f.,  ride  f.  , Strom,  Bach',  as.  rxth  m.  ,torrens',  mnd.  ride  Vm_ ,Bach,  Wasserlauf',  nhd.  -reid{e)  in  Ortsnamen;  Dimin.  (^rtpulön)  ndd rille  ,Furche  nach  Regen wasser,  Rinne';  weiters  ags.  ä-rceman  ,erheben,  sich erheben',  mengl.  r^men^  engl,  roam  ,umherstreifen',  aisl.  reimudr  ,Umher- streifen',  reimir  ,Schlange',  par  er  reimt  ,da  ist  es  nicht  geheuer,  spukt, reima  ,infestare'  (Bed.  wie  abg.  rijati  ,stoßen').    Über  rinnan  s.  oben.
331
as.
Mit  germ.  s-Erweiterung:  got.  urreisan  ,auf stehen',  aisl.  risa^  ao-s. rtsan  ;Sich  erheben',  ahd.  risan,  mhd.  rlsen  ^steigen,  fallen';  ahd.  reisa ^Aufbruch,  Zug,  Kriegszug,  Reise',  ^ot^urraisjan  ,aufstehen  machen,  auf- richten, erwecken',  aisl.  reisa  ds.,  ags.  rceran  ,erheben,  aufrichten,  er- richten', ahd.  reren  ,fallen  machen,  herablaufen  machen,  vergießen';  ndd. reren  ,fallen',  mhd.  riselen  ,tropfen,  regnen',  nhd.  rieseln^  mhd.  risel  m. ^Regen',  aisl.  blöd-risa,  mhd.  bluotvise  ,blutbespritzt',  afries.  blödrisne  ,blutende Wunde';  aus  , fallen'  wird  ,gefallen'  in  ags.  (ge)rlsan  ,ziemen',  ahd.  garlsan ^zukommen,  geziemen'  (vgl.  die  s-Erw.  abg.  ristati),  mhd.  rkch,  hurtig, schnell'  (vgl.  abg.  riskanije)\
lit.  ry-tas  ,Morgen'  (,*Sonnenaufgang',  vgl.  got.  urreisan),  lett.  rietu, -6Ju,  -et  ,hervorbrechen,  aufgehen  (z.  B.  vom  Tag),  hervorströmen',  riete ,Milch  in  der  Mutterbrust'  (vgl.  formal  ai.  reta-)]
slav.  "^raia-  m.  ,Strömung'  ( :  oben  ai.  raya-h  m.  ,Strom,  Lauf)  in  abg. izrojh  ,Samenerguß',  s^rojh  ,Zusammenfluß',  naroj  , Andrang',  roj  ,Bienen- schwarm'  (*roto-s);  dazu  reka  (*roi-ka)  ,Fluß';  slav.  *reiö  ,stoße'  in  aksl. rejqj  rejati  ,fließen'  (nslav.)  und  ,stoßen,  drängen'  (wie  dgirco  ,bewege'); dazu  ablautendes  aksl.  vy
```


## [2026-09-05T20:35:42.331Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==345' POK_01.txt | head -45",
 "description": "Pokorny leaf 344"
}
```


### [2026-09-05T20:35:46.543Z] TOOL RESULT

```
nngti  ji^co^slv',  ririQtis^  ,ruere';  aruss.  rint  ,Sand- bank',  klr.  rin  ,Sand,  Flußgeröll'  (vgl.  ai.  renn-);  in  anderer  Bed.  (s.  oben zu  lat.  rlvlnus)  abg.  rbVhm  ,Nebenbuhler'  rhvenije  ,£Qig,  igd^sia^  6ech.  fevniti ,nacheifern',  poln.  rzewnic  ,bewegt  machen'.
Mit  s-Erw.  bsl.  *reistiö  in  abg.  ristq,  ristati  ,laufen',  riskanije  ,cur- sus',  lit.  raistas  (,Laufzeit'  =)  ,Brunstzeit',  lett.  rlests  ds.,  lit.  ristas ,schnell',  ri§ciä  Instr.  Sg.  ,im  Galopp'.
e.  Basis  ereu-]  er-nu-  ,Wettkampf',  or-uo-  ,eilig'.
Ai.  fnöti  (Perf.  ära  aber  idg. ^*öra),  arnavd--^  av.  ardnu-  s.  oben  S.  327;
ai.  drvan-,  drvant-  ,eilend,  Renner',  av.  aurva-,  aurvant-  ,schnell,  tapfer' ; vielleicht  av.  auruna-  ,wild,  grausam,  von  Tieren';  sehr  unsicher  ^\.  rü-rd- jhitzig,  vom  Fieber';
gr.  0Qvv(.u,  odgog  s.  oben;  altes  Kausativ  doovw  ,stürze  mich,  stürme los',  ävoQOVo)  ,springe  auf  (wohl  als  *oqov\<j]o}  zur  s-Erw.,  s.  unten);  vgl. Schwyzer  Gr.  Gr.  I  683;
lat.  ruö,  -ere  ,rennen,  eilen,  einherstürmen';
mir.  rüafhar  {*reu-tro-)  ,Ansturm',  cymr.  rhuthr  ds.,  air.  rü(a)e  ,Held' {*reu-io-)]  hierher  die  gall.-brit.  FIN  *Ai-vä,  engl.  Arroio,  frz.  Erve,  Auve (*fwä);  messap.  FIN  Arvö]
as.  aru,  ags.  earu  ,hurtig,  bereit,  flink',  aisl.  grr  ,rasch,  freigebig^ {*arioa-  =  av.  aui-va-]  hierher  als  ursprüngl.  ,freigebig'  vielleicht  auch got.  arwjö  ,unentgeltlich,  umsonst',  ags.  earwunga,  ahd.  ar{a)wün  ,gratis, frustra',  arod  ^kraftvoll,  flink';  ahd.  ernust  s.  S.  328.
332
f
ag'S.  reow  ,aufgeregt^   stürmisch,   wild,   rauh^,  got.  unmana-rlggics  ,wil(i grausam^  ,  -k;.
Erweiterung  reu-s-:
Ai.  rösatij  rusdti  ,ist  unwirsch^,  rusitd-,  rustd-  ,ergrimmt^;  ..^^
schwed.  rüsa  ,daherstürmen,  eileii'^,  mnd.  rüsen  ,rasen,  toben,  lärmen«  ^ rüsck  ,Rausch^,  aisl.  rosi  ,Sturmbö^,  raust  ,Stimme^,  aschwed.  ruska  ,her-  B vorstürmen,  eilen^;  ^^'
[aber  got.  raus  n.,  mit  gramm.  Wechsel  aisl.  reyrr  m.,  ahd.  röi^  ^Schilf.  - rohr^,  rörea  ,Röhre^  (^rauziön),  mit  Stammbetonung  (wie  got.)  schwed.  I. rysja^  ahd.  rüssa,  rüsa,  riusa  f.  ,Reuse^,  weitergebildet  mit  Ä-Suffix  a^s.  '■^- rysc  f.,  mhd.  rusch(e)  f.  ,Binse^,  bleiben  wohl  fern];  ^
lit.  ruosüs  ,geschäftig,  tätigt,  lett.  ruo§s  ds.,  lit.  rnoHü,  ruosiaü,  rimti ,besorgen^,  reflex.  ,sich  bemühen^;
slav.  "^ruchh  in  russ.  ruch  ,Unruhe,  Bewegung^,  rwcÄww^
```


## [2026-09-05T20:35:59.990Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KNT leaf 185 (p.170) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==186' KNT.txt | head -40",
 "description": "Kent p.170"
}
```


## [2026-09-05T20:36:00.208Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SYN leaf 302 (p.278) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==303' SYN.txt | head -45",
 "description": "Buck p.278"
}
```


### [2026-09-05T20:36:01.622Z] TOOL RESULT

```
=== KNT leaf 185 (p.170) ===
ugh not mentioned in the Behistan inscription, must have followed in the same or the next year.
V. THE ACCESSION OF XERXES.
In XPf, Xerxes gives us an account of his sue- cession to the throne: Darius had a number of sons, but—-as was Ahuramazda’s desire—he made Xerxes (presumably not his eldest son, though this is not stated in the inscription) the ‘greatest after himself; and when Darius ‘went from the throne,’ Xerxes—as was Ahuramazda's desire—became king on the throne of his father.
The account given by Herodotus 7.1-4 agrees with this, but gives more details: After Darius re- ceived the news that his forces had been defeated at Marathon and somewhat later that Egypt had risen in rebellion, he started preparations for one campaign against the Athenians and another against the Egyptians. Àt this time there was a dispute between Artobazanes, eldest son of Darius by his first wife, a daughter of Gobryas, and Xerxes, eldest son of Darius by Atossa, daughter of Cyrus the Great, whom Darius had married
after his accession to the throne, as to which should have the succession. On the advice of Damaratus, exiled king of Sparta, Xerxes went to his father and pressed his claim on the ground that he was the oldest son of Darius the King, while Artobazanes was only the oldest son of Darius the private individual. Darius approved the claim, though perhaps the argument was not really needed (Atossa as daughter of Cyrus must have had great influence with Darius, and Xerxes was probably the ablest of Darius's sons), and named Xerxes to succeed him. Before he had finished the preparations for the campaigns, Darius died; whereupon Xerxes ascended to his father's throne.
5 Kent, JNES 2.109-10 ; cf. R. A. Parker, AJSLL 58.373-7. $ Parker, l.c.
164
PART III. LEXICON
This Lexicon includes a concordance to the words in the inscriptions, as well as materials for etymological comparison.
The alphabetic orderisáf dk zgejt6 edn pfo тутіоѕ §zh, while final y and v are disregarded (thus пату has the alphabetic place of nai, and pre- cedes naiba-). Raised letters inserted to show sounds omitted in the OP system of writing also have no effect on the alphabetic order.
References to Part I (the Grammar) are marked by §; they include all mentions of the word or form which add to the information given in the Lexicon, but are not in all instances complete list- ings. The Chapter on Syntax is only sparingly re- ferred to in this Lexicon, since the citations in that Chapter are mostly for passages rather than for words; there is an Index of Passages at the end of the Chapter.
а adv. as prefix and prep. ‘to’; Av. Skt. à, prep. with acc. and abl., ‘to, as far as’ (also with other uses and meanings); pIE *à if = Lt. à ‘from’ (Sturtevant, Lg. 15.145-54), or *0 if = Gk. ó- in ó-xeayós ‘(lying round about), ocean’.
(1) Prefix with verbs ay-, zšnav-, gam-, grab-, jan-, bar-, mà-, yam-; in verbal nouns dyadana-, dvahana-, and in the second parts of compounds Adiyabaukna-, Ariyáramna-, Bagabigna-, also in Akaufaciya-.
(2) Postposition attached to loc. sg. and pl. ($270.1V) and in conj. yada.
(3) Prep. with abl.: yàtà à ‘as far as’, DPh 6, 7; DH 5, 6.
(4) Prep. with adv.: DSe 48.
! a- neg. prefix before consonants (867, 67.1, 0182.1; an- antevocalie, q.v.): Av. Skt. a-, Gk. a~, Lt. ?n-, Сте. un-, pIE *n-. See akarta-, ax áaina-, axsata-, Anümaka-, ayaumani-.
* a- demonst. ‘this’: Av. a- as in GAv. gsm. ahé, Skt. a- as in gsm. asyd, Gk. lsn. є 40, Lt. nsn. tod in ecce ‘lo’; pIE *e-. See also aciy, ada-. Decl., $199.
anã ism. DPe 8 (not to Av. Skt. ana-, cf. Mt. MSLP 19.49-52); XPa 14 (with Wb. KIA 109, Mt. Gr. $326; translated by АКК. a-ga-’, Elam. hi ‘this’, which refutes interpretation of Bv. Gr. $368,
$388, as prep. w. inst. ‘throughout’, Av. ana with ace. ‘along, on’, Gk. дра 'along. ahyāyā lsf, DB 447; DNa 11; DSd 2°; DSe 10; DSf 7, 15; DSg lf; DSi lf, 4; DS} 1°; D8m 5°; D8s If, 3°; DSy 2; DZb 3; DZc 5f; DE 17; XPa 8f; XPc 7; ХВ 12, 24; XPh 9f; XPj; XV 13; A!Pa 13; РЬ if; Аа 1; Ае 4; A’Sdb 1 (ahyd de, $52.VI) ; A?Ha If; А°Не 9, 16f; А#Ра 11; Wb 6; We 7f; Wd 7. ahiydyd ($27) XPb 17; XPd 12; XPjv; XE 17.
aita- demonst. ‘this’ ($260. IIT, $266): Av. адіа-, Skt. elá, PAr. *айа-. айа nsn. ($202) DB 1.44, 45; DNa 48. aita-maty DNb 31. ай�
```


### [2026-09-05T20:36:05.057Z] TOOL RESULT

```
=== SYN leaf 302 (p.278) ===
 ChSl.  potit i, ie Sw. _—svelt SCr. — znoj (pot) ae sudor Ris swat Boh. pot eee eae om Sven feet ee Ms, allus Du. —_zweet Skt.  sveda- BR. chtoys Saw sueiz Av. —_-z"atéa-
Oue, Sweiz
NHG _ schweiss
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
on aa’ ee
—— ee eee ee
Digitized by Arya Samaj Foundation Chennai and eGangotri
The majority of the words for ‘sweat’ belong to an inherited group pointing to an IE word for this notion. In most of the others ‘sweat’ is a specialization of ‘heat’. Noun and verb are regularly parallel, and in this case it is the nouns that are listed.
1. Derivs. of IE *sweid- (in part with r-suffix). Walde-P. 2.521. Ernout-M. 997.
Grk. tdpas, NG idpwras (for accent, ef. Hatzidakis, Meo. 1.190, 2.91); Lat. sudor (> It. sudore, Fr. sueur, Sp. sudor, Rum. sudoare); W. chwys, Br. c’houez; ON sveiti, OE swat, etc., general Gme. (ME swet, NE sweat fr. the vb. ME swete, OF sw@tan); Lett. sviedri (pl.); Skt. sveda-, Av. x*aéda-; Arm. k‘trtn, Alb. dirsé, djersé.
2. Rum. nddugeald, fr. nddugi ‘make Sweat, sweat’, fr. ndduf ‘sultriness,
264. SELECTED INDO-EUROPEAN SYNONYMS
closeness, asthma’, this a loanword fr Slavic, SCr. neduh ‘asthma’, etc. 4 ne-+duh beside dah ‘breath’, 4.51), Tiktin 774, 1030. :
3. Ir. allas, NIr. allus, etym.? (Mac. bain 162 as *yas-l- : W. tas ‘boiling seething’, Grk. téw ‘boil’, ete.; not in Walde-P. 1.208, Stokes 228).
4. Lith. prakaitas : kaisti, Lett, kaist ‘become hot’, etc., OHG heiz, ON heitr, OE hat ‘hot’ (parallel ¢- and d- extensions of an IE *kdi-). Walde-P. 1.327,
5. ChSl. pott, ete., general Slavic, (but SCr. only dial.) fr, *poktit : Chl, pekit ‘heat’, pestz, pekq ‘bake’, Lat, coquere, Skt. pac- ‘cook’, ete. Walde-P, 2.18. Briickner 432.
SCr. znoj = ChSI., Boh., Russ, 2noj, Pol. zndj ‘sultry heat, etc.’ Briickner 655.
4.56 SPIT (vb.)
Grk.  rriw Goth. speiwan Lith. spiauti NG ss griw ON hrekja, spyta Lett. spl/aut Lat. spuere Dan. spyite ChSl.  pljtvati It. spulare Sw. spotta SCr.  pljuvati Fr. cracher OE sp@lan, hr@can, spyt- Boh. _ plivati Sp. escupir tan Pol. plué Rum.  scuipa ME spete, spite (reche) Russ. plevat’ Tr. saile (sb.) NE spit Skt. sthiv- NIr.  sailighim Du. spuwen Av. spama- (sb.) W. poert OHG = spiwan
Br. skopa, tufa MHG spi(w)en
NHG  speien, spucken
The majority of the words for ‘spit’ are of imitative origin, and most of these belong to an inherited group, which, though partly affected by new imitative associations, clearly reflect an IE ex- pression.
1. IE *spyéu-, spyu-, etc. Most of the forms included here are derivable by regular phonetic processes from init. *spy-, but some owe their form to new associations. Walde-P. 2.683. Ernout- M. 969.
Grk. rriw, NG pop. drive, drs, $7; Lat. spuere, frequent. sputare (> It. spu- tare, OF r. espuer); Goth. speiwan, Du. spuwen, OHG spiwan, spian, MHG spi(w)en, spiien, NHG speien (in the older language also ‘spew, vomit’, as chiefly OE spiwan, ON spyja, cf. 4.
```


## [2026-09-05T20:36:14.847Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KNT p.170 try leaf 191 ===\"; awk 'BEGIN{RS=\"\\f\"} NR==192' KNT.txt | head -12; echo; echo \"=== SYN excrement ===\"; grep -n \"EXCREMENT\\|Excrement\\|excrement\" SYN.txt | head -8",
 "description": "Kent p.170 and Buck excrement"
}
```


### [2026-09-05T20:36:17.237Z] TOOL RESULT

```
=== KNT p.170 try leaf 191 ===
 formed like Gk. &exero to root *segh-, ёттєтө to root *pet- (JAOS 62.269; 855.IT, §103.I1).
amala adv. ‘thence’: demonst. stem ama-, found (though rarely) in Skt., + adv. -tos, as in Skt. tátas ‘thence’, Gk. ёктоѕ ‘outside’, Lt. caelitus ‘from the sky’: Buck, Lg. 3.4-5; Jn. quoted by Gray, JRAS 1927.101: ef. Kent, JAOS 51.231. Hardly, with Gray, JRAS 1927.99-100, and Hz. ApI 65-6, the same as Skt. abl. asmat remade to *asmatas, with -tos ending. DPh 6, 7; DH 5, 6.
отида, see maub-.
ay- vb. ‘go’: Av. ay- (pres. aiti), Skt. i- (pres. éti), Gk. «о, Lt. it: conj., §208. Cf. also youviyd-. айу ($69) DZe 10. aii imf. (§72, 6228.11) DB 1.98; 2.67; 3.35, 43.
à + ay- ‘come’: aya"là 3d pl. imf. mid. ($181, $208) DZe 11.
ali- + ay- ‘go beyond, go along’: aliyäiš imf. (872, 8122, 5298.11) DB 3.73.
upa- + ay- ‘go to, arrive at’: [ulpayam Ist sg. imf. (8122, §131, 8226.IT) DB 1.91f.
169
upari- + ay- ‘behave, conduct one's self’: upa- riyü[ya]m 1st sg. imf. ($122, §226.1T) DB 4.64f.
nij- + ay- ‘go forth’: nijäyam Ist sg. imf. ($120, $208, $226.IT) DB 2.64. |
pati- + ay- ‘come to, come into the possession of’: patiyãiša” За pl. imf. ($140.11, $208, §232.- П) DB 1.18, 18.
тата + ay- ‘go forth, proceed’: paraidiy 2d sg. тту. (§122, §181, $2371) DB 2.30, 50; 3.14. paratta 2d pl. іту. ($181, §208, $231, $237) DB 2.20, 83; 3.58, 85. parailé npm. past ptc. ($122, 8242, 59421) DB 2.32f, 38, 43, 52, 58; 3.65.

=== SYN excrement ===
880:Although ‘mud’ is wet earth, none of the common words for ‘mud’ are con- nected with those for ‘earth’. Several come from the more generic ‘dirt, filth’, these in part originally ‘excrement’. Some are used also for, or are cognate with, others for ‘marsh, swamp’. Others are connected with words for ‘liquid’, ‘pour, flow’ (through ‘flood, inundation’ to the resulting ‘mud’), ‘sink’ (what one sinks into), etc. Some are perhaps based on certain color notions. A few are used for both ‘mud’ and ‘clay’.
905:ME mudde, NE mud, MLG mudde, MIG, Du. modder (MLG > Dan., Sw. mudder), fr. a root *meu-, *mu- and ex- tensions, seen in many words with a common notion of ‘wet? or ‘dirty’, as Grk. pbdos ‘damp’, pvdéw ‘be dace boos (*nvdc0s) ‘defilement’, Pol. mut ‘Slime’, Skt. mitra- ‘urine’, Av. miéra- excrement, filth’, etc, Here also, fr. a Parallel *smu-, NHG Schmutz (> Dan.
909:MHG quat, kat, kot, NHG kot, orig. ‘excrement’ (4.66) and now most famil- iar in this sense in northern Germany, but ‘mud’ in southern Germany (so used by Luther Jn. 9.6).
910:NHG dreck, orig. and still in part ‘excrement’ (4.66), but also the usual word for ‘mud’ in many regions. On the local distribution of dreck vs. kot in this sense, cf. Kretschmer, Wortgeogr.
6856:Skt. chrd- : MIr. sceirdim ‘spew out’, perh. also Grk. cxip ‘excrement’, etc. Walde-P. 2.587.
7052:pARTS OF 4.66 VOID EXCREMENT; EXCREMENT, DUNG taae ee Goth. . ; maihstus, Lith.  Sikti; $udas, méSlas k KaKKaO, xe} Noe smarna Lett. dirst; stids, mésls
7064:Th oe oe ae for ‘excrement, dung’ are die ce that ‘ Selection is some- Seciaty € notion is oft alization of ‘filth’, but the dan aige # cen (as in NE dirt), A Ween human excrement
7078:ChSl. govno (*govino), etc., general Slavic word for ‘excrement’; Skt. gutha-, Av. guéa-, Arm. ku, koy ‘dung’; with d- extension OE cwéad, OHG quat, MHG quat, kot, kat, NHG kot.
```


## [2026-09-05T20:36:26.406Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KNT leaf 192 ===\"; awk 'BEGIN{RS=\"\\f\"} NR==193' KNT.txt | head -20; echo \"=== SYN 4.66 ===\"; sed -n '7050,7080p' SYN.txt",
 "description": "Kent p.170 and Buck 4.66"
}
```


### [2026-09-05T20:36:28.606Z] TOOL RESULT

```
=== KNT leaf 192 ===
-, GAv. angra-, LAv. apra- ‘hostile, enemy’, to рАт. root *ans-, seen in Av. qsta- ‘hate, enmity’; ef. also Av. (nom.) avrd mainyus ‘evil spirit, Ahriman’ (Bthl. AiW 189); not to Skt. art- ‘en- emy’ (MB Gr. §273), nor to Skt. alikd- (Wacker- nagel, KZ 59.28-9). алка nsm. DB 1.22, 33; 4.63. ага npm. DB 5.15°, 31°.
Ariya- adj. ‘Aryan’ (perhaps Ariya-, §126): Ау. atrya-, Skt. drya- ‘noble’, cf. NPers. ёгт ‘Iran, Persia’, Irish Eire ‘Ireland’, to pIE root *er-, OP ar- (585.1, §144.1). See also Ariyacica-, Artydramna-. Ariya паш. DNa 14; DSe 13; XPh 18. ariyd isn. as sb. ‘in Aryan (language) DB 4.89.
Ariyacica- adj. ‘of Aryan lincage’ (5161.18): Ariya- + ciga-. Artyacica пет. XPh 13; Ariya cica (written as two words, $44) DNa 14f, DSe 18f.
Ariydramna- sb. ‘Ariaramnes’, great-grand- father of Darius: Elam. har-ri-ia-ra-wm-na, АКК. ar-ja-ra-am-na-', Gk. 'Ариараштѕ. From ariya- + pass. pte. of d-ram- (8131; Av. Skt. ram- ‘to be at peace, to pacify’): ‘Having the Aryans at peace’ (8161.]1c). Hardly Ariyà pl. + ramna- (Foy, KZ 35.9), or Ariya- + aramna- pres. pte. mid. to ar- (Hz. Ар! 287). Anydramna nsm. AmH 1, 4, 9; DB 1.5; DBa 7; as gsm. AsH 3 ($313.1). Ariydramnahyé gsm. DB 1.5; DBa 7.
aruvü- sb. ‘action’ (JNES 444, 52; 53511, $150; so also Bv. TPS 1945.42-3): fem. to adj. arwa-, Av. aurva- ‘schnell, tapfer’ (Bthl. AiW 200), doublet to Av. aurvant- (q.v., under aru- vasta-).  aruváyà \sf. DNb 38 (inscribed afuvayá, $55.11; not anwasa with Wb. Grab 28, KIA 94;
OLD PERSIAN
not to be emended with Hz. Ар] 293-6 to aruvāðā ‘love’, cf. Av. urvafa- ‘amicus, befreundet’, ВЕЦ, AiW 1537; dfusdyd acc. nt. pl. ‘measures to be taken’, from *épy-dia-, acc. to Pisani, Riv. Stud. Or. 19.82-5, to root *&p- ‘get’, of. Av. afonte ‘they obtain’, Bthl. AiW 70 and 72, note 1 to ap-).
aruvasta- sb. ‘activity’ (INES 4.50-2, 232), ‘physical prowess’ (Bv. TPS 1945.40-1): -ta- ab- stract (5145) to arvani- ‘moving’, Av. aurvant- ‘schnell, tapfer, Held’ (ВЫ. AiW 200), Skt. ar- vant- ‘running, hasting, horse’, from Ar. ar- ‘move’ + suffix -vani- (535.11, §85, §126, §157), ef. Lt. orior ‘arise’; cf. АКК. translation '2t-ba-ru-tum ‘ac- tivity’, to abdru ‘be strong’ (Schaeder, OLZ 43.280-03). See also aruvi- Not with Hz. RHRel. 113.29-31, ApI 80-6, ‘Gut-sein’, to Ау, urvafa- ‘amicus’, with it-ba-ru-tum as ‘companion- ship’ to ibru ‘friend’ (cf. JNES 4.51); no valid evidence for meaning in Arm. loanword arwest ‘wonders’, cited by Nyberg, Rel. 351, from St. John 448. arwastam nsn. DNb 31, 33; asn. DNb 4.
Arza- sb. ‘Arkha’, an Armenian rebel (531, $164.V): Elam. ha-rak-ga, АКК. a-ra-hu. Атта nsm. DB 3.78, 91°; 4.28f; DBil. Arzam asm. DB 3.82, 89.
arjana- sb. ‘ornamentation’, as shown by АКК. : si-im-ma-nu-u ‘decoration’ (§84, §126, 8147.1): for meaning, see JAOS 51.208, 53.13, 53.19, Schaeder, Arch. Anz. 47.272-4, against Hz.’s ‘lime- stone’ (AMI 3.52-3) and ‘building material’ (ApI 88-93). Cf. Av. pres. arga- ‘be worth’, Skt. árhati, and Ars. РЫ, arzün, NPers. arzün, Av. arojah- ‘worth, value’, Skt. argha-. — arjanam nsn. DSI 41f; arjanam-Sary DSf 23°.
arta- sb. ‘Law, Justice’, an archangel attend- ing Ahuramazda: pte. to ar- as sb., Av. aša- and arata-, Skt. rid- ‘cosmic order’, Lt. ortus -‘risen, originated’, pIE *rto- ($30, $66, 5242.1). See also Artaxsaca-, arlavan-, Artavardiya-. ^ arid-cà isn. (8252.1, Lg. 21.223-9) XPh 41, 50f, 531 (not with Hartmann, OLZ 40.145-60; nor with Nyberg, Rel. 367, 478; Bailey ap. Nyberg, Rel. 478; Henning, TPS 1944.108; hardly, with Sen 155, artäcã braz- maniy apn. ‘and the divine fulfillments’; nor with Pisani, Riv. Stud. Or. 19.85-8, as elliptic dual ‘Arta and Brazman’, the -cé connecting with the preceding Auramazdém, and Brazman being the OP for the Av. vohü man ‘Good Though
=== SYN 4.66 ===
igitized by Arya Samaj Foundation Chennai and eGangotri
tai BODY; BODILY FUNCTIONS AND CONDITIONS 275
pARTS OF 4.66 VOID EXCREMENT; EXCREMENT, DUNG taae ee Goth. . ; maihstus, Lith.  Sikti; $udas, méSlas k KaKKaO, xe} Noe smarna Lett. dirst; stids, mésls
Grk. xbmP0S) ihe i z ON skita, drita; drit, skitr, ChSl. - 5 gnojt, govno,
NG xefo; apie Cie myki, skarn lajtno xompava Se merda, Dan. _ skide; skidt, mg SCr. _.srati; govno, gnoj, ba- ; Jat.  oa0dres Hg Zmentum Sw. skita; skit, dynga, lega : fimus, exer sae track Boh.  srdti; hovno, lejno, 1. oacare; eae es OE scitan; meox, cwead, hnij
Ir. chier; merae, scearn, dung, tord Pol. sraé; gowno, tajno, fiente - ME schite, drite; schit, gn6j
Sp. cagar; oe ; dung, mix, lord Russ.  srat’; govno, kal,
estiérco | NE shit; shit, dung, turd, pomet, etc.
Rum citea; edca he manure Skt. had-; cakrt-, purisa-,
Ir. case 2 Du. __ schijten, drijten; mest, visthd-, giitha- Nir.  cacaim; cac hoes drek, dreet Av. ri-; mi0ra-, giida-
W. _cachu, caca; cach, ican; mist, qual irya-, $a , ca, tom OHG Ariens mist, quat, sairya-, §2man- pony yep ES unga Br. kac’hout; kac’h, mon MHG > schizen; schize, mist, drec, quat, tunge NHG - scheissen; scheisse,
mist, dreck, kot, dtinger
Many of the verbs listed, and some of the nouns, belong to inherited groups re- flecting a variety of roots, in part, of the imitative or nursery type, which were apparently applied already in the IE pe- tiod to this bodily function. In the Gme. group and several of the other words the development is from ‘sepa- Tate’, whence ‘discharge from the body’. The countless euphemistic expressions are mostly ignored, as for example those meaning lit. ‘discharge, empty one’s self, Wythe ne sli doone’sneed’, andespecial- : a eta use of the simple verbs defecate shows eas me Hy au finned fe ecent Specialization of
wt. os Purify’ (Fr. deféquer Lat, défaecare fr. PAC quer, sy.), » Ir. faecés dregs’ ; NED
Th oe oe ae for ‘excrement, dung’ are die ce that ‘ Selection is some- Seciaty € notion is oft alization of ‘filth’, but the dan aige # cen (as in NE dirt), A Ween human excrement
and animal dung is partly observed, though this is not indicated in the list and many words for ‘manure’ are not entered. The etymology of certain words reflects the use of dung for fertilizing the land.
1. IE *kakka-, orig. nursery word. Walde-P. 1.336. Ernout-M. 125. Walde- H. 1.127. Falk-Torp. 484. Berneker 470.
Grk. xaxkaw (sb. xaxxn ‘human excre- ment’); Lat. cacdre (> It. cacare, Fr. chier, Sp., Port. cagar, Rum. céica, deriv. sb. Rum. cdcat) ; Ir. caccaim, NIr. cacaim, sbs. Ir. cacc, NIr. cac, W. cach, Br. kac’h (hence vbs. W. cachu, Br. kac’hout); Arm. k'akor ‘manure’; still as nursery words in Slavic, SCr. kakati, kakiti, Boh. kakati, Pol. kakaé, Russ. kakat’; disputed whether the Gme. words, NE cack (rare, but OE cac-his ‘latrina’), Du. kakken, Dan. kakke, NHG kacken (nurs- ery words) are native of the same popu- lar type (Walde-P., Walde-H., ete.) or through student slang fr. Lat. cacdre (NED, Kluge-G., Weigand-H., Falk-
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
276 SELECTED INDO-EUROPEAN SYNONYMS
Digitized by Arya Samaj Foundation Chennai and eGangotri
Torp). Re-formed to the original type | smrdét, ChSl. smriidétd ‘stink’. Walde.
apparently W. caca (vb. and sb.) like It. cacca, Fr. caca, etc.
2. IE *ghed-. Walde-P. 1.571.
Grk., NG xéfw (also xodirebev" azro- marety (‘retire to ease oneself’, Hesych.) ; Skt. had-, Alb. dhjes ‘cacare’; Av. zadah- ‘ump’, Grk. xédavov zy édpav Hesych. etc.
3. IE *kekv-. Walde-P. 1.381.
Grk. xémpos (NG xémpava, pl., medical term), Lith. sikiz,Skt. cakrt-(gen. caknas).
4. IE *g”ou-, *g”u- in words for ‘ex- crement, dung, filth’ (orig. ‘cow dung’ : TE *g”ou- ‘ox, cow’?). Walde-P. 1.694 ff. Falk-Torp 600. Berneker 339.
ChSl. govno (*govino), etc., general Slavic word for ‘excrement’; Skt. gutha-, Av. guéa-, Arm. ku, koy ‘dung’; with d- extension OE cwéad, OHG quat, MHG quat, kot, kat, NHG kot.
5. Derivs. of IE sker- partly neut. r/n stem (or, with separation of Slavic and Av. forms, *sker-, same as in vbs. for ‘cut, cut off, separate’, as OE sceran, Lat. cernere, Lith. skirti,etc.?). Walde-P. 2.587. Falk-Torp 986. Benveniste, Origines de la formation des noms 9.
Grk. cxép, gen. cxaréds, hence NG oxaré, usually pl. cxara; Lat. miscerda ‘mouse dung’, sucerda ‘swine dung’, etc.; OE scearn, ON skarn; Slavic vbs., SCr. sratt, ete.; Av. sairya- (Barth. 1567); Hitt. sakkar, gen. saknas (Sturtevant, Hitt. Gloss. 128).
```


## [2026-09-05T20:36:42.070Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=7080 && NR<=7130' SYN.txt | grep -n \"Av\\. ri\\|Av\\. rī\\|Pers\\. ridan\\|riden\\|rī-\" ; echo \"---\"; sed -n '7080,7120p' SYN.txt | grep -n \"27[5-9]\\|Skt. ri\\|rinati\"",
 "description": "Find Buck's discussion of Av. rī-"
}
```


### [2026-09-05T20:36:43.661Z] TOOL RESULT

```
50:Av. ri- (only with prefix), NPers. ridan ‘cacare’ : Skt. 77- ‘let go, release’, raya-‘flow’, etc. Barth. 1511. Horn 639.
---
26:HE BODY; BODILY FUNCTIONS AND CONDITIONS 277
```


## [2026-09-05T20:36:55.276Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"1511\\|1512\" BRT.txt | head -5; echo \"=== rī- verb headword ===\"; grep -n \"^• *[jgp][.,].*'ri-\\|• *j\\. *ri-\\|V\\.  'kacken\\|kacken\" BRT.txt | head",
 "description": "BRT col 1511 rī-"
}
```


### [2026-09-05T20:36:55.352Z] TOOL RESULT

```
=== rī- verb headword ===
5246:•   j.   avi  irita   InC'>    'zu   bekacken,
5370:•  j.  a-iritay-  f.  'Bekacken',  mit  Akk.  ver- bunden: 'tö  (LS.)  panliimm  ya^ä  jahika "(der  Hund)  kackt  auf  dem  Weg  wie  die Hure"  V.y.4S.
14563:•  j.  SräS'ri-  f.:  s,  unter  %rälar:
19255:•  j.  nisanharvd'ri-  f.:  s.  unter  tUlhantar-.
25172:���  j.  ray-  V.  'kacken';  nur  mit  Praev. Inf.  'trita;  Absol.  •iritlm.
25173:mit  aiwi  'bekacken';  s.  AbsoL mit  avi  'bekacken';  s.  Inf. np.  riyaä,  riäan  'kacken';  ai.  ritiati  (DbP.  auch nyätij  'er  lässt  laufen'.
```


## [2026-09-05T20:36:56.995Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && grep -n \"\\[pdf page\" WLD_Bd1_pages.txt | head -5; grep -n \"\\[pdf page\" WLD_Bd1_pages.txt | awk -F'page ' 'NR%1==0' | sed -n '150,160p'",
 "description": "WLD Bd1 page tags"
}
```


### [2026-09-05T20:36:58.834Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-05T20:38:23.446Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"raek-\\|raec-\\|'übrig  lassen\\|irinaxti\\|ir'naxti\" BRT.txt | head -5; echo \"=== WLD ===\"; cd incoming/WLD && head -3 WLD_Bd1_pages.txt; grep -c \"\" WLD_Bd1_pages.txt; grep -n \"page 1[34][0-9]\\]\" WLD_Bd1_pages.txt | head -5",
 "description": "BRT raek and WLD structure"
}
```


### [2026-09-05T20:38:23.533Z] TOOL RESULT

```
17075:•  j.  baäa  Fart  i)  der  Beteuerung,  am  Satz- anfang 'fürwahr':  b'  ila  aEni  6)n%i  (sd,) V.J.a?;  37,  39',  Yt-ÄS,  5.127,  F.ji?,Vyt 35^  3^-  3)  "^^^  Hervorhebung,  meist hinter  dem  ersten  Wort  des  Satz(teii)es"; a)  hinter  dem  Verbum:  lunti  b'  mavayacit cdkwars  arsäna  "sunt  profecto  mihi  etiam quattuor  mares"  V.  Jt^.  31.  b)  hinter dem  Relativ:_>'?  b'  ustanazastu gpnzaite  Yt 10.  53;  73;  —  ya%ra  b°  Y.  10.  7';  — yas» %wä  b'  fräyazäile  Y.  62.  i ;  — y!}  nS  b°  frä- yasäite  Yt y - S 2 ;  —  yas>  leb' .. baxsaite  Y. io,  13; — yim  vIsS  vTspaitis  b''^^  ustänazastö sbayeiti  Yt  10.  83;  84-86*''.  c)  sonst; avi  i'  fratmsaiti  Yt  iQ.  134;  134';  — alca  hl  b'  kammo^m  jaynvä  ..'^•Sy. 10; — yat  dim  dämSi^  upamanS  huirixttm  b° irinaxti  Yt/0.  68;  —  tal  i^aranS  b°  asti N.  30  ".  Ohne  Wert :  Vyt  5^,  Yt  2. 1 1 , Vd.  20.
17419:Zum  V.  raek-,  —  Pü. ;  täk  3  bar  pa  3  baxHhiih (Hds.  ark£t)  pa  3  känakik;  undeutlich.  — : 1)  D.  h.  das  Grundstück  soll  so  gross  sein, ' dass  es  dnich  ÖfTnung  des  oberhalb  gezogenen  j Bewäiserongsgrabens  zweimal  im  Jahr  unter ' Wasser  gesetzt  werden  kann.  1
24726:•  j.  raek-  V.  'linquerc'.  Praes.  8  irinak-, i6  (Des.)  irlrixsa-,  30  (Iter.)  raf'aya-; j-Aor.  I  raixs:  —  PFP.  'riiya-;  Inf. »rixti,  'ri^3;  AbsoL  'irixtfm.
24732:Stich  lassen,  preisgeben':  ks  mthnm  aiwi.- druiaili  kS  rashäm  paiti.irinaxti  Yt  14^  4  7 ; —  mäca  tl  ihra  ,  .  astvatahe  arshSus  di- drizvö  pxsa  (sd.)  manahim  paiti  ragxfiia (»SOM.)  P.40;  —  yS  ..  manafnm  aßtäm paiti  *irinaxfi^''  P.  40.  3)  'unterlassen': s.  Inf.  'riqia.         S.  noch  PFP.
25272:•  j.  raSnav-  i)  Adj.  'gerecht":  atarlö- hrJsca  yasats  .  .  atars'SAnsca  **ffa/(AP.) yatamaide  Vr. /ö'.  i.  a)  m.  Name  des Gotts  der  Gerechtigkeit:  iS  mi^rym  ahei.- druSaiti  Alf  'nOm  paiti.irinaxti  Yt.  7J.47; —  'nao!ca  paiti.sat3h3m  mihraAe^a  aiwi.- druxfim  (sd.)  V.  4.54; — ys  matdqm  tarS manyete .  ■  tarS  datgmta  •nUm^a  arUat^mca Yt./0.i39; —  daHmm  A^  (näml.  des  J/(- 'hra)' upa  arttam  vataite  yB  .,  traeiS  vair-
=== WLD ===
            GOVERNMENT OF INDIA
 ARCHEOLOGICAL SURVEY OF INDIA

81975
```


## [2026-09-05T20:38:45.684Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && grep -n \"arika\\|araeka\\|araēka\\|ari-h\\|ai\\. ari-\\|„Feind\\|'Feind\" WLD_Bd1_pages.txt | head -20",
 "description": "Grep WLD Bd1 for ari- Feind"
}
```


### [2026-09-05T20:38:45.738Z] TOOL RESULT

```
6290:womit Reuter KZ. 31, 594 a 1 auch ai. ari-yurtd-, stuta- als „eifrig ge-
10478:aaO. Yf. 34, 484f. und bes. Hermann GGK". 1918, 223 ff.) eydgog „Feind,
12170: „Feindschaft, Yerfolgung, HaB“, ( *ans-tha Bartholomae Wb. 361), qstai inf.
12173: (Kompositionsform der ro-Stamme auf i ) arika „feindlich gesinnt’ ( *ahrika).
12312:                                                                                          aber dri-, art- „Feind"
12315:Wb. B) kaum nur in der Bed. „Feind" hierherzustellen (Uhlenbeck ver-
13046:     lit. iriit,      }rti ..rudern", 'irklas „Ruder“                            Qr- Tiefstufe zu ai. ari-; de Saussure
25745:sich auch mit aksl. vragz „Feind", apr. wargs ..schlecht" usw., s. unter
30457:siech", apr. wargs „schlecht“, aksl. vragz „Feind", poln. wrog „EFbel, Boses;
34059:                                                                                                            heif'sl      „Feind-
64370:-ghn-ah (= av. wr&Shra-jan-, gen. - yn-o -) „Feinde erschlagend, siegreich",
80952:„Feindschaft“, dolgr „Feind“, dylgja „Feindschaft“, wozu wohl nd. dalgen
```


## [2026-09-05T20:38:48.661Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && sed -n '12150,12200p' WLD_Bd1_pages.txt; echo \"======== 12300\"; sed -n '12300,12330p' WLD_Bd1_pages.txt",
 "description": "Print WLD Bd1 ari- context"
}
```


### [2026-09-05T20:38:48.724Z] TOOL RESULT

```
 4- *teg- „decken“ (s. Pedersen KG. II 655; auch nicht nach Lagercrantz
 Z. gr. Ltg. 71, Marstrander IF. 20, 352f. als pnt- zu gr. jzdrog' evdvjua rrjg
"Hoag Hes.).
   Die gr. Sippe aber wohl vielmehr mit a = idg. 3 oder a zu iftoiov, dor.
axQtov „der (stehende) Kettenfaden beim Gewebe, Aufzug des Gewebes“,
bv)xQifiog „nebeneinandergereiht wie die Kettenfaden des Aufzuges, die
tjxQia sni xq> yxgtq)“ (Bezzenberger BB. 5, 313, Ehrlich KZ. 40, 375, Bechtel
Lexil. 1 30 f. ohne anl. _p-, daher nicht zu *uei- „flechten, weben“ oder zu
                      ;


ahd. wilt „Kleid“, Lit. bei Boisacq 330 mit Anm. 2, der freilich 1009 rjxQiov
trotzdem zu ai. vatavc „weben“ stellt, s. u. au- „flechten“).      Auch das —
 ar.     a-   ist   doppeldeutig.


 ens- „in feindseliger Absicht treffen"?
   Die Gruppe ist unsicher. Man konnte an einen Zusammenhang folgender
 Worter denken: ai. asand ,AYurfgeschoB“, astra-m „Gescho6, YVurfwaffe“,
 dsyati „wirft, schleudert“, av. rmJiyeiti ds. (Fick I 4 171). Dazu av. qsta- m.
 „Feindschaft, Yerfolgung, HaB“, ( *ans-tha Bartholomae Wb. 361), qstai inf.
 „zu befeinden“, gpav. angra-, av. atom- „feind, arg, bose“) aus *ans-ra- oder
 *as-ra- s. Johansson IF. 2, 26).   Ygl. ap. cthi-fraSlay „strenges Gericht“
 (Kompositionsform der ro-Stamme auf i ) arika „feindlich gesinnt’ ( *ahrika).
                                                              ;
                                                                                1
                                                er-, or-   — er-                            135

Der ved. Damonenname vyainsa-, den Bartholomae Grdr. d. Iran. Phil. I,
1,    167 hierher stellen         will,   bleibt besser       weg.
     Charpentier KZ. 40, 453 f.             stellt   das aus av. angra-, atom- gewonnene
ar.    *a.?-ra- als idg. *ns-lo-          dem    sons! unerklarten aisl. illr „schlecht, bose“
zur Seite, welches er aus idg. *enselo- iiber germ. *inzila- erklart. (Der
zu erwartende aisl. nom. sg. *inml sei durch dat. *'dle zu illr geworden.)
Das bleibt hochst unsicher. Koch weniger iiberzeugend ist die weitere
Yerbindung mit lat. Imus (*insmo-               <
                                     *ns-mo-) und air. Isel usw. „niedrig“
(angeblich kelt. *ins(e)lo          < *idg. ns(e)lo; richtiger Pedersen KG. I 36).
      Dafi idg. nsis „Schwert“ zu dieser Gruppe *ens- gehort, will nicht recht
einleuchten;      s.   d.



1.    er-, or- „Adler“ arm. gr. „(gro6erer) Yogel iiberhaupt“.
      Air. iVar, ilar, cymr. eryr, mbret. ever (nbret. corn, er daraus durch Yokal-
schwund, Pedersen KG. I 491) „Adler“ ( *erur -; Pick II* 39, Grammont
[Diss. 71], Pedersen aaO.); got. ara, aisl. orn, are, ags. earn, ahd. aro am,
„Aar, Adler“, mhd. aelel-ar, nhd. Adler-, lit. erelis, dial, arelis, (daraus riick-
gebildet eras, dras), apr. arelie (lies arelis), lett. erglis „Adar“, abg. or eh
ds.    (ob urn. erilaR,       aisl. jarl,       ags. eorl,    as. erl   „Mann“, bes. „vornehmer
Mann“ nach Uhlenbeck PBrB. 33, 183 damit zu verhinden sei nach MaB-
======== 12300
/-Basis gehoren), irin- „gewaltig, gewaltsam", ai. drtha- n. m. „(*wozu man
gelangt)“ „Angelegenheit, Sache, Geschaft; Gut, Yermogen, Yorteil", av.
ar&a- n. „Sache, Angelegenheit, Obliegenheit, Rechtsstreit" (Uhlenbeck
Ai. Wb. 13, Brugmann IF. 37, 240 f.; nicht zu *ar- .,zuteilen‘‘);
   ai. rti-, rti- f. „Angriff, Streit", av. -arati- „Energie“ (= arm. ah „Furcht“?

abl. abg. rah)-,
  Aber rti- „Art, Ware", rja- ,.gehdrig, richtig", rtu- u. dgl. zu ar- „fiigen“.
Uber ai. arati- „Diener“ s. u. ere- „rudern“ und ar- „fiigen“, desgleichen
uber gr. i'glhog (gegen Brugmann IF. 19, 384).
     Ai. drta- „betroffen, versehrt, bedrangt, leidend", arti- f. „Unheil, Leiden"
(*a-rta-, -rti-)-,                   aruka- „verletzend“ (dehnstufig)                   ;
                                                                                          aber dri-, art- „Feind"
(Lit. bei Bois.                 u.    igig)   ist    wegen seines             viel    weitern Bedeutungsumfangs
„verlangend, begierig, anhanglich; feindselig, unfromm" (s. LThlenbeck Ai.
Wb. B) kaum nur in der Bed. „Feind" hierherzustellen (Uhlenbeck ver-
bindet es mit got. aljan „Eifer"? i;                          /

     Ai. drna- „wallend, wogend, flutend", m. „Woge, Flut", drnas n. „wallende
Flut"        (formed = gr.                  I'grog    n.;     vgl.       unten   ahd. rims),         arnavd- „wallend,
                                                                 ct-                                        (37

wogend“; m. „Flut, wogende See                          :t
                                                                 (wo-Weiterbildung zu urna-t oder in
alter formantischer Beziehung zu                                 rnotit Letzteres ist sieher fiir:) av.
aranu- m. „Ivampf, Wettkampf (: ahd. eniust );
                                               -1
```


## [2026-09-05T20:39:15.646Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && awk 'NR>=12180 && NR<=12420' WLD_Bd1_pages.txt | grep -nE \"^ *1[0-9]{2} *$|er-, or-|  13[5-9] *$|^ *13[5-9]\" | head",
 "description": "WLD page headers around 136"
}
```


## [2026-09-05T20:39:16.154Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"arika-\\|arīka\" KNT.txt | head -5",
 "description": "Kent arika"
}
```


### [2026-09-05T20:39:17.404Z] TOOL RESULT

```
14:1.    er-, or- „Adler“ arm. gr. „(gro6erer) Yogel iiberhaupt“.
62:136                                                                     er-
```


### [2026-09-05T20:39:17.467Z] TOOL RESULT

```
521:abiyajavayam XPg 9, and abijdvayam ХРЕ 40. niyasaya DNb 5, 46, 49, probably for *niyayasaya. [a]fiya[s?]ya DB 4.91, perhaps for *atiyayasiya. marika- DNb 50, 55, 59°, cf. Phi. mérak, Skt.
1526:*mer- ‘die’ in marika- ‘menial person’ (see Lex. s.v.), *mor- in martiya ‘man’ (see Lex. s.v.), *mr- in marta ‘dead’, uvä-maršiyuš ‘by self- death’ (see Lex. s.v.); perhaps *m»r- in amari- yata ‘he died’ (cf. Av. miryeite ‘he dies’).
5050:arika- adj. ‘evil, faithless’: deriv. (6146.11) of *asra-, GAv. angra-, LAv. apra- ‘hostile, enemy’, to рАт. root *ans-, seen in Av. qsta- ‘hate, enmity’; ef. also Av. (nom.) avrd mainyus ‘evil spirit, Ahriman’ (Bthl. AiW 189); not to Skt. art- ‘en- emy’ (MB Gr. §273), nor to Skt. alikd- (Wacker- nagel, KZ 59.28-9). алка nsm. DB 1.22, 33; 4.63. ага npm. DB 5.15°, 31°.
5775:mar- vb. ‘die’: Av. mar-, pres. miryeite ($122, $214), Skt. mriydte, Lt. moritur, pIE *mer-. See also uvdmarsiyu-, marika-, maria-, martiya-. amarijalü imf. mid. (835.1, $285.II) DB 1.43.
5776:marika- sb. ‘person of lower rank, subject’, as shown by АКК. *"gal-la ‘menial’: contracted ($23.1) for *mariyaka-, deriv. of stem in Skt. (Vedic) márya- ‘young man, stallion’, ef. Skt. maryakd- ‘little man (said of a bull among cows)’, Phi. mérak (from *maryaka), Gk. шера ‘boy, girl’ (from *merjak-); ultimate root pIE *mer-, OP mar- (5122, 5146.11). Cf. Hz. ApI 251-3, Bv. TPS 1945.43-4. татка узш. DNb 50, 55, 59°.
```


## [2026-09-05T20:39:27.275Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && head -3 BQT_v1_pages.txt; grep -n \"\\[pdf page\" BQT_v1_pages.txt | head -3; echo \"=== search آریغ ===\"; grep -n \"آریغ\\|أریغ\" BQT_v1_pages.txt BQT_v1.txt BQT_v2_pages.txt FSF_pages.txt MON_part1.txt MON_part2.txt 2>/dev/null | head -10; echo \"=== ریغ ===\"; grep -n \"ریغ\" FSF_pages.txt | head -5",
 "description": "Search Persian sources for آریغ/ریغ"
}
```


### [2026-09-05T20:39:27.374Z] TOOL RESULT

```
۱ ۵ ۱! ۱
7 موم ۳ لام
م ۱ 0 و طق صفرررنیاعدریرماروی
=== search آریغ ===
BQT_v1_pages.txt:7459:آریغ ۴ - بکر مالك و سکون
BQT_v1.txt:13085:آریغ ۴ - بکر مالك و سکون 
BQT_v2_pages.txt:26634:             ‫‪٩‬‏ رك ‪:‬آریغ ‪.‬‬       ‫‪ ۴‬اسم مفعول از «رشیدن» ‪.‬‬                    ‫ار‬
MON_part1.txt:2779:آریغ: 19 [دشمن] (.) کراهت» نفرت» 
MON_part1.txt:69820:ریغ: بآ [- آریغ] () کینه؛ عداوت» نفرت. 
=== ریغ ===
3199:‫دریغ آن شده رنج‌های کهن‬                                                               ‫تک‬
3475:                                       ‫باران‬                    ‫همی گفت کای پادشاهی دریغ‬
3478:                ‫دریغ آن شده روزگاران من‬
4683:           ‫دریغ آن دلیران و چندین سپاه‬                         ‫روک دن ‪۳۳۱0۱‬‬
4891:           ‫دریغ آن سوار گراننمایه نیز‬                                    ‫(ویس ‪:)۸۹-۸۲‬‬
```


## [2026-09-05T20:39:36.080Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== MON آریغ ===\"; sed -n '2775,2783p' MON_part1.txt; echo \"=== MON ریغ ===\"; sed -n '69816,69824p' MON_part1.txt; echo \"=== BQT v1 آریغ ===\"; sed -n '7450,7470p' BQT_v1_pages.txt; echo \"=== BQT v2 ریغ ===\"; sed -n '26625,26640p' BQT_v2_pages.txt",
 "description": "Print Persian dictionary entries"
}
```


### [2026-09-05T20:39:36.196Z] TOOL RESULT

```
=== MON آریغ ===
خواننده در این قسمت قدرت و مهارت خود 
را نشان می‌دهد. آهنگی دلکش برای ساز با 
آواز. آوازهای انفرادی ابر ا؛ مق. کر. 

آریغ: 19 [دشمن] (.) کراهت» نفرت» 
کینه. ضح.- این کلمه بصورت «آزیغ» 
تحریف شد ۵. 

از: () حسرص» طمع» زباده‌جویی» 
=== MON ریغ ===
امدن. (امص.) افزونی» نام گر 
(خمیر؛ برنج پخته و مانند آن) 
ریعان: 130۳5۹3350 [ع.] (.) اول هر چیز و 
بهترین آن؛ بهترین موسم: ریعان شباب. 
ریغ: بآ [- آریغ] () کینه؛ عداوت» نفرت. 
ریخ: (قد. ۰70 [- راغ] (.) دامن کوه» 
صحر ا؛ راغ. 
ریغ: «: (0) (عم.) پلیدی؛ گه. 
ریعو: تآ: (ص ۰ (عم.) آنکه خود را 
=== BQT v1 آریغ ===
و اسحان و آزماش راک ند .
ده ه بروزن چاره. بیخ و بن دندان ها
را گویند ؟ «
]رید بر فك - یکی الت و سکون
نحتانی و دال ابسد . این لفت از اباع است
وبمعنی دوائی‌باشد مانندییاز شکافتهوآ ترالزسیتان
آورند وبربواسیر طلا کتند تاقع باشد . وخوردن
آن زنان راخون حیض آورد ؛ وبکر همزه تیز
کگفته‌اند که آزدبرید باشد و
آریغ ۴ - بکر مالك و سکون
نحتانی و غين نقطهدار . کینه و عداوت باشد -و
سردی (۱) و نفرنی را نز گوبندکه از شخصی
(۱) چك : سردئی .
۱ و ایس کت ادا وود ۴ رك : اربدبربد. ۴ دریارسی‌باستان (دکتبة بستون. متون؟
بند ۱۲ ) 2621624 از رشه ۲18 بمعنی دشمن ۳0288,۳6۲61566ععدای۲۲.۲۲ )
(۱25-6 . 5 ,1895 96110160,5)۲255018این لت درفر‌هنگه‌اسدی چاب‌نهران س‌۲۳۸ونیز
موضع‌دیگر برهان بخلط «آزیغ»آعده. خسروانی شاعرکوید : کآربغ زمن بدل کرفته + کتجکاوی
های علمی و ادبی . نشریهٌ دانشگاه تهران شمارء ۸۳ . قطمه .ای از بفستان بقلم نگارنده 4۱
آریا _ اوستا ۰21۲72 پارسی‌ب‌استان 211۷2. سانسکرمت 217338 «بارتولمه ۱۹۸ نام
طایفه‌ای از ند و اروپائیان که در عبدی بسیارکهن با هم میزیستند و مد ها بدو بخش بزر که
تیم شده کروهی بیند و گروه دیگر بابران آعدند . هت کش مولر ۱۷۵116۲ ۳2( آرائی را
=== BQT v2 ریغ ===
 ‫ونایت از ذره‬
            ‫‏(‪ ۱٩)۱‬و عربان رمل خوانند ‪ -‬ک‬                                         ‫وبی‌حمیتی باشد ‪.‬‬
 ‫هم‌هست ‪ -‬و بمعنی بخت وطالم نیزگفته‌اند ‪-‬‬              ‫= بروزن‌نیشه‪ .‬تارهای ربمائی‬             ‫ربثه‬

                                                                       ‫‪.‬‬   ‫اس‬    ‫(‪ )۷‬چك ‪+ :‬‬

       ‫ی (مصدری) ‪.‬‬            ‫‪ - ۴‬از‪ :‬رشمال‬               ‫‪ - ۱‬لفة لحية فاضی (رش داور) ‪2‬‬

  ‫‪ - ۴‬پهلوی ‪( 2۵15۵۲‬مو) «اسشق ‪1۰٤٥‬ء‏ بازند ‪ 6051۲‬پ»ارسی رسکه ( بکر اول )‬
             ‫‪٩‬‏ رك ‪:‬آریغ ‪.‬‬       ‫‪ ۴‬اسم مفعول از «رشیدن» ‪.‬‬                    ‫ار‬
                                                                  ‫دنوالا ‪. ۵۲4‬‬
  ‫» رء‌فغوادمی وجالوری که‬      ‫ریخ («‪.‬م‪ ).‬است‬     ‫دیمع‬        ‫‪۲‬‬               ‫رك ‪ :‬راغ ‪.‬‬   ‫‪-‬‬    ‫‪۹‬‬

   ‫شمش روان بود و اهال داشته باشد و تواند خویشتن‌را نگهدارد ‪ -‬یلید ‪ .‬در کتابادی ربشوله‬
  ‫‪٩‬‏ ‪« -‬ازین تفسیر واضح میشودکه مؤلف ظاهراً‬                       ‫_زربكغ‪:‬ال ‪.‬‬                  ‫«کنابادی» ‪.‬‬
   ‫« ويك » (بفتح اول ) عربی را «ريك» خوانده و آبرا فارسی تصور کرده» «محمد قزوننی»‪ .‬موّلف‬
```


## [2026-09-05T20:40:01.050Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT arika ===\"; grep -n \"•  p\\.  arika\\|arika-  Adj\" BRT.txt | head -3; echo \"=== اروند BQT/MON ===\"; grep -n \"اروند\" BQT_v1_pages.txt MON_part1.txt | head -6; echo \"=== الوند ===\"; grep -n \"الوند\" BQT_v1_pages.txt MON_part1.txt | head -6; echo \"=== لهراسب/لهراسپ ===\"; grep -n \"لهراسب\\|لهراسپ\" MON_part1.txt MON_part2.txt FSF_pages.txt | head -6",
 "description": "Search Arvand, Alvand, Lohrasp"
}
```


### [2026-09-05T20:40:01.176Z] TOOL RESULT

```
=== BRT arika ===
=== اروند BQT/MON ===
BQT_v1_pages.txt:11140:شخصی در آن کوء آسوده است که نام او اروند
BQT_v1_pages.txt:13706:۴ رك : آله و آموت .او فد بروزن و معنی اروند باشدکه
BQT_v1_pages.txt:14907:۴ رگ + آورند و اروند .
MON_part1.txt:5253:اورند: اجه [- ۱ - اروند] (ا.) 
MON_part1.txt:5256:آورند: 0 ([< آورند - اروند] (ا.) فرء 
MON_part1.txt:10308:اروند: 27274 [تند» تب چالاکك» دلیر - 
=== الوند ===
BQT_v1_pages.txt:166:وشوش ( درعیلام ) وبنستان ( - بیستون ) وهمدان والوند ( در ماد) و وانمقد مه دو
BQT_v1_pages.txt:8642:درهمدان که بالوند شپرت دارد ؟ . «
BQT_v1_pages.txt:8664:۴ - ر4 : الوند . ۵ رد : آفك .
BQT_v1_pages.txt:10344:همدان مشهور بالوند .
BQT_v1_pages.txt:11138:ارو ثف ۴ « بر وزن ومعتی الوند است
BQT_v1_pages.txt:12620:الوند » نام ملوکی است ازیلوکات نشابورمشتمل
=== لهراسب/لهراسپ ===
FSF_pages.txt:1226:                           ‫د‬ ‫از ه‬                    ‫ایرانیان و کشته شدن لهراسب به‬
FSF_pages.txt:1401:‫[لهراسب] به بگلزخین شد بر آن نوبهار‬                     ‫ار‬        ‫ییک ان زمه‬
FSF_pages.txt:4525:               ‫برآنم که تو خویش لهراسپی‬       ‫(تاریخ سیستان)‪ :‬و مردی مردست‪ .‬و کسی‬
FSF_pages.txt:5856:‫گشتاسپ از پدرش لهراسب رنجیده به‬                      ‫‏)‪(TA1-F۶4-£‬‬
FSF_pages.txt:9970:        ‫چنین داد پاسخ که ای پهلوان‬                                  ‫بفرمود لهراسب تامهتران‬
FSF_pages.txt:12034: ‫پس رافع دستوری خواست به آمدن‪.‬‬                    ‫ببخشای بر جان لهراسپ پیر‬
```


## [2026-09-05T20:40:31.880Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== MON اروند ===\"; sed -n '10305,10315p' MON_part1.txt; echo \"=== BQT اروند/الوند ===\"; sed -n '11130,11150p' BQT_v1_pages.txt; echo \"=== BQT 12615 الوند ===\"; sed -n '12615,12630p' BQT_v1_pages.txt",
 "description": "Print Arvand/Alvand entries"
}
```


### [2026-09-05T20:40:31.953Z] TOOL RESULT

```
=== MON اروند ===
اشخار از آن حاصل شود» شخارء اشنان؛ 
اشنه. 

اروند: 27274 [تند» تب چالاکك» دلیر - 
اورنسد - آورند] (ا.) فر» شکوه» شان و 
شوکت. حسرت» آرزو. 

ارون.د: 27274 [- اورند - آورند] (.) 
مکر فربب» حبله. سحر؛ جادو. 
ارویس‌گاه: 2۳2-2 (امر.) (در آداب 
دینی زرتشتی) سنگ بزرگی است چهار 
=== BQT اروند/الوند ===
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
=== BQT 12615 الوند ===
گران و صحافان چیزها بدان چسیانند .
اشفر - بن اول وغین نقطه‌دار وسکون
ثانی و رای بی نطه » خاریشت بزرک نیرانداز
را گویند .
اشفنك - بغتح اول و فای سعفص بیوزن
الوند » نام ملوکی است ازیلوکات نشابورمشتمل
بر هشتاد و سه فربه .
اشق . ینم اول و فتح ثانی و سکون
فاف » صمغ کیاهی است که آنرا بدران کویند
و بعربی صمم العطرئوث خوانند. استسقا را ناف
است » و بعضی کویند جوهری است عمدنی که
0-ر که : استیم .
اشکبوی
آنرا بمربی فراق الذهب خوانند. وآن نیوممدیی
«,هست که عملی باشد و آن چنانت که بول
کود کان را باسر که در هاون سین کنند و در
```


## [2026-09-05T20:40:54.980Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in a3de197a826362e1 704467a24d42db61; do echo \"##### $f\"; wc -c $f.txt; grep -n -i \"proto-indo-european\\|PIE root\" $f.txt | head -4; done",
 "description": "Check etymonline fetches"
}
```


### [2026-09-05T20:40:57.580Z] TOOL RESULT

```
##### a3de197a826362e1
6526 a3de197a826362e1.txt
25: 1570s, "one who is in pursuit of the same object as another;" 1640s, "one who emulates or strives to equal or exceed another" in some way; from Latin rivalis "a rival, adversary in love; neighbor," originally, "of the same brook," from rivus "brook" (from PIE root *rei- "to run, flow").
##### 704467a24d42db61
11875 704467a24d42db61.txt
126: sally, excursion, expedition," figuratively "an outset, opening," noun of action from past-participle stem of excurrere "run...out, run forth, hasten forward; project, extend," from ex "out" (see ex-) + currere "to run" (from PIE root *kers- "to run...
130: 1520s, "meet, meet in argument," from French occurrer "happen unexpectedly" or directly from Latin occurrere "run to meet..., run against, befall, present itself," from ob "against, toward" (see ob-) + currere "to run" (from PIE root *kers- "to...run")....
134: upon oneself;" mid-15c. as "become liable for (payment or expenses)," from Anglo-French encurir, Old French encorir "to run..., flee; commit, contract, incur" (Modern French encourir), from Latin incurrere "run into or against, rush at, make an attack...;" figuratively, "to befall, happen, occur to," from in- "upon" (from PIE root *en "in") + currere "to run" (from PIE root...*kers- "to run")....
```


## [2026-09-05T20:41:05.464Z] TOOL CALL #60: Bash

```json
{
 "command": "for u in \"https://www.etymonline.com/word/are\" \"https://www.etymonline.com/word/origin\" \"https://en.wiktionary.org/wiki/Lohrasp\"; do python3 tools/fetch_source.py \"$u\" --note \"page 156 Er 1: English are/origin; Lohrasp\"; done",
 "description": "Fetch are, origin, Lohrasp"
}
```


### [2026-09-05T20:41:09.037Z] TOOL RESULT

```
Exit code 1
/home/sfmqrb/git/rishe/data/verification/sources/web/3c6379a69d2a2a6d.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/5a855f25814f91f7.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/852bd5a2aec4b210.txt
```


## [2026-09-05T20:41:12.490Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in 3c6379a69d2a2a6d 5a855f25814f91f7 852bd5a2aec4b210; do echo \"##### $f\"; wc -c $f.txt; sed -n '1,6p' $f.txt; grep -n -i \"PIE root\\|Proto-Indo\" $f.txt | head -3; done",
 "description": "Check fetched are/origin/Lohrasp"
}
```


### [2026-09-05T20:41:14.610Z] TOOL RESULT

```
##### 3c6379a69d2a2a6d
249 3c6379a69d2a2a6d.txt
URL: https://www.etymonline.com/word/are
FETCHED: 2026-09-05T20:41:07Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 301: The HTTP server returned a redirect error that would lead to an infinite loop.
##### 5a855f25814f91f7
7668 5a855f25814f91f7.txt
URL: https://www.etymonline.com/word/origin
FETCHED: 2026-09-05T20:41:08Z
STATUS: 200
TITLE: Origin - Etymology, Origin & Meaning

Origin - Etymology, Origin & Meaning 
40: 1570s, "to miscarry in giving birth," from Latin abortus , past participle of aboriri "to miscarry, be aborted, fail, disappear, pass away," a compound word used in Latin for deaths, miscarriages, sunsets, etc., which according to OED is from ab , here as "amiss" (see ab- ), + stem of oriri "appear, be born, arise," from PIE *heri- "to rise" (see origin ). [Watkins, contra de Vaan, etc., derives the second element from a suffixed form of PIE root *er- (1) "move, set in motion."]
80: instigate" (to sin or violence) from Old French enticier "to stir up (fire), to excite, incite," which is of uncertain origin...set on fire," from Latin in- "in" (from PIE root *en "in") + titio (genitive titionis) "firebrand," which is of uncertain origin...
##### 852bd5a2aec4b210
133 852bd5a2aec4b210.txt
URL: https://en.wiktionary.org/wiki/Lohrasp
FETCHED: 2026-09-05T20:41:09Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 404: Not Found
```


## [2026-09-05T20:41:26.509Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"aurvat\\.asp\\|aurva^\\.asp\\|auruuat\" BRT.txt | head -6; echo \"=== FSF aurvat/Lohrasp gloss ===\"; grep -n \"لهراسب\" FSF_pages.txt | head -3",
 "description": "BRT aurvat.aspa headword"
}
```


### [2026-09-05T20:41:26.576Z] TOOL RESULT

```
4752:F.  ff;  —  :^ahe  gayehe  :^airvats{5A^  "sähe Y.5.1,  Yt-Äii.  a)  von  der  Sonne: hvan^ail>m  'hm  raim  aurvat.asp»m  Yt. 6.\,  4,  6; —  hvar>.xsaitahe  'sähe  ra^ahe Yt-ö-o,  Y.22.24J  —  paurva.naemäi  °hhe hä  yaf  aurvat.aspahe  Yt.  10. 1 3.  A)  ins- bes.  von  den  dem  AhuraMazdäh  nächst- stehenden Gottheiten*':  yaia  vahm>m 'iaiibyS  Y.  21.2;  —  -saHi  . .  avarshe  ismti masyäkänAs  Aog.  41.  a)  sonst  in  Ver- bindung mit  spitUa-  Adj.  'heilig',  das  in GHapL'vor-,  sonst  nachsteht:  *vyäX3mca kanjamanimca  (sd.)  yat  as  'sanqm  sp?nta- nqm  banlnvS  *avarihe  as/0  y?mat^m  (sd.)
17769:•  j.  baxsänti  raisla  . .  "frayaha^w8-«i aurvat.aspa^a  .  .  Vytj4-
18541:•  ).,  g.,  p.  naplt-:ffa//-  m.,  j.  naptar-: nafsir-  m.",  j.  naptl-  f.  'Enkel;  Enkelin': '  adam  d3ray^v(^ui . .  vistäspahya  puh^e^ arSätnakyä  '/J(NS.)'*  Eh.  j.  i;  —  'pS (NS.)"  ..  ■■//("  (NSf.)  i/a  V./2.11;  10;  — nyaka  haca  'ptöisSs,  (^\%y^  nyske  haca  'pti (statt  AblSf.)  V.  J2. 1 1 ;  —  hyai  us  alä napiyaisii  na/i'uCLP.yVä ..uzp//  (Sp.4gSm.)  ' fryänakya  aojyaiiü  '^.46.12.  a)  mit GP.  apam''  'Enkel  derWasser',  Name  einer Gottheit**;  a  dim  (näml.  3^ar)nö)  Hahra kangturvayat  apum  'ph  (NS.)  aun'at.aspö Yt.  rp.  s  1 ;  5 '".  '.7-  95^';  —  «/>?'»  >'»  (NS.) t&  ups  ,  .  aiiuhe  .  .  vi.baxsaiti  Yt  8.  34; —  b^ntantfm  ahuntn  xsa^rlm  xSaltitn apqm  'pättm  aurvat.asp?m  .  .  yB  upäpB yazatS  Yt  ig.  51 ;  Y.  2,  5;  —  apqm  'ptär?m yasamaide  nairJm  sanh^m  Y.  7/.  23;  — b»->sat3  ahurake  'fiorS  aPqm  apasca  maida- la/aya  Y.  r.  5;  —  b^ryza  a/iura  xsa^rya apqm  V»?(VS.)Y.6'5.ia.  _  a)Nameeiner jener  Gottheit  geweihten  Örtlichkeit*'  (oder eines  Husses,  einer  Quelle,  eines  Berges): tarn  (näml.  andriin)  yaznäa  . .  sSyuidrSis pu%ra  upa  b3r?zant?m  ahur>m  xsairim xsaWm  apqm  'paism  Ylj.  73.  [na/jonm Y. ij.ii:  s.  x/alirB.napiar-.\
21197:—  ttaota(sd.)ca  .  .y  aisa  ahurahe  Vr,  g.  6j  1 6f.';  —  s.  noch  Anhang.  d)  DSm.,  n.: ra%we  .  .  y  ahurai  mazdät  .  .  y  zara- %ulfräi  Vr.  12.1;  —  Primat  y  pouru.- baoxinahe  (statt  DaL)  Y,^.  37; —  huxla- hrSJfmai  ..hya^  mazdäi  ahuräi  Y.jj.  5, A.J.  6  {vioy);  —  kvävSya  y  sadhreY.^g. 30;  V.  jp.  47,VyL_jj';  —  maZsahe ..y  vars- fiSi/yU7.s6.  e)AblSm.,n.:  asätiStverz.) haca  y  vahiUät  Y.ip.  iiusw.; —  drvatat y  anrät  mainyaot  YL  /_J.  7 1 ;  —  %'wai  y eara'husträt  ^.2.3.  f)  GSra.,  ^.:  asoAe y  vahiitaÄeY.i.to;G.2.y,'Vtlj.9i,92;  — amp^ahe  hü y  aurvat.aspahe  Yt  10.  13;  67, J2.38,  S.J.  18;  —  k>r)säspahe y  *£ae%äus', gahavarahe  Yt.  /j.  6 1 ;  — ■  anhus  yS  mana (Stverz.)^"  ahurahe'?.43;\x%'v.\  —  manay zara%uUr3i  (statt  Gen.)  V.  2.  i ;  —  tava y  ahurahe  mazdä  V,  4.  3;  —  myaxdahe aoäiti  (sd.)  .  .  y  maiaySizanmayehe  A. J.7;  8— 12*,  7.  o):  aheca  kar^anS y i^anira%aht  Vr.  /o.  i;  —  aiMe  .  .  y° yasnaheca  vahmahtca  Y.  /.  2 1 ;  —  aRahe nars  .  .  y  irisfs.kasahe  V.  ^,  15;    18.  39;
24610:•  j.  viäa'vant-  Adj.  'giftig':  aiJm  .  .  ytm.jj.Gi;  —  puhrtm  yat  aurvat.aspahe  .  . 'vant9m..yim  upairi  *vi<{%A)*raolat..\kavam  -p^m  Yt,5.ios;  117,  15.84;  — Y.5.11.  \kavdis   'pake  Yl.7_j.99,  5-i3*i  '5-36,  Y.
30662:—  yS  yataite  hvar»  yat  am»hm  raim aurvat.asptm  Yt,  6,  4;  —  mi^r»m  ..yakmäi hvar»  aurvat,asp»m  dürät  tutnS  baohayäti Yt.io.go;  Az.^;  — paurva.natmat am»sahe hu  yat  aurvat.aspahe  Ytio.  13; — hva  r»Ja am»s}  sp»ntt  yatamaide  Vr.  ig.  2  (?),
=== FSF aurvat/Lohrasp gloss ===
1226:                           ‫د‬ ‫از ه‬                    ‫ایرانیان و کشته شدن لهراسب به‬
1401:‫[لهراسب] به بگلزخین شد بر آن نوبهار‬                     ‫ار‬        ‫ییک ان زمه‬
5856:‫گشتاسپ از پدرش لهراسب رنجیده به‬                      ‫‏)‪(TA1-F۶4-£‬‬
```


## [2026-09-05T20:41:28.632Z] TOOL CALL #63: Bash

```json
{
 "command": "python3 tools/fetch_source.py \"https://en.wikipedia.org/wiki/Lohrasp\" --note \"page 156 Er 1: Lohrasp < Av. Aurvat-aspa\"; python3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/%D8%A7%D9%84%D9%88%D9%86%D8%AF\" --note \"page 156: Alvand\"",
 "description": "Fetch Lohrasp wikipedia"
}
```


### [2026-09-05T20:41:30.983Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/4acdd6dcaf1aafeb.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ec8db32a1def647f.txt
```


## [2026-09-05T20:41:35.799Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && grep -n -i \"Aurvat\\|auruua\\|Avestan\" 4acdd6dcaf1aafeb.txt | head -6",
 "description": "Lohrasp wikipedia content"
}
```


### [2026-09-05T20:41:35.845Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-05T20:41:38.570Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && wc -c 4acdd6dcaf1aafeb.txt && grep -n -i \"lohrasp\\|Luhrasp\" 4acdd6dcaf1aafeb.txt | head -5",
 "description": "Check Lohrasp page"
}
```


### [2026-09-05T20:41:38.615Z] TOOL RESULT

```
2935 4acdd6dcaf1aafeb.txt
1:URL: https://en.wikipedia.org/wiki/Lohrasp
128: (Redirected from Lohrasp )
```


## [2026-09-05T20:41:42.626Z] TOOL CALL #66: Bash

```json
{
 "command": "python3 /home/sfmqrb/git/rishe/tools/fetch_source.py \"https://en.wikipedia.org/wiki/Aurvataspa\" --note \"page 156: Lohrasp < Av. Aurvat.aspa\" ; sed -n '120,200p' /home/sfmqrb/git/rishe/data/verification/sources/web/$(python3 -c \"\nimport hashlib;print(hashlib.sha1('https://en.wikipedia.org/wiki/Aurvataspa'.encode()).hexdigest()[:16])\").txt | grep -v \"^ *$\" | head -25",
 "description": "Fetch Aurvataspa wikipedia"
}
```


### [2026-09-05T20:41:45.546Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/e1d189d302e08243.txt
```


## [2026-09-05T20:41:48.035Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && grep -n -i \"avestan\\|aurvat\\|swift\" e1d189d302e08243.txt | head -8",
 "description": "Check Aurvataspa page"
}
```


### [2026-09-05T20:41:48.087Z] TOOL RESULT

```
1:URL: https://en.wikipedia.org/wiki/Aurvataspa
```


## [2026-09-05T20:41:59.895Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BQT ریدن/ریم v2 ===\"; grep -n \"ربدن\\|ریدن\" BQT_v2_pages.txt | head -4; echo \"--- ریم\"; grep -n \"^ریم\\|ریم -\\| ریم \" BQT_v2_pages.txt | head -4; echo \"=== پتیاره ===\"; grep -n \"پتیاره\\|پتباره\" BQT_v1_pages.txt BQT_v2_pages.txt FSF_pages.txt MON_part1.txt | head -6; echo \"=== پذیره ===\"; grep -n \"پذیره\" FSF_pages.txt MON_part1.txt | head -4; echo \"=== رنده MON ===\"; grep -n \"رنده:\" MON_part1.txt | head -4",
 "description": "Grep Persian sources for remaining words"
}
```


### [2026-09-05T20:42:00.067Z] TOOL RESULT

```
=== BQT ریدن/ریم v2 ===
1148: ‫وبربدن آن بیم حلاکت باشد ویشتی مردم‌فرغانه‬           ‫سردوش ناخنها دارد وخودرا سرنگون از درخت‬
1359:‫جرغول ‪ -‬بفتحاول بروزن مرغول »‬                          ‫مالیدن دندان و دربدن کرباس و امثال ‪.‬آن‬
1722:‫است‬    ‫وعده ‪ °‬دوی‬     ‫= بروزن‬        ‫جعدم‬                        ‫است دمرربدنم ‏‬
4101:                     ‫میکب از تفه فولادین ودستش‌ای چویین ‪ ۰‬وآن برای بربدن و تراشیدن پار رود ‪.‬‬
--- ریم
4749:‫چرك و ریم داشته باشد ؛ و بفتح اول همآمده‬                   ‫‪ -‬روزن رسددن ؛ بمعنی دم‬        ‫جخیدن‬
16202:                                                ‫خوانند ‪.‬‬               ‫بمعای داشخار است که ریم آهن باشد ‪.‬‬
24800:‫اول مخفف ریم است که‬          ‫یکت‬   ‫_‬    ‫ریخته باشدا‬      ‫و گوشت اندرون و بیرون دهان را لگیوزنند ‪-‬‬
26716:                                                              ‫پرومته از آن چرك و ریم آید؟‪ ۴‬و اين نون هم‬
=== پتیاره ===
BQT_v1_pages.txt:24031:وپارسی باستان(جنبیدن ورفتن) بنابراین پتیاره و پتیارك (پهلوی) لغة بمعنی جند رونده و برخلاف
BQT_v1_pages.txt:24037:که آن اژدها طرفه پتباره بود ۰ فردوسی
BQT_v1_pages.txt:24039:۰ رك : پتباره .
FSF_pages.txt:6283:                                              ‫=اسخ؛ پتیاره [] = پت ی‬
FSF_pages.txt:6681:                                                ‫‪۱۳۹‬‬                                        ‫‪7‬پتباره‬
FSF_pages.txt:6698:                 ‫پتباره (بروزن همسایه) پ=تیار‬         ‫کینه‌جویی سیاوش می‌آید‪ .‬سیاوش نیز که‬
=== پذیره ===
FSF_pages.txt:1777:                                            ‫‪- ۲‬دشمن را پذیره شدن برای نبرد به‬
FSF_pages.txt:6831:             ‫پذیره شدش دیو را جنگجوی‬                ‫سخنگوی و پرمایه آزادگان‬
FSF_pages.txt:6878:         ‫‪۱‬‬                             ‫پزان‬                                           ‫پذیره‬
FSF_pages.txt:7036:                                         ‫پرکار‬           ‫پذیره شدندش به آیین خویش‬
=== رنده MON ===
795:اشکك خونین. آب برنده: آب گوارا. آب 
3734:قوش برنده: برنده سفید] (.) نامی است از 
4819:آموز رنده: (6-)202-2002 را آمو حتن» 
20040:آورنده: )۱( آغاز» شروع.
```


## [2026-09-05T20:42:07.921Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BQT پتیاره footnote ===\"; sed -n '24020,24045p' BQT_v1_pages.txt; echo; echo \"=== FSF پتیاره ===\"; sed -n '6694,6706p' FSF_pages.txt; echo \"=== FSF پذیره ===\"; sed -n '6874,6886p' FSF_pages.txt",
 "description": "Print BQT patyareh footnote and FSF entries"
}
```


### [2026-09-05T20:42:07.985Z] TOOL RESULT

```
=== BQT پتیاره footnote ===
یز گفته اند -- و آ شوب و شور و غوغا را حم
۳۹
لشبر ه- بر وزن کنیره » هر چیز که
مکروه طبیمت باشد ٩٩‏ .
ب مننهی -
۱ ء ازیت بمعنی وی (< ۴
که چنن خوانده "یسنی. باريك بیزه « لت نامه > .
* لت نامه » . - امروزه 0654 گوند. ۵ - رك: هرگو . ۱ رك :دوازو لغت نامه.
۲ - نز ینواز » در پهلوی 084۷2626 از اوستا )081 + ۷۷36 (کفتن) بمعتی جواب
آمده. درپهلوی تورفان080۷732 «اونوالا +مو» .۰۱۲‏ ۸ - پپلوی0۵0۷47۵1. 0102727۵
از اوستا 09109272 (ضد آفرنش) * اسشق ۰۲۸4 مشتقاز ۳91 ( ضد) + ۵۲ ارستابی
وپارسی باستان(جنبیدن ورفتن) بنابراین پتیاره و پتیارك (پهلوی) لغة بمعنی جند رونده و برخلاف
رفتار کننده ۶ فاب ۱ : ۲۸۹ ح » . شهرسنانی گوید : «ومما اخبی به زرادشت فی کاب « زند
وستا» قال: سبظهر فیآخرالزمان رجل اسمه اشبدزیکا (هوشبدر) ومعناه «الرجل العالم » زین -
المالم بالدین والمدل شم بظهرفی زمانه «بتیاره» فیوفم ال فة فی‌امره و هلکه عشرین سنة » « ملل
7 رتنص ۱۸۲*.
_ جهانی برآن جنگ نظارء بود
که آن اژدها طرفه پتباره بود ۰ فردوسی
طوصیاشت ۱ص ۱۳ »
۰ رك : پتباره .
( بر هان اطع )» بفتح اول و سکون ثانی » بممنی
کوه باشد وآنرا جربی جبل خوانندا .
پجاد - بفتح اول بر وزن هزار , بععنی
پچ است که کوه باشد .
پجول - بنم اود بروزن ترول » بمعتی
کب گنتق :

=== FSF پتیاره ===
‫(سیاست‌نامه ‪ :)۸۱‬کهملک بکافر بپاید و با‬                                           ‫چیزی بودن‪:‬‬
                           ‫یمد‪.‬‬
                              ‫اظل‬
                                ‫سنتمپو‬                ‫افراسیاب به تحریک و فریب گرسیوز به‬
                 ‫پتباره (بروزن همسایه) پ=تیار‬         ‫کینه‌جویی سیاوش می‌آید‪ .‬سیاوش نیز که‬
‫اصل این واژه اوستایی است‪ .‬پائیتی آر‬                   ‫گرفتار نیرنگ گرسیوز شده است‪ .‬آشفته‬
 ‫(دارمستتر‪ .‬ارمزد و اهریمن‬          ‫ة‪1‬‬                        ‫چه بکند‪:‬‬    ‫اند‬
                                                                            ‫‌تدو‬
                                                                               ‫ینس‬
                                                                                 ‫میشا‬
                                                                                    ‫نپر‬
                                                                                      ‫و‬
 ‫‪ )۶۴۲‬و مرکب است از پائیتی [یهلوی‪:‬‬      ‫ص‬                     ‫فرنگیس گفت ای خردمند شاه‬
=== FSF پذیره ===
                    ‫ولی‬                              ‫نپذرفت پوزش برآشفت سخت‬
‫(‪)۳-۱۸-۲۵۲۱‬‬                                         ‫(‪)۶-۶۴۳-۲۶‬‬


         ‫‪۱‬‬                             ‫پزان‬                                           ‫پذیره‬
‫صفت فاعلی از بریدن‪ :‬پرنده پرواز کنند‪:‬‬               ‫اوستایی‪« :‬پئیتی ‪-‬ار» ‪ 7-12۳‬پهلوی‪:‬‬
                                             ‫‪1۳‬‬                                     ‫پرتاب تیر‬

‫لندن آمده و در دو نسخة دیگر به جای‬                                ‫فرود آرد از ابرپران عقاب‬
‫«پرچجین» واژه «آذین» ضبط است‪ .‬از‬                   ‫نتابد به تندی برو آفتاب‬
‫مفهوم دو بیت و «آذین» در دو نسخه دیگر‬              ‫(‪)۲-۷۷۱-۴۰۱‬‬
```


## [2026-09-05T20:42:25.071Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== MON رنده ===\"; grep -n \"رنده\" MON_part2.txt | head -5; echo \"=== SNS reman ===\"; grep -n \"reman\\|rēman\\|rytn\\|ritan\" SNS_pages.txt SNS.txt | head -5; echo \"=== CHEUNG ===\"; grep -n \"\\*Har-\\|\\*HraiH\\|\\*Hrad\\|ras-\\|rīdan\\|randīdan\" CHEUNG.txt | head -12",
 "description": "MON rande, SNS reman, Cheung"
}
```


### [2026-09-05T20:42:25.164Z] TOOL RESULT

```
=== MON رنده ===
23:گردآورنده عزیزالته علیزاده 
224:غاز؛ 2, [تر. - قاز] (.) (جاد.) پرنده‌ای 
309:غارنده» غاز بده). 
344:غصب کننده» گیرنده چیزی به قهر و ظلم؛ 
359:غافلگیر: تآو-« (ع. ف. - غافل‌گیرنده] 
=== SNS reman ===
SNS.txt:31605:reman 235/10 
SNS_pages.txt:15915:pusarSn 109/15             r3z 222/4                         reman 235/10           rtTd/rut 229/17
=== CHEUNG ===
510:IE meaning can be explained in terms of euphemistic usage, notably *HraiH ‘to 
1950:abhiyukta’ and may derive from *4-fras- ‘to inform’ (*fras/prs), on which see 
2640:*MISC: Огт. bras-/brastak ‘to burn [intr.]’ = brés-/bréSok, bróxtok 
5031:*AVESTAN: daras- ‘to see’ || (+ *ui-) ‘to see, erschauen’ || (+ *fra-(a-)-) ҮАУ. 
5064:*AVESTAN: (+ *upa-) Y Av. upadaras- ‘to dare’ — Liste: 28 
6447:SANSKRIT: ? vfka-dvaras- ‘running like a wolf ?’ (RV 2.30.4). Ф The interpretation 
6706:*AVESTAN: fras- (paras-) ‘to ask, inquire’, YAv. frasna- ‘question’ || (+ *4-) Чо be 
6758:*KHOTANESE: puls- ‘to ask’ || (+ *4-) (caus.) auräss (oras-, auras-) ‘to inform’ || (+ 
6785:*NEIR: Ishk. f(s)ras-/f(e)rüt-, Sh. (Baj.) peXc-/peXst-, Rosh. paws-/pawst, Sariq. 
7003:*SANSKRIT: psáras- (n.) ‘enjoyment, joy’ (RV) = EWAia II: 198 
9890:*AVESTAN: ras- (rāņh-) ‘to be disloyal, (?) apostatize’, YAv. ranha- ‘epileptic’ (Yt 
11330:*MIDDLE PERSIAN: (old inch.) MMP rs-, BMP Is- (YHMTWN-) /ras-/ ‘to come,
```


## [2026-09-05T20:42:28.491Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '11310,11360p' CHEUNG.txt; echo \"===== HraiH =====\"; grep -n \"HraiH\" CHEUNG.txt | head -6",
 "description": "Cheung *Har entry"
}
```


### [2026-09-05T20:42:28.579Z] TOOL RESULT

```
Пг. & Idg.: 262 ff. = Liste: 9, 10 

Pres. {1} them. red.: IND. 3sg. YAv. uziiöraiti (V 19.28); SUBJ. 35р. YAv. uziiarat (Yt 8.5), IMPV. 2sg. 
Y Av. uzaiiara (V 21.5), INJ. 3sg. YAv. nirat (Yt 8.38), 3pl. (?) YAv. *niron (Y 10.17), SUBJ. 3pl. YAv. 
*iránti (FrW 4.1), IMPV. 2sg. YAv. uzira (V 21.5, V 21.17), 3sg. OAV. iratü (Y 53.8); Pres. {2} athem.: 
IND. med. Zeg OAV. paiti.orote (Y 44.12); Aor. {1} athem.: IND. 15р. OAv. arom (Y 43.10), SUBJ. med. 
3р1. OAv. fraranté (Y 46.3); Aor. {2} them.: SUBJ. 3pl. YAv. 'aránti (V 15.4; Kümmel, Le: 264); 
Partic.: pres. YAv. uziiorant- (Yt 8.36); Inf.: pres. OAv. "uziroidiiai (Y 43.12, Y 43.14), aor. ? OAv. 
uruuané (Y 31.2); Caus.: pres. IND. 35р. YAv. "viiaraiieiti (V 18.26) 


*OLD PERSIAN: гѕ(5)а- (inch.) ‘to move, go or come toward’ || (+ *aua-) avars(s)a- ‘to 
go down to, arrive at’ || (+ *para-) parars(s)a- ‘to come to, arrive at’ || (+ *ni-) 
nirs(s)a- ‘to come down, descend’. 0 The transcription /rasa-/ is the generally 
accepted one, no doubt on the basis of modern Persian. — Kent: 169b 

Pres. inch.: impf. IND. 1sg. ars(s)am <a-r-s-m> (DB 1.54, DB 2.28, DB 2.48, DB 2.63), avars(s)am 
<a-v-a-[r]-[s]-[m]> (DB 5.23), <a-v-a-r-s-m> (DSf 24), 3sg. parärs(s)am <p-r-a-r-s-m> (DB 2.22, DB 
2.32, DB 2.52, etc.), SUBJ. 35р. nirs(s)atiy <n-i-r-s-a-t-i-y> (DPe 24) 

*MIDDLE PERSIAN: (old inch.) MMP rs-, BMP Is- (YHMTWN-) /ras-/ ‘to come, 


arrive’ = DMMPP: 296b 
Pres.: IND. 3sg. MMP гуа, MMP rsyyd, 3р1. MMP rsynd, SUBJ. 3sg. MMP rs’d, OPT. 3sg. MMP *rsy 


*SOGDIAN: (+ *abi-) BSogd. Byr- ‘to obtain, acquire, receive, find’, CSogd. byr- ‘to 
find, receive’, MSogd. Byr- ‘to obtain’ 

Widely attested: Pres.: IND. 15р. SSogd. Byr’m, 3sg. SSogd., BSogd. Byrt, 1р1. SSogd. Byrym, etc. 
*CHORESMIAN: (+ *api-) byry- ‘to desire’ (< intens. *api-Iraia-) || (+ *abi-) Byr- ‘to 
find, obtain’, (sec. inch./pass.) m/Byrs- ‘to be created, to become into existence’, 
(caus. inch.) m/Byrsy- ‘to create’ || (+ *uz-) m/wz’ry- ‘to establish’ (cf. MacKenzie 
IV: 533), ‘to make firm, elevate, perform (prayer), lead (a war)’ = Samadi: 34, 44, 
227 

*BACTRIAN: (+ *abi-) aßıp- ‘to obtain, find’ = S-W, Bact.: 175a 

*NWIR: Widely attested: NP rasidan/ras-, Zaz. resäyis/resen-, Abz. rasa/ras-, Anar. 
ireso/eres-, Gz. räs-/räsa, Gil. (Rsht.) fa-ráscen/fa-ráse-, Ham. resayan/res-, Isfah. 
resän/res-, Meim. be-resaj-/a-res-, Khuns. res-/resa, Mah. ris-, räs-, Nn. rassä/ras- 
(res-), Natan. -räsäj-/räs-, Qohr. rasa/res-, Semn. -rása, Shamerz. -räsim-/räsäm-, 
Siv. räs-/räsä, ráse, Soi -räs-/-räs- ‘to arrive, attain’, (caus.) NP rasan(i)dan/rasan- ‘to 
cause to arrive; to bring to bear; to convey’, Abyan. rasnoyan, Gz. räsn-/räsnä, Ham. 
resenayän/resen-, Jow. bam-rasno/a-rasn-, Meim. bem-resnä/a-resn-, Siv. räsän- ‘to 
send’, Nn. räsnä/räsn- ‘to cause to arrive, send’ || (+ *ni-) Kurd. (North.) hinärtin/ 
hinér-, (Central) (ha)nardin/nér- ‘to send’ (with sec. hin-, han- ?) 

*NEIR: Oss. I. aryn, waryn/ard, (+ *abi- ?) D. erun/ird ‘to arrive; to be born’, ? Sariq. 
yur (in xu dust mur yur ‘reach me your hand’) || (+ *abi- ?) Sh. (Baj.) viri-/virüd, 
===== HraiH =====
510:IE meaning can be explained in terms of euphemistic usage, notably *HraiH ‘to 
12809:188 *HraiH 
12825:etymologically connected to *HraiH and it is tempting to regard it as an enlarged 
12826:variant of *HraiH. This enlargement must be a purely Ir. development: °¢ is perhaps 
12840:*HraiH ‘to defecate’ 
56294:*Cialf (s.v), *HraiH, *xard
```


## [2026-09-05T20:42:35.457Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '12805,12870p' CHEUNG.txt; echo \"=== Har header ===\"; sed -n '11280,11312p' CHEUNG.txt | head -25",
 "description": "Cheung HraiH and Har headers"
}
```


### [2026-09-05T20:42:35.534Z] TOOL RESULT

```
Abz. reta/rej-, Abyan. retta/rej-, Ard. réte/rij-, Anar. risaye/ris-, Ham. rijayän (ret-) 
/rij-, Delij. ban. berriji, Nn. rite/rij-, Qohr. rita/rij-, Tr. rita/réj-, Varz. rite/rij- ‘to 


188 *HraiH 


pour (out)’, (caus.) Zaz. riznayis/riZnen- ‘to pour (out), shake out’, Gz. reZn-/reZna 
‘to let flow, pour, fall off, Gur. (Kand.) (ppp.) riziará/-riz- ‘to pour, strew’, Khuns. 
riZ-/rit ‘to scatter, spread’, Jow. bam-ri:t/a-ri:dz-, Meim. bem-ret/a-ri:dz-, Semn. 
ritä-, Shamerz. -rítam-/rizám-, Siv. гіё-, rëš-/ret ‘to pour, strew’, riš-/rešiā ‘to be 
poured, fall over’ (LW ?), Sorkh. dü-rát-/dá-riZ- ‘to pour’. © In many dialects the 
verb has been contaminated with *raiz?. 

*NEIR: Pash. rinjal ‘to have liquid stool’, (inch.-intr.) Yghn. rixs-, rexs- ‘to flow’, ? 
Oss. D. lixsun/lixst ‘to spit’, ? Wa. rox(n) ‘excrements; defecating' || (+ *aua-) Sariq. 
wareyz-/warezd ‘to melt [intr.]’ || (+ *pari-) Sh. pireX-/pirext, Rosh. pirix-/pirixt ‘to 
strew’ || (+ *fra-) Yi. forx-/farxi- ‘to stool’ 

© Exact IE correspondences of this root cannot be found. The root is no doubt 
etymologically connected to *HraiH and it is tempting to regard it as an enlarged 
variant of *HraiH. This enlargement must be a purely Ir. development: °¢ is perhaps 
from *ta£!. 

*PIE — > LIV: – | Pok.: 

*REFERENCES: KPF I: 140b f., 207a; Ivanow 1926: 421; KPF II: 202; Christensen, Contributions I: 164; 
Christensen, Contributions II: 57, 159; Abrahamian 1936: 120; IIFL II: 209a; Lambton 1938: 42a, 77b; 
Morgenstierne 1942: 264; Andreev — PeSéereva: 314b; Abaev, Slovar’ П: 46 Ё; EVS: 61a, 92b; WIM I: 


72; WIM ПЛ. 82; WIM Ш: 115; Safari 1373: 101; Cabolov 1997: 72; Paul 1998: 311b; 
Steblin-Kamenskij 1999: 304; Shahbakhsh: s.v. réc-; Korn 2005: 151, 199, 378 (passim) 


*HraiH ‘to defecate’ 
*AVESTAN: (+ *abi-) Y Av. auui ... irita (ppp.) ‘defecated’ (V 5.1) = Liste: 58 


*MIDDLE PERSIAN: BMP ld- /riy-/ ‘to defecate, void’ 
Pass.: IND. 3sg. BMP Iyt /rid/ 


*KHOTANESE: rrima ‘faeces’, riyai ‘anus’ 

*SOGDIAN: CSogd. rym (m.) “dirt, impurity’ 

*CHORESMIAN: rymyc (pl.) “dirty (spots)’ 

*NWIR: NP ridan/ri-, Bal. rit/ri(y)-, Kurd. ritin/rri-, Siv. rin-/rid ‘to defecate’, NP rim 
“pus, matter, humour; dregs, dross (vel sim.)’, Anar. rix ‘diarrhoea’ 

*NEIR: Oss. І. Iyjyn/lyd, D. ШипЛиа ‘to defecate’, Pash. roma, rima ‘mucus, 
dysentry’ 

*SANSKRIT: ray ‘to flow, drip, run, bubble up’ (RV+) > EWAia II: 437 

© The Ir. cognate root of Skt. ray has become an euphemism for ‘to defecate’, 
replacing forms of a root that was no doubt considered uncouth, possibly *zad 
(Y Av. zadanha (pl.) ‘backside, anus’, cf. Skt. had, EWAia Ш: 532). 

PIE *HoreiH- ‘to flow, stream’ > LIV: 305 | Pok.: 330 f. 

*IE COGNATES: Gr. ópívo ‘I bring in commotion, confuse’ (influenced by ópvuju ?), 
Lat. rivus (m.) ‘brook’, Olrish rian ‘river, sea’, Russ. réjat’ ‘to stream fast, flow’, 
rinut’ ‘to stream, to flow’, Cz. finouti se ‘to stream, to flow’ 
=== Har header ===

*Hard ‘to prosper’ 

*AVESTAN: ard- ‘to prosper’ — Liste: 10 

Aor. athem.: SUBJ. 3sg. OAv. aradat (Y 50.11) 

*KHOTANESE: (+ *pati-) pata(’)I- (pyal-) ‘to prosper’, LKh. pyalya- (P 3513.62v1 KT 
1.248, Vajr. 12b4 KT 3.22) ‘welfare’ © SGS: 82 

*SANSKRIT: ardh ‘to prosper, promote growth, success, etc.’ (RV+) = EWAia I: 118 
9 Further cognates are uncertain. 

«PIE ? *Hheld’- ‘to promote’ > LIV: 262 | Pok.: 27 

*IE COGNATES: Gr. &A Gat vo ‘I heal’ 

«REFERENCES: Werba 1997: 167 Ё; ESIJa I: 216 


*Har! ‘to go to(wards), reach’ 
*AVESTAN: ar- ‘to start to move’ || (+ *a-) ‘to come, arrive’ || (+ *uz-) ‘to rise, go up’ 
|| (+ *ni-) ‘to go, fall down’ || (+ *ui-) caus. ‘to drive off. 0 Assuming a separate
```


## [2026-09-05T20:42:45.133Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"\\*Hrad\\|rand-\\|randīdan\\|randidan\" CHEUNG.txt | head -8",
 "description": "Cheung Hrad"
}
```


### [2026-09-05T20:42:45.184Z] TOOL RESULT

```
4012:give’ (pret. supplet. of rand-, *HraH) || (+ *para-) Pash. prolal, Sh. paröäd-/parööd, 
8763:thunder, roar, fly in a passion’, Bal. grandit/grand- (denomin.) ‘to thunder’, Bal. 
8779:Steblin-Kamenskij 1999: 185; NEVP: 32; Shahbakhsh: s.v. grand-; Korn 2005: 317, fn. 200 
12297:*AVESTAN: OAv. morand- ‘to crush’ = Liste: 44 
12676:186 *Hrad 
12687:*Hrad ‘to dig, pave’ 
12733:*NEIR: Wa. rand-/rat- (rat) ‘to give’, (?) Oss. I. raddyn/rard, D. raddun/rard 
13109:*NEIR: (+ *us-) Yzgh. sori0-/sorust ‘to break, tear [intr.]’, sarand- (caus.) ‘to break,
```


## [2026-09-05T20:42:47.647Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '12687,12730p' CHEUNG.txt",
 "description": "Cheung *Hrad entry"
}
```


### [2026-09-05T20:42:47.691Z] TOOL RESULT

```
*Hrad ‘to dig, pave’ 
*AVESTAN: Y Av. raó- ‘to pave (a way)’, ? YAv. “pai0m raó- ‘road-paver’ (Yt 9.23). 
9 The long vowel of this hapax form is perhaps from the nominal derivative, on 


which see Kellens 1984: 116, 118 fn. 7f. — Liste: 56 
Pres. them.: IND. 3sg. YAv. raóaiti (Yt 10.68) 


*NWIR: Bal. rast'/raó- ‘to tear up the ground, be beaten’ 

*NEIR: (+ *fra-) Sh. (Baj.) raró-/ruxt ‘to dig, excavate, hollow out’, ? Rosh. rarö-/ruXt 
*to demolish, destroy, scatter? 

*SANSKRIT: rad ‘to dig, gnaw; to pave’ (RV+) = EWAia П: 430 

© The laryngeal disappeared in IIr., on which see further Lubotsky 1981: 134 ff. 

«PIE *HreHsd- ‘to gnaw, furrow’ (A.L.) = LIV: 497 | Pok.: 854 


*IE COGNATES: Lat. rödere ‘to gnaw (at) 
«REFERENCES: EVS: 68b; Shahbakhsh: s.v. raó- 


*HraH ‘to offer, give’ 

*AVESTAN: rã- ‘to offer, give’ = Liste: 57 

MED. ?; Aor. s-: IND. 2sg. YAv. fora ranhé (Y 12.3), INJ. Isg. YAv. fora rah (Y 0.5, Y 11.18), SUBJ. 
2sg. OAv. ranhanhoi (Y 28.8); Perf.: IND. 3pl. YAv. raire (Е 17); Partic.: pres. inch. act. YAv. rasant- (Y 
52.1, Y 52.3, et al. ?, v. Hoffmann, Aufs. I: 266, fn. 1) 


*SOGDIAN: BSogd. r't (pret. stem) ‘to give’ || (+ *pati-) CSogd. p’cr’t (m.) ‘reward’ 
Inf.: BSogd. rt 

*CHORESMIAN: (+ *para-) pry- ‘to leave, let go; to repudiate (wife); to take out [+ 
с]. 9 Although Samadi foremost maintains the reconstruction *para-isa- (*HaiSH ‘to 
set in motion’) for Chor. pry-, she also remarks that the past participle pr’dyk 
suggests *para-ra-ta-ka- (*raH). The latter proposal is preferable, especially since 
the reconstruction *para-isa- would rather yield Chor. **prys- or **pryh- The 
postulated pres. stem *para-rä(H)'-ia- would have undergone, subsequently, 
haplology and shortening of *4 in front of *Т (attested in Av. and Elr.). © Samadi:
```


## [2026-09-05T20:43:24.160Z] TOOL CALL #75: Bash

```json
{
 "command": "python3 /home/sfmqrb/git/rishe/tools/fetch_source.py \"https://en.wiktionary.org/wiki/are\" --note \"page 156 Er 1: English 'are' from Germanic *ar-\"; f=$(python3 -c \"import hashlib;print(hashlib.sha1('https://en.wiktionary.org/wiki/are'.encode()).hexdigest()[:16])\"); grep -n \"Middle English aren\\|Proto-Germanic\\|h₁es\\|Old English earun\\|From Middle English\" /home/sfmqrb/git/rishe/data/verification/sources/web/$f.txt | head -6",
 "description": "Wiktionary 'are' etymology"
}
```


### [2026-09-05T20:43:26.082Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/1a8819cf4ca66c6a.txt
873: Proto-Germanic *arun ? 
875: Middle English aren 
878: From Middle English aren , from Old English ( Anglian ) earun , earon ( “ are ” , plural ) . Possibly reinforced by the Old Norse plural forms in er- , this displaced the alternative forms Old English sind and bēoþ . In the second person singular it displaced archaic art . Further etymology controversial:
880: The English forms, as well as the Old Swedish forms in ær- , could reflect Proto-Germanic preterite-present *ōr ~ *arum , from Proto-Indo-European *h₃e-h₃ór-h₂e ( “ I have risen ” , perfect ) . [ 2 ] [ 3 ] 
882: Since they are not the expected outcomes of the Proto-Germanic forms of *wesaną ( “ to be ” ) in *iz- , they would have to be irregular alterations. For Seebold this explanation is still preferable as similar variants in other verbs are not uncommon. [ 4 ] 
1090: ^ Ringe, Donald ( 2006 ), From Proto-Indo-European to Proto-Germanic (A Linguistic History of English; 1)‎ [2] , 1st edition, Oxford: University Press, →ISBN , page 72 . Note: in the 2nd edition (2017) this example has been omitted.
```


## [2026-09-05T20:43:37.229Z] TOOL CALL #76: Bash

```json
{
 "command": "ls site/pages/156.jpg 2>/dev/null; pdftoppm -f 156 -l 156 -r 300 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg156 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/",
 "description": "Render PDF page 156"
}
```


### [2026-09-05T20:43:39.859Z] TOOL RESULT

```
site/pages/156.jpg
total 17668
drwx------ 2 sfmqrb sfmqrb    4096 Sep  5 16:43 .
drwx------ 4 sfmqrb sfmqrb    4096 Sep  5 16:02 ..
-rw-rw-r-- 1 sfmqrb sfmqrb   68775 Sep  5 16:43 ary440.png
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
-rw-rw-r-- 1 sfmqrb sfmqrb  101504 Sep  5 16:43 pg156.png
-rw-rw-r-- 1 sfmqrb sfmqrb  169880 Sep  5 16:34 pg158_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb   80624 Sep  5 16:34 pg158.png
-rw-rw-r-- 1 sfmqrb sfmqrb  124379 Sep  5 16:31 pg159_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb   27814 Sep  5 16:31 pg159.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4694 Sep  5 16:31 pg159_word.png
-rw-rw-r-- 1 sfmqrb sfmqrb  168057 Sep  5 16:34 pg161_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb   76745 Sep  5 16:34 pg161.png
-rw-rw-r-- 1 sfmqrb sfmqrb  110270 Sep  5 16:42 pg162_400.png
-rw-rw-r-- 1 sfmqrb sfmqrb   76438 Sep  5 16:42 pg162.png
-rw-rw-r-- 1 sfmqrb sfmqrb    8523 Sep  5 16:42 pg162_verse.png
-rw-rw-r-- 1 sfmqrb sfmqrb   25911 Sep  5 16:32 pg163.png
-rw-rw-r-- 1 sfmqrb sfmqrb   59398 Sep  5 16:33 pg164.png
-rw-rw-r-- 1 sfmqrb sfmqrb   61265 Sep  5 16:40 pg165.png
-rw-rw-r-- 1 sfmqrb sfmqrb   86005 Sep  5 16:39 pg168.png
-rw-rw-r-- 1 sfmqrb sfmqrb   68420 Sep  5 16:42 pg169.png
-rw-rw-r-- 1 sfmqrb sfmqrb   73551 Sep  5 16:43 pg171.png
-rw-rw-r-- 1 sfmqrb sfmqrb   44812 Sep  5 16:34 pg532.png
-rw-rw-r-- 1 sfmqrb sfmqrb  153161 Sep  5 16:34 pg532_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4868 Sep  5 16:14 prt.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  333088 Sep  5 16:16 sod135_c.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1817364 Sep  5 16:16 sod135.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  101641 Sep  5 16:15 sod136_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1892712 Sep  5 16:15 sod136.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   56398 Sep  5 16:26 write144.py
```


## [2026-09-05T20:43:44.810Z] TOOL CALL #77: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg156.png"
}
```


### [2026-09-05T20:43:45.490Z] TOOL RESULT

```

```


## [2026-09-05T20:43:45.488Z] INPUT

[Image: original 2550x3300, displayed at 1546x2000. Multiply coordinates by 1.65 to map to original image.]


## [2026-09-05T20:44:41.122Z] TOOL CALL #78: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg156.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/156.png && echo copied; cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SKT rival/run ===\"; grep -n \"^RIVAL\\|Rival,\\|RUN,\\|Run, \" SKT.txt | head -5; grep -on \"Rival.\\{0,180\\}\" SKT.txt | head -3; grep -on \"Run, to move.\\{0,200\\}\\|Run (1).\\{0,200\\}\" SKT.txt | head -3",
 "description": "Copy page PNG; grep Skeat"
}
```


### [2026-09-05T20:44:42.850Z] TOOL RESULT

```
copied
=== SKT rival/run ===
16129:Rival ;  sec  Rivulet. ,  to   tear.    (Scand .>      M.  E.  riucn —  Iccl.  H/a,  pt.  t.  rif,  pp.  rifinn  (  ^ »1.  to  rive  ;  Dan.  rive,  Swed.  rifva. t/iYW,  to  grate.  G.
```


## [2026-09-05T20:44:46.290Z] TOOL CALL #79: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -on \"Rivulet.\\{0,300\\}\" SKT.txt | head -2; echo ---; grep -on \"Orient.\\{0,250\\}\" SKT.txt | head -2; echo ---; grep -on \"Run.  (E.).\\{0,300\\}\\|Run,  to.\\{0,300\\}\" SKT.txt | head -3",
 "description": "Skeat rivulet, orient, run"
}
```


### [2026-09-05T20:44:48.106Z] TOOL RESULT

```
16129:Rivulet. ,  to   tear.    (Scand .>      M.  E.  riucn —  Iccl.  H/a,  pt.  t.  rif,  pp.  rifinn  (  ^ »1.  to  rive  ;  Dan.  rive,  Swed.  rifva. t/iYW,  to  grate.  G.  rriden,  to  grate, f.  Gk.  tptinuv,  to  dash  down,  l/Miir- ive;  Lilhuan.  r^Jtfi.  to  cut. (I),  a  ridge  of  rocks.  (Du.)   
16145:Rivulet).
---
260:Orient.
12867:Orient,  eastern.  (F.-L.>  F.  orUni.- L.  orictU;  stem  of  oriens,  rising,  the  east ; orig.  pres.  pt  of  oriri,  to  rise,  begin.  + Skt.  n.  to  rise.     (VAR.)
---
```


## [2026-09-05T20:44:55.111Z] TOOL CALL #80: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -on \"Are,  the.\\{0,60\\}\\|Are.  (E.).\\{0,250\\}\\|Art  (2).\\{0,250\\}\" SKT.txt | head -4; echo \"--- run\"; grep -on \"Run,.\\{0,250\\}\" SKT.txt | head -3; echo \"--- rivulet full\"; sed -n '16144,16148p' SKT.txt",
 "description": "Skeat are/art/run/rivulet"
}
```


### [2026-09-05T20:44:56.683Z] TOOL RESULT

```
--- run
--- rivulet full
—  Low  L.  ripariui,   belonging  to  a  shore.
—  L.  ripa,  shore,  bank.  The  special  <>ense nmy  have  been  due  to  some  confusion  with L.  riuuj  (Sec  Rivulet).
arrive.  (F.  -  L.)  F.  arriver.  -  Ixjw  L arripare,  adripare,  to  come  to  shore,  land.
—  L.  aJ,  to ;  ripa^  shore,  bank.  Dor. arriv-al.
Rivet.  (F. -Scand.)  F.  rivet,  'the welt  of  a  shoe,'  Cot.  ;  also  a  rivet  (Uttr^),
```


## [2026-09-05T20:45:04.653Z] TOOL CALL #81: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -on \"run, intr\\..\\{0,300\\}\\|OE\\. rinnan.\\{0,200\\}\" KLN_1966.txt | head -3; echo \"--- are\"; grep -on \"are, pres\\..\\{0,300\\}\\|aron.\\{0,200\\}\" KLN_1966.txt | head -3",
 "description": "Klein run/are"
}
```


### [2026-09-05T20:45:06.252Z] TOOL RESULT

```
--- are
1118:aron,  masc.  PN.;  in  the  Bible,  the  brother  of Moses.  —  LateL.,fr.  Gk.  ’Aotpwv.fr.  Heb.  Ahd- rSn,  which  is  prob.  of  Egyptian  origin.  Arab. Martin  is  borrowed  from  Hebrew.
1119:aron-ic,  adj.
2292:aronymous,  patronymic, synonym.
```


## [2026-09-05T20:45:09.887Z] TOOL CALL #82: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -on \"run, .\\{0,320\\}\" KLN_1966.txt | head -3; echo \"--- are2\"; grep -on \"are (2)\\|are, v\\..\\{0,300\\}\\|^are\\b.\\{0,300\\}\" KLN_1966.txt | head -3; echo \"--- rivulet\"; grep -on \"rivulet.\\{0,200\\}\" KLN_1966.txt | head -2",
 "description": "Klein run/are/rivulet"
}
```


### [2026-09-05T20:45:11.889Z] TOOL RESULT

```
4471:run,  fr.  OF.  baron , oblique  case  of  ber,  fr.  ML.  hard,  gen.  -unis, which  is  of  Teut.  origin ;  cp.  OHG.  baro,  ‘man  , prop,  ‘warrior’,  which  is  rel.  to  ON.  berjask , ‘to  fight’,  and  cogn.  with  OSlav.  horjp,  boriti, ‘to  fight’.  All  these  words  prob.  derive  fr.  I.-E. base  *bher-,  ‘to
5741:run, ‘brown’,  of  W.  Teut.  origin;  cp.  OHG.  bruno, ‘brown’  and  see  brown.  OProvcng.  brun.  It. bruno,  ‘brown’,  are  of  the  same  origin.  For  the ending  see  suff.  -ette.  Cp.  burnet. brunissure,  n.,  a  plant  disease  characterized  by the  browning  of  the  leaves  (plant  physiol.)  —  F., lit.  ‘a 
5741:run,  ‘brown’  See  prec.  word.
--- are2
3372:are
--- rivulet
3516:rivulet,  small  stream’,  fr.  L.  ar- rugia,  ‘shaft  or  pit  in  a  gold  mine’,  which  is prob.  formed,  fr.  ad-  and  ruga,  ‘wrinkle’;  the orig.  meaning  was  ‘a  digging  out’.  See  ruga, arse,
4241:rivulet  (dial.  E.)  —  OE.  base, rel.  to  OS.  beki,  ON.  bekkr,  Dan.  back,  Swed. back,  MDu.  beke,  Du.  beck,  OHG.  bah, MHG.,  G.  bach,  and  cogn.  with  Mir.  bual  (for *bhogla),  ‘flqwing
```


## [2026-09-05T20:45:17.052Z] AGENT

Now I have enough evidence. Writing the verification file.


## [2026-09-05T20:53:29.876Z] TOOL CALL #83: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build156.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\n\nPOKW = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%83er-\"\nW_RAS = \"https://en.wiktionary.org/wiki/%D8%B1%D8%B3%DB%8C%D8%AF%D9%86\"\nW_ARV = \"https://en.wiktionary.org/wiki/%D8%A7%D8%B1%D9%88%D9%86%D8%AF\"\nW_RID = \"https://en.wiktionary.org/wiki/%D8%B1%DB%8C%D8%AF%D9%86\"\nW_RIM = \"https://en.wiktionary.org/wiki/%D8%B1%DB%8C%D9%85\"\nW_RAN = \"https://en.wiktionary.org/wiki/%D8%B1%D9%86%D8%AF%D9%87\"\nW_ARE = \"https://en.wiktionary.org/wiki/are\"\nE_RIV = \"https://www.etymonline.com/word/rival\"\nE_ORI = \"https://www.etymonline.com/word/origin\"\n\nnodes = []\n\nnodes.append({\n \"id\": 1,\n \"lang\": \"Avestan / Old Persian\",\n \"words\": \"ar, ra 1; ras 1, rasa; paity-âra; pati-ara\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Avestan ar- (present stems ar-/arə-, iyar-/ir-, causative āraya-, ppp. -ərəta-) 'to set (oneself) in motion, to get to, reach' is the direct Iranian continuant of PIE *h₃er-; the thematic/zero-grade by-form Nourai writes 'ra 1' is the ə-grade stem (Av. rəna-, rāna-, cf. Pokorny's themat. root form (e)rə-). 'ras 1, rasa' is the inchoative *r̥-ske/o- > Proto-Iranian *r̥sa-, attested as Old Persian rasa- (impf. arasam 'I arrived', DB 1.54, 2.28; parārasam, niraṣatiy DPe 24) and as the Avestan sko-present beside Skt. r̥ccháti; Pokorny p.327 gives exactly '*re-skō in apers. rasatiy \\\"kommt, gelangt\\\", np. rasad ds.' Both compounds are paiti- 'against, back, towards' + the same root: Av. paitiiāra- n. 'counter-attack, counter-creation, plague' (Vd. 1.2 āat ahe paityārəm frākərəntat aŋrō mainyuš 'thereupon the Evil Spirit fashioned as its counter-creation ...'), which gives MP patyārag and NP patyāreh; and *pati-āra- 'a going to meet' > MP padīrag 'towards, to meet' > NP padīra/pazīreh. Nourai's 'pati-ara' is therefore not a second, different word but the same compound in its neutral, non-hostile use. All four items and both cross-references to 'Per 3' (the preverb paiti-) are correct.\",\n \"derivation_fa\": \"ستاک اوستایی ar- «به جنبش درآمدن، رسیدن» (ستاک‌های حال ar-/arə-، iyar-/ir-، سببی āraya-) دنبالهٔ مستقیم ریشهٔ هندواروپایی آغازین *h₃er- است. صورت «rasa» همان ستاک آغازی (اینخوآتیو) *r̥-ske/o- > ایرانی آغازین *r̥sa- است که در پارسی باستان rasa- (ماضی arasam «رسیدم» در بیستون ۱٫۵۴) گواهی شده؛ پوکورنی در صفحهٔ ۳۲۷ می‌نویسد: «*re-skō در پارسی باستان rasatiy، فارسی نو rasad». دو ترکیب paitiiāra- و *pati-āra- هر دو از پیشوند paiti- «در برابر، به‌سوی» و همین ریشه ساخته شده‌اند: نخستی «آفرینش وارونه، بلا» (وندیداد ۱٫۲) و دومی «به پیشواز رفتن». ادعای نورایی در این گره درست است.\",\n \"sources\": [POKW, W_RAS],\n \"ref_check\": [\n  {\"ref\": \"POK:327\", \"status\": \"supports\", \"note\": \"Pokorny IEW p.327 (POK_01.txt leaf 338-339): 'av. ar- \\\"(sich) in Bewegung setzen, hingelangen\\\", Präs.-St. ar-:arə-, iyar-:ir- (wie ai. iyarti:irta), Kaus. āraya-, Partiz. -ərəta-; sko-Präs. ai. r̥cchāti ... *re-skō in apers. rasatiy \\\"kommt, gelangt\\\", np. rasad ds.' — exactly the arrow drawn.\"},\n  {\"ref\": \"BRT:184\", \"status\": \"supports\", \"note\": \"Bartholomae, AiW col. 184 (BRT.txt line ~5251, running header \\\"'ar- 184\\\"): '• j., g., p. ¹ar- V. \\\"(sich) in Bewegung setzen\\\". Praes. 1 ar-:ir-, 5 iyar-, 14b rasa-, 30 (Kaus.) āraya-. — PPfP. -ərəta-', with the etymological note 'ai. r̥ta-, ... iyarti:irte, r̥cchati; np. rasad \\\"er kommt\\\"'. Both 'ar' and the present stem 'rasa' stand in this one column.\"},\n  {\"ref\": \"BRT:368\", \"status\": \"not_found\", \"note\": \"AiW col. 368 falls (BRT.txt lines 7890-7952, between the running headers '365 iδāt — iθra 366' and '371') among the entries iδa, iθa, iδe, it, inja, ənitay-, indra- — nothing about ar-/rasa- or paitiiāra-. The paitiiāra- material is in the pait- section (cols. ~830 ff.). Nourai's second column number does not lead to a supporting page.\"},\n  {\"ref\": \"FSF:105\", \"status\": \"partial\", \"note\": \"Noushin, Vazhe-namak (FSF_pages.txt line 6698) s.v. پتیاره: 'اصل این واژه اوستایی است. پائیتی آر ... و مرکب است از پائیتی' (citing Darmesteter, Ormazd et Ahriman §642) — supports paiti + ar- for paityāreh, but the OCR of this scan carries no printed page numbers, so p.105 itself could not be confirmed.\"}\n ],\n \"consulted\": [\n  {\"src\": \"BRT\", \"where\": \"col. 184 s.v. ¹ar- (BRT.txt ~line 5251)\", \"stance\": \"supports\", \"note\": \"'\\\"(sich) in Bewegung setzen\\\" ... 14b. rasa- ... np. rasad \\\"er kommt\\\"'.\"},\n  {\"src\": \"CHEUNG\", \"where\": \"s.v. *Har¹ 'to go to(wards), reach' (CHEUNG.txt lines 11290-11350)\", \"stance\": \"supports\", \"note\": \"'*AVESTAN: ar- \\\"to start to move\\\" || (+ *ā-) \\\"to come, arrive\\\"'; '*OLD PERSIAN: rs(s)a- (inch.) \\\"to move, go or come toward\\\" ... — Kent: 169b'; '*MIDDLE PERSIAN: MMP rs-, BMP ls- /ras-/ \\\"to come, arrive\\\"'.\"},\n  {\"src\": \"KNT\", \"where\": \"p.170 s.v. aruvasta- (KNT.txt leaf 192)\", \"stance\": \"supports\", \"note\": \"'from Ar. ar- \\\"move\\\" + suffix -vant- ... cf. Lt. orior \\\"arise\\\"' — Kent operates with the same Old Iranian root ar-.\"},\n  {\"src\": \"POK\", \"where\": \"p.327 (POK_01.txt leaf 338-339)\", \"stance\": \"supports\", \"note\": \"see ref_check.\"}\n ]\n})\n\nnodes.append({\n \"id\": 2,\n \"lang\": \"Persian\",\n \"words\": \"resîdan «رسیدن»; patyâreh «پتیاره ، پتیره»; pazîreh «پذیره»\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"رسیدن rasīdan continues Middle Persian rasīdan (Book Pahlavi ls-ytn', ideogram YHMTWN-tn'; Manichaean rs-ydn) 'to arrive, mature', itself the OP inchoative rasa- (< *r̥-ske/o- of Av. ar-); the present stem رس ras- is the bare Old Iranian stem, and نورسیده nō-rasīde 'newly arrived, newly ripe' shows the same past participle — MacKenzie already glosses MP rasīdan 'arrive, mature', so Nourai's double gloss 'to arrive, to ripe' is the inherited one, not a Persian innovation. پتیاره patyāreh comes through MP patyārag (Manichaean pdy'rg) 'adversary, calamity' from Av. paitiiāra-; the variant پتیره shows the ordinary NP loss of intervocalic -g plus the common ā > i weakening in an unstressed syllable. پذیره pazīreh is MP padīrag 'towards, against, to meet' (MacKenzie: 'padirag ... towards, against, counter-; ~ āmadan: come to meet'), from *pati-āra-ka-; MP d between vowels becomes NP ذ/ز (padīrag > paδīra > pazīra), exactly as in padīriftan > پذیرفتن. Ferdowsī's line quoted on the page (پذیره شدش دیو را جنگجوی) uses it in precisely the sense 'to go out to meet (an enemy)'.\",\n \"derivation_fa\": \"«رسیدن» از فارسی میانهٔ rasīdan (پهلوی کتابی ls-ytn'، مانوی rs-ydn) و آن از ستاک آغازی پارسی باستان rasa- است؛ ستاک حال «رس» همان ستاک کهن ایرانی است و «نورسیده» همان صفت مفعولی. مکنزی خودِ فعل پهلوی را «arrive, mature» معنی کرده، پس معنی دوگانهٔ «رسیدن / رسیده شدن (میوه)» میراثی است نه نوساخته. «پتیاره» از پهلوی patyārag و آن از اوستایی paitiiāra- «آفرینش وارونه، آفت»؛ گونهٔ «پتیره» با افتادن گِ پایانی و تضعیف واکه پدید آمده. «پذیره» از پهلوی padīrag «رویاروی، به پیشواز» است؛ دال میان‌واکه‌ای فارسی میانه در فارسی نو به ذ/ز بدل شده، درست همان‌گونه که padīriftan > «پذیرفتن». حاشیهٔ معین بر برهان قاطع نیز پتیاره را از paiti «ضد» + ar «جنبیدن و رفتن» می‌داند؛ ادعای نورایی درست است.\",\n \"sources\": [W_RAS],\n \"ref_check\": [\n  {\"ref\": \"HRN:137\", \"status\": \"supports\", \"note\": \"Horn, Grundriss no. 616 (HRN.txt leaf 158 = printed p.137): 'resīden \\\"ankommen, erreichen\\\", Praes. res-em, resānīden. ap. √ras \\\"kommen, gelangen\\\", arasam; phlv. rasītan, ras(i)šn (AV.), rasēnītan.' — precisely Nourai's arrow.\"},\n  {\"ref\": \"BQT:374\", \"status\": \"supports\", \"note\": \"Borhan-e Qate', Mo'in's etymological footnote to پتیاره (BQT_v1_pages.txt line 24031): 'پهلوی patyārak ... از اوستا paitiyāra (ضد آفرینش) ... مشتق از paiti (ضد) + ar اوستایی و پارسی باستان (جنبیدن و رفتن) بنابراین پتیاره و پتیارک (پهلوی) لغةً بمعنی ضد رونده و برخلاف رفتار کننده' — Mo'in's analysis is identical with Nourai's. (The OCR of this volume carries no printed page numbers, so p.374 itself could not be verified, only the entry.)\"},\n  {\"ref\": \"BQT:950\", \"status\": \"not_checked\", \"note\": \"the پذیره entry of Borhan-e Qate' could not be located in the OCR of vols. 1-2 (BQT_v1/v2_pages.txt) and the volumes carry no page tags; not verifiable from the local text.\"},\n  {\"ref\": \"FSF:107\", \"status\": \"supports\", \"note\": \"Noushin, Vazhe-namak s.v. پذیره (FSF_pages.txt line 6878): 'اوستایی: «پئیتی -ار» paiti-ar، پهلوی: ...' — the same paiti + ar analysis Nourai draws.\"},\n  {\"ref\": \"FFD:56\", \"status\": \"not_checked\", \"note\": \"Abolqasemi, Fe'l-hā-ye Fārsi-ye Dari exists locally only as an un-OCR'd scan (incoming/FFD); not consulted.\"}\n ],\n \"consulted\": [\n  {\"src\": \"PHD\", \"where\": \"p.70 s.v. rasīdan and p.63 s.v. padirag (PHD.txt lines 557, 536)\", \"stance\": \"supports\", \"note\": \"'rasidan, ras- [YHMTWN-tn' ...; ls-ytn! | M rs-ydn, N ~] arrive, mature'; 'padirag [ptylk' | M pdyrg, N padīra] towards, against, counter-. ~ āmadan: come to meet'.\"},\n  {\"src\": \"CHEUNG\", \"where\": \"s.v. *Har¹ (CHEUNG.txt line ~11340)\", \"stance\": \"supports\", \"note\": \"'*NWIR: NP rasīdan/ras- ... (caus.) NP rasan(i)dan/rasan- \\\"to cause to arrive\\\"'.\"},\n  {\"src\": \"HRN\", \"where\": \"no. 616, p.137\", \"stance\": \"supports\", \"note\": \"see ref_check.\"},\n  {\"src\": \"BQT\", \"where\": \"s.v. پتیاره, Mo'in's footnote\", \"stance\": \"supports\", \"note\": \"see ref_check.\"}\n ]\n})\n\nnodes.append({\n \"id\": 3,\n \"lang\": \"Avestan / Old Persian\",\n \"words\": \"aurva, aurvant; auruma; aurvat-aspa\",\n \"verdict\": \"transcription_suspect\",\n \"error_in\": \"book\",\n \"book_prints\": \"auruma\",\n \"correct_form\": \"auruna\",\n \"derivation\": \"Avestan aurva-, aurvant- 'swift; brave, a hero' (AiW col. 200) and Old Persian arva-/arvant- belong to the u-extension of the root, PIE *h₃r-ew-, i.e. *h₃ér-went-s > Proto-Indo-Iranian *Hárwant-, whence also Sanskrit árvan-, árvant- 'racer, courser'. Pokorny p.331 has it verbatim: 'ai. árvan-, árvant- \\\"eilend, Renner\\\", av. aurva-, aurvant- \\\"schnell, tapfer\\\"; vielleicht av. auruna- \\\"wild, grausam, von Tieren\\\"'. Kent p.170 derives OP aruvā- 'action' and aruvasta- 'activity, physical prowess' from the same adj. arva-/arvant-, 'from Ar. ar- \\\"move\\\" + suffix -vant-, cf. Lt. orior'. aurvaṱ.aspa- 'having swift horses' is a real Avestan bahuvrīhi, used both as the epithet of the Sun (Yt 6.1,4,6; Yt 10.13 hvarə.xšaētahe ... aurvaṱ.aspahe) and as the personal name of Vīštāspa's father (Yt 5.105 puθrəm yaṱ aurvaṱ.aspahe), and the cross-reference to root Ekwos for -aspa- is correct. — But the second item as printed, 'auruma: wildly', is not an Avestan word: Bartholomae has '• j., g. auruna- \\\"wild, ferus, saevus\\\"' (Yt 14.23, Y 34.9), and Pokorny's tentative addition to this very entry is auruna- too. Nourai's -m- is a misreading of -n-; the printed page (book p.126, PDF 156) really shows 'auruma', so this is the author's own misprint and the JSON extraction is faithful. With auruna- restored the whole node is sound.\",\n \"derivation_fa\": \"اوستایی aurva- و aurvant- «تند، چالاک؛ دلیر، پهلوان» (بارتولومه، ستون ۲۰۰) و پارسی باستان arva-/arvant- از گسترش u‌داری ریشه، یعنی *h₃r-ew-، ساخته شده‌اند: هندوایرانی آغازین *Hárwant- که سنسکریت árvant- «تازنده، اسب دونده» نیز از آن است. پوکورنی در صفحهٔ ۳۳۱ همین را می‌آورد. کنت (پارسی باستان، ص ۱۷۰) واژه‌های aruvā- و aruvasta- را از همین صفت می‌گیرد. ترکیب aurvaṱ.aspa- «دارندهٔ اسبان تیزرو» هم صفت خورشید است (یشت ۶٫۱) و هم نام پدر ویشتاسپ (یشت ۵٫۱۰۵). ولی صورت «auruma» در کتاب واژه‌ای اوستایی نیست؛ صورت درست auruna- «وحشی، درنده» است. تصویر صفحهٔ چاپی (ص ۱۲۶ کتاب) نشان می‌دهد که خودِ کتاب «auruma» چاپ کرده است، پس این خطای چاپی نورایی است نه خطای خوانش اسکن.\",\n \"sources\": [POKW, W_ARV],\n \"ref_check\": [\n  {\"ref\": \"POK:331\", \"status\": \"supports\", \"note\": \"Pokorny IEW p.331 (POK_01.txt leaf 344, section 'e. Basis ereu-'): 'ai. árvan-, árvant- \\\"eilend, Renner\\\", av. aurva-, aurvant- \\\"schnell, tapfer\\\"; vielleicht av. auruna- \\\"wild, grausam, von Tieren\\\"' — supports both the derivation and (with -n-) the second word.\"},\n  {\"ref\": \"KNT:170\", \"status\": \"supports\", \"note\": \"Kent, Old Persian p.170 (KNT.txt leaf 192): 'aruvā- sb. \\\"action\\\" ... fem. to adj. arva-, Av. aurva- \\\"schnell, tapfer\\\" (Bthl. AiW 200), doublet to Av. aurvant-'; 'aruvasta- sb. \\\"activity\\\" ... to arvant- \\\"moving\\\", Av. aurvant- \\\"schnell, tapfer, Held\\\", Skt. arvant-, from Ar. ar- \\\"move\\\" + suffix -vant-, cf. Lt. orior \\\"arise\\\"'.\"},\n  {\"ref\": \"IRN:112\", \"status\": \"not_checked\", \"note\": \"Farahvashi, Iranvij exists locally only as an un-OCR'd scan (incoming/IRN); not fetched for this page.\"}\n ],\n \"consulted\": [\n  {\"src\": \"BRT\", \"where\": \"cols. 189-200 (aurvant-, aurva-) and col. 197 s.v. auruna- (BRT.txt lines 5583, 5383); Yt 5.105 in the viδaᵛvant- entry (line 24610)\", \"stance\": \"supports\", \"note\": \"'j., g. aurvant-, aourvant- Adj. \\\"schnell; tapfer, Held\\\"'; '• j., g. auruna- \\\"wild, ferus, saevus\\\"'; 'puθrəm yaṱ aurvaṱ.aspahe' — Vīštāspa 'son of Aurvaṱ.aspa'.\"},\n  {\"src\": \"NYB\", \"where\": \"Glossary p.28 s.v. arvand\", \"stance\": \"supports\", \"note\": \"'arvand [lwnd] swift 228. — Av. (200) aurvant-' (NYB_vol2_glossary.txt line 656), with 'arvandēh valour, gallantry'.\"},\n  {\"src\": \"POK\", \"where\": \"p.331\", \"stance\": \"supports\", \"note\": \"see ref_check.\"}\n ]\n})\n\nnodes.append({\n \"id\": 4,\n \"lang\": \"Persian\",\n \"words\": \"Arvand «اروند»; Alvand «الوند»; Lohrâsp «لهراسپ»\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"اروند Arvand is Middle Persian arwand 'swift, valiant' (MacKenzie: 'arwand swift, valiant; river Orontes; ~īh swiftness, valour'; Nyberg: 'arvand swift — Av. aurvant-'), i.e. Av. aurvant- with the regular MP loss of the diphthong (au > a before r + consonant) and of the final -t. Used as a river-name it means 'the swift one', and in New Persian it is the Iranian name of the Tigris — the very point of Ferdowsī's couplet printed on the page, 'if you do not know the Pahlavi tongue, call Arvand \\\"Dijla\\\" in Arabic'. الوند Alvand is the same word with the sporadic Persian r > l (as in زلف/زرف, لشکر); Borhan-e Qate' says so outright: 'اروند بر وزن و معنی الوند است و آن کوهی باشد در نواحی همدان ... و دجلهٔ بغداد را نیز گفته‌اند'. لهراسپ Lohrāsp is Av. aurvaṱ.aspa- 'having swift horses' through MP Lohrāsp — the name of Vīštāspa/Goshtāsp's father in both the Avesta and the Šāhnāme, so the semantic and genealogical identification is exact. Nourai's NOTE ('\\\"Arvand:swift\\\" is a translation of \\\"Dejleh:swift\\\"') is right in substance for the Greek/Old Persian side — the Greek Tígris rests on OP Tigrā, associated with tigra- 'pointed, swift' (root *steig-) — though Arabic دجله itself descends from Aramaic Diglat < Akkadian Idiqlat < Sumerian Idigna rather than from a Persian word for 'swift'; Nourai's cross-reference to root 'Steig' is therefore the right place to look.\",\n \"derivation_fa\": \"«اروند» همان arwand فارسی میانه است؛ مکنزی آن را «swift, valiant؛ نام رود» و نیبرگ آن را «تند، از اوستایی aurvant-» معنی کرده‌اند. مصوت مرکب au در فارسی میانه پیش از r + همخوان به a ساده شده و t پایانی افتاده است. این واژه به‌عنوان نام رود یعنی «تندرو» و در فارسی نو نام ایرانی دجله است؛ همان نکته‌ای که بیت فردوسی («به تازی تو اروند را دجله خوان») می‌گوید. «الوند» همان واژه است با ابدال ر به ل؛ برهان قاطع صریحاً می‌نویسد: «اروند بر وزن و معنی الوند است و آن کوهی باشد در نواحی همدان». «لهراسپ» از اوستایی aurvaṱ.aspa- «دارندهٔ اسبان تیزرو»، نام پدر ویشتاسپ در اوستا و شاهنامه است. یادداشت نورایی دربارهٔ برابری «اروند: تیز» با «دجله: تیز» از سوی یونانی/پارسی باستان (Tigris < تیگرا «تیز») درست است، هرچند خودِ «دجله» عربی از اکدی Idiqlat می‌آید. ادعای نورایی درست است.\",\n \"sources\": [W_ARV],\n \"ref_check\": [\n  {\"ref\": \"BQT:111\", \"status\": \"supports\", \"note\": \"Borhan-e Qate' s.v. اروند (BQT_v1_pages.txt lines 11138-11150): 'اروند ـ بر وزن و معنی الوند است و آن کوهی باشد در نواحی همدان ... و دریای محیط ـ و گرداب ـ و دجلهٔ بغداد را نیز گفته‌اند ... و بمعنی حسرت و آرزو هم آمده است ـ و فر و شکوه و زیبایی را نیز گویند' — the Arvand = Alvand = Tigris equation Nourai draws. (Volume OCR has no page tags, so p.111 itself could not be confirmed.)\"},\n  {\"ref\": \"BQT:160\", \"status\": \"partial\", \"note\": \"the الوند entries in BQT_v1_pages.txt (lines 8642, 10344, 12620) mention 'کوهی در همدان که بالوند شهرت دارد' and 'همدان مشهور بالوند', i.e. they confirm the mountain but the local OCR gives no etymological footnote and no page numbers.\"},\n  {\"ref\": \"BQT:1918\", \"status\": \"not_checked\", \"note\": \"p.1918 falls in Borhan-e Qate' vol. 4, which exists locally only as an un-OCR'd scan (incoming/BQT/BQT_v4_picofile.pdf); the لهراسپ entry was not fetched.\"},\n  {\"ref\": \"IRN:114\", \"status\": \"not_checked\", \"note\": \"Farahvashi, Iranvij: un-OCR'd local scan only.\"}\n ],\n \"consulted\": [\n  {\"src\": \"PHD\", \"where\": \"p.13 s.v. arwand (PHD.txt line 214)\", \"stance\": \"supports\", \"note\": \"'arwand [/wnd] swift, valiant; river Orontes. ~īh: swiftness, valour.'\"},\n  {\"src\": \"NYB\", \"where\": \"Glossary s.v. arvand (NYB_vol2_glossary.txt line 656)\", \"stance\": \"supports\", \"note\": \"'arvand [lwnd] swift 228. — Av. (200) aurvant-.'\"},\n  {\"src\": \"MON\", \"where\": \"s.v. اروند (MON_part1.txt line 10308)\", \"stance\": \"supports\", \"note\": \"'اروند [تند، تیز، چالاک، دلیر ...]' — Mo'in glosses the word itself as 'swift, brisk, brave'.\"},\n  {\"src\": \"BQT\", \"where\": \"s.v. اروند\", \"stance\": \"supports\", \"note\": \"see ref_check.\"}\n ]\n})\n\nnodes.append({\n \"id\": 5,\n \"lang\": \"Sanskrit\",\n \"words\": \"rad, radati\",\n \"verdict\": \"disputed\",\n \"derivation\": \"The word itself is real and correctly glossed: Sanskrit rádati 'scratches, gnaws, digs, furrows' (RV+), vi-rádati 'splits open'. Nourai's page reference is also literally accurate — Pokorny does print it inside the er-3 entry, on p.330 under the extension er-ed-. But Pokorny puts it there only with an explicit hesitation, 'weiter hierher oder zu 5. er- ai. rádati \\\"kratzt, ritzt, gräbt, hackt\\\"', and modern scholarship has decided against the er- connection: rádati belongs with Latin rādō, rōdō to PIE *reh₁d-/*HreHd- 'to gnaw, scrape, furrow' (Pokorny 854 rēd-, rōd-, rəd-; LIV² 497). Cheung's Iranian dictionary lists the root separately as *Hrad 'to dig, pave' (Av. raδ- 'to pave a road', Yt 10.68 raδaiti) and gives 'PIE *HreHd- \\\"to gnaw, furrow\\\" > LIV: 497 | Pok.: 854', with Latin rōdere as the IE cognate. So the arrow ROOT → #5 attaches a word of a different root to Er 1: the branch is genuine as a family (#5 → #6 below is fine), but its head is wrong.\",\n \"derivation_fa\": \"واژه درست است: سنسکریت rádati «می‌خراشد، می‌کَنَد، شیار می‌زند» (ریگ‌ودا به بعد). ارجاع نورایی هم لفظاً درست است، چون پوکورنی این واژه را در همان صفحهٔ ۳۳۰ ذیل er-3 آورده، اما با تردید صریح: «یا اینجا یا ذیل er-5». پژوهش امروزی این پیوند را رد می‌کند و rádati را با لاتینی rādō/rōdō به ریشهٔ *reh₁d-/*HreHd- «ساییدن، شیار زدن» می‌برد (پوکورنی ۸۵۴؛ LIV² ۴۹۷). چونگ نیز آن را ریشهٔ جداگانهٔ ایرانی *Hrad «کندن، راه‌سازی کردن» (اوستایی raδ-) می‌داند و PIE آن را *HreHd- می‌نویسد. پس پیوند این گره به ریشهٔ «Er» را دانش امروز نمی‌پذیرد، هرچند خودِ خانوادهٔ واژگانی درست است.\",\n \"sources\": [POKW],\n \"ref_check\": [\n  {\"ref\": \"POK:330\", \"status\": \"partial\", \"note\": \"Pokorny IEW p.330 (POK_01.txt leaf 342): 'weiter hierher oder zu 5. er- ai. rádati \\\"kratzt, ritzt, gräbt, hackt\\\", vi-radati \\\"zertrennt, eröffnet\\\"; vielleicht auch apr. redo \\\"Furche\\\"'. The page really carries the word, but Pokorny himself offers er-5 as the alternative and does not commit.\"}\n ],\n \"consulted\": [\n  {\"src\": \"CHEUNG\", \"where\": \"p.186 s.v. *Hrad 'to dig, pave' (CHEUNG.txt lines 12687-12700)\", \"stance\": \"contradicts\", \"note\": \"'*SANSKRIT: rad \\\"to dig, gnaw; to pave\\\" (RV+) = EWAia II: 430 ... *PIE *HreHd- \\\"to gnaw, furrow\\\" (A.L.) = LIV: 497 | Pok.: 854. *IE COGNATES: Lat. rōdere \\\"to gnaw (at)\\\"' — a root distinct from *h₃er-.\"},\n  {\"src\": \"POK\", \"where\": \"p.330 and p.854 (rēd-)\", \"stance\": \"partial\", \"note\": \"listed under er-3 with an explicit 'oder zu 5. er-'; the competing lemma rēd-, rōd-, rəd- stands at p.854.\"},\n  {\"src\": \"HRN\", \"where\": \"no. 622, p.138\", \"stance\": \"supports\", \"note\": \"Horn connects the Iranian words with 'ai. √rad, rádati \\\"kratzen, ritzen\\\"' — i.e. the Indo-Iranian equation itself is uncontroversial; only its attachment to Er is.\"}\n ]\n})\n\nnodes.append({\n \"id\": 6,\n \"lang\": \"Persian\",\n \"words\": \"randîdan «رندیدن» (rande «رنده»)\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"The arrow drawn here — Persian randīdan beside Sanskrit rádati — is right. رندیدن 'to scrape, grate, plane' continues Middle Persian randīdan (MacKenzie: 'randīdan, rand- [/nd-ytn'] scratch, grate, abrade'; Horn: 'phlv. randītan (AV.)'), from Proto-Iranian *rand- , a nasal-infixed/present enlargement of the *Hrad root that Sanskrit shows in rádati. The instrument noun رنده rande 'plane, grater' is the ordinary Persian -a nomen instrumenti to that stem, and it was already borrowed into early Classical Arabic as رَنْدَج randaj, which shows that a Middle Persian *randag existed. Horn no.622 draws exactly Nourai's line ('rendīden \\\"schaben, kratzen\\\", rende. ai. √rad, rádati \\\"kratzen, ritzen\\\"; phlv. randītan'). The one reservation is inherited from node #5: the family as a whole hangs from PIE *HreHd-, not from Er 1.\",\n \"derivation_fa\": \"پیوندی که این‌جا کشیده شده درست است: «رندیدن» دنبالهٔ randīdan فارسی میانه است (مکنزی: «scratch, grate, abrade»؛ هرن: «phlv. randītan») از ایرانی آغازین *rand-، گونهٔ خیشومی‌شدهٔ همان ستاکی که سنسکریت آن را rádati نشان می‌دهد. «رنده» اسم ابزار با پسوند ـه از همین ستاک است و صورت پهلوی *randag آن در عربی کهن به شکل «رَنْدَج» وام گرفته شده است. هرن (شمارهٔ ۶۲۲) همین زنجیره را می‌آورد. تنها ایراد، ایرادِ گرهِ پیشین است: این خانواده به ریشهٔ *HreHd- می‌رسد نه به «Er».\",\n \"sources\": [W_RAN],\n \"ref_check\": [\n  {\"ref\": \"MON:964\", \"status\": \"not_found\", \"note\": \"Mo'in, Farhang-e Fārsi: the local OCR (MON_part1/part2.txt) has no locatable رنده / رندیدن headword (greps for 'رنده' return only compounds such as آورنده, برنده), and the text carries no page numbers, so p.964 could not be checked.\"},\n  {\"ref\": \"HRN:138\", \"status\": \"supports\", \"note\": \"Horn, Grundriss no. 622 (HRN.txt leaf 159 = printed p.138): 'rendīden \\\"schaben, kratzen\\\", rende. ai. √rad, rádati \\\"kratzen, ritzen\\\"; phlv. randītan (AV.). kurd. renīn; bal. randag \\\"kämmen\\\".' — verbatim Nourai's arrow, including the noun rande.\"}\n ],\n \"consulted\": [\n  {\"src\": \"PHD\", \"where\": \"p.70 s.v. randīdan (PHD.txt line 555)\", \"stance\": \"supports\", \"note\": \"'randīdan, rand- [/nd-ytn! | N ~] scratch, grate, abrade.'\"},\n  {\"src\": \"HRN\", \"where\": \"no. 622, p.138\", \"stance\": \"supports\", \"note\": \"see ref_check.\"},\n  {\"src\": \"Wiktionary\", \"where\": \"s.v. رنده\", \"stance\": \"supports\", \"note\": \"'From Middle Persian *randag, found also in early Classical Arabic as رَنْدَج (randaj), derivative to the verb رندیدن (randidan, \\\"to grate, to scrape\\\").'\"}\n ]\n})\n\nnodes.append({\n \"id\": 7,\n \"lang\": \"Avestan\",\n \"words\": \"rî, rae, raec 1\",\n \"verdict\": \"plausible\",\n \"derivation\": \"Two of the three items are right, the third is not. Avestan raii-/rī- 'to let flow, release; to defecate' is the yé-present *h₃riH-yé-ti of the erei-/reiə- basis of this very root: Bartholomae's headword is '• j. ray- V. \\\"kacken\\\"; nur mit Praev. Inf. -irita ... np. rīyad, rīdan \\\"kacken\\\"; ai. riṇáti (auch riyáti) \\\"er lässt laufen\\\"' (AiW col. 1511), and Cheung's *HraiH 'to defecate' gives 'PIE *H₃reiH- \\\"to flow, stream\\\" > LIV: 305 | Pok.: 330 f.' — i.e. exactly Pokorny's page under er-3. So 'rī' and its ablaut form 'raē' are correctly placed, and the gloss 'to release, discharge, defecate' matches Bartholomae's and Buck's ('Av. rī- (only with prefix), NPers. rīdan \\\"cacare\\\" : Skt. rī- \\\"let go, release\\\", raya- \\\"flow\\\"'). But 'raec' is a different Avestan verb: raēk-/iriš-, present irinaxti, s-aorist raēxš, 'linquere, to leave, abandon' (AiW col. 1487, '• j. raek- V. \\\"linquere\\\"'), which belongs to PIE *leykʷ- (Pokorny 669-70; Latin linquō, Greek leípō), not to *h₃er-. Nourai has folded it in because its meaning 'to release' looks like rī-'s. Everything the chart builds on this node (#8, #9) rests on the sound half.\",\n \"derivation_fa\": \"دو مورد از سه مورد درست است. اوستایی raii-/rī- «رها کردن، روان کردن؛ ریدن» همان حالِ *h₃riH-yé-ti از پایهٔ erei-/reiə- همین ریشه است؛ بارتولومه (ستون ۱۵۱۱) می‌نویسد: «ray- فعل «کاکن»، تنها با پیشوند ... فارسی نو rīyad، rīdan؛ سنسکریت riṇáti «رها می‌کند»». چونگ نیز ذیل *HraiH می‌آورد: «PIE *H₃reiH- «روان شدن» > LIV ۳۰۵ | پوکورنی ۳۳۰». پس «rī» و گونهٔ «raē» درست‌اند. اما «raec» فعل دیگری است: اوستایی raēk-/irič- «رها کردن، وانهادن» (بارتولومه ستون ۱۴۸۷: «raek- V. linquere») که از ریشهٔ هندواروپایی *leykʷ- (لاتینی linquō، یونانی leípō) می‌آید و ربطی به *h₃er- ندارد. نورایی به سبب نزدیکی معنایی «رها کردن» آن را در همین جعبه گنجانده است. با احتیاط پذیرفتنی است.\",\n \"sources\": [W_RID, POKW],\n \"ref_check\": [\n  {\"ref\": \"BQT:987\", \"status\": \"not_checked\", \"note\": \"the ریدن / ریم entries of Borhan-e Qate' could not be located in the OCR of vols. 1-2 (the ریـ range is very poorly OCR'd) and the volumes carry no page tags.\"},\n  {\"ref\": \"SYN:278\", \"status\": \"supports\", \"note\": \"Buck, Selected Synonyms §4.66 'Void excrement' (SYN.txt line ~7129, printed pp.277-278): 'Av. rī- (only with prefix), NPers. rīdan \\\"cacare\\\" : Skt. rī- \\\"let go, release\\\", raya- \\\"flow\\\", etc. Barth. 1511. Horn 639.' — Nourai's page may be off by one, but the paragraph is the one he means, and it supports both the Avestan form and the gloss.\"},\n  {\"ref\": \"HRN:142\", \"status\": \"supports\", \"note\": \"Horn no. 639 (HRN.txt leaf 163 = printed p.142): 'rīden \\\"kacken\\\" ... aw. √raē-(?), avi dim irita \\\"kackt darauf\\\" (vd. 5,1) ... ai. √rē-, riyáti \\\"frei lassen, laufen lassen\\\"'.\"}\n ],\n \"consulted\": [\n  {\"src\": \"BRT\", \"where\": \"col. 1511 s.v. ray- (BRT.txt lines 25172-25173) and col. 1487 s.v. raek- (line 24726)\", \"stance\": \"partial\", \"note\": \"'• j. ray- V. \\\"kacken\\\"; nur mit Praev. ... np. rīyad, rīdan \\\"kacken\\\"; ai. riṇáti' supports rī-/raē-, but the separate headword '• j. raek- V. \\\"linquere\\\"' shows that raēc- is another root.\"},\n  {\"src\": \"CHEUNG\", \"where\": \"p.188 s.v. *HraiH 'to defecate'\", \"stance\": \"supports\", \"note\": \"'*AVESTAN: (+ *abi-) YAv. auui ... irita (ppp.) \\\"defecated\\\" (V 5.1) ... PIE *H₃reiH- \\\"to flow, stream\\\" > LIV: 305 | Pok.: 330 f.'\"},\n  {\"src\": \"POK\", \"where\": \"p.330, basis erei-/reiə-\", \"stance\": \"supports\", \"note\": \"'ai. riṇāti, riṇvati \\\"lässt fliessen, entlaufen, entlässt\\\", rīyate, rīṇa-, rīti- ... zum u-Suffix vgl. unten lat. rīvus' — this is the sub-basis of er-3 to which rī- belongs.\"},\n  {\"src\": \"SYN\", \"where\": \"§4.66, pp.275-278\", \"stance\": \"supports\", \"note\": \"see ref_check.\"}\n ]\n})\n\nnodes.append({\n \"id\": 8,\n \"lang\": \"Pahlavi\",\n \"words\": \"rîtan; rěman\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Middle Persian rīdan/rīy- 'to defecate' (Book Pahlavi ld- /riy-/, 3sg. lyt /rīd/) is the regular continuation of Proto-Iranian *HriHyátī, i.e. the Avestan raii-/rī- of the parent node; Horn cites the Pahlavi forms from the Ardā Wirāz Nāmag as 'phlv. rītan, rēman, rēmanīh'. The second word, rēman, is the derived adjective/noun in *-man-: MacKenzie 'rēm [lym | M rym] dirt, filth, purulence' and 'rēman [lymn'] dirty, filthy, purulent; ~īh: filth'. Nourai's gloss 'dirty discharges from eyes etc.' is narrower than the Pahlavi usage (rēman is the general word for ritual and physical impurity — it is the standard term of the Šāyast nē-šāyast purity code, where the Shiraz glossary indexes 'rēman 235/10'), but the form, the meaning-field and the descent from rī- are all correct. Nourai's transliteration 'rěman' with a short e is his own convention for MP ē.\",\n \"derivation_fa\": \"فارسی میانهٔ rīdan/rīy- «ریدن» (پهلوی کتابی ld-، سوم‌شخص lyt) دنبالهٔ منظم ایرانی آغازین *HriHyátī، یعنی همان raii-/rī- اوستایی گرهِ بالاست؛ هرن صورت‌های پهلوی را از ارداویراف‌نامه چنین می‌آورد: «phlv. rītan, rēman, rēmanīh». واژهٔ دوم، rēman، مشتق با پسوند ‌man‌ است: مکنزی «rēm: چرک، پلیدی» و «rēman: پلید، چرکین؛ rēmanīh: پلیدی». معنایی که نورایی داده («ترشح چرکین چشم») تنگ‌تر از کاربرد پهلوی است، زیرا rēman اصطلاح عام ناپاکی آیینی در شایست‌ناشایست است، اما صورت و خانوادهٔ واژه و اشتقاق آن از rī- درست است. ادعای نورایی درست است.\",\n \"sources\": [W_RID],\n \"ref_check\": [\n  {\"ref\": \"HRN:142\", \"status\": \"supports\", \"note\": \"Horn no. 639, p.142: 'phlv. rītan, rēman, rēmanīh' — both Pahlavi words in one line, under the Avestan √rī.\"},\n  {\"ref\": \"BQT:987\", \"status\": \"not_checked\", \"note\": \"not locatable in the local Borhan-e Qate' OCR (see node #7).\"},\n  {\"ref\": \"SNS:235\", \"status\": \"supports\", \"note\": \"Tavoosi, Vāzhe-nāme-ye Šāyast nē-Šāyast: the Latin index lists 'rēman 235/10' (SNS.txt line 31605; SNS_pages.txt line 15915), i.e. the word occurs at p.235 line 10 of the text — Nourai's page reference is exact.\"}\n ],\n \"consulted\": [\n  {\"src\": \"PHD\", \"where\": \"p.71 s.v. rēm / rēman (PHD.txt line 557)\", \"stance\": \"supports\", \"note\": \"'rēm [lym | M rym, N ~] dirt, filth, purulence. rēman [lymn' | M rymn, N ~] dirty, filthy, purulent. ~īh: filth.'\"},\n  {\"src\": \"CHEUNG\", \"where\": \"p.188 s.v. *HraiH\", \"stance\": \"supports\", \"note\": \"'*MIDDLE PERSIAN: BMP ld- /riy-/ \\\"to defecate, void\\\"; Pass.: IND. 3sg. BMP lyt /rīd/'; also 'CSogd. rym (m.) \\\"dirt, impurity\\\"', 'Khot. rrīma \\\"faeces\\\"'.\"},\n  {\"src\": \"HRN\", \"where\": \"no. 639, p.142\", \"stance\": \"supports\", \"note\": \"see ref_check.\"},\n  {\"src\": \"SNS\", \"where\": \"glossary index, 'rēman 235/10'\", \"stance\": \"supports\", \"note\": \"see ref_check.\"}\n ]\n})\n\nnodes.append({\n \"id\": 9,\n \"lang\": \"Persian\",\n \"words\": \"rîdan «ریدن»; rîm «ریم ، ریمن ، ریمه»\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"ریدن rīdan (present stem رین rīn-, older ری rī-) is Middle Persian rīdan/rīy- unchanged apart from the New Persian infinitive ending; Cheung lists 'NP rīdan/rī-' with Balochi rit/rī(y)-, Kurdish rîtin and Ossetic līyyn under *HraiH, and Wiktionary's chain is 'Middle Persian rīdan < Old Persian < Proto-Iranian *HriHyátī < Proto-Indo-Iranian *HriHyáti < PIE *h₃riH-yé-ti \\\"to flow\\\"', with Sanskrit rī́yate as the cognate. ریم rīm 'pus, filth' is MP rēm (MP ē > NP ī regularly, cf. šēr > šīr), and Cheung gives it in the same entry: 'NP rīm \\\"pus, matter, humour; dregs, dross\\\"'. ریمن rīman is MP rēman 'polluted, filthy' (as in the Manūčehrī line quoted on the page, ریمنی 'foulness'), and ریمه rīme is the -a derivative. One caveat that Nourai does not signal: Horn (no. 643) warns that the homophonous ریمن 'deceitful' belongs to رِیو rēw 'trickery' (Skt. rip-, root *leyp-) and must not be joined to rīm 'pus'; only the 'filthy' sense of ریمن belongs here.\",\n \"derivation_fa\": \"«ریدن» همان rīdan فارسی میانه است و جز پایانهٔ مصدری فارسی نو تفاوتی ندارد؛ چونگ ذیل *HraiH صورت «NP rīdan/rī-» را در کنار بلوچی rit/rī(y)- و کردی rîtin می‌آورد و ویکی‌واژه زنجیرهٔ «فارسی میانه rīdan < ایرانی آغازین *HriHyátī < هندواروپایی *h₃riH-yé-ti «روان شدن»» را با هم‌ریشهٔ سنسکریت rī́yate می‌دهد. «ریم» از rēm فارسی میانه است (ē فارسی میانه در فارسی نو به ی کشیده بدل می‌شود، مانند šēr > شیر) و چونگ آن را در همین مدخل آورده: «NP rīm: چرک، ریم». «ریمن» همان rēman پهلوی «پلید» است (بیت منوچهری: «ریمنی» یعنی پلیدی) و «ریمه» مشتق ـه‌دار آن. یک نکته که نورایی نگفته: هرن (شمارهٔ ۶۴۳) هشدار می‌دهد که «ریمن» به معنی «فریبکار» از «ریو» می‌آید نه از «ریم». ادعای نورایی درست است.\",\n \"sources\": [W_RID, W_RIM],\n \"ref_check\": [\n  {\"ref\": \"HRN:142\", \"status\": \"supports\", \"note\": \"Horn no. 639, p.142: 'rīden \\\"kacken\\\", Praes. rīy-em, rīsten, rīm, rīme' — the headword lists rīm and rīme exactly as Nourai does; footnote 1 adds 'rēm, LW kurd. afγ. rīm \\\"Eiter\\\", bal. rēm \\\"Eiter\\\"'.\"},\n  {\"ref\": \"BQT:987,990\", \"status\": \"not_checked\", \"note\": \"the ریدن and ریم entries could not be located in the local Borhan-e Qate' OCR (vols. 1-2, no page tags, and the ریـ range OCRs very badly).\"}\n ],\n \"consulted\": [\n  {\"src\": \"CHEUNG\", \"where\": \"p.188 s.v. *HraiH\", \"stance\": \"supports\", \"note\": \"'*NWIR: NP rīdan/rī-, Bal. rit/rī(y)-, Kurd. rîtin ... NP rīm \\\"pus, matter, humour; dregs, dross (vel sim.)\\\"' — both of Nourai's words in one entry.\"},\n  {\"src\": \"PHD\", \"where\": \"p.71 s.v. rēm, rēman\", \"stance\": \"supports\", \"note\": \"'rēm ... dirt, filth, purulence' with the NP equivalent marked '~'.\"},\n  {\"src\": \"HRN\", \"where\": \"no. 639 and the caveat at no. 643, p.142\", \"stance\": \"partial\", \"note\": \"no.643 (rēw 'Betrug'): 'rēmen, rīmen \\\"betrügerisch\\\" ... so wird man es nicht zu phlv. rēman, np. rīm (oben No. 639) ziehen dürfen' — i.e. the deceit-sense of ریمن is a different word.\"},\n  {\"src\": \"Wiktionary\", \"where\": \"s.v. ریدن\", \"stance\": \"supports\", \"note\": \"'From Middle Persian rīdan ... from Proto-Iranian *HriHyátī ... from Proto-Indo-European *h₃riH-yé-ti (\\\"to flow\\\"). Cognate with ... Sanskrit रीयते (rī́yate).'\"}\n ]\n})\n\nnodes.append({\n \"id\": 10,\n \"lang\": \"Avestan / Sanskrit\",\n \"words\": \"ari, arika, araeka\",\n \"verdict\": \"disputed\",\n \"derivation\": \"All three items are problematic, and the reference Nourai gives says so himself. (a) Sanskrit arí- 'stranger, enemy' — Walde-Pokorny I 136, in the er- article that Nourai cites, writes: 'aber ári-, arí- \\\"Feind\\\" ist wegen seines viel weitern Bedeutungsumfangs \\\"verlangend, begierig, anhänglich; feindselig, unfromm\\\" ... kaum nur in der Bed. \\\"Feind\\\" hierherzustellen', i.e. it refuses to file ari- under this root; Mayrhofer likewise links arí- with the arya-/ā́rya- word-family, not with *h₃er-. (b) arika- is Old Persian arīka- 'evil, faithless' (DB 1.22, 1.33, 4.63), and Kent p.176 derives it from *aŋra- 'hostile' (GAv. aŋra-, the Ahriman word) to the Proto-Aryan root *ans-, adding explicitly 'not to Skt. ari- \\\"enemy\\\"'; Walde-Pokorny I 135 files it under exactly that root *ens- ('Vgl. ap. arika- \\\"feindlich gesinnt\\\" (*ahrika)'). (c) araēka- is not an Avestan word for 'enemy' at all: Bartholomae's only headword is '• j. araēka- Adj. — ? —, Bez. einer Ameisenart' (Vd. 14.5, in the list of ants), meaning unknown. So the node collects one word whose root is disputed, one that belongs to a different root, and one that means something else entirely.\",\n \"derivation_fa\": \"هر سه واژهٔ این گره مسئله‌دار است و منبعی که خودِ نورایی آورده همین را می‌گوید. یکم، سنسکریت arí- «بیگانه، دشمن»: والده-پوکورنی جلد ۱ صفحهٔ ۱۳۶ در همان مدخل er- می‌نویسد که این واژه به سبب دامنهٔ معنایی بسیار گسترده‌ترش («خواهان، آزمند، وابسته؛ دشمنانه، بی‌دین») «به‌سختی می‌توان آن را تنها به معنی دشمن این‌جا نهاد». دوم، arika همان arīka- پارسی باستان «بدکنش، بی‌وفا» (بیستون ۱٫۲۲) است و کنت آن را از *aŋra- «دشمن» (همان واژهٔ اهریمن) از ریشهٔ *ans- می‌گیرد و صریحاً می‌افزاید «نه از سنسکریت ari». سوم، araēka- در اوستا اصلاً به معنی دشمن نیست؛ بارتولومه تنها مدخل آن را چنین می‌آورد: «araēka- صفت ـ ؟ ـ نام گونه‌ای مورچه» (وندیداد ۱۴٫۵). پس پژوهش امروزی این گره را رد می‌کند.\",\n \"sources\": [POKW],\n \"ref_check\": [\n  {\"ref\": \"WLD1:136\", \"status\": \"contradicts\", \"note\": \"Walde-Pokorny, Vergleichendes Wörterbuch I 136 (WLD_Bd1_pages.txt line 12312, under the running header '136 er-' at line 12242): 'aber ári-, arí- \\\"Feind\\\" (Lit. bei Bois. u. ἔρις) ist wegen seines viel weitern Bedeutungsumfangs \\\"verlangend, begierig, anhänglich; feindselig, unfromm\\\" (s. Uhlenbeck Ai. Wb.) kaum nur in der Bed. \\\"Feind\\\" hierherzustellen (Uhlenbeck verbindet es mit got. aljan \\\"Eifer\\\")'. The very page cited rejects the derivation. On p.135 the same book files ap. arika- 'feindlich gesinnt' (*ahrika) under *ens-, not under er-.\"},\n  {\"ref\": \"AEF:20\", \"status\": \"not_checked\", \"note\": \"Khaleqi Motlaq, Asās-e Ešteqāq-e Fārsi (the Persian translation of Horn/Hübschmann) is not available online or on disk; refs_online.json records it as catalogue-only.\"}\n ],\n \"consulted\": [\n  {\"src\": \"WLD\", \"where\": \"Bd. I 135-136\", \"stance\": \"contradicts\", \"note\": \"see ref_check.\"},\n  {\"src\": \"KNT\", \"where\": \"p.176 s.v. arika- (KNT.txt line 5050)\", \"stance\": \"contradicts\", \"note\": \"'arika- adj. \\\"evil, faithless\\\": deriv. of *aṣra-, GAv. aŋra-, LAv. aŋra- \\\"hostile, enemy\\\", to pAr. root *ans- ... not to Skt. ari- \\\"enemy\\\" (MB Gr. §273), nor to Skt. alīka-.'\"},\n  {\"src\": \"BRT\", \"where\": \"col. 185 s.v. araēka- (BRT.txt line 5285)\", \"stance\": \"contradicts\", \"note\": \"'• j. araēka- Adj. — ? —, Bez. einer Ameisenart: maoirinąm araēkanąm kutakanąm duždaēninām V. 14.5' — a kind of ant, not 'enemy'.\"},\n  {\"src\": \"POK\", \"where\": \"pp.326-332 (er-3)\", \"stance\": \"silent\", \"note\": \"Pokorny's er-3 article does not mention ari-, arika- or araēka- at all.\"}\n ]\n})\n\nnodes.append({\n \"id\": 11,\n \"lang\": \"Persian\",\n \"words\": \"ârîğ «آریغ ، أَریغ»; rîğ «ریغ»\",\n \"verdict\": \"plausible\",\n \"derivation\": \"The Persian words are real and correctly glossed. Borhan-e Qate': 'آریغ ... کینه و عداوت باشد و سردی و نفرتی را نیز گویند که از شخصی [در دل باشد]', and Mo'in's dictionary has 'آریغ: کراهت، نفرت، کینه' and 'ریغ [= آریغ]: کینه، عداوت، نفرت'; ریغ is simply آریغ with loss of the prothetic/initial ā- (the same alternation as آهو/هو type doublets), and Nourai's spelling variant أَریغ is the Arabic-script hamza writing of the same word. The derivation from Old Persian arīka- is not Nourai's invention: Mo'in's own etymological footnote to the آریغ entry says 'در پارسی باستان (کتیبهٔ بیستون ... بند ۱۲) arīka از ریشهٔ ari بمعنی دشمن (Bartholomae ...)', and cites Khosravānī's line 'کآریغ ز من به دل گرفته'. So BQT:33 supports Nourai exactly. What keeps this from 'confirmed' is the parent node: the Old Persian etymon arīka- itself is now referred to *aŋra- (Kent, Walde-Pokorny), so the Persian word may well go back to arīka- while arīka- does not go back to Er 1. Nourai's added gloss 'dung' for ریغ belongs to a different homonym (ریغ 'sand, gravel', Horn no.642 rēg, and the colloquial ریغ 'filth' of Mo'in), not to this word.\",\n \"derivation_fa\": \"خودِ واژه‌های فارسی درست‌اند. برهان قاطع: «آریغ ... کینه و عداوت باشد و سردی و نفرتی را نیز گویند»؛ فرهنگ معین: «آریغ: کراهت، نفرت، کینه» و «ریغ [= آریغ]: کینه، عداوت، نفرت». «ریغ» همان «آریغ» است با افتادن الف آغازین، و «أَریغ» تنها گونهٔ نگارشی است. اشتقاق از arīka پارسی باستان از خودِ معین است: حاشیهٔ او بر مدخل «آریغ» می‌نویسد «در پارسی باستان (کتیبهٔ بیستون، بند ۱۲) arīka از ریشهٔ ari بمعنی دشمن (بارتولومه)» و بیت خسروانی را گواه می‌آورد. پس ارجاع BQT:33 دقیقاً پشتیبان نورایی است. آنچه این گره را از «درست» به «با احتیاط پذیرفتنی» می‌کشاند گرهِ بالاست: امروزه خودِ arīka- را به *aŋra- می‌برند نه به ریشهٔ Er. افزودهٔ «سرگین» برای «ریغ» هم به هم‌آوای دیگری بازمی‌گردد نه به این واژه.\",\n \"sources\": [],\n \"ref_check\": [\n  {\"ref\": \"BQT:33\", \"status\": \"supports\", \"note\": \"Borhan-e Qate' s.v. آریغ (BQT_v1_pages.txt lines 7459-7466): entry 'آریغ ـ بکسر اول و سکون تحتانی و غین نقطه‌دار. کینه و عداوت باشد و سردی و نفرتی را نیز گویند که از شخصی ...' plus Mo'in's footnote 'در پارسی باستان (کتیبهٔ بیستون، متون ... بند ۱۲) arīka از ریشهٔ ari بمعنی دشمن ... این لغت در فرهنگ اسدی چاپ تهران ص ۲۳۸ و نیز موضع دیگر برهان بخلط «آزیغ» آمده. خسروانی شاعر گوید: کآریغ ز من بدل گرفته'. Exactly Nourai's arrow. (Page number itself not verifiable: the local OCR of vol.1 carries no page tags.)\"},\n  {\"ref\": \"AEF:20,21\", \"status\": \"not_checked\", \"note\": \"Asās-e Ešteqāq-e Fārsi is not available online or on disk.\"}\n ],\n \"consulted\": [\n  {\"src\": \"MON\", \"where\": \"s.v. آریغ and ریغ (MON_part1.txt lines 2779, 69820)\", \"stance\": \"supports\", \"note\": \"'آریغ: [دشمن] کراهت، نفرت، کینه. — این کلمه بصورت «آزیغ» تحریف شده'; 'ریغ: [= آریغ] کینه، عداوت، نفرت'. Mo'in also has a separate 'ریغ: (عم.) پلیدی، گه' — the 'dung' sense is a different, colloquial word.\"},\n  {\"src\": \"BQT\", \"where\": \"s.v. آریغ with Mo'in's footnote\", \"stance\": \"supports\", \"note\": \"see ref_check.\"},\n  {\"src\": \"KNT\", \"where\": \"p.176 s.v. arika-\", \"stance\": \"contradicts\", \"note\": \"the Old Persian etymon that Mo'in and Nourai use is itself derived by Kent from *aŋra-, 'not to Skt. ari- \\\"enemy\\\"'.\"}\n ]\n})\n\nnodes.append({\n \"id\": 12,\n \"lang\": \"Avestan\",\n \"words\": \"arati; aranu, ham-aranu; ham-ara, ham-aratha; râna 1; artha\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Every item of this node stands, word for word, on Pokorny pp.327-328, the range Nourai cites. 'arati' is Av. -arəti- 'energy' (Pokorny: 'ai. r̥tí-, r̥̄tí- f. \\\"Angriff, Streit\\\", av. -arəti- \\\"Energie\\\"'), an abstract in -ti- to the root. 'aranu' is Av. arənu- m. 'fight, contest' ('Letzteres ist sicher für: av. arənu- m. \\\"Kampf, Wettkampf\\\" (: ahd. ernust)'), and ham-arənu- is the same with ham- 'together': OP ham-arana- n. 'hostile encounter, battle' is the word used throughout Bīsutūn (hamaranam akunavam 'I did battle'), and Bartholomae's own note there reads 'Zum V. ar-. — ai. samara- m. \\\"Kampf\\\". Vgl. hamarana- und hamarəθa-'. 'ham-ara, ham-aratha' are Av. hamara- and hamarəθa- m. 'adversary, rival'. 'râna 1' is Av. rāna-, rąna- m. 'fighter, combatant' (beside rəna- n. 'battle'), from the thematic root form (e)rə-. 'artha' is Sanskrit ártha- n. 'affair, matter, property' — the Avestan equivalent is arəθa- n. 'thing, affair, litigation', so the language label is loose here (Nourai copies Pokorny's paired citation), but the etymology, '*wozu man gelangt' = 'that which one arrives at', is Pokorny's own. The two cross-references to Sem 1 (ham- < *sem- 'one, together') are correct.\",\n \"derivation_fa\": \"همهٔ واژه‌های این گره واژه‌به‌واژه در صفحات ۳۲۷ و ۳۲۸ پوکورنی، یعنی همان محدوده‌ای که نورایی ارجاع داده، آمده‌اند. «arati» همان -arəti- اوستایی «نیرو، تکاپو» است (اسم مصدر با پسوند ti-). «aranu» همان arənu- «نبرد، پیکار» و «ham-aranu» ترکیب آن با پیشوند ham- «با هم» است؛ صورت پارسی باستان hamarana- «رویارویی خصمانه، نبرد» واژهٔ رایج کتیبهٔ بیستون است (hamaranam akunavam «نبرد کردم») و بارتولومه خود در همان‌جا می‌نویسد: «به فعل ar-؛ سنسکریت samara- «نبرد»». «ham-ara» و «ham-aratha» همان hamara- و hamarəθa- «حریف، دشمن»اند. «rāna» همان rāna-/rąna- «جنگاور» است. «artha» اما سنسکریت است نه اوستایی (اوستایی آن arəθa- «کار، دعوی» است)؛ نورایی برچسب زبانی را از جفت‌نویسیِ پوکورنی برداشته است. ارجاع‌های Sem 1 نیز درست‌اند. ادعای نورایی درست است.\",\n \"sources\": [POKW],\n \"ref_check\": [\n  {\"ref\": \"POK:327-331\", \"status\": \"supports\", \"note\": \"Pokorny IEW p.327-328 (POK_01.txt leaf 339): 'ai. sam-ará- m., sam-áraṇa- n. \\\"Kampf, Wettstreit\\\", av. ham-arəna-, apers. ham-arana- n. \\\"feindliches Zusammentreffen, Kampf\\\", av. hamara- m. (und mit th-Formans hamarəθa- m.) \\\"Gegner, Widersacher\\\"; ... ai. ártha- n. m. \\\"(*wozu man gelangt)\\\" \\\"Angelegenheit, Sache\\\", av. arəθa- n. \\\"Sache, Angelegenheit, Obliegenheit, Rechtsstreit\\\"; ai. r̥tí-, r̥̄tí- f. \\\"Angriff, Streit\\\", av. -arəti- \\\"Energie\\\"; ... av. arənu- m. \\\"Kampf, Wettkampf\\\" (: ahd. ernust); von der themat. Wurzelf. (e)rə- ... = av. rəna- n. \\\"Treffen, Kampf, Streit\\\"; av. rāna-, rąna- m. \\\"Streiter, Kämpfer\\\"'. Every word of the node is there.\"}\n ],\n \"consulted\": [\n  {\"src\": \"POK\", \"where\": \"pp.327-328\", \"stance\": \"supports\", \"note\": \"see ref_check.\"},\n  {\"src\": \"WLD\", \"where\": \"Bd. I 136-137\", \"stance\": \"supports\", \"note\": \"the same list in the parent work: 'ai. ártha- n. m. \\\"(*wozu man gelangt)\\\" ... av. arθa- n. \\\"Sache, Angelegenheit, Obliegenheit, Rechtsstreit\\\"'; 'ai. r̥ti-, r̥̄ti- f. \\\"Angriff, Streit\\\", av. -arəti- \\\"Energie\\\"'; 'av. arənu- m. \\\"Kampf, Wettkampf\\\" (: ahd. ernust)' (WLD_Bd1_pages.txt lines 12300-12320).\"},\n  {\"src\": \"BRT\", \"where\": \"s.v. OP hamarana- and cartanaiy (BRT.txt lines 29421, 11238)\", \"stance\": \"supports\", \"note\": \"'Zum V. ar-. — ai. samara- m. \\\"Kampf\\\". Vgl. hamarana- und hamarəθa-'; 'hamaranam cartanaiy \\\"praelium facere\\\"' with the Bīsutūn citations.\"},\n  {\"src\": \"KNT\", \"where\": \"p.170 s.v. arta-\", \"stance\": \"supports\", \"note\": \"'arta- sb. \\\"Law, Justice\\\" ... ptc. to ar- as sb., Av. aša- and arəta-, Skt. r̥tá- \\\"cosmic order\\\", Lt. ortus \\\"risen, originated\\\", pIE *r̥to-' — the same root, same formation type.\"}\n ]\n})\n\nnodes.append({\n \"id\": 13,\n \"lang\": \"Latin\",\n \"words\": \"oriri; rivus\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Latin orior, orīrī, ortus sum 'to rise, spring up, be born' is the yé-present *h₃r̥-yé-tor of this root; its participle ortus is the exact equal of Sanskrit r̥tá-, and the derived noun orīgō 'source, beginning' is built on it. Watkins files it under er-1 'to move, set in motion' as 'suffixed form *or-yo- in Latin oriri, to arise, appear, be born' with the tag [Pok. 3. er- 326] — i.e. Nourai's 'AHD' citation is precise. Latin rīvus 'brook' is *rei-wo-s from the erei-/reiə- sub-basis of the same root (Pokorny p.330-331: 'lat. orior, origo s. oben; rīvus (*rei-uo-s) \\\"Bach\\\"'), and Watkins likewise puts it under rei-3 'to flow, run', again tagged [Pok. 3. er- 326]. So both Latin words really do belong to one and the same Pokorny lemma, which is exactly what the chart claims by putting them in one box.\",\n \"derivation_fa\": \"لاتینی orior، orīrī، ortus «برخاستن، برآمدن، زاده شدن» همان حالِ *h₃r̥-yé-tor این ریشه است؛ صفت مفعولی آن ortus برابر دقیق r̥tá- سنسکریت است و اسم orīgō «سرچشمه» از آن ساخته شده. واتکینز آن را ذیل er-1 «به جنبش درآوردن» می‌آورد با یادداشت [Pok. 3. er- 326]، پس ارجاع «AHD» نورایی دقیق است. لاتینی rīvus «جوی» نیز *rei-wo-s از زیرپایهٔ erei-/reiə- همین ریشه است؛ پوکورنی در صفحهٔ ۳۳۰–۳۳۱ می‌نویسد: «lat. orior، origo ... rīvus (*rei-uo-s) «جوی»». واتکینز هم آن را ذیل rei-3 «روان شدن» با همان یادداشت [Pok. 3. er- 326] می‌گذارد. پس هر دو واژه به یک مدخل پوکورنی می‌رسند و ادعای نورایی درست است.\",\n \"sources\": [E_ORI],\n \"ref_check\": [\n  {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins (AHD_watkins1985.txt line 447): 'er-1. To move, set in motion. ... 3. Suffixed form *or-yo- in Latin oriri, to arise, appear, be born: ORIENT, ORIGIN, ORIGINAL; ABORT. [Pok. 3. er- 326; ergh- 339.]'; and line 895: 'rei-3. To flow, run. ... 3. Suffixed form *rei-wo- in Latin rivus, stream: RIVAL, RIVULET; DERIVE. [Pok. 3. er- 326.]' — both Latin words assigned to Pokorny's er-3, exactly as the chart draws them.\"}\n ],\n \"consulted\": [\n  {\"src\": \"AHD\", \"where\": \"s.v. er-1 and rei-3\", \"stance\": \"supports\", \"note\": \"see ref_check.\"},\n  {\"src\": \"POK\", \"where\": \"pp.330-331 (POK_01.txt leaves 343-344)\", \"stance\": \"supports\", \"note\": \"'lat. orior, -īrī, ortus sum \\\"to rise; to spring up, be born\\\" (ortus = ai. r̥tá-) ... origo \\\"origin, source, beginning\\\"'; 'rīvus (*rei-uo-s) \\\"Bach\\\"'.\"},\n  {\"src\": \"SKT\", \"where\": \"s.v. Orient (SKT.txt line 12867)\", \"stance\": \"supports\", \"note\": \"'Orient, eastern. (F.-L.) F. orient — L. orient-, stem of oriens, rising, the east; orig. pres. pt. of oriri, to rise, begin. + Skt. r̥, to rise. (√AR.)'\"},\n  {\"src\": \"Etymonline\", \"where\": \"s.v. origin / abort\", \"stance\": \"supports\", \"note\": \"'from Latin ... oriri \\\"appear, be born, arise\\\", from PIE *h₃eri- \\\"to rise\\\" ... [Watkins, contra de Vaan, etc., derives the second element from a suffixed form of PIE root *er- (1) \\\"move, set in motion.\\\"]'\"}\n ]\n})\n\nnodes.append({\n \"id\": 14,\n \"lang\": \"English\",\n \"words\": \"orient, origin, abort, rival, derive\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"All five are Latin loans into English through French and all five are covered by the two Watkins entries that carry Nourai's own tag [Pok. 3. er- 326]. Orient (14c., Old French orient < Latin oriēns, -entis 'the rising sun, the east', present participle of orīrī), origin (15c., Latin orīgō, -inis 'source', from orīrī) and abort (1570s, Latin abortus, past participle of aborīrī 'to miscarry', ab- 'amiss' + orīrī) all belong to orīrī of node #13; Watkins lists them together as 'ORIENT, ORIGIN, ORIGINAL; ABORT'. Rival (1570s) is Latin rīvālis 'one using the same brook', a derivative of rīvus; derive is Old French deriver < Latin dērīvāre 'to lead off water, draw off', literally 'from the stream' (dē- + rīvus). Watkins gives 'RIVAL, RIVULET; DERIVE' under rei-3. The node's arrow, Latin → English, is a simple and uncontroversial borrowing chain.\",\n \"derivation_fa\": \"هر پنج واژه وام‌واژه‌های لاتینی‌اند که از راه فرانسه به انگلیسی رسیده‌اند و هر پنج در همان دو مدخل واتکینز آمده‌اند که یادداشت [Pok. 3. er- 326] دارند. orient (سدهٔ ۱۴، از فرانسهٔ کهن، از لاتینی oriēns «خورشیدِ برآینده، خاور»، اسم فاعل orīrī)، origin (سدهٔ ۱۵، از لاتینی orīgō «سرچشمه») و abort (۱۵۷۰، از لاتینی abortus، صفت مفعولی aborīrī «سِقط شدن» از ab- + orīrī) همه به orīrī گرهِ پیشین بازمی‌گردند. rival از لاتینی rīvālis «هم‌جوی، کسی که از یک جوی آب می‌برد» و derive از لاتینی dērīvāre «آب را از جوی بیرون بردن» است، هر دو از rīvus. ادعای نورایی درست است.\",\n \"sources\": [E_RIV, E_ORI],\n \"ref_check\": [\n  {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the node carries no references of its own in the book; the parent Latin box cites AHD, which covers all five words (see node #13).\"}\n ],\n \"consulted\": [\n  {\"src\": \"AHD\", \"where\": \"s.v. er-1 and rei-3 (AHD_watkins1985.txt lines 447, 895)\", \"stance\": \"supports\", \"note\": \"'ORIENT, ORIGIN, ORIGINAL; ABORT' under er-1; 'RIVAL, RIVULET; DERIVE' under rei-3.\"},\n  {\"src\": \"SKT\", \"where\": \"s.v. Orient (SKT.txt line 12867)\", \"stance\": \"supports\", \"note\": \"'F. orient — L. orient-, stem of oriens, rising ... pres. pt. of oriri, to rise, begin. + Skt. r̥, to rise. (√AR.)'\"},\n  {\"src\": \"Etymonline\", \"where\": \"s.v. rival, origin/abort\", \"stance\": \"supports\", \"note\": \"'rival ... from Latin rivalis \\\"a rival, adversary in love; neighbor,\\\" originally, \\\"of the same brook,\\\" from rivus \\\"brook\\\" (from PIE root *rei- \\\"to run, flow\\\")'.\"}\n ]\n})\n\nnodes.append({\n \"id\": 15,\n \"lang\": \"Germanic\",\n \"words\": \"ri-nwan : to run; art : to be\",\n \"verdict\": \"plausible\",\n \"derivation\": \"The first half is solid: Watkins reconstructs 'suffixed zero-grade form *ri-nu- in Germanic *ri-nw-an, whence *rinnan, to run' — Nourai's odd-looking 'ri-nwan' is a verbatim copy of Watkins' notation — with Gothic rinnan, rann 'to run', urrinnan 'to rise (of the sun)', Old Norse rinna, OHG/OS rinnan, OE rinnan and iernan; Pokorny p.328-329 has the same, 'got. rinnan, rann \\\"rennen, laufen\\\" (*re-nu-ō), urrinnan \\\"aufgehen, von der Sonne\\\"'. The second half is a genuine but contested hypothesis. Watkins' er-1 opens '1. Probably Germanic *ar-, *or-, *art(a), to be, exist, in Old English eart and aron, second person singular and plural present of bēon, to be: ARE, ART' — note his 'probably'. Wiktionary sets the state of the question out: the Anglian forms earun/earon (and Old Swedish ær-) 'could reflect Proto-Germanic preterite-present *ōr ~ *arum, from Proto-Indo-European *h₃e-h₃ór-h₂e (\\\"I have risen\\\", perfect)' (Ringe 2006:72, Seebold), 'since they are not the expected outcomes of the Proto-Germanic forms of *wesaną in *iz-'; but the competing and commoner view keeps them with *h₁es- 'to be' as irregular alterations. So Nourai's box faithfully reports AHD, and AHD's own hedge is what keeps this node short of 'confirmed'.\",\n \"derivation_fa\": \"نیمهٔ نخست استوار است: واتکینز صورت «*ri-nu- در ژرمنی *ri-nw-an > *rinnan «دویدن»» را بازسازی می‌کند — نگارش عجیبِ «ri-nwan» نزد نورایی عیناً از واتکینز گرفته شده — با گواه‌های گوتی rinnan «دویدن»، urrinnan «برآمدن (خورشید)»، نورس کهن rinna و انگلیسی کهن rinnan/iernan؛ پوکورنی نیز در صفحهٔ ۳۲۸–۳۲۹ همین را دارد. اما نیمهٔ دوم فرضیه‌ای واقعی ولی محل بحث است: واتکینز ذیل er-1 می‌نویسد «احتمالاً ژرمنی *ar-, *or-, *art(a) «بودن» در انگلیسی کهن eart و aron» — با همان قید «احتمالاً». ویکی‌واژه وضع پژوهش را چنین می‌آورد: صورت‌های earun/earon «می‌توانند بازتاب ژرمنی آغازین *ōr ~ *arum از هندواروپایی *h₃e-h₃ór-h₂e «برخاسته‌ام» باشند» (رینگه ۲۰۰۶، زیبولد)، اما دیدگاه رایج‌تر آن‌ها را دگرگونی‌های بی‌قاعدهٔ *h₁es- «بودن» می‌داند. پس با احتیاط پذیرفتنی است.\",\n \"sources\": [W_ARE],\n \"ref_check\": [\n  {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins: 'rei-3. To flow, run. 1. Suffixed zero-grade form *ri-nu- in: a. Germanic *ri-nw-an, whence *rinnan, to run, in Old English rinnan ... RUN, RUNNEL. [Pok. 3. er- 326.]' and 'er-1 ... 1. Probably Germanic *ar-, *or-, *art(a), to be, exist, in Old English eart and aron ... ARE, ART. [Pok. 3. er- 326]'. Both forms are Watkins' own; the 'art(a)' half is explicitly hedged with 'Probably'.\"}\n ],\n \"consulted\": [\n  {\"src\": \"AHD\", \"where\": \"s.v. er-1 and rei-3\", \"stance\": \"supports\", \"note\": \"see ref_check.\"},\n  {\"src\": \"POK\", \"where\": \"pp.328-329 (POK_01.txt leaf 341)\", \"stance\": \"partial\", \"note\": \"'got. rinnan, rann \\\"rennen, laufen\\\" (*re-nu-ō), urrinnan \\\"aufgehen, von der Sonne\\\", aisl. rinna \\\"fliessen, rennen\\\", ahd. as. rinnan ... ags. rinnan und iernan, arn' — Pokorny supports *ri-nw-, but says nothing about OE eart/aron.\"},\n  {\"src\": \"Wiktionary\", \"where\": \"s.v. are (etymology 2)\", \"stance\": \"partial\", \"note\": \"'Further etymology controversial: The English forms, as well as the Old Swedish forms in ær-, could reflect Proto-Germanic preterite-present *ōr ~ *arum, from Proto-Indo-European *h₃e-h₃ór-h₂e (\\\"I have risen\\\", perfect) [Ringe 2006 p.72] ... Since they are not the expected outcomes of the Proto-Germanic forms of *wesaną in *iz-, they would have to be irregular alterations.'\"}\n ]\n})\n\nnodes.append({\n \"id\": 16,\n \"lang\": \"English\",\n \"words\": \"run, are\",\n \"verdict\": \"plausible\",\n \"derivation\": \"Run continues Old English rinnan / iernan, arn (with the well-known metathesis of r and the vowel: *rinnan > iernan > modern run), reinforced by Old Norse rinna; Watkins gives 'RUN, RUNNEL' from Germanic *ri-nw-an under rei-3, tagged [Pok. 3. er- 326] — so for 'run' the chain root → Germanic → English is straightforward and confirmed. Are is Middle English aren, Old English (Anglian) earun/earon, plural of 'to be', which displaced Old English sind and bēoþ; art is its 2sg. Watkins takes both back to a Germanic *ar-/*or-/*art(a) belonging to this root, and Ringe reconstructs a preterite-present *ōr ~ *arum from the PIE perfect *h₃e-h₃ór-h₂e 'I have risen' — a real hypothesis, and the only one that explains why the forms are not the expected reflexes of *wesaną (*iz-). But most handbooks still class earun/earon with *h₁es- 'to be'. The node therefore mixes one certain item with one that is genuinely open, which is why it is graded plausible rather than confirmed.\",\n \"derivation_fa\": \"«run» دنبالهٔ rinnan / iernan, arn انگلیسی کهن است (با قلبِ شناختهٔ r: *rinnan > iernan > run امروزی) که نورس کهن rinna نیز آن را تقویت کرده؛ واتکینز «RUN, RUNNEL» را از ژرمنی *ri-nw-an ذیل rei-3 با یادداشت [Pok. 3. er- 326] می‌آورد، پس این نیمه قطعی است. «are» از انگلیسی میانهٔ aren و انگلیسی کهن (انگلی) earun/earon است که جای sind و bēoþ را گرفت، و «art» صورت دوم‌شخص مفرد آن است. واتکینز هر دو را به ژرمنی *ar-/*or-/*art(a) از همین ریشه می‌برد و رینگه یک ماضی‌ـ‌حال *ōr ~ *arum از کاملِ هندواروپاییِ *h₃e-h₃ór-h₂e «برخاسته‌ام» بازمی‌سازد؛ فرضیه‌ای جدی، ولی بیشتر کتاب‌های مرجع هنوز آن صورت‌ها را به *h₁es- «بودن» می‌بندند. از این‌رو این گره با احتیاط پذیرفتنی است.\",\n \"sources\": [W_ARE],\n \"ref_check\": [\n  {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the node carries no references of its own; the parent Germanic box cites AHD, which supplies both English words (see node #15).\"}\n ],\n \"consulted\": [\n  {\"src\": \"AHD\", \"where\": \"s.v. rei-3 and er-1 (AHD_watkins1985.txt lines 895, 447)\", \"stance\": \"supports\", \"note\": \"'RUN, RUNNEL' under rei-3; 'ARE, ART' under er-1 with 'Probably'.\"},\n  {\"src\": \"POK\", \"where\": \"pp.328-329\", \"stance\": \"partial\", \"note\": \"supports Germanic *rinnan (> run); silent on OE eart/aron.\"},\n  {\"src\": \"Wiktionary\", \"where\": \"s.v. are\", \"stance\": \"partial\", \"note\": \"'Further etymology controversial ... could reflect Proto-Germanic preterite-present *ōr ~ *arum, from Proto-Indo-European *h₃e-h₃ór-h₂e (\\\"I have risen\\\", perfect).'\"}\n ]\n})\n\nentry = {\n \"entry\": 0,\n \"root\": \"Er 1, Or\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *h₃er- 'to move, stir; to rise, spring up' (Pokorny 326-332 er-3 : or- : r-; LIV² 299)\",\n \"note\": \"The root box is right in all three respects. The reconstruction is real and standard: Wiktionary's *h₃er- '(perfective) to move, to stir; to rise, to spring', with the extensions *h₃er-dʰ-, *h₃r-ey-H- and *h₃r-ew- that this very page uses for its three main branches; Pokorny's lemma is '3. er- : or- : r-, ursprünglich athematische Wurzel mit terminativem Aspekt: \\\"sich in Bewegung setzen, erregen (auch seelisch, ärgern, reizen); in die Höhe bringen\\\"' at pp.326-332, and Watkins' equivalent is er-1 'to move, set in motion' [Pok. 3. er- 326]. The label 'Indo-European' is correct, the two variant spellings 'Er / Or' are Pokorny's own e/o ablaut pair (er- : or- : r-), and the gloss 'to set in motion, excite' translates Pokorny's German almost word for word. The page number POK:327 is also exact: it is the page on which the lemma's Material section opens, with Av. ar- and OP rasatiy. Nourai's 'Er 1' numbering distinguishes this root from his 'Er 2' etc., matching Pokorny's own 1.-5. er- homonyms. — Cross-cutting comment: of the sixteen nodes, twelve are sound; the disputed ones are #5 (Skt. rádati, which modern work assigns to *reh₁d-, Pokorny 854) and #10 (ari-/arika-/araēka-, where the very page Nourai cites, Walde-Pokorny I 136, refuses the connection and Kent refers OP arīka- to *aŋra-); #7 folds in an unrelated verb (Av. raēk- 'linquere', PIE *leykʷ-); #3 misprints Av. auruna- as 'auruma'; #11 and #15/#16 are hypotheses that are held by some but not all. The Persian branch (#1-#2, #3-#4, #7-#9) is the strongest part of the page and is confirmed at every step by Horn, MacKenzie, Nyberg, Cheung, Buck and Mo'in.\",\n \"note_fa\": \"جعبهٔ ریشه از هر سه جهت درست است. بازساخت واقعی و متعارف است: ویکی‌واژه *h₃er- «به جنبش درآمدن، برخاستن» را با گسترش‌های *h₃er-dʰ-، *h₃r-ey-H- و *h₃r-ew- می‌آورد — همان سه شاخه‌ای که این صفحه بر آن‌ها بنا شده است. مدخل پوکورنی «3. er- : or- : r-، ریشهٔ آغازاً بی‌میانوندی با نمود پایانی: «به جنبش درآوردن، برانگیختن (نیز از نظر روحی)؛ بالا بردن»» در صفحات ۳۲۶ تا ۳۳۲ است و برابرِ واتکینز er-1 «به جنبش درآوردن» با یادداشت [Pok. 3. er- 326]. برچسب «هندواروپایی» درست است، دو گونهٔ «Er / Or» همان جفت آواگردانِ e/o نزد پوکورنی است و معنای داده‌شده تقریباً ترجمهٔ لفظیِ آلمانیِ پوکورنی است. شمارهٔ صفحهٔ POK:327 نیز دقیق است: همان صفحه‌ای که بخش گواه‌ها با اوستایی ar- و پارسی باستان rasatiy آغاز می‌شود. — نکتهٔ فراگیر: از شانزده گرهِ این صفحه دوازده گره استوارند؛ دو گره رد می‌شود: گرهٔ ۵ (سنسکریت rádati که امروزه به *reh₁d- برده می‌شود، پوکورنی ۸۵۴) و گرهٔ ۱۰ (ari/arika/araēka که همان صفحهٔ والده-پوکورنی که نورایی ارجاع داده این پیوند را رد می‌کند). گرهٔ ۷ فعلِ بی‌ربطِ raēk- «وانهادن» را در خود جای داده، گرهٔ ۳ صورت auruna- را «auruma» چاپ کرده، و گره‌های ۱۱ و ۱۵ و ۱۶ فرضیه‌هایی‌اند که همهٔ پژوهشگران نپذیرفته‌اند. شاخهٔ فارسی صفحه (گره‌های ۱–۲، ۳–۴ و ۷–۹) استوارترین بخش آن است و هرن، مکنزی، نیبرگ، چونگ، باک و معین گام‌به‌گام آن را تأیید می‌کنند.\",\n \"sources\": [POKW],\n \"ref_check\": [\n  {\"ref\": \"POK:327\", \"status\": \"supports\", \"note\": \"Pokorny IEW (POK_01.txt leaf 338, the page whose printed number '327' stands in this leaf): '3. er- : or- : r-, ursprünglich athematische Wurzel mit terminativem Aspekt: \\\"sich in Bewegung setzen, erregen (auch seelisch, ärgern, reizen); in die Höhe bringen (Erhebung, hochwachsen), z. T. auch von Bewegung nach abwärts\\\"; Basenformen er-, ere-, erə-(?), erei-, ereu- ...' The lemma range printed at the end of the article is 'Page(s): 326-332', and 327 is where the Material begins.\"}\n ],\n \"consulted\": [\n  {\"src\": \"POK\", \"where\": \"pp.326-332, lemma '3. er- : or- : r-'\", \"stance\": \"supports\", \"note\": \"see ref_check; the article's own reference line is 'WP. I 136 ff., ... WH. I 64 f., 416 f.'\"},\n  {\"src\": \"WLD\", \"where\": \"Bd. I 136 ff. (WLD_Bd1_pages.txt from line 12242, header '136 er-')\", \"stance\": \"supports\", \"note\": \"the parent article of Pokorny's lemma, same root, same glosses; it is also the page Nourai cites for node #10, where it contradicts him.\"},\n  {\"src\": \"AHD\", \"where\": \"s.v. er-1 (AHD_watkins1985.txt line 447)\", \"stance\": \"supports\", \"note\": \"'er-1. To move, set in motion. ... [Pok. 3. er- 326; ergh- 339.]'\"},\n  {\"src\": \"CHEUNG\", \"where\": \"s.v. *Har¹ 'to go to(wards), reach'\", \"stance\": \"supports\", \"note\": \"the Iranian verb dictionary treats the whole Iranian branch of the root as one lemma, with Av. ar-, OP rs(s)a-, MP ras-, NP rasīdan.\"}\n ],\n \"nodes\": nodes\n}\n\nout = {\n \"pdf_page\": 156,\n \"book_page\": 126,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-05\",\n \"note\": \"Printed page checked against the PDF render (pdftoppm -f 156, copied to data/verification/sources/refs/ocr/BOOK/156.png): the extraction in data/extracted/batch/page-156.json is faithful to the book in every word, script form, gloss, reference string, verse and note. The one odd form on the page, 'auruma' in node #3, really is printed that way in the book, so it is Nourai's own misprint for Avestan auruna-, not a scan error. The page carries a single chart (PART 1 of root Er 1, Or) and one empty box beside node #12, which is empty in the book too.\",\n \"entries\": [entry]\n}\n\nwith open(\"/home/sfmqrb/git/rishe/data/verification/page-156.json\", \"w\", encoding=\"utf-8\") as f:\n    json.dump(out, f, ensure_ascii=False, indent=2)\n    f.write(\"\\n\")\nprint(\"written\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build156.py && python3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-156.json > /dev/null && echo \"JSON OK\" && python3 /home/sfmqrb/git/rishe/tools/verify_check.py 156",
 "description": "Build and validate page-156.json"
}
```


### [2026-09-05T20:53:32.336Z] TOOL RESULT

```
written
JSON OK
nodes verified: 16/16
node verdicts: {'confirmed': 9, 'transcription_suspect': 1, 'disputed': 2, 'plausible': 4}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 18, 'not_found': 2, 'partial': 3, 'not_checked': 12, 'contradicts': 1}
books consulted: {'supports': 44, 'contradicts': 5, 'partial': 7, 'silent': 1} | by book: {'POK': 9, 'CHEUNG': 6, 'BRT': 5, 'PHD': 5, 'HRN': 5, 'KNT': 4, 'Wiktionary': 4, 'AHD': 4, 'BQT': 3, 'NYB': 2, 'MON': 2, 'WLD': 2, 'SKT': 2, 'Etymonline': 2, 'SYN': 1, 'SNS': 1}
```


## [2026-09-05T20:53:53.662Z] AGENT

Done. `data/verification/page-156.json` written; `verify_check.py 156` reports **0 PROBLEM lines** (16/16 nodes).

**Page 156 (book p. 126) — root "Er 1, Or" (PIE *h₃er-), PART 1, 16 nodes**
- Root: **confirmed** (Pokorny er-3, pp. 326–332; POK:327 is the exact page where the Material opens with Av. *ar-* / OP *rasatiy*).
- Node verdicts: 9 confirmed · 4 plausible · 2 disputed · 1 transcription_suspect.
- Ref checks: 18 supports · 3 partial · 1 contradicts · 2 not_found · 12 not_checked (BQT vols. 1–2 OCR has no page tags; BQT vol. 4, IRN, FFD, AEF unavailable).

Flagged items:
- **disputed #5** — Skt. *rad, radati*: Pokorny p.330 does list it under er-3, but only as "weiter hierher **oder zu 5. er-**"; Cheung/LIV² 497 assign it to *\*HreHd-* (Pokorny **854**, Lat. *rōdō*). Wrong root-head; the #5→#6 arrow to Persian *randīdan* is fine.
- **disputed #10** — Av./Skt. *ari, arika, araeka*: the page Nourai cites, **WLD I 136, refuses the connection** ("kaum nur in der Bed. 'Feind' hierherzustellen"); Kent p.176 derives OP *arīka-* from *\*aŋra-* ("not to Skt. *ari-*"); Bartholomae's *araēka-* is "a kind of ant, meaning ?".
- **transcription_suspect #3** — "auruma : wildly" is not Avestan; correct form **auruna-** 'wild, savage' (BRT col. 197; Pokorny p.331 "vielleicht av. auruna-"). `error_in: "book"` — the printed page really shows *auruma*, so it is Nourai's misprint. Page PNG saved to `data/verification/sources/refs/ocr/BOOK/156.png`.
- **plausible #7** — "raec 1" is Av. *raēk-* 'linquere' (AiW col. 1487), from PIE *\*leykʷ-*, not this root; *rī-/raē-* half fully confirmed (Cheung *\*HraiH*, Buck §4.66, Horn 639).
- **plausible #11 / #15 / #16** — Persian *ārīγ/rīγ* rests on Mo'in's OP *arīka-* etymology (BQT:33 supports verbatim) but inherits #10's problem; English *are/art* from *\*h₃er-* is Watkins' hedged "Probably" (Ringe 2006 vs. the usual *\*h₁es-*).
- **BRT:368** (node #1) **not_found**: AiW col. 368 covers *iδa/it/indra-*, nothing relevant; BRT:184 supports fully.

**No extraction errors** — the JSON matches the printed page word for word (scripts, glosses, refs, both Ferdowsī verses, the Manūchehrī verse, and the empty box beside node #12).
