# Verification process log — verify-page-218


## [2026-09-06T15:10:29.885Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 218 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-218.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-218.json. Write /home/sfmqrb/git/rishe/data/verification/page-218.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 218` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-06T15:10:31.594Z] AGENT

I'll start by reading the instructions.


## [2026-09-06T15:10:32.262Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


## [2026-09-06T15:10:32.272Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-218.txt"
}
```


### [2026-09-06T15:10:32.322Z] TOOL RESULT

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


### [2026-09-06T15:10:32.325Z] TOOL RESULT

```
1	=== PDF page 218 (book page 188) ===
2	--- entry 0 ---
3	ROOT Gyŭna -> redirect to Yau
4	--- entry 1 ---
5	ROOT [Arabic] Ğ.z.l, Ghazâl : a new born deer, a wild goat  (refs FVA:209)
6	#1 (parent #0) [Persian] refs=FVA:297 | ğazâl «غَزال» : antelope ; Ğazâleh «غزاله» : a name
7	#2 (parent #0) [Spanish] refs=SKT:209 | gacele
8	  #3 (parent #2) [French] refs=KLN:644 | gazel
9	    #4 (parent #3) [English] refs=AHD:547 | Gazelle
10	--- entry 2 ---
11	ROOT [Parthian] Gzn : treasure  (refs SOD:182)
12	#1 (parent #0) [Pahlavi] refs=BQT:1841; FVQ:122 | ganj : treasure | NOTE: FVQ indicates that this word is possibly borrowed from a Median root
13	  #2 (parent #1) [Persian] refs=BQT:1838,1841 | ganj «گنج» : treasure ; gonjândan «گنجاندن» : to fit in | extra: گنجور ، گنجه ؛ گنجایش
14	    #3 (parent #2) [English] refs=FSD:1313 | Jasper 1 : "treasurer", a male name
15	#4 (parent #0) [Arabic] refs=FVQ:251; ARB:297 | kanz : treasure
16	  #5 (parent #4) [Persian] refs=MON:3096 | kanz «كَنز» : treasure | extra: كنوز
17	  #6 (parent #4) [Arabic] refs=PLA:108; FVQ:122; DOZ:60 | x.z.n : he saves, stores ; maxzan : storage ; maxâzin : storage
18	    #7 (parent #6) [Persian] refs=FVA |  | extra: خازن ، مخزن ، خزانه ، خزینه
19	    #8 (parent #6) [Italian] refs=None | mazazzino : storage
20	      #9 (parent #8) [French] refs=None | magasin : storage, store
21	        #10 (parent #9) [English] refs=KLN:922 | magazine
22	        #11 (parent #9) [Turkish] refs=ETM:70 | maghazeh : store
23	          #12 (parent #11) [Persian] refs=ETM:70 | mağâzeh «مغازه» : shop, store
24	#13 (parent #0) [Arabic] refs=KLN:648; FVA:82 | j.n.z : covers, hides ; jenâzeh : casket
25	  #14 (parent #13) [Persian] refs=FVA:82 | jenâzeh «جنازه» : casket, dead body
26	#15 (parent #0) [Greek] refs=KLN:644; FVQ:251 | gaza : treasure
27	  #16 (parent #15) [Latin] refs=None | gaza : treasure, the smallest Venetian coin paid for a newspaper, newspaper.
28	    #17 (parent #16) [French] refs=None | gazette : newspaper
29	      #18 (parent #17) [English] refs=KLN:644 | gazette
30	#19 (parent #0) [Sogdian] refs=SOD:182 | gzn : treasure
31	
```


## [2026-09-06T15:10:35.154Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-218.json",
 "description": "Read source JSON for page 218"
}
```


### [2026-09-06T15:10:35.193Z] TOOL RESULT

```
{
  "pdf_page": 218,
  "book_page": 188,
  "entries": [
    {
      "root": {"name": "Gyŭna", "redirect": "Yau"},
      "nodes": []
    },
    {
      "root": {
        "name": "Ğ.z.l, Ghazâl",
        "lang": "Arabic",
        "refs": "FVA:209",
        "gloss": "a new born deer, a wild goat"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Persian",
          "refs": "FVA:297",
          "words": [
            {"translit": "ğazâl", "gloss": "antelope", "script": "غَزال"},
            {"translit": "Ğazâleh", "gloss": "a name", "script": "غزاله"}
          ],
          "script_extra": null,
          "note": null,
          "quote": {"text": "تو آن وحشی غزال و هر قدم از من رمیدنها - من واین دشت بی پایان و بیحاصل دویدنها", "poet": "Hâtef Esfahânî"}
        },
        {
          "id": 2,
          "parent": 0,
          "lang": "Spanish",
          "refs": "SKT:209",
          "words": [
            {"translit": "gacele", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "French",
          "refs": "KLN:644",
          "words": [
            {"translit": "gazel", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "English",
          "refs": "AHD:547",
          "words": [
            {"translit": "Gazelle", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Gzn",
        "lang": "Parthian",
        "refs": "SOD:182",
        "gloss": "treasure"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Pahlavi",
          "refs": "BQT:1841; FVQ:122",
          "words": [
            {"translit": "ganj", "gloss": "treasure", "script": null}
          ],
          "script_extra": null,
          "note": "FVQ indicates that this word is possibly borrowed from a Median root",
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT:1838,1841",
          "words": [
            {"translit": "ganj", "gloss": "treasure", "script": "گنج"},
            {"translit": "gonjândan", "gloss": "to fit in", "script": "گنجاندن"}
          ],
          "script_extra": "گنجور ، گنجه ؛ گنجایش",
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "English",
          "refs": "FSD:1313",
          "words": [
            {"translit": "Jasper 1", "gloss": "\"treasurer\", a male name", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Arabic",
          "refs": "FVQ:251; ARB:297",
          "words": [
            {"translit": "kanz", "gloss": "treasure", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Persian",
          "refs": "MON:3096",
          "words": [
            {"translit": "kanz", "gloss": "treasure", "script": "كَنز"}
          ],
          "script_extra": "كنوز",
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 4,
          "lang": "Arabic",
          "refs": "PLA:108; FVQ:122; DOZ:60",
          "words": [
            {"translit": "x.z.n", "gloss": "he saves, stores", "script": null},
            {"translit": "maxzan", "gloss": "storage", "script": null},
            {"translit": "maxâzin", "gloss": "storage", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "Persian",
          "refs": "FVA",
          "words": [],
          "script_extra": "خازن ، مخزن ، خزانه ، خزینه",
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 6,
          "lang": "Italian",
          "refs": null,
          "words": [
            {"translit": "mazazzino", "gloss": "storage", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "French",
          "refs": null,
          "words": [
            {"translit": "magasin", "gloss": "storage, store", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 9,
          "lang": "English",
          "refs": "KLN:922",
          "words": [
            {"translit": "magazine", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 9,
          "lang": "Turkish",
          "refs": "ETM:70",
          "words": [
            {"translit": "maghazeh", "gloss": "store", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 11,
          "lang": "Persian",
          "refs": "ETM:70",
          "words": [
            {"translit": "mağâzeh", "gloss": "shop, store", "script": "مغازه"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 13,
          "parent": 0,
          "lang": "Arabic",
          "refs": "KLN:648; FVA:82",
          "words": [
            {"translit": "j.n.z", "gloss": "covers, hides", "script": null},
            {"translit": "jenâzeh", "gloss": "casket", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 14,
          "parent": 13,
          "lang": "Persian",
          "refs": "FVA:82",
          "words": [
            {"translit": "jenâzeh", "gloss": "casket, dead body", "script": "جنازه"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 15,
          "parent": 0,
          "lang": "Greek",
          "refs": "KLN:644; FVQ:251",
          "words": [
            {"translit": "gaza", "gloss": "treasure", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 16,
          "parent": 15,
          "lang": "Latin",
          "refs": null,
          "words": [
            {"translit": "gaza", "gloss": "treasure, the smallest Venetian coin paid for a newspaper, newspaper.", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 17,
          "parent": 16,
          "lang": "French",
          "refs": null,
          "words": [
            {"translit": "gazette", "gloss": "newspaper", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 18,
          "parent": 17,
          "lang": "English",
          "refs": "KLN:644",
          "words": [
            {"translit": "gazette", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 19,
          "parent": 0,
          "lang": "Sogdian",
          "refs": "SOD:182",
          "words": [
            {"translit": "gzn", "gloss": "treasure", "script": null}
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


## [2026-09-06T15:10:36.216Z] TOOL CALL #4: Bash

```json
{
 "command": "ls data/verification/ | head -50 && echo ---- && cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "List verification dir and source matrix"
}
```


### [2026-09-06T15:10:36.267Z] TOOL RESULT

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
page-130.json
page-131.json
page-132.json
page-133.json
page-134.json
page-135.json
page-136.json
page-137.json
page-138.json
page-139.json
page-140.json
page-141.json
page-142.json
page-143.json
page-144.json
page-145.json
page-146.json
page-147.json
page-148.json
page-149.json
----
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


## [2026-09-06T15:10:41.629Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['FVA','SKT','KLN','AHD','SOD','BQT','FVQ','FSD','ARB','MON','PLA','DOZ','ETM']:\n    print(k, json.dumps(d.get(k), ensure_ascii=False)[:800])\n    print()\n\"",
 "description": "Look up ref metadata"
}
```


## [2026-09-06T15:10:41.725Z] TOOL CALL #6: Bash

```json
{
 "command": "sed -n 1,80p tools/verify_check.py",
 "description": "Read verify_check tool"
}
```


### [2026-09-06T15:10:44.046Z] TOOL RESULT

```
FVA {"title": "S.M. Nahvi, Farhang-e Vazheha-ye Arabi dar Farsi (dakhil), Tohi/Azadi 1368/1989", "kind": "catalog", "url": "https://openlibrary.org/works/OL4602367W (edition OL2012991M: Intisharat-i Islami 1368/1989, 582 pp)", "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: no digital copy found.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 2026-09: still no digital copy on any permitted platform. Library catalogues list the 1368 book under the variant title «فرهنگ ریشهٔ وام‌واژه‌های عربی (لغات عربی مستعمل در فارسی دخیل)» — reconcile with Nourai's title when buying. Catalogue record only."}

SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Headword in caps at line start, e.g. grep -n '^TREE' SKT.t

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt", "page_offset": "KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 74

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only", "identifier": "watkins-american-heritage-dictionary-of-indo-european-roots-1985", "local_file": "/home/sfmqrb/

SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.com (links from farhangoadabeirani.blogsky.com post-482): vol 3 https://s3.picofile.com/file/82307409

FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ.txt"], "page_offset": "printed page = leaf − 17 (0-based \\f blocks in FVQ_pages.txt; 335 leaves)", "covers_etymology": true, "notes": "Good English OCR (Arabic script garbled). Same 193

FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-Dive), in.ernet.dli.2015.272042 (vol II), in.ernet.dli.2015.83695 (vol III), in.ernet.dli.2015.147440 (vol IV Sabi-Z)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt", "page_offset": "vol1: leaf = p + 41..56 (drifts; e.g. leaf 87 = p.46, leaf 612 = p.556); vol3: leaf = p - 1466 (e.g. leaf 215 = p.1681); vol4: leaf = p - 2144..2148 (e.g. leaf 229 = p.2373); vol2 o

ARB {"title": "al-Jawaliqi, al-Mu'arrab min al-kalam al-a'jami, Tehran 1966 (reprint of Ahmad M. Shakir's Cairo 1361/1942 edition)", "kind": "archive_djvu", "url": "https://archive.org/details/mo3rb (probably the Shakir edition) ; https://archive.org/details/almo3rab_gwaliqy_f_abduraheem (F. 'Abd al-Rahim ed., Damascus 1990) ; also uc1.aa0003615705 / AAlexandrina-148752 (Sachau's Leipzig 1867 ed.) ; text on shamela.ws", "lookup_hint": "Alphabetical Arabic headwords; grep in ARB_mo3rb.txt / ARB_abdulraheem.txt (raw, no page breaks); edition of mo3rb not confirmed — check its title page image.", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/ARB_mo3rb.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/ARB_abdulraheem.txt"], "page_offset": null, "covers_etymology"

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02

PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt"], "page_offset": "301 leaves (pdftotext -layout, \\f-separated): printed page = leaf(1-based) − 15 (leaf 291 = p.276).", "lookup_hint": "HathiTrust search-only; Google Books id q_ErAAAAMAAJ snippet view; DDB has only the tabl

DOZ {"title": "R. Dozy, Oosterlingen: Verklarende lijst der Nederlandsche woorden die uit het Arabisch, Hebreeuwsch, Chaldeeuwsch, Perzisch en Turksch afkomstig zijn, Leiden 1867", "edition_found": "1867", "kind": "archive_djvu", "url": "https://archive.org/details/oosterlingenver00dozygoog", "identifier": "oosterlingenver00dozygoog (also ...01dozygoog, ...02dozygoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/DOZ.txt", "page_offset": "leaf = printed + 11..13 (e.g. leaf 15 = p.2, leaf 43 = p.32). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Dutch headword in caps at line start.", "notes": "Built from djvu.xml."}

ETM {"title": "Mohsen Abolghasemi, Risheh-shenasi (Etimoloji), Qoqnus 1374/1995", "kind": "catalog", "url": "https://ketabnak.com/book/107170/ (no download) ; https://ketab.ir/book/2ebb5f53-ba49-4955-98f4-d419919d0ebc ; purchase: https://adinehbook.com/gp/product/9643110451", "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: not found.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 2026-09: no digital copy on any permitted platform; catalogue/purchase only."}
```


### [2026-09-06T15:10:44.086Z] TOOL RESULT

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
```


## [2026-09-06T15:11:11.297Z] TOOL CALL #7: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/page-202.json'))\nprint(json.dumps(d['entries'][0], ensure_ascii=False, indent=1)[:3000])\n\"",
 "description": "Inspect template verified page"
}
```


## [2026-09-06T15:11:12.304Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SOD gzn ===\" && grep -n \"yzn\\|γzn\\|gzn\" SOD.txt | head -30",
 "description": "Grep SOD for gzn"
}
```


### [2026-09-06T15:11:13.594Z] TOOL RESULT

```
{
 "entry": 0,
 "root": "Gwa, Gwâ, Gwen 2",
 "verdict": "confirmed",
 "modern_form": "PIE *gʷem- 'to go, to come' (with the collateral root *gʷeh₂- / *gʷā- 'to step, go'); Pokorny IEW 463-465",
 "note": "Pokorny's entry, which begins on p.463 exactly as Nourai cites, is headed 'gʷā-, gʷem- „gehen, kommen; zur Welt kommen, geboren werden“; gʷm̥-ti-s f., gʷem-tu-s m. „Gang, Schritt“', and it is deliberately a double entry (I. gʷā-, II. gʷem-), which is why Nourai's box carries two names, 'Gwa, Gwâ'. His third name 'Gwen 2' reflects the *gʷem- > *gʷen- variant Pokorny himself notes ('Unthematisch *(e)-gʷem-t (> *e-gʷen-t)', and Latin advenam / veniō with -n- for -m-); it is not a separate root in any modern handbook, so it is Nourai's own labelling convenience rather than an error of substance. Watkins/AHD 1985 heads the same material 'gʷā-. Also gʷem-. To go, come'; Cheung splits it into *gaH¹ (PIE *gʷeh₂-, Pok. 463 f.) and *gam¹ (PIE *gʷem-, Pok. 464 f.). The gloss 'to walk, to step, to come, to go' is an accurate rendering. Two words in the chart do not belong to this root: Avestan 'gâv' in node 6 (a misprint) and 'thamân' in node 12 (an unidentifiable form), and one Persian word, nîyâm (node 3), is derived by modern scholarship from a different root (*ni-dā-, not *ni-gam-). Everything else on the page is standard, well-attested Iranian etymology.",
 "note_fa": "جعبهٔ ریشه درست است: پوکورنی در صفحهٔ ۴۶۳ فرهنگ خود مدخل «gʷā-, gʷem-» را با معنای «رفتن، آمدن؛ به جهان آمدن، زاده شدن» آورده و همان‌جا نام‌های gʷm̥-ti-s و gʷem-tu-s «گام، رفتار» را می‌افزاید؛ پس هر دو صورت «Gwa/Gwâ» و «Gwem» از یک مدخل‌اند و برچسب «هندواروپایی» و معنای «راه رفتن، گام برداشتن، آمدن، رفتن» درست است. نام سوم «Gwen 2» گونهٔ *gʷen- است که خود پوکورنی (در *e-gʷen-t و در veniō لاتین) یاد کرده و در کتاب‌های امروزی ریشهٔ جداگانه‌ای به شمار نمی‌رود؛ این نام‌گذاری از خود نورایی است نه خطای علمی. واتکینز (پیوست AHD) نیز همین ماده را «gʷā-, also gʷem-: رفتن، آمدن» آورده و چونگ آن را به دو ریشهٔ *gaH¹ و *gam¹ بخش کرده است. در سراسر این صفحه تنها سه لغزش هست: صورت «gâv» در گرهٔ ۶ (غلط چاپی)، صورت «thamân» در گرهٔ ۱۲ (صورتی که در هیچ فرهنگی یافت نشد) و واژهٔ «نیام» در گرهٔ ۳ که پژوهش امروزی آن را از ریشهٔ دیگری (*ni-dā-) می‌داند.",
 "sources": [
  "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/gʷem-"
 ],
 "ref_check": [
  {
   "ref": "POK:463",
   "status": "supports",
   "note": "POK_02.txt line 1790 (the leaf whose running numbers are 463-465): 'gʷā-, gʷem- „gehen, kommen; zur Welt kommen, geboren werden“; gʷm̥-ti-s f., gʷem-tu-s m. „Gang, Schritt“, Verbaladjektiv gʷm̥-to-s. I. gʷā-: ... 2. gʷem-: ...'. The same pages carry 'av. gātu-s „Ort, Liegerstatt, Sessel, Thron“, apers. gāθu- ds.', 'av. gā-man- n. „Schritt“', 'av. jantu (*gʷem-tu-)' and 'av. jasaiti „er geht“' — i.e. Pokorny 463 alone underwrites the root box and nodes 1, 2 and 6."
  }
 ],
 "consulted": [
  {
   "src": "WLD",
   "where": "Bd. I 675-677 (WLD_Bd1 djvu line 42665 ff., running head 'gʷem-, gʷā-'
```


### [2026-09-06T15:11:13.639Z] TOOL RESULT

```
=== SOD gzn ===
14451:1050  'nyyznykh    B        jfjxS3Ji><S'j~xs3MKfs  ft) 
14501:1053  'nyznyy  =*  'nyzynyy 
14504:anxaz(e)nc   Onyznyy)   ©prcs.  pt. 
20514:1953  Wytyzn    B  J^V^w, 
20695:1985  Vswytyzn   B  tf«?..^  <U^UJjTl 
20712:1987  Hvswytkp'zn  =>  'wswytyzn 
21950:2163  }yjn  =»  yznyh 
22291:erzan   ©*arjydna  -►'yzn,  <vJn 
22328:escane  ?   Oysc'ny)  ^'yzn,  'scyWk,  (yjn 
22331:GMS  1041,  155  =  >yzn  +  one 
22682:2273  >yzn   S  klJ&ix^jJ 
22683:ezan   ^'yzn,  {yjn 
22688:2274  >yzn    C  4s^li  <jiui  jjl 
22689:ezan   ©<OP  arjana   ©pi.  -/   ^yzn,  *yJn» 
22700:2275  'yzndy  C 
22701:ezande   Oyjndy,  }yznty)   =>>yznty 
22705:2276  >yznty   B 
22706:ezande   =^Jyzndy 
22711:2277  'yznty  =»  >yzndy 
23567:arzdn   ^yzn,  }yzn,  'yscWy 
23577:2403  'yjndy   M  =»  >yzndy,  'yznty 
37031:4442  Ywryznych   S  (j->-V^)^f^u 
37039:4443  Ywry  zync(h)  =»  ywryznych 
37818:Yazn  <DParth.  gzn;  MP  gnz  ©nom.  ob.  -y(yk 
39423:ganzag  =*yzn- 
45808:5693  mzt'yzn   M  j^^jj  cc^^y 
50523:nizand   =*nyznt 
50528:nizandya/i   =»nyzndy* 
50607:6374  nyzn-   C  *^*~k 
50615:nizandya   (nyzntyO  =»nyz'ntyh,  nzndy*h
```


## [2026-09-06T15:11:18.166Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '37805,37840p' SOD.txt",
 "description": "Context of Sogdian gzn entry"
}
```


### [2026-09-06T15:11:18.214Z] TOOL RESULT

```
MDii  pl69  A- 17.2 

4551  YzS'n   B,  S  w-j  iohji^\  <j_*^ 
xazdan   ©<*azdana  <*asta-ddna;  Pahl.  fcz'n 

©loc.  -y 

grave 

Hen.  Tales.  478.4  n  p479;  Frag.  27,  6,  IIJ  1976, 
70;  GMS  117A 

4552  Yzn-   B,  M,  C  ^f 
Yazn  <DParth.  gzn;  MP  gnz  ©nom.  ob.  -y(yk 

ace.  -w;  loc.  -yh 
treasure 
VJ;  TSP;  Hen.  Tales.  486.4;  JRAS  1944,  138.9; 

GMS  1171;  Benv.  Notesiii  228;  Hen.  AM  1963, 

197;  Bailey.  Asica.  15;  C2  n  p96 

4553  Yznpr   B  J*dj^<jj>*£ 
yazn(3ar  ©pi.  -/ 

treasurer 

VJ  106;  GMS  1131;  pi.  -flar>yh  VJ  1332  n  p98 

4554  Yzny*  C  g^  ^U- «*l>- 
yaznya 

treasury 

C2,  51R  4n  p96;  BSTii  885.4
```


## [2026-09-06T15:11:20.847Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Yzn\\|yzn'\\|Yzn'\" SOD_pages.txt | head -20; echo \"=== find page ===\"; python3 - <<'EOF'\nimport re\np=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD_pages.txt',encoding='utf-8',errors='replace').read()\npages=p.split('\\f')\nfor i,pg in enumerate(pages):\n    if 'Parth. gzn' in pg or 'Parth.  gzn' in pg:\n        print('leaf',i)\n        print(pg[:200])\nEOF",
 "description": "Locate SOD page for gzn"
}
```


### [2026-09-06T15:11:23.092Z] TOOL RESULT

```
16728:4552 Yzn- B, M, C                                                       that, he, the
16738:4553 Yznpr B                                 J*dj^<jj>*£                wen- (XZYH) ©Idg.
16745:4554 Yzny* C                               g^ ^U- «*l>-
=== find page ===
leaf 247
                                                      If» ■■!!■■

                                                                                                                               182

 y
```


## [2026-09-06T15:11:34.065Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SKT gazelle ===\" && grep -n -i \"GAZELLE\\|GAZETTE\" SKT.txt | head; echo \"=== KLN_1966 gazelle/gazette ===\" && grep -n -i \"^gazelle\\|^gazette\\|gazelle,\\|gazette,\" KLN_1966.txt | head -20; echo \"=== KLN 1971 ===\" && grep -n -i \"gazelle\\|gazette\" KLN_1971.txt | head -20",
 "description": "Grep Skeat and Klein for gazelle/gazette"
}
```


### [2026-09-06T15:11:34.152Z] TOOL RESULT

```
=== SKT gazelle ===
755:Anlelopu.  vGk.)  In  Spenser,  F.  Q.  i. fi  J^.  iS.-iicI  to  be  corniptcd  from  latt  Gk. ilrfiaAi>»-,  or  d.vBnXon-,  the  stem  o^  uv&t\Ka/\tf or  lii^uAo^,  used  by  Eiifitathitu  of  Antiodi to  signify  *  bright*  eyed,'  i.  c.  a  gucUe Coined  from  Gk  dftfiif,  lu  iprout.  iNoaom, aUo  lo  shine;  nnd  w\f/  'gen.  iuir(^t\  the  eye. See  Auiher  and  Optica.  ^  Tlic  word Dorau,  tilt*  Gk.  and  Roman  name  of  the gazelle,  IS  from  SV^ico/icu,  1  see  clearly.
23600:French  from  Italian:  bojilion,  bauble (j).  bergamot,  brigade,  brigand,  brigantine, brig,  bnisquc,  burlesque,  bust,  caprice,  ca- puchin, caronsal  (a),  casemate,  charlatan, frigate,  gala,  gallery,  gallias,  gazette,  gusset, maroon  (i),  pavjuin.  pa-^ninade,  pistol, pistole,  ravelin,  rodomontade  theorbo,  ton- tine.
=== KLN_1966 gazelle/gazette ===
15884:gazebo,  n.,  turret,  balcony.  —  Facetious  forma¬ tion  fr.  gaze  after  L.  videbo,  ‘I  shall  see’, gazelle,  n.  —  F.,  fr.  ghazel,  N.  African  pronun¬ ciation  of  Arab,  ghazdl.
15885:gazette,  n.,  newspaper.  —  F.,  fr.  It.  gazzetta,  of s.m.,  fr.  gazzetta,  name  of  the  smallest  Venetian coin,  said  to  have  been  paid  for  the  perusal  of  the manuscript  newspaper  issued  by  the  Venetian Government  once  a  month.  It.  gazzetta,  ‘coin’, is  prob.  a  dimin.  formed  fr.  L.  gaza,  ‘treasure’, fr.  Gk.  y <*£<x,  which  is  of  Persian  origin.  See genizah  and  cp.  next  word.
15886:Derivatives:  gazette,  tr.  v.,  gazetteer  (q.v.) gazetteer,  n.,  1)  a  journalist;  2)  a  geographical dictionary.  —  F.  gazettier  (now  spelled  gazetier), lit.  ‘one  who  writes  in  a  gazette’,  fr.  gazette.  See prec.  word  and  -eer.
=== KLN 1971 ===
19479:ariel, n., a gazelle. — Arab, dryil, a vulgar variant 
75520:name derives from Gk. Sopxic, ‘gazelle’, which 
79871:‘antelope, gazelle’. All these words derive fr. 
100799:gazelle, n. — F., fr. ghaztl, N. African pronun- 
100802:gazette, n., newspaper. — F., fr. It. gazzetta , of 
100811:Derivatives : gazette, tr. v., gazetteer (q.v.) 
100812:gazetteer, n., 1) a journalist; 2) a geographical 
100814:lit. ‘one who writes in a gazette’, fr. gazette. See 
100817:Derivative: gazetteer, tr. v. 
101114:‘young deer, gazelle’. See hind, ‘female of the 
101423:also gazette and the first element in Gaspar, 
229974:springbok, n., a South African gazelle. — S. Afr. 
239955:of tabhya, ‘gazelle’, which is rel. to Heb. tz e bht,
```


## [2026-09-06T15:11:35.665Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AHD watkins gazelle ===\" && grep -n -i \"gazelle\" AHD_watkins1985.txt | head; echo \"=== FSD jasper ===\" && grep -n -i \"jasper\" FSD_vol3.txt | head -20; echo \"=== DOZ ===\" && grep -n -i \"magazijn\\|magazin\" DOZ.txt | head -20",
 "description": "Grep AHD, FSD, DOZ"
}
```


### [2026-09-06T15:11:35.761Z] TOOL RESULT

```
=== AHD watkins gazelle ===
=== FSD jasper ===
74236:reront reooTt or acioimt. tidings, as, /o ICS Iron) tin •« at neat Jasper H. A ciuuiiy In N (leorglu. 259 sq m.
150247:Georgia. 210 sq. m . oountynnat, Jasper. 4. A county In
172559:i'p«», 1 is)'p«( 2 i»0'po, « I Vfr I 1, \ grwMi Jasper highly
172942:wan*, Jasper or the like i a trade term
208514:xtonr, Uispts, joaper, onyi ploama, porcelain jasper, prase,
243524:William the Conqueror 4. B. 11. (about lori2-*/Ml 1.34). in alluslun to his blue ribbon os Knight of the Carter Jasper Ludwig. HtN>i>i>EKii AuiEur
=== DOZ ===
1819:MAGAZIJN.
1845:het Dnitsch is Magazin niet oud; volgens Sefamitthen-
```


## [2026-09-06T15:11:45.420Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SKT leaf 229 (p209) ===\" && awk 'BEGIN{RS=\"\\f\"} NR==230' SKT.txt | head -60",
 "description": "Print Skeat leaf for page 209"
}
```


## [2026-09-06T15:11:46.057Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '101400,101440p' KLN_1971.txt",
 "description": "Klein genizah entry"
}
```


### [2026-09-06T15:11:46.845Z] TOOL RESULT

```
=== SKT leaf 229 (p209) ===
e.  Lc.  drongly 1--  eum/a,  Gk.  cofiAij,  a  »pccie& Ski  >«i//,  to  slink. S  ;  K«  Houa«. iing.     a     kind     of    fence ;     sec
tiound ;  Mv  Hoar •e^  hiving  a   rough,  harsh  voice, he    r   is    intnj5iv'e,    bttC   sometimes 1  M  E  Affn,  pio(>erly  Aoos.  hoatse U«  hoarse.  -^  Iccl.  Aitts,  Dan.  /uts, Du.  A/z/fA,  G.  Ariifr, see  Hoar. Hocua. Hub,    ihe  nave  nf  a  whrel, ite.    ^E.}     The  true  sense  is the  had  of  a  firc-plve  was ibed  slane  on  ciihcr  siJc  of  the tirecn    which   the  embers   were [Wehattrl.      Closely   telatefl  to lich    is   merely    the    nasalises) Der.  k^^naii,  a  nail  with  a
\\  %  ctowu,    mstic,  a  fairy.    (F. ^.)      'Elvts,    kohs,   and    fairies;* and   Fletcher,    Mods.  Thomas. was  a  common  personal  name, of  Ro^in  (.like  Hodgt  from narac  H^in    is   F.,  and  is i>tion  of  PoUrt,  a  came  of ongui.      Der.    hebgobiim ;    see
I
;  see  Hop  (I). (I),     an    ambling    lutg ;    see
r    (l\    •    kind    of   telocD ;    Me
I.
obllB ;  wfK  Hob  <  3)*
•llf  see  Hob  (I'l.
Habn&b.  with  free  leave,  at
\     Compounded   of  hah  and
'o  have,  hence  a[>plied
leaving  it,  implying
w  a  familiar  invitation
lo  hU-noh  together.'     Hab
'i  to  have  :  nab  is  from
put  for  mi  httUan^  not  to
re.
ce  Hou£h
winc-    G  \     For  U^khttm. a  place  m  Gcimauy,  on  the
MS
rlv«r  Main,  whence  the  wine  comci.  It mean-"* '  high  home.*
Hockey,  a  gamei  see  Hook.
Hoous-pocUB,  8  juggler's  trick,  a  jug- gler. (Low  L. )  As  iar  as  it  can  be  said  to briong  to  any  language,  it  is  a  sort  of Laliti,  having  the  L.  termination  -tu. But  it  is  meitly  an  invented  term,  uud  by jugglers  in  performLng  tricks ;  see  Todd's Johnson,
hoax.  (Low  L.)  Short  for  hocus ,  i.e. to  juggle,  cheat.
Hod.,  a  kind  of  trongh  for  earthing bricks.  (E.)  A  prov.  K.  form  of  MoU;  see Hold.  In  Lmc.  and  York,  hod  meana 'hold'  or  •  receptacle';  as  in  (Whitby) PowiUr.hoiit  p<jwder-flask  ;  asnnUM»i,  am- dle^tick.     %  Not  from  K.  hotte,  as  said.
Hodge-podge .-  see  Hotobpot.
Hoe:  M:e  Hew.
Hog.  (E.)  M.E.  Ai7jj:y,  *maialis,e5tenim porcus  carais  testiculis';  Catbol.  Anglic, p.  1 8  ; .  K  rom  the  verb  hack  \  Scotch  hag),  to cut-  Ci.hcg-shnp.  one  clip|«il  the  first  year.
Hogahead.  tO.  Du.)  More  contctly, oxhtad.  An  adaptation  of  O.  Du.  okihoojd^ oxhoefdt  a  hogshead :  of  which,  however, the  lit.  sense  is  ex-head.  So  also  Dan. oxhoved,  O.  Swed.  oxhufwud,  an  ox>hcadt also  a  hogshead.  No  doubt  the  cask  was at  first  named  from  the  device  or  brand  of an  '  ox  head  *  upon  it.
Hoiden,  Hoyden;  see  Heath.
Hoist,  to  heavij.  (O.  Du.)  The  final  i is  rluc  to  the  pp.  hout,  used  for  hoiscd. The  verb  is  really  h&ise.  (Cf.  graft  for «T[i^)«»0.  Du.  hyssen,  Du.  htjsschtn.  to houc  {y  sounded  as  E.  long  r.4'Dan, htise,  hisse ;  Swed.  hissa,  to  hoist  (whence K.  hiistr).  %  Not  allied  to  F.  Aaujur,  to elevate.
Hold  (0,  to  keep.  (E.)  A  S.  htaldan. •4-  Du.  heuden,  Icel.  haida,  ^wcd.  h^Ua, Dan.  h^lde,  Goth,  haldam,  G.  halten.  Dor. hold,  sb.;  abo  b<  hoid,  with  prefix  b<-  <£. by);  up-hold.
upholsterer.  (E.)  Lengthened  from Nf*hohtrr,  put  for  ufhoid-ster,  another  form uf  upholder,  which  was  fonneily  used  of  a dealer  in  fuinituie,  lit.  one  who  kaldi  up  to sale.
Hold  (>),  the  'hold'  of  a  ship;  tea Hole.
Hole.  (E.>  M.  E.  holt,  hsl,  A.S.  M a  cave.  ^  Do.  Ac/,  Iccl.  hol^  Dan.  Aw/. Swed.  hM.  G.  hohL  Cf.  Goth,  mhulom^ lo  hollow  out.      p.  Prob.  A.  S.  W  is  fiom
206
HOUBUT.
Jko/fta.  pp.  of  str.  vb.  AeloM,  to  cover ;  see HflU.    Not  allied  to  Gk  roTAof,  hollow.
hold  (f),  the  cavity  of  a  ship,  (Da) Put  for  ho!<.  wilb  cKCresccnt  <l'»  doc  to confusion  with  the  verb  to  Ar/e^.  —  Du. Atf/,  a.  hole,  CAve,  esp.  tucd  of  ths  hold  of  a ship  (Sewrcl).
hollow.  (E.)  M.  £.  Ac/we,  adj.  A.  S. Jkff/A.  sb.  a  hollow  pUcc.  also  spelt  Aa^. Extended  from  A.  S.  ho/,  a  hole,  cave.
Holibut.  Holiday;  sec  Hale  (i).
HoUa,  Hallo,  Slop!  wai
```


### [2026-09-06T15:11:46.905Z] TOOL RESULT

```
mistranslation of another Greek case name see 
accusative. 

Derivatives: genitiv-al, adj., genitive-ly, adv. 
genito-, pertaining to the genitals. — Fr. L. geni- 
tus, pp. of gignere. See genital, 
genius, n. — L., ‘tutelary spirit; inclination’, orig. 
‘generative power’, for *gen-yos, fr. I.-E. base 
*gen-, ‘to beget, produce’. See genus and cp. king, 
genius loci, the tutelary of a place. — See prec. 
word and locus. 

genizah, n., storeroom of a synagogue in which 
Hebrew books are preserved. — Mishnaic Heb. 
g*nizd h , ‘hiding place’, fr. ganaz, ‘he saved; he 
hid’, rel. to Biblical Heb. g e nazim (pi.), ‘treasury’ 
(in the Bible the word occurs only in the construct 
state pi. ginzd); borrowed fr. Pers. garij, ‘treas- 
ure’, whence also Aram. g*naz, ‘he saved’, 
ginzd , gazzd, ‘treasure’, Arab, janaza , ‘he cov- 
ered up’. Cp. Arm. garij, Gk. ydc^oc (whence L. 
gaza ), and Hung, kincs, ‘treasure’, which are 
also Persian loan words. Cp. also gunge. Cp. 
also gazette and the first element in Gaspar, 
Jasper. 

genocide, n., extermination of an ethnic group. — 
Lit. ‘killing a tribe’; a hybrid coined fr. Gk. 
yevo?, ‘race, tribe’, and L. -cidere, fr. caedere , 
‘to kill’ ; see genus and -cide, ‘killing’. The cor- 
rect word would be genticide, in which both 
elements are of Latin origin. The word genocide 
was introduced by Raphael Lemkin in his Axis 
Rule in Occupied Europe, 1 944, p. 1 9. See Encyclo- 
pedia Britannica, Book of the Year 1949, p, 386. 
-genous, suff. forming adjectives meaning 1) ‘gen- 
erating, producing, yielding’, as in erogenous; 
2) ‘produced by’, as in autogenous. — Com- 
pounded of the suffixes -gen and -ous. 
genre, n., 1) kind, sort ; 2) style. — F., fr. L. genus , 
gen. generis , ‘sort, kind, class’. See genus and cp.
```


## [2026-09-06T15:12:10.059Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"azelle\\|Gazel\\|gacela\\|gazella\" SKT.txt | head -20; echo \"=== leaves containing Gazette/Gazelle ===\"; python3 - <<'EOF'\np=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt',encoding='utf-8',errors='replace').read()\nfor i,pg in enumerate(p.split('\\f')):\n    if 'azelle' in pg or 'Gazette' in pg:\n        print('leaf(0-based)',i,'=> printed',i-20)\nEOF",
 "description": "Find gazelle in Skeat"
}
```


## [2026-09-06T15:12:10.996Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== DOZ leaf ~71-73 ===\" && sed -n '1810,1860p' DOZ.txt",
 "description": "Dozy magazijn entry"
}
```


### [2026-09-06T15:12:11.648Z] TOOL RESULT

```
755:Anlelopu.  vGk.)  In  Spenser,  F.  Q.  i. fi  J^.  iS.-iicI  to  be  corniptcd  from  latt  Gk. ilrfiaAi>»-,  or  d.vBnXon-,  the  stem  o^  uv&t\Ka/\tf or  lii^uAo^,  used  by  Eiifitathitu  of  Antiodi to  signify  *  bright*  eyed,'  i.  c.  a  gucUe Coined  from  Gk  dftfiif,  lu  iprout.  iNoaom, aUo  lo  shine;  nnd  w\f/  'gen.  iuir(^t\  the  eye. See  Auiher  and  Optica.  ^  Tlic  word Dorau,  tilt*  Gk.  and  Roman  name  of  the gazelle,  IS  from  SV^ico/icu,  1  see  clearly.
=== leaves containing Gazette/Gazelle ===
leaf(0-based) 34 => printed 14
```


### [2026-09-06T15:12:11.691Z] TOOL RESULT

```
=== DOZ leaf ~71-73 ===
Zie Azuur.
LIMOEN.
Het Perz. litnoen (ook liinoe en limoend), in 't
Arab. laimom.
LUIT.
Fr. luthy Sp. laud, Port. alaud; de laatste vorm60
is de zoiyerste, want het is. het Arab. al-'oed (j^))>
samengesteld uit het lidwoord en het woord 'oed, dat
hetzelfde instrument aanduidt.
MAGAZIJN.
Het Arab. machzeny verzachte uitspraak machazeUy
van het werkwoord chazana^ bewaren, de plaats, het
gebouw, waar men iets bewaart; Sp. magacen, ook
almacenj Port. almazem, armazem; Ital. maggazino;
Fr. magasin. Het woord is bg ons niet oud; Kiliaan
heeft het niet; en Ambrosius Zeebout; die met van
Ghistele, bg wien hg kapelaan waS; in 1481 het Oosten
bezocht; vermeldt het als een Arabisch; toen hier nog
onbekend woord; daar hg zegt (Tvoyage van Mher
Joos van Ghistele, p. 198): ;,Ende in d' onderste pan-
den siint al verwelven vauten elck afgeschutt op hem
selven, daer elc coopman zyn coopmanschap in sluut;
'daer ghenaemt MagasienneU;" en elders (p. 228): ;,Maer
hoewel dattet een schoon behuysde plaetse is daer en
zijn poorten noch mueren: Ende is een vanden besten
A venen vander Eooder ZeC; daer oock aencommen alle
de Specerien die gebracht werden wt India ende den
lande daer ontrent; naer de landen des Souldaens ende
naer Europen. De Souldaen heefter doen maken veel
groote huysen ghenaemt Magazeeneu; daer in al de
specerie gedaen wert als zy ontladen iS; ende moet
daer eenen zekeren tgt bliven eer mense verpumen
mach: Dien tijt leden ; de Souldaen zgn Eecht heb-
bende; so wertse ghevoert met groeten Carrevanen
daer mense hebben wilt al de weerelt deure." Ook in61
het Dnitsch is Magazin niet oud; volgens Sefamitthen-
ner's Wörterbuch, umgearbeitet von Weigand, is bet
daarin eerst in de 17® eeuw opgenomen.
MAMELUK.
In het Arab. mamloeky slaaf; het is het partic. pass.
van het werkwoord malaka, bezitten. Het korps ma-
melukken ; dat de Egyptische sultans in de 13® eeuw
vormden, bestond uit jonge slaven, vooral uit Circassië
en Mingrelië, die door de Mongolen gevangen waren
genomen en die de genoemde sultans van hen kochten.
Later werd het steeds op dezelfde wgze aangevuld.
MAROKIJN.
De naam, die door de Europeanen aan het geiten-
leder gegeven wordt, dat in Marocco gemaakt of in
Europa nagemaakt wordt. In Marocco zelf heet het
niet zóó, maar filali^ filêlï, naar de provincie Tafïldlet,
```


## [2026-09-06T15:12:22.868Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\np=open('SKT.txt',encoding='utf-8',errors='replace').read().split('\\f')\nimport re\nfor i,pg in enumerate(p):\n    if re.search(r'Gauze|Gavotte|Gauntlet|Gaunt\\b|Gazcttc|Gazcllc|Gaze\\b', pg):\n        print('leaf',i,'printed~',i-20, repr(pg[:300]))\n        print('---')\nEOF",
 "description": "Locate Skeat G-section leaves"
}
```


### [2026-09-06T15:12:24.682Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T15:12:36.424Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\np=open('SKT.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in range(216,232):\n    t=' '.join(p[i].split())\n    print('LEAF',i,':',t[:160])\n    print('   tail:',t[-120:])\nEOF",
 "description": "Scan Skeat leaves 216-231"
}
```


### [2026-09-06T15:12:38.118Z] TOOL RESULT

```
LEAF 216 : wtth : ' -wmJUS: see Ha1«. vrawlering of mind. _„ Aii.j.v.'i/id//>, a wanoerin^ of the ^m^jlk Ad//Mc'iiMW. aUucimari, aluH' wmA*x in nund, dxram, lave. tjilsi ;
   tail:  hangodt, to hanj; down ^intr.); denvcd from the base of the A. S. strong verb kSn (contracted form of hangiin\ pt. I. h
LEAF 217 : Mg, pp. haHgiti.-^X^X. htnga, weak verb, from hanga {pt. t. lUkk, for kMk*^ pp. ^dfi^i>r#i) ; G. hkngiHt weak verb, from G. hangin <pL t. king, pp. gtkamgm). Al
   tail: n ; d. lul. arUcthtno, a bafloon, The Itnl. vord seemi^ to be derived .; ibcO. F.phnAcwa&/j ntau^nw hUr- Low I* kcrU^uim
LEAF 218 : familioi), a Iroc^p laos Uut haunted lonely places. This «B CO be derived from O. Fries. heiU lS. htili cyn, Iccl. htljar kyn), i.e. bell, host 01 hrll, troop o
   tail: n), i.e. bell, host 01 hrll, troop of cluu'tfe (torn htIU.juiH to from a popular cl)molcigy the word with CkArlts Muller
LEAF 219 : , Lect. ii. 58 1. (F. - Tent) Orig. used of and not aJ «-&)-$ in ■ very bad to mod. E. 'fellow;' Lh. S4Q. — O, F. ktrlot, arlot. a vagabond ; luioi, a vagabond 
   tail: ke. — L. kasta, a spear. Allied to Oood. Haate, verb and sb. (Scaod.) O. Swed. hasta^ to haste, haai, baste; Dan. haste,
LEAF 220 : to baste, hast, baste. 4* O. Fries. Mast, sb., Du, haasttn, G. hasten, vb.. Du. haasi. G. hast, sb, Allied to Skt. p>f (for fas), to jump; see Hare. (^ KAS.) Xt
   tail: c, kaxnc, Icel, Atf**r, Swed, {Ml, O. H.G. hafmM. Prob. lied to fcl. Aow. L. «/^rr ; see to carry sboot for sale (O. vtr
LEAF 221 : b formed from the %b. RAvk«r. to clear the tbro&t (W.) kwk ; <l#rA. the throwing up (O. Low G.) Intro- Ketbei lands ; Do. heuktr, Dtt ktuktrtn, lo hawk, sell ia
   tail: s. .^K ^M- ■ r 1 G^ Ylkw».^-=-=£. ^r-«. 4 n.M«l s« s^ «. SMT ^iA ai tad HECKLE. H«<^W« H«tohttl: fccHook .« a icver. (F.
LEAF 222 : -Gk.) n Low L. Aertuus^). ic, oonsumptivc. •Gk. ; aJ»o. a habit of body. of Ix**'* to luvc, hold. ft ballr. CC^k.) From Gk. ff*£tor, oelcbraied hero of Troy. Li
   tail: . Alli&I to Hell. Helmintholoffy, history of worms. (Gk.) Coined trom Gk. iX/uvSo-, crude form oiis^rt, a worm ; -Acryio
LEAF 223 : , a discourse, from A,i7ii»', to speak. The sb. i\i»tvt, also <A/ii(, means ' thai which curls about ; ' allied to HeUx. Helot, a (Spartan) slave. (L.-Gk.) L. p
   tail: (Gk.) Vx. ' seven-angled." - Gk seven ; yoitia, an oiigle. allied to y«n. See Beren and Knee. hebdomadal, weekly. (L^Gk)
LEAF 224 : hetniomatialit. — Gl. is^.n:u-\S. t-»*n iQhofiM, a week.— ' heptahedroD, » (Gk.) KromGk. 2«ra,fccvca, iJ^a^ seat (allied to £. Bit). heptarohjTi m« As^k^pf^j, H
   tail:  10 fats lord ; after- to include borse«, &:c — If ; piitUt£eatuH, appaict, HeriUee : see Heir. Hermaphrodite, an animal
LEAF 225 : or plant of both sexes. i,L. — Gk.> \.. k4rmaphrodhHS, ■■(*k. Jp>io<f<pi'>iSiTac ; coined fiom 'Ep^i^c. Mercury (repre^cnling ihe male) aiid 'h^poZiTt}^ Venus (
   tail: ). hiffht, was or is called. (E.) The only E. verb with a jHtsrivt sense; he higkt = he was named. M. E. highte ; also h
LEAF 226 : atu^ kette. A. S. Mdttt, I am called, I was called ; pt. t of A. S. htitan (i) to call (2) 10 be called, be named. So also G. iek keine, I am named ; from heiss
   tail: to shew, explain. ; seeH«tsl« <^) (t) M E A/«i-^. key, ky. A. S. A/A. 4> Du. iA^i', IceL A^r, Swrd. CiuL Ui, G. ^mA<. G.
LEAF 227 : k<Kk. The •coic is bctit, hrnoe loimded, knob- at a iBouiid or hill Cf. G. kiigtl, s Lfcnob. biHock. Ski. ht<ka^ the female as well C«*A.^. Jn («U»ve , ^ locL i
   tail: st. horehotuad, a plant, h^rkfiHHJ \% the white. irt. The final ti is excr«f - AdrJkJftf, also calleil siinpiy Hdr, boar
LEAF 228 : : Aiin
   tail: : Aiin
LEAF 229 : e. Lc. drongly 1-- eum/a, Gk. cofiAij, a »pccie& Ski >«i//, to slink. S ; K« Houa«. iing. a kind of fence ; sec tiound ; Mv Hoar •e^ hiving a rough, harsh voice
   tail: llow pUcc. also spelt Aa^. Extended from A. S. ho/, a hole, cave. Holibut. Holiday; sec Hale (i). HoUa, Hallo, Slop! wai
LEAF 230 : t! (F.) Not the same word as Aa//ao, to &hout; but difTcrciitly usc't in old aulhore. See Oth. t 2 56; As You Like It. iii. 3. «5;. — F. 4W(}, * an tnierJLCtion
   tail: OQ)0^ (£.) AS. ^Jrt, a hone, (with _ from d lo long e, as iii d^rin, bone). > led. Jknn, SweiL ^^ ; Skt fdna. a *^' «oo�
LEAF 231 : � EromjT, tu sharpen ; Gk, jHlrt-of, > eoBT, poik. Sec Coae. Bonest ; see Honour. Ho&ey. {£.) Si.K Auhi. AS. ^«nr^'. Dd Aamir, I eel. hunaug, Don. honnhig, * kc
   tail: me in whicb children A^p over tceUhsSf i.e. lines scoicd on the ground. f*tmt% HOST. WOT. Ion3 ; -— V-'-'l'tile kmMp€M •
```


## [2026-09-06T15:12:46.753Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\np=open('SKT.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in range(190,218):\n    t=' '.join(p[i].split())\n    print('LEAF',i,':',t[:110])\nEOF",
 "description": "Scan Skeat leaves 190-217"
}
```


### [2026-09-06T15:12:49.282Z] TOOL RESULT

```
LEAF 190 : fuUocks ^joot-ffcJu (cf. buUock). Bailey gives tbe lorm/w/-AM7<(.r. Future, about to be. (F.-L.) O. F. futur^ 
LEAF 191 : Icti.ga//, Swed. gati^ Dan- gaJ(/f (tor galif). G. ga/U. i^/tf, Gk xnAi;. Allied to YeUow and Oreea. Gall (2>.
LEAF 192 : ent.. The particle go or gu ecuv an adj. into &n anv. Qalvanlsm (Hal.) Named from su/zi of Bologna, Italy; abo
LEAF 193 : man, I gamm/»t O. Swed. gamffum, O. H. G man, jov. mirth. gamble. (F..> A late word, put gttmm U or gam U, a f
LEAF 194 : aao. Garland. i.F.-TetitT) M. E.^ — O. ¥. gariofu//. Cf. Span, ^tnrmt Ital.ghir/oMifa 1 whence mod. F.gMtrian 
LEAF 195 : — O.V.joel, Jouel (later jpyau), dimin. of F- toU, used m the sense of trinket ; see joy (below). % Early mimn
LEAF 196 : gem- ran, to produce, — U g<nfr-, item oigmus. greneric, pertaining to a germs. (L.) Coined from I- gentri-, c
LEAF 197 : y. ~L. €X, very; sg^r, a heap, from <v- - o//, to, genre, to bring, gestAtion, the carrying of the yoting in G
LEAF 198 : to F. gi^iir. game. Cf. I, a fc7«r» giztaid. r. (E.J M. E. giM, adj. Formed S /iddtam, to king, be merry; mj «
LEAF 199 : 'rr/, gu*J, often tued to mean ' a boy ;' a c^ld. Formed, fts a dimin.. from O. Low G.gor, ft child. Cf. i}wis
LEAF 200 : e, O Du. iupptH. Sec Lop. Glide. CE.) M.E. gUdm, pt. t. gi»od, A. S. ^iitian. + Du. gltjtfin, Dan. xi'iV/ir, S
LEAF 201 : of gimtin, U swallow. glutton. (F.-M M.E.^;*/#».-O.K glofoH. * L. ace. gikta/itot, a glotlon. •• ginlire, to d
LEAF 202 : and.) In J^vins. Lit. to run like cattle stui^ by Riea.— Icel. ^/i/a, to goad. •• Icel. j«(/i^ (sboTc). rw^ri 
LEAF 203 : , to gild (Etlmlillcr) ; d. K.^. gyldfn, golden. Formed (by regular change fioni o lojf) from gold, gold. Qol^
LEAF 204 : of a spout. Formed _ _ th» throat (above). So also '/^fg^, a gargoyle; Ital ^r^zta, from gsfptf tlic chroa.L a
LEAF 205 : gm/m'tas.^1^ grmtui- iui (abovc^ gratulate, lo congratuUle. (L-) From pp. of L. graiuJari, to wish a person jo
LEAF 206 : . (F. — L.) M. E /^vmtK — F. ^tmifr, variant of ^tnier^ a gra- — L. groftaria, a grajiary. — L. r*rjw, com. ga
LEAF 207 : o icue with a grapnel. — O. F. gmppii, sb., • the grappU of a ship;' Cot. — 0. I'gnxppt, a hook ^above). Oraph
LEAF 208 : dirt ; ^^^K, 'lieht-tliii, rc/it$e ol tal- ^^^^^pjulciug ; Swed. dial, ^trvar, Dliu <f Low li. ^rven, greaves,
LEAF 209 : \. S. grimlan, pt. t grand, pp. gruiiden. Allied to h.friare, to rub, Gk. xpitiv. to graze, Ski. gkiish, to gr
LEAF 210 : t of a ,) From gyvunJ, Milb double M. V-aV', with a cunleraptuous n, dnft. (C) This pecnliar tobcCe]tic» Gael.
LEAF 211 : il. giisa, to guc»s.+ Du. gissem, eel giska. Allied to Dan. gjeae. to guess ; the Iccl. giika stands for git-s
LEAF 212 : 'a &OID the lound which the fisli Ukm oot of the water. • O. F. (F. grpgnarJ), gi uatm^, grunter . O- F. gtunt
LEAF 213 : bluff callcil haftriaj in O. F. , see Liber AUua, ed. Riley, pp 235, 331. *0. led. hapuriaxk, ihiogs oif small
LEAF 214 : alicnem. — L. habi' kaiitartt to dwell, ficqucnt. (F.-L.) P. hahifU'U, c«s- , ild^i/ui/tf,conditioD. «• i^AoAi
LEAF 215 : Helm (1). Halcyon, a kingfisher; as adj. serene. (L. — Gk,) Halcyon days = calm days; it was supposed lliat (b
LEAF 216 : wtth : ' -wmJUS: see Ha1«. vrawlering of mind. _„ Aii.j.v.'i/id//>, a wanoerin^ of the ^m^jlk Ad//Mc'iiMW. aUu
LEAF 217 : Mg, pp. haHgiti.-^X^X. htnga, weak verb, from hanga {pt. t. lUkk, for kMk*^ pp. ^dfi^i>r#i) ; G. hkngiHt weak
```


## [2026-09-06T15:13:00.268Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\np=open('SKT.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(' '.join(p[195].split()))\n\" | head -c 3000",
 "description": "Print Skeat leaf 195"
}
```


### [2026-09-06T15:13:01.863Z] TOOL RESULT

```
— O.V.joel, Jouel (later jpyau), dimin. of F- toU, used m the sense of trinket ; see joy (below). % Early mimnden^tood, and wrongly Latinised as iofale, as if it were a derivative of i»cu$, which is not the case- joy. (F.-L.) M.E. Hy^.-O. F- ioyt, joyt ; oldest form g^t (F. joii) ; cf. Ilal. gioj^t joy, also a gand, jewel, Span./?ya. a gaud. — L. gaudia, neut. pL, afterwards turned into a fenu sing. — L. giudtrt, to rejoice (above). r^oioe. (F. — L.) M. E, rtiohen. — O- F. rtijaii'^ stem of prcs. pt. of rtsj^r (mod. F. rijeuir\ to gladden, rejoice. — L. rt-, again ; F. ujeir, to rejoice, from L. ex, much, very, and gaudert, to rejoice. Oaxige, Qoge, to mensurc the content of a vessel. i.F. — Low L.) Spelt ga^ in Shak. — O. F. gougrr, later jaugrr, ' lo gage,' Cot — O. F. gaugt* (not foundt, old lorra of Jaagr. 'a gage, instrument where* wilh a cask is measured:* Cou Law L» gctugsa (A.n, 1446). Doubtless allied to )ejaU. a tsrge bowl ; tee Gallon. Oaunt. thin, lean. (Scand.) An East* Anglian word, ind therefore presttmaMy .^and. Also spelt gont (167I). Cf. Nofweg. gand, a Ihin stick, a tall and thin man. an overgrown itri^lin^ (^Kucd'^*- 4 I ^, 9U^ gmi, xpj (T. /m> Ct •liipc OB tftht Vr. Cr. H & i«im^ to Mfc ^mmtCT flit. i4$;f. o •I' udlc. I ) 0,F. /Butfte. aa , th« orig. MBtc k -';]«, from lul. gaii£tta. % (f^atut, M mftfple, wbeacc U '- '■■•)- :' 'T ' .' - Ttry ■ .Icjjc '■'-). tl OOin IvM iliaii a inri^- rm$k*u\y. 'I'l. VK«, K 1r«'4aui)', 'I' OMf, «1 nfiaLlL.-Gk). L *Gk. 'r^yvnt, orifia, Mmroe. 1c»K.ntt; ittaeiMU. (VGAN) iailoeimi,ftplaM ihatgravi froai « of y'7»nn*i, 1 wm btva, ftUied to y^««, t ■ro^en, a plant tK«t lacrcmM* vaidlf. (Gk.) From Ok. ff-*. «« fron «^. out ; aad Yf* (m abmV genealogy. (F. - I^ i- Gk.> V m.nmiifsu. • O F stmcipgu. » L /■< A^<a. « Gk. ^cnaAo^fo, ui Ai funUy, p*cdi£Tce (i Tim. L 4.)«Gk. i' birth (i[lic«l lo 7lrM^ ■ ■•■-• *-*- *^ accounL, allied to \vy<.i * 0«net, an uiinuj. ^. ~ ^ J -<-;/£. ' ft kind of wccscU ;' Coi- Uonial; ice Oasiu. HonlAte^ jointed. (L.) Id boluiy. il» gmiiuhim, a little knee, joint in & ; ooable dunio. of gtnu, k knee. BfdUctlon, genuflexion, a bend ^h^fa>ci: ( V — I. ■! F. gcnnftxitm. ^^^Ht^ 'Hcm, > L. gtnUt ^B^V'' *^ bend. wSSaU O«iutivo, OeniUB ; see KT, bom. ; cecJeanet. Itvel; tec 0«QU«. ttl&n. a |4fl.nt. (F-L) O F.^u- » L grntmtm \ na-ined after GentitUt TTtsn km^. abt. ax. 180. lUXe. Oontle ; see Oonus. itry, 0«iitiliie ; «e 0«naa. luflection; see Qenioulate. IIUL kin (L^ L.^tmnj (stein ^vw^t), »oe.<4-Gk. 7^ren,rftcc.+A-b- ^rt, kin. Oil (V CAN > nffenial. kinrlreil (L.) Coined from an'l jrww/, adj. from rc below '^fi-«/ -L. with; -rr, to pioduce. ■■pflm* I : ■■:n pp. of L. tie^tt- J^^ becouiti L>Aae. *■ L. Jt^ner^ adj , ^Kh 4iSr. down ; giner-, stem oi gentu, {K>ve). g«n(lor. to breed, <F.«-L.) ME. itiren.^O. F. c»9^imdrtr,^V.. t'njyH' , to |>rodooe.Mi. iw, in; ^w^/o»r. to , frtMD gmir-, c
```


## [2026-09-06T15:13:03.139Z] TOOL CALL #21: Bash

```json
{
 "command": "ls site/pages/218.jpg 2>/dev/null; pdftoppm -f 218 -l 218 -r 200 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg218 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/",
 "description": "Render PDF page 218"
}
```


### [2026-09-06T15:13:05.463Z] TOOL RESULT

```
site/pages/218.jpg
total 1668
drwx------ 2 sfmqrb sfmqrb   4096 Sep  6 11:13 .
drwx------ 4 sfmqrb sfmqrb   4096 Sep  6 10:51 ..
-rw-rw-r-- 1 sfmqrb sfmqrb    418 Sep  6 11:13 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  92182 Sep  6 10:55 bqt1854.png
-rw-rw-r-- 1 sfmqrb sfmqrb  66580 Sep  6 10:57 bqt2023.png
-rw-rw-r-- 1 sfmqrb sfmqrb   6971 Sep  6 11:03 crop1.png
-rw-rw-r-- 1 sfmqrb sfmqrb   8619 Sep  6 11:03 crop2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   5240 Sep  6 11:03 crop3.png
-rw-rw-r-- 1 sfmqrb sfmqrb  12820 Sep  6 11:05 crop_germ.png
-rw-rw-r-- 1 sfmqrb sfmqrb   3408 Sep  6 11:05 crop_guthjo.png
-rw-rw-r-- 1 sfmqrb sfmqrb   9001 Sep  6 11:05 crop_node12.png
-rw-rw-r-- 1 sfmqrb sfmqrb   5564 Sep  6 11:05 crop_node1.png
-rw-rw-r-- 1 sfmqrb sfmqrb   5286 Sep  6 11:05 crop_varathra.png
-rw-rw-r-- 1 sfmqrb sfmqrb    228 Sep  6 11:06 jscheck.js
-rw-rw-r-- 1 sfmqrb sfmqrb  37376 Sep  6 11:09 mk201.py
-rw-rw-r-- 1 sfmqrb sfmqrb  77132 Sep  6 11:11 mk207.py
-rw-rw-r-- 1 sfmqrb sfmqrb  61121 Sep  6 11:11 mk208.py
-rw-rw-r-- 1 sfmqrb sfmqrb  54688 Sep  6 10:58 pg201.png
-rw-rw-r-- 1 sfmqrb sfmqrb  70083 Sep  6 10:52 pg204.png
-rw-rw-r-- 1 sfmqrb sfmqrb  77858 Sep  6 10:52 pg206.png
-rw-rw-r-- 1 sfmqrb sfmqrb  67371 Sep  6 10:53 pg207.png
-rw-rw-r-- 1 sfmqrb sfmqrb  59146 Sep  6 10:53 pg208.png
-rw-rw-r-- 1 sfmqrb sfmqrb  53054 Sep  6 11:00 pg209.png
-rw-rw-r-- 1 sfmqrb sfmqrb  74515 Sep  6 11:02 pg211.png
-rw-rw-r-- 1 sfmqrb sfmqrb 141781 Sep  6 11:03 pg212hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb  75961 Sep  6 11:02 pg212.png
-rw-rw-r-- 1 sfmqrb sfmqrb  83761 Sep  6 11:03 pg213.png
-rw-rw-r-- 1 sfmqrb sfmqrb  83752 Sep  6 11:01 pg214.png
-rw-rw-r-- 1 sfmqrb sfmqrb 194102 Sep  6 11:05 pg215hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb 117034 Sep  6 10:54 pg215.png
-rw-rw-r-- 1 sfmqrb sfmqrb  82099 Sep  6 11:13 pg218.png
```


## [2026-09-06T15:13:18.451Z] TOOL CALL #22: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg218.png"
}
```


### [2026-09-06T15:13:18.870Z] TOOL RESULT

```

```


## [2026-09-06T15:13:18.867Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-06T15:13:31.705Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && pdftoppm -f 218 -l 218 -r 500 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf pg218hi && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg218hi.png'); print(im.size)\nw,h=im.size\nim.crop((int(w*0.28),int(h*0.30),int(w*0.85),int(h*0.36))).save('c_gacele.png')\nim.crop((int(w*0.28),int(h*0.62),int(w*0.70),int(h*0.68))).save('c_mag.png')\nim.crop((int(w*0.25),int(h*0.55),int(w*0.85),int(h*0.63))).save('c_xzn.png')\n\"",
 "description": "Crop page regions at high res"
}
```


### [2026-09-06T15:13:35.665Z] TOOL RESULT

```
(4250, 5500)
```


## [2026-09-06T15:13:38.082Z] TOOL CALL #24: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/c_gacele.png"
}
```


### [2026-09-06T15:13:38.177Z] TOOL RESULT

```

```


## [2026-09-06T15:13:38.175Z] INPUT

[Image: original 2422x330, displayed at 2000x273. Multiply coordinates by 1.21 to map to original image.]


## [2026-09-06T15:13:45.463Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg218hi.png'); w,h=im.size\nim.crop((int(w*0.20),int(h*0.253),int(w*0.80),int(h*0.293))).save('c1.png')\nim.crop((int(w*0.28),int(h*0.545),int(w*0.80),int(h*0.60))).save('c2.png')\n\"",
 "description": "Recrop"
}
```


### [2026-09-06T15:13:47.485Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T15:13:49.673Z] TOOL CALL #26: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/c1.png"
}
```


### [2026-09-06T15:13:49.738Z] TOOL RESULT

```

```


## [2026-09-06T15:13:49.736Z] INPUT

[Image: original 2550x220, displayed at 2000x173. Multiply coordinates by 1.27 to map to original image.]


## [2026-09-06T15:13:52.915Z] TOOL CALL #27: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/c2.png"
}
```


### [2026-09-06T15:13:52.994Z] TOOL RESULT

```

```


## [2026-09-06T15:13:52.992Z] INPUT

[Image: original 2210x303, displayed at 2000x274. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-06T15:14:23.546Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PHD ganj ===\" && grep -n -i \"ganj\\|gan[jz]\" PHD.txt | head -20; echo \"=== PHD_mackenzie ===\" && grep -n \"ganj\" PHD_mackenzie.txt | head -20; echo \"=== NYB ===\" && grep -n \"ganj\\|gnz\" NYB_vol2_glossary.txt | head -20",
 "description": "Grep Pahlavi dictionaries for ganj"
}
```


### [2026-09-06T15:14:23.618Z] TOOL RESULT

```
=== PHD ganj ===
175:-üg [> | M Ze, N -a] suffix forming agent nouns from present stems. a-gàh [?g's] without rank. āgāh [?k’s | M ?g(h), N <] aware, knowing. ~ih: knowledge. ügahénidan, абваһёп- [A?^syn-ytn!] inform. ügandan, Agan- [’kn-dn' | P ?gnd, N ~] fill, stuff. a-ganj [Аис !] penniless. agar (HT, for А hn | Mgr, N ~] if. agar DEI | М °g°r-] inactive, powerless, имко ~ih : inactivity, impotence. agarénidan, agarén- [?/?/уп-уїп!] render powerless. agarihistan, agarih- [?*4?/y%-stn! | M ?g’ryyh-] become powerless. ag-dén [k-, ?gdyn!] of evil religion, infidel. ~th: heterodoxy, non-Mazdean religion. абепёп [’k(y)nyn' | M (*)*g(y)nyn] together.
378:galēģ [glwk' | N guld] throat. бато [gm | = M, N ~j pace, step, stride; a yard (3 ft.). ~ í dó pay: a pace (s ft.). -рапаб [-k’nk' | M eng, N -gàna] suffix forming numerical adjectives, -fold. бапа [gnd | N ~] stench. gandag [gndk' | (M gng), N —a] foul, stinking. ~th: stench. ģandanāģ [gndn’k' | N gandanā] leek. gandum [Hš < A nth | (M gnwm), N ~] wheat. ganj [gnc | (M gnz), N e treasure, treasury. ~war [-wbl | M -wr, N ~] treasurer. ģan(n)āģ [gr &! | (P gnd?g)] foul, corrupt (v. gandag). ~ ménó$g the Evil Spirit. ~ih: corruption. gar [gl] mountain. -gar [-Al, -gl | M -gr, N ~] suffix forming actor nouns. -gar [-£1| M -g’r, N ~] suffix forming actor nouns. garan [gPn! | M г?л, N girán] heavy, serious, difficult. АҺ; heaviness, weight. garasman [glsm’n' | М ртт?п] = garddman. gard [g/t! | N ~] dust. gardan [gitn! | M grdn, N ~] neck. ģardānāģ [gl h] die (for gaming). gardanidan, gardan- [gl n-ytn! | M grd(y)nydn, N ~] turn (tr.). gardidan, gard- [git-yin' | M grd-, N ~] turn, revolve. ~išn: revolution, turning. garm [gim | M grm, N ~] warm, hot. «„«ih: warmth, heat. garm-ābag [gim'pk! | N ~a] bath-house. garmāģ [glm^ k! | М grmg, N garmá] warmth, heat. g£armóg [gimwk!] warm, ardent, fervent. garmówar(ih) [glmwk wl(yh)] heat ordeal. ģarmsēr [gimsyl | N ~] warm region, lowlands. garódman [glwtmn' = Av. garó dəmana- | M grdm?n] paradise. ~ig [-yk'] (worthy) of paradise. yarranag [g”7k! | M grn’g ?] thunder. yarranidan, yarran- [gl’n-ytn' | (N yurridan)] roar, thunder. ~i$n: roaring. garzag [gick! | N garza] snake, serpent. garzidan, garz- [glc-ytn'] complain; confess. ~i$n: complaint. ~iSnig : complaining. gaw [gw!'] hand (daevic). базу [ТИРА < А twr) | M gw, N ~] ox, bull, cow; astr. Taurus. gawars [PZ < A prg’; g”wls | N ~] sorghum, giant millet.
4059:treasurer gahbed, ganjwar.
4061:treasury ganj.
5419:duz, ganj, 202, убх
5420:dūz-, duz- duzih gozihr duzdih duzidan duzidag ganjwar
=== PHD_mackenzie ===
10700:ganjwar
=== NYB ===
1624:ganj [gne'] treasury 72. 10816 etc. — MPrs gnz (A-H II); Paz. ganž (SGV); NP ganj; MPrth gzn (A-H III) gzng (MHC); Arm. lw. ganj (j = -dz!); Aram. Iw. gnz?, gnzk (Pap., J.-Ar.); Gr. lw. yača. Mayr- hofer, RekMed 13 sqq.
3631:Šēcīkān [Sycyk’n'] belonging to Sc, the name given by the Western Zoroastrians to Lake Urmia: ganj ~ the (royal) treasury on Lake S. 10815. 10912, 1119-14-22, referring to the town Ganjak (g. v.) SE. of this lake, later called Siz (< Šēc), v. Yagut 3, 353sqq.; it had the most prominent fire-temple of the whole Erän- shahr, no doubt long before the Sassanids. V. Cat. 108-110. — Sec through dissimila- tion < *Cēc, an abbreviation of Cécist (g. v.); another abbreviation (through haplology) is Cyst’ = Cist, Zsprm X, 15, whence the form Jis quoted by Yagut (1. e. 354, 1. 1).
4370:xuatäi [hwt’y; MRWHY Ps.] pl. cas. obl. ~-dn (used as cas. rect. pl. 176-10, 9013-14) 1. suzerain in a political sense: ~ u dahyupat 12%. 7223; nē ~-an rād u nē-c an dahyupatän 7271; ~ u dahyupat u sardär u dastavar i den äkäh 1081-2; ~ -ē u pätixsäy-& 513; peš 4 ~-ān u pätixsäyäan 7021; with a gen. of the governed people or country: ~ % Pärsikän 1315; X20nàn ~ 18-29 passim; Eran u Anērān ~ 11919; fradandān + ~ -àn124; ganj i 110?! — of minor rulers: sar-~ properly ‘ruling as the head of a family’, prince, vice-roy, vassal: sar-~-dn 4 Erän 13%; sar-~~-Gn  kustak kustak the vice-roys of the different territories 17>-*-19; in the same sense katak-~ 13, properly ‘the master of the house’. — 2. of the heavenly beings: Ohurmazd ~ Lord O. 12%; Ohurmazd 4 ~ 745 and passim; ~ alone: the Lord Paramount 10411; ~ u pātixšāi of Srosh 86%; [MRWHY] God in the Jewish-Christian sense 1289.19.20, — Prth inser. hwtwy (Prs always MRWHY); MPrth zwd’wn, awd'y; MPrs zwd'y, cwd^wy (A-H I), zwdy’(h), pl. zwdy’h’n (S, A-H II); Paz. x"adàe, x"uaddič; NP xuda ‘God; master, owner’. Meillet, MSL 17, 1911, 109 sqq.; Bthl, MirM ITT, 1920, v. Index; Junker, WuS XII, 1929, 145— 147; Schaeder, UJ XV, 570 n.; Eilers, AOi 24, 1956, 185. — V. also dérang- xatar.
5621:gwnd: gund gwng: gonak gwrd: gurtvar gyn: jan gy'nbr: janvar gyh, -n: géhan gzn(g): ganj
5964:gnz: ganj
```


## [2026-09-06T15:14:25.679Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN ganj ===\" && grep -n \"ganǰ\\|gang\\|ganj\" HRN.txt | head -20; echo \"=== HUB ===\" && grep -n \"ganǰ\\|ganj\\|gang\" HUB.txt | head -20; echo \"=== CHEUNG ===\" && grep -n \"ganǰ\\|ganj\\|gunǰ\" CHEUNG.txt | head -20",
 "description": "Grep Horn, Hübschmann, Cheung"
}
```


### [2026-09-06T15:14:25.789Z] TOOL RESULT

```
=== HRN ganj ===
35:von Land zu Land unterschiedlich sein. Öffentlich zugängliche Bücher sind unser Tor zur Vergangenheit und stellen ein geschichtliches, kulturelles
48:über maschinelle Übersetzung, optische Zeichenerkennung oder andere Bereiche durchführen, in denen der Zugang zu Text in großen Mengen
569:schnur; schon im Pehlevl verloren gegangen^). Also
673:röS'äsan 'Sonnenaufgang' (17); vergl. Salemann, Mel.
810:entgangen.- 11 -
881:Übergang von der aw. skr. Bedeutung 'dieser zu jener'
1105:^) Bedeutungsübergang etwa: finster — höllisch ~ zornig.- 19 --
1113:minj. yiz selbst ist sonst im Np. verloren gegangen.
1666:und (irregulär) pati zusammengefallen, ein Vorgang,
2691:270. pär 'das vergangene Jahr', pärsal^ parm.
2692:skr. vergl. panit 'im vergangenen Jahre' ; arm. heru
2693:Vergangenes Jahr' (H. No. 167).
3011:und d (bei letzterem häufige Fälle des Übergangs in h)
3149:begangenen Irrtum zu berichtigen, dass ich auch Darmesteter die
3318:351. pfrär, pirar[sal *das vor vergangene Jahr.
3702:Der Übergang von der Bedeutung 'ziehen* zu 'trinken
4365:Der Übergang von s zu s ist erst neupersisch (an aw.
4969:der Bedeutung *keck, frech' ausgegangen ^).
5240:583. {i)dös 'die letzte, vergangene Nacht'.
6436:Über den Bedeutungsübergang spricht de Lagard e,
=== HUB ===
573:unsterblich, unverganglich' BE. 4, 45, zd. anaoSa-
574:unsterblich', arm. LW. anusak unverganglich, unsterb-
1073:griflfsubergang : Kleid— Hiille — Vorwand macht doch
1372:auch ins Afgh. {pa§Tmcin Veuig') iibergegangen ist. Vgl.
1522:351. Np. pirdr *das vorvergangene Jahr = ap. p{a)ruviya-
1549:359. Np. paig Tussganger = syr. N3^£> Noldeke,
1553:Anm. 14, arm. LW. payilc, skr. padika- Tussganger ,
2216:den Bedeutungsiibergang : ziehen : durchziehen : nahen,
2323:raju *Reihe'). Der Ubergang von 'Schlachtreihe' zu
2486:konnten. Der Ubergang von ap. ri m np. rd ist laut-
3213:*Durchgang'). Auch unsicher.
3568:*Untergang' (von Sonne und Mond) Min. cap. 49, 27,
3951:Boim Uebergang der idg. zur arischen Grundsprache
3997:w d y, falls der Uebergang der Medien (der arischen Medien
4008:Sprachen unterscheidet, ist der (theilweise) Uebergang von
4010:g^, g^h in d, ein Uebergang, der dem Zend, den Pamir-
4028:S. unten § 100 und 110. Dieser Uebergang ist also das
4052:vorgegangen. Das alteste Pehlevi unterschied sich in laut-
4137:Das Neupersische ist die Schrift- und Umgangssprache
4207:lich*, arm. anvsak unverganglich' ; dazu N. pr. Nosirevan
=== CHEUNG ===
```


## [2026-09-06T15:14:39.818Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN Schatz ===\" && grep -n \"Schatz\" HRN.txt | head -20; echo \"=== HUB Schatz ===\" && grep -n \"Schatz\" HUB.txt | head -20; echo \"=== CHEUNG gan ===\" && grep -n \"gan[jzǰ]\\|to fit\\|\\*ganǰ\" CHEUNG.txt | head -20",
 "description": "Grep Horn/Hübschmann for Schatz, Cheung"
}
```


### [2026-09-06T15:14:39.890Z] TOOL RESULT

```
=== HRN Schatz ===
=== HUB Schatz ===
3724:Zahlung, Rechnung, Schatzung', davon hamarim 'zahle,
8272:(Atharva Veda), gr. ogv'Qa ; — ganj *Schatz' (5. Jhd.) = np.
8274:syr. Nill *Schatz', dazu X*1DT:i --= hebr. "\2u *Schatzmeister'
8820:Sessel*; ganj 'Schatz* = np. ganj\ goin 'Farbe*, ^rat; 'Pfand*
=== CHEUNG gan ===
13341:*NEIR: (+ *4-) Oss. І. areexsyn/araxst, D. arzexsun/araxst ‘to fit, match; to deal, cope 
21216:*sač! ‘to fit, be suitable, be able, be in command of; to prepare’ 
21648:‘to fit’ (in order to suit Khot. sam-, Oss. I. somy, D. somi), deriving notably Skt. sam 
28140:Verknüpfung ist semantisch nicht ganz befriedigend.". On the other hand, BSogd. 
56533:to fit, be suitable
```


## [2026-09-06T15:14:41.447Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== FVQ pages 122 & 251 ===\"; python3 - <<'EOF'\np=open('FVQ_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor printed in (122,251):\n    leaf=printed+17\n    print('==== printed',printed,'leaf',leaf,'====')\n    print(' '.join(p[leaf].split())[:2500])\nEOF",
 "description": "Print Jeffery FVQ pages 122 and 251"
}
```


### [2026-09-06T15:14:43.098Z] TOOL RESULT

```
=== FVQ pages 122 & 251 ===
==== printed 122 leaf 139 ====
122 FOREIGN VOCABULARY OF THE QUR*AN as is indicated by the common Tigre word rh*flH*]h used for a popular kind of bread. It was probably an early borrowing into Arabic, for the root has become well naturalized and many forms have been built from it. (Khardal). xxi, 48 ; xxxi, 15. A mustard seed. Both passages are reminiscent of the coy KQKKOV of Matt, xvii, 20, etc. The Muslim authorities take it as an Arabic word, though they are in some doubt as to whether it should be <j$>- or (j>*~. Fracnkel, Fremdw, 141, has shown, however, that the word is a borrowing from Aram. 7TU1 ; Syr. U?;**. The probabilities are in favour of its being from the Syr. U?r*, which as a matter of fact translates crlva.TTi in the Peshitta text of Matt, xvii, 20, etc., and occurs also in Christian Palestinian. 1 The borrowing will have been early for the word is used in the old poems, e.g. Divan Hudhail, xcvii, 11. * "{'" 4 1^>- (Khazana). vi, 50 ; xi, 33 ; xii, 55 ; xv, 21 ; xvii, 102 ; xxxviii, 8 ; lii, 37 ; Ixiii, 7. Treasury, storehouse. *" ""i ** \ The verb /Y}>- does not occur in the Qur'an, but besides < 1 J>- ( which occurs, however, only in the plu. form j \ j>-), we find a form <W* AwV ! ""' **'''' JjLi- " one who lays in store " in xv, 22 ; and A> j>- keepers in xxxix, 71, 73 ; xl, 52 ; Ixvii, 8. It is fairly obvious that Oj*~ ^ s a denominative verb, and the word has been recognized by many Western scholars as a foreign borrowing. 2 Its origin, however, is a little more difficult to determine. Hoffmann, 1 Schultheas, Lex, 69. 2 Fraenkei in e#r. Aasy,m, 81; Vollers, ZDMG, 1, 640 ; Horovitz, Paradies, 6 n.
==== printed 251 leaf 268 ====
FOREIGN VOCABULARY OP THE QUR'AN 251 3 (Kanz). xi, 15 ; xviii, 81 ; xxv, 9 ; xxvi, 58 ; xxviii, 76. Treasure. The denominative verb Jlj to treasure up is also found in ix, 34, 35. Some of the Muslim authorities take it as genuine Arabic and derive it frdrn jj , but it was well known to the early philologers that it was a foreign word and it is noted as such by al-Jawallqi, Mu'arrab, 133 ; ath-Tha'alibi, Fiqh, 317 ; al-Khafaji, 170, all of whom give it as Persian *dj , meaning, of course, *clj , which BQ, 797, defines as Jj^ j jjj j} $ ( \$J*j) j j. That it was originally Iranian is certain. Paz. ganz ; Phlv. (2 y gan] means treasury , l and the word has been widely borrowed, cf. Skt. *rar ; Arm. ^t,^ 2 ; Baluchi, gan$ ; Gk. ydfyt ; Sogd. ynz> and in the Semitic family, cf. "J /QH ^33 of Esth. iii, 9 ; Aram. KT33, nP33, and KT3 3 ; Syr. ll^t, and Mand. XT3 n 3, 4 all meaning treasury. The direct borrowing of all these from Middle Persian seems clear from the fact that the Phlv. 3l>g y ganjdpar 5 for the treasurer is also common to them all, cf. Skt. l^sf^ \ Arm. /^U^/<W/YJ (Gk. yab0i/Aa) ; Heb. 13T3; Syr. Ir^kv lr^V*M> an d Aram. K"1DT3 (cf . Telegdi in J^[ , ccxxvi (1935), p. 237 ; Hcnning in BSOS, ix, 83). It is most probable that the word came direct from Middle Persian into Arabic, 6 though j for (2 might point to Aram, influence on the word. The word must have been borrowed long before Muhammad's time, though it occurs but rarely in the old poetry. 1 West, Glossary, 274; PPGl, 112; Nyberg, Glossar, 77; Herzfeld, Paikuli, Glossary, 159. Lagarde, Arm. Stud, 453, thinks that it is an old Median word which passed later into Iranian and thence to India ; cf. also his GA t 27. 2 Hubschmann, Arm. Gramm, i, 126. 3 Levy, Worterbuch, i, 316, however, thinks that HP33 and K73 arc from T33 to hide. * Noldeke, Mand. Gramm, 51. 6 PPGl, 119 ; Frahang, Glossary, 79. It is the Pers. j^se^l and Paz. ganzubar (Shikand, Glossary, 245). Compare also Phlv. ganfenak barn or storehouse (Sayast, Glossary, 161). 8 Vollers, ZDMG, 1, 613, 647.
```


## [2026-09-06T15:14:56.010Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== FVQ p123 ===\"; python3 -c \"\np=open('FVQ_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(' '.join(p[140].split())[:2200])\n\"; echo; echo \"=== HUB context 8265-8285 ===\"; sed -n '8262,8290p' HUB.txt; echo \"=== HUB 8815-8825 ===\"; sed -n '8812,8826p' HUB.txt",
 "description": "FVQ p123 and Hübschmann context"
}
```


### [2026-09-06T15:14:57.830Z] TOOL RESULT

```
=== FVQ p123 ===
FOREIGN VOCABULARY OF THE QUR 5 AN 123 ZDMG, xxxii, 760, 1 suggested that we should find its origin in the Pers. 3 . This ij$ which BQ defines as & (^y ) jj AxlJ &} clc*J -P k cognate with Skt. *I^ (~?Sfa[) a treasury or jewel room, 2 and has been borrowed through the Aram. KT33 ; Syr. 1 C*' IPM into Arabic as JO . It seems hardly likely that by another line of borrowing, through say Heb. D^T33 3 or Mand. &UKTK2, 4 it has come to form the Ar. AM "*>-. Barth, Etymol. Stud, 51, makes the happier suggestion that it may be connected with the form that is behind the Heb. ]0fl treasure. - (Khatia). To do wrong, sin. Several verbal and nominal forms from this root occur in the 1^ ^ * Qur'an, e.g. l.ia>- by mistake (iv, 94) ; LLi>-l to be in error, to sin (ii, * ^ ** 286 ; xxxiii, 5) ; ,^-kv>- (xxviii, 7 ; Ixix, 37) ; LJa>- sin, error (xvii, 33) ; 4~Ja^, plu. \>\b>* ww, error (ii, 55, 75 ; iv, 112, etc.) ; and AL^U habitual sinfuhiess (Ixix, 9 ; xcvi, 16). The primitive meaning of the Semitic root was apparently to miss 5 as in Heb. K3n (cf. Prov. viii, 36, 127S3 OQIl ''KBn " he who misses me wrongs himself"), and in the Eth. *1TJ| to fail to find. The Hiphil form in Heb. is used of markmanship, and XhlD 1 "! in S. Arabian seems to have the same meaning, as we may judge from two inscriptions given by Levy in ZDMG, xxiv, 195, 199 (cf. also Rossini, Glossarium, 155). It was from this sense of missing the mark that there developed the idea of to sin, which is the commonest use 1 Cf. also his Mdrtyrer, 250. 2 It is probably a loan-word in Skt. Lagarcle, GA, 27, and Arm. Stud, 453, thinks it is an old Median word. 3 Cf. Esth, iii, '.) ; iv. 7, "J^On TO. 4 Fracnkel, Beitr. Assy, iii, 181, takes it to bo from Aram. * But see Zimmern, Akkad. Fremdw, 11.

=== HUB context 8265-8285 ===
sipanj, syr. aspizkana, mand. spinza aus *aspinj (oben p. 73).
Das Armenische hat also z im Anlaut sowie inlaut. nach
Vokalen und r, dagegen / nach «.
Hochst auifallig sind nun vier Worter, in denen per-
sischem nf (d. i. ndz) armenisches nj (d. i. ndz) gegeniiber-
steht: Ganjak 'Stadt in Atrpatakan (Faust us, Sebeos) =
^QY^.Ganjak, Ganja, gr. Totfaxa, lat. G^a^a, (?an^ag'a_,Plinius,
Gazaca Ammian, ar ab. /an-s^a, jaznaq u. s. w. Tab. 100; —— 232 —
bfinj^) 'Reis' (Mos. Geogr. ed. Soukry 43, 6 v. u., Galen,
Yaismav.) = np. birinjf, gurinj^), afgh. vrize, skr. vrihi^
(Atharva Veda), gr. ogv'Qa ; — ganj *Schatz' (5. Jhd.) = np.
ganj, phi. ganj Gl. and Ind. 274, skr. LW. ganja-, gr. yd^a,
syr. Nill *Schatz', dazu X*1DT:i --= hebr. "\2u *Schatzmeister'
= arm. ganjavor^ np. ganjvar ; — plinj *Kupfer, Erz' (5. Jhd.)
=-= np. birinjj kurd. pirinjok (oben p. 27 und § 65).
Hatten diese W5rter urspr. nz, das, da es dem Arme-
nisehen und Persischen von Haus aus fremd ist, dort zu
nj (= «(fo), hier zu nj (= ndz) werden musste? Dann
sind diese Worter nicht persischen, sondern (wie Ganjak
vermuthen lasst) medischen Ursprungs. Vgl. die medisehen
Namen Tov^aQfjta^ ^Aydvl,apa, 'AXivl^a bei Ptolomaeus.
Kapitel 23: ap. S.
Ap. s = 1) idg. s nach ?, U, ai, au, r, x, f (ap. fs =
idg. ps und pk^),
2) idg. k%
3) ap. st auch = idg. k%
4) ap. sy auch = idg. k^y^
5) ap. sn auch = idg. g^n, g^hn und k^n.
§ 124. Ap. s aus s nach ?, u, a% au, r = np. s:
=== HUB 8815-8825 ===
'Hefenballen', zd. gunda-; gos 'Ohr ^= ap. gausa-; gun
'Farbe* == zd. gaona-; guh 'Sehmutz, Koth* = zd. guda-;
gohar 'Ursprung H. 948, oben p. 96; ges^ gesU 'Locken\
zd. ga^sa-; gehan *Welt* = zd. gaedanqm (gen.pl.); angust
'Finger, Zehe' = zd. angiista-; angist 'Kohle', vgl. skr. an-
gdra- ; bang 'Bilsenkraut* — skr. bhanga- ; 7'ang 'Farbe' =
skr. rafiga-.
Im Armenischen stelit hier ebenfalls g: gah 'Thron,
Sessel*; ganj 'Schatz* = np. ganj\ goin 'Farbe*, ^rat; 'Pfand*
u. s. w. ; erang 'Farbe' = np. rang; zangapan *Beinschiene',
zd. zanga- 'Knochel'.
Das anlautende y von yund 'Menge, Sehaar H. 805,
oben p. 83 kann ich nicht erklaren.— 247
§ 139. Ap. g nach Vokalen und r = y bleibt im
Np. als }': mury 'Vogel' ^= zd. mereya-; mary 'Wiese'
```


## [2026-09-06T15:14:58.129Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== CHEUNG gunj ===\"; grep -n -i \"gunj\\|gunǰ\\|ganǰ\\|\\bganz\\b\" CHEUNG.txt | head -20; echo \"=== KLN_1966 magazine ===\"; grep -n \"magazine, n\\|^magazine\" KLN_1966.txt | head -5; echo \"=== KLN_1966 genizah ===\"; grep -n \"genizah\" KLN_1966.txt | head -5",
 "description": "Cheung and Klein 1966 lookups"
}
```


### [2026-09-06T15:14:58.223Z] TOOL RESULT

```
=== CHEUNG gunj ===
28080:*NWIR: NP gunjidan/gunj- ‘to be contained’, NP gunj ‘volume’, Khuns. buydä 
28140:Verknüpfung ist semantisch nicht ganz befriedigend.". On the other hand, BSogd. 
41052:gunj, 434 
41053:gunjidan/gunj-, 434 
=== KLN_1966 magazine ===
22513:magazine,  n.  —  MF.  magazin  (F.  magasin),  lr. OF.  magazin,  fr.  It.  magazzino,  fr.  Arab,  ma- khdzin,  pi.  of  makhzdn,  ‘storehouse’,  fr.  khdzana, ‘he  stored  up’,  for  the  etymology  of  which  see Paul  de  Lagarde,  Gesammelte  Abhandlungen, Leipzig,  1866,  p.  25.  Cp.  alhacena,  almacen. Derivatives :  magazine,  tr.  v.,  magazin-er,  n. magdalen,  also  magdalene,  n.,  a  reformed  pros¬ titute.  —  Named  after  Mary  Magdalene,  men¬ tioned  in  Luke  8:2  (often  identified  with  the penitent  woman  in  Luke  7 : 37-50).  See  Magda¬ lene.
=== KLN_1966 genizah ===
15885:gazette,  n.,  newspaper.  —  F.,  fr.  It.  gazzetta,  of s.m.,  fr.  gazzetta,  name  of  the  smallest  Venetian coin,  said  to  have  been  paid  for  the  perusal  of  the manuscript  newspaper  issued  by  the  Venetian Government  once  a  month.  It.  gazzetta,  ‘coin’, is  prob.  a  dimin.  formed  fr.  L.  gaza,  ‘treasure’, fr.  Gk.  y <*£<x,  which  is  of  Persian  origin.  See genizah  and  cp.  next  word.
15974:genizah,  n.,  storeroom  of  a  synagogue  in  which Hebrew  books  are  preserved.  —  Mishnaic  Heb. glnizdh,  ‘hiding  place’,  fr.  ganaz,  ‘he  saved;  he hid’,  rel.  to  Biblical  Heb. glnaztm  (pi.),  ‘treasury’ (in  the  Bible  the  word  occurs  only  in  the  construct state  pi.  ginzd);  borrowed  fr.  Pers.  gan],  ‘treas¬ ure’,  whence  also  Aram.  genaz,  ‘he  saved’, ginzd,  gazzd,  ‘treasure’,  Arab,  jdnaza,  ‘he  cov¬ ered  up’.  Cp.  Arm.  gan],  Gk.  y&yx  (whence  L. gaza),  and  Hung,  kincs,  ‘treasure’,  which  are also  Persian  loan  words.  Cp.  also  gunge.  Cp. also  gazette  and  the  first  element  in  Gaspar, Jasper.
16876:Derivatives:  gun,  intr.  v.,  gunnage  (q.v.),  gunn¬ er,  n.,  gunn-ery,  n.,  gunn-ing,  n. gunge,  n.,  a  storehouse;  a  market  {India).  • Hind,  ganj,  fr.  OI.  ganjah,  ‘treasury’,  which  is an  Iranian  loan  word.  Cp.  Pers.  ganj,  ‘treasure  , and  see  genizah. gunja,  n.  —  A  var.  of  ganja. gunnage,  n.,  number  of  guns  carried  by  a  war¬ ship.  —  A  hybrid  coined  fr.  gun  and  -age,  a suff.  of  Latin  origin.
20185:jasper,  n.,  an  opaque  variety  of  quartz.  —  ME. iaspre,  fr.  OF.  jaspe,  jaspre,  fr.  L.  iaspis,  fr.  Gk. lacm ?,  ‘jasper’,  which  is  of  Sent,  origin.  Cp. Heb.  yashephih,  Akkad,  yashupu,  ashpu,  ‘jasper’. Jasper,  masc.  PN.  —  A  name  of  Persian  origin. Jas-per  lit.  means  ‘treasure  holder’.  The  first element  of  this  compound  name  is  traceable  to Pers .ganj,  ‘treasure’.  See  genizah  and  cp.  Gaspar. Jataka,  n.,  a  birth  story  of  Gautama  Buddha.  — OI.  jatakah,  ‘begotten  by;  birth’,  fr.  jatah, bom;  son',  which  is  cogn.  with  L .gnatus,  ‘bom’, Gk,  -yviQToi;  (in  compounds),  ‘bom’,  fr.  I.-E. base  gen-,  ‘to  beget,  bear,  bring  forth,  produce’, whence  also  L.  gignere,  ‘to  beget,  bear,  bring forth’,  genus,  ‘birth,  descent,  origin’.  See  genus and  cp.  words  there  referred  to.
```


## [2026-09-06T15:15:15.711Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '28060,28150p' CHEUNG.txt",
 "description": "Read Cheung entry mentioning gunjidan"
}
```


### [2026-09-06T15:15:15.803Z] TOOL RESULT

```
575 

9 The formation is probably unrelated to *Hnar ‘to be able, skilled’, although it is 


morphologically unclear. = LIV: — | Pok.: 
*REFERENCES: Henning 1954: 174 f.; Paul 1998: 316a f. 


*uiaé ‘to contain’ 
*MIDDLE PERSIAN: ВМР wnc- /winj-/, (раѕѕ.) wncyh- /winjih-/ ‘to be contained’ 


c DMMPP: 95 
Pres.: IND. 3р1. ВМР wnend /winjand/; Pass.: pres. IND. 3sg. BMP wncyhyt / winjthed/ 


*KHOTANESE: ? LKh. bijs- ‘to assemble, gather [intr.]’ (cited in DKS: 280 f.) 
= SGS: — 

*NWIR: NP gunjidan/gunj- ‘to be contained’, NP gunj ‘volume’, Khuns. buydä 
‘closet’ 

*NEIR: Sh. wiz-/wizd, Rosh. wiz-/wizd, Sariq. wez-/wezd, Yzgh. waZ-/wayd, M. 
wüj-/wüyd-, Wa. wic-/wict ‘to be contained in, find room in, go into’ 

*SANSKRIT: vyac ‘to contain, embrace, encompass’ (RV+) = EWAia П: 590 

9 This Пг. root has no certain IE correspondences. The comparison to Lat. vincire 
‘to bind, to wrap up’ has been declined by Emout — Meillet: 1066 on semantic 
grounds: "les sens des deux groupes n’ont rien de commun". 


*PIE — — LIV: 696 | Pok.: 1130 
*REFERENCES: Zarubin 1927: 176; Henning 1945: 469, fn. 3; EVS: 95b f.; WIM I: 345; DKS 280b f., 
392b. f.; Werba 1997: 399; Steblin-Kamenskij 1999: 388 


*uiaH ‘to cover, wrap’ 

*PARTHIAN: (+ *pari-) prwy- ‘to encompass’ = Ghilain: - | DMMPP: 281b 

Pres.: IND. 3sg. prwyyd; Partic.: perf. pass. prwyd 

*SOGDIAN: (+ *pati-) BSogd. ptw’y (caus. ?) ‘to wind, roll’ || (+ *pari-) BSogd. 
prw’’y ‘to wrap up’. Ф On semantic grounds, these Sogd. forms cannot be connected 
to Skt. o- ‘to weave’ (related to Sh. pidytic (m.), (Baj.) pedyoc, Sariq. padec ‘thread’ 
?), as suggested by Bailey (Gs Henning: 29 f.) and cautiously accepted by 


Mayrhofer (EWAia I: 275). 
(+ *pati-) Impf.: IND. 3sg. BSogd. pt’yw’y; Inf.: pret. BSogd. ptwy’t, BSogd. ptwy’ty || (+ *pari-) Pres.: 
IND. 3sg. BSogd. prw’’yt 


*urad 435 


*NEIR: Yzgh. woyeg ‘blanket, counterpane' || (+ *upa-) Sariq. bawey-/bawid, Yzgh. 
baway-/bawad ‘to cover, veil’, Rosh. bawin ‘covering, closing’, Sariq. bawéin 
‘blanket, body covering’ || (+ *uz-) Sh. zarwin-t, Rosh. zarwin-/zarwid, Bart. 
zarwi(y)-/zarwid, Orosh. zarway-/zarwid, Sang, zarwey(n)-/zarwid, Yzgh. 
zorway-/zorwayd ‘to roll, wind, reel, wrap up’ (with -r- from the *pari-formations ?), 
Wa. z(o)way- (zaw(a)y-) / z(o)wot- (zway-) ‘to wind, wrap, roll up’ || (+ *pati-) ? Sh. 
(Baj.) pidwin, Rosh. padwin 'guard(ing), keeping, custody’ || (+ *pari-) Sariq. 
parwey-/parwid ‘to cover, veil’, Sh. parwin ‘cover, wrapping’, Sariq. parwein 
*horse-clothing'. ó Oss. I. byjyn/byd, D. bijun/bid ‘to wind, braid (hair)’ is not of 
Iranian origin, pace Abaev 1958: 277 (and Steblin-Kamenskij 1999: 441), on 
account of initial b-, which can only reflect older *8 < Pir *b or *up-. The Oss. 
forms are rather borrowings from Slavic, cf. OCS po-viti (NB: Sl. v = [ß]). The 
Slavic forms are close to the Oss. forms, not only formally, but especially 
semantically. It is striking that Oss. byjyn is translated as Russ. vit’ ‘to wind, braid; 
[also] to build a nest’ by Abaev. 

*SANSKRIT: ууа ‘to wrap, to veil, to envelop’ (RV+) || (+ *upa-) upavya ‘to enclose, 
enfold, wrap’ = EWAia II: 592 

9 It remains doubtful whether the Iranian and Skt. forms above are connected to IE 
*ujeH;. ‘to braid, wind’ (Lat. viére ‘to bind, to plait’; Lith. vun ‘to twist’; OCS 
po-viti ‘to wrap, to bind’), on account of the meaning. Cf. EWAia, Le: "Die 
Verknüpfung ist semantisch nicht ganz befriedigend.". On the other hand, BSogd. 
wyt(’k) ‘cord’, Yghn. wita (or vita) ‘cord’ and especially Kurd. ba ‘braiding, 
twisting, rolling up’ (ba dan ‘to braid, twist, roll up’), Zaz. viya (Ё) ‘a piece of 
thread, string, etc.’ do certainly continue IE *ujeH)- ( *ueiH;-). 

«PIE? > LIV: 695 f. | Pok.: 1120 f. 


*REFERENCES: EVS: 21b, 60, 109a, 117b; Werba 1997: 411 f.; Paul 1998: 317b; Steblin-Kamenskij 1999: 
441
```


## [2026-09-06T15:16:20.533Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== LKT gazelle/magazin ===\"; grep -n -i \"gazelle\\|magazin\\|Gazette\\|kanz\\|ganǧ\\|ganj\" LKT.txt | head -30",
 "description": "Grep Lokotsch"
}
```


### [2026-09-06T15:16:20.590Z] TOOL RESULT

```
=== LKT gazelle/magazin ===
706:'Lager,  Magazin,  Vorhalle'  [Pijn  35b]; hieraus  angloind.  bankshall  'Warenhaus, Büro  eines  Halenmeisters'.  [Hobson- Jobson  61/62.
1389:'Laden';  \k. ebenso  dükjan;  hieraus  rum. dughiana  'Kramladen';  bulg.  dukan 'Laden',  djukjan  'Werkstätte',  serb.  du- can  'Laden,  Werkstatt',  doganja  'Kauf- mannsladen", russ.  duhan  'Schenke, Bude',  duhanscik.  —  Im  westlichen Afrika  und  Spanien  sprach  man  mit Imäla:  dokkin;  hieiaus  mit  ar.  Art.  sp. adoquin  'viereckige  Steinplatte',  meist als  Pflaster  verwandt,  fig.  'Tölpel'  [zu der  Bedeutungswandlung  vgl.  frz.  tete carrie].  [Gorjajew  99.  Bern  SlEtWb 237.    DE  46/47.
1546:'Magazin,  Lager,  Wirtshaus'  [seit  Golius bereits  auf  gr.  iravboxeiov  zurückgeführt; besser  irdvboxoq] ;  hieraus  rum.  fundac 'Heuschober',  it.  fondaco.  venez.  (alt) fonteco,  (modern)  fontego,  afrz.  fondique, sp.  alhöndiga,  fundago,  pg.  alhondega, alfandega 'Zollhaus' ;  siz. f 'Wirts- haus niederster  Sorte',  wo  sicii  die  Fuhr- leute usw.  mit  ihren  Pferden  und  Maul- tieren erholen,  funnacaru  'Wirt'.  Rück- gebildet ist  sp.  fo7ida  'Hotel,  Wirtshaus'. [DE  139  u.  270.  Eguilaz  192.  Devic DEt  121.    ML  .3424.
1719:'Gazelle,  Antilope  dorcas  Lieht.';  die  nord- afrikanische Aussprache  hat  Imäla,  also gazel;  hieraus  sp.  gacela,  pg.  gazella, frz.  gazelle,  it.  gazzella,  rum.  gazelä; engl,  gazelle,  ndl.  gazel,  dtsch.  Gazelle, siihviQä.  gasell;  luss.  gazel'.    [DE  5!71.
2051:Fem.  zu  ahu  'ar  'schwarzäugig'  besonders von  einer  Gazelle,  einem  Jünglinge  oder einer  Jungfrau  gesagt;  dazu  plur.  hür. Dieses  Wort  betrachteten  die  Perser  [und gelegentlich  auch  schon  die  Araber,  s. BSGW  Leipzig  ph.-hist.  Kl.  1881 .  XXXIII, 31]  als  sglr.  und  fügten  ein  *  der  Ein- heit an :  hüri ;  darunter  versteht  man die  Paradiesesjungfrauen,  die  man  nach Muhammads  Verheißung  im  Paradiese vorfinden  soll ;  hieraus  zur  Bezeichnung
2514:1059.  Ar.  kanz:
2515:'Schatz'  [aus  pers.^r««^  ZDMG  L,  647/648] und  kanzija  'dass.' ;  liieraus  sp.  alcancla 'Sparbüchse',  Vb.  alcanzar  'erreichen', siz.  accanzari  'erlangen,  nach  und  nach erreichen',  it.  scansia  'Regal',  dtsch. Schanze.  —  Das  pers.  Grundwort  wurde
2516:schon  früh  lat.  gaza  'Schatz';  hieraus it.  gazzetta,  ursprünglich  eine  kleine Münze,  die  man  für  ein  Zeitungsblatt hingab,  dann  'Zeitung'[die  ersten  geschrie- benen Zeitungen  erschienen  im  Jahre 1560  in  Venedig],  frz.  gazette,  sp.  gaceta, pg.gazeta  'Zeitung'  [Körting  4117  a  leitet dagegen  vom  Demin.  von  gazza  'Elster' ab,  weil  die  Zeitungsbiätter  so  schwatz- haft seien  wie  dieser  Vogel;  noch  merk- würdiger ist  die  hier  nur  als  Kuriosum angeführte  Etymologie  in  Gonstancio Dicc  587  b  aus  dtsch.  Ganz-zeit.'];  engh gazette,  ndl.  gazet;  russ.  bulg.  poln.  ga- zeta  'Zeitung'.  —  Aus  dem  pers.  Grund- wort und  pers.  Suffix  -bär  'Träger'  [Horn NpEt  S.  36,  Nr.  158]  ergibt  sich  *gazbär 'Schatzträger,  -meister'  und  hieraus  Kas- par, der  König  aus  dem  Morgenlande; da  er  komisch  wirkte,  entstand  die  Figur des  Kasperle.  Dagegen  geht  gauner- deutsch kaspern  'betrügen'  auf  hehr. käza^  'lügen'  zurück.
3162:1362.  Ar.  mahzan: 'Warenniedei  läge,  Scheune,  Zeughaus', plr.  mahäzin;  hieraus  it.  tnagazzino, sai'd.  magasinu,  camasinu  [mit  Meta- thesis],  SIZ.  magasenu,  maasemi,  mala- senu,  malase,  frz.  ntagasin,  sp.  magacSn, almagacen,  alniacen,  pg.  almazem,  ar- mazem,  almacen,  rum.  magaza,  magazin; dtsch.  Magazin,  ndl.  magazijn,  engl,  ma- gazi)ie ;  russ.  magazyn,  (dial )  gamazeja [Metathesis  wie  im  Sard. !],  klruss.  ma- gazyn, kamazej,  bulg.  serb.  magaza, magazin  'Warenniederlage,  Zeughaus'. [Lasii.io  8.  DE  147.  Eguilaz  205.  ML 5447  (wo  als  Grundwort  mayzen  'Scheune' gegeben  wird!).  Gorjajew  199.  Mikl SIElWb  180.
3376:1461a.  Ar.  mimbar: Aussprache  für  ursprüngliches  minbar [von  ar.  nabara  'erheben';  minbar  aXso ursprünglich  die  Erhebung,  auf  die  man sieh  setzt  oder  stellt,  Untergestell,  s. BECKER  in  Orient.  Studien  (Festschrift für  Nöldeke)  I,  S.  338;  letzten  Endes aus  dem  Äthiop.,  s.  Nöldeke,  Neue  Bei- träge, S.  49]  'Kanzel',  und  zwar  im Gegensatz  zur  Predigtkanzel  kurst  die- jenige Kanzel  in  der  Moschee,  auf  der an  jedem  Freitag  die  Jiutba,  d.  h.  das Gebet  für  den  obersten  Herrscher  der Gläubigen,  gehalten  wird.  Hieraus  jüd.- dtsch.  Almemor,  die  inmitten  der  Syna- goge betindliche,  zum  Verlesen  der Tliora  bestimmte  Erhöhung  [die  in  jüd. Schriften  als  bema  oder  mifdal  bezeich- net wird],  vgl.  z.  B.  in  Heinrich  Heines , Prinzessin  Sabbath":  'Stolz  aufflackern auch  die  Kerzen  /  Auf  der  Brüstung des  Almemors'.
5285:A;«^«?'«  1002 ka'fihn  1002 ÄrrtÄA-rt/ur  1003 kahwa  1005 k'i^  1006 A;«*/*  1007.  1173 kail  1 174  a kä^iininnkäm  1010 katsänia  1011 kaitus  273 Ä-«)i;ö(i  lol3 käkang  1016 ter«  1021 kala'a  1036 kalaba  1376 kalada  1505 fcatofa  1022 Ä-aZ«w  1023 Ä:ffZ6  1025 A-a/ö  1026 teZ»  1029 k^/ö  1030 Ä;fl?«»iffl  1032 A;a?tö'  1036 A-aWfli  1037 A;rt>Hä  1157 käma  1010.  1999 if«H!7  1044 kammün  1046 kand(l)  10.52 kandara  1051 kandil  1053 kantara  1057.  1506 kanz(lja)  1059 Ä;ar«  1181.  1507 A;ßm  1071.  1072 A-ar'^a  689 kaya'a  1250 karam  1083 karawän  1086 karawijä'  1087 kafija  1094 karlwija  1095 A;ar>«  1096 Ä-flrA-rti  1096  b Ä:a»-n  1098 karräza  1101 karsana  1 103 A-a;YSs  1104 karuba  1252 Ära's  1105 A-äsa  1174 kas^a  1106 iW&ff  1108.  1118 Ä-asa/'a  1109 kasama  1187 kasara  1575 Ä;as(i  1110 kasdlr  1111 Ä-ßs/r  1575 A-as/s  1114 fcasr  1117
5645:Jcabanina  947 kacul(a)  1019 Ä;arf?/e  1125 fcarf/j«  984 kad%na  989 Ärarfö;-  987 Äraft-^;  993 kahwe  1005 fcatÄ;  1014 Ä;ais  1015 Ä;a;maA;  1009 A^o/ä/ä  1012 kalabadan  1275 kalabahk  645 Ä;nZf//'a<  1022 ykaZfli  1021 kalamfir  1085 kalaimz  1276 kahhrtna  1028 I  kaldznm  1028 !  1023 '  Ära/fa  798 kalgun  795 Ä;aZ/Ä-o  1031 !  fcff/i-an  1034 I  Ä-a/^rtfc  1039 j  kalpaiv  1027 I  Ä-a/?,p  1030 [  kamcik  1042 I  kamdzija  1042 I  kamfora  1100 j  kamila  653 kamis  1047 j  kamuha  1043 I  ÄrawBs  1047 !  fca/fai  1048 kansa  1056 I  kanza  1056 '  kapak  1061 kapan  1062 j  kapari  978 j  kaplan  1066 I  fear  1069 t  fcaro  1070
5779:Gannef  \.  659 Garaf  1182 Ö«seZ  698 (?««<Z  653 Gauner  932 GawaZ  714 C?a^«  702.  1147 Gazelle  699 Gebenek  1159 Geöer  632 Ge^'Ä-o  707 Gehenna  705 Geischa  706 Gelsemin  942 genieren  705 Geseier  j.  713 Geseires  j.  713 G/ftwr  632 Gjf/-scÄ  760 Gingang  722 Ginggang  722 Ginghum  722 Ginseng  955 Geps  716 G^-ff/f*  2234 Golgatha  743 6ro«ö'  558 Graz  731
5813:JUacheier  1497 Madapolam  1342 Magazin  1362 Maharadscha  1692 Mah-Jong  1338  a Mamluk  1384 Mammon  1386 Mammut  1385 M'indarin  1400 Mandoline  2015 Mandarin  1400 Mango  1393 Mangrove  1394 Manguxte  1395 Manichäer  1397 Jlf«MM«  1398 manna  ahd.  1398 Marabu  1410 Marienkäfer  1417 Markab  St.  1420 Markasit  1374
6044:gazelle  699
6045:gazette  1059
6101:madapollam  1342 madias  1345 magazine  1362 maharajah  1692 mah-djong  1338  a mahout  1352 mamnluke  1384 mamelttke  1384 manihmk  1384 mammon  1386 »«ammuife  1385 manatee  541 mandarin  1400 mangis  1395 mangle  1394 mango  1393 mangosteen  1395 mangrove  1394 marigustin  1395 wafwn«  1398 marabou  1410 marcasite  1374 marchpane  1452 /»/rtsfc  1436 masque  1436 mattrexs  1446 meerschauin  1416 Messiah  1437 mikado  1468 minarct  1463  a J/0(/J*«  (Great)  1494 mohair  1497 moZ/a  1448 moloch(ize)  1379 wionsoow  1451 moolah  1448 tnoonshee  1512 mordechi  1478 mordishee  1478 morocco  1406 mosÄ;  1435 moslem  1516  a mosque  1435 »woxa  1480 moxibustion  1480 /»McÄ;  71
6518:gaban  971 gaharit  1030 gabeile  974 gäühe  1714 gaife  994 gaüan  741 lyaZa  864 galanga  795 galange  afz.  795 galant(erie)  864 galanthomme  864 gatnache>!  633 ganse  1056 garatnaches  dial.  633 garbin  674 garde-boeuf  11 garingal  afz.  795 garo(u)  1155 ^awp?  1002 <7a«e  702.  1147 gazelle  699 5rö2:p«<>  1059 gecko  701 gehene  afz.  705 gShenne  705 gene(r)  705 genetCte)  2192 genette  685 gengeli  744 gerbo(ise)  936 gJiazel  698 giaour  632 giberne  641 </«7c<  9.t1 GtV?«-«  951 gingembre  1930 ^tV«/"«'  2234 .9jVo/?*'  1085 giroflee  1085 gnacarS  1546 godemetim  afz.  633 golgotha  743 gomtne  gutte  712 pon^  558 gouape  1002 goudon  703 goudron  1128 gouge  728 goujat  728 $fOM?e  741 goum  747 goumhie  750 gourbi(l)  1252 gourgandine  677 Graa?  731 grubeau  673 grabeler  673 Gr^ai  731 gulbre  632
8719:mn!  64 macar  1456 macara  1371 mar-«!'  1370 madem  1341 magaza  1362 magazin  1362 mahal  806 mahala(giü)  1350 mahmicr(ie)  1359 waza  1367 maidan  1364 maimu^ä  1365 malotea  1380 mamelegiü  1487 mmneluc  1384 manä  1398 mandanea  1390 mangal  1392 marabut  1410 marafet  1418
9586:magazin  1362
```


## [2026-09-06T15:16:22.232Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== DEV ===\"; grep -n -i \"gazelle\\|magasin\\|gazette\" DEV.txt | head -20; echo \"=== PHN ===\"; grep -n -i \"gazelle\\|magasin\\|gazette\" PHN.txt | head -20; echo \"=== LAM ===\"; grep -n -i \"gazelle\\|magasin\" LAM.txt | head -10",
 "description": "Grep Devic, Pihan, Lammens"
}
```


### [2026-09-06T15:16:22.331Z] TOOL RESULT

```
=== DEV ===
1389:Gazelle.  Esp.  gaceln,  gacele,  gacel,  autref.  algacel;  por- tug.  gazella,  ital.  gazzeUa.  De  l'arabe  JIji  ghazâl,  même sons.  Buffon  a  donné  le  nom  à^aJgazelle  h  une  espèce  de
1393:gazelle,  qui,  selon  Giivier,  ne  diiïère  pas  de  la  gazelle proprement  dite.
1531:^  ^^^  hoûi\  qui  a  les  yeux  noirs  de  la  gazelle.  Les  Persans en  ont  fait  (S)^^  hoûrl  avec  le  ^  i  d'unité,  et  les  Arabes ont  repris  ce  mot  sous  la  forme  ^jjj^-a»-  hoûrJa.  (Voy.  Dozy,
1600:Kazine.  Trésor  du  Grand-Seigneur.  De  l'arabe  io->y^ hhazïnn ,  venant  de  la  même  racine  qui  a  donné  magasin.
1657:Magasin.  Esp.  magacen,  almagacen ,  almarcen,  almacen, portug.  almazem,  armazem,  ital.  magazzino.  De  l'arabe  (j-y^ makhzen ,  plur.  (j)!^  makhâzin,  grenier,  lieu  de  dépôt,  ve- nant du  verbe  ijys^  mettre  en  magasin,  serrer,  conserver.
1698:magasins  souterrains   La  forme  des  matamores  ne
1709:^  Citons  pour  mémoire  Texplication  suivante  :  ffll  y  eut  vers  i38/i,  ou Provence,  une  sorte  de  Jacquerie  dont  les  trop  nombreux  associés  étaient connus  sous  le  nom  de  tuchins  ou  coquins;  et  dans  quelques  parties  du  Midi , sur  le  territoire  de  Bormes,  par  exemple,  on  appelle  encore  niatnuchiiis (mali  tuchini)  les  brigands  et  les  (iloiis.-'i  [Magasin  pittoresque ,  numéro  de  fé- vrier 1876,  p.  55,  d'après  M.  Pli.  Giraïul,  Notes  rhronnlng.  pour  servir  à rbistoire  de  Bormes,  1  859.)
2534:Algacel ,  esp.  voy.  Gazelle.
2549:Algazelle,  voy.  Gazelle.
2633:Almacen ,  esy>.  voy.  Magasin.
2641:Almagacen,  esp.  voy.  Magasin.
2648:Almarcen,  esp.  voy.  Magasin.
2657:Almazem,pg'.  voy.  Magasin.
2774:Armazem,/?^*-.  voy.  Magasin.
3501:Gabian,  voy.  Grèbe. Gabrian,  voy.  Grèbe. Gacel,  esp.  voy.  Gazelle. Gacela,  esp.\o\.  Gazelle. Gacele,  esp.  voy.  Gazelle.
3530:Gazella ,  p^.  voy.  Gazelle.
3531:Gazelle.
3535:Gazzella,  ital.  voy.  Gazelle.
3807:Magacen,  esp.  voy.  Magasin.
3808:Magasin.
=== PHN ===
5179:GAZELLE, 6. f. (a.)
5180:^\^ [ghazâl] antilope, gazelle, féminin âII^ [ghazâlat]. Mam-
5266:fondre ce mot avec gazelle, qui, tout en dérivant du même
5680:l'emmagasinage et à la vente de diverses marchandises ; par
6034:lant d'une gazelle, d'un jeune homme ou d'une jeune fille).
6554:MAGASIN. — Los Turcs écrivent tJ^^^ [khazînph]^ qu'ils pro-
6839:MAGASIN, s. m. (a.)
6845:magazine. — Figurément, le nom de magasin se donne à cer-
6847:Magasin eficyclopédique , le Magasin théâtral, etc. En Orient, plu-
6848:sieurs ouvrages portent, comme chez nous, le titre de Magasin,MAG 2^3
8170:des boutiques et des magasins. Conune on y reçoit aussi des
10691:Magasin, s. m. (a) a^a
=== LAM ===
322:fanfaron ; g : bagasse, magasin, estragon; cA dans Achernar
968:kantar, kazine, gazelle, etc. M' Jeannier dit qu'à Bagdad
1491:Algazelle ou AlgazeL Espèce du genre des antilopes
1492:vivant en Afrique; de Jljàl algka:^âl, la gazelle (i).
4147:la grandeur de la gazelle (}); J'jill jj5 çiôl^^ ^3 Les moder-
4754:kha^Uia, trésor, de la racine ùj»- kha:^an , emmagasiner ,
4755:serrer. Cette même racine nous a donné magasin (i), de
4757:cliambres, des magasins tûjtf-\ un four et un bain.»
4763:(1) M. Gasaeiin se contente de relevai- ii l'analogie» de magasin avec
4960:(5) C. Flaubert : Magasin Catholique illustré. 1853. p. 285.152 MAHA
```


## [2026-09-06T15:16:46.772Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== FSD vol2 Jasper ===\"; grep -n \"Jasper\" FSD_vol2.txt | head -20",
 "description": "Grep FSD vol2 for Jasper"
}
```


### [2026-09-06T15:16:46.829Z] TOOL RESULT

```
=== FSD vol2 Jasper ===
3250:1924),  a   French  organist  and  comi)o--:er  of  operas,  songs,  and sacred  music.  3.  Guillaume  (l().'j6~s/iol73.l3,  a   Itrencli prelate  and  statHsman.  4-  Jean  («/24l7!i-l-u/5o!S42),  a French  Roman  Catholic  preiate;  went  to  tiie  United  rfiate.s in  1791:  founded  Mount  St.  Mary’s  College,  Emmitsburg; Maryiaml.  S.  Paul  Antoine  t-.  rlTiG- IsrD,  a   Fs-etirii piiysicl'tn  to  Emp;-e.-s  Eugenic.  C.  1   du-hois',  2   dn-t.ois'. A   county  in  sauthwe.stern  Indiana:  435  sq.  m.:  county* seat,  Jasper.  7.  A   borough  in  Ciciirileld  county.  Pa.
5728:—   E.  pebble,  a   brown  mottled  variety  of  Jasper  found  in Egypt;  used  as  a   gem.— E.  porcelain,  earthenware  figures, cups,  etc.,  coated  with  a   blue  or  green  enamel  and  found  in Egyptian  tombs,  etc.  Compare  pottery.—  E.  scarf  or veil,  a   scarf  or  veil  made  of  cotton  netting  and  appUquAd on  both  sides.—  E.  thorn,  a   tree  (Acacia  vera)  from  which gum  arable  is  obtained.—  E.  type,  letters,  or  figures,  same as  ANTIQUE,  n.,  3.—  E.  vulture,  see  under  vulture.—  E. ware,  a   kind  of  Wedgwood  ware.
30180:it  of  Vascortia,  Kings  of  Cologne.  See  under  KiNGt.  2,  .same  as  Jasper. Gas'pardt.
40497:diplomat  who  procured  the  Rosetta  Stone  for  the  British Museum.  24.  Sir  William  Eowan  (»/alS05-“/2l8(l.5),  an Irish  mathematician;  invented  the  quaternlon.s;  astronomer royal  for  Ireland.  25.  A   county  In  N.  Florida;  508  sq.  m.; county'seat,  Jasper.  26.  A   county  la  S.  Illinois:  438  sq. m.;  coimty'seat,  McLeansboro.  27.  A   county  In  central Indiana;  402  sq.  m.;  county»spat,  Noble.sville.  28.  A county  In  central  Iowa:  576  sq.  m.;  eounty’seat,  Webster City.  30.  A   county  In  S.  W.  Kansas;  033  sq.  m.;  county-
43715:spelled  hxnia-,  which  see  for  words  not  found  here.  Bee  aist ISEMO-.]  — heiu"a-ba<roni'e-ter,  n.  An  apparatus  to  as- certain and  register  the  specific  gravity  of  Ijlcod.—  liens'a- chatc,  n.  A   ligiit-colored  .agate  svmtted  witli  red  Jasper;  a blooii-awte.—  hem"a-chro"ma-to'sIs,  m   .^ame  as  hem TOCHKo.MiTosLS.— hem'a-ehroine,  n.  .Stime  as  hemo- CHHOME.—  hem"a-chro'.sIs,  n.  Same  as  hematochrosib. —   hem'a-citc,  n.  A   preparation  of  the  blood  ot  animals with  pulverized  mineral  and  vegetable  substances,  dried, com.pre.ssed  Into  molds,  and  varnished;  used  for  buttons, etc.—  hem'a-cec''loin,  n.  Parae  as  HE.MOctBiOM.—  hera'a- cyte,  n.  Anat.  A   blood-corpuscle.—  hem"a-cy-tom'e-ter, n.  An  instrument  for  determining  the  number  of  corpttscles in  a   given  quantity  of  blood.— hem''a-cy"to-2o'on,  n. See  CYTozooN.
45287:Hey 'wood,  1   hS'wud;  2   hfi'wdbd,  n.  1.  Eliza  (n#e  Fowler), (lC937-Vssl756),  an  English  novelist;  satirized  in  Pope’s Dunciad.  3.  Jasper  (lS35-yi8l59S),  an  English  Jesuit poet.  3.  John  (1497-1S65),  an  English  dramatist  and epigrammatist:  father  of  the  preceding.  4.  Thomas,  an English  dramatist  and  actor  who  lived  about  1645.  5.  A manufacturing  borough  In  S.  E.  Lancashire.  England.
61506:FIVE  Nations,  under  five.  S.  One  of  the.Iroquoian  stock of  North-American  Indians  or  their  language.  See  Ameri- can. 3.  A   river  In  Jasper  county,  Ind.;  length,  120  m.  to the  Kankakee  river.  4.  A   county  in  E.  Illinois:  1,123  sq. m.;  county-seat,  Watseka.
63426:Would  bring  thee  down  an  eagle.  color.  4.  Jasper»ware.  [<  OF.  jVespre,  <   L.  iiispis,
63469:I'sl-kow,  re.  Same  as  Yazikop.  ly  “Sergeant  Jasper”  C17S0-“/9 1779),  an  American  Rev-
63479:Sv  white  flowers  ®   o4aY A   0*  A   County  in  E.  Texas:  077  sq.  m.;  oounty*aeat.  Jasper.
63487:samftac).  the  Spanish  or  Cat-  \   Jas'po-nyx,  1   Jas'po-nlks;  2   jas'po-nyks.  re.  Hfirecral.  Jasper
64897:A   city  in  Jasper  county, Jo'p'pa,  IJap's;  2   jOp'a,  n.  Bib.  3   Chron.  II,  16.  The  ancient American  physician;  President  of  'Texas  republic,  1844-  name  of  Jaffa.  Jop'peJ,  [Gr.  lopp'd,  <   Heb.  Yafo, 1846;  committed  suicide.  2.  David  Buniple  (182,5-’/8  .
66852:Kas'per,  n,  [D.]  Same  as  Jasper.
```


## [2026-09-06T15:16:48.894Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== ARB mo3rb kanz ===\"; grep -n \"كنز\\|الكنز\" ARB_mo3rb.txt | head -10; echo \"=== ARB abdulraheem ===\"; grep -n \"كنز\" ARB_abdulraheem.txt | head -10; echo \"=== AFM ===\"; grep -n \"كنز\\|مخزن\\|خزانة\" AFM.txt | head -10; echo \"=== TAD ===\"; grep -n \"كنز\\|مخزن\" TAD.txt | head -10",
 "description": "Grep Arabic sources for kanz/makhzan"
}
```


### [2026-09-06T15:16:48.989Z] TOOL RESULT

```
=== ARB mo3rb kanz ===
21170:« واصاه من كثزث القر قى الوعاء > . وقال الث : « يقال : كيز الإضان ما لايكزه ٠‏ ركنزت 1 
=== ARB abdulraheem ===
=== AFM ===
5157:+ ( القشنيزة ) ترايت كنزلا وهى عشة 3 توق رق الهندباء 5 خضراء 
=== TAD ===
```


## [2026-09-06T15:16:58.328Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '63460,63480p' FSD_vol2.txt; echo \"=== page markers near ===\"; python3 - <<'EOF'\nimport re\nt=open('FSD_vol2.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint('leaves',len(t))\nfor i,pg in enumerate(t):\n    if 'Jas\\'po-nyx' in pg or 'Jaspe' in pg:\n        print('leaf',i)\n        print(' '.join(pg.split())[:300])\n        break\nEOF",
 "description": "FSD Jasper entry and leaf"
}
```


## [2026-09-06T15:16:58.907Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '21160,21185p' ARB_mo3rb.txt",
 "description": "Jawaliqi kanz context"
}
```


### [2026-09-06T15:17:00.246Z] TOOL RESULT

```
Jarn'dyce,  1   Jum'dis;  2   jiirn'dyc,  John.  In  Dickens’
.   "   American  jasmlne.ciaworitt  coccinea,  of  the  southei
Jar  n«t"»  1   jari^nut  ,   3   ]ar_niit ,   re.  [dal  J   bee  GnouNwroT.  ^nd  western  United  States.  It  has  tube«shaped  red  flowei Jam  vld,  l   yarn  vit,  3   yarn  yf*.  Norse  Myth.  A   forest,  _   bastard  J.,  the  matrimony«vlne.—  blue  J,,  the  marsh*
cast  of  Midgard,  the  leavM  of  which  were  Iron,  the  abode  of  clematis  (.Clematis  crispa)  of  the  southern  United  States.
i-shn"blsle'hem,  l   ]a-slia’'bal,U'hem:  2   ja-shu”W»ie'U£m,  Kas'perJ;  F.  Gas"pard',  1   gos’por',  3   gas”piir';  G.  Cas'-
re.  Bib.  f   Cftrore.  iv,  22.  par,  1   kas'por,  2   kas'i3.ir,  Kas'parf;  It.  Gas'pa-ro,  1
I'shub-ites,  1   je'shitb-olts  or  ja.-m'ub-<ilt3;  2   ja'shi'ib-Its  or  gas'pa-rO,  2   giis'pa-ro,  Gas-par'rof;  L.  Gas'par,  1   gas'-
jash'iib-Its,  re.  pf.  Bib.  Nwrej.  .xxvl,  24.  [CArore.  xi,  47,  par,  2   6a.s'par;  Pg.  Sp.  Gas-par',  1   gns-pQr',  2   gas-pari;
I'sl-el,  1   j6'si-el  or  jas'i-el;  2   j5'sl-61  or  jia'I-ei,  re.  Bib.  1   Sw.  Kas'per,  ikas'par,  2   kiis'per.  2.  William,  common-
I'sl-kow,  re.  Same  as  Yazikop.  ly  “Sergeant  Jasper”  C17S0-“/9 1779),  an  American  Rev-
is"mln',  1   sos’man';  2   zhiis'man',  Jacques  (V6l79S-’“/4  oUitlonary  soldier  who  replaced  the -American  flagon  Fort
1864).  A   French  poet  who  wrote  In  the  Provencal  or  Agenals  Moultrie,  June28, 1776.  He  wasmortally  wounded  In  trying
patois;  known  as  "   the  Barber  Poet  of  Agen”:  Lem  Papillotos.  to  place  the  colors  on  Spring  Hill  redoubt.  Savannah,  Oct.  7,
is"ml-na'ce-»,  1   jas'mi-n5'si-l;  2   jAs*ml-a5'ce-S,  re.  pi.  Mot.  1779.  3.  A   county  la  central  Georgia;  410  sq.  m.;  county*
A   former  family  of  plants  that  Included  the  jasmine.  [   <   seat,  Monticello.  4.  A   county  In  S.  E.  Illinois;  S03  sq.  m.;
JASM1NUM.1  county*seat,  Newton.  5.  A   county  In  N.  W.  Indiana;  585
^s'lntnc,  1 1   Jaa'imn;  2   jSa'min  (xui),  n.  1.  An  orna-  sq,  m.  ;   count.v»seat,  Rensselaer.  6.  A   county  In  central iS 'mins,  f   mental  apocyna-  -   Iowa;  720  sq.  m.;  county»seat,  Newton.  7.  A   county  In. S.
ceous  plant  of  the  genua  7^08-  C\  Mississippi;  647  sq.  m.;  county*seat,  Paulding.  8.  A
minum,  with  fragrant,  gen-  RVI  ( — o   county  In  S.  VV.  Mlasourl;  632  sq.  m.;  coiintyseat,  Carthage,
Sv  white  flowers  ®   o4aY A   0*  A   County  in  E.  Texas:  077  sq.  m.;  oounty*aeat.  Jasper.
•   .ft  9   10-  A   town,  county-seat  of  Hamilton  county,  Fla.  11.  A
=== page markers near ===
leaves 774
leaf 35
game by scent of the foot. II. adv. I. With dry feet. 3. [Archaic.] By scent of the foot.— dry-footed, o.— dry -founder, vt. To founder.— dry-foundered, a. [Archaic.] Foundered, as a horse, from food rather than from drink.— dry -grind, vt. & vt. To grind without wetting.— dry -handed, a. [Scot.] We
```


### [2026-09-06T15:17:00.315Z] TOOL RESULT

```
وان +00 
تعالل ) وتزودوا ا( قال : اكوك والززيت 0 





0١‏ فى م ج«فم» وهو خبطا وام . وفى < «مفتح» يكسر المي ؛ ودوشطأ أيشاء لأن المفتح 
بالكسر المفتاح .و ”الك“ من الألفاظ القرآئية » وردت فية مراراء ومرد نيه أيضا « كتتم ». 
ر «كززرن» و« تكؤرن » ٠١‏ وه كلة ع بة بحت » م يدع يحمتا غير المؤلف فيا أعل ٠‏ قال الرأغب : 
« واصاه من كثزث القر قى الوعاء > . وقال الث : « يقال : كيز الإضان ما لايكزه ٠‏ ركنزت 1 
المقّاء : إذا علد" > ٠‏ وأنظر اللسات ٠.‏ (؟) كذلك ”*الكئان' لفظ عربة 6 لم أجد من خالف 
فى ذلك إلا فى هذا الككّاب ٠‏ قال ابن دريد ( ”؟ 3 ): ٠:‏ « والكّان عرفى” معروف» ©» بإماعى 
0 فم الناء هو اليج والتوشع 


5 ومر 


مانا انه خيس دياق لعضة عل عض حى 0 
أرالدرن والوتخ ٠‏ ويقال : سقاء كن - إذا تلزج به الدرن ٠‏ 2 ق ب «أظه» وهو أاوافق 
لمان (5 ٠1‏ ام) ٠‏ (4) مشى البيت فى ص ١8١‏ س 7 كا هنا ٠‏ وفى ص #٠4‏ س 8 
بلفظ «مع سويق» وه وألموائق هنا لما فى ىع * ٠‏ وفى اللسان «سويق» ٠‏ 
(١‏ فى م «بن سفيان» وهو خطأ : فان نصر بن على هو : ام 
اللَدث الثقة » شيخ أصعاب الكتب الستة » مات سنة ٠‏ 6 ؟ وسقياث هر ابن عبينة 5 الإمام الخافظ 
6 هو تمد بن سوقة الخنوى” ؟ من قات أهل الكوفة وخيارهم » اه نأتباع النابعين ٠‏
```


## [2026-09-06T15:17:15.844Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '21120,21160p' ARB_mo3rb.txt",
 "description": "Jawaliqi kanz headword"
}
```


### [2026-09-06T15:17:15.889Z] TOOL RESULT

```
(1) ل يدع أحد ” الكثرى ““ معرمة غر الأصمى” فيا نقل عنه المزلف ٠‏ فانى لم أجد هذا النقل 
ونه عنك غيره ٠‏ إلا أن أين دريد قال )98 : 14م : 2 الكتثرة قعل مات» وهو تداخل الثىء 
بعضه فى عض واجيّاعه » فات كان الكمثرى عربيا فن هذا اشتقاقه » ١‏ وقال الأزهرى فيا تقله الادان : 


ومأات جماعة من الأعراب عن الكمترى ظٍ يعرقوها » ٠‏ 


ان 

ا 
ا ست جز | | 

7 عراس لبلالده 





باب الكاف كن 
1098ز1ز101010|[|ةإة1ذ12121111ظ ٠ش‏ 





رق 
: 8 - ا 0 3 واسمة 1 بالعر ب 2 مفتح * 0 
اك 
5 ال أبو هلال َ وقال لعقهوم ف ” الكان “ أنه فارسى مغرنيا ه 
1 سوير ور .2 ر فق 2 0ط 
5 اك الكعك 56 |الميزالياس 0 قال الث 0 أحسبةه معرب 05 و ل : 
)2 
ل سم رُ - 2ه سور م 
اذا امك بلحم ل #د وخشكان وسعسسوفق مقنود 
2 595 5 )2 ل زفق 
وى و 5 عونق غل عق ن سيان عن ابن سوقة عن سعيد فى قوله . 8 


وان +00
```


## [2026-09-06T15:17:16.672Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"treasure-master\\|treasure  master\\|master  of  the  treasure\\|treasurer\" FSD_vol2.txt | head -20",
 "description": "Search FSD for treasurer gloss"
}
```


### [2026-09-06T15:17:16.731Z] TOOL RESULT

```
25007:For'rest,  l   fer'est;  2   f6r'6st,  n.  1.  Edwin  ( Vtl  806-1“  /islS72) ,   . an  American  tragic  actor.  3.  Sir  John  {8/5!l847-V3l61S), an  Australian  explorer,  surveyor,  and  statesman;  first  pre- rnlerand  treasurer  of  Western  Australia,  1890-1901.  3.  Na- than Bedford  (7/i,l,821~io/5s]877),  a   Confederate  general; took  Fort  Pillow,  1804.  4.  A   city,  county»seat  of  St.
40703:—   at  the  h.  of,  from  the  hand  of;  by  the  operation  of.— Black  H.  [U.  ri.],  a   secret  society  of  Sicilian  origin  that ende.avors  to  override  the  law  and  extorts  money  under threat  of  violence.—  book  h.,  a   stiff  legible  business  hand- writing suitable  for  bookkeeping.—  Buddha’s  h.,  a   culti- vated variety  of  the  citron  (Citrus  medlca}  the  fruit  of  which re.semblea  alighOy  the  hand  and  is  frequently  reproduced  in Japanese  works  of  art. —   clean  hands,  freedom  from  cor- ruption; honesty  In  money  matters:  as,  the  treasurer  came out  of  the  ex.amlnatlon  with  clean  bands.—  comparison  of hands,  see  under  compabison,  dead  man’s  h.  (Poker), a   combination  of  cards,  usually  two  pairs  of  jacks  and  eights, generally  considered  as  being  worthless.— eldest  h.  (Card- playing), the  first  player;  the  player  on  the  dealer’s  left;  the age.  In  poker,  this  plaj’er  is  entitled  to  bet  last  before  the drsiw;  in  some  varieties  of  the  game,  after  the  draw.—  for one’.s  own  h.,  for  one’s  own  benefit  or  gain.—  from  h.  to h.,  from  one  person  to  another,  as  around  a   circle  or  along a   series.—  from  h.  to  mouth,  without  provision  for  the future:  with  no  care  for  the  morrow:  iw,  tramps  live  from hand  to  mouth.—  h.  and  glove,  in  close  intimacy.—  hand's
41534:A   Macedonian  satrap  of  Babylonia;  treasurer  under  Alex- ander; he  proved  unfaithful,  fled  to  Greece,  and  was  assas- sinated. Har'pa-Iost  [Gr.].
46459:Keole;  Christian  year.  Sunday  AjUr  Ascensiun  st.  4. [<  AS.  liortliim,  <   hord,  treasure.]  Syn.:  .see  .vmass.— hoard'er,  n.  One  who  hoards;  anciently,  a   treastirer. hoard*,  n.  1.  That  which  has  been  accumulated  and stored  away;  stock  and  store ;   treasure.  3.  A   hoarding* place;  treasury.  3t-  A   place  of  concealment.  [<  AS. hord,  fund.]  Syn.:  see  heap.—  hoard' »house"t,  n.  1.  A cattio»slied.  2.  .Atreasure»hou.se.— h.»wardt, «.  One  who Is  in  charge  of  a   hoard;  a   treasurer, hoard'*,  u.  An  ennlo.surc;  .shelter.  See  hoarding*.  [<  OF. horde,  <   OD.  Jionle,  hurdle.]
63482:Atixiialiem  Bt  13  Uf/  7   ^Ad.  [Per,,  treasurer.]
74035:Leeds,  1   lldz; 216ds, ?}.  1.  Dukcof  (1631-V2ol712), Thomas Osborne,  an  English  statesman;  lord  treasurer;  five  years In  prison;  president  of  the  councU.  2.  A   borough  In  the West  Riding,  Yorkshire,  England;  noted  for  manufacture of  woolen  goods,  3.  A   town  In  Androscoggin  county.  Me.
```


## [2026-09-06T15:17:29.016Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('FSD_vol2.txt',encoding='utf-8',errors='replace')\nlines=t.readlines()\n# find leaf containing line 63482\ntxt=''.join(lines)\nidx=txt.find('[Per,  treasurer.]')\nif idx<0: idx=txt.find('treasurer.]')\nprint('idx',idx)\nleaf=txt[:idx].count('\\f')\nprint('leaf(0-based)',leaf,'of',txt.count('\\f'))\nseg=txt.split('\\f')[leaf]\nimport re\nprint('numbers on leaf:',re.findall(r'\\b1[0-9]{3}\\b',seg)[:20])\nEOF\necho \"=== ARB formfeeds ===\"; python3 -c \"\nt=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/ARB_mo3rb.txt',encoding='utf-8',errors='replace').read()\nprint('ff',t.count('\\f'))\ni=t.find('باب الكاف')\nprint('leaf of bab al-kaf', t[:i].count('\\f'))\n\"",
 "description": "Locate FSD page and ARB leaf"
}
```


### [2026-09-06T15:17:30.889Z] TOOL RESULT

```
idx 13018426
leaf(0-based) 607 of 773
numbers on leaf: ['1850', '1848', '1751', '1777', '1028', '1883', '1569', '1779', '1864', '1776', '1779']
=== ARB formfeeds ===
ff 0
leaf of bab al-kaf 0
```


## [2026-09-06T15:17:38.151Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\ntxt=open('FSD_vol2.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (605,606,607,608):\n    s=' '.join(txt[i].split())\n    print('LEAF',i,'HEAD:',s[:140])\n    print('   TAIL:',s[-140:])\nEOF",
 "description": "FSD vol2 leaf headers"
}
```


### [2026-09-06T15:17:40.179Z] TOOL RESULT

```
LEAF 605 HEAD: ee. Jam'bo-rin(cc, 1 jam'bo-rln: 2 jiira'bo-rin, re. Awhitecrys- talline product of jambolana*seeds, of wiiich the exact nature is undetermi
   TAIL:  l]a-n5'o;2ja-nB'a, re. Bib. 2 /Cirejis .xv, 29. [Heb., resting-place.) Ja-no'e, 1 ja-nO'i; 2 ja-nS'e, re. Bib. (iDouai). Ja-uo'bali, I ja-n
LEAF 606 HEAD: o'ha; 2 ja-nQ'ha, n. Josh, xvi, 6. [Heb.I Ja'nos, re. [Hung.] See John. Jan'seu, 1 jan'sen or (Z).) yan'sen; 2 jau'sfin or (£>.) yiin'sBn, S
   TAIL:  -M- I n J.J ! -rr The cabs and jorrcws, the Vehicles of tho despwed Public, roHcd pobj) of the Argo. See M130KA. Jar cMiiN !i 1 oor dan , 2
LEAF 607 HEAD: zhar dan , Marie Catlieriae Hor* paat, N. I\ Winua I have Met p. 18. (n. *: sen. 1850,] Jasp., afibr. .Taiipefa 5 c v, Jaf'vie, M. Sce B.AIU
   TAIL: f the family Ofeace*, with takas are of interest as the source of 23sop’a Fables, and of Australian tree (Eucalyptus niarginata), xem&Tkaole
LEAF 608 HEAD: tor opposite odd-pinnate leaves and clusters ot often beautiful innumerable fairy-tales, folk-songs, and nursery-rimes, the durability of it
   TAIL:  and the lower. 1®y bawk er, 1 JB hok er: 2 jn, hakjjr, »._ iE??” In mammals the upper jaw is fixed, the lower movable. (2) One of the bones
```


## [2026-09-06T15:17:48.196Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && ls -la; python3 - <<'EOF'\nimport re\nfor v in (3,4,5):\n    f=f'/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v{v}_pages.txt'\n    try:\n        t=open(f,encoding='utf-8',errors='replace').read()\n    except Exception as e:\n        print(v,e); continue\n    print('vol',v,'len',len(t),'ff',t.count('\\f'))\n    print(t[:300].replace('\\n',' | ')[:300])\nEOF",
 "description": "Check BQT vol3-5 OCR"
}
```


### [2026-09-06T15:17:50.189Z] TOOL RESULT

```
total 28692
drwxrwxr-x  4 sfmqrb sfmqrb     4096 Sep  4 14:06 .
drwxrwxr-x 23 sfmqrb sfmqrb     4096 Sep  4 14:06 ..
-rw-rw-r--  1 sfmqrb sfmqrb     8390 Sep  4 14:06 BQT_v3_pagemap.json
-rw-rw-r--  1 sfmqrb sfmqrb  2499427 Sep  4 14:06 BQT_v3_pages.txt
-rw-rw-r--  1 sfmqrb sfmqrb 11053965 Sep  4 14:06 BQT_v3_picofile.pdf
-rw-rw-r--  1 sfmqrb sfmqrb  2055176 Sep  4 14:06 BQT_v4_pages.txt
drwxrwxr-x  2 sfmqrb sfmqrb    20480 Sep  4 12:59 BQT_v4_pages.txt.pages
-rw-rw-r--  1 sfmqrb sfmqrb  8501918 Sep  4 14:06 BQT_v4_picofile.pdf
-rw-rw-r--  1 sfmqrb sfmqrb   723928 Sep  4 14:06 BQT_v5_pages.txt
drwxrwxr-x  2 sfmqrb sfmqrb    12288 Sep  4 13:14 BQT_v5_pages.txt.pages
-rw-rw-r--  1 sfmqrb sfmqrb  4472561 Sep  4 14:06 BQT_v5_picofile.pdf
vol 3 len 1461478 ff 720
[pdf page 1] | [NOT OCRED - use tools/ref_page.py] | [pdf page 2] | 7 | Ub | sits k ge | AS ۱۰۶۲ ‏نتف‌بال‎ | ‏ومع‎ ‘oo ‏داي و‎ el Oe |  | far | en rotons ‘ ‘ ths ۰ ‏دیهان‎ | ‎۳ 2 7 | ۰ SF Ps | On Awe | ۰ | ‏-ل‎ 9 ‘il | ۱۳۴۳ ‏چاپ دوم فروردین‎ | ‏با تجدید نظر کامل‎ | ‏بسرمایه کتاپفروشی ابن سینا- تهرا
vol 4 len 1196230 ff 552
[pdf page 1] | [pdf page 2] | ه | و سم | ۰ و | الب | اس ی 9 ۱ | عه ر جر ن‌خلف بربری لیر رها | ّف‌بال ۱۰۶۲ #کک . | ناس مد ی «چا لد ولوح ا! | ۰ ً ّ ۰ ,7 اس ۸۰ | و مین ۰ شور بر رود نات سا رراصاو رصم | ی | تم و3 رو | اد دش نوت | طلرجارم : م-ی | ی اس - | چاپ دوم فروردین ۹۳۴۳ | با تجدید نظر کامل | بسرمای
vol 5 len 413652 ff 292
[pdf page 1] | 5 | [pdf page 2] | ,۶ +مه | مان ها | ۰ | بل | هم هم ه | اعلیات | 8 | کم | ول ری | « داژن » | موسسة انتشار ات امی رکیهر | تهران» ۱۳۷۹ | [pdf page 3] | تعلیقات بران اطع |  | دکترمحمد معین |  | چاپ چهارم : ۱۳۶۲ |  | چاپ پنجم : ۱۳۷۶ |  | چاپ و صحافی: چاپخانةٌ سپهر » تهرانت |  | تیراژ: ۳
```


## [2026-09-06T15:17:53.797Z] TOOL CALL #46: Bash

```json
{
 "command": "timeout 300 python3 tools/ref_page.py BQT:1841 --image 2>&1 | head -60",
 "description": "Fetch Borhan-e Qate page 1841"
}
```


### [2026-09-06T15:18:02.363Z] TOOL RESULT

```
IMAGE: /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/1841.png
REF: BQT:1841  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 638  OCR-lang: fas

-۱۸:۱- کند بیدسنر
است که از جمشید بود و بدست بهرام گورافتاد. | است مشهورمایین تبریز وشیروان٩ ‏ وکرجتان.
گنج گاومیش ۱ - بسنی کنج و مولد شیخ نظامی علیه‌الرحمه از آنجا است -
کاوان است که کنج جمشید باشد . و خر الاع دم پریده را لیز گوبند و بمربی آبتر
۳ ۹ ان 3
گنج کاووس(۱)- ب‌لسن‌هندخاست | او
: 8 گند - بفتح اول و سکون ثانی و دال
از سی لحن باربد وآن راکنج کاو هم میگوبند
: ها" ابجد . بوی بد راکوبند ۸ - ویضم اول, بمعنی
ورسم‌الخط این زمان بيك واو آمت . ۹ اد ۰ ۹
8 . ی خابه باشد که بعربی خصیه خوانند ‎٩‏ .
گنجگاه ؟ » بروزن ومعنی پنجگاه کند) :۱ ۱ : ۱
است که شمه بلندی مقام راست و شعبه‌پستی‌آن < بر وزد عمدا , چیزی زر
بفه اس گونند که کندیده باشد و ازآن بوی‌ناخوشآید.
۴ له
گنجود ؟ - بروزن رنجور, خزانه‌دار گندآور < بضم اولوفتح واوبروزن
راکونند . خنیاگر» مردم شجاع و دلاور و مردانه‌راگوبند-
رسیده پروزن سردسیر , بلغت زند وپازند بمعنی گندای ۱۲ بر وزن دروای » بمعنی
کنجور است که خزانه‌دار باشد ؛ و در جای‌دیگن کند است که هر چیز بدیوی و کنده وهتعقن
بجای تحتانی بای ابجد نوشته‌بودند : ااعلم ۰ باشد .
(69 چك » چش : کاوی.
۹ < کنجکاو < کنج‌کاوان .
۴ - از :کنج + کاه (< بپلوی 828 * اوستایی 82182 سرود [ رل : کانها بقلم
پورداود چاپ اول ص ‎٩۱‏ ] ). ۴ - از :کنج ور ۵0۲ (* ور » ۷8۵۳ » پوند اتصاف و
دارند کی ( ۰ پپلوی 27( «منای 4 . جزء دوم ازمصدر ۹ (بردن) است بعنی بر لده
وحامل کنج . ر4: ح .4‏ ۴- تحریف کنجوبر 828101027 پهلوی‌بمعنی‌خز انه‌دار» کنجور. رك :
یوتکرص۷۹. رك : ح۳. 8 کنجك ۳ کنز4 ۳ غز نه - غزنین(لغة محل کنج ‏ کنجینه).
‎٩‏ - اصح «شروان» است . ۷ - نیز کنجه» بمعنی قفه ودولایچه استعمال‌شود.
۸ - اوستا 821811 ( بوی متعفن ) » پپلوی 820 ۰ 88808۴ ( کنده ) » هندی
استان 880408 ( بو عطر [خوشیو] ) . افقانی 8808 ۰ بلوچی ع 8800 (کل [ نکن
اول ] ۰ فئله ) . 8200428 . 8280280 ( بد » شربر ) » پارسی باستان - 88818 ( بدی»
تنفر آور ) » سربکلی 813000 « اسشق ۹۳۵ > و رك : هویشمان ۹۳۶ .
‎٩‏ -کردی 807 ( خمیتین ) «زاباس ۰۳۹۹ ممرب‌آن « جند » [ جند بیدستر ]-
نیز کند < پهلوی 818 ( سرباز . سپاه ) « هنای ۲۷۵ » ** غند(ه.م.) ۳ معرب « جند > »
کردی 8020 ( دهکده . پبلاق ) « ژاباص ۳۹۹ ۴ از :کند ( کندیدن ) +۱
( پسوند فاعلی و صفت مشبهه ) , رك : کندای . ۹۱ رك : کندآور .
۴ کندا (هم.) . ۴ جنم اول » رك :کند ( بضم ) و رك : بیدستر .
۰ گنجیدن - بضم اول وفتح پنجم. از : کنج خن اول] (ه.م.) + یدن (پسوندمصدری)؛
جا کرفتن مظروفی در ظرفی » درآمدن چیزی در چیزی -
```


## [2026-09-06T15:18:17.218Z] TOOL CALL #47: Bash

```json
{
 "command": "timeout 300 python3 tools/ref_page.py BQT:1838 --image 2>&1 | head -45",
 "description": "Fetch Borhan page 1838"
}
```


### [2026-09-06T15:18:25.343Z] TOOL RESULT

```
IMAGE: /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/1838.png
REF: BQT:1838  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 635  OCR-lang: fas

کنجار . ۱۸۳۸
رسانند - و بفتح اول زر وگوهری باشد که در کنایه از فناعت است - و کلام خدا را دز
زیرزمین دفن کنند ۱- و بکسراولء بمعنی کیج | کوبند ‎٩‏ -
وس رگشته و متحیر باشد ۴ - و پمعنی صاحب گنج باد - بسمتی کنج باد آورد است
عجب و نکیی وخوستای هم‌آمده است . که کنج دویم باشد از جملهٌ هشت کنج خسرو
گنجار ِ بفتح اول بر وزن زنگار | پرویز ۷ وآن چنان بودکه قیصرروم ازبیمخرو
بمعنی غازه باشد وآن سرخیی است که زنان بر | خزاین پدران خود را بکشتیها در آورده بجاب
روی مالند وآنرا غازه وغنجار و غنجاره رغنجر»* | درباگربزانیده بود اتفاقاً بادی و طوفانی برخاست
و غلفونه وکلگوده نیز خوانند . وآن ششتیپا را بجایی که خسرو پرویز لشکرگاه
گنجاره ۴ « بر وزن انگاره » بممنی | ساخته بود آورد وتمامی‌آن خزائن بدست خسرو
غنجاره است که غازه وکلگوّنهٌ زنان باشد . آمد آنرا باین نام خواندند ۸ .
گنج اگراسیاب نم کنی ات | نج بادآورد - مانکنچیرات
که افراسیاب نهاده بود وپرویز ترا بیافت وآن 8
گنج چهارم است از جملةٌ هعت کنج 9 خرو که کنج دویم خرو پرویز باشد و آنرا گنج
پرویز که کنج عروس و گنج باد آورد و دییه باد آور هم میگوبند که بحذف دال آخر
خروی وکنج افراسیاب و گنج سوخته و کنج باشد ‎٩‏ - و نام نوایی ولحنی هم هست از جملهٌ
خضرا وگنج شادآورد وگنج بار باشد . سی‌لحن بارید . گویندچون این گنج بدست‌خسرو
گنج‌الهی - یک جیم و همزه. پرویز افتاد باربد این لحن را ساخت ونواخت ‎.٩‏
‏۱- پهلوی [827 » ارمنی [688 » آرامی 81022 ۰ 86228 » عربی کنز ۷2۳2
۰ نیب رکك ص ۷۷ > : « ملك زاده‌ای کنج فراوان از پدر میراث یافت » «کلستان <8 ۰ .
۲ -ظ . مصحف «کیج > . ۴ < کنجاره * غنجار* غنجاره ۳ غنجرم
کنجره . ۴ << کنجار < کنجر ‏ کنجره * غنجار * غنجاره ‏ غنجره .
9 - غالبا هفت کنج گفته‌اند. . فردوسی طوسی در شاهنامه آرد :
نخستی ن که بنهاد (خسروپرویز) * کنج‌عروس» . زچین وزبرطای وازهند وروی
دگر « کنج بادآور > ش خواندند شمارش بکردند و درماندند
دکر آنکه داش همی بشنوی تو خوانی ورا «دیبة خسروی»
دکر دامور « کنج افراساب > که کس رانبودآنبخشکی و آب
دگرکنج کش خواندی « سوخته > کز آن کنج بد کشور افروخته
دگر کنج کز در خوشاب بود که بالاش يك تیر پرتاب بود
که ۶« خضرا > نپادند نامش ردان همان نامور کاردان بخردان
دگر آنکه بد « شادورد بز رکه > که کوبند رامشگران ستر گه.
« شاهنامدّیخ ج۹ ص۲۳ ‎٩‏ ۸ #۲بنابرین «کنج بار» (ه.م.) بحساب نیامده, ورك : کربستنشن اسان
ص ۶۹۵ - ۰.۹۹ ‎٩‏ - رك : رشیدی. ۷ -رد :جح ۰
۸ - نیز * کنج بادآورد : لحنی از الحان بلرید :
وقت سحر که چکاو . خوش بزند در تکاو ساعتکی کنجگاو ‏ ساعتگی کنج باد .
7 منوچهر دامقانی ص ۱۸ ۰
رد :گنج اد .
```


## [2026-09-06T15:18:34.119Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for f in MON_part1.txt MON_part2.txt; do echo \"=== $f ===\"; grep -n \"کنز\\|كنز\" $f | head -8; done; echo \"=== Adena v2 ===\"; grep -n \"کنز\" incoming/MON/MON_2vol_Adena_v2_djvu.txt | head -8",
 "description": "Grep Mo'in for kanz"
}
```


### [2026-09-06T15:18:35.823Z] TOOL RESULT

```
=== MON_part1.txt ===
=== MON_part2.txt ===
27177:کنز: 12102 [معر. گنج] (.) گنج» گنجینه. کنز 
30586:بردن. گربة در انبان داشتن 1 کند:) مکنز 
34590:کتاه کنزردن ۲01-0 (مسصم.) گل 
=== Adena v2 ===
27177:کنز: 12102 [معر. گنج] (.) گنج» گنجینه. کنز 
30586:بردن. گربة در انبان داشتن 1 کند:) مکنز 
34590:کتاه کنزردن ۲01-0 (مسصم.) گل
```


## [2026-09-06T15:18:45.472Z] TOOL CALL #49: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 3
}
```


### [2026-09-06T15:18:45.482Z] TOOL RESULT

```


```


## [2026-09-06T15:18:48.222Z] TOOL CALL #50: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/gazelle",
 "prompt": "Give the full etymology text for gazelle, including any mention of Spanish, Old French gazel, Arabic ghazal, and dates."
}
```


## [2026-09-06T15:18:49.330Z] TOOL CALL #51: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/gazette",
 "prompt": "Give the full etymology text for gazette, including Italian gazzetta, Venetian coin, gazza magpie, Latin gaza, Greek gaza, Persian ganj."
}
```


### [2026-09-06T15:18:52.465Z] TOOL RESULT

```
# Etymology of Gazelle

The word "gazelle" has the following etymological path:

**c. 1600**: The term entered English from French _gazelle_, which derived from Old French _gazel_ (14c.). The ultimate source traces back "probably via Spanish, ultimately from North African pronunciation of Arabic _ghazal_."

In summary, the word traveled from Arabic through Spanish and Old French into French before reaching English around 1600, with the North African Arabic pronunciation of _ghazal_ serving as the root origin.
```


### [2026-09-06T15:18:56.533Z] TOOL RESULT

```
# Etymology of Gazette

Based on the Online Etymology Dictionary, here's the documented etymology:

**Gazette** (noun, c. 1600) derives from French *gazette*, which came from Italian *gazzetta*—a Venetian dialectal term meaning "newspaper" that also referred to a small copper coin.

The Italian origin has multiple competing theories:

1. **Magpie connection**: The word may stem from *gazza* (magpie), applied to the newspaper either because the coin bore the bird's image or due to the bird's association with "false chatter."

2. **Coin etymology**: The Venetian *gazetta* coin was reportedly the standard price for reading the government-published *gazeta de la novità* (gazette of news).

3. **Latin root**: Some etymologists propose descent from Latin *gaza* ("treasury"), which would "colloquially lengthen into *gazetta*" as "a little treasury of news."

The source notes: "The general story of the origin of the word is broadly accepted, but there are many variations in the details."

First English use appeared in 1665 for papers issued at Oxford. The verb form emerged in the 1670s, meaning "to announce in the Gazette," since the official journals contained appointments and public notices.
```


## [2026-09-06T15:19:03.773Z] TOOL CALL #52: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%DA%AF%D9%86%D8%AC",
 "prompt": "Give the Persian entry for گنج: etymology (Middle Persian, Old/Proto-Iranian, Median, Parthian, borrowings into Arabic/Greek/Armenian/Aramaic), and any note on گنجیدن."
}
```


## [2026-09-06T15:19:05.715Z] TOOL CALL #53: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AC%D9%86%D8%A7%D8%B2%D8%A9",
 "prompt": "Give the Arabic entry for جنازة: etymology — is it from the root ج ن ز 'to cover', or a borrowing from Persian ganj / Aramaic? Quote the etymology section."
}
```


### [2026-09-06T15:19:09.741Z] TOOL RESULT

```
# Persian Entry: گنج (ganj)

## Etymology

According to the Wiktionary source, گنج derives from **Middle Persian** (/ganǰ/, "treasure"), which came from **Old Persian** *ganzah* ("treasure"). The source suggests this likely originated from **Old Median** *ganǰam* ("treasure").

The entry notes a cognate relationship with Arabic كَنْز (kanz, "treasure"), indicating shared etymological roots across these ancient languages.

## Key Details

**Definition**: The word primarily means "treasure," with secondary meanings including "store" and "granary."

**Pronunciation variants** exist across Classical Persian, Dari, Iranian, and Tajik dialects, with the IPA representation /ˈɡand͡ʒ/ for Classical Persian.

## Note on گنجیدن

The provided Wiktionary content does not include information about گنجیدن (the verb form), so I cannot offer details on this related term based on the source material provided.

The entry demonstrates how this Persian word has influenced other languages, with descendants appearing in Turkmen (genç).
```


### [2026-09-06T15:19:12.015Z] TOOL RESULT

```
# Etymology of جنازة

Based on the Wiktionary entry, the word جنازة is **not** from a root meaning "to cover," nor is it a borrowing from Persian ganj or Aramaic.

Here's the quoted etymology section:

"The whole root ج ن ز (j n z) is from Ge'ez and Old South Arabian, compare Ge'ez ገነዘ (gänäzä, 'to wrap, to prepare a body for funeral') and old Sabaean gnz, gnzt ('funeral'), potentially the same Iranian word as كَنْز (kanz, 'treasure')."

The entry indicates the term derives from ancient Semitic languages—specifically Ge'ez and Old South Arabian—with meanings related to wrapping or preparing bodies for funeral rites. The potential connection to an Iranian word (kanz, meaning "treasure") is noted as speculative ("potentially").
```


## [2026-09-06T15:19:17.551Z] TOOL CALL #54: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AE%D8%B2%D9%86",
 "prompt": "Give the Arabic entry for خزن (khazana) and its root خ ز ن: etymology — native Semitic? cognates (Hebrew, Aramaic, Akkadian, Ge'ez)? any claim of Persian/Iranian origin? Also mention مخزن if given."
}
```


## [2026-09-06T15:19:19.308Z] TOOL CALL #55: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%85%D8%BA%D8%A7%D8%B2%D9%87",
 "prompt": "Give the Persian entry for مغازه: etymology (Turkish? French? Italian magazzino? Arabic makhzan?) and meaning."
}
```


### [2026-09-06T15:19:23.656Z] TOOL RESULT

```
# Arabic Entry: خزن (khazana)

## Root and Etymology
The entry shows the root **خ ز ن** (ḵ z n) with "7 terms" belonging to it. However, the Wiktionary page provides **no etymological information** regarding whether this root is native Semitic or borrowed, and it contains **no cognates** listed from Hebrew, Aramaic, Akkadian, or Ge'ez.

## Meanings (Form I - خَزَنَ)
The primary verb definitions include: "to store, to stock, to lay up, to hoard, to amass, to accumulate" and "to contain, to conceal" (for discovery sites like oil/minerals), plus "to keep secret" and "to put in safekeeping."

## Related Terms
The page references **مخزن** (mukhazzan/makhzan) as a passive participle meaning "stored," though a full entry wasn't provided.

## Limitation
The Wiktionary article does **not address** Persian or Iranian origin claims, nor does it provide comparative Semitic data—focusing instead on Arabic conjugations and modern usage including a Yemen-specific meaning related to qat preparation.
```


### [2026-09-06T15:19:24.643Z] TOOL RESULT

```
# Persian Entry for مغازه

**Etymology:** Borrowed from Ottoman Turkish مغازه (mağâza), which came from Byzantine Greek μαγαζίον (magazíon), from Venetan magazén, ultimately from Arabic خزن (ḵazana) meaning "to store."

**Meaning:** "shop" (Persian: مغازه / maġāza or maġâze). The word has a related term مخزن (maxzan, meaning warehouse), reflecting its shared Arabic root related to storage.
```


## [2026-09-06T15:19:33.135Z] TOOL CALL #56: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%DA%AF%D9%86%D8%AC%DB%8C%D8%AF%D9%86",
 "prompt": "Give the Persian entry for گنجیدن: etymology (Middle Persian winǰ-/wnc-, Proto-Iranian *wyač-, Sanskrit vyac?), meaning, and related forms گنجاندن گنجایش."
}
```


## [2026-09-06T15:19:34.255Z] TOOL CALL #57: WebFetch

```json
{
 "url": "https://www.nisanyansozluk.com/kelime/ma%C4%9Faza",
 "prompt": "Give the etymology of Turkish mağaza: source language (Italian magazzino? Greek? Arabic makhzan?), first attestation date."
}
```


### [2026-09-06T15:19:39.269Z] TOOL RESULT

```
# گنجیدن (Gonjidan)

## Meaning
The Persian verb گنجیدن is "an intransitive verb" that means "to be contained; to be held."

## Example
The entry includes a classical citation from Rumi's Masnavi (c. 1260s): if you pour the sea into a pitcher, "how much will it hold [lit. how much is contained]? One day's store."

## Related Forms
The page references the related verb **گنجاندن** (ganjāndan), which is the transitive counterpart meaning "to contain" or "to cause to fit."

**Note:** The Wiktionary entry does not provide etymological information beyond the transliterations and pronunciations across Persian dialects (Classical, Dari, Iranian, and Tajik). Etymology details like Middle Persian origins are not included in the accessible content.
```


### [2026-09-06T15:19:39.325Z] TOOL RESULT

```
I cannot provide the etymology information you requested based on the provided content. The webpage excerpt only shows the header and footer of Nişanyan Sözlük (Nişanyan Dictionary), but does not include the actual dictionary entry for "mağaza" that would contain etymological details about its source language, whether from Italian, Greek, or Arabic, or its first attestation date.

To obtain this information, you would need to access the full dictionary entry for "mağaza" on the Nişanyan Sözlük website directly.
```


## [2026-09-06T15:19:46.278Z] TOOL CALL #58: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/magazine",
 "prompt": "Full etymology of magazine: Middle French magasin, Italian magazzino, Arabic makhazin plural of makhzan, khazana. Include dates."
}
```


## [2026-09-06T15:19:47.524Z] TOOL CALL #59: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%CE%B3%CE%AC%CE%B6%CE%B1",
 "prompt": "Give the Ancient Greek entry γάζα: meaning, etymology (Old Persian/Median ganza-?), and descendants (Latin gaza)."
}
```


### [2026-09-06T15:19:52.044Z] TOOL RESULT

```
# Etymology of Magazine

The word "magazine" traces back through several languages, beginning with its Arabic root. According to the Online Etymology Dictionary, the term originates from "Arabic _makhazin_, plural of _makhzan_ 'storehouse'" (1580s).

**Language Journey:**
- **Arabic**: _makhzan_ (storehouse) → _khazana_ (to store up)
- **Italian**: _magazzino_
- **Middle French**: _magasin_ (warehouse, depot, store)
- **English**: magazine (1580s)

**Meaning Evolution:**
The original sense referred to "warehouse, place for storing goods, especially military ammunition." By 1868, it meant "cartridge chamber in a repeating rifle," and by 1892, "a case in which a supply of cartridges is carried."

The modern publishing meaning emerged in 1731 with _Gentleman's Magazine_, drawing from the figurative sense of a publication as a "storehouse" of information—conceptually similar to earlier uses for "printed lists of military stores and information."
```


### [2026-09-06T15:19:52.899Z] TOOL RESULT

```
# Ancient Greek γάζα

**Meaning:** The word denotes a "treasury" or "treasure," and can also refer to "great riches" or "a large sum of money."

**Etymology:** The term originates from Old Median *ganǰam* ("treasure"), which spread through the administrative systems of the Achaemenid Empire. As the Wiktionary source notes, there is scholarly discussion about vowel length: "The Liddell-Scott-Jones dictionary marks the first α long in this word and all its derivatives, but if the second α is short (as the declension class leads us to expect), then the accentuation proves the first must also be short."

**Descendants:** The Ancient Greek word evolved into Latin *gaza*, representing a direct transmission of the term across classical languages. This Latin form subsequently influenced vocabulary in Romance languages and beyond.
```


## [2026-09-06T15:20:02.052Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PHD winj ===\"; grep -o \"wing[^ ]*\\|winj[^ ]*\\|wnc[^ ]*\" PHD.txt | head -20; echo; grep -n \"wanjidan\\|winǰ\" PHD.txt | head; echo \"=== NYB wnc ===\"; grep -n \"wnc\\|winj\" NYB_vol2_glossary.txt | head",
 "description": "Look for MP winj- in Pahlavi dictionaries"
}
```


### [2026-09-06T15:20:02.127Z] TOOL RESULT

```
=== PHD winj ===
wing
wing
wing
wing
wing
wing.
wing
wing,
wing.
wing,
wing.
wing
wing.
wing
wnc(y)t!
wing.
wing.
winged.
winged.
wing

=== NYB wnc ===
299:ahanün-ie ['hnwnc] now 574; — ... nē not yet 77". — MPrs ’hnwn ‘now’, ’hnwnc ny ‘not yet’ (S); NP hanüz.
3937:vanj- [wnc-] *to hold exactly, pres. pass. 3d p. sg.: dek i catrusvätak vanjihet [wneyhyt', restore the reading of M] a pot in which is contained (which holds) a quarter (?) 428-9. — NP gunjidan ‘to be contained or held; to hold exactly, to be filled’.
4106:iyöxtan [*NDYHWN-tn'] vēc- (vinj-, v. below) to detach, to separate, to sift, to remove: di véxt šusr his sperm was de- tached from him, with the gl. kū-š Suhr pat post ul Gmat that is: his sperm broke through his skin 5419-29; ātaxš haciš nē šāyet véxtan the fire (hidden in the plant) cannot break forth (from it) 95! (gl.); api-š hösak vest u hošet and its ears having been torn off (by the wind) it withers 12814-15 (uncertain, v. note below); v. also vecisn. — Av. (1312 sq.) vaék-, pres. vaéca-; Skr vic-, pres. vinakti ‘to sift, to winnow, to separate; to inquire, to con- sider’; Arm. lw. wié-em ‘to dispute, to debate’, več ‘discussion’, vičak, v. večak; Bal gécag ‘to sift? < vēc-, gécin, gēšin ‘sieve’ (Makrani, v. Geiger); NP béxtan bez- ‘to sift’. The pres. vinj- is only attest- ed by Cod. K in FrP 18: wync-, but read vij- = the other MSS; as this vb. is al- ways written ideographically in the texts the existence of vinj- in BP is not fully ascertained. However, Psht has winjal ‘to wash, to cleanse’; traces of vinj- in NP are perhaps bunjak ‘carded cotton’ (« *binjak < *vinjak); banjidan (for *binj-) ‘to cut to pieces’ (Steingass); possibly banj ‘one of two women who share a common husband’ < *vincä-, cf vēcak and nēm-vēcak. — [Note: — The Phl translation of 12814-15 is based on a Syriac text which is guite as obscure as the Hebr. original: 'grass on the roof which, as soon as the wind blows upon it, šālef and it withers’. The vb. ŠLP means ‘to extract, to pull, to draw a sword’, so the senses ‘to dry up, to languish’ and ‘to shoot up, to form blades and ears’ seem to be simply conjectured from our Ps. verse. Evidently the Prs. translator took Syr SLP in its ordinary sense ‘to extract, to pull’, and tried to make sense of its Phl. equivalent včatan to the best of his ability. He needed an obj. for it,
6298:dwhšy: duxt dwnb'wncy: Dumbavand gdy: Gai
```


## [2026-09-06T15:20:03.051Z] TOOL CALL #61: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%83%D9%86%D8%B2",
 "prompt": "Give the Arabic entry كنز: etymology (borrowed from Middle Persian/Parthian ganj?), meaning, plural كنوز."
}
```


### [2026-09-06T15:20:08.383Z] TOOL RESULT

```
# Arabic Entry: كنز (kanz)

**Etymology:** The word derives from Old Median *ganǰam* ("treasure"), a term spread by the Achaemenid administration and possibly mediated through Imperial Aramaic gnzʾ (*ganzā*, "treasure").

**Meaning:** "treasure" — a noun referring to valuable items or wealth.

**Plural:** كنوز (kunūz) — formed as a broken plural in Arabic.

The entry also documents two additional etymologies: a verb form meaning "to bury in the ground" or "to pile up/amass," and an adjective describing something with firm texture or carnous quality. Notably, this Arabic root generated descendants in European languages, including Spanish *alcancía* and Portuguese *alcanzia*.
```


## [2026-09-06T15:20:16.964Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nfor key in ['gazelle,  n.','gazette,  n.','genizah,  n.','magazine,  n.','Jasper,  masc.']:\n    i=t.find(key)\n    leaf=t[:i].count('\\f')\n    print(key,'leaf',leaf,'=> printed ~', (leaf-12)*2, 'or', (leaf-12)*2+1)\nEOF",
 "description": "Calibrate Klein page numbers"
}
```


### [2026-09-06T15:20:18.667Z] TOOL RESULT

```
gazelle,  n. leaf 348 => printed ~ 672 or 673
gazette,  n. leaf 348 => printed ~ 672 or 673
genizah,  n. leaf 350 => printed ~ 676 or 677
magazine,  n. leaf 495 => printed ~ 966 or 967
Jasper,  masc. leaf 446 => printed ~ 868 or 869
```


## [2026-09-06T15:20:42.602Z] TOOL CALL #63: WebFetch

```json
{
 "url": "https://www.ahdictionary.com/word/search.html?q=gazelle",
 "prompt": "Give the American Heritage Dictionary entry for gazelle, including its etymology line (French, Old French, Spanish, Arabic ghazal)."
}
```


### [2026-09-06T15:20:46.952Z] TOOL RESULT

```
# Gazelle Entry from American Heritage Dictionary

**Definition:**
"Any of various small, swift antelopes of the genus *Gazella* and related genera of Africa and Asia, characteristically having a slender neck and ringed horns."

**Etymology:**
The entry traces the word's origin as "[French, from Old French, from Arabic *ġazāl*.]"

Note: The page content provided does not include Spanish in the etymology line—only French, Old French, and Arabic sources are listed.
```


## [2026-09-06T15:20:48.598Z] TOOL CALL #64: Bash

```json
{
 "command": "for u in \"https://www.etymonline.com/word/gazelle\" \"https://www.etymonline.com/word/gazette\" \"https://www.etymonline.com/word/magazine\" \"https://en.wiktionary.org/wiki/%DA%AF%D9%86%D8%AC\" \"https://en.wiktionary.org/wiki/%D8%AC%D9%86%D8%A7%D8%B2%D8%A9\" \"https://en.wiktionary.org/wiki/%D8%AE%D8%B2%D9%86\" \"https://en.wiktionary.org/wiki/%D9%85%D8%BA%D8%A7%D8%B2%D9%87\" \"https://en.wiktionary.org/wiki/%CE%B3%CE%AC%CE%B6%CE%B1\" \"https://en.wiktionary.org/wiki/%D9%83%D9%86%D8%B2\" \"https://en.wiktionary.org/wiki/%DA%AF%D9%86%D8%AC%DB%8C%D8%AF%D9%86\"; do timeout 120 python3 tools/fetch_source.py \"$u\" --note \"page 218, roots Ghazal / Gzn (ganj): gazelle, gazette, magazine, ganj, janaza, khazana, magaza, gaza, kanz, gonjidan\" 2>&1 | tail -2; done",
 "description": "Archive web sources"
}
```


### [2026-09-06T15:20:54.239Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/0b4da0e06ca1ff58.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f076f4c21148aa74.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d1dcd1d1998db336.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/eb4a82e76eccc24a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/23d4c43089fa3430.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/576754e68e24ffbc.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/dfc1eb209c539ab3.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e5c92da6368ab789.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/6b961ea378a60d86.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/bcf05234aaa2599b.txt
```


## [2026-09-06T15:21:04.446Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA && python3 - <<'EOF'\nt=open('PLA_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint('leaves',len(t))\nfor leaf in (122,123,124):\n    print('==== leaf',leaf,'(printed',leaf-15,') ====')\n    print(' '.join(t[leaf-1].split())[:1200])\nEOF",
 "description": "Asbaghi page 108"
}
```


### [2026-09-06T15:21:06.222Z] TOOL RESULT

```
leaves 302
==== leaf 122 (printed 107 ) ====
harbanda 107 argäha 0>_> - harbanda: "Eseltreiber" aus pers. -s.> barbande I aus pers. > bar mp.) xar "Esel" +0» bande "Diener, Sklave" <Tmp.»u bandag — ap. bandaka. GN_> -barbandi: "Eseltreiben" s. harbanda. au,» - harbandiyya: Pl. v. Sa» barbandi s. harbandi, &> - burraf: "Ranzen" aus pers. LS kuräz (über das Aramäische ins Ar.). Slr> - hardädi: "Wein" aus dem pers. »I,» xordäd 2 mp. ww» harvatat < aw. haurvatat 3, «Py>- hurdaßi: "Kleinwarenhändler" aus dem pers. „> hord "klein". a&y>- hurdafiyya: Pl. v. hurdafi. Jr - hardal: "Senf" pers. a ?., syr., misch. bayn®. er - barzahraf: "Nerium Oleander" aram. ge» 6, aus dem pers.go,> harzahre. ou.» - huristän: "Wandschrank" pers. 7 wahrscheinlich aus dem pers. > bör v. Verb hordan +olL. istan Suffix des Ortes vgl. bustän,u. ähnl, we - bars: "Erbsen" pers, aus dem pers. L» harba_?. @#- hard: "Erbsen" = hars 8, ab,» - bargäha: "Zelt" pers. aus dem pers. el hargah mp. xar- gäh am. xara + gätu / ap. gädu. 1. Wahrmund s. v. 2. Muhit s. v. 3. Nyberg Bd. II s. v. 4, Muhit s. v. 5. Löw s. v. 6. ebda. 7. Muhit s. v. 8. ebda.
==== leaf 123 (printed 108 ) ====
harkäha 108 azan ankls - harkäha = hargäha s. hargäha. fr?- burram: "froh" aus dem pers. „»borram < mp. ). xurram. >53 - harmandiyya: "Eseltreiber, Eselbesitzer" s.. #..> barbandiyya.! ans. burramiyya: "Sekte der an Seelenwanderung glaubenden u. locker lebenden" pers. ? <T mp ._ une xurramih "Fröhlichkeit" °, - bazz: "Seidenware, Biberhaare" pers. 4 aus dem pers, » hbaz <Tmp,er 5 xaz ”. oler_ hazaq: ein Ort in Isfahan 6, ol - hazzän: "Sammler" nom. agent. v. hazan s. hazan. Par PR Aul)s- bazäna: "Schatz" u. kanz stammen aus dem pers. gang mp. tr ganj, paz. ganz, mprth. gzn, aram. Lw. gnz’ o#ll2_ hazäyin: Pl. v. “ls hazäna s. hazäna. ur bazar: "Kaspisches Meer". &L - bazränag: "eine Art Bekleidung" pers. 7 ?. Or - hazän: "sammeln" ist nach Jefferys "Foreign Vocabulary of Qoran" ein denom. Verb, welches v. vielen westl. Sprachwissen- schaftlern als Lw. im Ar. angesehen wurde 8, Hoffmann schlägt in einem Artikel in ZDMG BD. 32 S. 760 vor, Seinen Pi Ursprung im persischen & gand zu suchen « 1. Muhit s. v. 2. Wahrmund s. v. 3. Farawa$i s. v. 4. TaCälivi figh al-luga S. 198, Fraenkel s. v. 5. Mackenzie s. v. 6. al-MuCarrab s. v. 7. ebda, Muhit s. v. 8. Jeffery s. v.
==== leaf 124 (printed 109 ) ====
azan 109 bistag M. E. könnte hazan seinen Ursprung im pers, ii» hazine mp. >rsı uzenag 1 haben. IS - Hazandär: "Schatzmeister" pers. 2, 22» - hazüz: Pl. v. > bazz s. bazz. „Is 5 - hazindär = bazandär s. hazandär. us busrü: "Titel des Perserkönigs" mp. ner husrav am. xusrav, > skr. sushravas 3 ar. PM kasrä, syr. aan * alu - busruwäni; "feine Seide" Nisba v. busrü pers. 5, vba - busrüdärü: "ein Heilmittel", aus pers. »Y!>2--> busrüdärü <T MP. (Ps por busrüdäru. 2 2-5 - husrüsäbür: eine Stadt im Iran, aus dem pers._ “Li, > busrü- $ähpür Tmp.Iteruu ‚Der busrü-$ähpühr Taw. xu-srav + ap. xSayadiya "König" + aw. puöra / ap. puga "Sohn" „Le - ba$är: "das Kratzen" eine Metathese v. pers. vb» aras s. baras 7, yo. An =ız ur - basäf: "Scherbett, Sorbet" aus dem pers. zi2> bösäb "Fruchtsaft" 8 mp. sr xwaß +wäp Taw. 2p. as - hißtaßa: "Flachs, Seide; Achselzwickel" aus dem pers. us hidtak - biätag = biftafa s. hiätaßa 9 1. Mackenzie s. v. 2. Muhit s. v. 3. Bartholomae S. 1378. 4. Brockelmann s. v. 5. al-MuCarrab s. v. 6. ebda, Nyberg Bd. II s. v. 7. Kiyä s. v. 8. Wahrmund s. v., Chista Bd. 10. Ss. v. 9. ebda, Muhit s. v.
```


## [2026-09-06T15:21:34.513Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('SKT.txt',encoding='utf-8',errors='replace').read()\ni=t.find('French  from  Italian')\nprint('leaf of origin-lists', t[:i].count('\\f'))\n# find Spanish list\nfor key in ['Spanish','Arabic']:\n    j=t.find(key, i-4000, i+8000)\n    print(key,'at',j)\nseg=t[i-3000:i+4000]\nprint(' '.join(seg.split())[:3500])\nEOF",
 "description": "Skeat appendix language lists"
}
```


### [2026-09-06T15:21:36.322Z] TOOL RESULT

```
leaf of origin-lists 635
Spanish at 2551052
Arabic at 2552462
or, cortege, costume, countertenor, ttiraos. douclie. ducal. e>cort, esplanade, icade. florin, fracas, fugue, gabion, gambol, Viproviae, incatoadiiie, infantry, lavender, Itestring, macaroon ?, manage, manege, ben. mizcn, (.mizzcn), modeU motet, msket, niche, ortolan, paladi'i, palette, ftUet (3), parapet, partisan \\)t pastel, rruke, pilaster, piniiacc, piston, pomade ^mmoile), pontoon, ix>puUce, porcelain, D&lillion. preconcert, rtpnsal, revolt, rocket 1), aalad, sallct, salmagundi, saveloy (ccr* pifts), scamper, Bentinel?, sentry 1, somer- lult (Somerset), sonnet, spinet, squad. Buadron. termagant, terrace, tramontane, Ironiontoiie, umber, vault (1), vcdcltc fkietlc>. Aiso crtmaiion* l^Htck from Frenth from Italian from ttUtn: pcnwig. ishambfe ^,t/fr^l, wig. Otrman from Itaiian from Latin : Brouche Spanish from Iiatln : alligator, rnt'i la, armadillo, b->oby, capsize, car- Dnodo, cask, commodore, comrade, cork, yunc>an, di>riiibo^ue, domino, don (j). lennOy dulcimer, flotilla, funambnlist, imbado, grandee, hi<IaIgo, jade i.'). jnato, to^ las>o. manchincel. matador, merino, ilo (mosquito), negio, olio, pay (3), Uo, pnmcTo. punctilio, quadroon. real (a\ renegade (rcncgado^, salver. ■hcrTy, ■tcvrdore. tent V3), tornado, ultramarine, vanilla, venndnh. French from Spanish from Latin-, ca- lenture, Creole, doubloon, escalade, far- thingale (fordingalc), grenade, ogre, ombre, parade, paragon, jx^tronel, pint, punt (.3), quadrille, risk, so&safros, spaniel, tartan?. Fortugnefle from Ijatin: binnncle. caste, jnitk (. i), moidorc, molasses, pimento, port ^4), tank. Frenth from Portugutst from Latin \ corvtltc, fetich (fetish), parasol. Dutch from liattn: buoy, tafTerel (taffrail). OU Dutch from Latin : chop (a), BciLndinaYian from T»atin : cake, skate (tV Scandinavian from Englijhfrom Latin : kindle. German from Iiatln: drilling French from Did High German frcm^ Latin : w.i.sie. Fremkfrom Teutonic from Latin : pamp-1 (i)T. Dutch from German from Latini rum- mer T. Celtic from Latin : ingle, pot, spigot Russian from Latin: czar. French from Portugueu from Arabic from Gretk from I-atin: apricot French from Spanish from Arabic from Latin; quintal. IjOw Latin: baboon, barrister, cam paniform, cap, capital (3), dominion, edi- ble, elongate, elucidate, cmtiossy, fine {i\ flask, flavour, funeral, grate (i), hosi, hocus-pocus, imptemcntf indent, intimidate, pageant, plenary, proxy. French from Ijnu Latin : »ba<«. ballet, barbican, bargain, baas ( 1 ), bittern, boiagc, burden (3'), burl, camlet, canton, cape (O, cope (I), cygnet, felon?, ferret (i), festival. tlat;on, frock, gash, gauge ^age), gouge^ hntch, oleander, palfrey. French from Provenfal from Low Latin : ballad. French from Italian from Lew Latin : basement, bassoon, pivot. French from S/anish from Low Latin t capanson. 5« Wordfl of GREEK origin ; mc p. 603. We must also include the following [Zmv Latin from latin from Greek: Inoc IJfalt'an /ram la/w /rem Greek : ba- lustrade, grotto, madu^il, tt\xvi, vaata^,. torso. Fr*n<\ fn^m Italian /rgm Lal^tv jvoi 6o6 VI, DISTRIBUTION OF WORDS, ETC. Creek: canopy, cornice, espalier, gerawnder, grotesque, pt&stre. Dutch Jrom Italian from Latin from Creek: sketch. Spanish from Latin from Gretki bttflklo, ■cochineal, moms, pellitory («) (peHeler), '«avuina (i>iivannah). French from Spanish from Latin from Creek I maroon (i), rumb (rhumb). Pifrtugi*ese from Latin from Greek ; cockroach, palaver. French from Fortugiuse from Latin from Greek: marmalade. Frove
```


## [2026-09-06T15:21:50.130Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== WEB gazelle ===\"; grep -n -o \"gazelle[^.]\\{0,200\\}\" WEB_vol1.txt | head -4; echo \"=== WEB gazette ===\"; grep -n -o \"ga\\.zette[^.]\\{0,250\\}\\|gazette, n[^.]\\{0,250\\}\" WEB_vol1.txt | head -4; echo \"=== SKT magazine ===\"; grep -n -o \"Magazine[^.]\\{0,200\\}\" SKT.txt | head -4",
 "description": "Webster and Skeat extra checks"
}
```


### [2026-09-06T15:21:52.021Z] TOOL RESULT

```
=== WEB gazelle ===
4906:gazelle
5438:gazelle
5438:gazelle
10853:gazelle, Gazella dama, of Asia and Pee É A/ri-és, n
=== WEB gazette ===
80707:gazette, ne prob
=== SKT magazine ===
10886:Magazine
```


## [2026-09-06T15:21:55.033Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '80700,80720p' WEB_vol1.txt; echo \"=== SKT magazine line ===\"; sed -n '10884,10890p' SKT.txt",
 "description": "Webster gazette and Skeat magazine"
}
```


### [2026-09-06T15:21:55.112Z] TOOL RESULT

```
horns, and large, lus-
trous soft eyes;
cially the Gazelle dor-
cas of North Africa.
Gaz-el-li/nae, 2.p~l. a group of antelopes which the gazelle is the ce
gāz’ēr, n. one who gazes. 3
ga-zet’, n. [It.] a copper coin formerly issued the Venetian Republic. [Obs.] k
ga-zette’, n. [It. gazzetta, a gazette, ne prob. from gazzeľta, a gazet or sma price paid for the paper; also om gazzetta, a magpie, and terer or tattler.] 1, a newspaper; a printed sheet
containing an account t EEA E then 2 me t
se, bull 3 ; ; ull, brite, tärn, up; cry, myth; cat, maching, ace, church, chord; gem, añger, (Fr.) bon, as; this, thin; azure
gazette
2. any of several official newspapers of Great Britain, containing announcements and bulletins, as of appointments and promotions in the Horua service, of public honors award- ed, of bankrupts, etc.
gazette’, v.t.; gazetted, pt, pp.; gazetting,
Š per. to publish, announce, or list in a gazette;
ence, to announce formally, as an appoint-
“ment to the public service. gaz-et-teer’, n. [It. gasselliere, a writer of news,
from gazella, a gazette.]
1. a writer of news for a gazette, or an officer appointed to publish a gazette.
2. a ee a newspaper. [Obs.]
3. a book containing geographical names and descriptions, alphabetically arranged; a geographical dictionary or index.
g4z/ing-stock, n. a person or thing gazed at; an object of curiosity or contempt.
=== SKT magazine line ===
name,  due  to  the  existence  of  such  terms madtx-jc/va,  honeysuckle  (lit.  moth wood),  madrrdHitiv,  worxibine  (lit  molV bush),  madrt-pcrla,  mother  of  pearl.  Hcri ma*frt  is  from  L.  mafrtm,  ace  <4  maftf mother;  see  Mother.  Pora  U  from  Gl wSipoz,  a.  light  friable  stone,*  also  a  stalid tile.  ^  Itut  the  word  has  certainly  bed mtdefstaiHi  (prob.  misundtrttocd)  as  coa nccted  witn  pert,  whence  na  merool scientific  terms  such  as  taitm-pora.  tnbi pora^  dfnti-fora. gtmmUporn,  'Scientific' etymology  is  usually  clumsy,  and  frC quently  wrong.  We  may  conclude  t E.  fere  has  been  substituted  for  Gk. by  conftision.
Madrigal,  a  pastoral  song.  (Ilal.  — L Gk.)  Iial.  madrigaU,  i  short  song, pastoral  ditty  ;  put  for  mandn\fa/i Florio  also  gives  mardfia/i,  mandnan* a  hetdftiuan,  also  a  madrigal.  —  Ital, mandra,  a  herd,  flock.  —  L.  ntandra stall,  stable.- Gk.  ^f?/>a.  a  foM -f  Ski matidura,  stable;  frum  mand,  to  slcef (The  suffix  -ijc^-aU"  1.   MiTix  -ft  a/u.)
Magazine.    (F.-lu1.«Aiab.)     O ma^iin  (F.  wtagasin).'^\iiL a  storehouse.  —Arab,    makhdam,    pi. maihzatt,  a  storehouse.  —  Arab.  AMmsH, laying  up  in  store.
Maggot,  a  gnib.  (W.)  M  E.  magpi ma^t.  —  W.  moi-fiad,  matai,  a  mi^i^ cf.  magiaid,  grubs.  Allied  to  W.  mapai breeding,  ma<^d,  a  brood  ;  from  magu^  (I breed,     Cf.  Bret,  and  Com.  m^fit,  to  feed
Magi,  priests  of  the  Per<^ianv  (U— Gl •  Pcrs,)  L.  magi,  pi.  — Gk.  >m7«>i,  pL ^Ytff,  a  Ma^n,  one  of  a  Medisn  triW also  an  enchanter,  properly  a  wise who  interpreted  dreams.  Tbe  orig. was  prob.  great,  Irom  Zend allied  to  L.  maptHS,  Gk n$ag-ic,  short  for  mai^i:  ati ;  tna^-ii4^m.
Magistrate ;  sec  Macnitude.
Magnanimity,  Magnate ;  see nituda.
```


## [2026-09-06T15:22:47.634Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== MON ghazal ===\"; grep -n \"غزاله\\|غزال:\" MON_part1.txt MON_part2.txt | head -8; echo \"=== MON magaze ===\"; grep -n \"مغازه\" MON_part1.txt MON_part2.txt | head -5; echo \"=== MON jenazeh ===\"; grep -n \"جنازه:\" MON_part1.txt MON_part2.txt | head -5",
 "description": "Grep Mo'in for ghazal, magaze, jenazeh"
}
```


### [2026-09-06T15:22:47.802Z] TOOL RESULT

```
=== MON ghazal ===
MON_part2.txt:1621:غزال: 222« [غ.] (ا.) آهو بره» آهو. (کن.) 
MON_part2.txt:1622:غزال: 72222 [ع.] (ص.) ریسسمان تاب؛ 
MON_part2.txt:1626:غزاله: (م-)۱2221-2 [ع.] ۱( آهو بر ماده؛ 
MON_part2.txt:1627:ج. غزالات. آفتاب. غزالهً فلکك: (کن.) 
MON_part1.txt:82685:(کد.) قد و بالای معشوق. شاخ غزال: شاخ 
=== MON magaze ===
MON_part1.txt:2630:مغازه سلمانی. 
MON_part1.txt:27782:بادو مغازه. بادو نانوابیی. در حمام‌های قدیم 
MON_part1.txt:36245:خانه با مغازه نصب کنند. تخته سباه که در 
MON_part1.txt:52299:حانوت: 205۰ (ع.] (.) دکان» مغازه. کلبه؛ 
MON_part1.txt:90480:خرید از مغازه یا آنچه در مهمانخانه و 
=== MON jenazeh ===
```


## [2026-09-06T15:23:00.967Z] TOOL CALL #70: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg218.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/218.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/ | tail -5",
 "description": "Save page image for audit"
}
```


### [2026-09-06T15:23:01.046Z] TOOL RESULT

```
-rw-rw-r--  1 sfmqrb sfmqrb  90918 Sep  5 10:16 92.png
-rw-rw-r--  1 sfmqrb sfmqrb  93420 Sep  5 10:18 94.png
-rw-rw-r--  1 sfmqrb sfmqrb  78178 Sep  5 10:14 95.png
-rw-rw-r--  1 sfmqrb sfmqrb  72929 Sep  5 10:19 96.png
-rw-rw-r--  1 sfmqrb sfmqrb  65608 Sep  5 10:43 99.png
```


## [2026-09-06T15:25:02.428Z] TOOL CALL #71: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk218.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\n\nW_ETYM_GAZELLE = \"https://www.etymonline.com/word/gazelle\"\nW_ETYM_GAZETTE = \"https://www.etymonline.com/word/gazette\"\nW_ETYM_MAGAZINE = \"https://www.etymonline.com/word/magazine\"\nW_GANJ = \"https://en.wiktionary.org/wiki/%DA%AF%D9%86%D8%AC\"\nW_JANAZA = \"https://en.wiktionary.org/wiki/%D8%AC%D9%86%D8%A7%D8%B2%D8%A9\"\nW_KHAZANA = \"https://en.wiktionary.org/wiki/%D8%AE%D8%B2%D9%86\"\nW_MAGAZE = \"https://en.wiktionary.org/wiki/%D9%85%D8%BA%D8%A7%D8%B2%D9%87\"\nW_GAZA = \"https://en.wiktionary.org/wiki/%CE%B3%CE%AC%CE%B6%CE%B1\"\nW_KANZ = \"https://en.wiktionary.org/wiki/%D9%83%D9%86%D8%B2\"\nW_GONJIDAN = \"https://en.wiktionary.org/wiki/%DA%AF%D9%86%D8%AC%DB%8C%D8%AF%D9%86\"\nW_AHD = \"https://www.ahdictionary.com/word/search.html?q=gazelle\"\n\nNOT_CHECKED_FVA = lambda r: {\"ref\": r, \"status\": \"not_checked\",\n    \"note\": \"FVA = S.M. Nahvi, Farhang-e Vazheha-ye Arabi dar Farsi (1368/1989). refs_online.json records that no digital copy exists on any permitted platform (archive.org, ketabnak, noorlib all searched); catalogue record only. Not consultable.\"}\n\ndoc = {\n  \"pdf_page\": 218,\n  \"book_page\": 188,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-06\",\n  \"entries\": []\n}\n\n# ------------------------------------------------------------------ entry 1\ne1 = {\n  \"entry\": 1,\n  \"root\": \"Ğ.z.l, Ghazâl\",\n  \"verdict\": \"confirmed\",\n  \"modern_form\": \"Arabic غَزَال ġazāl 'gazelle, fawn' (root غ-ز-ل), a native Arabic/Semitic word\",\n  \"note\": \"The root box is correct in substance: Arabic ġazāl is the ordinary word for the young of the gazelle/antelope, and every Western etymological dictionary that traces English gazelle stops at exactly this Arabic word — Klein p.644 'gazelle, n. — F., fr. ghazel, N. African pronunciation of Arab. ghazāl'; AHD online 'French, from Old French, from Arabic ġazāl'; Lokotsch no. 699 'Gazelle, Antilope dorcas'. Nourai's gloss 'a new born deer, a wild goat' renders the Arabic lexicographers' definition (Lane: a young gazelle, from birth until it is strong) accurately enough; 'wild goat' is loose but is how the older European Arabists (Devic, Pihan) paraphrased it. Note that the triliteral غ-ز-ل also yields ġazal 'spinning; love-poetry', which is a different lexeme and is not implicated here. The one weak spot on this chart is not the root but the page reference SKT:209, which in our copy of Skeat's Concise Dictionary is in the H section, not at gazelle.\",\n  \"note_fa\": \"جعبهٔ ریشه درست است: «غَزال» واژه‌ای عربی (سامی) از ریشهٔ غ-ز-ل به معنی «بچه‌آهو، آهوی جوان» است و همهٔ فرهنگ‌های ریشه‌شناختی غربی زنجیرهٔ gazelle انگلیسی را دقیقاً به همین واژهٔ عربی می‌رسانند؛ کلاین (ص ۶۴۴) می‌نویسد «فرانسوی، از ghazel، تلفظ شمال‌آفریقایی عربی ghazāl» و فرهنگ American Heritage نیز «فرانسوی < فرانسوی باستان < عربی ġazāl». معنایی که نورایی داده («بچه‌آهوی نوزاد، بز کوهی») برگردان آزادِ تعریف لغویان عرب است؛ بخش «بز کوهی» دقیق نیست ولی همان تعبیری است که عرب‌شناسان قدیم اروپا (دُویک، پیهان) به کار می‌بردند. توجه شود که از همین ریشهٔ غ-ز-ل واژهٔ «غزل» (ریسندگی؛ شعر عاشقانه) نیز ساخته شده که واژه‌ای جداگانه است و ربطی به این نمودار ندارد. تنها لغزش این صفحه در ارجاع SKT:209 است که در نسخهٔ در دسترسِ فرهنگ اسکیت به بخش حرف H می‌افتد، نه به مدخل gazelle.\",\n  \"sources\": [W_ETYM_GAZELLE, W_AHD],\n  \"ref_check\": [NOT_CHECKED_FVA(\"FVA:209\")],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"1966 ed. p.644 (KLN_1966.txt leaf 348, line 15884)\", \"stance\": \"supports\",\n     \"note\": \"'gazelle, n. — F., fr. ghazel, N. African pronunciation of Arab. ghazdl [= ghazāl].' Klein stops at the Arabic word, exactly as the root box does.\"},\n    {\"src\": \"LKT\", \"where\": \"no. 699 (LKT.txt line 1719), Ar. ġazāl\", \"stance\": \"supports\",\n     \"note\": \"\\\"'Gazelle, Antilope dorcas Licht.'; die nordafrikanische Aussprache hat Imāla, also gazel; hieraus sp. gacela, pg. gazella, frz. gazelle, it. gazzella, rum. gazelä; engl. gazelle, ndl. gazel, dtsch. Gazelle\\\" — Arabic head-word, Romance forms derived from it.\"},\n    {\"src\": \"DEV\", \"where\": \"s.v. Gazelle (DEV.txt line 1389)\", \"stance\": \"supports\",\n     \"note\": \"\\\"Gazelle. Esp. gacela, gacele, gacel, autref. algacel; portug. gazella, ital. gazzella. De l'arabe ghazâl, même sens.\\\"\"},\n    {\"src\": \"PHN\", \"where\": \"s.v. GAZELLE (PHN.txt lines 5179-5180)\", \"stance\": \"supports\",\n     \"note\": \"'GAZELLE, s. f. (a.) [ghazâl] antilope, gazelle, féminin [ghazâlat]' — Pihan lists it among the French words of Arabic origin.\"},\n    {\"src\": \"AHD\", \"where\": \"ahdictionary.com s.v. gazelle\", \"stance\": \"supports\",\n     \"note\": \"'[French, from Old French, from Arabic ġazāl.]' — supports the Arabic etymon; note that AHD gives no Spanish stage.\"}\n  ],\n  \"nodes\": []\n}\n\ne1[\"nodes\"].append({\n  \"id\": 1, \"lang\": \"Persian\", \"words\": \"ğazâl; Ğazâleh\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"Both words are straightforward Arabic loans in New Persian, taken over with the script unchanged: غزال ġazāl 'gazelle, antelope' and its feminine غزاله ġazāla 'doe-fawn', which in classical Persian poetry also became a kenning for the sun (the sun 'grazing' over the sky) and thence a woman's name. Mo'in's Farhang marks both with the tag [ع.] 'Arabic': 'غزال [ع.] (اِ.) آهو بره، آهو' and 'غزاله [ع.] ۱) آهو بره ماده … آفتاب. غزالهٔ فلک'. There is no sound change to describe — Persian keeps the Arabic ġayn, the long ā and the final -a > -eh; the only Persianisation is the pronunciation of tāʾ marbūṭa as -eh. The Hātef Esfahānī couplet quoted in the box ('تو آن وحشی غزال…') uses the word in exactly this borrowed sense.\",\n  \"derivation_fa\": \"هر دو واژه وام‌واژهٔ عربی در فارسی نو هستند و بی هیچ دگرگونی آوایی و خطی به فارسی آمده‌اند: «غزال» به معنی آهو و آهوبره و مؤنث آن «غزاله» به معنی آهوبرهٔ ماده که در شعر فارسی کنایه از خورشید («غزالهٔ فلک») و سپس نام زنان شده است. معین در فرهنگ فارسی هر دو را با نشانهٔ [ع.] (عربی) آورده است: «غزال [ع.] (اِ.) آهو بره، آهو» و «غزاله [ع.] آهو برهٔ ماده … آفتاب». تنها تغییر، خواندن تاء مربوطه به صورت «ـه» فارسی است؛ غین و الف کشیده دست‌نخورده مانده‌اند. ادعای نورایی درست است.\",\n  \"sources\": [W_AHD],\n  \"ref_check\": [NOT_CHECKED_FVA(\"FVA:297\")],\n  \"consulted\": [\n    {\"src\": \"MON\", \"where\": \"MON_part2.txt lines 1621, 1626 (s.vv. غزال، غزاله)\", \"stance\": \"supports\",\n     \"note\": \"'غزال: [ع.] (اِ.) آهو بره، آهو' and 'غزاله: [ع.] ۱) آهو بره ماده؛ … آفتاب. غزالهٔ فلک' — Mo'in tags both as Arabic loans and records the 'sun' sense that makes Ġazāleh a name.\"},\n    {\"src\": \"KLN\", \"where\": \"1966 ed. p.644\", \"stance\": \"supports\",\n     \"note\": \"Klein's 'Arab. ghazāl' is the same word Persian borrowed; Klein does not treat the Persian reflex, but nothing in him conflicts.\"},\n    {\"src\": \"LKT\", \"where\": \"no. 699 (LKT.txt line 1719)\", \"stance\": \"silent\",\n     \"note\": \"Lokotsch lists only the European reflexes of Ar. ġazāl, not the Persian loan.\"}\n  ]\n})\n\ne1[\"nodes\"].append({\n  \"id\": 2, \"lang\": \"Spanish\", \"words\": \"gacele\",\n  \"verdict\": \"plausible\",\n  \"derivation\": \"Arabic ġazāl entered Ibero-Romance through Andalusi Arabic, where the North-African imāla raised ā to ē (Lokotsch: 'die nordafrikanische Aussprache hat Imāla, also gazel'); Old Spanish shows the word both with and without the Arabic article — algacel, gacel, gacele — and modern Spanish settled on gacela. Nourai's 'gacele' is therefore a real (if minor) Spanish variant and not an invention: Devic lists it explicitly ('Esp. gacela, gacele, gacel, autref. algacel'), and it is cross-referenced again in his index ('Gacele, esp. voy. Gazelle'). The verdict is only 'plausible' rather than 'confirmed' because the head-form of the Spanish word is gacela, and because the Spanish stage is itself optional in the modern accounts: Etymonline says French gazelle came 'probably via Spanish', while AHD and Klein take the word straight from Arabic into Old French.\",\n  \"derivation_fa\": \"«غزال» عربی از راه عربی اندلسی به زبان‌های شبه‌جزیرهٔ ایبری رفت؛ در تلفظ مغربی، «اماله» الفِ کشیده را به «ی» نزدیک می‌کرد (لوکوچ: تلفظ شمال‌آفریقایی با اماله، یعنی gazel) و از همین‌رو در اسپانیایی کهن هم صورت با حرف تعریف (algacel) و هم بی آن (gacel، gacele) دیده می‌شود؛ صورت رایج امروزی gacela است. پس «gacele» که نورایی آورده گونه‌ای واقعی و کم‌کاربرد است نه ساختگی: دُویک آن را صریحاً فهرست کرده («Esp. gacela, gacele, gacel, autref. algacel»). با این‌همه چون صورت اصلی اسپانیایی gacela است و چون خودِ حلقهٔ اسپانیایی در منابع امروزی قطعی نیست (اتیمانلاین «احتمالاً از راه اسپانیایی» و کلاین و AHD یکسره از عربی به فرانسوی)، این گره «با احتیاط پذیرفتنی» است.\",\n  \"sources\": [W_ETYM_GAZELLE, W_AHD],\n  \"ref_check\": [{\"ref\": \"SKT:209\", \"status\": \"not_found\",\n    \"note\": \"Checked the Google/archive.org scan of Skeat's Concise Etymological Dictionary (SKT.txt). The gaze/gazelle/gazette block sits on leaf 195 (its garbled OCR still shows '…from Ital. gaz[z]etta … [gazza], a magpie …'), which on this scan's offset is printed p. ~172-175; printed p.209 falls on leaf ~229, whose visible page footer is '206' and whose entries are HOARSE, HOB, HOCK, HOLD, HOLE — i.e. the H section. So p.209 of this edition does not contain gazelle. Skeat's actual entry does support the chain (his origin-lists on pp.605-606 classify such words 'French from Spanish from Arabic'), but the cited page number cannot be confirmed for the edition on disk.\"}],\n  \"consulted\": [\n    {\"src\": \"DEV\", \"where\": \"s.v. Gazelle and index s.v. Gacele (DEV.txt lines 1389, 3501)\", \"stance\": \"supports\",\n     \"note\": \"'Esp. gacela, gacele, gacel, autref. algacel' and 'Gacel, esp. voy. Gazelle. Gacela, esp. voy. Gazelle. Gacele, esp. voy. Gazelle.' — the exact form Nourai prints is attested.\"},\n    {\"src\": \"LKT\", \"where\": \"no. 699 (LKT.txt line 1719)\", \"stance\": \"partial\",\n     \"note\": \"'die nordafrikanische Aussprache hat Imäla, also gazel; hieraus sp. gacela, pg. gazella, frz. gazelle' — gives Spanish gacela (not gacele) and derives French directly from the Arabic, in parallel with Spanish rather than through it.\"},\n    {\"src\": \"SKT\", \"where\": \"SKT.txt leaf 195 (G section) and the origin-lists on printed pp.605-606\", \"stance\": \"partial\",\n     \"note\": \"The gazelle entry is present in the G block but the OCR of that leaf is unreadable; the appended 'distribution of words' lists show Skeat's habit of routing such words 'French from Spanish from Arabic'.\"}\n  ]\n})\n\ne1[\"nodes\"].append({\n  \"id\": 3, \"lang\": \"French\", \"words\": \"gazel\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"gazel is the genuine Old French form: Etymonline dates 'Old French gazel' to the 14th century and derives modern French gazelle from it, the -elle being the ordinary French feminine/diminutive remodelling of a masculine loan. Klein reaches the same form from the other side — 'F., fr. ghazel, N. African pronunciation of Arab. ghazāl' — so the -el of the French word reflects the imāla vowel of Maghribi Arabic ġazēl, not a French innovation. Whether the word reached French through Spanish (Etymonline: 'probably via Spanish', which is Nourai's arrow) or directly from Arabic through the Crusades and the Maghreb trade (AHD, Klein) is not settled, but the form itself is exactly right.\",\n  \"derivation_fa\": \"«gazel» صورت اصیل فرانسوی باستان است: اتیمانلاین آن را از سدهٔ چهاردهم میلادی ثبت کرده و gazelle فرانسوی نو را برآمده از آن می‌داند؛ پسوند ‑elle همان مؤنث‌ساز/تصغیرساز معمول فرانسوی است که بر وام‌واژهٔ مذکر نشسته است. کلاین از سوی دیگر همین صورت را از عربی می‌گیرد: «فرانسوی، از ghazel، تلفظ شمال‌آفریقایی عربی ghazāl»؛ یعنی «ـِل» پایانیِ واژهٔ فرانسوی بازتاب امالهٔ عربی مغربی (ġazēl) است نه نوآوری فرانسوی. اینکه واژه از راه اسپانیایی به فرانسوی رسیده باشد (نظر نورایی و «احتمالاً» اتیمانلاین) یا یکسره از عربی (کلاین و AHD) قطعی نیست، ولی خودِ صورت کاملاً درست است.\",\n  \"sources\": [W_ETYM_GAZELLE],\n  \"ref_check\": [{\"ref\": \"KLN:644\", \"status\": \"supports\",\n    \"note\": \"KLN_1966.txt leaf 348 (= printed p.644 on the offset that puts genizah, leaf 350, on the p.648 Nourai cites): 'gazelle, n. — F., fr. ghazel, N. African pronunciation of Arab. ghazdl.' Klein's page is exactly the one cited, and it carries the French stage.\"}],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"1966 ed. p.644\", \"stance\": \"supports\", \"note\": \"See ref_check — French form with the Maghribi imāla vowel.\"},\n    {\"src\": \"DEV\", \"where\": \"s.v. Gazelle (DEV.txt line 1389)\", \"stance\": \"supports\",\n     \"note\": \"Devic's article groups the French word with 'Esp. gacela, gacele, gacel', i.e. the Ibero-Romance forms, which is Nourai's route.\"},\n    {\"src\": \"PHN\", \"where\": \"s.v. GAZELLE (PHN.txt line 5179)\", \"stance\": \"supports\",\n     \"note\": \"Pihan's 'Dictionnaire étymologique des mots de la langue française dérivés de l'arabe' has GAZELLE as an Arabic-derived French word, from [ghazâl].\"}\n  ]\n})\n\ne1[\"nodes\"].append({\n  \"id\": 4, \"lang\": \"English\", \"words\": \"Gazelle\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"English gazelle is first recorded c. 1600, borrowed straight from French gazelle with no change beyond the English stress and vowel; the OED/Etymonline chain is 'c. 1600, from French gazelle, from Old French gazel (14c.), probably via Spanish, ultimately from North African pronunciation of Arabic ghazal'. The American Heritage Dictionary — the very book Nourai cites — gives '[French, from Old French, from Arabic ġazāl.]' The English word carried the Linnaean genus name Gazella with it into scientific usage.\",\n  \"derivation_fa\": \"واژهٔ انگلیسی gazelle نخستین بار حدود سال ۱۶۰۰ میلادی به کار رفته و مستقیم از gazelle فرانسوی گرفته شده است، بی هیچ دگرگونی جز جای تکیه و کیفیت واکه. اتیمانلاین زنجیره را چنین می‌دهد: «حدود ۱۶۰۰، از فرانسوی gazelle، از فرانسوی باستان gazel (سدهٔ ۱۴)، احتمالاً از راه اسپانیایی، سرانجام از تلفظ شمال‌آفریقاییِ عربی ghazāl». همان فرهنگ American Heritage که نورایی به آن ارجاع داده می‌نویسد «[فرانسوی، از فرانسوی باستان، از عربی ġazāl]». ادعای نورایی درست است.\",\n  \"sources\": [W_ETYM_GAZELLE, W_AHD],\n  \"ref_check\": [{\"ref\": \"AHD:547\", \"status\": \"supports\",\n    \"note\": \"The New College Edition's main word-list p.547 falls in the G's; we could not open that printed page (the local AHD file is only the Watkins IE-roots appendix, in which 'gazelle' does not and should not appear, the word being Semitic). The AHD entry itself, read online at ahdictionary.com, reads: 'gazelle … [French, from Old French, from Arabic ġazāl.]' — i.e. AHD supports the French > English step Nourai draws, though it gives no Spanish stage.\"}],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"1966 ed. p.644\", \"stance\": \"supports\", \"note\": \"'gazelle, n. — F., fr. ghazel …' — French as the immediate donor of the English word.\"},\n    {\"src\": \"WEB\", \"where\": \"WEB_vol1.txt s.v. gazelle (lines 4906, 10853)\", \"stance\": \"supports\",\n     \"note\": \"Webster's Twentieth Century keeps the same word and defines it 'especially the Gazella dorcas of North Africa'.\"},\n    {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt\", \"stance\": \"silent\",\n     \"note\": \"grep 'gazelle' in the Watkins IE-roots appendix returns nothing — expected, since the word is a Semitic loan, not an IE inheritance.\"}\n  ]\n})\n\ndoc[\"entries\"].append(e1)\njson.dump(doc, open('/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/part1.json','w',encoding='utf-8'), ensure_ascii=False, indent=1)\nprint(\"entry1 nodes:\", len(e1[\"nodes\"]))\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk218.py",
 "description": "Build entry 1 of verification JSON"
}
```


### [2026-09-06T15:25:05.330Z] TOOL RESULT

```
entry1 nodes: 4
```


## [2026-09-06T15:33:23.103Z] TOOL CALL #72: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk218b.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\nP='/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/'\ndoc=json.load(open(P+'part1.json',encoding='utf-8'))\n\nW_ETYM_GAZETTE = \"https://www.etymonline.com/word/gazette\"\nW_ETYM_MAGAZINE = \"https://www.etymonline.com/word/magazine\"\nW_GANJ = \"https://en.wiktionary.org/wiki/%DA%AF%D9%86%D8%AC\"\nW_JANAZA = \"https://en.wiktionary.org/wiki/%D8%AC%D9%86%D8%A7%D8%B2%D8%A9\"\nW_KHAZANA = \"https://en.wiktionary.org/wiki/%D8%AE%D8%B2%D9%86\"\nW_MAGAZE = \"https://en.wiktionary.org/wiki/%D9%85%D8%BA%D8%A7%D8%B2%D9%87\"\nW_GAZA = \"https://en.wiktionary.org/wiki/%CE%B3%CE%AC%CE%B6%CE%B1\"\nW_KANZ = \"https://en.wiktionary.org/wiki/%D9%83%D9%86%D8%B2\"\nW_GONJIDAN = \"https://en.wiktionary.org/wiki/%DA%AF%D9%86%D8%AC%DB%8C%D8%AF%D9%86\"\n\nNONE_REF = {\"ref\": \"(none printed)\", \"status\": \"not_checked\",\n            \"note\": \"Nourai gives no reference for this box; the claim was checked against the other books instead (see consulted).\"}\nFVA = lambda r: {\"ref\": r, \"status\": \"not_checked\",\n    \"note\": \"FVA = Nahvi, Farhang-e Vazheha-ye Arabi dar Farsi (1368/1989); refs_online.json records that no digital copy exists on any permitted platform. Not consultable.\"}\nETM = lambda: {\"ref\": \"ETM:70\", \"status\": \"not_checked\",\n    \"note\": \"ETM = Abolghasemi, Risheh-shenasi (Etimoloji), Qoqnus 1374/1995; refs_online.json: no digital copy on any permitted platform (ketabnak listing without download). Not consultable.\"}\n\nSOD_CHECK = {\"ref\": \"SOD:182\", \"status\": \"supports\",\n  \"note\": \"Gharib, Sogdian Dictionary, entry 4552 on printed p.182 (SOD.txt line 37818; the page number 182 is printed on leaf 247 of SOD_pages.txt): '4552 γzn- B, M, C / γazn ① Parth. gzn; MP gnz ② nom. ob. -y(yk), acc. -w; loc. -yh / treasure'. The entry gives precisely Nourai's Parthian gzn 'treasure', and the neighbouring entries 4553 γznβr 'treasurer', 4554 γznyʾ 'treasury'.\"}\n\ne2 = {\n  \"entry\": 2,\n  \"root\": \"Gzn\",\n  \"verdict\": \"plausible\",\n  \"modern_form\": \"Old Median *ganǰa-/*ganza- 'treasure' (Parthian gzn = ganz, Middle Persian gnz/ganj, Sogdian γzn); not of Proto-Indo-European date\",\n  \"note\": \"The form, the language label and the gloss are all supported by the reference Nourai cites: Gharib's Sogdian Dictionary p.182 s.v. γzn- gives 'Parth. gzn; MP gnz — treasure'. What is questionable is making Parthian the head of the family. Every modern authority makes the source a MEDIAN word carried across the empire by the Achaemenid administration: Hübschmann, Persische Studien pp.231-232, groups ganj with Ganjak and birinj and concludes 'Dann sind diese Wörter nicht persischen, sondern (wie Ganjak vermuthen lässt) medischen Ursprungs'; Nyberg's glossary s.v. ganj refers to Mayrhofer, 'Reste von Medisch' 13ff.; Jeffery p.251 quotes Lagarde to the same effect ('an old Median word'); Wiktionary reconstructs Old Median *ganǰam for both Greek γάζα and Arabic كنز. Greek gaza in particular was borrowed in the 5th-4th c. BCE from the Achaemenid chancery, centuries before any Parthian could have transmitted it, so the arrow root→Greek cannot literally run through Parthian. Note also that Parthian ⟨gzn⟩ and Middle Persian ⟨gnz⟩ are two graphic orders of the same *ganz-; the -zn/-nz alternation is orthographic, not a real metathesis. The root is therefore right as a word but mislabelled as to which Iranian language is the ancestor.\",\n  \"note_fa\": \"صورت، برچسب زبانی و معنای جعبهٔ ریشه با همان منبعی که نورایی آورده تأیید می‌شود: قریب در فرهنگ سغدی، ص ۱۸۲، ذیل γzn- می‌نویسد «پارتی gzn؛ فارسی میانه gnz — گنج». آنچه جای چون‌وچرا دارد این است که پارتی سرِ خانواده شمرده شده. پژوهش امروزی سرچشمه را واژه‌ای مادی می‌داند که دیوان هخامنشی آن را در سراسر شاهنشاهی پراکنده است: هوبشمان در «پژوهش‌های پارسی» صص ۲۳۱–۲۳۲ گنج را در کنار «گنجه» و «برنج» می‌نهد و نتیجه می‌گیرد که «این واژه‌ها نه پارسی، بلکه مادی‌اند»؛ نیبرگ در واژه‌نامهٔ خود ذیل ganj به «بازمانده‌های مادی» ماریوفر ارجاع می‌دهد؛ جفری (ص ۲۵۱) از لاگارده نقل می‌کند که «واژه‌ای کهن مادی» است؛ ویکی‌واژه نیز برای γάζα یونانی و «کنز» عربی صورت مادی باستان *ganǰam را بازسازی می‌کند. به‌ویژه γάζα یونانی در سدهٔ پنجم–چهارم پیش از میلاد از دیوان هخامنشی وام گرفته شده، یعنی سده‌ها پیش از آنکه پارتیان بتوانند ناقل آن باشند. افزون بر این، ⟨gzn⟩ پارتی و ⟨gnz⟩ فارسی میانه دو ترتیب نگارشی از یک *ganz- هستند و این جابه‌جایی، قلبِ آوایی نیست بلکه خطی است. پس ریشه از نظر واژه درست است ولی برچسب زبانی آن نادقیق است.\",\n  \"sources\": [W_GANJ, W_GAZA, W_KANZ],\n  \"ref_check\": [SOD_CHECK],\n  \"consulted\": [\n    {\"src\": \"HUB\", \"where\": \"Persische Studien pp.231-232 (HUB.txt lines 8266-8280)\", \"stance\": \"partial\",\n     \"note\": \"'ganj \\\"Schatz\\\" (5. Jhd.) = np. ganj, phl. ganj … skr. LW. ganja-, gr. γάζα, syr. … \\\"Schatz\\\" … Hatten diese Wörter urspr. nz …? Dann sind diese Wörter nicht persischen, sondern (wie Ganjak vermuthen lässt) medischen Ursprungs.' — same word, but Median, not Parthian, is the head.\"},\n    {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II, glossary s.v. ganj (NYB_vol2_glossary.txt line 1624)\", \"stance\": \"partial\",\n     \"note\": \"'ganj [gnc\\\\'] treasury … — MPrs gnz (A-H II); Paz. ganž (SGV); NP ganj; MPrth gzn (A-H III) gzng (MHC); Arm. lw. ganj; Aram. lw. gnzʾ, gnzk; Gr. lw. γάζα. Mayrhofer, RekMed 13 sqq.' — Nyberg confirms Parthian gzn but files the whole set under Mayrhofer's Median residues.\"},\n    {\"src\": \"PLA\", \"where\": \"Asbaghi, Persische Lehnwörter im Arabischen p.108 (PLA_pages.txt leaf 123)\", \"stance\": \"supports\",\n     \"note\": \"s.v. ḫazāna: '\\\"Schatz\\\" u. kanz stammen aus dem pers. ganǰ, mp. ganj, paz. ganz, mprth. gzn, aram. Lw. gnzʾ' — 'mprth. gzn' is Nourai's root form verbatim.\"},\n    {\"src\": \"PHD\", \"where\": \"MacKenzie, Concise Pahlavi Dictionary s.v. ganj (PHD.txt line 378)\", \"stance\": \"supports\",\n     \"note\": \"'ganj [gnc | (M gnz), N ~] treasure, treasury. ~war [-wbl | M -wr, N ~] treasurer.' — Manichaean MP spelling gnz beside book-Pahlavi gnc.\"}\n  ],\n  \"nodes\": []\n}\n\nN=e2[\"nodes\"]\n\nN.append({\n  \"id\": 1, \"lang\": \"Pahlavi\", \"words\": \"ganj\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"Middle Persian ganj 'treasure, treasury' is written ⟨gnc⟩ in book Pahlavi and ⟨gnz⟩ in Manichaean Middle Persian (MacKenzie, Concise Pahlavi Dictionary: 'ganj [gnc | (M gnz), N ~] treasure, treasury'); the Parthian cognate is ⟨gzn⟩, and both continue Old Median *ganǰa-/*ganza-. Nyberg's glossary sets out the whole set: 'ganj … MPrs gnz; Paz. ganž; NP ganj; MPrth gzn … Arm. lw. ganj; Aram. lw. gnzʾ; Gr. lw. γάζα'. The derived agent noun ganjwar 'treasurer' (MacKenzie s.v.) is the form behind the Aramaic gizbarā and the name Gaspar/Jasper further down this chart. The chart's own NOTE, that FVQ suspects a Median origin, is exactly right — Jeffery p.251 cites Lagarde, 'an old Median word which passed later into Iranian and thence to India' — but that note belongs to Jeffery's p.251 (kanz), not to the p.122 Nourai cites here.\",\n  \"derivation_fa\": \"«گنج» در فارسی میانه ganj «گنج، خزانه» است که در پهلوی کتابی ⟨gnc⟩ و در فارسی میانهٔ مانوی ⟨gnz⟩ نوشته می‌شود (مکنزی: «ganj [gnc | مانوی gnz] گنج، خزانه»)؛ همتای پارتی آن ⟨gzn⟩ است و هر دو دنبالهٔ *ganǰa-/*ganza- مادی باستان‌اند. نیبرگ همهٔ خانواده را یک‌جا آورده است: «ganj … فارسی میانه gnz؛ پازند ganž؛ فارسی نو گنج؛ پارتی میانه gzn … وام‌واژهٔ ارمنی ganj؛ وام‌واژهٔ آرامی gnzʾ؛ وام‌واژهٔ یونانی γάζα». مشتق آن ganjwar «گنجور، خزانه‌دار» (مکنزی) همان صورتی است که «گیزبَرا»ی آرامی و نام Gaspar/Jasper در پایین همین نمودار از آن برخاسته‌اند. یادداشت خودِ کتاب که «جفری این واژه را احتمالاً برگرفته از ریشه‌ای مادی می‌داند» درست است (جفری ص ۲۵۱ به نقل از لاگارده: «واژه‌ای کهن مادی»)، ولی این نکته در ص ۲۵۱ اوست نه در ص ۱۲۲ که نورایی ارجاع داده است.\",\n  \"sources\": [W_GANJ],\n  \"ref_check\": [\n    {\"ref\": \"BQT:1841\", \"status\": \"supports\",\n     \"note\": \"Borhan-e Qate' p.1841 (rendered with tools/ref_page.py BQT:1841, pdf p.638 of BQT_v3): the گنج-family page, whose Mo'in footnotes read '۵ – از: گنج + ور var … پهلوی ganjwar' and '۶ – تحریف گنجویر ganjebar پهلوی بمعنی خزانه‌دار، گنجور … گنجک، کنز، غزنه–غزنین'. Mo'in's footnote on the previous cited page (1838, n.1) gives the etymology outright: 'پهلوی ganǰ، ارمنی ganj، آرامی ginzā، ganzā، عربی کنز kanz. نیبرگ ص ۷۷'.\"},\n    {\"ref\": \"FVQ:122\", \"status\": \"partial\",\n     \"note\": \"Jeffery p.122 is the entry ḵazāna, not ganj; it does reach Persian ganj on the following page ('This [ganj] … is cognate with Skt. gañja a treasury or jewel room, and has been borrowed through the Aram. גנזא; Syr. … into Arabic as كنز', FVQ p.123). The Median claim Nourai's NOTE attributes to FVQ is on p.251 n.1: 'Lagarde, Arm. Stud. 453, thinks that it is an old Median word which passed later into Iranian and thence to India.' So the substance is Jeffery's, but not on p.122.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"PHD\", \"where\": \"MacKenzie s.v. ganj (PHD.txt line 378)\", \"stance\": \"supports\",\n     \"note\": \"'ganj [gnc | (M gnz), N ~] treasure, treasury. ~war [-wbl | M -wr, N ~] treasurer.'\"},\n    {\"src\": \"NYB\", \"where\": \"Nyberg II, glossary s.v. ganj (line 1624)\", \"stance\": \"supports\",\n     \"note\": \"'ganj [gnc\\\\'] treasury 72.10816 etc. — MPrs gnz; Paz. ganž; NP ganj; MPrth gzn; Arm. lw. ganj; Aram. lw. gnzʾ, gnzk; Gr. lw. γάζα.'\"},\n    {\"src\": \"HUB\", \"where\": \"Persische Studien p.232 (HUB.txt line 8272)\", \"stance\": \"supports\",\n     \"note\": \"'ganj \\\"Schatz\\\" (5. Jhd.) = np. ganj, phl. ganj Gl. and Ind. 274, skr. LW. ganja-, gr. γάζα' — with the Median conclusion two lines later.\"}\n  ]\n})\n\nN.append({\n  \"id\": 2, \"lang\": \"Persian\", \"words\": \"ganj; gonjândan\",\n  \"verdict\": \"disputed\",\n  \"derivation\": \"The first word is impeccable: NP گنج ganj continues MP ganj without change (Mo'in's footnote to Borhan p.1838 n.1: 'پهلوی ganǰ، ارمنی ganj، آرامی ginzā، ganzā، عربی کنز kanz'), and so do the box's extras گنجور ganjūr 'treasurer' (< ganj + -war/-ūr, Borhan p.1841 n.5, MP ganjwar) and گنجه ganjeh 'chest, cupboard' (Borhan p.1841 n.7 'نیز گنجه، بمعنی قفه و دولابچه'). The second word does NOT belong here. گنجیدن/گنجاندن 'to be contained / to make fit', and with them گنجایش 'capacity', continue a completely different Iranian verb: Middle Persian wanj-/winj- ⟨wnc-⟩ 'to be contained', with the regular New Persian change of initial w- to g- (as in wišādan > gušādan, wizīdan > guzīdan, wirēxtan > gurēxtan). Nyberg's glossary states it outright — 'vanj- [wnc-] to hold exactly … — NP gunjidan \\\"to be contained or held\\\"' — and Cheung's Etymological Dictionary of the Iranian Verb p.434 sets up the root *u̯iač- 'to contain' with BMP wnc- /winj-/, NP gunjidan/gunj-, NP gunj 'volume', Wakhi wic-, Shughni wiz- and Sanskrit vyac- 'to contain, encompass'. The homophony with ganj is accidental; Mo'in himself (Borhan p.1841 n.10) derives گنجیدن from a separate head-word گنج (with u, 'capacity'), which is that same *winj-. Verdict for the node = the worst of its words.\",\n  \"derivation_fa\": \"واژهٔ نخست بی‌عیب است: «گنج» فارسی نو دنبالهٔ ganj فارسی میانه است (حاشیهٔ معین بر برهان قاطع، ص ۱۸۳۸، پانوشت ۱: «پهلوی ganǰ، ارمنی ganj، آرامی ginzā، ganzā، عربی کنز») و همچنین‌اند «گنجور» (گنج + ور، برهان ص ۱۸۴۱ پانوشت ۵، پهلوی ganjwar) و «گنجه» به معنی قفه و دولابچه (همان‌جا پانوشت ۷). ولی واژهٔ دوم به این خانواده تعلق ندارد: «گنجیدن/گنجاندن» و «گنجایش» دنبالهٔ فعل دیگری در ایرانی‌اند، یعنی wanj-/winj- فارسی میانه ⟨wnc-⟩ «جا گرفتن»، با همان تبدیل قاعده‌مندِ «و» آغازین به «گ» در فارسی نو (وشادن > گشادن، وزیدن > گزیدن، ورختن > گریختن). نیبرگ صریح می‌گوید: «vanj- [wnc-] درست جا گرفتن … فارسی نو گنجیدن»، و چونگ در فرهنگ ریشه‌شناختی فعل ایرانی (ص ۴۳۴) ریشهٔ *u̯iač- «جا گرفتن» را با wnc- فارسی میانهٔ مانوی، gunjidan فارسی نو، wic- وخی و vyac سنسکریت («فراگرفتن») می‌آورد. همانندی آوایی «گنج» و «گنجیدن» تصادفی است؛ خودِ معین (برهان ص ۱۸۴۱ پانوشت ۱۰) گنجیدن را از مدخل جداگانهٔ «گُنج» می‌گیرد که همان *winj- است. پس دربارهٔ «گنجاندن» پژوهش امروزی ادعای نورایی را رد می‌کند.\",\n  \"sources\": [W_GANJ, W_GONJIDAN],\n  \"ref_check\": [\n    {\"ref\": \"BQT:1838\", \"status\": \"supports\",\n     \"note\": \"Borhan p.1838 (ref_page.py BQT:1838, pdf p.635 of BQT_v3), Mo'in's footnote 1 to گنج: 'پهلوی ganǰ، ارمنی ganj، آرامی ginzā، ganzā، عربی کنز kanz. نیبرگ ص ۷۷' — Pahlavi > New Persian exactly as drawn, plus the Arabic and Aramaic offshoots that Nourai draws elsewhere on this page.\"},\n    {\"ref\": \"BQT:1841\", \"status\": \"partial\",\n     \"note\": \"The same page carries گنجور (n.5 'از: گنج + ور var … پهلوی ganjwar') and گنجه (n.7), which support the box's extras; but footnote 10 handles گنجیدن under a separate head-word ('گنجیدن — بضم اول … از: گنج (ه.م.) + یدن'), i.e. Mo'in does not derive it from ganj 'treasure' either.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"CHEUNG\", \"where\": \"Etymological Dictionary of the Iranian Verb p.434, root *u̯iač- (CHEUNG.txt lines 28068-28085, index 41052)\", \"stance\": \"contradicts\",\n     \"note\": \"'*u̯iač \\\"to contain\\\": MIDDLE PERSIAN BMP wnc- /winj-/, (pass.) wncyh- … NWIR: NP gunjidan/gunj- \\\"to be contained\\\", NP gunj \\\"volume\\\" … SANSKRIT vyac \\\"to contain, embrace, encompass\\\"' — گنجیدن is from *u̯iač-, not from ganj.\"},\n    {\"src\": \"NYB\", \"where\": \"Nyberg II, glossary s.v. vanj- (NYB_vol2_glossary.txt line 3937)\", \"stance\": \"contradicts\",\n     \"note\": \"'vanj- [wnc-] *to hold exactly, pres. pass. 3d p. sg.: dēg ī čatrusvātak vanjihēd a pot … which holds a quarter … — NP gunjidan \\\"to be contained or held; to hold exactly, to be filled\\\".'\"},\n    {\"src\": \"PHD\", \"where\": \"MacKenzie s.v. ganj (PHD.txt line 378)\", \"stance\": \"supports\",\n     \"note\": \"For ganj: 'ganj [gnc | (M gnz), N ~] treasure, treasury' — the 'N ~' explicitly equates the New Persian form.\"},\n    {\"src\": \"MON\", \"where\": \"Mo'in's footnotes as printed in BQT pp.1838, 1841\", \"stance\": \"partial\",\n     \"note\": \"Supports ganj/ganjūr/ganjeh; keeps گنجیدن under a different head-word.\"}\n  ]\n})\n\nN.append({\n  \"id\": 3, \"lang\": \"English\", \"words\": \"Jasper 1\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"The male name Jasper (beside Caspar, Gaspar, Kaspar) has nothing to do with the mineral jasper (that is Greek íaspis, a Semitic word); it is the name traditionally given to one of the three Magi and goes back to Middle Persian ganzabara / ganjwar 'treasurer' (ganj 'treasure' + -bara 'bearer'), Aramaic gizbarā, which entered the Christian East as Gaspar and reached English through Latin and Dutch/German. Klein states it in as many words: 'Jasper, masc. PN. — A name of Persian origin. Jas-per lit. means \\\"treasure holder\\\". The first element of this compound name is traceable to Pers. ganj, \\\"treasure\\\". See genizah and cp. Gaspar.' Lokotsch (no. 1059) spells out the compound: 'Aus dem pers. Grundwort und pers. Suffix -bār \\\"Träger\\\" ergibt sich *gazbār \\\"Schatzträger, -meister\\\" und hieraus Kaspar, der König aus dem Morgenlande.' Funk & Wagnalls, the reference Nourai cites, glosses the name '[Per., treasurer.]' — Nourai's box verbatim. Strictly the English name descends from the compound ganjwar/ganzabara rather than from bare ganj, which is the only nuance the arrow hides.\",\n  \"derivation_fa\": \"نام مردانهٔ Jasper (و گونه‌های Caspar، Gaspar، Kaspar) هیچ پیوندی با سنگ «یَشم/jasper» ندارد (آن از íaspis یونانی و سامی‌تبار است)؛ این نام همان نام یکی از سه مغِ داستان میلاد است و به ganzabara/ganjwar فارسی میانه «گنجور، خزانه‌دار» (گنج + ‑بَر «برنده») و gizbarā آرامی بازمی‌گردد که در مسیحیت شرقی Gaspar شد و از راه لاتین و هلندی/آلمانی به انگلیسی رسید. کلاین صریح می‌نویسد: «Jasper، نام خاص مذکر — نامی ایرانی‌تبار؛ Jas-per تحت‌اللفظ یعنی دارندهٔ گنج؛ جزء نخست آن به فارسی ganj بازمی‌گردد». لوکوچ (شمارهٔ ۱۰۵۹) ترکیب را باز می‌کند: «از واژهٔ پایهٔ فارسی و پسوند ‑بار «برنده» صورت *gazbār «گنج‌بر، خزانه‌دار» به دست می‌آید و از آن Kaspar، همان شاهِ خاورزمین». فانک و واگنالز، همان مرجعی که نورایی آورده، نام را چنین تفسیر می‌کند: «[فارسی، خزانه‌دار]». تنها نکتهٔ ناگفته آن است که نام از ترکیبِ «گنجور» آمده نه از «گنجِ» تنها.\",\n  \"sources\": [],\n  \"ref_check\": [{\"ref\": \"FSD:1313\", \"status\": \"supports\",\n    \"note\": \"Funk & Wagnalls New Standard Dictionary, vol. II, the Jasper column (FSD_vol2.txt leaf 607): the entry gives the cognate name-forms 'Kas'per‡; F. Gas\\\"pard'; G. Cas'par; It. Gas'pa-ro; L. Gas'par; Pg. Sp. Gas-par'; Sw. Kas'per' and the bracketed etymology '[Per., treasurer.]' (line 63482) — Nourai's gloss verbatim. This OCR has no printed page numbers, so the cited page 1313 itself could not be read off the scan, but the entry is unmistakable.\"}],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"1966 ed. s.v. Jasper, masc. PN (KLN_1966.txt leaf 446, line 20185)\", \"stance\": \"supports\",\n     \"note\": \"'Jasper, masc. PN. — A name of Persian origin. Jas-per lit. means \\\"treasure holder\\\". The first element of this compound name is traceable to Pers. ganj, \\\"treasure\\\". See genizah and cp. Gaspar.' (The preceding entry, 'jasper, n., an opaque variety of quartz', is expressly a different, Semitic word — which is why Nourai numbers his box 'Jasper 1'.)\"},\n    {\"src\": \"LKT\", \"where\": \"no. 1059, Ar. kanz (LKT.txt line 2516)\", \"stance\": \"supports\",\n     \"note\": \"'Aus dem pers. Grundwort und pers. Suffix -bār \\\"Träger\\\" [Horn NpEt S.36, Nr.158] ergibt sich *gazbār \\\"Schatzträger, -meister\\\" und hieraus Kaspar, der König aus dem Morgenlande.'\"},\n    {\"src\": \"FSD\", \"where\": \"vol. II, s.v. Gaspard (FSD_vol2.txt line 30180)\", \"stance\": \"supports\",\n     \"note\": \"'… Kings of Cologne. See under KING. 2, same as Jasper.' — Funk & Wagnalls itself equates Gaspar/Jasper and ties the name to the Magi ('the Three Kings of Cologne').\"}\n  ]\n})\n\nN.append({\n  \"id\": 4, \"lang\": \"Arabic\", \"words\": \"kanz\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"Arabic كَنْز kanz 'treasure' (pl. كنوز kunūz) is one of the best-attested Iranian loans in the Qur'anic lexicon. Jeffery, Foreign Vocabulary of the Qur'an p.251, is categorical: 'Some of the Muslim authorities take it as genuine Arabic … but it was well known to the early philologers that it was a foreign word and it is noted as such by al-Jawāliqī, Muʿarrab 133; ath-Thaʿālibī, Fiqh 317; al-Khafājī 170, all of whom give it as Persian [ganj] … That it was originally Iranian is certain. Paz. ganz; Phlv. ganj means treasury … It is most probable that the word came direct from Middle Persian into Arabic, though j for [z] might point to Aram. influence.' Wiktionary reconstructs the source as Old Median *ganǰam, 'spread by the Achaemenid administration and possibly mediated through Imperial Aramaic gnzʾ'. Phonetically Iranian g- is regularly rendered by Arabic k- (there being no g in Arabic), and the cluster -nǰ- is resolved as -nz-; the borrowing is pre-Islamic, since kanz appears in Qur'an ix,34 and xviii,81.\",\n  \"derivation_fa\": \"«کَنْز» عربی (جمع: کنوز) از شناخته‌شده‌ترین وام‌واژه‌های ایرانی در واژگان قرآنی است. جفری در «واژگان بیگانهٔ قرآن» ص ۲۵۱ قاطعانه می‌نویسد: «برخی از لغویان مسلمان آن را عربی اصیل شمرده‌اند … ولی زبان‌شناسان کهن به‌خوبی می‌دانستند که واژه‌ای بیگانه است و جوالیقی در المعرّب (۱۳۳)، ثعالبی در فقه‌اللغة (۳۱۷) و خفاجی (۱۷۰) همگی آن را فارسی [گنج] دانسته‌اند … ایرانی‌بودن آن قطعی است. پازند ganz؛ پهلوی ganj به معنی خزانه … به‌احتمال بسیار واژه مستقیم از فارسی میانه به عربی رفته است، هرچند «ز» در برابر «ج» شاید نشان اثرگذاری آرامی باشد». ویکی‌واژه سرچشمه را *ganǰam مادی باستان می‌داند که «دیوان هخامنشی آن را پراکنده و شاید آرامی شاهنشاهی (gnzʾ) واسطهٔ آن بوده است». از نظر آوایی، «گ» ایرانی در عربی همواره به «ک» بدل می‌شود (زیرا عربی «گ» ندارد) و خوشهٔ ‑نج به ‑نز می‌گراید. وام‌گیری پیش از اسلام است، چون «کنز» در قرآن (توبه ۳۴، کهف ۸۱) آمده است.\",\n  \"sources\": [W_KANZ],\n  \"ref_check\": [\n    {\"ref\": \"FVQ:251\", \"status\": \"supports\",\n     \"note\": \"FVQ_pages.txt leaf 268 = printed p.251, the entry كنز: 'Treasure … it was well known to the early philologers that it was a foreign word … all of whom give it as Persian [ganj] … That it was originally Iranian is certain. Paz. ganz; Phlv. ganj means treasury, and the word has been widely borrowed, cf. Skt.; Arm.; Baluchi ganj; Gk. γάζα; Sogd. γnz.' Footnote 1 adds Lagarde's 'old Median word' — the source of the chart's NOTE.\"},\n    {\"ref\": \"ARB:297\", \"status\": \"supports\",\n     \"note\": \"al-Jawāliqī, al-Muʿarrab (ARB_mo3rb.txt, باب الكاف, lines 21120-21175): the head-word list of the kāf chapter includes 'وقال … في «الكنز» أنه فارسي معرّب', and the editor Aḥmad Shākir's footnote objects, '«الكنز» من الألفاظ القرآنية، وردت فيه مراراً … وهي كلمة عربية بحتة، لم يدّعِ عجمتها غير المؤلف فيما أعلم' — i.e. Jawāliqī does list kanz as an arabized Persian word, exactly as Nourai claims. This OCR has no page breaks, so the printed page 297 of the Tehran/Shākir edition could not be verified directly (Jeffery cites the same passage as 'Muʿarrab 133' in a different edition).\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"PLA\", \"where\": \"Asbaghi p.108 (PLA_pages.txt leaf 123), s.v. ḫazāna\", \"stance\": \"supports\",\n     \"note\": \"'ḫazāna: \\\"Schatz\\\" u. kanz stammen aus dem pers. ganǰ, mp. ganj, paz. ganz, mprth. gzn, aram. Lw. gnzʾ.'\"},\n    {\"src\": \"LKT\", \"where\": \"no. 1059 (LKT.txt lines 2514-2515)\", \"stance\": \"supports\",\n     \"note\": \"'1059. Ar. kanz: \\\"Schatz\\\" [aus pers. ganǰ, ZDMG L, 647/648] und kanzija \\\"dass.\\\"; hieraus sp. alcancía \\\"Sparbüchse\\\" …'\"},\n    {\"src\": \"BQT\", \"where\": \"Borhan-e Qateʿ p.1838 n.1 (Mo'in)\", \"stance\": \"supports\",\n     \"note\": \"'پهلوی ganǰ … عربی کنز kanz' — Mo'in lists Arabic kanz among the offshoots of Pahlavi ganj.\"},\n    {\"src\": \"KLN\", \"where\": \"1966 ed. p.648 s.v. genizah\", \"stance\": \"supports\",\n     \"note\": \"Klein derives the whole Aramaic/Hebrew/Arabic set (ginzā, gazzā, janaza) from 'Pers. ganj, treasure'.\"}\n  ]\n})\n\nN.append({\n  \"id\": 5, \"lang\": \"Persian\", \"words\": \"kanz\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"This is the round trip: the Arabic loan كنز kanz (with its Arabic broken plural كنوز kunūz, the box's extra) came back into literary Persian as a learned Arabism, so that Persian now has both the inherited گنج ganj and the re-borrowed کنز kanz side by side — a classic doublet. Mo'in's Farhang marks it as such: 'کنز: [معر. گنج] (اِ.) گنج، گنجینه' — 'kanz: [arabicized form of ganj] (noun) treasure, treasury'. Nourai's arrow (Arabic → Persian) and his Persian spelling كَنز with fatḥa are both right; the word is chiefly Qur'anic and juristic in Persian usage (e.g. in the title Kanz al-ʿummāl).\",\n  \"derivation_fa\": \"این گره نمونهٔ روشنِ «رفت و برگشت» واژه است: «کنز» عربی — که خود معرّبِ «گنج» است — همراه جمع مکسّر عربی‌اش «کنوز» دوباره به فارسی ادبی بازگشت، چنان‌که امروز فارسی هم «گنج» موروثی را دارد و هم «کنز» وام‌گرفتهٔ دوباره را؛ این دو، دوگانهٔ (doublet) یکدیگرند. معین در فرهنگ فارسی همین را می‌گوید: «کنز: [معر. گنج] (اِ.) گنج، گنجینه». پیکان نورایی (از عربی به فارسی) و املای «کَنز» او هر دو درست است؛ کاربرد این واژه در فارسی بیشتر قرآنی و فقهی است (مانند نام کتاب «کنز العمّال»). ادعای نورایی درست است.\",\n  \"sources\": [W_KANZ],\n  \"ref_check\": [{\"ref\": \"MON:3096\", \"status\": \"supports\",\n    \"note\": \"Mo'in, Farhang-e Farsi, s.v. کنز (found in MON_part2.txt line 27177 = the same text in the Adena two-volume abridgement): 'کنز: [معر. گنج] (اِ.) گنج، گنجینه' — 'arabicized form of ganj'. The abridged scan carries no page numbers, so p.3096 of the six-volume Amir Kabir edition could not be verified directly, but the entry says precisely what the arrow claims.\"}],\n  \"consulted\": [\n    {\"src\": \"MON\", \"where\": \"MON_part2.txt line 27177 s.v. کنز\", \"stance\": \"supports\", \"note\": \"'[معر. گنج]' = 'arabicized ganj'.\"},\n    {\"src\": \"FVQ\", \"where\": \"p.251 s.v. كنز\", \"stance\": \"supports\",\n     \"note\": \"Jeffery's account of kanz as an Iranian word in Arabic underwrites the Persian re-borrowing of the Arabic form.\"},\n    {\"src\": \"BQT\", \"where\": \"Borhan p.1841 n.6\", \"stance\": \"partial\",\n     \"note\": \"Mo'in's cross-reference chain on the گنج page runs 'گنجک … کنز … غزنه–غزنین', linking ganj and kanz.\"}\n  ]\n})\n\nN.append({\n  \"id\": 6, \"lang\": \"Arabic\", \"words\": \"x.z.n; maxzan; maxâzin\",\n  \"verdict\": \"plausible\",\n  \"derivation\": \"Arabic خزن ḵazana 'to store up', with مخزن maḵzan 'storehouse' (pl. مخازن maḵāzin) and خزانة ḵizāna 'treasury', is genuinely contested. Nourai's cited authority backs him: Asbaghi, Persische Lehnwörter im Arabischen p.108, writes 'ḫazāna: \\\"Schatz\\\" u. kanz stammen aus dem pers. ganǰ, mp. ganj, paz. ganz, mprth. gzn, aram. Lw. gnzʾ', and adds that Hoffmann (ZDMG 32, 760) sought the origin of ḫazan in Persian ganj. But Jeffery, whom Nourai also cites here, rejects precisely that: 'It seems hardly likely that by another line of borrowing … it has come to form the Ar. ḵazāna. Barth, Etymol. Stud. 51, makes the happier suggestion that it may be connected with the form that is behind the Heb. ḥōsen \\\"treasure\\\"' (FVQ p.123). Wiktionary and the standard Arabic lexica treat خ ز ن as an ordinary Semitic root with a full verbal paradigm, and Dozy, Devic, Lammens and Skeat all derive maḵzan from ḵazana without any Iranian element. Two further points count against the arrow as drawn: nobody derives ḵazana from kanz (the parent box) — Asbaghi's two words are parallel loans from ganj, not one from the other — and the derivation would require both k > ḵ and a metathesis n-z > z-n. So: an old and still-defended idea, but not the majority view, and not by the route drawn.\",\n  \"derivation_fa\": \"دربارهٔ ریشهٔ عربی «خ‑ز‑ن» (خَزَنَ «انباشتن»، مَخزَن «انبار»، جمع مَخازِن، خزانه) اختلاف واقعی هست. مرجعی که خودِ نورایی آورده او را تأیید می‌کند: اصبغی در «وام‌واژه‌های فارسی در عربی» ص ۱۰۸ می‌نویسد «خزانه «گنج» و کنز هر دو از فارسی ganǰ (فارسی میانه ganj، پازند ganz، پارتی میانه gzn، وام‌واژهٔ آرامی gnzʾ) برآمده‌اند» و می‌افزاید که هوفمان (ZDMG ۳۲، ۷۶۰) ریشهٔ خزن را در «گنج» فارسی جسته است. ولی جفری — که نورایی به او هم ارجاع داده — درست همین را رد می‌کند: «چندان محتمل نمی‌نماید که از راه وام‌گیریِ دیگری … صورت خزانهٔ عربی پدید آمده باشد؛ پیشنهاد پسندیده‌تر از بارت است که آن را با صورتِ پشتِ «حُسن/حصن» عبری مربوط می‌داند» (ص ۱۲۳). ویکی‌واژه و فرهنگ‌های معیار عربی «خ ز ن» را ریشه‌ای سامی با صرف کامل می‌دانند، و دوزی، دُویک، لامنس و اسکیت همگی «مخزن» را بی هیچ عنصر ایرانی از «خزن» می‌گیرند. دو نکتهٔ دیگر نیز به زیان پیکانِ نمودار است: هیچ منبعی «خزن» را از «کنز» (جعبهٔ مادر) نمی‌گیرد — نزد اصبغی این دو، وام‌های موازی از «گنج»‌اند نه یکی از دیگری — و چنین اشتقاقی هم بدل ک > خ و هم قلبِ ن‑ز به ز‑ن می‌خواهد. پس: اندیشه‌ای کهن و هنوز مدافع‌دار، ولی نه نظر اکثریت و نه از این راه.\",\n  \"sources\": [W_KHAZANA, W_ETYM_MAGAZINE],\n  \"ref_check\": [\n    {\"ref\": \"PLA:108\", \"status\": \"supports\",\n     \"note\": \"Asbaghi p.108 (PLA_pages.txt leaf 123, the printed folio number '108' is visible in the running head): 'ḫazāna: \\\"Schatz\\\" u. kanz stammen aus dem pers. ganǰ, mp. ganj, paz. ganz, mprth. gzn, aram. Lw. gnzʾ' and 'ḫazan: \\\"sammeln\\\" ist nach Jefferys \\\"Foreign Vocabulary of Qoran\\\" ein denom. Verb, welches v. vielen westl. Sprachwissenschaftlern als Lw. im Ar. angesehen wurde. Hoffmann schlägt in einem Artikel in ZDMG Bd. 32 S. 760 vor, seinen Ursprung im persischen ganǰ zu suchen.' The cited page is exactly on point and supports Nourai.\"},\n    {\"ref\": \"FVQ:122\", \"status\": \"contradicts\",\n     \"note\": \"FVQ_pages.txt leaf 139-140 = printed pp.122-123, the entry خزانة: 'It is fairly obvious that [ḵazana] is a denominative verb, and the word has been recognized by many Western scholars as a foreign borrowing. Its origin, however, is a little more difficult to determine. Hoffmann, ZDMG xxxii, 760, suggested that we should find its origin in the Pers. [ganj] … It seems hardly likely that by another line of borrowing … it has come to form the Ar. ḵazāna. Barth, Etymol. Stud. 51, makes the happier suggestion that it may be connected with the form that is behind the Heb. [ḥsn] treasure.' Jeffery explicitly declines the derivation Nourai draws.\"},\n    {\"ref\": \"DOZ:60\", \"status\": \"partial\",\n     \"note\": \"Dozy, Oosterlingen, s.v. MAGAZIJN, printed pp.60-61 (the inline folio marks 60 and 61 bracket the article, DOZ.txt lines 1819-1848): 'Het Arab. machzen, verzachte uitspraak machazen, van het werkwoord chazana, bewaren, de plaats, het gebouw, waar men iets bewaart; Sp. magacen, ook almacen; Port. almazem, armazem; Ital. maggazino; Fr. magasin.' The page is the right one and supports maḵzan < ḵazana and its Romance offspring, but says nothing about any Persian source.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"1966 ed. s.v. magazine (KLN_1966.txt leaf 495, line 22513)\", \"stance\": \"partial\",\n     \"note\": \"'fr. Arab. makhāzin, pl. of makhzān, \\\"storehouse\\\", fr. khāzana, \\\"he stored up\\\", for the etymology of which see Paul de Lagarde, Gesammelte Abhandlungen, 1866, p.25' — Klein treats the root as Arabic and refers the deeper etymology out to Lagarde (who argued for an Iranian source), i.e. he neither asserts nor denies the ganj connection.\"},\n    {\"src\": \"SKT\", \"where\": \"s.v. Magazine (SKT.txt line 10886)\", \"stance\": \"contradicts\",\n     \"note\": \"'Magazine. (F. — Ital. — Arab.) O[F]. magasin — Ital. [magazzino], a storehouse. — Arab. makhzan, pl. makhāzin, a storehouse. — Arab. khazan, laying up in store.' Skeat stops at the Arabic verb.\"},\n    {\"src\": \"DEV\", \"where\": \"s.v. Magasin (DEV.txt line 1657)\", \"stance\": \"contradicts\",\n     \"note\": \"'De l'arabe makhzen, plur. makhâzin, grenier, lieu de dépôt, venant du verbe [khazana] mettre en magasin, serrer, conserver.' No Iranian element.\"},\n    {\"src\": \"LAM\", \"where\": \"Lammens, s.v. (LAM.txt lines 4754-4755)\", \"stance\": \"contradicts\",\n     \"note\": \"'khazîna, trésor, de la racine khazan, emmagasiner, serrer. Cette même racine nous a donné magasin.'\"},\n    {\"src\": \"LKT\", \"where\": \"no. 1362 Ar. maḫzan vs no. 1059 Ar. kanz\", \"stance\": \"contradicts\",\n     \"note\": \"Lokotsch files maḫzan (no.1362) and kanz (no.1059) as two unrelated Arabic head-words; only the latter is marked 'aus pers. ganǰ'.\"}\n  ]\n})\n\nN.append({\n  \"id\": 7, \"lang\": \"Persian\", \"words\": \"\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"A pass-through box with no transliteration, only the Persian script forms خازن، مخزن، خزانه، خزینه. All four are ordinary Arabic loans in New Persian, taken over as whole words with their Arabic morphology intact: خازن ḵāzen 'treasurer' (active participle fāʿil of ḵazana), مخزن maḵzan 'storehouse' (noun of place mafʿal), خزانه ḵazāne 'treasury' and its colloquial doublet خزینه ḵazine (also 'the hot-water basin of a bath-house'). Their arrival in Persian is post-Islamic and purely lexical; there is no sound change beyond the Persian reading of tāʾ marbūṭa as -e/-eh. Whatever the ultimate origin of the Arabic root (see node 6), these Persian words are borrowed from Arabic, which is what the arrow says.\",\n  \"derivation_fa\": \"این جعبه گذرگاهی است و آوانگاشت ندارد؛ تنها صورت‌های فارسی «خازن، مخزن، خزانه، خزینه» را می‌آورد. هر چهار واژه وام‌واژهٔ عربی در فارسی نو هستند و با ساختِ صرفی عربی خود به فارسی آمده‌اند: «خازن» اسم فاعل بر وزن فاعل، «مخزن» اسم مکان بر وزن مَفعَل، «خزانه» و گونهٔ عامیانه‌ترش «خزینه» (که در فارسی معنی حوضچهٔ آب گرم حمام را نیز گرفته است). ورود این‌ها به فارسی پس از اسلام و یکسره واژگانی است و جز خواندن تاء مربوطه به صورت «ـه» فارسی، دگرگونی آوایی در کار نیست. سرچشمهٔ نهایی ریشهٔ عربی هرچه باشد (نگاه کنید به گرهٔ ۶)، این واژه‌های فارسی از عربی وام گرفته شده‌اند و پیکان نمودار همین را می‌گوید.\",\n  \"sources\": [W_KHAZANA],\n  \"ref_check\": [{\"ref\": \"FVA\", \"status\": \"not_checked\",\n    \"note\": \"Nourai cites FVA without a page. FVA (Nahvi, Farhang-e Vazheha-ye Arabi dar Farsi) has no digital copy on any permitted platform per refs_online.json, so it could not be consulted.\"}],\n  \"consulted\": [\n    {\"src\": \"MON\", \"where\": \"MON_part1.txt line 52299 (s.v. حانوت, glossed 'دکان، مغازه') and passim\", \"stance\": \"supports\",\n     \"note\": \"Mo'in's dictionary carries خازن/مخزن/خزانه/خزینه throughout as Arabic-tagged loans; the same lexicon glosses shop-words with مغازه, confirming the family is naturalised Persian vocabulary.\"},\n    {\"src\": \"DEV\", \"where\": \"s.v. Kazine (DEV.txt line 1600)\", \"stance\": \"supports\",\n     \"note\": \"'Kazine. Trésor du Grand-Seigneur. De l'arabe [ḵazīna], venant de la même racine qui a donné magasin.' — the same خزینه, recognised as a derivative of the Arabic root.\"},\n    {\"src\": \"PLA\", \"where\": \"Asbaghi p.109 (leaf 124)\", \"stance\": \"partial\",\n     \"note\": \"'könnte ḫazan seinen Ursprung im pers. ḫazine, mp. uzēnag haben' and 'ḫazandār: \\\"Schatzmeister\\\" pers.' — Asbaghi even entertains the reverse direction for خزینه, which shows how entangled the Arabic and Persian members of this family are.\"}\n  ]\n})\n\nN.append({\n  \"id\": 8, \"lang\": \"Italian\", \"words\": \"mazazzino\",\n  \"verdict\": \"transcription_suspect\",\n  \"error_in\": \"book\",\n  \"book_prints\": \"mazazzino\",\n  \"correct_form\": \"magazzino\",\n  \"derivation\": \"The Italian word is magazzino 'warehouse, store', borrowed in the Venetian and Genoese Levant trade of the 13th-14th centuries from Arabic (plural) makhāzin / (singular) makhzan; Lokotsch no.1362 lists the whole Romance family — 'hieraus it. magazzino, sard. magasinu, siz. magasenu, frz. magasin, sp. magacén, almacén, pg. almazém' — and Dozy p.60 has 'Ital. maggazino'. The printed page of Nourai's dictionary (checked at 500 dpi: see data/verification/sources/refs/ocr/BOOK/218.png) really does read 'mazazzino', so the JSON extraction is faithful and the error is the author's own misprint: a g mis-set as z. No Italian dictionary knows a form *mazazzino.\",\n  \"derivation_fa\": \"صورت درست ایتالیایی magazzino «انبار، فروشگاه» است که در سده‌های سیزدهم و چهاردهم میلادی از راه بازرگانی ونیزی و جنوایی در شام و مصر از عربی «مَخازِن» (جمع «مَخزَن») وام گرفته شده است؛ لوکوچ (شمارهٔ ۱۳۶۲) همهٔ خانوادهٔ رومی آن را می‌شمارد: «ایتالیایی magazzino، ساردی magasinu، سیسیلی magasenu، فرانسوی magasin، اسپانیایی magacén/almacén، پرتغالی almazém» و دوزی (ص ۶۰) نیز «Ital. maggazino» دارد. صفحهٔ چاپی کتاب نورایی — که با تفکیک ۵۰۰ نقطه بررسی شد (تصویر در data/verification/sources/refs/ocr/BOOK/218.png) — به‌راستی «mazazzino» چاپ کرده است؛ پس خوانش داده‌ها درست بوده و خطا، خطای چاپی خودِ کتاب است: حرف g به‌جای z نشسته. هیچ فرهنگ ایتالیایی صورت *mazazzino را نمی‌شناسد.\",\n  \"sources\": [W_ETYM_MAGAZINE],\n  \"ref_check\": [NONE_REF],\n  \"consulted\": [\n    {\"src\": \"LKT\", \"where\": \"no. 1362, Ar. maḫzan (LKT.txt line 3162)\", \"stance\": \"supports\",\n     \"note\": \"'hieraus it. magazzino, sard. magasinu, camasinu [mit Metathesis], siz. magasenu, maasemi, malasenu, malase, frz. magasin, sp. magacén, almagacen, almacen, pg. almazem, armazem, rum. magaza, magazin; dtsch. Magazin, ndl. magazijn, engl. magazine' — the Italian form is magazzino.\"},\n    {\"src\": \"DOZ\", \"where\": \"s.v. MAGAZIJN, printed p.60 (DOZ.txt line 1826)\", \"stance\": \"supports\",\n     \"note\": \"'Sp. magacen, ook almacen; Port. almazem, armazem; Ital. maggazino; Fr. magasin.'\"},\n    {\"src\": \"SKT\", \"where\": \"s.v. Magazine (SKT.txt line 10886)\", \"stance\": \"supports\",\n     \"note\": \"'Magazine. (F. — Ital. — Arab.) OF. magasin — Ital. [magazzino], a storehouse' — Skeat too has the Italian stage that Nourai draws.\"}\n  ]\n})\n\nN.append({\n  \"id\": 9, \"lang\": \"French\", \"words\": \"magasin\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"French magasin 'warehouse, store' is borrowed in the 15th-16th c. from Italian magazzino (Provençal magazin is attested from 1409), the Italian itself from Arabic makhāzin; Etymonline gives the chain 'Middle French magasin \\\"warehouse, depot, store\\\" … from Italian magazzino, from Arabic makhazin, plural of makhzan \\\"storehouse\\\"'. Lokotsch no.1362 lists frz. magasin in the same family, and Devic s.v. Magasin gives 'ital. magazzino. De l'arabe makhzen, plur. makhâzin'. The Italian geminate -zz- [ts] is simplified to French -s- [z], and the Arabic plural pattern maCāCiC lies behind the -a- of the second syllable.\",\n  \"derivation_fa\": \"«magasin» فرانسوی به معنی انبار و فروشگاه در سده‌های پانزدهم و شانزدهم میلادی از magazzino ایتالیایی وام گرفته شده (صورت پرووانسی magazin از سال ۱۴۰۹ گواهی شده است) و ایتالیایی خود از «مَخازِن» عربی است؛ اتیمانلاین زنجیره را چنین می‌دهد: «فرانسوی میانه magasin «انبار، فروشگاه» … از ایتالیایی magazzino، از عربی makhāzin، جمع makhzan». لوکوچ (۱۳۶۲) و دُویک نیز همین را می‌آورند: «ایتالیایی magazzino؛ از عربی مخزن، جمع مخازن». از نظر آوایی، مشدّدِ ایتالیایی ‑zz‑ در فرانسوی به ‑s‑ ساده شده و واکهٔ هجای دوم بازتاب وزن جمع عربی «مَفاعِل» است. ادعای نورایی درست است.\",\n  \"sources\": [W_ETYM_MAGAZINE],\n  \"ref_check\": [NONE_REF],\n  \"consulted\": [\n    {\"src\": \"DEV\", \"where\": \"s.v. Magasin (DEV.txt line 1657)\", \"stance\": \"supports\",\n     \"note\": \"'Magasin. Esp. magacen, almagacen, almarcen, almacen, portug. almazem, armazem, ital. magazzino. De l'arabe makhzen, plur. makhâzin, grenier, lieu de dépôt.'\"},\n    {\"src\": \"PHN\", \"where\": \"s.v. MAGASIN (PHN.txt lines 6839-6848)\", \"stance\": \"supports\",\n     \"note\": \"Pihan devotes a full article to MAGASIN, s. m. (a.) among the French words of Arabic origin.\"},\n    {\"src\": \"LKT\", \"where\": \"no. 1362 (LKT.txt line 3162)\", \"stance\": \"supports\",\n     \"note\": \"'frz. magasin' listed directly after 'it. magazzino'.\"}\n  ]\n})\n\nN.append({\n  \"id\": 10, \"lang\": \"English\", \"words\": \"magazine\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"English magazine is first recorded in the 1580s in the sense 'warehouse, place for storing goods, especially military ammunition', borrowed from Middle French magasin; Klein's entry is exactly Nourai's chain: 'magazine, n. — MF. magazin (F. magasin), fr. OF. magazin, fr. It. magazzino, fr. Arab. makhāzin, pl. of makhzan, \\\"storehouse\\\", fr. khazana, \\\"he stored up\\\".' The specialised senses developed inside English: 'cartridge chamber of a repeating rifle' (1868) and, by the metaphor of a store-house of information, the periodical sense from the Gentleman's Magazine of 1731.\",\n  \"derivation_fa\": \"واژهٔ انگلیسی magazine نخستین بار در دههٔ ۱۵۸۰ به معنی «انبار، جای نگهداری کالا، به‌ویژه مهمات» ثبت شده و از magasin فرانسوی میانه وام گرفته شده است؛ مدخل کلاین دقیقاً همان زنجیرهٔ نورایی است: «magazine — فرانسوی میانه magazin (فرانسوی magasin)، از فرانسوی باستان magazin، از ایتالیایی magazzino، از عربی makhāzin، جمع makhzan «انبار»، از khazana «انباشت»». معناهای ویژه در خودِ انگلیسی پدید آمده‌اند: «خزانهٔ فشنگِ تفنگ» (۱۸۶۸) و معنای «مجله» که از استعارهٔ «انبار دانستنی‌ها» و از نام Gentleman's Magazine (۱۷۳۱) برخاسته است. ادعای نورایی درست است.\",\n  \"sources\": [W_ETYM_MAGAZINE],\n  \"ref_check\": [{\"ref\": \"KLN:922\", \"status\": \"supports\",\n    \"note\": \"KLN_1966.txt leaf 495, s.v. magazine: 'MF. magazin (F. magasin), fr. OF. magazin, fr. It. magazzino, fr. Arab. ma-khāzin, pl. of makhzān, \\\"storehouse\\\", fr. khāzana, \\\"he stored up\\\", for the etymology of which see Paul de Lagarde, Gesammelte Abhandlungen, Leipzig, 1866, p.25. Cp. alhacena, almacén.' The page number 922 falls in Klein's vol. II (pp.854-1776) among the ma- words, which is right; the leaf-to-page offset that puts genizah on the cited p.648 would put this leaf a little later, so the citation is approximate but the entry is unambiguous.\"}],\n  \"consulted\": [\n    {\"src\": \"SKT\", \"where\": \"s.v. Magazine (SKT.txt line 10886)\", \"stance\": \"supports\",\n     \"note\": \"'Magazine. (F. — Ital. — Arab.) OF. magasin (F. magasin) — Ital. [magazzino], a storehouse. — Arab. makhzan, pl. makhāzin.'\"},\n    {\"src\": \"LKT\", \"where\": \"no. 1362 (LKT.txt line 3162)\", \"stance\": \"supports\", \"note\": \"'engl. magazine' in the same list.\"},\n    {\"src\": \"DOZ\", \"where\": \"printed p.61 (DOZ.txt line 1845)\", \"stance\": \"supports\",\n     \"note\": \"Dozy notes the lateness of the word in the north: 'Ook in het Duitsch is Magazin niet oud; volgens Schmitthenner's Wörterbuch … is het daarin eerst in de 17e eeuw opgenomen.'\"}\n  ]\n})\n\nN.append({\n  \"id\": 11, \"lang\": \"Turkish\", \"words\": \"maghazeh\",\n  \"verdict\": \"disputed\",\n  \"derivation\": \"The Turkish word is mağaza 'shop, store' (Ottoman مغازه), not 'maghazeh' — Nourai's form is really the Persian pronunciation written back into the Turkish box. More importantly the parent is wrong: Turkish did not take the word from French magasin. Wiktionary derives Persian مغازه 'from Ottoman Turkish مغازه (mağâza), from Byzantine Greek μαγαζίον (magazíon), from Venetan magazén, ultimately from Arabic خزن (ḵazana)' — i.e. the Ottoman word came in through the Greek-and-Venetian Levantine trade language, not through 19th-c. French; Lokotsch's Balkan list points the same way, with Romanian magaza/magazin beside Turkish forms in the maḫzan family (no.1362). French magasin has no -a final vowel that could give Turkish -a, whereas Venetian/Greek magazén/magazíon does. The word itself is unquestionably a member of this family, so only the route (and the shape of the form) is wrong.\",\n  \"derivation_fa\": \"واژهٔ ترکی mağaza «فروشگاه، دکان» است (عثمانی: مغازه) نه «maghazeh»؛ صورتی که نورایی نوشته در واقع تلفظ فارسی است که در جعبهٔ ترکی نشسته. مهم‌تر آنکه جعبهٔ مادر نادرست است: ترکی این واژه را از magasin فرانسوی نگرفته است. ویکی‌واژه «مغازه»ی فارسی را چنین می‌گیرد: «از ترکی عثمانی مغازه، از یونانی بیزانسی μαγαζίον، از ونیزی magazén، سرانجام از عربی خزن»؛ یعنی واژه از راه زبان بازرگانی یونانی–ونیزی مدیترانهٔ شرقی به عثمانی رسیده، نه از فرانسویِ سدهٔ نوزدهم. فهرست بالکانی لوکوچ (شمارهٔ ۱۳۶۲) نیز همین را نشان می‌دهد (رومانیایی magaza/magazin در کنار صورت‌های ترکی). افزون بر این، magasin فرانسوی واکهٔ پایانی ندارد که «ـه/‑a»ی ترکی را توضیح دهد، حال آنکه magazén/magazíon چنین واکه‌ای دارد. خودِ واژه بی‌گمان از همین خانواده است؛ تنها راهِ رسیدن (و صورت نوشته‌شده) نادرست است.\",\n  \"sources\": [W_MAGAZE],\n  \"ref_check\": [ETM()],\n  \"consulted\": [\n    {\"src\": \"LKT\", \"where\": \"no. 1362 and the Romanian index (LKT.txt lines 3162, 8719)\", \"stance\": \"partial\",\n     \"note\": \"'rum. magaza, magazin' and 'bulg. serb. magaza, magazin \\\"Warenniederlage, Zeughaus\\\"' — Lokotsch places the Balkan/Ottoman forms in the maḫzan family but derives them from the Arabic/Italian side, not from French.\"},\n    {\"src\": \"TTS\", \"where\": \"Vámbéry, Etymologisches Wörterbuch der turko-tatarischen Sprachen (TTS_pages.txt)\", \"stance\": \"silent\",\n     \"note\": \"Vámbéry's dictionary covers inherited Turkic vocabulary and has no article for this recent Levantine loan.\"},\n    {\"src\": \"DOZ\", \"where\": \"printed pp.60-61\", \"stance\": \"partial\",\n     \"note\": \"Dozy's article shows the word spreading through the eastern Mediterranean trade in the 15th c. ('Magasienne', 'Magazeenen' in the 1481 travel account of Joos van Ghistele), the milieu in which Ottoman Turkish would have taken it up.\"}\n  ]\n})\n\nN.append({\n  \"id\": 12, \"lang\": \"Persian\", \"words\": \"mağâzeh\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"Persian مغازه maġāze 'shop, store' is a modern loan from Ottoman Turkish mağaza, as Wiktionary states: 'Borrowed from Ottoman Turkish مغازه (mağâza), from Byzantine Greek μαγαζίον, from Venetan magazén, ultimately from Arabic خزن (ḵazana)'. The Turkish final -a is regularly rendered by Persian -ه -e, and the ġayn spelling reflects the Turkish ğ. The word entered Persian in the Qajar period as a term of the new European-style retail trade, alongside the older دکان and حانوت; Mo'in's dictionary glosses حانوت as 'دکان، مغازه', which shows the word fully naturalised. Nourai's arrow (Turkish → Persian) is correct even though his Turkish box's own parent is not.\",\n  \"derivation_fa\": \"«مغازه» در فارسی وام‌واژه‌ای نو از ترکی عثمانی mağaza است؛ ویکی‌واژه می‌نویسد: «وام‌گرفته از ترکی عثمانی مغازه، از یونانی بیزانسی μαγαζίον، از ونیزی magazén، سرانجام از عربی خزن». واکهٔ پایانی ‑a در ترکی به‌قاعده در فارسی «ـه» می‌شود و نگارش با «غ» بازتاب ğ ترکی است. این واژه در دورهٔ قاجار همراه با دادوستد اروپایی‌شکلِ تازه وارد فارسی شد و در کنار «دکان» و «حانوت» کهن‌تر نشست؛ معین «حانوت» را «دکان، مغازه» معنی می‌کند که نشان می‌دهد واژه کاملاً فارسی‌شده است. پیکان نورایی (ترکی ← فارسی) درست است، هرچند جعبهٔ مادرِ ترکی نادرست است.\",\n  \"sources\": [W_MAGAZE],\n  \"ref_check\": [ETM()],\n  \"consulted\": [\n    {\"src\": \"MON\", \"where\": \"MON_part1.txt lines 2630, 52299, 90480 (مغازه سلمانی; حانوت 'دکان، مغازه'; 'خرید از مغازه')\", \"stance\": \"supports\",\n     \"note\": \"Mo'in uses مغازه freely as the ordinary modern Persian word for a shop and glosses the Arabic حانوت by it — a naturalised recent loan, as the Turkish route implies.\"},\n    {\"src\": \"LKT\", \"where\": \"no. 1362 (LKT.txt line 3162)\", \"stance\": \"partial\",\n     \"note\": \"The Ottoman/Balkan branch of the maḫzan family from which the Persian word comes.\"}\n  ]\n})\n\nN.append({\n  \"id\": 13, \"lang\": \"Arabic\", \"words\": \"j.n.z; jenâzeh\",\n  \"verdict\": \"plausible\",\n  \"derivation\": \"Arabic جَنَازة/جِنازة janāza/jināza 'bier; corpse' belongs to a root ج ن ز whose only other members mean 'to cover, to wrap (a body)'. Klein, the reference Nourai cites, treats that root as the Arabic member of the ganj family: s.v. genizah (p.648) he derives Mishnaic Hebrew genīzāh from ganaz 'he saved, he hid', which is 'borrowed fr. Pers. ganj, \\\"treasure\\\", whence also Aram. genaz \\\"he saved\\\", ginzā, gazzā \\\"treasure\\\", Arab. janaza \\\"he covered up\\\"'. Modern Semitic scholarship is more cautious: Wiktionary derives the whole root from Ge'ez ገነዘ (gänäzä) 'to wrap, to prepare a body for funeral' and Old Sabaean gnz, gnzt 'funeral', adding only that this may be 'potentially the same Iranian word as كنز (kanz)'. So the connection is real in the literature but is now framed as South-Semitic first, with the Iranian tie an open possibility rather than a demonstrated borrowing; and if it is Iranian, it entered through Aramaic gnz 'to hide, store', not directly from the Parthian box.\",\n  \"derivation_fa\": \"«جَنازه/جِنازه» عربی به معنی تابوت و پیکر مرده از ریشهٔ ج‑ن‑ز است که دیگر مشتقات آن معنی «پوشاندن، در کفن پیچیدن» دارند. کلاین — همان مرجعی که نورایی آورده — این ریشه را عضو عربیِ خانوادهٔ «گنج» می‌داند: ذیل genizah (ص ۶۴۸) «گنیزهٔ» عبری میانه را از ganaz «پنهان کرد، نگاه داشت» می‌گیرد که «از فارسی ganj «گنج» وام گرفته شده، و از همان‌جاست آرامی genaz «نگاه داشت»، ginzā و gazzā «گنج»، و عربی janaza «پوشاند»». اما سامی‌شناسی امروزی محتاط‌تر است: ویکی‌واژه کل ریشه را از گِعِز ገነዘ (gänäzä) «پیچیدن، آمادهٔ خاک‌سپاری کردن» و سبئی کهن gnz، gnzt «خاک‌سپاری» می‌گیرد و تنها می‌افزاید که «احتمالاً همان واژهٔ ایرانیِ کنز» باشد. پس پیوند در ادبیات علمی هست ولی امروز نخست سامی جنوبی دانسته می‌شود و پیوند ایرانی تنها یک احتمال گشوده است؛ و اگر هم ایرانی باشد، از راه آرامی gnz «پنهان کردن» آمده نه یکسر از پارتی. یعنی ادعای نورایی با احتیاط پذیرفتنی است.\",\n  \"sources\": [W_JANAZA],\n  \"ref_check\": [\n    {\"ref\": \"KLN:648\", \"status\": \"supports\",\n     \"note\": \"KLN_1966.txt leaf 350, s.v. genizah — and leaf 350 is precisely printed p.648 on the offset that puts gazelle/gazette (leaf 348) on the p.644 Nourai cites for those boxes: 'genizah, n., storeroom of a synagogue … fr. ganaz, \\\"he saved; he hid\\\" … borrowed fr. Pers. ganj, \\\"treasure\\\", whence also Aram. genaz, \\\"he saved\\\", ginzā, gazzā, \\\"treasure\\\", Arab. jánaza, \\\"he covered up\\\". Cp. Arm. ganj, Gk. γάζα (whence L. gaza), and Hung. kincs … Cp. also gazette and the first element in Gaspar, Jasper.' Klein's page carries almost the whole right-hand half of Nourai's chart.\"},\n    FVA(\"FVA:82\")\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"1966 ed. p.648 s.v. genizah\", \"stance\": \"supports\", \"note\": \"See ref_check.\"},\n    {\"src\": \"FVQ\", \"where\": \"Jeffery pp.122-123, 251\", \"stance\": \"silent\",\n     \"note\": \"Jeffery has entries for خزانة and كنز but no entry for جنازة; he does not discuss the root ج ن ز at all.\"},\n    {\"src\": \"PLA\", \"where\": \"Asbaghi p.108 (leaf 123)\", \"stance\": \"silent\",\n     \"note\": \"Asbaghi's ganj-derived Arabic words are ḫazāna and kanz; janāza is not among the Persian loanwords he lists.\"},\n    {\"src\": \"AFA\", \"where\": \"Fraenkel, Die aramäischen Fremdwörter im Arabischen (AFA.txt)\", \"stance\": \"silent\",\n     \"note\": \"Searched for the root; Fraenkel's Aramaic-loan list does not carry janāza, which is consistent with Wiktionary's South-Semitic derivation.\"}\n  ]\n})\n\nN.append({\n  \"id\": 14, \"lang\": \"Persian\", \"words\": \"jenâzeh\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"Persian جنازه jenāze 'corpse, bier, funeral procession' is a plain post-Islamic Arabic loan, taken over with the Arabic form intact and the tāʾ marbūṭa read as Persian -eh; it is a religious-legal term (نماز جنازه 'funeral prayer') and carries in Persian, as in Arabic, both 'bier' and 'the body on it'. The arrow Arabic → Persian is therefore certainly right, whatever one decides about the ultimate origin of the Arabic root in node 13.\",\n  \"derivation_fa\": \"«جنازه» در فارسی وام‌واژه‌ای عربی و پس از اسلام است که با صورت عربی خود گرفته شده و تنها تاء مربوطهٔ آن به «ـه» فارسی خوانده می‌شود؛ اصطلاحی دینی–فقهی است («نماز جنازه») و در فارسی، مانند عربی، هم «تابوت» و هم «پیکر مرده» معنی می‌دهد. پس پیکان عربی ← فارسی بی‌گمان درست است، هر تصمیمی که دربارهٔ سرچشمهٔ نهایی ریشهٔ عربی در گرهٔ ۱۳ گرفته شود.\",\n  \"sources\": [W_JANAZA],\n  \"ref_check\": [FVA(\"FVA:82\")],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"1966 ed. p.648 s.v. genizah\", \"stance\": \"partial\",\n     \"note\": \"Klein's 'Arab. jánaza, \\\"he covered up\\\"' is the Arabic verb behind the noun Persian borrowed.\"},\n    {\"src\": \"MON\", \"where\": \"MON_part1/part2 (searched s.v. جنازه)\", \"stance\": \"silent\",\n     \"note\": \"The abridged two-volume Mo'in scan on disk does not return a جنازه head-word (OCR of Arabic-script head-words in this scan is unreliable); no contrary evidence.\"}\n  ]\n})\n\nN.append({\n  \"id\": 15, \"lang\": \"Greek\", \"words\": \"gaza\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"Ancient Greek γάζα 'treasure, treasury, royal treasure' is the classic Achaemenid administrative loan: Greek writers of the 4th c. BCE (Theophrastus, and Curtius/Polybius later, of Persian royal treasuries) use it as a Persian word, and it is standardly derived from the Median form *ganǰam/ganza- — Wiktionary: 'from Old Median *ganǰam (\\\"treasure\\\"), which spread through the administrative systems of the Achaemenid Empire'. Jeffery lists 'Gk. γάζα' among the direct borrowings from Middle Persian ganj, and Hübschmann and Nyberg both cite γάζα in the same breath as Armenian ganj and Aramaic ginzā. The Iranian -nz- cluster is simplified in Greek to -z- (as in Ecbatana < Hagmatāna, with no nasal preserved before the fricative), giving γάζα with an inflectional -a.\",\n  \"derivation_fa\": \"«γάζα» یونانی باستان به معنی «گنج، خزانه، خزانهٔ شاهی» نمونهٔ کلاسیک وام‌واژهٔ دیوانی هخامنشی است: نویسندگان یونانی سدهٔ چهارم پیش از میلاد آن را واژه‌ای پارسی می‌دانند و منابع امروزی آن را از صورت مادی *ganǰam/ganza- می‌گیرند؛ ویکی‌واژه می‌نویسد «از مادی باستان *ganǰam «گنج» که از راه دستگاه دیوانی شاهنشاهی هخامنشی پراکنده شد». جفری «γάζα یونانی» را در شمار وام‌های مستقیم از ganj فارسی میانه می‌آورد، و هوبشمان و نیبرگ هر دو γάζα را در کنار ganj ارمنی و ginzā آرامی یاد می‌کنند. از نظر آوایی، خوشهٔ ‑nz‑ ایرانی در یونانی به ‑z‑ ساده شده و پایانهٔ صرفی ‑a بر آن افزوده شده است. ادعای نورایی درست است.\",\n  \"sources\": [W_GAZA],\n  \"ref_check\": [\n    {\"ref\": \"KLN:644\", \"status\": \"supports\",\n     \"note\": \"KLN_1966.txt leaf 348 s.v. gazette: 'It. gazzetta, \\\"coin\\\", is prob. a dimin. formed fr. L. gaza, \\\"treasure\\\", fr. Gk. γάζα, which is of Persian origin. See genizah.' Klein's cited page states the Greek word and its Persian origin.\"},\n    {\"ref\": \"FVQ:251\", \"status\": \"supports\",\n     \"note\": \"FVQ p.251 (leaf 268): '… the word has been widely borrowed, cf. Skt.; Arm.; Baluchi ganj; Gk. γάζα; Sogd. γnz.'\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"HUB\", \"where\": \"Persische Studien p.232 (HUB.txt line 8272)\", \"stance\": \"supports\",\n     \"note\": \"'ganj \\\"Schatz\\\" (5. Jhd.) = np. ganj, phl. ganj … skr. LW. ganja-, gr. γάζα, syr. … \\\"Schatz\\\"'.\"},\n    {\"src\": \"NYB\", \"where\": \"Nyberg II glossary s.v. ganj (line 1624)\", \"stance\": \"supports\",\n     \"note\": \"'… Gr. lw. γάζα' listed among the loans from the Iranian word.\"},\n    {\"src\": \"LKT\", \"where\": \"no. 1059 (LKT.txt line 2516)\", \"stance\": \"supports\",\n     \"note\": \"'Das pers. Grundwort wurde schon früh lat. gaza \\\"Schatz\\\"' — via Greek.\"}\n  ]\n})\n\nN.append({\n  \"id\": 16, \"lang\": \"Latin\", \"words\": \"gaza\",\n  \"verdict\": \"plausible\",\n  \"derivation\": \"Latin gaza 'treasure, royal treasure' is a straight borrowing of Greek γάζα (Wiktionary s.v. γάζα: 'Descendants: Latin gaza'), used by Cicero, Virgil and the Vulgate; that part of the box is beyond doubt. What is not right is the gloss. Latin gaza never meant a Venetian coin or a newspaper: those senses belong to Italian gazzetta, the diminutive that Klein and Lokotsch derive from gaza — Klein p.644: 'It. gazzetta, name of the smallest Venetian coin, said to have been paid for the perusal of the manuscript newspaper issued by the Venetian Government once a month. It. gazzetta, \\\"coin\\\", is prob. a dimin. formed fr. L. gaza.' Nourai has compressed Klein's Italian stage into his Latin box and carried Klein's gloss over with it, which leaves the chart with a Latin word defined by a 16th-century Venetian coin. The derivation is sound; the label is not.\",\n  \"derivation_fa\": \"«gaza» لاتین به معنی «گنج، خزانهٔ شاهی» وام‌گیریِ مستقیم از γάζα یونانی است (ویکی‌واژه ذیل γάζα: «بازماندگان: لاتین gaza») و در نوشته‌های سیسرون، ویرژیل و ترجمهٔ وولگات به کار رفته است؛ این بخشِ جعبه بی‌چون‌وچراست. آنچه نادرست است معنای نوشته‌شده است: gaza در لاتین هرگز به معنی سکهٔ ونیزی یا روزنامه نبوده؛ این معناها از آنِ gazzetta ایتالیایی است، یعنی همان مصغّری که کلاین و لوکوچ آن را از gaza می‌گیرند — کلاین (ص ۶۴۴): «ایتالیایی gazzetta، نام کوچک‌ترین سکهٔ ونیزی که گفته‌اند بهای خواندن روزنامهٔ دست‌نویسِ ماهانهٔ حکومت ونیز بوده است … gazzetta «سکه» احتمالاً مصغّری است ساخته‌شده از gaza لاتین». نورایی حلقهٔ ایتالیایی کلاین را در جعبهٔ لاتین فشرده کرده و معنای ایتالیایی را نیز با آن آورده است؛ نتیجه آنکه واژه‌ای لاتین با سکه‌ای ونیزی از سدهٔ شانزدهم تعریف شده است. اشتقاق درست است، برچسب معنایی نه.\",\n  \"sources\": [W_GAZA, W_ETYM_GAZETTE],\n  \"ref_check\": [NONE_REF],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"1966 ed. p.644 s.v. gazette\", \"stance\": \"partial\",\n     \"note\": \"Klein has 'L. gaza, \\\"treasure\\\"' and puts the coin/newspaper senses on It. gazzetta, not on the Latin word.\"},\n    {\"src\": \"LKT\", \"where\": \"no. 1059 (LKT.txt line 2516)\", \"stance\": \"partial\",\n     \"note\": \"'Das pers. Grundwort wurde schon früh lat. gaza \\\"Schatz\\\"; hieraus it. gazzetta, ursprünglich eine kleine Münze, die man für ein Zeitungsblatt hingab, dann \\\"Zeitung\\\"' — again, the coin sense is Italian.\"},\n    {\"src\": \"LEW\", \"where\": \"Walde, Lateinisches etymologisches Wörterbuch (LEW_1910.txt)\", \"stance\": \"silent\",\n     \"note\": \"The scan yields no usable entry for gaza; no contrary evidence.\"}\n  ]\n})\n\nN.append({\n  \"id\": 17, \"lang\": \"French\", \"words\": \"gazette\",\n  \"verdict\": \"plausible\",\n  \"derivation\": \"French gazette 'newspaper' (from 1600, popularised by Théophraste Renaudot's La Gazette, 1631) is borrowed not from Latin directly but from Italian gazzetta, the name Venetians gave to the manuscript news-sheets sold from 1560 for one gazeta, the smallest copper coin — the intermediate box Nourai has left out. Where the coin's name comes from is genuinely unsettled: Klein and Lokotsch derive it as a diminutive of Latin gaza 'treasure' (Nourai's line), while Körting, Webster and Etymonline prefer gazza 'magpie' (from the bird stamped on the coin, or from the chatter of the news-sheets), and a third view makes gazzetta 'a little treasury of news'. Etymonline's summary applies: 'The general story of the origin of the word is broadly accepted, but there are many variations in the details.' So the arrow is defensible but is one of several competing accounts, and it skips Italian.\",\n  \"derivation_fa\": \"«gazette» فرانسوی به معنی روزنامه (از سال ۱۶۰۰، و پرآوازه‌شده با «لا گازت» تئوفراست رنودو در ۱۶۳۱) نه مستقیم از لاتین، بلکه از gazzetta ایتالیایی وام گرفته شده است؛ ونیزیان از ۱۵۶۰ خبرنامه‌های دست‌نویس را به بهای یک «گازِتا»، کوچک‌ترین سکهٔ مسی، می‌فروختند و همین نام بر خودِ خبرنامه نشست — و همین حلقهٔ ایتالیایی است که در نمودار نورایی جا افتاده است. خاستگاه نامِ سکه به‌راستی محل اختلاف است: کلاین و لوکوچ آن را مصغّرِ gaza لاتین «گنج» می‌دانند (همان خطی که نورایی برگزیده)، حال آنکه کورتینگ، وبستر و اتیمانلاین gazza «زاغی» را ترجیح می‌دهند (به سبب نقش پرنده بر سکه یا پرگویی خبرنامه‌ها)، و نظر سومی gazzetta را «گنجینهٔ کوچک اخبار» می‌داند. جمع‌بندی اتیمانلاین چنین است: «داستان کلی خاستگاه این واژه تا حد زیادی پذیرفته است، ولی در جزئیات روایت‌های گوناگون هست». پس این پیکان پذیرفتنی ولی یکی از چند روایت است و حلقهٔ ایتالیایی را نیز نادیده می‌گیرد.\",\n  \"sources\": [W_ETYM_GAZETTE],\n  \"ref_check\": [NONE_REF],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"1966 ed. p.644 s.v. gazette\", \"stance\": \"partial\",\n     \"note\": \"'gazette, n., newspaper. — F., fr. It. gazzetta … It. gazzetta, \\\"coin\\\", is prob. a dimin. formed fr. L. gaza, \\\"treasure\\\", fr. Gk. γάζα, which is of Persian origin.' Klein supports the gaza line but insists on the Italian intermediary and hedges with 'prob.'\"},\n    {\"src\": \"WEB\", \"where\": \"Webster's Twentieth Century s.v. ga-zette' (WEB_vol1.txt line 80707)\", \"stance\": \"contradicts\",\n     \"note\": \"'[It. gazzetta, a gazette, … prob. from gazzetta, a gazet or sma[ll coin, the] price paid for the paper; also [fr]om gazzetta, a magpie, and [chat]terer or tattler.]' — Webster prefers the coin/magpie explanations and does not mention gaza.\"},\n    {\"src\": \"LKT\", \"where\": \"no. 1059 (LKT.txt line 2516)\", \"stance\": \"supports\",\n     \"note\": \"'hieraus it. gazzetta … frz. gazette, sp. gaceta, pg. gazeta \\\"Zeitung\\\" [Körting 4117a leitet dagegen vom Demin. von gazza \\\"Elster\\\" ab …]' — Lokotsch chooses the gaza line but records the magpie alternative.\"},\n    {\"src\": \"SKT\", \"where\": \"SKT.txt leaf 195 (the gazette entry) and the origin-list on printed p.605\", \"stance\": \"partial\",\n     \"note\": \"Skeat's badly-OCR'd entry still shows '… from Ital. gaz[z]etta … [gazza], a magpie …', and his classified list has 'French from Italian: … gazette …' — i.e. the Italian stage that Nourai's chart omits.\"}\n  ]\n})\n\nN.append({\n  \"id\": 18, \"lang\": \"English\", \"words\": \"gazette\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"English gazette is taken from French gazette about 1600; the first English use of the word as a title is for the papers issued at Oxford in 1665 (the Oxford Gazette, later the London Gazette), and the verb 'to gazette' = to announce officially, from the 1670s, follows from the London Gazette's function as the government's register of appointments and bankruptcies. Klein's entry (the reference cited) gives simply 'gazette, n., newspaper. — F., fr. It. gazzetta'.\",\n  \"derivation_fa\": \"واژهٔ انگلیسی gazette حدود سال ۱۶۰۰ از gazette فرانسوی گرفته شده است؛ نخستین کاربرد آن به عنوان نام روزنامه در انگلستان برای نشریهٔ آکسفورد در ۱۶۶۵ است (Oxford Gazette که بعدها London Gazette شد) و فعل to gazette به معنی «رسماً اعلام کردن» از دههٔ ۱۶۷۰ برخاسته، چون London Gazette دفتر رسمی انتصاب‌ها و ورشکستگی‌ها بود. مدخل کلاین — همان مرجعی که نورایی آورده — تنها می‌نویسد: «gazette، روزنامه — فرانسوی، از ایتالیایی gazzetta». ادعای نورایی درست است.\",\n  \"sources\": [W_ETYM_GAZETTE],\n  \"ref_check\": [{\"ref\": \"KLN:644\", \"status\": \"supports\",\n    \"note\": \"KLN_1966.txt leaf 348 = printed p.644: 'gazette, n., newspaper. — F., fr. It. gazzetta, of s.m., fr. gazzetta, name of the smallest Venetian coin … Derivatives: gazette, tr. v., gazetteer (q.v.)'.\"}],\n  \"consulted\": [\n    {\"src\": \"SKT\", \"where\": \"classified list, printed p.605 (SKT.txt line 23600)\", \"stance\": \"supports\",\n     \"note\": \"'French from Italian: … frigate, gala, gallery, gallias, gazette, gusset …' — Skeat classifies English gazette as French from Italian.\"},\n    {\"src\": \"WEB\", \"where\": \"WEB_vol1.txt s.v. gazette (line 80707 ff.)\", \"stance\": \"supports\",\n     \"note\": \"Webster gives the English senses '1. a newspaper … 2. any of several official newspapers of Great Britain, containing announcements and bulletins, as of appointments and promotions … of bankrupts' and the verb 'to publish, announce, or list in a gazette'.\"},\n    {\"src\": \"LKT\", \"where\": \"no. 1059 (LKT.txt line 2516)\", \"stance\": \"supports\", \"note\": \"'engl. gazette, ndl. gazet; russ. bulg. poln. gazeta \\\"Zeitung\\\"'.\"}\n  ]\n})\n\nN.append({\n  \"id\": 19, \"lang\": \"Sogdian\", \"words\": \"gzn\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"Sogdian γzn- (γazn) 'treasure' is attested in Buddhist, Manichaean and Christian Sogdian alike, with the derivatives γznβr 'treasurer' and γznyʾ 'treasury'; Gharib's dictionary, the very reference cited, prints '4552 γzn- B, M, C / γazn ① Parth. gzn; MP gnz … treasure' on p.182, i.e. it puts the Sogdian and Parthian forms side by side exactly as this box does. Sogdian γ- for older g- is the regular Sogdian lenition of initial voiced stops (cf. γrīw < *grīwa- 'neck'), so γazn and Parthian ganz are sister reflexes of Old Median *ganza- rather than one being derived from the other — which is the only quibble with the arrow, since the chart makes the Sogdian a descendant of the Parthian box.\",\n  \"derivation_fa\": \"«γzn-» سغدی (γazn) به معنی «گنج» در هر سه گونهٔ بودایی، مانوی و مسیحیِ سغدی گواهی شده است، همراه با مشتقات γznβr «گنجور» و γznyʾ «خزانه». فرهنگ قریب — همان مرجعی که نورایی آورده — در ص ۱۸۲ چنین دارد: «۴۵۵۲ γzn- (بودایی، مانوی، مسیحی) / γazn ① پارتی gzn؛ فارسی میانه gnz … گنج»، یعنی درست همان‌گونه که این جعبه می‌کند، صورت سغدی و پارتی را کنار هم می‌نهد. تبدیل g- آغازین به γ- در سغدی قاعده‌مند است (مانند γrīw از *grīwa- «گردن»)؛ پس γazn سغدی و ganz پارتی هر دو بازتاب *ganza- مادی باستان‌اند و یکی از دیگری برنیامده است — و این تنها خردهٔ وارد بر پیکان نمودار است که سغدی را فرزند جعبهٔ پارتی نشان می‌دهد.\",\n  \"sources\": [],\n  \"ref_check\": [SOD_CHECK],\n  \"consulted\": [\n    {\"src\": \"SOD\", \"where\": \"Gharib, entries 4552-4554, printed p.182 (SOD.txt lines 37818-37825; page number visible on leaf 247 of SOD_pages.txt)\", \"stance\": \"supports\",\n     \"note\": \"'4552 γzn- B, M, C / γazn ① Parth. gzn; MP gnz ② nom. ob. -y(yk), acc. -w; loc. -yh / treasure'; '4553 γznβr B / γaznβar ② pl. -t / treasurer'; '4554 γznyʾ C / γaznyā / treasury'.\"},\n    {\"src\": \"FVQ\", \"where\": \"p.251 (leaf 268)\", \"stance\": \"supports\",\n     \"note\": \"Jeffery lists 'Sogd. γnz' among the borrowings of the Iranian treasure-word.\"},\n    {\"src\": \"NYB\", \"where\": \"Nyberg II glossary s.v. ganj (line 1624)\", \"stance\": \"partial\",\n     \"note\": \"Nyberg gives the Parthian and Middle Persian forms and the Aramaic/Greek/Armenian loans but does not cite the Sogdian; no conflict.\"}\n  ]\n})\n\ndoc[\"entries\"].append(e2)\nout='/home/sfmqrb/git/rishe/data/verification/page-218.json'\njson.dump(doc, open(out,'w',encoding='utf-8'), ensure_ascii=False, indent=1)\nprint(\"wrote\", out, \"entry2 nodes:\", len(N))\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk218b.py && python3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-218.json > /dev/null && echo \"JSON OK\" && python3 /home/sfmqrb/git/rishe/tools/verify_check.py 218",
 "description": "Build entry 2 and run verify_check"
}
```


### [2026-09-06T15:33:26.336Z] TOOL RESULT

```
wrote /home/sfmqrb/git/rishe/data/verification/page-218.json entry2 nodes: 19
JSON OK
nodes verified: 23/23
node verdicts: {'confirmed': 15, 'plausible': 5, 'disputed': 2, 'transcription_suspect': 1}
root verdicts: {'confirmed': 1, 'plausible': 1}
ref checks: {'not_checked': 10, 'not_found': 1, 'supports': 15, 'partial': 3, 'contradicts': 1}
books consulted: {'supports': 43, 'silent': 8, 'partial': 15, 'contradicts': 7} | by book: {'LKT': 14, 'KLN': 10, 'MON': 6, 'SKT': 6, 'DEV': 5, 'NYB': 4, 'WEB': 3, 'PLA': 3, 'FVQ': 3, 'DOZ': 3, 'PHN': 2, 'PHD': 2, 'HUB': 2, 'BQT': 2, 'AHD': 1, 'CHEUNG': 1, 'FSD': 1, 'LAM': 1, 'TTS': 1, 'AFA': 1, 'LEW': 1, 'SOD': 1}
```


## [2026-09-06T15:33:49.945Z] AGENT

Done — `/home/sfmqrb/git/rishe/data/verification/page-218.json` written, valid JSON, `verify_check.py 218` reports **0 PROBLEM lines** (23/23 nodes).

**Counts (pdf p.218 / book p.188, entries: Arabic Ğ.z.l + Parthian Gzn; the Gyŭna redirect skipped)**
- Roots: 1 confirmed (Ğ.z.l), 1 plausible (Gzn)
- Nodes: 15 confirmed · 5 plausible · 2 disputed · 1 transcription_suspect
- Ref checks: 15 supports · 3 partial · 1 contradicts · 1 not_found · 10 not_checked (FVA and ETM have no digital copy)
- 22 books consulted (LKT, KLN, SOD, NYB, PHD, HUB, CHEUNG, FVQ, PLA, ARB, BQT, MON, DOZ, DEV, PHN, LAM, SKT, FSD, WEB, AHD, AFA, TTS)

**Disputed / suspect**
- **Gzn #2 «گنجاندن»** — disputed: ganj is fine, but gonjidan/gonjândan/گنجایش continue MP *wanj-/winj-* ⟨wnc-⟩ < PIr *u̯iač- "to contain" (Cheung p.434; Nyberg glossary s.v. vanj- "NP gunjidan"), with regular NP w- > g-. Homophony with ganj only.
- **Gzn #11 Turkish "maghazeh"** — disputed: Turkish is *mağaza*, and it came via Byzantine Greek μαγαζίον / Venetan magazén (Wiktionary), not from French magasin as drawn.
- **Gzn #8 Italian "mazazzino"** — transcription_suspect, **error_in: book**. The printed page (verified at 500 dpi; copy saved to `data/verification/sources/refs/ocr/BOOK/218.png`) really reads "mazazzino"; correct form is *magazzino*. Extraction is faithful — no data fix needed.

**No extraction errors found** — every form checked against the page image (gacele, gazel, mazazzino, all refs) matches the JSON.

**Notable findings**
- Root box "Parthian Gzn" is right as a word (Gharib SOD p.182 s.v. γzn-: "Parth. gzn; MP gnz") but the family head is **Median** *ganǰa-* (Hübschmann pp.231-232, Nyberg via Mayrhofer, Jeffery p.251 citing Lagarde) — Greek γάζα was borrowed from the Achaemenid chancery, not from Parthian.
- **Gzn #6 (Arabic خ ز ن)** left plausible, not disputed: Nourai's own PLA:108 (Asbaghi) explicitly says *ḫazāna* and *kanz* both come from Persian ganj, but his FVQ:122 (Jeffery p.123) **contradicts** it ("hardly likely… Barth's happier suggestion" = Heb. ḥōsen), and Dozy/Devic/Skeat/Lammens/Lokotsch keep the root Arabic. Also, no source derives ḵazana from *kanz* (the parent box) — they are parallel loans at best.
- **SKT:209 is the one bad page reference**: in the 1911 Concise on disk, gazelle/gazette sit on leaf 195 (≈ printed p.175); printed p.209 is the H section (HOARSE…HOLE). Recorded as `not_found` with the calibration.
- KLN page offsets check out exactly: leaf 348 = p.644 (gazelle/gazette), leaf 350 = p.648 (genizah) — Klein's *genizah* entry alone underwrites ganj → Aram. ginzā/gazzā, Arab. janaza, Gk. γάζα > L. gaza, gazette, and Gaspar/Jasper.
