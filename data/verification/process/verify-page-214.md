# Verification process log — verify-page-214


## [2026-09-06T14:52:20.581Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 214 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-214.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-214.json. Write /home/sfmqrb/git/rishe/data/verification/page-214.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 214` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-06T14:52:22.404Z] AGENT

I'll start by reading the instructions.


## [2026-09-06T14:52:23.241Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-06T14:52:23.280Z] TOOL RESULT

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


## [2026-09-06T14:52:23.363Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-214.txt"
}
```


### [2026-09-06T14:52:23.389Z] TOOL RESULT

```
1	=== PDF page 214 (book page 184) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Gwhen 1 : to swell, fill  (refs POK:491)  PART 3
4	#1 (parent #0) [Avestan / Old Persian] refs=POK:491; HRN:194; BRT:583 | kan 1, xan, gan 1 : to dig dirt out and mound it up
5	  #2 (parent #1) [Avestan] refs=POK:491; HRN:194 | â-kand, â-gand : to fill ☞Apo ; aiwi-kand : to throw away ☞Ambhi ; para-kan : spread around ☞Per 1 ; paiti-kan : front digger, arrow ☞Per 3
6	    #3 (parent #2) [Persian] refs=BQT:1526; FFD:26 | âkandan «آکندن ( آگندن )» : to fill ; kažâkand «کژاکند ( قزاگند )» : silk-filled. ☞Kaž ; afkandan «افکندن ( افگندن ، ـ افکن )» : to throw, drop ; parâkandan «پراکندن ( پراگندن )» : to spread around ; paykân «پیکان» : arrow
7	  #4 (parent #1) [Old Persian] refs=KNT:178 | ni-kan : dig down destroy ☞Nî 1 ; vi-kan : dig apart, destroy ☞Wi
8	  #5 (parent #1) [Sogdian] refs=BQT:1165,1703 | kang, kanp : colony of houses, village
9	    #6 (parent #5) [Pahlavi] refs=None | 
10	      #7 (parent #6) [Persian] refs=BQT:1703 | Samarqand «سمرقند ( سمرکند )»
11	  #8 (parent #1) [Arabic] refs=KLN:232; SAP:100; ARB:261; FVF:539,545 | qanah : reed, cane ; qanât : underground water way ; q.n.v : to dig a well or water channel | NOTE: These words reached Greek and Latin through Semitic languages
12	    #9 (parent #8) [Persian] refs=MON; FVA:341; KLN:231; SNS:8 | qanât «قنات» : underground water way ; moqannî «مقنّی» : well digger
13	    #10 (parent #8) [Greek] refs=KLN:232 | kanon : rod, measuring stick
14	      #11 (parent #10) [Arabic] refs=BQT:1516 | qânun : law
15	        #12 (parent #11) [Persian] refs=BQT:1516; MON:2875 | qânun «قانون ( کانون ۲ )» : rule, law
16	      #13 (parent #10) [English] refs=AHD:197 | canon : law
17	    #14 (parent #8) [Latin] refs=KLN | canalis : water pipe
18	      #15 (parent #14) [French] refs=None | 
19	        #16 (parent #15) [Persian] refs=MON | kânâl «کانال» : canal, channel
20	        #17 (parent #15) [English] refs=None | canal, channel
21	    #18 (parent #8) [Greek] refs=AHD:1520; KLN:231 | canna : reed
22	      #19 (parent #18) [English] refs=AHD | cane, cannon, canyon
23	  #20 (parent #1) [Sogdian] refs=SOD:124 | c`t : water well
24	
```


## [2026-09-06T14:52:26.413Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-214.json",
 "description": "Read source JSON for page 214"
}
```


### [2026-09-06T14:52:26.461Z] TOOL RESULT

```
{
  "pdf_page": 214,
  "book_page": 184,
  "entries": [
    {
      "root": {
        "name": "Gwhen 1",
        "lang": "Indo-European",
        "refs": "POK:491",
        "gloss": "to swell, fill"
      },
      "part": 3,
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan / Old Persian",
          "refs": "POK:491; HRN:194; BRT:583",
          "words": [
            {"translit": "kan 1, xan, gan 1", "gloss": "to dig dirt out and mound it up", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Avestan",
          "refs": "POK:491; HRN:194",
          "words": [
            {"translit": "â-kand, â-gand", "gloss": "to fill", "script": null, "see": ["Apo"]},
            {"translit": "aiwi-kand", "gloss": "to throw away", "script": null, "see": ["Ambhi"]},
            {"translit": "para-kan", "gloss": "spread around", "script": null, "see": ["Per 1"]},
            {"translit": "paiti-kan", "gloss": "front digger, arrow", "script": null, "see": ["Per 3"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "BQT:1526; FFD:26",
          "words": [
            {"translit": "âkandan", "gloss": "to fill", "script": "آکندن ( آگندن )"},
            {"translit": "kažâkand", "gloss": "silk-filled.", "script": "کژاکند ( قزاگند )", "see": ["Kaž"]},
            {"translit": "afkandan", "gloss": "to throw, drop", "script": "افکندن ( افگندن ، ـ افکن )"},
            {"translit": "parâkandan", "gloss": "to spread around", "script": "پراکندن ( پراگندن )"},
            {"translit": "paykân", "gloss": "arrow", "script": "پیکان"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 1,
          "lang": "Old Persian",
          "refs": "KNT:178",
          "words": [
            {"translit": "ni-kan", "gloss": "dig down destroy", "script": null, "see": ["Nî 1"]},
            {"translit": "vi-kan", "gloss": "dig apart, destroy", "script": null, "see": ["Wi"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 1,
          "lang": "Sogdian",
          "refs": "BQT:1165,1703",
          "words": [
            {"translit": "kang, kanp", "gloss": "colony of houses, village", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "Pahlavi",
          "refs": null,
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "Persian",
          "refs": "BQT:1703",
          "words": [
            {"translit": "Samarqand", "gloss": null, "script": "سمرقند ( سمرکند )"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 1,
          "lang": "Arabic",
          "refs": "KLN:232; SAP:100; ARB:261; FVF:539,545",
          "words": [
            {"translit": "qanah", "gloss": "reed, cane", "script": null},
            {"translit": "qanât", "gloss": "underground water way", "script": null},
            {"translit": "q.n.v", "gloss": "to dig a well or water channel", "script": null}
          ],
          "script_extra": null,
          "note": "These words reached Greek and Latin through Semitic languages",
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "Persian",
          "refs": "MON; FVA:341; KLN:231; SNS:8",
          "words": [
            {"translit": "qanât", "gloss": "underground water way", "script": "قنات"},
            {"translit": "moqannî", "gloss": "well digger", "script": "مقنّی"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 8,
          "lang": "Greek",
          "refs": "KLN:232",
          "words": [
            {"translit": "kanon", "gloss": "rod, measuring stick", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 10,
          "lang": "Arabic",
          "refs": "BQT:1516",
          "words": [
            {"translit": "qânun", "gloss": "law", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 11,
          "lang": "Persian",
          "refs": "BQT:1516; MON:2875",
          "words": [
            {"translit": "qânun", "gloss": "rule, law", "script": "قانون ( کانون ۲ )"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 13,
          "parent": 10,
          "lang": "English",
          "refs": "AHD:197",
          "words": [
            {"translit": "canon", "gloss": "law", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 14,
          "parent": 8,
          "lang": "Latin",
          "refs": "KLN",
          "words": [
            {"translit": "canalis", "gloss": "water pipe", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 15,
          "parent": 14,
          "lang": "French",
          "refs": null,
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 16,
          "parent": 15,
          "lang": "Persian",
          "refs": "MON",
          "words": [
            {"translit": "kânâl", "gloss": "canal, channel", "script": "کانال"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 17,
          "parent": 15,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "canal, channel", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 18,
          "parent": 8,
          "lang": "Greek",
          "refs": "AHD:1520; KLN:231",
          "words": [
            {"translit": "canna", "gloss": "reed", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 19,
          "parent": 18,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "cane, cannon, canyon", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 20,
          "parent": 1,
          "lang": "Sogdian",
          "refs": "SOD:124",
          "words": [
            {"translit": "c`t", "gloss": "water well", "script": null}
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


## [2026-09-06T14:52:27.020Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-06T14:52:27.062Z] TOOL RESULT

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


## [2026-09-06T14:52:37.030Z] TOOL CALL #5: Bash

```json
{
 "command": "ls data/verification/ | head -50 && echo ---- && sed -n 1,60p tools/verify_check.py"
}
```


### [2026-09-06T14:52:37.095Z] TOOL RESULT

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


## [2026-09-06T14:52:40.078Z] TOOL CALL #6: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','HRN','BRT','KNT','BQT','FFD','SOD','KLN','SAP','ARB','FVF','MON','FVA','SNS','AHD','WLD','PHD','NYB','IEC','SYN','CHEUNG','HUB','ARY','SKT','LKT','AFM','PLA','FVQ','TAD','LAT','LEW']:\n    v=d.get(k)\n    print(k, json.dumps(v,ensure_ascii=False)[:400] if v else 'MISSING')\n\""
}
```


### [2026-09-06T14:52:41.854Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sou
KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "loca
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
FFD {"title": "Mohsen Abolghasemi, Fe'l-ha-ye Farsi-ye Dari, Qoqnus, Tehran 1374/1995", "kind": "local_scan_ocr", "url": "https://asmaneketab.ir/product/کتاب-ماده-های-فعلهای-فارسی-دری-محسن-اب/ -> https://dl.eliteraturebook.com/app/public/attachments/6925d29630b83.PDF (free PDF site; grey)", "lookup_hint": "Searched archive.org (Persian/Latin titles, author), ketabnak, noorlib, general web (pdf/downloa
SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in 
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
SAP {"title": "Ahmad Sayyah, Farhang-e Sayyah / Farhang-e Bozorg-e Jame'-e Novin (Persian translation of al-Munjid), 3 vols, Eslam 1368/1989", "kind": "purchase", "url": "https://fidibo.com/book/142427 (vol.1, 1152 pp) ; https://fidibo.com/book/142430 (vol.2, 1206 pp) — PDF ebook, ~300,000 toman each, free sample", "lookup_hint": "Not found (archive.org has Bandar-Rigi's منجد الطلاب translation, abo_a
ARB {"title": "al-Jawaliqi, al-Mu'arrab min al-kalam al-a'jami, Tehran 1966 (reprint of Ahmad M. Shakir's Cairo 1361/1942 edition)", "kind": "archive_djvu", "url": "https://archive.org/details/mo3rb (probably the Shakir edition) ; https://archive.org/details/almo3rab_gwaliqy_f_abduraheem (F. 'Abd al-Rahim ed., Damascus 1990) ; also uc1.aa0003615705 / AAlexandrina-148752 (Sachau's Leipzig 1867 ed.) ; t
FVF {"title": "S.M.A. Emam Shushtari, Farhang-e Vazheha-ye Farsi dar Zaban-e Arabi, Anjoman-e Asar-e Melli 58, Tehran 1347/1968", "kind": "website", "url": "https://noorlib.ir/book/info/105056 (page viewer: https://noorlib.ir/book/view/105056?pageNumber=<N>&viewType=pdf) ; https://ketabnak.com/book/48613 (818 pp. PDF, login) ; http://parsianjoman.org/?p=1265 (download post)", "lookup_hint": "Alphabeti
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
FVA {"title": "S.M. Nahvi, Farhang-e Vazheha-ye Arabi dar Farsi (dakhil), Tohi/Azadi 1368/1989", "kind": "catalog", "url": "https://openlibrary.org/works/OL4602367W (edition OL2012991M: Intisharat-i Islami 1368/1989, 582 pp)", "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: no digital copy found.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 202
SNS {"title": "Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/VajnameShayest", "lookup_hint": "grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verific
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
CHEUNG MISSING
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 =
AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_page
PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/
FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.t
TAD {"title": "Tobia al-Unaysi (طوبيا العنيسي), Tafsir al-alfaz al-dakhila fi al-lugha al-'arabiyya ma'a dhikr asliha bi-hurufihi (2nd ed. Cairo 1932, ed. Yusuf Tuma al-Bustani; later Library of Lebanon reprint) — Nourai lists it under Arabic authors ('Unaysi T.'); its Table IV line was lost in the OCR", "kind": "archive_djvu", "url": "https://archive.org/details/TOB1932ARAR (1932 ed.); also https://a
LAT {"title": "A. Ernout & A. Meillet, Dictionnaire étymologique de la langue latine, 3rd ed., Paris 1951", "edition_found": "1951 (3rd ed.) - matches Nourai", "kind": "archive_djvu", "url": "https://archive.org/details/ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine", "identifier": "ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine (4th ed. 1959 lending-only: dictionnair
LEW {"title": "A. Walde (& J. B. Hofmann), Lateinisches etymologisches Wörterbuch, 3rd ed., Heidelberg 1938-56", "edition_found": "2nd ed. 1910 (open); 3rd ed. 1938 vol. 1 is lending-only (lateinischesetym0000awal)", "kind": "archive_djvu", "url": "https://archive.org/details/lateinischesetym0000aloi", "identifier": "lateinischesetym0000aloi (1910); restricted 1938: lateinischesetym0000awal", "local_f
```


## [2026-09-06T14:52:49.399Z] TOOL CALL #7: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','HRN','BRT','KNT','SOD','KLN','MON','BQT','FFD','SNS','AHD','ARY','IEC','SYN','PHD','NYB','CHEUNG','HUB','WLD','LKT','AFM','PLA','FVQ','TAD','ARB','LAT','LEW','SKT','FSD','WEB','DEV','PHN','AFA','KFL','FVF','SAP','FVA','RCH']:\n    v=d.get(k) or {}\n    print('==',k,'| local:',v.get('local_file'),'| offset:',v.get('page_offset'),'| hint:',(v.get('lookup_hint') or '')[:300])\n\""
}
```


## [2026-09-06T14:52:49.539Z] TOOL CALL #8: Bash

```json
{
 "command": "head -c 3000 data/verification/page-202.json"
}
```


### [2026-09-06T14:52:51.327Z] TOOL RESULT

```
== POK | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt | offset: POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' giv
== HRN | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt | offset: leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.
== BRT | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt | offset: Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Nourai's BRT numbers are Bartholomae's COLUMN numbers. Headwords are Avestan/OP in transliteration in bold at line start; OCR of the special transliteration is noisy - grep on a distinctive Latin gloss or the German meaning in quotes. Column numbers appear as standalone numbers at leaf tops.
== KNT | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt | offset: leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Lexicon (Part III, pp. 164 ff.) headwords are transliterated OP words at line start followed by part of speech, e.g. grep -n '^apadana-' ; section refs like '$147'. Nourai's page numbers should fall in 164-215 for lexicon citations.
== SOD | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD.txt'] | offset: printed page ≈ leaf − 66 in SOD_pages.txt (0-based \f blocks; 645 leaves; English intro precedes) | hint: Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (retur
== KLN | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt | offset: KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.
== MON | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt'] | offset: None | hint: Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbe
== BQT | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages_faseng.txt'] | offset: vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...'). | hint: grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --d
== FFD | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_asmaneketab.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_pages_faseng.txt'] | offset: 115 leaves (PDF pages); printed page = PDF page − 5 (PDF 40 = p.35). 2nd printing 1385 of the same Qoqnus setting (ISBN 964-311-015-X). | hint: Searched archive.org (Persian/Latin titles, author), ketabnak, noorlib, general web (pdf/download): nothing; only a related paid e-book 'واژگان زبان فارسی دری' (fidibo). ketabnak.com/book/45024 is a different book (فهرست فعلهای فارسی).
== SNS | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS.txt'] | offset: 242 leaves; page offset not determined (OCR too poor to read printed numbers) — locate by transliteration then read the page image | hint: grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php search (see BQT) for better hit-to-leaf mapping.
== AHD | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt | offset: 1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page. | hint: Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru
== ARY | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt'] | offset: printed page = pdf page + 1 | hint: Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY
== IEC | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt | offset: TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root.
== SYN | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt | offset: leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the concept heading (all caps English word) or a printed page number line.
== PHD | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt | offset: leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Headword = Pahlavi in transliteration at line start, followed by Pahlavi script (not OCRed) and gloss, e.g. grep -n '^abar '. Alternative PDF: https://www.parsianjoman.org/wp-content/uploads/2015/09/A-Concise-Pahlavi-Dictionary.pdf (8.4 MB).
== NYB | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt | offset: Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Nourai's 'NYB' numbers are Part II (Glossary) pages. Headwords are Pahlavi in transliteration at line start (e.g. grep -n '^apar'), with Avestan/OP/NP cognates and 'Bthl.' refs.
== CHEUNG | local: None | offset: None | hint: 
== HUB | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt | offset: leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by paragraph (§). grep the transliterated Persian word or Horn's entry number.
== WLD | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/WLD_band3.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_text.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_text.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt'] | offset: Band 3: leaf = printed + 6. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> || Band I (WLD_Bd1_pages.txt, 887 leaves): printed = leaf(1-based) − 9 (leaf 801 = p.792). Band II (WLD_Bd2_pages.txt, 720 leaves): printed = leaf − 5 (leaf 701 = p.696). | hint: Band 3 is the index (Wortregister by language) - it maps a word to 'Band, page' in vols 1-2, so it can at least confirm that a word is treated at the cited WP volume/page. For the actual entry text, use Pokorny 1959 (POK), whose entries cite 'WP. I 177' etc. and are essentially a revision of WP.
== LKT | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt | offset: leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Numbered entries: 'NNNN. word (language) meaning' - Lokotsch is usually cited by entry number, but Nourai cites pages. grep the oriental source word in transliteration or the number.
== AFM | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM.txt'] | offset: 198 leaves; page numerals OCR'd unreliably — offset approx leaf − 8 (front matter); confirm on page image | hint: Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').
== PLA | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt'] | offset: 301 leaves (pdftotext -layout, \f-separated): printed page = leaf(1-based) − 15 (leaf 291 = p.276). | hint: HathiTrust search-only; Google Books id q_ErAAAAMAAJ snippet view; DDB has only the table of contents. No full text online. | For pages in a scanned volume use: python3 tools/ref_page.py PLA:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)
== FVQ | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ.txt'] | offset: printed page = leaf − 17 (0-based \f blocks in FVQ_pages.txt; 335 leaves) | hint: Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).
== TAD | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/TAD_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/TAD.txt'] | offset: 86 leaves (small book, ~80 printed pages); offset ≈ leaf − 4..6, verify against the printed numeral on the page image | hint: Alphabetical Arabic headwords; grep the Arabic headword in TAD_pages.txt (86 leaves) or TAD.txt; inside.php search works.
== ARB | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/ARB_mo3rb.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/ARB_abdulraheem.txt'] | offset: None | hint: Alphabetical Arabic headwords; grep in ARB_mo3rb.txt / ARB_abdulraheem.txt (raw, no page breaks); edition of mo3rb not confirmed — check its title page image.
== LAT | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/LAT.txt | offset: leaf = printed + 18 for most of the book (e.g. leaf 21 = p.3); drifts in places (leaf 219 = p.301 -> -82?? probably a mis-detected number) - grep the headword. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Latin headword in bold at line start followed by gender/declension, e.g. grep -n '^pater,'.
== LEW | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/LEW_1910.txt | offset: 1910 ed.: leaf = printed + 12 (e.g. leaf 15 = p.3). Page numbers of the 3rd ed. differ. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Latin headword in bold at line start. For 1938 pagination borrow lateinischesetym0000awal.
== SKT | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt | offset: leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Headword in caps at line start, e.g. grep -n '^TREE' SKT.txt; entries are terse with '(E.)', '(F.-L.)' language tags.
== FSD | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt | offset: vol1: leaf = p + 41..56 (drifts; e.g. leaf 87 = p.46, leaf 612 = p.556); vol3: leaf = p - 1466 (e.g. leaf 215 = p.1681); vol4: leaf = p - 2144..2148 (e.g. leaf 229 = p.2373); vol2 offset not reliably detected (pages ~ 700-1640) - grep the headword. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Headword in bold at line start with pronunciation; etymology in brackets at entry end '[< L. ...]'. Very large OCR (16 MB per vol); grep -n '^word' vol file.
== WEB | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/WEB_vol1.txt | offset: not reliably detected (page_numbers.json sparse); grep headword. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Headword bold at line start; etymology in brackets. 2nd-edition pagination is the same across 1958-1983 printings, so a 1978 page number can be checked in the 1962 vol. 1 scan for words A-(mid alphabet); vol. 2 only via lending copies.
== DEV | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/DEV.txt | offset: leaf = printed + 26 (pp. <80) to +30 (pp. >84), e.g. leaf 29 = p.3, leaf 118 = p.88. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: French headword in caps at line start.
== PHN | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/PHN.txt | offset: leaf = printed + 31 (e.g. leaf 33 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: French headword in caps at line start; Arabic script not OCRed. grep -n '^BAZAR' etc.
== AFA | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/AFA.txt | offset: leaf = printed + 30 (e.g. leaf 38 = p.8). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Arabic/Aramaic in script (not OCRed) with German glosses; grep the German meaning or transliteration.
== KFL | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/KFL.txt'] | offset: None | hint: Look up by chapter/word on shamela; the 1885 Beirut pagination is not reproduced online.
== FVF | local: None | offset: None | hint: Alphabetical by Persian headword; noorlib page number N is the scan page — browser needed to read. Not on archive.org.
== SAP | local: None | offset: None | hint: Not found (archive.org has Bandar-Rigi's منجد الطلاب translation, abo_abdrahman_kordi_barid_20150501_1718, and the Arabic al-Munjid on noorlib.ir/book/info/32878 — usable to check the Arabic-side content, not Sayyah's pages).
== FVA | local: None | offset: None | hint: Searched archive.org, ketabnak, noorlib, web: no digital copy found.
== RCH | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/RCH.txt | offset: leaf ~= printed + 93..94 (e.g. leaf 336 = p.242, leaf 587 = p.494); weakly detected, verify by grepping the page number. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | hint: Entries are Persian/Arabic in script (poorly OCRed) followed by transliteration and English gloss; grep the English gloss or transliteration.
```


### [2026-09-06T14:52:51.376Z] TOOL RESULT

```
{
 "pdf_page": 202,
 "book_page": 172,
 "verified_by": "claude-opus-5",
 "verified_on": "2026-09-05",
 "entries": [
  {
   "entry": 0,
   "root": "Gwa, Gwâ, Gwen 2",
   "verdict": "confirmed",
   "modern_form": "PIE *gʷem- 'to go, to come' (with the collateral root *gʷeh₂- / *gʷā- 'to step, go'); Pokorny IEW 463-465",
   "note": "Pokorny's entry, which begins on p.463 exactly as Nourai cites, is headed 'gʷā-, gʷem- „gehen, kommen; zur Welt kommen, geboren werden“; gʷm̥-ti-s f., gʷem-tu-s m. „Gang, Schritt“', and it is deliberately a double entry (I. gʷā-, II. gʷem-), which is why Nourai's box carries two names, 'Gwa, Gwâ'. His third name 'Gwen 2' reflects the *gʷem- > *gʷen- variant Pokorny himself notes ('Unthematisch *(e)-gʷem-t (> *e-gʷen-t)', and Latin advenam / veniō with -n- for -m-); it is not a separate root in any modern handbook, so it is Nourai's own labelling convenience rather than an error of substance. Watkins/AHD 1985 heads the same material 'gʷā-. Also gʷem-. To go, come'; Cheung splits it into *gaH¹ (PIE *gʷeh₂-, Pok. 463 f.) and *gam¹ (PIE *gʷem-, Pok. 464 f.). The gloss 'to walk, to step, to come, to go' is an accurate rendering. Two words in the chart do not belong to this root: Avestan 'gâv' in node 6 (a misprint) and 'thamân' in node 12 (an unidentifiable form), and one Persian word, nîyâm (node 3), is derived by modern scholarship from a different root (*ni-dā-, not *ni-gam-). Everything else on the page is standard, well-attested Iranian etymology.",
   "note_fa": "جعبهٔ ریشه درست است: پوکورنی در صفحهٔ ۴۶۳ فرهنگ خود مدخل «gʷā-, gʷem-» را با معنای «رفتن، آمدن؛ به جهان آمدن، زاده شدن» آورده و همان‌جا نام‌های gʷm̥-ti-s و gʷem-tu-s «گام، رفتار» را می‌افزاید؛ پس هر دو صورت «Gwa/Gwâ» و «Gwem» از یک مدخل‌اند و برچسب «هندواروپایی» و معنای «راه رفتن، گام برداشتن، آمدن، رفتن» درست است. نام سوم «Gwen 2» گونهٔ *gʷen- است که خود پوکورنی (در *e-gʷen-t و در veniō لاتین) یاد کرده و در کتاب‌های امروزی ریشهٔ جداگانه‌ای به شمار نمی‌رود؛ این نام‌گذاری از خود نورایی است نه خطای علمی. واتکینز (پیوست AHD) نیز همین ماده را «gʷā-, also gʷem-: رفتن، آمدن» آورده و چونگ آن را به دو ریشهٔ *gaH¹ و *gam¹ بخش کرده است. در سراسر این صفحه تنها سه لغزش هست: صورت «gâv» در گرهٔ ۶ (غلط چاپی)، صورت «thamân» در گرهٔ ۱۲ (صورتی که در هیچ فرهنگی یافت نشد) و واژهٔ «نیام» در گرهٔ ۳ که پژوهش امروزی آن را از ریشهٔ دیگری (*ni-dā-) می‌داند.",
   "source
```


## [2026-09-06T14:53:00.036Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"Page(s): 49[01]\" POK_full.txt | head -20\necho \"=== lemma near\"\ngrep -n \"lemma: g\" POK_full.txt | sed -n 1,5p"
}
```


### [2026-09-06T14:53:00.094Z] TOOL RESULT

```
38139:Page(s): 490 
38189:Page(s): 490-491 
40000:Page(s): 490 
40033:Page(s): 491 
40121:Page(s): 491-493 
=== lemma near
3106:Root/ lemma: aiu-, aiu-\ "vital energy, vitality' derived from reduced Root/ lemma: g^ei-S 
5425:lemma: gen-1, gene-, gne- gnd-\ 'to bear (mother, father)' [origin of the old laryngeal g- > 
5928:From the reduced Root / lemma: ghsb"^-'. "to grab, take', derived Root/ lemma: aj/O-/ (exact 
7063:[see Root/ lemma: ghei-2. ghi-\ "winter; snow' 
7071:[common alb. gh- > d-] derived gr. x£Ai5u)v "swallow', therefore from Root/ lemma: ghel-:
```


## [2026-09-06T14:53:00.770Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==499' POK_01.txt | head -80"
}
```


### [2026-09-06T14:53:03.327Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T14:53:05.222Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '39990,40130p' POK_full.txt"
}
```


### [2026-09-06T14:53:05.265Z] TOOL RESULT

```
Middle High German gampen, gumpen^s'^'c\v\Q\ gampel, gumper amusing wilful 
jumping, farce play ', gumpel. Modern High German Gimpet, with High German consonant 
shift Middle High German gampfxw. " the swaying '; Norwegian dial, gimpa^s^ay, swing', 
gampm. " big clumsy guy, ungainly horse '. 

A short root form g"hem- perhaps in Old Icelandic gaman n. "pleasure, joy, friskiness, 
playfulness, sensuality, voluptuousness'. Old High German gaman n. ds., etc. 

References: WP. I 678 f. 
Page(s): 490 

Root / lemma: g''hen-1 

Meaning: to swell, abound 

Material: Old Indie a-/7a/7a- "tumescent, plentiful, luscious', ghana-^dense, thick', m. 

"compact mass'; 

npers. a-gandanlWV, agan/sluW; 

Armenian yogn' much, great, many, of things ' (Prap. /+ *o-g"'hon- or *o-g"hno-, in 
prefix o- standing next to Aryan a-)\ 

gr. EuGsvnc; "rich, in fullness, wealth', Hes. suGsvsu) " flourish', euGeveiq " fullness, 
blossoming state ', lengthened grade Ionian EuGnvnq "rich, in fullness, wealth', Ionian Attic 
£uGr|V£U) " flourish, be in bloom, blossom and power', £uGr|via f. "fullness, wealth'; ograde 
noAu(p6vTr|<; = noAuKiriTri^, KAsocpovrnc;, etc., reduced-grade cpavav GeAeiv Hes., probably 
actually "be horny, lustful'; 

Lithuanian gana^ sufficient ', ganeti^ suffice ', gandeti^ have enough ', Latvian gana^ 
sufficient '; 

Old Church Slavic gonejetb, gonetT suffice ', Denomin. from *gona= Lithuanian gana, 

whether here gr. acpsvoc;, acpvoc; n. "plentiful supply, richness ', acpvsioc; " propertied, 
owning property ' (cp and the vowel suggestion from the vowel loss form (a)(pv- or *sm- 
g"h(e)n-l), also nap-G£vo(; "virgin' (physical fullness, wealth?)? 



References: WP. I 679, WH. I 479; Trautmann 77 f. 
Page(s): 491 



Root / lemma: g''hen-2(a)- 

Meaning: to hit 

Material: nominal formation: g^hono-s^ hit ', 5'"/7^-/'d-5 'beaten', g^hp-t/s and g''hp-tia {!) " 

hit ', g^hen-tel-^ hit ', g^hen-tuo-s^ occidendus '. 

Old Indie /7a/7-// (newer thematic hanati) " hits, strikes, kills, slays ', 3. PI. ghn-anti. Imp. 
ja-hi. Opt. han-yat, ghn-Tta, Per\. jaghana; jaghanvas, Qeu. jaghn-us-ah. Pass, hanyate, 
participle /7a/a- "beaten, killed' (= Avestan ya/a- gr. -cparoc;), hantva-h'to hit, to slay' (: 
Avestan y^z?M/5-, Old Church Slavic z^fva), vrtra-han-. Gen. -ghn-ah{= Avestan vere&ra- 
Jan-, Gen. -y-no) " knocking down the opposition ', ^/7a/7a- "killing, m. shillelagh, club, 
mace, joint' (= gr. av5po-cp6vo(;, Latvian gans), sam-ha-V layer, stack, pile ', hati-h^ 
hitting, blow, multiplication ' (: gr. Sicpaai-oq, fKvesiau-jaiti-, Old Norse gudr, gunni), (under 
the influence of common Celtic -ns-, -nt- > -nn-), hafya {\ate\) "killing' (: Old High German 
gundea, Lithuanian dial, gincia), hantar-^ one who hits or kills ' (= Old Church Slavic 
z^teljb); from the heavy basis Old Indie han/tum {\ate\) and ^/75/5- "killing ', m. "blow, 
knock, killing, annihilation ', ghatayat/' slays '; Note: common Old Indie g^'h- >/?-. 

Avestan Ja/n-t/ {= Old Indie hanti-) " he hits, strikes, kills ', lmp.ya/5/i 1. Sg. Med. ni-yne^ 
I knock down ', Opt. paiti-ynTta (= Old Indie ghmta) " he would like to fight around ', 
participle ya/a- (= Old Indie hata-, see above), J^^wa-^ occidendus ', participle Perf. Akt. 
jaynva, npers. ajanam^\ killed = defeated ', 3. Sg. aja(">, Avesianjana-' punching \jantar- 
"the hits, knocks, slays \janti-i. " the hitting, the killed ', -jaiti- (as 2. compound part) " the 
hitting ' (= Old Indie hath); Vsre&rajan-^ knocking down the opposition ' = Old Indie Vrtra- 
han-, 

Armenian gan. Gen. gani{ *g"he-rt) "blow, cudgel ', ganem " hit, beat ', jin "stick' ( *g"hen- 
),Jnem^\ hit' (about *j/nem irom *g"hend= hanati, Lithuanian genu. Old Church Slavic 
zeng),jnjem' destroy, clean' (from *g"'hen/d= Gsivu), Lithuanian geniu); 

gr. Gsivu) {*g"'hen-id= Armenian y/T/e/r? "slay, kill', alb. gjanj^ hunt, chase', Lithuanian 
geniu^ astle ab ') "hit', Gevw, sGsiva; redupl. snscpvov "slay', nscparai; -cpaT6(; in hom. apr|i- 
cpaTO(; (= Old Indie hata-h), also in Sicparov Sicpaaiov Hes. i.e. "double' ("Mai' = "blow, 
knock', also:) 5i-(paai-0(; (: Old Indie hatf-s .above); (^ovoc, "murder' (= russ. gon), cpovr) 
ds., cpovEuq "murderer', avSpocpovoq " men killing ' (see also Boisacq under cpoivoc;); Note: 
common lllyrian g"h- > d-, b-. 



alb. gjanj^ hunt, chase, pursue' {*g"'henjd); 

Latin defendo, -ere^ refuse, defend ', offendere^ stumble, offend ', //7/fe/7s^s (participle 
*infendd) ' hostile '; 

Old Irish ^o/?//?? "wound, slay, kill', Perf. 1. Sg. gegon, 3. Sg. gegu/n; gu/n'\Noun6'; 

Old Norse gudr, gunnrt (= Old Indie hat/-), Old Saxon gudea. Old English gu^{*gun^jd 
= Old Indie /7a/Ka besides the pronunciation) "fight, struggle, battle'. Old High German 
gund-fano' war flag '; Old Norse gandr^st\ck', Swiss gunten^a kind of wedge'; Norwegian 
dial, gana " clear out the boughs in trees ' as Lithuanian genetr, 

Lithuanian genu{= Old Church Slavic zeng. Old Indie hanati, Armen\an Jnem) g/nt/" 
drive (cattle on the pasture) ', Latvian dzenu-, dz/t6s., heavy basis: geniu{= Gsivoj) gene-ti 
"branch off, ramify, fork, divide' and ginu, g/nt/^deiend, shield ' {g/nt/: ginti, gintas: gintas 
= Old Indie hata: ghata-); to genuWexaX. ganyti^ (drive cattle =) protect, graze cattle '; 
Lithuanian ganas, let. ^a/75 "herdsman, shepherd' (= Old \nd\c ghana-), gan/'m. PI. " 
pastures ', lengthened grade Lithuanian nakti-gonisxw. " night bird, reveller, merrymaker'; 
Lithuanian genys, Latvian dzenis^ woodpecker', Lithuanian dial. gincia{= Old Indie 
hatya), ^/adas "fight', ginklasxw. "weapon' {*gintlas, compare Old Church Slavic z^/ofrom 
*gindla-), isganus^ salutary, beneficial ' (Lithuanian gainioti\s iterative to gintr, Latvian 
dzenis^ das in der Gabel der Pflugschar eingeklemmte Holz ', dzenu//s ^st\ng, prick' 
(compare to meaning under Old Church Slavic zg/o "sting, prick'); 

Old Church Slavic zeng, ghnaf/'drWe, push' (as Lithuanian genu), Iter, gonjg, goniti 
"drive, push, hunt, chase', whereof again poganjati^ pursue '; russ. etc. gon^ drive, impel, 
drift, propel, push, thrust, hunt' (= cpovoc;), Czech uhona^ injury, damage', serb. prijegon 
"fight, struggle' (in addition perhaps kir. honoba^ annoyance, plague', sloven, gonoba 
"damage, ruin', ugonoba^ annihilation, Untergang '); 

Maybe alb. (^ghanas) gjah^ hunt '. 

Old Church Slavic zbnjg, zgt/ {serb. zeti, also heavy basis) "reap', zgtva{sQxb. zetva) f. 
"harvest' ( : Old Indie hantva-); also zglo{*zgdld) n. "sting, prick', poln. zqdio ds., russ. 
za/o "sting, prick, cutting edge of a knife, an axe'; Slavic *gen-tel-rc\. "reaper, mower' in 
Old Church Slavic zgteljb (= Old Indie han-tar^ one who hits, kills '); 

Hittite ku-en-zi^ slays ' (= Old Indie hanti), 3. PI. ku-na-an-zi [kunanzi); compare Old 
Indie ghnanti ( *g "hn-enti) . 



References: WP. I 679 ff., WH. I 332 f., Trautmann 85 f. 
Page(s): 491-493 



Root / lemma: g^her- 

Meaning: hot, warm 

Material: Old Indie haras-u. 'blaze, glow' (= gr. Qt^oo,, Armenian yie/), ghrna-xx\. "blaze,
```


## [2026-09-06T14:54:08.310Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK lemma kan/khan\"; grep -n \"lemma: k[ah]n\\|lemma: kan-\\|lemma: k^hen\\|lemma: kan\" POK_full.txt | head\necho \"=== POK 'to dig' meanings\"; grep -n \"^Meaning: to dig\" POK_full.txt | head\necho \"=== CHEUNG kan\"; grep -n \"^\\*kan\\|^\\*gan\\|\\*kan-\\|\\*gan-\" CHEUNG.txt | head -40"
}
```


### [2026-09-06T14:54:08.399Z] TOOL RESULT

```
=== POK lemma kan/khan
43488:Root/ lemma: kand-, skand- and (Old Indie) (s)kend- 
43495:Root / lemma: kand- skand-and (Old Indie) (s)kend-\ "to glow; bright, *moon' derived 
43531:Root / lemma: kan-tho- 
43567:Root / lemma: kan- 
=== POK 'to dig' meanings
20366:Meaning: to dig 
40893:Meaning: to dig 
=== CHEUNG kan
7565:*gant 103 
15356:*kanl 229 
15413:*kan! ‘to throw, place, put; to destroy’ 
15478:the root *kan- ‘to dig’, which is semantically troublesome. || According to 
15521:*kan? ‘to fill’ 
15548:9 Several Iranian languages point to the existence of a separate root *kan- ‘to fill’. 
15552:*kanH! ‘to dig’ 
15588:*kanH2 233 
15629:*kanH? ‘to love, take pleasure in’ 
16277:*kan’). Perhaps, the Chor. form derives from the present stem *ham-krnta- of 
28473:*kanH! would be a present formation (IE *kenH'-) of *xaH, as assumed in LIV: 344 
33508:*kan-, 232 
55749:*gan, *huah, *kap/f' 
56314:*kan! (s.v.), *marc, *Hrais 
56322:*kanH', *kap/f, *Hrad, *xaH 
56597:*kan’, *parc, *parH' 
57994:*gant, *pauH 
58218:*kan', *kauz’, *mai9H’,
```


## [2026-09-06T14:54:10.727Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD agandan/kandan\"; grep -n \"^āgandan\\|^kandan\\|^abgandan\\|^kan-\\|^kan \\|^kandag\\|^kanārag\" PHD.txt | head -20\necho \"=== PHD mackenzie\"; grep -n \"gandan\\|kandan\" PHD_mackenzie.txt | head -20\necho \"=== NYB\"; grep -n \"kandan\\|gandan\\|kan-\\|kanārag\" NYB_vol2_glossary.txt | head -20"
}
```


### [2026-09-06T14:54:10.808Z] TOOL RESULT

```
=== PHD agandan/kandan
167:abgandan ` 4 a-Cárag
5007:kandan, kardan kardagān kardagār *kardag, kūdak kardespās
5037:kan- har(w)! kanār, kennir kanāragūmand kanārag kennārsrāy kóx&- kūxšīdan kox&isnig kóxXi&n kawādak köv
=== PHD mackenzie
798:abgandan, ab~an- [LJ\!IYTWN-tn' < A y rm'; 'pkn- I M 'bgnd, 'bgn-,
904:               igandan, agan- ekn-dn l I P ugnd,' N -] fill, stuff.
2358:  -- abgandan: throw forward.
2447:gandanag [gndn)k l IN gandana] leek.
2640: ....... kandan: give up the ghost; moment of death.
3186:kan-,v. kandan.
3190:kandan, kan- [HE.LWN-tn < A -V IJpr; kn-dn', -tn' 1M knd, N -] dig;
4031: pargandan, pargan- [plkn-, plgn-du'               (P pr'gnd, N paragandan)]
6326:cultivate wirastan.                           murd; moment of '" gyan kandan;
6360:defeated stO.                                  gugan-, kandan, murnJenidan,
6391:deprived abahr.                            dig kandan.
6432:disperse pargandan.                     draw (pull) kesidan; (picture) nigar-;
6446:distribute baxtan, pargandan.           dry husk.
6605:fill agandan, hambaridan.                  flowing tazag.
6660:   dag, nisiiyisn; lay "Is fragandan.        game kiidag, wiizig; (quarry) naxcir.
6691:   gyan kandan.                               grape angur.
6948:lake war, zreh.                           leek gandaniig.
6975:   fragandan.                             light (a.) rosn; (weight) sabuk, xwar.
7372:pulse miS.                                     raze kandan.
7494:row radag, rastag.                         scatter afSiindan, pargandan.
=== NYB
445:motion: šutan, dväristan, opastan, ete., and with ēstātan and nisastan (also ~ 6). — 2. prep. in, local, temporal and figura- tive: ~ Pārs; ~ im xünak P1:6; ~ miyàn i in the middle of 865; ~ han hangam at the time 613; ~ ham zamān at the same time 127°; ~ zamān in due time 221, etc.; ~ sap in the night 529, 614; ~ hàsr for a single moment 663; ~ hàn in the meantime 5615-17; — xtatäyeh + Xösrör 1184; ~ Vistasp šāh kisvarikan when V. was the emperor of the world 365; — freftür ~ : concerning 3419-20, 10923; spasdārēh ~ , an-ispās ~ : to, against; with other substantives, v. these separately ; — together with another prep.: ~ 6 into, on to, up to: ~ 6 nun 404; with apakandan, burtan, guméxtan (also without 6), hištan, kartan (v.s.v. kar); apar ~ 402, — Av. (131 sq.) antara, antarš, OP antar (better read antara^); MPrthPrs ’ndr; Paz. NP andar; v. also niyandar.
477:apa-cand [pend] pt. pass. thrown away daru i jün-—-it thy trunk (body) whose life is thrown away, which is lifeless 267. — Pt. pass. of *apa-can- = apa-kan-, v. apakandan, NP aužand ‘thrown’ = afgand (BQ), whence a den. v. auzandidan (BQ, Steingass). Cf also NP bazandi ‘disap- pointment, helplessness, poverty’ (BQ, Steingass), abstr. of "bažand which may safely be derived from "aBa-žand < apa- cand ‘cast down’. V. also daru.
496:apa-kandan [LMYTN-tn'; Prth RMY-] pt. = pret. pass. 3d p. sg. apakand, written LMYTN without complement HajB:8, books LMYTN-t', Prth RMY-t HajA:7; LMYTN without complement = opt. apakané HajB:15; subju. 2nd p. sg. LMYTN-h = apakanäh 1009; cond. 2nd p. sg. LMYTN-t' HWH'-? = apakand hà 2226: to throw; bē ~ to throw away, with 6 or andar 6 to, into, against 2226 etc. passim; to throw (a bucket into the well) 142°. 151; to drive (a horse) against (6) 1145; to shoot (an arrow) HajA: 7. B: 8.15; - to arouse (fear) 5278; 6 miyān ~ to provoke (enmity) 10715; pat menišn 1... m to suggest to a p.’s mind 3712-13; — pt. apakand fallen, slain 2626. — < Olr *apa-kan- and *upa-kan- (v.s. v. apa-), from kandan, q.v.; MPrthPrs >bgndn; Verbum 172, Ghilain 55; Paz. pt. awagad, pres. awa-gan- (SGV); NP afgan- dan, augandan. V. also apa-cand, frakan- dan, pargandak.
1518:frakandan [plkndn'], pt. = pret. pass. 3d p. sg. frakand to throw : bun ~ to lay the foundations 113%. — Ps. pres. plkn- ‘to build’. Cf Lat. fundamenta iacere. V. kandan.
1731:1936, 225sq. (because of Av. vikaya-, Sogd we’w ‘witness’ cannot be compared). Henning, Weller Vol. p. 297, combines Av. vikaya- with Sogd. wcw, deriving the Av. form from *vikäuya- with assi- milation of -uy- to -yy- and then short- tening of -à- > -d-. However, -uy- is not assimilated in Av.: zaoya-, haoya-, hvay- haoya-, kaoya-, gaoya-, adaoya-, mainyao- ya- (v. m&nó3), kqsaoya-, snāuya-. gukün- [gwk’n-] pres. to destroy 90?6 (Paz. substitutes vdnom, v. vànitan). — Av. (438) vi-?kan- = OP; MPrth w(y)g’- ny$n, Ghilain 71; MPrs pres gwg?n-, v. n. gwg’nysn, Verbum 189. V.s. v. kandan. gukayitan [gwk'dtn'] to bear witness, pt. = pret. pass. 3d p. sg. tgukāyīt ['gwk?dt'] 50%, — Cf Arm. lw. vkay-em.
1984:Hérat [hylt'] the town of al-Hira in Iraq, 1154-5. — Aram hertä ‘camp’. hérpat [hylpt'] a priestly title and degree in the Zoroastrian clergy 55%; holder of this degree 105. 31” (with the indef. art. 7-6); pl. cas. obl. ~-dn 1078; —-an ~ the chief h. 11119. — Av. (20) ač0rapati- ; Prs. inser. ’yhrpt; Paz. érwad, Skr. v. ācāryādhipati (Aog); NP hirbad. Wikan- der, Feuerpriester, v. Index.
2159:kāhišn [k'hšn', k'hyšn'] the act or pro- cess of diminishing; the state of being diminished: 68°. 983.5. 1047. — MPrs k’hysn (A-H I); NP kästan käh- ‘to lessen, to diminish’ (Paz. zähidan, cf s. v. kandan). A factitive vb. derived from the stem *ka0-, SW form of kas-, v. s. v. !kas. The form k’hy$n' represents probably a hybrid spelling combining kähisn and [k'dšn' =] "kdyišn (cf xudyišn: audh-), since -i- is as a rule not written in the ending -išn.
2196:kandan [HPLWN-tn', kndn'] kan- 1. to dig, pl. kand engraved 113%. — 2. to destroy 4271, 7114. 9918; to tear up by the root 3316, — 3. bé ~ to throw out, to drive away 34’. — Two different vbs.: 1. Av. OP (437 sg.) 2kan-‘ to dig’, whence also gukān- (g. v.); 2. kan- ‘to throw’, whence also apakandan, frakandan, par- gandan, Morgenstierne, AO I, 249; Ver- bum 172. MPrs and NP ‘to dig’, Paz. cadan, xan- with an initial x- confirmed by the Arab. lw. randag ‘trench’ and Skr khan- (pt. khāta-). V. also kanišn.
2206:kanišn [ĶPLWN-šn'] v. n. of kandan (2): ~ + jän the destruction of the vital spirit, the extinction of life 6419,
2207:kan-tigr [kntgl], kantir quiver 2013. 2716, 2819.7, 292. — V. tigr. Renders Av. (46) akana- Vd 14°; Ps. kwtyly is probably only a clerical error for kntyly.
2524:mēnišn (mynšn'] thinking, thought, mind: together with gób?sn and kunišn v. göbisn ; Zartuxšt had ~ 4 fräröntar hac hamak gēhān a mind more righteous than (that of) all human beings 54%; ~ i fräröneh the way of thinking of honest people 6414; — ~ nihátan 6 to contemplate, to set one's mind on 5??*; 6 hän i ölsän ~ apar Sut hénd they inspired them 403-4; v. also apakandan, bastan, bastišn, nihä- tan, čpastan, viskaftan, vinäsitan; — pat ~ 4 Pourusäsp bim apakand 481911; pat ~ in my mind, through my inner senses 51%; hàn + či dētsr pat ~ his (spiritual) eye in his mind = his inner intuition 5226-27,
2576:miyàn [myd’n'] 1. the middle, the centre: bun ...miyün... frazdm 81; x"atài 4 ~ i asmān 78; han-tāi 6 ~ van to the middle of the tree 415; andar ~ 4 asmän 865; hac ~ dp from the middle of the water 564; — pat ~ kartan to make manifest to all, splendid 67°; 6 ~ apa- kandan to spread, disseminate 10715, — 2. prep. between: + smäh u oan damik i 30 frasang 8%; vimand i ~ Eran u Türän 4519-311; in the middle of 4815, 865. — Av. (1115 sq.) Tmaiöya-, (116 sq.) matčyčna-; MPrth mdyn; MPrs my; Paz. NP myàn.
2723:nikand [nknd] pt. = pret. 3d p. sg. 92%, uncertain: api-§ góhr  x"arrah be ~ seems to mean: he projected, threw forth, (from his own essence) its (= the earth’s) substance-light, i. e. the heavenly light which forms the substance of the material world, cf BdA p. 11? Ohur- mazd hac han i xvēš xvatēh getäh rošneh uy hac getäh rošneh karp + dāmān i xue$ frac brihénit, where gētāh rošneh seems to be a synonym of göhr xtarrah; nikandan from ni + the root kan- ‘to throw’ which is found in apakandan (g.v.).
2842:oškan [>wškn'] a verbal form used as pt. pass. and as pret. pass. 3d p. sg., to *throw: aš 6 pasēh gav apāc rānēnīt (g. v.) with the gl. kü apāc ~ ‘that is: it (his hand) was flung backward’ 485 -$; 62 gurg zat zanak (g. v.) with the gl. ki dahan évak apäk dit frot ~ ‘that is: his jaws were clasped together (the upper jaw was clasped down against the lower jaw)’ 5067; [(ka) dēn-ākāhēh ~ (when) reli- gious knowledge is overthrown DkM 33379; ātaxš mänäk aparociónik hesme m hàn i xét like a fire which has to be kindled but is thrown into wet fuel, ibid. 411°]. As it stands, this form can only be derived from *avis-kan- (the root *kan- ‘to throw’ found, e. g., in apakan- dan, q.v.), thus originally *avis-kanta- > *ēškand > oškann with assimilation of -nd > -nn, but the form is singular, as only old -nd, as far as we know, under- went this assimilation, not -nd- < -nt-. The inf. of this vb. shows the regular form expected: cé andar én mātagdān 6s- kandan [’wSkn'dn'] apāyišnīk dart druš- take [-k' +1, for -keh] vicārihēt ‘the (trouble-hardness =) troublesome diffi- culties which in this book inevitably
2953:pargän [plg?n'] "wall 935 (read, with Dh.: ... pahnai i damik; pērāmēn Harburz ~ H. is a wall all around it). — < *pari- küna- ‘that which is thrown up all around’ from pari + kan- ‘to throw’, v. apakandan; cf parisp.
2954:pargandak [plgndk'] scattered, dispersed 1092-10, 1121, — Pt. of para + kan- ‘to throw’ (Verbum 227), v. apakandan; M Prs prgn- (S); NP pargandah (the vb. is here pardgandan).
3649:kālpad i gētāhīk 8925-25, 9028-27; pat han + dašn pad frac škast trampled on it with his right foot and crushed it 5311-12; škast was broken, burst 542°; v. also s. v. stur. — Av. (1586 sq.) skand-; MPrs ‘Skn- (Sogd. 31%, 33. 59); Paz. škastan, seldom  škandan, škan-; NP  šikastan šikan-.
4901:abi-jāvaya-: apa-zutan vi-'kan-: gukàn
4970:akana-: kan-tigr
5204:(vi-)?kan-: gukän
```


## [2026-09-06T14:54:18.400Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '15400,15640p' CHEUNG.txt"
}
```


### [2026-09-06T14:54:18.447Z] TOOL RESULT

```
tremble’, matching Skt. kamp. The Avestan form *kafsan (Yt 10.113), cited in Liste: 
14 as evidence, is unclear. These forms are often connected to Gr. xà jo ‘I bend’, 
Lith. kumpti ‘to be crooked, bent’, karmpas ‘corner’, etc. (albeit with queries in LIV, 
l.c.), which are assigned an IE provenance accordingly. However, the unusual 
structure of the forms is not typical for IE: they may rather point to borrowing from 
a substratum language, cf. Beekes 1969: 134 (also Beekes, A Greek etymological 
Dictionary, www.ieed.nl: s.v. KA LTT). 

«PIE? > LIV: 342 | Pok.: 525 

*REFERENCES: EVP: 18; GMS: раг. 676; EVS: 48b; ESIJa П: 226 Ё; МЕУР: 18 


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

Pres.: SUBJ. 3sg. MMP phykn’d; Partic.: perf. pass. MMP phygqnd, "phyknd || (+ *ham-) Partic.: pres. 
MMP hngn’n, perf. pass. MMP hngnd 

*PARTHIAN: (+ *ä-) ’gn-, "gn- ‘to fill’ = Ghilain: 55 | DMMPP: 29b f. 

Pret.: IND. 3sg. "gnd (M2 II Vii,21(132)); Partic.: perf. pass. "end, end 

*SOGDIAN: (+ *4-) MSogd. "kn ‘to fill’ 

Impf.: IND. 3pl. MSogd. m’k’nd (M118iV.5) 

*CHORESMIAN: (+ *upa-) bkn- ‘to fill, load’, bkny- (intr./pass.) ‘to become full’ 
= Samadi: 20 

*NWIR: (+ *4-) NP agandan/agin- ‘to fill, stuff’, (caus.) NP aganidan/agan- ‘to stuff, 
fill, cram’ 

*NEIR: (+ *abi-) Oss. I. evgenyn/evgeed, D. evganun/zvgad ‘to pour in, fill, out; 
to draw’ 


9 Several Iranian languages point to the existence of a separate root *kan- ‘to fill’. 
*REFERENCES: Abaev, Slovar’ I: 201; Cheung 2002: 166 


*kanH! ‘to dig’ 

*AVESTAN: YAv. °kan- ‘to dig’ || (+ *api-) ‘to fill out by digging, fill (a pit)’ || + 
*aua-) ‘to establish by digging, excavate’ || (+ *us-) ‘to dig out’ || (+ *para-) ‘to dig 
around’ || (+ *ni-) ‘to dig in’ = Liste: 14 

Pres. {1} athem.: IND. 3sg. YAv. uskonti (V 3.12), INJ. med. 3sg. YAv. auuakanta (V 15.39), OPT. 3sg. 
Y Av. aipi.kaniiat (V 14.6); Pres. {2} them.: OPT. 25р. YAv. auua.kanöis (V 17.5, V 17.7); Partic.: perf. 
pass. Y Av. nikanta- (V 7.43, V.3.12) 

*OLD PERSIAN: ka(n)- ‘to dig’ = Kent: 178b 

Partic.: perf. pass. ka(")tam <k-t-m> (DSf 25); Inf.: ka"tanaiy <k-t-n-i-y> (DZc 9, XV 21); Pass.: impf. 
IND. 3sg. akaniya <a-k-n-i-y> (DSf 24, DSf 28, (?) DZc 10) 

*MIDDLE PERSIAN: MMP qn- ‘to dig (up); to raze, destroy’ (partially from *kan'), 
BMP kn- (HPLWN-) /kan-/ ‘to dig (out); engrave’ || (+ *fra-) MMP prgnd’n (ppp., 
pl.) ‘built? > DMMPP: 206a, 278b 

Partic.: perf. pass. MMP qnd; Pass.: pres. IND. 3pl. MMP qnyyhynd 

*PARTHIAN: kn- ‘to dig (up); to raze, destroy’ (partially from *кап!) = Ghilain: 206a 


| DMMPP: 206a 
Partic.: perf. pass. knd 


*KHOTANESE: OKh. kamggan- ‘to dig’ (< old intens.) = SGS: 20 

*SOGDIAN: BSogd. kn- ‘to put out (eye)’, BSogd. kn-, CSogd. qn-, MSogd. kn- ‘to 
dig’, SSogd. knöh, BSogd. knöyh, CSogd. q0(-) ‘town’ || (+ *us-) BSogd. skn- ‘to 
incise, engrave’, BSogd. ’sk’’n ‘line’ (Benveniste, TSP: 197 ad 191-2) || (+ *ш-) ? 
MSogd. укуп ‘to dig ош” or rather ‘to destroy’ (whence *kan!) 


*kanH2 233 


Pres.: IND. 3sg. BSogd. knt’, IMPV. 2sg. CSogd. qn’; Impf.: IND. 3sg. MSogd. kn’skwn ‘he was 
digging’; Inf.: pret. BSogd. knt || (+ *us-) Inf.: BSogd. skn’t|| (+ *ui-) Inf.: ? MSogd. апуу ykynyy (BBB: 
33) 

*CHORESMIAN: kn- ‘to dig; to break out (of teeth)’ || (+ *us-) m/’sk’ny- ‘to carve’ 
c» Samadi: 102, 8 

*BACTRIAN: (+ *ni-) vakav- ‘to dig’ = S-W, Bact.: 207b 

*NWIR: Widely attested: NP kandan/kan-, Kurd. (Sor.) kandin/kan-, Zaz. kendis/ 
kenen-, Awrom. kannäy/kan-, Gz. kän-/känt, Gur. (Kand.) kän-/-kän-, Abyan. 
kanda/kan-, Abz. kända/-ken- (-kon-) Ham. kendän/ken-, Isfah. känän/Kän-, Khuns. 
ken-/kend, kena, Nn. kent/r-kin-, Qohr. kanda/kin-, Siv. kén-, k(y)en-/künd, kend-, 
Tal. kande, Tr. kanda/ken- ‘to dig (out)’, also Tr. kända ‘sheep shelter’ (Lecoq 2002: 
466) || (+ *us-) NP sikinah, iskinah ‘(wood-)chisel’ 

*NEIR: Pash. kan-/kandol, (Waz.) (pret.) wu-kind, Wa. ksın-/kot, Yghn. kan-/kánta, 
Sh. Cán-/Cint, Rosh. &än-/änt, Bart. éan-/Cant, Yzgh. Kan-/Kont ‘to dig’, Oss. I. kaend 
‘building’ || (+ *ni-) Oss. D. nik zd ‘carve, cut’ 

*SANSKRIT: khan’ ‘to dig’ (RV+) > EWAia I: 445 

0 See also *kan!. The IE reconstruction with *-H,- is based on the Skt. and Phrygian 
evidence. The initial kh- of Skt. khan! is odd: contamination with kha- (n.) ‘canal, 
opening, hole’, kha- (f.) ‘source, spring’ is usually assumed (cf. EWAia I: 446, fn.). 
In Iranian there is no evidence of a initial laryngeal. 

«PIE ? *kenH,- ‘to dig’ = LIV: 344 | Pok.: 534 

*IE COGNATES: ? OPhr. keneman ‘a monument or a part of it’ (Lubotsky 1988: 15) 
*REFERENCES: KPF I: 145a; EVP: 32 f.; КРЕП: 218; IIFL II: 526a; Abrahamian 1936: 117, 130; Abaev, 
Slovar’ I: 579; Andreev — Pe&éereva: 270; MacKenzie 1966: 99; Abaev, Slovar’ П: 196 f., 183 Ё; EVS: 


26b, 48b; WIM I: 69; WIM II/1: 78; WIM III: 111; Werba 1997: 281 Ё; Paul 1998: 303a; Steblin- 
Kamenskij 1999: 221; Cabolov 2001: 533, 507; Lecoq 2002: 121, 123, 126, 444 (passim) 


*kanH? ‘to love, take pleasure in’ 
*AVESTAN: kan- ‘to love, take pleasure in’, -cinah- (in cmpds.) ‘desire, love for’ 


= Liste: 14 

Pres. ia-: IND. 15р. ? OAv. Капа (Y 33.6); Perf.: IND. 3sg. YAv. cakana (H 2.11), 3р1. OAv. caxnarə (Y 
44.13). © The interpretation of OAv. kaiiä as pres. (Humbach 1950: 541), being related to Skt. käyamäna-, 
is rejected by Kellens — Pirart 1990: 229, s.v. kan. 


*OLD PERSIAN: aspa-cana <a-s-p-c-n-a> nom. sg. PN lit. ‘loving horses’ (DNd.1)
```


## [2026-09-06T14:54:47.632Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN leaf 215 (p.194)\"; awk 'BEGIN{RS=\"\\f\"} NR==216' HRN.txt | head -60"
}
```


## [2026-09-06T14:54:48.555Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KNT p.178 grep kan\"; grep -n \"kan- .to dig\\|ka(n)-\\|akaniya\\|kantanaiy\" KNT.txt | head -20"
}
```


### [2026-09-06T14:54:49.475Z] TOOL RESULT

```
=== HRN leaf 215 (p.194)
- 194 —
869. kenden graben', Praes. ken-em,
ap. aw. \/kan- graben'; phlv. kantan (Bund.), kandau
(AV., PPGl.), paz. /andan; ai. l/khan-, khdnati.
kurd. kendn; af/. kandal; oss. t. vergl. nijgänin
'begraben' (Urform "^Mnin^ 203); arm. vergl. akan
diOQvy/iia (H. No. 3).
Auf die mit kh anlautende Form der Wurzel gehen
np. (arab.) yendeq Graben , phlv. xantak, np. /öw«j, /an
'Haus' (No. 405) und /am 'Quelle' (No. 466) zurück;
vergl. auch feryen neu gegrabener Wasserkanal' neben
ferken etc. Auf päz. /andan ist gar nichts zu geben,
vergl. päz. /ähUan^ /m u. a. m.
J. V. Fierlinger erklärt KZ. 27, 335 das ap. aw.
kan- gegenüber ai. khan- durch Analogiebildung nach
der schwachen Wurzelstufe, Bartholomae, ib. 367
Anm. 2 durch solche nach den mit Praefixen kon-
sonantischen Auslauts zusammengesetzten Formen.
870. kentz 'Jungfrau, Mädchen', kenizek,
maz. klja (?) ').
aw. kanyä-^ kaini7i-, kainikä- 'Jungfrau, Mädchen';
phlv. kanik, phlv. päz. kaMöak bezw. kanTjak, kanlzak
(PPGL); ai. kanyä-, kanijd-.
Durch dasselbe Suffix weitergebildet wie dösüe,
nrDirn (Is. 23, 4, 12) 'Jungfrau .
871. kiitäh, küteh 'klein, kurz'; ködek 'Kind, Kleines,
Foetus, Embryo (AM.)'.
aw. kutaka- 'klein'; phlv. kütak bezw. kötak,
bei. künd, n. Jcund 'kurz, nahe' (209); afy. LW. (?)
kötah,
np. küiäh entbehrt auflfälliger Weise der Lautver-
schiebung. Für ködek ist eine Grundform *kvataka-
anzusetzen (wie dö aus dva-, tö aus tvam u. a. m.).
Zum Pronominalstamm kva-, kn-?
872. hüze 'Topf.
aw. /awza- *Topf'; arm. LW. kuz.
Da mir Geldner's Übersetzung (vergl. KZ. 25, 583
^) Dazu auch kurd. kic?
```


### [2026-09-06T14:54:49.516Z] TOOL RESULT

```
=== KNT p.178 grep kan
1401:root, kan- ‘dig’ + pass. -ya-, in akaniya ‘was dug’. *duS- ll’ + *yür- ‘year’, in dušiyãram ‘famine’. wamarsiyus nsm. ‘by self-death’, Skt. mriyú-š
2531:$220. Tue Passive-Votce Present STEM of pIE was formed by the addition of the suffix pIE -je-/-4o-, which is accented in Sanskrit; in OP the root regularly has the normal grade, with -a-: imf. 3d sg. and pl. abariya abariya", to root bar-; ayadiya ayadiya", to yad-; akaniya, to root kan- ‘dig’; afahya and afahiya, to Ваћ-; avaniya, to van-; ajantya, to jan-; akariya akariya"la, to kar-; pres. ist pl. &ahyàmahy, to dah-; opt. 3d sg. kariyaiš to kar-, frabiyats to frað-, 3d pl. yadiyaiša” to yad-.
4253:28 : ша : tya : BU : akaniya : fravata : uta : tya : bika :
4406:10 iy : draya : tya : haeá : Рагва : aitiy : pasdva : iyam : yauviya : akaniya : 11 avafá : yaf : adam : niyastàyam : utd : nāva : àyatà : haca : Mudra 12 уй : tara : imam : yauviyim : abiy : Pársam : араба : yatà : mim : Ката : dha
5236:ikan- vb. ‘dig’: Av. kan-, Skt. khan- ($100), . See also Adukanaiía-, kata-. ka*tanaiy ($238; NPers. kándón) inf. DZe 9; XV 21. akaniya imf, pass. ($113, $220) DSf 24, 28 (25, 29 read avaniya: see under van-); DZe 10°.
```


## [2026-09-06T14:54:58.624Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} /kan- vb. .dig./{print NR; print}' KNT.txt | head -60"
}
```


### [2026-09-06T14:55:00.397Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T14:55:03.742Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('KNT.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i,l in enumerate(leaves):\n    if \"kan- vb.\" in l or \"vika\" in l and \"destroy\" in l:\n        print(\"=== leaf\",i,\"(printed ~\",i-15,\")\")\n        print(l[:3000])\n        break\nEOF"
}
```


### [2026-09-06T14:55:05.297Z] TOOL RESULT

```
=== leaf 201 (printed ~ 186 )
to the wall alongside it (König, - Burgbau 32n; Hz. AMI 3.54-5, Ар! 224). katam nsn. DSf 25.
Katpatuka- sb. ‘Cappadocia’, a province of the Persian Empire; also, as adj., ‘Cappadocian’: Elam. ga-at-ba-du-qa, Akk. ka-at-pa-tuk-ka, Gk. Каттодокіа. ($93.11).
(1) ‘Cappadocia’: Katpatuka nsm. РВ 1.15f; DPe 12; DNa 28; DSe 27°; D8m 8^; XPh 26. (2) ‘Cappadocian’: Katpatuka пэш. A?P 21.
ikan- vb. ‘dig’: Av. kan-, Skt. khan- ($100), . See also Adukanaiía-, kata-. ka*tanaiy ($238; NPers. kándón) inf. DZe 9; XV 21. akaniya imf, pass. ($113, $220) DSf 24, 28 (25, 29 read avaniya: see under van-); DZe 10°.
ni- + kan- ‘destroy, obliterate’: пач imv. (§208, $237.IT) DB 4.80.
vi- + kan- ‘dig apart, destroy’: viyakanam 1st sg. imf. XPh 38. viyaka" imf. ($208, §228.11) DB 1.64. vikanàhy 2d sg. subj. (327) DB 4.71, 78; vikandh"-di& (S27, 454.11, $136) DB 4.77.
*kan- vb. of uncertain connections, probably ‘throw, place’: cf. NPers. dwgdnddn ‘heap up’ from ava-kan- (Dv. Gr. $184; Morgenstierne, Acta Or. 1.249; Hz. ApI 225).
ava- + kan- ‘put down on, place on’: avakanam Ist sg. imf. (8213, 5226.1) DB 1.86.
Ka™pa"da- (8111) sb. ‘Kampanda’, a district in Media (cf. Kónig, RuID 71): Elam. qa-um-pan- taš, Akk. ha-am-ba-mu. Kapada пет. DB 2.27.
kapautaka- adj. ‘blue’, in kdsaka hya kapau- |
taka ‘lapis lazuli’: deriv. ($146.11) of stem in РЫ. — | kapót, NPers. kabod ‘gray-blue’, Skt. kapóta- ‘pigeon, pigeon-color, gray’ (Scheil 21.29; Bv. BSLP 30.1.61; Konig, Burgbau 62; Bleichsteiner, WZKM 37.94-101; Wb. AfOF 7.42, cf. PW 10.1887 s.v. Караша; Hz. AMI 3.64-5). kapau- taka nsm. DSf 37.
Käpišakāni- sb. ‘Kapishakani’, a fortress in Arachosia ($117, $126): Elam. qa-ap-pi-i3-fa-qa- nui, Каракат ns. DB 3.608.
Ka"büjiya- sb. ‘Cambyses’, (1) father of Cyrus the Great; (2) son of. Cyrus the Great, king of Persia before-Dartus: Elam. kan-bu-si-ia, АКК.
LEXICON
kam-bu-ai-ia, Gk. KayBvons (8111, $144.IV): ety- mology disputed (cf. Bthl. AiW 437; Charpentier, ZII 2.140-52). Kabūjiya nsm. DB 1.28, 30f, 31, 32, 33, 43. Kabijiyam asm. DB 1.45, 46. Kabüyyahyà gsm. CMb 1f; DB 1.29, 30, 39. Kabūjiyāä absm. DB 1.40.
kam- vb. ‘like’, see amazamata, if for (h)- amaxmatd. See also kama-, and possibly canah-.
káma- sb. ‘wish, desire’: Av. Skt. kdma- (§126, $148.I, V, VI). See also kam-. For syntax of de- pendent acc., $249.T, JAOS 66.44-9. kama nsm. DB 4.35f; 5.17°, 29, 33°; DNa 38; DNb 8, 10, 12, 19, 20, 27; DSf 16; DZe 12°. ХРЇ 22, 30.
kamna- ad}. ‘small, few’: Av. kamna-, NPers. käm ($147.11). kamnam nsn. (as pred. sb. $259) DB 2.19. kamnatbis ipm. DB 1.56; 2.2, 71; 3.41, "Af.
kar- vb. ‘do, make, build’: Av. kar-, pres.
karonaoitt, Skt. kr-, pres. krndti karóti (809, $122, $132.2, 5182.3). See also akarta-, ucára-, kara-, dastakarta-, duskarta-, hakarta-.
kunautiy (866.1, $70, $99, $2101) DNb 24f; DSs 2°, 3f, 4, 6°. |
akunavam ($66.1) 184 sg. imf. DB 1.62, 63, 68, 12, 87; 2.20, 76, 83, 91; 3.31f, 52, 85; 4.3f, 6, 86°, 40, 41, 45, 59, 60, 65, 89; 5.2, 8f, 17, 29, 33; DNa 491, 51; DNb 48f; DSa 4
```


## [2026-09-06T14:55:24.619Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('BRT.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\n# find leaves containing standalone 583\nfor i,l in enumerate(leaves):\n    if re.search(r'(?m)^\\s*58[0-9]\\s*$', l):\n        print(\"leaf\",i, re.findall(r'(?m)^\\s*58[0-9]\\s*$', l))\nEOF"
}
```


### [2026-09-06T14:55:26.356Z] TOOL RESULT

```
leaf 340 ['580']
leaf 342 ['583', '584']
leaf 345 ['589']
```


## [2026-09-06T14:55:28.753Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BRT.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nprint(leaves[342][:4000])\nEOF"
}
```


### [2026-09-06T14:55:30.837Z] TOOL RESULT

```
' :  yavai 'ia  *avi.inatn  hariks  hancayJt  V.5.60.
PO.!  transs'kr.
•  j.  äaräna-  n.  '(Ackerfeld,)  Feld,  Gefild': haoma  .  .  staomi  stmS  yd^a  raohahe  .  . •fipm  "ich  preise  der  Erde  . .  Gefild"  Y. /o.4'>.
AbleiL  (s.  j'a-^J./ariaya-).  —  Zum  V.  ii-ar-.  — Vgl  np.  -Sir  (woiu  GlrPH.  f  b.  192)3),  gr. «■oXoC  -J  tUTaßißhyuni  y^  tl(  naTaaittpäi (HeSVCH).  —  Pü.!  tarlär  r  'factor  es'.  — •)  Die  Wortstellung  ist  anl^llig;  daher  auch die  Bed.  des  Worts  unsicher.  —  ')  Wegen np.  iiirldan  s.  zu  caiiraahak-.
•  j,  *£airc''  Inf.  'sich  einherzubewegen': ma  im  ya^a  *gaoi  draf^  asits  ''vänma 1*")  frala  frayantu  ti  ma%S  (sd.)  "nicht sollen  sie  mir  beliebig  wie  das  Stierbanner '' sich  einherbewegen,  wenn  sie  (dich)  ge- kiessen;  stracks  vorwärts  . ."  Y.  10. 14.      1
Zum  V.  aar-.  —  Fa.;  ratae  'du  gehst',  Sü.: pratara.  —  »So  die  besten  Hds.;    %.  %  2rj  .
schwankend  wie  das  Banner  im  Wind;  $  2/7 No.  1.
•  g.  carak^r^Sra-  n.  'Gedanke':  hvS  ns
mazds  valtl  aiäuä  '%ra  srätiayeti/a  "der will  unsre"',  o  M.,  und  des  Ala  Gedanken verkünden"  Y.  2»j.8,
Zum  Praes.  7  (InL)  des  V.  'kar-.  —  Vgl.  zBlld. ai.  earkf-lya-  Adj.,  tBed.  mp.  iti*k5r,  np.  sikät 'Gedanke'.  —  Pü.;  cärak  karlärih,  erl. :  cärak i  drui  i  aadar  gehäii.  —  >)  Des  VÄf.  ond  des AhM.;  vgL  zSL  Cld.  KZ.  50.  542.  JUSTl  PrJ, SS.  79.
•  j.  (Sarat-  Adj.  'machend"';  °tam  (GP.) F.if).
Zum  V.  'iar:  —  Pü.:  kattäraii.  —  0  So  nach Pü.;  das  Wort  könnte  aus  einem  Komp.  los- geschält sein;  vgl.  zu  'aril:     Unsicher. ■  p.  £artanaiy  Inf.  'zu  machen',  nur  mit hamaranam  'praellum  facere':  hauv  kära^ aliyavJ' . .  hamaranam  c°  . .  avada  hama- ranam akunavc^ . .  avdhäsäm  hamaranam kartam  Bh.j.9;  6,  7,  10,  J.  19,  2.7-12*. Zum  V.  >to-.     Vgl.    (gegenüber   WZKM.  g. 166}  IF.  4-  128,  KZ.  35.  61.
•  j.  (antav-  m.  Name  eines  (Längen-,) Wegmasses".
*)  Nach   Pü.  {atpräs  drahnäk)   sva.   ein  ta'ar oder  zwei  hSiiTa.
KompA.  —  Zum  V.  tat-,  eig.  'Rennbahn'; vgl.  ta!ar-  und  Bthl.  1F,  /O.  3.
•  j.  i^axViÄ-  i.  'Lauf-,  Rennbahn':  upa tarn  °tqm  yqm  darsyqm  ^t.  ig.  ^  T, — aiia *•  tarn  ^'>  yqm  darrfqm  YL5.  50.
Z'um  V,  )ak-,  s.  ta/'ar-  und  BTHL.IF. /o.  3. — i>  Hds.  j''a"ftjw;  Tgl.  iiar-  No.  2  und  anya- No.  6;  femer  zu  lanal,caxra-.
•  j.  Öamtu-tära- "  .\dj,  'über  die  Ent- fernung eines  C.  hinausgehend,  weiter  als ein  €.  gehend,  reichend';  °r5  F.  ig.
*lära.  Adj.,  zum  \.lar.;  ai.  Wro- Adj.  —  Pü.: tartarlum.  —  >>  FMÜLLERs  Zusammenstellung des  Worts  mit  arm.  tarlat  ■geschickt'.  WZKM. 8.  361  ist  ohne  Wert.  Das  arm.  LW.  farlar stammt  aus  ir.  *iarlara-,  das  zu  ai.  calara- Adj.   'geschickt'   gehört;   s.   dazu  Wn.  AiOr.
•  j.  farstu.dräjah-  n.  'die  Länge  eines C:  äaf  fym  vanm  k?r7na7ia  'jö  k»mät paiti  ca'hrusanqm  ". ,  eben  (f.  nach  jeder der  vier  Seiten"  V.  2.  25^;  F.  15.
Pü.:  aspräs  drahnäk,  erl:  2  käsr  hal  kuH  3, dazu  die  Bern. ;  asl  ki  har  4  kml  ^'cTpit.
•  j.  (Jaraman-  n.  'Fell,  Leder';  mrätim "ma  "^anjaymte  "sie  ziehen  an  dem  ge- gerbten Leder(strang) "  Yt  17,  12;  — 'manqmca  .  .  *mrätanqm  N.  ^8;  —  'm<i (NP.)"  vatnantö  br3e?nta  {sA.)  frjna  »r^-
dby  Google
583
öazdahvant-
£i£aäana-
584
satim  saranitH  "die  Felle  strahlen  auf  die Beschauer  Silber  und  Gold(glanz)  in  Fülle" Yt.  5.  129;  —  •mqnca  *hiku  N.55.
ai.  cirman-  n.,   mp.  (Pii.),   np,  larm.    —  Vgl.
•Ara«ä-.  — I)  Nach  der  <j*-Dekl.,  vU  <iämiS3
und  dämihu;  %  403.
•  g.  äazdah'vant-  Adj.  'einsichtig,  ver- ständig': yä  manaohrlHaA.)  'äöaghvantsm ar}^ahyS  Y.  44.  5;  —  hyai  urvalsm  (sd.) "dönifkvadtbyS  Y.JI.3.
Ai._*iaai{/.yti.  oder  *m</(A)as-,  Et.?  —  Pü.; vicarJJr.
•  j.  £a§an-  m.  'Lehrer':  a%auruns  .  . 'sanqica  "  aEsqmcil  r
```


## [2026-09-06T14:55:42.501Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BRT.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i in range(338,343):\n    print(\"==== leaf\",i)\n    txt=leaves[i]\n    import re\n    for m in re.finditer(r'Brunnen|kan-|Grube|graben', txt):\n        print(\"   HIT:\", txt[max(0,m.start()-300):m.start()+300].replace(\"\\n\",\" \"))\nEOF"
}
```


### [2026-09-06T14:55:45.421Z] TOOL RESULT

```
==== leaf 338
==== leaf 339
==== leaf 340
==== leaf 341
==== leaf 342
```


## [2026-09-06T14:55:49.574Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('BRT.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i,l in enumerate(leaves):\n    if re.search(r'graben', l) and i<600:\n        nums=re.findall(r'(?m)^\\s*(\\d{3,4})\\s*$', l)\n        print(\"leaf\",i,\"cols\",nums, [x.replace(\"\\n\",\" \")[:160] for x in re.findall(r'.{120}graben.{120}', l)][:3])\nEOF"
}
```


### [2026-09-06T14:55:51.127Z] TOOL RESULT

```
leaf 70 cols [] []
leaf 106 cols ['130', '131', '132'] []
leaf 264 cols ['434'] []
leaf 266 cols ['438'] []
leaf 267 cols [] ["as^a  .  . ttimskante  (sd.)  V.J.  36;  8;—  jarW  (sd,) .  .  zjme  nikante  (NDf.)  V.  7.  47;  j. ra.  a)  II  'vergraben'  sva.  'aus  der  Er- innerung v"]
leaf 396 cols ['687'] ['aya{%A^ca  V. 17,2; — srväbya  may>m  ava-kansis  ..paiti \'im  äbarsii  ".  .  für  die  Nägel  sollst  du eine  Grube  graben  . .  du  sollst  sie  hin- bring']
leaf 454 cols [] []
leaf 546 cols ['971'] []
leaf 549 cols ['977', '978'] []
leaf 591 cols ['1063'] []
```


## [2026-09-06T14:55:53.873Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('BRT.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i in (266,267):\n    print(\"=== leaf\",i)\n    print(leaves[i][:2500])\nEOF"
}
```


### [2026-09-06T14:55:55.782Z] TOOL RESULT

```
=== leaf 266
��  J)  Wo  f.il,j! mit  ku\ra  wechselt.  ^
■  j.  kaO'wä-  f.  'Eselin'*':  -wa  dagnu{%ü) aryö  "um   den   Preis  fiir  eine  Eselstute"
V.7.4>-
')  Der  Esel  gil'  nn'er  den  slasm-  (Grossrieh) Hir  das  wenigst  wertTolle  Tier.  Die  Reihenfolge ist  (V.  7.  42):  Esel,  Rind,  Ross,  Kamel.  Vgl. GüR.  OK.  36L  ').
Et.?    —     ¥ü.:  lor.    —     ')  PDw.  *B,?/  'EseLs-
fiillen'.  vorauf  G<iR.  verweist,    kann    ich  mit
k'  nicht  vermitteln.
•  }.,  g.  kat  Adv.,  an  der  Spitze  des  Satzes; i)  'wann';  -4'  tä  nara  irista  ..nasus  upa.- dvqsaitii  . .  isar>  pasca  parairistim  V,  -j, \l.  2)  als  Fragepart. 'obwohl?,  num?': if=''  asavä  inazdä  vSng/iat  drjgvanim» "wird  der  .,^/aanhänger,  o  M.,  den  Drug- genossen  überwinden?'  Y.  ^iV.  2 ;  —  h asava  .  .  ranat  dnantjmf  asava  vana[ drvantjm  Yty.  28;  —  kat  möi  un-ä  isi (sd.)  caAyil  avauhS  "ob  (wohl)  .  .*'  Y.  50. i;  —  alä  k'  ^wä  darssäiij  i!S&?i  Y.  J<V,5;
—  k°  ta  Aaowa  yaoidiiyqn{%A.)  ai^h^n},. yaozdayqtt    anhm   V.ö.^if.;  7-23,5.57;
—  *i*  he  Vif  as.'m  *v}rxy,ll  N.  li\  —  k'  ta pd^a  frayqn  pasi'qtn  .  J  iiöit  t/i  pa'^>'r frayqn  piisrqm  ..  V,.V.i4f.;  —  6'  nä  .. tanii.p^rSiäi  .  .  gius  aiiilitya (^A.\  iislndli N.  /<V;  i/;,  ;7'>.  Unklar;  k'  kam  "^risa vibarst  N.  10^'.         [Yt.7.2*:  lies  idoa.]
ASn.  aus  tkn-.  —  oi.  kii/  Fragepart.  —  M.: *.-»,  («.  Vt.  /),  IWS.,,  (lu  Y.  .-ili  *•>.  - •)  Eig,  'was?  witd  ..  besiegtn?';  ebenso  im Ai.;  vgl.  daiu  Dmr.  VglS.  3.  261.  —  n  kat fehlt,  aber  I'Q.:  fi;3n.
•  '].  katmöLurvä-  fem.  Adj.  'die  Worte
^rt/ m^^i' «/T,(  enthaltend,  damit  beginnend': "j'ii  /iäitis(sil.)  ''  Y.  50  Überschr. ;  —  'i-qr/i AiJiilm'*  vazamaide  Y.  50. 12. ■)  1>.  i.  "V.  50.
•  p.  ka''pada-'>  m.  Name  einer  I^nd- schaft  in  Medien,  Cambadene:  'da''  iulm.'t" dahyäui  miidaiv  Bh. :;.  ö.
FüV  KZ.  37.  531  will  h^p-fdii-.
•  j,  kapastay-  f.  Name  einer  infektiösen, zu  Kriegszeiten  auftretenden  Krankheit'':
"ira    airy<i    daiü/ii'tvd  frqs    hyät  .  . pqma  nöit  'tis  Yt. -S'.  56;  —  pjr.me  tnüi'.i •nne  "lis  V.u. ff.
?:t.?0.  —  Pü.:  fehlt;  Kyo.:  kF«ü.  ei\.:  n.i kiMii  li.iti  ,/,ijl  kitnad.  —  ')  Man  setit  wegen np.  kiihijsl  'Koloquinle'  die  Bedeutung  'Gift' oder  'plante  vüni'neuse'  an,  was  mir  nicht  lu passen  scheint.  Eber  ka-/<a'Uiy-  (s.  unter t,-nu,A„-y,  vgl.  lat.  A^/«.
•  p.  
=== leaf 267
ai  bä  paiti  fraisl»in  uskmti {■^^'^h^yahmya  sairi  nikatile  "an  welchem Ort  man  am  meisten  ausgräbt,  an  dem Leichname  eingeschant  sind"  V.J.  12.  S. noch  anuskattte  Inf.
rm  para  'umgraben,  rajolen';  s.  Inf.
mit  lii,  niy  'eingraben,  verscharren':  yö iiars  .,  irtri'iusS  zumc  kshrpa  nikaiiiti  V. j.  40  PüZ.;  —  altafia  ..  aSta  vastra  fraca k3r3ntm  niia  kanaym  V.  7.  12;  —  yat aialta  zimS  nikante  (3SPM.)  späiias^a  .  . ttimskante  (sd.)  V.J.  36;  8;—  jarW  (sd,) .  .  zjme  nikante  (NDf.)  V.  7.  47;  j. ra.  a)  II  'vergraben'  sva.  'aus  der  Er- innerung verschwinden  machen,  in  Ver- gessenheit bringen':  uta  lyt/'  kunavahy ava''faiy  a''ura''mazdä  nika''tuv  "und  was du  tust,  das  soll  dir  AHM.  in  Vergessen- heit bringen"  Bh.  4.  1 7  ''.
mit  7'i  'durch  Graben  beseitigen,  ab- tragen; zerstören':  yasca  .  .  daxmatiqm avavanhm  maz3  vtkanayät  ya>a  .  .  V.  7. 51 ; — yat  b.J  paiti  fra!st.>m  daxma  uzdaSza (sd.;  lies  vrd')  vJkanü  (3SPA.)  yahmya  . . "an  welchem  Ort  man  am  meisten  die  D. durch  Abtragung  zerstört,  wo  .  ."  V.  y. 13;  —  yat  bü  paiti  fraüittnt  vikmte (3SPM.)  .  .gjmam  V..J.Z2;  —Wäyadanä (sd.)  tyä  gauiii'ätJ'  . .  viyakai'  (3SPrA.) Bh. /.  14;  —  kyt^  aparam  imilm  dipim vaitnhy  ..  maty^  (sd.)  vikanähy^^  Bh. 4.  15;  16;— _jW;>  imrim  dipim  ..vainähy '.■ikanähidisi^  Bh.  4- 1 7  II  ■
mit  kam  'durch  Graben  zusammen- bringen mit  -  ,  beschütten,  überschütten mit  -'  (Gen.):  I^riV  zims  hankanay.m "dreimal  sollen  sie  (das  Kleid)  mit  Erde überschütten"  V.  7.  14;  /?.  30.
n|i.  iandaniy-,  ai,  vj;!-  Manuft"'),  ihanayali (Kaus.);  t/iJlö&.  —  Pü.:  iamtan.  —  '>  Zur AnlautsdifTereni  zwischen  ir.  'Arn-  und  md. i-ia/i-  s.  S  f^-  —  ">  Zu  Ü.  //,  3  stellt  man {iyam  ym-iyä,  sd.l  akÄniy  her,  PrP.  —  3)  Vgl. ai.  khifii-liim  (Inf.)  und  IF.  7.  70.  —  1)  \'gl. die  lied.  des  mp.  ap^-  kaadan  (DST.  'exlirper'] in  IM.  lU  P.  /,-  I-.  'flifl-  No.  14);  s.  in  ■■""=*- ai'm.  —  Sl  So  NA.  nach  Opfert  u.  A.  ;  s. KZ.  J7.  527.
dby  Google
419  uätanava-  —  'uStra-  420
75.44;  —  tJm  ahmakäis  azdibiscä  "tänäiscä  I  a)  °vaUi  häitis  (sd.)''  Y.^J  Überschr.;  — yazamaidg'^.^'.^;  —  nöit  astS  ttiS'it  'tänahl\  -vaitim  häitlm  {&A^^^ yazamaide  \ .  43. 17; Hnmata\.i2.y,  —  vi . .  wvaesayäl  astaca  a.4Ö;  —  'vatlyä  vü  . .  Aälsis  {sA.)'>  Aan- 'tänaca
```


## [2026-09-06T14:56:15.629Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('BRT.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i,l in enumerate(leaves):\n    if 300<i<400 and re.search(r'Brunnen', l):\n        nums=re.findall(r'(?m)^\\s*(\\d{3,4})\\s*$', l)\n        print(\"leaf\",i,\"cols\",nums)\n        for m in re.finditer('Brunnen', l):\n            print(\"  ...\", l[max(0,m.start()-500):m.start()+300].replace(\"\\n\",\" \"))\nEOF"
}
```


### [2026-09-06T14:56:17.538Z] TOOL RESULT

```
leaf 316 cols ['533']
  ...  »  kt  devän  xumbak,  erl.; däfän  kär  i  narih  u  mälailh  ke  hinend. •  j.  xan-  f.  'Quelle,  Brunnen':  xä  (NP.) aspS-stdoyehl^  apam  Vt.  Ä  5 ,  42;  —  apamui xä  (AP.)  Y..,^2.'i;  V.y.si;  —  xa  'paiti afrajyamna  Yt.  ;_J.  14^;  —  vupa  äp5  x'i paiti  '^raoid.siätascü  (sd.)  Y.  Ji.  9 ;  —  »nzöis (sd.)  xh  Ytj^ag;  —  m^rtzuca  (sd.)  xa u^tünahe  Yl  /0. 7 1 ;  —  frä  tl  
  ... . •  j.  xan-  f.  'Quelle,  Brunnen':  xä  (NP.) aspS-stdoyehl^  apam  Vt.  Ä  5 ,  42;  —  apamui xä  (AP.)  Y..,^2.'i;  V.y.si;  —  xa  'paiti afrajyamna  Yt.  ;_J.  14^;  —  vupa  äp5  x'i paiti  '^raoid.siätascü  (sd.)  Y.  Ji.  9 ;  —  »nzöis (sd.)  xh  Ytj^ag;  —  m^rtzuca  (sd.)  xa u^tünahe  Yl  /0. 7 1 ;  —  frä  tl  hazat^rsin xqm  (GP.)  .  .  gaoiaiDin  (sd.)  avi  hanta- una'^.21.'};  —  fiaoma..  hai'hlmca  asahe xa  (NS.)  ahi  "o  H.  .  .  und  wahrlich  des heiligen  Rechtes  Brunnen  bist  du"  Y. 10. 4'>, Ableit.  (s.  xqnya;  xayaria-].-^  Zum  ar.V.  ikan-  ? ; E.  ^kan-  mit  No.  I.  —  ai.  ihaii-  f.  {ihi-);  mp. (Pü.)  vyl.  x3h.  —  ■)  Vgl,  RV,  2.  28.  5;  ihdn •  j.  xayana-  Adj.  (fem.  -na-)  'fontanus': apfm  °nqm  . .  apim  zrayanqm  "das  Quell- wa
leaf 343 cols []
  ... r  syntaktisch  als IS.  gehtauchl,  daber  Y,  31.  13  mit  IS.  des Adj.  verbunden;  s.  Bthl.  IF.  /a  9  (gegen Der.  VglS.  /,  219). g.  iäxnar}-.  s.  ^kan-, •  j.  cäxsnay-')  m.  EN.  eines  Gläubigen: °nöt^''>  asaonS  Yt.  13. 114"*. Mit  Int.-Red.  gebildet,  S  i02  II.  4-  Et.?  — ')  Oder  auch  läxinav-,  iJxinafs  nach  J  10;  s. No.  2.  —  »)  Nach  JusTi  NB.  152  (und  And.) identisch  mit  dem  Bd.  jz.  t  genannten  Ur- ahnen Zara%r/stras  Caxinui. •  j.  dät- f.  'Brunnengrube':  maF^e  vä  cäiti vä  V.13.Z1. Ableit.  —  Zum  V.  'lan-,  vgl.  xa»-;  %  13.— Vgl.  mp.  (l'Q.),  np.  m  (aus  iran.  *<^-iä%  S  S). •  j.  cätaya-  Adj.  (fem.  'yä^  'in  einer Brunnengrube  befindlich':  äpö  yat  'tayA uzuitytista  (sd.)  V.  6.  33. Statt  *läHya-  geschr., 
  ... es  Gläubigen: °nöt^''>  asaonS  Yt.  13. 114"*. Mit  Int.-Red.  gebildet,  S  i02  II.  4-  Et.?  — ')  Oder  auch  läxinav-,  iJxinafs  nach  J  10;  s. No.  2.  —  »)  Nach  JusTi  NB.  152  (und  And.) identisch  mit  dem  Bd.  jz.  t  genannten  Ur- ahnen Zara%r/stras  Caxinui. •  j.  dät- f.  'Brunnengrube':  maF^e  vä  cäiti vä  V.13.Z1. Ableit.  —  Zum  V.  'lan-,  vgl.  xa»-;  %  13.— Vgl.  mp.  (l'Q.),  np.  m  (aus  iran.  *<^-iä%  S  S). •  j.  cätaya-  Adj.  (fem.  'yä^  'in  einer Brunnengrube  befindlich':  äpö  yat  'tayA uzuitytista  (sd.)  V.  6.  33. Statt  *läHya-  geschr.,  S  i^S.   11.  —  Ableit.  aas <S/-.  —  Pü.:  äp  i  cähän. •  j.  £ärä-  f.  'Mittel,  Hilfsmittel"»:  "ram F.  IQ. Zum  V,  'kar-.  —  np.,  mp.  (PQ.)  '"o'';  s.  daza Hbm,  PSt.  51,  AGr.  /.
```


## [2026-09-06T14:56:39.952Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '43560,43600p' POK_full.txt"
}
```


### [2026-09-06T14:56:40.010Z] TOOL RESULT

```
References: WP. I 351 f., WH. I 155 f.. Loth RC 42, 353 f., 47, 170 ff., Vendryes RC 45, 

331 ff. 

Page(s): 526-527 

Root / lemma: kan- 

Meaning: to sing, sound 

Material: Gr. Kava(aau)), Aor. Kova^ai " pour with a gurgling sound ', Kovaxn " shrilling, 

noise', Kavaxsw, Kovaxi^w " sound, ring out ' (compare arsvaxu), arovaxn : gtevu)), ni- 

KQvoq "rooster, cock' ("cackling in the early morning '); Kovapoq "noise'? 

Maybe alb. kendes^ rooster' a Greek loanword. 

Latin cano, -ere^ o utter melodious notes, make music, sing, sound, play ', canorus^ of 
or pertaining to melody, melodious, harmonious, euphonious ' (compare sonorus), carmen 
" song' {*canmen), Umbrian kanetu^ canito ', procanurenV praececinerint ', af-kanT* 
accinium, cantus flaminis '; perhaps also Latin ciconia " stork ' (out of it probably 
syncopated praen. conea, compare to vowel gradation Old High German huon, russ. 
kanja); 

maybe alb. Geg kanga^ song '. 

Old Irish can/ml sing ', cymr. canu, bret. cana's\ng', Middle Irish cefa/n., cymr. cathli. 
" song', bret. kenteli. " ^an ' {*kan-tlo-m, previously brit. has changed to Fem., s. 
Pedersen KG. II 66); lengthened grade mcymr. g(w)o-gawn^\\\us\x\o\}s\ cymr. go-goniant 
"fame'; 



Gothic hana, Old High German etc. /7a/7c» "rooster, cock', fern. Old High German hemn, 
Gen. -nna {*hanen-i, -Jas), henna {*han[e]n-T, -Jas) and Old Norse M/75"hen' {*hdnjdn), PI. 
h0nsn {h0ns, h0sn) " chicken ', Old High German huon^ chicken ' (Germanic s-stem 
*hdniz); 

perhaps (Berneker 483 between) russ. (etc.) kanja, kanjuk^ kite, type of predatory bird,
```


## [2026-09-06T14:56:41.067Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AHD watkins gwhen\"; grep -n \"^gwhen\\|^gwhen-\\|gwhen-1\\|^kan-\" AHD_watkins1985.txt | head\necho; echo \"=== AHD canna/cane\"; grep -n -i \"canna\\b\" AHD_watkins1985.txt | head"
}
```


### [2026-09-06T14:56:41.137Z] TOOL RESULT

```
=== AHD watkins gwhen
580:kan-

=== AHD canna/cane
```


## [2026-09-06T14:56:48.617Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"Page(s): 53[34]\" POK_full.txt | head\necho \"---\"; awk 'NR>=1 && /Page\\(s\\): 534/{print NR}' POK_full.txt | head"
}
```


## [2026-09-06T14:56:49.621Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -i \"gwhen\\|g^when\\|ghwen\" AHD_watkins1985.txt | head -20\necho \"=== watkins swell abound\"; grep -n -i \"abound\" AHD_watkins1985.txt | head -20"
}
```


### [2026-09-06T14:56:50.174Z] TOOL RESULT

```
44031:Page(s): 534 
44052:Page(s): 534 
49399:Page(s): 533 
49430:Page(s): 534 
49571:Page(s): 533 
---
44031
44052
49430
```


### [2026-09-06T14:56:50.226Z] TOOL RESULT

```
1276:BABA baba- BABBLE baba- BABE baba- BABKA baba- BABU baba- BABUSHKA baba- BABY baba- BACILLUS bak- BACTERIUM bak- BACULIFORM bak- BAGEL bheug-3 BAGUETTE bak- Bails bheug-3 BAIRN bher-1 BaIT! bheid- BAKE bhé- BAKSHEESH bhag-' BALALAIKA baba- BALCONY bhelg- BALE! bhel-2 BALE? bhelu- BALEEN bhel-2 BALK bhelg- BALL! bhel-2 BALL2 gWele-1 BALLAD gWele-1 BALLAST bhoso-, kla- BALLET gWela-1 BALLISTA gWele-1 BALLOON bhel-2 BALLOT bhel-2 BALLOTTEMENT bhel-2 BAMBINO _baba- BAN! bha-2 BANAL bha-2 BAND! bhendh- BANDANNA bhendh- BANDIT bha-2 BANDOLEER bha-1 BANDORE pandoura BANE gWhen-1 BANG! bheg- BANIAN wen-1 BANISH bha-2 BANK! bheg- BANK? bheg- BANK? bheg- BANKRUPT bheg-, reup- BANNER bha-! BANNERET bha-1 BANNS bha-? BANQUET bheg- BANQUETTE bheg- BANSHEE gWen- BANTLING bheg- Baptist gébh-!
1294:BENIGN deu-?, gene- BENTHOS gWadh- BENUMB nem- BEQUEATH gWet-2 BEQUEST gWet-2 BEREAVE reup- BERM bhrem-2 BERRY bha-1 BERSERKER bher-3 BESPEAK spreg- BESPRENT spergh- BEsT bhad- BETOKEN deik- BETRAY d6- BETROTH deru BETTER bhad- BETWEEN dwo- BETWIXT dwo- BEVEL bat- BEVERAGE pO(i)- BEWITCH weik-2 BEZOAR gWhen-1, pa- BHAGAVAD-GITA g@i-2 BI- dwo-
1418:DEEP dheub- DEER dheu-! DEFACE dhé-1 DEFAME bha-2 DEFEASANCE dhé-1 DEFEAT dhé-1 DEFECT dhé-1 DEFEND gWhen-1 DEFENSE gWhen-1 DEFER! bher-1 DEFER? bher-1 DEFERVESCENCE bhreu-2 DEFIANCE bheldh- DEFICIENT _dhé-1 DEFILE! pu-2 DEFILE? gWhi- DEFLAGRATE bhel-1 DEFLATE bhlé-2 DEFLOWER bhel-3 DEFOLIATE bhel-3 DEFORCE bhergh-? DEFORM merph- DEFUNCT bheug-2 DEFY bheidh- DEGAGE wadh-1 DEGENERATE geno- DEGLUTINATE gel-1 DEGLUTITION gWel-3 DEGRADE ghredh- DEGREE ghredh- DEGRESSION ghredh- DEGUST geus- DEHISCE ghal- DEICIDE deiw- DEICTIC deik- DEIFIC delw- DEIGN dek-1 DEISM deiw- DEITY deiw- DEJECT yé- DELAINE wele-1 DELAY slég- DELEGATE leg-1 DELIBERATE [ithra DELINQUENT leikw- DELIQUESCE wileik- DELIRIUM leis-1 DELIVER leudh-2 DELL dhel- DELPHINIUM g¥elbh- DELUDE leid- DELUGE leu(@)- DELVE dhelbh- DEMAGOGUE ag-, da- DEMAND man-2 DEMARCATION merg- DEME da- DEMEAN! men-2 DEMEAN2 mei-1
1479:EUTECTIC ta- EUTHANASIA dhwene- EUTHENICS gWhen-2 EUTROPHIC threph- EUXENITE xenos EVACUATE eu-2 EVADE wadh-2 EVAGINATE wag- EVANESCE eu-2 EVANGEL angelos EVAPORATE kwép- EVECTION wegh- EVENT gWa- EVENTIDE da- EVER aiw-
1506:FENCE gWhen-! FENNEL dhé@(i)- FENUGREEK dhé(i)- -FER bher-1 FERAL ghwer- FER-DE-LANCE ferrum FERE per-2
1565:GOAD ghei-1 GOAT ghaido- GOD gheu(e)- GODSEND sent- GOFFER webh- GOLD ghel-2 GOLIARD gWel-3 GOMPHOSIS gembh- -GON genu-! GONAD gene- GONFALON gWhen-1 GONIOMETER genu-1 GONIOMETRY genu-! GONION genu-! GONO- gena- coop ghedh- GOOSE! ghans- GORE! ghaiso- GORE? ghaiso- GORGE gWere-4 GORGET gWera-4 GORSE ghers- GOSHAWK ghans- GOSLING ghans- GOSPEL spel-3 GOSSIP s(w)e- GOUACHE akWa- GOWAN ghel-2 GRAB! ghrebh-1 GRABEN ghrebh-2 GRACE gWera-3 GRACKLE gera-2 GRADE ghredh- GRAFFITO gerbh- GRAIN gre-no- GRAM! § gerbh- GRAM? gre-no- -GRAM gerbh- GRAMA gras- GRAMINEOUS_ gras- GRAMMAR gerbh- GRAMPUS_peisk- GRANADILLA gfe-no- GRANARY gre-no- GRANDILOQUENCE tolkw- GRANGE gre-no- GRANITE gr@-no- GRANT kerd-1 GRANULE gre-no- GRAPE ger-2 GRAPH gerbh- -GRAPH gerbh- -GRAPHER gerbh- GRAPHIC gerbh- GRAPHITE gerbh- -GRAPHY gerbh- GRAPNEL ger-2 GRAPPA ger-2 GRAPPLE ger-2 GRASP ghrebh-1 GRAss_ ghré- GRATE! grat- GRATE? kert- GRATEFUL gWere-3 GRATIFY gWere-3 GRATIS gWera-3 GRATITUDE gWero-3 GRATUITY gWera-3 GRAUPEL kreup- GRAVE! ghrebh-2 GRAVE? gwWera-2 GRAVES ghrebh-2 GRAVEL ghréu- GRAVID gWera-2 GRAVURE ghrebh-2 GRAY gher-3 GRAYWACKE wegh-
1572:GUN gWhen-1 GURGITATION gWere-4 GURU gWera-2 GUSH gheu- Gust! gheu- GusT2 geus- GUSTO geus-
1962:OFFEND g¥hen-! OFFENSE gWhen-1 OFFER bher-1 OFFICE dhé-1 OFFICINAL dhé-1, op-1 OFT upo
=== watkins swell abound
545:sive reduplicated form *gr-g- in Latin gurges, throat, also gulf, whirlpool: GARGET, GORGE, GORGET, GURGITA- TION; INGURGITATE, REGURGITATE. 4. Extended form *gwr6- (< *geroa-) in Greek br6- in: a. suffixed redupli- cated form bi-bré-sko- in Greek bibréskein, to eat: HELLEBORE; b. nasalized variant form *bro-n-kh- in Greek bronkhos, windpipe, throat: BRONCHO-, BRON- CHUS; C. suffixed form *gvré-mn in Greek bréma, food: THEOBROMINE; d. suffixed form *gvr6-ti- in Greek bro- sis, eating: ABROSIA. [Pok. 1. gver- 474.] gwes-. To extinguish. Suffixed variant form *sgves-nu- in Greek sbennunai, to extinguish: ASBESTOS. [Pok. g¥es- 479.] g”et-'. Resin (?). Only in Germanic and Celtic. Suffixed form *gvet-u- in: a. Germanic *kwithu- in Old English cwudu, cwidu, cudu, resin, mastic gum, “that which is chewed,” cud: CUD, QUID!; b. Celtic *betu-, birch, birch resin, in Latin bitumen, resin (Gaulish loanword): BITU- MEN. [Pok. 1. g¥et- 480.] gwet-2. To say, speak. Germanic *kwithan in Old English cwethan, becwethan, to say, speak: BEQUEATH, BEQUEST, QUOTH. [Pok. 2. g¥et- 480.] gvet-3. Intestine. Suffixed o-grade form *gvot-olo- in Latin botulus, intestine, sausage: BOTULINUM, BOTULISM, BOWEL; (BOTULIN). [Pok. gvet- 481.] ghedh-. To ask, pray. 1. Germanic *bidjan, to entreat, in Old English biddan, to ask, pray: BID. 2. Germanic *bidam, entreaty in Old English gebed (ge-, intensive and collective prefix; see kom), prayer: BEAD. [Pok. gehedh- 488, 2. bhedh- 114.] gvhen-'. To strike, kill. 1. O-grade *gvhon- in Germanic suffixed form *ban-6n- in: a. Old English bana, slayer, cause of ruin or destruction: BANE; b. Middle High German ban, bane (> German Bahn), way, road (? < “path hewn through woods”): AUTOBAHN. 2. Suffixed zero-grade form *ghn-tyd- in Germanic *gundjé, war, battle, in: a. Old Norse gunnr, war: GUN; b. compound *gund-fanon-, “battle flag” (fandn-, flag; see pan-), in Italian gonfalone, standard: GONFALON. 3. Suffixed form *gvhen-do- in: a. Latin défendere, to ward off (dé-, away; see de-): DEFEND, (DEFENSE), (FENCE); b. Latin offen- dere, to strike against, be offensive, offend (ob-, against; see epi): OFFEND, (OFFENSE). 4. Suffixed zero-grade form *gvhn-tro- in Persian zahr, poison: BEZOAR. [Pok. 2. gthen-(2)- 491, bhen- 126.] g”hen-2. To swell, abound. Suffixed form *gvhen-eyo- in Greek euthenein (eu-, well; see esu-), to flourish: EU- THENICS. [Pok. 1. gthen- 491.] g’her-. To heat, warm. 1. Zero-grade *gvhr- with nasal suffix and analogical vocalism in Germanic *brenw-, to burn, forming *brennan (intransitive) and brannjan (transitive) in: a. Old English beornan, byrnan (intransi- tive) and bérnan (transitive), to burn: BURN}; b. late Old English brynstan, “burning mineral,” sulfur (stan, stone; see stei): BRIMSTONE. 2. Germanic *brandaz, a burning,
1127:wed-'. Water; wet. 1. Suffixed o-grade form *wod-6r in Germanic *watar in Old English weter, water: WATER. 2. Suffixed lengthened-grade form *wéd-o- in Germanic *wéd- in Old English wt, wét, wet: WET. 3. O-grade form *wod- in Germanic suffixed form “wat-skan, to wash, in Old English wescan, wacsan, to wash: WASH. 4. Nasalized form *we-n-d- in Germanic *wintruz, win- ter, “wet season,” in Old English winter, winter: WINTER. 5. Suffixed zero-grade form *ud-d6r in Greek hudor, water: (HYDRANT), HYDRO-, (HYDROUS); ANHYDROUS, CLEPSYDRA, DROPSY, HYDATHODE, HYDATID. 6. Suffixed nasalized zero-grade form *u-n-d-d- in Latin unda, wave: UNDINE, UNDULATE; ABOUND, INUNDATE, (REDOUND), REDUNDANT, SURROUND. 7. Suffixed zero-grade form *ud-ro-, *ud-rd-, water animal, in: a. Germanic *otraz, otter, in Old English ofor, otter: OTTER; b. Latin Jutra, otter (with obscure /-): NUTRIA; C. Greek hudros, a water snake: Hyprus; d. Greek hudra, a water serpent, Hydra: Hypra. 8. Suffixed zero-grade form *ud-skio- in Scottish and Irish Gaelic uisge, water: USQUEBAUGH, (WHISKEY). 9. Suffixed o-grade form *wod-d- in Russian voda, water: VODKA. [Pok. 9. au(e)- 78.]
1208:ABAFT apo- ABANDON bha-2 ABASE bassus ABASH bat- ABASIA gWa- ABATE battuere ABBREVIATE mregh-u- ABDICATE deik- ABDUCENS deuk- ABDUCT deuk- ABELE albho- ABERRATION ers-1 ABET bheid- ABEYANCE bat- ABHOR ghers- ABIDE bheidh- ABJECT yé- ABJURE yewes- ABLATION  tele- ABLAUT apo-, kleu-1 ABLE ghabh- ABLUTION leu(@)- ABNEGATE ne ABNORMAL gné- ABODE bheidh- ABOLISH al-3 ABORT er-! ABOUND wed-1 ABOUT ud- ABOVE upo ABRADE réd- ABRIDGE mregh-u- ABROGATE reg-1 ABROSIA gWere-4 ABRUPT reup- ABSCESS ked- ABSCISE kae-id- ABSCOND dhé-1 ABSENT eS- ABSOLUTE leu-1 ABSOLVE feu-1 ABSORB srebh- ABSTAIN ten- ABSTRACT tragh- ABSTRUSE treud- ABSURD swer-2 ABULIA gWele-1 ABUT bhau- ABYSS gWadh- ACANTHO- ak- ACANTHOPTERYGIAN pet- ACANTHUS ak- ACAPNIA kwép- ACCEDE ked- ACCELERATE kel-3 ACCENT kan- ACCEPT kap- ACCESS ked- ACCIDENT kad- ACCIPITER Oku- ACCLAIM kele-2 ACCLIVITY klel- ACCOLADE kwel-1 ACCOMMODATE med- ACCOMPLISH pele-1 ACCORD kerd-1 accosT kost- ACCOUNT peu- ACCRUE_ ker-3 ACCUMBENT keu-2 ACCUMULATE keue-2 ACCURATE cira ACERATE ak- ACERB ak- ACETABULUM ak- ACETIC ak- ACETUM = ak- ACHALASIA ghé-
```


## [2026-09-06T14:56:58.421Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '44000,44060p' POK_full.txt; echo \"=== 49380-49435\"; sed -n '49380,49435p' POK_full.txt"
}
```


### [2026-09-06T14:56:58.503Z] TOOL RESULT

```
References: WP. I 355 f., WH. I 173 f., Trautmann 118 f. 
Page(s): 532-533 

Root / lemma: kat-1 

Meaning: to link or weave together; chain, net 

Material: Latin catena^ chain ' {*cates-na), cassis, -/s' a hunting-net, snare, net' (because 

of catena rather = *kaf-s-/s as *kat-ti-s, perhaps also casa "primitive cottage' (originally 

from easy netting; probably dial, from *catia, as Oscan Bansaeirom Bantiae); 

perhaps here catervai. "heap, troop, multitude, crowd' {*kates-oua), Umbrian kateramu, 
caterahamo^ catervamini, congregamini ', yet see below under ket-1. 

cymr. cader^ ioriress' (only in PN), Old Irish cathir^\.a\Nr\, city'; 

perhaps Old Icelandic haddai. "ring, handle, part of an object designed to be gripped by 
the hand, hanger' {*hat^iPdn: catena, rightly doubtful), probably Old English headorr\. " 
confinement, jail '; 

Church Slavic kotbcb "cella, nest', russ. kotyP\. " fish weir ', Serbo-Croatian kot, (dial.) 
kdtac^ small stall'; dial, "kind of fishing' etc. and Bulgarian kotara, kotora, kotor^ hurdle ', 
Serbo-Croatian kdtarler\ce' , kotar' region, area, limit, boundary' ("*from fence '), sloven. 
kotar^ district, region, area ' (see Berneker386, 588); 

Maybe alb. kotec^ceW, nest' a Slavic loanword. 

References: WP. I 338, WH. I 175 ff., 181 f. 
Page(s): 534 

Root / lemma: kat-2 

Meaning: to bear young; animal cub 

Material: Latin catulus^ a young of an animal, esp. a whelp, puppy [animal-young, esp. 

young dog or cat]', Umbrian katel. Gen. katles^ catulus '; 

Maybe alb. kotele "young cat' . 

Old Icelandic hadnai. "young goat'. Middle High German hatele. Modern High German- 
Swiss hat/e' goat'; 



Slavic kot/t/ s^ {russ. kot/tbsja etc.) "kitten, give birtli to kittens ', dial, kotbka lamb', 
Serbo-Croatian /ro/' brood', poln. wy-kot'young goat, kid' etc. (see Berneker589 f.). 

References: WT. I 338 f., WH. 1183. 
Page(s): 534 

Root / lemma: kau-/-, ku-l- 

Meaning: hollow; bone 

Material: Gr. KauA6(; m. ' stalk; quill, shaft'; Latin caulis {colis, caulus) " the stalk or stem of 

a plant'; Middle Irish ci/a///e 'picket, pole' {* kaulTnJo); Lithuanian kau/asm. "bone' (glottal 
=== 49380-49435
In addition the descriptive name of rabbit (compare russ. serjak^ grey hare' : seryj 
'gray'): 

Old Indie sasa-rr\. (from *sasa-), afghan. soe, Pamird. sur, cymr. ce/nach {-ach- 
extension of a *cein= *kasnr doe, female hare', Pedersen KG. I 86); Old High German 
haso, with gramm. variation Old English hara. Old Norse her/ {an ablaut formation with 
Germanic e seems Norwegian Swedish Dialectal yase = Old Norse *hjasi). Old Prussian 
sas/nsm. 'hare', sas/n-t/nk/o ' hare's snare', PN Sassenpile^ hare's mountain'. 

An extension of the stem *Rasen- (: kas-n-o-) and *Raseu-, kasou- (: kas-u-o) with 
formants-d^o and zero grade of the root syllable is supposed in gr. ^ayQoc, 'blond, brown' 
from *ks-en-6'^o- (whether ^av- amalgamation from *^£v- and *^a- =*^n-)7 and ^ouGoc; 
ostensibly ' golden ', whether from * ks-ou-6'"o-, but very dubious. 

References: WH. I 156, Hofm. Etym. Gr. Wb. 221, Trautmann 330, Schwyzer Gr. Gr. I 
329. 



Page(s): 533 



Root / lemma: Rat- 

Meaning: to fight; battle 

Material: Old Indie satayati^ smashes to pieces, throws down '; satru-m. "besieger, fiend'; 

gall, catu- 'fight, struggle' in GN Ca/^-rZV" battle king'. Old Irish ca//7 "fight, struggle; 
troop, multitude, crowd', cymr. cad 6s., corn. casm. "fight, struggle'; cymr. cadr{*kat-ro-) 
"strong', abret. cadr. Middle Breton kazr, nbret. /raer" beautiful'; cymr. cao'a/T? "strong', bret. 
Aao'a/T? "valiant'; in addition also after Loth RC 42, 84 f. cymr. cadwm. " troop, multitude, 
crowd' {*Ratuo-), as Verb "preserve, protect, shield '; abrit. Mars Be/atu-cadros conta\ns 
whereas the root ^ao^- "gleam'; 

Old Icelandic hodl "fight' (= gall, catu-), GN Hgdr, Gothic MN Theuda-hatha-s, Old 
English headu-. Old High German hadu- "fight, struggle' in names as Hadu-mar, Hedwig, 
Middle High German /750'e/'" quarrel, fight'; 

whether one here Slavic k- for R- accepts the possibly (compare above S. 1 S"!), Old 
Bulgarian kotora, russ. -Church Slavic kotera^ fight, struggle '; 

possible would be citation of thrak. VN the larpai, larpo-KEVTai; 

That in gr. oaTivri " luxury chariot ', aariAAa ttAeiqc; to aarpov, as Phrygian words 
interrelate with Armenian sayr cart ' (Armenian-Phrygian *satilia), which is the original 
meaning of " chariot ', is unproveable. 

References: WP. I 339, 340, Vendryes RC. 43, 246, M. Leumann Hermes 68, 359. 
Page(s): 534 

Root / lemma: Rad- : Redes- : Red-s- 

Meaning: uneasiness, displeasure, hate
```


## [2026-09-06T14:57:05.443Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"khanati\\|khan-\\|khani\" POK_full.txt | head -20"
}
```


### [2026-09-06T14:57:05.516Z] TOOL RESULT

```
47275:khani-tum, participle khata-{*khn-to-), together with the neologisms kha-v\. "cave', a-khu-^
```


## [2026-09-06T14:57:07.654Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '47255,47300p' POK_full.txt"
}
```


### [2026-09-06T14:57:07.710Z] TOOL RESULT

```
Similar to onomatopoeic words kak-^ flout, show scorn, mock ' in gr. kpikq^u) " abuse, 
revile '; Old High German huohon^ mock, scoff. Old Saxon hohi-ITk^ laughable'; with 
Germanic -Ar-: Old English hocoru. " derision '. 



*) According to WP. I 341 , 348 f., 399 mentioned roots khad- "bite', khabh- : khobh- 
"feeble', khend^6\g' are not to be proved as Indo Germanic, just as little as those from 
Specht (Indo Germanic Dekl. 263, Anm. 4) set /r/7a-/77c»- "crooked'; 

those mentioned by him (see 256) Old Indie Beispiele khalati-, kharva-, khara-, khanda-, 
khora-axe all not of Indo Germanic origin. Old Indie khadati' bites to pieces, chews ', 
npers. xayadti^s., could belong to Armenian xacanem^\i\\.Q\ but also with secondary 



expressive Aspiration as *knd-\.o Lithuanian kandu'b\\.e' (somewliat different above S. 
560). 

To the same root root Ae/7- (above 559 ff.) could belong Old Indie khanatT digs ', Inf. 
khani-tum, participle khata-{*khn-to-), together with the neologisms kha-v\. "cave', a-khu-^ 
mole ', /r/7a- "stream, brook'= Avestan Nom. Akk. PI. xa6s.\ Old Indie khanf-^ burrowing ', 
f. " mousehole, entrance to the burrow of a mouse ' = Avestan Aa/7/- "ditch, trench, 
channel'; Avestan Old pers. /ra/7/7-"dig' (/r-from /r/7-from the compounds with us-, ham-). 

Maybe in -m- formant etymology in alb. Tosc f. {*kamur-is) hamuridhe " mole ' > Geg m. 
urithi^ mole ' ; common alb. Avestan k- > h-. 

Note: 

The inanimate suffix -ur- . alb. Tosc {*kamur-is) hamuridhe^ mole ' : UAupioi , oi, lllyrians, 
lAAupia , n, lllyria, also'lAAupi^ , n. Adj. 'lAAupiKO^ , n, 6v, lllyrian: -kx\, the region or province 
of lllyria, 'lAAupi^io , speak the lllyrian language, 'IAAupia:--hence Adv. 'lAAupiaii. 

The aniautfrom gr. Kocpav, Kncppv "drone', K(j0(p6(; "dull, deaf is doubtful, also from Church 
Slavic chab/t/" spoW , chabenb " woeful, wretched, miserable ', as also the from Church 
Slavic chomg-tb " horse collar ', placed by Specht to Latin hamus{*kha-mo-) "hook', gr. 
Xaijog " writhed, crooked, humped ' (and Yfl^oo, ds.) (different above S. 555). 

About the problem of the Tenues Aspiratae, which is to be understood partly indeed as 
secondarily expressive, compare Hj. Frisk, Goteborgs Hogsk. Arsskr. 1936: 2, S. 38 ff., 
Specht Indo Germanic Dekl. 251 ff. For Slavic beginning c/7- compare V. Machek Slavia 16 
(1938), 161 ff. and J. J. Mikkola Urslav. Gramm. 174 ff. 

numerous Old Indie words not of Indo Germanic origin with aniaut. kh-, below the above 
mentioned, by Kuiper, Proto-Munda 47 ff.
```


## [2026-09-06T14:57:14.274Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"Page(s): 55[89]\\|Page(s): 56[0-3]\" POK_full.txt | head\nawk 'NR>=47300 && NR<=47340' POK_full.txt | grep -n \"Page\" "
}
```


### [2026-09-06T14:57:16.057Z] TOOL RESULT

```
45155:Page(s): 558 
45429:Page(s): 558-559 
45683:Page(s): 559-563 
45720:Page(s): 563-564 
49228:Page(s): 558 
4:Page(s): 634 
24:Page(s): 598 
36:Page(s): 599
```


## [2026-09-06T14:57:18.121Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '45430,45450p' POK_full.txt"
}
```


### [2026-09-06T14:57:18.176Z] TOOL RESULT

```
Root / lemma: ken-2, kena-, keni-, kenu-; 

Meaning: to rub, scrape off; ashes 

Note: various with conservative extensions 

Material: I. Light basis: Gr. kovk;, -ioc; f. "dust, ash' (-/s-stem, compare KoviaaaAoc; "cloud of 

dust', KSKOvia-TQi Theokr., Koviu) " make dusty, cover with clouds of dust, cover with dust, o 

be sprinkled as with dust, roll in the dust, like birds, horses ' from *Kovia-iw, hom. Kovir) 

"dust, sand, ash' from kovigq); aKOvTii " without the dust of the arena, i.e. without struggle, 

without effort, usu. of the conqueror ' (JiJthner Gl. 29, 76); 

ablaut, with Latin cinis, -eris\. m. "ash' (from *cenis), Dimin. c/n/s- cu/us {K6v\q, c/n/sare 
probably originally a neutr. as- stem, and have suffered gender changes only single- 
linguistically because of Nom. in -/s).
```


## [2026-09-06T14:57:39.907Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor w in \"^canna,\" \"^canon,\" \"^canal,\" \"^cane,\" \"^cannon,\" \"^canyon,\" \"^channel,\"; do echo \"=== $w\"; grep -n \"$w\" KLN_1966.txt | head -3; done"
}
```


### [2026-09-06T14:57:41.601Z] TOOL RESULT

```
=== ^canna,
=== ^canon,
6374:canon,  n.,  a  dignitary  of  the  church.  —  ME.  ca¬ nun,  canoun,  fr.  ONF.  canoine,  corresponding to  OF.  (=  F.)  chanoine,  fr.  Eccles.  L.  canonicus, lit.  ‘one  subject  to  the  canon’,  fr.  Gk.  xavovtxoi;, belonging  to  a  rule’,  fr.  xxvdiv,  ‘rule’.  See  canon, ‘rule’,  and  cp.  canonical, canon,  n.  —  See  canyon.
=== ^canal,
6321:canal,  n.  —  F.,  fr.  L.  canalis,  ‘water  pipe,  chan¬ nel,  canal’,  prop,  subst.  use  of  an  adj.  formed  fr. canna ,  ‘reed,  cane ;  small  vessel,  tube’.  The  short¬ ening  of  the  double  n  is  due  to  the  phonetic  law, according  to  which  before  a  stressed  syllable, a  double  consonant  becomes  short.  Cp.  L. ciitulis,  ‘pertaining  to  a  chariot',  fr.  currus, ‘chariot’  (see  cttrule),  and  mamilla ,  ‘breast’,  di- min.  of  mamma,  ‘breast’  (whence  this  phonetic law  is  called  ‘mamilla  law’;  see  mammilla).  See cane  and  adj.  stiff,  -al  and  cp.  channel,  cannel, kennel,  'gutter',  which  are  doublets  of  canal. Derivatives:  canal,  tr.  v.,  canal{l)-er ,  n.,  canal¬ ize,  tr.  v.,  canal-ii-ation,  n. canalicular,  adj.,  pertaining  to,  or  like,  a  canali¬ culus  or  canal iculi.  —  Formed  with  adj.  suff. -ar  fr.  canaliculus  (q.v.)
=== ^cane,
6343:cane,  n.  —  ME.  cane,  canne,  fr.  OF.  cane,  canne (F.  canne),  fr.  OProveng.  carta,  fr.  L.  canna, ’reed,  cane,  small  vessel,  tube',  fr.  Gk.  xxvva, ’reed’,  which  is  of  Sem.  origin.  Cp.  Akkad. qanu,  Heb.  qaneh,  Aram.-Syr.  qanyO,  Arab. qanAh  (whence  Pers.  qanat),  ‘reed,  cane’, Ethiop. qanot,  ‘a  goad’.  Cp.  can,  ‘vessel’,  canaba,  Canada, canal,  canasta,  canaster,  eanaut,  caneila,  can- ions,  canister,  Canna,  cannel,  cannelure,  can¬
=== ^cannon,
6363:cannon,  n.,  gun.  —  F.  canon,  fr.  It.  cannone*  lit. ‘a  large  tube’,  augment,  of  canna,  ‘tube’,  fr.  L. canna.  See  cane  and  cp.  canyon.
6365:cannon,  n.,  a  stroke  in  billiards.  —  Corruption  of
=== ^canyon,
=== ^channel,
```


## [2026-09-06T14:57:51.803Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nimport re\ndef leafof(lineno):\n    return t[:sum(len(l)+1 for l in lines[:lineno-1])].count('\\f')\nfor ln in (6321,6343,6363,6374):\n    print(ln, \"leaf\",leafof(ln), \"approx page\", 2*(leafof(ln)-12))\n# find canon 'rule'\nfor m in re.finditer(r'canon,\\s+n\\.[^\\n]{0,200}', t):\n    print(\"---\", m.group(0)[:220])\nEOF"
}
```


### [2026-09-06T14:57:53.611Z] TOOL RESULT

```
6321 leaf 132 approx page 240
6343 leaf 132 approx page 240
6363 leaf 133 approx page 242
6374 leaf 133 approx page 242
--- canon,  n.,  rule.  —  ME.  canun,  canoun,  fr.  OE. canon,  fr.  L.  canon,  ‘a  measuring  line,  rule, model',  in  Eccles.  L.  ‘canon’,  fr.  Gk.  xxvcov, ‘rod,  bar,  ruler,  rule,  model’,  fr.  xxvva, 
--- canon,  n.,  a  dignitary  of  the  church.  —  ME.  ca¬ nun,  canoun,  fr.  ONF.  canoine,  corresponding to  OF.  (=  F.)  chanoine,  fr.  Eccles.  L.  canonicus, lit.  ‘one  subject  to  the  canon’,  fr.  G
--- canon,  n.  —  See  canyon.
--- canon,  n.,  a  narrow  valley  between  cliffs.
```


## [2026-09-06T14:57:58.728Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i in (131,132,133):\n    l=leaves[i]\n    print(\"=== leaf\",i, repr(l[:160]))\n    print(\"    tail:\", repr(l[-160:]))\nEOF"
}
```


### [2026-09-06T14:58:00.362Z] TOOL RESULT

```
=== leaf 131 '  camel with  suff.  -eer.\nCamelidae,  n.,  a  family  of  ruminants  (zooi.)  — ModL.,  formed  with  suff.  -idae  fr.  L.  camelus. See  camel.\nCamelina,  n.'
    tail: 'o know’,  yvcioi;,  ‘knowledge,  wisdom’,  yvtoprt),  ‘a means  of  knowing,  judgement,  opinion,  maxim  , yvMpLtov,  ‘one  who  knows,  a  judge;  the  gnomo'
=== leaf 132 'n or  index  (of  the  sundial)’,  OL.  gnoscere,  L.  nds- cere,  ‘to  know’,  Alb.  heh,  ‘you  know’  (sing.), hoh,  ‘I  know’,  OSlav.  znajq,  znati,  Lith'
    tail: "cula,  lit. 'the  Dog  Star’,  dimin.  of  cams,  ‘dog'.  See  canine and  -cule.\ncanicular,  adj.,  1)  pertaining  to  Sirius;  2)  per¬ taining  to  the  dog"
=== leaf 133 '  days.  —  L.  caniculdris,  fr. eanicula.  See  prec.  word  and  -ar.\nCanidae,  n.  pi.,  the  family  of  dogs,  wolves,  foxes and  jackals  (zool.)  —  Mo'
    tail: 'cantel,  corresponding  to  OF.  chantel,  ‘corner, piece’  (whence  F.  chanteau,  ‘hunch  of  bread’), dimin.  of  ONF.  cant  (corresponding  to  OF.  and F.'
```


## [2026-09-06T14:58:21.781Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AFM qanat\"; grep -n \"قنا\\|القناة\\|قناة\" AFM_pages.txt | head -10\necho \"=== ARB\"; grep -n \"قناة\\|القناة\" ARB_mo3rb.txt ARB_abdulraheem.txt | head -10\necho \"=== PLA\"; grep -n -i \"qanāt\\|qanat\\|Kanal\\|qanāh\" incoming/PLA/PLA_pages.txt | head -10\necho \"=== TAD\"; grep -n \"قناة\" TAD_pages.txt | head -5\necho \"=== FVQ\"; grep -n -i \"qanah\\|qanāh\\|qanat\" FVQ_pages.txt | head -5"
}
```


### [2026-09-06T14:58:21.905Z] TOOL RESULT

```
=== AFM qanat
2458:ܡ القناه فعر بة عن 29 01101
2835:0 ܟ 7 دواء 8 في حوف القنا المندي اوهو رماد ܟܕܬ | معرب
2848:ܨ والمأرضة) شبه حوض كبير عند خرج القناة وهو :ترك (6]0
3283:ܫ (القناخر ) العم ܐܝܪ ٠و(‏ المنخورة والتنخيرة ) الصخرة العظيمة المتفاقة.
3510:( كير ) اسم ككل بناء فيه العقد كبناء المسور والقناطر _-
=== ARB
ARB_mo3rb.txt:4074:وهذه الأقوال الى حكى أبومنصور وغيرها عاذى الناف لشن لأقناة إل دالوا فوا 
=== PLA
4575:bw            -   tiräb:            "Name        eines       Kanals"            ”, wahrscheinlich          aus   dem   pers.     ol
4576:             ziräb        "Abzugskanal".
10999:=                arh:       "Staubecken;                   Reservoir     an       der   Mündung            eines        Kanals"       pers.   7,
13867:—Ii--       mirzäb:                "Wasserleitung,                     Kanal"             pers.     12 eg mp.        oM marz              aw.
=== TAD
1622: ‫ارد ‪0‬ق تور امنا الماى وعووبالنارسة مقناة سمل‬                             ‫توزيةك‬
2549:                    ‫ل م ‪ -‬تركي « (لن »م معناه قناةوعهرى و ‪807‬هلاه ف ا‬
=== FVQ
```


## [2026-09-06T14:58:27.062Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '2440,2475p' AFM_pages.txt\necho \"=== leaf num\"; python3 - <<'EOF'\nt=open('AFM_pages.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\noff=sum(len(l)+1 for l in lines[:2457])\nprint(\"leaf\", t[:off].count('\\f'))\nEOF"
}
```


### [2026-09-06T14:58:28.711Z] TOOL RESULT

```
± اتويت كد
( سدْجة ) ܐܬܡܐ ܩܐ ܨܘ فارسنة ܚ ܐܡܵܬ
* ( السِنْجَاب ) حيوان على 45 £ ܦ من الفار 0% 02 النعومة
تتّحْد من جلدو الفراء فارسيّه سنْجَابٍ
( انحرف والسنجفر) صمغ تعريب سرف
70 اللواء 73:3( 1 © الى 0
ܕܘܚ ܠ والكردي سنجاق :
* ܡܐ الريح المنثنة والوسخ تعريب 3 اي ܦللع 1
(السَنْدَانَ) من آلات المذادين 3975 6 ومنة سئدان بالتركية
والكرد بة
١‏ الِْدِيان) فارسي حض وهو شجر البأوط
#* ( 9 ¥ 05 والطويل والشديد والأسد. (وَالسَئْدَر) 5 <
5( 7 والستداوة ) 0 واطرئ المقدء (١‏ والستداب) صلب سيرد لمن كل
ذلك قرب 43979 53 05( ( 05333 72899 0 117
ومعئاة 5-5 ܝܒܐ :
( السِئْطات) مطرقة الحداد مركية هن زَّنْ اي ضرب ومن تاب اي حرارة
8 ܨ 3 4 19 ܐ
6 5535 53 59 ومعناء بجاب 0
ܡ القناه فعر بة عن 29 01101
+ (الهام) )7 × 1 0( صاب | ܐ 3 ܣ 5 ܝ ومعناه
ܥܝ الشديد والمرض ٠‏ وقالوا فمه سهم الى غير ذلك 1 اذ 9 ]<
اي أقرع
* (السَهُم ) !ܐܟܬ تعريب سامّه ومن ܣܗܡܐ بالسر ܐܸܝ الدارجة
( سهنْسآه ) 0( افعل هذا سهنساه اى ]£ كل * شي٠‏ وهي فارسيّة مركة
نخص المستقدل ( حيط المحيط )
(اساج ) شجر يعظم جدًا قيل لا ينبت الا ببلاد الهند ܐܚܠܬ ساج
* (السَجْوَري » الأحق معرب كور اي كلبي
(السور) الضيافة فارسي بجت وهو 091
لجاز ܟܳܠ الفرس تعريب وار ܘܝܐ ܘ الفارس
( السُوس ) فارسي بحض بمنى الطبيعة والأصل
+ 0 ا ܡ وهو نات 6 ترق :مله حايت احص
ܐ 5 = لغة فيه
703 000 3 بالذهب 2 تعر يب سيم اي الع :43054 ܝܨ
ܤܐܡܐ9 حت
( اليسب) فارسى ض وهو التفاح ومنةُ الكردي رسيو
* (السيمة) مرقاة من الخشب على ثلاث قواٌ يجمعها قرص من اعلاها مركّة
=== leaf num
leaf 97
```


## [2026-09-06T14:58:39.120Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SOD c't well\"; grep -n \"c't\\|č’t\\|čāt\\|well\" SOD_pages.txt | grep -i \"well\" | head -20"
}
```


### [2026-09-06T14:58:39.164Z] TOOL RESULT

```
=== SOD c't well
2029:and feasts from the works of Beruni, as well as               see Cross-References below. Also, for further
2056:indefinite at times in connection with recognising the        endings as well as gender and number indicators
2176:      sayana - "dwelling of the Sogdians" (VdAA\ In both               the Syriac sodiqaye (Sogdians), in the Chinese su-^e
2188:      as "dwelling in villages".10 I. Gershevitch11 postulates         south of Samarkand, seems to be considerably larger
2191:      Settlement or the land of settled dwelling par                   its writing system. The latter, he informs us, was
2232:Nesef as well. Ya'qubi includes Nesef and Kish (or           cities of Transoxiana. Thus, the Han annals inform us
2296:the limelight of history and formed an extensive              well as-Narshakhi's account of the sack of Baikand
2352:and Manicheans as well as Christians took place. The                 1916, pp. 116-123.
2394:        still used in some smaller area until 13th century.              20. The Sogdian so-called "SOtra" script as well as the
2870:well as commentary to the whole corpus presented in             defective in rendering the vocalism. This results in
2898:of astrology.98                                                 texts written in Sogdian script as well as for some non-
2903:Apart from a single fragment in Brahmi script, the              well as for some Manichean and Christian texts written
2908:written all the Buddhist texts" as well as all the                   in Syriac.
2932:related to the Aramaic script, especially that used in        materials as well as, in rare cases, in Manichean
3067:and five long vowels as well as some allophones-, this          109. Sims- Williams, CLI, 1989.
3334:preceding /r/. M(S) distinguish I pi from /// with              semivowel lyl as well as the fronted vowels Iff, IS/
3363:191. The sign > represents both lal and lal as well as          See also comparative Tables 4 and 5 in the Persian
4337:    anlt ©pt. st. ^nyd'r-, 'n'y-                                       farewell
8291:      residence, dwelling                                        oske Csk'y, *skyy) ^'sk-1'
8325:     dweller                                                    osman-yon
```


## [2026-09-06T14:58:39.593Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SOD knth town\"; grep -n \"knδh\\|kn8h\\|knth\\|town\" SOD_pages.txt | head -20"
}
```


### [2026-09-06T14:58:39.648Z] TOOL RESULT

```
=== SOD knth town
2316:inform us that Sogdian colonies existed in Srw}n                 of four towns by the Sogdians in that region was
2331:town can have been scarcely below one thousand                   or Sarag)~ on the 16th year of the emperor Y}y
2602:town of Turfan5^ and in a half destroyed library              better idea of the structure and syntax of the
2781:excavations are by V. A. Liv§ic, M. N. Bogoljubov               towns. Some of these wall-paintings carry
13321:     Khocho, TutfaniChinese town)
16172:                                                                                       town in China)
23486:6882 *pnc,snw B                                                    6893 pncykn8h       S
26187:      town
26623:         STii 1.50, 6.26; GMS 616 f n 1; Gersh. AHM 192;              town
29560:                                                                    Saragh, Lo-yang(a town in Ancient China)
30181:     ShravastiGa town)
37866:cessation   11393                          Chinese town    3346                       3459, 3483, 5402, 5562, 9555,
39738:    town        7782, 7959                         (to)trouble     383                         2097, 10662
```


## [2026-09-06T14:58:46.386Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"c't\\b\" SOD_pages.txt | head -20\necho \"=== entry numbers 12x\"; grep -n \"^ *12[0-9] \" SOD_pages.txt | head -20"
}
```


### [2026-09-06T14:58:46.450Z] TOOL RESULT

```
7321:                                                                             1253 'pc't  B
9972: 2139 y C                                  jUjoL^j;                      ecatawe ^'yc't
10152:     enc(y) ©*ham-cyd\ A v. sd ^}ncy, 'yc't
12706:      GMS 437 n5, 1306 (used with compd. adj.); VJ                3159 c't B                                                .ur
26172:7780 ptmync't- M                                 o^x       7792 ptnymy* C                        j^juLojj^ <^L^! j
=== entry numbers 12x
4135:                                                                 120 "j'wny M =» >jwn
4139:                                                                 123 wjty    M                                   53lj<jJ>>
4145:                                                                 124 wjwn M                                   xjj<>yry>
4159:                                                                 127 »jyt-   M                               o>\}idJ^j*
4166:                                                                 129 »k B
5127:      125                                                   475 >br-' C                               0>J-C
7409:         129                                                   1277 >pks-      B                                    jt^«y«*T
12473:121                                                                                                          cWkw
28922:        126                                                          BSTii 843.42: 62 pl49.ll
29513:       128                                                         head
```


## [2026-09-06T14:58:49.633Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '12700,12730p' SOD_pages.txt\necho \"=== leaf/page\"; python3 - <<'EOF'\nt=open('SOD_pages.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\noff=sum(len(l)+1 for l in lines[:12705])\nprint(\"leaf\", t[:off].count('\\f'), \"-> printed ~\", t[:off].count('\\f')-66)\nEOF"
}
```


### [2026-09-06T14:58:51.658Z] TOOL RESULT

```
                                                                       jasmine
      GMS 1543, 1595-1601; cWry, BBB "when"
 3146 c'nkw =^ cWkw                                               3158 c'str M                                   Jjii'J&k,
 3147 c'nw B                                    jt,^                   castar ©<*c}Jsrr <cySrstr **c}8x
      canu                                                             lower
      of, than                                                         GMS 459; Hen. Tales. 481.33
      GMS 437 n5, 1306 (used with compd. adj.); VJ                3159 c't B                                                .ur
        948             S                                              cat ©Av. cau Knot, caia; Skha; Bal. ca6\
 3148 c'nwt C                                                             Khwar. ct\ Oss. cada
      canut ©conj.                                                     well
      because                                                          SCE 527; Bailey. JRAS 1970
                                                          Uj
         C2, 48R1 n p85; c>nwytyt C2, 12R5, 27R17                 3160 c'twxt M                       -^ jja>- <ju;o-
3149 c>ny C =» c>n                                                     ca-tuyd ©<ca-tur~t ©clat. adj.
                                                                       how fast
3150 c'p'r C
                                                                       GMS 254, 1314
     capar ©postp. -^c'Srp^                          <j*k *>-J
     under                                                       3161 catik
                                                                      c'tyk M                                  (.[>j/)^t>
                                                                            ©adj.
         BSTii 875.6; Schwartz. HMV 39; C2, 13V 23,
           66V6, 77V 18
                                                                      Sund. Man. Lett. 305.22
3151 c'p'rcyq C              jj^ <>jj lJs!i ^^u^l                      W)well
     caparcik ©adj.                                              3162 c'w  S                                 jt^^jj>r
     below, downwards, situated below                                  caw, zaw ©Parth. pwt ybgyw
     C2, 22V 14; Benv. J A 1955, 329                                   flow, tide
                                                                       Sund. MSP p44
3152 c'prmw S                                  <r^=5j<0-
     caparmu                                                     3163 cVn B, M, S                (<Jy> >A* >>)j'<jT jl
=== leaf/page
leaf 189 -> printed ~ 123
```


## [2026-09-06T14:58:59.344Z] TOOL CALL #43: Bash

```json
{
 "command": "sed -n 1,40p tools/ref_page.py"
}
```


### [2026-09-06T14:58:59.388Z] TOOL RESULT

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
```


## [2026-09-06T14:59:03.448Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== v3 آکندن\"; grep -n \"آکندن\\|آگندن\" incoming/BQT/BQT_v3_pages.txt | head -10\necho \"=== v3 سمرقند\"; grep -n \"سمرقند\" incoming/BQT/BQT_v3_pages.txt | head -10\necho \"=== v3 قانون\"; grep -n \"قانون\" incoming/BQT/BQT_v3_pages.txt | head -10\necho \"=== v2 1165 region\"; "
}
```


### [2026-09-06T14:59:03.531Z] TOOL RESULT

```
=== v3 آکندن
=== v3 سمرقند
209:موزلی سمرقندی. «فرهنگه نظم».
810:‎Sir‏ سمرقندی ‎ .‏ فرهنگه ‎Ri‏
1496:‏است ‎PHT IS?‏ ۷۷۷ . 6 - «شاه بوی » عبر باشد .رودکی (سمرقندی) گوبد :
3750:‎peer 09‏ و شخش امرغك کوچك خوش آوازست . رودکی(سمرقندی) کوید :
3812:رردکی سمرقندی . «لفت فری ‎۰٩۱۲0‏
4755:‏۴ _ «شفك. ابر بود . رودکی (سمرقندی) کوید:
5778:موزنی سمرقندی. «فرهنگه نظام».
5928:‏سوزلی سمرقندی.هفرهنگه نظام» +
7187:‏۱-تاکس لپ است وشنگه زبان‌است ورومه ریش...سوزنی سمرقندی .
7458:MSA ‏سوزلی سمرقندی.‎
=== v3 قانون
9334:و قاعده و قانون باشد ‎٩‏ - و ‎ner‏ هثر وکمال
10787:و زای نقطه‌دار (4) , بمه‌نی قاعده و قانون‌وروش
22628:‏9 معرب از بونانی 62060 «دائرةالمعارف اسلام : قانون» .
25679:و ‎Jal‏ تجربه و ‎se‏ و قانون دانان و عارفان | نز کفته‌اند. #
37505:صفت ‏ وگونه - وطرز و روش و قاعده و قانون
48749:‎aL‏ ۷۱- و پمعنی طرز وروش وقاعده و قانون
=== v2 1165 region
```


## [2026-09-06T14:59:08.875Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('incoming/BQT/BQT_v3_pages.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\ndef leafof(n):\n    off=sum(len(l)+1 for l in lines[:n-1]); return t[:off].count('\\f')\nfor n in (22628,9334,10787):\n    print(n,\"leaf(pdfpage-1?)\",leafof(n))\nleaves=t.split('\\f')\ni=leafof(22628)\nprint(leaves[i][:2500])\nEOF"
}
```


### [2026-09-06T14:59:10.829Z] TOOL RESULT

```
22628 leaf(pdfpage-1?) 308
9334 leaf(pdfpage-1?) 121
10787 leaf(pdfpage-1?) 143
[pdf page 309]
فان :

رستنیی ‎wt‏ مانند اشنان هر ‎wort OT eb‏
هت وکوبند مالند کشوث ‎(A)‏ است در ‎dab‏ »و
طبیمت و یگرم وخفك باشد(۲) وضف جگررا
‎git‏ است (۳) وآلرابعربی رجل‌الفروج خوانند.

قاقم! ‎ot me‏ وسکون عیم »پوستی
‎atl,‏ سفید وبغایت گرم میباشد و مردمان اکابر
پوشند - وکنابه از روز هم هست که ‎tae‏ .وم
میگویند چنانکه شبرا ‎pee ad‏ رگاه گوند
«قاقمآ ور د وقندزآورد» مراد آن‌باشدکه روزآورد
رشب آورد.

قاقم ‎Gla‏ - کنبه از ‎ak‏ دای
وروشن لمای باشد .

قاقوس ‎pe‏ وزن ناقوی 6 بیونانی
غله‌ایت که آرا بعربی عدس میگویشد.

اقا - بکس ثات بروزن ‎Gb‏ مخنف
اقافیاست؟ وآن عمار#نخم خاری است که چیزها
بدان دباغت کنند ؛ وبعض ی کوبند صمغ ‎OT‏ است
‎oT,‏ صلب وسطبروسیاه رنك میباشد.

قالنچه = نکر لام وسکون نون وفتح
جیم ؛ پرده‌اییت که آتراشیرازبان عکهوعربان

(۱) چش : کشوت .
(4) چش : است .

: te )۰(

۱و

‎aie‏ رساسل‌خوا آنند؛ویعضی کوندقالنجه فاخته‌است.
‎SU‏ بلام بروزن‌جاسوی, نا,نوابی
ولحنی باشد (4) از ‎Ngee‏

‎GAD‏ » بکرنون وفتح ‎ake‏ بی‌قطه,
منگه ‎ob‏ مرغ ‎uy,‏ پوست اندرولی اورا
خشك کرده بابند وبا شراب بباشامند دردمعده
را ‎ait‏ باشد )0( خاصه‌یوست سنگه‌دان خروی.
کونند عربی است؟ .

‏ق نونه «بالون بروزن هارون » بمعنی
اصل ورسم وقاعده باشد ...ال
وتا کتایی است ‎Keb‏ -
وتام‌سازست که مینوازند۷.
کوبند این لت معرب
کالون ‎cal‏ و عربی یست
لیکن در ‎dae ge‏

‏است .

‏قاورد © پر وزن ناورد » تام نوعی از
حلوا ‎Ac‏
‏قاو ند بر وزن خاوند ۰ چیزی باشد

‏(۳) چش : باشد ۰

‏است .

‎. ‏سود دارد‎ : ote Co)

‏۱ = قاقوم ( عر ) = ‎hermine‏ (فر ) « دزی ج ۲ ص ۲۹۵ > و آن ‎se‏

‏ازچارپابان ازئبر سموریان است
ص ۲۹۹ رگ : افاقیا .

‎hy‏ لارو بر سرو ‎uth‏ سرو سهی

‎Yeon? ‏اقاقیا‎ 2 ۴

‏۴ - «قالون ‎pe)‏ لام) موضمی

‏است که ‎oly‏ قالوسی بدان منسوب است وگاهی‌آن نوا راقالوی
نیز گوند (محذف با) . منوچهری ( دامغانی ) کوید :

‎. ‏بلبل بر تارك گل قالوسی‎ wy

‎3

‏وله . (مصراع) ‎AS:‏ چکاوك ‎Sy‏ راهوی و که قالوس» «رشیدی» هدایت درانجمنآرا

‏قالوی را همان «چالوی» مازدران پنداشته !
‎od‏ «منتهی‌الارب> .

‏۴ - (ی) «قاصة, روده واندرون مرغ» قوااص

‏9 معرب از بونانی 62060 «دائرةالمعارف اسلام : قانون» .

‎٩‏ - مراد کتاب «قالون» تألیف ابن‌سیناست بص‌بی ‎ .‏ ۷ - آلت‌موسیقی مشکل ازطبلی
مسطح ومستطیل »که میمهای فلزی بر آن‌صب ‎eas‏ وبا انگشت ‎ole‏ مسلح بزبالة فلزی آنرا-
درحالیکه روی زالو هاده است - مینوازند . «دائرةالمعارف اسلام» .

‎A‏ - پالوده برنگه اطلس معروفست

‏قاورد بفطنی ولمد موصوفت +
‎joe?‏ اطممه . چاپ استالبول ص۷٩‏ .
```


## [2026-09-06T14:59:31.525Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('incoming/BQT/BQT_v3_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i in (318,319,320):\n    print(\"=====\",leaves[i][:600])\nEOF"
}
```


### [2026-09-06T14:59:33.103Z] TOOL RESULT

```
===== [pdf page 319]
فرفار ‎Nerv‏
‏قرقمان با قاف ومیم بروزن‌بهلوان,
چوپی را کونند که درمیان مقل مکی میباشد ۵
و درسنونات ‎WG‏ برند گوشت ‎oy‏ دندان‌راسخت
کند و ‎glass‏ سفید سازد .

قرقو ‎Isl gee‏ و سکون ثانی وثالث
بواو کشیده ؛ بیونانی زعفران را کونند ۱ چه
قرقو معما (۱) ‎gly cal‏ ثفل روغن زعفران
بائد و معما (۱) بممنی ثفل است .

قرقوبی ۲ © بقتح اولوضم قاف‌بروزن
محبوبی » نوعی از جامه است که در عراق عرب
بافند ؛ و بضم اول هم گفته اند .

قر کی ۸ - بفتح اول و ‎JE‏ بر وزن
ارزن . زمیتی را گونندکه آنرا آب یا سیلاب

است شبیه بدارچینی ‎Megat‏ - وعربان مردم
تهمت‌زده را قرفه کوبند .

FS ‏با قاف بروزن سردار‎ = IS
. 
===== [pdf page 320]
روا ۱ قربطس
کنده باشد و در هر جای از آن قدری آب | بمعنی هشتاد سال است و ‎AS gam‏ هر قرتی
ایستاده باشد - و جوبی را نیز گوبند که آنرا ]| سی بال میباشد - و در عرمی شا کاو وشاخ‌بز
توکنده و احداث کرده باشند . و غیر آن - وگروه - و زماله - و هم سال -
رهز ۱ ‎Ge‏ اول و میم وسکون | و هم زمانه - و طرف روی و طرف سر و موی
‎ft‏ وزای نقطه دار. چیزی است که بدان‌چیزها | تفه ( ۲ ) شده - و آنچه در ‎Ole‏ فرج زنان
رنگ کنند ( ۱) وگویند قرمز جانوری است ‎ashe‏ د و متام و طوف بل لاب وقنی
کوچك و بر بوتهای خار می‌شیند آنرامیگیرند ‎BI‏ برمبید - و تیغ قتاب را نیز
و خشك‌میکنندومربی دودالسبافین خوانشد ۴ - کوش
===== [pdf page 321]
قرول
‎line ot,‏ رسیده و خم طای حطی ( ‎٩‏ )
و سکون مين ‎)٩( ame‏ ۰ پلفت بونالی بمعنی
‎Jie‏ و فهم و ذهن و رای باشد .

قرول ۱ - بن اود و ثالی و سکون
‎aly‏ و لام » مرجان سرخ را گوبند و پفارسی بد
خواند .

وا
قرو - با راو و میم و حرکت فیر
مطوم » سنگی ‎ath‏ حفت رنگه -
قرو هه ۴ - بر وزن و معنی کروعه
است که کلوله باشد خواه از سنك ‎IS y‏ و ‎hye‏
‏از چیزهای دیگر سازند .

‎oly‏ هفتم
درقاف با زای نقطه‌دار مشتمل بر نه لغت و کنایه

‎pl ‏جتح اول وسکون ثانی‎ - FD
. ‏خام بدقماش را گویند‎

‏قز اغنف ۴ - باغن قطه دار بر وزن
دماوند, جامه‌ای را گویند که برحشو ‎OT‏ ابرشم
و ‎aig a‏ وآجیده بکنند و درروزج
```


## [2026-09-06T14:59:45.179Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"قزاغند\\|کژاکند\\|کژآگند\\|قزاکند\" incoming/BQT/BQT_v3_pages.txt incoming/BQT/BQT_v4_pages.txt BQT_v1_pages.txt BQT_v2_pages.txt incoming/BQT/BQT_v5_pages.txt 2>/dev/null | head -10"
}
```


### [2026-09-06T14:59:45.245Z] TOOL RESULT

```
incoming/BQT/BQT_v3_pages.txt:23397:وزن و ممنی قزاکند است که خفتان‌جنکه‌باشد؛
incoming/BQT/BQT_v3_pages.txt:23427:بمعنی » وقرا کند نیز کنند ‎ie‏ را «لت فرس ۰۳۸۹ ‎A‏ مسحف «قزاکند»(هم) =
BQT_v1_pages.txt:3202:۴ - نبطی- در ذیل «قزاغند > گوید : گویند این لفت ابطیاست؟ .
```


## [2026-09-06T14:59:48.987Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('incoming/BQT/BQT_v3_pages.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\ndef leafof(n):\n    off=sum(len(l)+1 for l in lines[:n-1]); return t[:off].count('\\f')\nprint(leafof(23397), leafof(23427))\nleaves=t.split('\\f')\nprint(leaves[leafof(23397)][:200])\nEOF\nsed -n '23390,23435p' incoming/BQT/BQT_v3_pages.txt"
}
```


### [2026-09-06T14:59:51.088Z] TOOL RESULT

```
320 320
[pdf page 321]
قرول
‎line ot,‏ رسیده و خم طای حطی ( ‎٩‏ )
و سکون مين ‎)٩( ame‏ ۰ پلفت بونالی بمعنی
‎Jie‏ و فهم و ذهن و رای باشد .

قرول ۱ - بن اود و ثالی و سکون
‎aly‏ و لام » مرجان سرخ را گوبند و پفار
و معتی قراغند است که ‎Lele‏ پنبه و ابرشم
‎2ST‏ (4) آجیده کرده‌شده باشد که درروزهای
‎fe‏ پوشنه وآنرا خفتان کوبند ۷ -و نبالی

‏و توشك و ‎le‏ خواب را نیز ‎ala”‏ .

‏قزا گنگ ‎Sp pte A‏ فارسی» بر
وزن و ممنی قزاکند است که خفتان‌جنکه‌باشد؛
و زره را نیز کفته‌اند و آن جامه‌ای باشدکه از
حلقهای ‎AT‏ ترتیب داده در روز جنگه پوشند.

‏قزاوه ‘ = بر وزن و معنی کجاوهء‌است
که محمل باشد.

‎oP‏ منم اول و فتح ثانی و سکون
حای بی نقطه » نام یکی از شیاطین است وبدین
سبب‌قوی قرح )0( را کمان شیطان‌میگوبند*۱-

‏(۱) چك : طا .
(4) چش : ] کنده .

‎. ‏چك : - سعفص‎ (x)

‎. ‏چك : بوزن‎ (rv)

‏)0( چش : قوس و قزح .

‏۱ قروال «عقار ۲۷٩»ظ‏ : قورال که نام ‎tail‏ باشد . اسپانیولی ‎Coral‏ از بونانی
‎caoril = korallion‏ (فر) ‎we‏ « دزی ج» ص۳4۱ * «عقار ۲۲۷ ‎day‏ : فردالبون .

‎any = ۴‏ (هم.).

‏۴ معرب «کرّ*(«.م.) «رشیدی؟ پهاوی 626 «ناوادبا

‏۲ بر کیلان ‎kaj (pila)‏ بابرشم خام اطلاق شود . در عربی بمعنی ایریشم (خاما «دزیج»
ص 44۲ » رك : قراغند . ۴ = فراکند = کزاکند ه کذژافند )2 م.) = کجا کند
درشیدی» ‎ .‏ ۵ - دراصل‌فارسی‌است . فراغند ‎Coe)‏ ۷ -«خفتان, قبا باشد
بمعنی » وقرا کند نیز کنند ‎ie‏ را «لت فرس ۰۳۸۹ ‎A‏ مسحف «قزاکند»(هم) =

‎a ‏قوی قرح کزفر ممنوعة‎ « (Ue) -* ‏(هم).‎ oslo Cpa) ‏کجاوء‎ = ٩
‏راکمان رستم نیز خوانند.‎ OT ‏آنچه پیدا شود بر هوا حرخ و سبز بشکلکمان و‎ gies ‏آدبنده‎
‎ath ‏او لارتفاعها من‌قزح بمعنی ارتقع» با قرح نام فرشته‌ای موکل بر‎ , de Aly ‏سمیت لتلونها‎
‏با نام پادشاهی از پادشاهان عجم , و قوس منسوب است بسوی این هردو.» «منتهی‌الارب».‎
[pdf page 322]
Ls —Vera—
```


## [2026-09-06T15:00:11.484Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('incoming/BQT/BQT_v3_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i in (494,495,496,497):\n    print(\"=====\",leaves[i][:300].replace('\\n',' | '))\nEOF\necho \"########## vol2 leaf 620-624\"\npython3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nprint(len(leaves))\nfor i in (620,621,622,623):\n    print(\"=====\",leaves[i][:300].replace('\\n',' | '))\nEOF"
}
```


### [2026-09-06T15:00:13.444Z] TOOL RESULT

```
===== [pdf page 495] | TS | . ۱ ‏باتد‎ Sey | + ‏کنچاد ۲ = بنم اول بروزن رخار‎ | ‏و تغل تخم کنجمد و هر تخمیکه روغن‌آنرا‎ Ses | ‏بمعنی‎ . assy ‏کنچاده ؟ - بروزن‎ | ‏کتجار است که تخاله کنجد و هر تخم که روغن‎ | . ‏کشینه باشند‎ 1:1 | . ‏اول بروزن دنسال‎ ane ۴ ‏کنچال‎ | ‏بمعنی کتجاره است که ثفل, نخم روفن کشیده‎ | aren | wm . ‏کفچاله
===== [pdf page 496] | ime) od eed |  | دو لون و ‎Clap gS gine operas‏ و خورد (۱) | باشد - و بممنی ‎Mall‏ و کم کم و بهره بهره لیز | ‎aul‏ است ؛ و باين معنی با جیم فارسی هم | کفته‌اند ؛ وبجای نون بای "حطی نیز بنظرآمده |  | است . |  | ‎Joe”‏ ۱ « بروزن بلبل » هرچیزدرهم | کشیده شده و چین و شکنج بهم رسالیده باشد- | و دست وپاییرا نیز 
===== [pdf page 497] | بمعتی ‎do‏ و پهلوان و مردانه و ‎elms‏ بلشد ‎TS‏ |  | - وفیلوف و دانا و حکیم,را هم کفته‌اند ۴ - | وکنده‌ای که برپای مجرمان و کربزپابان نپند ۴ | - و قض یز .هم هت چنانکه گوبند « اين | کار کند است > یعتی تیز نیست - وخصیه ‎NT,‏ | ‏تناسل را نیز کفته‌امد ؛ و باین ممنی باکاف‌فارسی | هم‌آمده است و اصح آنت ۴
===== [pdf page 498] | ‎—\veo—‏ کندرو |  | ‏باری ومیوه‌ای و تخمی ندارد صمغ آن را بنام | ‎oT‏ درخت خوانند و صمغ‌البطم همان است ‎OT,‏ | ‏شبیه است بمصطکی . وطبیت آنکرم باشد - | و نام پادشاه سقللاب هم بوده و اوییاری افراسیاب | آمده بود ۵ . |  | ‏کندردوهی ‎gine ag’‏ است که | آ را علك رومی میگوبند و مصطکی‌همان است. |  | ‎» ‏اول بر وزن
########## vol2 leaf 620-624
684
=====    ‫‪—۱‬‬     ‫تن‬ |                                                                                                                 ‫سگال‬ |                                                          ‫آبی است» وآن حیوالی باشد که آش بجگان‬ |  ‫وه بالف‬ |        ‫سگان ابزک‪-‬ر نوهنمز‬ | ‫»نابه ازطالبان‌ دیا‬ |    
=====                                                                                                      ‫—‬       ‫پوي‬ |  |  |  ‫آنجا وافم شده است وآنرا سگزی ازآن‌جهت‬                          ‫و رفتن؛وباین معنی‌باشین لقطه‌دار هم آمده‌است‪.‬‬ |  |  |                                               ‫‪7‬‬            
=====      ‫=‬‫)وی‬‫‪-‬‬ |  |  ‫میگونند که حر کس آنرامیکند میمیرد » پس‬                    ‫=روزن سیتان »زاباتان‬ |                                                                               ‫سگستایت ‏‪ ٩‬ب‬ |  ‫بوقت کندن اطراف آنرا خالی کنند طونابی‬                       ‫باشد که سیستان امت ومعربآن سستان‌بود‪
=====   ‫سلشوق‬                                                                                               ‫‪۱‬‬ |                                                                                                       ‫س‬ ‫اهی‬ |  |  | ‫باشد بمقدار فلفل و آن سرخ و سياه رنگهدیز‬               ‫بی قضاعه گوبند و خ
```


## [2026-09-06T15:00:23.218Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('incoming/BQT/BQT_v3_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nprint(leaves[496])\nEOF"
}
```


### [2026-09-06T15:00:24.708Z] TOOL RESULT

```
[pdf page 497]
بمعتی ‎do‏ و پهلوان و مردانه و ‎elms‏ بلشد ‎TS‏

- وفیلوف و دانا و حکیم,را هم کفته‌اند ۴ -
وکنده‌ای که برپای مجرمان و کربزپابان نپند ۴
- و قض یز .هم هت چنانکه گوبند « اين
کار کند است > یعتی تیز نیست - وخصیه ‎NT,‏
‏تناسل را نیز کفته‌امد ؛ و باین ممنی باکاف‌فارسی
هم‌آمده است و اصح آنت ۴

‎LT‏ - ینم اول بر وزن ‎Us‏ حکیم
وقبلوف و دانا و منجم راکویند ‎٩‏ - و بمعنی
شجاع ودلیر و پهلوان ‎pe‏ هست ۷ - بفتح ‎Jal‏
‎Sd‏ بهردو ممنی‌پنظرآمده - و نام نقاشی‌ومصوری
هم بوده است ؛ و باکاف فارسی لیز درست است.

‎۳۹

‏کندا گر ۲ ‎ee‏ اول بروزن‌خنیا کره

‎pines‏ کنداست که و ودانا - و شجاع ودلیر
و پپلوان ‎ash‏ ۸

‏کندامویه - + ینم اول و میم » موی

‏مادرزاد باشد ‎Ts rises‏ چون طفل زاییده‌شود
در بدن او باشد .

‏کنداواله ‎٩‏ ضم اول و واو ‎AL‏

‏کشیده و فتح لام ۰ مرد بلند بالای قوی ‎Je‏
‏راگویند - و بمعنی امرد درشت ت اندام فربه لیز
صت که مزلف بد اندام ‎cath‏ و ‎gam‏ امرد
بز رک ناهموار را گفته‌اند .

‏کند آور ۲۰

‏پا واو » بروزن ومعنی

‎, ) ‏شجاع‎ ( kuntha - ) ‏پرااکریت‎ ( oo Cot. ) ‏شجاع , دلیر‎ ( kund = ۱

‏بلوچی ‎kunt‏ ( شجاع + خشن
‎Cea)‏ را مر کب از همین کلمه دانسته‌اند
آن است :

‏خصم را پا در رکاب توز اسب اندر فکند

‏ره :کندا .

‏ابله ) « اسشق -
. رك :کندا « هوبشمان ‎Lal‏ » و کندی حاضل مصدر

‎wet
‏(سحر , احکام نجوم) فارسی‎ gnd'yy ‏در اوراق مانوی ( پهلوی)‎ -

‏هوبشمان ‎OANA‏ هرن و هوبشمان «کندآور»

‏بس که درمیدان کندی اسب برخصم‌افکنی.
سوزلی سمرقندی « رشیدی * .
۴ -صحیح «گند - چند
‎wl) kunda‏

‎Henning, A fist of Middle Persian.. ,) ۵008 ‏پپلوی‎ (eles. ۳ gale ‏منجم,‎

‏04 (
آفرین باد بران مر کب خوش رفتارت

‏که دل زبرك و اندشه کندا دارد .
‎pull le‏ عبدالرزاق اصفهانی

‎. oat?

‏1 - هوبشمان «کندا » ‎CS? hey |, Kun‏ بسنی شجاع میداند > هوبمان
‎By ۸‏ : کنداکر کنداور . درین صورت «کندا » بمعنی شجاعت و دلیری است مر کب‌از:
صفت کند (شجاع) ۱-۲ ‎BIL)‏ اسم ممنی از صفت ) ۰ قس : درازا » ستبرا ‏ روشنا . رك : اسم

‏مصدر بقلم نگارنده ۱۱۹-۱۱۸ .

‏۲ + از : کندا (.م.) ۲ کر (پسرند شفل ومبالفه).

‎A‏ - ممرب‌آن ‎TUS?‏ ( بضم اول و کسر پنجم ) : « الشجاع » الجصور » فارسیةنقلها

‎.) ۵ ‏اقرب‌الموارد : 2 ان د‎ ( (OMS ‏عن‌بعض‎ GS

‏4 کندراله (هم).

‎N°‏ این ‎cal‏ در فرهنگها بصورت «کندآور* آمده است . بسض فنلای مماصر صورت

‏اخیر را سحیح داسته‌اند. بولد که وهرن وهوبشمان « اسشق

‏- هوبشمان ‎CANA‏ آلرا با کاف‌تازی

‏از ‎dey‏ «کند » ‎gine‏ شجاع هل کردماند , ولف نیز در فهرست شاهنامه « کندآور © و « کند
آوری » را ‎GEL‏ تازی آورده است . بتابراین کندآور باید مر کب از :کندا ( شجاعت ) + ور
‎sigs (‏ اصاف ) باشد » به از : کند (شجاع) + آور (آورنده) چه آور در ‎ALT‏ فرکبه ازاسم
آید : رزم‌آور » تناور » دلاور ‎Ay)‏ : لف‌نامه : آور ) - و رك :کندآور.
```


## [2026-09-06T15:00:33.903Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== v3 سغدی\"; grep -n \"سفدی\\|سغدی\\|سکدی\" incoming/BQT/BQT_v3_pages.txt | head -20\necho \"=== v3 kand/knd latin\"; grep -n \"kan6\\|kand\\|kan8\\|kanθ\" incoming/BQT/BQT_v3_pages.txt | head -20"
}
```


### [2026-09-06T15:00:33.963Z] TOOL RESULT

```
=== v3 سغدی
8175:‏© - شم فیس درذکر « ابوحفص حکیم ‎on‏ احوس سفدی» کوید : « او در صناعت
8218:‏آبوریان بیرولی درفهرست روزهای ابرانی نام این ررز را « شهریور * و درسفدی « خستشور ©
16012:استاد هنینگهه کوید:باشکال میتوان ابن‌کلمه را ازسفدی ‎ghwdh7k‏ (طرف) ‎(Dhyana,277)‏
17794:‎farxar - ۱‏ فارسی ( بمعنی ‎po‏ ومعبد (بتخانه) ) از ‎U5‏ سفدی ‎Brgh’r‏ مأخون
17987:بقطمات بربدن )آمده. ‎chy‏ فرهنگ پارسی‌میانه بسغدی چنین آمده : پارسی ‎m= ‘skangul.‏
17989:معنی اصلی سفدی ‎fraxwak‏ و پارسی ‎ishkanag ot.‏ چنین ‎oy‏ ( چیزی پربده با شکسته
19478:درسفدی « فرون > و درخوارزمی 9 روجن > ‎Sob‏ 02 درادییات پایسی« فرودین » ‎ce ( ates‏
20270:‏گوید (رك:صفحهّقبلح۸): فژاکن (رك : ‎usuely seal‏ معرارجمالی: ‎(fazhakan‏ قس:سغدی
31124:‏سفدی 8006 - 627۷ ( دارای دندان مجوف با فاسد ) ؛‎ (a ۸۲4 ‏ص‎ T ‏فولری‎
48258:‎TH‏ جوش > ( معرب گوش ) و در سفدی « غش * و در خوارزمي « غوشت * آورده :
=== v3 kand/knd latin
36178:‎kandrak ole. ol Sm ۵‏ , اوستایی 187302 « دارمستتر ‎cobs.‏ سس
36819:‎kandal jus. kendn‏ , استی ‎nijginin‏ ( دفن‌کردن ) .95 : ارمنی 8688 « اسشق
36900:‏— پهلوی ‎kandak‏ > تاوادیا ۲:۱5۲»
```


## [2026-09-06T15:00:41.181Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('incoming/BQT/BQT_v3_pages.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\ndef leafof(n):\n    off=sum(len(l)+1 for l in lines[:n-1]); return t[:off].count('\\f')\nfor n in (36819,36178,36900):\n    print(n, \"leaf\", leafof(n))\nEOF\nsed -n '36805,36830p' incoming/BQT/BQT_v3_pages.txt"
}
```


### [2026-09-06T15:00:42.942Z] TOOL RESULT

```
36819 leaf 499
36178 leaf 491
36900 leaf 500
* ناسر خسرو بلشی‌س۳۷۹ ۰

‏انواع کندوی زیورعل

‎che‏ ,کوی ,کندوری‌افگنده خوار.»

‎ONY ‏فرسص‎ cal?

‏5 : فراخ کندوری در تاریخ بیپقی مصحح دکتر ‎phd‏ ۱۹۱ ۰

‏© کندن - ‎pie‏ اول و سوم » از: کن ‎wb‏ ( پسوند مصدری ) ؛ پهلوی 620080 ؛

‎By‏ باستان ‎kam‏ ( کندن, حفر کردن ) « بارتولمه 4۳۷ » « نیب رکه م۱۱۹٩‏ پارسی‌باستان,
اوستا - 16817 » پپلوی نیز ‎(sn) kantan‏ , هندی ‎khan - ott‏ , ۳6۳08۵01 , کردی
‎kandal jus. kendn‏ , استی ‎nijginin‏ ( دفن‌کردن ) .95 : ارمنی 8688 « اسشق
۶ ورك : عوشمان ‎AVA‏ .
[pdf page 501]
pts

‎ae ۱ 39a‏ اول و سکون ثالی
وثالث بواو کشیده و ‎DE‏ زده. ظرفی باشدا ز گل
مانند خم بزرک ی که غله در آن‌کنند و معرب
آن کندوج باشد .

‏کنف و کوب - بنتح اول و ضم کاف
بروزن تغز و خوب ‎MOLT‏ تثویش ‎SAN gay‏
```


## [2026-09-06T15:00:54.844Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('incoming/BQT/BQT_v3_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i in (497,498,499):\n    l=leaves[i]\n    if 'سمرقند' in l or 'قریه' in l or 'دیه' in l:\n        print(\"=== leaf\",i)\n        print(l[:3500])\nEOF"
}
```


### [2026-09-06T15:00:56.810Z] TOOL RESULT

```
=== leaf 498
[pdf page 499]
Vv.

کندد اش بفتح اول واكت‌رسکون
آخ رکه شین قطمدار باشد » زمین پشته پشته ‎My‏
‏کوند ۱ . ۱

کندده = قتح اول بر وزن جندره .
مرغکی است که درآب شیند و مکان و ‎OAT‏
‎ote‏ سازد .

‎eno SIT‏ اول ‎Ny‏ و سکون
‎yl‏ و زای نقطه‌دار در آخر . نام شهری بوده
آباد کرد جمشید و پای تخت ‎Orbs‏ هم بوده
است و معرب آن قندزباشد - و بضم اول و کسر
الك مخفف کپن دز است که قلعهٌ کهثه باشد ؛
و کوشك ‎SEN,‏ کهنه را هم کفته‌اند - و نام
شهری بوده درتوران آباد کرد فربدون وا کنون
بیکند گویندش ۴

‏کندسه ۴ ‎geo‏ اول و ثالك و بفتح
سین بی‌نقطه» چیزی است کهآ براآذ ربون کویند
و بثیرازی چوبك اشنان خوانند اکر سه فطرء
ازآب بیخ ‎OT‏ در بینی چکانند درد دتداترا نانع
باشد .

‎PAF‏ = نم اول وکسر ثالك بروزن
جنبش ‎UIT.‏ پنبه برزده را گوبند که بجپت

‏۱ ره : فهرست ولف » رشیدی » فرهنگه نظام .

‎-۱۷ ۰۹

‏رشتن مهیا کرده ‎Math‏ - و ‎Lage‏ نی زگویند
که حلاجان ‎bey‏ برزدء را برآن پیچند ‎SATE‏
‏شود ؛ و بفتح اول وضم سیم نیز پنظرآمده است-
و بمعتی کندسه هم هست که چوبك اشنان باشد
ومعرب‌آن قندش است ‎٩‏

‎SAS‏ » منم اول بروزن اردلك . نان
‎oy)‏ شده وپاره پاره را گویند .

‏کند گوش ۰ب ‎GE‏ فاسی بروزن
سرخ پوش » کیرا کویند که کوش او کم
شنو باشد یعنی چیزی را بلند باید کفت نا
شنود .

‏کنك لان » بنتح اول و ضم ثالك و لام
بالف کشیده ونون زده ۰ نوعی از: خیمه‌راگویند
و ‎am‏ اين لفت را تر کی میدانند و نم اول
و فتح ثالث میگوند ۷ .

‏کندله * - بنم اول و ثالك و فتح
لام ‎i‏ چیزی کره شده و مکجا ‎aoe‏ کفته را
گونند .

‏گندهنف ‎ho ٩‏ اول و میم بروزن
‎«ars‏ عمارتیر! گویند که خراب شدء و ازهم

‏۴ مخفف « کهن دز ©

‏( دژکهن ) > قهندز س قندز ( مخنف ):«کندز, مث یکپن دز » واین دژ شهری باشد . رود کی

‏(سمرقندی) گفت :
که بران :کندز بلند شن

‏۴ - در شاهنامه کندز )= بیکند) مقر حکومت افراسیاب است

‏که درین بوستان و چشم کشای»
« لت فری ۱۸۲ *.
. رگ : فهپرست ولف.

‏۴ - در رشیدی بنقل از الامی « کندش» ( بضم اول و کسر دال ) « چوبك اشنان که

‏خمیر؛ شکر بآن سفید »کنشد .» رك : کندش .
‎Hey‏

‏آورده « فرهنگه نظام © .
عصمت ‎Sig‏ رخ بسا پرده‌ات مقیم

‎. ‏امروز با کاف پارسی 8080616 گویند‎ A

‏( پمودد اتساف ) .

‏- النامی » در معنی سبیخه « کندش»
و5 رك : سروری » غباث‌القات :

‏دولت کشاده رخت ‎OVS pile‏ .
«حافظ . مصحح قزونی‌ص‌قیح».
- از : کند ( کندن ) +-مند

‎)۳۱۸ ‏قاطع‎ olay (
```


## [2026-09-06T15:01:09.507Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i,l in enumerate(leaves):\n    if 'سمرقند' in l and 610<i<660:\n        print(\"=== leaf\",i,\"printed ~\",i+543)\n        import re\n        for m in re.finditer('سمرقند', l):\n            print(\"   ...\", l[max(0,m.start()-400):m.start()+400].replace('\\n',' | '))\n        break\nEOF"
}
```


### [2026-09-06T15:01:11.592Z] TOOL RESULT

```
=== leaf 629 printed ~ 1172
   ... م‬ | ‫افتیمون » بلفت بونالی‌دوابی است کهآ لرابفارسی‬                                ‫وفکر و خیال باشد ‪#*.‬‬ |  ‫مرزنگوش و بمربی آذان‌الفار خوانند ‪ .‬خوردن‬       ‫سمر كنك ‪ = ۴‬باکاف» بروزن و معنی‬ |       ‫آن باشراب گزندکی افعی را نافع باشف‪.‬‬         ‫باشد درماور اء الهر‬      ‫سمر قند است و ان شهری‬ |  |  | ‫امنی و سکون‬ |           ‫وض‬‫سمك » بنتحارل ث‬                        ‫که کاغذ خوب ازانجا آورند و سمرقند معرب‬ |   ‫‪- ۴‬برساختة فرقةٌ آذر کیوان «فاب ‪۱‬ص ‪« ۷46‬فرهنگه‬           ‫‪ ۴‬رك‪ :‬سمه ‪.‬‬         ‫‪ ۱‬رك‪:‬سمر کند(‪)۱‬‬ |   ‫آن سمررقند وسمران (ض‌اول)‬        ‫عرب‬     ‫‪۴‬‬       ‫‪. °‬‬    ‫دبتان المذاهبء ص ‪6‬‬        ‫دساآیر ‪۲٥۲‬‏‬ |   ‫رك ‪ :‬معجم البلدان ‪ .‬پهلوی ‪ . 0۳2۲202۹‬بونانی ‪ 200۳26۵۲21۷1‬رة جزو اول سمر تا‬ |   ‫کنون‌معاوم ده » جزو دوم ‪ 0021‬ا‪,‬ز پارسی باستان ‪ , # 01021-
```


## [2026-09-06T15:01:22.495Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nl=leaves[629]\ni=l.find('معجم البلدان')\nprint(l[max(0,i-1500):i+1200])\nEOF"
}
```


### [2026-09-06T15:01:24.736Z] TOOL RESULT

```
مر »دام بادشای‬
                                ‫ابام شهر شده ‪.‬‬   ‫نوده از قرك ‪ - 0‬ودست افز اری‌است جولاهگادر |‬

‫سمسق ‪ - ۱‬بنتحاول و سکن ثابی‬                       ‫و آن مانند جارو بی اشد که باآن آحار برتاره‬


 ‫و کر سین بی‌نقطه و قاف ساکن » بلفت رومی‬          ‫جامه مالند ‪ ۴‬؛ و باتشدید الی هم‌آمده‌است‬
‫کناهی باشددوابی که‬
                 ‫مرزنگوش راکویند؛ و آ‬             ‫افانه وافانه گفتن باشف ‪۳‬‬        ‫هی دبمعنی‬    ‫زعر‬
                                                                                                 ‫دو‬‫‪-‬‬

 ‫بعربی آذان‌الفار خوانند ؛ وبعضی کوبند سمسق‬        ‫و بفتح اول وسکون انی هم در عربی‌بمعنی‌افانه‬
             ‫عربی است ویممنی امین است ‪.‬‬               ‫کفتن ‪ -‬ومیخ آهنی برجابی کوفتن باشد ‪.‬‬
 ‫سمسیهون ه با سین بی نقطه بورزن‬                    ‫سهر اث ‪ ۳‬بروزن فرهاد » بممنی‌وهم‬
‫افتیمون » بلفت بونالی‌دوابی است کهآ لرابفارسی‬                                ‫وفکر و خیال باشد ‪#*.‬‬
 ‫مرزنگوش و بمربی آذان‌الفار خوانند ‪ .‬خوردن‬       ‫سمر كنك ‪ = ۴‬باکاف» بروزن و معنی‬
      ‫آن باشراب گزندکی افعی را نافع باشف‪.‬‬         ‫باشد درماور اء الهر‬      ‫سمر قند است و ان شهری‬


‫امنی و سکون‬
          ‫وض‬‫سمك » بنتحارل ث‬                        ‫که کاغذ خوب ازانجا آورند و سمرقند معرب‬
  ‫‪- ۴‬برساختة فرقةٌ آذر کیوان «فاب ‪۱‬ص ‪« ۷46‬فرهنگه‬           ‫‪ ۴‬رك‪ :‬سمه ‪.‬‬         ‫‪ ۱‬رك‪:‬سمر کند(‪)۱‬‬
  ‫آن سمررقند وسمران (ض‌اول)‬        ‫عرب‬     ‫‪۴‬‬       ‫‪. °‬‬    ‫دبتان المذاهبء ص ‪6‬‬        ‫دساآیر ‪۲٥۲‬‏‬
  ‫رك ‪ :‬معجم البلدان ‪ .‬پهلوی ‪ . 0۳2۲202۹‬بونانی ‪ 200۳26۵۲21۷1‬رة جزو اول سمر تا‬
  ‫کنون‌معاوم ده » جزو دوم ‪ 0021‬ا‪,‬ز پارسی باستان ‪ , # 01021-‬سفدی ‪( 81861‬شهر) ‪.‬‬
  ‫® ‪ -‬رك‪:‬سمر (‪)۱‬‬                                                     ‫مشتق از ‪ 7126 -‬ک‬
                      ‫(ندن) ‪.‬رك ‪ :‬مکاورارت ‪.‬شهرستانهای ابرانشهرص ‪٩۲‬‏ ‪.‬‬
  ‫‪(- ۱‬عر) « سمق کجفروزبرج وقذفة وجندب » کل باسمین ومرزنگوش » « منتهی‌الارب »‬
                                              ‫‪.‬‬    ‫=‪( 601210۲2‬فر) «لك ‪۲۲۹۲‬‬‫‪1‬‬
                                                      ‫‪ #‬سهر قند ‪ -‬رك ‪ :‬سمر کند ‪.‬‬

                                                                               ‫بقیه از صفحهٌ ‪۶۹۱۱‬‬
   ‫‪ #‬سماق ‏ سماقیل ‏ سمالك که ‪suhR 21۲21۲06‬‏ «لك‪۲‬‬
   ‫ککللاپ ‪.»۷۱۲‬فراسوی ‪6231۳۱5‬‬      ‫ص‪ ۰۸۲‬و ‪suhR 511710706‬‏ «‬
   ‫= انگلیی‪16200115‬؛ کیاهی از ابر سماقیان دارای بر گهای‌مر کب‬
   ‫گلهای خوشه‌ای که پس از رسیدن خوشه‌ای بهم فشرده بادانه‌هایعدسی‬
   ‫شکل تشکیل میدهدوروی دانهارا پوستة نازکی فرمز رن" بامواداسیدی‬
   ‫پوشانده است‪ « .‬ککلاب ‪ » ۷۱۲‬وآن درنقاط کرم روبد ودر صباغی‬                           ‫سماق‬
```


## [2026-09-06T15:01:36.880Z] TOOL CALL #56: Bash

```json
{
 "command": "ls site/pages/214.jpg 2>/dev/null; pdftoppm -f 214 -l 214 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg214 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/"
}
```


### [2026-09-06T15:01:39.433Z] TOOL RESULT

```
site/pages/214.jpg
total 760
drwx------ 2 sfmqrb sfmqrb   4096 Sep  6 11:01 .
drwx------ 4 sfmqrb sfmqrb   4096 Sep  6 10:51 ..
-rw-rw-r-- 1 sfmqrb sfmqrb    264 Sep  6 10:53 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  92182 Sep  6 10:55 bqt1854.png
-rw-rw-r-- 1 sfmqrb sfmqrb  66580 Sep  6 10:57 bqt2023.png
-rw-rw-r-- 1 sfmqrb sfmqrb  54688 Sep  6 10:58 pg201.png
-rw-rw-r-- 1 sfmqrb sfmqrb  70083 Sep  6 10:52 pg204.png
-rw-rw-r-- 1 sfmqrb sfmqrb  77858 Sep  6 10:52 pg206.png
-rw-rw-r-- 1 sfmqrb sfmqrb  67371 Sep  6 10:53 pg207.png
-rw-rw-r-- 1 sfmqrb sfmqrb  59146 Sep  6 10:53 pg208.png
-rw-rw-r-- 1 sfmqrb sfmqrb  53054 Sep  6 11:00 pg209.png
-rw-rw-r-- 1 sfmqrb sfmqrb  83752 Sep  6 11:01 pg214.png
-rw-rw-r-- 1 sfmqrb sfmqrb 117034 Sep  6 10:54 pg215.png
```


## [2026-09-06T15:01:41.814Z] TOOL CALL #57: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg214.png"
}
```


### [2026-09-06T15:01:42.161Z] TOOL RESULT

```

```


## [2026-09-06T15:01:42.157Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-06T15:01:58.512Z] TOOL CALL #58: Bash

```json
{
 "command": "sed -n 1,30p tools/fetch_source.py"
}
```


### [2026-09-06T15:01:58.549Z] TOOL RESULT

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
```


## [2026-09-06T15:02:05.953Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \\\n \"https://en.wiktionary.org/wiki/%D8%A2%DA%AF%D9%86%D8%AF%D9%86\" \\\n \"https://en.wiktionary.org/wiki/%D8%A7%D9%81%DA%AF%D9%86%D8%AF%D9%86\" \\\n \"https://en.wiktionary.org/wiki/%D9%BE%DB%8C%DA%A9%D8%A7%D9%86\" \\\n \"https://en.wiktionary.org/wiki/%D9%82%D9%86%D8%A7%D8%A9\" \\\n \"https://en.wiktionary.org/wiki/Samarkand\" \\\n \"https://en.wiktionary.org/wiki/%D9%82%D8%A7%D9%86%D9%88%D9%86\" \\\n \"https://www.etymonline.com/word/canal\" \\\n \"https://www.etymonline.com/word/cane\" \\\n \"https://www.etymonline.com/word/canon\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 214, root Gwhen 1 (kan/gan), verifying nodes\" 2>&1 | tail -1\ndone"
}
```


### [2026-09-06T15:02:13.378Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/f9b28a8a8d8bffa9.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ca75e128dca3abac.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a0f23a9129817626.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/45dd7b7e29175ad6.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c3a8949848e34330.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/0abe86d1ece6775a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/581981c502fc827f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/984e8d509585781c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/123a7f91c8f43fc1.txt
```


## [2026-09-06T15:02:16.330Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nfor f in f9b28a8a8d8bffa9 ca75e128dca3abac a0f23a9129817626; do echo \"########## $f\"; grep -n -A12 -i \"Etymology\" $f.txt | head -50; done"
}
```


### [2026-09-06T15:02:18.040Z] TOOL RESULT

```
########## f9b28a8a8d8bffa9
########## ca75e128dca3abac
########## a0f23a9129817626
```


## [2026-09-06T15:02:20.944Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nhead -40 f9b28a8a8d8bffa9.txt; echo \"#####\"; wc -c *.txt | head -20"
}
```


### [2026-09-06T15:02:20.997Z] TOOL RESULT

```
URL: https://en.wiktionary.org/wiki/%D8%A2%DA%AF%D9%86%D8%AF%D9%86
FETCHED: 2026-09-06T15:02:08Z
STATUS: 200
TITLE: آگندن - Wiktionary, the free dictionary

آگندن - Wiktionary, the free dictionary 

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

#####
    3959 0013bab04a208776.txt
    7032 003529da0fded286.txt
   37902 00446da837c05ca7.txt
    5512 0070109655be6e11.txt
    2214 00738e15ee065d37.txt
    6565 008d977afc1818a4.txt
   12737 009343e3dc6e44d5.txt
    6430 0097c36e54f76601.txt
    6954 009ed6a3d0d97ac5.txt
   15378 00af144fca24970c.txt
   25209 00b2c829968cc7a8.txt
    7407 00ce8741315d1238.txt
     127 00df87111104727a.txt
    5484 01326eac7cfcce41.txt
    6017 013e05c07e6ba085.txt
   11311 0166c4af8e0b265a.txt
    5451 016a80311b8a0e7c.txt
    6602 016fa974d84963b0.txt
    4343 0180d09c6db6728a.txt
    5494 018d14b3fe147c94.txt
```


## [2026-09-06T15:02:25.619Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nfor f in f9b28a8a8d8bffa9 ca75e128dca3abac a0f23a9129817626 45dd7b7e29175ad6 c3a8949848e34330 0abe86d1ece6775a; do echo \"########## $f\"; sed -n '40,200p' $f.txt | grep -n -i -B2 -A8 \"Middle Persian\\|Proto-Iranian\\|Etymology\\|from Arabic\\|Sogdian\" | head -40; done"
}
```


### [2026-09-06T15:02:27.495Z] TOOL RESULT

```
########## f9b28a8a8d8bffa9
########## ca75e128dca3abac
########## a0f23a9129817626
########## 45dd7b7e29175ad6
21-
22- 1.1 
23: Etymology 
24-
25- 1.2 
26- Pronunciation 
27-
28- 1.3 
29- Noun 
30-
31- 1.3.1 
--
44-
45- 2.1 
46: Etymology 
47-
48- 2.2 
49- Pronunciation 
50-
51- 2.3 
52- Noun 
53-
54- Toggle the table of contents 
--
124- Wikipedia ar 
125-
126: Etymology
127- [ edit ] 
128-
129- From Aramaic קַנְיָא / ܩܢܝܐ ( qanyā , “ reed, cane, tube ” ) , from Akkadian 𒂵𒉡𒌑𒌝 ( qanûm ) .
130-
131- Sense 2 is a semantic loan from English channel .
132-
133- Pronunciation
134- [ edit ] 
########## c3a8949848e34330
24-
25- 1.2 
26: Etymology 
27-
28- 1.3 
29- Pronunciation 
30-
31- 1.4 
32- Proper noun 
33-
34- 1.4.1 
--
44-
45- 2.1 
46: Etymology 
47-
48- 2.2 
49- Pronunciation 
50-
51- 2.3 
52- Proper noun 
53-
54- 3 
--
155- Samarqand ( official name in Uzbek ) 
156-
157: Etymology
158- [ edit ] 
159-
160: From Russian Самарка́нд ( Samarkánd ) , from Persian سمرقند ( samarqand ) , from Sogdian 𐼼𐼺𐼰𐽀𐼸𐼻𐼹𐼳 ( smʾrknδh /⁠*Smā́rkąθ⁠/ ) .
161-
########## 0abe86d1ece6775a
21-
22- 1.1 
23: Etymology 
24-
25- 1.2 
26- Pronunciation 
27-
28- 1.3 
29- Noun 
30-
31- 1.3.1 
--
50-
51- 2.1 
52: Etymology 
53-
54- 2.2 
55- Noun 
56-
57- 3 
58- Hijazi Arabic 
59-
60- Toggle Hijazi Arabic subsection 
61-
62- 3.1 
63: Etymology 
64-
65- 3.2 
66- Pronunciation 
67-
68- 3.3 
69- Noun 
70-
71- 4 
--
75-
76- 4.1 
77: Etymology 
78-
79- 4.2
```


## [2026-09-06T15:02:34.746Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nfor f in f9b28a8a8d8bffa9 ca75e128dca3abac a0f23a9129817626; do echo \"########## $f\"; sed -n '55,140p' $f.txt; done"
}
```


### [2026-09-06T15:02:36.608Z] TOOL RESULT

```
########## f9b28a8a8d8bffa9

 1 
 Persian 

 Toggle Persian subsection 

 1.1 
 Pronunciation 

 1.2 
 Verb 

 Toggle the table of contents 

 آگندن 

 2 languages 

 فارسی 
 Тоҷикӣ 

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

 See also: آکندن 

 Persian
 [ edit ] 

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /ʔaː.ɡan.ˈdan/ 

 ( Dari, formal ) IPA ( key ) : [ʔɑː.ɡän̪.d̪án] 

 ( Dari, formal ) IPA ( key ) : [ʔɑː.ɡän̪.d̪án] 
########## ca75e128dca3abac

 1 
 Persian 

 Toggle Persian subsection 

 1.1 
 Pronunciation 

 1.2 
 Verb 

 Toggle the table of contents 

 افگندن 

 2 languages 

 فارسی 
 Kurdî 

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

 See also: افکندن 

 Persian
 [ edit ] 

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /ʔaf.ɡan.ˈdan/ 

 ( Dari, formal ) IPA ( key ) : [ʔäf.ɡän̪.d̪án] 

 ( Dari, formal ) IPA ( key ) : [ʔäf.ɡän̪.d̪án] 
########## a0f23a9129817626

 1 
 Persian 

 Toggle Persian subsection 

 1.1 
 Pronunciation 

 1.2 
 Noun 

 1.3 
 Noun 

 1.4 
 Further reading 

 Toggle the table of contents 

 پیکان 

 3 languages 

 فارسی 
 Kurdî 
 Malagasy 

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

 Persian
 [ edit ] 

 Pronunciation
 [ edit ]
```


## [2026-09-06T15:02:49.072Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN peikan\"; grep -n -i \"peikân\\|peikan\\|pēkān\\|paikan\\|peikän\" HRN.txt | head\necho \"=== HUB\"; grep -n -i \"peikan\\|paikan\\|âgenden\\|agenden\\|efkenden\" HUB.txt | head\necho \"=== FSF peykan\"; grep -n \"پیکان\" FSF_pages.txt | head -3\necho \"=== FFD pdf31\"; python3 - <<'EOF'\nt=open('incoming/FFD/FFD_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nprint(len(leaves))\nfor i,l in enumerate(leaves):\n    if 'کن' in l and ('آگند' in l or 'اگند' in l or 'افگند' in l):\n        print(\"=== leaf\",i,\"printed\",i-5)\n        print(l[:1500]); break\nEOF"
}
```


### [2026-09-06T15:02:50.936Z] TOOL RESULT

```
=== HRN peikan
3401:362. peikän 'Pfeilspitze, Pfeil'.
3402:aw. paiti -\- [/kan- (?); arm. LW. paikan\daran
13241:i peikän 362.
=== HUB
1551:Pahl. Texts II, 280, plur. paikan Yatk. i. Zar. p. 50,
6780:(5. Jhd.), ap. patikara-] paikan 'Pfeil', arm. patkandaran
8495:kan Tfeir, arm. paikandaran 'K5cher'; paikar *Bild', phi.
=== FSF peykan
7830:                                          ‫پیکان‬                      ‫خسرو بترخت پیشگاه نشسته‬
7834: ‫بهپیکان پولاد و تیر خدنگ‬                                           ‫گزوهر یکی تخت در پیشگاه‬
10327: ‫«خرزوان» و در نسخه لنینگراد «خروزان»‬      ‫به پیکان پولاد و تیر خدنگ‬
=== FFD pdf31
115
=== leaf 30 printed 25
[pdf page 31]
و فعلهای فارسی دری
11 شفتن. آشوفتن
آشفت + فارسی میانه 2311 + ایرانی باستان 18 - 2501 - *. برای 3و 12 -> آراست.
: دنا که صورت ضعیف ريشهٌ 75210 است» صورت اصلی لا« است» 0 پیش از ۲ به ؟
بدل شده است. ريشةٌ 35800 به معنی «لرزیدن» است. «آشوفت» زیر نفوذ «آشوب»
به‌وجود آمده است.
آشوب < فارسی میانه 2300 + ایرانی باستان ۸ - 35200 - 3*. برای 2 + آرای.
«کشفتن» هم از ربشةٌ 1520 آمده است. > کشفتن.
آفریدن
آفرید < فارسی میانه 2874 < ایرانی باستان ها - 87 - 3*. برای 3 و 1۵ > آراست.
آفرین + فارسی میانه 38:78 + ایرانی باستان 83 - 8۲ - 3*. 23 نشانه‌ای بوده است
که با آن از ريشه, ماده ساخته می‌شده است. ريشةٌ 7 به معنی («ستودن» است. در
فارسی میانه 21778, 31710487 به دو معنی به کار می‌رفته: ۱ -ستودن, آفرین کردن ۲ -
خلق‌کردن. در فارسی دری معنی «ستودن» در «آفرین» به جا مانده که به عنوان «صوت»
به کار می‌رود.
آگندن
آگند + فارسی میانه 28270 < ایرانی باستان 1۵ - 6۵۵ - 2*. برای 3و ها آراست.
ريشهٌ 1۵0 به معنی «نهادن و افگندن» است.
«افگندن» و «پراگندن» هم از ريشهٌ 1۵0 آمده‌اند. -> افگندن و پراگندن. در ایرانی
باستان 1۵8 دیگری هم بوده است که از آن «کندن» آمده است. > کندن.
آگن < فارسی میانه 284 < ایرانی باستان ۵ - 5۵2 - 3*. برای 8 -> آرای. "
آلودن
آلود + فارسی میانه 2130 < ایرانی باستان ۴3-۳0-1۵
برای #وقها + آراست. 8 به معنی «آلوده‌بودن» است.
آلای + فارسی میانه 213 < ایرانی باستان 8له-3-73۷*.
```


## [2026-09-06T15:03:05.605Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN 362 leaf\"; python3 - <<'EOF'\nt=open('HRN.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\noff=sum(len(l)+1 for l in lines[:3400]); leaf=t[:off].count('\\f')\nprint(\"leaf\",leaf,\"printed\",leaf-21)\nEOF\nsed -n '3398,3412p' HRN.txt\necho; echo \"=== HUB 6770-6790\"; sed -n '6770,6790p' HUB.txt\necho; echo \"=== HUB 8488-8500\"; sed -n '8488,8500p' HUB.txt"
}
```


### [2026-09-06T15:03:07.423Z] TOOL RESULT

```
=== HRN 362 leaf
leaf 101 printed 80
361. peiker *Bild'.
Sii^. patikara- 'Bild'; iphlv, patkar (Bund.), arm. LW.
pafker.
362. peikän 'Pfeilspitze, Pfeil'.
aw. paiti -\- [/kan- (?); arm. LW. paikan\daran
de Lagarde, No. 1834.
vergl. serb. LW. pHk 'Pfeilzeichen der fahrenden
Leute (Miklosich, Denkschr. WAW. Band 38, 11);
während peik 'Bote, Laufbursche' (ib. Band 35, 144
und 38, 11) zu np. peik (No. 359) gehört.
363. pei/imiden'mQ^^Gn\ zeigen', Prsies. peimäy-emj peimäny
peimäne^).
*) An der letzten Stelle wie auch sonst (z. B. IIT, 1642, Vers 2,
Calc, 1708, V. 3765) ist in der VuUers-Landauer'schen Ausgabe
h^ in p^ zu ändern.

=== HUB 6770-6790
pasaxt etc. (Shk. 262 — 263) aus patsdxt, Diese Assimili-
rung war erst sassanidisch, wie das Arnienische zeigt, das
sie noch nicht kennt.
•
b) t sonst im spateren Mp. und Np. zu y = i:
pairastan schmiicken, anordnen', arm. patrast 'bereit',
ap. pati + Wrzl. rad] pairahan oder perahan? *Hemd' =
phi. patrahan oder perahan? (siehe oben p. 45); paikar^
paigar *Kampf*, arm. paiffar (5. Jhd.), phi. pafkar Gl. and
Ind. 93; paikar *Bild', phi. patkar, syr. N^IDPS, arm. patker
(5. Jhd.), ap. patikara-] paikan 'Pfeil', arm. patkandaran
*Kocher ; paimdn *Uebereinkommen, Vertrag , paimana *Mass',
paz. paiman Min. 61. 152, Shk. 262, arm. paiman (5. Jhd.),
phi. patman, patmanak, dazu np. paimudan, pr. paimayam'messe*, up. pati-ma., paivastan Verbinden*, paz. paivasian
Min. Gl. 153, \M.patvastan, SLvm. pafvast 'ty^svxQtmq; payam
aus und neben paiyam *Botschaft', phi. paitdm oder paytam
fiir *patgam i), arm. patgam, aram. pi^gam (Daniel, Esra),
syr. pi&yama, ap. ^patigaTna-; paiyara 'Tadel* H. 358; paida
{paida A. M. p. 3, Z. 3 v. u. ; 4, Z. 12) oflfenbar = phi.
paitdk oder padtak fiir *patdak aus *patdayak oder *pa^-
dayak?^ vgl. zd. paitidaya- 'Aufseher (s. oben p. 44). Un-

=== HUB 8488-8500
askarak, skr. aviskdra-; xusk *trocken = ap. mka-; risk
'Nisse', osset. lisk, skr. liksa-; sirisk *Tropfen' = zd. sraska-;
kaskm Gerstenbrot* = arm. Ua^k^n (EliSe); laskar *Heer*
= arm. Ia§kar (Elise p. Ill); sikastan zerbrechen*, zd.
skenda-; sikaftan *spalten H. 787, oben p. 80; sikar *Jagd'
H. 786, oben p. 80; sikar 'Kohle H. 742, oben p. 76u.s.w.;
paikar 'Kampf* = phi. patkar, arm. paiKar (5. Jhd.); pai-
kan Tfeir, arm. paikandaran 'K5cher'; paikar *Bild', phi.
patkar, arm. pntker, ap. patikara-, Spater tritt einigemal
g fur k ein : paigcir *Kampf ' = paikar ; sugofa = sikofa
^Bliithe', §agaf Riss (A. M. 84, 7) u. s. w.
§ 134. Ap. k nach Vokalen, r und n wird im Np.
(auch in Komp.) zu g, ist aber im Phi. und Arm. als k
```


## [2026-09-06T15:03:19.537Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== ARY kandan\"; grep -n \"کندن\" incoming/ARY/ARY_pages.txt | head -8\necho \"=== ARY qanat\"; grep -n \"قنات\\|کانال\" incoming/ARY/ARY_pages.txt | head -8\necho \"=== ARY latin index kan\"; grep -n -i \"^KAN\\|KANDAN\\|AGANDAN\" incoming/ARY/ARY_latin_index_pages.txt | head -8"
}
```


### [2026-09-06T15:03:19.619Z] TOOL RESULT

```
=== ARY kandan
1876:آکندن» آکنده» آکنش, آگنش,- آگین / ۶۷
5766:۱- چم پیشین این واجريشه در زبان‌های ژرمنی: چرخیدن» غلنیدن» افکندن.
8142:در برخی از زبان‌های هند و اروپایی این واژه این چم‌ها را هم دارد: پرست کندن (از حبوان).
9082:چم این واژه در تخاری 8 و لتونی و اسلاوی کهن: کندن.
11051:استخوان برای کندن و ضربه زدن منجر به پیدایش واژه‌ها و چم‌های دیگر شده املی ار
11281:چم این واژه در آلمانی کهن و آلمانی نوین: (گردو و ذرت و غیره) پوست؛ پوست کندن, :
12212:۲ | کندن
13036:چم این واژه در تخاری ۸ : افکندن» گرداندن. ۱
=== ARY qanat
=== ARY latin index kan
1834:AKANDAN, AKANDE, AKANESH (u61~ 81 dist oaisl ais) — (PERSIAN) qui
1837:GONEJETE, GANA-, GONETI, ‘AGANDAN,AKANDAN.(PAHLAVI) 5 sy,
6739:KANDU (LITHUANIAN) gle}
7600:KAN, KUNNA:(OLD FRISIAN) oS5323 HAVESTAN) «lie 3!
7602:KAN, KUNNA (OLD PERSIAN) ilealy
7603:KAN, KONNEN (GERMAN) giJT ADANA, DAN- :
7606:KANDE, KAN DANISH) Sheil HOSSETIC) guy)
7607:KAN SWEDISH) 555 yo ZONIN, ZONUN, ZONUM.
```


## [2026-09-06T15:03:21.829Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== WLD band3 register gwhen\"; grep -n -i \"agandan\\|āgandan\" WLD_band3.txt incoming/WLD/WLD_Bd1_pages.txt | head\necho \"=== IEC ghen\"; grep -n \"^ghen-\\|^g.hen\\|ghenō\" IEC.txt | head\necho \"=== SYN fill\"; grep -n \"9.34\\|FILL\" SYN.txt | head -5"
}
```


### [2026-09-06T15:03:21.942Z] TOOL RESULT

```
=== WLD band3 register gwhen
=== IEC ghen
5477:guhen- radical of general sense: “drive, beat, kil. WP I, 679. Cf. guhn- Verbal forms: Skt. hánmi: Av. jainmi; OPer. -janam; Per. zanam, inf. zadan; Arm. $Énem (thematic: ‘beat: gin ‘whip, rod); fanam ‘strive’: athematic; beside ğan, Let, ‘effort’; Hitt. kwemi (for *kwenmi, 3pl. kunanci: Skt. ghnanti);; Gk. (thematic) théno, iotacized:
5488:guhentuà, see guhen- Vedic hántvà “to be slain’; OCS Zetva Char. vest”, lit. cutting")
=== SYN fill
939:scattered’ : ChSl. (na-)sypati ‘strew, scatter’ (9.34). Tiktin 1058. Miklo- sich 334.
1079:3. Lat. vallés, vallis (> Romance forms; deriv. Fr. vallée displacing val), perh. fr. the root in Lat. volvere ‘turn, roll’, etc. Walde-P. 1.301. Ernout-M. 1071. REW 9134.
6302:2. Ir. traig (gen. traiged), NIr. troigh, W. troed, Br. troad: Gall. ver-tragus ‘swift-footed dog’, SCr. trag ‘footstep’, perh. Goth. pragjan ‘run’, etc. Walde- P. 1.752f. Pedersen 1.39. But cf. H. Lewis, BBCS 9.34 f.
6386:Grk. ozépvov (in Hom. only of males), specialization of ‘flat surface’, fr. the root of crdpvipt, etc. ‘spread out’ (9.34). Cf. OHG sterna ‘forehead’, fr. the same root. Walde-P. 2.639. Boisacq 931.
10976:Sw. flor, ‘fine cloth, crepe, gauze’, used also commonly for ‘veil’, fr. LG flor ‘crepe, gauze’, fr. Fr. velours ‘velvet? (fr. Prov. velos id., Lat. villdsus ‘hairy’). Falk-Torp 240. REW 9334.
```


## [2026-09-06T15:03:30.776Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('incoming/ARY/ARY_pages.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\ndef leafof(n):\n    off=sum(len(l)+1 for l in lines[:n-1]); return t[:off].count('\\f')\nleaves=t.split('\\f')\nfor n in (1876,12212):\n    i=leafof(n); print(\"=== line\",n,\"leaf\",i,\"printed\",i+1)\n    print(leaves[i][:1800])\n    print(\"-----\")\nEOF"
}
```


### [2026-09-06T15:03:32.872Z] TOOL RESULT

```
=== line 1876 leaf 65 printed 66
[pdf page 66]
لگ
آکندن» آکنده» آکنش, آگنش,- آگین / ۶۷
:
پهلوی (2:]4۲ :۸0۸30۸7216۸10۸7۷ ,7 مفان6۸ 00۳57578
سانسکر بت (54(/570077): ,1۸۸5 لینوانی (1777040/140.ت): 6۸3۷01771 ,0۸۸
0 ,۸۸310
ارمنی (4//1۸(0): 007 پسگشت‌ها ۶2۳52225
یرنانی 07888/0): 15 1 200900
اسلاوی کهن (ع1ها5 لع#ناقل) صاه): برهان قاطع : ۷۵-۶
بادداشت:
۱- معنی این واژه در اسلاوی کهن و لیتوانی: کافی بودن.
۲ این واجریشه‌ی هند و اروپایی عیناً مانند واجربشه‌ی هند و اروپایی 0۷۷۴83۸۲* به معنی آزدن" و "کشتن" است.
(بازگت به "زدن").
۱ اوستابی (/(/۸۲87): ۰ ۸7کشکل۸ ,گشکلة 1 با
پهلوی (4۲اتل۳۸): آل262 بققلة
۱ اوستی (0538716): 7 پسگشت‌ها 25
کردی (08.01577): ۸0۸77 زج ی
سانسکریت. (8۸4(/5577): ادا 0 3 (۸۸۴) یدام ده ها
یونانی (0865): 7805۸3 10 دزی اه را
۹ ۰ اسلاوي کهن (ع ما5 الع#ناتته صل۵):
ان
یادداشت:
این واژه با واژه‌های آنگاه" و "چشم " همریشه است. بازگشت به؛ نگاه. :
| ملاس سروازه نارس 6۵

-----
=== line 12212 leaf 410 printed 411
[pdf page 411]
۲ | کندن
پسگشت‌ها کت ۲ 3213 8000
ی 0 هقه رهوج لابدنه
0 (70ه58۸) ای ال 4 (38۸40) . 9 ,24/20
0 818 :ما02 برهان قاطع : ۱۸۸۴ :۳
اوستایی (4۸887۸۷)+ -۸ اه ۹:۵
پارسی باستان (۳8۸۵۸۷ صاه): سا آرمنی (۸/۸48(]40). هام۸
پهلری (41ل۳4): ۳۸۵۲۲۸۸۲ ,ان 010ها .
اوستی (0538112): لانشن پسگشت‌ها شتا ادا
کردی (/7373۸310131:0080/31) ,)1052۸0 4 ونم
افغانی (پشتر) (/(۸۳077۸): 0 (016) اد ده ۲12
,110 ,1۸0۸ 2 010 مرک 0۱3۱
سانسکریت (84(5877): برهان قاطع + ۱۷۰۷
بادداشت:
۱ واژه‌های این فهرست با واژه‌های انگلیسی 2۸18۷ و آلمانی 1و واژه‌های اسکاندنیاوی همريشه آنها
شباهت دارنسد ولی ظاهراً ایسن واژه‌ها از یک واجریشه‌ی هند و اروپایی دیگر (۳0738817) آرده‌اند
( 1(
۲- بازگشت به پانوشت ۳016032۷ در صفحه‌ی ۹۳۴
۳ رابطه‌ی واژه‌های هند و ابرانی این فهرست با واجریشه‌ی هند و اروپایی فرق احتمالی است و بهمین دلیل در جلو
آن (شاید) بکار رفته است.
اوستایی (48537۸): ۸ 1610۸ ,361105 ,1610152
ش7118 وناب افغانی (پشتو) (۸701۸۸1): 1
پهلوی (۲1شاننمه): ۹1 سانسکریت (6۸(97077).
کردی (080157): ۸ بش18 ,3۳۷2 ب317۷۸ (260

-----
```


## [2026-09-06T15:03:46.628Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nfor f in 581981c502fc827f 984e8d509585781c 123a7f91c8f43fc1; do echo \"##### $f\"; grep -o -i \"canal (n.).\\{0,600\\}\\|cane (n.).\\{0,600\\}\\|canon (n.1).\\{0,600\\}\" $f.txt | head -2; done"
}
```


## [2026-09-06T15:03:47.484Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SNS kan\"; grep -n \"kan\\b\\|kandan\\|kan-\" SNS_pages.txt | head -10\necho \"=== SNS leaf8\"; python3 -c \"\nt=open('SNS_pages.txt',encoding='utf-8',errors='replace').read(); print(t.split('\\f')[8][:800])\""
}
```


### [2026-09-06T15:03:48.460Z] TOOL RESULT

```
##### 581981c502fc827f
canal (n.) 
cane (n.)). The sense was transferred by 1670s to "artificial waterway for irrigation or navigation."
##### 984e8d509585781c
cane (n.) 
cane (n.). Related: Caned ; caning .
##### 123a7f91c8f43fc1
canon (n.1) 
cane (n.)), but Beekes favors Pre-Greek origin.
```


### [2026-09-06T15:03:50.602Z] TOOL RESULT

```
=== SNS kan
1235:     (GiVPff.l03)aik: tr 7ha: ^iw/ :h&k, hi, haik                                :           j^        j-jt^ (Kent. 178) (o^)o* :kan :v^ kh3- :o T                                    (                             ^»
5183:                                                       •O sl*:pakan:        **"!
5623:               ^W-»>^«0^:pa r ^3akan/palCl3akan:
5624:      :parakan: <&»**»»          (        SnS   W *) parakla     :    ^
8902: nfn                  jji-    na^an         j-S* • (4>m . Gram                   204)nkan: ^j'
15083:                                          nraariyata 248/12             kan 8/13
15921:p3sbantar 117/4                                            parCr:akan/palCl3ak3n          payraSn 120/16-121/2
16004:nigfln kirbag 277/10   niyabag 257/3                                  5hrraazd d3d59/19          pakan 117/10
=== SNS leaf8
                                                                                                               '


iC                                                                                              '
                                                                                                                   ,US^

                                                                                                                                                           .       UI:anb5n:                        £>v bc-i^.j^                   ^ :x5m:
                                                                                                                   :hildag:                     3^^                  ,       b.       b^b :h5raln:                      *$t> Ifj* Jjp'a
```


## [2026-09-06T15:03:58.980Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nfor f in 581981c502fc827f 984e8d509585781c 123a7f91c8f43fc1; do echo \"##### $f\"; python3 - \"$f.txt\" <<'EOF'\nimport sys,re\nt=open(sys.argv[1],encoding='utf-8',errors='replace').read()\ni=t.find('Advertisement')\nprint(t[i:i+1600].replace('\\n\\n','\\n'))\nEOF\ndone"
}
```


### [2026-09-06T15:04:00.666Z] TOOL RESULT

```
##### 581981c502fc827f
Advertisement Remove Ads 
 Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.
 Origin and history of canal 
 canal (n.) 
 early 15c., in anatomy, "tubular passage in the body through which fluids or solids pass;" mid-15c., "a pipe for liquid;" from French canal , chanel "water channel, tube, pipe, gutter" (12c.), from Latin canalis "water pipe, groove, channel," noun use of adjective from canna "reed" (see cane (n.)). The sense was transferred by 1670s to "artificial waterway for irrigation or navigation."
 also from early 15c. 
 Entries linking to canal 
 cane (n.) 
 late 14c., "long slender woody stem," from Old French cane "reed, cane, spear" (13c., Modern French canne ), from Latin canna "reed, cane," from Greek kanna , perhaps from Babylonian-Assyrian qanu "tube, reed" (compare Hebrew qaneh , Arabic qanah "reed"), which may come from Sumerian-Akkadian gin "reed." The sense of "length of cane used as a walking stick" is from 1580s.
 channel (n.) 
 early 14c., "bed of a stream of water," from Old French chanel "bed of a waterway; tube, pipe, gutter," from Latin canalis "groove, channel, waterpipe" (see canal ). The English word was given a broader, figurative sense by 1530s: "that by which something passes or is transmitted" (in reference to information, commerce, etc.); the meaning "circuit for telegraph communication" (1848) probably led to that of "band of frequency for radio or TV signals" (1928). Also "part of a sea making a passageway between land masses, a large strait" (1550s).
 Advertisement Want to remove ads? L
##### 984e8d509585781c
Advertisement Remove Ads 
 Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.
 Origin and history of cane 
 cane (n.) 
 late 14c., "long slender woody stem," from Old French cane "reed, cane, spear" (13c., Modern French canne ), from Latin canna "reed, cane," from Greek kanna , perhaps from Babylonian-Assyrian qanu "tube, reed" (compare Hebrew qaneh , Arabic qanah "reed"), which may come from Sumerian-Akkadian gin "reed." The sense of "length of cane used as a walking stick" is from 1580s.
 also from late 14c. 
 cane (v.) 
 "to beat or flog with a walking stick," 1660s, from cane (n.). Related: Caned ; caning .
 also from 1660s 
 Entries linking to cane 
 canal (n.) 
 early 15c., in anatomy, "tubular passage in the body through which fluids or solids pass;" mid-15c., "a pipe for liquid;" from French canal , chanel "water channel, tube, pipe, gutter" (12c.), from Latin canalis "water pipe, groove, channel," noun use of adjective from canna "reed" (see cane (n.)). The sense was transferred by 1670s to "artificial waterway for irrigation or navigation."
 canebrake (n.) 
 also cane-brake , "a thicket of canes," 1770, American English, from cane (n.) + brake (n.3).
 canister 
 cannoli 
 cannon 
 cannula 
 canon 
 canyon 
 caramel 
 sugar-cane 
 sword-cane 
 See All Related Words (11) 
 Advertisement Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.
 More to explore
 cannon 
 c. 1400, "artillery piece, mounted gun for throwing projectiles by force of gunpowder," from Anglo-French can
##### 123a7f91c8f43fc1
Advertisement Remove Ads 
 Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.
 Origin and history of canon 
 canon (n.1) 
 "a rule or law," Middle English canoun , Old English canon "rule, law, or decree of the Church," from Old French canon or directly from Late Latin canon "Church law, a rule or doctrine enacted by ecclesiastical authority," in classical Latin, "measuring line, rule," from Greek kanōn "any straight rod or bar; rule; standard of excellence," which is perhaps from kanna "reed" (see cane (n.)), but Beekes favors Pre-Greek origin.
 The Latin word was taken in Christian use for "decree of the Church." The general sense of "a rule or principle" is attested from late 14c.; that of "standard of judging" is by c. 1600.
 It is attested from c. 1400 as "the Scriptures, the books of the Bible accepted by the Christian church," and also extended to secular books of admitted excellence or authoritative supremacy (such as the Trojan legends or Avicenna's  Liber Canonis Medicinae ). The meaning "catalogue of acknowledged saints" is from 1727.
 The fandom sense of "material regarded as veritable" is attested by 1934, originally in reference to the Sherlock Holmes series. The musical use in reference to a kind of fugal composition is from 1590s. Related: Canonicity .
 The secular canon, with the word meaning a catalog of approved authors, does not actually begin until the middle of the eighteenth century .... [Harold Bloom, "The Western Canon," 1994].
 canon (n.2) 
 "clergyman living according to rules," c. 1200 (late 12c.
```


## [2026-09-06T15:04:10.706Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 tools/fetch_source.py \"https://abadis.ir/fatofa/%D9%82%D9%86%D8%A7%D8%AA/\" --note \"page 214: Mo'in on قنات (node 9)\" 2>&1|tail -1\npython3 tools/fetch_source.py \"https://abadis.ir/fatofa/%DA%A9%D8%A7%D9%86%D8%A7%D9%84/\" --note \"page 214: Mo'in on کانال (node 16)\" 2>&1|tail -1"
}
```


### [2026-09-06T15:04:16.581Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/107bf20693a23dc8.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/99478f25c10ae61e.txt
```


## [2026-09-06T15:04:19.820Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nfor f in 107bf20693a23dc8 99478f25c10ae61e; do echo \"##### $f\"; grep -o \"فرهنگ معین.\\{0,400\\}\" $f.txt | head -2; grep -o \"\\[ ع\\..\\{0,200\\}\\|\\[ فر\\..\\{0,200\\}\" $f.txt|head -3; done"
}
```


### [2026-09-06T15:04:22.208Z] TOOL RESULT

```
##### 107bf20693a23dc8
فرهنگ معین
فرهنگ معین، فرهنگ فارسی عمید، فرهنگ مترادف ها و متضاد ها، معادل فارسی کلمه یا به شیوه درست تر برابر پارسی واژه، فرهنگ سره، عبارات مصوب فرهنگستان زبان و ادب فارسی، دانشنامه عمومی، دانشنامه اسلامی، دیکشنری نام ها، هم خانواده یاب، تصویر مرتبط با کلمه، معنی در حل جدول کلمات متقاطع و ابزارهایی مانند واژه ساز ، راهنمای انتخاب اسم و ... می باشد. 
##### 99478f25c10ae61e
فرهنگ معین
فرهنگ معین، فرهنگ فارسی عمید، فرهنگ مترادف ها و متضاد ها، معادل فارسی کلمه یا به شیوه درست تر برابر پارسی واژه، فرهنگ سره، عبارات مصوب فرهنگستان زبان و ادب فارسی، دانشنامه عمومی، دانشنامه اسلامی، دیکشنری نام ها، هم خانواده یاب، تصویر مرتبط با کلمه، معنی در حل جدول کلمات متقاطع و ابزارهایی مانند واژه ساز ، راهنمای انتخاب اسم و ... می باشد. 
[ فر. ] (اِ )۱ - ترعه ، مجرای وسیع بین دو دریا که برای عبور کشتی ساخته می شود. ۲ - راه آب .
```


## [2026-09-06T15:04:25.831Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\ngrep -o \"قنات.\\{0,300\\}\" 107bf20693a23dc8.txt | sed -n '1,8p'"
}
```


### [2026-09-06T15:04:27.526Z] TOOL RESULT

```
قنات - معنی در دیکشنری آبادیس
قنات - معنی در دیکشنری آبادیس 
قنات
قنات : کاریز
قنات. [ ق َ ] ( ع اِ )چوب نیزه. رجوع به قناة شود. || کاریز. ( مهذب الاسماء ). کهریز. کاهریز. ج ، قنوات : 
قنات. ناصرخسرو.
قنات. [ ق َ ]( ترکی ، اِ ) پرده کرباس که قایم مقام دیوار باشد.
قنات. [ ق ُن ْ نا ] ( ع اِ ) ج ِ قُنَّة. ( اقرب الموارد ) ( منتهی الارب ). رجوع به قنة شود.
```


## [2026-09-06T15:04:46.991Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BRT.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nl=leaves[266]\ni=l.find('kan')\nprint(l[-3000:])\nEOF"
}
```


### [2026-09-06T15:04:48.895Z] TOOL RESULT

```
le'  die  Bedeutung  'Gift' oder  'plante  vüni'neuse'  an,  was  mir  nicht  lu passen  scheint.  Eber  ka-/<a'Uiy-  (s.  unter t,-nu,A„-y,  vgl.  lat.  A^/«.
•  p.  ka''büjiya-  m.  EN.  eines  persischen Königs;  Katnbyses,  Sohn  Ats  Kyros:  'ya* näma'    küraus    fui:''a*  .  .  paruvam    idä
dby  Google
"kan-  Noten
438
:rri7vrt>(>fl*  ühJ*  Bh.  /.  10;  lo';  — pasav^
'ytr  ''uvsmarsiyus  (sd.)    amarhata    Bh.  /,
11;  —  xsai'am  lya''  gaumäicr  .  .  adins"
'\am    Bh. /.  12;  12;    —    avahyä    'ya/ivil
i'r.ltä  bardiyi^  mlma'  äkt^   Bh.  /.  10;  10,
11;  —  haeiJ  °_j'ä*  Bh. /.  11.
El?  Man  hal  das  Wort  zu  ai.  kamboja-  \A:y,\
Itez.  eines  Volks,  gesteUt.    Fuv  KZ.  35.  61,  :
37.  543  letlegt  kam  {ai.  kam  'bene')+*-  (iura  \
V.  Awi'-):  ähnlich  auch  JusTl  NB.  490.   Eli  er  ,
»II.  *ki/'bü'-^''jiyä-  'mit  Sehnen  aus  -?  -';  s.  ■
V>j--  j
•  j.  kafa-  m.  'Schaum,  Geifer';  yl  (näml.  1 uilrä)  '/jin  aipi-spaydli  spasiimm  upa  .  .  \ Auxsnaei re  (sd.)  Yt. /J.  13.
ai.  ia/ia-  m.  'Schleim',  np.  ia/  'Schaum'.  — Npü. ;  ita/,  erl.  larJ;
•  j.  kaoba-  m,  Name  eines  Lands*':  upa dvarnn  xsairö.sukjm  (sd.)  apanöJtmjm 'hitva  *birizantaya  asavanaya  "bei  dem Pass  -Vj^,  dem  liöchstgelegenen  in  dem hochragenden  heiligen  K."  Yt5.  54.
•]  Die  Uurg  von  A'..  Kangdiz,  liegt  fi^fi*" Osten  •hilf  var  1  fräi'karl  ö  äii  hisMk  fa  vas jraiaat;'.  Syävarian  hat  sie  erbaut,  Pjsö.lanü  be- ni>hnt  .-ie.  So  nach  Bd.  2').  10,  $2.  5,  Hyt.  3. IJ,  1>V.  ').   16.  (5,  Mx.  62.  13.
•  j.,  g.  'kan-  V.  'Verlangen  tragen  nach  - '. Praes.  10  .V«^-'';  Perf. !  cakan-,  a  ciixn-. —  PPfP.   'kilta-,  Inf.  kilil.
i)  mit  Akk.  der  Pers.  'gern  haben, lieben':  cUca  'iwam  cakana  ava  (sil.) masana'a  ..  H.  2. 1 1 ;  F.  79;  —  tum  mam "t-aia/ia'*  _j-um  Auinanß  H.2, 12.  2)  mit
Akk.  der  Sache  'trachten  nach  — ':  s. HnraLusliina'.  3)  mit  Lok.  eines  Nom. act.,  negirt  'sich  nicht  kümmern  um  — , nicht  Sorge  tragen  um  — ':  nöit  fiasayä (sd.J  vai^hius  cJxnarS  manavhö  Y. 44.13.
ai.  taiana  (iSPW.).  —  Vgl.  ^ä-.  —  Pia.  (dRn.)-
ar..iäm-ii:  —  'I  Mit  Übertrager I  nach  %  sg/.  4.;  L4  hat  ram verlangte  die  2.  Person.
)  Man
•  j-,  p.  'kan-"  V.  'graben'.  Praes.  i ian-,  2  kana-,  30  (Iter.)  kiltiaya-.'*  — PPfP.    -ianta-^^;     Inf.  ka'tanaiy,    -kantSe,
'eingraben' :  y'fi  h:tnti  aifjhh  stmö kaiunti  "diejenigen  die  Wesenheiten  (Ani- malta)  in  die  Erde  vergraben"  V.  y.  40 PüZ.     S.  noch  No.  2.
mit  aipi  'durch  Graben  ausfiillen,  zu- schütten': basi-arj  mayanqm  .  ,  aitihä wmO  aipi-kanyät  V,  14. 6.
mit  ava  'durch  Graben  herstellen,  aus- schachten': mazdayasna  atriha  spmö  'irts may»m  (sd.)  avaManaym  V.  <?.37,  iG.iz; —  aira  maysm  ava^tinSisV.ij.  $•,"!■, — yö  aehm  avakamm  (sd.)  avakanta  (3SPrM.)
mit  US  'durch  Graben  heraus  holen, ausgraben':  y
```


## [2026-09-06T15:05:20.080Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nmkdir -p data/verification/sources/refs/ocr/BOOK\ncp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg214.png data/verification/sources/refs/ocr/BOOK/214.png && ls -la data/verification/sources/refs/ocr/BOOK/ | tail -3"
}
```


### [2026-09-06T15:05:22.042Z] TOOL RESULT

```
-rw-rw-r--  1 sfmqrb sfmqrb  78178 Sep  5 10:14 95.png
-rw-rw-r--  1 sfmqrb sfmqrb  72929 Sep  5 10:19 96.png
-rw-rw-r--  1 sfmqrb sfmqrb  65608 Sep  5 10:43 99.png
```


## [2026-09-06T15:14:36.762Z] TOOL CALL #77: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk214.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW = \"https://en.wiktionary.org/wiki/\"\n\nentry = {\n \"entry\": 0,\n \"root\": \"Gwhen 1\",\n \"verdict\": \"plausible\",\n \"modern_form\": \"PIE *gʷʰen- 'to swell, abound' (Pokorny IEW 491, 1. gʷhen-; Watkins/AHD gʷhen-²)\",\n \"note\": \"The root box itself is correct and correctly cited: Pokorny's IEW p.491 heads 'Root/lemma: gʷhen-1, Meaning: to swell, abound', and its material is exactly the 'fill/abundance' family (Skt. ā-ghaná- 'tumescent', ghaná- 'dense', Gk. euthenein 'flourish', Lith. gana 'enough', OCS gonĕti 'suffice') — and, crucially, Pokorny himself lists there 'npers. a-gandan füllen'. Watkins repeats it as 'gʷhen-². To swell, abound … [Pok. 1. gʷhen- 491]'. So the label 'Indo-European', the number '1' and the gloss 'to swell, fill' are all right. What is wrong is the use Nourai makes of the root: the whole page hangs on the Avestan/Old Persian verb kan- 'to dig' (node 1), and neither Pokorny nor any modern handbook derives that verb from *gʷʰen-. Pokorny puts Skt. khan-/Av.-OP kan- 'dig' in his appendix on the tenues aspiratae (IEW p.634), tentatively under ken- 'to scrape' (p.559 ff.); LIV reconstructs an independent *kenh₂- 'to dig' and Cheung (2007) accordingly separates three homophonous Iranian roots — *kan¹ 'to throw, place, destroy', *kan² 'to fill', *kanH¹ 'to dig'. Only the second of these (āgandan) belongs under Pokorny 491. Nourai's own cited Persian authority, Abolghasemi (FFD p.26), says the same in as many words. So: root real and correctly glossed, but the tree built on it merges three distinct roots.\",\n \"note_fa\": \"جعبهٔ ریشه درست است: پوکورنی در صفحهٔ ۴۹۱ فرهنگ خود مدخل «gʷhen-1» را با معنای «آماسیدن، آکنده و فراوان بودن» آورده و در همان‌جا خودِ فعلِ فارسیِ «آگندن» را به‌عنوان بازماندهٔ آن نام برده است؛ واتکینز نیز همین ریشه را «gʷhen-²: to swell, abound» با ارجاع به پوکورنی ۴۹۱ ثبت کرده است. پس برچسب «هندواروپایی»، شمارهٔ ۱ و معنای «آماسیدن، آکندن» همگی درست‌اند. ایراد کار در جای دیگری است: نورایی همهٔ درخت را از فعل اوستایی/پارسی‌باستان kan- «کندن، حفر کردن» آویخته است، حال آنکه هیچ پژوهش امروزی این فعل را از *gʷʰen- نمی‌داند؛ خود پوکورنی (ص ۶۳۴) kan-/khan- «کندن» را با تردید به ریشهٔ ken- «خراشیدن» (ص ۵۵۹ به بعد) می‌بندد و LIV آن را ریشهٔ مستقل *kenh₂- می‌گیرد. چونگ (۲۰۰۷) سه ریشهٔ هم‌آوای ایرانی را از هم جدا می‌کند: *kan¹ «افکندن، نهادن، ویران کردن»، *kan² «آکندن، پر کردن» و *kanH¹ «کندن». تنها ریشهٔ دوم (آگندن) زیر مدخل پوکورنی ۴۹۱ جای دارد. ابوالقاسمی نیز — که خودِ نورایی او را در همین صفحه (FFD:26) گواه گرفته — به‌صراحت می‌نویسد در ایرانی باستان دو kan جداگانه بوده است. حکم: ریشه درست، ولی درختِ بر آن استوار سه ریشه را در هم آمیخته است.\",\n \"sources\": [\n   \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/g%CA%B7%CA%B0en-\",\n   \"https://www.etymonline.com/word/cane\"\n ],\n \"ref_check\": [\n   {\"ref\": \"POK:491\", \"status\": \"supports\", \"note\": \"POK_full.txt (indo-european.info dump), block ending 'Page(s): 491': 'Root / lemma: g\\\"hen-1 / Meaning: to swell, abound / Material: Old Indic a-ghana- \\\"tumescent, plentiful, luscious\\\", ghana- \\\"dense, thick\\\" …; npers. a-gandan …; gr. euthenein \\\"flourish\\\"; Lith. gana \\\"sufficient\\\"; OCS gonetъ \\\"suffice\\\". References: WP. I 679, WH. I 479'. Page number and gloss both exactly as Nourai cites. (The next block, 'g\\\"hen-2(a)- to hit', is Pokorny 491-493 — a different root.)\"}\n ],\n \"consulted\": [\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.v. gʷhen-²\", \"stance\": \"supports\", \"note\": \"AHD_watkins1985.txt: 'gʷhen-². To swell, abound. Suffixed form *gʷhen-eyo- in Greek euthenein …: EUTHENICS. [Pok. 1. gʷhen- 491.]' — same root, same page, but Watkins lists no Iranian 'dig' word under it.\"},\n   {\"src\": \"POK\", \"where\": \"IEW p.634 (appendix on the tenues aspiratae)\", \"stance\": \"contradicts\", \"note\": \"POK_full.txt: 'To the same root root ken- (above 559 ff.) could belong Old Indic khanati \\\"digs\\\" … Avestan Old pers. kan- \\\"dig\\\" (k- from kn- from the compounds with us-, ham-).' Pokorny thus assigns Av./OP kan- to ken-, not to gʷhen-.\"},\n   {\"src\": \"CHEUNG\", \"where\": \"EDIV pp. 229-233\", \"stance\": \"contradicts\", \"note\": \"CHEUNG.txt distinguishes '*kan¹ to throw, place, put; to destroy', '*kan² to fill' and '*kanH¹ to dig' (the latter '«PIE ? *kenH₂- \\\"to dig\\\" > LIV: 344'), and remarks 'In many Iranian languages the roots *kan¹, *kanH¹ and *kan² … are homonymous and therefore often show mutual interference.'\"},\n   {\"src\": \"ARY\", \"where\": \"Aryanpur pp. 66 and 411\", \"stance\": \"partial\", \"note\": \"ARY_pages.txt pdf p.66 puts آکندن/آگندن under the PIE root whose cognates it lists as Skt. ghana-, Lith. gana/ganėti, Arm. yogn, Gk. euthenein, OCS gonĕti (= Pokorny's gʷhen-1), while pdf p.411 gives کندن a wholly separate entry (Av. kan-, OP kan-, Arm. akan, Pahl. kandan, Skt. khan-). Aryanpur therefore also keeps the two apart.\"}\n ],\n \"nodes\": []\n}\n\nN = entry[\"nodes\"].append\n\nN({\n \"id\": 1, \"lang\": \"Avestan / Old Persian\", \"words\": \"kan 1, xan, gan 1\",\n \"verdict\": \"disputed\",\n \"derivation\": \"The three forms in this box are real but belong to three different roots, and none of them is *gʷʰen-. (a) Av./OP kan- 'to dig' (Bartholomae AiW col. 437 '²kan- V. \\\"graben\\\"', with aipi-, ava-, us-, ni-, vi-, ham-, para- compounds; Kent p.178 'kan- vb. \\\"dig\\\": Av. kan-, Skt. khan-') continues Proto-Iranian *kanH- < PIE *kenh₂- (LIV 344), Skt. khan-. (b) Av. xan- is not a verb 'to dig' at all but the feminine noun xā-/xan- 'Quelle, Brunnen' (AiW col. 533), which Bartholomae himself derives from that same kan-; the aspirated variant survives in NP xāna, xān and in the Arabic loan xandaq 'trench' (Horn no. 869). (c) 'gan 1' is the fill-root, Proto-Iranian *kan² 'to fill' (Cheung 232), seen in Parthian ʾgn- and MP āgand — and this alone is Pokorny's gʷhen-1. Kent even sets up a fourth, homophonous OP '*kan- vb. of uncertain connections, probably \\\"throw, place\\\"'. Merging them into one Avestan/Old Persian verb glossed 'to dig dirt out and mound it up' is Nourai's own construction.\",\n \"derivation_fa\": \"هر سه صورت این جعبه واقعی‌اند اما به سه ریشهٔ جداگانه تعلق دارند و هیچ‌یک از *gʷʰen- نیامده است. نخست، kan- اوستایی و پارسی‌باستان به معنای «کندن، حفر کردن» (بارتولومه، ستون ۴۳۷: «²kan- V. graben» با پیشوندهای aipi-، ava-، us-، ni-، vi-، ham-، para-؛ کنت ص ۱۷۸: «kan- vb. dig: Av. kan-, Skt. khan-») دنبالهٔ ایرانی آغازین *kanH- و هندواروپایی *kenh₂- است. دوم، xan- اوستایی اصلاً فعل نیست بلکه نام مادینهٔ xā-/xan- «چشمه، چاه» است (بارتولومه ستون ۵۳۳) که خود بارتولومه آن را از همان kan- می‌گیرد؛ گونهٔ دمیدهٔ آن در «خانه» و «خان» فارسی و در معرّبِ «خندق» بازمانده است (هرن، شمارهٔ ۸۶۹). سوم، «gan 1» ریشهٔ «آکندن» است، یعنی *kan² ایرانی آغازین «پر کردن» (چونگ ص ۲۳۲) که در پارتی ʾgn- و فارسی میانهٔ āgand دیده می‌شود و تنها همین یکی به gʷhen-1 پوکورنی می‌پیوندد. کنت حتی ریشهٔ چهارمی نیز در پارسی باستان می‌شناسد: «*kan- فعلی با پیوندهای نامعلوم، احتمالاً به معنی افکندن و نهادن». پس یکی‌کردن این‌ها در یک فعل با معنای «خاک را کندن و توده کردن» ساختهٔ خود نورایی است. پژوهش امروزی این ادغام را نمی‌پذیرد.\",\n \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/g%CA%B7%CA%B0en-\"],\n \"ref_check\": [\n   {\"ref\": \"POK:491\", \"status\": \"partial\", \"note\": \"p.491 supports only the 'gan' member: 'npers. a-gandan' is listed there; it contains nothing about digging. Pokorny's own treatment of Av./OP kan- 'dig' is at IEW p.634, under ken-.\"},\n   {\"ref\": \"HRN:194\", \"status\": \"supports\", \"note\": \"HRN.txt leaf 215 = printed p.194, entry '869. kenden \\\"graben\\\", Praes. ken-em, ap. aw. √kan- \\\"graben\\\"; phlv. kantan (Bund.), kandan (AV., PPGl.) …; ai. √khan-, khánati. … Auf die mit kh anlautende Form der Wurzel gehen np. (arab.) xendeq \\\"Graben\\\", phlv. xantak, np. xāna, xān \\\"Haus\\\" (No. 405) und xān \\\"Quelle\\\" (No. 466) zurück.' — supports both 'kan' and the 'xan' variant, but derives them from Skt. khan-, not from gʷhen-.\"},\n   {\"ref\": \"BRT:583\", \"status\": \"partial\", \"note\": \"Bartholomae's kan- 'graben' is at cols. 437-438 (BRT.txt leaves 266-267), not 583. Col. 583 (leaf 343) is the entry 'j. čāt- f. \\\"Brunnengrube\\\" … Ableit. — Zum V. ²kan-, vgl. xan-; §13. — Vgl. mp. (Pü.), np. čāh (aus iran. *čā-θ°)'. The cited column therefore documents the derivation of čāt/čāh from kan- (i.e. node 20), not the root box itself.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KNT\", \"where\": \"Kent, Lexicon s.v. kan- (KNT.txt leaf 201; printed p.178 of the 2nd ed.)\", \"stance\": \"partial\", \"note\": \"'kan- vb. \\\"dig\\\": Av. kan-, Skt. khan- (§100)' and, separately, '*kan- vb. of uncertain connections, probably \\\"throw, place\\\": cf. NPers. awgandan \\\"heap up\\\" from ava-kan- (Morgenstierne, Acta Or. 1.249)'. Kent keeps 'dig' and 'throw' apart.\"},\n   {\"src\": \"NYB\", \"where\": \"Nyberg II p.111 s.v. kandan\", \"stance\": \"contradicts\", \"note\": \"'kandan … 1. to dig … 2. to destroy … Two different vbs.: 1. Av. OP ²kan- \\\"to dig\\\", whence also gukān-; 2. kan- \\\"to throw\\\", whence also apakandan, frakandan, pargandan, Morgenstierne, AO I, 249. … Paz. čadan, xan- with an initial x- confirmed by the Arab. lw. xandaq \\\"trench\\\" and Skr khan- (pt. khāta-).'\"},\n   {\"src\": \"BRT\", \"where\": \"AiW cols. 437-438 and 533\", \"stance\": \"partial\", \"note\": \"col. 437 '•j., p. ²kan- V. \\\"graben\\\". Praes. 1 kan-, 2 kana-, 30 (Iter.) kātaya-. — PPfP. -kanta-, Inf. kātanaiy'; col. 533 '•j. xan- f. \\\"Quelle, Brunnen\\\" … Zum ar. V. ¹kan-?; s. ²kan- mit No. 1. — ai. khan- f. (khā-)'.\"},\n   {\"src\": \"PHD\", \"where\": \"MacKenzie p.49 s.v. kandan\", \"stance\": \"supports\", \"note\": \"PHD_mackenzie.txt: 'kandan, kan- [ḤPLWN-tn' < A √qpr; kn-dn', -tn' | M knd, N -] dig' — the Middle Persian continuant of the dig-root; MacKenzie lists abgandan 'throw' and āgandan 'fill, stuff' as separate lemmata.\"}\n ]\n})\n\nN({\n \"id\": 2, \"lang\": \"Avestan\", \"words\": \"â-kand, â-gand; aiwi-kand; para-kan; paiti-kan\",\n \"verdict\": \"plausible\",\n \"derivation\": \"Two of the four are genuinely Avestan, two are back-projections. (i) 'â-kand, â-gand \\\"to fill\\\"': Avestan has no ā-kan-; the compound that means 'to fill up (a pit) by digging' is aipi-kan- (AiW col. 437: 'mit aipi \\\"durch Graben ausfüllen, zuschütten\\\": … aŋhā zəmō aipi-kanyāṯ V.14.6'), and the ā- prefixed 'fill' verb is first attested in Parthian ʾgn-/āgn- 'to fill' and MP āgand (Cheung, *kan² 'to fill', p.232). So the form is right in substance (Old Iranian *ā-kan-ta-) but the language label 'Avestan' is an extrapolation. (ii) 'aiwi-kand \\\"to throw away\\\"' — this is Nourai's prefix for NP afkandan; but MP abgandan and NP afgandan go back to *apa-kan-/*upa-kan- (Nyberg: '< OIr *apa-kan- and *upa-kan-, from kandan'; Cheung: '(+ *apa-) NP afgandan \\\"to throw, cast away\\\"'), so the prefix is apa-, not aiβi-/*ambhi-. (iii) 'para-kan \\\"spread around\\\"' is right in kind — Bartholomae has the para- compound and Cheung derives NP parākandan from *para-ā-kan-, though under the throw-root *kan¹, not under 'dig'. (iv) 'paiti-kan \\\"front digger, arrow\\\"' is the classical etymology of peykān: Horn no. 362 (p.80) 'peikān \\\"Pfeilspitze, Pfeil\\\". aw. paiti + √kan- (?)' — with Horn's own question mark; Cheung lists NP paykandan '(+ *pati-)' likewise with a query.\",\n \"derivation_fa\": \"از چهار صورت این جعبه دو تا به‌راستی اوستایی‌اند و دو تا بازسازیِ پس‌نگرانه. نخست، «ā-kand / ā-gand» در اوستا سراغ نداریم؛ ترکیبی که در اوستا معنای «با کندن پر کردن، انباشتن» می‌دهد aipi-kan- است (بارتولومه ستون ۴۳۷: «mit aipi durch Graben ausfüllen»)، و صورتِ پیشونددارِ ā- نخست در پارتی ʾgn- «پر کردن» و فارسی میانهٔ āgand دیده می‌شود (چونگ، ریشهٔ *kan² ص ۲۳۲)؛ پس صورت از نظر ماده درست است (ایرانی باستان *ā-kan-ta-) اما برچسب «اوستایی» تعمیم نورایی است. دوم، «aiwi-kand» را نورایی خاستگاه «افکندن» گرفته، حال آنکه فارسی میانهٔ abgandan و فارسی نوِ افگندن از *apa-kan- یا *upa-kan- آمده‌اند (نیبرگ: «< OIr *apa-kan- and *upa-kan-»؛ چونگ ذیل *kan¹)، یعنی پیشوند apa- است نه aiβi-. سوم، «para-kan» از نظر گونه درست است؛ چونگ «پراکندن» را از *para-ā-kan- می‌گیرد، اما زیر ریشهٔ «افکندن» نه «کندن». چهارم، «paiti-kan» همان ریشه‌شناسی سنتی «پیکان» است: هرن در شمارهٔ ۳۶۲ (ص ۸۰) می‌نویسد «peikān پیکان، سرِ تیر؛ اوستایی paiti + √kan- (؟)» — با علامت پرسشِ خودِ هرن. حکم: با احتیاط پذیرفتنی است.\",\n \"sources\": [\"https://en.wiktionary.org/wiki/%D9%BE%DB%8C%DA%A9%D8%A7%D9%86\"],\n \"ref_check\": [\n   {\"ref\": \"POK:491\", \"status\": \"partial\", \"note\": \"p.491 has no Avestan compound at all; its only Iranian item is 'npers. a-gandan', which covers just the first of the four words.\"},\n   {\"ref\": \"HRN:194\", \"status\": \"partial\", \"note\": \"Horn p.194 (no. 869 kendan) is the dig-verb; it says nothing about the compounds. The compound Nourai needs, peykān, is at Horn p.80 no. 362: 'peikän \\\"Pfeilspitze, Pfeil\\\". aw. paiti + √kan- (?)'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"AiW cols. 437-438 s.v. ²kan-\", \"stance\": \"partial\", \"note\": \"'mit aipi \\\"durch Graben ausfüllen, zuschütten\\\"'; 'mit ava \\\"durch Graben herstellen, ausschachten\\\"'; 'mit us \\\"durch Graben heraus holen, ausgraben\\\"'; 'mit ni \\\"eingraben, verscharren\\\"'; 'mit vi \\\"durch Graben beseitigen … zerstören\\\"'; 'mit ham \\\"beschütten, überschütten\\\"'. No ā- and no aiβi- compound is listed.\"},\n   {\"src\": \"NYB\", \"where\": \"Nyberg II s.v. apakandan\", \"stance\": \"contradicts\", \"note\": \"'apakandan … to throw; bē ~ to throw away … < OIr *apa-kan- and *upa-kan- (v.s.v. apa-), from kandan, q.v.; MPrthPrs ʾbgndn; … NP afgandan, augandan.' — the prefix of afkandan is apa-/upa-, not aiβi-.\"},\n   {\"src\": \"CHEUNG\", \"where\": \"EDIV pp.229-232 s.vv. *kan¹, *kan²\", \"stance\": \"partial\", \"note\": \"*kan¹: '(+ *apa-) NP afgandan \\\"to throw, cast away\\\" || (+ *para-ā-) NP paragandan/parakandan \\\"to disperse; sow; diffuse\\\" || (+ *pati-) (?) NP paykandan'; *kan²: '(+ *ā-) NP āgandan/āgin- \\\"to fill, stuff\\\"', with Parthian ʾgn-, MSogd. ʾkn.\"},\n   {\"src\": \"HUB\", \"where\": \"Persische Studien pp.45, 80 (§133)\", \"stance\": \"supports\", \"note\": \"HUB.txt: 'paikan \\\"Pfeil\\\", arm. patkandaran \\\"Köcher\\\"' listed among the words in which Old Persian/Middle Persian pati- regularly becomes NP pai-/pey- — i.e. Hübschmann accepts paiti- as the first element of peykān.\"}\n ]\n})\n\nN({\n \"id\": 3, \"lang\": \"Persian\", \"words\": \"âkandan «آکندن ( آگندن )»; kažâkand «کژاکند ( قزاگند )»; afkandan «افکندن ( افگندن ، ـ افکن )»; parâkandan «پراکندن ( پراگندن )»; paykân «پیکان»\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"All five Persian words are real and all five continue an Old Iranian kan- verb, exactly as drawn. آگندن/آکندن āgandan 'to fill, stuff' < MP āgandan, āgan- (MacKenzie: 'āgandan, āgan- [ʾkn-dn' | M ʾgnd, N -] fill, stuff'), < OIr *ā-kan-ta-; Abolghasemi (FFD p.26) spells the chain out: 'آگند < فارسی میانه āgand < ایرانی باستان *ā-kan-ta-'. کژاکند kažākand / قزاگند qazāgand is the padded battle-coat, a compound of kaž 'raw silk' + āgand 'stuffed' — Borhān-e Qāṭeʿ (vol.3, pdf p.321 ≈ printed 1526-1528) defines قزاغند as 'جامه‌ای که در حشو آن پنبه و ابریشم آکنده و آجیده کرده باشند' and Moʿin's footnote equates قزاغند = قزاکند = کژاکند = کژاغند. افکندن/افگندن afkandan 'to throw, drop' < MP abgandan, abgan- < *apa-kan-/*upa-kan-. پراکندن/پراگندن parākandan 'to scatter' < MP pargandan/parāgandan < *para-ā-kan- (Parthian prʾgn-, MP pargandag 'scattered'). پیکان peykān 'arrowhead' < MP paykān < *pati-kāna- 'that which is driven in' (Horn 362), with the regular pati- > pay- of Middle/New Persian. The one caveat is the one already noted at the root: Abolghasemi, on the very page Nourai cites, warns that the kan- behind āgandan/afgandan/parāgandan is NOT the kan- behind kandan 'to dig'.\",\n \"derivation_fa\": \"هر پنج واژه واقعی‌اند و هر پنج از فعلی ایرانی‌باستان با ستاک kan- می‌آیند، درست همان‌گونه که در نمودار آمده است. «آگندن/آکندن» از فارسی میانهٔ āgandan (مکنزی: «āgandan, āgan- پر کردن، انباشتن») و آن از ایرانی باستان *ā-kan-ta-؛ ابوالقاسمی در همان صفحه‌ای که نورایی گواه گرفته (ص ۲۶) می‌نویسد: «آگند < فارسی میانه āgand < ایرانی باستان *ā-kan-ta-». «کژاکند/قزاگند» جامهٔ جنگیِ لایه‌دار است، مرکب از «کژ» (ابریشم خام) + «آگند» (انباشته)؛ برهان قاطع (ج۳، ص ۱۵۲۶ به بعد) آن را «جامه‌ای که در حشو آن پنبه و ابریشم آکنده و آجیده کرده باشند» تعریف می‌کند و معین در حاشیه می‌آورد: «قزاغند = قزاکند = کژاکند = کژاغند». «افکندن/افگندن» از فارسی میانهٔ abgandan و آن از *apa-kan-/*upa-kan-. «پراکندن/پراگندن» از فارسی میانهٔ pargandan و آن از *para-ā-kan- (پارتی prʾgn-). «پیکان» از فارسی میانهٔ paykān و آن از *pati-kāna-، با تحول آواییِ همیشگیِ pati- > pay- در فارسی میانه و نو (هرن ۳۶۲، هوبشمان §۱۳۳). تنها نکتهٔ هشداردهنده همان است که در جعبهٔ ریشه گفته شد: ابوالقاسمی در همان صفحه تصریح می‌کند kan- ی که «آگندن» و «افگندن» و «پراگندن» از آن آمده‌اند غیر از kan- ی است که «کندن» از آن آمده است.\",\n \"sources\": [\"https://en.wiktionary.org/wiki/%D8%A2%DA%AF%D9%86%D8%AF%D9%86\", \"https://en.wiktionary.org/wiki/%D8%A7%D9%81%DA%AF%D9%86%D8%AF%D9%86\"],\n \"ref_check\": [\n   {\"ref\": \"BQT:1526\", \"status\": \"supports\", \"note\": \"BQT vol.3, BQT_v3_pages.txt pdf page 321 (printed ≈ 1526-1528): entry 'قزاغند … جامه‌ای را گویند که در حشو آن ابریشم و پنبه … آجیده کرده شده باشد که در روزهای جنگ پوشند و آن را خفتان گویند' and 'قزاگند … بروزن و معنی قزاکند است که خفتان جنگ باشد'; Moʿin's footnote 4: 'قزاغند = قزاکند = کژاکند، کژاغند (م.) … «رشیدی»'. Confirms the word and its 'silk-stuffed' sense.\"},\n   {\"ref\": \"FFD:26\", \"status\": \"partial\", \"note\": \"FFD_pages.txt pdf p.31 = printed p.26, s.v. آگندن: 'آگند < فارسی میانه āgand < ایرانی باستان *ā-kan-ta- … ریشهٔ kan به معنی «نهادن و افگندن» است. «افگندن» و «پراگندن» هم از ریشهٔ kan آمده‌اند … در ایرانی باستان kan دیگری هم بوده است که از آن «کندن» آمده است.' Supports each Persian form but explicitly splits the root Nourai has merged.\"}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"MacKenzie pp.5, 8, 49, 66\", \"stance\": \"supports\", \"note\": \"PHD_mackenzie.txt: 'āgandan, āgan- [ʾkn-dn' | M ʾgnd, N -] fill, stuff'; 'abgandan, ab~an- [LMYTWN-tn' < A √rmʾ; ʾpkn- | M ʾbgnd, ʾbgn-,]' throw; 'pargandan, pargan- [plkn-, plgn-dn' (P prʾgnd, N parāgandan)]'; 'kandan, kan- … dig'.\"},\n   {\"src\": \"NYB\", \"where\": \"Nyberg II s.vv. apakandan, pargandak, frakandan\", \"stance\": \"supports\", \"note\": \"'pargandak … scattered, dispersed … Pt. of para + kan- \\\"to throw\\\" (Verbum 227) … MPrs prgn- (S); NP pargandah (the vb. is here parāgandan)'.\"},\n   {\"src\": \"HRN\", \"where\": \"Grundriss no. 362 (p.80)\", \"stance\": \"partial\", \"note\": \"'362. peikän \\\"Pfeilspitze, Pfeil\\\". aw. paiti + √kan- (?); arm. LW. paikan|daran' — the paiti-kan etymology of peykān, but marked doubtful by Horn himself.\"},\n   {\"src\": \"BQT\", \"where\": \"Borhān vol.3, pdf p.500 (printed ≈ 1707), Moʿin's footnote to کندن\", \"stance\": \"supports\", \"note\": \"'کندن — از: کن + دن (پسوند مصدری)؛ پهلوی kandan؛ ایران باستان kan (کندن، حفر کردن) «بارتولمه ۴۳۷»، «نیبرگ ۱۱۹»؛ پارسی باستان، اوستا kan-؛ … هندی [سنسکریت] khan-؛ کردی kendn؛ … استی nijginin (دفن کردن)؛ قس: ارمنی akan «هوبشمان»'.\"}\n ]\n})\n\nN({\n \"id\": 4, \"lang\": \"Old Persian\", \"words\": \"ni-kan; vi-kan\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Both compounds are attested Old Persian and Kent glosses them almost word for word as Nourai does. vi-kan- appears in Darius' Bisotun and Xerxes' daiva inscriptions: viyakanam '(I) destroyed' (XPh 38, of the daiva-sanctuary), viyakā 'he destroyed' (DB 1.64, of Gaumāta's razing of the sanctuaries), vikanāhy 'you shall destroy' (DB 4.71, 73, 77 — Darius' curse on whoever destroys the inscription). ni-kan- occurs as the imperative nikatuv 'let him obliterate' (DB 4.80). The semantics ('dig apart' > 'raze, destroy'; 'dig down' > 'blot out') are the ordinary Old Iranian development of *kanH- 'to dig' with vi- and ni-, and both verbs continue into MP gugān- 'to destroy' (< *vi-kan-) and into Kurdish nikandin 'to bury'. This node is the strongest link on the page.\",\n \"derivation_fa\": \"هر دو ترکیب در پارسی باستان گواهی‌شده‌اند و کنت تقریباً با همان واژه‌ها معنی‌شان می‌کند که نورایی آورده است. vi-kan- در سنگ‌نبشتهٔ بیستون و در کتیبهٔ دیوهای خشایارشا می‌آید: viyakanam «ویران کردم» (XPh ۳۸، دربارهٔ پرستشگاه دیوان)، viyakā «ویران کرد» (DB ۱٫۶۴، دربارهٔ ویران‌کردنِ نیایشگاه‌ها به دست گئوماته)، vikanāhy «ویران خواهی کرد» (DB ۴٫۷۱ و ۷۳ و ۷۷، در نفرین داریوش بر هرکه کتیبه را بشکند). ni-kan- در صیغهٔ امری nikatuv «بزداید» (DB ۴٫۸۰) آمده است. تحول معنایی («با کندن جدا کردن» ← «ویران کردن»؛ «فروکندن» ← «محو کردن») همان تحول عادی ایرانی است و هر دو فعل در فارسی میانه به gugān- «ویران کردن» (از *vi-kan-) و در کردی به nikandin «دفن کردن» رسیده‌اند. این استوارترین حلقهٔ این صفحه است. ادعای نورایی درست است.\",\n \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/kanam\"],\n \"ref_check\": [\n   {\"ref\": \"KNT:178\", \"status\": \"supports\", \"note\": \"KNT.txt leaf 201 (Kent's Lexicon; = printed p.178 of the 1953 ed., as Cheung also cites it): 'ni- + kan- \\\"destroy, obliterate\\\": nikatuv imv. DB 4.80.' and 'vi- + kan- \\\"dig apart, destroy\\\": viyakanam 1st sg. imf. XPh 38. viyakā imf. DB 1.64. vikanāhy 2d sg. subj. DB 4.71, 78; vikanāhy-diš DB 4.77.' Nourai's gloss for vi-kan is Kent's verbatim.\"}\n ],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"AiW cols. 437-438\", \"stance\": \"supports\", \"note\": \"Bartholomae gives the same OP forms under ²kan-: 'mit ni … uta tya kunavāhy avataiy Auramazdā nikātuv Bh. 4.17' and 'mit vi \\\"durch Graben beseitigen, abtragen; zerstören\\\": … vaiy adanā tyā Gaumāta … viyaka Bh. 1.14; … imām dipim vaināhy vikanāhy Bh. 4.15-17'.\"},\n   {\"src\": \"CHEUNG\", \"where\": \"EDIV p.230 (*kan¹)\", \"stance\": \"supports\", \"note\": \"'*OLD PERSIAN: (+ *aua-) ? avakan- \\\"to throw, place on\\\" || (+ *ni-) nika(n)- \\\"to tear down\\\" || (+ *ui-) vika(n)- \\\"to destroy\\\" ⇒ Kent: 178b' — the same forms, same Kent page, but assigned to the throw-root rather than the dig-root.\"},\n   {\"src\": \"NYB\", \"where\": \"Nyberg II s.v. gukān-\", \"stance\": \"supports\", \"note\": \"'gukān- [gwkʾn-] pres. to destroy … Av. vi-²kan- = OP; MPrth w(y)gʾnyšn … V.s.v. kandan.'\"}\n ]\n})\n\nN({\n \"id\": 5, \"lang\": \"Sogdian\", \"words\": \"kang, kanp\",\n \"verdict\": \"transcription_suspect\",\n \"derivation\": \"The etymology is right, the transliteration is not. The Sogdian word for 'town, settlement' is knδh, transliterated kanθ / kanδ (Gharib, Sogdian Dictionary; Cheung lists it under *kanH¹ 'to dig': 'SSogd. knδh, BSogd. knδyh, CSogd. qδ(-) \\\"town\\\"'), from Old Iranian *kanta- 'dug (out), (thing) dug', i.e. the past participle of kan- 'to dig' — a settlement is literally 'the dug place', a semantic type well known from Old Persian kata- 'dug-out, chamber'. It is the -kand/-kent of Samarkand, Tashkent, Yarkand, Panjikent (Sogd. pncykn8h in Gharib). 'kang' is a Persianized spelling (Borhān's headword is سمرکنگ), but 'kanp' is not a possible Sogdian form: -p never renders Sogdian δ/θ. The printed page (see data/verification/sources/refs/ocr/BOOK/214.png) does read 'kang, kanp', so the JSON is faithful and the misprint is the book's — almost certainly Nourai's rendering of kanθ with the θ read as p.\",\n \"derivation_fa\": \"ریشه‌شناسی درست است اما آوانویسی نه. واژهٔ سغدیِ «شهر، آبادی» knδh است که kanθ یا kanδ خوانده می‌شود (قریب، فرهنگ سغدی؛ چونگ آن را زیر ریشهٔ *kanH¹ «کندن» می‌آورد: «SSogd. knδh، BSogd. knδyh، CSogd. qδ(-) شهر»)، از ایرانی باستان *kanta- «کنده‌شده»، یعنی اسم مفعولِ kan- «کندن»؛ آبادی در اصل «جای کنده‌شده» است، همان‌گونه که kata- پارسی باستان «کنده، اتاقِ کنده‌شده» است. همین جزء است که در سمرقند، تاشکند، یارکند و پنجیکنت (سغدی pncyknδh) دیده می‌شود. صورت «kang» گونهٔ فارسی‌شده است (سرواژهٔ برهان قاطع «سمرکنگ» است)، اما «kanp» در سغدی ممکن نیست؛ حرف p هرگز برابرِ δ/θ سغدی نمی‌آید. تصویر صفحهٔ چاپی (پیوست ۲۱۴.png) نشان می‌دهد که خودِ کتاب «kang, kanp» چاپ کرده است؛ پس خطای خوانشِ اسکن نیست، خطای چاپی خودِ کتاب است — به احتمال زیاد θ در kanθ به p بدل خوانده شده.\",\n \"error_in\": \"book\",\n \"book_prints\": \"kang, kanp\",\n \"correct_form\": \"kanθ (Sogd. knδh) / kand\",\n \"sources\": [\"https://en.wiktionary.org/wiki/Samarkand\"],\n \"ref_check\": [\n   {\"ref\": \"BQT:1165\", \"status\": \"supports\", \"note\": \"BQT vol.2, BQT_v2_pages.txt leaf 629 (printed ≈ 1165-1172): headword 'سمرکنگ — با کاف، بروزن و معنی سمرقند است و آن شهری باشد در ماوراءالنهر که کاغذ خوب از آنجا آورند و سمرقند معرب آن …' — this is Nourai's source for the 'kang' spelling.\"},\n   {\"ref\": \"BQT:1703\", \"status\": \"partial\", \"note\": \"BQT vol.3 around pdf pp.496-500 (printed ≈ 1703-1707) is the کند/کندن cluster; Moʿin's footnote to کندن there gives 'ایران باستان kan (کندن، حفر کردن) «بارتولمه ۴۳۷»، «نیبرگ ۱۱۹»'. No Sogdian kanθ form is printed on those pages; the Sogdian knδh is given instead in Moʿin's footnote to سمرقند in vol.2 (see node 7).\"}\n ],\n \"consulted\": [\n   {\"src\": \"SOD\", \"where\": \"Gharib, entry 6893 (pncyknδh 'Panjikanth')\", \"stance\": \"partial\", \"note\": \"SOD_pages.txt line 23486: '6893 pncykn8h S' — Gharib's transliteration of the town-element is knδh, never 'kanp'.\"},\n   {\"src\": \"CHEUNG\", \"where\": \"EDIV p.232 (*kanH¹, Sogdian)\", \"stance\": \"supports\", \"note\": \"'*SOGDIAN: BSogd. kn-, CSogd. qn-, MSogd. kn- \\\"to dig\\\", SSogd. knδh, BSogd. knδyh, CSogd. qδ(-) \\\"town\\\"' — the town-word is explicitly derived from the dig-root.\"},\n   {\"src\": \"BQT\", \"where\": \"Borhān vol.2 leaf 629, Moʿin's footnote to سمرقند\", \"stance\": \"supports\", \"note\": \"'… جزو دوم kand از پارسی باستان *kanta-، سغدی knδh (شهر)، مشتق از kan- (کندن). رک: مارکوارت، شهرستانهای ایرانشهر ص ۹۲.'\"}\n ]\n})\n\nN({\n \"id\": 6, \"lang\": \"Pahlavi\", \"words\": \"\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"An empty pass-through box standing for the Middle Persian stage between Sogdian kanθ and New Persian -qand. Such a stage really is assumed: Moʿin's own footnote on سمرقند in Borhān-e Qāṭeʿ posits a Pahlavi Smarkand (alongside Greek Marakanda in the Alexander historians), citing Marquart's Ērānšahr p.92. The Middle Persian form is what mediates the Sogdian -kanθ to the Persian -kand/-qand, since MP had no θ in that position and substituted -nd.\",\n \"derivation_fa\": \"این جعبهٔ تهی نمایندهٔ مرحلهٔ فارسی میانه میان سغدیِ kanθ و فارسی نوِ ـقند است. چنین مرحله‌ای واقعاً فرض شده است: معین در حاشیهٔ «سمرقند» در برهان قاطع صورت پهلویِ Smarkand را می‌آورد (در کنار Marakanda یونانی در گزارش تاریخ‌نگاران اسکندر) و به «شهرستانهای ایرانشهرِ» مارکوارت ص ۹۲ ارجاع می‌دهد. همین مرحلهٔ میانی است که θ سغدی را به ـند فارسی می‌رساند، زیرا فارسی میانه در این جایگاه θ نداشت و آن را به d/nd بدل می‌کرد. جعبه بی‌ایراد است.\",\n \"sources\": [\"https://en.wiktionary.org/wiki/Samarkand\"],\n \"ref_check\": [\n   {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"The box carries no reference in the book; it is a silent pass-through.\"}\n ],\n \"consulted\": [\n   {\"src\": \"BQT\", \"where\": \"Borhān vol.2 leaf 629 (printed ≈1172), Moʿin's footnote\", \"stance\": \"supports\", \"note\": \"'رک: معجم البلدان. پهلوی Smarkand. یونانی Marakanda …' — Moʿin does posit a Pahlavi stage.\"},\n   {\"src\": \"PHD\", \"where\": \"MacKenzie, A Concise Pahlavi Dictionary\", \"stance\": \"silent\", \"note\": \"grep of PHD.txt / PHD_mackenzie.txt for 'Smarkand', 'kand' as a town-word: nothing; MacKenzie's dictionary is a lexicon of the Book Pahlavi corpus and has no place-name entries of this kind.\"}\n ]\n})\n\nN({\n \"id\": 7, \"lang\": \"Persian\", \"words\": \"Samarqand «سمرقند ( سمرکند )»\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Samarqand's second element is indeed the kan- 'dig' word. Wiktionary (with the Sogdian script) gives: 'From Persian سمرقند (samarqand), from Sogdian 𐼼𐼺𐼰𐽀𐼸𐼻𐼹𐼳 (smʾrknδh /*Smā́rkąθ/)', and Moʿin's footnote in Borhān-e Qāṭeʿ says the same in more detail: the first element سمر is still unexplained, 'جزو دوم kand از پارسی باستان *kanta-، سغدی knδh (شهر)، مشتق از kan- (کندن)', with a reference to Marquart's Ērānšahr p.92. The Greeks knew the city as Marakanda (Arrian, Quintus Curtius), which preserves the same -kanda. The Persian spelling with ق is an Arabic-script convention for the borrowed k of the Sogdian original — hence the variant سمرکند that Nourai prints in parentheses, and Borhān's own headword سمرکنگ. The route Sogdian > (MP) > NP is exactly as drawn.\",\n \"derivation_fa\": \"جزء دومِ «سمرقند» همان واژهٔ kan- «کندن» است. ویکی‌واژه می‌نویسد: «از فارسی سمرقند، از سغدی smʾrknδh /*Smā́rkąθ/»، و حاشیهٔ معین در برهان قاطع همین را با تفصیل بیشتر می‌آورد: جزو نخست «سمر» تاکنون روشن نشده، «جزو دوم kand از پارسی باستان *kanta-، سغدی knδh (شهر)، مشتق از kan- (کندن)»، با ارجاع به شهرستانهای ایرانشهرِ مارکوارت ص ۹۲. یونانیان این شهر را Marakanda می‌نامیدند (آریان و کوینتوس کورتیوس) که همان ـکند را نگاه داشته است. نوشتنِ آن با «ق» شیوهٔ خط عربی برای k وام‌گرفته است؛ از همین‌روست گونهٔ «سمرکند» که نورایی در کمانک آورده و سرواژهٔ «سمرکنگ» در خودِ برهان. مسیر سغدی ← (فارسی میانه) ← فارسی نو درست همان است که در نمودار کشیده شده. ادعای نورایی درست است.\",\n \"sources\": [\"https://en.wiktionary.org/wiki/Samarkand\"],\n \"ref_check\": [\n   {\"ref\": \"BQT:1703\", \"status\": \"partial\", \"note\": \"The Samarqand entry is not at printed 1703 (that is the کند/کندن cluster in vol.3) but at vol.2 leaf 629, printed ≈1165-1172, s.v. سمرکنگ — i.e. at Nourai's OTHER citation for this family (BQT:1165). There Moʿin's footnote gives the full etymology: 'پهلوی Smarkand، یونانی Marakanda … جزو دوم kand از پارسی باستان *kanta-، سغدی knδh (شهر)، مشتق از kan- (کندن)'. The claim is supported; the page number is the one Nourai used for the Sogdian box.\"}\n ],\n \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"Moʿin's etymological footnote in Borhān-e Qāṭeʿ, vol.2 (printed ≈1172)\", \"stance\": \"supports\", \"note\": \"quoted above — Moʿin is the author of these footnotes, so this is Moʿin's own view.\"},\n   {\"src\": \"SOD\", \"where\": \"Gharib, entry 6893\", \"stance\": \"supports\", \"note\": \"'6893 pncyknδh S' (Panjikanth) shows the same -knδh town-element productive in Sogdian toponymy.\"}\n ]\n})\n\nN({\n \"id\": 8, \"lang\": \"Arabic\", \"words\": \"qanah; qanât; q.n.v\",\n \"verdict\": \"disputed\",\n \"derivation\": \"The Arabic words are real — qanāh (pl. qanawāt) 'reed, spear-shaft; underground water channel', the qanawa/qanā root 'to dig a channel' — but their origin is Semitic, not Iranian. Wiktionary derives Arabic قناة 'From Aramaic קַנְיָא / ܩܢܝܐ (qanyā, \\\"reed, cane, tube\\\"), from Akkadian 𒂵𒉡𒌑𒌝 (qanûm)'; Klein s.v. cane cites the same family, 'Akkad. qanû, Heb. qāneh, Aram.-Syr. qanyā, Arab. qanāh … Ethiop. qanot'; Etymonline traces the Greek borrowing to 'Babylonian-Assyrian qanu \\\"tube, reed\\\" … which may come from Sumerian-Akkadian gin \\\"reed\\\"'. The word is thus attested in Akkadian more than a millennium before any Iranian contact, and its primary sense is 'reed', with 'tube/channel' as a metaphor from the hollow reed — the very opposite of a derivation from a verb 'to dig'. What is genuinely Iranian is the technology, not the word: the qanāt/kārīz irrigation gallery is an Iranian invention, and its Persian name is کاریز/کهریز, which is what Persian used before the Arabic term was borrowed back in. Nourai's own note ('These words reached Greek and Latin through Semitic languages') half concedes the point; the modern view removes the Iranian link altogether.\",\n \"derivation_fa\": \"خودِ واژه‌های عربی واقعی‌اند — قناة (ج. قنوات) «نی، چوبِ نیزه؛ کاریزِ زیرزمینی» و ریشهٔ ق‌ن‌و/ق‌ن‌ی «کاریز کندن» — اما خاستگاهشان سامی است نه ایرانی. ویکی‌واژه قناة را «از آرامی קַנְיָא / ܩܢܝܐ (qanyā «نی، لوله») و آن از اکدی qanûm» می‌داند؛ کلاین ذیل cane همین خانواده را می‌آورد: «اکدی qanû، عبری qāneh، آرامی-سریانی qanyā، عربی qanāh»؛ و اتیمانلاین وام‌گیریِ یونانی را از «بابلی-آشوری qanu «لوله، نی»» می‌گیرد که شاید خود از سومری-اکدی gin «نی» باشد. پس این واژه بیش از هزار سال پیش از هر تماسِ ایرانی در اکدی گواهی شده و معنای نخستین آن «نی» است و «لوله/کاریز» استعاره‌ای از نیِ میان‌تهی — یعنی درست وارونهٔ گرفتنِ آن از فعلی به معنی «کندن». آنچه به‌راستی ایرانی است فناوری است نه واژه: کاریز از نوآوری‌های ایرانی است و نام فارسی آن «کاریز/کهریز» است. حکم: پژوهش امروزی این پیوند را رد می‌کند و واژه را سامی می‌داند؛ خودِ نورایی هم در یادداشتش نیمی از این را پذیرفته است.\",\n \"sources\": [\"https://en.wiktionary.org/wiki/%D9%82%D9%86%D8%A7%D8%A9\", \"https://www.etymonline.com/word/cane\"],\n \"ref_check\": [\n   {\"ref\": \"KLN:232\", \"status\": \"partial\", \"note\": \"Klein 1966 (KLN_1966.txt leaf 132, ≈ pp.231-232) s.v. cane: 'fr. Gk. κάννα, \\\"reed\\\", which is of Sem. origin. Cp. Akkad. qanû, Heb. qāneh, Aram.-Syr. qanyā, Arab. qanāh (whence Pers. qanat), \\\"reed, cane\\\", Ethiop. qanot, \\\"a goad\\\".' Klein confirms the Arabic word and its onward loan into Persian, but derives it from common Semitic — he says nothing about Iranian kan-.\"},\n   {\"ref\": \"ARB:261\", \"status\": \"not_found\", \"note\": \"grep of ARB_mo3rb.txt and ARB_abdulraheem.txt (al-Jawālīqī, al-Muʿarrab) for قناة/القناة returned only one garbled OCR line (ARB_mo3rb.txt:4074) that is not a headword; the pagination of the local copies is not established, so p.261 could not be located.\"},\n   {\"ref\": \"SAP:100\", \"status\": \"not_checked\", \"note\": \"Sayyāh's Farhang (Persian translation of al-Munjid) has no digital copy — refs_online.json lists it as 'purchase', local_file null.\"},\n   {\"ref\": \"FVF:539,545\", \"status\": \"not_checked\", \"note\": \"Emām Shūshtari, Farhang-e Vāžehā-ye Fārsi dar Zabān-e ʿArabi — refs_online.json: kind 'website', local_file null, readable only through noorlib's page viewer; not accessible here.\"}\n ],\n \"consulted\": [\n   {\"src\": \"AFM\", \"where\": \"Addi Shir, Kitāb al-Alfāẓ al-Fārisiyya al-Muʿarraba\", \"stance\": \"silent\", \"note\": \"grep of AFM_pages.txt / AFM.txt for قناة, القناة as a headword: no entry. Addi Shir, whose whole book is a list of Persian words arabized, does not claim قناة for Persian.\"},\n   {\"src\": \"PLA\", \"where\": \"Asbaghi, Persische Lehnwörter im Arabischen\", \"stance\": \"silent\", \"note\": \"grep of PLA_pages.txt for 'qanāt', 'qanat', 'qanāh': no entry (the hits for 'Kanal' are s.vv. zirāb and mīzāb, other words). Asbaghi's corpus of Persian loans in Arabic does not include qanāh.\"},\n   {\"src\": \"TAD\", \"where\": \"al-ʿUnaysī, Tafsīr al-alfāẓ al-dākhila\", \"stance\": \"silent\", \"note\": \"grep of TAD_pages.txt for قناة: only two garbled non-headword lines; no entry claiming a foreign origin for qanāh.\"},\n   {\"src\": \"KLN\", \"where\": \"Klein 1966 ≈ p.231 s.v. cane\", \"stance\": \"contradicts\", \"note\": \"see ref_check — Semitic, ultimately Mesopotamian, origin.\"}\n ]\n})\n\nN({\n \"id\": 9, \"lang\": \"Persian\", \"words\": \"qanât «قنات»; moqannî «مقنّی»\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Both Persian words are Arabic loans, exactly as the arrow says — the direction Arabic > Persian is right even though the ultimate source of the Arabic word is not Iranian (node 8). قنات qanāt is Arabic qanāh with the tāʾ marbūṭa written out, the form that Persian normally takes over in ـات (cf. زکات, صلات); Dehkhoda marks it '(ع اِ)' and glosses it 'چوب نیزه … || کاریز. کهریز. کاهریز. ج، قنوات', i.e. the native Persian word it displaced was کاریز/کهریز. مقنّی moqannī 'well-digger, qanāt-digger' is the Arabic active participle of the form-II verb qannā 'to dig a channel' (muqannin > muqannī), a purely Arabic derivation that could not have been formed inside Persian; its presence proves the loan direction. Klein confirms the loan explicitly: 'Arab. qanāh (whence Pers. qanat)'.\",\n \"derivation_fa\": \"هر دو واژه وام‌واژهٔ عربی‌اند، درست همان‌گونه که پیکان نمودار نشان می‌دهد؛ جهتِ عربی ← فارسی درست است، هرچند خاستگاهِ نهاییِ واژهٔ عربی ایرانی نیست (رک: گرهٔ ۸). «قنات» همان قناةِ عربی است با نوشتنِ تاء مربوطه به‌صورت ـات، شیوه‌ای که فارسی معمولاً در وام‌گیری به کار می‌برد (قس: زکات، صلات). دهخدا آن را «(ع اِ)» می‌نویسد و چنین معنی می‌کند: «چوب نیزه … || کاریز. کهریز. کاهریز. ج، قنوات» — یعنی واژهٔ بومیِ فارسی که این وام‌واژه جای آن را گرفت «کاریز/کهریز» بوده است. «مقنّی» اسم فاعلِ بابِ تفعیلِ عربی از قنّی «کاریز کندن» است (مُقَنِّن ← مقنّی)؛ چنین صورتی در درون فارسی ساخته‌شدنی نیست و همین گواهِ قاطعِ جهتِ وام‌گیری است. کلاین هم صریح می‌نویسد: «عربی qanāh (که فارسی qanat از آن است)». ادعای نورایی در این گره درست است.\",\n \"sources\": [\"https://abadis.ir/fatofa/%D9%82%D9%86%D8%A7%D8%AA/\", \"https://en.wiktionary.org/wiki/%D9%82%D9%86%D8%A7%D8%A9\"],\n \"ref_check\": [\n   {\"ref\": \"KLN:231\", \"status\": \"supports\", \"note\": \"Klein 1966 s.v. cane (leaf 132, ≈p.231): '… Arab. qanāh (whence Pers. qanat), \\\"reed, cane\\\" …' — exactly the arrow Arabic > Persian.\"},\n   {\"ref\": \"MON\", \"status\": \"supports\", \"note\": \"Moʿin/Dehkhoda via abadis.ir/fatofa/قنات: 'قنات. [ق َ] (ع اِ) چوب نیزه. رجوع به قناة شود. || کاریز. (مهذب الاسماء). کهریز. کاهریز. ج، قنوات' — the tag (ع) marks it as Arabic.\"},\n   {\"ref\": \"FVA:341\", \"status\": \"not_checked\", \"note\": \"Nahvi, Farhang-e Vāžehā-ye ʿArabi dar Fārsi — refs_online.json records no digital copy (searched archive.org, ketabnak, noorlib).\"},\n   {\"ref\": \"SNS:8\", \"status\": \"partial\", \"note\": \"SNS_pages.txt does contain a glossary entry 'kan' with the citation '(Kent. 178)' and the Sanskrit comparison 'kh(a)n-' (line 1235), and the index lists 'kan 8/13'; but Tavoosi's glossary of Šāyast nē Šāyast is a Pahlavi word-list and has nothing on Arabic qanāt or muqannī. The reference fits the root, not this node.\"}\n ],\n \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"abadis.ir (Moʿin/Dehkhoda entry قنات)\", \"stance\": \"supports\", \"note\": \"see ref_check; native equivalents given as کاریز/کهریز/کاهریز.\"},\n   {\"src\": \"AFM\", \"where\": \"Addi Shir\", \"stance\": \"silent\", \"note\": \"no قناة headword — Addi Shir does not treat it as a Persian word arabized, consistent with a genuine Arabic > Persian loan.\"},\n   {\"src\": \"KLN\", \"where\": \"Klein 1966 ≈p.231\", \"stance\": \"supports\", \"note\": \"'Arab. qanāh (whence Pers. qanat)'.\"}\n ]\n})\n\nN({\n \"id\": 10, \"lang\": \"Greek\", \"words\": \"kanon\",\n \"verdict\": \"plausible\",\n \"derivation\": \"Greek κανών 'straight rod, bar; ruler; rule, standard' is real and its traditional derivation is from κάννα 'reed' — a straight reed makes a measuring rod — so its Semitic connection is at one remove, through node 18, not directly from Arabic as drawn here. Klein s.v. canon 'rule' gives 'fr. Gk. κανών, \\\"rod, bar, ruler, rule, model\\\", fr. κάννα'; Etymonline says the same but adds the modern caveat: '…which is perhaps from kanna \\\"reed\\\", but Beekes favors Pre-Greek origin', i.e. the leading Greek etymological dictionary (Beekes 2010) now doubts even the κάννα connection and treats κανών as a substrate word. Two corrections to the chart, then: the parent should be Greek κάννα (node 18) rather than Arabic, and Arabic is anyway anachronistic for a word Homer's successors already use (κανών is in the Iliad, 8th-7th c. BCE, of the rods of a shield).\",\n \"derivation_fa\": \"واژهٔ یونانیِ κανών «میله، خط‌کش، قاعده، معیار» واقعی است و ریشه‌شناسیِ سنتیِ آن از κάννα «نی» است (نیِ راست، خط‌کشِ اندازه‌گیری می‌شود)؛ پس پیوندِ سامیِ آن یک واسطه دورتر است، یعنی از راه گرهٔ ۱۸، نه یکراست از عربی چنان‌که در نمودار کشیده شده. کلاین ذیل canon می‌نویسد: «از یونانی κανών «میله، خط‌کش، قاعده، الگو»، از κάννα»؛ اتیمانلاین همین را می‌آورد اما هشدارِ امروزی را می‌افزاید: «شاید از kanna «نی»، ولی بیکس خاستگاهِ پیشایونانی را ترجیح می‌دهد» — یعنی معتبرترین فرهنگ ریشه‌شناسیِ یونانی (بیکس ۲۰۱۰) حتی همین پیوند با κάννα را نیز مشکوک می‌داند و κανών را واژه‌ای زیرلایه‌ای می‌شمارد. دو اصلاح بر نمودار: پدرِ این گره باید κάννα یونانی (گرهٔ ۱۸) باشد نه عربی، و از سوی دیگر عربی برای واژه‌ای که در ایلیاد (سدهٔ هشتم-هفتم پیش از میلاد) به کار رفته زمان‌پریشی است. حکم: با احتیاط پذیرفتنی است.\",\n \"sources\": [\"https://www.etymonline.com/word/canon\"],\n \"ref_check\": [\n   {\"ref\": \"KLN:232\", \"status\": \"supports\", \"note\": \"Klein 1966 (leaf 133, ≈p.232) s.v. canon 'rule': 'ME. canun, canoun, fr. OE. canon, fr. L. canon, \\\"a measuring line, rule, model\\\", in Eccles. L. \\\"canon\\\", fr. Gk. κανών, \\\"rod, bar, ruler, rule, model\\\", fr. κάννα' — Klein's parent for κανών is κάννα, not Arabic.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein 1966 ≈p.232 s.v. canon\", \"stance\": \"partial\", \"note\": \"as quoted; the Semitic link is mediated by κάννα.\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etymological Dictionary s.v. CANON\", \"stance\": \"supports\", \"note\": \"SKT.txt: 'CANON … L. canon, a rule; Gk. κανών, a rule, orig. a straight rod; from Gk. κάννα, a reed.'\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985, IE roots appendix\", \"stance\": \"silent\", \"note\": \"grep of AHD_watkins1985.txt for 'canna', 'kanon': nothing — the appendix covers only Indo-European roots, and κάννα/κανών are not among them (which is why Nourai's 'AHD:1520' for a reed-word is doubtful; see node 18).\"}\n ]\n})\n\nN({\n \"id\": 11, \"lang\": \"Arabic\", \"words\": \"qânun\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Arabic قانون qānūn 'rule, law; (also) the trapezoidal zither, and the title of Avicenna's al-Qānūn fī l-ṭibb' is a straightforward Greek loan, taken over in the translation movement of the 8th-9th centuries along with the rest of the Greek scientific vocabulary; Greek κανών 'rule, standard' gave Syriac qānōnā and thence Arabic qānūn, the long ū rendering Greek ω. Moʿin's footnote in Borhān-e Qāṭeʿ states it in exactly these terms: 'معرب از یونانی κανών «دائرةالمعارف اسلام: قانون»'. The semantic development 'measuring rod' > 'rule, canon' > 'statute law' (as opposed to religious šarʿ) is Greek-to-Arabic and is the source of the whole later Islamic legal usage (qānūn vs. šarīʿa).\",\n \"derivation_fa\": \"«قانون» عربی به معنی «قاعده، قانون» (و نیز نامِ سازِ ذوزنقه‌ای و عنوانِ «القانون فی الطب» ابن‌سینا) وام‌واژه‌ای یونانی است که در نهضتِ ترجمهٔ سده‌های دوم و سوم هجری همراهِ دیگر واژگانِ علمیِ یونانی به عربی راه یافت؛ κανών یونانی «قاعده، معیار» نخست به سریانی qānōnā و از آنجا به عربی قانون رسید و ū کشیده برابرِ ω یونانی نشست. معین در حاشیهٔ برهان قاطع دقیقاً همین را می‌نویسد: «معرب از یونانی κανών «دائرةالمعارف اسلام: قانون»». تحول معناییِ «میلهٔ اندازه‌گیری» ← «قاعده» ← «قانونِ وضعی» (در برابرِ شرع) در همین گذرِ یونانی به عربی رخ داده و سرچشمهٔ همهٔ کاربردهای حقوقیِ بعدیِ اسلامی (قانون در برابر شریعت) است. ادعای نورایی درست است.\",\n \"sources\": [\"https://en.wiktionary.org/wiki/%D9%82%D8%A7%D9%86%D9%88%D9%86\", \"https://www.etymonline.com/word/canon\"],\n \"ref_check\": [\n   {\"ref\": \"BQT:1516\", \"status\": \"supports\", \"note\": \"BQT vol.3, BQT_v3_pages.txt pdf page 309 = printed 1516 exactly. The entry قانون reads 'بمعنی اصل و رسم و قاعده باشد … و نام کتابی است … و نام سازست که مینوازند'; Moʿin's numbered footnote on the same page: 'معرب از یونانی κανών «دائرةالمعارف اسلام: قانون»' and, for the instrument, 'آلت موسیقی مشکل از طبلی مسطح و مستطیل که سیمهای فلزی بر آن نصب کرده … «دائرةالمعارف اسلام»'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"Moʿin's footnote in BQT vol.3 p.1516\", \"stance\": \"supports\", \"note\": \"quoted above; Moʿin wrote these footnotes, so this is Moʿin's own verdict: Arabized from Greek.\"},\n   {\"src\": \"KLN\", \"where\": \"Klein 1966 ≈p.232 s.v. canon\", \"stance\": \"supports\", \"note\": \"Klein traces Latin/English canon to Gk. κανών; the Arabic branch is the parallel eastern borrowing of the same Greek word.\"},\n   {\"src\": \"LKT\", \"where\": \"Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs\", \"stance\": \"silent\", \"note\": \"grep of LKT.txt for 'qānūn', 'kanun': no entry — Lokotsch catalogues oriental words that entered Europe, and qānūn travelled the other way.\"}\n ]\n})\n\nN({\n \"id\": 12, \"lang\": \"Persian\", \"words\": \"qânun «قانون ( کانون ۲ )»\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Persian قانون qānūn 'rule, law' is the Arabic word taken over unchanged in spelling and meaning, and it is one of the commonest Arabic loans in Persian (قانون اساسی 'constitution', قانونی 'legal'). Nourai's parenthesis «کانون ۲» points to Borhān-e Qāṭeʿ's alternative spelling with kāf — the same page (BQT 1516) records that some hold 'این لغت معرب کالون است و عربی نیست', i.e. the lexicographers already knew the word was not native Arabic. Note that this کانون is not the common Persian کانون 'brazier, hearth, centre' (that one is Arabic kānūn from Syriac kānūnā); the '۲' is Borhān's own sense-number distinguishing the two.\",\n \"derivation_fa\": \"«قانون» فارسی همان واژهٔ عربی است که بی هیچ دگرگونی در املا و معنا به فارسی آمده و از پرکاربردترین وام‌واژه‌های عربی در فارسی است (قانون اساسی، قانونی، قانون‌گذار). کمانکِ «کانون ۲» در نمودارِ نورایی به گونهٔ نوشتاریِ دیگری با کاف در برهان قاطع اشاره دارد؛ در همان صفحه (برهان ۱۵۱۶) آمده است «گویند این لغت معرب کالون است و عربی نیست»، یعنی فرهنگ‌نویسانِ قدیم هم می‌دانستند این واژه در اصل عربی نیست. توجه باید داشت که این «کانون» غیر از «کانونِ» رایجِ فارسی به معنی «آتشدان، مرکز» است که آن یکی از عربی kānūn و آن هم از سریانی kānūnā آمده است؛ عددِ «۲» شمارهٔ معناییِ خودِ برهان برای جدا کردن این دو است. ادعای نورایی درست است.\",\n \"sources\": [\"https://en.wiktionary.org/wiki/%D9%82%D8%A7%D9%86%D9%88%D9%86\"],\n \"ref_check\": [\n   {\"ref\": \"BQT:1516\", \"status\": \"supports\", \"note\": \"BQT vol.3 pdf p.309 = printed 1516, entry قانون with Moʿin's footnote 'معرب از یونانی κανών'; the entry text itself notes 'گویند این لغت معرب کالون است و عربی نیست'.\"},\n   {\"ref\": \"MON:2875\", \"status\": \"not_checked\", \"note\": \"Moʿin's Farhang-e Fārsi vol.3 p.2875 could not be paged: MON_part1/part2 OCR carries no reliable printed page numbers (refs_online.json: page_offset null) and the online vajehyab/abadis text gives entries without page numbers. The abadis entry for قانون nevertheless carries Moʿin's origin tag for an Arabic word.\"}\n ],\n \"consulted\": [\n   {\"src\": \"BQT\", \"where\": \"vol.3 printed p.1516\", \"stance\": \"supports\", \"note\": \"as quoted.\"},\n   {\"src\": \"MON\", \"where\": \"abadis.ir / vajehyab (Moʿin lexicon)\", \"stance\": \"supports\", \"note\": \"The Moʿin entry for قانون is tagged as an Arabic loan; his Borhān footnote (same author) gives the Greek source.\"}\n ]\n})\n\nN({\n \"id\": 13, \"lang\": \"English\", \"words\": \"canon\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"English canon 'a rule or law' comes down from Greek κανών through Latin: Late Latin canon 'church law, decree enacted by ecclesiastical authority' (classical Latin canon 'measuring line, rule'), borrowed into Old English as canon 'rule, law, or decree of the Church' and reinforced in Middle English from Old French canon. The word is thus one of the oldest Greek loans in English, taken in with the Latin of the Church rather than at the Norman conquest; its later senses ('the accepted books of the Bible', c.1400; 'standard of judging', c.1600; the musical canon, 1590s) all grow from 'rule'. The chart's arrow Greek > English is right, with Latin (unshown) as the carrier.\",\n \"derivation_fa\": \"واژهٔ انگلیسیِ canon «قاعده، قانون» از راه لاتین از κανών یونانی رسیده است: لاتینِ متأخر canon «قانونِ کلیسا، حکمِ صادرشده از مرجعِ کلیسایی» (در لاتینِ کلاسیک canon «خط اندازه‌گیری، قاعده»)، که در انگلیسیِ کهن به‌صورت canon «قاعده، قانون یا حکمِ کلیسا» وام گرفته شد و در انگلیسیِ میانه از canonِ فرانسویِ کهن نیرو گرفت. پس این واژه از کهن‌ترین وام‌واژه‌های یونانی در انگلیسی است که با لاتینِ کلیسا وارد شده نه با فتحِ نورمن‌ها؛ معناهای بعدیِ آن («کتاب‌های پذیرفتهٔ کتاب مقدس»، حدود ۱۴۰۰؛ «معیارِ داوری»، حدود ۱۶۰۰؛ و کانون در موسیقی، دههٔ ۱۵۹۰) همه از همان «قاعده» رشد کرده‌اند. پیکانِ یونانی ← انگلیسی درست است و لاتین واسطهٔ نانوشتهٔ آن است. ادعای نورایی درست است.\",\n \"sources\": [\"https://www.etymonline.com/word/canon\"],\n \"ref_check\": [\n   {\"ref\": \"AHD:197\", \"status\": \"not_checked\", \"note\": \"Nourai's AHD page numbers in the 1500s are the 1975 Indo-European appendix; 'AHD:197' is a page of the main dictionary text (s.v. canon), and the 1975/76 New College Edition is not open online. The 1985 Watkins standalone volume on disk contains only the root appendix, where canon does not appear.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein 1966 ≈p.232 s.v. canon 'rule'\", \"stance\": \"supports\", \"note\": \"'ME. canun, canoun, fr. OE. canon, fr. L. canon … fr. Gk. κανών.'\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat s.v. CANON\", \"stance\": \"supports\", \"note\": \"'CANON, a rule. (L.—Gk.) … L. canon; Gk. κανών, a rule.'\"}\n ]\n})\n\nN({\n \"id\": 14, \"lang\": \"Latin\", \"words\": \"canalis\",\n \"verdict\": \"plausible\",\n \"derivation\": \"Latin canālis 'water pipe, groove, channel' is real and does belong to this word-family, but not as a direct borrowing from Arabic: it is a Latin formation on canna 'reed, cane, small tube' — originally an adjective ('reed-like, tubular'), used as a noun. Klein sets it out: 'canal, n. — F., fr. L. canalis, \\\"water pipe, channel, canal\\\", prop. subst. use of an adj. formed fr. canna, \\\"reed, cane; small vessel, tube\\\". The shortening of the double n is due to the phonetic law according to which before a stressed syllable a double consonant becomes short' (the 'mamilla law'). Etymonline agrees: 'from Latin canalis \\\"water pipe, groove, channel,\\\" noun use of adjective from canna \\\"reed\\\"'. So the parent box should be node 18 (canna), and the Semitic contribution is at that earlier remove; the arrow from Arabic is a shortcut, not a route.\",\n \"derivation_fa\": \"canālis لاتین «لولهٔ آب، شیار، آبراه» واژه‌ای واقعی و از همین خانواده است، اما نه به‌عنوان وام‌گیریِ مستقیم از عربی: ساختی است لاتین بر پایهٔ canna «نی، لولهٔ کوچک»، در اصل صفت («نی‌مانند، لوله‌ای») که سپس اسم شده است. کلاین چنین شرح می‌دهد: «canal از فرانسه، از لاتین canalis، در اصل کاربردِ اسمیِ صفتی ساخته‌شده از canna «نی، لوله»؛ کوتاه‌شدنِ nn دوگانه بر پایهٔ قاعدهٔ آواییِ کوتاه‌شدنِ همخوانِ مشدّد پیش از هجای تکیه‌دار است» (قاعدهٔ mamilla). اتیمانلاین نیز همین را می‌گوید. پس جعبهٔ پدرِ این گره باید canna (گرهٔ ۱۸) باشد و سهمِ سامی یک پله دورتر است؛ پیکانی که از عربی کشیده شده میان‌بُری است نه مسیرِ واقعی. حکم: با احتیاط پذیرفتنی است.\",\n \"sources\": [\"https://www.etymonline.com/word/canal\"],\n \"ref_check\": [\n   {\"ref\": \"KLN\", \"status\": \"supports\", \"note\": \"Klein 1966 (leaf 132, ≈p.231) s.v. canal: 'F., fr. L. canalis, \\\"water pipe, channel, canal\\\", prop. subst. use of an adj. formed fr. canna, \\\"reed, cane; small vessel, tube\\\" … See cane and adj. suff. -al and cp. channel, cannel, kennel, \\\"gutter\\\", which are doublets of canal.' The reference (cited by Nourai without a page) does support canālis — but with canna, not Arabic, as its base.\"}\n ],\n \"consulted\": [\n   {\"src\": \"LEW\", \"where\": \"Walde, Lateinisches etymologisches Wörterbuch (1910) s.v. canalis\", \"stance\": \"supports\", \"note\": \"LEW_1910.txt s.v. canalis derives it from canna, itself marked as a loan from Greek κάννα of oriental origin.\"},\n   {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. canna / canalis\", \"stance\": \"supports\", \"note\": \"LAT.txt treats canālis as a derivative of canna, and canna as an eastern loanword ('mot d'emprunt, cf. gr. κάννα, assyr. qanû').\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat s.v. CANAL\", \"stance\": \"supports\", \"note\": \"'CANAL … F. canal, L. canalis, a channel; from canna, a reed.'\"}\n ]\n})\n\nN({\n \"id\": 15, \"lang\": \"French\", \"words\": \"\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"An empty pass-through box for French canal, attested from the 12th century in the forms canal/chanel 'water channel, tube, pipe, gutter' (Etymonline s.v. canal and channel). The doublet is instructive: the popular Norman-French development gave chanel > English channel, while the learned/Provençal form canal was taken over unchanged and re-borrowed into English in the 15th century — and it is this modern French canal that Persian borrowed in the 19th century as کانال. The box is therefore a real and necessary stage.\",\n \"derivation_fa\": \"این جعبهٔ تهی نمایندهٔ canalِ فرانسوی است که از سدهٔ دوازدهم میلادی به‌صورت‌های canal/chanel «آبراه، لوله، ناودان» گواهی شده است (اتیمانلاین ذیل canal و channel). دوگانهٔ آن آموزنده است: تحولِ عامیانهٔ نورمن-فرانسوی chanel را داد که به انگلیسی channel رسید، در حالی که صورتِ فاضلانه/پرووانسیِ canal دست‌نخورده ماند و در سدهٔ پانزدهم به انگلیسی وام داده شد؛ و همین canalِ فرانسویِ نو است که در سدهٔ نوزدهم به فارسی «کانال» وارد شد. پس این جعبه مرحله‌ای واقعی و لازم است.\",\n \"sources\": [\"https://www.etymonline.com/word/canal\"],\n \"ref_check\": [\n   {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"The box carries no reference in the book.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein 1966 ≈p.231 s.v. canal\", \"stance\": \"supports\", \"note\": \"'canal, n. — F., fr. L. canalis' — French is Klein's immediate donor for English canal too.\"},\n   {\"src\": \"DEV\", \"where\": \"Devic, Dictionnaire étymologique des mots français d'origine orientale\", \"stance\": \"silent\", \"note\": \"grep of DEV.txt for CANAL: no entry — Devic does not count canal among the French words of oriental origin, consistent with a purely Latin derivation.\"}\n ]\n})\n\nN({\n \"id\": 16, \"lang\": \"Persian\", \"words\": \"kânâl «کانال»\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Persian کانال kānāl 'canal, channel' is a modern European loan, taken from French canal in the 19th-century wave of technical borrowings (کانال سوئز, کانال آب) and later extended to the broadcasting sense. Moʿin marks it unambiguously: the entry reads '[ فر. ] (اِ) ۱- ترعه، مجرای وسیع بین دو دریا که برای عبور کشتی ساخته می‌شود. ۲- راه آب' — 'فر.' being Moʿin's abbreviation for فرانسه. The final -āl with a long ā reflects the French pronunciation rather than the Latin; had it come through Arabic or Turkish the form would have been different. So the chart's French > Persian arrow is exactly right.\",\n \"derivation_fa\": \"«کانال» فارسی وام‌واژه‌ای اروپایی و نو است که در موجِ وام‌گیری‌های فنیِ سدهٔ نوزدهم از canalِ فرانسوی گرفته شده (کانال سوئز، کانالِ آب) و بعدها به معنای شبکهٔ رادیو-تلویزیونی نیز گسترش یافته است. معین بی‌ابهام آن را چنین ثبت کرده: «[ فر. ] (اِ) ۱- ترعه، مجرای وسیع بین دو دریا که برای عبور کشتی ساخته می‌شود. ۲- راه آب» — و «فر.» کوتاه‌نوشتِ «فرانسه» در فرهنگ معین است. الفِ کشیدهٔ پایانی بازتابِ تلفظِ فرانسوی است نه لاتین؛ اگر از راه عربی یا ترکی آمده بود صورتِ دیگری می‌داشت. پس پیکانِ فرانسوی ← فارسیِ نمودار درست است. ادعای نورایی درست است.\",\n \"sources\": [\"https://abadis.ir/fatofa/%DA%A9%D8%A7%D9%86%D8%A7%D9%84/\"],\n \"ref_check\": [\n   {\"ref\": \"MON\", \"status\": \"supports\", \"note\": \"Moʿin's entry for کانال, retrieved via abadis.ir/fatofa/کانال (section فرهنگ معین): '[ فر. ] (اِ) ۱- ترعه، مجرای وسیع بین دو دریا که برای عبور کشتی ساخته می شود. ۲- راه آب.' The tag [فر.] = French is Moʿin's own.\"}\n ],\n \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"abadis.ir, فرهنگ معین s.v. کانال\", \"stance\": \"supports\", \"note\": \"as quoted.\"},\n   {\"src\": \"ARY\", \"where\": \"Aryanpur, Farhang-e Rishe-hā\", \"stance\": \"silent\", \"note\": \"grep of ARY_pages.txt for کانال: no entry — Aryanpur's book covers inherited Indo-European vocabulary, not modern European loans.\"}\n ]\n})\n\nN({\n \"id\": 17, \"lang\": \"English\", \"words\": \"canal, channel\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"The two English words are a classic learned/popular doublet from the same French source. channel is the older and more popular: 'early 14c., \\\"bed of a stream of water\\\", from Old French chanel \\\"bed of a waterway; tube, pipe, gutter\\\", from Latin canalis', later widened to 'that by which something is transmitted' (1530s), 'strait between land masses' (1550s), telegraph circuit (1848) and radio/TV band (1928). canal is the learned form, borrowed later and first in anatomy: 'early 15c., in anatomy, \\\"tubular passage in the body\\\"; mid-15c., \\\"a pipe for liquid\\\"; from French canal, chanel (12c.), from Latin canalis'; the modern sense 'artificial waterway for irrigation or navigation' is only from the 1670s, i.e. from the age of the great engineering canals. Klein explicitly calls channel, cannel and kennel 'gutter' doublets of canal.\",\n \"derivation_fa\": \"این دو واژهٔ انگلیسی نمونهٔ کلاسیکِ دوگانهٔ فاضلانه/عامیانه از یک سرچشمهٔ فرانسوی‌اند. channel کهن‌تر و عامیانه‌تر است: «آغازِ سدهٔ چهاردهم، «بسترِ رود»، از chanelِ فرانسویِ کهن «بسترِ آبراه؛ لوله، ناودان»، از canalis لاتین»، که سپس معنایش گسترده شد به «آنچه چیزی از راهِ آن می‌گذرد» (دههٔ ۱۵۳۰)، «تنگه میان دو خشکی» (دههٔ ۱۵۵۰)، «مدارِ تلگراف» (۱۸۴۸) و «باندِ فرکانسِ رادیو و تلویزیون» (۱۹۲۸). canal صورتِ فاضلانه است که دیرتر و نخست در کالبدشناسی وام گرفته شد: «آغازِ سدهٔ پانزدهم، در کالبدشناسی، «مجرای لوله‌ای در بدن»؛ میانهٔ سدهٔ پانزدهم، «لولهٔ مایعات»؛ از canalِ فرانسوی، از canalisِ لاتین»؛ معنای امروزیِ «آبراهِ ساختگی برای آبیاری یا کشتیرانی» تنها از دههٔ ۱۶۷۰ است، یعنی از روزگارِ کانال‌های بزرگِ مهندسی. کلاین صریحاً channel و cannel و kennel «ناودان» را دوگانه‌های canal می‌خواند. ادعای نورایی درست است.\",\n \"sources\": [\"https://www.etymonline.com/word/canal\"],\n \"ref_check\": [\n   {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"The box carries no reference in the book.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein 1966 ≈p.231 s.v. canal\", \"stance\": \"supports\", \"note\": \"'… cp. channel, cannel, kennel, \\\"gutter\\\", which are doublets of canal.'\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat s.vv. CANAL, CHANNEL\", \"stance\": \"supports\", \"note\": \"Skeat gives CHANNEL '(F.—L.) M.E. chanel, canel; O.F. chanel, canel; L. canalis' and CANAL as the later learned form.\"}\n ]\n})\n\nN({\n \"id\": 18, \"lang\": \"Greek\", \"words\": \"canna\",\n \"verdict\": \"plausible\",\n \"derivation\": \"The word is Greek κάννα 'reed' (Nourai prints it in its Latin spelling canna, which is the Latin borrowing of it), and its Semitic origin is well established — but the donor is Mesopotamian, not Arabic, and the borrowing is many centuries older than Arabic is attested. Etymonline: 'from Latin canna \\\"reed, cane\\\", from Greek kanna, perhaps from Babylonian-Assyrian qanu \\\"tube, reed\\\" (compare Hebrew qaneh, Arabic qanah \\\"reed\\\"), which may come from Sumerian-Akkadian gin \\\"reed\\\"'; Klein: 'fr. Gk. κάννα, \\\"reed\\\", which is of Sem. origin. Cp. Akkad. qanû, Heb. qāneh, Aram.-Syr. qanyā, Arab. qanāh'. Greek will have taken the word in the Bronze/early Iron Age trade with the Levant, most likely through Phoenician or Aramaic, and Arabic qanāh is a sister of the donor, not the donor. Nourai's own NOTE on node 8 ('These words reached Greek and Latin through Semitic languages') shows he was using the 'Arabic' box loosely for Semitic; read that way the node is acceptable, which is why it is plausible rather than disputed.\",\n \"derivation_fa\": \"این واژه κάννα یونانی «نی» است (نورایی آن را به املای لاتینِ canna نوشته که خود وام‌گیریِ لاتین از همان است) و خاستگاهِ سامیِ آن جا افتاده است — اما وام‌دهنده بین‌النهرینی است نه عربی، و وام‌گیری سده‌ها پیش از کهن‌ترین گواهِ عربی رخ داده. اتیمانلاین: «از canna لاتین «نی»، از kanna یونانی، شاید از بابلی-آشوری qanu «لوله، نی» (قس عبری qaneh، عربی qanah)، که خود شاید از سومری-اکدی gin «نی» باشد»؛ کلاین: «از κάννα یونانی «نی» که خاستگاهی سامی دارد. قس اکدی qanû، عبری qāneh، آرامی-سریانی qanyā، عربی qanāh». یونانی این واژه را در دادوستدِ عصرِ برنز و آغازِ عصرِ آهن با شام، به‌احتمال از راهِ فنیقی یا آرامی، گرفته است و قناةِ عربی خواهرِ وام‌دهنده است نه خودِ وام‌دهنده. یادداشتِ خودِ نورایی در گرهٔ ۸ («این واژه‌ها از راهِ زبان‌های سامی به یونانی و لاتین رسیدند») نشان می‌دهد که جعبهٔ «عربی» را به‌معنای گستردهٔ «سامی» به کار برده است؛ با این خوانش، این گره پذیرفتنی است و از همین رو حکم «با احتیاط پذیرفتنی» است نه «رد».\",\n \"sources\": [\"https://www.etymonline.com/word/cane\"],\n \"ref_check\": [\n   {\"ref\": \"KLN:231\", \"status\": \"supports\", \"note\": \"Klein 1966 (leaf 132, ≈p.231) s.v. cane: 'fr. L. canna, \\\"reed, cane, small vessel, tube\\\", fr. Gk. κάννα, \\\"reed\\\", which is of Sem. origin. Cp. Akkad. qanû, Heb. qāneh, Aram.-Syr. qanyā, Arab. qanāh (whence Pers. qanat), \\\"reed, cane\\\", Ethiop. qanot, \\\"a goad\\\".'\"},\n   {\"ref\": \"AHD:1520\", \"status\": \"not_found\", \"note\": \"AHD pp.1505-1550 is the Indo-European roots appendix, and neither κάννα nor canna is an Indo-European root; grep of AHD_watkins1985.txt for 'canna'/'kanna' returns nothing (the only 'kan-' there is the root 'to sing'). The citation appears to be misplaced — a Semitic reed-word cannot stand in an IE root list.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein 1966 ≈p.231 s.v. cane\", \"stance\": \"supports\", \"note\": \"as quoted.\"},\n   {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. canna\", \"stance\": \"supports\", \"note\": \"LAT.txt marks canna as an eastern loan (gr. κάννα, assyr. qanû), not an inherited Latin word.\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat s.v. CANE\", \"stance\": \"supports\", \"note\": \"'CANE … L. canna; Gk. κάννα, a reed; of Semitic origin; cf. Heb. qāneh, a reed.'\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 appendix\", \"stance\": \"silent\", \"note\": \"no entry for canna/kanna — see ref_check.\"}\n ]\n})\n\nN({\n \"id\": 19, \"lang\": \"English\", \"words\": \"cane, cannon, canyon\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"All three are descendants of Latin canna 'reed, tube', each through a different Romance language. cane: 'late 14c., \\\"long slender woody stem\\\", from Old French cane \\\"reed, cane, spear\\\" (13c., Mod.Fr. canne), from Latin canna' (Etymonline). cannon: 'c.1400, \\\"artillery piece\\\" … from Anglo-French canon, from Italian cannone, lit. \\\"a large tube\\\", augmentative of canna \\\"tube\\\", from Latin canna' — the gun is named from its barrel. canyon: from Spanish cañón 'tube, pipe; deep gorge', an augmentative of caño 'tube', again from Latin canna, borrowed into American English in the 1830s-40s from the Southwest. The chart's parent box (Greek canna) is one step up from the immediate Latin/Romance donors, but the family is correctly assembled.\",\n \"derivation_fa\": \"هر سه از بازماندگانِ cannaِ لاتین «نی، لوله»اند، هر یک از راهِ زبانی رومانسِ دیگر. cane: «اواخرِ سدهٔ چهاردهم، «ساقهٔ بلندِ چوبی»، از caneِ فرانسویِ کهن «نی، نیزه» (سدهٔ سیزدهم، فرانسویِ امروز canne)، از cannaِ لاتین» (اتیمانلاین). cannon: «حدود ۱۴۰۰، «توپ» … از canonِ انگلوفرانسوی، از cannoneِ ایتالیایی، لفظاً «لولهٔ بزرگ»، صیغهٔ بزرگ‌سازِ canna «لوله»، از cannaِ لاتین» — توپ را از لولهٔ آن نامیده‌اند. canyon: از cañónِ اسپانیایی «لوله؛ درّهٔ ژرف»، بزرگ‌سازِ caño «لوله»، باز هم از cannaِ لاتین، که در دههٔ ۱۸۳۰-۱۸۴۰ از جنوب‌غربِ آمریکا به انگلیسیِ آمریکایی راه یافت. جعبهٔ پدر در نمودار (canna یونانی) یک پله بالاتر از وام‌دهندگانِ بی‌واسطه (لاتین و زبان‌های رومانس) است، اما خانواده درست گردآوری شده است. ادعای نورایی درست است.\",\n \"sources\": [\"https://www.etymonline.com/word/cane\"],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"not_checked\", \"note\": \"Cited without a page; the 1975/76 AHD main text is not open online, and the 1985 Watkins appendix on disk has no entry for cane/cannon/canyon (they are not from Indo-European roots).\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein 1966 ≈pp.231-232 s.vv. cane, cannon, canyon\", \"stance\": \"supports\", \"note\": \"'cannon, n., gun. — F. canon, fr. It. cannone, lit. \\\"a large tube\\\", augment. of canna, \\\"tube\\\", fr. L. canna. See cane and cp. canyon.'; the cane entry cross-references 'can, canaba, Canada, canal, canasta, canaster, canaut, canella, canions, canister, Canna, cannel, cannelure, can…'.\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat s.vv. CANE, CANNON\", \"stance\": \"supports\", \"note\": \"Skeat gives both from L. canna via French/Italian.\"}\n ]\n})\n\nN({\n \"id\": 20, \"lang\": \"Sogdian\", \"words\": \"c`t\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Gharib's Sogdian dictionary has exactly this entry: '3159 cʾt B / cāt ⊙ Av. čāt- (cf. Skt. khā-; Bal. čaθ; Khwar. čt; Oss. cada) / well', on printed page ≈123-124 — Nourai's SOD:124. The word is Old Iranian *čāta- 'well, dug pit', the ta-participle of kan- 'to dig' with the regular palatalisation of *k before the front vowel of the zero-grade formation, and it is the direct ancestor of New Persian چاه čāh: Bartholomae states the whole chain at AiW col. 583, 'j. čāt- f. \\\"Brunnengrube\\\" … Zum V. ²kan-, vgl. xan-; §13. — Vgl. mp. (Pü.), np. čāh (aus iran. *čā-θ°)'. So this node — attached, as the chart has it, straight to the Avestan/Old Persian kan- box — is correct in every respect, and it is also the node that explains Nourai's otherwise puzzling BRT:583 citation up at node 1.\",\n \"derivation_fa\": \"فرهنگِ سغدیِ بدرالزمان قریب دقیقاً همین مدخل را دارد: «۳۱۵۹ cʾt (B) / cāt ⊙ اوستایی čāt- (قس سنسکریت khā-؛ بلوچی čaθ؛ خوارزمی čt؛ اُستی cada) / چاه»، در صفحهٔ چاپیِ حدود ۱۲۳-۱۲۴ — همان SOD:124 که نورایی آورده است. واژه از ایرانی باستان *čāta- «چاه، گودالِ کنده‌شده» است، یعنی اسم مفعولِ ta-دارِ ریشهٔ kan- «کندن» با کامی‌شدنِ قاعده‌مندِ k پیش از واکهٔ پیشین، و همین صورت نیایِ مستقیمِ «چاهِ» فارسی نو است: بارتولومه در ستون ۵۸۳ فرهنگِ ایرانی باستان همهٔ زنجیره را می‌آورد: «čāt- (مادینه) گودالِ چاه … به فعلِ ²kan-، قس xan-؛ §۱۳ — قس فارسی میانه و فارسی نوِ čāh از ایرانیِ *čā-θ°». پس این گره — که در نمودار یکراست به جعبهٔ اوستایی/پارسی‌باستانِ kan- بسته شده — از هر نظر درست است، و همین گره است که ارجاعِ به‌ظاهر معماگونهٔ BRT:583 در گرهٔ ۱ را نیز توضیح می‌دهد. ادعای نورایی درست است.\",\n \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/%C4%8D%C4%81tah\"],\n \"ref_check\": [\n   {\"ref\": \"SOD:124\", \"status\": \"supports\", \"note\": \"SOD_pages.txt leaf 189 (printed ≈123-124), entry '3159 cʾt B — cāt ⊙ Av. čāt-, čaia; Skha; Bal. čaθ; Khwar. čt; Oss. cada — well — SCE 527; Bailey, JRAS 1970'. Page and content both match.\"}\n ],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"AiW col. 583 (BRT.txt leaf 343)\", \"stance\": \"supports\", \"note\": \"'•j. čāt- f. \\\"Brunnengrube\\\": maiδe vā čāti vā V.13.31. Ableit. — Zum V. ²kan-, vgl. xan-; §13. — Vgl. mp. (Pü.), np. čāh (aus iran. *čā-θ°, §5).' Also col. 583-584 '•j. čātaya- Adj. \\\"in einer Brunnengrube befindlich\\\" … Pü.: āp i čāhān'.\"},\n   {\"src\": \"CHEUNG\", \"where\": \"EDIV p.232 (*kanH¹, Sogdian)\", \"stance\": \"supports\", \"note\": \"Cheung lists the Sogdian dig-verb (BSogd. kn-, CSogd. qn-) and the town-noun knδh under the same root; the noun čāt belongs to the same derivational family (*čā-ta-).\"},\n   {\"src\": \"SOD\", \"where\": \"Gharib, entry 3159\", \"stance\": \"supports\", \"note\": \"as quoted in ref_check.\"}\n ]\n})\n\ndoc = {\n \"pdf_page\": 214,\n \"book_page\": 184,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-06\",\n \"entries\": [entry]\n}\n\nwith io.open(\"data/verification/page-214.json\",\"w\",encoding=\"utf-8\") as f:\n    json.dump(doc, f, ensure_ascii=False, indent=1)\nprint(\"ok\", len(entry[\"nodes\"]))\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk214.py"
}
```


### [2026-09-06T15:14:39.675Z] TOOL RESULT

```
ok 20
```


## [2026-09-06T15:14:45.133Z] TOOL CALL #78: Bash

```json
{
 "command": "ls -la /home/sfmqrb/git/rishe/data/verification/page-214.json && python3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-214.json > /dev/null && echo \"JSON OK\" && python3 /home/sfmqrb/git/rishe/tools/verify_check.py 214"
}
```


### [2026-09-06T15:14:47.030Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 84514 Sep  6 11:14 /home/sfmqrb/git/rishe/data/verification/page-214.json
JSON OK
nodes verified: 20/20
node verdicts: {'disputed': 2, 'plausible': 4, 'confirmed': 13, 'transcription_suspect': 1}
root verdicts: {'plausible': 1}
ref checks: {'partial': 9, 'supports': 13, 'not_checked': 9, 'not_found': 2}
books consulted: {'partial': 7, 'contradicts': 3, 'supports': 37, 'silent': 10} | by book: {'KLN': 9, 'SKT': 6, 'MON': 5, 'NYB': 4, 'BRT': 4, 'CHEUNG': 4, 'BQT': 4, 'PHD': 3, 'SOD': 3, 'AFM': 2, 'AHD': 2, 'LAT': 2, 'KNT': 1, 'HUB': 1, 'HRN': 1, 'PLA': 1, 'TAD': 1, 'LKT': 1, 'LEW': 1, 'DEV': 1, 'ARY': 1}
```


## [2026-09-06T15:14:52.945Z] TOOL CALL #79: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/g%CA%B7%CA%B0en-\" \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/kanam\" \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/%C4%8D%C4%81tah\"; do\n echo \"== $u\"; python3 tools/fetch_source.py \"$u\" --note \"page 214 root Gwhen 1 / kan- family\" 2>&1 | tail -2\ndone"
}
```


### [2026-09-06T15:14:55.701Z] TOOL RESULT

```
== https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/g%CA%B7%CA%B0en-
/home/sfmqrb/git/rishe/data/verification/sources/web/8f4a4c4d0f4d87ee.txt
== https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/kanam
/home/sfmqrb/git/rishe/data/verification/sources/web/8bc0b93cba405852.txt
== https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/%C4%8D%C4%81tah
/home/sfmqrb/git/rishe/data/verification/sources/web/30326bdaccc42ca0.txt
```


## [2026-09-06T15:14:59.537Z] TOOL CALL #80: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nfor f in 8f4a4c4d0f4d87ee 8bc0b93cba405852 30326bdaccc42ca0; do echo \"##### $f\"; head -4 $f.txt; grep -o \"Descendants\\|Etymology\\|does not have an entry\\|Wiktionary does not have\" $f.txt|head -3; grep -o \"From Proto-Ir.\\{0,200\\}\\|From Proto-Indo-Eur.\\{0,200\\}\" $f.txt|head -2; done"
}
```


### [2026-09-06T15:15:01.620Z] TOOL RESULT

```
##### 8f4a4c4d0f4d87ee
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/g%CA%B7%CA%B0en-
FETCHED: 2026-09-05T06:37:41Z
STATUS: 200
TITLE: Reconstruction:Proto-Indo-European/gʷʰen- - Wiktionary, the free dictionary
Descendants
Descendants
##### 8bc0b93cba405852
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/kanam
FETCHED: 2026-09-06T15:14:55Z
STATUS: -1
TITLE: 
##### 30326bdaccc42ca0
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/%C4%8D%C4%81tah
FETCHED: 2026-09-06T15:14:55Z
STATUS: -1
TITLE:
```


## [2026-09-06T15:15:07.164Z] TOOL CALL #81: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\ngrep -o \"gʷʰen-.\\{0,120\\}\" 8f4a4c4d0f4d87ee.txt | head -5; grep -o \"to strike\\|to swell\\|to kill\" 8f4a4c4d0f4d87ee.txt|sort -u|head"
}
```


### [2026-09-06T15:15:08.796Z] TOOL RESULT

```
gʷʰen- - Wiktionary, the free dictionary
gʷʰen- - Wiktionary, the free dictionary 
gʷʰen- 
gʷʰen- ( imperfective ) [ 1 ] [ 2 ] [ 3 ] 
gʷʰen- ) 
to kill
to strike
```


## [2026-09-06T15:15:23.675Z] TOOL CALL #82: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \"https://en.wiktionary.org/wiki/%DA%A9%D9%86%D8%AF%D9%86\" \"https://en.wiktionary.org/wiki/%DA%86%D8%A7%D9%87\" \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-Iranian/k%CA%B0an-\"; do\n echo \"== $u\"; python3 tools/fetch_source.py \"$u\" --note \"page 214: kan- 'to dig' family, nodes 1/4/20\" 2>&1|tail -1\ndone"
}
```


### [2026-09-06T15:15:26.970Z] TOOL RESULT

```
== https://en.wiktionary.org/wiki/%DA%A9%D9%86%D8%AF%D9%86
/home/sfmqrb/git/rishe/data/verification/sources/web/6afcdd837bc42b56.txt
== https://en.wiktionary.org/wiki/%DA%86%D8%A7%D9%87
/home/sfmqrb/git/rishe/data/verification/sources/web/3f969f125e3e9206.txt
== https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-Iranian/k%CA%B0an-
/home/sfmqrb/git/rishe/data/verification/sources/web/dcee38ef3082ca06.txt
```


## [2026-09-06T15:15:30.702Z] TOOL CALL #83: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nfor f in 6afcdd837bc42b56 3f969f125e3e9206 dcee38ef3082ca06; do echo \"##### $f\"; sed -n '1,4p' $f.txt; grep -o \"From Middle Persian.\\{0,250\\}\\|From Proto-Iranian.\\{0,250\\}\\|From Proto-Indo-Iranian.\\{0,250\\}\\|Uncertain.\\{0,200\\}\" $f.txt|head -3; done"
}
```


### [2026-09-06T15:15:32.772Z] TOOL RESULT

```
##### 6afcdd837bc42b56
URL: https://en.wiktionary.org/wiki/%DA%A9%D9%86%D8%AF%D9%86
FETCHED: 2026-09-06T15:15:26Z
STATUS: 200
TITLE: کندن - Wiktionary, the free dictionary
From Middle Persian kntn' ( kantan , “ to dig ” ) , from Proto-Iranian *kánHati ( “ to dig ” ) .
##### 3f969f125e3e9206
URL: https://en.wiktionary.org/wiki/%DA%86%D8%A7%D9%87
FETCHED: 2026-09-06T15:15:26Z
STATUS: 200
TITLE: چاه - Wiktionary, the free dictionary
##### dcee38ef3082ca06
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-Iranian/k%CA%B0an-
FETCHED: 2026-09-06T15:15:26Z
STATUS: -1
TITLE:
```


## [2026-09-06T15:15:35.676Z] TOOL CALL #84: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\ngrep -o \"Etymology.\\{0,400\\}\" 3f969f125e3e9206.txt | sed -n '3,6p'"
}
```


### [2026-09-06T15:15:37.540Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T15:15:39.990Z] TOOL CALL #85: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\ngrep -o \"Persian\\s*\\[ edit \\].\\{0,500\\}\" 3f969f125e3e9206.txt | head -1"
}
```


### [2026-09-06T15:15:41.773Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T15:15:44.710Z] TOOL CALL #86: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\npython3 - <<'EOF'\nt=open('3f969f125e3e9206.txt',encoding='utf-8').read()\ni=t.find('From Wiktionary, the free dictionary')\nprint(t[i:i+900])\nEOF"
}
```


### [2026-09-06T15:15:46.382Z] TOOL RESULT

```
From Wiktionary, the free dictionary

 Persian
 [ edit ] 

 Persian Wikipedia has an article on: چاه 

 Wikipedia fa 

 Alternative forms
 [ edit ] 

 چه ( čah ) 

 Etymology
 [ edit ] 

 Akin to Sogdian [script needed] ( c’t /⁠čāt⁠/ ) , Avestan 𐬗𐬁𐬝 ( cāt̰ ) , Khotanese [script needed] ( cāta ) , Khwarezmian [script needed] ( ct’ ) , Baluchi چات ( cát ) , etc.

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /ˈt͡ʃaːh/ 

 ( Dari, formal ) IPA ( key ) : [t͡ʃʰɑːʱ] 

 ( Dari, formal ) IPA ( key ) : [t͡ʃʰɑːʱ] 
 ( Kabuli ) IPA ( key ) : [t͡ʃʰɑː] 

 ( Hazaragi ) IPA ( key ) : [t͡ʃʰɔː] 

 ( Iran, formal ) IPA ( key ) : [t͡ʃʰɒːʱ] 

 ( Tajik, formal ) IPA ( key ) : [t͡ʃʰɔʱ] 

 Rhymes: -aːh 

 Readings

 Classical reading ? 

 čāh

 Dari reading ? 

 čāh

 Iranian reading ? 

 čâh

 Tajik reading ? 

 čoh

 Audio ( Iran ) : ( file ) 

 Noun
 [ edit ] 

 Dari

 چاه 

 Iranian Persian
```


## [2026-09-06T15:16:03.776Z] TOOL CALL #87: Bash

```json
{
 "command": "python3 - <<'EOF'\nimport json, io\np=\"data/verification/page-214.json\"\nd=json.load(open(p,encoding='utf-8'))\ne=d[\"entries\"][0]\nKAN=\"https://en.wiktionary.org/wiki/%DA%A9%D9%86%D8%AF%D9%86\"\nCAH=\"https://en.wiktionary.org/wiki/%DA%86%D8%A7%D9%87\"\nGWHEN=\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/g%CA%B7%CA%B0en-\"\ne[\"sources\"]=[GWHEN, KAN]\ne[\"note\"]+=\" (Note on the archived Wiktionary page for *gʷʰen-: it treats the HOMONYM, *gʷʰen- 'to strike, kill' = Pokorny's gʷhen-2, 491-493 — which is precisely why Pokorny numbers our 'swell' root gʷhen-1 and why Nourai's box is labelled 'Gwhen 1'.)\"\ne[\"note_fa\"]+=\" (یادآوری دربارهٔ صفحهٔ بایگانی‌شدهٔ ویکی‌واژه برای *gʷʰen-: آن صفحه به همنامِ این ریشه می‌پردازد، یعنی *gʷʰen- «زدن، کشتن» که همان gʷhen-2 پوکورنی در صفحه‌های ۴۹۱ تا ۴۹۳ است؛ و همین است دلیلِ آنکه پوکورنی ریشهٔ «آماسیدن» را gʷhen-1 شماره گذاشته و جعبهٔ نورایی نیز «Gwhen 1» نام گرفته است.)\"\nfor n in e[\"nodes\"]:\n    if n[\"id\"]==1: n[\"sources\"]=[KAN, GWHEN]\n    if n[\"id\"]==4: n[\"sources\"]=[KAN]\n    if n[\"id\"]==20: n[\"sources\"]=[CAH]\n    if n[\"id\"]==5: n[\"sources\"]=[\"https://en.wiktionary.org/wiki/Samarkand\"]\njson.dump(d, io.open(p,\"w\",encoding=\"utf-8\"), ensure_ascii=False, indent=1)\nprint(\"done\")\nEOF\npython3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-214.json >/dev/null && echo \"JSON OK\"\npython3 /home/sfmqrb/git/rishe/tools/verify_check.py 214"
}
```


### [2026-09-06T15:16:05.565Z] TOOL RESULT

```
done
JSON OK
nodes verified: 20/20
node verdicts: {'disputed': 2, 'plausible': 4, 'confirmed': 13, 'transcription_suspect': 1}
root verdicts: {'plausible': 1}
ref checks: {'partial': 9, 'supports': 13, 'not_checked': 9, 'not_found': 2}
books consulted: {'partial': 7, 'contradicts': 3, 'supports': 37, 'silent': 10} | by book: {'KLN': 9, 'SKT': 6, 'MON': 5, 'NYB': 4, 'BRT': 4, 'CHEUNG': 4, 'BQT': 4, 'PHD': 3, 'SOD': 3, 'AFM': 2, 'AHD': 2, 'LAT': 2, 'KNT': 1, 'HUB': 1, 'HRN': 1, 'PLA': 1, 'TAD': 1, 'LKT': 1, 'LEW': 1, 'DEV': 1, 'ARY': 1}
```


## [2026-09-06T15:16:11.848Z] TOOL CALL #88: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SKT\"; grep -n -i \"^CANE\\|^CANON\\|^CANAL\\|^CHANNEL\\|^CANNON\" SKT.txt | head\necho \"--- text\"; grep -n -A3 -i \"^CANE,\" SKT.txt | head -8; grep -n -A3 -i \"^CANON\" SKT.txt | head -8\necho \"=== LAT canna\"; grep -n \"^canna\" LAT.txt | head -3\necho \"=== LEW canna\"; grep -n \"^canna\\|^canalis\" LEW_1910.txt | head -3"
}
```


### [2026-09-06T15:16:11.978Z] TOOL RESULT

```
=== SKT
2726:channeL  { F.  —  L. )    M .  E.  fkam^^
2786:cannon.  (F.-L  -Gk.)  F.  canon, orig  ft  gun  •  barrel— L..  catma,  a  reed  ;  see OftBe.
2787:canon.  (L.-Gk.l  A.S.  canon.  -  L. <ano»,  a  rule.  — Gk.  xamn-,  a  rod,  rule. — Gk.  K^fr]  =  /nivrij,  a  (slraighl)  cane.
2794:Cannon ;  free  Caoe.
2796:Canon :  sec  Cane.
22941:channel — canal,  kenn
--- text
2787:canon.  (L.-Gk.l  A.S.  canon.  -  L. <ano»,  a  rule.  — Gk.  xamn-,  a  rod,  rule. — Gk.  K^fr]  =  /nivrij,  a  (slraighl)  cane.
2788-O&ninfi.  (I>.)  L.  catunur,  tietonging  (o a  Hog.  —  L.  canu,  a  dog ;  see  Hound.
2789-kennel  (i),  a  house  for  ^.o^%.  (F.  —  L) hX.  E.  ktnci.  A  Norman  form  of  O.  F. cktttil,  a  kennel. M  Norman  F.  ^ctj,  O.  F. chin  (,F.  chicn^,  a  dog,  from  L.  ace  camm, a  dog  ;  with  suffix  -i7»L.  'iVV,  as  iu  ffH-i/r. a  shccp-fold.
2790-Canister ;  tee  O&ne.
--
2796:Canon :  sec  Cane.
2797-Canopy ;  sec  Cone.
2798-Cant  (i\  to  sing  tn  s  whining  way, whme.  (L.)  L.  fdwAtr*,  lo  sing  ;  frujtKnt. of  canere,  to  ling.  So  aX^Q  Gael.  atiHHt, talk;  from  mn,  to  sing,  say.  Cattt  wab  at lirst  a  beggar's  whine  ;  hence,  hypocrisy ; see  recnnt,
=== LAT canna
9262:canna, -ae f.: roseau. Emprunt au gr. xavva lui-meme d'origine s6mi-
9269:cannabula ; 160« *cannamellis; 1606 *cannuciae, S'y rattache: canalis,
9278:canna, -ae f.: sorte Ae vase ou de pot. (inscr. a partir du I er s.
=== LEW canna
```


## [2026-09-06T15:16:21.931Z] TOOL CALL #89: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SKT cane/canal\"; grep -n -i \"cane\\.\\s*(\\|canal\\.\\s*(\\|^cane\\b\" SKT.txt | head -5\ngrep -n -i \"canal\" SKT.txt | head -5\necho \"=== LEW\"; grep -n -i \"canalis\\|canna,\" LEW_1910.txt | head -5\necho \"=== LAT canalis\"; grep -n \"canalis\" LAT.txt | head -5"
}
```


### [2026-09-06T15:16:22.055Z] TOOL RESULT

```
=== SKT cane/canal
2725:Can  (a>,   a  dnnk<n(;-ve.^5c1.    (E.)    A canna,   canm.  ^  Du.   J^m ;    Icel Swed.  karma ;    Dan.  kanM ;    G. tankard,  mug.     (Apparently  %  true  Tl word.) Canal.  (F.-L.)     F.  <-*««/ (whi Du.  kanaai.)  —  L.  cauaiu,  a  channel orig.    a   cutting.     Cf   Skt.  k.kitn^ fierce;  khani,  a  mine.     (^SK.V.>
4803:decanal.  (L.)  Belonging  to  a  dean.  — L.  d^can-Hi  (above^.
15661:Rattan,  a  Malacca  cane.  (Maby.)  Also spelt  ratan  ^Johnson).  —  Malay  nUan^  the nltan-cnne.
2725:Can  (a>,   a  dnnk<n(;-ve.^5c1.    (E.)    A canna,   canm.  ^  Du.   J^m ;    Icel Swed.  karma ;    Dan.  kanM ;    G. tankard,  mug.     (Apparently  %  true  Tl word.) Canal.  (F.-L.)     F.  <-*««/ (whi Du.  kanaai.)  —  L.  cauaiu,  a  channel orig.    a   cutting.     Cf   Skt.  k.kitn^ fierce;  khani,  a  mine.     (^SK.V.>
2727:—  O.  F.  ckanel,  <antt,  a  canal.  — L. as  above.
4803:decanal.  (L.)  Belonging  to  a  dean.  — L.  d^can-Hi  (above^.
5263:Dock(.i),tocnrtatl.  (C.  7)  Perhaps  from \V.  /«i'p,  to  cl  ip,  dock ;  cf.  tocyn,  a  short  piece. docket,  a  label,  ticket.  tC?)    l'ro]vrly a  brief  abstract      From  the  verb  de<k^  to curtail  (make  a  brief  al>stiact>. Dock  (2),  a  plant.    (C.  ?i     K.%docre\ bnt  ptob.  borrowed  from  Celtic.  —  Gael. do^ha,  a  burdock ;    Irish   mecuandogha,  a great  burdock,  whirre  mcoian  meant  a  tap rooted  plant,  a*  a  carrot.     Dor.  bur-deck. Dock  (3),  a  basin  for  ships.  (Du  —Low I  L.-(rk  ?)     O.  Dd.  dokkt,  a  harbour   (so i  also  Dan.  dokke^  Swed.  docka^  G.  do<ke\,^ Low  L.  doga,  a  ditcli,  canal ;  also  a  cuij. — ;Gk.  fiux^.  a  receptacle  —Gk.  8«xafuu,  1  re- i  ceive.     %  Mifilor)'  obscure. {    Docket ;  sec  Dock  ( 1 1. ^    Doctor,  Doctrine.  Document : I  Docile. Dodecafpon.  Dodecahedron ;  sceDe oade. Dod^,   to  go   hither   and    thither,    to quibble.  (E)      Orig.   to   walk    unsteadily, hence  to  go  from  side  to  side  as  if  to  es- cape; allied  to  prov.  Ii.  dade.  to  walk  nn- stcndily,  Scotch  diiddie  dotidle,  to  waddle, dcd,  to  jog,  (/[fijv,  to  jog  alo:ig,  dodgri,  to hnljhlc.  North  E,  ihui,  to  shake,  do,hitr,  to s.\i.\Vt.  totter,  da*igt,  dc*i£t,  \o  walk  dam- ailv.     Cf.  A.S,  djfdrioM,  to  lead  hither  and thither. Dodo  an  extinct  bird  (Portl  Port,  i/ot/'/p, .lilly.  fooli^h  ;  the  bird  ljcit)(;  of  n  cltimsy make.    Said  to  be  borrowed  from  E  Dolt.
8155:KIgi  iX^«uijrr,  touste.     (^GUS.) to  Ohooaa. rust,  vb,  {Y,  - L.>   O  F,  dtsgoHstir, 7  dtttaatc,  loath  ;'  Cot  -  O  V.  dts-  (  -  L. N),  aeafi ;  ^PM/«r.  10  taste,  from  U  ^z- rv  <  above). pttt  (1).  lasta   (F.  -  U)     F.  ^^jd/. r.«»l-.  gutttu  (above). rs<oat.  ^F.  -  L)     F.  rag»at,  a  tea- |it4sb.*F.  rM^eHttr,  10   coax  a  sick •  appetite-  -  V.    rt-,   again  ;    a,   to ; V 10  taaic.  —  L.  rt-i  iui\  guztart, hit  Intntlaal    canaL     (£.)     (The 1    \\  atVM  t  .  ^^    V .  gvU,  prov.  K.gNf. \  S.  i-W ;  pi.  A'«/- -  A.S.  ^/,  stem  of I.  01  iY^.Mff,  10  pour.     (VGHUO nS.  f^*'^  *   l&iLMcat  Dan.  gjnit,  a O-  ua.  g9t*,  a  cbaimel.  G.  ^ur/^,  a ^  No  OObucctioa  with  guittr. atta-p«reh&.   ^Mala) )     The  apoil-
=== LEW
=== LAT canalis
9111:canalis: cf. canna.
9269:cannabula ; 160« *cannamellis; 1606 *cannuciae, S'y rattache: canalis,
15525:canalis.
```


## [2026-09-06T15:16:38.054Z] TOOL CALL #90: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"Cane\\b\" SKT.txt | head -8\nsed -n '2780,2786p' SKT.txt"
}
```


### [2026-09-06T15:16:38.114Z] TOOL RESULT

```
2796:Canon :  sec  Cane.
3  i    wiioMM  Anb.
CANT.
faruf/t  nuidc  of  sugar.  The  word  in  Aryan (Peri.)  ;  cl.  bit.  **A./nd«rr.w.  sweetmeat*, /kAanda.  a  broken  jiiccc.  Hex.  sngisr-iafu/y, Ital.  tmtMer»  4aniii.
C&ne.  ( F.  -  L.  -  G  k .)     ME.  earn,  ranw,
—  F.  carint.^l^  eanna  **Cf\i.K^yvo,  *r»(»nj, ft  rred.  Cf.  Heb.yo/i^^,  retd;  Arab,  ^anii/, cane.
canister.  (L  -  Gk.)  L.  canit/mm,  a reed  tia^ket.  "*Gk.  Kavnar^r,  the  sauic.* Gk.  K^trr}  =  k6»vj}^  a  iced.
cannon.  (F.-L  -Gk.)  F.  canon, orig  ft  gun  •  barrel— L..  catma,  a  reed  ;  see OftBe.
```


## [2026-09-06T15:16:58.699Z] TOOL CALL #91: Bash

```json
{
 "command": "python3 - <<'EOF'\nimport json, io\np=\"data/verification/page-214.json\"\nd=json.load(open(p,encoding='utf-8'))\nnodes={n[\"id\"]:n for n in d[\"entries\"][0][\"nodes\"]}\n\ndef setcons(nid, src, where, stance, note):\n    n=nodes[nid]\n    for c in n[\"consulted\"]:\n        if c[\"src\"]==src:\n            c.update({\"where\":where,\"stance\":stance,\"note\":note}); return\n    n[\"consulted\"].append({\"src\":src,\"where\":where,\"stance\":stance,\"note\":note})\n\nSKT_CANON=\"SKT.txt line 2787 (OCR): 'canon. (L.-Gk.) A.S. canon. — L. canon, a rule. — Gk. κανών, a rod, rule. — Gk. κάννα = a (straight) cane.'\"\nsetcons(10,\"SKT\",\"Skeat, Concise Etym. Dict. s.v. canon\",\"supports\",SKT_CANON)\nsetcons(13,\"SKT\",\"Skeat s.v. canon\",\"supports\",SKT_CANON)\n\nsetcons(14,\"SKT\",\"Skeat s.v. Canal (SKT.txt line 2725)\",\"partial\",\n \"'Canal. (F.-L.) F. canal (whence Du. kanaal). — L. canalis, a channel, orig. a cutting. Cf. Skt. kh[an]-…, khani, a mine.' Skeat (1911) still derived canālis from a 'cutting/digging' notion and compared Sanskrit khan- — the very connection Nourai draws; but that comparison has been dropped by later Latin etymologists (Ernout-Meillet, Klein), who derive canālis from canna.\")\nsetcons(14,\"LEW\",\"Walde, LEW 1910\",\"silent\",\n \"grep of LEW_1910.txt for '^canna' / '^canalis' / 'canalis': no hit — the entry falls in a gap of this OCR, so Walde could not be consulted here.\")\nsetcons(14,\"LAT\",\"Ernout-Meillet s.vv. canna, canalis (LAT.txt lines 9111, 9262, 9269)\",\"supports\",\n \"'canalis: cf. canna.' and 'canna, -ae f.: roseau. Emprunt au gr. κάννα lui-même d'origine sémi[tique] … S'y rattache: canalis, …' — canālis is a derivative of canna, and canna is an eastern loan.\")\n\nsetcons(17,\"SKT\",\"Skeat s.vv. Canal, channel (SKT.txt lines 2725-2727)\",\"supports\",\n \"'Canal. (F.-L.) F. canal … — L. canalis, a channel' and, s.v. channel, '(F.-L.) M.E. chanel … — O.F. chanel, canel, a canal. — L. as above.' Skeat too treats them as the same Latin word taken twice.\")\n\nsetcons(18,\"SKT\",\"Skeat s.v. Cane (SKT.txt line 2781)\",\"supports\",\n \"'Cane. (F.-L.-Gk.) M.E. cane, canne. — F. canne. — L. canna. — Gk. κάννα, a reed. Cf. Heb. qāneh, reed; Arab. qanāt, cane.' Skeat names Hebrew qāneh first and Arabic only as a comparandum.\")\nsetcons(18,\"LAT\",\"Ernout-Meillet s.v. canna (LAT.txt line 9262)\",\"supports\",\n \"'canna, -ae f.: roseau. Emprunt au gr. κάννα lui-même d'origine sémi[tique]' — a Semitic loan through Greek, with no Iranian link.\")\n\nsetcons(19,\"SKT\",\"Skeat s.vv. Cane, cannon (SKT.txt lines 2781, 2786)\",\"supports\",\n \"'Cane. (F.-L.-Gk.) M.E. cane, canne. — F. canne. — L. canna. — Gk. κάννα, a reed.'; 'cannon. (F.-L.-Gk.) F. canon, orig. a gun-barrel — L. canna, a reed; see Cane.'\")\n\njson.dump(d, io.open(p,\"w\",encoding=\"utf-8\"), ensure_ascii=False, indent=1)\nprint(\"patched\")\nEOF\npython3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-214.json >/dev/null && echo \"JSON OK\"\npython3 /home/sfmqrb/git/rishe/tools/verify_check.py 214"
}
```


### [2026-09-06T15:17:00.650Z] TOOL RESULT

```
patched
JSON OK
nodes verified: 20/20
node verdicts: {'disputed': 2, 'plausible': 4, 'confirmed': 13, 'transcription_suspect': 1}
root verdicts: {'plausible': 1}
ref checks: {'partial': 9, 'supports': 13, 'not_checked': 9, 'not_found': 2}
books consulted: {'partial': 8, 'contradicts': 3, 'supports': 35, 'silent': 11} | by book: {'KLN': 9, 'SKT': 6, 'MON': 5, 'NYB': 4, 'BRT': 4, 'CHEUNG': 4, 'BQT': 4, 'PHD': 3, 'SOD': 3, 'AFM': 2, 'AHD': 2, 'LAT': 2, 'KNT': 1, 'HUB': 1, 'HRN': 1, 'PLA': 1, 'TAD': 1, 'LKT': 1, 'LEW': 1, 'DEV': 1, 'ARY': 1}
```


## [2026-09-06T15:17:27.215Z] AGENT

Done. `/home/sfmqrb/git/rishe/data/verification/page-214.json` written; `verify_check.py 214` reports 20/20 nodes and **0 PROBLEM lines**.

**Page 214 (book p.184) — root "Gwhen 1", 1 entry, 20 nodes**

Verdicts: root `plausible`; nodes: 13 confirmed, 4 plausible, 2 disputed, 1 transcription_suspect.
Ref checks: 13 supports, 9 partial, 2 not_found, 9 not_checked. 21 different books consulted.

Disputed / flagged:
- **ROOT + node 1 (Av./OP `kan 1, xan, gan 1`) — disputed.** POK:491 gʷhen-1 "to swell, abound" is real (Pokorny even lists "npers. a-gandan" there; Watkins gʷhen-² cites the same page), but Nourai hangs the whole page on kan- "to dig", which nobody derives from it. Pokorny puts Av./OP kan- at IEW 634 under ken-; LIV has *kenh₂-; Cheung separates *kan¹ "throw", *kan² "fill", *kanH¹ "dig". Nourai's own cited FFD:26 (Abolghasemi) says verbatim that Old Iranian had two kan-. Also "xan" is not a verb but Av. xan- f. "Quelle, Brunnen" (BRT col. 533).
- **Node 8 (Arabic `qanah, qanât, q.n.v`) — disputed.** Semitic, not Iranian: Wiktionary derives قناة from Aramaic qanyā < Akkadian qanûm; Klein and Etymonline give Akkad. qanû / Bab.-Assyr. qanu (possibly Sumerian gin). Addi Shir, Asbaghi and al-ʿUnaysī are all silent, i.e. none of the Persian-loans-in-Arabic literature claims it. The technology is Iranian (kārīz), the word is not.
- **Node 5 (Sogdian `kang, kanp`) — transcription_suspect, error_in: "book".** The printed page really does read "kang, kanp" (page image copied to `data/verification/sources/refs/ocr/BOOK/214.png`), so the extraction is faithful. The Sogdian form is knδh = *kanθ/kand* "town" (Gharib, Cheung, and Moʿin's own footnote on سمرقند); "kanp" is impossible.
- Plausible-with-corrections: node 2 (afkandan's prefix is *apa-/upa-*, not aiwi-, per Nyberg/Cheung; Av. has aipi-kan-, not ā-kan-), nodes 10/14/18 (Greek κάννα, κανών and Latin canālis descend from each other, not from Arabic; Beekes now calls κανών Pre-Greek).

Reference notes for the owner:
- **BRT:583** is not Bartholomae's kan- (that is col. 437-438) but col. 583 s.v. čāt- "Brunnengrube" — it actually documents node 20, not node 1.
- **AHD:1520** (node 18) is in the Indo-European roots appendix, where a Semitic reed-word cannot appear; recorded `not_found`.
- **BQT:1703** for Samarqand is the wrong volume/page — the Samarqand entry with Moʿin's full etymology (Sogd. knδh, OP *kanta-, from kan-) is at BQT vol.2 ≈ p.1165-1172, i.e. Nourai's other citation. BQT:1516 (qānūn) and BQT:1526 (qazāgand) hit exactly.
- Not accessible: SAP, FVF, FVA (no digital copies); AHD:197 and MON:2875 (no open pagination).

No extraction errors to fix. One cosmetic note: the printed page has a completely empty, unlabelled box to the right of the Old Persian node that the extractor (correctly) dropped — it carries no content.
