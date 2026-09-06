# Verification process log — verify-page-189


## [2026-09-05T21:00:51.129Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 189 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-189.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-189.json. Write /home/sfmqrb/git/rishe/data/verification/page-189.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 189` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-05T21:00:52.439Z] AGENT

I'll start by reading the instructions.


## [2026-09-05T21:00:53.179Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-05T21:00:53.190Z] TOOL RESULT

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


## [2026-09-05T21:00:53.651Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-189.txt"
}
```


### [2026-09-05T21:00:53.665Z] TOOL RESULT

```
1	=== PDF page 189 (book page 159) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Gher 3; Ghrěi, Ghreu : to scratch, scrape away; to rub, grind  (refs OEW:120; POK:439,457)
4	#1 (parent #0) [Sanskrit] refs=OEW:120 | ghat : a place where sins are wiped away, a shrine
5	#2 (parent #0) [Greek] refs=OEW:120 | xriein, khriein : anoint ; Christ : the anointed
6	  #3 (parent #2) [English] refs=OEW:120 | Christ, Christian, Christmas
7	    #4 (parent #3) [Persian] refs=VOP:281 | krîsmas «کریسمس» : Christmass
8	  #5 (parent #2) [Turkish] refs=OEW:120 | xorozma : anointment
9	    #6 (parent #5) [Old French] refs=OEW:120 | cresme
10	      #7 (parent #6) [French] refs=KLN:369 | creme
11	        #8 (parent #7) [Persian] refs=VOP:280 | kerem «کِرِم» : cream
12	        #9 (parent #7) [English] refs=KLN:369 | cream
13	#10 (parent #0) [Greek] refs=AHD:240 | xrôs : skin, rough surface ; xroma : complexion, color
14	  #11 (parent #10) [French] refs=AHD:240 | chrome
15	    #12 (parent #11) [Persian] refs=VOP:281 | korom «کُرُم» : chromium ; koromosom «کرموزُم» : chromosome
16	    #13 (parent #11) [English] refs=AHD:240 | chrome, chromium, chromosome
17	#14 (parent #0) [Greek] refs=AHD | kharax, xarax : a pointed stake, character
18	  #15 (parent #14) [English] refs=AHD | character
19	#16 (parent #0) [Germanic] refs=AHD | grautaz : coarse, large
20	  #17 (parent #16) [English] refs=AHD | great
21	#18 (parent #0) [Celtic] refs=AHD | graw : rough surface, gravel
22	  #19 (parent #18) [English] refs=AHD | gravel
23	--- entry 1 ---
24	ROOT [Indo-European] Gher 4 : to wish, desire, want  (refs POK:440)
25	#1 (parent #0) [Avestan] refs=POK:440 | zara 2 : desire, aim, target
26	  #2 (parent #1) [None] refs=None | 
27	#3 (parent #0) [Germanic] refs=AHD | gernjan : want ; grěduz : hunger
28	  #4 (parent #3) [English] refs=AHD | yearn ; greed, greedy
29	#5 (parent #0) [Latin] refs=AHD | hortârî : to urge
30	  #6 (parent #5) [English] refs=AHD | exhort
31	#7 (parent #0) [Greek] refs=AHD | khoris. xoris : grace
32	  #8 (parent #7) [English] refs=AHD | charisma, charismatic
33	
```


## [2026-09-05T21:00:56.823Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-189.json",
 "description": "Read source JSON for page 189"
}
```


### [2026-09-05T21:00:56.860Z] TOOL RESULT

```
{
  "pdf_page": 189,
  "book_page": 159,
  "entries": [
    {
      "root": {
        "name": "Gher 3; Ghrěi, Ghreu",
        "lang": "Indo-European",
        "refs": "OEW:120; POK:439,457",
        "gloss": "to scratch, scrape away; to rub, grind"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "OEW:120",
          "words": [
            {"translit": "ghat", "gloss": "a place where sins are wiped away, a shrine", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 0,
          "lang": "Greek",
          "refs": "OEW:120",
          "words": [
            {"translit": "xriein, khriein", "gloss": "anoint", "script": null},
            {"translit": "Christ", "gloss": "the anointed", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "English",
          "refs": "OEW:120",
          "words": [
            {"translit": "Christ, Christian, Christmas", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Persian",
          "refs": "VOP:281",
          "words": [
            {"translit": "krîsmas", "gloss": "Christmass", "script": "کریسمس"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 2,
          "lang": "Turkish",
          "refs": "OEW:120",
          "words": [
            {"translit": "xorozma", "gloss": "anointment", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "Old French",
          "refs": "OEW:120",
          "words": [
            {"translit": "cresme", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "French",
          "refs": "KLN:369",
          "words": [
            {"translit": "creme", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 7,
          "lang": "Persian",
          "refs": "VOP:280",
          "words": [
            {"translit": "kerem", "gloss": "cream", "script": "کِرِم"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 7,
          "lang": "English",
          "refs": "KLN:369",
          "words": [
            {"translit": "cream", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 0,
          "lang": "Greek",
          "refs": "AHD:240",
          "words": [
            {"translit": "xrôs", "gloss": "skin, rough surface", "script": null},
            {"translit": "xroma", "gloss": "complexion, color", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 10,
          "lang": "French",
          "refs": "AHD:240",
          "words": [
            {"translit": "chrome", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 11,
          "lang": "Persian",
          "refs": "VOP:281",
          "words": [
            {"translit": "korom", "gloss": "chromium", "script": "کُرُم"},
            {"translit": "koromosom", "gloss": "chromosome", "script": "کرموزُم"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 13,
          "parent": 11,
          "lang": "English",
          "refs": "AHD:240",
          "words": [
            {"translit": "chrome, chromium, chromosome", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 14,
          "parent": 0,
          "lang": "Greek",
          "refs": "AHD",
          "words": [
            {"translit": "kharax, xarax", "gloss": "a pointed stake, character", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 15,
          "parent": 14,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "character", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 16,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "grautaz", "gloss": "coarse, large", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 17,
          "parent": 16,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "great", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 18,
          "parent": 0,
          "lang": "Celtic",
          "refs": "AHD",
          "words": [
            {"translit": "graw", "gloss": "rough surface, gravel", "script": null}
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
            {"translit": "gravel", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Gher 4",
        "lang": "Indo-European",
        "refs": "POK:440",
        "gloss": "to wish, desire, want"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:440",
          "words": [
            {"translit": "zara 2", "gloss": "desire, aim, target", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": null,
          "refs": null,
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "gernjan", "gloss": "want", "script": null},
            {"translit": "grěduz", "gloss": "hunger", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "yearn", "gloss": null, "script": null},
            {"translit": "greed, greedy", "gloss": null, "script": null}
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
            {"translit": "hortârî", "gloss": "to urge", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "exhort", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 0,
          "lang": "Greek",
          "refs": "AHD",
          "words": [
            {"translit": "khoris. xoris", "gloss": "grace", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 7,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "charisma, charismatic", "gloss": null, "script": null}
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


## [2026-09-05T21:00:58.912Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['OEW','POK','AHD','KLN','VOP','WLD','IEC','SYN','BRT','KNT','PHD','NYB','HRN','HUB','MON','BQT','ARY','SKT','FSD','WEB','CHEUNG']:\n    v=d.get(k)\n    print(k, json.dumps(v, ensure_ascii=False)[:400] if v else 'MISSING')\n\""
}
```


### [2026-09-05T21:01:00.725Z] TOOL RESULT

```
OEW {"title": "J. T. Shipley, The Origins of English Words: A Discursive Dictionary of Indo-European Roots, Baltimore 1984", "edition_found": "1984 (lending-only)", "kind": "archive_restricted", "url": "https://archive.org/details/originsofenglish0000ship ; https://archive.org/details/originsofenglish00jose (both JHU 1984, borrowable) ; HathiTrust mdp.49015002910322 search-only ; Google ELSm5zUgP_wC n
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
VOP {"title": "Mahshid Moshiri, Farhang-e Vazheha-ye Orupayi dar Farsi, Alborz 1371/1992", "kind": "none", "url": null, "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: not found (only unrelated similar-title books, e.g. Zomorrodian's فرهنگ ریشه‌شناختی واژه‌های دخیل اروپایی, ketabnak 132354).", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 2026-09:
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sou
KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "loca
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verific
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-D
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-di
CHEUNG MISSING
```


## [2026-09-05T21:01:50.065Z] TOOL CALL #5: Bash

```json
{
 "command": "ls data/verification/sources/refs/ && echo ---- && sed -n 1,120p data/verification/sources/SOURCE_MATRIX.md"
}
```


### [2026-09-05T21:01:50.107Z] TOOL RESULT

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
NYB.txt
NYB_vol1.txt
NYB_vol2_glossary.txt
ocr
pageimg
PEI.txt
PHD_mackenzie.pdf
PHD_mackenzie.txt
PHD_pages.txt
PHD.pdf
PHD.txt
PHN.txt
POK_01.txt
POK_02.txt
POK_03.txt
POK_full.txt
RCH.txt
SBK.txt
SDQ.txt
SIN.txt
SKT.txt
SNS_pages.txt
SNS.txt
SOD_pages.txt
SOD.txt
SPG_keilinschriften1881.txt
SYN.txt
TAD_pages.txt
TAD.txt
tessdata
TLM.txt
UNV.txt
WEB_vol1.txt
WLD_band3.txt
ZAP.txt
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
```


## [2026-09-05T21:01:52.567Z] TOOL CALL #6: Bash

```json
{
 "command": "pdftoppm -f 189 -l 189 -r 300 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg189 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/"
}
```


### [2026-09-05T21:01:54.991Z] TOOL RESULT

```
total 24508
drwx------ 2 sfmqrb sfmqrb    4096 Sep  5 17:01 .
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
-rw-rw-r-- 1 sfmqrb sfmqrb   98352 Sep  5 17:01 pg178_hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   64024 Sep  5 17:01 pg178.png
-rw-rw-r-- 1 sfmqrb sfmqrb   57139 Sep  5 16:54 pg179.png
-rw-rw-r-- 1 sfmqrb sfmqrb   81598 Sep  5 16:58 pg180.png
-rw-rw-r-- 1 sfmqrb sfmqrb   56794 Sep  5 17:00 pg181.png
-rw-rw-r-- 1 sfmqrb sfmqrb   66020 Sep  5 17:01 pg182.png
-rw-rw-r-- 1 sfmqrb sfmqrb   77310 Sep  5 16:58 pg184.png
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


## [2026-09-05T21:01:58.278Z] TOOL CALL #7: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg189.png"
}
```


### [2026-09-05T21:01:58.823Z] TOOL RESULT

```

```


## [2026-09-05T21:01:58.819Z] INPUT

[Image: original 2550x3300, displayed at 1546x2000. Multiply coordinates by 1.65 to map to original image.]


## [2026-09-05T21:02:37.027Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg189.png')\nprint(im.size)\n# persian scripts: node12 box approx x 1400-1960, y 1050-1240 (in 2550x3300)\nim.crop((1380,1030,1970,1250)).resize((1180,440)).save('p189_n12.png')\nim.crop((1250,1980,1970,2120)).resize((1440,280)).save('p189_empty.png')\nim.crop((560,2400,1000,2520)).resize((1320,360)).save('p189_khoris.png')\nim.crop((560,750,1000,930)).resize((1320,540)).save('p189_greek2.png')\n\""
}
```


## [2026-09-05T21:02:38.680Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"ghrēi\\|ghrei-\\|ghrēu\\|ghreu-\" AHD_watkins1985.txt | head -40; echo \"=== gher\"; grep -n \"^gher\\|gher-1\\|gher-2\\|gher-3\\|ĝher\" AHD_watkins1985.txt | head -30"
}
```


### [2026-09-05T21:02:39.238Z] TOOL RESULT

```
(2550, 3300)
```


### [2026-09-05T21:02:39.288Z] TOOL RESULT

```
=== gher
219:ghers-. 2. Lengthened-grade form
521:gher-'. To grasp, enclose; with derivatives meaning “enclosure.” 1. Suffixed zero-grade form *ghr-dh- in: a. Germanic *gurdjan in Old English gyrdan, to gird: GIRD; b. Old English gyrdel, girdle: GIRDLE; c. Old Norse gjordh, girdle, girth: GirTH. 2. Suffixed o-grade form *ghor-dho- (in Germanic) or *ghor-to-, an enclosure, in: a. Germanic *gardaz in (i) Old English geard, enclosure, garden, yard: YARD?; ORCHARD (ii) Old Norse gardhr, garden, yard: GARTH (iii) Old High German garto, gar- den: KINDERGARTEN (iv) Old North French gardin, gar- den: GARDEN (v) compound *midja-gardaz, “middle zone,” earth (see medhyo-); b. Latin hortus, garden: HORTICULTURE, ORCHARD, ORTOLAN. 3. Prefixed and suffixed zero-grade form *ko(m)-ghr-ti- (*ko(m)-, collec- tive prefix, “together”; see kom) in Latin cohors (stem cohort-), enclosed yard, company of soldiers, multitude: COHORT, CORTEGE, COURT, COURTEOUS, COURTESAN, (COURTESY), COURTIER, (CURTILAGE), (CURTSY). 4. Per- haps suffixed o-grade form *ghor-o- in Greek khoros, dancing ground (? perhaps originally a special enclosure for dancing), dance, dramatic chorus: (CHOIR), (CHORAL), (CHORALE), CHORIC, (CHORISTER), CHORUS; CHORAGUS, TERPSICHORE. [Pok. 4. gher- 442, gherd- 444.]
522:gher-2. To call out. Extended root *ghréd-. Germanic *grotjan in Old English grétan, to speak to, greet: GREET. [Pok. 1. gher- 439.]
524:gher-’. To shine, glow; gray. Hypothetical base of various Germanic forms. 1. Germanic *gréwaz, gray, in: a. Old English greg, gray: GRAY; b. probably Old English grighund, greyhound: GREYHOUND. 2. Germanic *gris- Jaz, gray, in: a. Old French gris (> French gris), gray: GRISAILLE, (GRISETTE), (GRISON), GRIZZLE; AMBERGRIS; b. Medieval Latin griseus, gray, grayish: GRISEOUS. [Pok. 3. gher- 441.] gher-4. To scrape, scratch. 1. Extended zero-grade form *ghr(e)-k- in: a. Greek kharax, a pointed stake, also a kind of sea bream: CHARACIN; b. Greek kharassein, to sharpen, notch, carve, cut: CHARACTER, GASH. 2. Ex- tended form *ghers-.in suffixed zero-grade form *ghrs-to- perhaps (but unlikely) in Sanskrit ghattah, ghat: GHAT. See also extensions ghréi- and ghréu-. [Pok. 2. gher- 439.] gher-5. To like, want. 1. Suffixed form *gher-n- in Ger- manic “*gernjan in Old English giernan, gyrnan, to strive, desire, yearn: YEARN. 2. Extended form *ghré- possibly in: a. Germanic *gréduz, hunger, forming *grédagaz, hungry, in Old English grédig, hungry, covetous, greedy: GREEDY; b. Greek khré, it is necessary, whence krésthai, to lack, want, use: CATACHRESIS, CHRESARD, CHRESTOM- ATHY. 3. Suffixed zero-grade form *ghr-td- in Latin hortari, to urge on, encourage (< “to cause to strive or desire”): HORTATIVE; EXHORT. 4. Suffixed zero-grade form “ghr-i- in Greek kharis, grace, favor: CHARISMA; Eucnarist. [Pok. 1. gher- 440.] ghere-. Gut, entrail. 1. Suffixed form *ghero-no- in Ger- manic *garn6, string, in Old English gearn, yarn: YARN. 2. Suffixed form *ghero-n- in Latin hernia, “protruded viscus,” rupture, hernia: HERNIA. 3. Suffixed o-grade form *ghoro-d- in Greek khordé, gut, string: (CHORD?), CORD, (CORDON); HARPSICHORD, TETRACHORD. 4. O-grade form *ghors- in Greek khorion, intestinal membrane, afterbirth: CHORION. 5. Possible suffixed zero-grade form *ghr-u- in Latin haruspex (-spex, “he who sees” < *spek-, “to see”; see spek-), “he who inspects entrails,” diviner (but perhaps borrowed from Etruscan): HARUSPEX. [Pok. 5. gher- 443.] ghers-. To bristle. 1. Extended zero-grade form *ghrzd-, prickly plant, in: a. Germanic *gorst- in Old English gorst, furze, gorse: GORSE; b. Latin hordeum, barley: ORGEAT. 2. Lengthened-grade form *ghér(s)- in Latin hér, ér, hedgehog: URCHIN. 3. Suffixed lengthened-grade form *ghér(s)-ika in Latin ériica, caterpillar: ROCKET?. 4. Suffixed full-grade form *gher-tu-, remade to *hirsu- in Latin hirsitus, bristly, shaggy, hairy: HIRSUTE. 5. Suf- fixed full-grade form *ghers-ko- in Latin hispidus (prob- ably a dialectal borrowing), bristly, shaggy, prickly: HISPID. 6. Suffixed o-grade form “ghors-eyo- in Latin horrére, to bristle, shudder, be terrified, look frightful: HORROR; ABHOR, ORDURE. 7. Suffixed full-grade form *ghers-o- in Greek khersos, dry land: CHERSONESE. [Pok. Bhers- 445.] gheslo-. Seen by some as a base for words meaning “thousand.” 1, Suffixed form *ghesl-yo- in Greek khilioi, thousand: CHILIAD, KILO-. 2. Latin mille, thousand, which has been analyzed as *smi-, “one” + a form *ghsli-, is of obscure origin: MIL!, MIL2, MILE, MILLE- NARY, MILLESIMAL, MILLI-, MILLIEME, MILLION; MIL- FOIL, MILLENNIUM, MILLEPORE, MILLIARY, MILLIPEDE. [Pok. ghéslo- 446.] ghesor-. Hand. Reduced form “ghesr- in Greek kheir, hand: CHIRO-; (CHIRURGEON), ENCHIRIDION, (SURGEON), SURGERY. [Pok. 1. 8hesor- 447.] gheu-. To pour, pour a libation. I. Extended form *gheud-. 1. Zero-grade form *ghud- in Germanic *gut- in Old English guttas, intestines: GuT. 2. Nasalized zero-grade form *ghu-n-d- in Latin fundere, to pour: FOISON, FONDANT, FONDUE, FONT, FOUND2, FUNNEL, FUSE?, FUSILE, FUSION; AFFUSION, CIRCUMFUSE, CON- FOUND, CONFUSE, DIFFUSE, EFFUSE, INFUSE, PERFUSE, PROFUSE, REFUND!, (REFUSE!), (REFUSE?), SUFFUSE,
732:form *m6-ro- in Gaelic mor, big, great: CLAYMORE. [Pok. 4, mé- 704.] mé-4, To cut down grass or grain with a sickle or scythe. Contracted from *mea-. 1. Germanic *mé- in Old English mawan, to mow: Mow?. 2. Suffixed form *mé-ti- in Germanic *médiz in Old English m#th, a mowing, a mown crop: AFTERMATH. 3. Suffixed form *mé-twd-, a mown field, in Germanic *médw6 in Old English méd (oblique case m&@dwe), meadow: MEAD?, MEADOW. [Pok. 2. mé- 703.] med-. To take appropriate measures. 1. a. Germanic *metan in Old English metan, to measure (out): METE!; b. Germanic derivative *m#t6, measure, in Old English gem&te (ge-, with; see kom), “commensurate,” fit: MEET?. 2. a. Latin medéri, to look after, heal, cure: MEDICAL, MEDICATE, (MEDICINE), (MEDICO); METHEG- LIN, REMEDY; b. Latin meditdri, to think about, con- sider, reflect: MEDITATE. 3. Suffixed form *med-es-, replaced in Latin by *modes- by influence of modus (see 4. below), in: a. Latin modestus, “keeping to the appro- priate measure,” moderate: MODEST; IMMODEST; b. Lat- in moderdre, “to keep within measure,” to moderate, control: MODERATE; IMMODERATE. 4. Suffixed o-grade form *mod-o- in Latin modus, measure, size, limit, man- ner, harmony, melody: MODAL, MODE, MODEL, MODERN, MODICUM, MODIFY, MODULATE, MODULE, MODULUS, MOLD!, (MOOD?), (MOULAGE); (ACCOMMODATE), (COM- MODE), COMMODIOUS, (COMMODITY). 5. Suffixed o-grade form *mod-yo- in Latin modius, a measure of grain: MODIOLUS, MUTCHKIN. 6. Possibly lengthened o-grade form *méd- in Germanic *mét-, ability, leisure, in: a. Old English métan, to have occasion, to be permitted or obliged: MOTE2, MUST}; b. Germanic compound é-mot-ja- (prefix *é-, meaning uncertain, from Indo- hinppoes é, 6; see Pok. é, 6 280) in Old English émetta, rest, leisure: EMPTY. [Pok. 1. med- 705.] medhu-. Honey; also mead. 1. Germanic *medu in Old English meodu, mead: MEAD!. 2. Greek methu, wine (> methuein, to be intoxicated): AMETHYST, METHYLENE. [Pok. médhu 707.] medhyo-. Middle. 1. Germanic *midja- in: a. Old English midd(e), middle: M1D!; AMID; b. West Germanic diminu- tive form *middila- in Old English middel, middle: MIDDLE; Cc. Germanic compound *midja-gardaz, “middle zone” (*gardaz, enclosure, yard; see gher-1), name of the earth conceived as an intermediate zone lying between heaven and hell, in Old Norse Midhgardhr, Midgard: MipGarD. 2. Latin medius, middle, half: MEAN, MEDIAL, MEDIAN, MEDIASTINUM, MEDIATE, MEDIUM, MITTEN, MIZZEN, MOIETY, MULLION; INTERMEDIATE, MEDIEVAL, MEDIOCRE, MEDITERRANEAN, MERIDIAN, MILIEU. 3. Greek mesos, middle: MESO-. See also me-2. [Pok. medhi- 706.] meg-. Great. 1. Germanic suffixed form *mik-ila- in: a. Old English micel, mycel, great: MUCH; b. Old Norse mikill, great: MICKLE. 2. Suffixed form *mag-no- in Latin magnus, great: MAGNATE, MAGNITUDE, MAGNUM; MAG- NANIMOUS, MAGNIFIC, (MAGNIFICENT), (MAGNIFICO), (MAGNIFY), MAGNILOQUENT. 3. Suffixed (comparative) form *mag-yos- in: a. Latin major, greater: MAJOR, MAJOR-DOMO, MAJORITY, MAJUSCULE, MAYOR; b. Latin majestds, greatness, authority: MAESTOSO, MAJESTY; c. Latin magister, master, high official (< “he who is greater”): MAESTRO, MAGISTERIAL, MAGISTRAL, MAGIS- TRATE, MASTER, (MISTER), MISTRAL, (MISTRESS). 4. Suf- fixed (superlative) form *mag-samo- in Latin maximus, greatest: MAXIM, MAXIMUM. 5. Suffixed form *mag-to-, “made great,” in Latin mactus, worshiped, blessed, sacred: MATADOR. 6. Suffixed (feminine) form *mag-ya-, “she who is great,” in Latin Maia, name of a goddess: May. 7. Suffixed form *meg-a-l- in Greek megas (stem megal-), great: MEGA-, MEGALO-; ACROMEGALY, ALMA- GEST, OMEGA. 8. Variant form *megh- in Sanskrit maha-,
1235:AMATIVE amma AMATORY amma AMAZON magh-2 AMBAGE ag- AMBASSADOR ag- AMBERGRIS gher-3 AMBI- ambhi AMBIDEXTROUS deks- AMBIENT ei-1 AMBIGUOUS ag- AMBITION ei-1
1356:CHIRO- ghesor- CHIRURGEON ghesor- CHISEL kaa-id- CHITTERLINGS ku- CHLOASMA ghel-2 CHLORITE! ghel-2 CHLORO- ghel-2 CHOANA gheu- CHOANOCYTE gheu- CHOICE geus- CHOIR gher-1
1357:CHOLE- ghel-2 CHOLER ghel-2 CHOLERA ghel-2 CHOLESTEROL ster-1 CHOLINERGIC werg- CHOLLA g(e)u-lo- CHONDRO- ghrendh- CHONDROMALACIA mel-1 CHOOSE geus- CHORAGUS_§ ag-, gher-1 CHORAL gher-1 CHORALE gher-1 CHORD? ghere- -CHORE ghé- CHORIC gher-1 CHORION ghere- CHORISTER gher-! CHOROGRAPHY ghé- CHORUS gher-1 CHOWDER kele-1 CHRESARD gher-5 CHRESTOMATHY gher-5, mendh-1 CHRISM ghréi- Curist ghréi- CHRISTEN ghréi- CHRISTIAN ghréi- CuRIsTMas ghréi- CHROMA ghréu- CHROMATIC ghréu- CHROMATO- ghréu- -CHROME ghréu- CHROMIUM ghréu- CHROMO- ghréu- CHROMONEMA (s)né- CHRONAXY ag- CHRYSANTHEMUM § andh- CHTHONIC dhghem- CHUFA swei-! CHUKAR kau-! CHUKKER kwel-1 CHURCH keue-? CHURL karlaz CHUTE kad-
1381:COGENT ag- COGNATE gene- COGNITION gné- COGNIZANCE gnoé- COGNOMEN no-men- COHABIT ghabh- COHERE ghais- COHORT gher-1 cor! leg-1 coiTus ei-1
1394:CONVOLVE wel-3 CONVULSE wel-4 cook pekw- cOoKY kak-2 cooL gel-3 COOPER ku- COOPERATE op-1 CO-OPT op-2 COORDINATION ar- COPE! kel-1 COPEPOD kap- COPIOUS op-1 COPRO- kekw- COPULA ap-! COPULATE ap-1 COPY op-1 CORACIIFORM ker-2, merph- CORACOID ker-2 CORBEL ker-2 CORBINA ker-2 CORD ghere- CORDATE kerd-1 CORDIAL kerd-1 CORDIFORM kerd-1 CORDON ghere- COREOPSIS sker-! CORGI kwon- CORIACEOUS sker-1 CORIUM §sker-1 cOoRM sker-! CORMORANT ker-2 CORN! gre-no- CORN2 ker-1 CORNEA ker-1 CORNEL ker-6 CORNEOUS ker-1 CORNER ker-1 CORNET ker-1 CORNICULATE ker-1 CORNIFICATION ker-1 CORNU_ ker-1 CORNUCOPIA op-! CORONA sker-3 CORONOID  sker-3 CORPORAL! kWrep- CORPORAL’ kWrep- CORPORATE kWrep- CORPOREAL kWrep- CORPOSANT kWrep-, sak- CORPS kWrep- CORPSE kWrep- CORPULENCE kWrep- CORPUS krep- CORPUSCLE kWrep- CORRADE réd- CORRECT reg-! CORRIDOR kers-2 CORRIE kWer-2 CORROBORATE reudh-! CORRODE réd- CORRUGATE ruk-2 CORRUPT reup- CORSAGE kWrep- CORSAIR kers-2 CORSE kWrep- CORSET kWrep- CORTEGE gher-1 CORTEX sker-1 CORUSCATE sker-2 CORVEE reg-! CORVINE ker-2 Corvus ker-2 CORYDALIS_ ker-1 CORYMB_ ker-1 CORYNEBACTERIUM bak-, ker-1 CORYPHAEUS_ ker-1 COSMONAUT nau-2 COSMOPOLITE pele-3 cosmos kes-3 cost sta-
1397:COUPLE ap-! COURAGE kerd-1 COURANTE kers-2 COURIER kers-2 COURSE kers-2 COURT gher-1 COURTEOUS gher-1 COURTESAN gher-1 COURTESY gher-' COURTIER gher-1 COUSIN swesor- COUTH gnd- COUTURE syi- COUVADE keu-2 COVE! ku- COVEN gWa- COVENANT gWa- COVER wer-5 COVET kwép- COVEY keu-2 cow! gWou- cow2 ku- COWER ku- COWSLIP gWou-, sleubh- coxa koksa
1404:CUPID kwép- CUPIDITY kwép- CUPOLA keu-2 CUPULE keu-2 CUR gere-2 CURATE cura CURATOR cira CURB sker-3 CURD greut- CURE cira CURETTE cira CURIA wWi-ro- CURIO cira CURIOUS cira CURL ger-2 CURRENT kers-2 CURRIER sker-1, CURSIVE kers-2 CURSOR kers-2 CURT sker-1 CURTAL sker-1 CURTILAGE gher-1 cuRTSY gher-* CURULE kers-2 CURVATURE sker-3 CURVE sker-3 CURVET sker-3 CUSHION koksa
1555:GAR? garwian GARAGE wer-5 GARB garwian GARBLE kreij- GARBOIL beu-1 GARDEN gher-1 GARFISH ghaiso- GARGET gere-4 GARLIC ghalso-, leug-1 GARMENT wer-5 GARNER gre-no- GARNISH wer-5 GARRET wer-5 GARRISON wer-5 GARRULOUS | gar- GARTH gher-! Gas ghéu-
1560:GEODE gé GEODESY da- GEOMETRY mé-2 GEOPONIC (s)pen- GEORGIC gé, werg- GERANIUM gera-2 GERENT gerere GERIATRICS gera-1 GERM gene- GERMAN? gena- GERMANDER deru, dhghem- GERMANE gene- GERMINAL gene- GERMINATE gene- GERONTO- gera-1 GERUND gerere GEST gerere GESTALT stel- GESTATION gerere GESTICULATE gerere GESTURE gerere GET ghend- GEYSER gheu- GHAT gher-4 GHOST gheis- GIDDY gheu(e)- Girt ghabh- GILD! ghel-2 GILL! ghel-una GILLS ghai- GILLYFLOWER bhel-3, kar-1 GILT2 ghel-3 GIMMAL yem- GINGERLY gene- GIRASOL sawel- GIRD gher-1 GIRDLE gher-1 GIRTH gher-1 GIST yé-
1565:GOAD ghei-1 GOAT ghaido- GOD gheu(e)- GODSEND sent- GOFFER webh- GOLD ghel-2 GOLIARD gWel-3 GOMPHOSIS gembh- -GON genu-! GONAD gene- GONFALON gWhen-1 GONIOMETER genu-1 GONIOMETRY genu-! GONION genu-! GONO- gena- coop ghedh- GOOSE! ghans- GORE! ghaiso- GORE? ghaiso- GORGE gWere-4 GORGET gWera-4 GORSE ghers- GOSHAWK ghans- GOSLING ghans- GOSPEL spel-3 GOSSIP s(w)e- GOUACHE akWa- GOWAN ghel-2 GRAB! ghrebh-1 GRABEN ghrebh-2 GRACE gWera-3 GRACKLE gera-2 GRADE ghredh- GRAFFITO gerbh- GRAIN gre-no- GRAM! § gerbh- GRAM? gre-no- -GRAM gerbh- GRAMA gras- GRAMINEOUS_ gras- GRAMMAR gerbh- GRAMPUS_peisk- GRANADILLA gfe-no- GRANARY gre-no- GRANDILOQUENCE tolkw- GRANGE gre-no- GRANITE gr@-no- GRANT kerd-1 GRANULE gre-no- GRAPE ger-2 GRAPH gerbh- -GRAPH gerbh- -GRAPHER gerbh- GRAPHIC gerbh- GRAPHITE gerbh- -GRAPHY gerbh- GRAPNEL ger-2 GRAPPA ger-2 GRAPPLE ger-2 GRASP ghrebh-1 GRAss_ ghré- GRATE! grat- GRATE? kert- GRATEFUL gWere-3 GRATIFY gWere-3 GRATIS gWera-3 GRATITUDE gWero-3 GRATUITY gWera-3 GRAUPEL kreup- GRAVE! ghrebh-2 GRAVE? gwWera-2 GRAVES ghrebh-2 GRAVEL ghréu- GRAVID gWera-2 GRAVURE ghrebh-2 GRAY gher-3 GRAYWACKE wegh-
1567:GREAT ghréu- GREAVES ghrebh-2 GREEDY gher-5 GREEN ghré- GREET gher-2 GREGARIOUS ger-1 GRENADE gre-no- GRESSORIAL ghredh- GREYHOUND gher-3 GRID kert- GRIDDLE kert- GRIDIRON kert- GRIEF gWera-2 GRIEVE gWere-2 GRIM ghrem- GRIMACE ghrem- GRIME ghréi- GRIND ghrendh- Grip! ghreib- GRIPE ghreib- GRIPPE ghreib- GRISAILLE gher-3 GRISEOUS gher-3 GRISETTE gher-3 GRISLY ghréi- GRISON gher-3 GRisT ghrendh- GRIT ghréu- GRIZZLE gher-3 GROAT ghréu- GROATS ghréu- GROCER gWres- GROOVE ghrebh-2 GROPE ghreib- GROSCHEN gWres- GROSS gWres- GROSSULARITE ger-2 GROSZ gWres-
1648:HORN ker-1 HORNBEAM ker-1 HORNBLENDE ker-1 HORNET ker-1 HORNITO gWher- HOROLOGE yér- HOROLOGY yér- HOROSCOPE spek-, yér- HORROR ghers- HORST kert- HORTATIVE gher-5 HORTICULTURE gher-1 HOSE (s)keu- HOSPICE ghos-ti- HOSPITAL ghos-ti- HOSPITALITY ghos-ti- HosT! ghos-ti-
1716:KIND! gene- KIND? gene- KINDERGARTEN gene-, gher-1 KINDRED af-, gene- KINE gWou- KINEMATICS kei-3 KINESIOLOGY kei-3 -KINEsIS_ kei-3 KINESTHESIA kei-3 KINETIC kei-3 KING gene-
1995:ORATORY? Or- ORCHARD gher-1 ORCHESTRA ergh- ORCHID ergh- ORDAIN  ar- ORDEAL dail- ORDER ar- ORDINAL ar- ORDINANCE ar- ORDINARY ar- ORDINATE ar- ORDO ar-
```


## [2026-09-05T21:02:53.227Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"ghréi-\\|ghréu-\" AHD_watkins1985.txt | sed -n 1,12p | cut -c1-3000"
}
```


### [2026-09-05T21:02:53.312Z] TOOL RESULT

```
524:gher-’. To shine, glow; gray. Hypothetical base of various Germanic forms. 1. Germanic *gréwaz, gray, in: a. Old English greg, gray: GRAY; b. probably Old English grighund, greyhound: GREYHOUND. 2. Germanic *gris- Jaz, gray, in: a. Old French gris (> French gris), gray: GRISAILLE, (GRISETTE), (GRISON), GRIZZLE; AMBERGRIS; b. Medieval Latin griseus, gray, grayish: GRISEOUS. [Pok. 3. gher- 441.] gher-4. To scrape, scratch. 1. Extended zero-grade form *ghr(e)-k- in: a. Greek kharax, a pointed stake, also a kind of sea bream: CHARACIN; b. Greek kharassein, to sharpen, notch, carve, cut: CHARACTER, GASH. 2. Ex- tended form *ghers-.in suffixed zero-grade form *ghrs-to- perhaps (but unlikely) in Sanskrit ghattah, ghat: GHAT. See also extensions ghréi- and ghréu-. [Pok. 2. gher- 439.] gher-5. To like, want. 1. Suffixed form *gher-n- in Ger- manic “*gernjan in Old English giernan, gyrnan, to strive, desire, yearn: YEARN. 2. Extended form *ghré- possibly in: a. Germanic *gréduz, hunger, forming *grédagaz, hungry, in Old English grédig, hungry, covetous, greedy: GREEDY; b. Greek khré, it is necessary, whence krésthai, to lack, want, use: CATACHRESIS, CHRESARD, CHRESTOM- ATHY. 3. Suffixed zero-grade form *ghr-td- in Latin hortari, to urge on, encourage (< “to cause to strive or desire”): HORTATIVE; EXHORT. 4. Suffixed zero-grade form “ghr-i- in Greek kharis, grace, favor: CHARISMA; Eucnarist. [Pok. 1. gher- 440.] ghere-. Gut, entrail. 1. Suffixed form *ghero-no- in Ger- manic *garn6, string, in Old English gearn, yarn: YARN. 2. Suffixed form *ghero-n- in Latin hernia, “protruded viscus,” rupture, hernia: HERNIA. 3. Suffixed o-grade form *ghoro-d- in Greek khordé, gut, string: (CHORD?), CORD, (CORDON); HARPSICHORD, TETRACHORD. 4. O-grade form *ghors- in Greek khorion, intestinal membrane, afterbirth: CHORION. 5. Possible suffixed zero-grade form *ghr-u- in Latin haruspex (-spex, “he who sees” < *spek-, “to see”; see spek-), “he who inspects entrails,” diviner (but perhaps borrowed from Etruscan): HARUSPEX. [Pok. 5. gher- 443.] ghers-. To bristle. 1. Extended zero-grade form *ghrzd-, prickly plant, in: a. Germanic *gorst- in Old English gorst, furze, gorse: GORSE; b. Latin hordeum, barley: ORGEAT. 2. Lengthened-grade form *ghér(s)- in Latin hér, ér, hedgehog: URCHIN. 3. Suffixed lengthened-grade form *ghér(s)-ika in Latin ériica, caterpillar: ROCKET?. 4. Suffixed full-grade form *gher-tu-, remade to *hirsu- in Latin hirsitus, bristly, shaggy, hairy: HIRSUTE. 5. Suf- fixed full-grade form *ghers-ko- in Latin hispidus (prob- ably a dialectal borrowing), bristly, shaggy, prickly: HISPID. 6. Suffixed o-grade form “ghors-eyo- in Latin horrére, to bristle, shudder, be terrified, look frightful: HORROR; ABHOR, ORDURE. 7. Suffixed full-grade form *ghers-o- in Greek khersos, dry land: CHERSONESE. [Pok. Bhers- 445.] gheslo-. Seen by some as a base for words meaning “thousand.” 1, Suffixed form *ghesl-yo- in Greek khil
526:TRANSFUSE. II. Extended form *gheus-. 1. Germanic zero-grade form *gus- in: a. suffixed form *gustiz in Old Norse gustr, a cold blast of wind: cusT!; b. Icelandic gusa, to gush, perhaps akin to Middle English gushen, to gush: GUSH. 2. Germanic suffixed o-grade form *gausjan in Old Norse geysa, to gush: GEYSER. III. Suffixed form *gheu-ti- in Latin fatilis, “(of a vessel) easily emptied, leaky,” hence untrustworthy, useless: FUTILE. IV. Basic form *gheu- in Greek khein, to pour: CHOANA, CHYLE, (CHYME); CHOANOCYTE, ECCHYMOSIS, PARENCHYMA. [Pok. gheu- 447.] ghéu-. To yawn, gape. Compare ghai-. 1. Germanic suffixed form g6-ma- in Old English goma, palate, jaw: GuM?, 2. Variant form *ghau- in Greek khaos, chasm, empty space, chaos: CHAOS, GAS. [Pok. ghéu- 449.] gheu(e)-. To call, invoke. Suffixed zero-grade form *ghu-to-, “the invoked,” god, in Germanic *gudam, god, in: a. Old English god, god: Gop; b. Germanic *gud-igaz, possessed by a god, in Old English gydig, gidig, possessed, insane: GIDDY. [Pok. ghau- 413.] gh6. Behind, after. Slavic *za in Russian za, by, to: SASTRUGA. [Pok. 26 451.] ghos-ti-. Stranger, guest, host; properly “someone with whom one has reciprocal duties of hospitality.” 1. Basic form *ghos-ti- in: a. Germanic *gastiz in Old Norse gestr, guest: GUEST; b. Latin hostis, enemy (< stranger): HOST?, (HOSTILE). 2. Compound “ghos-pot-, *ghos-po(d)-, “guest-master,” one who symbolizes the relationship of reciprocal obligation (*pot-, master; see poti-), in Latin hospes (stem hospit-), host, guest, stranger: (HOSPICE), (HOSPITAL), (HOSPITALITY), HOST!, (HOSTAGE), (HOSTEL), (HOSTLER). See also xenos. [Pok. ghosti-s 453.] ghow-é-. To honor, revere, worship. 1. Germanic *gaw6n in Old Norse gd, to heed: GAWK. 2. Basic form *ghow-é- in Latin favére, to favor, be favorable: FAVOR, (FAVOR- ITE). [Pok. ghou(é)- 453.] ghré-. To grow, become green. Contracted from “ghreo-. 1. O-grade form “ghré- in Germanic *grd(w)an in Old English gréwan, to grow: GROW. 2. Suffixed o-grade form *ghro-nyo- in Germanic *grénjaz, green, in Old English gréne, green: GREEN. 3. Suffixed zero-grade form *“ghro-so- in Germanic *grasam, grass, in Old English grees, grass: GRASS. [Pok. ghré- 454.] ghrebh-'. To seize, reach. 1. Zero-grade form *ghrbh- in Sanskrit grbhndati, grhndati, he seizes: SATYAGRAHA. 2. Parallel (imitative) Germanic creations with base *grab-, *grap- in: a. Middle English graspen, to grasp: GRASP; b. Middle Dutch and Middle Low German grab- ben, to seize: GRAB. [Pok. 1. ghrebh- 455.] ghrebh-?. To dig, bury, scratch. 1. O-grade form “ghrobh- in: a. Germanic *graban in (i) Old English grafan, to dig, engrave, scratch, carve: GRAVE3; (EN- GRAVE) (ii) Old High German graban, to dig: GRABEN (iii) Old French graver, to engrave: GRAVURE; b. Germanic *grabam in Old English grzf, trench, grave: GRAVE}. 2. Germanic *grub(byan (with secondary ablaut) in Old English *grybban (> Middle English grubben), to dig: GRUB. 3. Ger
528:in Greek khriein, to anoint: CHRISM, CHRIST, CHRISTEN, (CHRISTIAN); (CHRISTMAS). [Pok. ghréi- 457.] ghreib-. To grip. 1. Germanic *grip- in Old English gripe, grasp, and gripa, handful: crip!. 2. Germanic *gripan in: a. Old English gripan, to grasp: GRIPE; b. Old French gripper, to seize: GRIPPE. 3. Suffixed o-grade form *ghroib-eyo- in Germanic *graipjan in Old English grd- pian, to feel for, grope: GROPE. [Pok. ghreib- 457.] ghrem-. Angry. 1. Germanic *grimmaz in: a. Old English grim(m), fierce, severe: GRIM; b. Old French grimace, a grimace: GRIMACE. 2. Germanic *grum- in Middle Dutch grommen, to mutter angrily, probably akin to Middle English grummen, to grumble: GRUMBLE. 3. Suffixed o-grade form *ghrom-o- in Russian grom, thunder: Po- crom. [Pok. 2. ghrem- 458.] ghrendh-. To grind. 1. Germanic “grindan in Old Eng- lish grindan, to grind: GRIND. 2. Germanic *grinst-, a grinding, in Old English grist, the action of grinding: GRisT. 3. Latin frénum (< frendere, to grind), horse’s bit (on which its teeth grind), bridle: FRENULUM, FRENUM; REFRAIN). 4, Variant form *ghrend- is sometimes but improbably regarded as the root of Greek khondros, granule, groats, hence cartilage: CHONDRO-; HYPOCHON- DRIA, MITOCHONDRION. [Pok. ghren- 459.] ghréu-. To rub, grind. Extension of gher-4. 1. Germanic *greut- in Old English gréot, sand, gravel: GRIT. 2. Ger- manic *grut- in Old English grotan, pieces of hulled grain, groats: GROATS. 3. Germanic “grit- in: a. Old English griit, coarse meal: GRouT; b. Old French gruel, porridge: GRUEL. 4, Germanic *grautaz, coarse, thick (< “coarsely ground”), in: a. Old English gréat, coarse, thick, bulky, large: GREAT; b. Middle Dutch groot, thick: Groat. 5. Germanic *griiw-, to recoil from (< “to be offended, be grated on by”), in Middle Dutch griiwen, to abhor, akin to Middle English grue, horrible: GRUESOME. 6. Variant form *ghrow- in Greek khrés, skin (< “rough surface” ?), hence flesh, complexion, color: RHODOCHRO- SITE. 7. Suffixed variant form *ghré-mn in Greek khréma, skin, complexion, color (semantic development as in 6. above): CHROMA, CHROMATIC, CHROMATO-, CHROME, -CHROME, (CHROMIUM), CHROMO-; ACHRO- Matic. 8. Probably Celtic *graw- in Old French grave, greve, coarse sand, gravel: GRAVEL. 9. Probably Latin *grau-, to touch, graze, in con-gruere, to agree (com-, together; see kom): CONGRUENT. [Pok. 2. ghréu- 460.] ghwer-. Wild beast. 1. Suffixed form *ghwer-o- in Latin ferus, wild: FERAL, FIERCE. 2. Compound *ghwero-okv-, “of wild aspect” (*-ak-, “-looking”; see okw-), in Latin feréx (stem feréc-), fierce: FEROCIOUS. 3. Length- ened-grade form *ghwér- in Greek thér, wild beast: TREACLE; THEROPOD. [Pok. ghuér- 493.] gladh-. Smooth. Suffixed form “gladh-ro- in Latin gla- ber, smooth, bald: GABRO, (GLABELLA), GLABROUS. gleubh-. To cut, cleave. 1. Germanic *k/euban in Old English cléofan, to split, cleave: CLEAVE!. 2. Germanic *klub-, a splitting, in: a. Old English clufu, c
1209:ACHE ag-es- ACHENE ghai- ACHERON eghero- ACHOLIA ghel-2 ACHROMATIC ghréu- ACICULA ak- ACID ak-
1357:CHOLE- ghel-2 CHOLER ghel-2 CHOLERA ghel-2 CHOLESTEROL ster-1 CHOLINERGIC werg- CHOLLA g(e)u-lo- CHONDRO- ghrendh- CHONDROMALACIA mel-1 CHOOSE geus- CHORAGUS_§ ag-, gher-1 CHORAL gher-1 CHORALE gher-1 CHORD? ghere- -CHORE ghé- CHORIC gher-1 CHORION ghere- CHORISTER gher-! CHOROGRAPHY ghé- CHORUS gher-1 CHOWDER kele-1 CHRESARD gher-5 CHRESTOMATHY gher-5, mendh-1 CHRISM ghréi- Curist ghréi- CHRISTEN ghréi- CHRISTIAN ghréi- CuRIsTMas ghréi- CHROMA ghréu- CHROMATIC ghréu- CHROMATO- ghréu- -CHROME ghréu- CHROMIUM ghréu- CHROMO- ghréu- CHROMONEMA (s)né- CHRONAXY ag- CHRYSANTHEMUM § andh- CHTHONIC dhghem- CHUFA swei-! CHUKAR kau-! CHUKKER kwel-1 CHURCH keue-? CHURL karlaz CHUTE kad-
1392:CONFOUND gheu- CONFRERE bhrater- CONFUSE gheu- CONFUTE bhau- CONGE mei-1 CONGEAL gel-3 CONGENER gene- CONGENIAL gene- CONGENITAL gene- CONGERIES gerere CONGEST gerere CONGLOBATE gel-1 CONGLOMERATE gel-1 CONGLUTINATE gel-1 CONGRATULATE gWera-3 CONGREGATE ger-! CONGRESS ghredh- CONGRUENT ghréu- CONIDIUM keni- CONIOSIS keni- CONJECTURE yé- CONJOIN yeug- CONJUGAL yeug- CONJUGATE yeug- CONJUNCT yeug- CONJURE yewes- CONNATE gene- CONNECT ned- CONNIVE kneig’h- CONNOISSEUR gn6- CONNOTE gné- CONNUBIAL sneubh- CONQUER quaerere CONQUIAN kom, kWo- CONSCIENCE skei- CONSCIOUS | skei- CONSCRIPT skribh- CONSECRATE sak- CONSENT sent- CONSEQUENT sekw-1 CONSERVE ser-1 CONSIDER sweid-1 CONSIGN sekw-1 CONSIST sta- CONSOCIATE sekw-1 CONSOLE! sel-2 CONSOLIDATE sol- CONSOLUTE leu-1 CONSONANT swen- CONSORT ser-3 CONSPICUOUS _ spek- CONSPIRE spirare CONSTABLE ei-1 CONSTANT sta- CONSTELLATION  ster-3 CONSTERNATE  ster-2 CONSTIPATE  steip- CONSTITUTE sta- CONSTRAIN | streig- CONSTRUCT  ster-2 CONSUETUDE s(w)e- CONSUME em- CONTACT tag- CONTAIN ten- CONTAMINATE tag- CONTEMPLATE tem- CONTEND ten- CONTEST trei- CONTEXT teks- CONTINUE ten- CONTORT terkw- CONTOUR tera-1 CONTRA- kom CONTRABAND bha-2 CONTRACT tragh- CONTRADICT deik- CONTRARY kom CONTRAST sta- CONTRAVENE gWa- CONTRITE tere-1 CONTRIVE trep-2 CONTROL ret- CONTROVERSY wer-3 CONTUSE (s)teu- CONVALESCE wal- CONVECTION wegh- CONVENE gWa- CONVENIENT gWa- CONVENT gWa- CONVENTICLE gWa- CONVENTION gWa- CONVERGE wer-3 CONVERSE! wer-3 CONVERT wer-3 CONVEX wegh- CONVEY wegh- CONVINCE weik-5 CONVIVIAL gWei- CONVOKE wekw-
1565:GOAD ghei-1 GOAT ghaido- GOD gheu(e)- GODSEND sent- GOFFER webh- GOLD ghel-2 GOLIARD gWel-3 GOMPHOSIS gembh- -GON genu-! GONAD gene- GONFALON gWhen-1 GONIOMETER genu-1 GONIOMETRY genu-! GONION genu-! GONO- gena- coop ghedh- GOOSE! ghans- GORE! ghaiso- GORE? ghaiso- GORGE gWere-4 GORGET gWera-4 GORSE ghers- GOSHAWK ghans- GOSLING ghans- GOSPEL spel-3 GOSSIP s(w)e- GOUACHE akWa- GOWAN ghel-2 GRAB! ghrebh-1 GRABEN ghrebh-2 GRACE gWera-3 GRACKLE gera-2 GRADE ghredh- GRAFFITO gerbh- GRAIN gre-no- GRAM! § gerbh- GRAM? gre-no- -GRAM gerbh- GRAMA gras- GRAMINEOUS_ gras- GRAMMAR gerbh- GRAMPUS_peisk- GRANADILLA gfe-no- GRANARY gre-no- GRANDILOQUENCE tolkw- GRANGE gre-no- GRANITE gr@-no- GRANT kerd-1 GRANULE gre-no- GRAPE ger-2 GRAPH gerbh- -GRAPH gerbh- -GRAPHER gerbh- GRAPHIC gerbh- GRAPHITE gerbh- -GRAPHY gerbh- GRAPNEL ger-2 GRAPPA ger-2 GRAPPLE ger-2 GRASP ghrebh-1 GRAss_ ghré- GRATE! grat- GRATE? kert- GRATEFUL gWere-3 GRATIFY gWere-3 GRATIS gWera-3 GRATITUDE gWero-3 GRATUITY gWera-3 GRAUPEL kreup- GRAVE! ghrebh-2 GRAVE? gwWera-2 GRAVES ghrebh-2 GRAVEL ghréu- GRAVID gWera-2 GRAVURE ghrebh-2 GRAY gher-3 GRAYWACKE wegh-
1567:GREAT ghréu- GREAVES ghrebh-2 GREEDY gher-5 GREEN ghré- GREET gher-2 GREGARIOUS ger-1 GRENADE gre-no- GRESSORIAL ghredh- GREYHOUND gher-3 GRID kert- GRIDDLE kert- GRIDIRON kert- GRIEF gWera-2 GRIEVE gWere-2 GRIM ghrem- GRIMACE ghrem- GRIME ghréi- GRIND ghrendh- Grip! ghreib- GRIPE ghreib- GRIPPE ghreib- GRISAILLE gher-3 GRISEOUS gher-3 GRISETTE gher-3 GRISLY ghréi- GRISON gher-3 GRisT ghrendh- GRIT ghréu- GRIZZLE gher-3 GROAT ghréu- GROATS ghréu- GROCER gWres- GROOVE ghrebh-2 GROPE ghreib- GROSCHEN gWres- GROSS gWres- GROSSULARITE ger-2 GROSZ gWres-
1569:GROUP ger-? GROUT ghréu- GROW ghré-
1570:GRUB ghrebh-2 GRUDGE gru- GRUEL ghréu- GRUESOME ghréu- GRUFF kreup- GRUMBLE ghrem- GRUNION gru- GRUNT gru-
2181:RETE era-2 RETIARY era-2 RETICENT tak-1 RETICLE era-2 RETICULE ere-2 RETIFORM ere-2 RETINA era-2 RETINACULUM  ten- RETORT! terkw- RETRACT tragh- RETRAL re- RETRIEVE trep-2 RETRO- re- RETROACTIVE ag- RETROCEDE ked- RETROGRADE ghredh- RETROGRESS ghredh- RETRORSE wer-3 RETROSPECT spek- RETURN tera-1 RETUSE (s)teu- REVEAL weg-1 REVEILLE weg-2 REVEL duellum REVENANT gWa- REVENGE deik- REVENUE gWa- REVERBERATE wer-3 REVERE! wer-4 REVERT wer-3 REVEST wes-4 REVIEW weid- REVIVE gWei- REVOKE wekw- REVOLVE wel-3 REVULSION wel-4 REWARD wer-4 RHABDOMANCY wer-3 RHABDOVIRUS wer-3 RHAPSODY wed-2, wer-3 RHEO- sreu- RHETOR wer-6 RHEUM sreu- RHINOCEROS ker-1 RHIZO- wrad- RHIZOBIUM gWei- RHIZOME wrad- RHODIUM wrod- RHODO- wrod- RHODOCHROSITE ghréu- RHODODENDRON deru RHODOPSIN OkW- RHOMBUS_ wer-3 RHONCHUS  srenk- RHYME sreu- RHYNCHOCEPHALIAN srenk- RHYOLITE sreu- RHYTHM = sreu-
```


## [2026-09-05T21:03:03.920Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nimport json\nd=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'))\nprint(json.dumps(d['POK'],ensure_ascii=False,indent=1))\nprint(json.dumps(d['AHD'],ensure_ascii=False,indent=1))\nprint(json.dumps(d['KLN'],ensure_ascii=False,indent=1))\nprint(json.dumps(d['OEW'],ensure_ascii=False,indent=1))\n\""
}
```


### [2026-09-05T21:03:05.988Z] TOOL RESULT

```
{
 "title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)",
 "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/indogermanisches01pokouoft",
 "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt",
 "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-dictionary/ (entry pages with page numbers) and StarLing https://starlingdb.org/cgi-bin/query.cgi?basename=\\data\\ie\\pokorny&root=config",
 "notes": "Nourai's page numbers are Band I 1959 pages, which match these scans. Band II (1969 index) is at pokorny-indogermanisches-etymologisches-worterbuch-band-ii-1969 (djvu 200). local_files: /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt (pp. 1-348), /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_02.txt (pp. 349-770), /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_03.txt (pp. 771-1183); /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_full.txt (unpaginated database text with 'Page(s): N' per root)",
 "local_files": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_02.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_03.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_full.txt"
 ],
 "cites": "page number of Pokorny, Indogermanisches etymologisches Wörterbuch, Band I (1959)"
}
{
 "title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)",
 "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)",
 "kind": "archive_djvu+website+archive_restricted",
 "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only",
 "identifier": "watkins-american-heritage-dictionary-of-indo-european-roots-1985",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt",
 "page_offset": "1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page.",
 "lookup_hint": "Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru-' ; entries list English derivatives in caps. Restricted 1970s AHD scans on IA (lending only, djvu.txt returns 401): americanheritage0000dict (July 1977 printing, 970 leaves - probably the New College Edition), bwb_P9-BHZ-437 (1974), americanheritage00nyde (1970), bwb_W9-CSW-086 (1969, 1610 leaves = original 1969 ed.).",
 "notes": "AHD is by far the most cited source (1906). Root order is alphabetical in all versions, so root-name lookup is reliable; page numbers can only be checked against a borrowed copy of the 1976 New College Edition. || RE-SEARCH 2026-09: no open scan of the New College Edition; three borrowable copies on archive.org (avoid the ~840-pp Dell abridgements, which lack the appendix). Local proxy remains AHD_watkins1985.txt.",
 "cites": "page number of the 1975/76 New College Edition; pp. 1505–1550 are the Indo-European roots appendix (look the root up by name)"
}
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
{
 "title": "J. T. Shipley, The Origins of English Words: A Discursive Dictionary of Indo-European Roots, Baltimore 1984",
 "edition_found": "1984 (lending-only)",
 "kind": "archive_restricted",
 "url": "https://archive.org/details/originsofenglish0000ship ; https://archive.org/details/originsofenglish00jose (both JHU 1984, borrowable) ; HathiTrust mdp.49015002910322 search-only ; Google ELSm5zUgP_wC no view",
 "identifier": "originsofenglish00jose (also originsofenglish0000ship)",
 "local_file": null,
 "page_offset": null,
 "lookup_hint": "Borrow via IA lending (djvu.txt returns 401/403). Entries are IE roots in alphabetical order; use IA's in-book search: https://archive.org/details/originsofenglish00jose?q=<root>",
 "notes": "RE-SEARCH 2026-09: borrowable only (Internet Archive lending, 1 hr / 14 days with a free account)."
}
```


## [2026-09-05T21:03:11.185Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for L in 95 96 113 116 117; do echo \"===== leaf $L (0-based) =====\"; awk 'BEGIN{RS=\"\\f\"} NR=='\"$((L+1))\"'' POK_02.txt | head -20; done"
}
```


## [2026-09-05T21:03:12.371Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"lemma: g^her-\\|lemma: gher\\|lemma: ghrēi\\|lemma: ghrēu\\|lemma: ĝher\" POK_full.txt | head -30"
}
```


### [2026-09-05T21:03:12.870Z] TOOL RESULT

```
===== leaf 95 (0-based) =====
terndes  Geschwür'. WP.  I  588.
ghengh'  ^schreiten;  Schritt,  Schenkelspreize,  Schamgegend'.
Ai.jdmhas-  n.  ,Schritt,  Flügelschlag',  jaw^Ää  ,Unterschenkel',  av.  zangdvf^ , Knöchel  des  Fußes',  -zangra-  (in  Kompositis)  ds.,  schwundstufig  SA.jagJidna; m.  n.  ,Hinterbacke,  Schamgegend'  :  gr.  -/.oxco^rj  ,Stelle  zwischen  denil Schenkeln'  (assim.  aus  *-/.ax(hvQ) ;
ags.  -gllit  ,Gang',  mhd.  gtht  ,Gang,  Reise'  (urgerm.  *ginxti-  aus  gheng-ti-), mit  Abtönung  o:  got.  gagg  n.,  aisl.  gangr,  ags.  ahd.  gang  ,Gang'  und  germ. *gangjan  Iter.  (got.  Prät.  gaggida  ,ging',  ags.  gengan,  mhd.  gengen,  gande ,losgehen')  und  danach  auch  ^gangan^  got.  gaggan  ,gehen'  =  aisl.  ganga (gekk),  as.  gangan  {geng),  ahd.  gangan  {giang),  ags.  gongan  ds.,  wozu  ahcl. gengi,  ags.  genge,  aisl.  gengr  ,gangbar',  got.  framgähts  ,Fortschritt',  aisl. gätt  , Einschnitt  am  Türpfosten',  gcetti  ,Türrahmen';  schwundstufig  afries. gunga  ,gehen',  dän.  gynge,  älter  gunge  ,schaukeln';
lit.  zengiü,  zeTigti  ,schreiten',  prazangä   ,Übertretung',   zifigsnis   ,Schritt'.
I
439
Eine  Anlautdublette  (durch  Dissimilation?)  vielleicht  in  air.  cingim schreite^  (3.  PL  cengait,  Perf.  cecliaing),  cjmr.  rhy-gyngu  ^Paßgehen^,  air. cing,  Gen.  cinged  ^Krieger^^  gall.  Cingeto-rix,  schwundstufig  urkelt.  *kngsmn in  air.  ceimm  (*Jcenksmen),  cymr.  com.  cam^  bret.  camm  ^Schritt^  (^kanksman).
Eine  andere  Variante  "^ghenk-  ist  (unter  ökii-s  ;,schnelP)  für  ahd.  gähi rasch^  hastig,  plötzlich^  in  Erwägung  gezogen.
WP.  I  588,  WH.  I  217,  Trautmann  370.
j,  gher-  in  Schallworten,  meist  nur  jüngere  parallele  Wortschöpfungen,  häufig mit  expressivem  Vokalwechsel  und  Gemination.
Ai.  gharghara-h  , rasselnd,  gurgelnd',  m.  , Gerassel,  Gelächter',  ghargharita- n.  , Gegrunze',  gliurghura-h  ,ein  gurgelnder  Laut',  ghurghurl  , Grille', ghurghuräyate  , saust,  surrt';
lat.  hirrlre  , winseln,  knurren'  (,7'r'  mit  i  vokalisiert  als  Wiedergabe  des hohen  Tons);
ags.  gierran  st.  V.  , tönen,  knarren,  schwatzen',  nhd.  gU-ren  (mhd.  auch garren,  gurren),  schwed.  norw.  garpa  ,lärmen,  prahlen',  aisl.  garpr  , uner- schrockener streitbarer  Mensch';  norw.  dial.  garta  , spaßen,  plaudern, grunzen';  ags.  gierman,  norw.  garma  , brüllen',  anord.  garmr  .Hund'; weiters  ags.  gryllan  ,knirschen,  wüten',  mhd.  grellen  st.  V.  , durchdringend, vor  Zorn  schreien',  grel  ,rauh,  gr
===== leaf 96 (0-based) =====
ell,  zornig',  ndl.  grollen  , murren,  zornig sein',  mhd.  grüllen  ,höhnen',  nhd.  grollen-^
russ.-ksl.  gzrkati  ,girren',  öech.  hr^eti  , rasseln,  schnurren,  rieseln',  hrkati .krachen,  schnarren' ;  slov.  grgati  , gurgeln,  girren' ;
hierher  vielleicht  ghre-d-  in  got.  gretan,  anord.  grata,  asächs.  grätan, a,gs.  gräetan  (greotan  na^ch.  reotan  ds.)j  nhd.  alem.  gratsd  , weinen,  jammern'; ablaut.  Kausat.  aisl.  grßta  ,zum  Weinen  bringen',  ags.  gra>tan  , angreifen, grüßen',  asächs.  grötian  , anrufen',  ahd.  griiozen,  nhd.  grüßen-,  anord.  grätr m.  ,Weinen',  ahd.  gräz  ,Wut' ;
ghi-e-dh-  in  ags.  grledan  , rufen,  schreien'.
WP.  I  605.
2.  gher-  ,hart    worüber    streichen,    reiben';    vgl.    auch    die   Erweiterungen ghrei-,  ghreu-,  ghrem-,  ghren-,  sowie  oben  gröd-, Gr.  -/.eyxQog  , Hirse,  Korn',  Y.axQvq  , geröstete  Gerste'  (diss.  aus  *gher-ghro- und  *ghn-ghru-);   xegadog  n.  und   x^Q^Q'>  -d^og   f.    , Geröll,   Kies'    {*gherdd- oder  *ghernd-  ?) ;    x^Quaq^  -adog  f.  , Kiesel,  Schleuderstein' ;
\a,t.  furfur,  -uris  m.  ,der  Balg,  die  Hülse  des  Getreides  und  der  Hülsen- früchte; die  Kleie'  {*for-for)]  Vokalstufe  wie  in  lit.  guriis  , bröckelig', gfirti  , zerbröckeln'.
440  9
s-Er  Weiterung:
ai.  gharsati  ,reil)t\  ghr?ta-h  ,geriebeii' ;  russ.  goröchz  ,Erbse',  skr.  gräh ,Bohne,  Erbse'  (die  sl.  Intonation  entw.  aus  einer  dehnst.  Grundf.  *ghörso-i oder  aus  *ghordsos).
WP.  I  605  f.,  WH.  I  545  f.,  570.
5.  gher-f  ghre-  :  ghrö-  :  ghro-  »hervorstechen',  von  Pflanzentrieben  oder -stacheln,  Borsten,  von  Erderhebungen,  Kanten  usw.  (wahrscheinlich identisch  mit  ghre-  :  ghrö-  :  ghrd-  ,wachsen,  grünen',  s.  dort) ;  s.  auch unter  ghers-.
a.  Gr.  xa^/a*  ßovvög  Hes.,  x^Q^r]  ,obere  Lanzenspitze',  Hy-xagfiov ävidcpsQfj  T'^v  alxfi^v  Hes.,  xo^Q^^S  ,emporstehend,  hervorragend;  hervorragende Klippe  im  Meer'  (*ghorio-);
allenfalls  (doch  ganz  unsicher)  hierher  norw.  dial.  gare  , Spitze',  gara , stechen,  stoßen';
von  der  schweren  Basis:  mhd.  grät,  PI.  grcete  m.  , Fischgräte,  Ähren- spitze,  Bergspitze,  Berggrat',  nhd.  Grat,  Gräte  (*ghre-ti-)',
mit  Red. -Stufe:  poln.  grot,  cech.  hrot  ,Pf eilspitze,  Wurfspieß';
b.  mit  -d-Suffix:  ahd.  mhd.  graz  n.  , Schößling,  Zweig  von  Nadelhölzern' (auch  wohl  aufs  Seelische  gewendet  ahd.  gj^azzo  Adv.  ,heftig,  streng',  mhd. graz,  gräz  ,Wut',  graz  , wütend,  zornig');
c.  mit  rz-Suffix:
Got.  *granö  (Isidor  Orig.  XIX  23,  7),  ahd.  grana,  ags.  granu,  aisl.  grgn f.    »Schnurrbart;    Mund,    Fichte',   mhd.   gran,   grane    , Spitze    des    Haares,'    _ Barthaar,    Gräte',    nhd.    Granne    , Ährenstachel',    dial.    , Rückenborste    des   ^ Schweins
===== leaf 113 (0-based) =====
sl.  jpogrebq,  pogreti  ,begraben',  skr.  grebem,  grebsti  , krallen,  kratzen' mit  po-  ,begraben',  cech.  (alt)  hrebu,  hrebsti  ,graben,  begraben',  poln. grzeb^,  grzesc  , kratzen,  graben,  begraben' ;  schwundstufig  slav.  *grbbeti  in aöech.  hfbieti  , begraben  liegen^  heute  pohfbiti  ,begraben' ;  Iterativ  aksl. pogräbati,  gribati  , begraben',  russ.  pogrebäh  ds.,  skr.  (alt)  zagribati  ,ver- scharren',  cech.  hrebati  , Vorwürfe  machen,  tadeln',  poln.  grzebie,  grzebad ,scharren,  striegeln,  kratzen*,  mit  po-  , begraben' ;  ksl.  grebent  ,Kamm*, russ.  grebem  ds.,  skr.  greben  , Stachel,  Krämpel,  Bergrücken',  cech.  hrehen ,Kamm,  Hechel',  poln.  grzebien  ds.;  aksl.  grob^  ,Grab',  skr.  grob  (Gen. gröba),  cech.  hrob,  russ.  grob  (Gen.  gröba).
WP.  I  653  f.,  Trautmann  96.
gbredb-  ,schreiten*.  'j
Av.  aiwi-gdrddmahi  ,wir  beginnen,  ingredimur',  gdrdzdi-  f.  ,das  (*Antreten=) Inbesitznehmen,  Bekommen';  aber  mind.  (Asoka-Inschr.)  adhigicya  ,be- ginnend'  ==  ai.  adhi-krtya-,  S.  Levi  GA  1912 ;
lat.  gradior,  -l  ,schreiten',  gradus,  -üs  , Schritt,  Stufe',  grallae  ,Stelzen* (lat.  grad'  aus  *ghrßh-,  Ablautstufe  wie  in  lit.  gridiju)]
got.  grips  (nur  Akk.  Sg.  grid)  ,Schritt,  Stufe'  (aber  mhd.  grit  »Schritt', griten  ,die  Beine  auseinanderspreizen',  nhd.  bair.  gritt,  gritten  ds.  und  — allerdings  eindeutig  der  z-Reihe  angehörigem  —  graiteln  ,die  Finger  oder Beine  auseinandersperren'  u.  dgl.  gehören  zu  germ.  *gr^-  ,gespreizt,  aus- einanderklaffend', das  auswärtiger  Anknüpfung  bisher  entbehrt);
lit.  grldiju,  -yti  (Juäkevicz)  ,gehen,  wandern,  umherirren'.
Nasalpräsentia:
457
air.  in-grenn-,  to-grenn-  , verfolgen*  (-enn-  aus  -ndh-n-,  themat.  n-Präs., 3.  Sg.  *ghrn-dh-ne-t),  vgl.  Thurneysen  KZ.  63,  114  f.,  Kuiper  Nasalpräs. 170  f.;
aksl.  gr^dq,  gresti  , kommen',  russ.  grjadü,  grjasti  ,gelien,  schreiten*  usw.
WP.  I  651  f.,  WH.  I  615  f.,  Trautmann  98.
ghrei-  :  ghroi-  :  ghri-  und    (lit.)   ghrei-   ,  dar  überstreichen,    hart    darüber- streifen,  bestreichen  (auch  z.  T.  beschmieren,  Schmutzstreifen)',   Er- weiterung  von  gher-  , reiben' ;   viel  weniger  fruchtbar  als   die   w-Er- weiterung  ghreu-. Gr.  x^fw  ,salbe,  streiche  an,  färbe,  kratze,  steche*  (*x^ro'-;iw  oder  x^ww, vgl.   ^xqtGd-iqVj   xQ^axog),   XQi(JLg    ,das  Salben,  Bestreichen,   Färben',    /^t^a, jünger  XQtai.La  , Salbe;    Anstrich',  ^yxqiio  , steche  ein;    salbe,  beschmiere'; XQij^Ttrw  ,streife  über  die  Oberfläche,  ritze^  usw. ;    Med.  , streife   hart   an etwas,  nähere  mich' ;
aisl.  grima  ,Maske,  Helm;  Rätsel',  engl,  grime  ,Ruß,  Schmutz',  ags.  as. grlma,  -o m. , Maske,  Helm;  Gespenst',  mnd.  grlmet  , schwarzge
===== leaf 116 (0-based) =====
ünt  , Grund,  Boden'.
ghren-d- :
Gr.  xövÖQog  m.  , Graupe,  Korn'  (diss.  aus  "^XQOvd-Qog)'^ alb.  {-d-  oder  -dli-)  gründe,  krunde  , Kleie'  (*ghrn-d\}i\a)] lat.  frendö,  -ere  , zermalmen,  die  Zähne  knirschen'; aisl.  grotti  m.  ,Mühle'.
ghren-dh- :
Ags.  grindan  , zerreiben,  zermalmen',  engl,  to  grind  ,ds.,  schärfen'  (ags. grindan  mit  töpum),  engl,  to  grind  ones  teeth  ,die  Zähne  knirschen';  nhd. (ndd.)  Grand  ,Sand',  ndd.  grand  f.  , grober  Sand,  grobes  Mehl,  Kleie', ahd.  in  grente  ,in  argillosa  terra',  risI.  grandi  m.  , Sandbank,  Kies';  ndd. grind  f.  , Kieselsand;  , Schorf,  nid.  grind,  grint  , grobes  Mehl,  grober  Sand'. 'ahd.  mhd.  grint  , Grind,  Schorf,  got.  grinda-frapjis  ,kleinmütig'  (von  einem adj.  *grinds  ,*zerrieben') ;
lit.  grendu,  gresti  und  grendziu,  gresti  , tüchtig  reiben,  scheuern'  (dehnst. Präs.),  Iter.  grdnd-au,  -yti  (vgl.  gremzti  oben  unter  1.  glirem-)]  russ.  grjada.
WP.  I  656  f.,  WH.  I  545  f.,  Trautmann  96  f.
ghrendh-  ,Balken'.
Lat.  grunda  f.  ,GTeyri\  suggrunda  f.  , Dachstuhl'  aus  '^ghrondhäy aisl.  g7'ind   f.    , Gitterwerk,    Gittertür,    Hafen',   ags.   grindel,   as.   grindil , Riegel',  ahd.  grintil  ,Riegel,  Pflugbaum',  mnd.  grindel,  grendel  , Querholz, Riegel,  Pflugbaum';
lit.  grindis,  grindas,  grindä  , Dielenbrett',  PI.  grindos  , Bretterbelag,  ge- dielter Fußboden',  grindöti,  grindyti,  grindziü  grlsti  ,mit  Brettern  belegen', grandä  ,Brückenbohle',  lett.  gr\da,  auch  grzds  , Fußboden,  Diele',  gruodi m.  PI.  , Bohlen,  Balken',  apr.  grandico  f.  , Bohle',  grandan  (Akk.)  ,Mann' (zur  Bedeutung  vgl.  E.  Lewy  IF.  32,  162  mit  Lit.);
460  f
slav.   greda  in   russ.   grjadd   ,Bett,    Reihe',   skr.   greda   ,Balken',   Sech. Jifada  ,Stange,  Balken,  Gerüst^  poln.  grzeda  ,Stange,  Furche,  Beet' ;  daneben  -. slav.  gr^db  in  sloven.  gred,  Gen.  gredi  , Stange'.
WP.  I  657,  WH.  I  623  f.,  Trautmann  98.
1.  ghreu-  :  ghrau-  :  ghrü-  ,zusaninienstürzen,  einstürzen,  auf  etwas  stürzen'.
Hom.  Aor.  exqccov  (ßxQaJ^ov)  ,überfiel,  bedrängte*,  ^axQrjrjg  ,heftig  andrän-
gend,  ungestüm'  (-XQ^-f^-VO)  j
lat.  ingruö,  -ere  ,mit  Heftigkeit  hereinstürzen,  hereinbrechen',  congrua^ -ere  »zusammenfallen,  zusammentreffen';
lit.    griäuju,    grioviau,    griduti    ,niederbrechen    (trans.    intr.);    donnern* (iau  aus  eu;  daraus  das  r  von:)  griüvü  {griy,vü,  Trautmann  100),  griuvaü griüti  ,zusammenf allen,  in  Trümmer  fallen*  (griüvü  =  lat.  -gruö  aus  ^ghruuö)'^    ' lett.  ^J^aw;w,  grävu,  gi^aut  ,zertrümmern',  grüstu,  gruvu,  grut  ,einstürzen*,  ■ gfuveli  m.  PI.  , Schutt';  Anlautdoublette  neben  qreu-  (s.  dort)?
Russ.  dial.  grüchnuth  sa  ,mit  Geräusch  zusammenstürzen',  klr.  hrüchnuty jpoltern;  krähen',  skr.  grühäm,  gruhati  ,krachen',  sloven.  grüh  , Stein- geröll', grusa  ,grober  Sand,  Schotter',  poln.  gruchnqc  ,
===== leaf 117 (0-based) =====
 ertönen ;  mit  Krachen hinfallen;  fest  schlagen'  {gruchac  ^girren  wie  die  Taube*  malt  hingegen sicher  den  Girrlaut).
WP.  I  647 f.,  WH.  I  700 f.,  Trautmann  100.    Ob  zum  Folgenden?
2.  ghreu- :  ghrQu- :  ghrü-   , scharf  darüber  reiben,   zerreiben',  Erweiterung   ♦
von  gJier-  , reiben'.
Gr.  *x^auw,  Konj.  Aor.  XQ^^^^I]  »ritze,  verletze',  iyxQavo)  ,schlage  hinein', kypr.  xQ^^'^of.iai,  %^ai;^o^at  , stoße  an,  bin  benachbart',  äxQcci^S  , unberührt, rein*;  mit  Abtönung  *ghrö[u}-:  xQfi^S  , Oberfläche  eines  Körpers  (*worüber man  darüber  streift)',  daher  ,Haut,  Hautfarbe*  (Nom.  XQ^^S  ^.us  *ghrö[ii]-8, Gen.  XQOog  danach  aus  *g7irdu-ös]  daneben  dann  später  x^wTo'g),  XQV^^ und
```


### [2026-09-05T21:03:12.918Z] TOOL RESULT

```
7161:lemma: arua {* herui): "intestines' derived from Root/ lemma: gher-5, ghor-na\ "bowels'. 
18272:Root / lemma: deii(- : to look derived from Root / lemma: gher-3 und ghere-, ghre- : to 
33008:Root / lemma: gher-1 
33052:Root / lemma: gher-2 
33078:Root / lemma: gher-3, ghre- : ghro- : ghra- 
33134:Root / lemma: ghers-1, ghres- 
33159:Root / lemma: ghers-2 
33175:Root / lemma: gherto- 
36766:Root / lemma: gher-1 
36823:Root / lemma: gher-2 
36838:Root / lemma: gher-Sand ghera-, ghre- 
36881:Root / lemma: gher-4 
36925:Root / lemma: gher-5, ghor-na 
36960:lemma: gher-5, ghor-na\ " bowels '. [common alb. gh-> z\ 
36968:Root / lemma: gher-6 [ghera- : ghre-1) 
36999:Root / lemma: gher-7 
37004:Root / lemma: ghers- and partly gher- 
37014:eater)' derived Root/ lemma: ghers-, gher-\ "rigid, *pig' > Root/ lemma: portto-s\ pig' : 
37096:Root / lemma: gherzd(h), Gen. ghfzd(h)-es, gherzda 
38290:Root/ lemma: guer-, guera-\ to burn and be hot' derived from Root/ lemma: gher-San^ 
39398:g^era-: to devour; throat; but from Root/ lemma: gher-5, ghor-na\ bowels, [common alb. 
42430:Root / lemmai^b/^fr- : a kind of roebuck : Root / lemma: ghers-, gher-\ rigid : alb. o'er/r pig'
```


## [2026-09-05T21:03:27.602Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== leaf 96 full ===\"; awk 'BEGIN{RS=\"\\f\"} NR==97' POK_02.txt | sed -n 1,200p | grep -n -i \"begehr\\|zara\\|gairn\\|xai\\|char\\|4\\. gher\\|1\\. gher\" ; echo \"=== leaf 97 ===\"; awk 'BEGIN{RS=\"\\f\"} NR==98' POK_02.txt | grep -n -i \"begehr\\|zara\\|gairn\\|441\\|440\" | head -20"
}
```


## [2026-09-05T21:03:27.789Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==118' POK_02.txt | sed -n 1,60p"
}
```


### [2026-09-05T21:03:29.278Z] TOOL RESULT

```
=== leaf 96 full ===
=== leaf 97 ===
7:I.  gher-  ,begehren,  gern  haben*,  z.  T.  mit  Formen  von  einer  Basis  *ghere{iy :  gheri-  (s.  Persson  Beitr.  728). Ai.  hdryati  ,findet  Gefallen,  begehrt';  av.  zara-  m.  »Streben,  Ziel'; gr.  xa/^w  {*xccQi-(o),  xccQrj^ca  ,sich  freuen*,  xciQig  f.  ,Anmut,  Gunst*,  x<XQ(^ »Freude*,  x^^QOuog  ,Kampfesfreude  blitzend',  x^Ql^a  n.  ,Freude,  Vergnügen* ;
8:441
12:ahd.  ger  ,begehrend*,  gerön  ,begehren*,  ahd.  girig,  as.  gerag  ,gierig* ; got.  faihu-gairns  ,geldgierig*,  aisl.  gjarrij  ags.  georn  ,wozu  geneigt,  worauf begierig*,  ahd.  as.  gern  ,begierig,  eifrig  nach  etwas*,  Adv.  ahd.  gerno,  nhd. gerUy  Denom.  got.  gairnjan^  aisl.  girna,  ags.  giernan^  as.  girnean  , begehren*.
```


### [2026-09-05T21:03:31.187Z] TOOL RESULT

```
 ertönen ;  mit  Krachen hinfallen;  fest  schlagen'  {gruchac  ^girren  wie  die  Taube*  malt  hingegen sicher  den  Girrlaut).
WP.  I  647 f.,  WH.  I  700 f.,  Trautmann  100.    Ob  zum  Folgenden?
2.  ghreu- :  ghrQu- :  ghrü-   , scharf  darüber  reiben,   zerreiben',  Erweiterung   ♦
von  gJier-  , reiben'.
Gr.  *x^auw,  Konj.  Aor.  XQ^^^^I]  »ritze,  verletze',  iyxQavo)  ,schlage  hinein', kypr.  xQ^^'^of.iai,  %^ai;^o^at  , stoße  an,  bin  benachbart',  äxQcci^S  , unberührt, rein*;  mit  Abtönung  *ghrö[u}-:  xQfi^S  , Oberfläche  eines  Körpers  (*worüber man  darüber  streift)',  daher  ,Haut,  Hautfarbe*  (Nom.  XQ^^S  ^.us  *ghrö[ii]-8, Gen.  XQOog  danach  aus  *g7irdu-ös]  daneben  dann  später  x^wTo'g),  XQV^^ und
```


## [2026-09-05T21:03:41.232Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==119' POK_02.txt | sed -n 1,80p"
}
```


### [2026-09-05T21:03:43.174Z] TOOL RESULT

```
%^ot^w  ,die  Oberfläche  eines  Körpers  berühren  oder  bestreichen, färben,  beflecken',  x^w^ta,  -arog  ,Haut,  Hautfarbe,  Farbe,  Schminke',  x^ota,  .^M att.  xQOCi  , Körperoberfläche,  Haut,  Farbe'  (*x^w/-jtß) ;  "
gall.  *grava  ,Kies^,  cymr.  grOj  acorn.  groUj  mcorn.  groiv  ,Sand^,  mbret. grouanenn  ds.,  nbret.  gro{a)  f.  , Sandstrand*,  groan,  grouan  ,gravier'  (Voka- lismus unklar) ;
aisl.  grjön  n.  , Grütze  (*geschrotetes  Korn)',  mhd.  grien  m.  n.  ^Kiessand; sandiges  Ufer',  mnd.  gren  , Sandkorn*  (*ghreuno-]  auch  norw.  isl.  grugg n.  ^Bodensatz*  aus  *gruwwa-  als  ,sandartiger  Rückstand*).
Da  die  erweiterte  Wz.  ghreu-d-  mehrfach  auf  das  seelische  Gebiet  ange- wendet ist  (,im  Gemüte  hart  berühren*),  vermutet  man  auch  Zugehörig- keit von   ahd.  ingrüen,    mhd.   grüen,   grüiven   , schaudern,    fürchten',   mhd.
461
griul,  griuioel  ;Schrecken,  Greuel',  ahd.  grüsön,  grüwisön  , Schrecken empfinden',  nhd.  ,grauSj  grausen^  usw.,  ahd.  grunuy  -nnes  ,Jammer,  Elend', griuna  , Begierde,  Heftigkeit,  Grausamkeit'  u.  dgl.
Erweiterung-  ghreu-d-:
ahd.  *ßrgriozan  ,zerreiben*,  Partiz.  ßrgrozzen,  mhd.  ver-j  dnrcli-griezen ^in  kleine  Teile  zerreiben';  aisl.  grjöt  n.  (a-St.)  , Stein,  Grieß',  ags.  greot n.  ,Sand,  Staub,  Erde',  as.  griot  n.  ,Sand,  Ufer',  ahd.  griozj  mhd.  griez  m., n.  , Sandkorn,  Sand,  Ufergrieß',  nhd.  , Grieß'  (germ.  *greuta-  , Gestein, Sand,  Kies'  auch  in  VN  Greutungi  , Strandbewohner'  und  in  finn.  riutta , Sandbank,  Klippe');
aisl.  grautr  m.  , Grütze'  (,grohgemahlenes') ;  ags.  great  ,grobkörnig, groß,  dick'  (engl,  great),  afries.  grät,  as.  gröt,  ahd.  mhd.  gröz  ,groß',  mhd. auch  ,grob,  dick'  (germ.  *grauta-)  ;   über  aisl.  grotti  , Mühle'  s.  unter  gliren- ;
ags.  grytt  , Grütze'  (engl,  grits  ,ds.,  grober  Sand'),  ahd.  gruzzi,  mnd. griltte  , Grütze'  (germ.  *grut{a-)]  ags.  grüt  (Dat.  gryt)  t  ,grobes  Mehl, Treber',  afries.  gret  ,Sand',  mhd.  grüz  m.  ,Sand,  Getreidekorn',  nhd. Graus  , Sandkorn,  Schutt,  Geröll',  mnd.  grüt  ,Porsch  als  Gärungsmittel', ndl.  gruit  ,Malz,  Hefe,  Bodensatz',  norw.  grüt  n.  ,Bodensatz';  ags.  grot n.  , grobes  Mehl'  (germ.  *gruta-)  •
mit  Formans  -to-  oder  -so-:  mnd.  grüs,  gros  , zerbröckelte  Steine,  Kies';
bsl.  *grüdiö  , stampfe'  in  lit.  grudziu  oder  grüdau,  grüsti  , stampfen  (Gerste zur  Graupenbere
```


## [2026-09-05T21:04:05.515Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for w in \"^cream,\" \"^chrism,\" \"^Christ,\" \"^Christmas,\" \"^character,\" \"^charisma,\" \"^great,\" \"^gravel,\" \"^chrome,\" \"^chromium,\" \"^chromosome,\" \"^yearn,\" \"^greedy,\" \"^exhort,\" \"^ghat,\"; do echo \"### $w\"; grep -n \"$w\" KLN_1966.txt | head -3; done"
}
```


## [2026-09-05T21:04:06.385Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"cresme\\|chrisma\" KLN_1966.txt | head -10; echo \"=== which leaf has cream ===\"; awk 'BEGIN{RS=\"\\f\"} /^cream,/{print NR}' KLN_1966.txt | head"
}
```


### [2026-09-05T21:04:07.298Z] TOOL RESULT

```
### ^cream,
9598:cream,  n.  —  ME.  creme,  fr.  OF.  cresme  (F. crime),  which  is  a  blend  of  Gaulish  crama  and Eccles.  L.  chrisma,  fr.  Gk,  ypTapa.  See  chrism. Derivatives:  cream,  tr.  and  intr.  v.,  cream-er,  n., creamery  (q.v.),  cream-y,  adj. creamery,  n.  —  F.  cremerie,  fr.  crime.  See  cream and  -ery,
### ^chrism,
7562:chrism,  n.,  holy  oil.  —  ME.  crisme,  fr.  OE.  cris- ma,  fr.  Eccles.  L.  chrtsma,  fr.  Gk.  xpmp-a,  ‘an unguent’,  fr.  ypkw,  ‘t0  anoint’,  which  is  of  un¬ certain  origin.  It  possibly  derives  fr.  I.-E. *ghrei-,  *ghri-,  whence  also  Lith.  grieju,  grieti, ‘to  skim  the  cream  off’.  I.-E.  *ghrii-,  *ghri-  are enlargements  of  base  *gher-,  ‘to  rub’.  See  grind and  cp.  chondro-.  Cp.  also  rusma,  which  is  a doublet  of  chrism.  Cp.  also  Christ.  Cp.  also cream.
### ^Christ,
7565:Christ,  n.  —  L.  Christus,  fr.  Gk.  xpIoTo?,  ‘anoint¬ ed’,  translation  of  Heb.  mashtah;  verbal  adj. of  xpfew,  ‘to  anoint’.  See  chrism.
### ^Christmas,
7573:Christmas,  n.  —  ME.  cristesmesse,  fr.  Late  OE.
### ^character,
### ^charisma,
### ^great,
### ^gravel,
16619:gravel,  n.  —  ME.  gravel,  fr.  OF.  gravele,  gravelle, ‘gravel,  sand,  beach,  strand’  (whence  F.  gra¬ velle,  ‘gravel’,  a  medical  term),  dimin.  of  OF. grave  (F.  grive),  ‘strand  of  sand,  sandbank’, which  is  of  uncertain,  possibly  Celtic,  origin. Cp.  W.  gro,  ‘coarse  gravel’,  Bret,  grouan,  Co. grow,  ‘gravel’.  Cp.  also  grave,  ‘to  clean  (the  hull of  a  ship)’,  grit,  groats,  grout.
### ^chrome,
7587:chrome,  n.,  1)  chromium;  2)  chrome  steel.  —  F., coined  by  the  French  chemist  Nicolas-Louis Vauquelin  (1763-1829)  in  1797  fr.  Gk.  /pupa, gen.  /pcopaxo;,  ‘surface  of  the  body,  skin,  color of  the  skin,  color’,  which  is  rel.  to  /poid,  of s.m.,  /pco;,  gen.  /purd;,  of  s.m.,  /pd^civ,  ‘to touch  the  surface  of  a  body,  to  tinge,  to  color’, fr.  I.-E.  base  *ghrdu-,  *ghrd-,  ‘to  rub,  smear, tinge’,  which  is  rel.  to  base  *gher-,  ‘to  rub’, whence  Gk.  /pteiv,  ‘to  rub,  anoint’,  /pinna, ‘an  unguent’.  See  chrism  and  cp.  -chroia,  chroma, chromatic,  and  the  second  element  in  helio¬ chrome,  homochromous,  metachromatism,  me¬ tachrosis,  monochroic,  monochrome,  parachroma. Derivative:  chrome,  tr.  and  intr.  v. chromic,  adj.,  pertaining  to  chromium.  —  Formed fr.  chromium  with  suff.  -ic.
### ^chromium,
### ^chromosome,
### ^yearn,
### ^greedy,
16653:greedy,  adj.  —  ME.  gredy,  fr.  OE.  grxdig,  rel.  to OS.  gradag,  ‘greedy’,  ON,  gradr,  ‘greed,  hun¬ ger’,  ON.  gradugr,  Dan.  graadig,  Du.  gretig, OHG.  grdtag,  ‘greedy’,  Goth,  gredus,  ‘hunger’, gredags,  ‘hungry’,  and  perh.  cogn.  with  OI. grdhyati,  ‘is  greedy’,  gardhah,  ‘greed’.  Cp. greed.
### ^exhort,
### ^ghat,
```


### [2026-09-05T21:04:09.086Z] TOOL RESULT

```
7563:Derivative:  chrism-al,  adj. chrism,  tr.  v.,  to  anoint  with  chrism.  —  OF.  chres- mer,  fr.  Eccles.  L.  chrismare,  fr.  chrtsma.  See chrism,  n.
9598:cream,  n.  —  ME.  creme,  fr.  OF.  cresme  (F. crime),  which  is  a  blend  of  Gaulish  crama  and Eccles.  L.  chrisma,  fr.  Gk,  ypTapa.  See  chrism. Derivatives:  cream,  tr.  and  intr.  v.,  cream-er,  n., creamery  (q.v.),  cream-y,  adj. creamery,  n.  —  F.  cremerie,  fr.  crime.  See  cream and  -ery,
=== which leaf has cream ===
```


## [2026-09-05T21:04:20.196Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"rusma\" KLN_1966.txt | head -5; echo \"=== leaves ===\"; python3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\ndef leafof(lineno):\n    return t[:sum(len(l)+1 for l in lines[:lineno-1])].count('\\f')\nfor ln in [9598,7562,7565,7573,7587,16619,16653]:\n    print(ln, 'leaf', leafof(ln), '-> printed p ~', 2*(leafof(ln)-12))\nEOF"
}
```


### [2026-09-05T21:04:22.349Z] TOOL RESULT

```
7562:chrism,  n.,  holy  oil.  —  ME.  crisme,  fr.  OE.  cris- ma,  fr.  Eccles.  L.  chrtsma,  fr.  Gk.  xpmp-a,  ‘an unguent’,  fr.  ypkw,  ‘t0  anoint’,  which  is  of  un¬ certain  origin.  It  possibly  derives  fr.  I.-E. *ghrei-,  *ghri-,  whence  also  Lith.  grieju,  grieti, ‘to  skim  the  cream  off’.  I.-E.  *ghrii-,  *ghri-  are enlargements  of  base  *gher-,  ‘to  rub’.  See  grind and  cp.  chondro-.  Cp.  also  rusma,  which  is  a doublet  of  chrism.  Cp.  also  Christ.  Cp.  also cream.
33369:rusma,  n.,  a  depilatory.  - —  It.  and  F.,  a  corrup¬ tion  of  Turk,  khorozma,  inexact  transliteration of  Gk.  xpiafjux,  ‘unguent’,  lit.  ‘anything  smear¬ ed  on’,  fr.  xpfs'-v,  ‘to  smear,  anoint’.  See
=== leaves ===
9598 leaf 204 -> printed p ~ 384
7562 leaf 160 -> printed p ~ 296
7565 leaf 160 -> printed p ~ 296
7573 leaf 160 -> printed p ~ 296
7587 leaf 160 -> printed p ~ 296
16619 leaf 365 -> printed p ~ 706
16653 leaf 366 -> printed p ~ 708
```


## [2026-09-05T21:05:13.479Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==205' KLN_1966.txt | grep -n \"^[0-9]\\{2,4\\}$\\|^ *[0-9]\\{3\\}\" | head; echo \"--- head of leaf 205 ---\"; awk 'BEGIN{RS=\"\\f\"} NR==205' KLN_1966.txt | head -4; echo \"--- tail ---\"; awk 'BEGIN{RS=\"\\f\"} NR==205' KLN_1966.txt | tail -4"
}
```


### [2026-09-05T21:05:15.400Z] TOOL RESULT

```
--- head of leaf 205 ---
o?,  ‘tree,  oak’.  The  first  element  is  cogn. with  Goth,  hardus,  OE.  heard;  see  hard.  The second  element  is  cogn.  with  L.  aesculus,  ‘the Italian  oak’,  OE.  ac,  ‘oak’;  see  oak  and  cp. Aesculus.
cratch,  n.,  crib,  rack.  —  ME.  crecche,  fr.  OF. creche  (F.  criche),  fr.  Frankish  *kripja,  which  is related  to  OHG.  krippa,  OE.  cribb.  See  crib  and cp.  cradge,  crbchc.
cratch,  tr.  and  intr.  v.,  to  scratch  ( obsol .)  —  MDu. cratsen,  rel.  to  OHG.  krazzon,  ‘to  scratch’.  See scratch.
crate,  n.  — -  L.  cratis,  ‘wickerwork,  hurdle’,  fr. I.-E.  base  *qerat-,  *qert-,  ‘to  roll  or  twist  to¬ gether’,  whence  also  L.  crassus,  ‘thick,  solid, dense,  fat’,  OI.  kptsnah,  ‘complete,  whole’, Russ. -Church  Slav,  cristvu,  cirstvu,  ‘firm,  solid genuine’,  Russ,  krutu,  ‘firm,  thick’,  OE.  hyrd, ‘door’  (orig.  ‘door  of  wickerwork’),  hyrdel, ‘hurdle’.  See  hurdle  and  cp.  cartilage,  crass, creel.  The  above  base  is  a  -/-enlargement of  base  *qer-,  ‘to  turn,  twist’,  whence  L.  curvus , ‘bent,  crooked’.  See  curve  and  cp.  words  there referred  to.
--- tail ---
credenda,  n.  pi.,  articles  of  faith.  —  L.  credenda, lit.  ‘those  things  which  must  be  believed’,  neut. pi.  of  credendus ,  gerundive  of  credere,  ‘to  be¬ lieve’.  See  creed.  For  other  Latin  gerundives used  in  English  see  agenda  and  words  there referred  to.
credeni,  adj.,  believing.  —  L.  credens,  gen.  -entis, pres.  part,  of  credere,  ‘to  believe’.  See  creed and  -ent.
credential,  adj.,  that  which  entitles  to  credit.  — Formed  with  adj.  suff.  -al  fr.  ML.  credentia.  See credence.
Derivatives:  credential,  tr.  v.,  credentials,  n.  pi. credibility,  n.  — -  ML.  credibilitds,  fr.  L.  credi- bilis.  See  next  word  and  -ity. credible,  adj.  —  L.  credibilis,  ‘worthy  of  belief, credible’,  fr.  credere.  See  creed  and  -ible.
```


## [2026-09-05T21:05:30.408Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for w in \"^character,\" \"^charisma,\" \"^great,\" \"^yearn,\" \"^exhort,\" \"^chromosome,\" \"^chromium,\" \"^ghat,\" \"^ghaut,\"; do echo \"### $w\"; grep -n \"$w\" KLN_1971.txt | head -2; done"
}
```


### [2026-09-05T21:05:32.132Z] TOOL RESULT

```
### ^character,
44043:character, n. — ME. caracter , caractere, fr. OF. 
105211:character, letter’, from the stem of ypdtqsetv, ‘to 
### ^charisma,
### ^great,
105902:great, adj. — ME. great, gret, greet, grete, fr. 
154952:great, much’);rel. to OE. ma, ‘more’(neut. and 
### ^yearn,
269617:yearn, intr. v. — ME. yernen, fr. OE. geornan, 
### ^exhort,
88066:exhort, tr. and intr. v., to advise earnestly. — 
### ^chromosome,
46505:chromosome, n., a minute body occurring in de- 
226290:chromosome, plasmosome. — Fr. Gk. awjia, 
### ^chromium,
46477:chromium, n., name of a metallic element (chem.) 
### ^ghat,
102310:ghat, ghaut, n., a mountain pass; a landing place 
### ^ghaut,
```


## [2026-09-05T21:05:33.356Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== MON کریسمس ==\"; grep -n \"کریسمس\" MON_part1.txt MON_part2.txt | head -5; echo \"== MON کروم ==\"; grep -n \"کروم\\b\\|کرومیوم\\|کروموزوم\\|کروموسوم\" MON_part1.txt MON_part2.txt | head -8; echo \"== ARY ==\"; grep -n \"کریسمس\\|کروموزوم\\|کرومیوم\" incoming/ARY/ARY_pages.txt | head -5; echo \"== MON کرم cream ==\"; grep -n \"کِرِم\\|کرم (فر\\|کرم(فر\" MON_part1.txt MON_part2.txt | head -5"
}
```


### [2026-09-05T21:05:33.469Z] TOOL RESULT

```
== MON کریسمس ==
== MON کروم ==
MON_part2.txt:22235:کرم: ع)() رزه تاکدا. کروم 
MON_part2.txt:22593:کرومانیون: ۵۲۵0۸ (۱.) ۳۳۹ از 
MON_part2.txt:63850:(مکروم): ۱ [ع. کرم] (امف.) تا ک 
MON_part2.txt:70466:اخیر به پیچ میکرومتری موسوم است و یک 
MON_part2.txt:91609:هموکروموژن که ماد رنگی (قرمز تیره) 
MON_part2.txt:91616:هموکروموژن در حقیقت یک هماتین تغییر 
MON_part2.txt:93071:به کروموزوم درمی آیند» در داخل هسته 
== ARY ==
== MON کرم cream ==
```


## [2026-09-05T21:05:38.357Z] TOOL CALL #23: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p189_n12.png"
}
```


### [2026-09-05T21:05:38.379Z] TOOL RESULT

```

```


## [2026-09-05T21:05:47.257Z] TOOL CALL #24: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p189_empty.png"
}
```


### [2026-09-05T21:05:47.268Z] TOOL RESULT

```

```


## [2026-09-05T21:05:47.375Z] TOOL CALL #25: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p189_khoris.png"
}
```


### [2026-09-05T21:05:47.389Z] TOOL RESULT

```

```


## [2026-09-05T21:05:58.140Z] TOOL CALL #26: Bash

```json
{
 "command": "sed -n 1,60p tools/fetch_source.py; echo ===; sed -n 1,80p tools/verify_check.py"
}
```


### [2026-09-05T21:05:58.179Z] TOOL RESULT

```
Exit code 1
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
(eval):1: == not found
```


## [2026-09-05T21:05:59.993Z] TOOL CALL #27: Bash

```json
{
 "command": "sed -n 1,90p tools/verify_check.py"
}
```


### [2026-09-05T21:06:00.038Z] TOOL RESULT

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
```


## [2026-09-05T21:06:07.525Z] TOOL CALL #28: Bash

```json
{
 "command": "for u in cream chrism chrome character great gravel charisma; do python3 tools/fetch_source.py \"https://www.etymonline.com/word/$u\" --note \"page 189, Gher 3/Gher 4: $u chain\" ; done 2>&1 | tail -20"
}
```


### [2026-09-05T21:06:12.192Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/e604d9f555976e0c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/714ff44b16524c2f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/108342db65c49352.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a70b443aaab279dd.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d473ecc6d4dbe8a7.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/3baf3e9832ff8922.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/36a0834d503486e1.txt
```


## [2026-09-05T21:06:14.827Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in e604d9f555976e0c 714ff44b16524c2f 108342db65c49352 a70b443aaab279dd d473ecc6d4dbe8a7 3baf3e9832ff8922 36a0834d503486e1; do echo \"##### $f\"; head -c 1800 $f.txt | tr -s ' \\n' ' \\n' | sed -n 1,40p; echo; done"
}
```


### [2026-09-05T21:06:16.418Z] TOOL RESULT

```
##### e604d9f555976e0c
URL: https://www.etymonline.com/word/cream
FETCHED: 2026-09-05T21:06:09Z
STATUS: 200
TITLE: Cream - Etymology, Origin & Meaning
Cream - Etymology, Origin & Meaning 
 Search 
 Log in 
 Columns 
 Forum 
 Apps 
 Premium 
 Log in 
 Advertisement Remove Ads 
 Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.
 Origin and history of cream 
 cream (n.) 
 early 14c., creyme , "the rich and buttery part of milk," from Old French cresme, craime, creme "chrism, holy oil" (13c., Modern French crème ). This word is a blend of Late Latin chrisma "ointment" (from Greek khrisma "unguent;" from PIE root *ghrei- "to rub") and Late Latin cramum "cream," which is of uncertain origin, perhaps from Gaulish. The French word replaced Old English ream; it was re-borrowed 19c. as creme .
 From early 15c. as "dish or confection made from or resembling cream." The figurative sense of "most excellent element or part" is from 1580s. It is attested from 1660s as "any part that separates from the rest and rises to the surface" and also in its application to substances resembling cream.
 Cream-cheese is from 1580s. Cream-soda is attested by 1854. Cream-colored (also cream-coloured ) "having the pale, yellowish-white color of cream," is from 1707. Cold cream , a cosmetic, is by 1709, translating Latin ceratum refrigerans (see cold (adj.)).
 also from early 14c. 
 cream (v.) 
 mid-15c., "to foam, to froth," from cream (n.). From 1610s in figurative sense of "remove the best part of." Meaning "to beat, thrash, wreck" is 1929, U.S. slang; the exact sense connection is unclear. There was a slang cream (v.) in the 1920s that meant "cheat, deceive, especially by guile." Related: Creamed ; creaming .
 also from mid-15c. 
 Entries linking to cream 
 cold (
##### 714ff44b16524c2f
URL: https://www.etymonline.com/word/chrism
FETCHED: 2026-09-05T21:06:09Z
STATUS: 200
TITLE: Chrism - Etymology, Origin & Meaning
Chrism - Etymology, Origin & Meaning 
 Search 
 Log in 
 Columns 
 Forum 
 Apps 
 Premium 
 Log in 
 Advertisement Remove Ads 
 Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.
 Origin and history of chrism 
 chrism (n.) 
 "oil mingled with balm, a sacred ointment consecrated and used in Church rites," late Old English chrisma , from Church Latin chrisma , from Greek khrisma "an unguent, anointing, unction," from khriein "to anoint" (from PIE root *ghrei- "to rub"). Chrisom "baptismal robe," is a c. 1200 variant of this. Related: Chrismal ; chrismatory .
 Entries linking to chrism 
 anoint (v.) 
 mid-14c., enointen , "pour oil upon, smear with ointment," from Old French enoint "smeared on," past participle of enoindre "smear on," from Latin inunguere "to anoint," from in- "in, into" (see in ) + unguere "to smear" (see unguent (n.)).
 Forms in a- by late 14c. Originally in reference to grease or oil smeared on for medicinal purposes; its use in the Coverdale Bible in reference to Christ (as in The Lord's Anointed ; see chrism ) has spiritualized the word. Related: Anointed ; anointing (c. 1300 as a verbal noun).
 *ghrei- 
 ghrēi- , Proto-Indo-European root meaning "to rub." 
 It might form all or part of: chrism ; Christ ; christen ; Christian ; Christmas ; cream ; grime ; grisly ; Kriss Kringle .
 It might also be the source of: Greek khriein "to anoint, besmear;" Lithuanian grieju, grieti "to skim the cream off;" Old English grima "mask, helmet, ghost," Middle Low German greme "dirt."
 Advertisement Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove
##### 108342db65c49352
URL: https://www.etymonline.com/word/chrome
FETCHED: 2026-09-05T21:06:10Z
STATUS: 200
TITLE: Chrome - Etymology, Origin & Meaning
Chrome - Etymology, Origin & Meaning 
 Search 
 Log in 
 Columns 
 Forum 
 Apps 
 Premium 
 Log in 
 Advertisement Remove Ads 
 Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.
 Origin and history of chrome 
 chrome (n.) 
 1800, "chromium," from French chrome , the name proposed by Fourcroy and Haüy for a new element, from Greek khrōma "color" (see chroma ); so called because it makes colorful compounds. The metallic element had been isolated 1798 by French chemist Louis Nicolas Vauquelin, who named it chrome . It is now known as chromium (q.v.).
 Chrome continued in commercial use in English for "chrome steel" (steel with 2 percent or so chrome) after the chemical name was changed internationally. As a short form of chromium plating it dates from 1937. Related: Chromic .
 also from 1800 
 Entries linking to chrome 
 chroma (n.) 
 in reference to color, "intensity of distinctive hue, degree of departure of a color-sensation from that of white or gray," 1889, from Latinized form of Greek khrōma "surface of the body, skin, color of the skin," also used generically for "color" and, in plural, "ornaments, makeup, embellishments," a verbal noun from khroizein "to color, stain, to touch the surface of the body," khrosthenai "to take on a color or hue," from khros, khroia "surface of the body, skin."
 Beekes considers this noun to be of uncertain origin. It sometimes is explained as being somehow from PIE *ghreu- "to rub, grind" (see grit (n.)).
 chromium (n.) 
 metallic element, 1807, Latinized from French chrome (Fourcroy and Haüy), from Greek chroma "color" (see chrome ; also see chrom
##### a70b443aaab279dd
URL: https://www.etymonline.com/word/character
FETCHED: 2026-09-05T21:06:10Z
STATUS: 200
TITLE: Character - Etymology, Origin & Meaning
Character - Etymology, Origin & Meaning 
 Search 
 Log in 
 Columns 
 Forum 
 Apps 
 Premium 
 Log in 
 Advertisement Remove Ads 
 Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.
 Origin and history of character 
 character (n.) 
 mid-14c., carecter , "symbol marked or branded on the body;" mid-15c., "symbol or drawing used in sorcery;" late 15c., "alphabetic letter, graphic symbol standing for a sound or syllable;" from Old French caratere "feature, character" (13c., Modern French caractère ), from Latin character , from Greek kharaktēr "engraved mark," also "symbol or imprint on the soul," properly "instrument for marking," from kharassein "to engrave," from kharax "pointed stake," a word of uncertain etymology which Beekes considers "most probably Pre-Greek." In English the Latin ch- spelling was restored from 1500s.
 The meaning of Greek kharaktēr was extended in Hellenistic times by metaphor to "a defining quality, individual feature." In English, the meaning "sum of qualities that define a person or thing and distinguish it from another" is from 1640s. That of "moral qualities assigned to a person by repute" is from 1712.
 You remember Eponina, who kept her husband alive in an underground cavern so devotedly and heroically? The force of character she showed in keeping up his spirits would have been used to hide a lover from her husband if they had been living quietly in Rome. Strong characters need strong nourishment. [Stendhal 
 "de l'Amour,"  1822] 
 The sense of "person in a play or novel" is first attested 1660s, in reference to the "defining qualities" he or she is 
##### d473ecc6d4dbe8a7
URL: https://www.etymonline.com/word/great
FETCHED: 2026-09-05T21:06:11Z
STATUS: 200
TITLE: Great - Etymology, Origin & Meaning
Great - Etymology, Origin & Meaning 
 Search 
 Log in 
 Columns 
 Forum 
 Apps 
 Premium 
 Log in 
 Advertisement Remove Ads 
 Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.
 Origin and history of great 
 great (adj.) 
 Old English great "big, tall, thick, stout, massive; coarse," from West Germanic *grauta- "coarse, thick" (source also of Old Saxon grot , Old Frisian grat , Dutch groot , German groß "great"). If the original sense was "coarse," it is perhaps from PIE root *ghreu- "to rub, grind," via the notion of "coarse grain," then "coarse," then "great;" but "the connextion is not free from difficulty" [OED].
 It took over much of the sense of Middle English mickle , and itself now is largely superseded by big and large except in reference to non-material things. In the sense of "excellent, wonderful" great is attested from 1848.
 Great White Way "Broadway in New York City" is from 1901, in reference to brilliant street illumination. The Great Lakes of North America so called by 1726, perhaps 1690s. Great Spirit "high deity of the North American Indians," 1703, originally translates Ojibwa kitchi manitou. The Great War originally (1887) referred to the Napoleonic Wars, later (1914) to what we now call World War I (see world ).
 "The Great War" — as, until the fall of France, the British continued to call the First World War in order to avoid admitting to themselves that they were now again engaged in a war of the same magnitude. [Arnold Toynbee, "Experiences," 1969]
 Also formerly with a verb form, Old English greatian "to become enlarged," Middle English greaten "to become larger
##### 3baf3e9832ff8922
URL: https://www.etymonline.com/word/gravel
FETCHED: 2026-09-05T21:06:11Z
STATUS: 200
TITLE: Gravel - Etymology, Origin & Meaning
Gravel - Etymology, Origin & Meaning 
 Search 
 Log in 
 Columns 
 Forum 
 Apps 
 Premium 
 Log in 
 Advertisement Remove Ads 
 Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.
 Origin and history of gravel 
 gravel (n.) 
 "stone in small, irregular fragments," early 13c., from Old French gravele "sand, gravel; sea-shore; sandy bed of a river," diminutive of grave "sand, seashore" (Modern French grève ), possibly from Celtic *graw- (compare Welsh gro "coarse gravel," Breton grouan , Cornish grow "gravel"), perhaps ultimately from PIE *ghreu- "to rub, grind" (see grit (n.)). Gravel-crusher was World War I slang for "infantryman."
 also from early 13c. 
 Entries linking to gravel 
 grit (n.) 
 Old English greot "sand, dust, earth, gravel," from Proto-Germanic *greutan "tiny particles of crushed rock" (source also of Old Saxon griot , Old Frisian gret , Old Norse grjot "rock, stone," German Grieß "grit, sand"), from PIE *ghreu- "rub, grind" (source also of Lithuanian grūdas "corn, kernel," Old Church Slavonic gruda "clod"). Sense of "pluck, spirit, firmness of mind" first recorded American English, 1808.
 If he hadn't a had the clear grit in him, and showed teeth and claws, they'd a nullified him so, you wouldn't have see'd a grease spot of him no more. [Thomas Chandler Haliburton, "Sam Slick in England," 1843]
 gravelly (adj.) 
 late 14c., "covered with gravel or sand," from gravel + -y (2). Of voices, by 1943.
 sand (n.) 
 "water-worn detritus finer than gravel; fine particles of rocks (largely crystalline rocks, especially quartz); the material of the beach, desert, or sea-bed;" Ol
##### 36a0834d503486e1
URL: https://www.etymonline.com/word/charisma
FETCHED: 2026-09-05T21:06:12Z
STATUS: 200
TITLE: Charisma - Etymology, Origin & Meaning
Charisma - Etymology, Origin & Meaning 
 Search 
 Log in 
 Columns 
 Forum 
 Apps 
 Premium 
 Log in 
 Advertisement Remove Ads 
 Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.
 Origin and history of charisma 
 charisma (n.) 
 1875, "special spiritual gift or power divinely conferred, talent from God" (as on the early Christians in "Acts," etc.), Latinized form of Greek kharisma "favor, divine gift," from kharizesthai "to show favor to," from kharis "grace, beauty, kindness" ( Charis was the name of one of the three attendants of Aphrodite), which is related to khairein "to rejoice at" (from PIE root *gher- (2) "to like, want").
 In the form charism (plural charismata ) it is attested in the "special spiritual gift from god" sense from 1640s. Middle English, meanwhile, had karisme "spiritual gift, divine grace" (c. 1500).
 These gifts were of two classes, the gift of healing and gift of teaching, the latter again being of two kinds, the gift of prophecy and the gift of tongues. Such gifts have been claimed in later ages by certain teachers and sects in the church, as the Montanists and the Irvingites, and in recent times by some of those who practise the so-called faith-cure. [Century Dictionary, 1897]
 The meaning "gift of leadership, power of authority" is from c. 1930, from German, used in this sense by Max Weber (1864-1920) in "Wirtschaft u. Gesellschaft"  (1922). The more mundane sense of "personal charm" recorded by 1959.
 also from 1875 
 Entries linking to charisma 
 charismatic (adj.) 
 "of or pertaining to charisma," 1851, in Bible commentary and theology, in reference
```


## [2026-09-05T21:06:22.170Z] TOOL CALL #30: Bash

```json
{
 "command": "for u in yearn exhort ghat christmas; do python3 tools/fetch_source.py \"https://www.etymonline.com/word/$u\" --note \"page 189, Gher 3/4: $u\"; done; for w in \"کریسمس\" \"کروموزوم\" \"کروم\" \"کرم\"; do python3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/$w\" --note \"page 189: Persian $w borrowing\"; done"
}
```


### [2026-09-05T21:06:27.576Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/4fa6e2b6b73da474.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/0ae49def8c67c42a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/865d7530e3559878.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/9612a31fc0af6b58.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/1d0ccdd48c82612f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b9d1346a17b905a9.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/68a4ed2c40eb9dc3.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/7738476aa3dfe87a.txt
```


## [2026-09-05T21:06:30.036Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in 4fa6e2b6b73da474 0ae49def8c67c42a 865d7530e3559878; do echo \"##### $f\"; sed -n 1,20p $f.txt | head -c 1200; echo; done"
}
```


## [2026-09-05T21:06:31.056Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in 9612a31fc0af6b58 1d0ccdd48c82612f b9d1346a17b905a9 68a4ed2c40eb9dc3; do echo \"##### $f\"; grep -n -A3 -i \"Persian\\|Etymology\" $f.txt | head -40; echo; done"
}
```


### [2026-09-05T21:06:31.572Z] TOOL RESULT

```
##### 4fa6e2b6b73da474
URL: https://www.etymonline.com/word/yearn
FETCHED: 2026-09-05T21:06:24Z
STATUS: 200
TITLE: Yearn - Etymology, Origin & Meaning

Yearn - Etymology, Origin & Meaning 

 Search 
 Log in 

 Columns 
 Forum 
 Apps 
 Premium 

 Log in 

 Advertisement Remove Ads 
 Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.


##### 0ae49def8c67c42a
URL: https://www.etymonline.com/word/exhort
FETCHED: 2026-09-05T21:06:24Z
STATUS: 200
TITLE: Exhort - Etymology, Origin & Meaning

Exhort - Etymology, Origin & Meaning 

 Search 
 Log in 

 Columns 
 Forum 
 Apps 
 Premium 

 Log in 

 Advertisement Remove Ads 
 Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.


##### 865d7530e3559878
URL: https://www.etymonline.com/word/ghat
FETCHED: 2026-09-05T21:06:25Z
STATUS: 200
TITLE: Ghat - Etymology, Origin & Meaning

Ghat - Etymology, Origin & Meaning 

 Search 
 Log in 

 Columns 
 Forum 
 Apps 
 Premium 

 Log in 

 A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 

 Quick and reliable accounts of the origin and history of English words. Scholarly, yet simple.
```


### [2026-09-05T21:06:33.261Z] TOOL RESULT

```
##### 9612a31fc0af6b58
4:TITLE: Christmas - Etymology, Origin & Meaning
5-
6:Christmas - Etymology, Origin & Meaning 
7-
8- Search 
9- Log in 
--
104: <a href="https://www.etymonline.com/word/Christmas">Etymology of Christmas by etymonline</a> Copy 
105-
106- APA Style :
107: Harper, D. (n.d.). Etymology of Christmas. Online Etymology Dictionary. Retrieved September 5, 2026, from https://www.etymonline.com/word/Christmas Copy 
108-
109- Chicago Style :
110: Harper Douglas, "Etymology of Christmas," Online Etymology Dictionary, accessed September 5, 2026, https://www.etymonline.com/word/Christmas. Copy 
111-
112- MLA Style :
113: Harper, Douglas. "Etymology of Christmas." Online Etymology Dictionary, https://www.etymonline.com/word/Christmas. Accessed 5 September, 2026. Copy 
114-
115- IEEE Style :
116: D. Harper. "Etymology of Christmas." Online Etymology Dictionary. https://www.etymonline.com/word/Christmas (accessed September 5, 2026). Copy 
117-
118- Remove Ads 
119- Advertisement Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.

##### 1d0ccdd48c82612f
57: Persian 
58-
59: Toggle Persian subsection 
60-
61- 1.1 
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
--
139: Persian
140- [ edit ] 
141-
142: Etymology
143- [ edit ] 
144-
145: Etymology tree
146-
147- Proto-Indo-European *gʰer- 
148- Proto-Indo-European *gʰrey- der. 
--
198: Persian کریسمس 
199-
200- Borrowed from English Christmas .
201-
--
239: Categories : Persian terms derived from Old English 
240: Persian terms derived from Biblical Hebrew 
241: Persian terms derived from Proto-Germanic 
242: Persian terms derived from Proto-Italic 
243: Persian terms derived from Proto-West Germanic 
244: Persian terms derived from Middle English 
245: Persian terms derived from Latin 
246: Persian terms derived from Ancient Greek 
247: Persian terms derived from Aramaic 
248: Persian terms borrowed from English 
249: Persian terms derived from the Proto-Indo-European root *mey- (change) 
250: Persian terms derived from the Proto-Indo-European root *gʰrey- 
251: Persian terms derived from Proto-Hellenic 
252: Persian terms derived from English 

##### b9d1346a17b905a9

##### 68a4ed2c40eb9dc3
57: Persian 
58-
59: Toggle Persian subsection 
60-
61- 1.1 
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
--
76: Etymology 
77-
78- 2.2 
79- Noun 
--
147: Persian
148- [ edit ] 
149-
150- Chemical element ( edit ) 
--
174: Persian Wikipedia has an article on: کروم 
175-
176- Wikipedia fa 
177-
178: Etymology
179- [ edit ] 
180-
181: Etymology tree
182-
183- Proto-Hellenic *kʰrṓwmə 
184- Ancient Greek χρῶμα ( khrôma ) bor. 
--
186: Persian کروم 
187-
188- Borrowed from French chrome .
189-
--
211: Etymology
212- [ edit ] 
213-
```


## [2026-09-05T21:06:40.173Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"### کروموزوم\"; head -c 700 b9d1346a17b905a9.txt; echo; echo \"### کرم\"; grep -n -i \"cream\\|French\\|Etymology 3\\|Etymology 4\" 7738476aa3dfe87a.txt | head -30"
}
```


### [2026-09-05T21:06:40.224Z] TOOL RESULT

```
### کروموزوم
URL: https://en.wiktionary.org/wiki/کروموزوم
FETCHED: 2026-09-05T21:06:26Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 404: Not Found
### کرم
103: Etymology 3 
115: Etymology 4 
354: From French crème .
372: cream ( dairy product ) 
378: Etymology 3
447: Etymology 4
656: Persian terms derived from French
```


## [2026-09-05T21:06:47.338Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT zara ===\"; grep -n \"zara-\\|zara,\\|^zara\" BRT.txt | head -20"
}
```


### [2026-09-05T21:06:47.386Z] TOOL RESULT

```
=== BRT zara ===
4180:•  j.  'anhuyav-  Adj.  'der  sich  (den  Anspruch auf)  das  (andere)    Leben  erwirbt':    zara-
4708:•  j.  anyö,  ainyö  Adv.  'ausser,  ausgenom- men, abgesehen  voa  — ',  mit  Abi.:  ^at  äs ma^änqm  ,  .  v3r>iravasl3mS  ain-  zara- %ulträ:  yt.jg.^6;  38;—  kakmai paoiryd malyänqm  "apir^si  (sd.)  tum  . .  an'  mana (statt  AbL)  yat  zaraittitnit  ,  .  ahntäi paoiryS  afi^Dse  (sd.)  az»m  an"  ^wat  yat tara>usträt  V.  2.  i  f.;  —  taii  also  s}a  .  , äamanqm  ham.rai'iviayeiti  . .  an'  ahmüt yS . .  "nicht  erstreckt  der  Hund  . .  auf  die Geschöpfe  . .  seinen  indirekten  EinBuss ausser  auf  den,  der  . ."  V.5.34;  —  kaf nä  *daivayasnai  vä  .  .  gSus  aiiiiitya  (sd.)
5480:kainlnö  kihrpa  srJrayh  Yt5.64;  —  bow- raini  vastrh  vat»hala  °dvl  süra  anilAi/a Yt.5. 129;  7,19,88,91,  95,96,  123,  127, laS;  —  avaj  nyapt^m  dazdi  me  vami/ii snisU  -dvliyS.)  süre  anil/iile  yäh  a  . .  Yt 5-  18;  9.  63.  77',  »S.  87,  90-  94.  130. 131,  Ny.  /.  19;  —  paili  dim  p»r>sal  zara- %uilrS  "dvltn  sürqnt  anahitqm  yt5.9o; I,  9,  62,  94,  Vr,2.  7,  Ny.4.9.
5830:•  j.,  g.  ast'vant-  Adj.  (fem.  'vaitt-)  'mit einem  stofflichen  Leib  versehen,  leiblich,  | stofflich,  materiell';  Ayat  'vant»m  dada uäatam  "als  du  Leben  mit  Leib  versahst" Y,_5/.  11;  —  tat  (näml.  mlidf/n)  er  mazdä vairlm  'vaits  ustänät  data  vatfhlus ^ttoiana  manar-ks ySi . .  "diesen  köstlichen (Lohn)  ja,  0  M.,  werdet  ihr  durch  das Wirken  des  VM.  dem  leiblichen  Leben (derer)  verschaffen,  die  . ,"  Y.54. 14;  — •vat  ahm  hyät  uslStiä  (sd.)  aojSrigAvat "^.43-  16;  —  ash-atjrmya%a  astva  *kqm ustanava  (sd.)  °vat  *ai^yeja/nm  paitisät Yt.  13. 1 29;  —  *vTjvähu  (sd.)  paiii  tanusti 'vh  gays  *däryeife  FTVf.4.2.  A)  sonst. nur  als  Beiwort  von  a)  stay-  (sd.) :  zara- , %ustrahe..yS paoiryö  stsis  'vadyä ..  Yt.ij.  1 Sgf«.  b)  gai^ä-  (sd.),  Sg.  und  Plur.J darfsca  (sd.)  da^at^amirixfyantim  vTspatn yam  "vaitlm  gae^qm  Yt  i<).  94;  Y.  g.  8, 37.23,  *Vd.£'>;  —  zarai:mtr5  ratus 'vai>ya  gaf^ayä  Yt.  73.  4r;  j.  89;  — kat»  %wqm  paoiryS  'vai^yäi  hunüta gai^yäi  Y.p.  3;  4;  —  m/l  m?m>cainTs gai>a  'vaitls  asake  SrB._j;  Yt/5.  41,  V. , ^^•SS;  —  "J  ^^  apqm  a'javö..  jasanli..' yavanqm  .  .  västranqm  ,  ,  gafianamüa 'vaitinqm  Yt  ^'.29;  —  V?'"  ■  ■  /rävavacä .  .  zara'iuströ  gae'iabyö  'vaiHbyS  Y.ö'j.g; P.  13;  —  ahura  mazda  mainyö  spinista däiar>  gad'^ariqm  'vaitinqm  asäum  ''" I.  7- 1.  9- 1,  lo- ".  "■  I.  '4-  I,  34,  K
6082:jrjmuibmS  Y.57.4;  7.1,  2^.2;  —  zara- ^BsTrvm  .  .  yat  as  °hm  alavasfornd  (sd.) .■V._y.  4;  — j'aia  °ä7/  x!a%tym  cinasti  (sd) Y.20,3"';  —  äat..  ah<  nmänahe fraf^wd gäus  .  .  'um  .  .  i-ästrpm  V.J.  3;  —  asis/a itä  airihat  haca  vlsat  gaul  buyat  asUbm •am  Y.  60.  3 ;  —  us  nü  aiAhäi  vXse  jamyät •ämca  x/a^nm/a,.Y.6o.2.  III) 'Recht, reditmässiger  Anspruch  (auf  — )'  und  zu- gleich 'Gegenstand  des  Rechts,  worauf  man Anspruch  ha^  was  einem  gerecht  ist';  spez. von  dem  ftir  die  Zugehörigkeit  zur  sara- l^u/jyischen  Religion  und  das  ihr  ent- sprechende Verhalten  zugesicherte  und  da- durch erworbene  (höchste)  Anrecht,  d.  i.  das auf  das  ewige  Gut  (Paradies)  und  dieses selbst  (S.  auch  vAbleit).  i)im  gAw.:  '/,/m 'dtrndyai  (sd.) . .  räyS  asts  vanfOui  galm (sd.)  manauhs  Y.  43-  •  "'j  —  .y?"»  i^am (sd.)  data  .  ,  ahurö  °sahyä  iizäyäi  (sd.) pmdim  Y.^i.ij;  —  käds..ysi  uxifinn (sd.)  asnqm  a»!iSu^  dar^%rai  (sd.)  frS •iahyä  /rar  iitzY.46.y,  —  ya  ^aohana.. awuntStim  "hmcä  *iaibys  dänAä  (sd.) natda  xsa>r»nca  Aaurvalät3  Y.S4- läis  yüs  g/ae^ORäis  'um  xsmmbyä  dadi^l (sd.)  Y.46.  is'J>;  —  ktßarä  yas5  (sd.) hyin  'liin  Y.  5/.  4.  2)  im  jAwr.:  tßit
6768:raütica  1 .  .  urvaiainarS  . .  tümc'a  ys  zara-  r*"^"t1'  1'  Ta    *'w''/v'"'""'  ^°- '  ^""l!
6863:'rahe    mazda    Yti^.pf.;   —   yazus  .'r5  mazdäY.22.9>;  —  eil  hau  a pu^rö  'rö  (statt  Gen.?)  mazdä  F. 4%;  —  lyJ  . .  /  äat  mraot  (Stverz,,  unter  I  i )  'rd ätars  (Stverz.)  'rahe  mazda  puira  Y.6$}mazdä  "Y.g.^it;    usw.;    ö.  44,  7.78,  Yt 1 2;  7.2 ;  usw.; — ätari  (Stverz.)  mazdä  'rahe]8.5J;  — pfrpsat  (Stvetz.,  unter  i  a),  zara-
7741:•  j.  9r«zvo  Adv."  'wahrlich,  fürwahr'; 1)  an  der  Spitze  des  Satzteils,  vor  Vok.: fr°  asäum  spitama  ^7vam  da^at  ahurB maidä  Yt.  5.  89;  91,  95,  12.3,  13.  i,  Ij. 31.  2)  hinter  dem  Wort,  das  hervor- gehoben werden  soll;  a)  hinter  dem  Pron. pers.:  yat  tum  hs  uzsayatjha  tum  3r° zarahultra  Y.g.13;  —  aez'alia  bä  zara- 'i^ustra  ya>a  tum  jf  vasanhe  V.5. 17; z\;  —  paiti  »lam  if  ptnsat^uha  yim ahursm  mazäam  V. /^.  7,  b)  sonst: mazilt»n  ..vispanqm  tr"  sravaahamYi^N. 4.1;  —  daliiqm  »r'  yaozdaii-Xta  a^a  zX. . asti  yaozdäili^  .  .  havaya  ir'  dasnaya  V. la.  1 9.
10318:•  j.  gäSS-  f.  'Lied'  uzw.  religiösen  Inhalts; 1)  insbes.  von  den  fünf  Hymnen,  bez. Hymnensammtungen,  die  in  Y.  28—34, 43—51,  59  erhalten  sind*':  sraobm  .  .  y5 paoiryd  "^.J  frasrävayatya panca  . .  zara- iu/traAe  *a/smaimvan  (sd.)  vacastastivaf malMzaintls  mal.paiti./rasä  Y.57,8;  7/. 6, G.  7.6;  —  akunavaitlm  (Stverz.)  °'i:qm aiaonlm  .  .  mai.afsmanam  mat.vaüäslallim map.äzaintim  matpjnsvlm  mat.paiti.p?r>s- Vlm  map  varfiibyjca  *pa^?byasca  kufra- mtrttqm  . .  küfrayaslqm  . .  Vr.  14.  o  f.;  usw.; — ahunafalca{^A.)  'Lariam  ^.46;  —  uita- vaitya  (Stverz.)  '"^aya  handatä  ya^amaide . .  haitiPca  afsmans^a  vacasca  vacaslal- llmca  /rasraa'knmca  ..'Vj.iS.y,  usw.;  — sp)ni:1.mainyBm  (Stverz.)  '"^qm  asaonzm  . . Vüiuxsa'irqm  (Stverz.)  '^qm  ..vaAisISistim (Stverz.)  'iqm\x.2.Zl;m-»i.  2)Bezeich- nung  für  alle  (anscheinend)**'  im  Gä^ä- dialekt  verfassten  Stücke  des  Awesta,  d.  s.  — ausser  den  eigentlichen  0<i>äs  —  AtxYHapt. und  die  vier  heiligen  Gebete  (V.  27. 13— 15, 54.  i  )'*'>;  nur  Plur-,  womit  entweder  die Gesammtheit  dieser  Li  tteratur  oder  einzelne Abschnitte  daraus  gemeint  sind  (s.  auch  A): imäsf  tg  haoma  °^ii  imä  h^nti  staomsyS'^. /0. 18;  — farS  amisä  sp>nta  ''ka  gJurvJin Y.2S.0;  —  tipma  vi  0(7  dcflö«/"/ Y.2(V.o, 430,  47-o,5io,S3°''  —  '"i'^byS  spintäbyd ratuxsa^räbyS  (Stverz.)  alaonibyö  Y.55.  i ; usw.;  —  tä  713  hmti  °äi7  har^'iravaitista
10914:•  g.  *xkn3iV'  i)  Adj.  'Genüge  leistend,! zufriedea  stellend',  mit  Akk. :  yS  ,  ,  zara- ' "iiultnm  rääarfhä  . .  'näuiiüS.)  Y.4Ö'.  13;
11194:♦)  Nicht  fünf,  wie  die  übrigen  Länder;  es hat  keinen  besonderen  raiui  däKyumö,  dessen StellDng  Tielmehr  zusammen  mit  der  des  zara- %uJtr3.ümö  in  einer  Person  vereinigt  ist;  zuletzt Marqdakt  EranSahr  uz.
11753:—  tä  xsapanB  yä  *ß'äM  Y.öa.io;  — .  a)  adjektivisch;  a)  im  gAw.:  däidl  .  . ätiti  tä  ^ao^na  .  .  yä  anhus  . .  v»rft- '  tarn  aslm  vaahsus  äyaptä  (sd.)  manatgAs yäii  V.J5. 1;  4.41;  —  yat  ta  sravA  drm-  Y.  25.  7.  B)imjAw.:  *us  ^täai  späna jayqri  yä  pagurva  ,  .  'S,  4,  45;  —  ta  fryi  pat»titi  pasus.haurvqmca  . .  V.  /J.  4a;  43; , .  tä  isuds  .  .  ta  rätayo  *yam  (APn.)  —  pqscaUa  ava  ta  aiü  maya  ..  V.g.ii; oAurS  . .  frävavaca  Y.ö^.g; —  tä  daiA-\^2.  a)  mit  relativischem  Anschluss"; MävS  ..  nijayntnte .  .ydhra  /r<Mir!Hnti  ..^  k)  yai  %Pi}K.:  gavöi  aääisizA.)  iäis  ^ao- /mvafayuYtij.^Si  —  yasf  tarn  dahyüm  .'haiiäis  yäis  vahiitäis  Y.J5.4,  b)  im äcaraiti  yaia  {'wo')  huh3r?ts  *baraite  Yt-ijAiw.:  ttm  ratüm  yaxamaide  yim  zara- 10.112;  —  tä  (statt  NPf.)  daiMävS  ti  "ä-usinm  Y.70.IJ  i';  —  i?m  aküm  paik- ^hamtTT^e  yd^a  duzh?nni5  *baraite  mi~  yäite  yim  aiaoiiqm  V. 18.^6;  76,  5.62; ärff  Yt  10.  48;  41.  b)  substantivisch,  —  upa  tarn  ear?lqm  yqm  datvyqm  Yt  /'/. a)  im  gAw.:  «m  (ASm.)  ..  mimaysff  y!  77;  —  tqm  krhrffm  yqm  iristake  V.$.i; qnm3til(sd.)  mazda  srävl  ahursY.4$.io;  —  täia  vt'hü  yaxamaide  yä  antarpsta  Yt 9;  —  alca  töi  (NPm.)  vaim  hyäma  (Sp.  I3.\^y,~- tä  fravaiay5..aojiita  fuiiti  yä '75  0-)  y^^  ■  ■  ^^fDnaoit  . .  Y.30.  9;  —  paoiryanqm lialsanqm  Yt/J.17,  b)  sub- ai  tSi  at?h>n  saosyaiits  .  .  yH  .  .  htüänti  stantivisch;  A)imgAw.:(i//(i/  msi  daxstfm Y.dS.xi;  —  talcit  . .  ySi  /iisitms  \.  data:  ahyl  ar)ASu£  vTspä  atag^ä  (sd.)  Y. 32. 11;  —  t^ng  tfarayS (sd.)  yöi  vä  daibi-  34.6;  —  tatcä  .  .  'kwaAml  *ä  dqm{sA.) Alt/r  Y.  32.1;  44.11,  13;  —  maf  täis  nipäail:  man5  vofia  urunas^a  ..Y.4g.\o; vispais  yöi  .  .  marintl  Y.43. 14;  —  tal  —  yä  tat  upä.jamyjmä :  tavacä  haxfmä v»myädyäi  kyai  msi  mraota  (sd.)  i-aktstim  ,  asaAyl'ä  Y.  40.  a ; — y.J  tat  upä.jamyämä : 43. 1 1 ;  J/.  5 ;  —  vaida  tat  y''  "Ami  .  .  \  tavatä  sarSm  asafiyä/ä  Y.  4l-  6;  —  ta/a analiS  (sd)  Y.46',2;  —  ta  (APn.)  hwa'  vupä .  .htvaAml ..  xia%r?i  ä  voya'i  ra  (%A.) p^rysä  ..ya  aX  aiil(Sp.  14$  ZD.)  ..Y. 31.  i^l^Y.  34. 10;  —  tat  vJ  nJ  Aasaas Jr^Aj  (sd.)
12424:oAurischta  Religion :  kahmät  paoiryS  mal-  \ yänqm  , ,  frada^ayS  'nqm  ,  .1  . .  yimäi .  .  fradaisalm  °nqm  .  .  äai  hi  mraom  . . vUanha  ml  minlff  b^ntala  (sd)  "nayäi (als  Gen.)  äat  . .  pailyaoxta  yimS  .  .  nSit dato  ahmt  . ,  tnirstl!  b3r?tala  'nayäi  V. 2.1  ff.;  Ytn.  14;  —  vXltäspaht.  .yS  batuUa upastaca  vTsata  .  .  •nayä  Yt  13.  99;  — ya%a  axsm  Asüyene .  .  zara%uänm  anu- matSe  'nayäi  anuxtie  'nay3i  anu.värltSe •nayäi  Yt.  j,  18;  Y.t?.  7;  —  hutaosqm  .  . yä  rrn  °nam . .  zraiia  (sd.)  dät  apica  aotaf Yt  ().26;'Vyt.  Jo(?);  —  ks  .  .  'nam  .  . vJbarat  aitaisva  vanfsva  ySyimö  ktnrtaoi^ .  .  vTs  iarsipia  V.  2. 42 ;  —  satö  .  .  zara- huiirS  .  .  ita  apam  vTjasaiH  .  .  °na  .  . vlspais  avi  karsvqn  Yt  jj.  94; —  mi^nm . .  yahmi  vyane  (sd.)  °nayäi  (als  Gen.) srirayai  p}r>^u.fräkaysi  . .  Yt  10.  64;  — sraoi^m  .  .  yB  damsJisS  *°nayä  Y. 57.23;
12600:'lehren,  unterweisen',  mit  Akk.  der  Per- son: a^J  a^ä  cSii  (sd.)  aAurö  .  .  zara- 'hustnm  ataxsayaaa^^  (Augm.)*^  vJspa^ farasnt^la  Y.  iz.  5.  a)  mit  Inf.  als  Sach- objekt: kyat  mS  . .  daxsat  usyai  (sd.) *titsna.maiiis  vahistä  Y.  43.  r  5.
13326:•  j.  däityä-  f.  Name  eines  Flusses**  in AiryanaVa^ah  (sd.):  tarn  yazata  ..  zatri.- vairil  *pasne  apö  "yayh  Vt5. 112;  g.f), I/.61; — mmS ape  'yayaYti.21.  a)sonst mit  vatiuhi-:  äpS  vanuAli'  .  .  vaahuyh 'yayä  V.  ig.  2;  —  tarn  yazata  .  .  zara- ^uHrS  airyene  valjaki  vauhuyä  °yays  ". .  in dem  arischen  Vaijah  der  guten  D"  Yt 5.104;  17, /5-«.  V./.z,  2.20'.
14890:yaoiädhd  dakmayStparS  ä/ritstt.,  dairihu. paitlm yaozdd^ö  ustraAe'ti  arsnSV.Q.^T'^; 37  f.*.  a)  bes.  beim  V._>'a«-:  vanani^m .  .  yazamaide  amaheca  °ii  kuiastahe  Yt. Ä  I2J  12',  U- 133-135 '^  JJi;  —  yaf^a- maide  ^a/am  malfi^anahe  (sA)  °//*'  .  . drvaßaoi  Y.  7Ö'.  10;  —  ft«  yazata  . .  zara- %uitrS  v^fhraynaAe  'ti  manahi  Yt/^^aS; 78';  —  yqm  yasata  zard^uilrS  .  .  ava- he^a  'ti  yqnahe  yat  hi  da^a/  .  .  Yt.  16, 6f.  b)  aSahe  paiti  (Sp.  14  m.,  u.)  '(als
17233:•  j.  be  Part  zur  Hervorhebung  des  ersten Worts  im  Satz:  zätS  b'  yS  asava  zara- ^u/irS  V.  ig.  46.
17821:yemi  , ,  imat  am>ia  spptita  .  .  imat  asäu- nqm  varguAls  °iays  (VP.)  Wjra  aiiuihüra Y.  65. 1 2 ;  Ny.  /.  I ;  —  aora  varmkis  upa.- sa^a  .  .  äps  .  .  urvarä  .  .  tüäunqm  fra- vasays  Yt  13. 147;  1. 9,  10. 100,  H.  34,  y, 79,  FrW. /.  3;  —  jamyqn  i^ra  asäunqm .  ,  'iaylf  asöis  basfaza  hacimnä  . .  istSe *vadhar»Aqm  paitiHätSe  ätaranqm  Y.  60. 4;  —  qpqmea  .  .  urvaranqmca  .  ,  asao- nqmla  'hnqm  yasnsm  Vr. 21.  \;  —  yS nä  his  hubinta  *barat  jva  a?aonqtn *says  (als  AP.)  sästa  .  .  hö  anhaiti  za- sulttmS  Yt  /J.  1 8 ;  —  fravasayS  .  .  yä a/raourvisvat  k?r»navainti  irsm  yahmya jaanti  Yt.  y.  26;  —  -says  . .  ya  ahurahe xsayats  dasinqm  upa  yü&yänti  yezi  aim bavaiti  ^alavaxsnuiW.  13. 63  ;  — frasüSTnii uyrä  asäunqm  'fayS  paoirij'  pouru^sata .  .  pouruAatanra  .  .  pouruiasvanS  apitii ashntnä  haväi  käcil  näfäi  . .  tä  yü^yeinti pfianähu  have  asahi  Yt  l^.  65if.;  —  "sayS .  .ya  avai  trayS  aiwyaxsayänti  yat  vouru- kahm  ..yä  ave  strjui  atwyäxsayeinti yqm ^haptöiringS  ..ya  avqm  k^hrpim  aiwyäxsa- yänti  yqm  .  .  hnsäspahe  .  .  ya  avqm *x^rqm  (sd)  aiwyäxSayänti  yqm . .  tara- 'huStrahe  navaca  navaitlsla  navaca  sota nava^a  hatattra  navasSs^a  baevqn  Yt  13. 59—62;  —  "iayS  .  .  yä  vts^&a  ävayänli hamaspa>:maedaim  paiti  ratüm  äat  a^ra vtcar?nii  dasa  pairi  xsa/nö  Yt/J.  49;  — asSunqmcä  'HbyS  yä  nS  iltä  urvSibys  Y. 5Ö.  2 ;  —  asäunqm  '/is  narqmcä  näiri- nqmcä  yazamaidl  Y.^7. 3;  —  °fayS  yä paeirya  (sd.)  anhan  Y.  23.  \;  —  äyeseyesti "vTspaya  asavane  'se"  Y,  2_j.  3;  —  vTspä °iayS  (als  AP.)  asäunqm  yazamaide  ädah- *yunqmca ..  'say5 ..*u%dahyunqmla . .  °iayS.. narqmca  ..'^ayD  ..näirinqmfa  ..  °sayS  yaza- maide  Vr.l6.  2;  7.  i,  10.2,  16.  i;  —  nabä- nazdiäanqm  para.iristanqm  aliirapaitinqm a!>iryanqm  narqm..näirinqm  'iayff  yaza- maide  Y.  26.  T,  8  ff.";  —  a/äunam  "sayd .  .  nmänyä  visya  zantumä  däAyumä  zara- ^ustrSJpmä  Y.  ly.  18;  —  airyanqm'  .  . /ßityanqm'  .  .  sairimanqm'  .  .  säininqm' . .  dahfnqm' . .  vTspanqm'  dakyunqm  narqm .  .  näirinqm  .  .  °sayö"  yasamaide  Yt  13. 143—145;  —  fä  'sayU  .  .  aoßstA  hittti  .  . ya  paoiryanqm  tkaihnam  ya  vä  narqm azätanqm  /rais.car>^rqM  saoiyantqm  Yt. y.i7;'Y./.i8',  23.2,  24.5;  —'  vjipä .  .  'Iay3  .  .  yä    haca   gayät    mariihnai   ä
17835:•  j.  fra-väka-  n,  i)  'Anrede,  Rede',  im Gegensatz  ZMpäitivaka- :  tPtn  yazata  . .  zara- 5wj?r?  . .  v?r»%ra-]nake  paiti  °ke . .  päifi- väit  Yt  14-  28.  i)  'Ausspruch,  Ver- kündigung;  Offenbarung' i^-fa^MÄ»  „alvahmi paiti  vacö  vTspanam  vohunqm  .  .  'k?m "cui  (est)  .  .  unam  per  vocem  omnium bonorum  .  .  proQuntiatio?"  H.  j.  1";  — mazdä  frsmraot . .  cvas  (sd.)  frsmraoi  'kim Y,  7p.  20'';  —  vTspjm  vacö  'k^m  haurum vacö  ahurahe  mazda  "der  gesammte  Spruch ist  eine  Offenbarung,  der  ganze  Spruch  (eine Offenbarung)  des^^J/."Y.75. 14.  Aa)DS. und  b)  LS.  als  Inf.  'edicere,  proountiare'; a)°iäi:  usi  ahurahe  mazdä yazamaide dar»- &rJi(sd.)  ..xratüm..  marn^räi  ..  hizi'qm.. •käi  mtfhrahf  spmtahe  Yt/.  28;  — yasnahe haptanhätSis  .  ,  yH  fravaoce  .  .  facqmca värfhrtrjninqm  °kaiyi.i$.%.  b)  'kas-ca-. yasnahe  haptanhaisii'  °haila  paitySstayalüa *masdataeca..  Vr.i5. 2.  3)  'Preis,  Ruhm': ahm/li . .  'häi  ula  ^framainyai  (sd.)  Yl  16. 3,
17882:m\Xä  i)dnwS.  la:  ä  dim  pimat  zara- %uärs:  kö  .J  Y.p.ijNik./.  i)Med. dnwS.  7:  kP  vS  asa  a^raiVj  "wer  wird  sich von  A.  beraten  lassen?"  ¥.57,11.
```


## [2026-09-05T21:06:49.059Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== IEC ghreu ===\"; grep -n \"ghrēu\\|ghreu-\\|ghrēi\\|ghrei-\" IEC.txt | head -20; echo \"=== SYN great/desire ===\"; grep -n \"grauta\\|gréat\\|ghreu\" SYN.txt | head -10"
}
```


### [2026-09-05T21:06:49.147Z] TOOL RESULT

```
=== IEC ghreu ===
4301:Tokh. B cf. krámp- (“be restrained" or sim.); NAIb. grémbc, grémg, m. (hook; anchor, fr. *grembhitio-); Ir. greim, pl. greammanna ‘grip, bite’; W grem ‘gnashing’; MHG krimme ‘cramp in bowels’; G cf. Krimmer ‘hawk’? greng- (greng-) (1) ‘plunge’. Cf. grengh- & grenĝos OE crincan ‘fall, succumb, die’; Cz. hřízit ‘immerse’ beside o-gde hroužit, hrouzit, id.; — se ‘sink’ (ambig. cf. grengho (3)) greng- (2) (?) “twist, knot OE crinc “buskin?; Du. cf. krinkel “twist, bend’; E crinkle; Blg. grež ‘knot in wood grenĝos, å, is “dirt, stain’ LG krink, id.; OCS ere, greza ‘mud’; R grjazi ‘mud, dirt’; Cz. cf. vy-hfez ‘excremenť gren£holos, io ‘round object’. See grongholos and next MHG kringel (circle; pretse; ON kringla “disk, circle, orb’; Li. grezule *wagon-pole'. (Variant in Latv. grizulis ‘eddy’, fr. *gringh-) gren£he, ið (1) ‘turn’ ON kringja ‘encircle’; Sw. cf. kring, prp. ‘round’; Li. greZiu, ti, v. “bore; return’, tr.; Latv. cf. gredzens “ring? (?) grengho, ið (2) “press, squeeze’ Fris. kringe, id.; Cz. cf. vy-hfeznout 'cram out (ambig. cf. greng-) Li. greZiu, ti (2) ‘wring’ greného, ið (3) ‘sink, fall’. Cf. greng- (greng-) OE cringan “fall in battle; yield”; cring, m. ‘downfall’; OCS greZo, grezëti ‘plunge, sink’, cf. Pol. gražyć (:OCS groZo, iti; Cz. hroužit, id. and tr. ‘immerse’ from an o-gde root *erongh-); Cz. hiíZit *immerse'; — se ‘sink’; R cf. grjaznut' (‘sink into mire’, influenced by grjazi, see grengos) (Note: Cz. variant hrouzit: hrouZit. A parallel root occurs in Li. gle£ztu, glezti («droop', fr. *gleng-, gleg-) grésó, ið (ghrés-?) *provoke, threaten'. (The evidence is ambig.) Mir gresim ‘urge’; Ir. greisim, greasaim, grío- saim ‘incite’; Li. gresiü, gresti ‘threaten’ greuó, ið “strike, hit, meet, find'. (Li. & Latv. ambig. Cf. ghreu-) Lesb. agréo, Thess. aggréo “take, seize, catch”, cf. agreutós, adj. (/caught', etc.); Lat. gruo, Gre ‘find’; con-gruo ‘meet’; in-gruo, Gre "at,
4311:tack’; LLat. cf. in-gruus ‘threatening’; Du. krieuwen (2) ‘bicker’; Li. (ambig.) griauju, ti (overthrow; thunder. Cf. ghreu-); Latv. grauju, t (destroy; fling; rage; thunder’. See ghreu-)
4881:ghrauos (ghrēuos) ‘dun, grey’. WP I, 602. For vocalism cf. bhlàuos Lat. ravus (1) ‘dun’; OHG grao, ON grár ‘grey’; OE cf. græg, id. fr. *ghreuio-. (The vocalism is that of Lat. flavus: OHG blao). Cf. also perb. Slovene gruj (émuraena' = “gray- ling'?). (Variant: ON grjár 'grey")
4930:ghreun- (ghreuən, ghreusn-) ‘grit, gravel, groats’ Br. gruan ‘gravel’; W graian, (d: MHG grien, G Grien, id.; ON grjon, npl. ‘groats’; OE cf. greosn 'gravel' (Olr. grian 'gravel fr. *ghrei-)
4939:ghriuos ‘dun, grey’. Cf. ghrauos (ghreu-) Alb. grivé (*dun, dull, fawn’. LW?); Bulg. griv *blue-grey'; Fr. Cat. Sard. grive, griva (thrush', lit. as E dunlin 'sandlark, a grey bird)
=== SYN great/desire ===
22447:_ in number; Toch. this Pe ‘great in number". ma Wee *meé-, ‘vs 3 Falk-Torp 714. “NIr. mor, W. mawr (Br. grand, etc.’) : Grk. ‘great in spear- OHG mari, etc. BY wavig -mérti in Vladi-mérit, 10 mau, mo(u), W. mwy; I ‘more’, maists ‘sreatest’, mara, mest ‘greater, reatest’ (in siZe, quantity, or number; VB more, most not used of size). "4 Lat grandis (> It., Sp. grande, Fr. grand), esp. ‘great (morally and physical- iy) and often also ‘full-grown’, etym. dub, but perh. (as ‘swollen’?) : Grk. pots ‘pride’, ChSl. gradi ‘breast’, etc. Walde-P. 1.699. Ernout-M. 481 f. Walde-H. 1.617 f. It. grosso, Fr. gros ‘thick, coarse’ (12.63), but also ‘stout’ and ‘big’. Rum. mare, fr. Lat. mas, maris ‘male’ (m designating the male animal of a spe- ces and consequently the larger). Pus- canu 1027, Tiktin 952. 4. Ir, mar, mér, W. mawr, above, 2. a brass, Br. Corn. bras (W. bras shi Son ), prob. : Lat. grossus Welder a (12.63). Walde-P. 1.698. tea u : Stokes 183. il, tia | as prefix oll- (cf. also lire "be arise us, a Prob: : Lat. pol- ton of ae ete., with primary no- Nut, 795, g Walde-P. 2.102. Er- » Stokes 52 f. Dan., Sw. stor (late OE ), ef. OF ris. star id., OS ae starti ‘old’, Lith. Tithsemant?, Le root. *sta- ‘stand’ fsty to hig velopment fr. ‘standing Pt et Welder. ~ gréat e mostly ‘coarse, stout,
```


## [2026-09-05T21:06:54.952Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Streben\" BRT.txt | head -10"
}
```


### [2026-09-05T21:06:54.995Z] TOOL RESULT

```
6399:'-.-J.  Adj.  'findend'.  lum  V.  'vaFd;  ü.  -vid- ; •  j-  aSö.iä-  Adj.  'das  Asa  suchend,  nach Adj,;  oder  'treffend',  lum  ai.  V.  vidkyati,  ai.  1  dem  A.  Strebend"*:  paili.ajq'ir»m  a^au- -.u'*-  Adj.  ruriqm   .  .   ySi    *iyeyqm    äOrät    'Tsd    (AP.)
7549:•  g.  Eiav-  DO.  'Streben,  Eifer',  spez.  in Glaubetissachen :  yavat  'his*zrazdUtS  banöi haxtaya  (sd.)  "sofern  der  gläubigste  Eifer (euch)  in  Fleisch  und  Blut  (sitzt)"  Y.55.7.
8075:tayö  (sd.)  Y-^Äa.       a)  'Ziel  des  Strebens'  •  j.  ujra-,  g.  ugra-  Adj.  (fem.  °r.7-)  'stark,
8737:setzen  wäre,  ein  höchst  fragwürdiges  Gebilde. —  Pä.!  fraif  uiih'),  erl.!  dättäi  usih;  Sü,; Pflhulacaitanyam,  vipiilacailaiiyam.  —  i)  Deu- lungsveisuche,  alle  verfehlt,  bei  Gdn.  KZ.  zS. 164  ('Bemühung,  Streben,  Eifei'),  Bn.  Stud.  r. 464  {'Veistand'),  Dsr.  ZA.  /.  342,  153  ('in- tetligence',1,  Mills  G.  486, 503  ('wide  enlighte- ment,  wide  apprehension',  danach  Kanqa Dict.  'Wide  mental  light').  —  '»  Weil  n us—\-um-  letiegte,  nach  Mills  'a  descriptive compositum  with  the  adjective  last',  was  ihm möglich  erscheint.
19770:•  j.,  g.  "manah-  n.  'der  innere  Sinn,  Geist" als  Sitz  des  Denkens,  Erkennens  und Wollens;  'Sinn,  Geist;  Denken,  Gedanke; Streben,  Begierde;  Plan,  Anschlag';  I)  im gAw.:  at  %wa  mSr^hs  .  .  'noTgAä  Y. 31. 8  '>;  —  iaya  (Sp.  462  m.) . ,  ava  'nanha ya  .  .  manta  vastryS  Y._JJ.  6'';  —  n^ra i  Audätihg  ya%ana  vagdfmnai  (sd.)  'nanha V.31.32;  —  Ayat  Aahra  (sd.)  °nä  bavat ya'iira  listi/  atahai  maiha  Y.J0.9;  — yS  dat  °nS  vahyS  .  .  a^a4?A,)ca  hv5  daf- nqm  iyaohanaH'a  vai'anha^  Y.4^.4(3.  a);
22533:Zu  'vaahav-;  %  153.  3.  —  Pü.:/n  ahräklh  i vih,  Sü. :  punyäjia  ultamäj/a,  NpQ. :  iaräy  i lazhi.  —  «)  Wegen  der  Asyndese  verweise ich  auf  al  iäm  yih  {woneben  iäm  ca  yii  ca) und  Dwt.  AiS.  75-  —  ')  Ander»  Gdk.  SPreuss AW.  ig.  ^6  *au»  dem  löblichen  Streben  nach Rechtschaffeiiheit';  aber  aiayä-  f.  bedeutet sonst  etwas  anderes.
27784:•  g.  zara-  m.  'Streben,  Ziel' :  ka%ä  mazda °nm  carani  haca  ximat  *ashitlm  (sd.) x^ntäkqm  "ob  ich  wohl,  o  M.,  durch  euch mein    Ziel     durchsetzen     werde    .  ."    Y.
```


## [2026-09-05T21:06:57.211Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"ghrēi\\|ghrei-\\|khriein\\|chrisma\" IEC.txt | head -10; echo \"=== SKT ===\"; for w in \"^cream\\b\" \"^chrism\" \"^character\" \"^great \" \"^gravel\" \"^greedy\" \"^yearn\" \"^exhort\"; do echo \"## $w\"; grep -n \"$w\" SKT.txt | head -2; done"
}
```


### [2026-09-05T21:07:00.042Z] TOOL RESULT

```
4930:ghreun- (ghreuən, ghreusn-) ‘grit, gravel, groats’ Br. gruan ‘gravel’; W graian, (d: MHG grien, G Grien, id.; ON grjon, npl. ‘groats’; OE cf. greosn 'gravel' (Olr. grian 'gravel fr. *ghrei-)
=== SKT ===
## ^cream
## ^chrism
## ^character
## ^great 
## ^gravel
## ^greedy
## ^yearn
## ^exhort
```


## [2026-09-05T21:08:15.738Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && head -c 600 SKT.txt; echo; echo \"=== grep ===\"; grep -n -i \"cresme\" SKT.txt | head -3; grep -n -i \"CREAM\" SKT.txt | head -3"
}
```


### [2026-09-05T21:08:15.797Z] TOOL RESULT

```
This  is  a  digital  copy  of  a  book  that  was  preserved  for  generations  on  library  shelves  before  it  was  carefully  scanned  by  Google  as  part  of  a  project to  make  the  world's  books  discoverable  online.
It  has  survived  long  enough  for  the  copyright  to  expire  and  the  book  to  enter  the  public  domain.  A  public  domain  book  is  one  that  was  never  subject to  copyright  or  whose  legal  copyright  term  has  expired.  Whether  a  book  is  in  the  public  domain  may  vary  country  to  country.  Public  domain  books are  our  gateways  to  the
=== grep ===
1119:Auction-  (L.)  L.  auciifffifm,  ace.  of auctio,  a  sale  by  auction,  lit.  •  an  increase/ because  the  sale  is  to  the  highest  bidder.— L.  au£tus,  pp.  of  augert,  to  IncreaM.  See Ske.
4316:Cream,  t  F.  —  L.)  O.  F.  <resmt  {erf me) ; Low  L.  erema.^h„  ertmor,  thick  broth» ihick  juice  from  soaked  com.
9598:Jttnlcet,  a  kind  of  sweetmeat.  (Ilal.  • L.)    Orig.  a  kind  of  aeanjchccse,  served up    on     rushes,    whence    its    oame.     I  till. gwtua/a,  a  kind  of  cream-cheese  on  rushes, also  a  junket    (Florio).  —  ItaJ.  gitmcc.   a rush.*>ll.  imtcum,  ace,  oi  iuncus,  a  nuh. Junta,  Junto :  see  Join. Juridical ;  see  Jury. Juriadiotlon,  Jurist ;  see  Jury. Jury,  a  body  of  sworn   men.   (F.  — L.) F.Jur/t,  a  jury,  a  company  of  sworn  men; orig.  the  fem.  pp.  of  jitrer,  to  swear.  — L, I'urarf,    to   swear,    bind    by   an     oath.  4* Ski.  rw.io  bind.     (VVU.)
```


## [2026-09-05T21:08:29.536Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== LKT rusma/chrisma ==\"; grep -n -i \"rusma\\|chrisma\\|khorozma\" LKT.txt | head -5; echo \"== WLD Bd1 gher reiben ==\"; grep -n \"ghrēi\\|ghrei\\|ghreu\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -8; echo \"== FSD character/charisma ==\"; grep -n -i \"kharax\\|charax\" FSD_vol1.txt | head -3"
}
```


### [2026-09-05T21:08:29.609Z] TOOL RESULT

```
== LKT rusma/chrisma ==
== WLD Bd1 gher reiben ==
30237:388 als Anlautdublette neben *ghreu- „fallen“ (lit. griuti usw.) betrachtet. 
37499:146 zu *ghreu-bh- „reiben"). 
38084:2. gher- „hart woriiber streichen, reiben“; vgl. auch die Erw. ghrei-, ghreu-, 
38089:gnldas , lett. grands „Korn“ < ghreii-d-; Gdf. *ghen-ghro- diss. aus *ghor- 
38090:ghro- Persson Wzerw. 73, und *glm-ghru-\ letzteres naher zur Wzf . ghreu-l 
38481:Wzvariante ghrei-dh- neben gher-(e)s- betrachten; davon ist nur die Be- 
38483:Persson Wzerw. 103, Scheftelowitz IF. 33, 162 stellen xg7ftfj zu *ghrei- 
40375:sind, s. u. ghreu ghreud- „reiben‘ ) fiir „stolz“ von einer Gdbed. „sich wo- 
== FSD character/charisma ==
62842:Char"a-cln'l-da}#  1   kar'o-sln'i-dl;  2   cfir'a-cIn'1-dS,  n.  pi.  Ich. A   family  of  plectospondylous  fishes,  especially  those  with brain-case  not  produced  between  orbits,  cyprlnlform  body and  fins,  and  generally  toothed  laws:  Including  many South-Amerlcan  and  African  species.  Cha-rac'l-nus,  n. (t.  g.)  ( <   Gr.  charax,  sea-fish,  <   charassd,  sharpen.]  Cha- rac'l-daot;  Cha-rac"l-nol'dreJ;  Cha-rac"l-nol'de-lt.
```


## [2026-09-05T21:08:31.226Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '93068,93074p' MON_part2.txt; echo \"=== ARY کروم/کریسمس ===\"; grep -n \"کروم\\|کریسم\" incoming/ARY/ARY_pages.txt | head -5; echo \"=== HRN/HUB kerem ==\"; grep -n -i \"krem\\|kerem\" HRN.txt HUB.txt | head -5"
}
```


### [2026-09-05T21:08:31.318Z] TOOL RESULT

```
کرماتین دارد که رنگ‌های قلیایی را جذب 
می‌کند این رشته‌های کرماتین در موفع تقسیم 
غیر مستقیم بصورت رشته‌های کو تاه موسوم 
به کروموزوم درمی آیند» در داخل هسته 
یک يا دو دانة کوچکث موسوم به نو کلثول 
(هستک) وجود دارد و بعلاوه غشایی از 
خسارج هسته را فرا گرفته است که مانع 
=== ARY کروم/کریسمس ===
=== HRN/HUB kerem ==
HUB.txt:3072:850. Die Bedeutung von zd. kerema- ist ganz unsicher.
HRN.txt:7413:aw. kerema- 'Wurm'; phlv. karm; ai. kfini- (krinn-)
HRN.txt:8211:gütha- Exkremente*; arm. ku 'Mist' (H. No. 149); ksL
HRN.txt:8213:kurd. gü 'Exkremente'; afy. yul; bei. n. gtd^ (436);
```


## [2026-09-05T21:08:45.973Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && grep -n -i \"ghat (n\\|Sanskrit\\|Hindi\" 865d7530e3559878.txt | head -10; echo \"=== yearn ===\"; grep -n -i \"yearn (v\\|Proto-Germanic\\|PIE root\" 4fa6e2b6b73da474.txt | head -6; echo \"=== exhort ===\"; grep -n -i \"exhort (v\\|hortari\\|PIE root\" 0ae49def8c67c42a.txt | head -6"
}
```


### [2026-09-05T21:08:46.036Z] TOOL RESULT

```
56: ghat (n.) 
58: also ghaut , from Hindi, "a pass of descent from a mountain," hence also "mountain range, chain of hills," also "stairway leading up from a river" (to a shrine, temple, etc.), from Sanskrit ghattah "landing place," of unknown origin.
74: 11c., from Old English ginȝifer, ginȝiber, from Late Latin gingiber, from Latin zingiberi, from Greek zingiberis, from Prakrit (Middle Indic) singabera, from Sanskrit srngaveram, from srngam "horn" + vera- "body," so called from the shape of its root. But this may be Sanskrit fol
=== yearn ===
23: yearn (v.) 
25: Middle English yernen , "long for, feel strong desire for," from Old English giernan (West Saxon), geornan (Mercian), giorna (Northumbrian) "strive, be eager, desire, seek for, beg, demand," from Proto-Germanic *gernjan , from PIE root *gher- (2) "to like, want." Related: Yearned ; yearning .
33: "feeling of one who yearns, wishing, longing; desire, covetousness," Middle English yerning , from Old English gierning , verbal noun from yearn (v.). Related: Yearnings; yearningly . Yearnful is Old English geornfull .
53: Middle English aken, from Old English acan "suffer continued pain," from Proto-Germanic *akanan, which is perhaps from a PIE root *ag-es- "fault, guilt," with apparent cognates in Sanskrit and Greek, which itself is perhaps imitative of groaning. Originally the verb was pronounce
61: early 14c., "fail in strength, exhibit signs of approaching death," from languiss-, present participle stem of Old French languir "be listless, pine, grieve, fall ill" (12c.), from Vulgar Latin *languire, from Latin languere "be weak or faint" (from PIE root *sleg- "be slack, be 
69: late 15c., residen, "to remain at a place," from Old French resider (15c.) and directly from Latin residere "sit down, settle; remain behind, rest, linger; be left," from re- "back, again" (see re-) + sedere "to sit" (from PIE root *sed- (1) "to sit"). The meaning "to dwell perma
=== exhort ===
23: exhort (v.) 
25: c. 1400, exhorten , "to exhort, encourage," from Old French exhorer (13c.) and directly from Latin exhortari "to exhort, encourage, stimulate," from ex , here probably "thoroughly" (see ex- ) + hortari "encourage, urge" (from PIE root *gher- (2) "to like, want"). Related: Exhorted ; exhorting .
32: "of or pertaining to exhortation, tending incite by means of argument, appeal, or admonition," early 15c., exhortatori , from Late Latin exhortatorius , from Latin exhortari "to encourage, stimulate" (see exhort ).
52: It might also be the source of: Sanskrit haryati "finds pleasure, likes," harsate "is aroused;" Avestan zara "effort, aim;" Greek khresthai "to lack, want; use, make use of," kharis "grace, favor," khairein "to rejoice, delight in;" Latin hortari "exhort, encourage, urge, incite, instigate;" Russian zhariti "awake desire, charm;" Old English giernan "to strive, desire, yearn;" Gothic gairnei "desire."
60: 1550s, from Latin urgere "to press hard, push forward, force, drive, compel, stimulate," perhaps [de Vaan] from a PIE root *urgh- "to tie, bind" (source also of Lithuanian veržti "tie, fasten, squeeze," vargas "need, distress," vergas "slave;" Old Church Slavonic vragu "enemy;" G
68: c. 1200, "the face, countenance," especially as expressing emotion, from Anglo-French chere "the face," Old French chiere "face, countenance, look, expression," from Late Latin cara "face" (source also of Spanish cara), possibly from Greek kara "head" (from PIE root *ker- (1) "ho
```


## [2026-09-05T21:08:48.142Z] TOOL CALL #42: Bash

```json
{
 "command": "python3 tools/fetch_source.py \"https://www.nisanyansozluk.com/kelime/rusma\" --note \"page 189: Turkish rusma/hurusma < Greek khrisma, Nourai's 'xorozma' node\" && python3 -c \"\nimport sys;print(open('/home/sfmqrb/git/rishe/data/verification/sources/web/'+__import__('hashlib').sha1(b'https://www.nisanyansozluk.com/kelime/rusma').hexdigest()[:16]+'.txt',encoding='utf-8').read()[:1500])\""
}
```


### [2026-09-05T21:09:10.708Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/f538e614d6d46aa1.txt
URL: https://www.nisanyansozluk.com/kelime/rusma
FETCHED: 2026-09-05T21:09:10Z
STATUS: 200
TITLE: Kelime bulunamadı - Nişanyan Sözlük

Kelime bulunamadı - Nişanyan Sözlük 

 Nişanyan Sözlük 

 ç ğ ı ö ş ü 
 ileri arama

 Bu sözlük nedir? Kullanım Şartları ·
 Gizlilik Politikası 

 © Sevan Nişanyan 2002-2026
 Alıntılarda kaynak gösterilmesi rica olunur.
```


## [2026-09-05T21:09:25.018Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && grep -n -i \"chromosome\" 108342db65c49352.txt | head -5; echo \"=== christmas ===\"; grep -n -i \"Christmas (n\\|Cristes\\|maesse\" 9612a31fc0af6b58.txt | head -5; echo \"=== KLN chromosome/character/charisma 1971 ===\"; sed -n '46505p;44043p;102310p' /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1971.txt | cut -c1-700"
}
```


### [2026-09-05T21:09:25.106Z] TOOL RESULT

```
125: chromosome 
=== christmas ===
23: Christmas (n.) 
25: "Church festival observed annually in memory of the birth of Christ," late Old English Cristes mæsse , from Christ (and retaining the original vowel sound) + mass (n.2).
=== KLN chromosome/character/charisma 1971 ===
character, n. — ME. caracter , caractere, fr. OF. 
chromosome, n., a minute body occurring in de- 
ghat, ghaut, n., a mountain pass; a landing place
```


## [2026-09-05T21:09:28.246Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '46505,46512p;44043,44050p;102310,102316p;105902,105908p;269617,269622p;88066,88070p' KLN_1971.txt | tr -s ' '"
}
```


### [2026-09-05T21:09:28.348Z] TOOL RESULT

```
character, n. — ME. caracter , caractere, fr. OF. 
caractere (F. caractere), fr. L. character, fr. Gk. 
Xapax-nfjp, ‘graying tool, mark engraved, im- 
press, character’, from the stem of xapaacEiv, 
‘to engrave’, which is of Semitic, prob. Hebrew, 
origin. Cp. Heb. hardsh, ‘he engraved, plowed’, 
b drath, ‘he engraved’, Aram, hardth, ‘he plow- 
ed’, Ugar. hrs, ‘to plow’. Arab, hdratha, Ethiop. 
chromosome, n., a minute body occurring in de- 
finite number in the cells of a given animal 
species (biol.) — Coined by the German ana- 
tomist Wilhelm von Waldeyer-Hartz (1836- 
1921) in 1888 fr. Gk. xp&jxa, ‘color’, and cr&ixa, 
‘body’. See chromo- and -some, combining form 
denoting the body. 

exhort, tr. and intr. v., to advise earnestly. — 
ME. exhorten, fr. L. ex hortarl, ‘to exhort, en- 
courage, stimulate’, fr. 1st ex- and hortarl , ‘to 
incite, encourage, urge’. See bortation and cp. 
words there referred to. 
ghat, ghaut, n., a mountain pass; a landing place 
{India). — Hind, ghat, ft. OI. ghaffab, ‘landing 
place, bathing place’, which is of uncertain 
etymology. 

ghazi, n., among Mohammedans, a warrior 
fighting against infidels. — Arab, ghazi , prop, 
great, adj. — ME. great, gret, greet, grete, fr. 

OE. great, rel. to OS. grot, OFris. grdt, Du. 
groot, OHG., MHG. groj, G. gross, ‘great’. The 
original meaning of these adjectives was prob, 
‘gross-grained, coarse’. Cp. ON. grautr, ‘groats’, 
E. greot, ‘grit, sand, dust, gravel’, and see grit, 
yearn, intr. v. — ME. yernen, fr. OE. geornan, 
giernan, gernan, fr. georn, ‘desirous’, which is 
rel. to OS., OHG. gem, ON. gjarn , ‘desirous’, 
OS. gernean, girnean , ON. girna } OHG. ger on, 
geren, Goth, gairnjan , ‘to desire’, MHG. gem, 
be-gern, G. be-gehren , ‘to desire’, Du. gdarne ,
```


## [2026-09-05T21:10:32.938Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== KLN71 charisma ==\"; grep -n -A5 \"^charisma\" KLN_1971.txt | head -12; echo \"== LAT hortor ==\"; grep -n -i \"hortor\\|hortari\" LAT.txt | head -5; echo \"== LEW hortor ==\"; grep -n \"hortor\" LEW_1910.txt | head -5; echo \"== WLD begehren gher ==\"; grep -n \"gher- „begehren\\|begehren, gern haben\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -5"
}
```


### [2026-09-05T21:10:33.028Z] TOOL RESULT

```
== KLN71 charisma ==
== LAT hortor ==
10760:mortem est minitatus nisi sibi hortorum possessione cessissent. Le
27347:habeS, Sali., Cat.58,1; quod me hortaris ut absoluam, habeo absolutum
27815:se retrouve dans le causatif horior, hortor propreaent "faire vouloir",
28443:horior et hortor (horitor et horto, arch.), -aris, hortatus sum,
28444:hortari: proprement "faire vouloir", d'oi "exhorter, encourager".
== LEW hortor ==
== WLD begehren gher ==
37876:freude blitzend" zu *gher- „begehren, gern haben" (s. d.), aber germ. 
39868:„Hunger“ von ai. gardha-h in der Vokalstellung ab (s. u. gher- „begehren“).
```


## [2026-09-05T21:10:41.488Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"charass\\|kharass\\|charax\\|χαράσσω\\|χάραξ\" POK_full.txt | head -10; echo \"== POK_full gher-2 block ==\"; sed -n '36823,36840p' POK_full.txt"
}
```


### [2026-09-05T21:10:41.567Z] TOOL RESULT

```
== POK_full gher-2 block ==
Root / lemma: gher-2 
Meaning: to scratch, scrape 

Material: Gr. xapaSpa " Erdrift, crevice, gorge, ravine, gulch '; xapaaau), Attic -ttoj "whet, 
sharpen, notch, incise', xapa^. -OKoq "picket, pole, vine-prop, pole, pale, used in fortifying 
the entrenchments of a camp, cutting, slip, esp. of an olive, a seafish, one of the breams, 
Sargus', xapoKinp "engraver, one who mints coins', then "mark engraved, impress, stamp 
on coins and seals, distinctive mark or token impressed (as it were) on a person or thing, 
by which it is known from others, characteristic, character ' (Kretschmer Gl. 20, 254); 

Lithuanian zeriu, zeftT scrape, scratch', zarstyti' scratch often, scrape '. 

References: WP. I 602. 
Page(s): 441 

Root / lemma: gher-Sand ghera-, ghre- 
Meaning: to shine, shimmer
```


## [2026-09-05T21:10:51.080Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==99' POK_02.txt | sed -n 1,40p | cut -c1-400"
}
```


### [2026-09-05T21:10:52.830Z] TOOL RESULT

```
äd  n.  ,Liebe*  ist  aus  lat.  grätum  facere  alicui  und  ähnlichen  Wen- dungen entlehnt  (d  statt  th  nach  grad  ,gradus*).
WP.  I  600  f.,  WH.  I  657  f.
2.  gber-  , kratzen,  ritzen,  scharren*?
Gr.  x^Q^^Q^  , Erdriß,  Erdspalte,  Schlucht*;  x^Q^^^^i  2,tt.  -ttu)  ,spitze, schärfe,  kerbe,  schneide  ein*,  x^Q^^i  -ay,og  ,Pfahl,  Spitzpfahl,  Weinpfahl ; Schnittling  vom  Ölbaum*,  %a^axr?J^  ,Präger*,  dann  , Stempel,  Gepräge, Eigenart*  (Kretschmer  Gl.  20,  254);
lit.  zeriü,  zefti  ,kratzen,  scharren*,  zarstyti  ,oft  kratzen,  scharren*.
WP.  I  602.
3-  gher-  und  ^hero-,  ghre-  ,strahlen,  glänzen,  schimmern'.
Aisl.  grdr  (*ghre-uo-s) y  ags.  grceg  (^ghre-uio-s),  engl,  gray^  afries.  ^re,  as. grüj  gre,  ahd.  gräo  (Gen.  gräwes)  ,grau*;
lit.  ^eriüy  zeriti  ,im  Glänze  strahlen*,  zeruöti  ,glühen,  funkeln',  ablaut. zarijä  f.  ,glühende  Kohle*,  apr.  sari  f.  ,Glut*;
aksl.  zhrjQy  zhräti  ,sehen,  blicken*,  russ.  zretb,  sloven.  Z7'4tij  öech.  zriti, poln.  £rzec  ds.,  aksl.  zorja  , Schein,  Glanz*,  zarja  , Strahl*,  klruss.  zörja  , Stern,
442  ^
Gestirn,  Morgenröte^  russ.  zaM  ,Röte  am  HimmelS  skr.  zora  ,Morgen^ rot',  öech.  zore  ,MorgenröteS  zdre  ,Schein,  Glanz,  Strahl',  poln.  sore^j ,Morgenröte';  sk^\.  pozon  ,-^swoia',  russ.  pozor  , Anblick,  Schande^  nadzr;,. , Aufsicht',  cech.  pozor  , Aufmerksamkeit,  Acht',  ndzor  , Anschauung,  An. sieht';  hierher  auch  aksl.  zrak^  .Anblick,  Form,  Art',  russ.  
über  lat.  grävastelhis  s.  WH.  I  620.
Wurzelerweiterung  ghrei-: Air.  grian  f.  , Sonne'  i^ghrtinä)]
afries.  as.  ahd.  mhd.  gria  ,grau',  nhd.  gi-eis  ,grau,  alt',  wozu  wohl  auch aisl.  griss  ,Ferkel',  aschwed.  gils  ds.,  schwed.  dän.  gris  , Ferkel,  Schwein'.
Wurzelerweiterung  (*^i2ereu-) :  ^Arü-.
In  aisl.  gryiandi  f.  ,Morgenröte',  aschwed.  gry  ,(vom  Tage)  grauen', dän.  gry  ds.,  gry  n.  ,das  Grauen';  hierher  auch  aisl.  grey  n.  , Hündin, Feigling',  greyhundr  ,Windhund',  ags.  griegJmnd  ,Windhund'?
WP.  I  602  f.,   Persson  Beitr.  300  ff.,  Trautmann  366.
4.  gher-  ,greifen,  fassen,  umfassen,  einfassen';  erweitert  gher-dh-  (s.  u
```


## [2026-09-05T21:11:03.247Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== BQT کریسمس/کروم ==\"; grep -c \"کریسمس\" BQT_v1_pages.txt BQT_v2_pages.txt 2>/dev/null; grep -c \"کروم\" BQT_v2_pages.txt 2>/dev/null; echo \"== MON کریسمس/کرم==\"; grep -c \"کریسمس\" MON_part1.txt MON_part2.txt; echo \"== ARY total lines ==\"; grep -c \"کروم\" incoming/ARY/ARY_pages.txt; echo \"== ARY کرم ==\"; grep -n \"کرم \" incoming/ARY/ARY_pages.txt | head -3"
}
```


### [2026-09-05T21:11:03.340Z] TOOL RESULT

```
== BQT کریسمس/کروم ==
BQT_v1_pages.txt:0
BQT_v2_pages.txt:0
3
== MON کریسمس/کرم==
MON_part2.txt:0
MON_part1.txt:0
== ARY total lines ==
0
== ARY کرم ==
```


## [2026-09-05T21:11:17.555Z] AGENT

Now I'll write the verification file.


## [2026-09-05T21:11:19.740Z] TOOL CALL #49: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg189.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/189.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/ | tail -3"
}
```


### [2026-09-05T21:11:19.808Z] TOOL RESULT

```
-rw-rw-r--  1 sfmqrb sfmqrb  78178 Sep  5 10:14 95.png
-rw-rw-r--  1 sfmqrb sfmqrb  72929 Sep  5 10:19 96.png
-rw-rw-r--  1 sfmqrb sfmqrb  65608 Sep  5 10:43 99.png
```


## [2026-09-05T21:18:11.365Z] TOOL CALL #50: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build189.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nE = \"https://www.etymonline.com/word/\"\nW = \"https://en.wiktionary.org/wiki/\"\n\nPOK_ROOT = {\"src\":\"POK\",\"where\":\"pp. 439-440 (POK_02 leaf 95-96)\",\"stance\":\"supports\",\n  \"note\":\"\\\"2. gher- ,hart worüber streichen, reiben'; vgl. auch die Erweiterungen ghrei-, ghreu-, ghrem-, ghren-\\\" — the printed page 439/440 gives exactly the root, gloss and the two extensions Nourai names.\"}\nWLD_ROOT = {\"src\":\"WLD\",\"where\":\"Bd. I p. 605 f. (WLD_Bd1_1930_dli_70244_djvu.txt line 38084)\",\"stance\":\"supports\",\n  \"note\":\"\\\"2. gher- „hart worüber streichen, reiben\\\"; vgl. auch die Erw. ghrei-, ghreu-, ...\\\" — Walde-Pokorny I 605 f. is Pokorny's own source for the entry.\"}\nAHD_ROOT = {\"src\":\"AHD\",\"where\":\"Watkins 1985 s.v. gher-4, ghrēi-, ghrēu-\",\"stance\":\"supports\",\n  \"note\":\"\\\"gher-4. To scrape, scratch. ... See also extensions ghréi- and ghréu-. [Pok. 2. gher- 439.]\\\"; \\\"ghréu-. To rub, grind. Extension of gher-4 ... [Pok. 2. ghréu- 460.]\\\"\"}\n\ndef ent0():\n    nodes = []\n    nodes.append({\n      \"id\":1,\"lang\":\"Sanskrit\",\"words\":\"ghat\",\"verdict\":\"disputed\",\n      \"derivation\":\"Sanskrit घट्ट (ghaṭṭa-) / Hindi ghāṭ means 'landing place, flight of steps down to a river; mountain pass', not 'a place where sins are wiped away, a shrine' — that gloss is Shipley's picturesque paraphrase, taken over by Nourai. Watkins attaches it to *gher- only with an explicit disclaimer (extended *ghers- > zero-grade *ghr̥s-to- 'perhaps (but unlikely)'), and Klein and Etymonline both call the Sanskrit word etymologically unknown; Turner and the Dravidian-substrate literature treat ghaṭṭa as a non-Indo-Aryan word of the same family as ghaṭa 'jar'. The arrow root→Sanskrit is therefore not supportable in modern terms, and the gloss is wrong as well.\",\n      \"derivation_fa\":\"واژهٔ سنسکریت घट्ट (ghaṭṭa) و هندی ghāṭ به معنای «پلکان کنار رود، لنگرگاه، گذرگاه کوهستانی» است، نه «جایگاه شستن گناهان، زیارتگاه»؛ این معنی، تعبیر ادبی شیپلی است که نورایی آن را نقل کرده. واتکینز (AHD) پیوند آن را با ریشهٔ *gʰer- تنها با قید «شاید، ولی بعید» می‌آورد و کلاین و اتیمانلاین ریشهٔ واژه را نامعلوم می‌دانند؛ بسیاری آن را وام‌واژه‌ای از بستر دراویدی می‌شمارند. بنابراین این پیکان و نیز معنی داده‌شده پذیرفتنی نیست.\",\n      \"sources\":[E+\"ghat\"],\n      \"ref_check\":[{\"ref\":\"OEW:120\",\"status\":\"not_checked\",\"note\":\"Shipley, Origins of English Words, is lending-only on archive.org (djvu.txt 401); the gloss 'a place where sins are wiped away' is characteristic of Shipley's discursive style, but the page could not be read.\"}],\n      \"consulted\":[\n        AHD_ROOT | {\"stance\":\"partial\",\"where\":\"Watkins 1985 s.v. gher-4 §2\",\"note\":\"\\\"Extended form *ghers- in suffixed zero-grade form *ghrs-to- perhaps (but unlikely) in Sanskrit ghattah, ghat: GHAT.\\\" — Watkins himself calls the connection unlikely.\"},\n        {\"src\":\"KLN\",\"where\":\"KLN_1971 s.v. ghat, ghaut\",\"stance\":\"contradicts\",\"note\":\"\\\"Hind. ghat, fr. OI. ghaṭṭaḥ, 'landing place, bathing place', which is of uncertain etymology.\\\" — no IE root, and the meaning is 'landing/bathing place'.\"},\n        {\"src\":\"POK\",\"where\":\"pp. 439-441\",\"stance\":\"silent\",\"note\":\"neither 2. gher- (439) nor 2. gher- 'kratzen' (441) lists any Sanskrit ghaṭṭa-.\"}]})\n\n    nodes.append({\n      \"id\":2,\"lang\":\"Greek\",\"words\":\"xriein, khriein; Christ\",\"verdict\":\"confirmed\",\n      \"derivation\":\"Greek χρίω (khríō) 'I anoint, smear, colour', infin. χρίειν, is the classic representative of the ī-extension *gʰrei- of *gʰer- 'to rub': Pokorny 457 heads the entry \\\"ghrei- : ghroi- : ghri- ... Erweiterung von gher- 'reiben'\\\" and cites χρίω 'salbe, streiche an, färbe' together with ON gríma, Engl. grime. The verbal adjective χριστός 'anointed' was chosen by the Septuagint translators (3rd–2nd c. BCE) to render Hebrew māšīaḥ 'anointed one', and in the New Testament Χριστός became the title of Jesus — a purely semantic, not phonetic, step.\",\n      \"derivation_fa\":\"یونانی χρίω (khríō) «می‌مالم، روغن می‌مالم، رنگ می‌زنم» (مصدر χρίειν) نمایندهٔ گسترشِ *gʰrei- از ریشهٔ هندواروپایی *gʰer- «سودن» است؛ پوکورنی در ص ۴۵۷ همین ریشه را با معنی «بر چیزی مالیدن» می‌آورد. صفت مفعولی χριστός «مسح‌شده» در ترجمهٔ سبعینیه برابر عبری māšīaḥ (مسیح) به‌کار رفت و در عهد جدید لقب عیسی شد؛ پس تحول اینجا معنایی است نه آوایی. ادعای نورایی درست است.\",\n      \"sources\":[E+\"chrism\"],\n      \"ref_check\":[{\"ref\":\"OEW:120\",\"status\":\"not_checked\",\"note\":\"Shipley lending-only; the same chain is however standard in Pokorny 457 and AHD.\"}],\n      \"consulted\":[\n        {\"src\":\"POK\",\"where\":\"p. 457 (POK_02 leaf 113)\",\"stance\":\"supports\",\"note\":\"\\\"ghrei- : ghroi- : ghri- ... ,darüberstreichen, hart darüberstreifen, bestreichen', Erweiterung von gher- ,reiben'. Gr. χρίω ,salbe, streiche an, färbe, kratze, steche'\\\"\"},\n        {\"src\":\"AHD\",\"where\":\"Watkins 1985 s.v. ghréi-\",\"stance\":\"supports\",\"note\":\"\\\"...in Greek khriein, to anoint: CHRISM, CHRIST, CHRISTEN, (CHRISTIAN); (CHRISTMAS). [Pok. ghréi- 457.]\\\"\"},\n        {\"src\":\"KLN\",\"where\":\"KLN_1966 s.v. chrism\",\"stance\":\"partial\",\"note\":\"\\\"fr. Gk. χρῖσμα, 'an unguent', fr. χρίω, 'to anoint', which is of uncertain origin. It possibly derives fr. I.-E. *ghrei-, *ghri- ... enlargements of base *gher-, 'to rub'.\\\" — Klein flags the root attachment as only probable.\"}]})\n\n    nodes.append({\n      \"id\":3,\"lang\":\"English\",\"words\":\"Christ, Christian, Christmas\",\"verdict\":\"confirmed\",\n      \"derivation\":\"The English words come through Latin, not directly from Greek: Gk Χριστός > Latin Christus > Old English Crīst (with the vowel of Latin ī, whence the modern diphthong); Christian < Latin Christiānus (OE cristen, remodelled on Latin in the 16th c.); Christmas < late Old English Crīstes mæsse 'Christ's mass', first recorded c. 1038, contracted to Christmas by Middle English. Nourai's Greek→English arrow compresses the Latin link but is otherwise right.\",\n      \"derivation_fa\":\"واژه‌های انگلیسی از راه لاتین آمده‌اند نه یکسره از یونانی: Χριστός یونانی > Christus لاتینی > Crīst انگلیسی باستان؛ Christian از Christiānus لاتینی؛ و Christmas از Crīstes mæsse انگلیسی باستان «مراسم مسیح» (نخستین ثبت حدود ۱۰۳۸ م). پیکان «یونانی ← انگلیسی» در نمودار، حلقهٔ لاتینی را حذف کرده اما در اصل درست است.\",\n      \"sources\":[E+\"christmas\"],\n      \"ref_check\":[{\"ref\":\"OEW:120\",\"status\":\"not_checked\",\"note\":\"Shipley lending-only.\"}],\n      \"consulted\":[\n        {\"src\":\"KLN\",\"where\":\"KLN_1966 s.v. Christ / Christmas\",\"stance\":\"supports\",\"note\":\"\\\"Christ, n. — L. Christus, fr. Gk. χριστός, 'anointed', translation of Heb. mashiah\\\"; \\\"Christmas, n. — ME. cristesmesse, fr. Late OE. ...\\\"\"},\n        {\"src\":\"AHD\",\"where\":\"Watkins 1985 s.v. ghréi-\",\"stance\":\"supports\",\"note\":\"CHRISM, CHRIST, CHRISTEN, (CHRISTIAN), (CHRISTMAS) all listed under ghréi-.\"}]})\n\n    nodes.append({\n      \"id\":4,\"lang\":\"Persian\",\"words\":\"krîsmas «کریسمس»\",\"verdict\":\"confirmed\",\n      \"derivation\":\"Persian کریسمس (krismas) is a 20th-century loan straight from English Christmas, not from French (French Noël would have given a quite different form); the spelling کریسمس renders English /ˈkrɪsməs/ with kāf + rā + yā for the short i and sīn-mīm-sīn for -smas. Wiktionary's Persian entry states plainly \\\"Borrowed from English Christmas\\\" and files it under Persian terms borrowed from English.\",\n      \"derivation_fa\":\"«کریسمس» وام‌واژه‌ای است از انگلیسی Christmas که در سدهٔ چهاردهم خورشیدی وارد فارسی شده است؛ اگر از فرانسه گرفته شده بود صورت Noël می‌داشت. املای «کریسمس» تلفظ انگلیسی /krɪsməs/ را با «ی» برای i کوتاه بازمی‌نماید. ویکی‌واژه نیز آن را صریحاً «وام‌گرفته از انگلیسی» می‌داند؛ ادعای نورایی درست است.\",\n      \"sources\":[W+\"کریسمس\"],\n      \"ref_check\":[{\"ref\":\"VOP:281\",\"status\":\"not_checked\",\"note\":\"Moshiri, Farhang-e Vazheha-ye Orupayi dar Farsi (VOP), has no copy online or on disk (refs_online.json: kind 'none', re-searched 2026-09).\"}],\n      \"consulted\":[\n        {\"src\":\"MON\",\"where\":\"MON_part1/part2, grep 'کریسمس'\",\"stance\":\"silent\",\"note\":\"0 hits — Mo'in's lexicon volumes do not carry the word.\"},\n        {\"src\":\"BQT\",\"where\":\"BQT_v1_pages.txt / BQT_v2_pages.txt, grep 'کریسمس'\",\"stance\":\"silent\",\"note\":\"0 hits, as expected for a 17th-century dictionary.\"},\n        {\"src\":\"ARY\",\"where\":\"ARY_pages.txt, grep 'کریسم'\",\"stance\":\"silent\",\"note\":\"0 hits.\"}]})\n\n    nodes.append({\n      \"id\":5,\"lang\":\"Turkish\",\"words\":\"xorozma\",\"verdict\":\"plausible\",\n      \"derivation\":\"The form is real but Nourai took it out of context. Klein s.v. rusma writes: \\\"rusma, n., a depilatory. — It. and F., a corruption of Turk. khorozma, inexact transliteration of Gk. χρῖσμα, 'unguent', lit. 'anything smeared on', fr. χρίειν, 'to smear, anoint'.\\\" So Ottoman Turkish khorozma/hurusma is indeed a (loose) rendering of Greek khrîsma 'unguent', borrowed from Byzantine Greek — the parent arrow Greek→Turkish is fine. What is wrong is what the chart makes of it: this Turkish word gave Italian/French rusma 'depilatory paste' in the 16th–17th c., and has nothing to do with Old French cresme (see node 6).\",\n      \"derivation_fa\":\"این صورت جعلی نیست ولی جای آن در نمودار نادرست است. کلاین ذیل rusma می‌نویسد که ایتالیایی و فرانسوی rusma «مادهٔ موبَر» تحریفی است از ترکی khorozma، که خود آوانگاشتِ نادقیقِ یونانی χρῖσμα «روغن، مرهم» است. پس وام‌گیری ترکی از یونانیِ بیزانسی درست است، اما این واژهٔ ترکی در سده‌های دهم–یازدهم هجری به ایتالیایی و فرانسوی rusma رسیده و هیچ ربطی به cresme فرانسوی کهن ندارد (بنگرید به گرهٔ ۶).\",\n      \"sources\":[],\n      \"ref_check\":[{\"ref\":\"OEW:120\",\"status\":\"not_checked\",\"note\":\"Shipley lending-only; the Turkish form appears in Klein s.v. rusma, which is very likely Nourai's real source (his next node cites KLN:369, the cream page).\"}],\n      \"consulted\":[\n        {\"src\":\"KLN\",\"where\":\"KLN_1966 s.v. rusma (line 33369)\",\"stance\":\"partial\",\"note\":\"\\\"It. and F., a corruption of Turk. khorozma, inexact transliteration of Gk. χρῖσμα, 'unguent'\\\" — confirms the word, but as the source of rusma, not of cresme.\"},\n        {\"src\":\"LKT\",\"where\":\"LKT.txt, grep 'rusma|chrisma|khorozma'\",\"stance\":\"silent\",\"note\":\"Lokotsch has no entry for the word.\"}]})\n\n    nodes.append({\n      \"id\":6,\"lang\":\"Old French\",\"words\":\"cresme\",\"verdict\":\"disputed\",\n      \"derivation\":\"Old French cresme (13th c.) 'chrism, holy oil; cream' does not come from Turkish. Klein s.v. cream: \\\"ME. creme, fr. OF. cresme (F. crème), which is a blend of Gaulish crama and Eccles. L. chrisma, fr. Gk. χρῖσμα\\\"; Etymonline and Skeat say the same (Skeat: \\\"Cream, (F. — L.) O.F. cresme (crème); Low L. crema\\\"). The route is Greek khrîsma → Church/Late Latin chrisma (already in the 4th–5th c. Latin Fathers) → Gallo-Romance, where it was contaminated with Late Latin cramum/crama 'cream' (probably Gaulish) → OF cresme. Turkish khorozma is a much later, parallel borrowing of the same Greek word and cannot be the ancestor of a 13th-century French form.\",\n      \"derivation_fa\":\"فرانسوی کهن cresme «روغن تدهین؛ سرشیر» از ترکی نیامده است. کلاین می‌نویسد cresme آمیزه‌ای است از crama گالی و chrisma لاتینی کلیسایی که خود از χρῖσμα یونانی است؛ اسکیت و اتیمانلاین نیز همین را می‌گویند. مسیر درست چنین است: یونانی khrîsma ← لاتینی کلیسایی chrisma (از سدهٔ چهارم میلادی) ← گالو-رومی، با آمیختگی با cramum «سرشیر» ← cresme. واژهٔ ترکی khorozma وام‌گیریِ جداگانه و بسیار متأخرترِ همان واژهٔ یونانی است و نمی‌تواند نیای صورتی فرانسوی از سدهٔ سیزدهم میلادی باشد؛ پس این پیکان خطای نورایی است.\",\n      \"sources\":[E+\"cream\"],\n      \"ref_check\":[{\"ref\":\"OEW:120\",\"status\":\"not_checked\",\"note\":\"Shipley lending-only.\"}],\n      \"consulted\":[\n        {\"src\":\"KLN\",\"where\":\"KLN_1966 s.v. cream (scan leaf 204; Nourai cites p. 369)\",\"stance\":\"contradicts\",\"note\":\"\\\"OF. cresme (F. crème), which is a blend of Gaulish crama and Eccles. L. chrisma, fr. Gk. χρῖσμα. See chrism.\\\" — Latin, not Turkish.\"},\n        {\"src\":\"SKT\",\"where\":\"SKT.txt s.v. Cream (line 4316)\",\"stance\":\"contradicts\",\"note\":\"\\\"Cream, (F. — L.) O.F. cresme (crème); Low L. crema...\\\" — Skeat too routes it through Latin.\"}]})\n\n    nodes.append({\n      \"id\":7,\"lang\":\"French\",\"words\":\"creme\",\"verdict\":\"confirmed\",\n      \"derivation\":\"Modern French crème is the regular continuation of Old French cresme: pre-consonantal /s/ was lost with compensatory lengthening in the 12th–13th c. (cresme > crême > crème), the same change as in teste > tête, isle > île. The modern spelling with grave accent is 18th-century orthography. Klein's cream entry gives exactly this ('OF. cresme (F. crème)').\",\n      \"derivation_fa\":\"crème فرانسوی دنبالهٔ منظم cresme در فرانسوی کهن است: «س» پیش از همخوان در سده‌های دوازدهم و سیزدهم میلادی افتاد و واکهٔ پیشین کشیده شد (cresme > crême > crème)، همان دگرگونی که در teste > tête و isle > île دیده می‌شود. کلاین نیز همین صورت را می‌آورد؛ ادعای نورایی درست است.\",\n      \"sources\":[E+\"cream\"],\n      \"ref_check\":[{\"ref\":\"KLN:369\",\"status\":\"supports\",\"note\":\"Klein s.v. cream (KLN_1966 line 9598, scan leaf 204): \\\"ME. creme, fr. OF. cresme (F. crème)\\\" — the cited page is the cream entry; page numbering of the scan is by leaf, but the entry is unambiguous.\"}],\n      \"consulted\":[\n        {\"src\":\"SKT\",\"where\":\"SKT.txt s.v. Cream\",\"stance\":\"supports\",\"note\":\"\\\"O.F. cresme (crème)\\\"\"},\n        {\"src\":\"KLN\",\"where\":\"KLN_1966 s.v. creamery\",\"stance\":\"supports\",\"note\":\"\\\"creamery, n. — F. cremerie, fr. crème\\\" — the modern French form is crème.\"}]})\n\n    nodes.append({\n      \"id\":8,\"lang\":\"Persian\",\"words\":\"kerem «کِرِم»\",\"verdict\":\"confirmed\",\n      \"derivation\":\"Persian کِرِم /kerem/ 'cream (dairy and cosmetic)' is a 20th-century loan from French crème, taken in through the French-dominated technical and cosmetic vocabulary of the Pahlavi era; the English form cream would have given *کریم. Wiktionary's Persian entry for کرم (Etymology 4) says simply \\\"From French crème\\\" and glosses it 'cream (dairy product)'. The two kasras in the book's vocalisation کِرِم mark the e-e vowels that Persian substitutes for French /ɛ/.\",\n      \"derivation_fa\":\"«کِرِم» به معنی سرشیر و نیز فرآوردهٔ آرایشی، وام‌واژه‌ای از فرانسوی crème است که در دورهٔ پهلوی همراه انبوه واژه‌های فنی و آرایشیِ فرانسوی وارد فارسی شد؛ اگر از انگلیسی cream گرفته شده بود صورت *کریم می‌داشت. ویکی‌واژه ذیل «کرم» (ریشه‌شناسی ۴) آن را «از فرانسوی crème» می‌داند. اعراب‌گذاری کتاب («کِرِم») همان واکهٔ e را نشان می‌دهد که فارسی به‌جای /ɛ/ فرانسوی می‌نشاند؛ ادعای نورایی درست است.\",\n      \"sources\":[W+\"کرم\"],\n      \"ref_check\":[{\"ref\":\"VOP:280\",\"status\":\"not_checked\",\"note\":\"VOP (Moshiri) not available in any copy.\"}],\n      \"consulted\":[\n        {\"src\":\"MON\",\"where\":\"MON_part1/part2, grep 'کِرِم'\",\"stance\":\"silent\",\"note\":\"0 hits in the OCR of Mo'in's lexicon volumes (the OCR of Persian diacritics is unreliable, so this is weak evidence).\"},\n        {\"src\":\"BQT\",\"where\":\"BQT_v1/v2_pages.txt\",\"stance\":\"silent\",\"note\":\"no European loan of this kind in Borhan-e Qate'.\"}]})\n\n    nodes.append({\n      \"id\":9,\"lang\":\"English\",\"words\":\"cream\",\"verdict\":\"plausible\",\n      \"derivation\":\"English cream is right in substance but hangs from the wrong box: it was borrowed in the early 14th c. as creyme/creme from OLD French cresme (node 6), not from modern French crème — the latter was re-borrowed separately in the 19th c. as creme in cosmetic and culinary use. Klein: \\\"cream, n. — ME. creme, fr. OF. cresme (F. crème)\\\"; Etymonline: \\\"early 14c., creyme ... from Old French cresme, craime, creme ... The French word replaced Old English ream; it was re-borrowed 19c. as creme.\\\"\",\n      \"derivation_fa\":\"واژهٔ انگلیسی cream در اصل درست است ولی از جعبهٔ نادرست آویخته شده: انگلیسی آن را در آغاز سدهٔ چهاردهم میلادی به صورت creyme از فرانسویِ کهن cresme گرفت، نه از crème فرانسوی امروزی؛ صورت اخیر جداگانه و در سدهٔ نوزدهم به شکل creme دوباره وام گرفته شد و با cream دوگانه (doublet) می‌سازد. کلاین و اتیمانلاین هر دو همین را می‌گویند. پس پیکان با یک پله جابه‌جایی رسم شده است.\",\n      \"sources\":[E+\"cream\"],\n      \"ref_check\":[{\"ref\":\"KLN:369\",\"status\":\"partial\",\"note\":\"Klein s.v. cream: \\\"ME. creme, fr. OF. cresme (F. crème)\\\" — supports the word but makes Old French, not Modern French, the immediate source.\"}],\n      \"consulted\":[\n        {\"src\":\"SKT\",\"where\":\"SKT.txt s.v. Cream\",\"stance\":\"partial\",\"note\":\"\\\"(F. — L.) O.F. cresme\\\" — again Old French.\"},\n        {\"src\":\"AHD\",\"where\":\"Watkins 1985 s.v. ghréi-\",\"stance\":\"silent\",\"note\":\"Watkins lists CHRISM/CHRIST etc. under ghréi- but does not list CREAM (the Gaulish half of the blend keeps it out).\"}]})\n\n    nodes.append({\n      \"id\":10,\"lang\":\"Greek\",\"words\":\"xrôs; xroma\",\"verdict\":\"plausible\",\n      \"derivation\":\"Greek χρώς (khrṓs) 'surface of the body, skin, complexion' and χρῶμα (khrôma) 'skin, complexion, colour' are attached to the u-extension *gʰreu- 'to rub, grind' by Pokorny (p. 460: \\\"mit Abtönung *ghrō[u]-: χρώς ,Oberfläche eines Körpers (*worüber man darüber streift)', daher ,Haut, Hautfarbe'\\\") and by Watkins (ghrēu- §6-7), i.e. 'rubbed surface' → 'skin' → 'colour of the skin' → 'colour'. That is Nourai's picture. Beekes (2010), however, judges χρώς/χρῶμα of uncertain origin, and Etymonline follows him (\\\"Beekes considers this noun to be of uncertain origin. It sometimes is explained as being somehow from PIE *ghreu-\\\"). Hence plausible rather than confirmed. Note also that the chart's forms belong under Pokorny 460, not the cited 439/457.\",\n      \"derivation_fa\":\"یونانی χρώς «سطح تن، پوست» و χρῶμα «رنگ‌وروی پوست، رنگ» را پوکورنی (ص ۴۶۰) و واتکینز ذیل گسترشِ *gʰreu- «ساییدن» می‌آورند، با این تحول معنایی: «سطحِ ساییده» ← «پوست» ← «رنگِ پوست» ← «رنگ»؛ همان چیزی که نورایی رسم کرده است. اما بیکس (۲۰۱۰) ریشهٔ این دو واژه را نامعلوم می‌داند و اتیمانلاین نیز از او پیروی می‌کند. پس این پیوند «با احتیاط پذیرفتنی» است. افزون بر آن، جای درست این شاخه در پوکورنی ص ۴۶۰ است نه ۴۳۹/۴۵۷ که نورایی ارجاع داده.\",\n      \"sources\":[E+\"chrome\"],\n      \"ref_check\":[{\"ref\":\"AHD:240\",\"status\":\"supports\",\"note\":\"Content check in Watkins 1985 s.v. ghréu- §6-7: \\\"Variant form *ghrow- in Greek khrōs, skin (< 'rough surface' ?) ... Suffixed variant form *ghrō-mn̥ in Greek khrōma, skin, complexion, color\\\". Nourai's page 240 is a page of the 1975/76 New College Edition dictionary text (probably the CHROME entry), which is not open online, so the page itself could not be inspected.\"}],\n      \"consulted\":[\n        {\"src\":\"POK\",\"where\":\"pp. 460-461 (POK_02 leaf 117-119)\",\"stance\":\"supports\",\"note\":\"\\\"2. ghreu- ... ,scharf darüber reiben, zerreiben', Erweiterung von gher- ,reiben' ... χρώς ,Oberfläche eines Körpers', daher ,Haut, Hautfarbe' ... χρῶμα ,Haut, Hautfarbe, Farbe, Schminke'\\\"\"},\n        {\"src\":\"KLN\",\"where\":\"KLN_1966 s.v. chrome\",\"stance\":\"supports\",\"note\":\"\\\"Gk. χρῶμα ... 'surface of the body, skin, color of the skin, color' ... fr. I.-E. base *ghrōu-, *ghrō-, 'to rub, smear, tinge', which is rel. to base *gher-, 'to rub'\\\"\"},\n        {\"src\":\"AHD\",\"where\":\"Watkins 1985 s.v. ghréu-\",\"stance\":\"supports\",\"note\":\"\\\"[Pok. 2. ghréu- 460.]\\\" — the same root, but Pokorny page 460.\"}]})\n\n    nodes.append({\n      \"id\":11,\"lang\":\"French\",\"words\":\"chrome\",\"verdict\":\"confirmed\",\n      \"derivation\":\"French chrome is a learned neologism, not an inherited word: Vauquelin isolated the metal in 1797 in Siberian red lead, and Fourcroy and Haüy proposed the name chrome from Greek χρῶμα 'colour', because its compounds are brilliantly coloured (chrome yellow, chrome green). Klein: \\\"chrome, n. — F., coined by the French chemist Nicolas-Louis Vauquelin (1763-1829) in 1797 fr. Gk. χρῶμα\\\". English took chrome from French in 1800.\",\n      \"derivation_fa\":\"chrome فرانسوی واژه‌ای ساختگی و علمی است نه میراثی: وُکلَن در ۱۷۹۷ م این فلز را جدا کرد و فورکروا و اویی نام chrome را از χρῶμα یونانی «رنگ» برای آن پیشنهاد کردند، چون ترکیب‌های آن رنگ‌های درخشان دارند. کلاین همین را می‌گوید و انگلیسی نیز در ۱۸۰۰ م آن را از فرانسه گرفت؛ ادعای نورایی درست است.\",\n      \"sources\":[E+\"chrome\"],\n      \"ref_check\":[{\"ref\":\"AHD:240\",\"status\":\"supports\",\"note\":\"Watkins 1985 s.v. ghréu- §7 lists CHROMA, CHROMATIC, CHROME, (CHROMIUM) from Greek khrōma; the cited New College page is not accessible online.\"}],\n      \"consulted\":[\n        {\"src\":\"KLN\",\"where\":\"KLN_1966 s.v. chrome (line 7587)\",\"stance\":\"supports\",\"note\":\"\\\"F., coined by the French chemist Nicolas-Louis Vauquelin (1763-1829) in 1797 fr. Gk. χρῶμα\\\"\"},\n        {\"src\":\"WEB\",\"where\":\"WEB_vol1.txt\",\"stance\":\"silent\",\"note\":\"Webster vol. 1 (A–?) as scanned does not yield a usable chrome entry.\"}]})\n\n    nodes.append({\n      \"id\":12,\"lang\":\"Persian\",\"words\":\"korom «کُرُم»; koromosom «کرموزُم»\",\"verdict\":\"transcription_suspect\",\n      \"derivation\":\"The derivation is right: Persian کُرُم /korom/ 'chromium' is borrowed from French chrome (Wiktionary's Persian entry: \\\"Borrowed from French chrome\\\", tree Ancient Greek χρῶμα > French > Persian), and کروموزوم /koromozom/ 'chromosome' from French chromosome — Persian breaks up the initial cluster kr- with an epenthetic vowel (kr- > ko-r-), as in کلوپ, پروتئین. The problem is the printed script of the second word: the book prints «کرموزُم», which is missing the و of کرو- and the second و of -زوم; the normal Persian spelling is کروموزوم (so Mo'in's own text: \\\"...بصورت رشته‌های کوتاه موسوم به کروموزوم درمی‌آیند\\\"). The JSON reproduces the page exactly (checked on the 300-dpi render of pdf page 189), so this is the book's own defective vocalisation, not an extraction error; note too that the transliteration koromosom (with s) does not match the ز of the printed script.\",\n      \"derivation_fa\":\"ریشه‌شناسی درست است: «کُرُم» از فرانسوی chrome و «کروموزوم» از فرانسوی chromosome گرفته شده‌اند؛ فارسی خوشهٔ آغازینِ kr- را با واکهٔ میانجی می‌شکند (کُرُم، کُروموزوم) چنان‌که در «کلوپ» و «پروتئین». اشکال در املای چاپی واژهٔ دوم است: کتاب «کرموزُم» چاپ کرده که «و»های آن افتاده است؛ املای رایج و درست «کروموزوم» است، چنان‌که در متن خودِ فرهنگ معین آمده. تصویر ۳۰۰ نقطه‌ای صفحهٔ ۱۸۹ نشان می‌دهد که استخراج داده‌ها امین بوده و خطا از چاپ کتاب است؛ افزون بر آن، آوانگاشت koromosom با «ز» متن فارسی نمی‌خواند.\",\n      \"error_in\":\"book\",\"book_prints\":\"کرموزُم\",\"correct_form\":\"کروموزوم\",\n      \"sources\":[W+\"کروم\"],\n      \"ref_check\":[{\"ref\":\"VOP:281\",\"status\":\"not_checked\",\"note\":\"VOP (Moshiri) unavailable in any copy.\"}],\n      \"consulted\":[\n        {\"src\":\"MON\",\"where\":\"MON_part2.txt line 93071 (article on the cell nucleus)\",\"stance\":\"partial\",\"note\":\"\\\"...این رشته‌های کرماتین در موقع تقسیم غیر مستقیم بصورت رشته‌های کوتاه موسوم به کروموزوم درمی‌آیند\\\" — Mo'in spells the word کروموزوم, against the book's کرموزُم.\"},\n        {\"src\":\"ARY\",\"where\":\"ARY_pages.txt, grep 'کروم'\",\"stance\":\"silent\",\"note\":\"0 hits; Aryanpur's IE-root dictionary does not treat modern European loans.\"},\n        {\"src\":\"BQT\",\"where\":\"BQT_v2_pages.txt\",\"stance\":\"silent\",\"note\":\"no such entry.\"}]})\n\n    nodes.append({\n      \"id\":13,\"lang\":\"English\",\"words\":\"chrome, chromium, chromosome\",\"verdict\":\"plausible\",\n      \"derivation\":\"Two of the three are exactly as drawn: chrome (1800) and chromium (1807) are from French chrome/chromium (Fourcroy and Haüy's name, Latinised). Chromosome, however, is not French: it was coined in German by Wilhelm von Waldeyer-Hartz in 1888 (Chromosom) from Greek χρῶμα 'colour' + σῶμα 'body', because the bodies took up aniline stains, and English borrowed it from German in 1889. Klein s.v. chromosome states this explicitly. So the node is right for chrome/chromium, loose for chromosome.\",\n      \"derivation_fa\":\"دو واژه از سه واژه دقیقاً چنان‌اند که نورایی رسم کرده: chrome (۱۸۰۰ م) و chromium (۱۸۰۷ م) از فرانسوی گرفته شده‌اند. اما chromosome فرانسوی نیست: والدیر-هارتس در ۱۸۸۸ م آن را در آلمانی (Chromosom) از χρῶμα «رنگ» و σῶμα «تن» ساخت، چون این اجسام رنگ‌های آنیلینی را می‌گیرند، و انگلیسی آن را از آلمانی گرفت. کلاین همین را می‌گوید. پس گرهٔ انگلیسی دربارهٔ chromosome دقیق نیست.\",\n      \"sources\":[E+\"chrome\"],\n      \"ref_check\":[{\"ref\":\"AHD:240\",\"status\":\"partial\",\"note\":\"Watkins 1985 s.v. ghréu- lists CHROME, (CHROMIUM) — but not CHROMOSOME — under the root; the cited 1975/76 dictionary page is not accessible online.\"}],\n      \"consulted\":[\n        {\"src\":\"KLN\",\"where\":\"KLN_1971 s.v. chromosome\",\"stance\":\"partial\",\"note\":\"\\\"Coined by the German anatomist Wilhelm von Waldeyer-Hartz (1836-1921) in 1888 fr. Gk. χρῶμα, 'color', and σῶμα, 'body'.\\\" — German, not French.\"},\n        {\"src\":\"KLN\",\"where\":\"KLN_1966 s.v. chrome / chromic\",\"stance\":\"supports\",\"note\":\"chrome from French; \\\"chromic, adj., pertaining to chromium. — Formed fr. chromium with suff. -ic.\\\"\"}]})\n\n    nodes.append({\n      \"id\":14,\"lang\":\"Greek\",\"words\":\"kharax, xarax\",\"verdict\":\"disputed\",\n      \"derivation\":\"Greek χάραξ 'pointed stake, vine-prop' and χαράσσω 'to sharpen, notch, engrave' (whence χαρακτήρ 'engraving tool; stamp; distinctive mark') are indeed grouped with a 'scratch' root by Watkins (gher-4 §1) — but not with the root of this chart page: Pokorny keeps them in a separate entry, \\\"2. gher- ,kratzen, ritzen, scharren'?\\\" on p. 441 (with a question mark), away from 2. gher- 'reiben' 439 and its ghrei-/ghreu- extensions. Modern Greek etymology has moved further away: Beekes 2010 calls χάραξ \\\"most probably Pre-Greek\\\" (so Etymonline: \\\"a word of uncertain etymology which Beekes considers 'most probably Pre-Greek'\\\"), and Klein derives χαράσσειν from Semitic (Hebrew ḥārash 'he engraved, plowed'). The arrow as drawn is therefore not supported.\",\n      \"derivation_fa\":\"یونانی χάραξ «چوب نوک‌تیز، داربستِ تاک» و χαράσσω «تیز کردن، کندن، حکاکی کردن» (که χαρακτήρ از آن است) را واتکینز ذیل ریشه‌ای به معنی «خراشیدن» می‌آورد، اما نه ذیل همان ریشهٔ این صفحه: پوکورنی آن‌ها را در مدخل جداگانه‌ای با نشان پرسش، «۲. gher- خراشیدن، خط انداختن» در ص ۴۴۱، آورده است نه ذیل gher- «ساییدن» ص ۴۳۹. ریشه‌شناسی امروزی حتی دورتر رفته است: بیکس (۲۰۱۰) χάραξ را «به احتمال زیاد پیش‌یونانی» می‌داند و کلاین χαράσσειν را از سامی (عبری ḥārash «کند، شخم زد») می‌گیرد. پس این پیکان به شکلی که رسم شده پذیرفتنی نیست.\",\n      \"sources\":[E+\"character\"],\n      \"ref_check\":[{\"ref\":\"AHD\",\"status\":\"partial\",\"note\":\"Watkins 1985 s.v. gher-4 §1: \\\"Extended zero-grade form *ghr(e)-k- in: a. Greek kharax, a pointed stake ...; b. Greek kharassein, to sharpen, notch, carve, cut: CHARACTER, GASH. [Pok. 2. gher- 439.]\\\" — supports Nourai's arrow, but Watkins' own Pokorny reference (439) does not contain these words.\"}],\n      \"consulted\":[\n        {\"src\":\"POK\",\"where\":\"p. 441 (POK_02 leaf 99); POK_full 'Root/lemma: gher-2, Page(s): 441'\",\"stance\":\"partial\",\"note\":\"\\\"2. gher- ,kratzen, ritzen, scharren'? Gr. χαράδρα ... χαράσσω ,spitze, schärfe, kerbe' , χάραξ ,Pfahl, Spitzpfahl, Weinpfahl' , χαρακτήρ ,Präger', dann ,Stempel, Gepräge, Eigenart'\\\" — a separate root entry (with Pokorny's own question mark), not the 439/457 root of this chart.\"},\n        {\"src\":\"KLN\",\"where\":\"KLN_1971 s.v. character\",\"stance\":\"contradicts\",\"note\":\"\\\"from the stem of χαράσσειν, 'to engrave', which is of Semitic, prob. Hebrew, origin. Cp. Heb. ḥārāsh, 'he engraved, plowed' ...\\\"\"},\n        {\"src\":\"WLD\",\"where\":\"Bd. I 602\",\"stance\":\"partial\",\"note\":\"Walde-Pokorny I 602 is the reference given for this separate 'kratzen' root, distinct from I 605 f. (the 'reiben' root of this chart).\"}]})\n\n    nodes.append({\n      \"id\":15,\"lang\":\"English\",\"words\":\"character\",\"verdict\":\"confirmed\",\n      \"derivation\":\"Whatever the ultimate origin of χάραξ, the Greek→English chain itself is beyond doubt: χαράσσω 'engrave' → χαρακτήρ 'engraving tool, stamp, distinctive mark' → Latin character → Old French caractere (13th c.) → Middle English carecter (mid-14c., 'symbol marked on the body'), the Latin ch- spelling restored in the 1500s; the sense 'sum of qualities defining a person' is a Hellenistic metaphor that reaches English in the 1640s.\",\n      \"derivation_fa\":\"هرچه ریشهٔ نهاییِ χάραξ باشد، زنجیرهٔ یونانی ← انگلیسی تردیدناپذیر است: χαράσσω «حک کردن» ← χαρακτήρ «ابزار حکاکی، مُهر، نشان ویژه» ← character لاتینی ← caractere فرانسوی کهن (سدهٔ سیزدهم) ← carecter انگلیسی میانه (میانهٔ سدهٔ چهاردهم، به معنی «نشانِ داغ‌شده بر تن»)؛ املای ch- در سدهٔ شانزدهم از روی لاتین بازگردانده شد و معنی «مجموعهٔ خصایل شخص» استعاره‌ای هلنیستی است که در دههٔ ۱۶۴۰ به انگلیسی رسید.\",\n      \"sources\":[E+\"character\"],\n      \"ref_check\":[{\"ref\":\"AHD\",\"status\":\"supports\",\"note\":\"Watkins 1985 s.v. gher-4 §1b lists CHARACTER from Greek kharassein.\"}],\n      \"consulted\":[\n        {\"src\":\"KLN\",\"where\":\"KLN_1971 s.v. character\",\"stance\":\"supports\",\"note\":\"\\\"ME. caracter, caractere, fr. OF. caractere (F. caractère), fr. L. character, fr. Gk. χαρακτήρ, 'graving tool, mark engraved, impress, character'\\\"\"},\n        {\"src\":\"FSD\",\"where\":\"FSD_vol1.txt s.v. Characinidae\",\"stance\":\"supports\",\"note\":\"\\\"[< Gr. charax, sea-fish, < charassō, sharpen.]\\\" — Funk & Wagnalls has the same Greek pair.\"}]})\n\n    nodes.append({\n      \"id\":16,\"lang\":\"Germanic\",\"words\":\"grautaz\",\"verdict\":\"confirmed\",\n      \"derivation\":\"Proto-Germanic *grautaz 'coarse-grained, thick, bulky' is the o-grade of the d-extension *gʰreu-d- of *gʰreu- 'to rub, grind' — literally '(what is) coarsely ground'. Pokorny 461 puts it there explicitly (\\\"Erweiterung ghreu-d-: ... ags. great ,grobkörnig, groß, dick' (engl. great), afries. grāt, as. grōt, ahd. grōz ,groß' (germ. *grauta-)\\\"), beside ON grautr 'groats, porridge' and OE grēot 'grit'. Watkins ghrēu- §4 gives the same. Nourai's form and gloss ('coarse, large') are exactly Watkins'.\",\n      \"derivation_fa\":\"ژرمنی آغازین *grautaz «درشت‌دانه، ستبر، بزرگ» صورتِ o-دار گسترشِ *gʰreu-d- از ریشهٔ *gʰreu- «ساییدن، آسیاب کردن» است، یعنی در اصل «آنچه درشت آسیا شده». پوکورنی در ص ۴۶۱ همین را می‌آورد (در کنار grautr «بلغور» در نورس کهن و grēot «شن» در انگلیسی باستان) و واتکینز نیز ذیل ghrēu- بند ۴. صورت و معنایی که نورایی داده عیناً از واتکینز است؛ ادعای او درست است.\",\n      \"sources\":[E+\"great\"],\n      \"ref_check\":[{\"ref\":\"AHD\",\"status\":\"supports\",\"note\":\"Watkins 1985 s.v. ghréu- §4: \\\"Germanic *grautaz, coarse, thick (< 'coarsely ground'), in: a. Old English gréat, coarse, thick, bulky, large: GREAT\\\".\"}],\n      \"consulted\":[\n        {\"src\":\"POK\",\"where\":\"p. 461 (POK_02 leaf 119)\",\"stance\":\"supports\",\"note\":\"\\\"aisl. grautr m. ,Grütze' (,grobgemahlenes'); ags. great ,grobkörnig, groß, dick' (engl. great) ... (germ. *grauta-)\\\"\"},\n        {\"src\":\"KLN\",\"where\":\"KLN_1971 s.v. great\",\"stance\":\"supports\",\"note\":\"\\\"The original meaning of these adjectives was prob. 'gross-grained, coarse'. Cp. ON. grautr, 'groats', E. greot, 'grit, sand, dust, gravel', and see grit.\\\"\"}]})\n\n    nodes.append({\n      \"id\":17,\"lang\":\"English\",\"words\":\"great\",\"verdict\":\"confirmed\",\n      \"derivation\":\"Old English grēat 'big, tall, thick, stout, massive; coarse' continues West Germanic *grauta- directly (OS grōt, OFris. grāt, Du. groot, Ger. groß); OE ēa > ME ē > modern /eɪ/ gives great. The semantic path 'coarse' → 'bulky' → 'great' is the standard account, though the OED, quoted by Etymonline, warns that \\\"the connexion is not free from difficulty\\\" — that caution touches the PIE attachment (node 16), not the Germanic→English step, which is certain.\",\n      \"derivation_fa\":\"great انگلیسی دنبالهٔ مستقیم grēat انگلیسی باستان «بزرگ، ستبر، درشت» از ژرمنی باختری *grauta- است (هم‌ریشه با groot هلندی و groß آلمانی)؛ دوواکهٔ ēa در انگلیسی باستان به ē در انگلیسی میانه و سپس به /eɪ/ امروزی بدل شده است. مسیر معنایی «درشت» ← «حجیم» ← «بزرگ» پذیرفتهٔ همگان است؛ تردیدِ فرهنگ آکسفورد («این پیوند بی‌اشکال نیست») به پیوند با ریشهٔ هندواروپایی بازمی‌گردد نه به این پله. ادعای نورایی درست است.\",\n      \"sources\":[E+\"great\"],\n      \"ref_check\":[{\"ref\":\"AHD\",\"status\":\"supports\",\"note\":\"Watkins 1985 s.v. ghréu- §4a: \\\"Old English gréat ... : GREAT\\\".\"}],\n      \"consulted\":[\n        {\"src\":\"KLN\",\"where\":\"KLN_1971 s.v. great\",\"stance\":\"supports\",\"note\":\"\\\"ME. great, gret, greet, grete, fr. OE. great, rel. to OS. grot, OFris. grāt, Du. groot, OHG., MHG. grōz, G. gross\\\"\"},\n        {\"src\":\"POK\",\"where\":\"p. 461\",\"stance\":\"supports\",\"note\":\"\\\"ags. great ... (engl. great)\\\" cited under 2. ghreu-.\"}]})\n\n    nodes.append({\n      \"id\":18,\"lang\":\"Celtic\",\"words\":\"graw\",\"verdict\":\"confirmed\",\n      \"derivation\":\"The Celtic word is well attested: Gaulish *grava 'gravel', Welsh gro 'coarse gravel', Old/Middle Cornish grou, grow, Middle Breton grouanenn, Breton groan/grouan 'gravier' (Pokorny 460). Watkins reconstructs it as \\\"Probably Celtic *graw-\\\" — which is precisely Nourai's 'graw' with its gloss 'rough surface, gravel'; the attachment to *gʰreu- 'rub, grind' is what Pokorny and Watkins both propose (Pokorny notes the vocalism is unclear).\",\n      \"derivation_fa\":\"واژهٔ سلتی به‌خوبی گواهی شده است: گالی *grava «سنگ‌ریزه»، ولزی gro، کورنی کهن grou/grow، برِتونی grouan «شن درشت» (پوکورنی ص ۴۶۰). واتکینز آن را «احتمالاً سلتیِ *graw-» بازسازی می‌کند که همان صورتِ نورایی است. پیوند آن با *gʰreu- «ساییدن» را هم پوکورنی و هم واتکینز پیشنهاد کرده‌اند، هرچند پوکورنی خودِ آواگردانی واژه را «نامشخص» می‌داند؛ ادعای نورایی درست است.\",\n      \"sources\":[E+\"gravel\"],\n      \"ref_check\":[{\"ref\":\"AHD\",\"status\":\"supports\",\"note\":\"Watkins 1985 s.v. ghréu- §8: \\\"Probably Celtic *graw- in Old French grave, greve, coarse sand, gravel: GRAVEL.\\\"\"}],\n      \"consulted\":[\n        {\"src\":\"POK\",\"where\":\"p. 460 (POK_02 leaf 119)\",\"stance\":\"supports\",\"note\":\"\\\"gall. *grava ,Kies', cymr. gro, acorn. grou, mcorn. grow ,Sand', mbret. grouanenn ds., nbret. gro(a) f. ,Sandstrand', groan, grouan ,gravier' (Vokalismus unklar)\\\"\"},\n        {\"src\":\"IEC\",\"where\":\"Mann, s.v. ghreun- (IEC.txt line 4930)\",\"stance\":\"supports\",\"note\":\"\\\"ghreun- (ghreuən, ghreusn-) 'grit, gravel, groats' Br. gruan 'gravel'; W graian ... ON grjon 'groats'\\\"\"}]})\n\n    nodes.append({\n      \"id\":19,\"lang\":\"English\",\"words\":\"gravel\",\"verdict\":\"plausible\",\n      \"derivation\":\"English gravel is not taken from Celtic directly, as the arrow implies: it appears in the early 13th c. from Old French gravele 'sand, gravel; sandy river-bed', a diminutive of OF grave 'sand, seashore' (modern French grève), and it is that Gallo-Romance grava that is 'possibly Celtic' (Klein) / 'probably Celtic *graw-' (Watkins). So the substance is right but a Romance link is missing.\",\n      \"derivation_fa\":\"gravel انگلیسی یکسره از سلتی گرفته نشده است، برخلاف آنچه پیکان نشان می‌دهد: این واژه در آغاز سدهٔ سیزدهم میلادی از gravele فرانسویِ کهن، مصغّرِ grave «شن، ساحل»، وارد انگلیسی شده و همان grava گالو-رومی است که «احتمالاً سلتی» دانسته می‌شود. پس محتوا درست است اما حلقهٔ فرانسوی از نمودار افتاده است.\",\n      \"sources\":[E+\"gravel\"],\n      \"ref_check\":[{\"ref\":\"AHD\",\"status\":\"partial\",\"note\":\"Watkins 1985 s.v. ghréu- §8 routes GRAVEL through \\\"Old French grave, greve\\\" — a step the chart omits.\"}],\n      \"consulted\":[\n        {\"src\":\"KLN\",\"where\":\"KLN_1966 s.v. gravel (line 16619)\",\"stance\":\"partial\",\"note\":\"\\\"ME. gravel, fr. OF. gravele, gravelle ... dimin. of OF. grave (F. grève), 'strand of sand, sandbank', which is of uncertain, possibly Celtic, origin. Cp. W. gro, 'coarse gravel', Bret. grouan, Co. grow, 'gravel'.\\\"\"},\n        {\"src\":\"SKT\",\"where\":\"SKT.txt\",\"stance\":\"silent\",\"note\":\"the OCR of Skeat's Gravel entry is not recoverable (the g-section OCR is badly damaged).\"}]})\n\n    return {\n      \"entry\":0,\n      \"root\":\"Gher 3; Ghrěi, Ghreu\",\n      \"verdict\":\"confirmed\",\n      \"modern_form\":\"PIE *gʰer- 'to rub, scrape' (Pokorny 2. gher- 439) with its extensions *gʰrei- (Pok. 457) and *gʰreu- (Pok. 460)\",\n      \"note\":\"The root box is right: Pokorny p. 439 heads \\\"2. gher- ,hart worüber streichen, reiben'; vgl. auch die Erweiterungen ghrei-, ghreu-, ghrem-, ghren-\\\", and Watkins' gher-4 'To scrape, scratch ... See also extensions ghréi- and ghréu-' is the same thing, so both the language label (Indo-European) and the gloss are correct. Two bookkeeping caveats: (a) the second cited page, 457, is the ghrei- entry, but the ghreu- material (xrôs/xroma, grautaz, graw) is on Pokorny 460-461, not 457; (b) the kharax/character branch is not from this root at all in Pokorny, who gives it a separate, query-marked entry \\\"2. gher- ,kratzen, ritzen'?\\\" on p. 441. Substantively the page's real problem is the Turkish→Old French link (nodes 5-6), which is a genuine error: Old French cresme comes from Ecclesiastical Latin chrisma.\",\n      \"note_fa\":\"جعبهٔ ریشه درست است: پوکورنی در ص ۴۳۹ مدخل «۲. gher- سخت بر چیزی کشیدن، ساییدن» را با اشاره به گسترش‌های ghrei- و ghreu- می‌آورد و واتکینز نیز همین را ذیل gher-4 «خراشیدن، ساییدن» دارد؛ پس هم برچسب «هندواروپایی» و هم معنی درست است. دو نکتهٔ ارجاعی: نخست آنکه صفحهٔ ۴۵۷ مدخل ghrei- است و مواد ghreu- (χρώς، *grautaz، *graw) در صص ۴۶۰–۴۶۱ آمده نه ۴۵۷؛ دوم آنکه شاخهٔ χάραξ/character در پوکورنی اصلاً از این ریشه نیست و مدخل جداگانه‌ای در ص ۴۴۱ دارد. خطای اصلی صفحه اما پیوند «ترکی ← فرانسوی کهن» است (گره‌های ۵ و ۶): cresme از chrisma لاتینیِ کلیسایی آمده است.\",\n      \"sources\":[E+\"chrism\", E+\"gravel\"],\n      \"ref_check\":[\n        {\"ref\":\"POK:439\",\"status\":\"supports\",\"note\":\"POK_02 leaf 95-96 (printed pp. 439-440): \\\"2. gher- ,hart worüber streichen, reiben'; vgl. auch die Erweiterungen ghrei-, ghreu-, ghrem-, ghren-\\\".\"},\n        {\"ref\":\"POK:457\",\"status\":\"supports\",\"note\":\"POK_02 leaf 113 (printed p. 457): \\\"ghrei- : ghroi- : ghri- ... Erweiterung von gher- ,reiben'; viel weniger fruchtbar als die u-Erweiterung ghreu-\\\" — but the ghreu- entry itself begins on p. 460, so the chart's Ghreu material is one page-reference short.\"},\n        {\"ref\":\"OEW:120\",\"status\":\"not_checked\",\"note\":\"Shipley 1984 is lending-only on archive.org (djvu.txt 401/403); no open copy found.\"}],\n      \"consulted\":[POK_ROOT, WLD_ROOT, AHD_ROOT,\n        {\"src\":\"IEC\",\"where\":\"Mann s.v. ghreun-, greuō (IEC.txt lines 4301, 4930)\",\"stance\":\"supports\",\"note\":\"Mann has the same family: \\\"ghreun- (ghreuən, ghreusn-) 'grit, gravel, groats'\\\".\"}],\n      \"nodes\":nodes}\n\ndef ent1():\n    nodes = []\n    nodes.append({\n      \"id\":1,\"lang\":\"Avestan\",\"words\":\"zara 2\",\"verdict\":\"confirmed\",\n      \"derivation\":\"Gathic Avestan zara- m. 'striving, goal' is one of Pokorny's two Iranian witnesses for *ǵʰer- 'to desire': Bartholomae, Altiranisches Wörterbuch, has \\\"g. zara- m. 'Streben, Ziel'\\\" quoting Y.28 (kaθā mazdā zarəm carānī 'how, o Mazdā, shall I attain my goal'). The Avestan z- is the regular Iranian outcome of PIE palatal *ǵʰ (as in zaotar- < *ǵʰeu-tor-), and Sanskrit háryati 'takes pleasure in, desires' is the Indic match. Nourai's gloss 'desire, aim, target' is Bartholomae's 'Streben, Ziel' exactly.\",\n      \"derivation_fa\":\"«zara-» در اوستایی گاهانی، اسم مذکر به معنی «کوشش، آماج» است و یکی از دو گواه ایرانیِ پوکورنی برای ریشهٔ *ǵʰer- «خواستن» به شمار می‌رود؛ بارتولومه در فرهنگ ایرانی باستان آن را «Streben, Ziel» معنی کرده و شاهدی از یسنا ۲۸ آورده است. «ز» ایرانی بازتاب منظمِ *ǵʰ کامیِ هندواروپایی است (چنان‌که در zaotar-) و همتای هندی آن háryati سنسکریت است. معنایی که نورایی داده عیناً همان بارتولومه است؛ ادعای او درست است.\",\n      \"sources\":[E+\"exhort\"],\n      \"ref_check\":[{\"ref\":\"POK:440\",\"status\":\"supports\",\"note\":\"POK_02 leaf 97 (printed pp. 440-441): \\\"1. ĝher- ,begehren, gern haben' ... Ai. háryati ,findet Gefallen, begehrt'; av. zara- m. ,Streben, Ziel'\\\".\"}],\n      \"consulted\":[\n        {\"src\":\"BRT\",\"where\":\"Bartholomae, AiW, s.v. zara- (BRT.txt line 27784)\",\"stance\":\"supports\",\"note\":\"\\\"• g. zara- m. 'Streben, Ziel': kaθā mazdā °nm carani haca xšmat ... 'ob ich wohl, o M., durch euch mein Ziel durchsetzen werde'\\\"\"},\n        {\"src\":\"POK\",\"where\":\"pp. 440-441\",\"stance\":\"supports\",\"note\":\"\\\"av. zara- m. ,Streben, Ziel'\\\" cited in the root entry itself.\"},\n        {\"src\":\"KNT\",\"where\":\"KNT.txt (Kent, Old Persian lexicon)\",\"stance\":\"silent\",\"note\":\"no Old Persian cognate of zara- is recorded.\"}]})\n\n    nodes.append({\n      \"id\":2,\"lang\":None,\"words\":\"\",\"verdict\":\"unverified\",\n      \"derivation\":\"Empty pass-through box: on the printed page (pdf p. 189, book p. 159; see data/verification/sources/refs/ocr/BOOK/189.png) the box to the right of the Avestan box is drawn but left completely blank — no language, no reference, no word. The extraction is faithful to the page; there is nothing to verify. Judging by the layout of the other charts, this slot was meant for the Persian reflex (the expected fillers would be Middle/New Persian forms of the same root, e.g. NP آز/زور-type words), but the book prints nothing.\",\n      \"derivation_fa\":\"جعبهٔ خالی: در صفحهٔ چاپی (برگ ۱۸۹ پی‌دی‌اف، ص ۱۵۹ کتاب) خانهٔ کنار جعبهٔ اوستایی کشیده شده اما یکسره سفید مانده است؛ نه نام زبان دارد، نه ارجاع، نه واژه. استخراج داده‌ها امین بوده و چیزی برای راستی‌آزمایی وجود ندارد. به قرینهٔ چیدمان دیگر نمودارها، این خانه جای بازتاب فارسیِ همین ریشه بوده که نویسنده آن را پر نکرده است.\",\n      \"sources\":[],\n      \"ref_check\":[{\"ref\":\"None\",\"status\":\"not_found\",\"note\":\"the node carries no reference in the book.\"}],\n      \"consulted\":[\n        {\"src\":\"POK\",\"where\":\"pp. 440-441\",\"stance\":\"silent\",\"note\":\"Pokorny's ĝher- entry lists no New Persian continuant that could fill the box.\"},\n        {\"src\":\"HRN\",\"where\":\"HRN.txt (Horn, Grundriss)\",\"stance\":\"silent\",\"note\":\"nothing to look up: the box is blank on the printed page.\"}]})\n\n    nodes.append({\n      \"id\":3,\"lang\":\"Germanic\",\"words\":\"gernjan; grěduz\",\"verdict\":\"confirmed\",\n      \"derivation\":\"Both Germanic forms are Watkins' own: *gernjan (suffixed *ǵʰer-n-) in OE giernan/gyrnan 'to strive, desire', Gothic gairnjan; and *grēduz 'hunger' (extended *ǵʰrē-), with derived *grēdagaz 'hungry' in OE grǣdig, Gothic grēdags. Pokorny 441 lists the same set: \\\"got. faihu-gairns ,geldgierig', aisl. gjarn, ags. georn ... Denom. got. gairnjan, aisl. girna, ags. giernan ,begehren'\\\". The macron in the book's grěduz is a breve for the long ē of *grēduz — a typographic slip of no consequence.\",\n      \"derivation_fa\":\"هر دو صورت ژرمنی از واتکینز گرفته شده‌اند: *gernjan (ساختِ پسوندیِ *ǵʰer-n-) در giernan انگلیسی باستان «کوشیدن، خواستن» و gairnjan گوتی؛ و *grēduz «گرسنگی» (گسترشِ *ǵʰrē-) با صفتِ *grēdagaz «گرسنه» در grǣdig انگلیسی باستان. پوکورنی در ص ۴۴۱ همین مجموعه را می‌آورد. علامت کوتاهیِ واکه در «grěduz» کتاب باید کشیده (ē) می‌بود؛ لغزش حروف‌چینی است و بی‌اثر. ادعای نورایی درست است.\",\n      \"sources\":[E+\"yearn\"],\n      \"ref_check\":[{\"ref\":\"AHD\",\"status\":\"supports\",\"note\":\"Watkins 1985 s.v. gher-5: \\\"1. Suffixed form *gher-n- in Germanic *gernjan in Old English giernan, gyrnan ... YEARN. 2. Extended form *ghré- possibly in: a. Germanic *gréduz, hunger, forming *grédagaz, hungry ... GREEDY.\\\"\"}],\n      \"consulted\":[\n        {\"src\":\"POK\",\"where\":\"p. 441 (POK_02 leaf 97)\",\"stance\":\"supports\",\"note\":\"\\\"got. faihu-gairns ,geldgierig', aisl. gjarn, ags. georn ,wozu geneigt' ... Denom. got. gairnjan, aisl. girna, ags. giernan ,begehren'\\\"\"},\n        {\"src\":\"KLN\",\"where\":\"KLN_1966 s.v. greedy (line 16653)\",\"stance\":\"supports\",\"note\":\"\\\"OE. grǣdig, rel. to OS. gradag, ON. gradr, 'greed, hunger' ... Goth. gredus, 'hunger', gredags, 'hungry'\\\"\"},\n        {\"src\":\"WLD\",\"where\":\"Bd. I (WLD_Bd1 line 39868)\",\"stance\":\"supports\",\"note\":\"\\\"„Hunger“ von ai. gardha-ḥ in der Vokalstellung ab (s. u. gher- „begehren“)\\\" — Walde-Pokorny files the 'hunger' word under gher- 'begehren'.\"}]})\n\n    nodes.append({\n      \"id\":4,\"lang\":\"English\",\"words\":\"yearn; greed, greedy\",\"verdict\":\"confirmed\",\n      \"derivation\":\"OE giernan > ME yernen > yearn (the initial g- before a front vowel palatalised to /j/ in Old English, spelled y- from Middle English on). Greedy is OE grǣdig < *grēdagaz; the noun greed is a 17th-century back-formation from greedy (first recorded 1609), which is why the chart's 'greed, greedy' pair is right only in that order of derivation. Etymonline: \\\"yearn ... from Old English giernan ... from Proto-Germanic *gernjan, from PIE root *gher- (2) 'to like, want'.\\\"\",\n      \"derivation_fa\":\"giernan انگلیسی باستان از راه yernen انگلیسی میانه به yearn رسیده است؛ «گ» آغازین پیش از واکهٔ پیشین در انگلیسی باستان کامی شده و به /j/ بدل گشته و از انگلیسی میانه با y نوشته می‌شود. greedy از grǣdig انگلیسی باستان است و اسمِ greed اشتقاق معکوس از آن در سدهٔ هفدهم (نخستین ثبت ۱۶۰۹ م). اتیمانلاین همین زنجیره را می‌آورد؛ ادعای نورایی درست است.\",\n      \"sources\":[E+\"yearn\"],\n      \"ref_check\":[{\"ref\":\"AHD\",\"status\":\"supports\",\"note\":\"Watkins 1985 s.v. gher-5 lists YEARN and GREEDY under the root.\"}],\n      \"consulted\":[\n        {\"src\":\"KLN\",\"where\":\"KLN_1971 s.v. yearn\",\"stance\":\"supports\",\"note\":\"\\\"ME. yernen, fr. OE. geornan, giernan, gernan, fr. georn, 'desirous' ... Goth. gairnjan, 'to desire'\\\"\"},\n        {\"src\":\"KLN\",\"where\":\"KLN_1966 s.v. greedy\",\"stance\":\"supports\",\"note\":\"\\\"ME. gredy, fr. OE. grǣdig ... Goth. gredus, 'hunger'\\\"\"}]})\n\n    nodes.append({\n      \"id\":5,\"lang\":\"Latin\",\"words\":\"hortârî\",\"verdict\":\"confirmed\",\n      \"derivation\":\"Latin hortārī 'to urge, encourage' is the frequentative/intensive of the older horior 'I urge' (< zero-grade *ǵʰr̥-i-, with the regular Latin change of PIE *ǵʰ- to h- initially). Ernout-Meillet: \\\"horior et hortor ... hortari: proprement 'faire vouloir', d'où 'exhorter, encourager'\\\" — literally 'to make (someone) want', which is exactly the semantics required by the root 'to wish, desire'. Watkins reconstructs \\\"suffixed zero-grade form *ghr-to-\\\".\",\n      \"derivation_fa\":\"لاتینی hortārī «برانگیختن، تشویق کردن» صورت تکراری/تشدیدیِ فعل کهن‌تر horior است (از پایهٔ صفرِ *ǵʰr̥-i-)، با این دگرگونی منظم که *ǵʰ آغازینِ هندواروپایی در لاتین به h بدل می‌شود. ارنو-میه می‌نویسد hortari در اصل یعنی «خواستاندن، به خواستن واداشتن» و از آنجا «تشویق کردن»، که دقیقاً همان معنایی است که ریشهٔ «خواستن» ایجاب می‌کند. ادعای نورایی درست است.\",\n      \"sources\":[E+\"exhort\"],\n      \"ref_check\":[{\"ref\":\"AHD\",\"status\":\"supports\",\"note\":\"Watkins 1985 s.v. gher-5 §3: \\\"Suffixed zero-grade form *ghr-to- in Latin hortari, to urge on, encourage (< 'to cause to strive or desire'): HORTATIVE; EXHORT.\\\"\"}],\n      \"consulted\":[\n        {\"src\":\"LAT\",\"where\":\"Ernout-Meillet, LAT.txt lines 28443-28444\",\"stance\":\"supports\",\"note\":\"\\\"horior et hortor (horitor et horto, arch.), -aris, hortatus sum, hortari: proprement 'faire vouloir', d'où 'exhorter, encourager'.\\\"\"},\n        {\"src\":\"POK\",\"where\":\"pp. 440-441\",\"stance\":\"supports\",\"note\":\"the ĝher- 'begehren' entry is the same root Ernout-Meillet's 'faire vouloir' presupposes.\"}]})\n\n    nodes.append({\n      \"id\":6,\"lang\":\"English\",\"words\":\"exhort\",\"verdict\":\"confirmed\",\n      \"derivation\":\"English exhort (c. 1400, exhorten) is from Latin exhortārī 'to encourage thoroughly' (ex- intensive + hortārī), partly through Old French exhorter; a purely learned, bookish borrowing, with no sound change to speak of beyond the Anglicisation of the infinitive.\",\n      \"derivation_fa\":\"exhort انگلیسی (نخستین ثبت حدود ۱۴۰۰ م به صورت exhorten) از exhortārī لاتینی «سخت برانگیختن» است (پیشوند تشدیدیِ ex- + hortārī)، تا حدی از راه exhorter فرانسوی کهن؛ وام‌واژه‌ای کتابی و عالمانه است و جز انگلیسی‌سازی مصدر، دگرگونی آوایی چشمگیری ندارد. ادعای نورایی درست است.\",\n      \"sources\":[E+\"exhort\"],\n      \"ref_check\":[{\"ref\":\"AHD\",\"status\":\"supports\",\"note\":\"Watkins 1985 s.v. gher-5 §3 lists EXHORT.\"}],\n      \"consulted\":[\n        {\"src\":\"KLN\",\"where\":\"KLN_1971 s.v. exhort\",\"stance\":\"supports\",\"note\":\"\\\"ME. exhorten, fr. L. exhortari, 'to exhort, encourage, stimulate', fr. 1st ex- and hortari, 'to incite, encourage, urge'.\\\"\"},\n        {\"src\":\"LAT\",\"where\":\"Ernout-Meillet s.v. horior/hortor\",\"stance\":\"supports\",\"note\":\"the compound ex-hortari is listed under the same head.\"}]})\n\n    nodes.append({\n      \"id\":7,\"lang\":\"Greek\",\"words\":\"khoris. xoris\",\"verdict\":\"transcription_suspect\",\n      \"derivation\":\"The Greek word for 'grace' is χάρις (kháris), gen. χάριτος, not *khoris. The printed page (pdf p. 189, image kept at data/verification/sources/refs/ocr/BOOK/189.png) really does read \\\"khoris. xoris : grace\\\", so the extraction is faithful and the error is the book's: elsewhere Nourai writes the Greek letter khi as x and adds a Latin transcription, so the box should read \\\"kharis, xaris\\\". χάρις (< *ǵʰr̥-i-) belongs exactly where the chart puts it — Pokorny 440-441 lists \\\"gr. χαίρω, χάρις f. ,Anmut, Gunst', χαρά ,Freude'\\\" under ĝher- 'begehren', and Watkins gher-5 §4 has \\\"Suffixed zero-grade form *ghr-i- in Greek kharis, grace, favor: CHARISMA\\\". Note also that Greek χωρίς (khōrís) 'apart, separately' is a real but wholly unrelated word, so the misprint is a genuinely misleading one.\",\n      \"derivation_fa\":\"واژهٔ یونانیِ «فیض، لطف» χάρις (kháris) است، نه *khoris. تصویر صفحهٔ چاپی نشان می‌دهد که کتاب واقعاً «khoris. xoris : grace» چاپ کرده است؛ پس خطا از خوانش اسکن نیست بلکه غلط چاپیِ خودِ کتاب است و صورت درست «kharis, xaris» است (نورایی حرف χ را x می‌نویسد و در کنارش آوانگاشت لاتین می‌آورد). خودِ χάρις (از *ǵʰr̥-i-) درست همان‌جاست که نمودار نشانده: پوکورنی در صص ۴۴۰–۴۴۱ آن را ذیل ĝher- «خواستن» آورده و واتکینز نیز ذیل gher-5. نکتهٔ گمراه‌کننده آنکه χωρίς یونانی واژه‌ای واقعی اما یکسره بی‌ربط («جدا، جداگانه») است.\",\n      \"error_in\":\"book\",\"book_prints\":\"khoris. xoris\",\"correct_form\":\"kharis, xaris (Greek χάρις)\",\n      \"sources\":[E+\"charisma\"],\n      \"ref_check\":[{\"ref\":\"AHD\",\"status\":\"supports\",\"note\":\"Watkins 1985 s.v. gher-5 §4: \\\"Suffixed zero-grade form *ghr-i- in Greek kharis, grace, favor: CHARISMA; EUCHARIST.\\\" — Watkins spells it kharis, confirming the misprint.\"}],\n      \"consulted\":[\n        {\"src\":\"POK\",\"where\":\"pp. 440-441 (POK_02 leaf 97)\",\"stance\":\"supports\",\"note\":\"\\\"gr. χαίρω (*χαρι-ω), χάρη-μα ,sich freuen', χάρις f. ,Anmut, Gunst', χαρά ,Freude'\\\" — under 1. ĝher- ,begehren, gern haben'.\"},\n        {\"src\":\"WLD\",\"where\":\"Bd. I (WLD_Bd1 line 37876)\",\"stance\":\"supports\",\"note\":\"\\\"...freude blitzend\\\" zu *gher- „begehren, gern haben\\\" (s. d.)\\\" — Walde-Pokorny puts the χαρ- family under this root.\"}]})\n\n    nodes.append({\n      \"id\":8,\"lang\":\"English\",\"words\":\"charisma, charismatic\",\"verdict\":\"confirmed\",\n      \"derivation\":\"English charisma (1875) is a Latinised form of Greek χάρισμα 'favour, divine gift', from χαρίζεσθαι 'to show favour', from χάρις; it entered English through the Pauline epistles' vocabulary of spiritual gifts, and acquired the modern 'gift of leadership' sense from Max Weber's Wirtschaft und Gesellschaft (1922), in English from c. 1930; charismatic follows (1851 in theology). So the Greek→English arrow is right, once the Greek form is corrected to kharis (node 7).\",\n      \"derivation_fa\":\"charisma انگلیسی (۱۸۷۵ م) صورت لاتینی‌شدهٔ χάρισμα یونانی «موهبت، بخشش الهی» است، از χαρίζεσθαι «لطف کردن» و آن از χάρις؛ از راه اصطلاح‌های عهد جدید دربارهٔ مواهب روحانی وارد انگلیسی شد و معنی امروزیِ «جاذبهٔ رهبری» را از ماکس وبر (۱۹۲۲ م) گرفت که از حدود ۱۹۳۰ م در انگلیسی رواج یافت. پس پیکان «یونانی ← انگلیسی» درست است، به شرط آنکه صورت یونانی به kharis اصلاح شود.\",\n      \"sources\":[E+\"charisma\"],\n      \"ref_check\":[{\"ref\":\"AHD\",\"status\":\"supports\",\"note\":\"Watkins 1985 s.v. gher-5 §4 lists CHARISMA (and EUCHARIST) from Greek kharis.\"}],\n      \"consulted\":[\n        {\"src\":\"KLN\",\"where\":\"KLN_1966/1971, grep '^charisma'\",\"stance\":\"silent\",\"note\":\"Klein has no charisma entry in either scan (the word was still rare in 1966).\"},\n        {\"src\":\"POK\",\"where\":\"pp. 440-441\",\"stance\":\"supports\",\"note\":\"χάρις is listed there, the base of χάρισμα.\"}]})\n\n    return {\n      \"entry\":1,\n      \"root\":\"Gher 4\",\n      \"verdict\":\"confirmed\",\n      \"modern_form\":\"PIE *ǵʰer- 'to like, want, desire' (Pokorny 1. ĝher- 440)\",\n      \"note\":\"Exactly right, and the reference is exact too: Pokorny pp. 440-441 head \\\"1. ĝher- ,begehren, gern haben'\\\" and give in order the very witnesses of this chart — Skt. háryati, Av. zara- 'Streben, Ziel', Gk. χαίρω/χάρις, Goth. gairnjan/OE giernan; Latin hortārī is added by Watkins (gher-5 §3). The root is the palatal *ǵʰ- one, distinct from the *gʰer- of the previous entry, which Nourai's 'Gher 3 / Gher 4' numbering keeps apart correctly. The only defect on the chart is the misprint khoris for kharis (node 7) and the blank box (node 2).\",\n      \"note_fa\":\"این جعبهٔ ریشه یکسره درست است و ارجاع آن هم دقیق: پوکورنی در صص ۴۴۰–۴۴۱ مدخل «۱. ĝher- خواستن، خوش داشتن» را دارد و به همین ترتیب گواهانِ همین نمودار را می‌آورد: háryati سنسکریت، zara- اوستایی «کوشش، آماج»، χαίρω و χάρις یونانی، و gairnjan گوتی؛ hortārī لاتینی را واتکینز افزوده است. این ریشه با *gʰer- مدخل پیشین فرق دارد (کامی در برابر ساده) و شماره‌گذاری «Gher 3 / Gher 4» نورایی همین تمایز را درست نگه داشته است. تنها عیب‌های نمودار، غلط چاپیِ khoris به‌جای kharis (گرهٔ ۷) و جعبهٔ سفید (گرهٔ ۲) است.\",\n      \"sources\":[E+\"charisma\", E+\"exhort\"],\n      \"ref_check\":[{\"ref\":\"POK:440\",\"status\":\"supports\",\"note\":\"POK_02 leaf 97 (printed pp. 440-441): \\\"1. ĝher- ,begehren, gern haben', z. T. mit Formen von einer Basis *ghere(i)- : gheri- ... Ai. háryati ,findet Gefallen, begehrt'; av. zara- m. ,Streben, Ziel'; gr. χαίρω ... χάρις f. ,Anmut, Gunst' ... got. gairnjan, aisl. girna, ags. giernan ,begehren'.\\\"\"}],\n      \"consulted\":[\n        {\"src\":\"AHD\",\"where\":\"Watkins 1985 s.v. gher-5\",\"stance\":\"supports\",\"note\":\"\\\"gher-5. To like, want. ... [Pok. 1. gher- 440.]\\\" — same root, same page.\"},\n        {\"src\":\"WLD\",\"where\":\"Bd. I (WLD_Bd1 lines 37876, 39868)\",\"stance\":\"supports\",\"note\":\"Walde-Pokorny refers the χαρ- words and the 'hunger' word to *gher- „begehren, gern haben\\\".\"},\n        {\"src\":\"POK\",\"where\":\"pp. 440-441\",\"stance\":\"supports\",\"note\":\"see ref_check.\"}]}\n\ndoc = {\"pdf_page\":189,\"book_page\":159,\"verified_by\":\"claude-opus-5\",\"verified_on\":\"2026-09-05\",\n       \"entries\":[ent0(), ent1()]}\nwith io.open(\"/home/sfmqrb/git/rishe/data/verification/page-189.json\",\"w\",encoding=\"utf-8\") as f:\n    json.dump(doc,f,ensure_ascii=False,indent=2)\n    f.write(\"\\n\")\nprint(\"ok\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build189.py && python3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-189.json > /dev/null && echo JSON_OK && python3 /home/sfmqrb/git/rishe/tools/verify_check.py 189"
}
```


### [2026-09-05T21:18:14.291Z] TOOL RESULT

```
Exit code 1
ok
JSON_OK
nodes verified: 19/27
node verdicts: {'disputed': 3, 'confirmed': 10, 'plausible': 5, 'transcription_suspect': 1}
root verdicts: {'confirmed': 2}
ref checks: {'not_checked': 8, 'supports': 7, 'partial': 4}
books consulted: {'partial': 9, 'contradicts': 4, 'silent': 12, 'supports': 19} | by book: {'KLN': 15, 'POK': 7, 'AHD': 5, 'SKT': 4, 'MON': 3, 'BQT': 3, 'ARY': 2, 'LKT': 1, 'WEB': 1, 'WLD': 1, 'FSD': 1, 'IEC': 1}
PROBLEM: page 189: entry 1 (Gher 4) node #1 missing
PROBLEM: page 189: entry 1 (Gher 4) node #2 missing
PROBLEM: page 189: entry 1 (Gher 4) node #3 missing
PROBLEM: page 189: entry 1 (Gher 4) node #4 missing
PROBLEM: page 189: entry 1 (Gher 4) node #5 missing
PROBLEM: page 189: entry 1 (Gher 4) node #6 missing
PROBLEM: page 189: entry 1 (Gher 4) node #7 missing
PROBLEM: page 189: entry 1 (Gher 4) node #8 missing
```


## [2026-09-05T21:18:14.751Z] AGENT

You've hit your session limit · resets 7:40pm (America/Toronto)


## [2026-09-06T02:13:08.165Z] INPUT

The coordinator sent a message while you were working:
You were cut off by a rate limit while writing /home/sfmqrb/git/rishe/data/verification/page-189.json: it currently covers only 19 of 27 nodes and `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 189` prints 8 PROBLEM lines. Please complete the file (all nodes, all fields per AGENT_INSTRUCTIONS.md), re-run verify_check.py 189 until it shows 0 PROBLEM lines, and reply with the short summary described in the instructions.

Address this before completing your current task.


## [2026-09-06T02:13:13.111Z] AGENT

The entry-1 dict was returned without its `nodes` key. Fixing.


## [2026-09-06T02:13:16.148Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && python3 - <<'EOF'\np='build189.py'\ns=open(p,encoding='utf-8').read()\nold='''        {\"src\":\"POK\",\"where\":\"pp. 440-441\",\"stance\":\"supports\",\"note\":\"see ref_check.\"}]}\n\ndoc'''\nnew='''        {\"src\":\"POK\",\"where\":\"pp. 440-441\",\"stance\":\"supports\",\"note\":\"see ref_check.\"}],\n      \"nodes\":nodes}\n\ndoc'''\nassert s.count(old)==1\nopen(p,'w',encoding='utf-8').write(s.replace(old,new))\nprint('patched')\nEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build189.py && python3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-189.json > /dev/null && echo JSON_OK && python3 /home/sfmqrb/git/rishe/tools/verify_check.py 189"
}
```


### [2026-09-06T02:13:19.264Z] TOOL RESULT

```
patched
ok
JSON_OK
nodes verified: 27/27
node verdicts: {'disputed': 3, 'confirmed': 16, 'plausible': 5, 'transcription_suspect': 2, 'unverified': 1}
root verdicts: {'confirmed': 2}
ref checks: {'not_checked': 8, 'supports': 14, 'partial': 4, 'not_found': 1}
books consulted: {'partial': 9, 'contradicts': 4, 'silent': 16, 'supports': 33} | by book: {'KLN': 20, 'POK': 13, 'AHD': 5, 'SKT': 4, 'MON': 3, 'BQT': 3, 'WLD': 3, 'ARY': 2, 'LAT': 2, 'LKT': 1, 'WEB': 1, 'FSD': 1, 'IEC': 1, 'BRT': 1, 'KNT': 1, 'HRN': 1}
```


## [2026-09-06T02:13:24.713Z] TOOL CALL #52: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/page-189.json'))\nbad=[]\nfor e in d['entries']:\n    for k in ['note','note_fa','verdict','ref_check','consulted','sources']:\n        if not e.get(k) and k!='sources': bad.append(('entry',e['entry'],k))\n    for n in e['nodes']:\n        for k in ['derivation','derivation_fa','verdict','ref_check','consulted']:\n            if not n.get(k): bad.append((e['entry'],n['id'],k))\n        if len(n['consulted'])<2: bad.append((e['entry'],n['id'],'consulted<2'))\nprint('issues:',bad)\nprint('nodes:',sum(len(e['nodes']) for e in d['entries']))\n\""
}
```


### [2026-09-06T02:13:26.389Z] TOOL RESULT

```
issues: []
nodes: 27
```


## [2026-09-06T02:13:45.400Z] AGENT

Page 189 (book p. 159) verified — `verify_check.py 189`: 27/27 nodes, **0 PROBLEM lines**.

**Verdicts** — roots: 2 confirmed. Nodes: 16 confirmed, 5 plausible, 3 disputed, 2 transcription_suspect, 1 unverified.

**Disputed**
- Gher 3 #1 Sanskrit `ghat` — Watkins himself says "perhaps (but unlikely)"; Klein/Etymonline: ghaṭṭa "landing place", origin unknown (likely non-Indo-Aryan). The gloss "place where sins are wiped away, a shrine" is Shipley's paraphrase, not the word's meaning.
- Gher 3 #6 Old French `cresme` — the page's real error. OF cresme is a blend of Eccles. Latin *chrisma* (< Gk χρῖσμα) and Gaulish *crama* (Klein s.v. cream; Skeat; Etymonline), **not** from Turkish. Nourai's "Turkish xorozma" node (#5, graded plausible) comes from Klein s.v. *rusma* — "It. and F., a corruption of Turk. khorozma, inexact transliteration of Gk. χρῖσμα" — i.e. a later parallel loan that gave It./Fr. *rusma*, not the ancestor of a 13th-c. French word.
- Gher 3 #14 Greek `kharax` — Pokorny puts χάραξ/χαράσσω in a separate, query-marked root on p. 441, not the 439/457 root of this chart; Beekes calls χάραξ "most probably Pre-Greek" and Klein derives χαράσσειν from Semitic (Heb. ḥārash).

**Transcription_suspect** (both `error_in: book`; extraction is faithful, checked against a 300-dpi render, copied to `data/verification/sources/refs/ocr/BOOK/189.png`)
- Gher 3 #12 Persian: book prints «کرموزُم» for *koromosom*; correct spelling is کروموزوم (so Mo'in's own text); the transliteration with -s- also mismatches the ز.
- Gher 4 #7 Greek: book prints "khoris. xoris : grace"; the word is χάρις *kharis* (Pokorny 440-441; Watkins gher-5 §4). χωρίς is a real but unrelated word, so the misprint misleads.

**Other notes**: Gher 4 node #2 is a genuinely blank box on the printed page (unverified — nothing to check). Root refs check out (POK 439 = "2. gher- … reiben"; POK 457 = ghrei-; POK 440 = ĝher- "begehren", with Av. *zara-* "Streben, Ziel" as Bartholomae has it), except that the Ghreu material (χρώς, *grautaz, *graw) sits on Pokorny 460-461, not 457.

**No extraction errors found** — the JSON matches the printed page everywhere, including the empty box and the odd Persian script. OEW:120 (Shipley) and VOP:280/281 (Moshiri) are unobtainable (lending-only / no copy exists), so those 8 ref_checks are `not_checked`; 14 supports, 4 partial, 1 not_found. 15 web pages archived via fetch_source.py.
