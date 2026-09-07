# Verification process log — verify-page-341


## [2026-09-07T17:36:07.686Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 341 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-341.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-341.json. Write /home/sfmqrb/git/rishe/data/verification/page-341.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 341` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-07T17:36:09.401Z] AGENT

I'll start by reading the instructions.


## [2026-09-07T17:36:10.050Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-07T17:36:10.064Z] TOOL RESULT

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


## [2026-09-07T17:36:10.769Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-341.txt"
}
```


### [2026-09-07T17:36:10.811Z] TOOL RESULT

```
1	=== PDF page 341 (book page 311) ===
2	--- entry 0 ---
3	ROOT Mon -> redirect to Men 3
4	--- entry 1 ---
5	ROOT Mono -> redirect to Men 3
6	--- entry 2 ---
7	ROOT Mor-to -> redirect to Mer 2
8	--- entry 3 ---
9	ROOT Morui -> redirect to Morwi
10	--- entry 4 ---
11	ROOT [Indo-European] Morwi, Morui : ant  (refs POK:749)
12	#1 (parent #0) [Avestan] refs=POK:749 | maoirî : ant
13	  #2 (parent #1) [Pahlavi] refs=BQT:2049; SNS:248 | môr, môrčag : ant
14	    #3 (parent #2) [Persian] refs=BQT:2049 | mŭr «مور» : ant | extra: مورچه ، موریانه
15	#4 (parent #0) [Latin] refs=AHD | vormîca, formica : ant
16	  #5 (parent #4) [French] refs=None | 
17	    #6 (parent #5) [Persian] refs=MON |  | extra: کلروفرم ، اسید فرمیک
18	  #7 (parent #4) [English] refs=AHD | formic [acid] ; chloroform
19	--- entry 5 ---
20	ROOT [Indo-European] Moudh, Moudhiô : to mourn  (refs IEC:802)
21	#1 (parent #0) [Avestan] refs=HRN:224 | môy : groaning ; a-mayavâ : grief
22	  #2 (parent #1) [Pahlavi] refs=HRN:224; FFD:77; MON | môy, môyak : groaning ; must : groaning, complaint
23	    #3 (parent #2) [Persian] refs=HRN:224; FFD:77; MON:4080,4433,4455; IEC:802 | mŭy-îdan «موییدن» : to cry ; most «مُست ۲» : groaning, complaint, sorrow | extra: مویه ، موی ، موژ ، موژه
24	مُستمند | NOTE: HRN:223 links these to Avestan "amâ-yavâ:grief". See root "Ome".
25	#4 (parent #0) [Old Iranian] refs=FFD:77 | maud, mauda : to cry, to groan
26	--- entry 6 ---
27	ROOT Moudhiô -> redirect to Moudh
28	--- entry 7 ---
29	ROOT Mozgho -> redirect to Mozgo
30	
```


## [2026-09-07T17:36:11.018Z] TOOL CALL #3: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/extracted/batch/page-341.json"
}
```


### [2026-09-07T17:36:11.032Z] TOOL RESULT

```
1	{
2	  "pdf_page": 341,
3	  "book_page": 311,
4	  "entries": [
5	    {
6	      "root": {"name": "Mon", "redirect": "Men 3"},
7	      "nodes": []
8	    },
9	    {
10	      "root": {"name": "Mono", "redirect": "Men 3"},
11	      "nodes": []
12	    },
13	    {
14	      "root": {"name": "Mor-to", "redirect": "Mer 2"},
15	      "nodes": []
16	    },
17	    {
18	      "root": {"name": "Morui", "redirect": "Morwi"},
19	      "nodes": []
20	    },
21	    {
22	      "root": {
23	        "name": "Morwi, Morui",
24	        "lang": "Indo-European",
25	        "refs": "POK:749",
26	        "gloss": "ant"
27	      },
28	      "nodes": [
29	        {
30	          "id": 1,
31	          "parent": 0,
32	          "lang": "Avestan",
33	          "refs": "POK:749",
34	          "words": [
35	            {"translit": "maoirî", "gloss": "ant", "script": null}
36	          ],
37	          "note": null,
38	          "quote": null
39	        },
40	        {
41	          "id": 2,
42	          "parent": 1,
43	          "lang": "Pahlavi",
44	          "refs": "BQT:2049; SNS:248",
45	          "words": [
46	            {"translit": "môr, môrčag", "gloss": "ant", "script": null}
47	          ],
48	          "note": null,
49	          "quote": null
50	        },
51	        {
52	          "id": 3,
53	          "parent": 2,
54	          "lang": "Persian",
55	          "refs": "BQT:2049",
56	          "words": [
57	            {"translit": "mŭr", "gloss": "ant", "script": "مور"}
58	          ],
59	          "script_extra": "مورچه ، موریانه",
60	          "note": null,
61	          "quote": null
62	        },
63	        {
64	          "id": 4,
65	          "parent": 0,
66	          "lang": "Latin",
67	          "refs": "AHD",
68	          "words": [
69	            {"translit": "vormîca, formica", "gloss": "ant", "script": null}
70	          ],
71	          "note": null,
72	          "quote": null
73	        },
74	        {
75	          "id": 5,
76	          "parent": 4,
77	          "lang": "French",
78	          "refs": null,
79	          "words": [],
80	          "note": null,
81	          "quote": null
82	        },
83	        {
84	          "id": 6,
85	          "parent": 5,
86	          "lang": "Persian",
87	          "refs": "MON",
88	          "words": [],
89	          "script_extra": "کلروفرم ، اسید فرمیک",
90	          "note": null,
91	          "quote": null
92	        },
93	        {
94	          "id": 7,
95	          "parent": 4,
96	          "lang": "English",
97	          "refs": "AHD",
98	          "words": [
99	            {"translit": "formic [acid]", "gloss": null, "script": null},
100	            {"translit": "chloroform", "gloss": null, "script": null}
101	          ],
102	          "note": null,
103	          "quote": null
104	        }
105	      ]
106	    },
107	    {
108	      "root": {
109	        "name": "Moudh, Moudhiô",
110	        "lang": "Indo-European",
111	        "refs": "IEC:802",
112	        "gloss": "to mourn"
113	      },
114	      "nodes": [
115	        {
116	          "id": 1,
117	          "parent": 0,
118	          "lang": "Avestan",
119	          "refs": "HRN:224",
120	          "words": [
121	            {"translit": "môy", "gloss": "groaning", "script": null},
122	            {"translit": "a-mayavâ", "gloss": "grief", "script": null}
123	          ],
124	          "note": null,
125	          "quote": null
126	        },
127	        {
128	          "id": 2,
129	          "parent": 1,
130	          "lang": "Pahlavi",
131	          "refs": "HRN:224; FFD:77; MON",
132	          "words": [
133	            {"translit": "môy, môyak", "gloss": "groaning", "script": null},
134	            {"translit": "must", "gloss": "groaning, complaint", "script": null}
135	          ],
136	          "note": null,
137	          "quote": null
138	        },
139	        {
140	          "id": 3,
141	          "parent": 2,
142	          "lang": "Persian",
143	          "refs": "HRN:224; FFD:77; MON:4080,4433,4455; IEC:802",
144	          "words": [
145	            {"translit": "mŭy-îdan", "gloss": "to cry", "script": "موییدن"},
146	            {"translit": "most", "gloss": "groaning, complaint, sorrow", "script": "مُست ۲"}
147	          ],
148	          "script_extra": "مویه ، موی ، موژ ، موژه\nمُستمند",
149	          "note": "HRN:223 links these to Avestan \"amâ-yavâ:grief\". See root \"Ome\".",
150	          "quote": {"text": "من این مُست گران را با که گویم - من این بیداد را داد از که خواهم", "poet": "Vîs-o-Râmîn"}
151	        },
152	        {
153	          "id": 4,
154	          "parent": 0,
155	          "lang": "Old Iranian",
156	          "refs": "FFD:77",
157	          "words": [
158	            {"translit": "maud, mauda", "gloss": "to cry, to groan", "script": null}
159	          ],
160	          "note": null,
161	          "quote": null
162	        }
163	      ]
164	    },
165	    {
166	      "root": {"name": "Moudhiô", "redirect": "Moudh"},
167	      "nodes": []
168	    },
169	    {
170	      "root": {"name": "Mozgho", "redirect": "Mozgo"},
171	      "nodes": []
172	    }
173	  ]
174	}
175	
```


## [2026-09-07T17:36:15.832Z] TOOL CALL #4: Bash

```json
{
 "command": "ls tools/ && sed -n '1,120p' data/verification/sources/SOURCE_MATRIX.md"
}
```


### [2026-09-07T17:36:15.879Z] TOOL RESULT

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
```


## [2026-09-07T17:36:17.476Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','IEC','HRN','FFD','MON','BQT','SNS','AHD','WLD','BRT','PHD','NYB','CHEUNG','SYN','KLN','ARY','HUB','SKT','FSD','WEB']:\n    v=d.get(k)\n    print(k, json.dumps(v, ensure_ascii=False)[:400] if v else 'MISSING')\n\""
}
```


### [2026-09-07T17:36:19.532Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 
FFD {"title": "Mohsen Abolghasemi, Fe'l-ha-ye Farsi-ye Dari, Qoqnus, Tehran 1374/1995", "kind": "local_scan_ocr", "url": "https://asmaneketab.ir/product/کتاب-ماده-های-فعلهای-فارسی-دری-محسن-اب/ -> https://dl.eliteraturebook.com/app/public/attachments/6925d29630b83.PDF (free PDF site; grey)", "lookup_hint": "Searched archive.org (Persian/Latin titles, author), ketabnak, noorlib, general web (pdf/downloa
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
SNS {"title": "Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/VajnameShayest", "lookup_hint": "grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sou
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verific
CHEUNG MISSING
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-D
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-di
```


## [2026-09-07T17:36:39.647Z] TOOL CALL #6: Bash

```json
{
 "command": "sed -n '1,60p' tools/verify_check.py"
}
```


### [2026-09-07T17:36:39.689Z] TOOL RESULT

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
```


## [2026-09-07T17:36:40.082Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"moru\" POK_full.txt | head -40; echo ---; grep -n -i \"morwi\\|moru̯i\\|Ameise\" AHD_watkins1985.txt | head -20"
}
```


### [2026-09-07T17:36:40.147Z] TOOL RESULT

```
4718:{*meisula) morula^ a blackbird; a fish, the sea-carp ' (Kluge EWb.''2 s. v.) and cymr. 
4731:3|| 140, Fick l|4 205: morula from *misula, cymr. mwyalch etc from meisalka, finally, with - 
59903:muir- moru6s.). 
60100:ash-colored striped cow ', moraty^ black striped ', poln. morus^ sloven, untidy or dirty 
61301:Old Saxon moru.. Old High German muoru. 'moor, fen, sea'. Old Icelandic m0rri. 
61357:Latin morum " mulberry, blackberry ' gr. loanword, Latin das replacement of closed gr. o- 
61359:morumhas been absorbed from popov phonetically? from to mer-3S. 734? 
61370:Root / lemma: moruT- 
61374:Root / lemma: moruT- : ant, derived from Root / lemma: mai-1 : to cut down, work with a 
61587:Modern High German Mohr-rube, Mohre, Old English more, moru6s.. Late Old High 
78471:(through metathesis) Armenian mauruk', moruk' 'beard'; 
---
762:mizdho-. Reward. West Germanic *médé- in Old English méd, reward, compensation, meed: MEED. [Pok. mizdho- 746. m6-. To exert oneself. Suffixed form *mé-I- in: a. Latin molés, heavy bulk, mass, massive structure: MOLE%, MOLECULE; DEMOLISH; b. Latin molestus (irregularly from mdélés), labored, difficult, troublesome: MOLEST. [Pok. m6- 746.] m6d-. To meet, assemble. 1. Germanic *mdtjan in Old English métan, to meet: MEET!. 2. Germanic *méta- in Old English mot, gemét (ge-, together; see kom), meet- ing, moot, assembly, council: MOOT; FOLKMOTE, GEMOT, WITENAGEMOT. 3. Perhaps suffixed zero-grade form *mod-tlo- in Germanic *mathla- in Old Norse mdl, speech, agreement (> Norwegian mdi, speech): MAIL; (BLACKMAIL), RIKSMAL. [Pok. mdd- 746.] modhro-. A color. Germanic *madraz in Old English meedere, madder: MADDER!. [Pok. modhro- 747.] molko-. Skin bag. Germanic *malhé- in Old High Ger- man malha, pouch, bag, akin to the Germanic source of Old French male, bag: Matti. [Pok. molko- 747.] mone. Neck, nape of the neck. 1. Germanic *man6 in Old English manu, mane: MANE. 2. Latin monile, necklace: MONILIFORM. [Pok. mono- 747.] mori-. Body of water; lake (?), sea (?). 1. Germanic *mari- in: a. Old English mere (> Middle English mere), sea, lake, pond: MERE?; (MERMAID); b. Old Norse marr, sea, akin to the Scandinavian source of MARRAM; C. Old High German mari (> German Meer), sea: MEER- SCHAUM. 2. Germanic *mariska-, water-logged land, in: a. Old English mersc, merisc, marsh: MARSH; b. Old French marasc, maresc, marsh: MORASS. 3. Latin mare (> French mer), sea: MARE?, (MARINARA), MARINE, MARI- TIME; BECHE-DE-MER, MARICOLOUS, MARICULTURE, OR- MER, ULTRAMARINE. [Pok. mori 748.] mormor-. Also murmur-. Murmur. Imitative root. Latin murmur, a murmur: MURMUR. [Pok. mormor- 748.] moro-. Blackberry, mulberry. 1. Greek moron, mulberry, in sukomoros, an African fig tree: SYCAMORE. 2. Latin morum, mulberry (probably from Greek): MORULA, MUR- REY; MULBERRY. [Pok. moro- 749.] morwi-. Ant. 1. Germanic variant form *meur- in Danish myre, ant, akin to the Scandinavian source of Middle English mire, ant: PISMIRE. 2. Variant form *morm- in: a. Greek murméx, ant: MYRMECO-; b. (with dissimila- tion) Latin formica, ant: FORMIC, FORMICARY; FORMICI- vorous. [Pok. morui- 749.] m6(u)lo-. Name of a plant. Greek mélu, moly: MOLY. [Pok. mé(u)-lo- 750.] m6(u)ro-. Foolish. Greek méros, foolish: MORON; OXYMO- RON. [Pok. mé(u)ro- 750.] mozgo-. Marrow. Germanic *mazg6- in Old English mezrg, mzerh, marrow: MARROW. [Pok. moz-g-o- 750.] mregh-m(n)o-. Brain. 1. Germanic *brag-na- in Old English bregen, brain: BRAIN. 2. Greek bregma, the front part of the head: BREGMA. [Pok. mregh-m(n)o- 750.] mregh-u-. Short. I. Suffixed form *mregh-w-i- in Latin brevis, short (> briima, the shortest day, winter): BRIEF, BRUMAL; ABBREVIATE, (ABRIDGE). II. Zero-grade form *“mrghu-. 1.Germanic *murgja-, short, also pleasant, joyful, in: a. Old English myrge, mirige, pleasant: MERRY; b. Germanic *murgithd, pleasantness, in Old English myrgth, pleasure, joy: MIRTH. 2. Greek brakhus, short: BRACHY-; AMPHIBRACH, TRIBRACH. 3. Greek com- parative brakhion, shorter, hence also “upper arm” (as opposed to the longer forearm): BRACE, BRACERO, BRA- CHIUM, BRASSARD, BRASSIERE, PRETZEL; EMBRACE. [Pok. mreghu- 750.] mu'-. Imitative of inarticulate sounds. 1. Reduplicated form in Germanic *mum- in: a. Middle Low German mummen, to be silent, akin to Middle English mum, silent: MUM}; b. Icelandic mumpa, to eat greedily, akin to the probable Scandinavian source of dialectal English mump, to mumble, grimace: MUMPs; c. Low German
1533:FORE- pert FORECLOSE dhwer- FOREFATHER per, peter- FOREGO! ghé- FOREIGN dhwer- FOREMOST per! FORENSIC dhwer- FOREST dhwer- FORESTALL | stel- FORFEIT dhé-1, dhwer- FORFICATE bherdh- FORGE! dhabh- FORGET ghend- FORGIVE ghabh- FORGO ghé- FORLORN leu-! FORLORN HOPE keu-?, leu-1 FORM merph- FORMAL merph- FORMER? per! FORMIC morwi- FORMICARY morwi- FORMICIVOROUS morwi- FORMULA merph- FoRNAX gWher- FORNICATE gWher- FORSAKE sag- ForT bhergh-2 FORTALICE bhergh-2 FORTE! bhergh-2 FORTE? bhergh-2 FORTH pert FORTIFY bhergh-2 FORTIS bhergh-2 FORTISSIMO bhergh-2 FORTITUDE bhergh-2 FORTRESS bhergh-2 FORTY kWetwer- FORUM dhwer- Fossa bhedh- FOSSE bhedh- FossIL bhedh- FOSSORIAL bhedh- FOSTER pa- FOUDROYANT bhel-1 FOUL pu-2
1898:MUSTARD meu- MUSTELINE mis- MUSTER men-! MUSTY meug-2 MUTATE mei-1 MUTCHKIN med- MUTE mul- MUTILATE mut- MUTTER mul- MUTTON mel-1 MUTUAL mei-1 MUZHIK man-1 MUZZLE musum MY me-1 MYCELIUM walso- -MYCETE meug-2 MYCO- meug-2 MYCORRHIZA wrad- MYELO- mis- MYIASIS § mu-2 MYLONITE mele- MYNA mad- MYNHEER me-1 MYO- mis- MYOCARDIUM kerd-1 MYOPIA mut-, okw- MYOSOTIS miis-, ous- MYRIAD meu- MYRMECO- morwi- MYROBALAN gWel@-2 MYSELF me-! MYSOPHILIA meu- MYSOPHOBIA meu- MYSTAGOGUE ag- MYSTERY! mut- MYSTERY? mei-2 MYSTIC mul- MYSTICETE miis- MYTHOPOEIC kWeij-2 MYXO- meug-2
2097:PIQUE (s)peik- PIRATE per-4 PIROG pd(i)- PISCARY peisk- PISCATORIAL peisk- Pisces peisk- PISCI- peisk- PISCINA peisk- PISCINE peisk- PISMIRE morwi- PISTIL peis-1 PISTON peis-1 PIT! peu-
```


## [2026-09-07T17:36:47.606Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '61360,61420p' POK_full.txt"
}
```


### [2026-09-07T17:36:47.654Z] TOOL RESULT

```
Maybe truncated alb. (*M6pov) man^ mulberry ', mana-ferre^ dewberry, blackberry ' {man 
' mulberry ' + ferre^ shrub ') a Greek loanword; 

From Latin derive Old High German mur-, morbere. Middle High German mulber^ 
mulberry ' and Lithuanian moras 6s. 

References: W P. II 306, WH. II 114, Specht Indo Germanic Dekl. 119. 
Page(s): 749 

Root / lemma: moruT- 

Meaning: ant 

Root / lemma: moruT- : ant, derived from Root / lemma: mai-1 : to cut down, work with a 

sharp instrument, ant. 

Note: distorted taboo uormo-, mormo-, mouro- [Qermauxc also meuro^ 

Material: attributable to mo/yT-are. Avestan /77ac»/>'^ (secondary m. maurvay-), sogd. 'm'wrc 

f., npers. mor^ ant '; 

Maybe expressive -/r-in alb. morr' louse '. 

Old Irish moirb, PI. cymr. myrion, bret. merien, corn, muryon. Old Bulgarian mravi{o\}\. of 
it reshaped russ. muravej, slov. mrav, Bulgarian mravija). 

In /770/777-; Latin formica {compare to phonetically above Latin formTdd:qx. (jopijcb); gr. 
|jup|Jog (Lycophr.), |jup|jr|^, Doric Muppa^ (/r-extension to a-stem, as opplKag Latin formica. 



Old Indie valmT-ka-io astern, and Old Indie vamra-kaio ostem); unclear Armenian mrjiun 
{*murjimno-). Gen. mrjman. 

Maybe Italian formica : Spanish hormiga : French fourmi : Asturian formiga : Bergamasco 
fijrmiga : Bolognese furmTga : Bresciano : furmiga : Welsh morgrugyn; myrionyn; 
myrionen; myr : Breton merienenn : Albanian {* merienenn) milingone : Calabrese 
furmicula : Catalan formiga : Dzoratai fremi; froumi : Furlan furmie : Galician formiga : 
Greek Muppn^ '■ Greek puppnyKi : ( > alb. merimanga, miremanga, milimanga, merimajka^ 
spider') = Griko Salentino mermico : Latin formica : Leonese formiga : Lombardo 
Occidentale formiga : Napulitano furmfcula : Portuguese formiga : Reggiano : furmiga; 
furmia : Romagnolo furmiga : Romanian furnica : Romansh furmicia : Sardinian 
Campidanesu fromiga : Sicilian fummicula : Valencian formiga : Venetian formiga; 
formigola : Viestano furmich' : Wallon furmi : Zeneize formigoa ' ant'. 

In uorm-, gr. puppa^, popija^ Hes. (p- Schriftbehelf for F, compare also 6piJiKa(; MUPMH^ 
Hes.); Old Indie valmTka- m. ' ant heap '; besides with totally single sound result vamra-vn., 
vamni. ' ant '. 

Auf mouro-: 0\d Icelandic maurr, besides *meur-\n Danish myre, Swedish myra 
{*meuridn-). Middle Dutch PI. mure {once covered) miere. Modern Dutch mier. Middle Low 
German m/re {to /~s. van Wijk), Middle English m/'re, /t?//*© (Scandinavian loanword), Old 
English myre, engl. m/'re, nowadays only still p/s-m/re {vom Ausspritzen ihrer Saure), 
Crimean Gothic miera. 

References: WP. II 306 f., WH. I 531 f., Trautmann 170, Specht Indo Germanic Dekl. 45. 
Page(s): 749
```


## [2026-09-07T17:36:49.253Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"maoiri\\|maoiri-\\|môr\\b\" BRT.txt | head -20; echo === PHD; grep -n -i \"^mōr\\|mōr \\|mwlc\\|mōrčag\\|mōrč\" PHD.txt PHD_mackenzie.txt | head -20"
}
```


### [2026-09-07T17:36:49.311Z] TOOL RESULT

```
Exit code 1
5285:•  j.  araeka-  Adj.  -  ?  -,  Bez.  einer  Ameisen- art: maoirinqm  'kanam  kutakanqm  duzai- ninqm  V.  74. 5.
11356:paitis  , .  zbayeiti  . .  yim  *driyBsat  . .  sba- yäti  Yt  10.  84;  —  %wqm  yazSnte  .  .  dai- AAu.paiays  . .  '^wqm  naraHt  ySi  taxma Jai'jyhnte  Yt  5.  85  f;  —  haraiti  bars  .  . kä  Aama  päirisSite  frSpayä  (sd.)  . ,  M3r?- fiaaS  gairis  . .  AämS  hasHt  päirisaile  .  . "das  jy.-Gebirg  . ,  umlagert  . . ;  . .  das  Z.- Gebii^,  auch  das  umlagert  . ."  Yt  ig.  i; y- 69;  —  Vlspe  ,.  tirKtnti  pfnmne  {%äj) avaia  mävayaiit.-tprisantu  Yt  14.38;  — *daSinqtn..Äaoyqm  h! paiayqm ..  dumtnüit Af  upa.%w^r^saym'V.i3.ai.;^vlsfe  haoma . . yaicit . .*upa  *dintäku{sA.)  V./0.17J  — Aazaignrn  maoirinqm  d3nS.karSanqm  ava.- jartyat  duye  hazanre  anyalsamat'-'^  V.  18. 73i  73i  —  ^y^  *gr}Amö  ä.ASi^Si  (sd.) «r  ksvayas^l  xratül  «r  dadat  ".  .  Gr., de^leichen  (sva,  und)  die  K.  richten  .." Y.  J2.  14; —  aSavatca  alsasät  ästärayeite (sd.)  N.72; — nava..anaiwyasHi  kunämi; hinti  (Sp.  370  o.)  .  .  mävayacit  ca^warS arsäna  V.lS.^j;  —  ksnti  anyäsät'^  (Sp. 137  in.)  asäs^a  /äi^ris^a  srIras/a..Y.l.2o; —  aam^i  akyS  . .  %wam  tUSökj  , .  vai- <hm  (sd.)  Y.  ig.  10;  —  mainya  .  .  yS  ä narSm(,sd.)ät.,Aäi>0  Y.^i.y  i — in  auffälliger Stellung:  mUca  paslaSa  mazdayasna  vXmä- oasHt*^  vTmSoayanta  "nicht  sollen  sie  dann auch  bei  M.  als  Ärzte  praktiziren"  V.  7, 38;  38,  40;  —  hinter  ula^^:  iavaj  aiwi.- vanyä  .  .  ta^ryävanttm  , .  ptiatamca  .  . Uta  anyäscit'^  ..  kyaon&tgkB  Wtig.ST, 89;  —  hasannm  aspä  uta  äsitqmHt /rastUntim  Yt  18.  5 ».  a)  Bei  hypotak- tischer Saufiigung  steht  das  mit  /■■  hervor- gehobene Wort  jeweils  an  zweiter  Stelle*', U2W.  a)  des  Hauptsatzes;  b)  im  Aw.: Sfit  MOra^uslrS  da^äU  sanm  vyämrvUä .  .  flS-a  *aspm^  .  .  vlinruyg  Y.  12.  6\  — ya'ha    . .    kvarsxiatä^m    .  .  fraca    Siti  .  .
13402:•  j.  (0n5.kars-Adj.'(Getreide)kömer(ver)- schleppend',  Bezeichnung  einer  Ameisen- art*': maoirJm  °spm  Y.iö.ia; — maoirinam ■!„nqm  V.J4.S.  'i«  73-
20075:j.  maurvay-  m.'>  'Ameise',  ein  daemscbes Tier,  von  dem  zwei  Arten  geschieden werden:  xrafstnm  ava.Janalta  moffifftn danHjtarsim  (sd.)  V.  16.  la;  —  hagvan maoirinam  danS.iarsanqm  ava.Janyat  V. 14.S1  ^o-73i  —  baiiian  maoirinqm  arai- kanqm  (sd.)  kutakanqm  duiaininqm  ava.- /anyai\:i4.$.
(eval):1: == not found
```


## [2026-09-07T17:37:03.353Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Ameise\" BRT.txt | head -20; echo === PHDgrep; grep -n -i \"ant\\b\" PHD_mackenzie.txt | grep -n -i \"m\" | head -5; echo ===; grep -n -i \"mwlc\\|mōrč\\|morc\\|mwl \" PHD_mackenzie.txt PHD.txt | head"
}
```


### [2026-09-07T17:37:03.410Z] TOOL RESULT

```
Exit code 1
5285:•  j.  araeka-  Adj.  -  ?  -,  Bez.  einer  Ameisen- art: maoirinqm  'kanam  kutakanqm  duzai- ninqm  V.  74. 5.
13402:•  j.  (0n5.kars-Adj.'(Getreide)kömer(ver)- schleppend',  Bezeichnung  einer  Ameisen- art*': maoirJm  °spm  Y.iö.ia; — maoirinam ■!„nqm  V.J4.S.  'i«  73-
13403:*)  Die  Zoologen  des  Awesta  haben  offenbar die  Puppen,  die  die  Ameisen  in  die  Sonne  tragen, für  geraubte  Getreidekürner  angesehen.
13812:*>   Vgl.    Bd.  74-  19:    J'^a^   (in    Aw.-Buchst.) i/  xärpuSt   (=  np.  xStpasi  'Igel')  i^änend',    lg. £Ü    gilt    der    Igel    als    .ipezi elter   Gegner    der Ameisen ;  iäiak  fa  AamislJriA  1  mör  i  i/änai  t:s da    eslel,    H^ön   xdwet   ku    iälai    Aar  *iärak  *i  1 andar  mar  xSHoi  i  mizet  (ü)  lOCO  mar  iaHft. KorapA.   —   Et.?    Vgl.    HORN   KZ.  J^.  437, 1 HBM.AGT.AI4l.VI!.Va/+»fl*fl.'derRch]imme Haken  (Stacheln)  hat'7  -  mp.  (Pü.):  iüSal;  np.  I £uia;  A3;similation  der  silbenanl.  Kons. ■  j.  duzakö.sayana-  Adj.  'wo  der  Auf- enthalt, dieHeimat  desIgels  isf :  i'alk^ntim (sd)  yim  -mm  V,  /.  9.
20075:j.  maurvay-  m.'>  'Ameise',  ein  daemscbes Tier,  von  dem  zwei  Arten  geschieden werden:  xrafstnm  ava.Janalta  moffifftn danHjtarsim  (sd.)  V.  16.  la;  —  hagvan maoirinam  danS.iarsanqm  ava.Janyat  V. 14.S1  ^o-73i  —  baiiian  maoirinqm  arai- kanqm  (sd.)  kutakanqm  duiaininqm  ava.- /anyai\:i4.$.
21263:. ,  aparaöhayäe  y  v  naimsm  y  v  ä«'- /um  y  V  cahru/um  y  V  paatartkum '^■ig.y,  Y.6.32*,  l6.2*; — yä  *xsudra(ßd.) *y'il  y  yazmti  y  v°  *hqm.ralhwpnii y'v' ..  N.  61.  n)  in  aülimiliger  Ver- wendung; xrafstrMn  ava.janaita  maotrim dänSjiaritm  y"  v'  hama  duyt  laile  kahyä- cit  .  .  xrafstranqm  ava.janyät  y  v  .  . zaOta  "das  Xr.-Geschmeiss,  die  kömer- schleppende  Ameise  soll  er  im  Sommer töten,  zweihundert  Stück,  dagegen  (zwei- hundert Stück)  beliebiger  Xr.s  soll  er  im Winter  töten"  V.  16. 12  {?).
(eval):1: == not found
```


## [2026-09-07T17:37:04.102Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"moru\\|morwi\\|formica\" IEC.txt | head -20; echo === SYN; grep -n -i \"formica\\|myrmex\\|ant\\b\" SYN.txt | head -10"
}
```


### [2026-09-07T17:37:04.156Z] TOOL RESULT

```
Exit code 1
10336:mär- (mər-, maronio) ‘harass, torture, kill. Cf. máruos (moruos), mruos, mrið, mrtis, etc. Skt. maráyami, v. “kill; Gk. maraíno ‘quench, quell; languish, die’; Cz. motit, inf. ‘exhaust, torture, kill beside Srb. mãriti, inf. “be con- cerned, worry’; ON mara ‘be awash, be water- logged'; Li. marinti, inf. ‘kil’; cf. also Hind. marnà, inf. ‘strike; Romani marav, id. (& “kilP)
10358:máruos (moruos, mruos) ‘dead, decayed, broken-down'. Cf. mruos, moros, us & moruos. WP II, 276. (Variant mris, io) Ligurian (in Rumansch) marv, -a, adj. ‘stiff with cold'; Olr. marb, Ir. marbh ‘numb, dead’; W marw, Br. maró, Cor. marow dead: OHG maro, gs *marwes ‘rotten, mellow’ beside mu- ruwi ‘mellow, crumbly’; MHG mürwe, wd: G mürbe, id.; Du. murw ‘tender, soft; LG, Sw. mör ‘crumbly, mellow’; Cz. mp ‘dead’; mrva ‘dung’; cf. Srb. mrva ‘crumb’; OCS mrúv-ica, id.; cf. Srb. (vowel?) marva ‘cattle’. (Variant of type mri-, mruio in OHG ei-muria, OE &- mege ‘embers’, if for *aidh-^, and Latv. miris, adj. "dead. cf. Li. mirimas ‘death’. For Fr. morve ‘snot, glanders' see smeruos, à. The variant vocalism seems to be present where two continuants are followed by Si or *-u-, but the evidence is inconclusive. A dative absolute formula occurs in Li. tévui mirus ‘the father having died’. Cf. ON moru-eldr ‘phosphorescence’, lit. ‘dead fire")
10658:mer- (mern-) (e-gde radical of type mr-, q. v. with extensions, and cf. mruos (moruos), etc. Per. cf. miram, inf. murdan die: Arm. mef- nim, meranim, aor, meraj, id.; merot, gs -i, ab. s. -av ‘mortal; Hitt. (queried) mernun, 1sg. (T die? or ‘cause to die") beside merr- die: W meru, inf. ‘droop’ beside merth, pl. -i, m. exhaustion’, fr. *mertis); Cor. cf. mernans, m. ‘death’; Latv. mernéju, et ‘starve’
10680:meruos, is limp, soft, weak’. Cf. máruos (mo- ruos), mruos & moruos Arm. cf. merav ‘dead’; Olr meirb ‘weak, slug- gish’; Ir. meirbh ‘limp, mild, sluggish, sultry’; W merw (and mert ‘limp; tasteless’; Sw mör, adj. ‘tender’, fr. *mourio- with metath.); Slo- vak cf. meravý ‘numb’. (An isophone occurs in Li. merva ‘gadfly’. Lalis. LW?). WP II, 276
10748:morios (mrios) "dead, deadly, mortal; death’. Cf. már-, mr- and moruos Skt. máryah “mortal man’; Av. mairyo dead. ly; Arm. majr, in the phr. i majr mtanem ‘extinguish’; W merydd ('sluggish', fr. *mo- I1io-)
10761:(moruos *withered, decayed, dead'. See má- ruos, meruo-, moru-, mru-)
11166:mormolos (mormoros) ‘murmur; humming creature, murmurer. Cf. murmur-, etc. Skt. marmarah ‘murmur, rustle’; Gk. cf. mor- moruzo ('frighten'. A formal equivalent, re- dup. to moros, q.v); Li. marmalas ‘gadfly’; cf. marmu, eti, v. ‘murmur’. WP II, 307
11177:(moruis, os, ios, iə "ant, see muruis, etc.)
11178:moruos ‘foul, decayed, dead’. Cf. máruos (moruos, mruos) and meruos, mrsos Av. cf. Mourus (name of a desert-town); Pahl. maruv-; OHG maro, gs marawes, adj. ‘rotten’; OE mear ‘weak, ailing’; Slovak cf. morava ‘lea, grassland’. (Vocalism ambiguously *-o- or *-á- (*-o-))
11305:mruos, ios (moru-) ‘waste, dead, decayed, rotten’. See máruos. Zero-grade in OHG muruwi, adj. ‘mellow, soft, friable, frail; MHG mürwe, wd: G mürbe, mürb; Du. murw & morw, id.; LG & Sw. mór, id.; Cz. mrv- iti, v. ‘dung’; Srb. cf. marva ‘cattle’; Latv. cf. (for vowel) miris, adj. "dead. WP II, 276
11411:myr, myrion, morion, pl. ‘ants’; Br. mérion, mérien, id.; EME mire ant beside piss-mire, id.; Sw. myra, f. (1) “ant; Icel. mor, n. (1) ‘swarm’; OCS mravij, f. ant Srb. mráv, gp mravi, id., R muravéj, muràš, m. id.; Big. mràva, f. id. Variants w. vocalism *-eu-/-ou- in Du. mier, f. id. beside ON maurr, m. id. and (ambig.) Av. maoiris, m. id., and of type *moru- in Olr. & Ir. moirb: Li. marva ‘gadfly’. (For the semantics, cf. Blg. mravulja, v. *swarm')
12917:piplàio, piplió (1) 'idle, tinker, potter, trifle’. Cf. pipolos ON fifla, wv. ‘beguile’; mod. ‘dally’; Cz. pip- lat, inf. ‘tinker, potter; Blg. cf. páplja, v. (swarm, crawl'. Semantics of Fr. fourmiller & Lat. formica ‘ant’, and cf. Skt. pipilih ant: Li. cf. pyplineti, inf. ‘ramble, roam’
(eval):1: == not found
```


## [2026-09-07T17:37:11.841Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"maoiri\" BRT.txt | head; echo === col; grep -n \"mōr\\|mor \" PHD_mackenzie.txt | head -20; echo ===PHDfile; grep -n \"ant$\\|ant,\\| ant \" PHD.txt | sed -n '1,40p'"
}
```


### [2026-09-07T17:37:13.258Z] TOOL RESULT

```
Exit code 1
5285:•  j.  araeka-  Adj.  -  ?  -,  Bez.  einer  Ameisen- art: maoirinqm  'kanam  kutakanqm  duzai- ninqm  V.  74. 5.
11356:paitis  , .  zbayeiti  . .  yim  *driyBsat  . .  sba- yäti  Yt  10.  84;  —  %wqm  yazSnte  .  .  dai- AAu.paiays  . .  '^wqm  naraHt  ySi  taxma Jai'jyhnte  Yt  5.  85  f;  —  haraiti  bars  .  . kä  Aama  päirisSite  frSpayä  (sd.)  . ,  M3r?- fiaaS  gairis  . .  AämS  hasHt  päirisaile  .  . "das  jy.-Gebirg  . ,  umlagert  . . ;  . .  das  Z.- Gebii^,  auch  das  umlagert  . ."  Yt  ig.  i; y- 69;  —  Vlspe  ,.  tirKtnti  pfnmne  {%äj) avaia  mävayaiit.-tprisantu  Yt  14.38;  — *daSinqtn..Äaoyqm  h! paiayqm ..  dumtnüit Af  upa.%w^r^saym'V.i3.ai.;^vlsfe  haoma . . yaicit . .*upa  *dintäku{sA.)  V./0.17J  — Aazaignrn  maoirinqm  d3nS.karSanqm  ava.- jartyat  duye  hazanre  anyalsamat'-'^  V.  18. 73i  73i  —  ^y^  *gr}Amö  ä.ASi^Si  (sd.) «r  ksvayas^l  xratül  «r  dadat  ".  .  Gr., de^leichen  (sva,  und)  die  K.  richten  .." Y.  J2.  14; —  aSavatca  alsasät  ästärayeite (sd.)  N.72; — nava..anaiwyasHi  kunämi; hinti  (Sp.  370  o.)  .  .  mävayacit  ca^warS arsäna  V.lS.^j;  —  ksnti  anyäsät'^  (Sp. 137  in.)  asäs^a  /äi^ris^a  srIras/a..Y.l.2o; —  aam^i  akyS  . .  %wam  tUSökj  , .  vai- <hm  (sd.)  Y.  ig.  10;  —  mainya  .  .  yS  ä narSm(,sd.)ät.,Aäi>0  Y.^i.y  i — in  auffälliger Stellung:  mUca  paslaSa  mazdayasna  vXmä- oasHt*^  vTmSoayanta  "nicht  sollen  sie  dann auch  bei  M.  als  Ärzte  praktiziren"  V.  7, 38;  38,  40;  —  hinter  ula^^:  iavaj  aiwi.- vanyä  .  .  ta^ryävanttm  , .  ptiatamca  .  . Uta  anyäscit'^  ..  kyaon&tgkB  Wtig.ST, 89;  —  hasannm  aspä  uta  äsitqmHt /rastUntim  Yt  18.  5 ».  a)  Bei  hypotak- tischer Saufiigung  steht  das  mit  /■■  hervor- gehobene Wort  jeweils  an  zweiter  Stelle*', U2W.  a)  des  Hauptsatzes;  b)  im  Aw.: Sfit  MOra^uslrS  da^äU  sanm  vyämrvUä .  .  flS-a  *aspm^  .  .  vlinruyg  Y.  12.  6\  — ya'ha    . .    kvarsxiatä^m    .  .  fraca    Siti  .  .
13402:•  j.  (0n5.kars-Adj.'(Getreide)kömer(ver)- schleppend',  Bezeichnung  einer  Ameisen- art*': maoirJm  °spm  Y.iö.ia; — maoirinam ■!„nqm  V.J4.S.  'i«  73-
20075:j.  maurvay-  m.'>  'Ameise',  ein  daemscbes Tier,  von  dem  zwei  Arten  geschieden werden:  xrafstnm  ava.Janalta  moffifftn danHjtarsim  (sd.)  V.  16.  la;  —  hagvan maoirinam  danS.iarsanqm  ava.Janyat  V. 14.S1  ^o-73i  —  baiiian  maoirinqm  arai- kanqm  (sd.)  kutakanqm  duiaininqm  ava.- /anyai\:i4.$.
(eval):1: == not found
```


## [2026-09-07T17:37:16.719Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls | head -60; echo; wc -c PHD*.txt NYB*.txt 2>/dev/null"
}
```


### [2026-09-07T17:37:16.756Z] TOOL RESULT

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

 609465 PHD_mackenzie.txt
 609465 PHD_pages.txt
 340898 PHD.txt
    146 NYB.txt
 504627 NYB_vol1.txt
 920054 NYB_vol2_glossary.txt
2984655 total
```


## [2026-09-07T17:37:22.343Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"mōr\\b\\|mōrčag\\|mwlc\\|mwlck\" PHD_mackenzie.txt | head -20"
}
```


### [2026-09-07T17:37:22.421Z] TOOL RESULT

```
1016:imurzidan, iimurz- [)mwlc-ytn l 1M )mwrz-yd, N -] forgive, pity, have
1056:an-Imurzid ['n'mwlcyt l I M 'n'mwrzCyd] merciless.
1057:an-amurzisn ['n'mwlcfn'] mercilessness.
```


## [2026-09-07T17:37:22.904Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"mōr\" NYB_vol2_glossary.txt | head -20"
}
```


### [2026-09-07T17:37:22.952Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-07T17:37:26.663Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^m[oō]\" PHD_mackenzie.txt | sed -n '1,80p'"
}
```


### [2026-09-07T17:37:26.710Z] TOOL RESULT

```
3584:mor [mwl I N -] ant.
3586:morwarid [mwlw'lyt 1M mwrw)ryd, N -] pearl.
3589:moy [mwd IN -] hair.
3590:moyag [mwdk I N maya] lamentation.
3592:moyen [mwdyn ] (made of) hair.
3594:moz [mwc I N --] banana.
3595:mozag [mwck , N moza] shoe.
7114:mobile wazisnig.                               mustard seed spandiin.
7115:mocker afsosgar.                               mutability wardisn(ig)ih.
7116:mockery afsos, riyahrih.                       muzzle poz(ag).
7117:moderate paymiinig.                            myriad bewar.
7118:moderation paymiin(igih).                      myrobalan halilag.
7119:modesty nang.                                  myrtle mord.
7120:modius griw.                                   mystery raz.
7121:moist naft, tarr, xwed.
7122:moisture nam, xwedih.
7123:monkey kabig.                                  nail mcx; (finger) naxun, sru.
7124:month miih, mahigiin.                          naked brahnag.
7125:moon iiyism, mah; full ...... purrmah;         name niim.
7127:more fray, freh, wes.                          narcissus nargis.
7128:moreover enyii.                                narrow tang.
7129:morning bamdiid.                               narrowness tangih.
7130:morocco leather saxtag.                        natural eihrig, gohrig.
7131:mortal anosxwar, gehanig, marg-                nature Cihr(ag), gohr(ag); ciyunih;
7133:mortar hawan; (lime) carGg.                    navel nMag.
7134:mosque mazgit.                                 navigable naydag.
7135:mosquito paxsag.                               near nazd(ik).
7136:most frahist.                                  necessary abiiyisnig; be ....., abayistan.
7137:mother miid(ar).                                 (andar) aMy-.
7138:motion jumbiigih, Jumbisn, rawisn;             necessity abayisn.
7140:mottled pes.                                   neck~guard griwban.
7141:mount barag, stor.                             need astiinag, niyaz.
7142:mountain gar, kOf.                             needle sozan.
9168:moyen                     \tUt6      mlEy
9174:moyag                      \il r6    namagi
9190:mor                        ~r6       mijfig
9241:moymard       l
```


## [2026-09-07T17:37:41.007Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^mus\\|^must\\|mustōmand\\|mustomand\" PHD_mackenzie.txt | head -20; echo \"--- pages tags\"; grep -n \"\\[pdf page\" PHD_pages.txt | awk -F: '$1>3560 && $1<3600' | head"
}
```


## [2026-09-07T17:37:42.061Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"maud\\|mud-\\|\\*mau̯d\" CHEUNG.txt | head -30"
}
```


### [2026-09-07T17:37:42.197Z] TOOL RESULT

```
3622:mustl-abarmand [mwstPPlm'nd] aggressive, aggressor.
3624:mustomand [mwst)wmnd I N mustmand] complaining, unhappy.
3629:must [mwst I N ---] fist.
3632:mustan, mal- [mwstn', m'l- IN .......] rub, sweep.
6204:clime kiswar.                            complaining garzisnig, mustomand.
7879:unhappy axwas, dusnim, mustomand.        valid wizurd.
9126:marg                     ~          mustomand        "~l""\e»t6
--- pages tags
```


### [2026-09-07T17:37:42.263Z] TOOL RESULT

```
17844:*maud? ‘to learn, teach’ 
17887:*maud ? ‘to mourn’ 
17906:correspondences cited by Pokorny: 743: Lith. maudziu (maüsti) ‘I long for’, Gr. 
17908:were from older *maud as assumed generally, they would be identical with the 
17909:semantically antonymous root *maud ‘to rejoice’ (Skt. mod), which is attested in 
17911:OP (*maudabaga- ‘who pleases God’, Mayrhofer 1973: 208, ad 8.1185). The co- 
17914:mourn’ (q.v.), which became contaminated with the antonymous root *maud ‘to 
34068:*maudabaga-, 271 
52589:maudZiu (maüsti), 271 
56343:*darH (s.v.), *maud (s.v.), 
57224:*maud, *zarH (s.v.)
```


## [2026-09-07T17:37:45.738Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '17835,17925p' CHEUNG.txt"
}
```


### [2026-09-07T17:37:45.787Z] TOOL RESULT

```
«PIE *meuk- ‘to take, untie, etc.’ > LIV: 443 f. | Pok.: 744 f. 

*IE COGNATES: Gr. uócoopnoa ‘I blow my nose’, Lat. e-mungö ‘I blow out, snuff’, 


Lith. maükti ‘to take off’ 
*REFERENCES: IIFL I: 401b; Werba 1997: 217 f.; Kiefer 2003: 201 


*maud? ‘to learn, teach’ 
*MIDDLE PERSIAN: (+ *ham-) MMP hmwc- ‘to teach’, (pass./inch.) MMP hmwxs- 


‘to learn [i.e. to be teached, instructed] > DMMPP: 179a 
(+ *ham-) Well attested: Pres.: IND. 15р. MMP hmwcym, BMP hmwcym /hammözem/, 3sg. BMP 
/hammozed/, 3р1. BMP hmwcynd /hammözend!, etc. 


*PARTHIAN: (+ *ham-) ’mwc- ‘to teach’ = Ghilain: 63 | DMMPP: 40a 


, 


Pres.: IND. 3pl. *’mwcynd, SUBJ. 25р. ’mwc’h; Partic.: perf. pass. ’mwxtg ‘learned’, "mwxt, П "mwc'd; 
Inch./Pass.: pres. IND. 3sg. ’mwxsyd, SUBJ. 3р1. hmwxs’nd; Inf.: *’mwxtn 

*SOGDIAN: BSogd. mwck, BSogd. mwck’, SSogd. mwz’’k’ ‘teacher’, (pl.) SSogd. 
*mwz'kty 

*CHORESMIAN: (+ *4- ?) "mxs- ‘to learn’, mwcy- (caus.) “to teach, instruct’ 
= Samadi: 113, 112 

*NWIR: Zaz. misayis/misen- (inch. ?) ‘to learn, experience’, misnayis/misnen- (caus.) 
‘to teach, show’, Awrom. mısäy/*mıs- ‘to learn, understand’ || (+ *à-) NP ämöxtan/ 
amoz-, Ham. ämotän/ämuz- ‘to learn; teach’ || (+ *fra- or *ham- ?) Anar. ihmut ‘he 
learnt’ || (+ *ham- ?) Kafr. hamiitemiin/hamis- ‘to learn’ 

*NEIR: (+ *ni-) Oss. L nymuzyn/nymygd, D. nimozun/nimugd ‘to point out; to carry 
to, out; to recommend’ 

9 The root is exclusively Iranian. It is perhaps no coincidence that it is formally 
similar to *jaué ‘to teach, learn’: таиё may have been abstracted from *ham-Hauc 
(cf. Skt. oc ‘to be accustomed, to get used to’), comparable to *iaué, which has been 
abstracted from prefixed formations in *abi-, *ni-, etc. (q.v.). 


“PIE LIV: — | Pok.: 
*REFERENCES: Zhukovskij II: 96; Ivanow 1926: 419; Abrahamian 1936: 107; MacKenzie 1966: 102; 
Abaev, Slovar’ II: 205; Paul 1998: 306a 


*maud ? ‘to mourn’ 
*MIDDLE PERSIAN: MMP mwy- ‘to mourn’, BMP mwst /must/ ‘mourning’ 


c DMMPP: 234b f. 


Pres.: IND. 3pl. MMP mwyynd, SUBJ. 1sg. MMP mwy’n; Partic.: pres. pl. MMP mwy’g’n, perf. pass. 
BMP mwst /must/ 


*maus(H) ? 271 


*NWIR: NP möyidan ‘to mourn; weep and cry aloud’, NP must ‘trouble, distress of 
mind, complaint, lamentation’ 

*MISC: ? Arm. (LW) moyr ‘begging’ (semantically not evident, Benveniste 1964: 5) 
© The Persian forms are isolated within Ilr.: they might be connected to the IE 
correspondences cited by Pokorny: 743: Lith. maudziu (maüsti) ‘I long for’, Gr. 
u$00c (m.) ‘word; tale’, OCS mysle ‘thought’, etc. However, if the Persian forms 
were from older *maud as assumed generally, they would be identical with the 
semantically antonymous root *maud ‘to rejoice’ (Skt. mod), which is attested in 
Iranian: not only in Avestan (maoóano.kara- “providing joy’), but apparently also in 
OP (*maudabaga- ‘who pleases God’, Mayrhofer 1973: 208, ad 8.1185). The co- 
existence of two formally identical roots with opposite meanings within one 
language is inconceivable. More likely, we are dealing with the root *nau(H) ‘to 
mourn’ (q.v.), which became contaminated with the antonymous root *maud ‘to 
rejoice’ at a certain stage. Cf. NP noyidan ‘to cry aloud, lament’, navistan ‘to groan’, 
NP nöyah ‘plaint, moan’, nöstah, navastah ‘noise in the throat by one’s crying’. 

*PIE — = LIV: — | Pok.: 743 


*REFERENCES: Horn 1893: 223 f. 


*maug (*mauz) ? ‘to err, be foolish’
```


## [2026-09-07T17:37:58.294Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"mūjīden\\|mūjīdan\\|mōjīdan\\|mūyīdan\\|mujiden\\|moyidan\" HRN.txt | head -20; echo \"-- leaves\"; grep -n \"\\[pdf page\\|leaf\" HRN.txt | head -3"
}
```


### [2026-09-07T17:37:58.357Z] TOOL RESULT

```
-- leaves
```


## [2026-09-07T17:37:59.069Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"mayava\\|amayava\\|a\\.mayava\\|mayavā\" BRT.txt | head -20"
}
```


### [2026-09-07T17:37:59.135Z] TOOL RESULT

```
10855:•  j.,  g.  xSi-  f  'Not,  Elend':  x^3  (GS.)''> dangSm  ayU  (sd.)  Umanhö  Y.31.20;  — paiiistaße  xsayasca  (GS.)''  amayavay&sla Y.7/.  17;  —  xUm^'>  F.J.
20310:•  j.  mäyav-  Adj.  '(in  besonderer  Weise und  Richtung)  geschickt,  gewandt;  findig*: nairyB.sanhasca  yS  'yus  Yt  10,  52.  VgL mayava-.
22701:•  j.  *vaya'vant-  Adj.  (fem.  *vai/T-)  'mit Vögeln  versehen,  bevölkert':  iä^a  asäum apa.jas3  sitibyasca  haca  gaomaiOhyaica *'vaitibyasca*^  Itaca  mayavaitibyas^a  (sd.) H.2. 16.
```


## [2026-09-07T17:38:05.257Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"amayav\\|amaiiauu\\|ämayav\\|maySva\\|mayäva\" BRT.txt | head -20; echo \"-- lemma mayava\"; grep -n \"mayava-\" BRT.txt | head -20"
}
```


### [2026-09-07T17:38:05.334Z] TOOL RESULT

```
4693:«  j.  amayavä-  f.  'Leid,  Drangsal':  paiti- staue  xlayasla  'vayasca  "um  zu  widerstehen dem  Jammer  und  Leid"  Y.'!.!"}.
10855:•  j.,  g.  xSi-  f  'Not,  Elend':  x^3  (GS.)''> dangSm  ayU  (sd.)  Umanhö  Y.31.20;  — paiiistaße  xsayasca  (GS.)''  amayavay&sla Y.7/.  17;  —  xUm^'>  F.J.
-- lemma mayava
20310:•  j.  mäyav-  Adj.  '(in  besonderer  Weise und  Richtung)  geschickt,  gewandt;  findig*: nairyB.sanhasca  yS  'yus  Yt  10,  52.  VgL mayava-.
```


## [2026-09-07T17:38:05.986Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls | grep -i hrn; wc -l HRN.txt; grep -n \"Klage\\|klagen\\|jammern\" HRN.txt | sed -n '1,30p'"
}
```


### [2026-09-07T17:38:06.044Z] TOOL RESULT

```
HRN.txt
23313 HRN.txt
1940:Klagen (Is. 14, 31 ; 15, 4, 5), nwXir:N2 (Is. 57, 13).
4357:aw. [//raos-, yraosyöii^ /jaosya- Vehklagend, heulend',
5723:646. {\)xär 'Klagen', zäri^ zäre^), zandefi.
5725:afy. Sarai 'klagen'; oss. d. zarw?, t. zarin singen'
7206:828. feryäd *Hilfe; Hilferuf, Klage.
7929:915. giristen, giristen *klagen, weinen', Impt. girl ^) girye,
7932:klagen (AV.), g(i)rt/TnUan (AV.) ; ai. [/^gar-, gpidti 'an-
8079:930. gile 'Klage .
8080:aw. gerezü" 'Klage', vergl. [/^gar2-, gerezaiti 'klagen';
8082:garhate 'klagen, anklagen' ^).
8083:kurd. gilt 'Klage', gire 'Streit'; oss. d. yärziin, t.
8665:997. möye 'Weinen, Klage', möylden,
8680:Torjammern', moiracik 'bettelnd' ; dazu auch np. mit st
8681:*Klage*, mustmeud,
9131:1054. nöylden 'klagen (Sahn. I, 183 Vers 986, Calc),
9132:necä 'Klage', nevtden, vergl. nevaliden, nallden.
10541:93. garzltan 'klagen, weinen; beichten^)', garz(i)sn,
10544:gdrhate 'klagen*.
```


## [2026-09-07T17:38:13.182Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '8655,8700p' HRN.txt"
}
```


### [2026-09-07T17:38:13.222Z] TOOL RESULT

```
küfai 'Maus, junge Ratte*; oss. d. miste, t. mist (189);
bei. musk, n. milsk (245).
996. möT 'Haar' ^).
g. mld.
phlv. mö, möd bezw. möf; bei. müd^ mtd, n. mi^
'Haar (eines Menschen), Ziegenhaar' (247).
i tritt sonst dialektisch im Np. nur für ursprüng-
liches ü, nicht für ö ein, doch giebt es Ausnahmen;
man wird also trotz g. bei. mtd doch eine ap. Grund-
form *mauda- annehmen müssen 2).
997. möye 'Weinen, Klage', möylden,
aw. vergl. amayavä' 'Leid'; phlv. wöyaÄ:; ai. vergl.
dmtvä'.
Die von Darmesteter, Et. ir. H. 169, ver-
glichenen aw. ai. Worte lassen sich mit np. möye
lautlich nicht vereinigen, und auch Bartholomae,
») Reimt auf röt, 8ähn. III, 1074 Vers 161, auf jöi, Vis und
RAmln, Seite 84 Yers 16.
*j Ganz unmöglich ist Spiegel 's Erklärung, Ar. Per. 61 (vergl.
Bartholomae, ZDMG. 42, 155^.— 224 —
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
```


## [2026-09-07T17:38:35.266Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"moudh\\|moudos\\|moudi\" IEC.txt | head -20"
}
```


### [2026-09-07T17:38:35.338Z] TOOL RESULT

```
11221:moudh-, moudhio ‘ponder, long, mourn, flag, reflect upon'. See Supt: M Per. cf. mūyah ‘sadness, lament’; Go. maud- jan, v. ‘remember’; OCS cf. mudü, adj. “be- hindhand, sluggish'; muZdo, muditi ‘dawdle’; Big. cf. müden ‘sluggish’; Slovene muditi, inf. ‘retard; dally, waver’; Li. maudZiü, maüsti ‘ache; long, yearn' beside ap-maudüs ‘glum’; áp-maudas, -mauda, mf ‘sulks’
```


## [2026-09-07T17:38:35.465Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"meu-d-\\|meud-\\|meudh\" POK_full.txt | head -20"
}
```


### [2026-09-07T17:38:35.525Z] TOOL RESULT

```
60507:from *mu-n-d-os{-d-\.o root extension meu-d-) in tlie meaning " washed, made clean ' 
60513:1. meu-d-; mud-ro-3\er\, awake, smart' (compare "humid, wet-cheerful').
```


## [2026-09-07T17:38:42.519Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '60495,60560p' POK_full.txt"
}
```


### [2026-09-07T17:38:42.574Z] TOOL RESULT

```
Maybe alb. Geg myt, Tosc mt>yt' drown, strangle ' a Slavic loanword? 



with. ani. 5- Latvian smau//s' ein schmutzig gewordener', smu/et' befoul ', smu//s'a 
sloven '; 

poln. kir. /77^/ "slime, mud', russ. dial. mu//tb {vodu) "(water) go cloudy ' {mou-lo-); forms 
with A-suffix, respectively ^-extension see below; 



from *mu-n-d-os{-d-\.o root extension meu-d-) in tlie meaning " washed, made clean ' 
also Latin mundus^ clean, cleanly, nice, neat, elegant, toilet ornament, decoration, dress 
(of women), the world, earth, inhabitants of the earth, mankind ' (after gr. K6apo(;); 

B. extensions: 

1. meu-d-; mud-ro-3\er\, awake, smart' (compare "humid, wet-cheerful'). 

Old Indie mudira-m. "cloud', lex. also "frog'; in addition Old Indie m6date^\s funny', 
moda-m., modana-n. "lust, cheerfulness ', Avestan maodano-karana-^ causing lust ', Old 
Indie /77^o''//a "blithe, glad', Avestan a-h§musta- {*a-sam-musta-) " disgusting, unsavory, 
distasteful'. Old Indie mud-, mudalust, pleasure, joy', mudra-' funny '; 



gr. |ju^w {*mudjd) "suck', [juSoc; m. " damp, decay ', puSau) "be humid, wet, decayed ', 
Mu5aA£0(; "humid, wet' (hom. u: through metr. lengthening, whereupon newer puSaivoj " 
irrigate '); 

Latin mundus {see above meu-)\ 

Middle Irish muad {*moudo-) "pure, stout, proud'; 

Middle Low German muten^ wash the face ', Old High German muzzan^c\eav\\ 
Swedish dial, muta^ fine rain', Dutch /77c»/"fine rain'; 

with ani. 5-engl. smut^ smirch, stain, splotch ', Middle High German smuz. Modern High 
German Schmutz, Middle English smotten, smoteren " befoul '; 

Lithuanian mudrus, Latvian mudrs^a\ert, awake, smart' (: Old Indie mudra-), Lithuanian 
mudrinti, Latvian mudfV set in motion '. 

From in -es-stem m(e)udes-\\3Ne derived: 

Latin mustus {*muds-to-s) " young, new, fresh ' (originally "damp, humid, wet'); gr. puao(; 
(*|ju5ao(;) n. " maculation, blemish'; [juaap6(; " dishonorable '; Old Irish /77c»ss5c/7 "impure, 
unclean' {*mud-s-ako-), cymr. mws, bret. mous ds.; ndd. muss/g'd\(iy, filthy'; russ. muslitb 
" drool, drivel, slaver ', musljaki, " dribbler, unclean person'. 

Maybe alb. /77i/s/7/"must, new wine' a Latin loanword. 

2. meug-, meuk-^ slippery ' see below esp. headword. 



3. meu-r(o)-e\.c.: 

Armenian /770/''smut, swamp, marsh' {*m9u-ri-l), mrur^ deposit ' {*murui)\ gr. pupco 
(*[jupju)), pupofjai " let flow, weep, cry', aAi-|Jupn£ic; ' flowing to the sea '; whether here 
Mupio(; " eternal, infinite, endless ', [jupioi '10.000'? Latin muria' brine, pickle '? Lithuanian 
murstu, murtr become soppy ', m. PI. mauraf duckweed, stemless water plant ', Latvian 
maursm. 'lawn', Lithuanian /77a^/'as 'slime, mud', ablaut, murasxu. 'smut', Latvian murfV 
befoul '; russ. murvn. muravat ' oat-grass, false oat, tall oatgrass ', dial. ' mildew ', muryj' 
dark grey ', etc.; compare S. 741 Middle Irish mur^sWme, mud'.
```


## [2026-09-07T17:38:43.502Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=11150 && NR<=11230' IEC.txt | grep -n \"^[0-9]\\{3,4\\}$\\|page\" | head; echo \"--- nearby page markers\"; grep -n \"^80[0-9]$\" IEC.txt | sed -n '1,20p'"
}
```


### [2026-09-07T17:38:44.881Z] TOOL RESULT

```
13:798
21:799
40:800
49:801
65:802
76:803
--- nearby page markers
11189:800
11198:801
11214:802
11225:803
11242:804
11254:805
11274:806
11282:807
11296:808
11302:809
```


## [2026-09-07T17:39:01.020Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"mōr\\|mor\\b\\|mwlc\\|mwl\\b\" SNS.txt | head -20; echo \"--- pages\"; grep -n \"mōr\" SNS_pages.txt | head -10"
}
```


### [2026-09-07T17:39:01.089Z] TOOL RESULT

```
14168:.. ., *, ^i^mor than one place : ^j** 
--- pages
```


## [2026-09-07T17:39:01.729Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"maudjan\\|gamaudjan\\|meu-dh\\|meudh\" POK_full.txt | head -10; echo \"--- WLD moru\"; grep -n -i \"moru\\|Ameise\" WLD_band3.txt | head -20"
}
```


### [2026-09-07T17:39:01.791Z] TOOL RESULT

```
61115:|j09o(; m. ' discourse ', nuGsopai ' speak, think; consider'; Gothic maudjan, ga-maudjan' 
--- WLD moru
```


## [2026-09-07T17:39:07.176Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '61090,61135p' POK_full.txt"
}
```


### [2026-09-07T17:39:07.224Z] TOOL RESULT

```
(Lesbian pnvvoc;), Nom. Ionian \iz\c,, Doric \xr\(;, m. ' month ' {*mens), \xryjx\ (*|jr|vaa) 'moon'; 
alb. muai^ month ' ( */77d/7- from Indo Germanic *men-); lat mens/sm. ' month ' 
(conservative Gen. PI. mens-um), menstruus^ monthly ' (GN Mena\s gr. loanword), 
seme(n)stris^ 6-month, half-years of age, six-month-old ', Umbrian menzne^ mense '; Old 
Irish mT{*mens), Gen. mTs{*mensos), cymr. acorn, mis, bret. /77/z' month '; Gothic mena. 
Old Icelandic man!. Old English mona. Old Saxon Old High German /77a/7c»'moon' {-en- 
stem); Gothic menot^s. Old Icelandic manadr. Old English monad. Old Saxon manuth. Old 



High German manot, Modern High German month {*mendt-), Lithuanian menuo{*mendt), 
menes/sm. 'moon, month ', Latvian menes{/)s^ moon, month ' (dial. Lithuanian menas 
from a neutr. *menos). Old Prussian men/'ns' moon'; Old Bulgarian mes^cbm. 'moon, 
month ' ( *mes-n-ko-)\ 

Tocharian A man^ month ', man nkat'moon' (= ' month god '), B mene' month ', mem 
'moon'. 

References: WP. II 271 f.. WH. II 71 f., Trautmann 179 f., Brandenstein Studien 11 f. 
Page(s): 731-732 

Root / lemma: meuA^-, mauA^-, mud'^- 
Meaning: to complain or care about smth. 

Material: Npers. moja^ lament' (-/from -cf-, compare:) must' lament ' (-s/-from -d'^sf); gr. 
|j09o(; m. ' discourse ', nuGsopai ' speak, think; consider'; Gothic maudjan, ga-maudjan' 
remind sb'; Lithuanian maudziu, mausti' long, want strongly ', apmaudas' displeasure, 
care '; Old Bulgarian mysib 'thought, notion' ( *mud-slio-)\ perhaps nir. smuainidh' thinks '. 
References: WP. II 255 f., Trautmann 171 f. 
Page(s): 743 

Root/ lemma: ma-r. Gen. ma-n-es, mQtos 

Meaning: hand 

Grammatical information: heteroklitischer r/n-siem 

Material: On the r- nominative are based: gr. piapn f. 'hand', supapnt; ' manageable ', 

Ijapic;, -£U)c; m. ' liquid measure, measurement of fluid quantities '; alb. /77a/r'take, receive, 

hold, catch' ( *marnd, />present as denominative formation from *mar- ' to get one's hands 

on somebody '). 

On *ma-n-Vne case oblique is based: Latin manus, -usi. 'hand, used for an oath ' (the
```


## [2026-09-07T17:39:07.546Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && grep -n \"moru\\|Ameise\" WLD_Bd2_pages.txt | head -20"
}
```


### [2026-09-07T17:39:07.596Z] TOOL RESULT

```
5305:piin „Eegenwolken‘’, sJcudru-pillis „Ameisenhaufe'', pilldl „sich vermehren,
18227:^miirbe*’^ nicht aus ^moru- umgestellt, s. Persson Beitr. 821 f. und u. *7nawro-);
20225:auch als eine Weiterbildung eines entlehnten moro- deutbar. Lat. morum
20233:bar; ist also etwa ein ^morum „Brombeere'' durch das entlehnte morum
20237:    Ob fur gr. fxogov arm. mor, lat. morum Beziehung zu mer- „flimmern“
20241:  Nicht iiberzeugend Pedersen KG. I 67 morum, jlioqvv aus idg. ^smdro-,
20247:cymr. mwyar pi. ds., acorn, moyr-hren „morus“, bret. mouar „mora'’ stehe.
20251:     (urspriinglichst "^^momro-, ^^memroA s. u.) „Ameise“.
20253:np. mor „Ameise“ (iiber arm. mrjimn, gen. mrjman und mrjian, gen.
20280:Krit. 29fiP., vgh auch ogjatyag javg/arji Hes.);' ai. vahmJca m. „Ameisen-
20287:folge vamrd- m., vamrT .,Ameise“.
20291:lichen Ameisennamen aufgesaugt habe; doch konnte leizteres umgekehrt
20294:„Ameise“      — auf einem dem anord. maurr entsprechenden Ameisennamen
45716:moruk          (s. dazu Pedersen KZ. 39, 351);    alb. mjekrs „Kinn, Bart“
```


## [2026-09-07T17:39:19.357Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && sed -n '20245,20300p' WLD_Bd2_pages.txt; echo \"--- page tag before\"; awk 'NR<=20260 && /\\[pdf page/ {l=$0; n=NR} END{}' WLD_Bd2_pages.txt; grep -n \"\\[pdf page\" WLD_Bd2_pages.txt | awk -F: '$1<20260' | tail -3"
}
```


### [2026-09-07T17:39:20.625Z] TOOL RESULT

```
woneben mit smi- (kelt. smii-) ir. smer, nir. smear „Brombeere'‘ (abere!),
cymr. mwyar pi. ds., acorn, moyr-hren „morus“, bret. mouar „mora'’ stehe.


mornO” (und fern, -a, -t), uormo-, mormo-, mouro- (germ, auch meuro-j
     (urspriinglichst "^^momro-, ^^memroA s. u.) „Ameise“.
  Auf morti- sind zuriickfuhrbar av. maoiri~s (konnte auch '"‘inoiiri- sein),
np. mor „Ameise“ (iiber arm. mrjimn, gen. mrjman und mrjian, gen.
mrjean s. Bugge KZ. 32, 18, Hubschmann Arm, Gr. I 476);
  air. moirh, cymr. myr^ morion PL, bret. mericn-enn', skr. mrdv, gen. pi.
mrawi, ksl. mravhji usw. (s. Berneker II 79, Trautmann Pestschrift f. Bezz.
16S; russ. muravej Umbildung von *morovej nach muravd „Rasen“. Auf
Kreuzung mit einem "^mtirh = aisl. maurr hat N. van Wijk, s. u., kein
Yertrauen); aber lit. marvd, mend „Brem8e“ (Zubaty AfslPh. 16, 400)
wegen der Bed. (trotz Berneker II 79) nicht hieher, sondern wohl nach
Persson Beitr. 822 naher zu marmalai „gro6e Bremsen^^, s. mormor-
„murmeln“.
   Auf morm-   :   lat.   fomlca   (vgl.   zum   lautlichen formido ; fjLoofico ;   s.   Yf.
LEWb.2 s. V. m. Lit.; f- nicht nach Holthausen KZ, 47, 311 nach/m/zr);
                                          mormor-, murmur*                               307

gr. fivQixoz (Lycophr.) ixvqiat]^, dor. juvQjud^ (Z;-Erw. zum a-Sfc.,           wie oQjulyMg
lat.   formica,       ai.   valml-Tca-    und ai. vamra-hd zum o-St., Hirt
                                         zum   7-St.,
IF. 31, 14; gegen J. Schmidts Krit. 30 Amiahrae von Suffixablaut a[e] %                   :



wendete sich schon Solmsen Beitr. 129).
   Auf vorm- gr. ^vQjudi, fogjuai Hes. (^- Schriftbehelf fur y, J. Schmidt
                  ;



Krit. 29fiP., vgh auch ogjatyag javg/arji Hes.);' ai. vahmJca m. „Ameisen-
                                           ’




haufen‘‘; daneben mit ganz alleinstehender (urspriinglichster ? s. u.) Laut-
folge vamrd- m., vamrT .,Ameise“.
   Auf mouro- aisl. maurr, norw. ^naiir (^-Epenthese nehmen kaum mit Recht
J. Schmidt Voc. II 132, Pedersen KZ. 39, 459, Berneker II 79 an; Bezzem
berger BB. 26, 188 stellt es zu lit. mauroti „wuhlen“ indem es einen ahn-
lichen Ameisennamen aufgesaugt habe; doch konnte leizteres umgekehrt
liber „kribbeln“            —
                      vgl. ndl. mieren „mit den Pingern wiihlen^, von niier
„Ameise“      — auf einem dem anord. maurr entsprechenden Ameisennamen
beruhen, was bei der geographischen Nachbarschaft trotz der berechtigten
Zuruckhaltung van Wijks, s. u., immerhin offen zu lassen ist. Aisl. maur
nicht nach Persson Beitr. zu aisl. meyrr „murbe“, woriiber s. mauro- „matt“).
Daneben "^meur- in dan. myre, schwed. myra {^metiridn--'), mndl. pi. mure
(einmal belegt) miere, nndl. mier,          mnd. mire (zum 1 s. van AVijk), mengl.
mire, myre (wohl scand.            Lw. nach Holthausen KZ. 47, 311, wo auch liber
--- page tag before
```


## [2026-09-07T17:39:38.595Z] TOOL CALL #34: Bash

```json
{
 "command": "ls site/pages/341.jpg 2>/dev/null; pdftoppm -f 341 -l 341 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg341 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/"
}
```


### [2026-09-07T17:39:40.339Z] TOOL RESULT

```
site/pages/341.jpg
total 17864
drwx------ 2 sfmqrb sfmqrb     4096 Sep  7 13:39 .
drwx------ 4 sfmqrb sfmqrb     4096 Sep  7 11:48 ..
-rw-rw-r-- 1 sfmqrb sfmqrb     8635 Sep  7 12:07 318-bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   101267 Sep  7 12:07 318-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    61586 Sep  7 12:18 320-bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   115970 Sep  7 12:18 320hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    86272 Sep  7 12:18 320-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    13284 Sep  7 12:18 320-zoom.png
-rw-rw-r-- 1 sfmqrb sfmqrb   107524 Sep  7 12:27 328-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    43713 Sep  7 12:35 331-bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   135301 Sep  7 12:35 331-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    52382 Sep  7 12:41 333-bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    88345 Sep  7 12:41 333-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    68568 Sep  7 12:43 335-bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   105946 Sep  7 12:43 335-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb      725 Sep  7 13:36 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    14937 Sep  7 11:56 arrows.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1413 Sep  7 12:27 box1b.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1385 Sep  7 12:27 box1.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1132 Sep  7 12:27 box2b.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1988 Sep  7 12:27 box2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    85949 Sep  7 11:57 bqt2002_a.png
-rw-rw-r-- 1 sfmqrb sfmqrb    72256 Sep  7 11:58 bqt2002_f1.png
-rw-rw-r-- 1 sfmqrb sfmqrb   161214 Sep  7 11:57 bqt2002_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    63319 Sep  7 12:40 build333.py
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
-rw-rw-r-- 1 sfmqrb sfmqrb    63978 Sep  7 12:35 mk330.py
-rw-rw-r-- 1 sfmqrb sfmqrb    64100 Sep  7 12:34 mk331.py
-rw-rw-r-- 1 sfmqrb sfmqrb    90456 Sep  7 12:42 mk332.py
-rw-rw-r-- 1 sfmqrb sfmqrb    99976 Sep  7 12:34 mk334.py
-rw-rw-r-- 1 sfmqrb sfmqrb    57252 Sep  7 12:38 mk337.py
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
-rw-rw-r-- 1 sfmqrb sfmqrb    65267 Sep  7 13:37 pg338.png
-rw-rw-r-- 1 sfmqrb sfmqrb    64116 Sep  7 13:39 pg341.png
-rw-rw-r-- 1 sfmqrb sfmqrb    64151 Sep  7 13:39 pg343.png
-rw-rw-r-- 1 sfmqrb sfmqrb    76794 Sep  7 13:39 pg346.png
-rw-rw-r-- 1 sfmqrb sfmqrb        0 Sep  7 13:36 queue.txt
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


## [2026-09-07T17:39:43.670Z] TOOL CALL #35: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg341.png"
}
```


### [2026-09-07T17:39:44.039Z] TOOL RESULT

```

```


## [2026-09-07T17:39:44.030Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-07T17:39:56.922Z] TOOL CALL #36: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:2049 --image 2>&1 | tail -40"
}
```


### [2026-09-07T17:40:04.300Z] TOOL RESULT

```
-۹ ۲ موود
مود ۰۱- بنم اول بروزن دود » بمعنی و اگر صدکس باشند فراخور صدکس آب پم
عقاب باشد و آن پردده‌است بز رکه و سیاه‌که | میرسد .
پراورا برتیر چبانند . مور چائه - با جیم فارسی » بر وزن
هار - با اول بنانی رسیده و برای بی | وممنی‌موربانه‌است. وآن زنگاری باشد که درآهن
نقطهٌ زده» معروف است که ازچملةٌ حشرات‌الارش | وفولاد بهم میرصد .
باشد ۴ ؛ ومورچه مسفرآست - وزنگاربرا لیز مورچه ۱ - مسنرموراست همچنانکه
کوبند که در جم‌آهن کا رکند و صیقل کردن | باغجه مسخرباغ -
برطرف بشود ۴ - وکنایه از حقیر و شمیف هم | و موربانه را نیز 4
هت. کوشند و آن
موراآمون - بامیم بروزن کوا کون زنگاری باشد (۱)
کزر و زردك صحرائی راکونند . که درتیغ وآیینه مورچه
۱ وفولاد وامثال آن‌افند - و کنایه از کی‌است که
مور چال ؟ - با جیم فارسی بر وزن فامت دمة : شر باه
بفایت ضعیف ولحیف و حفیر باشد .
کوشمال » کودالی را کوبند که بجهت کرفتن :۰
قلمه در اطراف آن‌کنند . مور چه پی ددت -کنابه از چیدن
۰ حاء. ه | رش باشد از بیخ - ۰
مودحان - « با جمم ابجد بر وزن ۰
دودمان؛ کوهی‌است درار اضی‌فاری وود آن غارست مورچةٌ عنبرین - کنایه از خط
که از آن بقدرآ نچه مردم درآ نجا وارد شوندآب خوبان و نوخطاست .
برمیاید بعنی اکر يكکس باشد بقدر يك کس مودد ۷ - بنم اولوسکون‌انیمجهول
)۱( خم۱: - باشد . ۰ ۱
۱ -رك : فرهنگه دساتیر ص ۲۹۹ ۰ ۴ - اوستا -3380171 ( مور ) » پهلوی
7۳ . کلمات ع (:) افغانی . بلوچی 1۳2۵7 ۰ 130711 (مور) » بودغا 131781081 ۰ قس :
ارمنی 17[1232 . 1050ژ8۵5 ۰ استی 8تازًا10 ۰ 8آزا323 (مور) «اسشق ۹۹۳ ر4: مورچه.
۴ - رك : مورچانه . مورچه . ۴ «مورچل * موریچال « انجمن‌آرا > در
جهانگشای نادری مورچل مکرر آمده « فرهنگه نظام > . 8 - دهی ازدهستا ن کوهمره
سرخی ۰ بخش مرکزی آشهرستان شیراز » ۹۹ کیلومتری جنوب باختر شیراز » سکنه ۳۰۰ تن
« فرهنگه جغرافیائی ارتش ج۷ ص ۰2۲۲۷ ‎٩‏ - از: مور (ه.م.) ۳ چه ( پوند تصفیر )
رك: اسشق ۹۹۳. پهلوی 73287626 « تاوادبا۰*۱۹ کلپایگانی 133500722 «قاسمی».خواناری
اس « سالنامه کلپایگان > ؛ نوعی از حشرات ناز4 بال که بطور اجتماع در زبرزمین‌زن دک ی کنند.
کار گران آنها عموماً بی‌بال ولی‌برها و ماده هاکه تندادشان کم است بال دارند .کار کران در زیر
زمی‌دالانهایی حفر و برروی آنها تیه‌ای ازخاشاك بنا میکنند . جمع مورچه » مورچگان آید :
مورچگان را چو بود اتقاق شیر ژدان را بدراند پوست . «دکلتان ۰۱۱۹
۷ - پهلوی 28071 « اونوالا ۵۰۰ >؛ مورد ۳ 1271148 آزتیرة موردیها 127۳120668
است وگل سفید آن ۵ کلب رکه و هکاسب رکه و تخمه‌اش سه پرچهٌ بهم چبیده دارد . بر کهای
آنها سبز دائمی و معطر است .» و میوه‌های آنرا «آسی دانه > کوبند « کل کلاب ۳۲ . رکه :
آی . آسار.
```


## [2026-09-07T17:40:15.818Z] TOOL CALL #37: Bash

```json
{
 "command": "timeout 300 python3 tools/ref_page.py BQT:2049 --image 2>&1 | head -15; ls -la data/verification/sources/refs/ocr/BQT/ | head"
}
```


### [2026-09-07T17:40:17.107Z] TOOL RESULT

```
(no exact page map; using offset -1917 -> pdf page 132; check the printed number and re-run with --pdf-page if off)
IMAGE: /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/2049.png
REF: BQT:2049  PDF: data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf page 132  OCR-lang: fas

-۹ ۲ موود
مود ۰۱- بنم اول بروزن دود » بمعنی و اگر صدکس باشند فراخور صدکس آب پم
عقاب باشد و آن پردده‌است بز رکه و سیاه‌که | میرسد .
پراورا برتیر چبانند . مور چائه - با جیم فارسی » بر وزن
هار - با اول بنانی رسیده و برای بی | وممنی‌موربانه‌است. وآن زنگاری باشد که درآهن
نقطهٌ زده» معروف است که ازچملةٌ حشرات‌الارش | وفولاد بهم میرصد .
باشد ۴ ؛ ومورچه مسفرآست - وزنگاربرا لیز مورچه ۱ - مسنرموراست همچنانکه
کوبند که در جم‌آهن کا رکند و صیقل کردن | باغجه مسخرباغ -
برطرف بشود ۴ - وکنایه از حقیر و شمیف هم | و موربانه را نیز 4
هت. کوشند و آن
موراآمون - بامیم بروزن کوا کون زنگاری باشد (۱)
total 53108
drwxrwxr-x  2 sfmqrb sfmqrb   12288 Sep  7 13:40 .
drwxrwxr-x 12 sfmqrb sfmqrb    4096 Sep  6 18:36 ..
-rw-rw-r--  1 sfmqrb sfmqrb  368375 Sep  4 13:39 0001.png
-rw-rw-r--  1 sfmqrb sfmqrb    1684 Sep  4 13:39 0001.txt
-rw-rw-r--  1 sfmqrb sfmqrb  534367 Sep  4 13:39 0049.png
-rw-rw-r--  1 sfmqrb sfmqrb    2677 Sep  4 13:39 0049.txt
-rw-rw-r--  1 sfmqrb sfmqrb    1076 Sep  4 15:27 103.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb  330101 Sep  6 17:59 1092.jpg
-rw-rw-r--  1 sfmqrb sfmqrb    2600 Sep  6 17:59 1092.vision.txt
```


## [2026-09-07T17:40:20.429Z] TOOL CALL #38: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/2049.png"
}
```


### [2026-09-07T17:40:21.121Z] TOOL RESULT

```

```


## [2026-09-07T17:40:21.118Z] INPUT

[Image: original 1650x2546, displayed at 1296x2000. Multiply coordinates by 1.27 to map to original image.]


## [2026-09-07T17:40:54.424Z] TOOL CALL #39: Bash

```json
{
 "command": "cat > data/verification/sources/refs/ocr/BQT/2049.vision.txt <<'EOF'\n[Borhan-e Qate', ed. Mo'in, p. 2049 — read from the page image (Persian print), 2026-09-07]\n\nHeadwords in the two columns: مود ۱ / مور / مورامون / مورچال ۴ / مورجان ۵ /\nمورجانه / مورچه ۶ / مورچه پی زدن / مورچهٔ عنبرین / مورد ۷\n\nمور - با اول بنانی رسیده و برای بی نقطه زده، معروف است که از جملهٔ حشرات‌الارض\nباشد ۲؛ و مورچه مصغر آست - و زنگار را نیز گویند که در جسم آهن کار کند و صیقل\nکردن برطرف نشود ۳ - و کنایه از حقیر و ضعیف هم هست.\n\nمورچه ۶ - مصغر مور است همچنانکه باغچه مصغر باغ - و موریانه را نیز گویند و آن\nزنگاری باشد (۱) که در تیغ و آیینه و فولاد و امثال آن افتد - و کنایه از کسی است که\nبنهایت ضعیف و نحیف و حقیر باشد.\n\nMo'in's etymological footnotes at the foot of the page:\n\n۲ - اوستا maoiri- ( مور )، پهلوی mōr، کلمات ع(؟) افغانی، بلوچی mōr، mōrîk (مور)،\nبودغا murghah، قس: ارمنی mrjimm، mrjium، استی māljig، muljug (مور) «اسـتق ۹۹۳»\nرك: مورچه.\n\n۶ - از: مور (ه.م.) + چه ( پسوند تصغیر ) رك: اسـتق ۹۹۳. پهلوی mōrcak «تاوادیا ۱۶۳»،\nکلپایگانی mārcūna «قاسمی». خوانساری ایضاً «سالنامهٔ کلپایگان»؛ نوعی از حشرات\nنازك‌بال که بطور اجتماع در زیرزمین زندگی می‌کنند. کارگران آنها عموماً بی‌بال ولی نرها و\nماده‌ها که تعدادشان کم است بال دارند... جمع مورچه، مورچگان آید:\nمورچگان را چو بود اتفاق / شیر ژیان را بدرانند پوست. «گلستان ۱۱۹»\n\n۷ - پهلوی mūrt «اونوالا ۵۰۰»؛ مورد = myrtus؛ از تیرهٔ موردیها myrtacées است...\nEOF\nwc -l data/verification/sources/refs/ocr/BQT/2049.vision.txt"
}
```


### [2026-09-07T17:40:54.478Z] TOOL RESULT

```
26 data/verification/sources/refs/ocr/BQT/2049.vision.txt
```


## [2026-09-07T17:40:56.278Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"pdf page\" SNS_pages.txt | head -5; echo \"---\"; python3 - <<'EOF'\nimport re\nt=open('SNS_pages.txt',encoding='utf-8',errors='replace').read()\n# find page tags\ntags=[(m.start(),m.group(0)) for m in re.finditer(r'\\[pdf page \\d+\\]',t)]\nprint(len(tags), tags[:5])\ni=t.find('mōr')\nprint('mor idx',i)\nEOF"
}
```


### [2026-09-07T17:40:57.644Z] TOOL RESULT

```
---
0 []
mor idx -1
```


## [2026-09-07T17:41:05.382Z] TOOL CALL #41: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'));print(json.dumps(d['SNS'],ensure_ascii=False,indent=1))\"; grep -rn \"مور\\|مورچه\" data/verification/sources/refs/SNS_pages.txt | head -5"
}
```


### [2026-09-07T17:41:06.777Z] TOOL RESULT

```
{
 "title": "Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1986",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/VajnameShayest",
 "lookup_hint": "grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php search (see BQT) for better hit-to-leaf mapping.",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS.txt"
 ],
 "page_offset": "242 leaves; page offset not determined (OCR too poor to read printed numbers) — locate by transliteration then read the page image",
 "covers_etymology": true,
 "notes": "OCR quality is POOR: Persian text mostly garbage, Latin transliterations partially readable. Verification will usually need the page image."
}
```


## [2026-09-07T17:41:13.506Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -iE \"\\bmor(ak|cak|čak|ic|ik)?\\b\" SNS_pages.txt | head -20; echo \"--- count lines\"; wc -l SNS_pages.txt SNS.txt; echo \"--- formfeeds\"; python3 -c \"\nt=open('SNS_pages.txt',encoding='utf-8',errors='replace').read(); print(t.count(chr(12)))\""
}
```


### [2026-09-07T17:41:14.764Z] TOOL RESULT

```
596:                                               WZKiM .         :     Wiener Zeitschrift fUr die Kunde des Mor-
10049:        ..       .,   *,   ^i^mor            than one place                   :
16016:ma£Sg 254/11                 MSdGgmah 253/1                     mOr 248/4                 nazuklh 259/6
--- count lines
  16583 SNS_pages.txt
  34173 SNS.txt
  50756 total
--- formfeeds
242
```


## [2026-09-07T17:41:22.953Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '15995,16030p' SNS_pages.txt; echo \"--- which leaf\"; python3 -c \"\nt=open('SNS_pages.txt',encoding='utf-8',errors='replace').read().split('\\n')\nimport sys\nn=0\nfor i,l in enumerate(t[:16030]):\n    n+=l.count(chr(12))\nprint('formfeeds before line 16016:',n)\""
}
```


### [2026-09-07T17:41:24.313Z] TOOL RESULT

```
nSvdiltar 291/17       niraudan 282/11                                O abaySd 15/16             padafrah 116/12
nSzag 286/12           niraQd SstSd 282/9                             Obastan 267/14             padixsa 115/17-116
nlrang 290/2           nisan 287/16                                   Obastan 267/18               201/6
nibaySd 199/21         nilast 276/4-310/4                             O bavSd 281/18             padixlayih 115/20
nibSsSra 164/8         nisast SstSd 310/7                             Obaxt 60/11                pSdrOz 116/16
nibfisura   164/5      nislnan 310/1                                  Obun 207/5-281/17          padyab 116/4
nibist 266/21          nislnSd 310/11                                 OftSd 62/8                 padyab dan 116/10
nigan 277/7            nislnisn 310/9                                 OgSn/an^On 82/9            padyablh 116/8
niganlh 277/11         nivSdSnisn (?) 285/5                           Chrraazd 59/14             pak 117/6-318/13
nigfln kirbag 277/10   niyabag 257/3                                  5hrraazd d3d59/19          pakan 117/10
niglrisn 278/5         niy3yisn 258/6                                 Shrmazd xV aday 59/17      paklh 117/14-318/]
niglrisn manag 278/7   niyaz 256/15-257/6                             -Oraand 74/13              paktar 117/12
niglrisntar 278/10     niySglSnd 291/10                               OmSd 74/17                 panag 118/5
niglrisnlg 278/12      niyOgsisn 291/9                                O nihisn 57/13             panaglh 117/8
niglrisnlgtar 278/14   niyOsldar 291/14                               OrOn 72/7                  panzdah 118/2-304,
nihad 57/5             niyOsIdartar 291/15                            OspOrlg 66/1               panzdah saiag 118;
nihadag 57/24-256/4    niz3r 271/11                                   Ostlganlha 66/15           p3nzdahum 304/16
25                                               Li;^Li*.L y>   ^At tfl**;'* ^-vr»
mahraanih 239/14             mazdist 241/17                     raiySnag 237/12           naxun 258/3
Mahraspand/Maraspand         raazdistan 241/20                  raizag 253/6              nSyrlg 264/19
  240/8                      raazg     243/18                   ra5g   248/1              nayrlg zan 264/24
ma£Sg 254/11                 MSdGgmah 253/1                     mOr 248/4                 nazuklh 259/6
man 221/1                    mShan 252/17                       ra&r   3sy3nag 248/8      namad 282/5
raang 248/2                  raSnisn 254/17                     raSrcag 248/10            naraak 282/7
man-iz 233/4                 raSniinlg 254/24                   mSristan 248/18           narab   282/2
raanuyscihr 240/20           mSniinlha 254/22                   raBy 249/22-24            nar 164/10
ma Bzan 39/21                raSnCg 255/1                       mOyfin 250/22             NarsSh Burzmihr 283
raar    244/23               mfinCgan 255/9                     mCylh 250/21              nasay/nasa 272/20
raard 308/2                  ra6nCg I     3b 255/7              mGzag 247/24              nas3y niganlh 273/5
mardan 308/12                raSnOglha 255/10                   murdag 248/11               277/12
mard b313y 308/6             raSs    253/14                     murdagan 248/15           nas3y x v ardan 273/7
Mard bGd 245/2               rafis   mfis(?)    253/13          raurdag pus 248/16        nask 274/8
raard I    ahrav 308/9       m§vag 254/14                       murv 248/20               naskdad 286/13
mard I druvand 308/11        m5xag(?) 252/2                     murvag 245/19-249/1       nasrOst 244/15
mardOm 68/19-245/4           raSzfid   253/7                    murvag-iz 249/2           nasus 274/16
mardOraan 69/3-245/7         raSzSnd 257/9                      raurvarlt 245/15          navad 33/11-182/4-3
--- which leaf
formfeeds before line 16016: 229
```


## [2026-09-07T17:41:30.807Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"mOr\\|mSrcag\\|mOrcag\" SNS_pages.txt | head -20"
}
```


### [2026-09-07T17:41:30.854Z] TOOL RESULT

```
16016:ma£Sg 254/11                 MSdGgmah 253/1                     mOr 248/4                 nazuklh 259/6
```


## [2026-09-07T17:42:06.647Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD && grep -n \"موییدن\\|مویید\\|مویه\" FFD_pages.txt | head -20; echo \"--- page tags\"; grep -n \"\\[pdf page\" FFD_pages.txt | head -3"
}
```


### [2026-09-07T17:42:06.730Z] TOOL RESULT

```
2092:موییدن
2093:«مویید» مادهٌ ماضی جعلی است. از مادهٌ مضارع ساخته شده است.
--- page tags
1:[pdf page 1]
24:[pdf page 2]
59:[pdf page 3]
```


## [2026-09-07T17:42:07.948Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=11395 && NR<=11415' IEC.txt | head -25; echo \"--- BRT tags\"; grep -n \"\\[pdf page\\|Sp\\.\" BRT.txt | head -3; sed -n '13395,13405p' BRT.txt"
}
```


### [2026-09-07T17:42:09.191Z] TOOL RESULT

```
muluos (mluos?) “dun, dark, brown’. WP II, 286 Gk. cf. molüno (soil, dirty”, if < *mulu-); Lat. mulleus ‘reddish’; EME cf. mollock, s. "dung: Li. mulvas ‘yellowish’; mulve, f. “mire”
mumioó, mumulió ‘mouth, munch, mumble (chew), mumble (mutter). Onomat. with vari- ants Lat. cf. *mumio, Ire (‘chew over, munch.
817
Fest.). (Misspelt or misread as a vbl. noun *munnitio. WH: LEW), Arm. cf. mncem ‘croon, wail’ beside Krt'- mn£éem, v. ‘grumble’; mněik, adj. *muffled, subdued' (fr. *mumtio-, etc.); OCS mümljo, mümati “stammer; blab- ber'. For type *mumulio cf. LG mummeln, v. ‘mumble, murmur’; Du. mommelen ‘mouth, munch’ beside mompelen, v. ‘mutter, mur- mur’; E to mumbie (‘to chew over and ‘to murmur); Sw. mumia, v. as LG; Slovene memljati, momljati & mumljati, inf. as LG; Blg. cf. mámólja, v. ‘munch’ & ‘murmur be- side mámrja, v. ‘murmur’; Sw. cf. also mumsa, v. ‘munch’
mundos, ios ‘mutilated, mute, dumb’ Arm. mung & munğ, gs mněo, mnčo, o-st. ‘dumb’; Gk. mundós, id.; Skt. mundah ‘bald; hornless; blunt'; Br. muñ, mons, moti, adj. ‘armless, legless, mutilated’
mundhros ‘bright, lively, gay’. Variant of type mudros (2), q.v. Go. cf. mundrei, f. ‘aim’; OHG muntar ‘brisk, wide-awake'; muntri, f., MHG, MLG munter, munder, id. (LW in Du. monter, Fris. & Norw. munter, fr. HG); OCS modrü (‘clever’, and com. S1); (SI. DW in Rum. mândru, mindru, adj. *proud"); Li. (Zemaite) mundras ('bright, lively’. Lalis); Latv. (LW, fx. Li.) mundrs, id. beside (alleged) modrs, id.
münió (mün-) Gk. cf. a-múnd “protect, fend off; Ir. máinim, v. “teach; show; advise; MHG münen, wv ‘protect’. (Lat. münio, ire is apparently fr. a type moenio, ultimately *moghnio? See mogh- and cpds.)
măr- (murouis, muràuis, muruis, ios, meur, mour-) (1) ‘swarm; ant Cf. WP II, 306 & 312. Variants as follow: Per. mür, dim: mürce "ant: (*-eu- or *-ou- in) Av. maoiris, m. id.; Arm. mrÉiwn & mrěimn, gs mr&man, id.; Kurd. mérü ‘insect; Beluchi müri,id.; Hind. mor (fr. Per.) id.; cf. Per. mū- riàne ‘white ant; Oss. Dig. cf. muldzug Cant, dim. type); Gk. cf. mürmos, m., mür-mex, gs -m&kos, m. id. beside müríos, adj. (Ccount- less’, lit. ‘swarming’, cf. Fr. fourmillant); MIr. múr "large number beside moirb, f. ‘ant; OW cf. mor-grug (Cant-hil hence “ants'); W
mundos, ios — murguos
20
25
30
35
40
45
818
myr, myrion, morion, pl. ‘ants’; Br. mérion, mérien, id.; EME mire ant beside piss-mire, id.; Sw. myra, f. (1) “ant; Icel. mor, n. (1) ‘swarm’; OCS mravij, f. ant Srb. mráv, gp mravi, id., R muravéj, muràš, m. id.; Big. mràva, f. id. Variants w. vocalism *-eu-/-ou- in Du. mier, f. id. beside ON maurr, m. id. and (ambig.) Av. maoiris, m. id., and of type *moru- in Olr. & Ir. moirb: Li. marva ‘gadfly’. (For the semantics, cf. Blg. mravulja, v. *swarm')
mür- (2) “dust, fly-ash’ Ir. múr, m. ‘ash, dust; Icel. mor, n. ‘dust, pother
mür- (2) *mire, bog Olr. (queried) múr, m. ‘clay; ON myrr, pl. mýrar, s. “bog'; Nor. myr, id.; Sw. myra, pl. -Or, f. id.; Li. cf. mürinas, adj. ‘dirty’; mürü, mur, v. ‘get sodden’; SG Mure, f. mudslope'. Cf. muronio (?)
mür- (4) (a plant) Skt. mura, f. (a fragrant plant); Ir. mür, m. (2) ‘red seaweed’; ON mura, f. 'silverweed' Or *goosegrass
mur- (5) ‘murmur, grunt. Cf. murmuró G murren ‘murmur; rumble — as thunder’; ON murra, v. id. beside morra, v. ‘doze, idle’; Du. morren, v. ‘murmur’; Sw. morra, v. id.; Li. muroju, -oti ‘low, bellow’
--- BRT tags
38:Sp.  W.-B.  AirWb.
153:(Sp.  Ca  und  Cb),  sowie  da  und  db  (Sp.  Ea  und  Eb)  völlig  gleichlautend;  nur  die
2036:Die  Gaitas  und  den  —  etwas  jüngeren  —  Yasna  Hapiatthäfay  (s.  Sp.  1271) fasse  ich  unter  dem  Namen  gääisch-awestisch  (gAw.,  g.)  zusammen,  alle  übrigen Stücke  bezeichne  ich  als  jungawestisch  (jAw.,  j.).
•  j.  ^dänav-  £  ' (Getreide) koro'.
KompE.  —  zEl.  s.  unter  dänd^karS-.
•  j,  dänazväza-  m.  andrer  Name  für  den abpr»t-{sA.y.  . .  paoiryd ..  kSvarttlit3m{&Ai)  ., astayeiti  .  .  tüirlm  'stm  N.  82.
Wahrscheinlich  verderbtes  Wort;  T  hitVJjuiB.
—  Pü.!  pa röi viÜnilSrih'}  "für das  Amt  dessen, der  den  Fluss  (aus  dem  das  Wasser  geholt werden  soll)  aassucht";  erl.;  pa  äiariiA.  — >l  Nach  DsT.  ZA.  3.  133,   Blocket  Lex,  88
mehr  .
ules
•  j.  (0n5.kars-Adj.'(Getreide)kömer(ver)- schleppend',  Bezeichnung  einer  Ameisen- art*': maoirJm  °spm  Y.iö.ia; — maoirinam ■!„nqm  V.J4.S.  'i«  73-
*)  Die  Zoologen  des  Awesta  haben  offenbar die  Puppen,  die  die  Ameisen  in  die  Sonne  tragen, für  geraubte  Getreidekürner  angesehen.
Komp.:  'däiiä'f.  'Getreldekom';  ai.  ./4ono- f., mp.  a'iin,  np.fl'JHo;  H-Vari-Adj.  (aus  ir. '.iz-i-, IF.  5.  261),  zum  \.'tatl-;  mp.,  np.  'iü;  vgl. yäri.iarJi:  —  mp.  (Pü.)  däa  kii,  np.  dinaiis.
•  j.  dänu.drä]ah-  Adj.  'von  der  Länge
```


## [2026-09-07T17:42:22.778Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=19950 && NR<=20090' BRT.txt | grep -nE \"^[0-9]{3,4}$|11[0-9][0-9]\" | head -10; echo \"---\"; sed -n '20060,20080p' BRT.txt"
}
```


### [2026-09-07T17:42:24.024Z] TOOL RESULT

```
63:s.  Wh.  Gr.»  S  1197  c.
74:'martiya-  1148
93:1150
114:1152
---
"5>
marotä-
mar»z-
1152
•  j.  man^-  £  -  ?  -,  eine  Landplage Margianes:  mSurum  . .  aat  ahe  paüySrim ß-ak^rmlat  atars  mainyuf..  °ham/a  vl%u- iqmea  V.  i.  5.
*Pä.!  5mil  (HORN  BB,  //.  36s)'J,  erl.:  ahm/') I  ayäaiSrin  an  yäi  kitnind.  S.  dazn  die  GrB.- Stelle  bei  Dst.  ZA.  2.  8.  —  ')  amar;  ich halte  die  obige  Lesung  nicht  für  sicher;  GrB. hat  am  n  ar.
•  p.  marduniya-  m.  EN.  eines  Persers, Mardonius:  *gaubrtan^  nämt^  °yahyä pu%'^J'  parst^  Bh.4. 18.
VIL  AbleiL  aus  "marduna-  m.  •Winier';  Yg'- np.  mul  'Wein',  ai.  m^dvikä-  f.  'Weintlock' 0. —  •)  Doch  ».  auch  ZDMG.  54.  35g,
•  j.  maraSra-  n,  'Merken,  Imgedächtnis- behalten*:  'rtmca  vam,Tmca  dmnaya  vaa- kuy&  Y.  22. 3.        DS.  'räi  als  Inf.  sbcs.
Zum  V.  *niar-.  —  Pü. :  BsmutihüA,  Sü. :  adhya-
•  j.  maradrü  Inf.  'im  Gedächtnis  zu  be- halten'; IUI  ahurahe  mazdä  dan%räi  (sd.) . .  xratam  .  .  m*  .  .  Aisvqm  , .  fraväkäi mahrake  sp?niahe  Yt  i.  aS,
Zum  V.  »«ar-.  —  Vgl.  mar>%ra:  —  Pü. *eimurilii  räi.
•  j.  mairya-  Adj.  (fem.  ya-)  'betrügerisch, tückisch,  schurkisch;  Schurke':  *ahalcti ♦»/•«'>  (NSf.)  nas'atagca  'ys  "und  es  wird  zu Grunde  gehen  die  Schurkin  und  verder- ben wird  der  Schurke"  Yt/p.ia;  4.Z; —  armatsis  deihrubya  avästryaia  (sd.) -ys  Yt/.  29;  —  tmnniaite  vJspqm  daiti- haom  'yS  mihrSjruxl  YLJ0.3;  —  °yS drvi  bizangrs  V.  5,  35;  —  sii^rqm yqm  karafnqmüa  'yanqmla  bieangn aimcur/anqmca  Y,  <>.  18;  —  *JanyS. 'yayh  Y.  JO.  15;  —  mä  hl 'y3  giurvayHt ma  /akika  Yt.<?.59;  —  nSU  *'yehe'''  ttSij jakikayä  t.io;  —  'yS  tBiryS  franrase  Yt. J.41,  J5-S6.  82;  8»,  77.5-5°;  —  'r^^ tairim/raarasyanam  YL5. 18,  zz,  ip.  77, Y. //.  7;  —  °yeke  tyaonaAe  ar»jal.aspahe Yt.  5.  30 ;  —  tafsatca  AS  °yB  (näml.  aiis srvarü)  Y.p.  11;  —  "«(NSC)  .  .  bSsyqsta FrW, /0.4a;  —  Sai  mqm  °yS  äkasat  atsrö mainyui"V.22.a;  2.  '  a)  ASn.  'rfm  ' Adv. 'trügerischer Weise.betrüglich':  a/trqm *rTm  küsayeiti  (sd.)  anaiwySstS  dalnqm "betrüglich  handhabt  die  Strafgeissel,  wer nicht  . ."  V.  18.  41'.  \az»M  maire  Yt /.  ag:  lies  zamara^
Vgl.  mp.  mar,  air.  mtUaim  Ich  betrüge',  liL n/fo/ 'Lüge',  arm.  n^/ 'Sünde';  LitLbeiHBU. AGr.  f.  473.     Falich  GlrPh.  2.  531). —  Pü.:
vua;  {zaY.ro): marämt;  S&. :  n^iamtah,  erL: nüj'ifa^i  Npü.:  räixoH  'Sttaasenränber'.  S. noch  No.  2.  —  >)  NA.  mart.  Lesung  un- sicher.—  ■)  Hds.  maraie.  Vi.:  mär;  s.  aber Yt  S.  59.  —  })  Dst.  'il  manie  un  Ashira mairya  irrf  golier',  womit  zuvor  *ainim  überaetzt wurde.  Aber  ainim  (sd.)  fehlt  hier,  musa  alio dem  Sinn  nach  ungefähr  durch  mairim ,  das D.  stillschweigend  Icoirigirt,  ersetzt  sein.  S. jetzt  auch  Gdn.  SPreussAW.  zg.  423.  zFü.  t. unter  käiaya-.    —  4)  S.  dazu  Bthl.  LG&RFh.
j.  maurvay-  m.'>  'Ameise',  ein  daemscbes Tier,  von  dem  zwei  Arten  geschieden werden:  xrafstnm  ava.Janalta  moffifftn danHjtarsim  (sd.)  V.  16.  la;  —  hagvan maoirinam  danS.iarsanqm  ava.Janyat  V. 14.S1  ^o-73i  —  baiiian  maoirinqm  arai- kanqm  (sd.)  kutakanqm  duiaininqm  ava.- /anyai\:i4.$.
Aus  ar.  'marg'  oder  ^margg' ;  zSchr.  ni*w* s.  S  ^6S.  44.  —  mp.  (Pü.),  np.  mär ').  Weiteres bei  Hbm.  AGr.  /.  476,  IFAnz.  10.  23;  dara noch  Wn.  AiGr.  /.  277.  —  >)  Gegen  den  An- sati  eines  fem.  "vt-  sprechen  die  Epitheta.— ')  VgL  mp.  ier  unter  baoiryo:
•  j.  maraz-  V.  'streifend  berühren'.  Praes. 2  marsza-,  3  mfrpza-,  8  m^qz-''>.  —  Int m^rqidyäi.  [S,  noch  zu  mfr>^yumna-^
1)  'streifend  berühren,  streifen';  mürpm .  .yS  .  .  aiwyaiti  .  .  mar»zaiti  <^a  karatia ai^Aä    z>md    Yt  10.  95.  2)    'im  Flug
streifen':  värrfnahe..y5  vasaiie,.barjmavö marizat  gairinam  Jqfnavd  marpxai  numam Yt.i4~i9-'i;'2i'.
mit  aipi  '(ein  Tor,  Akt.)  anbrmgea  an  -' (Akk.):  apica  hm  vanm  mar»sa  dvanm (sd.)  raolamm  V.  2. 30;  38  (wo  manxat).
```


## [2026-09-07T17:42:35.830Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=4600 && NR<=4700' BRT.txt | grep -nE \"^[0-9]{2,4}$\" | tail -5; echo \"--- HUB\"; grep -n \"Ameise\\|mör\\|mōr\\|möye\\|müye\" HUB.txt | head -20"
}
```


### [2026-09-07T17:42:37.039Z] TOOL RESULT

```
47:137
50:138
68:135
71:136
--- HUB
125:*rig geworden ware. Aw. ara^ka, Beiwort der Ameise,
```


## [2026-09-07T17:42:43.895Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '110,140p' HUB.txt; echo \"=== HRN Ameise\"; grep -n \"Ameise\" HRN.txt | head"
}
```


### [2026-09-07T17:42:43.963Z] TOOL RESULT

```
14. Kurzes a im Aniaut hatte abfallen miissen, also wird
dran u. s. w. die Vichtigere' Form sein, vgl. die kas.
Dialectformen orinj u. s. w.
16. Ich wiirde np. art fiir contrahirt aus aoari (vgl. arad
aus avarad *bringt* halten), wenn das Wort nicht are
lautete, wie mir No Id eke aus Reimen (mit bar-e, mar-e
etc.) nachweist, vgl. kas. orE^ are,
Ueber das Vorkommen von np. avar certitudo',
avan 'flde dignus' vgl. Mann, ZDM6. 47, 701. Ist fur
phi. paz. evar 'certain , evarth 'certainty', evarik certain
(Shk. p. 243 etc.) avar u. s. w. zu lesen? An e = adhi
(das weder im Zd. noch im Ap. vorkommt) glaube ich
nicht.
17. Ist unsicher, da im Ap. ebensogut arika *feindlich* (zu
skr. ari' Teind*) gelesen werden kann, das im Np. zu
*rig geworden ware. Aw. ara^ka, Beiwort der Ameise,
ist dunkel. Die Form rey belegt Vullers aus Firdusi.
20. Fiige hinzu: np. dzard-a = zd. azareta- *beleidigt\
Sal. Shuk. geben freilich azurdan *kranken fiir
Vullers' Ozardan. Dazu stimmt afgh. LW. azurda
afflicted, sad*.
24. Zd. dstdrayettti ist mit Darmesteter, Le Zend-
Avesta II, p. 66, Anm. 7 durch *sundig, schuldig machen'
zu ubersetzen und als Denom. von *a8tara- = parsi
astar *Sunde' zu fassen; es geh5rt zu zd. anastareta--
ohne Schuld, ohne Siinde'. Ap. ma starava wird von
*) ^gl- jfid. tat. ovxur *Krippe* (Miller p. 75; «u qv 'Wasser'
= np. CUb.PERSISCHE STUDIEN
VOK
m HtBSCHMANN.
STRASSBURG.
=== HRN Ameise
8626:993. mör 'Ameise', mürce-),
8627:g. möirik 'schwarze Ameise'; Käs. V. möröund,
8628:aw. maoiri- 'Ameise'; phlv. mör.
8630:belegt); afy. bei. (248) mör, n. möHk "Ameise*, vergl.
8640:nniljvg, t. mäljig 'Ameise' ein.
```


## [2026-09-07T17:42:56.352Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '8620,8650p' HRN.txt"
}
```


### [2026-09-07T17:42:56.399Z] TOOL RESULT

```
(Schrader, Sprachvergl. und Urgesch.- 206 folg., 252)?
992. meniS, menisn (Wörterbücher) 'Sinn, Charakter,
vergl. dus[men, rr^^DirilD (Is. 12, 1).
ap. vergl. 'Jlpiaj/LisvTjg (Plutarch); aw. manah-^ dm-
manah-; phlv. dusman, vergl. men(i)sn; ai. rndnas-,
skr. durmanas.
993. mör 'Ameise', mürce-),
g. möirik 'schwarze Ameise'; Käs. V. möröund,
aw. maoiri- 'Ameise'; phlv. mör.
LW. (?) kurd. mürt^ merü (vergl. np. mtrük, nicht
belegt); afy. bei. (248) mör, n. möHk "Ameise*, vergl.
auch mörag 'Korn an der Flinte' (?); echt yidg. mur-
yäh (BB. Vn, 198).
^) Genaue Angaben über die verschiedenen gebräuchlichen Mens
findet man bei F. Stolze und F. C. Andreas, Die Handelsverhältnisse
Persiens (Petermann^s Mitteilungen, Ergänzungsheft Ko. 77), S. 83.
*) Keimt auf hör fäähn. I, 508 Vers 135), vergl. auch das reimende
hemcü mör bezör.~ 223 —
Eine Sonderstellung nimmt im Iranischen — vergl.
auch arm. mrjimn, mrjiun (H. No. 207) — oss. d.
nniljvg, t. mäljig 'Ameise' ein.
994. tnöze 'Schuh', arab. LW. manzaj.
aw. [/^maoc^ mit paiti 'anziehen (sc. Schuhe)*, vergl.
framv/ti' *das Ausziehen (der Schuhe)'; phlv. tnööak
(Men. ; arm. LW. muöak), vergl. mök (chald. LW.
NpID), auch patmö/tan 'anziehen'; ai. [/^möö- mit ä,
prati anziehen (irgend ein Kleidungsstück)*, mit upa
*Schuhe anziehen*.
LW. afy. möza ; bei. müzag, n. mözay 'Socken, Stiefel,
Beinkleider* (174).
995. ninS *Maus*.
```


## [2026-09-07T17:43:03.979Z] TOOL CALL #51: Bash

```json
{
 "command": "sed -n '1,40p' tools/fetch_source.py"
}
```


### [2026-09-07T17:43:04.022Z] TOOL RESULT

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


## [2026-09-07T17:43:09.954Z] TOOL CALL #52: Bash

```json
{
 "command": "for u in \"https://en.wiktionary.org/wiki/%D9%85%D9%88%D8%B1\" \"https://en.wiktionary.org/wiki/formica#Latin\" \"https://www.etymonline.com/word/formic\" \"https://www.etymonline.com/word/chloroform\" \"https://en.wiktionary.org/wiki/%D9%85%D9%88%DB%8C%DB%8C%D8%AF%D9%86\" \"https://en.wiktionary.org/wiki/%D9%85%D9%88%D8%B1%DB%8C%D8%A7%D9%86%D9%87\"; do echo \"=== $u\"; timeout 120 python3 tools/fetch_source.py \"$u\" --note \"page 341, roots Morwi and Moudh: ant words and mourn words\" 2>&1 | tail -2; done"
}
```


### [2026-09-07T17:43:17.584Z] TOOL RESULT

```
=== https://en.wiktionary.org/wiki/%D9%85%D9%88%D8%B1
/home/sfmqrb/git/rishe/data/verification/sources/web/8fe312771154d4de.txt
=== https://en.wiktionary.org/wiki/formica#Latin
/home/sfmqrb/git/rishe/data/verification/sources/web/e7a012c50d4f6a7d.txt
=== https://www.etymonline.com/word/formic
/home/sfmqrb/git/rishe/data/verification/sources/web/fd37bc0ac14df983.txt
=== https://www.etymonline.com/word/chloroform
/home/sfmqrb/git/rishe/data/verification/sources/web/67fbca4574c9a486.txt
=== https://en.wiktionary.org/wiki/%D9%85%D9%88%DB%8C%DB%8C%D8%AF%D9%86
/home/sfmqrb/git/rishe/data/verification/sources/web/6fd17ebed02a0318.txt
=== https://en.wiktionary.org/wiki/%D9%85%D9%88%D8%B1%DB%8C%D8%A7%D9%86%D9%87
/home/sfmqrb/git/rishe/data/verification/sources/web/ed22ec7c3bf6532e.txt
```


## [2026-09-07T17:43:21.307Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"##### mur\"; grep -n -A30 \"Persian\" 8fe312771154d4de.txt | grep -i -m40 \"etymolog\\|Middle Persian\\|Proto-Iranian\\|maoiri\\|ant\\b\\|mūr\" | head -30"
}
```


### [2026-09-07T17:43:21.361Z] TOOL RESULT

```
##### mur
150- Etymology 
164- Etymology 
428- Eren, Hasan ( 1999 ), “ mor ”, in Türk Dilinin Etimolojik Sözlüğü [ Etymological Dictionary of the Turkish Language ]‎ [2] (in Turkish), Ankara: Bizim Büro Basım Evi, pages 296–297 
430- Levitskaja, L. S. ; Blagova, G. F. ; Dybo, A. V. ; Nasilov, D. M.; Pocelujevskij, Je. A. ( 2003 ), Etimologičeskij slovarʹ tjurkskix jazykov [ Etymological Dictionary of Turkic Languages ] (in Russian), volume 7, Moscow: Vostočnaja literatura, pages 80–81 
432- Räsänen, Martti ( 1969 ), Versuch eines etymologischen Wörterbuchs der Türksprachen (in German), Helsinki: Suomalais-ugrilainen seura, page 3440b 
436- Stachowski, Marek ( 2019 ), “ mor ”, in Kurzgefaßtes etymologisches Wörterbuch der türkischen Sprache (in German), Kraków: Księgarnia Akademicka, →DOI , page 257b 
446- Etymology
449- From Proto-Pathan *mor < *mā́dr , from an ancestral Middle Iranian form *mā́dər , [ 1 ] from Proto-Iranian *máHtā , from Proto-Indo-Iranian *máHtā , from Proto-Indo-European *méh₂tēr .
498- Etymology
501: From Middle Persian [script needed] ( mwl /⁠mōr⁠/ ) , from Proto-Indo-Iranian *marwíš ( “ ant ” ) .
723: Persian terms derived from Middle Persian 
724: Persian terms inherited from Middle Persian 
758- Urdu masculine consonant-stem nouns 
773: Requests for native script for Middle Persian terms 
774- Urdu terms with redundant transliterations 
775- Brahui terms with non-redundant manual transliterations
```


## [2026-09-07T17:43:27.222Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"##### muriane\"; grep -n -i -m10 \"Etymology\\|termite\\|مور\" ed22ec7c3bf6532e.txt | head -20; echo; sed -n \"$(grep -n -m1 'Etymology' ed22ec7c3bf6532e.txt | cut -d: -f1),+12p\" ed22ec7c3bf6532e.txt; echo \"##### muyidan\"; sed -n \"$(grep -n -m1 'Etymology' 6fd17ebed02a0318.txt | cut -d: -f1),+14p\" 6fd17ebed02a0318.txt"
}
```


### [2026-09-07T17:43:28.455Z] TOOL RESULT

```
Exit code 1
##### muriane
4:TITLE: موریانه - Wiktionary, the free dictionary
6:موریانه - Wiktionary, the free dictionary 
65: Etymology 
75: موریانه 
141: مورانه ( murâne ) , مورجانه ( murjâne ) , مورچانه ( murčane ) 
143: Etymology
146: Derived from the word مور ( mur , “ ant ” ) , from Proto-Indo-Iranian *marwíš .
151: موریانه • ( muryâne ) ( plural موریانه‌ها ) 
153: termite 
154: Synonyms: مورچه‌ی سفید ( murče-ye sefid ) , ریونجه ( rivanje ) , ترده ( tarde ) 

 Etymology 

 1.3 
 Noun 

 1.4 
 References 

 Toggle the table of contents 

 موریانه 

 3 languages 
##### muyidan
sed: -e expression #1, char 1: unknown command: `,'
```


## [2026-09-07T17:43:33.050Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && head -30 6fd17ebed02a0318.txt; echo \"#### formica\"; sed -n \"$(grep -n -m1 'Etymology' e7a012c50d4f6a7d.txt | cut -d: -f1),+20p\" e7a012c50d4f6a7d.txt"
}
```


### [2026-09-07T17:43:34.297Z] TOOL RESULT

```
URL: https://en.wiktionary.org/wiki/%D9%85%D9%88%DB%8C%DB%8C%D8%AF%D9%86
FETCHED: 2026-09-07T17:43:16Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 404: Not Found#### formica
 Etymology 

 1.2 
 Pronunciation 

 1.3 
 Noun 

 1.3.1 
 Synonyms 

 1.3.2 
 Hyponyms 

 1.4 
 Anagrams 

 2 
 French 

 Toggle French subsection
```


## [2026-09-07T17:43:39.181Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && grep -n -i \"dissimil\\|Proto-Italic\\|morm\\|Proto-Indo-European\" e7a012c50d4f6a7d.txt | head -10; echo \"#### formic\"; grep -n -i \"formic\\|1791\\|ant\" fd37bc0ac14df983.txt | head -12; echo \"#### chloroform\"; grep -n -i \"chloroform\\|1838\\|Dumas\\|formyl\" 67fbca4574c9a486.txt | head -12"
}
```


### [2026-09-07T17:43:39.248Z] TOOL RESULT

```
352: From Latin formīca , ultimately from Proto-Indo-European *morwi . Cognates include Ancient Greek μύρμηξ ( múrmēx ) .
471: Traditionally, from a form with earlier initial /m/ , such as Proto-Italic *mormīkā , considered to derive from Proto-Indo-European *morwi(s) ( “ ant ” ) , a term with many deviating forms – probably taboo distortions – in various Indo-European languages. The irregular sound change can be explained by dissimilation of /m…m/ to /f…m/ . [ 1 ] 
473: Cognates would include Sanskrit वम्र ( vamra ) , Ancient Greek μύρμηξ ( múrmēx ) , Old Church Slavonic мравии ( mravii ) , Polish mrówka , Old Irish moirb , Welsh myrion , Old Norse maurr , English mire . Compare especially Sanskrit वल्मीक ( valmī́ka , “ anthill ” ) and Iron Ossetian мӕлдзыг ( mælʒyg , “ ant ” ) , which could point to Proto-Indo-European *morm-iH-ko- .
669: Italian terms derived from Proto-Indo-European 
685: Latin terms derived from the Proto-Indo-European word *morwís 
686: Latin terms derived from Proto-Italic 
687: Latin terms inherited from Proto-Italic 
688: Latin terms derived from Proto-Indo-European 
#### formic
1:URL: https://www.etymonline.com/word/formic
4:TITLE: Formic - Etymology, Origin & Meaning
6:Formic - Etymology, Origin & Meaning 
19: Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.
21: Origin and history of formic 
23: formic (adj.) 
25: 1791 (in formic acid ), literally "from ants," coined from Latin formica "ant" (see Formica (n.2)). The acid first was obtained in a fairly pure form in 1749 by German chemist Andreas Sigismund Marggraf (1709-1782), who prepared it by distilling red ants. It also is found in nettles and bee stings.
26: also from 1791 
28: Entries linking to formic 
30: Formica (1) 
32: proprietary name (1922) of a product manufactured originally by Formica Insulation Co. of Cincinnati, Ohio, U.S. (founded 1913). According to the company, the material (originally marketed as an industrial insulator) was so called because it could be used for mica , i.e., in place of mica , a more expensive natural insulator. Primarily used in consumer goods since c. 1945.
36: "trichloromethane," a volatile, colorless liquid used as an anaesthetic, 1835, from French chloroforme , a hybrid coined 1834 by French chemist Jean-Baptiste Dumas (1800-1884) from chloro- , a combining form meaning "chlorine" (see chlorine ), + formique "formic (acid)" (see formic (adj.)).
#### chloroform
1:URL: https://www.etymonline.com/word/chloroform
4:TITLE: Chloroform - Etymology, Origin & Meaning
6:Chloroform - Etymology, Origin & Meaning 
21: Origin and history of chloroform 
23: chloroform (n.) 
25: "trichloromethane," a volatile, colorless liquid used as an anaesthetic, 1835, from French chloroforme , a hybrid coined 1834 by French chemist Jean-Baptiste Dumas (1800-1884) from chloro- , a combining form meaning "chlorine" (see chlorine ), + formique "formic (acid)" (see formic (adj.)).
27: As a verb, "to subject to the influence of chloroform," from 1848, which is the year its anaesthetic properties were discovered. Related: Chloroformed .
30: Entries linking to chloroform 
44: It might form all or part of: arsenic ; Chloe ; chloral ; chloride ; chlorinate ; chlorine ; chloro- ; chloroform ; chlorophyll ; chloroplast ; cholecyst ; choler ; cholera ; choleric ; cholesterol ; cholinergic ; Cloris ; gall (n.1) "bile, liver secretion;" gild ; glad ; glance ; glare ; glass ; glaze ; glazier ; gleam ; glee ; glib ; glide ; glimmer ; glimpse ; glint ; glissade ; glisten ; glister ; glitch ; glitter ; glitzy ; gloaming ; gloat ; gloss (n.1) "glistening smoothness, luster;" glow ; glower ; gold ; guilder ; jaundice ; melancholic ; melancholy ; yellow ; zloty .
92: Share chloroform 
96: https://www.etymonline.com/word/chloroform Copy 
99: <a href="https://www.etymonline.com/word/chloroform">Etymology of chloroform by etymonline</a> Copy
```


## [2026-09-07T17:43:50.311Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for w in موییدن مویه مستمند کلروفرم; do echo \"=== $w\"; grep -c \"$w\" MON_part1.txt MON_part2.txt 2>/dev/null; done"
}
```


### [2026-09-07T17:43:51.485Z] TOOL RESULT

```
=== موییدن
MON_part1.txt:0
MON_part2.txt:0
=== مویه
MON_part1.txt:5
MON_part2.txt:9
=== مستمند
MON_part1.txt:3
MON_part2.txt:3
=== کلروفرم
MON_part1.txt:1
MON_part2.txt:5
```


## [2026-09-07T17:43:54.881Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"کلروفرم\" MON_part2.txt | head -6; echo \"=== مویه\"; grep -n \"مویه\" MON_part2.txt | head -10"
}
```


### [2026-09-07T17:43:54.948Z] TOOL RESULT

```
16744:کلروفرم یا در بتزین حل می‌کنند و چون 
25084:کلروفرم: (-0۳۳9۸)۲6]-۱۵۱۵۲۵ (۱.) (یز. شننم. ) 
58763:است و در اتر و کلروفرم و اسانس تربانتین و 
84052:محلولند ولی در الکل و کلروفرم و اتر و 
93802:کلروفرم وارد بدن شوند. ۴ -يرقان عفونی - 
=== مویه
8559:فلفلمویه: (۵-)۱6۱]۵1۴0۲۷۵ (۱.) (گیا.) 
8575:فلفل مونیه: درخت فلفل مویه» فلفل مور 
8577:پلپلمونیه. ضح.- برخی از کتب فلفلمویه را 
8579:کبابه گیاه دیگی غیر از فلفلمویه است. 
26982:کندامویه: ()«۳« (امر.) مویی که 
68887:مویه: (7۱۷۸)()06۰ (امسص.) کر به و 
68890:نواخته می‌شود. مویه زال: (مس.) لحنی است 
68892:مویه گر: ۱-۲ (ص‌فا.) زاری کننده؛ نو حه 
73139:نامویه: (۵۷۸()۵) ۱۱1-011۷۵ (رص. ۱.) نام
```


## [2026-09-07T17:44:01.830Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '68885,68895p' MON_part2.txt; echo \"=== formik\"; grep -n \"فرمیک\" MON_part1.txt MON_part2.txt | head -5; echo \"=== must\"; grep -n \"^مست:\\|مست:\" MON_part2.txt | head -8; grep -n \"مستمند\" MON_part2.txt | head -5"
}
```


### [2026-09-07T17:44:01.949Z] TOOL RESULT

```
ضح.- در انجا مراد « کشمش» نیست زیرا 
کشمش عصاره (خون) ندارد. 
مویه: (7۱۷۸)()06۰ (امسص.) کر به و 
زاری» نوحه. (.) (مد.) گوشه‌ای است در 
دستگاه سه گاه که شدرت در چها رگاه شم 
نواخته می‌شود. مویه زال: (مس.) لحنی است 
دی قدیم. 
مویه گر: ۱-۲ (ص‌فا.) زاری کننده؛ نو حه 
کننل د. 
مو پیدد: ۶-۵ [قس. موبه ] (مص‌ل.) 
گریه و زاری کردن. نوحه کردن؛ شیون 
=== formik
=== must
41074:لول: انا (ص.) ست مست: سخت مست؛ 
55662:مست: ۱118۸51 (ص.) کسی که به ست 
77178:نعمست: 2622۸ [ع. تعمه ]| (.) انجه باعث 
62011:(ص.) نباز مند» محتأج» مستمند؛ ج. مفتقر بن. 
79927:فقبران و مستمندان را در آن نگهداری کنند؛ 
93944:(عم.) تنگدست» بیچاره که از مستمندی
```


## [2026-09-07T17:44:13.169Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD && awk 'NR<=2093 && /\\[pdf page/ {n=$0; ln=NR} END{print ln, n}' FFD_pages.txt; sed -n '2075,2100p' FFD_pages.txt"
}
```


### [2026-09-07T17:44:14.460Z] TOOL RESULT

```
2084 [pdf page 82]
مانست-
«مانست» مادةٌ ماضی جعلی است. از «مان» < فارسی میانه 830 < ایرانی باستان
42 13302 ماد مضارع جعلی است از 13382. 12372 اسم است به معنی «هیئت
ظاهری».
مُردن :
مُرد < فارسی میانه ۵۶۵ < ایرانی باستان 13-1۵" برای 12 > آراست. 17
صورت ضعیف ريشةٌ 1387 به معنی «مردن» است.
میر < فارسی میانه 3۲۲ < ایرانی باستان 2دیط*. برای ساختن مادهٌ مضارع از
ریشه به کار می‌رفته است.
[pdf page 82]
ماده‌های ماضی و مضارع قارسی دزی شش ۷۷
مشت.
مُشت + فارسی میانه 151 + ایرانی باستان 1۹-1۵*. برای ۵ > آراست. 177
صورت.اصلی ۲5 است» 2 پیش از ۲ به 5 بدل شده است. 172 صورت ضعیف ريشهةٌ
2 به معنی «مالیدن» است.
مال + فارسی میانه 721 + فارسی باستان 1۵۳4-8* < ایرانی باستان 1۵72-۵*. برای
3 > آرای.
موییدن
«مویید» مادهٌ ماضی جعلی است. از مادهٌ مضارع ساخته شده است.
موی < فارسی میانه 136 < ایرانی باستان 1۳۵-2*. برای 2 آرای.
ریش 13200 به معنی «نالیدن» است.
نازیدن
«تازید» مادهٌ ماضی جعلی است. از مادةٌ مضارع ساخته شده است.
ناز ج فارسی میانه 232 + ایرانی باستان ۸32*. 232 در ایرانی باستان اسم است به
معنی «شادی»» «افتخار». 132 در فارسی میانه «شاد بودن» «مفتخر بودن» معنی
می‌دهد.
```


## [2026-09-07T17:44:23.688Z] TOOL CALL #61: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py FFD:77 --image 2>&1 | head -8"
}
```


### [2026-09-07T17:44:25.039Z] TOOL RESULT

```
no scan of FFD covers printed page 77 (see 'scans' in refs_online.json)
```


## [2026-09-07T17:44:28.378Z] TOOL CALL #62: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'));print(json.dumps(d['FFD'],ensure_ascii=False,indent=1))\""
}
```


### [2026-09-07T17:44:29.870Z] TOOL RESULT

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


## [2026-09-07T17:44:33.933Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD && grep -n -B3 -A6 \"موييدن\\|موییدن\" FFD_pages_faseng.txt | head -40"
}
```


### [2026-09-07T17:44:33.987Z] TOOL RESULT

```
ugrep: warning: FFD_pages_faseng.txt: No such file or directory
```


## [2026-09-07T17:44:37.301Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD && ls; echo; timeout 600 python3 /home/sfmqrb/git/rishe/tools/ref_page.py FFD:77 --pdf-page 82 --image 2>&1 | head -6"
}
```


### [2026-09-07T17:44:38.711Z] TOOL RESULT

```
FFD_asmaneketab.pdf
FFD_pages.txt
FFD_pages.txt.pages

Traceback (most recent call last):
  File "/home/sfmqrb/git/rishe/tools/ref_page.py", line 95, in <module>
    sys.exit(main(sys.argv[1:]))
             ^^^^^^^^^^^^^^^^^^
  File "/home/sfmqrb/git/rishe/tools/ref_page.py", line 63, in main
    pdf = scan["file"] if os.path.isabs(scan["file"]) else os.path.join(REFS, scan["file"])
```


## [2026-09-07T17:44:44.244Z] TOOL CALL #65: Bash

```json
{
 "command": "pdftoppm -f 82 -l 82 -r 200 -png -singlefile data/verification/sources/refs/incoming/FFD/FFD_asmaneketab.pdf \"$TMPDIR/ffd82\" 2>/dev/null || pdftoppm -f 82 -l 82 -r 200 -png -singlefile data/verification/sources/refs/incoming/FFD/FFD_asmaneketab.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/ffd82; ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/ffd82*"
}
```


### [2026-09-07T17:44:45.998Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 61328 Sep  7 13:44 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/ffd82.png
```


## [2026-09-07T17:44:49.314Z] TOOL CALL #66: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/ffd82.png"
}
```


### [2026-09-07T17:44:49.340Z] TOOL RESULT

```

```


## [2026-09-07T17:45:15.323Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== LEW formica\"; grep -n \"formica\" LEW_1910.txt | head -5; echo \"== LAT formica\"; grep -n \"formica\" LAT.txt | head -5; echo \"== KLN formic\"; grep -n \"formic acid\\|formic (\\|formica\" KLN_1966.txt | head -6; echo \"== SKT\"; grep -n \"formic\\|formica\" SKT.txt | head -5; echo \"== NYB moy\"; grep -n \"mwd\\|mōy\\|moyag\" NYB_vol2_glossary.txt | head -8"
}
```


### [2026-09-07T17:45:15.497Z] TOOL RESULT

```
== LEW formica
== LAT formica
19806:*- par diaaimilation: y. formica, et peut-etre dans *mr~: y.frem 5
23592:formastrum n.: opus pistorium (Gloaa.).formica
23620:formica (furmlca app.Prob. GLK IV 197,37), -ae f.: fourai. Ancien.
23624:cf. p,upp,T}>ct.^<»); M.L.3446, d'ou formica(bi) lis; formicoleon, Isid.Or.
23630:Le lat .formica doit resulter d'une dissiailation de *morml- (cf. for¬
== KLN formic
7479:chloroform,  n.,  a  volatile  liquid,  CHC13,  used  as an  anesthetic  (chem.)  —  F.  chloroforme,  a  hybrid coined  by  Jean-Baptiste  Dumas  (1800-84)  in 1834  fr.  chloro-  and  F .formique,  ‘formic’  (fr.  L. formica,  ‘ant’,  see  formic);  so  called  by  him  in allusion  to  its  capacity  of  forming  potassium chloride  and  formic  acid.
15184:‘ant’,  with  L.  formica,  ‘ant’,  and  Gk.  poppui, ‘bugbear,  hob,  goblin’,  with  L.  formidd,  ‘dread, terror’.  The  connection  of  L.  forma  with  ferire, ‘to  beat,  cut’,  suggested  by  Pick  and  others  is justly  rejected  by  Hofmann  in  Walde-Hofmann, LEW.,  I,  p.530.  See  morpho-  and  cp.  formal, formula  and  conform,  deforpi,  inform,  v.,  in¬ form,  adj.,  perform,  reform,  transform,  uniform. Derivatives:  formless,  adj.,  formless-ly,  adv., formless-ness,  n.
15195:formic,  adj.,  1)  of,  or  pertaining  to,  ants;  2)  per¬ taining  to,  or  designating,  a  colorless  acid, HC02H  (chem.)  —  Contraction  of  *formic-ic, fr.  L.  formica,  ‘ant’,  dissimilated  fr.  *mor-mica, fr.  orig.  *vormica;  cogn.  with  OI.  vamrt-  (fern.) vamrah  (masc.),  ‘ant’,  valmt-kah  , ‘anthill’, Avestic  maoiri-.  Arm.  mrjiun,  Gk.  ;j.up[j.rj5, OSlav.  mraviji  (for  *morvi),  OIr.  moirb  (for *morvi),  W.  myrion,  ON.  maurr,  ‘ant’.  See  pis¬ mire  and  cp.  myrmeco-  and  the  second  element in  chloroform.  For  the  contraction  of  *formic-ic into  formic  see  haplology.
15197:Derivatives:  formicary  (q.v.),  formic-ate,  intr.v., formic-ate,  adj.,  formication  (q.v.),  formic-ative, adj.,  Formicidae  (q.v.)
15198:formicary,  n.,  an  ant’s  nest.  —  ML .  formicarium, fr.  L.  formica,  ‘ant’.  See  formic  and  subst.  suff. -ary.
15199:Derivative:  formicari-an,  adj.,  pertaining  to ants’  nests.
== SKT
3411:chloroform.  (L.  anJ  Gk.)  The  latlci clrment  rtlates  to  formic  acid,  an  acid formerly  ob.ained  from  red  aBts.»L.  /i»r- mittt.  an  ant,
6980:Formio.  pertaining  to  ants.  (L.)  L. formica,  an  ant.
== NYB moy
1848:ham-mód [hm mwd] having hair of the same colour 12075 (read MNW hm mwd). — V. mod.
1849:hāmēdēn [h'mwdyn'] of every kind, all, whole, subst., and adj. placed before its subst., but after a pron.: hac öisän ~ 319; passim; adv. in short, brief 111, — *hama- (v. hamist) +- abdén > audén > oden, NW form corresponding to SW ātvēnak (g. v.); thus a synonym of ham-ātvēnak (g. v.). Paz. hamöin. The scribes write and read admodin = hdmwdyn = hémodén ; I have throughout corrected this form to h?mw- = hämö-, but perhaps hčmo- is an authen- tic form, cf MPrth hynz’wr ‘powerful’ (A-H III and, with correct explanation, BBB) = henzävar < *ham-zävar.
2582:mod [mwd] hair 932%, 1001, 120% (v. ham-mód); cand ~-é tak ... né not a hairbreadth 7272. — SW pronunciation moi; Paz. mu; NP mu, mūy.
2583:módak [mwdk'] mourning for the dead 862°. — Paz. müyai < mēdakēh, Skr. v. keša-trotana- ‘the tearing of hair’ (through influence of the preceding w.); MPrs. mwyg ‘lamenting’ (A-H II). Cf NP must ‘trouble, lamentation’ < *mud-ti-.
2738:nimütan [nmwtn'] nimay- [nm?d-], pres. 3d p. sg. nm'dt', inser. nm?dty, both = nimáyét, 3d. p. pl. nm’dynd = nimdyénd, to show, to denote, to signify, to indicate 512, 810 etc.; to teach 81!!; — a syn. of kartan : patifras ~ 10112; handácak ~, v. the preceding w.; bahrak ~ to allot a share 1152-35, — < ni + Av. OP (1165) mäy-, cf framütan; MPrth nm?dn nm’y-; MPrs nmwdn nm?y; Paz. NP namudan; Verbum 203.
6053:nihuftan nm?e: naīnāc nmwdn, nm’y: nimütan nrm: *a-namr-tom nrysh-yzd: Narsah ns'h: nasāi nw(w)m: nahom nwx: Naxu-Ohurmazd nxwst: naxUist nym: nem nymrwz: nöm-röc nyrwg: nörök nyyšydn, nyyš-: murv- niš nzd: nazd nzdyk: nazdik
```


## [2026-09-07T17:45:35.194Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== PHD page tags near 3584\"; awk 'NR<=3595 && /\\[pdf page/ {n=$0;l=NR} END{print l,n}' PHD_pages.txt; sed -n '3580,3592p' PHD_pages.txt; echo \"== NYB tags\"; awk 'NR<=2583 && /\\[pdf page|^Page |^[0-9]+$/ {n=$0;l=NR} END{print l,n}' NYB_vol2_glossary.txt | head -3"
}
```


### [2026-09-07T17:45:36.428Z] TOOL RESULT

```
== PHD page tags near 3584
 
·mizne [m(y)znydy] mist, dew.
miig [mwk ] shoe:-
            '
·moy-mard [m~!mlt', -gGBRA I N muy] magus.
mor [mwl I N -] ant.
m('jrd [mwlt' I N -] myrtle.
morwarid [mwlw'lyt 1M mwrw)ryd, N -] pearl.
                         '
·mowbed [mgwpt l I N mobad] Mazdean priest.
moy [mwd IN -] hair.
moyag [mwdk I N maya] lamentation.
                   '
moyen [mwdyn ] (made of) hair.
== NYB tags
2549 132
```


## [2026-09-07T17:45:37.022Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== KLN page marker near formic\"; awk 'NR>=15150 && NR<=15200 && /^[0-9]{3,4}$|page/ {print NR\": \"$0}' KLN_1966.txt | tail -5; echo \"== ARY\"; grep -n \"مور\\b\\|مویه\" incoming/ARY/ARY_pages.txt | head -10"
}
```


### [2026-09-07T17:45:38.286Z] TOOL RESULT

```
== KLN page marker near formic
15194: 613
== ARY
83:می‌بردند و وپژگی‌های بدنی و اجتماعی و فرهنگی آنان را مورد ستایش قرار می‌دادند. در دوران
93:عنوان یک برچسب نژادی و به منظور تأ کید برتری خودشان مورد تحریف قرار دادند. مثلاً در نظر
97:بهمین دلیل پس از شکست نازی‌ها در پایان جنگك جهانی دوم» واژه‌ی «آریایی» کمتر مورد
104:نکته‌ای که باید مورد تأ کید قرار گیرد این است که منظور از «هند و اروپایی» نژاد بخصوصی
116:نکات زیر درستی دیدمان فوق را مورد تردید قرار می‌دهد: ۱- کردستان وارمشتان و نواحی
211:میان این دو دسته زبان (نواحی شمال دریای سیاه) بوده است. آنچه این بیش را تا اندازه‌ای مورد ۱
280:شده‌اند. اصل جغرافیای زبانشناسی فوق‌الذکر مورد قبول همه‌ی دانشمندان نیست ولی در نظرکسانی
326:(16780۸71) ساخته شده. در کنار جسد گنجانه‌ی سفالی (و در مورد بزرگان قوم) اسلحه و سپر قرار . ذٌ
368:هشدار در مورد خاستگاه هند و اروپائیان
374:هیچ دلیل مستندی برای چنین فرضیه‌ای وجود ندارد.... در مورد هند و اروپائیان هیچ گواه و
```


## [2026-09-07T17:45:46.322Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -c \"pdf page\" PHD_pages.txt; grep -n \"pdf page\" PHD_pages.txt | sed -n '1,3p'; awk '/\\[pdf page/{p=$0} NR==3584{print \"line3584 page tag:\",p}' PHD_pages.txt"
}
```


## [2026-09-07T17:45:46.791Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"MUR\\|MUYE\\|MOUR\\|MUY\" incoming/ARY/ARY_latin_index_pages.txt | head -10"
}
```


### [2026-09-07T17:45:47.617Z] TOOL RESULT

```
0
line3584 page tag:
```


### [2026-09-07T17:45:47.663Z] TOOL RESULT

```
1721:BARNHART: (EDEG) 315, HAMUR — (OLD SAXON) oS gyS
2606:AM-MIVANT HITTITE) «20 AMURDAD PAHLAVI) 54
3532:BARMUZ, BARMUR, BARMAZ, BARMU, BOOZ
9353:MACKENZIE: (ARMOUR) 102 ZIRA AFGHAN) (34), gail
11122:MURNAN, MORNEN HISHMARAITI, HISHMAR-
11124:MURNAN OSHMAR, OSHMARTAN,
11125:MOURN HENGLISH) JS ‘OSHMURDAN, SHUMAR
11131:(MEMORY) 650,(MOURN) 682 SANSKRIT) xy Saile
11135:ONIONS: (MOURN) 593 MEMOR, MEMORIA (LATIN) oY
11136:SKEAT: (MOURN) 388 MAURNAN “AGOTHIC) S36
```


## [2026-09-07T17:45:59.443Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -nE \"^مور|^ مور|مور \\(|مورچه\" incoming/ARY/ARY_pages.txt | head -10; echo \"== ANT\"; grep -n \"ANT (ENGLISH)\\|(ANT)\" incoming/ARY/ARY_latin_index_pages.txt | head -5"
}
```


### [2026-09-07T17:45:59.503Z] TOOL RESULT

```
637:مورد بحث قرار پدهند. طبق برآوردی که شده (193 ,112873۳10) حدود ۸۵ درصد واژه‌های ایرانی
981:مورد به قربانی کردن انسان اشاره شده است. ظاهراً در نظر هندیان پاستان» انسان والاترین جانداری
1445:مور موز 8۵08 ات۸ للقط ,50۸
== ANT
14018:MACKENZIE: (ANT) 102 (OLD SCANDINAVIAN) (5.5)
14021:; AMINDAROV: (ANT) 185 MYRE “OLD BYU, gli *
```


## [2026-09-07T17:46:04.867Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '13995,14035p' incoming/ARY/ARY_latin_index_pages.txt"
}
```


### [2026-09-07T17:46:04.908Z] TOOL RESULT

```
wpe TUN
seed Ab ely cat jl pa MENTAL lS! sols -¥
[pdf page 480]
TAI open
MYRA (SWEDISH) «5. p+ MAOIRI- HAVESTAN) yleas)
s(NORWGIAN) 539 3 MOR, MORCAK — (PAHLAVI) 5
-MAUR (MIGEMAUR) MALJIG, MULJUG — {OSSTIC) 244)
MIERE :(DUTCH) (sola MURI (KURDISH) 3,5
HOLD CHURCH SLAVIC) pS 531 MOR, MORIK ABALUCHI) gx gy
MRAVI MOR, MORIK, (AFGHAN!) (4) {Uil
MROWKA (POLISH) long) MEZHAY
MURAVEJ (RUSSIAN) guy MARME :(TOKHARIAN B) B sas
MRAVENEC CZECH) Soy MWRCH «(SOGHDIAN) tice
MRAVI, MRAVIJA (BULGARIAN) «5 ky YVARML, (SANSKRIT) a) Sail
MRAVEC s(SLOVAK) 5 gla! VALMIKA
° MOIRB (OLD IRISH) 4S 543 p! MURCHIUN ARMENIAN)
MYRION WELSH) jy WORMIKAS, MURMEX.(GREEK) iy
MERIEN BRETON) sin -MICA (FORMICA) ALATIN) ys
' MURYON GAELIC) SIE FOURMI SFRENCH) sil}
HORMIGA +(SPANISH)  glailes!
REFERENCES thy FORMICA HUTALIAN) gles
POKORNY; —SOS~*~S*~*~«SD FURMICA HRUMANIAN) ley
DELAMARRE: (FOURMI 143 FORMIGA (PORTUGUESE) (is
MACKENZIE: (ANT) 102 (OLD SCANDINAVIAN) (5.5)
i ONIONS: (PISMIRE) 684 MAURR, MYRE
i SKEAT: (PISMIRE) 454 MIRE HOLD FRISIAN) S523 215
; AMINDAROV: (ANT) 185 MYRE “OLD BYU, gli *
\ rors sebt oly -MIRE (PIS-MIRE)\ (ENGLISH) 161
: MYRE DANISH) Sails
|
MUSHIKA MUSH, MUSHAKA, (AVESTAN) (ou)!
[pdf page 481]
. (028) oy 2S" pM) On eye [EAT
MUS (NORWGIAN) 6355 MUSHK (PAHLAVI) 5 shy,
MUIS (DUTCH) gala MIST, MISTE HOSSETIC) ou s\ |
OLD CHURCH why) AT EME! MISHK KURDISH) 2,5 q
‘eMYSHI MUSHK, MUSHK —:(BALUCHI) 5h {
MYSZ (POLISH) ging) MOZHAK, HAPGHANI) (y2t;) gli! q
MYSH LARUSSIAN) «gus MAGHAK
MYSH CZECH) Sop MUs, MUSH (SANSKRIT) ey St. x
MISH © (SERBIAN) «9 pe MUKN, MOUG, — (ARMENIAN) . <4)!
```


## [2026-09-07T17:46:17.377Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"MOYAK\\|MOYIDAN\\|MUYIDAN\\|MUST (\\|MUST,\\|MOY,\" incoming/ARY/ARY_latin_index_pages.txt | head -10"
}
```


### [2026-09-07T17:46:17.423Z] TOOL RESULT

```
13770:LITHUANIAN) gg.) MUST (PAHLAVI) 5 pgp
```


## [2026-09-07T17:46:20.497Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '13745,13790p' incoming/ARY/ARY_latin_index_pages.txt"
}
```


### [2026-09-07T17:46:20.549Z] TOOL RESULT

```
| BUCK: m2 MUNTAR, MUNTER, MENDI,

ever Misha delice MENDEN
[pdf page 471]
Sy whe | FVY
lentloal
ile A isa 9 ey SG 50 o3hy yl oe 1
J yh. ee aTisln Sole
% pele pe pe Ste SSF 3 3s ol p
ea chal ys Let sda 9 AS glu 2 cal pt
23 dBA 3 Gd 205s oll ee
: Shas BLT 52 Sly ol oe
sel aag a" GIE" y "ee 3” PF eMAZDA plies! ,> -¥
MUCHUTU PAHLAVI) 6 hy
HOLD IRISH) 4S 5) p\ MICHAK, MIZH, MIZHAG
DE-MECCIM KURDISH) 2,
MYGR (WELSH) 3 MIJGAN, MIZHL, MIZHANK, MUJGAL
ABALUCHD) gx de
‘REFERENCES Wena MICAC, MISHASH, MIZHAGHAN |
POKORNY, —SSS~S~«STABTAB NIMISHA (SANSKRIT) ey Sst. |
MACKENZIE: (EYELASH) 113 MICO, MICARE X(LATIN) 3
Leeds Look eb oy (OLD BULGARIAN) 55 j\aly
~ Sent loo
: sree ahem 1oSY Ob5 29 Sly onl |
MYSLU (OLD BULGARIAN) aS 66 lil *MUSTI (OLD PERSIAN) kl poh
LITHUANIAN) gg.) MUST (PAHLAVI) 5 pgp
MAUDZHIG, MAUSTI MUTHOS GREEK) sbi
MAUDJAN AGOTHIC) 3
[pdf page 472]
Mle
MACKENZIE: (COMPLAINT) 107 ‘REFERENCES bok,
Jeetloal
Om tae gin 85 32 05a onl
MADHA., MAD-—.(AVESTAN) gleeyl

REFERENCES beth MAST HMPAHLAV) 6 hy

POKORNY, SSS ag MEST KURDISH) «53,5
AMINDAROV: (DRUNK) 215 MADYATI, (SANSKRIT) cy Sl.

Tey sabi ou, MAMATTI, MANDATI, MATTA-

MECH RUSSIAN) gy, MARSHA HAVESTAN) (glues)
MECHD :(BULGARIAN) 65 ,\sh, PAHLAVI) 65 shy
MAISHAS :(LITHUANIAN) gl.) MASHK, MASHKIZAG
```


## [2026-09-07T17:46:33.821Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== SYN ant\"; grep -n \"formica\" SYN.txt | head -5; echo \"== WLD Bd2 meudh\"; grep -n \"moja\\|mudh-\\|maudh-\\|meudh-\\|must .Klage\\|maudjan\" incoming/WLD/WLD_Bd2_pages.txt | head -10"
}
```


### [2026-09-07T17:46:33.880Z] TOOL RESULT

```
== SYN ant
== WLD Bd2 meudh
16733:                            meuk          meudh-, maudh-, mudh-                          255
16790:meudh-, meudh-, mudh- etwa ^,worauf bedacht sein, sehnlich, schmerzlicb
16792:   Xpers. moja ,,Klage” {-j- aus -r?-, vgl.:) must ,,klage“            {-st-    aus -dhrt):
```


## [2026-09-07T17:46:39.401Z] TOOL CALL #77: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '16788,16812p' incoming/WLD/WLD_Bd2_pages.txt"
}
```


### [2026-09-07T17:46:39.448Z] TOOL RESULT

```
Glossar) anreihen, dies         ist   aber mtigh ,,Sklave“!

meudh-, meudh-, mudh- etwa ^,worauf bedacht sein, sehnlich, schmerzlicb
     verlangen^t
   Xpers. moja ,,Klage” {-j- aus -r?-, vgl.:) must ,,klage“            {-st-    aus -dhrt):
got. maiidjan, gamatidjan ,,jmdn erinnern''; lit maiidfih,             tnaiisti   „sehnlich
256                                    meq          megh

verlaiigen“,    apmawcZas „Verdru6, Sorge“; d})g.mysJ'b „Gedanke“; nicht (mit
ani. s~) air.   smuainm „denke‘' (nicht aus '^smeudnio^ smoiidnid)        ;   sehr fraglich
istj   oh gr.     „R®de, Worf',          „reden; sorgen; uberlegen^‘ den
BegriflP der Uberlegung und nicht vielmehr der der miindlichen AuBerung
(dann      zum Schallwort mu)        das urspriingliche      ist.   Wood Mn. [15, 96],
Fick in^ 302, Pedersen KG. I 113.

iiieq[-    Naturlaut dos Meckerns.
      makamakCiyaU „quakt‘^ makaha- m. „ein Tier“, mekci- m. „Bock“
     Ai.
(Thurneysen Yerba auf -io 20; e durch Keuschopfung des Schallwortes,
nicht im Ablaut zum i von lat. micclre) arm. maki „Schaf (s. Pedersen
                                                        ;
                                                                          '


KZ. 39, 390);
```


## [2026-09-07T17:46:47.088Z] TOOL CALL #78: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && grep -n \"موژه\\|موژ \\|مویه\" BQT_v4_pages.txt | head -12"
}
```


### [2026-09-07T17:46:47.141Z] TOOL RESULT

```
5315:۴ - قی : موی » موبه . ورك : موژه - - رك : موژه :
5317:چو زلف خوبان در جوبهاش مرزنگوش چو خطخوبان بر موژهاش سیسنس.
5319:ولی دردبوان فرخی چاپ عبدالرسولی (س ۱۳۲) بجای موژهاش « مرزهاش >آمده .
5355:۹ - ر3: موژ . ۴ - رك : جهانگیری » رشیدی .
5585:مویه گر ۴ - بنتح‌کاف فارسی » توحه | ووز را میکویند :
5595:- بلفظ پارسی وچینی و خماخرو بلحن مویهٌ زال و قصیدء لغزی .
7511:در حسرت رخار قو ای زا روی ! از باله چونال گشتم , ازمویه چر موی.
7599:۴ - سولت او دران صف ناورد زن نامویه بر کند از هرد -
19398:هموژه - بفتم زای فارسی بروزن‌موزه, هوش - با نانی مجهول بروزن کوش,
```


## [2026-09-07T17:46:54.155Z] TOOL CALL #79: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && awk '/\\[pdf page/{p=$0} NR==5315{print \"5315:\",p} NR==5355{print \"5355:\",p} NR==5585{print \"5585:\",p}' BQT_v4_pages.txt; sed -n '5305,5320p' BQT_v4_pages.txt; echo \"-----\"; sed -n '5580,5600p' BQT_v4_pages.txt"
}
```


### [2026-09-07T17:46:55.453Z] TOOL RESULT

```
5315: [pdf page 134]
5355: [pdf page 135]
5585: [pdf page 141]
۹ - موز 088886 (ش) میوة درخت موز ۳88826۲ (فر) ( 18و62 له ۳۵52 )
است . رل : ستوده ص ۷۹-۷۸ ؛ وآن از گیاهان يك لپه است. ۲ - +« موز ... میوه‌ای
بود درمصی معروق, وموز مکی چون باتنگانی بود . طیان (مرغزی) گوید :

موز مکی اگرچه دارد نام نکنندش چوشکر اسر جام. > « لفت فری ص ۱۸۸ >

۴ - «-موز ترکش بود » « لغت فرس ص ۱۸۸ *. ظ. تراکش مصحف « ار کس > است
که بعد درمتن برهان ذکرشده و۶ بر کش > هم که موّلف کمان برده آنهم ظ. مصحف همین‌کلمه
است » وگوبا اصل « نرکس موژان > بوده . رك : موژان » موجان .

۴ - قی : موی » موبه . ورك : موژه - - رك : موژه :

چو زلف خوبان در جوبهاش مرزنگوش چو خطخوبان بر موژهاش سیسنس.
فرخی سیستّانی « جهالگیری >.
ولی دردبوان فرخی چاپ عبدالرسولی (س ۱۳۲) بجای موژهاش « مرزهاش >آمده .

-----
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
```


## [2026-09-07T17:47:10.288Z] TOOL CALL #80: Bash

```json
{
 "command": "for u in \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/morw%C3%ADs\" \"https://en.wiktionary.org/wiki/%D9%85%D9%88%DB%8C%D9%87\" \"https://en.wiktionary.org/wiki/%D9%85%D8%B3%D8%AA%D9%85%D9%86%D8%AF\"; do echo \"=== $u\"; timeout 120 python3 tools/fetch_source.py \"$u\" --note \"page 341: PIE ant root; Persian muye/mostmand for root Moudh\" 2>&1 | tail -1; done"
}
```


### [2026-09-07T17:47:15.036Z] TOOL RESULT

```
=== https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/morw%C3%ADs
/home/sfmqrb/git/rishe/data/verification/sources/web/c5ec3cc14a645d3d.txt
=== https://en.wiktionary.org/wiki/%D9%85%D9%88%DB%8C%D9%87
/home/sfmqrb/git/rishe/data/verification/sources/web/a88916b69e926d77.txt
=== https://en.wiktionary.org/wiki/%D9%85%D8%B3%D8%AA%D9%85%D9%86%D8%AF
/home/sfmqrb/git/rishe/data/verification/sources/web/e2f4005cb55bd815.txt
```


## [2026-09-07T17:47:20.570Z] TOOL CALL #81: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"### PIE morwis\"; grep -n -i \"ant\\|Proto-Iranian\\|maoiri\\|reconstruct\" c5ec3cc14a645d3d.txt | head -12; echo \"### muye\"; grep -n -i \"etymolog\\|Middle Persian\\|lament\\|mourn\\|FETCH\" a88916b69e926d77.txt | head -10; echo \"### mostmand\"; grep -n -i \"etymolog\\|Middle Persian\\|must\\|FETCH\" e2f4005cb55bd815.txt | head -10"
}
```


### [2026-09-07T17:47:20.639Z] TOOL RESULT

```
### PIE morwis
1:URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/morw%C3%ADs
4:TITLE: Reconstruction:Proto-Indo-European/morwís - Wiktionary, the free dictionary
6:Reconstruction:Proto-Indo-European/morwís - Wiktionary, the free dictionary 
68: Reconstruction notes 
71: Descendants 
78: Reconstruction:Proto-Indo-European/ morwís 
82: Reconstruction 
132: This Proto-Indo-European entry contains reconstructed terms and roots . As such, the term(s) in this entry are not directly attested , but are hypothesized to have existed based on comparative evidence.
147: ant 
149: Reconstruction notes
152: The term was seemingly subject to a significant amount of tabooistic distortion in the daughter languages. [ 3 ] 
154: Descendants
### muye
2:FETCHED: 2026-09-07T17:47:13Z
6:FETCH FAILED: HTTP Error 404: Not Found
### mostmand
2:FETCHED: 2026-09-07T17:47:15Z
62: Etymology 
138: Etymology
146: ( Classical Persian ) IPA ( key ) : /must.ˈmand/ 
156: mustmand
```


## [2026-09-07T17:47:24.578Z] TOOL CALL #82: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && sed -n '138,146p' e2f4005cb55bd815.txt; echo \"### PIE descendants\"; sed -n '154,200p' c5ec3cc14a645d3d.txt | head -30"
}
```


### [2026-09-07T17:47:24.638Z] TOOL RESULT

```
 Etymology
 [ edit ] 

 From مست ( most ) +‎ ـمند ( -mand ) .

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /must.ˈmand/ 
### PIE descendants
 Descendants
 [ edit ] 

 Terms derived from the Proto-Indo-European word *morwís 

 Proto-Armenian: ( with assimilation *morwo- > *mormo- ) 
 > ? Middle Armenian: մորմ ( morm , “ tarantula ” ) 

 ⇒ Proto-Armenian: 
 Old Armenian: մրջիւն ( mrǰiwn ) 
 Armenian: մրջյուն ( mrǰyun ) 

 Proto-Balto-Slavic: *marwís ( see there for further descendants )

 Proto-Celtic: *morwis   f ( see there for further descendants )

 Proto-Germanic: *mauraz , *miurijǭ ( see there for further descendants )

 Proto-Hellenic: ( with assimilation *morwo- > *mormo- ) 
 Ancient Greek: μύρμηξ ( múrmēx ) ( see there for further descendants )

 Ancient Greek: μύρμος ( múrmos ) 

 Proto-Indo-Iranian: *marwíš   m ( see there for further descendants )

 ⇒ Proto-Italic: *mormīkā ( see there for further descendants )

 Unsorted formations:
 > ? Ancient Greek: βόρμαξ ( bórmax ) , βύρμαξ ( búrmax ) ( or from *worm- )
```


## [2026-09-07T17:48:31.082Z] TOOL CALL #83: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/page-313.json'))\nprint(json.dumps(d['entries'][0], ensure_ascii=False)[:2500])\n\" ; echo; ls data/verification | head"
}
```


### [2026-09-07T17:48:32.394Z] TOOL RESULT

```
{"entry": 0, "root": "Leup", "verdict": "confirmed", "modern_form": "PIE *lewp- / *lewb(ʰ)- 'to peel off, strip the bark from, break off, damage' (Pokorny 690–691 leup-, leub-, leubh-; Watkins/AHD leup-)", "note": "Pokorny IEW 690–691 has exactly this root: 'leup- und leub(h?)- \"abschälen, entrinden, abbrechen, beschädigen\"', with the p-forms Skt. lumpáti, lopáyati, Lith. lupti, Russ. lupitь and the b-forms ON laupr, OE lēap, Goth. laufs 'leaf'. Nourai's language label (Indo-European), his headword shape 'Leup' and his gloss 'to break, peel off' are all correct, and POK:690 is the right page. Cross-cutting caveat: the root has always been hard to keep apart from the near-homophonous *Hrewp- 'to break, tear' (POK 868 reup-, Lat. rumpō); Pokorny, Walde-Pokorny and Mann keep the two apart, while Cheung (2007) assigns the Iranian 'rob' verb to a separate root *raup¹ of unclear IE pedigree. That is why the Iranian branch (nodes #1–#3) is graded 'plausible' rather than 'confirmed', while the Indic and Germanic branches are secure.", "note_fa": "ریشهٔ هندواروپایی آغازین *lewp- / *lewb(ʰ)- به معنی «پوست/پوسته کندن، کندن، شکستن، آسیب رساندن» است؛ پوکورنی در فرهنگ ریشه‌شناسی هندواروپایی (ص ۶۹۰–۶۹۱) همین ریشه را با صورت leup-, leub(h)- و همین معنا آورده و شواهد آن را سنسکریت lumpáti «می‌شکند، غارت می‌کند»، لیتوانیایی lupti «پوست کندن» و گوتی laufs «برگ» می‌داند. برچسب زبانی، صورت ریشه و معنایی که نورایی داده است درست است و ارجاع او به POK:690 نیز دقیق است. تنها نکتهٔ احتیاطی این است که این ریشه با ریشهٔ نزدیک‌آوای *Hrewp- «شکستن، دریدن» (پوکورنی ص ۸۶۸، لاتینی rumpō) آمیخته می‌شود و چونگ (۲۰۰۷) فعل ایرانی «ربودن» را به ستاک جداگانهٔ *raup می‌برد؛ از این رو شاخهٔ ایرانی این نمودار با احتیاط پذیرفته شده است.", "sources": ["https://en.wiktionary.org/wiki/loot", "https://www.etymonline.com/word/lobby"], "ref_check": [{"ref": "POK:690", "status": "supports", "note": "POK_full.txt (line 56281 ff.) 'Root / lemma: leup- and leub-, leubʰ- / Meaning: to peel, cut off, harm, etc. … Page(s): 690-691'; the printed German (POK_02.txt, same entry) reads 'leup- und leub(h?)- „abschälen, entrinden, abbrechen, beschädigen“'. Nourai's gloss 'to break, peel off' is a fair rendering and the page is right."}], "consulted": [{"src": "WLD", "where": "Bd. II 417–418 (incoming/WLD/WLD_Bd2_pages.txt line 27648 ff.)", "stance": "supports", "note": "'leup- und leub(h?)- „abschälen, entrinden, abbrechen, beschädigen“ … Mit p-: Ai. lumpáti „zerbricht, beschädigt, plündert“, lopáyati „verletzt“ (=

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
```


## [2026-09-07T17:48:37.325Z] TOOL CALL #84: Bash

```json
{
 "command": "python3 - <<'EOF'\nimport json,glob\nfor f in ['data/verification/page-313.json','data/verification/page-312.json','data/verification/page-316.json']:\n    d=json.load(open(f))\n    for e in d['entries']:\n        for n in e.get('nodes',[]):\n            if not n.get('words'):\n                print(f, json.dumps(n,ensure_ascii=False)[:1200]); print()\n                break\nEOF"
}
```


### [2026-09-07T17:48:38.592Z] TOOL RESULT

```
data/verification/page-313.json {"id": 6, "lang": "Germanic", "words": "", "verdict": "confirmed", "derivation": "A pass-through node standing for the Germanic reflexes of the b-variant of the root: Proto-Germanic *laubaz/*lauban 'leaf, foliage' (Goth. laufs, OE lēaf, OHG loub, G. Laub) and the derived *laubjō 'shelter of foliage, roof made from bark' (OHG louba, MHG loube, G. Laube). The note Nourai puts in the box — 'a group of words meaning bark peeled off trees, roofs made of bark, roof or top of a high place' — is a paraphrase of Watkins's AHD entry, which is also the reference he cites; the semantics ('what is peeled off a tree' > 'leaf' / 'bark roof') is the standard explanation, and the '(roof or) top of a high place' half covers the disputed loft/luft group.", "derivation_fa": "این خانه گرهی گذری است و شاخهٔ ژرمنی صورت b-دار ریشه را نمایندگی می‌کند: ژرمنی آغازین *laubaz/*lauban «برگ، شاخ‌وبرگ» (گوتی laufs، انگلیسی باستان lēaf، آلمانی علیای باستان loub، آلمانی Laub) و مشتق آن *laubjō «سرپناهِ برگ، بامِ پوست‌درخت» (آلمانی علیای باستان louba، آلمانی Laube). توضیحی که نورایی در این خانه آورده، بازگفت مدخل واتکینز در پیوست ریشه‌های هندواروپایی فرهنگ American Heritage است — همان مرجعی که خود ارجاع داده — و معن

data/verification/page-312.json {"id": 8, "lang": "French", "words": "", "verdict": "confirmed", "derivation": "The empty pivot box is French lustre 'gloss, radiance' (attested 14th c.), which is not a direct continuation of Latin lūstrāre but a Renaissance-era borrowing from Italian lustro 'splendour, brilliancy' (from Italian lustrare < Latin lūstrāre); the noun is pan-Romance (Spanish/Portuguese lustre, Romanian lustru). Etymonline s.v. luster: \"from French lustre 'gloss, radiance' (14c.), common Romanic ... a noun ultimately from Latin lustrare 'spread light over, brighten, illumine'\"; Klein: \"MF. (= F.) lustre, fr. It. lustro, fr. lustrare\". In French the word then took on the concrete sense 'hanging light fixture, chandelier' (17th c.), which is the sense that both Persian لوستر and, partly, English luster inherit.", "derivation_fa": "این جعبهٔ خالی همان lustre فرانسوی است، به معنی «درخشش، جلا» (گواه‌شده از سدهٔ ۱۴م). این واژه ادامهٔ مستقیم lūstrāre لاتین نیست، بلکه وام‌گیری از ایتالیایی lustro «درخشش» است (خودِ آن از lustrare ایتالیایی و لاتین)؛ همین اسم در همهٔ زبان‌های رومی هست (اسپانیایی و پرتغالی lustre، رومانیایی lustru). سپس در فرانسوی سدهٔ ۱۷م معنای عینیِ «چراغِ آویز، چلچراغ» گرفت و همین معنا اس

data/verification/page-316.json {"id": 7, "lang": "French", "words": "", "verdict": "confirmed", "derivation": "Empty pass-through box: the French stage between Latin and the Persian loans below. The relevant French words are the nursery maman (< Latin mamma, reduplicated, first recorded 17th c. and the form actually borrowed into Persian) and, for the learned strand, mère < Latin māter and matière < materia. Latin mamma > French maman with the nasalised second syllable characteristic of French hypocoristics (cf. papa).", "derivation_fa": "این جعبهٔ خالی مرحلهٔ فرانسوی میان لاتین و وام‌واژهٔ فارسی است: فرانسوی maman (از mamma لاتینی، با دوگان‌سازی واژهٔ کودکانه) و نیز mère از māter و matière از materia. این گره فقط گذرگاه است و مشکلی ندارد.", "sources": ["https://www.etymonline.com/word/mammal", "https://en.wiktionary.org/wiki/%D9%85%D8%A7%D9%85%D8%A7%D9%86"], "ref_check": [{"ref": "None", "status": "not_checked", "note": "no reference given by Nourai for this pass-through node."}], "consulted": [{"src": "KLN", "where": "printed p.929 s.v. mamma", "stance": "supports", "note": "Klein lists 'F. maman' among the reduplicated *ma- forms alongside L. mamma."}, {"src": "LAT", "where": "s.v. mamma", "stance": "su
```


## [2026-09-07T17:49:11.831Z] TOOL CALL #85: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"مستمند:\" MON_part1.txt MON_part2.txt | head; grep -n \"مُست\\|مست ۲\" MON_part1.txt MON_part2.txt | head -5"
}
```


### [2026-09-07T17:49:11.901Z] TOOL RESULT

```
MON_part2.txt:60058:. الفت و مصاست دامُستن. (امسص.)
```


## [2026-09-07T17:49:17.572Z] TOOL CALL #86: Bash

```json
{
 "command": "sed -n '1,25p' tools/ganjoor.py"
}
```


### [2026-09-07T17:49:17.624Z] TOOL RESULT

```
#!/usr/bin/env python3
"""Corpus analyses against the Ganjoor corpus of Persian poetry.

Reads the official Ganjoor database dump (MySQL, from
https://github.com/ganjoor/ganjoor-db — data/dump.sql.gz), matches every
verse token against the dictionary's modern-Persian words with the same
conservative morphology the site's verse-linker uses, and computes:

  1. the poets' purism gradient over full divans (not Nourai's citations),
  2. first-attestation dates for borrowed words -> influx curves,
  3. token-frequency-weighted borrowing statistics.

Usage:
  ganjoor.py --import <dump.sql.gz> [ganjoor.db]   # one-time: MySQL dump -> SQLite
  ganjoor.py <ganjoor.db> [extracted-dir ...]      # writes data/research/ganjoor.json
"""
import collections, gzip, json, random, re, sqlite3, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import research

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "data" / "research"
```


## [2026-09-07T17:49:20.725Z] TOOL CALL #87: Bash

```json
{
 "command": "ls -la data/research/*.db data/*.db 2>/dev/null; ls data/research 2>/dev/null | head"
}
```


### [2026-09-07T17:49:20.781Z] TOOL RESULT

```
(eval):1: no matches found: data/research/*.db
domains.json
ganjoor.json
research.json
```


## [2026-09-07T17:49:28.883Z] TOOL CALL #88: Bash

```json
{
 "command": "timeout 120 python3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/%D9%85%D8%B3%D8%AA\" --note \"page 341, root Moudh: Persian most 'sorrow, complaint' (Etymology sections)\" 2>&1 | tail -1"
}
```


### [2026-09-07T17:49:30.212Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/244093519d94a7bb.txt
```


## [2026-09-07T17:49:33.527Z] TOOL CALL #89: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && grep -n -i \"Etymology 2\\|Etymology 3\\|sorrow\\|grief\\|Middle Persian\\|complaint\\|Proto-Iranian\" 244093519d94a7bb.txt | head -20"
}
```


### [2026-09-07T17:49:33.583Z] TOOL RESULT

```
93: Etymology 2 
128: Etymology 2 
293: Etymology 2
336: Inherited from Middle Persian 𐭬𐭮𐭲 ( mst /⁠mast⁠/ , “ drunk, bemused ” ) , from Proto-Indo-Iranian *matˢtás ( “ drunk, intoxicated ” ) , from Proto-Indo-European *meh₂d- ( “ wet ” ) . Cognate with Sanskrit मत्त ( matta ) .
444: Etymology 2
492: complaint 
575: Persian terms inherited from Middle Persian 
576: Persian terms derived from Middle Persian
```


## [2026-09-07T17:49:36.472Z] TOOL CALL #90: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && sed -n '440,500p' 244093519d94a7bb.txt"
}
```


### [2026-09-07T17:49:36.521Z] TOOL RESULT

```
 drunk ; drunkard 

 ( Islam , Sufism , figurative ) person who is intoxicated with or overcome with love for God; Sufi 

 Etymology 2
 [ edit ] 

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /ˈmust/ 

 ( Dari, formal ) IPA ( key ) : [mʊst̪] 

 ( Dari, formal ) IPA ( key ) : [mʊst̪] 
 ( Kabuli ) IPA ( key ) : [mʊst̪] 

 ( Hazaragi ) IPA ( key ) : [must̪] 

 ( Iran, formal ) IPA ( key ) : [most̪ʰ] 

 ( Tajik, formal ) IPA ( key ) : [must̪] 

 Rhymes: -ust 

 Readings

 Classical reading ? 

 must

 Dari reading ? 

 must

 Iranian reading ? 

 most

 Tajik reading ? 

 must

 Noun
 [ edit ] 

 مست • ( must / most ) ( Tajik spelling муст ) 

 distress 

 need 

 complaint 

 Derived terms
 [ edit ] 

 مستمند ( mustmand ) 

 Urdu
 [ edit ]
```


## [2026-09-07T17:51:18.138Z] AGENT

Now I have all the evidence. Let me save the auxiliary audit files and write the verification JSON.


## [2026-09-07T17:51:28.924Z] TOOL CALL #91: Bash

```json
{
 "command": "mkdir -p data/verification/sources/refs/ocr/BOOK data/verification/sources/refs/ocr/FFD && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg341.png data/verification/sources/refs/ocr/BOOK/341.png && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/ffd82.png data/verification/sources/refs/ocr/FFD/77.png && cat > data/verification/sources/refs/ocr/FFD/77.vision.txt <<'EOF'\n[Abolghasemi, Māde-hā-ye fe'l-hā-ye fārsi-ye dari (FFD), printed p. 77 = pdf page 82 —\nread from the page image, 2026-09-07. Header: «ماده‌های ماضی و مضارع فارسی دری ۷۷»]\n\nمُشتن\nمُشت ← فارسی میانه mušt ← ایرانی باستان *mr̥š-ta. برای ta ← آراست. mr̥z صورت اصلی\nmr̥š است، z پیش از t به š بدل شده است. mr̥z صورت ضعیف ریشهٔ marz به معنی «مالیدن» است.\nمال ← فارسی میانه māl ← فارسی باستان *mard-a ← ایرانی باستان *marz-a. برای a ← آرای.\n\nموییدن\n«مویید» مادهٔ ماضی جعلی است، از مادهٔ مضارع ساخته شده است.\nموی ← فارسی میانه mōy ← ایرانی باستان *maud-a. برای a ← آرای.\nریشهٔ maud به معنی «نالیدن» است.\n\nنازیدن\n«نازید» مادهٔ ماضی جعلی است، از مادهٔ مضارع ساخته شده است.\nناز ← فارسی میانه nāz ← ایرانی باستان *nāz. nāz در ایرانی باستان اسم است به معنی\n«شادی»، «افتخار». nāz در فارسی میانه «شاد بودن»، «مفتخر بودن» معنی می‌دهد.\n\nنالیدن\n«نالید» مادهٔ ماضی جعلی است، از مادهٔ مضارع ساخته شده است.\nنال ← فارسی میانه nāl ← ایرانی باستان *nard-a. برای a ← آرای. ریشهٔ nard به معنی\n«بانگ کردن» است.\nEOF\nls -la data/verification/sources/refs/ocr/FFD data/verification/sources/refs/ocr/BOOK/341.png"
}
```


### [2026-09-07T17:51:30.287Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 64116 Sep  7 13:51 data/verification/sources/refs/ocr/BOOK/341.png

data/verification/sources/refs/ocr/FFD:
total 72
drwxrwxr-x  2 sfmqrb sfmqrb  4096 Sep  7 13:51 .
drwxrwxr-x 13 sfmqrb sfmqrb  4096 Sep  7 13:51 ..
-rw-rw-r--  1 sfmqrb sfmqrb 61328 Sep  7 13:51 77.png
-rw-rw-r--  1 sfmqrb sfmqrb  1587 Sep  7 13:51 77.vision.txt
```


## [2026-09-07T17:57:59.333Z] TOOL CALL #92: Write

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/mk341.py",
 "content": "# -*- coding: utf-8 -*-\nimport json, io\n\nW_MUR = \"https://en.wiktionary.org/wiki/%D9%85%D9%88%D8%B1\"\nW_MURYANE = \"https://en.wiktionary.org/wiki/%D9%85%D9%88%D8%B1%DB%8C%D8%A7%D9%86%D9%87\"\nW_FORMICA = \"https://en.wiktionary.org/wiki/formica#Latin\"\nW_PIE = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/morw%C3%ADs\"\nE_FORMIC = \"https://www.etymonline.com/word/formic\"\nE_CHLORO = \"https://www.etymonline.com/word/chloroform\"\nW_MOST = \"https://en.wiktionary.org/wiki/%D9%85%D8%B3%D8%AA\"\nW_MOSTMAND = \"https://en.wiktionary.org/wiki/%D9%85%D8%B3%D8%AA%D9%85%D9%86%D8%AF\"\n\nentry4 = {\n \"entry\": 4,\n \"root\": \"Morwi, Morui\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *morwi- / *morwís 'ant' (Pokorny 749 morui-; Watkins/AHD morwi-), with the taboo-distorted byforms *morm-, *worm-, *mouro-/*meur-\",\n \"note\": \"Pokorny IEW 749 has the root under exactly Nourai's two spellings: 'Root / lemma: morui- … Meaning: ant', with the explicit remark 'distorted taboo uormo-, mormo-, mouro-', and its first material is 'Avestan maoiri (secondary m. maurvay-), sogd. ʼmʼwrc f., npers. mor \\\"ant\\\"'. Walde-Pokorny II 306 f. is the same entry ('mornO-/uormo-/mormo-/mouro- … „Ameise“. Auf morui- sind zurückführbar av. maoiri-s …, np. mōr „Ameise“'), and Watkins/AHD prints 'morwi-. Ant. … Variant form *morm- in … (with dissimilation) Latin formica, ant: FORMIC, FORMICARY … [Pok. morui- 749]'. Language label (Indo-European), root shape and gloss 'ant' are all correct, and POK:749 is the right page. The chart's only substantive flaw is the Latin box, which prints the reconstructed *vormīca as if it were a Latin word (node #4). The two Persian boxes are a nice doublet: the inherited مور and the French-mediated chemical words اسید فرمیک/کلروفرم both go back to this one PIE ant word.\",\n \"note_fa\": \"ریشهٔ هندواروپایی آغازین *morwi- / *morwís به معنی «مور، مورچه» است. پوکورنی (ص ۷۴۹) همین ریشه را با دو صورت morui-/morwi- آورده و یادآور شده که این نام در زبان‌های دختر دچار «دگرگونی تابویی» شده و صورت‌های *uormo-، *mormo- و *mouro- از آن پیدا آمده است؛ نخستین گواه‌های او نیز اوستایی maoiri-، سغدی ʼmʼwrc و فارسی نو «مور» است. والده-پوکورنی (جلد ۲ ص ۳۰۶) و واتکینز در پیوست ریشه‌های هندواروپایی فرهنگ American Heritage همین را می‌گویند و واتکینز افزوده که formica لاتینی با ناهمگونی (dissimilation) از صورت *morm- برآمده است. بنابراین برچسب زبانی، صورت ریشه و معنای «مور» در نمودار نورایی درست است و ارجاع POK:749 نیز دقیق. تنها ایراد این نمودار در خانهٔ لاتینی است که صورت بازسازیِ *vormīca را چون واژه‌ای لاتینی نشان داده است. نکتهٔ دلپذیر این صفحه آن است که «مور» ارثی و «اسید فرمیک/کلروفرم» وام‌گرفته از فرانسوی، هر دو از یک ریشهٔ هندواروپایی‌اند (دوگانه/doublet).\",\n \"sources\": [W_PIE, W_MUR, W_MURYANE],\n \"ref_check\": [\n   {\"ref\": \"POK:749\", \"status\": \"supports\",\n    \"note\": \"POK_full.txt line 61370 ff.: 'Root / lemma: moruT- [= morui-] / Meaning: ant / Note: distorted taboo uormo-, mormo-, mouro- … Material: attributable to mo/yT-are [morui-]. Avestan maoiri (secondary m. maurvay-), sogd. ʼmʼwrc f., npers. mor \\\"ant\\\" … In morm-: Latin formica … References: WP. II 306 f., WH. I 531 f. Page(s): 749'. Exactly the root, the gloss and the branches Nourai draws.\"}\n ],\n \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Bd. II 306 f. (incoming/WLD/WLD_Bd2_pages.txt line 20251 ff.)\", \"stance\": \"supports\",\n    \"note\": \"'mornO- (und fem. -a, -i), uormo-, mormo-, mouro- (germ. auch meuro-) … „Ameise“. Auf morui- sind zurückführbar av. maoiri-s (könnte auch *mouri- sein), np. mōr „Ameise“ … Auf morm-: lat. formica … Auf vorm- gr. βύρμαξ, ϝορμαί Hes.; ai. valmīka- m. „Ameisenhaufen“.' Note that the *vorm- variant yields only Greek and Sanskrit forms — never a Latin word.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins, s.v. morwi- (AHD_watkins1985.txt line 762)\", \"stance\": \"supports\",\n    \"note\": \"'morwi-. Ant. 1. Germanic variant form *meur- in Danish myre … PISMIRE. 2. Variant form *morm- in: a. Greek murmēx, ant: MYRMECO-; b. (with dissimilation) Latin formica, ant: FORMIC, FORMICARY; FORMICIVOROUS. [Pok. morui- 749.]' — the reference Nourai cites for his Latin and English boxes.\"},\n   {\"src\": \"IEC\", \"where\": \"pp. 817–818 s.v. mūr- (1) 'swarm; ant' (IEC.txt line 11411)\", \"stance\": \"supports\",\n    \"note\": \"Mann: 'mūr- (murouis, muràuis, muruis, ios, meur, mour-) (1) \\\"swarm; ant\\\". Cf. WP II, 306 & 312 … Per. mūr, dim. mūrče \\\"ant\\\"; (*-eu- or *-ou- in) Av. maoiris, m. id.; Kurd. mērū; Beluchi mūrī; Hind. mor (fr. Per.); cf. Per. mūriāne \\\"white ant\\\" …' — covers the whole Iranian branch of the chart including موریانه.\"},\n   {\"src\": \"SYN\", \"where\": \"grep 'formica', 'ant' in SYN.txt\", \"stance\": \"silent\",\n    \"note\": \"Buck's synonym dictionary as OCRed here returns no hit for formica/ant in the relevant section; nothing to add.\"}\n ],\n \"nodes\": []\n}\n\nentry4[\"nodes\"] = [\n {\n  \"id\": 1, \"lang\": \"Avestan\", \"words\": \"maoirî\", \"verdict\": \"confirmed\",\n  \"derivation\": \"Avestan maoiri- m. 'ant' continues PIE *morwís through Proto-Indo-Iranian *marwíš: the cluster *-rw- was resolved by vocalising *w to u̯, giving the diphthong written ao (*marwiš > *maurī̆š), and Avestan then inserted its regular epenthetic -i- before the following -i- (maur- > maoir-), whence maoiri-. Bartholomae lemmatises the word as maurvay- m. 'Ameise' (a daēvic creature of which two kinds are distinguished) and cites the attested forms maoirīm, maoirinąm from Vd. 14.5, 16.12, 18.73; the ant appears there with the epithets dānō.karš- 'dragging (grain) kernels' and araēka-. Pokorny 749 quotes the same Avestan maoiri (with secondary maurvay-) beside Sogdian ʼmʼwrc and NP mōr, so the root→Avestan edge is exactly as drawn.\",\n  \"derivation_fa\": \"اوستایی maoiri- «مور» بازماندهٔ *morwís هندواروپایی است که از راه هندوایرانی آغازین *marwíš به اوستایی رسیده: خوشهٔ *-rw- با واکه‌ای‌شدن w به دوگانه‌واکهٔ au (در خط اوستایی ao) بدل شده (*marwiš > *maurī̆š) و سپس «ی» میانجی (epenthesis) که ویژگی اوستایی است پیش از i بعدی افزوده شده و maoir- پدید آمده است. بارتولومه این واژه را زیر maurvay- «مور» آورده و صورت‌های گواه‌شدهٔ maoirīm و maoirinąm را از وندیداد ۱۴٫۵، ۱۶٫۱۲ و ۱۸٫۷۳ نقل کرده است؛ در آن بندها مور جانوری اهریمنی (دیوآفریده) شمرده شده و صفت dānō.karš- «دانه‌کش» دارد. پوکورنی نیز در ص ۷۴۹ همین maoiri را در کنار سغدی ʼmʼwrc و فارسی mōr نقل می‌کند. پس ادعای نورایی درست است.\",\n  \"sources\": [W_PIE],\n  \"ref_check\": [\n    {\"ref\": \"POK:749\", \"status\": \"supports\",\n     \"note\": \"POK_full.txt line 61378: 'Avestan maoiri (secondary m. maurvay-), sogd. ʼmʼwrc f., npers. mor \\\"ant\\\"' — the Avestan form and its Iranian continuation in one line.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"BRT\", \"where\": \"cols. 1152 f. s.v. maurvay- (BRT.txt line 20075); also s.v. araēka- and dānō.karš- (lines 5285, 13402)\", \"stance\": \"supports\",\n     \"note\": \"'j. maurvay- m. \\\"Ameise\\\", ein daēvisches Tier, von dem zwei Arten geschieden werden: … maoirim dānō.karšim … V.16.12; hazaŋrəm maoirinąm dānō.karšanąm V.14.51; … maoirinąm araēkanąm kutakanąm V.14.5.' Bartholomae's footnote adds that the Avestan zoologists took the pupae ants carry into the sun for stolen grain kernels.\"},\n    {\"src\": \"WLD\", \"where\": \"Bd. II 306\", \"stance\": \"supports\",\n     \"note\": \"'Auf morui- sind zurückführbar av. maoiri-s (könnte auch *mouri- sein), np. mōr „Ameise“' — same edge, with the caveat that the Avestan vocalism could also reflect *mouri-.\"},\n    {\"src\": \"HRN\", \"where\": \"no. 993, printed pp. 222–223\", \"stance\": \"supports\",\n     \"note\": \"'993. mōr \\\"Ameise\\\", mūrče; … aw. maoiri- \\\"Ameise\\\"; phlv. mōr.' Horn draws exactly the Avestan → Pahlavi → NP chain of this entry.\"},\n    {\"src\": \"AHD\", \"where\": \"s.v. morwi-\", \"stance\": \"silent\",\n     \"note\": \"Watkins lists only the Germanic, Greek and Latin reflexes; no Iranian material, so it neither supports nor contradicts the Avestan box.\"}\n  ]\n },\n {\n  \"id\": 2, \"lang\": \"Pahlavi\", \"words\": \"môr, môrčag\", \"verdict\": \"confirmed\",\n  \"derivation\": \"Middle Persian mōr [written mwl] 'ant' is the regular continuation of Old Iranian *mauri-/Av. maoiri-: the final syllable was lost and the diphthong *au monophthongised to ō (*maurī > mōr), the ordinary MP development. mōrčag is mōr plus the MP diminutive suffix -čag (> NP -če), i.e. 'little ant', the direct ancestor of NP مورچه mūrče. Both forms are textually attested in Book Pahlavi: Tavoosi's glossary of Šāyast nē Šāyast registers mōr (248/4), mōr āšyānag 'ant's nest' (248/8) and mōrcag (248/10), and MacKenzie's Concise Pahlavi Dictionary has 'mōr [mwl] ant'. Mo'in's etymological footnote to Borhan-e Qate' p. 2049 gives 'پهلوی mōr' under مور and 'پهلوی mōrcak «تاوادیا ۱۶۳»' under مورچه — precisely the pair Nourai prints.\",\n  \"derivation_fa\": \"فارسی میانهٔ mōr (به خط پهلوی mwl) «مور» دنبالهٔ قاعده‌مند ایرانی باستان *mauri-/اوستایی maoiri- است: هجای پایانی افتاده و دوگانه‌واکهٔ *au در فارسی میانه به ō تک‌واکه شده است (*maurī > mōr). صورت mōrčag همان mōr با پسوند تصغیر فارسی میانهٔ -čag (که در فارسی نو -چه شده) است، یعنی «مورِ کوچک»، و نیای مستقیم «مورچه» است. هر دو صورت در متون پهلوی گواه دارند: در واژه‌نامهٔ شایست نه شایست (طاوسی) mōr (۲۴۸/۴)، mōr āšyānag «آشیانهٔ مور» (۲۴۸/۸) و mōrcag (۲۴۸/۱۰) آمده است، و مکنزی هم «mōr [mwl] ant» را ثبت کرده. معین نیز در حاشیهٔ برهان قاطع (ص ۲۰۴۹) زیر «مور» نوشته «پهلوی mōr» و زیر «مورچه» «پهلوی mōrcak «تاوادیا ۱۶۳»» — همان دو صورتی که نورایی آورده است. ادعای نورایی درست است.\",\n  \"sources\": [W_MUR],\n  \"ref_check\": [\n    {\"ref\": \"BQT:2049\", \"status\": \"supports\",\n     \"note\": \"Read from the page image (saved as data/verification/sources/refs/ocr/BQT/2049.png and 2049.vision.txt). Mo'in's footnote 2 to مور: 'اوستا maoiri- ( مور )، پهلوی mōr، … بلوچی mōr، mōrîk (مور) … «اسـتق ۹۹۳»' (the last is a reference to Horn's Grundriss no. 993); footnote 6 to مورچه: 'از: مور (ه.م.) + چه ( پسوند تصغیر ) … پهلوی mōrcak «تاوادیا ۱۶۳»'.\"},\n    {\"ref\": \"SNS:248\", \"status\": \"supports\",\n     \"note\": \"Tavoosi's index (SNS_pages.txt line 16016) lists 'mōr 248/4 … mōr āšyānag 248/8 … mōrcag 248/10', i.e. both of Nourai's Pahlavi forms occur on the cited page 248 of the glossary. (The Persian-script body of that page is unreadable in this OCR; the Latin index entries are clear.)\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"PHD\", \"where\": \"MacKenzie, CPD s.v. mōr (PHD_mackenzie.txt line 3584)\", \"stance\": \"supports\",\n     \"note\": \"'mor [mwl | N -] ant.' — the Pahlavi spelling mwl with New Persian identical (mūr). MacKenzie's English index has 'ant mōr' (cited by Aryanpur as MACKENZIE (ANT) 102).\"},\n    {\"src\": \"ARY\", \"where\": \"Aryanpur, pdf p. 480 (printed 481), entry for مور\", \"stance\": \"supports\",\n     \"note\": \"The entry lists 'MAOIRI- (AVESTAN) … MOR, MORCAK (PAHLAVI) … MURI (KURDISH), MOR, MORIK (BALUCHI), MWRCH (SOGHDIAN), VAMRI, VALMIKA (SANSKRIT), MURCHIUN (ARMENIAN), WORMIKAS, MURMEX (GREEK), -MICA (FORMICA) (LATIN), FOURMI (FRENCH)…' with references to Pokorny, MacKenzie (ANT) 102 and Skeat (PISMIRE) 454 — an independent modern chart identical to Nourai's, including the Pahlavi pair mōr/mōrčag.\"},\n    {\"src\": \"NYB\", \"where\": \"grep 'mōr', 'mwl' in NYB_vol2_glossary.txt\", \"stance\": \"silent\",\n     \"note\": \"Nyberg's Šāyast/Pahlavi glossary does not carry the ant word; no hit.\"},\n    {\"src\": \"HRN\", \"where\": \"no. 993, printed p. 223\", \"stance\": \"supports\",\n     \"note\": \"'phlv. mōr' under NP mōr, with 'mūrče' as the New Persian diminutive.\"}\n  ]\n },\n {\n  \"id\": 3, \"lang\": \"Persian\", \"words\": \"mŭr «مور»\", \"verdict\": \"confirmed\",\n  \"derivation\": \"NP مور mūr 'ant' is MP mōr with the regular New Persian raising of Middle Persian ō to ū (mōr > mūr, still written مور; Horn no. 993 records the older mōr and the dialect diminutive mōrīk in Baluchi/Afghan). مورچه mūrče = MP mōrčag with the ordinary loss of final -g/-k (mōrčag > mūrče), and it is now the everyday word for 'ant', مور being the literary/poetic form. موریانه mūryāne 'termite, white ant' is مور + the suffix -yāne, beside Borhan's variants مورانه/مورجانه/مورچانه — Mann (IEC 817 f.) lists it as 'Per. mūriāne \\\"white ant\\\"' in the same entry as mūr/mūrče. Mo'in's footnotes to Borhan p. 2049 give the whole chain (Avestan maoiri- > Pahlavi mōr > مور; مورچه = مور + -چه) and Wiktionary derives Persian مور 'from Middle Persian mwl /mōr/, from Proto-Indo-Iranian *marwíš', موریانه being 'derived from the word مور'.\",\n  \"derivation_fa\": \"«مور» فارسی نو همان mōr فارسی میانه است با تحول قاعده‌مندِ ō فارسی میانه به ū در فارسی نو (mōr > mūr، هنوز به خط «مور»)؛ هرن (شمارهٔ ۹۹۳) صورت کهن‌ترِ mōr و مصغّر گویشی mōrīk (بلوچی و افغانی) را ثبت کرده است. «مورچه» همان mōrčag پهلوی است با افتادن -g/-k پایانی، و امروز واژهٔ رایج است و «مور» صورت ادبی. «موریانه» از «مور» + پسوند -یانه ساخته شده و در برهان قاطع صورت‌های «مورانه، مورجانه، مورچانه» نیز آمده است؛ مان (فرهنگ مقایسه‌ای هندواروپایی، ص ۸۱۷ به بعد) آن را در همان مدخل «mūr, mūrče» با معنی «مور سفید» آورده. معین در حواشی برهان (ص ۲۰۴۹) همین زنجیره را می‌دهد و ویکی‌واژه هم «مور» را از فارسی میانهٔ mōr و آن را از هندوایرانی آغازین *marwíš می‌داند. ادعای نورایی درست است.\",\n  \"sources\": [W_MUR, W_MURYANE],\n  \"ref_check\": [\n    {\"ref\": \"BQT:2049\", \"status\": \"supports\",\n     \"note\": \"Borhan-e Qate' p. 2049 (image read; vision text saved) has the headwords مور ('معروف است که از جملهٔ حشرات‌الارض باشد … و مورچه مصغر آنست') and مورچه ('مصغر مور است همچنانکه باغچه مصغر باغ - و موریانه را نیز گویند'), with Mo'in's footnotes 2 and 6 giving Avestan maoiri-, Pahlavi mōr and mōrcak. This one page carries everything in Nourai's Persian box, موریانه included.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"HRN\", \"where\": \"no. 993, printed pp. 222–223\", \"stance\": \"supports\",\n     \"note\": \"'993. mōr \\\"Ameise\\\", mūrče; g. mōirik \\\"schwarze Ameise\\\"; … aw. maoiri- \\\"Ameise\\\"; phlv. mōr. LW.(?) kurd. mūrī, merū …; afγ. bei. mōr, n. mōrīk \\\"Ameise\\\"' — and Horn's separate note that Ossetic muljug/mäljig stands apart in Iranian.\"},\n    {\"src\": \"IEC\", \"where\": \"pp. 817–818 s.v. mūr- (1)\", \"stance\": \"supports\",\n     \"note\": \"'Per. mūr, dim. mūrče \\\"ant\\\" … cf. Per. mūriāne \\\"white ant\\\"' — independent confirmation of both extras (مورچه، موریانه).\"},\n    {\"src\": \"ARY\", \"where\": \"pdf p. 480 (printed 481)\", \"stance\": \"supports\",\n     \"note\": \"Aryanpur's Persian headword مور with Avestan maoiri-, Pahlavi mōr/mōrcak and the full IE cognate set.\"},\n    {\"src\": \"MON\", \"where\": \"grep مور/مورچه in MON_part1/2.txt\", \"stance\": \"silent\",\n     \"note\": \"Mo'in's Farhang is quoted here only through his Borhan footnotes; the OCR of the Farhang volumes gives no clean مور headword (the string مور is swamped by مورد).\"}\n  ]\n },\n {\n  \"id\": 4, \"lang\": \"Latin\", \"words\": \"vormîca, formica\", \"verdict\": \"plausible\",\n  \"derivation\": \"The edge itself is right, but one of the two forms is not a Latin word. Latin formīca 'ant' goes back to the *morm- byform of the root (Proto-Italic *mormīkā), with dissimilation of m…m to f…m: Pokorny 749 'In morm-: Latin formica (compare phonetically Latin formīdō : Gk. μορμώ)'; Walde-Pokorny II 306 'Auf morm-: lat. formica (vgl. zum lautlichen formido; μορμώ)'; Ernout-Meillet s.v. formica 'le lat. formica doit résulter d'une dissimilation de *mormi-'; Wiktionary, with a citation, 'Traditionally, from a form with earlier initial /m/, such as Proto-Italic *mormīkā … The irregular sound change can be explained by dissimilation of /m…m/ to /f…m/'. 'vormîca', by contrast, is unattested: it is Klein's reconstructed pre-form, printed s.v. formic as 'fr. L. formica, \\\"ant\\\", dissimilated fr. *mor-mica, fr. orig. *vormica' (Klein 1966, p. 613), i.e. Pokorny's/Walde's *u̯orm- variant, whose only real reflexes are Greek βύρμαξ/ϝορμαί (Hesychius) and Sanskrit valmīka- 'anthill'. The printed page (book p. 311, PDF 341, image saved) does show 'vormîca, formica : ant' inside a box labelled Latin, so the extraction is faithful; the mistake is Nourai's — an asterisked reconstruction promoted to a Latin headword with the asterisk dropped. Hence 'plausible' rather than 'confirmed': the derivation root → Latin formīca is correct, the form vormīca is not Latin.\",\n  \"derivation_fa\": \"خودِ پیوند درست است، اما یکی از دو صورتِ این خانه واژهٔ لاتینی نیست. formīca لاتینی «مور» از صورت دگرگون‌شدهٔ *morm- ریشه برآمده است (ایتالیکِ آغازین *mormīkā) و f آغازین آن نتیجهٔ ناهمگونی (dissimilation) m…m به f…m است: پوکورنی ص ۷۴۹ («In morm-: lat. formica»، با مقایسهٔ formīdō لاتینی در برابر μορμώ یونانی)، والده-پوکورنی جلد ۲ ص ۳۰۶، و ارنو-مه‌یه زیر formica («le lat. formica doit résulter d'une dissimilation de *mormi-»)؛ ویکی‌واژه هم همین را با ارجاع آورده است. اما «vormîca» گواه‌شده نیست: این صورتِ بازساخته را کلاین زیر formic چنین چاپ کرده: «fr. L. formica … dissimilated fr. *mor-mica, fr. orig. *vormica» (کلاین ۱۹۶۶، ص ۶۱۳)، یعنی همان گونهٔ *u̯orm- پوکورنی که تنها بازمانده‌هایش βύρμαξ/ϝορμαί یونانی و valmīka- سنسکریت («مورتپه») است. تصویر صفحهٔ چاپی (ص ۳۱۱ کتاب) نشان می‌دهد که «vormîca, formica : ant» در خانهٔ «Latin» چاپ شده است، پس خطای خوانش اسکن نیست؛ خطا از نویسنده است که صورت ستاره‌دار بازساخته را بی‌ستاره در جایگاه واژهٔ لاتینی نشانده است. از این رو حکم «با احتیاط پذیرفتنی» است.\",\n  \"sources\": [W_FORMICA],\n  \"ref_check\": [\n    {\"ref\": \"AHD\", \"status\": \"supports\",\n     \"note\": \"Watkins s.v. morwi-: 'Variant form *morm- in … b. (with dissimilation) Latin formica, ant: FORMIC, FORMICARY; FORMICIVOROUS.' The reference Nourai cites supports formīca — and gives no *vormica.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"printed p. 613 s.v. formic (KLN_1966.txt line 15195)\", \"stance\": \"partial\",\n     \"note\": \"'formic … Contraction of *formic-ic, fr. L. formica, \\\"ant\\\", dissimilated fr. *mor-mica, fr. orig. *vormica; cogn. with OI. vamrī-, valmī́kaḥ \\\"anthill\\\", Avestic maoiri-, Arm. mrjiun, Gk. μύρμηξ, OSlav. mraviji, OIr. moirb, W. myrion, ON. maurr.' This is evidently Nourai's source for 'vormîca' — but Klein prints it with an asterisk as a reconstruction, not as Latin.\"},\n    {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. formica (LAT.txt lines 23620–23630)\", \"stance\": \"supports\",\n     \"note\": \"'formica (furmīca app. Prob.), -ae f.: fourmi. Ancien … cf. μύρμηξ … Le lat. formica doit résulter d'une dissimilation de *mormi- …' — dissimilation from *morm-, no *vorm- in Latin.\"},\n    {\"src\": \"WLD\", \"where\": \"Bd. II 306 f.\", \"stance\": \"supports\",\n     \"note\": \"'Auf morm-: lat. formica … Auf vorm- gr. βύρμαξ, ϝορμαί Hes.; ai. valmīka- „Ameisenhaufen“' — the *vorm- grade is explicitly Greek/Indic only.\"},\n    {\"src\": \"LEW\", \"where\": \"grep 'formica' in LEW_1910.txt\", \"stance\": \"silent\",\n     \"note\": \"The Walde 1910 OCR on disk returns no hit for formica (the f- fascicle is missing/garbled); Walde-Hofmann I 531 f. is cited at second hand by Pokorny and by Klein (Hofmann in Walde-Hofmann LEW I p. 530).\"}\n  ]\n },\n {\n  \"id\": 5, \"lang\": \"French\", \"words\": \"\", \"verdict\": \"confirmed\",\n  \"derivation\": \"Empty pass-through box for the French stage between Latin and the Persian loans. Latin formīca gave popular Old French fourmi(e) (Fr. fourmi 'ant'), but the words that matter here are the learned chemical coinages: French formique, coined in 1791 for acide formique 'formic acid' — the acid had first been obtained in fairly pure form in 1749 by A. S. Marggraf by distilling red ants — and chloroforme, a hybrid coined in 1834 by the chemist Jean-Baptiste Dumas from chloro- (chlorine) + formique, so named because the substance yields potassium chloride and formic acid. These two French words are the immediate donors of both the Persian box below and the English box.\",\n  \"derivation_fa\": \"این خانهٔ خالی مرحلهٔ فرانسوی میان لاتین و وام‌واژه‌های فارسی است. formīca لاتینی در فرانسوی به fourmi «مور» رسیده، اما آنچه در این نمودار به کار می‌آید دو ساختهٔ علمی است: formique که در ۱۷۹۱ برای acide formique «اسید فرمیک» ساخته شد (این اسید را نخست در ۱۷۴۹ مارگراف از تقطیر مورچهٔ سرخ به دست آورد)، و chloroforme که در ۱۸۳۴ ژان-باتیست دوما، شیمی‌دان فرانسوی، از chloro- «کلر» + formique ساخت، زیرا این ماده کلرید پتاسیم و اسید فرمیک می‌دهد. همین دو واژهٔ فرانسوی سرچشمهٔ بی‌واسطهٔ واژه‌های فارسی و انگلیسی این نمودارند. گره گذری است و اشکالی ندارد.\",\n  \"sources\": [E_FORMIC, E_CHLORO],\n  \"ref_check\": [\n    {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Nourai gives no reference for this pass-through box.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"printed p. 291 s.v. chloroform (KLN_1966.txt line 7479); p. 613 s.v. formic\", \"stance\": \"supports\",\n     \"note\": \"'chloroform … F. chloroforme, a hybrid coined by Jean-Baptiste Dumas (1800-84) in 1834 fr. chloro- and F. formique, \\\"formic\\\" (fr. L. formica, \\\"ant\\\", see formic); so called by him in allusion to its capacity of forming potassium chloride and formic acid.'\"},\n    {\"src\": \"SKT\", \"where\": \"s.v. Chloroform (SKT.txt line 3411)\", \"stance\": \"supports\",\n     \"note\": \"'chloroform. (L. and Gk.) The latter element relates to formic acid, an acid formerly obtained from red ants. — L. formica, an ant.'\"}\n  ]\n },\n {\n  \"id\": 6, \"lang\": \"Persian\", \"words\": \"\", \"verdict\": \"confirmed\",\n  \"derivation\": \"The box holds two modern Persian scientific loans from French: کلروفرم kloroform < Fr. chloroforme, and اسید فرمیک asid-e formik < Fr. acide formique (Persian keeps the French adjective فرمیک and prefixes the noun اسید, so the order is reversed relative to French). Mo'in's Farhang, the reference Nourai cites (MON), lists 'کلروفرم: (chloroforme) (فر.، شیمی)' — explicitly tagged فر. 'French' — and the word turns up throughout Mo'in's technical entries ('در اتر و کلروفرم و اسانس تربانتین'). Both words are 20th-century additions to Persian through French-language chemistry and medicine, and they descend, via Latin formīca, from the same PIE ant word as the inherited مور of node #3.\",\n  \"derivation_fa\": \"این خانه دو وام‌واژهٔ علمی نو فارسی از فرانسوی است: «کلروفرم» از chloroforme فرانسوی و «اسید فرمیک» از acide formique فرانسوی (فارسی صفت فرمیک را نگه داشته و «اسید» را پیش آورده، پس ترتیب واژه‌ها برعکس فرانسوی است). معین در فرهنگ فارسی — همان مرجعی که نورایی ارجاع داده — می‌آورد: «کلروفرم: (chloroforme) (فر.، شیمی)»، یعنی صریحاً آن را فرانسوی می‌داند، و این واژه در مدخل‌های فنی او پرکاربرد است («در اتر و کلروفرم و اسانس تربانتین»). این دو واژه در سدهٔ بیستم از راه شیمی و پزشکی فرانسوی‌زبان به فارسی آمده‌اند و از راه formīca لاتینی به همان ریشهٔ هندواروپاییِ «مور» می‌رسند؛ پس «کلروفرم» و «مور» دوگانهٔ (doublet) یک ریشه‌اند. ادعای نورایی درست است.\",\n  \"sources\": [E_CHLORO],\n  \"ref_check\": [\n    {\"ref\": \"MON\", \"status\": \"supports\",\n     \"note\": \"MON_part2.txt line 25084: 'کلروفرم: (chloroforme) (فر. شیمی)' — Mo'in marks it a French chemistry term. (Nourai gives no page for MON here; the OCR of the Farhang carries no pagination, so only the entry itself could be checked.) اسید فرمیک is not retrievable from this OCR.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"MON\", \"where\": \"MON_part2.txt lines 25084, 58763, 84052, 93802\", \"stance\": \"supports\",\n     \"note\": \"کلروفرم appears both as a headword with the French etymon and inside pharmacological definitions; no competing (e.g. Arabic or English) source is suggested.\"},\n    {\"src\": \"KLN\", \"where\": \"printed p. 291 s.v. chloroform\", \"stance\": \"supports\",\n     \"note\": \"Confirms the French chloroforme (Dumas 1834) that Persian borrowed, and its formica base.\"}\n  ]\n },\n {\n  \"id\": 7, \"lang\": \"English\", \"words\": \"formic [acid]; chloroform\", \"verdict\": \"confirmed\",\n  \"derivation\": \"English formic (adj.) is first recorded 1791 in formic acid, 'literally \\\"from ants\\\"', from Latin formīca 'ant' (via French formique); chloroform is 1835, from French chloroforme (Dumas's 1834 coinage). Watkins/AHD — the reference Nourai cites — puts FORMIC, FORMICARY and FORMICIVOROUS under morwi- (and PISMIRE under the Germanic *meur- variant), so the English box hangs from the Latin box exactly as drawn; Klein p. 613 and Skeat s.v. Formic/Chloroform give the same chain. Note that English mire in pismire is the inherited Germanic member of the family (< Danish/ON myre), not a Latin borrowing — Nourai does not claim otherwise.\",\n  \"derivation_fa\": \"صفت انگلیسی formic نخست در ۱۷۹۱ در ترکیب formic acid گواه شده است، به معنی تحت‌اللفظی «مورچه‌ای»، از formīca لاتینی و از راه formique فرانسوی؛ chloroform نیز در ۱۸۳۵ از chloroforme فرانسوی (ساختهٔ دوما در ۱۸۳۴) به انگلیسی رسیده است. واتکینز در پیوست ریشه‌های هندواروپایی فرهنگ American Heritage — همان مرجعی که نورایی ارجاع داده — واژه‌های FORMIC، FORMICARY و FORMICIVOROUS را زیر ریشهٔ morwi- آورده (و PISMIRE را زیر گونهٔ ژرمنی *meur-)، پس این خانه درست از خانهٔ لاتینی آویخته است؛ کلاین (ص ۶۱۳) و اسکیت هم همین زنجیره را می‌دهند. ادعای نورایی درست است.\",\n  \"sources\": [E_FORMIC, E_CHLORO],\n  \"ref_check\": [\n    {\"ref\": \"AHD\", \"status\": \"supports\",\n     \"note\": \"Watkins, s.v. morwi-: '… Latin formica, ant: FORMIC, FORMICARY; FORMICIVOROUS'; the index confirms 'FORMIC morwi-, FORMICARY morwi-, FORMICIVOROUS morwi-, PISMIRE morwi-, MYRMECO- morwi-'.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"printed p. 613 s.v. formic, formicary; p. 291 s.v. chloroform\", \"stance\": \"supports\",\n     \"note\": \"'formic … fr. L. formica, \\\"ant\\\" …'; 'formicary, an ant's nest. — ML. formicarium, fr. L. formica'; chloroform from F. chloroforme (Dumas 1834).\"},\n    {\"src\": \"SKT\", \"where\": \"s.v. Formic (SKT.txt line 6980) and Chloroform (line 3411)\", \"stance\": \"supports\",\n     \"note\": \"'Formic. pertaining to ants. (L.) L. formica, an ant.'\"},\n    {\"src\": \"FSD\", \"where\": \"grep 'formic' in FSD_vol1-4\", \"stance\": \"silent\",\n     \"note\": \"The Funk & Wagnalls OCR gives no usable hit for the entry; Klein, Skeat, Watkins and Etymonline already cover this uncontroversial chain.\"}\n  ]\n }\n]\n\nentry5 = {\n \"entry\": 5,\n \"root\": \"Moudh, Moudhiô\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *meudʰ- / *maudʰ- / *mudʰ- 'to be intent on, long for, complain, lament' (Pokorny 743; Walde-Pokorny II 255 f.; Mann IEC 802 moudh-, moudhio)\",\n \"note\": \"The page Nourai cites reads verbatim (Mann, IEC 802): 'moudh-, moudhio \\\"ponder, long, mourn, flag, reflect upon\\\". … M Per. cf. mūyah \\\"sadness, lament\\\"; Go. maudjan, v. \\\"remember\\\"; OCS cf. mudŭ \\\"behindhand, sluggish\\\"; Li. maudžiù, maũsti \\\"ache; long, yearn\\\" beside ap-maudùs \\\"glum\\\"' — so both headword shapes and the gloss are Mann's own. Pokorny 743 sets up the same root independently: 'Root/lemma: meudʰ-, maudʰ-, mudʰ- / Meaning: to complain or care about smth. / Material: Npers. mōja \\\"lament\\\" (-i- from -dʰ-, compare:) must \\\"lament\\\" (-st- from -dʰ-st-); gr. μῦθος; Gothic maudjan, ga-maudjan \\\"remind sb\\\"; Lithuanian maudžiu, mausti; Old Bulgarian myslĭ \\\"thought\\\" (*mud-slio-)' — i.e. Nourai's Persian branch is the first material Pokorny lists, and the phonetics of both موییدن and مُست are spelled out there. Walde-Pokorny II 255 f. is the same entry ('meudh-, maudh-, mudh- etwa „worauf bedacht sein, sehnlich, schmerzlich verlangen“; Npers. moja „Klage“ … must „Klage“'). Two caveats: (a) 'to mourn' is a narrowing of the root's real sense ('long for, be intent on, complain'), and (b) Pokorny's neighbouring meu-d- on the same page 743 ('hell, munter, klug', whence Lat. mundus, mustus) is a DIFFERENT root, not to be confused with this one. Aryanpur (printed p. 472) has the same family, with '*MUSTI (OLD PERSIAN), MUST (PAHLAVI), MUTHOS (GREEK), MAUDJAN (GOTHIC), MAUDZHIG/MAUSTI (LITHUANIAN), MYSLU (OLD BULGARIAN)' and a reference to MacKenzie (COMPLAINT) 107.\",\n \"note_fa\": \"صفحه‌ای که نورایی ارجاع داده (مان، فرهنگ مقایسه‌ای هندواروپایی، ص ۸۰۲) عیناً چنین است: «moudh-, moudhio: اندیشیدن، آرزو کردن، سوگواری کردن…؛ فارسی میانه mūyah «اندوه، مویه»؛ گوتی maudjan «به یاد آوردن»؛ اسلاوی کلیسایی کهن mudŭ؛ لیتوانیایی maudžiù, maũsti «درد کشیدن، آرزومند بودن»» — پس هر دو صورت سرواژه و معنای نورایی از مان است. پوکورنی نیز در ص ۷۴۳ همین ریشه را مستقل آورده: «meudʰ-, maudʰ-, mudʰ-: شکایت کردن یا در اندیشهٔ چیزی بودن؛ فارسی نو mōja «شکوه» (که -i- آن از -dʰ- است، بسنجید با:) must «شکوه» (که -st- آن از -dʰ-st- است)؛ یونانی μῦθος؛ گوتی maudjan؛ لیتوانیایی maudžiu…» — یعنی شاخهٔ فارسیِ این نمودار نخستین گواهِ پوکورنی برای این ریشه است و دگرگونی آواییِ «مویه» و «مُست» را همان‌جا توضیح داده است. والده-پوکورنی (جلد ۲ ص ۲۵۵) هم همین است. دو نکتهٔ احتیاطی: نخست آنکه معنای «سوگواری کردن» تنگ‌کردنِ معنای اصلی («آرزومند بودن، شکوه کردن») است؛ دوم آنکه ریشهٔ همسایهٔ meu-d- در همان ص ۷۴۳ («روشن، سرزنده»، مادرِ mundus و mustus لاتینی) ریشهٔ دیگری است و نباید با این یکی درآمیخت. آریان‌پور (ص ۴۷۲ چاپی) همین خانواده را با *musti- (پارسی باستان)، must (پهلوی)، μῦθος یونانی، maudjan گوتی و maudžiu لیتوانیایی آورده است. حکم: ریشه و معنا درست است.\",\n \"sources\": [W_MOST, W_MOSTMAND],\n \"ref_check\": [\n   {\"ref\": \"IEC:802\", \"status\": \"supports\",\n    \"note\": \"IEC.txt line 11221, between the page markers '802' (line 11214) and '803' (line 11225), i.e. exactly Mann's p. 802: 'moudh-, moudhio \\\"ponder, long, mourn, flag, reflect upon\\\". See Supt: M Per. cf. mūyah \\\"sadness, lament\\\"; Go. maudjan, v. \\\"remember\\\" …'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"p. 743 s.v. meudʰ-, maudʰ-, mudʰ- (POK_full.txt line 61113 ff.)\", \"stance\": \"supports\",\n    \"note\": \"'Root / lemma: meudʰ-, maudʰ-, mudʰ- / Meaning: to complain or care about smth. / Material: Npers. moja \\\"lament\\\" (-i- from -dʰ-, compare:) must \\\"lament\\\" (-st- from -dʰst-); gr. μῦθος m. \\\"discourse\\\", μυθέομαι; Gothic maudjan, ga-maudjan \\\"remind sb\\\"; Lithuanian maudziu, mausti; Old Bulgarian myslĭ \\\"thought\\\" (*mud-slio-) … References: WP. II 255 f. Page(s): 743'. Note Nourai cites IEC, not POK, for the root — but Pokorny is the stronger authority and agrees.\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. II 255 f. (incoming/WLD/WLD_Bd2_pages.txt line 16790 ff.)\", \"stance\": \"supports\",\n    \"note\": \"'meudh-, meudh-, mudh- etwa „worauf bedacht sein, sehnlich, schmerzlich verlangen“: Npers. moja „Klage“ (-j- aus -dh-, vgl.:) must „Klage“ (-st- aus -dhst-): got. maudjan, gamaudjan „jmdn erinnern“; lit. maudžiu, mausti „sehnlich verlangen“, apmaudas „Verdruß, Sorge“; abg. myslĭ „Gedanke“ …' Walde adds that the Greek μῦθος connection is 'sehr fraglich'.\"},\n   {\"src\": \"ARY\", \"where\": \"Aryanpur, pdf p. 471 (printed 472)\", \"stance\": \"supports\",\n    \"note\": \"Independent modern Persian chart of the same root: '*MUSTI (OLD PERSIAN), MUST (PAHLAVI), MUTHOS (GREEK), MAUDJAN (GOTHIC), MAUDZHIG, MAUSTI (LITHUANIAN), MYSLU (OLD BULGARIAN)', with references to Pokorny and 'MACKENZIE: (COMPLAINT) 107'.\"},\n   {\"src\": \"CHEUNG\", \"where\": \"Etymological Dictionary of the Iranian Verb, s.v. *maud? 'to mourn' (pp. 270 f.; CHEUNG.txt line 17887 ff.)\", \"stance\": \"partial\",\n    \"note\": \"Cheung accepts the Persian material but doubts the root: 'The Persian forms are isolated within IIr.: they might be connected to the IE correspondences cited by Pokorny: 743 … However, if the Persian forms were from older *maud as assumed generally, they would be identical with the semantically antonymous root *maud \\\"to rejoice\\\" … More likely, we are dealing with the root *nau(H) \\\"to mourn\\\" … which became contaminated with the antonymous root *maud \\\"to rejoice\\\"'.\"}\n ],\n \"nodes\": []\n}\n\nentry5[\"nodes\"] = [\n {\n  \"id\": 1, \"lang\": \"Avestan\", \"words\": \"môy; a-mayavâ\", \"verdict\": \"disputed\",\n  \"derivation\": \"The Avestan label is wrong for the first word and doubtful for the second. There is no Avestan mōy: mōy/mōyag are Middle Persian forms, and Cheung (2007, s.v. *maud?) states flatly that 'the Persian forms are isolated within IIr.' — nothing of this root is attested in Avestan or Old Persian, which is why Nourai's own node #4 has to reconstruct an Old Iranian *maud-. Avestan amayavā- f. does exist, but Bartholomae glosses it 'Leid, Drangsal' (only Y. 71.17, paitištātaē xšayasca amayavayāsca 'to withstand misery and distress'), and Horn — the very page Nourai cites (no. 997, printed pp. 223 f.) — offers it only as a hesitant comparison, 'aw. vergl. amayavā- \\\"Leid\\\"', in the same breath as 'ai. vergl. āmīvā-', i.e. Skt. āmīvā- 'affliction, disease', which belongs to a different root (Nourai's own cross-reference 'See root Ome' points there). Formally amayavā- cannot come from *maudʰ-: it has an initial a- and no dental. Horn then rejects Darmesteter's Avestan/Sanskrit comparanda as phonetically irreconcilable with NP mōye and Bartholomae's Studien II 178 as unsatisfactory, and reports F. Müller's *√maud- with OP *mauda- instead. So the arrow root → Avestan → Pahlavi as drawn is not supportable: the ancestor of MP mōy is a reconstructed Old Iranian *maud-a-, not an Avestan word, and amayavā- is at best a doubtful cognate.\",\n  \"derivation_fa\": \"برچسب «اوستایی» برای واژهٔ نخست نادرست و برای واژهٔ دوم مشکوک است. در اوستایی صورتی به شکل mōy نداریم؛ mōy و mōyag صورت‌های فارسی میانه‌اند و چونگ (۲۰۰۷، زیر *maud?) صریح می‌گوید که «صورت‌های فارسی در هندوایرانی تک‌افتاده‌اند»، یعنی از این ریشه در اوستایی و پارسی باستان چیزی گواه نشده است؛ به همین سبب خودِ نورایی در گرهٔ ۴ ناچار شده صورت ایرانی باستانِ بازساخته *maud- را بیاورد. اوستایی amayavā- (مادینه) وجود دارد، اما بارتولومه آن را «رنج، تنگی» معنی کرده و تنها یک گواه دارد (یسنا ۷۱٫۱۷: paitištātaē xšayasca amayavayāsca «برای ایستادگی در برابر سختی و رنج»)؛ هرن نیز در همان صفحه‌ای که نورایی ارجاع داده (شمارهٔ ۹۹۷) آن را فقط با قید «بسنجید» آورده است: «aw. vergl. amayavā- „Leid“» و در همان جمله «ai. vergl. āmīvā-»، یعنی سنسکریت āmīvā- «رنج، بیماری» که به ریشهٔ دیگری می‌رسد (همان که نورایی خود در یادداشت به «ریشهٔ Ome» ارجاع داده). از نظر آوایی هم amayavā- با a- آغازی و بی هیچ دندانی نمی‌تواند از *maudʰ- بیاید. هرن سپس مقایسه‌های دارمستتر را با «مویه» ناسازگار می‌شمارد و به جای آن *√maud- فریدریش مولر را با پارسی باستان *mauda- گزارش می‌کند. پس پیکانِ ریشه ← اوستایی ← پهلوی چنان‌که کشیده شده پذیرفتنی نیست: نیای mōy فارسی میانه صورت بازساختهٔ ایرانی باستان *maud-a- است، نه واژه‌ای اوستایی. پژوهش امروزی این گره را رد می‌کند.\",\n  \"sources\": [],\n  \"ref_check\": [\n    {\"ref\": \"HRN:224\", \"status\": \"partial\",\n     \"note\": \"Horn no. 997 (HRN.txt lines 8665–8682) reads 'mōye \\\"Weinen, Klage\\\", mōyīden. aw. vergl. amayavā- \\\"Leid\\\"; phlv. mōyak; ai. vergl. āmīvā-.' Horn's Avestan comparison is explicitly tentative ('vergl.'), he gives NO Avestan mōy, and he goes on: 'Die von Darmesteter, Ét. ir. II. 169, verglichenen aw. ai. Worte lassen sich mit np. mōye lautlich nicht vereinigen, und auch Bartholomae, Studien, II, 178, befriedigt nicht … Fr. Müller (WZKM 5, 65) construirt eine *√maud- mit einem ap. *mauda- als Grundform'. So the page supports the Persian/Pahlavi boxes but not an Avestan node.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"BRT\", \"where\": \"cols. 136–138 s.v. amayavā- (BRT.txt line 4693)\", \"stance\": \"partial\",\n     \"note\": \"'j. amayavā- f. \\\"Leid, Drangsal\\\": paitištātaē xšayasca amayavayāsca \\\"um zu widerstehen dem Jammer und Leid\\\" Y.71.17.' The word and the gloss 'grief' are right; Bartholomae offers no etymology linking it to *maudʰ- (he cross-refers to mayava-, and the Avestan lexicon has no mōy).\"},\n    {\"src\": \"CHEUNG\", \"where\": \"s.v. *maud? 'to mourn' (CHEUNG.txt line 17887 ff.)\", \"stance\": \"contradicts\",\n     \"note\": \"'*MIDDLE PERSIAN: MMP mwy- \\\"to mourn\\\", BMP mwst /must/ \\\"mourning\\\" … *NWIR: NP mōyidan … The Persian forms are isolated within IIr.' No Avestan/Old Persian attestation is admitted, and Cheung's preferred solution is contamination of *nau(H) 'to mourn' with *maud 'to rejoice' — the opposite of a straight Avestan ancestor.\"},\n    {\"src\": \"POK\", \"where\": \"p. 743 s.v. meudʰ-\", \"stance\": \"silent\",\n     \"note\": \"Pokorny's material for this root begins with 'Npers. moja … must' and lists no Avestan or Old Persian form at all — again pointing to a Persian-only Iranian branch.\"}\n  ]\n },\n {\n  \"id\": 2, \"lang\": \"Pahlavi\", \"words\": \"môy, môyak; must\", \"verdict\": \"confirmed\",\n  \"derivation\": \"Middle Persian mōy- 'to mourn' (Manichaean MP mwy-, pres. 3pl mwyynd) and its verbal noun mōyag 'lamentation' descend from Old Iranian *maud-a-: post-vocalic *-d- became -y- in Middle Persian, while Book Pahlavi kept the historical spelling with d — MacKenzie prints 'mōyag [mwdk | N mōya] lamentation' and Nyberg 'mōdak [mwdk'] mourning for the dead … MPrs. mwyg \\\"lamenting\\\"'. (The same graph mwd also writes mōy 'hair' (< *mauda- 'hair', Horn no. 996), a homograph that has to be kept apart.) must 'mourning, complaint' is the inherited *-ti- abstract of the same root: *mud-ti- > must, with the regular Iranian d+t > st — Nyberg says so explicitly ('cf. NP must \\\"trouble, lamentation\\\" < *mud-ti-'), Pokorny 743 derives must with '-st- from -dʰ-st-', and Cheung registers 'BMP mwst /must/ \\\"mourning\\\"' as the perfect passive participle of mwy-. It survives in MP mustōmand 'complaining, unhappy' (MacKenzie), NP مستمند. Nourai's Pahlavi box is therefore accurate in every form; only the parent he gives it (the Avestan box) is wrong.\",\n  \"derivation_fa\": \"فارسی میانهٔ mōy- «مویه کردن» (فارسی میانهٔ مانوی mwy-، سوم‌شخص جمع mwyynd) و اسم مصدر آن mōyag «مویه، زاری» از ایرانی باستان *maud-a- آمده‌اند: -d- پس از واکه در فارسی میانه به -y- بدل شده، اما پهلوی کتابی املای تاریخی با d را نگه داشته است — مکنزی می‌نویسد «mōyag [mwdk | N mōya] lamentation» و نیبرگ «mōdak [mwdk'] سوگ برای مرده … فارسی میانه mwyg «مویه‌کنان»». (همان نوشتار mwd صورت mōy «مو، گیسو» را هم می‌نویسد که از *mauda- «مو» است — هرن شمارهٔ ۹۹۶ — و باید از این یکی جدا شود.) must «مویه، شکوه» همان اسم انتزاعیِ *-ti-دار همین ریشه است: *mud-ti- > must با ابدال قاعده‌مندِ d+t به st؛ نیبرگ صریح می‌گوید «قس فارسی نو must «رنج، مویه» < *mud-ti-»، پوکورنی هم -st- را از -dʰ-st- می‌داند و چونگ «BMP mwst /must/» را اسم مفعول mwy- می‌شمارد. این واژه در must-ōmand پهلوی «شکوه‌گر، ناشاد» (مکنزی) و «مستمند» فارسی زنده مانده است. پس همهٔ صورت‌های خانهٔ پهلوی نورایی درست است؛ تنها گرهِ پدرِ آن (خانهٔ اوستایی) نادرست است.\",\n  \"sources\": [W_MOSTMAND],\n  \"ref_check\": [\n    {\"ref\": \"HRN:224\", \"status\": \"supports\",\n     \"note\": \"Horn no. 997: 'phlv. mōyak' for the verbal noun, and, reporting F. Müller, 'dazu auch np. must \\\"Klage\\\", mustmend' — both of Nourai's Pahlavi words on the cited page.\"},\n    {\"ref\": \"FFD:77\", \"status\": \"supports\",\n     \"note\": \"Abolghasemi, Māde-hā-ye fe'l-hā-ye fārsi-ye dari p. 77 (pdf 82; image + vision text saved under refs/ocr/FFD/): 'موییدن — «مویید» مادهٔ ماضی جعلی است … موی ← فارسی میانه mōy ← ایرانی باستان *maud-a. ریشهٔ maud به معنی «نالیدن» است.' The Middle Persian stem mōy is given explicitly.\"},\n    {\"ref\": \"MON\", \"status\": \"not_checked\",\n     \"note\": \"No page is cited for MON on this node and the Farhang's Pahlavi notes cannot be located in the OCR on disk (no pagination); Mo'in's own etymological footnote in Borhan (p. 2058) was checked instead — see node #3.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"PHD\", \"where\": \"MacKenzie, CPD s.v. mōyag, mustōmand (PHD_mackenzie.txt lines 3590, 3624)\", \"stance\": \"supports\",\n     \"note\": \"'moyag [mwdk | N maya] lamentation.'; 'mustomand [mwstwmnd | N mustmand] complaining, unhappy.' (MacKenzie's separate 'must [mwst] fist' is a different word, from *mušti-.)\"},\n    {\"src\": \"NYB\", \"where\": \"A Manual of Pahlavi II (Glossary), p. 132 s.v. mōdak (NYB_vol2_glossary.txt line 2583)\", \"stance\": \"supports\",\n     \"note\": \"'mōdak [mwdk'] mourning for the dead 86²⁰. — Paz. mūyai < mōdakēh … MPrs. mwyg \\\"lamenting\\\" (A-H II). Cf NP must \\\"trouble, lamentation\\\" < *mud-ti-.' Nyberg supplies exactly the -st- < *-d-ti- explanation.\"},\n    {\"src\": \"CHEUNG\", \"where\": \"s.v. *maud? (CHEUNG.txt line 17888 ff.)\", \"stance\": \"supports\",\n     \"note\": \"'MMP mwy- \\\"to mourn\\\", BMP mwst /must/ \\\"mourning\\\" … Pres.: IND. 3pl. MMP mwyynd, SUBJ. 1sg. mwyʾn; Partic.: pres. pl. mwyʾgʾn, perf. pass. BMP mwst /must/' — the Middle Persian paradigm behind both of Nourai's forms.\"}\n  ]\n },\n {\n  \"id\": 3, \"lang\": \"Persian\", \"words\": \"mŭy-îdan «موییدن»; most «مُست ۲»\", \"verdict\": \"confirmed\",\n  \"derivation\": \"NP موییدن mūyīdan 'to weep, lament' is a New Persian denominative on the present stem mūy- (< MP mōy-, with the regular MP ō > NP ū), its past stem mūyīd being secondary; Abolghasemi (FFD p. 77) analyses it in exactly those terms ('«مویید» مادهٔ ماضی جعلی است، از مادهٔ مضارع ساخته شده است. موی ← فارسی میانه mōy ← ایرانی باستان *maud-a'). Beside it stand the nouns مویه mūye 'lamentation, dirge' (Mo'in: 'مویه: گریه و زاری، نوحه'; مویه‌گر 'mourner' = مویه + گر) and the doublets موژ/موژه, which Borhan-e Qate' cross-references with موی/مویه (v. 4, printed pp. 2051 f., 'قس: موی، مویه. و رك: موژه'). مُست must/most 'complaint, grievance, sorrow' is the inherited *mud-ti- abstract (Pokorny 743 cites 'Npers. mōja … must' as the root's first material, deriving -st- from -dʰ-st-), whence مستمند 'wretched, sorrowful' (= مست + ـمند, so Wiktionary), MP mustōmand. Nourai's Vis-o-Rāmin citation (Gorgani, mid-11th c.: من این مُست گران را با که گویم…) is an apt early attestation of the noun. Two caveats: the extra موی is homophonous with موی 'hair' (a distinct word, MP mōd, Horn no. 996), so only the 'lament' sense belongs here; and Mo'in's own footnote to موییدن in Borhan (p. 2058) derives it 'از: موی (مویه) + یدن (پسوند مصدری)' and refers to 'اسـتق ۹۹۷' — i.e. Horn's Grundriss no. 997, the very page Nourai cites.\",\n  \"derivation_fa\": \"«موییدن» فعلی است که در فارسی نو از ستاک حالِ mūy- (از mōy- فارسی میانه، با تحول قاعده‌مندِ ō به ū) ساخته شده و مادهٔ ماضیِ «مویید» آن جعلی و ثانوی است؛ ابوالقاسمی (ماده‌های فعل‌های فارسی دری، ص ۷۷) درست همین را می‌گوید: «مویید» مادهٔ ماضی جعلی است، از مادهٔ مضارع ساخته شده است. موی ← فارسی میانه mōy ← ایرانی باستان *maud-a». در کنار آن اسم‌های «مویه» (معین: «گریه و زاری، نوحه») و «مویه‌گر» (مویه + گر) و دوگانه‌های «موژ/موژه» هست که برهان قاطع آنها را با «موی/مویه» ارجاع متقابل داده است (جلد ۴، ص ۲۰۵۱ و بعد: «قس: موی، مویه. و رك: موژه»). «مُست» به معنی «شکوه، گرانی دل، اندوه» همان اسم *mud-ti- ارثی است (پوکورنی ص ۷۴۳ «فارسی نو mōja … must» را نخستین گواه این ریشه می‌داند و -st- را از -dʰ-st- می‌گیرد) و «مستمند» از «مست + ـمند» ساخته شده است (فارسی میانه mustōmand). بیتی که نورایی از ویس و رامین (فخرالدین اسعد گرگانی، میانهٔ سدهٔ پنجم هجری) آورده گواه کهن خوبی برای این اسم است. دو نکته: «موی» در فهرست این خانه هم‌آوای «موی» به معنی «گیسو» است (واژه‌ای دیگر، فارسی میانه mōd، هرن شمارهٔ ۹۹۶) و تنها معنای «زاری» به این ریشه می‌رسد؛ دیگر آنکه معین در حاشیهٔ «مویدن» در برهان (ص ۲۰۵۸) می‌نویسد «از: موی (مویه) + یدن (پسوند مصدری). رك: اسـتق ۹۹۷» که همان شمارهٔ ۹۹۷ گروندریسِ هرن است — یعنی دقیقاً همان صفحه‌ای که نورایی ارجاع داده. ادعای نورایی درست است.\",\n  \"sources\": [W_MOST, W_MOSTMAND],\n  \"ref_check\": [\n    {\"ref\": \"HRN:224\", \"status\": \"supports\",\n     \"note\": \"Horn no. 997 (pp. 223 f.): 'mōye \\\"Weinen, Klage\\\", mōyīden … dazu auch np. must \\\"Klage\\\", mustmend' — both Persian words of this box are on the cited page.\"},\n    {\"ref\": \"FFD:77\", \"status\": \"supports\",\n     \"note\": \"See the saved image/vision text of FFD p. 77: موییدن with mūy- < MP mōy < OIr *maud-a and 'ریشهٔ maud به معنی «نالیدن» است'.\"},\n    {\"ref\": \"MON:4080,4433,4455\", \"status\": \"partial\",\n     \"note\": \"The entries are in Mo'in's Farhang — MON_part2.txt lines 68887–68895: 'مویه: (mūya) (ا.مص.) گریه و زاری، نوحه … مویه‌گر: (ص.فا.) زاری کننده؛ نوحه کننده … مویید[ن]: [قس. مویه] (مص.ل.) گریه و زاری کردن، نوحه کردن؛ شیون' — but the OCR of the Farhang carries no pagination, so the three cited page numbers themselves could not be verified; مُست was not retrievable from this OCR.\"},\n    {\"ref\": \"IEC:802\", \"status\": \"supports\",\n     \"note\": \"Mann p. 802 s.v. moudh-: 'M Per. cf. mūyah \\\"sadness, lament\\\"' — the Persian noun مویه is the entry's Iranian witness.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"POK\", \"where\": \"p. 743 s.v. meudʰ-, maudʰ-, mudʰ-\", \"stance\": \"supports\",\n     \"note\": \"'Npers. moja \\\"lament\\\" (-i- from -dʰ-, compare:) must \\\"lament\\\" (-st- from -dʰst-)' — Pokorny states the sound changes for both مویه and مُست.\"},\n    {\"src\": \"WLD\", \"where\": \"Bd. II 255\", \"stance\": \"supports\",\n     \"note\": \"'Npers. moja „Klage“ (-j- aus -dh-, vgl.:) must „Klage“ (-st- aus -dhst-)'.\"},\n    {\"src\": \"BQT\", \"where\": \"printed p. 2058 (v. 4 pdf p. 141) s.v. مویدن, مویه‌گر; pp. 2051 f. (pdf 134–135) s.v. موژ/موژه\", \"stance\": \"supports\",\n     \"note\": \"Borhan: 'مویدن … بمعنی گریه و نوحه کردن و گریستن باشد', with Mo'in's footnote 'از: موی (مویه[ه.م.]) + یدن (پسوند مصدری). رك: اسـتق ۹۹۷؛ دارمستتر، تتبعات ج۲ ۱۹۹' and 'از: مویه + گر (پسوند شغل و مبالغه)'; the موژ/موژه pages carry 'قس: موی، مویه. و رك: موژه'.\"},\n    {\"src\": \"MON\", \"where\": \"MON_part2.txt lines 68887–68895\", \"stance\": \"supports\",\n     \"note\": \"مویه، مویه‌گر، مویید[ن] as quoted above; Mo'in cross-references مویید[ن] to مویه, exactly the derivation drawn.\"},\n    {\"src\": \"ARY\", \"where\": \"Aryanpur, pdf p. 471 (printed 472)\", \"stance\": \"supports\",\n     \"note\": \"Independent entry for the مست/مویه family with '*MUSTI (OLD PERSIAN), MUST (PAHLAVI), MUTHOS (GREEK), MAUDJAN (GOTHIC)' and 'MACKENZIE: (COMPLAINT) 107'.\"},\n    {\"src\": \"CHEUNG\", \"where\": \"s.v. *maud?\", \"stance\": \"supports\",\n     \"note\": \"'NP mōyidan \\\"to mourn; weep and cry aloud\\\", NP must \\\"trouble, distress of mind, complaint, lamentation\\\"' — the two New Persian words of this box, with Nourai's glosses.\"}\n  ],\n  \"note_on_chart_note\": \"Nourai's own NOTE ('HRN:223 links these to Avestan \\\"amâ-yavâ:grief\\\". See root \\\"Ome\\\"') is a fair report of Horn — but Horn's link is explicitly tentative ('vergl.'), the Avestan form is amayavā- (not amâ-yavâ), and modern scholarship (Cheung 2007) rejects the connection; the cross-reference to 'Ome' is where the Skt. āmīvā- family that Horn cites in the same line actually belongs.\"\n },\n {\n  \"id\": 4, \"lang\": \"Old Iranian\", \"words\": \"maud, mauda\", \"verdict\": \"confirmed\",\n  \"derivation\": \"Abolghasemi's Fe'l-hā/Māde-hā-ye fe'l-hā-ye fārsi-ye dari p. 77 — the page Nourai cites — gives verbatim 'موی ← فارسی میانه mōy ← ایرانی باستان *maud-a … ریشهٔ maud به معنی «نالیدن» است', i.e. root *maud- with the thematic present stem *maud-a-, exactly Nourai's pair 'maud, mauda'. Iranian *maud- is the de-aspirated reflex of PIE *maudʰ- (Iranian merged the voiced aspirates with the plain voiced stops), and Middle Persian mōy comes from it by monophthongisation of *au > ō plus the change of post-vocalic *-d- > -y-. Horn had already reported the same reconstruction from F. Müller (WZKM 5, 65: 'construirt eine *√maud- mit einem ap. *mauda- als Grundform'). Cheung 2007 sets up '*maud ? \\\"to mourn\\\"' for these forms but marks it doubtful, because an identical Iranian root *maud 'to rejoice' is attested (Av. maoδanō.kara- 'providing joy', OP *maudabaga-) and he prefers contamination with *nau(H) 'to mourn' (cf. NP نوییدن، نویه). So the node's forms are right and standard in the Iranian handbooks; their status is 'reconstructed, and questioned by Cheung'.\",\n  \"derivation_fa\": \"ابوالقاسمی در «ماده‌های فعل‌های فارسی دری» ص ۷۷ — همان صفحه‌ای که نورایی ارجاع داده — عیناً می‌نویسد: «موی ← فارسی میانه mōy ← ایرانی باستان *maud-a … ریشهٔ maud به معنی «نالیدن» است»؛ یعنی ریشهٔ *maud- با ستاک حالِ *maud-a-، درست همان دو صورتی که نورایی آورده است. ایرانی *maud- بازتاب بی‌دمشِ *maudʰ- هندواروپایی است (در ایرانی، انسدادی‌های واکدارِ دمیده با واکدارِ ساده یکی شده‌اند)، و mōy فارسی میانه از آن با تک‌واکه‌شدنِ *au به ō و بدل شدن -d- میان‌واکه‌ای به -y- ساخته شده است. هرن نیز پیش‌تر همین بازسازی را از فریدریش مولر گزارش کرده بود («*√maud- با صورت بنیادینِ پارسی باستان *mauda-»). چونگ (۲۰۰۷) این ریشه را با علامت پرسش «*maud? سوگواری کردن» آورده و در آن تردید کرده است، زیرا در ایرانی ریشهٔ همسانِ *maud «شادی کردن» گواه دارد (اوستایی maoδanō.kara-، پارسی باستان *maudabaga-) و او آمیختگی با ریشهٔ *nau(H) «مویه کردن» را محتمل‌تر می‌داند (قس «نوییدن، نویه»). پس صورت‌های این گره درست و در کتاب‌های ایران‌شناسی رایج است، با این قید که بازساخته‌اند و چونگ در آنها تردید کرده است.\",\n  \"sources\": [],\n  \"ref_check\": [\n    {\"ref\": \"FFD:77\", \"status\": \"supports\",\n     \"note\": \"Read from the page image (data/verification/sources/refs/ocr/FFD/77.png, transcript in 77.vision.txt): 'موییدن — «مویید» مادهٔ ماضی جعلی است، از مادهٔ مضارع ساخته شده است. موی ← فارسی میانه mōy ← ایرانی باستان *maud-a. برای a ← آرای. ریشهٔ maud به معنی «نالیدن» است.' Printed p. 77 = pdf p. 82 (header «ماده‌های ماضی و مضارع فارسی دری ۷۷»), matching the stated offset printed = pdf − 5.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"CHEUNG\", \"where\": \"s.v. *maud? 'to mourn' (pp. 270 f.)\", \"stance\": \"partial\",\n     \"note\": \"Cheung reconstructs the same root shape but with a question mark and prefers contamination of *nau(H) 'to mourn' with *maud 'to rejoice'; 'REFERENCES: Horn 1893: 223 f.' — the same Horn pages Nourai cites.\"},\n    {\"src\": \"HRN\", \"where\": \"no. 997, printed p. 224\", \"stance\": \"supports\",\n     \"note\": \"'Fr. Müller (WZKM. 5, 65) construirt eine *√maud- mit einem ap. *mauda-- als Grundform und identificirt np. mōye mit arm. moir \\\"Bettelei\\\" … dazu auch np. must \\\"Klage\\\", mustmend' — the Old Iranian *maud-/*mauda- of this box, with its scholarly provenance.\"},\n    {\"src\": \"POK\", \"where\": \"p. 743 s.v. meudʰ-, maudʰ-, mudʰ-\", \"stance\": \"supports\",\n     \"note\": \"Pokorny's lemma already contains the *maudʰ- grade that Iranian *maud- reflects, and its Persian material (mōja, must) is the branch this node feeds.\"},\n    {\"src\": \"BRT\", \"where\": \"grep 'maud', 'maoδ' in BRT.txt\", \"stance\": \"silent\",\n     \"note\": \"Bartholomae has no Avestan verb *maud- 'to lament' (only maoδanō.kara- 'joy-causing' belongs to the homophonous 'rejoice' root), which is why this box must be labelled Old Iranian rather than Avestan — and confirms that node #1's Avestan label is the chart's real error.\"}\n  ]\n }\n]\n\nout = {\n \"pdf_page\": 341,\n \"book_page\": 311,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-07\",\n \"entries\": [entry4, entry5],\n}\n\nwith io.open(\"/home/sfmqrb/git/rishe/data/verification/page-341.json\", \"w\", encoding=\"utf-8\") as f:\n    json.dump(out, f, ensure_ascii=False, indent=1)\n    f.write(\"\\n\")\nprint(\"written\")\n"
}
```


### [2026-09-07T17:57:59.365Z] TOOL RESULT

```
File created successfully at: /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/mk341.py (file state is current in your context — no need to Read it back)
```


## [2026-09-07T17:58:03.836Z] TOOL CALL #93: Bash

```json
{
 "command": "python3 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/mk341.py && python3 -m json.tool data/verification/page-341.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 341"
}
```


### [2026-09-07T17:58:05.929Z] TOOL RESULT

```
written
JSON OK
nodes verified: 11/11
node verdicts: {'confirmed': 9, 'plausible': 1, 'disputed': 1}
root verdicts: {'confirmed': 2}
ref checks: {'supports': 13, 'not_checked': 2, 'partial': 2}
books consulted: {'supports': 28, 'silent': 7, 'partial': 3, 'contradicts': 1} | by book: {'HRN': 4, 'KLN': 4, 'CHEUNG': 4, 'BRT': 3, 'WLD': 3, 'ARY': 3, 'MON': 3, 'POK': 3, 'PHD': 2, 'NYB': 2, 'SKT': 2, 'AHD': 1, 'IEC': 1, 'LAT': 1, 'LEW': 1, 'FSD': 1, 'BQT': 1}
```


## [2026-09-07T17:58:10.450Z] TOOL CALL #94: Bash

```json
{
 "command": "python3 tools/verify_archive_sources.py 2>&1 | tail -20"
}
```


### [2026-09-07T17:58:13.393Z] TOOL RESULT

```
3222 cited URLs, 9 not yet archived
archived 9, failed 0
```


## [2026-09-07T17:58:18.403Z] TOOL CALL #95: Bash

```json
{
 "command": "python3 - <<'EOF'\nimport json\nurls=set()\nd=json.load(open('data/verification/page-341.json'))\ndef walk(o):\n    if isinstance(o,dict):\n        for k,v in o.items():\n            if k=='sources': urls.update(v)\n            else: walk(v)\n    elif isinstance(o,list):\n        for x in o: walk(x)\nwalk(d)\nidx={json.loads(l)['url'] for l in open('data/verification/sources/web/index.jsonl')}\nfor u in sorted(urls):\n    print('OK ' if u in idx else 'MISSING ', u)\nEOF"
}
```


### [2026-09-07T17:58:19.734Z] TOOL RESULT

```
OK  https://en.wiktionary.org/wiki/%D9%85%D8%B3%D8%AA
OK  https://en.wiktionary.org/wiki/%D9%85%D8%B3%D8%AA%D9%85%D9%86%D8%AF
OK  https://en.wiktionary.org/wiki/%D9%85%D9%88%D8%B1
OK  https://en.wiktionary.org/wiki/%D9%85%D9%88%D8%B1%DB%8C%D8%A7%D9%86%D9%87
OK  https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/morw%C3%ADs
OK  https://en.wiktionary.org/wiki/formica#Latin
OK  https://www.etymonline.com/word/chloroform
OK  https://www.etymonline.com/word/formic
```


## [2026-09-07T17:58:40.883Z] AGENT

Page 341 verified; `verify_check.py 341` shows 11/11 nodes, 0 PROBLEM lines.

**Counts** — roots: 2 confirmed. Nodes: 9 confirmed, 1 plausible, 1 disputed. Ref checks: 13 supports, 2 partial, 2 not_checked. Books consulted: 28 supports, 3 partial, 1 contradicts, 7 silent (POK, WLD, AHD, IEC, BRT, PHD, NYB, CHEUNG, HRN, HUB, KLN, SKT, LAT, LEW, BQT, MON, ARY, SNS, FFD, SYN, FSD).

**Flagged items**
- `disputed` — **Moudh**, node #1 [Avestan] "môy : groaning; a-mayavâ : grief". There is no Avestan *mōy* (mōy/mōyag are Middle Persian); Cheung 2007 s.v. *maud? says the Persian forms are "isolated within IIr." Av. amayavā- does exist (Bartholomae 'Leid, Drangsal', Y.71.17) but Horn — the cited page (no. 997) — offers it only as "aw. vergl.", paired with Skt. āmīvā- of another root (Nourai's own "see root Ome"). The real ancestor is his own node #4, Old Iranian *maud-a-.
- `plausible` — **Morwi**, node #4 [Latin] "vormîca, formica". formīca is right (< Proto-Italic *mormīkā, dissimilation m…m > f…m: POK 749, WLD II 306, Ernout-Meillet, Wiktionary). "vormîca" is not Latin: it is Klein's reconstruction (*p. 613 s.v. formic*: "dissimilated fr. *mor-mica, fr. orig. *vormica"), i.e. Pokorny's *u̯orm- grade attested only in Greek βύρμαξ and Skt. valmīka-. Book p. 311 prints it in the Latin box, so this is Nourai's error, not the extraction's.

**Extraction errors**: none — the JSON matches the printed page (checked against a render of PDF p. 341, copied to `data/verification/sources/refs/ocr/BOOK/341.png`).

**Best finds**: Pokorny 743 has a lemma "meudʰ-, maudʰ-, mudʰ- 'to complain'" whose first material is "Npers. mōja … must (-st- from -dʰ-st-)", so the Moudh root is better supported than Nourai's own IEC:802 citation; Mo'in's Borhan footnotes p. 2049 give Av. maoiri- → Pahl. mōr / mōrcak verbatim; SNS:248 checks out via Tavoosi's index (mōr 248/4, mōrcag 248/10); FFD p. 77 gives "موی ← فارسی میانه mōy ← ایرانی باستان *maud-a" verbatim. New audit files: `refs/ocr/BQT/2049.vision.txt`, `refs/ocr/FFD/77.png` + `77.vision.txt`. 8 web sources archived via fetch_source.py.
