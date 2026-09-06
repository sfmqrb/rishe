# Verification process log — verify-page-176


## [2026-09-05T20:50:14.327Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 176 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-176.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-176.json. Write /home/sfmqrb/git/rishe/data/verification/page-176.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 176` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-05T20:50:15.856Z] AGENT

I'll start by reading the instructions.


## [2026-09-05T20:50:16.568Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-05T20:50:16.579Z] TOOL RESULT

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


## [2026-09-05T20:50:16.892Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-176.txt"
}
```


### [2026-09-05T20:50:16.904Z] TOOL RESULT

```
1	=== PDF page 176 (book page 146) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Gĕu 1, Gu; Keu 1, Keup, Kumb, Kub, Keub, Keuk 2 : to bend; to bend, curved, hump  (refs POK:394-398; POK:588-592)  PART 1
4	#1 (parent #0) [Avestan] refs=POK:398 | gaošaka : corner
5	  #2 (parent #1) [Persian] refs=BQT:1859 | gŭšeh «گوشه» : corner
6	  #3 (parent #1) [Persian] refs=BQT:1731 | kŭšk «کوشک» : a room at the top corner of a castle, castle | extra: کوشه
7	    #4 (parent #3) [Turkish] refs=KLN:847 | kiošk : pavilion
8	      #5 (parent #4) [French] refs=None | kiosque
9	        #6 (parent #5) [Persian] refs=MON:3160 | kîŭsk «کیوسک» : kiosk
10	        #7 (parent #5) [English] refs=KLN:847 | kiosk
11	#8 (parent #0) [Avestan] refs=SYN:1051; SNS:90 | gaona : hair, hair color ; hamo-gaona : all colors (everyone) ☞Sem 1 ; nî-gaona : downward ☞Nî 1
12	  #9 (parent #8) [Sogdian] refs=SOD:174 | gwn`k : hair
13	  #10 (parent #8) [Pahlavi] refs=BQT:671 | gôn : color ; cigôn : how ; hamôgĕn : all ; ni-kŭn : downward
14	    #11 (parent #10) [Persian] refs=BQT:1861; MON:3473 | gŭn «گون» : color ; negŭn «نگون» : downward ; zargŭn «زرگون» : golden, a yellow mineral ☞Ghel | extra: چگونه ، چون ، همگی ؛ سرنگون ، نگونسار
15	      #12 (parent #11) [French] refs=None | jargon : a yellow mineral
16	        #13 (parent #12) [English] refs=AHD:1489 | zircon, zirconium
17	          #14 (parent #13) [Persian] refs=None |  | extra: زیر کونیم
18	#15 (parent #0) [Avestan] refs=POK:394 | gunda : ball of dough
19	  #16 (parent #15) [Persian] refs=HRN:209; BQT:1843 | gondeh «گنده» : a lump of dough, large
20	#17 (parent #0) [Pahlavi] refs=POK:396 | gumbat : dome
21	  #18 (parent #17) [Persian] refs=MON:3396; BQT:1836 | gonbad «گنبد» : dome
22	#19 (parent #0) [Persian] refs=POK:395; POK:589; LAT:488 | ğŭz «غوز» : a lump on the back bone ; ğŭzak «غوزک» : ankle | extra: قوز ، کوز ۲ ، کوژ ؛ قوزک ، گوزک
23	#20 (parent #0) [Old Persian] refs=KNT:178 | kaufa : mountain
24	#21 (parent #0) [Greek] refs=AHD | guros : ring
25	  #22 (parent #21) [English] refs=None | gyroscope
26	
```


## [2026-09-05T20:50:20.776Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-176.json",
 "description": "Read source JSON for page 176"
}
```


### [2026-09-05T20:50:20.816Z] TOOL RESULT

```
{
  "pdf_page": 176,
  "book_page": 146,
  "entries": [
    {
      "root": {
        "name": "Gĕu 1, Gu; Keu 1, Keup, Kumb, Kub, Keub, Keuk 2",
        "lang": "Indo-European",
        "refs": "POK:394-398; POK:588-592",
        "gloss": "to bend; to bend, curved, hump",
        "note": "Compare with root \"Kam 2:to bend\""
      },
      "part": 1,
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:398",
          "words": [
            {"translit": "gaošaka", "gloss": "corner", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT:1859",
          "words": [
            {"translit": "gŭšeh", "gloss": "corner", "script": "گوشه"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT:1731",
          "words": [
            {"translit": "kŭšk", "gloss": "a room at the top corner of a castle, castle", "script": "کوشک"}
          ],
          "script_extra": "کوشه",
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Turkish",
          "refs": "KLN:847",
          "words": [
            {"translit": "kiošk", "gloss": "pavilion", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "French",
          "refs": null,
          "words": [
            {"translit": "kiosque", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "Persian",
          "refs": "MON:3160",
          "words": [
            {"translit": "kîŭsk", "gloss": "kiosk", "script": "کیوسک"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 5,
          "lang": "English",
          "refs": "KLN:847",
          "words": [
            {"translit": "kiosk", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 0,
          "lang": "Avestan",
          "refs": "SYN:1051; SNS:90",
          "words": [
            {"translit": "gaona", "gloss": "hair, hair color", "script": null},
            {"translit": "hamo-gaona", "gloss": "all colors (everyone)", "script": null, "see": ["Sem 1"]},
            {"translit": "nî-gaona", "gloss": "downward", "script": null, "see": ["Nî 1"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "Sogdian",
          "refs": "SOD:174",
          "words": [
            {"translit": "gwn`k", "gloss": "hair", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 8,
          "lang": "Pahlavi",
          "refs": "BQT:671",
          "words": [
            {"translit": "gôn", "gloss": "color", "script": null},
            {"translit": "cigôn", "gloss": "how", "script": null},
            {"translit": "hamôgĕn", "gloss": "all", "script": null},
            {"translit": "ni-kŭn", "gloss": "downward", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 10,
          "lang": "Persian",
          "refs": "BQT:1861; MON:3473",
          "words": [
            {"translit": "gŭn", "gloss": "color", "script": "گون"},
            {"translit": "negŭn", "gloss": "downward", "script": "نگون"},
            {"translit": "zargŭn", "gloss": "golden, a yellow mineral", "script": "زرگون", "see": ["Ghel"]}
          ],
          "script_extra": "چگونه ، چون ، همگی ؛ سرنگون ، نگونسار",
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 11,
          "lang": "French",
          "refs": null,
          "words": [
            {"translit": "jargon", "gloss": "a yellow mineral", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 13,
          "parent": 12,
          "lang": "English",
          "refs": "AHD:1489",
          "words": [
            {"translit": "zircon, zirconium", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 14,
          "parent": 13,
          "lang": "Persian",
          "refs": null,
          "words": [],
          "script_extra": "زیر کونیم",
          "note": null,
          "quote": null
        },
        {
          "id": 15,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:394",
          "words": [
            {"translit": "gunda", "gloss": "ball of dough", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 16,
          "parent": 15,
          "lang": "Persian",
          "refs": "HRN:209; BQT:1843",
          "words": [
            {"translit": "gondeh", "gloss": "a lump of dough, large", "script": "گنده"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 17,
          "parent": 0,
          "lang": "Pahlavi",
          "refs": "POK:396",
          "words": [
            {"translit": "gumbat", "gloss": "dome", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 18,
          "parent": 17,
          "lang": "Persian",
          "refs": "MON:3396; BQT:1836",
          "words": [
            {"translit": "gonbad", "gloss": "dome", "script": "گنبد"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 19,
          "parent": 0,
          "lang": "Persian",
          "refs": "POK:395; POK:589; LAT:488",
          "words": [
            {"translit": "ğŭz", "gloss": "a lump on the back bone", "script": "غوز"},
            {"translit": "ğŭzak", "gloss": "ankle", "script": "غوزک"}
          ],
          "script_extra": "قوز ، کوز ۲ ، کوژ ؛ قوزک ، گوزک",
          "note": null,
          "quote": null
        },
        {
          "id": 20,
          "parent": 0,
          "lang": "Old Persian",
          "refs": "KNT:178",
          "words": [
            {"translit": "kaufa", "gloss": "mountain", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 21,
          "parent": 0,
          "lang": "Greek",
          "refs": "AHD",
          "words": [
            {"translit": "guros", "gloss": "ring", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 22,
          "parent": 21,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "gyroscope", "gloss": null, "script": null}
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


## [2026-09-05T20:50:20.845Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-05T20:50:20.878Z] TOOL RESULT

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


## [2026-09-05T20:50:56.706Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','BQT','MON','KLN','SYN','SNS','SOD','HRN','KNT','AHD','LAT','BRT','PHD','NYB','HUB','WLD','IEC','TTS','LKT','SKT','DEV','PHN','ARY','FSD','WEB']:\n    v=d.get(k)\n    if v is None: print(k,'MISSING'); continue\n    print('==',k, json.dumps({kk:vv for kk,vv in v.items() if kk!='scans'}, ensure_ascii=False)[:700])\n\""
}
```


## [2026-09-05T20:50:57.179Z] TOOL CALL #6: Bash

```json
{
 "command": "ls data/verification/ | head -50 && echo --- && ls tools/"
}
```


### [2026-09-05T20:50:58.397Z] TOOL RESULT

```
== POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index 
== BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.c
== MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol 
== KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt", "page_offset": "KLN_1966: TWO pri
== SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<i
== SNS {"title": "Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/VajnameShayest", "lookup_hint": "grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php search (see BQT) for better hit-to-leaf mapping.", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS.txt"], "page_offset": "242 leaves; page offset not determined (OCR too poor to read printed numbers) — 
== SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get s
== HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or grep the 
== KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt", "page_offset": "leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archiv
== AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only", "identifie
== LAT {"title": "A. Ernout & A. Meillet, Dictionnaire étymologique de la langue latine, 3rd ed., Paris 1951", "edition_found": "1951 (3rd ed.) - matches Nourai", "kind": "archive_djvu", "url": "https://archive.org/details/ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine", "identifier": "ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine (4th ed. 1959 lending-only: dictionnairetymo0000unse; another open copy: DictionnaireEtymologiqueDeLaLangueLatine)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LAT.txt", "page_offset": "leaf = printed + 18 for most of the book (e.g. leaf 21 = p.3); drifts in places (leaf 219 = p.301 -> -82?? probably a mis-detec
== BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \\f between 
== PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<ident
== NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Nourai's 'NYB' nu
== HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by parag
== WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.39015066210397 (browser only from this host)", "identifier": "in.gov.ignca.20339 (Band 3); also in.ernet.dli.2015
== IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Reconstruct
== TTS {"title": "H. Vámbéry, Etymologisches Wörterbuch der turko-tatarischen Sprachen, Leipzig 1878 (repr. Osnabrück 1972)", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/etymologischesw00vmuoft (Toronto scan; also Google/bub_gb copies)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_vambery1878_uoft.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_vambery1878_uoft_djvu.txt"], "page_offset": "TTS_pages.txt: 253 leaves; printed page N = leaf N+30.", "lookup_hint": "Not searched exhaustively 
== LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Numbered entries: 'NNNN. word (language) meaning' - Lokotsch is usually cited by entry number, but Nourai cites pages.
== SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<i
== DEV {"title": "L. M. Devic, Dictionnaire étymologique des mots français d'origine orientale, Paris 1876", "edition_found": "1876", "kind": "archive_djvu", "url": "https://archive.org/details/dictionnairety00devi", "identifier": "dictionnairety00devi (also dictionnairetym02devigoog, fr105comparative41)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/DEV.txt", "page_offset": "leaf = printed + 26 (pp. <80) to +30 (pp. >84), e.g. leaf 29 = p.3, leaf 118 = p.88. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "French headword in caps at line start.", "no
== PHN {"title": "A. P. Pihan, Dictionnaire étymologique des mots de la langue française dérivés de l'arabe, du persan ou du turc, Paris 1866", "edition_found": "1866", "kind": "archive_djvu", "url": "https://archive.org/details/dictionnairetym01pihagoog", "identifier": "dictionnairetym01pihagoog (others: bub_gb_QnsSAAAAIAAJ, dictionnairetym00pihagoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHN.txt", "page_offset": "leaf = printed + 31 (e.g. leaf 33 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "French headword in caps at line start;
== ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY:<printed page> --image", "local_file": ["/home/sfmqrb/git/rishe/
== FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-Dive), in.ernet.dli.2015.272042 (vol II), in.ernet.dli.2015.83695 (vol III), in.ernet.dli.2015.147440 (vol IV Sabi-Z)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt", "page_offset": "vol1: leaf = p + 41..56 (drifts; e.g. leaf 87 = p.46, leaf 612 = p.556); vol3: le
== WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w (restricted full copies: webstersnewtwent00webs_0 1977, webstersnewtwent01webs 1983)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/WEB_vol1.txt", "page_offset": "not reliably detected (page_numbers.json sparse); grep headword. local
```


### [2026-09-05T20:50:58.461Z] TOOL RESULT

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
---
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
```


## [2026-09-05T20:51:01.161Z] TOOL CALL #7: Bash

```json
{
 "command": "sed -n 1,200p /home/sfmqrb/git/rishe/tools/verify_check.py"
}
```


### [2026-09-05T20:51:01.200Z] TOOL RESULT

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


## [2026-09-05T20:51:02.070Z] TOOL CALL #8: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('/home/sfmqrb/git/rishe/data/verification/page-127.json'))\nprint(json.dumps(d['entries'][0], ensure_ascii=False, indent=1)[:3000])\""
}
```


### [2026-09-05T20:51:03.862Z] TOOL RESULT

```
{
 "entry": 0,
 "root": "Dhem",
 "verdict": "confirmed",
 "modern_form": "PIE *dʰemH- (LIV² *dʰmeh₁-) 'to blow, breathe; to smoke, raise dust'",
 "note": "Pokorny IEW 247-248 heads the entry 'dhem-, dhemə- \"stieben, rauchen (Rauch, Dunst, Nebel; nebelgrau, rauchfarben = düster, dunkel), wehen, blasen (hauchen = riechen)\"', so Nourai's language label (Indo-European) and his gloss 'to make vapor, raise dust' are an accurate short rendering of the German. Cheung (Etym. Dict. of the Iranian Verb, *damH³) writes the same root «PIE *dʰmeH- 'to blow' = LIV: 153 | Pok.: 247 f.»; Wiktionary reconstructs *dʰemH-. Watkins/AHD carries no dhem- root (its list goes dhembh- → dhen-¹), simply because no English word reaches it through Latin or Greek, so its silence is not a disagreement. Two weak spots in the chart: the Avestan node's gloss (node 1) and the name Damāvand (node 2), which Nourai's own source BQT:878 derives from a different root.",
 "note_fa": "ریشهٔ نمودار همان ریشهٔ هندواروپاییِ آغازینِ *dʰemH- «دمیدن، فوت کردن؛ دود و بخار برخاستن» است. پوکورنی در صفحهٔ ۲۴۷ کتاب خود آن را با معنای آلمانیِ «stieben, rauchen … wehen, blasen» آورده و برگردانِ کوتاهِ نورایی («بخار ساختن، گرد برانگیختن») با آن می‌خواند؛ چونگ نیز همین ریشه را *dʰmeH- «دمیدن» (LIV ۱۵۳) می‌نویسد. پس جعبهٔ ریشه، برچسبِ زبان و معنای آن درست است و ادعای نورایی در این حد پذیرفتنی است. تنها دو نقطهٔ سست در نمودار هست: معنایی که برای صورتِ اوستایی داده شده (گرهٔ ۱) و نامِ «دماوند» (گرهٔ ۲) که خودِ مأخذِ نورایی، یعنی حاشیهٔ معین بر برهان قاطع ص ۸۷۸، آن را از ریشهٔ دیگری می‌گیرد.",
 "sources": [
  "https://en.wiktionary.org/wiki/%D8%AF%D9%85%DB%8C%D8%AF%D9%86",
  "https://en.wiktionary.org/wiki/%D8%AF%D9%85"
 ],
 "ref_check": [
  {
   "ref": "POK:247",
   "status": "supports",
   "note": "POK_01.txt (grep -n 'dbem-' → line 3513), IEW p.247: 'dbem-, dhemo- ,stieben, rauchen (Rauch, Dunst, Nebel; nebelgrau, rauchfarben == düster, dunkel), wehen, blasen (hauchen = riechen)'; the page continues 'Ai. dhámati ,bläst', av. daδmainya- …, npers. damīdan ,blasen, wehen', dam ,Atem, Atemzug''. Exactly the root box as drawn."
  }
 ],
 "consulted": [
  {
   "src": "WLD",
   "where": "Bd. I 851 f. (WLD_Bd1 djvu line 53642)",
   "stance": "supports",
   "note": "'dhem-, dhemə- „stieben, rauchen (Rauch, Dunst, Nebel; nebelgrau, rauchfarben = düster, dunkel), wehen, blasen (hauchen = riechen)“. Bedeutungsumfang wie bei Wz. *dheu- „stieben“.' — the source Pokorny 247 abridges."
  },
  {
   "src": "CHEUNG",
   "where": "s.v. *damH³ (CHEUNG.txt line 4670 ff.)",
   "stance": "supports",
   "note": "'*damH³ \"to blow, breathe; to swell\" … «PIE *dʰmeH- \"to blow\" > LIV: 153 | Pok.: 247 f.»'"
  },
  {
   "src": "AHD",
   "where": "Watkins 1985, d-list (AHD_watkins1985.txt line 377)",
   "stance": "silent",
   "note": "the appendix runs 'dhembh-. To bury. … [Pok. (dhembh-), dhmbh- 248.] dhen-¹. To run, flow.' — no dhem- entry at all, since no English word descends from it via Latin/Greek."
  },
  {
   "src": "IEC",
```


## [2026-09-05T20:51:08.660Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for f in POK_01.txt POK_02.txt POK_03.txt; do echo \"== $f leaves: $(awk 'BEGIN{RS=\"\\f\"} END{print NR}' $f)\"; done"
}
```


## [2026-09-05T20:51:09.590Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"gaoša\\|gaosa\\|gaoša-\" BRT.txt | head -40"
}
```


### [2026-09-05T20:51:10.788Z] TOOL RESULT

```
== POK_01.txt leaves: 363
== POK_02.txt leaves: 433
== POK_03.txt leaves: 429
```


### [2026-09-05T20:51:10.832Z] TOOL RESULT

```
5955:asrutgaosa-
9893:KompE.  —  Komp.:  gaosa-+*d-iiara-  (zum  V. 'Äd-,  S  2**37)  m-  'wasiraOhtEetragen  wird'.
14496:•  j.  9-raDh-  n.  'Mund':  -arg  (NS.)'>  F. 23.  a)  Du.  'die  Mundwinkel' :  nazdyd  . . ya^a  *näaha  haca  *gaosalibya  yaha vä  gaosa  haca  ^'anhibya'^  "näher .. als  die Nase  von  den  Ohren  oder  als  die  Ohren von    den   Mundwinkeln   (entfernt    sind)"
18941:•  j.,  p.  nah-  m.  'Nase',  Sing,  und  Du.: Waäamsaiy  uta  nüham  utä  gausa  fraja- nam  Bh.  2. 14;  13;  —  yim  yava  vatim närahabya  hubaoüitim^m  ßgaurva  H. 2.8;  26;  —  t^m  vahm  ninhaya  (LS.)'> *uzgnmiiiysil.2.8;  a6;  —  «Jw^a  (ND.)'' F.jd; — yaha  *nänhai''  Aaca  *gaoSaäbya ydha  vä  gaosa  Aaca  *^raaAiiya  (sd.)  P.  28.
21124:2  a):  mit  tnaslm  ,  .  masyä  hacaite  J^fnJJ  möglich  oder  denkbar  hingestellt;  nur  c)  im xratu^ y  mtir»mcii  ..  halatie  äinasHl\\Pi.vt.\  a)  mit  Opt:  hö  mqm  ava'ha xratusYt  10.107.  zuzb):  hsuca  ..vohu^VTrmqm  nijaintHsÄ.)  y  v»Arkd..barf%ryät manB jiig)r)bustarU  anhai yS ..y  häti y5 ..  \^/iaca pui:r»m  midafy.dairyat(sd.)'V.iff.3S V.4.48;  F._yf,  V. /_J.  42,  43;  — ■  staotärpm' — y  .,  nmänS.paitim  paiti  tard.pikwtm vaf9hat?h>m  , .  aoxta  ahurS..y°  aäm  yat  .dai^yät  aha  astryäti  V.y.20;  A-^J.?; vaAist?mY.i0.g;  —  nazdyS akmi ..vTspahe\ —  th  yüioyänti  .,  mqnaytn  ake  y  .. ar?hsui*'maiiihca .  .y  Stsha  haca  *gaosalibya  \  ra%ailta  . .  haca  saäst  (sd.)  .  .  paiti.yntta y  vä  gaosa  haca  *%rar»hibya  (sd.)  P.  26';  I  Yt /J.  67;  —  tä  he  stiai^iifia  var^'äjosca
21933:nazdyö  ya%a   änha  haca  *gaosalibya  ya%a
21934:V  gaosa  haca  *'^ranMbya  'P.28;  V.S.22 PUZ.(?};  —  yai^a  .  .  asii  .  .  ganmshva (sd.)  vfdante  yal  v° . .  ganma  (sd.)  3^ar3%  a stamamm  vä  (zu  III)  hisvam  vä  apa.- dazai  V.  15. 4 ;  —  yat  hl  nazdistS  dahmS  vJ.- srunvaili  (sd.)  yavat  v  atm  aitn  havaiibyä unbya  N.  27;  —  yat  hxi  spä  .  .  aiwi.- vantaiti  .  .  vayB  v  hl .  .  avi  usvataite FrW.  U;  —  ayatthainaU  kantais  atdibli paiti  ava.hr3%yät  (sd.)  .  .  masyS  (sd.)  v akmstcit  V.4.50.  II)  v  steht  beim zweiten  und  den  folgenden  Gliedern;  zu  I); B)  im  gAw.:  d?manahyä  xsdisnm  ssi- hrahyä  v  dahySu^  v°  "domus  regnum vel  pagi  vel  provinciae"  Y.jr.  16;  — "ä  *«I d^mätum  vls>m  v'  iöi^rtm  v  dahyüm  v° adät  duStäiiä.)cä  . .  Y.J/.  18.  C)  im jAw.:  yasca  ,  .  bayqm  ahunaht  vairyeJte maräl  frä  v°  marS  dr?njayäi  frä  v  drvn- /ayö  srävayät  frä  »• . .  Y.  jg.  6.        zu  2);
26761:avatghtm  (sd.)  Y.jrf-4;  ^T.  vciwcndel    Ny.       „  ^  AKri-i;  vgl.  »neh  «e»..  mhd.  j^^  'steif. J.  10;  — _y5  ^ijH   ahmäi  västravaitim  stsi       itatüich';  Bthl,  IF.  ii.  ijS. »tTj-J/fSp.  i38so.)  Y.50.2;— ^^"/(f  WT'«Ä/  ,  j    stiptay-  £  Name  eines  Insekts,  das *ustä  *j/»"    "denen  wir  beide  wünschen,   auf    Hunden    sclimaroUt':     duye    navaüi dass    es    ihnen    nach    Wunsch    gehe"    ^.  galwqm  pairi.yaoidaihtta   -tibyasca    ans- 4ß-i6;    —    a/    "i-^J    »tStighi    *J>aourvm  iritib}asca    -.yamiraHbyasca    vUpaäbyasca mazää  *ya^m  (sd)  stSi  Y.31.8;  —  nSil  pairi  aHitaäbyS  ySi  gahwam  pairiiavaiti spmiqm    dSTist  (Sp.  690  a)    ahmäi    stü  "zweimal  neunzig  Hunde  soll  er  von  St. armaitlm   \.4g.2-,  —   Ayat  ..  Bist  (Sp.   reinigen   und  von  An.  und  Vy.   und  von 430  m.)  ..  ahmäi  slH  dqn  ^JA  K/<7yfii/7|  ^11  den  bösesten  (Insekten),  die  auf  Hunden \.4S.io;  —    data  xratius  hixi-3  rai^ltit   schmarotzen"  V. 74.17. (sd.)  stöi  mahyä  räifng  .  .  iähil  ¥.50.6;!      Eig.  Bed.   und   Et.?    —    Pa,:    ddrptkrak, —  tum  tiB  äiraom  *tafftasU'>  "du,  O  A>.,  I      halb  {jap)  twtsskr. sollst  unser  Z.   sein"   Vr.j.7.        a)  im  •  j.   stivant*  in.  EN.   eines  Gläubigen: jAw,    mit    der   Negation,    in    altnbuüveja  /r3dat.vawhfus  •talö  aiaotiS  Yt  IJ.  121. Gebrauch  'der  nicht  existireQ  kann,  den      Ablcit.  mos  'siay-i    Bed.7 es  nicht  geben  kann' ^:  nöil  ma^S  gal^yj   •    j.    siai',    sli'i',    nur   KompA.:    sva. Sil  agjä  (sd.)  sunaiaoiti  gaosaiwe  "es  gibt ;  "stüra-.
27909:•  j.  zaranyo.pis-,  **pi9--  Adj.  (auch  fem.) 'goldgeschmückt':  yS  paoiryS  °pTsS  srirä barssnava  ginwnaiti  "der  als  erster  die goldgeschmückten  .  .  Höhen  erklimmt" Yt.  JO.  1 3 ;  —  fr3  gaosavara  sisptmna  .  . minu{%A.)ca  -/m  (ADf.)'>  YtJj.io;  — ya^a  vil  *>r?tats.pai'hi  (sd.)  yaia  vä *-pafki  {K'Pa.)''^  ydha  v<t  *kilat  gaonaiiam Aog.  ly.
27921:•  j.  zairi.gaosa-  Adj.  "mit  gelben,  gold- farbigen Ohren':  spanim  .  .  spaStim  'sim V.if.  16'  17,  18;  —  aspahe  ..  aurus'afie .  .  'sähe  Yt.Äi8.
28980:Sp.  928  o.)  ist  weggelassen:  danys.Hli (sd.)  ile  vTse  afrJnämi  yahmat  h°  imti zaoira  y.SS.i^;  \t.  S.  4'.  '  b)  bei NomiDa";  o)  bei  verbalen  Substantiven: raiis  i&i.;  'decessum')  rm  A^  ariha  ztmat vaähs  k^nnaoili  Vt.  17.  20;  —  spmtat  h" mainyaot  aisam  ahr^m  ('origo')  FrW. 70,40;  —  yä  h"  daSnayUt  .  ,  apastüilis ('abdicatio'j  ^.4J-  ß)  bei  Raumwörtera: dsräl  Cprocul')  A'  ahmiil  nmänät  .  .  ays i^yejä . .*yeyenH yeAhe ..  Y.57,  14;  14';  — nSii . .  *dräjyS  ('longius')  *'iyeillm  framraomi (sd.)  . .  ä/rllim  yUnat  -4'  .  .  P.  7j;  — nazdyS  ('propius')  ahmi  . .  yaia  änha  k' *gaosaHöya  P.  2  V;  28;  —  airime  gätüm hs nUhthaüta  . .  *psr3ntanm  (sd.;  'seorsum') h'  anyanbyS  mazdayasna^byS  V.g.  33;  29; —  aiai  dräjö  ('quantam  longitudinem')  h* i!^ral\.  3. 16;  16^;  — yS  hn%rS.masar»h3m iS/wamm  ('viam  miUe  passuum')  h'  vizibys paräiti  V.  JJ.  18;  —  äiat  ('quantum*)  h' mtiya^bya  Y.i).  10;  8f.';  —  avavat  ('tan- tum')  h'  paourt-aiibya  yäha  %rigilim  V. 1M39;  II,  76;  — yd  *yujyastxm  (sd.)  h' gat^abyS  parätti  'v.  7^.  17;  N.  8,  <??(?), V,_j.  17*,  J(5'.4*,  17. 4«,  b)  im  gÄw. a)  bei  Verben  (bei  solchen  der  Bewegung nicht  bezeugt):  frg  ma  sl/iJ  (Sp.  1575  o.) "iiwahmut  *vaoca^hl  *mainy}us  h'  'üwä Siaiihn  "..  pronuntiare  ex  tuo  , tuum  os"  Y.  28. 11;  —  ysi  gSus  h'  iyävtl (sd.)  "qui  a  bove  (habitant  sva.)  stant' Y.  J7.  a";  —  ka^ü  . .  zarjm  (sd.)  laränl h'  xsmap''  ",  .  impetrem  a  vobis  (sva. per  vos)"  Y.  44-17;  —  a^byS  mazdh  .  . xsäi^rät  A'  paifi.mraot  ". .  per  Regnum (deum)  respondit"  Y.ya.  2;  —  sonst mit  'asa-  A  (als  Gottheit)  im  Sinn  von 'peri^nim,  As'o  juvante  (u.  dgl.)':  aiät  h'
29707:gaosahe  Y.  j.  3;    —    mikräi  .  ,  'rö.gaoiäi  yäha   yat    'pam    halnam    avazöit  ,  ,  V,
29735:•  j.  hazaDrä.gaosa-  Adj. :  s.  unter  Aata- igra-g".
```


## [2026-09-05T20:51:15.181Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"gaona\" BRT.txt | head -30"
}
```


### [2026-09-05T20:51:15.231Z] TOOL RESULT

```
2461:—  ahmi  atskvö  yat  astvainti  V,  5.  Sprecher  vorgeschwebt:  jaji-a..  7rfJ»aVfl/ 39;  —  ai^hS  zimo  yat  faianaya  Yt  w.  poHbm  hl  matw  .  .  nöit  zT  ahmi  paiti 95;  — ■  anhqm  dämanqm  yat  ahurake  .  ..nairi  .  .  V.  7.51  f.;  _j.zi;  —  ^aei  iskata dätarasca  ,  .  Yl  ig.^Si  —  ar>zahiby5  sa- '  .*aoi  spita.gaona  gairi  aat  äkva  paurva- vahUyB  .,  aheca  iarsvanf  yat  :i^anira-)tähva..\.lo.ii{.; — *unäAva..raBsayaca  aal '^ahe  Vr.  70. 1 ;  — yat  ahmi  nmSm  yal^  ähva'  iyar»^ähva' {^'^  V.iy.zi.;  —  vasö »»äaÄy(MHÄ/(Stverz.)  "wenn  hier  im  Hause '/fljc'äö'fl  mazdayasna  aits  pa'^h  frayqn  . . eines  M.  .  ."  V. 5. 4 5 ;  usw. ;  — ■  aitihä  dae-  ahe  nmänahe  myasd»m  dai'^yärys  V.  S.xz; naya yat  ähuröHY .60.1;  Yt  jj.gg;  Y.  Ä  7  ■  10;  —  asfmacrjS  ,  .  yS  altahmi  aahvS  .. {•MO  yä  ahairU).  b)  substantivisch,  am  faitiMiuaiti  a  dim  näii  apivatäite  . .  para gAw.,  von  dem,  der  so  bekannt  ist,  dass  ns  ahmai^  atat?halca  soi'iraatca  ..\.g. ein  'er"  genügt,  ihn  zu  bezeichnen  ('Er'J,|52f,;  — yasca  ..  imat  ..  i<acS  fravaoc^ von  AaraMainyav :  yl  ml  nä  manxiaiti\ .  .  nsit  dim  yava  aii'ihe  ayqn  nöit  airika anyä>ä  (sd.)  ahmjt  Y.5/.10.  II)  iu'.xsafS  ..  Yt.ii.^t^^,  —  y/üse  mq>rahe schwachdeiktischemSinn 'dieser,  der,  er":  a^,;  ar  «ä  *sravat?hs . .  N.22;  —  vispim 1)  auf  Vorhergenanntes,  Vorausgehendes:,,  aya  ratu/rita  (näml.  Y.55.1— 5;  LS. (Wort  oderSatz)  zurückweisend;  i)  auf|  als  Instr.)  hvävayanh>m  .  .  paiti.barähi ein  Substantiv  oder  subsL  Pronomen;  a)  ad- ;  Y.  55.4.  o)  Das  adjekL  Pron.  steht,  wo jektivisch:  spinti  mainyü  .  .  ahyl'  *main-'AKi  Römer  die  Gen.  von  is  brauchte  (s. yius..ahm3t*mainyiusM.4y.i—^;  —  vaa-\  I  aaa,  23  aa):  aSe  mazdayasna  ..  atarj- hius  ivistl  manatshö  .  .  ahyä  vaahiul  tqm  aSoAmiti  naire  frabäraytn  .  .  yai manaahd  Y.  34-  9  f. ;  —  alnaahqm  . .  aisqm  ,  also  nä  . .  haca  aiibyö  nm3nalibyS  xsnütö alnaahqtn\.^2.it.;  —  tä ..  mainyü  {ai).)\.  .  pärayät  ",.  ex  eorutn  domis  . ."  V,^. ,,  ayä  *mainivä  ..  ayä  Y._J0.4— 6;  —  Äa-\  39;  —  yat  baväni  aiwi.vanyä  tq'irya- zaignm  yaexäinqm  .  .  balaar»  döi^ranqm  \  vant^m  . .  ahmt  gal^e  piianlhu  "dass  ich .  .    aal  äbyS  dei'iräbyB    ai-uiyasca    (DPf.)  [  Sieger  werde  über  den   7:  .  .  im  Kampf
2531:y.  I ;  —  cayö  'te  raola  at»A)n  . .  yö  ava^a  '  vayrjanake  .  .  yat  °&o  kanjasante  paouru Sraoiayeite'^.2.^<j\  —  "taFsva  daxtnaih'a .gaonaAec'a  IsA.)  . .  ti.6^\  yi(7);  —  taotarf yöi  faiti  äya  z^mä  iavainti  "V.y.^^;  — ^.gstava  ..  ■""'oa'*  ..  N-tVi;  —  yetiAe  'oa "U  malsma  .  .  yaHbyö  .  .  framayattte  V. .  mazdayasnanqm  näirika  . .  *ham.raf^wa- (S'.ii;  —  'taisam  syao^nafiam  yöi  v»r>-  yeiti  "wes  von  den  M.  Frau  dort  . ."  N, sjbA'  masy.lka  V.  J5.2;  —  "tiitbyff  zao-  11;  —  ava'ia  ''QrtV.4.50;  —  taica  "'jaca >rabyö  ..  yämham  ..  N.  71;  —  ku^a  -tat  pü^nm    baraili    Y.iy^^if).  a)    mit
2559:;j.  I ;  —  cayö  'tt  raocii  atjhin  . .  yö  avaha  '  v(rf'ianahe  .  .  yat  '6a  han)asSnte  paouru Sraoeayeite\.2.y);  —  'tae^va  äaxmagh'a,gaonaAe^a  (sd.)  ..  N.f*j;  "/(?);  —  saetari frV  paiii  3ya  ztma  bavainii  V.7.54;  ■ — \gätava  .  .  *'oa'>  ,  ,  N.  A;  —  yetiie  '6a "le  malsma  .  .  yaiibyö  .  .  /rasnayiinte  V. ;  mazdayasnanam  näirika  . .  *hqm.raEä:wa- J'.ii;  —  'taiiam  syao^naiiqm  yöi  V3r>-  yeiti  "wes  von  den  M.  Frau  dort  . ."  N, ziiiti  masyjka  V. /j.  2;  —  "täibyö  zao-  11;  —  avaoa  °oa  'V.4-50;  —  taica  °üaca 'irJbyß  ..yäakqm..  N.  7/;  —  iu>a 'tat  pu>nm    baraiti    V.  15. 49(?).  a)    mit
5771:—  yai  nsit  sün}  .  .  a3atf/iqm  °tqm  .  . bannhm  (sA.) /rafasqn  V,  6.46;  —  'ti'a (AP.)  gaonaca  *dmi}'iaca  Ytij.  11;  —  yS süne  .  .  'tanqm'-''  (als  Obj.)  ahmarslanqm da',aiti  . .  yaica  alle  'ti  (NP.)  dälshva arSnte  V./3.3f.;  —  "tfin  .  .  *maslrr/nqm F,_y  c ;  —  ayanhaHiäis  kantlU  asdibls  paili
6991:dt'a:  /rasa  frayäi  (sd.)  vahi^jm  ä  ahUm ä  V.  J|V,  29;  —  avi  Um  spayat ..  UmS  äca va^ö  dia  acisUm  Sca  aküm  <J  V,_^.55*>;  — bufvm  ä  ¥.4^.  ß)  'bei,  an,  auP:  iatär^m ä  angrö  (sA)  vs  ,  .  Y,44-i2;  —  dasttum J  vs  gaonavats  (sd.)  N.  ffj;  —  yäka särim^a^''  varsanqm  (sd.)  iarämi  Yt.  5. 77.  b)  zeitlich,  a)  'in,  bei':  tä  yüioyai^S J  rapi'iwifum  ervänam  "die  beiden  kämpf- ten in  der  Mittagszeit"  Yt.ÄaS;  Y.5.11; —  kävanJm  ä  ratüm  Y.g.\;  —  ai  a ^waAmäi  ä^rl  rätqm  n>ma»ia  ..manyai Y. 4.3. 9; —  ä paitiMnitlm  N. 2 (?).  ß)  'bis zu  -'  (nurKompA.;  s.  axlüirjm).  c)  'nach, gemäss':  var^m^a  (s.  *vära-)  Yt.j.iso,  i-].  2, *Y.  10.  \\.  2)  mit  Lok.;  'in,  auf,  a)  auf
7231:3h-  fraiä  fi-ayäi  (sd.)  vahi^fm  ä  akUm a  V.  iS.ig;  —  avi  /pm  spayat ..  e>m3  äea vaisB  ii'a  aastim  äca  ahuin  ä  V,_J.35";  — burum  ö  F.  4  a.  ß)  'bei,  an,  auf:  kalärSm ä  arigrS  {s,A.)  Vil  ..  \.  44.12;  —  dattnsm ä  vä  gaonavats  (sd)  N.  Ö5;  —  ya%a sanm'a^^  varsanqm  (sd.)  barämt  Yt.  5. , 77.  b)  zeitlich,  a)  'in,  bei':  ta  yaiiyaärS S  rapi>win?m  zrvämm  "die  beiden  kämpf- ' ten  in  der  MitUgszeit"  Yt.ÄaS;  Y.9.11; —  häi'anTiii  3  ratüm  Y.  p.  i ;  —  at  3' ^waAmäi  äire  rätam  mmaiihS  ..manysi\ Y.  4J.  9 ;  —  3  paiti-bsTfitlm  N.  2  (?).  ß)  'bis  ! zu  —'  (nurKompA.;  s.  3xtairTm).  c)  'nach,  j gemäss';  vamn^a  (s. ^vära-)  YL 5.1 30,  77. 2,  \ ''Y.  /o.  14.  2)  mit  Lok.;  'in,  auTj  a)  anf
7705:•  j.  ^razav-  m.  'Finger":  °zu  F.jg;  — ci'al  gaonahe  (sd.)  . .  ya  dvaHbya  "zubya *hiing3riwn,lt  N.  Ö5;  —  avaval  tafta  ydha kasistahe  (,  mawmaAe,  masistahe)  °svB sisV.6.10,  12,  14, /Ä44  PüZ.  a)  die Breite  der  Finger  als  Maasseinheit:  dva 'ZU  nismaAe  (sd.)  V.(j.6;  —  avavat  aipi yd^a  caiwärS  °zavö\.g.2();  —  cd^wSrö 'zvö  V.  6.  43,  f).  6.  [V.  iS.  2  PüZ. :  lies bai.intu\
8234:\pouru  gaonaAe  (sd.)  '^aA^a  N.  65;  65.
8857:(sA)  Jasti  N,/oj; — ^kaAyl^^"^  dahmanqm sao^räoa  (si)  *ratu/rU  N,  40 ;  —  draos (sd.)  z-iJ  paiti  söinma  unam  vä  katcit  vS paiti  sidaranqm  N.  IQO;  —  kahmäicit yanhqm  jasS  Yt  13.  41;  41,  V.  7.  7: —  yahmäl  kahmäiHt  na^nanqtn  va ä'ird  baoiöTm  baraiti  ahmst  kahmätHi naimanam  .  .  paiH.jasalH  ütars welcher  (Seite)  her  nach  irgend Seite  der  Wind  des  Feuers  Geroch  ver- breitet, von  der  her  nach  irgend  einer Seite  wendet  sich  ^.."  V.iV.So; — pasBm .  .  7-ohu^aorvm  vä  käcit  (IS.)  vä  gaona- nqm  hamS4;aontm  (sd.)  Yt.  8.  58;  *Aog. »7;  —  di^e  saite  kahyJat . ,  xrafstranqm V.  16.12;  —  kasatinm  kaAhhcit  va^wa- nqm  A.  j,  11;  — 'in  Verbindung  mit  anya- A(tj.  '.ilius  (]uispiam':  anys  kasat  ar?hsiis astiatö  N.  6j.  a)  Piur.  im  Sinn  unsres zurück  weisenden  'welche,  solche', Zeichnung  einer  uobestimniten  Zahl:  äjal aaaelqm  . .  hj/il  (APa)  upaÄsSi  (sd.)  N. io().  a)sva.|jedermann,  jeder,  quisque' fravalayS  . .  ijp^m  aZi?mnil  (sd.)  havä käHt  (NSf.)  näfäi  ". .  suae  quaeque  origini" Yt.  13. 66;  —  äai  anyähu  ratufrisu  latai>rS *kai3h^scil^^  bar?smqn  frastaraitys  (sd.) N.  ;o2;  —  sdäi  (sdl)  *Aahyä^t^*^  paiti V.33. 1 1.  a)  mit  Gen.  part:  hazatinm vairyaiiqm  . .  kßsalia  alsqm  vatryanqm  . . "tausend  Seebuchten  .  .  und  jede  dieser Seebuchten  . ."  Y.  Ö5.4;  4;  —  kasHt avAius' (sd.)  aslvate  F.  36';  P.  y,  V.  7.50, iO- 19,  P.43  (kakynat);  —  Hat  vö  kasat masyjiiqm  .  .  ¥1/5.53;  Vr.^.5;  — yäva- ranJ  kascit  sao^antqm  Y.12.J;  —  iäat tanuHam  V.  16.10;  —  ka^häscit  tanunqm H.  /.  5 ;  —  kahmai^t  häiqm  "Jedem  der Seienden"  Y.J5.8;  /fl.ii',  F.^b'«;  — kakyäcii  hstqm  V, /2, 4;  —  ijmcit  paiti cairusanqm  (Stverz.)  V.tf. 31  usw.;  — a^'ahe  pasvd  {sA.)  ..  aliiqm  *kakmaicit*''^ td'ia  */rayarihqm  (sd.)  N.  65.  a)  mit
9798:■gaona-  48a
9807:•  j.  'gaona-  n.  i)  'Haai':  astica  -naca (AP.)  *d3r>whaca  Vt.  13.1-1;  —  ^avat  'nahe avaharäp  yä  *dvaiibya  »nzubya  *Aart- g>r)wnät"'9i\t  viel  vom  Haar  (näml./an/ö) soll  man  hinzubringen?  Was  man  mit zwei  Fingern  fassen  kann"  N.  (*5;  —  yat aadha  *hanjasaiite  paouru  'nahe ''  u^aAe/a" "weil  dort  (am  Rückenhöcker)  reichlich Haar  und  Fett  zusammen  sind"  N.öj;  — navanqm  aspanqm  arsnam  'mm  barat airyama  "Haar  vun  neun  Rosshengsten brachte^."V.22.2o;  20^.  a)'Haarfarbe, Farbe' :  pasUnt  . .  aurusim  vä  ,  .  käcit  vä 'nanqm  Aamffgaarum  (sd.)  Yt.  A'.  s8;*Aog. ly.       3)  'Art  und  Weise'  (nur  Komp.).
9809:•  j.  "gaona-  m,  'Gewinn"':  yö  .  .  sqm ai'wi.v>rKyHti ..upa  he  'nsm  baraiH..yd^a
9812:gaonavant-
9824:mit  igaona-,
9825:•  j.  gaona'vant-   Adj.  'behaart,   haarig';
9830:'o/  gaonahe  (sd.)  avabarät  .  .  *dann3m   U-A,;  *Vd.  4\  —  nmafum  ..  ä%ravat^ a  va  *vat5  *bar}snv3  vä  paiH  vayhanaAe  ^-S-^i  —  airyamm  :fannU .  ,  'vaiflm
10068:mit  harn  i)  '(mit  einander)  zosammen- konunen,  -treffen  (auch  feindlich),  sich  zu- sammenfinden', Akt.undMed.:  yim  aiwits (sd.)  paoiris  apö  hqm  . .  jasßn/s{^PIA.)"i Yl.ifi.66; —  Aya^  hSm  spadä  aiiaocanhä (sd.)  jamactl  (3DKM.)  Y.  ^.  15;  —  yal spfl'ja  hanjasäiiU  (statt  Du.)  YL/4.43;  V.  7. 44;  —  atcS  hyat  13  kSm  mainya  jasaügm "und  als  diese  beiden  Geister  zusammen- trafen" Y.  30.  4 ;  —  yat  atima  *Aanja- sante'^^  pouru  gaonalie  (sd.)  u^akeca  N. ^5\  —  yi  pairi  barasma  kanjasrnte  N. 6'2(?),  3)  D  'sich  sammeln'  (miltärisch) : pasiU-e^  hami^''iyä  *ha''gmatä  (PPfP.)"' paraitn  .  .  hamaranam  {fartanaiy  "drauf sammelten  sich  die  Aufruhrer,  ste  zogen aus  ..  eine  Schlacht  zu  liefern"  Bh.  2.7, 10;  Äci,  II,  _j.  lo**'.  3)'zumAbschlüss
10228:ig.  i;  6',  66;  —  'rsU  ^uHjIar^nahe  Y.i. 14,  22.36;  Ny.5.  5,6,  FrW.5.  i;  —  airyB.- xs'uiai  haca  'rsit  :^anvant»m  avi  HrXm Yt5.6;  i.zZ,  5.4s,  &33,  Y.2.14,  Ny./. 8,  V.  22. 19,  S.  2. 9';  —  *aoi  spitagaona (sd.)  Hri  (AP.)  4>  Y.  jo.  1 1 .  [FrBy. :  lies gairi  ifrpzB.]
11496:raiti  V.4.  5;  13.  so.  zu  e):  °vat  alsqm upa.mqnqy^n  {sA.)  V.  12.  r;  i'.  a)  mit Gen.  part;  zua):  °vat  gaonahe  {iA.)  ava- iarai  N.  (»5;  —  'vat  na  ape  . .  xsäudri- nqm  .  .  paiti.baräi  N.  6'7;  6"^";  —  'vat nä  *nilfma  a&mahe  (sd.)  paiti,barS  ratu- /ris  N.  loO;  —  'vat  agtaaAa  SpS ..  V.6. 30;  —  'vai  .  .  avar^tanqm  ,  .  Vd.  2;  — 'vat . .  spgntahe  mainyjus  dämanam  hqm.- rai%wayäti  'val  paiti.ra^wayeiti  V,  5. ^^.  zu  d):  "vaiti  (LS.)  narqm  *haxts zaota  (sd.)    ratufri^  .  .    N.  20.  a)    mit
13052:•  j.  da^a-  Adj.  (fem.  °nä')  'recht,  dexter'; *Aaoys  'nö  F.jg;  —  kainayä  ,  .  «i/a  ka- ratta  hffyttmca  'ramca  'mmca  hSyümca  YL j.  131;  —  'Htm  hl  upa  ariiam'S.X.  10.  \QO', 99;  —  'tum  '*  upa  sraxtim  N.  -jg;  75;  — 'näl  *Aal  tiaemäl  (s±)  N.?»); — 'na  paiii ar3%at?ha  (sd.)  N.  65;  —  'tum  gaoS?m  V. Ä4+45,  5-»ö,i7,  y.32;  Ä46-70", 5.17—24",  /;.  33;  —  hävöya  dStvif  (sd.) •>iaca(lS.)  'na  bäsv&  ^kävayaea  V.j.2$;  — 'nam  (APm.)  aiigmtqm  V,<?.  71.  a)  ASn. 'tarn  als  Adv.  "rechts":  'tttm  hx  ^^^(sd.) vasaiU  .  .  Yt  10. 126.  A)  n.  und  f.  als Subst.  'die  rechte  Seite':  fravasays  .  .  yu oAuraAe  . .  'nqm  upa  yätöyeittti  Yt  13. 63; —  *'n?m  ä  gaonavatB(sd.)  N.65.  a)  sva. 'Westen"*:  ya'^a  vfitd..  ^zciiAot  (sd.)  'ttät fairi  fratmr^^it  'Von  Westen  her  .  ." V.^.4a.
13541:•  j.  '''darawÄa-"  a  'Muskelbiindel',  im Plur.  'Muskelfleisch':  asii/a  gaonala  "hala ^urUhwqm^a  Yt.  y.  11.
14885:—  paoiryS  gairiS  AqtnJtisiat  .  .  'ti  äya z^mä  YX.ig.i;  /O.  98,  /J.97,  Y.9.IS.  V, 7,  54;  —  nasunqm  yä  'ti  aya  zimä  irJri- ^ar»  V.5. 4;  — '11  karJ*  pärst^  hyJ'  vtha- (id.)patiy3'^  . .  Bh.  J.  4;  2.  5  (ergänzt);  — tiyri/  ,  ,  afanvaia  'ti  niral  (Sp.  184  o.) Yt^.  38;  —  dasina  'ti  ahoanha  "auf  der rechten  Seile"  N.  65.  4)  mit  Abi.,  nur räumlich;  a)  auf  die  Frage  woher?:  mihr>m .  .  yS  vlspfm  aAsm  . ,  ädiiäiti  haraihyat 'ti  bar3tanhai  Ytio.  51.  b)  auf  die Frage  wo?:  dunmqn  hqmJiiitinli  *iisMndvat °ti  garsit  YtS.32;  —  yim  yazata  ahurS mazda  raoxinat  'ti  gara  nmana£  Yt /0. 1 2  3 ; 5.25,45.  s)  mit  Gen.,  nur  raumlich; a)  auf  die  Frage  woher?:  naKa  dunmqn (sd.)  uzjasaiti  Aaraihyd  'ti  iamayä  Yt 10.  50.  b)  auf  die  Frage  wo?r  ^dasimm J  va  gaonavatö  (sd.)  ^banstrvS  va  'ti vayhanaAe  N.  65;  —  zqm  .  .  yetiAa  'ti  . . apa  taünti  Yt  jj.  9  f. ;  i  o ;  — y^iihe  nmämm ..vüätfm  banzi'te  paiti  bar^aAi (Sp.Ba^ u.)  AaraiiyS  'tt  banxayä  Y. 57.21;  19;  — ys .  .  Aaomq  utdasta  .  .  kara^yS  'ti  bar»- '  xayä  Ytio.  90.  c)  auf  die  Frage  wo- hin?: aurvantim  %wä  .  .  bcrjS  nida'iat .  . Aarai^yS  'ti  banzaya  Y.SO.  10.  6)  mit Dat(?)"'',  räumlich  auf  die  Frage  wo?: tarn  yazata  auf  .  .  daAakS  bawrsii  'ti daiiihaove  Yt.  5.  29.  3)  zum  Ausdruck des  Gleichkoromens,  Aufwiegens;  mit  Akk. 'gleichwertig  mit  — ',  bei  Ellipse  des  Verbums {'ah-):  ha  ml  baya  .  .  satam  'ti  anyaisqm ra^wqm  gä^anqm  "dieses  Stück  .  .  wiegt hundert  andre,,  auf  Y./^.S"';  15.  A)bes. zur  Angabe  dessen,  was  als  Preis  oder  Lohn geboten  oder  verlangt  wird,  'gegen,  um, für';  i)  mit  Akk.:  uzbasaui  'ti  ammxtttn (sd.) /rarazaite  miirS  Yt  10. 1 24.  a)  mit Lok.:  yehyS  .  .  vaAistptn  yesng  'ti  vaidä (sd.)   mazda  Y,  57.  2a;   27.15,  Vr.  16I3;
15180:•  j.  paidyä-  f.  'Fuss',  1)  der  Menschen: as/ica  gaonah  *dfr)w'haca  ^uruhwqmca •yäsfa(,AP,)/ravaxsascaYt.ij.ii.       2)  der
15661:•  j.  paount^gaona-  Adj.  'grauhaarig*: "rwM  F.^b.
16817:a)  '(Kleider)  herabziehen  sva,  von oben  her,  über  den  Kopf  her  anlegen'; yS  vastra  vastnm  *aiwyaithaysrii  *itzba- rmti  (sd.)  . .  uparat  ftaOnai  ava-bannti  . . N.pJ.  a)  'hinzu-,  herzubringen,  ver- schafien':  *yaoxHayS  ava-bantam  (statt Hur.)  F.  4  g;  —  cvat  gaonahe  (sd.)  ava.- barat  N.  65.  a)  mit  Angabe  des  wohin? oder  wem?,  a)  durch  avi  mit  Abi.:  ya^a ..amirjxtim  ava,baram  avi  mazdä  däma- iysYt.g.^;  9.  ß)durchGen.:  ya  vTspa- nqm  hairisinqm  .  .  rähwim  paima  ava.- baraiti  Y.  65.  2.  y)  «n^^-  Gen.-DaL  des Pron.:  ava  hl  gatam  baraym  afryeAe  (sd.) va  ..  V.  Ä  8;  —  Uta  hi  astunt  xratQm avaJiaraiti  vanma  (sd.)  Yt  //.  a;  V.  16. II.  3)  'etwas  anbringen  an—'  iupa mit  Akk.):  ava  hl  baraym  .  .  dsuru(sd.) Ufa  . .  manae^rfm  V.  13.  30.  4)  'etwas
21179:•  j.  ya3«  vä  part-artige  Verb.,  wieder- holt 'sei  es  . .  sei  CS  . . ,  vel  . .  vel  . .': y  va  *)r?tatö^ai^i  (sd.)  y  v3  *zaranyB.- pai%i  y  va  *iaäj  gaonanqm  Aog.  17.
21237:(sd.)  dngvanhm  avS  Y.32, 14;  —  täis  zl nä  /yao^anai/dyentf(sd.)..Ay  ('insofern') as  *aojS.  näidyankifn  (sd.)  Y.^J^.  8;  — vaidä  tal  ya  aAml . .  anaisö  tnä  kamna/svä hyatcä  (Sp.  574  o.)  kamnäna  aAmX  Y. 46.3;  —  parstim  zl  %wa  yohanä  tat )mavatqm{sA.)  Ay  {'■<Nt)[')%wä  x^ayqs{5i) alitm  dyat  imavantim  Y.43, 10.  b)  im jAw.:  atcit  bä  lumS  Aaomai  y'  ('weil') vupe  anye  tnatävAs  ailma  Aacinte  Yt  //.  5 ; Y,  /0. 1 3 ;  —  avat  vayul  ba  nqma  aAmi y  »va  dqma  vayemi  Yt  i^.  43;  43f-^;  — aojists . .  y  dim  upanAacat . .  Aqm.vanitts Yt/p.  38f.;  —  aom  ofarmB  AangSurva- yata  . .  ^raltaond .  .y  as . .  vftT^ravastTtnB Yt/5.36;  38;  —  bawraini  vasfrä  vajtAata ,,y  asti  bawris{sd.)  sraiita  Yt.5. 129;  — wn'^rayriB  ..  nBil ..  yanyB  (sd.)  vaAmyB .. y  nürjm  .  ,  dafvayäsS  voAunim  va  taca- yänti  . .  Yt  J^  54;  —  ^banhvB  va  patU vajaanaAe  .  .  y  alta%a  *Aanjastlnte  pouru gaonaAe  (sd.)  u%aheca  N.  65.  IV)  die Folge  oder  den  Zweck  angebend  'so  dass; auf  dass,  damit';  a)  im  gAw.;  1)  mit dem  Praeteritum;  Ayatis.!!!)  ji 3.dibaomä (sd.)  .  .  upa.jasat  Ay  ('so  dass')  vtrstmtä (sd.)    aciitim    manB   Y. 30.(1.  2)    mit
23826:~  Bed.  von  •banUayt    Laullich  stimmt  ai.  ,  •  j.  vohu.gaona-   l)  Adj.  'schwarzhaarig, tArtfäy-  f.  'Zacke'.  ^  -farbig*:    pasüm  .  .  aurusfm    va  'lam    vS
24490:•  j.  vispö.gaona-  Adj.  'von  allen  Farben (des  Haars)':  anumayanqm  harilS  (sd.) 'nanqm  V.  22.  4.
24491:Pü.!  hamäk  moi*'),  etl.:  hai  niak  w^J');  vgl. daiu  Vt.  8. 58  unter  hami^aona;  —  ')  'Haar' ^  'Farbe',  vgl.  'gaona:
```


## [2026-09-05T20:51:16.471Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^ *•  j\\.\\|gaoäa\\|gaoia\\|gaosa-\\+ \" BRT.txt | grep -in \"gaos\" | head -20"
}
```


### [2026-09-05T20:51:16.588Z] TOOL RESULT

```
886:7499:•  j.  'ä-sna-  Adj.  'angeboren,  natürlich', von  xratav-  m.  'Weisheit'  (im  Gegensatz zu  gmiSsräta-,  sd.):  «J»V  mailm..  s/g(s±) masyä  kacaiie  °nS  xrahts  yaüa  mi'inmni .  .  ha<aiu  'nasHt  xratus  "es  gibt  keinen Menschen,  dem  grössere  natürliche  Weis- heit zu  eigen  ist,  als  , ."  Yt.ro.107;  — "rum  xraiBm  tnasdaoättm  .  .  gaosS-srütim xratüm  tnazda'Mit^m  Y.  25.6;  —  'nahe xraiwö\.  22.2%;  —  Uta  kg  "fum  xratäm avaiaraiti  vSrjma  (sd.)  Yt/j.a,
1040:8308:•  j.  upa.mraoda- Adj. '(etwa)  der  Wollust, den  Huren  ergeben,  Hurenjäger':  äat  *ag!e ydi  fracarmti  .  .  gaosUj/ca  (sd.)  . ,  'dss'a
1296:9892:•  j.  gaoSävara-  m.,  Du.  'Ohrschtnuck, Ohrgehänge':  °ra  ca^ru.iarana  Yt. 5. 121, ij.  10.         [V.  74.15:  lies  matg'.]
1297:9895:•  j.  gaoSö.baraz-  f.  'Höhe  des  Ohrs': ä^ritlM  xsa'hrS.k^ntake  (sd.)  'zS  us.iäva- yuit{%±)  "^.46.
1313:10111:•  j.  ^gav-  Adj.  'rufend,  schreiend':  yeäie (näml.  mihrahe)  växs"  .  ,  yatat  fumaaha vä(im  baraiti  yat  gaosHt  (NS.)  ". .  sei  es dass  er  betend  seine  Stimme  erhebt  oder (laut)  rufend"  Yt/o.  85''.
1497:11156:•  j.  £a9-warasata-  Adj.  'der  vierzigste': °t3tn  gaosfm  fräyasämaide  N.  6$  (?).
1843:13052:•  j.  da^a-  Adj.  (fem.  °nä')  'recht,  dexter'; *Aaoys  'nö  F.jg;  —  kainayä  ,  .  «i/a  ka- ratta  hffyttmca  'ramca  'mmca  hSyümca  YL j.  131;  —  'Htm  hl  upa  ariiam'S.X.  10.  \QO', 99;  —  'tum  '*  upa  sraxtim  N.  -jg;  75;  — 'näl  *Aal  tiaemäl  (s±)  N.?»); — 'na  paiii ar3%at?ha  (sd.)  N.  65;  —  'tum  gaoS?m  V. Ä4+45,  5-»ö,i7,  y.32;  Ä46-70", 5.17—24",  /;.  33;  —  hävöya  dStvif  (sd.) •>iaca(lS.)  'na  bäsv&  ^kävayaea  V.j.2$;  — 'nam  (APm.)  aiigmtqm  V,<?.  71.  a)  ASn. 'tarn  als  Adv.  "rechts":  'tttm  hx  ^^^(sd.) vasaiU  .  .  Yt  10. 126.  A)  n.  und  f.  als Subst.  'die  rechte  Seite':  fravasays  .  .  yu oAuraAe  . .  'nqm  upa  yätöyeittti  Yt  13. 63; —  *'n?m  ä  gaonavatB(sd.)  N.65.  a)  sva. 'Westen"*:  ya'^a  vfitd..  ^zciiAot  (sd.)  'ttät fairi  fratmr^^it  'Von  Westen  her  .  ." V.^.4a.
1859:13299:•  j.,  g.  dätar-  :  dahr-  m.j  j.  däJhri-  f. i)  'der,  die  gibt,  schenkt',  mit  Akk.  der Sache  und  a)  Dat  der  Person:  lumasp  te gaosp?nta  .  ,  'ärö  baxlim  (sd.)  . .  asaone V.  2J.  1  '>;  —  ava.jasa  aridvJ . .  avaahe  . . aridrai  yazimnäi  jaloyanfäi  '>ri/  (NSf.) äyapfym  VL5. 132;  19;  —  JravaSayB  .  . _>'S  °^rf/  (NPt)  v;irjimm  siayaite..  "^ris tiAmSi  voku  x^annS  yS  .  .  Yt  JJ.  24; 24'.  ß)  Gen,  der  Person:  asi (VSf.)  vohOm  i^annö  assqm  narqm Yt.  i-j.  6  *>.  2)  'der  schaffend  hervorbringt, Schöpfer'  von  jiAM.  und  den  AmSp. a)  mit  Gen.  des  Objekts:  aÄura  matda  .  , °tar>gat&anqin  astvaiiiftqm{Stw^iz.)asaum Yt  1. 1  usw.;  —  ahur)m  mazdqm  . .  °tärim vokunqm  dämanqm  Y.  16. 1 ;  —  azim  yö almrö  masdä  azim  yd  'la  vaithvqm  V. 22.  i;  — p»-3sal  zardhusträ  a/iur?m  maz- dqm: *°tar»*vaiikvqm^''  aAura  mazda  V. ig.iT,  verwendet Vyt. i'O ;  —  atmsä  spuita ..  vokunqm  VdrJ  Y.  65. 12;  Vr.  ;7, 12; aiimanam  spmlanqm  .  .  ysi  funti  Snhqm dämanqm  yal  ahurake  mazdä  'tarasca inanxslarasäi  .  .  Yt  ig.  18;  —  azSm  täii "iwä  fraxsnlisA)  auäml  masda  .  .  vispa- nqm  'tänm  Y.  44. 7 ;  —  'tä  artÄJus  andat .  .  hati^y5var?stqm  (sd.)  Y.  ^o.  1 1'*;  —  'tä xratSu^  .  .  räzSng  .  .  sähli  (sd.)  Y.  S'^- 6'*.  ß)  absolut,  von  AhM.:  taha  dim ahurS  mazda  avqn  (sd.)   'ta  Yt  8.  7
1871:13341:•  j.  dÜtyö.draonah-  Adj.  'der  die  ge- hörige Nahrung,  Kost  hat';  ilai  "ailaya fracarmti  kirisas^a  gaositisca  ..°nar?has^a haiitS  ^.53.
2080:14496:•  j.  9-raDh-  n.  'Mund':  -arg  (NS.)'>  F. 23.  a)  Du.  'die  Mundwinkel' :  nazdyd  . . ya^a  *näaha  haca  *gaosalibya  yaha vä  gaosa  haca  ^'anhibya'^  "näher .. als  die Nase  von  den  Ohren  oder  als  die  Ohren von    den   Mundwinkeln   (entfernt    sind)"
2660:17383:•  j.,  g.  buray-  Adj.  "reichlich;  völlig,  voll- kommen': 'uiri  gaos  'uiri  ^an^a  °u:ri vastra  'uiri  anyaHbyS  mazäayasnaübyöyyi. 4^ ;  —  masdä  dadat  ahurS  . .  'ärsis  ä  . . :^'apa^yai  (sd.) . .  Y.  ?7. 2 1.  a)  Akk.  mit 'kar-  'etwas  (Akk.)  völlig  machen  sva. (Erhofftes)  erfüllen  mit-'  (Instr.)":  mat- damüä  'airiiä  ksrt^ä  räitl  isi  xrapaitJ (sd.)  ahmat  hyat  aibl  hyat  mtzditn  . .  V. 40.J.  '        '
3005:18941:•  j.,  p.  nah-  m.  'Nase',  Sing,  und  Du.: Waäamsaiy  uta  nüham  utä  gausa  fraja- nam  Bh.  2. 14;  13;  —  yim  yava  vatim närahabya  hubaoüitim^m  ßgaurva  H. 2.8;  26;  —  t^m  vahm  ninhaya  (LS.)'> *uzgnmiiiysil.2.8;  a6;  —  «Jw^a  (ND.)'' F.jd; — yaha  *nänhai''  Aaca  *gaoSaäbya ydha  vä  gaosa  Aaca  *^raaAiiya  (sd.)  P.  28.
3128:19687:•  j.  ^matgaoSävara- ■)  Adj.  (fem,  'ra-) 'mit  Ohrsdimuck,  Ohrgehängen  versehen': ^anha  vs  duy%a  va  . .  'var>'^  . .  upa,' valayaSa  (sd.)  V.  14. 1  g.
4284:26803:•  j.  spaeta-  Adj.  (fem.  'tä-)  'weiss'; spunam  .  .  't?m  sairi.gaostm  V,  8. 16",  17, 18; — ye^he  ca%würö  vastära  'ta  vispa., Yti.  13;  —  'ta  vastri  vaahaiti  Ha  (NSf.) "weisse  Kleider  hat  die  weisse  an"  Yt. 10. 136.
4377:27225:•  j.  sraota. gaoSa-  Adj.  (fem.  °/J-)  —  ?  — : daitxamca  m3zdayasnlm  .  ,  *sam  Vyt.  I4- Wertlos.
4418:27474:•  j.  srutgaoSa-  Adj,  'des  Ohren  hören, scharfhörig"':  mt^raiaf  .  .  °lS  hazanra.- yaoxsHS  YtJO.107;  19.35.
4484:27858:•  j.  zaranaena-,  zaranaena-'*  Adj.  (fem, "«r-)  'von  Gold,  golden';  auch  'mit  Gold besetzt,  verziert  (usw.)':  väiim  . .  'tarn  Yt 10. 124;  —  'nim^^  (näml.  tait>m)  aoi  Y. 10. 11;  —  'mm  faili.dsn3m  Yt5. 123;  — suwrqm  'njm  V.  2,  6;  —  suwrya  'nya  (ISf) V.  2.  10,  30,  38;  —  pusqm  .  .  'nim  Yt. 5.  iz8;  —  alva  caxrah^.)  'naY\..io.iz^) —  yezi  atakat  "«i'/""  "wenn  sie  (die Schale)  von  Gold  ist"  V.  7.  74;  —  alktm . .  'n>m  Yt  j.  136; —  hukairJm  barnS  .  . 'nfm  Yt.5.  96;  —  hukaityä^  haca  bari- zanhat  .  .  °«j}  Yt/5.  15;  —  'w  paiir gatvd  Yt/5.  i;  a*;  —  U  para.safanhs (sd.)  'na  (NPm.)  paiH.Muxla  (sd.)  äal  hl apara  >r)zataina  Yt  /O.  125;  —  gaosävara ..  •«/(ADm.)J'  Ytj.ra?.
4496:27909:•  j.  zaranyo.pis-,  **pi9--  Adj.  (auch  fem.) 'goldgeschmückt':  yS  paoiryS  °pTsS  srirä barssnava  ginwnaiti  "der  als  erster  die goldgeschmückten  .  .  Höhen  erklimmt" Yt.  JO.  1 3 ;  —  fr3  gaosavara  sisptmna  .  . minu{%A.)ca  -/m  (ADf.)'>  YtJj.io;  — ya^a  vil  *>r?tats.pai'hi  (sd.)  yaia  vä *-pafki  {K'Pa.)''^  ydha  v<t  *kilat  gaonaiiam Aog.  ly.
4502:27921:•  j.  zairi.gaosa-  Adj.  "mit  gelben,  gold- farbigen Ohren':  spanim  .  .  spaStim  'sim V.if.  16'  17,  18;  —  aspahe  ..  aurus'afie .  .  'sähe  Yt.Äi8.
4804:29731:•  j.  hazaDra.yaoxätay-,  hazaorä.y" Adj.  'der  tausend  Fertigkeiten  besitzt': mikrS  srutgaosS  'tU  Yt  10. 107,  /p.  35; —  mihnm  .  .  •tlm  Yt  jo.  35;  —  azfm dahäkfni . .'Um  Y.5.8;  —  '^•xltyö  bavaM yaha  aisis  dahäkäi  Az.3.
```


## [2026-09-05T20:51:24.118Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"gaosaka\\|gaoshaka\\|gaošaka\\|gauSaka\\|gausaka\" BRT.txt POK_*.txt HRN.txt HUB.txt PHD.txt NYB_vol2_glossary.txt 2>/dev/null | head -20; echo \"=== gaosa- Ohr entry:\"; grep -n \"j\\.,  g\\.  gaosa-\\|gaosa-  m\\.\\|gaoSa-  m\\.\" BRT.txt | head"
}
```


### [2026-09-05T20:51:24.184Z] TOOL RESULT

```
POK_02.txt:1585:Trotz  des  abweichenden  Anlautes  (vgl.  oben  S.  18  Anm.)  vielleicht hierher  lit.  gausüs,  gausmgas  , reichlich,  ergiebig,  fruchtbar',  gausmga  üpi , reichliche  Wassermengen  führender  Fluß',  gauseti  , reichlich  versehen  sein mit',  gausakalbis  ,wer  viel  zu  sprechen  vermag,  beredt'  (vgl.  norw.  dial.  * gausta  ,schnell  und  undeutlich  reden,  wie  wenn  man  sich  beeilt,  etwas  zu erzählen'),  lett.  gaüss  ,lange  dauernd'.
POK_full.txt:37339:the main river ', gausetT be provided with plentiful ', gausakalbis^ who is able to speak a 
=== gaosa- Ohr entry:
```


## [2026-09-05T20:51:24.977Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==1298||NR==1299' BRT.txt | head -60"
}
```


### [2026-09-05T20:51:26.759Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-05T20:51:29.927Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '9790,9900p' BRT.txt | cut -c1-300"
}
```


### [2026-09-05T20:51:29.982Z] TOOL RESULT

```
•  ).  gao-Äay-  m..  Du.''  'Milchbehälter, ■gefäss'  (wie  es  von  Priestern  bei  be- stimmten Opfern  gebraucht  wurde?):  yaJ- /am  tayanqm  disaurune  astra  °i6i  paitL- dam  W.14.Z.
Zum  V.  da-,  ai,  'dAay-  m.;  s.  %  305.  —  Vgl. j;aadana:  —  Pü.:  göll  därt.  —  ')  Woraus  lu scblies&en,  dass  dos  Gera.s&  aus  zwei  Teilen bestand  (eig.  Gefiss  und  Deckel?).
•  j.  gao-däyav-  Adj.  'das  Rind  hegend und  pflegend':  väsfr>m  hntun  gave  hiSia- »he  .  .  'yUtn  tianm  aiavaiDtn  Vr.  -'.  11.
Zum  V.  idi{jiy.  —  "^ ^.  gaodiyah;  i^aoHya:  — Pii. :  fehlL
•  g.  gao-däyah-  Adj.  'das  Rind  hegend und  pflegend,  dafür  sorgend':  °yS  (ASn.) ia'Ä«:ÄJ(sd.)  Y.  2p.2.
ai.  i,',yhäyai-  Adj.  —  Pü. ;  gJs/andän  daiisa, Sfi.:  gflsj-zläj/avasäj/T.
•  j.  *gao'iÄya-'>  Adj.  'das  Rind  hegend und  pflegend':  vaslreiiratahda  gave  hii- tiäohe  'hyeAeät ''  «ar/  asaonS  Vr.  /.  9.
BAinouiiiAi,  Altinn.  Wb.
■gaona-  48a
*dya-  Adj.,  zum  V.  'dä^y)- ;  vgL  goodäya»-.  — Pü. !  gÖsfandSti  dätrir.  —  D  So  K  7  B;  NA. •dy.  —  »)  Fälschlich  gäidy  N.  /oj.
•  j.  gao'pivanhav-  m.  EN.  eines  Gläu- bigen :  °»ÄJu/  asaonB  Yt,  13.111.
Eig.  'Rinder  fett  machend,  mästend';  "fhan- hau-  Adj.,  PPA.  (5209.4).  zum  den.  Praes.  3t 'fivah'ya-  [S  26S.  38,  30)  'siaiyiri'.
•  p.  gaub-  V.  'düir^.    Praes,  z  gauba-. Med.    i)  'sich  nennen,    erklären,   aus- geben für  — ',  mit  Nom.:  vakyazdätj'  Ayt^ bardiye^  a^nM^d/jBh.j.Ö;  9,  ^.  18,  r.18,19;
I  — /ravarti^ Aya"  mildaty  xsäyakiye^  agau- '  batä  Bh.2.iz.  a)  'sich  erklären  für —,
au  Gunsten  von  — ',  mit  Gen.  (statt  Dat): käram  hyJ^  däraya'vahaus  gaubalaiy  Bh. 3.  9;  —  hatnih^iyä  abava"  uiä  fravar- lais*agaubc^ta  Bh.2. 16".  a)m!tNeg, sva.  'den  Gehorsam  verweigern',  von Truppen;  käram  .  .  Ayi^  manä  naiy  gau- bataiy'&h.2.6,3.3,i4;2.T,\o;  
•  p.  *gau'bruva-'>  m,  EN.  eines  Persers, Genosse  Darios  I.  bei  der  Magophonie, Gobryas:  'v<^  pätil^uvarU däraya  vakaus xsäyä^iyahyä  arstibara''  "G.,  der  Patt' scAorier,  des  Königs  Z>.  Speerträger"  D. 8;  —  °J'o*  nämt^  mardutiiyaAyä  J>u^''a!' pärsa''  Bh.4. 1
O  zLes.  zuletzt  Fov  ZDMG.  54-  360.
•  j.  'gaona-  n.  i)  'Haai':  astica  -naca (AP.)  *d3r>whaca  Vt.  13.1-1;  —  ^avat  'nahe avaharäp  yä  *dvaiibya  »nzubya  *Aart- g>r)wnät"'9i\t  viel  vom  Haar  (näml./an/ö) soll  man  hinzubringen?  Was  man  mit zwei  Fingern  fassen  kann"  N.  (*5;  —  yat aadha  *hanjasaiit
KompE.;  Ableit.  —  afy.  yütia  'Haar;  Farbe', ■woss.')  y««  'Haar;  Farbe  (des  Haars)';  mp.^fli, np.  gün  'Farbe'.  —  Pü.  (lu  N.):  dannpt  oder danpt,  (zu  V.  2?,  Aog.):  fehlt,  (im  Komp.): i/iäi,  ^'-'«;  Sü.  (zu  Aog.):  varnaA.  —  1)  Gen. parL  als  Subj.  -  
•  j.  "gaona-  m,  'Gewinn"':  yö  .  .  sqm ai'wi.v>rKyHti ..upa  he  'nsm  baraiH..yd^a
dby  Google
483
gaonavant-
gaorayana-
484
nä  fijB  fryäi  vantaoe  . .  puHnm  vä  'n?m
vä  ava.^araiti   ".  .  der    schafft   ihr    (der
Erde)  Gewinn,  wie  ein  lieber  Mann  seinem
lieben  Weib   einen    Sohn   oder  (andern)
Gewinn  verschafft"  V.j.  25.
Zum  V.  'fflsv-i).  -  Pu.  (l.St.):  i«-  'satt',  (a.SL):
gött'1,  erl. ;  veA  ape  bavet  'sie  wird  besser'.  —
')  Anders  Gdn.  KZ.  30.  $23;  besser  35.402.
—  >)  Transäkr.  oder  in  Folge  Verwechilune
mit  igaona-,
•  j.  gaona'vant-   Adj.  'behaart,   haarig';
•  j.  'gaomant-  m.  EN.  eines  Gläubigen : 'matS  zavanS  (sd.)  .  .  a!aonö  Yt  13.  1 2  5.
Vgl.  ^gaomant:
•  j.  gaomavant-  Adj.  (fem.  °vain-)  'mil
Milch  versehen,  Milch  enthaltend':  saoüra .  ,  haomavaiti  'vaiti  hanana^atavaiti  Y. C8.\;  —  sad^ram  ..  'vaitm  Y.6Ü.  i; —  saoi:rä  .  .  'vaitls  (AP.)  Y.  22.  a ;  — 'vaitibyS  zaohrSbyS  Yt.5.8;  Ä15,  Vd.p; saohranqm  .  .  'vaitinqm  Vt.  5.  63,  V.
'o/  gaonahe  (sd.)  avabarät  .  .  *dann3m   U-A,;  *Vd.  4\  —  nmafum  ..  ä%ravat^ a  va  *vat5  *bar}snv3  vä  paiH  vayhanaAe  ^-S-^i  —  airyamm  :fannU .  ,  'vaiflm
.  auf  der   rechten   Seite   des   haarigen (Rückenhöckers)  oder  oben  auf  dem  Kopf"
N.  65.
l'Q.i  hac  dtüin  afiar  vailat  (gescht.  i'')0  hae fiixai')  i  silTiar  "rechls  auf  dem  EückgtBl  0 beim  drillen  Wirbel" a).  Vorher  steht:  apar\ buland  fa  sar  i  kSf  "oben  auf  der  Spitze  des , Höckers",  —  >>  Zu  vaslan  'drehen',  rgl.  lat. virUbra.  —  ")  Eig.  'Kno
Yt./Äi,
Steht  nur  V.  3  und  Yt.  l8  (5.  No.  1}  nicht neben  haomavani-.  Ich  halte  dafür,  dass  es in  den  Verbindungen  mit  h'  darauf  gereimt und  aus  gasmanU  hervorgegangen  ist;  Bthl. IF.  3.  3.  -  PÜ. :  gBitSmand.  (ru  V.  j):  gS^pcn- dömand,  (lu  Vd.):  ÜT/ämömand.  —  '
gaumäta-  m.  EN.  eines  Magiers,  des
•  j.  gaonö.tama-    Adj.   (fem. haarigste,  dichtest  behaarte':  bawri^  (sd.) . ,  'tima  Yt.5.  lag.
Superl.  aus  V*"""""  Adj-,  Ableit.  aus 'fuona-; B  wie  in  iatapeJäl;  %  364  D;  vgl.  tayS.lima-.
•  j.  gao-maeza-  m.  'Rindsharn',  als  rituelles Reinigungs-   und    als   Heilmittel'*:    'am
ayasöis  yaont  fiairi  uxsän.>fn  bix^'^rgm (sd.)  .  .  V.  7p,  21;  —  »sj«  pas^aSa  upa- t3har?Z3m{^A^  V.p.  14;  —  catura  frasnana frasnaySit  °z3m  gava  daiäya  bis  äp>m tnazdmätaya  "vier  Waschungen  nehme  er ' vor  mit  Rindsurin,  der  vom  Rind  produ- zirt,  zwei  mit
Zum  V.  maes:    —    ai.  meha-   m. ,    mp.   ),Pü.) gömiz,  ZDg.giimh  'Urin'.  —  O  S.  lu  moÄrma-*).
—  ")  Ungramm.  Stelle.
•  j.  gao'marf  Adj.  'Milch  enthaltend,  saft- reich': haomS  'ma  (NS.)  eairigaonS  V. 10.  12.
ai.  vgl.  gimln.  Adj.  —   Pü.i  carp  'Fett'  (statt !<,rpöma»ä7i,  Sü:  gmdyam.
•  j.  'gao'niant-  Adj.  (fem.  'maitl-)  i)  'mit
rfüssigen  Tieren  versehen,  be- byasca  haca  - maitibyasca  H. 'mit  Fleisch  vei  sehen,  Fleisch myatdim  .  .  'm^nfyrrt .  22  ■>;  —  4j  fiB  ..  paiti^anät vastravata  (sd.)  Yt  13. 50. i/-  EN.  i  femer  gaoman-  und  gae- aL  gimant'  Adj.  —  Pö.  (lu  l); d,   (lu  j):  göU
■1  'derl'''^'*°    falschen    Smerdis'^:     t     mariiyi^
-        '  magui  .  .  'iJ'  näma'  hauv    udapatatä  .  .
hauv    kärahyä    ava%ä    adurujiy<^    adam
bardiyc^    amiy    Bh.  /.  11;   12',  I4-J,  4,  2,
Bh.  b;    —    °tam   tyam   mt^um  Bh.i.  13^
[6,  4.ii
•  j-  gaoya-  Adj.  (fem.  yä-)  'bubulus'; i)  vom  Rind  kommend':  payat>hqm  .  . gävayanqmea'^  V. 5,  53.  2)  'aus  Rin- dern   bestehend':    gaoyqm    istlm   gaoyam
vahwqm  Yt.  (V.  17.
Ableit.  aus  igav-,  —  ai.  gäz-ya-,  gavyä-  Adj.  — PS.  (lu  V.):  fnSlaii  gäv  pim.  —  D  iSchr. ävaya  (vor  A)  statt  a^ya  s.  S  26e.    13  c.
•  j.  gao-yaotay-  f,  'Weideland,  Flur": ima  asiifa  Isdrasia  yaoitlffa  Y.  2.  16; —  xS  .  .  asBjiiihräsäi  'yagitisca  ätacinils (sd.)  Yt.<?.42; — aahqm  asanhqmca  sSiira- nqmca  yaoitinqmcaY.i.\6.  '  a)'Wcide': frayana  (sd,)  . .  pa'kanä  Jafrh  'tse  Ytio.
KompE.  —  ai,  vgl.  givyälay-  f.').  —  Kg. wohl  'Rinderheimstalte';  vgl- ^anwn-.  —  Pü.: gävyöl,  Sü.!  aranyam.  —  >)  WoiO  WN.  AiGr. l.    222.
•  j.  gaoray-  m,  EN.  eines  Gläubigen: 'rdii'  aiaonö  Yt  13.  118.
Bed.  ?  —  Vgl.  gaerayana-.
•  j.  gaorayana-  m.  EN.  eines  Gläubigen: 'nahe  asoonü  Yt  13. 1 1 8.
Oh  eig.  patr.  Adj.,  Ableit.  aus  gaoray-1  Mfj hat  gäuniay",     S.  auch  DL.  g.  13.  3.
Uiflitized  by  VjOOQ  IC
4S5
gaosura-
•  j.  gao-s&ra-  Adj.  'über  Rinder  gebietend, reich  an  Rindern':  nmän»n  bir^züstütum 'sütvm  Vyt.  p;  —  ailam  nmänä  ki'taätä ^'surar?kö^^  histtnte  Ytiy.S.
VgL  gaosutä:  —  Vgl,  DsT.  ZA.  2. 572.  Ohne Wert  Gdn.  3  Yt  79.  —  ■)  Die  mask.  statt der  neutr.  Form.  Im  Ausgang-^  und  -a  fielen die  Nom.  Flur,  beider  Geschlechter  zusammen. NA.  'sür',  s.  aber  die  Hds.
•  j.  gao-8urä-  f.  'Reichtum  an  Rindern' (?) : TtrthrtrjnS  avi  imal  nmänpm  •räbyBijiV. als  IP.)  :^ar»nö  pairi.vsnnavaiti  (sd.)  Yt.
Seht  unsicher  i  vgl.  ^aataf  n-.  —  Npü. :  un- deutlich.
•  j-^gac'^-Stäna-m.,  -stanay-  m.,  'Rin- derstall': yaua  ai^a  galwa  -naisva /ra- jasiit  V.  ;5.  29; — yö  altim  -tarn  uzdasta yerihh  v3  alsS  °nis  anhai  V.  /j.  30  ".
BJ.  goflhana-  Adj.,  gasthäna-  n.;  mp.  (Pü.j ^slän.  —  I)  So  Jpi,  Mfa;  NA.  hat  ^avö.ü'. —  ä)  zSt.  s.  HHr5.slSna.  No.   l.
•  j.  gaoz-,    p.  gaud-    V.     'verberget Praes.  4   gusa-,    24   gutaya-,    30  (Iter.) gauiiayot,
'verbergen,  verstecken':  haom  tanSm guzaita  Yt  4~  4.
D  mit  apa  'verbergen,  verheimlichen' yadiy  imäm  htfdugam  afiagaudayäAy  Bh. i^iiiio; — avakyarädiy  mä  apagaudaya'' (aS.)  Bh.^io.
mit  a  'ins  Versteck  bringen':  yat  .  . äal  azftn  tanSm  aguse  atairi ..  "..dabe- gab  ich  mich  ins  Versteck  unter  .."   Yt.
mit^a  'aus  dem  Versteck  hervorholen': äai  mam  fraguzayanta  . .  "da  holten  mich aus  dem  Versteck  . ."  Yt. /".  55.
ai.  guhaH  'er  verbirgt'.    —    Npil.  (lu  Yt.  4);
dar  miyStt  guiäilan  (wegen  des  Anklaugs !).
•  j.  gao-zasta-  Adj.  'Milch  in  der  Hand habend,  mit  M.  in  der  Hand':  yasß  %wä .  .  fräyazSite  .  .  'td  Y.  62.  i ;  V.J.  1.
PQ.  (in  Y.)i  göit  dasl,  (lu  V.):  yäml^)  dast, mit  der  Bemerkung:  lui  ke  elön  gäuiet  fatkSß fTir-ofl;   s.  daiu  DST.  ZA.  2.  33.
•  j-,  g.  gaoS-  V.  'hören'.  Praes.  i  gus-, 3  gäid-,  30  (Kaus.)  güsaya-,  —  PPfP. 'guäa-.
'hören,  hören  auf  — ;  vernehmen'.  Med.: mi  eis  ai  V}  dngvatö  mahrascS gUsfä{^S.) säinasiä  {sd.)   Y.j/.  18,'   —  gültä  y!  ..
—  gaoio.sruta-  486
\  aÄnmM/ (sA.) . .  Y.  31.  19;  — y5  paoiryS aAuräi  . .  manasca  *gusta  säsnäsca  Yt  13. 87");  55')^  F.^f'>,  21;  —  at  fravaxsya na  *gäsiJ.däm  "'  nä  iraotä  "ich  will  reden: nun  vernehmet,  nun  höret"  Y.  45.  i ;  — sraotü  asä  güsahvä  tä  akura  "hören 
ai.  ghifali  'es  hallt  wieder',    mp.  (Pü.):  iiigä-
iilan,  np.  myösldan,  nbaJ.^äAiy,  PDs.  «a-jH^r/;
E.  dazu  Hbm.  PSt   104.   —   *)  In  Anlehnung
an  Y.  31.  18.  —  «  S  i68.  57. j.  goäl:  E.  igav,  igav;    F.  _J  g:  lies  gaosö.
•  p.  gauia-,  j.  gaoSa-,  g.  *g«uä.a-''  m. 'Ohr':'''''j&F._^g^';  — (ÄuvffjM  {^z.kSyum) 'fym  V.  (V,  44—46',  Q.  i6f.*;  —  sraotä *'gius.äiii'>  vakistd  "höret  mit  den  Ohren das  Beste"  Y._^.  z;  — _yaSa  *riär?Aa  haca *'saeibya'i>  ydha  vä  °/a  (ND.)  Aaca'*"Si
■  >ff/iiiya  (sd.)  P.  2A';  —  yai  kl  dahat  .  . \'same  (DD.)  sraoma  Ytlö'.  7;  —  suru- \naoiti  '■saiwe  (ID.)^^  YL/0. 107;  —  /Sm granß  .  .  barahi  . ,  afa  'sayä  sraoma Yt70. 23;  —  apa  's'a  (AD.)  taoiayäü (sd.)  YtJO.  48;  — laäamsaiy  Uta  näham Uta  
KompA.,  E.  —  Zum  V.  gaos-.  —  ai.  ghiia-  m. 'Lärm',  np.^Ji<0[ir'.  — Pii.i  ^äj,  (zuY.jaa): nigSsünTA,  (lU  Y.  J7.  3!:  an  d  an  i  imäi  . . •ligSsitär  5  iam  TOiaiin.  —  ')  Maroltenhalte Zetlegong,  S  ^63.  57;  s.  No.  3,  6.  —  »>  Hds. gaos.  —  3)  NA.
-  7)  Pü. :  fehlt.
•  j.  gaoSävara-  m.,  Du.  'Ohrschtnuck, Ohrgehänge':  °ra  ca^ru.iarana  Yt. 5. 121, ij.  10.         [V.  74.15:  lies  matg'.]
KompE.  —  Komp.:  gaosa-+*d-iiara-  (zum  V. 'Äd-,  S  2**37)  m-  'wasiraOhtEetragen  wird'.
—  Vgl.  np.  gösvär  (aus  *gaiiia-iara-)  'Ohr- gehänge', ai.  ööAafana-  n.  'Schmuck'.
•  j.  gaoSö.baraz-  f.  'Höhe  des  Ohrs': ä^ritlM  xsa'hrS.k^ntake  (sd.)  'zS  us.iäva- yuit{%±)  "^.46.
Pü. :  göS  bäläk.
•  j.  gaoäÖ.srüta-  Adj.  'vom  Ohr  gehört', von  xralav-  m.  'Weisheit'  sva.  'erlernt' (im  Gegensatz  zu  'asna-,  sd.)":  äsnim xratüm  mazdaaätpm . ,  °t>m  xratütn  masda-
16«
dby  Google
487  gata-
```


## [2026-09-05T20:51:45.511Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 49 50 51; do echo \"===== NR=$n\"; awk -v N=$n 'BEGIN{RS=\"\\f\"} NR==N' POK_02.txt | head -5; done"
}
```


### [2026-09-05T20:51:47.374Z] TOOL RESULT

```
===== NR=49
hen',  ursprüngl.  , kriechen/ indem  man  sich  festhakt'),  wozu  anord.  krabbi  m.,  ags.  crabba,  mnd.  krabbe .  ,Krabbe'  und  ahd.  (krebiz),  *krabita-,  krebaz(o),  asächs.  krebit,  nhd.  Krebs.  — ^ Ganz  fraglich  gr.  ygö^q)ig  ,Sau'  (besser  ,die  Grunzende'?)  als  Nasalform.
3.  Daneben  ^gribh-  (mit  expressivem  i?): Gr.  yqicpaad'ai '   ygacpsLv.  Aa%(ßveg.   oX    ös   ^vecv   'Aal   äiivaaeiv  Hes.  (vgl,
von  sker- :  gr.  oy.aQLq)aof.iai,  lat.  scribo),  äyQicpri,  dygelcfva  ,Harke,  Rechen* {ä-  aus  *7}-  ,iv',  ,einritzen'?);
holl.  kribbelen  ,murren',  kribelen  ,jucken',  mhd.  md.  kribeln  , kitzeln  (von; der  Sinnenlustj',  nhd.  kribbeln^  und  mit  germ.  pp:  ahd.  kinpfan  , rasch  und, wiederholt  wonach  greifen',  nhd.  kripfen  ,bes.  vom  Wegkratzen  einer  Riefe' fj
lett.  gripsta  , Schramme'.
===== NR=50
Dentalerweiterungen:
gnd-,  geud'  (vereinzelt  g-u-ed-?),  vor  allem  im  Germ.;  gudo-m  ,Darm'.
Ai.  guddm  ,Darm';
maked.  yöda '  evrega  MaxEÖöveg  Hes. ;
ndd.  kilt  ,Darm',  nhd.  bair.  kütz  ,ein  Teil  der  Gedärme';  ndd.  küt,küte
===== NR=51
 ceod{a)  m.  ,Sack,  Tasche',  ahd.  kiot  ds.,  mnd.  küdel  , Tasche', mhd.  kiutel , Wamme,  Unterkinn',  nhd.  Keutel , Fischnetz,  Darm,  Geschwulst';
gut-  in  mnd.  koder  m.,  nhd.  dial.  Köderl,  Goderl  (^gut-ro-)  ,Unterkinn, Kropf,  ndd.  koden  ds.,  engl,  cud  ,das  Innere  des  Schlundes  bei  Wieder-, käuern',  ndl.  kossem  ,Unterkinn'  (*gutsvio-),  norw.  kusma  ,parotitis' ;  mhd. kuteln,  nhd.  Kutteln  ,Kaldaunen' ;
mit  expressivem  dd:  ags.  codd  m. , Hülse,  Schote,  Sack',  aisl.  koddi  , Kissen, Hode' ;  vielleicht  ahd.  kutti  , Herde',  nhd.  Kette,  bair.  kütt  , Schar  jagd- barer Tiere';
hitt.  ku-u-tar  (kuttar),  Dat.  ku-ut-ta-ni  {kuttani)  n.  ,Nacken,  Oberarm' (=  lat.  guttur,  s.  oben) ;  kuttanalli  , Halskette'.
6.  Gutturalerweiterungen;  gugä  , Kugel'.
```


## [2026-09-05T20:51:54.126Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"gund\\|guṇ\\|guna-\" POK_02.txt | head -20; echo \"=== full:\"; grep -n \"gund\" POK_full.txt | head -20"
}
```


### [2026-09-05T20:51:54.191Z] TOOL RESULT

```
578:A.  Ai.  gund-h  (*gT-nö-s)  ,der  einzelne  Faden  einer  Schnur,  Schnur,  Strick; mal'  (dvi-,  tri-guna-  eigentlich  ,aus  zwei;,  drei  Fäden  bestehend') ;  gdrta-h Wagensitz  des  Streitwagens'  (,*aus  Ruten  geflochtener  Sitz,  Wagenkorb'), vgl.  mit  Formans  -mo-  anord.  karmr  , Brustwehr',  schwed.  karm  ,Rücken- lehne  aus  Flechtwerk,  Wagenkorb'  (*gor-mo-s  , Flechtwerk').
698:nasaliert  anord.  kunta  ,vulva'  aus  mnd.  kunte  ,cunnus;  auch  Hintere^ norw.  schwed.  kunt  ,Ranzen  (von  Birkenrinde)';  auch  av.  gunda-,  gund^ ,Teigballen'?
1412:Gr.  -/.av^vlrj  ,Geschwür,  Geschwulst',  y.ovd^rjlal'  al  dvoidijGsig  Hes.; got.   gund   n.    ,krebsartiges    Geschwür',   norw.    dial.    gund    m.    ,Schorf', ags.  gund  m.  , Eiter',  ahd.  gund  m.  , Eiter,  eiterndes  Geschwür'. WP.  I  588.
2268:Gen.  jaghn-us-ah,  Pass.  hanyäte,  Partiz.  hatd-  ^geschlagen,  getötet'  (==  ay.*^ jata-j  gr.  -cpatog),  hdntva-h  ;Zu  schlagen,  zu  töten'  ( :  av.  jq^iva-^  aksl  .^ 0gtva)j  vrtra-hdn-,  Gen.  -ghTi-dh  (=  av.  vdrd^ra-jan-,  Gen.  -y-no)  ,<ien  Wider-  S stand  niederschlagend',  ghand-  ^erschlagend,  m.  Knüttel,  Keule'  (==  g^^  „- ävÖQO-q)6vogj  lett.  gans),  sam-hd-t  ,Schicht',  hati-h  ,das  Schlagen,  Schlag^ ^ Multiplikation'  (:  gr.  ÖLcpaai-og,  av.  -jaüi-,  anord.  gudr,  gunnr),  hatyä  (spät) ,Tötung'  (:  ahd.  gundea,  lit.  dial.  ginciä),  hantdr-  ,wer  einen  schlägt  od( tötet'  (=aksl.  z§teljb)',  von  der  schweren  Basis  ai.  hanitum  (spät!)  und^fÄö^ ,tötend',  m.  ,Schlag,  Tötung,  Vernichtung',  ghätayati  ,tötet';
2275:anord.  gudr,  gunnr  f.  (=  ai.  hati-),  as.  güdea,  ags.  güp  (*gunpjö  =  ai. hatyä  bis  auf  den  Akzent)  , Kampf,  Schlacht',  ahd.  gund-fano  ,Kriegs- fahne';  anord.  gandr  , Stock',  Schweiz,  gunten  ,eine  Art  Keil';  norw.  dial. gana  ,die  Äste  an  Bäumen  abhauen'  wie  lit.  geneti]
2520:iuuent-,  iuunt-:  ai.  yüvant-j  i.  yuvati-lj,  ,jung;  Jungfrau';  shdi.  jugundj as.  jugud,  ags.  geogud  (g  statt  w  nach  *duzunpi-  ^Tugendj  Tüchtigkeit'), got.  junda  ^Jugend'  (*iuunta) ;  lat.  Juventus,  -tütis  , Jugend'  (jüventa  =  got. junda?)  =  air.  öetiu,  öitiu,  Gen.  -ted  ^Jugend'  {^iountüt-Sj  umgebildet  aus iuui}tüt-j  s.  oben  zu  öac).
3428:burgund.  hendinos  ,König' ;  strittig  got.  hindumists  »äußerster,  hinterster', ahd.  hintana,  hintar  ,hinter',  ags.  hindema  ,der  letzte'  (,novissimus');
5498:trot.  liudan,  ahd.  liotan,  as.  liodan,  ags.  leodan  , wachsen',  ahd.  sumarlota ^Sommerschößling',  anord.  lodenn  , bewachsen,  haarig,  rauh',  loda  ,(*fest- o-eTvachsen  sein  =)  festhangen,  festkleben';  got.  laudi  i.  , Gestalt',  swa-, sama-laups  ,so  groß',  jugga-lanps  ,Jüngling',  mhd.  löt  , beschaffen';  got. ludja  ^Antlitz'  (vgl.  np.  röi),  as.  lud  .Äußeres,  Körperkraft  (?  nur  Hei. 154),  ahd.  ant-lutti  , Antlitz' -^  (Nachwuchs  =  Menge,  Volk  :)  ahd.  Hut,  ags. Uod  ,Volk',  mhd.  Hute  , Leute',  ags.  leode  ds.,  dann  auch  von  einzelnen Menschen  ahd.  Hut  , Mensch',  nhd.  dial.  das  Leut  ,Person',  nd.  lud,  lüt , Weibsperson,  Mädchen',  burgund.   leudis  ,der  Gemeinfreie';
=== full:
5713:resentment, disfavor'; Middle High German gundm. ' favour'. Old Norse gf-undi. " 
5721:(see Brugmann Grdr. I|2 2, 437), while Middle High German gund. Old Norse gfund\he 
5728:Old Saxon gi-onsta, then also Middle High German gund. Old Norse gfund (suffix-t/-) new 
7311:Estonian N aeg : Turkish N gun, gundiJz, donem, zaman : Basque egun^ day ' 
12292:brhatT{= Irish Brigit, Germanic Burgund), Avestan bsrszant- {npers. buland), f. berezaitJ 
12336:Germanic *burgundT{= Old Indie brhatT, Celtic *brigantT, Irish Brigit) in Burgund, oldest 
12338:Norwegian islands. Old High German Purgunt women's name, in addition Burgundiones, 
24537:{Ant-aib, Burgund-aib), Old High German -eiba {Weter-eiba, Wingart-eiba); 
26601:Gothic niunda. Old High German niunto. Old Norse nionde. Old Saxon nigundo, nigudo. 
26602:Old Frisian niugunda. Old English ni^oda, Lithuanian devintas. Old Prussian newTnts, Old 
31819:also buttocks ', Norwegian Swedish kunt' Ranzen (from birch bark)'; also Avestan gunda-, 
31820:gunda " Teigballer\ '? 
32871:Gothic gundu. " cancerous ulcer ', Norwegian dial, gundm. "scurf'. Old English gundxu. 
32872:"pus'. Old High German gundm. "pus, pustulating ulcer'. 
40053:gundea, Lithuanian dial, gincia), hantar-^ one who hits or kills ' (= Old Church Slavic 
40087:gund-fano' war flag '; Old Norse gandr^st\ck', Swiss gunten^a kind of wedge'; Norwegian 
41814:juuent-,juuQt-:0\d \nd\c yuvant-, f. yuvatf-h' young; virgin'; Old High German Jugund, 
45710:burgund. hend/nos' king'; controversial Gothic hindumists^ extreme, hindermost ', Old 
55728:"person'. Low German lud, /J/"woman, girl', burgund. leudis' the commonly free, layman '; 
85084:Mayrhofer 468, 491, Durante, Ricerche lingunder 1, 234 ff., Pedersen Hittitisch 141 Anm.
```


## [2026-09-05T20:51:55.306Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"kaufa\\|keu-p\\|keup-\\|kumb\\|Kuppe\" POK_03.txt | head -30"
}
```


### [2026-09-05T20:51:55.353Z] TOOL RESULT

```
2602:(s)keup-,  skeub(h)-  , Büschel,  Schopf,  Quaste';  nur  gerin.  und  slav.
```


## [2026-09-05T20:52:07.876Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"keu-b\\|keub-\\|keup-\\|keu-p\\|kumb\\|Kuppe\\|kaufa\" POK_02.txt | head -30"
}
```


### [2026-09-05T20:52:07.945Z] TOOL RESULT

```
729:hingegen  stammen  wohl  aus  lat.  cuppa  f.  ,Becher' :  ags.  copp  m.  , Gipfel^ Becher'  (mengl.  auch  ,Kopf'),  cupp  m.,  cuppe  f.  ,Becher',  nhd.  (eigentlich  '^^ md.)  Koppe  ,Kamm  (Haube)  der  Vögel',  Koppe,  Kuppe  ,runder  Berggipfel*^ mhd.  kuppe,  ahd.  chuppa  ,Kopfbedeckung'  (mit  expressiver  Verschärfung ahd.  chuppha  ds.,  mhd.  kupfe,  kuffe,  gupfe  ds.,  gupf,  gupfe  m.  ,Gipfel eines  Berges,  Spitze  des  Turmes',  worin  g-  wohl  Substitution  für  roman» ;,; C-;  anord.  koppr  ,Kopf,  Gefäß,  Helmknopf,  Augenhöhle'  ist  Lw.  aus  mnd. kopp)]  afries.  mnd.  kopp  ,Becher',  ahd.  köpf,  chuph  , Becher',  mhd.  köpf ,Trinkgefäß,  Hirnschale,  Kopf  (ähnlich  rom.  testa  ,Kopf  aus  lat.  testa , Scherbe,  Schale',  mlat.  testa  capitis),  nhd.  Kopf
730:Nasaliertes  germ.  '^kumb-:  ags.  cumb  (engl,  coomb)  ,Napf'  (in  der  Bed. ,Tal'  aus  abrit.  *kumbo-s  ,Tal'),  mnd.  kumm(e)  f.  , rundes,  tiefes  Gefäß, Kufe,  Napf,  nhd.  Kumme  , tiefe  Schale',  Schweiz,  chumme  , Zisterne'; ^kump-  (aus  *kumb-  mit  Kons. -Schärfung)  mnd.  kump,  mhd.  Äjwwip/ , Gefäß, Tasse',  nhd.  Kumpf
731:Dazu  vielleicht  npers.  gumbed  ,Wölbung,  Kuppel,  Becher';
3332:aisl.  hnakki,  hnakkr  m.  ,Nacken'  (norw.  nakk  auch  ,Berggipfel,  Kuppe')^ ahd.  Jinac,  -ckes  , Nacken,  Gipfel',  bair.  nacken  , Knochen',  ablautend  ags» hnecca  ,Nacken,  Hinterkopf,  mnd.  necke  ds.,  mhd.  genicke  ,Genick';  mit der  Bed.  ,knicken'  hierher  isl.  hnakki  ,Anker',  norw.  nakke  ,kleiner  eiserner Haken',  nekia  ,krümmen,  biegen',  mengl.  nö/c,  engl,  nook  ,Winkel,  Ecke* (aisl.   hnekkja  ,zurücktreiben,   hemmen',   eigentlich   ,zusammendrücken'?).
3854:2.  keu-,  keup-,  of   mit   labialen   oder   gutturalen    Erweiterungen:   ,biegen'
3858:kumb{ti)o-s  ,Gefäß',  kupro-s  , Buckel',  küpä  ,Höhlung,  Hohlgefäß',
3868:A.  Dentalerweiterung  (redupl.)  ka-ku-d-  ;  ai.  kakud-  ,Kuppe,  Gipfel', käküd-  ,Mundhöhle,  Gaumen',  kaküdmant-  ,mit  einem  Gipfel  oder  Hocker .    versehen';  lat.  cacümen  ,Spitze,  Gipfel'  (die  wew -Weiterbildung  wohl  nach acümen),  Grundbed.  ,Wölbung';    auf  ein  germ.  *hagu  =  ai.  kaküd-  führt    1
3881:C.  Labialerweiterungen. C.  L  keu-b-:
3895:C.  II.  keu-bh-   (einschließlich   von  Worten,    die    bh   oder   b   enthalten können).
3897:redupl.  ai.  hakübh-  f.  , Kuppe,  Gipfel',  hakubhd-  ,hervor-,  emporragend' (erst  nach  haküd-  umgebildet?);
3905:C.  III.  keu-p-:
3912:Apers.  kaufa-  ,Berg',  av.  Jcaofa-  ,ds. ;  Kamelbuckel',  npers.  köh  ,Berg' (setzen  -ph-  voraus);
3915:ahd.  hovar  ,Buckel'  (:  lit.  kuprä),  ags.  hofer  m.  ds.,  ahd.  hubil  ,Hügel', as.  huvil  ds.  (davon  nhd.  hobeln  als  ,die  Unebenheiten  entfernen');  vielleicht ahd.  hüfila,  hiufila  , Wange',  nhd.  Schweiz,  hüfelin  ,unter  den  Augen  liegen- der Teil  der  Wange';  norw.  hov  n.  , Anhöhe,  kleiner  Hügel',  aisl.  hof  n. , Tempel',  ags.  hof  n.  , Gehege,  Haus,  Tempel',  as.  hof,  ahd.  hof  m.  , um- schlossener Raum  beim  Haus,  Hof,  Gut'  (ursprüngl.  von  der  Lage  auf Anhöhen);  mhd.  huste  ,auf  dem  Felde  zusammengestellter  Getreidehaufen, Hauste'  {-Ait.  küpstas)  ]  *hüfsto  ist  ablautgleich  mit  ahd.  hüfo  und  scheint wie  dieses  wohl  eher  zu  keu-b-  zu  gehören  (s.  dort);  wird  auch  mit  russ. kust^  , Busch,  Strauch,  Staude',  klr.  kust  , Strauch,  Staude'  verbunden;
3925:mir.  comm  , Gefäß',  cummal  , Becher,  Schale',  cymr.  cwmm  ,Tal'  (m.), bret.  komm  ,Trog'  (m.);  aus  urbrit.  *kumbos  stammen  ags.  cumb  ,Tal', engl,  coomb,  combe  , Talmulde',  hingegen  ist  gall.-rom.  cumba  ,Tal,  Trog' Fem.;  aus  dem  Frz.  stammt  bret.  komb  ,Tal';  vgl.  die  unnas.  Gefäßbe- zeichnungen pam.  kubun,  poln.  kubek,  auch  gr.  y,vßog  jTQvßXtov']
3967:keu-bh- :  ai.  sümbhati  , leuchtet',  äöhhate  ,ist  stattlich,  nimmt  sich  schön aus',  söbhand-  ,schön,  glänzend',  Subha-  , hübsch,  angenehm,  erfreulichV iubhrd-  , schön,  glänzend,  hellfarbig'  =  arm.  surb  ,rein,  heilig',  srbem , reinige,  heilige'.
5686:(aisl.  makr  ^passend,  bequem^  ist  ndd.  Lw.);  afries.  mek  n.  ^Verheiratung^;, jjiekere   ^Ehenunterhändler^^    mhd.   mechele    , Kuppelei^ ;    aus    germ.    *makö stammt  lat.  mac{h)iö  ,Maurer';   daraus  rom.  *matsiö,   woher  wieder  ahd. stein-mezzo  ,Steinmetz^ WP.  n  226 f.,  WH.  II  3,  Trautmann  173;  vgl.  2.  mak-  und  menk-.
```


## [2026-09-05T20:52:09.218Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('POK_02.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\n# find leaf containing 'Teigballen'\nfor i,p in enumerate(pages):\n    if 'Teigballen' in p or 'gunda' in p:\n        print('leaf idx(0-based)',i, 'NR',i+1)\n        print(p[:300].replace('\\n',' | '))\n        print('---')\nEOF"
}
```


### [2026-09-05T20:52:10.781Z] TOOL RESULT

```
leaf idx(0-based) 49 NR 50
Dentalerweiterungen: | gnd-,  geud'  (vereinzelt  g-u-ed-?),  vor  allem  im  Germ.;  gudo-m  ,Darm'. | Ai.  guddm  ,Darm'; | maked.  yöda '  evrega  MaxEÖöveg  Hes. ; | ndd.  kilt  ,Darm',  nhd.  bair.  kütz  ,ein  Teil  der  Gedärme';  ndd.  küt,küte | auch  ,Eingeweide  kleinerer  Tiere,  Rogenbeutel;  Wad
---
```


## [2026-09-05T20:52:23.873Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('POK_02.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\n# map line number -> leaf\nleaf=0; m={}\nfor i,l in enumerate(lines,1):\n    m[i]=leaf\n    leaf+=l.count('\\f')\nfor ln in [698,729,730,731,3854,3858,3868,3881,3895,3905,3912,3925,578]:\n    print(ln, 'leaf', m[ln], 'page', m[ln]+344)\nEOF"
}
```


### [2026-09-05T20:52:25.806Z] TOOL RESULT

```
698 leaf 49 page 393
729 leaf 52 page 396
730 leaf 52 page 396
731 leaf 52 page 396
3854 leaf 247 page 591
3858 leaf 247 page 591
3868 leaf 247 page 591
3881 leaf 248 page 592
3895 leaf 249 page 593
3905 leaf 249 page 593
3912 leaf 250 page 594
3925 leaf 251 page 595
578 leaf 40 page 384
```


## [2026-09-05T20:52:35.549Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('POK_02.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in (243,244,245,246,247,248,249,250):\n    print('=== leaf',i,'-> p?',i+344)\n    print(pages[i][:400].replace('\\n',' | '))\nEOF"
}
```


### [2026-09-05T20:52:37.334Z] TOOL RESULT

```
=== leaf 243 -> p? 587
r-. | Air.  hrndtti  ,dreht  den  Faden,  spinnt',  Icarttar-  ,der  Spinner',  crtdH ,bindet,  heftet  zusammen',  Jcata-  m.  , Geflecht,  Matte'  (mind.  für  Vcrta-), wohl  auch  huti-,  kutl  f.  ,Hütte'  (""Jcrti),  Jcudya-  n.  {Hftya-)  ,(*geflochtene) Wand',  päli  Jcoccha-  ,Flechtwerk'  (ai.  Hrtsa-)-^  ai.  Jcrtsnd-  , vollständig, ganz'  (vgl.  lat.  crassus,  slav.  *(i'brstv^)] | gr.  y
=== leaf 244 -> p? 588
a  ,Knoten  im  Gespinst^, ßech.  Jcrutina  ,ds. ;  Windung:  Wiege^,  poln.  sTir^tka  ,WeidenseiF; | nach  Pedersen  Toch.  Sprachg.  hierher  toch.  B  Jcercclye  ,Palast^ | WP.  I  421  f.,  WH.  I  285  f.,   Trautmann  142,  146. | ^eS'  ,kratzen,  kämmen^;  ksu-ro-  ,Schermesser^ | Gr.  'ASOTisov  (zur  Form  asg-äLov  s.  ßoisacq)  ,Werg^  {*'kes-'kes-)] | mir.  clr  f.  ,Kamm^  (*te-rä); | anord.  ha
=== leaf 245 -> p? 589
vgöv  (:  ai.  ksurd-)  ,Schermesser',  ^vgöv  toiiöv,  loy(y6v^  d^v Hes. ;  ^oavov  (*ks-ou-,nom)  ,alles  Geschnitzte',  bes.  ,Götterbild';  ^ | gr.  ^(barga'  xpr]yirgig,  iprjTcrgta  Hes.  (,Striegel'),  eher  mit  ]csö[u]-  hierher, als  mit  *Jcsös-  zur  Wurzelf.  Jcs-es-; | hierher  wohl  mit  Metathese  halt.  *skuuö  ,rasiere'  in  lett.  sJcuvu,  sJcüt, lit.  sJcutü,  sküsti  ds.  ij | WP. 
=== leaf 246 -> p? 590
os  ,Ruhm^ | 1.  Ai.  kavi-  ,klug,  weise;  Seher,  Dichter^,  Jcaväri-  ^eigennützig,  karg', d-kava-  ,nicht  geizig';  ä-küvatB  ,beabsichtigt',  a-hüta-  n.,  ä-hüti-  f.  , Absicht'; | av.  (Sdvlst  1.  Sg.  Med.  Aor.  ,ich  erhoffte,  versah  mich'; | gr.  Y.oe(ü  , merke,  höre'  (Denomin.  von  *houos]  =  lat.  caveö);  "^-Kofag  steckt in  ion.-att.  äva^wg  e'xsLv  ,Sorge  tragen' ;  dor.  
=== leaf 247 -> p? 591
-)^ wovon  skygna  ,spähen';  got.  skauns  ,schön^  (ihna-skauns  ,von  gleicher  Ge- stalt'), ahd.  scöni  ds.,  aisl.  skjöni,  as.  sköni  ,glänzend,  schön',  ags.  sclene ds.  (eigentlich  ,conspicuous') ;  tiefstufiges  *sku-ni-  in  aisl."  6%n  f.  n.  ,Ord- nung,  Bescheid,  Einsicht',  skynja  ,untersuchen,  verstehen';  aisl.  skoda ,spähen'; | apr.  aw-sc/ia«c?i^i(;ei., vertrauen'. | WP. 
=== leaf 248 -> p? 592
  Garben  (12 — 16)^;  über  Schoch s.  zuletzt  Sommer  ,Zum  Zahlwort^,  S.  78ff.,  S.-ß.  Bayr.  Akad.  1950,  Heft  7; | lit.  hduge,  ablaut.  Jciügis  ,Heuhaufe^,  apr.  Jcugis  ,Knauf  am  Schwertgriff^, lit.  Jcaugurl  ,kleiner  steiler  HügeF,  lett.  käudze  ,Haufen,  Schober^  (und slcaudze). | B.  IL  keu-k'i | Ai.  Jcucdtiy  huncate  ,zieht  sich  zusammen,  krümmt  sicli'^,  Jcicücikä  ,S
=== leaf 249 -> p? 593
hd.  dial.  hoppen  ^hüpfen',  engl,  hobble  , hinken*  (Wissmann  Nom.  postverb. 174f.). | b.  Mit  nicht  aufs  Biegen  des  Körpers  gewendeten  Bedeutungen : | ai.  Jcubra-  n.    ^Höhlung   in    der   Erde,    Grube ;    Ohrring^ ;    gr.  xvßog  .  .  . ndq)ioL  d^  TÖ  tQvßXlov  Hes. ; | [aber  ags.  höpig  ,in  hills  and  hollows',  höp  m.  ,Reifen',  engl,  hoop,  ndl. hoep  jRing,  Reifen
=== leaf 250 -> p? 594
b-)  wohl  auch  ags.  gehopp  ,folliculus',  hoppe  f. ,bulla,  Kapsel',  mengl.  hoppe  , Samenkapsel  des  Flachses'; | allenfalls  slav.  *k^p^,  öech.  Jeep  ,vulva',  poln.  kiep  ,ds.;  Narr,  Tauge- nichts' (Berneker  664  f.  zw.). | b.  Bedeutungsgruppe  ,Wölbung  nach  oben,  Haufe  u.  dgl.': | Apers.  kaufa-  ,Berg',  av.  Jcaofa-  ,ds. ;  Kamelbuckel',  npers.  köh  ,Berg' (setzen  -ph-  v
```


## [2026-09-05T20:52:47.160Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('POK_02.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in range(42,56):\n    head=pages[i][:200].replace('\\n',' | ')\n    print(i,'|',head)\nEOF"
}
```


### [2026-09-05T20:52:48.826Z] TOOL RESULT

```
42 | ztas  , Bohrer',  apr.  granstis  ds.  (lit.  gruzulat , Deichsel'  vermutlich  ebenfalls  aus  ,Strang'). | 2.  Dentalerweiterungen: | a.  gr-etih)-:  ags.  cradol  m.  ,Wiege'  {*kradula-  ,geflochtenes
43 |  gorb  , Buckel,  Höcker,  Auswuchs,  Erhöhung,  Rücken',  sloven.  grb^ grba  , Höcker,  Buckel,  Runzel',  grbati , buckelig  machen,  krümmen,  runzeln^; | nisl.  korpa  f.  .Runzel,  Falte',  korpna
44 | ',  nor^ mdartl.  krasen  ,schwach,  hinfällig';  vermutlich  as.  ahd.  kresso  , Gründling*! nhd.  Kresse,  KressUng  ds. ;  *ger-s-  wohl  in  norw.  karra  ,einschrumpfeii, sich  kräuseln'. | Danebe
45 | (über  ahd.  krüsel  , Schmelztiegel'  usw.  s.  Falk-Torp  unter  krus  m.  Nachtrag) zur  Erwägung  steht.  Über   nhd.  Kriechbaum  s.  Kluge  ^^  unter  Krieche. | 2.  Labialerweiterungen: | greu-p-: 
46 | rayeitl und  oben  S.  280 ;  anders  Schwyzer  Gr.  Gr.  1  648  ^)j  Aor.  eygsTo,  syQea^ai^ Perf.  i-ygrj-yoQa  (für  s-yrj-yoga  —  vgl.  ai.  jä-gdra  —  mit  dem  g  von " iygiad-ai]  Med.  (sp
47 | fe',  yvjgaXiog  (bei  Hes.  auch  yegaleog) ,alt';  att.  ygavg,  Gen.  yga{*f)6g  (hom.  Dat.  ygrj'C)  ,alte  Frau'  (hom.  ygr/vg wohl  spätere  Umschrift  eines  richtigen  *}grj{ß)Lg  nach  dem 
48 | hen',  ursprüngl.  , kriechen/ indem  man  sich  festhakt'),  wozu  anord.  krabbi  m.,  ags.  crabba,  mnd.  krabbe .  ,Krabbe'  und  ahd.  (krebiz),  *krabita-,  krebaz(o),  asächs.  krebit,  nhd.  
49 | Dentalerweiterungen: | gnd-,  geud'  (vereinzelt  g-u-ed-?),  vor  allem  im  Germ.;  gudo-m  ,Darm'. | Ai.  guddm  ,Darm'; | maked.  yöda '  evrega  MaxEÖöveg  Hes. ; | ndd.  kilt  ,Darm',  nhd.  bair.  kütz
50 |  ceod{a)  m.  ,Sack,  Tasche',  ahd.  kiot  ds.,  mnd.  küdel  , Tasche', mhd.  kiutel , Wamme,  Unterkinn',  nhd.  Keutel , Fischnetz,  Darm,  Geschwulst'; | gut-  in  mnd.  koder  m.,  nhd.  dial.  Kö
51 | za^  guzma  stehen  kuza  , Haufen',  kuzma  ,Hühnerkropf', die  formantisch  mit  guza  usw.  im  Zusammenhang  stehen,  im  anlaut.  k- aber  ein  mit  av.  /ra-,  apa-kava-  ,vorn,  hinten  mit  ei
52 | ',  kawpa ,  Knolle'; | hingegen  stammen  wohl  aus  lat.  cuppa  f.  ,Becher' :  ags.  copp  m.  , Gipfel^ Becher'  (mengl.  auch  ,Kopf'),  cupp  m.,  cuppe  f.  ,Becher',  nhd.  (eigentlich  '^^ md.
53 | che' (ndl.  kuil  ,der  mittlere,  sackförmige  Teil  eines  Netzes'  aber  nach  Franck- van  Wijk  Wb.  356  aus  andl.  kuidel  von  der  ^Erw.  der  Wz.);  ahd.  ^•äZt, mhd.  kiule^  nhd.  Keule  
54 | n'  (fraglich  hingegen  sloven usw.  zur  , Molken'  wegen  der  auf  g  weisenden  Nebenform  sloven.  züra zgra  ,Molken'); | lit.  gauras  m.,  meist  PL  gauraX  ^Haar  am  Körper,  Flachsfaser',  
55 | s-  ,Schnellig- j^eit',  jdvana-h  , treibend,  anregend'; | av.  zavah-  n.  ,Kraft,  Stärke',  zävar-  n.  , (physische)  Kraft,  Stärke'  (bes. der  Füße  und  der  Rosse),  npers.  zör  , Kraft',  b
```


## [2026-09-05T20:52:55.011Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"biegen,  krümmen,  wölben\\|krümmen,  wölben\" POK_02.txt | head; echo ---; python3 - <<'EOF'\nt=open('POK_02.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nimport re\nfor i in range(46,54):\n    p=pages[i]\n    for kw in ['wölben','Ecke','Winkel','gaoša','gösa','gös','Ohr']:\n        for m in re.finditer(kw,p):\n            print(i,kw,'::',p[max(0,m.start()-200):m.start()+200].replace('\\n',' | '))\n    print('--- leaf',i)\nEOF"
}
```


### [2026-09-05T20:52:56.630Z] TOOL RESULT

```
682:(reü-,  g^^-f  S^-  ^biegen,  krümmen,  wölben^;  Nominalbildungen:  gudom ^Darm;  Eingeweide^;, ^uf-r  ^Kehle^  Hals^;,  gugä  ^Kugel,  Buckel,  geu-lo-s ^rundes  Gefäß,  KugeP,  gou-no-m  ^Gekräuseltes,  Gewölbtes^,  gupä ,Erdhöhle,  StalP,  geu-ro-s,  gou-ro-s  ^gekräuseltes  (Haar,  Welle)', gur-no-s  ,Rücken,  Hüfte',  gü-ro-s  ,rund,  gekrümmt'.
---
--- leaf 46
--- leaf 47
48 wölben :: intr.  sich  wenden',  hecierran drehen',  cierr  m.  (*karzi-)  ,Zeit,  Mal,  Geschäft'. | WP.  I  609  f.,  WH.  I  594,  596,    Loth  RC  40,  375  f.      , | (reü-,  g^^-f  S^-  ^biegen,  krümmen,  wölben^;  Nominalbildungen:  gudom ^Darm;  Eingeweide^;, ^uf-r  ^Kehle^  Hals^;,  gugä  ^Kugel,  Buckel,  geu-lo-s ^rundes  Gefäß,  KugeP,  gou-no-m  ^Gekräuseltes,  Gewölbtes^,  gupä ,Erdhöhle,  Stal
--- leaf 48
--- leaf 49
--- leaf 50
51 wölben :: ühnerkropf', die  formantisch  mit  guza  usw.  im  Zusammenhang  stehen,  im  anlaut.  k- aber  ein  mit  av.  /ra-,  apa-kava-  ,vorn,  hinten  mit  einem  Höcker'  und der  Sippe  qeu-  , biegen,  wölben'  zusammenhängendes  Wort  zur  Voraus- setzung haben; | über   das   von   slav.  guz-  nicht   sicher   zu   trennende  ggz-  s.  unter  geng-. | c.  Labialerweiterungen;  gupä  , Erdhöhle'. | Gr. 
--- leaf 51
--- leaf 52
--- leaf 53
```


## [2026-09-05T20:53:11.849Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('POK_02.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in (53,54):\n    print('==== leaf',i,'(p.%d)'%(i+344))\n    print(pages[i])\nEOF"
}
```


### [2026-09-05T20:53:13.880Z] TOOL RESULT

```
==== leaf 53 (p.397)
che' (ndl.  kuil  ,der  mittlere,  sackförmige  Teil  eines  Netzes'  aber  nach  Franck- van  Wijk  Wb.  356  aus  andl.  kuidel  von  der  ^Erw.  der  Wz.);  ahd.  ^•äZt, mhd.  kiule^  nhd.  Keule  (urgerm.  ^külön-)  , Stock  mit  dickem  kugelförmigem Ende',  mnd.  küle  , Keule,  keulenförmiges  Gefäß,  Hode,  Geschwulst,  Kaul- quappe; (konkav:)  , Grube,  Höhle'  (letztere  Bed.  auch  in  mhd.  küle^  nhd. (md.)  kaule  und  aschwed.  küla)^  mhd.  küle,  nhd.  Kaule  ,KugeI,  kugel- förmiger Gegenstand',  nhd.  Kaulquappe  (vom  kugelförmigen  Aussehen), anord.  küla  ,Beule,  Kugel';  nhd.  mdartl.  kulle  , Kugel,  Rolle,  Walze', kullern^  kollern  ,rollen,  kugeln'  ( :  gr.  yvXXög '  y.vßog  ^  lergaycovog  Xid-og Hes.  mit  Verblassen  der  Bed.  des  runden?);  vermutlich  auch  a.nov^.  kollr m.  , abgerundeter  Gipfel,  Kopf,  mnd.  kol^  kolle  m.  ,Kopf,  oberster  Teil von  Pflanzen',  nhd.  kullhock  und  (hochstufig)  kielbock  ,hornloser  Bock', vgl.  alb.  tsjap  gul  ,hornloser  Bock';  norw.  keyla  (^kauliön)  ,Rinne,  Kanal'.
e.  Mit  7J -Suff ix;  gou-no-zn  , Gekräuseltes,  Gewölbtes'. '   Av.  gaona-  n.  ,Haar  (bes.  der  Tiere);  (Haar) färbe'  (vgl.  oben  lit.  ^rawrar usw.);
speziell  germ.  Bildung  anord.  kann  n.  , Beule',  mnl.  coon  f.  ,Kiefer, Kinnbacken',  nid.  koon  ,Wange'  (*Ä:awnö);  dazu  got.  kuna-wida  , Fessel' (»gekrümmter  Strick',  zu  ahd.  icidi  , Strick').
/.  Mit  r-Suf fixen;  geu-ro-s,  gou-ro-s,  gü-ro-s,  gur-no-s.
Arm.  kui-n  Gen.,  ki'-an  , Rücken'  (=  lit.  gurnas),  kr-ukn^  Gen.  krkan  ,Ferse', kui%  Gen.  kri  ,Boot,  Kahn',  auch  , Becken,  Napf,  Pfanne';  kray  (^güräti-) , Schildkröte' ;  o-stufig  kor  {^gou-ero-  oder  -^ro-)  , gekrümmt,  gebogen;  ver- kehrt', kori  , Kanal',  koriz  , Geschwulst;  Obstkern,  Samenkorn';
gr.  yvqög  ,rund,  ausgebogen',  yvqog  , Rundung,  Kreis,  runde  Grube', yvQOb)  ,krümme',  yvQLvog  oder  yvQivog  ,Kaulquappe'  (wie  mnd.  kü-le,  nhd. Kaulquappe^  s.  oben);
mir.  güaire  ,Haar'  (ursprüngl.  ,*Kraushaar',  vgl.:)  nir.  guairnedn ,Wirbelwind' ;
398  f
iiorw.  haure  ,krause  Locke  (bes.  von  Wolle)',  kaur  ,gekräuselte  "Welle^ (idg.  "^gou-ro-;  daneben  germ.  '^kait-ara-  in:)  anord.  karr  m.  ,krause  Locke' käri  ,das  Wasser  kräuselnder  Windstoß',  norw.  käre  ,Hobelspan' ;  mit  -^u, das  germ.  Lehnwort  finn.  keuru  ,curvus';  mit  iZ  (vgl.  yvqoq  und  die  ^  ent. haltenden  arm.  Worte)  norw.  küra  ,sich  zusammenkauern;  ruhen',  mn^ küren  ,(dem  Wild)  auflauern',  nhd.  kauern]  mit  Anwendung  von  Gerinnen der  Milch  norw.  kjere  i^keuran-)  ,Käse  im  ersten  Zustand',  kür  (^kuraÄ ,ds.,  geronnene  Milch',  keyr  {^^kauri-)  ,Käsemasse  von  säuerlicher  Milch* kaara  (^kauarön)  ,gerinnen,  käsig  werde
==== leaf 54 (p.398)
n'  (fraglich  hingegen  sloven usw.  zur  , Molken'  wegen  der  auf  g  weisenden  Nebenform  sloven.  züra zgra  ,Molken');
lit.  gauras  m.,  meist  PL  gauraX  ^Haar  am  Körper,  Flachsfaser',  lett. gauri  m.  PL  , Schamhaare'  (vgl.  oben  av.  gaona-  n.  ,Haar');  lit.  gurnat m.  ,Hüfte,  Fußknöchel',  lett.  gürus  ,Hüfte,  Gabel  am  Spinnrad'  (==  arm kufn)'^  lit.  gurinti^  gürüoti  ,gekrümmt  gehen',  lett.  güräties,  guorities  sich rekeln';  lit.  kdlno  güras  m.  , Bergvorsprung' ;
serb.  güra  f.  , Höcker',  güriti  se  ,sich  zusammenziehen,  krümmen'-  ob hierher  skr.  züriti  se  ,sich  eilen'?;  s.  auch  unter  geu-  , fördern,  eilen';  auch bulg.  gürkam^  gürm  ,tauche  ins  Wasser'?;  die  Intonation  erforderte  *^öwra oder  "^gou^rä  (vgl.  oben  anord.  karr  usw.).
g.  Mit  s-Suffixen:
npers.  gösä  ,Winkel,  Ecke';  .^
gr.  yvrjg  ,Krummholz  am  Pflug',  Ixqotqov  airöyvov  ,Pflug,  an  dem  Krumm- . holz  und  Scharbaum  noch  aus  einem  Stück  bestanden'  (s-Suffix  unsicher) wozu  yvrjg  , Ackermaß'  ('^yv[a]äg-,  aber  auch  "^yvJ^äg-  möglich);  gr.  yvToy , Glied  Arm  und  Bein',  y^rjXQÖg  yvTcc  , Schoß',  yvtöü)  ,lähme',  woraus  yvLÖg ,gliederlahm'  (Grdf.  "^yva-iov-  oder  yvf-iov?  ders.  Zweifel  bei  yvaXov,  s.  oben), yavaög  ,krumm,  auswärts  gekrümmt  (von  Beinen)',  yavGÖo^iai  ,krümme mich'  (aber  yavaddag'  ifjsvörjg  Hes.  vielleicht  galatisch,  zu  air.  gdu,  Lüge'?) kann  a  nach  andern  Adj.  auf  -aög  für  ,gekrümmt'  bewahrt  haben,  doch ist  auch  das  av  schwierig,  da  ein  Ablaut  *^ew-  :  gdu-  trotz  der  häufigen Stufe  *^ü- nicht  sicher  steht;  unklar  hom.  äiKpiyvog,  Beiwort  des  Speeres, und  dixcpiyvrjeig,  Beiwort  des  Hephaistos;
mnd.  nnd.  küse  ,Kolben,  Keule;  Backenzahn',  norw.  dial.  küs  ,BuckeI*; schwed.  kusa  ,cunnus';  anord.  kjöss  f.  ,Tasche',  kjöss  m.  ,Bucht,  HöhlungS far0.  kjös  f.  ,KropfS  schwed.  kjusa  ,Talschlucht',  kjus  ,Ecke  eines  Sackes* u.  dgl.,  norw.  kysa  (*keusiön-)  und  kei/sa  (*kausiön-)  ,Haube,  Kapuze'.
WP.  I  555ff.,  WH.  I  112f.,  311,  629,  852,    Trautmann  80,  lOOf.
399
^eü'f  ^^o^"  (daneben  geu9-)  , fördern,  eilen'?
J^i.junäti  , treibt  zur  Eile,  treibt  an,  facht  ^n^jdvate  ,e\\t\  jütd-h  , eilend', jfi-  ^schnell',  Jw^i  , Schnelligkeit,  Aufmunterung',  j'avzn  , eilend',  java-/i  , eilend, ^chneW,  jävistha-h  ,der  rascheste',  m.  ,Eile,  Schnelligkeit',  jdva
```


## [2026-09-05T20:53:30.414Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('POK_02.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in (51,52):\n    print('==== leaf',i,'(p.%d)'%(i+344))\n    print(pages[i])\nEOF"
}
```


### [2026-09-05T20:53:32.296Z] TOOL RESULT

```
==== leaf 51 (p.395)
za^  guzma  stehen  kuza  , Haufen',  kuzma  ,Hühnerkropf', die  formantisch  mit  guza  usw.  im  Zusammenhang  stehen,  im  anlaut.  k- aber  ein  mit  av.  /ra-,  apa-kava-  ,vorn,  hinten  mit  einem  Höcker'  und der  Sippe  qeu-  , biegen,  wölben'  zusammenhängendes  Wort  zur  Voraus- setzung haben;
über   das   von   slav.  guz-  nicht   sicher   zu   trennende  ggz-  s.  unter  geng-.
c.  Labialerweiterungen;  gupä  , Erdhöhle'.
Gr.  yvTtr]  , Erdhöhle,  Schlupfwinkel,  Geiernest'  (Hes.);  yvxp^  yvTTÖg  , Geier' (vom  krummen  Schnabel  oder  den  krummen  Klauen,  wie  ygvxp  zu  yQVTtög ,gekrümmt');
ahd.  chubisi  ,tugurium',  mhd.  kohe  , Stall,  Schweinestall,  Käfig,  Höhlung', nhd.  Koben  , kleines,  schlechtes  Gemach  oder  Gebäude,  Schweinestall' (dazu  mhd.  kobolt^  nhd.  Kobold^  z.  B.  Kluge ^^  315),  ags.  cofa  (engl,  cove) , Kammer,  Versteck,  Höhle'  (daraus  anord.  kofi  .Kammer,  Zelle'),  westfäl. kilffe  (^kufjö)  , schlechte  Hütte' ;  Grundbed.  ,Loch  in  der  Erde  als  Wohn- grube', eigentl.  ,Einwölbung',  ndd.  Kübbung  ,Anbau' ;  mhd.  nhd.iro5e?',Korb' ; holl.  kub^  kubbe  ,Fischreuse' ;  mhd.  kobel  m.  , (gewölbter)  Kasten,  enges schlechtes  Haus,  Stall' ;  hingegen  stammen  mhd.  kobel  n.  , Felsenschlucht', kofel  , Bergkuppe',  nhd.  bair. -allem.  Kofel^  Kobel^  Gufel,  rätorom.  cüvel^ ital.  cövolo  , Höhle,  Felswand'  aus  lat.  '^cubidum  (zu  cubäre)  , Lagerstätte des  Viehs'  (Zinsli,  Grund  u.  Grat  322)  und  ahd.  miluh-chubül  ,Milchkübel', mhd.  kübel^  nhd.  Kübel  wohl  aus  mlat.  cupellus;
anord.  küfr  , runde  Spitze,  Haufen',  norw.  küveri  , rundlich,  gewölbt' (davon  norw.  kuva^  kyva  , abrunden,  abstumpfen',  vgl.  auch  schwed.  kuffa , bändigen,  stoßen  =  ndd.  kuffen  , stoßen,  ohrfeigen'),  holl.  kuif  (mndl. *cwve)  ,Federbusch,  Schopf,  Haube,  Baumwipfel'  (vgl.  in  ähnlicher  Bed. frühnhd.  Kaupe  , Federbusch,  eigentlich  Haube,  auf  dem  Kopf  der  Vögel'
Mi
396
aus  ahd.  *küha,  wohl  aus  der  rom.  Sippe  von  cüpa,  ebenso  ags.  cyf  ,p^^ Tonne',  as.  küvln  ,Faß',  vgl.  frz.  cuve  aus  lat.  cüpa  ,Kufe') ;
germ.  ""kuhb- :  westflämisch  kohbe  ,Federbüschel,  buschiges  Haar,  Ilutkopp aisl.  kobbi  m.  ,Seehund\  bair.  koppen  ,buschige  Krone  eines  Nadelbaumes»* engl,  ciib  ,Junges',  cob  ,runder  Klumpen,  Kopf,  Spinne',  vermutlich  auch isl.  kubbur,  kubbi  ,Klotz,  Stumpf  (dazu  schwed.  isl.  norw.  kubba  ,abhauen*);
germ.  *A:wp-:  norw.  dial.  küp  ,Buckel',  schwed.  kupa  ,h albkugelförmiges Gehäuse,  Bienenkorb'  u.  dgl. ;   schwed.    kypa    ,rundes    Gefäß    aus   Stroh\ .. ndd.   küpe  ,großer  Tragkorb',    engl.    dial.    klpe   (ags.   ^ci/pe)    ,geflochtene Fischreuse,   Korb';    ablautend  norw.   dial.  kanp   ,hölzerne  Kanne
==== leaf 52 (p.396)
',  kawpa ,  Knolle';
hingegen  stammen  wohl  aus  lat.  cuppa  f.  ,Becher' :  ags.  copp  m.  , Gipfel^ Becher'  (mengl.  auch  ,Kopf'),  cupp  m.,  cuppe  f.  ,Becher',  nhd.  (eigentlich  '^^ md.)  Koppe  ,Kamm  (Haube)  der  Vögel',  Koppe,  Kuppe  ,runder  Berggipfel*^ mhd.  kuppe,  ahd.  chuppa  ,Kopfbedeckung'  (mit  expressiver  Verschärfung ahd.  chuppha  ds.,  mhd.  kupfe,  kuffe,  gupfe  ds.,  gupf,  gupfe  m.  ,Gipfel eines  Berges,  Spitze  des  Turmes',  worin  g-  wohl  Substitution  für  roman» ;,; C-;  anord.  koppr  ,Kopf,  Gefäß,  Helmknopf,  Augenhöhle'  ist  Lw.  aus  mnd. kopp)]  afries.  mnd.  kopp  ,Becher',  ahd.  köpf,  chuph  , Becher',  mhd.  köpf ,Trinkgefäß,  Hirnschale,  Kopf  (ähnlich  rom.  testa  ,Kopf  aus  lat.  testa , Scherbe,  Schale',  mlat.  testa  capitis),  nhd.  Kopf
Nasaliertes  germ.  '^kumb-:  ags.  cumb  (engl,  coomb)  ,Napf'  (in  der  Bed. ,Tal'  aus  abrit.  *kumbo-s  ,Tal'),  mnd.  kumm(e)  f.  , rundes,  tiefes  Gefäß, Kufe,  Napf,  nhd.  Kumme  , tiefe  Schale',  Schweiz,  chumme  , Zisterne'; ^kump-  (aus  *kumb-  mit  Kons. -Schärfung)  mnd.  kump,  mhd.  Äjwwip/ , Gefäß, Tasse',  nhd.  Kumpf
Dazu  vielleicht  npers.  gumbed  ,Wölbung,  Kuppel,  Becher';
ferner  vermutlich  lit.  gumbas  m.  , Wölbung,  Geschwulst,  Knorren';  lett. gumba  , Geschwulst';
aksl.  g^ba  , Schwamm,  Pilz',  skr.  güba  , Schwamm,  Aussatz',  sloven.  ggba , Schwamm,  Pilz'^  göbec  m.  ,Maul',  aöech.  hüba  .Schwamm',  jünger  ,Maul, Lippe',  russ.  gubd  ,Baumschwamm' ;  daneben  güba  ,Lippe' ;  im  Slav.  liegt Intonationswechsel  vor,  die  Bedeutung  ,Maul'  ist  überall  jünger.
Unter  einer  Grundbed.  , bergen'  wurde  nhd.  Koben  verbunden  mit  av. gufra-  ,tief;  geheimnisvoll,  wunderbar',  angeblich  ursprünglich  ,in  eine Grube  versenkt'?
d.  Mit  Z-Suf fixen;  geu-Io-s  ,rundes  Gefäß'.
Ai.  göla-h  ,Kugel',  gölä,  gölam  ,Ball,  runder  Wasserkrug' ;  vielleicht  ai. gula-h,  gull,  gulikä  ,Kugel,  Kügelchen,  Spielball'  (oder  als  gj,-  zu  *gel- , ballen') ;
397
arm.  kaluni  ,ich  nehme,  fasse^  (^W«^^)»
gr.  yvliOQ  , längliche  Tasche'  (auch  yoy-yvXog'?  s.  gong--^  üher  yojXeög s.  unter  "^gol-  ,lieg-en');
gr.  yvaXov  , Höhlung  des  Panzers',  später  , Schlucht',  meg.  yvdXäg  ,Trink- becher^,  iyyvaU^cü  , händige  ein'  (vgl.  zu  letzterem  iyyvdcj  unter  ^goud-) können  auch  als  "^yvaaXo-  von  der  s-Erw.  '^g{e)iL-s-  stammen;
lat.  vola  f.  , Höhlung  der  Hand,  des  Fußes'  (^gu-ela)]
ahd.  kiol^  ags.  ceol^  anord.  kjöll  m.  ,(*rundliches)  Fahrzeug,  Schiff  (die jüngere  Bed.  ,Kiel'  durch  Einfluß  von  anord.  kjqlr  ,Kiel' ;  germ.  "^keula- =  ai.  göla-)^  ahd.  kiulla  ,Tasche' ;  ags.  cyll{e)  , Schlauch,  Gefäß',  entlehnt aus  lat.  culleus;  woraus  finn.  keula  , Steven',  anord.  kyll  m.  ,Sack,  Tas
```


## [2026-09-05T20:53:46.187Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('POK_02.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in range(49,52):\n    print('==== leaf',i)\n    print(pages[i][:2500])\nEOF"
}
```


### [2026-09-05T20:53:47.949Z] TOOL RESULT

```
==== leaf 49
Dentalerweiterungen:
gnd-,  geud'  (vereinzelt  g-u-ed-?),  vor  allem  im  Germ.;  gudo-m  ,Darm'.
Ai.  guddm  ,Darm';
maked.  yöda '  evrega  MaxEÖöveg  Hes. ;
ndd.  kilt  ,Darm',  nhd.  bair.  kütz  ,ein  Teil  der  Gedärme';  ndd.  küt,küte
auch  ,Eingeweide  kleinerer  Tiere,  Rogenbeutel;  Wade;    Tasche,  Beutel',
mnd.  küt  ,Weichteile  im  Tierkörper,  Rogenbeutel,  Wade',  holl.  kuit  (*küt-)
•  und   kiete    (*keot-)   ,Fischrogen ;   Wade',    engl,    mdartl.    kyte,  kite  , Bauch,
Magen'  (vgl.  zur  Bedeutung  unten  qipus) ;
afries.  käte  (*kaut-)  , Knöchel',  mnd.  köte,  küte  ,Huf,  Klauen,  bei  Pferden das  Fußgelenk',  ndd.  (und  entlehnt  nhd.)  Kote,  Köte  .Knöchel,  Fessel  der Pferde',  Demin.  mnd.  kötel,  nd.  Kötel  (aus  ^kiitü)  , rundliche  Exkremente z.  B.  von   Ziegen,  Pferden',  mndl.  cotel,  holl.  keutel  ,ds.,  Kegel,  Knirps';
norw.  dial.  kyta  , Buckel,  aufgebauschte  Falte,  Anschwellung  an  einem feisten  Körper,  sackförmige  Erweiterung  eines  Netzes',  schwed.  dial.  küta ,mit  gekrümmtem  Rücken  gehen  oder  laufen',  nhd.  kauzen  =  kauern  (,sich zusammenkrümmen'),  geminiert  schwed.  kott{e)  , Tannenzapfen',  dial.  kutte, kutting  ,kleiner  feister  Knabe' ;
mit  dem  Begriff  der  Einbiegung,  Höhlung:  ndd.  küte  , Grube',  mhd.  küz, nhd.  Kauz  , Grube  als  Gerichtsstätte'  (formell  =  norw.  dial.  küt  ,\Qr- krüppelung  im  Wuchs',  schwed.  dial.  ,Knolle,  Buckel';  mhd.  küte  , Grube, Loch',  nhd.  mdartl.  Kaute  ds.  wohl  aus  dem  Ndd.);  norw.  dial.  keyta jEinsenkung  im  Erdboden,  Pfütze;  Gefäß,  worin  man  Fische  trägt'  i^kauti-) =  mhd.  koetze,  nhd.  mdartl.  Kötze  , Ruckkorb',  ags.  cyte  , Hütte,  Haus, Lager'  (y  =  le)  =  norw.  keyta  , Waldhütte  aus  Zweigen',  vgl.  nhd.  dial. kieze  , Bastkorb'  (-ew-),  ags.  cyt-wer  , Fischreuse'  mit  expressiver  Geminata
394  ,
mnd.  usw.  kutte  ,cuniius'  (mlid.  kotze  ,meretrix');  Loch  =  schlecht^ Wohn-  oder  Liegerstatt:  ndd.  (und  entlehnt  nhd.)  kot,  kote  ,Schuppen Stall,  HütteS  mndl.  cot,  cote  , Höhle,  Lager  wilder  Tiere,  Stall,  schlecht^ Hütte',  ags.  cot  ,(Räuber-)  Höhle,  Haus,  Lager',  anord.  kot  ,kleine  Hütte', kytia  ds. ;
nasaliert  anord.  kunta  ,vulva'  aus  mnd.  kunte  ,cunnus;  auch  Hintere^ norw.  schwed.  kunt  ,Ranzen  (von  Birkenrinde)';  auch  av.  gunda-,  gund^ ,Teigballen'?
gU't-,  geu't']  über  gu-et-  siehe  besonderen  Artikel;  gut-r  ,Kehl
==== leaf 50
 ceod{a)  m.  ,Sack,  Tasche',  ahd.  kiot  ds.,  mnd.  küdel  , Tasche', mhd.  kiutel , Wamme,  Unterkinn',  nhd.  Keutel , Fischnetz,  Darm,  Geschwulst';
gut-  in  mnd.  koder  m.,  nhd.  dial.  Köderl,  Goderl  (^gut-ro-)  ,Unterkinn, Kropf,  ndd.  koden  ds.,  engl,  cud  ,das  Innere  des  Schlundes  bei  Wieder-, käuern',  ndl.  kossem  ,Unterkinn'  (*gutsvio-),  norw.  kusma  ,parotitis' ;  mhd. kuteln,  nhd.  Kutteln  ,Kaldaunen' ;
mit  expressivem  dd:  ags.  codd  m. , Hülse,  Schote,  Sack',  aisl.  koddi  , Kissen, Hode' ;  vielleicht  ahd.  kutti  , Herde',  nhd.  Kette,  bair.  kütt  , Schar  jagd- barer Tiere';
hitt.  ku-u-tar  (kuttar),  Dat.  ku-ut-ta-ni  {kuttani)  n.  ,Nacken,  Oberarm' (=  lat.  guttur,  s.  oben) ;  kuttanalli  , Halskette'.
6.  Gutturalerweiterungen;  gugä  , Kugel'.
Mhd.  kugel(e),  nhd.  Kugel,  mnd.  hoU.  kogel  ds.,  nhd.  dial.  Kogel  , runde Bergkuppe'  (Persson  Beitr.  113);  rhein.  Klugel,  Krugel  nach  Persson  wohl erst  durch  Verquickung  mit  kliuiuel  und  Klüngel]
mit  gg:  ags.  cycgel,  engl,  cudgel  (*kuggila)  ,Knüttel',  anord.  kuggr  aus mnd.  kogge,  engl,  cog  , breites,  plumpes  Seeschiff';
mit  germ.  k:  isl.  kjüka  , Fingerknöchel',  norw.  kjüka  ,Klumpen',  kokle, kukle  jKlumpen',  kokla  (und  kogla),  kokul  .Fruchtzapfen  der  Nadelbäume'; ags.  cycel,  nengl.  dial.  kitchel  , kleiner  Kuchen' ;  dazu  anord.  kjüklingr mit  , Gänschen',  ags.  ciecen,  nengl.  chicken,  mnd.  küken,  nhd.  Küchlein ,Hühnchen' ;
mit  germ.  kk:  ahd.  coccho,  nhd.  mdartl.  Kocke  , Haufen,  Heuhaufen, Misthaufen'^  dän.  kok{k)  , Haufen,  Heuhaufen' ;
lit.  gugä  f.  , Knopf,  Buckel,  Hügel',  gaugaras  m.  , Gipfel  eines  Berges*;
russ.  guglja,  poln.  guga  , Beule'  (Persson  Beitr.  937);  aber  lit.  guoge,  göge f.  ,Kopf',  gogas  m.  , Widerrist  des  Pferdes',  wohl  nicht  aus  dehnstufigem *gö[u]-g-;  anders  darüber  Trautmann  KZ.  43,  176;
395
mit  -g-:
npers.  güzak  .Fußknöchel' (?);
lit.  güzas  , Knorren,  Beule,  Kropf,  güzys  , Kropf,  ganze  ,Kopf,  lett fjuza,  gnza  .Kropf,  guznia  , Haufen,  Höcker',  guza  , Hüfte,  Lende,  Keule beim  Braten' ;
a6ech.  hyzü  , Hüfte,  Oberschenkel',  poln.  giza^  giza  , Knochenkopf  am Schienbein  u.  dg'L'  (auch  ksl.  gyza  vimnaja  , Weinstock',  serb.  gidza  ds. als  , Knorren,  Knorrengewächs') ;  wahrscheinlicher  hierher  als  zu  *geng- (s.  dort),  poln.  guz  , Beule,  Höcker',  guza  , Hinterer',  ^loven.  
==== leaf 51
za^  guzma  stehen  kuza  , Haufen',  kuzma  ,Hühnerkropf', die  formantisch  mit  guza  usw.  im  Zusammenhang  stehen,  im  anlaut.  k- aber  ein  mit  av.  /ra-,  apa-kava-  ,vorn,  hinten  mit  einem  Höcker'  und der  Sippe  qeu-  , biegen,  wölben'  zusammenhängendes  Wort  zur  Voraus- setzung haben;
über   das   von   slav.  guz-  nicht   sicher   zu   trennende  ggz-  s.  unter  geng-.
c.  Labialerweiterungen;  gupä  , Erdhöhle'.
Gr.  yvTtr]  , Erdhöhle,  Schlupfwinkel,  Geiernest'  (Hes.);  yvxp^  yvTTÖg  , Geier' (vom  krummen  Schnabel  oder  den  krummen  Klauen,  wie  ygvxp  zu  yQVTtög ,gekrümmt');
ahd.  chubisi  ,tugurium',  mhd.  kohe  , Stall,  Schweinestall,  Käfig,  Höhlung', nhd.  Koben  , kleines,  schlechtes  Gemach  oder  Gebäude,  Schweinestall' (dazu  mhd.  kobolt^  nhd.  Kobold^  z.  B.  Kluge ^^  315),  ags.  cofa  (engl,  cove) , Kammer,  Versteck,  Höhle'  (daraus  anord.  kofi  .Kammer,  Zelle'),  westfäl. kilffe  (^kufjö)  , schlechte  Hütte' ;  Grundbed.  ,Loch  in  der  Erde  als  Wohn- grube', eigentl.  ,Einwölbung',  ndd.  Kübbung  ,Anbau' ;  mhd.  nhd.iro5e?',Korb' ; holl.  kub^  kubbe  ,Fischreuse' ;  mhd.  kobel  m.  , (gewölbter)  Kasten,  enges schlechtes  Haus,  Stall' ;  hingegen  stammen  mhd.  kobel  n.  , Felsenschlucht', kofel  , Bergkuppe',  nhd.  bair. -allem.  Kofel^  Kobel^  Gufel,  rätorom.  cüvel^ ital.  cövolo  , Höhle,  Felswand'  aus  lat.  '^cubidum  (zu  cubäre)  , Lagerstätte des  Viehs'  (Zinsli,  Grund  u.  Grat  322)  und  ahd.  miluh-chubül  ,Milchkübel', mhd.  kübel^  nhd.  Kübel  wohl  aus  mlat.  cupellus;
anord.  küfr  , runde  Spitze,  Haufen',  norw.  küveri  , rundlich,  gewölbt' (davon  norw.  kuva^  kyva  , abrunden,  abstumpfen',  vgl.  auch  schwed.  kuffa , bändigen,  stoßen  =  ndd.  kuffen  , stoßen,  ohrfeigen'),  holl.  kuif  (mndl. *cwve)  ,Federbusch,  Schopf,  Haube,  Baumwipfel'  (vgl.  in  ähnlicher  Bed. frühnhd.  Kaupe  , Federbusch,  eigentlich  Haube,  auf  dem  Kopf  der  Vögel'
Mi
396
aus  ahd.  *küha,  wohl  aus  der  rom.  Sippe  von  cüpa,  ebenso  ags.  cyf  ,p^^ Tonne',  as.  küvln  ,Faß',  vgl.  frz.  cuve  aus  lat.  cüpa  ,Kufe') ;
germ.  ""kuhb- :  westflämisch  kohbe  ,Federbüschel,  buschiges  Haar,  Ilutkopp aisl.  kobbi  m.  ,Seehund\  bair.  koppen  ,buschige  Krone  eines  Nadelbaumes»* engl,  ciib  ,Junges',  cob  ,runder  Klumpen,  Kopf,  Spinne',  vermutlich  auch isl.  kubbur,  kubbi  ,Klotz,  Stumpf  (dazu  schwed.  isl.  norw.  kubba  ,abhauen*);
```


## [2026-09-05T20:53:58.629Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('POK_02.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in range(243,254):\n    p=pages[i]\n    nums=re.findall(r'(?m)^\\s*(5[89]\\d)\\s*$', p)\n    hasnp=[m.start() for m in re.finditer('npers|apers|Apers|av\\\\.', p)]\n    print(i, 'pagemarkers',nums, 'len',len(p))\nEOF"
}
```


### [2026-09-05T20:54:00.393Z] TOOL RESULT

```
243 pagemarkers ['585'] len 2679
244 pagemarkers [] len 2705
245 pagemarkers ['587'] len 2740
246 pagemarkers [] len 2761
247 pagemarkers ['589'] len 2822
248 pagemarkers ['590'] len 3048
249 pagemarkers ['591'] len 2897
250 pagemarkers [] len 2367
251 pagemarkers ['593'] len 2693
252 pagemarkers [] len 2379
253 pagemarkers ['594'] len 1738
```


## [2026-09-05T20:54:03.730Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('POK_02.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in (247,248):\n    print('===== leaf',i); print(pages[i])\nEOF"
}
```


### [2026-09-05T20:54:05.376Z] TOOL RESULT

```
===== leaf 247
-)^ wovon  skygna  ,spähen';  got.  skauns  ,schön^  (ihna-skauns  ,von  gleicher  Ge- stalt'), ahd.  scöni  ds.,  aisl.  skjöni,  as.  sköni  ,glänzend,  schön',  ags.  sclene ds.  (eigentlich  ,conspicuous') ;  tiefstufiges  *sku-ni-  in  aisl."  6%n  f.  n.  ,Ord- nung,  Bescheid,  Einsicht',  skynja  ,untersuchen,  verstehen';  aisl.  skoda ,spähen';
apr.  aw-sc/ia«c?i^i(;ei., vertrauen'.
WP.  I  368  ff.,  WH.  I  186  f.,  Trautmann  132.
2.  keu-,  keup-,  of   mit   labialen   oder   gutturalen    Erweiterungen:   ,biegen'
in  verschiedenen  Sonderungen  wie  ,im  Gelenk  biegen,   Gelenk,  sich
bücken,  sich  drehen^;   ,Einbiegung,  Einwölbung,  Höhlung^-   ,Ausbie-
gung,  Buckel,  runder  Haufen';  kubo-s,  kubbo-s  ,gehöhlt,  gekrümmt',
kumb{ti)o-s  ,Gefäß',  kupro-s  , Buckel',  küpä  ,Höhlung,  Hohlgefäß',
koupo-s  ,Berg,   Haufen^,   kouko-s    ,gewölbt^,    ka-kud-    ,Wölbung^
Zahlreiche  Parallelbildungen  von  der  Wz.  geu-  s.  dort,  vgl.  bes.  die
Gegenüberstellungen  bei  Persson  Beitr.  100  f.,  104  Anm.  1.  —  Über
den  Versuch  einer  Vermittlung  mit  (s)keu-  ,bedecken'  s.  dort.
Die  einf.  Wz.  in  ai.  kora-  m.  ,bewegliches  Gelenk^;  av.  fra-j  apa-kava-
,vorn,  hinten  buckelig'^;  klr,  külity  ,sich  zusammenziehen,  vor  Kälte^,  poln.
kulic  ,zusammenziehen,  krümmen'.
Ebenso  ist  die  Vorgeschichte  von  lett.  kuza  ,Kropf'  u.  dgl.  wegen  des Reimverhältnisses  zu  guza  usw.  nicht  sicher  zu  beurteilen,  s.  unter  geit- ,biegen'  oben  S.  395.
Unter  einer  Anlautvariante  kh  will  Petersson  KZ.  47,  277  hierher  stellen ai.  khölaka-  , Ameisenhaufe'  (auch  lit.  külys  ,Bund  Stroh'),  zuversichtlicher arm.  xoyl,  Gen.  xuli  ,struma,  scrofula',  russ.  suljata  ,Hoden',  serb.  Hljevi ,goldene  Ader'.
A.  Dentalerweiterung  (redupl.)  ka-ku-d-  ;  ai.  kakud-  ,Kuppe,  Gipfel', käküd-  ,Mundhöhle,  Gaumen',  kaküdmant-  ,mit  einem  Gipfel  oder  Hocker .    versehen';  lat.  cacümen  ,Spitze,  Gipfel'  (die  wew -Weiterbildung  wohl  nach acümen),  Grundbed.  ,Wölbung';    auf  ein  germ.  *hagu  =  ai.  kaküd-  führt    1
589
man    auch    afries.    heüa   ,Kopf^   zurück    {*hagila-,   mit   Suffixwechsel   für hagu-la-)]  vgl.  auch  ai.  kalcübh-  ^GipfeF  unter  ^Labialerweiterungen^
B.  Gutturalerweiterungen.
B.  I.  keu-g-:
aisl.  hüJca  ^kauern,  hocken^  (hüJcta,  st.  Partiz.  hohinn),  hoha,  hohra  ^krie- chen^;  heylciask  ^zusammensinken^  zusammenkriechen'^;.  mhd.  hüchen  , kauern, sich  ducken^,  nhd.  hocJcen-^  Schweiz,  hoch  m.  ^Haufe^,  tirol.  hocken  m. Haufe  Heu^;  mit  anlaut.  s-  mhd.  schoche  m.  .aufgeschichteter  Haufe  Heu u.  dgl/;  (mityfc/c:)  asächs.  sJcoJc  m.  ,60  Stück"^,  mhd.  schoc(7ces)  ,Haufe  Büschel, Anzahl  von  60  Stück^,  mengl.  shocJc  ,Haufe
===== leaf 248
  Garben  (12 — 16)^;  über  Schoch s.  zuletzt  Sommer  ,Zum  Zahlwort^,  S.  78ff.,  S.-ß.  Bayr.  Akad.  1950,  Heft  7;
lit.  hduge,  ablaut.  Jciügis  ,Heuhaufe^,  apr.  Jcugis  ,Knauf  am  Schwertgriff^, lit.  Jcaugurl  ,kleiner  steiler  HügeF,  lett.  käudze  ,Haufen,  Schober^  (und slcaudze).
B.  IL  keu-k'i
Ai.  Jcucdtiy  huncate  ,zieht  sich  zusammen,  krümmt  sicli'^,  Jcicücikä  ,SchlüsseF, kuca-  m.  , weibliche  Brust^,  köcayati  ,zieht  zusammen^,  köca-  m.  ,das  Ein- schrumpfen^, npers.  köz  ,gekrümmt,  buckelig^;
air.  cüar  ,krumm^  (*kukro-) ;
mhd.  hockevj  hogger,  hoger  , Buckel,  Höcker' ;  got.  hauhs,  aisl.  hör,  här, ags.  heah,  as.  ahd.  höh  ,hoch^  (,*aufgewölbt^),  aisl.  haugr,  mhd.  houc ,HügeF,  got.  hiuhma  ,Haufe;  Menge^,  hühjan  ,häufen,  sammeln',  nhd. (md.)  Hügel]
lit.  kaükas  ,Beule,  Eitergeschwür^,  kaukos  PI.  f.  ,Drüsen^,  kaükas  ,Kobold, zwerghafter  Geist',  apr.  cawx  ,Teufel*',  lit.  kaukarä  ,HügeF,  kukulys  ,Mehl- kloß^,  kükis  ,Misthaken^,  lett.  kukurs,  kukums  , Höcker,  Beule^,  kükis  , Zwerg; Zaunkönig^,  küksa  ,eine  vom  Alter  Gebeugte'^,  russ.-ksl.  kukonos^  ,krumm- nasig' ;
russ.  küka  ,Faust',  bulg.  küka  ,Haken,  Krücke',  skr.  kuka  ,Haken', kükonosast  ,hakennasig',  kükara  ,Haken  bei  der  Pflugdeichsel',  okuka,  okuc f.  ,Windung  eines  Flusses';  skr.  cuclra,  cücati  ,hocken,  kauern',  sloven. ^uöim,  cüSati  und  kucirrij  kü^ati  ds. ;  russ.  dial.  küceri  PI.  f.,  klr.  kucery PL  m.  , Locken';  mit  einer  Bed.  ,Haufen'  russ.  küca  ,Haufen',  dial.  , Heu- schober', kückath  ,zusammenballen,  häufen',  kücki  ,die  Plejaden',  öech.  kii^^e ,Masse',  poln.  kuczki  PL  ,kleine  Haufen'.  Abg.  k^k^nj'b  , Unterschenkel'.
C.  Labialerweiterungen. C.  L  keu-b-:
a.  In  Anwendung  auf  Biegungen  am   Körper,   sich   im   Gelenk  biegen:
gr.  y.vßog  ,Höhlung  vor  der  Hüfte  beim  Vieh;  Wirbelknochen — Würfel'
(daraus  lat.  ciihus]  xvßuAov  ,Ellbogen'  Poll.  entweder  von  Y.vßoQ,  mit  Suff.
590
'wlo-  oder  Umbildung  von   %vßiTOv  ds.  —  aus  lat.  cuhitum  —  unter  Ein- Wirkung  von  wlhi])',
lat.  cubitum  n.,  -us  m.  ^Ellbogen'  (daraus  gr.  -nvßiTov  ds.);  cuhö,  -ö^J ,liegen^  (fal.  cwpaj  d.  i.  c?i5a[^],  neben  loferta  ders.  Inschr.,  erweist  ital.  J.f auch  pälign.  incuhat),  lat.  (ac-_,  in-)  cumbö,  -ere  ^sich  legen^  (^rsprüngd ,sich  zum  Liegen  niederbücken^)^  sabin.  cumba  _,lectica^;
cymr.  gogof  ^Höhle^  (Ableitung  mcjmr.  guocobauc),  bret.  Jcougon  ^sj (*upo-lcuba) ;
got.  hups  m.  (St.  hupi-),  ags.  %pe  m.,  ahd.  huf  f.  _,Hüfte^;    aisl.  Äopa ags.  on-hupian   ^zurückweichen^,   ags.    {fen-j   mör-)hop.  n.    ^Schlupfwinkel'] (als  ^Lager^  Höhlung^);
intensives  J-Verbum  ist  ndd.  huppen,  nhd.  hüpfen,  mhd.  hüpfen,  hupfen  i hopfen ;   ö-Verbum   mit   Geminata :   aisl.    hoppa,    ags.    hoppian,  hoppettan  \ nhd.    hopsen]   geminierte   Media   in   schwed.    dial.    hobba,    hubba  ,stoßen'J n
```


## [2026-09-05T20:54:19.471Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PHD gōšag/kōšk/gōn/nigūn/gumbad/gund\"; grep -n \"gōšag\\|gosag\\|kōšk\\|kosk\\|gōn\\b\\|čigōn\\|cigōn\\|nigūn\\|nigun\\|gumbad\\|gund\\b\\|gundag\" PHD.txt | head -40"
}
```


### [2026-09-05T20:54:19.520Z] TOOL RESULT

```
=== PHD gōšag/kōšk/gōn/nigūn/gumbad/gund
384:ёгбһ [glwh | N guroh] group, crowd. gubrág [gwpl’k'] awake, alert, vigilant. ģubrās- [gwp/”s-] = wigras-, v. wigrádan. ģuftan, $0(w)- [YMRRWN-, YMLLWN-tn! < A ymlwn, V тЇ; gwptn', gwb- | M gwptn, gw-, N ~, gā(y)-] say, speak. ~išn: speech. ģuftār [gwpt?] | N ~] speaker. ~ih: (power of) speech. gugiin- [gwk’n- | M gwg^n-] destroy. gugar(i)dan, gugar- [gwk”/-(y)tn! | N guwár-idan] digest. tuģāy [gwk*dy | M gwg'y, N guwah] witness. ~ih: testimony. ģūh [gwh | N —] dung, excrement. guhrayénidan, guhrayén- [gw AP yn-ytn!] waken, arouse. gul [gwl | N ~] flower, rose. ботап [gwnmn! | = M, N ~] doubt. ~par [-A/] casting doubt. ~ig [-yk'] doubtful. ~ih, ~igih: doubt. gumardag [gwmltk'] appointee, deputy. ģumārdan, gumār- [gwm’l-tn' | М gwm'r-dn, N gumāštan, gumar-] appoint, commission, entrust. gumbad [gwmbt' | N ~] dome, fire-temple. £umég [gwmyk! | M gwmyg] mixture. guméxtan, gumēz- [gx”myhtn!, gwmyc- | M gwmyxtn, gwmyz-] mix. ~išn: mixing, mixture; = gumézagih. gumëzag [gwmyck'] mixture. ~th: the Mixture, (the duration of) this material world. Jgund [gwnd | = P] army, troop; group, gathering. *gund [gwnd | N ~] testicle. gung [g(w)ng | N ~] dumb. ģurbaģ [gwibk! | N ~a] cat. Бита [gwlt! | P gwrd, N ~] hero. lih: heroism, bravery. gurdag [gwltk! | N ~a] kidney. *gurdih [ewityh] (some piece of) armour. gurdwār [gwltw’!] befitting a hero. ёпгр [gwlg | N ~] wolf. gurganig [gw/g”nyk! | N ~i] of (the province) Gurgan. gursag [ewlsk] | N gurusna !] hungry. «ЛЬ: hunger. Suën [gvfn! | N ~] male. gusnag [gwšnk! | J gušna] hungry. Gušnasp [gwšn(*)sf] the second major Fire of Sasanian Eran, that of warriors. £yà$ [gyw'k! | M gy'g, N jay] place.
839:army gund, hén, laskar, spāh.
1675:dome gumbad.
1687:downwards nigūnsār.
1951:fire temple dadgah, gumbad.
2083:gathering  čīnišn, ` harróbiin(ih); (group) gund, hanjaman.
2164:group dastag, groh, gund.
3960:testicle gund.
4074:troop gund.
5003:kosk
5429:g gumbad
```


## [2026-09-05T20:54:20.640Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== NYB\"; grep -n \"gōn\\|gōnak\\|kōšk\\|nigūn\\|gumbad\\|gōšak\" NYB_vol2_glossary.txt | head -30"
}
```


### [2026-09-05T20:54:20.690Z] TOOL RESULT

```
=== NYB
```


## [2026-09-05T20:54:26.471Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"gon \\[\\|gōn \\[\\|g6n\\|gwn'\\|kwšk\\|kwsk\\|nykwn\\|colour\\|color\" PHD.txt | head -30; echo \"=== leaf 5003 context:\"; sed -n '4995,5010p' PHD.txt"
}
```


### [2026-09-05T20:54:26.531Z] TOOL RESULT

```
302:čiyðn [cygwn' | М cwn, N čūn) as, like, how, when. — ka: as if. ^h: nature, character.
306:īdabr [dpi] sinner, deceiver. *dabr [dpl] *dark-coloured. dad [dt' | M dd, N ~] wild animal. 1ааа [d't! | M d?d, N ~] law, justice; those scriptures dealing with legal matters. даа [d’t' | N ~] age. зааа [d>1!] tooth. tdād, v. ahlaw-dād. dādan, dah- [YH BWN-tn! < A Vyhb; d*tn!, dh- | M d'dn, (dy-), P dh- N ~, dih-] 1. give; 2. create. —išn [dh(y)sn'] giving, donation; creation. dādār [d’t?l | N ~] creator. -- ih : creatorship. dādestān [DYNA < А dyn; d'ts?n! | M d'(d)ys?n, N dá(de)stan] judgement, justice, law; case, process. dàd-gàh [2^? gs] proper place, fire temple; = daxmag. dādīg [d'tyk'] legal, concerned with the Law. dad-meh (d"tms] adult, elder. dādwar [d?twbl | (M d^ywr, P d'dbr), N da(d)war] judge. ~ih: judgement. daftan, dam- [dptn', dm- | M dm-, N dam-idan] breathe, blow. «dišn: breath. daftar [dptl | N —] register, account-book. dagr [AL YK < А ryk; dgl | M dgr > dur, N dër] long. dagrand [дата | N dërand] long. ~«xwaday [-hwt’y] eternal, of long dominion. daģr|-pattāy [dgl pt'd] long-lasting. -—-zamáàn [-2т?п!] a long time. ^-zi(w)isn [-zywsn'] long-lived. dah [ro, ASLY A < A ә | M dh, N ~] ten. dah-, —išn, v. dádan. Юаһаӣр [dř k' | (N Dahàk)] = Azdahág. dahān [РИМЕ < A p(w)m-h | M dhyn, N даһап] mouth. dahibed [dhywpt! | M dhybyd] ruler, lord of the land.
382:*g5k4n [gwk’n'] details. Lc um ~ig [-yk'] detailed; precisely. (sassa tu) ģūmēz [gwmyc | N giméz] bull's urine (as ritual purifier). ģgūmēz- [gwmyc- | N giméz-] urinate. gön [gwa' | N gün] colour, complexion. ~ag [-k' | M geng, N güna] = gön ; sort, kind, form. gor [gwl | N ~] onager, wild ass. göspand [K YNA < А апу ? ; gwspnd | N ~] (small) cattle, sheep. ~-tihrag [-cyhlk'] holding the seed of cattle. ģūstān [gwst^n!] cattle-stall, cowshed. 1858 [gws | = M, N ~J ear. *GÓ68 [guš | N ~] cal. 14th day. tūšag [gwsk' | N ~a] corner. ģēošūsrūd [rwi^wslwt! = Av. gaošū.srūta-| acquired, learnt. 5051 [BSLYA < A bsr’; рой! | N ~] meat, flesh. ģūšwār [gwštw] | N ~] ear-ring. ģūw-, ~išn, v. ģuftan. gowag [swb k! | М gw'g, N goya] speaking, eloquent; speaker. *ģoūwizār [gwwc'[] explicit, in detail. göy [gwd | N ~] ball. göz [gwc | N ~] walnut. ~énag [gwzynk! | N gózina) a walnut sweetmeat. Gözihr [gwcyhl | Ar. jawzahr] astr. the Dragon. ~ dumb: the descending node of the moon. ~ sar: the ascending node of the moon. grab [22р | P grb] womb. grāmag [gľmk! | P gr’mg] possessions, wealth. grāmig [gľmyk! | M grmyg, N girāmī] treasured, dear. ~ih: affection, respect. 1$raw [giwb! | P grww] cane. *ģraw [glwb' | N giraw] pledge, security. ~ih, ~(a)g4n [glwk’n' | M grug*n, N giraugān] = *graw. grayidan, gray- [gl?d-yin' | P gry-, N gtráy-] lean, incline; intend, desire. ģriftan, gir- [OHDWN-tn' < A V?hd; glptn!, gyl- | M grypt, gyr-, N giriftan, ~] take, hold, restrain. «išnīģ : tangible. griftār [gipt?l | N gir~] held, taken; captive. ~Omand [-'wmnd) tangible. grih [glyh | N girth] knot. lgriw [CWLE < A swr-h; glyw'] neck, throat. ?0riw [CWLE, glyw' | M gryw] self, soul. sgriw [glyw! | P gryw, N girī(b)] a grain measure, modius, peck. griwag [glywk!' | N giriwa] hill, ridge. ģrīwbān [g/ywp?n! | N girībān] neck-guard, gorget. griyistan, griy- [BK YWN-stn'< A У bky; gld-stn! | M gryy-stn, N giristan, giry-] weep, cry.
400:huniyāģar [hwayd’kl | N xunyágar] entertainer, musician. hu-niyox$ [hwnydwhs] attentive. hunsand [hwnsnd | = P, (N xursand)] happy, contented. ~ih : happiness, content. hunušak [hwnsk' = Av. hunu§] offspring (daevic). hunušakēnīdan [hwnskynytn'] bear daevic offspring. hu-pādixšā(y) [hwp?thš”(d)) good ruler. ~th: good rule. hu-passandagih [hwpsndkyh] satisfaction. hur [ŠKL < A fkr; hwl] an alcoholic drink, *koumiss. huram [hwlm | N xurram !] happy. ««īh: happiness. hurām [л?т] blissful. hu-|-ramag [hwlmk'] having good flocks. ~-rust [-/wst'] well-grown. ---Süzagih [-s’ckyh] agreement. ~-8рӣз [-s5?s] grateful. ^ husraw [hwslwb' | (M hwsrwg), N xusraw] famous, of good керше у m ~ih: fame, good repute. Ms hušk [kwšśk! | = M, N xušk] dry. —-kün [-S TE] impotent. hu-škūh [kwškwh] dignified, splendid. ^h: dignity. hu&nüd(ag) [лото (А)! | M hwinwd, N xusniid] contented, happy. ~th: contentment, happiness. hu-tuxš [kwtwhš] artisan. huwaršt [hwwlst! = Av. hwarfta-] virtue, good deed. hu-xém [hwhym] of good character, good-natured. ^h: good character. hüxt [kwht' = Av. hüxta-] good speech.
549:pazzām- [pz^m-] mature, ripen (intr.). ~išn: maturation, ripening. pazzáménidan [pz’myn-ytn'] = pazzāftan. pēčīdan, pēč- [pyc-ytn' | N ~] twist, entwine. pēm [pym] milk. péménidan, pémén- [5ymyn-ytn'] cause to well up, swell up. pen [p(y)n'] mean, miserly, niggardly. ~ih: meanness. pérámoón [pyPmwn! | M pyrmwn, N ~miin] around, péróz [pylwe | M pyrwz, N ~] victorious. ~th: victory. pérózgar [pylwekl | N ~] victorious. ~ih : victory. pés [pys | N ~] mottled, leprous; leper. pēsīdan, pēs- [pys-yin'] colour, adorn. ~iSn: adornment. pestān [pyst?n' | N ~] breast. pēš [LOYN! < A I-‘yn; руї | = M, N ~] before. IpéSag [py$k! | N péfa] trade, craft; guild, caste. *pēšaģ [pysk'] limb, member, part. pëššánig [pyš”nyk! | N pēšānī] forehead. pēšār [py | M py?r] leader, guide. ~ büdan: be guilty (of), commit. pēšārwār [руло], v. pëšyàr] urination. péSémàl [руѓут?/, v. hamēmāl] plaintiff. ~ih: prosecution, pēšēnīg [pysynyk! | (M pysyn(g), N pésina)] former; foremost, noble. pëš-gāh [pyšg”5 | N ~) audience chamber; foremost seat. pēš-kār [py$k'/ | N ~] servant. pēšēbāy [byš')wp?d | M руйору, N péfwa] leader, vanguard. ~th: leadership. pēš-pāraģ [pyšp*/k! | N —a] an appetizer. pēšyār [pyšk”/ | N ~] urine. petit [pytyt! = Av. paitita-] penance. ~ig [-yk'] penitent. ~igih: penitence. petyárag [p(y)tyd'lk! = Av. paityára- | M pty’r, N patydra] evil, mis- fortune; adversary; astr. detriment, ~th: (onslaught of) evil. рі [AB' < А "bur р(у) | M pyd] father. *pid [5(5)!! | P pyd] meat, flesh. pidar [AB Ytl, v. ipid ; ру | M pydr, N ~] father. pih [pyhw'] food, victuals. pīh [TL BA = A trb; рур | N ~] fat, tallow. pil [py] | M pyl, N ~] elephant; (chess) bishop. --bān [-p’n' | N ~] elephant-driver.
555:rabih [/pyh | M rbyh] noon, midday (heat). rad [/t! | N —] (spiritual) chief, master. АҺ: office of rad. rad [Pu | P rd, N ~] generous, liberal. ~ih: generosity, liberality. radag [itk! | M rdg, N rada] line, rank, row. radómand [/t?^wmnd] having a rad. rad-passag [/tps’k'] ceremonies of the gáhanbar festivals. radunay [/twny = Av. ratunaya-] one under the guidance of a rad. raftan, raw- [SGY TWN-tn! < А V sg’; lwb- | M rptn, rw-, N ~] go, move, proceed. ~išn, v. rawišn. raftār [/pt?] | N ~] goer. rag А! | M rg, N ~] vein. «ЛЬ: disposition, character. ray [/gy | P rg] quick, swift. ray [Pg | N —] meadow, plain. rah [/s, lh, [hy | M rh(y)] chariot, wagon. rah-, у. rastan. rah [Ps | M rh, N ~] road, way. rahag [/hk! | P rhg] = rag. rāh-dār [lsd] | N ~] brigand, highway robber. ~ih: brigandage. rahig [/syk!, Ikyk' | M rhyg, N rahi] child, page. ~ih: childhood. rāh-nimāy [Psnm?d | (M r’-hnmwd’r), № ~numa] guide. ram [Pm | М әт, N ~] peace; cal. 21st day. ram(ag) [/m(k') | P rm, N ram(a)] herd, flock. ráménidan, rāmēn- [Pmyn-ytn! | M ?myn-] give peace, pleasure. rāmišn [P min! | M rmyfn, N rāmi$] peace, ease, pleasure. ~ig [-vk! | N —z#] peaceful, at ease. ran [Рп! | N ~] thigh. P rān- [/^n-] fight. randidan, rand- [/nd-ytn! | N —] scratch, grate, abrade. rang [/ng | M rng, N —] colour, dye. ranj [Inc | P rnj, (M rnz), N ~] toil, trouble. ~ag [-k' | N —a] troubled. ranjénidan, ranjén- [/ncyn-ytn'] trouble.
557:ranjwar [Incwl | (M rnzwr), N ranjūr] troubled, distressed. rapihwin [/pys-, Ipyt-pyn!, -wyn' = Av. rapiüfina-] the afternoon gah; south. ~tar [-tl] southern. rasan [/sn' | N ~] rope. rasénidan, rasén- [/syn-yin'] bring. rasidan, ras- [YHMTWN-tn' < А yhmtwn, V mt^; ls-ytn! | M rs-ydn, N ~] arrive, mature. raspig [Pspyk!] second officiating priest. rast [Pst! | M rst, N ~] true, straight, direct. ~ih: truth, rastaģ [lstk! | N rasta] series, row, progression; element, газап, rah- [Istn', Ї(?)А- | N ~] escape. rastarih [/st?/y%] escape. rasüg [/swk! | (N rāsū)] weasel. Rašn [/@! | M ri, N ~] god of Justice; cal. 18th day. ra&tan, *raz- [/ftn'] colour, dye. raw-, v. raftan. rawag [/wP^k! | N rawá] current. ~ih: currency. rawügenidan, rawagén- [/zob)hyn-ytn!] set in motion, propagate. rawénidan, rawén- [SGYTWNyn-ytn', v. raftan] cause to go, extend. rawišn [lwbin', SGYTWNsn', v. raftan | N rawif] going, motion. ^h : behaviour; as a suffix, forms abstract nouns. ray [Pd | M ry, N ra] postposition, for, for the sake of. rāyēnāģ [Pdym bi | M r’yn’g] arranger. rayénidan, rāyēn- [Pdyn-ytn! | M r'yn-ydn] lead, direct, arrange, organize. ~išn: action, function; arrangement. rāyēnīdārīh [/”*dynyt?lyh | M r!ynyd?ryh] direction, organization, rāyišn [”dsn'] order, arrangement. rāyomand [Pd^wmnd] rich, majestic. raz [/c, lz | N ~] vine; vineyard. raz [Pc | M Pz, N ~] secret, mystery. ~ig [-yk'] secret. rāz-kirrēģ [Pc kylwk' | M г qrwg] architect, builder. razm [/cm | M rzm, N —] battle. —--$àh [-g's | P -g’h, (M rzm?h), N ~] battlefield. razor [lcw] | M rzwr] forest. rédak [lytk' | N ~] lad, page. тёр [/yā! | N ~] sand. rëm [lym | M rym, N —] dirt, filth, purulence. réman [lymn' | M rymn, N ~] dirty, filthy, purulent. ^b : filth. 1r€§ []yf | N ~] wound, sore. *rēš [/yf | N —] beard.
677:zamān [ОЮМА < А ‘dw; gwn’, zmn! | M zmn, N ~] time, hour. ~ag [zm)nk!] = zaman. *zamānīģ [zm”nyk'] prescribed. zāmēnīdan, zāmēn- [p myn-ytn' | M z?myn-] lead, send. zamestān [z7nst?n! | (М dmyst?n), N ~] winter. zamīģ [z-, zmyk! | M zmyg, N zami] earth. ~ig [-yk'] terrestrial, earthly. ---paymānīh [-pim’nyh] geometry. zāmyād [*zmd't! (misreading of z'myzdt! = zām-yazd?) | М myd, N —] cal. 28th day. zan[NYSE < A nth; zn! | = M, N ~] (ĝl. -ān, -in) woman, wife. zan- , —i$n, v. zadan. 1zand [znd | N ~] commentary, explanation, Zend. *zand [zzd | = M] district, tribe. zandag [zndk! | N zanda] rampant. zandbed [zndpt' | M zndbyd] headman of a district, tribe. zandik [zndyk' | N ~] heretic, Manichaean. rmih: heresy. zang [zng] ankle, shank. zangig [zngyk! | N zangi] negro. zanjir [zncyl | (P zyncyhr), N —] chain. zānūg [2”nwk! | P z^nwg, N zānū] knee. zard [21 | N ~] yellow. ~1һ : yellowness. zardaģ [z/tk! | N zarda] (egg) yolk. zardak [zltk! | N ~] safflower. zard|-alüg [zit?hwk! | N ~ü] apricot. ~-tdbag [-cwpk! | N —čēba] turmeric. Zardu(x)&t [zltw(h)st' | (M zrdrwšt), N Zardust] Zaraduštra, Zoroaster. zargon [zlgwn' | P zrgwng, N zaryün] golden, green, fresh. ^ jh: greenness. zarig [zlyk' | M zryg] sorrow, grief. ~6mand [-’wmnd] sad, sorrowful. zarmān [zin?n! | M zrwn-, N ~] old man; old age, decrepitude. ~ih: old age. zarr [ZH BA < А zhb’; DHBA < A dhb | M zr-, N ~] gold. ~én [ZH B Aua. zlyn! | M zryn, N —in] golden. ~(i)gar [zlykl | N ~gar] goldsmith. zarwan [2/wp?n! | P zrw’n] old age. zastan, zāy- [zstn!, z())d-] ask, demand. zaxm [ztm, z?hm | (P jxm), N ~] wound. тау [zyd$ = Av. zaya-] instrument, weapon. ZÁy-, v. zastan. zay-, -išn(-ig), v. zádan. Zāyč(aģ) [z'yc(k') | N zāyča) horoscope. zayistan [2”dstn'] = zastan.
1275:colour (n.) gēūn(ag), rang.
1276:colour (v.) pésidan.
1490:dark tarig/k, térag; ~-coloured dabr.
2121:golden zarrén; (colour) zargón.
=== leaf 5003 context:
xwandan!
kulang kirrdg sett kargās karkēhan kark karm, kirm karmīr karb, kirb karafs karbunag karzang kardār
kardārīh
[121]
Neds >Da
kirbakkarih kirbag, kofag
koftan
kēšīdan
kosk
ku&tan
kardār kardārīh kāntigr
kard
kandan, kardan kardagān kardagār *kardag, kūdak kardespās
ahy!
dandàn!
karr, -gat.
```


## [2026-09-05T20:54:35.914Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -no \"nigūn[^ ]* \\[[^]]*\\][^.]*\\.\\|kōšk[^ ]* \\[[^]]*\\][^.]*\\.\\|k6šk[^ ]*\\|kōšk\" PHD.txt | head -20; echo \"===\"; grep -no \"kwšk\\|kwsk\\|kōšk\" PHD_mackenzie.txt | head -10"
}
```


### [2026-09-05T20:54:35.975Z] TOOL RESULT

```
===
```


## [2026-09-05T20:54:38.728Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"kosk\\|k5sk\\|kôsk\\|palace, pavilion\\|pavilion\" PHD.txt PHD_mackenzie.txt | head -20; echo \"=== nigun\"; grep -n \"nigūn\\|nigun\\|nykwn\" PHD.txt | head -10"
}
```


### [2026-09-05T20:54:38.787Z] TOOL RESULT

```
PHD.txt:428:kem [kym] less, fewer; v. kam. кёп [kyn' | = M, N kīn(a)] hate, malice, revenge. ~ig [-yR'] malicious, vengeful. kennār [Rl] lyre, harp. ~-sray [-sPd] harpist. kénwar [kynwl | (M kynw’r), N kinawar] vengeful, vindictive. ««īh: vindictiveness. kër [kyl | N ~] penis. kēsar [kysl] Caesar. këš [kyš | = M, N ~] dogma, faith (especially non-Mazdean). ~-dar [-d’/] sectary, non-Mazdean. keSidan, keš- [k(y)$-ytn! | (M kr$-), N kafidan] pull, draw. Kēwān [kyw’n! | Ar. kaywān] astr. Saturn. kēwūd [kypwt! | M R'ywd] box, ark. kilēl [R]yl | N ktlīd)] key. kirb [klp | M kyrb] body, form. kirbag [krpk' | M kyrbg, N Аја] virtue, good deed. ~ig [-y%!] virtuous, pious. kirbakkar [krpkkl | M kyrbkr] beneficent. ~ih: beneficence. kirih- [OBYDWNyh-, v. kardan, kiyh- | M kyryh-] be done, made. kirm [kim | M krm, N —] worm, serpent. kirrénidan, kirrén- [klyn-ytn'] rend; create (daevic). kirróg [k(y)lwk! | M grwg] artisan, craftsman; skilled. ~th: arts, crafts, craftsmanship, skill. kiš [k(y)š | M АЎ, N ~] furrow, line. kišnīz [kšnyc] = gi$niz. kištan, kar- [ZL Y TWN-tn! < А У ar; kyštn!, Pl- | M kyšt, kis- N ~] till, furrow; sow. kištār [ZLY TW NTt'l] tillage. kišw, ~4n [kysw', x! | P Аун] tillage. ~(an)zar [-c?/ | (N kištzār)] field. ki$war [Rystol | M kyswr, N ~] region, clime, continent. kišwzār, v. kišwānzār. kūb-, v. koftan. kódak [kxwtk! | M gwdk, N ~] young, small; baby. kof [kwp | = M, N koh] hill, mountain; hump. ~ag [-4! | N Абла] saddle. ~ig [-yk! | N kēkī] wild, mountain-. koftan, kūb- [kwp-tn' | N ~] beat, pound, crush. kör [kwl | M kar, N ~] blind. ~-dil [-dyl | M -dyl, N ~] blind-hearted, incorrigible. kūstan [kwstn' | = M, N ~] beat, pound. kūš-, v. kóx&-. kēšk [how fA! | N ~] pavilion, palace, kiosk.
PHD.txt:462:2mašk [mšk! | N maškē] tent, pavilion. ~abarzén [-!pizyn! | M mškbrzyn] royal pavilion.
PHD.txt:3059:pavilion kēšk, mašk; royal ~ mašk- abarzēn.
PHD.txt:5003:kosk
PHD_mackenzie.txt:3333:ko§k [l?7Vfk' I N --] pavilion, palace, kiosk.
PHD_mackenzie.txt:3502:2mask [msk I N mafhO] tent, pavilion.
PHD_mackenzie.txt:3504: ........abarzen [-'p[zyn l I M mfkbrzyn] royal pavilion.
PHD_mackenzie.txt:6925:iris herig.                                kiosk kosk.
PHD_mackenzie.txt:7213:oval xayagdes.                         pavilion kosk, mask; ro:)'ol ...., mask-
=== nigun
1687:downwards nigūnsār.
```


## [2026-09-05T20:54:45.048Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"nigūn\\|nigōn\\|nigun\\|nikun\\|prone\\|upside\" PHD.txt | head -10"
}
```


### [2026-09-05T20:54:45.110Z] TOOL RESULT

```
321:ë ру | (M hyb)] particle giving the present tense optative sense. é, v, éd, éw. ēbāraģ [*dyp'lk', ^dwlk! | N éwàr] evening. ébgat(ih) ['ybgt!, -yh = Av. aifi.gati-] (onslaught of) Evil; the Adver- sary. ēbsrūsrim [>ур-, ?ybslwslym = Av. atBisrūdrima-) the gah from sunset to midnight. ébyünghan [>ур-, ?ywby?nghn!, etc. = Av. aiBydshana-] sacred girdle, = kustig. ёё Pye | (P ?ушус), N héc] (with a negative) not any. ēčand, v. éw-Cand. éd (HN A < A hr? | M? yd] this; v. dāštan. ~ ray ёё [cf. N z-é-rá] because, since. édar [LTME < À I-tnh | M?ydr, N ~] here. édin [ytwn'! | N ēdūn] thus, so. ~ih: (correct) manner. ëg [ADYN' < А *dyn | М ?yg] then, thereupon. ëk Pywk' | M yk, N yak] one. ëkanag [Pywk’nk! | N yagana) submissive, obedient. ^h : submission, obedience. ēk-dād [ywkd’t'] sole-created. ēmēd [*dmyt'] hope. ēn [ZNE < A znh | M *yn, N in] this. -ën [-yz! | = M, N -in] suffix forming adjectives of material or quality. -endag [-ndk! | M -yndg, N -anda] suffix forming present participles. -én-idan [-yn-ytn' | M -yn-ydn, (N -àn-)] suffixes forming causative and transitive denominative verbs. *énókén Pynw(k)kyn' = Av. *aēnē.kaēnā-) heiress (under the obligation of continuing her father's line). enya рулу | (M ?n’y)] otherwise, moreover. lër [d] | M Zur, v. azér] down, below; low; under. — ud abar: upside down. tēr Pyl] noble; hero, ~ih: nobility, good conduct. Eran [y”x! | N ~] Eran, (land of) the Aryans. ~ag [-k'] an Eranian, Aryan. érang [”y/ng] blame, condemnation; error, heresy. ~ih: = érang. éranj-, v.  * éraxtan. Ērān|-šahr (yPnitr! | N ~] land of the Aryans. —-wëz [-wyc] (original) home of the Aryans. 1ёгахќап, ёгапј- Pylhtn!, ?уЇпс- | J ?yrxt] blame, condemn, damn.
512:nest [LOY T! < А P?yty | M nyst, N ~] is not. ~ih : non-existence. néw [TB < A tb; nyw' | = M, N —] good, brave. ~-ardaxSir [nyw lthsyl | N nard !] backgammon. nézag [nyck! | N néza] lance. nēzūmān, —16 [nycwmn', -yk! | M nyzwm!n] dextrous, skilful. -~th: skill, artistry. nibard [nplt' | N nabard] fight, struggle, battle. ~ag [-k! | N ~a] tried, experienced. nibardīdan, nibard- [npit-ytn! | P nbrd'd] fight, do battle. nibastan, nibay- [SK BHWN-tn! < A У hb; npstn', npd- | M nbst] lie down, sleep. nibāstan, *nibày- [np'stn! | M nb’st, nb y-] lay down. nibég [npyk! | N niwé] writing, scripture, book. nibém [npdm | (P nbdm-)] lying, prostrate. nibištan, nibés- [VK TY BWN-stn! < A yktbwn, У КЬ; npstn' | M nbyšt, nbys-, N —] write. nidan, nay- [YD(B)LWN-tn! < A ydbrwn, V dbr | M nyydn, ny-] lead. nidom [nytwm] least, smallest. nifridag [nplytk' | N nifrid] accursed. nifrin [nplyn' | N <] curse. nigah [nk’s | M пол, N ~] look, attention. ~ dāštan: watch, keep. — kardan: look. ~-darih, —-dári&nih [-d?/(sn)yh | N —dārī] keeping, care. nigān [nk’n' | P ng’n] buried. nigar- [nk’l- | M ng’r-, N ~] draw, design, paint. ~ag [-h! | (M agin, N nigār)] image, picture, diagram. nigástar [nk?s I] guard; protective. nigeridan, niger- [nkyl-ytn! | N nigaridan] look, observe. --išn: observation. ~iSnig : evident, manifest. nigéxtan, nigéz- [nkyhtn!, nkyc-] expound. ~i$n: exposition. nigéz [nkyc] exposition. nigün [nkwn! | N ~] inverted, upside down. ~th: depth, downward direction. ~sar [-s?l | М ngwns’r] downwards. nihadag [nyd’tk' | M ny? dg] foundation. nihādan, nih- [TNH TWN-tn! < А hnht, ~ nht | M пуа, nyh-, N ~] put, place, establish. nihal [nbl | N ~] sapling, self-planted tree. nihān [nyh’n' | N ~] concealment, secrecy. ~ig [-yk! | N ~7] secret. nihang [nsng] small, few.
1687:downwards nigūnsār.
4173:upside down ér ud abar, nigün.
```


## [2026-09-05T20:54:45.450Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== SOD gwn\"; grep -n \"gwn'k\\|gwn\\`k\\|gwnk\" SOD.txt SOD_pages.txt | head -20"
}
```


### [2026-09-05T20:54:47.126Z] TOOL RESULT

```
== SOD gwn
```


## [2026-09-05T20:54:52.664Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"γwn\\|gwn\" SOD_pages.txt | head -30; echo \"===sizes\"; wc -l SOD.txt SOD_pages.txt"
}
```


### [2026-09-05T20:54:52.732Z] TOOL RESULT

```
7414:      opyund   ©<*apa-gunda-, Parth. >bgwnd\ Khwar.                  Benv. VJ n p90.8, >pksy\ VJ 8-, GMS       161A; >pksy,
15921:                                                                    yasn ©<IE *gwndhsmo ©nom. -(>)y; ace. -w; pi.
27465:                                                                  pos-yone    ©Parth. psgwn}w ©pi. -t
===sizes
 111423 SOD.txt
  45615 SOD_pages.txt
 157038 total
```


## [2026-09-05T20:54:56.557Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"\\bhair\\b\" SOD_pages.txt | head -30"
}
```


### [2026-09-05T20:54:56.608Z] TOOL RESULT

```
16224:           consolation                                                    hair
16247:     hair pore                   -               ^C'J>"        TSP 2.1161 n pi 84; S W, BSOAS 1983, 42,
16772:     hair
19267:                                                                            twisted locks, curly hair
26251:      0<9)pull out(hair)                                            TSP 2.356, 774, 3.276, 289, 14.5, 19.9, 8.177; SCE;
33124:      OcObelieve, (/cOhave faith                                    hair
33135:                                                                    hair
36961:       (ro)raise                                                      hair
37170:11498 zwst- C =» zywst-, ,zw,st-                                             hair pore
37960:(to)creep     10875                      curly hair      5443
38417: gratitude     1283, 7205                       hair 4383, 4559, 10177, 10178,            (^)haste 6421, 6787
38421: gravel   9397                                  hair pore 4386,11509                      hastily 9030
38438:       n  i s h -hair
39193: (to)pu\\ out(hair)   7809               quick    4576, 11256, 11257               1083, 1084, 6683, 6859, 7226,
```


## [2026-09-05T20:55:00.424Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '16210,16260p' SOD_pages.txt; echo \"=== 16760-16790\"; sed -n '16760,16790p' SOD_pages.txt"
}
```


### [2026-09-05T20:55:00.485Z] TOOL RESULT

```
      4368 YwSnyk       S                          o-^'cr^J*'
            xutanik, xu8anik                                              xonax (ywn'x, ywny, ywnx) ©demons, pron.
            Khotanese                                                       art. nom. sg. m. =>xwnx
                                                                          that, he
            GMS 976; Sogdica. p8-l0.11c                                   VJ; SCE; TSP; BSTBL; YwnYw, Frag. 11.2; TSP;
      4369 Ywdy     C «* Yw5>k(h)                                           GMS 1410 n pi; VJ 1509
      4370 Ywkt     B                                      >ff       4382 ywn'k1 B, S                             y.jT
III         Yokot (ywqtt) ©<*gaukrta                                      xone, xonaku (ywn'kw) ©demons, pron. art. sg,
            sulphur                                                         m. =>xwn}k, xwny
            GMS 76, 148; TSP 3.226, 229; Hen. BSOAS                       that, he
             11.69.38 "brimstone"                                         GMS 1402, 1405, 1411; VJ 1232; TSP 12.18; MDii
      4371 Ywqtt M =* ywkt                                           4383 ywnV B                                      ^
      4372 YwmV B                                  jJLs t^*^              yone    (ywn'yy, ywn*y)   ©<Av. gaona      ^ywn'k
           xumar ©<Av. vohu~mq$ra         4xwm'r
           consolation                                                    hair
           TSP 8.201-, VJ 1115; GMS 391; Frag. Len. 39.4                    Pwn>kh
                                                                          Bailey. Prolexis. 74; EGSii 90; TSP 2.296 n pl73;
      4373 Ywmr     C                                   <**>*<>_*           Ywn'y, Hen. BSOAS 11, 718; Ywn*y. SCE 302



i
4384 ywnV     B                                ^<^              SCE 318, 502

      xune, xwane =»ywny, ywn-1, xw'n2                    4397 ywdy     B =± yvsrfy
      proclamation, news
      Ywn>kwy VJ 75, 89                                   4398 ywny(w) «> Ywn?
                                                          4399 Ywnnc C                                            *xJ>l
4385 -ywn'k B                      (u,>-)jujU ««jf              increasing
                                                                yunanc  ? ©*Ywnny        ©f. adj. =$yv/n-7
     yonc (-ywny) ©<*gaunaka ©as suff. in
       compd. ^'nywn^, wvywnc, cYwny,                           BSTii 895.25: C2, 54R25
        wyspYwn}y                                         4400 ywnpyk      B                                        of
      like, similar to                                         foam
      GMS 1113, 1114; TSP 211.9; VJ 239                         STii 8.4; Bcnv. TSP n pl84, 1161
4386 Ywn'k pwn'kh B                                       4401 Ywnpr,yck) B                                         ^jf
     Yone- Pune ? =»Ywn)k\ Pwn}kh                              foam
     hair pore                   -               ^C'J>"        TSP 2.1161 n pi 84; S W, BSOAS 1983, 42,
     TSP 2.296, ob. pi. >yr, 373
4387 Ywnlkw => yw^k1                                             Ywzpryycky
                                                          4402 Y>vntJk  B                          (a-U^)JJ?j <0_^X^
4388 ywn'nk S                              Kjo* 'Ky>^*-        Yonde, Yondak ?
     xunanc/k (yw'nk) ©adj. ^»Ywn3                             poison spider, tarantula
     (related to)Huns                                          TSP 3.84, 6.9 n pl94
     F. Grenct. SI cahicr 7, 1984, 167, 184               4403 Ywnty C                                       jU >jy tffi
4389 ywn'x =» Ywn>Y                                             Ywande, Yundc =»yw~
                                                                necessary
4390 YwnJy B                                       jif
     xwane, xune                                               STi 38.5; GMS 1068; CII, 1990 F14
     crying
     TSP 2.911 n pl80f; Hen. Texts. 723                   4404 Ywnx *=» Ywn>Y» xwnx
=== 16760-16790
     debauched, licentious
     BSTBL, Dhu. 82                                                4567 j'r M                                                   >j
                                                                        zar ©<*jan&ra\ A v. jq$ra\ Parth. zahn MP
4557 Yztwq C                                  jj±~ <cM* ^1
     xazt/duk ©MP xayug                                                   zahr ©ob. -yy     ^z'r2, z*r
     saliva
                                                                        BBB b36 b85; GMS 1058; Gersh. TPS 1964, 14 n
     STii L25; GMS 978; Hen. Texts. 719                                 poison
                                                                          1; pryy, BBB 639; Hen. Cosm. 311.67
4558 yzw     C => y?w*                                             4568 j'rm'nwq M                             xfoyj
4559 yzw*' B                                              ^             zar-manuk ^z'r^r'k
     y(u)zu/wa ? (yzw) ©f. n. =»zw, zw-                                 poison-like (similar to poison)
     hair
                                                                        Gersh. Sogd. Cpds. 143b; BBB b36; GMS 1058
 183                                                                                                              jn'ptnym


 4569 j'rnyy M                                   jb^Aj ttfjAj          hard, cruel
      zarne                                                            BBB 510, Hen. Tales. 473.28; BSOAS 11, 66.9;
        poisonous                                                        GMS 410n 1
        BBB b36
                                                                 4580 jyyr-   M                               q*j\x* < jxl^-
 4570 j^rynyh       M                            J*y>j <i$j*j
                                                                       zyer   Ojyyr-) ©impf. jyYyr =^zy>yr-, zyyr-,
                                                                         >Zy)yr„
      zarene
        poisonous
        GMS 1058                                                      (/o)call
                                                                      GMS 629, 706, 730-, W-Li; Cropp. p39
4571 j>y- M                                i>jo^ ^ i            4581 jyyrt- M                         j-^o/i tdxiy-
     zay ©<*dray-\ MP dray                                           zyert ©pt. st.
```


## [2026-09-05T20:55:09.684Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=16050 && NR<=16260 && /^ *[0-9]{2,3} *$/ {print NR\": \"$0}' SOD_pages.txt; echo \"---pdfpage tags:\"; awk 'NR>=16100 && NR<=16300 && /pdf page/ {print NR\": \"$0}' SOD_pages.txt"
}
```


### [2026-09-05T20:55:11.677Z] TOOL RESULT

```
---pdfpage tags:
```


## [2026-09-05T20:55:15.232Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=15800 && NR<=16400 && /^[[:space:]]*1[0-9][0-9][[:space:]]*$/ {print NR\": [\"$0\"]\"}' SOD_pages.txt | head; echo \"== any short numeric lines\"; awk 'NR>=15900 && NR<=16350 {gsub(/^ +| +$/,\"\"); if ($0 ~ /^[0-9]{3}$/) print NR\": \"$0}' SOD_pages.txt"
}
```


### [2026-09-05T20:55:16.913Z] TOOL RESULT

```
15870: [                                                                                                                       170]
16019: [                                                                                                                      172]
16093: [ 173]
16160: [                                                                                                                            174]
16293: [                                                                                                                          176]
16358: [ 177]
== any short numeric lines
16019: 172
16093: 173
16160: 174
```


## [2026-09-05T20:55:30.510Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('SYN.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint('leaves',len(pages))\n# leaf = printed + 24\nfor p in (1051,1052):\n    i=p+24\n    print('==== printed',p,'leaf',i)\n    print(pages[i][:1800])\nEOF"
}
```


### [2026-09-05T20:55:32.163Z] TOOL RESULT

```
leaves 1545
==== printed 1051 leaf 1075
k., | and Du. vandaag with van ‘from, of”. Balto-Slavic, and a part of the Gmc. Du. heden, MDu. héden, beside ! forms. hude(n), OS hiudu, OHG hiutu, MHG s 4 1. Grk. Ion. ojpepov, Dor. capepov | hiute, NHG heute, fr. *hiu-tagu ‘on this (Att. riuepov rare), NG pop. oxuepa, fr. day’, cpd. with pron, stem in Goth. t A *xduepov, fr. auépa ‘day’ and pron. stem himma, etc. (above). Weigand-H. ( F *ki-, *ky-. Walde-P. 1.452f. Boisacq | 1.860, Franck—v. W. 237.
861.
2. Lat. hodié (> It. oggi, Sp. hoy, OFr. hui, Fr. epd. aujourd'hui), fr. *ho- dié : Skt. a-dya ‘today’, or with vowel shortening fr. abl.-loc. *hd dig? Ernout- M. 456. Walde-H. 1.653f. REW 4163.
Rum. astdzi (shortened azt), fr. astdé zi ‘this day’. Tiktin 114,
3. Ir. indiu, W. heddyw, Br. hizio,
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
5. Lith. Sandien, Lett. suodien, fr. forms of Ss ‘this’ and diena ‘day’.
6. ChSI. dinist, etc., general Slavic fr. dint and pron. si ‘this’ (reformed Russ. sego-dnja adv. gen.). Berneker 253. Briickner 113.
7. Skt. adya, adya, cpd. of pron. stem a- (in a-sdu ‘that’) and dy& : dydus, Lat. diés, etc. ‘day’. Walde-P. 1.98.
Most of the expressions for ‘tomor- row’ ate derived from words for ‘morn- ing’ (14.44), the semantic development being ‘in the morning’ = ‘on the follow- ing morning’, whence with extension to the entire day ‘tomorrow’.
1. Grk. atpiov, fr. *abopror : Lith. nigra ‘dawn’, etc. (14.43). Walde-P. 197. Schwyzer, Gr. Gram. 1.282.
9, Lat. crds, etym.? Ernout-M. 227 Walde-H. 1.285.
It. domani, Fr. demain fr. VLat. démane, phrase cpd. of mdne ‘morning’ (>Rum. miine ‘tomorrow’). REW 2048, 5294.
Sp. maftiana = manana ‘morning’.
3, Ir. imbarach, NIr. i mbaireach, W. wfory : W. bore ‘morning’ (14.44). Peder- Sen 1,99,
Be arc’hoaz (also warc’hoaz, cpd. with Fa on’
==== printed 1052 leaf 1076
 beside adv. dat. in OHG mor- gane, MHG morgen(e), NHG, Du. mor- gen. Weigand-H. 2.219. Franck-v. W. 422f. NED s.v. tomorrow.
Goth. gistradagis (adv. gen.) : OE geostra-deg, etc. ‘yesterday’ (14.49), renders atpuv Mt. 6.30, with puzzling shift of meaning if not merely a blunder in translating. Cf. Brugmann, op. cit. p. 15.
5. Lith. ryto(j), Lett. rit, ritu, ria, orig. ‘in the morning’, fr. Lith. rytas, Lett. rits ‘morning’.
6. ChSI. uéré loc. sing. (renders reg. atpiov in Gospels), also phrase za utra (but in Gospels only ‘early in the morn- ing, tpwt’), similarly SCr. sjutra, Boh. zejtra, Russ. zavira, but Pol. simply jutro (acc. as. adv.), all fr. ChSl. utro, etc. ‘morning’. Berneker 462.
7. Skt. cvas: Av. sir- ‘morning’. Walde-P. 1.368. Walde-H. 1.285. Brug-
mann, op. cit., p. 17.
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
SELECTED INDO-EUROPEAN SYNONYMS
14.49 YESTERDAY
Grk. —_xés, Ex0és Goth. . Lith. vakar NG xrés, éxrés, Wes ON i g@r Lett. vakar Lat. —heri Dan. 7 gaar ChSl.  v%%era It. teri Sw. t gdr SCr.  juéer Fr. hier Or geostran dag Boh.  véera Sp. ayer ME __yister(n)day Pol. wezoraj Rum. tert NE yesterday Russ. véera Ir. indhé Du. gisteren Skt. hyas Nir. indé, iné OHG - gesteron Av. te W. doe MHG gester(n)
Br. dec’h NHG gestern
Most of the words for ‘yesterday’ be- long to an inherited group, pointing clearly to an IE adv. of this meaning. The others (the Balto-Slavic, and pop. NG) meant orig. ‘in the evening’ or ‘ate’, whence ‘in the past evening’, and with extension to the entire day ‘yester- day’. Cf. the parallel but forward shift in the history of words for ‘tomorrow’ (14.48).
1. IE *hes, etc. (variant init. com- binations). Walde-P. 1.664. Ernout- M. 449. Walde-H. 1.642f. Falk-Torp
```


## [2026-09-05T20:55:40.220Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"gaona\" SYN.txt | head -10; echo \"=== check offset\"; python3 - <<'EOF'\nt=open('SYN.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint(repr(pages[26][:200]))\nEOF"
}
```


### [2026-09-05T20:55:42.091Z] TOOL RESULT

```
5376:414 HAIR tly distinguished as a) of the Head, b) of the Body, of Animals) ar s (P PEO) Goth. tagl, skuft (a) ae poe Sate (b) oplt, pi. Pixs) ON har, skopt (a) ett. mats, spalva (b) Gr year pexes 187 a ChSl. last NG 70lxe FE ) Dan. haar padded a ), erimis Sw. hdr SCr.  vlas, kosa (a), dlaka Lat. capillus , (a), Bi- OE har, feax (a) OF ie : ME here, fax (a) Boh we oak (a), pelo (b) NE hair ae wi i ae ae (a), poi Du. =—haar uss. volos _ _ chevett ‘ Ma (a) OHG shar, fahs (a) Skt. _ keca- (a), roman- (b) anne piel} cave MHG har, vahs (a) Av. varasa- (2), gaona- (b) Rum. NHG _ haar
5400:Lith. gauras, mostly pl. gaurai ‘hair on the body, tuft of hair’ : Lett. gauri ‘hair on private parts’, NIr. guaire ‘rough hair, bristle’, Norw. kaur ‘lamb’s wool’, also with different suffix Ay. gaona- ‘hair’, root *geu-, perh. the same as in Grk. yipés ‘round, curved’, etc, Walde-P. 1.557.
5407:Av. gaona- (b, also ‘color’, NPers. gin ‘color’) : Lith. gauras, above, 5.
18971:5. Lith. gauti, Lett. gat, gaut (Lett. mostly ‘catch, try to get’, but locally ‘get’) : Av. gunaoiti ‘promotes’, gaona- ‘profit’. Miihl.-Endz. 1.687. Walde-P. 1.637.
26592:15.61 COLOR (sb.) Grk. xpGya Goth. .. Lith.  spalva NG Xpapa. ON litr Lett. krasa Lat. color Dan. farve (Id) Ch&l. nat. It. colore Sw. jarg SCr.  boja Fr. couleur OE bleo(h), hiew Boh. _barva Sp. color . ME colour, ble, hew Pol. —_farba, kolor, barwa Rum. coloare, fafa NE color (hue) Russ. cvet Ir. dath, li Du. kleur, verf Skt. varna-, ranga-, raga- Nir. .dath, li OHG farawa Av. gaona- W. lliw MHG zarwe Br. liv NHG farbe
26626:Av. gaona- ‘hair’, also ‘color’ (Yt. 8.58; cf. Afgh. yuna ‘hair, color’, NPers. gin ‘color’) : Lith. gaurai ‘hair’, etc. (4.14). Walde-P. 1.557. Barth. 482.
=== check offset
'opean\nlyr. Illyrian\nTon. Tonic\nTr. Trish (Old and/or Middle, only occasionally distinguished as Olr, MIr)\nTran Iranian\nIt. Italian\nLac. Laconian\nLat. Latin\nLesb. Lesbian\nLett. Lettic\nLG Low German\nLit'
```


## [2026-09-05T20:55:47.542Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('SYN.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n'); leaf=0; m={}\nfor i,l in enumerate(lines,1):\n    m[i]=leaf; leaf+=l.count('\\f')\nfor ln in (5376,5400,5407,26592,26626):\n    print(ln,'leaf',m[ln],'printed',m[ln]-24)\nEOF"
}
```


### [2026-09-05T20:55:49.172Z] TOOL RESULT

```
5376 leaf 238 printed 214
5400 leaf 240 printed 216
5407 leaf 240 printed 216
26592 leaf 1129 printed 1105
26626 leaf 1131 printed 1107
```


## [2026-09-05T20:56:00.483Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"gaona\\|gōn\\|gon\\b\\|gwn\" SNS.txt | head -20; echo \"=== pages file\"; grep -n \"gaona\\|gwn\" SNS_pages.txt | head -20"
}
```


### [2026-09-05T20:56:00.546Z] TOOL RESULT

```
4663:: j^/i (Aitffc. 1774)hamO-gaona-/hama-gaona- : b* 
4665:.(ij±)~*) ham-guna: y {Mir. Man. II, 56) hamgwng 
6365:!«»». 211) gaona- . h ^ :0 9° n /ang0n: « 
6770:haraMn :L UiWb. 1776) ?hamG.gaona-: £. 
10044:.^, OJ S:gaona + UiWfc. 584) .^:Sis . bJ— 
10728:• o****- : sahmgen/ sahmgon W .#->-> 
11217:. cLl^ -«U* . oA- •• "argon : **>*• 
11219:*/*><*«»«*• = sargon adurxstar: V 
18494:\%/X4 {AiWb. AQ3) %unaz tflxl gaona- : L* 
29028:sairi-gaona- 187/4 
29111:hama-gaona- 54/16 
29113:harao-gaona 54/16-90/7 
29743:gaona- 338/21 
30378:hmgwng 54/16 
32819:gon 338/20 
32897:edon cegon 87/11 
=== pages file
2971:                                                                                                                    :   j^/i (Aitffc.   1774)hamO-gaona-/hama-gaona-                              :   b*
2975:     «*»A __j L            *l»       *iV*<"i^lb(^=) j .:5                   f       HN   :>*                      .(ij±)~*)   ham-guna: y {Mir. Man.                        II,       56)    hamgwng
4064:                                                                                                 !«»». 211) gaona-
4323:     'ywp       (wjj&jrj)'isU^StfA*                                      l*<*.       Wan.      II, 45)         I               haraMn :L UiWb. 1776) ?hamG.gaona-:
6775:             .^, OJS:gaona + UiWfc. 584)
13333:                                                                                                                                                                                AQ3) %unaz tflxl gaona-
15096:vi taxti- 267/21         saracfa- 174/8-183/11             saiti- 196/12            hama-gaona- 54/16
15098:vi-da5vS-data- 285/13    sastar- 174/2                                              harao-gaona 54/16-90/7
15116:sairi-gaona- 187/4       sraota- 184/20                    ha-nuharana 89/7         hu 29/12
15311:                                                              xsnSvayeiti 202/7        gaona- 338/21
15518:                                                                              hmgwng 54/16
```


## [2026-09-05T20:56:08.786Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '4310,4340p' SNS_pages.txt | cut -c1-250; echo \"=== page tags nearby:\"; awk 'NR>=4200 && NR<=4400 && /pdf page/ {print NR\": \"$0}' SNS_pages.txt; echo \"=== 6355-6375 SNS.txt\"; sed -n '6355,6375p' SNS.txt | cut -c1-250"
}
```


### [2026-09-05T20:56:10.424Z] TOOL RESULT

```
                                                          .^j^.jLS,: gvbar:                         ^y^                                  (A/ir.    Win.
      nv-nf/t ^                 (^    *   ,
                                              j
                                                  ,
                                                      ^      :   ^)"iJ, ^ :b5r+ ^ 5v
                                                                                                                                   •
                                                                                                                                                                II,     53> J lto.l.jlAjS wrWy5nSif5 fi
                                                                                                                                                                        •a/a^       .fj^.^; garSSt:^
                                                                                                                                       6/6^ .oii jlj^l.jjjfc : n g virravSd:YHrtv^_Js
                                                                                         l*:   ayab:      o^
     Yb :^fc(i4ttfb. 136-1310) va                                           :    ^tS^- vaj' t-                                                        •   </*«*•»         :    hamOggn/hamOySh: v'4?^
     'ywp       (wjj&jrj)'isU^StfA*                                      l*<*.       Wan.      II, 45)         I               haraMn :L UiWb. 1776) ?hamG.gaona-:
                                                                                                                                                                   £.
                                ./^AT^A-T-T/l* 5 .(*s>,~*) ayS :V                                                      4. Pagliavo, Jackson Memorial
                                                                                                                                                                                             !&*3WtfU)
                                                                                                               I




                                                                                                                         ^^c-'^^a.tal;^^                                 VoZame. pp. 140-48)




                                                             .^ei-^i .o^J        1
                                                                                     :   Svtum:         -*V               ^tUM, I64)aiva-: ^                                       4iJ/fc.22)aSva-     ;   fc.

                                                      *-•*'<• a-**' uJ-0* iU * : tum+fiv                                 yak           S6«tt^c«^i
=== page tags nearby:
=== 6355-6375 SNS.txt



'^•^:angOSl<Ug: JltMui 
K**. Jfe». H,46) >ngvsydg:^ 

VA* { tvotri ;i ^.j 



!«»». 211) gaona- . h ^ :0 9° n /ang0n: « 

'" (WlJ --^n. II, 43, »„„ tj3b 



: *- ■«*•,**. gOn +o T:an/0 
I, 43) », 

>^u= 0g0n hum3n5g ^/^^ ^
```


## [2026-09-05T20:56:17.887Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"kiosk\" KLN_1966.txt KLN_1971.txt SKT.txt LKT.txt DEV.txt PHN.txt | head -20"
}
```


### [2026-09-05T20:56:17.947Z] TOOL RESULT

```
LKT.txt:1789:'Winkel,  Ecke'  [Horn  NpEt S.  211, Nr.  945], tk.  zu  kjosk,  kjöSk  Talast,  Villa,  Pavillon' geworden;  hieraus  bulg.  kosk  'Garten- haus', serb.  cosak  'Söller',  poln.  kiosk, russ.  kiosk;  it.  chiosco,  frz.  kiosque,  sp. Jciosco,  rum.  chiosc  'Verkaufsbude', c/t/oscar 'Zeitungsverkäufer';  dtsch. iiiosÄ;, ndl.  engl,  kiosk  'dass.'.  Die  pers.  Form zeigen  noch  bulg.  kose,  kuse  'Winkel', serb.  cose  'dass.'.  [Devic  DEt  149.  Bern SlEtWb  680.
KLN_1971.txt:131490:kiosk, also kiosque, n>, an open pavilion or sum- 
KLN_1966.txt:20716:kinoplasm,  n.,  the  active  element  of  protoplasm. —  Compounded  of  kino-  and  Gk.  7rXaa(xa, ‘something  molded’.  See  -plasm, kiosk,  also  kiosque,  n.,  an  open  pavilion  or  sum¬ merhouse;  an  open  building  used  as  a  news¬ stand.  —  F.  kiosque,  fr.  Turk,  kidshk,  ‘pavilion’, fr.  Pers.  kushk,  ‘palace’, kip,  n.,  the  hide  of  a  calf  or  another  young  beast. —  Of  uncertain  origin.
```


## [2026-09-05T20:56:18.782Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"zircon\\|jargon\" AHD_watkins1985.txt KLN_1966.txt LKT.txt DEV.txt | head -20"
}
```


### [2026-09-05T20:56:18.835Z] TOOL RESULT

```
DEV.txt:347:/j6.   Sericon,  siricon,  minium.  (Voy.  au  mot  Jargon.)
DEV.txt:1555:Jargon.  Gemme  de  couleur  jaune  tirant  sur  le  rouge, souvent  confondue  avec  VhyacintJie.  Le  minéralogiste  Haûy a  réuni  ces  deux  sortes  de  pierres  sous  le  nom  commun de  zircon.  Ital.  giargone.  Jargon  et  zircon,  dont  personne, à  ma  connaissance,  n'a  encore  établi  l'étvmoloffie,  sont certainement  identiques  à  l'espagnol  azarcon.  D'après  le Dictionnaire  de  l'Académie  espagnole,  azarcon,  en  pein- ture, signifie  orangé  vif  :  ^e\  color  naranjado  muy  encen- dido,  color  aureus;v  ce  qui  s'applique  très-exactement  à l'hyacinthe.  Azarcon  s'est  dit  aussi,  comme  le  portugais zarcâo,  zarquào,  azarcâo,  de  l'ocre  rouge.  Et  tous  ces  mots correspondent  à  un  terme  arabe,  ij^)';)  zarqoûn,  avec  l'ar- ticle az-zarqoûn,  qui  se  disait  du  minium  et  d'autres  sub-
DEV.txt:1560:Dans  tous  les  cas,  noive jargon  me  paraît  venir  de  cette expression  persane  qui  définit  très-exactement  la  couleur de  la  gemme.  N'oublions  pas  que  celle-ci  est  originaire de  Ceyian,  de  l'Inde  et  du  Pégu.
DEV.txt:2893:Azane,  voy.  Alchimie,  28. Azar,  hisp.  voy.  Hasard. Azarcâo,  pg.  voy.  Jargon. Azarcon,  esp.  voy.  Jargon. Azardum,  b.  lat.  voy.  Hasard. Azarnefe,  esp.  voy.  Alchimie,  99. Azarnet,  voy.  Alchimie,  29. Azarole,  voy.  Azerolle. Azarolla,  esp.  voy.  Azerolle. Azarrum,  b.  lat.  voy.  Hasard. Azarum,  b.  lat.  voy.  Hasard. Azazeze,  voy.  Alchimie,  3o. Azebibe,  esp.  voy.  Jubis. Azebit,  voy.  Jubis.   . Azebre,  pg.  voy.  Azerbe. Azeche,  pg.  voy.  Alchimie,  3i.
DEV.txt:2919:Azuric,  voy.  Jargon.
DEV.txt:3690:Jargon.
DEV.txt:4318:Sil,  voy.  Jargon.
DEV.txt:4325:Sirucum,  lat.  voy.  Jargon.
DEV.txt:4341:Sory,  voy.  Jargon,
DEV.txt:4376:Suradain,  voy.  Astronomie,  .'^8. I!.vpi}c6v,  voy.  Jargon. Surrapa ,  p^''.  voy.  Sirop. Surmeh,  voy.  Alcool,  note  a. Syricum ,  lat.  voy.  .largon. Syrupus,  b.  lat.  voy.  Sirop.
DEV.txt:4484:Zarcào,  pg.  voy.  Jargon.
DEV.txt:4489:Zarquâo,  pg.  voy.  Jargon.
DEV.txt:4522:Zivho, pg.  ital.  voy.  Girbe. Zircon,  voy.  Jargon. Zirgehn,  pg.  voy.  Gengeli. Zmala,  voy.  Smala. Zouave,
DEV.txt:4551:Sy^  £5*=»;'  voy.  Artichaut. j3^!  voy.  Argali. c^>-i^^J>  3!;)  pers.  voy.  Azédarac. ij^)')^  P^^^-^-  voy.  Jargon. xUy  voy.  Smala. ^Uu^l  pers.  voy.  Epinard. o^^l  voy.  Alchimie,  aG;  Astrono- mie, 2/1,  et  Nébulasit. (-j^u/i  voy.  Alchimie,  7. ^jytjjA»*!  voy.  Jargon. ^UUuw!  voy.  Epinard. ^UjLu/I  voy.  Epinard. cilCv!  voy.  Escarpin. (j>^Xlu.i  voy.  Escarpin. -liUw!  voy.  Islam. ij<i!  voy.  Aigrefin. *JLi;l  voy.  Usnée. y3uo\  voy.  Astronomie,  3 5. AAs\  voy.  Zain. ^jL.c!  voy.  Ayan. Le!  fwrc,  voy.  Aga. c^ovJLil  tmx ,  voy.  Efendi. (j(^!  voy.  Aflion. ^1  mal.  voy.  Coahlaban. (£y^\  voy.  Aigrefin.
DEV.txt:4814:y-^  pers.  voy.  Jargon.
DEV.txt:4815:^^3_S^;  voy.  Jargon. ij^f)  ppi's.  voy.  Jargon. l3>;  pers.  voy.  Zurna. LUr;  pers.  voy.  Girafe. ^LJ^;  voy.  Zérumbet. *^)')  ^oy-  Zérumbet. ^;3  voy.  Alchimie,  29. iULcj  voy.  Zaïm. ^JlJLc;  voy.  Safran, rfvc^  voy.  Zaïm. ajLcv  vov.  Zajïaie.
DEV.txt:4838:(jyb^ww  voy.  Jargon.
DEV.txt:4870:(j1j>^^  voy.  Sultan, j^^.*»»  voy.  Sourate. (£^yi»  pers.  voy.  Jargon. i-oL^  m«/.  voy.  Siamang. ChJiku  voy.  Cid. <^jy^*k,  voy.  Cid. yL-i.ws*k,  voy.  Sesban. yyLL.»«  voy.  Jargon.
DEV.txt:5083:^y^ mal.  voy.  Gomuli. J^^OsJO  mrt/.  voy.  Gandasuli. J^.>jSmaJ.  \o\.  Gandole. >^  pers.  voy.  Giaoïir. i-.^ mal.  voy.  Goura, ^p  mal.  voy.  Gong. x^p  mal.  voy.  Pangolin. fj^ pers.  voy.  Jargon. X^  mal.  voy.  Calambac. ^^^^  mal.  voy.  Gecko.
LKT.txt:2075:'Teil'  [Ave-L  IV,  o30],  hieraus  jüd.- dtsch.  Chelek  'Teil,  Anteil  an  der  Diebes- beute', ndl.  (Gaunerjargon)  cheilek:  Man spricht  von  einem  eh.,  wenn  bei  einem Verkaufe  oder  einer  Versteigerung  sich einige  Personen  ohne  Wissen  des  Ver- käufers heimlich  verbinden,  nicht  gegen- einander zu  bieten,  und  später  das  Ge- kaufte unter  sich  verteilen.  [Dozy  Oost  30.
```


## [2026-09-05T20:56:35.069Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '1780,1795p' LKT.txt | cut -c1-1200; echo \"=== LKT leaf/page\"; python3 - <<'EOF'\nt=open('LKT.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n'); leaf=0;m={}\nfor i,l in enumerate(lines,1):\n    m[i]=leaf; leaf+=l.count('\\f')\nfor ln in (1789,):\n    print(ln,'leaf',m[ln],'printed',m[ln]-26)\nEOF"
}
```


### [2026-09-05T20:56:36.867Z] TOOL RESULT

```
'See'  [Stamm  öl,  köl  'naß,  feucht;  Meer, See'  Vämbery  TktEtWb  S.  54,  Nr.  61]; hieraus  gemäß  der  vulg.  tk.  Ausspraclie gjöl  rum.  ghiol,  ghiole  'See,  Teich'.
730.  Fers,  gölä:
'Kugel'  [Horn  NpEt  S.  207,  Nr.  928], ebenso  tk.  kuUe,  gülle  'Kanonenkugel'; hieraus  rum.  ghiulea  'dass.,  Bombe', bulg.  gulle,  serb.  zulle  'Kugel  zum Schießen'.    [Sain.ö2.   Bern  SlEtWb  375.
731.  Hebr.  göräl:
'Los,  Losstein',  die  Übersetzung  des  ar. fäl,  d.  h,  der  Kunst  vorherzusagen,  be- sonders auch  aus  Steinen;  im  mittel- alterlichen Spanien  sind  zahlreiche  Los- bücher in  arabischer  Sprache  verfaßt und  in  hebräischer  Sprache  als  sef^r görälöQ  weit  durch  das  christliche  Eu- ropa verbreitet  worden ;  so  entstand  für den  geheimnisvollen  Stein,  der  die  Zu- kunft vorhersehen  ließ  [s.  Parzival,  Aus- gabe von  Lachmann  483,  20  ff.],  der Name  Gral,  frz.  Graal,  Gr^al,  engl. Grail.  —  [Andere  nicht  mehr  haltbare Etymologien  sind  a)  gradalis  'weite Prunkschüssel,  worin  stufenweise,  d.  h. gradatim,  reiche  Delikatessen  abgeteilt lagen';  dafür  HERTZ  in  seinf^r  Parzival- ausgabe.  5.  Aufl.  Stuttgart  1911.  S.  41 9  f. b)  mlai.  garalis  'Behältnis  für  Getränke', im  9.  und  10.  Jahrhundert  in  England und  Italien  belegt;  dafür  Gröber,  Grund- riß der  romauischen  Philologie.  II,  1. Straßburg  1902.  S.  .502;  Dietz,  Etymo- logisches Wörterbuch  der  romaiuschen Sprachen.  ^  Bonn  1887.  S.  601.  c)  lat, turris  oder  mons  gradalis  'stufenförmig sich  aufbauender  Palast'  als  Ort 
Pers.  gOsä.]
58
Gral.  Köln  1916.  S.  101.  d)  frz.  grS und  engl,  all,  so  Tieck,  s.  Horrigs  Ar- chiv CXXXVIII,  77.  e)  Ar.  gär  'Höhle' und  Art.  al  geschraubt  -  mystisch "]. Vgl.  KAIMPENS  in  Mitteilungen  der Schlesischen  Gesellschaft  für  Volkskunde. Breslau  1917.  S.  XIX,  109/111.  Die  hier gegebene  Etymologie  stammt  von  Pasch- niann.  Vgl  meine  Zusammenfassung  in KZ  1925,  Nr.  504  Beilage.
732.  Pers.  gösä:
'Winkel,  Ecke'  [Horn  NpEt S.  211, Nr.  945], tk.  zu  kjosk,  kjöSk  Talast,  Villa,  Pavillon' geworden;  hieraus  bulg.  kosk  'Garten- haus', serb.  cosak  'Söller',  poln.  kiosk, russ.  kiosk;  it.  chiosco,  frz.  kiosque,  sp. Jciosco,  rum.  chiosc  'Verkaufsbude', c/t/oscar 'Zeitungsverkäufer';  dtsch. iiiosÄ;, ndl.  engl,  kiosk  'dass.'.  Die  pers.  Form zeigen  noch  bulg.  kose,  kuse  'Winkel', serb.  cose  'dass.'.  [Devic  DEt  149.  Bern SlEtWb  680.
733.  Tk.  götiirme:
Subst.lnfin.  Aes'^hs. götürmek  'aufheben, aufbürden'  [Stamm  göc,  köc,  s.  hier Nr.  725] ;  hieraus  russ.  ktäer'ma  'Schnee- gestöber, Wirrwarr'.
734.  Tk.  götürü:
'Vollständig,  im  großen  und  ganzen' [vom  tk.  götürniek,  s.  hier  Nr.  733] ;  hier- aus rum.  CM  ghioturä  'in  Bausch  und Bogen,  en  gros'.
735.  Tk.  Gozz:
N.  pr.,  ein  tk.  Stamm,  dessen  Angehörige von  den  Almohaden  in  Marokko  und Spanien  (1 130—1269)  zu  Henkersdiensten gebraucht  wurden ;  hieraus  mit  ar.  Art. pg.  algoz,  sp.  algoce  'Henker,  Scharf- richter', sp.  pg.  algozaria  'Grausamkeit, grausame  Handlung'.  [DE  128/129. Eguilaz  182.    ML  3826  a.
=== LKT leaf/page
1789 leaf 85 printed 59
```


## [2026-09-05T20:56:42.509Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^ *945\\.\\|^ *944\\.\\|^ *946\\.\\|945\\. \" HRN.txt | head; echo \"===\"; grep -n \"gundah\\|gunda\\|gonde\\|kuSk\\|kušk\\|kuschk\\|gōša\\|gösa\\|gosa\" HRN.txt | head -20"
}
```


### [2026-09-05T20:56:42.564Z] TOOL RESULT

```
8185:944. gast 'Fleisch*.
8192:945. göSe 'Winkel, Ecke .
===
4441:skr. gösa-.
8130:aw. gunda- (vd. 3, 32) 'Teig (Geldnor, KZ. 24,
8131:549 Note 4); phlv. gundak.
8195:kurd. güi, güse 'Winkel*; bei. LW. gösak (127).
8198:als kuSk und kü§k zu den Persern zurückgewandert
9247:bei. mgösag, niyösay (262).
14662:gunda- 936.
20611:nigösag 1070.
```


## [2026-09-05T20:56:46.408Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '8120,8145p' HRN.txt; echo \"-----\"; sed -n '8180,8205p' HRN.txt; echo \"=== pages\"; python3 - <<'EOF'\nt=open('HRN.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n'); leaf=0;m={}\nfor i,l in enumerate(lines,1):\n    m[i]=leaf; leaf+=l.count('\\f')\nfor ln in (8125,8130,8185,8192,8198):\n    print(ln,'leaf',m[ln],'printed',m[ln]-21)\nEOF"
}
```


### [2026-09-05T20:56:48.318Z] TOOL RESULT

```
Bartholomae, ZDMG. 44, 552 zu ap. gasta- *übel,
widerwärtig* ; sar. yofid.
935. gend/um *Weizen', ar. LW. jandum in jauz-i jandum.
skr. gödhüma- 'Weizen* (dagegen iran. ^gandhüma-^
Hübschmann, ZDMG. 44, 556 2)); phlv.-paz. gantum
d. i. gandum (PPGl.).
LW. kurd. genim (vergl. g. gamim); af/. yanum;
wa/. yid%m, sangl. minj. yanddm, sar. zandani, sandum,
^\yn. zindum, yidg. yadum; bei. gandtm (98).
936. gunde *Hefenballen (für ein BrotV.
aw. gunda- (vd. 3, 32) 'Teig (Geldnor, KZ. 24,
549 Note 4); phlv. gundak.
Unsicher.
937. gv/ng 'stumm' 8).
skr. [/^guüj-, gufijati summen, brummen' (Geiger:
'das Brummen bezeichnet die tierischen Laute des
Stummen im Gegensatz zur menschlichen Sprache').
Unsicher.
LW. afy. bei. (77) gung stumm*.
938. gor 'Wildesel*, gür/er,
ai. gäurd' 'weisslich, gelblich, rötlich; eine Büflfel-
art: Bos Gaurus* (Spiegel, Ar. Periode 55); phlv. gör
(Papyrus, Hörn ZDMG. 43, 51 und 619).
LW. kurd. gör; afy. yyara; bei. gör 'Wildesel' (80).
^) Das angebliche phlv. ganäk, ganräk erklärt Bartholomae
a. a. O. auch nicht richtig, es ist höchst wahrscheinlich mit Andreas
-----
ghoSa- 'Lärm, Getön .
kurd. güh; afy. yvay; oss. d. yos, t. qüs (94); bei.
gös (125); wa/. yws, yis etc.
np. gösvär^ ^öst^äre 'Ohrgehänge*: aw. frä.[gaosävara-,
mat,[gaosävare; phlv. gösvär,
944. gast 'Fleisch*.
aw. gäv, Nom. gän§ 'Fleisch' ; phlv. göst^ göstm (GFr.).
LW. afy. yva/a 'Fleisch'; kurd. güst; bei. gö$t, n.
göM (128); wa/. gust, minj. yös, sar. gü^t, siyn. goß,
^) Zuerst hat dies wohl Bückert, ZDMG. 10, 183 ausgesprochen.
«) Vergl. Fr. Müller, WZKM. 5, 263.mmtmmmmmmm^mmmmi^^^m^^^
— 211 —
945. göSe 'Winkel, Ecke .
KäS. gm.
aw. *gaosaha-.
kurd. güi, güse 'Winkel*; bei. LW. gösak (127).
de Lagard e, Ges. Abb. stellt auch küsk *Kiosk'
hierher, das, im türkischen Munde zu kföik geworden,
als kuSk und kü§k zu den Persern zurückgewandert
sei ; arab. LW. jausäq, syr. LW. pK'i;! *Kiosk' sprechen
dafür, phlv.-päz. küSk bezw. köSk (PP61.) als späte
Form nicht dagegen.
^46. gün 'Farbe; Art und Weise*, güne,
ap. 'Podo]y(wvrj, 'AXojyovvrj; aw. goona- *Farbe'; phlv.
günak, gün, arm. LW. goin^),
afy. LW. yüna,
=== pages
8125 leaf 230 printed 209
8130 leaf 230 printed 209
8185 leaf 231 printed 210
8192 leaf 232 printed 211
8198 leaf 232 printed 211
```


## [2026-09-05T20:57:11.763Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KNT kaufa\"; grep -n \"kaufa\" KNT.txt | head -10"
}
```


### [2026-09-05T20:57:11.828Z] TOOL RESULT

```
=== KNT kaufa
1030:There is no identifiable example of OP f from pIE ph; OP kaufa- ‘mountain’, Av. kaofa-, seems to have no cognates outside Iranian.
1256:OP Ahaufaciya ‘men of *Akaufaka’, similarly.
1403:Note pAr. kj > pAr. ё > OP Sy, $104; pAr. fi > рії. 6; > OP sy, 580. OP Maciya- to the province-name Maka must be for *makuos, or a late formation in which *makjos did not make the second phonetic change; similarly Akaufaciya to * Akaufaka.
1778:IIT. With no obvious simpler nominal or verbal form: ama- in Arsdma-, asa- aspa-, u-ba-, poss. ^upa-, kaufa-, kara-, daiva-, darga-, naiba-, Parsa-, pisa-, Máda-, raba- in u-rafa-, varka- in Varkána- and Varka-zana-, Saka-, späda- in Taxma-spáda-, spára- in Vdya-spara-; the restored hana- in hana- {й-; mayüra-, of uncertain etymology; the pos- sible vāra- in ^U-vára-zmi-.
1792:Ш. Forming ethnics: Akaufac-iya- to * Akau- faka-; Aéur-iya- to Aéurd-; Armin-iya- to Ar- mina-; Asagart-iya- to Asagarta-; U(v)j-iya- to 0(0)ја-; Uvürazmiya-; Küfiya- to Küša-; Ga"dara-ya- (possibly error for -riya-) to Ga"dara-; Gatagu-iya- (error for -uviya- or -udaya- or -udiya- ?) to 8alagu-; Pulü-ya-; Bäbiruv-tya-; Mac-iya- to Maka-; Spard-iya- to Sparda-; Haxámanis- iya-; Harawati-ya-; Hi"du-ya (error for Hi"duv- iya- ?).
1801:IL. Secondary: *Akaufa-ka- in Akaufaciya-; Andma-ka-; ar-ika-, to pAr. *asra-, LAv. аюга; Атќа-Ка-, hypocoristic to a compound name; äršti- ka-, probably with vriddhi; kapauta-ka-; kdsa-ka-; ba^da-ka-; vazra-ka-; Vahau-ka-, hypocoristic to a compound name.
1967:‘town’; dvahanam ‘village’; didà ‘fortress’; kaufa
1981:Akaufaciya ‘Men of Akaufaka’; Unarazmiy and -miš ‘Chorasmia’; Gadára ‘Gandaritis’; 8ata- gu’ Sattagydia’; Рала ‘the Daae’; Maka or ethnic Maciya; Saka or fem. бака Scythia’ or Хака ‘the Scythians’; Sug(u)da ‘Sogdiana’; Haraiva ‘Aria’; Hidus Sind’.
3120:‘fortress, stronghold’, vardanam ‘town’, dvahanam ‘village’, kaufa ‘mountain’, rauta ‘river’, The re- sumptive adverbs are avadà ‘there’, hacá avadaSa
4256:31 caina : hauv : Labanàna : пата : kaufa : hacd : avana : aba 32 riya : kara : hya : Auriya : haudim : abara : yata :
```


## [2026-09-05T20:57:12.443Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls -la incoming/BQT/ && head -5 incoming/BQT/BQT_v4_pages.txt && grep -c \"pdf page\" incoming/BQT/BQT_v4_pages.txt"
}
```


### [2026-09-05T20:57:12.555Z] TOOL RESULT

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
[pdf page 1]
[pdf page 2]
ه
و سم
۰ و
553
```


## [2026-09-05T20:57:22.540Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KNT.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint(len(pages))\nfor i in (192,193,194):\n    print('=== leaf',i,'printed',i-15)\n    print(pages[i][:1500])\nEOF"
}
```


### [2026-09-05T20:57:24.603Z] TOOL RESULT

```
232
=== leaf 192 printed 177
-, GAv. angra-, LAv. apra- ‘hostile, enemy’, to рАт. root *ans-, seen in Av. qsta- ‘hate, enmity’; ef. also Av. (nom.) avrd mainyus ‘evil spirit, Ahriman’ (Bthl. AiW 189); not to Skt. art- ‘en- emy’ (MB Gr. §273), nor to Skt. alikd- (Wacker- nagel, KZ 59.28-9). алка nsm. DB 1.22, 33; 4.63. ага npm. DB 5.15°, 31°.
Ariya- adj. ‘Aryan’ (perhaps Ariya-, §126): Ау. atrya-, Skt. drya- ‘noble’, cf. NPers. ёгт ‘Iran, Persia’, Irish Eire ‘Ireland’, to pIE root *er-, OP ar- (585.1, §144.1). See also Ariyacica-, Artydramna-. Ariya паш. DNa 14; DSe 13; XPh 18. ariyd isn. as sb. ‘in Aryan (language) DB 4.89.
Ariyacica- adj. ‘of Aryan lincage’ (5161.18): Ariya- + ciga-. Artyacica пет. XPh 13; Ariya cica (written as two words, $44) DNa 14f, DSe 18f.
Ariydramna- sb. ‘Ariaramnes’, great-grand- father of Darius: Elam. har-ri-ia-ra-wm-na, АКК. ar-ja-ra-am-na-', Gk. 'Ариараштѕ. From ariya- + pass. pte. of d-ram- (8131; Av. Skt. ram- ‘to be at peace, to pacify’): ‘Having the Aryans at peace’ (8161.]1c). Hardly Ariyà pl. + ramna- (Foy, KZ 35.9), or Ariya- + aramna- pres. pte. mid. to ar- (Hz. Ар! 287). Anydramna nsm. AmH 1, 4, 9; DB 1.5; DBa 7; as gsm. AsH 3 ($313.1). Ariydramnahyé gsm. DB 1.5; DBa 7.
aruvü- sb. ‘action’ (JNES 444, 52; 53511, $150; so also Bv. TPS 1945.42-3): fem. to adj. arwa-, Av. aurva- ‘schnell, tapfer’ (Bthl. AiW 200), doublet to Av. aurvant- (q.v., under aru- vasta-).  aruváyà \sf. DNb 38 (inscribed afuvayá, $55.11; not anwasa with Wb. Grab 28, KIA 94;
OLD PERSIAN
not to be 
=== leaf 193 printed 178
t’).
-
LEXICON
ч.
Атах$аса- sb. ‘Artaxerxes’ (Т, son of Xerxes; П, son of Darius II; III, son of Artaxerxes II): Elam. ir-tak-Sa-a8-Sa, Akk; ar-tak-Sat-su, Gk. ’Aprakeptns (§29.n2, 530). From arta- ‘justice’ + т$аса- ‘kingdom’, ‘Having a kingdom of justice’ (hardly, with Nyberg, Rel. 352, ‘whose zšaça- de- rives from aría-); imitation of Xšayāršā, acc. -üm, explains the long vowel of the ultima in the nom. and acc. ($78, §161.[b; decl, §172, $187). Artazšaçã nsm. А:Ра 9°, 17°; АЧ; D'Sb 3°; A’Sa 1; A’5b; A*8c 1°; А4 1, 2; А? На 1; A*Hb; Ае 7, 156; A*Pa 5 (as acc., 52476), 8, 12 (as gen., $313.IT), 13 (as gen.), 14f (as gen.), 15f (as gen.), 21, 231; AVsb-d. — Ardaxcasca ($49; or -Sda) AVsa. Arlax áagüm asm. АІРА 51°; А%8а 4; A?He 5; S£ 2-4. ArtaxSacahyé gsm. D'Sb 2°; Artaxíafrahyà (Tm. Lex. 54) A?Ha 2f, 3; Arlazíagühya ($53) A’Sa 2 bis; A?He 101, (аз nom., 5313.1) 11.
ariàvan- adj. ‘righteous, blessed’, denoting the blissful state of the true religionists after death: identical with Av. asavan- ‘characterized by Arta or Asha, righteous’, Skt. rldvan- ‘true to sacred Jaw’ (cf. Hz. Ар! 289-93); from *ria-, OP arta-, with lengthened final vowel, + ad]. suffix -van- ($30, $155.IV). атара nsm. (8124.5, $187) XPh 48, 55.
Artavardiya- sb. ‘Artavardiya’, one of Darius’s generals: Flam. ?r-du-mar-ti-ja, АКК. ar- ta-mar-2i-ja. From arta- + vard- ‘to work’ + adj. suffix ($80, §31, §144.1V, S160.Ia): ‘Doer of Jus- tice’ (not from vard- ‘to increase’, Skt. vardh-, be- cause of -z- in АКК. 
=== leaf 194 printed 179
пат. AsH 1, 5; DB 1.4f; DBa 6; DSf 13; XPf 19, 20; A’Pa 20 (as gen.; §313.1[). Aršämahyā gsm. DB 1.3, 5; DBa 4, 6.
arstà- sb. ‘rectitude’ ($80; $93): haplologie for *aršta-tā- (8129), abstract to arSta- ‘upright’ (8145), pIE *rĝ-ta-, with zero-grade to root *rej- (8122; Mt. Gr. $123, $125), cf. Av. arštāt- ‘goddess of rectitude’, OP ardu- in Ardumani&-, rüsta-; or merely fem. *rĝ-iã- as abstract (Bv. Gr. $123, $125). атат asf. DB (4.64.
172
аг$Е- sb. ‘spear’ (830): Av. arsti-, Skt. rstt-, pIE *rs-ti- ($152.IIT, $179.IIT), to root in Skt. drsatt rşáli ‘rush, push’. See also ár&tika-, arsti- bara-. ат] nsf. DNa 44.
Grshka- sb. 'spearman': from ar&- ‘spear’ with vriddhi (as in wárttika-, $126), + suffix -ka- ($146.10). ага пет. DNb 44.
arslibara- sb. ‘spear-bearer’: aršti- ‘spear’ + bara- ‘bearer’ ($122, §143.V, §160.Ia). arStbara пзш. DNe 2 (written 59519, $51; the original draft seems to have had ате; on proofread- ing, the $° which was to have replaced the s* was wrongly substituted for the a, and this falsely cor- rected orthography was inscribed on the rock).
‘ava- demonst. adj. and pron. ‘that’ (5260.11, $264): Av. ava-, Skt. gen. du. avós, oCS орй; see also avd, араба, avadà, avapard, avahyarüdiy, pasiva. Decl., $200.
avam asm. DB 1.21, 22, 31, 40, 49, 57, 76, 80, 84, 88; 2.4, 4f, 12, 17, 20, 25, 30, 31, 35, 40f, 46, 50, 51, 55, 61, 84, 87, 94, 97; 3.4, 7, 12, 14, 14f, 17, 27, 38, 45f, 47f, 50, 56f, 58, 62, 67, 82, 85, 89; 4.38, 66 bis; 5.6°, 27; DNa 2; DSe 2; DSf 2°; DSt
```


## [2026-09-05T20:57:32.970Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KNT.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if 'kaufa' in p and 'mountain' in p and i>150:\n        print('leaf',i,'printed?',i-15)\n        import re\n        for m in re.finditer('kaufa',p):\n            print('   ...',p[max(0,m.start()-300):m.start()+300].replace('\\n',' '))\n        print('PAGENUMS in leaf:', re.findall(r'(?m)^\\s*(1[6-9]\\d|2[0-1]\\d)\\s*$',p))\nEOF"
}
```


### [2026-09-05T20:57:34.584Z] TOOL RESULT

```
leaf 186 printed? 171
   ... 3, 37, 44; A'Pa 18f. AM nsm. (842) DSe 50°; DSi 3°; DS} 4, 6°; DSk 4; DSn 2^; D'Sa 3; A*Sa 4° (as gen., 5818.1), 4; A’Sd 3; А?На 5° (as gen), 6. АМташ DSk 5; D8m 3. AMm asm. DSk 4. AMha gsm. DSa 4; ligature ($42) DSk 4. AMha DS] 3°, 5; Аа 3. AMha or АМ№ DSd 3°; DSi 4°; DSm 5°; D8o 3°; D’Sb 4°. 165 Akaufaciya- adj. sb. ‘man of Akaufaka’; pl. a province of the Persian Empire: АКК. a-ku-pi-i-1$. Deriv. of * Akaufaka- ‘Kohistan’, prefix à + kaufa- ‘mountain’ + adj. suffix ($113, 814411; ef. Hz. AMI 8.72; Kent, Lg. 13.298-9). Akaufaciyd npm. XPh 27. | akarta- adj. ‘not made, no
   ... (842) DSe 50°; DSi 3°; DS} 4, 6°; DSk 4; DSn 2^; D'Sa 3; A*Sa 4° (as gen., 5818.1), 4; A’Sd 3; А?На 5° (as gen), 6. АМташ DSk 5; D8m 3. AMm asm. DSk 4. AMha gsm. DSa 4; ligature ($42) DSk 4. AMha DS] 3°, 5; Аа 3. AMha or АМ№ DSd 3°; DSi 4°; DSm 5°; D8o 3°; D’Sb 4°. 165 Akaufaciya- adj. sb. ‘man of Akaufaka’; pl. a province of the Persian Empire: АКК. a-ku-pi-i-1$. Deriv. of * Akaufaka- ‘Kohistan’, prefix à + kaufa- ‘mountain’ + adj. suffix ($113, 814411; ef. Hz. AMI 8.72; Kent, Lg. 13.298-9). Akaufaciyd npm. XPh 27. | akarta- adj. ‘not made, no
   ... 1), 4; A’Sd 3; А?На 5° (as gen), 6. АМташ DSk 5; D8m 3. AMm asm. DSk 4. AMha gsm. DSa 4; ligature ($42) DSk 4. AMha DS] 3°, 5; Аа 3. AMha or АМ№ DSd 3°; DSi 4°; DSm 5°; D8o 3°; D’Sb 4°. 165 Akaufaciya- adj. sb. ‘man of Akaufaka’; pl. a province of the Persian Empire: АКК. a-ku-pi-i-1$. Deriv. of * Akaufaka- ‘Kohistan’, prefix à + kaufa- ‘mountain’ + adj. suffix ($113, 814411; ef. Hz. AMI 8.72; Kent, Lg. 13.298-9). Akaufaciyd npm. XPh 27. | akarta- adj. ‘not made, no
   ...  6. АМташ DSk 5; D8m 3. AMm asm. DSk 4. AMha gsm. DSa 4; ligature ($42) DSk 4. AMha DS] 3°, 5; Аа 3. AMha or АМ№ DSd 3°; DSi 4°; DSm 5°; D8o 3°; D’Sb 4°. 165 Akaufaciya- adj. sb. ‘man of Akaufaka’; pl. a province of the Persian Empire: АКК. a-ku-pi-i-1$. Deriv. of * Akaufaka- ‘Kohistan’, prefix à + kaufa- ‘mountain’ + adj. suffix ($113, 814411; ef. Hz. AMI 8.72; Kent, Lg. 13.298-9). Akaufaciyd npm. XPh 27. | akarta- adj. ‘not made, no
   ...  3°, 5; Аа 3. AMha or АМ№ DSd 3°; DSi 4°; DSm 5°; D8o 3°; D’Sb 4°. 165 Akaufaciya- adj. sb. ‘man of Akaufaka’; pl. a province of the Persian Empire: АКК. a-ku-pi-i-1$. Deriv. of * Akaufaka- ‘Kohistan’, prefix à + kaufa- ‘mountain’ + adj. suffix ($113, 814411; ef. Hz. AMI 8.72; Kent, Lg. 13.298-9). Akaufaciyd npm. XPh 27. | akarta- adj. ‘not made, no
PAGENUMS in leaf: ['165']
leaf 200 printed? 185
   ... yntax der Pron. im Av. 47; Kieckers, Etymol. Miszellen 1934.135; otherwise Gray, JAOS 23.60). DB 4.37, 41, 67°, 70, 87°; DSt 10°; XPh 46. -katy, emphatic encl. particle, m ada-katy (q.v.): probably lsn. to ka- ($191.11), ef. Gk. то ‘somewhither’ (Bv. Gr. $336 takes as *ka*<4, cf. naiy from *na-19). kaufa- sb. ‘mountain’: Av. kaofa-, Phl. kof, NPers. köh ($75.IT, $106). See also Akaufactya-. kaufa nsm. DB 1.37; 3.44; DSf 31. OLD PERSIAN ka"ta- pte. as sb. (8276. TII) ‘excavation’: pAr, « 7 с *knta-, to 'kan-, with restored n ($242.11) agin с Samar-kand, wherein -kand has been transferred from t
   ... AOS 23.60). DB 4.37, 41, 67°, 70, 87°; DSt 10°; XPh 46. -katy, emphatic encl. particle, m ada-katy (q.v.): probably lsn. to ka- ($191.11), ef. Gk. то ‘somewhither’ (Bv. Gr. $336 takes as *ka*<4, cf. naiy from *na-19). kaufa- sb. ‘mountain’: Av. kaofa-, Phl. kof, NPers. köh ($75.IT, $106). See also Akaufactya-. kaufa nsm. DB 1.37; 3.44; DSf 31. OLD PERSIAN ka"ta- pte. as sb. (8276. TII) ‘excavation’: pAr, « 7 с *knta-, to 'kan-, with restored n ($242.11) agin с Samar-kand, wherein -kand has been transferred from the ditch 
   ... DB 4.37, 41, 67°, 70, 87°; DSt 10°; XPh 46. -katy, emphatic encl. particle, m ada-katy (q.v.): probably lsn. to ka- ($191.11), ef. Gk. то ‘somewhither’ (Bv. Gr. $336 takes as *ka*<4, cf. naiy from *na-19). kaufa- sb. ‘mountain’: Av. kaofa-, Phl. kof, NPers. köh ($75.IT, $106). See also Akaufactya-. kaufa nsm. DB 1.37; 3.44; DSf 31. OLD PERSIAN ka"ta- pte. as sb. (8276. TII) ‘excavation’: pAr, « 7 с *knta-, to 'kan-, with restored n ($242.11) agin с Samar-kand, wherein -kand has been transferred from the ditch 
PAGENUMS in leaf: ['178']
```


## [2026-09-05T20:57:41.355Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"gyre\\|gyro\\|geu-\\|gwher\\|gyros\" AHD_watkins1985.txt | head -20"
}
```


### [2026-09-05T20:57:41.415Z] TOOL RESULT

```
499:geue-. To hasten. Possibly the base of Germanic *kaur- Jan in Old Norse keyra, to drive: SKIJORING. [Pok. geu- 399.]
557:gyeu-. Also geu-. To chew. Germanic *kewwan in Old English céowan, to chew: CHEW. [Pok. g(iJeu- 400.]
```


## [2026-09-05T20:57:43.193Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"zircon\\|zirkon\" LKT.txt WEB_vol1.txt FSD_vol4.txt SKT.txt 2>/dev/null | head -10; echo \"=== FSD vol4 jargon\"; grep -n -i \"giargone\" *.txt incoming/*/*.txt 2>/dev/null | head"
}
```


### [2026-09-05T20:57:43.295Z] TOOL RESULT

```
WEB_vol1.txt:62799:Vanadium 1... ™ 23 30°33 Wolframuce. equ NY lA Bia Kenon od ogo E, a 173.04 Ytterbium . .. . Yb 70 88.92 Yttrium e ses 39 65.38 Aa A ate CO. 30 : Zirconium .... Zr 40 i
WEB_vol1.txt:67302:eu-di/a-lyte, n. [Gr. eudialytos, easy to break up or dissolve; ex-, well, easy, and dialylos, capable of dissolution, from dialyein, to dis- solve; dia, through, and lyein, to loosen.) a mineral of a brownish-red color found in Greenland, and containing lime, soda. and jron in combination with zirconium, silica, tantalum, manganese, and other elements.
WEB_vol1.txt:93142:4. a gem; specifically, (a) among the an- cients, a blue gem, probably the sapphire; (b) any of the reddish-orange varieties of zircon, garnet, or topaz; jacinth.
WEB_vol1.txt:101567:1. a reddish-orange precious stone, a vari- ety of zircon; a hyacinth.
WEB_vol1.txt:101827:jar’ddn, n. a jarde. jar/fly, a. a cicada. p i ar/gle, v.i.toemit aharsh or shrill sound. [Obs.] yellow jasmine; the Gelsemium sempervirens, ES, n. [OFr. jargon, gergon, gibberish.] a shrub having showy, fragrant, yellow flow- 1 1. confused, unintelligible talk or language; | €TS. | ; A gabble; gibberish. ; i Jasmine tree, the red Me ae ao 2. the dialect resulting from the mixture of inum, 7. a genus of the family Oleacez, suages: as, the Chinook jargon. whose species are cultivated for their fowers langua pai Gage or dialect that is incompre- or fragrant oils. ; á hensible, outlandish, etc. to one. Jā’sðn, n. [L. Iāson; Gr. Iéson, lit., healer.] in 4. the specialized vocabulary and idiomsof Greek legend, a prince who led the Argonauts those in the same work, way of life, etc., as and, with Medea’s help, got the Golden journalism or social work: somewhat deroga- Fleece in spite of the fire-breathing bulls and (ory term, implying unintelligibility. 3 the dragon guarding it. jar’g6n, v.i. jargoned, pt., pp.; jargoning, ppr. Jas’pa-chate, n. agate jasper. [Obs.] [Fr. jargonner, from jargon, gibberish.]totalk jas-pé’ (zhas-pa’), a. [Fr.] in ceramics, streaked gibberish or jargon; to gabble. , and mottled in imitation of jasper. __ jar’g6n, n. [Fr. jargon; It. giargone, a sort of jas’pér, n. [ME. jasper, jaspr; OFr. jaspre, yellow diamond; perhaps from Per. zargiin, J@SPé. L. iaspis, Gr. taspis, a green-colored gold-colored; zar, gold, and gin, color.] a col- Precious stone.] E, í s Buea cr smoky variety pfzircon low, or brown, When Meo gee es jar-30- /. 747r.60-nel/ A iar- ’ own. ri stri Järigo. neue, ia go-nel a mE do of jar- or bands, it is called banded or striped jasper; _ gon, the mineral.] an early harvest pear. when it has layers of chalcedony, it is called jar-gon’ic, a. pertaining to the mineral jargon. agate jasper. jar’g6n-ist, n. one who uses jargon. 2. in the Bible, probably a green orna- jar’g6n-ize, v.7.; jargonized, pt., pp.; jargoniz- _mentalstone. _ ee hs ing, ppr. to talk or write in jargon. jas’pér-a-ted, a. mixed with jasper, containing jar’g6n-ize, v.t. to express in jargon; to make , particles of jasper; as, jasperated agate. jargon of. jJas’per-ize, v.t.; jasperized, pi., pp.; jasperi- jar’goon, n. same as jargon (zircon). zing, ppr. to cause to Pee or become like järl (yarl), n. [Scand.] an ancient Scandinavian , eee A Ze RAA, 11 nobleman, chief, or leader. jas’pér 6 , a kind of opal containing yellow jar’nut, n. (Dan. jorduod, earthnut.] the pig-
FSD_vol4.txt:29651:ta-chom'e-ter,  1   ta-korn'i-tor,  2   ta-eSm'e-ter,  n   A contrivance  for  measuring  v'elocitj  (1)  A   device  to show  the  swiftness  of  a   current  by  Its  effect  upon  a   sub- merged paddle  or  paddle-wheel  (2)  Med  An  instrument lor  ascertaining  the  velocity  of  the  blood  in  circulation  (3) A   device  for  showing  changes  In  the  velocity  of  machines by  the  action  of  mercury  in  a   revolving  cup,  which  spreads from  centrifugal  force  and  causes  the  mercury  to  fall  In  a tube  connecting  with  the  cup  [<  Gr  meftos,  swiftness  ( < taehys  swift),  +   -meter  ]   — Woltmann’s  tachometer,  a current-meter  having  a   rotating  screw  for  driving  clock- work, indicating  the  speed  in  miles  per  hour  —   ta-chom'c- try,  n   The  art  or  science  ot  using  a   tachometer  tach"e- om'e-tryj  —   tach"o-met'rlc,  a tach'y-,  1   taVi-,  2   t5c'>-  From  Greek  facAj/s,  swift  a combining  form  — tach"y-a-plialtqte,  n   Mineral  An alteration  product  of  zircon  —   tach"y-car'dl-a,  n   Abnor- mal rapidity  of  the  action  of  the  heart  —   tacU'>-dl-dax"y, n   (Rare }   An  art  or  method  of  rapid  Instruction  —   tach'y- dromc,  n   A   cursorlold  plover-llke  bird,  a   courser  — ta-chyd'ro-mous,  a   —   tacli'y-gen,  n   An  organ  or  part which  has  dev  eloped  suddenly  during  ev  olutlon  of  a   species
FSD_vol4.txt:34412:2   Entom  The  middle  region  of  the  body  of  an  insect, bettv  een  the  head  and  abdomen,  consisting  of  three  umt- ed  soni’tes—  the  prothorax,  the  mcsothorax,  and  the metathorax*  In  typical  insects  it  bears  the  wings  and legs  3.  The  corresponding  region  of  the  bod\  m   other arthropods,  as  crustaceans  and  arachiuds  4.  Gr.  An- ttq  A   cuirass  or  breastplate,  as  of  metal  (usually bronze)  or  leather,  for  protecting  the  chest,  stomach,  and bach  and  sometimes  the  hips  [L  ,   <   Gr  thOrax,  thorax  ] Tho'rean*  l   fhC'ro  or  fho-r5',  2   tho'ro  or  tho-rC5%  Ilenry David  C/i5l8l7-*/eI862)  An  American  essaj  1st,  critic,  and naturalist  TroWen,  or  Life  in  the  Woods  —   Tho-rcl'I-an,  a Of  or  relating  to  Thoreau  or  his  works tbo'rl-a,  1   thQ'n-a  2   th5'ri-a,  n   Chem  A   white,  very heavy  compound  (ThOi),  In  thorite,  consisting  of  thorium ozJd  used  with  zirconla  and  other  earths  In  the  mantle  of ■Wclsbach’s  Incandescent  lamp  {Latinized  form  from  Thob  ] tbo'rl-a-nite,  1   fhQ'n-a-nnIt,  2   thS'rl-a-nlt  n   Mineral  A black  radioactive  mineral  composed  chiefly  of  thorium, cerium  and  uranium  oxids,  dlscov  cred  at  Ceylon  In  1905
FSD_vol4.txt:61425:po'rah,  1   zi-p5'ra,  2   zl-p6'ra  n   fern  Bib  Ex  !1,  21 Xir'a-leet,  1   zlr'o-Ut  2   zlr'a-15t,  n   A   song  of  triumph slr'co-,  1   zur'ko-,  2   zir'co-  From  zirconium  a   com- bining form  m   chemistry  indicating  the  presence  of zircomum  in  a   compound  or  senes  of  compounds,  as,  a nrcofluond  feiore  properly  a   fluozirconate) zlr'con,  1   zur\0n,  2   zir'con,  n   ilftneral  An  adaman- tine, vanously  colored,  transparent  to  opaque  zircomum Bilicate  (ZrSiOi),  crys^lizing  in  the  tetragonal  system Certain  \   arietles  of  zircon  are  cut  Into  gems,  and  as  such  ex- hibit more  fire  than  any  other  known  gem  except  the  dia- mond The  gem  %   arietles  of  zircon  are  called  jargon  and hyacinth.
FSD_vol4.txt:61426:Zircon  occura  in  crystalline  rocks,  especially  granular  lime- stone chlontic  and  other  schists  cneiss,  syenite  also  m   eranite, Bometimes  in  iron-ore  beds  J   D   Daija  Mincralouv  ed  by  E   8 Dana  S   394.  p   485  [was  *09  1
FSD_vol4.txt:61427:IF,  =   jargon  see  jargon* ] —   rircon  syenite  {Petrol),  a variety  ot  eleollte  syenite  locally  rich  In  zircon,  occurring  In southern  Norway  —   zir'con-ate,  n   A   salt  of  zlrconlc  acid —   zlr^co-nlf'er-ous,  a   Petrol  Containing  zircon
=== FSD vol4 jargon
DEV.txt:1555:Jargon.  Gemme  de  couleur  jaune  tirant  sur  le  rouge, souvent  confondue  avec  VhyacintJie.  Le  minéralogiste  Haûy a  réuni  ces  deux  sortes  de  pierres  sous  le  nom  commun de  zircon.  Ital.  giargone.  Jargon  et  zircon,  dont  personne, à  ma  connaissance,  n'a  encore  établi  l'étvmoloffie,  sont certainement  identiques  à  l'espagnol  azarcon.  D'après  le Dictionnaire  de  l'Académie  espagnole,  azarcon,  en  pein- ture, signifie  orangé  vif  :  ^e\  color  naranjado  muy  encen- dido,  color  aureus;v  ce  qui  s'applique  très-exactement  à l'hyacinthe.  Azarcon  s'est  dit  aussi,  comme  le  portugais zarcâo,  zarquào,  azarcâo,  de  l'ocre  rouge.  Et  tous  ces  mots correspondent  à  un  terme  arabe,  ij^)';)  zarqoûn,  avec  l'ar- ticle az-zarqoûn,  qui  se  disait  du  minium  et  d'autres  sub-
WEB_vol1.txt:101827:jar’ddn, n. a jarde. jar/fly, a. a cicada. p i ar/gle, v.i.toemit aharsh or shrill sound. [Obs.] yellow jasmine; the Gelsemium sempervirens, ES, n. [OFr. jargon, gergon, gibberish.] a shrub having showy, fragrant, yellow flow- 1 1. confused, unintelligible talk or language; | €TS. | ; A gabble; gibberish. ; i Jasmine tree, the red Me ae ao 2. the dialect resulting from the mixture of inum, 7. a genus of the family Oleacez, suages: as, the Chinook jargon. whose species are cultivated for their fowers langua pai Gage or dialect that is incompre- or fragrant oils. ; á hensible, outlandish, etc. to one. Jā’sðn, n. [L. Iāson; Gr. Iéson, lit., healer.] in 4. the specialized vocabulary and idiomsof Greek legend, a prince who led the Argonauts those in the same work, way of life, etc., as and, with Medea’s help, got the Golden journalism or social work: somewhat deroga- Fleece in spite of the fire-breathing bulls and (ory term, implying unintelligibility. 3 the dragon guarding it. jar’g6n, v.i. jargoned, pt., pp.; jargoning, ppr. Jas’pa-chate, n. agate jasper. [Obs.] [Fr. jargonner, from jargon, gibberish.]totalk jas-pé’ (zhas-pa’), a. [Fr.] in ceramics, streaked gibberish or jargon; to gabble. , and mottled in imitation of jasper. __ jar’g6n, n. [Fr. jargon; It. giargone, a sort of jas’pér, n. [ME. jasper, jaspr; OFr. jaspre, yellow diamond; perhaps from Per. zargiin, J@SPé. L. iaspis, Gr. taspis, a green-colored gold-colored; zar, gold, and gin, color.] a col- Precious stone.] E, í s Buea cr smoky variety pfzircon low, or brown, When Meo gee es jar-30- /. 747r.60-nel/ A iar- ’ own. ri stri Järigo. neue, ia go-nel a mE do of jar- or bands, it is called banded or striped jasper; _ gon, the mineral.] an early harvest pear. when it has layers of chalcedony, it is called jar-gon’ic, a. pertaining to the mineral jargon. agate jasper. jar’g6n-ist, n. one who uses jargon. 2. in the Bible, probably a green orna- jar’g6n-ize, v.7.; jargonized, pt., pp.; jargoniz- _mentalstone. _ ee hs ing, ppr. to talk or write in jargon. jas’pér-a-ted, a. mixed with jasper, containing jar’g6n-ize, v.t. to express in jargon; to make , particles of jasper; as, jasperated agate. jargon of. jJas’per-ize, v.t.; jasperized, pi., pp.; jasperi- jar’goon, n. same as jargon (zircon). zing, ppr. to cause to Pee or become like järl (yarl), n. [Scand.] an ancient Scandinavian , eee A Ze RAA, 11 nobleman, chief, or leader. jas’pér 6 , a kind of opal containing yellow jar’nut, n. (Dan. jorduod, earthnut.] the pig-
```


## [2026-09-05T20:57:55.926Z] TOOL CALL #58: Bash

```json
{
 "command": "sed -n 1,60p tools/fetch_source.py"
}
```


### [2026-09-05T20:57:55.969Z] TOOL RESULT

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


## [2026-09-05T20:58:01.269Z] TOOL CALL #59: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/%DA%AF%D9%88%D8%B4%D9%87\" \\\n \"https://en.wiktionary.org/wiki/%DA%A9%D9%88%D8%B4%DA%A9\" \\\n \"https://en.wiktionary.org/wiki/kiosk\" \\\n \"https://en.wiktionary.org/wiki/%DA%AF%D9%86%D8%A8%D8%AF\" \\\n \"https://en.wiktionary.org/wiki/%DA%AF%D9%88%D9%86\" \\\n \"https://en.wiktionary.org/wiki/zircon\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 176, root Geu 1/Keu 1, kiosk/gonbad/gun chain\" ; done 2>&1 | tail -20"
}
```


### [2026-09-05T20:58:06.031Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/a97ed1789e31fcde.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c394bd3dcfa96441.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/43add7b77c3c48a2.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/82a6b1f7b0486cdc.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d57074b9dda3ae12.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/32c93613a193bfd9.txt
```


## [2026-09-05T20:58:08.768Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in a97ed1789e31fcde c394bd3dcfa96441; do echo \"======== $f\"; sed -n '1,20p' $f.txt; echo \"...\";  grep -n -A25 \"^Persian\" $f.txt | head -60; done"
}
```


### [2026-09-05T20:58:10.630Z] TOOL RESULT

```
======== a97ed1789e31fcde
URL: https://en.wiktionary.org/wiki/%DA%AF%D9%88%D8%B4%D9%87
FETCHED: 2026-09-05T20:58:03Z
STATUS: 200
TITLE: گوشه - Wiktionary, the free dictionary

گوشه - Wiktionary, the free dictionary 

 Jump to content 

 Main menu 

 Main menu

 move to sidebar 
 hide 

 Navigation

 Main page 
 Community portal 
...
======== c394bd3dcfa96441
URL: https://en.wiktionary.org/wiki/%DA%A9%D9%88%D8%B4%DA%A9
FETCHED: 2026-09-05T20:58:03Z
STATUS: 200
TITLE: کوشک - Wiktionary, the free dictionary

کوشک - Wiktionary, the free dictionary 

 Jump to content 

 Main menu 

 Main menu

 move to sidebar 
 hide 

 Navigation

 Main page 
 Community portal 
...
```


## [2026-09-05T20:58:13.383Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in a97ed1789e31fcde c394bd3dcfa96441 82a6b1f7b0486cdc d57074b9dda3ae12; do echo \"======== $f\"; grep -n -i \"Etymology\" -A18 $f.txt | sed -n '1,70p'; done"
}
```


### [2026-09-05T20:58:15.067Z] TOOL RESULT

```
======== a97ed1789e31fcde
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Noun 
69-
70- 1.3.1 
71- Inflection 
72-
73- 1.3.2 
74- Derived terms 
75-
76- 1.3.3 
77- Related terms 
78-
79- 1.3.4 
80- Descendants 
--
159: Etymology
160- [ edit ] 
161-
162- From Middle Persian [script needed] ( gwšk' /⁠gōšag⁠/ , “ corner ” ) , which appears to be a suffixed formation from the word found now as گوش ( gōš , “ ear ” ) , in the sense of a lappet or protruding end of something. [ 1 ] 
163-
164- Pronunciation
165- [ edit ] 
166-
167- ( Classical Persian ) IPA ( key ) : /ɡoː.ˈʃa/ 
168-
169- ( Dari, formal ) IPA ( key ) : [ɡoː.ʃä] 
170-
171- ( Dari, formal ) IPA ( key ) : [ɡoː.ʃä] 
172- ( Kabuli ) IPA ( key ) : [ɡoː.ʃä] 
173-
174- ( Hazaragi ) IPA ( key ) : [ɡʊː.ʃä] 
175-
176- ( Iran, formal ) IPA ( key ) : [ɡ̥uː.ʃe] 
177-
======== c394bd3dcfa96441
65: Etymology 
66-
67- 1.3 
68- Pronunciation 
69-
70- 1.4 
71- Noun 
72-
73- 1.4.1 
74- Inflection 
75-
76- 1.4.2 
77- Descendants 
78-
79- Toggle the table of contents 
80-
81- کوشک 
82-
83- 9 languages 
--
157: Etymology
158- [ edit ] 
159-
160- From Middle Persian kwšk' ( kōšk , “ pavilion, palace, kiosk ” ) . Compare Aramaic קושקא ( qōšqāʾ ) / ܓܘܫܩܐ ( gawšāqāʾ ) , Iranian borrowings. Doublet of کیوسک .
161-
162- Pronunciation
163- [ edit ] 
164-
165- ( Classical Persian ) IPA ( key ) : /ˈkoːʃk/ 
166-
167- ( Dari, formal ) IPA ( key ) : [kʰoːʃk] 
168-
169- ( Dari, formal ) IPA ( key ) : [kʰoːʃk] 
170- ( Kabuli ) IPA ( key ) : [kʰoːʃk] 
171-
172- ( Hazaragi ) IPA ( key ) : [kʰʊːʃk] 
173-
174- ( Iran, formal ) IPA ( key ) : [kʰuːʃkʰʲ] 
175-
======== 82a6b1f7b0486cdc
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Noun 
69-
70- 1.3.1 
71- Alternative forms 
72-
73- 1.3.2 
74- Derived terms 
75-
76- 1.3.3 
77- Descendants 
78-
79- 1.4 
80- Further reading 
--
91: Etymology 
92-
93- 2.3 
94- Pronunciation 
95-
96- 2.4 
97- Noun 
98-
99- 2.4.1 
100- Declension 
101-
102- Toggle the table of contents 
103-
104- گنبد 
105-
106- 7 languages 
107-
108- বাংলা 
109- فارسی 
--
177: Etymology
178- [ edit ] 
179-
180- Inherited from Middle Persian [script needed] ( gwmbt' /⁠gumbad⁠/ , “ dome, fire-temple ” ) , from Classical Syriac ܩܘܒܬܐ ( qubbəṯā ) . Doublet of قبه ( qobbe , “ dome ” ) , also from Syriac but through Arabic. Compare Old Armenian գմբեթ ( gmbetʻ ) and Georgian გუმბათი ( gumbati ) , Iranian borrowings.
181-
182- Pronunciation
183- [ edit ] 
184-
185- ( Classical Persian ) IPA ( key ) : /ɡun.ˈbad/ 
186-
187- ( Dari, formal ) IPA ( key ) : [ɡʊm.bád̪] 
188-
189- ( Dari, formal ) IPA ( key ) : [ɡʊm.bád̪] 
190- ( Kabuli ) IPA ( key ) : [ɡʊm.bád̪] 
191-
192- ( Hazaragi ) IPA ( key ) : [ɡum.bád̪̥] 
193-
194- ( Iran, formal ) IPA ( key ) : [ɡ̥om.bǽd̪̥] 
195-
--
352: Etymology
353- [ edit ] 
354-
355- Borrowed from Classical Persian گُنْبَد ( gunbad ) .
356-
357- Pronunciation
358- [ edit ] 
359-
360- ( Standard Urdu ) IPA ( key ) : /ɡʊm.bəd̪/ 
361-
======== d57074b9dda3ae12
73: Etymology 
74-
75- 2.2 
76- Pronunciation 
77-
78- 2.3 
79- Noun 
80-
81- 2.3.1 
82- Derived terms 
83-
84- 2.4 
85- References 
86-
87- 3 
88- Persian 
89-
90- Toggle Persian subsection 
91-
--
93: Etymology 1 
94-
95- 3.1.1 
96- Pronunciation 
97-
98- 3.1.2 
99- Noun 
100-
101- 3.1.2.1 
102- Derived terms 
103-
104- 3.1.2.2 
105- Descendants 
106-
107- 3.2 
108: Etymology 2 
109-
110- 3.2.1 
111- Pronunciation 
112-
113- 3.2.2 
114- Noun 
115-
116- 3.2.2.1 
117- Descendants 
118-
119- 3.3 
120- References 
121-
122- 3.4 
123- Further reading 
124-
125- 4 
126- Ushojo 
--
262: Etymology
263- [ edit ] 
264-
265- Compare Persian گند ( gond , “ testicle ” ) and Middle Persian [script needed] ( gwnd /⁠gund⁠/ ) .
266-
267- Pronunciation
268- [ edit ] 
269-
270- IPA ( key ) : /ɡʊn/ 
271-
272- Noun
273- [ edit ] 
274-
275- Northern Kurdish
276-
```


## [2026-09-05T20:58:29.647Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"=== گوشه refs\"; sed -n '155,260p' a97ed1789e31fcde.txt | grep -v \"^$\" | head -60"
}
```


## [2026-09-05T20:58:30.194Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"=== گون Persian etym\"; awk 'NR>=280 && NR<=420' d57074b9dda3ae12.txt | grep -v \"^ *$\" | head -70"
}
```


### [2026-09-05T20:58:31.409Z] TOOL RESULT

```
=== گوشه refs
 Persian Wikipedia has an article on: گوشه 
 Wikipedia fa 
 Etymology
 [ edit ] 
 From Middle Persian [script needed] ( gwšk' /⁠gōšag⁠/ , “ corner ” ) , which appears to be a suffixed formation from the word found now as گوش ( gōš , “ ear ” ) , in the sense of a lappet or protruding end of something. [ 1 ] 
 Pronunciation
 [ edit ] 
 ( Classical Persian ) IPA ( key ) : /ɡoː.ˈʃa/ 
 ( Dari, formal ) IPA ( key ) : [ɡoː.ʃä] 
 ( Dari, formal ) IPA ( key ) : [ɡoː.ʃä] 
 ( Kabuli ) IPA ( key ) : [ɡoː.ʃä] 
 ( Hazaragi ) IPA ( key ) : [ɡʊː.ʃä] 
 ( Iran, formal ) IPA ( key ) : [ɡ̥uː.ʃe] 
 ( Tajik, formal ) IPA ( key ) : [ɡɵ.ʃä] 
 Rhymes: -a 
 Readings
 Classical reading ? 
 gōša
 Dari reading ? 
 gōša
 Iranian reading ? 
 guše
 Tajik reading ? 
 güša
 Noun
 [ edit ] 
 Dari
 گوشه 
 Iranian Persian
 Tajik
 гӯша 
 گوشه • ( gōša / guše ) ( plural گوشه‌ها ( gōša-hā / guše-hâ ) , Tajik spelling гӯша ) 
 corner 
 Synonym: کنج ( konj ) 
 1985 , “آشیونه [ âšiune ] ”: از این گوشه دنیا
به اون گوشه دنیا
منو به آشیونه
به یارم می‌رسونه az in guše-ye donyâ
be un guše-ye donyâ
man-o be âšiune
be yâram mi-resune from this corner of the world to that corner of the world
to my nest,
to my beloved, it delivers me 
 angle 
 Synonym: زاویه ( zâviye ) 
 ( music ) gosha / gusheh , dastgah , maqam 
 Inflection
 [ edit ] 
 Basic forms of گوشه 
 singular
 plural
 bare
 گوشه ( gušé ) 
 گوشه‌ها، گوشه‌ا △ ( guše-hấ, gušeấ △ ) 
 definitive direct object
 گوشه را، گوشه رو △ ( gušé râ, gušá ro △ ) 
 گوشه‌ها را، گوشه‌ا رو △ ( guše-hấ râ, gušeấ ro △ ) 
 ezâfe 
 گوشهٔ ( gušé-ye ) 
 گوشه‌های، گوشه‌ای △ ( guše-hấ-ye, gušeấ-ye △ )
```


### [2026-09-05T20:58:33.114Z] TOOL RESULT

```
=== گون Persian etym
 testicle 
 Derived terms
 [ edit ] 
 گوندێن ( gundên ) 
 گونڕەش ( gunrreş ) 
 گونی ( gunî ) 
 گونەوێڵە ( gunewêlle ) 
 References
 [ edit ] 
 Hejar ( 1990 ), “ گون ”, in Henbane borîne ‎ [2] , Tehran: Soroush, page 718 
 Wahby, T. ; Edmonds, C. J. ( 1966 ), “ gun ”, in A Kurdish-English Dictionary , London: Oxford University Press, page 57 
 Persian
 [ edit ] 
 Etymology 1
 [ edit ] 
 Etymology tree
 Proto-Iranian *gauna 
 Middle Persian 
 Persian گون 
 From Middle Persian [Book Pahlavi needed] ( gwn' /⁠gōn⁠/ , “ colour, complexion ” ) , from Proto-Iranian *gauna ( “ hair; color ” ) , perhaps related to Sanskrit गुण ( guṇa , “ thread, cord ” ) , with further origin beyond Indo-Iranian uncertain.
 Possibly from the BMAC substrate . [ 1 ] Alternatively, from Proto-Indo-European *gow-no-m ( “ something curved or vaulted ” ) , from *gew- ( “ to curve ” ) . [ 2 ] 
 Akin to Avestan 𐬔𐬀𐬊𐬥𐬀 ( gaona , “ colour ” ) , Pashto غونه ( γūna , “ colour ” ) , Ossetian хъуын ( qwyn , “ hair ” ) . Old Armenian գոյն ( goyn ) is an Iranian borrowing.
 Pronunciation
 [ edit ] 
 ( Classical Persian ) IPA ( key ) : /ˈɡuːn/ 
 ( Dari, formal ) IPA ( key ) : [ɡuːn] 
 ( Dari, formal ) IPA ( key ) : [ɡuːn] 
 ( Kabuli ) IPA ( key ) : [ɡuːn] 
 ( Hazaragi ) IPA ( key ) : [ɡun] 
 ( Iran, formal ) IPA ( key ) : [ɡ̥uːn] 
 ( Tajik, formal ) IPA ( key ) : [ɡun] 
 Rhymes: -uːn 
 Readings
 Classical reading ? 
 gūn
 Dari reading ? 
 gūn
 Iranian reading ? 
 gun
 Tajik reading ? 
 gun
 This entry needs an audio pronunciation . If you are a native speaker with a microphone, please record this word . The recorded pronunciation will appear here when it's ready.
 Noun
 [ edit ] 
 Dari
 گون 
 Iranian Persian
 Tajik
 гун 
 گون • ( gun ) 
 ( usually in compounds ) colour 
 Synonym: رنگ ( rang ) 
 kind , type , species 
 Synonym: نوع ( now' ) 
 c. 1260s , Jalāl ad-Dīn Mohammad Rūmī , translated by Reynold A. Nicholson , مثنوی معنوی [ Masnavi-ye-Ma'navi ], volume I, verse 269: هر دو گون آهو گیا خوردند و آب
زین یکی سرگین شد و ز ان مشک ناب har du gūn āhū giyā xwardand u āb
z-īn yakē sargēn šud u z-ān mušk-i nāb Both species of deer ate grass and drank water: from this one came dung, and from that one pure musk. ( Classical Persian transliteration ) 
 manner , fashion , mode 
 Derived terms
 [ edit ] 
 آسمانگون ( âsmângun ) 
 زرگون ( zargun ) 
 گوناگون ( gunâgun ) 
 گونه ( gune ) 
 Descendants
 [ edit ] 
 → Ottoman Turkish: گون ( gûn ) 
 Etymology 2
 [ edit ] 
 Apparently گو ( gaw , “ cow ” ) with suffix as hinted at گرزن ( garzan , “ crown ” ) .
```


## [2026-09-05T20:58:43.305Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && grep -n -i \"references\\|Syriac\\|Hasandust\\|Ciancaglini\\|further reading\" -A6 82a6b1f7b0486cdc.txt | sed -n '1,80p'"
}
```


### [2026-09-05T20:58:43.359Z] TOOL RESULT

```
80: Further reading 
81-
82- 2 
83- Urdu 
84-
85- Toggle Urdu subsection 
86-
--
180: Inherited from Middle Persian [script needed] ( gwmbt' /⁠gumbad⁠/ , “ dome, fire-temple ” ) , from Classical Syriac ܩܘܒܬܐ ( qubbəṯā ) . Doublet of قبه ( qobbe , “ dome ” ) , also from Syriac but through Arabic. Compare Old Armenian գմբեթ ( gmbetʻ ) and Georgian გუმბათი ( gumbati ) , Iranian borrowings.
181-
182- Pronunciation
183- [ edit ] 
184-
185- ( Classical Persian ) IPA ( key ) : /ɡun.ˈbad/ 
186-
--
335: Further reading
336- [ edit ] 
337-
338- Dehkhoda, Ali-Akbar ( 1931– ), “ گنبد ”, in Dehkhoda Dictionary Institute , editors, Dehkhoda Dictionary (in Persian), Tehran: University of Tehran Press . 
339-
340- Steingass, Francis Joseph ( 1892 ), “ گنبد ”, in A Comprehensive Persian–English dictionary (overall work in English), London: Routledge & K. Paul 
341-
--
404: Persian terms derived from Classical Syriac 
405- Persian doublets 
406- Persian terms with IPA pronunciation 
407- Rhymes:Persian/ad 
408- Rhymes:Persian/ad/2 syllables 
409- Persian lemmas 
410- Persian nouns
```


## [2026-09-05T20:58:49.180Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"gumbad\\|gunbad\\|gumbed\\|gonbad\\|Kuppel\" HRN.txt HUB.txt NYB_vol2_glossary.txt AFA.txt LKT.txt | head -20"
}
```


### [2026-09-05T20:58:49.234Z] TOOL RESULT

```
LKT.txt:2867:in  Nordafrika,  mit  dem  Grabe  eines Heiligen,  frz.  irrtümlicli  marabout,  s.  hier Nr.  141U,  genannt]';  hieraus  zum  Teil mit  ar.  Art.  sp.  alcoba,  pg.  alcova  'Schlaf- kabinett', kat.  alcova,  prov.  alcuba  'Zelt', afrz.  aucnbe  'dass.',  frz.  alcdve  'kleines Nebenzimmer',  rum.  alcove;  siz.  cnbba 'Wasserturm',  sp.  alcubilla  'dass.';  mit romanischer  Demin.-Endung  it.  ctipola, frz.  coiipole.  Dtsch.  Alkoven,  Ktqypel, mhd.  ekub  'Zelt'  [bei  WOLFRAM  VON ESCHENBACH],  ndl.  alkoof,  engl,  alcove 'Zimmervvinkei  für  Sitz  oder  Bett'  [m einem  Zimmer  oder  einer  Bibliothek].. Bulg.  kube,  serb.  kube,  kuba  'Kuppel, Gewölbe',  russ.  alkow  'Alkoven';  über vulg.  ar.  kiibbat,  kas.-tat.  kibbet,  kirgis. kibü  wurde  russ.  kibitka  'Verdeck  über einem  russ.  Wagen,  halbverdecktes  russ. Fuhrwerk'.  —  Auf  die  vulg.  Form  ar. kubbäja  'Glas  zum  Trinken'  geht  viel- leicht siz.  ciibbäita  'Art  Mandelkuchen aus  geriebenen  Apfelsinenschalen,  Honig, Karamel!'  usw.  zurück  [wegen  der  zylin- drischen Form;  vielleicht  auch  vom  ar. kubbait  'Mandelkuchen',  vgl.  Dozy  Suppl s.  V.  kubbat].  Als  Eigenname  hat  sich in  Palermo  für  ein  sarazenisches  Gebäude der  Name  La  Ctiba  erhalten  [vgl.  Schack, Poesie  und  Kunst  der  Araber  in  Spanien und  Sizilien.  ^.  II,  266/269].  —  [Mög- licherweise geht  das  ar.  Grundwort  selbst auf  pers.  gunbäd  zurück,  ZDMG  L,  646.] [Kluge  11.  DE  90/91.  95.  Eguilaz  131. Devic  DEt  14.  Lammens  Rem  8.  ML 6909.  Hobson-Jobson  11/12.  Gorjajew 4  und  139.  Bern  SlEtWb  635.  GrS VociSic  232/233.
LKT.txt:3790:'Führer,  Zuhälter'  [aus  pers.  pes  'zuerst' Horn  NpEt  S.  79,  Nr.  356  und  ähäng. Präsensstamm  zu  ahängldän  'ziehen' ebenda  S.  14,  Nr.  58],  tk.  umgestaltet zu  pezeivenk  'dass.'  [Kelekian  Kämüs 321  b];  hieraus  rum.  pezeoenchm  'Kupp- ler', pezevenche  'Kupplerin',  pecevenclic 'Kuppelei'.
HUB.txt:3116:Bogen, Kuppel, Halle* = gr. Kajudga (xa^idgtj schon
HUB.txt:9123:Gl. 154, phi. pambak Bdh. 65, 10; gmbef 'Kuppel* = np.
AFA.txt:9596:lASiO >Ei** dann »Kuppel" entspricht arabischem L^Ij ,
```


## [2026-09-05T20:59:02.314Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '9118,9130p' HUB.txt; echo \"=== HUB gōn / gōše\"; grep -n \"gūn\\|gōn 'Farbe\\|gôn\" HUB.txt | head -10"
}
```


## [2026-09-05T20:59:02.337Z] TOOL CALL #67: ToolSearch

```json
{
 "query": "select:WebSearch,WebFetch",
 "max_results": 3
}
```


### [2026-09-05T20:59:02.342Z] TOOL RESULT

```


```


### [2026-09-05T20:59:02.382Z] TOOL RESULT

```
Lehnworter haben gleichfalls n fiir urspr. m, aber m vor 6,
das im Arm. bilabial war: ambar 'Speicher, amharem ich
speichere auf, hambar Speicher'; ambox *Menge, Volk* =
np. anboh; stambak 'streng, tyrannisch, widerspenstig* = np.
sitanba; bambak 'Baumwolle' = np. panba, paz. panba Min.
Gl. 154, phi. pambak Bdh. 65, 10; gmbef 'Kuppel* = np.
gmibad (syr. LW., Noldeke, Pers. Stud. II, 41); smpatak
Triifstein* = np. sunbada, arab. stmbadaj u. s. w. ; angam
-nial = np. hangam 'Zeit'; angarem Vechne an == np. an-
garam; andacem *untersuche' , np. andaz *Plan'; andam
*Glied* = np. andam; andarj 'Testament* = np. andarz
*Uath, Testament'.
Dagegen bleibt m in ham- *derselbe, der gleiche* =
=== HUB gōn / gōše
```


## [2026-09-05T20:59:10.070Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('HUB.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n'); leaf=0;m={}\nfor i,l in enumerate(lines,1):\n    m[i]=leaf; leaf+=l.count('\\f')\nprint(9123,'leaf',m[9123],'printed',m[9123]-10)\nEOF"
}
```


## [2026-09-05T20:59:10.816Z] TOOL CALL #69: Bash

```json
{
 "command": "for u in \"https://www.etymonline.com/word/kiosk\" \"https://www.etymonline.com/word/zircon\" \"https://www.etymonline.com/word/gyro-\" ; do python3 tools/fetch_source.py \"$u\" --note \"page 176: kiosk/zircon/gyro chains\" ; done"
}
```


### [2026-09-05T20:59:11.852Z] TOOL RESULT

```
9123 leaf 265 printed 255
```


### [2026-09-05T20:59:14.981Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/f2e81b4d8a39c5f3.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/33235a6910a8d53c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/3b0edf0f4a2bc11d.txt
```


## [2026-09-05T20:59:17.701Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in f2e81b4d8a39c5f3 33235a6910a8d53c 3b0edf0f4a2bc11d; do echo \"======= $f\"; grep -v \"^ *$\" $f.txt | sed -n '5,40p'; done"
}
```


### [2026-09-05T20:59:19.649Z] TOOL RESULT

```
======= f2e81b4d8a39c5f3
Kiosk - Etymology, Origin & Meaning 
 Search 
 Log in 
 Columns 
 Forum 
 Apps 
 Premium 
 Log in 
 Advertisement Remove Ads 
 Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.
 Origin and history of kiosk 
 kiosk (n.) 
 1620s, "kind of open pavilion" (made of light wood, etc., often supported by pillars), from French kiosque (17c.), which is (along with German and Polish kiosk ) from Turkish koshk , kiöshk "pavilion, summer house," from Persian kushk "palace, villa; pavilion, portico." They were introduced in Western Europe 17c. as ornaments in gardens and parks. Later of street newsstands (1865), on some resemblance of shape, a sense perhaps originally in French. Modern sense has been influenced by British telephone kiosk (1928).
 also from 1620s 
 Advertisement Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.
 More to explore
 booth 
 c. 1200, mid-12c. in place-names, "temporary structure of boards, etc.," especially a stall for the sale of goods or food or entertainment, at a fair, etc., from Old Danish boþ "temporary dwelling," from East Norse *boa "to dwell," from Proto-Germanic *bowan-, from PIE root *bheu
 cubicle 
 mid-15c., "bedroom, bedchamber," from Latin cubiculum "bedroom," from cubare "to lie down," which is perhaps from a PIE *kub-, with cognates in Middle Welsh kyscu, Middle Cornish koska, Middle Breton cousquet "to sleep," but de Vaan regards the PIE origin of the Latin word as "un
 stall 
 [place in a stable for animals] Middle English stalle, from Old English steall "standing place, any fixed place or position, state; place where cattle are kept, stable; fishing ground," from Proto-Germanic *stalli- (source also of Old Norse stallr "pedestal for idols, altar; crib
 closet 
 late 14c., "a small private room for study or prayer," from Old French closet "small enclosure, private room," diminutive of clos "enclosure," from Latin clausum "closed space, enclosure, confinement," from neuter past participle of claudere "to shut" (see close (v.)). In Matthew
 telephone 
 1835, "system for conveying words over distance by musical notes" (devised in 1828 by French composer Jean-François Sudré (1787-1862); each tone played over several octaves represented a letter of the alphabet), from French téléphone (c. 1830), from télé- "far" (see tele-) + phōn
 pilgrim 
 c. 1200, pilegrim, "a person traveling to a holy place (as a penance or to discharge some vow or religious obligation, or seeking some miracle or spiritual benefit)," also "a traveler" generally, "a wayfarer," from Old French pelerin, peregrin "pilgrim, crusader; foreigner, stran
 fascinate 
 1590s, "bewitch, enchant," from French fasciner (14c.), from Latin fascinatus, past participle of fascinare "bewitch, enchant, fascinate," from fascinus "a charm, enchantment, spell, witchcraft," which is of uncertain origin. Earliest used of witches and of serpents, who were sai
 race 
 [act of running] late Old English, also rase, "a narrative, an account;" c. 1300, "an act of swift running, a hurried attack," also "a course of life or conduct, a swift current;" from Old Norse rās "a running, a rush (of water)," cognate with Old English ræs "a running, a rush, 
 addiction 
 c. 1600, "tendency, inclination, penchant" (a less severe sense now obsolete); 1640s as "state of being (self)-addicted" to a habit, pursuit, etc., from Latin addictionem (nominative addictio) "an awarding, a delivering up," noun of action from past-participle stem of addicere "t
 war 
 late Old English wyrre, werre "large-scale military conflict," from Old North French werre "war" (Old French guerre "difficulty, dispute; hostility; fight, combat, war;" Modern French guerre), from Frankish *werra, from Proto-Germanic *werz-a- (source also of Old Saxon werran, Ol
======= 33235a6910a8d53c
Zircon - Etymology, Origin & Meaning 
 Search 
 Log in 
 Columns 
 Forum 
 Apps 
 Premium 
 Log in 
 Advertisement Remove Ads 
 Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.
 Origin and history of zircon 
 zircon (n.) 
 yellowish mineral occurring in crystal form, 1794, circon , also jargon , a new name given in chemistry to jacinth , from German Zirkon (Klaproth, 1789), which probably is from 18c. French jargon , a vague mineral word used of high-quality diamond-like gemstones.
 This has been traced to Medieval Latin jargonce , which is of uncertain origin. Compare Italian giargone , from the same source. Century Dictionary suggests Arabic zarkun "cinnabar." Related: Zirconic ; zirconian ; zirconate .
 also from 1794 
 Entries linking to zircon 
 jacinth (n.) 
 c. 1200, iacinct , a blue gem (occasionally a red one), from Old French jacinte , iacinte "hyacinth; jacinth," or directly from Late Latin iacintus (see hyacinth ).
 In modern use, a reddish-orange gem. The word is hyacinth with the h- lost and the initial -i- made consonantal (forms in j- begin to be attested late 14c.; see J ).
 zirconium (n.) 
 metallic chemical element, 1808, coined in Modern Latin by German chemist and mineralogist Martin Heinrich Klaproth (1743-1817) in 1789; so called because it was obtained from zircon . With -ium , name-ending of metallic elements.
 Advertisement Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.
 More to explore
 mineral 
 late 14c., "substance obtained by mining," from Old French mineral and directly from Medieval Latin minerale "something mined," noun use of neuter of mineralis "pertaining to mines," from minera "a mine" (see mine (n.1)). Meaning "material substance that is neither animal nor veg
 hyacinth 
 1550s, "the plant hyacinth;" re-Greeked from jacinth (late 14c.) "hyacinth; blue cornflower," which earlier was the name of a precious stone blue (rarely red) in color (c. 1200), from Old French jacinte and Medieval Latin jacintus, ultimately from Greek hyakinthos, which is proba
 jargon 
 mid-14c., "unintelligible talk, gibberish; chattering, jabbering," from Old French jargon "a chattering" (of birds), also "language, speech," especially "idle talk; thieves' Latin" (12c.). Ultimately of echoic origin (compare Latin garrire "to chatter"). From 1640s as "mixed spee
 nightcap 
 also night-cap, late 14c., "covering for the head, worn in bed," from night + cap (n.). In the alcoholic sense, it is attested from 1818. American English sense of "final event in a sporting contest" (especially the second game of a baseball double-header) is by 1924. Sunday's b
 precipitate 
 1520s, "to hurl or fling down" (from a precipice or height), a back formation from precipitation or else from Latin praecipitatus, past participle of praecipitare "to throw or dive headlong; be hasty," from praeceps (genitive praecipitis) "steep, headlong, headfirst," from prae "
 Mississippi 
 originally the name of the river, from the French rendering of an Algonquian name (French missionaries first penetrated the river valley in its upper reaches) meaning "big river;" compare Ojibwa mshi- "big," ziibi "river." Organized as a U.S. territory 1798; admitted as a state 1
 cipher 
======= 3b0edf0f4a2bc11d
Gyro- - Etymology & Meaning of the Prefix 
 Search 
 Log in 
 Columns 
 Forum 
 Apps 
 Premium 
 Log in 
 Advertisement Remove Ads 
 Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.
 Origin and history of gyro- 
 gyro- 
 word-forming element meaning "gyrating" or "gyroscope," from Greek gyros "a ring, circle" (see gyre (n.)).
 Entries linking to gyro- 
 gyre (n.) 
 1560s, "a circular motion," from Latin gyrus "circle, circular course, round, ring," from Greek gyros "a circle, ring," related to gyrós "rounded," perhaps from PIE root *geu- "to bend, curve" (source also of Armenian kor "crooked," Lithuanian gurnas "hip, ankle, bone," Norwegian kaure "a curly lock of hair"). The noun is attested in Middle English only in reference to ship's tackle (early 15c.).
 gyrocopter (n.) 
 1915, from gyro- + ending as in helicopter .
 gyromancy 
 gyrostat 
 See All Related Words (4) 
 Advertisement Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.
 More to explore
 matrix 
 late 14c., matris, matrice, "uterus, womb," from Old French matrice "womb, uterus" and directly from Latin mātrix (genitive mātricis) "pregnant animal," in Late Latin "womb," also "source, origin," from māter (genitive mātris) "mother" (see mother (n.1)). The many figurative and 
 drone 
 Middle English drane, drone, "male honeybee," from Old English dran, dræn, from Proto-Germanic *dran- (source also of Middle Dutch drane; Old High German treno; German Drohne, which is from Middle Low German drone), probably imitative (compare Lithuanian tranni, Greek thronax "a 
 catharsis 
 1770, "a bodily purging" (especially of the bowels), from Latinized form of Greek katharsis "purging, cleansing," from stem of kathairein "to purify, purge," from katharos "pure, clear of dirt, clean, spotless; open, free; clear of shame or guilt; purified" (with most of the exte
 compass 
 c. 1300, "space, area, extent, circumference," from Old French compas "circle, radius; size, extent; pair of compasses" (12c.), from compasser "to go around, measure (with a compass); divide equally," from Vulgar Latin *compassare "to pace out," from Latin com "with, together" (s
 derogatory 
 c. 1500, "detracting or tending to lessen authority, rights, or standing by taking something away from," from Late Latin derogatorius, from Latin derogatus, past participle of derogare "to take away, detract from, diminish," also "repeal partly, restrict, modify," from de "away" 
 crestfallen 
 "dejected, dispirited," 1580s, creast falne, it has the form of a past-participle adjective, but the verb crestfall is recorded only from 1610s, in reference to diseased horses, and is rare. It's possible that the image behind this use of the word is not having the crest fallen, 
 retreat
```


## [2026-09-05T20:59:34.922Z] TOOL CALL #71: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/%DA%A9%DB%8C%D9%88%D8%B3%DA%A9\" \\\n \"https://en.wiktionary.org/wiki/k%C3%B6%C5%9Fk\" \\\n \"https://en.wiktionary.org/wiki/%D9%82%D9%88%D8%B2\" \\\n \"https://en.wiktionary.org/wiki/%DA%AF%D9%86%D8%AF%D9%87\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/gauna\" \\\n \"https://en.wiktionary.org/wiki/%DA%AF%D9%88%D8%B4\" ; do python3 tools/fetch_source.py \"$u\" --note \"page 176 Geu/Keu chart nodes\" ; done"
}
```


### [2026-09-05T20:59:40.188Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/7bb90c993bfa2c6b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/7a1689460c38a6c5.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f6f7a1208dd6078f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/5e602aba1e7fd0ae.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e70868e6140df01f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/016fa974d84963b0.txt
```


## [2026-09-05T20:59:43.973Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in 7bb90c993bfa2c6b 7a1689460c38a6c5 f6f7a1208dd6078f 5e602aba1e7fd0ae e70868e6140df01f 016fa974d84963b0; do echo \"======= $f\"; grep -v \"^ *$\" $f.txt | grep -n -B2 -A8 \"^ Etymology$\\|^ Etymology 1$\\|Borrowed from\\|Inherited from\\|From Middle Persian\\|From Proto\" | head -40; done"
}
```


### [2026-09-05T20:59:46.338Z] TOOL RESULT

```
======= 7bb90c993bfa2c6b
80- Persian
81- [ edit ] 
82: Etymology
83- [ edit ] 
84- Etymology tree
85- Middle Persian kwšk' ( kōšk ) bor. 
86- Classical Persian کوشْک ( kōšk ) bor. 
87- Ottoman Turkish كوشك ( köşk ) bor. 
88- Italian chiosco bor. 
89- French kiosque bor. 
90- Persian کیوسک 
91: Borrowed from French kiosque . Doublet of کوشْک .
92- Noun
93- [ edit ] 
94- کیوسک • ( kiyusk ) ( plural کیوسک‌ها ) 
95- kiosk 
96- Retrieved from " https://en.wiktionary.org/w/index.php?title=کیوسک&oldid=92021092 "
97- Categories : Persian terms derived from Classical Persian 
98- Persian terms derived from Middle Persian 
99- Persian terms derived from Italian 
======= 7a1689460c38a6c5
120- Azerbaijani
121- [ edit ] 
122: Etymology
123- [ edit ] 
124: Borrowed from Classical Persian کوشک ( “ palace, portico ” ) .
125- Pronunciation
126- [ edit ] 
127- IPA ( key ) : [cœʃc] 
128- Noun
129- [ edit ] 
130- köşk ( definite accusative köşkü , plural köşklər ) 
131- arbor , gazebo , pavilion ( a shady place for sitting ) 
132- kiosk 
--
138- Turkish
139- [ edit ] 
140: Etymology
141- [ edit ] 
142- From Ottoman Turkish كوشك ( köşk ) , from Classical Persian کوشْک ( kōšk , “ palace, portico ” ) . Cognate with English kiosk .
143- Pronunciation
144- [ edit ] 
145- IPA ( key ) : /cøʃc/ 
146- Noun
147- [ edit ] 
148- köşk ( definite accusative köşkü , plural köşkler ) 
--
184- Turkmen
185- [ edit ] 
186: Etymology
187- [ edit ] 
188: Borrowed from Classical Persian کوشْک ( kōšk , “ palace, portico ” ) .
189- Noun
190- [ edit ] 
191- köşk ( definite accusative köşgi , plural köşkler ) 
192- palace 
193- kiosk 
194- Declension
195- [ edit ] 
196- Declension of köşk 
======= f6f7a1208dd6078f
107- [ edit ] 
108- قوز 
109: Etymology
110- [ edit ] 
111- Iranian borrowing, see Old Armenian ընկոյզ ( ənkoyz ) for more.
112- Noun
113- [ edit ] 
114- قوز • ( qwz / qoz /) ( plural قوزلار ) 
115- walnut ( a nut of the walnut tree ) 
116- Derived terms
117- [ edit ] 
--
127- coz ( Latin ) 
128- խօզ ( xōz ) ( Armenian ) 
129: Etymology
130- [ edit ] 
131- Iranian borrowing, see Old Armenian ընկոյզ ( ənkoyz ) for more.
132- Noun
133- [ edit ] 
134- قوز ( koz ) 
135- walnut 
136- Descendants
137- [ edit ] 
--
141- Ottoman Turkish
142- [ edit ] 
143: Etymology
144- [ edit ] 
145- From Romanian coz ( “ trump ” ) , clipped from Russian ко́зырь ( kózyrʹ , “ trump ” ) , from Polish kozyr , see the Russian for more.
146- Noun
147- [ edit ] 
148- قوز • ( koz ) 
149- ( card games ) trump 
150- Descendants
151- [ edit ] 
======= 5e602aba1e7fd0ae
102- Persian
103- [ edit ] 
104: Etymology 1
105- [ edit ] 
106: From Middle Persian [script needed] ( gndk' /⁠gandag⁠/ , “ foul, stinking ” ) , from Proto-Indo-Iranian *g(ʰ)andʰ- ( “ to smell ” ) ; see Sanskrit गन्ध ( gandhá ) for more. [ 1 ] 
107- Pronunciation
108- [ edit ] 
109- ( Classical Persian ) IPA ( key ) : /ɡan.ˈda/ 
110- ( Dari, formal ) IPA ( key ) : [ɡän̪.d̪ä] 
111- ( Dari, formal ) IPA ( key ) : [ɡän̪.d̪ä] 
112- ( Kabuli ) IPA ( key ) : [ɡän̪.d̪ä] 
113- ( Hazaragi ) IPA ( key ) : [ɡän̪.d̪ä] 
114- ( Iran, formal ) IPA ( key ) : [ɡʲæn̪.d̪e] 
======= e70868e6140df01f
======= 016fa974d84963b0
118- Baluchi
119- [ edit ] 
120: Etymology
121- [ edit ] 
122: From Proto-Iranian *gáwšah , from Proto-Indo-Iranian *gʰáwšas . Cognate with Persian گوش ( gôš ) .
123- Noun
124- [ edit ] 
125- گوش • ( goš ) 
126- ear 
127- Persian
128- [ edit ] 
129- Persian Wikipedia has an article on: گوش 
130- Wikipedia fa 
--
144- Click on labels in the image
145- body 
146: Etymology
147- [ edit ] 
148- Etymology tree
149- Proto-Indo-Iranian *gʰáwšas 
150- Proto-Iranian *gáwšah 
151- Old Persian 𐎥𐎢𐏁 ( g-u-š ) 
152- Middle Persian 𐭢𐭥𐭱 ( gʿš ) 
153- Persian گوش 
154: Inherited from Middle Persian 𐭢𐭥𐭱 ( gʿš /⁠gōš⁠/ ) , from Old Persian 𐎥𐎢𐏁 ( g-u-š /⁠gauša⁠/ , “ ear ” ) , from Proto-Iranian *gáwšah , from Proto-Indo-Iranian *gʰáwšas , from Proto-Indo-European *gʰows- ( “ hear ” ) .
155- Indo-Iranian cognates include: Avestan 𐬔𐬀𐬊𐬱𐬀 ( gaoša ) , Baluchi گوش ( goš ) , Northern Kurdish guh , Ossetian хъус ( qus ) / гъос ( ǧos ) , Sanskrit घोष ( ghoṣa ) . Also compare Old Armenian գոյշ ( goyš ) , an Iranian borrowing.
156- Pronunciation
157- [ edit ] 
158- ( Classical Persian ) IPA ( key ) : /ˈɡoːʃ/ 
159- ( Dari, formal ) IPA ( key ) : [ɡoːʃ] 
160- ( Dari, formal ) IPA ( key ) : [ɡoːʃ] 
161- ( Kabuli ) IPA ( key ) : [ɡoːʃ] 
162- ( Hazaragi ) IPA ( key ) : [ɡʊːʃ]
```


## [2026-09-05T21:00:03.497Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"== گنده sections\"; grep -n \"Etymology 2\\|Etymology 3\" -A10 5e602aba1e7fd0ae.txt | grep -v \"^ *$\" | head -30; echo \"== قوز persian?\"; grep -n \"Persian\" f6f7a1208dd6078f.txt | head"
}
```


### [2026-09-05T21:00:05.235Z] TOOL RESULT

```
== گنده sections
86: Etymology 2 
87-
88- 1.2.1 
89- Pronunciation 
90-
91- 1.2.2 
92- Adjective 
93-
94- Toggle the table of contents 
95-
96- گنده 
--
249: Etymology 2
250- [ edit ] 
251-
252- (This etymology is missing or incomplete. Please add to it, or discuss it at the Etymology scriptorium .) 
253-
254- Pronunciation
255- [ edit ] 
256-
257- ( Iran ) IPA ( key ) : [ɡonˈd̪e] 
258-
259- Adjective
== قوز persian?
```


## [2026-09-05T21:00:05.344Z] TOOL CALL #74: Bash

```json
{
 "command": "for u in \"https://en.wiktionary.org/wiki/%DA%A9%D9%88%DA%98\" \"https://en.wiktionary.org/wiki/%D9%82%D9%88%D8%B2%DA%A9\" \"https://www.ahdictionary.com/word/search.html?q=zircon\" ; do python3 tools/fetch_source.py \"$u\" --note \"page 176 nodes 13,19\" ; done"
}
```


### [2026-09-05T21:00:09.045Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/54cda20fd419efec.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e276544c1a9bde49.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ef890fa9527721ba.txt
```


## [2026-09-05T21:00:14.099Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in 54cda20fd419efec e276544c1a9bde49 ef890fa9527721ba; do echo \"======= $f\"; grep -v \"^ *$\" $f.txt | sed -n '1,10p'; grep -n -A10 \" Etymology\" $f.txt | grep -v \"^ *$\" | head -25; done"
}
```


### [2026-09-05T21:00:15.571Z] TOOL RESULT

```
======= 54cda20fd419efec
URL: https://en.wiktionary.org/wiki/%DA%A9%D9%88%DA%98
FETCHED: 2026-09-05T21:00:08Z
STATUS: 200
TITLE: کوژ - Wiktionary, the free dictionary
کوژ - Wiktionary, the free dictionary 
 Jump to content 
 Main menu 
 Main menu
 move to sidebar 
 hide 
62: Etymology 1 
63-
64- 1.1.1 
65- Alternative forms 
66-
67- 1.1.2 
68- Adjective 
69-
70- 1.2 
71: Etymology 2 
72-
73- 1.2.1 
74- Noun 
75-
76- 1.2.1.1 
77- Descendants 
78-
79- 1.3 
80- References 
81-
--
150: Etymology 1
151- [ edit ] 
152-
153- Compare کژ ( kaž , “ crooked ” ) .
======= e276544c1a9bde49
URL: https://en.wiktionary.org/wiki/%D9%82%D9%88%D8%B2%DA%A9
FETCHED: 2026-09-05T21:00:08Z
STATUS: 200
TITLE: قوزک - Wiktionary, the free dictionary
قوزک - Wiktionary, the free dictionary 
 Jump to content 
 Main menu 
 Main menu
 move to sidebar 
 hide 
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Noun 
69-
70- 1.4 
71- Further reading 
72-
--
138: Etymology
139- [ edit ] 
140-
141- From قوز ( quz , “ hump ” ) +‎ ـک ( -ak , diminutive suffix ) .
142-
143- Pronunciation
144- [ edit ] 
145-
146- ( Classical Persian ) IPA ( key ) : /quː.ˈzak/ 
147-
148- ( Dari, formal ) IPA ( key ) : [quː.zák] 
======= ef890fa9527721ba
URL: https://www.ahdictionary.com/word/search.html?q=zircon
FETCHED: 2026-09-05T21:00:09Z
STATUS: 200
TITLE: American Heritage Dictionary Entry: zircon
American Heritage Dictionary Entry: zircon 
 HOW TO USE THE DICTIONARY
 To look up an entry in The American Heritage Dictionary of the English Language, use the search window above. For best results, after typing in the word, click on the “Search” button instead of using the “enter” key.
 Some compound words (like bus rapid transit, dog whistle, or identity theft ) don’t appear on the drop-down list when you type them in the search bar. For best results with compound words, place a quotation mark before the compound word in the search window.
 guide to the dictionary 
 THE USAGE PANEL
```


## [2026-09-05T21:00:19.377Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && grep -n -i \"zircon\" ef890fa9527721ba.txt | head -20; echo \"=== کوژ etym2\"; grep -n -A12 \"Etymology 2\" 54cda20fd419efec.txt | grep -v \"^ *$\" | sed -n '10,40p'"
}
```


### [2026-09-05T21:00:21.127Z] TOOL RESULT

```
1:URL: https://www.ahdictionary.com/word/search.html?q=zircon
4:TITLE: American Heritage Dictionary Entry: zircon
6:American Heritage Dictionary Entry: zircon 
48: [German Zirkon (originally in obsolete scientific German Zirkonerde , zirconium oxide, coined by German chemist Martin Heinrich Klaproth (1743-1817), who first isolated it from a jacinth), probably partly from Arabic zarq ū n , minium, bright red (from Persian zarg ū n , gold-colored, from Middle Persian zarg ō n , golden : zarr, zar- , golden from Old Iranian, *zarna- ; see ghel- 2 in the Appendix of Indo-European roots + g ō n , color, from Old Iranian *gaona- ; akin to Sanskrit gu ṇ a ḥ , string, thread, quality), and partly from European terms for "jacinth" such as French jargon (from Old French jargonce , ultimately from Latin hyacinthus ; see HYACINTH ).]
=== کوژ etym2
80- References 
81-
82- Toggle the table of contents 
83-
--
169: Etymology 2
170- [ edit ] 
171-
172- Compare غوره ( ġure , “ unripe grapes ” ) .
173-
174- Noun
175- [ edit ] 
176-
177- کوژ • ( kewž, kuviž ) 
178-
179- ( obsolete ) fruit of the medlar 
180-
181- Descendants
```


## [2026-09-05T21:00:36.479Z] TOOL CALL #77: Bash

```json
{
 "command": "ls site/pages/176.jpg 2>/dev/null; pdftoppm -f 176 -l 176 -r 200 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg176 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/"
}
```


### [2026-09-05T21:00:38.843Z] TOOL RESULT

```
site/pages/176.jpg
total 23680
drwx------ 2 sfmqrb sfmqrb    4096 Sep  5 17:00 .
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
-rw-rw-r-- 1 sfmqrb sfmqrb    7816 Sep  5 16:35 c_am2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   14765 Sep  5 16:35 c_am3.png
-rw-rw-r-- 1 sfmqrb sfmqrb   10038 Sep  5 16:35 c_empty2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4123 Sep  5 16:34 crop_am.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4986 Sep  5 16:34 crop_arabic_refs.png
-rw-rw-r-- 1 sfmqrb sfmqrb    7702 Sep  5 16:34 crop_empty.png
-rw-rw-r-- 1 sfmqrb sfmqrb   16978 Sep  5 16:34 crop_morocco.png
-rw-rw-r-- 1 sfmqrb sfmqrb  163996 Sep  5 16:46 gar2.png
-rw-rw-r-- 1 sfmqrb sfmqrb  124975 Sep  5 16:47 gar3.png
-rw-rw-r-- 1 sfmqrb sfmqrb   77205 Sep  5 16:46 gar.png
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
-rw-rw-r-- 1 sfmqrb sfmqrb    2692 Sep  5 16:49 n16.png
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
-rw-rw-r-- 1 sfmqrb sfmqrb   54907 Sep  5 16:54 pg175.png
-rw-rw-r-- 1 sfmqrb sfmqrb   83583 Sep  5 17:00 pg176.png
-rw-rw-r-- 1 sfmqrb sfmqrb   57139 Sep  5 16:54 pg179.png
-rw-rw-r-- 1 sfmqrb sfmqrb   81598 Sep  5 16:58 pg180.png
-rw-rw-r-- 1 sfmqrb sfmqrb   56794 Sep  5 17:00 pg181.png
-rw-rw-r-- 1 sfmqrb sfmqrb   77310 Sep  5 16:58 pg184.png
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


## [2026-09-05T21:00:41.938Z] TOOL CALL #78: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg176.png"
}
```


### [2026-09-05T21:00:42.321Z] TOOL RESULT

```

```


## [2026-09-05T21:00:42.320Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-05T21:00:57.322Z] TOOL CALL #79: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && pdftoppm -f 176 -l 176 -r 600 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf p176hi && python3 -c \"\nfrom PIL import Image\nim=Image.open('p176hi.png'); print(im.size)\nw,h=im.size\n# node14 box approx at x 1075-1190/1545, y 1000-1075/2000 in displayed coords\nim.crop((int(1050/1545*w),int(995/2000*h),int(1200/1545*w),int(1085/2000*h))).resize((900,540)).save('n14.png')\nim.crop((int(720/1545*w),int(1280/2000*h),int(1200/1545*w),int(1380/2000*h))).save('n19.png')\n\"; ls -la n14.png n19.png"
}
```


### [2026-09-05T21:01:14.881Z] TOOL RESULT

```
(5100, 6600)
-rw-rw-r-- 1 sfmqrb sfmqrb 24939 Sep  5 17:01 n14.png
-rw-rw-r-- 1 sfmqrb sfmqrb  7472 Sep  5 17:01 n19.png
```


## [2026-09-05T21:01:17.311Z] TOOL CALL #80: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/n14.png"
}
```


### [2026-09-05T21:01:17.329Z] TOOL RESULT

```

```


## [2026-09-05T21:01:30.924Z] TOOL CALL #81: Bash

```json
{
 "command": "sed -n 1,80p tools/ref_page.py"
}
```


### [2026-09-05T21:01:30.960Z] TOOL RESULT

```
#!/usr/bin/env python3
"""Fetch ONE cited page of a scanned reference, on demand.

    python3 tools/ref_page.py BQT:918          # printed page 918 of Borhan-e Qate'
    python3 tools/ref_page.py IRN:119 --image  # also print the path of the page image
    python3 tools/ref_page.py BQT:918 --pdf-page 375   # override the offset mapping

Looks up the reference in data/verification/sources/refs_online.json
(`scans`: list of {file, first_printed, last_printed, pdf_offset, lang}), renders the
matching PDF page to PNG (for reading with a vision model), OCRs it with tesseract in
the reference's language(s), caches both under
data/verification/sources/refs/ocr/<ABBR>/<printed page>.{png,txt}, and prints the
OCR text. Only the cited page is ever processed — never the whole book.

`pdf_offset` means: pdf page index (1-based) = printed page + pdf_offset.

If the OCR is too poor and you transcribe the relevant passage(s) from the PNG yourself,
save that transcription as <printed page>.vision.txt next to the .txt; from then on this
tool prints the transcription instead of the OCR, so no page is ever read twice.
"""
import sys, os, json, subprocess, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "data", "verification", "sources")
TABLE = os.path.join(SRC, "refs_online.json")
REFS = os.path.join(SRC, "refs")
OCR = os.path.join(REFS, "ocr")
TESSDATA = os.path.join(REFS, "tessdata")


def main(argv):
    args = [a for a in argv if not a.startswith("--")]
    if not args:
        print(__doc__); return 2
    m = re.match(r"^([A-Z]+)(\d*):(\d+)$", args[0])
    if not m:
        print("expected ABBR:page (e.g. BQT:918 or MON5:528)"); return 2
    abbr, vol, page = m.group(1), m.group(2), int(m.group(3))
    table = json.load(open(TABLE, encoding="utf-8"))
    ref = table.get(abbr, {})
    scans = ref.get("scans") or []
    if vol:
        scans = [s for s in scans if str(s.get("volume", "")) == vol] or scans
    scan = None
    for s in scans:
        if s.get("requires_volume") and not vol:
            continue
        if s.get("first_printed", 0) <= page <= s.get("last_printed", 10**9):
            scan = s; break
    if "--pdf-page" in argv:
        pdf_page = int(argv[argv.index("--pdf-page") + 1])
        scan = scan or (scans[0] if scans else None)
    elif scan:
        pdf_page = None
        pm = scan.get("page_map")
        if pm and os.path.exists(pm):
            pdf_page = json.load(open(pm)).get("map", {}).get(str(page))
        if pdf_page is None:
            pdf_page = page + int(scan.get("pdf_offset", 0))
            print(f"(no exact page map; using offset {scan.get('pdf_offset', 0)} -> pdf page {pdf_page}; check the printed number and re-run with --pdf-page if off)")
    else:
        print(f"no scan of {abbr} covers printed page {page} (see 'scans' in refs_online.json)"); return 1
    pdf = scan["file"] if os.path.isabs(scan["file"]) else os.path.join(REFS, scan["file"])
    if not os.path.exists(pdf):
        print("PDF not found:", pdf); return 1
    lang = scan.get("lang", "fas")
    out_dir = os.path.join(OCR, abbr + vol)
    os.makedirs(out_dir, exist_ok=True)
    base = os.path.join(out_dir, f"{page:04d}")
    png, txt = base + ".png", base + ".txt"
    if not os.path.exists(png):
        subprocess.run(["pdftoppm", "-f", str(pdf_page), "-l", str(pdf_page), "-r", "300", "-png", "-singlefile", pdf, base], check=True)
    if not os.path.exists(txt):
        # try the PDF's own text layer first; fall back to tesseract
        r = subprocess.run(["pdftotext", "-layout", "-f", str(pdf_page), "-l", str(pdf_page), pdf, "-"], capture_output=True, text=True)
        text = r.stdout if len(r.stdout.strip()) > 80 else ""
        if not text:
            env = dict(os.environ, TESSDATA_PREFIX=TESSDATA)
            r = subprocess.run(["tesseract", png, "-", "-l", lang, "--psm", "6"], capture_output=True, text=True, env=env)
            text = r.stdout
```


## [2026-09-05T21:01:34.409Z] TOOL CALL #82: Bash

```json
{
 "command": "ls data/verification/sources/refs/ocr/ 2>/dev/null; echo \"--- BQT scans:\"; python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'));print(json.dumps(d['BQT'].get('scans'),ensure_ascii=False,indent=1))\""
}
```


### [2026-09-05T21:01:37.500Z] TOOL RESULT

```
AFM
ARY
BOOK
BQT
HRN
IRN
PLA
SNS
SOD
--- BQT scans:
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


## [2026-09-05T21:02:02.392Z] TOOL CALL #83: Bash

```json
{
 "command": "python3 - <<'EOF'\nimport json,re\npm=json.load(open('data/verification/sources/refs/incoming/BQT/BQT_v3_pagemap.json'))\nm=pm.get('map',pm)\nfor p in ('1731','1836','1843','1859','1861'):\n    print(p,'->pdf',m.get(p))\nEOF"
}
```


### [2026-09-05T21:02:04.244Z] TOOL RESULT

```
1731 ->pdf 528
1836 ->pdf 633
1843 ->pdf 640
1859 ->pdf None
1861 ->pdf None
```


## [2026-09-05T21:02:07.858Z] TOOL CALL #84: Bash

```json
{
 "command": "python3 - <<'EOF'\nimport re\nt=open('data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nidx={}\nfor p in pages:\n    m=re.search(r'\\[pdf page (\\d+)\\]',p)\n    if m: idx[int(m.group(1))]=p\nfor n in (528,633,640):\n    p=idx.get(n)\n    print('==== pdf',n, 'len', len(p) if p else None)\n    if p: print(p[:1500])\nEOF"
}
```


### [2026-09-05T21:02:09.675Z] TOOL RESULT

```
==== pdf 528 len 2471
[pdf page 528]
-۱۷۳۱-

احتلام و ثیطالی شدن هم بنظر آمده است -
یز کنته‌اند « و آن گرانبی
باشد که در خواب برمردم افتد - و ‎pel‏ نیز
کویند که هئوز خطش ندمیده باشد ؛ و باین
معنی و پمعنی احتلام ‎GEL‏ و بای فارسی هم
آمده است .

‎OLS‏ -بروزن جوثان .کوتش
وسمی وجهد کننده راگویند ۴

‏کوشش ۴« با نانی مجهول ‎Olay‏
‏پوشش » بمعنی سعی و چهد - و جنگه و جدل
باشد ۴ .

‏کوشك ینم اول وفتح ‎AE‏ بروزن
موشك , بمعن ی کوچك باشد ۵ - و مردم کوچك
اندام را نیز گوبنده و مدرب ‎OT‏ قوذق است -
وبسکون ‎elt‏ بنای بلند را گویند و بمربی‌قص
خوانند ‎٩‏

‏وکابوی وعبدالجته را

‏کوف
‏کوشکنچیر ۷ - بن اول ‎Sei,‏

‏دویم ؛ بمعنی کشکنجیر است که سنگه منجنیق
‎UIT,‏ توپ باشد. ووجه :سمیٌآآن کوشك‌انجیر
است یمنی کوشك سوراخ کن چه الجیر بمعنی
‎tla‏ هم‌آمده است .

‎OT‏ = بروزن توشه ‎geet‏ کوشیده
و سعی وجهد نموده ۸ بدست آورده باشد ۸ .
‎Seg‏ ۰ , وزن‌هوشیار»امعکمی

‏ت از ‎OUT‏ و بعضی گویند نام حکیمی

‎aay‏ است از فاری و شیخ ابوعلی سینا شاگردی
او کرده است *۱؛ و با کاف فارسی هم آمده
است .#۴

‎ES‏ © بر وزن دوغ ۰ بمعنی درون
شدن واندرون رفتن باشد ۱۱.

‎SST‏ = بر وزن صوف ۰ پرنده ایست
بنهوست مشهو رکه آنرا بوم و چفد نیز کویند

‏بوده است

‏- از : کوش ( کوشیدن )+ ان ( پسوند صفت فاعلی ) .

‏۴ - یزه کوشان » نام قومی‌است ‎Dy.‏ : کشان . - از : کوش (کوشیدن) +
ش ( پنولد اسم مصدر ) ‎Hy.‏ : کوشیدن .
۴ - یراکنده + شد ترك سیصد هزار ‎gles‏ نبد کوشش و کارزار .

‏قردوسی طوسی ‎LLL.‏ بخ ج ۸ ‎VEEN‏ و ‎Ay‏ : اسم مصدر بقلم نکارنده ی ۸

‏۵ رل :کوچك . ۱ س کوشه « تاریخ سیستان ص ۳۲۹ ۰ ۳۳۸ » پهلوی
‎kushk‏ > برنکرس ۱۰4, ‎ss‏ 05/0 ( کلاه فرنگی بالای بناه اطاق تابستانی
==== pdf 633 len 2033
[pdf page 633]
آن در درون‌آن صدا دهد. اکر درزیرزن‌آبستن
قدری ازآن دود کنند ‎GET‏ بزابد ‎HALT,‏
‏حجرء الولادة وحجرة النسر یزخوانند .۴

گنبد © ‎gin‏ اول‌وفتح بای ایسوسکون
‎yl‏ و دال بی‌نقطه « نوعی از عمارت باشدمدور
که ازخشت کل و کچ وآجر پوشند ۱ - وغنچةً
کل را یز گوبند- ونوعی ‎ya THI‏ بندی باشد که
مانند کنبد سازند؛ وبعربی قبه کویند. - ویمعنی
جتن و خیز کردن همهت - و مطلق پیاله را
نیز گفته‌اند (۱) خواء بدان شراب خورند وخواء
چیزی ‎Ke‏ ۳

‎a - OT‏ ازحباب‌است وآن
شیشه ماندی باشد که بوفت ‎Ook‏ باران‌برروی
آن بهم میرسد .

‏گنید اذدق - کنابه از آسان

‏گنید اعظم - بنمنی فلك‌اعظم است
که فلك الافلاك باشد , و عرش اعظم همان

‏است

‏است

‏گنبد آفت پذیر - کنابه ازآسان

‏(۱) چك » چس : گویند .
(۳) چش : دود کشت .

‎-۱۸۳۹-

‎. cel
‏لیزدق - بست یکنبدافت‌پذیر‎ Ae
. ‏است که کنابه از آسمان باشد‎

‎AT ‏چار بفك - کنابه از‎ a?
‏است باعتبار چهار نقطةٌ عشرق و مفرب و جنوب‎
‏هم هست باعتبار چهار‎ ls ‏و شمال - و کنابه از‎
. ۴ ‏عنص‎

‏گنید ججان‌ستان - بسن یکنبدتیزرو
است ‎(x)‏ که کنابه از آسمان باشد .

‏گنبد جر اه ‎SIG‏ - بسن ی کنید
جان ستان است که کنابه ازآسمان باشد .

‏گنید خضر \ - بمعنی کنبد ‎i>‏
‏رنگ است ک هکنابه از آسمان باشد .

‏گنبل دود گشت (۳) » بعنی کنبد
خضرا است که کنابه از آسمان باشد. وآنراکنبد
دو رگشت )2( هم گفته‌اند که بجای دال درمرتبةً
هفتم رای قرشت باشد .

‏نیال 8۵ لاب ‎KI‏ 9 بسن یکنبد
دور گشت (4) باشد که کنایه از آسسان است

‎ath pe )۲(‏ .
(4) چش : دور کشت .

‏۱ - پپلوی ‎gumbat‏ ( کنبد » فبه) « ناوادبا ‎oe‏ ۲:۱۹۱ * در تهران واراك (سلطان

‏آباد ) 800122 , معرب « جنبن »
« معجم‌البلدان در: جنبذ » « د
==== pdf 640 len 2432
[pdf page 640]
—N\ate—

کنکه

تولول ‎a Ke‏ وفارسیان ‎EP‏ .
گتك فا » بنتح اول و ثالث و نون بالف
کشیده» معروف‌است و آن‌سبزبی‌باند خوردلی۱ .
گونند چون خواهند روفن بلسانرا ببازمایند
‎Ua‏ را اف چرب ‎wil‏ و بر چراغ دارند .
‎SI‏ افروخته شود خالص‌است والا نه . اگرنخم
‎ba”‏ را درس رکه ریزند ترشی آنرابرطر فکند.
گند نا گو هر - بانی است که آنرا
علقم میکویند , ‎OT,‏ حنظل ‎col‏ که هندوانة
تلع باشد ؛ وبعضی کوین دکندنا ‎Byard pS‏

تلع است که ‎hey‏ حنظل باشد .
گثد فا گون - با کف فارسی » ‎wee‏
‏سبز ‎OS ez ath GG,‏ بمعنی رنگ ولون هم

آمده ‎«cel‏
‎OO”‏ - بنم اول و فتح تالك 1 ممروف
است که در مقابل باربك باشد ۴ - و ‎aS‏
‏بزرگیرا یز گونند که از کوشت سازند ودر شله
پلاو وآش اندازند ۴ - و کلوله‌ای که از خمیر
بجیت مك ته نان کنند ۴ - و کره ی که ازبدن
بر آید و درد نکند و بعریی ‎INE‏ خوانند -
و بفتح اول. بوی بد وهرچیز که بدبو شد» (۱)

(۱) چش : - شنم .

. Mask
‏گنه هر ۲ - زان پبر سالخورده را‎
. ‏گونند‎
‎oy ‏گندهپیر کابلی ‘ = پر زالی‎
. bE ‏جاد و گر وساخره در‎
‏گنده مغزی = پفتح‌اول ومیم‌وسکون‎
‏کردن و سخنان‎ KG ‏غین نقطه‌دار , کنابه از‎
‏متکیرانه کفتن وهرزه وباوه برزبان‌راندن‌ودرشتی‎
‏گویند‎ a ‏و کج خلقی‌نمودن باشد - وشخصی را‎
. ‏صفات داشته باشد‎ gpl ‏که‎
‏گذر ۲ = بفتح اول و الی وسکون رای‎
SPB ‏بی‌قطه , تام جنگ گاه سلطان محمود‎
. ‏(با) پادشاء تر کستان بوده‎
SE ‏گشگ = بفتح اول وسکون ثانی و‎
‏فارسی ۰ چند ممتی دارد : ۱- نام پتکده ایست‎
‏از بتکده های چین ۸ ۰ ۲- رودخانه ای باشد‎
‏بسیاربز رکه درملك‌هندوستان ومنبعآ نکوههای‎
‏سوالك است و ازملك هندوستان وبنگاله گذشته‎
‏بعمان میریزد و هندوان بدان اعقاد بیار دارند‎
‏و
```


## [2026-09-05T21:02:29.292Z] TOOL CALL #85: Bash

```json
{
 "command": "python3 - <<'EOF'\nimport re\nt=open('data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nidx={}\nfor p in pages:\n    m=re.search(r'\\[pdf page (\\d+)\\]',p)\n    if m: idx[int(m.group(1))]=p\nfor n in (654,655,656,657):\n    p=idx.get(n)\n    print('==== pdf',n,'len',len(p) if p else None)\n    if p: print(p[:1200])\nEOF"
}
```


### [2026-09-05T21:02:31.212Z] TOOL RESULT

```
==== pdf 654 len 2324
[pdf page 654]
۷7 ویر

گوشتاب ۱ - بر ‎Sy oi‏ (6۱.
بفعنی کوش پیچ است که کوشمال وپارچه‌ای‌باشد
که بردور گوش پیچند . .

گوشتاست = بسکون سین بی شله
و بای قازسی , بمعنی احتلام و شیطالی شدن
باشد ۴ - و ‎dite‏ مرغالرا نی زگوبند .

گوشت ‎EDT‏ ۴ - بنتح ها وسکون
تون و ‎ge‏ قلابیراگوین که بدان کوشت از
درون دنگ بیرون آرند - وغلیواج ‎wil” zal,‏
که زغن باشد .

گوشت [هنگ ۴ = بائاف فارسی,
بروزن ومعن ی کوشت آهنج است که قلاب گوشت
از ‎Ka‏ برآوردن - وغلیواج باشد .

گوشت وبا * ‎eae‏ رای فرشت‌وبای
ابجد بالف کشید» , غلیواج را کوبند که زغن
باشد و گوشت ربای (۲) هم کفته‌اند با تحتالی در
آخر » و گوشد ‎ILG‏ نر ‎ILE,‏ ماده میباشد
و بسضی شش ماه گفته‌اند - و قلاییر! نیز گوبند
که کوشت را بدان از ‎Kas‏ ببرون‌آورند .

گوش ‎٩ sole‏ © باخای نقطه‌دار(۳)

بالف کشیده و فتح را وسکون‌کاف + هرچیز که

(۱) چك . چش : بونقاب.
(۳) خم ۱ : - نقطه دار .

۱ - از ‎CEG ST:‏ (تابنده (با) تاییده) .

کوتدار
بدان کوش خارند - .وجانوری را لي زگوبندبسیار
پای که بگوش مردم رود و مردم را بی‌آرام ساژد
و با باشد که هلا ‎oS‏ و آنرا هزار پا هم
میگونند .
گوش ‎ONE‏ - کنایه از ‎Bg‏

کردن و مکت لمودن - وفک رکردن و درفکر

شدن باشد .

گوشن خبه - اين لت رادرفرهنک
جپانگیری بفتح رابع و بای ابجد بمعنی کوش
خارك آ ورده که میل ‎VSM FS‏ - وجاتوربسیار
پای باشدکه 
==== pdf 655 len 2143
[pdf page 655]
‎nh ply‏ معنی هم هست یمنی‌دگاهدار ومحافظت

‏گوش‌داشتن- بمعنی متوجه خدن
باشد ۱ - و کنایه از دیدن و نگاهداشتن (۱)
ونگاه گردن یز(۲) هست ۲ .

‏گوش ‎OI‏ - کنابه از مخنی و حرفی
بود که ‎Kr lS‏ شنیده شده ‎ath‏ ولیزسخنی
باشدکه بشخصی بگویند تا وقتی ازاوقات ‎Koo‏
‏بکارآن شخص با دنگری (۳)آبد 5

‏گوش صرای ‎ce‏ سین بی قله
ورای فرشت(4) بالف کشیده وتحتالی‌زده, کیرا
کوبندکه هرچه بشنود لیکو فه مکند.

‏گوشك ۴ - با ‎gt‏ مجپول بر وزن
‎ley‏ دو گوشت پاره را کوبند که برسرحلقوم
آدم ی که مجرای طمام است میباشد وآنرا بعربی
لوزتان خوانند - و صاحب ملازه را نیز گویند
و او را کام فرود آمده هم میگویند - و صفیر
گوش باشدکه بعربی اذن خوانند .

‎ASF‏ کره ۴ - مانی کوش کردن
است یعتی شنید - ونگاه داشت - و ‎MG‏ کرد
و دید .

‏رو و

‏گوش کرت ‎Gy ont sen‏
داشتن - و نگاه کردن باشد .

‏و ش گشتن «کنابه از سخن‌شنیدن
و متوجه شدن ‎Pach‏ .

‏گوش ‎PIES gare OT‏
است که کن‌ابه از سخن شنیدن و متوجه شدن
باشد .

‏گوش لب - بروزن ‎Ast‏ . آنکه
خطش هنوز ندمیده باشد + .

‏گوش ماهی - ‎dae‏ میکویند
و ‎OT‏ غلاف مروارید ‎ol‏ - و پیاله ای را نیز
کویندکه از صدف سازند .

‏گوش موش ه بکسر ‎tS. att‏
است کهآترا مرزنگوش‌خوانند ۷ وآن خوشبوی
میباشد و ‎FSS OT Ey‏ موش میمالد وبعرمی
آنان‌الفار خوانشد .

‏گوش ‎ONG‏ » بکس نون . کنابه
از سخن شنیدن
==== pdf 656 len 2389
[pdf page 656]
SS

وا

است که ‎Wey‏ باشد 6 .

‎GE Le ۱ UP gh‏ فارسی بر وزن
مودار, نام جالوری است که س رگین را کلوله کند
و بگردانه وغلطان غلطان ‎Glogs‏ خود بردوآنر!
عربان خنفاء میگوبند .

‏وال ۷ (۱) روز نکویل,بسنی
‎IOS‏ است که م کین
‎bls‏ باشد و عربان
ختفاء گوبندش ‎Oy)‏ ۰

‎wo *۵ ‏گر‎ oF

‏کاف فارسی ‎Losey‏ ودال
بی‌نقطه» جوهریت که آلرا
کبرت‌هم ‎au Se‏ و آن
ک وکال چهار لوع میباشد : سفید

‎aS

‎LS‏ باغی ‎AF‏ - کنابه از
کوشه‌شینی وخلوت کزیدن باشد .

‎is‏ بالش = کتایه‌از کوشم وکنار
مسند باشد .

‎tle ay‏ شکیته ه کنابه از
ماء لو باشد که هلا لگوبند +

‏گوشیار ۱ - بر وزن هوشیار ‎ths‏
‏حکیمی بوده ازفاری وشیخ ابوعلی‌سینا شاگردی
‎are‏

‏گود ‎en‏ اول و سکون ثانی مجهول
وکاف فارسی » ‎Ob SEG gee‏ باشد و آنرا
کوی گریبان هم میگویند ۴ - ودانهای سختی
که در ‎Lael‏ بیم میرسد و درد نمیکند و عربان | وزرد وسرخ وسیاء؛ وبسضی گوبندچشمه‌ایست‌روان
تولول خوانتدش ۴ - و بممنی کوساله هم آمده ]| چون منجمد گردد کبربت شود ؛ و بست یکوشد

‏(۱) چش : کوکال . ‎)٩(‏ چك : میکوبند ؛ چش : - و عربان ...گوبندش .

‎FH ‏اصح همین صورت است یمنی با کاف پارسی » از :کوش ( نام فرشته ) («.م.)‎ - ٩
‏داده [ قس : بهمتیار , اسپندبار , هرمزدیار ) 4 ابوالنکیا‎ tee: * ‏داد‎ « Jae ‏پسوند‎ ( ob
‏چهارم‌هجری میزسته ومژلف‎ OF ‏دوم‎ bag ‏کوشیارین لبا
==== pdf 657 len 2297
[pdf page 657]
My

ممدیی است وآن بشاری باشد دخالی که بعضی
ازآن درزیر زمین منجمد میشود وبعضی ازفرجها
و تراکهای کوه برمیآبد و در ‎WIM‏ برروی
‎e‏ می‌لشیند وک وکرد میشود , و گرداحمر
از جواهر است ومعدن‌آن دروادی موران میباشد
و موران آنجا مقابل بزی ميشوند. گوبشد درشب
مالند آتش میدرخشد چنانکه روشنابی آن چند
فرسخ میرود » وچون از ممدن بیرون آورنداین
خاصیت ندارد وآن جزواعظم ا کسیر است‌چنانکه
سیماب را ابوالارواح خوانند و ‎LT‏ ابوالاجاد
نامند . گرم و خشك است در چهارم و اقعام ‎OT‏
‏منافع بسپار دارد (۱).

گ و گر دا نك ‎٩‏ = با دالبالف کشیده
و قلح نون و سکونکاف » سر کین کردانك‌باشد
‎sly‏ را عربان (۷) جمل و خنفاء خوانندوترکان
قیقور گویند .

گو گه - بنم اول و ثالی مجهول وفع
‎GE‏ فارسی » بمعنی او لگوساله باشد که‌يچة کاو
ات ۳ - وبمعنی ‎AS‏ هم‌هست ک هگوی گریبان
و تکمه بائد ۴ - و دانهایی را نیز کوبند سخت
که در اعنای آدمی بهم میرسد و درد ‎ale‏
‏و پخته نمیشود وآترا بفارسی دب ویعربی ‎IDF‏
‏خواننه ۴ "و معرب‌آن قوقه است

کول ‎ee‏ اول بر وزن غول » بمعنی
ابله و ادن باشد و مت و فرب هم
هست ۵ - ‎ly GT,‏ نیز گوبندکه اند آب
درآن ایستاده ‎Vath‏ - و بسعنی ‎aie‏ هم آمده

رات

است و ‎oT‏ پرنده‌است منحوس که در وبرانها
و خرابها بسربرد و ‎Hee‏ شبها پروازکنسوبفتح
‎‘Jy!‏ پشمینه‌ایست‌با موبهای آویخته و آترادروشان
پوشند و بع
```


## [2026-09-05T21:02:58.600Z] TOOL CALL #86: Bash

```json
{
 "command": "python3 - <<'EOF'\nimport re\nt=open('data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor p in pages:\n    m=re.search(r'\\[pdf page (\\d+)\\]',p)\n    n=int(m.group(1)) if m else 0\n    if 640<=n<=680 and ('gōšak' in p or 'gosak' in p or 'kušk' in p or 'gwn' in p or 'gaona' in p or 'gōn' in p or 'gun' in p.lower()):\n        print('== pdf',n)\n        for mm in re.finditer(r'(gōšak|gosak|kušk|gwn|gaona|gōn|gun)',p):\n            print('   ',p[max(0,mm.start()-300):mm.start()+200].replace('\\n',' '))\nEOF"
}
```


### [2026-09-05T21:03:00.355Z] TOOL RESULT

```
== pdf 640
    کوبند « رشیدی » . رك : دزی ج۷ ص 4۵۳ :کراث . ۴ - امروزه یز 80806 ‎at».‏ ( سلطان آباد ) 55 800085 « مکی ژاد ». کنده ‎gine‏ بزرکه و حجیم و جسیم است و مقابل باريك ( بمعنی اصلی ) پهن است .  ۴ - من بگویم صفت ‎AST‏ پرواری گرم  کو بگویند مرا مدعبان کوقه خوار. ‎Gla?‏ اطممه . چاپ التالبول س ۱۷ *.  ۴ - پهلوی ‎gundak‏ , ارمنی ع 8080 (کلوله , کرء ) . 8021 (کلوله» کرء ) رك : استق - هوبشمان ‎a te nk . ٩۳۹‏ در ارال ( سلطان‌آباد ) 80008 > مکی‌نژاد *.  © « کند ( بفتح ) ‎Cpe)‏ ‏که فرخی در اشمار خودآورده : بجای ‎SG
```


## [2026-09-05T21:03:08.222Z] TOOL CALL #87: Bash

```json
{
 "command": "python3 - <<'EOF'\nimport re\nt=open('data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor p in pages:\n    m=re.search(r'\\[pdf page (\\d+)\\]',p)\n    n=int(m.group(1)) if m else 0\n    if 650<=n<=670:\n        for kw in ['گوشه','گون','گونه']:\n            for mm in re.finditer(kw,p):\n                seg=p[max(0,mm.start()-120):mm.start()+160].replace('\\n',' ')\n                if 'پهلوی' in seg or 'اوستا' in seg or 'gōn' in seg:\n                    print('pdf',n,kw,'::',seg)\nEOF"
}
```


### [2026-09-05T21:03:09.937Z] TOOL RESULT

```
pdf 656 گوشه :: ش‌میآید. ک و کرد در طبیعت بوفور بصورت سولفورها با سولفانها , با صورت ‎gel‏ خویش درحوالی کوههای آتشفشان یافت میشود .  ‏» گوشه - بضم اول و کر سوم ( در لهجهٌ مرکزی ) و بقتح ‎OT‏ ( در تلفظ قدیم ) 4 اوستا - ‎ogaoshaka‏ . کردی 802 , 805۲6 . بلوچی ¢ 805۳086 ‎ys.‏ 805126 ‎EO ۹40 gel?‏ کن
pdf 658 گون :: معرب) است که ام‌قدیم فیروزآباد باشد > ‎PLN NLA‏ ص ۱۳۷ » و رگ : فهرست همان کتاب » و ركك : معجم‌البلدان : جور ,  ‎. ‏رك : گونه‎ - ٩  ‏۰ رك . تملیقات ‎ale)‏ پنجم). ۱ رك :گلگونه. ۴ رگ :کون .  ‏۴ هز . 6602 » پپلوی ۷8۲۲۵ ( بره ) « ‎Gy‏ ص ۱۱۰ ‎٩‏ .  ‏۴- 5 :کلگونه . - قی : پهلوی 860216 -
pdf 658 گون ::  ۱۳۷ » و رگ : فهرست همان کتاب » و ركك : معجم‌البلدان : جور ,  ‎. ‏رك : گونه‎ - ٩  ‏۰ رك . تملیقات ‎ale)‏ پنجم). ۱ رك :گلگونه. ۴ رگ :کون .  ‏۴ هز . 6602 » پپلوی ۷8۲۲۵ ( بره ) « ‎Gy‏ ص ۱۱۰ ‎٩‏ .  ‏۴- 5 :کلگونه . - قی : پهلوی 860216 - 800816 ( کرنه گر ) «اوبوالا ‎Al‏ و رك :ح ۱۰ ‎NV‏
pdf 658 گون :: ۰ رك . تملیقات ‎ale)‏ پنجم). ۱ رك :گلگونه. ۴ رگ :کون .  ‏۴ هز . 6602 » پپلوی ۷8۲۲۵ ( بره ) « ‎Gy‏ ص ۱۱۰ ‎٩‏ .  ‏۴- 5 :کلگونه . - قی : پهلوی 860216 - 800816 ( کرنه گر ) «اوبوالا ‎Al‏ و رك :ح ۱۰ ‎NV‏ رك :. کوانبی . 
pdf 658 گونه :: معرب) است که ام‌قدیم فیروزآباد باشد > ‎PLN NLA‏ ص ۱۳۷ » و رگ : فهرست همان کتاب » و ركك : معجم‌البلدان : جور ,  ‎. ‏رك : گونه‎ - ٩  ‏۰ رك . تملیقات ‎ale)‏ پنجم). ۱ رك :گلگونه. ۴ رگ :کون .  ‏۴ هز . 6602 » پپلوی ۷8۲۲۵ ( بره ) « ‎Gy‏ ص ۱۱۰ ‎٩‏ .  ‏۴- 5 :کلگونه . - قی : پهلوی 860216 -
pdf 658 گونه ::  ۱۳۷ » و رگ : فهرست همان کتاب » و ركك : معجم‌البلدان : جور ,  ‎. ‏رك : گونه‎ - ٩  ‏۰ رك . تملیقات ‎ale)‏ پنجم). ۱ رك :گلگونه. ۴ رگ :کون .  ‏۴ هز . 6602 » پپلوی ۷8۲۲۵ ( بره ) « ‎Gy‏ ص ۱۱۰ ‎٩‏ .  ‏۴- 5 :کلگونه . - قی : پهلوی 860216 - 800816 ( کرنه گر ) «اوبوالا ‎Al‏ و رك :ح ۱۰ ‎NV‏
pdf 658 گونه :: ۰ رك . تملیقات ‎ale)‏ پنجم). ۱ رك :گلگونه. ۴ رگ :کون .  ‏۴ هز . 6602 » پپلوی ۷8۲۲۵ ( بره ) « ‎Gy‏ ص ۱۱۰ ‎٩‏ .  ‏۴- 5 :کلگونه . - قی : پهلوی 860216 - 800816 ( کرنه گر ) «اوبوالا ‎Al‏ و رك :ح ۱۰ ‎NV‏ رك :. کوانبی .
```


## [2026-09-05T21:03:27.887Z] TOOL CALL #88: Bash

```json
{
 "command": "python3 - <<'EOF'\nimport re\nt=open('data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nidx={}\nfor p in pages:\n    m=re.search(r'\\[pdf page (\\d+)\\]',p)\n    if m: idx[int(m.group(1))]=p\nfor n in (656,658,528):\n    p=idx.get(n,'')\n    print('======= pdf',n,' printed',n+1203)\n    print(p[-1400:])\nEOF"
}
```


### [2026-09-05T21:03:29.742Z] TOOL RESULT

```
======= pdf 656  printed 1859
 همین صورت است یمنی با کاف پارسی » از :کوش ( نام فرشته ) («.م.)‎ - ٩
‏داده [ قس : بهمتیار , اسپندبار , هرمزدیار ) 4 ابوالنکیا‎ tee: * ‏داد‎ « Jae ‏پسوند‎ ( ob
‏چهارم‌هجری میزسته ومژلف‎ OF ‏دوم‎ bag ‏کوشیارین لبان باشهر یگیلالی منم بزرکه , وی‎
Bab ‏و «مجمح‌الاسول» است . رك : کوشیار گیلانی بقلم نگارنده در‎ UL ‏جامم » و «زیج‎ mS?
‏و ص۲۰8-۷۰۰. ۰ ۴ - ظ.با «بهمنیار» که شاکرد ابن‌سینا‎ BLL IIL ‏فرهنگه, چاپ مشهد‎
‏خلطشده» ولی او آنر باجالی است + وک شکل‌قديم :کوء گوی (هدم.),‎ (kn ‏بوده (نه‎

‏۴ < ک که («م.) © کو که (هم.) طبری 80 ‎(JLT)‏ « واژه نامه
‎dy > ۶‏ :کار ,کو . ۲ ص کوکال ‎(pn)‏ , قس : اوستا ‎vareta‏ 806۳8 .که درتفیی
‎Jalen) Soles OT Is) ose Favs f gOh _vartsse‏ وهای‌ملفوظ بمعنی سکین‌است) ‎ope‏
‏دوم همریشه وبععنی گردیدن وگرداندن‌است. لفة بمعنیس کین گردان(ه.م.) ورك ‎US FF‏
ورك : ح٩‏ ص۱۸۲ ۷ ک کار ‎pa)‏ ۸ - دراوراق مالوی‌بپپلوی ۳۵
«کو گرد . -ولفور» ,1 ‎(Henning, A list of Middle Persian..., 3505, XI,‏
‎p ۰3‏ )ک وکرد ‎Soufte)‏ فر) جنمی است بیط و جامد » برنگه زرد لیموبی » بی‌مزه وبی
بو . وزن‌مخضصوص‌آن ۵ است ودره ۱۱۶ درجه ذوب میشود ودر 440/۵ درجه بجوش‌میآید.
ک و کرد در طبیعت بوفور بصورت سولفورها با سولفانها , با صورت ‎gel‏ خویش درحوالی کوههای
آتشفشان یافت میشود .

‏» گوشه - بضم اول و کر سوم ( در لهجهٌ مرکزی ) و بقتح ‎OT‏ ( در تلفظ قدیم ) 4
اوستا - ‎ogaoshaka‏ . کردی 802 , 805۲6 . بلوچی ¢ 805۳086 ‎ys.‏ 805126
‎EO ۹40 gel?‏ کنج » زاوبه - خلوت . خلوتگاه ‎Se‏ کناره = دستهٌآوند - دکمه, کره.

======= pdf 658  printed 1861
نکرس ‎V8‏
‏۲ - پهلوی 800 > تاوادبا ۰۱5۱ و 8002 اوستا

‏کونجی
‎caw‏ رنگ ولون باشد ۷ چ هکلگو ‎SM‏

‏راگویند - و بمعنی طرز و روش وقاعده وفالون
و صفت لیزآمده است - و بضم اول ‏ و کسر ‎tall‏
‏نام شهری است از شهر های فاری و معرب ‎OT‏
‏جون باشد ۸ .

‏گو نا * = ‎en‏ اول و نون‌بالف کشید»,
‎yom‏ گونه و رنگه ولون‌باشدچه کون گونبمعنی
‎NG,‏ است *9- و غازه‌ای که زنان بر روی
‎aL‏ ۷۱- و پمعنی طرز وروش وقاعده و قانون
و صفت هم‌آمده است ‎VF‏ و بلفت زند و پازند
بچه و بر کوسفند راگوند ‎OM‏

‏گو اب - بر وزن خوناب ؛ سرخی
وگلگوهه‌ای باشدکه زنان بجهت زببابی‌بررخسازه
‎Fadl‏

‏گو نا گون ‎oO‏ بمی‌رنگارنگگ‌است
که جنس بجنس و ‎A‏ باشد .

‏گو نجی ۰۱۷ بنم اول و کر شا
وسکون نون و شتا کید ‎HP ae!‏
وکرامی ‎ath‏ - و بمعنی شجاع ودلیر و پهلوان
‎oul‏ است

‎:4, ۴

‏- 88002 ( مو , رنگه مو ( > پارتولمه 4۸۷ € ارمنیع 8010 ( رنگه ) ‎Baum yt‏
قس : کلمات پهلوی : ‎6gh6n , hamg6nak . cighon‏ . 227۵6۵01 د بی رکه س
‎٩ ۷‏ نیز آرمني فارسی کوده . اقنانی 80008 ( مو , رنگگ ) « هوبشمان ‎Aer‏
‏و رك ‎A stad gets‏ کون با جون در ‎LLG‏ ابن‌البلخی ومعجم‌البلدان وحدودالعالم
نيامده ؛ ظ . مصحف «کور» ‏ جور(معرب) است که ام‌قدیم فیروزآباد باشد > ‎PLN NLA‏
ص ۱۳۷ » و رگ : فهرست همان کتاب » و ركك : معجم‌البلدان : جور ,

‎. ‏رك : گونه‎ - ٩

‏۰ رك . تملیقات ‎ale)‏ پنجم). ۱ رك :گلگونه. ۴ رگ :کون .

‏۴ هز . 6602 » پپلوی ۷8۲۲۵ ( بره ) « ‎Gy‏ ص ۱۱۰ ‎٩‏ .

‏۴- 5 :کلگونه . - قی : پهلوی 860216 - 800816 ( کرنه گر )
«اوبوالا ‎Al‏ و رك :ح ۱۰ ‎NV‏ رك :. کوانبی .

======= pdf 528  printed 1731
کویند

‏بوده است

‏- از : کوش ( کوشیدن )+ ان ( پسوند صفت فاعلی ) .

‏۴ - یزه کوشان » نام قومی‌است ‎Dy.‏ : کشان . - از : کوش (کوشیدن) +
ش ( پنولد اسم مصدر ) ‎Hy.‏ : کوشیدن .
۴ - یراکنده + شد ترك سیصد هزار ‎gles‏ نبد کوشش و کارزار .

‏قردوسی طوسی ‎LLL.‏ بخ ج ۸ ‎VEEN‏ و ‎Ay‏ : اسم مصدر بقلم نکارنده ی ۸

‏۵ رل :کوچك . ۱ س کوشه « تاریخ سیستان ص ۳۲۹ ۰ ۳۳۸ » پهلوی
‎kushk‏ > برنکرس ۱۰4, ‎ss‏ 05/0 ( کلاه فرنگی بالای بناه اطاق تابستانی) « ژابا س
۰ معرب آن « جوسق ‏ « ابن درید *. ۷ رگ : کشکنجیر .

‎wat, A‏ «کوشه » را ‎Gal ce‏ «کوشا » و « کوشان » بمعنی کوشنده آورده بدون
شاهد . جهانگیری «کوشه » را بعمتی کوشیده گفته بدون شاهد ۰ انجمن‌آرا و فرهنگه نظام این
کلمهرا بیاورده اند . اکراستعمال شده باشد ظ۰ اسم مصدر است از: کوش ‎(ty)‏ |-»(پسوند
‎ol‏ مصدر ) رك : اسم مصتر بقلم تگارنده ص ‎٩٩‏ ببمد ؛ در تاجیکی 108106 پیمنی ششواراست
‎ee?‏ ۷ : +اص ۹۲۱ ‎۰٩‏ و در تاریخ سیستان « کوشه » بمعنی کوشك آمده . رلك : ح ‎٩‏ .

‏- اصح «کوشیار» ‎Cpe)‏ است . ‎te‏ بمعنی اخبر ‎b‏ با « بپمنیار » که
شاکرد ابوعلی بوده , لفظاً و معناً خلط کرده‌اند . ‎MN‏ ره : رشیدی .

‏۵ کوشیدی - بنم اول و فتح پنجم ( درقدیم ‎kdshitan‏ ) . پهلوی ‎-kéxshitan‏
‏از ‎kosh - , 16۵29 - ix,‏ ( قی : پهلوی ‎Jats. (késhttarth , késhishn‏
‎kdk(u)shét , okau _ kushati‏ ۵ . ساختمانی از - ‎kush‏ , ماسکریت ‎kushnati‏
‏(کشیدن ) , فارسی کنولی « کشتن » ( نم ) « لیب رکه ص۱۳۶ » ؛ جد وجهد کردن»سعی کردن:
« دولت نه بکوشیدن است , چاره کم جوشیدن است . » «کلستان ص ۱۱۳ .
```


## [2026-09-05T21:03:50.070Z] TOOL CALL #89: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nfor f in ('BQT_v2_pages.txt','BQT_v1_pages.txt'):\n    t=open(f,encoding='utf-8',errors='replace').read()\n    pages=t.split('\\f')\n    hit=[]\n    for p in pages:\n        m=re.search(r'\\[pdf page (\\d+)\\]',p)\n        n=int(m.group(1)) if m else -1\n        if 'چگون' in p and ('پهلوی' in p or 'cig' in p or 'gōn' in p):\n            hit.append(n)\n    print(f, 'pages with چگون+پهلوی:', hit[:20], 'total leaves', len(pages))\nEOF"
}
```


### [2026-09-05T21:03:54.441Z] TOOL RESULT

```
BQT_v2_pages.txt pages with چگون+پهلوی: [-1, -1, -1] total leaves 684
BQT_v1_pages.txt pages with چگون+پهلوی: [-1, -1] total leaves 777
```


## [2026-09-05T21:03:58.432Z] TOOL CALL #90: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && head -3 BQT_v2_pages.txt && python3 - <<'EOF'\nimport re\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if 'چگون' in p and ('پهلوی' in p or 'cig' in p):\n        print('=== leaf idx',i)\n        for mm in re.finditer('چگون',p):\n            print('  ',p[max(0,mm.start()-250):mm.start()+250].replace('\\n',' '))\n        print(p[:120].replace('\\n',' | '))\nEOF"
}
```


### [2026-09-05T21:04:00.127Z] TOOL RESULT

```
                                         ‫‪7‬‬

                          ‫رن‪۳‬‬
=== leaf idx 113
    ‫؟ ‪.‬‬   ‫‪ ۶‬جفتای ‪۷۸۲‬‬                                                                                  ‫‪۶۵٩‬‏‬    ‫حً‬                                                                                          ‫قصهفاز‬    ‫* چګو لگی ‪ -‬از ‪ :‬چگونه (چگونك) ‪ +‬ی (مصدری) ‪ .‬پهلوی ‪ « 005۵880‬مناس‬         ‫«ثف المحجوب‌سجتانی ‪۷۱‬؟‪.‬‬                               ‫‪»۲ : ۷‬؛ کیفیت «کویفیت بود چون چگونگی چیزها» ک‬     ‫» پهلوی ‪0۵8۵0‬‬        ‫کهو‪+‬نه‬                               ‫‪ #‬چ
   ‬   ‫‪ ۶‬جفتای ‪۷۸۲‬‬                                                                                  ‫‪۶۵٩‬‏‬    ‫حً‬                                                                                          ‫قصهفاز‬    ‫* چګو لگی ‪ -‬از ‪ :‬چگونه (چگونك) ‪ +‬ی (مصدری) ‪ .‬پهلوی ‪ « 005۵880‬مناس‬         ‫«ثف المحجوب‌سجتانی ‪۷۱‬؟‪.‬‬                               ‫‪»۲ : ۷‬؛ کیفیت «کویفیت بود چون چگونگی چیزها» ک‬     ‫» پهلوی ‪0۵8۵0‬‬        ‫کهو‪+‬نه‬                               ‫‪ #‬چگوله ‪ 
                                                              ‫قصهفاز‬    ‫* چګو لگی ‪ -‬از ‪ :‬چگونه (چگونك) ‪ +‬ی (مصدری) ‪ .‬پهلوی ‪ « 005۵880‬مناس‬         ‫«ثف المحجوب‌سجتانی ‪۷۱‬؟‪.‬‬                               ‫‪»۲ : ۷‬؛ کیفیت «کویفیت بود چون چگونگی چیزها» ک‬     ‫» پهلوی ‪0۵8۵0‬‬        ‫کهو‪+‬نه‬                               ‫‪ #‬چگوله ‪ -‬بکر اول و چپارم (درلېجۀ‌مر کزی)‪ .‬از‪ :‬چ‬       ‫«مسینا‪ ۲۳۱‬؛ چه دوع » چان ‪ ۰‬چطور (استفهام) ‪ .‬ر که ‪ :‬اسفا ‪ ۲ : ۱‬ص ‪ ۲۳‬و ‪٥٤‬‏ و‪۱٩۲‬‏‬  
                                                                                              ‫‪0‬ی‬ |                    
=== leaf idx 122
   ر کك ‪ :‬خرده‬  ‫‪ - ۱‬از ‪ :‬چندل و‬         ‫زره سستان امت ‪ .‬رکه‪ :‬زره‪.‬‬ ‫‪۵‬‬             ‫اوستا ‪ ۹۳۱‬و‪۲6۱۰‬‬   ‫‪ - ¥‬پهلوی ‪« 110026‬منای ‪۰۷۲۰‬؛ ( بباای‬        ‫(یسوند) ‪ .‬رک ‪ :‬فرهنك دساتیر ‪. ۳۸۲‬‬   ‫مصدری) کمیت ‪« :‬کیفیت بود چون چگونگی چیزها و کیت بود چرن چندی‪ «»:‬کشف‌المحجوب‬  ‫را‬    ‫‪:‬اچندی برین آمد لعلف طبض‬                               ‫چذدی (بابای نکره) سنی چند روزی » مدثی «‬                       ‫سستأنی ‪۷۱‬‬                 ‫(لملف طبع دوست سعدی را) بدیدند و حسن 
  ‫‪-‬‬    ‫وا‬                                                                                         ‫چندر‬ |  | ‫چندی ‪ 
=== leaf idx 129
   فرانوی ‪ 611201016‬ازفارسی‌مأخون امت « اسفا ‪۱:۲‬‬  ‫‪۴‬خ‪-‬تی حر‬   ‫ص؟‪ .‬‏ در بوت‪1‬ان‪2‬ي‪ 00108511‬آلمانی‪ « 0082005‬دائرة المعارف اسلام » ‪ .‬ل‬                                               ‫ی( نبت ) ‪:‬‬         ‫‪ - ۴‬از ‪ :‬چوکان‬        ‫«چگون» و«چگونه»‪.‬‬              ‫‪۰‬‬    ‫سرد‬   ‫را بچ وکانی خود‬           ‫عنان‬                 ‫سکندر که ازخروان گوی برد‬   ‫نظامی گنجوی« کنجینه»ع» ‪.‬‬   ‫‪٩‬‏ ‪ -‬باین‌معنی«تر کی» است«جفتای ‪ ۷۹۲‬؟‪.‬‬                        ‫رکک‪ :‬چغو‪ .‬چفد
    611201016‬ازفارسی‌مأخون امت « اسفا ‪۱:۲‬‬  ‫‪۴‬خ‪-‬تی حر‬   ‫ص؟‪ .‬‏ در بوت‪1‬ان‪2‬ي‪ 00108511‬آلمانی‪ « 0082005‬دائرة المعارف اسلام » ‪ .‬ل‬                                               ‫ی( نبت ) ‪:‬‬         ‫‪ - ۴‬از ‪ :‬چوکان‬        ‫«چگون» و«چگونه»‪.‬‬              ‫‪۰‬‬    ‫سرد‬   ‫را بچ وکانی خود‬           ‫عنان‬                 ‫سکندر که ازخروان گوی برد‬   ‫نظامی گنجوی« کنجینه»ع» ‪.‬‬   ‫‪٩‬‏ ‪ -‬باین‌معنی«تر کی» است«جفتای ‪ ۷۹۲‬؟‪.‬‬                        ‫رکک‪ :‬چغو‪ .‬چفد‪ .‬جفد‪
                     ‫‪ ¥‬جوماق ‌‪ -‬رک ‪ :‬جماق ‪۰‬‬        ‫* چولاق رک ‪ :‬چلاق ‪.‬‬    ‫(ونه‌رنك )‪ .‬مخفف آن» چو‬                          ‫‪ #‬چون ‪ -‬پهلوی ‪ 0081‬از (»(چه) ‪ 201028 +‬گ‬    ‫«نیب رکك ‪« »4 4‬تاوادی‪4۵۱‬؟؛ *بوستی ‪ .‬بندهش ‪۱۲۱6‬؛ چگونه ‪ -.‬چسانب موثملانند(ر که‪:‬ص به‬                                                          ‫‪-‬را ازبرای ‪ -‬وقتیکه» هنگامنکه‪.‬‬                                                                                       ‫از دبباچة ملف) ز‬ 
 ‫چوبگان‬
```


## [2026-09-05T21:04:14.290Z] TOOL CALL #91: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfa='۰۱۲۳۴۵۶۷۸۹'\ndef nums(p):\n    out=[]\n    for m in re.finditer(r'[۰-۹]{3}',p):\n        s=m.group(0); out.append(int(''.join(str(fa.index(c)) for c in s)))\n    return sorted(set(x for x in out if 600<=x<=760))\nfor i in range(110,136):\n    print(i, nums(pages[i])[:12])\nEOF"
}
```


### [2026-09-05T21:04:15.896Z] TOOL RESULT

```
110 []
111 []
112 []
113 []
114 []
115 [653]
116 []
117 []
118 []
119 []
120 []
121 []
122 [730]
123 []
124 []
125 []
126 []
127 []
128 []
129 []
130 []
131 []
132 []
133 [722]
134 [630]
135 []
```


## [2026-09-05T21:04:27.323Z] TOOL CALL #92: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -c \"\" MON_part1.txt MON_part2.txt; grep -n \"کیوسک\" MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v2_djvu.txt 2>/dev/null | head -5"
}
```


### [2026-09-05T21:04:27.391Z] TOOL RESULT

```
MON_part2.txt:94500
MON_part1.txt:99339
incoming/MON/MON_2vol_Adena_v2_djvu.txt:29109:کیوسک: ۲5:0 [از ف. کوشک] (ا.) 
MON_part2.txt:29109:کیوسک: ۲5:0 [از ف. کوشک] (ا.)
```


## [2026-09-05T21:04:32.284Z] TOOL CALL #93: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^گنبد:\\|^گون:\\|^گنده:\\|^کوشک:\\|^گوشه:\" MON_part2.txt MON_part1.txt | head -20"
}
```


### [2026-09-05T21:04:32.335Z] TOOL RESULT

```
MON_part2.txt:28035:کوشک: 55 [- کوشه» گوشک - 
MON_part2.txt:35447:گنده: )0 ی ۰ زسر» درشضت.» 
MON_part2.txt:36716:گوشه: (0-)2154 (.) کنار» کناره» کران. از 
MON_part2.txt:36867:گون: (قد. :1۱)86ع | گونه, گونا] (ا ) رنگ.» 
MON_part2.txt:36876:گون: (.) (گیا.) گیاهی اتیت ار تبر 5
```


## [2026-09-05T21:04:34.832Z] TOOL CALL #94: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '28035,28040p;36716,36722p;36867,36875p' MON_part2.txt; echo \"=== گنبد\"; grep -n \"گنبد\" MON_part2.txt | head -5"
}
```


### [2026-09-05T21:04:34.897Z] TOOL RESULT

```
کوشک: 55 [- کوشه» گوشک - 
جوسق» معر.] (ا.) بنای مر تفع و عالی» قصرء 
کاخ. قلعه» حصار. 

کوشی: ۲۵ [تر. م.] (ا.) علوفه و آزوقه و 
سبورسات. 
گوشه: (0-)2154 (.) کنار» کناره» کران. از 
(ز) گوشه به گوشه: از کران تا کران؛ سراسر 
و ماه نو گوشه چگر :کار 
جگر. (کد.) فرزند. جگر گوشه. گوشة 
چشم: کنج چشم. (مج.) کسترین ناه 
(مج.) اند ک تو جه. و وه 
خاطر: اندک میل باطن. گوشة دهان (دهن): 
گون: (قد. :1۱)86ع | گونه, گونا] (ا ) رنگ.» 
لون. رخسار» چهره» گونه. نوع» قسم. طرز؛ 
روش؛ شیوه. شکل» هیثت. (پس.) بصورت 
پسوند در ترکیبات ات ی رک 


لون» شکل و هیشت. 


=== گنبد
2954:غوزه آب. گنبد. (کد.) دهان معشوق. ( کد.) 
11352:فراز آن گنبدی باشد. سقف برجسته و 
11353:مدون گنبد. قهٌ آب: (کد.) قنة بادین: (کد.) 
13673:گنبدی شکلی بنام حجاب حاجز می‌پوشاند. 
26387:کمرا: تسه (طاق گنبد] (ا.) محوطه‌ای که
```


## [2026-09-05T21:04:43.989Z] TOOL CALL #95: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('LAT.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint('leaves',len(pages))\nfor i in (504,505,506,507):\n    print('=== leaf',i,'printed?',i-18)\n    print(pages[i][:900])\nEOF"
}
```


### [2026-09-05T21:04:46.190Z] TOOL RESULT

```
leaves 1409
=== leaf 504 printed? 486
genuinus
-486-
a dtd rattach^ A genus, et n$ae eaployd seuleaent dans nn sens ddrivd;
cf. ingenuus, s. gens, 7.
Antres derives et coaposds: genuSle: yovaxoSecjioe; genudrius (lire
genu<cu> Idriust) yovimexrie; genuflects = yovux\t,vet.v ( 1 . Egi.); in-,
pergenuS ( 61 .).
Le non da "genoa" en indo-europden a ane forne ddfinie, aais avec
des rocalisaes divers qui tiennent A ce que la flexion coaportait
des dlargissenents. La forae da not varie: gr. yovu, ekr. j anu (d'accord
avec pehlvi zanuk), lat. genu presentent trois vocalisaes distincts.
II y a an dlargissenent -r- dans le no*.-acc. ara,cunr "genoa" (le
plariel est cungk') et an elargissenent -n- dans gr. *yovFaxoe (hoa.
youvaxoe, att. yovaxoc), ved. janunl "les (deax) genoax". Le vocalisne
a degrd zdro apparaat dans des ddrivds coane gr. tyvur) "jarret", yvuJ;
"A genoax", got. kniu (ddrivd thdnatiqae) "genoa" oa des conposds
coane g
=== leaf 505 printed? 487
- 487
gestis
gerulus a., gerula f.: porteur, porteuse, terse general qui s'est
spdcialisd dans les langues techniques. Gerula dans Pline ddsigne
1'abeille ouvribre; dans les 1. roianes, il est applique a differents
objets servant 1 porter: hotte, cuve, etc. M.L.3747. Coaposds plau-
tiniens: saluti-, scutigerulus, gerulifigulus (Ba.381).
3° en gest-: gestid: adainistration, gestion (classique, aais rare;
Cic. Inu.1,36,38; 2 ) 13 ) 39 ); gestus,-Us a.: aanibre de se tenir, port,
attitnde, geste; d*ou gestuSsus (Geli., Apnl.); gestor: porteur (trbs
rare, Pl., Dig.); glosd aussi Y u M- vota,CT 1 C >
gesto,-os: frdquentatif de gerS, dont le sens souvent ne differe
gubre du siaple, c£ Pl., Ps. 437 sqq., ftoaines qui gestant quique auscul¬
tant crimina \ si meo arbitratu liceat, omnes pendeant, \ gestores
linguis, auditores auribus. Spdcialeaent: "porter en litibre"; et
"porter un enfant, etre 
=== leaf 506 printed? 488
gerra
488
suggestum ; sug gest i 5 ,-tus,-us m , supergero (Coi.).
antegeriB (anti -) "de pr^ference". Adverbe archalque cite par
Festus et Quintilien, aais non atteste dans les textes.
Dn verbe cone gero n'a gubre de chance d'etre emprnnt^; aais on
ne trouve dans les aatres langues indo-enrop 4 ennes rien qui ressenble
netteaent au *ges- de lat .gerS, gestus. On rapproche souvent v.isl.
kps (g£n .kasar) "congeriSs", kasta "jeter", aais cela n'^claire pas
le gronpe latin. II est exceptionnel qu*un verbe radical de type
aussi archaique n'ait pas de correspondance hors du latin.
gerra, -ae f. (usite surtout au pl.): gerrae crates uimineae, P.F.
83,1. Enprunt au gr. yeppov, yeppa, lui-aene d'origine inconnue. Seable
different, aalgr 4 1'^tyaologie populaire, du suivant. .
gerrae: exclaaation ironique sans doute eaprunt^e au grec de' Si¬
cile ou yeppa designe les ouBoux. de 1 1 hoaae ou de l
=== leaf 507 printed? 489
- 489 -
glrba
glgas, -antis m.: emprunt litt< 5 raire an gr. -avxec d'ori-
gine inconnue. Passe dans la langue commune comme nom conmun, et
de IX dans les 1 . romanes, sons la forne *g 'agante(mj, M.L.3750.
D^rive: giganteus.
gigeria (gizeria), -orum n.pl.: entrailles de volaille, g^sier.
Terne de cnisine attest^ senlement au pluriel, quoique le fr. gdsier
remonte a gigerium, M.L.3760. Les mss. de Nonius, p.119,18, attribuent
X Lucilius une forne gizerini (lire g izerianit), mais le texte est
peu sur, et, serait-il exact, on ne pourrait d 4 cider si la forme
remonte k Lucilius, ou repr^sente une prononciation contenporaine
de Nonius, ou du copiste. Sur gizeriator, v. gingrid.
Schuchardt, Z.f. rom.Phil.38,444sqq., a suppose que le mot a-pu
etre emprunte a une langue iranienne, ou il designait le "foie" (cf.
persan nod. jfigar "foie"; v. iecur). Une origine punique a 4 t^ aussi
proposee .
```


## [2026-09-05T21:04:52.810Z] TOOL CALL #96: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"gibbus\\|gibber\\|gibba\" LAT.txt | head -10; echo ---; python3 - <<'EOF'\nt=open('LAT.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nimport re\nfor i,p in enumerate(pages):\n    if 'gibbus' in p or 'gibber' in p:\n        print('leaf',i)\n        j=p.find('gibb')\n        print(p[max(0,j-200):j+1800])\n        break\nEOF"
}
```


### [2026-09-05T21:04:54.469Z] TOOL RESULT

```
15345:ainee expressive, cf. flaccus, gibber, etc. Cuppes a servi de cogn&aen,
26143:gibber, -a, -um; gibbus, -a, -um (la forne la plus ancienne sen-
26144:ble gibber qui est dans Varron; gibbus est de l' 4 poque iaperiale):
26145:bossu. Ancien (Lucii.). Technique ou faailier. - Substantif gibber,
26146:-ris n. (cf. tuber), gibbus, -t; gibba,-aei bosse, gibbosite.
26147:D 4 riv< 5 s: gibberSsus ( gliberSsus CGL III 597,44); gibbSsus, tous
26149:Les 1 . roaanes attestent gibbus, *gibbulus, et des d^foraations
26152:gheb, cf. Graur, Mei.ling.36), un derive *gibberutus, M.L.3755,3754, 3753 «
26153:L 1 eaploi de gibber coaae adj. et subst. a son correspondant dans
---
leaf 301
-
bydd.
Coapos 4 s: discupio: je crbve de desir (l. faailibre); percupio.
k cupio s 1 apparentent:
cuppes: (Pl.Tri.340): gouraand, goinfre, ou "d 4 bauche"?, avec g 4 -
ainee expressive, cf. flaccus, gibber, etc. Cuppes a servi de cogn&aen,
cf. Donat, Eu.356; cuppedo,-inis (cf .Forum Cuppedinis) f.: gouraandise
(d'ou "desir" dans Lucr.1,1083; 3,994, etc.) et "friandise", cuppedium
(Flante), cuppedia ( Cic., Geli., Aaa. ), cuppedinarius ob, par suite de
la sp 4 cialisation de sens, les Latins croyaient reconnaitre cupio et
esse "aanger". Cuppedium, cuppedo coaae le fr , gourmandise, friandise
avaient k la fois le sens abstrait et le' sens concret; cf.Pl.Stich.
714, Cic.Tuse.4,36.
Le pr 4 sent cupio est d 4 riv 4 coaae on le voit par le perfectua cu-
piui. Le latib a reaplac 4 les aots anciens signifiant "desirer" (v.
Fenus, uenor et aerusco) par un aot nouveau expressif. Qn rapproche
ordinaireaent de cupio des aots de dialectes orientasx dont le sens
est 41 oigne: skr.feu pyati "il bouillonne, il se aet en colfere" et v.sl.
kypitii "il bout" (ou il y a un anci en u; cf. Iit. kupa, qui se dit de
l'eau qui s^chappe d'un vase par suite de 1 1 ebullition; lett.feu^u
"je fune"). - Peut-etre ces prdsents sont-ils d 4 rives d'un thbne radical
ath 4 aatique dont lit. kvepia "il r 4 pand une odeur" serait aussi deriv 4 ;
lit. pa-kvimpu, pa-kvipti si^nifie "se aettre k r 4 pandre une odeur".
Le rapproebeaent de gr.xcwivoc "fun 4 e" et de X(X7toe* \|/uxn.> 7 tvEupxx Hes.
est rendu douteux par 1'a, (le x s 1 expliquerait a la rigueur par dis-
siailation); on pense 4 galeaent a. lat .uapor ou il y aurait eu aussi
dissiailation (*kwap- devant aboutir k pap- ). Tout cela incertain,
fuyant, parce qu'il s'agit d'un verbe de caractbre affectif.
cuppa, -ae f,(u.): coupe. Panroaan, M.L.3409. Le teaoignage des
langues roaanes (cf.fr. coupe et cuve) indique qu'il y avait un aot
k consonne g 4 ain 4 e different de cupa', cf. aussi sans doute la glose
de CGL V 584,1, copa uas uinarium, quod
```


## [2026-09-05T21:04:58.652Z] TOOL CALL #97: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('LAT.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n'); leaf=0;m={}\nfor i,l in enumerate(lines,1):\n    m[i]=leaf; leaf+=l.count('\\f')\nprint('line 26143 leaf',m[26143])\npages=t.split('\\f')\nprint(pages[m[26143]][:2200])\nEOF"
}
```


### [2026-09-05T21:05:00.387Z] TOOL RESULT

```
line 26143 leaf 506
gerra
488
suggestum ; sug gest i 5 ,-tus,-us m , supergero (Coi.).
antegeriB (anti -) "de pr^ference". Adverbe archalque cite par
Festus et Quintilien, aais non atteste dans les textes.
Dn verbe cone gero n'a gubre de chance d'etre emprnnt^; aais on
ne trouve dans les aatres langues indo-enrop 4 ennes rien qui ressenble
netteaent au *ges- de lat .gerS, gestus. On rapproche souvent v.isl.
kps (g£n .kasar) "congeriSs", kasta "jeter", aais cela n'^claire pas
le gronpe latin. II est exceptionnel qu*un verbe radical de type
aussi archaique n'ait pas de correspondance hors du latin.
gerra, -ae f. (usite surtout au pl.): gerrae crates uimineae, P.F.
83,1. Enprunt au gr. yeppov, yeppa, lui-aene d'origine inconnue. Seable
different, aalgr 4 1'^tyaologie populaire, du suivant. .
gerrae: exclaaation ironique sans doute eaprunt^e au grec de' Si¬
cile ou yeppa designe les ouBoux. de 1 1 hoaae ou de la femae. A ce
second gerrae se rattachent probableaent gerr 5 (cf. dor. Teppoov) et
congerro,-onis (congerrae dans Fest.38«,30), aots de la 1 . comique;
cf. P.F.35,15, cerrones (l. ger-), leues et inepti...
gerrgs ( girris Gloss.), -is a.: poisson, sans doute sorte d'an-
chois, glos 4 p,0UVI.6e£ Gloss.Philox. Conserve en fr. it. prov., M.L. 3746;
cf .jarret qui dgsigne le picarel.
Derives: gerricula et peut-etre gerrinus (Pl.Ep.a33).
gestio: v. gestus, s.u.ger 5 .
geun: v. gaeum.
geuslae, -arun f.: gosier (Marcell. Enpir. ). Sans doute gaulois. M.
37 S° •
gibber, -a, -um; gibbus, -a, -um (la forne la plus ancienne sen-
ble gibber qui est dans Varron; gibbus est de l' 4 poque iaperiale):
bossu. Ancien (Lucii.). Technique ou faailier. - Substantif gibber,
-ris n. (cf. tuber), gibbus, -t; gibba,-aei bosse, gibbosite.
D 4 riv< 5 s: gibberSsus ( gliberSsus CGL III 597,44); gibbSsus, tous
de 1 'gpoque imperiale; gibbula (Chir.), gibatus, -a, -um (Anth.904,13)?
Les 1 . roaanes attestent gibbus, *gibbulus, et des d^foraations
*gimbus (gimberosus CGL III 630,74, gembrOsus Isid.Quaest. test. 48,
p.aofib; cf .sambatus, sambucus, etc.), *gubbus, *gumbjis, *glilbus (roua.
gheb, cf. Graur, Mei.ling.36), un derive *gibberutus, M.L.3755,3754, 3753 «
L 1 eaploi de gibber coaae adj. et subst. a so
```


## [2026-09-05T21:05:07.077Z] TOOL CALL #98: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('LAT.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\np=pages[506]\nj=p.find('gibber, -a')\nprint(p[j:j+2600])\nEOF"
}
```


### [2026-09-05T21:05:08.750Z] TOOL RESULT

```
gibber, -a, -um; gibbus, -a, -um (la forne la plus ancienne sen-
ble gibber qui est dans Varron; gibbus est de l' 4 poque iaperiale):
bossu. Ancien (Lucii.). Technique ou faailier. - Substantif gibber,
-ris n. (cf. tuber), gibbus, -t; gibba,-aei bosse, gibbosite.
D 4 riv< 5 s: gibberSsus ( gliberSsus CGL III 597,44); gibbSsus, tous
de 1 'gpoque imperiale; gibbula (Chir.), gibatus, -a, -um (Anth.904,13)?
Les 1 . roaanes attestent gibbus, *gibbulus, et des d^foraations
*gimbus (gimberosus CGL III 630,74, gembrOsus Isid.Quaest. test. 48,
p.aofib; cf .sambatus, sambucus, etc.), *gubbus, *gumbjis, *glilbus (roua.
gheb, cf. Graur, Mei.ling.36), un derive *gibberutus, M.L.3755,3754, 3753 «
L 1 eaploi de gibber coaae adj. et subst. a son correspondant dans
1’eaploi de uber, et de p&ber.
Mot expressif que M.Trautaann, KZ 43,373, a rapproche de lette
gibstu, gibt "se courber", gibbis "bossu" et de v.sl.feet/r "de tra —
vers, bossu". La forae geraanique usuelle est v.isl .skeifr, v.angl.
scSf "de travers". Cf. v.isl. kippa "reculer". La forne *gubbus attest^e
par des langues roaanes et le vgnitien gufo indiquent une interfgrence
avec gr. xucpoc "courbe en avant", xucpoc "bosse". - Les aots qui de¬
signent cette infimite ont ailleurs des foraes voisines: skr.kubjdh
"bossu", pers. k&£, et a.h.a .hogger.
gigarus, -I a«(?): draconteua, serpentine. Gaulois d'aprbs Mar¬
cellus, Med.10,58.
```


## [2026-09-05T21:05:21.916Z] TOOL CALL #99: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n'); leaf=0;m={}\nfor i,l in enumerate(lines,1):\n    m[i]=leaf; leaf+=l.count('\\f')\nprint('kiosk line 20716 leaf',m[20716])\npages=t.split('\\f')\nimport re\nprint(re.findall(r'(?m)^\\s*(8[0-9]{2})\\s*$', pages[m[20716]])[:6])\nprint(pages[m[20716]][:300])\nEOF\necho \"=== klein gyre/gyroscope\"; grep -n \"gyroscope\\|gyre, n\" KLN_1966.txt | head -5"
}
```


### [2026-09-05T21:05:23.977Z] TOOL RESULT

```
kiosk line 20716 leaf 456
['848']
 n.,  a  kind  of  East  Indian  brocade.
Hind,  kimkhab,  fr.  Pers.  kimkhdb. kind,  n.  —  ME.  kinde,  kund,  kende,  fr.  OE.  cynd, ge-cynd,  ‘kind,  nature,  quality,  manner,  origin, generation,  offspring’,  rel.  to  OE.  cyn,  ‘kind, kin’.  See  kin  and  cp.  kind,  adj. kind,  adj.  — 
=== klein gyre/gyroscope
16956:gyrocompass,  n.,  a  compass  with  gyroscope.  — Compounded  of  gyro  and  -compass, gyrograph,  n.,  an  instrument  for  recording  re¬ volutions  of  a  wheel,  etc.  —  Compounded  of gyro-  and  Gk.  -ypt^op,  fr.  ypc^Eiv,  ‘to  write’. See  -graph.
16959:gyroplane,  n.,  a  flying  machine  furnished  with rotating  horizontal  planes.  —  Compounded  of gyro-  and  plane,  ‘airplane’, gyroscope,  n.,  a  heavy  rotating  wheel,  having  its axis  free  to  turn  in  any  direction.  —  Compound¬ ed  of  gyro-  and  Gk.  -oxomov,  fr.  oxo-sw,  ‘to look  at,  examine’.  See  -scope.
16960:Derivative:  gyroscop-ic,  adj. gyrostat,  n.,  a  modified  form  of  a  gyroscope.  — Compounded  of  gyro-  and  Gk.  ora-roc,  ‘placed; standing’.  See  static  and  cp.  aerostat,  and  words there  referred  to.  N
```


## [2026-09-05T21:05:28.940Z] TOOL CALL #100: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"gyro-,\\|gyre,\\|yupo?,\\|ypp\" KLN_1966.txt | head -5; sed -n '16950,16956p' KLN_1966.txt"
}
```


### [2026-09-05T21:05:29.007Z] TOOL RESULT

```
3395:argand  lamp.  —  Named  after  its  inventor  Aim6 Argand,  a  Swiss  physicist  (1755-1803). Argemone,  n.,  a  genus  of  plants  of  the  poppy family  (bot.)  —  Gk.  apyEpuivT),  ‘a  kind  of  pop¬ py’,  prob.  fr.  Heb.  argamdn,  ‘purple’.  Cp.  Ak¬ kad.  argamannu,  of  s.m.  Cp.  also  agrimony.  For the  ending  -cow)  in  apye|ic I>vr),  cp.  dcvspuiw),  ‘the wind  flower’  (see  anemone). argent,  n.,  silver  (archaic).  —  F.,  fr.  L.  argentum, ‘silver’,  which  is  cogn.  with  Gk.  Spyupo?,  ‘silver’, prop,  ‘the  white  (metal)’,  fr.  dpyo?  (dissimul¬ ated  fr.  *ipypo?),  ‘shining,  bright,  white’;  fr. I.-E.  base  *arg-,  ‘to  shine’,  whence  also  OI. rirdh,  ‘shining,  glowing,  bright’,  rajatam ,  Aves¬ tic  ‘r*zata,  ‘silver’,  OI.  drjunah,  ‘shining,  white’, Toch.  A  drki,  ‘white’  (said  of  teeth),  arkyant, ‘silver’,  B  arkwi,  of  s.m.,  arkwirme,  ‘light  color’, Hitt,  harkish.  ‘bright,  clear’,  Thracian  4pytX<x;,
3416:argyrite,  n.,  argentite  (mineral.)  —  Formed  with subst.  suff.  -ite  fr.  Gk.  apyupop,  ‘silver’.  See argyro-  and  cp.  argentite. argyro-,  before  a  vowel  argyr-,  combining  form meaning  ‘silver’.  —  Gk.  txpyupo-,  ipyup-,  fr. Sipyupop,  ‘silver’,  which  is  cogn.  with  L.  ar¬ gentum,  ‘silver’.  See  argent  and  cp.  the  second element  in  hydrargyrum, argyrodite,  n.,  a  steel  gray  mineral  containing  sil¬ ver,  geranium  and  sulfur  (mineral.)  —  G.  Ar- gyrodit,  coined  by  its  discoverer  the  German chemist  Aloys  Auer  von  Welsbach  (1858-1929) fr.  Gk.  apyuptoSvjp,  ‘rich  in  silver’  (fr.  apyupop, ‘silver’,  and  -coSrjp,  ‘like’),  and  suff.  -f-nqp.  See argyro-,  -ode  and  subst.  suff.  -ite.
3446:arjun,  n.,  an  Asiatic  tropical  tree  (Terminalia  ar- juna).  —  Hind,  arjun,  fr.  OI.  arjunaft,  ‘white’, which  is  cogn.  with  Gk.  dcpyop,  ‘bright,  white’, dpyupo?,  ‘silver’,  L.  argentum,  ‘silver’.  See
4045:autogiro,  n.,  a  type  of  airplane.  —  Sp.,  compound¬ ed  of  auto-  and  Gk.  yupo?,  ‘ring’.  See  gyre, autointoxication,  n.,  self-poisoning  ( med .)  — Compounded  of  auto-  and  intoxication, automatic,  adj.  —  Formed  with  suff.  -ic  fr.  Gk. ocux6(xaxoi;  (see  automaton);  first  used  by  the English  physician  and  philosopher  David  Hart¬ ley  (1705-57)  in  1748.
7937:Clio,  n.,  the  Muse  of  history  (Greek  mythol .)  — L.  Clio,  fr.  Gk.  KXeuo,  lit.  ‘the  proclaimed,  fr. xXsieiv,  xXsav,  ‘to  tell  of,  celebrate,  make famous’,  fr.  xXso?,  ‘fame,  flory’.  See  loud  and cp.  cledonism,  and  the  first  element  in  Clianthus. clip,  tr.  and  intr.  v.,  to  embrace  (archaic.)  — ME.  clippen,  cluppen,  fr.  OE.  clyppan ,  ‘to  em¬ brace,  love’,  rel.  to  OFris.  kleppa,  of  s.m., OHG.  klaftra,  MHG.  klafter,  G.  Klafter,  MLG. klachter,  ‘fathom’,  lit.  ‘the  outstretched  arms’, and  cogn.  w’ith  Lith.  glebys,  ‘armful’,  gldbiu, globti,  ‘to  embrace,  support’,  Lett,  glabt,  glebt, ‘to  protect’,  L.  gleba,  ‘clod’,  globus,  ‘ball,  sphere’. See  clamp,  ‘a  device  for  fastening’,  and  cp.  words there  referred  to.
gypseous,  adj,  1)  containing  gypsum;  2)  resem¬ bling  gypsum.  —  L.  gvpseus,  ‘of  gypsum’,  fr. gypsum.  See  gypsum  and  -ous. gypsiferous,  adj,  producing  gypsum.  —  See gypsum  and  -ferous.
Gypsophila,  n,  a  genus  of  plants  of  the  pink family  (bot)  —  ModL,  compounded  of  Gk. yuil*/?,  ‘chalk,  gypsum’,  and  9Uelv,  ‘to  love’. See  gypsum  and  philo-. gypsous,  adj.  —  A  var.  of  gypseous, gypsum,  n.  —  L,  fr.  Gk.  yuij/oc,  ‘chalk’,  of  Sem. origin.  Cp.  Arab,  jibs,  Mishnaic  Heb.  gebhes, gephes,  ‘plaster,  mortar,  gypsum’,  which  prob. derive  fr.  Akkad,  gassu  (whence  also  Aram. gassd,  whence  Arab,  jass,  jiss,  juss,  qa$s,  qisf), ‘gypsum’.  —  Cp.  gesso.
gypsy,  gipsy,  n.  —  Fr.  earlier  gypcian,  aphetized fr.  still  earlier  Egypcian,  ‘Egyptian,  gypsy’,  fr. OF.  Egyptien  (F.  £gyptien),  fr.  L.  Aegyptianus, ‘Egyptian’.  See  Egyptian  and  cp.  gitano.  Cp. aiso  gyp.
Derivatives:  gypsy,  intr.  v,  gypsy-ish,  adj. gyr-,  form  of  gyro-  before  a  vowel, gyral,  adj,  moving  in  a  gyre  or  circle.  —  Formed with  adj.  suff.  -al  fr.  L.  gyrus.  See  gyre. Derivative:  gyral-ly,  adv. gyrate,  intr.  v,  to  revolve.  —  L.  gyrdtus,  ‘cir¬ cular’,  pp.  of  gyrare,  ‘to  turn  round  in  a  circle’.
fr.  gyrus.  See  next  word  and  verbal  suff.  -ate. Derivatives:  gyrat-ion,  n„  gyrat-ion-al,  gyrat¬ ory,  adjs.
gyre,  n,  a  circular  motion.  —  L.  gyrus,  fr.  Gk. yupo<;,  ‘circle,  ring’,  which  is  rel.  to  yiipop, ‘rounded,  curved’,  and  cogn.  with  Arm.  kor, ‘crooked’,  kurn,  ‘the  back’,  Lith.  gurnets,  hip, ankle,  bone’,  Norw.  kaure,  ‘a  curly  lock  of  hair’, Swed.  kura,  Dan.  kure,  ‘to  squat’,  MLG.  kuren, ‘to  lie  in  wait’,  G.  kauern,  ‘to  squat,  cower’.  All these  words  are  derivatives  of  I.-E.  *geu-r-,  an -/•-enlargement  of  base  *geu-,  ‘to  bend,  curve, arch’.  See  cove,  ‘a  small  bay’,  and  cp.  cower.  Cp. also  gyrus,  the  first  element  in  girandole,  virelai, and  the  second  element  in  autogiro,  circumgyrate, helicogyre.  Cp.  also  Gyps, gyre,  intr.  v,  to  gyrate.  —  L.  gyrare,  ‘to  turn round  in  a  circle’,  fr.  gyrus.  See  gyre,  n. gyrfalcon,  n.  —  A  var.  of  gerfalcon, gyro-,  combining  form  meaning  ‘circle,  circular, spiral’.  - — •  Gk.  yupo-,  fr.  yupop,  ‘circle’.  See gyre,  n.
gyrocompass,  n.,  a  compass  with  gyroscope.  — Compounded  of  gyro  and  -compass, gyrograph,  n.,  an  instrument  for  recording  re¬ volutions  of  a  wheel,  etc.  —  Compounded  of gyro-  and  Gk.  -ypt^op,  fr.  ypc^Eiv,  ‘to  write’. See  -graph.
```


## [2026-09-05T21:05:39.714Z] TOOL CALL #101: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"geu-.*biegen\\|biegen.*wölben\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -5; echo \"=== IEC\"; grep -n \"gūros\\|geuros\\|gū̆ros\\|gouno\" IEC.txt | head -8"
}
```


### [2026-09-05T21:05:39.854Z] TOOL RESULT

```
19090:scheinlicber als *gu-ela zu *geu- „biegen“, s. Persson Beitr. 538 f. ; vgl. anord. 
34969:1. geu- „biegen, kriimmen, wolben" (ausfiihrlich Liden Arm. St. Ill — 122, 
35725:Berges" s. u. *geu- „biegen“), ags. gupan PI. „clunes, cloxae", ahd. goffa 
38376:St. 121, Petersson KZ. 47, 257: nicht zu gr. yvgog, Wz. *geu- „biegen“). 
38519:(oder mit Z-Suffix zu *geu- „biegen“?); 
=== IEC
```


## [2026-09-05T21:05:42.690Z] TOOL CALL #102: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '34969,34985p' incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt; echo \"--- gaona in WLD:\"; grep -n \"gaona\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -5"
}
```


### [2026-09-05T21:05:42.761Z] TOOL RESULT

```
1. geu- „biegen, kriimmen, wolben" (ausfiihrlich Liden Arm. St. Ill — 122, 
IF. 19, 318, 326 ff., 341 ff., Persson Beitr. 10<> ff.. 936f.). 

Unerweitert wohl in *goiid x - : gu- „Hand", s. d.; ferner norw. kaa „das 
Heu umdrehen, wenden", anord. I'd ,,einem die Ruhe storen"; ka-beinn 
„Krummbein“ ( *gouo -; Liden IF. 19, 318, 344; aber air. gait, go , ; Liige“ 
wohl mit lat. haucl zu verbinden); iiber gr. yvgg, yvTov, yva/.ov s. u. 

Mit Z-Suffixen: 

ai. gola-h „Kugel‘‘, gold, golam „Ball, runder Wasserkrug" (nicht nach 
Bartholomae IF. 3, 176, Uhlenbeck Ai. Wb. 83 aus *gloudos = dt. Klop , 
s. Petersson Stud, zu Fortunatovs Regel 27), womit an sich gr. yej.vi.6g 
„Melkeimer, Schopfeimer, Bienenkorb“ gleichsetzbar ware (s. Bezzenberger 
BB. 4, 322; Brugmann I 2 576 nimmt Ablaut on gegeniiber dt Kiel an, das 
-cm- enthalte; viel eher aber semitisch nach Lewy Fremdw. 150: hebr. 
gol, guild „0lkrug“; Spiegelberg KZ. 41, 132 nimmt agypt. Ursprung an; 
--- gaona in WLD:
35102:Av. gaona- n. ,,Haar (bes. der Tiere) ; (Ilaar)farbe - (vgl. oben lit. gau- 
40120:Av. gunaoiti ,.verschafft“, gaona- m. ,,Gewinn", zunachst (Bartholomae
```


## [2026-09-05T21:07:00.458Z] TOOL CALL #103: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"gunda-\\|gunda\\b\\|Teigballen\\|Teig'\" BRT.txt | head -10"
}
```


### [2026-09-05T21:07:00.502Z] TOOL RESULT

```
10408:•  j.  gunda-  m.,  gundä-  f.  'zum  Backen ! angerührtes  Mehl,  Mehlteig,  Te igb allen' :  | yat  'ds  d-:iyäl  "wenn  der  Teig  (zum  Backen) ' zurecht  gelegt  wird"  V.?.32j — lia  miimHl ..nmlne  ai)ih3i  "lAy.?/"  "hier  soll  dauernd im  Haus  vorhanden  sein  von  diesem  Mehl-  \ teig"  V.,j.32.  I
26381:gunda-.     Anders  bei  Gdn.  KZ.  24. 549,  Ggr.
```


## [2026-09-05T21:07:02.579Z] TOOL CALL #104: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg176.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/176.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/ | head"
}
```


### [2026-09-05T21:07:02.654Z] TOOL RESULT

```
total 6496
drwxrwxr-x  2 sfmqrb sfmqrb   4096 Sep  5 17:07 .
drwxrwxr-x 11 sfmqrb sfmqrb   4096 Sep  5 16:42 ..
-rw-rw-r--  1 sfmqrb sfmqrb  71589 Sep  5 10:46 100.png
-rw-rw-r--  1 sfmqrb sfmqrb 104864 Sep  4 19:03 101.png
-rw-rw-r--  1 sfmqrb sfmqrb  68145 Sep  5 10:49 102.png
-rw-rw-r--  1 sfmqrb sfmqrb  79623 Sep  5 10:55 103.png
-rw-rw-r--  1 sfmqrb sfmqrb  78826 Sep  5 10:59 104.png
-rw-rw-r--  1 sfmqrb sfmqrb  82500 Sep  5 11:05 105.png
-rw-rw-r--  1 sfmqrb sfmqrb  55270 Sep  5 11:03 106.png
```


## [2026-09-05T21:07:14.664Z] TOOL CALL #105: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=10380 && NR<=10420' BRT.txt | grep -n \"^[0-9]\\{3\\}\\|^ *[0-9]\\{3\\} \" | head; sed -n '10400,10412p' BRT.txt | cut -c1-200"
}
```


### [2026-09-05T21:07:16.543Z] TOOL RESULT

```
•  j.    garapta-    Adj,    (fem.    'lä-),    VVlP.:\aAur3m    Tim  Yt.  70.25;  —  tattuATs'  Tii s.  grab-.  (näml  fravasays)  Yt.  /J.30.
KotnpE.  I      Vgl.  mp.  (Pü.)  iuj'r '),  shal.y'H^/O ;  gr,  ^üir^,  nhd.
dby  Google
5^5
guoda-
'grab-  3
A>4c«;  E.  dazu  Bgm.  IF.  it.  III").  —  ')  Das  I
i  des  mp.  i$ifr,  j  des  sbal.  Juki  stammt  von  1 iafr,  jahl  =  j.  ja/ta-.  —  i)  Falsch  JAOS.  i6.  \ XL,  MSL,  p.  379.  I
•  j.  gunda-  m.,  gundä-  f.  'zum  Backen ! angerührtes  Mehl,  Mehlteig,  Te igb allen' :  | yat  'ds  d-:iyäl  "wenn  der  Teig  (zum  Backen) ' zurecht  gelegt  wird"  V.?.32j — lia  miim
mp.  aiinil,  gtindai  |Pü.\  np.  spmda;  weiteres  i bei  Bthl.  IF.  ^.  zSi  und  zu  suhuK  —  i)  Bat  ' an  Stelle  des  Gen.  {part.,  als  Subj.;;    s.  ebd. ;
•  j-,  g.  guzra-  Adj.  'verborgen,  geheim';  [ sp»i!i-l  vidvä  yaSclt  'rä  (NF.)  s}ngh^i7ihö\ .,  vaiihSus  xraiwä  ffia«a«-4J  "der  heilige, der  auch  die  geheimen  Lehren  kennt, 
KompA.)?).  —  Zum  V.  ^112..  —  Fü,;  mh'i- mkä,  nihih'k.  —  I)  Hds.  giilia,  vgl.  ZDMC. 48.   514.  I
•  j.  *guzra-sai*ha-  m.  'geheime  Lehre':  I -hö  F. je.  !
```


## [2026-09-05T21:07:22.336Z] AGENT

Now I have enough evidence. Let me write the verification file.


## [2026-09-05T21:17:02.300Z] TOOL CALL #106: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk176.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\n\nW = \"https://en.wiktionary.org/wiki/\"\n\nnodes = []\n\ndef N(**kw):\n    nodes.append(kw)\n\nN(id=1, lang=\"Avestan\", words=\"gaošaka\", verdict=\"plausible\",\n  derivation=\"The form is Horn's reconstruction, not an attested Avestan word. Horn, Grundriss der neupersischen Etymologie no. 945 (p. 211) heads the entry 'gōše \\\"Winkel, Ecke\\\"' and reconstructs 'aw. *gaošaka-'; Mo'in copied it into his footnote on گوشه in Borhan-e Qate' p. 1859 as 'اوستا °gaošaka' (the ° is Mo'in's asterisk-equivalent), and Nourai took it over, but dropped the asterisk, so the chart reads as if the word were attested. Bartholomae's Altiranisches Wörterbuch has no gaošaka-; the only Avestan gaoša- it knows (col. 485-486) is gaoša- m. 'Ohr' from the verb gaoš- 'to hear'. What IS attested is the New Persian word itself: Pokorny IEW 398, in the s-suffix section of the root geu- 'biegen, krümmen, wölben', lists plainly 'npers. gōšā \\\"Winkel, Ecke\\\"' beside gr. gyēs, so the *geu-s- assignment (not the Avestan intermediary) is Pokorny's. Phonetically OIran. *gauša-ka- > MP gōšag > NP gōše is regular (au > ō, intervocalic -k- > -g > -a). Verdict: the derivation is defensible and is the classical (Horn/Pokorny/Mo'in) view, but the node's Avestan form is a reconstruction and modern Wiktionary prefers a different parent (see node 2).\",\n  derivation_fa=\"«گوشه» را نورایی از صورتی اوستایی به‌نام gaošaka می‌گیرد، اما چنین واژه‌ای در اوستا گواهی نشده است: این صورت را نخست هرن در «بنیاد ریشه‌شناسی فارسی نو» (شمارهٔ ۹۴۵، ص ۲۱۱) با ستاره بازسازی کرد و معین آن را در حاشیهٔ «گوشه» در برهان قاطع (ص ۱۸۵۹) به شکل «اوستا °gaošaka» آورد؛ نورایی ستاره را انداخته و آن را چون واژه‌ای گواهی‌شده نشان داده است. در فرهنگ ایرانی باستانِ بارتولمه تنها gaoša- «گوش» (ستون ۴۸۵-۴۸۶) هست که از ریشهٔ gaoš- «شنیدن» است. در برابر، پوکورنی در ص ۳۹۸، زیر ریشهٔ geu- «خم شدن، برگشتن»، خودِ صورت فارسی نو را می‌آورد: «npers. gōšā \\\"Winkel, Ecke\\\"». پس نسبت‌دادن «گوشه» به این ریشه دیدگاه کلاسیک (هرن، پوکورنی، معین) است و پذیرفتنی می‌نماید، ولی گرهٔ اوستایی نمودار بازسازی است نه گواه.\",\n  sources=[W+\"%DA%AF%D9%88%D8%B4%D9%87\"],\n  ref_check=[{\"ref\":\"POK:398\",\"status\":\"supports\",\"note\":\"POK_02.txt leaf 54 (printed p. 398, verified by the '399' marker at the foot of the same leaf): 'g. Mit s-Suffixen: npers. gōšā ,Winkel, Ecke'; gr. γυης ,Krummholz am Pflug'…' — Pokorny does put Persian gōše under geu- 'biegen, krümmen, wölben', but he cites the New Persian word directly and reconstructs no Avestan *gaošaka-.\"}],\n  consulted=[\n    {\"src\":\"HRN\",\"where\":\"no. 945, p. 211 (HRN.txt line 8192, leaf 232)\",\"stance\":\"supports\",\"note\":\"'945. gōše \\\\'Winkel, Ecke\\\\'. … aw. *gaošaka-. kurd. gūš, gūse \\\\'Winkel\\\\'; bal. LW. gōšak (127).' — the asterisked reconstruction Nourai reproduces without the asterisk.\"},\n    {\"src\":\"BRT\",\"where\":\"col. 485-486 s.v. gaoša- (BRT.txt line ~29700)\",\"stance\":\"contradicts\",\"note\":\"'p. gauša-, j. gaoša-, g. *gauša- m. \\\\'Ohr\\\\' … Zum V. gaoš-' — no gaošaka- anywhere in the Altiranisches Wörterbuch; the only Avestan gaoša- means 'ear' and belongs to gaoš- 'to hear'.\"},\n    {\"src\":\"WLD\",\"where\":\"Bd. I 555 ff., '1. geu- „biegen, krümmen, wölben“' (WLD_Bd1 djvu line 34969)\",\"stance\":\"partial\",\"note\":\"the source article of Pokorny 393-398; it carries the s-suffix group but, like Pokorny, cites the New Persian form, not an Avestan one.\"}])\n\nN(id=2, lang=\"Persian\", words=\"gŭšeh «گوشه»\", verdict=\"plausible\",\n  derivation=\"NP گوشه gōše/guše 'corner, angle' is real and correctly glossed. Its parentage is genuinely contested. (a) The classical line — Horn 945, Mo'in's footnote in BQT 1859 ('اوستا °gaošaka … کردی gōše, بلوچی gōšak'), Pokorny 398, Lokotsch no. 732 — takes it from an old *gauša-ka- 'a bend, angle' belonging to PIE *geu-s- 'to bend', with Kurdish gūš/gōše and Baluchi gōšak as cognates. (b) Modern Wiktionary derives it instead from Middle Persian gwšk' /gōšag/ 'corner' seen as a suffixed formation of gōš 'ear' (< PIr. *gauša-, PIE *gʰews- 'to hear'), the ear being 'a lappet or protruding end'. MacKenzie's Concise Pahlavi Dictionary registers both without deciding: 'gōš [gws] ear' and 'gōšag [gwšk'] corner'. The two are formally identical (*gauša-ka-), so only the semantics separate them; nothing in the phonology decides. Nourai follows (a).\",\n  derivation_fa=\"«گوشه» واژه‌ای است اصیل و معنای «کنج، زاویه» برای آن درست است، اما ریشهٔ آن دو دیدگاه دارد. یک) خط کلاسیک — هرن (شمارهٔ ۹۴۵)، حاشیهٔ معین بر برهان قاطع ص ۱۸۵۹ («اوستا °gaošaka، کردی gōše، بلوچی gōšak»)، پوکورنی ص ۳۹۸ و لوکوچ شمارهٔ ۷۳۲ — آن را از ایرانی باستان *gauša-ka- «خمیدگی، زاویه» از ریشهٔ هندواروپایی *geu-s- «خم شدن» می‌گیرد. دو) ویکی‌واژه آن را از فارسی میانهٔ gōšag «گوشه» می‌داند که خود ساختِ پسوندی «گوش» (< *gauša-، از ریشهٔ *gʰews- «شنیدن») است، به معنای «کنارهٔ برآمده». مکنزی هر دو صورت gōš و gōšag را بی‌داوری ثبت کرده است. از نظر آوایی هر دو یکی است (*gauša-ka-) و تنها معنا آن‌ها را جدا می‌کند؛ ادعای نورایی با احتیاط پذیرفتنی است.\",\n  sources=[W+\"%DA%AF%D9%88%D8%B4%D9%87\", W+\"%DA%AF%D9%88%D8%B4\"],\n  ref_check=[{\"ref\":\"BQT:1859\",\"status\":\"supports\",\"note\":\"Borhan-e Qate' ed. Mo'in, printed p. 1859 (= pdf p. 656 of the vol.-3 scan, printed = pdf + 1203, calibrated on the '-۱۷۳۱-' header of pdf 528): Mo'in's footnote reads «گوشه ـ بضم اول و کسر سوم (در لهجهٔ مرکزی) و بفتح آن (در تلفظ قدیم)، اوستا °gaošaka. کردی gōše… بلوچی gōšak… کنج، زاویه ـ خلوت، خلوتگاه ـ کناره…». Exactly Nourai's node 1 → node 2 arrow.\"}],\n  consulted=[\n    {\"src\":\"PHD\",\"where\":\"p. 37 s.v. gōšag / gōš (PHD.txt line 382)\",\"stance\":\"partial\",\"note\":\"'gōš [gws | = M, N ~] ear.' and 'gōšag [gwšk' | N ~a] corner.' — MacKenzie lists the two side by side and offers no derivation, so he neither confirms nor refutes the *geu- assignment.\"},\n    {\"src\":\"MON\",\"where\":\"s.v. گوشه and s.v. کوشک (MON_part2.txt lines 36716, 28035)\",\"stance\":\"partial\",\"note\":\"«گوشه: (gōša) (اِ.) کنار، کناره، کران» — no etymology; but s.v. کوشک Mo'in writes «کوشک [= کوشه، گوشک ـ جوسق، معر.]», i.e. he treats کوشه/گوشک and کوشک as one word.\"},\n    {\"src\":\"LKT\",\"where\":\"no. 732, printed p. 58 (LKT.txt line 1789)\",\"stance\":\"supports\",\"note\":\"'732. Pers. gōšā: \\\\'Winkel, Ecke\\\\' [Horn NpEt S. 211, Nr. 945], tk. zu kjosk, kjöšk \\\\'Palast, Villa, Pavillon\\\\' geworden…' — Lokotsch bases the whole kiosk family on this Persian word.\"}])\n\nN(id=3, lang=\"Persian\", words=\"kŭšk «کوشک»\", verdict=\"plausible\",\n  derivation=\"NP کوشک kōšk 'pavilion, palace, castle' is attested from Middle Persian on: MacKenzie, Concise Pahlavi Dictionary, 'kōšk [kwšk' | N ~] pavilion, palace, kiosk'. Borhan-e Qate' p. 1731 defines it «بسکون ثانی بنای بلند را گویند و بعربی قصر خوانند» ('a tall building; Arabic qaṣr'), so Nourai's gloss 'a room at the top corner of a castle, castle' is his own paraphrase, coloured by the etymology he is arguing for. The link کوشه → کوشک is not Nourai's invention: it is de Lagarde's, transmitted by Horn 945 ('de Lagarde stellt auch kūšk \\\"Kiosk\\\" hierher, das, im türkischen Munde zu kjöšk geworden, als kušk und kūšk zu den Persern zurückgewandert sei'), and Mo'in supports it twice — the BQT 1731 footnote «کوشه، تاریخ سیستان ص ۳۲۹، ۳۳۸؛ پهلوی kushk… معرب آن جوسق» plus the remark «و در تاریخ سیستان \\\"کوشه\\\" بمعنی کوشک آمده», and the Farhang-e Farsi entry «کوشک [= کوشه، گوشک ـ جوسق، معر.]». Against this, Wiktionary simply starts from MP kōšk and gives it no further etymology. So: an old, well-attested proposal, not a proven one — the doubling کوشه/کوشک (ō-vowel plus a -k that is not the usual diminutive) remains unexplained.\",\n  derivation_fa=\"«کوشک» از فارسی میانهٔ kōšk «کاخ، غرفه» است (مکنزی: 'kōšk [kwšk'] pavilion, palace, kiosk')؛ برهان قاطع ص ۱۷۳۱ آن را «بنای بلند… و بعربی قصر خوانند» معنی کرده، پس معنای «اتاقِ گوشهٔ بالای قلعه» ترجمهٔ آزاد نورایی است. پیوند «گوشه ← کوشک» از دُلاگارد است که هرن (شمارهٔ ۹۴۵) نقل کرده و معین دو بار آن را تأیید کرده است: در حاشیهٔ ص ۱۷۳۱ «کوشه، تاریخ سیستان ص ۳۲۹، ۳۳۸؛ پهلوی kushk… معرب آن جوسق» و در فرهنگ فارسی «کوشک [= کوشه، گوشک]». در برابر، ویکی‌واژه فقط تا فارسی میانه پیش می‌رود و ریشه‌ای نمی‌دهد. بنابراین ادعا کهن و آبرومند است ولی قطعی نیست؛ دوگانگی «کوشه/کوشک» هنوز آوا‌شناسانه توضیح داده نشده است.\",\n  sources=[W+\"%DA%A9%D9%88%D8%B4%DA%A9\"],\n  ref_check=[{\"ref\":\"BQT:1731\",\"status\":\"supports\",\"note\":\"BQT printed p. 1731 (pdf 528 of the vol.-3 scan; the page carries the header «-۱۷۳۱-»). Entry: «کوشک … و بسکون ثانی بنای بلند را گویند و بعربی قصر خوانند»; Mo'in's footnote 6: «کوشه، تاریخ سیستان ص ۳۲۹، ۳۳۸، پهلوی kushk … (کلاه فرنگی بالای بنا، اطاق تابستانی)… معرب آن «جوسق» ابن درید» and, further down, «و در تاریخ سیستان «کوشه» بمعنی کوشک آمده». This is precisely the کوشه ↔ کوشک equation the chart draws, and the source of Nourai's script_extra «کوشه».\"}],\n  consulted=[\n    {\"src\":\"PHD\",\"where\":\"p. 51 s.v. kōšk (PHD.txt line 428; PHD_mackenzie.txt line 3333)\",\"stance\":\"supports\",\"note\":\"'kōšk [kwšk' | N ~] pavilion, palace, kiosk.' — the Middle Persian form exists exactly as required.\"},\n    {\"src\":\"HRN\",\"where\":\"no. 945, p. 211\",\"stance\":\"supports\",\"note\":\"'de Lagarde, Ges. Abh. stellt auch kūšk \\\\'Kiosk\\\\' hierher, das, im türkischen Munde zu kjöšk geworden, als kušk und kūšk zu den Persern zurückgewandert sei; arab. LW. jausaq, syr. LW. … \\\\'Kiosk\\\\' sprechen dafür.'\"},\n    {\"src\":\"MON\",\"where\":\"s.v. کوشک (MON_part2.txt line 28035)\",\"stance\":\"supports\",\"note\":\"«کوشک: [= کوشه، گوشک ـ جوسق، معر.] (اِ.) بنای مرتفع و عالی، قصر، کاخ، قلعه، حصار.»\"}])\n\nN(id=4, lang=\"Turkish\", words=\"kiošk\", verdict=\"confirmed\",\n  derivation=\"Persian کوشک kōšk was taken into Ottoman Turkish as كوشك köşk 'pavilion, garden house, summer palace'; the Persian ō was rendered by Turkish ö and the final -k palatalised, giving modern Turkish köşk (definite accusative köşkü). Klein s.v. kiosk: 'F. kiosque, fr. Turk. kiöshk, \\\"pavilion\\\", fr. Pers. kushk, \\\"palace\\\"'; Etymonline: 'from Turkish koshk, kiöshk \\\"pavilion, summer house,\\\" from Persian kushk \\\"palace, villa; pavilion, portico\\\"'; Wiktionary s.v. köşk: 'From Ottoman Turkish كوشك (köşk), from Classical Persian کوشْک (kōšk, \\\"palace, portico\\\")'. The word denoted the open garden pavilions of Ottoman palaces (Topkapı's Çinili Köşk, 1472).\",\n  derivation_fa=\"فارسی «کوشک» به ترکی عثمانی وام رفت و به صورت كوشك (köşk) «غرفه، کاخ تابستانی، کلاه‌فرنگی» درآمد؛ واکهٔ ō فارسی در ترکی به ö بدل شد و کاف پایانی پیشین‌شده تلفظ گردید. کلاین (ذیل kiosk) می‌نویسد «ترکی kiöshk از فارسی kushk»، و ویکی‌واژه: «از ترکی عثمانی كوشك، از فارسی کلاسیک کوشک». این واژه در عثمانی نام غرفه‌های باغیِ کاخ‌ها بود (مانند چینیلی کوشکِ توپکاپی، ۸۷۶ق/۱۴۷۲م). ادعای نورایی درست است.\",\n  sources=[\"https://www.etymonline.com/word/kiosk\", W+\"k%C3%B6%C5%9Fk\"],\n  ref_check=[{\"ref\":\"KLN:847\",\"status\":\"supports\",\"note\":\"Klein, A Comprehensive Etymological Dictionary (1966), the leaf carrying printed pp. 847-848 (KLN_1966.txt line 20716, leaf 456, whose page number '848' is printed on it): 'kiosk, also kiosque, n., an open pavilion or summerhouse; an open building used as a newsstand. — F. kiosque, fr. Turk. kiöshk, \\\\'pavilion\\\\', fr. Pers. kushk, \\\\'palace\\\\'.' Exactly the chain of nodes 3 → 4 → 5 → 7.\"}],\n  consulted=[\n    {\"src\":\"LKT\",\"where\":\"no. 732, p. 58\",\"stance\":\"supports\",\"note\":\"'Pers. gōšā … tk. zu kjosk, kjöšk \\\\'Palast, Villa, Pavillon\\\\' geworden; hieraus bulg. kosk \\\\'Gartenhaus\\\\', serb. ćošak \\\\'Söller\\\\', poln. kiosk, russ. kiosk; it. chiosco, frz. kiosque, sp. kiosco…'\"},\n    {\"src\":\"DEV\",\"where\":\"cited by Lokotsch as 'Devic DEt 149'\",\"stance\":\"supports\",\"note\":\"Devic's Dictionnaire étymologique des mots français d'origine orientale is Lokotsch's authority for the French kiosque < Turkish route; the reference is given at LKT no. 732.\"}])\n\nN(id=5, lang=\"French\", words=\"kiosque\", verdict=\"confirmed\",\n  derivation=\"French kiosque, first attested in the 17th c. (Etymonline: 1620s in English, 'from French kiosque (17c.)'), is the Turkish köşk borrowed into western Europe together with the Ottoman garden pavilions that became fashionable ornaments in French and English parks. Wiktionary's etymology tree for کیوسک routes it Ottoman Turkish köşk > Italian chiosco > French kiosque; Klein and Etymonline take French straight from Turkish. Either way the French word is the pivot from which the modern international word spreads (German Kiosk, Polish/Russian kiosk, Romanian chioşc). The later French sense 'newsstand' (1865) is a metonymy on the shape of the little pavilion.\",\n  derivation_fa=\"واژهٔ فرانسویِ kiosque در سدهٔ ۱۷م همراه با مدِ غرفه‌های باغیِ عثمانی به اروپای غربی راه یافت. ویکی‌واژه مسیر را «ترکی عثمانی köşk ← ایتالیایی chiosco ← فرانسوی kiosque» می‌داند و کلاین و اتیمانلاین آن را یکراست از ترکی می‌گیرند. همین صورت فرانسوی است که واژه را جهانی کرد (آلمانی Kiosk، لهستانی و روسی kiosk، رومانیایی chioşc). معنای «دکهٔ روزنامه‌فروشی» در فرانسوی از ۱۸۶۵م و بر پایهٔ شباهت شکل پدید آمد. ادعای نورایی درست است.\",\n  sources=[\"https://www.etymonline.com/word/kiosk\", W+\"%DA%A9%DB%8C%D9%88%D8%B3%DA%A9\"],\n  ref_check=[{\"ref\":\"None\",\"status\":\"not_checked\",\"note\":\"the chart cites no reference for this node; the link is covered by Klein p. 847 (cited on the flanking nodes 4 and 7) and by Etymonline, both archived.\"}],\n  consulted=[\n    {\"src\":\"KLN\",\"where\":\"pp. 847-848 s.v. kiosk\",\"stance\":\"supports\",\"note\":\"'F. kiosque, fr. Turk. kiöshk' — French is explicitly the intermediary between Turkish and English.\"},\n    {\"src\":\"LKT\",\"where\":\"no. 732, p. 58\",\"stance\":\"supports\",\"note\":\"'…it. chiosco, frz. kiosque, sp. kiosco, rum. chioşc \\\\'Verkaufsbude\\\\'… dtsch. Kiosk, ndl. engl. kiosk \\\\'dass.\\\\''\"}])\n\nN(id=6, lang=\"Persian\", words=\"kîŭsk «کیوسک»\", verdict=\"confirmed\",\n  derivation=\"A round trip: Persian کوشک kōšk > Ottoman Turkish köşk > (Italian chiosco >) French kiosque > modern Persian کیوسک kiyusk 'kiosk, newsstand, telephone box'. The modern Persian form betrays its European route by its shape: ki- for the French ki-, -u- for the French -o-, and the -sk cluster, none of which could come out of کوشک by Persian sound change. Mo'in's Farhang-e Farsi says so in one bracket: «کیوسک: [از ف. کوشک]», i.e. 'from French, [which is] from کوشک'. Wiktionary states it as an etymology tree ending 'French kiosque > Persian کیوسک' and labels کیوسک a doublet of کوشک.\",\n  derivation_fa=\"این گره یک «سفرِ رفت و برگشت» است: فارسی «کوشک» ← ترکی عثمانی köşk ← (ایتالیایی chiosco ←) فرانسوی kiosque ← فارسی نوِ «کیوسک». خودِ صورتِ امروزی گواهِ راهِ اروپایی آن است: کی- در برابر ki- فرانسوی، واکهٔ ـو- در برابر -o-، و خوشهٔ پایانی ـسک؛ هیچ‌یک از این‌ها با تحول آوایی درون‌فارسی از «کوشک» به دست نمی‌آید. معین در فرهنگ فارسی همین را در یک قلاب آورده است: «کیوسک: [از ف. کوشک]». ویکی‌واژه نیز «کیوسک» را دوگانهٔ (doublet) «کوشک» می‌خواند. ادعای نورایی درست است.\",\n  sources=[W+\"%DA%A9%DB%8C%D9%88%D8%B3%DA%A9\"],\n  ref_check=[{\"ref\":\"MON:3160\",\"status\":\"partial\",\"note\":\"Mo'in's entry is exactly as Nourai claims — MON_part2.txt line 29109: «کیوسک: [از ف. کوشک] (اِ.)» — but the page number cannot be checked: the only scan on disk is the 2-volume Adena reprint, whose pagination differs from the 6-volume Amir Kabir edition Nourai cites. The place of the entry in the alphabet (کیوسک at 3160 < گنبد at 3396 < گون at 3473) is internally consistent with his other MON citations.\"}],\n  consulted=[\n    {\"src\":\"MON\",\"where\":\"s.v. کیوسک (MON_part2.txt line 29109)\",\"stance\":\"supports\",\"note\":\"«کیوسک: [از ف. کوشک] (اِ.)»\"},\n    {\"src\":\"KLN\",\"where\":\"pp. 847-848 s.v. kiosk\",\"stance\":\"partial\",\"note\":\"Klein gives the outward journey (Pers. > Turk. > Fr. > Eng.) but, being an English dictionary, says nothing about the re-borrowing into Persian.\"}])\n\nN(id=7, lang=\"English\", words=\"kiosk\", verdict=\"confirmed\",\n  derivation=\"English kiosk is first recorded in the 1620s in the sense 'kind of open pavilion' (of light wood, often on pillars), borrowed from French kiosque; Ottoman-style pavilions were put up as garden ornaments in western Europe in the 17th c. The sense 'street newsstand' follows the French in 1865, and the modern everyday sense owes much to the British telephone kiosk of 1928. Klein p. 847 gives the same chain (F. kiosque < Turk. kiöshk < Pers. kushk).\",\n  derivation_fa=\"واژهٔ انگلیسی kiosk نخستین بار در دههٔ ۱۶۲۰م به معنای «غرفهٔ باز» (از چوب سبک و بر ستون) از فرانسویِ kiosque وام گرفته شد؛ در سدهٔ ۱۷م چنین غرفه‌هایی به سبک عثمانی در باغ‌های اروپای غربی می‌ساختند. معنای «دکهٔ روزنامه‌فروشی» در ۱۸۶۵م به پیروی از فرانسوی پدید آمد و معنای امروزی بیشتر از «کیوسک تلفنِ» بریتانیایی (۱۹۲۸م) مایه گرفته است. کلاین (ص ۸۴۷) همین زنجیره را می‌آورد. ادعای نورایی درست است.\",\n  sources=[\"https://www.etymonline.com/word/kiosk\"],\n  ref_check=[{\"ref\":\"KLN:847\",\"status\":\"supports\",\"note\":\"KLN_1966.txt line 20716 (leaf 456, printed pp. 847-848): 'kiosk, also kiosque, n., an open pavilion or summerhouse; an open building used as a newsstand. — F. kiosque, fr. Turk. kiöshk, \\\\'pavilion\\\\', fr. Pers. kushk, \\\\'palace\\\\'.'\"}],\n  consulted=[\n    {\"src\":\"KLN\",\"where\":\"pp. 847-848\",\"stance\":\"supports\",\"note\":\"see ref_check.\"},\n    {\"src\":\"LKT\",\"where\":\"no. 732, p. 58\",\"stance\":\"supports\",\"note\":\"'…dtsch. Kiosk, ndl. engl. kiosk \\\\'dass.\\\\''\"}])\n\nN(id=8, lang=\"Avestan\", words=\"gaona; hamo-gaona; nî-gaona\", verdict=\"plausible\",\n  derivation=\"Avestan gaona- is well attested and correctly glossed: Bartholomae, AiWb col. 481-482, 'j. ¹gaona- n. 1) \\\"Haar\\\" … a) \\\"Haarfarbe, Farbe\\\" … 3) \\\"Art und Weise\\\" (nur Komp.)', with the note 'afγ. γūna \\\"Haar; Farbe\\\", oss. γun \\\"Haar; Farbe (des Haars)\\\"; mp. gōn, np. gūn \\\"Farbe\\\"'. hamō-gaona- 'of one/all colour(s)' is likewise in Bartholomae (AiWb 1774/1776, Yt. 8.58 'kācit vā gaonanąm hamō.gaonəm'). nī-gaona- 'downward', by contrast, is NOT an attested Avestan compound; it is back-projected from Middle Persian nigūn, and even there the second element is more probably not gōn 'colour' (see node 10). The root attachment is Pokorny's: IEW 398, 'e. Mit n-Suffix: gou-no-m \\\"Gekräuseltes, Gewölbtes\\\". Av. gaona- n. \\\"Haar (bes. der Tiere); (Haar)farbe\\\" (vgl. oben lit. gaurai usw.)', i.e. 'hair' as 'the curly, the arched thing' from *geu- 'to bend'. Wiktionary offers this as one of two options and prefers 'perhaps related to Sanskrit guṇa \\\"thread, cord\\\", with further origin beyond Indo-Iranian uncertain… possibly from the BMAC substrate'. Hence plausible rather than confirmed.\",\n  derivation_fa=\"واژهٔ اوستایی gaona- گواهی‌شده و معنای آن در نمودار درست است: بارتولمه (ستون ۴۸۱-۴۸۲) آن را «۱) مو، ۲) رنگِ مو، رنگ، ۳) گونه و شیوه (تنها در ترکیب)» می‌آورد و می‌افزاید «پشتو γūna، آسی γun، فارسی میانه gōn، فارسی نو گون». ترکیبِ hamō-gaona- «هم‌رنگ، هر رنگ» نیز در فرهنگ بارتولمه (شمارهٔ ۱۷۷۴/۱۷۷۶، یشت ۸:۵۸) هست. اما nī-gaona- در اوستا گواهی نشده و بازسازی‌ای است از روی «نگون» فارسی میانه. نسبت‌دادن gaona- به ریشهٔ *geu- از پوکورنی است (ص ۳۹۸، بخشِ پسوندِ -n-: «gou-no-m: چیزِ پیچیده و برآمده؛ اوستایی gaona-»). ویکی‌واژه این را یکی از دو احتمال می‌داند و بیشتر به پیوند با سنسکریت guṇa «رشته، تار» یا زیرلایهٔ BMAC گرایش دارد. پس ادعای نورایی با احتیاط پذیرفتنی است.\",\n  sources=[W+\"%DA%AF%D9%88%D9%86\"],\n  ref_check=[\n    {\"ref\":\"SYN:1051\",\"status\":\"supports\",\"note\":\"Buck, Dictionary of Selected Synonyms, §15.61 COLOR (SYN.txt line 26592-26626; §15.61 falls on printed p. 1051 of the 1949 edition): the table lists 'Av. gaona-' for 'color', and the note reads 'Av. gaona- \\\\'hair\\\\', also \\\\'color\\\\' (Yt. 8.58; cf. Afgh. γūna \\\\'hair, color\\\\', NPers. gūn \\\\'color\\\\') : Lith. gaurai \\\\'hair\\\\', etc. (4.14). Walde-P. 1.557. Barth. 482.' Both of Nourai's glosses, in one sentence.\"},\n    {\"ref\":\"SNS:90\",\"status\":\"supports\",\"note\":\"Tavoosi, Vāže-nāme-ye Šāyast ne Šāyast: the index (SNS.txt line 29113) gives 'harao-gaona 54/16-90/7', i.e. an entry at p. 90 line 7, and the corresponding gloss (SNS.txt line 4663) reads «hamōgōn/hamōgōn … (AiWb. 1776) ?hamō.gaona-», with «ham-gūna» and Mir. Man. hamgwng. This is exactly the hamō-gaona- of node 8.\"}],\n  consulted=[\n    {\"src\":\"BRT\",\"where\":\"col. 481-482 s.v. ¹gaona- (BRT.txt lines 9798-9808)\",\"stance\":\"supports\",\"note\":\"'j. ¹gaona- n. 1) \\\\'Haar\\\\' … a) \\\\'Haarfarbe, Farbe\\\\': pasūm … aurušīm vā … kācit vā gaonanąm hamōgaonəm Yt. 8.58 … 3) \\\\'Art und Weise\\\\' (nur Komp.). — afγ. γūna \\\\'Haar; Farbe\\\\', oss. γun; mp. gōn, np. gūn \\\\'Farbe\\\\'.'\"},\n    {\"src\":\"WLD\",\"where\":\"Bd. I 557 (WLD_Bd1 djvu line 35102)\",\"stance\":\"supports\",\"note\":\"'Av. gaona- n. „Haar (bes. der Tiere); (Haar)farbe“ (vgl. oben lit. gau[rai])' — under '1. geu- „biegen, krümmen, wölben“', the source of Pokorny 398.\"},\n    {\"src\":\"SYN\",\"where\":\"§4.14 HAIR (SYN.txt lines 5376-5407)\",\"stance\":\"supports\",\"note\":\"'Lith. gauras… : Lett. gauri…, also with different suffix Av. gaona- \\\\'hair\\\\', root *geu-, perh. the same as in Grk. γυρός \\\\'round, curved\\\\', etc. Walde-P. 1.557.' — Buck explicitly ties gaona- to the same *geu- that gives Greek gyros (node 21).\"}])\n\nN(id=9, lang=\"Sogdian\", words=\"gwn`k\", verdict=\"confirmed\",\n  derivation=\"Gharib's Sogdian Dictionary entry 4383 reads 'γwn'y B — γōne (γwn'yy, γwn'y) © < Av. gaona ⇒ γwn'k — hair', with the parallel entry 4385 '-γwn'k … γōnč © < *gaunaka © as suffix in compounds ('nyγwn', wyδγwnc, cγwny, wyspγwn'y) — like, similar to' and 4386 'γwn'k pwn'kh — hair pore'. Sogdian γ- is the regular Sogdian reflex of Old Iranian initial *g- before a back vowel (spirantisation), and *gauna-ka- gives γwn'k /γōnak/. Strictly the Sogdian word is not descended from Avestan but is the sister Middle Iranian outcome of the same Old Iranian *gauna-; Gharib's '< Av. gaona' is a comparandum, exactly as Nourai's arrow is to be read.\",\n  derivation_fa=\"در فرهنگ سغدیِ بدرالزمان قریب، مدخل ۴۳۸۳ چنین است: «γwn'y — γōne © < اوستا gaona ⇒ γwn'k — مو»، و مدخل ۴۳۸۵ صورت پسوندیِ -γwn'k / γōnč «همانند، به‌گونهٔ» از *gaunaka را می‌آورد. گافِ ایرانی باستان در آغاز واژه در سغدی به‌طور قاعده‌مند به γ (غین) سایشی بدل می‌شود، پس *gauna-ka- > γwn'k. به‌دقت باید گفت واژهٔ سغدی از اوستایی نیامده، بلکه هر دو بازماندهٔ ایرانی باستانِ *gauna- هستند و «< Av. gaona» در فرهنگ قریب نشانهٔ هم‌ریشگی است، نه سرچشمه. ادعای نورایی در این حد درست است.\",\n  sources=[],\n  ref_check=[{\"ref\":\"SOD:174\",\"status\":\"supports\",\"note\":\"Gharib, Sogdian-Persian-English Dictionary, entry 4383 (SOD_pages.txt line 16224, between the printed page markers '174' at line 16160 and '176' at line 16293, i.e. printed p. 174/175): «4383 γwn'y B — γōne (γwn'yy, γwn'y) © < Av. gaona ⇒ γwn'k / hair / Bailey, Prolexis. 74; EGS ii 90; TSP 2.296 n p173». Nourai's page number lands on or within one page of the entry.\"}],\n  consulted=[\n    {\"src\":\"SOD\",\"where\":\"entries 4383, 4385, 4386\",\"stance\":\"supports\",\"note\":\"see ref_check; 4385 '-γwn'k … < *gaunaka … like, similar to' shows the same suffixed stem Nourai's γwn'k presupposes.\"},\n    {\"src\":\"BRT\",\"where\":\"col. 481-482 s.v. ¹gaona-\",\"stance\":\"supports\",\"note\":\"Bartholomae's cognate list (Afghan γūna, Ossetic γun, MP gōn, NP gūn) is the Iranian family the Sogdian form belongs to.\"}])\n\nN(id=10, lang=\"Pahlavi\", words=\"gôn; cigôn; hamôgĕn; ni-kŭn\", verdict=\"confirmed\",\n  derivation=\"All four Middle Persian forms are real, though Nourai's transliterations are the older (Mo'in/Horn) ones. MacKenzie: 'gōn [gwn' | N gūn] colour, complexion. ~ag [-k' | M gōng, N gūna] = gōn; sort, kind, form'; 'čiyōn [cygwn' | M cwn, N čūn] as, like, how, when'; 'nigūn [nkwn' | N ~] inverted, upside down. ~īh: depth, downward direction. ~sār: downwards'. Mo'in's footnote in BQT 1861 sets out the same set: «پهلوی gōn … و gōnak، اوستا gaona (مو، رنگِ مو) — بارتولمه… ارمنی goin (رنگ)… قس: کلمات پهلوی: čigōn، hamgōnak، ōgōn». čigōn is čē 'what' + gōn 'kind, manner' ('of what kind' > 'how'), hamgōnak is ham- 'same' + gōn-ak ('of the same kind' > 'all alike'); OIran. *gauna- > MP gōn is the regular monophthongisation au > ō. nigūn 'upside down' is ni- 'down' + a second element usually taken as gōn 'manner', though some analyse it rather with the participle of *gav-/gu- 'to bend'; either way it is the form the chart needs.\",\n  derivation_fa=\"هر چهار صورتِ فارسیِ میانه واقعی‌اند، هرچند آوانگاری نورایی کهنه (بر پایهٔ معین و هرن) است. مکنزی می‌آورد: «gōn [gwn'] رنگ، چهره؛ gōnag = gōn، گونه، نوع»؛ «čiyōn [cygwn'] چون، چگونه»؛ «nigūn [nkwn'] وارونه، سرنگون؛ nigūnsār فروسو». حاشیهٔ معین بر برهان قاطع ص ۱۸۶۱ همین مجموعه را دارد: «پهلوی gōn… و gōnak، اوستا gaona (مو، رنگ مو) ـ بارتولمه… ارمنی goin (رنگ)… قس: کلمات پهلوی: čigōn، hamgōnak، ōgōn». čigōn از čē «چه» + gōn «گونه» است و hamgōnak از ham- «هم» + gōn-ak. دوواکهٔ ایرانی باستانِ au در فارسی میانه به ō بدل شده است (*gauna- > gōn). ادعای نورایی درست است.\",\n  sources=[],\n  ref_check=[{\"ref\":\"BQT:671\",\"status\":\"partial\",\"note\":\"Borhan-e Qate' vol. 2: the چگونگی / چون footnotes are on the leaves around printed pp. 659-675 (BQT_v2_pages.txt leaves 113 and 129) and read «چگونگی ـ از: چگونه (چگونک) + ی (مصدری). پهلوی čigōnak…» and «چون ـ پهلوی čiyōn از چه + gōnak…». The content is exactly the claim of node 10, but I could not pin printed page 671 itself: the Persian page numbers in this volume's OCR are illegible, and the volume has no page map.\"}],\n  consulted=[\n    {\"src\":\"PHD\",\"where\":\"pp. 36-37, 58 (PHD.txt lines 382, 302, 512)\",\"stance\":\"supports\",\"note\":\"'gōn [gwn'] colour, complexion. ~ag = gōn; sort, kind, form.'; 'čiyōn [cygwn'] as, like, how, when.'; 'nigūn [nkwn'] inverted, upside down. ~sār downwards.'\"},\n    {\"src\":\"BQT\",\"where\":\"printed p. 1861 (pdf 658, vol.-3 scan), Mo'in's footnote on گون\",\"stance\":\"supports\",\"note\":\"«پهلوی gōn … gōnak، اوستا gaona (مو، رنگِ مو) ـ بارتولمه AiW…، ارمنی goin (رنگ)… قس: کلمات پهلوی: čigōn، hamgōnak، ōgōn…»\"},\n    {\"src\":\"NYB\",\"where\":\"NYB_vol2_glossary.txt, grep 'gōn', 'nigūn', 'gumbad'\",\"stance\":\"silent\",\"note\":\"the OCR of Nyberg's glossary returns no hits for any of these headwords (the Latin transliteration with macrons does not survive the scan), so it can neither confirm nor deny.\"}])\n\nN(id=11, lang=\"Persian\", words=\"gŭn «گون»; negŭn «نگون»; zargŭn «زرگون»\", verdict=\"plausible\",\n  derivation=\"The three head words are secure. گون gūn 'colour; kind, manner' continues MP gōn (Mo'in, Farhang-e Farsi: «گون: (قد.: gōn) [= گونه، گونا] (اِ.) رنگ، لون… نوع، قسم، طرز، روش»), the MP ō regularly raised to NP ū; چگونه and چون are its compounds with čē. نگون negūn 'upside down' = MP nigūn, whence سرنگون and نگون‌سار. زرگون zargūn 'gold-coloured' = زر zar 'gold' + گون, and this is the compound the American Heritage Dictionary itself analyses s.v. zircon: 'Persian zargūn, gold-colored, from Middle Persian zargōn, golden: zarr, zar-, golden from Old Iranian *zarna-; see ghel-² … + gōn, color, from Old Iranian *gaona-' — which also justifies Nourai's cross-reference '☞Ghel'. The one weak item is in the script_extra: همگی 'all' does not belong here; it is هَمه/هَمَگ (MP hamāg 'all') + -ī, not a derivative of gōn. (The Pahlavi hamgōnak of node 10 does mean 'all alike', but it did not give همگی.) Hence plausible rather than confirmed.\",\n  derivation_fa=\"سه واژهٔ اصلیِ این گره استوارند. «گون» (رنگ؛ گونه، شیوه) دنبالهٔ فارسی میانهٔ gōn است — معین: «گون: (قد.: gōn) [= گونه، گونا] رنگ، لون… نوع، قسم، طرز، روش» — و واکهٔ ō در فارسی نو به ū بدل شده است؛ «چگونه» و «چون» ترکیب‌های آن با «چه»اند. «نگون» همان nigūn پهلوی است که «سرنگون» و «نگون‌سار» از آن ساخته شده. «زرگون» = «زر» + «گون»، و همین ترکیب را فرهنگ American Heritage ذیل zircon تحلیل می‌کند: «فارسی zargūn «زرین‌رنگ» از فارسی میانهٔ zargōn: zar از ایرانی باستان *zarna- + gōn از ایرانی باستان *gaona-» — که ارجاع نورایی به ریشهٔ Ghel را نیز موجه می‌کند. تنها نقطهٔ سست، «همگی» در فهرست افزودهٔ نمودار است: «همگی» از «همه/هَمَگ» (فارسی میانه hamāg «همه») + ـی است و ربطی به «گون» ندارد. از این رو حکم: با احتیاط پذیرفتنی.\",\n  sources=[W+\"%DA%AF%D9%88%D9%86\", \"https://www.ahdictionary.com/word/search.html?q=zircon\"],\n  ref_check=[\n    {\"ref\":\"BQT:1861\",\"status\":\"supports\",\"note\":\"BQT printed p. 1861 (= pdf 658 of the vol.-3 scan). Entry «گون … بمعنی رنگ و لون باشد… و بمعنی طرز و روش و قاعده و قانون و صفت نیز آمده است»; Mo'in's footnote: «پهلوی gōn … و gōnak، اوستا gaona (مو، رنگِ مو) ـ بارتولمه AiW …، ارمنی goin (رنگ)… قس: کلمات پهلوی: čigōn، hamgōnak، ōgōn… افغانی γūna (مو، رنگ) ـ هوبشمان». Precisely the arrow node 10 → node 11.\"},\n    {\"ref\":\"MON:3473\",\"status\":\"partial\",\"note\":\"the entry is as claimed — MON_part2.txt line 36867: «گون: (قد.: gōn) [= گونه، گونا] (اِ.) رنگ، لون، رخسار، چهره، گونه. نوع، قسم. طرز، روش، شیوه…» — but the page number is unverifiable: only the 2-volume Adena reprint is on disk, with different pagination from the 6-volume Amir Kabir edition.\"}],\n  consulted=[\n    {\"src\":\"HRN\",\"where\":\"no. 946, p. 211 (HRN.txt line ~8203)\",\"stance\":\"supports\",\"note\":\"'946. gūn \\\\'Farbe; Art und Weise\\\\', gūne. ap. Ῥοδογούνη, Ἀλογούνη; aw. gaona- \\\\'Farbe\\\\'; phlv. gūnak, gūn, arm. LW. goin. afγ. LW. γūna.' — Horn even adduces the Old Persian personal names Rhodogune/Alogune as evidence for the Old Iranian element.\"},\n    {\"src\":\"AHD\",\"where\":\"ahdictionary.com s.v. zircon (etymology bracket)\",\"stance\":\"supports\",\"note\":\"'…from Persian zargūn, gold-colored, from Middle Persian zargōn, golden: zarr, zar-, golden from Old Iranian *zarna-; see ghel-² in the Appendix of Indo-European roots + gōn, color, from Old Iranian *gaona-; akin to Sanskrit guṇaḥ, string, thread, quality'.\"},\n    {\"src\":\"PHD\",\"where\":\"p. 96 s.v. zargōn (PHD.txt line 677)\",\"stance\":\"supports\",\"note\":\"'zargōn [zlgwn' | P zrgwng, N zargūn] golden, green, fresh. ~īh: greenness.' — the Middle Persian ancestor of زرگون is on record.\"}])\n\nN(id=12, lang=\"French\", words=\"jargon\", verdict=\"disputed\",\n  derivation=\"French jargon (also jargon, jargoon) as a gem name — 'a smoky or straw-yellow variety of zircon' — is real; the question is whether it comes from Persian زرگون. Two older authorities say yes: Devic, Dictionnaire étymologique des mots français d'origine orientale s.v. Jargon, ties jargon/zircon to Spanish azarcón, Portuguese zarcão and Arabic زرقون zarqūn, and concludes 'notre jargon me paraît venir de cette expression persane qui définit très-exactement la couleur de la gemme'; Webster's New Twentieth Century likewise: 'jargon, n. [Fr. jargon; It. giargone, a sort of yellow diamond; perhaps from Per. zargūn, gold-colored; zar, gold, and gūn, color.]'. Modern scholarship disagrees about the French word specifically. Etymonline: the mineral name 'has been traced to Medieval Latin jargonce, which is of uncertain origin. Compare Italian giargone, from the same source.' AHD is explicit that the two strands are separate: English zircon comes 'partly from Arabic zarqūn … (from Persian zargūn …), and partly from European terms for \\\"jacinth\\\" such as French jargon (from Old French jargonce, ultimately from Latin hyacinthus; see HYACINTH)'. On that account French jargon is a worn-down hyacinthus, not زرگون, and the Persian element reached Europe through Arabic and German instead. Hence: disputed.\",\n  derivation_fa=\"واژهٔ فرانسویِ jargon به‌عنوان نامِ سنگ («گونه‌ای زیرکونِ زرد کاهی») واقعی است؛ پرسش این است که آیا از «زرگون» فارسی آمده. دو مرجع کهن آری می‌گویند: دُویک (فرهنگ ریشه‌شناسیِ واژه‌های فرانسویِ خاورزمینی، ذیل Jargon) آن را به اسپانیایی azarcón و عربی «زرقون» می‌پیوندد و می‌نویسد «به گمان من jargon ما از همین ترکیبِ فارسی می‌آید»؛ وبستر نیز: «jargon [فرانسوی؛ ایتالیایی giargone…؛ شاید از فارسی zargūn «زرین‌رنگ»: zar «زر» + gūn «رنگ»]». اما پژوهش امروزی دربارهٔ خودِ واژهٔ فرانسوی این را نمی‌پذیرد: اتیمانلاین آن را به لاتینِ میانهٔ jargonce با ریشهٔ نامعلوم بازمی‌گرداند، و فرهنگ American Heritage دو رشته را جدا می‌کند: zircon انگلیسی «تا اندازه‌ای از عربی zarqūn (< فارسی zargūn) و تا اندازه‌ای از واژه‌های اروپاییِ یاقوت‌کبود مانند jargon فرانسوی (از فرانسویِ کهن jargonce، سرانجام از لاتینِ hyacinthus)». بر این پایه jargon فرانسوی صورتِ فرسودهٔ hyacinthus است نه «زرگون»، و عنصر فارسی از راه عربی و آلمانی به اروپا رسیده است. پس پژوهش امروزی این پیکان را رد می‌کند.\",\n  sources=[\"https://www.etymonline.com/word/zircon\", \"https://www.ahdictionary.com/word/search.html?q=zircon\"],\n  ref_check=[{\"ref\":\"None\",\"status\":\"not_checked\",\"note\":\"the chart gives this node no reference of its own; the claim is covered by the AHD:1489 citation on the daughter node 13, which in fact separates jargon from zargūn.\"}],\n  consulted=[\n    {\"src\":\"DEV\",\"where\":\"s.v. Jargon (DEV.txt line 1555)\",\"stance\":\"supports\",\"note\":\"'Jargon. Gemme de couleur jaune tirant sur le rouge… Ital. giargone. Jargon et zircon… sont certainement identiques à l'espagnol azarcon… Et tous ces mots correspondent à un terme arabe, زرقون zarqoûn… Dans tous les cas, notre jargon me paraît venir de cette expression persane qui définit très-exactement la couleur de la gemme.'\"},\n    {\"src\":\"WEB\",\"where\":\"vol. 1 s.v. jargon (WEB_vol1.txt line 101827)\",\"stance\":\"supports\",\"note\":\"'jar′gon, n. [Fr. jargon; It. giargone, a sort of yellow diamond; perhaps from Per. zargūn, gold-colored; zar, gold, and gūn, color.] a colorless or smoky variety of zircon…' — note Webster's own 'perhaps'.\"},\n    {\"src\":\"AHD\",\"where\":\"ahdictionary.com s.v. zircon\",\"stance\":\"contradicts\",\"note\":\"'…and partly from European terms for \\\"jacinth\\\" such as French jargon (from Old French jargonce, ultimately from Latin hyacinthus; see HYACINTH).'\"},\n    {\"src\":\"FSD\",\"where\":\"vol. 4 s.v. zircon (FSD_vol4.txt line 61425)\",\"stance\":\"partial\",\"note\":\"'The gem varieties of zircon are called jargon and hyacinth… [F. = jargon; see jargon]' — Funk & Wagnalls confirms the sense but sends the reader to the French word without an oriental etymology.\"}])\n\nN(id=13, lang=\"English\", words=\"zircon, zirconium\", verdict=\"plausible\",\n  derivation=\"The Persian ancestry of zircon is real, but not by the route the chart draws. AHD s.v. zircon: '[German Zirkon (originally in obsolete scientific German Zirkonerde, zirconium oxide, coined by German chemist Martin Heinrich Klaproth (1743-1817), who first isolated it from a jacinth), probably partly from Arabic zarqūn, minium, bright red (from Persian zargūn, gold-colored, from Middle Persian zargōn, golden: zarr, zar-, golden from Old Iranian *zarna-; see ghel-² … + gōn, color, from Old Iranian *gaona-…), and partly from European terms for \\\"jacinth\\\" such as French jargon…]'. So: (i) English got the word from German Zirkon (Klaproth, 1789; English 1794, first as circon/jargon); (ii) the زرگون element came in through Arabic زرقون zarqūn, not through French; (iii) French jargon contributed only the shape. zirconium is Klaproth's Modern Latin coinage of 1789 (English 1808) on zircon + -ium, so that word is uncontroversial. Nourai's arrow French jargon → English zircon is therefore half right: right about the Persian ultimate source, wrong about the intermediary.\",\n  derivation_fa=\"ریشهٔ فارسیِ zircon واقعی است، اما نه از راهی که نمودار می‌کشد. فرهنگ American Heritage ذیل zircon می‌نویسد: «از آلمانی Zirkon (نخست در Zirkonerde، ساختهٔ کلاپروتِ شیمی‌دان در ۱۷۸۹م)، احتمالاً تا اندازه‌ای از عربی «زرقون» (سرخِ روشن، سرنج) که خود از فارسی zargūn «زرین‌رنگ» و آن از فارسی میانهٔ zargōn است: zar از ایرانی باستان *zarna- + gōn از *gaona-؛ و تا اندازه‌ای از واژه‌های اروپاییِ یاقوت مانند jargon فرانسوی». پس: انگلیسی واژه را از آلمانی گرفته (۱۷۹۴م، نخست به صورت circon)؛ عنصر «زرگون» از راه عربی «زرقون» رسیده نه از فرانسوی؛ و jargon فرانسوی تنها بر شکلِ واژه اثر گذاشته است. zirconium نیز ساختهٔ کلاپروت از zircon + -ium است (۱۸۰۸م). بنابراین پیکانِ «jargon فرانسوی ← zircon انگلیسی» نیمه‌درست است: در سرچشمهٔ فارسی درست، در واسطه نادرست.\",\n  sources=[\"https://www.ahdictionary.com/word/search.html?q=zircon\", \"https://www.etymonline.com/word/zircon\"],\n  ref_check=[{\"ref\":\"AHD:1489\",\"status\":\"supports\",\"note\":\"Nourai's AHD:1489 is the main-dictionary page of the New College Edition (the Z range, before the IE appendix at pp. 1505-1550), i.e. the entry 'zircon'. The 1975 print could not be opened, but the online AHD (same editorial line) carries the etymology in full: '[German Zirkon…, probably partly from Arabic zarqūn, minium, bright red (from Persian zargūn, gold-colored, from Middle Persian zargōn, golden: zarr, zar-, golden from Old Iranian *zarna-; see ghel-² in the Appendix of Indo-European roots + gōn, color, from Old Iranian *gaona-; akin to Sanskrit guṇaḥ, string, thread, quality), and partly from European terms for \\\"jacinth\\\" such as French jargon…]'. It supports the Persian zargūn = zar + gōn analysis (and Nourai's ☞Ghel cross-reference) but routes it through Arabic and German rather than through French jargon.\"}],\n  consulted=[\n    {\"src\":\"AHD\",\"where\":\"online entry 'zircon'\",\"stance\":\"partial\",\"note\":\"see ref_check: Persian source confirmed, French intermediary denied.\"},\n    {\"src\":\"FSD\",\"where\":\"vol. 4 s.v. zircon (FSD_vol4.txt line 61425)\",\"stance\":\"partial\",\"note\":\"'zircon… An adamantine, variously colored, transparent to opaque zirconium silicate (ZrSiO4)… The gem varieties of zircon are called jargon and hyacinth. [F. = jargon; see jargon]'\"},\n    {\"src\":\"WEB\",\"where\":\"vol. 1 s.v. jargon / hyacinth (WEB_vol1.txt lines 101827, 101567)\",\"stance\":\"supports\",\"note\":\"Webster's keeps the Persian zargūn etymology for the jargon/zircon family: 'perhaps from Per. zargūn, gold-colored; zar, gold, and gūn, color.'\"}])\n\nN(id=14, lang=\"Persian\", words=\"(no transliteration; script only: زیرکونیم)\", verdict=\"transcription_suspect\",\n  derivation=\"The box has no Latin transliteration and no gloss; it holds a Persian re-borrowing of the chemical name zirconium, closing the circle زرگون → (Arabic/French/German) → back into Persian. The substance of the node is right — modern Persian did take the element name back from European languages — but the printed form is wrong. On the printed page (pdf p. 176 = book p. 146) the box reads «زیرکونیم» (z-y-r-k-w-n-y-m). The normal Persian word is زیرکونیوم zirkoniyum, with the واو of the -ium ending; زیرکونیم is not a form the Persian dictionaries know. The extraction is otherwise faithful; the JSON's «زیر کونیم» with a space merely reflects the fact that ر does not join to the following letter, so the OCR read the normal non-joining gap as a word break. Error is in the book (a dropped و), with a minor extraction artefact on top (the inserted space).\",\n  derivation_fa=\"این جعبه نه آوانگاری دارد و نه معنی؛ محتوای آن وام‌گیریِ دوبارهٔ نامِ عنصرِ زیرکونیوم به فارسی است و حلقهٔ «زرگون ← عربی/فرانسوی/آلمانی ← فارسی» را می‌بندد. جانِ مطلب درست است، اما صورتِ چاپی نادرست: در صفحهٔ چاپی (ص ۱۴۶ کتاب) نوشته شده «زیرکونیم»، حال آنکه صورت رایج و درست «زیرکونیوم» است و واوِ پایانهٔ -ium افتاده. این خطای کتاب است نه خطای استخراج؛ تنها فاصله‌ای که در JSON میان «زیر» و «کونیم» آمده، ساختگیِ خوانشِ ماشینی است، زیرا «ر» به حرف پس از خود نمی‌چسبد و شکافِ طبیعیِ خط، مرزِ واژه پنداشته شده است. حکم: خطای چاپی کتاب، به‌علاوهٔ یک ناهماهنگی کوچک در داده که باید اصلاح شود.\",\n  error_in=\"book\",\n  book_prints=\"زیرکونیم\",\n  correct_form=\"زیرکونیوم\",\n  sources=[\"https://www.etymonline.com/word/zircon\"],\n  ref_check=[{\"ref\":\"None\",\"status\":\"not_checked\",\"note\":\"the chart cites no reference for this node.\"}],\n  consulted=[\n    {\"src\":\"MON\",\"where\":\"MON_part2.txt, grep زیرکونیوم / زیرکونیم\",\"stance\":\"silent\",\"note\":\"neither spelling appears in the Mo'in text on disk; the element name is later than the dictionary's core vocabulary.\"},\n    {\"src\":\"BOOK\",\"where\":\"printed page image data/verification/sources/refs/ocr/BOOK/176.png, node at the right edge below 'English AHD:1489 zircon, zirconium'\",\"stance\":\"contradicts\",\"note\":\"the page unambiguously prints «زیرکونیم» — read at 600 dpi — so the JSON is faithful to the book and the book is wrong.\"}])\n\nN(id=15, lang=\"Avestan\", words=\"gunda\", verdict=\"plausible\",\n  derivation=\"The Avestan word is attested exactly as glossed. Bartholomae, AiWb col. ~515: 'j. gunda- m., gundā- f. \\\"zum Backen angerührtes Mehl, Mehlteig, Teigballen\\\": yat gundəs daiδyāt \\\"wenn der Teig (zum Backen) zurecht gelegt wird\\\" V. 3.32', with the descendants 'mp. gundak (Pü.), np. gunda'. What is uncertain is the arrow from the root: Pokorny puts it there only with a question mark. IEW 394, in the dental-extension section geud-/gud- of geu- 'biegen', ends: 'nasaliert anord. kunta \\\"vulva\\\" aus mnd. kunte…, norw. schwed. kunt \\\"Ranzen (von Birkenrinde)\\\"; auch av. gunda-, gund \\\"Teigballen\\\"?'. Horn no. 936 is equally cautious ('Unsicher'). Semantically the link is 'lump, rounded mass' < 'the bent, curved thing'; formally gunda- would be *gu-n-d-o- with the nasal infix Pokorny posits for the Germanic forms.\",\n  derivation_fa=\"واژهٔ اوستایی درست همان است که در نمودار آمده: بارتولمه (ستون ≈۵۱۵) می‌آورد «gunda- (مذکر)، gundā- (مؤنث): آردِ خمیرشده برای پختن، خمیر، گلولهٔ خمیر»، با شاهدِ وندیداد ۳:۳۲، و بازماندگانِ «فارسی میانه gundak، فارسی نو گنده». آنچه نااستوار است پیکانِ ریشه است: پوکورنی آن را تنها با علامت پرسش زیر ریشهٔ geu- «خم شدن» (بخشِ گسترشِ دندانیِ geud-) در ص ۳۹۴ آورده: «auch av. gunda-, gund „Teigballen“?». هرن نیز (شمارهٔ ۹۳۶) می‌نویسد «Unsicher» (نامطمئن). از نظر معنایی پیوند از راهِ «تودهٔ گِرد» < «چیزِ خمیده» است و از نظر صرفی gunda- را باید *gu-n-d-o- با میان‌وندِ خیشومی دانست. پس: با احتیاط پذیرفتنی.\",\n  sources=[],\n  ref_check=[{\"ref\":\"POK:394\",\"status\":\"supports\",\"note\":\"POK_02.txt leaf 49, in the part of the leaf that follows the printed page marker '394': 'nasaliert anord. kunta ,vulva' aus mnd. kunte ,cunnus; auch Hintere', norw. schwed. kunt ,Ranzen (von Birkenrinde)'; auch av. gunda-, gund ,Teigballen'?' — Pokorny does place the Avestan word under geu- on exactly the page cited, but with a question mark.\"}],\n  consulted=[\n    {\"src\":\"BRT\",\"where\":\"col. ~515 s.v. gunda- (BRT.txt line 10408)\",\"stance\":\"supports\",\"note\":\"'j. gunda- m., gundā- f. \\\\'zum Backen angerührtes Mehl, Mehlteig, Teigballen\\\\': yat gundəs daiδyāt … V. 3.32 … mp. gundak (Pü.), np. gunda.' The word, the gloss and the whole Iranian chain of nodes 15 → 16.\"},\n    {\"src\":\"WLD\",\"where\":\"Bd. I 555 ff., '1. geu- „biegen, krümmen, wölben“'\",\"stance\":\"partial\",\"note\":\"the parent article of Pokorny 393-398; the Avestan dough-word appears there with the same hesitation Pokorny reproduces.\"},\n    {\"src\":\"AHD\",\"where\":\"Watkins 1985, g-list (AHD_watkins1985.txt lines 499, 557)\",\"stance\":\"silent\",\"note\":\"Watkins's appendix has no *geu- 'to bend' at all (it runs geuə- 'to hasten' → gyeu- 'to chew'), simply because no English word reaches that root through Latin or Greek; its silence is not disagreement.\"}])\n\nN(id=16, lang=\"Persian\", words=\"gondeh «گنده»\", verdict=\"plausible\",\n  derivation=\"Borhan-e Qate' p. 1843 has both senses Nourai gives: «گنده … معروف است که در مقابل باریک باشد… و کوفتهٔ بزرگی را نیز گویند که از گوشت سازند… و گلوله‌ای که از خمیر بجهت پختن نان کنند» ('a ball made of dough for baking bread'), and Mo'in's footnote 4 derives it: «پهلوی gundak، ارمنی gund (کلوله، کره)… رک: هوبشمان… در اراک (سلطان آباد) gonda». Horn no. 936 (p. 209) says the same: 'gunde \\\"Hefenballen (für ein Brot)\\\". aw. gunda- (Vd. 3, 32) \\\"Teig\\\" (Geldner, KZ. 24, 549 Note 4); phlv. gundak. Unsicher.' The chain OIran. *gunda- > MP gundak > NP gunda/gonda is regular (loss of the -k after the vowel > -a). Two cautions: (i) Horn himself marks the whole thing 'unsicher', and Pokorny's attachment of gunda- to *geu- carries a question mark (node 15); (ii) the everyday modern گنده 'big, fat, stinking' is a different word — Wiktionary derives that one from MP gandag 'foul, stinking' (Proto-Indo-Iranian *g(ʰ)andʰ- 'to smell'), and its Wiktionary 'Etymology 2' (the adjective gonde 'big') is explicitly left blank. So Nourai's gloss 'a lump of dough, large' conflates two homophones, of which only the first belongs here.\",\n  derivation_fa=\"برهان قاطع در ص ۱۸۴۳ هر دو معنایی را که نورایی آورده دارد: «گنده… معروف است که در مقابل باریک باشد… و کوفتهٔ بزرگی را نیز گویند که از گوشت سازند… و گلوله‌ای که از خمیر بجهت پختن نان کنند»، و معین در حاشیه (پانوشت ۴) آن را چنین ریشه‌یابی می‌کند: «پهلوی gundak، ارمنی gund (کلوله، کره)… رک: هوبشمان… در اراک gonda». هرن (شمارهٔ ۹۳۶، ص ۲۰۹) نیز همین را می‌گوید و در پایان می‌افزاید «نامطمئن». زنجیرهٔ ایرانی باستانِ *gunda- > فارسی میانه gundak > فارسی نو «گنده» قاعده‌مند است (افتادنِ کافِ پایانی و بدل شدن آن به «ـه»). دو نکتهٔ احتیاط: نخست آنکه پوکورنی خودِ gunda- را با علامت پرسش به ریشه بسته است؛ دوم آنکه «گندهٔ» رایجِ امروزی به معنای «بزرگ، بدبو» واژهٔ دیگری است و از فارسی میانهٔ gandag «بدبو» می‌آید. پس معنیِ دوگانهٔ نمودار دو هم‌آوا را در هم آمیخته است.\",\n  sources=[W+\"%DA%AF%D9%86%D8%AF%D9%87\"],\n  ref_check=[\n    {\"ref\":\"HRN:209\",\"status\":\"supports\",\"note\":\"Horn, Grundriss der neupersischen Etymologie, no. 936 on printed p. 209 (HRN.txt lines 8129-8132, leaf 230 = printed 209): '936. gunde \\\\'Hefenballen (für ein Brot)\\\\'. aw. gunda- (vd. 3, 32) \\\\'Teig\\\\' (Geldner, KZ. 24, 549 Note 4); phlv. gundak. Unsicher.' Exactly the arrow of node 15 → 16, page number exact — but with Horn's own 'Unsicher'.\"},\n    {\"ref\":\"BQT:1843\",\"status\":\"supports\",\"note\":\"BQT printed p. 1843 (= pdf 640 of the vol.-3 scan). Entry «گنده … و گلوله‌ای که از خمیر بجهت پختن نان کنند» and Mo'in's footnote «پهلوی gundak، ارمنی gund (کلوله، کره)… هوبشمان… در اراک (سلطان‌آباد) gonda».\"}],\n  consulted=[\n    {\"src\":\"BRT\",\"where\":\"col. ~515 s.v. gunda-\",\"stance\":\"supports\",\"note\":\"'…mp. gundak (Pü.), np. gunda' — Bartholomae himself draws the line from the Avestan word to New Persian.\"},\n    {\"src\":\"BQT\",\"where\":\"printed p. 1843, Mo'in's footnote 4\",\"stance\":\"supports\",\"note\":\"see ref_check.\"},\n    {\"src\":\"HUB\",\"where\":\"HUB.txt, grep 'gund'\",\"stance\":\"silent\",\"note\":\"Hübschmann's Persische Studien has no separate entry for گنده; he is cited only second-hand, through Mo'in's footnote, for the Armenian gund.\"}])\n\nN(id=17, lang=\"Pahlavi\", words=\"gumbat\", verdict=\"disputed\",\n  derivation=\"The Middle Persian word is beyond doubt — MacKenzie: 'gumbad [gwmbt' | N ~] dome, fire-temple' — but its ancestry is not. Nourai follows Pokorny, who, in the nasalised *kumb- section of keu-2 on IEW 396, writes only: 'Nasaliertes germ. *kumb-: ags. cumb ,Napf' …, mnd. kumm(e) …; Dazu vielleicht npers. gumbed ,Wölbung, Kuppel, Becher''. That 'vielleicht' is the whole of the Indo-European case. Against it stands a long Semitic-loan tradition: Hübschmann, Persische Studien p. 255, listing Armenian words with n for original m, writes 'gmbeṭ \\\"Kuppel\\\" = np. gunbad (syr. LW., Nöldeke, Pers. Stud. II, 41)' — i.e. Nöldeke and Hübschmann take New Persian gunbad itself to be a Syriac loan; Wiktionary follows, deriving MP gumbad from Classical Syriac ܩܘܒܬܐ qubbəṯā and calling گنبد a doublet of Arabic-mediated قبه. The traffic may also have run the other way: Lokotsch, s.v. Arabic qubba, notes '[Möglicherweise geht das ar. Grundwort selbst auf pers. gunbād zurück, ZDMG L, 646.]'. Since the prevailing modern account (Nöldeke/Hübschmann/Wiktionary) makes gumbad a Semitic loan rather than an inherited *kumb- derivative, the arrow is disputed.\",\n  derivation_fa=\"خودِ واژهٔ فارسی میانه بی‌گمان است — مکنزی: «gumbad [gwmbt'] گنبد، آتشکده» — اما تبارِ آن نه. نورایی از پوکورنی پیروی کرده که در ص ۳۹۶، در بخشِ خیشومی‌شدهٔ *kumb- از ریشهٔ keu-، تنها می‌نویسد: «شاید فارسی نو gumbed «گنبد، طاق، جام» نیز به این‌جا مربوط باشد» — و همین «شاید» تمامِ دلیلِ هندواروپایی است. در برابر آن، سنّتی دیرپا این واژه را وام‌واژهٔ سامی می‌داند: هوبشمان در «پژوهش‌های فارسی» ص ۲۵۵ می‌نویسد «ارمنی gmbeṭ «گنبد» = فارسی نو gunbad (وام‌واژهٔ سریانی، نُلدکه، Pers. Stud. II, 41)»؛ ویکی‌واژه نیز gumbad فارسی میانه را از سریانیِ کلاسیک ܩܘܒܬܐ (qubbəṯā) می‌گیرد و «گنبد» را دوگانهٔ «قبّه» (از همان سریانی ولی از راه عربی) می‌خواند. البته جهتِ وام‌گیری هم محلِ گفت‌وگوست: لوکوچ ذیل «قبّه»ی عربی می‌افزاید «شاید خودِ اصلِ عربی به فارسی gunbād بازگردد (ZDMG L, 646)». چون دیدگاهِ غالبِ امروزی آن را وام‌واژهٔ سامی می‌داند، پیکانِ نمودار مورد اختلاف است.\",\n  sources=[W+\"%DA%AF%D9%86%D8%A8%D8%AF\"],\n  ref_check=[{\"ref\":\"POK:396\",\"status\":\"partial\",\"note\":\"POK_02.txt leaf 52, after the printed page marker '396': 'Nasaliertes germ. *kumb-: ags. cumb (engl. coomb) ,Napf'… ^kump- … nhd. Kumpf / Dazu vielleicht npers. gumbed ,Wölbung, Kuppel, Becher'; ferner vermutlich lit. gumbas m. ,Wölbung, Geschwulst, Knorren'…'. The page number is exact, but Pokorny commits himself only to 'vielleicht', and he cites the New Persian word, not a Pahlavi gumbat.\"}],\n  consulted=[\n    {\"src\":\"PHD\",\"where\":\"p. 37 s.v. gumbad (PHD.txt line 384)\",\"stance\":\"supports\",\"note\":\"'gumbad [gwmbt' | N ~] dome, fire-temple.' — the Middle Persian form is exactly as drawn, whatever its origin.\"},\n    {\"src\":\"HUB\",\"where\":\"Persische Studien p. 255 (HUB.txt line 9123, leaf 265)\",\"stance\":\"contradicts\",\"note\":\"'…gmbeṭ \\\\'Kuppel\\\\' = np. gunbad (syr. LW., Nöldeke, Pers. Stud. II, 41)…' — Hübschmann classes New Persian gunbad itself as a Syriac loanword.\"},\n    {\"src\":\"LKT\",\"where\":\"s.v. Arab. qubba (LKT.txt line 2867)\",\"stance\":\"partial\",\"note\":\"'[Möglicherweise geht das ar. Grundwort selbst auf pers. gunbād zurück, ZDMG L, 646.]' — the opposite direction of borrowing, which at least shows the question was open.\"},\n    {\"src\":\"WLD\",\"where\":\"Bd. I / Pokorny's keu-2 article\",\"stance\":\"partial\",\"note\":\"the same hesitant 'vielleicht' as Pokorny; no independent evidence.\"}])\n\nN(id=18, lang=\"Persian\", words=\"gonbad «گنبد»\", verdict=\"confirmed\",\n  derivation=\"Whatever the ultimate source (see node 17), the Middle Persian → New Persian step is secure. Borhan-e Qate' p. 1836 defines «گنبد … نوعی از عمارت باشد مدور که از خشت گل و گچ و آجر پوشند … و بعربی قبه گویند», and Mo'in's footnote reads «پهلوی gumbat (گنبد، قبه) … در تهران و اراک (سلطان‌آباد) gombad … معرب «جنبذ» «معجم البلدان در: جنبذ»». MacKenzie gives MP gumbad, and Wiktionary states 'Inherited from Middle Persian gwmbt' /gumbad/, \\\"dome, fire-temple\\\"'. Phonetically MP gumbad > NP gonbad involves only the ordinary lowering/fronting of the vowel before the labial cluster (Tehran gombad), and the m assimilates to n in the spelling. The word passed on into Arabic as جنبذ and into Old Armenian գմբեթ gmbetʻ and Georgian გუმბათი gumbati.\",\n  derivation_fa=\"هر چه سرچشمهٔ نهاییِ واژه باشد (بنگرید به گرهٔ ۱۷)، گامِ «فارسی میانه ← فارسی نو» استوار است. برهان قاطع ص ۱۸۳۶: «گنبد… نوعی از عمارت باشد مدور که از خشت گل و گچ و آجر پوشند… و بعربی قبه گویند»، و در حاشیهٔ معین: «پهلوی gumbat (گنبد، قبه)… در تهران و اراک gombad… معرّبِ آن «جنبذ»، معجم‌البلدان». مکنزی نیز gumbad فارسی میانه را ثبت کرده و ویکی‌واژه می‌نویسد «به ارث رسیده از فارسی میانهٔ gumbad». از نظر آوایی تحول gumbad > گنبد جز افتادگیِ اندکِ واکه پیش از خوشهٔ لبی چیزی ندارد (تلفظ تهرانی gombad) و «م» در نوشتار به «ن» بدل شده است. واژه از فارسی به عربی («جنبذ») و به ارمنی کهن (գմբեթ) و گرجی (გუმბათი) رفته است.\",\n  sources=[W+\"%DA%AF%D9%86%D8%A8%D8%AF\"],\n  ref_check=[\n    {\"ref\":\"BQT:1836\",\"status\":\"supports\",\"note\":\"BQT printed p. 1836 (= pdf 633 of the vol.-3 scan). Entry «گنبد ـ بضم اول و فتح بای ابجد و سکون نون و دال بی‌نقطه، نوعی از عمارت باشد مدور که از خشت گل و گچ و آجر پوشند… و بعربی قبه گویند»; Mo'in's footnote 1: «پهلوی gumbat (گنبد، قبه)… در تهران و اراک (سلطان آباد) gombad، معرب «جنبذ»، «معجم‌البلدان در: جنبذ»».\"},\n    {\"ref\":\"MON:3396\",\"status\":\"partial\",\"note\":\"the Mo'in entry for گنبد could not be located in the 2-volume Adena reprint on disk (the only MON scan available), whose pagination differs from the 6-volume Amir Kabir edition Nourai cites; the position of 3396 in his sequence (کیوسک 3160 < گنبد 3396 < گون 3473) is at least alphabetically consistent.\"}],\n  consulted=[\n    {\"src\":\"PHD\",\"where\":\"p. 37 s.v. gumbad\",\"stance\":\"supports\",\"note\":\"'gumbad [gwmbt' | N ~] dome, fire-temple.'\"},\n    {\"src\":\"BQT\",\"where\":\"printed p. 1836, Mo'in's footnote 1\",\"stance\":\"supports\",\"note\":\"see ref_check.\"}])\n\nN(id=19, lang=\"Persian\", words=\"ğŭz «غوز»; ğŭzak «غوزک»\", verdict=\"confirmed\",\n  derivation=\"Both words are real and both are in Pokorny at exactly the pages cited. غوز/قوز/کوز/کوژ qūz/kūz/kūž 'hunch, hump on the back' is Pokorny's 'npers. kōz \\\"gekrümmt, buckelig\\\"', IEW 589, in the guttural extension keu-k- of keu-2 'biegen' beside Skt. kucáti, kuñcate 'zieht sich zusammen, krümmt sich', kóca- 'das Einschrumpfen'. غوزک/قوزک/گوزک 'ankle(-bone)' is Pokorny's 'npers. gūzak \\\"Fußknöchel\\\" (?)', IEW 395, under the -g- extension of geu-, beside Lith. gūžas 'Knorren, Beule, Kropf' and Pol. guz 'Beule, Höcker'. Ernout-Meillet, s.v. gibber/gibbus p. 488, quote the Persian word in the same company: 'Les mots qui désignent cette infirmité ont ailleurs des formes voisines: skr. kubjáḥ \\\"bossu\\\", pers. kūž, et a.h.a. hoggêr.' Wiktionary derives قوزک simply from قوز + the diminutive ـک. The variation of the initial consonant (غ ~ ق ~ ک ~ گ) is orthographic and dialectal, not etymological: an original *k- with a back rounded vowel is written with any of the four in Persian manuscripts. The one caution is Pokorny's own '(?)' on gūzak, and the fact that he distributes the two Persian words over two different roots (geu- and keu-), which Nourai's merged root box conveniently accommodates.\",\n  derivation_fa=\"هر دو واژه واقعی‌اند و هر دو دقیقاً در همان صفحه‌هایی از پوکورنی هستند که نورایی یاد کرده. «غوز/قوز/کوز/کوژ» را پوکورنی در ص ۵۸۹، در گسترشِ کامیِ keu-k- از ریشهٔ keu- «خم شدن»، چنین آورده: «npers. kōz \\\"خمیده، گوژپشت\\\"»، در کنارِ سنسکریت kucáti «در هم می‌کشد، خم می‌شود» و kóca- «چروکیدگی». «غوزک/قوزک/گوزک» را نیز در ص ۳۹۵، زیر گسترشِ -g- از ریشهٔ geu-، آورده: «npers. gūzak \\\"قوزکِ پا\\\" (؟)»، همراه با لیتوانیایی gūžas «گره، ورم» و لهستانی guz «برآمدگی». ارنو و مِیه در فرهنگ ریشه‌شناسیِ لاتین، ذیل gibbus «کوهان» در ص ۴۸۸، همین واژه را در کنار هم‌خانواده‌هایش می‌آورند: «واژه‌هایی که این نقص را می‌نامند در جاهای دیگر صورت‌های نزدیک دارند: سنسکریت kubjáḥ، فارسی kūž، و آلمانیِ علیای کهن hoggêr». گوناگونیِ حرفِ آغازین (غ ~ ق ~ ک ~ گ) املایی و گویشی است نه ریشه‌شناختی. تنها احتیاط، علامت پرسشِ خودِ پوکورنی بر gūzak است. ادعای نورایی درست است.\",\n  sources=[W+\"%D9%82%D9%88%D8%B2%DA%A9\"],\n  ref_check=[\n    {\"ref\":\"POK:395\",\"status\":\"supports\",\"note\":\"POK_02.txt leaf 50, immediately after the printed page marker '395': 'mit -g-: npers. gūzak ,Fußknöchel' (?); lit. gūžas ,Knorren, Beule, Kropf', gūžys ,Kropf'…; poln. guz ,Beule, Höcker'…' — Nourai's غوزک 'ankle' verbatim, on the exact page.\"},\n    {\"ref\":\"POK:589\",\"status\":\"supports\",\"note\":\"POK_02.txt leaf 248, the part following the '589' marker of leaf 247: 'B. II. keu-k-: Ai. kucáti, kuñcate ,zieht sich zusammen, krümmt sich', kuñcikā ,Schlüssel', kuca- m. ,weibliche Brust', kōcayati ,zieht zusammen', kōca- m. ,das Einschrumpfen', npers. kōz ,gekrümmt, buckelig'.' — Nourai's غوز/کوز 'hump' verbatim, on the exact page.\"},\n    {\"ref\":\"LAT:488\",\"status\":\"supports\",\"note\":\"Ernout–Meillet, Dictionnaire étymologique de la langue latine, printed p. 488 (LAT.txt leaf 506, whose header reads 'gerra 488'), s.v. gibber/gibbus 'bossu … bosse, gibbosité': '…La forme *gubbus attestée par des langues romanes et le vénitien gufo indiquent une interférence avec gr. κυφός \\\\'courbé en avant\\\\', κῦφος \\\\'bosse\\\\'. — Les mots qui désignent cette infirmité ont ailleurs des formes voisines: skr. kubjáḥ \\\\'bossu\\\\', pers. kūž, et a.h.a. hoggêr.' The Persian word is cited by name on the page Nourai gives.\"}],\n  consulted=[\n    {\"src\":\"LAT\",\"where\":\"p. 488 s.v. gibber, gibbus\",\"stance\":\"supports\",\"note\":\"see ref_check.\"},\n    {\"src\":\"POK\",\"where\":\"IEW 395 and 589\",\"stance\":\"supports\",\"note\":\"see ref_check; note Pokorny splits the two Persian words between geu- and keu-, which is why Nourai's root box merges the two.\"},\n    {\"src\":\"HRN\",\"where\":\"HRN.txt, grep 'kūz', 'gūzak'\",\"stance\":\"silent\",\"note\":\"Horn's Grundriss has no numbered entry for قوز/قوزک; the OCR returns no hit for either spelling.\"}])\n\nN(id=20, lang=\"Old Persian\", words=\"kaufa\", verdict=\"confirmed\",\n  derivation=\"Old Persian kaufa- 'mountain' is attested in the Bisotun inscription (DB 1.37, 3.44) and at Susa (DSf 31). Kent's lexicon, p. 178: 'kaufa- sb. \\\"mountain\\\": Av. kaofa-, Phl. kof, NPers. kōh (§75.II, §106). See also Akaufaciya-. kaufa nsm. DB 1.37; 3.44; DSf 31.' The Indo-European attachment is Pokorny's: IEW 592, in section b of keu-p- ('Bedeutungsgruppe \\\"Wölbung nach oben, Haufe u. dgl.\\\"'), 'Apers. kaufa- ,Berg', av. kaofa- ,ds.; Kamelbuckel', npers. kōh ,Berg' (setzen -ph- voraus)' — the Avestan sense 'camel's hump' is what makes 'mountain' = 'the humped thing' credible. One reservation from Nourai's own source: Kent remarks elsewhere (p. 171 area) that 'OP kaufa- \\\"mountain\\\", Av. kaofa-, seems to have no cognates outside Iranian', which is a comment on the -f- (< *-ph-) rather than a rejection of the root.\",\n  derivation_fa=\"واژهٔ پارسی باستانِ kaufa- «کوه» در کتیبهٔ بیستون (DB ۱:۳۷ و ۳:۴۴) و در شوش (DSf ۳۱) گواهی شده است. کنت در واژه‌نامهٔ خود، ص ۱۷۸: «kaufa- (اسم) «کوه»: اوستایی kaofa-، پهلوی kof، فارسی نو kōh». پیوند هندواروپایی از پوکورنی است: در ص ۵۹۲، در بخشِ «برآمدگی رو به بالا، توده» از گسترشِ keu-p-: «پارسی باستان kaufa- «کوه»، اوستایی kaofa- «همان؛ کوهانِ شتر»، فارسی نو kōh «کوه» (که *-ph- را پیش‌فرض می‌گیرند)». همان معنای اوستاییِ «کوهانِ شتر» است که «کوه = چیزِ برآمده» را باورپذیر می‌کند. یک احتیاط از خودِ مأخذ نورایی: کنت در جایی دیگر می‌نویسد که kaufa- «بیرون از ایرانی هم‌ریشه‌ای ندارد» که سخنی است دربارهٔ فای این واژه، نه ردِ ریشه. ادعای نورایی درست است.\",\n  sources=[],\n  ref_check=[{\"ref\":\"KNT:178\",\"status\":\"supports\",\"note\":\"Kent, Old Persian, Lexicon, printed p. 178 (KNT.txt leaf 200, which carries the printed page number '178'): 'kaufa- sb. \\\\'mountain\\\\': Av. kaofa-, Phl. kof, NPers. kōh (§75.II, §106). See also Akaufaciya-. kaufa nsm. DB 1.37; 3.44; DSf 31.' Page number exact.\"}],\n  consulted=[\n    {\"src\":\"KNT\",\"where\":\"p. 178 and p. 165 s.v. Akaufaciya-\",\"stance\":\"supports\",\"note\":\"p. 165: 'Akaufaciya- adj. sb. \\\\'man of Akaufaka\\\\'… Deriv. of *Akaufaka- \\\\'Kohistan\\\\', prefix ā + kaufa- \\\\'mountain\\\\' + adj. suffix'. But note also Kent's remark 'OP kaufa- \\\\'mountain\\\\', Av. kaofa-, seems to have no cognates outside Iranian' (KNT.txt line 1030).\"},\n    {\"src\":\"POK\",\"where\":\"IEW 592 (POK_02.txt leaf 250, line 3912)\",\"stance\":\"supports\",\"note\":\"'b. Bedeutungsgruppe ,Wölbung nach oben, Haufe u. dgl.': Apers. kaufa- ,Berg', av. kaofa- ,ds.; Kamelbuckel', npers. kōh ,Berg' (setzen -ph- voraus)'.\"},\n    {\"src\":\"PHD\",\"where\":\"p. 50 s.v. kōf (PHD.txt line 428)\",\"stance\":\"supports\",\"note\":\"'kōf [kwp | = M, N kōh] hill, mountain; hump.' — MacKenzie's gloss preserves both meanings, 'mountain' and 'hump', which is the semantic bridge the root needs.\"}])\n\nN(id=21, lang=\"Greek\", words=\"guros\", verdict=\"confirmed\",\n  derivation=\"Greek γῦρος gŷros 'ring, circle, round pit' (with the adjective γυρός gyrós 'rounded, curved') is one of the pillars of the root. Pokorny IEW 398, in the r-suffix section geu-ro-s, gou-ro-s, gū-ro-s: 'gr. γυρός ,rund, ausgebogen', γῦρος ,Rundung, Kreis, runde Grube', γυρόω ,krümme'', beside Arm. kur-n 'Rücken', Lith. gurnas 'Hüfte, Fußknöchel', Norw. kaure 'krause Locke'. Klein s.v. gyre says the same and names the base: 'L. gyrus, fr. Gk. γῦρος, \\\"circle, ring\\\", which is rel. to γυρός, \\\"rounded, curved\\\", and cogn. with Arm. kor, \\\"crooked\\\"… All these words are derivatives of I.-E. *geu-r-, an -r-enlargement of base *geu-, \\\"to bend, curve, arch\\\".' Buck, in the note on Av. gaona- (§4.14), makes the same identification from the other end: 'root *geu-, perh. the same as in Grk. γυρός \\\"round, curved\\\"'.\",\n  derivation_fa=\"یونانیِ γῦρος (gŷros) «حلقه، دایره، گودالِ گرد» — با صفتِ γυρός «گرد، خمیده» — یکی از ستون‌های این ریشه است. پوکورنی در ص ۳۹۸، در بخشِ پسوندهای -r- (geu-ro-s، gou-ro-s، gū-ro-s)، می‌آورد: «یونانی γυρός «گرد، برآمده»، γῦρος «گِردی، دایره، گودالِ گرد»»، در کنار ارمنی kur-n «پشت»، لیتوانیایی gurnas «ران، قوزک» و نروژی kaure «طرّهٔ پیچیده». کلاین نیز ذیل gyre همین را می‌گوید و پایه را نام می‌برد: «همهٔ این واژه‌ها مشتقِ *geu-r- هندواروپایی‌اند، گسترشِ -r- از پایهٔ *geu- «خم شدن، برگشتن، طاق زدن»». باک هم در یادداشتِ خود بر gaona- اوستایی همین را از سوی دیگر تأیید می‌کند. ادعای نورایی درست است.\",\n  sources=[\"https://www.etymonline.com/word/gyro-\"],\n  ref_check=[{\"ref\":\"AHD\",\"status\":\"partial\",\"note\":\"Nourai cites 'AHD' without a page. Watkins's Indo-European appendix (AHD_watkins1985.txt) has no *geu- 'to bend' entry at all — its g-list runs geuə- 'to hasten' [Pok. geu- 399] → gyeu- 'to chew' — because no English word reaches that root through Latin or Greek; so the appendix cannot be the support. The AHD main dictionary does carry gyro-/gyre from Greek gyros, which is presumably what Nourai means; the claim itself is amply covered by Pokorny 398 and Klein s.v. gyre.\"}],\n  consulted=[\n    {\"src\":\"POK\",\"where\":\"IEW 398 (POK_02.txt leaf 53/54)\",\"stance\":\"supports\",\"note\":\"'f. Mit r-Suffixen: geu-ro-s, gou-ro-s, gū-ro-s, gur-no-s. … gr. γυρός ,rund, ausgebogen', γῦρος ,Rundung, Kreis, runde Grube', γυρόω ,krümme'…'\"},\n    {\"src\":\"KLN\",\"where\":\"s.v. gyre, n. (KLN_1966.txt line ~16955)\",\"stance\":\"supports\",\"note\":\"'gyre, n., a circular motion. — L. gyrus, fr. Gk. γῦρος, \\\\'circle, ring\\\\', which is rel. to γυρός, \\\\'rounded, curved\\\\', and cogn. with Arm. kor, \\\\'crooked\\\\', kurn, \\\\'the back\\\\', Lith. gurnas \\\\'hip, ankle, bone\\\\', Norw. kaure, \\\\'a curly lock of hair\\\\'… All these words are derivatives of I.-E. *geu-r-, an -r-enlargement of base *geu-, \\\\'to bend, curve, arch\\\\'.'\"},\n    {\"src\":\"SYN\",\"where\":\"§4.14 HAIR, note on Av. gaona- (SYN.txt line 5400)\",\"stance\":\"supports\",\"note\":\"'…Av. gaona- \\\\'hair\\\\', root *geu-, perh. the same as in Grk. γυρός \\\\'round, curved\\\\', etc. Walde-P. 1.557.'\"}])\n\nN(id=22, lang=\"English\", words=\"gyroscope\", verdict=\"confirmed\",\n  derivation=\"gyroscope is a 19th-century learned compound, not an inherited word: Klein, 'gyroscope, n., a heavy rotating wheel, having its axis free to turn in any direction. — Compounded of gyro- and Gk. -σκόπιον, fr. σκοπεῖν, \\\"to look at, examine\\\"', where 'gyro-, combining form meaning \\\"circle, circular, spiral\\\" — Gk. γυρο-, fr. γῦρος, \\\"circle\\\". See gyre, n.' The device and the name are Léon Foucault's (Paris, 1852), coined because the instrument made the rotation of the earth visible — literally 'rotation-viewer'. So the English word does descend from Greek γῦρος, and through it from PIE *geu-r-/*geu- 'to bend, curve'; the same element gives gyre, gyrate, gyrocompass, autogiro.\",\n  derivation_fa=\"«gyroscope» واژه‌ای است ساختگی و دانشورانه از سدهٔ نوزدهم، نه واژه‌ای به‌ارث‌رسیده: کلاین می‌نویسد «gyroscope: ترکیبِ -gyro و یونانی -σκόπιον از σκοπεῖν «نگریستن»»، و «-gyro از γῦρος یونانی «دایره»». دستگاه و نامِ آن از لئون فوکوی فرانسوی است (پاریس، ۱۸۵۲م) و نام را از آن رو نهاد که این ابزار چرخشِ زمین را دیدنی می‌کرد؛ یعنی «چرخش‌نما». پس واژهٔ انگلیسی به‌راستی از γῦρος یونانی و از راهِ آن از ریشهٔ هندواروپاییِ *geu-r-/*geu- «خم شدن» می‌آید؛ همین جزء در gyre، gyrate، gyrocompass و autogiro نیز هست. ادعای نورایی درست است.\",\n  sources=[\"https://www.etymonline.com/word/gyro-\"],\n  ref_check=[{\"ref\":\"None\",\"status\":\"not_checked\",\"note\":\"the chart cites no reference for this node; Klein s.v. gyroscope and gyro- (KLN_1966.txt lines 16956-16960) and Etymonline s.v. gyro- cover it.\"}],\n  consulted=[\n    {\"src\":\"KLN\",\"where\":\"s.v. gyro-, gyroscope (KLN_1966.txt lines 16955-16960)\",\"stance\":\"supports\",\"note\":\"'gyro-, combining form meaning \\\\'circle, circular, spiral\\\\'. — Gk. γυρο-, fr. γῦρος, \\\\'circle\\\\'. See gyre, n.' / 'gyroscope, n. … Compounded of gyro- and Gk. -σκόπιον, fr. σκοπεῖν, \\\\'to look at, examine\\\\'.'\"},\n    {\"src\":\"SKT\",\"where\":\"SKT.txt, grep 'gyre', 'gyro'\",\"stance\":\"silent\",\"note\":\"Skeat's Concise Etymological Dictionary has no entry for gyroscope (too recent and too technical for his list).\"}])\n\nentry = {\n  \"entry\": 0,\n  \"root\": \"Gĕu 1, Gu; Keu 1, Keup, Kumb, Kub, Keub, Keuk 2\",\n  \"verdict\": \"confirmed\",\n  \"modern_form\": \"PIE *g(e)u- 'to bend, curve, arch' (Pokorny IEW 393-398) together with *keu- 2 / *keu-b-, *keu-bh-, *keu-p-, *keu-k- 'to bend' (Pokorny IEW 588-592)\",\n  \"note\": \"The root box is accurate and the two page ranges are exactly right. Pokorny IEW 393 heads the first entry 'g(e)u-, g(e)u̯ə-, gū- „biegen, krümmen, wölben“; Nominalbildungen: gudom „Darm“, gugā „Kugel, Buckel“, geu-lo-s „rundes Gefäß, Kugel“, gou-no-m „Gekräuseltes, Gewölbtes“, gupā „Erdhöhle, Stall“, geu-ro-s, gou-ro-s „gekräuseltes (Haar, Welle)“, gur-no-s „Rücken, Hüfte“, gū-ro-s „rund, gekrümmt“' (= WP I 555 ff.), and IEW 588 heads the second '2. keu-, keup-, mit labialen oder gutturalen Erweiterungen: „biegen“ … kubo-s, kubbo-s „gehöhlt, gekrümmt“, kumb(h)o-s „Gefäß“, kupro-s „Buckel“, kūpā „Höhlung, Hohlgefäß“, koupo-s „Berg, Haufen“, kouko-s „gewölbt“, ka-kud- „Wölbung“'. Every one of Nourai's headwords corresponds to a real subsection: 'Gu' = Pokorny's gū-, 'Keup' = C. III keu-p-, 'Kub'/'Keub' = C. I keu-b- and C. II keu-bh-, 'Keuk 2' = B. II keu-k-, 'Kumb' = the nasalised *kumb- of IEW 396. Merging the two entries into one box is Nourai's own decision, but Pokorny invites it: at the head of keu-2 he writes 'Zahlreiche Parallelbildungen von der Wz. geu- s. dort, vgl. bes. die Gegenüberstellungen bei Persson Beitr. 100 f.', and under geu- (IEW 395) he notes that lett. kuza etc. cannot be sorted between the two 'wegen des Reimverhältnisses'. Language label ('Indo-European') and glosses ('to bend'; 'to bend, curved, hump') are correct. The chart's cross-reference 'Compare with root “Kam 2: to bend”' is also Pokorny-compatible (IEW 525 kam-p- 'biegen'). The whole page is unusually well referenced: POK:394 (gunda), POK:395 (gūzak), POK:396 (gumbed), POK:398 (gōšā), POK:589 (kōz), KNT:178 (kaufa), HRN:209 (gunde), KLN:847 (kiosk), LAT:488 (pers. kūž), BQT:1731/1836/1843/1859/1861 all hit the exact printed page. Two nodes are weak (12: French jargon; 17: Pahlavi gumbat), one is a printing error (14).\",\n  \"note_fa\": \"جعبهٔ ریشه درست است و هر دو بازهٔ صفحه دقیقاً می‌خواند. پوکورنی در ص ۳۹۳ مدخل نخست را چنین آغاز می‌کند: «g(e)u-, g(e)u̯ə-, gū- «خم شدن، برگشتن، طاق زدن»؛ ساخت‌های اسمی: gudom «روده»، gugā «گوی، برآمدگی»، geu-lo-s «ظرفِ گرد»، gou-no-m «چیزِ پیچیده و برآمده»، gupā «نهانگاهِ زیرِ زمین»، geu-ro-s / gou-ro-s «مویِ پیچیده»، gū-ro-s «گرد، خمیده»»؛ و در ص ۵۸۸ مدخل دوم را: «۲. keu-, keup- با گسترش‌های لبی و کامی: «خم شدن» … kubo-s «گودشده، خمیده»، kumb(h)o-s «ظرف»، kupro-s «برآمدگی»، kūpā «گودی»، koupo-s «کوه، توده»، ka-kud- «برآمدگی»». هر یک از سرواژه‌های نورایی به بخشی واقعی از همین دو مدخل بازمی‌گردد: Gu همان gū-، Keup بخشِ C.III، Kub و Keub بخش‌های C.I و C.II، Keuk 2 بخشِ B.II، و Kumb همان *kumb- خیشومیِ ص ۳۹۶. یکی‌کردنِ دو مدخل کارِ خودِ نورایی است، ولی پوکورنی خود به آن دعوت می‌کند: در سرِ مدخل keu-2 می‌نویسد «ساخت‌های موازیِ فراوان از ریشهٔ geu- را همان‌جا ببینید» و در ص ۳۹۵ می‌گوید برخی صورت‌ها را «به‌سببِ هم‌آواییِ قافیه‌وار» نمی‌توان میان دو ریشه تقسیم کرد. برچسبِ زبان و هر دو معنی درست است. این صفحه به‌طرزی کم‌مانند ارجاع‌های دقیق دارد: POK:394، ۳۹۵، ۳۹۶، ۳۹۸، ۵۸۹؛ KNT:178؛ HRN:209؛ KLN:847؛ LAT:488؛ و پنج ارجاع به برهان قاطع (۱۷۳۱، ۱۸۳۶، ۱۸۴۳، ۱۸۵۹، ۱۸۶۱) همگی به صفحهٔ چاپیِ درست می‌خورند. دو گره سست است (۱۲: jargon فرانسوی؛ ۱۷: gumbat پهلوی) و یکی خطای چاپی دارد (۱۴).\",\n  \"sources\": [\"https://www.etymonline.com/word/gyro-\"],\n  \"ref_check\": [\n    {\"ref\":\"POK:394-398\",\"status\":\"supports\",\"note\":\"POK_02.txt leaves 48-54. The entry heading, on the leaf whose next page marker is '394', reads 'g(e)u-, g(e)u̯ə-, gū- ,biegen, krümmen, wölben'; Nominalbildungen: gudom ,Darm; Eingeweide', gū̆t-r ,Kehle, Hals', gugā ,Kugel, Buckel', geu-lo-s ,rundes Gefäß, Kugel', gou-no-m ,Gekräuseltes, Gewölbtes', gupā ,Erdhöhle, Stall', geu-ro-s, gou-ro-s ,gekräuseltes (Haar, Welle)', gur-no-s ,Rücken, Hüfte', gū-ro-s ,rund, gekrümmt'.' The article closes on p. 398 with 'WP. I 555 ff., WH. I 112 f., 311, 629, 852, Trautmann 80, 100 f.' — exactly the range Nourai cites, and the four individual page citations on this page (394, 395, 396, 398) all land on the right page.\"},\n    {\"ref\":\"POK:588-592\",\"status\":\"supports\",\"note\":\"POK_02.txt leaves 247-250. The heading, on the part of leaf 247 preceding the '589' marker (= printed p. 588), reads '2. keu-, keup-, mit labialen oder gutturalen Erweiterungen: ,biegen' in verschiedenen Sonderungen wie ,im Gelenk biegen, Gelenk, sich bücken, sich drehen'; ,Einbiegung, Einwölbung, Höhlung'; ,Ausbiegung, Buckel, runder Haufen'; kubo-s, kubbo-s ,gehöhlt, gekrümmt', kumb(h)o-s ,Gefäß', kupro-s ,Buckel', kūpā ,Höhlung, Hohlgefäß', koupo-s ,Berg, Haufen', kouko-s ,gewölbt', ka-kud- ,Wölbung'. Zahlreiche Parallelbildungen von der Wz. geu- s. dort…'. The article runs to p. 592, where kaufa- stands. Range exact.\"}],\n  \"consulted\": [\n    {\"src\":\"WLD\",\"where\":\"Bd. I 555 ff., '1. geu- „biegen, krümmen, wölben“' (WLD_Bd1_1930 djvu line 34969)\",\"stance\":\"supports\",\"note\":\"'1. geu- „biegen, krümmen, wölben“ (ausführlich Lidén Arm. St. 111—122, IF. 19, 318, 326 ff., 341 ff., Persson Beitr. 100 ff., 936 f.). … Mit l-Suffixen: ai. gōla-ḥ „Kugel“…' — the article Pokorny 393-398 abridges, and the source of his 'WP. I 555 ff.'\"},\n    {\"src\":\"KLN\",\"where\":\"s.v. gyre, n.\",\"stance\":\"supports\",\"note\":\"'All these words are derivatives of I.-E. *geu-r-, an -r-enlargement of base *geu-, \\\\'to bend, curve, arch\\\\'.' — Klein states the root and its gloss in Nourai's own terms.\"},\n    {\"src\":\"SYN\",\"where\":\"§4.14 HAIR and §15.61 COLOR\",\"stance\":\"supports\",\"note\":\"Buck operates with the same root: 'Av. gaona- \\\\'hair\\\\', root *geu-, perh. the same as in Grk. γυρός \\\\'round, curved\\\\', etc.'\"},\n    {\"src\":\"AHD\",\"where\":\"Watkins 1985, g-list (AHD_watkins1985.txt lines 499, 557)\",\"stance\":\"silent\",\"note\":\"Watkins's appendix carries no *geu- 'to bend' and no *keu- 'to bend': the list jumps from 'geuə-. To hasten. … [Pok. geu- 399.]' to 'gyeu-. Also geu-. To chew. … [Pok. g(i)eu- 400.]'. No English word descends from these roots through Latin or Greek except the learned Greek gyro- words, so its silence is not a disagreement.\"},\n    {\"src\":\"IEC\",\"where\":\"IEC.txt, grep 'gūros', 'gouno'\",\"stance\":\"silent\",\"note\":\"Mann's Indo-European Comparative Dictionary returns no hit for either reconstruction in the OCR on disk.\"}],\n  \"nodes\": nodes,\n}\n\nout = {\n  \"pdf_page\": 176,\n  \"book_page\": 146,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-05\",\n  \"entries\": [entry],\n}\n\nwith open('/home/sfmqrb/git/rishe/data/verification/page-176.json','w',encoding='utf-8') as f:\n    json.dump(out,f,ensure_ascii=False,indent=1)\nprint('ok', len(nodes))\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk176.py"
}
```


### [2026-09-05T21:17:05.852Z] TOOL RESULT

```
ok 22
```


## [2026-09-05T21:17:06.494Z] AGENT

You've hit your session limit · resets 7:40pm (America/Toronto)
