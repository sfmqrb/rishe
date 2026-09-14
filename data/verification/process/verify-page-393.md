# Verification process log — verify-page-393


## [2026-09-14T00:49:38.419Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 393 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-393.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-393.json. Write /home/sfmqrb/git/rishe/data/verification/page-393.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 393` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-14T00:49:39.520Z] AGENT

I'll start by reading the instructions.


## [2026-09-14T00:49:40.360Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-14T00:49:40.381Z] TOOL RESULT

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


## [2026-09-14T00:49:40.863Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-393.txt"
}
```


### [2026-09-14T00:49:40.888Z] TOOL RESULT

```
1	=== PDF page 393 (book page 363) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Per 1 : around, forward. Also see roots "Per 2", "Per 3" and "Per 4".  (refs POK:810)  PART 1
4	#1 (parent #0) [Avestan] refs=POK:244,810 | pairi, pari, parâ 3, para 3 : around, perimeter ; pairi-daeza : walled-in place, paradise ☞Dheigh ; pairi-vâra : sheltered from all around, a barn ☞Wer 3 ; pairi-vaz : fly around ☞Wegh ; pairi-šta : stand around, nurse ☞Stâ ; pairi-čayeiti : sort around, divider ☞Kwei 2
5	  #2 (parent #1) [Persian] refs=HRN:66; BQT:376-91,437 | pîrâmŭn «پیرامون» : perimeter | extra: پردیس ، فردوس ، پالیز ، جالیز
6	پروار ، پرواز
7	پرستیدن ، پرستار ، پرچین
8	  #3 (parent #1) [Greek] refs=AHD:950 | paradeisos : paradise
9	    #4 (parent #3) [English] refs=None | paradise
10	#5 (parent #0) [Avestan] refs=POK; HUB:39; HRN:68 | para-kan : spread around ☞Gwhen ; para-tab : shine forward ☞Tep ; para-tak : run around, to do ☞Teku 1
11	  #6 (parent #5) [Persian] refs=BQT; HUB:39; SNS:133 | parâkandan «پراکندن» : spread ; partow «پرتو» : beam of light ; pardâxtan «پرداختن» : to do | extra: پراگندن ، پراکن
12	#7 (parent #0) [Avestan] refs=POK; HUB:39; HRN:68 | par-šti : back (causing to stand up) ☞Stâ ; pari-bar, pari-bahr : carry around, develop ☞Bher 1 ; pairi-kara : go (draw) around, a compass ☞Kwer
13	  #8 (parent #7) [Persian] refs=BQT; HUB:39; SNS:133 | pošt «پشت» : back ; parvardan «پروردن» : develop ; pargâr «پرگار» : compass, fortune, necklace | NOTE: HUB:39 is not sure about the derivation of "pargâr"
14	#9 (parent #0) [Avestan] refs=HRN:184; BQT:1442-82 | fra 2, frank : forward ; fra-thang : pull forward (culture) ☞Ten 1 ; fra-stâ : stand (send) forward ☞Stâ ; fra-aiš, fraĕšta : sent forward (angel) ☞Stâ ; fra-var : protecting all around, Farvahar ☞Wer 3 ; fra-var-tinam : month of Farvahar
15	  #10 (parent #9) [Persian] refs=BQT:1446,1482 | farâ «فرا» : forward, more | extra: فراتر
16	فراگرفتن ، فراز ، فراسو ، فرهنگ
17	فرستادن ، فرشته
18	فروَهَر ، فروردین ، فردین
19	  #11 (parent #9) [Sogdian] refs=SOD:155 | frtr : more, better
20	#12 (parent #0) [Avestan] refs=HRN:184; BQT:1442-82 | fra-â-marz : one who forgives all ☞Mĕlg ; fara-mana : pre-evaluate, order ☞Me ; fra-dâta : promotion, call for help ; fra-jâma : end of going (destination) ☞Gwa ; fra-vaxš : call out to sell ☞Wekw
21	  #13 (parent #12) [Persian] refs=BQT:1482 |  | extra: فرامرز ، فرمان
22	فریاد ، فرجام
23	فروختن
24	
```


## [2026-09-14T00:49:43.701Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-393.json | head -200",
 "description": "Read source JSON for page 393"
}
```


### [2026-09-14T00:49:43.752Z] TOOL RESULT

```
{
  "pdf_page": 393,
  "book_page": 363,
  "entries": [
    {
      "part": 1,
      "root": {
        "name": "Per 1",
        "lang": "Indo-European",
        "refs": "POK:810",
        "gloss": "around, forward. Also see roots \"Per 2\", \"Per 3\" and \"Per 4\"."
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:244,810",
          "words": [
            {"translit": "pairi, pari, parâ 3, para 3", "gloss": "around, perimeter", "script": null},
            {"translit": "pairi-daeza", "gloss": "walled-in place, paradise", "script": null, "see": ["Dheigh"]},
            {"translit": "pairi-vâra", "gloss": "sheltered from all around, a barn", "script": null, "see": ["Wer 3"]},
            {"translit": "pairi-vaz", "gloss": "fly around", "script": null, "see": ["Wegh"]},
            {"translit": "pairi-šta", "gloss": "stand around, nurse", "script": null, "see": ["Stâ"]},
            {"translit": "pairi-čayeiti", "gloss": "sort around, divider", "script": null, "see": ["Kwei 2"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "HRN:66; BQT:376-91,437",
          "words": [
            {"translit": "pîrâmŭn", "gloss": "perimeter", "script": "پیرامون"}
          ],
          "script_extra": "پردیس ، فردوس ، پالیز ، جالیز\nپروار ، پرواز\nپرستیدن ، پرستار ، پرچین",
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 1,
          "lang": "Greek",
          "refs": "AHD:950",
          "words": [
            {"translit": "paradeisos", "gloss": "paradise", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "paradise", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK; HUB:39; HRN:68",
          "words": [
            {"translit": "para-kan", "gloss": "spread around", "script": null, "see": ["Gwhen"]},
            {"translit": "para-tab", "gloss": "shine forward", "script": null, "see": ["Tep"]},
            {"translit": "para-tak", "gloss": "run around, to do", "script": null, "see": ["Teku 1"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "Persian",
          "refs": "BQT; HUB:39; SNS:133",
          "words": [
            {"translit": "parâkandan", "gloss": "spread", "script": "پراکندن"},
            {"translit": "partow", "gloss": "beam of light", "script": "پرتو"},
            {"translit": "pardâxtan", "gloss": "to do", "script": "پرداختن"}
          ],
          "script_extra": "پراگندن ، پراکن",
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK; HUB:39; HRN:68",
          "words": [
            {"translit": "par-šti", "gloss": "back (causing to stand up)", "script": null, "see": ["Stâ"]},
            {"translit": "pari-bar, pari-bahr", "gloss": "carry around, develop", "script": null, "see": ["Bher 1"]},
            {"translit": "pairi-kara", "gloss": "go (draw) around, a compass", "script": null, "see": ["Kwer"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 7,
          "lang": "Persian",
          "refs": "BQT; HUB:39; SNS:133",
          "words": [
            {"translit": "pošt", "gloss": "back", "script": "پشت"},
            {"translit": "parvardan", "gloss": "develop", "script": "پروردن"},
            {"translit": "pargâr", "gloss": "compass, fortune, necklace", "script": "پرگار"}
          ],
          "script_extra": null,
          "note": "HUB:39 is not sure about the derivation of \"pargâr\"",
          "quote": {
            "text": "چنین است گفتار و کردار نیست - جز از گردش کژ پرگار نیست",
            "poet": "Ferdowsî"
          }
        },
        {
          "id": 9,
          "parent": 0,
          "lang": "Avestan",
          "refs": "HRN:184; BQT:1442-82",
          "words": [
            {"translit": "fra 2, frank", "gloss": "forward", "script": null},
            {"translit": "fra-thang", "gloss": "pull forward (culture)", "script": null, "see": ["Ten 1"]},
            {"translit": "fra-stâ", "gloss": "stand (send) forward", "script": null, "see": ["Stâ"]},
            {"translit": "fra-aiš, fraĕšta", "gloss": "sent forward (angel)", "script": null, "see": ["Stâ"]},
            {"translit": "fra-var", "gloss": "protecting all around, Farvahar", "script": null, "see": ["Wer 3"]},
            {"translit": "fra-var-tinam", "gloss": "month of Farvahar", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 9,
          "lang": "Persian",
          "refs": "BQT:1446,1482",
          "words": [
            {"translit": "farâ", "gloss": "forward, more", "script": "فرا"}
          ],
          "script_extra": "فراتر\nفراگرفتن ، فراز ، فراسو ، فرهنگ\nفرستادن ، فرشته\nفروَهَر ، فروردین ، فردین",
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 9,
          "lang": "Sogdian",
          "refs": "SOD:155",
          "words": [
            {"translit": "frtr", "gloss": "more, better", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 0,
          "lang": "Avestan",
          "refs": "HRN:184; BQT:1442-82",
          "words": [
            {"translit": "fra-â-marz", "gloss": "one who forgives all", "script": null, "see": ["Mĕlg"]},
            {"translit": "fara-mana", "gloss": "pre-evaluate, order", "script": null, "see": ["Me"]},
            {"translit": "fra-dâta", "gloss": "promotion, call for help", "script": null},
            {"translit": "fra-jâma", "gloss": "end of going (destination)", "script": null, "see": ["Gwa"]},
            {"translit": "fra-vaxš", "gloss": "call out to sell", "script": null, "see": ["Wekw"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 13,
          "parent": 12,
          "lang": "Persian",
          "refs": "BQT:1482",
          "words": [],
          "script_extra": "فرامرز ، فرمان\nفریاد ، فرجام\nفروختن",
          "note": null,
          "quote": null
        }
      ]
    }
  ]
}
```


## [2026-09-14T00:49:44.694Z] TOOL CALL #4: Bash

```json
{
 "command": "ls data/verification/ | head -30 && echo --- && cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "List verification dir and source matrix"
}
```


### [2026-09-14T00:49:44.748Z] TOOL RESULT

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
---
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


## [2026-09-14T00:49:49.263Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/page-385.json'))\nprint(json.dumps(d['entries'][0], ensure_ascii=False, indent=1)[:3000])\n\"",
 "description": "Inspect a recent verification file format"
}
```


### [2026-09-14T00:49:50.423Z] TOOL RESULT

```
{
 "entry": 0,
 "root": "Peg",
 "verdict": "plausible",
 "modern_form": "PIE *peg- / *pōg-, *pōk-s- 'armpit, hip, loin, side' (Pokorny 792); Watkins/AHD lists the same root as *peg- 'breast'",
 "note": "Pokorny 792 prints the headword as '(peg-:) pog-: pōg-, pōk-s-' and glosses it 'Achsel, Hufte, Lende, Seite' (armpit, hip, loin, side) — the full-grade *peg- is only a bracketed, inferred variant. Nourai's headword 'Peg' with the gloss 'breast' is copied verbatim from the AHD (Watkins) appendix, which prints 'peg-. Breast.' The 'breast' sense in fact rests only on Latin pectus and Tocharian A pässäṃ / B pāścane 'the two breasts'; Sanskrit pakṣa- and Latvian paksis point to 'side, flank'. Modern scholarship (de Vaan via Wiktionary) further doubts that Lat. pectus and Skt. pakṣa- belong together at all. Root is real and the language label is right; the gloss is a one-sided simplification.",
 "note_fa": "ریشهٔ هندواروپایی آغازین که نورایی آن را Peg با معنای «سینه» آورده، در فرهنگ پوکورنی (ص ۷۹۲) با سرواژهٔ «(peg-:) pog-: pōg-, pōk-s-» و معنای «زیربغل، ران، پهلو» ثبت شده است؛ صورت *peg- تنها گونه‌ای بازسازی‌شده و درون‌کمانک است. معنای «سینه» را نورایی از پیوست ریشه‌های هندواروپایی فرهنگ AHD (واتکینز) گرفته که همان‌جا «Breast» نوشته است، ولی این معنا فقط بر پایهٔ pectus لاتین و pāścane تخاری است، حال آنکه pakṣa- سنسکریت و paksis لتونیایی بر معنای «پهلو، سو» دلالت دارند. افزون بر این، پژوهش امروزی (دِ ڤان، به نقل ویکی‌واژه) در پیوند pectus لاتین با pakṣa- سنسکریت تردید می‌کند. پس: ریشه واقعی است و برچسب زبانی درست، اما معنای داده‌شده یک‌سویه و ساده‌سازانه است — ادعای نورایی با احتیاط پذیرفتنی است.",
 "sources": [
  "https://en.wiktionary.org/wiki/%E0%A4%AA%E0%A4%95%E0%A5%8D%E0%A4%B7",
  "https://en.wiktionary.org/wiki/pectus"
 ],
 "ref_check": [
  {
   "ref": "POK:792",
   "status": "partial",
   "note": "Pokorny IEW p.792 (local POK_03.txt, form-feed leaf 25) reads: '(peg-:) pog-: pōg-, pŏk-s- \"Achsel, Hufte, Lende, Seite\". Ai. pákṣa- m. \"Schulter, Flugel\" und \"Seitenpfosten\", pákṣas- n. \"Seite\"; lat. pectus \"Brust\"; lett. paksis \"Hausecke\"; toch. A pässäṃ, B päścane \"die beiden Bruste\" ... WP. II 3 f., WH. II 270.' The page number is exact; the gloss is not 'breast'."
  }
 ],
 "consulted": [
  {
   "src": "AHD",
   "where": "Watkins 1985, s.v. peg-",
   "stance": "supports",
   "note": "'peg-. Breast. 1. Suffixed variant form *pek-tos- in Latin pectus, breast: PECTORAL; EXPECTORATE, PARAPET. 2. Possibly suffixed variant form *pek-so- in Sanskrit paksah, wing: PUNKA. [Pok. (peg-), pog- 792.]' — this is verbatim Nourai's chart (grep '^peg-' AHD_watkins1985.txt line 820)."
  },
  {
   "src": "WLD",
   "where": "Walde-Pokorny II 3-4 (WLD_Bd2_pages.txt leaf 8)",
   "stance": "partial",
   "note": "Entry headed 'pag-' (their spelling) with 'ai. pajasyá- n. Bauchgegend, Weichen, russ. pachu \"Leistengegend\", pacha \"Achselhohle\" ... ein io-St. *pagio- in cech. paze \"Arm\"' — again 'flank/armpit', no 'breast'."
  },
  {
   "src": "IEC",
   "w
```


## [2026-09-14T00:49:51.479Z] TOOL CALL #6: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','BRT','HRN','HUB','SOD','SNS','BQT','AHD','MON','PHD','NYB','WLD','KLN','IEC','SYN','CHEUNG','ARY','KNT']:\n    v=d.get(k)\n    print(k, json.dumps(v, ensure_ascii=False)[:400])\n    print()\n\"",
 "description": "Read refs_online entries"
}
```


### [2026-09-14T00:49:52.669Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 

BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sou

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 

HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1

SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in 

SNS {"title": "Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/VajnameShayest", "lookup_hint": "grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a

PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac

NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verific

WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-

IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I

SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in

CHEUNG null

ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 

KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "loca
```


## [2026-09-14T00:49:57.243Z] TOOL CALL #7: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','BRT','HRN','HUB','SOD','SNS','BQT','AHD']:\n    v=d.get(k) or {}\n    print('===',k)\n    print(' page_offset:',v.get('page_offset'))\n    print(' lookup_hint:',v.get('lookup_hint'))\n    print(' local_file:',v.get('local_file'))\n    print(' scans:',json.dumps(v.get('scans'),ensure_ascii=False)[:300])\n\"",
 "description": "Get page offsets"
}
```


### [2026-09-14T00:49:58.415Z] TOOL RESULT

```
=== POK
 page_offset: POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
 lookup_hint: Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-dictionary/ (entry pages with page numbers) and StarLing https://starlingdb.org/cgi-bin/query.cgi?basename=\data\ie\pokorny&root=config
 local_file: /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt
 scans: null
=== BRT
 page_offset: Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
 lookup_hint: Nourai's BRT numbers are Bartholomae's COLUMN numbers. Headwords are Avestan/OP in transliteration in bold at line start; OCR of the special transliteration is noisy - grep on a distinctive Latin gloss or the German meaning in quotes. Column numbers appear as standalone numbers at leaf tops.
 local_file: /home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt
 scans: null
=== HRN
 page_offset: leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
 lookup_hint: Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.
 local_file: /home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt
 scans: null
=== HUB
 page_offset: leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
 lookup_hint: Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by paragraph (§). grep the transliterated Persian word or Horn's entry number.
 local_file: /home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt
 scans: null
=== SOD
 page_offset: printed page ≈ leaf − 66 in SOD_pages.txt (0-based \f blocks; 645 leaves; English intro precedes)
 lookup_hint: Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/SogdianDictionary for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}
 local_file: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD.txt']
 scans: null
=== SNS
 page_offset: 242 leaves; page offset not determined (OCR too poor to read printed numbers) — locate by transliteration then read the page image
 lookup_hint: grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php search (see BQT) for better hit-to-leaf mapping.
 local_file: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS.txt']
 scans: null
=== BQT
 page_offset: vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...').
 lookup_hint: grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=dehkhoda, parsi.wiki, abadis.ir/fatofa/<word>/) quotes Borhan and often Mo'in's footnotes as (حاشیهٔ برهان قاطع چ معین). noorlib.ir/book/info/10294 is a 1-vol Nima 1380 Borhan without Mo'in's notes. | For pages in a scanned volume use: python3 tools/ref_page.py BQT:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)
 local_file: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages_faseng.txt']
 scans: [{"volume": "3", "file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf", "first_printed": 1208, "last_printed": 1925, "pdf_offset": -1205, "page_map": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pagemap.json", "lang": "fas", "o
=== AHD
 page_offset: 1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page.
 lookup_hint: Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru-' ; entries list English derivatives in caps. Restricted 1970s AHD scans on IA (lending only, djvu.txt returns 401): americanheritage0000dict (July 1977 printing, 970 leaves - probably the New College Edition), bwb_P9-BHZ-437 (1974), americanheritage00nyde (1970), bwb_W9-CSW-086 (1969, 1610 leaves = original 1969 ed.).
 local_file: /home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt
 scans: null
```


## [2026-09-14T00:50:02.970Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"lemma: per\" POK_full.txt | head -30; echo ===; grep -n \"Page(s): 810\" POK_full.txt | head",
 "description": "Find per- root in Pokorny full dump"
}
```


### [2026-09-14T00:50:03.036Z] TOOL RESULT

```
Exit code 1
16935:deesse : Portuguese deusa ' goddess '. [see Root / lemma: per-2\ to go over; over]. 
66301:Root / lemma: perd- 
66318:Root / lemma: perg-1 
66324:Root/ lemma: perg-1 \ "pole; trunk' derived from lllyrian : Baltic : Slavic prefix pre- + ga 
66353:Root / lemma: perg-2 
66371:Root / lemma: perk-1, prek- 
66379:Root/ lemma: perk-1, prek-\ to fill, derived from Root/ lemma: *(s)p(h)ereg-, (s)p(h)erag-, 
66418:Root / lemma: pertt-1 
66436:Root / lemma: perti-2, preR- 
66468:Root / lemma: perR-3, pfR- 
66490:Root / lemma: perti-4, preR-, pfR- 
66530:Root / lemma: pericu-s 
66537:the oldest IE cognate, hence Root/ lemma: pertcu-s'. oak derived from an earlier Root 
66569:Root / lemma: per-1, pera- : pre-, preu- 
66577:Root / lemma: per-1, pere- : pre-, preu- : to drizzle, sprinkle, jet, derived from Root / 
66631:Root / lemma: per-2 
66947:Root / lemma: per-2. B. per-, pera- 
67039:Root / lemma: per-2: C. per-, pera- 
67071:Root / lemma: per-2. D. per- 
67102:Root / lemma: per-2. E. per- 
67128:Root / lemma: per-3, per-g- 
67172:Root / lemma: persna, -snT-, -sno- 
67190:Root / lemma: pers- 
67196:Root/ lemma: pers-\ to drizzle, sprinkle; dust, ashes, derived from Root/ lemma: per-1, 
67220:Root / lemma: perth- {*pe-horghi-a) 
67228:Root / lemma: perth-{*pe-horghi-a)\ pole; sprout, derived from a prefixed pe- of Root/ 
(eval):1: == not found
```


## [2026-09-14T00:50:03.891Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==467' POK_02.txt | head -60",
 "description": "Print POK_02 leaf 466"
}
```


### [2026-09-14T00:50:04.899Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T00:50:08.089Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '66631,66720p' POK_full.txt",
 "description": "Print Pokorny per-2 entry"
}
```


### [2026-09-14T00:50:08.147Z] TOOL RESULT

```
Root / lemma: per-2 

Meaning: to go over; over, through, very, exceedingly 

Material: 

A. Dient as preposition, proverb and Adverb: a. per, pe/7(locative of root noun) 
"vorwarts, in Hinausgehen, HiniJbergehen about, in Durchdringen, in Ubermaft', from 
which "about - out, through - toward '; 



Old \nd'\c pan, Avestan pa/n, Old pers. par/y, gr. TTspi, irsp, alb. per {partiy also = Indo 
Germanic *pro), pej, pe, besides per {*per/) with wiederhergestelltem r, Latin per{*peror 
*per/y, Oscan-Umbrian per- and pert {*per-tl)\ gall, eri-. Old Irish ir-, e/"- (analogical *ero-)\ 
cymr. corn. bret. er, Gothic fafr-. Old English fyr-. Old High German fir- 'ver-', Old High 
German Old Saxon firi- ds.; Old Prussian per, Lithuanian per, per-; Slavic per-\v\ Old 
Church Slavic pre- etc.; from "vorwarts' entwickelte sich already Indo Germanic die 
meaning "very' (Old Indie pari-prT-'very dear', gr. nspi-KaAAnq "very beautiful', Latin per- 
magnus "very groft'; Lithuanian per-didis "to big, large'. Old Church Slavic pre-blagt "very 
good'), then die the Uberlegenheit (Old \u6\c pari- as-, pari- biiu-^ excel, surpass ', gr. 
nspi-sTvai ds.), of Ubermaftes or hohen Grades (Old \v\d\c pari-vid-, gr. n£pi-oi5a, Latin 
per-videre "genau know, have knowledge of '); esp. Old Indie and gr. is die meaning 
"ringsum, umherum' (Old Indie /Oa/7/-"umhergehen', gr. nspi-isvai; gr. nspi-^cbwufji = 
Lithuanian yOe/'-yc'i/s//"umgurten'); 

derivatives are: 

Gothic fairra NdN. "afar', as preposition "fern from'. Old Icelandic fjar{ri) Adv. "afar' 
(therefrom Kompar. firr, Superl. first). Old English feor(r), engl. far. Old Saxon ferr. Old 
High German ferrofKdv. "afar, very', Kompar. ferror {*fer-ro- iroru *fer-ero-); Old Church 
Slavic pred-b "before; voran; das Vordere' (as na-di^, prezh "about - toward '; -/roAdj.: 
prel^t "quer', Czech pi'fc(l<a)^ transom ' = Umbrian pe/ra/77 "virgam', Oscan perl<[ais] 
"perticis'; 

in zeitlicher Verwendung: Old \v\d\c par-ut, gr. nspuai etc. (see below uet-'year') and die 
derivatives Lithuanian pernai"\n vorigen years', Latvian perns Ad], "the previous year, firn'. 
Middle High German verne'the previous year', vern^\n vorigen years', Gothic only in af 
fairninjera'oiWor]a\r\re', Old Saxon fernun gere, fernun iara^\n Vorjahre', therefrom with 
„/b-forms Gothic fafrneis^-naKa\6(^ , Old Icelandic fyrndt "age'. Old High German firni^o\d; 
wise'. Modern High German F//77"old snow'; also to zero grade Gothic faur: Old Icelandic 
forn'o\d', besides the /-stem Old Saxon an furndagun. Old English fyrn, firn ^o\d'; compare 
Old Indie purana- "vormalig' to pura, ap. paranam " previously, in the past ' to para, Latin 
perendie^ the day after tomorrow ' from *peren-diel 

Maybe in -e- grade Latin Greek Albanian: Latin perendie {* peren-dies) " on the day after 
tomorrow ' : Albanian {* peren-diem) perendim m. " sunset, end of the day ', perendimi' 
west ', {* peren-destia) perendestia^ upper goddess ' {*peren-dea) perendia^ divinity '. 
Albanian {-dea, -desha^ goddess ' : Latin dea: Italian dea: Spanish diosa: French 
deesse : Portuguese deusa " goddess '. 



auf per- \n other Verwendung point at *per-u-r/n-\n horn. irsTpap (Pind. n£Tpa(;), 
n£ipaTO(;, Attic n£pa(;, -aTO(; 'ending, end', horn, direipajv ' eternal, infinite ' = (Attic) 
dnspova nspac; fjr| exovtq Hes., horn, nsipaivu), Attic TTspaivu) ' vollende '; - besides in Old 
Indie eine gleichlautende family the meaning 'knot': Old Indie pan/a- Nom. Akk. PI. n. 
"knot, joint ' (instead of *pan/j), paru-m. 'knot, joint, limb, member (ocean, sky, heaven)', 
parus-n. 'knot, joint, limb, member'; gr. nsTpap 'knot' is doubtful (G. Bjorck Mel. Boisacq 1, 
143 ff.). 

b. Adj. pero-s lurther': Old Indie p^^a-/? 'further, jenseitig, fiend; prior; later', Superl. 
parama-h lernster, last, best', Avestan ap. para- 'ulterior, the other, spatere, kijnftige', 
para-tara-l\en6'; Old Indie pa/'a/? (Nom. Sg. m. with adv. End stress) preposition m. Akk. 
'about - out', with Abl. 'fern from', with Instr. 'beyond from', seldom adverbal = Avestan 
paAd preposition m. Akk. 'besides - apart from'; Old \n6\c para, Avestan para {\nstr. Sg.) 
adverbal 'fort, weg, zurSeite'; Old \n6\c pare {Lok. Sg.) 'darauf, fernerhin'; Old Indie yoa/'a/r? 
(Nom. Akk. Sg. n. = Osean perum) 'out about, beyond, after', preposition with Abl.; 

Armenian /7e/7"remote, distant, afar'; 

gr. n£pc((v), Ionian nspnv (Akk. Sg. f.) 'daruber out, beyond'. Adv., preposition m. Abl. 
(Gen.); Latin per-peram^ inverted ', per-perus^ ineorreet ', from which gr. TT£pTT£po(; 
'Geek'; gr. TTspd 'daruber out, beyond' (Instr. Sg. f. of stem *pero-= Old Indie yoara' away, 
in another plaee, fort') ; therefrom n£paTo(; 'jenseitig' (TTspaiTspoq), nspaGsv 'from beyond 
her', Tfi nsparn (yfi) 'gegen Westen'; 

from a sehwundstufigen additional form from nspa through -/ro- extended is delph. 
npaKO(; 'with e. Geldstrafe covered', Ionian npnaaw Attic npaTToo 'durchfahre, vollstrecke, 
vollfiJhre, verriehte, do'; 

Osean perum (= Old Indie param) 'sine'; 

Old Irish l^e 'further, langer' {*perio-, das /"after s/?'long'); 

Hittite para{= gr. nspd) 'vorwarts, further, further', postposition 'from - heraus'; periia(n) 
'daruber out', postposition 'about - out', parranda 6s. (*= gr. nspav + 5£). 

e. prai, per5/(Riehtungsdativ of stem pei), also prei, pri, peri.
```


## [2026-09-14T00:50:11.988Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=66631 && NR<=67130 && /Page\\(s\\)|References|See also/' POK_full.txt | head -20",
 "description": "Find page numbers for per-2"
}
```


### [2026-09-14T00:50:13.174Z] TOOL RESULT

```
References: WP. II 29 ff., EM.2 754 f., 801 , 808 ff., 811 f., WH. II 283 ff., 351 , 364 ff., 
Page(s): 810-816 
References: WP. II 39 f., WH. II 344, Trautmann 206, 215 f. 
Page(s): 816-817 
References: WP. II 40 f., WH. II 250 f., 256 f., 257 ff. 
Page(s):817 
References: WP. II 41 f., WH. II 255 f., Trautmann 215. 
Page(s):818 
References: WP. II 28 f., WH. II 288 f. 
Page(s):818
```


## [2026-09-14T00:50:13.475Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"810\" POK_02.txt | head -20; echo \"=== leaf count\"; awk 'BEGIN{RS=\"\\f\"} END{print NR}' POK_02.txt",
 "description": "Find printed page 810 in POK_02"
}
```


### [2026-09-14T00:50:14.502Z] TOOL RESULT

```
5603:WP.  II  440  f.,  WH.  I  810  f.,  Trautmann  162.
=== leaf count
433
```


## [2026-09-14T00:50:24.548Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 44 45 46 47 48; do echo \"--- leaf $n\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n+1' POK_03.txt | head -12; done",
 "description": "Locate Pokorny page 810 in POK_03"
}
```


### [2026-09-14T00:50:25.659Z] TOOL RESULT

```
--- leaf 44
r'.
A.  Dient  als  Präposition,  Präverb  und  Adverb:
a.  per,  peri  (Lokative  des  Wurzelnomens)  , vorwärts,  im  Hinausgehen,- Hinübergehen  über,  im  Durchdringen,  im  Übermaß',  woraus  ,über  —  hinaus,' durch  —  hin';
ai.  pari,  av.  pairi,  apers.  pariy,  gr.  tvsql,  tcbq,  alb.  per  (z.  T.  auch  = idg.  *pr6),  pej,  pe-,  daneben  per  {*periy  mit  wiederhergestelltem  r;  lat. per  (-^per  oder  *peri):  osk.-umbr.  per-  und  per t  {*per-ti)]  gall.  eri-,  air.  iV, er-  (analogisch  *ero-)]  cymr.  com.  bret.  er;  got.  fair-,  ags.  fyr-,  ahd. /r- ,ver-',  ahd.  as.  firi-  ds.;  apr.  per,  lit.  per,  per-]  slav.  per-  'm  aksl.  pr^- usw. ;  aus  ,vorwärts'  entwickelte  sich  schon  idg.  die  Bedeutung  ,sehr^  (ai. pari-pri-  ,sehr  lieb',  gr.  Ttsgi-y.allrjg  ,sehr  schon',  lat.  per-magnus  ,sehr groß';  lit.  per-didis  ,zu  groß',  aksl.  prä-hlag^  ,sehr  gut'),  dann  die  der Überlegenheit  {2i\.  pari — as-,pdri — bhü-  ,übertreffen',  gr.  negi-eZvai  ds.),  des Übermaßes  oder  hohen  Grades  (ai.  pdri-vid-,  gr.  Ttegl-oida,  lat.  per-videre ,genau  wissen');  besonders  ai.  und  gr.  ist  die  Bedeutung  ,ringsum,  um- herum'  (ai.  pari  i-  ,umhergehen',  gr.  negi-ievai]  gr.  TC£Qi-L,(bvvviii  =  lit. per-jousti  ,umgürten*) ;
Ableitungen  sind:
Got.  fairra  Adv.  ,fern',  als  Präp.  ,fern  von',  aisl.  fjar{ri)  Adv.  ,fern' (davon  Kompar.  firr,  Superl.  first),  ags.  feor(r),  engl,  far,  as.  ferr,  ahd. ferro  Adv.  ,fern,  sehr',  Kompar.  f error  (♦/er-ro- aus  *fer-ero-)]  aksl.  ^r^c?^ ,vor;  voran;  das  Vordere'  (wie  na-d.^),  prez-h  ,über  —  hin';  -Ä:o-Adj. :  prlk^ ,quer',  cech.  pH^{kd)  ,Querholz'  =  umbr.  percam  ,virgam',  osk.  perk\ais\ ,perticis*;
in  zeitlicher  Verwendung:  ai.  par-üt,  gr.  -rtigvoL  usw.  (s.  unter  uet-  ,Jahr') und   die  Ableitungen  lit.  pernai  ,im  vorigen  Jahre',   lett.  perns  Adj.   ,vor-
k
811
iährig;  firn'^,  mhd.  verne  ^vorjährig^,  vern  ,im  vorigen  Jabre^,  got.  nur  in (if  fairnin  jera  ,yom  Vorjahre^,  as.  fernun  gei-e,  fernun  iära  ,\m  Vorjahre^, ^.ivon  mit  lo-Formans  got.  fairneis  ^itakaio^^  aisl.  fymd  i.  ,Alter',  ahd. jlrni  ,alt;  weise^,  nhd.  Firn  ^alter  Schnee^;  ebenso  zum  tiefstufigen  got. faur  das  aisl.  forn  ^alf^^,  neben  dem  i-St.  as.  an  furndagun^  ags.  fyrn^ ßrn  ^alt^;  vgl.  ai.  puränd-  ,vormalig^  zu  purä,  ap.  paranam  ,vormals^  zu parä]  lat.  perendie  ^übermorgen'  aus  *peren-die?
auf  per-  in  anderer  Verwendung  weist  '^per-u-2'ln-  in  bora.  neigag  (Find. itstgagjf  TTslgarog,  att.  Ttsgag,  -aTog  ,Ausgang^  Ende'^  bom.  dcTreiQwv  ,unend- licb^  =  (att.)  djtSQOva '  rvegag  ^ij  e'xovra  Hes.,  bom.  neiQaivcjjj  att.  nsgalvu) ^voUende^;  —  daneben  im  Ai.  eine  gleicblautende  Sippe  der  Bedeutung ^Knoten^:  ai.  parva-  Nom.  Akk.  PI.  n.  _,Knoten^  Gelenke'  (statt  *2?arüf), pdrii'  m.  , Knoten,  Gelenk,  Glied  (Ozean,  Him
--- leaf 45
mel)',  paru§-  n.  ^Knoten, Gelenk,  Glied' ;  gr.  TtsiQag  , Knoten^  ist  unsicber  (G.  Björck  Mel.  Boisacq 1,  143  ff.).
b.  Adj.  pero-s  , ferner':  ai.  pdra-h  ,ferner,  jenseitig,  Feind;  früber; später',  Superl.  paramd-h  ,fernster,  letzter,  bester',  av.  ap.  para-  ,ulterior, der  andere,  spätere,  künftige',  jpara-iara-  ,Feind';  ai.^rt?*«^  (Nom.  Sg.  m.  mit adv.  Endbetonung)  Präp.  m.  Akk.  ,über : —  binaus',  mit  Abi.  ,fern  von',  mit Instr.  ,jenseits  von',  selten  adverbal  =  av.  parö  Präp.  m.  Akk.  ,außer  — abgesehen  von';  ai.  pdräj  av.  para  (Instr.  Sg.)  adverbal  ,fort,  weg,  zur Seite';  ai.  pari  (Lok.  Sg.)  ,darauf,  fernerbin';  ai.  param  (Nom.  Akk.  Sg. u.  =  osk.  perum)  , binaus  über,  jenseits,  nach',  Präp.  mit  Abi.;
arm.  Jiei-i  ,entfernt,  fern';
gr.  7t£Qa(v),  ion.  7t€Qr]v  (Akk.  Sg.  f.)  , darüber  binaus,  jenseits',  Adv., Präp.  m.  Abi.  (Gen.);  lat.  per-peram  , verkehrt',  per-perus  , falsch',  woraus gr.  TtegrrsQog  ,Geck';  gr.  negä  , darüber  binaus,  jenseits'  (Instr.  Sg.  f.  vom St.  *pero-  =^  ai.  pdrä  ,weg,  fort^) ;  davon  uegaZog  ,jenseitig'  (itegalTegog), Tcegad-ev  ,von  jenseits  her',  tfi  Ttsgariß  (yfj)  ,gegen  Westen' ;
aus  einer  schwundstufigen  Nebenform  von  nsga  durch  -Jco-  erweitert  ist delph.  TcgäY.og  ,mit  e.  Geldstrafe  belegt',  ion.  Tigrjaaoj  att.  ng&TTO)  , durch- fahre, vollstrecke,  vollführe,  verrichte,  tue' ;
osk.  perum  (=  ai.  param)  ,sine';
air.  ¥re  ,weiter,  länger'  (^perio-,  das  l  nach  s'ir  ,lang') ;
bitt.  parä  (=  gr.  rtega)  ,vorwärts,  weiter,  ferner^,  Postpos.  ,aus  —  heraus'; periia{n)  , darüber  hinaus',  Postpos.  , über  —  hinaus', ^«rra72c?a  ds.  (*=  gr. negav  +  -de).
c.  prai,  perai  (Richtungsdativ  des  St.  per),  auch  prei,  priy  pe^i. Ai.  parB  ,daraufhin'  (Lok.  Sg.) ;
gr.   Tvagai    ,7vagd\    außerhalb    des   bom.    (ion.  att.)    nur   in   Kompositis,
812
•  .^
--- leaf 46
tibulätrix' ;  hierher  wohl  auch  lat.  jprwws  {*prei-uo8)  ,für sich  bestehend,  einzeln;  eigentümlich;  einer  Sache  beraubt',  prlvö,  äre  ,einer Sache  berauben',  prlvätus  , beraubt;  jemandem  als  Sondereigentum  gehö- rig', umbr.  prever  ,singulis',  preve  ,singuläriter',  osk.  preiuatud  Abi. ,privätö,  reo';
PcTi-  =  kelt.  [p'lari-  in  gall.  ai^e-  [Are-morica,  Are-brigium,  abrit.  Are- clütä  usw.)  ,bei,  vor,  bes.  östlich  von'  (vgl.  ir.  an-air  ,von  Osten^);
ahd.  as.  furi  ,vor,  für,  vorbei',  aisl.  fyr  (und  mit  Komparativendung fyrir)  ,vor,  für';  Kompar.  ahd.  furiro  ,der  frühere,  vordere'.  Superl. furist,  mhd.  vürst  ,erster,  vornehmster',  3ls.  furisty  ags.  fyr (e) st,  engl.ßrst, aisl.  fy7'r  adv.  , früher,  vorher',  fyrri  ,der  frühere',  fyrstr  ,der  erste',  ags. fyrsta,  as.  ahd.  furisto  ,Fürst';  got.  fri-sahts  ,Bild,  Beispiel,  Rätsel'  ent- hält schwundstufiges  *pin-,  wie  auch  ahd.  fri-liez  ziehen  fir-,  fai^-^fra-liez.
prei-  in  \h.  prie,  zem.  pry  ,bei,  an',  Nominalpräf.  prie-,  prie-,  prie-,  pi^- (auch  prei-kälas  m.  .Amboß),  Präverb  pri- ;  Präpos.  prie^  ,gegen',  pries ,vov^]  lett.  prie{k)8a  ,das  Vordere' (*preiiiä) ;  lett.  ^zere  , Stirn.  Vorderseite' (*^nere?);  apr.  prei  .zu.  bei',  als  Präf.  ,auch,  vor,  an',  preisiks  m.  ,Feind'; aksl.  pri  Präp.  und  Präf.  ,bei,  an,  zu';
aus  einem  dem  lat.  pri[s]mus  ähnlichem  '^prisjni-,  -ei:  air.  rem-  Präf. (lenierend)  ,vor,  voran'  {rlam  ,vor  ihm',  remi  .vor  ihr'),  remi-  als  Präverb, Präpos.  re  (nas.).
d.  Peres,  peros  (und  als  1.  Kompositionsglied  pres-  ,vor'.  Gen.- Abi. des  St.  per-) :
Ai.  puräk  Adv.  und  Präf.  .voran,  vorn'.  Präp.  .vor',  av.  parö  Adv. .vorn,  vor',  Präp.  ,vor',  gr.  ndcgog  Adv.  ,f ruber ;  voran,  vorn'.  Präp.  .vor'; prcs-  in  gr.  ngea-ßvg,  -yvg  .alt'  (,*im  Alter  vorangehend',  vgl.  ai.  purö- gavd'  .Führer'  (*Leitstier),  s.  unter  g^ou-  .Rind';  zu  kret.  itgeTayog  s.  oben);
813
^liS-ffist  m.  n.,  as.  frist  n.^  Sigs.ßrst  m.  ,Frist^  aus  *pres-sti-,  a,is\,  fr  est  n. eis.  lins'^pres-sto-j  vgl.  3i\.  pur  ah- sthita-  ^bevorstehend^ ;  aus  ^p^ros-stäti-s  ,im Alter  voran  seiend'^  wohl  air.  arsaid,  arsid  ,vetus^  (ai.  purdstät  ^yov,  voran^ vorn,  vorher'  ist  freilich  purah  +  Abl.-^J^).
e.  pr-  ^hervor^,  etwa  Nom.  Sg.  n.  des  St.  ^e?'- :  gr.  tt«^  in  Eigennamen ^vie  TlaQ'f-iBVLO'AOq,  in  el.  icaQ-ßaiva)  u.  dgl.,  /rao  Tor  vöfxov  u.  dgl,;  lat. por-tendö    (:  got.  faura^janjan),    -rigö,  pol-liceor    u.  a.,    umbr.   pur-douitu
porricito^,  falisk.  por-ded  ^brachte  dar,  widmete';  got.  faür,  as.  for,  für präp.  ,vor,  ^ür'^  ags.  for  ds.,  aisl.  for-  ,yoy%  mit  steigender  Bed.  aisl. for-ljötr  ,sehr  häßlich',  ags.  for-manig  ,gar  viele,  allzu  viele';
germ.  Ableitungen :  aisl.  forr  , hastig,  voreilig'  (*furha-,  vgl.  von  *pro : <rr.  Ttgö-aa  unten  S.  815);  as.  dlvies.  forth,  ford,  ag
--- leaf 47
s.  for d  ,fort,  vorwärts' ; mild,  vort  ^vorwärts,  weiter,  fort',  norw.  fort  , schnell,  bald',  3iis\.  forda,  ags. ge-forpian  , fortbringen' ;  Kompar.  *furpera-  in  a.s.  furpor,  für dor  Adv., ags.  furdor  Adv.  ,weiter',  furdra  Adj.  , größer,  höher',  ahd.  furdir,  -ar Adv.  Adj.  ,vorder,  vorzüglicher,  früher,  vormalig'.
Komposita  mit  Formen  von  stä-  ,stehen'  in  ai.  pv-stA-  f.  ,Rippe',  pf-sthä-m ,hervorstehender  Rücken,  Gipfel',  av.  par-Ua-  m.  , Rücken',  ^ar-s^i-  f.  (Du.) , Rücken',  mnd.  vorst-  f.  , Dachfirst'  aus  *for-stö,  a.gs.  fyrst  ds.  aus  *fur-sti-'^ daneben  mit  hochstuf.  Präfix  ahd.  first  m.,  ags.  fierst  f.  ,First'  aus  *ßr-sti- : wahrscheinlich  ebenso  lat.  postis  , Pfosten,  Türpfosten'  (*por-sti-s  ,hervor- stehendes');  gr.  naardg  (neben  naqaatdg)  ,Pfosten,  Pfeiler,  Türpfeiler', TtaoTcideq'  äfiTtsloi  Hes.  {*7taq-aTag),  lit.  pirHas,  aksl.  pr^si^  ,Finger' (,hervorstehend') ;
f.  perä  Instr.  Sg.  des  St.  *per:  ai.  purä  Adv.  ,vormals,  früher;  ehe, bevor',  Präp.  ,(zum  Schutze)  vor,  ohne,  außer',  av.  para,  ap.  parä  Adv. ,zuvor',  Präp.  ,vor',  davon  ai.  puränd-  ,vormalig,  früher,  alt',  ap.  paranam Adv.  ,vormals';  gr.  Ttagd,  Ttdga  Verbalpräf.  ,vor  —  hin,  dar-',  Präp.  ,an etwas  hin,  entlang,  neben;  während';  ,bei,  aus  der  Nähe  weg,  von  Seiten'; got.  faüra,  ahd.  as.  foi-a  Adv.  ,vorn,  vorher',  Verbalpräf.  ,vorher,  voraus, vor',  Präp.  ,vor',  ags.  fore  Präp.  ,vor'.
g.  pro,  pro  , vorwärts,  vorn,  voran',  Bildung  wie  *apo,  *upo]  pro  mit Auslauts  dehnun  g .
Ai.  prd-  Präf.  ,vor,  vorwärts,  fort'  (vor  Subst.  und  Verben),  ,sehr'  (vor Adj.),  2,Y.  frä,  fra-,  2i^.  fra-  Präf.  ,vorwärts,  voran;  fort,  weg';  gr.  ttqö Präverb  ,vor',  Präp.  ,vor',  TCQw-neqvoi  (rhythm.  Dehnung)  ,im  vorvorigen Jahr';  lat.  pro-,  pro-  in  Kompositis,  pro  Präp.  ,vor,  für';  prönus  ,vorwärts geneigt'  (von  *pröne,  vgl.  pöne  ,hinten'  aus  *post-ne)]  üher  prödest  s.  WH. II  365 ;  osk.-umbr.  Präverb,  pro-,  pru- ;
814
air-  ro-,  cymr.  ry-,  abret.  rf»-,  ru-,  mbret.  nbret.  ra-,  Präverb  und  \^:\ tensivpräfix,  z.  B.  air.  vo-mdr  ,zu  groß^  gall.  GN  f.  Ro-smerta;
got.  /ra-,  ahd.  /r-,  nhd.  ver-  Präverb  (letztere  z.  T.  auch  ==  got.  fair. ' s.  oben  A.);
apr.  pra,  pro  ,durch^,  als  Präverb  ,ver-',  lit.  pra,  pro  ,vorbei^  als  Prä, verb  ,vorbei-,  durch-,  ver-^  vgl.  prä-garas  , Vielfraß'  =  lett.  pra-garis  ds.;S^ lett.  prud-jäm  ,weg,  fort' ;  aksl.  Präverb  pro-  ,durch-,    ver-',  Präpos.  russ. öech.  pro  ,wegen',  ablaut.  russ.  prd-däd,  serb.  prä-djed  ,Urgroßvater' ;
gedoppelt:  ai.  prd
--- leaf 48
pra,  gr.  ttqöttqo  ,immer  vorwärts'.
pru-  (Reim  auf  *pW;  s.  *apo?)  liegt  zugrunde  in  gr.  öia-TVQv-aiög  ,durch.^ gehend',  Ttgv^vög  ,das  äußerste  Ende  von  etwa  bildend'  {fiQvuvr]  , Hinter- schiff' usw.).
pro-  ,früh,  morgens'  in  ai.  prä-tdr  ,früh,  morgens',  gr.  ngwi  (att.  nq(^) ,früh,  morgens',  ngmog  ,morgendlich',  dor.  nqoyäv,  nq&v  {*nQ(joäv),  att. 7tQ(^riv  [*n:Q(jüJ^Lav  seil,  -fj^gav)  ,kürzlich,  vorgestern',  ahä.fruo  ,in  der  Frühe', fruoi,  mhd.  vrüeje  (=  Ttgtülog)  Adj.  ,früh'  (idg.  *prö);  lit.  pro  ,vorbei', slav.  pra-  s.  oben.
Ableitungen  von  pro-:
prO'tero-  in  ai.  pratardm,  -am  Adv.  ,weiter,  künftig',  av.  fratara-  ,der vordere,  frühere',  gr.  Ttgövegog  ,der  vordere,  vorige';  osk.  pruter  pan ,priusquam'  ist  einzelsprachlich  zu  *prö-  gebildet,  ebenso  ai.  prätdr  ,früh, morgens'  s.  oben;
dazu  mit  Superlativsuffix  -temo-:  ai.  pratamäm  ,vorzugsweise',  av. fratdma-,  ap.  fratama-  ,der  vorderste,  vornehmste,  erste'  (daneben  ai. prathamd-  , erster'  und  einzelne  iran.  Formen  mit  th) ;  gr.  ^ngö-atog  (aus TTQÖzaTog?)  vielleicht  in  dor.  Ttgazog  , erster';  aber  gr.  TtgOJrog  ds.  aus *pf-to-  (umgebildet  aus  *pf-mo-  ds.);  dazu  rrgrjrrjv  m.  ,einjähriges  Lamm' (s.  oben  S.  314) ;
pro-zno- :  gr.  rrgöfiog  , Vorderster,  Vorkämpfer,  Führer',  umbr.  promom Adv.  ,prlmum',  got.  fram  Adv.  , weiter',  Präp.  ,von  —  her',  aisl.  fram  Adv. , vorwärts',  fra  (*fram)  Präp.  ,weg  von',  ahd.  fram  Adv.  ,vorwärts,  fort, weiter,  sogleich',  Präp.  ,fort  von,  von  —  her',  Sigs.  from  Adv.  , fort',  Präp. ,weg  von';  aisl.  framr  ,voranstehend,  vorwärtsstrebend,  ausgezeichnet', ags. /?'am  ,tüchtig  keck';
pTc-znO'  in  gr.  jigd^og  ,Führer'  (eher  korrupt  für  Ttgöfxog  ds.?),  got. fruma  ,erster'  (Su^.frumists),  mhd./rww,  vrom  ,tüchtig,  brav'  (nhd.  fromm] ahd.  as.  fruma  f.  Nutzen',  nhd.  Frommen) ;  ähnlich  lat.  probus  ,gut,  tüchtig, brav',  umbr.  profe  ,probe'  aus  *pro-bhuo-s  :  ai.  pra-bhü-  ,hervorragend  an Macht  und   Fülle',  sowie  in  abg.  pro-st^  ,rechtscha£fen,  einfach,  schlicht',
815
und  (aus  *pf-mo-)  as.  formo,  SLgs.  forma  .erster'  (Superl.  fyrmest),  lit. pirTuas  apr.  pirmas  .erster',  wahrscheinlich  lat.  prandium  .Frühmahlzeit' aus  *präm-ediom  (*pfm-).
prü-ko-  .voran  seiend' :  gT.  itgöy-a  (Nom.  Akk.  PL  n.)  Adv.  .sofort',  lat. reci-procus  eig.  .rückwärts  und  vorwärts  gerichtet',  alat.  procum  Gen.  PL. procerum'.  nach  pauperes  umgebildet  zu  proceres,-um  .die  Vornehmsten;  die aus  der  Wand  herausragenden  Balkenköpfe';  procul  .fern'  (vgl.  simul)-^
lat.  prope  .nahe  bei'.  Superl.  proximus,  eigeutl.  *pro-h'^.e  .und  vorwärts (an  etwas  heran)',  mit  Assimil.  p  —  k^  im  p — p;  dazu  propier  .daneben' (*propiter)  und  propinquus  .benachbart,  verwandt'  (vgl.  ai.  praty-dnd-  .zu- o-e wandt');  vgl.  oben  S.  813  germ.  *furha)
```


## [2026-09-14T00:50:41.904Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for p in 66 67 68; do n=$((p+21)); echo \"=== HRN printed p.$p (leaf $n)\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n+1' HRN.txt | head -40; done",
 "description": "Print Horn pages 66-68"
}
```


### [2026-09-14T00:50:42.870Z] TOOL RESULT

```
=== HRN printed p.66 (leaf 87)
— m —
np. per7' soll auch *Blatt' bedeuten, wie ai. parnd- ;
vgl. ebenso g. par^ kurd. per, af;'. pur, bei. pan (442),
wa;^. paU^ sar. porÄ-, si/n. />arjr (aus "^parnaka-).
294. /mr Voll'.
aw. perena- Voll*; phlv. pur; ai. pmrid-,
LW. kurd. afy. bei. (210) pyr, wa/. sar. pur 'voir.
Ich sehe nicht ein , weshalb auch Geiger, Laut-
lehre des BalücT, np. piir 'v o 1 V statt von aw. perena-^
ai. pfirnd' VolF von ap. pan^-, aw. pouru-, ai. puni-
Viel' ableitet, deren Bedeutung nicht passt. Laut-
lich mussten ja allerdings beide Worte schon im
Pchlevr zusammenfallen , aber pur 'viel' ist hier
bereits aufgegeben. Wenn der Kommentar z. B. aw.
pouru.mahrku' mit pnrmarg wiedergiebt, so hat er
voll Tod\ nicht 'viele tödtend' gemeint ; denn anderen-
falls hätte er rasmarg übersetzen müssen.
295. perfuf enden zerstreuen; erschrecken, pergenden,
phlv. pargantan (Bund.).
ap. "^para -\~ y/kan- (?). Der Bedeutungswechsel ist
allerdings sehr auffällig. Vergl. efgenden (No. 103).
296. pertew 'Glanz*.
para j- ^fap-^ vergl. np. fäßen (No. 372).
297. perdayten 'ausführen, ausleeren; streben, sich be-
mühen* ; Praes. ,perdazem.
phlv. parda/tan (AV.).
aw. *para + l^tac-; Bedeutungswechsel wie bei
end (Ixten (No. 117). Die np. Bedeutung 'ausleeren'
lässt sich aus 'weglaufen lassen' erklären.
von Stackeiberg (briefl. Mitteilung) vergleicht
oss. t. fäldä/jn 'wenden' (ZDMG. 41, 574 Anm. 3),
dessen Bedeutung sich mit der von V^tac- {-\- pard)
unschwer vermitteln lässt.
298. perest 'Verehrer , verehrend*, perestTde7i , perestür^
perestis.
=== HRN printed p.67 (leaf 88)
- 67 -
phlv.paras^* Verehrer, parastar,parastakzh, i)arast(i)sn
'Verehrung.
pari + l^ sthä' *um jemand herum stehen *).
299. pursTden 'fragen', pursis^).
g. parsädmün ; mäz. parsien ; Käs. vapersöddn, vöper-
sö'imün, vepersad,
ap. aw. [//ras-, Praes. pat{\parsähy bezw. peresahi
'fragen; iphW. pursUan, purs(i)sn, ptirsttar; ai. i^prag-^
Praes. pfchdti; arm. harc 'Frage', harcanem 'fragen,
harsn 'Braut' (H. No. 161).
kurd. />:/r5m 'fragen' ; aty. pust- hezw. pu/t-edal; oss.
d. farsun^ t. färsin (279); bei. LW. n. pur§ay (211);
WS,/, sar. pörsam.
300. perrisiym^uS, perrisiyCLvesän ^) , 'Frauenhaar (Pflanze),
Adiantum capillus Veneris L.'.
^= perr-t Siyävus y d. i. parenö (yö) Sydvarsäuahe
(de Lagarde, Armen. Stud. No. 1688, Pers. Stud.
S. 76).
301. pers 'Bach, Quell'.
aw. vergl. äpö parsuyäo 'Quellwasser yt. 8 , 41
(Geldner, KZ. 25, 481 Note 61).
Das Wort ist zweifelhaft und auch durch den von
Vullers s. v. citirten Vers Abu'l Ma'cäni's nicht ge-
V
sichert. Da es nur in dem FS. vorkommt, so könnte
es möglicher Weise sogar türkisch sein.
302. pergene 'Provinz, Distrikt'.
*parikhana' 'ein rings herum durch einen Graben
abgegrenzter Bezirk' (Hörn).
303. peren 'gestern', perendös 'gestern Nacht'.
ap. parana- 'ehemalig, früher ; aw. vergl. parö\ ai.
vergl. pards 'über hinaus, mehr als', purand- 'vor-
malig, purd einst'.
*) Dazu arm. amparist , ambarisf *unfpomm , gottlos* nach F r.
Müller, WZKM. 5, 186 (?).
*) Arm. LW. p^ursis,
«) AM., Seite 46. Vergl. auch x^n-i S. (AM. 128 Zeile 6).
5*
=== HRN printed p.68 (leaf 89)
— 68 —
kurd, per e; af}'. parün; oss. vergl. /ar- (274, 1);
bei. paran- 'darüber hinaus gehend' (284).*
304. pervär *Stair^).
aw. *2)airivära?ia-, vergl. pairi.vära- 'Wall*, 'Stall'
(vd. 2, 26 vielleicht, Bartholomae); phlv. {pä-amün-)
parvär,
eS05. perväi^ 'Flug .
aw. pairi (oder para) — V^vciz-, 'herum- bezw. weg-
fliegen , vergl. vazaiti er fliegt*.
306. jyerwerden ernähren, erziehen*, periveris, perwer'tden,
pari -f- y^hhar-; phlv. partoarfan, partvar(i)sn,
307. pervez 'siegreich*.
phlv. aparvej 'siegreich'; wohl zu «r^i, be.ze (No. 253)?
Dann perwez.
308. pervfn 'Plejaden*.
aw. paoiryaeinyas\ca (yt. 8, 12), de Lagarde, Beitr.
z. altb. Lex. 56.
af/. peröne; bei. panvar 'Plejaden (Dam es, 54).
309. perhey(ten 'sich enthalten ; sich hüten', Praes. perliez-etn^
perhez, perheztden^).
aw. palti + [/ra^c- 'verlassen'; phlv. pahre/tan
'sich enthalten', pahrej, pahrej(i)sn.
kurd. pärlstin, dispärise 'ist enthaltsam, enthält sich*.
^) Die persischen Original Wörterbücher geben für hervär (No. 210)
und pervär (die de Lagarde schon geschieden hat) zusammen die
folgenden Formen an : pervär^ perräre, perbär, perbärff perbäl, perbcUe^
fervür^ ferväre (vergl. No. 82S)^ fet'väl^ ferväle . von denen die mit/
beginnenden in dieser Bedeutung gewiss falsch sind. Als Beleg für
die Bedeutung *Stall* dient ein Vers des Xäqänl (Metrum: Munsarih).
röz^ beperrär^ büd^ färbe ez an sude cünin
seb tSn-t himär^ däst läylr ez an sude dun an
^) Die Annahme , dass np. pärsä 'enthaltsam , fromm*, aus
*perhezä (eine solche Form construirt sich Darmesteter, Et. ir. I,
115, NB. ohne Stern) contrahirt sei, ist durchaus unstatthaft. Pärsä
bedeutet überhaupt nicht 'enthaltsam', sondern ursprünglich nur *brav*
(vergl. Sahn. I, 35 Vers 15, 70 Vers 158 u. o.), es bezeichnet gewiss
eigentlich den Pärsen.
```


## [2026-09-14T00:50:54.956Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"irämün\\|iramun\\|Irämün\\|pTrämün\\|rämün\" HRN.txt | head -20; echo \"=== pust/pusht\"; grep -n -i \"^3[0-9][0-9]\\. pu\\|paršti\\|par.sti\" HRN.txt | head -20",
 "description": "Grep Horn for piramun and posht"
}
```


### [2026-09-14T00:50:55.021Z] TOOL RESULT

```
=== pust/pusht
3037:318. puser, pur 'Sohn, pus (Sahn. III, 1516 Vers 336,
3068:322. pusek, pösek *Katze' ('Dialekt von Transoxanien' BQ.)^).
3096:325. pul^) 'Brücke.
3210:340. puläd 'Stahl'.
```


## [2026-09-14T00:50:56.432Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for p in 184; do n=$((p+21)); echo \"=== HRN printed p.$p (leaf $n)\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n+1' HRN.txt | head -45; done",
 "description": "Print Horn page 184"
}
```


### [2026-09-14T00:50:57.449Z] TOOL RESULT

```
=== HRN printed p.184 (leaf 205)
— \Si -
826. ftHh viel, mehr.
aw. vergl. fräyäo, fraesta-; phlv. fr ah, f rahist
(Päz. freh^ frehest), ursprünglich freh^ vergl. freh[dätär
(AV.).
Die Aussprache ßrih (nicht fireh) bezeugen die
Keime der beiden bei Vullers s. v. mitgeteilten
Verse {bih und girih). Ich stelle das Wort zu den
von Andreas erklärten bih, kih, mih (No. 241).
827. ferl *lieb, schön .
aw. frya- geliebt, Freund*; ai. pnyä-,
828. feryäd *Hilfe; Hilferuf, Klage.
aw. fraöäia- ^Gedeihen, Förderung' (yt. 13, 68);
phlv. frayät bezw. fradät 'Hilfe*.
Die mittelpersische Bedeutung *Hilfe* findet sich
auch noch im Neupersischen, z. ß. AM. 43 Zeile 6, 82
Zeile 1 V. u., Öähn. I, 126 Vers Uli (NB. wohl un-
echter Vers).
LW. kurd. af/. feryad-, bei. paryat 'Geschrei* (199).
Anders Fr. Müller, WZKM. 5, 353.
829. fireften 'betrügen*, Praes. fireb-em , ßreb 'Betrug*,
ßreftär, JTJKSnE^ (Jer. 20, 7).
ai. pra + [/"rep- 'anschmieren, betrügen', vergl. rip^
'Betrug, ripü' 'Betrüger ; phlv. freftan^ frepet^ f^^P^
frep(i)sn, freftär.
oss. d. fälewun, t. fäliwin 'betrügen* (271). Sar.
rof-am hat noch die Bedeutung 'beschmieren' bewahrt.
830. fe^, fuy 'Götterbild (Geliebter, Geliebte)', fuyistün
V
'Harem* (Sahn. II, 532 V. 198), fuyäk 'töricht', fuyvare
sprachlos, vergl. Fayfür (Seite 71 Note 1).
ap. baga- 'Gott*; aw. baya-; phlv. bag]baxt (ge-
schrieben baW) ; ai. bhdgha-.
Die echt persische Form hat sich im Np. nur in
Ba/däd erhalten, das / ist eine Arabisirung.
```


## [2026-09-14T00:51:09.452Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && n=49; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n+1' HUB.txt | head -60",
 "description": "Print Hübschmann page 39"
}
```


### [2026-09-14T00:51:10.420Z] TOOL RESULT

```
— 39 —
proceeding', parddz ^finishing, completing ) stimmt nicht
zu Horn's Etymologie: zA. para + tacay- Veglaufen
lassen . Phi. pardaxt verbraucht' Arta-Vlraf Cap. 89,
6 ist unsicher.
298. Bei der vorgeschlagenen Etymologie: skr. pari -f
sthci 'umstehen' erwartet man ein praes. *paristam
aiis *paristam (fur parastatn)^ inf. *paristadan (fiir
parastidan). Vgl. estadan und firistadan,
299. Np. pursam = ap. prsamiy (nicht parsamiy). Die
Wurzel war ap. und iran. fras (auf der mittleren
Stufe), prs (auf der NuUstufe).
301. Die Bedeutung von zd. parsuy&o ist unsicher; Geld-
ner erschliesst sie aus np. pars *Bach*, das Horn
wieder fiir unsicher halt. Auch sollte np. *pas- einera
zd. pars- entsprechen.
Np. pargdl = pargOr 'Zirkel' (afgh. parr/dr 'Zirkel')
stellt de Lagarde (Btrg. zur bactr. Lexic. p. 54) nebst
pargar 'Halskette' zu zd. pairikara- vd. 17, 6 = Turche'
(phi. pBramUn-karisnlh) und vergleicht skr. jmrikara-
'Giirtel'. Unsicher.
302. Np. pargana 'terra vel provincia vectigalis; an in-
ferior division of a country nearly equalling a barony',
afgh. LW. pargana dt. gehort sicher nicht zur Wurzel
kan *graben'.
303. Slvend. para Vorgestern' (Journ. asiat. 1893, 294)
hierher oder zu Nr. 311 oder 270.
304. Zd. pairivara- heisst yt. 1, 19; 13, 71 bestimmt
'Schutzwehr'(*Abwehr Geld ner,*Wehr* Bart hole mae,
'cuirasse par devant' Darmesteter) und wird also
vd. 2, 26 ohne Not nicht anders zu iibersetzen sein.^)
Es gehort also nicht zu np. parvdr 1) 'Mastvieh*,
2) *Nahrung*, 3) 'Ort, wo man Vieh mastet', das doch
sicher zu parv(lra^ parvdrl gemastet, fett*, parvardan
'ernahren, futtern, erziehen' etc. zu stellen ist. Be-
deutung und Etymologie von hebr. parbdr, parvdrtm
*) Dazu nach Fr. Miiller aram. parvara ^Vorstadt, Vorhof*
(aus Levi's neuhebr. Wb.)
```


## [2026-09-14T00:51:24.377Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && n=48; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n+1' HUB.txt | tail -30; echo \"=== p40\"; awk 'BEGIN{RS=\"\\f\"} NR==51' HUB.txt | head -30",
 "description": "Print Hübschmann pages 38 and 40"
}
```


### [2026-09-14T00:51:25.429Z] TOOL RESULT

```
oben Nr. 144. Das Wort padid sichtbar ist erst im
Mittelpers. componirt aus pa und dU == 'in Sicht'
wie padrud aus pa und drut (Horn, Nr. 288).
291. Np. padtra 'entgegen = paz. padtra Min. Gl. 151,
Shk. 261, phi. patlrak Gl. and Ind. 95 etc. lasst sich,
da phi. paVSrak fest steht, nicht auf ein phi. "^patglrak
zuriickfiihren und mit Nr. 290 : padlruftan ( entgegen-
nehraen, annehmen = phi. patgrafian (ap. patiy H-
grh) vermitteln. Ich glaube, dass die beiden Worter
wurzelhaft verschieden *) sind und nur die Praep. pad-
= ap. patiy gemein haben, dass aber phi. patgraftan,
pr. *patg%ram 'entgegennehmen' friih von patlrak *ent-
gegen* lautlich beeinflusst worden ist. Sonst sind auch
die Lautverhaltnisse von padlruftan unerklarbar. Denn
warum heisst es nicht: *paigriftan, *paigiram?
295. Np. pardgandan zerstreuen', phi. pargandak 'scat-
tered* (61. and Ind. 103) passt jedenfalls nicht zur
Wrzl. kan graben'. Es gab ja wohl auch noch andere
Wurzeln kan oder gan. Vgl. Nr. 41 : agandan VoU-
stopfen'.
296. Np. partav 'Licht, Strahl* (auch afgh. LW.) mit auf-
falligem t fiir d, Anlehnung an tab, taftan etc.?
297. Np. pardaxtan hat bei Vullers 12 Bedeutungen,
es ist schwer zu entscheiden, auf welche man die
Etymologie bauen soil. Die gewohnliche Bedeutung:
VoUenden, beendigen, sich mit etwas beschaftigen'
(vgl. afgh. LW. pardaxt performance, relinquishment,
*) paSira = phi. patirdh gehort zu zd. paiti + ar^ wovon pat-
tyUra' 'Opposition', paiti-ereiti- 'Widerstand, Hinderniss*, apaitiereta-
'ohne Widerstand, ungehemmt'. Ich setze paSira = ap. ^pati-jrya-.
=== p40
— 40 —
ist unsicher; de Lagarde, Btrg. z. bactr. Lex. p. 55
ist schwerlich im Recht.
307. Fr. Muller WZKM. 6, 352 bemerkt mit Recht, dass
man fiir paz. awarvez Shk. 233 = arm. AprUSz (= Aprv^)
im Neupersischen *barvez anstatt parvez Victor, felix,
fortunatus' erwarten miisste. Ist es beeinflusst durch
p^rdz Victor, felix, faustus ?
308. Ich kann die ihrem Sinne nach zusammengehorigen
Worter (ZDMG. 44, 560) lautgesetzlich nicht ver-
einigen. Darmesteter liest mit Westergaard
paoirySnyaS' (von paoiry^i- aus *pdrvydni-^ vgl. afgh.
pSrune, Geiger, Etym. Nr. 170), das er mit ahuranfs
(von ahurani' ahurisch*) vergleicht und durch *die
(Wasser) des Paoirya (Zend-Avesta II, p. 418) iiber-
setzt. Aber Geldner liest paoirya^iny as- von paoirya^i-
= ap. *paruviyaini' = np. parvm?
309. Np. parhe» 'Enthaltsamkeit, Fasten', parMxtan *sich
enthalten' = paz. pahrez Min. GL 154, phi. pahrSd
'abstinence* GI. and Ind. 88, *Vorsicht* Yatk. i. Zar.
p. 62, Anm. 48, pClhredSnd *sie hiiten, pflegen ebenda
p. 51, Anm. 16. Von dieser Pehleviform fiihrt kein
Weg zu Fr. Muller' s (WZKM. 6, 185) zd. ^paiti-ra^d-
Verlassen*", dem doch nur np. *pairextan entsprechen
wiirde. — Arm. pahrez 'Fasten' ist einmal im 14. Jhd.
belegt.
310. Zd. pairika- schlechtweg durch *Hure' zu iibersetzen,
ist falsch. Die Pairika s sind Teufelinnen, die die
Frommen zu verfuhren und vom rechten Glauben ab-
wendig zu machen suchen; phi. parlk bose Fee'
```


## [2026-09-14T00:51:26.557Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"pairi\\.vāra\\|pairi-vāra\\|pairivāra\\|pairi\\.vara\" BRT.txt | head; echo \"=== frank/frąnk\"; grep -n \"frąnk\\|fra\\$k\\|frank-\" BRT.txt | head -20",
 "description": "Grep Bartholomae"
}
```


### [2026-09-14T00:51:27.640Z] TOOL RESULT

```
=== frank/frąnk
18332:•  fri^s'*  Adv.:  s.  MxOia  frank- . «)  Auch  YL  10.  ;i,
```


## [2026-09-14T00:51:50.766Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '18320,18345p' BRT.txt; echo \"======= search frąnk\"; grep -n \"fra\\{0,1\\}[aą]nk-\" BRT.txt | head -20",
 "description": "Bartholomae frąnk- context"
}
```


### [2026-09-14T00:51:51.888Z] TOOL RESULT

```
•  g.  firörstöÜ  InC  Vonrärts  zu  bringen, zu  fördern':  t^  tSng  ängvä  ySng  asahya vasdrStig  (sd.)  pal  ga  fr'  SsikrahyS  vä daäysus  vä  "der  .^n^fgenosse  will  es  nicht haben,  dass  die  Förderer  des  Aia  das Rind  in  Gau  und  Land  zimi  Gedeihen bringen"  y.46.4.
Zum  V.  lor-  mit/rJ,  %36S.  4,  —  \g\./rin- lay:  —  Pü. :  kac  franatniln,  Sü. :  samadeiil, NpO. !  fls  raflan.
•  j.  frö.hakafra-  m.  EN.  eines  Gläubigen: °rake  mansismyehe  sasttanqm  aiaoaif  Yt 7j.  ia6.
Et?    An  ehesten  ootAt /rÖ,Aaita-/ra:
•  '].  (frJcnk-)  Adj.  'nach  vom,  herzuge- wendef ;  nur  ISn.  fra^a  und  NSm.  frql als  Adv.  1)  fraca  "voran,  hervor',  nur  ^ Praev.  mit  V.  Aarpt-  sva.  fra-karst-,  Y. 9.8".  2)  frqs'^  a)  'voran,  von^its': hö  mairyS .  ./f  ayanhs  frasparal  ". .  vor- wärts schnellte  er  unter  dem  Kessel  her- vor" Y.p.  11;  F.  13;  —  mit  AbL^);  vm- %raynB  .  .  yS  yr"  *lacS*'^  hamfn%ä%a  .  . ni/ainti  ".  .  der  dem  Gegner  voran- laufends*.."  Ytio.71.  b) 'herzu,  heran': ndit  iiira  .  .yr°'>  iyä/  (Sp.  270  o.)  Aagna . . "nicht  möge  hier.,  herankommen  Feindes- heer" Yt.  Ä  s6.
Ableit.  (vgl.  '/räia-,  /rSrya-,  fraka-,  /raJa\  — Ableit.  ans  */ra;  S  r/S,  38g.  —  ai.  fraük- : prak- ;  aip./rai7),/räc>i),  o'p./arä  »./aräx«).  — Pa. !  /rä/.  —  I)  Sonst  ist>'  /ra-ü  Cnnd'):  V.  a. 'Of  5-  34«  7-  12,  Yt.  /a  iiS  oder  kann  es
Diaitizedby  VjiOOQIC
fr^s
nigster
,19-  i
t,jo.  :
Cld.s  Bemerkung  zu  Y.j.  8,  GGA. /(?pj.  400 ist  mir  nicht  deuilicli.  —  =>  Vgl.  No.  6  und  ' zu  far^  ttls  Ad«.  —  3)  Vgl.  ai.  p-äi  tnü  Abi.  I —  4>  NA,  /nfs/arS,  —  s)  Sva,  im  Lauf  über-  ^ holend.  —  ^)  Lässt  sich  nur  als  Adv.,  nicliC ' als  NS.  fassen,  da  AnFml-  feminin  ist.  — ! :\7)  Aus  ir.  */r5kam;  Dthl.  IF.  I2.  99.  — »)  Wohl  gleich  ai.  ftäd  Adv.
•  fri^s'*  Adv.:  s.  MxOia  frank- . «)  Auch  YL  10.  ;i,
•  j.  fraätay-  f.  'Erreichen,  Treffen':  nsit gmake".  .  tbaisB  "liQS.yVina  früsiiuyM Yt.7/.s.
Komp.;  *fra\*^lay-  f.,  lum  V.  qs-.  —  PQ.: ^u?  .  ,  bis  fräi  hamparsik  /täc  hamfursiin.  — ■)    Zur  Verslärkung   des   Verbalbegritfs ;    die Stelle  hat  geringen  Wert. g./ri^tä:  s.  qs-
•  j.  fri-  f.  '(was  dazu  dient,  einen  Gott gnädig  zustimmen,)  Flehen,  Gebet';  kui^ra ia  fryS  (NP.)  . .  tä  iluds  . .  tä  ratayS  (sd.) öavan  {näml.  aoiMta)  Y.  65.  9.
KÖmpE.  (s.  ä/rl').  —  Zum  V.  frSy.  —  ai. vgl.  ä-frt-  f.    —    Pü. !    ,  .  franäft  .  . ;    s.  bei
•  j.  fritay-  f.  'Gebe^'':  ''fm  *mä ..*gära- ySis  (sd.)  yat  ratus  *°töiP'^  *äjasät  N.  ig.
KompE.  —  Zum  W./räy:  —  fi.-./mnämii- nlh,    erl. ;  gäsäiiiär  yaSlan.  —  "»  Vgl.  fri:  —
]. /rilSJarqra  Vyt.  6q:  V\ks  J'rßiö.'.
•  j.  "friSist  N.  6>.    Ob  Faz-I
•  j.  friO'a-  Adj.  (fem.  -äa-)  i)  'erfreut, froh,  sich  freuend  an'  (Gen,):  -"ham (näml.  da^am)  gSusca  väsirahe:a  Yt.  13. 100.  2)  'geliebt,  lieb,  beliebt':  fryS '■'äo/ai/i.zaniJY.3j.$4;  Yt.(?.43,  V.iff.40; —frya  '%a  (NS(.)paiti.san/aYt.lS-$6;  — iU  "Sja  (NPf.)  JiaiHsantä  buyata  (sd.)  Yt. 13. 147;  —  'äd«  haitim  fri%S.larqm  (sd.) H.  2. 14;  —  '%a  (VSf)  spmta  ärmaite  V. 2.  10;  —  Uta  tl  . .  afrmämi  .  .  'äfl(ISf.) dahma  a/riii  V.  22,  5,
Ableil.  (s.  auch  '/rÄ/Va-)-  —  Zum  V./rSy; S  sqp.  8,  —  Ttp./arT  'froh';  s.  daiu  HbM. IFAni.  6.  33.  —  Pü.:>flBä/V,  zu  H.  ?  erl.: JH^  däil;  (zu  V.  2):  dülärmJhä.
•  j.  fri96.tara-  Adj.  (fem.  °rä-)  'der  be- liebtere': Ja/  mam  frfiqm  kailTm  'rqm "du  (hast)  mich,  die  ich  beliebt  war,  noch beliebter  (gemacht)"  H.  2. 14,
Vi.:  franSftlar,  erl.:  xvptar  däil.
•  j.  frinäspa-  m.  £N.  eines  Gläubigen: 'pahe  kaivahe  (sd.)  a^aanS  Yt.  y,  122.
======= search frąnk
18332:•  fri^s'*  Adv.:  s.  MxOia  frank- . «)  Auch  YL  10.  ;i,
```


## [2026-09-14T00:51:55.089Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PHD pērāmōn\"; grep -n -i \"peramon\\|pērāmōn\\|pyrʾmwn\" PHD*.txt | head; echo \"=== PHD parwardan\"; grep -n -i \"parwardan\\|parwar\" PHD*.txt | head; echo \"=== PHD pargar\"; grep -n -i \"pargār\\|pargar\" PHD*.txt | head; echo \"=== PHD pardaxtan\"; grep -n -i \"pardāxtan\\|pardaxtan\" PHD*.txt | head; echo \"=== PHD partaw\"; grep -n -i \"partaw\\|partab\" PHD*.txt | head; echo \"=== PHD paragandan\"; grep -n -i \"parāgandan\\|paragandan\\|pargandan\" PHD*.txt | head; echo \"=== PHD pušt\"; grep -n -i \"pušt \\|pusht\" PHD*.txt | head; echo \"=== PHD frāz/frēstag\"; grep -n -i \"frāz\\|frēstag\\|frestag\" PHD*.txt | head",
 "description": "Grep MacKenzie Pahlavi dictionary"
}
```


### [2026-09-14T00:51:55.229Z] TOOL RESULT

```
=== PHD pērāmōn
PHD_mackenzie.txt:4196:peramOn [pyPmwn l I M pyr)mwn, N --mun] around.
PHD_pages.txt:4196:peramOn [pyPmwn l I M pyr)mwn, N --mun] around.
=== PHD parwardan
PHD.txt:542:~ AZ: free (oneself) from. pargandan, pargan- [plkn-, plgn-dn! | (P pr'gnd, N parāgandan)] scatter, distribute, disperse. pargast [plgst' | N ~] let it not happen! Heaven forbid! pargüd [plgwt' | P prgwdg], ~ az: free, exempt from. parig [plyk' | M pryg, N pari] witch. paristag [pistk! | N pirista] servant. ~th: service; worship. paristar [plsť] | N parastár] maidservant. paristidan, parist- [plst-ytn' | M pryst-, N parastidan] serve, worship. ~išn: service, worship. paristog/k [plstwk' | P prstwg, N piristū(k)] swallow. рагпабап [pinyE?n! | M prng?n, N parniyān] polychrome damask. parr [pl | M pr, N ~] feather, wing. parrag [plk', pig | P prg, N ~a] wing. ~ig [-vk'] winged. parréxtan, parréz- [plyhin', plyc-] remain over, be superfluous. parrón [plwn' | M prwn] hence, away. parrwar [plwl | M prwr] winged. parsig [p’lsyk' | N pārsī] Persian. pars [5/f] spotted, speckled. parwāl [plwl | (P prwrz)] refreshment, nourishment. parwal- [plw���l- | (P prwrz'dn)) foster, nourish, -išn: nourishment. parwanag [phonk! | M prw’ng, N ~a] guide, leader. ^h : guidance, leadership. parwand [plwnd | N —] enclosure, comprehension. parwand-, v. parwastan. P parwānģāh [*plw?ng’s] throne. parwār [plyw?l | N ~] citadel; circumvallation; suburb, surroundings. parwardan, parwar- [plwl-tn' | M prwrdn, N ~) foster, nourish, cherish, educate. ~išn: nourishment, fostering, education. parwast [plwst'] enclosure. parwastan, parwand- [plwstn', plwnd-] surround, enclose, contain, comprise. parwāz [plw’c | N ~] flight. parzin [picyn' | M prcyn, J przyn, (N parčīn)] fence, hedge. pas [AHL < A?hr; BATL < Ab2tr; ps| = M, N ~] then, afterwards, behind. ~ az: after. ~ih: rear. pas [p’s | = M, N ~] guard, watch. ~ dāštan: keep watch, guard. pāsbān [p’sp’n' | M p’sb’n, N ~] guardian, watcher. ~ih: defence, protection.
PHD.txt:1214:cherish parwardan.
PHD.txt:1736:educate frahixtan, parwardan.
PHD.txt:1738:education frahang, parwarišn.
PHD.txt:2022:foster parwardan, parwāl-.
PHD.txt:2942:nourish parwardan, parwal-.
PHD.txt:2943:nourishment parwül(i$n), parwarišn.
PHD.txt:4667:parwar- parwarisn Frawardin Frawardīgān fraward parwardan frawardag franam- parwast parwastan franaftan frušag
PHD.txt:4682:frasang parragig pargan- parwar pargandan pargüd frég, parig frest- fréstadan fréstidan pargast fréstag fréb
PHD_pages.txt:4062:parwar [plyw'll N ......] citadel; circumvallation; suburb, surroundings.
=== PHD pargar
=== PHD pardaxtan
PHD.txt:539:pahikdftan 64 pardāxtan
PHD.txt:540:pahikēftan, pahikob- [ptkwp-tn'] strike. pahlawig [*p’hlwbyk' | (M phlwnyg), N paklaw(ān)i] Parthian; Pahlavi. pāhlom [phlwm] excellent, best, foremost. ~ih: excellence. pahlüg [p'Aok! | N pahli] side, rib. pahn [p?An! | N ~] wide, broad. сау [2d | N —à] width, breadth. lpahrextan, pahrēz- [phlyhtn', p'hlyc- | M phryz-, ] ~, N parhéxtan, parhéz-] abstain, refrain, avoid. *pahréxtan, pahrēz- [p’hlyhtn', p'hlyc- | M (phrystn), phryz-] care for, tend, protect. pahréz [Аус | N parhéz] defence, care. *pahrmāh- [ptimwh- | (N parmds-)] touch. ~арфіһ [Pkyh], ~i$n: touch, feeling. pak [DKY A < A аку; рк | = M, N ~] clean, pure, holy. ~ih: purity, holiness. pākīzaģ [p’kyck' | N ~a] pure. palang [ping | N ~] leopard. —-mušk [-mwsk' | N ~] speckled basil. pálüdag [p'Iwtk! | N ~a] starch jelly, flummery. pālūdan, pālāy- [p’lwtn', pPd- | (M p’rwdn, p’r’y-), N ~] strain, filter, purify. pambag [pmbk' | N panba] cotton. —ën [-yn'] (made of) cotton. pānāģ [p’n(’)k' | M p’ng] guard, protector; shepherd. ~th: protection. panāh [рт | = M, N ~] protector; refuge. pad ~ griftan: take refuge with. ~ih: protection. pand [pnd | = M, N ~] path; counsel, advice. panir [pnyl | N ~] cheese. panj [pnc | P рту, (M pnz), N ~] five. ~ag [-k! | N —a] pentad; hand, paw. ~аһ [h | N ~] fifty. panzdah [p’ncdh | M p’nzdh, N ~] fifteen. ірагаб [p?/k! | N para] piece, part, portion. ?párag [p?/k! | M p’rg, N para] gift, offering, bribe. paráhóm [pP?hwm = Av. para.haoma-] consecrated drink (the infusion in holy water of pounded лот and pomegranate twigs, sometimes with milk added). pardag [pitk! | N parda] veil, curtain. pardaxtan, pardaz- [pldhin', pldc- | M prdxt, N ~}, ~ az: be done with, freed of. ^ 6: set about, undertake. ~išn: freedom; undertaking. pardāxtan, pardaz- [pld’htn', pld?c- | N ~] accomplish.
PHD.txt:541:pardāxtan 65 pāsbānīh
PHD.txt:1680:done, be ~ kirīh-; be ~ with pardaxtan az; not — akard.
PHD.txt:2038:free (v.) wišādan; ~ oneself from pardāxtan az.
PHD.txt:2039:freed, be — of pardaxtan az.
PHD.txt:3599:set about pardaxtan 6.
PHD.txt:4123:undertake abar burdan, fraz griftan, pardaxtan 6.
PHD.txt:4688:frahixtan frahixtag frayádisnig fravādišn frāy frādahišnīh frahist farroxīh farrox lxwah-I xwastant frārāst frārūnīh frārēn frāmēš frūmēš- frāmuštan frahist parrag frch pardāxtan frehbūdīh frehbūd pardāz-
PHD.txt:4689:pardaxtan, parrēxtan
=== PHD partaw
=== PHD paragandan
PHD.txt:542:~ AZ: free (oneself) from. pargandan, pargan- [plkn-, plgn-dn! | (P pr'gnd, N parāgandan)] scatter, distribute, disperse. pargast [plgst' | N ~] let it not happen! Heaven forbid! pargüd [plgwt' | P prgwdg], ~ az: free, exempt from. parig [plyk' | M pryg, N pari] witch. paristag [pistk! | N pirista] servant. ~th: service; worship. paristar [plsť] | N parastár] maidservant. paristidan, parist- [plst-ytn' | M pryst-, N parastidan] serve, worship. ~išn: service, worship. paristog/k [plstwk' | P prstwg, N piristū(k)] swallow. рагпабап [pinyE?n! | M prng?n, N parniyān] polychrome damask. parr [pl | M pr, N ~] feather, wing. parrag [plk', pig | P prg, N ~a] wing. ~ig [-vk'] winged. parréxtan, parréz- [plyhin', plyc-] remain over, be superfluous. parrón [plwn' | M prwn] hence, away. parrwar [plwl | M prwr] winged. parsig [p’lsyk' | N pārsī] Persian. pars [5/f] spotted, speckled. parwāl [plwl | (P prwrz)] refreshment, nourishment. parwal- [plw���l- | (P prwrz'dn)) foster, nourish, -išn: nourishment. parwanag [phonk! | M prw’ng, N ~a] guide, leader. ^h : guidance, leadership. parwand [plwnd | N —] enclosure, comprehension. parwand-, v. parwastan. P parwānģāh [*plw?ng’s] throne. parwār [plyw?l | N ~] citadel; circumvallation; suburb, surroundings. parwardan, parwar- [plwl-tn' | M prwrdn, N ~) foster, nourish, cherish, educate. ~išn: nourishment, fostering, education. parwast [plwst'] enclosure. parwastan, parwand- [plwstn', plwnd-] surround, enclose, contain, comprise. parwāz [plw’c | N ~] flight. parzin [picyn' | M prcyn, J przyn, (N parčīn)] fence, hedge. pas [AHL < A?hr; BATL < Ab2tr; ps| = M, N ~] then, afterwards, behind. ~ az: after. ~ih: rear. pas [p’s | = M, N ~] guard, watch. ~ dāštan: keep watch, guard. pāsbān [p’sp’n' | M p’sb’n, N ~] guardian, watcher. ~ih: defence, protection.
PHD.txt:1644:disperse pargandan.
PHD.txt:3526:scatter afšāndan, pargandan.
PHD.txt:4671:fragandan, pargandan
PHD.txt:4682:frasang parragig pargan- parwar pargandan pargüd frég, parig frest- fréstadan fréstidan pargast fréstag fréb
PHD_pages.txt:4031: pargandan, pargan- [plkn-, plgn-du'               (P pr'gnd, N paragandan)]
PHD_pages.txt:6432:disperse pargandan.                     draw (pull) kesidan; (picture) nigar-;
PHD_pages.txt:6446:distribute baxtan, pargandan.           dry husk.
PHD_pages.txt:7494:row radag, rastag.                         scatter afSiindan, pargandan.
PHD_pages.txt:8639:                                              pargandan                 \~\~CU
=== PHD pušt
PHD.txt:551:pillagan [plk’n' | M pylg, N ~] steps, ladder. pim [pym] pain, pang, sorrow. ~gén [-kyn'] sorrowful. pir [руі | N ~] old, aged, ancient. ~ih: age. piring [pling | M pryng, (N pirind)] monochrome damask, pist [pst! | N ~] browned flour. pistag [pstk! | IN pista] pistachio nut. pišīz [pšyc | N ~] small copper coin, ‘farthing’. pēhišn [pwhsn'] corruption, decay. pēlāwad [pwPft! | М pwl'wd, N pēlād] steel. ~ën [-yn!] (made of) steel. pondik [pndk' | Ar. b/fundug] hazel-nut. por [pwl | N —] francolin. pēryētkēš [pwlyw(k)kyf = Av. paoiryē.tkaēša-| (one of) the first teachers of the Mazdean religion. ~ЛЬ : the primal doctrine of the Mazdean religion. pēst [pwst! | = M, N ~] skin, hide; bark, shell. mēn [-yn! | N ~in] (made of) skin. pēšīdan, pēš- [pws-yin' | N <] cover, put on, wear. ~išn: covering. potk [pwtk' | N ~] sledge-hammer. poxtan, paz- [APPWN-tn' < А V?ph; pwhtn', pc- | M pwxtn, N ~] cook, bake. рӧу- [pwd- | (P pwd-), N ~] run. ~iSnig : running. p6z(ag) [pwc(k!) | N pēz(a)] snout, muzzle. püdag [pwtk! | N pūda) foul, rotten. —ih: rottenness. 1puhl [pwhl | N pul] bridge. *puhl [pwhl] expiation, atonement; punishment. puhlénidan [ pwhlynytn'] cause to atone. purnāy [pwln’d] adult. purr (MALE < A mlh; pul | M pur, N ~} full. =-ģāh [-g’s] at the fullness of time, about to die. ~-тюаһ [-mh] full moon. —-rawišnih [-lwbsnyh] fullness. ~-sardag [-sltk'] of all kinds. --xwarrah [-G DE] full of glory. pursidan, purs- [pwrs-ytn' | M pwrs-ydn, N ~] ask. Vu re: Е ~iSn: question. — ~i$nig : responsible. pus [BRE < A br-h; pws | = M, N =] son. ~ar [BREI, pwsl | M pwsr, N ~] son. —yàn [pwsd?n! | M pwsy’n] womb. pušt [52001 | = M, N ~] back; support, protection.
PHD.txt:661:2xān [/?п! | P л?п] spring, source. хапар [BYTA < A рур; h'nR! | N хапа] = іхап. xandidan, xand- (*GHBHWN-yitn' < A V ghk, or У *ghqh; hnd-ytn' | (M xnyst), N —] laugh. xānīg [/?nyk! | M x?nyg, N xàni] = *xān. xar (HMRA < А hmr’; hl | N ~] donkey, ass. хаг [P1 | M ær, N ~] thorn. xar-buz [hibwe | M xrbwz] oryx. xar-g68 [higws | N ~] rabbit, hare. хаготапа [/PPwmnd] thorny. xār-pušt [/?Ipwst! | N ~] porcupine, hedgehog. xastan [hstn' | M xst, N ~] wound, injure. xašën [hsyn! | N хайл] (dark) blue. хауар [Pd(y)k! | N xdya] egg. ~-dés [-dys] oval, egg-shaped. xayüg [Ah )dwk! | N xayū] saliva, spittle. xaz [hz | N —] marten. xém [лут] nature, character. xëšm [?yfm, hfm | M xysm, N xifm] anger; the demon Wrath. --én [-ya! | M -yn) angry. xindag [hyndk' | M xyndg] ill, sick. ~th: illness, sickness. xir [C BW! < А sbw; hyl | M хут] thing, matter. xirs [hls | N ~] bear. xišt [Ast! | (P hystyg), N ~] brick. хбё [hwk' | N xwk, xóy] nature, character, disposition. x6n [DM YA < А dm’; һит! | M хоп, N хип] blood. xormā [TE A tmryn; hwlm’k' | N ~] date. xrad [hit! | M xrd, N xirad] wisdom, reason. ~ig, ~Omand [-yā!, тиа | N -mand] wise. xrafstar [hlpst] = Av. xrafstra-] reptile, noxious creature. xridan, xrin- [ZBNN-tn! < A V zbn| M xryd, xryn-, N xaridan, (xar-)] buy. xróhak [hlwhk' | N ~] coral. xrēs [DYLK A < A dkr’; hlws | P xrws, N xurós] cock. xróstan [Alwstn! | M xrwst] call, cry. xüb [hwp | M xwb, N ~] good. ~th: goodness. xuftan, xufs- [HLMWN-tn! < А У Ыт; hwptn', hwps- | М xwpt, N xuftan, xusp-] sleep. xūg [HZWL УА < А hzyr; hwk' | N ~] pig. xükar(ag) [hwkl(k') | N xūkara] hedgehog. xumb [kwmb! | M xwmb, N ~] jug, pitcher. xunak [hwnk' | M xwnk, N xunuk] happy; cool. xurdruš [kwldlwš, -dlpš = Av. xrwidruf] ‘with a bloody club’ (epithet of Xēšm, later misinterpreted as *ul-draff ‘*with raised banner’).
PHD.txt:4704:purrmāh Ku purrsardag 15 Qa» yes dahint roe to pusyān V 10 pusar ND 10 póstén V yen 10) póst we» 105 рап}, poz So panjah ay S ya) panjag, pēzag 13619 pos- = 74010 pūšīdan Wres“O ve pēšišn VUV puštībānīh «U ye) 43 «650105 pustiban т^” оу S ANA pušt VOU 199 puštag 1100010) püdagih ^t 5120
=== PHD frāz/frēstag
PHD.txt:170:abilag 5/4! | N ~a] blister. a-bim [bym] fearless. āb-kāmag [5A mk! | N ~a] a thick, sour soup. abnüs Pžēnws | (N ābnūs)] ebony. a-biy Pbwd] senseless. ~ih: senselessness. à abr РЫ, Séi | N ~] cloud. M bel abrang [ing | N aurang] glory, splendour. abrastan, abraz- [AP stn',SPc- | М ?br?st, N (afráttan), afrdz-] lift, raise. abraz [Pe | N afrāz] acclivity. abrēšom Pflyš(u)m | M? bryfwm, N ~} silk. ~én [-yn!] silken. abróxtan, abróz- ['piwhtn', ?phoc- | M brwxt, ?)brwc-, N afróxtan, afróz-] light, kindle, illuminate, polish. ~i$n(ih): illumination. āb-tazan Pftcn!] watercourse. a-bun [*dwx!] baseless, bottomless. a-burd-framān ['bwltplm^n'] disobedient. ~th: disobedience. aburnāy f(w)lnd, v. purnāy | N burnā] under age, child. ^h : childhood. aburnáyag [?A(w)/n’(d)yk'] child. abus [pws] (woman) having just given birth. “АҺ: childbirth. арив, -tan Pws, -tn! | M ’bwws, v. ábestan] pregnant. „il: pregnancy. abydxtan, abyóz- Phywhtn', ?bywc-] join, mix. āb-zan zn! | N ~] bath. labzar [el pel] M *6c*7, N afzār] instrument, means; spice. *abzar [6271 | M bail skill, power; powerful. „ūmand [-wmnd] skilled, able. abzāy-, —išn, у. abztidan, abzón [?pzwn! | M, J ”*bzwn, N afzün] increase, growth. ~ig [-yk!] increasing, expansive, bountiful. ~igih: bountifulness. abzüdan, abzáy- ['pzwtn!,^?pzd- | M ?bz'y-, N afzüdan, afzāy-] in- crease, grow. ~i$n: increase, growth. a-čār [cI] inevitable, Jee ~ag [-k'] compelled.
PHD.txt:347:~išn: help, assistance. ~išnig: helpful. frāz [рге | M prz, N faraz] forth, focwarile ~ abgandan: throw forward. ~ 82: after, apart from. ~ bréhénidan: fashion forth, create. ~ griftan: undertake, perform; appoint, decide. ~ 6: up to.
PHD.txt:1436:create af(u)ridan, (frāz) brēhēnīdan, dādan, tāšīdan; (daevic) kirrén- idan.
PHD.txt:3090:perform frāz griftan,kardan,wizārdan.
PHD.txt:4171:up to frāz б.
PHD.txt:4718:[154] 1-2pešag 1 V. pēšpārag S eoo petyāragīh AS dax sa) petyārag ҳу 10 paydāgīh ^0 з» 10303 paydāgīh- = 95747 №0 paydagihistan 1152294 3” е 0 paydāgēn- = 527310500 paydāgēnīdan ММ 8” 5 05 paydag 15? ye» о) paygām -È ve os paygāmbar Sye Yeso petitigih A3 4) M 4290) petītīg 14) 95 1050) petit 12d уез 0› **pid we es panāh ^U? 103 panāhīh AY 10) "oul PITT puhlén- = "yes 10) puhlénidan ure rne 19у frāz erie pēhišn IMO” tay poxtan ure 125 nem! 519
PHD_pages.txt:2393:frestag [plystk l I M prystg, (N firilta)] apostle, angel.
PHD_pages.txt:5926:alert gubrag, wigriid, zenawand.          apostle frestag, paygiimbar; v. pro-
PHD_pages.txt:5955:angel frestag; guardian ,...., frawahr,   army gund, hen, laskar, spiih.
PHD_pages.txt:8670:franaftan                    "~Cb'~Q)    frestag                     \~~QJ
```


## [2026-09-14T00:52:10.360Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SOD frtr\"; grep -n \"frtr\" SOD_pages.txt | head -20; echo \"=== SOD leaf for p155 = 155+66=221\"; awk 'BEGIN{RS=\"\\f\"} NR==222' SOD_pages.txt | head -30",
 "description": "Grep Gharib Sogdian dictionary for frtr"
}
```


### [2026-09-14T00:52:11.400Z] TOOL RESULT

```
=== SOD frtr
5147:                                                                     (o)fratar =*frtr, prtr1
14810:                                                                                                                 frtry>
14855:       glory, majesty, fortune                                       3926 frtr M, C                              y# <yj±j ij^>
14862:       GMS 1132                                                      3927 frtrstr   M
14869:                                                        eJUi-^       3928 frtrwny       C
14874:       GMS 1273; W-Lii                                               3929 frtry' M, C                               J^J^j3J
15132:        1974 p233, 14.15                                                     f(a)tarune =*frtrwny
15135:        f(a)tar ©<*fra-tara ^'ft'r, frtr                                      GMS 473; fwtrwny, GMS 473 n 1
24514:                                                                    fratar ©<Av. fratara =»frtr, >Prtr
24559:     frataryak ©La =*frtry>
=== SOD leaf for p155 = 155+66=221
                                                                                                                       156
 fr8yp-

 3930 frByp-      C                            oJJt*JJ^j>        3943 f rwxspS M               (^J> JjL*)«U ^U-oU- jl Ji
       fra9/5cp (frtyp-) ©<*fra-daipa =*ftyp-                         froxspad ©<Skt.- prost [ha pada% Khwar. frxsbyO
       (to)lighten, (fo)flash, (ro)shine                              lunar mansion
       GMS 318 n 2; STi 65.6; Sund. AoF 6V6 p235;                      GMS 481, 1142; Hen. JRAS 1942 p242n 1
         STSC; C2, 54V25; BSTii 895.55; AVS 166                  3944 frwy B                               L&-«-Aj~«~*J
                                                                      farwe/i ? =>prwy, Prwy
 3931 frtyp- => frGyp-
                                                                       illusion
 3932 frwq     M                                   y^^jj
                                                                       BSTBL, Dhy. 346
      frok (frwwq) ©<*fra-rauka
      brightness, glow                                           3945 frwycy C                                     ^ySj
      Sogdica. 29.3; GMS 319                                           frawici ©<frdwisci =»fr*wyscy, frNvycy h,
                                                                         P^wscyCh)
 3933 frwra =* Pr'wm
 3934 frwmcyq   C                                                      forgetting, oblivion

      frumcik ©pi. -/        v                                         +wn- nto forget" C2, 48V 20, 94V 14
                                                         cr-JJ
      Roman, Byzantine                                           3946 frwy$(6)- M                      j&f ^^ijju-j
      STi 57, 4.42; GMS 1016                                           fraweS     ©<*fra-waida\ fwaid- ^prw'yS-,
 3935 frwmyq      C
                                                                       0o)reach, (to)h\t (an illness), (/o)af flict
      frumik ©ob. pi. -ty ^Prwm'yk                       <SJJ
                                                                               y5;- Hen. BSOAS 11, 484; Gersh. AHM
                                                                       GMSPrw*329                                      263
      Roman, Byzantine
```


## [2026-09-14T00:52:12.664Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SNS\"; grep -n \"pargand\\|parward\\|pardax\\|pust\\|frataran\\|paristi\" SNS_pages.txt | head -20; echo \"=== NYB\"; grep -n -i \"pērāmōn\\|pēramōn\\|parwardan\\|pargandan\\|pardaxtan\\|pušt\\b\" NYB_vol2_glossary.txt | head -20",
 "description": "Grep SNS and Nyberg"
}
```


### [2026-09-14T00:52:12.737Z] TOOL RESULT

```
=== SNS
1808:                                                                                                                       (%»j'j :i)     .oi-yT.        flbustan/apustan:               m««i a>>
11475:                                                                                                                               I       Spustan: \\\**>ly » rP-»-»l
15647:yBzdahrgarlh 334/15      zan x apustan 288/13
15890:petrSt 142/14              pust 139/5-10                     radlh 226/5            rSsag 234/18
16535:Sgrift 88/16                apustan 24/7                            Svar3d 305/16            abaz axezend 220/11
=== NYB
1357:dru-puštēh [dipwStyh] stronghold, citadel 11795, — Paz. drūpuštī; dru- ‘firm’: v. druyist.
1588:be a secondary form of ?pr'yc-, pr'yc-, Gauthiot 126, Benveniste, GS 19). Cf also Dhabhar, PYV, Gl. p. 80. — This vb. coincides graphically with pardaxtan par- dac- [pldhtn! plde-] q. v.; this has caused some confusion: 7619 Paz. has frēž where- as only pardac (marked d in Cod. K) is appropriate; SGV III, 24 West, followed by de Menasce, conjectured pardacısneh, rejecting frež- which is, however, the adequate vb. there.
2277:ke [MNW] with encl. MNW-m = ké-m, MNW- = kē-š ete.; MNW-c = ké-c: A. interrog. pron. who? whom ?: én rētak kē hast? 161”; emphasized kē hàn he? who art thou, say? 561%; as cas. obl.: kē pat panāh kunom? 749; ke ax"eš hom? to whom do I belong? 624; én zanišn ké (ag.) kart? who made this deadly shot? 323; — gen. + ke: En pus + kē hast? whose son is this? 1621; or hàn 4 ke: ruvan... hàn t kē...? whose soul? 31?3; — governed by a prep.: hac ke? nazd ke? tài ke? ete. ; — indirect interrogation may be introduced by ku: gob ku to hac fradandän i ke hah 1517-18; without kū: (én-ic dine) hac pusa- ran...ı man ke zīvēt u kë mīrēt 219-19; nē (Gkah hom) i ke hàn 574. — B. rel. pron. who, which ; with pronominal antecedents : man ke, tē ke, šmāh ke, či ke, čišan ke, -$...ke, han (kas) ke, har (hàn) ke; hec (kas) ke both in a positive (6417-18) and a negative (11817-18) sense; 1. used as cas. rect. and cas. obl: (subj.) asvdr-é nest ke ... ētūn cigon to 1519-316; (dat.) (Kävul) ke Mihr u Mah pat pušt hah K. over which Sun and Moon keep guard 317%; (agens) Krisäsp ke Dahāk vanit K. by whom D. was vanquished 1064-5; — its syntactic function may be marked by an enclitic referring to the antecedent: (hu- nušk + Gana Menoi) kē-š ciš-ic pat poc nest (the progeny of the Evil Spirit) for whom there is nothing to furnish an ex- cuse 1021-?; but dastavar ké-§ guft ku there was a theologian who said 1018, also but ké-§ guft ki someone has said (taught) that 103? ; Gišān kē-šān Yam kirrenit those by whom Y. was cut to pieces 10145; — the gen. is regularly ex-
2933:pardaxtan
2946:pardaxtan [pldhtn'] pardac- [plde-] to run after, or to run to an end: 1. to strive for (6): avis névak pardac strive well for it! 7616 (Paz. friz = frēc [plyc], g. v., Skr v. sadrsam sädhu vardhaya; however, Cod. K has explicitly pidc with a marked d ; this reading pardac, accepted already by West, suits the context bet- ter). — 2. to be accomplished, finished, cf MPrs w "z ’wd dyw'n zd "wd prdxt mnd
2948:pardaxtan
2951:and Covetousness and the devils re- mained slain and finished (destroyed) M 4708-7 (S); to be ready with, to get rid of (hac): Vištāsp ka hac kārēcār i apāk Arjāsp pardaxt būt as soon as V. had got to the end of the war with A. 1088; [bë ~ to be taken away from (hac), to be refused: xYarišn hac zan i dastän bē pardacét food is taken away from, refused to, a menstruous woman Vd. 16° comm.]. — From Olr pari + tac-, v. tacitan; Av. (625) pairi-tac- ‘to run round (a p.)’; (Verbum 227: para + tac-, not probable) ; Paz. pardazasn- ‘completion, perfection’ ; NP pardaxtan commonly supplanted by the caus. parddatan, pt. pardaxtah com- pleted, finished, disengaged etc.; MPrs v. above.
3187:pušt [pwšt'; Ps. pwšty] the back 1112. 2521. 29%. 6513. 1287; pat ~ tacitan to run after, to pursue 311%; pat ~ bütan to protect, to be the protector 31°; ~ kartan 6 to protect 872%; — pl. eas. obl. ~-dn: pat puštān i Vištāspān for the (acts of) protection of the Vistasp dynasty 9514. — MPrs pws, NP pušt < *pršti-; Av. (878) paršta-, parsti-, v. s. v. puštēpān.
3188:*pušt-aspān [pwSt’sp’n'] 1118, v. next w.
3189:puštēpān [pwštyp'n'] “protector of the back" = life-guards, pl. cas. obl. in ~-an sardär the commander of the life-guards 11911, — pušče cas. obl. of pušt (g. v.) + pan; the Sass. title is transcribed in Arm by p‘ustipanac (gen. pl.) (or p*usti- pan) satar ; besides, Arm has the Prth. lw. pašt-pan “protector, defender’ < *parésti- päna- (v.s. v. pušt); NP pustibän, pustvän. — pušt-aspān 1118 is an old misreading (Paz. pustaspän Mx) of pustepän, cer- tainly due to wrong association with asp ‘horse’, as is suggested by the spelling pwšt'sp'n'; moreover, in the BP writing the ligature -yp- is very often formed so as to coincide with -sp-. Read conse- quently 1118 puštēpān sardär = the Arm. form just quoted.
3190:puštčpinakčh protection, defence 8514. — Paz. puštaspānī, v. above.
3689:tacitan [teytn'] to run: api-m cand 4 nem roc pat pušt hamé tacit hom (for tacit-om) almost half a day (he was run after by me =) I ran after him 311? (cf s. v. kar- tan); be tacit pat oš han mat *cautiously (v. s. v. 68) his mother ran to him 48?9, 217.49 5019; pčš tacit ran before, got ahead (of the others) 494-19, — Av. (624) tak-; M Prth tc-; MPrs čz- (S); Paz. 0ajü for tazak (tajäk; Aog. 77); Verbum 169; Ghilain 50. Cf täxtan.
4245:to Z. through the line of his maternal grandmother 3619-11, cf 3817-18, — 2. intens. of vitartan: vitartan % Cinvat puhl to cross the Ch. bridge 64!?; the arrow ditikar sok bé vitärt pierced through to the other side 371, pat pušt be vitārēt (pres. hist.) pierced through and came out through the back 292-3, pat dil be vitārēt penetrated into the heart 2521-22, — MPrthPrs wyd’rdn w(y)d’r-; MPrs also pt. wd’$, Verbum 192; NP guöärdan or guöästan, guóür-.
5274:pāra-: pārak Para-data-: Pēš-dāt parena-, perona-: parr paresu- (peresu-): pahlūk paršta-, paršti-: pušt pasca: pas
5388:pairi-tac-: pardaxtan
6106:pwlwd: polavatčn pwr: purr pwrsydn: pursitan pws: pus pwst: post pwšt: pušt py'dg: padatak pyd, pydr: pit pyd’g: paitak pyg: padak pygm: paitäm pym’n: patmän pymwen: patmöcan pymwxtn, pymwe-: patmöxtan pyr’yg: pairayak pyrwz: péroz pyšwb'y: p&söpäi pyšyn: pēšēnīk Pyš, pyšyy, pyšyh: pēš pyw’c-: patvac- pywn: patvand pywst: patvastan
6535:drün-: drütan drūpuštī: drupuštēh drūž-: druxtan drūž: druž
6769:patmoxtan pašsār: patisär padvazed: pat-vac- padyavand- patiyavand pšč: pad paēdā, paidà: paitäk pačma(n): patman pačvand: patvand pačvastan: patvastan pahalim, pahlum : pahlom paharčxtan, paharčž-: pahrčxtan parastidan: paristätan pardazašn: pardaxtan pasand: passand pasaxt: passaxt päsux: passaxu paščman, -màni: pašč- mančh patit: patit patkàr: ~ päya: pädak péda: paitäk pédabar: paitäm-bar pčrož: pérdz pēš: ~
6772:agar: pēšakkār pēšavāē: pēšēpāi pēšiār: pēšārvār pēšīnaga: pēšēnīk phālum: pahlom pīm: pēm pradim: fratom puh(a)l: puhl pulādīn: pēlāvatēn pur: purr pursīdan: pursītan puštaspān: puštēpān
7313:pardaxtan, pardäxtan: pardaxtan
```


## [2026-09-14T00:52:26.000Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==221' SOD_pages.txt | sed -n '1,60p'",
 "description": "Print Gharib page 155"
}
```


### [2026-09-14T00:52:27.102Z] TOOL RESULT

```
                                                                                                        mMmmmmm           ^^WHiiiiiHiili&




 155

                                                                     3919 frnxwndy(y) M
        GMS 565, BBB; trans, pret. frrritd'r-. Hen. Tales.
          467.41; frmWr-, Sund. AoFviii 1981 p214;                         farnxunde (prnywn8y) ©<Av. xvardtxahvant
                                                                                                                 frtry>
          AVS 91
                                                                           BBB; GMS 939, 1092, 1241; frnxwnd, Frag. Lcn.
 3909 frm'tyty) M, C                             jjUJ<ij*J                   77R6
      framate ©pp. nom. n. -/w>; pi. -t
      ordered, commanded                                                   gloriousB, * M
                                                                     3920 frpws-                                     0*j<j=^W
        BBB 729; GMS 849; C2 gloss.                                        frapas (frp's-) ^Prp's-
                                                                           (^)throw, (/o)beat
 3910 frm'y-      M, C                     (Jj> s^ j*)o>j*J
                                                                           BSTBL, Dhy. 17, 134; Hen. JRAS 1944, 143.24
      framay      ©<*/ra-maya-         ©impf. f^rrty
          -^frnVt-, prm'y-1, Prm'y-                                  3921 frp's- =» frp»s-
        OcOorder, (r^)command
                                                                     3922 frst- M                           d>J'^j><d>J'Js-*l
        BBB; GMS      327, 565; C2, 2sg. impv. frm'y,                     frast ©<*fra-rasta       ©pt. st. ^fr'st-, Pr>st-,
                                                                            fryz-, frsty
          "please" S W, C2 p57.15LAVS 91
 3911 frm}ync        C                                                     0o)settle, (to)makc straighten
      framene        ©f. pres. part,                                       BBB; GMS 319 n 1; S W, C2 n pl32; AVS 128
      mistress
                                                                     3923 frst'h                              ^>><c-iJOi^.
                                                         _yLi-:U»-
        C2, 13R30
                                                                           frasta ©f. pp. ^fr'yz-, fr'st-, fr^t'y
                                                                           settled
                                                    osj'oljis
3912 frmrz-       M
                                                   Of                      Hen. Talcs. 466.1, 468 n 2; GMS 884, ( +/?vw,
        framarz, framrz ©impf. framrz
        (fo)spoil, (/o)dcstroy                                              potent, pass. )
        GMS 327, 529; AVS 132                                        3924 frsty C                                    o^^lj
3913 frmst-      M                                      J^j                frastc ©ace. -tw\ pi. -tyt =*fryz-, frst-
       framast    ©<*fra-masta ©pt. st. -^fr'mrz-,                         upright, straight
                                                                           C2, 61R 22, 52V 10
         Prm'yst-
       (/o)spoil                                                     3925 frtp55 M                                        Ub«>tfT
       GMS 147, 327, 529
                                                                           f/ParatpaB ? (brtpd) ©*abi-(fra-rata- paOa
                                                                             ^PrtpS
3914 frn     M, C                           j&*±y*-<.jii<j
                                                                           informed
       farn ©<Av. xvardnah OP *farna           ©ob. ~y
         =»prn\ fn                                                         Sund. MSP p45

       glory, majesty, fortune                                       3926 frtr M, C                              y# <yj±j ij^>
       GMS 526; W-Li, ii; BBB; Tales. 470.50; BSTi 189                     fratar ©<Av. fratara ©pi. -t =»ft'r, prtr1, }Prtr
3915 frnpry      M                                                         more, better
                                            (jj^)jjtJtJ^AJ                BBB el2; GMS 437; STi 8.11, 10.11; C2, 120V2,
       farnPare =»pnu3rch
```


## [2026-09-14T00:52:40.139Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"پیرامون\" BQT_v1_pages.txt | head -10; echo \"=== leaf numbers\"; python3 - <<'EOF'\nimport re\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if 'پیرامون' in p:\n        print('leaf',i, p[:120].replace('\\n',' '))\nEOF",
 "description": "Find piramun in Borhan vol 1"
}
```


### [2026-09-14T00:52:41.305Z] TOOL RESULT

```
2868:ازطرف دیگر بحث وجدال واثبات وابطالبسیاردر پیرامون آن کتاب
18778:بر 9و د « بروزن‌سردوزءاطراف‌وپیرامون
18804:آموزء بمعنی پیرامون و اطراف دهان باشد ٩‏ .
24495:۱ - مرکب از : پر - اوستا :025 ( پیرامون ) + چن (از : چیدن ) جمعاً یرامون
24880:۲ م رکب از : پشوند ۳8۳ ( پیرامون ) + 0 > 28 (کندن) . رك : کندن .
25111:۴ اوسئا 08161 ( 0272 ۲۳ ۷22 (در پیرامون پریدن ) قی:
28515:تافول » بر وزن خافود ۰ پیرامون
=== leaf numbers
leaf 97 هشتاد و ه تقایص برهان ازطرف دیگر بحث وجدال واثبات وابطالبسیاردر پیرامون آن کتاب ابجاد شده. مرحوم محید علی تر بست » کتاب 
leaf 480 بر فشا ندن‌ذست ه کنابه ازرقصدن بر قنجاك » بنتح او و سکون ثالی و فتح ثاكث و سکون نون و فتح جیم و سکون کاف : میاهیو کرانی 
leaf 603 پر یی ۱ ۰ بر وژن پروین ؛ حساری باشد که از خاروخللاشه وشاخ درختان بر دورباغ وفالیز و کشت زارساز ند وچوبهای‌سر‌تیزوخاربرا 
leaf 611 - پر۳ - ۳۳ کی هر کم -_بفتح‌کاف تازی بروزن پرچم؛ پر و لك - باعاف فارسی بروزن‌مفاوك, نا چیز شده و از کار رفته و کار افتاده
leaf 615 و قری وییم وباگك٩‏ -و سروب رکه را نی زکوین و بمعنی داشتن (۱) و فرات - و پرداخت - و پرورش - و پرواز هم آ مده‌است. رواد ۲ 
leaf 689 39۳9 تانبول- بن بای ایجد و سکون واو ولام» : بمعنی تامول است که ب رکه‌پان باشدو | نرا با فوفل 3 خورند ۴ ۰ تا ثك ه بر وزن
```


## [2026-09-14T00:52:51.671Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\ntargets=['پرگار','پرتو','پرداختن','پروردن','پراکندن','پرگندن','پرستیدن','پردیس','پالیز']\nfor i,p in enumerate(pages):\n    if i<560 or i>700: continue\n    for w in targets:\n        if w in p:\n            print('leaf',i,'~p',i-223,'has',w)\nEOF",
 "description": "Locate Borhan vol1 entries"
}
```


### [2026-09-14T00:52:52.832Z] TOOL RESULT

```
leaf 581 ~p 358 has پالیز
leaf 592 ~p 369 has پرتو
leaf 599 ~p 376 has پرتو
leaf 603 ~p 380 has پرتو
leaf 604 ~p 381 has پرداختن
leaf 605 ~p 382 has پرداختن
leaf 611 ~p 388 has پرداختن
leaf 614 ~p 391 has پرتو
leaf 616 ~p 393 has پرداختن
leaf 616 ~p 393 has پرستیدن
leaf 617 ~p 394 has پروردن
leaf 663 ~p 440 has پراکندن
leaf 664 ~p 441 has پرداختن
leaf 678 ~p 455 has پرتو
leaf 686 ~p 463 has پرتو
leaf 694 ~p 471 has پرتو
```


## [2026-09-14T00:53:01.826Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in [603,604,611,615,616,617]:\n    print('='*20,'leaf',i,'~printed p',i-223)\n    lines=[l for l in pages[i].split('\\n') if l.strip()]\n    # print lines that look like footnotes (contain اوستا or پهلوی or - )\n    for l in lines:\n        if 'اوستا' in l or 'پهلوی' in l or 'مرکب' in l or 'رك' in l or 'فارسی باستان' in l:\n            print(l.strip())\nEOF",
 "description": "Print Borhan footnotes on relevant leaves"
}
```


### [2026-09-14T00:53:03.107Z] TOOL RESULT

```
==================== leaf 603 ~printed p 380
۱ - مرکب از : پر - اوستا :025 ( پیرامون ) + چن (از : چیدن ) جمعاً یرامون
۴ یز بممنی شمشیر. رك: لفت‌نامه . ۴ - از ساخته‌های دساتیر « غاب ۱ : 4۷ 4
د فرهنکگ دساثیر ۷۲۳۸ > . ۴ رك : پریدن .
==================== leaf 604 ~printed p 381
و ترك دادن‌باشد - و بممتیآرامتن - ومشفول
کردیده - و انگیخته. وتركك داده- ودور کرد
۳ - رك : پرداختن :
==================== leaf 611 ~printed p 388
۲ م رکب از : پشوند ۳8۳ ( پیرامون ) + 0 > 28 (کندن) . رك : کندن .
۴ ر: پرماسیدن ویرمای . ۵ رك: پرماسدن (حاشیه) . رك: برماه .
==================== leaf 615 ~printed p 392
۴ - هرن *بروار» فارسی رابمعنی اصطبل آورده و گوید: دراوستا 02171۷2۲202 ۵ قی :
2 . 21۴1 (باروء طوبله)؛ پهلوی ۳3۲۷27 ودرحاشبه امن‌یت خاقانی شروانی راکه برولررا
==================== leaf 616 ~printed p 393
==================== leaf 617 ~printed p 394
```


## [2026-09-14T00:53:15.836Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && python3 - <<'EOF'\nt=open('BQT_v3_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint('nleaves',len(pages))\ntargets=['فریاد','فرستادن','فرهنگ','فروردین','فرمان','فرجام','فروختن','فروهر','فرامرز']\nfor i,p in enumerate(pages):\n    hits=[w for w in targets if w in p]\n    if hits and 225<=i<=290:\n        print('leaf',i,hits)\nEOF",
 "description": "Locate fa- words in Borhan vol 3"
}
```


### [2026-09-14T00:53:16.913Z] TOOL RESULT

```
nleaves 721
leaf 227 ['فرهنگ']
leaf 229 ['فرهنگ']
leaf 230 ['فرهنگ']
leaf 232 ['فرهنگ']
leaf 233 ['فرهنگ']
leaf 235 ['فرمان']
leaf 236 ['فرهنگ']
leaf 238 ['فرهنگ', 'فرمان', 'فروختن']
leaf 241 ['فرهنگ']
leaf 242 ['فرهنگ']
leaf 243 ['فرهنگ', 'فرمان', 'فرجام']
leaf 244 ['فرهنگ']
leaf 245 ['فرهنگ', 'فروردین']
leaf 246 ['فرهنگ']
leaf 248 ['فروردین']
leaf 251 ['فرهنگ']
leaf 252 ['فرستادن']
leaf 253 ['فرستادن']
leaf 254 ['فرهنگ']
leaf 255 ['فرهنگ']
leaf 256 ['فرهنگ']
leaf 257 ['فرهنگ']
leaf 259 ['فرهنگ']
leaf 260 ['فرهنگ', 'فرمان']
leaf 261 ['فرمان']
leaf 262 ['فرمان']
leaf 263 ['فرهنگ']
leaf 264 ['فرهنگ']
leaf 265 ['فرهنگ', 'فروختن']
leaf 266 ['فروردین', 'فروختن', 'فروهر']
leaf 267 ['فروردین', 'فروهر']
leaf 268 ['فروردین', 'فروختن', 'فروهر']
leaf 269 ['فرهنگ', 'فروختن']
leaf 270 ['فروردین', 'فروهر']
leaf 271 ['فرهنگ']
leaf 272 ['فرهنگ']
leaf 273 ['فرهنگ']
leaf 274 ['فریاد', 'فرهنگ']
leaf 275 ['فرهنگ']
leaf 279 ['فرهنگ']
leaf 283 ['فرهنگ']
leaf 284 ['فرهنگ']
```


## [2026-09-14T00:53:23.896Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && python3 - <<'EOF'\nt=open('BQT_v3_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in [235,236,237,238,252,253,266,274]:\n    p=pages[i]\n    print('='*15,'leaf',i)\n    print(p[:200].replace('\\n',' | '))\n    for l in p.split('\\n'):\n        if 'اوستا' in l or 'پهلوی' in l or 'مرکب' in l:\n            print('  FN:',l.strip()[:220])\nEOF",
 "description": "Print Borhan v3 leaves with footnotes"
}
```


### [2026-09-14T00:53:24.983Z] TOOL RESULT

```
=============== leaf 235
[pdf page 236] | oN Efe |  | ودبوث هم حست - و بزبان ‎blk‏ خوردلی | و طمامی باشد که در دستمال (۱) بسته از جایی | بجایی برند - و بیعنی دستور هم بنظر آمده |  | است . |  | قدرو نك ‎bw‏ رای قرشت (۲) ‎ogy‏ | ‏بروزن(۳)زتبورلك س
  FN: ‏جلو,بسوی‌جلو وغیره؛ چنانکه‌در کلمات: فرخجته. قرسوده» فرمان؛ درپارسی باستان واوستا ‎fra‏
  FN: ‏پهلوی £18 « ارمنی ع - ۱۲۳۵, ‎jae‏ پاستان ‎hal. hil - 6.55% pra‏ « استق ۰۸۰۷ .
  FN: ‎fara - ۱‏ پیشوند ( & بسوی .5( = مانکرت ‎prak‏ ( پیش . جلو ) اوستا
=============== leaf 236
[pdf page 237] | فرابرز | هست - وبمعنی بر و در ‎ee‏ علی‌وفی‌خوانند | - وبمعنی مه‌ومجموع- وزیادت - و اخذ کردن | و ستایدن آهده است - و با تشدید ‎«gt‏ | ‏بلفت‌عربی بمعن ی کر بختنو کربزان شدن‌باشد ۷. |  | فرا برد ‎cae‏
  FN: ‏۴ - اوستا ‎eye) frathah_‏ پپنا) . پهلوی ‎frah‏ .3 : |۵6 .
  FN: ‏( کشاد . عریض ) « اسشق ۸۱۰ ۰ . درپهلوی 675 که ۳21۷] نوشته شود » از پارسی باستان
=============== leaf 237
[pdf page 238] | سووعوت | قراخ ‎gi‏ - کنابه ازبتتابوسبیل | رفتن باشد . | ‎O18‏ و ۱ - بنتهرایبی قطه,تمجیل | و شتاب رونده را گویند - و کنایه از کی است | که ازحد خود بیرون رود- ومسرف وعرزه‌خرج |  | ,\ نیز گویند ۳ - وم ر
  FN: ورك: بشتپا ۷ ص ۱۷۹ متن و حاشیه ؛ نب ر کلص ۷۲ - ۷۳ ‎aS‏ : پهلوی ۲۵۲۵۵ ‎cool)‏
  FN: ۵ فراخی - بفتح اول ‎le‏ فراخطی ‎el)‏ مصدر ) < ‎EL‏ فراخنا. پهلوی
=============== leaf 238
[pdf page 239] | فراز | فلاطرن , کسیرا و چیزیر! کویند که نه بطریق | ‎He THe‏ پس رود. یمنی روز به نباشد وروزبروز | پي رود . |  | ‎ILS‏ ۷ - بروزن نماز . چندممنی‌دارد: | ۱- پهن شده و پخش کردیده باشد . ۲ - بسته | و کشاده
  FN: ‏۱ - پهلوی ‎frie‏ ( بهپیش , جلو . باینجا ) از اوستا - ‎frank‏ « بارنولمه۱*۲۵*.
=============== leaf 252
[pdf page 253] | ۱ ws |  | فزدو ۱ ‎peo‏ اول و سکون نالی | ‎gly city‏ کشیده. بمعنی‌فرزبود اس تکهحکمت | ‎OT, atk‏ دریافتن افضلمملومات‌است‌بافضل علم. |  | رده = بفتح اول‌بروزن(۱)هرزه‌بمعنی؛ | فرژد است که نوعی از ,سبز#تر
  FN: ‏۱ = فرسپ » پهلوی ‎frasp‏ . اوستا . ‎fraspat‏ . ممنی ‎ysl Ls‏ معین نیست .
  FN: ‎frastatan ‏رکزی )۰ پهلوی‎ Bnd ‏بکسر اول و دوم وفتح ششم ( در‎ - ole se
=============== leaf 253
[pdf page 254] | ‎aah Nee‏ فرستاف |  | ‏فرسطوت ۴ ‎phe abs‏ وزن | تفق ‎oS‏ بلت‌رومی قبان راکوبند وآن ترازو | ‎sale‏ است که چیزها بدان‌ستجند ووز نکنشد؛ | و باين معنی بجای طای حطی (۱) نای قرشت‌م | بنظر‌آمده است . |  | ‏فر
=============== leaf 266
[pdf page 267] | فرود | گوبند - و بمعنی افروخته هم آمده ‎٩‏ است که | ف‌وزان و درخشان باشد + |  | فر و۵ = بفتح ‎Jol‏ راك مجهولبروزن | ‎(hope‏ پسس سیاوش ب نکیکاوس بوده - ونم | اول برشته و بربان کرده باشد ۳ - و بکسر | ‎
=============== leaf 274
[pdf page 275] | Age ed |  | باشد . |  | فریاد خوان- با بای حطی .کنابه | از دادخواه و مظلوم باشد + |  | قر یپ ۱ = اول بروزن ‎Ke‏ | ‏بمعنی‌عشوه ‎ath Cry‏ وغافل‌شدن‌بخدعه_وغافل | کردن‌بخدعهرا نیز ‎aii‏ وطلم‌راهممیگوبندچه | ف
  FN: ‏دایر ۷۵۹ . ۷ ‎cae ty‏ هریز » ورلك: فژیژء فزژ؛ ۷ - پهلوی ۳۳6100 ,اوستا
  FN: ‎Oo‏ فری - ‎SG‏ اول » ازاوستا - 87208 ( دوست. محبوب ) ۰ ‎cae‏ باستان- ‎priyd‏
```


## [2026-09-14T00:53:47.689Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && python3 - <<'EOF'\nt=open('BQT_v3_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in range(234,282):\n    p=pages[i]\n    for l in p.split('\\n'):\n        s=l.strip()\n        if ('اوستا' in s or 'پهلوی' in s) and any(w in s for w in ['fravashi','frava','frawa','fravar','frayat','frad','fram','fraj','fraw','fro','vaxs','vax','frax','frahang','fraθ','frang','frya','fri']):\n            print(i, s[:200])\nEOF",
 "description": "Grep Borhan v3 footnotes with Avestan forms"
}
```


### [2026-09-14T00:53:49.144Z] TOOL RESULT

```
238 ‏۱ - پهلوی ‎frie‏ ( بهپیش , جلو . باینجا ) از اوستا - ‎frank‏ « بارنولمه۱*۲۵*.
240 ‏پهلوی ‎framésb_‏ ( از 2 بردن ) , پازند - ‎woe , farmdsh‏ باستان ۳0875-4۳8
240 هرن وهوبشمانگوید : فرامش پهلوی باید از _ ‎framush‏ ۵ از - ‎framursb‏ © تاشی ‎ous‏
265 ‏۴ - اوستا - ۰5۲۵۷2۲۵۵9 - ۲2۷۵۲۵ , پهلوی ‎su fravar‏ « فروارنه »
265 ‏۵ فر وختی - بضم اول ودوم وفتح پنجم ( درزبان کنونی ) ؛ اوستا ‎ofra +vaxsh.‏
268 ‏۴ - رك : فروردکان . ۴ - پهلوی ‎fravartin‏ مأخون از پارسی باستان
270 ‎٩‏ - پپلوی ۲۲8۷8۳۲ . ابرانی ‎ofravarti_ ott‏ . اوستا -62۷25/11/:بارتولمه
```


## [2026-09-14T00:54:03.076Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && python3 - <<'EOF'\nt=open('BQT_v3_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nimport re\nfor i in range(234,282):\n    p=pages[i]\n    for l in p.split('\\n'):\n        s=l.strip()\n        if ('اوستا' in s or 'پهلوی' in s):\n            print(i,'|', s[:170])\nEOF",
 "description": "Print all Avestan/Pahlavi footnote lines in Borhan v3 fa- section"
}
```


### [2026-09-14T00:54:04.152Z] TOOL RESULT

```
235 | ‏جلو,بسوی‌جلو وغیره؛ چنانکه‌در کلمات: فرخجته. قرسوده» فرمان؛ درپارسی باستان واوستا ‎fra‏
235 | ‏پهلوی £18 « ارمنی ع - ۱۲۳۵, ‎jae‏ پاستان ‎hal. hil - 6.55% pra‏ « استق ۰۸۰۷ .
235 | ‎fara - ۱‏ پیشوند ( & بسوی .5( = مانکرت ‎prak‏ ( پیش . جلو ) اوستا
236 | ‏۴ - اوستا ‎eye) frathah_‏ پپنا) . پهلوی ‎frah‏ .3 : |۵6 .
236 | ‏( کشاد . عریض ) « اسشق ۸۱۰ ۰ . درپهلوی 675 که ۳21۷] نوشته شود » از پارسی باستان
237 | ورك: بشتپا ۷ ص ۱۷۹ متن و حاشیه ؛ نب ر کلص ۷۲ - ۷۳ ‎aS‏ : پهلوی ۲۵۲۵۵ ‎cool)‏
237 | ۵ فراخی - بفتح اول ‎le‏ فراخطی ‎el)‏ مصدر ) < ‎EL‏ فراخنا. پهلوی
238 | ‏۱ - پهلوی ‎frie‏ ( بهپیش , جلو . باینجا ) از اوستا - ‎frank‏ « بارنولمه۱*۲۵*.
240 | ‏پهلوی ‎framésb_‏ ( از 2 بردن ) , پازند - ‎woe , farmdsh‏ باستان ۳0875-4۳8
240 | هرن وهوبشمانگوید : فرامش پهلوی باید از _ ‎framush‏ ۵ از - ‎framursb‏ © تاشی ‎ous‏
240 | ‏© فراوای - بفتح‌اول . اوستا ‎fravdn(g)p?‏ ( افزونی « بیار ), کردی ‎ferawin‏
242 | ‎fraybut ۰ ‏مناعت ؛ تکیر « تاوادیا ص۱۸۱‎ caw fre - DOL ‏در پهلوی‎ ٩
242 | ‎= frapth sale < ‏رك:فربود . ۴ - ازاوستا -2 2۳00100۷ = فربی‎ - ۴
247 | آذر کیوان . 6 معرب از ‎lal‏ . در اوستا دوبار ‎Lk,‏ ۳8171-02628 بر میخورم
247 | ‏۵ فردا - بفتح اول وسوم پردا («.م.)؛ پهلوی ‎VN Sy rfratak‏ شهمیرزادی
251 | ‎POU ©‏ -بفتح ‎pind wees pads!‏ کزی بکرپنجم). پهلوی1722808161
251 | ‏۵ فرز ند - بقتح‌اولوسوم ؛ پهلوی ‎frazand‏ . ایرانی باستان - 4 ۲82210]دبارتولمه
252 | ‏۱ = فرسپ » پهلوی ‎frasp‏ . اوستا . ‎fraspat‏ . ممنی ‎ysl Ls‏ معین نیست .
252 | ‎frastatan ‏رکزی )۰ پهلوی‎ Bnd ‏بکسر اول و دوم وفتح ششم ( در‎ - ole se
254 | در پهلوی هم گذارند وآن شش قبضه است یعنی
254 | sassy ( ۳2۳85888165 ‏پارسي باستان‎ «(Jb ‏مقیای‎ ( frasang ‏پهلوی‎ - ۴
254 | ‏فرسودی - بفتح اول وپنجم = فرساییدن از 58+ 1۲8 ؛ اوستا ‎gulfra - sana‏
261 | ‎Oo‏ قرمای - ‎ch‏ اول ء اسم از « فرمودن » ؛ پهلوی ۳81080] ( امر )ءایرائی‌باستان
263 | ‏فقط وچه اخیر را پذیرفته است « عقار 4۷ > ‎whe‏ نظر !5 ‎Ls‏ پهلوی عأنا5لا 800 ۳2120 است.
265 | ‏وفراء ( بقتح اول وتعدید دوم ) پوستین دوزاست . اما « فرو * درفارسی ‏ فرود ۰ پهلوی ‎APOE‏
265 | ‏۴ - اوستا - ۰5۲۵۷2۲۵۵9 - ۲2۷۵۲۵ , پهلوی ‎su fravar‏ « فروارنه »
265 | اوستابیمشخص تست . فروار فارسی با- 011821۳1۷272۳3 (بروار) (ه.م.) متطبق‌است . بعلاوه
265 | ‏۵ فر وختی - بضم اول ودوم وفتح پنجم ( درزبان کنونی ) ؛ اوستا ‎ofra +vaxsh.‏
265 | ‎vac - ins (‏ چنانکه ‎baxsh‏ از - ‎(hac‏ ( صداکردن » بمعرض فروش گذاشتن) ؛ پهلوی
267 | پور داود « خرده اوستا ص ۵۶ ۰ ۱۰۵ ۰ ۲۱۸ ۰ ۲۱۹ + ‎J.J.Modi , The Religious‏
267 | اوستا ص۹ ۲۱۶-۲۰ . این ‎ote‏ فرعی ومتأخر است.
267 | آتخان ‎AS‏ شماری مزدیسنی ‎AS)‏ شماری ‎ae‏ اوستالق ) در ‎Le‏ 4۱۱ ق.م. جمل‌آمده است »
268 | روزسال ‎bye‏ ميشده « پورداود . خرده اوستا ص ۲۱۹ > . ۴ — جشن فروردیان » جشن
268 | از اشتاد روز تا انیران روز از اسفندماء و پنج روز ‎WT‏ « پورداود. خرده اوستا ۰۴۲۱۹-۲۱۸
268 | ‏۴ - رك : فروردکان . ۴ - پهلوی ‎fravartin‏ مأخون از پارسی باستان
268 | ۷6 ( رك : فروهر ) » در اوستا نیز این‌کلمه بهیات اضامه در جمع موّث بیار آمده وهمیشه
270 | ‎٩‏ - پپلوی ۲۲8۷8۳۲ . ابرانی ‎ofravarti_ ott‏ . اوستا -62۷25/11/:بارتولمه
270 | پناه بنشیدن ). طبق مندرجات اوستا فروشی ( فرورنی ) نیروبی است که اهورمزدا برای‌نگهداری
271 | ‏قوی‌تر ) « تیبر کت ۷۵ ویز دریپلوی (۲2] ( بیار ) « منای ۲۷۶ > ؛ اوستا - ‎ofrahya‏
273 | - از: فر ( پیتاوند )-هنگگ ( از ره ‎thang‏ اوستابی‌بمعن ی کشیدن ). فرهنگه
274 | ‏دایر ۷۵۹ . ۷ ‎cae ty‏ هریز » ورلك: فژیژء فزژ؛ ۷ - پهلوی ۳۳6100 ,اوستا
274 | ‎Oo‏ فری - ‎SG‏ اول » ازاوستا - 87208 ( دوست. محبوب ) ۰ ‎cae‏ باستان- ‎priyd‏
```


## [2026-09-14T00:54:18.434Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^per-1\\|^per‑1\\|^per-\\|^peri\" AHD_watkins1985.txt | head -20",
 "description": "Find per- root in Watkins"
}
```


### [2026-09-14T00:54:18.485Z] TOOL RESULT

```
838:per-?
840:per-3. The young of an animal (< “a bringing forth,” “offspring”), Derivative root belonging to the group of per'. Suffixed o-grade form *por-si- in Germanic *farzi-, young cow, in Old English fearr, calf, and compound heahfore, calf (first element obscure): HEIFER. [In Pok. 2. D. per 818.]
841:per-‘. To try, risk (< “to lead over,” “press forward”). A verbal root belonging to the group of per’. 1. Lengthened grade *pér- in Germanic *féraz, danger, in Old English
```


## [2026-09-14T00:54:19.734Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"paradise\\|paradeisos\\|pairidaeza\\|pairi-daeza\" AHD_watkins1985.txt KLN_1966.txt SKT.txt | head -20",
 "description": "Grep for paradise"
}
```


### [2026-09-14T00:54:19.791Z] TOOL RESULT

```
AHD_watkins1985.txt:168:Roots indicating a number of technical operations are attested in most of the lan- guages of the family. One such is teks-, which in some dialects means “to fabricate, espe- cially by working with an ax,” but in others means “to weave” (TEXTILE). A root dheigh-, meaning “to mold, shape,” is applied both to bread (DOUGH) and to mud or clay, whence words for both pottery and mud walls (Ira- nian *pari-daiza, “walled around,” borrowed into Greek as the word that became English PARADISE).
AHD_watkins1985.txt:377:dapper, heavy, strong; later quick, nimble: DAPPER. [Pok. dheb- 239.] dhegvh-. To burn, warm. Suffixed o-grade form *dhogvh- eye- in Latin fovére, to warm, cherish, foment (> fomen- tare, to foment, and fomes, tinder): FOMENT, FOMITE. [Pok. dhegth- 240.] dh@(i)-. To suck. Contracted from *dheoa(i)-. 1. Suffixed reduced form *dhé-mnd- in Latin fémina, woman (< “she who suckles”): FEMALE, FEMININE; EFFEMINATE. 2. Suf- fixed reduced form *dhé-to- in Latin fétus, pregnancy, childbearing, offspring: FAWN, (FETAL), FETUS; EFFETE, (FETICIDE), SUPERFETATE. 3. Suffixed reduced form *dhé-kundo- in Latin fécundus, fruitful: FECUND. 4. Suf- fixed reduced form *dhé-no- in Latin fénum, faenum, hay ( < “produce”): FENNEL, FINOCHIO; (FENUGREEK), SAIN- FOIN. 5. Perhaps suffixed zero-grade form *dhi-lyo- (< *dhia-lyo-) in Latin filius, son, and filia, daughter (but these are equally possibly from the root bheue-): FILIAL, FILIATE; AFFILIATE, HIDALGO. 6. Suffixed reduced form *dhé-lo- in Latin fél(are, to suck: FELLATIO. 7. Suffixed reduced form *dhé-l-ik- in Latin félix, fruitful, fertile, lucky, happy: FELICITATE, FELICITY; FELICIFIC, INFELIC- Ty. 8. Suffixed reduced form *dhé-ld- in Greek thélé, nipple: ENDOTHELIUM, EPITHELIUM, (MESOTHELIUM). 9. Suffixed reduced form *dhé-l-u- in Greek thélus, female: THEELIN. [Pok. dhéi)- 241.] dheia-. To see, look. Variant form *dhyd- (< *dhyag-) in: a. suffixed form *dhyd-mn in Greek sémeion and séma (stem sémat-), sign: SEMANTIC, SEMATIC; SEMAPHORE, SEMASIOLOGY, SEMEME, SEMIOLOGY, SEMIOTIC; b, San- skrit dhydti, he meditates (< “he observes mentally”): ZEN BUDDHISM. [Pok. dheis- 243.] dheigh-. To form, build. 1. Germanic *daigjén in Old English d%ge, bread kneader: DAIRY. 2. Germanic *-dig- in Old English compound Aléfdige, mistress of a house- hold (< “bread kneader”; Al#f, bread, loaf): LADY. 3. Ex- tended o-grade form *dhoigho- in Germanic *daigaz in: a. Old English dag, dough: pouGH; b. Old High German teic, dough: TEIGLACH. 4. Suffixed zero-grade form *dhigh-ird, in Latin figira, form, shape (< “result of kneading”): FIGURE; CONFIGURATION, DISFIGURE, PRE- FIGURE, TRANSFIGURE. 5. Nasalized zero-grade form *dhi-n-gh- in Latin fingere, to shape: (FAINT), FEIGN, (FEINT), FICTILE, FICTION, FIGMENT; EFFIGY. 6. Nasal- ized zero-grade form *dhi-n-g(h)- in Greek thinganein, to touch: THIGMOTAXIS, THIXOTROPY. 7. Suffixed o-grade form *dhoigh-o- in Avestan daéza-, wall (originally made of clay or mud bricks): PARADISE. [Pok. dheigh- 244.] dhel-. A hollow. 1. Germanic *daljé in Old English dell, valley: DELL. 2. Germanic *dalam in Old English del, valley: DALE. 3. Germanic *del- in Old Norse dzla, wooden gutter on a ship: DALLES. [Pok. 1. dhel- 245.] dhelbh-. To dig, excavate. Germanic *de/ban in Old English de/fan, to dig: DELVE. [Pok. dhelbh- 246.] dhembh-. To bury. Suffixed zero-grade form *dhmbh-o- in Greek taphos (< *thaphos), tomb: CENOTAPH, EPI- TAPH. [Pok. (dhembh-), dhmbh- 248.] dhen-'. To run, flow. Suffixed o-grade form *dhon-ti- in Latin fons (stem font-), spring, fountain: FONT!, FOUN- TaIN. [Pok. 1. dhen- 249.] dhen-2. Palm of the hand. Suffixed form *dhen-r in Greek thenar, palm of the hand: THENAR. [Pok. 2. dhen- 249.] dher-1. To make muddy; darkness. 1. Suffixed form *dher-g- in Germanic *derk- in Old English deorc, dark: DARK. 2. Suffixed zero-grade form *dhr-egh- in: a. Ger- manic ‘suffixed form *drah-sta- in Old English drés, dregs: pross; b. Germanic *dragj6 in Old Norse dregg, dregs: DREGS. 3. Suffixed extended zero-grade form *dhro-bh- in Germanic *drab- in: a. Old English dreflian, to drivel: DRIVEL; b. probably Low German drabbelen, to paddle in water or mire, draggle, akin to the Low German source of Middle English drabelen, to draggle: DRABBLE; C. Middle Irish drab, dregs, probably akin to the Celtic source of DRAB2. 4. Suffixed extended
AHD_watkins1985.txt:837:“around.” I. Basic form *per and extended form *peri. 1. Germanic *fer-, *far-, used chiefly as an intensive prefix denoting destruction, reversal, or completion, in: a. Old High German far-, in German vereinen, to unite: TURNVEREIN; b. Middle Dutch vieren, to let out, slacken: VEER; C. compound “*fer-getan, “‘to lose one’s hold,” forget (see ghend-). 2. Suffixed (comparative) form *per-ero-, farther away, in Germanic *fer(e)ra’in Old English feor(r), far: FAR. 3. Compound “per-n-yo-, of last year (*-n-, year; see en-), in Germanic *fernja- in Old High German firni, old: FmRN. 4. Latin per, through, for, by: PER, PER-; PARAMOUNT, PARAMOUR, PARGET, PAR- VENU. 5. Greek peri, around, near, beyond: PERI-; PERIS- SODACTYL. 6. Sanskrit pari, through, around: PALANQUIN. 7. Avestan pairi, around: PARADISE. II. Zero-grade form *pr-. 1.Germanic *fur, before, in: a. Old English for, before, instead of, on account of: FOR; b. Old English for-, prefix denoting destruction, pejora- tion, exclusion, or completion: For-. 2. Extended form *prt- in Germanic *furth-, forward, in Old English forth, forth: FORTH; AFFORD. 3. Suffixed (comparative) form *pr-tero- in Germanic *furthera- in Old English furthra, furthor, farther away: FURTHER. 4. Compound *pr-st-i- (or *por-st-i-, with o-grade form *por-), “that which stands before,” stake, post (see sta-). III. Extended zero-grade form “pro-. 1. Suffixed (superlative) form *pro-mo- in: a. Germanic *fruma-, *furma- in Old Eng- lish forma, first, foremost: FOREMOST, FORMER?; b. Latin compound prandium, “first meal,” late breakfast, lunch (probably < *pram-d-ium < *pram-(e)d-yo-; second ele- ment *-(e)d-, to eat; see ed-). 2. Suffixed (superlative) form *pro-isto- in Germanic *furista-, foremost, in Old English fyrst, fyrest, first: FIRST. 3. Suffixed form *pre-wo- in Greek *prowo-, first, foremost, in: a. analogi- cally suffixed Greek form *préw-arya in Greek prdira, forward part of a ship: PROw; b. suffixed (superlative) Greek form *préw-ato- in Greek prétos, first, foremost: PROTEIN, PROTIST, PROTO-, PROTON. 4. Suffixed form *pro-i in Celtic *(p)ari, *are in Gaulish ari (combining form are-), before, in Latin arepennis, half-acre (second element obscure): ARPENT. IV. Extended form “prod. 1. Germanic *fura, before, in: a. Old English fore, for (> Middle English fore-), before: FORE, FORE-; FOREFA- THER; b. Old High German fora (> German vor), before: VORLAGE; Cc. Germanic prefixed and suffixed form *bi-fora-na, in the front (*bi-, at, by; see ambhi), in Old English beforan, before: BEFORE. 2. Greek para, beside, alongside of, beyond: PARA-); PALFREY. V. Extended form *pré. 1. a. Germanic *fra, forward, away from, in Old Norse *frd (> Middle English fro), from: FRO; FROWARD; b. Germanic *fra-, completely (see ed-, éik-). 2. Suffixed form *pro-mo- in: a. Germanic *fram, from, in Old English from, from: FROM; b. Germanic *frum, forward, hence derivative verb *frumjan, to further, in Old French f(ojurnir, to supply, provide: FURNISH, VE- NEER; C. Czech pram, raft: PRAAM. 3. Suffixed form *pr6é-wo- in Germanic *frdw6-, lady, in: a. Old High German frouwa, lady: FRAU, (FRAULEIN); b. Middle Dutch vrouwe, woman: vRouw. 4. Latin pré, pro-, be- fore, for, instead of: PRO!, PRO-!; PURCHASE. 5. Suffixed form *pr6-no- in Latin prénus, leaning forward: PRONE. 6. Possible suffixed form *pro-ko- in Latin compound reciprocus, alternating, ‘‘backward and forward” (*re-ko-, backward; see re-): RECIPROCAL. 7. Suffixed adverb *pro-kve in: a. Latin prope, near: APPROACH, RAPPROCHEMENT, REPROACH; b. suffixed form *prok- ink“o- in Latin propinquus, near: PROPINQUITY; Cc. suf- fixed (superlative) form *prok’-samo- in Latin proximus, nearest: PROXIMATE; APPROXIMATE. 8. Compound *pro-bhw-o-, growing well or straightforward (*bhw-o-, to grow; see bheue-), in Latin probus, upright, good, virtuous: (PROBABLE), PROBE, PROBITY, (PROOF), PROVE; APPROVE, IMPROBITY, (IMPROVE), (REPROVE). 9. Greek pro, before, in front, forward: PRO-2. 10. Suffixed (com-
AHD_watkins1985.txt:2059:-PARA pere-1 PARABLE gWelg-1 PARABOLA gW¥ele-1 PARACHUTE pere-1 PARACLETE kele-2 PARADE pere-1 PARADIGM deik- PARADISE dheigh-, pert PARADOX dek-! PARAFFIN pau- PARAGRAPH gerbh- PARALLAX al-1 PARALLEL al-1 PARALLELEPIPED ped-! PARALOGISM leg-1 PARALYSIS leu PARAMECIUM mak- PARAMOUNT ad-, per! PARAMOUR amma, pert PARANOIA nous PARAPET peg- PARAPHERNALIA bher-1 PARAPHRASE gWhren- PARAPLEGIA plak-2 PARASOL pere-1, sawel- PARATAXIS tag- PARBOIL beu-! PARCAE pera-1 PARCEL pere-2 PARCENER pere-2 PARDON d6-
SKT.txt:8882:Houri,  a  nymph  of  Paradise.  (Peti.^ Fer^.  A$iri,  one  virgin  of  Paradise,  ktird, Atir.  a  virgin  of  Paradise,  black-eyed nymph.  Cf.  Arab.  Aawrd,  fern,  of  akwar, having  fine  black  eyes.
SKT.txt:13216:Paradise.  (F.  -  L  -  tik.  - Paradis.  —  L.  paraJisus.  —  Gk.  v park,  pleasure-ground;    art  oru: and  now  a.<>ccrtained  to  be  of  Pcrs,  chij
SKT.txt:23151:paradise — parvis.                   L^^^|
KLN_1966.txt:4891:bheesty,  n.,  a  water  carrier.  —  Hind,  bhisti,  fr. Pers.  bihisti,  ‘one  from  Paradise’,  fr.  bihist, ‘Paradise’,  which  is  rel.  to  Avestic  vahishta-, Pahlavi  vahisht,  OI.  vasisthah,  ‘best’.
KLN_1966.txt:10662:‘I  smear,  anoint’,  dehf,  ‘rampart,  dam,  dike’, Avestic  daeza,  ‘wall’,  pairi-daeza,  ‘enclosure’, and  cogn.  with  Goth  daigs,  OE.  dag,  ‘dough’. See  dough  and  cp.  paradise, dehisce,  intr.  v.,  to  gape,  burst  open.  —  L.  de- hiscere,  ‘to  split  open,  gape,  yawn’,  fr.  de- and  hiscere,  inchoative  of  hiare,  ‘to  yawn’. See  hiatus.
KLN_1966.txt:11932:diwan,  n.  —  A  var.  of  dewan. diwani,  n.  —  A  var.  of  dewanee. dixie,  also  dixy,  n.,  a  kind  of  mess  tin  (slang).  — Hind,  degcht,  ‘a  small  kettle’,  fr.  Pers.  degcha, dimin.  of  deg,  ‘pot’,  which  is  rel.  to  Pahlavi  deg, ‘pot’.  Arm.  dez,  ‘heap’,  and  to  OI.  dihmi,  'I smear,  anoint’,  fr.  I.-E.  base  *dheigh-,  *dhoigh-, *dhigh-,  ‘to  form  out  of  clay,  to  knead,  form’. See  dough  and  cp.  next  word, dizdar,  disdar,  n.,  the  warden  of  a  castle.  —  Pers. dizdar,  ‘holder  of  a  castle’,  fr.  diz,  ‘castle’,  and -dar,  ‘holder,  possessor’.  The  first  element  is rel.  to  OPers.  dida,  ‘castle’,  Avestic  daeza, ‘wall’,  Arm.  dez,  ‘heap’ ;  see  prec.  word  and  cp. the  second  element  in  paradise.  For  the  second element  see  aumildar  and  cp.  words  there  re¬ ferred  to.
KLN_1966.txt:12148:rel.  to  ON.  deig,  Dan  deig ,  Swed.  deg,  MLG. deck,  MDu.  deech,  Du.  deeg,  OHG.,  MHG. teic,  G.  Teig ,  Goth,  daigs,  dough’,  digan,  ‘to knead’,  fr.  I.-E.  base  *dheigh-,  *dhoigh-,  *dhigh-, ‘to  form  out  of  clay,  to  knead,  form’,  whence also  Of.  dehmi,  ‘I  smear,  anoint’,  dehah,  ‘body’, lit.  ‘that  which  is  formed’,  dehi,  ‘rampart,  dam, dike’,  Avestic  daeza,  ‘wall’,  pairi-daeza,  ‘en¬ closure’  (whence  Gk.  TrapaSsiaop,  ‘enclosed park’),  OPers.  dida,  ‘castle’,  Toch.  A  tsek-, tsaik-,  B  tsik-,  ‘to  form’,  tseke,  ‘statue’,  Arm. dez ,  ‘heap,  pile’,  dizanem,  ‘I  heap  up,  pile  up’, Gk.  Tetyo?,  zov/'K  (dissimilated  fr.  *Hixoz, *ffotyo<;),  ‘wall’  (orig.  'clay  wall’),  (Hyyaveiv,  ‘to touch’,  Thracian  -SI£a,  ‘castle’,  L.  fingere,  ‘to form,  shape,  fashion’,  figura ,  ‘form,  shape’,  fi- gulus,  ‘potter’,  Oscan  feihuss,  ‘the  walls’,  ORuss. deza,  ‘baker’s  trough’,  Lith.  diezti,  dyzti,  ‘to cudgel,  thrash’  (lit.  ‘to  knead  thoroughly’),  OIr. digen,  ‘firm,  solid’  (orig.  ‘kneaded  into  a  com¬ pact  mass’).  Cp.  also  the  metathesized  forms: Lith.  ziedziu,  ziesti,  ‘to  form,  build’,  OSIav. zizdp,  zidati,  ‘to  build’,  zidu ,  ‘wall’.  Cp.  dairy, duff,  ‘pudding’,  and  the  second  element  in  lady. Cp.  also  deha,  dixia,  dizdar,  effigy,  faint,  feign, fictile,  fiction,  fictitious,  figure,  thigmo-,  the  first element  in  Tichodroma,  thixotropy  and  the second  element  in  paradise.
KLN_1966.txt:12634:edelweiss,  n.,  a  small  Alpine  plant  bearing  white flowers.  —  G.  Edelweifi,  compounded  of  edel, ‘noble’,  and  weifi,  ‘white’.  For  the  first  element see  atheling,  for  the  second  see  white, edema,  oedema,  a  swelling  ( med .)  —  Medical  L., fr.  Gk.  ol'Sr)(jta,  ‘a  swelling’,  fr.  oESoiv,  oESeiv,  ‘to swell’,  which  is  cogn.  with  Arm.  aitnum,  ‘I swell’,  aitumn,  ‘a  swelling’,  L.  aemidus  (for *aidmo-dos  or  *aidsmo-dos ),  ‘swelling’,  ON. eista  (for  *oid-s-to-),  ‘testicle’,  eitill,  ‘swelling’, eitr,  ‘poison’,  OE.  at  or,  attor,  of  s.m.,  and  prob. also  with  OSlav.  jadu ,  ‘poison’,  jadra  (pi.), ‘bosom’.  See  after  and  cp.  the  first  element  in Oedipus  and  the  second  element  in  myxedema. Derivatives:  edem-ic,  oedem-ic,  edemat-ous, oedemat-ous,  also  edemat-ose,  oedemat-ose,  adjs. Eden,  n.,  in  the  Bible,  the  garden  in  which  Adam and  Eve  first  lived;  Paradise.  —  Heb.  * Edhen , name  of  the  region  in  which  lay  the  Paradise (see  Gen. 2:8,  10,  15,  etc.)  The  name  is  usually explained  as  ‘the  place  of  delight’,  and  derived fr.  Heb.  'idhen,  ‘dainty,  delight’;  cp.  Edna.  U. Cassuto  in  his  Commentary  on  the  Book  of Genesis,  Part  One,  From  Adam  to  Noah,  The Hebrew  University,  Jersusalem,  1961,  pp.  107- to8,  explains  the  name  Eden — with  reference to  the  meaning  of  the  base  'dn  in  Ugaritic — as  ‘a  place  that  is  well  watered  throughout’. Derivative:  Eden-ic ,  adj. edenite,  n.,  a  variety  of  aluminous  amphibole (mineral.)  —  Named  after  £(/c'«ville,  New  York. For  the  ending  see  subst.  suff.  -ite.
KLN_1966.txt:15144:ford,  former,  forth,  further.  Cp.  also  arpent,  ex¬ perience,  experiment,  expert,  finnan,  paradise, pardao,  parallel,  Perean,  peregrine,  peril,  per¬ oneal,  pilgrim,  poligar,  pore,  ‘opening",  porrect, port,  ‘harbor’,  port,  ‘gate’,  port,  ‘to  carry’,  post, ‘stake’,  Prajapati,  Prakrit,  prakriti,  Pralaya, pram,  ‘a  kind  of  boat’,  prana,  priest,  primary, prime,  prior,  proceres,  procerity,  prodigal,  prone, prose,  proso-,  protero-,  proto-,  province,  prow, ‘fore  part  of  a  ship’,  prowess,  Purana,  and  the second  element  in  reciprocal.
KLN_1966.txt:18149:Derivatives:  hour-ly,  adj.  and  adv. houri,  n.,  a  nymph  of  the  Moslem  Paradise;  (fig.) a  seductive  woman.  —  F.,  fr.  Pers.  hurt,  fr. Arab,  hur,  pi.  of  ahwar,  fern,  haurd ’,  ‘having beautiful  black  eyes’,  fr.  fiawira,  ‘had  black eyes’,  which  is  rel.  to  Heb.  hawar,  Aram.-Syr. hdwdr,  ‘was  white’,  Heb.  hur,  ‘white  stuff’,  hori, ‘white  bread’.  The  -i  in  Pers.  hurt  is  a  formative element  serving  to  denote  the  singular, house,  n.  —  ME.  hus,  hous,  fr.  OE.  hits,  rel.  to OS.,  ON.,  OFris.,  OHG.  MHG,  Ads,  Du.Au/s,G. Haus,  Goth.  -Aur(in  the  compound^MdAnj.'temp- le\  lit.  ‘the  house  of  God’);  orig.  ‘shelter’,  fr. I.-E.  *qeus-,  -s-enlargement  of  base  *qeu-,  ‘to cover,  hide’.  See  hide,  v.  and  cp.  hoard,  hose, hut.  Cp.  also  husk,  the  first  element  in  husband, husting  and  the  second  element  in  caboose, house,  tr.  and  intr.  v.  —  OE.  husian,  ‘to  take  into a  house’,  fr.  hus,  ‘house’.  See  house,  n. housecarl,  n.,  member  of  the  bodyguard  of  a Danish  or  early  English  king  or  nobleman (hist.)  —  OE.  huscarl,  fr.  ON.  huskarl,  which  is compounded  of  ON.  hus,  ‘house’,  and  karl, ‘man’.  See  house  and  churl, housel,  n.,  the  Eucharist  (obsol.)  —  ME.  husel, fr.  OE.  husel,  ‘the  Eucharist’,  rel.  to  ON.  husl, of  s.m.,  Goth,  hunsl,  ‘sacrifice’,  and  prob.  cogn. with  Lith.  svehtas.  OSlav.  svetu,  OPruss.  swints, ‘holy’,  Lett,  svinet,  ‘to  hallow,  celebrate’, Avestic  splnta-,  ‘holy’.
KLN_1966.txt:27112:adj .  suff.  -ic  fr.  Late  L.  pandemus,  fr.  Gk.  TtavS^- [xo;,  7rxv8f][ii.oe,  ‘pertaining  to  all  the  people’,  fr. 7r<xv-  (see  pan-)  and  8rj[xo<;,  ‘people’.  See  demos. Derivatives:  pandemic,  n.,  pandemic-ity,  n. pandemonium,  n.,  the  abode  of  the  demons.  — ModL.,  the  capital  of  Hell  in  Paradise  Lost,  an epic  poem  by  John  Milton  (1608-74);  coined  by him  fr.  pan-  and  Late  L.  daemonium,  ‘inferior divine  being’,  in  Eccles.  L.  ‘evil  spirit’,  fr.  Gk. 8cap.6vt.ov,  ‘divine  power;  inferior  divine  being’, in  Eccles.  Gk.  ‘evil  spirit’,  prop,  subst.  use  of  the neut.  of  Scapovios,  ‘belonging  to  a  Sodptov’,  fr. Sodpcov,  ‘demon,  devil’.  See  demon.
KLN_1966.txt:27260:Derivative:  paradisaical-ly,  adv. paradise,  n.  —  ME .paradis,  fr.  OF.  (=  F .)  para- dis,  fr.  Late  L.  paradisus,  fr.  Gk.  TtapaSeiao?, ‘park,  the  garden  of  Eden,  paradise’,  a  word  of Old  Persian  origin;  cp.  Avestic  pairidaeza,  ‘an enclosure’,  whence  Heb.  pardes,  ‘park,  garden’ (whence  Aram,  pardes,  pardesa,  of  s.m.).  Aves¬ tic  pairidaeza  is  compounded  of  pairi,  ‘around’, and  daeza,  ‘wall’.  The  first  element  is  cogn.  with Gk.  Ttepi,  ‘around,  about’ ;  see  peri-.  The  second element  is  cogn.  with  OIr.  digen,  ‘firm,  solid’ (orig.  ‘kneaded  into  a  compact  mass’),  Gk.  tei- /o;,  ‘wall’,  L .  fingere,  ‘to  form,  fashion’,  Goth. deigan,  ‘to  smear’,  OE.  dag,  etc.,  ‘dough’.  See dough  and  cp.  deha,  fiction  and  the  first  element in  dizdar.  Cp.  also  parvis,  which  is  a  doublet  of paradise.
KLN_1966.txt:27262:Paradisea,  n.,  the  typical  genus  of  birds  of  para¬ dise.  —  ModL.,  fem.  of  ML.  paradiseus,  ‘per¬ taining  to  paradise’,  fr.  Late  L.  paradisus.  See prec.  word.
KLN_1966.txt:27263:Derivative:  paradise-an,  adj.,  pertaining  to birds  of  paradise.
KLN_1966.txt:27269:paradisiacal,  also  paradisiac  adj.,  pertaining  to, or  resembling,  paradise.  —  Late  L.  paradisiacus, fr.  L. paradisus.  See  paradise  and  suff.  -acand  -al. parados,  n.,  parapet  behind  a  trench.  —  F.,  prop, ‘defense  from  the  rear’,  coined  fr.  para-,  ‘that which  protects’,  and  F.  dos,  ‘back’,  fr.  L.  dor¬ sum.  See  dorso-.
KLN_1966.txt:27556:L.  parvi-,  fr.  parvus,  ‘small,  little’,  which  is  rel. to parum,  ‘a  little,  too  little’,  and  cogn.  with  Gk. mxupcx;,  ‘small’  (L. parvus  stands  to  Gk.  7raupo^ as  L.  nervus,  ‘nerve’,  stands  to  Gk.  vcupov,  of s.m.);  fr.  I.-E.  base  *pou-,  *peu-,  *pu-,  ‘small, little,  few’.  See  few  and  words  there  referred  to and  cp.  esp.  the  second  element  in  semper-, parvis,  n.,  open  space  in  front  of  a  church.  — ME.  parvys,  fr.  OF.  parevis,  parvis  (F.  parvis), fr.  ML.  Paradisus,  lit.  ‘paradise’,  name  of  the court  in  front  of  St.  Peter’s  in  Rome.  See  paradise, parvoline,  also  parvolin,  n.,  an  oily  liquid  C9H13N.
```


## [2026-09-14T00:55:09.696Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '836,839p' AHD_watkins1985.txt | cut -c1-300; echo \"=== tail of per1\"; awk 'NR==837' AHD_watkins1985.txt | tail -c 600",
 "description": "Check Watkins per1 Pokorny reference"
}
```


### [2026-09-14T00:55:10.767Z] TOOL RESULT

```
per’
“around.” I. Basic form *per and extended form *peri. 1. Germanic *fer-, *far-, used chiefly as an intensive prefix denoting destruction, reversal, or completion, in: a. Old High German far-, in German vereinen, to unite: TURNVEREIN; b. Middle Dutch vieren, to let out, slacken: VEER; C. compound
per-?
parative) form *pro-tero- in Greek proteros, before, former: HYSTERON PROTERON, PROTEROZOIC. VI. Exten- ded forms *prai-, *prei-. 1. Latin prae, before: PRE-; PRETERIT. 2. Suffixed (comparative) form *prei-yos- in Latin prior, former, higher, superior: PRIOR2. 3. Suffixed form *prei-wo- in: a. Latin
=== tail of per1
forward” (*re-ko-, backward; see re-): RECIPROCAL. 7. Suffixed adverb *pro-kve in: a. Latin prope, near: APPROACH, RAPPROCHEMENT, REPROACH; b. suffixed form *prok- ink“o- in Latin propinquus, near: PROPINQUITY; Cc. suf- fixed (superlative) form *prok’-samo- in Latin proximus, nearest: PROXIMATE; APPROXIMATE. 8. Compound *pro-bhw-o-, growing well or straightforward (*bhw-o-, to grow; see bheue-), in Latin probus, upright, good, virtuous: (PROBABLE), PROBE, PROBITY, (PROOF), PROVE; APPROVE, IMPROBITY, (IMPROVE), (REPROVE). 9. Greek pro, before, in front, forward: PRO-2. 10. Suffixed (com-
```


## [2026-09-14T00:55:12.472Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== CHEUNG kan\"; grep -n \"^\\*kan\\|\\*kan-\\|kan 2\\|to scatter, strew\" CHEUNG.txt | head -20; echo \"=== CHEUNG tak\"; grep -n \"pari-tak\\|\\*tak\\b\" CHEUNG.txt | head -10; echo \"=== CHEUNG bar parwardan\"; grep -n \"parwardan\\|parvardan\" CHEUNG.txt | head -10; echo \"=== CHEUNG stā paristīdan\"; grep -n \"paristīdan\\|parastīdan\" CHEUNG.txt | head -10",
 "description": "Grep Cheung for relevant verbs"
}
```


### [2026-09-14T00:55:12.564Z] TOOL RESULT

```
=== CHEUNG kan
15356:*kanl 229 
15413:*kan! ‘to throw, place, put; to destroy’ 
15478:the root *kan- ‘to dig’, which is semantically troublesome. || According to 
15521:*kan? ‘to fill’ 
15548:9 Several Iranian languages point to the existence of a separate root *kan- ‘to fill’. 
15552:*kanH! ‘to dig’ 
15588:*kanH2 233 
15629:*kanH? ‘to love, take pleasure in’ 
16277:*kan’). Perhaps, the Chor. form derives from the present stem *ham-krnta- of 
27154:*SANSKRIT: vap! ‘to scatter, strew (out), spread (out)’ (RV+) > EWAia II: 503 
28473:*kanH! would be a present formation (IE *kenH'-) of *xaH, as assumed in LIV: 344 
33508:*kan-, 232 
56314:*kan! (s.v.), *marc, *Hrais 
56322:*kanH', *kap/f, *Hrad, *xaH 
56597:*kan’, *parc, *parH' 
58218:*kan', *kauz’, *mai9H’, 
=== CHEUNG tak
=== CHEUNG bar parwardan
25665:*AVESTAN: Orao- ‘to nourish, [BMP tr.] /parwardan/’ = Liste: 27 
27396:*NWIR: Abz. varz ‘fertiliser, dung’ || (+ *pari-) NP parvardan/parvar- ‘to nourish, 
41256:parvardan/parvar-, 423 
=== CHEUNG stā paristīdan
```


## [2026-09-14T00:55:19.122Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '27380,27410p' CHEUNG.txt; echo \"======\"; sed -n '41250,41260p' CHEUNG.txt",
 "description": "Read Cheung parvardan context"
}
```


### [2026-09-14T00:55:19.185Z] TOOL RESULT

```
exact correspondence in Skt. RV urjavya- ‘abounding in strength’, Gershevitch apud 


Sims-Williams 1985: 100; Schwartz apud MacKenzie 1983: 535, fn. 8. 
Partic.: pres. MSogd. prwyjnyy (BBB: 37), MSogd. "prwyjynyy (BBB: 45) 


*uart 423 


*CHORESMIAN: (+ *pari-) prwr- ‘to rear, nourish, feed’ (LW). © Not from the root 
*bar ‘to carry, bring’, *pari-bar, as suggested by Samadi. || The Chor. forms cannot 
derive directly from *pari-uarza-, which would have yielded **prwZ- in Chor., cf. 
MacKenzie 1983, l.c. They may well be borrowed from Persian instead. = Samadi: 
156 

*NWIR: Abz. varz ‘fertiliser, dung’ || (+ *pari-) NP parvardan/parvar- ‘to nourish, 
feed’, parvardegar ‘Creator, Provider’ 

*NEIR: Oss. I. warzyn/warzt, D. warzun/warzt ‘to love’ (< *‘to take care of, foster’) 
*SANSKRIT: ürj- (f.) ‘nourishment, refreshment, strength” > EWAia I: 242 f. 

«PIE *uerH)g- ‘to be filled, nourished, brimming with life (energy)’. > A laryngeal is 
reconstructed on account of the long vowel in Skt. ürj-. => LIV: — | Pok.: 1169 

*IE COGNATES: Hitt. /uarkant-/ ‘fat, fattened’, Gr. opge ‘I am getting ready to bear, 
growing ripe; I swell with lust’, оруй ‘natural impulse, temperament, disposition’ 
*REFERENCES: Henning 1965: 176, fn. 38; Abaev, Slovar’ IV: 53 f.; Lecoq 2002: 604a; NEVP: 92 


*yarS ‘to be hungry’ 
======
pargandah, 231 

parmasidan, 180, 256 

parridan/parr-, 297 

parvardan/parvar-, 423 

parvardegar, 423 

parvaz, 431
```


## [2026-09-14T00:55:19.982Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '15413,15480p' CHEUNG.txt",
 "description": "Read Cheung *kan1 entry"
}
```


### [2026-09-14T00:55:20.039Z] TOOL RESULT

```
*kan! ‘to throw, place, put; to destroy’ 
*AVESTAN: (+ *ni-) ? Y Av. ni kan- ‘to bury’ || (+ *ui-) YAv. vikan- ‘to destroy, ruin’ 


230 *kanl 


Pres. athem. {1}: IND. 3sg. ()vika(i)nti (У 3.13), *vikonti (V 3.22); Caus.: pres. SUBJ. 3sg. ҮАУ. 
vikänaiiät (V 7.51); Pres. them. {2}: OPT. 3pl. ? YAv. ni kanaiion (V 17.12) 

*OLD PERSIAN: (+ *aua-) ? avakan- ‘to throw, place on’ || (+ *ni-) nika(n)- ‘to tear 
down’ || (+ *ui-) vika(")- ‘to destroy’ > Kent: 178b 

Pres. (a)them.: impf. IND. 1sg. avakanam <a-v-a-k-n-m> (DB 1.86), viyakanam <vi-i-y-k-n-m> (XPh 
38), 3sg. viyaka <vi-i-y-k> (DB 1.64), SUBJ. 2sg. vikanahy <vi-i-k-n-a-h-y> (DB 4.71, DB 4.73), 
vikanah° <vi-i-k-n-a-h-° > (DB 4.77), IMPV. 3sg. nika" tuv <n-i-k-tu-u-v> (DB 4.80) 

*MIDDLE PERSIAN: MMP qn-, BMP kn- /kan-/ ‘to dig (up); to raze, destroy’ || (+ 
*apa-) MMP ’bgn- (BMP LMYTWN-) ‘to throw away’ || (+ *pari-) MMP prgn-, 
BMP plkn- /pargan-/ ‘to scatter, sow’ || (+ *fra-) BMP plkn- /fragan-/ ‘to throw, lay 
(the foundations)’ || (+ *ui-) MMP gwg’n-, BMP gwk’n- /gugän-/ ‘to destroy’ 
c DMMPP: 206a, 10b, 278b, 166b 
Partic.: perf. pass. MMP qnd; Pass.: pres. IND. 3pl. MMP qnyyhynd || (^ *apa-) Pres.: IND. 3sg. MMP 
“’bgnyd, 3р1. MMP ’bgnynd, SUBJ. 3sg. MMP "bond 3р1. MMP *’bgn’nd, IMPV. 2р1. MMP ’bgnyd; 
Partic.: perf. pass. MMP ’bgnd || (+ *pari-) Pres.: IND. 3sg. BMP plknyt /parganéd/, 3pl. BMP plknynd 
/parganénd/, SUBJ. 3sg. ? MMP prgn’d; Partic.: perf. pass. BMP plgndk /pargandag/, BMP plknd 
/pargand/ || (+ *fra-) Partic.: perf. pass. BMP plknd /fragand/ || (+ *ui-) Pres.: IND. 3sg. MMP gwg’nyd, 
SUBJ. 3sg. BMP gwk’n’t/guganad/; Partic.: perf. pass. MMP gwgndg 
*PARTHIAN: kn- ‘to dig (up); to raze, destroy’ || (+ *apa-) ’bgn- ‘to throw’ || (+ 
*para-ä-) pr’gn- ‘to scatter, sow’ || (+ *pari-) prgn- ‘to scatter’ || (+ *ui-) wygn- ‘to 
be destroyed, perish’, (caus.) wyg’n- ‘to destroy’, wyg’n ‘destruction’, wyg’ng 
‘destroyer, destroying’, w(y)g’nysn ‘destruction’ — Ghilain: 55, 89, 71 | DMMPP: 
206a, 10b, 277a, 278b, 352b f. 

(+ *apa-) Pres.: IND. 35р. ’bgnyd, 3pl. 'bgnynd, OPT. 3pl. 'bgnyndy; Partic.: perf. pass. ’bgnd || (+ 


*para-ä-) Pres.: IND. 35р. "pr'gnyd; Partic.: perf. pass. pr'gnd, "prgnd || (+ *pari-) Partic.: perf. pass. 
*prgnd || (+ *ui-) Pres.: IND. 35р. wygnyd, wygynyd, 3р1. wygnynd; Partic.: perf. pass. wygndg, wygnd; 
Caus.: pres. IND. 2sg. MMP wyg’nyh, 3sg. wyg’nyd, 2р1. wyg’nyd, 3pl. wyg’nynd, SUBJ. 15р. "wyg’n’n 
*KHOTANESE: (+ *abi-) OKh. byañ- ‘to cover’ || (+ *pati-) LKh. pyan- ‘to cover’, (?) 
LKh. pacan- ‘to give, present; to cover’ || (+ *pari-) *paljsan-, pijsan- ‘to put around, 
surround; to apply’, ? LKh. parkam- (parküfi-) ‘to sprinkle, scatter’ || (+ *ui-) OKh. 
buvan- ‘to be harmed, ruined’, (caus.) OKh. buvañ- ‘to destroy’. © According to 
Emmerick (SGS: 75), the spelling variants of *paljsan-, pijsan- can hardly be 
reconciled with derivation *pari-kan’- ‘to fill’. A different meaning and, 
consequently, different etymology is given by Bailey (DKS: 218b): ‘to spread, 
bestrew’ (*pari-kau-). Alternatively, it may indicate a loan word or a living 
connection with unprefixed forms (S-W). = SGS: 105, 82, 62, 76, 75, 102 
*SOGDIAN: (+ *us-) BSogd. sknt’k, CSogd. sqnty (ppp.) ‘destroyed’, also in 
compounds, SSogd. ktsknt’k ‘ruined, waste’, MSogd. qtsndy ‘destruction’ (GMS: 
8365, fn. 1, 472) || (+ *рага-а-) BSogd. pr’kn- ‘to sow, scatter’ || (+ *ui-) MSogd. 
ykn- ‘to destroy’, MSogd. wyyn- (pass.) ‘to be destroyed’ (< Pth.) 


231 


(+ *para-ä-) Pres.: OPT. 2sg. BSogd. pr'kny; Inf.: pret. MSogd. "pr'gndy, MSogd. pr'qndyy, MSogd. 
pr’kndyyh || (+ *ui-) Inf.: ? MSogd. апуу ykynyy (BBB: 33}; Pass.: IND. pres. 3sg. MSogd. wyyndyy 
*CHORESMIAN: (+ *ati-) m/ckn- ‘to pick up’ || (^ *us-) m/sk(y)n- ‘to take out (sword, 
ink)’, ‘to take (revenge)’ || (+ *pati-) pckn- ‘to fulfil/perform (prayer), settle a debt; 
to take in (medicine)’ || (+ *para-ä-) pr’kn- ‘to sow, scatter, apply (medicine) on’ || 
(+ *ni-) nkn- ‘to bury’ || (+ *ui-) wkny- ‘to wear out, become old; be ruined’, 
(tr./caus.) wk’ny- ‘to wear out; ruin, tear down’. Ф Samadi (l.c.) assigns m/sk(y)n- to 
the root *kan- ‘to dig’, which is semantically troublesome. || According to 
MacKenzie 1990: 119, Chor. pckn- in the sense of ‘to (ful)fill, settle (a debt)’ has a 
different root, *Кат- ‘to fill’ ? > Samadi: 51, 181, 140, 149, 129, 215
```


## [2026-09-14T00:55:37.315Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '15480,15525p' CHEUNG.txt; echo \"=== uarz header\"; sed -n '27340,27382p' CHEUNG.txt",
 "description": "Cheung kan1 PIE line and uarz header"
}
```


### [2026-09-14T00:55:37.377Z] TOOL RESULT

```
different root, *Кат- ‘to fill’ ? > Samadi: 51, 181, 140, 149, 129, 215 

*BACTRIAN: (+ *para-à-) Tapayavo ‘sowing’ (J11, L12, V21, V21’) = S-W, Bact.: 
216 

*NWIR: NP kandan/kan-, Meim. bem-Kast (also supplet. bem-vat < *Hyaj)/ a-Ken- 
‘to take out, uproot, pluck’, Gz. békánaend ‘they jump up’, Gil. (Rsht.) daer-gadae/ 
dar-gan- ‘to throw’, (LW) kändcen/kän- ‘to take out, uproot, pluck’ || (+ *apa-) NP 
afgandan ‘to throw, cast away’ || (+ *upa- ?) Gil. (Rsht.) bägänæœstæ ‘struck against’ 
|| (+ *para-à- NP paragandan/paragan-, parakandan/parakan- ‘to disperse; sow; 
diffuse’, (ppp.) NP paragandah ‘dispersed, scattered, disbanded; dissipated’ || (+ 
*pati-) (?) NP paykandan/paykan- ‘to join; to collect; to draw out’ || (+ *pari-) NP 
pargandah ‘dispersed, scattered’ || (+ *ni-) Kurd. (Kurm.) nikandin ‘to bury’ 

*NEIR: (+ *aua-) Oss. D. (w)ogan ‘secret hiding place’ || (+ *fra-) Oss. D. regenun/ 
regzd ‘to shake, spread (salt, pepper for seasoning)’ || (+ *ni-) Oss. I. nyganyn/ 
nygad, D. nigzenun/niged ‘to bury’, Pash. njat-/njan- ‘to implant, imbed, thrust’, ? 
Khf. nijan ‘willow-rope, fastened in groves made in the shaft of a spade’, ? Yi. 
loyán-/loyád-, M. loyon-/loyend ‘to throw away, pour out’, (intr.) Yi. loyn-/loyód-, 
M. nayon-/loyöd- ‘to lie down, fall asleep’ (why -у- ?) || (+ *nis-) ? Oss. I. nykkaend 
‘cellar, underground accommodation’. © The past stem Pash. njat- "is inexplicable", 
according to МЕУР: Le, but it can be solved if we assume suppletion, viz. from 
*kar8/*xrah. 

*MISC: (+ *apa-) Arm. (LW) apakanel ‘to destroy’ 

Ó In many Iranian languages the roots *kan' ‘to throw’, *kanH! "o dig’ and *kan? 
‘to fill’ forms are homonymous and therefore often show mutual interference. For 
instance, the prefixed forms in *ni- ‘to bury’ may, alternatively, derive from *kan?. 
*PIE — > LIV: – | Pok.: 

*REFERENCES: Christensen, Contributions I: 58 f., 72; IFL II: 222b f. Lambton 1938: 42b; Abaev, 


Slovar’ П: 225, 366 f., 198, 196 Ё; EVS: 48b; Nyberg П: 111b; DKS: 251a, 307b; WIM II/1: 78; Asatrian 
— Livshits: 86; Cheung 2002: 78, 243; Lecoq 2002: 121 ff., 618, 665 (passim); NEVP: 56 


232 *kan2 


*kan? ‘to fill’ 
*MIDDLE PERSIAN: (+ *pati-) MMP phykn- ‘to fill, enter, penetrate’ || (+ *ham-) 


MMP hnen- ‘to fill in^ = DMMPP: 275a, 181a 
=== uarz header

*IE COGNATES: OSax., OHG werran, Du. (ver)warren, NHG verwirren ‘to confuse’ 


*yarHz ‘to (make) grow, nourish, be brimming with’ 

*AVESTAN: OAv. varoz- 'strength(ening) (Y 45.9), OAv. varazaiiant- ‘giving 
strength, strengthening' (Y 45.4, ? V 14.11). 9 On the connection between these 
forms and Skt. ürj- see Humbach 1958: 47 ff. This supersedes the previous 
interpretation by Bartholomae, AIW: 1378 f. (accepted by Insler, Gathas: 260, 257): 
*wirkend, werktätig’ and ‘zu wirken, Wirksamkeit zu entfalten’ respectively from 
*uarz. || Although referring to Humbach, l.c., Kellens — Pirart II: 299 rather translate 
the OAv. forms as ‘plaisir’ and ‘qui donne du plaisir’ without giving any explicit 
reason. See also below. || On the phonetic outcome involving "-rH- in Av., cf. 
Cantera 2001: 7 ff. 

*MIDDLE PERSIAN: MMP w’r- ‘to rejoice’, MMP w’ryn- (caus.) ‘to make happy, 
gladden’ || (+ *pari-) 1. MMP prwr-, BMP plwl- /parwar-/ ‘to foster, nurture, 
educate’, 2. MMP prwrd- (denomin. ?) ‘to foster, nourish’. 0 The meaning of MMP 
w'r- ‘to rejoice’ needs an explanation: perhaps < *'to be satisfied’ < *‘to be filled, 
nourished’ ? || MMP prwr-, BMP plwl- /parwar-/ has an unexpected -r- in the root. 
Its appearance is the result of assimilation: *r ... 1° < OP *г... rd’? = DMMPP: 
335b f., 280b, 281a 

Pres.: IND. 3pl. MMP w’rynd, SUBJ. 2sg. MMP w’r’y, 3sg. MMP w’r’d, IMPV. 2sg. w’r, 2pl. MMP 
w’tyyd; Caus.: pres. IND. 1sg. MMP w’rynwm, 35р. MMP w’rynyd, SUBJ. 3sg. MMP w’ryn’d || (+ 
*pari-) Well attested: 1. Pres.: IND. 1sg. BMP plwlwm /parwarum/, 258. MMP prwryh, 3sg. MMP 
prwryd, MMP prwryyd, BMP plwlyt /parwaréd/, 3р1. BMP plwlynd /parwarénd/, etc. || 2. Pres.: SUBJ. 
3sg. MMP "prwrd'd {hapax} 

*PARTHIAN: w'r- ‘to be glad’ (< MMP ?) || (+ *pari-) prwrz- ‘to nurture, care for’. > 
The form ww’r is unconnected, it means ‘separation’ (rather than ‘sorrow’). 
= Ghilain: 54, 52 | DMMPP: 335b, 281a 

Pres.: IND. 35р. “w’ryd, Ipl. w’r’m, 3pl. w’rynd, SUBJ. 25р. w’r’h, 1р1. w’r’m; Partic.: perf. pass. П 
w’r’d|| (+ *pari-) Pres.: IND. 3sg. prwrzyd, SUBJ. 2sg. “prwrz’h; Partic.: perf. pass. II prwrz’d 
*SOGDIAN: BSogd. wrz’yw, CSogd. wrzyw ‘haughty, arrogant’, SSogd. wrt, CSogd. 
wr’ (f.) ‘profit, interest’ (Gershevitch 1985: 49, fn. 43) || (+ *pari-) MSogd. prwyj- 
(pass./intr.) ‘to be fed, raised’, MSogd. prwyj (caus.) ‘to feed, raise’, BSogd. prw’rz 
‘care’, MSogd. prwyj’mndy ‘alimentation’. 0 BSogd. wrz’yw, CSogd. wrzyw has an 
exact correspondence in Skt. RV urjavya- ‘abounding in strength’, Gershevitch apud
```


## [2026-09-14T00:55:52.326Z] TOOL CALL #39: Bash

```json
{
 "command": "sed -n '1,60p' tools/fetch_source.py",
 "description": "Inspect fetch_source.py"
}
```


### [2026-09-14T00:55:52.366Z] TOOL RESULT

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
        with urllib.request.urlopen(req, timeout=60) as r:
            status = r.status
            raw = r.read(4_000_000)
            ctype = r.headers.get("Content-Type", "")
            enc = "utf-8"
            m = re.search(r"charset=([\w-]+)", ctype)
            if m: enc = m.group(1)
            body = raw.decode(enc, errors="replace")
            if "html" in ctype or body.lstrip().lower().startswith("<!doctype html") or "<html" in body[:2000].lower():
                mt = re.search(r"(?is)<title>(.*?)</title>", body)
```


## [2026-09-14T00:55:58.707Z] TOOL CALL #40: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/%D9%BE%DB%8C%D8%B1%D8%A7%D9%85%D9%88%D9%86\" \\\n \"https://en.wiktionary.org/wiki/%D9%BE%D8%B1%D9%88%D8%B1%D8%AF%D9%86\" \\\n \"https://en.wiktionary.org/wiki/%D9%BE%D8%B4%D8%AA\" \\\n \"https://en.wiktionary.org/wiki/%D9%81%D8%B1%D8%A7\" \\\n \"https://en.wiktionary.org/wiki/paradise\" \\\n \"https://www.etymonline.com/word/paradise\" \\\n ; do echo \"### $u\"; python3 tools/fetch_source.py \"$u\" --note \"page 393, root Per 1, verification of pairi-/para-/fra- derivations\"; done",
 "description": "Archive Wiktionary/Etymonline pages"
}
```


### [2026-09-14T00:56:02.528Z] TOOL RESULT

```
### https://en.wiktionary.org/wiki/%D9%BE%DB%8C%D8%B1%D8%A7%D9%85%D9%88%D9%86
/home/sfmqrb/git/rishe/data/verification/sources/web/470b78983ebfced5.txt
### https://en.wiktionary.org/wiki/%D9%BE%D8%B1%D9%88%D8%B1%D8%AF%D9%86
/home/sfmqrb/git/rishe/data/verification/sources/web/cb5ec453d1b82369.txt
### https://en.wiktionary.org/wiki/%D9%BE%D8%B4%D8%AA
/home/sfmqrb/git/rishe/data/verification/sources/web/d881b3b7e4d72c49.txt
### https://en.wiktionary.org/wiki/%D9%81%D8%B1%D8%A7
/home/sfmqrb/git/rishe/data/verification/sources/web/afd0646d55302f04.txt
### https://en.wiktionary.org/wiki/paradise
/home/sfmqrb/git/rishe/data/verification/sources/web/78b37ea759ce9974.txt
### https://www.etymonline.com/word/paradise
/home/sfmqrb/git/rishe/data/verification/sources/web/efa981c54c90a309.txt
```


## [2026-09-14T00:56:05.332Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in 470b78983ebfced5 cb5ec453d1b82369 d881b3b7e4d72c49 afd0646d55302f04; do echo \"##### $f\"; grep -n -A12 -i \"Etymology\" $f.txt | head -60; done",
 "description": "Read Wiktionary etymologies"
}
```


### [2026-09-14T00:56:06.401Z] TOOL RESULT

```
##### 470b78983ebfced5
65: Etymology 
66-
67- 1.3 
68- Pronunciation 
69-
70- 1.4 
71- Noun 
72-
73- 1.4.1 
74- Descendants 
75-
76- Toggle the table of contents 
77-
--
147: Etymology
148- [ edit ] 
149-
150- Inherited from Middle Persian [script needed] ( pylʾmwn' /⁠pērāmōn⁠/ ) , 𐫛𐫏𐫡𐫀𐫖𐫇𐫗 ( pyrʾmwn /⁠pērāmōn⁠/ , “ around, vicinity ” ) .
151-
152- Pronunciation
153- [ edit ] 
154-
155- ( Classical Persian ) IPA ( key ) : /peː.raː.ˈmuːn/ 
156-
157- ( Dari, formal ) IPA ( key ) : [pʰeː.ɾɑː.múːn] 
158-
159- ( Dari, formal ) IPA ( key ) : [pʰeː.ɾɑː.múːn] 
##### cb5ec453d1b82369
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Verb 
69-
70- 1.3.1 
71- Conjugation 
72-
73- Toggle the table of contents 
74-
--
140: Etymology
141- [ edit ] 
142-
143- Inherited from Middle Persian plwl-tn' ( parwardan , “ to foster, nourish, cherish, educate ” ) . Compare Northern Kurdish bergerr ( “ nourishment, nutrient; food for guests ” ) , Armenian պարարտ ( parart , “ fat, plump, portly ” ) . Exact cognate to pervert .
144-
145- Pronunciation
146- [ edit ] 
147-
148- ( Classical Persian ) IPA ( key ) : /par.war.ˈdan/ 
149-
150- ( Dari, formal ) IPA ( key ) : [pʰäɾ.wäɾ.d̪án] 
151-
152- ( Dari, formal ) IPA ( key ) : [pʰäɾ.wäɾ.d̪án] 
##### d881b3b7e4d72c49
62: Etymology 
63-
64- 1.2 
65- Noun 
66-
67- 1.2.1 
68- Derived terms 
69-
70- 1.2.2 
71- Descendants 
72-
73- 1.3 
74- Further reading 
--
85: Etymology 1 
86-
87- 2.2.1 
88- Pronunciation 
89-
90- 2.2.2 
91- Noun 
92-
93- 2.2.2.1 
94- Derived terms 
95-
96- 2.2.2.2 
97- Descendants 
--
103: Etymology 2 
104-
105- 2.3.1 
106- Pronunciation 
107-
108- 2.3.2 
109- Interjection 
110-
111- 2.4 
112- References 
113-
114- 3 
115- Urdu 
--
120: Etymology 
121-
122- 3.2 
123- Pronunciation 
124-
125- 3.3 
126- Noun 
127-
128- 3.4 
129- Further reading 
130-
131- Toggle the table of contents 
132-
--
210: Etymology
211- [ edit ] 
212-
213- Borrowed from Persian پشت ( pošt ) .
##### afd0646d55302f04
```


## [2026-09-14T00:56:16.469Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && sed -n '135,215p' d881b3b7e4d72c49.txt; echo \"#### FARA\"; sed -n '120,200p' afd0646d55302f04.txt",
 "description": "Read pošt and farā Wiktionary pages"
}
```


### [2026-09-14T00:56:16.517Z] TOOL RESULT

```
 15 languages 

 العربية 
 Ελληνικά 
 فارسی 
 Na Vosa Vakaviti 
 Français 
 Bahasa Indonesia 
 한국어 
 Kurdî 
 Malagasy 
 Bahasa Melayu 
 Polski 
 پښتو 
 Русский 
 Türkçe 
 中文 

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

 See also: بست , پست , and تست 

 Ottoman Turkish
 [ edit ] 

 Etymology
 [ edit ] 

 Borrowed from Persian پشت ( pošt ) .

 Noun
#### FARA
```


## [2026-09-14T00:56:19.754Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && grep -n -i \"Proto-Iranian\\|Middle Persian\\|Avestan\\|Old Persian\" d881b3b7e4d72c49.txt | head -20; echo \"#### fara file size\"; wc -l afd0646d55302f04.txt; grep -n -i \"persian\" afd0646d55302f04.txt | head -20",
 "description": "Find Persian etymology in posht page"
}
```


### [2026-09-14T00:56:19.823Z] TOOL RESULT

```
270: Inherited from Proto-Iranian *pr̥štáh ( “ back ” ) . Cognate with Avestan 𐬞𐬀𐬭𐬱𐬙𐬀 ( paršta ) , Sanskrit पृष्ठ ( pṛṣṭha ) . [ 1 ] 
488: Persian terms inherited from Proto-Iranian 
489: Persian terms derived from Proto-Iranian 
#### fara file size
5 afd0646d55302f04.txt
```


## [2026-09-14T00:56:30.340Z] TOOL CALL #44: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/per-\" \\\n \"https://en.wiktionary.org/wiki/%CF%80%CE%B1%CF%81%CE%AC%CE%B4%CE%B5%CE%B9%CF%83%CE%BF%CF%82\" \\\n \"https://en.wiktionary.org/wiki/%D9%BE%D8%B1%DA%AF%D8%A7%D8%B1\" \\\n \"https://en.wiktionary.org/wiki/%D9%BE%D8%B1%D8%AA%D9%88\" \\\n \"https://en.wiktionary.org/wiki/%D9%81%D8%B1%D8%B4%D8%AA%D9%87\" \\\n \"https://en.wiktionary.org/wiki/%D9%BE%D8%B1%D8%A7%DA%A9%D9%86%D8%AF%D9%86\" \\\n ; do echo \"### $u\"; python3 tools/fetch_source.py \"$u\" --note \"page 393, root Per 1 (Pokorny 810), verifying pairi-/para-/fra- derivations\"; done",
 "description": "Archive more Wiktionary pages"
}
```


### [2026-09-14T00:56:34.299Z] TOOL RESULT

```
### https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/per-
/home/sfmqrb/git/rishe/data/verification/sources/web/69aee26efd6f2318.txt
### https://en.wiktionary.org/wiki/%CF%80%CE%B1%CF%81%CE%AC%CE%B4%CE%B5%CE%B9%CF%83%CE%BF%CF%82
/home/sfmqrb/git/rishe/data/verification/sources/web/3ecfdce25b624877.txt
### https://en.wiktionary.org/wiki/%D9%BE%D8%B1%DA%AF%D8%A7%D8%B1
/home/sfmqrb/git/rishe/data/verification/sources/web/cd18e066f58697b8.txt
### https://en.wiktionary.org/wiki/%D9%BE%D8%B1%D8%AA%D9%88
/home/sfmqrb/git/rishe/data/verification/sources/web/02a09daef9492815.txt
### https://en.wiktionary.org/wiki/%D9%81%D8%B1%D8%B4%D8%AA%D9%87
/home/sfmqrb/git/rishe/data/verification/sources/web/216cb77378f93223.txt
### https://en.wiktionary.org/wiki/%D9%BE%D8%B1%D8%A7%DA%A9%D9%86%D8%AF%D9%86
/home/sfmqrb/git/rishe/data/verification/sources/web/c040fe294ca53c57.txt
```


## [2026-09-14T00:56:37.728Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in 69aee26efd6f2318 3ecfdce25b624877 cd18e066f58697b8 02a09daef9492815 216cb77378f93223 c040fe294ca53c57; do echo \"##### $f ($(wc -l < $f.txt) lines)\"; grep -n -i \"Inherited from\\|Borrowed from\\|From Proto\\|from Middle Persian\\|From Old\\|Avestan\\|Ancient Greek\\|Iranian\" $f.txt | head -12; done",
 "description": "Extract etymologies from fetched pages"
}
```


### [2026-09-14T00:56:38.942Z] TOOL RESULT

```
##### 69aee26efd6f2318 (517 lines)
175: Ancient Greek: πέρᾱ ( pérā ) , πέρᾱν ( pérān ) ( see there for further descendants )
176: ⇒ Ancient Greek: περάω ( peráō , “ to pass through ” ) ( see there for further descendants )
178: Proto-Indo-Iranian: *páras 
182: Proto-Iranian: *párah 
183: Avestan: 𐬞𐬀𐬭𐬀 ( para , “ higher, on the other side ” , first part of compounds ) 
189: → Ancient Greek: πέρπερος ( pérperos ) 
195: Ancient Greek: πόρσω ( pórsō ) , πόρρω ( pórrhō ) 
207: ⇒ Ancient Greek: πρέσβυς ( présbus ) 
240: Ancient Greek: πρίν ( prín ) , πρείν ( preín ) — Cretan ( see there for further descendants )
266: Proto-Indo-Iranian: *pr̥štʰás ( see there for further descendants )
280: Ancient Greek: πρυμνός ( prumnós ) 
312: Proto-Indo-Iranian: 
##### 3ecfdce25b624877 (470 lines)
57: Ancient Greek 
59: Toggle Ancient Greek subsection 
186: Ancient Greek
199: An Iranian borrowing, ultimately from Proto-Iranian *paridayjah . [ 1 ] [ 2 ] [ 3 ] 
301: This table gives Attic inflectional endings. For declension in other dialects, see Appendix:Ancient Greek dialectal declension .
326: ^ Tavernier, Jan ( 2007 ), Iranica in the Achaemenid Period (ca. 550–330 B.C.): Lexicon of Old Iranian Proper Names and Loanwords, Attested in Non-Iranian Texts , Peeters Publishers, →ISBN , pages 446, 447 
353: From Ancient Greek παράδεισος ( parádeisos ) .
408: Categories : Ancient Greek terms derived from Proto-Indo-Iranian 
409: Ancient Greek terms derived from the Proto-Indo-European root *dʰeyǵʰ- 
410: Ancient Greek terms derived from the Proto-Indo-European root *per- (fare) 
411: Ancient Greek terms derived from Proto-Indo-European 
412: Ancient Greek terms derived from the Proto-Indo-European root *per- (before) 
##### cd18e066f58697b8 (291 lines)
159: From Proto-Iranian , from Proto-Indo-Iranian . Cognate with Sogdian [script needed] ( prγrs’y /⁠parγarsē⁠/ , “ round, oval ” ) , Northern Kurdish pergal ( “ mode, system, order ” ) , Sanskrit प्रकार ( prakāra , “ sort, kind, form, nature, way, mode, manner ” ) . The first element is from Proto-Iranian *pari- ( “ around ” ) , ultimately from Proto-Indo-European *per- ( “ before, front ” ) .
189: Iranian reading ? 
243: Categories : Persian terms derived from Proto-Iranian 
244: Persian terms derived from Proto-Indo-Iranian 
245: Persian terms inherited from Proto-Iranian 
246: Persian terms derived from Proto-Indo-European 
##### 02a09daef9492815 (338 lines)
171: Borrowed from Classical Persian پرتو ( partaw ) 
204: The second part is ultimately from Proto-Indo-European *tep- . Related to Persian تفت ( “ heat, warmth ” ) , Persian آفتاب ( “ sun, sunshine ” ) , etc.
234: Iranian reading ? 
249: Iranian Persian
290: Categories : Ottoman Turkish terms borrowed from Classical Persian 
294: Persian terms derived from Proto-Indo-European 
##### 216cb77378f93223 (339 lines)
179: From Middle Persian plystk' ( frēstag , “ apostle; angel ” ) [Inscriptional Pahlavi needed] ( plystky , “ messenger ” ) . Compare Manichaean Middle Persian frystg , prystg ( frēstag ) , hrystg ( hrēstag , “ apostle; angle ” ) , Manichaean Parthian fryštg ( frēštag , “ apostle; angel ” ) , Avestan 𐬟𐬭𐬀𐬉𐬱𐬙𐬀- ( fraēšta- , “ messenger ” ) , Sanskrit प्रेष्यता ( preṣyatā ) ; Middle Iranian borrowings Old Armenian հրեշտակ ( hreštak ) , Jewish Babylonian Aramaic פרסתקא ( prestəqāʾ , “ royal guard, messenger ” ) , and Classical Syriac ܦܪܣܬܩܐ ( prestəqāʾ , “ royal guard, messenger ” ) .
209: Iranian reading ? 
269: a female given name , Fereshteh , Fereshte , Farishtah , Farishta , Fareshta , and Firishta , from Middle Persian 
280: Categories : Persian terms derived from Middle Persian 
281: Persian terms inherited from Middle Persian 
291: Persian female given names from Middle Persian 
##### c040fe294ca53c57 (616 lines)
170: Conjugation of پراکندن ( literary Iranian Persian )
```


## [2026-09-14T00:56:57.015Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && sed -n '140,200p' 69aee26efd6f2318.txt",
 "description": "Read PIE per- reconstruction page"
}
```


### [2026-09-14T00:56:57.062Z] TOOL RESULT

```
 hide 

 From Wiktionary, the free dictionary

 This Proto-Indo-European entry contains reconstructed terms and roots . As such, the term(s) in this entry are not directly attested , but are hypothesized to have existed based on comparative evidence.

 Proto-Indo-European
 [ edit ] 

 Root
 [ edit ] 

 *per- 

 before , in front 

 first 

 Derived terms
 [ edit ] 

 Terms derived from the Proto-Indo-European root *per- (before) (162 c, 0 e) 

 > ? *pér ( “ through ” ) [ 1 ] ( or from *per- ( “ to go through ” ) below, unless this is the source of that root ) 

 *pér-i ( “ around ” ) ( with locative suffix *-i ) 

 *per-nóy [ 2 ] or *pér-ero-s [ 1 ] 
 Proto-Germanic: *ferrai ( see there for further descendants )

 *pér-o- 
 Proto-Anatolian: *pérom 
 Hittite: 𒁉𒂊𒊏𒀭 ( pēran ) , 𒁉𒊏𒀭 ( peran ) 

 Proto-Hellenic: 
 Ancient Greek: πέρᾱ ( pérā ) , πέρᾱν ( pérān ) ( see there for further descendants )
 ⇒ Ancient Greek: περάω ( peráō , “ to pass through ” ) ( see there for further descendants )

 Proto-Indo-Iranian: *páras 
 Proto-Indo-Aryan: *páras 
 Sanskrit: पर॑ ( pára ) ( see there for further descendants )

 Proto-Iranian: *párah 
 Avestan: 𐬞𐬀𐬭𐬀 ( para , “ higher, on the other side ” , first part of compounds ) 

 ? Persian: فرفر ( farfar , “ in hurry ” ) ( archaic ) 

 Proto-Italic: 
 ⇒ Latin: (per)perus , (per)peram 
 → Ancient Greek: πέρπερος ( pérperos ) 

 *pér-uti ( “ last year ” ) (with *wet- ( “ year ” ) )

 *por-so- 
 Proto-Hellenic: 
 Ancient Greek: πόρσω ( pórsō ) , πόρρω ( pórrhō ) 

 Proto-Italic: *porsō 
 Latin: porrō 

 *pr̥-
```


## [2026-09-14T00:57:05.052Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== IEC peri\"; grep -n \"^peri\\|^per-\\|^pero-\\|^pr̥\\|^pro-\" IEC.txt | head -20; echo \"=== SYN\"; grep -n -i \"pairi\\|paršta\\|prsti\" SYN.txt | head -10; echo \"=== WLD Bd2 per\"; grep -n \"pairi\" incoming/WLD/WLD_Bd2_pages.txt | head -10",
 "description": "Grep Mann, Buck, Walde-Pokorny"
}
```


### [2026-09-14T00:57:05.148Z] TOOL RESULT

```
=== IEC peri
12710:per-a$- ‘pass through’. See peri, a$0 Oss. färäz ‘means’; Lat. perago, ére, f. “pass through, pierce, finish’; OE fercian, v. (convey, proceed’; OCS prézü, prp. “over, past; Slovak prez, id. Cf. also type *per-a$tos in Lat. per- actus; OS fer-aht, adj. ‘wise, shrewd'; OE ferhp, m.n. “life, mind, spirit; EME firth, s. ‘bogey’
12712:per-dhe- (-dhó-, -dho-). Cf. per-, dhé-mi Gk. pérthó, aor: éprathon, v. ‘destroy’; MHG cf. vertuon, inf. id.; Li. cf. perdem, adv. *ut- terly' beside perdedu, -déti, v. *'overdo?
12713:per-ei-mi ‘go through’. Cf. per-, ei-mi. Pp. type per-eitos Skt. cf. (intensive) piparmi, v.; Hitt. parhmi, v. “drive”; Gk. peráo, v.; OCS na-perjo, -periti, V. ‘pierce’; OLI. per-eimi, v. ‘pass’. Pp. in Skt. páretah beside paraitah *deceased'; Lat. peri- tus ‘expert; OPer. paraita- "past: Umb. pere- tom, supine ‘perished, lost’; OFris. ferd, f. ‘journey’; Li. pereitas ‘past, last
12714:per-ëiə, cf. per-, ei-mi, etc. Alb. prrue, Tosk prua, m. ‘torrent’; Cz. peřej, m. ‘current’; Blg. cf. perój, m. ‘mountain stream, downpour’; Ukr. perija ‘line, row’; Li. perēja, f. ‘defile, gulley’
12717:peri (per, per-) «through, over, round; very-'. WP II, 30 Skt. pári; Av. pairi; Ober pariy; Per. pār; Oss. fäl- ‘through-’; Gk. peri, per; (Alb. ambig. për ‘for’, see pro, pro); Lat. per; Umb. -per, post-
12720:peri-bhán-, cf. bha-mi, (bho-) Skt. cf. bhànam, n. “appearance”; pari-bhàse, mp. ‘appear’; Arm. cf. h-erevan acem, v. ‘show’; h-erevan gam, v. (appear, fr. *en- peri- or *pi-) Gk. peri-pháneia, f. *conspi- cuousness'
12721:peri-do-(-dídó-), cf. do-mi, dídó- Skt. pari-dMádami; Gk. peri-dídomai; Lat. perdo, -dére; W (?) rhyddau, inf. v. (free, cf. rhydd, adj. 'free); OCS pré-dami, datt: OLi. per-duomi, mod. -duodu, inf: -duoti
12722:perin- (peri-, pern-) Tokh. A pare, B peri ‘fault; Arm. her, i-st. “hate, envy; OS. OHG firina, Go. faírina ‘crime; blame’; OE firen, f. ‘crime; violence; suffering’; OFris. firne, f. ‘crime’; ON firn, npl. ‘outrage’; cf. mod. Icel. firnindi, npl. ‘the wilds; MHG virne, sf. *misdeed' (but virne, adj. “old, wise’ unrelated)
12723:perinēmi ‘transact’ Gk. pérnēmi, id.; Olr. renaim, renim, v. id.; Skt. cf. páne, mp. “buy, bargain'
12724:peri-sthà- Skt. pari-stha-, v. encompass; obstruct; Per. firistam, v. "send: Arm. (ambig.) ertam, v. (*go', but cf. strm-); Gk. periístémi ‘go round, surround'; Lat. cf. persto, -stare (continue, persist; OHG firstan, inf. ‘perceive, under- stand": OCS pré-stajgo, -stati, v. and -stajati (*cease', cf. Av. pairista, pp. ‘tried; powerless’); Li. per-stoju, -stoti, v. ‘cease’. Cf. variants of type *-sthon- in Arm. erit'anam, v. ‘sink, waste away” and Lat. prae-stino, åre, v. *pre-empt,, and type *-stos, -sthios, -sthis in Skt. paristih, f. ‘reverse, distress; Gk. perissós ‘huge’;
12725:peri-bhán- — perkt-, prKt-, prokt-
12735:per-itos, à, is, us “passed; passage”. Cf. per-, ei-mi Skt. paritas, adv. “round, about’; paritah, pp. ‘surrounded, clasped? beside páretab, adj. (deceased', fr. *per-eit-); Gk. cf. peritios “Macedonian month’; peritia ‘a feast’; Lat. cf. perítia, f. ‘expertise’ beside peritus, adj. ‘expert’; ON ferð, f. journey, conduct’; Swed. cf. fárde, adv. “in progress, under way”
12736:perior- (?) Per. parre ‘side, border: Gk. peirar, gs. pef- ratos, n. end. limit?
12737:perio, cf. peri-ei-, itos. Hitt. cf. pariya(mi), v. ‘send forth’; pariya(n), adv. “forth, ahead"; Gk. peíro; Lat. perio, ire; MHG cf. verje, verige, wm. (*ferryman': G Ferge, f. 'ferry); E also to ferry, v.; G also Fåhre, f. id.; Sw. fárja, f. id.
12748:per-m-, cf. per-, emó Lat. per-imo, -imére, v. (remove, liquidate'; OCS préimo, pré-eti (take, grasp, under- stand'; Li. pér-imu, -imti, v. 'take over; pull through, stab, grab'
12750:per-nokt- ‘overnight. Cf. per-, nokts (noktis) Alb. cf. (archaic) pér-nátet, v. 3s. ‘grows dark’; pér-nata, -naté, adv. (ambig. *per- or *pro-: “by night); Lat. cf. per-nocto, äre, f. spend
13532:pro-ag- (by crasis: próg-, prag-), cf. pro-, ago Per. far-àz, adj. *exalted"; far-azam, v. ‘erect’; Oss. (Graz, s. ‘means, facility’; fárazun, inf. ‘be able’; Arm. ar-ac, i-st. s. “proverb, precept’; Gk. prágos, n. “deed, act; Alb. prodh, m. ‘boon’; prodhë, f. ‘produce, product"; OHG fruohhan, adj. ‘bold’; OS cf. frokno *boldly'; ON froekn, adj. ‘bold’; OCS prazü, m. "breed. ing male animal” beside prozü, prp. ‘through’. Verbal types (pro-ag0, pro0, etc.) cf. Skt. pra- ajakah, m. ‘carter’; Av. paraze(imi), v. “bring along”; Per. farazam ‘erect’; Arm. ar-acem, v. ‘tend animals, graze’; Gk. proágo "drive on, lead on? beside prásso, présso (do, act’, if for *pragio) cf. prágos, eos, n. ‘deed, act’; (W rhoi ‘put, give’ is regarded by JMJ:WQG 1913 as a form of W rhoddi fr. *pro-de-, -dhe- or sim.); cf. E fraught, adj. & freight, s.: G Fracht, fr. a type *pro-aKt- > *pràkt- (: Gk. praktós, práksis, préksis, but Gk. -kh- in the pf. péprakha, péprēkha unexplained)
13534:pro-apo-, ‘back, away, off, forth? Gk. pro-apo- (stéllo, etc. ‘send away, etc.); Alb. prapa ‘again’; prapë, adv. "back: MHG vor-abe, adv. “in advance”. An alleged propo- dila, beside propé-dila *potentilla', of Dacian origin, is ambig. WH : LEW, p. 373.
13535:pro-aue-, -au- ‘downward, down? Skt. práva- (foff- in cpds.); Per. farü, adv. ‘down’; Lat. právus, adj. ((base, vile’. For pronus, see Supt: pro-án- with reservations)
13536:pro-bheudh-, bhoudh-, bhudh-. WP II, 147 Skt. pra-bodhami v. tr. ‘wake’; Olr. ro-bud,
=== SYN
2682:Words for ‘marry’ (and ‘marriage’ are from such diverse sources as the fol- lowing: ‘husband’, ‘wife’ (the verbs, at first at least, used only in sense a or b re- spectively), ‘spouse’; ‘union’, ‘pairing’; ‘house’, ‘household’, through the notion of establishing a family; various prac- tices preceding or accompanying the marriage ceremony, as ‘contract’, ‘oath’, ‘bargain’, ‘betrothal’; ‘giving’ (orig. of the father giving his daughter in mar- riage, hence mostly in sense b); ‘lead- ing’ (the husband leading the bride, so orig. in sense a); ‘following’ (the bride
5463:208 SELECTED INDO-EUROPEAN SYNONYMS 4.162 RIB tk.  wAeupdv Goth. .... Lith. Sonkaulis ne seat ON rif Lett. riba Lat. costa Dan. ribben’ ChSl.  rebro It. costa Sw. revben SCr. __rebro Fr. cole OE rib Boh. ebro Sp. costilla ME rib Pol. zebro Rum.  coastd NE rib Russ. ebro Tr. asna Du. rib Skt. parcu-, prsti- NIr.  ecasna OHG rippa Av. parasu- . asen MHG rippe Br. kostezen NHG rippe
5473:7. Skt. pargu-, prsti-, Av. parasu- : Ch8l. priisz (pl.) ‘breast’ (as region of the
6400:ChSl. priisi (pl.), SCr., Boh. prsa (pl.) or prsi, prsy (pl.), Boh. SE. prs ‘woman’s breast’, Pol. piers : Skt, Pargu., prsti-. Av. parasu- ‘rib’. Slavic shift from ‘ribs’ through ‘chest’ to ‘breast’, or ‘ribs’ and ‘chest’ fr. a common notion of ‘inclosing’; uncertain which, since root connection doubtful. Walde-P. 2.444
7191:Av. mié- (inf. maé@manam of dogs Barth. 1107; cf. also mayah- ‘coitus’ Barth. 1141): Av. miéwa-, midwara- ‘paired’, Skt. mith- ‘meet, alternate, etc.’, mithuna- ‘paired, pairing, copula- tion’, ete. Walde-P. 2.247 f.
12313:8.13 GARDEN Grk. —xijwos Goth. aurtigards Lith. darzas NG kijwos, weptBodt ON -gardr Lett. darzs Lat. —horlus Dan. have ChSl.  vrittit, vriitogradit It. giardino; orto Sw. trddgdrd (ogradit) Fr. jardin OE ortgeard, wyritin SCr. ort, baSta Sp. jardin, huerta ME _ garden, orchard Boh.  zahrada Rum. grddiné NE gardin Pol. ogréd Ir. lubgort, garda Du. luin Russ. sad, ogorod Nir. garrdha, gairdin OHG  garto Skt. —-vatika-, udyana- W. gardd MHG arte Av. (pairidaéza-) Br. liorz NHG garten
12340:Av. pairidaéza- ‘hedged-in place’, perh. ‘garden’ (cf. NPers. paléz ‘garden’, and loanwords Grk. rapédeoos, Arm. partéz ‘enclosed garden’) : pairi-daézaya- ‘wall about’, Skt. déhi-, Grk. retxos
14089:Av. bri- (only with pairi- ‘cut around’), NPers. burridan ‘cut’ : Skt. bhri- ‘injure’, ChSl. briti ‘shear’, britva ‘razor’. Walde-P. 2.194.
18350:3. Boh. ndprava, also ‘restoration, re- pairing’, abstract to napraviti ‘set right, repair’, with specialization to ‘axle’ as the part that breaks down and needs repairing?
=== WLD Bd2 per
445:   Av. 'pairika „die Frommen durch Liebeskiinste vom Glauben abspenstig
12685:  Ai. hhrinanti „8ie versehren*' (Pf. bibhraya Dhatup.), av. pairibrma‘}9 ha
15373:vgl. zum       -Formans bes, das Praes. ai. bhrtndti „verzehrt**, av. pairi-
34990:vaMa- = av. pairisx^axta- „rings umschlossen“.                           Aii\ seng „schlank“ (*„bieg-
```


## [2026-09-14T00:57:06.727Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY && grep -n \"پیرامون\\|پرگار\\|پرتو\\|پروردن\\|پشت\\|پراکندن\\|فرا\\b\" ARY_pages.txt | head -20",
 "description": "Grep Aryanpur IE roots dictionary"
}
```


### [2026-09-14T00:57:06.781Z] TOOL RESULT

```
86:نژادی بر سایرین برتری کامل داشتند. چون در آلمان و اسکاندیناوی اینگونه مردم فراوان ترند؛ آنها
159:فرعی آن هر یک تبدیل به زبان جداگانه‌ای می‌شوند (همانطور که مثلاً لاتین تبدیل شد به فرانمه و
207:واژهی «صده معمولاً حاوی حرف «7ق) است.(مثلاً در فرانسه ۳3۸۲7 و یا انگلیسی ۰171-30822
245:سارماتی * سغدی * خوازمی + فارسی > پشتو + زبانهای هندوستان شمالی. جهت این موج‌های
264:می‌شوند و زبانهای پیرامون بیشتر محافظه کارند و دارای واژه‌های کهن تراند. مثلاً زبان فرانسه‌ی رایج
266:در ایالت کبک در کانادا (یک زبان پیرامون) از زبان فرانسه‌ی رایج د رکشور فرانسه کمتر تغیی رکرده
267:است و شباهت یشتر به فرانس‌ی قرن هفدهم دارد. یگی از علت‌های این تفاوت این است که زبانهای
268:حاشیه یا پیرامون حاوی واژه‌هابی هستند که قبل از خروج از گهواره جزو زبان هند و اروپایی
320:این ريشه در زبانهای مختلف دارای معنی « کوه» يا «تپه؛ و یا «پشته» و يا «انباشته) هستند.
328:می‌کردند. جسدها معمولاً بر پشت خوایید و پاهای آنها به یک سو خم شده است. 2
348:باختری فرانسه تکلم می‌شود در گذشته بخش عمده‌ی اسپانیا را زیر پوشش داشته است. شواهد فراوان
392:می‌شوندبطوریکه مثلاً یک نفر انگلیسی يا فرانسوی نمی‌تواند زبان انگلیسی يا فرانسوی کهن را درک
401:از این خانواده‌ها شامل چند زبان‌اند. مثلاً خانواده‌ی لاتین شامل ایتالیایی و فرانسه و اسپانیایی و
408:از انگلیسی کهن (از ۵۰۰ تا ۰ میلادی). همین طور فرانسه پرمی گردد به فرانسه‌ی میانه (از ۱۴۰۰
409:تا ۱۹۰۰ میلادی) و فرانسه‌ی میائه منشعب است از فرانسه‌ی کهن (از ۹۰۰ تا ۱۴۰۰ میلادی). ضدنٌ
411:و غیره هم هست. همین طور دریافتند که فرانسه‌ی کهن نیز خود ناشی از زبان لاتین است و اين زبان
416:میان فرانسه‌ی کهن و اسپانیایی کهن بیشتر است تا شباهت میان فرانسه و اسپانیایی معاصر.
419:فرانسه کهن اسپانیایی کهن .
421:فرانسه اسپانیای
423:هم شباهت‌های فراوان دارند در صورتیکه شباهتی میان این زبان‌ها و عبری (/218151#) وجود
```


## [2026-09-14T00:57:20.338Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY && grep -n \"^PER\\|PERI\\|PER-\" ARY_latin_index_pages.txt | head -20",
 "description": "Grep Aryanpur latin index for PER"
}
```


### [2026-09-14T00:57:20.451Z] TOOL RESULT

```
1401:READ HENGLISH) 1S) PERI LATIN) oa
2107:(SUPERIROR) 135 UBER (GERMAN) AST
4246:PERNAI (LITHUANIAN) gl) PARUVA:(BLD PERSIAN) ole ors 3-74
4274:PERK, PIRKTI :(LITHUANIAN) gi} PURTI-, PURTIS
4399:| PARADISE (OLD ENGLISH) ot lS PARADEISOS, PERI+TO{CHOS
4406:(PARDISE) 754, (PERI-) 777 PARADIS NORWEGIAN) «5$3
4643:PERSHU, PIRSHTI PREGUNTA
4677:sgboay)) PERI: \ PER =) scant od Ce oat 9 in Sets 99 SI Cora cal tal dla
5257:PER- HOLD PRUSSIAN) 25.3.4 PAIRI- AVESTAN) oes}
5260:ER. s(WELSH) (53) PERI-, PER- i(GREEK) gly
5266:BARNHART: (PERI-) 777 FYR- (OLD ENGLISH) 248 JS
5269:PER., PER- A(LITHUANIAN) ip
11283:PER, PRE- PARIY, PARI, PER-
11287:PER- (BOHEMIAN) goa PERI (GREEK) gli
11288:PER., PRA+:(OLD PRUSSIAN) oS 3.4 PER-, PERI-, PRO- (LATIN) 3
11353:MACKENZIE: (ANGEL) 102 PERISHTA SANSKRIT) oy Sail
15893:PERKS, ROBERT S. P. COMPARATIVE INDO-EUROPEAN LINGUISTICS. AMSTERDAM: .
```


## [2026-09-14T00:57:21.699Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -c \"\" MON_part1.txt MON_part2.txt 2>/dev/null; grep -n \"پیرامون\" MON_part1.txt MON_part2.txt | head -5",
 "description": "Check Moin files"
}
```


### [2026-09-14T00:57:21.813Z] TOOL RESULT

```
MON_part2.txt:94500
MON_part1.txt:99339
MON_part1.txt:14616:پیرامون آن (مانند طویله» انبار و غیره) و 
MON_part1.txt:19796:پیرامون مقعد درد پیدا آرد. باد خصیه: (یز.) 
MON_part1.txt:21194:بتفوز: ۳۷۲02 [پتفوز] (.) پیرامون دهان 
MON_part1.txt:22567:بر کافوز] (امر.) پیرامون دهان؛ پکث و پوز. 
MON_part1.txt:31090:پرواز: ۲۵۳-۷22 [در پیرامون پریدن] (ا.) بالا
```


## [2026-09-14T00:57:31.957Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^پیرامون\\|پیرامون:\" MON_part1.txt | head -5; echo \"=== pargar\"; grep -n \"پرگار:\" MON_part1.txt | head -5; echo \"=== partow\"; grep -n \"پرتو:\" MON_part1.txt | head -5; echo \"=== parvardan\"; grep -n \"پروردن:\" MON_part1.txt | head -5; echo \"=== posht\"; grep -n \"^پشت:\\|پشت:\" MON_part1.txt | head -3; echo \"=== fara\"; grep -n \"فرا:\" MON_part1.txt MON_part2.txt | head -5",
 "description": "Grep Moin for headwords"
}
```


### [2026-09-14T00:57:32.106Z] TOOL RESULT

```
14616:پیرامون آن (مانند طویله» انبار و غیره) و 
19796:پیرامون مقعد درد پیدا آرد. باد خصیه: (یز.) 
54446:پیرامون» جوانب» جهات. ضح. در فارسی 
=== pargar
30843:پرگار: 1۲ |[ - پرگال - پرگاره ِ بر کار 
=== partow
=== parvardan
=== posht
1106:۹ پشت: ۲08 2.0 (امر.) منی» آب مرد. 
29968:کم‌پشت. باران پرپشت: که بسیار و فراوان 
31938:1 پشت: 0051-1-51 (ق‌مر.) پشت سر 
=== fara
MON_part1.txt:14907:افرا: هه (.) ( گیا.) درختی از تبرة افراها 
MON_part1.txt:85524:شفرا: 0778 (.) چاپلوسی» چرب‌زبانی. 
MON_part1.txt:89801:اصفر؛ زرد رنگ. (پز.) زرداب. کيسة صفرا: 
MON_part2.txt:5448:فرا: 1*۲2 (پشف.) بر سر فعل درآید و آن در 
MON_part2.txt:16004:نهفرا: همرطهر [ع. . فهقری] (مص‌ل.) به
```


## [2026-09-14T00:57:34.822Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '30843,30846p' MON_part1.txt; echo \"---- fara\"; sed -n '5448,5456p' MON_part2.txt; echo \"---- posht\"; sed -n '31938,31942p' MON_part1.txt",
 "description": "Read Moin entries"
}
```


### [2026-09-14T00:57:34.912Z] TOOL RESULT

```
پرگار: 1۲ |[ - پرگال - پرگاره ِ بر کار 
- پر کال - پردال - پرگر - برودال 
- پرکر - فرجار» معر.] (ا.) آلتی هندسی 
برای کشیدن دایره و خطو ط ؛ پر کار» 
---- fara
فرا: 1*۲2 (پشف.) بر سر فعل درآید و آن در 
اصل به معنی به؛ سویء در باشد. (حر. اض.) 
ده زر دبکگا بیش. به با. سوی» جانت. 
(ص.) بلند» عالی. 

فراء: تا زع. - فرا] (.) (جان.) گورخر. 
هیر 2۱ ۳9 [ع. ۰] (ص.) بسوستین‌دوز؛ 
پوستین فروش. پوست پیراه واتگر. 
فرابافن: 0.] (مسص‌ل.) دروغ نخ 
---- posht
1 پشت: 0051-1-51 (ق‌مر.) پشت سر 
هم پباپی» متوالی» متصل» مسلسل. بشت به 
پشت» برابر» دوش به‌دوش. 

پشت‌بند. ۳۰-0 (امر .) دیواری که پشت
```


## [2026-09-14T00:57:44.621Z] TOOL CALL #53: Bash

```json
{
 "command": "ls site/pages/393.jpg 2>/dev/null; pdftoppm -f 393 -l 393 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg393 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg393.png",
 "description": "Render PDF page 393"
}
```


### [2026-09-14T00:57:46.694Z] TOOL RESULT

```
site/pages/393.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb 101976 Sep 13 20:57 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg393.png
```


## [2026-09-14T00:57:48.816Z] TOOL CALL #54: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg393.png"
}
```


### [2026-09-14T00:57:49.397Z] TOOL RESULT

```

```


## [2026-09-14T00:57:49.395Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-14T00:58:20.387Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"pairi\\.daēza\\|pairidaēza\\|pairi-daēza\\|pairi\\.daeza\\|daSza\\|paiii\\.daE\" BRT.txt | head; echo \"=== paršta\"; grep -n \"parSta-\\|parsta-\\|paršta\" BRT.txt | head -10; echo \"=== SNS 133\"; awk 'BEGIN{RS=\"\\f\"} NR>=130 && NR<=136' SNS_pages.txt | head -40",
 "description": "Grep Bartholomae and SNS"
}
```


### [2026-09-14T00:58:21.469Z] TOOL RESULT

```
9063:mit  7'i  'durch  Graben  beseitigen,  ab- tragen; zerstören':  yasca  .  .  daxmatiqm avavanhm  maz3  vtkanayät  ya>a  .  .  V.  7. 51 ; — yat  b.J  paiti  fra!st.>m  daxma  uzdaSza (sd.;  lies  vrd')  vJkanü  (3SPA.)  yahmya  . . "an  welchem  Ort  man  am  meisten  die  D. durch  Abtragung  zerstört,  wo  .  ."  V.  y. 13;  —  yat  bü  paiti  fraüittnt  vikmte (3SPM.)  .  .gjmam  V..J.Z2;  —Wäyadanä (sd.)  tyä  gauiii'ätJ'  . .  viyakai'  (3SPrA.) Bh. /.  14;  —  kyt^  aparam  imilm  dipim vaitnhy  ..  maty^  (sd.)  vikanähy^^  Bh. 4.  15;  16;— _jW;>  imrim  dipim  ..vainähy '.■ikanähidisi^  Bh.  4- 1 7  II  ■
15604:•  j.pairi.daeza-m.,Plur.'einerings-,rundura gehende,  sich  zusamuienschliessende  Um- wallung, Ummauerung':  aSa^a  hl  aiie  ySi maxäayains  aiAhä  z»mö  'tan  pairi.dal- sayqn  V.^j.  18.
21510:•  j.  yahmya  Adv.  'wo,  ubi' :  yai  bä  paiti fraishm  daxma  (NPm.)  uzdaSza  (sd.)  kir- yeinie  y  narS  irtsta  moayeinteV.3.');i2, 7.  54i  —  tl  narB  xsd^ra  (APn.)  xsqymte ,,  y  stariiatca  gätus  .  .  Yt/7.  7;  — arpdvJm  (ASf.)  , ,  y  ('ubi'  statt  'in  qua') ahurS  masdh  ..  niva^ayal  Yt.5.  85.
=== paršta
27644:•  j.  zaintparSta-  Ad}.  Von  dem  kundigen erfragt,  durch  Fragen  ermittelt':  Aala.- mq'knmisA.)  'tfm,  Aa%a.mahrai  'tat,  Aala.- ma%rahe  'toAe,  Aala.ma%'ra  'ta  (VS.)  Eitr.
=== SNS 133
                                 Uj c-^b 4tU«llj
                                                                                                                  j^c^U^L^U
                                                                                                                                                   TIT



                                         *
                                                                                                  •o^'^rabaz darilnlh:
                                  ^.^j^vuzurg: RB              :   3*        ^>)3
                                                                                                                                  —JW\J>
                                                                                                                                  -*0*yj


                                  +* vajra-         :
                                                        L vazra-   :
                                                                            t-
nt.207)vazraka-              :




                    •   6/TT^        .   ^>:vuzurgan:              nyiP                                    W/Trf a*». 1523)
                                                                                                                            r5na-            ,*.



;r.
                                    LBBMH :>»: S> J
                                   aSJ»iJdsdil:

      dyl:^<* U^*>- 1692) hrd: ******
.(Mir. Ma*.    111,65)
                                      z^rad- :b-
                                  zyrd: >V          Man.   II, 41.)
                                                                                    i
                                                                                          U<* 1494, r udh^^
                                                                                                                    ,

                                                                                                                        '^
                                                                                                                         >    '   ran5nSd:
```


## [2026-09-14T00:58:34.908Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=15400 && NR<=15620 && /^ *[0-9]{3,4} *$/ {print NR\": \"$0}' BRT.txt | tail -8; echo \"=== around 18330 for frank\"; awk 'NR>=18200 && NR<=18340 && /^ *[0-9]{3,4} *$/ {print NR\": \"$0}' BRT.txt | tail -6",
 "description": "Find Bartholomae column numbers"
}
```


### [2026-09-14T00:58:36.002Z] TOOL RESULT

```
15547: 862
15585: 865
15588: 866
=== around 18330 for frank
```


## [2026-09-14T00:58:46.807Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && python3 - <<'EOF'\nt=open('WLD_Bd2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint('n',len(pages))\nfor i,p in enumerate(pages):\n    if 'pairi' in p and 'apers' in p:\n        print('leaf',i)\nEOF\ngrep -n \"apers. pariy\\|av. pairi,\" WLD_Bd2_pages.txt | head",
 "description": "Find Walde-Pokorny per- entry"
}
```


### [2026-09-14T00:58:48.102Z] TOOL RESULT

```
n 725
```


## [2026-09-14T00:58:51.534Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && grep -n \"pairi\" WLD_Bd2_pages.txt | head -20; echo \"--- find page 29\"; python3 - <<'EOF'\nt=open('WLD_Bd2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in range(30,70):\n    head=pages[i][:150].replace('\\n',' ')\n    print(i,'|',head[:120])\nEOF",
 "description": "Locate WLD Bd2 page 29"
}
```


### [2026-09-14T00:58:52.642Z] TOOL RESULT

```
445:   Av. 'pairika „die Frommen durch Liebeskiinste vom Glauben abspenstig
12685:  Ai. hhrinanti „8ie versehren*' (Pf. bibhraya Dhatup.), av. pairibrma‘}9 ha
15373:vgl. zum       -Formans bes, das Praes. ai. bhrtndti „verzehrt**, av. pairi-
34990:vaMa- = av. pairisx^axta- „rings umschlossen“.                           Aii\ seng „schlank“ (*„bieg-
--- find page 29
30 | 26                                                          pent-   qulntus^    osk. Apontes (vgl. o. Punfiis^ no/unneg,
31 |                                                                                                ;   ^                    
32 |                  :     28                                                per-      B.j?y-ew-:uaerweitert vielleicht in a
33 |                                                per-                                                29  Anfch. ds.); lat.
34 | 30                                              per-     Ai. pari Adv. „rmgsimi"‘   (mit Yerben auch „uber hinaus, hindu
35 |                                                                                                                  ;;     
36 |                                                                                         ,     32                        
37 |                                                                 per-                                             33     
38 | 34                                       per-   stufiges         anzuerkennen sei (vgl. ai. gru-miiitUli gimUh) oder ein
39 |                                                     per-                                                    35  „weiter‘
40 |                                                                                                                    ;    
41 |                                                per-                                      37  Pormen vci\tth\ urspriingli
42 |                                                                                                       —  38             
43 |                                                 per-                                           39   4.    per- „hmuberfu
44 |              :     40                                             per-               jjDurchgang, Furt^^r av. pordtu-s m
45 |                                                         per-                                41   gleich, Paar'', paro,  
46 |                                              per- 42  „Windei“, cech. spraieJc „unzeitiges Kalb“, klr. vyportok „Fruhgeb
47 |                                                          per-                              43     Lit. p'^rhtnas        
48 |                                                                                                      ;     44           
49 |             :                                                                         perk, prek                        
50 |                                                                                                    ;     46             
51 |                                                perk-,   p^k           perq^(o-)                                     47  
52 | 48                                        perg   — perg- reihen,   wozu nach Wackernagel ZfdA. 2, 558 kelt.             
53 |                                                  perth-    — perd-                             49   unsicher; anders iib
54 | 50                                      Potd-   — persaa konnteu      (vgl.      zur Bed. russ. peVesyj ^^gefleckt, bunt
55 |                                                (pel-)   — pel-                                                    51   S
56 | 52                                                     pel-    3.pel- mit Eedupl. in Worten fiir Schmetterling.   Lat. p
57 |                                                 pel-                                                   53   Anlaut nicht
58 | 54                                                        pel-      Germ.          (s. o.) in aisl.fqlr^ ags.fealo^ as.f
59 |                                                   pel-                                               55  nur unannehinba
60 | 56                                                pel-    ^r^fer,.triplis“, got. tivei-fls      ahd.      „zweifelhaft‘^
61 |                                                                                  '                                      
62 |                                                                                                     ;     schimmernder B
63 |                                                        pel-                                        59  TiaX/Lir]^   s. 0
64 | 60                                                pel-              flouw {"^fleiva-) „lau schlaff^^ (daraus dt. Til.vlo
65 | pela- „breit und flach, ausbreiten; durch Druck oder Schlag flacb formen,      breitschlagen, breitklatschen“.   Lat. pa
66 | 62                                        pela-   juventa^.     Oder von der ^Erw. der Wz.,          die    auch anderwa
67 |                                                       pel-                                                 63  Austernsc
68 |                                                                                      )     64                           
69 |                                                     pelaq-
```


## [2026-09-14T00:58:57.976Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && python3 - <<'EOF'\nt=open('WLD_Bd2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint(pages[34][:1400])\nEOF",
 "description": "Print WLD Bd2 p.30 per-"
}
```


### [2026-09-14T00:58:58.986Z] TOOL RESULT

```
30                                              per-


  Ai. pari Adv. „rmgsimi"‘   (mit Yerben auch „uber hinaus, hindurch u.
dgl.^"), vor Adj. verstarkend (z. B. pariprt „sehr lieb‘^), Praep. m. Acc.
„uber etwas hinaus, um herum, gegen^^, m. Abl. „(rings) von «her‘‘, av.
pair/, ap. pariy Adv. „vorne; zuvor, fruher‘‘, Praep. m. Acc. „um-heruni,
       iiber-      mitLok. (nur gath. aaO.) „in, bei^**, m, Abl. „von -her,
von -weg^^, m. Instr. „ex (aliqua re cognoscere)^^
   Gr. nsQi, TtEQi^ dial, auch neg (unsicher ob aus urpr. *7t€Qi entstanden
Oder idg. *per; s. Gunther IF. 20, 50 f., 62, 65, Kretschmer Gl. 1, 37 f., Jacob-
sohn KZ. 42, 278) Adv. „um herum, durch und durch“, Praef. vor Yerben
„uber etwas hinaus, iiber, voriiber, herum -um^^, vor Adj. „sehr, uber-
aus“ (z. B. jiEQixaklyg „perpulcher“) Praep. m. Acc. ,,um -herum, in etwas
umher, um (def^ mit Loc. („Datio“) „um herum, um (wegen)^^, m. Gen.
(des Bereiches) „um (den Bereich einer Sache) herum; um (= in betreff,
wegen“ (Ableitungen TtEgichoiog; Ttegi^, TiegiGoogf -tto?, s. Boisacq 772 f.
m. Lit.); in judla neg, og Jisg („der gerade^*’), d^vvpEvdg TtEg („betrubt
freilich“) liegt wohl idg. ^per (nicht *per/) vor, vgl. lat. parum-per „ein
Weilchen nur“, topper^ antioper (wohl auch paulisper^ tantisper', anders
Brugmann IF. 27, 244 f.), vgl. Skutsch AfLL. 1, 102, Porsch. 1 15, Nieder-
mann Rh. Mus. 52, 505 ff., Lindsay-
```


## [2026-09-14T00:59:19.329Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"mün\\|müu\\|rämü\" HRN.txt | head -20; echo \"=== HUB\"; grep -n -i \"eramun\\|rämün\\|pēramūn\" HUB.txt | head",
 "description": "Grep Horn for piramun"
}
```


### [2026-09-14T00:59:19.387Z] TOOL RESULT

```
216:g. zunädmün etc., No. 584, np. zerah, No. 561, ezS etc.,
431:Die philosophische Fakultät der Münchener Universität hat als
703:kiird. LW. asmärij äsimün, asmm; a{y, LW. äsmän;
742:bereits wohnen'^). (Nöldeke, mündliche Mitteilung).
932:Nöldeke (mündliche Mitteilung) meint, dass sich
1125:Nöldeke (mündliche Mitteilung) vergleicht deutsch
1169:(402) finden sich im Np. nur dialektisch in g. ustädmün,
1170:vistädmün.
1363:(PL amün) 'dieser; Käs. emseb , emril, emsöl; mäz.
1445:Die Etymologie stammt von Nöldeke (mündliche
1450:Nöldeke schlägt vor (mündliche Mitteilung), die
1614:validet) zu identificiren, wie dies nach mündlicher Mit-
1637:(mündliche Mitteilung), np. ermän 'Gast' hieran
1642:aw. yazata-; phlv. yas^d (Münzen), vergl. Izates
1845:g. vaftmün.
2108:"^^ ' g. bartmün; Käs. bertän^ bardin, bardemün, bebSrt;
2198:207. burnäf bernä Müngling', burnm 'Jugend, Kindheit',
2311:Übertragungen annimmt (mündliche Mitteilung), vergl.
2322:(mündliche Mitteilung) möchte gr. aY.vq)og 'Becher ver-
2349:ist; bulhös ist btt^l heves (Nöldeke, mündliche Mit-
=== HUB
4584:paz. peramun around' Shk. 263 (zu ap. pariy um, iiber'?).
```


## [2026-09-14T00:59:26.619Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('HUB.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\n# find leaf index of line 4584\nupto='\\n'.join(lines[:4584])\nleaf=upto.count('\\f')\nprint('leaf',leaf,'printed p',leaf-10)\npg=t.split('\\f')[leaf]\nprint(pg[:700])\nEOF",
 "description": "Find Hübschmann page for peramun"
}
```


### [2026-09-14T00:59:27.649Z] TOOL RESULT

```
leaf 141 printed p 131
— 181 —
nur in yetkar 'Brief, Urkunde ™ np. yadgar *Erinnerungs-
zeichen, Andenken'.
§ 8. Ap. any wird durch Epenthese zu phi. gw, np.
m; ary zu phi. np. Sr, wahrend fy zu Ir wird:
a) phi. m^Uk 'Geist* (oben p. 100; Horn- Andreas:
menoi) = zd. mainyu-; np. mJnO 'Himmer = zd. mainyava-
'himmlisch'; phi. mSiiltan meinen, glauben', paz. minfdan
{=*mmidan), ap. maniyahy 2. pers. conj., zd. mainy^t^, skr.
mdnyatB,
b) Eran = arm. Eran, paz. Erdn, phi. Eran, inschr.
Airan und Aryan, ap. g. pi. ^Ariyanam\ dSr Vacker =
paz. dSr, zd. cairyu" (fiir dirya-) Aogemad. § 84 ; nlro, alter
«5r5?, ^siz.n^rd (Min. und Shk.), aus *naryw- oder ^naryava-
(Horn Nr. 1064)?; b^rUn 'aussen* von *6?r- = "^dvarya-?
(ob
```


## [2026-09-14T01:00:16.247Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PHD framan/frazam/froxtan\"; grep -n -o \"framān \\[[^]]*\\][^.]*\\.\\|frazām \\[[^]]*\\][^.]*\\.\\|frōxtan[^.]*\\.\\|framarz[^.]*\\.\" PHD.txt | head -10; echo \"=== BRT fratara\"; grep -n \"fratara-\" BRT.txt | head -5",
 "description": "Grep MacKenzie and Bartholomae for final forms"
}
```


### [2026-09-14T01:00:16.318Z] TOOL RESULT

```
=== PHD framan/frazam/froxtan
170:framān ['bwltplm^n'] disobedient.
325:framān [pim^n! | M frmn, N farman] order, command; a minor degree of sin.
426:framān [%'/p/mn' | М k’rprm’n, Ar. qahramán] manager, overseer.
=== BRT fratara
```


## [2026-09-14T01:00:19.890Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -o \"frazām[^|]\\{0,60\\}\\|frōxtan[^|]\\{0,60\\}\\|frōš[^|]\\{0,40\\}\" PHD.txt | head -10; echo \"=== PHD frawahr/frawardin\"; grep -n -o \"frawahr[^|]\\{0,60\\}\\|Frawardīn[^|]\\{0,60\\}\" PHD.txt | head -6",
 "description": "Grep MacKenzie for frazam, froxtan, frawahr"
}
```


### [2026-09-14T01:00:21.042Z] TOOL RESULT

```
352:frazāmēnīdan, frazāmēn- [plc*myn-ytn!] = frazāftan.
353:frazām-pērēzīh [p/c”*m pylwcyh] final victory.
1308:frazāmišn, hanjām.
3913:frōšag, gēzēnag, lawzénag, Šiftēnag, watrēna
4211:frazām-pērēzīh.
4661:frazām $ à o frazám- -S à оу
4662:frazāmēn- - "edo frazāmēnīdan WO rā à o
4663:frazām-pērēzīh va eye à оу frazaftan we” à Q frazēn, parzin w Ф оу
=== PHD frawahr/frawardin
335:frawahr [рі 
337:frawahr.
789:frawahr, fraward.
3744:frawahr, fraward, griw, gyan, ruwan, uštān.
4681:frawahr - PO o parwāngāh 595 ep o parwanagih ^5 e» Ф parwanag 13 ?
```


## [2026-09-14T01:00:26.651Z] TOOL CALL #64: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg393.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/393.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/393.png",
 "description": "Archive page image"
}
```


### [2026-09-14T01:00:26.741Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 101976 Sep 13 21:00 /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/393.png
```


## [2026-09-14T01:13:28.053Z] TOOL CALL #65: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build393.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\n\nW = \"https://en.wiktionary.org/wiki/\"\n\nroot_entry = {\n \"entry\": 0,\n \"root\": \"Per 1\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *per- / locatival *per-i 'forward, in front, around, through' (Pokorny 810, s.v. per-2 section A; Watkins/AHD per¹ 'around')\",\n \"note\": \"Pokorny IEW p.810 opens the entry 'per-2' with exactly the material Nourai puts in this box: 'A. Dient als Präposition, Präverb und Adverb: a. per, peri (Lokative des Wurzelnomens) ‚vorwärts, im Hinausgehen, Hinübergehen über, im Durchdringen, im Übermaß‘ ... ai. pari, av. pairi, apers. pariy ... besonders ai. und gr. ist die Bedeutung ‚ringsum, umherum‘.' So both halves of Nourai's gloss ('around, forward') stand on that one page. The numbering 'Per 1 ... Per 4' with the gloss 'around' is taken over from Watkins' AHD appendix, which likewise heads the entry per¹ '“around.” I. Basic form *per and extended form *peri' and refers it to '[Pok. 2. per 810]'. The one imprecision is that Pokorny's per-2 is a single lemma covering pp.810-816 including the senses 'to lead over', 'to sell', 'to try', which Nourai splits off as Per 2-4; the split is Watkins', not Pokorny's. The Iranian preverbs pairi- (< *peri), para- (< *pero/*perā) and fra- (< *pro) all belong under this one lemma — Pokorny p.814 'ai. prá- Präf. ... av. frā, fra-, ap. fra- Präf. ‚vorwärts, voran; fort, weg‘' — so Nourai's grouping of pairi-, para- and fra- derivatives under one root box is correct.\",\n \"note_fa\": \"ریشهٔ هندواروپایی آغازین *per- (و صورت مکانی *per-i) به معنای «پیش، جلو، پیرامون، از میان» است؛ پوکورنی در صفحهٔ ۸۱۰ فرهنگ خود زیر سرواژهٔ per-2 دقیقاً همین مواد را می‌آورد: «per، peri ... به معنای به‌سوی جلو، فراتر رفتن، از میان گذشتن» و می‌افزاید که «در سنسکریت و یونانی به‌ویژه معنای «گرداگرد، پیرامون» دارد»، و صورت‌های ai. pari، av. pairi، apers. pariy را برمی‌شمارد. پس هر دو معنایی که نورایی داده («پیرامون» و «جلو») در همان صفحه پشتوانه دارد. شماره‌گذاری «Per 1» تا «Per 4» از پیوست ریشه‌های هندواروپایی فرهنگ AHD (واتکینز) گرفته شده، نه از پوکورنی؛ پوکورنی همه‌ی این‌ها را یک سرواژهٔ واحد (per-2، صص ۸۱۰–۸۱۶) می‌داند. پیشوندهای ایرانی pairi- (از *peri)، para- (از *pero) و fra- (از *pro) هر سه زیر همین ریشه جای می‌گیرند (پوکورنی ص ۸۱۴)، بنابراین گردآوردن آن‌ها در یک جعبه از سوی نورایی درست است. ادعای نورایی درست است.\",\n \"sources\": [W + \"Reconstruction:Proto-Indo-European/per-\"],\n \"ref_check\": [\n   {\"ref\": \"POK:810\", \"status\": \"supports\",\n    \"note\": \"Pokorny IEW p.810 (local POK_03.txt, form-feed leaf 44, which ends with the running number 811): 'A. Dient als Präposition, Präverb und Adverb: a. per, peri (Lokative des Wurzelnomens) ‚vorwärts, im Hinausgehen, Hinübergehen über, im Durchdringen, im Übermaß‘, woraus ‚über — hinaus, durch — hin‘; ai. pari, av. pairi, apers. pariy, gr. περί ... besonders ai. und gr. ist die Bedeutung ‚ringsum, umherum‘.' The POK_full dump confirms the lemma span: 'Root / lemma: per-2 ... Page(s): 810-816.' Page number exact; the only caveat is that Pokorny has one lemma where Nourai (after Watkins) has four.\"}\n ],\n \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Walde-Pokorny II 29-30 s.v. per- (WLD_Bd2_pages.txt leaf 34, header '30 per-')\", \"stance\": \"supports\",\n    \"note\": \"'Ai. pari Adv. „ringsum“ (mit Verben auch „über hinaus, hindurch u. dgl.“), vor Adj. verstärkend ... av. pairi, ap. pariy Adv. „vorne; zuvor, früher“, Präp. m. Acc. „um-herum, über-“' — the very pair of senses ('around' / 'forward, in front') Nourai's root box gives; this is the WP. II 29 ff. that Pokorny himself cites at the foot of p.816.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.v. per¹ (AHD_watkins1985.txt line 837)\", \"stance\": \"supports\",\n    \"note\": \"'per¹. “around.” I. Basic form *per and extended form *peri. ... 5. Greek peri, around, near, beyond: PERI-. 6. Sanskrit pari, through, around: PALANQUIN. 7. Avestan pairi, around: PARADISE. II. Zero-grade form *pr-. ... III. Extended zero-grade form *pro-. ... V. Extended form *prō. 1.a. Germanic *fra, forward...' — Nourai's headword, number and gloss are copied from here, and the index line 'PARADISE dheigh-, per¹' matches his double citation POK:244,810 on node 1.\"},\n   {\"src\": \"IEC\", \"where\": \"Mann, IEC col. s.v. peri (IEC.txt line 12717)\", \"stance\": \"supports\",\n    \"note\": \"'peri (per, per-) ‚through, over, round; very-‘. WP II, 30. Skt. pári; Av. pairi; OPers. pariy; Per. pār; Oss. fäl- ‚through-‘; Gk. peri, per; Lat. per ...' — an independent confirmation of the root and of the Iranian reflexes.\"},\n   {\"src\": \"SYN\", \"where\": \"Buck 8.13 GARDEN (SYN.txt line 12340)\", \"stance\": \"supports\",\n    \"note\": \"'Av. pairidaéza- ‚hedged-in place‘, perh. ‚garden‘ (cf. NPers. palēz ‚garden‘, and loanwords Grk. παράδεισος, Arm. partēz ‚enclosed garden‘) : pairi-daēzaya- ‚wall about‘' — covers both the root's pairi- and the pālīz of node 2's extras.\"}\n ],\n \"nodes\": []\n}\n\nN = root_entry[\"nodes\"]\n\nN.append({\n \"id\": 1, \"lang\": \"Avestan\",\n \"words\": \"pairi, pari, parâ 3, para 3; pairi-daeza; pairi-vâra; pairi-vaz; pairi-šta; pairi-čayeiti\",\n \"verdict\": \"plausible\",\n \"derivation\": \"The preverb/preposition is genuine: Av. pairi 'around, about' (= OP pariy, Skt. pari, Gk. peri) continues PIE *per-i, the locative of the root noun *per-; Av. para / parō 'beyond, away, before' continues the o-stem *pero-. Pokorny p.810 lists 'ai. pari, av. pairi, apers. pariy' together, so the language label and the gloss 'around, perimeter' are right. (1) pairi-daēza- is Bartholomae's headword (AiW col. 865): 'pairi.daeza- m., Plur. „eine rings-, rundum gehende, sich zusammenschliessende Umwallung, Ummauerung“' (Vd. 3.18) — pairi 'around' + daēza- 'wall (of kneaded clay)' from PIE *dʰeyǵʰ- (hence Nourai's second reference POK:244); confirmed. (2) pairi-vaz- 'to fly around' (pairi + vaz- 'to fly, convey') is Horn no. 305 for NP parvāz, confirmed. (3) pairi-šta = pairi + stā- 'to stand around, attend', the source of MP paristīdan/paristātan 'to serve, worship'; Hübschmann (ad Horn 298) objected that *pari-stā- ought to give NP *paristādan, but MacKenzie's Pahlavi paristīdan [plst-ytn'] 'serve, worship', paristār 'maidservant' and Nyberg's index entry 'parastīdan: paristātan' show the compound is real; plausible. (4) pairi-čayeiti is a 3sg. present of pairi + čay-/či- 'to pick out, discern, sort', the source of پرچین parčīn; Mo'in's footnote in Borhan (p. c. 380) gives exactly 'پرچین = پر — اوستا pairi (پیرامون) + چن (از: چیدن)'; plausible (a 3sg. verb form is an odd citation form for a chart). (5) pairi-vāra- is where Nourai is weakest: the Avestan word is attested at Yt. 1.19 and 13.71 and Hübschmann p.39 (ad Horn 304) insists it means 'Schutzwehr' ('Abwehr' Geldner, 'Wehr' Bartholomae, 'cuirasse par devant' Darmesteter) and 'gehört also nicht zu np. parvār „Mastvieh, Ort wo man Vieh mästet“'. Nourai's gloss 'a barn' follows Horn, whom Mo'in still quotes; modern opinion sides with Hübschmann, so that one gloss is doubtful.\",\n \"derivation_fa\": \"پیشوند اوستایی pairi «پیرامون، گرد» (برابر پارسی باستان pariy و سنسکریت pari) دنبالهٔ صورت مکانی *per-i از ریشهٔ هندواروپایی *per- است؛ صورت para نیز از ستاک *pero- است. یکایک ترکیب‌ها واقعی‌اند: pairi-daēza- در فرهنگ بارتولومه (ستون ۸۶۵) به معنای «دیوار گرداگرد، حصار» آمده؛ pairi-vaz- «گرد چیزی پریدن» بنیاد «پرواز» است (هرن شمارهٔ ۳۰۵)؛ pairi-šta از pairi + stā- «گرد کسی ایستادن، خدمت کردن» سرچشمهٔ «پرستیدن» است؛ و pairi-čay- «گرداگرد چیدن» بنیاد «پرچین» (حاشیهٔ معین بر برهان قاطع: «پر — اوستا pairi + چن از چیدن»). تنها مورد مشکوک معنای pairi-vāra- است؛ هوبشمان (ص ۳۹) می‌گوید این واژه در اوستا «سنگر و باروی دفاعی» است و با «پروار» فارسی به معنای طویله پیوندی ندارد. بنابراین ادعای نورایی در کل با احتیاط پذیرفتنی است.\",\n \"sources\": [W + \"%CF%80%CE%B1%CF%81%CE%AC%CE%B4%CE%B5%CE%B9%CF%83%CE%BF%CF%82\"],\n \"ref_check\": [\n   {\"ref\": \"POK:810\", \"status\": \"supports\", \"note\": \"p.810 'ai. pari, av. pairi, apers. pariy ... ‚ringsum, umherum‘' — the preverb and both glosses.\"},\n   {\"ref\": \"POK:244\", \"status\": \"supports\", \"note\": \"Pokorny 244 is the dʰeiǵʰ- page, cited here for the second element of pairi-daēza-; Watkins repeats it: 'dheigh-. To form, build. ... 7. Suffixed o-grade form *dhoigh-o- in Avestan daēza-, wall (originally made of clay or mud bricks): PARADISE. [Pok. dheigh- 244.]' (AHD_watkins1985.txt line 377).\"}\n ],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"Bartholomae AiW col. 865 (BRT.txt line 15604)\", \"stance\": \"supports\",\n    \"note\": \"'j. pairi.daeza- m., Plur. ‚eine rings-, rundum gehende, sich zusammenschliessende Umwallung, Ummauerung‘: ... V. 3.18' — exactly Nourai's 'walled-in place'.\"},\n   {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien p.39 (ad Horn 304 and 298); HUB.txt leaf 49\", \"stance\": \"partial\",\n    \"note\": \"ad 304: 'Zd. pairivara- heisst yt. 1,19; 13,71 bestimmt ‚Schutzwehr‘ ... Es gehört also nicht zu np. parvār 1) ‚Mastvieh‘, 2) ‚Nahrung‘, 3) ‚Ort, wo man Vieh mästet‘' — contradicts the gloss 'a barn'. ad 298: 'Bei der vorgeschlagenen Etymologie: skr. pari + sthā ‚umstehen‘ erwartet man ein praes. *paristam ... inf. *paristādan (für parastīdan)' — a phonological caveat on pairi-šta.\"},\n   {\"src\": \"SYN\", \"where\": \"Buck 8.13 GARDEN (SYN.txt line 12340)\", \"stance\": \"supports\",\n    \"note\": \"'Av. pairidaéza- ‚hedged-in place‘, perh. ‚garden‘ ... : pairi-daēzaya- ‚wall about‘, Skt. dēhi-, Grk. teichos'.\"},\n   {\"src\": \"BQT\", \"where\": \"Borhan-e Qate', Mo'in's footnote to پرچین, printed p. c.380 (BQT_v1_pages.txt leaf 603)\", \"stance\": \"supports\",\n    \"note\": \"'مرکب از: پر — اوستا pairi (پیرامون) + چن (از: چیدن)' — Mo'in analyses پرچین exactly as Nourai's pairi-čayeiti.\"}\n ]\n})\n\nN.append({\n \"id\": 2, \"lang\": \"Persian\", \"words\": \"pîrâmŭn «پیرامون»\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"NP پیرامون pīrāmūn 'surroundings, perimeter' is inherited unchanged from Middle Persian pērāmōn, written [pyrʾamwn'] in Book Pahlavi and pyrʾamwn in Manichaean script; MacKenzie glosses it 'around' and notes the New Persian reflex with -mūn. The MP form is built on the preverb *pari- with the long vowel of the open syllable (pari- > pēr- exactly as in pērāy-, pērāmixtan), so the first element is Nourai's pairi; MP ē regularly became NP ī (pērāmōn > pīrāmūn), and MP ō became NP ū. Hübschmann already made the identification: 'paz. pērāmūn ‚around‘ Shk. 263 (zu ap. pariy ‚um, über‘?)'. The Persian-script extras in the box are a mixed but defensible list: پردیس / فردوس / پالیز / جالیز all continue *pari-daiza- (فردوس through Arabic firdaws, itself from Greek/Syriac; جالیز is a later variant of پالیز), پروار and پرواز are Horn nos. 304-305, پرستیدن / پرستار are Horn 298 (MP paristīdan, paristār), پرچین is MP parzīn / *pari-či-na-.\",\n \"derivation_fa\": \"«پیرامون» از فارسی میانهٔ pērāmōn (به خط پهلوی کتابی pyrʾamwn') به معنای «گرداگرد» برجا مانده است؛ مکنزی همین معنا را می‌دهد. جزء نخست همان پیشوند *pari- است که در فارسی میانه به pēr- بدل شده (مانند pērāy- در «پیراستن»)؛ سپس ـېـ کشیدهٔ فارسی میانه در فارسی نو به ی و ـۇـ به و (واو معروف) بدل شده است. هوبشمان نیز پیش‌تر نوشته بود: «پازند pērāmūn „around“ ... به پارسی باستان pariy». واژه‌های افزوده در جعبه (پردیس، فردوس، پالیز، جالیز، پروار، پرواز، پرستیدن، پرستار، پرچین) همگی با همین پیشوند ساخته شده‌اند؛ «فردوس» وام‌واژه‌ای است که از راه عربی (firdaws) به فارسی بازگشته است. ادعای نورایی درست است.\",\n \"sources\": [W + \"%D9%BE%DB%8C%D8%B1%D8%A7%D9%85%D9%88%D9%86\"],\n \"ref_check\": [\n   {\"ref\": \"HRN:66\", \"status\": \"partial\",\n    \"note\": \"Horn p.66 (HRN.txt leaf 87) carries nos. 294-298: 'pur', '295. perāgenden ‚zerstreuen‘ ... ap. *para + √kan-', '296. pertew ‚Glanz‘. para + √tap-', '297. perdāḫten', '298. perest', and p.67 continues '298 ... pari + √sthā- ‚um jemand herum stehen‘'. It does support پرستیدن/پرستار of this box's extras, but Horn has NO entry for pīrāmūn, so the citation does not cover the headword itself.\"},\n   {\"ref\": \"BQT:376-91,437\", \"status\": \"supports\",\n    \"note\": \"Within that span Mo'in's footnotes give the pairi- etymologies of the extras: printed p. c.380 (leaf 603) 'پرچین ... مرکب از: پر — اوستا pairi (پیرامون) + چن (از: چیدن)', p. c.392 (leaf 615) 'هرن «پروار» فارسی را بمعنی اصطبل آورده و گوید: در اوستا pairi.vāra ... پهلوی parvār'. (The OCR page numbers of vol. 1 run about leaf−223, so the printed range Nourai gives is right to within a page or two.)\"}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"MacKenzie, CPD p.68 s.v. pērāmōn (PHD_mackenzie.txt line 4196)\", \"stance\": \"supports\",\n    \"note\": \"'pērāmōn [pyrʾamwn' | M pyrʾamwn, N ~mūn] around.' — the direct Middle Persian ancestor, with the New Persian form given.\"},\n   {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien, Part II §8 (HUB.txt line 4584, leaf 141 ≈ printed p.131)\", \"stance\": \"supports\",\n    \"note\": \"'paz. pērāmūn ‚around‘ Shk. 263 (zu ap. pariy ‚um, über‘?)' — Hübschmann himself refers pērāmūn to Old Persian pariy, i.e. to this root.\"},\n   {\"src\": \"MON\", \"where\": \"Mo'in, Farhang-e Farsi s.v. پرواز (MON_part1.txt line 31090)\", \"stance\": \"supports\",\n    \"note\": \"'پرواز: parvāz [در پیرامون پریدن] (ا.)' — Mo'in analyses پرواز as 'flying around', i.e. pairi + vaz-, one of this box's extras.\"},\n   {\"src\": \"PHD\", \"where\": \"MacKenzie, CPD s.v. paristīdan / paristār / parzīn (PHD.txt line 542)\", \"stance\": \"supports\",\n    \"note\": \"'paristār [plstʹ | N parastār] maidservant. paristīdan, parist- [plst-ytn' | M pryst-, N parastīdan] serve, worship ... parzīn [plcyn' | M prcyn, J przyn, (N parčīn)] fence, hedge' — the Middle Persian stage of three of the extras.\"}\n ]\n})\n\nN.append({\n \"id\": 3, \"lang\": \"Greek\", \"words\": \"paradeisos\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Gk. παράδεισος parádeisos 'enclosed park, pleasure-ground' is a 5th-c. BCE borrowing from an Old Iranian (Median/Old Persian) *paridaiza- 'walled enclosure', the exact cognate of Avestan pairi-daēza-; Xenophon uses it repeatedly of the Persian king's hunting parks (Anabasis, Oeconomicus), which is the earliest Greek attestation and fixes the route: Greeks in Achaemenid service took the word directly from spoken Iranian, not from the Avesta. Iranian -ai- was rendered by Greek -ei- and Iranian -z- by -s-, with the Greek masculine ending -os added. The word then passed to the Septuagint for the Garden of Eden (Gen. 2:8), whence Late Latin paradīsus and all the European forms; a parallel Achaemenid-age borrowing gave Hebrew פַּרְדֵּס pardēs and Armenian partēz. Nourai draws the arrow from the Avestan box, which is right in substance (the Greek was taken from an Old Iranian dialect form, Median rather than Avestan proper).\",\n \"derivation_fa\": \"واژهٔ یونانی parádeisos «باغ محصور، شکارگاه شاهی» وام‌واژه‌ای است از ایرانی باستان (مادی/پارسی باستان) *paridaiza-، هم‌ریشه با pairi-daēza- اوستایی. کهن‌ترین گواهی آن در آثار گزنوفون (سدهٔ پنجم پ.م.) است که آن را دربارهٔ باغ‌های شاهان هخامنشی به کار برده است؛ پس وام‌گیری از گفتار زندهٔ ایرانی بوده، نه از متن اوستا. در این وام‌گیری ـaiـ ایرانی با ـeiـ یونانی و z با s نوشته شده و پایانهٔ مذکر os- افزوده شده است. همین واژه در ترجمهٔ هفتادی برای «باغ عدن» به کار رفت و از آنجا به لاتین پسین paradīsus راه یافت؛ عبری pardēs و ارمنی partēz وام‌گیری‌های هم‌زمانند. ادعای نورایی درست است.\",\n \"sources\": [W + \"%CF%80%CE%B1%CF%81%CE%AC%CE%B4%CE%B5%CE%B9%CF%83%CE%BF%CF%82\", \"https://www.etymonline.com/word/paradise\"],\n \"ref_check\": [\n   {\"ref\": \"AHD:950\", \"status\": \"not_checked\",\n    \"note\": \"Nourai's AHD page numbers are to the 1975/76 New College edition's main dictionary (p.950 would fall in the 'par-' range), and that edition is not readable online (the Internet Archive copies are lending-only). The same publisher's root appendix, which IS on disk, carries the claim: AHD_watkins1985.txt line 377 'dheigh- ... Avestan daēza-, wall ...: PARADISE', and line 168 'Iranian *pari-daiza, “walled around,” borrowed into Greek as the word that became English PARADISE'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein s.v. paradise (KLN_1966.txt line 27260)\", \"stance\": \"supports\",\n    \"note\": \"'paradise, n. — ME. paradis, fr. OF. (= F.) paradis, fr. Late L. paradisus, fr. Gk. παραδεισος, ‚park, the garden of Eden, paradise‘, a word of Old Persian origin; cp. Avestic pairidaeza, ‚an enclosure‘, whence Heb. pardes ... Avestic pairidaeza is compounded of pairi, ‚around‘, and daeza, ‚wall‘.'\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat s.v. Paradise (SKT.txt line 13216)\", \"stance\": \"supports\",\n    \"note\": \"'Paradise. (F. — L. — Gk.) ... F. paradis. — L. paradisus. — Gk. [παράδεισος] park, pleasure-ground; ... now ascertained to be of Pers. origin.'\"},\n   {\"src\": \"SYN\", \"where\": \"Buck 8.13 (SYN.txt line 12340)\", \"stance\": \"supports\",\n    \"note\": \"lists 'Grk. παράδεισος, Arm. partēz' as loanwords from Av. pairidaēza-.\"}\n ]\n})\n\nN.append({\n \"id\": 4, \"lang\": \"English\", \"words\": \"paradise\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"The node has no citation in the book, but the chain is uncontroversial: Gk. parádeisos > Late Latin paradīsus (the Vulgate's word for the Garden of Eden) > Old French paradis (11th c., Chanson de Roland) > Middle English paradis (c.1175, Lambeth Homilies) > Modern English paradise. English took it from Old French, not directly from Latin, which is why it has -ise and initial stress. Klein and Skeat give the same chain; the doublet parvis 'church forecourt' entered English by the same route from Medieval Latin Paradisus, the name of the court before St Peter's in Rome.\",\n \"derivation_fa\": \"انگلیسی paradise از راه فرانسهٔ کهن paradis (سدهٔ یازدهم) از لاتین پسین paradīsus و آن از یونانی parádeisos گرفته شده است؛ صورت انگلیسی میانه paradis از است. این جعبه در کتاب بی‌ارجاع است، اما زنجیره نزد کلاین و اسکیت و اتیمانلاین یکسان است و جای چون و چرا ندارد. ادعای نورایی درست است.\",\n \"sources\": [\"https://www.etymonline.com/word/paradise\", W + \"paradise\"],\n \"ref_check\": [\n   {\"ref\": \"(none)\", \"status\": \"not_checked\", \"note\": \"The box carries no reference in the printed chart (refs=None on the page image).\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein s.v. paradise / parvis (KLN_1966.txt lines 27260, 27556)\", \"stance\": \"supports\",\n    \"note\": \"'ME. paradis, fr. OF. (= F.) paradis, fr. Late L. paradisus, fr. Gk. παραδεισος'; and 'parvis ... ME. parvys, fr. OF. parevis, parvis, fr. ML. Paradisus, lit. ‚paradise‘ ... Cp. also parvis, which is a doublet of paradise.'\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat s.v. Paradise (SKT.txt line 13216)\", \"stance\": \"supports\",\n    \"note\": \"'Paradise. (F. — L. — Gk.) ... F. paradis. — L. paradisus.' Skeat's index line 23151 pairs 'paradise — parvis'.\"}\n ]\n})\n\nN.append({\n \"id\": 5, \"lang\": \"Avestan\", \"words\": \"para-kan; para-tab; para-tak\",\n \"verdict\": \"plausible\",\n \"derivation\": \"All three are preverb + verbal root compounds in *para- (Av. para 'away, forth', the o-stem of *per-), reconstructed rather than directly attested in the Avesta — Nourai's 'Avestan' label is really 'Old Iranian'. (1) *para-ā-kan- 'to scatter about': the verb is Cheung's root *kan¹ 'to throw, place, put', not *kan 'to dig', and the prefixed form is attested in Parthian prʾagn- 'to sow, scatter', Sogdian prʾakn-, Choresmian prʾakn- and MP pargan- (< *pari-kan-), which is exactly the double prefix para-ā- Nourai draws. Horn no. 295 gives 'ap. *para + √kan- (?)' with the caveat 'Der Bedeutungswechsel ist allerdings sehr auffällig', and Hübschmann ad 295 objects flatly: 'Np. parāgandan ‚zerstreuen‘, phl. pargandak ‚scattered‘ passt jedenfalls nicht zur Wrzl. kan ‚graben‘. Es gab ja wohl auch noch andere Wurzeln kan oder gan.' Cheung 2007 vindicates Hübschmann's guess by setting up the separate root *kan¹ — for which, however, he gives NO Indo-European etymology ('*PIE — > LIV: – | Pok.:'), so Nourai's cross-reference of this -kan to the root 'Gwhen' (*gʷʰen- 'to strike') is unsupported. (2) *para-tap- 'to shine forth' = para + tap- 'to be hot, glow' (PIE *tep-), Horn no. 296 'pertew ‚Glanz‘. para + √tap-'. (3) *para-tak- 'to run forth' = para + tak- 'to run' (PIE *tekʷ-); here Nyberg prefers pari-: 'From OIr pari + tac-, v. tacitan; Av. (625) pairi-tac- ‚to run round (a p.)‘; (Verbum 227: para + tac-, not probable)'. So the prefix vowel is disputed for the third item, and the PIE anchoring of the first is not established.\",\n \"derivation_fa\": \"هر سه صورت، ساخته‌های پیشوندی با *para- (گونهٔ ستاکی *pero-) اند و بازسازی‌اند، نه مستقیماً اوستایی؛ پس برچسب «اوستایی» را باید «ایرانی باستان» خواند. دربارهٔ *para-ā-kan-، چونگ (۲۰۰۷) ریشهٔ جداگانهٔ *kan «افکندن، پراکندن» را بازسازی می‌کند (جدا از *kanH «کندن، حفر کردن») و صورت پارتی prʾagn- و سغدی prʾakn- «پراکندن، افشاندن» همین دو پیشوند para-ā- را نشان می‌دهد؛ ولی چونگ برای این ریشه هیچ خاستگاه هندواروپایی نمی‌شناسد، پس ارجاع نورایی به ریشهٔ Gwhen (*gʷʰen- «زدن») پشتوانه‌ای ندارد. هوبشمان نیز صریح گفته است: «پراگندن فارسی و pargandak پهلوی به ریشهٔ kan «حفر کردن» نمی‌خورد». دربارهٔ para-tap- و para-tak-، هرن (شماره‌های ۲۹۶ و ۲۹۷) همین تحلیل را می‌دهد، اما نیبرگ برای ـtak پیشوند pari- را درست‌تر می‌داند. پس ادعای نورایی با احتیاط پذیرفتنی است.\",\n \"sources\": [W + \"%D9%BE%D8%B1%D8%AA%D9%88\"],\n \"ref_check\": [\n   {\"ref\": \"POK\", \"status\": \"supports\",\n    \"note\": \"Pokorny 810 and 813-814 cover the para-/*pero- and *pro- preverbs: p.810 'av. pairi ... av. parō Präp. m. Akk. ‚ausser — abgesehen von‘; ai. párā, av. para (Instr. Sg.) adverbal ‚fort, weg, zur Seite‘' (POK_03.txt leaf 45).\"},\n   {\"ref\": \"HUB:39\", \"status\": \"partial\",\n    \"note\": \"Hübschmann's numbered remarks 295-297 straddle pp.38-39 (HUB.txt leaves 48-49). ad 295: 'Np. parāgandan ‚zerstreuen‘, phl. pargandak ‚scattered‘ passt jedenfalls nicht zur Wrzl. kan ‚graben‘.' ad 296: 'Np. partav ‚Licht, Strahl‘ ... mit auffälligem t für d, Anlehnung an tab, taftan etc.?' ad 297 (top of p.39): '...stimmt nicht zu Horn's Etymologie: zd. para + tacay- ‚weglaufen lassen‘.' So the cited page has all three words but questions two of the three derivations.\"},\n   {\"ref\": \"HRN:68\", \"status\": \"partial\",\n    \"note\": \"The three words are actually on Horn pp.66-67 (nos. 295 perāgenden, 296 pertew, 297 perdāḫten), not on p.68; Horn p.68 (leaf 89) has nos. 304-309 (pervār, pervāz, perwerden …), which belong to nodes 1/2 and 7/8. The reference is off by two pages for this box.\"}\n ],\n \"consulted\": [\n   {\"src\": \"CHEUNG\", \"where\": \"Cheung 2007, *kan¹ 'to throw, place, put; to destroy', pp.229-232 (CHEUNG.txt lines 15413-15500)\", \"stance\": \"partial\",\n    \"note\": \"'*PARTHIAN: ... (+ *para-ā-) prʾagn- ‚to scatter, sow‘ || (+ *pari-) prgn- ‚to scatter‘'; '*NWIR: ... (+ *para-ā-) NP parāgandan/parāgan-, parākandan/parākan- ‚to disperse; sow; diffuse‘'. Supports Nourai's para- prefix but assigns the verb to a root with no PIE etymology ('*PIE — > LIV: – | Pok.:'), not to *gʷʰen-.\"},\n   {\"src\": \"NYB\", \"where\": \"Nyberg II s.v. pardaxtan (NYB_vol2_glossary.txt line 2951)\", \"stance\": \"partial\",\n    \"note\": \"'From OIr pari + tac-, v. tacitan; Av. (625) pairi-tac- ‚to run round (a p.)‘; (Verbum 227: para + tac-, not probable)' — Nyberg explicitly prefers pari- to Nourai's para- for para-tak.\"},\n   {\"src\": \"HRN\", \"where\": \"Horn, Grundriss nos. 295-297, pp.66-67 (HRN.txt leaf 87)\", \"stance\": \"supports\",\n    \"note\": \"'295. perāgenden ‚zerstreuen‘ ... ap. *para + √kan- (?)'; '296. pertew ‚Glanz‘. para + √tap-'; '297. perdāḫten ... aw. *para + √tac-' — Nourai's box is Horn's three entries verbatim.\"},\n   {\"src\": \"BRT\", \"where\": \"Bartholomae AiW s.v. tak- / tap- / kan-\", \"stance\": \"silent\",\n    \"note\": \"Grepping BRT.txt for 'para.tak', 'para.tap' and 'para.kan' returns nothing: these prefixed forms are not attested in the Avestan corpus, confirming that the box's forms are Old Iranian reconstructions rather than Avestan citations.\"}\n ]\n})\n\nN.append({\n \"id\": 6, \"lang\": \"Persian\", \"words\": \"parâkandan «پراکندن»; partow «پرتو»; pardâxtan «پرداختن»\",\n \"verdict\": \"plausible\",\n \"derivation\": \"(1) پراکندن parākandan (variant پراگندن parāgandan, pres. stem پراکن parākan-) continues MP pargandan/pargan- [plkn-, plgn-dn'], which MacKenzie glosses 'scatter, distribute, disperse' and equates with Parthian prʾagnd and 'N parāgandan'; the long ā of the New Persian form comes from the double preverb *para-ā-, as the Parthian and Sogdian forms show, while the Book-Pahlavi form has only *pari-. Intervocalic -k- ~ -g- alternation is the usual Middle Persian lenition, whence both پراکندن and پراگندن. Mo'in's footnote in Borhan (printed p. c.388) gives 'مرکب از: پیشوند pairi (پیرامون) + kan (کندن). رک: کندن' — i.e. Mo'in takes the prefix as pairi- and the root as 'to dig', both of which modern work (Cheung) revises. (2) پرتو partow 'beam of light' < *para-tapa-, with the unexpected voiceless -t- that Hübschmann attributed to analogy with تاب/تافتن; the root tap- is PIE *tep- 'to be warm', the same root as تفت and آفتاب. (3) پرداختن pardāxtan 'to finish, to set about, to do' continues MP pardaxtan/pardāz- [pldhtn', pldc-], MacKenzie 'be done with, freed of; set about, undertake'; the past stem -āxt- is the regular outcome of Old Iranian *-āšta- to a root tak-/tac- (cf. tāxtan : tāz-). The semantic path 'let run off' > 'clear, empty' > 'be free for, set about, accomplish' is the one Hübschmann found hard to choose among Vullers' twelve senses. Nourai's gloss 'to do' is the late New Persian sense.\",\n \"derivation_fa\": \"«پراکندن» (گونهٔ «پراگندن»، ستاک حال «پراکن») دنبالهٔ فارسی میانهٔ pargandan/pargan- «پراکندن، پخش کردن» است؛ الف کشیدهٔ فارسی نو از دو پیشوند *para-ā- می‌آید، چنان‌که پارتی prʾagn- و سغدی prʾakn- گواهی می‌دهند؛ ابدال ک/گ میان دو واکه نرم‌شدگی معمول است. معین در حاشیهٔ برهان قاطع این واژه را «پیشوند pairi + kan (کندن)» می‌داند، حال آن‌که چونگ ریشهٔ جداگانهٔ *kan «افکندن» را پیش می‌نهد. «پرتو» از *para-tapa- است (ریشهٔ tap- «تابیدن، گرم بودن»، هم‌ریشه با «تفت» و «آفتاب»)؛ هوبشمان تِّ بی‌واک آن را اثر قیاس با «تاب/تافتن» می‌داند. «پرداختن» از فارسی میانهٔ pardaxtan/pardāz- «فارغ شدن، به کاری پرداختن» است که ستاک گذشتهٔ ـاختـ آن بازتاب *-āšta- از ریشهٔ tak-/tac- «دویدن» است (قیاس کنید با تاختن : تاز-). معنای «انجام دادن» که نورایی آورده معنای متأخر است. روی هم رفته ادعای نورایی با احتیاط پذیرفتنی است.\",\n \"sources\": [W + \"%D9%BE%D8%B1%D8%AA%D9%88\", W + \"%D9%BE%D8%B1%D8%A7%DA%A9%D9%86%D8%AF%D9%86\"],\n \"ref_check\": [\n   {\"ref\": \"BQT\", \"status\": \"partial\",\n    \"note\": \"Mo'in's footnote to پرگندن/پراکندن, Borhan-e Qate' printed p. c.388 (BQT_v1_pages.txt leaf 611): 'مرکب از: پیشوند pairi (پیرامون) + kan (کندن). رک: کندن.' Supports the *per- prefix but gives pairi- where Nourai has para-, and the root 'to dig'.\"},\n   {\"ref\": \"HUB:39\", \"status\": \"contradicts\",\n    \"note\": \"Hübschmann pp.38-39 ad 295 and 297: 'Np. parāgandan ... passt jedenfalls nicht zur Wrzl. kan ‚graben‘' and, of pardāxtan, '... stimmt nicht zu Horn's Etymologie: zd. para + tacay- ‚weglaufen lassen‘. Phl. pardaxt ‚verbraucht‘ Arta-Vīrāf Cap. 89,6 ist unsicher.' The page Nourai cites in fact argues against two of his three arrows (though Cheung has since rescued the first).\"},\n   {\"ref\": \"SNS:133\", \"status\": \"not_found\",\n    \"note\": \"The Shayast ne-Shayast glossary is on disk only as very poor OCR (SNS_pages.txt); greps for 'pargand', 'parward', 'pardax' and for page-133 material returned nothing usable, and the printed page numbers cannot be read from the OCR. Could not confirm what stands on SNS p.133.\"}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"MacKenzie, CPD pp.64-65 (PHD.txt lines 540-542)\", \"stance\": \"supports\",\n    \"note\": \"'pardaxtan, pardāz- [pldhtn', pldc- | M prdxt, N ~], ~ az: be done with, freed of. ~ ō: set about, undertake'; 'pargandan, pargan- [plkn-, plgn-dn' | (P prʾagnd, N parāgandan)] scatter, distribute, disperse' — the Middle Persian ancestors of two of the three words, with the Parthian and New Persian forms.\"},\n   {\"src\": \"CHEUNG\", \"where\": \"Cheung 2007 s.v. *kan¹ (CHEUNG.txt line 15450 ff.)\", \"stance\": \"supports\",\n    \"note\": \"'*NWIR: ... (+ *para-ā-) NP parāgandan/parāgan-, parākandan/parākan- ‚to disperse; sow; diffuse‘, (ppp.) NP parāgandah ‚dispersed, scattered‘ || (+ *pari-) NP pargandah' — the modern standard reference for Iranian verbs, and it gives exactly Nourai's para- for the long-ā form.\"},\n   {\"src\": \"NYB\", \"where\": \"Nyberg II s.v. pardaxtan (NYB_vol2_glossary.txt line 2951)\", \"stance\": \"partial\",\n    \"note\": \"'NP pardāxtan commonly supplanted by the caus. pardāẓatan, pt. pardāḫtah completed, finished, disengaged' — confirms the Middle Persian ancestry but prefers the prefix pari-.\"},\n   {\"src\": \"MON\", \"where\": \"Mo'in via the Borhan footnotes, and MON_part1 s.v. پرتو\", \"stance\": \"silent\",\n    \"note\": \"A grep of MON_part1.txt for a headword 'پرتو:' returns no hit in the available OCR of the lexicon volumes, so Mo'in's own dictionary entry for پرتو could not be read; Wiktionary (archived) supplies the *tep- analysis instead.\"}\n ]\n})\n\nN.append({\n \"id\": 7, \"lang\": \"Avestan\", \"words\": \"par-šti; pari-bar, pari-bahr; pairi-kara\",\n \"verdict\": \"plausible\",\n \"derivation\": \"(1) par-šti is genuinely Avestan: Bartholomae (col. 878) has paršta- m. and paršti- f. 'back', and Pokorny p.813 lists them under the zero-grade *pṛ- of this very root: 'Komposita mit Formen von stā- ‚stehen‘ in ai. pṛ-ṣṭí- f. ‚Rippe‘, pṛ-ṣṭhá-m ‚hervorstehender Rücken, Gipfel‘, av. par-šta- m. ‚Rücken‘, par-šti- f. (Du.) ‚Rücken‘' — so Nourai's gloss 'back (causing to stand up)' and his cross-reference to Stâ are both Pokorny's; Watkins too has 'Compound *pr-st-i- ... “that which stands before,” stake, post (see sta-)'. Confirmed. (2) pari-bar / pari-bahr = pari- + bar- 'to carry' (PIE *bʰer-) is Horn no. 306 ('perwerden ‚ernähren, erziehen‘ ... pari + √bhar-; phlv. parwartan'), but it is rejected by modern Iranian etymology: Cheung 2007 places NP parvardan under the root *u̱arHz 'to (make) grow, nourish', with Parthian prwrz- 'to nurture, care for' and Sogdian prwyj-, and writes of the Choresmian cognate 'Ø Not from the root *bar ‚to carry, bring‘, *pari-bar, as suggested by Samadi'. Disputed. (3) pairi-kara 'going/drawing around, compass' is Vd. 17.6 pairi-kara-, glossed by the Pahlavi version pērāmōn-karišnīh; de Lagarde connected NP پرگار pargar/pargal and پرگر 'necklace' with it, and Hübschmann reports this but ends 'Unsicher' — the dispute recorded in Nourai's own NOTE. Modern Wiktionary sides with de Lagarde: پرگار is 'from Proto-Iranian ... The first element is from Proto-Iranian *pari- ‚around‘, ultimately from Proto-Indo-European *per-', with Sogdian parγarsē 'round, oval' and Sanskrit prakāra- as cognates, i.e. second element *kar- 'to do, make' (Nourai's Kwer). So of the three, one is confirmed, one plausible-to-confirmed, one disputed.\",\n \"derivation_fa\": \"(۱) paršti- درست اوستایی است: بارتولومه (ستون ۸۷۸) paršta- و paršti- «پشت» را ثبت کرده و پوکورنی (ص ۸۱۳) آن را زیر صورت صفردرجهٔ *pṛ- همین ریشه و در ترکیب با stā- «ایستادن» می‌آورد؛ پس هم معنا و هم ارجاع نورایی به ریشهٔ Stâ درست است. (۲) pari-bar «گرداگرد بردن، پروردن» را هرن (شمارهٔ ۳۰۶) پیشنهاد کرده بود، اما ریشه‌شناسی امروزی آن را رد می‌کند: چونگ (۲۰۰۷) «پروردن» را زیر ریشهٔ *u̱arHz «بالیدن، پروردن» می‌آورد (پارتی prwrz-، سغدی prwyj-) و صریح می‌نویسد که از ریشهٔ *bar «بردن» نیست. (۳) pairi-kara- در وندیداد ۱۷؛۶ آمده و ترجمهٔ پهلویاش pērāmōn-karišnīh است؛ دو لاگارد «پرگار» فارسی را بدان بازبسته و هوبشمان (ص ۳۹) پس از نقل آن نوشته «نامطمئن» — همان تردیدی که خود نورایی در یادداشت جعبه آورده است؛ ویکی‌واژه امروز جانب دو لاگارد را می‌گیرد. پس: یکی درست، یکی پذیرفتنی و یکی مردود.\",\n \"sources\": [W + \"%D9%BE%D8%B4%D8%AA\", W + \"%D9%BE%D8%B1%DA%AF%D8%A7%D8%B1\"],\n \"ref_check\": [\n   {\"ref\": \"POK\", \"status\": \"supports\",\n    \"note\": \"Pokorny p.813 (POK_03.txt leaf 46/47): 'Komposita mit Formen von stā- ‚stehen‘ in ai. pṛ-ṣṭí- f. ‚Rippe‘, pṛ-ṣṭhá-m ‚hervorstehender Rücken, Gipfel‘, av. par-šta- m. ‚Rücken‘, par-šti- f. (Du.) ‚Rücken‘, mnd. vorst- f. ‚Dachfirst‘' — exactly the first item of the box, prefix and cross-reference included.\"},\n   {\"ref\": \"HUB:39\", \"status\": \"supports\",\n    \"note\": \"Hübschmann p.39 ad 301 (HUB.txt leaf 49): 'Np. pargal = pargar ‚Zirkel‘ (afgh. pargār ‚Zirkel‘) stellt de Lagarde (Btrg. zur bactr. Lexic. p. 54) nebst pargar ‚Halskette‘ zu zd. pairikara- vd. 17,6 = ‚Turche‘ (phl. pērāmūn-karišnīh) und vergleicht skr. parikara- ‚Gürtel‘. Unsicher.' This is the source of the gloss 'necklace' AND of Nourai's NOTE that HUB:39 is unsure.\"},\n   {\"ref\": \"HRN:68\", \"status\": \"supports\",\n    \"note\": \"Horn p.68 (HRN.txt leaf 89) no. 306: 'perwerden ‚ernähren, erziehen‘, perweriš, perwerīden, pari + √bhar-; phlv. parwartan, parwar(i)šn.' The page cited does say what the arrow says — but it is Horn's 1893 view, which Cheung 2007 abandons.\"}\n ],\n \"consulted\": [\n   {\"src\": \"NYB\", \"where\": \"Nyberg II s.v. pušt (NYB_vol2_glossary.txt line 3187)\", \"stance\": \"supports\",\n    \"note\": \"'pušt [pwšt'] the back ... — MPrs pwš, NP pušt < *pṛšti-; Av. (878) paršta-, paršti-, v. s.v. puštēpān' — Bartholomae's column number for the Avestan word plus the exact Old Iranian preform.\"},\n   {\"src\": \"CHEUNG\", \"where\": \"Cheung 2007, *u̱arHz 'to (make) grow, nourish', p.423 (CHEUNG.txt lines 27343-27400)\", \"stance\": \"contradicts\",\n    \"note\": \"'*MIDDLE PERSIAN: ... (+ *pari-) 1. MMP prwr-, BMP plwl- /parwar-/ ‚to foster, nurture, educate‘'; '*PARTHIAN: ... (+ *pari-) prwrz- ‚to nurture, care for‘'; '*NWIR: ... (+ *pari-) NP parvardan/parvar- ‚to nourish, feed‘, parvardegar'; and of the Choresmian cognate: 'Ø Not from the root *bar ‚to carry, bring‘, *pari-bar, as suggested by Samadi.' Cheung's PIE is *u̱erH₁g-, not *bʰer-.\"},\n   {\"src\": \"PHD\", \"where\": \"MacKenzie, CPD p.65 (PHD.txt line 542) and p.[pušt] (line 551)\", \"stance\": \"supports\",\n    \"note\": \"'parwardan, parwar- [plwl-tn' | M prwrdn, N ~] foster, nourish, cherish, educate'; 'pušt [= M, N ~] back; support, protection' — the Middle Persian stages; MacKenzie has no entry for pargār (silent on the third word).\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. per¹ II.4 (AHD_watkins1985.txt line 837)\", \"stance\": \"supports\",\n    \"note\": \"'II. Zero-grade form *pr-. ... 4. Compound *pr-st-i- (or *por-st-i-, with o-grade form *por-), “that which stands before,” stake, post (see sta-)' — the same *pṛ-sti- formation Nourai puts in the box, with the same cross-reference to stā-.\"}\n ]\n})\n\nN.append({\n \"id\": 8, \"lang\": \"Persian\", \"words\": \"pošt «پشت»; parvardan «پروردن»; pargâr «پرگار»\",\n \"verdict\": \"disputed\",\n \"derivation\": \"پشت pošt is confirmed: Proto-Iranian *pṛštáh > MP pušt [pwšt'] 'back; support, protection' > NP pošt, cognate with Av. paršta- and Skt. pṛṣṭhá-; Nyberg gives the chain explicitly ('MPrs pwš, NP pušt < *pṛšti-; Av. (878) paršta-, paršti-') and the syllabic *ṛ regularly yields Persian u/o before a cluster. پرگار pargār 'pair of compasses' is plausible: Wiktionary derives it from Proto-Iranian with '*pari- ‚around‘' as first element and compares Sogdian parγarsē 'round, oval' and Skt. prakāra-, matching Nourai's pairi-kara and his cross-reference to Kwer (*kʷer- 'to make'); Mo'in defines it only as 'آلتی هندسی برای کشیدن دایره و خطوط' and lists the variants پرگال / پرگر / فرجار (the last an Arabized form), so 'compass' and (via Hübschmann's pargar) 'necklace' are attested but the third gloss 'fortune' is not — no consulted source gives pargār that sense, and it looks like a slip. The node fails on پروردن parvardan: Nourai (with Horn 306) derives it from pari- + bar- 'to carry', but Cheung 2007, the modern standard for Iranian verbs, assigns MP parwar-/parwardan, Parthian prwrz- and Sogdian prwyj- to the root *u̱arHz 'to (make) grow, nourish' (PIE *u̱erH₁g-) and explicitly rejects '*pari-bar'; English Wiktionary, for its part, calls NP پروردن the 'exact cognate to pervert', i.e. *pari-vart- 'to turn about'. Either way the second element is not *bʰer-, so that arrow is disputed; per the rule the whole node takes that verdict.\",\n \"derivation_fa\": \"«پشت» قطعاً درست است: ایرانی باستان *pṛštáh > فارسی میانه pušt > فارسی نو پشت؛ هم‌ریشه با paršta- اوستایی و pṛṣṭhá- سنسکریت؛ نیبرگ همین زنجیره را می‌دهد. «پرگار» با احتیاط پذیرفتنی است: جزء نخست همان *pari- است و جزء دوم ریشهٔ kar- «کردن، ساختن»؛ سغدی parγarsē «گرد، بیضی» و prakāra- سنسکریت هم‌ریشه‌اند. معین تنها معنای «آلتی هندسی برای کشیدن دایره» را می‌آورد؛ معنای «گردن‌بند» از دو لاگارد/هوبشمان می‌آید، ولی معنای «بخت» (fortune) در هیچ منبعی دیده نشد و ظاهراً لغزش مؤلف است. اما «پروردن»: پژوهش امروزی ادعای نورایی (pari + bar «بردن»، بر پایهٔ هرن) را رد می‌کند؛ چونگ (۲۰۰۷) آن را از ریشهٔ *u̱arHz «بالیدن، پروردن» (هندواروپایی *u̱erH₁g-) می‌داند و پارتی prwrz- «پروردن» را گواه می‌آورد؛ ویکی‌واژه نیز آن را هم‌ریشهٔ دقیق pervert یعنی *pari-vart- می‌داند. در هر دو حالت جزء دوم ریشهٔ *bʰer- نیست؛ پس این پیکان مردود است و به حکم قاعده، حکم کل جعبه نیز همین است.\",\n \"sources\": [W + \"%D9%BE%D8%B4%D8%AA\", W + \"%D9%BE%D8%B1%DA%AF%D8%A7%D8%B1\", W + \"%D9%BE%D8%B1%D9%88%D8%B1%D8%AF%D9%86\"],\n \"ref_check\": [\n   {\"ref\": \"BQT\", \"status\": \"partial\",\n    \"note\": \"Borhan-e Qate' with Mo'in's notes has the three headwords in vol. 1 (پشت, پروردن at printed p. c.394 = leaf 617, پرگار), but the OCR of the relevant footnote lines on those leaves carries no Avestan etymology for parvardan or pargār; only the neighbouring پروار note (p. c.392, leaf 615) quotes Horn on pairi.vāra. So Borhan confirms the words but not the arrows.\"},\n   {\"ref\": \"HUB:39\", \"status\": \"supports\",\n    \"note\": \"Supports the NOTE printed in the box: Hübschmann p.39 ad 301 ends the pargār discussion with the single word 'Unsicher.' Nourai's note 'HUB:39 is not sure about the derivation of \\\"pargâr\\\"' is an exact and fair rendering.\"},\n   {\"ref\": \"SNS:133\", \"status\": \"not_found\",\n    \"note\": \"Same as node 6: the Shayast ne-Shayast glossary exists on disk only as unusable OCR (SNS_pages.txt, SNS.txt); greps for 'pušt', 'parward' and 'parg' gave only garbled fragments and the printed pagination is not recoverable from the scan text.\"}\n ],\n \"consulted\": [\n   {\"src\": \"NYB\", \"where\": \"Nyberg II s.v. pušt (NYB_vol2_glossary.txt line 3187)\", \"stance\": \"supports\",\n    \"note\": \"'pušt [pwšt'; Ps. pwšty] the back ... pat ~ būtan to protect, to be the protector ... — MPrs pwš, NP pušt < *pṛšti-; Av. (878) paršta-, paršti-.'\"},\n   {\"src\": \"CHEUNG\", \"where\": \"Cheung 2007 p.423 s.v. *u̱arHz (CHEUNG.txt lines 27386-27400)\", \"stance\": \"contradicts\",\n    \"note\": \"'Ø Not from the root *bar ‚to carry, bring‘, *pari-bar, as suggested by Samadi'; and NP parvardan/parvar- is listed in the *u̱arHz article's NWIR section, beside Parthian prwrz- 'to nurture, care for'.\"},\n   {\"src\": \"MON\", \"where\": \"Mo'in, Farhang-e Farsi s.v. پرگار (MON_part1.txt line 30843)\", \"stance\": \"partial\",\n    \"note\": \"'پرگار: [پرگال – پرگاره – برکار – پرکال – پردال – پرگر – فرجار، معرّب] (ا.) آلتی هندسی برای کشیدن دایره و خطوط' — only 'compass'; no 'fortune' and no 'necklace' in Mo'in.\"},\n   {\"src\": \"PHD\", \"where\": \"MacKenzie, CPD (PHD.txt lines 542, 551)\", \"stance\": \"supports\",\n    \"note\": \"'parwardan, parwar- [plwl-tn' | M prwrdn, N ~] foster, nourish, cherish, educate'; 'pušt [= M, N ~] back; support, protection'. No pargār in the CPD.\"}\n ]\n})\n\nN.append({\n \"id\": 9, \"lang\": \"Avestan\", \"words\": \"fra 2, frank; fra-thang; fra-stâ; fra-aiš, fraĕšta; fra-var; fra-var-tinam\",\n \"verdict\": \"plausible\",\n \"derivation\": \"The head of the box is right: Av. frā/fra- 'forward, forth, away' is the Iranian reflex of PIE *pro (Pokorny p.814: 'ai. prá- Präf. ‚vor, vorwärts, fort‘ ..., av. frā, fra-, ap. fra- Präf. ‚vorwärts, voran; fort, weg‘'), and 'frank' is not a misprint but Bartholomae's headword frāŋk-: BRT has 'j. (frāŋk-) Adj. ‚nach vorn, herzugewendet‘; nur ISn. fračā und NSm. frāš als Adv. ... ‚voran, vorwärts‘', and Mo'in's Borhan footnote to فراز says 'پهلوی frāz (به‌پیش، جلو) از اوستا frāŋk، بارتولمه ۱۰۲۵'. Of the compounds: fra-θang- 'to draw forward' (θang-/θanj- 'to pull') is the source of فرهنگ, and Mo'in says so verbatim ('از: فر (پیشاوند) + هنگ (از ریشهٔ thang اوستایی بمعنی کشیدن)'); fra-stā- 'to stand/send forth' underlies MP frēstīdan/frastātan and NP فرستادن, and Mann's IEC entry 'peri-sthā-' likewise cites 'Per. firistam, v. ‚send‘'; fra-var- gives Av. fravaši- > MP frawahr > NP فروهر, and its genitive plural (Av. fravašinqm, OIr. *fravartinām) gives MP frawardin > NP فروردین, both of which Mo'in's footnotes confirm. The one faulty item is 'fra-aiš, fraēšta': the word is real — Av. fraēšta- 'messenger' (Wiktionary s.v. فرشته), MP frēstag 'apostle, angel' — but it belongs to the root aiš-/iš- 'to set in motion, send', not to Stā, so Nourai's cross-reference '☞ Stâ' on that line is an error (evidently carried down from the fra-stā line above it).\",\n \"derivation_fa\": \"سرامد جعبه درست است: پیشوند اوستایی frā/fra- «پیش، به‌سوی جلو، دور» بازتاب *pro هندواروپایی است (پوکورنی ص ۸۱۴). «frank» نیز غلط چاپی نیست بلکه همان سرواژهٔ frāŋk- بارتولومه «روبه‌جلو، پیش‌روی» است که معین در حاشیهٔ «فراز» می‌آورد: «پهلوی frāz از اوستا frāŋk، بارتولمه ۱۰۲۵». از میان ترکیب‌ها: fra-θang- بنیاد «فرهنگ» است (معین: «فر + هنگ از ریشهٔ thang اوستایی به معنی کشیدن»)؛ fra-stā- بنیاد «فرستادن» (فارسی میانه frastātan)؛ fra-var- بنیاد «فروهر» (اوستا fravaši-، پهلوی frawahr) و صورت جمع اضافی آن بنیاد «فروردین» (پهلوی frawardin). تنها لغزش در سطر «fra-aiš, fraēšta» است: خود واژه درست است (اوستا fraēšta- «فرستاده، پیک»، پهلوی frēstag «فرشته»)، اما از ریشهٔ aiš-/iš- «روانه کردن» است نه از stā-؛ پس ارجاع «☞ Stâ» در آن سطر خطاست (از سطر پیشین فروافتاده است). روی هم رفته ادعای نورایی با احتیاط پذیرفتنی است.\",\n \"sources\": [W + \"%D9%81%D8%B1%D8%B4%D8%AA%D9%87\"],\n \"ref_check\": [\n   {\"ref\": \"HRN:184\", \"status\": \"partial\",\n    \"note\": \"Horn p.184 (HRN.txt leaf 205) has nos. 826-830: 'frīh ‚viel, mehr‘ ... aw. vergl. frāyāo, fraēšta-; phlv. frah, frahist', '827. ferī ‚lieb, schön‘. aw. frya-', '828. feryād ‚Hilfe; Hilferuf‘. aw. frāδāta- ‚Gedeihen, Förderung‘ (yt. 13,68); phlv. frayāt bezw. fradāt ‚Hilfe‘', '829. firēften'. The page is genuinely about fra- words and no. 826 even cites Av. fraēšta- (there as the superlative 'most'), but the specific compounds of this box (fra-θang, fra-stā, fra-var) are not on it — no. 828 belongs to node 12.\"},\n   {\"ref\": \"BQT:1442-82\", \"status\": \"supports\",\n    \"note\": \"Within that span Mo'in's footnotes give exactly these etymologies. Printed p. c.1447 (BQT_v3_pages.txt leaf 238, pdf 239), s.v. فراز: 'پهلوی frāz (به‌پیش، جلو، اینجا) از اوستا - frāŋk، بارتولمه ۱۰۲۵.' Printed p. c.1482 (leaf 273), s.v. فرهنگ: 'از: فر (پیشاوند) + هنگ (از ریشهٔ thang اوستایی بمعنی کشیدن).' Printed p. c.1461 (leaf 252), s.v. فرستادن: 'پهلوی frastātan'. Printed p. c.1479 (leaf 270), s.v. فروهر: 'پهلوی frawahr، ایرانی باستان *fravarti، اوستا fravaši-: بارتولمه'. Printed p. c.1477 (leaf 268), s.v. فروردین: 'پهلوی fravartin مأخوذ از پارسی باستان ... در اوستا نیز این کلمه به‌هیأت اضافه در جمع مؤنث بسیار آمده'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"Bartholomae AiW col. 1025 s.v. frāŋk- (BRT.txt line ~18325)\", \"stance\": \"supports\",\n    \"note\": \"'j. (frāŋk-) Adj. ‚nach vorn, herzugewendet‘; nur ISn. fračā und NSm. frāš als Adv. 1) fračā ‚voran, hervor‘ ... 2) frāš a) ‚voran, vorwärts‘ ... Ableit. aus *fra; ... ai. prāŋk- : prāk-; aip. frači, frāči, op. parā ... Pa.: frāẓ.' Nourai's 'frank' is this headword; the cross-reference 'frāš Adv.: s. frāŋk-' stands at BRT.txt line 18332.\"},\n   {\"src\": \"PHD\", \"where\": \"MacKenzie, CPD s.v. frāz and frēstag (PHD.txt line 347; PHD_pages.txt line 2393)\", \"stance\": \"supports\",\n    \"note\": \"'frāz [plʾc | M prz, N faraz] forth, forward'; 'frēstag [plystk' | M prystg, (N firišta)] apostle, angel' — the Middle Persian links for فراز and فرشته.\"},\n   {\"src\": \"POK\", \"where\": \"Pokorny 814 (POK_03.txt leaf 47)\", \"stance\": \"supports\",\n    \"note\": \"'g. pro, prō ‚vorwärts, vorn, voran‘ ... Ai. prá- Präf. ‚vor, vorwärts, fort‘ ..., av. frā, fra-, ap. fra- Präf. ‚vorwärts, voran; fort, weg‘' — puts the Iranian fra- under the same lemma as pairi-, as Nourai's chart does.\"},\n   {\"src\": \"IEC\", \"where\": \"Mann, IEC s.v. peri-sthā- (IEC.txt line 12724)\", \"stance\": \"partial\",\n    \"note\": \"'peri-sthā- Skt. pari-sthā-, v. ‚encompass; obstruct‘; Per. firistam, v. ‚send‘; ... Gk. periistēmi ‚go round, surround‘' — Mann derives Persian 'to send' from *pari-stā- rather than *fra-stā-, a variant of the prefix.\"}\n ]\n})\n\nN.append({\n \"id\": 10, \"lang\": \"Persian\", \"words\": \"farâ «فرا»\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"NP فرا farā is the inherited free form of the preverb: Old Iranian frā (long-grade adverbial beside fra-) > MP frā > NP farā, with the regular New Persian prothetic/anaptyctic vowel that breaks the initial cluster (fr- > far-, exactly as frāz > فراز, frēstag > فرشته). Mo'in's Borhan footnote (printed p. c.1444) reads 'فرا farā پیشوند (= بسوی، جلو) = سانسکریت prāk (پیش، جلو)، اوستا fra ... چنان‌که در کلمات: فرخجسته، فرسوده، فرمان؛ در پارسی باستان و اوستا fra، پهلوی fra، ... هندی باستان pra', which is Nourai's node word for word. The comparative فراتر farātar carries the Iranian comparative -tara-, i.e. *fra-tara-, the same formation as the Sogdian frtr of node 11 and Av. fratara- (Pokorny p.815). The other script extras belong to the compounds of node 9: فراگرفتن, فراز, فراسو, فرهنگ, فرستادن, فرشته, فروهر, فروردین, فردین (a contracted by-form of فروردین).\",\n \"derivation_fa\": \"«فرا» صورت آزاد همان پیشوند است: ایرانی باستان frā > فارسی میانه frā > فارسی نو فرا، با افزودن واکهٔ میانجی که خوشهٔ آغازین fr- را می‌شکند (همان‌گونه که frāz > فراز و frēstag > فرشته). معین در حاشیهٔ برهان قاطع می‌نویسد: «فرا farā، پیشوند (= بسوی، جلو) = سانسکریت prāk، اوستا و پارسی باستان fra، پهلوی fra». «فراتر» پسوند برتری ـtara- ایرانی را دارد، یعنی *fra-tara-، همان ساخت که در frtr سغدی و fratara- اوستایی دیده می‌شود. دیگر واژه‌های جعبه همان ترکیب‌های جعبهٔ پیشین‌اند. ادعای نورایی درست است.\",\n \"sources\": [W + \"%D9%81%D8%B1%D8%B4%D8%AA%D9%87\"],\n \"ref_check\": [\n   {\"ref\": \"BQT:1446\", \"status\": \"supports\",\n    \"note\": \"Mo'in's footnote at the فرا entry, BQT_v3_pages.txt leaf 235 (pdf page 236 ≈ printed 1444; the vol.3 offset drifts by 1-2 pages): '۱ - fara پیشوند (= بسوی) = سانسکریت prāk (پیش، جلو) اوستا ... جلو، بسوی جلو وغیره؛ چنانکه در کلمات: فرخجسته، فرسوده، فرمان؛ درپارسی باستان و اوستا fra ... پهلوی fra، ... هندی باستان pra.'\"},\n   {\"ref\": \"BQT:1482\", \"status\": \"supports\",\n    \"note\": \"Printed p. c.1482 (leaf 273) is the فرهنگ entry, whose footnote reads 'از: فر (پیشاوند) - هنگ (از ریشهٔ thang اوستایی بمعنی کشیدن)' — one of this box's script extras, referred to the same prefix.\"}\n ],\n \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"Mo'in, Farhang-e Farsi s.v. فرا (MON_part2.txt line 5448)\", \"stance\": \"supports\",\n    \"note\": \"'فرا: (پیشوند) بر سر فعل درآید و آن در اصل به معنی به، سوی، در باشد. (حرف اضافه) ... به، سوی، جانب. (ص.) بلند، عالی' — 'forward' and, in the adjectival use, 'high, superior', i.e. Nourai's 'forward, more'.\"},\n   {\"src\": \"PHD\", \"where\": \"MacKenzie, CPD s.v. frāz (PHD.txt line 347)\", \"stance\": \"supports\",\n    \"note\": \"'frāz [plʾc | M prz, N faraz] forth, forward: ~ abgandan: throw forward ... ~ griftan: undertake, perform' — the Middle Persian free preverb with the New Persian form spelled out.\"},\n   {\"src\": \"HRN\", \"where\": \"Horn, Grundriss no. 826, p.184 (HRN.txt leaf 205)\", \"stance\": \"partial\",\n    \"note\": \"'826. frīh ‚viel, mehr‘. aw. vergl. frāyāo, fraēšta-; phlv. frah, frahist' — Horn's nearest entry, which shows the 'more' sense of the fra- family that Nourai gives فرا, though he has no separate فرا entry.\"}\n ]\n})\n\nN.append({\n \"id\": 11, \"lang\": \"Sogdian\", \"words\": \"frtr\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Sogdian frtr, vocalized fratar, is the comparative *fra-tara- 'further, higher' > 'more, better', formed with the Indo-Iranian comparative suffix *-tara- on the preverb fra-. Gharib's dictionary, at exactly the page Nourai cites, has entry 3926: 'frtr M, C — fratar © < Av. fratara © pl. -t ⇒ ftʾar, prtr¹, δPrtr — more, better', i.e. the Manichaean and Christian Sogdian spellings of one word, with the Buddhist variant ftʾar and the accompanying adverb frtryʾ. The Avestan comparative fratara- 'the former, the foremost' is itself listed by Pokorny (p.815) under *pro-tero-, beside Gk. próteros and Skt. pratarám, so the whole chain root > fra- > fratara- > Sogdian frtr is sound. The semantic step 'further forward' > 'superior, better' is the same one seen in Av. fratama-/OP fratama- 'foremost, first'.\",\n \"derivation_fa\": \"واژهٔ سغدی frtr (خوانده fratar) صورت برتری *fra-tara- است، ساخته از پیشوند fra- و پسوند برتری هندوایرانی ـtara-. فرهنگ سغدی بدرالزمان قریب در همان صفحهٔ ۱۵۵ (مدخل ۳۹۲۶) می‌آورد: «frtr M, C — fratar < اوستا fratara — more, better». صورت اوستایی fratara- را پوکورنی (ص ۸۱۵) زیر *pro-tero- در کنار próteros یونانی و pratarám سنسکریت می‌آورد؛ پس زنجیرهٔ ریشه > fra- > fratara- > frtr سغدی استوار است. دگرگونی معنایی «پیش‌تر» > «برتر، بهتر» همان است که در fratama- اوستایی و پارسی باستان «نخست، سرور» دیده می‌شود. ادعای نورایی درست است.\",\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"SOD:155\", \"status\": \"supports\",\n    \"note\": \"Gharib, Sogdian Dictionary, printed p.155 (SOD_pages.txt leaf 221; printed ≈ leaf − 66), entry 3926: 'frtr M, C — fratar © < Av. fratara © pl. -t ⇒ ftʾar, prtr¹, δPrtr — more, better — BBB e12; GMS 437; STi 8.11, 10.11; C2, 120V2'. The page number and the gloss are exactly Nourai's.\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"Pokorny 815 (POK_03.txt leaf 48)\", \"stance\": \"supports\",\n    \"note\": \"'prō-tero- in ai. pratarám, -am Adv. ‚weiter, künftig‘, av. fratara- ‚der vordere, frühere‘, gr. próteros ‚der vordere, vorige‘ ... dazu mit Superlativsuffix -temo-: ... av. fratəma-, ap. fratama- ‚der vorderste, vornehmste, erste‘' — the Avestan base of the Sogdian word, under this root.\"},\n   {\"src\": \"SOD\", \"where\": \"Gharib, cross-references in the same dictionary (SOD_pages.txt lines 15135, 24514)\", \"stance\": \"supports\",\n    \"note\": \"'f(a)tar © < *fra-tara ⇒ ftʾar, frtr' and 'fratar © < Av. fratara ⇒ frtr, δPrtr' — the Buddhist-Sogdian spelling variants confirm the reading fratar and the preform *fra-tara-.\"},\n   {\"src\": \"PHD\", \"where\": \"MacKenzie, CPD (grep for 'fratar', 'fradār')\", \"stance\": \"silent\",\n    \"note\": \"MacKenzie has no Middle Persian *fratar; the comparative survives in Persian only in فراتر (node 10's extras), so the Sogdian form is the best attestation, as Nourai's chart implies by giving it its own box.\"}\n ]\n})\n\nN.append({\n \"id\": 12, \"lang\": \"Avestan\", \"words\": \"fra-â-marz; fara-mana; fra-dâta; fra-jâma; fra-vaxš\",\n \"verdict\": \"plausible\",\n \"derivation\": \"A second box of *fra- compounds, again Old Iranian reconstructions rather than attested Avestan citation forms. (1) fra-ā-marz- = fra + ā + marz- 'to wipe, stroke' (PIE *melǵ- 'to rub, wipe', Nourai's Mĕlg); the same verb gives فراموش 'forgotten' (Mo'in, Borhan p. c.1449: 'پهلوی framoš ... از framurš-'), and Nourai's gloss 'one who forgives all' for the epic name فرامرز rests on the 'wipe away (a fault)' sense — semantically attractive, phonetically regular, but the name is more often read as frā-marz 'he who wipes out (the enemy)'. Plausible. (2) fara-mana: the standard analysis of MP framān 'order, command' (MacKenzie: 'framān [plmʾan' | M frmn, N farmān]') is *fra-mā-na- 'what is measured out, ordained' from mā- 'to measure' — which is exactly where Nourai's cross-reference '☞ Me' points, so his transliteration '-mana' hides a root mā-, not man- 'to think'. Mo'in's Borhan footnote (p. c.1470) gives 'فرمای ... اسم از فرمودن؛ پهلوی framān (امر)، ایرانی باستان ...'. (3) fra-dāta is Av. frāδāta- 'furtherance, prosperity' (Yt. 13.68), MP frayāt/fradāt 'help' > NP فریاد 'cry for help' — Horn no. 828, confirmed. (4) fra-jāma = *fra-jāma- from jam-/gam- 'to go' (PIE *gʷem-, Nourai's Gwa), 'the end of going'; MP frazām 'end, completion' (MacKenzie has frazām-, frazāft, frazāmēnīdan) > NP فرجام, the j of the New Persian form being a Parthian-type retention beside the Middle Persian z. (5) fra-vaxš = fra + vak-/vac- 'to speak' (PIE *wekʷ-, Nourai's Wekw) 'to call out (wares)' > فروختن 'to sell'; Mo'in states it outright at Borhan p. c.1474: 'فروختن ... اوستا fra + vaxsh ... (صدا کردن، بمعرض فروش گذاشتن)'. Confirmed.\",\n \"derivation_fa\": \"این جعبه نیز ترکیب‌های *fra- است، بازسازی‌شده نه مستقیماً اوستایی. (۱) fra-ā-marz- از ریشهٔ marz- «ستردن، مالیدن» (هندواروپایی *melǵ-) است؛ همین ریشه «فراموش» را نیز داده (حاشیهٔ معین: «پهلوی framoš از framurš-»)؛ معنای «همه‌بخشای» که نورایی برای نام «فرامرز» می‌دهد پذیرفتنی است ولی بسیاری آن را «سترندهٔ دشمن» خوانده‌اند. (۲) «فرمان» از فارسی میانه framān است که به *fra-mā-na- از ریشهٔ mā- «اندازه گرفتن، مقرر کردن» باز می‌گردد — دقیقاً همان ریشه‌ای که نورایی با ارجاع «Me» بدان اشاره کرده، هرچند آوانویسی ـmana ممکن است خواننده را به ریشهٔ man- «اندیشیدن» بیندازد. (۳) frāδāta- اوستایی «بالندگی، یاری» (یشت ۱۳؛۶۸)، پهلوی frayāt/fradāt «یاری»، بنیاد «فریاد» است (هرن شمارهٔ ۸۲۸). (۴) *fra-jāma- از jam-/gam- «رفتن»، پهلوی frazām «انجام، پایان» > «فرجام». (۵) fra-vaxš از vak-/vac- «گفتن، ندا در دادن» > «فروختن»؛ معین به صراحت می‌نویسد: «اوستا fra + vaxsh ... (صدا کردن، بمعرض فروش گذاشتن)». روی هم رفته ادعای نورایی با احتیاط پذیرفتنی است.\",\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"HRN:184\", \"status\": \"supports\",\n    \"note\": \"Horn p.184 (HRN.txt leaf 205) no. 828: 'feryād ‚Hilfe; Hilferuf, Klage‘. aw. frāδāta- ‚Gedeihen, Förderung‘ (yt. 13, 68); phlv. frayāt bezw. fradāt ‚Hilfe‘. Die mittelpersische Bedeutung ‚Hilfe‘ findet sich auch noch im Neupersischen.' That is Nourai's 'fra-dāta: promotion, call for help' word for word.\"},\n   {\"ref\": \"BQT:1442-82\", \"status\": \"supports\",\n    \"note\": \"Borhan-e Qate', Mo'in's footnotes: printed p. c.1474 (BQT_v3_pages.txt leaf 265) 'فروختن ... اوستا fra + vaxsh ... چنانکه baxsh از hac (صداکردن، بمعرض فروش گذاشتن)؛ پهلوی ...'; printed p. c.1470 (leaf 261) 'فرمای ... اسم از «فرمودن»؛ پهلوی framān (امر)، ایرانی باستان ...'; printed p. c.1449 (leaf 240) 'پهلوی framoš (از ... بردن)، پازند farmāsh ... هرن و هوبشمان گوید: فراموش پهلوی باید از framuš از framurš- ...' — three of the five compounds, at pages inside Nourai's range.\"}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"MacKenzie, CPD s.v. framān, frazām- (PHD.txt lines 325, 352)\", \"stance\": \"supports\",\n    \"note\": \"'framān [plmʾan' | M frmn, N farmān] order, command; a minor degree of sin'; 'frazāmēnīdan, frazāmēn- [plcʾamyn-ytn'] = frazāftan' (and index 'frazām') — the Middle Persian stages of فرمان and فرجام.\"},\n   {\"src\": \"HRN\", \"where\": \"Horn, Grundriss no. 828 and the surrounding fra- entries, p.184\", \"stance\": \"supports\",\n    \"note\": \"See the ref_check quote; Horn treats the whole فر- family of this box as fra- compounds.\"},\n   {\"src\": \"BRT\", \"where\": \"Bartholomae AiW, grep for 'fra.δāta', 'fra.vaxš', 'fra.jāma'\", \"stance\": \"silent\",\n    \"note\": \"The OCR of BRT.txt yields no clean hit for these compound headwords (the transliteration diacritics are badly scanned), so Bartholomae could not be used to confirm the Avestan citation forms directly; Horn's and Mo'in's citations (frāδāta- Yt. 13.68) stand in for it.\"}\n ]\n})\n\nN.append({\n \"id\": 13, \"lang\": \"Persian\", \"words\": \"\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"A pass-through box with no transliterated headword: it merely carries the Persian-script outcomes of node 12 — فرامرز and فرمان (< *fra-ā-marz-, *fra-mā-na-), فریاد and فرجام (< Av. frāδāta-, *fra-jāma- via MP frayāt and frazām), and فروختن (< *fra-vakš-). Each line of the box corresponds to one line of the Avestan box above it, in the same order, and every one of the five is a regular New Persian continuation of a Middle Persian form attested in MacKenzie (framān, frazām, frōxtan/frōš-) or in Horn (frayāt > فریاد). The New Persian shape in every case shows the same anaptyxis fr- > far-/fir- that produced فرا in node 10.\",\n \"derivation_fa\": \"این جعبه سرواژهٔ آوانویسی‌شده ندارد و تنها برآیندهای فارسی جعبهٔ بالایی را به خط فارسی می‌آورد: فرامرز و فرمان (از *fra-ā-marz- و *fra-mā-na-)، فریاد و فرجام (از frāδāta- اوستایی و *fra-jāma-، از راه فارسی میانهٔ frayāt و frazām) و فروختن (از *fra-vakš-). هر سطر برابر یک سطر جعبهٔ اوستایی بالاست و همه دنبالهٔ صورت‌های پهلوی اند که در فرهنگ مکنزی یا در هرن ثبت شده‌اند؛ در همه همان واکهٔ میانجی fr- > فرـ دیده می‌شود. ادعای نورایی درست است.\",\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"BQT:1482\", \"status\": \"partial\",\n    \"note\": \"Printed p. c.1482 in vol. 3 (BQT_v3_pages.txt leaf 273) is the فرهنگ/فری- stretch of the dictionary, and leaf 274 (p. c.1483) has فریادخوان and the فری/فریب footnotes ('فری ... از اوستا - frya (دوست، محبوب)، هندی باستان priyā'). So the single page Nourai cites covers only فریاد of this box's five words; فرمان (p. c.1470), فروختن (p. c.1474) and فراموش/فرامرز (p. c.1449) lie earlier in the volume.\"}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"MacKenzie, CPD (PHD.txt lines 325, 352, 4661-4663)\", \"stance\": \"supports\",\n    \"note\": \"'framān [plmʾan' | M frmn, N farmān] order, command'; 'frazām', 'frazāftan', 'frazāmēnīdan' — the Middle Persian ancestors of فرمان and فرجام.\"},\n   {\"src\": \"HRN\", \"where\": \"Horn, Grundriss no. 828, p.184\", \"stance\": \"supports\",\n    \"note\": \"'feryād ‚Hilfe; Hilferuf‘ ... phlv. frayāt bezw. fradāt ‚Hilfe‘' — covers فریاد.\"},\n   {\"src\": \"MON\", \"where\": \"Mo'in via his Borhan footnotes, printed pp. c.1449, c.1470, c.1474\", \"stance\": \"supports\",\n    \"note\": \"The فراموش, فرمان and فروختن notes quoted under node 12 give the Avestan/Old Iranian sources of three more of this box's words.\"}\n ]\n})\n\nout = {\n \"pdf_page\": 393,\n \"book_page\": 363,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-13\",\n \"entries\": [root_entry]\n}\n\nimport io\nwith io.open('/home/sfmqrb/git/rishe/data/verification/page-393.json','w',encoding='utf-8') as f:\n    json.dump(out, f, ensure_ascii=False, indent=2)\nprint(\"ok\", len(N))\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build393.py && python3 -m json.tool data/verification/page-393.json > /dev/null && echo \"valid json\"",
 "description": "Build page-393.json"
}
```


### [2026-09-14T01:13:31.147Z] TOOL RESULT

```
ok 13
valid json
```


## [2026-09-14T01:13:35.014Z] TOOL CALL #66: Bash

```json
{
 "command": "python3 tools/verify_check.py 393",
 "description": "Run verify_check for page 393"
}
```


### [2026-09-14T01:13:36.356Z] TOOL RESULT

```
nodes verified: 13/13
node verdicts: {'plausible': 6, 'confirmed': 6, 'disputed': 1}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 14, 'partial': 7, 'not_checked': 2, 'contradicts': 1, 'not_found': 2}
books consulted: {'supports': 32, 'partial': 7, 'silent': 4, 'contradicts': 2} | by book: {'PHD': 10, 'MON': 5, 'BRT': 4, 'CHEUNG': 4, 'NYB': 4, 'HRN': 4, 'HUB': 2, 'SYN': 2, 'KLN': 2, 'SKT': 2, 'POK': 2, 'BQT': 1, 'AHD': 1, 'IEC': 1, 'SOD': 1}
```


## [2026-09-14T01:13:58.633Z] AGENT

Done. Wrote `/home/sfmqrb/git/rishe/data/verification/page-393.json`; `verify_check.py 393` reports 0 PROBLEM lines.

**Page 393 (book p. 363) — root "Per 1" (PIE *per-/*per-i), 1 entry, 13 nodes**

Verdicts: root confirmed; nodes 6 confirmed, 6 plausible, 1 disputed.
Ref checks: 14 supports, 7 partial, 1 contradicts, 2 not_found, 2 not_checked. 15 different books consulted (POK/WLD/AHD/IEC/SYN, BRT/NYB/PHD/CHEUNG/HRN/HUB/SOD, BQT/MON, KLN/SKT).

- **disputed — node 8, پروردن parvardan** (Nourai: Av. *pari-bar-* "carry around", after Horn 306). Cheung 2007 p.423 puts NP parvardan under the root *u̯arHz "to nourish, make grow" (Parth. prwrz-, Sogd. prwyj-) and writes explicitly "Not from the root *bar 'to carry, bring', *pari-bar"; Wiktionary instead makes it the exact cognate of Latin *pervertere* (*pari-vart-). Either way the second element is not *bʰer-.
- **node 8, پرگار gloss "fortune"** — unattested: Mo'in gives only "compass"; "necklace" comes from de Lagarde via Hübschmann. Book's own NOTE ("HUB:39 is not sure") is exactly right — Hübschmann p.39 ends the pargār discussion with "Unsicher"; modern Wiktionary nevertheless backs the *pari-kar- analysis.
- **node 9, line "fra-aiš, fraĕšta ☞ Stâ"** — the word is right (Av. fraēšta- "messenger" → MP frēstag → فرشته) but it belongs to the root aiš-/iš- "to send", not to Stā; the cross-reference has evidently slipped down from the fra-stā line above.
- **node 1, pairi-vâra "a barn"** — Hübschmann p.39 (ad Horn 304) insists the Avestan word means "Schutzwehr" and does not belong with NP parvār "stable"; Nourai follows Horn.
- **node 5/6, para-kan ☞ Gwhen** — Cheung's root *kan¹ "to throw, scatter" (which does vindicate Nourai's *para-ā-* prefix against Hübschmann's objection) has **no** PIE etymology at all, so the link to *gʷʰen- is unsupported.
- Citation slips (not data errors): HRN:68 on node 5 should be HRN:66–67; HRN:66 on node 2 does not contain pīrāmūn at all (Hübschmann §8 does).

**No extraction errors.** I checked the rendered page (copied to `data/verification/sources/refs/ocr/BOOK/393.png`): "frank" is faithful and is Bartholomae's Avestan headword frāŋk- (AiW col. 1025, confirmed by Mo'in's Borhan footnote to فراز), "pîrâmŭn", "fraĕšta", "pairi-čayeiti", the Ferdowsî quote and all refs match the JSON exactly.

SNS:133 could not be checked for nodes 6 and 8 — the Shāyast nē-Shāyast glossary is on disk only as unusable OCR with no recoverable pagination.
