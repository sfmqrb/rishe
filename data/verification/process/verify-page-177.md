# Verification process log — verify-page-177


## [2026-09-05T20:51:19.162Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 177 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-177.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-177.json. Write /home/sfmqrb/git/rishe/data/verification/page-177.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 177` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-05T20:51:20.677Z] AGENT

I'll start by reading the instructions.


## [2026-09-05T20:51:21.389Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-05T20:51:21.403Z] TOOL RESULT

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


## [2026-09-05T20:51:21.662Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-177.txt"
}
```


### [2026-09-05T20:51:21.679Z] TOOL RESULT

```
1	=== PDF page 177 (book page 147) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Gĕu 1, Gu; Keu 1, Keup, Kumb, Kub, Keub, Keuk 2 : to bend; to bend, curved, hump  (refs POK:394-398; POK:588-592)  PART 2
4	#1 (parent #0) [Avestan] refs=POK:591,592; KLN:391 | kaofa : mountain ; xumba : bent container, pot
5	  #2 (parent #1) [Pahlavi] refs=HRN:195 | kôf : mountain ; xombak : a jar
6	    #3 (parent #2) [Persian] refs=BQT:768,1739; WLD1:376 | kŭh «کوه» : mountain ; kohân «کوهان» : camel's hump ; xom «خُم ۱» : jar | extra: کوهه ؛ خمره
7	#4 (parent #0) [Avestan] refs=POK:395,588 | kava : humped ; fra-kava : humped front ; apa-kava : humped back
8	#5 (parent #0) [Latin] refs=AHD | cuppa : curved-in pot ; cymbalon : curved-in plate
9	  #6 (parent #5) [Arabic] refs=ARK:223; TAD:44 | koab : cup ; akvâb : cups ; sanj : cymbal
10	    #7 (parent #6) [Persian] refs=MON:332,1336; TAD:44 | akvâb «اکواب» : cups, jars ; sanj «صنج» : cymbal | extra: سنج | NOTE: See root "Keg" for another possible derivation.
11	  #8 (parent #5) [English] refs=None | cup, hump, cymbal
12	#9 (parent #0) [Germanic] refs=AHD | haup : heap
13	  #10 (parent #9) [English] refs=None | heap, hip, high. height
14	--- entry 1 ---
15	ROOT [Indo-European] Geu 2, Geua : to hasten  (refs POK:399)
16	#1 (parent #0) [Avestan] refs=POK:399; BQT:148 | zavah, zâvar : power, force ; api-zâwar : tool
17	  #2 (parent #1) [Persian] refs=POK:399; BQT:148; HRN:149 | zŭr 1 «زور ۱» : force, power ; zâvar «زاوَر» : power, force ; zâv «زاو» : powerful, strong ; abzâr, afzâr «ابزار ، افزار» : tools | NOTE: For a different derivation of "abzâr & afzâr" see root "Ghei 2".
18	#3 (parent #0) [Avestan] refs=POK:399; HUB:16 | zava : haste ; aiwi-zâvayeiti : adds up ☞Ambhi
19	  #4 (parent #3) [Persian] refs=POK:399; BQT:1043; HRN:149; HUB:16 | zŭd «زود» : fast, soon ; afzŭdan «افزودن» : to increase | extra: افزایش ، افزون ، فزون
20	#5 (parent #0) [Old Persian] refs=SOD:103 | abi-jâvaya : to increase ☞Ambhi
21	  #6 (parent #5) [Sogdian] refs=SOD:103 | bj`w : to increase
22	
```


## [2026-09-05T20:51:25.779Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-177.json",
 "description": "Read source JSON for page 177"
}
```


### [2026-09-05T20:51:25.816Z] TOOL RESULT

```
{
  "pdf_page": 177,
  "book_page": 147,
  "entries": [
    {
      "root": {
        "name": "Gĕu 1, Gu; Keu 1, Keup, Kumb, Kub, Keub, Keuk 2",
        "lang": "Indo-European",
        "refs": "POK:394-398; POK:588-592",
        "gloss": "to bend; to bend, curved, hump",
        "note": "See and compare with root \"Kam:to bend\""
      },
      "part": 2,
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:591,592; KLN:391",
          "words": [
            {"translit": "kaofa", "gloss": "mountain", "script": null},
            {"translit": "xumba", "gloss": "bent container, pot", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "HRN:195",
          "words": [
            {"translit": "kôf", "gloss": "mountain", "script": null},
            {"translit": "xombak", "gloss": "a jar", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "BQT:768,1739; WLD1:376",
          "words": [
            {"translit": "kŭh", "gloss": "mountain", "script": "کوه"},
            {"translit": "kohân", "gloss": "camel's hump", "script": "کوهان"},
            {"translit": "xom", "gloss": "jar", "script": "خُم ۱"}
          ],
          "script_extra": "کوهه ؛ خمره",
          "note": null,
          "quote": {
            "text": "چو روی هوا گشت چون آبنوس - نهادند بر کوهۀ پیل کوس",
            "poet": "Ferdowsî"
          }
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:395,588",
          "words": [
            {"translit": "kava", "gloss": "humped", "script": null},
            {"translit": "fra-kava", "gloss": "humped front", "script": null},
            {"translit": "apa-kava", "gloss": "humped back", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "cuppa", "gloss": "curved-in pot", "script": null},
            {"translit": "cymbalon", "gloss": "curved-in plate", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "Arabic",
          "refs": "ARK:223; TAD:44",
          "words": [
            {"translit": "koab", "gloss": "cup", "script": null},
            {"translit": "akvâb", "gloss": "cups", "script": null},
            {"translit": "sanj", "gloss": "cymbal", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "Persian",
          "refs": "MON:332,1336; TAD:44",
          "words": [
            {"translit": "akvâb", "gloss": "cups, jars", "script": "اکواب"},
            {"translit": "sanj", "gloss": "cymbal", "script": "صنج"}
          ],
          "script_extra": "سنج",
          "note": "See root \"Keg\" for another possible derivation.",
          "quote": null
        },
        {
          "id": 8,
          "parent": 5,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "cup, hump, cymbal", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "haup", "gloss": "heap", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 9,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "heap, hip, high. height", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Geu 2, Geua",
        "lang": "Indo-European",
        "refs": "POK:399",
        "gloss": "to hasten"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:399; BQT:148",
          "words": [
            {"translit": "zavah, zâvar", "gloss": "power, force", "script": null},
            {"translit": "api-zâwar", "gloss": "tool", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "POK:399; BQT:148; HRN:149",
          "words": [
            {"translit": "zŭr 1", "gloss": "force, power", "script": "زور ۱"},
            {"translit": "zâvar", "gloss": "power, force", "script": "زاوَر"},
            {"translit": "zâv", "gloss": "powerful, strong", "script": "زاو"},
            {"translit": "abzâr, afzâr", "gloss": "tools", "script": "ابزار ، افزار"}
          ],
          "script_extra": null,
          "note": "For a different derivation of \"abzâr & afzâr\" see root \"Ghei 2\".",
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:399; HUB:16",
          "words": [
            {"translit": "zava", "gloss": "haste", "script": null},
            {"translit": "aiwi-zâvayeiti", "gloss": "adds up", "script": null, "see": ["Ambhi"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Persian",
          "refs": "POK:399; BQT:1043; HRN:149; HUB:16",
          "words": [
            {"translit": "zŭd", "gloss": "fast, soon", "script": "زود"},
            {"translit": "afzŭdan", "gloss": "to increase", "script": "افزودن"}
          ],
          "script_extra": "افزایش ، افزون ، فزون",
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Old Persian",
          "refs": "SOD:103",
          "words": [
            {"translit": "abi-jâvaya", "gloss": "to increase", "script": null, "see": ["Ambhi"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "Sogdian",
          "refs": "SOD:103",
          "words": [
            {"translit": "bj`w", "gloss": "to increase", "script": null}
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


## [2026-09-05T20:51:26.176Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-05T20:51:26.215Z] TOOL RESULT

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


## [2026-09-05T20:52:27.479Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','KLN','AHD','HRN','WLD','WLD1','BQT','MON','ARK','TAD','SOD','HUB','BRT','PHD','NYB','ARY','PLA','CHEUNG','IEC','SYN','SKT','LKT','AFM','FVQ','KNT']:\n    print(k, json.dumps(d.get(k),ensure_ascii=False)[:700]); print()\n\""
}
```


## [2026-09-05T20:52:27.657Z] TOOL CALL #6: Bash

```json
{
 "command": "ls data/verification/ | tail -20 && echo ---- && head -c 2500 data/verification/page-124.json"
}
```


### [2026-09-05T20:52:29.265Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index 

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt", "page_offset": "KLN_1966: TWO pri

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only", "identifie

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or grep the 

WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.39015066210397 (browser only from this host)", "identifier": "in.gov.ignca.20339 (Band 3); also in.ernet.dli.2015

WLD1 null

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.c

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol 

ARK {"title": "M.H. Rokn-zadeh Adamiyyat, Arkan-e Sokhan, Sharq 1347/1968", "kind": "catalog", "url": null, "lookup_hint": "Not found.", "local_file": null, "page_offset": null, "covers_etymology": false, "notes": "none online. || RE-SEARCH 2026-09: nothing digitised on any permitted platform (archive.org, Google Books, Persian libraries/ebook stores). Check opac.nlai.ir manually / buy second-hand."}

TAD {"title": "Tobia al-Unaysi (طوبيا العنيسي), Tafsir al-alfaz al-dakhila fi al-lugha al-'arabiyya ma'a dhikr asliha bi-hurufihi (2nd ed. Cairo 1932, ed. Yusuf Tuma al-Bustani; later Library of Lebanon reprint) — Nourai lists it under Arabic authors ('Unaysi T.'); its Table IV line was lost in the OCR", "kind": "archive_djvu", "url": "https://archive.org/details/TOB1932ARAR (1932 ed.); also https://archive.org/details/ar113lang79 and https://archive.org/details/elshandawily14640", "lookup_hint": "Alphabetical Arabic headwords; grep the Arabic headword in TAD_pages.txt (86 leaves) or TAD.txt; inside.php search works.", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/TAD_pag

SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get s

HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by parag

BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \\f between 

PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<ident

NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Nourai's 'NYB' nu

ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY:<printed page> --image", "local_file": ["/home/sfmqrb/git/rishe/

PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt"], "page_offset": "301 leaves (pdftotext -layout, \\f-separated): printed page = leaf(1-based) − 15 (leaf 291 = p.276).", "loo

CHEUNG null

IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Reconstruct

SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<i

SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<i

LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Numbered entries: 'NNNN. word (language) meaning' - Lokotsch is usually cited by entry number, but Nourai cites pages.

AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM.txt"], "page_offset": "19

FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ.txt"], "page_offset": "printed page = leaf − 17 (0-based \\f blocks in FVQ_pages.txt; 

KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt", "page_offset": "leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archiv
```


### [2026-09-05T20:52:29.316Z] TOOL RESULT

```
page-82.json
page-83.json
page-84.json
page-85.json
page-86.json
page-87.json
page-88.json
page-89.json
page-90.json
page-91.json
page-92.json
page-93.json
page-94.json
page-95.json
page-96.json
page-97.json
page-98.json
page-99.json
process
sources
----
{
  "pdf_page": 124,
  "book_page": 94,
  "verified_by": "claude-opus-5",
  "verified_on": "2026-09-05",
  "entries": [
    {
      "entry": 0,
      "root": "Dhě 2",
      "verdict": "confirmed",
      "modern_form": "PIE *dʰeh₁- 'to put, place; to do' (Pokorny 235-239 dʰē-2; Watkins/AHD dhē-¹)",
      "note": "The root box is right on all three counts. Pokorny's own lemma reads 'Root / lemma: dʰe-2, Meaning: to put, place, say' with 'Page(s): 235-239', so Nourai's 'Dhě 2 : to do, set' with POK:235 reproduces Pokorny's numbering and gloss exactly; Watkins in the AHD appendix has 'dhē-¹. To set, put. Contracted from *dheə ... [Pok. 2. dhē- 235]', and Wiktionary's reconstruction page glosses *dʰeh₁- 'to do; to put, place'. The Iranian material of the chart is likewise Pokorny's own: 'with full grade Avestan Old pers. dāta-', 'Avestan ni-δaiti- „laying down, putting away, hiding“', 'Avestan gao-δi- / gao-δana- „milk container“', 'Avestan dāman-, dąman- n. „site, creature“'. Three things in Part 1 need correcting rather than the root itself. (1) The Avestan mouth-veil is paiti.dāna-, not 'paiti-dâma' (node #3) — a misprint in the printed book, and one that Mo'in's footnote on the very page Nourai cites (Borhān p.418) refutes. (2) apa-dāna- (node #6) is Old Persian, not Avestan, and means 'palace, columned hall'; 'the concealed part of a palace' is Kent's etymological comparison with Skt. apadhā-, not the word's attested sense. (3) Pahlavi dast-war (node #13) does not belong to this root at all: Horn p.127, the page Nourai cites, and Nyberg II 61 both derive it from the root daṇs-/dąh- 'to teach', and Wiktionary offers only *dasta-bara- 'hand-bearer' or *danh- 'to teach'. A fourth, smaller point: the gloss 'to settle, to give' on node #11 mixes this root with PIE *deh₃- 'to give', a distinction Nourai's own reference FFD:52 (Abolghasemi p.52) draws explicitly. Two of the four boxes on the Persian side, the Sogdian box and both of the Persian outcomes of the law-branch check out completely, and Gharib's Sogdian entry γwδʾak even carries the Avestan etymology Nourai draws.",
      "note_fa": "خودِ ریشه کاملاً درست است: پوکورنی در صفحات ۲۳۵–۲۳۹ مادهٔ dʰē-2 را با معنای «نهادن، قرار دادن» آورده و واتکینز در پیوست فرهنگ American Heritage همین را می‌گوید؛ مواد ایرانی نمودار (dāta-، ni-δ
```


## [2026-09-05T20:52:38.079Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK grep gēu / keu ===\"\ngrep -n \"Root / lemma: g[eēě]u\" POK_full.txt | head -20\ngrep -n \"Root / lemma: keu\" POK_full.txt | head -30\necho \"=== pages 394-398 / 588-592 / 399 ===\"\ngrep -n \"Page(s): 393\\|Page(s): 394\\|Page(s): 397\\|Page(s): 398\\|Page(s): 399\\|Page(s): 588\\|Page(s): 589\\|Page(s): 590\\|Page(s): 591\\|Page(s): 592\" POK_full.txt | head -40"
}
```


### [2026-09-05T20:52:38.164Z] TOOL RESULT

```
=== POK grep gēu / keu ===
31753:Root / lemma: geu-, gau-, gu-{*sgeu-) 
35683:Root / lemma: geus- 
35743:Root / lemma: geu- geua- (besides geus^ 
46624:Root / lemma: keuad- kud- 
46660:Root / lemma: keu-1, skeu-, lengthened grade keu- 
46749:Root / lemma: keu-2, keua- 
=== pages 394-398 / 588-592 / 399 ===
31720:Page(s): 399 
32130:Page(s): 393-398 
35741:Page(s): 399-400 
35768:Page(s): 399 
47010:Page(s): 588-592 
50942:Page(s): 592-594
```


## [2026-09-05T20:52:39.255Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AHD keu ===\"\ngrep -n \"^keu\\|^keup\\|^keuk\\|^keub\\|^kumb\\|^geu\" AHD_watkins1985.txt | head -40"
}
```


### [2026-09-05T20:52:39.307Z] TOOL RESULT

```
=== AHD keu ===
499:geue-. To hasten. Possibly the base of Germanic *kaur- Jan in Old Norse keyra, to drive: SKIJORING. [Pok. geu- 399.]
501:geus-. To taste, choose. 1. Germanic *keusan in: a. Old English céosan, cedsan, to choose: CHOOSE. b. Gothic *kausjan, to choose: CHOICE. 2. Zero-grade *gus- in Germanic *kuz-, becoming *kur- in Old Norse Valkyrja, “chooser of the slain,” Valkyrie (valr, the slain; see wele-2). 3. Suffixed zero-grade form *gus-tu- in: a. Latin gustus, taste: (GUST?), GUSTO; DISGUST, RAGOUT; b. Latin gustdre, to taste: DEGUST. [Pok. geus- 399.]
622:keu-?
627:keub-. Thorn. Germanic *heup- in Old English héope, brier, seed vessel of the wild rose: HIP’. [Pok. keub- 595.] keue-!. To pay attention, perceive (preternaturally). 1. Suffixed o-grade form *kous-o- becoming *kaw- in denominative (stative) Latin cavére, to beware, watch, guard against: CAUTION, CAVEAT; PRECAUTION. 2. Suf- fixed zero-grade form *ki-dos (< *kua-dos) in Greek kudos, magical glory: kuDos. [In Pok. 1. keu- 587.] keue-2. To swell; vault, hole. I. O-grade form *kouo-. 1. Basic form *kous- becoming *kaw- in Latin cavus, hollow, and cavea, a hollow: CAGE, CAVE, CAVERN, CA- VETTO, GABION, JAIL; CONCAVE, DECOY, EXCAVATE. 2. Suffixed form *kow-ilo- in Greek koilos, hollow: (-CELE2), -CELIAC, -COEL, COELOM. 3. Suffixed lengthened-grade form *kéw-o- in Greek kdos, hollow place, cavity (> kddeia, poppy head): CODEINE. II. Zero-grade form *ki- (< *kua-). 1. Suffixed shortened form *ku-m-olo- in Latin cumulus, heap, mass: CUMU- LATE, CUMULUS; ACCUMULATE. 2. Basic form *kd- in: a. suffixed form *ki-ro-, “swollen,” strong, powerful, in Greek kurios (vocative kurie), master, lord: CHURCH, (KIRK), KYRIE; b. suffixed form *kuw-eyo- in Greek kuein, to swell, and derivative kiima (< *ki-mn), “a swelling,” wave: CYMA. [Pok. 1. feu- 592.]
628:keuk-. To be white, be bright, shine. Suffixed zero-grade form *kuk-no- in Greek kuknos, swan: CYGNET, CYGNUS. [Pok. keuk- 597.]
```


## [2026-09-05T20:52:47.083Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== geu- 393-398 lemma ===\"\nsed -n '31750,31790p' POK_full.txt\necho \"=== ...around 32120-32135 ===\"\nsed -n '32100,32135p' POK_full.txt"
}
```


## [2026-09-05T20:52:47.145Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== geu- geua- (399) ===\"\nsed -n '35735,35790p' POK_full.txt"
}
```


### [2026-09-05T20:52:47.202Z] TOOL RESULT

```
=== geu- 393-398 lemma ===



Root / lemma: geu-, gau-, gu-{*sgeu-) 

Meaning: to bend, curl; a kind of vessel 

Note: 

Root/ lemma: geu- gsu- gu-\ to bend, curl; a kind of vessel probably derived from Root/ 

lemma: (s)keu-2, (s)keua : (s)ku- : to cover, wrap 

Phonetic evidence: Middle High German /rc»/?e 'stall, pigpen, cage, cavity' : kir. kuca^ 

pigpen' (Trautmann 145) 

Material: Unextended probably in goua-: ^J-"hand', see there; further Norwegian kaa^ 

turn, twist the hay ', Old Norse ka^ disturb the peacefulness ' {*kawdn)\ ka-beinn^ 

bowlegged' {*gouo-\ Old Irish gau, ^d'lie, falsity', whether from *gdua, here, otherwise to 

connect with Latin haud); about gr. Yur|<;, yuTov see below S. 398, about yuaAov see below 

S. 397. 

a. More dental extensions : 

gud-, ^re^/f/- (occasionally gu-ed-?), before all in Germanic; gudo-m^ intestine '. 

Old Indie gudam^ intestine '; 

maked. yoSa svispa MaKzboyzq, Hes.; 

ndd. kut^ intestine ', Modern High German Bavarian kutz^ a part the bowels '; ndd. kut, 
kute a\so " Intestine of smaller animals, roe bags; calf; bag, pouch ', Middle Low German 
kut^ soft parts in the animal body, roe bag, calf, holl. kuit{*kOt-) and kiete {* keot-) " roe; 
calf, engl. Dialectal kyte, A/fe "belly, stomach ' (compare to meaning under q/Pus); 

Old Frisian kate {* kaut-) "ankle'. Middle Low German kote, /rJ/e"hoof, talon, the foot 
=== ...around 32120-32135 ===

gr. Yur|<; " the crooked piece of wood in a plow ', aporpov auToyuov " Pflug, an dem 
ilCrummholz und Scharbaum noch aus einem Stuck bestanden ' (s-suffix doubtful), 



wherefore Yur|<; " piece of wood as field measure ' {*\/u[a]diq-, but also *YuFac;- possible); 
gr. YuTov " limb, the feet, womb, hands, the hand, (so prob. as device on signet); the whole 
body '; 

maybe alb. 5//" womb' 

gr. MHTpoc; yuTa "lap", yuiow " lame ', from which yuioq " lame ' (Grdf. *yua-iov; or yuF-iov? 
ders. doubt by yuaAov, see above), yavaoq 'crooked, bent outwards, writhed humped 
(from legs)', yauaoojjai " to be bent ' (but ^avaabaq i])Z{jbf\q Hes. perhaps Gaelic, to Old 
Irish gau'We, falsity'?) can a have preserved after other Adj. in -ooqior ' stooped, writhed, 
crooked, humped ', yet au is also difficult, because an ablaut *geu- : gdu-'\n spite of the 
frequent grade *gu- stands not certainly; unclear hom. apcpiyuoq " with a limb at each end, 
double-pointed, or bending both ways, elastic', epithet of spear, and aiJcpiyunsK; ' he that 
halts in both feet, the lame one ', epithet of Hephaistos; 

maybe also alb. genje/l'\e' 

Middle Low German nnd. kuse' stump, club, mace, joint; grinder, molar tooth ', 
Norwegian dial, kus' hump, hunchback '; Swedish /ri/s5 'pudenda'; Old Norse kjossi. " 
pouch ', kjossm. 'bay, cavity', faro, kjosi. 'craw ', Swedish kjusa^ valley gulch ', kjus 
'point, edge of a poke ' , Norwegian kysa {*keusidn-) and k0ysa ( *kausidn-) ' crest, bonnet, 
cowl '. 

References: WP. I 555 ff., WH. I 112 f., 311, 629, 852, Trautmann 80, 100 f. 
Page(s): 393-398 

Root / lemma: ghsb^(o)lo-, -la 
Meaning: bifurcation 

Material: Old Irish Middle Irish gabur\oxV.Qd bough, fork; fork point the thighs, vulva', cymr.
```


### [2026-09-05T20:52:47.226Z] TOOL RESULT

```
=== geu- geua- (399) ===
princes of the Holy Roman Empire entitled to elect the emperor', Will-ZTJA "capriciousness, 
despotism, arbitrariness'), with intersection in neuter Old Norse k0r' choice ', Old English 
ge-cor' verdict ', derived Old High German koron' taste, sip; have some experience of; 
enjoy, try'. 

References: WP. I 568 f., WH. I 628 f.. Feist 312 f. 
Page(s): 399-400 

Root / lemma: geu- geua- (besides geus^ 

Meaning: to advance; to hurry 

Material: Old \v\6\cjunati^ drive, hurry, set in motion, stir into action as if by fanning; 

arouse, instigate 'Javate^ hurries ',yzy/^-/7 "hurrying', y^- "quick, ias\.\jut/^ quickness, 

encouragement ',yai///7 "hurrying', yai/a-/7 "hurrying, quick, iast' , jav/stha-h 'the fastest', m. 

"haste, hurry, quickness ',Javas-' quickness \Javana-h' driving, animating, inciting '; 

Avestan zavah-r\. " power, strength ', zavar- n. "(physical) power, strength ' (esp. of the 
feet and the horse), npers. zor' power ', Baluchi zJ/ "quick, fast', Avestan zevTstya " the 
hastiest, most fastest, the most conducive ', uzutay-' hurrying out, foaming '; 

besides auf Indo Germanic ^'et/a-weisend: Avestan yai/a" hurry '; npers. zJo' "quick, 
fast' could belong to Aryan gox z, 

perhaps to Old Norse /rey/'a "drive, ride, push, throw, ride'; 

Serbo-Croatian zuriti se " hurry ', from Trautmann 80 to guriti se " brew ' placed, perhaps 
in spite of unclear aniaut here. 

References: WP. I 555. 
Page(s): 399 



Root / lemma: gei- : gT- 

Meaning: to sprout 

Material: Armenian c//, ciui, ceV stem, stalk', s/7-c/^/ "sprout, germ, sprout'; 

Gothic keinan, ^s-/re/>75/7 "germinate', us-kijans^ germinated, sprouted '; Old High 
German c/7/77a/7 "germinate, split, open'. Old English clhan^break, crack, be open'; Old 
High German chTmoxu., asachs. /r/777c»"germ, sprout'; Old English cTd, Old Saxon kTdm. 
"germ, sprout, young shoot ', Old High German frumakTdi^ first shoot '; Old Saxon kio. Old 
English ceon, cTun^ gills ' (probably *kijan-). 

Here probably with a previous form the bursting bud, sprout in general meaning "break, 
crack, sich split' Old High German kTI, Modern High German Keil, Middle Low German kTI, 
Norwegian kTlem. "wedge' (or this meaning of the sharpness deriving form of the plant 
bud? formally from *kT-dla-, compare *kT-Ma-\n:) Old High German k/de/, Modern High 
German Dialectal ke/de/m. "wedge'; Old Icelandic A/7/m. " narrow sea bay ' ("*cleft, 
fissure'), changing through ablaut Norwegian keilai. "small gully, canal'. Middle Low 
German kelrc\. "narrow Meerbucht '; with /Old English cinui. " cleft, col, gap', Danish
```


## [2026-09-05T20:52:54.315Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '46749,46800p' POK_full.txt\necho \"=== search xumba/kaofa/kumbha in that block ===\"\nawk 'NR>=46749 && NR<=47015' POK_full.txt | grep -n -i \"kumb\\|xumb\\|kaofa\\|kaufa\\|Avestan\\|cuppa\\|cupa\\|haufe\\|heap\\|hoch\\|hump\" "
}
```


### [2026-09-05T20:52:56.103Z] TOOL RESULT

```
Root / lemma: keu-2, keua- 

Meaning: to bend 

Note: Numerous parallel formations from the root geu-see there, compare esp. the 

confrontations by Persson Beitr. 1 00 f., 1 04 Anm. 1 . - About the attempt of a mediation 

with fsjkeu-' cover' see there. 

Material: The f. root in Old Indie kora- m. " movable joint '; Avestan fra-, apa-kava- " vorn, 

^inten buckelig '; kir. ku//ty' shrink up, before coldness', poln. ku//c'pu\\ together, crook'. 

Also the prehistory from Latvian kuza "craw, goiter ' and such is not to be judged 
because of the rhyme relation to guza etc. not certain, see below ^e^- "bend' above S. 
395. 

Under an initial sound variation A/? Petersson KZ. 47, 277 here will place Old Indie 
kho/aka-' ant heap ' (also Lithuanian kulys^ bundle straw'), more confidently Armenian 
xoyi. Gen. xuli^ a scrofulous tumor, swollen gland, struma, scrofula, tuberculosis of the 
lymph glands of the neck ', russ. s^^a/a "testicles', serb. suljevi' golden vein'. 



Maybe alb. kule^ hernia' = Armenian xoyi. Gen. xuir swollen gland ', alb. kulpra, kulper 
"bendable ivy, clematis ' = {*kupra) thupra, thuper^ twig, rod' see below. 

Maybe alb. per-kul, perkur bend'. 

A. Dental extension (redupl.) ka-ku-cf- 0\d Indie kakud-' summit, acme, apex ', kakuc/-' 
oral cavity, palate', kakudmant-' provide with a summit or hump '; Latin cacumen^cusp, 
peak, acme, apex ' (the men- further formations probably after acumen), basic meaning " 
bulge '; in Germanic *hagu= Old Indie kakud- one introduces also Old Frisian /7e//a'head' 
back ( *hagila-, with suffix change for hagu-la-)\ compare also Old Indie kakubh- " acme, 
apex ' under "labial extensions'. 

B. guttural extensions. 

B. I. keu-g-: 

Old Icelandic huka " cower, cringe, crouch ' {hukta, stem participle hokinn), hoka, hokra 
" grovel, truckle, creep ', h0ykiask^s\v\k down, creep together'. Middle High German 
huchen^ cower, cringe, crouch ', Modern High German hocken; Swiss hockrw. 'heap', 
Tirol hockenm. "heap of hay', with aniaut. 5- Middle High German schochem. " stacked 
heap of hay ', (with kk.) asachs. skokm. "60 pieces'. Middle High German schoc(kes) 
"heap tussock, number of 60 pieces ', Middle English shock^ heap sheaves (12 - 16)'; 
about Schochs. lastly Sommer " Zum Zahlwort ', S. 78 ff., S.-B. Bayr. Akad. 1950, Heft 7; 

Lithuanian kauge, ablaut, kiugis^ hay heap ', Old Prussian kugis^ Knauf am 
Schwertgriff ', Lithuanian kaugure^ small precipitous hill ', Latvian kaudze^heap, barn, 
haystack' (and skaudze). 
=== search xumba/kaofa/kumbha in that block ===
11:Material: The f. root in Old Indie kora- m. " movable joint '; Avestan fra-, apa-kava- " vorn, 
20:kho/aka-' ant heap ' (also Lithuanian kulys^ bundle straw'), more confidently Armenian 
32:oral cavity, palate', kakudmant-' provide with a summit or hump '; Latin cacumen^cusp, 
44:huchen^ cower, cringe, crouch ', Modern High German hocken; Swiss hockrw. 'heap', 
45:Tirol hockenm. "heap of hay', with aniaut. 5- Middle High German schochem. " stacked 
46:heap of hay ', (with kk.) asachs. skokm. "60 pieces'. Middle High German schoc(kes) 
47:"heap tussock, number of 60 pieces ', Middle English shock^ heap sheaves (12 - 16)'; 
48:about Schochs. lastly Sommer " Zum Zahlwort ', S. 78 ff., S.-B. Bayr. Akad. 1950, Heft 7; 
50:Lithuanian kauge, ablaut, kiugis^ hay heap ', Old Prussian kugis^ Knauf am 
51:Schwertgriff ', Lithuanian kaugure^ small precipitous hill ', Latvian kaudze^heap, barn, 
63:Middle High German hocker, hogger, hoger^ hump, hunchback, hunch '; Gothic hauhs. 
65:'); Old Icelandic haugr. Middle High German houc^h\\\\ Gothic h/'uhma' heap; bulk, mass', 
66:huhjan' heap, gather, collect'. Modern High German (md.) Huge/' hill'; 
79:kucat/6s.; russ. dial. kuceriP\. f., kir. kuceryP\. m. " curls '; with a meaning "heap' russ. 
80:kuca^hea^', dial, "haystack', kuckatb " conglobate, heap', kucki^ Pleiades {pi} ', Czech 
81:^^^©"mass', poln. kuczkiP\. "small heap'. Old Bulgarian k-bk-bnjb^ shank, leg, shin bone '. 
100:Latin cubitumx^., -usm. " elbow' (out of it gr. KupiTov 6s.)\cubd, -are^W (Faliscan cupa, 
128:Old English heapm. f.. Old Saxon hop. Old High German houfheap; troop, multitude, 
129:crowd'. Middle Low German hupe. Old High German hufo. Modern High German Haufe 
145:gr. KOcpoc; " crouched, writhed, crooked, humped ', Kucpoq n. " hump, hunchback ', Kucpu) " 
178:Latin cupai. " cask, butt ', roman. also ' bath' (besides gloss, and roman. cuppa^ qob\e\! 
192:b. Meaning group ' curvature upwards, heap ': 
196:Apers. /ra^/^- "mountain', Avestan kaofa-^6s.; camel hump ', npers. /ro/7 "mountain' 
199:alb. (South Tosc) Ay/prheap' {*kup-ija)\ 
201:Middle Irish cuani. "group, bunch, heap' {*koup-na); 
203:Old High German hovar^ hump, hunchback ' (: Lithuanian kupra). Old English hoferxw. 
211:Getreidehaufen, Hauste ' (: Lithuanian kupstas); *hufsto\s ablaut equally with Old High 
219:intonation as kaupas, s. Berneker 646); Lithuanian kaupiu, /r5Jp//"haufeln', kupiu, kCipti^ 
220:lay, place on a heap, sort, order, arrange', kupra^ hunch ', kupstas ^\\\\\\ kupeta^ haycock, 
221:haystack', /r^p/>75s"gehauft', Latvian kupt^sich ballen', /r^pe/7/5"Schneehaufen', kuprs^ 
224:with lengthened grade */rc»//7/y0-.- Lithuanian kuopiu, kudptr pile up, heap up (corn, 
225:grain)', Latvian /r^Oy05"heap', kuopina^ fascicle, sheaf; 
232:Old Indie kumba-vn. "the thick end (bone)'; kumbha-m. "pot, pan, crock, pitcher', Du. " 
233:both rises on the forehead of the elephant ' = Avestan xumba-m. "pot, pan; extension ', 
234:npers. xumb, xum^pot, pan, crock, pitcher' (this with aniaut. Tenuis asp.); 
248:/ro/77/77 "trough' (m.); from urbrit. *kumbos der'we Old English cumb'yaWey', engl. coomb, 
253:Old Icelandic aptr-huppr, Norwegian Dialectal buppan6 hump^ the hip of the cattle ', 
254:Modern High German humpein. Middle Low German humpelen " limp ' and in not 
257:Norwegian humprw. "bumpiness, knag' (ndd. loanword), engl. hump^ hump, hunchback 
258:', ndd. humpei. "thick piece', bumper low hillock', Dutch homp^Vc\\ck piece of bread'; 
259:perhaps Modern High German (ndd.) Humpen {compare Kuppog).
```


## [2026-09-05T20:53:05.821Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'NR>=46749 && NR<=47015 {printf \"%d: %s\\n\", NR, $0}' POK_full.txt | sed -n '55,75p;120,140p;185,270p'"
}
```


### [2026-09-05T20:53:07.741Z] TOOL RESULT

```
46803: 
46804: Old Indie kucati, kuncate^ contracts, curves ', kuhcika^ key ', kuca- m. " female breast', 
46805: kocayati^ raises together ', koca- m. " the shrinkage ', npers. koz^ crooked, hunchbacked 
46806: 
46807: 
46808: 
46809: Old Irish ci7a/'"crooked' {*kukro-)\ (common Celtic Alb. abbreviation). 
46810: 
46811: Middle High German hocker, hogger, hoger^ hump, hunchback, hunch '; Gothic hauhs. 
46812: Old Icelandic hor, har. Old English heah. Old Saxon Old High German /7d/7"high' ("*bulged 
46813: '); Old Icelandic haugr. Middle High German houc^h\\\\ Gothic h/'uhma' heap; bulk, mass', 
46814: huhjan' heap, gather, collect'. Modern High German (md.) Huge/' hill'; 
46815: 
46816: 
46817: 
46818: Lithuanian /raJ/ras" swelling, blister, purulent ulcer ', kaukos PI. f. ' glands ', kaukas 
46819: "fairy demon, ghost, dwarfish ghost'. Old Prussian cancY 'devil', Lithuanian kaukara^\\\\\ , 
46820: kukulys^ dumpling, small mass of dough which is boiled or steamed ', kukis^ Misthaken ', 
46821: Latvian kukurs, kukums^ hunch, swelling, blister', kuki's^ dwarf; wren, songbird ', kuksa' 
46822: sine vom Alter Gebeugte ', russ. -Church Slavic kukonost ' crooked-nosed '; 
46823: 
46868: b. Mit nicht aufs Biegen des Korpers gewendeten Bedeutungen : 
46869: 
46870: Old Indie kubra-v\. "cavity in the earth, pit, pothole; Ohrring'; gr. Kupoc; ... flacpioi 5£ to 
46871: TpupAiov Hes.; 
46872: 
46873: [but Old English hdpig^\v\ hills and hollows', hopm. " ring, hoop ', engl. hoop, Dutch 
46874: hoep^uuQ, hoop'. Old Icelandic hopu. "bay' to Lithuanian /r5M"hook'?]; 
46875: 
46876: Old English heapm. f.. Old Saxon hop. Old High German houfheap; troop, multitude, 
46877: crowd'. Middle Low German hupe. Old High German hufo. Modern High German Haufe 
46878: (also). Middle High German huste{see above under keu-p-). 
46879: 
46880: C. II. Aef/-bh- (including from words, can contain the b^ or b). 
46881: 
46882: Old Indie kubhanyu- perhaps " rotary, gyratory, dancing '; 
46883: 
46884: redupl. Old Indie kakubh-t " fingertip; rounded projection; small hillock, acme, apex ', 
46885: kakubha- " protruding, towering ' (previously reshaped after kakud-l); 
46886: 
46887: Maybe alb. kagube^ shrub, bush ' [hill = forest, bush very often in Indo Germanic]. 
46888: 
46933: root form in -b^- or -b^ probably also Old English gehopp ' a small bag, little sack ', hoppe 
46934: f. " a round swelling; in water, a bubble, capsule ', Middle English hoppe^ boll, seedpod of 
46935: flax '; 
46936: 
46937: at most Slavic *kbp-b, Czech kep 'vulva', poln. kiep "ds.; fool, good for nothing, useless 
46938: person' (Berneker 664 f. between). 
46939: 
46940: b. Meaning group ' curvature upwards, heap ': 
46941: 
46942: 
46943: 
46944: Apers. /ra^/^- "mountain', Avestan kaofa-^6s.; camel hump ', npers. /ro/7 "mountain' 
46945: (place -ph- ahead); 
46946: 
46947: alb. (South Tosc) Ay/prheap' {*kup-ija)\ 
46948: 
46949: Middle Irish cuani. "group, bunch, heap' {*koup-na); 
46950: 
46951: Old High German hovar^ hump, hunchback ' (: Lithuanian kupra). Old English hoferxw. 
46952: ds.. Old High German hubiThWX, Old Saxon huvil6s. (therefrom Modern High German 
46953: hobelnas "smooth wood using a plane, make smooth, remove rough areas '); perhaps Old 
46954: High German hufila, h/uf/7a^ cheek', Modern High German Swiss hufelin^ part of the cheek 
46955: lying down under the eyes '; Norwegian hovu. " tableland, hill, plateau, small hill'. Old 
46956: Icelandic hofu. "temple'. Old English hofu. "paddock, house, temple'. Old Saxon hof. Old 
46957: High German hofxr\. " surrounded space at the house, court, property ' (originally from the 
46958: position on hills); Middle High German huste^ auf dem Felde zusammengestellter 
46959: Getreidehaufen, Hauste ' (: Lithuanian kupstas); *hufsto\s ablaut equally with Old High 
46960: German hOfoav\6 appears like this probably rather to belong to keu-b-io (see there); is 
46961: also connected with russ. kustit "shrub, bush, bunch', kir. /r^s/ "shrub, bush, bunch'; 
46962: 
46963: Maybe alb. {* kupra) thupra, thuper^ twig, rod' (the meaning " bush' derived from " hill, hill 
46964: forest' (common alb. k- > th-) = Lithuanian kupra^ hunch '. 
46965: 
46966: Lithuanian kaupas^hea'gi' = Old Bulgarian kupb ds. (serb. /r^ijc certainly with other 
46967: intonation as kaupas, s. Berneker 646); Lithuanian kaupiu, /r5Jp//"haufeln', kupiu, kCipti^ 
46968: lay, place on a heap, sort, order, arrange', kupra^ hunch ', kupstas ^\\\\\\ kupeta^ haycock, 
46969: haystack', /r^p/>75s"gehauft', Latvian kupt^sich ballen', /r^pe/7/5"Schneehaufen', kuprs^ 
46970: hunch '; 
46971: 
46972: with lengthened grade */rc»//7/y0-.- Lithuanian kuopiu, kudptr pile up, heap up (corn, 
46973: grain)', Latvian /r^Oy05"heap', kuopina^ fascicle, sheaf; 
46974: 
46975: russ. (Berneker 646) kuprt, kuper^ coccyx, small triangular bone at the base of the 
46976: spinal column, rump ', poln. kuper^um^, buttocks '. 
46977: 
46978: D. Nasalized kum-b"^-, mostly kum-b- . 
46979: 
46980: Old Indie kumba-vn. "the thick end (bone)'; kumbha-m. "pot, pan, crock, pitcher', Du. " 
46981: both rises on the forehead of the elephant ' = Avestan xumba-m. "pot, pan; extension ', 
46982: npers. xumb, xum^pot, pan, crock, pitcher' (this with aniaut. Tenuis asp.); 
46983: 
46984: 
46985: 
46986: gr. Kuppn "bowl, bowl, barge', KU|jpO(;, Kuppiov "vessel", mostly PI. "cymbalum, bowl' 
46987: (after Banateanu REtlE. 1, 120 from Semitic qubbah. Van Windekens Lexique 48 
46988: compares Tocharian A /r^/77pac"drum'); 
46989: 
46990: KupPn "head' EM., Suid., hom. KU|jpaxo(; "crown of a helmet ' (compare KU|jpr|). S- 
46991: Leumann Hom. Worter231 ff.; 
46992: 
46993: Latin (with present nasalization) -cumbo {see above S. 590); 
46994: 
46995: Middle Irish co/77/77 "vessel'; c^/77/77a/ "goblet, bowl', cymr. cwmm 'vaWey' (m.), bret. 
46996: /ro/77/77 "trough' (m.); from urbrit. *kumbos der'we Old English cumb'yaWey', engl. coomb, 
46997: combe ^bas\n, hollow, coomb, narrow valley ', whereas is gall. -rom.c^/77i6'a "valley, trough' 
46998: Fem.; from French derives bret. /ro/r?/? "valley'; compare the unnasalized vascular names 
46999: pam. kubun, poln. kubek, also gr. KupO(; " cup. bowl '; 
47000: 
47001: Old Icelandic aptr-huppr, Norwegian Dialectal buppan6 hump^ the hip of the cattle ', 
47002: Modern High German humpein. Middle Low German humpelen " limp ' and in not 
47003: especially on the bending of the body ability meaning: 
47004: 
47005: Norwegian humprw. "bumpiness, knag' (ndd. loanword), engl. hump^ hump, hunchback 
47006: ', ndd. humpei. "thick piece', bumper low hillock', Dutch homp^Vc\\ck piece of bread'; 
47007: perhaps Modern High German (ndd.) Humpen {compare Kuppog). 
47008: 
47009: References: WP. I 370 ff., WH. I 127, 297 f., 298, 305, 306, 310 f., 859, Trautmann 121 f. 
47010: Page(s): 588-592 
47011: 
47012: Root / lemma: {keuap-.) kuep- kuap- kup-nexi to which occasional keu(e)p-, k(e)uep- 
47013: 
47014: Meaning: to smoke; to boil; to cook 
47015:
```


## [2026-09-05T20:53:17.137Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'NR>=46900 && NR<=46932 {printf \"%d: %s\\n\", NR, $0}' POK_full.txt\necho \"=== hip ===\"\nawk 'NR>=46749 && NR<=47010 {printf \"%d: %s\\n\", NR, $0}' POK_full.txt | grep -i \"hype\\|hip'\\|huf.*hip\\|Hufte\\|Huft\""
}
```


### [2026-09-05T20:53:18.878Z] TOOL RESULT

```
46900: 
46901: 
46902: stooping with tlie liead, Kubebos, minister of Cybele, one ecstatic or frantic ' EM., KupnPav 
46903: " to be frantic ' EM., " be seized by rage ' Hes. Poll., as well as Kupiarau) " tumble head 
46904: foremost '; 
46905: 
46906: to the labial extensions in the meaning from Kunrn TpcbyAn probably KunJsAri ' any 
46907: hollow vessel: chest, box (whence Cypselus was called), hollow of the ear, ear-wax ', 
46908: KuipsAoq ' of swallows' or sand-martins' nests, wax in the ears '; 
46909: 
46910: Old High German huba. Old Saxon huva. Old English hufe. Old Icelandic /7J/^ 'bonnet, 
46911: cap'; 
46912: 
46913: russ. kubarb "a humming spinning top, a spinning top that makes a humming noise ', 
46914: kubarem-b "headfirst, hastily', kubect "a humming spinning top, a spinning top that makes 
46915: a humming noise ', kubelb Dialectal ' wooden ball to the play ', kubokb "goblet, cup ', kir. 
46916: kub ' aus Holz ausgehohltes Geschirr ', kubok ' Napf, hauchiges Gefafl, kleines Geschirr ', 
46917: poln. kubek^ qob\e\, Schoppen, Obertasse '. 
46918: 
46919: cm. keu-p-: 
46920: 
46921: a. Old Indie kupa-\x\. "pit, pothole, cave'; 
46922: 
46923: gr. Kuirri TpwyAn Hes. (0?), kuttqi zxboc, ti yzbic,, Kai ai £^ uAr|c; Koi xopiou oiKnoEK;; 
46924: KunsAAov 'goblet', Kunpo(; m. ' grain measure '; 
46925: 
46926: Latin cupai. " cask, butt ', roman. also ' bath' (besides gloss, and roman. cuppa^ qob\e\! 
46927: seems late short form with consonant doubling besides KunsAAov to sein); about 
46928: respective forms from Latin and Rom. directed Berneker 645 f.; 
46929: 
46930: Maybe alb. qyp^ jug' a Latin loanword. 
46931: 
46932: Old Icelandic hufrm. ' hull, hulk, body of a ship ', Old English /Tj/Z^'beehive'; here (or to 
=== hip ===
46858: Gothic hupsxw. (stem hupi-), Old English hypem., Old High German hufi. "hip, haunch'; 
46932: Old Icelandic hufrm. ' hull, hulk, body of a ship ', Old English /Tj/Z^'beehive'; here (or to
```


## [2026-09-05T20:53:38.548Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT kaofa ===\"; grep -n \"kaofa\" BRT.txt | head\necho \"=== BRT xumba ===\"; grep -n \"xumba\" BRT.txt | head\necho \"=== BRT kava/fra-kava ===\"; grep -n \"kava-\\|frakava\\|fra-kava\\|apakava\\|apa-kava\" BRT.txt | head -20\necho \"=== BRT zavah / zavar ===\"; grep -n \"zavah\\|zavar\\|zāvar\" BRT.txt | head -20\necho \"=== BRT zava / aiwi-zav ===\"; grep -n \"aiwi.zav\\|zava-\\|zav-\" BRT.txt | head -20"
}
```


### [2026-09-05T20:53:38.648Z] TOOL RESULT

```
=== BRT kaofa ===
8940:•  j.  kaofa-,  p.  kaufa-  m.  r)  'Bergrücken, Höhenzug':  II  arkadris  näma"  °/a''  Bh.  /. » I ;  J-  7 ;  —  cd^wärü  vi'üwana  (sd.)  'fö YL  ig.z'i  —  vtgiihö  (sd.)  . .  'famm  Yt.  i4- 21.       2)'Höcker' desKamels  (nur Komp.).
9089:•  j.    'ustavaiti-    f.   EN,   einer   gläubigen  i  °r>h^hi>  . .  saini.kaofa  as.mananha  Yt.  iy. Frau:  'vaitya  aiaoiryJ  Yt.  y.  13g.  ,  13;  —  dasS  asps  . .  'nm^ä  \.44. 18;  —
23912:Pü.:  ramak  fräj^hotär.  "ä^  (AP.)   morfzat  kaofanqm   Yt/rf.  JI.
25797:•  j.  saeni.kaofa-  Adj.  '(mit  spitzem,  d.  i.) gerade  aufgerichtetem,  steifem  Höcker' '\ vom  Kamel:  uäräaha  .  .  'Ja  YLr7. 13; —  u/tranqm  .  .  'fanqm  V.  22. 3.
26794:•  j.  stvLkaofa-  Adj.  mit  starkem,  feistem Höcker''',  vom  Kamel;  ustrS  . .  V?  Yt
29609:Bed.  nach  Pü.  —  Ich  verbinde  das  Wort  mit pairiila-akara-  und  weiter  mit  ai.  jar/if-n.  — i'ü.;  i/iirw;  s.  zu  liaierämacu-.  —  >)  Statt anumayaitifm  hanlanum  v' ;  Abkürzung  mit der  Komp-  statt  Kasusform  im  mittleren  von drei  zusammengehörigen  Nomina  mit  gleichem Ka-susausgang;  S.  nocli  ahoUai'inakt  urvnti Jiaspaianahi  Yt,  14.  II,  varäzahe  pailijrtnö liii.dqslra&t  YL  14.  IJ  ,  giBqttqm  piiuru.sat>'iS virB,T/if%amnqta  Vr.7'.  5,  aspanqm  avnialö  d^riü.- /akanqm  und  itiiranqm  iirvald  sdeHi.kaofanqm  V. S2.  3  (aber  V.  32.  4  steht :  gavqni  axiaenanqm apirilBjanunqm,  weil  die  Ausginge  nicht  gleich sind);  s,  femer  un/A%ä-  No.
=== BRT xumba ===
10515:xumba-
10535:Die  Bedeutung  ist  vermutlich  eine  übertragenfi wie  bei  xumba-  (sd.).  —  np.  xafj  'incubus, Alp',  s.  Hbm.  PSt.  s6-  Wie  ist  aber  die  iran. Grundform  anzusetzen  und  wie  das  z  (gegen %  38.  \  b)  zu  erklären?  —  Pü. !  ki  Jh(i<i xamizah  (Transskr.)  »  kt  devän  xumbak,  erl.; däfän  kär  i  narih  u  mälailh  ke  hinend.
10557:•  j,  xumba-  m.  'Topf,  topfähnliche  Vor- richtung'; 'bat  haM  zimaini.pacikat  (sd.) V.  .M84;  —  '■bat  hactt  yämD-pacikat  (sd.) V.  cS*.  85.  a)  als  Bezeichnung  dessen, der  Päderastie  mit  sich  treiben  lasst, pathicus':  kö  daü'anam  xawzS  (sd.)  .  . 'bJ  V.tV.3i;  32.
10565:Ableit.  aas  xumba-\  t^.  lur  trad.  Ueutung des  Namens  DsT.  ZA.  2.  ii\;  s.  aber  No.  i.
21623:•  j.  yämö.paiika-  Adj.,  mit  xumba-  'Vor- richtung zum  Glasbiennen,  Glasbrennofen': xumbal  kala  'kat  V.S.8$.
21624:np.  Jäm  'Glas,  Becher'.  Wgh  yama-.  —  Pü. : xumbai  ape  yämii  palin,  erl. ;  däsht  (?)  karän  \ vgl.  Darabs  Bemerkung  dazu.
28114:•  j.  z3maitii.pa£ilEa-  Adj.,  mit  xumia- 'Vorrichtung  zum  Tonbrennen,  Töpferofen': xumbal  kaca  'kät  V.  8.  84.
=== BRT kava/fra-kava ===
3496:•  j.  apa-kava- 1 )  Adj,  'der  hinten,  auf  dem Rücken  einen  Höcker  hat':  mit  ml  aeta- yiisäl  zao^rayä  /mnharintu  frakavö  nttl 'vB  Yt  5.  93.  2)  m.  Name  fUr  solches Gebrechen:  mä  (a%ra)  'vö  2.  29.
4015:•  j.  afrakavastama-  Adj.  (fem.  'mi-) 'der  am  wenigsten  von  der  Stelle  zubringen ist,  der  unerschütterlichste':  fratujsayS  . . "mit  apa^srayamnanqm  "die  Fr.  . ,  die  un- erschütterlichsten unter  den  sich  anstem- menden" Yt  y.  26.
9730:—  "Alf  vJsph  ä  xsa>rsi  *yä  ..  ^raasiä'  vTmij(sd.)  katarascit  *parayat  N.  5;5";  — (sd.)  Y.^4.^.  A)  Plur,  und  Sing,  mit  al^S  ''ianam'''' *iris'ifiü»am  ra^s'^{sd.)  N, 2 ; vispa-  Adj.  von  der  Gesammtheit  derl  —  agta paräyaiti (sd.) yaia '^afys^'^A^iii stoflflichen  Lebewesen  'Welt,  Menschheit"  N. 2;  —  myazdava..amyasdavan9tn..yiU)m (vgl.  anhav-  Sp.  io7f,);  y<^a  °^3kva  {%d.)  "'kanqm  frap>r>naoiti  A.j.  11"*;  V. i'fljö^.Äjiiir?/ra(^a>-äne"dassichunabhängig|  19,29,  F,4f-; — /radahüi  'Ibanam  kava- unter  den  Wesen  einhergehe"  Y.9.  17;  —  M^häi  asavastanam  Y.  6S.  4(?);  —  yai aAümca  (sd.)  ratümca  '^anam  Vi.  I0.i}3,'.^avani  aiwi.vanyä  taiiryavantim  ..  ahmt 13. g2;  91;  —  ratu>wim  °%anqm  Yt  /o. ,  (sd-,  Sp,  4)  '"ke  (LS.)"'  ptlanahu  Yt  5. 92;  —  aat  .  .  mraom  .  .  az^m  yö  akurs\  109;  73, 113;  —  ka%S  ayärS  .  .  fprasayäi masda  .  .  yima  .  .  mS  Oi  fniciaya  .  .  mi'  (sd.)  lÄril  ai^T  '^wäAa  '^ahß  tariusiÖl  Y. °'ia  varihaya  ..  mg  vXsäi 'i:anqm  %rätSca'.43-T',  — yS  nS  ainrianqm  (sd.)  irJri- Aarpläca  .  .  V.  2.  4;  5^;  —  aiim  daA3A?m ;  xsäite  °%anam  (als  Obj.)''  .  .  tanunqm  Y. .  .  a^im  *'hsvays  (DP.)  '*  drvant3m  Y.  (J.  ö'j.  7 ;  —  ahmäi  ntmauhs  ävaidayamaidt 8;  —  cim  .  .  qsitm  tsattt  .  .  "'"itä/tz-ö'^  I  '^Sscä  tamiaslä  Y.  jÄ  2;  —  vJspa  °'i:Ssca mahrkaum  Aog.  48;  —  us  *täcil  v.'krka  tanvasca  asdibista  uStänqsca  kihrpasca  . ,
17540:•  j.  fra-kava-  1)  Adj.  'der  vom,  auf  der '  Brust  einen  Höcker  hat':  mä  mi  aOe^äsHi
21236:—  aAyH  *griAmB  ä.ASihBi  (sd.)  ta  kava- yasclt  xratul . .  dadat . .  Ay  ('weil')  vTsjutä
27308:mit  apa  'sich  anlehnen  an  — ,  hin- wenden zu  -'  (Abl.)*>:  *taolars  {sA.)  äättyS gätu!  .  ,  ma%p/näi  arä^raol  apa.sritö N.  -jS.  a)  absol.  'sich  anstemmen': frava^ayU  .  .  afrakavasUma  (sd.)  apa.- srayamnanqm  Yt.  y.  26.
=== BRT zavah / zavar ===
11905:•  j.  tatäp-  Adj.  'fallende  Wasser  habend', sva.  'der  den  Regen  fallen  lässt':  sata- %ais5  .  .  'äpa  (NS.)">  zavarm.srats  'äfS (NS.)''  ux^at.urvarS  Yt.  7^,44;  43"';  — tnihrsm  .  .  frat.ap)m  zavanlS.srBt>m  •ap?m uxryat.urvar»n  Yt  10. 6 1  "*,
27775:•  g.  zavah-  n.  'Kraft,  Stärke':  äaiva  . . spSniStä  mainya  maida  vanhuyü  'vS  iida (Sp.  3210.)  Y..??.ia.
=== BRT zava / aiwi-zav ===
5388:auniäa.bäzav-
5397:•  j.  auru5a.bäzav-    Adj.    (auch   : 'weissarmiß':  kaininö  kihrpa  . .  "Zfh  \^o.,  .  ^  ,,     ,
6493:die  Peitsche  knaÜt'  Yt,  /o.  1 1 3 ;  —  j«/ . . , ,  j.  as.bazav-  Adj.  'mit  tUchtigen,  starken 'rä  kakvqn  (sd)  Vtio.113;    —   Ja/  -4?  Vorderbeinen,  -schenkein':    uströ .  .   'zSus iyimai)  zaya  frabanm^  aum  y5  ahurö  .  .    (fjs.)  aii.kaüß  Vt  14- 12. suwram   (sd.)  .  .    'ramca  '>   zaramo.paisim  I      Kpü.;  läMib  biryär  zur  az-ar  bäsuvän. V.2.6;-»^Ä0,™)  .,y«/(sdL)  -ra,^  .    -    ^.t,„,.   ^dj.    (auch    fem.)    'rid, V.2  10.  .)    inb»    dit    pntsteihcht   ,^iai\A   bringsnd':  /r.valml .  .    ,4    ■Is
7662:■»«zav-
7692:•  g.  '«razav-  (,  p.  aräav-)  Adj.  'gerade, richtig,    recht',    vom   Weg;   yJ   «./    °züi
7697:"arazav-
7701:•  j,  'arazav-  m,  EN.  eines  Gläubigen' Bruders  des  Sra/öjpada  (sd.):    'ma  (GD.) srBtöjfädä  ahonä  Yty,  115.
7705:•  j.  ^razav-  m.  'Finger":  °zu  F.jg;  — ci'al  gaonahe  (sd.)  . .  ya  dvaHbya  "zubya *hiing3riwn,lt  N.  Ö5;  —  avaval  tafta  ydha kasistahe  (,  mawmaAe,  masistahe)  °svB sisV.6.10,  12,  14, /Ä44  PüZ.  a)  die Breite  der  Finger  als  Maasseinheit:  dva 'ZU  nismaAe  (sd.)  V.(j.6;  —  avavat  aipi yd^a  caiwärS  °zavö\.g.2();  —  cd^wSrö 'zvö  V.  6.  43,  f).  6.  [V.  iS.  2  PüZ. :  lies bai.intu\
8118:•  j.  Ujra.bäzav-  Adj.  'starkarmig':  {iiit^r?) ':,iu/ (NS.)  Yt.  70.  75.  [Vt  70.42:  lies ujra  dinara.]
8596:•  j.  uzava-  m.  EN.  eines  Gläubigen:  'vaAe
8660:•  j.  uzbäta-  Adj.  (fem.  'ta-),  PPf  P. :  s,  zav-. w+^-.  S  ja*  n.  36.
8661:•  j.  uz-bäzav-  Adj.  (auch  masfc.)  'die Ajme  emporhebend';  °zäus  (NS.)  fiaiii attunxllm  (sd.) /ravazai/e  mi^rS  Yt,/o.ia4.
11601:•  y  Jazav-  m,  (auch  mit  'spart-  m.)  Name einer  Art  des  Hundegeschlechts:  hau  °z3us (GS.)  hau  visäui  . .  hau  vTspanam  . .  spa- ct^ranam  V. /J.  16;  —  spä  *ius  V.^.^j.
12894:')  Ein  Schönheitsieichen;  vgl.  Artaxerxts  L Beiwort  Longimaiios,     S.  in  dar>-fö,bäzav-.
12906:darttgö.bazav-
12909:•  g.  darsgö.bäzav-,  j.  dar^ö.bäzav- Adj.  (auch  fem.)  langannig':  hukmlB  ahi
17125:•  j,  bäzav-  m.  i)  'Ann'  der  Menschen  und       '  5'  '*     ..  ..r,    _  .   i-n^    ,  *j:  -.^  « i-M^         i-,   -r  ,/TL'      .    Tc-v.i   j   <■      ■         Komp.  mit  ND.  im  l,  Glied;  s.  ituan-  A. Gotter:  ÄJtJv« '«i'jfLb.  als  IS.)'' j(jn«aiv)        .     /_      ■      v  ^      .  j-     (^    .     -       j ./aÄ«.-«.ä*te.«,*5,"milde,»li,JimAnn  •   !■   bs^-s-aolah-   Ad,.    Oak    m    den «.d  dem  «cht«,  mit  de«,  rechten  Ar»  m,d  '^f  "»  *^'  "^'  '""• '  -»ß-»«. . . deoh»kei."V.j.>5i-j...,yü!j»,,;7™i,  V»«"!'"  '?*''/'/?;  \t.,o.,y,-«-a^,aAr
20163:•  j.  mazav-  Adj.  'acht  habend  auf  — ',  mit Gea:  a^a  spamm  nida%}m  yat  dim  'zacs (NS.)  k)hrps  türahe  "den  Hund  habe  ich dazu  bestimmt,  dass  er  acht  habe  auf  die Person  des   Tärere"  V.  13.  39.
20395:•  j.  'msrszav-  n.  'Wirbel'  des  Halses  und Rückens:  yavata  . .  tii/ainti  °tu/a  ttünB gayehe  'sula  x&  uimnahe  "bis  er  entzwei
20399:j.  'iD'Srazav-  in.,  Du.  Bezeichnung iner  a frischen  Schöpfung,  vll.  eines Sternbilds:  nizbayemi  'zu  ^pourvs  *:^a%/ltd yüßis/ff  mairtivä  *d3mqn  'ich  rufe  an  die beiden  M.  im  Süden,  die  ewigen,  die  am besten  kämpfen  von  der  Schöpfung  der beiden  Geister"  V.  ig.  42.
```


## [2026-09-05T20:53:39.292Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD ===\"; grep -n -i \"kōf\\|kof \\|xumb\\|hwmb\\|abzār\\|zōr\\|zūd\\|abzūdan\\|abzūd\" PHD.txt PHD_mackenzie.txt | head -40"
}
```


### [2026-09-05T20:53:39.350Z] TOOL RESULT

```
=== PHD ===
PHD.txt:151:wizūdan ... = wizayidan. xig |ZKYA < A zq? | N xī(k)] leather bag.
PHD.txt:191:amāwandīh: power, strength. ambag [’mbk' | N anbajat] a preserve, conserve. ambar [mbl, ?nbl | Аг. ‘праг ambergris. ambarag [?mblk! | N anbara] hairless (animal). Р amburdan [h/^mbwultn! | Р ?mPr-] = hambārīdan. a-menīdār [^mynyt!l] unthinking. āmēxtan, āmēz- Pmyhtn', ?тус- | M *myxtn, ?myz-, N ~] mix. ~išn: mixture; element. āmiz [^myc] side dish, vegetables. āmēxtan, āmēz-, read hammóxtan, hammoóz-. Amurdād [?m(w)rdt' | N murdád] Immortality, the sixth Amahraspand, guardian of plants and food; cal. sth month; 7th day. āmurzīdan, āmurz- [mewlc-ytn! | M?mwrz-yd, N ~) forgive, pity, have mercy on. ~išn: mercy, forgiveness. Р amwaštan [h|mwstn! | P ?mwst] gather, collect. an- Pn- | M ’n-] prevocalic privative prefix, un-, -less. ап [ZK < A zk;?n! | M Ап, N ~] that, he. ~ 1: that of; with a qualifier preceding a noun, equivalent to a following 1 e.g. ап i ahlawàn ruwān = ruwan i ahlawān, the souls of the righteous. -ап [2s! | M An N ~] suffix forming (i) present participles, (ii) adverbs, (iii) plurals. ānāb-, —išn, v. ānāftan. an-ābādān Ppp’ rn'] uncultivated. an-abaxšāwand [m ph} wnd] unrepentant. ~ih: unrepentance. an-abāy Pr’ Pd) unfitting, improper. an-abēdān [”7?5yt?x'] useless, unwanted. ~th: uselessness. anübublag [9 fwhlk' = Av. anüpers0a-] inexpiable, unatonable; the highest degree of sin. an-abzār Pwi] unskilled, incapable. ~th: inability. an-ādān [*77:?x!] insolvent. ^h : insolvency. an-ádüg [tk] incapable. an-afsēnišn [”77?syx$n!] indestructible. ānāftan, ānāb- [77ftn',*775- | M ?w pt, Qn m-)] avert, reject, frustrate. ~išn: avoidance, warding off. anág [77 k! | M >ре} evil. ~th: evil, harm. an-ügàh и: | N ndgah] unaware, unwitting. anüg-kardàr [RU АРД, -kunisn [-kwnšn'] evil-doer, maleficent. anagr Pngl) infinite. ~an [”x! | M?nyr^n] Infinite Light; cal. 30th day.
PHD.txt:390:hambār [kmb’l | N anbdr] store. hambārīdan, hambār- [hm-, hnb'l-ytn! | M hmb'r-, N anbürdan] fill, collect. hambasān [Anbs?n! | M *mbs*n] enemy, opponent. ~ig [-yk'] inimical, opposing. hambast [Ambst' | N anbast] compact. !hambastag [Ambstk' | N anbasta] formed, composed. shambastag [hnbstk' | М hmbst] collapsed, fallen. hambāstag [hmb’stk'] *all. īhambastan, hamband- [hmbsin', hmbnd-] form, compose; bind to- gether, intertwine, encircle. ~i8nih : binding together, intertwining. žhambastan, hambah- [%xbstn!, hnb?h- | M hmbst, hmbh-] collapse, fall down. VW "E. hambāstan, hambāh- [hnb’stn', hnb’d- | M hmb’stn, hmb’h-] cast down, demolish. ~išn: felling, demolition. ham-bašn [hmbén'] of the same stature. hambaw-, —išn, v. hambüdan. hambāy [hmb?g | (M hmb’w)] companion, partner; adversary. hambāz [hm-, hnb’c | M ?mP?z, N anbáz] partner. hambedig [%mbytyk!] = hambadig. hambēš-, —išn [hnbwi-, -£n! | N anbūšif] = hambüs-, ~išn, hambdy- (hnbwd- | M hwmbwy-, N anbóy-idan] smell (tr.). —ügih [-*kyh], —iŠn: (sense of) smell. hambüdan, hambaw- [hm-YHWWN-tn', v. büdan; hmbwtn'] be united, composed. „«išn(īh): union, composition. hambun [hmbwn'] (with a negative) not at all, not in the least. hambüsidan, hambūs- [hnbws-ytn' | N anbüsidan] come into being, be conceived. ~išn: conception. ham-dádestàn (hm-D YN A, -d'tsn! | N ham-dástán] agreeable, of the same opinion. hamdam [hmdm | N ~] intimate. ham-désag [hmdysk'] of the same form, homomorphous. hamë [hm’y | M Атуш, N ~] always. ^ ka: whenever. ham-ēdēn [m)ytwn! | N hamédün] likewise, similarly. bamé|ig (/um)yyk! | M тушур] eternal. ~iha [-yh’] eternally. hamémiil [mym] | = J] opponent, adversary. --īh: opposition. haménidan, hamén- [hmyn-ytn'] unite, compose. hamē-rawišnīh, hamē-ud-hamē-rawišnīh [(Amy W) hwy lwbsnyh) eternity.
PHD.txt:428:kem [kym] less, fewer; v. kam. кёп [kyn' | = M, N kīn(a)] hate, malice, revenge. ~ig [-yR'] malicious, vengeful. kennār [Rl] lyre, harp. ~-sray [-sPd] harpist. kénwar [kynwl | (M kynw’r), N kinawar] vengeful, vindictive. ««īh: vindictiveness. kër [kyl | N ~] penis. kēsar [kysl] Caesar. këš [kyš | = M, N ~] dogma, faith (especially non-Mazdean). ~-dar [-d’/] sectary, non-Mazdean. keSidan, keš- [k(y)$-ytn! | (M kr$-), N kafidan] pull, draw. Kēwān [kyw’n! | Ar. kaywān] astr. Saturn. kēwūd [kypwt! | M R'ywd] box, ark. kilēl [R]yl | N ktlīd)] key. kirb [klp | M kyrb] body, form. kirbag [krpk' | M kyrbg, N Аја] virtue, good deed. ~ig [-y%!] virtuous, pious. kirbakkar [krpkkl | M kyrbkr] beneficent. ~ih: beneficence. kirih- [OBYDWNyh-, v. kardan, kiyh- | M kyryh-] be done, made. kirm [kim | M krm, N —] worm, serpent. kirrénidan, kirrén- [klyn-ytn'] rend; create (daevic). kirróg [k(y)lwk! | M grwg] artisan, craftsman; skilled. ~th: arts, crafts, craftsmanship, skill. kiš [k(y)š | M АЎ, N ~] furrow, line. kišnīz [kšnyc] = gi$niz. kištan, kar- [ZL Y TWN-tn! < А У ar; kyštn!, Pl- | M kyšt, kis- N ~] till, furrow; sow. kištār [ZLY TW NTt'l] tillage. kišw, ~4n [kysw', x! | P Аун] tillage. ~(an)zar [-c?/ | (N kištzār)] field. ki$war [Rystol | M kyswr, N ~] region, clime, continent. kišwzār, v. kišwānzār. kūb-, v. koftan. kódak [kxwtk! | M gwdk, N ~] young, small; baby. kof [kwp | = M, N koh] hill, mountain; hump. ~ag [-4! | N Абла] saddle. ~ig [-yk! | N kēkī] wild, mountain-. koftan, kūb- [kwp-tn' | N ~] beat, pound, crush. kör [kwl | M kar, N ~] blind. ~-dil [-dyl | M -dyl, N ~] blind-hearted, incorrigible. kūstan [kwstn' | = M, N ~] beat, pound. kūš-, v. kóx&-. kēšk [how fA! | N ~] pavilion, palace, kiosk.
PHD.txt:514:nihuftan, nihumb- [zhwptn', nhwmb- | = M, N <) cover, hide, conceal, clothe, nihumbidan [nhwmbytn'] = nihuftan. *nikóhidan, nikóh- [nkwh-ytn' | N ~] blame, execrate. ~išn: blame. ~išnīg : blameworthy, execrable. nil [nyl | N ~] indigo. nilópal [nylw(k)pl | N ~, nilēfar] lotus, water-lily. nimüdan, nimāy- [nmwtn', nmd- | M nmwdn, nm’y-, N ~] show, guide. nirfs- [nlps-] wane, decrease. ~išn: decrease, diminution. nirmad [nylmt'] profit, interest. ~ӧтапа [-’wmnd] profitable. P nisag [nys’k' | P nys’g] bright, splendid. niš- [nyi- | M nyyš-ydn, J ~] see, observe. nišān-, v. nišāstan. nīšān [ny$*x! | = M, N nisàn] sign, mark, banner. nišast [nsst! | N ~] association. nišastan, nišīn- [Y TY BWN-stn! < A V у; пт! | M nist, (nfyy-), N ~] sit. nišāstan, nišān- [Y TY BWN.stn!, 2n-; nP?stn!, nP?n- | M nf?st, (nP5y-), N ~] set, seat, plant, found. nišāyišn [n£ din! | M n$?y-, v. niSástan] foundation. nišēb [niyp | N ~] declivity; astr. dejection. ~ig [-yk'] declining. nišēm (nidm | M nšym, N ~an] seat, perch. ~ag [-k'] residence, abode. niSin-, v. niSastan. niwāģ [nw k! | M ng, N nawa] music, song, melody. *niwé [nwyk! | (N nuwéd)] good news. *niwéy-, -išn, v. niwistan, *niwéyénidan [nwykyn-ytn'] = niwistan. niwistan, *niwéy- [nwstn', nwyd- | nwyk-] announce, consecrate. —išn(ih): announcement. nixwār- [nswb’l- | M nyxw’r-] hasten. -išn: haste. niyübag [nyd’pk' | M ny’bg] becoming, fitting, suitable. ~th: suitability. niyāģ [nyd?k! | M nyg, N niya] grandfather, ancestor. niyāyišn [xyd?dšn! | N ~if] prayer, praise. niyāz [nyd?c | M ny’z, N ~] need, want, misery. —ómand [2wmnd | N ~mand] needy. ~6mandih: poverty. niyē(x)šidan, niyē(x)š- [n(y)duhš-ytn! | M nywi-, N niyófidan] hear. ~išn: hearing. І nizār [nz?l | (P nyz?*wr), N ~] weak, feeble.
PHD.txt:661:2xān [/?п! | P л?п] spring, source. хапар [BYTA < A рур; h'nR! | N хапа] = іхап. xandidan, xand- (*GHBHWN-yitn' < A V ghk, or У *ghqh; hnd-ytn' | (M xnyst), N —] laugh. xānīg [/?nyk! | M x?nyg, N xàni] = *xān. xar (HMRA < А hmr’; hl | N ~] donkey, ass. хаг [P1 | M ær, N ~] thorn. xar-buz [hibwe | M xrbwz] oryx. xar-g68 [higws | N ~] rabbit, hare. хаготапа [/PPwmnd] thorny. xār-pušt [/?Ipwst! | N ~] porcupine, hedgehog. xastan [hstn' | M xst, N ~] wound, injure. xašën [hsyn! | N хайл] (dark) blue. хауар [Pd(y)k! | N xdya] egg. ~-dés [-dys] oval, egg-shaped. xayüg [Ah )dwk! | N xayū] saliva, spittle. xaz [hz | N —] marten. xém [лут] nature, character. xëšm [?yfm, hfm | M xysm, N xifm] anger; the demon Wrath. --én [-ya! | M -yn) angry. xindag [hyndk' | M xyndg] ill, sick. ~th: illness, sickness. xir [C BW! < А sbw; hyl | M хут] thing, matter. xirs [hls | N ~] bear. xišt [Ast! | (P hystyg), N ~] brick. хбё [hwk' | N xwk, xóy] nature, character, disposition. x6n [DM YA < А dm’; һит! | M хоп, N хип] blood. xormā [TE A tmryn; hwlm’k' | N ~] date. xrad [hit! | M xrd, N xirad] wisdom, reason. ~ig, ~Omand [-yā!, тиа | N -mand] wise. xrafstar [hlpst] = Av. xrafstra-] reptile, noxious creature. xridan, xrin- [ZBNN-tn! < A V zbn| M xryd, xryn-, N xaridan, (xar-)] buy. xróhak [hlwhk' | N ~] coral. xrēs [DYLK A < A dkr’; hlws | P xrws, N xurós] cock. xróstan [Alwstn! | M xrwst] call, cry. xüb [hwp | M xwb, N ~] good. ~th: goodness. xuftan, xufs- [HLMWN-tn! < А У Ыт; hwptn', hwps- | М xwpt, N xuftan, xusp-] sleep. xūg [HZWL УА < А hzyr; hwk' | N ~] pig. xükar(ag) [hwkl(k') | N xūkara] hedgehog. xumb [kwmb! | M xwmb, N ~] jug, pitcher. xunak [hwnk' | M xwnk, N xunuk] happy; cool. xurdruš [kwldlwš, -dlpš = Av. xrwidruf] ‘with a bloody club’ (epithet of Xēšm, later misinterpreted as *ul-draff ‘*with raised banner’).
PHD.txt:680:žzēn [zyn! | N zin] saddle. zēn-abzār [zyn'pe!l | N zinafzár] horse-armour. zēnāwand [zy>zond] alert, vigilant. zēndān [zynd?n! | = M, N zindān] prison. «bān [-p?*x! | N -ban] jailer. ~ig [-yk! | N -i] prisoner. zënënidan, zënën- [zynyn-ytn!] look after, preserve. zēnhār [zyn)?] | N zinhàr] protection. zénig [zynyk!] armed. *zibāl [zb | N zībāl] swift (horse, etc.). zih [zyh | N zih] bow-string. zindag [zy(w)ndk! | M zyndg, N zinda] alive, living. ~th: life. zindakkar [zywndkkl | M zyndkr] vivifier, reviver. zinénidan, zinén- [zynyn-ytn'] damage, harm. zirak [zylk' | M zyr, N ~] wise, clever. zistan, v. ziwistan. zišt [zyst! | = P, N ~] hateful, ugly. ziwénidan, ziwén- [zywyn-ytn! | M zywyn-] vivify, revive. zi(wi)stan, zi(w)- [zyz-stn! | M zywystn, zyw-, N zistan] live. zi(w)išn [zywšn! | M zyysn] life; livelihood. ~ih: life, living. --6mand [-”xmnd] living, alive. ziyānaģ [zyd?nk'] young woman. zīyišn, v. zī(w)išn. zofāy [zwp'd | M zwp’y] deep; depth. *~ih: depth. ` zofr [zwpl | M zwwpr, J zwrf, (N žarf)) deep. —šy [2d] depth. ~-payag [-p'dyk'] deep. zóhr [zwhl | M zwhr] libation, offering. zor [z())wl | M zwr, N ~] power, strength. Bay ge J ~ig, ~dmand [-yk!, -wmnd | M -mnd, N —mand] powerful, strong. d z^ 201 [zwt! = Av. zaotar-] first officiating priest. ~ih: office of 201. Zraw-, v. zruftan. !zréh [zlyh | P zryh] sea, lake. *zréh [ziyh | N zirih] armour. zruftan, zraw- [zlwp-tn'] = azruftan. zūd [zwt! | M zwd, N ~] quick(ly). ^h : speed. zür [zwl | M z*wr] false, deceitful.
PHD.txt:2387:impair  wizüstan, (wizūdan); v. damage, injure.
PHD.txt:2402:inability anabzārīh.
PHD.txt:2513:judgement ^ dadestàn, dadwarih; handāzišn, wizir. Jug xumb.
PHD.txt:3133:pitcher xumb.
PHD.txt:3194:power abzār, amāwandīh, nērēg, 07, stahm, tuwān, zor.
PHD.txt:3195:powerful abzār, amāvand, kāmgār, nérógomand, ózómand, pādixšā(y), pādyāwand, warzāwand, orig, zóromand.
PHD.txt:3771:spice abzār.
PHD.txt:5078:zūr, zūr zoromand zūrgugāy zūrgugāyīh zorig Zurwün zofāy zofāyīh zofr zofrāy zofr-pāyag zanjīr zanišn zētīh, zūdīh zot, zūd wahīgt ant
PHD.txt:5104:zēnāwand ayy e$ zēnabzār ` Cer WS zēndānīg oro S zēndān wo pS zēndānbān i^o "GO u$ mër: 15 S. ` mee Ziwénidan zindagih A$ 43 HS zēnīg, zīndag yr
PHD_mackenzie.txt:2714:hamb6y- [hnbwd- I M hwmbwy-, N anboy-idan] smell (tr.) .
PHD_mackenzie.txt:3769:nihumbidan [nhwmbytn ] = nihuftan.
PHD_mackenzie.txt:5583:xumb [hwmb' I M xwmb, N --] jug, pitcher.
PHD_mackenzie.txt:6904: interpret wizardan.                       jug xumb.
PHD_mackenzie.txt:7292:pitcher xumb.                              portico dahliz.
PHD_mackenzie.txt:9596:karr, -gar.                        ~~           kOf                              eu ,,,
```


## [2026-09-05T20:54:01.600Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD abzar/abzudan ===\"; grep -n \"abzār \\[\\|abzūdan\\|abzāy\\|abzōn\" PHD.txt PHD_mackenzie.txt | head -10\necho \"=== HRN leaf for p195 (leaf=195+21=216) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==217' HRN.txt | head -60"
}
```


## [2026-09-05T20:54:01.724Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN p149 leaf 170 ===\"; awk 'BEGIN{RS=\"\\f\"} NR==171' HRN.txt | head -60"
}
```


### [2026-09-05T20:54:03.374Z] TOOL RESULT

```
=== PHD abzar/abzudan ===
PHD.txt:170:abilag 5/4! | N ~a] blister. a-bim [bym] fearless. āb-kāmag [5A mk! | N ~a] a thick, sour soup. abnüs Pžēnws | (N ābnūs)] ebony. a-biy Pbwd] senseless. ~ih: senselessness. à abr РЫ, Séi | N ~] cloud. M bel abrang [ing | N aurang] glory, splendour. abrastan, abraz- [AP stn',SPc- | М ?br?st, N (afráttan), afrdz-] lift, raise. abraz [Pe | N afrāz] acclivity. abrēšom Pflyš(u)m | M? bryfwm, N ~} silk. ~én [-yn!] silken. abróxtan, abróz- ['piwhtn', ?phoc- | M brwxt, ?)brwc-, N afróxtan, afróz-] light, kindle, illuminate, polish. ~i$n(ih): illumination. āb-tazan Pftcn!] watercourse. a-bun [*dwx!] baseless, bottomless. a-burd-framān ['bwltplm^n'] disobedient. ~th: disobedience. aburnāy f(w)lnd, v. purnāy | N burnā] under age, child. ^h : childhood. aburnáyag [?A(w)/n’(d)yk'] child. abus [pws] (woman) having just given birth. “АҺ: childbirth. арив, -tan Pws, -tn! | M ’bwws, v. ábestan] pregnant. „il: pregnancy. abydxtan, abyóz- Phywhtn', ?bywc-] join, mix. āb-zan zn! | N ~] bath. labzar [el pel] M *6c*7, N afzār] instrument, means; spice. *abzar [6271 | M bail skill, power; powerful. „ūmand [-wmnd] skilled, able. abzāy-, —išn, у. abztidan, abzón [?pzwn! | M, J ”*bzwn, N afzün] increase, growth. ~ig [-yk!] increasing, expansive, bountiful. ~igih: bountifulness. abzüdan, abzáy- ['pzwtn!,^?pzd- | M ?bz'y-, N afzüdan, afzāy-] in- crease, grow. ~i$n: increase, growth. a-čār [cI] inevitable, Jee ~ag [-k'] compelled.
PHD.txt:680:žzēn [zyn! | N zin] saddle. zēn-abzār [zyn'pe!l | N zinafzár] horse-armour. zēnāwand [zy>zond] alert, vigilant. zēndān [zynd?n! | = M, N zindān] prison. «bān [-p?*x! | N -ban] jailer. ~ig [-yk! | N -i] prisoner. zënënidan, zënën- [zynyn-ytn!] look after, preserve. zēnhār [zyn)?] | N zinhàr] protection. zénig [zynyk!] armed. *zibāl [zb | N zībāl] swift (horse, etc.). zih [zyh | N zih] bow-string. zindag [zy(w)ndk! | M zyndg, N zinda] alive, living. ~th: life. zindakkar [zywndkkl | M zyndkr] vivifier, reviver. zinénidan, zinén- [zynyn-ytn'] damage, harm. zirak [zylk' | M zyr, N ~] wise, clever. zistan, v. ziwistan. zišt [zyst! | = P, N ~] hateful, ugly. ziwénidan, ziwén- [zywyn-ytn! | M zywyn-] vivify, revive. zi(wi)stan, zi(w)- [zyz-stn! | M zywystn, zyw-, N zistan] live. zi(w)išn [zywšn! | M zyysn] life; livelihood. ~ih: life, living. --6mand [-”xmnd] living, alive. ziyānaģ [zyd?nk'] young woman. zīyišn, v. zī(w)išn. zofāy [zwp'd | M zwp’y] deep; depth. *~ih: depth. ` zofr [zwpl | M zwwpr, J zwrf, (N žarf)) deep. —šy [2d] depth. ~-payag [-p'dyk'] deep. zóhr [zwhl | M zwhr] libation, offering. zor [z())wl | M zwr, N ~] power, strength. Bay ge J ~ig, ~dmand [-yk!, -wmnd | M -mnd, N —mand] powerful, strong. d z^ 201 [zwt! = Av. zaotar-] first officiating priest. ~ih: office of 201. Zraw-, v. zruftan. !zréh [zlyh | P zryh] sea, lake. *zréh [ziyh | N zirih] armour. zruftan, zraw- [zlwp-tn'] = azruftan. zūd [zwt! | M zwd, N ~] quick(ly). ^h : speed. zür [zwl | M z*wr] false, deceitful.
PHD.txt:2167:growth ārēyišn, rēyišn; (increase) abzāyišn, abzón, wālišn, waxšišn.
PHD.txt:2410:increase (n.) abzón, abzāyišn, fra- dahišnih, mehēnišn.
=== HRN leaf for p195 (leaf=195+21=216) ===
- 195 —
Note 32) wahrscheinlicher ist als die de Lagarde's
(Ges. Abh., 55), so nehme ich eine aw. Nebenform
"^kawza- an (vergl. unter np. ;ifMsprrfew, No. 483)^).
873. höliden graben, aufreissen.
kurd. Icölän ^aushöhlen, ausgraben'; wa/. parjkölam
*eine Grube, einen Brunnen graben .
Justi, Kurd. Gramm. S. 205 No. 88 vergleicht
deutsch 'hohl\ das gewöhnlich zu got. hulundi *Höhle\
lat. occulö etc. gestellt wird.
874. kün 'Hinterer.
phlv. kün, kün\marz.
kurd. LW. hm, qlng neben qin, km (H.-Sch.);
bei. LW. kün, n. IHn (208).
Geiger vergleicht ai. l^knü- einen bestimmten Ton
von sich geben*, aber diese Wurzel kommt nur im
Dhätup. vor.
875. höh *Berg', köhe 'Höcker.
Käs. Q. küfün *Höcker ; kauk.-bergjüd. knf,
ap. kaufa- 'Berg* ; aw. kaofa- 'Berg, Höcker; phlv.
köf, köfak *Berg, Höcker'.
AUg. entlehnt; echt bei. köpak, n. ßöfay (211)
'Schulter*, kurd. kuwi 'wild*.
876. {\)ki{h) wer, welcher? dass etc.'; /.^ (ältere Schreibung,
z. B. AM.; äähn. I, 39 Vers 81)-), sowie in käskl,
kaßi (Öähn. I, 95 Vers 609).
Käs. ke, kl, ko, kö.
ap. aw. ka- wer?'; päz. ka (Conjunction), ke (Pro-
nomen) , ku (Partikel) , doch werden diese drei Aus-
sprachen häufig verwechselt; ai. kd-,
kurd. LW. ki(h); oss. d. f^a wer, welcher, dass' (149);
bei. ke, kai, n. Mai 'wer?' (200); wa/. küi, kör, sar. <J(5/
*) Skr. kiihjä', dessen Bedeutung 'buckelig, krumm* schon nicht
zu 'Topf* passt, vermag ich auch lautlich nicht mit dem Awostaworto
zu vereinigen. Bei Osthoff, Perfectum S. 33 vermisst man aw. nhjyeife.
•) Repristinirt auf Inschriften in Indien, Hörn, Epigraphia in-
dica, Vol. II. Abu Mansür Muvaffaq schreibt das Pronomen wie auch
die Conjunction öfter mit Kesre, z. 11. S. CA Zeile 1 v. u., S. 70 Zoilo 13,
S. 75 Zeile 7.
13*
```


### [2026-09-05T20:54:05.048Z] TOOL RESULT

```
=== HRN p149 leaf 170 ===
149
Der Bedüutungsunterschied macht diese Zusammen-
stellung bedenklich.
671. niindän 'Gefängniss'.
aw. *2:aewa.d(2wa- (y) ; ^\\\\, z(i)ndan (PPöl.); arm.
LW. zndan.
Etwa urspr. 'WafFenarsenar wie auch HNIliNDN (Jer.
32 (2) 8) *Ort, an dem die Scheiben aufgehoben werden*,
allgemein 'Gefängniss* heisst? Darmesteter, Et. ir.
I, 290 setzt zweifelnd auch np. zen}Tr^ zmjlr (andere
iranische Formen siehe bei Geiger bei. LW. No. 299)
hierher 0. Vergl. Hörn, KZ. 32, 583 No. 13 2).
672. xinüden, zunüden *heulen , Praes. ziuec-em, ztmöylden.
ai. [/'nav-j naiiti, ndmite *brüllen (von Tieren)', mit
accha 'zurufen' (mit ud kommt es nicht vor).
Vergl. np. nöyiden etc. (No. 1054).
673. xüd 'schnell'.
aw. \/jav- 'eilen*, Java, javarö (?, Geldner, BB.
XIV, 21, 22, aber auch KZ. 30, 533); phlv. zät (päz.
zöt); ai. i^jav-, jdvate *eilen*.
kurd. zu; bei. züt^ zU, n. zid^ (430).
674. zur 'falsch; Lüge*.
ap. zurah- {znrah-) ; aw. zurö.Jata- ; phlv. zur,
zür]zat, zür]ynhäsih, arm. LW. zur\ ai. hvaras-.
Bartholomae, zuletzt ZDM6. 46, 296, Ilübsch-
mann, gleichzeitig ib. 329.
674*»^'* {\)»ör 'Kraft, Gewalt' (reimt auf hör, Sahn. I, 202
Vers 1311).
aw. zävar- 'Macht, Kraft*; phlv. zör, zörlh, arm.
LW. zatir^ zaurcwor, zauruüun,
LW. kurd. afy. bei. (312) zör.
675. {^i)zör 'Weihwasser (pärsisch).
aw. zaotirä' 'Weihwasser*; phlv. zölir, zur, arm.
*) Im Ossctisclicn bezeichnet das L W. zjndon *Höllc* (v o n
Stack elberg, Baltische Monatsschrift, XXKVIII, lieft 8, 674).
*J Herr Prof. Nöldeke vermag zindän mit plene geschriebenem
i bezw. e im Pehlevl zu belogen, was für die Richtigkeit der obigen
Etymologie spricht.
```


## [2026-09-05T20:54:20.388Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HUB leaf 27 (p.16) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==27' HUB.txt | head -60"
}
```


### [2026-09-05T20:54:22.011Z] TOOL RESULT

```
=== HUB leaf 27 (p.16) ===
— It) —
— ap. *ava-pa8tanait/ (vgl. zd. avapasti- 'das Herab-
fallen) als Neubildung. Ich nehnie daher— wie Mann-
Andreas ZDM6. 47, 702 — an, dass OftGdan zum
Praesens oftad nach dem Muster von ^tadan = praes.
estad gebildet ist. Schwierigkeit macht nur die Bildung
des Praesens, denn Dftad setzt ein ap. ^ava-ftatiy = skr.
*ava'ptati (nach der 6. indischen Klasse von der Wrzl.
pat gebildet^) voraus, das sonst nieht vorliegt. Nach
dem Intinitiv hat sich wie gewohnlich das Particip
gerichtet, daher uftada *lapsns, vastatus, humilis, sub-
missus etc. fur das ursprungliche ptc. ^pasta^ (skr.
patita-), das ich in np. past parvus, depressus, planus,
devastatus, humilis' wiederfinde.-)
93. Np. afraxad ist nach Horn's richtiger Etymologie
(Wrzl. reg^ in ogiyto u. s. w.) — zd. aiwi + razay^iti
(vgl. zd. rdzayfAti 'ordnet', osset. araztn rich ten), also
afraktan der ursprungliche, afraxtan der (nach Analogie
von afrozam : afroxtan u. s. w.) neu gebildete Infinitiv.
Ebenso jetzt Fr. Miiller, WZKM. 8, 186.
95. Np. afzar Werkzeug* (bal. LW. auzar) ~ phi. afzar
geht nach ZDMG. 32, 408 auf ein ap. ^ahizara-, nicht
*abidara- zurtick. Daher bleibt arm. ddar 'arredo, for-
nimento, rimedio* etc. (das Fr. Miiller wieder heran-
zieht) besser weg. Mit ap. ^abizara- deckt sich laut-
lich skr. abhihara-^ das aber 'Herbeibringung, Raub* etc.
bedeutet.
96. Aus aiwi -\- savay^iti ware im Neup. ^afsdyad ge-
worden: das vorliegende afzayad Vermehrt' muss auf
*aiwizavayfiti zuriickgehen % das sich vielleicht zu skr../t^
^) Vgl. skr. avapatati *fallt herab* nach der 1. Klasse.
*) Vgl. afgh. LW. ufiSUiq 'humble, meek' neben afgh. LW. past
*low, abject, lower, below'.
') Bei solchen Reconstructionen mUssten eigentlich imm'er die
altpersischen Grundformen angesetzt werden. Da aber die (vorhandenen)
Zendformen hftufig fiir die (fehlenden) altpersischen eintreten mCLssen,
erlaube ich mir hier mehrfach, das Neupersisohe direkt an das Zend
anzuknupfen, wie auch andere Gelehrte thun.
i
```


## [2026-09-05T20:54:23.332Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT zāvar ===\"; grep -n \"zāvar\\|zavar-\\|zävar\\|z.var-  n\" BRT.txt | head -20\necho \"=== BRT zav- root / zava ===\"; grep -n \"^.\\{0,6\\}zav-\\|zavaiti\\|aiwi.zav\\|'zava-\\|zava- \" BRT.txt | head -20\necho \"=== BRT search Kraft Stärke zav ===\"; grep -n \"zaväiti\\|zavara\\|zavarə\" BRT.txt | head"
}
```


### [2026-09-05T20:54:25.375Z] TOOL RESULT

```
=== BRT zāvar ===
2899:•  j.,  g.  'ao}ah-  n.  '(physische)  Kraft,  Stärke': asistim  narl  alaotw  °Jö  Y.  60. 3;  —yakmi niyne  nars  'Jartha  Y.  /o.  a ;  —  ai-avaia '}arfka  yaia  yal  panca  narS  "mit  solcher Kraft,  als  wären  es  fünf  Männer"  V.  jj. loPaZ.;  Yt,2.i2,  14;  —  usla  U yd  ä"j 'jaiika  vasöjciairä  ahi  haoma  Y.9.25; —  kacaiti  dim  aspahe  "Jö  uitrahe  °Jö vlrahe  °j<>  Yt.  it).(i&;  8.2^^;  —  "jö  tanvö vispaya  Yt/.^.29;  —  -jö  vJspdMnüM  Y. 5.17;  —  drfahela  paiti  °)arakö  Yt,  i_j. 134;  ~-  y~'  itfsfro)  arinam  ..  matilüm 'jö  abaraiii  \t  14.12;  —  apa  .  .  buei'ä- °}5  , .  barahi  apa  pä',ayä  sävar»  Yt.  10. 23;  62;  —  haomö  asibil  yöi  ..  zävari "jssca  baxhili  Y.  9. 22; —  °Jasca  nn- S«)Wf'a..Y.  77.8,  yi.j.22,y.i,Y.  72.6;  — yS  nü  asSif  °janAil  vandayaÜJ  (sd.)  ., gae^am  Y.50,3.  a)  AS.  °jö  als  Adv,
11955:—  "nvS  vlspayä  drvatätim  °nvS  vTspayä vazdvar)  Yt/4.39;  —  imfm  'hwqm  ..yänim haema  Jailyemi  drvatätim  atiiAas)  'nvS.. darrjB.jltlm  ustänahe  Y.p.19;  K.i.Z;  — 'nuyäsca  paiti  druaiats  Yt.  13. 134;  —  aha r0  tarn  sraos'a  . .  zävar»  daya  AitaHbyB drvatätitn  °nubyu  ".  ,  Kraft  unsem  Ge- spannen, Gesundheit  unsern  Leibern"  Y. j7,  i6;  —  däl»m  te  'nuye  ^annd  'Yt.iy. 12;  15;  — ya>a  tW . .  ifä'^ravaiils  'nvö +,iwi/J  (Sp.  274  IL)  Y.  60.  11;  —  vohü uxsyä  (sd.)  manan&ä  .  .  ui'tä  'nUm  Y. ^.10;  —  haomü.artharstahe  (sd.)  hizvS mq%rS.hitahe  (sd.)  °nvd  A.4-5i  —  im Gegensatz  zu  gaihä-  (Sp.  477  in.),  urvan- usw,:  akmäi  nfmaahl  ävaldayamaidi  gal- %^slä  'nvascä  nipätayaicä  , .  Y.  56".  2  j  —  yö nS  . .  iririx/äite  gaghanqm  .  .  °nunqm  Y. 65, 7 ;  —  frähatiia  asake  gaghä  .  ,  asahe °nuy!  Yt,  6.1;  —  forasayäi  (sd.)  aibi %waha  gai'iäAa  -nuHcä  Y.  43.  T,  — 'nvagca  * kaosravar3h»m  untnaija  dan^tm havanium  F.^h;  —  cim  ,  .  qst>m  isaiti 'rwa  cim  uruna  Aog,  4^;  —  vJspS  gai- %isca  -nvasia  azdsbisca  .  .  iistänqs^a urvätamca  . .  pairica   dad>mahl  Y.  55.
20541:•  j.  miÖTÖ-drug-  Adj.  'den  Mf^ra  be- lügend, betrügend',  auch  sva.  'den  Vertrag brechend'"':  msrsncaiU  vTspqm  dai^kaom mairyS  'druxs  Yt/o.  a;  19;  —  VtspsAu paiti  barszähu  .  .  spass  änAaire  mikraAe ''  drujim  *AispS.S3mna  Yt.  10. 45;  — pdhS. . yim  wnii  'ärup (SP.)  Yt.  10.4$;  i8,  80;  — aspacilySi  *drujam  vazyqstra  (sd.)  bavaintt Yt.  JO.  20;  —  mihrS  .  .  tiaram  'drujqm apqlgavS  dar)zayeiH  Yt/0.48;  —  mi^rtm .  .yö  nöit  kaAmäi  'drujqm  maiyänqm  aojö da\siti  n5il  zävar»  Yt/O.öz;  62,  23,  26, 37%  38.  73,  133.  J-^- 63;  —  hamistayalca ..  mihrB.zyqmca  *'drujimca  Y.  ö';.  3;*Yt .10.82.
20789:10  m.)  bairyänte  yaisam  dim  /räye{%d^ vohunqm  V._j.  29.  p)  adjektivisch,  in- sofern das  Bezugswort  (Substantiv),  das man  beim  vorbeigehenden  Demonstrativ erwarten  sollte,  in  den  Relativsatz  gezogen ist:  aisqm  sanaoiti  virikrafmm  ySi  dim dahma  . .  fräyaz^nte  YL  /o.  16;  —  haomS aiiHi  ySi  aurrantö  hila  taxs^nti  arvnäum zävars  .  .  baxiaiti  "H.  schenkt  den  Hel- den, die.."  Y.5.22.  f)*iiÄrii-(Sp.34  o.); nur  B)  iinjAvr.;  das  Relativ  ist  substan- tivisch: aisS  *ratufris  yö  nSit  * aiwi-srun- vaili  N.  24;  *ig,  60,  V.  16.  5;  —  aÄ'a sadiranqm  . .  yä  *alaone  *daste  N.  84; —  baya  also  (in  Kongruenz  mit  dem Praed.)  äs  ahunahe  vatryehe  . .  y at  ii  frä- vaoc)m  Y.ig.^;- — aisa yeAhe apmnäyükB N.<?;7-.  g)  ^aaa-  (Sp.  13U.,  16  u.); nur  b)  im  jAw.;  das  Relativ  ist  substan- tivisch: all3m  a?sm»m  yö  vaoce  *n>miüika nqma  Yt.  74.  55;  —  aitayä  urvarayä  yä vaoce  hatäna^äta  V,  14.  4;  Yt  /4,  55;  — ime  alle  vaca  yöi  h?nti  atfrahe  mainySvS snäk?m  V.  10.  16;  3,  15,  17,  N._J_J;  — ku%a  aital  druxs  ppnnäne  yä  .  ,  upa fvaniim  upa^dvqsaiti  V.  /o,  i ;  i ;  —  tata^ bansma  yat  paiti  äp?m  fränayantgma N,  70;  —  altat  . .  yat  ti  asti  spmts.main- yaom  Y.  35.  j;  —  aKa  dämqn  .  ,  *yqm (APn.)  da%at  ahurB  Vr,  12.  4;  —  aOa^a daxmalsva  ..yöi paiti  äya  ztmä  bavainti
23246:•  j.,  g.  vazdvar-  n.  'Beständigkeit';  a)  sva. 'Ausdauer':  tanvS  vlspayh  drvatätsm  lanvs vUpayh  °pffl«  Yt  14.29;  —  tanvS'vars.. tamis  vpr?%rfm  Y.6S.11.  b)  sva.  'un- unterbrochene Dauer':  disyJt  ahmai  naire avat  müdsm  . .  'var)  vakistakt  aithSus V.J. 44;  —  ma*dä  dadat  ahurS  hauniats atmrttätas^a . .  asahyäcä  . .  xia%rahy3  sarO vatfhSul  'varV^  manatahö  yS  .  .  "MAk. wird  . .  die  besändige  Gemeinschaft''  mit If.  und  Am.  und  mit  Asa,  mit  Xf.,  mit VM,  dem  gewähren,  der  .  ."  Y._;r.  21.
27776:VgL  zävar;  —  Pü. :  vahumaii  gri/lär  haue  pa an  dahiin^  Sü. :  gvahman&sya  grahiläro  AAtwä' maii;  vgl.  zu  laalar-  No.  8.
28089:•  j.  zävar-  n.  '(physische)  Krafl,  Stärke': 'var»  aojaiia  Yt  13.  i ;  10.  62,  F.  20\  —  : aojas'a  zavanca"^  Y.  72.  6;  7J.  8,  Yt. i,sz.  a)  insbes.  a)  der  Ftlsse^;  yat kl  da'i^at  .  .  patave  'vars  YL  16.  7 ;  Y.  ^. a8;  —  apa  pälayä  "var>  (näml.  barahi) Yt  ro.  23.  b)  der  Rosse:  'van  dayä' hitaiibyö  Y.  57.  26;  Yt  iO.  1 1 ;  —  yS  mqm
30056:•  j.  hita-  Adj.  (fem.  Ha-),  PPfP.:  s- ha(y)-.  a)  m..  Du.  und  Plur.  'Gespann, Gespanne'  (von  Rossen):  ysi  .  .  Ua  (AD.) taxhnti  annäum  (sd.)  Y. 9.  32;  —  sraosa . .  zävar^  daya  'taHbyS  drvatät>m  lanubyS ¥.57.26;  Yl/o.ii.
=== BRT zav- root / zava ===
7662:■»«zav-
7697:"arazav-
8596:•  j.  uzava-  m.  EN.  eines  Gläubigen:  'vaAe
27532:'ta  ratufril  tthun>m  vair^m  frasraofyehe'i *vSspati6yS  aliiyS  ySi  hl  *mm»mya  vala /rasrävayamnake  vä  itpa.srumianH  *yal  vä *yastam  *yas3mnahe  "Für  wie  viel  Personen (im  Höchstfall)  darf  ein  qualiüzirter  Z.  das AhV.  aufsagen,  wenn  er  den  R.  genehm sein  will?'  'Für  alle  (d.  L  so  viele),  die ; (als)  ihn  hören  können,  wenn  er  ihn  (den  | AhV.)  mit  mittelstarker  Stimme  aufsagt oder  aber  wenn  er  (entsprechend)  den Ki/wa  betet'"  N,2o; — yai  aevS  -tafrä". yazäiti  myasdahe  *ayqn  'iars  gütava; *altata  myazde  *aiwi.va^ayeiti  .  .;  -tari  ^ gätava  *ahun?m  vairTm  frasrävayöit  *syao- ' %nl!.täitya  {sA.)  * hävanaiibya  paiH.jaahStl , hSvatiänS  gätüm;  ätravaxsahe  gatava  äta- nm  *aiwi.vaxfaydit;  frabmtarl  ^gstava yasrum  haptatshäifim  *frayazäiti  "wenn der  Z.  allein  den  Gottesdienst  vollzieht am  Tage  des  My.,  soll  er  am  Platz  des Z.  (sich  anstellen).  Hier  soll  er  die  My. zuweisea  ..  Am  Platz  des  Z.  soll  er  (noch) den  AhV.  anstimmen,  aber  bei  der  Stelle iyao'^ananqm  soll  er  sich  zum  Mörser  be- geben auf  den  Platz  des  Hiiv.  Auf  dem Platz  des  Ätr.  soll  er  das  Feuer  schüren, auf  dem  Platz  des  Frab.  soll  er  den  Yama HafthAtn"  N.A;  —  *'iari^  daifyS.gatul maifmya  nmänahe  matfmst  arahraoi apa.srilS  "sinuiüxti/ (sd.)  "des  Z.  gehöriger Platz  ist  in  der  Mitte  des  (Gottes)hauses  *', der  Mitte  des  Gerätetisches  zugewendet,  . ." li-7^;—y^  bityö  Ha  N.J7»(?).  a)als Vertreter  des  Priesteretandes:  gäus  "tänm zavaiti  Y.  //.  i  *'.  a)    von  Haoma    als
27759:»'in.  —  ')  Einen  AP,  aui  'zava-  (ai.  hdva-  \ m.)  halle  ich  Iroti  RV.  /.  183.  5  Rr  weniger ' wahrscheinlich,  weil  in  Y.  29.  3  das  Ziel  schon duTcb  den  Dativ  zum  Ausdruck  kommt  (Sp. 495  n»-)-
=== BRT search Kraft Stärke zav ===
```


## [2026-09-05T20:54:51.082Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT Eile ===\"; grep -n \"Eile\" BRT.txt | head -20\necho \"=== BRT aipi.zav / api.zav ===\"; grep -n \"aipi.zäva\\|aipi\\.zav\\|api\\.zav\\|aiwi\\.zav\\|aiwi\\.zäv\" BRT.txt | head -10\necho \"=== BRT zav- headwords ===\"; grep -n \"zav-  \" BRT.txt | head -20"
}
```


### [2026-09-05T20:54:51.187Z] TOOL RESULT

```
=== BRT Eile ===
=== BRT aipi.zav / api.zav ===
=== BRT zav- headwords ===
5397:•  j.  auru5a.bäzav-    Adj.    (auch   : 'weissarmiß':  kaininö  kihrpa  . .  "Zfh  \^o.,  .  ^  ,,     ,
6493:die  Peitsche  knaÜt'  Yt,  /o.  1 1 3 ;  —  j«/ . . , ,  j.  as.bazav-  Adj.  'mit  tUchtigen,  starken 'rä  kakvqn  (sd)  Vtio.113;    —   Ja/  -4?  Vorderbeinen,  -schenkein':    uströ .  .   'zSus iyimai)  zaya  frabanm^  aum  y5  ahurö  .  .    (fjs.)  aii.kaüß  Vt  14- 12. suwram   (sd.)  .  .    'ramca  '>   zaramo.paisim  I      Kpü.;  läMib  biryär  zur  az-ar  bäsuvän. V.2.6;-»^Ä0,™)  .,y«/(sdL)  -ra,^  .    -    ^.t,„,.   ^dj.    (auch    fem.)    'rid, V.2  10.  .)    inb»    dit    pntsteihcht   ,^iai\A   bringsnd':  /r.valml .  .    ,4    ■Is
7692:•  g.  '«razav-  (,  p.  aräav-)  Adj.  'gerade, richtig,    recht',    vom   Weg;   yJ   «./    °züi
7701:•  j,  'arazav-  m,  EN.  eines  Gläubigen' Bruders  des  Sra/öjpada  (sd.):    'ma  (GD.) srBtöjfädä  ahonä  Yty,  115.
7705:•  j.  ^razav-  m.  'Finger":  °zu  F.jg;  — ci'al  gaonahe  (sd.)  . .  ya  dvaHbya  "zubya *hiing3riwn,lt  N.  Ö5;  —  avaval  tafta  ydha kasistahe  (,  mawmaAe,  masistahe)  °svB sisV.6.10,  12,  14, /Ä44  PüZ.  a)  die Breite  der  Finger  als  Maasseinheit:  dva 'ZU  nismaAe  (sd.)  V.(j.6;  —  avavat  aipi yd^a  caiwärS  °zavö\.g.2();  —  cd^wSrö 'zvö  V.  6.  43,  f).  6.  [V.  iS.  2  PüZ. :  lies bai.intu\
8118:•  j.  Ujra.bäzav-  Adj.  'starkarmig':  {iiit^r?) ':,iu/ (NS.)  Yt.  70.  75.  [Vt  70.42:  lies ujra  dinara.]
8661:•  j.  uz-bäzav-  Adj.  (auch  masfc.)  'die Ajme  emporhebend';  °zäus  (NS.)  fiaiii attunxllm  (sd.) /ravazai/e  mi^rS  Yt,/o.ia4.
11601:•  y  Jazav-  m,  (auch  mit  'spart-  m.)  Name einer  Art  des  Hundegeschlechts:  hau  °z3us (GS.)  hau  visäui  . .  hau  vTspanam  . .  spa- ct^ranam  V. /J.  16;  —  spä  *ius  V.^.^j.
17125:•  j,  bäzav-  m.  i)  'Ann'  der  Menschen  und       '  5'  '*     ..  ..r,    _  .   i-n^    ,  *j:  -.^  « i-M^         i-,   -r  ,/TL'      .    Tc-v.i   j   <■      ■         Komp.  mit  ND.  im  l,  Glied;  s.  ituan-  A. Gotter:  ÄJtJv« '«i'jfLb.  als  IS.)'' j(jn«aiv)        .     /_      ■      v  ^      .  j-     (^    .     -       j ./aÄ«.-«.ä*te.«,*5,"milde,»li,JimAnn  •   !■   bs^-s-aolah-   Ad,.    Oak    m    den «.d  dem  «cht«,  mit  de«,  rechten  Ar»  m,d  '^f  "»  *^'  "^'  '""• '  -»ß-»«. . . deoh»kei."V.j.>5i-j...,yü!j»,,;7™i,  V»«"!'"  '?*''/'/?;  \t.,o.,y,-«-a^,aAr
20163:•  j.  mazav-  Adj.  'acht  habend  auf  — ',  mit Gea:  a^a  spamm  nida%}m  yat  dim  'zacs (NS.)  k)hrps  türahe  "den  Hund  habe  ich dazu  bestimmt,  dass  er  acht  habe  auf  die Person  des   Tärere"  V.  13.  39.
20395:•  j.  'msrszav-  n.  'Wirbel'  des  Halses  und Rückens:  yavata  . .  tii/ainti  °tu/a  ttünB gayehe  'sula  x&  uimnahe  "bis  er  entzwei
20399:j.  'iD'Srazav-  in.,  Du.  Bezeichnung iner  a frischen  Schöpfung,  vll.  eines Sternbilds:  nizbayemi  'zu  ^pourvs  *:^a%/ltd yüßis/ff  mairtivä  *d3mqn  'ich  rufe  an  die beiden  M.  im  Süden,  die  ewigen,  die  am besten  kämpfen  von  der  Schöpfung  der beiden  Geister"  V.  ig.  42.
20401:•  j.  Jm»r»zav-  Adj.  (fem.  'zvt)  —  ?— : zaya  ava%a  staxr!>{sA.)  yat  ha  druxsaHH 'ZVT  FrW.  S.  2  '>.         Vgl  '^mjnzu.
21480:•  j-,  g.  yazav-  Adj.  (fem.  yetivl-)  ■>  'der jüngste':  yasui pu%r3  F.  4g;  —  yasüm pu'hnm  'VyX.26;  —  pouruMstaisA.)  yesiv (VS.)  dt^rqm  (sd.)  tardku^rahl  Y 53-  3-         a)    sva,    'der   letzte':   o/   Saca
24155:•  j.  W-bäzav-  m.  'Klafter">  als  I^ngen- mass:  nava  °zva  (AP.)  ärajS  kimäi  paiti cähruicmqm  V.p.a;  32PUZ.,  ig.%1.  PliZ.
24565:•  j.  vizav-  m.  Name  eines  Nahrungs- miltels:  ralufriH  snSkmilca  'susca  (IP.) " :ifastais[eä\  . .  *atäyäis  . .  N. 57.
```


## [2026-09-05T20:54:53.509Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== CHEUNG zav / zaw ===\"; grep -n -i \"\\*zau\\|\\*dzau\\|zāuar\\|zavar\" CHEUNG.txt | head -20\necho \"=== SOD bj / increase ===\"; grep -n \"βj\\|bj'w\\|bj\\`w\" SOD.txt | head -20\necho \"=== SOD entry 103 ===\"; grep -n \"^103 \\|^ *103 \" SOD.txt SOD_pages.txt | head"
}
```


### [2026-09-05T20:54:55.329Z] TOOL RESULT

```
=== CHEUNG zav / zaw ===
11948:‘dry’. © Kurd. ziha, zuhä is not from *zu-ta- (i.e. *zau, e.g. Pth. wyz’w- ‘to exude, 
30392:*zau 471 
30455:*Zau ‘to pour (libation)’ 
30460:472 *zauH 
30494:*zauH ‘to call’ 
30527:gall’ < *a-zausa- ‘dis-pleasure’, *zau8. 
30541:*zauš ‘to take pleasure, rejoice in’ 
55139:*sam, *sand (s.v.), *zaus 
55368:*yarHz (s.v.), *zars', *zaus 
55891:*uab/f! , *xraus, *zauH 
56007:*uaic (s.v.), *uar(H)', *zaus 
56019:*uab/f! , *xraus, *zau H 
56345:*xsai (s.v.), *zauH (s.v.) 
56470:*yarHz (s.v.), *zars', *zaus 
57091:(s.v.), *raub (s.v.), *zaus 
57382:*haic, *Hraic, *Hmaij , *zau 
57481:*zauH (s.v.) 
57535:*yarHz (s.v.), *zars', *zaus 
58120:*kaH!, *kanH’, *naz, *zaus 
=== SOD bj / increase ===
=== SOD entry 103 ===
SOD.txt:8262:103  VkJ  B  (u^>^-j^jjT 
SOD.txt:24809:103 
SOD_pages.txt:4124:103 VkJ B                               (u^>^-j^jjT                    chief of table"
```


## [2026-09-05T20:55:07.140Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SOD increase ===\"; grep -n \"to increase\" SOD_pages.txt | head -20\necho \"=== SOD bj ===\"; grep -n \"bj[\\`'’]\" SOD_pages.txt | head -20"
}
```


## [2026-09-05T20:55:08.309Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== CHEUNG afzudan ===\"; grep -n \"afzūdan\\|abzūdan\\|afzāy\\|abzāy\" CHEUNG.txt | head -20\necho \"=== CHEUNG *zau block ===\"; sed -n '30380,30400p;30455,30500p' CHEUNG.txt"
}
```


### [2026-09-05T20:55:08.814Z] TOOL RESULT

```
=== SOD increase ===
=== SOD bj ===
16658:4528 yyp6      B, S     j->)(^bj' jT jl «y JU <ju <->>- <o^     4538 yyrtrcyq     S                                */ j>*
17997:              Hen. Tales. 474, 7b; GMS 1018             ^yJ^ Ijbj'
```


### [2026-09-05T20:55:08.892Z] TOOL RESULT

```
=== CHEUNG afzudan ===
=== CHEUNG *zau block ===

«PIE *g(e)rH>- ‘to bewail the deceased (i.e. through lamenting, calling, singing (etc.) 
in honour/memory of the deceased)’ = LIV: 161 | Pok.: 352 

ЈЕ COGNATES: Gr. үйрос ‘voice’, Olrish -gair ‘to call’, OE cearu ‘sorrow, care’, 


Engl. care 
*REFERENCES: Abaev, Slovar’ I: 96 Ё; DKS: 349a f., 355a; Abaev, Slovar’ IV: 295 f., 23 f., 288 f£; 
Cabolov 2001: 105; Shahbakhsh: s.v. zar-; Korn 2005: 206, 379 


*zau 471 


*zarš! ‘to be excited, delighted, rejoice’ 

*AVESTAN: YAv. zarš- ‘to be excited’ = Liste: 68 

MED.; Partic.: pres. (a)ia- Y Av. zarSaiiamna- (Yt 14.20) 

*Zau ‘to pour (libation)’ 
*AVESTAN: YAv. zaodra- ‘libation’ (Y 22.1, Y 66.1, Y 68.1, etc.) || (+ *a-) ҮАУ. 
a-zuiti- ‘clarified butter, sacrificial fat’ (Yt 10.65) 


472 *zauH 


*PARTHIAN: (+ *ui-) wzw- ‘to fade, wither’, wyz’w- (caus.) ‘to exude, extinguish’ 
=> Ghilain: 76 | DMMPP: 362b, 360b 

Pres.: IND. 35р. wzwyd, 3pl. wzwynd; Partic.: perf. pass. wzwd; Caus.: pres. IND. 35р. “wyz’wyd, 1р1. 
wyz’w’m, 3р1. wyz’wynd 

*KHOTANESE: LKh. ysun- ‘to pour, strain’ || (+ *ni3-) LKh. *nalysv- (na’ysv-) ‘to 
issue’ || (+ *ui-) buysai- ‘to extinguish’ => SGS: 113, 49, 101 

*SOGDIAN: BSogd. zwt’k ‘beer, liquor’, CSogd. Хуу (Asg. m.) ‘libation’ || (+ *ш-) 
MSogd. wyz’w ‘extinction’ 

*NEIR: (+ *apa-) Oss. I. evzyjyn/avzyd, D. evzujun/evzud ‘to fall out (of hair)’, 
Yzgh. zaw-/zod ‘to tread down, compress, squeeze’ || (+ *upa-) ? Yi. avzáno, M. 
yivzano ‘wooden ladle’ || (+ *ui-) Sh. wizaw-/wizud, Ishk. (w)uzin-/(w)uzit, Sariq. 
wazew-/wazid, wazud, Yzgh. woziw-/wozod ‘to be extinguished’, Yzgh. 
wozaw-/wozawd ‘to extinguish’, Yi. wuzä-/wuzievd- (caus.) ‘to extinguish, blow out 
a fire’, Yi. wuzyo ‘extinguished’ 

*SANSKRIT: hav ‘to sacrifice, to offer, to pour (an oblation, ghee etc.) (RV+) 
c» EWAia II: 808 

«PIE *g"eu- ‘to pour, libate” > LIV: 179 | Pok.: 447 f. 

*IE COGNATES: Gr. ҳёо ‘I pour, to spill’, (ppp) Gr. хотос ‘spilled’, Toch. В ku- ‘to 
pour’, Goth. gup (n.), Engl. god, etc. 

*REFERENCES: IIFL II: 264b f.; Abaev, Slovar’ I: 214 f.; EVS: 109b, 96a, 118b; Werba 1997: 270; 
Cheung 2002: 168; Kiefer 2003: 194b 


*zauH ‘to call’ 

*AVESTAN: Zu- ‘to call’ || (+ *abi-) ‘to call upon’ || (+ *ä-) ‘to call to’ || (+ *upa-) ‘to 
call upon, invoke’ || (+ *uz-) ‘to call out’ || (+ *ni-) ‘to call off, herabrufen’ = Liste: 
69 

Pres. {1} (a)ia-: IND. 15р. YAv. äzbaiia (Y 15.1, Vr 6.1), YAv. nizbaiia (Vd 20), YAv. zbaiiemi (Y
```


## [2026-09-05T20:55:15.876Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"to hasten\\|to hurry\" CHEUNG.txt | head -20\necho \"=== zwd / zud in Cheung ===\"; grep -n \"zūd\\|zwd’\\|‘quick\" CHEUNG.txt | head -20"
}
```


### [2026-09-05T20:55:15.930Z] TOOL RESULT

```
5309:*SANSKRIT: dhav ‘to walk, to hurry, to flow’ (RV+) = EWAia I: 789 
6415:|| + *pari-) ‘to run around’ || (+ *fra-) ‘to approach, engage’ || (+ *ni-) ‘to hasten’ 
6441:*PARTHIAN: (+ *ni-) nydf’r- ‘to hasten, hurry’ = Ghilain: 74 | DMMPP: 252b 
13079:*SANSKRIT: ramh ‘to hasten’ (RV+) = EWAia II: 421 f., 473 
19886:© This root is connected to Gr. oneÖ8@ ‘I hurry’, Lith. spüdinti ‘to hasten’, etc. by 
23707:*stap ‘to hasten, (op)press’ 
23719:*NWIR: NP sitaftan/sitab- ‘to hurry’ 
24369:tözd ‘to filter’ (not Pash. tajal ‘to hasten’, v. *tauj !) || (+ *apa-) Yzgh. boxtoxs-/ 
24399:*PIE *tek”- ‘to hurry, rush, walk, flow" > LIV: 620 f. | Pok.: 1059 f. 
25218:*NEIR: Oss. I. tynzyn, D. tunzun/tunst ‘to hasten, hurry, press on’. © The stem of the 
25931:*Ouar/tur ‘to hurry, hasten’ 
25936:*MIDDLE PERSIAN: (+ *ni-) BMP nswb'l- /nihar-/ ? ‘to hurry? 
25938:*PARTHIAN: (+ *ni-) nydf’r- ‘to hurry’ = Ghilain: 74 | DMMPP: 252b 
25943:*SOGDIAN: (+ *pati-) MSogd. pöß’yr ‘to hasten’ 
25953:*SANSKRIT: tvar ‘to hurry, hasten’ (KS, Br.+) > EWAia I: 684 f. 
26709:*NEIR: Oss. I. wajyn/wad, D. wajun/wad ‘to hurry, walk, jump’, I. wajyg, D. wajug 
56705:to hasten 
56829:to hurry 
=== zwd / zud in Cheung ===
3577:*NWIR: NP cust ‘quick, brisk, active’ || (+ *?) NP pizohidan/pizoh- ‘to investigate’ 
5316:*IE COGNATES: Gr. 8€ ‘I walk’, 8005 ‘quick’ 
6444:nydf'ryd; Partic.: pres. “nydfwrdg ‘hastening’, perf. pass. nydfwrd ‘quick’, (comp.) “nydfwrdystr 
6445:‘quicker’ 
6823:‘quick, hasty’, etc.), are difficult to assess. Mayrhofer, EWAia П: 195 f., considers 
22016:(Hom.), Lat. celer ‘quick, rapid’. Ф The connection with Germanic (Goth. haldan ‘to 
24364:ppp.) ‘quick’, I. tazyn/tagd, D. tazun/tagd (caus.) ‘to pour in drops, drop’, I. 
29452:Schmidt (Gs Henning: 377 f.) suggests a connection with Lith. skudrus ‘quick’, 
30632:*SOGDIAN: BSogd. zy’rt ‘quick’, BSogd. zy’rtr ‘quicker’, CSogd. Zyrt ‘quickly’, 
30639:‘to wade; to walk; to return’, Pash. zgast- ‘to swim’, Pash. zyard ‘quick, fleet’ || (+
```


## [2026-09-05T20:55:16.706Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SOD page 103 (leaf 169) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==170' SOD_pages.txt | head -40"
}
```


### [2026-09-05T20:55:18.514Z] TOOL RESULT

```
=== SOD page 103 (leaf 169) ===
     pjynd(-)
                                                                                                                        104
           P(9)zya6 ©<*abi-zgad =»Pjyst-, Pzy5-, biyd-
           Go)mount                                                  TSP 2; VJ; BSTBL; Frag. Len.; GMS 138l; MDii;
           GMS 376                                                     S W, TPS 1994, 179
     2624 pJYnd(-) M                          o^JfisJj-
                                                               2637 pnws =» Pn>s
          P(3)zyand ©inf.                                      2638 pn'j- M                                         CMi>J
          mounting, riding                                          P(o)naz ©<*abi-naj- ^n\j-
          GMS 342 n 1; BBB 509                                           you
                                                                    (ro)stumble
     2625 pjyst- M                                   O-^jl^         Hen. Sogdica. 31.3; GMS 877n 1
          P(o)zyast ©pt. St.; inf. -y ->Pjy65-, Pz'yst-        2639 pn's B                                        ^Li^uf
          0<?)mount                                                 fnas (Pn*s) ©<*fra-nasa      =*pn'ys-, fn}s
          BBB 508; GMS 586, 860                                     sin, corruption
     2626 pjn>(h) M                             c^o^                TSP 2.256, 315, 5.34
          f/p(a)zna ? ©<*fra-/abi~ jna ? Av. xsna-, Skt.       2640 pn}w-    S                                      o±jJ
            abhijna =>jn'      r                                    Ponaw, aPnaw (bn}w-) ^pn'w-
          mark, sign
                                                                    Go)trcmble
          Sogdica. 48.1; GMS 264                                    Sund. MSP p43; S W, C2 pl49, 20
     2627 pjng'rystr M              jijj^jt^jijj^^            2641 bn'w- C =» pn'w-
          Pozangarcstar ©pi. -t                               2642 pn'ys- B                   ^/xJaiC^/^j^
          most sinful
                                                                   f(o)nes ©<*fra-ndsaya; OP vi~na0aya-
          GMS 1289; Hen. BSOAS 12, 312.115                           =»fnys-
w   2628 pjng'ryy M                                 j£*y            (^corrupt
         P(o)zangarc (Pjnng'ryy) -^Pjng'ry, bzng'ry                 TSP 2.1115; Frag. 5.7; AVS 227
         sinful
                                                              2643 pnd' M                                         Olxj«x<
          GMS 1126; BBB 662; pi. JSjnnVrt, BBB 520, GMS            Pa/ond -»Pnt\ Pynt-
            48 n 1
    2629 pjnngVyy *» Pjng'ryy                                      GMS 107, 527, 957
                                                                   prison
    2630 pjy- M                        O-^J'jy. to^djjt       2644 pndJ M =» Pnt2
         Pozay ©intrans. v. ^'Pz'w-, Pj}w-, 'Pz'y-            2645 bnd'm C -> pnd>m
         (fo)grow                                             2646 pnd'm M                      oljU* ij£ t*~x
         BBB; GMS 187; W-Lii
                                                                   Pandam (bnd'm) =»mrc Pnd}m, Pnt}m
    2631 pjyk M                                 J&j'JJ*,
```


## [2026-09-05T20:55:25.032Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"abi-z\\|abi-j\\|\\*abi-zau\\|Pz'w\\|βz'w\\|bz'w\" SOD_pages.txt | head -20"
}
```


### [2026-09-05T20:55:25.090Z] TOOL RESULT

```
5440: 583 'JJyz'nkVk B                              X±<J&*jt              (o)Pzaw (*Pz»w-, 'Pz'w) ®*abi-zdwaya-
5442:     evildoer                                                           ©trans. v. =»Pjy-, pz'w-, bz'w-
11273:     place of the gods                                                          P(o)zaw ©<OP abi-jdvaya—, Parth. abgaw-\
11274:     TSP 8.36; BSTBL, Padm. 12, -w, Dhy. 76                                       MP abzay- ©trans, v. ^'Pz'w-, Pjy-
11302:           P(9)zya6 ©<*abi-zgad =»Pjyst-, Pzy5-, biyd-
11335:         Pozay ©intrans. v. ^'Pz'w-, Pj}w-, 'Pz'y-            2645 bnd'm C -> pnd>m
12515:     0o)grow, GcOincrease                                      P(o)zYa5      ©<*abi-zgad   ©impf. tfzYd    =>Pzy5-,
12520:3080 bz'w- C                                o^^JJi
45271:                                 ; abi-zuya-\ MP ^bzw-
```


## [2026-09-05T20:55:30.986Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '11260,11290p' SOD_pages.txt\necho \"=== page tag ===\"; awk 'NR<=11290 && /\\[pdf page/ {p=$0} END{}' SOD_pages.txt; grep -n \"\\[pdf page\" SOD_pages.txt | awk -F: '$1<11290' | tail -3\necho \"=== also 12515 ===\"; sed -n '12505,12530p' SOD_pages.txt"
}
```


### [2026-09-05T20:55:32.571Z] TOOL RESULT

```
      Payyak (Pyy'q) ©*baga-yakd                                           2615 pyyyst'n M => Py'yst'n
      divine                         ►byy'qy'
                                                                           2616 bhl C                                            £L
      BBB b43; GMS 1110, 1499; KG 418, 548, 636;                                pahl, baxl ©OP baxtri
          W-Lii; Frag. Lcn. 34.2                                                 Balkh
                                                                                 STii 1.31
 2604 byy>qy> C                                   ^'J***^*-
      Payyakya ©f. n. ^Pyy'kdi)                                            2617 pj- M                                 (c>)ja(x
      divinity, godhead                                                         Po/e/iz ©nom. ob. fljy(y) =^Pj-, Pyj-, pz-
      C2, 12V17; STii 3.16; GMS 1111                                            bad, pain
                                                                                GMS 179, 379, 570; Talcs. 473.29
2605 pyy'st'n B                     (jLJm- J^)jL-oJ
     ©Payestan =»pY}yst*n                                                  2618 pjJw- M                         jj/jLj(j^>I
     place of the gods                                                          P(o)zaw ©<OP abi-jdvaya—, Parth. abgaw-\
     TSP 8.36; BSTBL, Padm. 12, -w, Dhy. 76                                       MP abzay- ©trans, v. ^'Pz'w-, Pjy-
2606 pyyct      S                                             jLIj^              OcOincrease
                                                                                 GMS 90, 264
       Payist =^PY}yst
                                                                           2619 pj'wq M                               (<Sly>)c^±
        gods
       Afr.Insc. Livsic. AOH 1972, 79 n 8                                       P(o)zuk, P^zuk ©<*fi?zdxuk
                                                                                miserable
2607 pyynwy(y)         M                            (>^/-^)>U
     Paye-nawe         =*Pynwy(y)                                               Hen. Tales. 470.60
     new moon
                                                                           2620 *pj}xw   M                                   w^ju
       Hen. JRAS 1945, Fasts. 146
                                                                                P(o)zaxu ©^flyj+axu     ^bz'xwq
2608 pyyptyc         S ^ Py'ptyc                                                miserable

2609 pyyst'n B                                                                  Gersh. Sogd. Cpds. 1945, 140
=== page tag ===
=== also 12515 ===
                                                          3090 pz'yryn^ *± pz^yr'yn'k
3076 pz'ywty*   S =» bz'xwty*                             3091 Pzy6- B                                       b^Jy
3077 pz'ywty'kh S                         j±yxc^               p(o)zYa5      (P?y5-) ©impf. fi'zVS, pazYad
     P(3)zaxutya ->bz}xwty}, 'Pj'xwty^                           ^Pz^st-, Pjy55-, bzYd-, }nzYSt-
     hardship
                                                               (/<?)mount
      MDii A17R4                                               GMS 619; TSP 9.84, 3.232; VJ 855

3078 pz'w- B                                     o^j\     3092 p?Y6- =» Pzy§-
     p(o)zaw (pz'w-) =>Pzwt-, 'pz'w-, pj>w-               3093 bzYd-      C                                  uJiji>-
     0o)grow, GcOincrease                                      P(o)zYa5      ©<*abi-zgad   ©impf. tfzYd    =>Pzy5-,
     BSTBL, Vim. 93
                                                                        t
3079 pzV- => pz>w~                                             (rc)moun
                                                               C2, 77R5; AVS 114
3080 bz'w- C                                o^^JJi
     P(o)zaw =>pj>w-, 'pz'w-, Pz}w-                       3094 pzn^my       B                    (pXW-YJ/)*^
     (ro)increase                                                      5
                                                                    PjY ?5 -
                                                               Pazm5ane
     BSTii 873.16; C2, 66R16                                   stomach, bladder
                                                               TSP 7.57; Benv. n p211; Bailey. Prolexis. 248
3081 bz'xwq C                             jlujjj<couju
     P(o)zaxuk (PzYwkw) =*PzYwk                           3095 pzn- B, M                                     f>
     suffering, painful                                        pazn ©ace. -w =»nwpznyy
     C2 gloss.; STSC 13430; MD                                 shame
```


## [2026-09-05T20:55:39.727Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"pdf page\" SOD_pages.txt | awk -F: '$1>11100 && $1<11400'\necho \"---\"; grep -n \"pdf page\" SOD_pages.txt | head -3"
}
```


### [2026-09-05T20:55:41.481Z] TOOL RESULT

```
---
```


## [2026-09-05T20:55:45.057Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'NR<=11273 {n+=gsub(/\\f/,\"\")} END {print \"formfeeds before line 11273:\", n}' SOD_pages.txt\nawk 'NR<=12518 {n+=gsub(/\\f/,\"\")} END {print \"formfeeds before 12518:\", n}' SOD_pages.txt"
}
```


### [2026-09-05T20:55:46.594Z] TOOL RESULT

```
formfeeds before line 11273: 168
formfeeds before 12518: 186
```


## [2026-09-05T20:55:53.157Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== TAD kub ===\"; grep -n \"كوب\\|أكواب\\|الكوب\" TAD_pages.txt | head -10\necho \"=== TAD sanj ===\"; grep -n \"صنج\\|الصنج\\|سنج\" TAD_pages.txt | head -10\necho \"=== TAD page 44 approx: leaves ===\"; grep -c $'\\f' TAD_pages.txt"
}
```


### [2026-09-05T20:55:54.900Z] TOOL RESULT

```
=== TAD kub ===
838:                                  ‫جام‪ -‬فارسي « جام » وهو الكوب‬
1955:                    ‫فرماسول _ افر نسى كوب مع عنم معنأه البسائون الاحرار‬
=== TAD sanj ===
1452:                           ‫سئحة ‏ فارسي « سنجه ‪ 4‬معناه عبار المعزان‬
1454:‫منجاب ‪ -‬في الفارسية _سنجاب وفي اليونانية ‪507‬ناهأ!ة وتميه العامة‬
1456: ‫منجق ‪ -‬فالينارسية سنجاق وافليتركية سنجاق وفي اليوثانية ‪0016765‬‬
1707: ‫‪.‬لظاهر أن افظ صنج ج صنو ج هو حربف‬
1708:                                 ‫أماه سنج » الفارسي شعناه الوازن ا‬
=== TAD page 44 approx: leaves ===
85
```


## [2026-09-05T20:56:02.676Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'NR<=1707 {n+=gsub(/\\f/,\"\")} END {print \"leaf(0-based ff count):\", n}' TAD_pages.txt\nsed -n '1695,1720p' TAD_pages.txt\necho \"=== jam line 838 leaf ===\"; awk 'NR<=838 {n+=gsub(/\\f/,\"\")} END {print n}' TAD_pages.txt"
}
```


### [2026-09-05T20:56:04.408Z] TOOL RESULT

```
leaf(0-based ff count): 47
 ‫نمك ‪ -‬انكليزي عله مشتق من ‪ 01 16611‬أي حقدق ومنه الافر نسي‬
‫‪#‬ناوغدء أي الموالة الماليةومنهممنعربهشلك أوشاك ونقلمنالافرنسيةالى‬
                                                ‫التركية “جك ممعنى الكوالة‬
 ‫صلاطة ا‪-‬يطالي ‪80‬هادوه‪ :‬معناه مُملحة ومادتها أحرار البقول تؤكل‬
                                                              ‫يل وزيت‬
                                               ‫صلجة ‪ -‬راجعشرنقة‬
  ‫صلصا ايطالى ‪251‬ه‪ 5‬وهو الب" يٌصنممنالتوابل والابازير ودقاق السمك‬
                                                              ‫والبندورة‬
                                              ‫فارركارانن ‪75‬‬
                          ‫خردل بوناني أم‪60‬ز‪ 5‬معناه خردل‬       ‫صِئاب‬

 ‫لاتيني سالدفسك أصله وثاني ‪:‬ده‪120‬ه)! معناه جوف فى وسلله‬         ‫صل‬
 ‫‪.‬لظاهر أن افظ صنج ج صنو ج هو حربف‬
                                 ‫أماه سنج » الفارسي شعناه الوازن ا‬
   ‫المعويري أي صنواج وهو مشتق منصلصل العربى أي صوات‬           ‫لقي‬
 ‫معئاه شبال ولي الارابية سف معئأة‬                 ‫صدم ‪0‬‬
                                       ‫مثالوفي كلتااللغتينبراد به الوآن‬
  ‫ل‬                                                          ‫'‬

 ‫اقر‪-‬سى « جوب وحوبه » معناه عصا رقق‬
                                  ‫فوي‬
                                    ‫فو بسوشوبك وش‬
                         ‫بهاالعجين مرأدفه مسطح وملطاط ومطلة وسور‬
       ‫‪1‬‬     ‫‪2‬‬                    ‫‪78‬‬                         ‫‪5‬‬              ‫‪0‬‬
‫أي فرخ مشتق من د صوصي » الارامي اي صاى الفرخ‬                     ‫منّوص ‪-‬‬
                                                         ‫‪2‬‬
=== jam line 838 leaf ===
24
```


## [2026-09-05T20:56:23.175Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PLA sanj/kub ===\"; grep -n \"صنج\\|كوب\\|ṣanǧ\\|sang\\|Zimbel\" incoming/PLA/PLA_pages.txt | head -20\necho \"=== AFM sanj ===\"; grep -n \"صنج\\|الصنج\" AFM_pages.txt | head -10\necho \"=== FVQ akwab ===\"; grep -n -i \"akwab\\|akwāb\\|kūb\\|kub'\" FVQ_pages.txt | head -10"
}
```


### [2026-09-05T20:56:23.263Z] TOOL RESULT

```
=== PLA sanj/kub ===
2065:AR        -    ’awäz:           "eine       bestimmte           Melodie,              Gesang"             pers.         2 aus    dem    pers. .)>7
2423:O;L-       bäzan:       "Fels"            pers.                     wahrscheinlich          aus     dem    pers.   AL           pärsang
2424:                mp. Ju pärag                   "Stück,               Bruch"     +-era sang         "Stein".
2762:                    mp rgado) parsang.                                                                               z
2763:      Es ist            eine         Nebenform             v.      a      farsah pers.                           iu;        farsang           2,
6075:            bana’:          "Ton,      Gesang" "        pers,      10 ‚   aus    pers.       Bm
6970:ls»             - darwasang:                 "            m ohne
8815:de     - safil:             "harte        Backsteine"                    aus       pers.         Ya.    sang-gil            1 mp.      >     sang
8816:        <T aw.              asanga,           asan        2, ap.            asan         °, Sail mp.                    d gil 4,
8827:        sangidan              "wiegen"             mp.            eu»         sahtan           9
9265:        aus      pers...                        sangsabü.
9435: ge          and:     "Gleichgewicht"                     pers.             8 mp.              „w    sang     v.       Verb    2,»    saxtan    2,
9453:sangäbi                                                                        167                                                        sandrüs
9456:les» -                sanbäbi:            Nisba        v. u... sangäab "grau".
9459:Vom _                  sanfbüya:            "Steinkrug"                  aus    pers. sul,                     sangsabüye          1, S.o..l
9470:„Dam              sangafar = singarf                         q. v.        5,
9474:buosi»-               sangalät:            "eine wohlriechende                            Blume"        pers.        7,
9476:am          -     angalat             = sangalät               q.    v.
9518:          stickt,           od.       na             sangduz          "mit        Edelsteinen             bestickt".
9530:zus - sanksar:                        "Martyrologium'"                     (svrafa 9 lov)             io        pers._Li,        sangsär
=== AFM sanj ===
=== FVQ akwab ===
```


## [2026-09-05T20:56:30.547Z] TOOL CALL #33: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-05T20:56:30.554Z] TOOL RESULT

```


```


## [2026-09-05T20:56:34.519Z] TOOL CALL #34: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%DA%A9%D9%88%D9%87",
 "prompt": "Give the Persian etymology section for کوه (kuh) verbatim: Middle Persian, Old Persian, Avestan, Proto-Iranian and PIE forms cited. Also any mention of کوهان/کوهه."
}
```


## [2026-09-05T20:56:35.841Z] TOOL CALL #35: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AE%D9%85",
 "prompt": "Give the Persian etymology for خم (xom) 'jar': Middle Persian, Avestan xumba-, Sanskrit kumbha-, Proto-Indo-Iranian/PIE forms. Verbatim if possible."
}
```


### [2026-09-05T20:56:39.255Z] TOOL RESULT

```
# Persian Etymology for کوه

Based on the Wiktionary entry, here is the etymological progression:

The word کوه descends from **Middle Persian** _𐭪𐭥𐭯_ (kōf, "hill, mountain"), which came from **Old Persian** _𐎣𐎢𐎳_ (kaufa, "mountain"). These trace back to **Proto-Iranian** _*káwfš_, ultimately deriving from **Proto-Indo-European** _*kewHp-_ meaning "heap; to heap."

The entry contains no references to کوهان or کوهه, nor does it mention Avestan forms in the etymology section provided.
```


### [2026-09-05T20:56:41.142Z] TOOL RESULT

```
Based on the Wiktionary article provided, here is the Persian etymology for خم (xom) 'jar':

The article states that خم (xom) derives "From Classical Persian خنب (xunb), خمب (xomb), from Middle Persian [Book Pahlavi needed] (hwmb'), 𐫟𐫇𐫖𐫁 (xwmb /xumb/, 'jug, pitcher')."

Unfortunately, the document does not provide etymologies extending to Avestan, Sanskrit, or Proto-Indo-Iranian/PIE forms. The etymology is traced only back to Middle Persian, with no further ancestral connections documented in this source.
```


## [2026-09-05T20:56:45.612Z] TOOL CALL #36: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B2%D9%88%D8%B1",
 "prompt": "Give the Persian etymology of زور (zur) 'force, power': Middle Persian, Avestan zāvar-, Proto-Iranian and PIE root cited. Verbatim."
}
```


## [2026-09-05T20:56:47.383Z] TOOL CALL #37: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A7%D9%81%D8%B2%D9%88%D8%AF%D9%86",
 "prompt": "Give the Persian etymology of افزودن (afzudan) 'to increase': Middle Persian abzūdan, Old Persian/Avestan prefixed forms, Proto-Iranian and PIE root. Verbatim."
}
```


### [2026-09-05T20:56:51.689Z] TOOL RESULT

```
# Persian Etymology of زور (zur) 'force, power'

Based on the Wiktionary entry, here's the documented etymological path:

**Etymology 1** traces the word to: "Inherited from Middle Persian [script needed] (zwl /⁠zōr⁠/), which Pokorny derives from Proto-Indo-European *gew- ("to hasten")..."

The entry does not cite Avestan forms. Instead, it provides comparisons to related languages like Serbo-Croatian žúriti ("to hurry") and Old Norse keyra ("to whip").

**Etymology 5** offers an alternative origin: "Borrowed from Middle Persian [script needed] (zwl /⁠zōr⁠/)," also without specifying an Avestan connection or Proto-Iranian intermediate forms.

The document does not explicitly mention Avestan zāvar- or a specific Proto-Iranian reconstruction, contrary to your request.
```


### [2026-09-05T20:56:53.415Z] TOOL RESULT

```
# Persian Etymology of افزودن (afzudan)

According to the Wiktionary entry, the word derives as follows:

From Early New Persian *اڤزودن* (aḇzūdan), inherited from Middle Persian *abzūdan*, which comes from Proto-Iranian *\*Habigaw-* ("to increase"). 

The prefix originates in Proto-Indo-Iranian *\*Habʰí* ("to, against, for"), while "the root is of unclear origin, and possibly related to Lithuanian *gáuti* ('to obtain')."

The etymological path demonstrates how this Persian verb developed through multiple historical language stages, with the root's ultimate Indo-European connections remaining somewhat uncertain despite the Lithuanian cognate suggestion.
```


## [2026-09-05T20:57:06.777Z] TOOL CALL #38: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B2%D9%88%D8%AF",
 "prompt": "Persian زود (zud) 'quick, soon': give the etymology verbatim — Middle Persian, Proto-Iranian, PIE root, Avestan comparanda."
}
```


## [2026-09-05T20:57:08.184Z] TOOL CALL #39: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A7%D9%81%D8%B2%D8%A7%D8%B1",
 "prompt": "Persian افزار (afzār) 'tool, instrument': give the etymology verbatim — Middle Persian abzār, Old Persian/Proto-Iranian reconstruction, and any mention of ابزار."
}
```


### [2026-09-05T20:57:12.516Z] TOOL RESULT

```
# Etymology of Persian زود (zud)

Based on the Wiktionary entry, the Persian word **زود (zud)** meaning "quick, soon" derives from:

**Proto-Indo-Iranian origin** with cognates including Sanskrit _जू_ (jū, "hurry on, be quick") and Avestan _𐬰𐬆𐬬𐬍𐬱𐬙𐬫𐬀_ (zəvīštya, "the quickest").

The entry suggests a further **Proto-Indo-European root** _*ǵewH-_ meaning "force, drive," which connects it to Proto-Slavic _*žuriti_ ("to rage") and Old Norse _keyra_ ("drive").

The word is also related to Northern Kurdish _zû_ and Northern Luri _زی_ (zi), reflecting a broader Iranian language family pattern for this semantic concept.
```


### [2026-09-05T20:57:13.100Z] TOOL RESULT

```
# Etymology of Persian افزار (afzār)

According to the Wiktionary entry, this term is "Inherited from Middle Persian [Book Pahlavi needed] (ʾp̄cʾl, ʾp̄zʾl /⁠abzār⁠/, 'instrument, means; spice')."

The entry notes it is a "Doublet of ابزار (abzâr, 'tool, instrument, means')" in Persian, indicating both words share the same etymological root but developed differently over time.

The word has cognates in related languages, including Parthian forms meaning "materials, means" and "spice-related" items, reflecting its proto-Iranian heritage.
```


## [2026-09-05T20:57:18.887Z] TOOL CALL #40: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%83%D9%88%D8%A8",
 "prompt": "Arabic كوب (kūb) 'cup': give the etymology verbatim — is it a loan from Greek, Aramaic, Latin or Persian? Plural أكواب? Any Qur'anic citation?"
}
```


## [2026-09-05T20:57:20.126Z] TOOL CALL #41: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/cup",
 "prompt": "Give verbatim the etymology of 'cup' (Old English cuppe, Late Latin cuppa, Latin cupa, PIE root). Also any note on cognates."
}
```


### [2026-09-05T20:57:24.463Z] TOOL RESULT

```
# Etymology of كوب (kūb)

The word is borrowed through a chain of languages: **Aramaic כובא (kūbā)** → **Byzantine Greek κοῦπα (koûpa)** → **Latin cuppa**, ultimately from **Latin cūpa**.

**Plural:** أكواب (ʔakwāb)

**Qur'anic citation:** The word appears in Surah 56, verses 17-18 (609–632 CE): "There will circulate among them young boys made eternal, with beakers, pitchers and a glass of spring water."
```


### [2026-09-05T20:57:28.242Z] TOOL RESULT

```
# Etymology of Cup

**Word Path:** Old English *cuppe* → Old Northumbrian *copp* → Late Latin *cuppa* → Latin *cupa*

**Latin Root:** Latin *cupa* means "tub, cask, tun, barrel."

**Cognates:** The word is thought cognate with Sanskrit *kupah* ("hollow, pit, cave"), Greek *kype* ("gap, hole; a kind of ship"), Old Church Slavonic *kupu*, Lithuanian *kaupas* ("heap"), Old Norse *hufr* ("ship's hull"), and Old English *hyf* ("beehive").

**PIE Origin:** According to the source, De Vaan proposes that "all probably are from a non-IE loanword *\*kup-* which was borrowed by and from many languages." This suggests the ultimate root may not be Indo-European but rather a word borrowed across multiple language families.

**Germanic Spread:** The Late Latin term dispersed throughout Germanic languages: Old Frisian *kopp*, Middle Low German *kopp*, Middle Dutch *coppe*, and Dutch *kopje*.
```


## [2026-09-05T20:57:35.892Z] TOOL CALL #42: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B5%D9%86%D8%AC",
 "prompt": "Arabic صنج (ṣanj) 'cymbal': give the etymology verbatim — borrowed from Persian? Middle Persian? Any mention of سنج or چنگ?"
}
```


## [2026-09-05T20:57:36.599Z] TOOL CALL #43: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/hump",
 "prompt": "Give the etymology of 'hump' verbatim — Dutch/Low German source, date of first attestation, PIE root proposed."
}
```


### [2026-09-05T20:57:40.852Z] TOOL RESULT

```
# Etymology of Arabic صنج (ṣanj)

According to the Wiktionary entry, the word comes from **Middle Persian** (transliterated as čang, meaning "harp"), and **Modern Persian چنگ** (čang, "harp").

The entry states: "From Middle Persian [script needed] (čang, 'harp'), Modern Persian چنگ (čang, 'harp')..."

The document also mentions that Arabic later borrowed related forms again: جَنْك (jank) and جُنْك (junk), both meaning "harp," which derive from the same Persian source.

So the etymology traces: **Middle Persian čang → Persian چنگ → Arabic صنج (ṣanj)**, with the primary meaning shifting from "harp" (obsolete in Arabic) to its current meaning of "cymbal."
```


### [2026-09-05T20:57:41.577Z] TOOL RESULT

```
# Etymology of "Hump"

**Dutch/Low German Source:**
"perhaps from Dutch _homp_ 'lump,' from Middle Low German _hump_ 'bump'"

**Date of First Attestation:**
The noun form appears in the 1680s, specifically noted in the compound "_hump-backed_"

**PIE Root Proposed:**
The source traces it back to Proto-Germanic *hump-, deriving ultimately from the PIE root *kemb-, meaning "to bend, turn, change, exchange"
```


## [2026-09-05T20:57:51.487Z] TOOL CALL #44: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/cymbal",
 "prompt": "Etymology of 'cymbal' verbatim: Old English/Old French, Latin cymbalum, Greek kymbalon, kymbe. Dates."
}
```


## [2026-09-05T20:57:52.363Z] TOOL CALL #45: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/heap",
 "prompt": "Etymology of 'heap' verbatim: Old English heap, Proto-Germanic *haupaz, PIE root. Also any mention of high/hip."
}
```


### [2026-09-05T20:57:57.314Z] TOOL RESULT

```
# Etymology of "Cymbal"

The word "cymbal" originates from mid-15c. English, derived from "one of a pair of plates of brass or bronze which, when struck together, produce a sharp, ringing sound."

**Language Lineage:**
- **Old English & Old French**: _cimbal_ and _cymbale_
- **Latin**: _cymbalum_
- **Greek**: _kymbalon_, from _kymbē_ meaning "bowl, drinking cup"

**Possible Cognates:**
The term may connect to Sanskrit _kumbha-_, Avestan _xumba-_, and Middle Irish _comm, cummal_—all referring to vessels or pots. However, etymologist Beekes notes this is likely a "Wanderwort" (wandering word) that traveled across cultures rather than being inherited through standard linguistic descent, which fits its status as a vessel-related term.

The musical instrument retained its original meaning, while the related word "chime" evolved differently, eventually referring to sets of bells.
```


### [2026-09-05T20:57:59.098Z] TOOL RESULT

```
# Etymology of "Heap"

The word "heap" has West Germanic origins. According to etymonline, it comes from Old English *heap* meaning "pile (of things); great number, crowd," derived from West Germanic *haupaz*.

The OED suggests a possible connection to Old English *heah* ("high"), though the exact origin remains uncertain. Some scholars propose a link to Latin *cubare* ("lie down"), while others argue it may not be Indo-European at all.

**Key linguistic relatives:**
- Old Saxon *hop*
- Dutch *hoop*
- German *Haufe*

The verb form *heapian* ("collect, heap up") follows the standard Germanic pattern of verbs derived from nouns, similar to Old High German *houfon*.

In modern English, the slang meaning "old car" emerged around 1924, while the phrase "a lot, a great deal" became characteristic of American Indian English by 1832.
```


## [2026-09-05T20:58:05.747Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '618,630p' AHD_watkins1985.txt"
}
```


### [2026-09-05T20:58:05.790Z] TOOL RESULT

```
ker-1. Horn, head; with derivatives referring to horned animals, horn-shaped objects, and projecting parts. I. Zero-grade form *kr-. 1. Suffixed form *kr-n- in: a. Ger- manic *Aurnaz in (i) Old English horn, horn: HORN, (HORNBEAM) (ii) German Horn, horn: ALPENHORN, ALT- HORN, FLUGELHORN, HORNBLENDE; Db. Latin cornd, horn: CORN2, CORNEA, CORNEOUS, CORNER, CORNET, CORNICULATE, CORNU; BICORN, CADUCICORN, CAPRI- CORN, CLAVICORN, CORNIFICATION, LAMELLICORN, LON- GICORN, TRICORN, UNICORN. 2. Suffixed and extended form *krs-n- in Germanic *hurznuta in Old English hyrnet, hornet: HORNET. 3. Suffixed form *kr-ei- in: a. Germanic *hraina- in Old Norse hreinn, reindeer: REINDEER; b. Germanic *hrinda- in Old High German hrind, ox (> German Rinder, cattle): RINDERPEST. 4. Suffixed extended form *kros-no- in Greek kranion, skull, upper part of the head: CRANIUM; MIGRAINE, OLECRANON. 5. Suffixed form *kr-a- in: a. Greek karé, kara, head: CHARIVARI; CHEER; b. Greek karoun, to stupefy, be stupefied (< “to feel heavy-headed”): ca- ROTID; c. Greek kardton, carrot (from its hornlike shape): CARROT. 6. Possibly extended form *kri- in Greek krios, ram: CRIOSPHINX. II. Suffixed form *ker-wo-. 1. Latin cervus, deer: CERVINE, SERVAL. 2. Latin cervix, neck: CERVIX. III. Extended and suffixed form *keru-do- in Germanic *herutaz in: a. Old English heorot, hart, stag: HART; b. Dutch hart, deer, hart: HARTEBEEST. IV. Extended form *keras-. 1. Greek keras, horn: CARAT, CERASTES, KERATO-; CERATODUS, (CERATOID), CHELIC- ERA, CLADOCERAN, KERATIN, RHINOCEROS, TRICERA- Tops. 2. Persian sar, head: SIRDAR. 3. Suffixed form *keras-ro- in Latin cerebrum, brain: CEREBELLUM, CERE- BRUM, SAVELOY. V. Extended o-grade form *koru-. 1. Greek Rorumbos, uppermost point (< “head”): CoR- yMB. 2. Greek koruphé, head: CORYPHAEUS. 3. Suffixed form *koru-do- in Greek korudos, crested lark: coRY- DALIS. 4. Suffixed form *koru-ndé in Greek koruné, club, mace: CORYNEBACTERIUM. [Pok. 1. ker- 574.]
ker-2, Echoic root, base of various derivatives indicating loud noises or birds. I. Zero-grade form *kr-, becoming Germanic *hr-. 1. Germanic *hring- in Old English hringan, to resound, clink: RING. 2. Germanic *hraik- in Old English hré&can, to clear the throat: RETCH. 3. Ger- manic *hrdkaz, “croaking bird,” crow, in Old English
ker-*
hréc, rook: RooK!. 4. Germanic *hraban, *hrabnaz, raven, in Old English hrefn, raven: RAVEN}. 5. Extended form *krep- in Latin crepdre, to crack, burst, creak: CREPITATE, CREVICE; DECREPIT, DECREPITATE, QUEBRA- cHo. 6. Extended form *kri- in Germanic *krik- in Old French criquer, to creak, click: CRICKET!. II. Variant form *skr-. 1.Germanic *skrik- in Old English scric, thrush: SHRIKE. 2. Germanic *skrékjan- in Old Norse skrekja, to shriek: SCREAK, SCREECH. 3. Germanic *skrainjan, to shout, shriek, in Old Norse screma, to scream, perhaps akin to the possible Scandinavian source of Middle English scremen, to scream: SCREAM. III. O-grade form *kor-. 1. Latin corvus, raven: CORBEL, CORBINA, CORMORANT, CORVINE, Corvus. 2. Greek ko- rax, raven (> korakias, chough): CORACIIFORM, CORA- com. [Pok. 1. ker- 567.] ker-3. To grow. 1. Suffixed form *ker-es- in Latin Cerés, goddess of agriculture, especially the growth of grain: CEREAL, CERES. 2. Extended form *kré- (< *krea-) in: a. suffixed form *kré-yd- in Latin credre, to bring forth, create, produce (< “to cause to grow”): CREATE, CREOLE; PROCREATE; b. suffixed form *kré-sko- in Latin créscere, to grow, increase: CRESCENDO, CRESCENT, CREW!; AC- CRUE, CONCRESCENCE, CONCRETE, DECREASE, EXCRES- CENCE, INCREASE, RECRUIT. 3. Suffixed o-grade form *kor-wo-, “growing,” adolescent, in Greek kouros, koros, boy, son: DIOSCURI, HYPOCORISM. 4. Compound *sm-kéro-, “of one growth” (*sm-, same, one; see sem-'), in Latin sincérus, pure, clean: SINCERE. [Pok. 2. ker- 577.) ker-4, Heat, fire. 1. Suffixed form *ker-té in Germanic *herthé in Old English heorth, hearth: HEARTH. 2. Zero-grade form *kr- in: a. Latin carbé, charcoal, ember: CARBON, CARBUNCLE; b. extended form *krem- in Latin cremdre, to burn: CREMATE. 3. Possibly suffixed and extended form *kera-mo- in Greek keramos, potter’s clay, earthenware: CERAMIC. 4. Possibly variant ex- tended form *krds- in Russian krasa, beauty (< “bril- liance of fire”): CRASH?. [Pok. 3. ker(a)- 571.] ker-5. Also kere-. To injure. Suffixed zero-grade form *kro-yé- in Latin cariés, decay, caries: CARIES. [Pok. 4. her- 578.] ker-8. A kind of cherry. 1. Suffixed zero-grade form *kr-no- in Latin cornus, cornel tree: CORNEL. 2. Full- grade form *ker- probably in Greek kerasos, cherry: CHERRY. [Pok. 4. ker- 572.] kerd-', Heart. 1. Suffixed form *kerd-en- in Germanic *hertén- in Old English heorte, heart: HEART. 2. Zero-grade form *krd- in: a. Latin cor (stem cord-), heart: CORDATE, CORDIAL, COURAGE, QUARRY!; ACCORD, CONCORD, CORDIFORM, DISCORD, MISERICORD, RECORD; b. suffixed form *krd-yd- in Greek kardia, heart, stom- ach, orifice: CARDIA, CARDIAC, CARDIO-; DIPLOCARDIAC, ENDOCARDIUM, EPICARDIUM, MEGALOCARDIA, MYOCAR- DIUM, PERICARDIUM. 3. Possibly *kred-dha-, “‘to place trust” (an old religious term; *dho-, to do, place; see dhé-'), in Latin crédere, to believe: CREDENCE, CREDI- BLE, CREDIT, CREDO, CREDULOUS, GRANT; MISCREANT, RECREANT. [Pok. kered- 579.] kerd-2. Craft. Suffixed form *kerd-d in Old Irish cerd, art, artist: CAIRD. [Pok. 2. kerd- 579.] kerdh-. Row, herd. Suffixed form *kerdh-d@ in Germanic *herdo in Old English heord, herd: HERD. [Pok. kerdho- 579.] kere-. To mix, confuse, cook. 1. Variant form *kra- (< *kraa-) in Germanic *hrdr- in: a. possibly Old English hrér, lightly boiled, half-cooked: RARE?; b. Middle Dutch roer, motion: UPROAR. 2. Zero-grade form “krp- in: a. suffixed form *kro-ti- in Greek krasis, a mixing: IDIOSYNCRACY; b. suffixed form *kro-ter- in Greek kra- ter, mixing vessel: CRATER. [Pok. hero- 582.] kerp-. To gather, pluck, harvest. Variant karp-. 1. Ger- manic *harbistaz in Old English herfest, harvest: HAR- VEST. 2. Latin carpere, to pluck: CARPET; EXCERPT,
keu-?
(SCARCE). 3. Greek karpos, fruit: -cARP, CARPEL, CARPO-, -CARPOUS. [In Pok. 4. sker- 938.] kers-'. Dark, dirty. 1. Suffixed form *ker(s)-no- in Rus- sian chérnyi (feminine chérnaya), black: CHERNOZEM. 2. Suffixed zero-grade form *krs-no- in Sanskrit krsna-), black, dark: KrisHNa. [Pok. kers- 583.] kers-2. To run. Zero-grade form *krs-. 1. Latin currere (past participle cursus), to run: CORRIDOR, (CORSAIR), COURANTE, COURIER, COURSE, CURRENT, CURSIVE, CUR- SOR, CURULE; CONCOURSE, CONCUR, DECURRENT, DIS- COURSE, EXCURSION, HUSSAR, INCUR, INTERCOURSE, OCCUR, PERCURRENT, PRECURSOR, RECOURSE, RECUR, succor. 2. Suffixed form *krs-o- in Gaulish carros, a wagon, cart, in: a. Latin carrus, a two-wheeled wagon: CAR, CAREER, CARGO, CARICATURE, CARIOLE, CAROCHE, (CARRY), CHARGE, CHARIOT; b. Latin carpentum, a two- wheeled carriage: CARPENTER. [Pok. 2. fers- 583.] kert-. To turn, entwine. I. Zero-grade form *krt-. 1. Suf- fixed form *krt-i- in Germanic *hurdiz, wickerwork frame, hurdle, in: a. Old English hyrdel, hurdle, frame: HURDLE; b. Old French hourd, fence, hurdle, scaffold: HOARDING. 2. Suffixed form “*krt-sti- in Germanic *hur- sti- in Old High German hurst, thicket: Horst. II. Per- haps suffixed variant form *krot-i- in Latin crdatis, wickerwork hurdle: CRATE, GRATE?, (GRID), GRIDDLE; (GRIDIRON). [Pok. kert- 584.] kes-'. To scratch. 1. Germanic *hezd6 in Old English heordan, coarse parts of flax: HARDS. 2. Extended form *kseu- in Greek xuein, to scrape: XYSTER. 3. Nasalized form *ks-n-eu- in: a. Germanic *snaww- in Old Norse snéggr, “close-cropped,” perhaps akin to the source of snuG!: b. Latin novdcula, razor: NOVACULITE. [Pok. kes- 585.] kes-2. To cut. Variant kas-. 1. Suffixed form *kas-tro- in: a. Latin castrare, to castrate: CASTRATE; b. Latin cas- trum, fortified place, camp (perhaps “separated place”): CASTLE. 2. Suffixed form *kas-to- in Latin castus, chaste, pure (< “cut off from, free of, faults”): CASTE, CHASTE; CASTIGATE, INCEST. 3. Suffixed (stative) form *kas-é- in Latin carére, “to be cut off from,” lack: CARET. 4. Ex- tended geminated form *kasso- in Latin cassus, empty, void: (CASHIER), QUASH. [Pok. hes- 586.] kes-°. To order. Suffixed 0-grade form *kos-mo- in Greek kosmos, order: COSMOS; MACROCOSM, MICROCOSM. keu-' Also ekeu-. To perceive, see, hear. O-grade form *akou-. 1. Extended form *kous- in: a. Germanic *haus- Jan in (i) Old English hieran, to hear: HEAR (ii) Old English he(o)rcnian, to harken: HEARKEN; b. suffixed form *9-kous-yo- in Greek akouein, to hear: ACOUSTIC. 2. Variant *skou- in: a. Germanic *skauwon in (i) Old English scéawian, to look at: SHOW (ii) Flemish scauwen, to look at: SCAVENGER; b. Germanic *skaunjaz in Mid- dle Dutch schoon, beautiful, bright (< “conspicuous, attractive”): SCONE; Cc. Germanic *skauniz in Old Eng- lish sciene, bright, sheen: SHEEN. [Pok. 1. keu- 587.] keu-?. Base of various loosely related derivatives with assumed basic meaning “to bend,” whence “a round or hollow object.” I. Extended forms *keub-, *keup-. 1. Ger- manic *haup- in: a. Old English héap, heap: HEAP; b. Dutch hoop, heap, troop: FORLORN HOPE. 2. Germanic *hupp-, to leap (by first bending the legs), in Old English hoppian, to hop: HoP!. 3. Germanic *Aupiz in Old Eng- lish hype, hip: H1P!. 4. Zero-grade form *kup-, vessel, in: a. suffixed form *kup-s- in Greek kupselé, chest, hollow vessel: CYPSELA; b. long-vowel form *kip- in (i) Ger- manic *Aifi- in Old English hyf, hive: HIVE (ii) suffixed form *kip-a in Latin cupa, tub, vat: CUPOLA, CUPULE; c. expressive form *kupp- in Late Latin cuppa, drinking vessel: cup. 5. Zero-grade form *kub- in: a. Greek kubos, cube: CUBE; b. suffixed form *kub-@- in (i) Latin cubdre, to lie down on (< “to bend down, prostrate”): COUVADE, COVEY, CUBICLE; CONCUBINE, INCUBATE, SUCCUBUS (ii) Latin cubitum, elbow: CUBIT; Cc. nasalized form *ku-m-b- in (i) Latin -cumbere, to lie down, recline: ACCUMBENT,
kéu- 31
DECUMBENT, INCUMBENT, PROCUMBENT, RECUMBENT, SUCCUMB (ii) Greek kumbé, boat, bowl: (CEMBALO), (CHIME!), CYMBAL, CYMBIDIUM; d. aspirated long-vowel form *kiibh- in Greek Ruphos, bent: KYPHOSIS. II. Ex- tended o-grade form *kouk-. 1. Suffixed form *kouk-o- in: a. Germanic *hauhaz, “arched,” high, in Old English héah, high: HIGH; b. Germanic *hauhitho in Old English héhthu, héahthu, height: HEIGHT. 2. Germanic *huk- in: a. Middle Low German héken, to bend, squat, bear on the back, peddle: HAWKER; b. Old Norse hokra, to crouch, akin to the Scandinavian source of HUNKER; c. Middle Dutch hokester, “one who squats,” peddler, perhaps akin to the source of Middle English hukster, peddler: HUCKSTER. III. Reduplicated form *ka-ku-bh- in Latin caciimen, summit, point (< “arch, vault’): CACUMINAL. [Pok. 2. keu- 588.]
kéu-. To burn, Zero-grade form *kau- becoming *kaw- in suffixed form *kaw-yo- in Greek kaiein, to burn: CALM, CAUSTIC, CAUTERY; ENCAUSTIC, HOLOCAUST, (INK). [Pok. 2, kéu- 595.]
keub-. Thorn. Germanic *heup- in Old English héope, brier, seed vessel of the wild rose: HIP’. [Pok. keub- 595.] keue-!. To pay attention, perceive (preternaturally). 1. Suffixed o-grade form *kous-o- becoming *kaw- in denominative (stative) Latin cavére, to beware, watch, guard against: CAUTION, CAVEAT; PRECAUTION. 2. Suf- fixed zero-grade form *ki-dos (< *kua-dos) in Greek kudos, magical glory: kuDos. [In Pok. 1. keu- 587.] keue-2. To swell; vault, hole. I. O-grade form *kouo-. 1. Basic form *kous- becoming *kaw- in Latin cavus, hollow, and cavea, a hollow: CAGE, CAVE, CAVERN, CA- VETTO, GABION, JAIL; CONCAVE, DECOY, EXCAVATE. 2. Suffixed form *kow-ilo- in Greek koilos, hollow: (-CELE2), -CELIAC, -COEL, COELOM. 3. Suffixed lengthened-grade form *kéw-o- in Greek kdos, hollow place, cavity (> kddeia, poppy head): CODEINE. II. Zero-grade form *ki- (< *kua-). 1. Suffixed shortened form *ku-m-olo- in Latin cumulus, heap, mass: CUMU- LATE, CUMULUS; ACCUMULATE. 2. Basic form *kd- in: a. suffixed form *ki-ro-, “swollen,” strong, powerful, in Greek kurios (vocative kurie), master, lord: CHURCH, (KIRK), KYRIE; b. suffixed form *kuw-eyo- in Greek kuein, to swell, and derivative kiima (< *ki-mn), “a swelling,” wave: CYMA. [Pok. 1. feu- 592.]
keuk-. To be white, be bright, shine. Suffixed zero-grade form *kuk-no- in Greek kuknos, swan: CYGNET, CYGNUS. [Pok. keuk- 597.]
kéwero-. North, north wind. 1. Germanic *skiira- in Old English scir, shower, storm: SHOWER}. 2. Germanic *skiré in Old Norse skiar, a shower, akin to the probable Scandinavian source of Middle English scouren, to range over: scour?, [Pok. kéuero- 597.]
kigh-. Fast, violent. Germanic *hig- in Old English higian, to strive, exert oneself: HIE. [Pok. kei-gh- 542.] kista. Basket. Greek kisté, basket (> Old English cest, box): CHEST, CIST!, CISTERN. [Pok. kista 599.]
```


## [2026-09-05T20:58:25.879Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources\npython3 -c \"\nimport json;d=json.load(open('refs_online.json'));print(json.dumps(d['BQT'],ensure_ascii=False,indent=1))\""
}
```


### [2026-09-05T20:58:27.605Z] TOOL RESULT

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


## [2026-09-05T20:58:41.284Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BQT v2 leaf 228 (p.768) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==229' BQT_v2_pages.txt | head -50"
}
```


## [2026-09-05T20:58:41.434Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BQT v2 leaf 503 (p.1043) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==504' BQT_v2_pages.txt | head -50"
}
```


### [2026-09-05T20:58:43.076Z] TOOL RESULT

```
=== BQT v2 leaf 228 (p.768) ===
    ‫سە‬                                                                                                          ‫خم آهن کون‬
‫‪ ۰‬سم اول بر وزن عثمان '‬                  ‫خمدان‬                              ‫مایل‌باشد » وبعطی گویند مهره‌ایست‌سیاه بسرخی‬
‫وداش وکورة‬      ‫ومنکده را گونند‬               ‫شراخانه(‪)۲‬‬                                                                         ‫مابل ‪٩‬‏‬

     ‫خت یزی وسفال یزرا نز گفته اند ‪. ۷‬‬                                      ‫خم ] هن گون ‪ ۰‬کنابه از آسمان‬
‫مخقف خمیده است که از‬                 ‫‪-‬‬       ‫جمده‬                                                                                 ‫‪۳‬‬
‫خمیدن و خم کردیدن باشد ‪ -‬و بمعنی خفته‬                                       ‫وبای‬   ‫انی‬   ‫وسکون‬   ‫نم اول‬     ‫؟ ه‬        ‫خمت‬

                          ‫‪۳‬‬   ‫هما مده است‬         ‫وخوابیده‬
                                                                            ‫ابجد » بمعنی خم بزرگ است » و انرابعربی‬
                 ‫با رای‬              ‫خمره ‪۸‬‬                                                                             ‫دن گویند ‪.‬‬

                 ‫فرشت » بروزن و معنی خمجه‬                                   ‫خمیره ‪ - ۲‬با رای‌قرشت بروزن سنبله‪.‬‬
                      ‫است که خم کوچك باشد ‪.‬‬
                 ‫خم ردن ‪ -‬بفتح اول‬                                          ‫‪۰‬ممعي خمىره‬    ‫‪a" ۴‬‏ بروزن‌غنحه‪.‬‬      ‫حمجه‬

      ‫خمره‬                    ‫کنابه باخزگترن‌باشد ‪.‬‬                                               ‫است که کخموچك باشد ‪.‬‬
‫ضم‌اول بروزن گلستان‪,‬‬           ‫خمستان ‪۹‬‬
‫مبکده وشرابخانه را گونند ۔ وداش و کور سفال‬
                                                                                                 ‫مویشکدرهابخانه را گویند ‪.‬‬
         ‫‪,‬‬    ‫یزی وخشت یز برا نیز گفته‌اند ‪°‬‬
                                                                            ‫نم هر دو خاو سکون‬           ‫‏‪- ٩‬‬          ‫خمخم‬
‫بقتح اول و ضم انی وسکون‬              ‫‪.‬‬       ‫حمش‬
                                                                            ‫|را شفترك خوالند‬
                                                                                           ‫»ستنیی باشد که ن‬
                                                                                                          ‫هردومیم ر‬
‫شین نقطه دار › مخفف خموش است که ازحرف‬
                                                                             ‫وخاکشی را (‪ )۱‬نکیوزبند و آنرا شتر برغبت‬
‫نزدن وصامت بودن باشد ‪ -‬ودواب رام شده رالیز‬
                                                  ‫کویند‪.۱۱‬‬
                                                                                                                        ‫‪-‬‬   ‫ررد‬        ‫نمام‬



 ‫خمك؟"‪ -‬م اول و فتح ثانی مشدد‬                                               ‫خمخمه" ‪ -‬بنتح‌اول بر وزن زمزمه ‪,‬‬
 ‫وسکون‌کاف » بمعنی دست بردست زدن وصدای‬                                      ‫متکبرانه سخن گفتن واز یی حرف زدن وطمام‬
  ‫یزن‬
    ‫هیمنی‬
        ‫ب‪-‬ی‌وتشدید نا‬                        ‫ل‬
                                             ‫سشدوبا‬
                                                  ‫آانبا‬                           ‫خوردن باشد چنانکه صدای آن از بین‬
                                                                              ‫دیهون‬
‫معتی دارد ‪ -‬ودف ودار کوچکی را نیزگویند‬                                                                          ‫بر امد ‪.‬‬         ‫اشکس‬



 ‫که چنبرآن از برنج با روی باشد ‪ -‬ومصفرخم‬                                    ‫م دادن = کنابه آزردکردن ورفع‬
                                                  ‫هت ‪.‬‬                      ‫باشد چنانکه حهرگاه کوبند ‪:‬‬                 ‫و دفع نمودن‬
‫خسمخکمدخ ‪۱‬ا‪۳‬ن‪۵‬ه‌وشر بخ|الهرا گویند‪,‬‬                                     ‫أ‬    ‫« خم دهد » مراد آن باشدکه دفع نکند ورد‬
```


### [2026-09-05T20:58:44.698Z] TOOL RESULT

```
=== BQT v2 leaf 503 (p.1043) ===
                                                                                                 ‫—‬    ‫‪64 ۱‬‬   ‫س‬




‫و دیات را همگفته‌اند ‪ -‬وبمعنی ترس و میم حم‬
                                                       ‫رلو » بروزن زلو » جانوری است که‬
   ‫هدیز‬
      ‫راش‬
        ‫پب‬‫وایت‬
             ‫شکوءسوشک‬            ‫نی‬
                                  ‫عو‬‫بتم‪-‬‬
                                       ‫ه‬               ‫و زلو را هم‬            ‫خ‌والند ‪-‬‬   ‫آ را بعر نی ارضه‬
 ‫مرت‬      ‫و اجتناب را نیز گونند ‪ - ۱‬و بمعنی‬                                                   ‫میگوبند ‪٩‬‏ ‪#.‬‬
‫و افوس باشد ‪ -‬و بمعنی شتاب وتعجیل‌هم آمده‬
                                                     ‫ر نور = بروزن تنور » بن خوشة خرما‬
           ‫‪-‬هوش وکآاهی را هم گویند‪.‬‬
                                  ‫است و‬
                                                     ‫باشد ‪ -‬ونامکرم سیاه رنگی هم‌هست کهآ را زلو‬
‫شله دار‬         ‫ارخ‪-‬ای‬
                     ‫ز نهاربخوا‬                                ‫میگوبند » خون از بدن میمکد ‪. ۴‬‬
‫و وأو معدوله ‪ .‬عد کل و پیمان شکن را‬
                                     ‫گویشد ‪.‬‬
                                                       ‫باشد وثالی بواو مجهول رسیده » موبه والسگه‬
‫بیاقطه ‪ .‬امان‬    ‫ت با دال‬   ‫رنهاردار‬
                                                                         ‫راکوبند و پتازی هربر خوانند ‪.‬‬
                    ‫و مهلت دهنده رگاونند ‪. ۷‬‬
                                                       ‫للیودان = بفتح اول بروزن ببویدن‬  ‫ر‬
 ‫نهبادیرر‪-‬زن بیاری ‪ .‬کیرا‬             ‫ز‬                ‫بمعنی زلوبه است که ناله وموبه و زوزه کردن‬
 ‫کونند که شرط وعهد کند وامان ومپلت‌طلبد »‬                                                     ‫سک باشد ‪. ۴‬‬
                      ‫و زهاربان جمم آن است‪.‬‬
                                                     ‫= بکس اول وسکون ثالی و‬                          ‫رز‬
‫‪ -‬بکر اول و سکون ثاتی بر‬          ‫زان‬                ‫های (‪ )۱‬بااف کشیده بروزن بیار » بمعنی امان‬
 ‫وزن بربان » نایشواه را گویند»وآن تخمی است‬             ‫ادلرا لگیوزبند ‪ -‬و در‬‫معه‬
                                                                              ‫‪-‬و‬‫پی‬‫وشد‬
                                                                                    ‫ومهلت با‬
 ‫که برروی خمیر نان پاشند ؛ و با زای‌فارسی‌هم‬           ‫«لهار‬‫مقام تاکیدهم کفته میشرد چنانکه ز‬
                                   ‫آمده ات ‪.‬‬
                                                       ‫شراب نخوری» یمنی البته ضواهی‌خورد ‪-‬وامات‬


                                           ‫هزم‬
                                             ‫بیان شدان‬
                ‫کغتنوات‬
                      ‫در زای نقطه داریا وأو مشتمل بر نجاه و دو ل‬
 ‫خوانند ‏‪ - ٩‬وم اول » مخفف زود است که‬                ‫رو = بفتح اول و سکون انی » نامپسس‬
‫تمجیل وشتاب باشد *‪ -‬ونام ولابتی‌هم هست که‬              ‫طهماسب است که در ابران پنج سال پادشاهی‬
                 ‫آنرا زوزن بروزن سوزن کوبند ‪.‬‬          ‫بحر‬         ‫ی‬‫بو‬
                                                                     ‫رند‬
                                                                       ‫عگوی‬
```


## [2026-09-05T20:58:54.956Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor n in 366 367 368 369 370; do echo \"--- leaf $n ---\"; awk -v N=$((n+1)) 'BEGIN{RS=\"\\f\"} NR==N' BQT_v1_pages.txt | head -12; done"
}
```


### [2026-09-05T20:58:56.710Z] TOOL RESULT

```
--- leaf 366 ---
بدان غلهٌ کوفته شده را برباد دهند تاکاه از آن
9
اقشه - بروزن کفچه, بمعنی باغورباشد
وآن ظه‌ایست که درآسیا خرد کنند و بشکنند
افغات» باین
نقطه‌دار بروزن‌سنان ,
بممنی‌فرباد وزاری باشد-
ونام فسلهاست مشهور
چنانکه آرد نشود .
افشین ۱ ‌‌ مروزن کم 0 نام شخصی بوده
افی زد دفام - کنابه از قلمواسطی
ومعروف وجمعش‌آفاغنه
--- leaf 367 ---
افگنده(۱)سم کنابه ازعجز وزاری
بسیارباشد .
ومعرب افلاطون‌است . راو حکیمی بوده مشهور
و معروف در زمان کف واستاد ارسطو است»
وساز ارغنون مخترع اوست .
افالا گبان- بک رکف . کنامه ازئوابت
و سیارات است - وطایفه ای باششد از می دینان
ویدمذهبان .
افندبدن بت ور وزن ستدیدن ِ جنگ
وخصوحت کردن باشد ب
افیلون « بالام بروزن‌شبیخون » درمنة
کوهی را کوبند . | کرخاکشر آنرا باروغن‌بادام
--- leaf 368 ---
آفرعطی
۱ اقر یس ۱ - بح اول وسکون ثانی
و رای بی‌نقطه بتحتانی رسیده واضم طا و سکون
سین بی‌قطه .نلم جزبره ابست ازجزایی مونان .
اقسوس - بر وزن‌اضوی » یونانی؟
دانه است مانند زرشك وچون اورا (۱) شکنند
چیزی‌چسبنده ولج ازدرون‌آن برآید » با زرتیخ
بر تلخن تباه شده نهند بروباند. و جمیم ورمها
و آماسها را افع بود ۰ و مویزج علی عمان
اس :
اقشون » باین فرشت بروزن افیون .
بلفت یوتانی و بسنی گوبند رومی دوابی است
--- leaf 369 ---
9 تست سس با وس سید بد
و تسس سح
برایر ,۵ ۱ -
# 0
« ۵ و رم
7
--- leaf 370 ---
```


## [2026-09-05T20:59:07.689Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"ابزار\" BQT_v1_pages.txt | head -10\necho \"=== leaf numbers ===\"\nawk '/ابزار/{n=0; for(i=1;i<=NR;i++);} {n+=gsub(/\\f/,\"\")} /ابزار/{print NR\": leaf \"n\": \"$0}' BQT_v1_pages.txt | head -10"
}
```


### [2026-09-05T20:59:09.515Z] TOOL RESULT

```
4164:آت شگردان ۰ آرواره » آفتاب گردان ۰ آفتا به» آقا.ابزار» از گیل
30638:وسد.و 8۲۵016۱2 بمعنی نوشتن) , ابزاری که بدان میتوان مطاب خود را بشخص منظور از
=== leaf numbers ===
4164: leaf 0: آت شگردان ۰ آرواره » آفتاب گردان ۰ آفتا به» آقا.ابزار» از گیل
30638: leaf 0: وسد.و 8۲۵016۱2 بمعنی نوشتن) , ابزاری که بدان میتوان مطاب خود را بشخص منظور از
```


## [2026-09-05T20:59:14.993Z] TOOL CALL #52: Bash

```json
{
 "command": "ls tools/ && python3 tools/ref_page.py BQT:148 2>&1 | head -40"
}
```


### [2026-09-05T20:59:28.185Z] TOOL RESULT

```
build_site.py
fetch_source.py
ganjoor.py
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
no scan of BQT covers printed page 148 (see 'scans' in refs_online.json)
```


## [2026-09-05T20:59:37.660Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor n in 320 330 340 350 355 360 363; do echo \"--- leaf $n ---\"; awk -v N=$((n+1)) 'BEGIN{RS=\"\\f\"} NR==N' BQT_v1_pages.txt | head -4; done"
}
```


### [2026-09-05T20:59:39.284Z] TOOL RESULT

```
--- leaf 320 ---
ار که
واستر بشندند ودرعلف زارها (۱) سردهند تابچرد؛
و باین معنی نم اول و انی مشهور است
ار کال -بکر اول و سکون ثانی با
--- leaf 330 ---
اسپخحول بکسر اول و سکون‌انی
و بای فارسی مکور و خای نقطه دار حضموم‌بواو
ولام زده » بععتی‌پیخال است که فضله وافکند گی
اسیر ۱ س با بای فارسی بر وزن مهتر»
--- leaf 340 ---
استرش -ایم اول و لت و قحرابم
و سکون‌شین قرشت ۰ آنی راکوبند کهزمین‌را
بدان شیار کنند .
وسکون‌ثانی ونون وکاف فارسی» مردم کیاه باشد,
--- leaf 350 ---
اسکندروی
و دختثر از دارا حامله
بودوأنظهار نمیکردتابوی
دهن‌اورا با اسکندروی
--- leaf 355 ---
و سکن الی و دال ابجد , نام روزدوم است از
خمسا مترفةٌ فدیم- وبودن آفتاب دربرجعفرب
ودرین روز عفان بمنی آتش پرستان جش نکنند
و بمعنی اول بجای فوفانی نون عم آمده است .
--- leaf 360 ---
وشطهای سیله دارد . ۱ نوعی ازبوی مادران باتد . گویند کترانیدن‌آن
اطموط ‏ بنتم اول بر وزن مضوط , | درخانه گزندکان موذی را بکربزاند وآنرابعربی
بمعنی اطماط است که بندق حندی باشد  .‏ ۰ | قیصوم خوانند .
اطمسا ه بفتح ال و ثالت بتحتانی ابو ط ‏ پابای حطیء بروزن و معنی
--- leaf 363 ---
افر اشتن بروزن ومعنی‌برداشتن: بلند
ساختن باشد .
افر اشته بروزث ومعنی برداشته‌و بطند
ماخته و بالارده )۱( باشد ۰
```


## [2026-09-05T20:59:45.739Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor n in 363 364 365; do echo \"--- leaf $n ---\"; awk -v N=$((n+1)) 'BEGIN{RS=\"\\f\"} NR==N' BQT_v1_pages.txt; done"
}
```


### [2026-09-05T20:59:47.620Z] TOOL RESULT

```
--- leaf 363 ---
افر اشتن بروزن ومعنی‌برداشتن: بلند
ساختن باشد .
افر اشته بروزث ومعنی برداشته‌و بطند
ماخته و بالارده )۱( باشد ۰
۱ فر دون - بفتح اول رانی‌وسکون‌نالث
و کربای ابجد وبای حطی بواو رسیده و بنون
زده , دوایی اس تکه آنرا قرفیون کوبند . ا کر
کزند کی جانوران را نانع است .
که آنرا بشیرازی بالنگوی خوورو (۲گوبند .
ء اس را نافع است ۳
نام شهرست که نوشیروان آ ادکرده بود در کتار
دربای مصی » و مادر عثرا از آن شهر است ۱ -
وم ولایتی‌است از زنگبا - وم زمینی ه‌هست
در بلاد غرب ۰
ارف » بروزن فرزند ۰ فر و نیکوبی
وزیبایی وحشمت باشد؟ .
افر ندیدن مصدر افرید است بعنی
زب دادن وزشت کردن وآراستن .
افر نگ . بروژن و معنی اورنگت لست
تخت پادشاهان باشد - وبمعثی فر وفکوبی
کون که بمربی صاری‌خوانند؟ .
49 چث : (- شده .
۱ -ظ , معرب افرنگه.
۲ ۱۳
افر و خشن؟ « بروزن اندوختن بسعنی
روئن کردن آتش رچراغ باشد .
افر ود بر وزن سردوز . بممنی
روشن و روشن کردن باشد - و روشن کننده را
نز گویند - وامر بدین‌معنی م‌عست بمنی‌روشن
کن ویفروز . *
افر وسا لین باین بالف کشیدم و کس
لام وبای‌حطی بتحتانی رسیده وبنون زده ؛ بلخت
بونانی6 سنکی است که آنرا حربی حجر القمر
خوانند ؛ وآن سفید وشفاف میباشد ودر شبهای
افرونی ماه می‌بابند , اگر بر گردن‌مصروعبندند
شفا باید .
افر و شه۱ ۳ بفتح اول وشن شطمرار .
نام حلوابی است. وآن چنان باش دکه‌آرد وروغن
را باهم بيامیز ند وبدست بعالند تلدانه داله گُردده
آنگاه در بائیلی کنند وصل‌درآن ریزندوبربالای
آش هند نا يك بیزد و سخت شود - و بحنی
گوند نان‌خورشی‌است د رکیلان. و آن‌چنانباشد
که زرد؛ تخم مرغ را در شیی خم ریزند و يك
برهم زند ویربالای آاش نهند ۴ شیرمانند دلمه
بىته شود بعد از آن شیرینی داخل آن سازند
ونان را درآن تربت کنند با خشکه پلاو در آن
ریزید و با قاشق خورند - وحلوای کندم دلیده
شده - ولوژیشه را فیزافروشه گوبند .
افروغ « بنتح‌اول. بسنی‌فروخ‌ودوشنی
وفابش وپرنو باشد اعم‌از دوشنی‌وپرنو فتاب وعاء
و آش و امثال آن :
۱ فر هنج ه بغع‌اول واكوها وسکون
(۲) چك : خرد .
۵ افروزیدن - رکه : افروختن .
۱ رک : آفروشه .
--- leaf 364 ---
آفری
کشوث و نخم آنرا بذرالکشوث خوانند . فواق
را تافع است .
افری فتح اول وثانی بروزن سفری »
مخفف آفرین است که دد مقام تصی نگوند .
و بسکون انی هم درست است .
افر یدون ‏ - فربدونباشد. واویادشاهی
بوده. ءشهوره ویستی گویند افربدون نوح علیه ب
اللام است ۰ و بعضی ذوالقرنین اعظم او را
صسدانند ۰
اقفر پسموسش_ » بسکون سی‌بی نفطه
وم حیموواو وسین دیکرساکن, پیونانی؟ مرضی
است که مردانرا بهم میرسد و آن شدت تعوظ
است بعنی بوسته لت مردی ایستاده هیباشد ۰
وباسقاط همرز ه ی شت. -
گویندمقراض کرده وسوخته| تر | درمعاأجین‌خوردن
عفن را فربه سازد .
افز | ح بفتح اول‌بازای هوز بروزن‌اجزا»
1 ۱۳ اسج ۰
افز اد ه بر وزن رفتار , بمعنی کفش
ویای افزار باشد - وبادبانکشتی را نیز گویند -
والات مشهوران باشد عموماودفتن جولاگانرا
را کربند خصوصا ‏ وادوبة کرمی که در طعام
کنند همجو فلفل و دارچنی و ژبره و مانند
آن۴ .
۹ م2 : فربدون و آفربدون.
۳ ‌- ره 4 ابریشم.
4
افژ ول با زای قلرسی بروزن مقبول.
بمعنی تقاضا وانگیز باشد - و بمعتی پریشان هم
۳ ات ِ
افو لته » بر وزن افروزنده . بر
انگیز نده وتان را گویند - ویمعئی‌دود
کننده مویریشان سازنده م امه احست.
افو لین « بروزن افروزیدن.بمعنی
پرانگشتن بجشگه - وبرس رکارآوردن - وقانا
نمودن - ویریشان ماختن - و دور کردن هرچیز
باشد خصوصا کرد یکه برجامه نشیند .
ا فقس - پاسین‌بی‌نقطه بروزن‌ترساه بمعنی
رام کننده وافونگر باشد .
افسار » بر وزن رفتاد . بمعنی فا
ابت که افونگر و رام کننده باشد - وچیزی را
گون دکه از چرم ومانند آن سازند ویرسراسب
هنکن تافقال .اي تن
افسان بروزن ترسان . آهنی‌وسنگی
را کوش دکه بدان د وخمفی و عانتد ان کر
کنند - وبمعتی افسائه وسر گذشت هم گفته‌اندب
واضوشگررا فز گوید :
وحکامات گذنتگان باد - و مشهور و شهرت
بافثه شده را یز گوبند .
اقسای - با بای حطی بر وزن لبلای .
افونگر و رام کننده را گویند. واقسافیدن رام
کردن را ۰
اقسر ۷ بروژن برسر. بممنی‌تاج باشد
22لا ,۵52 « واثه ناید ۷د ۶ رل : اقفر .
۱ - از: اوستایی 211 یشوند (به - بر)
7 « ثبر که ۷۰ » . رك : افار .
--- leaf 365 ---
ات
وافرا یمرن الیل خوالند .
اسر ۵لن؟ « بر وزن افشردن » بمعنی
سردشدن ویخ بستن ومنجمد کردیدن باشد - واز
چیزی ‏ وکسی‌دل سرد شدن هم هست -
آقتاب عالمتاب است .
افسرسگزی « بکس مین بی شله
و سکون کاف فارسی و زای نقطه دار بتحتانی
رسیده ۰ نام سازی باشد که نوازند - ونام تصنیفی
وقولی است ازصنیفات بارید .
افسر شدن » کنابه از پادشاء خدن
باشك .
افستتین ۴ -
بکسر الث و سکون
نون و فوقانی بتحتانی
رسیده و بنون‌زده» نوعی
از بوی مادران کوهی
است .کلآن بافحوان
وتلخی آن صبر تزديك
است . دردچشم‌را سود
دارد . افنئی
افوس؟ با واو مجپول بر وزن
محبوی » بمعتی ظلم و ستم - ویراهی باشد -
ودریغ و حسرت را نیز گویند - و بمعنی بازی
وظرات - وسخر ولاغ هم‌هست - وبا واو معروف
تام‌شهر دقیاتوی بوده ۴» وبسنی گویند باین‌معنی
افتون
عربی‌است .
افسون؟ » بر وزن افیون ۰ خوادن
حصول مقاصد خود - و بمعنی حیله و تروبر هم
عست ۰ 3
اقشاد - با شین شلهدار بی‌وزن‌دستار ,
بمعنی افتردن باشد یمثیاب ازچیزی‌بزور دست
گرفتن - و ریزنده - و رشن یی دری را یز
گوند - و بسعنی خلالیدن حم آمده است هه
وامر بدین ممنی لیزهست یعنی بخلان و بغشار
ویریز - وبمعنی‌مد ومعاون وشربك ورفیق نیز
کنته‌اند همچو دزد افشار - و نام طایفه ای حم
هست از تر کان ۷ .
اقشره - بنم ناك وفتح رای قرشت »
هرچیز که آنرا افشرده باشند» و بعربی عصاره
گویشد . ۱
افشلك - بروزن چشمك » شبنم‌را گویند
که شبها برروی سبزه و کل ولاله شیند . . :
افشنگه » بر وزن خرچنگه ۰ سسمعتی
فشك است که شبنم باشد .
افشنه - بنتح اود وثاث ونون و سکون
ثانی » نام دهی است از دههای بضارا . گونند
ولادت شیخ ابوعلی آنجا شده ۹
اقشون » بر وزن اون . چیزی باشد
مانند یئجهٌ دست و دسته نیز دارد که دعقانان
۴ - بیونانی
0 « اشتینگای» بمعنی سوزان ودردتاك « نفی» ؛ )25610 ۸۲۱6۵0۲512 از
دستة آ فتابی‌ها وشببه ببومادران واسانس‌بیار ممطردارد « کل کلاب ۲۹۹ «فرهنگه روستابی۲۰۹*.
۴ - مهلوی21565 « دهارله۱۸۰» و02565» بازند 5 تن بومنگ4 ۱۱۵202599
مشتو از 202 (با[ 21۷۷ پیشوند) + 4۵1068 تلفظجنوب‌غربی ممادل لغت‌شمال‌غربی 2۳95۲۵۱011۳2
مشتق از: 5۲11 (شنبدن) « بارتولمه ۱٩۳۷‏ » « نب رکه ۱۵* » زبا کی21805 « کربرسن ۷۰ ۶ .
۴ - ظ . 05۱05 ۸(درکیاد و کیه). ٩‏ مشتق ازافابیدن (مقاسه شود: فاء فای, فاییدن
وغیرء)؛از ربشة ثا5 .۰ (304 و[ با ,. ا0اقط . 120 .4. ۵0۲ناعت) در ,5216008۳ )
۶ دائرالمعارف اسلام » . ۷ نادرخاه ازاین ابل بود . رك: مقالات کسروی ۱: ٩۸‏ بعد.
```


## [2026-09-05T21:00:07.509Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"افزار\" BQT_alt_v1.txt BQT_dli_part1.txt 2>/dev/null | head -20"
}
```


### [2026-09-05T21:00:07.568Z] TOOL RESULT

```
BQT_alt_v1.txt:9892:اادءباشدو شمر نبز خوانند - وتم افزارست 
BQT_alt_v1.txt:10784:است ۷ - و افزاری را نیز کون دکه نمد زین را 
BQT_alt_v1.txt:13216:آغازه بروزنآوازه » دست‌افزارست 
BQT_alt_v1.txt:16207:۵ ابزار - افزار اوزار. در پپلوی 2۱۷22 < تاوادیا ۱۵۸ : ۲ > و 2122۳ « منای 
BQT_alt_v1.txt:16217:م رکب همیشه بمعتی ات و وسیلت ومابه ات چون : دست افزار ۰ پا افزار . دمگافزار » بوی 
BQT_alt_v1.txt:21210:بروزن هترك » بمعنی اسکنه‌باشد و آن‌افزارست 
BQT_alt_v1.txt:21213:اسگنه ‏ بنینی اسکنك است که افزار 
BQT_alt_v1.txt:22214:اغاده - پر وزن ملازه . افزارست 
BQT_alt_v1.txt:22606:وبای افزار باشد - وبادبان کشتی را نیز گویند - 
BQT_alt_v1.txt:22662:واوزار بمعی‌آلات انتق عتوعا 0 باافزار ویااوزار بیعنی کفش وبوافزار تمعتی ادو به است 7 
BQT_alt_v1.txt:24713:باشد . وآن افزارست که بدا ن کل و کچ بربام 
BQT_alt_v1.txt:26389:او راد « بروزن و ممنی افزار است کد 
BQT_alt_v1.txt:26393:و پا افزار سوداروی گرم‌باشد مثل فلفل‌ودارچینی 
BQT_alt_v1.txt:26463:ه‌ ۳ ۳ افزار ۰ 
BQT_alt_v1.txt:33964:لرهاه - بر وزن درگاء » افزارست 
BQT_alt_v1.txt:36386:افزاری باشد که جولاهکان‌بدان]خار برتانممالنده 
BQT_alt_v1.txt:40156:افزارست که درود گران.بدان چوب و نخته 
BQT_alt_v1.txt:41946:#۶ پا مر وف است نهر بی رجل افزار » دو تَختَةٌ کوچك باشد بمقدار نملین که 
BQT_alt_v1.txt:42039:» پاپوش - هر چه که پای را پپوشاند - پاافزار ؛ 
BQT_alt_v1.txt:42043:ره ۳ باافزار.
```


## [2026-09-05T21:00:13.335Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '16195,16230p' BQT_alt_v1.txt\necho \"=== also around 22600-22670 (افزار headword page) ===\"\nsed -n '22595,22670p' BQT_alt_v1.txt"
}
```


### [2026-09-05T21:00:13.398Z] TOOL RESULT

```
ابر‌هه‌ملة ‏ به«الاشرم> حاکم حنشی یمن درحدود مه قرن‌ششم م‌. رك: دائرةالمعارفاسللام: آبرهد. 
؟ - پپلوی 208165111170 «تاوادت (ع۱» < بشدعتشی +۱4 ۰ گیلکی 00ناحاح0ا2, 
فریزندی 20۷۲191۱۱۵۳۱ یرای 2۱۲15860 , نشتزی ۱۵و2۲ و اس ۲۸۱ 
سمتاتی ۵۷۲۱51100 سنگری(0۳310110)8 , سرخ 2۷۲15400 , لاسگردی۵۷۲152۳. 
شهمیرزادی 071511117 < .۲ ص ۱۱ ۲ اشکاشمی ۵۲661۷:۲۴ , وخی ۷۵۲5/111۳ . 
منگلجی ۷2۲6۸11۳ « گربرسن ۷۵ > ۰ طبری ۷۳5218 , مازندرانی کنونی 0756۳0 
« واژه امد ٩۳‏ » مخقف آن بریشم وععرب آن ابرسم « تفی ۴ . 
رك : اوستا ومزدسنا ۱۱ و۱۳۲ و۳ ۴ - در برهان و 
پیض فرهنگهای دیگر هرجا کلمةٌ جاسوس میآآبد چاپلوس را نیز چون عطف ببان و تفیری در 
دنبال آن میآورند از جمله معنی کلم ابته . لکن جاسوی مرادف چاپلوس نست و هوبك را 
تن نکن است و 9 لت زامه: ۶ ۵ رك : آب‌کون . 
۵ ابزار - افزار اوزار. در پپلوی 2۱۷22 < تاوادیا ۱۵۸ : ۲ > و 2122۳ « منای 
۶ : ۲ » بمعثی اداة . الت ؛ ومیل , مایه . - آنچه بدان طعام خوشی و کنند - در کلمات 


۳ج اشتاه امت 2 


۲ - رگ : آیشتن . 


م رکب همیشه بمعتی ات و وسیلت ومابه ات چون : دست افزار ۰ پا افزار . دمگافزار » بوی 
اقزار و جزآن « لقت نامه > . ۰ ابستاغ رگ ؛ اوستا و مزدبنا ۰۱۱۷ 
ابتاق ‏ رك : اوسثا و مزدیسنا ۰۹۹ 


ِ۳ٍِ_ِ_- ۱ آوخلا 


آش‌را کوبند ۴ » وباین معنی بفتح اول و ثانی 
وثاك هم آمده است ۴ . 

ابلوج * ه بروزن محلوج. قنسفیدرا 
کوتتارت که عفید و فند سوده ۳ 
است (۱). 
=== also around 22600-22670 (افزار headword page) ===
است که مردانرا بهم میرسد و آن شدت تعوظ 
نت ععتی یوسته آلت مردی استاده هیباشد . 
وباسقاط هیزه هم هنت . 
افر یشم ۴ بروزن ومعنیآبر شم است. 
گویندهقراش کرده وسوختهةآ ترا درمعاجین‌خوردن 
تن را فربه مازد . 
افز اح بنتح اولبازای وز بروزن‌اجزا, 
افزابنده وافزون را کونند - و امر بافزودن هم 
حست یعنی بیفزا وزیاده کن - وبمعنی خمیاژه‌هم" 
آهده اس . 
افز اد - بر وزن رفتار » بمعنی کفش 
وبای افزار باشد - وبادبان کشتی را نیز گویند - 
وآلات پشه‌وران بائد عموماودفتن جولاهگانرا 
را گوبند خصوصا - وادوبة گرمی که در طعام 
کنند همچو فلفل و دارچینی و زیره و مانند 
آن؟ . 


٩‏ - رل: فریدون و آفربدون. 
۳ ‌ رل 1 ابرشم. 


-- ۸ - 


افژ و با زای فارسی بروزن مقبول, 
بمعتی تقاضا وانگیز باشد - و بمعتی پریشان هم 
آمده است ۳ 

افژ و لنده بر وزن افروزنده 4 سر 
انگیزنده وقاضاکننده را گویند - ویمعنی‌دور 
هن شون شاخ سازئده م‌ آمده است. 

اف و لین « بروزن افروزیدن.بمعنی 
برانگختن بجنشگه - وبرسر کارآوردن - وتقاضا 
مودن - وپریشان ساختن - و دور کردن هرچیز 
باشد خصوصاً گردی که برجامه نشیند . 

اسف - پاسین‌بی‌نقطه بروزن‌ترساه بمعنی 
رام کننده وافونگر باشد . 

و هه بر وژن رفتاز . بمستی آفا 
ایت که افشونگر و رام کننده باشد - وچیزی را 
کوندکه از چرم ومانند آن سازند وبرسراسب 
واستر وامثال آن‌کنند ۵ . 

ا فسات ه بروزن ترسان . آهتی‌وسنگی 
را گوبن که بدا کارد وشمشیر و مانتد آن تیز 
کنند - ویمعنی افساته وت لت هم گفته ات 
وافونگررا یز گویند ۰ 
وحکابات گذشتگان باشد - و مشهور و شهرت 
تافته شده ۳ نیز گویند ۰ 

افسای - با بای حطی بر وزن لیلای . 
افونگر و رام کننده را گویند واقماییدن رام 
کردن را ۲ 


فقس بروزن مرسر؛ بممنی‌تاج باشد 


۴ - ۳۳۱۵0/509 (محتو از ۳۳۱2۳05 نموظ). 


1 بشوند 1 و 2 اوستابی (ژور » نبرو) « بارتولمه ۹ ۰ « یرک ِ_ افرار وازار 


واوزار بمعی‌آلات انتق عتوعا 0 باافزار ویااوزار بیعنی کفش وبوافزار تمعتی ادو به است 7 
آشر )نیع عنی برسر ۰ (جدکه) برسر (گذارند يا بندند) . طبری 13۲ . مازندرائ ی کنونی 


۵521 با ‌ واژه ناهد 1 راد : اقسر . 


۱ از: اوستابی 21۷۷ یشوند (به - بر)
```


## [2026-09-05T21:00:32.149Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BQT v3: find کوهان / کوه headword pages ===\"\ngrep -n \"کوهان\" incoming/BQT/BQT_v3_pages.txt | head -5\necho \"=== pdf page tags near ===\"\ngrep -n \"pdf page 53[0-9]\" incoming/BQT/BQT_v3_pages.txt | head"
}
```


### [2026-09-05T21:00:32.239Z] TOOL RESULT

```
=== BQT v3: find کوهان / کوه headword pages ===
3044:‏شتر يك کوهان
3078:وشخوار کننده که ‎dh‏ بادو کوهان درپشت داراد ‎sles‏ پاهاو کردن: ‎eine on‏ باروواری
12599:‏عقار؟ کوهان ‎of‏ بان برارسید.
12603:که عقر کوهان باشد .
16496:سطبر کوهان را خوانند - ونام ‎gle‏ هم‌هست؟
=== pdf page tags near ===
38777:[pdf page 530]
38870:[pdf page 531]
38927:[pdf page 532]
38966:[pdf page 533]
39023:[pdf page 534]
39110:[pdf page 535]
39189:[pdf page 536]
39257:[pdf page 537]
39309:[pdf page 538]
39357:[pdf page 539]
```


## [2026-09-05T21:00:34.010Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON اکواب ===\"; grep -n \"اکواب\" MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt incoming/MON/MON_2vol_Adena_v2_djvu.txt 2>/dev/null | head -10\necho \"=== MON صنج ===\"; grep -n \"صنج\" MON_part1.txt MON_part2.txt 2>/dev/null | head -10"
}
```


### [2026-09-05T21:00:34.107Z] TOOL RESULT

```
=== MON اکواب ===
=== MON صنج ===
MON_part1.txt:45553:حصنجره قرار دارد. این غده در انسان از 
MON_part1.txt:90266:صنج؛ : 571 [معر. . سنج» قس. . چنگ] (.) 
MON_part1.txt:90378:صنوج: ۰ 20201 [ع.] (ا.) ج. . صنح. . صنج‌ها,
```


## [2026-09-05T21:00:42.295Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '90260,90275p' MON_part1.txt\necho \"=== سنج entry ===\"; grep -n \"^سنج\\|سنج:\" MON_part1.txt MON_part2.txt | head -10\necho \"=== کوب/اکواب ===\"; grep -n \"کوب:\\|^کوب\" MON_part1.txt | head -5"
}
```


### [2026-09-05T21:00:42.433Z] TOOL RESULT

```
است» مانند: بارچه‌بافی» قالی‌افی. صنایع 
ظر یفه: صنعت‌هایی که در آنها ظرافت بکار 
رود از قبل خطاطی» نقاشی» مجسمه‌سازی» 
رقص؛ هنرهای زیسبا. صنایع بسدی: 
دست‌ورزی (فره.) 
صنج؛ : 571 [معر. . سنج» قس. . چنگ] (.) 
چنکگ. در فد ۶ فلزی که به وسبلهة 
بندی به انگشتان پیوندد. مج ۱ س از بند 
کردن به انگشتان» به 7 تا آوازی 
از آن بر آید. 
صندل؛: اوه (.) نوعی کفش که با نند به 
پا بندند. 
صندلی: آ-20021: (ص‌نسه. امر.) صندلی 
بیدسته: صندلیی که دسته ندارد؛ مق. صندلی 
دسته‌دار. صندلی دسته‌دار: صندلیی که دارای 
=== سنج entry ===
MON_part2.txt:4482:سنجش شعر بکار رود و در تقطیع شعرء آن 
MON_part2.txt:7463:گویند. فشار خون شریانی. فشار خون‌سنج: 
MON_part2.txt:17808:کارسنج: [:52-.۲ [- کارسنجنده] (ص‌فا.) 
MON_part2.txt:27892:سنجده و بیگفتگو از کسی. 
MON_part2.txt:28999:سنجبدن» اندازه گرفتن چیزی را. (امسص.) 
MON_part2.txt:30522:سنجیده» آزموده. حمله برنده. جنانده؛ 
MON_part2.txt:51368:سنجش و آن نزد اهل عراق ۲ رطل عراقی 
MON_part2.txt:85963:سنجنده. وزان سخن: سحن سنج. 
MON_part2.txt:85990:سنجیدن. (امص.) اندازه گیری» تعبین 
MON_part2.txt:90586:سنجد»ه سماق؛ سیر سرکه» سبزه (مراد 
=== کوب/اکواب ===
1833:آبله کوب: «۳-.2 (ص مر.) (بز.) کسی که 
3340:کوب» ضرب. عیب و نقص يا شکستگی که 
3501:اشکوب: «تت2 (- آشکوبه] (.) (معم.) 
3608:آشکوب: بناهای چندین آشیان. 
4235:کوب رو تلات شک نب در اندرون
```


## [2026-09-05T21:00:51.015Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk '/\\[pdf page 534\\]/,/\\[pdf page 536\\]/' incoming/BQT/BQT_v3_pages.txt | head -60"
}
```


### [2026-09-05T21:00:53.973Z] TOOL RESULT

```
[pdf page 534]
—\vev—
‏و بمعنی‎ - ٩ ‏و دام را بکشند‎ uty ‏ایشان را نه‎
‏و احمق و بیعقل وکوناء باشد ۴ - وبمعنی‎ abl
‏حرامزاده هم هست ۴ - وخاریشت کلان و کوچك‎
‏فارسی‌هم آمده‎ GEL ‏گفته‌اند ؛ وباینمعنی‎ 5s ‏را‎

. cel
‏مجپول بر وزن‎ ot be ۴ ‏کولیدن‎
‏کندن و کاویدن زمین باشد‎ yin » ‏ژولیدن‎
‏ورشه کندن و بر آوردن از زمین را یز‎ -

گونند .

‎OS‏ - بنم اول پروزن موم » کیاهی
‎wth‏ خوشبوی که آنرا اذخ رکوبند ‎٩‏ ؛ وبضی
کفته‌اند گیاهیست که در زمين ‎Lt‏ کرده بسا
شود وبخ ‎Ley‏ آن همچو نی‌باشد ۷ ؛ وبمعنی
اول ‎GEL‏ فارسی هم‌آمده است - ودرعرب ی کله
و رمةٌ شتران را گوبند - و ‎pth‏ اول هم در
عربی بالا رفتن اسب در باشد براسب ماده ۷ .

‏(۱) خم ۱ :کمثرا .
۱ - رك :کول .کولیدن .
تا کی ‎wT‏ بدام مرغ مراد

‎nh - ۴‏ معنی‌سحيح «کوله »۳ کول ‎(eam)‏ است.

‏کون

‏کوماج ۸ ‎CLS gee‏ است و آن
‎gt‏ باشد معروف +

‎٩ oT‏ ینم اول وفتح تالوسکون
رای قرشت . بلفت زند وپازند بمعنی امرودباشد
وآن میوه‌ایست ممروف که بعربی کمثری (۱)
خوانند .

‎gt”‏ بکس ثالت بروزن‌جوتش,
چاء جوی(۷) وکتکن را کون که چاه کن
باشد *۷.

‏کوهه ۱۱ با ای مجپول وفتح ‎WME‏
‏خانه‌ای را کوبند که از نی وعلف ‎PT pe‏
پالیزبانان در آن نشته محافظت فالیز و زراعت
کنند و کاهی صیادان در کمن صیدشینند ۷۳.

‏ون -بنم اود و فتع ‎yu‏ و سکون
‎og‏ درخت پده را کویند و آن نوعی از بید

‏(۷) ظ : چاه خوی .

‏همچو صیاد مانده در کوله .
نزاری قهستالی « رشیدی > .

‏۴ -قی:کیلکی: 1001 .

‏۴ - د رکنابادی 501-012 (مییکند(بفتحکاف) ). ‎kOlesh‏ (شیار کردن) « کنابادی» »
کردی ‎kolan‏ (حفر کردن, حك کردن ) « ژابا 0۱-۲۵۰ > وخی 2[ 22۶ ‎Jo)‏
```


## [2026-09-05T21:00:58.886Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk '/\\[pdf page 536\\]/,/\\[pdf page 537\\]/' incoming/BQT/BQT_v3_pages.txt | head -70"
}
```


### [2026-09-05T21:01:00.556Z] TOOL RESULT

```
[pdf page 536]
پوت کوب رکوه
ماند همه را کوه میگویند ۱ - و بضم اولوظهور | شتر وکاو بر آمده هم کوحان میگویند لیکن

nese oe oe . ۴ ‏معروف است و عربان بل خوانند‎ ol
‏کوهان ود-‎

کوه ابراهيم ‎an‏ کرمیت در
ولابت کرمان . بقتح‌نای‌متلنهبرآهد کی

‎oS‏ اخضر ‏ کنایه از ‎We | GUS‏ راکوبند - کوهان شتو

‏وبمعنی پروین هم هست وآن چند سترکوچك

‏باشد که ‎Ob SY jew‏ است در ثور ۰ وآن مکی
ازمنازل قمر است و بعربی ثربا خوانند .

‏کوه هاده - با بای فارسی بر وزن
کوشواره , حسه و پاره ولختی از کوه را کویند

‏- و کنابه از اسب هم هست که عربان ‎us‏

‏است .
کوه اسف » بنتح ‎ope‏ وسینبی‌شطه,
کوهیست که پدوستهآ ش‌از آن افروخته‌ودرخشان

‎. ‏فرو نتشیند‎ ST py ath”

‏کوهاموی = بنم اول و اك بالف
کشیده و میم بواو رسیده و بتحتاهی؟زده » دام
لوعی از بازی باشد ‎OT,‏ چنان است که خالك را
توده کنند وموبی درمیان ‎OT‏ ینپان سازندم و بعد
از آن‌آب برآن ریزند و کل کنند پن کروی

‏و شرط بندند و بردورآ نگل شینند و موی را

‏طلبند هر که بیابد شرط و گرو را ببرد و آن

‏بازی را بعربی بقیری خوانند ۳ .

‏کوهان ۴ با اك ‎dew‏ بوزن
سوهان ۰ بمعنی‌زین اسب است - وآنچه ازپشت

‏خوانند .
کوه ‎VY‏ = دامن کوه رااکویند یعنی
زمین ی که ‎gabe‏ کوء واقع است ‎on‏ بمعلی
کوهتان هم هست.
کوه‌بر ‎Vo‏ ۰ عنبر مطبق را
کویند و آن ‎ey‏ از عنبر است ۵ ‎BLS‏
‏طبقه برروی هم تشه است ماد کوه .

‎weg: ‏چش‎ (\)

‎: ‏قبه (عر)‎ : yt

‏مستفرق ‎pals‏ درین کوة ‎glass‏ شاماجل وصبحجزا را شناسیم. امیرخسرو دهلوی.

‏چیست ‎KY Spat‏ دانهای ک و کتار ‎ .‏ امیر خسرو دهلوی ۰ ودر اين ده بیت «گوزه»
مرادف غوزه میتوان خواند » وافه اعلم فرشیدی» + ۴ - پپلوی 6۵1( کوه , قلهٌ کوه) +
‎yl)!‏ باستان- ‎kaufa‏ > بارتولمه ۲4۳۱ «تیبرکك ص ‎٩۱۳۰‏ اوستا - ‎kaofa‏ (کوه. کوهان)»
پارسی‌باستان - 81063( کوه). پهلوی یز 1۵181 (کوء ‎(obs.‏ بلوچی ‎kéfagh. képak‏
‎(als)‏ , کردی 60۷۷1 ( وحشی ) «اسشق ‎cave‏ , ارمنی ع ۷۵/8 ( کوه » موج ) ؛ وبقول
‎kvab sual, Cir‏ (کوهان) «هو,شمانه۸۷» ورك : کوهان, که (بضم). ‏ ۴ - مولف‌فرهنگه
‎a gS lls‏ : « در ‎ds‏ مپذب‌الاسماه که ترد من است معنی بقیری را « کوهامان» نوشته:» امادر
‎das‏ متعلق‌بکتابخانة علامه دهشداه کوهامون» آمده ۰ در منتهی‌الارب آهده : « بقیری کسمیهی
بازبی‌است که بفارسی آ ترا کوهاموی کوبند © ۴ - از: کوه(ان (نموند ‎(ct‏ :
پپلوی - ‎kaofa‏ ؛ 16۵18 (کوه , کوهان) ۰ رك : ح ۲ ؛ وقس : کردی 801288 ‎(ot)‏
‏«ژابا ۳۷۱ » قس :که ‎Me)‏ 8 ره : چهانگیری .
[pdf page 537]
```


## [2026-09-05T21:01:10.567Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==229' BQT_v2_pages.txt | tail -25"
}
```


### [2026-09-05T21:01:12.307Z] TOOL RESULT

```
                                             ‫سشدوبا‬
                                                  ‫آانبا‬                           ‫خوردن باشد چنانکه صدای آن از بین‬
                                                                              ‫دیهون‬
‫معتی دارد ‪ -‬ودف ودار کوچکی را نیزگویند‬                                                                          ‫بر امد ‪.‬‬         ‫اشکس‬



 ‫که چنبرآن از برنج با روی باشد ‪ -‬ومصفرخم‬                                    ‫م دادن = کنابه آزردکردن ورفع‬
                                                  ‫هت ‪.‬‬                      ‫باشد چنانکه حهرگاه کوبند ‪:‬‬                 ‫و دفع نمودن‬
‫خسمخکمدخ ‪۱‬ا‪۳‬ن‪۵‬ه‌وشر بخ|الهرا گویند‪,‬‬                                     ‫أ‬    ‫« خم دهد » مراد آن باشدکه دفع نکند ورد‬

             ‫چه کده بمغنی خانه هما مده است ‪۱‬‬                                                                                 ‫‪.‬‬        ‫شماید‬


                                                            ‫(‪ )۲‬چش ‪ :‬ر‪+‬ا‪.‬‬                        ‫(‪ )۱‬خم ‪ -: ۱‬را‪.‬‬
             ‫خم («‪.‬م) ‪3‬‬         ‫(ھ‪.‬م‪= ).‬‬          ‫خنب‬       ‫‪-‬‬       ‫‪۲‬‬               ‫ص ‪. ۵۱۲‬‬      ‫الرجكم‪:‬اهر‬
                                                                                                          ‫‪۷‬‬
    ‫از ‪ :‬خم ‪٣‬‏ چه (یوند صفیر) ‪.‬‬                         ‫‪۴‬‬                   ‫‪ = ۳‬خنه م(ه‪.‬م) = خمره («‪.‬م‪۰ ).‬‬
    ‫ص‪.۷۵-۸‬‬
         ‫ح‌حم (یفتح هردوحاء ) ‪ .‬رك ‪ :‬لك ‪۵ ۲‬‬                                        ‫‪ - ۰‬خمخم (بکسر هردوخاه) =‬
  ‫اسم صوت عربی « خمخه بروزن ومعنی خنخنه است ‪ ۰‬و آن سخن کردن از تور‬                                                     ‫‪1‬‬

       ‫‪ ۳" ۰۷‬ر که‪ :‬خمدان‪.‬‬                      ‫از‪ :‬خم ‪ +‬ستان ( پنوند مکان)‪. ‎‬‬                       ‫‪٩‬‬                 ‫دزفولي ‪.871‬‬
               ‫(«‪.‬م‪۰ ).‬‬       ‫خنيك‬       ‫—‬    ‫‪۳‬‬                 ‫‪.‬‬   ‫چموش‬      ‫»‪ .‬رك‪:‬‬     ‫« چمش‬   ‫ممحض‬   ‫‪,‬‬   ‫ظ‬     ‫_‬    ‫‪۱‬‬
```


## [2026-09-05T21:01:22.449Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nf=incoming/WLD/WLD_Bd1_pages.txt\necho \"=== grep kaofa/xumba/kumbha ===\"; grep -n \"kaofa\\|xumba\\|kumbha\\|kaufa\" $f | head -10"
}
```


### [2026-09-05T21:01:24.221Z] TOOL RESULT

```
=== grep kaofa/xumba/kumbha ===
34796:      Apers. kaufa- „Berg", av. kaofa- „ds.   Kamelbuckel", np. kdh ,Berg"
43194:   Av. saeni-s „Spitze, Wipfel", saeni-kaofa- „mit spitzem, d. i. aufgerich-
```


## [2026-09-05T21:01:28.541Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nf=incoming/WLD/WLD_Bd1_pages.txt\nsed -n '34780,34810p' $f\necho \"=== leaf ===\"; awk 'NR<=34796 {n+=gsub(/\\f/,\"\")} END {print n}' $f\necho \"=== page tags nearby ===\"; grep -n \"pdf page\" $f | head -3"
}
```


### [2026-09-05T21:02:06.403Z] TOOL RESULT

```
y.vjiq, ai. kupa-, germ. huOa „Haube“ sind trotz Scheftelowitz BB. 28, 150
                                                         5
nicht Lw. aus assyr. kappa „Gefa8, Kasten“); Curtius       159.   Yielleicht
mir. ciiach (zweisilbig) „Becher“, wenn aus *kupako- (Stokes KZ. 41, 383,
Pedersen KG. 1212; doch s. auch Yf. LEWb. 2 u. caucus) aisl. hufr „Schiffs-   ;


 rumpf",     ags. liyf „Bienenstock‘(Bed. wie lat. alveus; Zupitza Gutt. 128;
 s. auch u. gamp „biegen“); liierlier (oder zur Wzf. auf -bh- oder -h-) wohl

 auch ags. gehopp „folliculus“, hoppe f. „bulla, Kapsel", mengl. hoppe „Samen-
kapsel des Flachses“ (Holthausen IF. 32, 340); allenfalls slav. *k*pz, cech.
kep „ vulva", poln. kiep „ds.; Narr, Taugenichts" (Berneker 664 f. zw.).
  Bedeutungsgruppe „Wolbung nach oben, Haufe u. dgl." (mit der vor-
                                                4
hergehenden richtig verbunden z. B. von Fick I 380 f.;:
      Apers. kaufa- „Berg", av. kaofa- „ds.   Kamelbuckel", np. kdh ,Berg"
                                                          ;



 (setzen -ph- voraus);            „Haufen"
                            lit. kaiipas    = abg. kiipz, ds. (serb. kiip freilich
 mit  anderer  Intonation als kaiipas; s. Berneker  646); lit. kaupiii, kaiipti
                                               qeu-                                            373

„haufeln“, kupiii, Mipti „auf einen Haufen legen, ordnen“, kupra „Hocker“,
kupstas „Hiigel“, kupeta „Heuhaufen“, kupinas „gehauft“, lett. kupt „sich
ballen", kupenis „Schneehaufen“, kuprs „Hocker“, mit Dehnstufe qo[u]p-
(vgl. Leskien Abl. 301, Trautmann Grm. Lges. 23), lit. kuopiii kuopti „hiiu-   ,

=== leaf ===
380
=== page tags nearby ===
```


## [2026-09-05T21:02:14.952Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nf=incoming/WLD/WLD_Bd1_pages.txt\ngrep -n \"kumbh\\|xumb\\|Kuiapf]\\|xurnb\" $f | head\necho \"=== find running head 376 ===\"; grep -n \"qeu- *37[4-9]\\|37[4-9] *qeu\" $f | head\nsed -n '34860,34920p' $f"
}
```


### [2026-09-05T21:02:16.702Z] TOOL RESULT

```
=== find running head 376 ===
34897:374                                                                      qeu-
35135:376                                       qeu-   — ken-,   (:   kau-, ku-)

ahd. (nach       dem quastenartigen Bliiten-             und Fruchtstand) hopfo „Hopfem‘
(Fick III 4 94 f.  wohl eher zu *sqeup-, -hh- „Biisehel, Schopf, Quaste <;
                       ;                                                                             ,


die freilich im Germ, sonst nur s-anl. Yertreter hat).
                                                        4
  Fiir aschw. hinpon ,,Hagebutte“ usw. (Fick III 95) weist apr. kaaubri
„Dorn“ auf   eine andere   Gdbed.    (s. qeub- „Dorn“).
                                                                4
  Ygl. im allgem. Curtius 5 159. F. Schmidt Urk. 22, Fick I 380, III 94 f.
                                    2
Zubaty BB. 18, 263, Yf. LE\Vb. u. cnpa.
  DaB ai. kumpa- (unbelegt) „lahm an der Hand ', lit. kumpti „sich kriim-
men“, kumpas ,.krumm“, kumpis „Schweineschinken", lett. kumpt „krumm,
                                                                  t£
buckelig werden“, apr. ctkumps Adv. „wiederum Nasalformen unseror \Vz.
seien (z. B. Fick I 4 380, III 4 93 f., Trautmann Apr. 332) ist weniger wahr-
scheinlich als deren Zugehorigkeit zu qawp- „biegen“ (?«-farbige Reduk-
tionsstufe in der Stellung zwischen Yelar und Labial.)                     —
   qeu-b-.
   In Anwendung auf Biegungen am Korper, sicli im Gelenk biegen:
   gr. xv fog „Hohlung vor            der Hiifte beim Yieh: Wirbelknochen          —W         iirfel'
                                                                                                        1




(daraus       lat.   cubus   ;
                                 xvfcokov „Ellbogen“ Poll, entweder von             xvfog mit
                                                                                   25 *
               ,                                                                                                                                       .     -;




374                                                                      qeu-


Suff. -to 7.o- naeh Solmsen Beitr. 1 7. oder Umbildung von y.vfkxov ds.                                                                                    —
ous lat. cubitum- nach Worten auf -co/.o- unter Einwirkung von mtevrj)
      Lat. cubitum            ,
                                   -us .Ellbogen" (daraus gr. y.vfnov ds.); cubo
                                                                  -are Jiegen"                                 ,

(fal. citpn               neben loferto ders. Inschrift erweist ital. b Meyer-
                   d. i. aiba[t}.
                                                                                                                                   ,

Liibke Wr.-St. 24, 52Sf.; auch piilign. incubat), lat. (tic-, in-) cunibo -ere                                                                     ,

,,sich legen“ (ursprgl. ,.sich zum Liegen niederbiicken"), sabin. cuniba „lec-
tica‘‘ (daB anch cymr. ijotjof ,,Hohle‘ als „Ort zum Kiederlegen" dieselbe

Bedeutungswendung zeige, ist sehr bedenklich; s. u. H-eu- ,.schwellen, hohl“).
      Got. hups          (st.       hitpi-'j,           ags. hype, ahd. ltuj ..Hufte" (davon zu trennen                                                    ai.

riipti- usw.,        s .kup-              ,,Schulter" i; aisl hojui, ags. on-hnpian ,,zuriickweichen' ;
                                                                          .
```


## [2026-09-05T21:02:21.605Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nf=incoming/WLD/WLD_Bd1_pages.txt\nsed -n '35090,35140p' $f"
}
```


### [2026-09-05T21:02:24.720Z] TOOL RESULT

```
Zugehorigkeit auch von russ. Iciiblo „Vogel-, Eichhornnest, Lagerstiitte des
Ebers; eigenes Heim, Nest“, kublitbsja ,.sich zusammenkauern, nisten von                                                                          --



einer Anschauung wie lat. cumbo aus.
     Curtius 529, Fick l 4 3901'., Uhlenbeck PBrB. 21, I00f., Ai. Wb. 58 f.,
     S.
Yf. LEWb. u. cupa.

     Nasaliert                   qam-bh-, meist qum-b-:
     Aisl. aptr-huppr,norw. mdartl. hupp und Inimp „die Weichen beim Yielr                                                                                  -




(vgl. zur Bed. got. Imps ,,Hiifte“ usw.; z. B. Uhlenbeck Got. Wb. 2 85, Fick
III 4 93 f., Falk-Torp u. hofte, liumpe), nhd. humpeln, mnd. liumpelen ,.hinken“
(oder dies zu skamb -, s. d. ? noch anders von Schroder Abl. 37 mit Itampeln                                                                                ,


ags. hnappian „schlafen“ usw. unter einem germ. *hcnap- vereint) und in
nicht spez. auf das Biegen oder Bugstellen des Korpers gewendeter Bed.                                                                                      :




     Norw1tump m. „Unebenheit,
              -
                  .               Knorren, Knollen“, engl. hump „Buckel                                                                                --
                                                                                                                                                            ,



nd.  Jnunpc f. „dickes Stuck -- , humpcl „niediiger ErdhiigeP, ndl. homp
                                                                                                                                --
„dickes Stiick Brot“ (kaum besser zu qem- zusaminendriicken ) vielleicht                                                             ;



nhd. (nd.) Humpen (Fick I 4 380; vgl. xvpftog; anders Schroder Abl. 19 f.                                                                                   :



mit Napf zu einer germ. Basis ha nap-);
376                                       qeu-   — ken-,   (:   kau-, ku-)



  ai.   kumba-h „das dicke Ende (eines Knochens); hervorragendes, weib-
licher   Kopfputzi?)“; ai. kiimbha-li „Topf, Krug“, Du. „die beiden Er-
```


## [2026-09-05T21:02:28.921Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '35135,35160p' incoming/WLD/WLD_Bd1_pages.txt"
}
```


### [2026-09-05T21:02:28.969Z] TOOL RESULT

```
376                                       qeu-   — ken-,   (:   kau-, ku-)



  ai.   kumba-h „das dicke Ende (eines Knochens); hervorragendes, weib-
licher   Kopfputzi?)“; ai. kiimbha-li „Topf, Krug“, Du. „die beiden Er-
hohungen auf der Stiru des Elefanten“ = av. xmnba- m. „Topf, Yertiefung“,
np. xitmb, xum ./Topf, Krug“ (diese mit aril. Tenuis asp.);
   gr. y.vuBy .Beeken, Schale, Kahn“, xvufiog .,GefaB“; xvpftiov „GefaB,
                       ,


Fahrzeug“ trotz Petersson IP. 34, 249 nicht mit einem Formans -mho- zu
                   ,




y.vag usw., Wz. keu-\ xvf.ipa.Xov, meist PI. „cymbalum, Beeken, das mit
einem andern zusammengeschlagen einen gellenden Ton gibt“, avaxvfx^a-
X.i^etv „klirrend umkippen, yon \Yagen“ (Curtius 158'.

   xv/xfii} ,.Kopf, y.v<ptf‘ EM., Suid., xv/.ipayog (£ 586;
                                                                                                                        1'
                                                            kopfiiber fallend                        ,
```


## [2026-09-05T21:02:37.699Z] TOOL CALL #68: Bash

```json
{
 "command": "ls site/pages/177.jpg 2>/dev/null; pdftoppm -f 177 -l 177 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg177 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/"
}
```


### [2026-09-05T21:02:40.090Z] TOOL RESULT

```
site/pages/177.jpg
total 24820
drwx------ 2 sfmqrb sfmqrb    4096 Sep  5 17:02 .
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
-rw-rw-r-- 1 sfmqrb sfmqrb  100925 Sep  5 16:52 bqt_pdf600.png
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
-rw-rw-r-- 1 sfmqrb sfmqrb   17908 Sep  5 16:44 build151a.py
-rw-rw-r-- 1 sfmqrb sfmqrb   15986 Sep  5 16:46 build151b.py
-rw-rw-r-- 1 sfmqrb sfmqrb   11172 Sep  5 16:47 build151c.py
-rw-rw-r-- 1 sfmqrb sfmqrb   19592 Sep  5 16:50 build151d.py
-rw-rw-r-- 1 sfmqrb sfmqrb    6433 Sep  5 16:50 build151z.py
-rw-rw-r-- 1 sfmqrb sfmqrb   51529 Sep  5 16:51 build152.py
-rw-rw-r-- 1 sfmqrb sfmqrb   51266 Sep  5 16:51 build154.py
-rw-rw-r-- 1 sfmqrb sfmqrb   61639 Sep  5 16:53 build155.py
-rw-rw-r-- 1 sfmqrb sfmqrb   70485 Sep  5 16:53 build156.py
-rw-rw-r-- 1 sfmqrb sfmqrb   72953 Sep  5 16:48 build158.py
-rw-rw-r-- 1 sfmqrb sfmqrb   74140 Sep  5 16:56 build160.py
-rw-rw-r-- 1 sfmqrb sfmqrb   53286 Sep  5 16:55 build161.py
-rw-rw-r-- 1 sfmqrb sfmqrb   67253 Sep  5 16:56 build162.py
-rw-rw-r-- 1 sfmqrb sfmqrb   45662 Sep  5 16:49 build164.py
-rw-rw-r-- 1 sfmqrb sfmqrb   82221 Sep  5 16:56 build168.py
-rw-rw-r-- 1 sfmqrb sfmqrb   53542 Sep  5 16:57 build169.py
-rw-rw-r-- 1 sfmqrb sfmqrb   58105 Sep  5 17:02 build171.py
-rw-rw-r-- 1 sfmqrb sfmqrb    7816 Sep  5 16:35 c_am2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   14765 Sep  5 16:35 c_am3.png
-rw-rw-r-- 1 sfmqrb sfmqrb   10038 Sep  5 16:35 c_empty2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4123 Sep  5 16:34 crop_am.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4986 Sep  5 16:34 crop_arabic_refs.png
-rw-rw-r-- 1 sfmqrb sfmqrb    7702 Sep  5 16:34 crop_empty.png
-rw-rw-r-- 1 sfmqrb sfmqrb   16978 Sep  5 16:34 crop_morocco.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5391 Sep  5 17:02 g2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2929 Sep  5 17:02 g3.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5607 Sep  5 17:02 g4.png
-rw-rw-r-- 1 sfmqrb sfmqrb  163996 Sep  5 16:46 gar2.png
-rw-rw-r-- 1 sfmqrb sfmqrb  124975 Sep  5 16:47 gar3.png
-rw-rw-r-- 1 sfmqrb sfmqrb   77205 Sep  5 16:46 gar.png
-rw-rw-r-- 1 sfmqrb sfmqrb   14924 Sep  5 17:01 geus_left.png
-rw-rw-r-- 1 sfmqrb sfmqrb   10247 Sep  5 17:01 ghaido_left.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4197 Sep  5 17:01 ghaido_low.png
-rw-rw-r-- 1 sfmqrb sfmqrb  944060 Sep  5 16:18 kent.txt
-rw-rw-r-- 1 sfmqrb sfmqrb     222 Sep  5 16:30 leaf.py
-rw-rw-r-- 1 sfmqrb sfmqrb   57617 Sep  5 16:20 mk129.py
-rw-rw-r-- 1 sfmqrb sfmqrb   74680 Sep  5 16:26 mk131.py
-rw-rw-r-- 1 sfmqrb sfmqrb   33365 Sep  5 16:25 mk133.py
-rw-rw-r-- 1 sfmqrb sfmqrb   42635 Sep  5 16:29 mk140.py
-rw-rw-r-- 1 sfmqrb sfmqrb   51288 Sep  5 16:30 mk143.py
-rw-rw-r-- 1 sfmqrb sfmqrb   57696 Sep  5 16:46 mk153.py
-rw-rw-r-- 1 sfmqrb sfmqrb   49505 Sep  5 16:50 mk157.py
-rw-rw-r-- 1 sfmqrb sfmqrb   56703 Sep  5 16:54 mk166.py
-rw-rw-r-- 1 sfmqrb sfmqrb   61790 Sep  5 16:57 mk167.py
-rw-rw-r-- 1 sfmqrb sfmqrb   30384 Sep  5 16:51 mk170.py
-rw-rw-r-- 1 sfmqrb sfmqrb    4344 Sep  5 16:49 n12b.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3969 Sep  5 16:49 n12.png
-rw-rw-r-- 1 sfmqrb sfmqrb   24939 Sep  5 17:01 n14.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2692 Sep  5 16:49 n16.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3293 Sep  5 17:01 n17b.png
-rw-rw-r-- 1 sfmqrb sfmqrb   17771 Sep  5 17:01 n17c.png
-rw-rw-r-- 1 sfmqrb sfmqrb    6463 Sep  5 17:01 n17.png
-rw-rw-r-- 1 sfmqrb sfmqrb    7472 Sep  5 17:01 n19.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3278 Sep  5 17:01 n5b.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2334 Sep  5 17:01 n5c.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3215 Sep  5 17:01 n5.png
-rw-rw-r-- 1 sfmqrb sfmqrb   11831 Sep  5 16:32 node4.png
-rw-rw-r-- 1 sfmqrb sfmqrb    7427 Sep  5 16:32 node7.png
-rw-rw-r-- 1 sfmqrb sfmqrb  944060 Sep  5 16:13 oldpers_djvu.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    6054 Sep  5 16:36 p152_e0left.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2672 Sep  5 16:36 p152_node2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   35268 Sep  5 16:59 p162a.png
-rw-rw-r-- 1 sfmqrb sfmqrb   14337 Sep  5 16:59 p162b.png
-rw-rw-r-- 1 sfmqrb sfmqrb   76438 Sep  5 16:59 p162.png
-rw-rw-r-- 1 sfmqrb sfmqrb   41788 Sep  5 16:53 p173_ital.png
-rw-rw-r-- 1 sfmqrb sfmqrb   32898 Sep  5 16:53 p173_op.png
-rw-rw-r-- 1 sfmqrb sfmqrb  161412 Sep  5 17:01 p174hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb  173427 Sep  5 17:01 p176hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2762 Sep  5 17:02 p189_empty.png
-rw-rw-r-- 1 sfmqrb sfmqrb   24596 Sep  5 17:02 p189_greek2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   20222 Sep  5 17:02 p189_khoris.png
-rw-rw-r-- 1 sfmqrb sfmqrb   33994 Sep  5 17:02 p189_n12.png
-rw-rw-r-- 1 sfmqrb sfmqrb  671488 Sep  5 16:52 p600_350.png
-rw-rw-r-- 1 sfmqrb sfmqrb  139701 Sep  5 16:52 p600_foot2.png
-rw-rw-r-- 1 sfmqrb sfmqrb  183909 Sep  5 16:52 p600_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1717 Sep  5 16:52 p600_head2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5162 Sep  5 16:52 p600_head.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1189 Sep  5 16:57 p600_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb   22067 Sep  5 16:29 part0.json
-rw-rw-r-- 1 sfmqrb sfmqrb   14156 Sep  5 16:22 part1.json
-rw-rw-r-- 1 sfmqrb sfmqrb   17147 Sep  5 16:44 part_a.json
-rw-rw-r-- 1 sfmqrb sfmqrb   15703 Sep  5 16:46 part_b.json
-rw-rw-r-- 1 sfmqrb sfmqrb   10974 Sep  5 16:47 part_c.json
-rw-rw-r-- 1 sfmqrb sfmqrb   19420 Sep  5 16:50 part_d.json
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
-rw-rw-r-- 1 sfmqrb sfmqrb  116877 Sep  5 16:46 pg167.png
-rw-rw-r-- 1 sfmqrb sfmqrb   86005 Sep  5 16:39 pg168.png
-rw-rw-r-- 1 sfmqrb sfmqrb   68420 Sep  5 16:42 pg169.png
-rw-rw-r-- 1 sfmqrb sfmqrb   37351 Sep  5 16:44 pg170.png
-rw-rw-r-- 1 sfmqrb sfmqrb  120612 Sep  5 16:49 pg171_450.png
-rw-rw-r-- 1 sfmqrb sfmqrb   73551 Sep  5 16:43 pg171.png
-rw-rw-r-- 1 sfmqrb sfmqrb   73400 Sep  5 16:56 pg172.png
-rw-rw-r-- 1 sfmqrb sfmqrb   52970 Sep  5 16:53 pg173.png
-rw-rw-r-- 1 sfmqrb sfmqrb   70664 Sep  5 17:00 pg174.png
-rw-rw-r-- 1 sfmqrb sfmqrb   54907 Sep  5 16:54 pg175.png
-rw-rw-r-- 1 sfmqrb sfmqrb   83583 Sep  5 17:00 pg176.png
-rw-rw-r-- 1 sfmqrb sfmqrb   88207 Sep  5 17:02 pg177.png
-rw-rw-r-- 1 sfmqrb sfmqrb   98352 Sep  5 17:01 pg178_hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   64024 Sep  5 17:01 pg178.png
-rw-rw-r-- 1 sfmqrb sfmqrb   57139 Sep  5 16:54 pg179.png
-rw-rw-r-- 1 sfmqrb sfmqrb   81598 Sep  5 16:58 pg180.png
-rw-rw-r-- 1 sfmqrb sfmqrb   56794 Sep  5 17:00 pg181.png
-rw-rw-r-- 1 sfmqrb sfmqrb   66020 Sep  5 17:01 pg182.png
-rw-rw-r-- 1 sfmqrb sfmqrb   77310 Sep  5 16:58 pg184.png
-rw-rw-r-- 1 sfmqrb sfmqrb   53749 Sep  5 17:02 pg187.png
-rw-rw-r-- 1 sfmqrb sfmqrb   77516 Sep  5 17:01 pg189.png
-rw-rw-r-- 1 sfmqrb sfmqrb   44812 Sep  5 16:34 pg532.png
-rw-rw-r-- 1 sfmqrb sfmqrb  153161 Sep  5 16:34 pg532_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4868 Sep  5 16:14 prt.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  333088 Sep  5 16:16 sod135_c.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1817364 Sep  5 16:16 sod135.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  101641 Sep  5 16:15 sod136_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1892712 Sep  5 16:15 sod136.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  561602 Sep  5 16:57 t598.png
-rw-rw-r-- 1 sfmqrb sfmqrb  632359 Sep  5 16:57 t599.png
-rw-rw-r-- 1 sfmqrb sfmqrb  671488 Sep  5 16:57 t600.png
-rw-rw-r-- 1 sfmqrb sfmqrb  545905 Sep  5 16:57 t601.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1268 Sep  5 16:57 top598.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1268 Sep  5 16:57 top599.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1268 Sep  5 16:57 top600.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1268 Sep  5 16:57 top601.png
-rw-rw-r-- 1 sfmqrb sfmqrb   24918 Sep  5 16:58 tops2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4812 Sep  5 16:57 tops.png
-rw-rw-r-- 1 sfmqrb sfmqrb   56398 Sep  5 16:26 write144.py
```


## [2026-09-05T21:02:44.930Z] TOOL CALL #69: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg177.png"
}
```


### [2026-09-05T21:02:45.304Z] TOOL RESULT

```

```


## [2026-09-05T21:02:45.302Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-05T21:03:04.358Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN cymbal ===\"; grep -n \"cymbal\" KLN_1966.txt | head -5\necho \"=== KLN xumba / kaofa ===\"; grep -n \"xumba\\|kaofa\\|Avestic xumba\" KLN_1966.txt KLN_1971.txt | head -5\necho \"=== KLN cup n. ===\"; grep -n \"^cup, n\\|cup, n\\.\" KLN_1966.txt | head -3\necho \"=== KLN hump ===\"; grep -n \"^hump\\|hump, n\" KLN_1966.txt | head -3"
}
```


### [2026-09-05T21:03:04.467Z] TOOL RESULT

```
=== KLN cymbal ===
7414:chimb,  n.  —  See  chime,  ‘rim  of  a  cask’, chime,  n.,  a  set  of  bells.  —  ME.  chimbe,  chymbe, ‘cymbal’,  fr.  OF.  chimble,  cimble,  cimbe,  fr.  L. cymbalum,  ‘cymbal’.  See  cymbal.
7861:ML.  clavicymbalum.  See  clavicembalo. Derivative:  clavecin-ist,  n. clavelization,  n.,  inoculation  with  sheep  pox virus  (med.)  —  F.  clavelisation ,  fr.  clavelee, ‘sheep  pox’,  fr.  Late  L.  cldvellus,  ‘sheep  pox’, dimin.  of  L.  clavus,  ‘nail’,  which  is  rel.  to  clavis, ‘key’;  see  clavicle  and  -ization.  The  disease  is so  called  because  the  pustules  caused  by  it  re¬ semble  nailheads.
7862:clavicembalo,  n.,  a  harpsichord.  —  It.,  lit.  ‘cymbal with  a  keyboard’,  compounded  of  L.  clavis, ‘key’,  and  cymbalum,  ‘cymbal’.  See  clavicle  and cymbal.
8310:combatant,  1)  adj.,  fighting;  ready  to  fight;  2)  n., fighter.  —  F.  combattant,  pres.  part,  of  com¬ battre.  See  combat,  v.,  and  -ant. combe,  n.,  a  deep  valley.  —  OE.  cumb,  of  Celtic origin ;  cp.  Bret,  komb,  ‘small  valley’,  W.  cwmm, ‘dale,  valley’,  Mir.  comm,  Ir.  and  Gael,  cum, ‘vessel’,  which  are  cogn.  with  Gk.  xup.fkrj,  ‘the hollow  of  a  vessel,  cup,  boat’.  Sec  cymbal  and cp.  2nd  coomb.
10082:cymbal,  n„  either  of  a  pair  of  brass  plates  used
=== KLN xumba / kaofa ===
KLN_1971.txt:62711:OI. kumbhah, ‘pot, jar’, Avestic xumba, of 
KLN_1971.txt:132077:tic kaofa ‘mountain, hump’, and fr. Arab. 
KLN_1966.txt:10083:in  orchestras.  —  ME.  cimbal,  symbol,  fr.  OE. cymbal  and  MF.  (=  F.)  cymbak,  which  both derive  fr.  L.  cymbahtm,  fr.  Gk.  xupipaXov,  fr. x<VPt],  ‘the  hollow  of  a  vessel,  cup,  boat’,  fr. I.-E.  base  *qumb-,  ‘to  bend,  curve’,  whence  also OI.  kumbhdh,  ‘pot,  jar’,  Avestic  xumba,  of s.m.,  Toch.  A  kumpac,  ‘drum’,  W.  cwmm,  ‘val¬ ley’,  Bret,  komb,  ‘small  valley’,  MIr.  comm, ‘vessel’,  cummal,  ‘cup’,  and  E.  hump,  ‘swelling, protuberance’  (q.v.)  Cp.  cymba,  chime,  n.  Cp. also  combe.
KLN_1966.txt:20824:Koh-i-noor,  n.,  a  famous  diamond,  one  of  the British  crown  jewels.  —  Pers.  koh-i-nur,  lit. ‘mountain  of  light’,  prop,  a  hybrid  coined  fr. Pers.  koh,  ‘mountain’,  which  is  rel.  to  Pers. kohe,  ‘hump’,  OPers.  kaufa-,  ‘mountain’,  Aves- tic  kaofa-,  ‘mountain,  hump’,  and  fr.  Arab. nur,  ‘light’  (see  Menorah). kohl,  n.,  powder  (esp.  of  antimony),  used  by  East¬ ern  women  to  darken  the  eyelids.  —  Arab. kuhl.  See  alcohol.
=== KLN cup n. ===
=== KLN hump ===
18237:hump,  n.,  a  rounded  protuberance.  —  Of  LG. origin.  Cp.  MLG.  hump,  ‘bump,  hunch’,  Du. homp,  ‘lump,  chunk’,  Norw.  hump,  'knoll'. These  words  derive  fr.  I.-E.  base  *qumb-,  ’to bend,  curve',  whence  also  OI.  kumbhdh,  ‘pot, jar',  Gk.  x'i;i3r.  ‘the  hollow  of  a  vessel,  cup. boat’.  See  cymbal  and  cp.  chime,  'set  of  bells’. Derivatives:  hump,  tr.v.,  hump-ed,  adj.,  hump-y, adj.,  hump-i-ness,  n.
18238:humpback,  n.  —  Compounded  of  hump  and  back.
18243:humpty-dumpty,  n.,  a  short  or  dumpy  figure.  — Fr.  Humpty-Dumpty,  hero  of  a  nursery  rhyme. The  name  prob.  arose  through  the  reduplication of  Humpty,  a  pet  form  of  Humphrey.  Cp.  Ernest Weekley’s  Etymological  Dictionary  s.v.
```


## [2026-09-05T21:03:14.516Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor L in 10082 20824 18237; do awk -v T=$L 'NR<=T {n+=gsub(/\\f/,\"\")} END {print T\": leaf \"n}' KLN_1966.txt; done\npython3 -c \"\nimport json;d=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'));print(d['KLN']['page_offset'])\""
}
```


### [2026-09-05T21:03:16.283Z] TOOL RESULT

```
10082: leaf 216
20824: leaf 458
18237: leaf 404
KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
```


## [2026-09-05T21:03:40.951Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==208' KLN_1966.txt | head -20"
}
```


### [2026-09-05T21:03:42.775Z] TOOL RESULT

```
ed  of  crino,  ‘hair’  (fr. L.  crinis),  and  lino,  ‘flax’  (fr.  L.  linum).  It.  crino- lino  prop,  denotes  a  fabric  whose  woof  is  made of  hair  and  whose  warp  is  made  of  linen.  See crinite  and  linen.
Derivative :  crinoline,  tr.  v.
Crinum,  n.,  a  genus  of  plants  of  the  amaryllis family  ( bot .)  —  ModL.,  fr.  Gk.  xptvov,  ‘lily’, which  is  a  foreign  word  of  unknown  origin.  Cp. the  first  element  in  crinoid. crio-,  combining  form  meaning  ‘ram-headed’.  — Gk.  xpto-,  fr.  xptoc,  ‘ram,  battering  ram’,  which prob.  stands  for  *xplf6?  and  is  rel.  to  xepa6?, ‘homed’,  fr.  xspai;,  ‘horn’,  and  cogn.  with  ON. hreinn,  ‘reindeer’.  See  horn  and  cp.  cerato-,  cer¬ vine.  Cp.  also  the  first  element  in  reindeer, criosphinx,  n.,  a  sphinx  with  the  head  of  a  ram.  — Compounded  of  Gk.  xpf6<;,  ‘ram’,  and  aeptyi;, ‘sphinx’.  See  prec  word  and  sphinx, cripple,  n.  —  ME.  cripel,  crepel,  crupel,  fr.  OE. crypel,  rel.  to  ON.  kryppill,  OFris.  kreppel,  MDu. cropel,  crepel,  Du.  kreupele,  ‘cripple’,  MHG., G.  kriippel,  lit.  ‘bent,  twisted’,  and  to  OE. creopan,  ‘to  creep’.  See  creep  and  cp.  croft,  crop. Derivatives:  cripple,  tr.  v.,  crippl-ed,  adj.,  crip- ple-ness,  n.,  crippl-er,  n.,  crippl-ing,  adj.  and  n., crippl-ing-ly,  adv.,  crippl-y,  adj. crisis,  n.  —  L.,  fr.  Gk.  xptou;,  ‘a  separating,  put¬ ting  apart,  a  decision’,  rel.  to  xpiT/j!;,  ‘judge,’ xpfvetv,  ‘to  separate,  pick  out,  decide,  judge’, fr.  I.-E.  base  *(s)q(e)re(i)-,  ‘to  separate’,  whence
crisp
also  L.  cernere,  ‘to  separate,  sift,  distinguish, discern,  understand,  decide’.  See  certain  and  cp. critic  and  words  there  referred  to.  Cp.  also acrisia,  eccrinology,  endocrine,  hypocrisy, crisp,  adj.,  i)  brittle;  2)  lively;  3)  fresh;  4)  curly. —  OE.,  fr.  L.  crispus,  ‘curly’,  which  is  cogn. with  W.  crych,  Bret,  crech ,  of  s.m.,  fr.  I.-E.  base *(s)qreis -,  whence  also  L.  crlnis  (for  *crisnis ), ‘hair’,  and  crista,  ‘tuft  on  the  head  of  animals, cock’s  comb’.  See  crest  and  cp.  words  there referred  to.  Cp.  also  Crispin.
Derivatives :  crisp,  tr.  and  intr.  v.,  crispate,  adj. (q.v.),  crisp-ly,  adv.,  crisp-ness,  n.,  crisp-y,  adj. crispate,  adj.,  of  a  curly  appearance.  —  L.  cris- pdtus,  pp.  of  crispare,  ‘to  curl,  wave’,  fr.  crispus. See  prec.  word  and  adj.  suflf.  -ate.
Derivative:  crispat-ion ,  n.
Crispin,  masc.  PN.  —  L.  Crispmus,  a  Roman cognomen  derived  fr.  crispus,  ‘curled’.  See crisp,  adj.,  and  -in  (representing  L.  -inus). criss-cross,  n.,  a  mark  made  with  two  crossing lines.  —  Fr.  earlier  Christ-cross.
Derivatives:  criss-cross,  adj.,  tr.  v.,  adv. cristate,  adj.,  crested  (said  esp.  of  birds  and  other animals).  —  L.  cristatus,  ‘having  a  crest  or  tuft’, it.  crista.  See  crest  and  adj.  suff.  -ate. criterion,  n.  —  Gk.  xpiTrjpiov,  ‘a  means  for  judg¬ ing’,  fr.  xptr rfi,  ‘judge’,  fr.  xptveiv,  ‘to  sepa¬ rate,  decide,  judge’.  See  critic, crith,  n.,  a  unit  of  weight  for  gases.  —  Coined  by Hoffmann  fr.  Gk.  kplffr),  ‘barleycorn’,  which  is prob.  cogn.  with  L.  hordeum,  ‘barley’.  See Hordeum.
critic,  n.  —  L.  criticus,  fr.  Gk.  xpmxoi ;,  ‘capable of  judging’,  fr.  xpiTTjt;,  ‘judge’,  fr.  xpfveiv,  ‘to separate,  decide,  judge',  which  is  cogn.  with  L. cernere,  ‘to  sieve,  distinguish,  discern*  under¬ stand,  decide’.  See  certain  and  cp.  crisis,  crite¬ rion,  diacritical,  hypocrite,  oneirocritic. Derivatives:  critic-al,  adj.,  critical-ly,  adv., critical-ness,  n.,  critic-ism,  n.,  critic-ize,  critic¬ ise,  intr.  and  tr.  v.,  critic-iz-er,  critic-is-er ,  n., critic-iz-ing-ly,  critic-is-ing-ly,  adv. critique,  n.  —  F.,  fr.  Gk.  xpirixf)  (short  for  *xpi- tl x>,  te/vtj,  ‘the  critical  art’),  fem.  of  xpirixo?, ‘of,  or  for,  judging,  capable  of  judging’.  See critic.
croak,  intr.  and  tr.  v.  From  the  stem  of  OE. crac-ettan,  ‘to  croak’,  which  is  rel.  to  OE.  cra- cian,  ‘to  resound’,  OE.  crawan,  ‘to  crow’,  ME. creken,  ‘to  croak’.  All  these  words  are  of  imita¬ tive  origin.  See  raven  and  cp.  Circaetus.  Cp.  also crack,  crake,  creak,  crow,  grackle.
Derivatives:  croak ,  n.,  croak-er,  n.,  croak-ing, adj.  and  n.,  croak-y,  adj.
Croat,  n.  —  Fr.  earlier  Chorwat,  fr.  Serbo- Croatian  Hrvat,  fr.  OSIav.  Churvatinu,  ‘Croat’, lit.  ’mountaineer,  highlander’, fr .chitrva,  ‘moun¬ tain’,  which  is  rel.  to  OSIav.,  Serb,  and Croatian  gora,  Russ,  gora,  Pol.  gdra,  Czech  and Slovak  hora,  and  cogn.  with  OI.  girth,  Avestic gain,  ‘mountain’.  Alb.  gur,  ‘rock’,  Lith.  gire,
374
‘forest’  and  prob.  also  with  Gk.  pop £&?,  ‘north wind’,  lit.  ‘a  mountain  wind’.  See  Boreas  and cp.  cravat.
Derivatives:  Croat-ian,  adj.  and  n.
crocein,  croceine,  n.,  any  of  several  yellow  and red  dyes  ( chem .)  —  Formed  with  chem.  suff.  -in, resp.  -ine  fr.  L.  croceus,  ‘saffron-colored’,  fr. crocus,  ‘saffron’.  See  Crocus.
crochet,  n.,  a  kind  of  knitting  done  with  a  small hook.  —  F.,  ‘a  small  hook’,  dimin.  of  croc, ‘hook’,  which  is  a  Teut.  loan  word.  Cp.  ON. krokr,  ‘hook’  and  see  crook.  Cp.  also  crotchet, crocket,  and  accroach,  encroach.
Derivatives:  crochet,  tr.  and  intr.  v.,  crochet-er, n.,  crochet-ing,  n.
crocidolitc,  n.,  a  blue  or  green  fibrous  mineral, consisting  of  silicate  of  iron  and  solium  (mine¬ ral.)  —  Compounded  of  Gk.  xpoxu?,  gen.  xpo- xiiSo?,  ‘a  nap  of  woolen  cloth’,  and  X1&05, ‘stone’.  The  first  element  is  rel.  to  Gk.  xpAxrj, ‘woof,  thread’,  stands  in  gradational  relation¬ ship  to  xpexsiv,  ‘to  weave’,  and  is  cogn.  with OE.  hreol,  ‘reel’,  hrxg(e)l,  ‘garment’,  ON.  hrtell, ‘a  weaver’s  sley’,  fr.  I.-E.  base  *qrek-,  ‘to  strike’. See  rail,  ‘garment’,  reel,  ‘a  revolvable  instru¬ ment’,  and  cp.  next  word.  For  the  second element  see  -lite.
```


## [2026-09-05T21:03:51.094Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==217' KLN_1966.txt | grep -n \"^ *39[01] *$\\|39[01]\" | head -5"
}
```


### [2026-09-05T21:03:52.876Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-05T21:03:56.577Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==217' KLN_1966.txt | grep -oE \"^[0-9]{3}$|[[:space:]][0-9]{3}[[:space:]]\" | head -10\necho \"---first line---\"; awk 'BEGIN{RS=\"\\f\"} NR==217' KLN_1966.txt | head -2"
}
```


### [2026-09-05T21:03:58.616Z] TOOL RESULT

```
392
---first line---
ncyclopedia  (q.v.)
Derivatives:  cyclop(a)ed-ic,  adj.,  cyclop(a)ed- ist,  n.
```


## [2026-09-05T21:04:06.993Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== NYB ===\"; grep -n \"kōf\\|kôf\\|xumb\\|zōr\\|zūt\\|zūd\\|abzār\\|abzūd\" NYB_vol2_glossary.txt | head -20"
}
```


### [2026-09-05T21:04:07.053Z] TOOL RESULT

```
=== NYB ===
563:apa-zón [’pzwn'] increase, addition 11217; tan pat-~ kunéh increase thy physical well being 21%, cf s. v. ?pat (11); increase of spiritual blessings 50%. — MPrs ’bzwn (A-H IT); Paz. awazün; NP afzün ‘more, greater’; < *abi-Zavana-, in which api- was substituted for abi-, v.s. v. apa-; from apa-zūtan, q.v. Wikander, Orbis XXXI, 1972, 183—184, prefers the read- ing Ppzn'] = äp-zan ‘a bath(ing vessel)’, NP abzan referring to the corresponding passage of Sn: bi- garmäbah šau ‘go to the warm bath!’
566:apa-zütan ["pzwtn'], apa-zāyītan [’pz’dy- tn'], apazäy- ['pz?d-], to increase, to augment, pt. = pret. pass. 3d p. sg. apa- züt 109%, apazäyit ['pz'dt'] 925. — < *abi-jav-, in SW with api- substituted for abi- (v. s. v. apa-) < abi-+ Av. (504) !gav- ‘to procure’; MPrth "bgwdn *bg*w- ‘to increase, to add to’, ?bg^w ‘increase’; Arm lw. augut ‘profit’; — OP caus. abi- jävaya- ‘to add’; MPrs pres. ’bzw- intr., ’bz’y- trans. ‘to increase’; Paz. awazūdan awazüed. Henning, A-H III Gloss. s. v. ’bgwdn; Benveniste, JA 228, 1936, 203- 204; Ghilain 76.
4573:zat [zwt'] swift, prompt, quick 74; adv. quickly 181%, 1912. — MPrs zwd; NP zūd.
6435:awazūdan, -zāed: apazū- tan
```


## [2026-09-05T21:04:08.523Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== IEC (Mann) ===\"; grep -n \"kumbho\\|kaupos\\|geu-\\|kumb\" IEC.txt | head -10\necho \"=== SYN Buck mountain/heap ===\"; grep -n \"kaofa\\|kaufa\" SYN.txt | head -5"
}
```


### [2026-09-05T21:04:08.587Z] TOOL RESULT

```
=== IEC (Mann) ===
3979:geu-, see gieuuo, ið
4479:gumb- (gumbh-) ‘swelling, lump; lumpy, swollen’; gumbstos ‘swollen’. WP I, 562. Cf. gumbhos, ghumb-, 2humb-, etc. (All forms but Gmc. are ambig.) Arm. (ambig.) kumb (knob, hump’, but equally fr. *kumb-, q.v, cf. Skt. kümbah, etc.); Per. cf. gumbed ‘dome; tumbler, glass’; Oss. cf. gumbul “ball of cheese; MHG kumpf ‘blunt’; G cf. kumpfig ‘potbellied’; ON kumpi ‘Jump’; OCS goba ‘sponge’; Cz. houba *fun- gus’; Li. gumbas ‘tumour’ beside gumbstu, gumbti ‘form a lump’; Latv. gumba (fr. Lith.) ‘swelling’. Cf. OCS gostü (‘dense, compact’, fr. *gumbstos) LW in Finn. kumpu ‘hill’, and in Hung. gomba ‘fungus’
4490:kumbl, kuml (1) ‘cairn’; Cz. hemel ‘weft of hair, bun of hair’; Li. guñbulas, gùmulas ‘buri on tree; boil
4492:gumbhros (gumuros) *mass'. Cf. gumb-, etc. MHG kumber, kummer ‘rubbish’; G Kum- mer, id. (and ‘rubble’); Frisian: kommer ‘hare’s droppings’; Li. gumbras, gùmuras ‘Jump’
8262:kübo ‘lie’. Cf. kumbó (1) Lat. cubo, åre, pf. cübi, id.; Ir. cúbaim ‘crouch, lie down’; ON (?) hopa, v. ‘recoil’; OE cf. (?) hop-scyte ‘counterpane’
8368:küm- (?). Cf. kumb-, kumolos Alb. kum, v. ‘cram’; kümem ‘swell’; i kümur, adj. ‘chubby’; Ir. cf. cüm “body, shape’; cum-
8371:kumbolos, à, ios (1) 'hump, lump, bulge; bulging vessel". WP I, 375. Cf. kumbos, kumo- los Ligurian (place-name) cf. Cumbels; Alb. (?) kümbulil, f. “plum”, the sense perh. influenced by Gk. kokkümelon); Blg. (substrate) küm- bula ‘kind of plum’; Ir. comhal *door-jamb'; comhaille ‘bulge, belly’; W cwmwl, pl. cymy- lau, m. (‘cloud’, the sense influenced by Lat. cumulus); LG hümpel (‘pile’, but cf. Kum- bos); Latv. cf. (variant) kumbris 'hump; cervi- cal bone”
8372:kumbolos, om (2) *vessel'. Cf. kumbos. WP I, 375. Same as (1)? Gk. kümbalon ‘basin’; MHG cf. humpel- nache 'small boat
8373:kumbo (kumboló) ‘resound’ Gk. cf. kümbalon (2) «cymbalon'; Alb. kum- boj ‘resound’; MLG humpeln, v. ‘sob’; Norw. (variant) humre ‘whinny’. (A variant of type *kum- appears in Alb. kumë ‘musical note’ and MHG hummen ‘to hum’)
8374:kumbos, à ‘hump, dome, hollow, basin, bel- lied pot'. (Variant: kumbhos) Ski. kumbah, -am, m. n. ‘knuckle-bone, club- head, chignon’ (variant: kumbháh “jar, pot, urn’; kumbhih, f. id.); Av. xumbo (‘pot, < *-b- or *-bh-); Per. xum “jar, alembic'; Tokh. A umpa ((pot', *-b- or *-bh-); Arm. kumb ‘hump, boss’; Gk. kúmbos ‘hollow; pot’; kúm- bë “helmet, pot, cup, boat’; Phrygian (? Thra- . ^n) kúbba ‘cup’; LW in LLat. cumbia ‘cups’; Gaul. cumba ‘hold of ship; valley’; MIr. comm (*vessel, pot', fr. *-b- or *-bh- as also for Bry- thonic); Br. kumm (2) ‘hollow, dell, nook’; komm, m. pl. u ‘trough’; komb ‘valley’; Cor. cüm, pl. cummow ‘dingle’: W cwm, pl. cy- moedd ‘valley’, cf. also cwman, m. ‘tub’; Du. homp, f. ‘lump’; LG humpe, f. id.; EME hump; Norw. hump “hummock, bump, gnur?’; LG in > G Humpe, Humpen, m. 'tankard'; Latv. kumba ‘hernia’
=== SYN Buck mountain/heap ===
955:line hill Pol. gora; pagérek, Sp. montajia; colina, cerro Du. berg; heuvel wzg6rek Rum. munte; deal, colina OHG _ berg; buhil, houc Russ. gora; cholm Ir. sliab; telach, cnoc, bri MHG berg; biihel, hiibel, Skt. giri-, parvata-, acala-, NIr. — sliabh; cnoc (tulach) houc etc. W. mynydd; bryn (bre) NHG berg; hiigel Av. gairi-, paurvata, bara- Br. menez; Icrec’h, bre zah-, OPers. kaufa.
997:Du. heuvel, MAG hiibel ‘hill’ : OHG hovar, OE hofer ‘hump’, Lith. kupra ‘hump’. Here also Av. kaofa- ‘mountain peak, camel’s hump’, OPers. kaufa Mountain’ (NPers. kwh ‘mountain’) : Lith. kaupas, ChSl. kupt, NE heap, NHG haufe ‘heap’, Grk. xidés ‘bent’, all fr. TE *keup-, *keub-, *keubh- in words for ‘bend, curve’. Walde-P. 1.372 ff. oh ha a Gor, pe mound’, fr, the adj. seen in
1015:OPers. kaufa-: Du. heuvel, etc., above, 4.
```


## [2026-09-05T21:04:47.721Z] TOOL CALL #77: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nmkdir -p data/verification/sources/refs/ocr/BOOK\ncp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg177.png data/verification/sources/refs/ocr/BOOK/177.png && echo copied\nfor u in \\\n 'https://en.wiktionary.org/wiki/%DA%A9%D9%88%D9%87' \\\n 'https://en.wiktionary.org/wiki/%D8%AE%D9%85' \\\n 'https://en.wiktionary.org/wiki/%D8%B2%D9%88%D8%B1' \\\n 'https://en.wiktionary.org/wiki/%D8%A7%D9%81%D8%B2%D9%88%D8%AF%D9%86' \\\n 'https://en.wiktionary.org/wiki/%D8%B2%D9%88%D8%AF' \\\n 'https://en.wiktionary.org/wiki/%D8%A7%D9%81%D8%B2%D8%A7%D8%B1' \\\n 'https://en.wiktionary.org/wiki/%D9%83%D9%88%D8%A8' \\\n 'https://en.wiktionary.org/wiki/%D8%B5%D9%86%D8%AC' \\\n 'https://www.etymonline.com/word/cup' \\\n 'https://www.etymonline.com/word/hump' \\\n 'https://www.etymonline.com/word/cymbal' \\\n 'https://www.etymonline.com/word/heap' ; do\n python3 tools/fetch_source.py \"$u\" --note \"pdf page 177 (book p.147), roots Gĕu 1/Keu 1 and Geu 2: etymology check\" 2>&1 | tail -2\ndone"
}
```


### [2026-09-05T21:04:54.432Z] TOOL RESULT

```
copied
/home/sfmqrb/git/rishe/data/verification/sources/web/a7a60fb0048e8f97.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b9c7b3fad5f6902c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/162b84a90f3c113a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/bd578855bc4cc3ca.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/dc2637b7ad2b0c2f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/96550d35ac718862.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/fb36445e25e3e38e.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/76b256393a277f36.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/5586292324d9a4a6.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f681aae67595f6af.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/59cf53f33e3c23ec.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a1923ecdb4afa1de.txt
```


## [2026-09-05T21:04:56.884Z] TOOL CALL #78: Bash

```json
{
 "command": "sed -n '1,120p' tools/verify_check.py"
}
```


### [2026-09-05T21:04:56.925Z] TOOL RESULT

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


## [2026-09-05T21:05:24.830Z] TOOL CALL #79: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"jāvaya\\|jav-\\|abijāvaya\\|abiy-jāvaya\\|abij\" KNT.txt | head -10\necho \"=== TLM ===\"; grep -n \"jāvaya\\|jav\" TLM.txt | head -5"
}
```


### [2026-09-05T21:05:24.887Z] TOOL RESULT

```
521:abiyajavayam XPg 9, and abijdvayam ХРЕ 40. niyasaya DNb 5, 46, 49, probably for *niyayasaya. [a]fiya[s?]ya DB 4.91, perhaps for *atiyayasiya. marika- DNb 50, 55, 59°, cf. Phi. mérak, Skt.
1953:1, The typical IE name consisted of a com- pound of two stems; such names have mostly been interpreted in §160-§162. To these must be added the following, which are of uncertain interpreta- tion: Kabijiya-, Gaumata- (see Lex. s.vv.).
2027:Nom. Sg. martiya, х$йуабтуа, Ката, baga, drauga, hamiciya, атиќа; man’s name, Kabijiya; place names and ethnics Раза, Майа, Sugda Suguda, Saka, Sparda, Mudréya, Uja боја, Yauna, Parðava, Armina, Arminiya, Asagaria, Gadāra, Márgava, Uyjiya.
3451:CMb = Cyrus, Мовонав в. 1 Kūruš : xSdyabiya : vazraka : Kabijiya 2 hyd : zšāyaðiyahyā : puça : Hazdmani siya : З айу : уада... 4... ... akutà ...
3487:31 büjiya : avam : Bardiyam : avàja * уаба : Kabüjiya : Bardiyam : avaja : kürahy 32 à : пазу : azdà : abava : (уа : Bardiya : avajata : раѕауа : Kabijiya : Mudráyam 33 : akiyava : уада : Kabūjiya : Mudrayam : aSiyava : pasáva : kara : апка : abava 34 : pasava : drauga : dahyauvi : vasiy : abava : uta : Parsaiy : ша : Mádaiy : ut 35 d:aniy&uvà : dahyuSuvà ; 0àtiy : Dàrayavaus :х3йуайуа : pa
3489:38 уй : XIV : тапса : Sakata : dha : yadiy : udapatatà ; hauv : kérahya : avaflü 39 : adurujiya : adam : Bardiya : amiy : һуа : Kürau$ : puça : Kabijiyahya : br
4527:15 manisiya : (айу : Xšayāršā : 16 xSdyafiya : manā : pita : Daraya 17 vauš : Darayavahaus : pita : Vis 18 táspa : лаша : tha : Vistaspahy 19 à : pita : Ársàma : nàma : dha : а 20 tà : Vistàspa : uta : Arsima : 21 ubà : ajivatam : aciy : Auramaz 22 dim : ауада : ката : dha : Darayava 28 um : hya : mana : pita : avam : xš 21 dyafiyam : akunauš : ahyáyà :- 25 bümiyà : yafà : Dàrayavahaus : xš 26 ayaóiya : abava : vasiy : tya : табага 27 m :akunaus :байу : X sayársà 28 : xSayatiya : Darayavaus : puca : 29 aniyaiety : üáhatà : Auramazdàm 30 : ауада : Каша : dha : Darayavaus 31 : manā : pitä : pasă : tanüm : mim 82 : табат :akunauš : yabimaiy 83 : pita : Darayavaus : gàavà : а 34 Syava : vaSnà : Auramazdaha : ada 35 m : xSiyafiya : abavam : pica : gà 36 Gavi : уада : adam : xSàyafiya : a 37 bavam : vasiy : tya :frafaram : aku . 38 navam : tyamaty : pica : kartam : dha 39 : ауа : adam : apayaiy : utà : ani 40 ya : kartam : abijàvayam : tyapati 41 y : adam : akunavam : шашау : tya 42 : pita : akunauš :ava : visam : 43 vasna : Auramazdaha : akuma : 6 44 айу : XSayar8a : хӧдуабуа : 45 mim : Àuramazdà : patuy : utama 46 1y :xSacam : ша : tya : mana : kar 47 tam : uta : tyamaiy : pica : kartam 48 : avaSeiy : Auramazda : pütuv Nores то XPf: % Darayavahaus, for nom. -vaus; in the original draft, the М had been omitted in the gen. _ iu line 28, and when the error was noted the correction was made in the wrong occurrence of the word. ** On the accession of Xerxes, see Hist. App. V. TRANSLATION оғ XPf: $1. 1-8. ... (=XPa 1-6). $2. 8-15. ... (= XPa 6-11). $3. 15-27. Saith Xerxes the King: My father was Darius; Darius’s father was Hystaspes by name; Elystaspes’s father was Arsames by name. Both Hystaspes and Arsames were both living, at that time--thus unto Ahuramazda was the desire — Darius, who was my father, him he made king in this earth. When Darius became king, he built much excellent (construction).
5014:(2) Prefix with verb jav-, and first element in abicaris, abyapara, perhaps in Abirddus, but prob- ably not the base of abif. — —
5247:kam-bu-ai-ia, Gk. KayBvons (8111, $144.IV): ety- mology disputed (cf. Bthl. AiW 437; Charpentier, ZII 2.140-52). Kabūjiya nsm. DB 1.28, 30f, 31, 32, 33, 43. Kabijiyam asm. DB 1.45, 46. Kabüyyahyà gsm. CMb 1f; DB 1.29, 30, 39. Kabūjiyāä absm. DB 1.40.
5410:abi- + jav- caus. ‘promote, increase, add to’: abiyajüvayam 1st sg. imf. ($215) XPg 9; abijáva- yam (§23.1, $140.IIT) XPf 40.
=== TLM ===
```


## [2026-09-05T21:05:34.187Z] AGENT

Now I'll write the verification file.


## [2026-09-05T21:13:22.513Z] TOOL CALL #80: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build177.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW = \"https://en.wiktionary.org/wiki/\"\nE = \"https://www.etymonline.com/word/\"\n\ndoc = {\n  \"pdf_page\": 177,\n  \"book_page\": 147,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-05\",\n  \"entries\": []\n}\n\n# ------------------------------------------------------------------ entry 0\ne0 = {\n  \"entry\": 0,\n  \"root\": \"Gĕu 1, Gu; Keu 1, Keup, Kumb, Kub, Keub, Keuk 2\",\n  \"verdict\": \"confirmed\",\n  \"modern_form\": \"PIE *ǵēu-/*gēu-, *gəu-, *gū- 'to bend, curl; a kind of vessel' (Pokorny 393-398) and PIE *keu-2, *keu̯ə- 'to bend', with the extensions *keu-b-, *keu-p-, nasalised *kum-b(h)-, and o-grade *kouk- (Pokorny 588-592; Watkins/AHD keu-2)\",\n  \"note\": \"The root box is right on all counts, and the two Pokorny page ranges are Nourai's own two lemmata: Pokorny's 'geu-, gəu-, gu- : to bend, curl; a kind of vessel' is printed 'Page(s): 393-398' (Nourai writes 394-398, one page short at the front), and 'keu-2, keu̯ə- : to bend' is printed 'Page(s): 588-592', exactly Nourai's second citation. All six of the sub-lemmas Nourai lists as variants are Pokorny's own subsections of keu-2: 'B. guttural extensions ... keu-g-', 'C. I. keu-p-', 'C. II. keu-bh-', 'D. Nasalized kum-bh-, mostly kum-b-', and Watkins's 'II. Extended o-grade form *kouk-' (Nourai's 'Keuk 2'). Watkins glosses the root exactly as Nourai does: 'keu-2. Base of various loosely related derivatives with assumed basic meaning \\\"to bend,\\\" whence \\\"a round or hollow object.\\\"' Two cautions the chart does not raise. (1) The Latin/Greek vessel words at the bottom of the tree are suspect as inherited IE material: de Vaan (via Etymonline s.v. cup) holds that Latin cupa and its relatives 'all probably are from a non-IE loanword *kup- which was borrowed by and from many languages', and Beekes (via Etymonline s.v. cymbal) calls Greek kymbē a Wanderwort. (2) The Iranian branch (kaofa, xumba) is beyond doubt: Buck 4.16 puts 'Av. kaofa- \\\"mountain peak, camel's hump\\\", OPers. kaufa \\\"mountain\\\" (NPers. kūh)' with 'Lith. kaupas, ChSl. kupŭ, NE heap, NHG haufe' under 'IE *keup-, *keub-, *keubh- in words for \\\"bend, curve\\\"'. The chart also has one blank, unlabelled box to the right of node #4 on the printed page (p.147); it is empty in the book too, so nothing is missing from the extraction.\",\n  \"note_fa\": \"ریشهٔ نمودار درست است. پوکورنی دو مادهٔ جداگانه دارد: geu-/gəu-/gū- «خم کردن، پیچاندن؛ نوعی ظرف» در صفحات ۳۹۳–۳۹۸ (نورایی ۳۹۴–۳۹۸ نوشته که یک صفحه کمتر است) و keu-2, keu̯ə- «خم شدن» در صفحات ۵۸۸–۵۹۲ که دقیقاً همان ارجاع دوم اوست؛ همهٔ گونه‌های Keup و Kumb و Kub و Keub در همان مادهٔ دوم زیرِ عنوان‌های «گسترش لبی» و «صورت خیشومی kum-b(h)-» آمده و Keuk 2 همان *kouk- واتکینز است. بارتولومه، پوکورنی، والده‌ـ‌پوکورنی و باک همگی kaofa اوستایی و kūh فارسی و heap انگلیسی را زیر همین ریشه می‌آورند، پس شاخهٔ ایرانی استوار است. تنها هشدار پژوهش امروزی دربارهٔ شاخهٔ لاتینی‌ـ‌یونانی است: دخافان (de Vaan) واژهٔ لاتینی cūpa و بیکس (Beekes) واژهٔ یونانی kymbē را وام‌واژه‌ای سرگردان و احتمالاً غیرهندواروپایی می‌دانند.\",\n  \"sources\": [E+\"cup\", E+\"cymbal\"],\n  \"ref_check\": [\n    {\"ref\": \"POK:394-398\", \"status\": \"partial\", \"note\": \"POK_full.txt: 'Root / lemma: geu-, gau-, gu- ... Meaning: to bend, curl; a kind of vessel ... References: WP. I 555 ff. ... Page(s): 393-398' — the lemma and gloss are exactly Nourai's, but Pokorny prints the range as 393-398, not 394-398.\"},\n    {\"ref\": \"POK:588-592\", \"status\": \"supports\", \"note\": \"POK_full.txt: 'Root / lemma: keu-2, keua- / Meaning: to bend ... Page(s): 588-592', with the sub-sections 'C. I. keu-p-', 'C. II. keu-bh-', 'D. Nasalized kum-bh-, mostly kum-b-' that give Nourai's Keup / Kumb / Kub / Keub.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.v. keu-2\", \"stance\": \"supports\", \"note\": \"'keu-2. Base of various loosely related derivatives with assumed basic meaning \\\"to bend,\\\" whence \\\"a round or hollow object.\\\" I. Extended forms *keub-, *keup- ... 5 ... c. nasalized form *ku-m-b- ... II. Extended o-grade form *kouk- ... [Pok. 2. keu- 588.]'\"},\n    {\"src\": \"WLD\", \"where\": \"Bd. I pp. 370-376 (WLD_Bd1_pages.txt), running head 'qeu-'\", \"stance\": \"supports\", \"note\": \"Walde-Pokorny I 372 f.: 'Bedeutungsgruppe \\\"Wölbung nach oben, Haufe u. dgl.\\\": Apers. kaufa- \\\"Berg\\\", av. kaofa- \\\"ds.; Kamelbuckel\\\", np. kōh \\\"Berg\\\" ... lit. kaupas \\\"Haufen\\\" = abg. kupŭ'; p.376: 'Nasaliert qum-bh-, meist qum-b-'.\"},\n    {\"src\": \"SYN\", \"where\": \"Buck 4.16 'hill' (SYN.txt l.997)\", \"stance\": \"supports\", \"note\": \"'Here also Av. kaofa- \\\"mountain peak, camel's hump\\\", OPers. kaufa \\\"mountain\\\" (NPers. kūh \\\"mountain\\\") : Lith. kaupas, ChSl. kupŭ, NE heap, NHG haufe \\\"heap\\\", Grk. κυφός \\\"bent\\\", all fr. IE *keup-, *keub-, *keubh- in words for \\\"bend, curve\\\". Walde-P. 1.372 ff.'\"},\n    {\"src\": \"IEC\", \"where\": \"Mann col. s.v. kumbos (IEC.txt l.8374)\", \"stance\": \"supports\", \"note\": \"'kumbos, ā \\\"hump, dome, hollow, basin, bellied pot\\\" ... Av. xumbo (\\\"pot\\\") ; Per. xum \\\"jar\\\" ... Gk. kúmbos \\\"hollow; pot\\\"; kúmbē ... Du. homp; LG humpe; EME hump'.\"}\n  ],\n  \"nodes\": []\n}\n\ne0[\"nodes\"].append({\n  \"id\": 1, \"lang\": \"Avestan\", \"words\": \"kaofa; xumba\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"Both Avestan words are real and belong here. Av. kaofa- m. is 'mountain ridge, range' and, in compounds, the camel's 'hump' (Bartholomae AiW s.v.: \\\"j. kaofa-, p. kaufa- m. 1) 'Bergrücken, Höhenzug' ... 2) 'Höcker' des Kamels (nur Komp.)\\\", e.g. saēni.kaofa- 'with a straight, stiff hump' of the camel, Yt 14.13, V 22.3); it continues PIE *keup- 'curvature upwards, heap' with the regular Iranian development *p > f before a consonant-final stem, and has an exact Old Persian twin kaufa- 'mountain' (DB). Av. xumba- m. is 'pot, pot-shaped device' (V 8.84-85, of the potter's and the glass-maker's kiln); it goes back to the nasalised extension *kum-bʰ- and is the exact equivalent of Sanskrit kumbhá- 'pot, jar' and of Greek kymbē 'bowl', the initial aspirate x- being the Iranian reflex of the Indo-Iranian voiceless aspirate. Nourai's gloss 'bent container, pot' renders Pokorny's 'Topf, Vertiefung' well enough. Only the two glosses are slightly shuffled: 'mountain' is the primary sense of kaofa- and 'hump' the compound sense, whereas the chart uses kaofa- as the ancestor of both kūh and kohān below.\",\n  \"derivation_fa\": \"هر دو واژهٔ اوستایی درست‌اند. kaofa- در اوستا «کوه، رشته‌کوه» است و در ترکیب‌ها «کوهانِ شتر» (بارتولومه: «Bergrücken, Höhenzug ... Höcker des Kamels (nur Komp.)»، مانند saēni.kaofa- در یشت ۱۴٫۱۳)، و همتای دقیق آن در پارسی باستان kaufa- «کوه» است؛ این صورت از *keup- هندواروپایی «برآمدگی، توده» می‌آید و پ ایرانی باستان پیش از پایانهٔ صامت به f بدل شده است. xumba- اوستایی «خم، دیگ، دستگاه خم‌مانند» (وندیداد ۸٫۸۴–۸۵ دربارهٔ کورهٔ سفالگری و شیشه‌گری) از صورت خیشومی‌شدهٔ *kum-bʰ- است و برابر دقیق kumbhá- سنسکریت و kymbē یونانی؛ خ آغازین بازتاب ایرانی همخوان دمیدهٔ بی‌واک هندوایرانی است. ادعای نورایی درست است.\",\n  \"sources\": [W+\"%DA%A9%D9%88%D9%87\"],\n  \"ref_check\": [\n    {\"ref\": \"POK:591,592\", \"status\": \"supports\", \"note\": \"POK_full.txt l.46944: 'Apers. kaufa- \\\"mountain\\\", Avestan kaofa- \\\"ds.; camel hump\\\", npers. koh \\\"mountain\\\"' (p.591); l.46980-82: 'Old Indic kumbha- m. \\\"pot, pan, crock, pitcher\\\" ... = Avestan xumba- m. \\\"pot, pan; extension\\\", npers. xumb, xum \\\"pot\\\"' (p.592).\"},\n    {\"ref\": \"KLN:391\", \"status\": \"supports\", \"note\": \"KLN_1966.txt leaf 216 (printed page marker '392'; the leaf carries pp.391-392) s.v. cymbal: 'fr. L. cymbalum, fr. Gk. κύμβαλον, fr. κύμβη ... fr. I.-E. base *qumb-, \\\"to bend, curve\\\", whence also OI. kumbháḥ \\\"pot, jar\\\", Avestic xumba, of s.m.' — Klein's page 391 really does carry the Avestan xumba.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"BRT\", \"where\": \"AiW s.vv. kaofa-, xumba- (BRT.txt ll.8940, 10557)\", \"stance\": \"supports\", \"note\": \"'j. kaofa-, p. kaufa- m. 1) \\\"Bergrücken, Höhenzug\\\" ... 2) \\\"Höcker\\\" des Kamels (nur Komp.)'; 'j. xumba- m. \\\"Topf, topfähnliche Vorrichtung\\\": V. 8.84 ... V. 8.85'.\"},\n    {\"src\": \"WLD\", \"where\": \"Bd. I 372 and 376\", \"stance\": \"supports\", \"note\": \"'Apers. kaufa- \\\"Berg\\\", av. kaofa- \\\"ds.; Kamelbuckel\\\", np. kōh \\\"Berg\\\"'; 'ai. kumbha-ḥ \\\"Topf, Krug\\\" ... = av. xumba- m. \\\"Topf, Vertiefung\\\", np. xumb, xum \\\"Topf, Krug\\\"'.\"},\n    {\"src\": \"IEC\", \"where\": \"Mann s.v. kumbos\", \"stance\": \"supports\", \"note\": \"'Av. xumbo (\\\"pot\\\", < *-b- or *-bh-); Per. xum \\\"jar, alembic\\\"'.\"}\n  ]\n})\n\ne0[\"nodes\"].append({\n  \"id\": 2, \"lang\": \"Pahlavi\", \"words\": \"kôf; xombak\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"Middle Persian kōf [kwp] 'hill, mountain; hump' is MacKenzie's own entry, with the Manichaean form kōf and the New Persian outcome kōh given in the same line; it is Av. kaofa-/OP kaufa- with regular loss of the Old Iranian thematic ending and with -f- preserved. The diminutive kōfak 'mountain, hump' is likewise attested (Horn no. 875 lists 'phlv. kōf, kōfak \\\"Berg, Höcker\\\"'), and it is kōfak, not kōf, that underlies NP کوهه/کوهان. Pahlavi xumb [hwmb'] 'jug, pitcher' (MacKenzie; Manichaean xwmb) continues Av. xumba- unchanged apart from the loss of the ending; Nourai's 'xombak' is the -ak diminutive xumbag, which is attested in the Pahlavi version of the Avesta (Bartholomae quotes the Pahlavi gloss 'kē dēvān xumbak'). So both Pahlavi forms are real; the vowel of Nourai's transcription (xombak for xumbak) is the New-Persian-style o for MP u that he uses throughout.\",\n  \"derivation_fa\": \"کوفِ فارسی میانه [kwp] «کوه، تپه، کوهان» در فرهنگ مکنزی با همین معنا آمده و دنبالهٔ kaofa اوستایی و kaufa پارسی باستان است؛ f میانی حفظ شده و پایانهٔ ستاکی افتاده است. صورت مصغّر kōfak نیز در پهلوی هست (هرن، شمارهٔ ۸۷۵: «phlv. kōf, kōfak»)، و همین kōfak است که به «کوهه/کوهان» فارسی نو رسیده. xumb پهلوی «خم، کوزه» (مکنزی؛ مانوی xwmb) دنبالهٔ xumba اوستایی است و صورت مصغّر آن xumbag/xumbak در ترجمهٔ پهلوی اوستا گواهی شده (بارتولومه: «kē dēvān xumbak»). پس هر دو صورت پهلوی درست‌اند و «xombak» نورایی همان xumbak است با املای فارسی‌نوی o به جای u.\",\n  \"sources\": [W+\"%D8%AE%D9%85\"],\n  \"ref_check\": [\n    {\"ref\": \"HRN:195\", \"status\": \"supports\", \"note\": \"HRN.txt leaf 216 (printed p.195), entry '875. kōh \\\"Berg\\\", kōhe \\\"Höcker\\\". ... ap. kaufa- \\\"Berg\\\"; aw. kaofa- \\\"Berg, Höcker\\\"; phlv. kōf, kōfak \\\"Berg, Höcker\\\"' — exactly Nourai's Avestan > Pahlavi > Persian chain.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"PHD\", \"where\": \"MacKenzie 1971 p.51 s.vv. kōf, xumb (PHD.txt ll.428, 661)\", \"stance\": \"supports\", \"note\": \"'kōf [kwp | = M, N kōh] hill, mountain; hump. ~ag [-k' | N kōha] saddle'; 'xumb [hwmb' | M xwmb, N ~] jug, pitcher'.\"},\n    {\"src\": \"BRT\", \"where\": \"AiW s.v. xumba-, Pahlavi gloss (BRT.txt l.10535)\", \"stance\": \"supports\", \"note\": \"Bartholomae quotes the Pahlavi rendering 'kē dēvān xumbak' — the -ak diminutive Nourai prints as xombak.\"},\n    {\"src\": \"NYB\", \"where\": \"Nyberg II, glossary\", \"stance\": \"silent\", \"note\": \"grep of NYB_vol2_glossary.txt for kōf / xumb returns nothing; Nyberg's glossary is limited to the texts of Part I and does not contain either word.\"}\n  ]\n})\n\ne0[\"nodes\"].append({\n  \"id\": 3, \"lang\": \"Persian\", \"words\": \"kŭh «کوه»; kohân «کوهان»; xom «خُم ۱» (extra: کوهه ؛ خمره)\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"کوه kūh 'mountain' is MP kōf with the regular New Persian change of postvocalic/final -f to -h (kōf > kōh), the same change as in NP روباه < MP rōbāh: Wiktionary traces it 'from Middle Persian kōf, from Old Persian 𐎣𐎢𐎳 (kaufa), from Proto-Iranian *káwfš, from PIE *kewHp-'. کوهان kohān 'camel's hump' and کوهه kuha 'hump, back of an elephant' are Persian derivatives of the same stem: Mo'in's footnote in Borhān at the very page Nourai cites derives kohān as 'از: کوه + ان (پسوند)' beside 'پهلوی kaofa; kōfak (کوه، کوهان)', and Horn no. 875 already had 'kōhe \\\"Höcker\\\"'. خم xom 'large jar' continues MP xumb (Classical Persian خنب/خمب xunb/xomb, still with the -b), the -mb cluster simplifying to -m in later New Persian; خمره xomre is its -a diminutive. Ferdowsī's line quoted in the chart, 'نهادند بر کوههٔ پیل کوس', is a genuine attestation of کوهه in the sense 'the hump/back of the elephant'.\",\n  \"derivation_fa\": \"«کوه» از فارسی میانهٔ kōf است و f پایانی در فارسی نو به ه بدل شده (kōf > kōh)، همان دگرگونی که در «روباه» از rōbāh دیده می‌شود؛ ویکی‌واژه نیز آن را از kōf پهلوی، از kaufa پارسی باستان و از *kewHp- هندواروپایی می‌گیرد. «کوهان» و «کوهه» ساخته‌های فارسی از همین ستاک‌اند؛ حاشیهٔ معین در برهان قاطع، درست در همان صفحه‌ای که نورایی ارجاع می‌دهد، «کوهان» را «از: کوه + ان (پسوند)» و کنار «پهلوی kaofa؛ kōfak (کوه، کوهان)» می‌آورد و هرن هم پیشتر kōhe «کوهان» را ثبت کرده بود. «خم» دنبالهٔ xumb پهلوی است (در فارسی کلاسیک هنوز «خنب/خمب») که خوشهٔ -mb در فارسی نو به م ساده شده، و «خمره» مصغّر آن است. بیت فردوسی که در نمودار آمده گواه راستین کاربرد «کوهه» است. ادعای نورایی درست است.\",\n  \"sources\": [W+\"%DA%A9%D9%88%D9%87\", W+\"%D8%AE%D9%85\"],\n  \"ref_check\": [\n    {\"ref\": \"BQT:1739\", \"status\": \"supports\", \"note\": \"BQT_v3_pages.txt [pdf page 536] = printed 1739 (running head ۱۷۳۷ two pages earlier), headwords کوه / کوهان with Mo'in's footnotes: 'پهلوی kōf (کوه، قلهٔ کوه)؛ ایرانی باستان *kaufa ... اوستا kaofa (کوه، کوهان)، پارسی باستان kaufa (کوه)، پهلوی نیز kōfak' and 'از: کوه + ان (پسوند): پهلوی kaofa؛ kōfak (کوه، کوهان)'.\"},\n    {\"ref\": \"BQT:768\", \"status\": \"partial\", \"note\": \"BQT_v2_pages.txt leaf 228 (printed p.768, offset +540) carries خم، خمدان، خمره، خمستان، خمخانه — the headwords are there, but on this page Mo'in's footnotes are only cross-references ('خنب = (ه.م) خم (ه.م)'، 'از: خم + چه (پسوند تصغیر)'), so the page attests the word but carries no Avestan etymology.\"},\n    {\"ref\": \"WLD1:376\", \"status\": \"supports\", \"note\": \"WLD_Bd1_pages.txt, page with running head '376 qeu- — ken-': 'ai. kumbha-ḥ \\\"Topf, Krug\\\" ... = av. xumba- m. \\\"Topf, Vertiefung\\\", np. xumb, xum \\\"Topf, Krug\\\" (diese mit ar. Tenuis asp.)' — precisely the xumba > xum line Nourai draws.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"HRN\", \"where\": \"no. 875, p.195\", \"stance\": \"supports\", \"note\": \"'kōh \\\"Berg\\\", kōhe \\\"Höcker\\\" ... ap. kaufa-; aw. kaofa-; phlv. kōf, kōfak'.\"},\n    {\"src\": \"PHD\", \"where\": \"MacKenzie p.51\", \"stance\": \"supports\", \"note\": \"'kōf [kwp | = M, N kōh]'; 'xumb [hwmb' | M xwmb, N ~] jug, pitcher' — MacKenzie himself gives the New Persian outcomes.\"},\n    {\"src\": \"SYN\", \"where\": \"Buck 4.16\", \"stance\": \"supports\", \"note\": \"'Av. kaofa- \\\"mountain peak, camel's hump\\\", OPers. kaufa \\\"mountain\\\" (NPers. kūh \\\"mountain\\\")'.\"}\n  ]\n})\n\ne0[\"nodes\"].append({\n  \"id\": 4, \"lang\": \"Avestan\", \"words\": \"kava; fra-kava; apa-kava\",\n  \"verdict\": \"plausible\",\n  \"derivation\": \"The two compounds are genuine and are precisely Pokorny's evidence for the bare root: 'Material: The f[ull] root in Old Indic kora- m. \\\"movable joint\\\"; Avestan fra-, apa-kava- \\\"vorn, hinten buckelig\\\"'. Bartholomae has both as headwords: apa-kava- 'having a hump behind, on the back' (Yt 5.93; and as a noun, the name of that defect, Vd 2.29, in Yima's list of bodily blemishes barred from the vara) and fra-kava- 'having a hump in front, on the chest' (same passages). What is not right is the first word of the box: a simplex Avestan kava- 'humped' is not attested — Bartholomae records only the two prefixed compounds, and the only free-standing Avestan kava- is kavi-/kauua- 'seer, prince' (an unrelated word, PIE *kewh₁- 'to perceive'). So the node is correct except that its head-form kava- is an abstraction from the compounds rather than an attested Avestan word, and Nourai gives no derivative of it, which leaves the box a dead end in the chart.\",\n  \"derivation_fa\": \"دو ترکیب fra-kava- «دارای کوهان در جلو، بر سینه» و apa-kava- «دارای کوهان در پشت» راستین‌اند و همان گواهی‌اند که پوکورنی برای این ریشه می‌آورد؛ بارتولومه هر دو را با نشانی یشت ۵٫۹۳ و وندیداد ۲٫۲۹ (فهرست عیب‌های تنی در ورِ جمشید) ثبت کرده است. اما kava- ساده به معنای «کوهان‌دار» در اوستا گواهی نشده و بارتولومه تنها همان دو ترکیب پیشوندی را می‌آورد؛ تنها kava-/kauua- آزادِ اوستایی همان kavi- «کَی، شهریار، بیننده» است که ریشهٔ دیگری دارد. پس این خانه با احتیاط پذیرفتنی است: ترکیب‌ها درست‌اند ولی صورت سادهٔ سرِ خانه انتزاعی است، نه واژه‌ای گواهی‌شده.\",\n  \"sources\": [],\n  \"ref_check\": [\n    {\"ref\": \"POK:395,588\", \"status\": \"supports\", \"note\": \"POK_full.txt, lemma keu-2 (pp.588-592), first line of the Material: 'Avestan fra-, apa-kava- \\\"vorn, hinten buckelig\\\"' — verbatim Nourai's two compounds; p.395 is inside the geu- lemma to which Pokorny explicitly cross-refers ('Numerous parallel formations from the root geu-').\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"BRT\", \"where\": \"AiW s.vv. apa-kava-, fra-kava- (BRT.txt ll.3496, 17540)\", \"stance\": \"partial\", \"note\": \"'j. apa-kava- 1) Adj. \\\"der hinten, auf dem Rücken einen Höcker hat\\\" ... Yt 5.93. 2) m. Name für solches Gebrechen ... V. 2.29'; 'j. fra-kava- 1) Adj. \\\"der vorn, auf der Brust einen Höcker hat\\\"' — the compounds are there, a simplex kava- 'humped' is not.\"},\n    {\"src\": \"WLD\", \"where\": \"Bd. I 370 ff. (qeu-)\", \"stance\": \"supports\", \"note\": \"Walde-Pokorny carries the same material as Pokorny's keu-2, of which this line is the opening evidence.\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. keu-2\", \"stance\": \"silent\", \"note\": \"Watkins lists only the words with English descendants; the Avestan compounds do not appear.\"}\n  ]\n})\n\ne0[\"nodes\"].append({\n  \"id\": 5, \"lang\": \"Latin\", \"words\": \"cuppa; cymbalon\",\n  \"verdict\": \"transcription_suspect\",\n  \"derivation\": \"cuppa is right: Latin cūpa 'tub, cask, vat' (from *kūp-ā, the zero-grade *kup- of Pokorny's keu-p-) has beside it the Late Latin/Romance expressive doublet cuppa 'drinking vessel, goblet' — Pokorny p.591: 'Latin cūpa f. \\\"cask, butt\\\", roman. also \\\"bath\\\" (besides gloss. and roman. cuppa \\\"goblet\\\", seems late short form with consonant doubling)'; Watkins: 'expressive form *kupp- in Late Latin cuppa, drinking vessel: CUP'. cymbalon is not Latin. The word is Greek κύμβαλον, from κύμβη 'bowl, drinking cup, boat'; Latin borrowed it as cymbalum (with -um, not -on), and it is from that Latin form that Old English cymbal and Old French cymbale come. Nourai's own cited authority says so: Klein p.391 (his KLN:391 on node #1) has 'cymbal ... fr. L. cymbalum, fr. Gk. κύμβαλον, fr. κύμβη'; so do Walde-Pokorny I 376 ('gr. κύμβη ... κύμβαλον, meist Pl. \\\"cymbalum\\\"') and Watkins, who files CYMBAL under 'Greek kumbē, boat, bowl'. The printed page (p.147) really does show 'cymbalon : curved-in plate' inside the box headed 'Latin', so the extraction is faithful and the misattribution — both the -on ending and the language label — is the book's.\",\n  \"derivation_fa\": \"بخش نخست درست است: cūpa لاتینی «خمره، بشکه» از درجهٔ صفرِ *kup- می‌آید و همزادِ دیرینِ آن در لاتینی متأخر و زبان‌های رومی cuppa «جام» است (پوکورنی ۵۹۱؛ واتکینز: «صورت تأکیدی *kupp- در لاتینی متأخر cuppa»). ولی cymbalon لاتینی نیست: این واژه یونانی است (κύμβαλον از κύμβη «کاسه، پیاله») و لاتینی آن را به صورت cymbalum وام گرفته است. خودِ کلاین که نورایی به او ارجاع می‌دهد در صفحهٔ ۳۹۱ می‌نویسد «cymbal ... از لاتینی cymbalum، از یونانی κύμβαλον، از κύμβη»، و والده‌ـ‌پوکورنی و واتکینز هم همین را می‌گویند. تصویر صفحهٔ چاپی نشان می‌دهد که کتاب خود «cymbalon» را در خانهٔ «Latin» آورده است؛ پس خطا از چاپِ کتاب است نه از خوانش اسکن.\",\n  \"error_in\": \"book\",\n  \"book_prints\": \"cymbalon : curved-in plate (inside the box labelled 'Latin')\",\n  \"correct_form\": \"Greek κύμβαλον kymbalon (Latin cymbalum)\",\n  \"sources\": [E+\"cymbal\", E+\"cup\"],\n  \"ref_check\": [\n    {\"ref\": \"AHD\", \"status\": \"partial\", \"note\": \"AHD_watkins1985.txt s.v. keu-2: '4 ... c. expressive form *kupp- in Late Latin cuppa, drinking vessel: CUP' — supports cuppa; but the cymbal words are filed under '(ii) Greek kumbē, boat, bowl: (CEMBALO), (CHIME), CYMBAL, CYMBIDIUM', i.e. Watkins makes them Greek, not Latin.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"Klein p.391 s.v. cymbal\", \"stance\": \"contradicts\", \"note\": \"'cymbal, n. ... fr. OE. cymbal and MF. (= F.) cymbale, which both derive fr. L. cymbalum, fr. Gk. κύμβαλον, fr. κύμβη, \\\"the hollow of a vessel, cup, boat\\\", fr. I.-E. base *qumb-'.\"},\n    {\"src\": \"WLD\", \"where\": \"Bd. I 376\", \"stance\": \"contradicts\", \"note\": \"'gr. κύμβη \\\"Becken, Schale, Kahn\\\", κύμβος \\\"Gefäß\\\"; κύμβιον ... κύμβαλον, meist Pl. \\\"cymbalum, Becken, das mit einem andern zusammengeschlagen einen gellenden Ton gibt\\\"' — the -on form is expressly Greek.\"},\n    {\"src\": \"POK\", \"where\": \"p.591 (keu-p-)\", \"stance\": \"supports\", \"note\": \"'Latin cupa f. \\\"cask, butt\\\" ... (besides gloss. and roman. cuppa \\\"goblet\\\", seems late short form with consonant doubling)'.\"},\n    {\"src\": \"IEC\", \"where\": \"Mann s.v. kumbolos (2)\", \"stance\": \"contradicts\", \"note\": \"'kumbolos, om (2) \\\"vessel\\\" ... Gk. kúmbalon \\\"basin\\\"' — Mann too lists the form as Greek.\"}\n  ]\n})\n\ne0[\"nodes\"].append({\n  \"id\": 6, \"lang\": \"Arabic\", \"words\": \"koab; akvâb; sanj\",\n  \"verdict\": \"disputed\",\n  \"derivation\": \"Two different claims are packed into this box. (a) Arabic كوب kūb 'cup, beaker', pl. أكواب akwāb (Qur'ān 43:71, 56:18, 76:15, 88:14), is indeed the Latin cup-word, but not taken straight from Latin: Wiktionary gives the chain Latin cūpa > Late Latin cuppa > Byzantine Greek κοῦπα koûpa > Aramaic כובא kūbā > Arabic كوب, i.e. the word reached Arabic overland through Syriac-speaking Christian Mesopotamia in the pre-Islamic centuries, which is why it is already Qur'ānic. Nourai's transliteration 'koab' is not a possible reading of كوب (kūb) and is a misprint or an idiosyncratic rendering; the printed page does show 'koab'. (b) Arabic صنج ṣanj 'cymbal' does not come from Latin/Greek cymbalum at all in the modern account: it is a loan from Iranian, from Middle Persian čang / New Persian چنگ 'harp' (Wiktionary), and Nourai's own reference al-ʿUnaysī (TAD) says the same, deriving it from Persian سنج. The route Latin > Arabic ṣanj is therefore rejected, and with it the second half of the box.\",\n  \"derivation_fa\": \"این خانه دو ادعای جداگانه دارد. یکم، «کوب» عربی (جمع «أکواب»، در قرآن ۴۳:۷۱ و ۵۶:۱۸ و ۸۸:۱۴) به‌راستی همان واژهٔ لاتینی است، اما نه مستقیم: زنجیرهٔ پذیرفته‌شده cūpa لاتینی ← cuppa لاتینی متأخر ← κοῦπα یونانی بیزانسی ← כובא آرامی/سریانی ← «کوب» عربی است، یعنی وام‌گیری از راه بین‌النهرینِ سریانی‌زبان پیش از اسلام؛ آوانگاشت «koab» هم خوانشِ درستِ کوب نیست. دوم، «صنج» عربی از cymbalum لاتینی نیامده است؛ پژوهش امروزی آن را وام‌واژه‌ای ایرانی از čang فارسی میانه / «چنگ» فارسی می‌داند و خودِ مأخذِ نورایی (طوبیا العنیسی) آن را «تحریفِ سنجِ فارسی» می‌خواند. پس نیمهٔ دوم این خانه را پژوهش امروزی رد می‌کند.\",\n  \"sources\": [W+\"%D9%83%D9%88%D8%A8\", W+\"%D8%B5%D9%86%D8%AC\", E+\"cup\"],\n  \"ref_check\": [\n    {\"ref\": \"ARK:223\", \"status\": \"not_checked\", \"note\": \"ARK = Rokn-zadeh Adamiyyat, Arkān-e Sokhan (1347/1968); refs_online.json records 'Not found ... nothing digitised on any permitted platform', so this page cannot be checked.\"},\n    {\"ref\": \"TAD:44\", \"status\": \"contradicts\", \"note\": \"TAD_pages.txt leaf 47, s.v. صنج: 'الظاهر أن لفظ صنج ج صنوج هو تحريف [عن] «سنج» الفارسي معناه الوازن ...' — al-ʿUnaysī derives Arabic ṣanj from PERSIAN sanj, the reverse of the Latin > Arabic arrow drawn here (and of the Arabic > Persian arrow of node #7).\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"Klein p.391 s.v. cymbal\", \"stance\": \"silent\", \"note\": \"Klein's cymbal article traces the Greek and Latin line and the Germanic hump-words but knows no Arabic ṣanj.\"},\n    {\"src\": \"PLA\", \"where\": \"Asbaghi 1988 (PLA_pages.txt)\", \"stance\": \"silent\", \"note\": \"greps for صنج / كوب / 'Zimbel' in the OCR return nothing usable; the Arabic script in this scan is badly garbled, so Asbaghi could not be read on either word.\"},\n    {\"src\": \"FVQ\", \"where\": \"Jeffery 1938 (FVQ_pages.txt)\", \"stance\": \"silent\", \"note\": \"grep for akwāb / kūb finds no entry; Jeffery does not treat كوب among the Qur'ānic foreign words.\"},\n    {\"src\": \"MON\", \"where\": \"Mo'in s.v. صنج (MON_part1.txt l.90266)\", \"stance\": \"contradicts\", \"note\": \"'صنج [معر. سنج، قس. چنگ] (اِ.) چنگ ...' — Mo'in marks Arabic ṣanj as the Arabicised (معرّب) form of Persian sanj, cf. čang.\"}\n  ]\n})\n\ne0[\"nodes\"].append({\n  \"id\": 7, \"lang\": \"Persian\", \"words\": \"akvâb «اکواب»; sanj «صنج» (extra: سنج)\",\n  \"verdict\": \"disputed\",\n  \"derivation\": \"اکواب akvāb in Persian is a genuine Arabic-mediated round trip: the Latin/Greek cup-word entered Arabic as كوب, formed the broken plural أكواب there, and the plural was then taken into literary (mainly Qur'ānic-religious) Persian as اکواب 'cups, goblets' — the singular کوب never established itself, which is why Persian has only the plural. That half of the box is sound. صنج/سنج is the opposite case: the word is Iranian and travelled Persian > Arabic, not Arabic > Persian. Mo'in's own dictionary, which Nourai cites here (MON), tags the entry 'صنج [معر. سنج، قس. چنگ]', i.e. 'ṣanj: Arabicised form of sanj, compare čang'; al-ʿUnaysī (TAD:44), also cited here, calls Arabic ṣanj 'a corruption of the Persian sanj'; and Wiktionary derives Arabic صنج from Middle Persian čang 'harp'. Persian سنج is thus the source, and the spelling صنج in Persian is simply the Arabicised orthography returning home. Nourai's own NOTE ('See root \\\"Keg\\\" for another possible derivation') shows he knew the derivation was contested; modern scholarship takes the other side.\",\n  \"derivation_fa\": \"«اکواب» در فارسی نمونهٔ روشنی از رفت‌وبرگشتِ عربی‌میانجی است: واژهٔ لاتینی‌ـ‌یونانی به عربی «کوب» شد، جمع مکسّر «أکواب» در عربی ساخته شد و همان جمع به فارسی ادبی (بیشتر در بافت قرآنی) وارد شد؛ مفرد «کوب» در فارسی جا نیفتاد و به همین سبب فارسی تنها جمع را دارد. اما «صنج/سنج» وارونهٔ این است: واژه ایرانی است و از فارسی به عربی رفته، نه برعکس. خودِ معین که نورایی به او ارجاع می‌دهد می‌نویسد «صنج [معر. سنج، قس. چنگ]» و العنیسی هم آن را «تحریفِ سنجِ فارسی» می‌خواند؛ ویکی‌واژه نیز عربیِ صنج را از čang فارسی میانه می‌گیرد. پس نیمهٔ نخستِ این خانه درست و نیمهٔ دومش را پژوهش امروزی رد می‌کند و جهت وام‌گیری را وارونه می‌داند.\",\n  \"sources\": [W+\"%D8%B5%D9%86%D8%AC\", W+\"%D9%83%D9%88%D8%A8\"],\n  \"ref_check\": [\n    {\"ref\": \"MON:332,1336\", \"status\": \"contradicts\", \"note\": \"Mo'in's lexicon s.v. صنج (MON_part1.txt l.90266): 'صنج [معر. سنج، قس. چنگ] (اِ.) چنگ. ... فلزی که به وسیلهٔ بندی به انگشتان پیوندد' — the bracketed tag معر. ('Arabicised') makes Persian sanj the source, not the borrower. اکواب could not be located in the available Mo'in text files, so the first of the two page numbers is unverified.\"},\n    {\"ref\": \"TAD:44\", \"status\": \"contradicts\", \"note\": \"TAD_pages.txt leaf 47: 'الظاهر أن لفظ صنج ج صنوج هو تحريف [عن] «سنج» الفارسي' — Persian > Arabic, the reverse of the arrow.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"MON\", \"where\": \"s.v. صنج\", \"stance\": \"contradicts\", \"note\": \"see ref_check: '[معر. سنج، قس. چنگ]'.\"},\n    {\"src\": \"TAD\", \"where\": \"leaf 47 (ص section)\", \"stance\": \"contradicts\", \"note\": \"'تحريف «سنج» الفارسي معناه الوازن'.\"},\n    {\"src\": \"AFM\", \"where\": \"Addi Shir, al-Alfāẓ al-fārisiyya al-muʿarraba (AFM_pages.txt)\", \"stance\": \"silent\", \"note\": \"grep for صنج returns no entry in this OCR.\"},\n    {\"src\": \"KLN\", \"where\": \"Klein s.v. cymbal, p.391\", \"stance\": \"silent\", \"note\": \"no Semitic or Persian link is offered for the cymbal family.\"}\n  ]\n})\n\ne0[\"nodes\"].append({\n  \"id\": 8, \"lang\": \"English\", \"words\": \"cup, hump, cymbal\",\n  \"verdict\": \"disputed\",\n  \"derivation\": \"Two of the three are right and one is not. cup is OE cuppe/copp from Late Latin cuppa, itself from Latin cūpa 'tub, cask' (Etymonline; Watkins 'Late Latin cuppa, drinking vessel: CUP'), so it does descend from the box above it. cymbal is ME cimbal from OE cymbal and Old French cymbale, both from Latin cymbalum — so it too passes through Latin, though the Latin word is itself a borrowing from Greek κύμβαλον, and Latin is only a way-station. hump does not come from Latin at all: it is a late (1680s) borrowing from Low German, 'perhaps from Dutch homp \\\"lump\\\", from Middle Low German hump \\\"bump\\\"' (Etymonline), and Klein says the same — 'hump, n. ... Of LG. origin. Cp. MLG. hump ... Du. homp ... These words derive fr. I.-E. base *qumb-'. Pokorny p.592 likewise files 'engl. hump' among the Low German nasalised forms, not with Latin. So hump belongs under the root but under a Germanic parent (compare node #9), and the arrow Latin > hump is wrong.\",\n  \"derivation_fa\": \"دو واژه از سه واژهٔ این خانه درست است. cup از cuppe انگلیسی کهن و آن از cuppa لاتینی متأخر (از cūpa لاتینی) می‌آید، پس به‌راستی از خانهٔ بالا فرود آمده است. cymbal نیز از cymbalum لاتینی به انگلیسی کهن و فرانسهٔ کهن رسیده، هرچند خودِ لاتینی آن را از یونانی κύμβαλον وام گرفته و لاتینی تنها ایستگاه میانی است. اما hump هیچ پیوندی با لاتینی ندارد: وام‌واژه‌ای دیرهنگام (دههٔ ۱۶۸۰) از آلمانی سفلا/هلندی است — «شاید از homp هلندی، از hump آلمانی سفلای میانه» (اتیمانلاین)، و کلاین هم می‌گوید «of LG. origin». پوکورنی نیز در صفحهٔ ۵۹۲ hump انگلیسی را در کنار صورت‌های خیشومی آلمانی سفلا می‌آورد نه با لاتینی. پس این واژه زیر همین ریشه جای دارد ولی پدرِ درستش شاخهٔ ژرمنی است، نه لاتینی.\",\n  \"sources\": [E+\"hump\", E+\"cup\", E+\"cymbal\"],\n  \"ref_check\": [\n    {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Nourai gives no reference on this node; the AHD of the parent box (node #5) covers cup and cymbal but not hump.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"Klein s.v. hump (KLN_1966.txt l.18237) and cymbal (p.391)\", \"stance\": \"contradicts\", \"note\": \"'hump, n., a rounded protuberance. — Of LG. origin. Cp. MLG. hump, \\\"bump, hunch\\\", Du. homp, \\\"lump, chunk\\\", Norw. hump, \\\"knoll\\\". These words derive fr. I.-E. base *qumb-'.\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. keu-2\", \"stance\": \"partial\", \"note\": \"CUP and CYMBAL are listed (under Late Latin cuppa and Greek kumbē respectively); HUMP is not listed at all.\"},\n    {\"src\": \"POK\", \"where\": \"p.592 (D. Nasalized kum-b-)\", \"stance\": \"contradicts\", \"note\": \"'Norwegian humpr \\\"bumpiness, knag\\\" (ndd. loanword), engl. hump \\\"hump, hunchback\\\", ndd. humpe f. \\\"thick piece\\\" ... Dutch homp \\\"thick piece of bread\\\"' — the English word sits in the Low German group.\"}\n  ]\n})\n\ne0[\"nodes\"].append({\n  \"id\": 9, \"lang\": \"Germanic\", \"words\": \"haup\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"Proto-Germanic *haupaz 'heap' is the regular Germanic outcome of the zero/o-grade of Pokorny's keu-p-: PIE *koup-o- > Gmc *haupaz by Grimm's law (*k > *h, *p > *f, and the *-p- of the suffix preserved as -p- after the shift in the geminate/cluster environments), giving OE hēap, OS hōp, OHG houf/hufo, MLG hūpe, German Haufe. Watkins — the reference Nourai cites — has it in exactly these words: 'I. Extended forms *keub-, *keup-. 1. Germanic *haup- in: a. Old English hēap, heap: HEAP'. Pokorny p.592 lists the same set. Etymonline notes the OED's suspicion that OE hēap may rather belong with hēah 'high', and that some doubt the IE pedigree altogether, but that is a doubt about the root, not about the Germanic form.\",\n  \"derivation_fa\": \"*haupaz ژرمنی آغازین «توده، انبوه» بازتاب قاعده‌مندِ درجهٔ o/صفرِ *koup- هندواروپایی است: با قانون گریم k به h و p به f بدل شده و صورت‌های hēap انگلیسی کهن، hōp ساکسون کهن، houf/hufo آلمانی علیای کهن و Haufe آلمانی امروز از آن برآمده‌اند. واتکینز، یعنی همان مأخذی که نورایی ارجاع داده، عیناً می‌نویسد: «Germanic *haup- in Old English hēap: HEAP»، و پوکورنی هم در صفحهٔ ۵۹۲ همین مجموعه را می‌آورد. تنها تردید (به گفتهٔ اتیمانلاین از قول OED) در پیوند این خانواده با خودِ ریشه است نه در درستیِ صورت ژرمنی. ادعای نورایی درست است.\",\n  \"sources\": [E+\"heap\"],\n  \"ref_check\": [\n    {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt s.v. keu-2: 'I. Extended forms *keub-, *keup-. 1. Germanic *haup- in: a. Old English hēap, heap: HEAP; b. Dutch hoop, heap, troop: FORLORN HOPE.'\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"POK\", \"where\": \"p.592 (C. keu-b-/keu-p-)\", \"stance\": \"supports\", \"note\": \"'Old English hēap m. f., Old Saxon hōp, Old High German houf \\\"heap; troop, multitude, crowd\\\", Middle Low German hūpe, Old High German hufo, Modern High German Haufe'.\"},\n    {\"src\": \"SYN\", \"where\": \"Buck 4.16\", \"stance\": \"supports\", \"note\": \"'Lith. kaupas, ChSl. kupŭ, NE heap, NHG haufe \\\"heap\\\" ... all fr. IE *keup-, *keub-, *keubh-'.\"},\n    {\"src\": \"KLN\", \"where\": \"Klein s.v. heap\", \"stance\": \"supports\", \"note\": \"Klein's heap article assigns OE hēap to the same *qeup-/*qeub- base as the Lithuanian and Slavic heap-words.\"}\n  ]\n})\n\ne0[\"nodes\"].append({\n  \"id\": 10, \"lang\": \"English\", \"words\": \"heap, hip, high. height\",\n  \"verdict\": \"plausible\",\n  \"derivation\": \"All four English words belong under the root, but only the first descends from the Germanic form in the parent box. heap < OE hēap < Gmc *haupaz, exactly as drawn. hip < OE hype < Gmc *hupiz — a different, b-extension formation (Pokorny p.590: 'Gothic hups m. (stem hupi-), Old English hype m., Old High German huf f. \\\"hip, haunch\\\"'; Watkins: 'Germanic *hupiz in Old English hype, hip: HIP¹'). high < OE hēah < Gmc *hauhaz, and height < OE hēhthu/hēahthu < Gmc *hauhithō, both from the o-grade extension *kouk- (Watkins: 'II. Extended o-grade form *kouk-. 1. ... a. Germanic *hauhaz, \\\"arched,\\\" high, in Old English hēah, high: HIGH; b. Germanic *hauhithō in Old English hēhthu, hēahthu, height: HEIGHT'; this is Nourai's own 'Keuk 2' in the root box). So the root affiliation is right for all four and the immediate parentage is right for one; hip, high and height are siblings of *haupaz, not its children. The printed page also shows 'heap, hip, high. height' with a full stop where a comma belongs — the book's typo, faithfully extracted.\",\n  \"derivation_fa\": \"هر چهار واژه به این ریشه بازمی‌گردند، اما تنها یکی از خانهٔ بالای خود می‌آید. heap از hēap انگلیسی کهن و *haupaz ژرمنی است، درست همان‌گونه که در نمودار رسم شده. hip از hype انگلیسی کهن و *hupiz ژرمنی است، یعنی از گسترشِ b (پوکورنی ۵۹۰: «Gothic hups، Old English hype، Old High German huf»). high از hēah و height از hēhthu، هر دو از *hauhaz و *hauhithō ژرمنی و از درجهٔ o-ی *kouk- ــ همان «Keuk 2» که نورایی خود در خانهٔ ریشه آورده است. پس نسبت با ریشه برای هر چهار واژه درست است ولی پدرِ بی‌واسطه تنها برای heap درست است و سه واژهٔ دیگر خواهرانِ *haupaz‌اند نه فرزندان آن. در صفحهٔ چاپی هم «high. height» با نقطه به جای ویرگول آمده که خطای چاپیِ خودِ کتاب است و اسکن آن را درست خوانده.\",\n  \"sources\": [E+\"heap\"],\n  \"ref_check\": [\n    {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"no reference on this node; the parent's AHD citation covers heap, hip, high and height but assigns them to three different Germanic bases.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. keu-2\", \"stance\": \"partial\", \"note\": \"'1. Germanic *haup- ... Old English hēap: HEAP ... 3. Germanic *hupiz in Old English hype, hip: HIP¹ ... II. Extended o-grade form *kouk- ... Germanic *hauhaz ... HIGH; b. Germanic *hauhithō ... HEIGHT' — same root, three different Germanic bases.\"},\n    {\"src\": \"POK\", \"where\": \"pp.590, 591\", \"stance\": \"partial\", \"note\": \"'Gothic hups m. (stem hupi-), Old English hype m., Old High German huf f. \\\"hip, haunch\\\"' (keu-b-) and 'Middle High German hocker ... Gothic hauhs, Old Icelandic hōr, hār, Old English hēah ... \\\"high\\\"' — hip and high are separate formations from heap.\"},\n    {\"src\": \"KLN\", \"where\": \"Klein s.vv. hip, high\", \"stance\": \"partial\", \"note\": \"Klein likewise derives hip from OE hype/Goth. hups and high from OE hēah/Goth. hauhs, not from the heap-word.\"}\n  ]\n})\n\ndoc[\"entries\"].append(e0)\n\n# ------------------------------------------------------------------ entry 1\ne1 = {\n  \"entry\": 1,\n  \"root\": \"Geu 2, Geua\",\n  \"verdict\": \"confirmed\",\n  \"modern_form\": \"PIE *ǵeu-, *ǵeu̯ə- (*ǵewH-) 'to advance, hurry, drive' (Pokorny 399; Watkins/AHD geuə-)\",\n  \"note\": \"Root, language label, gloss and page number are all exactly right, and Pokorny's article on p.399 is in effect the whole Iranian half of Nourai's chart: 'Root / lemma: ǵeu-, ǵeuə- (besides ǵeus-) / Meaning: to advance; to hurry / Material: Old Indic junáti \\\"drive, hurry\\\", jávate \\\"hurries\\\" ... javas- \\\"quickness\\\" ...; Avestan zavah- n. \\\"power, strength\\\", zavar- n. \\\"(physical) power, strength\\\" (esp. of the feet and the horse), npers. zōr \\\"power\\\", Baluchi zū \\\"quick, fast\\\", Avestan zəvīštya \\\"the hastiest\\\" ...; besides pointing to Indo-European ǵeuə-: Avestan zava- \\\"hurry\\\"; npers. zūd \\\"quick, fast\\\" ... / Page(s): 399'. Watkins has the same lemma: 'geuə-. To hasten. ... [Pok. ǵeu- 399.]' The one thing worth flagging for the reader is that the two derivational side-claims Nourai attaches to the root — abzār/afzār 'tool' (node #2) and afzūdan 'to increase' (node #4) — are not part of Pokorny's article and are contested: Hübschmann p.16, which Nourai himself cites, derives afzār from OP *abi-zara-, not from zāvar-, while Nyberg II and Wiktionary trace afzūdan/abzūdan to Av. gav- 'to procure' (Proto-Iranian *Habi-gaw-) rather than to zav- 'to hasten'. Old Persian abi-jāvaya- (node #5) is genuinely attested (Kent, XPf 40, XPg 9), and its j does point to *ǵew-, which is the strongest argument on Nourai's side.\",\n  \"note_fa\": \"ریشه، برچسب زبانی، معنا و شمارهٔ صفحه همگی درست‌اند و مقالهٔ پوکورنی در صفحهٔ ۳۹۹ در واقع همان شاخهٔ ایرانی نمودار است: «ǵeu-, ǵeuə- : شتافتن ... اوستایی zavah- «نیرو»، zavar- «نیروی (تنی)»، فارسی نو zōr «زور»، بلوچی zū «تند»، اوستایی zəvīštya «تندترین» ... و کنار آن zava- اوستایی «شتاب» و zūd فارسی نو «زود»». واتکینز هم همین مادّه را با همین معنا دارد. تنها نکتهٔ درخورِ هشدار این است که دو ادعای فرعیِ نمودار — «ابزار/افزار» (خانهٔ ۲) و «افزودن» (خانهٔ ۴) — در مقالهٔ پوکورنی نیستند و محلّ اختلاف‌اند: هوبشمان در صفحهٔ ۱۶، که خود نورایی به آن ارجاع می‌دهد، «افزار» را از *abi-zara- پارسی باستان می‌گیرد نه از zāvar-، و نیبرگ و ویکی‌واژه «افزودن» را از ریشهٔ gav- «به دست آوردن» می‌دانند. در برابر، abi-jāvaya- پارسی باستان (خانهٔ ۵) به‌راستی در کتیبه‌های خشایارشا گواهی شده و همان j آن نیرومندترین دلیل به سود نورایی است.\",\n  \"sources\": [W+\"%D8%B2%D9%88%D8%AF\", W+\"%D8%B2%D9%88%D8%B1\"],\n  \"ref_check\": [\n    {\"ref\": \"POK:399\", \"status\": \"supports\", \"note\": \"POK_full.txt: 'Root / lemma: ǵeu- ǵeuə- (besides ǵeus-) / Meaning: to advance; to hurry ... Avestan zavah- n. \\\"power, strength\\\", zavar- n. \\\"(physical) power, strength\\\" ... npers. zōr \\\"power\\\" ... Avestan zava- \\\"hurry\\\"; npers. zūd \\\"quick, fast\\\" ... References: WP. I 555. Page(s): 399'.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. geuə- (AHD_watkins1985.txt l.499)\", \"stance\": \"supports\", \"note\": \"'geuə-. To hasten. Possibly the base of Germanic *kaur-jan in Old Norse keyra, to drive: SKIJORING. [Pok. ǵeu- 399.]'\"},\n    {\"src\": \"WLD\", \"where\": \"Bd. I 555\", \"stance\": \"supports\", \"note\": \"Pokorny's own reference line for this lemma is 'WP. I 555', i.e. Walde-Pokorny I 555 carries the same Indo-Iranian material.\"},\n    {\"src\": \"CHEUNG\", \"where\": \"Cheung 2007, Etymological Dictionary of the Iranian Verb, z- section\", \"stance\": \"silent\", \"note\": \"Cheung lists *zau 'to pour (libation)', *zauH 'to call' and *zauš 'to rejoice' but no root *zau 'to hasten'; the verb is not treated, so his dictionary neither supports nor contradicts.\"}\n  ],\n  \"nodes\": []\n}\n\ne1[\"nodes\"].append({\n  \"id\": 1, \"lang\": \"Avestan\", \"words\": \"zavah, zâvar : power, force; api-zâwar : tool\",\n  \"verdict\": \"plausible\",\n  \"derivation\": \"The first two words are attested exactly as printed. Bartholomae has Gathic zavah- n. 'Kraft, Stärke' (Y 33.12) and Younger Avestan zāvar- n. '(physische) Kraft, Stärke', especially of the feet and of horses (Yt 13.1, Yt 10.62, Y 57.26 'sraoša ... zāvarə dayā hitaēibyō' \\\"give strength to our teams\\\"); both are -ah-/-ar- heteroclitic abstracts from the root zav- 'to hasten, drive', the Iranian z- being the regular reflex of PIE palatal *ǵ (Skt. jávas- 'speed', jávate 'hurries'). The third item, api-zāwar 'tool', is not an Avestan word: Bartholomae has no aipi-/api-zāvar-, and greps of AiW find nothing. It is a reconstruction, and Nourai has it from Mo'in's footnote on the page he cites (Borhān p.148, s.v. افزار), which reads 'از: اوستایی aiwi پیشوند (به-، بر) + zavar اوستایی (زور، نیرو) «بارتولمه»' — Mo'in's own *aiwi-zāvar- for the ancestor of افزار. The node is therefore two-thirds attested fact and one-third an editorially reconstructed compound, which is why it can only be called plausible.\",\n  \"derivation_fa\": \"دو واژهٔ نخست دقیقاً همان‌اند که چاپ شده: بارتولومه zavah- گاهانی «نیرو، توان» (یسنا ۳۳٫۱۲) و zāvar- اوستایی متأخر «نیروی تنی»، به‌ویژه نیروی پا و اسب (یشت ۱۳٫۱، یسنا ۵۷٫۲۶) را ثبت کرده است؛ هر دو نامِ مصدرِ ناهمگون‌ستاکِ ah-/ar- از ریشهٔ zav- «شتافتن، راندن»اند و ز ایرانی بازتاب قاعده‌مندِ *ǵ کامی هندواروپایی است (سنسکریت jávas-، jávate). اما api-zāwar «ابزار» واژه‌ای اوستایی نیست؛ بارتولومه چنین ترکیبی ندارد. این صورت بازسازی‌شده است و نورایی آن را از حاشیهٔ معین در همان صفحهٔ برهان قاطع (ص ۱۴۸، ذیل «افزار») گرفته که می‌نویسد: «از: اوستایی aiwi پیشوند (به‌ـ، بر) + zavar اوستایی (زور، نیرو) «بارتولمه»». پس این خانه دو سومش گواهی‌شده و یک سومش بازسازیِ ویراستارانه است و تنها «با احتیاط پذیرفتنی» است.\",\n  \"sources\": [W+\"%D8%A7%D9%81%D8%B2%D8%A7%D8%B1\"],\n  \"ref_check\": [\n    {\"ref\": \"POK:399\", \"status\": \"supports\", \"note\": \"'Avestan zavah- n. \\\"power, strength\\\", zavar- n. \\\"(physical) power, strength\\\" (esp. of the feet and the horse)' — Pokorny p.399, verbatim the first two words of the box; he has nothing on api-zāvar-.\"},\n    {\"ref\": \"BQT:148\", \"status\": \"supports\", \"note\": \"BQT_v1_pages.txt leaf 364 (printed p.148; leaf 363 = افراشتن, leaf 365 = افسردن) carries the headword افزار, and Mo'in's footnote reads 'از: اوستایی aiwi پیشوند (به - بر) ... zavar اوستایی (زور، نیرو) «بارتولمه»' — this is the source of Nourai's api-zâwar.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"BRT\", \"where\": \"AiW s.vv. zavah-, zāvar- (BRT.txt ll.27775, 28089)\", \"stance\": \"partial\", \"note\": \"'g. zavah- n. \\\"Kraft, Stärke\\\": Y. 33.12'; 'j. zāvar- n. \\\"(physische) Kraft, Stärke\\\": Yt 13.1; 10.62 ... a) insbes. der Füße ... b) der Rosse'. No aipi-/api-zāvar- exists in Bartholomae.\"},\n    {\"src\": \"HUB\", \"where\": \"Persische Studien p.16, no. 95\", \"stance\": \"contradicts\", \"note\": \"'Np. afzār \\\"Werkzeug\\\" (bal. LW. auzār) ~ phl. afzār geht nach ZDMG. 32, 408 auf ein ap. *abizara-, nicht *abidara- zurück ... Mit ap. *abizara- deckt sich lautlich skr. abhihara-' — Hübschmann derives the tool-word from *abi-zara-, not from zāvar-.\"},\n    {\"src\": \"PHD\", \"where\": \"MacKenzie p.4\", \"stance\": \"partial\", \"note\": \"MacKenzie has two homonyms: '¹abzār [...| M ʾbzʾr, N afzār] instrument, means; spice' and '²abzār [...] skill, power; powerful. ~ōmand skilled, able' — the second is semantically the 'power' word Nourai needs, but MacKenzie keeps the two apart.\"}\n  ]\n})\n\ne1[\"nodes\"].append({\n  \"id\": 2, \"lang\": \"Persian\", \"words\": \"zŭr 1 «زور ۱»; zâvar «زاوَر»; zâv «زاو»; abzâr, afzâr «ابزار ، افزار»\",\n  \"verdict\": \"plausible\",\n  \"derivation\": \"زور zūr 'force, power' is beyond dispute: Horn no. 674bis, the entry on the page Nourai cites, reads 'zōr \\\"Kraft, Gewalt\\\" ... aw. zāvar- \\\"Macht, Kraft\\\"; phlv. zōr, zōrīh, arm. LW. zaur', and MacKenzie has MP zōr [z(w)wl] 'power, strength'; the chain is Av. zāvar- > *zāwar > MP zōr (with contraction of -āwa- to -ō-) > NP زور. زاور zāvar and زاو zāv are the learned/archaic Persian doublets of the same Avestan word, revived in poetry and lexicography rather than inherited through the ordinary spoken line. ابزار/افزار is the contested item. Mo'in's footnote at Borhān p.148, Nourai's own reference, derives it from Avestan aiwi- + zāvar- 'power', which is exactly the arrow drawn here; but Hübschmann p.16 no.95 rejects that and posits OP *abi-zara- (matching Skt. abhi-hara- 'bringing to'), and Wiktionary traces Persian افزار no further back than MP abzār 'instrument, means; spice', calling ابزار its doublet. Nourai's own note ('For a different derivation of \\\"abzâr & afzâr\\\" see root \\\"Ghei 2\\\"') acknowledges the split. Verdict: the zūr/zāvar/zāv part is confirmed, the abzār/afzār part is accepted by some (Mo'in) and denied by others (Hübschmann), so the node as a whole is plausible.\",\n  \"derivation_fa\": \"«زور» بی‌هیچ تردیدی از zāvar اوستایی است: هرن در شمارهٔ ۶۷۴ مکرر، درست در همان صفحه‌ای که نورایی ارجاع می‌دهد، می‌نویسد «zōr \\\"نیرو، توان\\\" ... اوستایی zāvar-؛ پهلوی zōr, zōrīh»، و مکنزی هم zōr پهلوی را دارد؛ زنجیره چنین است: zāvar- اوستایی ← *zāwar ← zōr فارسی میانه (با ادغام -āwa- به -ō-) ← «زور». «زاور» و «زاو» دوگانه‌های ادبی و کهن‌گرایانهٔ همان واژه‌اند که بیشتر از راه فرهنگ‌نویسی و شعر زنده مانده‌اند نه از راه گفتار روزمره. اما «ابزار/افزار» محلّ اختلاف است: حاشیهٔ معین در برهان قاطع (ص ۱۴۸) آن را از aiwi + zāvar اوستایی می‌گیرد، یعنی دقیقاً همین پیکانِ نمودار؛ ولی هوبشمان (ص ۱۶، شمارهٔ ۹۵) این را رد می‌کند و *abi-zara- پارسی باستان را می‌نهد، و ویکی‌واژه هم فراتر از abzār پهلوی نمی‌رود. خودِ نورایی نیز در یادداشتش به اختلاف اشاره کرده است. پس بخش «زور» درست و بخش «ابزار» با احتیاط پذیرفتنی است.\",\n  \"sources\": [W+\"%D8%B2%D9%88%D8%B1\", W+\"%D8%A7%D9%81%D8%B2%D8%A7%D8%B1\"],\n  \"ref_check\": [\n    {\"ref\": \"POK:399\", \"status\": \"supports\", \"note\": \"Pokorny p.399 s.v. ǵeu-: 'Avestan zavah- ..., zavar- ..., npers. zōr \\\"power\\\"' — the Persian word is in Pokorny's own material.\"},\n    {\"ref\": \"HRN:149\", \"status\": \"supports\", \"note\": \"HRN.txt leaf 170 (printed p.149), entry '674bis. zōr \\\"Kraft, Gewalt\\\" (reimt auf hōr, Šāhn. I, 202 Vers 1311). aw. zāvar- \\\"Macht, Kraft\\\"; phlv. zōr, zōrīh, arm. LW. zaur ... LW. kurd. afgh. bel. zōr.'\"},\n    {\"ref\": \"BQT:148\", \"status\": \"supports\", \"note\": \"Borhān p.148 (BQT_v1_pages.txt leaf 364) s.v. افزار, with Mo'in's footnote deriving it from Avestan aiwi- + zavar 'زور، نیرو' — the very derivation the arrow draws.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"HRN\", \"where\": \"no. 674bis, p.149\", \"stance\": \"supports\", \"note\": \"see ref_check; Horn is explicit that NP zōr is Av. zāvar-.\"},\n    {\"src\": \"PHD\", \"where\": \"MacKenzie p.99 and p.4\", \"stance\": \"partial\", \"note\": \"'zōr [z(w)wl | M zwr, N ~] power, strength'; but '¹abzār ... instrument, means; spice' and '²abzār ... skill, power' are separate entries, so MacKenzie does not join afzār to zōr.\"},\n    {\"src\": \"HUB\", \"where\": \"Persische Studien p.16 no. 95\", \"stance\": \"contradicts\", \"note\": \"'Np. afzār \\\"Werkzeug\\\" ~ phl. afzār geht ... auf ein ap. *abizara- ... zurück' — against the zāvar- derivation.\"},\n    {\"src\": \"BQT\", \"where\": \"Mo'in's footnote, p.148\", \"stance\": \"supports\", \"note\": \"'از: اوستایی aiwi پیشوند (به - بر) + zavar (زور، نیرو)'.\"}\n  ]\n})\n\ne1[\"nodes\"].append({\n  \"id\": 3, \"lang\": \"Avestan\", \"words\": \"zava : haste; aiwi-zâvayeiti : adds up (☞Ambhi)\",\n  \"verdict\": \"plausible\",\n  \"derivation\": \"zava- 'haste' is Pokorny's own citation on p.399: 'besides pointing to Indo-European ǵeuə-: Avestan zava- \\\"hurry\\\"'. It is the thematic action-noun of the root zav-, beside the -ah-/-ar- abstracts of node #1. aiwi-zāvayeiti is a different matter: it is not an attested Avestan verb form but Hübschmann's reconstruction, made on the page Nourai cites — Persische Studien p.16 no. 96: 'Aus aiwi + savayəiti wäre im Neup. *afsāyad geworden: das vorliegende afzāyad \\\"vermehrt\\\" muss auf *aiwizavayəiti zurückgehen'. In other words Hübschmann argued backwards from NP افزاید that the Old Iranian causative must have been *aiwi-zav-aya- with z, not s, and Nourai has printed the reconstruction as if it were a citation form. The prefix is Av. aiwi- 'to, upon' (PIE *h₂mbʰi, Nourai's 'Ambhi' cross-reference), and the sense 'adds up, increases' is the causative 'makes go forward'. The claim is defensible and is Hübschmann's, but the asterisk is missing.\",\n  \"derivation_fa\": \"zava- «شتاب» را خودِ پوکورنی در صفحهٔ ۳۹۹ می‌آورد: «در کنار آن، اشاره‌کننده به ǵeuə- هندواروپایی: zava- اوستایی «شتاب»»؛ این صورت نامِ کنشِ ستاکیِ همان ریشهٔ zav- است. اما aiwi-zāvayeiti صورتی گواهی‌شده در اوستا نیست، بلکه بازسازیِ هوبشمان است در همان صفحه‌ای که نورایی ارجاع می‌دهد (پرسیشه شتودین، ص ۱۶، شمارهٔ ۹۶): «از aiwi + savayəiti در فارسی نو *afsāyad می‌شد؛ پس afzāyadِ موجود باید به *aiwizavayəiti بازگردد». یعنی هوبشمان از روی «افزاید» فارسی نتیجه گرفته که سببیِ ایرانی باستان باید با ز بوده باشد نه با س. پیشوند همان aiwi- اوستایی «به، بر» است (ارجاع نورایی به Ambhi) و معنای «می‌افزاید» همان سببیِ «به پیش می‌راند». ادعا پذیرفتنی است ولی ستارهٔ بازسازی در چاپ افتاده است.\",\n  \"sources\": [W+\"%D8%A7%D9%81%D8%B2%D9%88%D8%AF%D9%86\"],\n  \"ref_check\": [\n    {\"ref\": \"POK:399\", \"status\": \"supports\", \"note\": \"'besides auf Indo Germanic ǵeuə- weisend: Avestan zava- \\\"hurry\\\"' (POK_full.txt, lemma ǵeu- ǵeuə-, p.399).\"},\n    {\"ref\": \"HUB:16\", \"status\": \"supports\", \"note\": \"HUB.txt leaf 27 (printed p.16), entry 96: 'Aus aiwi + savayəiti wäre im Neup. *afsāyad geworden: das vorliegende afzāyad \\\"vermehrt\\\" muss auf *aiwizavayəiti zurückgehen' — exactly Nourai's form, but marked by Hübschmann as a reconstruction.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"BRT\", \"where\": \"AiW, z- section\", \"stance\": \"silent\", \"note\": \"greps for aiwi.zav-, aipi.zav-, api.zav- in BRT.txt return nothing: Bartholomae records no such compound verb.\"},\n    {\"src\": \"NYB\", \"where\": \"Nyberg II s.v. apa-zūtan (NYB_vol2_glossary.txt l.566)\", \"stance\": \"partial\", \"note\": \"'apa-zūtan, apa-zāyītan, to increase ... < *abi-jav-, in SW with api- substituted for abi- < abi- + Av. gav- \\\"to procure\\\"' — Nyberg reconstructs the same prefixed causative but assigns it to gav-, not zav-.\"},\n    {\"src\": \"CHEUNG\", \"where\": \"Cheung 2007\", \"stance\": \"silent\", \"note\": \"no entry for a root *zau 'to hasten'; the verb underlying afzūdan is not treated in his dictionary.\"}\n  ]\n})\n\ne1[\"nodes\"].append({\n  \"id\": 4, \"lang\": \"Persian\", \"words\": \"zŭd «زود»; afzŭdan «افزودن» (extra: افزایش ، افزون ، فزون)\",\n  \"verdict\": \"plausible\",\n  \"derivation\": \"زود zūd 'fast, soon' is fully confirmed: Horn no. 673, on the page Nourai cites, has 'zūd \\\"schnell\\\". aw. √jav- \\\"eilen\\\", java, javar; phlv. zūt (pāz. zōt); ai. √jav-, jávate \\\"eilen\\\"', MacKenzie has MP zūd [zwt'] 'quick(ly)' and Nyberg 'zūt [zwt'] swift, prompt, quick ... MPrs zwd; NP zūd', and Wiktionary derives it from PIE *ǵewH- with Av. zəvīštya 'the quickest' and Skt. jū- alongside; the form is the verbal adjective *zū-ta- 'hastened' (Skt. jūtá-). افزودن afzūdan 'to increase' (with افزایش, افزون, فزون) goes back to MP abzūdan/abzāy- (Nyberg's apa-zūtan/apa-zāyītan, with the south-western prefix api- for abi-), and Hübschmann p.16 no.96 — Nourai's reference — explicitly makes it *aiwi-zavaya-, i.e. this root. But Nyberg derives the same Middle Persian verb from 'abi- + Av. gav- \\\"to procure\\\"', and Wiktionary reconstructs Proto-Iranian *Habigaw- with the root 'of unclear origin, possibly related to Lithuanian gáuti \\\"to obtain\\\"'. Both accounts start from the same prefixed OP causative abi-jāvaya-; they differ on whether its root is ǵew- 'hasten' or gew- 'obtain'. Because zūd is certain and afzūdan is contested, the node is plausible rather than confirmed.\",\n  \"derivation_fa\": \"«زود» یکسره تأیید می‌شود: هرن در شمارهٔ ۶۷۳ همان صفحه می‌نویسد «zūd \\\"تند\\\"؛ اوستایی √jav- \\\"شتافتن\\\"، java؛ پهلوی zūt»، مکنزی zūd پهلوی و نیبرگ zūt را دارند، و ویکی‌واژه آن را از *ǵewH- هندواروپایی می‌گیرد با هم‌ریشه‌های zəvīštya اوستایی «تندترین» و jū- سنسکریت؛ صورت آن صفتِ فعلیِ *zū-ta- «شتابیده» است (سنسکریت jūtá-). «افزودن» (و افزایش، افزون، فزون) از abzūdan/abzāy- فارسی میانه است (نیبرگ: apa-zūtan/apa-zāyītan با پیشوندِ جنوب‌غربیِ api- به جای abi-)، و هوبشمان که مأخذ نورایی است آن را صریحاً *aiwi-zavaya- می‌داند، یعنی از همین ریشه. اما نیبرگ همان فعل را از «abi- + gav- اوستایی (به دست آوردن)» می‌گیرد و ویکی‌واژه *Habigaw- ایرانی آغازین را بازسازی می‌کند و ریشه را ناروشن می‌خواند. هر دو از یک صورتِ سببیِ پارسی باستان (abi-jāvaya-) آغاز می‌کنند و تنها بر سرِ ریشهٔ آن اختلاف دارند. چون «زود» قطعی و «افزودن» محلّ اختلاف است، این خانه با احتیاط پذیرفتنی است.\",\n  \"sources\": [W+\"%D8%B2%D9%88%D8%AF\", W+\"%D8%A7%D9%81%D8%B2%D9%88%D8%AF%D9%86\"],\n  \"ref_check\": [\n    {\"ref\": \"POK:399\", \"status\": \"supports\", \"note\": \"Pokorny p.399: 'npers. zūd \\\"quick, fast\\\" could belong to Aryan ǵou z' (and 'Baluchi zū \\\"quick, fast\\\"') — the Persian adverb is in his material.\"},\n    {\"ref\": \"HRN:149\", \"status\": \"supports\", \"note\": \"HRN.txt leaf 170 (printed p.149), entry '673. zūd \\\"schnell\\\". aw. √jav- \\\"eilen\\\", java, javar (?, Geldner) ; phlv. zāt (pāz. zōt); ai. √jav-, jávate \\\"eilen\\\". kurd. zū; bel. zūt, zū, n. zid.'\"},\n    {\"ref\": \"HUB:16\", \"status\": \"supports\", \"note\": \"Hübschmann p.16 no.96: 'das vorliegende afzāyad \\\"vermehrt\\\" muss auf *aiwizavayəiti zurückgehen' — supports afzūdan under this root.\"},\n    {\"ref\": \"BQT:1043\", \"status\": \"supports\", \"note\": \"BQT_v2_pages.txt leaf 503 (printed p.1043, offset +540) is in the ز section and contains 'زو ... مخفف زود است که تعجیل و شتاب باشد' — the page really is the زود page.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"PHD\", \"where\": \"MacKenzie pp.4 and 99\", \"stance\": \"supports\", \"note\": \"'zūd [zwt' | M zwd, N ~] quick(ly). ~īh: speed'; 'abzūdan, abzāy- [ʾpzwtn', ʾpzʾd- | M ʾbzʾy-, N afzūdan, afzāy-] increase, grow'.\"},\n    {\"src\": \"NYB\", \"where\": \"Nyberg II s.vv. apa-zūtan, apa-zōn, zūt\", \"stance\": \"partial\", \"note\": \"'zūt [zwt'] swift, prompt, quick ... NP zūd' (supports zūd); but 'apa-zūtan ... < *abi-jav- ... < abi- + Av. gav- \\\"to procure\\\"' assigns afzūdan to a different root.\"},\n    {\"src\": \"HRN\", \"where\": \"no. 673, p.149\", \"stance\": \"supports\", \"note\": \"see ref_check.\"}\n  ]\n})\n\ne1[\"nodes\"].append({\n  \"id\": 5, \"lang\": \"Old Persian\", \"words\": \"abi-jâvaya : to increase (☞Ambhi)\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"This is a real, inscriptionally attested Old Persian form. Kent's lexicon has 'abi- + jav- caus. \\\"promote, increase, add to\\\": abiyajāvayam 1st sg. impf. XPg 9; abijāvayam XPf 40', i.e. Xerxes' own words at Persepolis: 'aniya kartam abijāvayam' \\\"I added other construction (to what my father had made)\\\". Morphologically it is the causative-iterative stem jāv-aya- (lengthened grade of jav- 'to move quickly, drive') with the preverb abiy- 'to, upon' (PIE *h₂mbʰi, Nourai's 'Ambhi'); the Old Persian j corresponds to Avestan z (both from PIE palatal *ǵ), which is why the Avestan cognate of node #3 has z-. The sense 'promote, add to' is the causative of 'go forward'. Nourai's spelling abi-jâvaya reproduces the stem as Gharib and Nyberg cite it; the inscriptional attestation carries a 1sg. imperfect ending.\",\n  \"derivation_fa\": \"این صورت راستین و گواهی‌شده در کتیبه‌های هخامنشی است. کِنت در واژه‌نامهٔ پارسی باستان می‌نویسد: «abi- + jav- سببی «افزودن، افزون کردن»: abiyajāvayam در XPg بند ۹ و abijāvayam در XPf بند ۴۰»، یعنی سخنِ خودِ خشایارشا در تخت‌جمشید: «aniya kartam abijāvayam» = «ساختِ دیگری بر آن افزودم». از نظر ساخت، ستاکِ سببیِ jāv-aya- (درجهٔ کشیدهٔ jav- «تند رفتن، راندن») با پیشوندِ abiy- «به، بر» است؛ j پارسی باستان برابرِ z اوستایی است (هر دو از *ǵ کامی هندواروپایی) و به همین سبب هم‌ریشهٔ اوستاییِ خانهٔ ۳ با ز آغاز می‌شود. ادعای نورایی درست است.\",\n  \"sources\": [],\n  \"ref_check\": [\n    {\"ref\": \"SOD:103\", \"status\": \"supports\", \"note\": \"SOD_pages.txt, form-feed leaf 168 (printed p.103; the facing page shows the numeral 104), entry 2618: 'βjʾw- M | β(ə)zaw ©<OP abi-jāvaya-, Parth. abgaw-; MP abzāy- ©trans. v. ⇒ʾβzʾw-, βjy- (to) increase' — Gharib's entry cites exactly the Old Persian form Nourai prints.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KNT\", \"where\": \"Kent, Old Persian, Lexicon s.v. jav- (KNT.txt l.5410)\", \"stance\": \"supports\", \"note\": \"'abi- + jav- caus. \\\"promote, increase, add to\\\": abiyajāvayam 1st sg. imf. (§215) XPg 9; abijāvayam (§23.1, §140.III) XPf 40.' The text of XPf 40 in Kent reads '... aniya kartam abijāvayam'.\"},\n    {\"src\": \"NYB\", \"where\": \"Nyberg II s.v. apa-zūtan\", \"stance\": \"supports\", \"note\": \"'OP caus. abi-jāvaya- \\\"to add\\\"; MPrs pres. ʾbzw- intr., ʾbzʾy- trans. \\\"to increase\\\"' — but Nyberg files the root as Av. gav- 'to procure' rather than zav- 'to hasten'.\"},\n    {\"src\": \"BRT\", \"where\": \"AiW (Old Persian entries)\", \"stance\": \"silent\", \"note\": \"no separate abi-jāvaya- headword; Bartholomae's Old Persian material is thin here and the compound is not listed.\"}\n  ]\n})\n\ne1[\"nodes\"].append({\n  \"id\": 6, \"lang\": \"Sogdian\", \"words\": \"bj`w : to increase\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"Sogdian βjʾw- (Nourai's bj`w, Manichaean-script spelling) 'to increase' is Gharib's entry 2618, and Gharib herself gives it precisely the pedigree the chart draws: '< OP abi-jāvaya-, Parth. abgaw-; MP abzāy-'. The Sogdian form shows the regular Iranian lenition of initial *b to the fricative β and the loss of the Old Iranian causative suffix vowel; the intransitive partner βzʾw-/βjy- 'to grow' (Gharib 3078, 2630) belongs with it. One correction to the chart's geometry: Sogdian is not descended from Old Persian, which is a South-Western Iranian language, but is an Eastern Middle Iranian language; Gharib's '<OP' is a comparison of the two Iranian outcomes of one Old Iranian preverb-plus-root compound, not a statement of borrowing. As a statement of cognacy the arrow is right; as a statement of descent it is a simplification of the standard kind Nourai's charts make throughout.\",\n  \"derivation_fa\": \"βjʾw- سغدی (همان bj`w نورایی، به خطّ مانوی) «افزودن» مدخل شمارهٔ ۲۶۱۸ فرهنگ قریب است و خودِ قریب دقیقاً همان تبارنامه را می‌دهد که نمودار رسم کرده: «< abi-jāvaya- پارسی باستان، abgaw- پارتی، abzāy- فارسی میانه». در سغدی b آغازین به سایشیِ β نرم شده و واکهٔ پسوند سببی افتاده است؛ همتای لازمِ آن βzʾw-/βjy- «رشد کردن» (مدخل‌های ۳۰۷۸ و ۲۶۳۰) نیز به همین خانواده تعلق دارد. تنها نکتهٔ اصلاحی در هندسهٔ نمودار این است که سغدی فرزندِ پارسی باستان نیست: پارسی باستان جنوب‌غربی و سغدی ایرانیِ میانهٔ شرقی است؛ نشانهٔ «<OP» در فرهنگ قریب سنجشِ دو بازماندهٔ یک ترکیبِ ایرانی باستان است نه بیان وام‌گیری. پس پیکان به معنای هم‌ریشگی درست است و تنها به معنای نسبِ مستقیم ساده‌سازی شده است.\",\n  \"sources\": [],\n  \"ref_check\": [\n    {\"ref\": \"SOD:103\", \"status\": \"supports\", \"note\": \"Gharib, Sogdian Dictionary, entry 2618 on printed p.103 (SOD_pages.txt, 168th form-feed block): 'βjʾw- M | β(ə)zaw ©<OP abi-jāvaya-, Parth. abgaw-; MP abzāy- ©trans. v. ⇒ʾβzʾw-, βjy- (to)increase; GMS 90, 264'.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"SOD\", \"where\": \"Gharib entries 2618, 2630, 3078, 3080\", \"stance\": \"supports\", \"note\": \"'βjy- ... β(ə)zay ©intrans. v. ⇒ʾβzʾw-, βjʾw-, ʾβzʾy- (to)grow'; 'βzʾw- B ... (to)grow, (to)increase'; 'βzʾw- C ... (to)increase'.\"},\n    {\"src\": \"NYB\", \"where\": \"Nyberg II s.v. apa-zūtan\", \"stance\": \"supports\", \"note\": \"'MPrth ʾbgwdn ʾbgʾw- \\\"to increase, to add to\\\", ʾbgʾw \\\"increase\\\"' — the Parthian cognate Gharib names, confirming the Middle Iranian spread of the verb.\"},\n    {\"src\": \"KNT\", \"where\": \"Kent, Lexicon s.v. jav-\", \"stance\": \"supports\", \"note\": \"the Old Persian source form 'abijāvayam XPf 40' is attested, so Gharib's comparison rests on a real word.\"}\n  ]\n})\n\ndoc[\"entries\"].append(e1)\n\nout = \"/home/sfmqrb/git/rishe/data/verification/page-177.json\"\nwith io.open(out, \"w\", encoding=\"utf-8\") as f:\n    json.dump(doc, f, ensure_ascii=False, indent=2)\n    f.write(\"\\n\")\nprint(\"written\", out)\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build177.py && python3 -m json.tool data/verification/page-177.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 177"
}
```


### [2026-09-05T21:13:25.151Z] TOOL RESULT

```
written /home/sfmqrb/git/rishe/data/verification/page-177.json
JSON OK
nodes verified: 16/16
node verdicts: {'confirmed': 6, 'plausible': 6, 'transcription_suspect': 1, 'disputed': 3}
root verdicts: {'confirmed': 2}
ref checks: {'supports': 20, 'partial': 2, 'not_checked': 3, 'contradicts': 3}
books consulted: {'supports': 22, 'silent': 10, 'partial': 10, 'contradicts': 10} | by book: {'BRT': 6, 'KLN': 6, 'PHD': 5, 'NYB': 5, 'POK': 4, 'WLD': 3, 'HRN': 3, 'AHD': 3, 'IEC': 2, 'SYN': 2, 'MON': 2, 'HUB': 2, 'KNT': 2, 'PLA': 1, 'FVQ': 1, 'TAD': 1, 'AFM': 1, 'BQT': 1, 'CHEUNG': 1, 'SOD': 1}
```


## [2026-09-05T21:13:25.637Z] AGENT

You've hit your session limit · resets 7:40pm (America/Toronto)
