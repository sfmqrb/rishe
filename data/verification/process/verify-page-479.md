# Verification process log — verify-page-479


## [2026-09-14T03:08:07.423Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 479 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-479.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-479.json. Write /home/sfmqrb/git/rishe/data/verification/page-479.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 479` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-14T03:08:08.467Z] AGENT

I'll start by reading the instructions.


## [2026-09-14T03:08:09.317Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-14T03:08:09.350Z] TOOL RESULT

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


## [2026-09-14T03:08:09.823Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-479.txt"
}
```


### [2026-09-14T03:08:09.846Z] TOOL RESULT

```
1	=== PDF page 479 (book page 449) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Steigh, Stoigh : to stride, step, rise  (refs POK:1017)
4	#1 (parent #0) [Greek] refs=POK:107; AHD | stoixeion : shadow line, element
5	  #2 (parent #1) [Arabic] refs=TAD:3 | estoqos : element
6	    #3 (parent #2) [Persian] refs=MON:266 | ostoqos «اُسطُقُس» : substance, strength
7	  #4 (parent #1) [English] refs=AHD:1269 | stoichiometry : determining different elements in a chemical compound
8	#5 (parent #0) [Sanskrit] refs=POK:1017 | stiğnôti : he climbs
9	#6 (parent #0) [Greek] refs=AHD | stixos : row, line
10	  #7 (parent #6) [English] refs=AHD:1268 | stitch
11	#8 (parent #0) [Germanic] refs=AHD | staigrî : stair, step
12	  #9 (parent #8) [English] refs=AHD | stair
13	--- entry 1 ---
14	ROOT Stena -> redirect to Ten 2
15	--- entry 2 ---
16	ROOT [Indo-European] Ster 1, Stor, Str : to spread  (refs POK:1029)
17	#1 (parent #0) [Avestan] refs=KLN:1522; FFD:73 | star 1 : to spread ; wi-star : to spread apart ☞Wi
18	  #2 (parent #1) [Pahlavi] refs=BQT:278,1816; HRN:205 | vi-startan : to spread out ☞Wi ; vi-starak : bed (spread for sleeping) ☞Wi ; xâk-astar : spread dust (fire ashes)
19	    #3 (parent #2) [Persian] refs=BQT:702,1816; SNS:273; FFD | gostardan «گستردن» : to spread ; bastar «بستر» : bed ; xâkestar «خاکستر» : ashes | extra: گسترانیدن ، گستریدن ، گستر ، گسترش
20	#4 (parent #0) [Latin] refs=KLN:1522 | strata : paved path
21	  #5 (parent #4) [Greek] refs=KLN | 
22	    #6 (parent #5) [Aramaic] refs=KLN:56 | isrâta : paved path
23	      #7 (parent #6) [Arabic] refs=POK:56; FVQ:195; TAD:34 | serât : path, way
24	        #8 (parent #7) [Persian] refs=MON | serât «صراط» : road
25	  #9 (parent #4) [English] refs=AHD; KLN | stray ; street
26	#10 (parent #0) [Latin] refs=AHD | struere : to construct ; industria : activity
27	  #11 (parent #10) [English] refs=None | construct ; destroy ; instruction ; industry ; structure
28	#12 (parent #0) [Greek] refs=AHD:1273 | stratos : multitude, army ; stratos-agein : army leader ☞Ag
29	  #13 (parent #12) [French] refs=AHD:1273 | strategie : a military plan
30	    #14 (parent #13) [Persian] refs=MON:246 | esterâtežî «استراتژی»
31	    #15 (parent #13) [English] refs=AHD:1273 | strategy
32	#16 (parent #0) [Germanic] refs=AHD | strawam : scattered
33	  #17 (parent #16) [English] refs=None | straw
34	
```


## [2026-09-14T03:08:13.014Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-479.json | head -200 && echo \"=== TOOLS ===\" && ls tools/ && echo \"=== EXISTING ===\" && ls data/verification/ | head -30",
 "description": "Read source JSON and list tools"
}
```


### [2026-09-14T03:08:13.144Z] TOOL RESULT

```
{
  "pdf_page": 479,
  "book_page": 449,
  "entries": [
    {
      "root": {
        "name": "Steigh, Stoigh",
        "lang": "Indo-European",
        "refs": "POK:1017",
        "gloss": "to stride, step, rise"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Greek",
          "refs": "POK:107; AHD",
          "words": [
            {"translit": "stoixeion", "gloss": "shadow line, element", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Arabic",
          "refs": "TAD:3",
          "words": [
            {"translit": "estoqos", "gloss": "element", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "MON:266",
          "words": [
            {"translit": "ostoqos", "gloss": "substance, strength", "script": "اُسطُقُس"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 1,
          "lang": "English",
          "refs": "AHD:1269",
          "words": [
            {"translit": "stoichiometry", "gloss": "determining different elements in a chemical compound", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "POK:1017",
          "words": [
            {"translit": "stiğnôti", "gloss": "he climbs", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 0,
          "lang": "Greek",
          "refs": "AHD",
          "words": [
            {"translit": "stixos", "gloss": "row, line", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "English",
          "refs": "AHD:1268",
          "words": [
            {"translit": "stitch", "gloss": null, "script": null}
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
            {"translit": "staigrî", "gloss": "stair, step", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "stair", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Stena",
        "redirect": "Ten 2"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Ster 1, Stor, Str",
        "lang": "Indo-European",
        "refs": "POK:1029",
        "gloss": "to spread"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "KLN:1522; FFD:73",
          "words": [
            {"translit": "star 1", "gloss": "to spread", "script": null},
            {"translit": "wi-star", "gloss": "to spread apart", "script": null, "see": ["Wi"]}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "BQT:278,1816; HRN:205",
          "words": [
            {"translit": "vi-startan", "gloss": "to spread out", "script": null, "see": ["Wi"]},
            {"translit": "vi-starak", "gloss": "bed (spread for sleeping)", "script": null, "see": ["Wi"]},
            {"translit": "xâk-astar", "gloss": "spread dust (fire ashes)", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "BQT:702,1816; SNS:273; FFD",
          "words": [
            {"translit": "gostardan", "gloss": "to spread", "script": "گستردن"},
            {"translit": "bastar", "gloss": "bed", "script": "بستر"},
            {"translit": "xâkestar", "gloss": "ashes", "script": "خاکستر"}
          ],
          "script_extra": "گسترانیدن ، گستریدن ، گستر ، گسترش",
          "note": null,
          "quote": {
            "text": "بگسترد فرشی زدیبای چین - که گفتی مگر آسمان شد زمین",
            "poet": "Ferdowsî"
          }
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Latin",
          "refs": "KLN:1522",
          "words": [
            {"translit": "strata", "gloss": "paved path", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Greek",
          "refs": "KLN",
          "words": [],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "Aramaic",
          "refs": "KLN:56",
          "words": [
            {"translit": "isrâta", "gloss": "paved path", "script": null}
          ],
          "note": null,
          "quote": null
=== TOOLS ===
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
=== EXISTING ===
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
```


## [2026-09-14T03:08:16.161Z] TOOL CALL #4: Bash

```json
{
 "command": "sed -n 200,400p data/extracted/batch/page-479.json; echo \"=== MATRIX ===\"; cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read rest of JSON and source matrix"
}
```


### [2026-09-14T03:08:16.224Z] TOOL RESULT

```
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "Arabic",
          "refs": "POK:56; FVQ:195; TAD:34",
          "words": [
            {"translit": "serât", "gloss": "path, way", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 7,
          "lang": "Persian",
          "refs": "MON",
          "words": [
            {"translit": "serât", "gloss": "road", "script": "صراط"}
          ],
          "note": null,
          "quote": {
            "text": "اِهدنا گفتی صراط مستقیم - دست تو بگرفت و بُردت تانعیم",
            "poet": "Molavî"
          }
        },
        {
          "id": 9,
          "parent": 4,
          "lang": "English",
          "refs": "AHD; KLN",
          "words": [
            {"translit": "stray", "gloss": null, "script": null},
            {"translit": "street", "gloss": null, "script": null}
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
            {"translit": "struere", "gloss": "to construct", "script": null},
            {"translit": "industria", "gloss": "activity", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 10,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "construct", "gloss": null, "script": null},
            {"translit": "destroy", "gloss": null, "script": null},
            {"translit": "instruction", "gloss": null, "script": null},
            {"translit": "industry", "gloss": null, "script": null},
            {"translit": "structure", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 0,
          "lang": "Greek",
          "refs": "AHD:1273",
          "words": [
            {"translit": "stratos", "gloss": "multitude, army", "script": null},
            {"translit": "stratos-agein", "gloss": "army leader", "script": null, "see": ["Ag"]}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 13,
          "parent": 12,
          "lang": "French",
          "refs": "AHD:1273",
          "words": [
            {"translit": "strategie", "gloss": "a military plan", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 14,
          "parent": 13,
          "lang": "Persian",
          "refs": "MON:246",
          "words": [
            {"translit": "esterâtežî", "gloss": null, "script": "استراتژی"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 15,
          "parent": 13,
          "lang": "English",
          "refs": "AHD:1273",
          "words": [
            {"translit": "strategy", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 16,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "strawam", "gloss": "scattered", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 17,
          "parent": 16,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "straw", "gloss": null, "script": null}
          ],
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
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt` (truncated before the lexicon's h–z section, ~p. 208 on)
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT_full.txt` (complete archive.org djvu text — use this for lexicon pages 208–215: haumavarga-, siyamam, etc.)
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


## [2026-09-14T03:08:21.397Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json,glob\nfor f in sorted(glob.glob('data/verification/page-4*.json'))[:20]:\n    d=json.load(open(f))\n    print(f, [e['entry'] for e in d['entries']])\n\" 2>&1 | head -20; echo ===; sed -n 1,80p data/verification/page-478.json 2>/dev/null || ls data/verification/ | tail -20",
 "description": "Inspect existing verification outputs"
}
```


### [2026-09-14T03:08:22.561Z] TOOL RESULT

```
Exit code 1
data/verification/page-40.json [0, 1]
data/verification/page-400.json [0]
data/verification/page-401.json [0, 1, 3]
data/verification/page-402.json [0, 3]
data/verification/page-403.json [0, 1, 2]
data/verification/page-404.json [0, 6]
data/verification/page-405.json [0, 4]
data/verification/page-406.json [0]
data/verification/page-407.json [0, 1]
data/verification/page-408.json [0, 2, 4]
data/verification/page-409.json [0, 1]
data/verification/page-41.json [0]
data/verification/page-410.json [8]
data/verification/page-411.json [3, 5]
data/verification/page-412.json [0, 6]
data/verification/page-413.json []
data/verification/page-414.json [0, 2]
data/verification/page-415.json [0, 2, 3]
data/verification/page-416.json [0]
data/verification/page-417.json [0]
(eval):6: == not found
```


## [2026-09-14T03:08:24.662Z] TOOL CALL #6: Bash

```json
{
 "command": "cat tools/verify_check.py",
 "description": "Read verify_check.py"
}
```


### [2026-09-14T03:08:24.726Z] TOOL RESULT

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


## [2026-09-14T03:08:30.520Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources && python3 -c \"\nimport json\nd=json.load(open('refs_online.json'))\nfor k in ['POK','KLN','AHD','MON','BQT','HRN','TAD','FVQ','SNS','FFD','WLD','IEC','SYN','BRT','PHD','NYB','CHEUNG','ARY','SKT','LEW','LAT','AFM','PLA','AFA','LKT']:\n    v=d.get(k)\n    if v: print(k, json.dumps(v, ensure_ascii=False)[:600]); print()\n\"",
 "description": "Check refs_online metadata"
}
```


### [2026-09-14T03:08:31.655Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 

TAD {"title": "Tobia al-Unaysi (طوبيا العنيسي), Tafsir al-alfaz al-dakhila fi al-lugha al-'arabiyya ma'a dhikr asliha bi-hurufihi (2nd ed. Cairo 1932, ed. Yusuf Tuma al-Bustani; later Library of Lebanon reprint) — Nourai lists it under Arabic authors ('Unaysi T.'); its Table IV line was lost in the OCR", "kind": "archive_djvu", "url": "https://archive.org/details/TOB1932ARAR (1932 ed.); also https://archive.org/details/ar113lang79 and https://archive.org/details/elshandawily14640", "lookup_hint": "Alphabetical Arabic headwords; grep the Arabic headword in TAD_pages.txt (86 leaves) or TAD.txt; insi

FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sou

SNS {"title": "Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/VajnameShayest", "lookup_hint": "grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php search (see BQT) for better hit-to-leaf mapping.", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS.txt

FFD {"title": "Mohsen Abolghasemi, Fe'l-ha-ye Farsi-ye Dari, Qoqnus, Tehran 1374/1995", "kind": "local_scan_ocr", "url": "https://asmaneketab.ir/product/کتاب-ماده-های-فعلهای-فارسی-دری-محسن-اب/ -> https://dl.eliteraturebook.com/app/public/attachments/6925d29630b83.PDF (free PDF site; grey)", "lookup_hint": "Searched archive.org (Persian/Latin titles, author), ketabnak, noorlib, general web (pdf/download): nothing; only a related paid e-book 'واژگان زبان فارسی دری' (fidibo). ketabnak.com/book/45024 is a different book (فهرست فعلهای فارسی).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/s

WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039

IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 

SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves

BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1

PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-

NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf

ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it 

SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves

LEW {"title": "A. Walde (& J. B. Hofmann), Lateinisches etymologisches Wörterbuch, 3rd ed., Heidelberg 1938-56", "edition_found": "2nd ed. 1910 (open); 3rd ed. 1938 vol. 1 is lending-only (lateinischesetym0000awal)", "kind": "archive_djvu", "url": "https://archive.org/details/lateinischesetym0000aloi", "identifier": "lateinischesetym0000aloi (1910); restricted 1938: lateinischesetym0000awal", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LEW_1910.txt", "page_offset": "1910 ed.: leaf = printed + 12 (e.g. leaf 15 = p.3). Page numbers of the 3rd ed. differ. local file has \\f b

LAT {"title": "A. Ernout & A. Meillet, Dictionnaire étymologique de la langue latine, 3rd ed., Paris 1951", "edition_found": "1951 (3rd ed.) - matches Nourai", "kind": "archive_djvu", "url": "https://archive.org/details/ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine", "identifier": "ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine (4th ed. 1959 lending-only: dictionnairetymo0000unse; another open copy: DictionnaireEtymologiqueDeLaLangueLatine)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LAT.txt", "page_offset": "leaf = printed + 18 for mos

AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/

PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt"], "page_offset": "301 lea

AFA {"title": "S. Fraenkel, Die aramäischen Fremdwörter im Arabischen, Leiden 1886 (repr. Hildesheim 1962, same pagination)", "edition_found": "1886", "kind": "archive_djvu", "url": "https://archive.org/details/diearamischenfr00fraegoog", "identifier": "diearamischenfr00fraegoog (also bub_gb_SzdbAAAAQAAJ)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AFA.txt", "page_offset": "leaf = printed + 30 (e.g. leaf 38 = p.8). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",

LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Numbered entries:
```


## [2026-09-14T03:08:37.885Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources && python3 -c \"\nimport json\nd=json.load(open('refs_online.json'))\nprint(d['POK']['page_offset']); print('---'); print(d['POK'].get('lookup_hint'))\nprint('=== KLN'); print(d['KLN']['page_offset']); print(d['KLN'].get('lookup_hint'))\nprint('=== AHD'); print(d['AHD'].get('page_offset')); print(d['AHD'].get('lookup_hint'))\nprint('=== BQT'); print(d['BQT'].get('page_offset')); print(d['BQT'].get('lookup_hint'))\nprint('=== TAD'); print(d['TAD'].get('page_offset'))\nprint('=== FFD'); print(d['FFD'].get('page_offset')); print(d['FFD'].get('lookup_hint'))\nprint('=== SNS'); print(d['SNS'].get('page_offset'))\nprint('=== MON'); print(d['MON'].get('page_offset')); print(d['MON'].get('lookup_hint'))\n\"",
 "description": "Print page offsets"
}
```


### [2026-09-14T03:08:39.008Z] TOOL RESULT

```
POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
---
Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-dictionary/ (entry pages with page numbers) and StarLing https://starlingdb.org/cgi-bin/query.cgi?basename=\data\ie\pokorny&root=config
=== KLN
KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.
=== AHD
1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page.
Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru-' ; entries list English derivatives in caps. Restricted 1970s AHD scans on IA (lending only, djvu.txt returns 401): americanheritage0000dict (July 1977 printing, 970 leaves - probably the New College Edition), bwb_P9-BHZ-437 (1974), americanheritage00nyde (1970), bwb_W9-CSW-086 (1969, 1610 leaves = original 1969 ed.).
=== BQT
vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...').
grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=dehkhoda, parsi.wiki, abadis.ir/fatofa/<word>/) quotes Borhan and often Mo'in's footnotes as (حاشیهٔ برهان قاطع چ معین). noorlib.ir/book/info/10294 is a 1-vol Nima 1380 Borhan without Mo'in's notes. | For pages in a scanned volume use: python3 tools/ref_page.py BQT:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)
=== TAD
86 leaves (small book, ~80 printed pages); offset ≈ leaf − 4..6, verify against the printed numeral on the page image
=== FFD
115 leaves (PDF pages); printed page = PDF page − 5 (PDF 40 = p.35). 2nd printing 1385 of the same Qoqnus setting (ISBN 964-311-015-X).
Searched archive.org (Persian/Latin titles, author), ketabnak, noorlib, general web (pdf/download): nothing; only a related paid e-book 'واژگان زبان فارسی دری' (fidibo). ketabnak.com/book/45024 is a different book (فهرست فعلهای فارسی).
=== SNS
242 leaves; page offset not determined (OCR too poor to read printed numbers) — locate by transliteration then read the page image
=== MON
None
Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different pagination from the 6-vol edition; OCR downloaded as MON_part1.txt / MON_part2.txt (no page breaks).
```


## [2026-09-14T03:08:43.046Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"lemma: steigh\" POK_full.txt; echo ===; grep -n \"lemma: ster\" POK_full.txt; echo === ; grep -n \"Page(s): 1017\\|Page(s): 1029\" POK_full.txt",
 "description": "Grep Pokorny for steigh and ster"
}
```


### [2026-09-14T03:08:43.118Z] TOOL RESULT

```
81594:Root / lemma: steigh- 
(eval):1: == not found
```


## [2026-09-14T03:08:45.068Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '81590,81640p' POK_full.txt",
 "description": "Print Pokorny steigh entry"
}
```


### [2026-09-14T03:08:45.131Z] TOOL RESULT

```
Page(s): 1014 



Root / lemma: steigh- 

Meaning: to march, ascend 

Material: Old Indie stighndti^s\.e\q\! (Dhatup.), ved. pra-stighnuyatO^i. present "er moge 

emporkommen', ati-stigham\n\. 'iJberstelgen, bemeistern'; 

gr. aTsixw 'schreite, go', *aTi^, Gen. OTixoq, PI. arixs";, -ac, "row, Zeile', Attic o^'xxoc, 'row, 
Zeile, line', OTixaaGai "in dichter Reihe besides- or hintereinander go or come', gtoTxoc; 
"row, line'; 

alb. shtek, shteg-u^ passage, entrance, way, Haarscheitel' (= aToTxo(;); 

Old Irish t/agu'\ schreite, go', techti. "the going, the summoner', cymr. /a///? "journey' = 
bret. //z"haste, hurry' {*[s]tikta), cymr. mor-dwy^Seeiahri' {*[s]teigho-) etc.; 

Gothic steigan. Old Icelandic stTga, Old English Old High German stTgan " ascend ' (= gr. 
GTsixu)); Old High German stTg^ steep path, path, track, grade'. Old Icelandic stTgr 
"Fuftsteig'; Gothic staiga^ steep path, way'. Old High German s/e/iga "steiler way'; 

Old High German stegm. "narrow bridge, gangplank, footbridge, small bridge'; Old 
Icelandic st/g/'m. 'Stiege, ladder', st/'gn. " footstep, grade'. Old English st/ge'das Hinauf- 
or Herabsteigen', Old High German stega^grade, stairs, ladder' (Old High German stiega. 
Modern High German Stiege W\Vc\ e^, also probably from *steigha)\ Old English staegeri. 
"Treppe' (engl. staii). Middle Low German ste/ger' steep', nid. "Ladeplatz, scaffold, trestle'. 
Old Icelandic ste/gur-//gr' steep, erect'; Old Icelandic stetti. " footprint, Trittstein, way. 
Stand, rank', steftrm. ds. (: cymr. fa/th). Old Icelandic stetta^ support, help'. Old English 
stihtan, st/ht/an {'*aui e\ne basis place =) einrichten, sort, order, arrange', anfrk. stihtan{= 
Old High German stiftanl) etc.; 

Lithuanian staigaMy. "sudden', s/5/g^5 "violent, quick, fast aufbrausend', staigaus, -ytis 
and steigiuos, ste/gt/s's\c\r\ beeilen, sich bemuhen'; Latvian steidzu(ds), steigi{ies) "sich 
beeilen', s/a/^^/ "change', stiga^ path, track '; Old Church Slavic st/gngl come', stbdza, 
s/i.za"Fuftsteig, road', sttgna ' road' . 

References: WP. II 614 f., Trautmann 285 f. 
Page(s): 1017-1018 

Root / lemma: (s)teig- 
Meaning: to stick; sharp 



Note: extension from stei- ds. 

Material: Old Indie tejate^'xs sharp, scharft', tejayat/ 'scharft, stachelt', t/kta- "sharp, bitter',
```


## [2026-09-14T03:08:54.177Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^Root / lemma: ster\" POK_full.txt | head -30; echo \"=== pages\"; grep -n \"^Page(s): 102[5-9]\\|^Page(s): 103[0-2]\" POK_full.txt | head",
 "description": "Find ster- roots in Pokorny"
}
```


### [2026-09-14T03:08:54.358Z] TOOL RESULT

```
81998:Root / lemma: sterg-, sterk- 
82496:Root / lemma: ster-3 
82508:Root / lemma: ster-4 
82599:Root / lemma: ster-5, stera- : stre-, steru- : streu- 
82687:Root / lemma: ster-6 
83007:Root / lemma: ster-2 
=== pages
82597:Page(s): 1028-1029 
82685:Page(s): 1029-1031 
82764:Page(s): 1031-1032 
82917:Page(s): 1032-1034 
83061:Page(s): 1027-1028
```


## [2026-09-14T03:08:56.767Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '82687,82770p' POK_full.txt",
 "description": "Print Pokorny ster-6 entry"
}
```


### [2026-09-14T03:08:56.835Z] TOOL RESULT

```
Root / lemma: ster-6 

Meaning: sterile 

Note: old Sonderanwendung from ster- " stiff ' 



Material: Old Indie stan-i. " infertile e cow'; 

Armenian sterj^ infertile, from animals', also sterd {*ster-6^-o-, -Jo); 

gr. GTsTpa f. ' infertile ' (cow, wife, woman), aT£pi(po(; ' infertile ' (and " rigid'); 

alb. sMJerre young cow, lamb'; also prefixed alb. meshqere " young cow'. 

Latin sterilis " infertile '; 

Gothic stairoi. " infertile ', Old High German stero^aues, ram'; with /r- extended mndd. 
s/eA/re "young cow'. Old English stierc^caW; isl. stirtla^ infertile cow'; 

Bulgarian s/e/7ic5'Gelte'. 

References: WP. II 640 f., WH. II 589 f. 
Page(s):1031 

Root / lemma: (s)ter-7n- 

Meaning: sharp stalk or thorn 

Note: to ster- ' stare, stiff sein' 

Material: Old Indie //•/7a-/77'Grashalm, grass, herb'; gr. rspva^ 'Artischocken-, 

Kaktusstengel'; Gothic t^aurnus. Old Icelandic Old English t^orn. Old High German dorn 

"thorn'; Old Church Slavic trbni, 'thorn', strbnt ' stem '. 

References: WP. II 641, Trautmann 324, Vasmer 3, 14, 98. 

Page(s):1031 

Root / lemma: (s)ter-8 

Meaning: dirty water, mud, smear 

Material: Avestan star- "sich blemish, commit a sin'; 

Armenian f arax, -ic, -oc'pus, humeur' {%ro-, besides ograde perhaps:) Armenian for 
"that flows down, that drops'; Norwegian storn. 'Faulen, Verwesen'; russ.-Church Slavic 
stbrvb, russ. sterva^ carrion '; without aniaut. s-: Lithuanian ferment/^ smear', Bulgarian 
torb ' manure'. 

(s)teii(-, nasal. (s)trenR-: 

Latin stercus, -oris " excrement, ordure, crap, muck, droppings, manure', sterculTnum, 
sterquilTnum^ dunghill '; cymr. trwnc^ urine, yeast', bret. s//ic»/7/r "human excrement'; 



cymr. troeth^\ye, urine ', /Aoe/^/'mingere', bret. troaz^ urine ' {*trokta or * tronktS); 
Lithuanian tersiu, /eA5//"smudge', S/O/eAs// "smudge', ///"sZ/'dickfiussig become'; East 
Litliuanian tr§siu, tr^stT fertilize ' (as Latin stercorare); 

Litliuanian tr^sa^ manure', tresti^ decayed, verwesen', fraskanos^pus in den Augen', 
wherefore nisi. Prarlau\, rancid ', Norwegian traads., Old English droh Rancor'. 

(s)terg-, (s)treg- 

gr. OTspyavoq Konpwv Hes.; rapyavov "Weinessig'; ablaut, rpu^, -yog "young, still trijber 
wine, Weinhefe '; expressive Old Icelandic t^rekkr. Middle High German dree, -ckes^ filth '; 
probably also Old English dreax^caues'; perhaps Latin tro/a'sow' {*troQ/a'6\e Dreckige'), 
das but also to Middle Irish //'c»^a/io'"gebiert' belong could; whether Old Irish tore, cymr. 
t\/i/rch, acorn, torch, bret. tourc'h'boar' from *trogos aiter fpjorc-' s\N\ne' reshaped sei, is 
doubtful, yet could es as *torkos zur group auf Tenuis belong. 

References: WP. II 641 f., WH. II 708, VasmerS, 12. 
Page(s): 1031-1032 

Root / lemma: (s)teu-1 

Meaning: to push, hit 

Note: with conservative extensions
```


## [2026-09-14T03:09:01.766Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '82599,82686p' POK_full.txt",
 "description": "Print Pokorny ster-5 entry"
}
```


### [2026-09-14T03:09:01.872Z] TOOL RESULT

```
Root / lemma: ster-5, stera- : stre-, steru- : streu- 

Meaning: to widen, to scatter 

Note: (compare ster- " stare, stiff sein') 



Material: A. Old Indie strnati, s//77d7/ (actually zur basis streu-), later also staratr s\xe\i\. 
(hin), bestreut; wirft hin, wirft low, base', participle strta-, stTrna-, Inf. s/5/fai/eand staritavai, 
stantave; sva-stara-m. 'eigene Streu', pra-stara-xx\. 'Streu, cushion; surface, plain, area, 
plain ' (= russ. prostor^Rawm, Geraumigkeit'); starT-man-v\. 'Ausbreitung, Ausstreuung' 
(ablaut, with gr. arpajpa, LaWustramen); 

Avestan star- (present starati, staranaoti, staranati) 'sternere', participle sfarafa-an6 
starata-, stain's- v\. 'Streu, lair, bed'; urvard-straya-^H\e6er\\auev\irom Pflanzungen'; 

gr. GTopvufji (only present and Impf.; to vocalism compare oijopyvupi), GTopswOpi 
(neologism), arpcbwupi (after arpwaai) 'bestreue, strecke hin; breite from; level, even ', 
Aeolic Perf. saropoTai; participlearpcjOTOc;; arpajpa n. 'Streu, lair, rug, cover', arpwijvri ds.; 
GTpaTOc; (= Old Indie strta-) 'troop, multitude, crowd, Volksmenge' (Cretan aTapT6(; with 
metathesis 'eine Unterabteilung the Phyle'), then ' army ' (in addition arpaTia, arpaTsia, 
aTpaTr|Y6(;), Aeolic arpoToc;; zero grade arspvov 'breast' ('ausgebreitete surface, plain, 
area'; compare Old High German 5///77a 'forehead', reduced-grade Old Indie stTrna-, cymr. 
sarn, and ograde Old Church Slavic strana); 

alb. sMrinJ^bre\te from' {strnjo); sht/elay, place there, throw, cast, make eine 
Fehlgeburt' {*sterd)\ shtrofke^ cover, cave, nest'; 

Latin sterna, -e/ie 'scatter, strew, hinbreiten; niederstrecken', participle stratus 
{*sterat6s), afterwards Perf. stravf, prosternere {: S\aV\c prostbrq. Old \x\(ii\c pra-stara-); 
stramen ^ Streu' (: arpajpia; Old Indie star/man-); in addition with ^-Erweit. strages^6as 
NiederstiJrzen, Hinsinken, VerwiJstung' ('*Hingestrecktsein'), stragu/us ^zum About - or 
Unterbreiten helpful'; 

Old Irish se/77//77 'breite from' (= Latin sterno), cossa/r^be6' {*kom-stari- or stori-), fossair 
'Strohdecke' {*upo-stori-), s^e/^'strues' {*strta), s/ie/Z^'pratum'; from the heavy basis 
Middle Irish srath (tu-stem) 'beach, seaside, bank, border, shore, Talgrund' (not loanword; 
Latin loanword are but cymr. ys//'5o' 'valley', bret. stradle fond, I'endroit le plus bas'); 
cymr. s5/77 'stratum, pavimentum' {*sterano-, proto Celtic *starno- : Old Indie stTrna-); 

Old High German stirna^ Stirnd {*sternia). Old English s/eo/r?©^^ 'audacious'; 

Lithuanian straJa^mVr\ Stroh ausgelegter stall'; 

Old Church Slavic pro-sttrg -stret/ {russ. steretb) ' outspread ', prostran-b {*storno) 
'breit', strana^s\6e, region', russ. storona6s.; Old Church Slavic Old Russian etc. strojb 
'order', stroj/'t/ ^parare'; 



perhaps here the partly s-losen, auf a stem *(s)tr-eno-, *(s)trent-, (s)tron-t- based forms: 

Prussian-Lithuanian //'e'/7/s "region, place' (compare Old Church Slavic strana, proto 
Slavic *stor-na)\ Old Lithuanian //'(9/7/a 'place, region, line'; Old Irish //'e/(Gen. treoit) "herd' 
{*trento-)\ Old Icelandic strindi. "side, edge; land'; strgnd'edge, beach, seaside'. Old 
English strand, Late Middle High German strant{-d-). Modern High German Strand, Old 
Icelandic fer-strendr' rectangular '. 

B. extensions: 

stre-k-:Q\d English stregdan siem V. "strew, distribute, spray, allot' (Prasensbildung as 
bregdan); lengthened grade Old Church Slavic strekat/ ^pnck', ablaut. stroka^Kt\/ipo\/, 
GTiypia', Slavic *strbkat/"\n Czech strkat/" bump, poke', serb. stfcat/" spray'. 

streu-: Lat\n struo, -ere{struxi, structum \n\Vc\ analog. Guttural after verbs with i/from ^") 
"ijbereinander breiten, schichten, aufbauen', strues, stru/x^ heap, bulk, mass', Umbrian 
strugia "*struiculam'; 

abret. strou/s 'stra\/'\', nbret. streue/n 'stre\N, distribute'; 

Gothic straujan' strew, distribute', Norwegian str0ya. Old Icelandic s/ra "strew, 
distribute, outspread ', Old English stre(o)wian, stregan. Old High German streuwen, 
strouwen' strew, distributd; Old Icelandic strar\. "straw'. Old English streaw. Old High 
German stro. Modern High German Stroh, post-verbal Middle High German strou. Modern 
High German Streu, Germanic strava^pyre, stake zur Siegesfeier'; Old English streonr\. " 
richness, profit, gain, usury'. Old High German gi-striunir\. "profit, gain'. Old English 
s//7e/75/7 "acquire, produce '; Old High German g/'-str/unan '\ucrar\'. Middle High German 
s//7^/7e/7 "schnuppernd umherstreifen'. Modern High German Bavarian streunen ^ aHer 
Vorteilen umhersuchen'. Low German s//'^/7e"Gassendirne', actually "die 
Umherstreifende'; 

whether here serb. s//'c»i/c"herabgeschuttelte FriJchte', kroat. strova//t/" strew, distribute' 
and Old Church Slavic ostruiti, ostrujat/' destroy' ("*apart strew ')?? 

References: WP. II 638 ff., WH. II 590 f., Trautmann 287 f., 289, Vasmer 3, 20, 29. 
Page(s): 1029-1031
```


## [2026-09-14T03:09:39.823Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AHD steigh\"; grep -n \"^steigh\\|^steig-\\|^ster-\" AHD_watkins1985.txt | head -20",
 "description": "Grep AHD Watkins for roots"
}
```


### [2026-09-14T03:09:39.876Z] TOOL RESULT

```
=== AHD steigh
243:ster-3, 3. Oldest root from *oster- in Greek astér...
1004:steigh-
1010:steig-. To stick; pointed. Partly blended with stegh-. I. Zero-grade form *stig-. 1. Germanic suffixed form *stik-ilaz in Old English sticel, a prick, sting: STICKLE- BACK. 2. Suffixed form *stig-i- in Germanic *stikiz in Old English stice, a sting, prick: STITCH. 3. Germanic expres- sive form *stikk6n- in Old English sticca, stick: sTICK. 4. Germanic blended variant *stekan in Middle Dutch steken (> Dutch steken), to stick, stab: (ETIQUETTE), TICKET; SNICKERSNEE. 5. Nasalized form “sti-n-g- in Latin stinguere, to quench, perhaps originally to prick, and its apparent derivative distinguere, to separate (semantic transitions obscure): DISTINGUISH, EXTIN- GUISH, INSTINCT. 6. Suffixed form *stig-yo- in Greek stizein, to prick, tattoo: STIGMA; ASTIGMATISM. 7. Suf- fixed reduced form “*tig-ro- in Old Persian tigra-, sharp, pointed, and Avestan fighri-, arrow, in Greek tigris, tiger (from its stripes): TIGER. II. Basic form *séeig- in Latin -stigdre, to spur on, prod, in instigdre, to urge: INSTI- GATE. III. Suffixed o-grade form *stoig-d- in Germanic *staikd in Old Norse steik, roast, steak, and steikja, to roast (on a spit): STEAK. [Pok. steig- 1016.]
1011:steigh-. To stride, step, rise. I. Basic form *steigh-. 1. Germanic *stigan in Old English stigan, to go up, rise: sty. 2. Germanic compound *stig-raipaz, “mount-rope” (*raipaz, rope; see rei-1), in Old English stigrdp, stirrup: STIRRUP. II. Zero-grade form *stigh-. 1. Germanic *sti- gila- in Old English stigel, series of steps: STILE!. 2. Suf- fixed form *stigh-to- in Germanic *stihtan, “to place on a step or base,” in Old English stiht/i)an, to settle, arrange:
1018:ster-2. Also stere-. To spread. I. Extended form *streu-. 1. Germanic suffixed form *streu-nam in Old English stréon, something gained, offspring: STRAIN?. 2. Latin struere, to pile up, construct: STRUCTURE; CONSTRUCT, DESTROY, INSTRUCT, OBSTRUCT, SUBSTRUCTION. 3. Zero-grade form *stru- in Latin industria, diligence, activity (endo-, within; see en): INDUSTRY. 4. Russian struga, deep place: SASTRUGA. 5. Germanic *strél6 in Old High German sirdla, arrow, lightning bolt (> German
1020:ster-*, Star. 1. Suffixed form “ster-s- in Germanic “ster- rén- in Old English steorra, star: STAR. 2. Suffixed form *stér-ld- in Latin stélla, star: STELLAR, STELLATE; CON- STELLATION. 3. Oldest root form “aster- in Greek astér, star, with its derivative astron, star, and possible com- pound astrapé, asteropé, lightning, twinkling (< “looking like a star”; Ops, stem op-, eye, appearance; see okw-): ASTER, ASTERIATED, ASTERISK, ASTERISM, ASTRAEA, ASTRAL, ASTRO-; ASTEROID, ASTRAPHOBIA, DISASTER, Sterope. 4, Iranian stem *s¢dr- in Persian sitareh, star: ESTHER. [Pok. 2. ster- 1027.]
1021:ster-4. To rob, steal. 1. Possibly dissimilated form in Germanic *ste/an in Old English stelan, to steal: STEAL. 2. Germanic derivative noun *stél-ithé (-ithd, abstract suffix) in Middle English stelth, stealth: STEALTH. 3. Ex- tended dissimilated form in Germanic frequentative *stalkon in Old English *stealcian, to move stealthily: STALK?. [Pok. 3. ster- 1028.]
1022:ster-5. Barren. Latin sterilis, unfruitful: STERILE. [Pok. 6. ster- 1031.]
```


## [2026-09-14T03:09:46.443Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '1011,1019p' AHD_watkins1985.txt",
 "description": "Print AHD steigh and ster-2"
}
```


### [2026-09-14T03:09:46.496Z] TOOL RESULT

```
steigh-. To stride, step, rise. I. Basic form *steigh-. 1. Germanic *stigan in Old English stigan, to go up, rise: sty. 2. Germanic compound *stig-raipaz, “mount-rope” (*raipaz, rope; see rei-1), in Old English stigrdp, stirrup: STIRRUP. II. Zero-grade form *stigh-. 1. Germanic *sti- gila- in Old English stigel, series of steps: STILE!. 2. Suf- fixed form *stigh-to- in Germanic *stihtan, “to place on a step or base,” in Old English stiht/i)an, to settle, arrange:
steip-
STICKLE. 3. Suffixed form *stigh-o- in Greek stikhos, row, line, line of verse: STICH; ACROSTIC, CADASTER, DISTICH, HEMISTICH, ORTHOSTICHOUS, STICHOMETRY, STICHO- MYTHIA. III. O-grade form *stoigh-. 1. Suffixed form *stoigh-ri- in Germanic *staigri in Old English stéger, stair, step: STAIR. 2. Greek stoikheion, shadow line, element: STOICHIOMETRY. [Pok. steigh- 1017.] steip-. To stick, compress. 1. Germanic *séifaz in: a. Old English séff, rigid, stiff: stirF; b. Dutch stip, tip, point: STIPPLE. 2. Latin stipes, post, tree trunk: STIPE, STIPES. 3. Suffixed form *steip-d- in Latin stipdre, to compress, stuff, pack: STEEVE!, STEVEDORE; CONSTIPATE. [Pok. stéib(h)- 1015.] stel-. To put, stand; with derivatives referring to a standing object or place. I. Basic form *stel-. 1. Suffixed form *stel-ni- in Germanic “*stilli- in Old English stile, quiet, fixed: sTILL’. 2. Suffixed form “stel-yo- in Greek stellein, to put in order, prepare, send, make compact (with o-grade and zero-grade forms sfol- and stal-): APOSTLE, DIASTOLE, EPISTLE, PERISTALSIS, SYSTALTIC. II. O-grade form *stol-. 1. Suffixed form *sfol-no- in Germanic *stalla- in: a. Old English steall, standing place, stable: STALL; FORESTALL; b. Old French estal, place: INSTALLMENT!; Cc. Old French estalon, stallion: STALLION; d. Old Italian stallo, stall: PEDESTAL; e. Me- dieval Latin stallum, stall: INSTALL; f. Germanic denomi- native *stalljan in Old High German stellen, to set, place: GESTALT. 2. Suffixed form stol-6n- in Latin stolé, branch, shoot: STOLON. 3. Suffixed form *stol-ido- in Latin stoli- dus, “firm-standing,” stupid: sTOLID. 4. Suffixed form *stol-d- in Greek stolé, garment, array, equipment: STOLE}, III. Zero-grade form “*stj-. 1. Suffixed form *stl-to- in Latin stultus, foolish (< “unmovable, unedu- cated”): STULTIFY. 2. Suffixed zero-grade form “st/-no- in Germanic *stullén- in Old High German stollo, post, support (> German Stolle, Stollen, stollen): sTOLLEN. 3. Suffixed zero-grade form *stal-nd- in Greek stélé, pillar: STELE. IV. Extended form “stelg- in Germanic *stalk- in Norwegian dialectal stalk, stalk, akin to the source of Middle English stalk(e), stalk: sTALK’. V. Ex- tended form *steld- in: a. Germanic *stiltjon- in Low German and Flemish sfilte, stick, akin to the source of Middle English stilte, crutch, stilt: sTILT; b. zero-grade form “*stld- in Germanic *stult-, “walking on stilts,” strutting, in Old French estout, stout: stout. [Pok. 3. stel- 1019.] stele-. To extend. Zero-grade form “*sélo-. 1. Suffixed form *stlo-to- in Latin /atus, broad, wide: LATITUDE; DILATE. 2. Attributed by some to this root (but more likely of obscure origin) is Latin /aémina, place, layer: LAMELLA, OMELET. [Pok. 2. stel- 1018.] sten-. Narrow. Suffixed form *sten-wo- in Greek stenos, narrow: STENO-, STENOSIS. [Pok. 2. sten- 1021.] (s)tene-. To thunder. 1. Zero-grade form *stno- in Ger- manic *thunaraz in: a. Old English thunor (genitive thunres), thunder, Thor: THUNDER; THURSDAY; b. Middle Dutch doner, donder (> Dutch donder), thun- der: BLUNDERBUSS, DUNDERHEAD; C. Old Norse Thorr (older form Thunarr), “thunder,” thunder god: THOR. 2. O-grade form *tona- in Latin tondre, to thunder: TORNADO; ASTONISH, DETONATE, STUN. [Pok. 1. (s)ten- 1021.] ster-'. Stiff. I. O-grade form *stor-. 1. Suffixed form *stor-é- in Germanic *staren in Old English sfarian, to stare: STARE. 2. Suffixed form *stor-g- in: a. Germanic *starkaz in Old English stearc, hard, severe: STARK; b. Germanic denominative *starkjan in Old English *stercan (> Middle English starchen), to stiffen: STARCH. II. Full-grade form *ster-. 1. Germanic *sternjaz in Old English stierne, styrne, firm: STERN}. 2. Suffixed form *ster-ewo- in Greek stereos, solid: STERE, STEREO-; CHOLESTEROL. 3. Lengthened-grade form *s¢ér- in Greek stérizein, to support: STERIGMA. III. Zero-grade form *str-. 1. Extended form *strg- in Germanic *sturkaz in
66
(s)teu-
Old English storc, stork (probably from the stiff move- ments of the bird): STORK. 2. Germanic *striit- in Old English striitian, to stand out stiffly: struT. IV. Extend- ed form *sterd-. 1.Germanic *stertaz in Old English steort, tail: REDSTART. 2. Germanic “*stert- in: a. Old English *styrtan, to leap up (< “move briskly, move stiffly”): start; b. Old English steartlian, to kick, strug- gle: STARTLE. V. Extended form *sterbh- in Germanic *sterban in Old English steorfan, to die (< “become rigid”): STARVE. VI. Extended form *(s)ierp- in suffixed (stative) zero-grade form *trp-é- in Latin torpére, to be
stiff: TORPEDO, TORPID, TORPOR. [Pok. 1. (s)ter- 1022.]
ster-2. Also stere-. To spread. I. Extended form *streu-. 1. Germanic suffixed form *streu-nam in Old English stréon, something gained, offspring: STRAIN?. 2. Latin struere, to pile up, construct: STRUCTURE; CONSTRUCT, DESTROY, INSTRUCT, OBSTRUCT, SUBSTRUCTION. 3. Zero-grade form *stru- in Latin industria, diligence, activity (endo-, within; see en): INDUSTRY. 4. Russian struga, deep place: SASTRUGA. 5. Germanic *strél6 in Old High German sirdla, arrow, lightning bolt (> German
Strahl, ray): BREMSSTRAHLUNG. II. O-grade extended form *strou-. 1. Suffixed form *strou-eyo- in Germanic *strawjan in: a. Old English stré(o)wian, to strew: STREW; b. Old High German strouwen, strowwen, to sprinkle, strew: STREUSEL. 2. Suffixed form *strow-o in Germanic *strawam, “that which is scattered,” in Old English stréaw, straw: sTRAW. III. Basic forms *ster-, *stero-. 1. Nasalized form *ster-n-a in Latin sternere (past participle strdtus from zero-grade *stro-to-), to stretch, extend: STRATUS, STREET; CONSTERNATE, SUB- STRATUM. 2. Suffixed form *ster-no- in Greek sternon, breast, breastbone: STERNUM. IV. Zero-grade form *str-, stra-. 1. Suffixed form “str-to- in Greek stratos, multi- tude, army, expedition: STRATAGEM; STRATOCRACY. 2. Suffixed form *stro-to- becoming Celtic s(t/rato- in Scottish Gaelic srath, a wide river valley: STRATH. 3. Suf- fixed extended form *stro-mn in Greek stréma, mattress, bed: STROMA; STROMATOLITE. [Pok. 5. ster- 1029.]
```


## [2026-09-14T03:10:04.913Z] TOOL CALL #16: Bash

```json
{
 "command": "pdftoppm -f 479 -l 479 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg479 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg479.png",
 "description": "Render PDF page 479"
}
```


### [2026-09-14T03:10:06.719Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 94168 Sep 13 23:10 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg479.png
```


## [2026-09-14T03:10:08.207Z] TOOL CALL #17: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg479.png"
}
```


### [2026-09-14T03:10:09.006Z] TOOL RESULT

```

```


## [2026-09-14T03:10:09.003Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-14T03:10:37.650Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && mkdir -p ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg479.png ocr/BOOK/479.png && echo copied\necho \"=== KLN Sirat\"; grep -n -i \"sirat\\|Al Sirat\" KLN_1966.txt | head -20\necho \"=== KLN street\"; grep -n \"^street,\" KLN_1966.txt\necho \"=== KLN stray\"; grep -n \"^stray,\" KLN_1966.txt\necho \"=== KLN strata/stratum\"; grep -n \"^stratum,\\|^strata\\|^stratagem,\\|^strategy,\\|^stoichio\" KLN_1966.txt",
 "description": "Grep Klein for sirat, street, stray, strata"
}
```


### [2026-09-14T03:10:38.794Z] TOOL RESULT

```
copied
=== KLN Sirat
2345:Al  Sirat,  n.,  in  the  Koran,  ‘the  right  way’  of  faith; the  narrow  bridge  leading  over  the  fire  of  hell (Islam).  —  Arab,  al-sirdt,  ‘the  road’,  fr.  al-, ‘the’,  and  sirat,  ‘road’,  fr.  Aram,  isfratd,  isrdtd, fr.  Late  Gk.  axpaxa,  fr.  L.  strata  (scil.  via),  lit. ‘paved  way’.  See  street.
36995:stream  with  dimin.  suff.  -let. street,  n.  —  ME.  strete,  ‘paved  way’,  fr.  OE. street,  fr.  Late  L.  strata  (via),  ‘paved  way’,  fem. pp.  of  sternere,  ‘to  spread  out,  pave’.  Cp.  Pro¬ ven?.  estrada,  ‘street’,  OIr.  srath,  ‘valley’,  which are  of  the  same  origin.  For  the  etymology  of  L. sternere  see  stratum.  Cp.  estrade,  strath,  stray, ‘to  wander’,  Al  Sirat.
=== KLN street
=== KLN stray
36988:stray,  intr.  v.,  to  wander,  go  astray.  —  ME.  strai- en,  fr.  MF.  estraier,  v.,  ‘to  go  astray’,  fr.  OF.,  fr. OF.  estree,  ‘road’,  fr.  Late  L.  strata  (via),  ‘paved road’.  See  street.
36990:stray,  n.,  a  strayed  animal.  —  ME.,  fr.  AF.  stray, estray,  from  the  adjective  stray,  estray,  fr.  OF. estraier,  ‘wandering  stray,  lost’,  fr.  VL.  *stratd- rius,  lit.  ‘abandoned  on  the  road',  fr.  Late  L.  stra¬ ta  (via).  See  stray,  v.,  and  cp.  estray.
=== KLN strata/stratum
36965:stratagem,  n.,  artifice,  trick.  —  F.  stratageme,  fr. earlier  strattegeme,  fr.  L.  strategema,  ‘artifice, stratagem',  fr.  Gk.  oxpaxfjYYpx,  ‘the  act  of  a general,  piece  of  generalship,  stratagem’,  fr. CTTpaTT,Y£tv,  ‘to  be  a  general,  to  command’,  fr. <jxpax7)Y<$S-  See  strategy.  For  the  ending  of  Gk. <Txpax7]Yr)pa  see  stiff,  -ma.
36967:stratal,  adj.,  pertaining  to  strata.  —  Formed  with adj.  suff.  -al  fr.  L.  stratum.  See  stratum, strategic,  strategical,  adj.  —  F.  strategique,  fr.  Gk. aTpa-nr)Yix6i;,  ‘of,  or  pertaining  to,  a  general’, fr.  aTpa-ni)Y<k-  See  strategy  and  adj.  suff.  -ic, resp.  also  -al.
36969:strategy,  n.  —  F.  strategic,  fr,  Gk.  oxpaxTjYta, ‘office  of  a  general’,  fr.  axpaxTjytii;,  ‘strategus, general’,  lit.  ‘leader  of  the  army’,  compounded of  n~.pri.~Jtc,  ‘army’,  and  the  stem  of  fiyelv>  ‘to lead’.  For  the  first  element  see  stratum  and  cp. stradiot,  for  the  second  see  agent,  adj. strath,  n.,  a  wide  river  valley.  —  Gael,  srath,  ‘val¬ ley’,  fr.  OIr.  srath,  of  s.m.,  fr.  L.  strata  (via), ‘paved  way’,  fem.  pp.  of  sternere,  ‘to  spread  out’. See  street.
36982:stratum,  n.,  a  horizontal  layer.  —  L.  stratum, ‘bed,  covering,  blanket’,  prop,  ‘something spread  out’,  pp.  of  sternere,  ‘to  spread  out, stretch  out;  to  scatter;  to  cover’,  which  is  rel.  to stramen,  ‘straw’,  lit.  ‘that  which  is  spread  out’, struere,  ‘to  put  together,  construct’,  fr.  l.-E. base  *ster-,  *stor-,  *str-,  ‘to  spread  out,  extend, strew’,  whence  also  OI.  strnati,  strnSti,  starati, ‘strews,  scatters’,  sfitah,  stirnafi,  ‘spread  out’, stariman-,  ‘spreading  out,  extension’,  Avestic star-,  ‘to  spread  out,  stretch  out’,  Gk.  ctxop- vuvou,  axopevvuvat,  crxpwvvuvai,  ‘to  spread out’,  ox£pvov,  ‘breast,  chest’,  axpeopa,  ‘bed¬ clothes,  mattress’,  axpax6?,  ‘army’  (whence oxpaxtS,  ‘army,  company,  band’,  oxpaxeta, ‘expedition,  campaign),  lit,  ‘that  which  is  spread out’,  Alb.  strih,  ‘I  spread  out’,  OSlav.  pro-stirg, pro-striti,  ‘to  spread  out’,  strana,  ‘side,  place,  re¬ gion’,  OIr.  sernim,  ‘I  spread  out’,  MLG.  sterne, OHG.  stirna,  MHG.  slirne,  G.  Stirn,  ‘forehead’, Goth,  straujan,  OE.  streowian,  streawian, strewian,  ‘to  strew,  scatter’.  Cp.  strew  and  words there  referred  to.  Cp.  also  sternum,  episternum, consternation,  construction,  destroy,  destruction, estrade,  prostrate,  straminous,  stratagem,  strat¬ egy,  stratus,  street,  stroma,  structure,  substra¬ tum,  Torilis.
```


## [2026-09-14T03:10:48.003Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport sys\ntxt=open('KLN_1966.txt',encoding='utf8',errors='replace').read()\nlines=txt.split('\\n')\ndef leaf_for(lineno):\n    upto='\\n'.join(lines[:lineno])\n    return upto.count('\\f')\nfor ln in [2345,36995,36988,36965,36969,36982]:\n    print(ln, 'leaf', leaf_for(ln))\nEOF",
 "description": "Compute Klein leaf numbers"
}
```


### [2026-09-14T03:10:49.330Z] TOOL RESULT

```
2345 leaf 41
36995 leaf 808
36988 leaf 808
36965 leaf 807
36969 leaf 807
36982 leaf 808
```


## [2026-09-14T03:11:00.161Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==809' KLN_1966.txt | head -5; echo \"--- leaf 775 ---\"; awk 'BEGIN{RS=\"\\f\"} NR==776' KLN_1966.txt | head -5; echo \"--- leaf 776 ---\"; awk 'BEGIN{RS=\"\\f\"} NR==777' KLN_1966.txt | head -5",
 "description": "Inspect Klein leaves for page numbers"
}
```


### [2026-09-14T03:11:01.205Z] TOOL RESULT

```
  the  form  of  a  stratum.  — Compounded  of  strati-  and  L.  forma,  ‘form, shape’.  See  form,  n.
stratify,  tr.  v.,  to  form  in  strata.  —  F.  stratifier, fr.  ML.  stratificare,  ‘to  form  strata’.  See  strati- and  -fy.
Derivatives:  stratifi-ed,  adj.,  stratifi-er,  n. stratigraphy,  n.,  description  of  the  arrangement of  strata.  —  A  hybrid  coined  fr.  L.  stratum,  ‘a covering’,  Gk.  -Ypx9ta,  fr.  ypxtpeiv,  ‘to  write’. See  -graphy.
Derivatives:  stratigraph-ic,  stratigraph-ic-al, adjs.,  stratigraph-ic-al-ly,  adv.,  stratigraph-ist,  n. Stratiomyiidae,  n.  pi.,  the  family  of  soldier  flies ( zool .)  —  ModL.,  formed  with  suff.  -idae  fr.  Gk. axpaxteox-r)?,  ‘soldier’,  and  (tuix,  ‘fly’.  See strategy  and  myo-.
Stratiotes,  n.,  a  genus  of  plants  of  the  family Hydrocharitaceae  ( bot .)  —  ModL.,  fr.  Gk. axpaxtcii xr,q,  ‘soldier,  yarrow,  milfoil’.  See strategy  and  cp.  stradiot. strato-,  combining  form  meaning  ‘stratus- shaped’.  —  See  stratus.
--- leaf 775 ---
  fr.  Du.  slof  ‘careless’, and  ME.  suff.  -ein,  -eyn,  fr.  OF.  -ain,  fr.  L.  -anus (see  -an).
Derivatives:  sloven-ly,  adj.,  sloven-!i-ness,  n. Slovene,  n.,  one  of  the  Slav  people  inhabiting Carinthia  and  Styria;  adj.,  of  Slovenia.  —  G. Slowene,  fr.  the  people’s  own  name,  orig.  mean¬ ing  ‘Slav’.  See  Slav  and  cp.  Slovak.  Cp.  also Slavonian.
smectite
Derivatives:  Sloven-ian,  adj.  and  n. slow,  adj.  —  ME.  slow ,  fr.  earlier  slaw,  fr.  OE. slaw ,  which  is  rel.  to  OS.  sleu,  ‘blunt,  dull’, MDu.  slee,  sleu,  sleeu,  Du.  slee,  sleeuw,  ‘sour, tart,  blunt’,  OHG.  sleo,  ‘blunt,  dull’,  ON.  sljor, slier ,  Dan.  slov,  Swed.  slo,  of  s.m.;  not  cogn. with  L.  laevus,  ‘lefthand’.  Cp.  sloth.
Derivatives:  slow,  intr.  and  tr.  v.,  slow,  n.  and adv.,  slow-ish,  adj.,  slow-ly,  adv.,  slow-ness,  n. slowworm,  n.  —  ME.  slaworm,  slowurm,  fr.  OE. slawyrm.  The  first  element  of  this  compound  is rel.  to  OE.  sliw,  sleo,  ‘tench’,  fr.  I.-E.  base  *slei-, ‘slime,  slimy’.  See  slime  and  cp.  words  there  re¬ ferred  to.  For  the  second  element  see  worm.  E. slowworm  was  influenced  in  form  by  slow. sloyd,  sloid,  n.,  a  system  of  manual  training  devel¬ oped  in  Sweden.  —  Fr.  Swed.  slojd,  ‘skill,  dex¬ terity’,  which  corresponds  to  ON.  slsegd,  ‘sly¬ ness’.  See  sleight.
--- leaf 776 ---
(we)n,  G.  schmieren,  ‘to  smear’, and  to  OE.  smeoru,  smeru,  ‘fat,  grease’.  See smear,  n.
Derivatives:  smear-ed,  adj.,  smear-er,  n. smectic,  adj.,  purifying.  —  L.  smeclicus,  ‘cleans¬ ing’,  fr.  Gk.  opt^xTixog,  fr.  opujx to?,  verbal adj.  of  oiigyELv,  ‘to  cleanse’.  See  smegma  and -ic.
smectite,  n.,  a  claylike  mineral.  —  Gk.  opajxTig,
smee
snafu
```


## [2026-09-14T03:11:22.179Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\ntxt=open('KLN_1966.txt',encoding='utf8',errors='replace').read()\nleaves=txt.split('\\f')\nfor i in range(795,815):\n    nums=re.findall(r'(?m)^\\s*(\\d{3,4})\\s*$', leaves[i])\n    head=leaves[i].strip().split('\\n')[0][:40]\n    print(i, nums[:4], '|', head)\nEOF",
 "description": "Find printed page numbers in Klein leaves"
}
```


### [2026-09-14T03:11:23.341Z] TOOL RESULT

```
795 [] | ask’,  and  to  OE.  spurnan,  ‘to  kick
796 ['1501'] | quander,  tr.  v.  —  Of  uncertain  ori
797 ['1503'] | ��,  and  houder,  ‘holder’;  in¬ fluenc
798 ['1505'] | Formed  with adj.  suff.  -ate  fr.  L. 
799 ['1507'] | ��starboard’,  are  Teut.  loan  words. 
800 [] | ic  and  -ics.
801 [] | le  jack,  n.,  one  who  climbs  steepl
802 ['1513'] | afette,  etape,  staff,  stamp,  stamped
803 ['1514', '1515'] | there  referred,  to. sternutation,  n.,
804 [] | ystima.  For  the  ending  see  suff. -m
805 [] | f.  -ate  fr.  L.  stipula.  See  stipul
806 [] | ��.  See  foot, stomatous,  adj.,  havin
807 [] | nd  pp.  of  stave, stover,  n.,  provis
808 [] | the  form  of  a  stratum.  — Compounded
809 [] | nnel’,  cogn.  with  Du.  striem,  OHG. 
810 [] | l about’,  Strolch ,  ‘a  tramp,  vagabo
811 ['1529', '1531'] | n. Derivatives:  studi-ed,  adj.,  studi
812 [] | ,  ‘to  hasten, hurry”  (intr.),  Lett, 
813 ['1533'] | e  understanding  of  something not  exp
814 ['1534'] | L.  sub,  ‘under’,  and  Gk. 9pf)v,  ‘di
```


## [2026-09-14T03:11:33.376Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\ntxt=open('KLN_1966.txt',encoding='utf8',errors='replace').read()\nleaves=txt.split('\\f')\nfor i in range(36,48):\n    nums=re.findall(r'(?m)^\\s*(\\d{1,4})\\s*$', leaves[i])\n    head=leaves[i].strip().split('\\n')[0][:40]\n    print(i, nums[:5], '|', head)\nprint('=== leaf 41 text ===')\nprint(leaves[41][:1200])\nEOF",
 "description": "Locate Klein page number for Al Sirat"
}
```


### [2026-09-14T03:11:34.596Z] TOOL RESULT

```
36 ['46'] | trength,  power’.  See  Alexander, alcoh
37 ['49'] | read’.  For  the  ending  see  suff.  -i
38 ['50', '51'] | .  formed  fr.  Thes- sal.  Gk.  akKiY.c
39 ['52', '53'] | allegare,  ‘to  despatch,  com¬ mission,
40 ['54', '55'] | v.  —  OF.  aloter  (F.  alloter,  allot
41 [] | r.  L.  admorsus,  pp.  of  admordere, ‘
42 ['58', '59'] | tles  of  the  family  Chryso- melidae  
43 ['60', '61'] | I.-E.  *am-ro-, fr.  base  *am-,  ‘bitte
44 ['62', '63'] | like  food’.  Cp.  Arab.  * unbar  (pron
45 ['64', '65'] | ddle’,  fr.  on  (see  a-,  ‘on’),  and 
46 ['66'] | SpneXog,  ‘vine’,  and  elSos, ‘form,  s
47 ['67', '68'] | se  to  gape  idly  about’,  fr.  a, ‘to
=== leaf 41 text ===
r.  L.  admorsus,  pp.  of  admordere, ‘to  bite  into’,  fr.  ad-  and  mordere,  ‘to  bite’.  See mordant.
aimng,  also  algum,  n.,  a  tree  mentioned  in  the
Bible,  prob.  the  sandalwood  (the  first  form  oc¬ curs  I  Kings  10:11-12,  the  second  11  Chron. 2:7  and  9:10-11).  —  Heb.  almuggtm,  resp.  al- gummfm  (pi.).  The  singular  of  these  words  must be  almdgh,  resp.  algdm,  so  that  the  forms almug  and  algum  are  incorrect.  They  should  be replaced  by  almog,  resp.  algom. alnage,  n.,  measurement  by  the  ell.  —  OF.  aul- nage  (F.  aunage),  fr.  aulne,  ‘ell’,  fr.  Frankish *alina,  prop,  ‘forearm’,  which  is  rel.  to  OHG. elina,  OE.  eln,  ‘ell’.  See  ell  and  -age.
Derivative:  alnag-er.  n.
Alnus,  n.,  a  genus  of  plants;  the  alder  (hot.)  — L.  alnus,  cogn.  with  ON.  obi,  OE.  alor,  ‘alder’. See  alder.
alodial,  alodium,  n.  —  See  allodial,  allodium, aloe,  n.  —  L.  aloe,  fr.  Gk.  aX6r),  ‘aloe’,  prob. borrowed  fr.  Heb.  ahaltm,  ahaldth  (pi.),  which are  perhaps  borrowed  fr.  OI.  agaruh,  aguruh, ‘aloewood’,  these  latter  being  prob.  of  Dravid- ian  origin.  Cp.  agalloch. aloetic,  adj.  conta
```


## [2026-09-14T03:11:42.040Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== FVQ sirat\"; grep -n -i \"sira\\|ṣirā\\|Sirat\" FVQ.txt | head -20",
 "description": "Grep Jeffery for sirat"
}
```


### [2026-09-14T03:11:42.104Z] TOOL RESULT

```
=== FVQ sirat
351:Ibn Hisham. Sirat an-Nabi, ed. Wustenfeld. Gottingen, 18,58-1860.
```


## [2026-09-14T03:11:44.055Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==213' FVQ_pages.txt | head -60",
 "description": "Print FVQ page 195 (leaf 212)"
}
```


### [2026-09-14T03:11:45.122Z] TOOL RESULT

```
FOREIGN VOCABULARY OF THE QUR^AN 195
As used in the Qur'an, however, it seems to have a technical sense,
being used in the sing, only of Biblical characters, and in the plu.
as " the righteous ", and for this reason it has been thought that we
can detect the influence of the Heb.-Aram. p"H!S. Thus Fleischer,
KUinere Schriften, ii, 594, says : " Das Wort ist dem heb.-aram.
p'HJJ entlehnt, mit Verwandlung des Vocals der ersten Silbe in i
nach dem bekannten reinarabischen PuTi."
^^ *
In the O.T. p'HX means just, righteous, and is generally rendered
by SIKOUOS in the LXX. In the Rabbinic Xp'HS the sense of piety
becomes even more prominent arid it is used in a technical sense for
the pious, as in Succa, 45, b. It is precisely in this sense that Joseph,

Abraham, and Idris are called ^ *X^ } and the Virgin Mary <a^*X^ in
the Qur'an, and there can be little doubt that both the Arabic
and the Eth. ftJP/4* are of this Aram, origin. 1
(Sirdt).
Occurs some forty-five times, e.g. i, 5, 6 ; ii, 13G, 209, etc.
A Way.
The word is used only in a religious sense, usually with the adj.
, and though frequently used by Muhammad to indicate his own
preaching, it is also used of the teaching of Moses (xxxvii, 118) and
Jesus (iii, 44), and sometimes means the religious way of life in general
(cf. vii, 15).
The early Muslim authorities knew not what to make of the word.
They were not sure whether it was to be spelled J^l^u?, 1*1^, or
J01 j j, 2 and they were equally uncertain as to its gender, al-Akhfash
1 Cf. Horovitz, KU, 49 ; Vacca, El, iv, 402 ; Ahrens, Christliches, 19 ; Grimme,
ZA, xxvi, 162, thought it was of S. Arabian origin, and this may be supported by tho
occurrence of Y^lm = Siddiq (1) as a proper name in the inscription, Glaser, 265
( CIS, iv, No. 287), though the vocalization here may be adiq (Rossini, Glossarium,
222 ; cf. Hyckmans, Noms propres, i, 182, 269). The Phon. name ZuSv* may also
represent p^lS (Harris, Glossary, 141).
2 Vide Bagh. on i, 6, and Jawhari, sub voc.
```


## [2026-09-14T03:11:48.672Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==214' FVQ_pages.txt | head -45",
 "description": "Print FVQ page 196"
}
```


### [2026-09-14T03:11:49.741Z] TOOL RESULT

```
196 FOREIGN VOCABULARY OF THE QUR ? AN
propounding a theory that in the dialect of Hijaz it was fern, and in the
dialect of Tamim masc. Many of the early philologers recognized it
as a foreign word, as we learn from as-Suyuti, Itq, 322 ; Muzhir, i, 130 ;
Mutaw 9 50. They said it was Greek, and are right in so far as it was
from the Hellenized form of the Lat. strata that the word passed into
Aram, and thence into Arabic.
The word was doubtless first introduced by the Roman administra-
tion into Syria and the surrounding territory, so that strata became
arpdra (cf. Procopius, ii, 1), and thence Aram. JTfinBOK; K^DIO^;
NtD"ION ; N^BIO l ; Syr. UrA&l- 8 From Aram - Jt was an earl 7
borrowing into Arabic, being found in the early poetry. 3
(Sarh).
xxvii, 44 ; xxviii, 38 ; xl, 38.
Tower.
The Lexicographers were not very sure of its meaning. They
generally take it to mean a palace or some magnificent building
(Jawhari), or the name of a castle (TA, ii, 179), while some say it means
glass tiles J^yjP /V 4 ^^. All these explanations, however, seem
to be drawn from the Qur'anic material, and they do not explain
how the word can be derived from fj**-
Noldeke, Neue Beitrage, 51, pointed out that in all probability
the word is from Eth. KCH\ a room, sometimes used for templum,
sometimes for palatium, but as Dillmann, Lex, 1273, notes, always for
aedes altiores conspicuac. This is a much likelier origin than the Aram.
rP""l!5, which, though in the Targum to Jud. ix, 49, it means citadel
or fortified place, usually means a deep cavity in a rock, and is the
It is doubtful if the word
equivalent of Ar. ij*& not of *r- j*&*
1 Cf. Krauss, Griechische und lateiniwhe Lehnworter im Talmud, ii, 82, 413. A
parallel formation is tfll^TID (= IflT^tflltflD) = arpartwr^.
2 Of particular interest is the fact that in an eschatological sense it passed from
Aramaic into Pahlavi as )^)j srdt. Cf. Bailey in JRAS, 1934, p. 505.
3 Fraenkel, Vocab, 25 ; von Kremer, Ideen, 226, n. ; Dvorak, Fremdw, 26, 31, 76 ;
Vollers, ZDMO, 1, 614 ; Ii, 314.
4 Hoffmann, ZA, xi, 322. What Fraenkel, Fremdw, 237, means by JimST I know
not.
```


## [2026-09-14T03:11:55.225Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== TAD sirat\"; grep -n \"صراط\" TAD_pages.txt | head; echo \"=== TAD istuqus\"; grep -n \"سطقس\\|اسطق\\|إسطق\" TAD_pages.txt | head",
 "description": "Grep TAD for sirat and istuqus"
}
```


### [2026-09-14T03:11:55.311Z] TOOL RESULT

```
=== TAD sirat
1364: ‫لانيني ‪ )317( 5485‬مناه طريق مباطة فنقلت‬         ‫سراط وصراط وزراط‬
1692:                                               ‫صراط ‪ -‬راجع سراط‬
=== TAD istuqus
```


## [2026-09-14T03:11:58.699Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '1355,1375p' TAD_pages.txt; echo \"=== leaf?\"; python3 - <<'EOF'\ntxt=open('TAD_pages.txt',encoding='utf8',errors='replace').read()\nlines=txt.split('\\n')\nfor ln in [1364,1692]:\n    print(ln,'leaf',' '.join(lines[:ln]).count('\\f') if False else '\\n'.join(lines[:ln]).count('\\f'))\nEOF\ngrep -n \"\\[pdf page\" TAD_pages.txt | head -5",
 "description": "Inspect TAD sirat entry and locate leaf"
}
```


### [2026-09-14T03:11:59.816Z] TOOL RESULT

```
                          ‫‪6‬هو اقذة‬
                                 ‫سددذة وسفط ‏ فارسي “‪9‬سيد و‬
 ‫وهو مرنيحة فضة مصتولة كانت الستعمل‬          ‫سحنجل ‪ -‬لاتبني م‪6‬‬
      ‫ظ‬                              ‫كاالرخآءتقربلاع الزجاج عربيه الوذيلة‬
‫‪-‬نانيمعناه جلد مدبوغ وطواءا عاذ من ‪05‬م‪60‬ماتزكاة أيديمالجهد‬
                                                         ‫سختيان وو‬

                     ‫سادج وساذج وساده ‪ -‬فارسي « ساده » معناه بسيط‬
            ‫السدر ‪ -‬قصرالنمان ‏ فارمي «ه دير » أي ثلاث قبب‬
 ‫لانيني ‪ )317( 5485‬مناه طريق مباطة فنقلت‬         ‫سراط وصراط وزراط‬
             ‫الى الابطالة ‪802‬اة والى الحرمانية ©وهاة والى الانكليزية كك‬
 ‫لاف‏افريسية م«عراى »‪6‬أصله أشوري مركب من « شارو » أي‬
                                                   ‫ااي‬
                                                     ‫سر‬
‫ملك ومن « أو » أييدت فبكون معناه بايلتملك أقيصره ‪ .‬و« أو » في‬
                                               ‫التركة معناه بيث‬

                                                ‫‏(‪ )١‬وفصيحها اليتري'‬
                                 ‫ا‬
                                 ‫سه‬‫سا‬

=== leaf?
1364 leaf 37
1692 leaf 47
```


## [2026-09-14T03:12:06.487Z] TOOL CALL #28: Bash

```json
{
 "command": "timeout 300 python3 tools/ref_page.py TAD:3 --image 2>&1 | tail -40",
 "description": "Render TAD page 3"
}
```


### [2026-09-14T03:12:07.618Z] TOOL RESULT

```
no scan of TAD covers printed page 3 (see 'scans' in refs_online.json)
```


## [2026-09-14T03:12:10.571Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 6 7 8 9 10 11; do echo \"--- leaf $n ---\"; awk -v n=$((n+1)) 'BEGIN{RS=\"\\f\"} NR==n' TAD_pages.txt | head -25; done",
 "description": "Print early TAD leaves"
}
```


### [2026-09-14T03:12:11.519Z] TOOL RESULT

```
--- leaf 6 ---
‫معاه أخبار تارمحية وقد استعمابا العرب ععى‬           ‫اساطير ‏ بوناني ‪8‬‬
                                                            ‫خرافات وحكابات‬
                                     ‫استبرق ‪ -‬فارسي معناه الديباج الغديظ‬
                                   ‫اسرب ‪ -‬فارسي «سيرب» معناه رصاص‬
        ‫إسطيل واصطيل ‪ -‬لاتيني ‪#‬دااناطهاة معناه مأوى الخيل والدواب‬
‫خا لان | رانم كن من ‪ 807653‬أى ك كب وهلاةطه‪:‬ذا أُخذ وكان‬
 ‫الفلكيون القدماء يعرفون حركة الكوكب مبذه الآلة ويعينورن موضعه‬
                                                             ‫ويعيسون ارتقاعه‬

                       ‫يونالي تاواع ‪ 1015‬معئاه عنصر وأعيل‬     ‫ب‬
                                                                      ‫د‪5‬ي‬
                                                                        ‫‪95‬‬

                    ‫معتأد عله حربية وطائفة سفن‬      ‫اسطول ‪ 8-3‬وناني ‪8‬‬


‫ملدابةمرادفهمودوقابمة‬
                    ‫اسطوانة ‪ 5-3‬فارسي ‪ 0‬أستون « هماه دعامة وقوات ا‬


                                                            ‫ايضا فيالطبيعيات‬
‫نحري جسمه متخلخل‬          ‫اون‬
                            ‫و وه‬
                               ‫ينعصر‬
                                   ‫حه م‬
--- leaf 7 ---
 ‫إرفج ‪ -‬تعريب علتهة؛ الجرماني الذيمعناهحر" وهوالسشمعب غرني‬
‫جرمانيا الذي دوخ غاليا سنة ‪ 584‬ومماها داعمه؛ ‪,‬ععده‪ :‬فدخل هذا الاسمإلى‬
                                               ‫بلادنا إبان الهروب الصليبية‬
 ‫معمخورائط ب يوئاني ‪ 52114‬وهو اسملجار حامل الكرة الارضية‬        ‫طلس‬
                      ‫فارسي < أفراز‪ 6‬معناهمرتفععربيهطنف‬         ‫ار‬

 ‫إفسنتين ‏ ووناني دا غمزومج معناه لاذع وهو ثبات ورقهكورق الصعتر‬

                                                                 ‫راطم‬
                                ‫افندي ‪ -‬نري ‪ 0‬اذنذئ م‪6‬عتأة السداك‬

  ‫يك ‪ -‬في اللائينية دامه وفي اليونانية وامه معناه مائعوهو عصارة‬
                                                                 ‫الخشخاش‬
                                ‫ل‬
                                ‫قو‬‫تزن‬
                                    ‫اقة في اليونانية معاعه معناه و‬

‫اكسيحين س يونا مرك من ولودة أي حائض ومن مفعفه» أي واد‬
  ‫استياك ‪ -‬ايطالي معتاهداه معناه ممطوط في الأصل البوناني ويراد به حذاء‬
                                                    ‫مخصوف بالمادة الممعلوطة‬

  ‫امام يوناني ‪520‬هلة معناه غير مروض مرادفه السامور وهو عند‬
  ‫الاقدمين حجركر أمافيزماننافا كتشف انهعنصر الفح املمتباور ودليل ذلك‬
                                             ‫ان المغناطسلا بقدر على جدبه‬

--- leaf 8 ---
                             ‫|قنوم ارامية ‪ 9 72‬قَدُوما ‪ 4‬معناه الشخص‬
 ‫في الفارسية ل‪2‬نكر» وفىاليونانية اله عرببها المرساة والموجل‬           ‫اجر‬

 ‫جيل يوناني‪#‬وألعههدوع (إوتجيليون )معناه خير بشارة وبشرى فرح‬
‫(نكليس ) عريها الجرى‬
                   ‫نقليسوحتكلس ‪ -‬يوناني ‪59‬ا‪600‬ي» إ‬
                                                               ‫والثلقوالصباور‬
        ‫هنا أراعى « عرب » أايلغرب‬
                                ‫صلةلولك‬
                                      ‫أجتا‬
                                         ‫اوريا ‏ ايطالي ‪#‬مه‬
                                ‫اوضة ‪ -‬ري وله يشارف عدر‬
‫أوقة‪ 5‬في اللددينية ‪3‬ن وفي اليونانية ‪#‬أعاىتاه براد مهاجزاء من|ثنيعشر‬

              ‫معناه مربع وعربية اليحر البط‬      ‫داتع يوناني ‪56‬‬

‫اوكاريستيا واوخاريستيا يوناني ‪2‬ناوذوداءنظا معناه نعمة وشكر أحسن‬
                                                        ‫وبراد به القريان المقكدس‬
                     ‫‪,‬نصاغوجي ‪ -‬يوناني ‪ ©8808351‬معناه مدخل وتوطئة‬

 ‫ارشّونة وقونة ‪ -‬يوناني ‪ ©7001‬معناءصورة وشبه ومثال وكثال أما نصمة في‬


‫ايطالي قجلاعناا‪ 61‬معناه لغة نفوذ وفي الطب هوالبلنمالوبابي‬          ‫إيتفاونسا‬
                                                            ‫برادفه العزلة الصدرية‬
--- leaf 9 ---
                                    ‫‪5‬‬

                                 ‫درن »‪6‬‬

           ‫بايا في اللاتينية همهم وهو تضعيف أب مقلوبا أي بايا‬
‫(كوين‬
    ‫ل الارض ت‬   ‫كسا‬
                  ‫نلل‬‫بأبللى ‏ دعي اسمهابابللان الرب هناك بلب‬
                ‫« بابيلو » أيباالباله‬   ‫ووت‬
                                          ‫نيةحفب‬
                                               ‫مشور‬
                                                  ‫‏‪ 4:١‬أ)مافي الا‬
‫يابج ‏ فارسي « بابوش » معناه غطاء الرجل وهو داس يلبس في الرجل‬
                        ‫باور ‪. 7‬يطالي عنندمة؟ معناه مخار امدرفه بآخرة‬

‫بواتبم ‪ -‬فارسي « بابونه » وحهشيشة ذات زهر أصفر مكلل بأبيض‬
                                                              ‫يتداوى بها‬
‫بادزص جافاريق عركن من بادأي ضد وزهرأي سم وهو حجر نحمله‬
                                                                 ‫الدجالون‬
‫باديجان ‪ -‬في الفارسية « بادينجان »‪ 6‬نقل الى الاسبانية ‪2‬مئمعمه‪ 8‬ومنها‬
‫الى الافر نسية ‪#‬هنعروطناة ثاملى الايطالية ‪5‬ةنهده؛وم ويقال له في الايطالية‬
‫أيضا هسةتدداءه» و «داعنت في اليونانية معناه اسود فنظر بعضيم الى ظاهر لنظه‬
‫ففسره « بيض المان أو ابن الجنينة ‪ 4‬أما أصل هذا النبات فههنودي فيكون‬
                           ‫اسمه هندي أيضا ويقال له في العربية قهقب حدق‬
‫بارجة ‪ -‬ايطالي هنهعه‪ 1:‬وهو اسمطائر ماي سميت تلك السفينة باسمه‬
--- leaf 10 ---
                                 ‫م‬‫ميه‬
                                    ‫م ل‬




‫وممامدم أي قاس وهو‬
                 ‫مكب م‪6‬ن‪ 5008‬أي قل د‬
                                   ‫باروسيرت يوناني ر‬
                                           ‫تستعمل لنرقة قن الوا وطذعاه‬
‫بارون ‪ -‬ايطاني مهن أصله من لغة جرمانيا ااقديمة ةط ومعناه رجل‬
‫حر كان يتولى قدي أراضي الامراء اعا هو الآن لقب شرف دون الكونت‬
                                                       ‫وهوآخر الالقاب‬
           ‫باز وبازي ‪ -‬فارسي عر بيهالصقر والعقاب واللاعة والحياقية‬
                                                 ‫اسايق ب ينا‬
     ‫وني مه لتههطا معناهملكيوهو لقب لعرق في الذراع‬
  ‫جرل ومن شاه أي ماك وسلطان‬
                          ‫باشا‪ -‬فارسي مركب من باأي لدم و‬
  ‫| باشق ‏ فارسي « باشه » وهو طائر أصشر من العقاب مرادفه يؤيو وج‪1‬م‬
‫بال ايطالي دادم معناه رفش وعربيه قملب ‪:‬قلب به الارضللزراعةأما‬
                        ‫رويب ‪ 8:585‬الابطالي وهومجرفة منحلية '‬
                                                            ‫عفه‬
                                                              ‫تمر‬
                                                                ‫ال‬
‫بال وبالة ‏ لاتيني ‪806‬هلده مناه المستحم وفي اليونانية ‪20‬ئهاها وهو‬
--- leaf 11 ---
                                                              ‫عت ات‬


 ‫بأميا ‪ -‬نبات له قرون تطبخ أصله من أهريكا الحو ببة واسمه هناك هطتترمع‬
 ‫و ‪40362‬دمع وعرنوه ياميا لويتئوه ‪1‬اناء وأطل! أي غاذق إزجة وهو من قصيلة‬
                                                                                                                          ‫الخعامي‬

                                                        ‫‪-‬مي « بير ب»راد به هعنردي‬    ‫ار‬‫يفبر‬
                                                 ‫بيغاء ‏ أصل هذا الطائر من الهند واسمه هندي‬
                                 ‫موف المفسول‬
                                           ‫من‬‫لم‬
                                              ‫ايج‬
                                                ‫بت ‪ -‬فارسي ‪ 0‬بت © وهو نس‬
               ‫مول ‪ 0‬ايطالي وتامماءم معناه زيت الحجر والنفط يستخرج منه‬

                ‫وبراد بهترميل من حشسب‬                          ‫دن اليونانية نا‬                  ‫ايطالي ‪06‬‬             ‫بثية ب‬


                                                                   ‫نخت ‪ -‬فارسي « مخت ‪ 4‬معناه حظ‬
                                       ‫‪5‬‬           ‫‪5‬‬                              ‫‪5‬‬                 ‫‪1‬‬          ‫‪١‬‬             ‫‪8‬‏‬
                        ‫>‪ 2‬معئاه عطية وهد‪.‬ه واحسان‬                           ‫فارمي « محش‬                  ‫مخشيش ”' ‪-‬‬


                                                                       ‫‪ 3‬ك‪ 5‬فارسي ‪ 2‬بت» أي صم‬
```


## [2026-09-14T03:12:22.983Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== MON\"; grep -c . MON_part1.txt; grep -n \"اسطقس\\|أسطقس\\|اسطق\" MON_part1.txt | head; echo \"=== MON2\"; grep -n \"اسطقس\\|اسطق\" MON_part2.txt | head; echo \"=== BQT v1\"; grep -n \"اسطقس\\|أسطقس\" BQT_v1_pages.txt | head",
 "description": "Grep Mo'in and Borhan for ostoqos"
}
```


### [2026-09-14T03:12:23.113Z] TOOL RESULT

```
=== MON
78085
2293:اسطقس» چهار آخشیج (عناصر اربعه). (فا.) 
12788:اسطقس ۰ (0500705)5 آمعر. محر. عنصر و 
12793:دوام چیزها است؛ ج. اسطقسات. 
12794:اسطقسات: 05۱0۳۵5۵-۱ [معر . بو. ع.] .( 
12795:ج. اسطقس. الف - مایه‌ها» مواد (اصلی). ب 
57484:رکن» اسطقس» اساس هر چیز (رسائل جابر که به وقت جماع از بینی و گلو برآید. 
=== MON2
50051:هبولی و اسطقس و ماده و حال را صورت 
=== BQT v1
3236:اسطر تو تاه اسقلینوس» اسطقس» اسطوخودوس » اغلیقی» غسیا» سالامندر|؛
```


## [2026-09-14T03:12:25.435Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '12784,12800p' MON_part1.txt; echo \"=== 2290\"; sed -n '2288,2296p' MON_part1.txt",
 "description": "Print Mo'in ostoqos entry"
}
```


### [2026-09-14T03:12:25.543Z] TOOL RESULT

```
(.) (نج.) ابزاری است که برای اندازه گیری 
موقع و ارتفاع ستارگان و دیگر امور فلکی 
بخار می‌رفت. 

اسطقس ۰ (0500705)5 آمعر. محر. عنصر و 
اصل ] (۱.) مایه» ماده» اصل هر چبز» مادة 
سجستین در و هبولی. عنصر های 
چهارگانه: آب و خاک و باد و آتش. 
استخوان‌بندی هر چیز» آنچه مایةٌ قوام و 
دوام چیزها است؛ ج. اسطقسات. 
اسطقسات: 05۱0۳۵5۵-۱ [معر . بو. ع.] .( 
ج. اسطقس. الف - مایه‌ها» مواد (اصلی). ب 
- عنصرهای نخستین هر چیزء عناصر اربعه. 
جَ اجرام سماوی. د علم هند سه. 
اسطوانه: (0-)05۱0۷2۵ [معر. ستون < 
استوانه ] (.) ور دنه تب رک نورد. 
اسطوره: (۵-)05۱۲۸ [ - اسطور - اسطاره» 
=== 2290
هنگام دست یافتن بر فراغت و آسایش» پس 
از رنج و ناراحتی گویند» آخه. کلمه‌ای است 
حاکی از درد یا ناخوشی. 

اخشیج: له [- آخشیک] (.) عنصر» 
اسطقس» چهار آخشیج (عناصر اربعه). (فا.) 
هیولی؛ سقة. صورت. صد»ه مخالف؟ ج.
```


## [2026-09-14T03:12:37.957Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT star\"; grep -n \"star-\\|staraiti\\|stərəta\\|vi-star\\|vī-star\" BRT.txt | head -30",
 "description": "Grep Bartholomae for star-"
}
```


### [2026-09-14T03:12:38.022Z] TOOL RESULT

```
=== BRT star
3984:•  j.  aiwyästar-  m.  'der  das  Bansman bündelt':  upa  tu  n6  'la  bansma . .  Yyt  2J.
5801:•  j.  astar-  m.  'Schleudercr,  Schütze',  mit Akk.  verbunden:  °ta  ilum  F.  7.
8554:•  j.  ustryamna-  Adj.,  PPM.:  s.  'star-.
9574:•  j.  kar«ma-  Adj.,  mit  star-  m.  'Stern-  y-6"i  136;  -  nairyain  kam.varAtJm  .. schnuppe"':  pairika  .  .  ya  slürä  -mJ  ^5  a/ffw^aira/ "/^w  YL  75.39;  — /«iW^am (NP.)  ^/tf«ft'  on/fl^j  a^w  asmanmca  "die  .J"?"'  *^q'iaili  (sd.)  upanhacat  ■'psm  V. y.  ...  die  als  Sternschnuppen  zwischen  /.9;"«y"«  aojishm  baväht  ya>a  'p^m Erde  und  Himmel  stürzen"  YLiy.S.  (statt  NS.)  Az.j.
12275:•  j.  tiätryo.star-   m.  'der   TiHrya    (ge- nannte) Stern':  yaihs  ainiis  brszaüi  yä^a
12993:j,  darstar-  m.  'der  erblickf.
13713:•  j.  dürae-darstar-  m.  'der  in  die  Feme ^ebt':  °ta  nama  ahmt  YLi.  12.
15155:•  g.  paity'i-star-  m-  'der  wiederholt,  durch Wiederholung  einschärft':  %wqm  atalSqm (näml.  vacaiikqm)  'tanmcä  fradoxstlrtmia dad^maidi  "dich  (Zar.)  bestellen  wir  als deren  Einschäifer  und  Lehrer"  Y.yj.  9'>.
15909:dizional, im  Nachsatz:  yö . .  tu^änatdiätm kl  *pära  p'  .  .  *astaraiti  (sd.)  N.p.
17805:•  j.  fra-varstar-  m.  'Bekenner  (des Glaubens)':  döai  anyaliqm  asaonqm  (nämL Jravaiis)  . .  yazäi  "ta  Yt  i.  30.
17930:Zum  V.  ^star-;  die  Bildung  ist  durch  da» Praes.  11  beeinflusst;  y^.  frtrintay-.  —  Pü.; ke  pa  an  i  an  r  dahm  pa  barsm  vistariaüh fräl  raset.
18486:•  j.  naenaestar-  m.  'der  eifrig  strebt nach  — ,  sich  bemüht  um  —'  (Gen.)'*:  kuma- tanqm  hüxtanam  kvar^lanqm  ..tnahl  aibi.- antärö  'tsrö  ya^ariä  voAunam  mahl  "wir
19272:•  j.  nisharstar-"  m.,  nisanharaSri-  f. 'der,  die  wacht  Über  -,  Acht  hat  auf  — ,
20269:Zu  sästar-,  eine  wertlose  Missbildung.
23548:•  g.  västar-  m.  'Hirte'  als  der,  der  für; Ndiiung  und  Sicherheit  der  anvertrauten Herde  sorgt:  yim  */fngui)-3  {sd.)  dadat Uarym  Y.27,13;  zit  /p.  I4i —  »^'^  "'*'■ •ta  xsmai  anyü  "ich  habe  keinen  andern  -■ Hirten  als  euch"  Y.  2g.  i.
25059:raS'aestar-
25082:•  j.  raö'ae-star-,  rad-ae-ätä-,  ra95i-ätä-'' m.  'Krieger,  Kriegsheld':  ya'ha  «j  taxmS °tä  (NS.)  Yt  13.  67;  —  taxmim  tusim  'ia- nm  Yt  5,  58;  Vyt  26;  —  mihnm  .  .  yim yaztnte  'tärS  Yt.  10.  \i;  j.  53  '> ;  —  mihrfm . .  laxiram  °tam  Yt  70.  140;  112,  25,  102; —  iraosahe  . .  taxmake  .  .  'ta  (GS.)  Y. 57-33;  —  ätari  spmta  'i3ra<yS.)^  Ny.j. 6;  Y.  ä^2.8Gl.  A)insbe3.alsBezeichnung für  den  zweiten,  den  Kriegerstand  (vgl.  unter 'piära-):  shrava  '/i  (NS.)  västryö /ü^qs Asitis'  Y.  ig.  ij;  11. 6,  Yt.i3.89,  V.5.  38, '^•45^i  —  ähravarum  ..'iär>nt  ..vasirJm fsuyantftn  Vr.^.  2;  Yt2, 12;  —  a%auru- naSca  °tüua  västrySica  fiitymte  Yt/p.  8; 7J.88,  V.5.  57,  58;  —  västry^Z  fsuyatas ..  'tä  (GS.)  ..  a'iiaurunS  Y.  13.21.;  — asti  iir  haim  (sd.)  ydha  'tärahe^l  Y.13. 44;  4Si  Vyt  J,  16,  Az.5;  —  vUpe  saya °%äis'ti  (LS.)  "alle  Ausrilstungsgegenstände für  einen  Krieger"  V.  74-9;  9;  —  '^^<»- urunqscä  -tascä  (AP.)  västryas^a  f/uyants Y.  7j.  3;  —  a^aurunqs^a  'tarSsla  (AP.)3) väitryqsca  fiuyants  Vr.^j,  5;  —  hast»ma alahe  ama  'ta  Y.13.2.
25097:•  j.  raJhöi&tä-  m.:  s.  imter  rdhaistar-.
25436:Aus  der  Fügung  'räilar>  (VS.)  vaiinlSÜ  'Ge- bieter, Leiter  dei  Festet'  hervorgegangen; vgl.  avartgav:  'rastar-  m-,  »om  ai.  V.  räjali ; vgl.  ai.  räffrd-  n.;  *vayjntT-{.  (iBild.  s.  Bthl, IF.  r.  300),  lu  ai.  väghät'i)  m.,  Ut.  vmei.  — 1)  Nicht  Titel,  vfic  West  SBE.  4/.  87  wilL  — »)  Nach  der  ^-Deklination.  —  »  Gdn.  VSt.  2. S4  'Priester',  MMüllek-Oldenberg  SBE.  ja. 46:  'suppliant,  worabipper,  iavoking,  sacri- ficer".
26236:•  j.,  g.  sästar-  m.  'Gebieter,  Machthaber, Fürst':  yoAmya  °tärS  aurva  .  .  Jrä  (sd.) rSsayaOe  Yt.io.  14;  —  ahurS  *'trmqm^^ dairihupaitis  Yt  i4-  37  i  —  ''o  äaitihius AamS^sa'^rff  Yt.  13.  18,  69,  Jj.  $a;  14.  13, t6. 19.  a)  bes.  von  Feinden  des maa^schen  Glaubens'':  nSit  mä  xMaus'.. naidä  dahySus  yöi  'tärö  dngvants  ". .  noch die  ungläubigen  Machthaber  des  Landes" Y.  4(f.  I.  a)  neben  as^maoya-:  yS aiimaoyS  anasava  yH  masyS  drvä  'ta  Y. Ö5.  8;  V.  2/.  I,  Yt.  J.  7,  10;  —  mahm drvantim  't  lr»m  .  .  ahmaoy^m  V.  4-  49  i —  tna^ehe  drvatö  '/arf  (GS.)  . .  asimao-jahe ¥.9.31;  —  asimaoya/ieca  .  .  'raheca^'' pouru.mahrkahe  Y.  16. 8,  61. 4.
26238:säslär,  erl.  (zu  V.  p) :  Me  apar  andahiht  4)  dät eslel,  (zu  Y.  16) :  lik  anäkih  . . ;  Sü. :  anyäyi, Npü. :  iikananda  kär  u  jiifJ #  (s.  dazu  Bakthe- 1.EMV  Gab.  S7)-  —  ')  So  die  lect.  diff.  in Ptl;  aus  ir.  ••^■f.äm,  %  36S.  39;  zSchr.  'Ira- nifrn  m  F  1  vgl.  ätravaxi'  neben  ätriv'  (sd., No.  1).  —  ')  Es  spielt  hier  vll,  ein  andres sästar-  rail,  das  zu  läJra-  gehört.  —  3)  Them.  — 4)  S.  tu  vayöi.
26597:•  j.  'Star-  V.  'stemere'.  Pracs.  i  star-^ 10  sttrtnu-,  1 1  slmnä- :  st>rm-  \,  1 1  +  ^5 sürvnaaa],  27  (Pass.)  'strya-.  —  PPfP. star^a-'^,  st^nta-;  PFP.  'statrya-;  Inf. *'st)rmti.         [S.  noch  "/rastaraityB^
26611:'star-
26623:•  j.,  p.  *star-  V,  'süDdigen'.    Praes,  4  b
26633:mit  ä  'sündigen,  sich  versündigen,  in den  Zustand  der  Sündigkeit  geraten;  sündig sein,  sich  im  Zustand  der  Süodigkeit  be- finden', Akt  und  Med.;  i)  absolut:  vlsatti (sd.)  ainyS  "usyS  null  ainyS  ^vlsimnö *äsiryäte  ava  ^vJsalte  (sd.)  *na^a.cil ästryeite  (in  pass.  Sinn  'non  pcccatur') P,57;  —  ya%a  .  .  äai^y^t  a^a  äsfryati "als  ob  er  ,  ,  so  versündigt  er  sich"  V. y.  zo;  —  aetavalla  aesasctt  *ästryäli^^ "und  in  solchem  Mass  macht  auch  er sich  sündig"  N. /2(?);  —  yalöil  (sd)  .  . asrävays  hyat  a^a  .  .  ästryaÜ  ",  .  bleibt er  im  Zustand  der  Sündigkeit"  N.  44',  — *ntsriti  (sd.)  aitahe  ästryeiti  mit  *'anisrili N.  II.  a)  Kaus.  'sündig  machen,  in den  Zustand  der  Sündigkeit  versetzen':; tiöit  asavarum  ainisHs  (sd.)  ästärayeiti\ P.12;  —  nsit  *asavan»m  *a/n)j?('/ (sd.)  1 ättäraiti  N,  log;  —  nStt  sp.bint5 ..  nasus nar?m  ndil  *äslärayaii  V.  5.  3 ;  "•'Nik.  2 ;  — AiaJ  aUai^qm  lyaoi^nanqm  (als  Subj.) astaraiti  "in  welchem  Mass  macht  solches Tun  sündig?"  V.  13.  20;  4.  5;  —  aha  tai "ä/rimnS  astärayäti  N.  12  (P);  —  mä äa/a  . .  *asläraila  Vyt_37(?).  2)  mit a)  Abi.  oder  Gen.  dessen,  an  dem,  b)  Instr, oder  Akk.  (des  Inhalts)  dessen,  womit man  sich  versündigt:  mit  ästryeiti  anyS^ ahmst  yS  kl  ''gaväsiryavans  N.  18;  —  nsil astqm  .  .  pairi.spaiti  (sd.)  apqm  ästrySnte V.  o,  2  9 ;  —  nasujpaSm  (sd.)  . .  astryante . . apasla  zimasca  urvarayasca  V.  6'.  3 ;  — fiBtl  gähanq/n  asruiti  ästryäti  N._50;  — yai  . .  anaiwiSfi  (sd.)  ästryäti  N.  i4\  ^4,
26634:3star-  1 598
26635:'3\  *^5<  ^5>  '8,  22;  —  rUli^  . .  anaiwiitlm ästryanti  N.  4;  —  yai  sS  *nisritim  frära (Sp.  185m.)  *ä  hl  *anisritlm  {staryäti) yeti . .  nSit  . .  frära  mii  *amsrrtlm  astryäte  . . *ahra  *a^ way aisAf m (sd.)  ..*ä  Ai*anisritlm staryäti  N.  10;  —  nsit  anaiwySsti  astrmti''^ N.p5;  —  ä  anaiwyasti strmti^  ^•95>  9^i —  :^araya  (sd.)  .  .  bäzujataya  .  .  yät^m ästryäti  N.  ^2^';  —  yattm  aslryäe  "er begeht  die  Z-Sünde"  F.^f.  a)  Kaus. *il  sl  ditn  aitalsqm  *bao6s.jaitii  astaraiti'''' "es  belastet  ihn  ihnen  gegenüber  die SUnde  ß."  N.  67.  3)  mit  Dat  incomm. : yaica  ,.  Aaine  ..  gar}7V}m  iri<yäii  ptfr>byö [Sp.  906  f,)  ästryäti  V.  15.  i  a.
26636:mit  para  und  ä  Kaus.  'J^^i^nd  (Akk.) einer  Sünde  (Instr.)  schuldig  machen': nabanaadiltitn  hl  para  ^pascaita  *raisaca *atwadäityaea  ''astaraiti''''  "seinen  nächsten Verwandten  macht  er  alsdann  der  Sünden R.  und  A.  schuldig"  N.5.
26639:•  j.,  g.  ^star-  m.  'Stern':  tainm  (sd.) httraihya  . .  yat . .  aiwits  urvisntti  staras- (NP.)'V'ä  mäsca  kvartla  Yt.  J2.  25;  V. '  2.  40;  —  slrfus{A2.)ca  mänhfmca  hvarna raocä  yazamaide  G.^.  6;  Y.  2.  11,  yi.<), Vtio.  145,  *V.  7.  52  (äs  Nom.)'>;  —  kuka . . yaosda'iäni . . ku%a  *strSus'* . . mänh>m . . hvart  V.  11.  \;  1  (als  Nom.),  10  (statt Abi.);  ~  kasnä  :^'Sng  *s/rfm(,GP.)äca  däl adväfam  (sd.)  Y.  44-  3 ;  —  ankam  (näml. fravasinqm)  raya  . .  hvan  . .  mh  . .  stärS ava  pdka  yänti  Yt.  i_j.  16;  FrBy.;  — fra- va^ayB  .  .  yä  strqm  mStthS  kür5  anayra- nqm  rao^anhqm  pa%S  dalsay»n~^\..i3.$T; V.l.  16;  —  Ääu  ma..  ave  stärö  V.9.41; Yt.  Ä  i;  —  tistrJm  ..yim  ratBm  ..vlspaisqm stärqm  Yt.  S.  44;  —  nittmalit  avaüqm stärqm  ya'ka  nars  malmyehe  va-^'hangm "selbst  die  kleinsten  jener  Sterne  (sind  so gross)  wie  der  Kopf  eines  mittelgrossen Manns"  'S. 4^;  —  ha(a  avaibyü  st>r^yS Ytj.  85;  —  slärqmia  sptntB.mainya'vanqm
26644:staramiyAs. Subj.)  bays.datanani {sd.J  ätwt.-     f^'"'''  ^*-  ^^^-  '■  *"■ rtucayänteN.ig.iy,  —  ttärä(VP.)*^ gu/ra   ■  j,  Starata-  Adj.,  PPfP.:  S.  'star-. aflB>:ra»hB    V.  21.  13;     —     vUpe    siärS       KompA.,  E.
```


## [2026-09-14T03:12:44.348Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '26597,26625p' BRT.txt",
 "description": "Print Bartholomae star- entry region"
}
```


### [2026-09-14T03:12:44.406Z] TOOL RESULT

```
•  j.  'Star-  V.  'stemere'.  Pracs.  i  star-^ 10  sttrtnu-,  1 1  slmnä- :  st>rm-  \,  1 1  +  ^5 sürvnaaa],  27  (Pass.)  'strya-.  —  PPfP. star^a-'^,  st^nta-;  PFP.  'statrya-;  Inf. *'st)rmti.         [S.  noch  "/rastaraityB^
i)  'auseinander  breiten,  spreiten,  durch Spreiten  zurecht  machen':  yahmya  stari- tasca  gätus  anyäsca  bjnxhä  avanlä  Yl 17.  7;  —  ya'ka  nä  fryö  fryäi  vantaee startta  gätus  sayamanS  (ad.)  püinm  .  . avi  ava.baraiti  V.^.  35.  a)  als  Term, techn.  für  das  Spreiten  des  Barisman (s.  Sp.  948'*),  d.  i.  dessen  Zurechtmachen, Bereiten  durch  vorschrifismässiges  An-  und Aufeinanderlegen  der  einzelnen  Stengel {urvarS-,  Sp.  402  m.,    403  u.):    ti   (näml.
fravaSayS)  ..staritalsu  bansmdhu  saoyi Yt.  /^-  2  7 ;  —  gaota  . .  p^nnimia  bansma (sd.)  staränS  darrj»m^a  yasn»m  yazJnS Yt.  70. 138; — /rac'arätH  (sd.)  aiva  tnazda- yasna  barismatt  * sl>r>n»nti*^  N.  103;  — bansma  stinnaSa (OpL)^  V.  12. 2'*;  —  ima slar)tai^  (nämL  bansma)  tma  myasda (näml.  avaioayamahi)  Vi.  11.  3;  —  Aap/a /lanti  fiävaiia  bar?sma  "stsrmaHli  N. /02(?)s'.  a)  mit  Dat  comm.:  bansma
/a  shr»nay?n^^  airyä  äaiiihävö  pasäm  hl pacayin  Yl  8.  58.  2)  'niederwerfen,  zu
Boden  strecken':  s.  -stfr^ta-.  a)  Pass. 'erliegen',  mit  Dat.  des  wem?:  druxs  hl stintö"''  apa.dvarai  baUi  dali-S  'V.ig.2;
—  yimS . .  d!ul.manaAyai{sA.)ca  hS  sUntS nidarat  upairt  zqm  Yt.  iff.  34.
mit  ava  und  J  'zu  Boden  strecken'": 3aJ  ha  druxs  avästryeite  kamiit  vä  vaca- tfhqm  V.^,  13;  —  spmiayä  ärmatsU  dsi- ^r3bya  avästryala  mairyS  YL  /,  29.
mit  US  'atisstrccken':  >^»(  bä  na  :^a/h3oa ustryamnS*^  avanuhabdfmnS  (sd.)  a^?m staoiti  H.  7. 11.
mit  nl  'htnbreiien':  s.  rtistantö.:
mit  yrJ  dnwS.  I  a:  sraoüm  ..yS paairyB bansma  frastmnata  j*  Y.  5  7, 6 ;  —  yS bansmqn  *ft'ast»rmte'*''  (3S.)  haomqsca var^Ss{si.)ca  N.97;  *6o',  *soi';  —  ya'ha aitahe  (näml.  öansmanB)  fras^rmäiii aia  .  .  N.  70;  —yH  anu  ailqm  (Sp.  34  u.) bansma  ^frastirmie^''  ya^a  .  .  jäm3spS *frast3rmaita  (Praet)"'>  N.  8g;  —  %risum bansma  /rast»r>nuyä  Vt.  /2, 3 ;  —  imal bansma  hähajaohnm  haha.aiwyaahan»m asaya  frastar>t3m  Y.  2.  i;  4.\,  62.^, 7/.  23,  Vr.(/.2.  V.J.  15,  Ä14,  15.  Vytsj;
—  bansmana  asaya  fi-astarilahe  Vr. 10.  2;  —  frastirstat  paiti  barssrrun  V, 9.56,  A.4.5,  YL/o.  137,  7j.a,  Y.57.2;  — bansmanqmca  aÜaya  */rastfr»tanqm"^ Vr.  12. 3;  —  yö  urvarqm  (sd.)  [.  ,]  *Jra- stfnnte^^  ü.gS;  gS;  —  haxattnm  fra- stirftanqm  (näml.  urvaranqm)  bansmaine frastairyät  "tausend  spreitbare  (PSanzen- stengel)    soll    er    zum    B.    spreiten"    V.
ai.  stj-nAü,  sljTiiti,  släratc,  'slfiak;  np,  gMsiar- dan.  —  Pü.;  viilarlax,  vistarcnilan;  s.  noch No.  1-7,  12.  —  ')  In  der  Wunelülbe  dem ai.  slirnäh  entsprechend.  —  ')  Hds.  itirmti, Vä.:  vislarincnd.  —  i>  Them.  —  *)  PO.:  bandft 'er  bindet';  die  Pü.  zu  V.  /:;  ist  gana  jung.  — ,      i)    Pü.:   x'istanitiiA;     ta   N.  loa:    ka^t   hinä
dby  Google
»597
'star-
ku  fa    Aävan
raShä     iarim     viitarilnTA.    —
7)   Pa.   (fürs   Pass.};    aiSr
iilan.  —  8)  Pö. !  HJ  n  p  dm  iirüA.  —  9)  St««
*/raslitinle  (ar,  *pra-sfinlai)  erscheint  in  den
N,-Hds.  •slpriHli  N.  /O  I.St,    sonst  •slariiUi;
s.  No.  lo.  —    ■")  HAi. /tasiarm:  —    '•)  So
K  7  tt,  b.  —  ")  Fü.:  lOoo  pa  fräe  vislarünlh
barsm  /räf  e  vislarel.     Ich  nehme  das  PPfP.
im  Sinn  des  PFP.   Anders  Gdn.  SPreussAW.
ig.  130.
•  j.,  p.  *star-  V,  'süDdigen'.    Praes,  4  b
(Kaus.)  Ji3ra-'\   10  si^nnav-,  20  *starav-
(p.)'*,    27    starya-,    'strya-,    30    (Kaus.)
```


## [2026-09-14T03:12:57.189Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"vTstar\\|vistar\\|vi.star\\|vīstar\" BRT.txt | head -20; echo \"=== col near 26597\"; sed -n '26590,26597p' BRT.txt | cut -c1-120",
 "description": "Grep BRT for vi-star"
}
```


### [2026-09-14T03:12:57.267Z] TOOL RESULT

```
7620:•  j.  *»-vista-'*  Adj.  'nicht  erhalten,  em- pfangen'; nur  LP.  'so  dass  man  nichts (dafür)  erhält'  sva.  'ohne  En^elt':  _^iwr.7- TayS  ava  däirayim  dim  vaeniil*°tash'a^'> vindatum  nSil  *afayiJ  *vistarh'a  "wenn  er nur  eine  solche  (so  geringe)  Besoldung dafür  bewilligt,  dass  man  ihn  für  einen, der  olme  Entgelt  (Unterricht)  erhält,  an- sieht, nicht  eine  solche,  dass  es  gegen Entgelt  (zu  geschehen  scheint)"  Ü.iO.
17928:PFP.  zum  V.  'Jtor-.  —  Pü.:  hal  bartm  pa ahräiTA  fräl  vistarl.
17930:Zum  V.  ^star-;  die  Bildung  ist  durch  da» Praes.  11  beeinflusst;  y^.  frtrintay-.  —  Pü.; ke  pa  an  i  an  r  dahm  pa  barsm  vistariaüh fräl  raset.
18517:•  j.  naotairyäna-,  °y^a-  patr.  Adj.,  dnw. naotara-:  vistaurus{sA.)  yS  °ya/tsYt.^.'j6; —  vistarao/  °yanahe  Yt  J^.  102.
24390:•  j.  vi'starav-  m,  EN.  eines  iranischen Helden":  tarn  (näml.  andvlm)  yazata 'taurus  yS  naotairyqnd  upa  apim  yani VTtafiuhaitlm  ". .  V.,  der  Naotande  . ." Yt5.  76;  —  'taraos  naoiairyanake  alagn
26608:ai.  stj-nAü,  sljTiiti,  släratc,  'slfiak;  np,  gMsiar- dan.  —  Pü.;  viilarlax,  vistarcnilan;  s.  noch No.  1-7,  12.  —  ')  In  der  Wunelülbe  dem ai.  slirnäh  entsprechend.  —  ')  Hds.  itirmti, Vä.:  vislarincnd.  —  i>  Them.  —  *)  PO.:  bandft 'er  bindet';  die  Pü.  zu  V.  /:;  ist  gana  jung.  — ,      i)    Pü.:   x'istanitiiA;     ta   N.  loa:    ka^t   hinä
=== col near 26597
tayaaüä   hazafihaüa  us   mazäayasnanqm  \ vTsqm  tyanayal{%Ä.)cä  vivapaila  Y.  12.  i.     ' xaitfrä  1)  dow
zu  Jemands  (Dat.)  Preis  anheben': /rJ  */?| *staemaide"'^  .  .  *var3hüi  yasnasca  *vaA-' masca  N.  48.  3)  'si
u.  iläumi,  stuvanli,  stola  (iP.\  iluM,  t/ävönai, slaläli;  rap.  ästai/äti"\  sutüdan. —  PB.;  stäyi- t
•  g.  stavat-  Adj.,  PPA.:  s.  stav-  mit No.  5-
•  j.  stavana-  Adj.,  PPM.:  s.  stav-  mit No.  2.
KompE.
•  j,  stavak-  n.  'Dicke,  Stärke'. KompE.  —  Vgl.  slüta:  —  Pü.:  tahik.
•  j.  'Star-  V.  'stemere'.  Pracs.  i  star-^ 10  sttrtnu-,  1 1  slmnä- :  st>rm-  \,  1 1  +  ^5 sürvnaaa],  27
```


## [2026-09-14T03:13:09.097Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"gustardan\\|gustar\\|wistardan\\|wistarag\\|STAR\" CHEUNG.txt | head -30",
 "description": "Grep Cheung for star"
}
```


### [2026-09-14T03:13:09.148Z] TOOL RESULT

```
23823:Bal. pastark ‘saddle’ || (+ *ui-) NP gustardan/gustar- ‘to spread’ 
41060:gustardan/gustar-, 365
```


## [2026-09-14T03:13:11.053Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '23790,23870p' CHEUNG.txt",
 "description": "Print Cheung star entry"
}
```


### [2026-09-14T03:13:11.106Z] TOOL RESULT

```
*starH! ‘to spread’ 

*AVESTAN: YAV. star- (star-) ‘to spread’ || (+ *upa-) YAv. upastorona- ‘cover’ (Yt 
15.2, Yt 15.39) || + *us-) °?” || + *fra-) ‘to spread out’ || (+ *ni-) ‘to stretch, spread 
down’ = Liste: 63f. 

Pres. {1} nä-: IND. 3sg. YAv. storonäiti (N 102), med. 3pl. ? YAv. “°starante, OPT. 25р. ҮАУ. 
*frastoroniiá (Yt 12.3); Pres. {2} them. nà-: INJ. med. 3sg. YAv. storonata (Y 57.6), OPT. med. 3sg. them. 
Y Av. storonaeta (V 12.2), 3р1. YAv. steronaiion (Yt 8.58, Yt 14.50); Aor. athem.: OPT. 3sg. ҮАУ. 
frastairiiat (V 3.17); Partic.: aor. med. Y Av. starana- (Yt 10.138), Partic.: pres. pass. ? YAv. ustriiamna- 
(H 1.11), ҮАУ. starota- (Yt 13.27), nistaroto.spaiia- ‘with spread, laid down pillow’ (Yt 10.30). 0 On 
Y Av. starota-, see De Vaan 2003: 505; Hoffmann — Forssman: 90 f.. 

*MIDDLE PERSIAN: (+ *ui-) BMP wstl- /wistar-/ ‘to spread [intr.], BMP wst’lyh- 
/ wistarih-/ (pass. caus.) ‘to be dispersed, spread’ 

(+ *ui-) Pres.: IND. 3sg. BMP wstlyt /wistaréd/, 3pl. BMP wstlynd /wistarénd/; Partic.: perf. pass. BMP 
wstlt /wistard/, caus. BMP wst’It /wistard/; Pass.: pres. caus. 3sg. BMP wst’lyhyt /wistärihed/ 


*starH2 365 


*KHOTANESE: LKh. star- ‘to spread’ || (+ *upa-) OKh. bastarr- ‘to bestrew’ || (+ 
*pati-) LKh. pastar- ‘to strew? = SGS: 134, 94, 77 

*SOGDIAN: (+ *pari-) BSogd. prstr- ‘to spread’, BSogd. prstrn ‘rug’ 

Inf.: pret. BSogd. prstrty 

*CHORESMIAN: (+ *upa-) bstn- ‘to make flat, spread (evenly) = Samadi: 27 

*NWIR: (+ *abi- ?) NP bistar, Khuns. bistär ‘bed, mattress’ || (+ *upa- or *pari- ?) 
Bal. pastark ‘saddle’ || (+ *ui-) NP gustardan/gustar- ‘to spread’ 

*NEIR: Oss. I. steryn/sterd, D. (&)ster(n)un/&)stard ‘to spread out; to cover; to 
pave; to adorn’ || (+ *a-) Oss. I. astaeryn/astard, D. asterun/astard ‘to adorn (clothes, 
weapon); to pave (road, way); to cover (the roof)’ || (+ *upa-) Pash. brastan (f.) 
*coverlet, quilt’ (*upa-starani-, EVP: 16) 

*MISC: (+ *abi- ?) Par. wiranö ‘bedding’ 

*SANSKRIT: star ‘to spread out, extend, strew’ (RV+) = EWAia II: 756 

«PIE *sterH;- ‘to spread, extend’ = LIV: 597 f. | Pok.: 1029 f. 

*IE COGNATES: Gr. otdpvvp ‘I extend, strew out’, Lat. sternere/strätus, Olrish 


sernim, Alb. shtrinj ‘to spread’, etc. 
*REFERENCES: IIFL I: 297b; Abaev, Slovar’ I: 78; Narten 1967: 57 ff.; Abaev, Slovar’ III: 150 f.; Werba 
1997: 327 


*starH ‘to make/become stiff, rigid’ 

*AVESTAN: (+ *ham-) Y Av. ham.storot- ‘stiffening’ (Yt 18.2, rather ^ham.starot- ?) 
*MIDDLE PERSIAN: ВМР st’! /star/ ‘torpor, unconsciousness’, ВМР stit /stard/ 
‘knocked down, stunned’ 

*KHOTANESE: stiru ‘rigid, hard’ 

*NEIR: Oss. I. st’zlyn/st’zld ‘to die, starve’, Pash. stdray ‘tired, weary’. Ф The Oss. 
verb is not from *star as assumed in Cheung 2002: 226. As for the semantics, cf. 
Lith. stipti ‘to become stiff; to die, starve’. 

*MISC: Orm. stir(äy), stor ‘tired’ (< Pash.) 

0 See also *star!. 

«PIE *sterH;- ‘to make/become stiff’. 0 On the reconstruction with *H; (on account 
of the Gr. evidence) see Sihler 1995: 556. The presence of the laryngeal can also be 
deduced from the Lith. (with acute accent) and Germanic forms (-rr-, Lühr 1976: 
74). = LIV: 597 f. | Pok.: 1022 

*IE COGNATES: Gr. стеребс̧ ‘rigid, hard, stiff, solid’, Toch. B scire ‘hard, stiff, rigid’, 
Lith. stérti ‘to be petrified, stiff’, Goth. and-staurran ‘to be obstinate’, OHG starén, 


OE starian, Engl. to stare, NHG starren ‘to become stiff’, starr ‘stiff, rigid’, etc. 
*REFERENCES: EVP: 71; Fraenkel II: 902 f.; Nyberg II: 180; DKS: 433; NEVP: 77; Kluge 2002: 876
```


## [2026-09-14T03:13:22.615Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PHD\"; grep -n \"wistar\\|wistarag\\|xākistar\\|hākistar\\|xakistar\" PHD.txt PHD_mackenzie.txt | head -20; echo \"=== NYB\"; grep -n \"vistar\\|wistar\\|xākistar\\|āxtar\" NYB_vol2_glossary.txt | head -20",
 "description": "Grep MacKenzie and Nyberg"
}
```


### [2026-09-14T03:13:22.693Z] TOOL RESULT

```
=== PHD
PHD.txt:652:wihézagig or wistar(ag)
PHD.txt:653:~agig [-yk!] movable; intercalary (year). wihir- [whyl- | (M whwr-)] change. —išn: change. wimand [wymnd | = M] boundary, frontier, limit. ~ig, —6mand [-yk', 2wmnd] bounded, limited. *wiméhgén [wmyhkn! | M wymyh-] *shapely. wimustan [uwymwstn! | M wymrz- (< P)] spoil, destroy. win [wn'] vina, lute. wināh [zs | М zoyz)h, N gunàh] sin, crime. winahgar [wsk] | M wwhg’r, (N gunahhar)] sinner. ~ih: sinfulness. wināhīdan, wināh- [wn’s-ytn' | M wyn’h-] spoil, damage, destroy. ~išn: damage, destruction. winastag [wnstk'] spoilt, corrupt. windādan, wind- [HŠKHWN-tn' < А ME, V skh; wnd'tn! | M wynd'd, wynd-} find, obtain, acquire. ~išn: acquisition, earnings. ~ignig : findable. winjišk [zvxcšk! | N gunjišk, binjišk] sparrow. win(n)ārdan, win(n)àr- [wyx?7-tn' | M wyn’r-dn] order, fix, arrange. ~išn: arrangement. win(n)irdan [wynltn' | M wynyrdn) be arranged, established; stay. iwir [wyl | M wyyr] man, hero. *wir [wyl | M wyr-, N bir] memory, mind. *wir [wyl | N bir] thunderbolt. wirāstan, wirāy-, (P wirāz-) [wyl’stn', wyPd-, (wPc-) | M турі, tyr y-, (P wyr st, wyr!z-)] arrange, prepare, cultivate, restore. —jišn(ih): arrangement, preparation. wirég [wlyk! | N guréy] flight, escape. wiréxtan, wiréz- [OL YKWN-tn! < А У ‘rq; wlyhtn', wlyc- | P wryxt, N guréxtan, guréz-] flee, escape. wirdmandih [wy”wmndyh | M wyrwmndyy] memory. wirózag [*wiwck! | (P wrwe)] lightning. wis [wys | = M] village. wisandan, wisān- [ws’n-dn'] separate. —išn(ih): separation. wisay- (ws'd- | M wys’y-] rest. wisbed [wyspt! | M wysbyd] village headman. wisé [wsydy | (P wsyd), N gusë] despatch. ~ kardan: send, despatch. wisistan, wisin(n)- [wsstn', wsyn- | N gusistan, (gusil-)] break, split. wisp [wsp | M wysp] all, every. wispurdan, *wispar- [wspwltn'] tread, trample. wist [20; wyst! | = M, N bist] twenty. wistan, *wih- [SDYTWN-tn' < A V šdh; wstn'] shoot, throw. wistar(ag) [wsti(g) | N bistar] bedding, cover.
PHD.txt:654:wistardan 92 wizürdan
PHD.txt:655:wistardan, wistar- [wstl-tn! | N gustardan] spread. wistāx [wst??hw! | M wyst?h, N gustāx, bistāx] confident, bold. ~ih: confidence, boldness. wis [w(y)$ | M wyš, N gus] poison, venom, bile. wišād [SLYTWNt', Р! | M wid, N gušād] open, wide, loose. wišādan, *wišāy- [SLYTWN-tn! < A У šrh; wPtn! | M шурап, (wys?h-), N gušādan, gušāy-) open, loose, free. wišād-dar [.SL Y TWNt! BBA] hospitable. wišād-dwārišnīh [zP??! dzb?lšnyh) going about ‘open’, i.e. without kustīg, or šabīg. | wišān- [w®n- | = P] shake down. *wišāy-, v. wišādan. wiškar [zo£hl | N bisgar(d)] hunting-ground, wilderness. wiškīdan, wiškin(n)- [wfkytn!, wškn-] divide, separate. ~išn: separation. wiskofag [wskwpk' | N biškēfa] blossom. wiškuftan, wiSk6f- [vvškup-tn! | J guškuftn, gwškwß-] blossom; hatch. wišūb-, —išn(-īģ), v. wišuftan. wišoūmand [w%wmnd] poisonous, venomous. wišūdag [wiwtk' | (M ghwdg)] abortion, daevic creature. wišūdan [wswtn'] bear daevic offspring. wišuftan, wišūb- (zfwp-tn! | M wiwb-, N *gusuftan] disturb, destroy. ~isn: destruction. ~1&п16 : destructible. *wixSay- [whsd-} forgive, forbear. ~iSn(ih): forbearance. ~išnīg : forbearing. lwiyaban [20(у) р?п! | Р шуп, N bīābān] desert. *wiyābān [wyd’p’n'] astray, wandering; deluded. ~ih: delusion, deception. wiyaban|garih [wyd"Pnklyh] deception. ~ig [-vk'] wandering, itinerant. wiyāftan, *wiyüb- [wd ptn! | M wy’b-] open (the mouth). wiyan [wyd?n! | M wy’n, N giyān] tent. wiyiz- [wydwe-] loosen, undo. *wiyufs- [wdwps-] make merry. ~išn: merry-making. ~iìšnīg : merry. wizandag [wzndk'] quaking. wizandidan, wizand- [wznd-ytn'] tremble, quake. -išn: quaking. wizar [wc] | M wer] separation; explanation. wizārdan, wizār- [wel-tn' | M wyc'rd, wyc^r-, J bz?rd-, N guzardan] separate; explain, interpret; perform, fulfil, redeem. ~išn: decision; redemption.
PHD.txt:960:bedding wistar(ag).
PHD.txt:1423:cover (n.) wistar(ag).
PHD.txt:3788:spread atšāndan, wistardan.
PHD.txt:5152:[103] nasrušt pev NT ` wisistan nte \ wisp 0239 \ wispurdan wed 120354 wistāxīh ^C) ҮАУ тез wistāx AWAY 19351 wastār є, 19.35 | wastārīh PR t€351 wassadēn \ 095 \ wassad 19351 wastóhmag vs? ea» 1 wistan 1112.35 | wastar, wistar ` vw», wistar- aN Y€.35|
PHD.txt:5153:wastarag, wistarag nastaran wistardan Widadafs
PHD_mackenzie.txt:5376:wlhezagig                         91                        wistar(ag)
PHD_mackenzie.txt:5425:wistar(ag) [wstl(g) I N bistar] bedding, cover.
PHD_mackenzie.txt:5426:wistardan                        92                        wizardan
PHD_mackenzie.txt:5427:wistardan, wistar- [wstl~tnl I N gustardan] spread.
PHD_mackenzie.txt:6040:bedding wistar(ag).                         bitter taxI.
PHD_mackenzie.txt:6287:continent kiswar; v. Appendix (vi).          cover (n.) wistar(ag).
PHD_mackenzie.txt:7638: soul frawahr, fraward, griw, gyan,     spread afSandan, wistardan.
PHD_mackenzie.txt:9979:""fisn                      \ t"UCU\    wastar, wistar
PHD_mackenzie.txt:9982:                           .s-u CU\     wistar-                   -~l'Ut\
PHD_mackenzie.txt:9983:xwcst".n[              \\¥' rtflU ~ \   wastarag, wistarag        ~tcvl
PHD_mackenzie.txt:9986:                              \l"V\     wistardan                '\~t4W1
=== NYB
552:apaxš [’phs] changing one's mind, repent- ing 8311. — Paz. awäx$, but in SGV awaxša- dar and awaxši. Perhaps Paz. awāxš = apāxš represents the original form: < "apa-axši ‘having his eye (look) turned back’; as to "axši- cf s. v. bītaxš. apaxtar [’p’htl] 1. planet 1151; han i 7 ~ 7718-19.22, 7915-16 (cas. rect.); 62 7 ~-dn 7720; Gišan ~-dn 7919-20 (pl. cas. obl. as subj.); —-àn 1152. — 2. the north 12012, — Av. (79) apäztara- ‘northern’; MPrs ’b’zir; Paz. awāxtar; NP bāxtar ‘the west’ or ‘the east’.
2559:*mih(a)rg [mytlg; Vd. 21? mtlg] cloud, the sphere of the clouds 21”. — Existing in the sphere called in Av. mäna-, v.s. v. mänenak. -g is to be explained in the same way as in andarg, vastarg, vistarg, vazurg: the suff. -ka- was added directly to the stem (cf arišk, husk) and -k- voiced by contact with the preceding -r-; -tl- is no doubt the archaistic spelling -0r- for Milr -hr.; original form consequently *miür-ka > mihrg and then perhaps with secondary vowel miharg, cf *vazrka- > vazurg ete. Possibly derived from M36ra-, cf Yt. 109! where he is praised as the giver of rain; not identical with MTL? (for Prth MTR’) varan, FrP 1.
3533:2star torpor, unconsciousness 6072. — V. start, vistartan, visturtan.
3535:start [stlt'] knocked down, senseless, swooning 101. 542-610, 912-3, 10318, — Pt. of Av. (1595) lstar-: starata- or starata- (whence sturt, v. sturteh) ‘to spread, to disperse; to knock down’; Paz. stard; v. also vistartan, visturtan.
4018:vastarg [wstlg] clothes 41?-4-? [472° read vistarg]. — Av. (1385) vastra- ‘clothing’ ; inser. SM 1. 50 wstlg; Paz. vastarg, vastrg ; Mand. lw. bastirga.
4211:vistarg [wstlg] bed coverlet 47%. — < OIr *vi-star-ka-, v. the next w. and cf vastarg; Ps. wstly, NP bistar ‘bed, mat- tress’; Talm. lw. bystrq?, Telegdi 235.
4212:vistartan [wstltn'], visturtan [wstwltn'] vistar-, to spread 45% (-urt). 11119 (-artan); pass.: ka-š fratom frasm vistarthét when its (viz. the sun’s) first dawn is spread, shines forth 4418, — < vt-+star-, v. start; NP gustardan, -ridan; Verbum 206.
4326:x"arg [hwlg] consuming, of the fire: —-ē ātaxš 92°, with the same ending -é as in menöye, v. meno. — < *xvarka-, cf vastarg, vistarg, vitarg, vazurg, etc. Cf MPrth xwryndg or waryndg.
4997:apāxtara-: apāxtar
6430:awāxtar: apāxtar
7055:bāxtar: apāxtar
7073:bistar: vistarg
7183:gustardan, -ridan: vistar- tan
```


## [2026-09-14T03:13:33.165Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN leaf 226 (p.205)\"; awk 'BEGIN{RS=\"\\f\"} NR==227' HRN.txt | head -50",
 "description": "Print Horn page 205"
}
```


### [2026-09-14T03:13:34.192Z] TOOL RESULT

```
=== HRN leaf 226 (p.205)
- 205 -
919. gu^lr 'Hilfsmitter, guz^rden (Sahn. I, 61 Vers 519),
ffuzer, guzerden; vergl. näguztr.
Etwa "^viöarija-, vergl. skr. vi -r- i^car- 'ausführen,
vollführen'.
Hat mit reztr (No. 1084) nichts zu tun.
920. gustäx *kühn, frech', busta/ (nicht belegt), vergl.
usta/ (ebenfalls unbelegt).
aw. *vistaka', vergl. stax^'a-, phlv. sta^mak (Darme-
steter. Et. ir. 62)0; P^lv. v{i)stax (Mgn.), arm. LW.
vstah unverzagt'.
921. gtisterden ausbreiten', guster, vergl. blster (No. 218).
ai. vi -f- [/'sfar- ausbreiten'; phlv. v{i)siarta)i aus-
breiten*.
922. guMMen 'zerbrechen, trennen', Praes. gmihem^ gml
kerden Verabschieden, entlassen' (Öähn. I, 74 Vers 236),
pin '^''Di: Verstössen (Jer. 3, 8), vergl. gusll (Vullers),
gtisilänlden (Öähn. I, 88 Vers 494).
phlv. v{i)sastan (Bund.), v{i)sastakih (PPGl.).
Darmesteter, Et. ir. I, 84 hat das Wort auf eine
\/^*Qard' zurückgeführt, die neben ai. gar^, gpidti *zer-
brechen' auf iranischem Boden existirt haben müsse.
Bartholomae (briefl. Mitteilung) denkt an eine Ver-
mischung der beiden synonymen Wurzeln sk^heid- (aw.
sa^d-, hisidyäf; ai. dhed-, chindtti; bei. sindag, n. sinday,
Hübschmann, ZDM6. 44, 559) und k\er- (ai. ^c/r-,
Cfnäti). Ifp. gusisten wäre ap. *visistanaig (aus *«^z-
sid'tanaiy), dagegen gtisilem ap. *visardann (aus sar-
mit dem d von sid-). Er verweist dazu auf die
Wochenschr. f. klass. Phil., 1892 Sp. 397.
Der Inf. guslxten ist ganz unklar.
923. gusäden offnen , sich öffnen ; Praes. gusay-em,
gusüden, gusäyis (Öähn. I, 169 Vers 734).
phlv. v{i)sätan oflfnen'.
Darmesteter, Et. ir. I, 59 Note 3 nimmt als
Grundbedeutung von np. gvsäden sich freuen , indem
') An *v%8taxf'(i' hatten schon Fr. Müller, Kuhn und Schleiclier's
Beiträge V, 139 und Spiegel, Kommentar T, 64 gedacht.
```


## [2026-09-14T03:13:40.126Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"218\\. \\|bister\\|hâkister\\|/jäkister\\|ister \" HRN.txt | head -20; echo \"=== search xakistar\"; grep -n -i \"kister\\|kistar\\|Asche\" HRN.txt | head -20",
 "description": "Grep Horn for bister and xakistar"
}
```


### [2026-09-14T03:13:40.196Z] TOOL RESULT

```
307:sehen (pister steht auch in Südi's Hafizkommentar ed.
2283:218. hister Xager (Vis und Kämm S. 69 Vers 3); guster
2288:Da np. bister nicht *Kleid' bedeutet, so hat Fr.
9898:218. Dazu arDi. LW. pastar, Hübschmann, KZ. 26, 605.
11238:218. varöniand zweifelnd', varömandth 'Zweifel' (AW.-
11281:218. vem Talle .
13386:pister XIII.
=== search xakistar
191:Pamir- Dialekte Tomasche k. Ebenso habe ich das
723:yayn. astiato forti 'se reconcilier (Tomaschek, 746).
737:aw. ai. ä -f- [/'snä-, nur in der Bedeutung Vaschen' ;
898:wa/. sar. yan anders* (Tomaschek, Pämir-Dial. 817).
1032:und Tomaschek (Pamirdialekte, 806) vergleichen
1203:89. iiSnän Name einer zum Waschen gebrauchten Pflanze,
2245:(Tomaschek, 867, und nach ihm auch Geiger, Laut-
2407:sar. wao-am, wüd (vergl. Tomaschek, 850).
4085:aus t. qapnn*<i *fangen, erhaschen* entlehnt.— 99 —
4464:sar. xoin, siyn. soin 'blau, yidg. ayßin (Tomaschek,
5136:(Ausnahme: Tomaschek, S. 78()).
6596:stehen isolirt. Wenn man mit Tomaschek (Central-
6789:782. susten Vaschen', Praes. söy-em^),
6791:'waschen' (vergl. g. sustinUu neben sustmün) ; bei.
6798:södafj , n. sööay, sözay Vaschen, reinigen, baden-
6870:^) Schon Tomaschek, Centralasiat. Studien, II, 891 (wo auch
6930:aw. l^snClr, US snayaeta 'sich waschen'; ai. l^snä-,
6932:oss. t. nähi 'baden', d. a^snun^ t. a^snin 'waschen*
7462:Toniaschek, Painirdialokte S. 771, veigkM'cht aw.
8173:käfir. vatsala, si^n. botsöri 'Jährling' (Tomaschek,
```


## [2026-09-14T03:13:43.175Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '2283,2295p' HRN.txt; echo \"=== 9898 ctx\"; sed -n '9894,9900p' HRN.txt",
 "description": "Print Horn no. 218 bister"
}
```


### [2026-09-14T03:13:43.240Z] TOOL RESULT

```
218. hister Xager (Vis und Kämm S. 69 Vers 3); guster
(fehlt bei Vullers).
g. vistara 'Bett, Bettzeug .
vi-\- [/^star- 'ausbreiten, *vistarana-; vergl. gusf erden
(No. 921).
Da np. bister nicht *Kleid' bedeutet, so hat Fr.
Müller (WZKM. 4, 259) kein Recht, es — abgesehen
von der Nebenform guster — von aw. vastra- ab-
zuleiten.
219. besten 'binden', Praes. bend-em., bend,
ap. basta^ gebunden'; aw. [/"band- 'binden', banda^
'Band'; phlv. bastan, band; ai. [/"bandh- , badhndü,
bandhd",
=== 9898 ctx
210. Vergl. S. 197 Anm. 2.
216. Arm. LW. bazpayit *Sündensühnung aus ap. *bampaiiti'
(Hübschmann, Literar. Centrbl. 1892, Sp. 1627).
217. Kauk.-bergjüd. auch ves, mäz. res.- 257 —
218. Dazu arDi. LW. pastar, Hübschmann, KZ. 26, 605.
228. Vergl. auch servbun *Cypressenbaum (Sahn. I, 156
Vers 489, 160 Vers 561), /ärbun 'Teufelszwirn' (AM.
```


## [2026-09-14T03:13:48.512Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HUB\"; grep -n -i \"xakistar\\|hakistar\\|kistar\\|Asche\" HUB.txt | head -20; echo \"=== PHD ash\"; grep -n \"^ash\\|ashes\\|Asche\" PHD_mackenzie.txt | head",
 "description": "Grep Hübschmann and MacKenzie for ashes"
}
```


### [2026-09-14T03:13:48.583Z] TOOL RESULT

```
=== HUB
252:^rispin'* nach Biddulph, y^ispin^ nach Tomaschek, BB. 7, 203.
424:(vgl. zd. uS'Snd Vaschen* und wegen sn fiir sn : ap.
1104:Geiger jetzt afgh. mnjql reinigen, saubern, waschen'.
2796:'waschen = reinigen', pOkTza kardan, vgl. paz. sus-
2797:tan Vaschen, reinigen , bal. SOday Vaschen, reinigen,
2837:zu osset. axsnun^ axsjnn waschen, ptc. axsnadt, axsdd ?
3290:auch grpan, grapanak *Tasche*) '), wahrend phi. grtvpdn
3317:') 'Tasche* dfter = 'Busen des Kleides'.- ^.:^h
7095:wasche', inf. sustan, bal. sddag, nb. sdJJay (s. oben p. 79);
8311:§%r *Milch* = skr. kslra- ; sustan Vaschen H. 782 , oben
=== PHD ash
869:   i.ldurestar ['twrystl] ashes.
5980:ashamed sarmgen; be - pafSir-.           awaken wigriidan; v. (a) rouse.
5981:ashen adurestaren.                       awakening wigriisisn(ih).
5982:ashes adurestar.                         aware agah.
```


## [2026-09-14T03:14:06.629Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BQT v1 bestar\"; grep -n \"^بستر\\|بستر \" BQT_v1_pages.txt | head -10; echo; echo \"=== BQT v2 xakestar\"; grep -n \"خاکستر\" BQT_v2_pages.txt | head -10; echo; echo \"=== BQT v3 gostardan\"; grep -n \"گستردن\\|گستر \" incoming/BQT/BQT_v3_pages.txt | head -10",
 "description": "Grep Borhan-e Qate for the three Persian words"
}
```


### [2026-09-14T03:14:06.743Z] TOOL RESULT

```
=== BQT v1 bestar
2009:بستر لك فواق .ابوالمعانی:
19683:بستر ] هگ بر ارو سکون‌انی
19691:بستر دن » بروزن حلبردن »نع وکردن

=== BQT v2 xakestar
9304:        ‫|رك‪ :‬خاکستری‌درذیل)؛ کردی که یس ازسوختن چیزی‌بای ماندبرماد‪.‬‬                      ‫‪۳‬‏ ‪ ûtur‬یمعئی آشات‬
9306:        ‫‪-‬رنگه خاکستر ‪-‬‬
11391:     ‫خاکستری رنگ و شه (‪ )۲‬بجمل و بشتر در‬
11933: ‫وزر » خاکستر‬           ‫حز لر = بر وزن‬                   ‫‪۰‬‬    ‫رده‬    ‫شون‬       ‫و‬       ‫بالف کشنده‬    ‫و تحتافی‬     ‫هیم‬   ‫وکو‬
11939:‫خاکستر سرکین را میگوبند ‪ -‬وآش‌را یز‬
12990:‫و بضم اول بمعنی خاکستر ‪٩‬‏ ‪ -‬و بزبان گیلان‬                  ‫حل = بفتح اول و سکون ثانی » ‪?ee‬‏‬
24285:‫پمایكکند و خاکستر خواکروبه میبرد ‪- ۴‬‬
33110:   ‫آمده وبقولکایگر کلمةٌ اففانی ‪( 8۳۳3‬خاکستری‌رنگه) ازآ نجاناشی‌است «هوبشمان‪>۷۰۷‬ورك‪:‬‬
39081:                                           ‫ومد بنه‌اسءت ‪٩‬‏ ‪#.‬‬             ‫خاکستری بیاهی مابل‌هم هست و‪-‬اسب‌واسشس‬
39439:‫ویمعنی بام خانه هم هت ومطلق‌بلندیها را نیز‬            ‫غبوملع"نی دوم سور است که رنگ خاکستری‬

=== BQT v3 gostardan
45031:‏گستر ۴ = ‎ee‏ اول‌بروزن دختی؛بمعنی
```


## [2026-09-14T03:14:15.695Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\ndef leaf(path, lineno):\n    txt=open(path,encoding='utf8',errors='replace').read()\n    return '\\n'.join(txt.split('\\n')[:lineno]).count('\\f')\nprint('v1 19683 leaf', leaf('BQT_v1_pages.txt',19683), '-> p ~', leaf('BQT_v1_pages.txt',19683)-222)\nprint('v1 19691 leaf', leaf('BQT_v1_pages.txt',19691))\nprint('v2 9304 leaf', leaf('BQT_v2_pages.txt',9304), '-> p ~', leaf('BQT_v2_pages.txt',9304)+543)\nprint('v3 45031 leaf', leaf('incoming/BQT/BQT_v3_pages.txt',45031))\nEOF",
 "description": "Compute BQT leaves and printed pages"
}
```


### [2026-09-14T03:14:17.046Z] TOOL RESULT

```
v1 19683 leaf 498 -> p ~ 276
v1 19691 leaf 498
v2 9304 leaf 160 -> p ~ 703
v3 45031 leaf 612
```


## [2026-09-14T03:14:22.009Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== v1 leaf 498 (bestar) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==499' BQT_v1_pages.txt | sed -n '1,60p'",
 "description": "Print Borhan bestar page"
}
```


### [2026-09-14T03:14:22.898Z] TOOL RESULT

```
=== v1 leaf 498 (bestar) ===
بستان تم اول بروزن برهان » کلزار
و کلسان‌را کوشد , ومشفف بوستان هم‌هت كِ
و جابی‌را نیز کویند که میوه‌های‌خوشبوق‌در آنجا
همرسد .
پستان‌افرود - کلیات سرم‌رنگ
و بی‌بوی که آنرا تاج خروس وگل بوسف نز
کوبند . وصنی اسیرغمرا که‌طیمران باشد بستان
افروز.میگویند . و بجای فا بای فارسی‌هم آمده
است .
بستان یر | -
کوبند که باغبان باشد .
بستان‌شی لن - نام توابی است از
خوسیقی .
بستاو لك » بفتح واو بروزن گل مانند؛
زمين پشته پشته زاءکونندکه کنل و کردوه‌باشد
و زمی ناهموار را نیز کنتداند . ۶
سبتتع ع نم اول و سکون انی و فتح
فوقانی و جیم ما کن , معرب بتکه است وآن
صمقی بائد که کندر گویندش » و اب یکوند
بستر ] هگ بر ارو سکون‌انی
و فتح ثالث و رای می نفطه بالف کشیده و حای
باغ ببراش دهنده را
۳ رگ : سنوه.
۱ ۳۹
مفتوح بنزن و کاف زده » جمعتین لحاف و مالن
باشد » و یی چادرثبی را کنته‌اندکه بر زوی
نزالی پوشند -
بستر دن » بروزن حلبردن »نع وکردن
و باكساختن باشد ۴
لستر سهنف‌دو » کنابه ازآش
آرا بعر بی تار گویند: .
بستاث ح بضم اول بر وزن آردك » صمغ
درخت پسته است » و بعضی گویند کندر است >
وبعضی‌دیگر گوبتدصمفی است. مانند کندروبمربی
لبان خوانند 4
بسع - بر وزن بدرو درطای تنم
کرچك را گویند و ممرپ آن ستوق باشد -
وچریی رایز گفته‌اند که بدان ماست‌ر! بشورانند
و برهم زنند تا هسکه و دوغ از همجدا گردد .
بست‌و نك - کنابه از استعام وضط
و ربط باشد . ۶
لست وه » یکر اول و سکون .شانی »
بمعثی متوماست که ملول وتنگ آمدهپاشد ؟ .
سقّه ‏ بفتح اول بروزن دسته ۴ «حربر
منقش باشد که در لس تراباد و ک رکان سازندوآن
چنان است که حربر را در هت ی
هه . «سص رهم
باشد که
#9 4
است «نفی».
» لاه بکر اول . اوسنا » رگ
و0۷
متجمد کردن - پوستن ؛ ضد کشودن "
```


## [2026-09-14T03:14:30.206Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==161' BQT_v2_pages.txt | sed -n '1,70p'",
 "description": "Print Borhan xakestar page"
}
```


### [2026-09-14T03:14:31.182Z] TOOL RESULT

```
    ‫پا‬     ‫‪۵‬‬




‫‪۰‬‬   ‫با ذال نقطه دار‬       ‫=‬    ‫ذلبلان‬       ‫ځا‬                  ‫ازکسی است که ازیرای حصول بمتصود بکارهای‬
        ‫باشد ‪.‬‬    ‫لان‬
                    ‫جفراانهو‬
                           ‫کنابه ازجسد وقالب کا‬                 ‫سخت و حرفتپای پست قیامدمابد ‪ -‬کنوابه از‬
        ‫ن‬
        ‫وتزبر‬
            ‫خا رنف ‪ -‬بارای قرش‬                                          ‫مردم دقیق‌النظر وباريك بین هم هست ‪.‬‬
            ‫آبکند » بمعنی گرد وغبار باشد ‪.‬‬
 ‫خاك ز لگین ‪ -‬عارت از طلاست ‪-‬‬
‫ولقره را تبز گفته‌اند "‪ ۳‬و کنابه از کلزار ولالهزار‬                               ‫درد ‪.‬‬    ‫از جسد وقاب آدمی(‪)۱‬‬
                 ‫هم هست ‪ -‬وآدمی زاد را لىز کوبند‬
                                                                ‫خاله خسبه "‪ ۳‬بطمخای نقطه‌داروسکون‬
‫خاك ردن‪ -‬کنابه از جاروب کردن‬                                    ‫» پرنده ایست‬    ‫اند‬   ‫سین بی لاطه ر فت بای‬

                                                                       ‫سحرای ی که آبرا بفارسی چرز ‪ ۱‬ورک‬
                                                                 ‫تی‌چفرق‬
                                                                                                         ‫گونند ‪.‬‬
    ‫کشیده » تضمی باشدکه آلرا باکافور دچرشم‬                      ‫امحد بر وزن‬    ‫خا کد ارن؟ = با دال‬
‫کشند » و در عربی بزرالخمخم و بزرالجنه (‪)۲‬‬
                                                                ‫آشمان ‪ ۰‬مزبله راکوبند ‪ -‬کونابه ازدلیا وعالم‬
                                                ‫خوالند ‪.‬‬


‫آندار ‪ ۰‬ممعنی خاك ماشد است چه سار بمعنی‬
‫ماشد هم آهدم است‪-‬و کنابه از چیزی گرد! لود‬
                                                                                  ‫کنهابه از دلیا وعالم باشد ‪.‬‬
 ‫افتاده و درو ش‌ولامرادوخوار‬        ‫ومردم‬   ‫‪-‬‬    ‫هم هت‬          ‫خاکدان غرور» بمسنی خاکدان‬
                                                                               ‫و است که کنانه از دلبا باشد ‪.‬‬
 ‫را کیتزده‌اند‬        ‫وسی‬
                        ‫® ک‬         ‫نزد‬
                                      ‫ا نی‬
                                         ‫ی‬ ‫ور‬
                                            ‫کلیل‬
                                               ‫وذ‬
‫در صف لمال یعنی در کفش کن خانه‬                       ‫که‬

                                         ‫‪‎‬دنیشنب ‪* ٩‬‬                           ‫غروراست که کنابه از دیا باشد ‪۰‬‬


                         ‫)‪ (۱‬خم‪ : ۳‬بذر الخمخم ویترالحنه ‪.‬‬                   ‫(‪ .)۱‬خم‪ 1 ۳‬آدمی زاد و‬

                                 ‫ران (یسوند معان)‪.‬‬         ‫اك‬    ‫از ‪:‬‬   ‫‪۳‬‬          ‫چرز ‪.‬‬    ‫رك ‪:‬‬   ‫‪- ۱‬‬

    ‫‪۰‬‬    ‫اتصاف وشیاهت)‬        ‫سر ‪ ۰‬سود‬    ‫خاك ‪ +۳‬سار ( =‬    ‫¬‬     ‫‪۴‬‬         ‫خا=کشی («م‪. ).‬‬
                                                                                         ‫‪۴‬‬
               ‫زین محر قطرمای بمن خاکار بخش‪.‬‬                     ‫ایآ نکه ره ممشرب مقصود بردهای‬           ‫‪۵‬‬

    ‫« حافظط شبرازی ‪. ۹۸۱‬‬
           ‫بفرفةٌ خا کاری » کروهی از متصوفه که امروز لىز پیروانی دارد ‪.‬‬               ‫‪ - ۱‬یز منتسب‬



        ‫ت‪۳‬ر (قس‪ »:‬پهلوی ‪78158-70002‬‬    ‫ساك‬
                                         ‫ا‪:‬خ‬
                                           ‫٭ خااستر ‪ -‬بکسر سوم وفتح چهارم » از‬
        ‫(بپمدن معنی) « تاوادبا ‪> ۹۹۱‬ر)ماشزه‪( 7805-‬کستردن " باشیدن ؟ ) « اقا ‪ : ۱‬ص‪٩۱٩۱۲‬‏‬
        ‫|رك‪ :‬خاکستری‌درذیل)؛ کردی که یس ازسوختن چیزی‌بای ماندبرماد‪.‬‬                      ‫‪۳‬‏ ‪ ûtur‬یمعئی آشات‬

        ‫‪-‬رنگه خاکستر ‪-‬‬
                     ‫بخاکتر ب‬                   ‫وب‬
                                                 ‫ن‪.‬‬‫مارم‬
                                                      ‫خ*اکستری ‪ -‬بکر سوم فوتح چه‬
        ‫فریزندی وبرنی ‪ . 1۲8196625‬سلنزی (‪۱ .۵ « 14056625‬ص ‪ , ۵۹۲۰‬سمنانی ‪»1۲853۵۲‬‬
    ‫‪ ۲ . ۰4‬ص ‪ > > ۵۹۱‬کیلکی‬                       ‫و لاسگردی و شهمیرزادی ‪1‬‬                    ‫ورهن‬         ‫ری‬
                                                                                               ‫‪. xãkastari‬‬
```


## [2026-09-14T03:14:40.255Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==613' incoming/BQT/BQT_v3_pages.txt | sed -n '1,60p'",
 "description": "Print Borhan gostardan page"
}
```


### [2026-09-14T03:14:41.240Z] TOOL RESULT

```
[pdf page 613]
‎Clea”‏ ۱ » بنم اول ؛ بروزن وممنی
بستاج است که ‎ge‏ ادب و دلی و تند باشد ۴ .

‏گستاخ دست «کنابه از چابدست
وجلد و تندکار کننده باشد ۴ .

‏گستر ۴ = ‎ee‏ اول‌بروزن دختی؛بمعنی
پهن‌کننده و افرازنده باشد ‎٩‏ - و امرباین‌معنی
هم‌هت عنی پهن کن و بیفراز و ‎Merged‏
‏میاه وخار سفید را نیز گوبند .

‎Vo pal?‏ © فتح دال و سکون‌تون,
بععني پهن ‎OS‏ و فرو چیدن و فراز کردن
باشد .

‏گسترش ۷ ۰ بنم ارل و سکون آخر

‏که شین نقطه‌دار باشد , هرچیز راکه توان فرو

‎NAN

‏چید ‎oS uy‏ از دام وباط و فرش ۸ وامثال
آن

‏کته ‎٩‏ » بفتح اول‌بروزن ‎austen‏
‏مر کین باشد که فلا اسب و استر و خر وکاو
است .

‎Cire ‏نم اول و قتج‌ها‎ 5 re
‏محترم ۰ نام پسس نوذرین منوچهر است - و دام‎
‏پ سگژدهم نیز هست و او یکی ازپهلوانان‌ایران‎
MY ‏بود‎

‏گحتی ۰۱۳ بنتح اول بر وزن پستی »
بمعتی درشتی وزبولی و ازیبابی باشد ۶.۱۳

‏گسته مهار - کنابه از بی قبد

‏9 رکش و ستیزنده - وسخن ‎FH‏ و بسرخود

‏۱ - پهلوی ۷150۵1۷ ۰ ارمنی ع ۷5۸82 « تیب رکه ص ۲4۵ > , پارسی باستان
0(۵۷۵ :۷1502 ۵ > هوبتمان ‎gets ayy > Ave‏ ایا

‏۴ - باب و آتش ‎CES‏ در دوه گوبی

‏۴ - ره :کستردن.
1 - از +کستر ‎ge) Oot Cee)‏ مصدری) ,کتر + قس : پنتر. هندی

‎۰

‏۴ -رك : رشیدی.

‏ساب ه کتر .

‏سمندر است درآتش , در ‎OT‏ ماهی‌وال.
«ممزی ‎Sayles‏ ص 44۲ *.
8 - اسم فاعل مرخم :داد کستر»

‏باستان ‎Startvi‏ ( پهن کردن ) . پهلوی ‎Vilstartan‏ ( پپن کردن ) « اسعق ۰۹۲۱ .
```


## [2026-09-14T03:14:51.698Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SNS\"; grep -n -i \"vistar\\|wistar\\|star-\" SNS.txt | head -10; echo \"=== FFD pdf78 (p.73)\"; awk 'BEGIN{RS=\"\\f\"} NR==79' incoming/FFD/FFD_pages.txt | head -40",
 "description": "Grep SNS and print FFD page 73"
}
```


### [2026-09-14T03:14:52.730Z] TOOL RESULT

```
=== SNS
3923:i^^Sj^ii :ra0Oi-sta-, ratfag-ita-, ragaS-star-: L. 
4560:.(*+**) hamastarlr^Wi^. 1774) hamaSstar-, *« 
9841:• ir/YT-^ Ij-j-Ah J>»<l>>i*3:tistar-it: *>]&xmf» 
10706:!.P$ •(/Kk'fc. 1573)sastar- : i^tf-** sastar-:* 5 " 
10825:st'rg-.^fc (vKJ/b. 1598)strbhih: ^Sj** star-: fc- 
15188:.♦ajaJT.jja-S- vistard: *W» 
15194:, t/T tf .c-L^ s vistard fistfid: y»w-" ^'| 
15196:(*1«*A ■ *&) v'^^-j'j'^'j-J'J^tOvistarg: ^^» 
16153:datar:^^.*^, dStar-: /i- .( y&^j :Jj) .^--l^yT 
28378:sastar- 174/2 
=== FFD pdf78 (p.73)
[pdf page 79]
4۳ نفعلهای فارسی دری
شده است. 814 صورت ضعیف ريشهٌ ۶210 است.

«گسل» در فارسی دری مادهٌ مضارع «گسستن) است. در فارسی میانه مادةٌ مضارع

: اقا ملع آمده است و آن از ۷۷۹-۹18۵* ایرانی باستان آمده است. ۶104 از ادخال 8

پیش از آخرین صامت ريشه برای ساختن مادهٌ مضارع از ريشه به کار رفته است.

در فارسی دری «گسیخت» به جای «گسست» به کار رفته است.

گشادن, گشودن

گشاد < فارسی میانه ۴834 < ایرانی باستان ۷1-33-1۵*. برای 1۵ > آراست. ۷۷
پیشوند فعلی است. ۳3 صورت اصلی 3 است» « پس از ابه 5 بدل شده است. ريشة ۲3
به معنی «بستن» است. «گشود» در فارسی دری به قباس با «سرود»» «سرای» به وجود
آمده است.

گشای + فارسی میانه 152 < ایرانی باستان ۳-52-78*. # برای ساختن ماده از
ريشه به کار می‌رفته است.

گید(

گشت < فارسی میانه ۷251 < ایرانی باستان ۹279-12*. برای 1۵ -> آراست. ۷۷۸۲۲
صورت اصلی ۷۷279 است. 1 پیش از ۲ به 8بدل شده است. ‏ -

گرد + فارسی میانه ۷۷۵۲ < ایرانی باستان ۳:۵۳-۵*. برای 2 -> آرای,

گاشت. مادةٌ ماضی گاشتن» از ۷37۳-۲۵ آمده است. ۷371 صورت بالاندةٌ 8۶۲ است.

گشت. ()

گشت < پهلوی اشکانی 8281 < ایرانی باستان 8۵3-12*. برای 1۵ -> آراست. 8۵7
صورت اصلی 825 است» 2 پیش از + به 5بدل شده‌است.ريشةٌ 822 به‌معنی «گزیدن» است.

گز + فارسی میانه 822 < پهلوی اشکانی 82۵7 < ایرانی باستان 827-2" برای ۵ ->
آرای.
```


## [2026-09-14T03:14:57.356Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==78' incoming/FFD/FFD_pages.txt | head -40",
 "description": "Print FFD pdf page 78"
}
```


### [2026-09-14T03:14:58.412Z] TOOL RESULT

```
[pdf page 78]
ماده‌های ماضی و مضارع قارسی دری ۷۳
است. «گله» فارسی دری از 81188 فارسی میانه آمده است و 8128 از 874-42* فارسی
باستان. 874 صورت ضعیف ريش 8۵74 / 8720 است. 218 پسوند بوده است.
۱ گزاردن
گزارد + فارسی میانه ۷12274 < ایرانی باستان 3۳-1۵.-۷*. برای ۵ -> آراست. ۷:۱
پیشوند فعلی است. لَن صورت بالاندةٌ ريشهٌ 27 به معنی «حرکت کردن» است.
«(چریدن) از ریشهٌ 47 آمده است > چریدن.
گزار < فارسی میانه ۷1237 < ایرانی باستان 2۲-۵.-۷۷*. برای 2 > آرای.
گُزیدن
گُزید ج فارسی میانه ۷127۵ < ایرانی باستان ۶۷-6۲-1۵ برای ۵ > آراست. ۷
پیشوند فعلی است. آت صورت ضعیف ریشةٌ له به معنی «گزیدن» است.
گزین ج فارسی میانه ۷۵217 < ایرانی باستان ۹1-61-۵*. 120 نشانه‌ای بوده که برای
ساختن ماده مضارع از ريشه به کار می‌رفته است.
گزیدن
۰ کِ شت.+
گستردن
گسترد < فارسی میانه ۷181۵74 < ایرانی باستان ۴۷۷1-81۵۳-12. برای ۵ -> آراست. ۷1
پیشوند فعلی است. ريشهٌ 5187 به معنی «پاشیدن» است.
گستر < فارسی میانه ۷۷۶17 < ایرانی باستان ۷1-۹1۵۳-۵*. برای 2 -> آرای.
ا گسست < فارسی میانه ۷9181 < ایرانی باستان ۷:1-918-1۵*. برای 2 > آراست. ۷:1
؛ پیشوند فعلی است. 814 صورت اصلی ريشه به معنی «بریدن» است و 4 پیش از ]به بدل
```


## [2026-09-14T03:15:07.282Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\ntxt=open('SNS_pages.txt',encoding='utf8',errors='replace').read()\nimport re\nlines=txt.split('\\n')\n# find vistard occurrences in SNS_pages\nfor i,l in enumerate(lines):\n    if 'vistar' in l:\n        leaf='\\n'.join(lines[:i]).count('\\f')\n        print(i, leaf, l.strip()[:140])\nEOF",
 "description": "Locate vistar in SNS_pages"
}
```


### [2026-09-14T03:15:08.360Z] TOOL RESULT

```
10884 154 vistard:      *W»
10899 154 ,   t/T tf   .c-L^ vistard fistfid: y»w-"
10904 154 v'^^-j'j'^'j-J'J^tOvistarg:                        ^^»                  I    '>tf>W nasae              : {,       (Mir. Man. IIi,58)ns*w
15731 222 vidast 268/4                    vistard 273/20            vuhuxfiatr 262/5
15733 222 vehlg 199/1              vidastan 268/8                  vistard 5stSd 273/23      vuhuxsatr-gah 262/8
15734 222 vShlh 198/20             vidaxtag 267/20                 vistarg 273/24            vuzurg 225/2-270/6
```


## [2026-09-14T03:15:12.306Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '10880,10908p' SNS_pages.txt",
 "description": "Print SNS glossary vistard entries"
}
```


### [2026-09-14T03:15:12.358Z] TOOL RESULT

```
                                      .ajaJT.jja-S-

                            :^)-^Wvi + /"star :^o
                                         Y/T^ (TYA^ci^'
                                                 •
                                                         vistard:      *W»
                                                                T c** J^

                                                                                    1
                                                                                            H-O^'^.ciMw 'dj*: vSziSn:N§Y*WN, fa:** .w^l
                                                                                        ln.kti,/fcS 8j ,^ tf
                                                                                                 ,r /T
                                                                                                            <   o>jj*   -V) >,
                                                                                                                                 ^
                                                                                                                                          >,
                                                                                                                                              {
                                                                                                                                                  b6xt       :
                                                                                                                                                                 ^
                                                                                                                                                  ;^ (CtfP£\57)vivekti-

 ,   t/T tf   .c-L^ vistard fistfid: y»w-"
                        s                                        ^'|                                     >u-*»<«*»t«ttl. **(-,)                   :nasay/nasa:                    -0»i/-^*i
                                                                                                   Wnw.1,43)             ns-'h                    jJ*
                                                                                                                                               Uifr7>.1057)nasu-:fc_
         (*1«*A *&)
                    v'^^-j'j'^'j-J'J^tOvistarg:                        ^^»                  I    '>tf>W nasae              : {,       (Mir. Man. IIi,58)ns*w
                                                                                                                                                                :                     ^L
TV6
                                      Ul; ^r   — „-*- «*b «j'j                                                                                                o-tf.U; tf-^U             bb 6-A,                             TYf
```


## [2026-09-14T03:15:22.938Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== MON esteratezi\"; grep -n \"استراتژی\" MON_part1.txt MON_part2.txt | head -5; echo \"=== MON serat\"; grep -n \"^صراط\\|صراط:\" MON_part1.txt MON_part2.txt | head -5; grep -n \"صراط\" MON_part2.txt | head -5",
 "description": "Grep Mo'in for esteratezi and serat"
}
```


### [2026-09-14T03:15:23.043Z] TOOL RESULT

```
=== MON esteratezi
MON_part1.txt:11745:استراتژی: 2 (.) فن ادارة 
=== MON serat
MON_part1.txt:89339:صراط: 3۱ [ع.] (.) راه» طریق. صراط
```


## [2026-09-14T03:15:25.016Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '11740,11755p' MON_part1.txt; echo \"===\"; sed -n '89335,89345p' MON_part1.txt",
 "description": "Print Mo'in entries"
}
```


### [2026-09-14T03:15:25.100Z] TOOL RESULT

```
استذ کارات. 

استر: ۲ [- ستر؛ مربوط به اسب قس. 
قاطر ] (.) (جان.) قاطر . 

استراتژی: 2 (.) فن ادارة 
عملیات جنگی؛ دانش رهبری عملیات 
نظامی؛ سوق الجیش. 

استراتوسفر: ۲ گنت (.) (همو.) 
طبقه‌ای از جو (اتسمفر) که فوق ۱۰ ۷ ۱۲ 
کیلومتر قرار دارد و حرارت در آنجا 9 
ثابت است. 

اسستراحت: 1 [ع. . استر احه4 ] 
(مصل.) آسودن» آسایش جستن» آسودگی 
===


بی آمیغ. 

صراط: 3۱ [ع.] (.) راه» طریق. صراط 
مستقیم: : راه راست. 
صراف: له [ع.] (ص.) آنکه پول نیکك 
را از بد جدا کند؛ سره گرء نقاد ناقد. (ف.) 
کسی که به داد و ستد انواع پول پردازد. 
صیرفی. 
صرافت: :«۰56: (ع. صرافة] (امص.) شغل
```


## [2026-09-14T03:15:31.992Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KLN stoich\"; grep -n \"^stoichio\\|^stich,\\|^stitch,\\|^stair,\\|^straw,\\|^structure,\\|^industry,\" KLN_1966.txt",
 "description": "Grep Klein for stitch, stich, stair, straw"
}
```


### [2026-09-14T03:15:32.092Z] TOOL RESULT

```
=== KLN stoich
19240:industry,  n.  —  F.  industrie,  fr.  L.  industria,  ‘dili¬ gence,  industry’,  orig.  fern,  of  industrius,  ‘dili¬ gent,  industrious’,  used  as  a  noun,  fr.  OL.  in- dostruus,  lit.  ‘building  into',  fr.  indu,  ‘in’,  and struere,  ‘to  build,  erect’.  See  indigene  and structure.
36543:stair,  n. — ME.  steyer,  steir,  fr.  OE.  stseger,  fr.  *stdg- ir,  fr.  Teut.  base  *staig-,  *st'ig-,  corresponding to  I.-E.  *stigh-.  See  sty,  ‘to  ascend’, staith,  n.,  a  wharf.  —  ME.  stathe,  a  blend  of  OE. stsed,  ‘bank,  shore’,  and  ON.  stop,  ‘landing place’.  Both  these  words  are  rel.  to  OS.  stath, OFris.  sted,  OHG.  stad,  stado,  MHG.  stade,  G. Staden,  Gestade,  Goth,  stafra  (dat.),  ‘bank, shore’.  These  words  derive  fr.  I.-E.  base  *sta-, ‘to  stand',  and  orig.  meant  ‘a  place  for  stand¬ ing’.  See  state  and  cp.  stead, stake,  n.  —  ME.,  fr.  OE.  staca,  rel.  to  ON.  stiaki, Swed.  stake,  Dan.  stage,  Du.  staak,  and  cogn. with  Lett,  stega,  stegs,  ‘rod,  pole,  perch’,  Russ. stozar',  of  s.m.,  and  possibly  also  with  L.  lig¬ num,  ‘building  material,  log,  beam’.  Cp.  stack, stagger,  stockade,  estacade.  Cp.  also  contigna- tion.
36984:straw,  n.  —  ME.  straw,  fr.  OE.  streaw,  rel.  to  ON. strd,  Dan.  straa,  Swed.  strd,  OFris.  sire,  ODu. strd,  Du.  stro,  OHG.,  MHG.  strd,  G.  Stroh,  lit. ‘that  which  is  scattered’,  fr.  I.-E.  base  *ster-, *stor-,  *str-,  ‘to  spread  out,  extend,  strew’, whence  also  L.  sternere,  pp.  stratus,  ‘to  spread out’.  See  stratum  and  cp.  strew.
36986:straw,  tr.  v.  —  ME.  slrawen,  a  collateral  form  of sire  wen.  See  strew.
```


## [2026-09-14T03:15:38.924Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"stitch,  n\\.\\|stich,  n\\.\\|stoichiometry\\|stoicheion\\|hemistich\" KLN_1966.txt | head -10; echo \"=== SKT\"; grep -n \"^Stitch\\|^Stair\\|^Straw\\|^Street\\|^Stray\\|Stitch,\\|Stair,\" SKT.txt | head -10",
 "description": "Grep Klein and Skeat for stitch/stich"
}
```


### [2026-09-14T03:15:39.009Z] TOOL RESULT

```
1519:acrostic,  n.,  a  poem  in  which  the  initial  letters  of the  lines  form  a  word  or  words.  —  L.  acrostichis, fr.  Gk.  4xpooxixk.  ‘acrostic’,  which  is  com¬ pounded  of  4xpop,  ‘at  the  end,  outermost’,  and cmxop,  ‘row,  line,  rank,  verse’,  which  is  rel. to  oxelxei v,  ‘to  go;  to  march  in  order’.  See aero-  and  sty,  ‘to  ascend’,  and  cp.  hemistich, monostich,  distich,  tetrastich,  pentastich,  hexa- stich,  beptastich,  octastich,  decastich,  stichich, orthostichy,  stoichiometry,  cadastre.
10476:decarchy,  n.,  a  government  of  ten.  —  Gk.  Sexap- Xia,  fr.  Sexdcpxr)?.  See  prec.  word  and  -archy. decastich,  n.,  a  poem  of  ten  lines.  —  Gk.  8exi- <mxo?,  ‘containing  ten  lines’,  fr.  Sexa,  ‘ten’,  and <jt ixoq,  ‘row,  line,  rank’.  See  deca-  and  sticbic. decastyle,  n.,  a  portico  with  ten  columns  ( arch .) — Compounded  of  deca- and  Gk.oxuXo?, ‘pillar’. See  style,  ‘gnomon’.
11841:distich,  n.,  a  group  of  two  lines  (pros.)  —  L.  di- stichon,  fr.  Gk.  Sicmyov,  neut.  of  8ia~iy_oc,  ‘of two  rows,  two-ranked’,  fr.  Si-  (see  di-,  ‘two’) and  cmyoi;,  ‘order,  row,  line,  rank;  verse’, which  is  rel.  to  utsi/eiy,  ‘to  go,  march  in  order’. See  acrostic  and  cp.  words  there  referred  to. Distichlis,  n.,  a  genus  of  grasses,  the  spike  grass (bot.)  —  ModL.,  fr.  Gk.  Sta-riyo q,  ‘of  two rows,  two-ranked’.  See  prec.  word, distichous,  adj.,  arranged  in  two  rows  (bot.)  —  L. distichus,  fr.  Gk.  SiaTiyo?,  ‘of  two  rows’.  See distich.  For  E.  -ous,  as  equivalent  to  Gk.  -oq, L.  -us,  see  -ous.
17548:hemistich,  n.,  half  of  a  poetic  line.  —  L.  hemi- stichium ,  fr.  Gk.  riptemyiov,  ‘half  line,  half verse’,  compounded  of  Tjpu-  (see  hemi-)  and nriyoc,,  ‘row,  line,  rank;  verse’,  which  is  related
17736:hexapod,  n.,  1)  any  six-footed  insect ;  2)  any  insect of  the  class  Hexapoda.  —  Gk.  iftdbrooi;,  gen. £500x0804,  ‘six-footed’,  compounded  of  e^a-  (see hexa-)  and  77064,  gen.  710864,  ‘foot’.  See  -pod. Hexapoda,  n.,  a  class  of  six-footed  insects  (ento- mol.)  —  ModL.  See  prec.  word, hexastich,  n.,  a  stanza  or  poem  consisting  of  six verses  or  lines  (pros)  —  Gk.  E^aaTi/09,  ‘of  six lines’,  compounded  of  spot-  (see  hexa-)  and crrl -jtpz,  ‘row,  line,  rank ;  verse’.  See  stichic  and cp.  acrostic  and  words  there  referred  to. hexastyle,  adj.,  having  six  columns  in  front.  — Gk.  i^aox’jXoc;,  ‘having  six  columns’,  com¬ pounded  of  E^a-  (see  hexa-)  and  0x6X04,  ‘pillar, column’.  See  style,  ‘gnomon’.
26036:octarchy,  n.,  a  government  by  eight  rulers.  — Compounded  of  oct-  and  -apyla,  ‘rule  of’,  fr. apx.6?,  ‘leader,  chief,  ruler’.  See  -archy. octastich,  n.,  a  stanza  or  poem  consisting  of eight  verses.  —  Gk.  oxTcxcmycx;,  ‘of  eight  lines’, compounded  of  oxtoc-  (see  octa-)  and  rs-.'v/pc, ‘row,  line,  rank ;  verse’ ;  see  stichic  and  cp.  acros¬ tic  and  words  there  referred  to. octastyle,  adj.,  having  eight  columns  in  front.  — L.  odastylos,  fr.  Gk.  fixTocoTuXoc;,  ‘having  eight columns’,  which  is  compounded  of  oxtoc-  (see octa-)  and  otuXoc,  ‘pillar,  column’.  See  style, ‘gnomon’.
28028:pentastich,  n.,  a  stanza  or  poem  consisting  of  five verses.  —  Gk.  Trevxaxxt/ot:.  ‘of  five  verses’,  fr. 7tsvxa-  (see  penta-)  and  xxiy/jc,  ‘row,  line’.  See acrostic  and  cp.  words  there  referred  to. Derivatives: pentastich-ous,  adj ,,pentastich-y,  n.
36842:Derivatives :  stirrup,  tr.  v.,  stirrup-less,  adj. stitch,  n.  —  ME.  stiche,  fr.  OE.  slice,  ‘puncture, stab,  stitch,  stitching’,  rel.  to  OE.  stician,  ‘to prick’.  See  stick,  v.,  and  cp.  etiquette,  ticket, stitch,  tr.  and  intr.  v.  —  ME.  stichen,  fr.  stiche. See  stitch,  n.
36859:Derivative:  stoic-al-ly,  adv. stoichiometry,  also  stoechiometry,  stoicheiometry, n.,  the  art  of  determining  the  atomic  and  molec¬ ular  weights  of  the  elements  (chem.)  —  G.  Std- chiometrie,  lit.  ‘measurement  of  elements’,  coin¬ ed  by  the  German  chemist  Jeremias  Benjamin Richter  (1762-1807)  in  his  “Anfangsgriinde  der Stochiometrie  oder  Meflkunst  chemischer  Ele- mente”  (1792)  fr.  Gk.  axotyeiov,  ‘element’,  and -pexpla,  ‘a  measuring  of’.  The  first  element  is  a derivative  of  axotyoq,  ‘row,  line,  rank’,  which is  rel.  to  oxt/os,  ‘row,  line,  rank;  verse’,  oxe(- yetv,  ‘to  go;  to  march  in  order’ ;  see  stichic.  For the  second  element  see  -metry.
38785:Derivative:  tetrasem-ic,  adj. tetrastich,  n.,  a  poem  consisting  of  four  lines.  — L.  tetrastichon,  fr.  Gk.  xsxpaox'./ov,  prop.  neut. of  the  adjective  xexparmyoc,  ‘of  four  lines’, used  as  a  noun;  compounded  of  xsxpa-  (see tetra-)  and  axi/op.  ‘row,  line,  rank;  verse’.  See stichic  and  cp.  acrostic  and  words  there  referred to.
=== SKT
18296:Stair,  n  step  op  (£.)  M.E.  ittir.  tttytr, A.S.  st<Xf^,  a  stair,  step;  lit.  a  step  to climb  by.*  A.  S.  sUg  (also  stdh).  pt.  t  ol sft'^tiH,  to  climb. 4>Du.  siei^tr,  a  staii,  Icel. //rA*)',  it^JPf  Swed.  t/r^it,  ladder,  Dan.  //jrjy, ladder,  U.  //rjr>  a  jath  ;  from  Du.  stiJgrH, Iccl.  stfga,  Swed.  ttiga^  Dan.  stigt^  G. sfet[^n,  to  mount,  climb.  Allied  to  Ski. stij^'h,  lo  asctnd.  (ik.  trrW^ftc.  (.^STKiH.) atag,  a  male  deer.  (Sciud.)  A\io  ap- plied (in  dialect--)  to  a  male  animal  gene- rally.,-Icel.  Jft^'f,  sUggi,  a  he-bird,  drake, tom*cat.  Liu  'mounter;'  from  kel.r/i'^'n, lo  mount.     Spt ! t //u^j;a  ;  I^usofCnut
18590:Stitch;  see  Stiok  (i>.
```


## [2026-09-14T03:16:03.750Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== LEW sterno\"; grep -n \"sterno\" LEW_1910.txt | head -5; echo \"=== LEW struo\"; grep -n \"^struo\\|struo,\" LEW_1910.txt | head -5; echo \"=== LAT\"; grep -n \"sterno\\|struo\" LAT.txt | head -8",
 "description": "Grep Latin etymological dictionaries"
}
```


### [2026-09-14T03:16:03.852Z] TOOL RESULT

```
=== LEW sterno
315:kazt I 178 kebu I 210 cehefi I 152, 631, 854 kenkatrum I 233/4 cisterno I 223 Klaverniie I 229 klavlaf I 229 kletram I 236 Kluviier I 237 krematra I 287 cringatro I 233/4 ku-, -ku(m), co-, com-, -co(m) I 251 Cubrar I 312 kukehes I 152, 854 kvestur, kvestretie IT 396 kumaltu II 104 kumates, comatir II 17, 104 combifiatu, combi- fianstust I 494 kumiaf I 589, 626 kumne, kumnakle I 251 comohota I 251, IT 116 comoltu, kumultu I 251, If 104,105 conegos I 251, 261 kunikaz I 261 kuraia, kuratu
=== LEW struo
=== LAT
3717:ancunulentus, -a, -inn: mot de gloss. -ae feminae menstruo tempore
7825:bublnS, -as, -are:-re menstruo mulierum sanguine inquinare , P. F.
10288:kastruvuf, castruo. Le sens ancien est peut-etre "separation, ce qui
13512:pard de sterno, -is, cf. profligare k cote de fligere.
18600:s iue halonem (?) i.e. hesterno uino languentem, quod swXov uocitant
19539:natus (Catul.64,71 et 165) se rattachent k externus, on a sterno ; le
27450:hesterno uino languentem ; halito,-as (Enn.): exhaler, souffler;
37542:forme d'apres annuus, annualis; menstruosus (GLoss.);et les composes
```


## [2026-09-14T03:16:09.556Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"sterno, \\|struo, \\|strues\\|strata (uia)\\|strdta\" LAT.txt | head -10; echo \"=== IEC\"; grep -n \"sterno\\|strātos\\|stratos\" IEC.txt | head -8; echo \"=== SYN army\"; grep -n -i \"stratos\" SYN.txt | head -5; echo \"=== SYN straw\"; grep -n -i \"straw\" SYN.txt | head -5",
 "description": "Grep Ernout-Meillet, Mann, Buck"
}
```


### [2026-09-14T03:16:09.674Z] TOOL RESULT

```
13512:pard de sterno, -is, cf. profligare k cote de fligere.
60349:sterno, -ls, straul, stratum, sternere: «Hendre, coucher k terre;
60374:A sterno, -is correspond un intensif en -d- attestd dans les com-
60382:iri. consterna in), dZ-, in-, inter-, ob-, per-, pro-, sub-sterno, M.L.
61354:strues, struix: v. struo.
61365:struo, -ls, -xi, -ctum, -ere: disposer en piles, "empiler" (des
61371:DErivEs et composEs: strues,-is f.: pile; en particulier, dans la
61403:Les formes struo et strues montrent que la gutturale de struxi,
61406:strupla (struhpla), strus la, au sens de strues, -pia- est un suffixe
=== IEC
17198:ster-, e-gde of radical str-, q. v. Cf. also stor- *strew, spread”, etc. WP II, 640 Skt. stare, mp. ‘strew’; pp: strtáb; Av. star-, id.; Per. cf. gu-stardan, inf. id.; gu-star, s. ‘spreader (fr. *aue-^); Lat. cf. sterno, Ere, v. id.; cf. ster-cus & -cor, -quilinium, n. ‘dung’; Srb. stérem, stérati, v. ‘stretch’; cf. OIr. sernaim, v. 'strew'. (In the sense of “side”, a possible formant in Gk. ari-sterós, Lat. sini-ster, OHG, OE winister, win-ster, etc.)
17201:stenos — stero (sterno)
17213:sterð (sterno), pp: strtós ‘strew, extend, spread, scatter’. WP II, 639 Skt. stárami beside Vedic strnómi, pp: strtáh, id.; Av. star-, id.; Lat. sterno, pf: stravi, sup. stratum, v. id.; cf. segi-sterium 'pigswill; Gk. cf. (o-gde) stórnümi, v. 'spread', etc.; Olr. Mir sernaim, v. id.; (z-gde) Alb. shtrij, shtrij, id.; and in OCS stro, stréti, Cz. stru, střít, id.; (o-gde in) Cz. pro-stor, m. ‘expanse’;
17427:strn- (stern-) ‘violent, precipitate; violence, severity’. Lat. (e-gde) cf. sternāx, -nācis, adj. ‘restive’; con-sterno, are, v. ‘dismay, rout; Ir. (long z-gde) srán, m. “dash, grab’; sráinim, v. over, whelm, defeat; OHG stornen, inf. ‘grow rigid’; OE styrne, adj. (severe, stern’; Cz. cf. strn-ist&, n. 'stubble-field'; Pol. $ciernisko, id. (For the extn. of type OCS strümínü, adj. *steep, stark, firm' cf. also strm-). The Slav simplex ‘stubble’ arises in OCS, Blg. strüni, f. 'haulm'; Li. stirnas, adj. ‘tough, springy’
=== SYN army
=== SYN straw
8405:rts tehungsgesch- 327, oe Jagh olrava, Pol. potrawa, strawa : Boh. a tgrass’, fr. the root in truti chsl. (rae ‘nourish, feed’, tryte
9591:Although there is a word for ‘berry’ in most of the Eur. languages, it is only in the Gmc. group that the word fuishes a long series of cpds. denoting the special kinds of berry. Thus NE ber- Ty, whence strawberry, raspberry, black- berry, blueberry, cranberra , gooseberry, éle,, formerly also wineberry (OE wein- berige, like Goth. weinabasi), now re- placed by grape, Similarly, NHG beere mith erdbeere, himbeere, etc., and in fie other Gme, languages. Elsewhere the
11576:Sp. choza, chozo, fr. Lat. pluteum ‘shed’. REW 6619. Otherwise (fr, Arab. huss ‘straw hut’) Lokotsch 887.
11738:5. Goth. haurds, ON hurd, orig. a door of ‘lattice work’ : OE hyrdel (NE hurdle), OHG hurt, Lat. cratis ‘wicker- work’, Grk. xaprados ‘basket’, Skt. kata- ‘straw mat’, krt- ‘wind’, etc., IE *kert-. Walde-P. 1.421. Feist 250.
11915:7.28 ROOF Grk. (a)réyos, oréyn, dpod7 Goth. hrot Lith. stogas NG oréyn, axe ON pak (hrot) Lett. jumis Int, — téclum Dan. tag ChSl.  krovit, strécha re lello Sw. tak SCr. _ krov ri i OE pac, hrof Boh. _ strecha, krov a i 0, techado ME rofe Pol. dach, strzecha ih (urge) ue roof Russ. krysa Nit. eeann OHG dan renew pore MHG dach NHG dach Most of the words for ‘roof’ are from | Ir. tuige ‘straw, thatch’ and prob. used
```


## [2026-09-14T03:16:18.742Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls incoming/WLD/ && python3 - <<'EOF'\nimport re\np='incoming/WLD/WLD_Bd2_pages.txt'\ntxt=open(p,encoding='utf8',errors='replace').read()\nleaves=txt.split('\\f')\nprint('leaves',len(leaves))\n# find leaf containing 'steigh'\nfor i,l in enumerate(leaves):\n    if 'steigh' in l or 'stéigh' in l:\n        print('steigh leaf',i, l[:200].replace('\\n',' '))\n        break\nfor i,l in enumerate(leaves):\n    if re.search(r'ster-\\s*:', l) and 'sterile' not in l:\n        pass\nEOF",
 "description": "Search Walde-Pokorny Bd2"
}
```


### [2026-09-14T03:16:19.892Z] TOOL RESULT

```
WLD_Bd1_1930_dli_70244_djvu.txt
WLD_Bd1_1930_dli_70244_text.pdf
WLD_Bd1_pages.txt
WLD_Bd2_1927_dli_106624_djvu.txt
WLD_Bd2_1927_dli_106624_text.pdf
WLD_Bd2_pages.txt
leaves 725
steigh leaf 618 614                                          (s)teig«        steigh-         Russ. stegdth, stegnUth „steppen, durchnahen, peitschen'*, steSka {e    in geschlossener Silbe aus h und auf stegdh iibertr
```


## [2026-09-14T03:16:22.875Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\ntxt=open('incoming/WLD/WLD_Bd2_pages.txt',encoding='utf8',errors='replace').read()\nleaves=txt.split('\\f')\nprint(leaves[618][:2500])\nEOF",
 "description": "Print WLD leaf 618 (p.614)"
}
```


### [2026-09-14T03:16:23.927Z] TOOL RESULT

```
614                                          (s)teig«        steigh-



     Russ. stegdth, stegnUth „steppen, durchnahen, peitschen'*, steSka
{e    in geschlossener Silbe aus h und auf stegdh iibertragen; gegen Verb,
mit    "^steg-   „Stange“ spricht die Bed.)
     cech. steh, poln. scieg, scig „Stich‘‘.
     Ygl, Curtins 2l4f.,           Fickl^ 144, 569, Zup. G. 168 (Lit.).                     Yerfehlt   ist
Reichelts        KZ.    Yereinigung unseres "^steig- „stecben“ mit *steg-
                         39, 17
„Stange'‘ unter idg. ste(i)g-, zumal fur "^steg- „Stange“ eine Urbedeutung
„stechend‘^ und fur steig- „stechen“ andrerseits eine Urbed. „mit einer
Stange oder einem Stock stechen'^ wenigstens nicht zu erweisen ist (aller-
dings bei der ahnlichen Wz. stegJi-, stmgh- sind beide Bed. nebenein-
ander belegt).

(s)teigS- „Schulter,             Arm, Schenkel“.
     Liden Arm. St, 31 verbindet;
  arm. fekn, gen. tikan „Scbulter, Achsel; Arm“, pi. tikunk „SGliultern;
Riicken; Hinterteil, Seite eines Gebaudes usw.“ {^toig^^-no-);
  aksl. sthg-no „femur“, slov. sUgno „Oberschenkel'', russ. stegno „Hufte,
Lende; Oberschenker^
  aber lit. *steigara „Glied, Gelenk'^ ist recte stiegard „Federkiek";
  kelt. "^toi^-es- in air. toeb^ toih n., cymr. corn. bret. tu „Seite“ (Bed.
wie bei abd. hlanca „Hufte“ und „Seite“; das kelt. Wort nicht wahrschein-
licher      nach Macbain Et. Diet, of the Gael. Langu. [323 ^ 359], Pedersen
KG. 1 116 zu lit. stdibiai usw., s. u. stlp-, sftb- „Stange usw.“; s. auch Morris-
Jones Welsh, Gr. 422).

steigh- „schreiten, steigen'".
     Ai. stighnoti „steigt“ (Dhatup.), ved. pra-stighnuyat Opt. praes. „er moge
emporkommen“, ati-stighani Inf. „ubersteigen, bemeistern“ Maitrayanisanih
gr. OTEiyco „schreite, gehe“,                           gen. ortyog, pi. ortyeg, -ag „Reihe, Zeile“,
att. oTiyog „Reihe, Zeile, Linie'^, oxiydo&at „in dichter                            Reihe neben- oder
hintereinander gehn oder kommen“, ordiyog „Reihe, Linie“;
  alb. stekj bestimmt steg-ti „Durchgang, Eingang, W^eg, Haarscheitel“
(= oToiyog) G. Meyer BB. 8, 1S7, Wb. 415); lat. yielleicht in vestigium
,,Pu6tapfe, FuBspur, Fu6sohle“                    (s.   Yf. LEWb.^ s. v. mit Lit; neueste Yer-
teidigung bei Persson KZ. 48, 133 f.,                       doch bleibt die Deutimg der ersten
Silbe       — *ve ,herab“?
                     3
                                   s.         ne           noch unsicher; verfehlt iiber ve- Fay
IF. 26, 37 a 4);
     ai
```


## [2026-09-14T03:16:30.609Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\ntxt=open('incoming/WLD/WLD_Bd2_pages.txt',encoding='utf8',errors='replace').read()\nleaves=txt.split('\\f')\nprint('--- leaf 619 (p.615) ---')\nprint(leaves[619][:1500])\nprint('--- leaf 643 (p.639) ---')\nprint(leaves[643][:1800])\nEOF",
 "description": "Print WLD pages 615 and 639"
}
```


### [2026-09-14T03:16:31.727Z] TOOL RESULT

```
--- leaf 619 (p.615) ---
                                                                                     ;                       ;




                                                  (s)teigah       steu-                                   615

geriist^;       aisl. stett        „Fu6spiir, Tritt, Stellung, Uberstieg iiber einen Zaiin“,
steitr „(Basis =) PuB                    eines Glases“   (:   cymr. taith)^     aisl.    stetta „unterstutzen,
helfen'', ags. stihtan, stihtian („'*'auf eine Basis stellen =) einrichten, ordnen‘‘,
ahd. ps. stihtan             (s.   auch Falk-Torp u. stift II)            ;
                                                                              usw.
     lit.    staiga   Adv.         „pl6tzlich“,     staigus „heftig,          schaell     aufbrausend“   (vgl.
dt. steigen        im Sinne von „gereizt werden*'), staigaiis, -^tis und (s. Leskien
Abl. 285,        wo falsch angesetzt) steigiHos, stelgtis „liastig sein, sich beeilen,
sich        bemuhen^;     steidzu{ps), steigt{i^) ,.sicli beeilen“, „wandeln“,
stiga       „Pfad“; abg. sfignq „ich komme“, shdza^ shza „Fu6steig, StraBe'',
shyna „StraBe“.
     Curtins 195, Pick IM44. 333, 568,                        IIM24, IIIM91 f.

(s)teig®h- j.ausharren,                   mhig verweilen^.
  Got. stiwiti „Geduld'‘ (das gewiB nicht als ^steiied-iom nach Johansson
PBrB. 15, 237 zu lat. stadium jjStreben, Eifer“ gehort, s. vielmehr steu-^
steu-d-' „stoBen“);                ai.    iitiMate „halt
                        
--- leaf 643 (p.639) ---
                                                                                                                            ;




                                                              ster-                                                      639

crgareia, orQart]y6g), aol. orgorog (s. Solmsen Gl. 1, 78 f. und bes. Pers-
son Beitr. 451, gegen eine Gdf. *strnt6s und die Verb, mit ir. tret „Herde",
abg. trqt^ „agmen“ durch Windisch IF. 3, 80 ff., Zup. KZ. 36, 55) hochstufig                             ;


oTsgvov „Brust‘‘ (ausgebreitete Flache''; vgl. ahd. stirna „Stirn“, red.-st.                                              ai.

stlrnd-h, cymr. sarn, und o-stufig abg. strana).
      Alb. Mrin „breite aus'' {strnio; G. Meyer BB. 8, 191,                                 Wb. 418, A.-St. Ill
78),     stie    „Iege bin, werfe, schleudere, schieBe,                              mache       eine   Fehlgeburt“
{^stero-,       Jokl SBAk. Wien 168, 1 84 f.,                     Thumb GGA. 1915, 25).
      Lat. sterno, -ere „auf den Boden hinstreuen, hinbreiten                                ;
                                                                                                  feindlich    :   nieder-
strecken‘‘,       Ptc. stratus            {^steTdtos),       darnach Pf.        stravt',     prosternere           (:   slav.
prosthrq,        ai.         aber nicht consternare (s. u. ster- .,starren‘‘ und
                           pi'a-stard-h),
pet- „auf etwas losstiirzen*')   sir amen „Streu“ (
                                                ;
                                                     oTgd)pa    ai. stdriman -)  :
                                                                                                  ;


dazu mit ^-Erw. strages „das Nieders
```


## [2026-09-14T03:16:39.500Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\ntxt=open('POK_01.txt',encoding='utf8',errors='replace').read()\nleaves=txt.split('\\f')\nprint('leaves',len(leaves))\nfor n in (115,64):\n    print('--- leaf',n,'---')\n    print(leaves[n][:700])\nEOF",
 "description": "Check Pokorny pages 107 and 56"
}
```


### [2026-09-14T03:16:40.546Z] TOOL RESULT

```
leaves 364
--- leaf 115 ---
n',  w( von  ahd.  barij  PI.  banna  , Gebot  unter  Strafandrohung*  (nhd.  Bann,  Bawdi tcald),  ags.  gebann,  aisl.  bann  n.  »Verbot,  Bann*.
Toch.  A  pä-j  pä-g-  , betteln'  (Van  Windekens   Lexique  87  f.).
Nach  Kuiper  (AO.  XII  262)  hierher  (*bhd-s-)  ai.  bhisdkti  ,heilt',  bhiSdfi jArzt',  jav.  -bis-  , heilend*;    über   av.  bisazjät   vgl.  Kuiper  Nasalpräs.  44 fj
WP.  II  123 f.,  WH.  I  437  f.,  450,  458  f.,  525 f.,  Schwjzer  Gr.  Gr.  I  674r
bhabhä  und  anklingende  Worte  für  , Bohne*,  u.  zw.  , Saubohne',  vgl.  zuml Sachlichen  Hoops  Waldb.  350,  400  f.,  464  f.,  Helm  Kltpfl.«  221,  570,1 Schrader  RL.^  159  f.  |
Lat.  faba  (fäl.  haba)
--- leaf 64 ---
293,    Schwyzer  Gr.  Gr.  I  434 hierher  mit  Präf.  *o-,  kaum  zur  Wz.  *ser-  oder  Wz.  *?^er-,  d-J^eigo))]   dazu öagl^ü)  ^liabe  vertrauten  Umgang'^;  auch  ^plaudere  vertraulich';  x^^'^^'^Q^^S ;,erzgefügt,   gepanzei't',   auch  xsQi-dgag   Ti%Vü)v   Pind.,   ^g-d-gov  , Glied,  Ge-  < lenk',  ägd-^ög  , Verbindung,  Freundschaft',  icgd-fiiog  ,vereint';  mit  ^-Suffixen  • homer.  dafi-or^-r- , Hausfrau'  (,die  des  Hauses  Waltende'),  äol.  doixogvLq  Hes. ;  ' Ttvlccgvrjg  , Hades  als  Verschließer  des  Unterweltstores'  (Schwyzer  Gr.  Gr. I  451,  5);    äge-   in  ägsaxco   ,gleiche   aus,    mache   gut,   befriedige',   dg€(Ty,EL IXOL  ,es  paßt,  gefällt  mir',
```


## [2026-09-14T03:16:51.940Z] TOOL CALL #61: Bash

```json
{
 "command": "sed -n '1,60p' tools/fetch_source.py",
 "description": "Inspect fetch_source.py"
}
```


### [2026-09-14T03:16:51.991Z] TOOL RESULT

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


## [2026-09-14T03:16:58.672Z] TOOL CALL #62: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/stey%C7%B5%CA%B0-\" \\\n \"https://en.wiktionary.org/wiki/%CF%83%CF%84%CE%BF%CE%B9%CF%87%CE%B5%E1%BF%96%CE%BF%CE%BD\" \\\n \"https://www.etymonline.com/word/stitch\" \\\n \"https://www.etymonline.com/word/stich\" \\\n \"https://www.etymonline.com/word/stair\" \\\n ; do echo \"### $u\"; timeout 120 python3 tools/fetch_source.py \"$u\" --note \"page 479 verification: Steigh root, stoicheion/stich/stitch/stair\" ; done",
 "description": "Fetch and archive web sources batch 1"
}
```


### [2026-09-14T03:17:02.915Z] TOOL RESULT

```
### https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/stey%C7%B5%CA%B0-
/home/sfmqrb/git/rishe/data/verification/sources/web/1db423436029d8ec.txt
### https://en.wiktionary.org/wiki/%CF%83%CF%84%CE%BF%CE%B9%CF%87%CE%B5%E1%BF%96%CE%BF%CE%BD
/home/sfmqrb/git/rishe/data/verification/sources/web/4f7103fd22351365.txt
### https://www.etymonline.com/word/stitch
/home/sfmqrb/git/rishe/data/verification/sources/web/39e822236cc8a3c7.txt
### https://www.etymonline.com/word/stich
/home/sfmqrb/git/rishe/data/verification/sources/web/d5e71e6915623b82.txt
### https://www.etymonline.com/word/stair
/home/sfmqrb/git/rishe/data/verification/sources/web/1f3199fd85ef9cc0.txt
```


## [2026-09-14T03:17:05.789Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in 1db423436029d8ec 4f7103fd22351365 39e822236cc8a3c7 d5e71e6915623b82 1f3199fd85ef9cc0; do echo \"######## $f\"; head -c 2500 $f.txt | tr -s '\\n' '\\n'; echo; done",
 "description": "Read archived web sources batch 1"
}
```


### [2026-09-14T03:17:06.686Z] TOOL RESULT

```
######## 1db423436029d8ec
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/stey%C7%B5%CA%B0-
FETCHED: 2026-09-14T03:17:00Z
STATUS: -1
TITLE: 
FETCH FAILED: HTTP Error 404: Not Found
######## 4f7103fd22351365
URL: https://en.wiktionary.org/wiki/%CF%83%CF%84%CE%BF%CE%B9%CF%87%CE%B5%E1%BF%96%CE%BF%CE%BD
FETCHED: 2026-09-14T03:17:01Z
STATUS: 200
TITLE: στοιχεῖον - Wiktionary, the free dictionary
στοιχεῖον - Wiktionary, the free dictionary 
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
 Ancient Greek 
 Toggle Ancient Greek subsection 
 1.1 
 Etymology 
 1.2 
 Pronunciation 
 1.3 
 Noun 
 1.3.1 
 Declension 
 1.3.2 
 Synonyms 
 1.3.3 
 Derived terms 
 1.3.4 
 Descendants 
 1.4 
 References 
 Toggle the table of contents 
 στοιχεῖον 
 7 languages 
 Ελληνικά 
 Français 
 Italiano 
 한국어 
 Malagasy 
 Русский 
 Српски / srpski 
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
 Ancient Greek
 [ edit ] 
 FWOTD – 27 February 2015 
 Etymology
 [ edit ] 
 στοῖχος ( stoîkhos ) +‎ -εῖον ( -eîon ) .
 Pronunciation
 [ edit ] 
 IPA ( key ) : /stoi̯.kʰêː.on/ → /styˈçi.on/ → /stiˈçi.on/ 
 ( 5 th BCE Attic ) IPA ( key ) : /stoi̯.kʰêː.on/ 
 ( 1 st CE Egyptian ) IPA ( key ) : /styˈkʰi.on/ 
 ( 4 th CE Koine ) IPA ( key ) : /styˈçi.on/ 
 ( 10 th CE Byzantine ) IPA ( key ) : /styˈçi.on/ 
 ( 15 th CE Constantinopolitan ) IPA ( key ) : /stiˈçi.on/ 
 Noun
 [ edit ] 
 στοιχεῖον • ( stoikheîon )  n ( genitive στοιχείου ) ; second declension 
 ( properly ) one of a row :
 ( in the sun-dial ) the shadow of the gnomon , which advances regularly hour after hour 
 391 BCE , Aristophanes , Assemblywomen 652 
 4th century BC , Eubulus , Incert. 1
 362 BCE – 262 BCE , Philemon , ap. Phot. 
 ( generally ) one of a series , a component part , an element :
 384 BCE – 322 BCE , Aristotle , Metaphysics 4.
######## 39e822236cc8a3c7
URL: https://www.etymonline.com/word/stitch
FETCHED: 2026-09-14T03:17:02Z
STATUS: 200
TITLE: Stitch - Etymology, Origin & Meaning
Stitch - Etymology, Origin & Meaning 
 Search 
 Log in 
 Columns 
 Forum 
 Apps 
 Premium 
 Log in 
 Advertisement Remove Ads 
 Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.
 Origin and history of stitch 
 stitch (n.) 
 Middle English stiche , from Old English stice "a prick, puncture, sting, stab" (senses now obsolete), from Proto-Germanic *stikiz (source also of Old Frisian steke , Old High German stih , German Stich "a pricking, prick, sting, stab"), from PIE *stig-i- , from root *steig- "to stick; pointed" (see stick (v.)).
 The sense of "sudden, stabbing pain in the side, acute sudden pain like that of the thrust of a needle" was in late Old English (in the leechdoms).
 The sense in sewing and shoemaking, "one movement of a threaded needle passing in and out of fabric," is by late 13c.; in reference to the part of thread left in the fabric by this, from late 14c. Hence by synecdoche the meaning "bit of clothing" one is (or isn't) wearing, from c. 1500. In reference to a particular type of needlework (as in cross-stitch ), by 1620s.
 The meaning "a stroke of work" (of any kind) is attested from 1580s. The surgical sense is recorded by 1520s. The sense of "amusing person or thing" is by 1968, from the notion of laughing so much one gets stitches of pain (compare verbal expression have (someone) in stitches , attested by 1935).
 stitch (v.) 
 c. 1200, stichen , "to stab, pierce, cause pain," also "to unite or ornament (a garment) with stitches;" from stitch (n.). With up (adv.) from c. 1500. The surgical sense is from 1570s. Related: Stitched ; stitcher ; stitching .
 also from c. 1200 
 Entries linking to stitch 
 cross-stitch (n.) 
 1710, in needlework, "a stitch in the form of an X; two stitches, one crossing the other in the middle," from cross- + stitch (n.). As a verb from 1794. Related: Cross-stitched; crossed-stitching .
 stick (v.) 
 Middle English stiken , from Old English stician "to pierce or puncture, to stab with a weapon; transfix; goad," also "to remain embedded, stay fixed, be fastened," from Proto-Germanic *stekanan "pierce, prick, be sharp" (source also of Old Saxon stekan , Old Frisian steka , Dutch stecken , Old High German stehhan , German stechen "to stab, prick").
 This is reconstructed to be from PIE *steig- "to stick; pointed" (source al
######## d5e71e6915623b82
URL: https://www.etymonline.com/word/stich
FETCHED: 2026-09-14T03:17:02Z
STATUS: 200
TITLE: Etymonline - Online Etymology Dictionary
Etymonline - Online Etymology Dictionary 
 Search 
 Log in 
 Columns 
 Forum 
 Apps 
 Premium 
 Log in 
 A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 
 Quick and reliable accounts of the origin and history of English words. Scholarly, yet simple.
 About
 Who Did This 
 Sources 
 Introduction 
 Links 
 Support
 Premium 
 Patreon 
 Donate with PayPal 
 Merch 
 Apps
Get Chrome Extension 
Get iOS App 
Get Android App 
 Dark
 Auto
 Light
 Terms of Services Privacy Policy 
 English (English) 
 © 2001–2026 Douglas Harper & Talia Felix
######## 1f3199fd85ef9cc0
URL: https://www.etymonline.com/word/stair
FETCHED: 2026-09-14T03:17:02Z
STATUS: 200
TITLE: Stair - Etymology, Origin & Meaning
Stair - Etymology, Origin & Meaning 
 Search 
 Log in 
 Columns 
 Forum 
 Apps 
 Premium 
 Log in 
 Advertisement Remove Ads 
 Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.
 Origin and history of stair 
 stair (n.) 
 Middle English steir , from Old English stæger "stair, staircase, flight of steps arranged one behind and above the other," from Proto-Germanic *staigri (source also of Middle Dutch stegher , Dutch steiger "a stair, step, quay, pier, scaffold;" German Steig "path," Old English stig "narrow path").
 This is reconstructed to be from PIE *steigh- "go, rise, stride, step, walk" (source also of Greek steikhein "to go, march in order," stikhos "row, line, rank, verse;" Sanskrit stighnoti "mounts, rises, steps;" Old Church Slavonic stignati "to overtake," stigna "place;" Lithuanian staiga "suddenly;" Old Irish tiagaim "I walk;" Welsh taith "going, walk, way").
 Originally also a collective plural; stairs developed by late 14c., and stair as "one of a succession of steps leading from one floor to another" is by 1520s. The figurative sense of "step in an ascending or descending scale" is from c. 1200.
 Entries linking to stair 
 acrostic (n.) 
 short poem in which the initial letters of the lines, taken in order, spell a word or phrase, 1580s, from Medieval Latin acrostichis , from Greek akrostikhis , from akros "at the end, outermost" (from PIE root *ak- "be sharp, rise (out) to a point, pierce") + stikhos "line of verse," literally "row, line" (from PIE root *steigh- "to stride, step, rise;" see stair ). The second element is properly -stich , but it has been assimilated to words in -ic . As an adjective from 1680s.
 backstairs (n.) 
 "stairs at the back of a structure," 1650s, from back (adj.) + stairs (see stair ). Figurative use is attested earlier (1640s).
 cadastral 
 downstairs 
 hemistich 
 staircase 
 stairway 
 stairwell 
 stichic 
 stickler 
 stile 
 stirrup 
 sty 
 tetrastich 
 upstairs 
 See All Related Words (15) 
 Advertisement Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.
 More to explore
 cadastral 
 "pertaining to the valuation of landed property as a basis for taxation," 1850, from French cadastral, from cadastre "register of the survey of lands" (16c.), from Old Italian catastico, from Late Gree
```


## [2026-09-14T03:17:16.633Z] TOOL CALL #64: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/steyg%CA%B0-\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/sterh%E2%82%83-\" \\\n \"https://en.wiktionary.org/wiki/%D8%B5%D8%B1%D8%A7%D8%B7\" \\\n \"https://en.wiktionary.org/wiki/%DA%AF%D8%B3%D8%AA%D8%B1%D8%AF%D9%86\" \\\n \"https://en.wiktionary.org/wiki/%D8%AE%D8%A7%DA%A9%D8%B3%D8%AA%D8%B1\" \\\n \"https://en.wiktionary.org/wiki/%D8%A8%D8%B3%D8%AA%D8%B1\" \\\n ; do echo \"### $u\"; timeout 120 python3 tools/fetch_source.py \"$u\" --note \"page 479 verification: Ster 1 root, sirat, gostardan, xakestar, bestar\"; done",
 "description": "Fetch and archive web sources batch 2"
}
```


### [2026-09-14T03:17:24.003Z] TOOL RESULT

```
### https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/steyg%CA%B0-
/home/sfmqrb/git/rishe/data/verification/sources/web/076d1965b9429ec8.txt
### https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/sterh%E2%82%83-
/home/sfmqrb/git/rishe/data/verification/sources/web/cfb3f5ffb0aa50ad.txt
### https://en.wiktionary.org/wiki/%D8%B5%D8%B1%D8%A7%D8%B7
/home/sfmqrb/git/rishe/data/verification/sources/web/50a196650898362c.txt
### https://en.wiktionary.org/wiki/%DA%AF%D8%B3%D8%AA%D8%B1%D8%AF%D9%86
/home/sfmqrb/git/rishe/data/verification/sources/web/9cc4f50b55f5be43.txt
### https://en.wiktionary.org/wiki/%D8%AE%D8%A7%DA%A9%D8%B3%D8%AA%D8%B1
/home/sfmqrb/git/rishe/data/verification/sources/web/793e57dcd504eb6f.txt
### https://en.wiktionary.org/wiki/%D8%A8%D8%B3%D8%AA%D8%B1
/home/sfmqrb/git/rishe/data/verification/sources/web/8069fc1a215aafef.txt
```


## [2026-09-14T03:17:27.507Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in 076d1965b9429ec8 cfb3f5ffb0aa50ad; do echo \"######## $f\"; grep -n \"STATUS\\|Etymology\\|Root\\|Derived\\|reflex\" $f.txt | head -5; sed -n '/Proto-Indo-European/,$p' $f.txt | sed -n '30,90p'; echo; done",
 "description": "Read PIE reconstruction pages"
}
```


### [2026-09-14T03:17:28.551Z] TOOL RESULT

```
######## 076d1965b9429ec8
3:STATUS: 200
62: Root 
65: Derived terms 
131: Root
140: Derived terms

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

 1.2 
 References 

 Toggle the table of contents 

 Reconstruction:Proto-Indo-European/ steygʰ- 

 Add languages 

 Reconstruction 

 Discussion 

 English 

 Read 

 Edit 

 View history 

 Tools 

 Tools

######## cfb3f5ffb0aa50ad
3:STATUS: 200
62: Etymology 
65: Root 
71: Derived terms 
140: Etymology

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
 Etymology 

 1.2 
 Root 

 1.2.1 
 Extensions 

 1.2.2 
 Derived terms 

 1.2.3 
 Descendants 

 1.3 
 References 

 Toggle the table of contents 

 Reconstruction:Proto-Indo-European/ sterh₃- 

 Add languages 

 Reconstruction 

 Discussion 

 English
```


## [2026-09-14T03:17:31.427Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"#### steygh\"; sed -n '125,190p' 076d1965b9429ec8.txt; echo; echo \"#### sterh3\"; sed -n '135,215p' cfb3f5ffb0aa50ad.txt",
 "description": "Print PIE root sections"
}
```


### [2026-09-14T03:17:31.562Z] TOOL RESULT

```
#### steygh

 This Proto-Indo-European entry contains reconstructed terms and roots . As such, the term(s) in this entry are not directly attested , but are hypothesized to have existed based on comparative evidence.

 Proto-Indo-European
 [ edit ] 

 Root
 [ edit ] 

 *steygʰ- ( imperfective ) [ 1 ] [ 2 ] [ 3 ] 

 to go 

 to climb 

 Derived terms
 [ edit ] 

 Terms derived from the Proto-Indo-European root *steygʰ- (40 c, 0 e) 

 *stéygʰ-e-ti ( thematic root present ) 

 *stḗygʰ-s-t ~ *stéygʰ-s-n̥t ( s-aorist ) [ 2 ] [ 4 ] 
 Proto-Celtic: *teixstē [ 5 ] 
 Old Irish: tías 

 *stoygʰ-éye-ti ( eye-causative ) 
 Proto-Germanic: *staigijaną ( “ to raise up, elevate ” ) ( see there for further descendants )
 ⇒ Proto-Germanic: *staigraz ( “ elevating; steep ” ) ( see there for further descendants )
 ⇒ Proto-Germanic: *staigriz ( “ scaffold; stairs ” ) ( see there for further descendants )

 *stigʰ-néw-ti ~ *stigʰ-n̥w-énti ( new-present ) [ 2 ] 
 Proto-Balto-Slavic: *stingneutei 
 Proto-Slavic: *stìgnǫti ( “ to attain, reach ” ) ( see there for further descendants )

 Proto-Indo-Iranian: *stigʰnáwti 
 Proto-Indo-Aryan: *stigʰnáwti 
 Sanskrit: स्तिघ्नोति ( stighnóti , “ to mount, step up, rise ” ) 

 *sti-né-gʰ-ti ~ *sti-n-gʰ-énti ( nasal-infix ) [ 2 ] 
 Proto-Celtic: *tinxti [ 2 ] [ 5 ] 
 * Old Irish: téit ( see there for further descendants )

 *stéygʰ-s ~ *stigʰ-és ( “ path ” ) 

 *stéygʰ-ti-s ~ *stigʰ-téy-s 
 Proto-Germanic: *stihtiz ( “ track ” ) [ 6 ] 
 Proto-West Germanic: *stihti 
 Dutch: sticht 

 Old Norse: stétt 
 Norwegian: stætt 

 *stóygʰ-i-s ~ *stigʰ-éy-s 
 Proto-Germanic: *stigiz ( “ a climb, ascent ” ) ( see there for further descendants )

 *stóygʰ-o-s ( “ path, way ” ) 

 *stigʰ-tó-s [ 1 ] 
 Proto-Germanic: *stihtaz 
 Old Norse: stéttr ( “ pavement ” ) ( see there for further descendants )

 References
 [ edit ] 

 ↑ 1.0 1.1 Pokorny, Julius ( 1959 ), “ steigh- ”, in Indogermanisches etymologisches Wörterbuch [ Indo-European Etymological Dictionary ] (in German), volume 3, Bern, München: Francke Verlag, pages 1017-1018 

#### sterh3
 This Proto-Indo-European entry contains reconstructed terms and roots . As such, the term(s) in this entry are not directly attested , but are hypothesized to have existed based on comparative evidence.

 Proto-Indo-European
 [ edit ] 

 Etymology
 [ edit ] 

 Extension of *ster- ( “ to spread ” ) .

 Root
 [ edit ] 

 *sterh₃- ( perfective ) [ 1 ] 

 to spread , extend , stretch out

 Extensions
 [ edit ] 

 *strew- ( “ to spread, strew ” ) 

 *str̥h₃-g- 
 Italic:
 Latin: strāgēs 

 Latin: strāgulus 

 Derived terms
 [ edit ] 

 Terms derived from the Proto-Indo-European root *sterh₃- (63 c, 0 e) 

 *stérh₃-t ~ *str̥h₃-ént ( root aorist ) [ 1 ] 
 Proto-Indo-Iranian: 
 Proto-Indo-Aryan: 
 Sanskrit: अस्तरीः ( astarīḥ , 2sg.aor. ) 

 *str̥-né-h₃-ti ~ *str̥-n-h₃-énti ( nasal-infix present ) [ 1 ] 

 *str̥h₃-tó-s 

 *stérh₃-mn̥ ~ *str̥h₃-mén-s ( “ that which is strewn/spread; bedding ” ) 
 Proto-Hellenic: *strṓmə 
 Ancient Greek: στρῶμα ( strôma ) ( see there for further descendants )

 Proto-Indo-Iranian: *stárHma 
 Proto-Indo-Aryan: *stárHma 
 Sanskrit: स्तरीमन् ( stárīman ) 

 Proto-Iranian: *stárHma 
 Avestan: 𐬯𐬙𐬆𐬭𐬆𐬨𐬀 ( stər ə ma , “ bed ” ) 

 Proto-Italic: *strāmən 
 Latin: strāmen 

 *storh₃-o- 
 Proto-Italic: 
 Latin: torus , storea ( see there for further descendants )

 Unsorted formations 

 Proto-Albanian: *śt(a)rē- 
 Albanian: shtroj 

 Proto-Albanian: *strinja 
 Albanian: shtrij 

 Proto-Balto-Slavic: 
 Proto-Slavic: *stornà ( “ side; land ” ) ( see there for further descendants )

 Proto-Balto-Slavic: 
 Proto-Slavic: *sterti ( see there for further descendants )
 ⇒ Proto-Slavic: *prosterti ( see there for further descendants )

 Proto-Hellenic: 
 Ancient Greek: στέρνον ( stérnon ) 

 Ancient Greek: στορέννῡμι ( storénnūmi ) , στρώννῡμι ( strṓnnūmi ) (byforms of στόρνῡμι ( stórnūmi ) )

 > ? Proto-Italic:
```


## [2026-09-14T03:17:38.157Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in 50a196650898362c 9cc4f50b55f5be43 793e57dcd504eb6f 8069fc1a215aafef; do echo \"######## $f\"; awk '/Etymology/{p=1} p' $f.txt | head -40; echo; done 2>&1 | head -140",
 "description": "Read Wiktionary Arabic/Persian entries"
}
```


### [2026-09-14T03:17:39.142Z] TOOL RESULT

```
######## 50a196650898362c
 Etymology 

 1.2 
 Pronunciation 

 1.3 
 Noun 

 1.3.1 
 Declension 

 1.3.2 
 Alternative forms 

 1.3.3 
 Descendants 

 1.4 
 References 

 Toggle the table of contents 

 صراط 

 7 languages 

 فارسی 
 हिन्दी 
 Magyar 
 Polski 
 Русский 
 Türkçe 
 Татарча / tatarça 

 Entry 

 Discussion 

 English 


######## 9cc4f50b55f5be43
 Etymology 

 1.2 
 Pronunciation 

 1.3 
 Verb 

 1.3.1 
 Conjugation 

 1.3.2 
 Derived terms 

 1.4 
 References 

 1.5 
 Further reading 

 Toggle the table of contents 

 گستردن 

 3 languages 

 فارسی 
 Malagasy 
 Русский 

 Entry 

 Discussion 

 English 

 Read 

 Edit 


######## 793e57dcd504eb6f
 Etymology 

 1.2 
 Noun 

 1.2.1 
 Declension 

 1.2.2 
 Derived terms 

 1.3 
 Further reading 

 2 
 Persian 

 Toggle Persian subsection 

 2.1 
 Etymology 

 2.2 
 Pronunciation 

 2.3 
 Noun 

 2.3.1 
 Derived terms 

 2.3.2 
 Descendants 

 Toggle the table of contents 

 خاکستر 

 13 languages 


######## 8069fc1a215aafef
 Etymology 

 1.2 
 Noun 

 2 
 Ottoman Turkish 

 Toggle Ottoman Turkish subsection 

 2.1 
 Etymology
```


## [2026-09-14T03:17:41.902Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in 50a196650898362c 9cc4f50b55f5be43 793e57dcd504eb6f 8069fc1a215aafef; do echo \"######## $f\"; awk '/Etymology$/{c++} c>=2' $f.txt | head -45; echo; done",
 "description": "Print etymology bodies"
}
```


### [2026-09-14T03:17:42.960Z] TOOL RESULT

```
######## 50a196650898362c

######## 9cc4f50b55f5be43

######## 793e57dcd504eb6f
 Etymology
 [ edit ] 

 Inherited from Middle Persian [Book Pahlavi needed] ( hʾkstl /⁠xākestar, xākistar⁠/ ) . This etymology is incomplete. You can help Wiktionary by elaborating on the origins of this term. 

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /xaː.kis.ˈtar/ 

 ( Dari, formal ) IPA ( key ) : [xɑː.kʰɪs.t̪ʰáɾ] 

 ( Dari, formal ) IPA ( key ) : [xɑː.kʰɪs.t̪ʰáɾ] 
 ( Kabuli ) IPA ( key ) : [xɑː.kʰɪs.t̪ʰáɾ] 

 ( Hazaragi ) IPA ( key ) : [xɔː.jiʃ.t̪ʰáɾ] 

 ( Iran, formal ) IPA ( key ) : [xɒː.kʰʲes.t̪ʰǽɹ] 

 ( Tajik, formal ) IPA ( key ) : [χɔ.kʰis.t̪ʰáɾ] 

 Rhymes: -ar 

 Readings

 Classical reading ? 

 xākistar

 Dari reading ? 

 xākistar

 Iranian reading ? 

 xâkestar

 Tajik reading ? 

 xokistar

 Noun
 [ edit ] 

 خاکستر • ( xākistar / xâkestar ) ( plural خاکسترها ( xākistar-hā / xâkestar-hâ ) , Tajik spelling хокистар ) 

######## 8069fc1a215aafef
 Etymology
 [ edit ] 

 Borrowed from Persian بستر ( bestar ) .

 Noun
 [ edit ] 

 بستر • ( bister ) 

 bed , a piece of furniture on which to rest or sleep 
 Synonym: یاتاق ( yatak ) 

 ( in general ) anything spread out on which one may lie or sleep 
 Synonyms: مرقد ( merkad ) , مهاد ( mihad ) , یاتاق ( yatak ) 

 Descendants
 [ edit ] 

 Turkish: bister , pister 

 Further reading
 [ edit ] 

 Çağbayır, Yaşar ( 2007 ), “ bister ”, in Ötüken Türkçe Sözlük (in Turkish), volume 1, Istanbul: Ötüken Neşriyat, page 627 

 Meninski, Franciszek à Mesgnien ( 1687 ), “Lectus”, in Complementum thesauri linguarum orientalium, seu onomasticum latino-turcico-arabico-persicum, simul idem index verborum lexici turcico-arabico-persici, quod latinâ, germanicâ, aliarumque linguarum adjectâ nomenclatione nuper in lucem editum ‎ [1] , Vienna, column 929 

 Meninski, Franciszek à Mesgnien ( 1680 ), “ بستر ”, in Thesaurus linguarum orientalium, Turcicae, Arabicae, Persicae, praecipuas earum opes à Turcis peculiariter usurpatas continens, nimirum Lexicon Turkico-Arabico-Persicum ‎ [2] , Vienna, column 818 

 Redhouse, James W. ( 1890 ), “ بستر ”, in A Turkish and English Lexicon ‎ [3] , Constantinople: A. H. Boyajian, page 364 

 Persian
 [ edit ] 

 Etymology
 [ edit ] 

 Etymology tree

 Proto-Indo-European *h₂m̥bʰi 
 Proto-Indo-Iranian *Habʰí 

 Proto-Indo-European *ster- 
 Proto-Indo-European *sterh₃-
```


## [2026-09-14T03:17:49.299Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"#### sirat\"; grep -n -A25 \"Arabic$\" 50a196650898362c.txt | grep -A25 \"Etymology\" | head -40",
 "description": "Find Arabic sirat etymology"
}
```


### [2026-09-14T03:17:50.385Z] TOOL RESULT

```
#### sirat
153- Etymology
154- [ edit ] 
155-
156- Etymology tree
157-
158- Proto-Indo-European *ster- 
159- Proto-Indo-European *sterh₃- 
160-
161- Proto-Indo-European *-tós 
162-
163- Proto-Indo-European *str̥h₃tós 
164- Proto-Italic *strātos 
165- Latin strātus 
166- Latin via strāta ellip. 
167- Latin strāta der. 
168- Classical Syriac ܐܣܛܪܛ bor. 
169- Arabic صراط 
170-
171- Variant of سِرَاط ( sirāṭ ) . From Classical Syriac ܐܣܛܪܛ ( ˀesṭrāṭ ) , from Latin strāta .
172-
173- Pronunciation
174- [ edit ] 
175-
```


## [2026-09-14T03:17:56.547Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"#### gostardan\"; sed -n '150,200p' 9cc4f50b55f5be43.txt; echo; echo \"#### bestar persian\"; grep -n -A40 \"^ Persian$\" 8069fc1a215aafef.txt | sed -n '1,60p'",
 "description": "Print gostardan and bestar etymologies"
}
```


### [2026-09-14T03:17:57.610Z] TOOL RESULT

```
#### gostardan
 Inherited from Middle Persian wstltn' ( /⁠wistardan⁠/ ) , [ 1 ] [ 2 ] [ 3 ] from Proto-Indo-Iranian *str̥náHti , ultimately from Proto-Indo-European *sterh₃- . Compare Avestan 𐬯𐬙𐬀𐬭- ( star- , “ to spread ” ) ), Latin sternō ( “ to bestrew, sprinkle ” ) , Sanskrit स्तृणाति ( stṛṇā́ti ) , Ancient Greek στόρνῡμι ( stórnūmi ) , Old Church Slavonic (о)строуити ( (o)struiti ) , Old English strewian (whence English strew ).

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /ɡus.tar.ˈdan/ 

 ( Dari, formal ) IPA ( key ) : [ɡʊs.t̪ʰäɾ.d̪án] 

 ( Dari, formal ) IPA ( key ) : [ɡʊs.t̪ʰäɾ.d̪án] 
 ( Kabuli ) IPA ( key ) : [ɡʊs.t̪ʰäɾ.d̪án] 

 ( Hazaragi ) IPA ( key ) : [ɡus.t̪ʰäɾ.d̪án] 

 ( Iran, formal ) IPA ( key ) : [ɡ̥os.t̪ʰæɹ.d̪ǽn] 

 ( Tajik, formal ) IPA ( key ) : [ɡus.t̪ʰäɾ.d̪án] 

 Rhymes: -an 

 Readings

 Classical reading ? 

 gustardan

 Dari reading ? 

 gustardan

 Iranian reading ? 

 gostardan

 Tajik reading ? 

 gustardan

 Verb
 [ edit ] 

 گستردن • ( gustardan  / gostardan ) ( present stem گستر ( gustar  / gostar ) , Tajik spelling густардан ) 

 ( literary ) to spread , to extend 

 Conjugation
 [ edit ] 

 Conjugation of گستردن ( literary Dari Persian )

 infinitive

#### bestar persian
250: Persian
251- [ edit ] 
252-
253- Etymology
254- [ edit ] 
255-
256- Etymology tree
257-
258- Proto-Indo-European *h₂m̥bʰi 
259- Proto-Indo-Iranian *Habʰí 
260-
261- Proto-Indo-European *ster- 
262- Proto-Indo-European *sterh₃- 
263-
264- Persian بستر 
265-
266- From Middle Persian [script needed] ( wstl /⁠wistar⁠/ , “ bedding ” ) , from Proto-Iranian *Habí ( “ to, for ” ) + *starH- ( “ to spread ” ) , from Proto-Indo-Iranian *Habʰí ( “ to, for ” ) + Proto-Indo-European *sterh₃- ( “ to spread, stretch out ” ) . [ 1 ] 
267-
268- Pronunciation
269- [ edit ] 
270-
271- ( Classical Persian ) IPA ( key ) : /bis.ˈtar/ 
272-
273- ( Dari, formal ) IPA ( key ) : [bɪs.t̪ʰäɾ] 
274-
275- ( Dari, formal ) IPA ( key ) : [bɪs.t̪ʰäɾ] 
276- ( Kabuli ) IPA ( key ) : [bɪs.t̪ʰäɾ] 
277-
278- ( Hazaragi ) IPA ( key ) : [bis.t̪ʰäɾ] 
279-
280- ( Iran, formal ) IPA ( key ) : [bæs.t̪ʰæɹ] , [bes.t̪ʰæɹ] 
281-
282- ( Tajik, formal ) IPA ( key ) : [bis.t̪ʰäɾ] 
283-
284- Rhymes: -ar 
285-
286- Readings
287-
288- Classical reading ? 
289-
290- bistar
```


## [2026-09-14T03:18:22.223Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== NYB xak\"; grep -n \"xākistar\\|h’kstl\\|hʾkstl\\|xāk \\|ādurestar\\|āturstar\" NYB_vol2_glossary.txt | head -10; echo \"=== PHD adurestar\"; grep -n \"durestar\" PHD_mackenzie.txt | head -5; echo \"=== ARY gostar\"; grep -n \"گستردن\\|خاکستر\\|بستر\" incoming/ARY/ARY_pages.txt | head -10",
 "description": "Grep Nyberg/MacKenzie/Aryanpur"
}
```


### [2026-09-14T03:18:22.324Z] TOOL RESULT

```
=== NYB xak
=== PHD adurestar
869:   i.ldurestar ['twrystl] ashes.
5981:ashen adurestaren.                       awakening wigriisisn(ih).
5982:ashes adurestar.                         aware agah.
11258:                       \~)                adurestaren   \~~\\"b'
=== ARY gostar
1439:لیترانی (40714ل 7 7/): 1018 برهان قاطع :(خاکستر) ۲۲و ۷۰۲ و(اگر)۵۳
6515:چم این واژه در زبان‌های لیتوانی و لتونی: خاکستر. 1 9
9001:چم این واژه در زبان‌های رمنی: واحد مسافت؛ (در سفر) استراحنگاه؛ بستره استراحت» غنودن,
10997:چم این واژه در زبان ابسلندی کهن؛ بستر» استراحت‌گاه. : :
12945:۱- واژه‌ی فارسی "بستر" (پهلری ۷787۸۸3۴ ,۷۷187۸۸6, ۷۷157۸3 نیز از همین ریشه است (برهان قاطع :
```


## [2026-09-14T03:18:25.916Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '12930,12965p' incoming/ARY/ARY_pages.txt; echo \"=== pdf page tag\"; awk 'NR>=12900 && NR<=12950 && /pdf page/' incoming/ARY/ARY_pages.txt; grep -n \"\\[pdf page\" incoming/ARY/ARY_pages.txt | awk -F'[][ ]' '{print $0}' | awk 'NR%1==0' | sed -n '1,2p'",
 "description": "Print Aryanpur bestar context"
}
```


### [2026-09-14T03:18:27.038Z] TOOL RESULT

```
0۸3 ,8780۲34 روسی (۷لفا9ئلا). ۳071۸7
لاتین (7/0): 878580888 ,875280 برهمی (۷ل0078(/4): ۲۸087883۲1
گرتیک (ع007[1): ۹1۹ ان ایرلندی کهن (للدل! صاه): 1 ادن
ایسلندی کهن (/(010۸۸(ین5 صا0): گالی (تاعلانامه): (21۱ بان
ان برترنی (8870۸): زرا ان
ساکسونی کهن (54000۷ 0: 87801۸71 آلبانی (00ماممهتم: راد ان
فریزی کهن (40اکل۲۶ 2ام): 8783۷۸ :
آلمانی کهن (/۸/ل058 ۶/07 صا0): پسگشت‌ها 5
شید تن 0 ۶000
آلمانی (/050۸): نون ان ان 6 (8185۷) لک ان
انگلیسی کهن 8۸/0574 صا0): 286 :ما02
لک ند ان 4 (5788۸3) ۸۸/2/8
[ انگلیسی (بل3الاه/(): ند ان 5 8
دانمارکی (0۸/837): زد بان برهان قاط : ۱۸۱۶
یادداشت:
۱- واژه‌ی فارسی "بستر" (پهلری ۷787۸۸3۴ ,۷۷187۸۸6, ۷۷157۸3 نیز از همین ریشه است (برهان قاطع :
۸) (8 31۸01633121 :(8500130) 004
پارسی‌پاستان (#لفای۲88 صا0): ۰ 6۸87۸ ای بان
گرتیکه (0077110)+ زسا نگ نت ون آلمانی (050/۸01): لد هلان
6۸ ,87166۸ انگلیسی کهن (تل5لا۸0ظ صا0):
ایسلندی کهن (5(010۸۲۸۸ )+ 876۸0
اد تن انگلیسی (5[4/ا62/0): نان
آلمانی کهن (0570/40۷ 14104 ضان): دانمارکی (0۸/13/7): ده لا ان
ا"ا
[pdf page 436]
1 ٍ
سوئدی (9[752[/57). 87106۸ پسگشت‌ها رد تا رد۲
هلندی (17ع007: لد ۳
لیعوانی (/4271۸0لاب0./72: اند نی 609 (57106) 8
1024 ۸
رون
4 (5713) ,60 (878077) ۱
برهان قاطع + 1۸۴
بادداشت:
۱ 8۸۹۸۷۲1۸7 معتقد است که ریشه‌ی اصلی واژه‌های ژُرمنی این فهرست ناشناخته است.
۲ بازگشت به: گند.
=== pdf page tag
[pdf page 435]
1:[pdf page 1]
10:[pdf page 2]
```


## [2026-09-14T03:18:39.586Z] TOOL CALL #73: Bash

```json
{
 "command": "for u in \"https://www.etymonline.com/word/strategy\" \"https://www.etymonline.com/word/street\" \"https://www.etymonline.com/word/stray\" \"https://www.etymonline.com/word/straw\" \"https://www.etymonline.com/word/stoichiometry\" ; do echo \"### $u\"; timeout 120 python3 tools/fetch_source.py \"$u\" --note \"page 479 verification: Ster 1 English/French derivatives\"; done",
 "description": "Fetch etymonline batch 3"
}
```


### [2026-09-14T03:18:42.066Z] TOOL RESULT

```
### https://www.etymonline.com/word/strategy
/home/sfmqrb/git/rishe/data/verification/sources/web/5a524583a77da29f.txt
### https://www.etymonline.com/word/street
/home/sfmqrb/git/rishe/data/verification/sources/web/f85f78cd7cec9925.txt
### https://www.etymonline.com/word/stray
/home/sfmqrb/git/rishe/data/verification/sources/web/af57c3a69862b35a.txt
### https://www.etymonline.com/word/straw
/home/sfmqrb/git/rishe/data/verification/sources/web/2570acf5c1b8bae5.txt
### https://www.etymonline.com/word/stoichiometry
/home/sfmqrb/git/rishe/data/verification/sources/web/042dbfc873f1d66a.txt
```


## [2026-09-14T03:18:45.095Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in 5a524583a77da29f f85f78cd7cec9925 af57c3a69862b35a 2570acf5c1b8bae5 042dbfc873f1d66a; do echo \"######## $f\"; sed -n '/Origin and history/,/Entries linking/p' $f.txt | head -14; echo; done",
 "description": "Read etymonline batch 3"
}
```


### [2026-09-14T03:18:46.520Z] TOOL RESULT

```
######## 5a524583a77da29f
 Origin and history of strategy 

 strategy (n.) 

 1810, "the art of a general, the science of war," from French stratégie (16c.) and directly from Latinized form of Greek stratēgia "office or command of a general," from stratēgos "general, commander of an army," also the title of various civil officials and magistrates, from stratos "multitude, troop, a division of the people; army, navy, expedition, encamped army," probably originally "a camping army," and meaning etymologically "that which is spread out" (from PIE *str-to- , from root *stere- "to spread"). With Greek agos "leader," from agein "to lead" (from PIE root *ag- "to drive, draw out or forth, move").

 As "an instance of strategy, a particular strategy" by 1833. In non-military use by 1887.
 also from 1810 

 Entries linking to strategy 

######## f85f78cd7cec9925
 Origin and history of street 

 street (n.) 

 Middle English strete , "road in a city or town," also "road from one city or town to another," from Old English stret (Mercian, Kentish), stræt (West Saxon) "street, high road," from Late Latin strata , used elliptically for via strata "paved road." Latin strata is fem. past participle of sternere "lay down, spread out, pave," from PIE *stre-to- "to stretch, extend" (from nasalized form of PIE root *stere- "to spread").

 One of the rare words that has been in use in England continuously from Roman times. An early and widespread Germanic borrowing (Old Frisian strete , Old Saxon strata , Middle Dutch strate , Dutch straat , Old High German straza , German Strasse , Swedish stråt , Danish sträde "street"). The Latin is also the source of Spanish estrada , Old French estrée , Italian strada .

 It was the usual Old English term for Roman roads ( Watling Street, Icknield Street ), "later extended to other roads, urban streets, and in SE dialects to a street of dwellings, a straggling village or hamlet" [Cambridge Dictionary of English Place-Names]. "In the Middle Ages, a road or way was merely a direction in which people rode or went, the name street being reserved for the made road" [Weekley].

 It has been used since late 14c. to mean "the people in the street, inhabitants of a street;" the modern sense of "the realm of the people as the source of political support" dates from 1931. The street for an especially important street is from 1560s (originally of London's Lombard-street). Man in the street "ordinary person, non-expert" is attested from 1831.

 Street people "the homeless, vagrants" is from 1967; the expression on the street "homeless" is from 1852 (by 1728 of women, with implications of prostitution). Street smarts is from 1971; street-credibility is from 1979. Street-preacher is by 1722, originally of Methodists (and sometimes Quakers); street-preaching is by 1838, distinguished by the Methodists from field-preaching . Street-sweeper as an occupation is from 1848.


######## af57c3a69862b35a
 Origin and history of stray 

 stray (v.) 

 c. 1300, straien , of animals, "wander away from an enclosure or herd," also figurative, of persons, "wander from the path of justice or rectitude," a shortening of Old French estraier "wander about, roam, drift, run loose," said of animals, especially a horse without a master, also of persons, perhaps literally "go about the streets," from estree "route, highway," from Late Latin via strata "paved road" (see street ).

 On another theory (reprinted in OED), the Old French word is from Vulgar Latin *estragare , a contraction of *estravagare , representing Latin extra vagari "to wander outside" (see extravagant ). Related: Strayed ; straying .
 also from c. 1300 

 stray (n.) 

 "domestic animal found wandering from its enclosure or proper place," early 13c., strai , a legal term, from Anglo-French stray , estray , noun use of Old French estraié "strayed, riderless," past-participle adjective from estraier "to roam, drift, run loose" (see stray (v.), and compare waif ).
 also from early 13c. 


######## 2570acf5c1b8bae5
 Origin and history of straw 

 straw (n.) 

 Middle English strau , from Old English streaw (rare) "dried stems or stalks of certain grains after threshing," apparently literally "that which is scattered or strewn," related to streowian (see strew ), from PIE root *stere- "to spread."

 The notion perhaps is of dried grain stalks strewn on a floor as carpeting or bedding. As a type of what is trifling or unimportant, attested from late 13c. The meaning "hollow tube through which a drink is sucked" is recorded from 1851.

 As an adjective, "made of straw," mid-15c.; hence "false, sham," as in straw bid (by 1889). Straw poll "vote taken without previous notice or at a casual gathering" is from 1932; earlier straw vote (1866).

 Straw hat , one made of woven or plaited straw, is attested mid-15c. ( strawen hattis ).

 To clutch (or grasp or catch ) at straws (1748) is what a drowning man proverbially would do. The last straw (1836 apart from the full phrase) is from the proverbial "it is the last straw that breaks the camel's back" (or, less often, the mare's, the horse's, or the elephant's), an image in use in English by 1755.


######## 042dbfc873f1d66a
 Origin and history of stoichiometry 

 stoichiometry (n.) 

 also stoicheiometry , "science of calculating the quantities of chemical elements involved in chemical reactions," 1807, from German Stöchiometrie (1792), coined by German chemist Jeremias Benjamin Richter (1762-1807) from Latinized form of Greek stoikheion "one of a row; shadow-line of a sundial," in plural "the elements" (from PIE *steigh- "to stride, step, rise"). Also see -metry "a measuring of." Related: Stoichiometric .
 also from 1807 

 Entries linking to stoichiometry
```


## [2026-09-14T03:18:54.456Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '60349,60360p' LAT.txt; echo \"--- struo ---\"; sed -n '61365,61375p' LAT.txt",
 "description": "Print Ernout-Meillet sterno and struo"
}
```


### [2026-09-14T03:18:54.528Z] TOOL RESULT

```
sterno, -ls, straul, stratum, sternere: «Hendre, coucher k terre;
s. herbas, harSnam, etc., d'ou stratum: couche (de feuillage), etc. ;
ou "joncher de^' s. solum ,te l is ; frequent dans sternere uiam {lapi¬
dibus) "cf.gr.080v oxopevvupu), de la strata (uia ) "chauss<?e"; cf.
M.L.8348 et 8391 strata, 839« stratum "Iit". - Ancien, usuel, class.
Celt.: iri. srdth, srathar "stratum, stratura", britt. ystrodur. A
strata, remontent les formes germ. du type v.h. n.strdzza, v.angl.
stroet.
Derivas: sternax : qui renverse son cavalier (Vg., Sil.); prosterni
(Sid.); —sternium second terme de compos^ dans lecti—sternium
sellisternium, termes du rituel; la forme simple *sternium, que
supposent certaines formes dialectales italiennes, M.L.8349, a du
--- struo ---
struo, -ls, -xi, -ctum, -ere: disposer en piles, "empiler" (des
matEriaux), "entasser, dresser", s. arbores in pyram (en particulier
"dresser une table"), "construire, batir" (sens propre et figurE):
templa saxo structa uetusto Vg.3,04; sycophantias struere Pl.,Asin.
71, "lever"; cf.Lex XII Tab.i,a si caluitur pedemue struit. - Ancien,
usuel, classique. Celt.: gall.ystryw.
DErivEs et composEs: strues,-is f.: pile; en particulier, dans la
1. religieuse, sorte de gateau: — genera liborum erant, digitorum
coniunctorum similia, qui continebantur in transuersum superiecta
panicula, P.F.409,3. A ce sens se rattache le composE strufertarii,
citE par P.F.377,3 -os dicebant qui quaedam sacrificia ad arbores
```


## [2026-09-14T03:19:28.990Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AFM\"; grep -n \"اسطقس\\|أسطقس\" AFM_pages.txt | head -3; echo \"=== FVQ stoich\"; grep -n -i \"ustuqus\\|istaqis\\|stoicheion\" FVQ.txt | head -3; echo \"=== PLA\"; grep -n \"اسطقس\" incoming/PLA/PLA_pages.txt | head -3; echo \"=== LKT\"; grep -n -i \"stoich\\|ustuqus\" LKT.txt | head -3; echo \"=== BQT v1 line 3236 leaf\"; python3 -c \"\ntxt=open('BQT_v1_pages.txt',encoding='utf8',errors='replace').read()\nprint('\\n'.join(txt.split('\\n')[:3236]).count('\\f'))\n\"; echo \"=== ARY sirat/serat\"; grep -n \"صراط\" incoming/ARY/ARY_pages.txt | head -3",
 "description": "Additional greps for Arabic sources"
}
```


### [2026-09-14T03:19:30.035Z] TOOL RESULT

```
=== AFM
=== FVQ stoich
=== PLA
=== LKT
=== BQT v1 line 3236 leaf
108
=== ARY sirat/serat
```


## [2026-09-14T03:19:37.979Z] TOOL CALL #77: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BQT intro leaf108\"; awk 'BEGIN{RS=\"\\f\"} NR==109' BQT_v1_pages.txt | grep -n \"اسطقس\" ; awk 'BEGIN{RS=\"\\f\"} NR==109' BQT_v1_pages.txt | sed -n '1,8p'; echo \"=== AFA sirat\"; grep -n -i \"sirat\\|strata\\|Strasse\" AFA.txt | head -8",
 "description": "Check Borhan intro and Fraenkel"
}
```


### [2026-09-14T03:19:39.035Z] TOOL RESULT

```
=== BQT intro leaf108
20:اسطر تو تاه اسقلینوس» اسطقس» اسطوخودوس » اغلیقی» غسیا» سالامندر|؛
دیگر - در برهان قل شده ازین قبیل است :
اتا » اتايك » انسیز » بلدرچین ( ذیل : سمانه » وذیل: 7 ۰ بلان
( ذیل : سعد )۰ تمر » چسارو ( ذیل : شم ))» سکز » سن » سو » سيك »
صفرجق( ذیل: سوبدی )» طوغان ( ذیل: شاهباز )» قنجوقه (ذیل: سیموت)؛
۳
( ذیل : سست ۱
۸4 - هن.ی موّلف برهان از زبانپای هندی ذیل » لغاتی آورده
است :
=== AFA sirat
3541:S) XXm# «Strasse** dürfte man kaom za ) ^^ a. stellen; eher könnte t'y^
6324:road). Der Serif von Mekka hat nun für die Pilgerstrasse
6394:leute (Handelsstrasse) nach Syrien. Be|qri 416, 8.
9837:aus dem Begriffe der »Strasse*' der Begriff des »Pflasters**
```


## [2026-09-14T03:19:44.485Z] TOOL CALL #78: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '3530,3550p' AFA.txt; echo \"=== leaf\"; python3 -c \"\ntxt=open('AFA.txt',encoding='utf8',errors='replace').read()\nprint('leaf', '\\n'.join(txt.split('\\n')[:3541]).count('\\f'))\"",
 "description": "Print Fraenkel context"
}
```


### [2026-09-14T03:19:45.530Z] TOOL RESULT

```
Der Name des Spiesses (^Jl^ Näb. 5,16^) hat einein
echt arabischen Wörtern nicht häufige Bildung^) und ist
wahrscheinlich erst aus "n£){7 syr. h&&A^ enÜehni
Um zu einigen anderen Hausgerathen überzugehen, die
zur Bereitung von Speisen benutzt werden , so scheint der
Name ^}JoJjt ursemitisch zu sein jüd. aram. KH /^*1D ans
• »nVlnn syr. IAV^V) vgl. Nöldeke Mand. Gr. p. 59 Anm.
Die eigenthümliche Yocalisation des Praformativs mit Damma
1) Aramüsierend geschrieben mit^D.
8) Wahncheinlieh bangt auch tsk^ »xweifeln*^ mit »decken, flechten** ra-
Hunmen; et ist «Terwickelt sein, tn etwas hängen**. .
S) XXm# «Strasse** dürfte man kaom za ) ^^ a. stellen; eher könnte t'y^
data gehören (X^L»Jt ö^t!^ ^'"^ *-^- (J^J^'
«) Vgl Ta'Ub Fasth (Barth) 26, 5.
5) Aach seheint das Braten am Spiease bei den Armbern nicht sehr gewöhn-
lieh gewesen xn sein.91
statt des gewöhnlichen t oder a ist gewiss durch das Za-
sammentreffen des Lippenlautes mit dem Nasal herrorge-
rufen. Auch sonst lieben Nasale die dunkleren Vocale;
vgl. ps^LSj für urspr. IXiJSJ u. a. Hier hat noch der
Lippenlaut mitge%Yirkt. Wenn man die aramäische Form
=== leaf
leaf 120
```


## [2026-09-14T03:19:49.724Z] TOOL CALL #79: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==56' AFA.txt | head -30",
 "description": "Print Fraenkel page 25"
}
```


### [2026-09-14T03:19:50.766Z] TOOL RESULT

```
25
sie zwischen Formen mit anlautendem und K auch sonst
im Aramäischen treffen, so dass man auf eiu aramäisches
Oriijinal •snsnSO schliessen darf, das in anderer, an
anderer Stelle zu besprechender Bedeutung, gerade auch
im Wechsel mit Nn3*'^3» wirklich vorkommt. — Als
Nebenform Ton v^lswo findet sich mit einer bei R und
einem Zischlaute sehr erklärlichen Umstellung v^Kwa. Daher
ist wahrscheinlich v^^ erst secuudiir gebildet. Mit ,.£i,•^ PSm.
1152 hat es nichts zu thun. Zerhis Pliuius VI, 118? [aus
Xiilß entstellt. Nüld.] Eudlich küunteu sogar noch v^^ u. ii.
vielleicht hierher gezogen werden, wenn dies nicht durch
äthiop. aanib gehalten würde.
Genügend ausführlich behandelt findet sich noch ein
anderes Wort für Wasserleitung Jt^r * schon bei Dozy II.
344, der es richtig mit ca^tellum identificiert. Aramäisch 7l2Dp
^irüch s. V. 7t2Dp I wnd wohl auch ) A > >^^ Elia bei
Lagarde Praeterm. 22, 84; Gast. 814 bildeten die Ver-
mittelung. — ^yÄ« Dozy I. 189 ist entlehnt aus jj^- PSm.
692.
Zweifellos übernommen ist auch %IÄ|. »Dach.** Yer-
dächtig ist schon , dass es von Gauh. als dem syrischen und
higäzischen Dialecte angehürig bezeichnet wird. Es giebt
ferner eine Nebenform «La^I; die Bildung ist durchaus
unarabisch und endlich hat es auch im Arabischen keine
Ableitung. Das Original ist Ij'^X jjJr (vielleicht zur Wur-
zel "njK »häufen** »schichten'*).
N X.5^^ U ^yi ^^ v^^< tLiy Et fehlt in dieser Bcdeatoog aach
bei Dozj; ich ÜDde es aber bei H&i zu KeUm 31. l s. ?. On«U tU Erklimag
von 113; .im Anbischcn 3nT8C" «■ s^^^'.
```


## [2026-09-14T03:20:04.965Z] TOOL CALL #80: Bash

```json
{
 "command": "sed -n '1,40p' tools/verify_archive_sources.py",
 "description": "Inspect verify_archive_sources.py"
}
```


### [2026-09-14T03:20:05.018Z] TOOL RESULT

```
#!/usr/bin/env python3
"""Archive every URL cited in data/verification/page-*.json that is not yet in
data/verification/sources/web/index.jsonl (post-pass, so no cited source is lost
even if an agent forgot to archive it).  Usage: verify_archive_sources.py [pages...]
"""
import sys, os, glob, json, subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VER = os.path.join(ROOT, "data", "verification")
INDEX = os.path.join(VER, "sources", "web", "index.jsonl")

def indexed():
    s = set()
    if os.path.exists(INDEX):
        for line in open(INDEX, encoding="utf-8"):
            try:
                d = json.loads(line)
                if d.get("status") == 200:
                    s.add(d["url"])
            except Exception:
                pass
    return s

def main(argv):
    only = set(argv[1:])
    have = indexed()
    todo = {}
    for f in sorted(glob.glob(os.path.join(VER, "page-*.json"))):
        pg = os.path.basename(f)[5:-5]
        if only and pg not in only:
            continue
        d = json.load(open(f, encoding="utf-8"))
        for e in d.get("entries", []):
            for u in e.get("sources") or []:
                todo.setdefault(u, f"page {pg}, root {e.get('root')} (root-level)")
            for n in e.get("nodes", []):
                for u in n.get("sources") or []:
                    todo.setdefault(u, f"page {pg}, root {e.get('root')}, node #{n.get('id')} {n.get('words','')}")
    missing = [u for u in todo if u not in have]
    print(f"{len(todo)} cited URLs, {len(missing)} not yet archived")
```


## [2026-09-14T03:28:07.473Z] TOOL CALL #81: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-479.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, os\n\nW = \"https://en.wiktionary.org/wiki/\"\nU_STEYGH = W + \"Reconstruction:Proto-Indo-European/steyg%CA%B0-\"\nU_STERH3 = W + \"Reconstruction:Proto-Indo-European/sterh%E2%82%83-\"\nU_STOIKH = W + \"%CF%83%CF%84%CE%BF%CE%B9%CF%87%CE%B5%E1%BF%96%CE%BF%CE%BD\"\nU_SIRAT  = W + \"%D8%B5%D8%B1%D8%A7%D8%B7\"\nU_GOST   = W + \"%DA%AF%D8%B3%D8%AA%D8%B1%D8%AF%D9%86\"\nU_XAK    = W + \"%D8%AE%D8%A7%DA%A9%D8%B3%D8%AA%D8%B1\"\nU_BESTAR = W + \"%D8%A8%D8%B3%D8%AA%D8%B1\"\nE = \"https://www.etymonline.com/word/\"\n\ndoc = {\n \"pdf_page\": 479,\n \"book_page\": 449,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-13\",\n \"entries\": [\n  {\n   \"entry\": 0,\n   \"root\": \"Steigh, Stoigh\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE *steygʰ- 'to stride, step, go, climb' (Pokorny 1017-1018 steigh- 'schreiten, steigen')\",\n   \"note\": \"Root, language label and gloss are all correct. Pokorny's entry 'steigh- / Meaning: to march, ascend / Page(s): 1017-1018' matches Nourai's POK:1017 exactly, and Watkins/AHD heads the entry 'steigh-. To stride, step, rise' — Nourai's gloss is copied verbatim from AHD. The o-grade variant 'Stoigh' that Nourai adds to the headword is the real ablaut grade *stoygʰ- that yields Gk. stoîkhos/stoikheîon and Gmc. *staigrī. Modern Wiktionary/LIV write the root *steygʰ- 'to go, to climb'; the semantic label 'rise/ascend' is the Germanic-Indic specialisation, so there is no substantive disagreement.\",\n   \"note_fa\": \"ریشهٔ هندواروپایی آغازین *steygʰ- «گام برداشتن، بالا رفتن»؛ پوکورنی (ص ۱۰۱۷–۱۰۱۸) آن را steigh- «schreiten, steigen» آورده و واتکینز در پیوست AHD دقیقاً با همین معنی «to stride, step, rise». صورت دوم عنوان (Stoigh) همان پایهٔ o-دار *stoygʰ- است که στοῖχος و στοιχεῖον یونانی و *staigrī ژرمنی از آن برآمده‌اند. برچسب زبانی، شمارهٔ صفحه و معنای ریشه هر سه درست است؛ ادعای نورایی دربارهٔ خودِ ریشه درست است.\",\n   \"sources\": [U_STEYGH, E + \"stair\"],\n   \"ref_check\": [\n    {\"ref\": \"POK:1017\", \"status\": \"supports\",\n     \"note\": \"POK_full.txt (grep -n 'lemma: steigh'): 'Root / lemma: steigh- / Meaning: to march, ascend … References: WP. II 614 f., Trautmann 285 f. / Page(s): 1017-1018'. Exactly Nourai's page and gloss.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"WLD\", \"where\": \"Bd. II 614 (WLD_Bd2_pages.txt leaf 618)\", \"stance\": \"supports\",\n     \"note\": \"'steigh- „schreiten, steigen“. Ai. stighnoti „steigt“ … gr. στείχω „schreite, gehe“, στίχος „Reihe, Zeile“ … στοῖχος „Reihe, Linie“' — the whole Greek/Sanskrit side of Nourai's chart is here.\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.v. steigh- (AHD_watkins1985.txt line 1011)\", \"stance\": \"supports\",\n     \"note\": \"'steigh-. To stride, step, rise. … III. O-grade form *stoigh-. 1. Suffixed form *stoigh-ri- in Germanic *staigri in Old English stéger, stair, step: STAIR. 2. Greek stoikheion, shadow line, element: STOICHIOMETRY. [Pok. steigh- 1017.]'\"},\n    {\"src\": \"IEC\", \"where\": \"Mann, s.v. steigh- region\", \"stance\": \"silent\",\n     \"note\": \"grep 'steigh' in IEC.txt returned no headword block for this root (Mann's arrangement splits it under stigh-/stoigh- forms); recorded as silent.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1, \"lang\": \"Greek\", \"words\": \"stoixeion\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Gk. στοιχεῖον (stoikheîon) is στοῖχος (stoîkhos) 'row, line, rank' + the diminutive/instrument suffix -εῖον; στοῖχος is the o-grade *stoygʰ-o- of *steygʰ- 'to step, march in order' (cf. στείχειν 'to march in order'). Its oldest concrete sense is the one Nourai prints: 'one of a row' and specifically the shadow-line of the gnomon on a sundial that advances hour by hour (Aristophanes, Eccl. 652); from 'one of a series, a component part' Plato and Aristotle made it the technical word for 'element' (letter of the alphabet, physical element). The step Greek → 'element' is thus internal to Greek, 5th-4th c. BCE.\",\n     \"derivation_fa\": \"واژهٔ یونانی στοιχεῖον از στοῖχος «رده، صف» و پسوند -εῖον ساخته شده و στοῖχος خود صورت o-دار ریشهٔ *steygʰ- است (قس. στείχειν «پشت سر هم گام برداشتن»). نخستین معنای آن همان است که نورایی آورده: «سایهٔ شاخص ساعت آفتابی که ساعت‌به‌ساعت پیش می‌رود» (آریستوفانس، ۳۹۱ پ.م)، و از معنای «یکی از یک رده، جزء» افلاطون و ارسطو آن را به معنی «عنصر» به کار بردند. پس تحول معنایی درون خودِ یونانی روی داده و ادعای نورایی درست است.\",\n     \"sources\": [U_STOIKH, E + \"stoichiometry\"],\n     \"ref_check\": [\n      {\"ref\": \"POK:107\", \"status\": \"not_found\",\n       \"note\": \"POK_01.txt leaf 115 (= printed p.107, offset leaf = p+8) is the bhā-/bhabhā 'Bohne, Saubohne' article — nothing to do with steigh-. Almost certainly a misprint for POK:1017, where στοῖχος is in fact listed ('στοῖχος \\\"Reihe, Linie\\\"').\"},\n      {\"ref\": \"AHD\", \"status\": \"supports\",\n       \"note\": \"AHD_watkins1985.txt line 1011, s.v. steigh-: 'III. O-grade form *stoigh-. … 2. Greek stoikheion, shadow line, element: STOICHIOMETRY.' Nourai's gloss 'shadow line, element' is word-for-word AHD's.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"KLN_1966.txt leaf 807-808 (≈ p.1522), s.v. stoichiometry\", \"stance\": \"supports\",\n       \"note\": \"'… fr. Gk. στοιχεῖον, \\\"element\\\" … The first element is a derivative of στοῖχος, \\\"row, line, rank\\\", which is rel. to στίχος … στείχειν, \\\"to go; to march in order\\\"; see stichic.'\"},\n      {\"src\": \"WLD\", \"where\": \"Bd. II 614 (leaf 618)\", \"stance\": \"supports\",\n       \"note\": \"under steigh-: 'στοῖχος „Reihe, Linie“' listed beside στίχος.\"}\n     ]\n    },\n    {\n     \"id\": 2, \"lang\": \"Arabic\", \"words\": \"estoqos\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Arabic إسطقس / أسطقس (usṭuqus, isṭaqis) 'element (of the four elements)' is a Greek loan of the translation movement: στοιχεῖον entered Arabic through Syriac scientific prose (ʾsṭwqs), Greek στ- being rendered by the emphatic س+ط cluster and the Greek neuter -ον dropped, with the prosthetic alif normal for Arabic loans beginning with a consonant cluster. It is a dead loan with no Arabic root: the Arab lexicographers list it among the dakhīl, and its plural is the foreign-style أسطقسات.\",\n     \"derivation_fa\": \"واژهٔ عربی «اُسطُقُس / إسطقس» به معنی «عنصر» وام‌واژه‌ای یونانی است که در نهضت ترجمه و از راه متون سریانی (ʾsṭwqs) وارد عربی شد: خوشهٔ آغازین στ- یونانی با «س+ط» بازنموده شده، پایانهٔ خنثای -ον افتاده و الف آغازین (الف وصل) طبق قاعدهٔ عربی برای واژه‌های دارای خوشهٔ آغازین افزوده شده است. این واژه ریشهٔ عربی ندارد و فرهنگ‌نویسان عرب آن را در شمار «دخیل» آورده‌اند؛ جمع آن نیز «اسطقسات» است. ادعای نورایی درست است.\",\n     \"sources\": [U_STOIKH],\n     \"ref_check\": [\n      {\"ref\": \"TAD:3\", \"status\": \"supports\",\n       \"note\": \"TAD_pages.txt leaf 6 (printed ≈ p.2-3; offset leaf−4..6), between إسطرلاب and إسطول: '… يوناني [στοιχεῖον] معناه عنصر وأصل' — al-Unaysi lists the word as Greek with the sense 'element', exactly Nourai's arrow.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"KLN_1966.txt s.v. stoichiometry (leaf 807-808)\", \"stance\": \"supports\",\n       \"note\": \"gives Gk. στοιχεῖον 'element' as the etymon of the learned European word; the same Greek source-word Arabic borrowed.\"},\n      {\"src\": \"FVQ\", \"where\": \"FVQ.txt / FVQ_pages.txt\", \"stance\": \"silent\",\n       \"note\": \"grep 'ustuqus', 'istaqis', 'stoicheion': no hit — Jeffery covers only Qurʾānic vocabulary and إسطقس is post-Qurʾānic.\"},\n      {\"src\": \"AFM\", \"where\": \"AFM_pages.txt\", \"stance\": \"silent\",\n       \"note\": \"grep 'اسطقس' / 'أسطقس': no hit — Addi Shir lists Persian Arabisms, and this word is Greek, not Persian.\"},\n      {\"src\": \"PLA\", \"where\": \"incoming/PLA/PLA_pages.txt\", \"stance\": \"silent\",\n       \"note\": \"grep 'اسطقس': no hit (Asbaghi covers Persian loans in Arabic only).\"}\n     ]\n    },\n    {\n     \"id\": 3, \"lang\": \"Persian\", \"words\": \"ostoqos\", \"verdict\": \"confirmed\",\n     \"derivation\": \"New Persian اُسطُقُس (ostoqos) is the Arabic form taken over unchanged in the medieval philosophical/medical literature (Avicenna's 'ʿanāṣir-e arbaʿa' terminology); Mo'in glosses it 'مایه، مادّه، اصل هر چیز، مادّهٔ نخستین، هیولی' and 'استخوان‌بندی هر چیز، آنچه مایهٔ قوام و دوام چیزهاست' — which is exactly Nourai's 'substance, strength' — with the plural اسطقسات. Mo'in tags it as Arabized Greek, so the route Greek → (Syriac) → Arabic → Persian drawn on the chart is right; it is not a direct Greek loan into Persian.\",\n     \"derivation_fa\": \"«اُسطُقُس» در فارسی وام‌واژه‌ای است که از عربی گرفته شده، نه یکراست از یونانی؛ در متون فلسفی و طبی (عناصر اربعه) رواج داشته است. معین آن را «معرّبِ یونانی» می‌داند و چنین معنی می‌کند: «مایه، مادّه، اصل هر چیز، مادّهٔ نخستین، هیولی… استخوان‌بندی هر چیز، آنچه مایهٔ قوام و دوام چیزهاست»، که همان «substance, strength» نورایی است؛ جمع آن «اسطقسات» است. پس زنجیرهٔ یونانی ← (سریانی) ← عربی ← فارسی که در نمودار آمده درست است.\",\n     \"sources\": [U_STOIKH],\n     \"ref_check\": [\n      {\"ref\": \"MON:266\", \"status\": \"supports\",\n       \"note\": \"MON_part1.txt line 12788: 'اسطقس (ostoqos) [معرّب … عنصر و اصل] (اِ.) مایه، مادّه، اصل هر چیز، مادّهٔ نخستین … استخوان‌بندی هر چیز، آنچه مایهٔ قوام و دوام چیزها است؛ ج. اسطقسات.' Content matches; the printed page number of the 6-vol. edition cannot be mapped because the only online Moʿin text is the 2-vol. abridgement without pagination.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"BQT\", \"where\": \"BQT_v1_pages.txt leaf 108 (Moʿin's introduction, §on Greek words in the Borhān)\", \"stance\": \"supports\",\n       \"note\": \"'… اسقلینوس، اسطقس، اسطوخودوس، اغلیقی …' — Moʿin lists اسطقس among the Greek-origin words of the Borhān-e Qāṭeʿ.\"},\n      {\"src\": \"MON\", \"where\": \"MON_part1.txt lines 12788-12795\", \"stance\": \"supports\",\n       \"note\": \"also the plural entry 'اسطقسات [معر. یو. ع.] … عنصرهای نخستین هر چیز، عناصر اربعه' — an explicit Greek→Arabic→Persian tag.\"},\n      {\"src\": \"ARY\", \"where\": \"incoming/ARY/ARY_pages.txt\", \"stance\": \"silent\",\n       \"note\": \"grep 'اسطقس': no hit — Aryanpur's dictionary covers only Indo-European inherited vocabulary of Persian, not Arabized Greek loans.\"}\n     ]\n    },\n    {\n     \"id\": 4, \"lang\": \"English\", \"words\": \"stoichiometry\", \"verdict\": \"confirmed\",\n     \"derivation\": \"English 'stoichiometry' (1807) is not a direct borrowing from Greek but from German Stöchiometrie, coined in 1792 by the chemist Jeremias Benjamin Richter in his 'Anfangsgründe der Stöchyometrie oder Meßkunst chymischer Elemente' from Gk. στοιχεῖον 'element' + -μετρία 'measuring'. Nourai's arrow Greek → English therefore compresses a modern learned coinage, but the Greek etymon and the sense 'determining the (quantities of) elements' are right.\",\n     \"derivation_fa\": \"واژهٔ انگلیسی stoichiometry (۱۸۰۷ م) وام مستقیم از یونانی نیست، بلکه از آلمانیِ Stöchiometrie گرفته شده که یرمیاس بنیامین ریشتر، شیمی‌دان آلمانی، در ۱۷۹۲ م از στοιχεῖον «عنصر» و -μετρία «اندازه‌گیری» ساخت. بنابراین پیکان «یونانی ← انگلیسی» در نمودار، یک برساختهٔ علمیِ نو را فشرده کرده است؛ اما ریشهٔ یونانی و معنای «سنجش عناصر» درست است.\",\n     \"sources\": [E + \"stoichiometry\"],\n     \"ref_check\": [\n      {\"ref\": \"AHD:1269\", \"status\": \"supports\",\n       \"note\": \"Nourai's AHD page numbers here are the main-dictionary pages of the New College edition (st- words around pp.1268-1273), not the IE appendix; the Watkins appendix entry steigh- does list 'Greek stoikheion … : STOICHIOMETRY' (AHD_watkins1985.txt line 1011), i.e. the same claim.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"KLN_1966.txt s.v. stoichiometry (leaf 807-808, ≈ p.1522)\", \"stance\": \"supports\",\n       \"note\": \"'G. Stöchiometrie, lit. \\\"measurement of elements\\\", coined by the German chemist Jeremias Benjamin Richter (1762-1807) … fr. Gk. στοιχεῖον, \\\"element\\\", and -μετρία.'\"},\n      {\"src\": \"SKT\", \"where\": \"SKT.txt\", \"stance\": \"silent\",\n       \"note\": \"grep 'stoich': Skeat's concise dictionary has no entry for this technical term.\"}\n     ]\n    },\n    {\n     \"id\": 5, \"lang\": \"Sanskrit\", \"words\": \"stiğnôti\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Sanskrit स्तिघ्नोति stighnóti 'he mounts, steps up, rises' is the nu-present *stigʰ-néw-ti of the zero grade *stigʰ- of *steygʰ-; it is a Dhātupāṭha form, with the Vedic derivatives pra-stighnuyāt (opt. 'may he rise up') and ati-stigham (inf. 'to overstep, master') actually attested. Nourai's transliteration 'stiğnôti' uses ğ for gh and ô for the o of the 3sg ending; the form and the gloss are correct.\",\n     \"derivation_fa\": \"سنسکریت stighnóti «بالا می‌رود، گام برمی‌دارد» صورت حالِ نو (nu-present) از پایهٔ صفرِ *stigʰ- ریشهٔ *steygʰ- است؛ خودِ فعل از دهاتوپاٹهه نقل شده و گواه‌های ودایی آن pra-stighnuyāt و ati-stigham است. آوانگاری نورایی (ğ برای gh) و معنای «او بالا می‌رود» درست است؛ پوکورنی و ویکی‌واژه هر دو همین را می‌گویند.\",\n     \"sources\": [U_STEYGH],\n     \"ref_check\": [\n      {\"ref\": \"POK:1017\", \"status\": \"supports\",\n       \"note\": \"POK_full.txt s.v. steigh-: 'Old Indie stighn[ó]ti … ved. pra-stighnuyat … ati-stigham … \\\"übersteigen, bemeistern\\\"'.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"WLD\", \"where\": \"Bd. II 614 (leaf 618)\", \"stance\": \"supports\",\n       \"note\": \"'Ai. stighnoti „steigt“ (Dhātup.), ved. pra-stighnuyat Opt. praes. „er möge emporkommen“'.\"},\n      {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. steigh-\", \"stance\": \"partial\",\n       \"note\": \"Watkins lists only the European reflexes under steigh-; the Sanskrit verb is implicit in the Pokorny reference. Etymonline s.v. stair repeats 'Sanskrit stighnoti \\\"mounts, rises, steps\\\"'.\"}\n     ]\n    },\n    {\n     \"id\": 6, \"lang\": \"Greek\", \"words\": \"stixos\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Gk. στίχος (stíkhos) 'row, line, rank; line of verse' is the zero-grade *stigʰ-o- beside στείχειν 'to march in order' and the o-grade στοῖχος; the Attic form στίχος with short i is the regular outcome. From it English has the learned words stich, distich, hemistich, acrostic, stichomythia and cadaster, all through Latin or French.\",\n     \"derivation_fa\": \"یونانی στίχος «رده، سطر، مصراع» صورت پایهٔ صفرِ *stigʰ-o- در کنار στείχειν «منظم گام برداشتن» و στοῖχος (پایهٔ o) است. واژه‌های عالمانهٔ انگلیسی stich، distich، hemistich، acrostic و stichomythia همه از همین στίχος و از راه لاتینی/فرانسوی به انگلیسی رسیده‌اند. ادعای نورایی دربارهٔ این گره درست است.\",\n     \"sources\": [U_STEYGH, E + \"stair\"],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"supports\",\n       \"note\": \"AHD_watkins1985.txt line 1011, steigh- II.3: 'Suffixed form *stigh-o- in Greek stikhos, row, line, line of verse: STICH; ACROSTIC, CADASTER, DISTICH, HEMISTICH, ORTHOSTICHOUS, STICHOMETRY, STICHOMYTHIA.'\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"POK\", \"where\": \"POK_full.txt s.v. steigh- (p.1017)\", \"stance\": \"supports\",\n       \"note\": \"'gr. στείχω \\\"schreite, gehe\\\", *στίξ, Gen. στιχός, Pl. στίχες, -ας \\\"Reihe, Zeile\\\", Attic στίχος \\\"Reihe, Zeile, Linie\\\"'.\"},\n      {\"src\": \"KLN\", \"where\": \"KLN_1966.txt s.v. acrostic (line 1519)\", \"stance\": \"supports\",\n       \"note\": \"'Gk. ἀκροστιχίς … and στίχος, \\\"row, line, rank, verse\\\", which is rel. to στείχειν, \\\"to go; to march in order\\\".'\"}\n     ]\n    },\n    {\n     \"id\": 7, \"lang\": \"English\", \"words\": \"stitch\", \"verdict\": \"transcription_suspect\",\n     \"derivation\": \"The printed page really does read 'stitch', but English stitch does NOT come from Greek στίχος. Every modern authority — including Nourai's own AHD — derives it from the homonymous but distinct root *steig- 'to stick, prick': ME stiche < OE stice 'a prick, puncture, sting' < PGmc *stikiz (OHG stih, Ger. Stich), AHD steig- I.2 'Suffixed form *stig-i- in Germanic *stikiz in Old English stice, a sting, prick: STITCH. [Pok. steig- 1016]'. The English derivative that does belong under Greek στίχος is 'stich' (a line of verse, with acrostic, distich, hemistich), which AHD prints in the very entry Nourai is copying. This is a one-letter slip by the author (stich → stitch), not an extraction error: the JSON faithfully reproduces the page.\",\n     \"derivation_fa\": \"در صفحهٔ چاپی هم «stitch» آمده است، اما واژهٔ انگلیسی stitch «بخیه» از στίχος یونانی نیامده. همهٔ منابع امروزی — از جمله همان AHD که نورایی به آن ارجاع می‌دهد — آن را از ریشهٔ جداگانهٔ *steig- «سوراخ کردن، نیش زدن» می‌گیرند: انگلیسی میانه stiche < انگلیسی کهن stice «نیش، سوراخ» < ژرمنی آغازین *stikiz (آلمانی Stich). آنچه به‌راستی زیر στίχος می‌نشیند واژهٔ stich «مصراع» است (و acrostic و distich و hemistich). پس این خطای چاپی/قلمی خودِ کتاب است (stich به‌جای stitch) و خطای خوانش اسکن نیست.\",\n     \"error_in\": \"book\",\n     \"book_prints\": \"stitch\",\n     \"correct_form\": \"stich\",\n     \"sources\": [E + \"stitch\", E + \"stair\"],\n     \"ref_check\": [\n      {\"ref\": \"AHD:1268\", \"status\": \"contradicts\",\n       \"note\": \"AHD_watkins1985.txt line 1010, s.v. steig- 'To stick; pointed': '2. Suffixed form *stig-i- in Germanic *stikiz in Old English stice, a sting, prick: STITCH. … [Pok. steig- 1016.]' — AHD puts STITCH under a different root, and puts STICH (not stitch) under stikhos at steigh-.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"KLN_1966.txt line 36842, s.v. stitch\", \"stance\": \"contradicts\",\n       \"note\": \"'stitch, n. — ME. stiche, fr. OE. stice, \\\"puncture, stab, stitch, stitching\\\", rel. to OE. stician, \\\"to prick\\\". See stick, v.'\"},\n      {\"src\": \"SKT\", \"where\": \"SKT.txt line 18590\", \"stance\": \"contradicts\",\n       \"note\": \"'Stitch; see Stick.' — Skeat likewise files it under stick, not under the στίχος family.\"},\n      {\"src\": \"POK\", \"where\": \"POK_full.txt s.v. (s)teig- 'to stick; sharp' (p.1016)\", \"stance\": \"contradicts\",\n       \"note\": \"the Germanic *stik- words stand under (s)teig-, a root Pokorny keeps separate from steigh- 1017.\"}\n     ]\n    },\n    {\n     \"id\": 8, \"lang\": \"Germanic\", \"words\": \"staigrî\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Proto-Germanic *staigrī 'stair, flight of steps' is the suffixed o-grade *stoygʰ-ri- of *steygʰ-, beside *staigrī 'steep' and the verb *stīganą 'to climb' (Goth. steigan, OHG stīgan, OE stīgan 'ascend', whence English sty 'to rise'). Cognates: MDu. stegher, Du. steiger 'stair, scaffold, quay', Ger. Steig 'path'. Nourai's transliteration staigrî = *staigrī; the gloss 'stair, step' is AHD's.\",\n     \"derivation_fa\": \"ژرمنی آغازین *staigrī «پلکان، پله» صورت پسوندگرفتهٔ پایهٔ o یعنی *stoygʰ-ri- از ریشهٔ *steygʰ- است و در کنار فعل *stīganą «بالا رفتن» می‌ایستد (گوتی steigan، آلمانی کهن stīgan، انگلیسی کهن stīgan). هم‌ریشه‌های آن: هلندی میانه stegher و هلندی steiger «پله، داربست»، آلمانی Steig «کوره‌راه». آوانگاری نورایی و معنای «پله» درست است.\",\n     \"sources\": [U_STEYGH, E + \"stair\"],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"supports\",\n       \"note\": \"AHD_watkins1985.txt line 1011, steigh- III.1: 'Suffixed form *stoigh-ri- in Germanic *staigri in Old English stéger, stair, step: STAIR.'\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"KLN_1966.txt line 36543, s.v. stair\", \"stance\": \"supports\",\n       \"note\": \"'fr. OE. stæger, fr. *stāg-ir, fr. Teut. base *staig-, *stig-, corresponding to I.-E. *stigh-.'\"},\n      {\"src\": \"POK\", \"where\": \"POK_full.txt s.v. steigh- (p.1017)\", \"stance\": \"supports\",\n       \"note\": \"'Old English stæger. \\\"Treppe\\\" (engl. stair)' listed among the Germanic reflexes.\"}\n     ]\n    },\n    {\n     \"id\": 9, \"lang\": \"English\", \"words\": \"stair\", \"verdict\": \"confirmed\",\n     \"derivation\": \"OE stǣger 'stair, staircase, flight of steps' (< PGmc *staigrī) > ME steir/steyer > modern stair; originally a collective plural, with 'stairs' remade by late 14c. and 'stair' = 'one of a succession of steps' from the 1520s. An entirely regular native inheritance, no borrowing involved.\",\n     \"derivation_fa\": \"انگلیسی stair از انگلیسی کهن stǣger «پلکان» (از *staigrī ژرمنی) و سپس انگلیسی میانه steir برآمده است؛ در آغاز جمعِ جمعی بوده و از سدهٔ چهاردهم صورت stairs و از سدهٔ شانزدهم معنای «یک پله» پیدا شده. این یک میراث بومیِ ژرمنی است و هیچ وام‌گیری در کار نیست؛ ادعای نورایی درست است.\",\n     \"sources\": [E + \"stair\"],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"supports\",\n       \"note\": \"AHD_watkins1985.txt steigh- III.1 ends '… in Old English stéger, stair, step: STAIR.'\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"KLN_1966.txt line 36543\", \"stance\": \"supports\",\n       \"note\": \"'stair, n. — ME. steyer, steir, fr. OE. stæger … See sty, \\\"to ascend\\\".'\"},\n      {\"src\": \"SKT\", \"where\": \"SKT.txt line 18296\", \"stance\": \"supports\",\n       \"note\": \"'Stair, n. step … A.S. stæger, a stair, step; lit. \\\"a step to climb by\\\" … Allied to Skt. stigh, to ascend, Gk. στείχειν. (√STIGH.)'\"}\n     ]\n    }\n   ]\n  },\n  {\n   \"entry\": 2,\n   \"root\": \"Ster 1, Stor, Str\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE *sterh₃- / *ster- 'to spread, strew, stretch out' (Pokorny 1029-1031, 5. ster-)\",\n   \"note\": \"Pokorny's 5. ster-, sterə- : strē-, steru- : streu- 'to widen, to scatter' stands on pp. 1029-1031 — Nourai's POK:1029 is exact, and his three headword shapes Ster/Stor/Str are Pokorny's own e-, o- and zero-grades. Watkins heads the same root 'ster-2. Also sterə-. To spread. [Pok. 5. ster- 1029.]'. Modern reconstruction writes *sterh₃-, with *strew- as an extension — the laryngeal notation is the only difference from Nourai. All four language-branch children of the root box (Avestan, Latin, Greek, Germanic) are Pokorny's own.\",\n   \"note_fa\": \"ریشهٔ هندواروپایی آغازین *sterh₃-/*ster- «گستردن، پراکندن»؛ پوکورنی آن را با شمارهٔ ۵ و در صفحات ۱۰۲۹–۱۰۳۱ آورده، پس ارجاع POK:1029 نورایی دقیق است و سه صورتِ عنوان (Ster/Stor/Str) همان پایه‌های e، o و صفرِ پوکورنی است. واتکینز نیز می‌نویسد: «ster-2 … To spread. [Pok. 5. ster- 1029]». بازسازی امروزی *sterh₃- است و گسترش *strew- را جدا می‌کند؛ تنها تفاوت، نشانهٔ حنجره‌ای است. ادعای نورایی دربارهٔ خود ریشه درست است.\",\n   \"sources\": [U_STERH3],\n   \"ref_check\": [\n    {\"ref\": \"POK:1029\", \"status\": \"supports\",\n     \"note\": \"POK_full.txt: 'Root / lemma: ster-5, sterə- : strē-, steru- : streu- / Meaning: to widen, to scatter … References: WP. II 638 ff. … / Page(s): 1029-1031'.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"WLD\", \"where\": \"Bd. II 638-641 (WLD_Bd2_pages.txt leaf 643 = p.639)\", \"stance\": \"supports\",\n     \"note\": \"'ster-' article: 'Lat. sterno, -ere „auf den Boden hinstreuen, hinbreiten“, Ptc. stratus (*sterətos) … (στρατεία, στρατηγός)'.\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.v. ster-2 (AHD_watkins1985.txt line 1018)\", \"stance\": \"supports\",\n     \"note\": \"'ster-2. Also sterə-. To spread. I. Extended form *streu- … Latin struere … 3. Zero-grade form *stru- in Latin industria … III. … Latin sternere (past participle strātus …): STRATUS, STREET … IV. … Greek stratos, multitude, army … [Pok. 5. ster- 1029.]' — the whole chart in one entry.\"},\n    {\"src\": \"IEC\", \"where\": \"Mann, IEC.txt line 17198 and 17213 (s.v. ster-, sterō)\", \"stance\": \"supports\",\n     \"note\": \"'ster-, e-gde of radical str- … Skt. stare … Av. star-, id.; Per. cf. gu-stardan, inf. id.; gu-star, s. \\\"spreader\\\" (fr. *ue-); Lat. cf. sterno' — Mann even has the Persian verb.\"},\n    {\"src\": \"CHEUNG\", \"where\": \"CHEUNG.txt p.365, *starH₁ 'to spread'\", \"stance\": \"supports\",\n     \"note\": \"'«PIE *sterH₁- \\\"to spread, extend\\\" = LIV: 597 f. | Pok.: 1029 f.' with Avestan, MP and NP reflexes.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1, \"lang\": \"Avestan\", \"words\": \"star 1; wi-star\", \"verdict\": \"plausible\",\n     \"derivation\": \"Young Avestan star- 'sternere, to spread, strew' is securely attested (Bartholomae col. 1596-98 '¹star- V. \\\"sternere\\\", Praes. 1 star-, 10 stərənu-, 11 stərənā-; PPfP. starəta-, stərəta-'), mainly as the technical term for spreading the barəsman twigs, and the noun stairiš- 'Streu, Lager'. The second word, wi-star-, is NOT attested in Avestan: Bartholomae's prefixed compounds of ¹star- are only with ava-, us-, ni-, frā- and para-, and Cheung likewise lists only *upa-, *us-, *fra-, *ni- for Avestan, giving *ui- first for Middle Persian. Old Iranian *wi-star- is nevertheless a legitimate reconstruction from MP wistardan, which is how Horn, Abolghasemi and Moʿin present it; Nourai has projected it back onto the Avestan box a stage too early.\",\n     \"derivation_fa\": \"اوستایی star- «گستردن، پراکندن» به‌روشنی گواهی شده است؛ بارتولومه (ستون ۱۵۹۶–۹۸) آن را چنین می‌آورد: «¹star- فعل «sternere»؛ حال: star-، stərənu-، stərənā-؛ اسم مفعول: starəta-» و بیشتر در معنای «گستردن برسم» به کار رفته است. اما صورت دوم، wi-star-، در اوستا گواهی ندارد: بارتولومه فقط پیشوندهای ava-، us-، ni-، frā- و para- را می‌آورد و چونگ نیز پیشوند *ui- را نخست برای فارسی میانه ثبت می‌کند. البته *wi-star- ایرانی باستان بازسازی درستی است که از wistardan فارسی میانه به دست می‌آید (چنان‌که هرن، ابوالقاسمی و معین نوشته‌اند)، ولی نورایی آن را یک مرحله زودتر، در خانهٔ «اوستایی»، نشانده است؛ پس با احتیاط پذیرفتنی است.\",\n     \"sources\": [U_GOST, U_STERH3],\n     \"ref_check\": [\n      {\"ref\": \"KLN:1522\", \"status\": \"supports\",\n       \"note\": \"KLN_1966.txt leaf 807-808 (printed pp.1521-1524, confirmed by the running numerals 1514/1515 on leaf 803 and 1529/1531 on leaf 811), s.v. stratum: '… fr. I.-E. base *ster-, *stor-, *str-, \\\"to spread out, extend, strew\\\", whence also … Avestic star-, \\\"to spread out, stretch out\\\".'\"},\n      {\"ref\": \"FFD:73\", \"status\": \"supports\",\n       \"note\": \"incoming/FFD/FFD_pages.txt pdf page 78 = printed p.73 (offset pdf−5), s.v. گستردن: 'گسترد < فارسی میانه wistard < ایرانی باستان *wi-star-…؛ wi پیشوند فعلی است. ریشهٔ star به معنی «پاشیدن» است.' Abolghasemi puts the *wi- prefixation in Old Iranian, as Nourai does.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"BRT\", \"where\": \"Bartholomae col. 1596-1598 (BRT.txt lines 26597-26620)\", \"stance\": \"partial\",\n       \"note\": \"'j. ¹star- V. \\\"sternere\\\". … PPfP. starəta-, stərəta-' with prefixed ava-, us-, ni-, frā-, para- only; the etymological footnote reads 'ai. stṛṇāti, stṛṇóti, stárate …; np. gustardan. — Pū.: vistarītan, vistarēnītan' — i.e. Bartholomae himself draws Av. star- → Pahl. vistarītan → NP gustardan, but knows no Avestan vī-star-.\"},\n      {\"src\": \"CHEUNG\", \"where\": \"CHEUNG.txt p.365, *starH₁\", \"stance\": \"partial\",\n       \"note\": \"'*AVESTAN: YAv. star- \\\"to spread\\\" || (+ *upa-) … (+ *us-) … (+ *fra-) … (+ *ni-)'; the *ui- compound appears only under '*MIDDLE PERSIAN: (+ *ui-) BMP wstl- /wistar-/'.\"},\n      {\"src\": \"POK\", \"where\": \"POK_full.txt s.v. ster-5 (p.1029)\", \"stance\": \"supports\",\n       \"note\": \"'Avestan star- (present starati, starənaoti, starənāti) \\\"sternere\\\", participle starəta- and stərəta-, stairiš- n. \\\"Streu, lair, bed\\\"'.\"}\n     ]\n    },\n    {\n     \"id\": 2, \"lang\": \"Pahlavi\", \"words\": \"vi-startan; vi-starak; xâk-astar\", \"verdict\": \"plausible\",\n     \"derivation\": \"Two of the three are exactly right. MP wistardan / wistar- [wstl-tn'] 'to spread' is MacKenzie p.92, glossed there with 'N gustardan'; MP wistarag [wstl(g)] 'bedding, cover' is MacKenzie p.91 with 'N bistar', and Nyberg II analyses it '< OIr. *vi-star-ka-' — precisely Nourai's vi-starak. The third, xāk-astar, is not attested in Book Pahlavi: MacKenzie's word for 'ashes' is ādurestar ['twrystl], i.e. ādur 'fire' + the same -(e)star 'spread' element, and Moʿin's footnote in the Borhān compares exactly that (ātur 'fire' + gustardan 'to scatter'). So the compound type is Middle Persian, but the attested member has ādur, not xāk; Wiktionary does posit an inherited MP *xākestar (hʾkstl) without citation.\",\n     \"derivation_fa\": \"دو واژه از سه واژه کاملاً درست است: فارسی میانه wistardan / wistar- «گستردن» در فرهنگ مکنزی (ص ۹۲) با معادل نوفارسی gustardan آمده، و wistarag «بستر، روپوش» (مکنزی ص ۹۱، معادل نوفارسی bistar) که نیبرگ آن را «از ایرانی باستان *vi-star-ka-» می‌داند؛ یعنی همان vi-starak نورایی. اما xāk-astar در پهلویِ کتابی گواهی ندارد: واژهٔ پهلوی «خاکستر» در مکنزی ādurestar است، یعنی ādur «آتش» + همان جزء -(e)star «گستردن»، و معین نیز در حاشیهٔ برهان همین را می‌آورد (ātur یعنی آتش + گستردن/پاشیدن). پس ساختِ ترکیب پهلوی است، ولی جزء نخستِ گواهی‌شده «آتش» است نه «خاک»؛ این گره با احتیاط پذیرفتنی است.\",\n     \"sources\": [U_XAK, U_BESTAR],\n     \"ref_check\": [\n      {\"ref\": \"BQT:278,1816\", \"status\": \"supports\",\n       \"note\": \"BQT_v1_pages.txt leaf 498 (printed ≈ p.277-278) carries the headwords 'بستر' and 'بستردن'; incoming/BQT/BQT_v3_pages.txt pdf page 613 (printed ≈ p.1816) carries 'گستر / گستردن' with Moʿin's footnote '… باستان *star-/vi-star (پهن کردن). پهلوی vi(s)tartan (پهن کردن)'. Both cited pages contain what the arrow claims.\"},\n      {\"ref\": \"HRN:205\", \"status\": \"supports\",\n       \"note\": \"HRN.txt leaf 226 = printed p.205 (offset leaf = p+21), no. 921: 'gusterden \\\"ausbreiten\\\", guster, vergl. bister (No. 218). ai. vi + √star- \\\"ausbreiten\\\"; phlv. v(i)starten \\\"ausbreiten\\\".' Horn's no. 218 adds 'bister \\\"Lager\\\" … vi- + √star-, *vistarana-'.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"MacKenzie 1971 pp.91-92 (PHD_mackenzie.txt lines 5425, 5427; PHD.txt line 869)\", \"stance\": \"partial\",\n       \"note\": \"'wistar(ag) [wstl(g) | N bistar] bedding, cover.' and 'wistardan, wistar- [wstl-tn' | N gustardan] spread.' — but for 'ashes' MacKenzie has 'ādurestar ['twrystl] ashes', not xāk-astar.\"},\n      {\"src\": \"NYB\", \"where\": \"Nyberg II, glossary s.vv. vistarg, vistartan (NYB_vol2_glossary.txt lines 4211-4212)\", \"stance\": \"supports\",\n       \"note\": \"'vistarg [wstlg] bed coverlet … < OIr *vi-star-ka-, … NP bistar \\\"bed, mattress\\\"' and 'vistartan [wstltn'], visturtan, vistar-, to spread … < vi- + star-, v. start; NP gustardan, -ridan'.\"},\n      {\"src\": \"SNS\", \"where\": \"Tavoosi, Shāyast nē Shāyast glossary p.273 (index leaf 222: 'vistard 273/20 … vistarg 273/24')\", \"stance\": \"supports\",\n       \"note\": \"the glossary entry reads 'vistard … vi + √star' with 'vistard ēstād' and 'vistarg' — an attested Pahlavi text occurrence of the verb and the noun.\"},\n      {\"src\": \"BQT\", \"where\": \"BQT_v2_pages.txt leaf 160 (printed ≈ p.703), Moʿin's footnote on خاکستر\", \"stance\": \"partial\",\n       \"note\": \"'… خاک + ...ستر (قس: پهلوی ātur-star …) ātur یعنی آتش … (گستردن = پاشیدن؟)' — Moʿin compares Pahlavi ādur-star, i.e. the fire-compound, not a Pahlavi xāk-astar.\"}\n     ]\n    },\n    {\n     \"id\": 3, \"lang\": \"Persian\", \"words\": \"gostardan; bastar; xâkestar\", \"verdict\": \"confirmed\",\n     \"derivation\": \"گستردن gostardan 'to spread' continues MP wistardan directly: initial Middle Persian wi- regularly becomes New Persian gu- (as in wistāx > gostāx, wišādan > gošādan, wizārdan > gozārdan), and the past stem -stard gives gostard, present stem gostar — Bartholomae, Horn (no. 921), Nyberg, Abolghasemi and Cheung all print this chain. بستر bastar/bestar 'bed' is MP wistarag 'bedding' with the same prefix, but with the b- outcome of the labial that Persian shows in the noun (bistar beside dialectal gustar; Horn no. 218 'bister \\\"Lager\\\" … vi- + √star-'); Cheung and Wiktionary prefer to read the prefix here as *abi- rather than *wi-, but Nyberg's *vi-star-ka- and the Pahlavi spelling wstl support Nourai. خاکستر xākestar 'ashes' is xāk 'dust, earth' + the -(e)star element of this root, i.e. literally 'spread dust', on the model of MP ādurestar 'ashes' (= 'spread fire'); Moʿin's footnote in the Borhān analyses it exactly so. The extra forms in the box (گسترانیدن، گستریدن، گستر، گسترش) are the regular causative, secondary infinitive, present stem and verbal noun.\",\n     \"derivation_fa\": \"«گستردن» یکراست دنبالهٔ wistardan فارسی میانه است: پیشوند wi- در آغاز واژه در فارسی نو به گُ بدل می‌شود (چنان‌که wistāx > گستاخ، wišādan > گشادن، wizārdan > گزاردن)، و ستاک گذشتهٔ -stard به «گسترد» و ستاک حال به «گستر» رسیده است؛ بارتولومه، هرن (شمارهٔ ۹۲۱)، نیبرگ، ابوالقاسمی و چونگ همگی همین زنجیره را می‌آورند. «بستر» از wistarag پهلوی «بستر، روانداز» است با همان پیشوند، اما با برونداد ب (قس. هرن شمارهٔ ۲۱۸: bister «Lager» … vi- + √star-)؛ چونگ و ویکی‌واژه پیشوند را در این واژه *abi- می‌خوانند نه *wi-، ولی صورت پهلوی wstl و تحلیل نیبرگ (*vi-star-ka-) گفتهٔ نورایی را تأیید می‌کند. «خاکستر» نیز «خاک + ـستر» است، یعنی «خاکِ پاشیده»، به قیاس ādurestar پهلوی («آتشِ پاشیده»)؛ حاشیهٔ معین بر برهان قاطع دقیقاً همین تحلیل را دارد. صورت‌های افزودهٔ جدول (گسترانیدن، گستریدن، گستر، گسترش) هم ساخت‌های سببی، مصدر ثانوی، ستاک حال و اسم مصدرِ همین فعل‌اند.\",\n     \"sources\": [U_GOST, U_XAK, U_BESTAR],\n     \"ref_check\": [\n      {\"ref\": \"BQT:702,1816\", \"status\": \"supports\",\n       \"note\": \"BQT_v2_pages.txt leaf 160 ≈ printed p.703 has 'خاکستر' with Moʿin's etymological footnote (خاک + ستر; قس. پهلوی ātur-star); incoming/BQT/BQT_v3_pages.txt pdf 613 ≈ printed p.1816 has گستر/گستردن/گسترش with the footnote 'باستان *star-/vi-star (پهن کردن). پهلوی vi(s)tartan'.\"},\n      {\"ref\": \"SNS:273\", \"status\": \"supports\",\n       \"note\": \"SNS index leaf 222 lists 'vistard 273/20', 'vistard ēstād 273/23', 'vistarg 273/24'; the glossary page itself (SNS_pages.txt leaf 154) gives 'vi + √star' for vistard — Nourai's page is exact.\"},\n      {\"ref\": \"FFD\", \"status\": \"supports\",\n       \"note\": \"FFD p.73 (pdf 78): 'گسترد < فارسی میانه wistard < ایرانی باستان *wi-star-…؛ گستر < فارسی میانه wistar < ایرانی باستان *wi-stara-'.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"HRN\", \"where\": \"Horn, Grundriss no. 921 p.205 and no. 218 (HRN.txt leaves 226, 2283ff)\", \"stance\": \"supports\",\n       \"note\": \"no. 921 'gusterden \\\"ausbreiten\\\" … phlv. v(i)starten'; no. 218 'bister \\\"Lager\\\" … g. vistara \\\"Bett, Bettzeug\\\". vi- + √star- \\\"ausbreiten\\\", *vistarana-; vergl. gusterden (No. 921)'.\"},\n      {\"src\": \"CHEUNG\", \"where\": \"Cheung 2007 p.365 s.v. *starH₁\", \"stance\": \"partial\",\n       \"note\": \"'*NWIR: (+ *abi- ?) NP bistar, Khuns. bistār \\\"bed, mattress\\\" … || (+ *ui-) NP gustardan/gustar- \\\"to spread\\\"' — gostardan confirmed, but Cheung hesitates over the prefix of bistar.\"},\n      {\"src\": \"ARY\", \"where\": \"Aryanpur, incoming/ARY/ARY_pages.txt pdf p.435 (note 1 to the *ster- entry)\", \"stance\": \"supports\",\n       \"note\": \"'۱- واژهٔ فارسی \\\"بستر\\\" (پهلوی wistarag, wistarak, wistar) نیز از همین ریشه است (برهان قاطع …)'.\"},\n      {\"src\": \"IEC\", \"where\": \"Mann, IEC.txt line 17198\", \"stance\": \"supports\",\n       \"note\": \"'Per. cf. gu-stardan, inf. \\\"strew, spread\\\"; gu-star, s. \\\"spreader\\\" (fr. *ue-)' — Mann derives the gu- from the *ui- prefix.\"},\n      {\"src\": \"MON\", \"where\": \"vajehyab/Moʿin not needed; MON_part1.txt\", \"stance\": \"silent\",\n       \"note\": \"grep 'گستردن' in the 2-vol. abridgement OCR gives no clean entry block (the OCR breaks the گ section); recorded as silent.\"}\n     ]\n    },\n    {\n     \"id\": 4, \"lang\": \"Latin\", \"words\": \"strata\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Latin strāta is the feminine past participle of sternere 'to spread out, lay down, pave' (perf. strāvī, ppp. strātus < zero-grade *str̥h₃-tó-), used elliptically in the road-building formula (via) strāta lapidibus 'a way paved with stones' — Ernout-Meillet: 'fréquent dans sternere uiam (lapidibus) … de là strata (uia) \\\"chaussée\\\"'. The word spread with the Roman road network into Germanic (OHG strāzza, OE strǣt), Romance (It. strada, Sp. estrada, OFr. estrée) and the Near East.\",\n     \"derivation_fa\": \"لاتینی strāta صفت مفعولی مؤنثِ sternere «گستردن، فرش کردن، سنگفرش کردن» است (ماضی نقلی strātus از پایهٔ صفر *str̥h₃-tó-) که در تعبیر راه‌سازیِ (via) strāta lapidibus «راهِ سنگفرش‌شده» به‌تنهایی به معنی «جاده» به کار رفت؛ ارنو و مِیه: «در sternere uiam پرکاربرد است … و از همین‌جا strata (uia) به معنی chaussée». این واژه همراه با شبکهٔ راه‌های رومی به ژرمنی (strāzza، strǣt)، به زبان‌های رومانس (strada، estrada) و به خاور نزدیک رفت. ادعای نورایی درست است.\",\n     \"sources\": [E + \"street\", U_STERH3],\n     \"ref_check\": [\n      {\"ref\": \"KLN:1522\", \"status\": \"supports\",\n       \"note\": \"KLN_1966.txt leaf 808 (printed ≈ p.1522-1524), s.v. stratum: 'L. stratum … pp. of sternere, \\\"to spread out, stretch out; to scatter; to cover\\\" … fr. I.-E. base *ster-, *stor-, *str-' and s.v. street: 'fr. Late L. strata (via), \\\"paved way\\\", fem. pp. of sternere'.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. sterno (LAT.txt line 60349)\", \"stance\": \"supports\",\n       \"note\": \"'sterno, -is, straui, stratum, sternere: étendre, coucher à terre … fréquent dans sternere uiam (lapidibus) … de là strata (uia) \\\"chaussée\\\" … À strata remontent les formes germ. du type v.h.a. strāzza, v.angl. strǣt.'\"},\n      {\"src\": \"POK\", \"where\": \"POK_full.txt s.v. ster-5 (p.1030)\", \"stance\": \"supports\",\n       \"note\": \"'Latin sterno, -ere \\\"scatter, strew, hinbreiten\\\", participle stratus (*sterətós)'.\"},\n      {\"src\": \"WLD\", \"where\": \"Bd. II 639 (leaf 643)\", \"stance\": \"supports\",\n       \"note\": \"'Lat. sterno, -ere „auf den Boden hinstreuen, hinbreiten“ … Ptc. stratus (*sterətos)'.\"}\n     ]\n    },\n    {\n     \"id\": 5, \"lang\": \"Greek\", \"words\": \"\", \"verdict\": \"confirmed\",\n     \"derivation\": \"This deliberately empty box is the Late/Byzantine Greek στράτα — Latin strāta borrowed back into Greek in the Roman imperial period as the ordinary word for a paved highway (Procopius II.1 has στράτα of the Syrian desert road). It is the necessary link because the Aramaic and Arabic forms show the Greek shape and the Greek accent, not a direct Latin borrowing. Jeffery: 'it was from the Hellenized form of the Lat. strata that the word passed into Aram. and thence into Arabic'.\",\n     \"derivation_fa\": \"این خانهٔ عمداً خالی، یونانیِ متأخر/بیزانسی στράτα است: واژهٔ لاتینی strāta در دورهٔ امپراتوری روم به یونانی وام داده شد و واژهٔ عادی «شاهراه سنگفرش» گردید (پروکوپیوس آن را برای راه بیابان شام به کار می‌برد). این حلقه ضروری است، زیرا صورت آرامی و عربی نشانهٔ گذر از یونانی است نه وام‌گیری یکراست از لاتینی؛ جفری می‌نویسد: «واژه از صورت یونانی‌شدهٔ strata لاتینی به آرامی و از آنجا به عربی رفت». ادعای نورایی درست است.\",\n     \"sources\": [U_SIRAT],\n     \"ref_check\": [\n      {\"ref\": \"KLN\", \"status\": \"supports\",\n       \"note\": \"KLN_1966.txt line 2345, s.v. Al Sirat: '… fr. Aram. isṭrāṭā, isrāṭā, fr. Late Gk. στράτα, fr. L. strata (scil. via), lit. \\\"paved way\\\". See street.'\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"FVQ\", \"where\": \"Jeffery pp.195-196 (FVQ_pages.txt leaves 213-214)\", \"stance\": \"supports\",\n       \"note\": \"'They said it was Greek, and are right in so far as it was from the Hellenized form of the Lat. strata that the word passed into Aram. and thence into Arabic. … so that strata became στράτα (cf. Procopius, ii, 1)'.\"},\n      {\"src\": \"LKT\", \"where\": \"LKT.txt\", \"stance\": \"silent\",\n       \"note\": \"grep 'strata'/'sirat': Lokotsch has no entry for this word (his book covers Oriental words in European languages, i.e. the opposite direction).\"}\n     ]\n    },\n    {\n     \"id\": 6, \"lang\": \"Aramaic\", \"words\": \"isrâta\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Aramaic/Syriac ʾesṭrāṭā (ܐܣܛܪܛܐ), with the prosthetic aleph Aramaic regularly prefixes to loanwords beginning in st-, is Gk. στράτα 'paved road'; the Talmudic and Targumic spellings ʾsṭrṭʾ, sṭrṭʾ, ʾsrṭʾ are all recorded (Krauss, Griechische und lateinische Lehnwörter im Talmud II, 82). Klein's entry prints precisely the two variants 'isṭrāṭā, isrāṭā', and Nourai's isrâta is the second of them — the one with the emphatic ṭ lost, which is also the one that best explains Arabic ṣ-r-ṭ.\",\n     \"derivation_fa\": \"آرامی/سریانی ʾesṭrāṭā (ܐܣܛܪܛܐ) همان στράτα یونانی است با «الفِ پیشین» که آرامی به‌طور قاعده‌مند بر سر وام‌واژه‌های آغازشونده به خوشهٔ st- می‌افزاید؛ در متون تلمودی و ترگومی صورت‌های ʾsṭrṭʾ، sṭrṭʾ و ʾsrṭʾ همه ثبت شده‌اند. کلاین دقیقاً دو گونهٔ «isṭrāṭā، isrāṭā» را می‌آورد و صورت نورایی (isrâta) همان گونهٔ دوم است، یعنی گونه‌ای که ط در آن افتاده و همان است که ساخت عربی ص-ر-ط را بهتر توضیح می‌دهد. ادعای نورایی درست است.\",\n     \"sources\": [U_SIRAT],\n     \"ref_check\": [\n      {\"ref\": \"KLN:56\", \"status\": \"supports\",\n       \"note\": \"KLN_1966.txt leaf 41 = printed pp.56-57 (leaf 40 carries '54/55', leaf 42 carries '58/59'), s.v. Al Sirat: '… fr. Arab. al-ṣirāṭ … fr. Aram. isṭrāṭā, isrāṭā, fr. Late Gk. στράτα, fr. L. strata (scil. via)'. Nourai's page is exact.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"FVQ\", \"where\": \"Jeffery p.196 (FVQ_pages.txt leaf 214)\", \"stance\": \"supports\",\n       \"note\": \"'thence Aram. ʾsṭrṭʾ; sṭrṭʾ; ʾsrṭʾ; Syr. ʾsṭrṭʾ' with the footnote 'Cf. Krauss, Griechische und lateinische Lehnwörter im Talmud, ii, 82, 413.'\"},\n      {\"src\": \"AFA\", \"where\": \"Fraenkel, Die aramäischen Fremdwörter (AFA.txt)\", \"stance\": \"silent\",\n       \"note\": \"grep 'sirat', 'Strasse', 'strata' finds only unrelated passages (p.90 n.3 on a different word); Jeffery's 'Fraenkel, Vocab, 25' refers to Fraenkel's other book (De vocabulis … peregrinis, 1880), not to this one.\"}\n     ]\n    },\n    {\n     \"id\": 7, \"lang\": \"Arabic\", \"words\": \"serât\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Arabic صِراط ṣirāṭ 'path, way' is the Aramaic word arabised: the initial s of ʾisrāṭā was assimilated to the following emphatic ṭ and became ṣ (hence the doublet spellings سراط / صراط / زراط that the early readers of the Qurʾān argued over), and the prosthetic aleph was reinterpreted away. It was borrowed early, before Islam — Jeffery notes it 'being found in the early poetry' — which is why it could be used forty-five times in the Qurʾān (I:5-6 al-ṣirāṭ al-mustaqīm) and become a theological term; the Muslim philologists themselves (Suyūṭī, Itq. 322) recognised it as foreign and called it Greek.\",\n     \"derivation_fa\": \"عربی «صِراط» همان واژهٔ آرامی معرّب است: سینِ آغازیِ ʾisrāṭā زیر تأثیر طای مُفَخَّمِ پس از خود به «ص» بدل شده (همگونیِ تفخیم) و از همین‌روست که قاریان نخستین بر سر سه املای «سراط / صراط / زراط» اختلاف داشتند؛ الفِ پیشین نیز افتاده است. این وام‌گیری پیش از اسلام روی داده — جفری می‌گوید در شعر کهن دیده می‌شود — و از همین‌رو چهل‌وپنج بار در قرآن آمده است («اهدنا الصراط المستقیم») و اصطلاحی کلامی شده؛ خودِ لغویان مسلمان (سیوطی، الاتقان ۳۲۲) آن را دخیل و یونانی می‌دانستند.\",\n     \"sources\": [U_SIRAT],\n     \"ref_check\": [\n      {\"ref\": \"POK:56\", \"status\": \"not_found\",\n       \"note\": \"POK_01.txt leaf 64 (= printed p.56) is the *ar- 'fügen, passen' article (ἀρθρόν, ἀραρίσκω …) and has nothing to do with ṣirāṭ. This is a slip for KLN:56, the Klein page (Al Sirat) that the sister node #6 cites.\"},\n      {\"ref\": \"FVQ:195\", \"status\": \"supports\",\n       \"note\": \"FVQ_pages.txt leaves 213-214 = printed pp.195-196: the headword ṣirāṭ 'A Way', 'Occurs some forty-five times, e.g. i, 5, 6', 'Many of the early philologers recognized it as a foreign word … They said it was Greek, and are right in so far as it was from the Hellenized form of the Lat. strata that the word passed into Aram. and thence into Arabic.'\"},\n      {\"ref\": \"TAD:34\", \"status\": \"supports\",\n       \"note\": \"TAD_pages.txt leaf 37 (printed ≈ p.32-34): 'سراط وصراط وزراط — لاتيني strata معناه طريق مبلطة، فنقلت الى الايطالية strada والى الجرمانية strasse والى الانكليزية street' — al-Unaysi's entry is exactly Nourai's chain.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"KLN_1966.txt line 2345, s.v. Al Sirat (p.56)\", \"stance\": \"supports\",\n       \"note\": \"'Arab. al-ṣirāṭ, \\\"the road\\\", fr. al-, \\\"the\\\", and ṣirāṭ, \\\"road\\\", fr. Aram. isṭrāṭā, isrāṭā …'\"},\n      {\"src\": \"AFM\", \"where\": \"AFM_pages.txt\", \"stance\": \"silent\",\n       \"note\": \"grep 'صراط': no hit — Addi Shir treats Persian Arabisms only, and ṣirāṭ is Greek/Aramaic.\"},\n      {\"src\": \"PLA\", \"where\": \"incoming/PLA/PLA_pages.txt\", \"stance\": \"silent\",\n       \"note\": \"grep 'صراط': no hit; Asbaghi likewise covers only Persian loans in Arabic.\"}\n     ]\n    },\n    {\n     \"id\": 8, \"lang\": \"Persian\", \"words\": \"serât\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Persian صراط serāt 'road' is a Qurʾānic Arabic loan taken over with the Arabic orthography and the religious sense, chiefly in the fixed phrase صراط مستقیم and in the eschatological 'bridge of ṣirāṭ' — hence the Rumi couplet the chart quotes ('اهدنا گفتی صراط مستقیم'). Moʿin marks it flatly '[ع.]' (Arabic). Note the curiosity that the same word had already reached Iran once before by another road: Jeffery records that in its eschatological sense it passed from Aramaic into Pahlavi as srāt (Bailey, JRAS 1934, p.505), so Persian has it twice over.\",\n     \"derivation_fa\": \"«صراط» در فارسی وام‌واژه‌ای عربی و قرآنی است که با همان املا و همان بار دینی گرفته شده، بیشتر در ترکیب «صراط مستقیم» و در معنای «پل صراط»؛ از همین‌رو بیت مولوی که در جدول آمده («اِهدنا گفتی صراط مستقیم…») شاهد خوبی است. معین آن را با نشانهٔ «[ع.]» (عربی) آورده و «راه، طریق» معنی می‌کند. نکتهٔ شنیدنی آنکه همین واژه یک‌بار پیش‌تر و از راهی دیگر نیز به ایران رسیده بود: جفری به نقل از بیلی می‌گوید که در معنای اخروی از آرامی به پهلوی به صورت srāt راه یافته است؛ پس فارسی آن را دوبار وام گرفته است.\",\n     \"sources\": [U_SIRAT],\n     \"ref_check\": [\n      {\"ref\": \"MON\", \"status\": \"supports\",\n       \"note\": \"MON_part1.txt line 89339: 'صراط: [ع.] (اِ.) راه، طریق. صراط مستقیم: راه راست.' Moʿin's tag [ع.] states the Arabic source explicitly.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"FVQ\", \"where\": \"Jeffery p.196 n.2\", \"stance\": \"supports\",\n       \"note\": \"'Of particular interest is the fact that in an eschatological sense it passed from Aramaic into Pahlavi as srāt. Cf. Bailey in JRAS, 1934, p. 505.'\"},\n      {\"src\": \"BQT\", \"where\": \"BQT_v1/v2_pages.txt\", \"stance\": \"silent\",\n       \"note\": \"grep 'صراط' in the Borhān volumes on disk returns no headword entry — the Borhān is a dictionary of Persian (non-Arabic) words, so its silence is expected and itself confirms the word is felt as Arabic.\"}\n     ]\n    },\n    {\n     \"id\": 9, \"lang\": \"English\", \"words\": \"stray; street\", \"verdict\": \"plausible\",\n     \"derivation\": \"'Street' is beyond doubt: OE strǣt/strēt (Mercian) 'street, high road' < Late Latin strāta (via), one of the very few Latin words in continuous English use since Roman Britain, with the parallel early Germanic borrowings OFris. strete, OS strata, OHG strāza, Ger. Straße. 'Stray' is the contested one: Klein and Etymonline's main entry take ME straien from OFr. estraier 'to roam', from estree 'road' < via strata — literally 'to go about the streets'; but the OED also reprints the rival derivation from Vulgar Latin *estragare < *extravagare 'to wander outside'. So the node is right for street, and only the majority (not unanimous) view for stray.\",\n     \"derivation_fa\": \"دربارهٔ street تردیدی نیست: انگلیسی کهن strǣt «راه سنگفرش، شاهراه» از strāta لاتینی متأخر است و یکی از معدود واژه‌های لاتینی است که از روزگار بریتانیای رومی تاکنون پیوسته در انگلیسی به کار رفته؛ وام‌های هم‌زمانِ ژرمنی آن هم strata، strāza و Straße است. اما stray محل گفت‌وگوست: کلاین و اتیمآنلاین آن را از estraier فرانسهٔ کهن و آن را از estree «راه» (< via strata) می‌گیرند، یعنی «در کوچه‌ها پرسه زدن»؛ ولی فرهنگ آکسفورد نظر رقیب را نیز می‌آورد که آن را از *extravagare لاتینی عامیانه «بیرون سرگردان شدن» می‌داند. پس این گره برای street قطعی و برای stray نظر اکثریت است؛ با احتیاط پذیرفتنی است.\",\n     \"sources\": [E + \"street\", E + \"stray\"],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"partial\",\n       \"note\": \"AHD_watkins1985.txt ster-2 III.1 lists 'Latin sternere (past participle strātus …), to stretch, extend: STRATUS, STREET; CONSTERNATE, SUBSTRATUM' — STREET yes, STRAY is not in Watkins' list.\"},\n      {\"ref\": \"KLN\", \"status\": \"supports\",\n       \"note\": \"KLN_1966.txt leaf 808: 'street, n. — ME. strete … fr. OE. street, fr. Late L. strata (via)'; 'stray, intr. v. … fr. MF. estraier … fr. OF. estree, \\\"road\\\", fr. Late L. strata (via), \\\"paved road\\\". See street.'\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"SKT\", \"where\": \"SKT.txt s.vv. street/stray\", \"stance\": \"partial\",\n       \"note\": \"Skeat likewise takes street from L. strata; his stray entry points to O.F. estraier without committing to a single Latin base.\"},\n      {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. sterno (LAT.txt line 60349)\", \"stance\": \"supports\",\n       \"note\": \"'À strata remontent les formes germ. du type v.h.a. strāzza, v.angl. strǣt' — the street half of the node.\"}\n     ]\n    },\n    {\n     \"id\": 10, \"lang\": \"Latin\", \"words\": \"struere; industria\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Latin struō, struere 'to pile up, build' is the *streu- extension of the root (*strew-e/o-; the -x- of strūxī, structum is analogical), with strues 'heap'. industria 'diligence, activity' is the feminine of industrius, from Old Latin indostruus, literally 'building into/within', indu- (old form of in-) + the zero grade *stru-; Watkins files it under ster-2 I.3 and Klein s.v. industry gives the same analysis. So both Latin words in the box belong to this root, the second only through the compound.\",\n     \"derivation_fa\": \"لاتینی struō/struere «روی هم چیدن، ساختن» از گسترشِ *streu- همین ریشه است (صامت x در strūxī قیاسی است) و strues «توده» نیز از همان. واژهٔ industria «کوشش، فعالیت» مؤنثِ industrius است و آن از لاتینیِ کهن indostruus به معنی تحت‌اللفظیِ «درون‌ساز»، از indu- (صورت کهن in-) و پایهٔ صفرِ *stru-؛ واتکینز آن را زیر ster-2 و کلاین نیز در مدخل industry همین‌گونه تحلیل می‌کند. پس هر دو واژهٔ این خانه به همین ریشه می‌رسند، دومی از راه ترکیب. ادعای نورایی درست است.\",\n     \"sources\": [U_STERH3],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"supports\",\n       \"note\": \"AHD_watkins1985.txt ster-2 I: '2. Latin struere, to pile up, construct: STRUCTURE; CONSTRUCT, DESTROY, INSTRUCT, OBSTRUCT, SUBSTRUCTION. 3. Zero-grade form *stru- in Latin industria, diligence, activity (endo-, within; see en): INDUSTRY.'\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"KLN_1966.txt line 19240, s.v. industry\", \"stance\": \"supports\",\n       \"note\": \"'F. industrie, fr. L. industria … fr. OL. indostruus, lit. \\\"building into\\\", fr. indu, \\\"in\\\", and struere, \\\"to build, erect\\\". See indigene and structure.'\"},\n      {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. struo (LAT.txt line 61365)\", \"stance\": \"supports\",\n       \"note\": \"'struo, -is, -xi, -ctum, -ere: disposer en piles, \\\"empiler\\\" … \\\"construire, bâtir\\\" … Dérivés et composés: strues, -is f.: pile'.\"},\n      {\"src\": \"POK\", \"where\": \"POK_full.txt s.v. ster-5 B, extension streu- (p.1030)\", \"stance\": \"supports\",\n       \"note\": \"'streu-: Latin struo, -ere (struxi, structum …) \\\"übereinander breiten, schichten, aufbauen\\\", strues, struix \\\"heap, bulk, mass\\\"'.\"}\n     ]\n    },\n    {\n     \"id\": 11, \"lang\": \"English\", \"words\": \"construct; destroy; instruction; industry; structure\", \"verdict\": \"confirmed\",\n     \"derivation\": \"All five are Latin-derived learned or Old French words on the struere family: construct (< construere, ppp. constructus, 15c. as adj., 17c. as verb), destroy (< OFr. destruire < VL *destrugere for Lat. dēstruere 'to unbuild'), instruction (< īnstructiō < īnstruere 'to build in, equip, teach'), industry (< Fr. industrie < industria), structure (< Lat. structūra). Watkins lists exactly this set (plus obstruct, substruction) under ster-2. The box carries no reference in the book, but the derivation is uncontroversial.\",\n     \"derivation_fa\": \"هر پنج واژه از خانوادهٔ struere لاتینی‌اند و یا مستقیم از لاتینی علمی یا از راه فرانسهٔ کهن وارد انگلیسی شده‌اند: construct از construere (اسم مفعول constructus)، destroy از destruire فرانسهٔ کهن و آن از dēstruere «واساختن»، instruction از īnstructiō (< īnstruere «آموختن، تجهیز کردن»)، industry از industrie فرانسوی، و structure از structūra. واتکینز دقیقاً همین فهرست را (به‌علاوهٔ obstruct و substruction) زیر ster-2 می‌آورد. این خانه در کتاب بی‌ارجاع است، ولی اشتقاق آن جای گفت‌وگو ندارد.\",\n     \"sources\": [U_STERH3],\n     \"ref_check\": [\n      {\"ref\": \"None\", \"status\": \"not_checked\",\n       \"note\": \"the node carries no reference in the book; checked against AHD and Klein instead (see consulted).\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. ster-2 I.2-3\", \"stance\": \"supports\",\n       \"note\": \"'STRUCTURE; CONSTRUCT, DESTROY, INSTRUCT, OBSTRUCT, SUBSTRUCTION … INDUSTRY' — Nourai's five words with two more.\"},\n      {\"src\": \"KLN\", \"where\": \"KLN_1966.txt s.v. stratum (leaf 808)\", \"stance\": \"supports\",\n       \"note\": \"the cross-reference list at the end of Klein's stratum entry names 'construction, destroy, destruction, … structure, substratum' as members of this base.\"}\n     ]\n    },\n    {\n     \"id\": 12, \"lang\": \"Greek\", \"words\": \"stratos; stratos-agein\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Gk. στρατός 'encamped host, multitude, army' is the zero-grade *str̥h₃-tó- (formally = Skt. stṛtá- 'strewn'), literally 'that which is spread out/encamped'; the Cretan by-form σταρτός shows the metathesis. From it στρατηγός 'army-leader, general' = στρατός + the stem of ἄγειν 'to lead' (PIE *ag-), whence στρατηγία 'generalship'. Nourai's 'stratos-agein' with the cross-reference ☞Ag is exactly Klein's analysis ('compounded of στρατός, \\\"army\\\", and the stem of … \\\"to lead\\\"; … for the second see agent').\",\n     \"derivation_fa\": \"یونانی στρατός «انبوه، اردو، سپاه» صورت پایهٔ صفرِ *str̥h₃-tó- است (از نظر ساخت برابر با stṛtá- سنسکریت «پراکنده») و در اصل یعنی «آنچه گسترده/اردو زده شده»؛ گونهٔ کرتیِ σταρτός نشانهٔ قلب (metathesis) است. از آن στρατηγός «سردار» ساخته شده، یعنی στρατός + ستاکِ ἄγειν «رهبری کردن» (از ریشهٔ *ag-)، و سپس στρατηγία «سرداری». صورت «stratos-agein» با ارجاع نورایی به ریشهٔ Ag دقیقاً همان تحلیل کلاین است. ادعای نورایی درست است.\",\n     \"sources\": [E + \"strategy\", U_STERH3],\n     \"ref_check\": [\n      {\"ref\": \"AHD:1273\", \"status\": \"supports\",\n       \"note\": \"AHD_watkins1985.txt ster-2 IV.1: 'Suffixed form *str̥-to- in Greek stratos, multitude, army, expedition: STRATAGEM; STRATOCRACY.' (Nourai's 1273 is the main-dictionary page of the st- entries, not the appendix.)\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"POK\", \"where\": \"POK_full.txt s.v. ster-5 (p.1029)\", \"stance\": \"supports\",\n       \"note\": \"'στρατός (= Old Indie stṛta-) \\\"troop, multitude, crowd, Volksmenge\\\" (Cretan σταρτός with metathesis …), then \\\"army\\\" (in addition στρατιά, στρατεία, στρατηγός)'.\"},\n      {\"src\": \"KLN\", \"where\": \"KLN_1966.txt line 36969, s.v. strategy\", \"stance\": \"supports\",\n       \"note\": \"'Gk. στρατηγία, \\\"office of a general\\\", fr. στρατηγός, \\\"strategus, general\\\", lit. \\\"leader of the army\\\", compounded of στρατός, \\\"army\\\", and the stem of … \\\"to lead\\\". For the first element see stratum … for the second see agent.'\"},\n      {\"src\": \"WLD\", \"where\": \"Bd. II 639 (leaf 643)\", \"stance\": \"supports\",\n       \"note\": \"'(στρατεία, στρατηγός), aeol. στρότος … gegen eine Gdf. *str̥ntós' — Walde-Pokorny discuss the exact formation.\"}\n     ]\n    },\n    {\n     \"id\": 13, \"lang\": \"French\", \"words\": \"strategie\", \"verdict\": \"confirmed\",\n     \"derivation\": \"French stratégie 'the art of the general, a military plan' is a learned 16th-century formation on the Latinised Greek strategia (στρατηγία 'office/command of a general'), which came into general military use in the Napoleonic period; it is the immediate source both of English strategy (1810) and, much later, of Persian استراتژی. Nourai's spelling 'strategie' omits the accents but is the French word.\",\n     \"derivation_fa\": \"فرانسوی stratégie «فنّ سرداری، نقشهٔ نظامی» ساختی عالمانه از سدهٔ شانزدهم بر پایهٔ صورت لاتینی‌شدهٔ یونانیِ strategia (στρατηγία «مقام و فرماندهیِ سردار») است که در دورهٔ ناپلئون کاربرد نظامیِ گسترده یافت؛ همین واژه هم سرچشمهٔ بی‌واسطهٔ strategy انگلیسی (۱۸۱۰ م) است و هم، بسیار دیرتر، سرچشمهٔ «استراتژی» فارسی. نورایی نشانه‌های زیر و زبَر فرانسوی را ننوشته، ولی واژه همان است.\",\n     \"sources\": [E + \"strategy\"],\n     \"ref_check\": [\n      {\"ref\": \"AHD:1273\", \"status\": \"supports\",\n       \"note\": \"the AHD main dictionary derives strategy from French stratégie / Greek stratēgia; Watkins' appendix lists STRATAGEM under stratos (AHD_watkins1985.txt line 1018).\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"KLN_1966.txt line 36969\", \"stance\": \"supports\",\n       \"note\": \"'strategy, n. — F. stratégie, fr. Gk. στρατηγία, \\\"office of a general\\\"'; and s.v. stratagem 'F. stratagème, fr. earlier strattegeme, fr. L. strategema'.\"},\n      {\"src\": \"DEV\", \"where\": \"DEV.txt\", \"stance\": \"silent\",\n       \"note\": \"grep 'stratég': Devic covers French words of Oriental origin only; a Greek learned word is out of scope.\"}\n     ]\n    },\n    {\n     \"id\": 14, \"lang\": \"Persian\", \"words\": \"esterâtežî\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Persian استراتژی esterātežī is a 20th-century French loan, taken in with the French pronunciation: the -gie /ʒi/ is written ژی (the letter ژ is Persian's regular rendering of French /ʒ/), and an epenthetic e- is prefixed to the initial st- cluster, which Persian phonotactics do not allow (cf. استکان, اسپانیا). Moʿin's dictionary defines it 'فنّ ادارهٔ عملیات جنگی؛ دانش رهبری عملیات نظامی؛ سوق‌الجیش'. The route French → Persian on the chart is right; it did not come through Arabic or English.\",\n     \"derivation_fa\": \"«استراتژی» وام‌واژه‌ای فرانسوی از سدهٔ بیستم است که با تلفظ فرانسوی وارد فارسی شده: پایانهٔ -gie فرانسوی با «ژی» نوشته می‌شود (حرف ژ برونداد همیشگیِ /ʒ/ فرانسوی در فارسی است) و چون فارسی خوشهٔ آغازی st- را نمی‌پذیرد، الفِ آغازین (e- افزایشی) بر سر آن آمده است؛ قس. استکان، اسپانیا. معین آن را چنین معنی می‌کند: «فنّ ادارهٔ عملیات جنگی؛ دانش رهبری عملیات نظامی؛ سوق‌الجیش». مسیر «فرانسوی ← فارسی» در نمودار درست است و این واژه از راه عربی یا انگلیسی نیامده است.\",\n     \"sources\": [E + \"strategy\"],\n     \"ref_check\": [\n      {\"ref\": \"MON:246\", \"status\": \"supports\",\n       \"note\": \"MON_part1.txt line 11745: 'استراتژی: (اِ.) فنّ ادارهٔ عملیات جنگی؛ دانش رهبری عملیات نظامی؛ سوق الجیش.' The entry is there; the 6-vol. page number cannot be verified because the online Moʿin text is the unpaginated 2-vol. abridgement.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"MON\", \"where\": \"MON_part1.txt lines 11745-11748\", \"stance\": \"supports\",\n       \"note\": \"the entry stands between استر and استراتوسفر, i.e. among the European loans, consistent with a French source.\"},\n      {\"src\": \"ARY\", \"where\": \"incoming/ARY/ARY_pages.txt\", \"stance\": \"silent\",\n       \"note\": \"grep 'استراتژی': no hit — Aryanpur's book treats inherited Indo-European Persian vocabulary, not modern European loans.\"}\n     ]\n    },\n    {\n     \"id\": 15, \"lang\": \"English\", \"words\": \"strategy\", \"verdict\": \"confirmed\",\n     \"derivation\": \"English strategy is first recorded in 1810 in the sense 'the art of a general, the science of war', from French stratégie and directly from the Latinised Greek strategia; the non-military use ('a plan') is only from 1887. The older English member of the family is stratagem (16c., through French and Latin from στρατήγημα).\",\n     \"derivation_fa\": \"واژهٔ انگلیسی strategy نخستین‌بار در ۱۸۱۰ م به معنی «فنّ سرداری، دانش جنگ» ثبت شده و از stratégie فرانسوی (و مستقیماً از صورت لاتینی‌شدهٔ یونانیِ strategia) گرفته شده است؛ کاربرد غیرنظامی آن («نقشه، تدبیر») تنها از ۱۸۸۷ م پیداست. عضو کهن‌ترِ این خانواده در انگلیسی stratagem (سدهٔ شانزدهم) است که از στρατήγημα و از راه فرانسوی و لاتینی آمده. ادعای نورایی درست است.\",\n     \"sources\": [E + \"strategy\"],\n     \"ref_check\": [\n      {\"ref\": \"AHD:1273\", \"status\": \"supports\",\n       \"note\": \"AHD's main dictionary entry for strategy (p.1273 of the New College edition, the st- pages Nourai is citing) gives French stratégie < Greek stratēgia; Watkins' appendix ster-2 IV.1 gives the root.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"KLN_1966.txt line 36969\", \"stance\": \"supports\",\n       \"note\": \"'strategy, n. — F. stratégie, fr. Gk. στρατηγία …'\"},\n      {\"src\": \"SKT\", \"where\": \"SKT.txt\", \"stance\": \"silent\",\n       \"note\": \"grep 'strateg': Skeat's concise dictionary has no entry for strategy.\"}\n     ]\n    },\n    {\n     \"id\": 16, \"lang\": \"Germanic\", \"words\": \"strawam\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Proto-Germanic *strawam (neut.) 'straw', literally 'that which is scattered', is the suffixed o-grade *strow-o- of the *strew- extension, beside the verb *strawjan 'to strew' (Goth. straujan, OE strē(o)wian, OHG strouwen). Watkins prints the form and the gloss Nourai uses word for word: 'Suffixed form *strow-o in Germanic *strawam, \\\"that which is scattered\\\", in Old English strēaw, straw'.\",\n     \"derivation_fa\": \"ژرمنی آغازین *strawam (خنثی) «کاه»، تحت‌اللفظی «آنچه پاشیده شده»، صورت پسوندگرفتهٔ پایهٔ o از گسترشِ *strew- است و در کنار فعل *strawjan «پاشیدن» می‌ایستد (گوتی straujan، انگلیسی کهن strēowian، آلمانی کهن strouwen). واتکینز همین صورت و همین معنا را که نورایی آورده، لفظ‌به‌لفظ می‌نویسد: «*strow-o در ژرمنی *strawam، یعنی آنچه پاشیده می‌شود». ادعای نورایی درست است.\",\n     \"sources\": [E + \"straw\", U_STERH3],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"supports\",\n       \"note\": \"AHD_watkins1985.txt ster-2 II.2: 'Suffixed form *strow-o in Germanic *strawam, \\\"that which is scattered,\\\" in Old English stréaw, straw: STRAW.'\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"POK\", \"where\": \"POK_full.txt s.v. ster-5 B, streu- (p.1030)\", \"stance\": \"supports\",\n       \"note\": \"'Gothic straujan \\\"strew, distribute\\\" … Old Icelandic strá n. \\\"straw\\\", Old English strēaw, Old High German strō, Modern High German Stroh'.\"},\n      {\"src\": \"KLN\", \"where\": \"KLN_1966.txt line 36984, s.v. straw\", \"stance\": \"supports\",\n       \"note\": \"'ME. straw, fr. OE. streaw … lit. \\\"that which is scattered\\\", fr. I.-E. base *ster-, *stor-, *str-, \\\"to spread out, extend, strew\\\".'\"}\n     ]\n    },\n    {\n     \"id\": 17, \"lang\": \"English\", \"words\": \"straw\", \"verdict\": \"confirmed\",\n     \"derivation\": \"English straw continues OE strēaw 'dried stalks of grain after threshing' (< PGmc *strawam) through ME strau; the notion behind the name is of stalks strewn on a floor as bedding or carpeting, which is why it belongs to the 'spread' root and not to any word for grain. The drinking-straw sense is only 1851. The box carries no reference in the book.\",\n     \"derivation_fa\": \"انگلیسی straw دنبالهٔ strēaw انگلیسی کهن «ساقه‌های خشکِ غله پس از خرمن‌کوبی» (< *strawam ژرمنی) است که از راه strau انگلیسی میانه به امروز رسیده. انگیزهٔ نام‌گذاری آن است که کاه را بر کف اتاق می‌گستردند تا بستر یا فرش شود؛ از همین‌روست که این واژه به ریشهٔ «گستردن» می‌رسد نه به واژه‌ای به معنی «غله». معنای «نی نوشیدنی» تنها از ۱۸۵۱ م پیدا شده است. این خانه در کتاب بی‌ارجاع است، اما اشتقاق آن قطعی است.\",\n     \"sources\": [E + \"straw\"],\n     \"ref_check\": [\n      {\"ref\": \"None\", \"status\": \"not_checked\",\n       \"note\": \"no reference printed in the book for this node; checked against AHD, Klein and Etymonline instead (see consulted).\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"KLN_1966.txt line 36984\", \"stance\": \"supports\",\n       \"note\": \"'straw, n. — ME. straw, fr. OE. streaw, rel. to ON. strá … lit. \\\"that which is scattered\\\" … See stratum and cp. strew.'\"},\n      {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. ster-2 II.2\", \"stance\": \"supports\",\n       \"note\": \"'… in Old English stréaw, straw: STRAW.'\"}\n     ]\n    }\n   ]\n  }\n ]\n}\n\nout = \"/home/sfmqrb/git/rishe/data/verification/page-479.json\"\nwith open(out, \"w\", encoding=\"utf-8\") as f:\n    json.dump(doc, f, ensure_ascii=False, indent=1)\nprint(\"wrote\", out, os.path.getsize(out))\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-479.py",
 "description": "Build page-479.json"
}
```


### [2026-09-14T03:28:08.886Z] TOOL RESULT

```
wrote /home/sfmqrb/git/rishe/data/verification/page-479.json 78831
```


## [2026-09-14T03:28:12.983Z] TOOL CALL #82: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-479.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 479",
 "description": "Validate JSON and run verify_check"
}
```


### [2026-09-14T03:28:14.056Z] TOOL RESULT

```
JSON OK
nodes verified: 26/26
node verdicts: {'confirmed': 22, 'transcription_suspect': 1, 'plausible': 3}
root verdicts: {'confirmed': 2}
ref checks: {'not_found': 2, 'supports': 28, 'contradicts': 1, 'partial': 1, 'not_checked': 2}
books consulted: {'supports': 42, 'silent': 14, 'partial': 7, 'contradicts': 3} | by book: {'KLN': 15, 'POK': 8, 'SKT': 5, 'WLD': 4, 'FVQ': 4, 'BQT': 3, 'MON': 3, 'ARY': 3, 'AHD': 3, 'LAT': 3, 'AFM': 2, 'PLA': 2, 'CHEUNG': 2, 'BRT': 1, 'PHD': 1, 'NYB': 1, 'SNS': 1, 'HRN': 1, 'IEC': 1, 'LKT': 1, 'AFA': 1, 'DEV': 1}
```


## [2026-09-14T03:28:16.611Z] TOOL CALL #83: Bash

```json
{
 "command": "python3 tools/verify_archive_sources.py 479 2>&1 | head -20",
 "description": "Check all cited URLs are archived"
}
```


### [2026-09-14T03:28:17.671Z] TOOL RESULT

```
14 cited URLs, 0 not yet archived
archived 0, failed 0
```


## [2026-09-14T03:28:32.491Z] AGENT

Done — `/home/sfmqrb/git/rishe/data/verification/page-479.json` written; `verify_check.py 479` reports **0 PROBLEM lines** (26/26 nodes, 2 roots), and all 14 cited URLs are archived.

**Page 479 (book p. 449) — 2 entries (entry 1 "Stena" is a redirect, skipped)**
- Node verdicts: 22 confirmed, 3 plausible, 1 transcription_suspect. Root verdicts: 2 confirmed (POK:1017 steigh- and POK:1029 ster-5 both verified verbatim in Pokorny).
- Ref checks: 28 supports, 1 partial, 1 contradicts, 2 not_found, 2 not_checked (unreferenced nodes).

**Flagged items**
- `transcription_suspect` — Steigh, node #7 **stitch** (under Gk. stixos): the printed page really reads "stitch", but AHD, Klein, Skeat, Pokorny and Etymonline all derive *stitch* from a different root (*steig- "to prick", Pok. 1016); the derivative of στίχος is **stich**. `error_in: book` (one-letter slip by Nourai), correct_form "stich". Page PNG saved to `data/verification/sources/refs/ocr/BOOK/479.png`.
- `plausible` — Ster 1, node #1 Avestan **wi-star**: star- is solid (Bartholomae col. 1596-98), but no vī- compound of ¹star- is attested in Avestan (Bartholomae, Cheung); *wi-star- is a back-projection from MP wistardan.
- `plausible` — Ster 1, node #2 Pahlavi **xâk-astar**: MacKenzie's MP word for "ashes" is *ādurestar*, and Mo'in's Borhān footnote compares ādur-star; the xāk- compound is New Persian (Wiktionary posits an unattested MP xākestar).
- `plausible` — Ster 1, node #9 **stray**: street is certain, but stray has a rival derivation (VL *extravagare, reprinted in OED) beside Klein's via strata.

**Reference errors in the book (not extraction errors)**
- `POK:107` on Steigh node #1 — p.107 is Pokorny's bhabhā "bean"; should be POK:1017.
- `POK:56` on Ster 1 node #7 (Arabic ṣirāṭ) — p.56 is Pokorny's *ar- "to fit"; evidently a slip for KLN:56, which is exactly Klein's "Al Sirat" page.

**No extraction errors found** — the JSON matches the printed page throughout (checked against the rendered PDF page).
