# Verification process log — verify-page-92


## [2026-09-05T14:05:00.004Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 92 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-92.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-92.json. Write /home/sfmqrb/git/rishe/data/verification/page-92.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 92` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-05T14:05:01.738Z] AGENT

I'll start by reading the instructions.


## [2026-09-05T14:05:02.445Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-05T14:05:02.465Z] TOOL RESULT

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


## [2026-09-05T14:05:02.775Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-92.txt"
}
```


### [2026-09-05T14:05:02.824Z] TOOL RESULT

```
1	=== PDF page 92 (book page 62) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Bhergh : high  (refs POK:140)  PART 1
4	#1 (parent #0) [Avestan] refs=POK:140; KLN:188; KNT:200; VDQ:36; MAG:181 | berez 1, berezi, berezra, barš, bareš, berezant, barzman : high ; barz-ahva : higher world ☞An 1
5	#2 (parent #0) [Persian] refs=KLN:148; BQT:254,256,300; FSF:78; VDQ:36 | borz «بُرز» : tall, tallness ; barzax «برزخ» : middle stage (above hell) ; barzoy «برزوی ، بروزیه» : "great", a name ; Farîborz «فریبرز» : "with elegant height", a male name ☞Sâwel
6	#3 (parent #0) [Persian] refs=KLN:148; BQT:254,256,300; FSF:78 | boland «بلند» : high ; bâlâ «بالا» : up, above ; bâlâ-xâneh «بالاخانه» : balcony ☞Gwhen 1
7	  #4 (parent #3) [Italian] refs=LKT:17 | barbacane : a watch room on castle wall ; balcone : balcony | NOTE: AHD derives these words from other roots
8	    #5 (parent #4) [French] refs=PHN:55 | balcon
9	      #6 (parent #5) [Persian] refs=MON:467 | bâlkon «بالکن»
10	    #7 (parent #4) [English] refs=KLN:148; LKT:17 | barbican, balcony
11	#8 (parent #0) [Avestan] refs=SOD:1 | bereg, â-bereg : high, desirable
12	  #9 (parent #8) [Pahlavi] refs=SOD:1 | âwarzog, âzôk : wish, hope
13	    #10 (parent #9) [Persian] refs=BQT; MON:42 | ârezŭ «آرزو» : hope, wish | extra: آرزومند
14	#11 (parent #0) [Avestan] refs=SOD:104 | bareša : high on top (of a horse neck), mane
15	  #12 (parent #11) [Sogdian] refs=SOD:104 | bnš : mane
16	    #13 (parent #12) [Persian] refs=SOD:140 | faš «فَش» : mane | extra: بَش ، پَش
17	#14 (parent #0) [Sogdian] refs=SOD:1 | â-brxsy : wish
18	#15 (parent #0) [Old Persian] refs=KNT:200,201 | bard- : to be high or tall ; Bardiya : the glorified (person) ; baršan : height, depth ; braz : prayer
19	  #16 (parent #15) [Persian] refs=FSF:79; KNT:200 | Bardiyeh «بردیه» : "great, tall", a historic male name ; barmaneš «برمنش» : with high manners and thoughts ; bar 2 «بَر ٢» : high ☞Upo | extra: برتر ، برترین ، برین | NOTE: See root "Upo" for another derivation.
20	
```


## [2026-09-05T14:05:05.743Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-92.json",
 "description": "Read source JSON page 92"
}
```


### [2026-09-05T14:05:05.781Z] TOOL RESULT

```
{
  "pdf_page": 92,
  "book_page": 62,
  "entries": [
    {
      "root": {
        "name": "Bhergh",
        "lang": "Indo-European",
        "refs": "POK:140",
        "gloss": "high"
      },
      "part": 1,
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:140; KLN:188; KNT:200; VDQ:36; MAG:181",
          "words": [
            {"translit": "berez 1, berezi, berezra, barš, bareš, berezant, barzman", "gloss": "high", "script": null},
            {"translit": "barz-ahva", "gloss": "higher world", "script": null, "see": ["An 1"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 0,
          "lang": "Persian",
          "refs": "KLN:148; BQT:254,256,300; FSF:78; VDQ:36",
          "words": [
            {"translit": "borz", "gloss": "tall, tallness", "script": "بُرز"},
            {"translit": "barzax", "gloss": "middle stage (above hell)", "script": "برزخ"},
            {"translit": "barzoy", "gloss": "\"great\", a name", "script": "برزوی ، بروزیه"},
            {"translit": "Farîborz", "gloss": "\"with elegant height\", a male name", "script": "فریبرز", "see": ["Sâwel"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "نه کوهست ازاین برزتر در جهان - نه یاقوت دارد جز اینجای کان",
            "poet": "Asadî"
          }
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Persian",
          "refs": "KLN:148; BQT:254,256,300; FSF:78",
          "words": [
            {"translit": "boland", "gloss": "high", "script": "بلند"},
            {"translit": "bâlâ", "gloss": "up, above", "script": "بالا"},
            {"translit": "bâlâ-xâneh", "gloss": "balcony", "script": "بالاخانه", "see": ["Gwhen 1"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Italian",
          "refs": "LKT:17",
          "words": [
            {"translit": "barbacane", "gloss": "a watch room on castle wall", "script": null},
            {"translit": "balcone", "gloss": "balcony", "script": null}
          ],
          "script_extra": null,
          "note": "AHD derives these words from other roots",
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "French",
          "refs": "PHN:55",
          "words": [
            {"translit": "balcon", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "Persian",
          "refs": "MON:467",
          "words": [
            {"translit": "bâlkon", "gloss": null, "script": "بالکن"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 4,
          "lang": "English",
          "refs": "KLN:148; LKT:17",
          "words": [
            {"translit": "barbican, balcony", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 0,
          "lang": "Avestan",
          "refs": "SOD:1",
          "words": [
            {"translit": "bereg, â-bereg", "gloss": "high, desirable", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "Pahlavi",
          "refs": "SOD:1",
          "words": [
            {"translit": "âwarzog, âzôk", "gloss": "wish, hope", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 9,
          "lang": "Persian",
          "refs": "BQT; MON:42",
          "words": [
            {"translit": "ârezŭ", "gloss": "hope, wish", "script": "آرزو"}
          ],
          "script_extra": "آرزومند",
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 0,
          "lang": "Avestan",
          "refs": "SOD:104",
          "words": [
            {"translit": "bareša", "gloss": "high on top (of a horse neck), mane", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 11,
          "lang": "Sogdian",
          "refs": "SOD:104",
          "words": [
            {"translit": "bnš", "gloss": "mane", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 13,
          "parent": 12,
          "lang": "Persian",
          "refs": "SOD:140",
          "words": [
            {"translit": "faš", "gloss": "mane", "script": "فَش"}
          ],
          "script_extra": "بَش ، پَش",
          "note": null,
          "quote": {
            "text": "بَش و یال اسبان کران تا کران - براندوده بر مُشت و بر زعفران",
            "poet": "Ferdowsî"
          }
        },
        {
          "id": 14,
          "parent": 0,
          "lang": "Sogdian",
          "refs": "SOD:1",
          "words": [
            {"translit": "â-brxsy", "gloss": "wish", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 15,
          "parent": 0,
          "lang": "Old Persian",
          "refs": "KNT:200,201",
          "words": [
            {"translit": "bard-", "gloss": "to be high or tall", "script": null},
            {"translit": "Bardiya", "gloss": "the glorified (person)", "script": null},
            {"translit": "baršan", "gloss": "height, depth", "script": null},
            {"translit": "braz", "gloss": "prayer", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 16,
          "parent": 15,
          "lang": "Persian",
          "refs": "FSF:79; KNT:200",
          "words": [
            {"translit": "Bardiyeh", "gloss": "\"great, tall\", a historic male name", "script": "بردیه"},
            {"translit": "barmaneš", "gloss": "with high manners and thoughts", "script": "برمنش"},
            {"translit": "bar 2", "gloss": "high", "script": "بَر ٢", "see": ["Upo"]}
          ],
          "script_extra": "برتر ، برترین ، برین",
          "note": "See root \"Upo\" for another derivation.",
          "quote": {
            "text": "ازاین دخت مهراب واز پورسام - گوی برمنش زاید و نیکنام",
            "poet": "Ferdowsî"
          }
        }
      ]
    }
  ]
}
```


## [2026-09-05T14:05:06.491Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-05T14:05:06.531Z] TOOL RESULT

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


## [2026-09-05T14:05:11.534Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','KLN','KNT','VDQ','MAG','BQT','FSF','LKT','PHN','MON','SOD','AHD','WLD','BRT','PHD','NYB','HRN','HUB','IEC','SYN','SKT','ARY']:\n    v=d.get(k)\n    print('==',k,json.dumps(v,ensure_ascii=False)[:700])\n\""
}
```


### [2026-09-05T14:05:13.801Z] TOOL RESULT

```
== POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index 
== KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt", "page_offset": "KLN_1966: TWO pri
== KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt", "page_offset": "leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archiv
== VDQ {"title": "Fereydun Badreh'i (tr.), Vazheha-ye Dakhil dar Qor'an-e Majid (Persian translation of Jeffery FVQ with notes), Toos 1372/1993", "kind": "website", "url": "https://noorlib.ir/book/view/12868?pageNumber=<N>&viewType=pdf (page images; viewType=html also exists) ; info: https://noorlib.ir/book/info/12868 ; ketabnak.com/book/51136 (download blocked)", "lookup_hint": "noorlib viewer is JavaScript-rendered (WebFetch/curl get only the site chrome); needs a browser. Since it is a translation of FVQ, verify the substance via FVQ (same entry order); page numbers differ.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "Not on archive.org. Also on ghaemiyeh (ghboo
== MAG {"title": "G. Widengren, Muhammad, the Apostle of God, and his Ascension (King and Saviour V), Uppsala 1955, ch. VIII 'Iranian elements in the Kuranic vocabulary'", "edition_found": null, "kind": "archive_restricted", "url": "https://archive.org/details/muhammadapostled0000geow (1955, lending) ; HathiTrust pst.000011130420 search-only", "identifier": null, "local_file": null, "page_offset": null, "lookup_hint": "HathiTrust has it search-only (limited view); Google Books ids -r4rAAAAIAAJ / h20wAAAAYAAJ are snippet view.", "notes": "RE-SEARCH 2026-09: borrowable only; not in DiVA; Google no view."}
== BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.c
== FSF {"title": "Abdolhossein Noushin, Vazhe-namak: Farhang-e Vazheha-ye Doshvar-e Shahnameh (Farhang-e Shahnameh), Donya 1363/1984", "kind": "archive_djvu", "url": "https://archive.org/details/20220809_20220809_1444", "lookup_hint": "grep the headword in FSF_pages.txt (alphabetical glossary); use inside.php search for leaf numbers. Also https://archive.org/details/nooshinshahnameh is a different Noushin book (گزارشی چند درباره شاهنامه).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF.txt"], "page_offset": "484 leaves; edition/printing of this scan not identified — determine offset from printed page 
== LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Numbered entries: 'NNNN. word (language) meaning' - Lokotsch is usually cited by entry number, but Nourai cites pages.
== PHN {"title": "A. P. Pihan, Dictionnaire étymologique des mots de la langue française dérivés de l'arabe, du persan ou du turc, Paris 1866", "edition_found": "1866", "kind": "archive_djvu", "url": "https://archive.org/details/dictionnairetym01pihagoog", "identifier": "dictionnairetym01pihagoog (others: bub_gb_QnsSAAAAIAAJ, dictionnairetym00pihagoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHN.txt", "page_offset": "leaf = printed + 31 (e.g. leaf 33 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "French headword in caps at line start;
== MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol 
== SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get s
== AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only", "identifie
== WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.39015066210397 (browser only from this host)", "identifier": "in.gov.ignca.20339 (Band 3); also in.ernet.dli.2015
== BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \\f between 
== PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<ident
== NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Nourai's 'NYB' nu
== HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or grep the 
== HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by parag
== IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Reconstruct
== SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<i
== SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<i
== ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY:<printed page> --image", "local_file": ["/home/sfmqrb/git/rishe/
```


## [2026-09-05T14:05:17.933Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==149' POK_01.txt | head -80"
}
```


## [2026-09-05T14:05:18.650Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"bhereg\" POK_full.txt | head -30"
}
```


### [2026-09-05T14:05:19.612Z] TOOL RESULT

```
reien (von  der  Dohle)',  fring{u)illa  ,Fink,  Sperling';
russ.  berglez  ,Stieglitz',   skr.   brglijez  ,Sitta    syriaca',   cech.  brhel  ,Pirol/   ^ Goldamsel',  mähr.  ,Specht',  poln.  bargiel  ,Bergmeise'.  ^
i
139
Vi  «liehe    aber  gewiß  jüngere  Schallvvorte  sind  lat.  mendus  frindit,  lit. Ijrr-gUi  .blöken,  meckern,  brummend ^yp.  II171f,  WH.  1548.
-  bbreg-  ^glänzen,  weiß^,  wozu  auch  der  Birkenname  N.  Sg.  *bherQg'S, Q^  So".  *bherdgös.  Gleichwertig  mit  hlierik-,  s.  d.
ni  hhräjate  .glänzt,  strahlt^;  apers.  hräzaiti  ds.  (*hhreyö),  npers.  barä- zidan  ^ghänzen',  haräz  .Schmuck';
hsl  *hresk-  aus  bhreg-sk-  in  lit.  hreksta,  hrUko,  hreksti  .anbrechen  (vom rr^a-eY  ctpybre§kis  .Zeit  um  Tagesanbruch';  slov.  hr'^sk,  öech.  bresk,  poln. hrzask  Morgendämmerung',  poln.  obrzasknqc  .hell  werden',  brzeszczy  si^ OS  o-raut  der  Tag',  mit  Assimil.  des  Auslauts  -sk-  an  den  tönenden  Wortan- laut aksl.  pobrSzg^  .Dämmerung.  Tagesanbruch',  russ.  brezg,  poln.  brzazg  ds.
Mit  Abtönung  bh(e)rög-  wahrscheinlich  schwed.  brokig  .bunt',  norw. indartl.  h^ök  .Sälmling'.  auch  wie  bröka  f.  .großgeflecktes  Tier'.
Mit  Hochstufe  der  1.  Silbe:  got.  bairhts  .hell,  glänzend,  deutlich',  ahd. heraht,  mhd.  berht  .glänzend'  (auch  in  Namen  ahd.  Bert-,  -bert,  -brecht), a«-s.  beorlit  .glänzend,  strahlend'  (engl,  bright),  aisl.  biartr  .licht,  hell'; cymr.  berth  .glänzend,  schön'.  PN  bret.  Berth-walart,  ir.  Flaith-bertacJi; lit.  javcn  berst  .das  Getreide  wird  weiß';  wohl  auch  norw.  mdartl.  bjerk .sehr  hell'  .(vgl.  noch  berk  .blanke  Forelle',  schwed.  björkna  .Abramis blicca').
Reduktionsstufig  alb.  barth  (bardh-i)  .weiß'  {*bht,rdgo-).
Im  Namen  der  Birke  (slav.  z.  T.  Ulme.  lat.  Esche):
Ai.  bhürjd-h  m.  .eine  Art  Birke';  osset.  6ärz  .Birke';  dak.  ON  Bersovia; lat.  farnus  .Esche'  {*fdr\_a]g-s-no-s,  ursprgl.  Stoffadj.  .eschen',  wie  auch:) fräxinus  ds.  (wohl  mit  a  anzusetzen,  ^bh^rdg-s-enös)-^  die  zwiefache  Ent- wicklung von  -erd-  in  farnus  und  fräxinus  wird  wie  bei  palma  =  gv. *ftdXa(.iG,  naXdj.irj  gegenüber  latus  =  rlr]r6g  durch  alte  Akzentverschieden- heit bedingt  sein;
ahd.  birihha  (*bher9g-iä),  ags.  beorc,  birce,  aisl.  hjqrk  {*bher9gä)  .Birke';
\it.  ber^as  m..  PL  6^riäi  .Birke',  ablaut.  birztva  f.  .Birkenwald';  bifzliai .Birkenzweige',  lett.  b(}fzs  m..  apr.  berse  .Birke';  russ.  bereza,  skr.  breza, aöech.  brieza  .Birke'  (die  alte  Farbbedeutung  noch  in  bulg.  brSz  .blässig' =  norw.  bjerk  s.  o..  slov.  breza  .Name  einer  weißgestreiften  Kuh  oder Ziege');  mit  Formans  -to-  (=  got.  bairhts)  und  Intonations Wechsel  slav. *berst^  in  russ.  berest  m.  .Ulme.  Rüster',  skr.  brijest,  öech.  brest  ds..  aber mit  der  Bed.  .Birke'  wiederum  russ.  beresta  f..  beresto  n.  .Birkenrinde',  öech. bfesta  .obere
```


### [2026-09-05T14:05:19.662Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-05T14:05:25.395Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==150' POK_01.txt | head -60"
}
```


### [2026-09-05T14:05:26.982Z] TOOL RESULT

```
  Birkenrinde'.
140
Ahd.   'brecht  kann;   wenn  diese  Vokalisierung  statt  'her(h)t   nicht   ei^ Neuerung   ist,   auch   auf   hherek-  bezogen  werden,   wie   an    sich  auch  gof lairJits,  cymr.  herth,  hitt.  parkuis.    Die  Gruppen  hhereg-,  hherek-  scheine Erweiterungen  zu  hher-  _,hell;  braun^  zu  sein.   Ähnliche  Erweiterung  hheU neben  hhel-  ^glänzen^
WP.  II  170  f.,    WH.  I  458,   510  f.,   544,   Trautmann   32,   37  f.,    Specf Pekl.  57.
bheregh-  ,hoch,  erhaben^,  bherghos  ,Berg^,  vielleicht  Erweiterung  von  hh ,(tragen,)  heben^  (s.  dort  die  Gruppe  von  nhd.  empor)  oder  von  hh ,hervorstehen^;  bhrbiü-s  ,hoch^;  bherghö  ,berge'. .    Ai.    Kaus.    harhdyati  ,mehrt^,    hrmhdti    ,macht    feist,    kräftigt,   erheb vermutlich  harha-s,  -m  ,Schwanzfeder,  Schwanz  eines  Vogels,  bes.  bei Pfau^;    hrhdnt-   ,groß,   hoch,    erhaben,    hehr^,    auch    ,hoch,   laut,   von   de] Stimme^,  fem.  bfhati  (=  ir.  Brigit,  germ.  Burgund),  av.  hdrdzant-  (npep huland),  f.  hdrdzaiti  ,hoch^,  im  Kompositum  hdrdzi-  (:  '*hdrdzra-)j  hdrdz-  ,hoc und  ,Höhe,  Berg^  (=  npers.  hurz  ds.,  ir.  hri]   der  Nom.  av.  har§  Subs kann  ar.  -ar-,  aber  auch  ar.  -f-  enthalten,  Bartholomae  IF.  9,  261),  hochstufi av.  uz-hardzayeni  ,ich  soll  aufwachsen  lassen'  (dazu  2aTL-ßaQ^dvr]g  ,Glüc! erhöhend',  iran.  *harzana-)j  hardzan-   m.  hardzah-  n.  ,Höhe',    hardsnu-  m ,Erhebung,  Höhe,  Himmel,  Kopf,  hardzyah-  ,höher',  bai-yzista-  ,der  höchste^ höchstgelegene' ;  npers.  häl-ä  ,Höhe'  {*harz-),  hurz  (s.  oben) ;
ai.  hrhdnt-  bedeutet  auch  ,groß,  gewaltig,  dick,  massenhaft'  und  hrmhatl ,macht  feist,  kräftigt,  stärkt,  vermehrt,  fördert',  bfhdnä  Adv.  ,dicht,  fest, derb,  tüchtig;  sehr,  durchaus',  jparihi'dha-h  ,feststehend,  dicht,  solid'.
Arm.  herj  ,Höhe'  in  erkna-y  lerna-herj  ,himmel-,  berghoch'  (*hherghos), harjr  ,hoch'  (^hhfghü-),  {ham-)harnam  [*harjnam,  Aor.  harji)  ,hebe  auf  usw.
Berg-  in  ON  der  Mittelmeerländer:  thrak.  BeQyovXrjj  maked.  Bioya,  ill. Berginium  (Bruttium:  Bergae),  lig.  Bergomum,  kelto-lig.  Bergusia,  hisp. Bergantia  usw.  Über  das  p-  in  kleinas.  lHqyr},  TleQya^Loq,  maked.  kret. Jlf^ya^og  Vermutungen  bei  Kretschmer  Gl.  22,  100  f.,  Krähe  ZNF.  19,  64.
Lat.  for{c)tis,  alat.  forctus,  dial.  horctus,  horctis  ,kräftig,  ausdauernd, tapfer,  (aus  *forg-tos,  idg.  *hhrgh-tos  =  ai.  hfähdli).
Cymr.  hera  ,Haufe'  (=  nhd.  Beo^g),  acorn.  bret.  herii  ds.  {-rgh-n-'?  s. Pedersen  KG.  I  105),  gall.  ON  Bergusia^  schwundstufi
```


## [2026-09-05T14:05:35.234Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==151' POK_01.txt | head -40; echo \"=== AHD ===\"; grep -n -i \"bhergh\" AHD_watkins1985.txt | head -20"
}
```


### [2026-09-05T14:05:37.131Z] TOOL RESULT

```
<persisted-output>
Output too large (31.1KB). Full output saved to: /home/sfmqrb/.claude/projects/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/tool-results/be8osu4pv.txt

Preview (first 2KB):
g  mir.  hri,  Akk.  hrig ,Hügel'  (s.  oben),  cymr.  hry  ,hoch,  oben',  fem.,  cymr.  corn.  bret.  hre  ,Hügel',  \ gall.  Litano-hriga  u.  a.  ON;  gall.  Brigantes,  Bglyarrsg  Volksname  (ent- weder ,die  Hohen,  Edlen'  oder  ,Höhenbewohner' ;  ai.  hrhant-),  Brigantia ON  ,Bregenz'  und  Name  einer  weiblichen  Gottheit,  air.  Brigit  {Hhrghntt)  ^^ ,Name  einer  berühmten  Heiligen  und  überhaupt  Frauenname'  (auch  ai.  :^ hrhati  ist  als  Frauenname  gebraucht,  ebenso  ahd.  Purgunt),  cymr.  hraint
Jll
141
V    recbt^  Prärogative^  (eig.  ;,Hoheit^),  pl.  hreinian,  dazu  mcymr.  hreenhin, '     'oir    hrenin  ^König^;,  corn.  hrentyn,  hryntyn  ds.  (*brigantmos). °  Got.   hairgaliei  .Berggegend^  aisl.  hjarg  und  herg,  alid.  as.  herg  ,Berg^, j^^^;-//^   6eor^  ,Höhe;  Grabhügel;  engl,  barrote  ^»GrabhügeF   (vgl.  arm. ^er;,  cymr.  hera,  ai.  harha-)-,
crerm.  *hurgundl  (==  ai.  hfliati,  kelt.  *hrigantij  ir.  Brigit)  in  Burgund,  älteste Vimeasform  von  Bornholm  (eig.  ,die  Hochragende^  und  Name  dänischer  und nor^v.  Inseln/  ahd.  Purgunt  Frauenname,  dazu  Burgundiönes,  Stammesname.
Got.  haurgs  f.  ^Stadt,  Turm^,  ahd.  hurg  usw.  ^Burg^  ist  echt  germ.  Ent- gprechung  von  av.  hdrdz-,  kelt.  hrig-  mit  der  Bed.  ^befestigte  Höhe  als Fluclitburg^;  damit  ist  jedoch  lat.  hurgus  ^Wachtturm^  zusammengefallen^, das  aus  gv.  itvoyog  ,Turm^  entlehnt  ist,  einem  oriental.  Kulturwort (?),  das aus  urart.  hurgana  ^Palast,  Festung^  stammt  (820  v.  Chr.,  s.  Adontz REtlE  1,  465),  wovon  auch  arm.  hurgn,  aram.  burgin,  burgon  ,Turm^ us\v.  herzuleiten  sind.    Nach  Kretschmer   wäre  jedoch   Ttvgyog  germ.  Lw.
Dieser   betrachtet  *berghö   ,berge^,  ursprgl.   angeblich   ,bringe  auf  einer ■    Fluchtburg  unter^  als  retrograde  Ableitung  zu  *b7iergh-  ;Berg^  (Gl.  22,  113); 8.  darüber  S.  145.
...
</persisted-output>
```


## [2026-09-05T14:05:40.901Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -iE \"bher[eəg]?gh|bhergh\" AHD_watkins1985.txt | head -20"
}
```


### [2026-09-05T14:05:40.956Z] TOOL RESULT

```
160:A root designating a human settlement is sel-'. These establishments were frequently built on the top of high places fortified for defense, a practice taken by Indo-European migrants into Central and Western Europe, and Italy and Greece, as confirmed by archaeological finds. Words for such fortified high places vary; there are pele-3, variant *poli- (ACROPOLIS), *ark-, dhiino- (TOWN), and bhergh-? (-burg in place names).
338:bherek-. To shine, glitter. A by-form of bhereg-. Variant form *bhrek-, possible root of various Germanic forms. 1. Germanic *bregdan, to move jerkily (> “to shimmer”), in Old English bregdan, to move quickly, weave, throw, braid: BRAID; UPBRAID. 2. Derivative West Germanic *brigdil-, bridle (referring to the movements of a horse’s head), in: a. Old English bridel, bridle: BRIDLE; b. Middle High German bridel, bridle, rein: BRIDE?. 3. Germanic *bréhw6, eyelid, eyelash, in Old Norse bra, eyelash: BRAE. 4. Germanic “breh(w)an, to shine, forming West Germanic *brehsmo, a bream, in Old French bre(s)me, a bream: BREAM!. [Pok. bherak- 141.] bherg-. To buzz, growl. Germanic *berk- in Old English beorcan, to bark: BARK}. [Pok. bhereg- 138.] bhergh-'. To hide, protect. 1. Germanic *bergan in: a.compound *h(w)als-berg-, “‘neck-protector,” gorget (*h(w)alsaz, neck; see k“el-1); b. compound *skér-berg-, “sword-protector,” scabbard (*skér-, sword; see sker-'). 2. Zero-grade form *bhrgh- in: a. Germanic *burgjan in Old English byrgan, to bury: BURY; b. Germanic deriva- tive *burgisli- in Old English byrgels, burial: BURIAL. 3. a. Germanic *borgén, to borrow (? < “to take care of one’s own interests, entrust, pledge, lend, loan”), in Old English borgian, to borrow: BORROW; b. Germanic de- rivative *borganjan in Old French bargaignier, to haggle (> bargaine, haggling): BARGAIN. [Pok. bhergh- 145.] bhergh-?. High; with derivatives referring to hills and hill-forts. 1. Germanic *bergaz, hill, mountain, in: a. Old English beorg, hill: BARROW?; b. Old Norse berg (> Danish and Norwegian berg), mountain: ICEBERG. 2. Compound *harja-bergaz, “army-hill,” hill-fort (*har- jaz, army; see koro-). 3. Compound *berg-frij-, “high place of safety,” tower (*frij-, peace, safety; see pri-), in Old French berfrei, tower: BELFRY. 4. Zero-grade form *bhrgh- in Germanic *burgs, hill-fort, in: a. Old English burg, burh, byrig, (fortified) town: BOROUGH, BURG; b. Old High German burg, fortress: BURGHER; Cc. Middle Dutch burch, town: BURGOMASTER; d. Late Latin bur- gus, fortified place (> burgensis, city dweller): BOURG, (BOURGEOIS), BURGESS, BURGLAR; FAUBOURG. 5. Suf- fixed zero-grade form *bhrgh-to- possibly in Latin fortis, strong (but this is also possibly from dher-?): FORCE, FORT, FORTALICE, FORTE!, FORTE?, FORTIS, (FORTISSIMO), FORTITUDE, FORTRESS; COMFORT, DEFORCE, EFFORT, ENFORCE, FORTIFY, (PIANOFORTE), REINFORCE. [Pok. bheregh- 140.] bhers-. Quick. Latin festindre (< *fers-ti-), to hasten: FESTINATE. [Pok. bheres- 143.] bhes-', To rub. 1. Zero-grade form with unclear suffix *(bh)s-amadho-, sand (in Greek psamathos), in Germanic *sam(a)dam, *sandam in Old English sand, sand: SAND. 2. Suffixed form *(bh)s-abh- in the further suffixed form *sabh-lo- in Latin sabulum, coarse sand: SABULOUS. 3. Suffixed form *bhs-d- in (i) Greek psén, to rub, scrape: PALIMPSEST (ii) Greek pséphos, ballot, pebble: PSEPHOLO- GY. 4, Perhaps suffixed form *bhs-ilo- in Greek psilos, smooth, simple: EPSILON, PSILOMELANE, UPSILON. [Pok. bhes- 145.] bhes-2. To breathe. Probably imitative. Zero-grade form *bhs- in Greek psukhein (< *bhs-il-kh-), to breathe, hence psukhé, spirit, soul: PSYCHE, PSYCHIC, PSYCHO-; METEMPSYCHOSIS. [Pok. 2. bhes- 146.] bheudh-. To be aware, to make aware. 1. Germanic *(for)beudan (*for, before; see per') in: a. Old English béodan, to proclaim: BID; b. Old English forbéodan, to forbid: FORBID; ¢. Old High German farbiotan, to forbid: VERBOTEN, @: Germanic *tudén- in Old English boda, messenger, hence bodian, to announce: BODE!. 3. Ger- manic *budilaz, herald, in Old English bydel, herald, messenger: BEADLE. 4, Germanic *budam in Old Norse bodh, command: OMBUDSMAN. 5. Sanskrit bodhati, he awakes, is enlightened, becomes aware, and bodhih, perfect knowledge: BUDDHA; BODHISATTVA, BO TREE. [Pok. bheudh- 150.]
379:zero-grade form *dhra-gh- in: a. Greek tarassein (Attic tarattein), to confuse, disturb: ATARACTIC; b. Greek trakhus, rough: TRACHEA, TRACHOMA, TRACHYTE. [Pok. 1. dher- 251.] dher-2, To hold firmly, support. 1. Suffixed form *dher-mo- in Latin firmus, firm, strong: FARM, FERMATA, FIRM, FIRMAMENT; AFFIRM, CONFIRM, INFIRM, (INFIR- MARY). 2. Extended form *dhergh- possibly in Latin fortis, strong (but this is also possibly from bhergh-?). 3. Suffixed zero-grade form *dhr-ono- in Greek thronos, seat, throne (< “support”): THRONE. 4. Suffixed form *dher-mn in Sanskrit dharma, statute, law (< “that which is established firmly”): DHARMA. 5. Old Persian dar-, to hold (whence Persian -ddr, ‘“-holder’’): SIRDAR, TAHSILDAR, ZAMINDAR. [Pok. 2. dher- 252.] dher-3, To drone, murmur, buzz. Extended zero-grade form *dhrén- in: a. Germanic *drén- in Old English dran, drén, male honeybee: DRONE}; b. Greek thrénos, dirge, lament: THRENODY. [Pok. 3. dher- 255.] dhers-. To venture, be bold. 1. O-grade form *dhors- and zero-grade form *dhrs- respectively in Germanic *ders- and *durs- in Old English dearr and durst, first and third person singular present and past indicative of durran, to venture: DARE, (DURST). 2. Possibly Latin -festus in: a. infestus, hostile (? < “directed against”; in-, into, against; see en): INFEST; b. manifestus, palpable, evident (< “caught red-handed, grasped by the hand”; manus, hand; see man-2): MANIFEST. [Pok. dhers- 259.] dhés-. Root of words in religious concepts. Possibly an extension of dhé-'. 1. Suffixed form *dhés-yd in Latin fériae (Old Latin fésiae), holidays: FAIR?, FERIA. 2. Suf- fixed form *dhés-to- in Latin féstus, festive (> German Fest, festival): FEAST, (-FEST), (FESTAL), FESTIVAL, FES- TIVE, FESTOON, (FETE), FIESTA; (GABFEST), OKTOBER- FEST. 3. Suffixed zero-grade form *dhas-no- in Latin fanum, temple: FANATIC; PROFANE. 4. Possibly suffixed zero-grade form *dhas-o- becoming *dhes-o- in Greek theos (< *thes-os), god: THEO-; APOTHEOSIS, ATHEISM, ENTHUSIASM, PANTHEON, POLYTHEISM. [Pok. dhés- 259.] dheu-'. Also dheue-. The base of a wide variety of derivatives meaning “to rise in a cloud,” as dust, vapor, or smoke, and related to semantic notions of breath, various color adjectives, and forms denoting defective perception or wits. 1. Suffixed extended zero-grade form *dhii-mo- (<*dhua-mo-), smoke, in: a. Latin fimus, smoke: FUMAROLE, FUMATORIUM, FUMATORY, FUME; FUMARIC ACID, FUMIGATE, FUMITORY, PERFUME; b. Greek thumos, soul, spirit: -THYMIA; ENTHYMEME; c. Greek thumon, thumos, thyme (< “plant having a strong smell”): THYME. 2. Suffixed lengthened zero-grade form *dhi-li- in Latin filigd, soot: FULIGINOUS. 3. Ex- tended form *dheus- possibly in Germanic *dus- in: a. Old English dysig, foolish (< “stupefied,” “confused”): pD1zzy; b. Danish dase, to make drowsy, akin to the probable Scandinavian source of DOZE. 4. Suffixed ex- tended form *dheus-o- in Germanic *deuzam, breathing creature, animal, in: a. Old English déor, animal: DEER; b. Old Norse dyr, animal, deer: REINDEER. 5. Suffixed o-grade form *dhous-o in Slavic *dukh- in Russian dukh, breath, spirit: DUKHOBoR. 6. Variant extended form *dhwes- in nasalized form *dhwens- in Germanic *duns-, dust, meal, in: a. Germanic suffixed form *duns-to- in Old English dist, dust: pustT; b. Old Norse diinn, bird’s down (< “fine like dust”): DOWN?, DUVETYN; (EIDER- Down). 7. Extended zero-grade form *dhus- in Greek thuos, burnt sacrifice, incense (> Latin thus, incense), and ¢huia, cedar: THUJA, THURIBLE; (THURIFER). 8. Suf- fixed extended zero-grade form *dhus-ko- in: a. Ger- manic duskaz in Old English dox, twilight: Dusk; b. Latin fuscus, dark, dusky: OBFUSCATE. 9. Suffixed extended zero-grade form *dhus-no- in Welsh dwn, dull brown color, whence Old English dun(n), dark-brown: DUN2, 10. Zero-grade extended form *dhubh- in Greek tuphein (< *thuphein), to make smoke, and tuphios,
644:Latin cinctari, to delay: cuNCTATION. [Pok. kenk- 566, konk- 614.] konk(h)o-. Mussel, shellfish. 1. Greek konkhé, konkhos, mussel, conch: COCKLE!, CONCH, CONCHA, CONCHO-. 2. Greek kokhilos, land snail: cocHLEa. [Pok. konkho- 614.] kormo-. Pain. Germanic *harmaz in Old English hearm, harm: HARM. [Pok. ormo- 615.] koro-. War; also war-band, host, army. I. Germanic *harjaz, army. 1. Old English here, army: HERIOT. 2. Old French herban, a summoning to military service: ARRI- ERE-BAN. 3. Compound *haryja-bergaz, “army hill,” hill- fort, later shelter, lodging, army quarters (*bergaz, hill; see bhergh-?), in: a. Old English herebeorg (> Middle English herberwe), lodging: HARBOR; b. Old French herberge, lodging: HARBINGER. 4. Compound *harja- waldaz, “‘army commander” (*wald-, rule, power; see wal-), in Anglo-Norman herald, herald: HERALD. II. Ger- manic denominative *harjén in Old English hergian, to ravage, plunder, raid: HARRY. III. Germanic compound *harihring, assembly, “host-ring” (*hringaz, ring; see sker-3), in Medieval Latin harenga, harangue: HA- RANGUE. [Pok. koro-s 615.] koselo-. Hazel. Germanic *haselaz in Old English hesel, hazel: HAZEL. [Pok. kos(e)lo- 616.] kost-. Bone. Probably related to ost-. Latin costa, rib, side: COAST, COSTA, COSTARD, COSTREL, CUESTA, CUTLET; ACCOST, INTERCOSTAL, STERNOCOSTAL. [Pok. kost- 616.] krau-. Also kru-. To conceal, hide. Suffixed extended form *krup-yo- in Greek kruptein, to hide: CRYPT, CRYP- TIC, CRYPTO-, KRYPTON; APOCRYPHA. [Pok. krd(u)- 616.] kred-. Framework, timberwork. Possible root. Germanic *hr6(d)-st- in Old English hrést, roost: Roost. [Pok. kred- 617.] krei-. To sieve, discriminate, distinguish. 1. Basic form with variant instrumental suffixes in: a. suffixed form *krei-tro- in Germanic *hridra-, a sieve, in Old English hridder, hriddel, sieve: RIDDLE}; b. suffixed form *krei-dhro- in Latin cribrum, a sieve: CRIBRIFORM, GAR- BLE. 2. Suffixed form *krei-men- in (i) Latin crimen, judgment, crime: CRIME; RECRIMINATE (ii) Latin discri- men, distinction (dis-, apart): DISCRIMINATE. 3. Suffixed zero-grade form *kri-no- (participial form *kri-to-) in Latin cernere (past participle certus), to sift, separate, decide: CERTAIN; CONCERN, DECREE, DISCERN, EXCRE- MENT, INCERTITUDE, RECREMENT, SECERN, SECRET. 4. Suffixed zero-grade form *kri-n-yo- in Greek krinein, to separate, decide, judge (> krinesthai, to explain): CRISIS, CRITIC, CRITERION; APOCRINE, DIACRITICAL, EC- CRINE, ENDOCRINE, EPICRITIC, EXOCRINE, HEMATOCRIT, HyYPrROCcRISY. [Pok. 4. sker-, Section II. 945.] krek-1. To weave, beat. 1. Germanic *hreh-ulaz in Old English hréol, reel, spool for winding cord: REEL. 2. Suf- fixed o-grade form *krok-u- in Greek krokus, nap of cloth: CROCIDOLITE. [Pok. 1. krek- 618.] krek-2. Frog spawn, fish eggs. Germanic *hrog- in Middle English row, roe: ROE}. [Pok. 2. krek- 619.] krem-. Wild garlic, onion. O-grade form *krom- in Ger- manic *hram- in Old English hramsan, onion, garlic: RAMSON. [Pok. kerem- 580.] kret-'. To shake. O-grade form *krot- in Germanic *hra- thaz, swift, nimble, in Old English hreth(e), nimble, quick, prompt, ready: RATHE, (RATHER). [Pok. 1. kret- 20.
650:kwed-. To sharpen. Germanic *hwatjan in Old English hweittan, to whet: WHET. [Pok. k¥ed- 636.] kwei-. To hiss, whistle. Imitative root. Germanic *hwi-n- and *hwis- in: a. Old English hwinan, to whine: WHINE; b. Old English Awisprian, to whisper: WHISPER; Cc. Old English hAwistlian, to whistle: WHISTLE. [Pok. 2. kuei- 628.] kvei-'. To pay, atone, compensate. Suffixed o-grade form *koi-néd in Greek poiné, fine, penalty, borrowed into Latin as poena, penalty: PAIN, PENAL, (PENALTY), PINE?, PUNISH; IMPUNITY, PENOLOGY, (PUNITORY), (REPINE), SUBPOENA. [Pok. k#ei-t- 636.] kwei-2. To pile up, build, make. O-grade form *koi- in: a. Sanskrit kayah, body: CHEETAH; b. suffixed form *koi-wo-, making, in denominative verb *k“oiw-eyo- in Greek poiein, to make, create: POEM, POESY, POET, POETIC, -POIESIS, -POIETIC; MYTHOPOEIC, ONOMATO- POEIA, PHARMACOPOEIA, PROSOPOPEIA. [Pok. 2. kyei- 637.] kweia-'. To value, honor. Suffixed zero-grade form *kvi-ma (< *kvia-md) in Greek timé, honor, worth: TImocrAcy. [In Pok. kvei-(t-) 636.] kweia-2. To rest, be quiet. I. Suffixed zero-grade variant form *k¥i-lo- (< *kvia-lo-). 1. Germanic *hwilé in: a. Old English Awil, while: WHILE; b. Old English hwilum, sometimes: WHILOM. 2. Possibly Latin tranguillus, tran- quil (trdns-, across, beyond; see tere@-2): TRANQUIL. IL. Variant form *kvyé- (< *kwyes-) in Latin quiés, quiet (> quiétus, calm, retiring), and in requiés, rest, and requiescere, to rest: COY, QUIET; ACQUIESCE, REQUIEM, REQUIESCAT. [Pok. k¥eis- 638.] kweit-. White; to shine. Suffixed form *kweit-o-. 1. Ger- manic *hwitaz in: a. Old English hwit, white: WHITE; b. Middle Dutch wijting, whiting: WHITING?; c. Old High German hwiz, wiz, white; EDELWEIss. 2. Germanic *hwaitjaz in Old English hwé&te, wheat (from the fine white flour it yields): WHEAT. [Pok. 3. kuei- 628.] kwek-. To appear, see, show. Variant form *kveg- in Slavic *kaz- in Russian ukazat’, to order: UKASE. [Pok. k#ek- 638.] kvel-1, To revolve, move around, sojourn, dwell. I. Basic form *kvel- in Latin colere, to till, cultivate, inhabit: COLONY, CULT, CULTIVATE, (CULTURE); INCULT, INQUI- LINE, SILVICOLOUS. II. Suffixed form *k¥el-es- in Greek telos, “completion of a cycle,” consummation, perfection, end, result (> teleos, perfect, complete): TELIC, TELIUM, TELO-; ENTELECHY, TALISMAN, (TELEOLOGY), TELEOST, TELEUTOSPORE. III. Suffixed reduplicated form *k/(e)- kvl-o-, circle. 1. Germanic *hwewlaz in Old English hwéol, hweogol, wheel: WHEEL. 2. Greek kuklos, circle, wheel: CYCLE, CYCLO-, CYCLOID, CYCLONE, CYCLOSIS; BICYCLE, ENCYCLICAL. 3. Sanskrit cakram, circle: CHUK- KER. IV. O-grade form *kvol-. 1. Suffixed form *k¥ol-so-, “that on which the head turns,” neck, in: a. Germanic *h(w)alsaz in (i) Old Norse hails, neck, ship’s bow: HAWSE (ii) Middle Dutch hals, neck: RINGHALS (iii) Germanic compound *h(w)als-berg-, “neck-protector,” gorget (*ber- gan, to protect; see bhergh-'), in Old French hauberc, hauberk: HAUBERK; b. Latin collum, neck: COL, COLLAR, COLLET, CULLET; ACCOLADE, DECOLLATE!, DECOLLETE, MACHICOLATE, (MACHICOLATION), TORTICOLLIS. 2. Suf- fixed form *kol-d in Latin -cola and incola, inhabitant (in-, in; see en): -COLOUS; PRATINCOLE. 3. Suffixed form *kvol-o- in: a. Latin anculus, “he who bustles about,” servant (an-, short for ambi-, around, about; see ambhi): ANCILLARY; b. Greek polos, axis of a sphere: POLE}, PULLEY; c. Greek -kolos, herdsman, in boukolos, cow- herd: BucoLic. 4. Suffixed zero-grade form *k»J-i- in Greek palin, again (< “revolving”): PALIMPSEST, PALIN- DROME, PALINGENESIS, PALINODE. [Pok. 1. k¥el- 639.] kvel-2, Far (in space and time). 1. Lengthened-grade form *kvél- in Greek téle, far off: TELE-. 2. Suffixed zero-grade form *k»l-ai in Greek palai, long ago: PALEO-. [Pok. 2. kuel- 640.]
872:+ esse, to be; see es-): POSSIBLE, POTENT; (IMPOTENT), PREPOTENT. 3. Form *pot- in: a. compound *ghos-pot-, “suest-master,” host (see ghos-ti-); b. compound *dems-pot-, “house-master,” ruler (see deme-'). 4. Old Persian pati-, master: PADISHAH. [Pok. poti-s 842.] [prak-. To make, do. Greek root. Greek prassein (Attic prattein), to effect, do: PRACTICAL, (PRACTICE), PRAG- MATIC, PRAXIS. [In Pok. 1. per 811.]] prek-. To ask, entreat. 1. Basic form *prek- in Latin *prex, prayer (attested only in the plural precés), with denominative precdri, to entreat, pray: PRAY, PRAYER?, PRECARIOUS; DEPRECATE, IMPRECATE. 2. Suffixed zero-grade form *prk-sk- becoming *pork-sk-, contracted into *posk- in suffixed form *posk-to-, contracted into *posto-, which appears in Latin postuldre, to ask, re- quest: POSTULATE; EXPOSTULATE. [Pok. 4. perk- 821.] prep-. To appear. Suffixed zero-grade form *prp-yo- in Germanic *furbjan, to cause to have a (good) appearance, polish, in Old French fo(u)rbir, to polish, burnish: FuR- BISH. [Pok. prep- 845.] preu-. To hop. 1. Zero-grade form *pru- in Germanic *fru- in Old English frogga (with obscure expressive suffix -gga), frog: FROG. 2. Extended o-grade form *prowo- in Germanic *frawaz in: a. Middle Dutch uro, “leaping with joy,” happy: FROLIC; b. Old High German fré, happy, in frewida, joy (> German Freude): scHa- DENFREUDE. [Pok. preu- 845.] preus-. To freeze, burn. 1. Germanic *freusan, to freeze, in Old English fréosan, to freeze: FREEZE. 2. Suffixed zero-grade form *prus-to- in Germanic *frustaz, frost, in Old English forst, frost, frost: FROST. 3. Suffixed form *preus-i- in Latin *preusis, *preuris, act of burning, whence denominative pririre, to burn, itch, yearn for: PRURIENT, PRURIGO, PRURITUS. 4. Suffixed zero-grade form *prus-ina in Latin pruina, hoarfrost: PRUINOSE. [Pok. preus- 846.] pri-. To love. Contracted from *pria-. 1. Suffixed form *priy-o- in Germanic “frijaz, beloved, belonging to the loved ones, not in bondage, free, in: a. Old English fréo, free; FREE; b. Dutch vrij, free: FILIBUSTER. 2. Suffixed (participial) form “priy-ont-, loving, in Germanic ‘“fri- Jjand-, lover, friend, in Old English friond, fréond, friend: FRIEND. 3. Suffixed shortened form *pri-tu- in Germanic *frithuz, peace, in: a. Old High German fridu, peace: SIEGFRIED; b. Old French esfreer, to disturb: AFFRAY; c. Germanic *frij-, peace, safety, in compound *berg-frij-, “high place of safety” (see bhergh-?). 4. Suffixed femi- nine form *priy-G, beloved, in Germanic *frijj6, beloved, wife, in: a. Old Norse Frigg, goddess of the heavens, wife of Odin: Fricc; b. Germanic compound “*frije-dagaz, “day of Frigg” (translation of Latin Veneris diés, “Ve- nus’s day”), in Old English frigedeg, Friday: FRIDAY. [Pok. prdi- 844.] prokto-. Anus. Greek prokios, anus: PROCTITIS, PROCTOL- OGY, PROCTOSCOPE. [Pok. prdkto- 846.] pster-. Also ster-. To sneeze. Imitative root. 1. Suffixed form *ster-nu- in Latin sternuere, to sneeze: STERNUTATION. 2. Suffixed form *ster-t- in Latin ster- tere, to snore: STERTOR. [Pok. pster- 846.] pu-'. Also phu-. To blow, swell. Imitative root. 1. Ex- tended form *pus- in Latin pustula, a bubble, blister: PUSTULE. 2. Perhaps extended form “pit-, penis, in Latin praepiitium, foreskin (prae-, before, in front; see per’): PREPUCE. 3. Variant form *phi- in Greek phusa (> phusan, to blow), bellows, bladder: EMPHYSEMA, PHYSO- STIGMINE, PHYSOSTOMOUS. [Pok. 1. pu- 847.] pu-2, To rot, decay. 1. Suffixed form *pi-lo- in Germanic *filaz, rotten, filthy, in: a. Old English fi, unclean, rotten: FOUL; b. Old Norse fill, foul, akin to the Scandi- Navian source of FULMAR; ¢. Germanic abstract noun *filithd in Old English fylth, foulness: FILTH; d. Ger- manic denominative *filjan, to soil, dirty, in Old English fylan, to sully: FILE’; DEFILE!. 2. Extended form *pug- in Germanic *fuk- in Icelandic fiki, rotten sea grass, and
938:skep-. Also kep-. Base of words with various technical meanings such as “to cut,” “to scrape,” “to hack.” 1. Germanic *skap- in: a. Old English gesceap (ge-, collective prefix; see kom), form, creation (< “cutting”): SHAPE; b. Old English -scipe, state, condition (collective suffix): -sHIP; c. Dutch -schap, “-ship,” condition (collec- tive suffix): LANDSCAPE. 2. Germanic ablaut variant *skOpo-, “thing cut out,” container, in Middle Dutch and Middle Low German schdépe, bucket for bailing water: scoop. 3. Germanic *skaftaz in Old English sceaft, rod of a spear: SHAFT! 4, Germanic expressive form *skabb- in: a. Old English sceabb, a scab, scratch: sHaBBy; b. Old Norse skabb, a scab: scaB. 5. Variant form *skabh- in: a. Germanic *skaban in (i) Old English sceafan, to scrape, pare away: SHAVE (ii) Old High German skaban, to scrape: SAPSAGO; b. Latin scabere, to scrape: SCABIES; c. suffixed form *skabh-ro- in Latin scaber, rough (< “scratched”’): SCABROUS; d. Greek skaphé, boat (< “thing cut out”): SCAPHOID; BATHYSCAPH. 6. Variant form *skap- in Latin scapula, shoulder blade (used as a tool for scraping): SCAPULA. 7. Variant form *kap- in: a. Latin capd, castrated cock: CAPON; b. Late Latin capuldre, to cut: SCABBLE. 8. O-grade form *kop- in: a. suffixed form *kop-yd- in Germanic *hapjo, a cutting tool, ax, sickle, in (i) Old High German hdppa, happa, sickle, akin to the Germanic source of Old Provencal apcha, small ax: PIOLET (ii) Medieval Latin hapia, ax, and Old French hache, small ax: HASH!, HATCHET; NUT- HATCH, QUEBRACHO; b. suffixed form *kop-yo- in Greek koptein, to strike, cut: COMMA; APOCOPE, SARCOPTIC MANGE, SYNCOPE; C. Russian kopat’, to hack, with de- rivative kop’e, lance, in kopeika, kopeck: KOPECK. 9. Pos- sibly zero-grade variant form *skup(h)- in Greek skuphos, a cup (but more likely of obscure origin): SCYPHISTOMA, SCYPHOZOAN. [Pok. 2. (s)kep- 931.] sker-!, Also ker-. To cut. I. Basic forms *sker-, *ker-. 1. Germanic *skeran in Old English scieran, sceran, to cut: SHEAR. 2. Germanic *skeraz in: a. Old English scéar, plowshare: SHARE?; b. Old English scearu, scaru, portion, division (but recorded only in the senses of “fork of the body,” “tonsure”): SHARE!. 3. Germanic *skér- in: a. *skér-6- and *sker-ez- in Old English scéar, scissors: SHEARS; b. compound *skér-berg-, “sword protector,” scabbard (see bhergh-') in Old High German scarberc, scabbard, akin to the possible Germanic source of Anglo- Norman escaubers, scabbard: SCABBARD. 4. Germanic *skur- in Old Norse skor, notch, tally, twenty: SCORE. 5. Germanic suffixed form *skar-jam in Old Norse sker, low reef (< “something cut off’’): scaR?. 6. Suffixed o-grade extended form *skord-o- in Germanic *skardaz in Old English sceard, a cut, notch: SHARD. 7. Extended form *skerd- in suffixed zero-grade form *skrd-o- in Germanic *skurtaz in: a. Old English scort, sceort, “cut,” short: SHORT; b. Old English scyrte, undergarment (< “cut piece”): SHIRT; c. Old Norse skyrta, shirt: SKIRT. 8. Germanic extended form *skerm- in: a. Old High German skirmen, to protect, akin to the source of Old French eskermir, to fight with a sword, fence: SKIRMISH; b. Middle Dutch scherm, shield: SCREEN. 9. Variant form *kar- in Latin caré (stem carn-), flesh: CARNAGE, CARNAL, CARNASSIAL, CARNATION, CARNIVAL, CARRION, CARUNCLE, CHARNEL, CRONE; CARNIVOROUS, INCAR- NATE. 10. Suffixed o-grade form *kor-yo- in Latin co- rium, leather (originally “piece of hide”): CORIACEOUS, CORIUM, CUIRASS, CURRIER; EXCORIATE. 11. Suffixed zero-grade form *kr-to- in Latin curtus, short: CURT, CURTAL, KIRTLE. 12. Suffixed o-grade form *kor-mo- in Greek kormos, a trimmed tree trunk: cor. 13. Suffixed o-grade form *kor-i- in Greek koris, bedbug (< “cutter”): corREopsis. II. Extended roots *skert-, *kert-. 1. Zero-grade form *krt- or o-grade form *kort- in Latin cortex, bark (< “that which can be cut off”): CORTEX; DECORTICATE. 2. Suffixed form *kert-snd- in Latin céna, meal (< “portion of food”): CENACLE. III. Extended root
1278:BAPTIZE gWébh-1 BAR? gWere-2 BARB! bhardha BARBARIAN baba- BARBARISM baba- BARBAROUS_ baba- BARBEL bhardha BARBELLATE bhardha BARBER bhardha BARBETTE bhardha BARBICEL bhardha BARBULE bhardha BARD! gWera-3 BARE! bhoso- BARGAIN bhergh-? BARITE gWera-2 BARITONE gWera-2 BARIUM gWera-2 BARK! bherg- BARLEY bhares- BARM_ Dbhreu-2 BARMY bhreu-2 BARN bhares- BARO- gWera-2 BAROUCHE dwo-, ret- BARROW! bher-1 BARROW? bhergh-2 BARROW’ = bher-2 BARYON gWere-2 BARYSPHERE gWere-2 BARYTA gWere-2 BASCULE (s)keu- BASE! gWa- BASE? bassus BASIS gWa- BAS-RELIEF bassus Bass! bhar- Bass? bassus BASSET! bassus BASSO bassus BAT? bhiag- BATE? battuere BATEAU bheid- BATH! bhé- BATHE bhé- BATHOS gWadh- BATHY- gWadh- BATHYSCAPH skep- BATTEN! bhad- BATTERY battuere BATTER! battuere BATTER’ battuere BATTLE battuere BAWD bhel-2 BAWL bhel-4 Bay? bat-
1283:BELFRY bhergh-? BELIE leugh- BELIEF feubh- BELIEVE leubh- BELL! bhel-4 BELL? bhel-4 BELLADONNA deu-2 BELLE deu-? BELLICOSE duellum
1314:BOOM? bheue- BOON! pbha-2 BOON2 deu-2 BOOR bheue- BOOT? bhad- BOOTH bheue- BORDELLO bherdh- BORDER bherdh- BORE! bher-2 BORE’ bher-1 Boreas gWero-1 BOROUGH bhergh-2 BORROW bhergh-1 BORSCHT bhar- BOSCAGE busk- BOSOM beu-1 BOTH ambh6o BOTHRIUM bhedh- BO TREE bheudh- BOTTOM bhudh- BOTTOMRY bhudh- BOTULIN gWet-3 BOTULINUM gWet-3 BOTULISM gWet-3 BOUCLE beu-1 BOUGH bhaghu- BOUILLABAISSE beu-! BOUILLON beu-1 BOULDER bhel-2 BOULE! gWele-1 BOULE? beu-! BOULEVARD bhel-2, werg-
1316:BOUND! bamb- BOUND‘ bheue- BOUNTY deu-2 BOUQUET busk- BoURG bhergh BOURGEOIS bhergh-2 BOURN bhreu-2 BOURSE bursa
1324:BRIO gWere-2 BRIOCHE bhreg- BRISANCE bhréi- BRISTLE bhar- BRITTLE bhreu-1 BRONCHIECTASIS  ten- BRONCHO- gWere-4 BRONCHUS gWere-4 BRONTOSAUR bhrem-! BROOD bhreu-2 BROOK? bhriig- BROOM bhrem-2 BROTH bhreu-2 BROTHEL bhreu-' BROTHER bhrater- BROW bhri- BROWN bher-3 BROWSE bhreus-1 BRUIN bher-3 BRUISE bhreus-2 BRUMAL mregh-u- BRUNET bher-3 BRUT gWere-2 BRUTE gWere-2 BUBO beu-! BUCCAL beu-1 BUCEPHALUS gWou- BUCK! bhugo- BUCKAROO wak- BUCKBOARD beu-! BUCKLE! beu-! BUCKLE? beu-1 BUCKSHEE bhag-' BUCKWHEAT bhago- BUCOLIC gou-, kWel-1 BuppHA bheudh- BUDGET bhelgh- BUDGE! beu-1 BUGLE! gWou- BUGLOss gldgh- BUILD bheue- BULGE bhelgh- BULIMIA gWou-, leia- BULK! bhel-2 BULL! bhel-2 BULL? beu-1 BULLA beu-1 BULLATE beu-1 BULLET beu-! BULLETIN beu-1 BULLION beu-1 BULLY? beu-1 BULWARK bhel-2, werg- BUNCO bheg- BUND! bhendh- BUND? bhendh- BUNDESRAT ar- BUNDLE bhendh- BUNG peuk- BUNGLE bheg- BUPRESTID gWou- BUR! bhar- BURDEN! bher-1 BURG bhergh-2 BURGESS bhergh-2 BURGHER bhergh-2 BURGLAR bhergh-2 BURGOMASTER bhergh-2 BURIAL bhergh-! BURIN bher-2 BURN! gWher- BURN? bhreu-2 BURNET bher-3 BURNISH bher-3 BURSA bursa BURSAR bursa BURSE bursa BURST bhres- BURY bhergh-1 BUSHEL? bhau- BUSK! busk- BUSK? s(w)e-
1385:coMAl keme- COMB gembh- COMBAT battuere COMBINE dwo- COMBUSTION eus- COME gWa- COMEDO ed- COMEDY wed-2 COMESTIBLE ed- COMFIT dhé-1 COMFORT bhergh-2 COMITIA  ei-1 COMITY smei- COMMA skep- COMMAND man-2 COMMANDO man-2 COMMEMORATE (s)mer-1 COMMENCE ei-1 COMMEND man-? COMMENSURATE mé-2 COMMENT men-! COMMERCE merk-2 COMMINUTE mei-2 COMMISERATE miser COMMIT (s)meit(a)- COMMIX meik- COMMODE med- COMMODIOUS med-
1418:DEEP dheub- DEER dheu-! DEFACE dhé-1 DEFAME bha-2 DEFEASANCE dhé-1 DEFEAT dhé-1 DEFECT dhé-1 DEFEND gWhen-1 DEFENSE gWhen-1 DEFER! bher-1 DEFER? bher-1 DEFERVESCENCE bhreu-2 DEFIANCE bheldh- DEFICIENT _dhé-1 DEFILE! pu-2 DEFILE? gWhi- DEFLAGRATE bhel-1 DEFLATE bhlé-2 DEFLOWER bhel-3 DEFOLIATE bhel-3 DEFORCE bhergh-? DEFORM merph- DEFUNCT bheug-2 DEFY bheidh- DEGAGE wadh-1 DEGENERATE geno- DEGLUTINATE gel-1 DEGLUTITION gWel-3 DEGRADE ghredh- DEGREE ghredh- DEGRESSION ghredh- DEGUST geus- DEHISCE ghal- DEICIDE deiw- DEICTIC deik- DEIFIC delw- DEIGN dek-1 DEISM deiw- DEITY deiw- DEJECT yé- DELAINE wele-1 DELAY slég- DELEGATE leg-1 DELIBERATE [ithra DELINQUENT leikw- DELIQUESCE wileik- DELIRIUM leis-1 DELIVER leudh-2 DELL dhel- DELPHINIUM g¥elbh- DELUDE leid- DELUGE leu(@)- DELVE dhelbh- DEMAGOGUE ag-, da- DEMAND man-2 DEMARCATION merg- DEME da- DEMEAN! men-2 DEMEAN2 mei-1
1442:EDIBLE ed- EpicT deik- EDIFICE aidh-, dhé-1 EDIFY aidh-, dhé-1 EDITION d6- EDUCATE deuk- EDUCE deuk- EFFACE dhé-1 EFFECT dhé-1 EFFEMINATE dhé(i)- EFFERENT bher-1 EFFERVESCE bhreu-2 EFFETE dh@(i)- EFFICACIOUS dhé-1 EFFICIENT dhé-1 EFFIGY dheigh- EFFLORESCE bhel-3 EFFLUENT bhleu- EFFLUVIUM bhieu- EFFLUX bhlieu- EFFORT bhergh-2 EFFULGENT bhel-1 EFFUSE gheu- EFTSOONS apo- EGEST gerere EGG! awi-
1459:ENERVATE (s)neeu- ENFILADE gWhi- ENFLEURAGE bhel-3 ENFORCE bhergh-2 ENGAGE wadh-! ENGAGE wadh-! ENGENDER gene- ENGINE gene- ENGRAVE ghrebh-2 ENGROSS gW¥res- ENHANCE al-3 ENIGMA ai-2 ENJOIN yeug- ENJOY gau-
1503:FATE bha-2 FATHER peter- FATHOM pete- FATIDIC deik- FAUBOURG bhergh-?, dhwer- FAVA BEAN bha-bha- FAVOR ghow-é- FAVORITE ghow-é- FAWN! pek-t FAWN? dhé(i)- FAY} pag- FEALTY bheidh- FEAR per-4 FEASIBLE dhé-1 FEasT dhés- FEAT! dhé-1 FEATHER pet- FEATURE dhé-1 FEBRIFUGE bheug-! FECUND dh@(i)- FEDERAL bheidh- FEDERATE bheidh- FEE peku- FEEBLE bhlé-1 FEED pa-
1528:FOR- per’ FORAGE pa- FORAMEN bher-2 FORBEAR bher-1 FORBID bheudh- FORCE bhergh-2
1533:FORE- pert FORECLOSE dhwer- FOREFATHER per, peter- FOREGO! ghé- FOREIGN dhwer- FOREMOST per! FORENSIC dhwer- FOREST dhwer- FORESTALL | stel- FORFEIT dhé-1, dhwer- FORFICATE bherdh- FORGE! dhabh- FORGET ghend- FORGIVE ghabh- FORGO ghé- FORLORN leu-! FORLORN HOPE keu-?, leu-1 FORM merph- FORMAL merph- FORMER? per! FORMIC morwi- FORMICARY morwi- FORMICIVOROUS morwi- FORMULA merph- FoRNAX gWher- FORNICATE gWher- FORSAKE sag- ForT bhergh-2 FORTALICE bhergh-2 FORTE! bhergh-2 FORTE? bhergh-2 FORTH pert FORTIFY bhergh-2 FORTIS bhergh-2 FORTISSIMO bhergh-2 FORTITUDE bhergh-2 FORTRESS bhergh-2 FORTY kWetwer- FORUM dhwer- Fossa bhedh- FOSSE bhedh- FossIL bhedh- FOSSORIAL bhedh- FOSTER pa- FOUDROYANT bhel-1 FOUL pu-2
1662:ICEBERG bhergh-2 IcH dhgWher- ICHTHYO- dhghi- ICHTHYORNIS  or- ICICLE eis-2, yeg- ICON weik-3
```


## [2026-09-05T14:05:41.486Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -iE \"barbican|balcony\" KLN_1966.txt | head -20"
}
```


### [2026-09-05T14:05:41.545Z] TOOL RESULT

```
3200:Derivatives:  appli-able,  adj.,  appliable-ness,  n., appli-abl-y,  adv.,  appli-ance,  n.,  appli-ant,  adj. appoggiatura,  n.,  a  grace  note  (music).  —  It.,  lit. ‘a  support’,  fr.  appoggiare,  ‘to  lean,  rest,  sup¬ port’,  fr.  VL.  *appodiare,  ‘to  support’,  fr.  ad- and  L.  podium,  ‘elevated  place,  balcony  .  See podium  and  cp.  appui.
3237:‘to  support’,  fr.  ad-  and  L.  podium ,  ‘an  elevated place,  balcony’.  See  podium  and  cp.  appoggia-
4311:balcony,  n.  —  It.  balcone,  formed  with  the  aug¬ mentative  suff.  -one  fr.  balco,  ‘scaffold’,  which is  borrowed  fr.  OHG.  balcho,  ‘beam’  (whence MHG.  balke,  G.  Balken,  ‘beam’).  See  balk, ‘beam’.
4321:base  *bhel-,  ‘to  swell’.  See  ball,  ‘a  round  body’, and  cp.  Balaena,  balinger. balefire,  n.  —  OE.  bielfyr,  ‘funeral  fire’,  com¬ pounded  of  bxl,  ‘a  blazing  fire,  a  funeral  pile’, and  fyr,  ‘fire’.  The  first  element  is  rel.  to  ON.  bdl, ‘a  great  fire’,  fr.  I.-E.  base  *bhel-,  ‘to  shine’;  see bald.  For  the  second  element  see  fire, balinger,  n.,  a  whaleship  ( obsol .)  —  OF.  balen- gier,  ‘whaleship*,  fr.  baleine,  ‘whale’.  See  baleen, balk,  also  baulk,  n.,  ridge  of  land  left  unplowed between  furrows :  a  beam.  —  ME.  balke,  ‘beam’, fr.  OE.  balca,  ‘ridge  between  furrows,  beam, rafter’,  rel.  to  OS.  balko,  ON.  bjalki,  Dan.  bjelke, Swed.  bjdlke,  OFris.  balka,  OHG.  balko,  balcho, MHG.  balke,  G.  Balken,  ‘beam,  rafter’  (cp., with  vowel  gradation,  OE.  bolca,  ‘wooden gangway  of  a  ship’),  ON.  bolr,  ‘trunk  of  a  tree’ ; fr.  I.-E.  base  *bheleg-,  ‘beam,  plank’,  whence also  Gk.  tpaXzy?,  ‘trunk,  log;  line  of  battle, battle  array’,  cpaXtoit;,  ‘beam’,  L.  fulcire,  ‘to prop’,  fulcrum,  ‘bedpost’,  Lith.  balziena,  ‘cross¬ bar’,  Lett,  bdlziens,  ‘prop,  stay’.  Cp.  balcony. Cp.  also  block,  bole,  ‘trunk’,  bulk,  ‘projection’, debauch,  ebauchoir,  fulcrum,  phalange,  phalanx, planch,  planchet,  plancier,  plank.
4441:barbette,  n.,  mound  for  mounting  guns  (fort.)  — F.,  dimin.  of  barbe,  ‘beard’  (see  barb,  ‘beard’, and  -ette) ;  so  called  from  a  fanciful  comparison of  the  mounted  guns  with  a  beard, barbican,  n.,  outer  defense  of  a  city  or  castle.  — ME.  barbecan,  fr.  OF.  barbacan,  barbican  (F. barbacane),  which  prob.  derives  ult.  fr.  Pers. bdla-khdna,  ‘upper  chamber,  balcony  on  the  top of  a  house’,  lit.  ‘a  high  house’,  fr.  bala,  ‘high’, and  khdna,  ‘house’.  The  first  element  is  rel.  to Avestic  berezant-,  OI.  brhant-,  ‘high’;  see borough.  The  second  element  derives  fr.  stem khan-,  ‘to  dig’.
15884:gazebo,  n.,  turret,  balcony.  —  Facetious  forma¬ tion  fr.  gaze  after  L.  videbo,  ‘I  shall  see’, gazelle,  n.  —  F.,  fr.  ghazel,  N.  African  pronun¬ ciation  of  Arab,  ghazdl.
28413:pew,  n.  —  ME.  pewe,  puwe,  pywe,  fr.  MF. puie,  puiee,  ‘prop,  stay,  raised  seat,  balcony’, verbal  noun  formed  fr.  puier,  ‘to  prop,  support’, fr.  VL.  *podiare,  fr.  L.  podium,  ‘an  elevated place,  parapet,  balcony’,  fr.  Gk.  noStov,  ‘base, pedestal,  balcony’,  dimin.  of  nouc,  gen.  :ro86<;, ‘foot’.  See  foot  and  cp.  -pod,  podium,  puy.  Cp. also  appui,  apoggiatura.
31135:puy,  n.,  a  hill  of  volcanic  origin.  —  F.,  fr.  L.  po¬ dium,  ‘a  height,  balcony’,  prop,  ‘support’,  fr. Gk.  7roSiov,  dimin.  of  Troup,  gen.  710861;,  ‘foot’. See  podium.
41257:Derivatives:  veracious-ly,  adj.,  veracious-ness,  n. veracity,  n.,  truthfulness,  truth.  —  F.  veracite,  fr. ML.  veracitdtem,  acc.  of  veracitas,  ‘truthfulness’, fr.  L.  verax,  gen.  -acis.  See  prec.  word  and  -ity. veranda,  verandah,  n.  —  Port,  varanda,  ‘balcony’, introduced  into  English  from  India.  Port,  ra- randa  itself  is  of  uncertain  origin.  F.  veranda was  borrowed  from  English.
```


## [2026-09-05T14:05:55.450Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"borough,  n\" KLN_1966.txt | head -5; echo \"---\"; grep -n -E \"^\\s*bal(a|conv|cony)|balcony,  n\" KLN_1966.txt | head"
}
```


### [2026-09-05T14:05:55.534Z] TOOL RESULT

```
5381:borough,  n.  —  ME.  burgh,  burwe,  fr.  OE.  burg, burh,  burg,  rel.  to  OS.,  OFris.,  burg,  ‘castle’, ON.  borg,  ‘wall,  castle’,  MDu.  burch,  borch, borcht,  Du.  burchl,  burg,  OHG.  burg,  burc, buruc,  ‘fortified  place,  citadel’,  MHG.  burc, G.  Burg,  ‘castle’,  Goth,  baurgs,  ‘city’,  OE.  beorg, etc.,  ‘mountain’.  These  words  prob.  derive  fr. I.-E.  base  *bhergh-,  ‘high’,  whence  also  Arm. berj,  ‘high  place',  OSlav.  bregu,  ‘bank  (of  a river)’,  W.  bera,  ‘stack,  pyramid’,  Mir.  bri,  acc. brig,  ‘hill’,  Toch.  A  parkas,  ‘long’,  Hitt,  parkush, ‘high’,  OI.  bfhdnt-,  Avestic  blrlzant-,  ‘high’, OCeltic  Brigantes,  lit.  ‘the  high  ones’  (cp.  Bur¬ gundians,  fr.  Late  L.  Burgundiones,  lit.  ‘high¬ landers’),  prob.  also  OL.  forctus,  ‘good’,  L. fortis  (fr.  OL.  forctis),  ‘strong’,  see  Walde-Hof- mann,  LEW.,  I, pp.  535-36,  s.v. fortis, and  Kluge- Mitzka,  EWDS.,  p.67,  s.v.  Berg.  Cp.  barrow, ‘mountain,  mound’,  bourgeois,  burgage,  burgess, burgh,  burgrave,  Burgundy,  canterbury,  faubourg, gaussbergite,  ghetto,  Hapsburg,  hauberk.  Cp.  al¬ so  Brahma,  fort,  and  the  second  element  in  bar- bicane.  Cp.  also  the  suff.  -bury  in  English  place names,  which  comes  fr.  OE.  byrig,  the  dative sing  of  OE.  burg.  Base  *bhcrgh-  is  prob.  an  en¬ larged  form  of  base  *bher-,  ‘to  carry,  lift’.  See bear,  ‘to  carry’.
---
4255:balalaika
4304:balan-
4308:balas,  n.,  a  variety  of  spinel  ruby.  —  F.  balais, fr.  Arab,  balakhsh,  fr.  Balakhshdn,  fr.  Pers. Badhakhshin,  name  of  a  region  in  Central  Asia (near  Samarkand),  where  this  variety  of  spinel ruby  is  found.
4309:balatron,  n.,  jester,  buffoon.  —  L.  balatro,  gen. -onis,  of  Etruscan  origin;  not  related  to  L. blaterd,  ‘babbler’.
4310:balaustine,  n.,  the  pomegranate  tree.  —  Formed with  suff.  -ine  fr.  Gk.  pocXaucmov,  ‘flower  of the  wild  pomegranate’,  a  word  of  Sem.  origin. Cp.  Aram,  balatz,  said  of  the  blossoming  of  the pomegranate  tree.  For  the  correspondence  of Greek  st  to  Semitic  s,  tz,  cp.  Gk.  e-rupa^,  fr. Heb.  tzdri  (see  sty  rax).  Cp.  baluster, balbriggan,  n.,  a  cotton  fabric  used  for  hosiery.  — Prop,  ‘fabric  made  in  Balbriggan  (in  Ireland)’, balbuties,  n.,  stammering  (med.)  —  Medical  L., fr.  L.  balbutire,  ‘to  stammer’,  fr.  balbus,  ‘stam¬ merer’,  from  the  I.-E.  imitative  base  *bal-,  ‘to stutter’.  See  booby  and  cp.  words  there  re¬ ferred  to.
4311:balcony,  n.  —  It.  balcone,  formed  with  the  aug¬ mentative  suff.  -one  fr.  balco,  ‘scaffold’,  which is  borrowed  fr.  OHG.  balcho,  ‘beam’  (whence MHG.  balke,  G.  Balken,  ‘beam’).  See  balk, ‘beam’.
```


## [2026-09-05T14:05:55.821Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -iE \"BALCONY|BARBICAN\" AHD_watkins1985.txt | head -10"
}
```


### [2026-09-05T14:05:55.876Z] TOOL RESULT

```
330:3. O-grade form *bhol- in Germanic *ball- in: a. Old English beallucas, testicles: BOLLIX; b. Old Norse bdllr, ball: BALL; c. Danish bolle, round roll, akin to the probable Scandinavian source of BILBERRY; d. Middle High German baile (> Italian balla, palla), ball: BAL- LOON, BALLOT; PALL-MALL; e. French baile, ball: BAL- LOTTEMENT; f. Old French baie, rolled-up bundle: BALE!. 4. Suffixed o-grade form *bhol-to- possibly in Germanic *balthaz, bold, in: a. Old English bald, beald, bold: BOLD; b. Old High German bald, bold: BAWD. 5. Suffixed o-grade form *bhol-n- in Latin follis, bellows, inflated ball: FOLLICLE, FOOL!; (FOLLICULITIS). 6. Possibly Greek phalaina, whale: BALEEN. 7. Conceivably (but more likely unrelated) Greek phellos, cork, cork oak: PHEL- LEM; PHELLODERM, PHELLOGEN. (The following deriva- tives of this root are entered separately: bhel-?, bhelgh-, bhlei-, bhleu-.) [Pok. 3. bhel- 120.} bhel-3, To thrive, bloom. Possibly from bhel-?. I. Suffixed o-grade form *bhol-yo-, leaf. 1. Latin folium, leaf: ForL?, FOLIAGE, FOLIO, FOLIUM; CINQUEFOIL, DEFOLIATE, EX- FOLIATE, FEUILLETON, FOLICOLOUS, MILFOIL, PORTFO- LIO, TREFOIL. 2. Greek phullon, leaf: (-PHYLL), PHYLLO-, -PHYLLOUS; GILLYFLOWER, PODOPHYLLIN. II. Extended form *bhlé- (< *bhlea-). 1. O-grade form *bhl6- in: a. suffixed form *bhlé-w- in Germanic *bl6-w- in Old English bléwan, to flower: BLOWS; b. Germanic suffixed form *bl6-m6n- in (i) Old Norse blém, blémi, flower, blossom: BLOOM! (ii) Old English bléma, a hammered ingot of iron (semantic development obscure): BLOOM?; c. Germanic suffixed form *bl6-s- in Old English bléstm, bléstma, flower, blossom: BLOssoM; d. Latin flés (stem flor-), flower: FERRET?, (FLORA), FLORA, (FLORAL), FLOR- IATED, FLORID, FLORIN, FLORIST, -FLOROUS, FLOSCULUS, FLOUR, FLOURISH, FLOWER; CAULIFLOWER, DEFLOWER, EFFLORESCE, ENFLEURAGE, FLORIGEN. 2. Germanic suf- fixed form *blé-do- in Medieval Latin bladium, produce of the land: EMBLEMENTS. 3. Suffixed zero-grade form *bhib-to- in Germanic *bladaz in Old English bled, leaf, blade: BLADE. [Pok. 4. bhel- 122.] bhel-4. To cry out, yell. Germanic *bell- in: a. Old English bellan, to bellow, bark, roar: BELL?; b. Old English belle, a bell: BELL!; c, Old English belgan, bylgan, to become enraged: BELLOW; d. perhaps Old English bealcan, *b(iJelcan, to utter, belch forth: BELCH; e. Middle High German buldern, boldern, to make noise: POLTERGEIST; f. Icelandic baula, to low, akin to the Scandinavian source of Middle English baulen, to howl: BAWL. [Pok. 6. bhel- 123.] bheld-. To knock, strike. Zero-grade form *bhid- in Germanic *bult-, missile, in Old English bolt, heavy arrow, bolt: BouT!. [Pok. bheld- 124.] bhelg-. Also bhelk-. A plank, beam. 1. Germanic *balku- in Old English balc(a), ridge: BALK. 2. Germanic *balk6n- in: a. Old French bauch, beam: DEBAUCH; b. Old Italian balcone, scaffold: BALCONY. 3. Suffixed zero-grade form *bhik-yo- in Latin fulcire, to prop up, support: FULCRUM. 4. Possibly Greek phalanx, beam, finger bone, line of battle: PHALANGE, PHALANX. [Pok. 5. bhel- 123.] bhelgh-. To swell. Extension of bhel-2. 1. Germanic *balgiz in Old English bel(ijg, belig, purse, bellows: BELLOWS, BELLY. 2. Germanic *bulgjan in Old Norse bylgja, a wave: BILLOW. 3. Germanic *bolgstraz in Old English bolster, cushion: BOLSTER. 4. Celtic *bolg- in Latin bulga, leather sack: BUDGET, BULGE. [Pok. bhelgh- 125.) bhelu-. To harm. Germanic *balwaz in Old English bealo, b(e)alu, harm, ruin, bale: BALE?. [Pok. bheleu- 125.] bhendh-. To bind. 1. Germanic *bindan in Old English bindan, to bind: BIND; WOODBINE. 2. O-grade form *bhondh- in Germanic *band- in: a. Old English bend, band, ribbon, akin to the Germanic source of Old French bende, band: BEND?; b. Old English bendan, to bend: BEND!; c. Old Norse band, band, fetter: BAND!, BOND; d. Old French bande, bond, tie, link: BAND!. 3. Zero-
844:fér, danger, sudden calamity: FEAR. 2. Suffixed form *peri-tlo- in Latin periclum, periculum, trial, danger: (PARLOUS), PERIL. 3. Suffixed form *per-yo- in Latin experirt, to try, learn by trying (ex-, from; see eghs): EXPERIENCE, EXPERIMENT, EXPERT. 4. Suffixed form *per-ya in Greek peira, trial, attempt (> peiran, to attempt): PIRATE; EMPIRIC. [Pok. 2. E. per 818.] per-5. To strike. Extended forms *prem-, pres- in Latin premere (past participle pressus), to press: PREGNANT?, PRESS!, PRESSURE, PRINT; APPRESSED, COMPRESS, DE- PRESS, EXPRESS, IMPRESS!, (IMPRINT), OPPRESS, RE- PRESS, (REPRIMAND), SUPPRESS. [Pok. 3. per- 818.] per-6. To traffic in, sell (< “to hand over,” “distribute”). A verbal root belonging to the group of per'. Base of two distinct extended roots. I. Root form *pret-. 1. Latin compound inter-pres (stem inter-pret-), go-between, negotiator (inter-, between; see en): INTERPRET. 2. Suf- fixed form “pret-yo- in Latin pretium, price: PRAISE, PRECIOUS, PRICE; APPRAISE, (APPRECIATE), DEPRECIATE. II. Root form *pers-. Suffixed form *p(e)r-n-o- in Greek pernanai, to sell, whence o-grade *por()-ndé in Greek porné, prostitute: PORNOGRAPHY. [In Pok. 2. C. per 817.] perd-. To fart. 1. Germanic *fertan, *fartén in Old Eng- lish *feortan (> Middle English farten), to fart: FART. 2. Greek perdix, partridge (which makes a sharp whirring sound when suddenly flushed): PARTRIDGE. See also pezd-. [Pok. perd- 819.] pere-'. To produce, procure. Perhaps an extension of per-3, a verbal root belonging to the group of per’. Possibly the same root as pere-2. Zero-grade form *pro- (becoming *par- in Latin) in: a. root form *par-d- in Latin pardre, to try to get, prepare, equip: PARADE, PARE, PARRY, (PARURE); APPARATUS, (APPAREL), COM- PRADOR, DISPARATE, EMPEROR, (IMPERATIVE), (IMPE- RIAL), (PARACHUTE), PARASOL, PREPARE, RAMPART, REPAIR}, SEPARATE, (SEVER), (SEVERAL); b. suffixed form *par-yo- in Latin parere, parire, to get, beget, give birth (> partus, accusative partum, birth): -PARA, PAR- ENT, -PAROUS, PARTURIENT, POSTPARTUM, REPERTORY; c. suffixed form *par-os, producing, in compound *pau- paros, producing little, poor (see pau-); d. suffixed form *par-ikaé in Latin Parcae, the Fates (who assign one’s destiny): Parca. [Pok. 2. D. per 818.] pere-2. To grant, allot (reciprocally, to get in return). Possibly the same root as pere-'. Zero-grade form *pro- (becoming *par- in Latin) in: a. suffixed form *par-ti- in Latin pars (stem part-), a share, part: PARCEL, (PARCE- NER), PARSE, PART; BIPARTITE, COMPART, IMPART, REP- ARTEE; b. possibly suffixed form *par-tid in Latin portid, a part (first attested in the phrase pré portiéne, in proportion, according to each part, perhaps assimilated from *pré partidne): PORTION, PROPORTION; C. perhaps Latin pdr, equal (> French pari, wager): PAIR, PAR, PARITY2, PARLAY, PEER?; COMPARE, IMPARITY, NONPA- REIL, PARI-MUTUEL. [Pok. 2. per, Section C. 817.] perg-. Pole, stem. Possibly Latin pergula, a projection, balcony, outhouse: PERGOLA. [Pok. 1. perg- 819.] perk-'. Speckled. Often used in names of spotted or pied animals. Greek perké, the perch: PERCH?. [Pok. 2. perk- 820.] perk-2. To dig out, tear out. Zero-grade form *prk- in Germanic *furh- in Old English furh, trench: FURROW. [Pok. 3. perk- 821.] perkwu-. Oak. 1. Zero-grade form *prkv- in Germanic *furhu- in Old English furh, fyrh, fir: rir. 2. Assimilated form *kverku- in Latin quercus, oak: QUERCETIN, QUER- CITRON. [Pok. perk#u-s 822.] persna. Heel. Latin perna, ham, leg, sea mussel: PEARL}. [Pok. persna 823.] pes-. Penis. Suffixed form *pes-ni- in Latin pénis (< *pesnis), penis, tail: PENCIL, (PENICILLIUM), PENIS. [Pok. 3. pes- 824.] pet- Also pete-. To rush, fly. Variant *p#é-, contracted from *ptea-. 1. Suffixed form *pet-rd in Germanic *feth-
1276:BABA baba- BABBLE baba- BABE baba- BABKA baba- BABU baba- BABUSHKA baba- BABY baba- BACILLUS bak- BACTERIUM bak- BACULIFORM bak- BAGEL bheug-3 BAGUETTE bak- Bails bheug-3 BAIRN bher-1 BaIT! bheid- BAKE bhé- BAKSHEESH bhag-' BALALAIKA baba- BALCONY bhelg- BALE! bhel-2 BALE? bhelu- BALEEN bhel-2 BALK bhelg- BALL! bhel-2 BALL2 gWele-1 BALLAD gWele-1 BALLAST bhoso-, kla- BALLET gWela-1 BALLISTA gWele-1 BALLOON bhel-2 BALLOT bhel-2 BALLOTTEMENT bhel-2 BAMBINO _baba- BAN! bha-2 BANAL bha-2 BAND! bhendh- BANDANNA bhendh- BANDIT bha-2 BANDOLEER bha-1 BANDORE pandoura BANE gWhen-1 BANG! bheg- BANIAN wen-1 BANISH bha-2 BANK! bheg- BANK? bheg- BANK? bheg- BANKRUPT bheg-, reup- BANNER bha-! BANNERET bha-1 BANNS bha-? BANQUET bheg- BANQUETTE bheg- BANSHEE gWen- BANTLING bheg- Baptist gébh-!
```


## [2026-09-05T14:06:03.912Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== LKT leaf 43 (p.17) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==44' LKT.txt | head -50"
}
```


## [2026-09-05T14:06:04.526Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PHN leaf 86 (p.55) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==87' PHN.txt | head -40; echo \"=== grep balcon in PHN ===\"; grep -n -i \"balcon\" PHN.txt | head"
}
```


### [2026-09-05T14:06:05.497Z] TOOL RESULT

```
=== LKT leaf 43 (p.17) ===
tammt,  ZDMG  LI,  29.o]; hieraus  sp.  albeitar,  pg.  alveitar  'dass.'. [DE  70.
184  a.  Hebr.  bajiö: 'Haus'  [ar.  bait,  assyr.  bitu];  hieraus gaunerdeulsch  Bais,  Bes,  Bos  'dass.'. Mit  hebr.  zönä  'Prostituierte'  ergibt  sich Sonebos,  Sonnenbos  'Bordell',  mit  hebr. zebfl  'Mist'  [s.  hier  Nr.  145  c]  Sefelbos 'Abtritt'.    S.  auch  hier  Nr.  145a.
18.5.  Mal.  bäjü: Besser  bägü  'eine  Art  Überkleid,  nia- layische  Jacke'  [Pijn  27  a] ;  hieraus  anglo- ind. badjoe,  bajoo  'dass.'.  [Hobson-Job- son 46/47.
186.  Ar.  bakara:
'Kuh';  hieraus  siz.  bdcara  'eine  Art kleiner  Wagen,  kleinstes  Gefährt  in  Si- zilien'.   [GrSVociSic  227.
187.  Hebr.  bakbük:
'Flasche' ;  hieraus  frz.  bacbuc  'dass.'  bei Rabelais:  la  dioe  Bacbuc  'die  göttliche Flasche!'    [Devic  DEt  56.
188.  Ar.  bakija:
'Rest,  Überbleibsel';  hieraus  mit  ar.  Art. sp.  albaquia  'der  Rest  einer  Schuld,  be- sonders das,  was  bei  der  Entrichtung des  Zehnten  sich  nicht  bequem  teilen ließ,  z.  B.  sechs  oder  sieben  Schafe'. [DE  65.    Dicc  Gast  104  a.
189.  Ar.  bakkäl: 'Gemüsehändler,  Händler  mit  Gemüse, Obst,  Pökelfleisch,  Rindfleischwürsten und  anderen  Gegenständen  häufigen (lebrauchs',  ebenso  tk.;  hieraus  rum. bacal,  bäcan  'Grünhändler',  bäcänesä 'Gemüsehändlerin',  bäcäliä,  bäcämä  'Ge- müsehandlung'; russ.  bakalvja,  bulg. bakalija,  serb.  bakalski  jespap,  poln. irt^'a/;>'Spezereien,Koloniaiwaren'.  [Gor- jajew 9.
190.  Ar.  bakkam:
'Farbholz  zum  Rotfärben'  [vielleicht  aus
17
[Tk.  baklawa.
dem  Pers.,  etwa  pük  Horn  NpEt  S.  75, Nr.  339  '^Brennholz'],  ebenso  tk.  bakam; hieraus  rum.  bäcan  'Blauholz',  russ. bakan  Tlorentinerlack'.  Bakkam  ist dasselbe  wie  Fernambuk-  oder  Brasil- holz, Caesalpinia  echinata  Lam.,  seit  der Entdeckung  Amerikas  unser  gebräuch- lichstes Rotholz,  das  die  Portugiesen 1.540  in  den  südamerikanischen  Wäldern in  großen  Mengen  fanden  [wie  Haema- toxylon  campechianum  L.  oder  Cam- pecheholz unser  gebräuchlichstes  Blau- liolz  ist].  Im  angloind.  sappanwood  ist wahrscheinlich  tamul.  shappu  oder  ma- layäl.  shappannani  "rot'  als  Grundwort anzusetzen.  Der  dritte  bereits  genannte Name  Brasil  oder  Brazil,  schon  im Mittelalter  gebraucht,  ist  noch  nicht  er- klärt.   [Hobson-Jobson  794.
191.  Tk.  baklawa:
'Kuchen  aus  Mandeln  oder  Rosinen  mit Honig  und  Zucker  hergestellt' ;  hieraus rum.  baclava  'Honigkuchen,  Marzipan'.
192.  Hind.  baknä:
""Schwatzen' ;  hieraus  angloind.  to  buck ^plappern,  viel  und  anhaltend  schwatzen'. [Hobson-Jobson  117.
193.  Tk.  bakyr:
'Kupfer';  hieraus  serb.  bakar  'dass.', bulg.  bakor  'Kupfer,  Kupfergefäß'.  [Mikl SlEtWb  6.    Bern  SlEtWb  40.
194.  Ar.  balä':
'Unglück',  tk.  ebenso  bela;  hieraus  rum. bela,  belea  'Mißgeschick,  Not',  beläleü 'schwach'.
195.  Mal.  baläcau:
^Vorspeise  aus  gesalzenen  und  dann  ge- stampften und  getrockneten  Fischchen oder  dergl.'  [Pijn  38  a];  hieraus  anglo- ind. balachong,  blachong,  die  charakte- ristische Speise  der  indochinesischen  und malayischen  Völker.  [Dass.  wie  hier Nr.  286.]    [Hobson-Jobson  51.
196.  Ar.  balad:
'Land',  Adj.  dazu  baladl  'ländlich,  ein- heimisch'; hieraus  mit  leicht  verständ- lichem Bedeutungswechsel  sp.  baladi 'wertlos,  gering'.    [DE  202/3.
197.  Pers.  bälähäuä:
[Aus  pers.  bälä  'hoch'  Horn  NpEt  S.  39, Nr.  171  und  pers.  hänä  'Haus'  ebenda S.  103,  Nr.  465;  also  eigentlich  'Hoch- haus'] 'ein  oberes  Zimmer,  hervorstehen- der Teil  des  Hauses,  Erker,  Balkon'; hieraus  mit  vielfachen  Kontaminationen ähnlich  bedeutender  Wörter  und  unter volksetymologischen  Einflüssen  it.  bar- ■bucane  'Brustwehr  mit  Schießscharten, Stützmauer',  prov.  barbacana,  frz.  bar- bacane  'Schießscharte',  kat.  barbacana ''Fensterdach,  Dachvorsprung',  sp.  bar- bacana und  pg.  barbacäa  'Außen werk
Lolcotsch,  Etymolog.  Wörterbuch.
einer  Feslunii'.  Wenn  Löbel  EITAP  11 diese  Ableitung  mit  mehr  als  einem Schein  von  Recht  elimologia  indoiosä nennt,  so  sind  die  folgenden  Wörter aus  semantischen  Gründen  unzweifel- haft aus  dem  angegebenen  Grundwort abzuleiten  und  Annahme  eines  ahd. palco  'Balken'  als  Grundwort  abzuleh- nen: it.  balcotie,  frz.  balcon,  rum.  halcon, sp.  balcÖH,  pg.  balcäo;  dtsch.  Balkon, engl,  balconi/;  russ.  bulg.  serb.  poln. balkon,  6ech.  bulkön.  —  Auf  direkterem Wege,  höchstens  über  tat.  bälahane  ist russ.  balagan  'Marktbude  aus  Brettern, Schaubude'  entstanden.  —  Andere  Ab- leitungen s.  DE  60.  Eguilaz  97.  ZfromPh V,  244;  XXX,  557.  [Gorjajew  9  u.  10. ML  890.
198.  Tat.  balaliiika:
'Laute' ;  hieraus  russ.  h
```


### [2026-09-05T14:06:07.233Z] TOOL RESULT

```
=== PHN leaf 86 (p.55) ===
BAL 55
et de Roxelane, qui péril étranglé en 1059; et 6% enfin, Ba-
jazet, fils d* Ahmed I'', qui fut mis à mort en 1 635, par Tordre
de son hère Mourad IV. Les malheurs de ce prince ont fourni
au grand poète Racine le sujet d'une de ses plus belles tragé-
dies, intitulée Bajazet, et qui parut en 1679.
BALAIS, adj. m. (p.)
^yu^J^ [balakhch] Sorte de pierre précieuse de couleur d'hya-
cinthe, et tirée d'une montagne du Turkestan, que l'on appelle
j&^Oo [badakhch] ou ^lâb^Oy [badakhchân], — Le premier
mot oriental n'est qu'une variante des deux autres, et l'adjectif
français est ordinairement précédé du substantif rubis : rubis
balais, en persan ^L&^«Xj JoJ [/aV badakhchân j. — Les Italiens
écrivent balascio; les Anglais, baiass; les Espagnols et les Por-
tugais, balax.
BALCON, s. m. composé, (p.)
JbU.^1; [bâlûkhâikeh], composé de l'adjectif ^l? [bâlà] élevé, et
du substantif Xîl^ [&/ran«/i] maison, demeure ou appartement.
Partie supérieure d'une habitation, d'où Ton aperçoit les alen-
toui*s; belvédère. (Voyez le Dictionnaire turc-^français de M. fiian-
ck', Q* édition, page 3 16, col. q, lig. 37.) — De là viennent
t^s-probablement, malgré l'altération d'orthographe, l'anglais
halcany, le portugais balcâo, l'italien balcone, l'espagnol et le
français balcon, servant à désigner une galerie avec balustrade
devant les fenêtres d'une maison.
BALDAQUIN, s. m. (a.)
Cp mot , qui désigne un dais nu-dessus dun lit, d'un trthie, etc..
l
=== grep balcon in PHN ===
2109:BALCON, s. m. composé, (p.)
2116:halcany, le portugais balcâo, l'italien balcone, l'espagnol et le
2117:français balcon, servant à désigner une galerie avec balustrade
10273:Balcon, s. ni. compose, (p.) Page 55
```


## [2026-09-05T14:06:19.265Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 215 216 217; do echo \"=== leaf $n ===\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n+1' KNT.txt | head -40; done"
}
```


### [2026-09-05T14:06:21.261Z] TOOL RESULT

```
=== leaf 215 ===
rada&a, duvaista-. dürau lsn. as adv. ‘afar, far away, far and wide’ (GAv. düiré, LAv. duire, Skt. d'ré; $65, 6191.111) DNa 44. duraty apiy DSe 11, DZe 6, DE 18, XPa 9, XPb 18, XPe 8, XPd 13, XPf 13, XPh 10, XE 18, XV 14, A'Pa 14f°, A’He 17. düraiapiyy DNa 12, dürayapiy DNa 46 ($18, $136).
duradasa adv. ‘from afar’, with preceding hacá: dūra- + adv. -dä asin отада + abl. -ša asin avada&a (§135, 5191.1; ЈАО 54.37).  DSf 23.
duruj- vb. ‘lie, deceive’: Av. druj- ‘le’ (draog-, Bthl. AYW 767), pres. druZasti, sb. druzé ‘principle of evil, devil’, Skt. drúhyatí ‘deceives’, Gm. trügen, pIE *dhrugh- (876.111). See alsodrauga-. adu- rujiya imf. (§101, $103.IV, $113, 5128, 4132.1, 2, 3, $214, 5228.11) DB 1.39, 78; 3.80; 4.8, 10f, 13, 16, 18, 21, 24, 261, 29; DBb 2; DBc 2; DBd 2; DBe 3f; DBf 1; DBg 2; DBh 2f; ОВ! 2f; DB} 2f. adurujiyasa" 3d pl. imf. ($214, §218.1, $232.III) DB 4.34f. duruxiam nsn. past pte. pass. ($103.IV, $122, $128, 8132.1, 3, $242.I) DNb 52, 5f; asn. DB 4.44f, 49f.
duruva- adj. ‘firm, secure’: Av. drva-, Skt. dhruvd-; deriv. to root in OP ‘dar- ($122, $128, $150). durwä nsf. DB 4.39.
duvatsta- adj. ‘very long, very far’: superl. to dūra- ($156.IIL, §190.11 $191.0; МВ Gr. $275), ef. Skt. davisthd- with slightly different formation.
192 OLD PERSIAN
duvais[ta]m asn. as adv. ‘for a long time’ DPe 23 (cf. remarks s.v. hyà).
duvara- sb. ‘door’: Av. dvar-, Skt. dhvar-, Gk. дора, Lt. forés, NEng. door, Lith. dvéras ‘court- yard’, pIE *dhuor- dhur- and its extended forms *dhyoro- etc.; see also duvarfi-. duvarayd-maiy lsn. ($186) DB 2.75; 89f.
duvari- sb. ‘portico, colonnade’: duvar- ‘door’ + varði- ‘cover, protection’, to root var- ‘cover’, with haplology ($34, $129, $152.IV, §160.Ia; ВЫ. AIW 766). duvarfim asm. XPa 12.
duvitdparanam adv. ‘one after the other, in succession’, a meaning agreeing with Elam. Samak- mar ‘ex ordine’: duvità ($191.11, $204.IT), MPers. dit ‘one or other of two’ (Bthl., quoted by Tm. Lex. 102), ef. OP duviliyam ‘a second time’, Skt. 0015 ‘twice’, Lt. bis, + paranam ‘before, previ- ously’ (Tm. 1.е., and Vdt. Stud. 1.8). This is better than Tm.’s "long aforetime', adv. duvità ong’, GAv. дайа, Skt. dvità (cf. OP duvaistam), + paranam (as above); also than KT's duvità- parnam ‘in two lines’, contaming the cognate of Skt. parnd- ‘wing’ (supported by Wb. ZDMG 61.724-5, KIA 10-1, and by Hz. AMI 1.112n). DB1.10; DBa 17.
duvitiya- adj. ‘second’: GAv. daibitya-, LAv. bitya-, Skt. dvitiya-, pLE *dyitiio- (676.11, 51441, 5204.1). See also duwilàáparanam. дилат, asn, as adv. ‘a second time’, DB 2.87f, 57, 3.77; as inner obj., ‘a second (uprising), DB 3.24 (not duvitiya-ma udapalalà ‘was second to rise up from me’, as Bthl. AiW 964 takes it, since udapatatà nowhere else takes an expression of the person against whom uprising is made).
duš- insep. prefix ʻi: Av. dui-, Skt. dus-, Gk. dve- ($76.Ш); in dušiyāra-, duskarta-.
dusiyara- sb. ‘evil year, bad harvest, famine’: duš- + yar- ‘year’ made thematic, Av. ydr-, Gk. ёра ‘season’, NGm. Jahr ($140.VIT, $143.IT). dušiyāram nsn. DPd 19. dudiyard absn. DPd 17.
| du$karia- ad). ‘ill-done’, opposite of naiba- (Hz. ApI 1434): duš- + karta- ‘done, made’, past pte. pass. tokar-. duskartam nsn. DSe 31f; XPh 42. draug- vb., see duruj- and draujiya-.
drauga- sb. *the Lie", the evil force opposed to Ahuramazda, Ávestan Druj: Av. draoga-, NPers.
dury, Skt. drógha- droha- ‘(malicious) injury’, pIE *dhrougho-, cf. NGm. Trug ‘deceit’, and OP duruj-, draujana-, draujiya- (870, 576.11, $101, $108.IV, $106, $122, $128, 5132.2, 3, $143.I, V). drauga nsm. DB 1.34, 434; DPd 20. draugà absm. DB 437; DPd 17f.
draujana- adj. ‘deceitful’, i.e. ‘adherent of the Lie’: deriv. of drauga- (§101, 5132.2, 5147.1), cf. GAv. drogvant- ‘adherent of the Dru? (Hz. Apl 140-1). draujana nsm. DB 4.38, 63, 68. drauja- nam asm. DNb 12.
draujiya- vb. ‘regard as a lie’, denom. to drauga- (S217). [Отау уау 2d sg. subj. (§222.11, §227.1) DB 4.43.
drayah- sb. ‘sea’: Av. zrayah-, NPers. dáryà, ·
Skt. jrdyas- ‘expanse’, pIE *órejos- (§88, $113, $128, $156.II). Decl, §185.1. See also para- draya. draya asn. DB 5.23; DP
=== leaf 216 ===
e 15; DZe 10. drayahya lsn. ($136, §251A; wrongly taken as gen., Hz. АрІ 141-3) DB 1.15, DPe 14, DSe 28°; drayahiyà ($27) XPh 23.
naiy adv. ‘not’: Av. 207, РЫ. në, Skt. ned; :
from pIE *ne, Skt. na, Lt. ne-scio ‘I don't know’, -+ Эа, asn. of pron. i-, Lt. id, OP id-am, ete. (869, 884, $191.1, $291.11, §292a). DB 1.32, 48, 49 ter, 52, 53, 71, 91°; 221, 24, 31, 51, 84; 3.15, 86; 4.44, 47 bis, 51, 55, 58, 63 bis, 63f, 64°, 65 bis; 5.16°, 31; DPd 11; DNb 7f, 12, 13, 21, 23, 36, 40; DSe 36, 40 bis, 43°; DS} 3; XV 22. nai-maiy (836) DB 4.64. nai-ma DNb 8, 10, 19. nai- pati-mà (8133) ОМ 20. nai-&im DB 4.49. naty- diš ($136) DB 4.73, 78.
naiba- adj. ‘beautiful, (religiously) good’, re- .
placing GAv. vahu- ‘good’, and opposite of duš- karta- (Hz. AMI 8.68, ApI 266-7): NPers. nē ‘brave, good’ ($11, §75.V, $148.11). пафа nsf. DPd 8. naibam nsn. XPa 13, 16; XPg 4; XV 20. naibam asn. DSe 32°; DSi 4^; DSp 2f°; XPh 43.
naucaina- adj. ‘of cedar’: NPers. nóZ, пдѓап ‘pine cone’; therefore naucaina- ‘pine-cone-shaped’ ($147.11), appropriate to the cedar (König, Burg- bau 53-4; Hz. AMI 3.58). naucaina nsm. DSf 30f. |
nab- vb. ‘perish’, causative (8123.2, $215) "in- jure; destroy’: Aw. )nas-) ӨЮ. naé-, Gk. vexus
7 ыйсы аЙ eet NUI ШЕЛ, АМАА а аз an ШО. Дені. Zr é
DD де 5... anes
LEXICON
‘corpse’, Lt. acc. nec-em ‘destruction’, nocet ‘harms’, pIE *nek- (887).
vi- + nab- caus. ‘injure, harm’: vindPayatiy (8215) DNb 17f. viyanatlaya imf. (§122, $1232, $215) DB 4.66. vinátayá"tiy За pl. subj. (8222.1I, §232.1) A’Sa 5°, A?Ha 7° (conj. Kent). vinátayais opt. ($215, $223.II, $228.11) DNb 20, 21. vi- nastahyd gsn. past pte. pass. as sb. ($03, $122, $242.11) DNb 18.
Nadi"labaira- sb. ‘Nidintu-Bel, a Baby- lonian rebel: Elam. nu-ti-ut-be-ul, Akk. ni-din-ti- йе] (§75.V, §76.V, $107). Naditabaira пзш. DB 1.77, 92f; 2.1; 4.12; DBd 1. Naditabairam asm. DB 1.80, 84; 24, 5. Naditabairahyà gsm. DB 1.85, 89, 95.
napüt- sb. ‘grandson’: Av. Skt. napat-, Lt.’
nepos, pIE *nepot- (875.1, §110, $142). napa nsm. (§124.5, §188.1) AmH 4; DB 1.3; DBa 4; А:Ра 16°.
Nabukudracara- sb. ‘Nebuchadrezzar’, son of Nabonidus; name assumed by the rebels Nidintu- Bel and Arkha: Elam. nab-ku-tur-ra-sir, Akk. nabu-kudurri-ugur (82, 833, §75.V, $128, §163.- VD. Nabukudracara nsm. DB 3.80f, 89; 4.14, 29f; DBd 3f; written Nabukuracara ($52.V) DBi 5f. Nabuk*dracara (822) DB 1.78f, 84, 93.
Nabunaita- sb. ‘Nabonidus’, last king of the New Babylonian Empire, 556-39. в.с: Elam. na- bu-ni-da, Akk. nabü-na'id; Gk. Aaßivnros (Hat. 1.74, ete.). Nabunailahyà gsm. DB 1.79. Na- bunaitahya (§36.1Vb) DB 3.81; 4.14, 30; DBd 5f; DBi 7f.
niman- sb. ‘name’: Ау. náman-, NPers. пат, Skt. náman-, Lt. nomen, pIE *nómen-, cf. Gk. буора, NEng. name ($109, $110, 5155.11). See also Andmaka-. náma^, suffixless lsn. used with mase. and nt. generic nouns to denote specification ($112, $187, §251C, §312): DB 1.28, 30, 36, 37, 74, 77, 92; 2.8f, 9, 14°, 19, 22, 29, 38, 49, 65, 79, 82, 95; 3.5, 12, 13, 22 bis, 31, 34, 44, 51, 56, 78, 84; 4.8, 10, 12f, 15f, 18, 20, 23, 26, 29, 83 bis, 84 bis, 85, 86°; 5.5, 8, 27; DSe 45°; DSf 31, 46; Юле 9; XPf 18, 19; А?Не 14f; A?Pa 19, 20; Sa 2f. nama, either asn. *ndmá ог lsn. лата” (with lengthened grade), specialized for similar use with fem. generic nouns because of similarity of end- ing ($67.1T, $187, §249L, $312; cf. Tm. Lex. 105,
193
with lit.; not with Foy, KZ 35.11, 37.505, IF 12.172n, nor with Debrunner, IF 52.153): DB 1.58, 58f; 2.271, 39, 44, 52, 59, 72; 3.11, 23, 61, 66, 12, 19; 54°.
nay- vb. ‘lead’: Av. nayeitt, Skt. náyati. Conj., §213. anaya imf. DB 2.88; 3.88°; 5.12. [ajnaya" 3d pl. imf. ($232.11) DB 5.28. anayatá imf. mid. as pass. ($235.П) DB 1.82, 2.73; 5.26". Some or all of these are possibly ànay-, from à + nay-. | fra- + nay- ‘lead forth, provide’: fránayam Ist sg. imf. ($226.11) DB 1.87.
nar- sb. ‘man’: Av. Skt. nar-, Gk. дир, cf. Lt. Ner-6; i
=== leaf 217 ===
n üv-nara- (§142).
nàv- sb. ‘ship’: Skt. ndus, Gk. vais, Lt. nav-is, pIE *ndv- ($142). See also ndviyd-. [naval прі. (8183.1V) DZe 11 (supplied by Tm. Lex. 52).
navama- adj. ‘ninth’: Ау. паота-, Skt. navamá-, pAr. navama- remade from pIE neyeno- after pAr. dasama- ‘tenth’ ($14911, $204IV), ef. Lt. nénus.  navama пзш. DB 1.10; DBa 10f.
naviyd- fem. adj. as sb., ‘navigability’, i.e. ‘impossibility of fording the river on foot’: Av. nàvaya- ‘navigable’, Skt. navyd-, adj. to nàv- ‘ship’ (§144.V). Hardly collective, ‘collection of ships, flotilla’, and certainly not lsf. to nav-, ‘on ship- board’; ef. König, RulD 70-1, and esp. Kent, JAOS 62.269-71 (with lit.), 63.67. ^ nàviyà nsf. DB 1.86.
nàh- sb. ‘nose’: Av. nàh-, Skt. nds-, Lt. narés, NEng. nose, pIE *nds- (5110, $142).  náham asm. (81181, §185.1V) DB 2.74, 88f.
ni- prep. and verbal prefix ‘down’: Ау. ni, Skt. ni-, pIE *ni; in adv. nipadiy, and with verbs ar-, kan-, cay-, pa10-, yam-, std-, had-.
nij- verbal prefix ‘away’: sandhi form of pIE *nis- before voiced stops, generalized, cf. Av. niš-, Skt. niş- ($120); with verb ay- ‘go’.
nipadiy phrasal adv. and prep., ‘on the track of, close after’: prep. ni- + loc. padiy, to pad- ‘foot’ ($76.11, $136, $140, $191.1V). тарайту adv. DB 2.73; prep. with acc. DB 3.73.
nipisti- sb. ‘impression’: deriv. of ni- + paid- ($152.11).  [niplisftiya] Isf DB. 4.90 (conj. of Kent, JAOS 62.268).
194 OLD PERSIAN
niydka- sb. ‘grandfather’: Av. nyáka- ($146.- HI); ef. apaniyüka-. {nilyaka nom. DSI 13; [n*yd|kama (522; for -Кат-тату, $41, §52.1, $130, $138.I) asm. A’Sa 4.
niyaSadayam, see had-.
Nisdya- sb. ‘Nisaya’, a district in Media: Elam. nu-is-fa-ja, Akk. ni-is-sa-a-a (5116). Per- haps from ni- ‘down’ + sdya-, to root Av. st- say- Tie’, Skt. §-, Gk. кт. ‘Ties’, pIE *kei-. Nisdya nsm. DB 1.58. |
niXadayam, see had-.
nüram adv. ‘now’: Av. nürom; from pIE *ná ‘now’ (Av. nū, Skt. пй, Lt. nu-nc, NEng. now) + final of (pAr.) *düram ‘long’ (§148.1), cf. düraty. DB 4.53.
pä- vb. ‘protect’: Av. pà-, pres. рйи, РЫ. pátan, Skt. pà-, pres. pati (ablaut, §122). See also zíacapüvan-. apayaiy lst sg. imf. mid. (Ву. BSLP 33.2.151-2; Kent, Lg. 9.42; S71, $214, $233.1II; wrongly to Skt. pt- ‘swell’, Wb. ЖА 41.820-1) XPf 39. padiy 2d sg. imv. (5208, §237.1) DPe 21f. pätwv (§208, $297.IT) AsH 12, 14; DPd 16; DPh 10; DNa 52; DSe 50; DSf 57; DS} 6°; D8n 2°; роз 7°; DSt 8°; ОН 8; XPa 18, 20; XPb 28; ХРе 12, 15; XPd 18; ХР 45, 48; XPg 13; XPh 57; Хе 5^; XV 25f; А:Ра 226; D'Sa 3; A?Hb^; A?He 19. pätw 3d pl. іту. (§237.1T) A'Sa 5°; A’Sd 4; А?На 6°; A?Pa 25. pála пзш. past ptc. pass. (§242.IT) DPe 22. pati- + pã- mid. ‘protect one’s self against’, with Ласа + abl.: райїрауаш@ (828; not wrongly written, despite MB Gr. §69) 2d sg. imv. mid. ($71, §214, 5297.11) DB 4.38.
paié- vb. ‘cut, engrave, adorn’: Av. paésa- ‘adornment’, Skt. pisdtz ‘cuts, adorns’, Gk. токіћоѕ ‘variegated’, OCS pisati ‘to write’, pIE *peik-, cf. Lt. pingit ‘embroiders, paints’ (Wb. AfOF 7.42). Cf. also nipišti-, parsiyd-, Paišiyđwwādā-, pisa-. аріа imf. DSf 54 (§211; cf. Konig, Burgbau 72). [ар #} уа] imf. pass. ($220) DB 4.91 (JAOS 62.268). [pjisia nsf. past pte. pass. ($242.1) DSf 42 (Bv. BSLP 30.1.62; Konig, Burgbau 71; not dista with Hz. Apī 121-5].
mi- + pub- ‘engrave, inscribe, write’: niyapat- Sam Ist sg. aor. ($02, $102, $130, $218.T, $226.IT) DB 4.71. mipaislanaty inf. ($03, $122, $288) XV 24f. nipislam asf. past ptc. pass. (803) XV 22f.
nipistü npf. XPh 31. nipistam nsn. ($122) DB 441, 47f; DNb 57°; DSe 52.
paišiyā- sb. ‘script, written text’: deriv. of pai- (§89, §144.V). See also Parsiyduvada-. ри nsf. DB 4.91 (conj. of Kent, JAOS 62.268).
PaiSiyd'uvdda- sb. ‘Paishtyauvada’: АКК. pi- &-"-hu-ma-du. Perhaps,
```


## [2026-09-05T14:06:28.884Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Bardiya\" KNT.txt | head -5; echo \"=== bar- entries ===\"; awk 'BEGIN{RS=\"\\f\"} /Bardiya- sb/' KNT.txt | head -c 6000"
}
```


### [2026-09-05T14:06:30.811Z] TOOL RESULT

```
563:! Greek єр is not conclusive evidence for 7, despite xépoa = karía- and Zytphs = Bardiya, both with у ($80); ef. "Гутафёриує = Vitdafarnd, with -ar-, and 'Apseáum = Aršāma and 'Apratiptys = ArtaxSacd, both with r by the Elam. testimony, despite Gr. ар-. Several Greek transliterations of place-names have ap for Persian ar: Tapa = Paréava, Xayapría = Asagaria, etc.
573:Bardiya = Brd-, Elam. bir-ti-ga.
1039:bond, from pIE bh-.. pIE *bhergh- ‘be high’, in Bardiya-, barSan-,
1940:a. Names of the Achaemenian dynasty: Ari- ? ydramna-, Árlaxíaga-, Aríüma-, Uvarstra- (M), Kabüjiya-, Küru-, XSayarSan-, Gaubaruva-, Cifpi-, Darayavau-, Bardiya-, Vistüspa- (M).
2662:C. As direct object anticipating the subject of an object clause: DB 1.52f. matyamdm xindsdtiy iya adam пазу Bardiya атту "lest (the people) know me, that Ї am not Smerdis'.
=== bar- entries ===
2; 4.66. abara imf. ($40, $84, 5228.) DB 1.25, 55, 88, 94; 2.25, 34f, 40, 45, 54, 60, 68, 86, 97^; 3.6, 17, 37, 45, 62, 67 (written ar?r^, 854.11), 87; 4.61, 62; DNa 50f; DSf 19°, 32; XPh 33, 45. abara” 3d pl. imf. ($10, $40, $84, $106, 8232.1) DPe 10; DSe 18°; DSf 34. aba- raha” 3d pl. imf. ($10, $218, $282.11) DNa 19f; XPh 17 (written орт, §54.1). abara"tà 3d pl. imf. mid. ($10, $236.II) DB 1.19. abariya imf. pass. (535.1, $220, $228.IT) DSf 23°, 31f, 35, 36, 38f, 40, 48, 45. abariya" 3d pl. imf. pass. ($220, 8232.11) DSf 41, 47.  baratuv imv. (5237.П) AmH 11^; DPd 14; DSk 5. аталаш inf. ($238) DNb 41.
à + bar- ‘perform’: dbaratiy ($218, $228.1) DNb 25. Cf. also Hz. Ар] 110-1, who refers to à-bar- certain other forms listed above as augmented forms of uncompounded bar-.
pati- + à + bar- ‘bring back, restore’: райуй- baram Ist sg. imf. DB 1.68 (but -à- perhaps only by influence of pardbartam, JAOS 62.275; 558, $206c).
para + bar- ‘bear away, take-away’: pardbara imf. DB 1.71, 96. pardbartam nsn. past pte. pass. (§242.1) DB 1.62, 67f.
pari- + bar- ‘protect, preserve’ (cf. Hz. Ар 112-3): paribarümiy Ist sg. (8226.]) DNb 17. paribarühy 2d sg. subj. ($27, $136, §222.IT, 4227.1) DB 4.78; paribaráh*-di$ (827, etc.) DB 4.74. pari- barā 2d sg. imv. (5237.1) DB 4.72, 88.
fra- + bar- ‘proffer, grant’: frábara imf. AmH 7; AsH 9; DB 1.12, 25, 60; DPd 3f, 7f; DPh 8; DNa 33; DSf 11; DSm 3°; DSp 2°; D8s 6; DZc 4; DH 7; A’He 18f, 20.
bara- sb. ‘bearmg, bearer’: Av. -bara-, Skt. -bhara-, Gk. -фороѕ, pIE "bhoros ($32, $122, $1431, ҮТ), to root bar- ‘bear’, in aritibara-, takabara-, vacabara-; also bāra- ‘borne by, rider of’, with vriddhi (8122, $126, 5148.1), in asabdra-, ef, usabüri-. See Hz. Ар] 95.
bard- vb. ‘be high’: Ау, baraz- ‘high’, baraz- ant- ‘lofty’, NPers. burz ‘high’, Skt. brhánt- ‘lofty’, OHG berg ‘mountain’, pIE *bhergh-; in Bardiya-, barsan-, probably in brazman-.
Bardiya- sb. Smerdis’, brother of Cambyses ($16411): Elam. bir-h-ia, АКК. bar-zi-ia, Gk. Урёрӧ ($29.02, $30). Репу. (§144.1V) of OP bard- ‘be high’ (575.11): ‘The Exalted’. Bardiya пет. DB 1.30, 32, 39, 52f; 3.25, 35, 54; 4.9, 27, 82; DBb 4f; DBh 5. Bardiyam asm. DB 1.31 bis, 51.
barSan- sb. ‘height, depth’ (S81): Av. barazan- .
(ВМ. AiW 950); deriv. of OP bard- (575.1, $155.1; Scheil 21.26; Konig, Burgbau 51; Hz. AMI 3.57; Bv. Gr. $812; Kent, JAOS 51.204, 99.15). bar$nà ism. (806, $120) DSf 26, 26f.
bav- vb. ‘become, be’: present stem bava- (8213), Av. bavatti, Skt. bhdvati, Gk. ote ‘grows’, Lt. fut ‘I was’, Lith. butt ‘to be’, NEng. be, pIE *bheu-. See also büm:-. bavatiy (§122, §228.1) XPh 55, 56. bæa"ty 3d pl. ($232.1) DNb 14 (башайу in 2d copy, Hz. ApI 115; ef. $48). abavam Ist sg. imf. DB 1.28, 60, 72; 4.5; 5.4^; DSm 6°; XPf 35, 36f; XPh 30; XSe 4°. abava imf. ($228.IT) DB 1.32, 38, 34, 40, 48, 77, 80; 2.16f, 17, 80, 94; 3.10, 11, 20, 27, 28, 76, 82, 83; 5.5, M^, 30; DSf 25; XPf 26.  abava^ 3d pl. imf. ($112, $232.IT) DB 1.76; 2.7, 93; 3.78; 4.34. bavātiy sub). ($222.11, §228.1) DNa 43, 45f; DNb 59 (Lg. 15.74; confirmed by photograph, JNES 444). [biyjä 2d sg. opt. ($114, $218.11, $223.I, $227.11) DB 4.69. буй opt. Cbhy-net, Bv. Gr. $232, comparing Av. buyd{ from *bhu-iët; but ВЫ. Gdr. IP 1. $143 takes as *bhy-i48t, = Lt. fiet, which may be either non-thematie opt. or thematic subj.; $114, $122, 5208, $218.II, §223.1, $228. ID) DB 4.56 bis, 58, 59, 741, 75, 78f, 79°.
bigna-, in d-bigna-, see Bagabigna-.
biimi- sb. ‘earth (= world or ground)’: Av. bümi-, NPers. büm, Skt. (RV) nom. bháümi bhümis; deriv. of root bhav- (see bav-) in grade bhi-, cf. Skt. aor. ábhüt, Gk. ёфо ($11, $65, §152.1V, §179.- IIT).
LEXICON
bümim asf. DNa 2, 32; DSe 2°; DSf 1; DSt 2; DZe 1f; DE 2; XPa 1; XPb 2; XPc 1; XPd 2; XPf 2; ХР 1f; ХЕ 3; XV 2f; A!Pa 2^; A?He 2. ратат, asf. ($55.1) A3Pa 2. bümiyà sf. (8179.IT) DNa 11f; DSb 9; DSe 10; Рб 5; DSs 2°, 3°; DZb 4; DZe 6; DE 17f; XPa 9; XPb 17; XPe 7f; XPd 12; XPf 12, 25; XPh 10; ХР); XE 17; XV 13; A'Pa 18°; A?8e 4°; Wb 7; Wc 8; Wd 8.
BU nsf. ($42) DSf 24, 28.
```


## [2026-09-05T14:06:37.502Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"brazman\" KNT.txt | head -10"
}
```


### [2026-09-05T14:06:37.551Z] TOOL RESULT

```
596:brazmaniya, Elam. pir-ra-1s-man-ni-ta.
1040:brazmantya-; see Lex. s.vv.
1494:pIE gh: brazmaniya-, Uvárazmi-, игта-, züra-, zü- rakara-.
1498:It is to be noted that OP 2 remained unchanged before m, as in brazman-, though it became voice- less (and was further changed) before m, as in baránà. But the zm which was retained in GAv. became sm in ТАУ.
1793:IV. Other formations, ineluding some personal names: agr-iya- to agra- (5148.1), батшап-їуа-, daran-ija-, brazman-iya-, mart-iya- to marta-, haš- iya- to hat- (8240), ha-mic-iya- to mitra-; Artavard- iya-, Ka"büj-iya-, Bard-iya-, M ardun-tya-.
1854:III. Stems in -man-: as-man-, lau-man-, nā- 4 man-, braz-man- in adj. brazman-tya-, yau-man- in. 4
2238:1! Nom. hamiciya DB 2.93 is predicate to two singular masculine nouns, but is more probably plural than dual; ef. $259. ? The form karšā does not belong here, nor probably artá-cà brazmanty (if во normalized) nor tau- mani-Saty; on these words see the Lexicon s.vv. * On these forms, cf. Kent. Lg. 19.225;
4596:41 iy : агійса : brazmaniya : uta : aniyas
4601:51 rtácá : brazmaniya : martiya : һуа : avan
4604:54 rtaca : brazmaniya : hauv : uta : iva :
```


## [2026-09-05T14:06:43.136Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} /brazmaniya- adj|brazmaniya- ad|brazman-/ {print NR\": \"substr($0,1,50)}' KNT.txt | head; echo \"---\"; grep -n -o \"brazmaniya-[^.]\\{0,300\\}\" KNT.txt | sed -n '1,8p'"
}
```


### [2026-09-05T14:06:44.620Z] TOOL RESULT

```
58: iizahya-, Izalà-.
It is to be noted that OP 2 rem
66: �urd-, Arbairü-, Arsada-, Izali-, Uyamá-, Kuga
68: , see Lex.:s.v.; on fem. aruva- as abstract, see L
225: 2; 4.66. abara imf. ($40, $84, 5228.) DB 1.25, 55,
226: BUyà Isf. DSd 2°; DSf 7, 15, 16, 18, 24^; DSg 2;
---
1494:brazmaniya-, Uvárazmi-, игта-, züra-, zü- rakara-
5748:brazmaniya- adj
```


## [2026-09-05T14:06:46.549Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '5745,5755p' KNT.txt"
}
```


### [2026-09-05T14:06:46.596Z] TOOL RESULT

```
bümim asf. DNa 2, 32; DSe 2°; DSf 1; DSt 2; DZe 1f; DE 2; XPa 1; XPb 2; XPc 1; XPd 2; XPf 2; ХР 1f; ХЕ 3; XV 2f; A!Pa 2^; A?He 2. ратат, asf. ($55.1) A3Pa 2. bümiyà sf. (8179.IT) DNa 11f; DSb 9; DSe 10; Рб 5; DSs 2°, 3°; DZb 4; DZe 6; DE 17f; XPa 9; XPb 17; XPe 7f; XPd 12; XPf 12, 25; XPh 10; ХР); XE 17; XV 13; A'Pa 18°; A?8e 4°; Wb 7; Wc 8; Wd 8.
BU nsf. ($42) DSf 24, 28. BUyà Isf. DSd 2°; DSf 7, 15, 16, 18, 24^; DSg 2; DSi 2, 4; DS) 1°; DSy 2; D'Sb 2; A’Sa 1; А4 2; A?Ha 2; A?He 9, 17; А?Ра 11.
brdtar- sb. ‘brother’: Av. brätar-, NPers. biraddr, Skt. bhratar-, Gk. @parnp ‘clan-brother’, Lt. frater, OCS bratru, Gt. brobar, pIE *bhráter- (862, 875.111, $128, $154.П). баі nsm. ($124.5, 5186.1) DB 1.29f, 39f.
brazmaniya- adj. ‘prayerful, reverent’ (cf. Kent, Lg. 21.223-9), with braz- rather than barz- (883; cf. Elam. pir-ra-us-man-ni-ia, АКК. bi-ra- 2a-man-ni-1): deriv. (§144.IV) to pAr. antecedent of Skt. bráhman- ‘religious devotion, prayer’, ef. identical Skt. deriv. brahmanyd- ‘religious’, to pIE root *bhergh- (see OP bard-; $75.1II, §95, $120, 5155.11; Henning, TPS 1944.108-18). For other views, see Kent, Lg. 13.301; Hartmann, OLZ 40.145-60; Nyberg, Rel. 367, 478; Hz. AMI 8.69, Apl 116-8 (to Av. barag- ‘to welcome’, barag- ‘rite’, Бәтәгба- ‘beloved’; wrongly, since this would give OP *bragman-); Christensen, Essai sur la démonologie iranienne 40-1; Henning, BSOS 10.506; Abayev, Iranskie Yazyki 1.134; Scherman, JAOS 65.141-3 n.23. Cf. also О. M. Dalton, Treasure of the Oxus 94-5. On form and meaning of РЫ. brahm brahmak, see Henning, TPS 1944. 108-18. brazmaniya nsm. ХР 41, 51, 54 (hardly brazmaniy isn. modifying arid; also not -niy apn. ‘divine’ with Sen 155, nor adn. in elliptic dual with Pisani, see under aria-).
т°, of dubious meaning, Se 1; taken by Justi, IFA 17.112, to be an abbreviation for OP *méraka ‘seal’, NPers. maráh.
та-, stem of ist person pron. in obl. cases of sg.; see adam.
mà conj. ‘not’, in prohibitions ete.: Av. Skt. mà, Gk. шӯ, pIE *mé ($109, §191.1, §292b). With subj.: DNb 55 (mé-taty), 58. With opt.: DB 4.59, 69, 79°; DPd 18, 19 bis, 20; XPh 39. With
201
inj.: DB 4.54; DPe 21; DNa 58, 59, 60; DNb 52 (mà-lay). With imv.: DNb 60. With lost verbs: DNb 57, DSq 4 bis; with restored subj. A'Sa 5^ bis, A?Ha 7, 7°. See also mdtya.
mā- vb. ‘measure’: Av. Skt. ma-, Lt. métior ‘I measure’. à + må- ‘extend’: атӣій npm. past ptc. pass. (6242. П) ‘noble’ DB 1.7; DBa 11. fra- + mā- ‘command’ (‘decide, judge’, acc. to Hz. ApI 154-6; ‘plan,’ Hinz, ZDMG 95.233-5); see also framülar-, framdnd-. јтатауаіа imf. mid. ($214, 5285.11) XPg 5. framatam nsn. past pte. pass. ($242.IT) DSf 19f°, 56.
таш- vb. ‘flee’: meaning established by Мат. and АКК. versions (Hüsing, KZ 38.258); probably to Skt. munthate ‘flees’ (Jn. JAOS 38.122). атида imf. ($211) DB 2.2, 71; 3.41f, 71.
```


## [2026-09-05T14:06:59.723Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -oE \"b[əa]r[əe]z(an|ant|i|ra|man|ah|nu|yah)?-[^,;.]{0,120}\" BRT.txt | head -40"
}
```


### [2026-09-05T14:07:01.347Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-05T14:07:05.083Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for p in \"b.r.zant\" \"b.r.zaiti\" \"b.r.zi-\" \"barsman\" \"b.r.snu\" \"berezant\"; do echo \"== $p\"; grep -c -iE \"$p\" BRT.txt; done"
}
```


### [2026-09-05T14:07:06.686Z] TOOL RESULT

```
Exit code 1
== b.r.zant
6
== b.r.zaiti
2
== b.r.zi-
5
== barsman
0
== b.r.snu
4
== berezant
0
```


## [2026-09-05T14:07:08.926Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -iE \"b.r.zant|b.r.zi-|b.r.snu|b.r.zah|b.r.zan-\" BRT.txt | head -30"
}
```


### [2026-09-05T14:07:08.998Z] TOOL RESULT

```
6068:cistfm  'sa  (Instr.)  manta..  ahurSX.^i.  läj  fravasays..  barPsnUsca  'saht yat  vahistahe
6845:l)  von  Miira:     mfir^m  .  .  'r>m  gu/nm  ^b»r3zanta  ai'iyejauAa  asiivana  Yt.  10. 14$;
7444:•  j.  ärStyö.barazan-  Adj.  'von  Klafter- höhe': yim  upairi  *vis*rao(iat  -««(NSn.)'' "auf  dem  das  Gift  klafterhoch  floss"  Y. 9.11.
9048:•  j.  kaoba-  m,  Name  eines  Lands*':  upa dvarnn  xsairö.sukjm  (sd.)  apanöJtmjm 'hitva  *birizantaya  asavanaya  "bei  dem Pass  -Vj^,  dem  liöchstgelegenen  in  dem hochragenden  heiligen  K."  Yt5.  54.
14871:•  j.  patarvta-  Adj.  'im  Flug  hegTiSeii,i  nipai'.yante(s±)  Äqm  vä 'ti  stairi/Aqrri  vä fliegend':  äsyajgia  (sd.)  vayazibya  °taiibya\°ti  bartzi^  V . ^.  ^i .  b)  auf  die  Frage ". ,  als  ein  paar  fliegende  Vögel"  Y.  57. 28;  i  wo?:  talam  vantanhS . .  gätiis  'ti  ^ätjfante — pasubya  staoralibya  vayaeibya 'taäbya^^  (S'p.  i^^  n.)  Ytij.io;  —  ya^/a  argAaJ yS  parmJnS  (sd.)  fravazänte  "mit  Klein-  1  bartsnul  'ti  gairinqm  V.  2.  23";  Y.^.  26, undOrossviehundmittliegenden Vägeln, .. "1 /0.3; —  :i^armö  baxlmli  zqm  'ti  akura- YtJO.119.  \Vttqm   Yt.6.1,  7.3;  jp.48,'$o,  Y. 13.4g,
17017:•  j.  bar^zan-  m.  'Höhe':  kukatrlm  (sd.) banzS . .  yahmat . .  haca  fi-azgmaite  andvl . .  AazavrHi  (statt  GS.)  'nsha  (IS.)  vTranqm YL5.  g6";  —  xiva/paya  (sd.)  vaOtaya 'nSna  Y.  5. 1 1  PüZ.,  Yt  ig.  40.
17019:•  j.  barszah-  n.  'Höhe,  Berg':  *upa *tnaitlm  (sd.)  'zargAam  V.J.  30;  —  mihnm .  .  yS  vlsp)m  aham  .  .  Sdt6aili  haratkyät (sd.)  paiti  'zatakat  Yt  jo.  5 1 ;  —  barniste paiti  'zaÄi  haraihyS  .  .  Y.  ^y.  19;  — AuiaitJm  (sd,)  °zS  Ytj.  96,  12.  24;  —  ya (näml.  arfdvt)  .  .fratacaiti  hukairyät  haca 'zaftkat  Y.  65.  3 ;  Yt  5.  2  5.
17022:'Zum  V.  tarn-.  —  VgL  barizan-  and  Bthl. IF.  p  65.  —  Ptt.  (dRn.);  bäUitä»  bälist,  bälist Aac  bäliilän,
17184:•  j,  b^rszant-  Adj.  (fem.  -«aiff-)''  'hoch'; a)  von  a)  Menschen,  ß)  Göttern  und Y)  Tieren,  'hochgewachsen,  von  hoher Statur'  '* :  a)  nari  hhrpa  .  .  'satS  . .  ama- vatB  Yt<P.  13;  —  kaintnS  hArpa  ..  -xaiiyä  ^ a  2. 9 ;  ät  Vyt  56,  wo  'zantyä  i>.  ß)  am»-  j /anam  sptntanqm  . .  'zatam  Y.  26. 3 ;  zit Yt/5,15,  wo  •zantami'';  —  mi^nm  ahu-\
17203:•  j.  b^razi-gäSra-*  'hoch'  oder  'laut singend':  yim  zaotärttn  stayala  ahurS  ,  . °r}nt;  yazata  zaeta  .  .  'rd  b)r»zata  vaca YL  lo.  89.
17205:•  j.  bar9zi-8ä(y)- :  '%i~  Adj.  'von  hoher Einsicht':  'zaiiis'''  (NSm.)  iava  vlstäsps Ytj.  108,  5-19,  17.53; —  sraosfm  "zai- Im'^  (ASm.)  Y.57.  II.
17209:•  j.  bar9zi-mita-"  Adj.  'hochgemessen, hochgebaut':  nman?m  ..  't>m  Yt/o.  30; —  Hahe  nmanahe  Yt  IQ.  z8.
17213:•  j.  b9r»zi-räz-  Adj.  (auch  fem.)  'in  der Höhe  gebietend':  tti  Alm  (näml.  daHtam) dasta  maioyllisäopM  °räzpm  Yt.13.100.
17215:•  j.  bar«zi-3avah-  Adj.  Bezeichnung  einer der  fünf  Arten  des  Feuers**:  ättvm  (sd.) 'vaftkim  Y.i-j.  II.
18541:•  ).,  g.,  p.  naplt-:ffa//-  m.,  j.  naptar-: nafsir-  m.",  j.  naptl-  f.  'Enkel;  Enkelin': '  adam  d3ray^v(^ui . .  vistäspahya  puh^e^ arSätnakyä  '/J(NS.)'*  Eh.  j.  i;  —  'pS (NS.)"  ..  ■■//("  (NSf.)  i/a  V./2.11;  10;  — nyaka  haca  'ptöisSs,  (^\%y^  nyske  haca  'pti (statt  AblSf.)  V.  J2. 1 1 ;  —  hyai  us  alä napiyaisii  na/i'uCLP.yVä ..uzp//  (Sp.4gSm.)  ' fryänakya  aojyaiiü  '^.46.12.  a)  mit GP.  apam''  'Enkel  derWasser',  Name  einer Gottheit**;  a  dim  (näml.  3^ar)nö)  Hahra kangturvayat  apum  'ph  (NS.)  aun'at.aspö Yt.  rp.  s  1 ;  5 '".  '.7-  95^';  —  «/>?'»  >'»  (NS.) t&  ups  ,  .  aiiuhe  .  .  vi.baxsaiti  Yt  8.  34; —  b^ntantfm  ahuntn  xsa^rlm  xSaltitn apqm  'pättm  aurvat.asp?m  .  .  yB  upäpB yazatS  Yt  ig.  51 ;  Y.  2,  5;  —  apqm  'ptär?m yasamaide  nairJm  sanh^m  Y.  7/.  23;  — b»->sat3  ahurake  'fiorS  aPqm  apasca  maida- la/aya  Y.  r.  5;  —  b^ryza  a/iura  xsa^rya apqm  V»?(VS.)Y.6'5.ia.  _  a)Nameeiner jener  Gottheit  geweihten  Örtlichkeit*'  (oder eines  Husses,  einer  Quelle,  eines  Berges): tarn  (näml.  andriin)  yaznäa  . .  sSyuidrSis pu%ra  upa  b3r?zant?m  ahur>m  xsairim xsaWm  apqm  'paism  Ylj.  73.  [na/jonm Y. ij.ii:  s.  x/alirB.napiar-.\
20460:•  j.  'm^Sra-  n.  i)  'Gedanke';  im  Gegensau zu  Wort  und  Werk:  l)m  . .  yazamaide  . . 'raca  vacaca  syao'hnaca  Ny.;.i6.  2)'Be- denken,  Nachdenken  über  — ':  bar>snusia astzhe , .  tnasiiia  *ra  . .  vmsya  , .  urvaitya  . . Aai^yä.v>r3sya..v}ndai%ya  dalnaya  G.2.'j.
20536:'^rütihayete  rahtus  paiti^ranhayde  sraosS afyö  . .  hqtn.väiti  .  .  Yt  /O-  41 ;  J?.  16;  — sraoiaiea  . .  ratttvalca  . ,  'räiäz  Vr.  11.  6;  Y, ^5.12, 70.3,  Yt//.6;  vgl.  Yt.;o.ioo,  2)  in Verbindung  mit  raman-  (sd.,  auch  fdSt) s^ästra-:  'rahe  vourugaoyaatBil rämanasca sPäsirahe  Yt/o.o;  usw.  3)  Du.  in  Ver- bindung mit  aAura-  Du.^';  tala  nS  jamyat avaiähe  'ra  aAura  b)r»zanta  Yt.  /0. 1 1 3 ; 145;  —  aAura  'ra  b)r»zania  aüiya/aivAa Y.3.1 1 ; — aAuraäbya  'raiibya  b^rvzanbya.. Y./.ii.  Aa)  'raAe  {ataA.  ma)  hetsst  der 7.  Monat  im  Jahr:  %risat^m  ays^rimahe (sd.)  -raAe  anayraaqm  A._J.  10.  b)  *raA^ (näiuL  ayar»)  heisst  der  lö.  Monatstag: 'raAe  *vourugaoyaoteis . .  yasatahe  S.  1. 16; vgl.  2.16,  Y.  16.5.
21254:•  j-  yat-£it  Konjn.  i }  konzessiv  'auch  wenn, wenn  schon';  das  Verbum  {'aA-)  ist  weg- gelassen: y  usas/aire  Aimivs(sd.)  *ag»urva- yeiti  Y.57.  29;  29,  Yt /o.  104';  —  mit Praes.:  hs ..  iiva.vasmai^A^  apayeifi  ..y° vazaite  hvastim  YLJ4.20.  a)  im  Nach- satz steht  o)  Hl;  das  Verbum  i^ah-)  ist we^elassen:  y°  vimaSiim  aiAhA  umö tfmcit  mi%rB  kangr>fs3mnS . .  Yt/o.io4f.; 104.  ß)  atH},  mit  Praes.:  y  Avast?m (sd.)  *aiihyäti  y  tanüm  apayäti  atßt  dim nOii  räsayaiU {sd.)  Yt. /o.  zi.  2)  tem- poral; 'als',  mit  Praes.,  im  Nachsatz  steht atai  'da':  y°  mam  tura  (sd.)  pazdayanta aiiii  atitn  tanüm  aguze  .  .  a0i  . .  Yl  sj. 56'';  56.  3)  kondizional  'wenn,  so- fern'; mit  Praes.:  y  *pascaaa  aH'qm raiufrittm  ava.raooayäti  tanüm  *pirydli N.  4"^,  3)  wiederholt  'sei  es  dass  .  . oder  dass';  mit  Praes.:  y  ahi  raihvd .  .  upa  karlvars  yat  ar>sahi  zbayamaki . . y^  ..  Yt.  12,9-37;  —  das  zweite  Mal mit  Tmesis:  y  n^mavAa  väcim  baraiti yat  gai>s{sd.)cii  Yt.  10.  S$.  b)  das  Ver- bum (,'aA-)  ist  weggelassen:  vTspe  haoma upastaomi  y°  barisnuna  gairinam  y'  jaf- nu&a  raonqm  yaicit  azahu  ,  ,  V,  /o.  17.
28093:•  j.  zäi^y-  Adj.  'gelb,  goldfarben',  von Hagma:  kaoina  'ire  Y.(j.  30,  /O.  13,  Vr. 11.2';  Y.g.i"];  —  haomasca  °iris  b>r?z3 V,  ig.  ig;  —  Aaom^m  'irim  b>r»zant}m Y.;o.ii.
```


## [2026-09-05T14:07:18.564Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '17015,17030p' BRT.txt"
}
```


### [2026-09-05T14:07:18.610Z] TOOL RESULT

```
•  j.  *bar»Z-  :  b»nz-^'>  i)  Adj.  'hoch,  er- haben': ratüm  Äj/vwm  Vr,  2.  10;  —  ratSuS hmlf{GS.)  Vt.i.%]  —  Hitrlm  . . yahmät haca  binzät^^  haosravanhtm  (sd.)  Vlä 4,  a)  von  Tönen  'hoch,  laut';  yas3  . . bsDBtn  barat  zaota  väHm  Yt.//.  61;  — yat  bsnism  barst  astra  ('die  Peitsche') vaHm  Yt. /o.  113.  2)  'Höhe;  Berg': haraiti  (sd.)  Äar/{NS.))>  Yt.ifj.  i;  —  upa upa.bdi  Aj«ya  (sd.)  i.wvÄ?(GS.)  Ytj?.  3, Jj.  24;  —  talrfincH  harai'hyä  btrpzö  Y. 42. 3;  —  lainm  harai^yä  barisö  (GS.) Ytr2. 15;  —  karai^yS  paiti  bar^zayä (GS.)*>  Y.io.  10,  57. 19,  Vt  10.  50,  90;  — vispkhu  paiti  öanzähu*''  Yt/o.4S.  [FrBy.: lies  °b?nts  als  Komp.]
KompA.  (s.  auch  btr^Bräi-),  E.  —  Zum  V. bam-.  —  np,  burs  "iioch;  Höhe',  bälä  'Höhe'; air.  ifj'Berg",  Km.  rrkna-bcrj  'himmelhoch' S. —  Pü.  (lu  1):  buland,  (lua):  burz.  —  0  Idg. *ihir^h- :  *blinA:  Eriteres  in  np.  bä!-ä  (,  tU. in  arm.  'b(r/]'>1,  letzteres  in  np.  bun  (,  gol. baurg-it,  air.  bri,  brtg).  —  »)  Them.  —  3)  Üg. *bAtrxt  oder*W/-ji  (=  ult. bri);  IF.p.aöi.— 4)  Nach  der  ä-Dekl.  —  s)  Richter  IF.9.  zso nimmt  fälschlich  ai.  ^AitspdliA  aU  (cig.J'Ber- gesherr';  s.  va  bing-.  —  6)  Anders  Hbm.  AGr. /.  4*8.
•  j.  bar^zan-  m.  'Höhe':  kukatrlm  (sd.) banzS . .  yahmat . .  haca  fi-azgmaite  andvl . .  AazavrHi  (statt  GS.)  'nsha  (IS.)  vTranqm YL5.  g6";  —  xiva/paya  (sd.)  vaOtaya 'nSna  Y.  5. 1 1  PüZ.,  Yt  ig.  40.
KompE.  —  Zum  V.  bariz-;  vgl.  bariiiman- und  Bthl.  IF.  7.  59.  —  0  Vgl.  Bd.  12.  6: hukar  i  buland  an  it  äf  i  ardvisür  ha?  ai  frei äyet  1000  mart  bälät.
•  j.  barszah-  n.  'Höhe,  Berg':  *upa *tnaitlm  (sd.)  'zargAam  V.J.  30;  —  mihnm .  .  yS  vlsp)m  aham  .  .  Sdt6aili  haratkyät (sd.)  paiti  'zatakat  Yt  jo.  5 1 ;  —  barniste paiti  'zaÄi  haraihyS  .  .  Y.  ^y.  19;  — AuiaitJm  (sd,)  °zS  Ytj.  96,  12.  24;  —  ya (näml.  arfdvt)  .  .fratacaiti  hukairyät  haca 'zaftkat  Y.  65.  3 ;  Yt  5.  2  5.
KompE.  — ■  Zum  V.  barix-,  vgl.  'banx:  — Fü. :  buland,  (zu  V.):  pa  bälisl,  erl.  ifatari  kif.
•  g.,  j.  baraziman- Adj. 'hoch':  imä  raeüa bartziit^m  •zimanqm  avat  (sd.)  yai  hvarJ avaaY.36.6i  —  Avan  bar7zisi?m  'zima- nqm Vr.  IQ,  2.
'Zum  V.  tarn-.  —  VgL  barizan-  and  Bthl. IF.  p  65.  —  Ptt.  (dRn.);  bäUitä»  bälist,  bälist Aac  bäliilän,
•  j.  bar9zi§-  n.  'Polster,  Kissen':  >?  narS hämS^ätvü  nipaüyeinte  Aqm  vä  paiti  stairis Aqm  vä  paiti  '«/V.J.  27;  —  cvat  alte slairisca  °tisca  aesa  druxs  .  .  fräshaoiti V.  7-9;  —  aitaoa  altahe  aste  (Sp.  340) slairii^a  °zi/^a  hqm.v^rtnattte  V.j.  59;  — ana  'zis  sayamnanqm  (sd.)  V.  lü.  26;  — gätu  *x''aiiii.star»tu  (sd.)  mai  °ziia  V. 7^14.         [Yt5.  loa:  lies  bar^zi/Aav'.]
KompE.;  Ableit.  —  ai.  barAif^n.  'Opferstren', np.  bälis  'Kissen';  vgl.  ai.  ufabärAaria-  n. 'l'olster'.  —  Pü.:  bälisn.
•  ].,  g.  baraziäta-  Adj.  'der  höchste,  hüchst- gelegene':  'te paiti  bantaAi  Aaraiiyg paiti bansayä  Y.  57.  19;  —  'taiibyS  gairibyö V. 2. 22;  —  'laihiaia  paiti  gätuha  V, 6^.45;  —  urvaranqm  .  ■  ysi  hftiii ..  'taca V.  2.  28; —  imä  raoiä  't?m  bar»zimanqm
dby  Google
951
^barfzi&havant-
I
V.^.6;  Yi.ig.2.         a)  'sehr  ticT:   -U
```


## [2026-09-05T14:07:21.448Z] TOOL CALL #25: Bash

```json
{
 "command": "ls site/pages/92.jpg 2>/dev/null; pdftoppm -f 92 -l 92 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg92 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/"
}
```


### [2026-09-05T14:07:23.671Z] TOOL RESULT

```
site/pages/92.jpg
total 30440
drwx------ 2 sfmqrb sfmqrb     4096 Sep  5 10:07 .
drwx------ 4 sfmqrb sfmqrb     4096 Sep  5 01:20 ..
-rw-rw-r-- 1 sfmqrb sfmqrb     4061 Sep  5 02:00 avestan.png
-rw-rw-r-- 1 sfmqrb sfmqrb     5971 Sep  5 02:13 baga.html
-rw-rw-r-- 1 sfmqrb sfmqrb   189420 Sep  5 02:15 bqt440_bottom.png
-rw-rw-r-- 1 sfmqrb sfmqrb   513902 Sep  5 02:15 bqt440.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   502834 Sep  5 02:02 bqt538_big.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb    72705 Sep  5 02:02 bqt538_fn6.png
-rw-rw-r-- 1 sfmqrb sfmqrb    24595 Sep  5 02:02 bqt538_head2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    22593 Sep  5 02:02 bqt538_head.png
-rw-rw-r-- 1 sfmqrb sfmqrb   207980 Sep  5 02:01 bqt538.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   282104 Sep  5 01:29 bqt733_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   669351 Sep  5 01:29 bqt733.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb    17369 Sep  5 01:35 bqtv1_361_head.png
-rw-rw-r-- 1 sfmqrb sfmqrb   470042 Sep  5 01:35 bqtv1_361.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   241161 Sep  5 01:36 bqtv1_398_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   482084 Sep  5 01:36 bqtv1_398.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   190109 Sep  5 01:35 bqtv1_399_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    53579 Sep  5 01:36 bqtv1_399_head2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1625 Sep  5 01:35 bqtv1_399_head.png
-rw-rw-r-- 1 sfmqrb sfmqrb   510341 Sep  5 01:35 bqtv1_399.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb    63555 Sep  5 01:43 build71.py
-rw-rw-r-- 1 sfmqrb sfmqrb     5214 Sep  5 02:23 build82a.py
-rw-rw-r-- 1 sfmqrb sfmqrb    53401 Sep  5 02:29 build82b.py
-rw-rw-r-- 1 sfmqrb sfmqrb    19831 Sep  5 02:31 build82c.py
-rw-rw-r-- 1 sfmqrb sfmqrb     4811 Sep  5 02:00 bulca.png
-rw-rw-r-- 1 sfmqrb sfmqrb    22149 Sep  5 01:51 c_belloth.png
-rw-rw-r-- 1 sfmqrb sfmqrb    30227 Sep  5 09:50 crop_ambor.png
-rw-rw-r-- 1 sfmqrb sfmqrb    25024 Sep  5 09:50 crop_berijab_lat.png
-rw-rw-r-- 1 sfmqrb sfmqrb    39114 Sep  5 09:50 crop_berijan_ar.png
-rw-rw-r-- 1 sfmqrb sfmqrb    65413 Sep  5 09:50 crop_persian_roast.png
-rw-rw-r-- 1 sfmqrb sfmqrb    23219 Sep  5 01:51 c_schyth.png
-rw-rw-r-- 1 sfmqrb sfmqrb    58057 Sep  5 02:29 e0full.json
-rw-rw-r-- 1 sfmqrb sfmqrb     4446 Sep  5 02:23 e0.json
-rw-rw-r-- 1 sfmqrb sfmqrb   445959 Sep  5 01:37 hrn126_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb  1213019 Sep  5 01:37 hrn126.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   456157 Sep  5 01:37 hrn127_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb  1278807 Sep  5 01:37 hrn127.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb    40966 Sep  5 01:40 mk67.py
-rw-rw-r-- 1 sfmqrb sfmqrb    58318 Sep  5 01:45 mk70.py
-rw-rw-r-- 1 sfmqrb sfmqrb    78619 Sep  5 02:02 mk73.py
-rw-rw-r-- 1 sfmqrb sfmqrb    68454 Sep  5 02:01 mk75.py
-rw-rw-r-- 1 sfmqrb sfmqrb    79383 Sep  5 02:19 mk78.py
-rw-rw-r-- 1 sfmqrb sfmqrb    52793 Sep  5 02:18 mk79.py
-rw-rw-r-- 1 sfmqrb sfmqrb    57729 Sep  5 02:31 mk81.py
-rw-rw-r-- 1 sfmqrb sfmqrb    58379 Sep  5 02:39 mk83.py
-rw-rw-r-- 1 sfmqrb sfmqrb    76819 Sep  5 02:39 mk84.py
-rw-rw-r-- 1 sfmqrb sfmqrb    25181 Sep  5 02:44 mk86.py
-rw-rw-r-- 1 sfmqrb sfmqrb    67712 Sep  5 10:03 mk87.py
-rw-rw-r-- 1 sfmqrb sfmqrb    70790 Sep  5 10:04 mk90.py
-rw-rw-r-- 1 sfmqrb sfmqrb    48553 Sep  5 10:03 mk91.py
-rw-rw-r-- 1 sfmqrb sfmqrb 18949704 Sep  5 02:30 mw1872.htm
-rw-rw-r-- 1 sfmqrb sfmqrb     3057 Sep  5 10:05 patch87.py
-rw-rw-r-- 1 sfmqrb sfmqrb    55169 Sep  5 01:30 pg67.png
-rw-rw-r-- 1 sfmqrb sfmqrb    57649 Sep  5 01:33 pg69.png
-rw-rw-r-- 1 sfmqrb sfmqrb    50966 Sep  5 01:33 pg69_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    77968 Sep  5 01:31 pg70.png
-rw-rw-r-- 1 sfmqrb sfmqrb    75801 Sep  5 01:29 pg71_300.png
-rw-rw-r-- 1 sfmqrb sfmqrb    71145 Sep  5 01:29 pg71.png
-rw-rw-r-- 1 sfmqrb sfmqrb   134140 Sep  5 01:44 pg72_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2377 Sep  5 01:44 pg72_afandi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    11769 Sep  5 01:47 pg72_fr2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2947 Sep  5 01:44 pg72_fr.png
-rw-rw-r-- 1 sfmqrb sfmqrb    49860 Sep  5 01:44 pg72.png
-rw-rw-r-- 1 sfmqrb sfmqrb    81180 Sep  5 01:47 pg73.png
-rw-rw-r-- 1 sfmqrb sfmqrb    56073 Sep  5 01:48 pg74.png
-rw-rw-r-- 1 sfmqrb sfmqrb   108877 Sep  5 01:51 pg75_400.png
-rw-rw-r-- 1 sfmqrb sfmqrb    20612 Sep  5 01:51 pg75_greeklatin.png
-rw-rw-r-- 1 sfmqrb sfmqrb    75134 Sep  5 01:51 pg75.png
-rw-rw-r-- 1 sfmqrb sfmqrb    66505 Sep  5 01:51 pg76.png
-rw-rw-r-- 1 sfmqrb sfmqrb    65211 Sep  5 02:00 pg77.png
-rw-rw-r-- 1 sfmqrb sfmqrb   155334 Sep  5 02:00 pg78_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb    63822 Sep  5 01:59 pg78.png
-rw-rw-r-- 1 sfmqrb sfmqrb    59439 Sep  5 02:09 pg79.png
-rw-rw-r-- 1 sfmqrb sfmqrb    58953 Sep  5 02:08 pg80.png
-rw-rw-r-- 1 sfmqrb sfmqrb    99904 Sep  5 02:15 pg81.png
-rw-rw-r-- 1 sfmqrb sfmqrb    29321 Sep  5 02:20 pg82_bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    74477 Sep  5 02:20 pg82.png
-rw-rw-r-- 1 sfmqrb sfmqrb    56108 Sep  5 02:20 pg82_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb   154129 Sep  5 02:25 pg83_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb     7123 Sep  5 02:26 pg83_apac.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4363 Sep  5 02:26 pg83_bohyah.png
-rw-rw-r-- 1 sfmqrb sfmqrb    67094 Sep  5 02:25 pg83.png
-rw-rw-r-- 1 sfmqrb sfmqrb    82358 Sep  5 02:23 pg84.png
-rw-rw-r-- 1 sfmqrb sfmqrb    63329 Sep  5 02:25 pg85.png
-rw-rw-r-- 1 sfmqrb sfmqrb    31530 Sep  5 02:35 pg86.png
-rw-rw-r-- 1 sfmqrb sfmqrb    79874 Sep  5 09:47 pg87.png
-rw-rw-r-- 1 sfmqrb sfmqrb   134852 Sep  5 09:54 pg88_400.png
-rw-rw-r-- 1 sfmqrb sfmqrb    11747 Sep  5 09:54 pg88_e0spine.png
-rw-rw-r-- 1 sfmqrb sfmqrb    31391 Sep  5 09:55 pg88_join.png
-rw-rw-r-- 1 sfmqrb sfmqrb    98452 Sep  5 09:54 pg88.png
-rw-rw-r-- 1 sfmqrb sfmqrb    26700 Sep  5 09:54 pg88_spine.png
-rw-rw-r-- 1 sfmqrb sfmqrb   171528 Sep  5 02:45 pg89_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4628 Sep  5 02:45 pg89_ambor.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4924 Sep  5 02:45 pg89_berijan.png
-rw-rw-r-- 1 sfmqrb sfmqrb    80984 Sep  5 09:49 pg89.png
-rw-rw-r-- 1 sfmqrb sfmqrb    77182 Sep  5 09:48 pg90.png
-rw-rw-r-- 1 sfmqrb sfmqrb    63799 Sep  5 09:55 pg91.png
-rw-rw-r-- 1 sfmqrb sfmqrb    90918 Sep  5 10:07 pg92.png
```


## [2026-09-05T14:07:40.863Z] TOOL CALL #26: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg92.png"
}
```


### [2026-09-05T14:07:41.341Z] TOOL RESULT

```

```


## [2026-09-05T14:07:41.339Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-05T14:08:16.611Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PHD ārzōg/burz/buland/bālā ===\"; grep -n -iE \"arzog|ʾlzwg|burz|buland|balay|bal-|barz\" PHD.txt | head -25"
}
```


### [2026-09-05T14:08:16.664Z] TOOL RESULT

```
=== PHD ārzōg/burz/buland/bālā ===
122:/abāz dādan б: 1. attribute, ascribe to; 2. appoint to. br ... add M fr! va-čār add helpless. delete á-distag ... (read ayidtag) add ‚тах |°р1°с | N farāz] acclivity. Afson ... add M ?pswn. Vagar ..., add useless. vāgēš [kw | (M "^ wa, P ?gwc), N aqóš] embrace, armful. add vājištag | gyštk' | P * gyšt, N ayišta] mixed, defiled. add \Ahliswang |*hlygwng] = Ard. delete Khriswang ... for alum ... read „alum |? № | N <] millet. Vāsnūd(ag) ... delete noble. aswür [|PR/LSYA < A pršy';.. āšnāg ... add acquainted with. āštīh ... add concord. ayad ... read |" byd^t' |... for bahr... and bahrag ... read bahr(ag) |b hl(k') | M bhr, N ~(a)] part, portion, share, lot; reason. (az) an bahrag ray : on that account, therefore. for  bahrwar ... read bahr(ag)war [b'hl(k)wl | N bahrawar| partaking, parti- cipator, partner. ~th : participation, advantage. balay add M by. add balgam |[blgm | N balyam] phlegm. baxtan ... add divide. bayaspān [by?sp^n' | = M]... bélür ... for M read P bylwr.
123:?bóy ... add incense. buland ... add aloud. čandīdan ... | (M cn-ystn), J ~]...
164:abarmān [5/mn'] in charge. abarmānd ['pín?nd] inheritance, privilege. abarmānīģ [%n?nyk!] noble. abar-menišn Pf/myn$n'!] proud, haughty. abarón Pf*/xwn! | N wárün] contrary, wrong, sinful. ~ih: sin. abar-6z PóPeoc] stronger. ~ih: mastery. abar-tan [Pltn'] arrogant. ~th: arrogance. abarwēz Pfltvyc | (M *bruyj, N parwéz)] triumphant, victorious. ~ih: triumph, victory. abarzén, v. zmašk, abaxs [hš] repentant; regret. ~ЛЬ : repentance. abaxšāwand [5hP^wnd] regretful. abaxšāyīdan, abaxšāy- [5APd-ytn! | М ?bxPy-, N baxšūdan, baxšāy-) forgive, have mercy on. ~išn: mercy, forgiveness. ~i&nig : forgiving, merciful. labāxtar [*5?*4tl | M 7b’xtr] planet. žabāxtar [PP’htl | (N bāxtar ‘west’)] north. abaydag Pyrťk', v. paydag | M ?byd?g] invisible. ~th: invisibility. abày- : abayéd ['yt' | M Maud, N bāyad] it is necessary, fitting; must (+ infinitive). ~ist Pf?dst' | N bāyist] it was necessary. ~istan [?P?dstn!] be necessary, fitting; desire, want. ~išn: necessity. ~išnīg : necessary, fitting, seemly. abāz [L AWHL < A lI2(w)hr;?Pc | М Рс, N baz, wa] back, again, re-. ~ айдап б: attribute, ascribe to. 7 appoint t= ~ dāštan: withhold, restrain, prevent. ~ ēstādan az: abandon, desist from. — kardan: open. — kardan az: disengage from, wean. ~ mándan: remain behind. ~ pádan: remain, stay. — raftan : issue, go forth. ~ waštan O: turn into, become. ~ wirāstan: rearrange. abāzsār [LAWHLs'I] rebellious. ~ih: rebellion. āb-čihrag [$ cyhlk'] holding the seed, essence of water. abd [>24 | М "Gd J ?bd-] wonderful. ~ sahistan: seem wonderful (to) > marvel.
243:balay [PPd | N bālā] height, stature.
292:*brinj [binc | (M bryng), N birinj] bronze, brass. ~én [-yx!] bronze, brazen. brinómand [blyn’wmnd] delimited. brištan, bréz- [blystn', blyc- | M bryz-, N biristan] roast. brüg [blwk' | M brwg, N abrü] (eye)brow. büdan, b(aw)- [YHWWN-tn! < A yhwwn, У hwh; bwtn', b- | M bwdn, bw-, N büdan] be, become. bawišn: becoming, genesis. büf [bwp | N <), *büg [bwk'] owl. buland [bwind | = M, N ~] high. būm [bwm | N ~] land, earth, country. ~-€andag [-cndk'] earthquake. Ibun [bwn' | = M, N ~] base, foundation, bottom. *bun [bwn! | N ~] = wan. bunag [bznk! | N ~a] baggage; abode, camp. — daštan: dwell, settle. bun-dahišn(īh) [bzundhšn!, -yh] primal creation. bunih [bwnyh] beginning. buništ [bwnyst! | = M] foundation. ~ag [-k'] principle. bun-kadaģ [bwnktk'] original house, home. bun-xān [bwnh?n'] source. bur-, —išn, v. buridan. burāģ [bzoP RU] cutting, sharp. burām-, v. bram-. burd [bwit! | M bwrd] patient. ~ih: patience. burdan, bar- [Y BLWN-tn! < А У ybl; bwltn', bl- | M Бата, br-, N <] carry, bear, take, endure. ~išn: bearing, behaviour. burdār [bwit!]] bearer; womb. ~ih: patience. burd-ešnēhr [bwit! fnwhl | P bwrdyfnwhr] grateful, thankful. burg [bwig | (Ar. burj)] tower. buridan, bur- [bwl-ytn! | M bwr-, N ~] = bridan. —j$n: cutting. Burz [bwic] the god of agriculture. Burzénmihr [bwlcynmtr!] the third major Fire of Sasanian Eran, that of husbandmen. burzidan, burz- [bwlc-ytn'] praise, honour. ~i$n: praise, honour. —iŠnié : praiseworthy. buš [ро | N ~] mane. būšāsp [bwPsp | M bwsy'sp, N ~] sleep, sloth; dream. * but [bwt! | = M, N ~] Buddha; idol. buz [AZ < A ‘z; Бос | N ~] goat.
396:hannàm [%7m | = M] = handām. Harborz [Albwic | N Alburz] the mountain range surrounding the world. harg [hlg | cf. M bie, Аг. xarj, xaraj] duty, tribute; work, effort. *harrób- [hlwp- | M hrwb-] collect, gather. —išn(ih): collection, gathering. har(w) [KRA < A АР; hl | M been, N har] all, each, every. harwin [%/wyx! | M hrwyn] pl. al. harwisp [Ahlwsp! | M hrwsp] all. ~in [-yn'] pl. all. harzag [hick! | N harza] loose, free. has®r [Ps] = Av. háóra-] a measure of time (unequal hour, ze of day- light); a measure of length (— frasang, or 1 frasang, 1 mile). haspin [hspyn! | = M] rest, repose. hast, ~ih [AY T!, -yh] = tast, ~ih. hašāģird [kP klt! | M APgyrd, N šāgtrd] disciple, pupil. hast [h#! | = M, N ~] eight. ~ad [80 | N ~] eighty. ~dah [лаһ | N ~, higdah] eighteen. lhàwan [h?wn! | N +] a mortar. *hawan [/?zn! = Av. háwani-] the morning gdh. hāwand [/?wnd | M ÞPw(y)nd] like, similar. ^h: likeness, similarity. hāwišt [h’wst'] disciple, pupil. ~ih: disciplehood. haxt [h()At'] thigh, haunch, hip. hāxtan, hàz- [/7htn', h'e-] lead, guide, persuade, convert. ~išn: persuasion, conversion. hazār [1,000, hel | M h?r, N ~] thousand. ~ag LEI | N ~a] millennium. hazzān [?/h2’n'] tomb, ossuary. hên [Ayn! | M hyyn] army. ~ih: attack, aggression. hérbed [%y/pt! | N hérbud] teacher-priest. ~ih: priestly office. hērbedestān [hylptst’n'] priestly school. ~ih: priestly studies. hérig [hylyk' | N h/xéri] iris, wallflower. hézag [Ayck! | (M hyjg), N лег] pail. hil-, —išn, v. histan. hindüg [Andwk! | M hyndwg, N hindi] Indian. ~ап [-°п!] India. hištan, hil-, (P hirz-) [S BKWN-tn! < A У #9; (hlc-) | M hyštn, hyl-, (P Ayrz-), N —] let, leave, abandon, pardon, set, appoint. ~išn: pardon, loosing. hixr [hyhl] excrement. hixtan, hanj- [Ayhtn', hne- | P hxt] draw (water).
462:2mašk [mšk! | N maškē] tent, pavilion. ~abarzén [-!pizyn! | M mškbrzyn] royal pavilion.
590:tà [OD < A “d | (M d’), N ~] until; so that. tab [tp | N ~] fever. tab-, —išn, v. taftan. tüb- , ~išn, v. tāftan. хабар [r5k! | N taba] frying-pan. tabāh [tp?% | N ~] ruined, spoilt, destroyed. 7h : ruin, destruction. tabāhīhistan, tabāhīh- [tp’hyh-sin' | J th’hh-] be ruined. tabangóg [ipngwk! | N tabangó] box, chest. tabarzad [tpizt' | N ~] manna. tābestān [P stn! | N ~] summer. tábidan [P 5ytn! | N ~] = tāftan. tadan, tan- [itn!, tn- | N tan-] spin (thread). tadar(w) [ttl | (N tačarw)] pheasant. taftan, tab- [tp-tn'] grow hot; shine. —išn: heat, fever. táftan, tāb- [2°p-tn' | P РЬ-, N ~] heat, burn; shine. ~išn: burning. taftīg [tptyk' | (P tft)] burning, ardent, fervent. tag [tk' | N ~] running, attack. — kardan abar, ó: attack. мар (Pk! | N ta] item, unit; alone, single. ңар [Ok | N tā] branch. tagarg [tklg | M erg, N ~] hail. tagig [tkyk!] swift, strong. ~ih: speed, strength. tah [th | N ~] bottom. tak6k [tkwk! | N ~] drinking vessel. talag [t/k' | N tala] snare, trap. ~-€in [-cyn'] fowler. tambiir [tm-, tnbwl | N ~] cither, lute. ~ag [-k'] tambour (?). tan [tn' | = M, N ~] body, person. tan-, v. tadan. *tanāpuhl [tr?pwhl = Av. tanu.parada- | (N tanáfür)] a degree of sin.
605:wad-baxt [wtP ht! | N badbaxt] unfortunate. wad-dil [wtdyl | M wddyl, N baddil] coward(ly). wadgarih [wtglyh] evil-doing. wād-ģirdaģ [w° tgltk' | (N gird-bād)] whirlwind. wad-góhr [wtgwhl | N bad-gauhar] ill-, low-born. wad-kamag [wtk’mk'] malevolent. ~ih: malevolence. wadrang [w’ ting | N bādrang] citron. cc Dë [-bwd | N -bóya] lemon balm. wad|-tóhm [wttwhm] = wad-góhr. ~-wazag [-w’ck! | (N gawāža)] abuse. --.Xém [-hym] ill-natured. waf- [wp- | Р wf-, (N bàf-)] weave. ~išn: weaving. wafr [wp! | M wpr, N barf] snow. ~énag [-ynk!] а sweetmeat. waydān [wy?n! = Av. waybana-] head (ahuric). wahāg [wP?k! | M тор, N baha] trading; value. — burdan: value, estimate. wahār [wh], (bj?l) | M wkr, № bahar] spring. ~ig [-уЁ! | N -z] spring, vernal. wahig [ZZLA < A Semi (?); whyk' | M whyg, N *bahi] kid; astr. Capricorn. wahist [ол | M whyst, N bihist] paradise. ~Ig [-yk! | N -1] (worthy) of paradise. Wahman [whwmn' | M whmn, N bahman] Good Mind, the first Amahra- spand, guardian of cattle; cal. 11th month; 2nd day. wāhmān [*w-n! = whmn' | MOw^hmn, J whmn, N bahman] so-and-so. Wahrām [wlhl?’n', whPm | M whr’m, N bahram] god of war, victory; astr. Mars; cal. zoth day. ātaxš 1~: a major sacred fire. wak [wk! | N bak] frog. wālan [zo n! | (IN barzan)] settlement, community walg [wlg] = warg. walidan, wāl- [w]-ytn! | N bdlidan] grow, increase, prosper. ~išn: growth. wümidan, wam- [w’m-yin'] vomit. wan [wn' | N bun] tree; stock, stem. ~ i $urgünig : pistachio tree. ~ 1 was-téhmag: the Tree of Many Seeds. wān-, ~išn, v. wanidan. wanafšag [zvnpšk! | N bunafša) violet. Wanand [wnnd] astr. Vega. wandaģ [wndk'] rope, cord. wang [KALA < А ql’; wng | = M, N bang] voice, cry. wānīdan, wan- [wn-ytn! | M w’n-yst] conquer, overcome, destroy.
607:~išn: conquest, destruction. wanigarih [4W BDN-, wny-klyh] waste. wany [A(W)BDN' < APbdn | M wny] lost, destroyed. wany(b)ūdīh [4WBDN'butyh, -YHWWNtyh | M wny(b)wdyh] destruction, ruination. iwar [wl | M wr, N bar] breast. *war [w/] lake. Zwar [wl] oath, ordeal. ‘war [wl] shelter, enclosure. war-, v. waridan. warāy [wl”g | J bry] crow. waran [win'] desire, lust. warān [wi’n'] ram. wārān [w’Pn' | M wrn, N bārān] rain. waranig [wlnyk'] greedy. ~ih: greed, lust. waranig [wL nyk! | N bārānī) rain(y). warāz [wl”c | N gurāz] boar. war-čašm [wicfm] with eye(s) in the breast. ward-, v. 'waštan. lwardag [witk! | M wrdg, N barda] captive, prisoner. ~ih: captivity. *warda$ [witk'] on heat (female animal). ~ih: heat. *wardānāģ (wi? mk! | N gardana] (roasting) spit. wardénidan, wardén- [wityn-ytn! | (N gardànidan)] cause to turn; change, alter. wardišn [witšn! | M wrdyšn, N дака] turning, change, metamorphosis. ~ig [-y%!] transient, changeable. ~(ig)ih : transience, mutability. wardyün [wltywn! | P wrdywn, N gardiin] vehicle, carriage, chariot. warg [wlg | N barg] leaf. wārīdan, wār- [w?l-ytn' | M w’r-yst, N bàáridan] rain. warišn [wilsn'] conduct, behaviour. lwarm [wlm | N barm] memory. — kardan: learn by heart, memorize. *warm [wim | N barm] pool, reservoir. wārom [w’lwm] mind. warómand [wl’wmnd] doubtful. ih: doubt. warr [LBWS Y A < A lbw?] wool; garment. warrag [КММА < ?; wlk! | M wrg, N barra] lamb, ram; astr. Aries. wars [wils] hair. lwarz [wle | M wrz, N barz] work, agriculture. *warz [wic | М wrc/z] miracle, miraculous power. *warz [wlz | N gurz] club, mace.
614:warzigar [wlcykl | M zorzygr, N barzigar] worker, peasant.
1948:fire adur, ātaxš; form of ~ āsrēkerpa; sacred ~ ádarog, Burzénmihr, Farrobág, Gušnasp, ātaxš i Wah- ram.
2251:height balay.
2280:high borz, buland; on ~ bālistīg.
2304:honour (n.) āzarm, āzarmīgīh, burzišn.
2305:honour ( v.) burzidan.
2688:lust arzog, àz, waran, waranigih.
2724:manna tabarzad.
3059:pavilion kēšk, mašk; royal ~ mašk- abarzēn.
3199:praise (n.) afrin, burzišn, niyāyišn, stāyišn, šnāyišn.
3200:praise (v.) āfrīdan, burzidan, stūdan, (stāyīdan), šnāyīdan,
3201:praiseworthy burzišnīg, stāyišnīg.
3805:stature balay, bain; of the same ~ hambašn, hamtan.
4401:Burz
4456:tabangog tabarzad tabišn taftīg taftan taz- tazàg tazén-
```


## [2026-09-05T14:08:17.341Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== CHEUNG barz ===\"; grep -n -E \"\\*barz|barz-|\\*b[aə]rz\" CHEUNG.txt | head -30"
}
```


### [2026-09-05T14:08:17.392Z] TOOL RESULT

```
=== CHEUNG barz ===
1969:with the root *barz ‘to enlarge, make high’, which does not appear to have acquired 
2044:*barz! ‘to make high’ 
2052:*barz2 13 
2079:discrepancies. See *barz?. 
2083:with the generally attested ‘high, tall’. See further *barz”. > EWAia II: 212, 232 
2096:*barz? ‘to cover, cushion’ 
2105:*CHORESMIAN: BZnyk ‘cushion’ (< *barzanaka-) 
2448:semantically not quite satisfactory. Samadi, l.c. therefore cautiously suggests *barz 
56163:*barz’, *gaud, *Huar', 
56190:*barz? 
57179:*barz!
```


## [2026-09-05T14:08:24.949Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '2040,2110p' CHEUNG.txt"
}
```


### [2026-09-05T14:08:25.000Z] TOOL RESULT

```
*PIE — > LIV: - | Pok.: 133 f. 
*REFERENCES: Klingenschmitt 1982: 231, n. 4; Werba 1997: 466; ESIJa II: 116; Shahbakhsh: s.v. érbar- 


*barz! ‘to make high’ 

*AVESTAN: YAv. baraz- ‘to enlarge’, (Gpl.) barazimanam ‘heights’, YAv. barazant- 
‘rising high, high, loud’ = Liste: 38 

Caus.: pres. SUBJ. YAV. us ... barazaiieni (Yt 10.108) 


*barz2 13 


*OLD PERSIAN: barsnä (instr. sg. m.) <b-r-S-n-a> ‘height, depth’ (DSf 26 f.) = Kent: 
200b 

*MIDDLE PERSIAN: MMP bsn, BMP bsn /basn/ ‘top, peak, height’, MMP b’l’y, BMP 
b’I’d /balay/ ‘height’, MMP bwlnd, BMP bwind /buland/ ‘high’ = DMMPP: 111b, 
103b, 117a 

*PARTHIAN: bwrz ‘high, lofty’, bwrzynd ‘high, height’, bwrzyyft ‘height’ 
=> DMMPP: 118a 

*KHOTANESE: OKh. balysga- ‘high’, OKh. bulysa- ‘long’ 

*SOGDIAN: BSogd. Brz’y, MSogd. Brzyy ‘long’, BSogd. Brzkw, MSogd. Brzqwyy 
‘length’, CSogd. brzy ‘loud’ 

*CHORESMIAN: BZk ‘long’ 

*NWIR: NP bala ‘height’, NP buland ‘high, tall’, Bal. burz, Tal. barz, Kurd. barz, 
Zaz. berz ‘high’, Kurd. (Kurm.) bilind, (Sor.) bitind ‘high, enormous’ 

*NEIR: Oss. beerzond ‘high, height’, Sh. vüyj (m.), (Baj.) vöyj (f.), Rosh. vüz, Bart. 
vüz, Yzgh. voz, Yi. vän, Yghn. vann, Pash. пуа (Waz.) wiZd ‘long’, Sangl., Ishk. 
voZdük ‘long; high (?)’. © Oss. I. æmbærzyn/æmbærzt, D. embzrzun/embarzt ‘to 
cover’, cited in LIV: Le fn. ба, is unconnected, on account of the semantic 
discrepancies. See *barz?. 

*SANSKRIT: brhánt- ‘high’ (RV+). 0 The connection of brhánt- with the root barh ‘to 
make strong, make great’ (RV+) is semantically difficult: it does not fit very well 
with the generally attested ‘high, tall’. See further *barz”. > EWAia II: 212, 232 
«PIE *b"erg"- ‘to become high’ = LIV: 78 f. | Pok.: 140 f. 

*IE COGNATES: Hitt. pär-ak-ta-ru ‘should raise himself’, Toch. pärk- ‘to rise (of the 


sun)’, NHG Berg (m.) ‘mountain’ 

*REFERENCES: IIFL II: 418a; GMS: par. 138, 999; Abaev, Slovar’ I: 254; EVS: 84a; DKS: 272b; Benzing 
1983: 209 f.; Werba 1997: 209; Paul 1998: 292a; Cabolov 2001: 127, 177; NEVP: 8; Korn 2005: 97, 143, 
355 (passim) 


*barz? ‘to cover, cushion’ 

*MIDDLE PERSIAN: BMP b’Iyn /balen/ ‘cushion, pillow’ (MacKenzie, Pahlavi: 16). > 
Nyberg II: 43 rather assigns the more poetic meaning ‘the crown of the head’, 
comparing the Persian form to Av. barazan- ‘top’. 

*KHOTANESE: ? vuda- ‘covered’. O The Khot. past participle can also derive from 
*Huar ‘to cover’, which is not mentioned in DKS: l.c. 

*CHORESMIAN: BZnyk ‘cushion’ (< *barzanaka-) 

*NWIR: ? Tt. (Cha.) u-mi-verzene ‘he seats’ (< **he puts someone on a cushion’ ?) || 
(+ *ham-) Tt. (Cha.) amberaz ‘clothing’ 

*NEIR: Sh. viyj(6j) ‘pillow, head of a bed’, Wa. vorz(ik), Sangl. vözd, Yi. virzáné,
```


## [2026-09-05T14:08:31.679Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -iE \"arzog|arzu|ʾʾβrxs|βrxs|brxs\" CHEUNG.txt | head -20; echo \"=== SOD ===\"; grep -n -iE \"brxs|arzog|arzu|آرزو\" SOD.txt | head -20"
}
```


### [2026-09-05T14:08:31.745Z] TOOL RESULT

```
1928:translated as ‘desire’ (/arzog/) in the Pahlavi commentary. = Liste: 38 
1972:to possess, to desire’, for which BSogd. ’’B’rxs’k, BSogd. ’’Brxs’kw ‘wish, desire, 
1973:lust’, Khot. aurista, orista, Pth. "wrjwg, MP /arzog/ (MMP ’(’)wrzwg, ВМР "Icwk) 
2118:against unpleasantness’ ?) || (+ *ham-) І. emberzyn/emberzt, D embarzun/ 
2628:‘to light, set on fire’, BSogd. "D'rxs'k, BSogd. ’’Brxs’kw ‘wish, desire, lust’, 
2629:MSogd. ”’Brxsyy ‘desire, lust’, SSogd. ’’Brxs’kmync ‘lascivious’ (cf. Sims-Williams 
12433:*NEIR: Oss. І. marzyn/marzt, D. marzun/marzt ‘to wipe, brush’, ? Pash. muz-/musal 
20935:|| + *a-) MMP "wrzwg, "wrzwg, ’wrzwwg, ВМР ’Icwk /arzog/ ‘desire, lust’. 0 The 
21133:*SOGDIAN: (+ *abi-) CSogd. brxs- ‘to loosen, release, shoot’, BSogd. Br'xs ‘to shoot’ 
21134:Pres.: IND. 3sg. BSogd. Br’xst; Impf.: IND. 3sg. CSogd. b’rxs; Inf.: Brxs’y 
27399:*NEIR: Oss. I. warzyn/warzt, D. warzun/warzt ‘to love’ (< *‘to take care of, foster’) 
34869:“сук /arzog/, 11, 318 
38072:UBrxs'k (B), 11, 22 
38074:"Brxs’kmync (S), 22 
38075:*’Brxs’kw (B), 11, 22 
38076:”Brxsyy (M), 22 
38435:brxs- (С), 322 
40765:arzu, 11 
46772:marzun/marzt (D), 181 
47147:warzun/warzt (D), 423 
=== SOD ===
5164:i  Barzu,  6  km.  southeast  of  Samarkand,  brought  to 
7758:Parth.  awarzog;  Pahl.  awarzog  %  Khot.  aursa 
25385:&Gersh.);  Oss.  raxsin   =»Pr}xs-,  b'rxs-,  brxs-, 
25591:Praxs   =*brxs-,  Pr'ys-,  prys- 
25820:Praxsakya   ^brxsqy'C-) 
26077:2795  brxs-   C  JiJ'^j  < dzj'^j,  *tf*-Mjj 
26084:2796  brxs'mnty   C  v^  \*jIjuL* 
26091:2797  brxsqy'(-)   C  0->^V^>T '(JJ'^L*7 
51645:6533  p>8  brxsqy*  C  ^ j'-^L*7 
77051:warzun-karc  =»wrcwnkrc
```


## [2026-09-05T14:08:35.262Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '1955,1995p' CHEUNG.txt; echo \"=== 20925-20945 ===\"; sed -n '20925,20945p' CHEUNG.txt"
}
```


### [2026-09-05T14:08:35.330Z] TOOL RESULT

```
hapax verbal form ’’Brync- is connected to Pth. 'brng, *brnng ‘zeal’, which is 
compared to Av. borog- The n-infix "changes defilement into refinement", which 
ultimately yields the meaning ‘cultivation’. Pth. 'brng, 'brnng is rather from *Hranj. 
|| In ESIJa П: 113, BSogd. "nBrytyk, CSogd. ’bryty ‘paralysed, cripple’ are classified 
under this root, which is wrong. These Sogd. forms actually derive from the 
(near-)homonymous root *braj ‘to break’. 

Pres.: IND. 35р. SSogd. Brysty, 3р1. SSogd. Brys’nt, IMPV. 1р1. BSogd. Brys’ym || (+ *a-) Pres.: IND. 
3pl. SSogd. ""Bryncynt {hapax} 

*CHORESMIAN: 9 Chor. m/BZ- ‘to rejoice, become happy’, derived by Henning 1970: 
12b from *barj, may rather go back to *bauj’ ‘to rejoice’. 

9 There are no particular reasons to consider possible convergence or contamination 
with the root *barz ‘to enlarge, make high’, which does not appear to have acquired 
a more metaphorical connotation (other than *loud' of sound). According to Henning 
1945: 487, fn. 2, the meaning of barog (i.e. *barj) in composition with *a- is ‘to like 
to possess, to desire’, for which BSogd. ’’B’rxs’k, BSogd. ’’Brxs’kw ‘wish, desire, 
lust’, Khot. aurista, orista, Pth. "wrjwg, MP /arzog/ (MMP ’(’)wrzwg, ВМР "Icwk) 
‘desire, lust, NP агли ‘desire, wish’ are cited. This can be disputed, either for 
semantic or for formal reasons. Semantically, the Sogd. (inchoative) formations are 
perhaps more likely to contain the root *braHz ‘to shine, burn, set on fire’. Equally 
semantically difficult to reconcile with ‘to praise, honour’ are the Pth. and Pers. 
‘desire’ formations (v. *rauj^), on which see the cited lit. in Kellens 1974: 351 ff., 
and on the Khotanese forms above. 

«PIE *b'erg"- ‘to honour, be attentive to (a guest)’ = LIV: 79 f. | Pok.: 145 

ЈЕ COGNATES: OCS ne-brésti ‘to neglect’, Russ. beréé’ (beregü) ‘to take care of, 
look after’, Goth. bairgan ‘to protect, shelter’, OE borgian ‘to give a pledge’, Engl. 
to borrow, etc. 


12 *barul (*brau) 
*REFERENCES: Nyberg II: 51а; DKS: 298b f.; Gharib: 19, 106; ESIJa II: 111 ff. 


*Баги! (*brau) ‘to brew, boil’ 

*NEIR: Sh. warv-/wirvd, Rosh. warv-/wirvd, Sariq. worv-/wirvd, Yzgh. wirv-/wirvd 
‘to boil, be boiling’, M. wurw-/wurw-, Yi. urw-/urw- ‘to be boiling’ 
=== 20925-20945 ===

*REFERENCES: IIFL II: 239a, 538b; Andreev — PeSéereva: 315b; Abaev, Slovar’ II: 444; EVS: 68b, 118a, 


91b; DKS: 175a, 88a; Werba 1997: 373; Cabolov 1997: 72; Steblin-Kamenskij 1999: 296; Shahbakhsh: 
S.v. ruj-, karuj- 


*rauf? (*raučĵ) ? ‘to please, desire’ 
*MIDDLE PERSIAN: MMP rwzd- (denomin. ?) ‘to desire, covet’, MMP rwzd ‘greedy’ 
|| + *a-) MMP "wrzwg, "wrzwg, ’wrzwwg, ВМР ’Icwk /arzog/ ‘desire, lust’. 0 The 


*raup 1 319 


additional -d- of MMP rwzd- may point to denominative origin or reflect a pres. 
stem in *-d-, cf. CSogd. sxwrd- ‘to shout’ (*huar?). || According to Henning 1945: 
487, fn. 2, the Persian and Parthian ‘desire, lust’ forms derive from *barj, which is 
semantically implausible. A more suitable root is *rauf. The Manichaean and 
Pahlavi forms perhaps reflect the different outcomes of syncope of the zero grade
```


## [2026-09-05T14:08:35.878Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '7745,7770p' SOD.txt"
}
```


### [2026-09-05T14:08:35.930Z] TOOL RESULT

```
16  "prYs'kmync  S  ^Ji^s*  < j*&^M^ 
aPraxse-menc  =^>Prxsymync 

lascivious 

S  W,  IIJ  1976,  49,  50,  Frag.  5.8-9 

17  "prYs'y  4  "Pr^s'k 

18  >Jprxsy   M  ^^  <o^  < jjj7 
apraxse  (^prY^y)  ®<*a-braxsaka\  Av.  bdrdg% 

Parth.  awarzog;  Pahl.  awarzog  %  Khot.  aursa 

^»pr>YS)k  t 
desire,  lust 
Hen.  Tales.  487  n  2;  GMS  5 

19  "prxsymync  M  ^jjjT 
apraxsemene  ^PrYS^mync 

desiring,  wishful 


"Pryn-
```


## [2026-09-05T14:09:01.178Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -iE \"^ *[0-9]+ +.?n[sš] |mane\" SOD.txt | head -30"
}
```


### [2026-09-05T14:09:01.233Z] TOOL RESULT

```
6693:AI    Acta  Iranica-,  Encyclopedie  Permanente  des 
7687:bound,  joined,  permanent 
9224:permanence 
9244:permanent 
9254:permanent 
9261:permanence 
9525:aw-manc,  omane   ©<*hdmd~mdnaka  ^'wm'n 
10874:attached,  fixed,  permanent 
16600:impermanence 
25147:2650  pns  B  (jii.-JL^^JL 
25149:mane 
28776:canaxu-c(a)mane   ^cn'wxy,  cnm*ny 
28797:can-mane   <£)<*haca-  manah-   ^cnVnCy), 
34938:4141  yns   M  ( jx,-?,C j<Uj)jU^j 
35007:yandak-mane 
41061:kor-mane 
42149:mane  ->*wm>n>k,  mWy 
42191:mane   (m'ny1)  ©nom.  ace.  gen.  =4m'n,  m'n'k 
42330:manestan   ©ob.  -yy 
43241:mane   =>-m,  -mc 
43566:mand-mane  ©pi.  -/   =>mndm,nky) 
44267:human,  humane 
44278:martoxmaneV-ya 
44280:human,  humane 
44286:human,  humane 
47860:nimane,  nimanak(u)  ^nm'ny,  nm'nyy 
47897:nimane-kare 
47902:nimaneken   (nnVnkyn) 
47907:nimane  =»nm}ny,  nm'n'kCw) 
48154:6017  nns  B   -  (^J^lo,^
```


## [2026-09-05T14:09:01.791Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -iE \"b.r.g-|b.r.ga-\" BRT.txt | head -20"
}
```


### [2026-09-05T14:09:01.846Z] TOOL RESULT

```
16956:•  j.  bar9g-  V.  'willkommen  heissen'. Praes.  34  hrtjaya-.  —  PPfP.  b>nxta- (sbes.);  PFP.  hryya-  (als  Name,  sbes.).
17133:b«r9g-
17138:•  j.  bsrsg-  f.  'religiöser  Brauch,  religiöse Form,  Ritus',  nur  in  Verbindung  mit  GS. a^ahe  oder  damayi :  ahurtm  . .  yasamaide . .  'nja  (IS.)  vanhSus  asahe  'r»jä  dalnayä va^huyä  mäzdayasnsil  Y,  SS-  • .  '3-  ^  (wo 'ja);  —  aismim  . .  asafte  'nja  yaoidätq Y.  62. 10;  *P.  4H;  —  frä  hl  am>iä  sptnta 'r?ja  vsrmta  damayäi  (als  Gen.)  "es bekannten  sich  dazu  die  ASp.  nach  dem Ritus  der  Religion"  Ytio. 92''; — saskuStima asahe  'njs  "die  sich  auf  die  Bräuche  des heiligenRcchts  am  besten  verstehen"  A.^.4.
```


## [2026-09-05T14:09:08.691Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '25135,25165p' SOD.txt"
}
```


### [2026-09-05T14:09:08.735Z] TOOL RESULT

```
2648  pndy(h)   M  *ju 
Pande  ©<bandaka  =*Pnt}k,  Pynd- 

servant,  slave 

GMS  107,  283;  BBB  b87 

2649  bnq>   C 

©1  sg.  fut.   =*P-,  pw- 
C2,  48R3 

2650  pns  B  (jii.-JL^^JL 
fons  ©<*brsa-,  Av.  bardsa-,  Pahl.  bus-,  Arm.  bars 
mane 

GMS  345;  TSP  19.21  n  p232;  Gersh.  AHM  170 


105 


pr»mt(wh) 


2651  pnt1   B,  S  -k*-^ 
(3and   (bnt1)  ©Yaghn.  vant  ©ace.  -w;  pi.  -ff 

bond,  fetter 

TSP  9.115,  129;  SCE  362;  BSTBL,  Dhu.  202;  Frag.
```


## [2026-09-05T14:09:09.701Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"2650\" SOD_pages.txt | head; echo \"---\"; awk '/\\[pdf page/{p=$0} /2650  pns|2650 pns/{print p\": \"$0}' SOD_pages.txt | head"
}
```


### [2026-09-05T14:09:11.378Z] TOOL RESULT

```
11362:                                                              2650 pns B                                 (jii.-JL^^JL
38808:    loathing 8117,8118                     lust 13, 18, 7347                           mane    2650
---
:                                                               2650 pns B                                 (jii.-JL^^JL
```


## [2026-09-05T14:09:19.767Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==207' SOD_pages.txt | head -60"
}
```


### [2026-09-05T14:09:21.327Z] TOOL RESULT

```
 141

        GMS lllln 1; Livsic. HMV 263; KG 401                     3572 Sr'ws'ycyk B              ^^^'^Vi^
 3559 6pyr      M, S                                     ^            5rosycik ?, zosik ?
                                                                      sacrificial
        6ipir (5byr, dpyr) ©pi. -t ^Sp'yrpt
        scribe                                                        TSP 2.540 n pi 76
                                                                                                                     5ryt>
        W-Lii: Gropp. 37; BBB 524; STi 17.4? KG 495;             3573 5r>wsy(h) B                                  juj
          GMS 44                                                      5rose ?, zose ? (jwsy) %<zaoBra =*zwsy
 3560 dpyr      C ==> 5pyr                                            sacrifice
                                                                      TSP 2.556, 562
 3561 dpyry* C                              L^i{Sj~>>            3574 SrSvt B                            ^/^
      Sipirya (Spyry'h) ^Sp'yry'kh
      writing, scribecraft                                            5rut
      BSTii 892.14; C2, 31R14; GMS 1111; BBB 524                      carpenter
                                                                      TSP 2.537, 3.192 n pl98
 3562 Spyry'h       M =4 dpyry1
 3563 Spyry'kh =* Sp^ry'kh       \                               3575 Sr'yNvr B =» 5rzy*wr, 5rjy}wr
 3564 6r- B                                      olSsJ^j i6jl    3576 6rp-
                                                                      6arp? ? M                                o^-o\p
      5ar ©Ioc. -yh
      ravine, valley                                                  (/o)worry
                                                                      Hen. BSOAS 11.66,9,68.6
      TSP 2.280; Hen. Texts. 718
                                                                3577 arynV    B                                    ^
 3565 5rMs-     B
                                           OxUil idxi'\jtt
        5/9ras, sas ©<*0rasa ? ©inf. ->y ^s's-                        za/oyma, 5rayma =»jym\ zymJ, zymh, Srymrf
        0<?)scatter, (to)strew                                        lie
                                                                      TSP 7.42
        BSTBL, Dhy. 68; AVS 76

3566 6r"w B                        ^ (<lu_u <o>i. ^U            3578 SrymOk) -> Srymh1
     5raw, zaw (5r}w, z*w) ©<*drava-\ fdraw-                    3579 8rYm)s,k B                                  jfcJj3
       =>z}w                                                          8raymasc, zaymase (zynVsy) ^zynVs'k
     fame, news, rumour                                               liar
       VJ; SCE 148; MDii pl99; Sr'w, VJ 552, 610, 11\                 SCE 247; GMS 1112 A
         Benv. Et. Oss. 59; Schwartz. HMV 385 n 2               3580 6rym5nk B                     (Jjj -^tj ft) ^&-r>>
                                                                     6raxm- Gang
3567 8rJw     B, S => 6r»w
                                                                      Dram-sang(a unit of weight)
3568 6rJwpt(-) B                      uJ^ij^j                         TSP 19.14 n p232; Hen. Texts. 713 n 5
     Sropd, zuPd (zwpt) ^pry^r'wpt, zwP-
     dance, OcOdance
                                                                3581 Srymh1 S                             (a>L* Jj,)^^
     SCE 123                                                         5raxm(a) (5rym0k)) ©ob. -yh
                                                                     Drahma
3569 8rW»     B                    ^U^c^                              Hen. Mittelir. p53; MDii p200; 6rYm(yh MDiii
     5ruk, zuk (5rw>k) ©<*druwaka =^jwk, Srwch,
       Srwk, zwq
     sound, whole                                               3582 Srymh2 B                                      ^
     GMS 285; TSP 2.1124; BSTBL, Dhy. 337, 6r}wk                     6rayma, zayma =>zymh, Srym*, jym\ zym*
                                                                     lie pll9
       csmyy "sound-eyed"
3570 8r>wn B                                                         VJ 186 etc.; SCE 253, 268, 274, 436, 441; BSTBL,
     Sron, zon =»zwn                 *JJJ 'tSJp <j(-»j                 Dhu. 178, 200; GMS 285; dVmh, Frag. Len.
     bow, arch                                                          112a3
       SCE 225; Bailey. Prolexis. 121; BSOAS 24, 271            3583 8ryt- B                                    ^b<£
3571 8r'wnp>6>y B                                                    8rayd, zayd ©pt. st. ^5'r-, zyt-, jyt-, Sryty
```


## [2026-09-05T14:09:29.691Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==206' SOD_pages.txt | head -12"
}
```


### [2026-09-05T14:09:32.752Z] TOOL RESULT

```
                                                                                                                            140


  dys-
 3533 6ys- B                           tJ^j'^^j^'j^K*-                 lamp, torch
      5axs ©fdag                                                       Sogdica. 40.11; GMS 60 n 1; C2, 60R 30, 94R 24,
         GcObe burned, (fcOget ripped                                    102V 19
         TSP 6.158 n p206; AVS 73                                3546 dmtyr      C =» 8mtyr
 3534 8yst-(h)       B                              l>w^.        3547 8n (MM,G=S
                                                                               rm)                            (oj* j~t j'K
         Saxst ®f. n.;ob. -y =*dxst-())                                6an (dn) ©<*hada-awana          -*6nn, 'Snn, S'wn,
         plain, desert                                                 with
```


## [2026-09-05T14:09:40.598Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && true; S=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad; pdftoppm -f 92 -l 92 -r 500 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf $S/pg92_500 && python3 -c \"\nfrom PIL import Image\nim=Image.open('$S/pg92_500.png'); print(im.size)\nw,h=im.size\n# Pahlavi box approx x 0.41-0.58, y 0.53-0.57 of page (from 1700x2200 view coords /2200)\nim.crop((int(0.40*w),int(0.525*h),int(0.60*w),int(0.575*h))).save('$S/pg92_pahlavi.png')\nim.crop((int(0.19*w),int(0.145*h),int(0.52*w),int(0.215*h))).save('$S/pg92_avestan.png')\n\""
}
```


### [2026-09-05T14:09:44.352Z] TOOL RESULT

```
(4250, 5500)
```


## [2026-09-05T14:09:46.607Z] TOOL CALL #40: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg92_pahlavi.png"
}
```


### [2026-09-05T14:09:46.622Z] TOOL RESULT

```

```


## [2026-09-05T14:09:50.047Z] TOOL CALL #41: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg92_avestan.png"
}
```


### [2026-09-05T14:09:50.059Z] TOOL RESULT

```

```


## [2026-09-05T14:09:55.651Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -iE \"barzakh\" FVQ.txt | head -10"
}
```


### [2026-09-05T14:09:55.697Z] TOOL RESULT

```
5097:T 1 *}j (Barzakh).
```


## [2026-09-05T14:09:56.347Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== FSF برزوی/فریبرز/برمنش ==\"; grep -n -E \"برزوی|فریبرز|برمنش|فریبرز\" FSF_pages.txt | head -10"
}
```


### [2026-09-05T14:09:56.398Z] TOOL RESULT

```
== FSF برزوی/فریبرز/برمنش ==
4626: ‫ز برج کمان بر سر گاه شد‬                                  ‫وزین رو فریبرز بر میسره‬
4842:                                                                                    ‫برمنش‬
4867:      ‫متکبر »با نخوت‪:‬‬    ‫‪-۲‬به معنی‪ :‬مغرور‬    ‫زايد و نیکنام‬        ‫برمنش‬    ‫گوی‬
4893:                                                        ‫هرآنکو برمنشباشدبهکُشی‬
4917:                   ‫خراسان سپاه برنشاند و‪...‬‬     ‫دلیل دیگر درستی «برمنش» [بابای ابجد]‬
4920:                                                  ‫برمنش» (یادداشت‌های گاتها ص ‪)۲۴۱‬‬
8091:       ‫جو آزاد گشتند از بند اوی‬                                ‫فریبرز کاوسشان پیشرو‬
8665: ‫سواری به نزد فریبرز رفت‬
11404:‫ز برزوی یک در سر نامه کرد‬                                         ‫اینک باید آن را تصحیح کرد‪.‬‬
11435:‫(‪)۲-۵۰۲-۲۳۲‬‬                                  ‫برزوی آورند؛ کلیله و دمنه از هند از‬
```


## [2026-09-05T14:10:01.181Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=4830 && NR<=4930' FSF_pages.txt | sed 's/^ *//' | head -70; echo \"=== page tags near ===\"; awk 'NR<=4930 && /\\[pdf page/{p=$0; n=NR} END{}' FSF_pages.txt; grep -n \"\\[pdf page\" FSF_pages.txt | awk -F: '$1<4930' | tail -3; grep -n \"\\[pdf page\" FSF_pages.txt | awk -F: '$1<11440' | tail -3"
}
```


### [2026-09-05T14:10:03.152Z] TOOL RESULT

```
‫به‬‫نمد‬
‫زيز‬
‫اد ن‬
‫مینن‬
‫نب‬
‫‏(‪)۵٩۲-۱۰۱۸-۲‬‬
‫سپاهش فزون شد ز سیصد هزار‬
‫و با دزر جایدیگربهعبارت دیگر‪:‬‬
‫سوار‬     ‫زره‌دار و بر گستوانور‬

‫(‪)۲-۶۴۱-۱۹۲‬‬
‫زد و مردرااز بلندی منش‬
‫برمنش‬
‫سزدگر فرازد سر از سرزنش‬                     ‫از بر [‪ :‬بلند‪ .‬بالاء ولا] ‪+‬منش‬    ‫‪-۱‬مرکب‬

‫(‪)۱-۸۲۲-۶۷۳۱‬‬                                ‫نهاد‪ .‬خحوی]‪ :‬بلند‬       ‫سرشت‪.‬‬     ‫‪ 1‬آندیشه‬

‫منش با‬      ‫و گاه در مقام دشنام یا سرزنش‪.‬‬




‫توصیف می‌گر دد‪:‬‬    ‫عبدالقادر [فصل میم ‪-‬واژ؛ منش] و در‬
‫‪ ...‬منش پست بادش بهبزم و بهرزم‬       ‫فهر ست ولف و در لغت‌نامهة دهخداو در‬

‫(‪)۶-۲۵۱-۲۶۲‬‬                                 ‫معین؛ به خطا‬       ‫فرهنگ فارسی دکتر محمد‬

‫که چون کاهلی پیشه گیرد جوان‬      ‫«اپرمنش» آمده است» برای روشن شدن‬

‫بماند منش پست و تیره روان‬                      ‫موضوع شاهدهای بیشتری می‌آوریم)‪:‬‬
‫(‪)۵-۳۲۱-۸۶۶‬‬                                              ‫شه بر منش راخحوش امد سخن‬



‫جز تو نزاد حواو ادم نکشت‬     ‫(‪)۱-۵۵-۷۶‬‬

‫شیر نهادی بهول و بر منشت‬                              ‫ازین دحت مهراب و از پور سام‬
‫متکبر »با نخوت‪:‬‬    ‫‪-۲‬به معنی‪ :‬مغرور‬    ‫زايد و نیکنام‬        ‫برمنش‬    ‫گوی‬

‫بزرگمهر در سخنان پندآمیز خود گوید که‬          ‫(‪)۱-۸۱۲-۹۳۳۱‬‬

‫اکر فعاکی ر کررد کین ا‬                    ‫و گاه بجای «بر» «برز [با پیش اول]به‬
‫مغرو ر گردد‪:‬‬

‫چو نزدیک دارد مشو بر منش‬                 ‫میانجی نخواهی جز از تیغو گرز‬
‫نوش‬
‫کی مش‬
‫دگرد‬
‫ر دور‬
‫ب‬ ‫وگ‬                      ‫مش برز داری و بالای برز‬
‫(‪۸‬نوشیروان ‪)۳۱۵۱‬‬                            ‫(‪)۴-۴۱-۵4‬‬
 ‫برنشست‬



‫اچ‪-‬یز‬
‫ریز‬
‫پبرنچ‬             ‫بدو گفت خسرو کهای بدکنش‬
‫بیهو ده مفت‪ .‬رایگان‪:‬‬
‫چرا گشته‌ای تند و برتر منش‬
‫(دقیقی ‪:)۶-۲۰۱-۰۴۵‬‬        ‫(پرویز ‪)۶۳۲‬‬
‫دریغ آن سوار گراننمایه نیز‬                                    ‫(ویس ‪:)۸۹-۸۲‬‬
‫که افگنده شد رایگان برنچیز‬
‫هرآنکو برمنشباشدبهکُشی‬
‫برنشاندن (فعل متعدی)‬        ‫باتع ارام ر‬
‫سوار کردن بر اسب یاکشتی و مانند آنها؛‬                                 ‫(ویس ‪:)۸۱۱-۵۷۱‬‬
‫نشاندن‪:‬‬    ‫تخت‬
‫بر ت‬                ‫نکی ر امان دار د بهکی‬
‫رسیدند پیش منوچهر شاه‬           ‫دمرام بیت‌هایی که شاهد آورده شد‬
‫ت‬
=== page tags near ===
```


## [2026-09-05T14:10:12.219Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -m3 \"pdf page\" FSF_pages.txt; echo \"---count\"; grep -c \"pdf page\" FSF_pages.txt"
}
```


### [2026-09-05T14:10:12.272Z] TOOL RESULT

```
---count
0
```


## [2026-09-05T14:10:15.445Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('FSF_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint(len(pages))\nfor i,p in enumerate(pages):\n    if 'برمنش' in p or 'برزوی' in p:\n        print('leaf',i, p[:80].replace('\\n',' '))\nEOF"
}
```


### [2026-09-05T14:10:17.073Z] TOOL RESULT

```
485
leaf 103                                                        ‫میان‪ .‬تباه‪ .‬خراب‬   
leaf 104  ‫برنشست‬                                    ‫اچ‪-‬یز‬                          
leaf 231                                            ‫‪۸۳۳‬‬                              
leaf 297                                                    ‫‪۳۹۴‬‬                      
leaf 343                                                                                ‫
leaf 366  ‫کفکت‬                                      ‫‪۳۳‬‬
```


## [2026-09-05T14:10:25.456Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('FSF_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in (102,103,104):\n    p=pages[i]\n    print('=== leaf',i,'===')\n    print(p[:1500])\nEOF"
}
```


### [2026-09-05T14:10:27.110Z] TOOL RESULT

```
=== leaf 102 ===
‫برگی‬

                                    ‫برفزود‬   ‫از‬       ‫صهود‬
                                                         ‫قک‬‫منیم‬
                                                              ‫کنید‪ .‬ع‪ .‬ن‪ ).‬اینک ببی‬
 ‫(نقیض برکاست) بسیان فراوان» بیشمار‪:‬‬          ‫برسم چیست‪ .‬مقصود از برسم گرفتن و‬
              ‫چو آمد برشیده دادش درود‬         ‫مدتی دعا بر ان خواندن همان از برای‬
‫ز شاه و ز ایرانیان برفزود‬                     ‫تغذية انسان و‬          ‫يهه‬
                                                                       ‫ا ک‬
                                                                         ‫متات‬
                                                                            ‫نعمت نبا‬
‫(‪)۵-۴۶۲-۲۸۴‬‬                                   ‫ستوران و زینت طبیعت است» سپاس بجای‬
                                   ‫برکاست‬
                                              ‫آوردن است‪ .‬برسم راکهگفتیماز شاخه‌های‌تر‬
                      ‫رو بکهمی کواستی‪:‬‬       ‫قرار داده به‬       ‫‌ها‬
                                                                  ‫یلیة‬
                                                                     ‫نک‬‫تونه‬
                                                                          ‫درختی ارستسنم‬
        ‫ناماوران‬    ‫ان‬
                     ‫دز‬‫رتم‬
                         ‫هسهشس‬
                             ‫گ‬ ‫ب‬
                                                                       ‫آن درود می‌فرستند‪...‬‬
‫زنگه شا
=== leaf 103 ===
                                                       ‫میان‪ .‬تباه‪ .‬خراب‬
                                                                      ‫ای ب‬
                                                                         ‫سعن‬
                                                                           ‫وهم‬
                                                                             ‫رک ب‬
                                                                                ‫بسیبر‬

  ‫«منش» رابا صفت‬          ‫و در بسیار جای‬          ‫ویسبایمان‪ ,‬تباه؛ خراب‬
                                                                      ‫بیرگک بسهمرعن‬
 ‫تفضیلی «برتر» ترکیب می‌کند‪ :‬برتر منش‪:‬‬                         ‫چو شکدار بی‌برگ بیگخرتم‬
                 ‫همیشه بزی شاد و برتر منش‬     ‫به‌دام بلادرنياويختم‬
      ‫ندش‬
        ‫کدا ب‬
            ‫در با‬
                ‫بو دو‬
                    ‫زت‬                       ‫‏(‪ ٩‬پرویز ‏‪(۶Y1‬‬

 ‫(‪)۴-۱۷-۵۸4‬‬
                                                                                  ‫برکستوان‬
                                              ‫پوشند و براسب‬         ‫که روز جنگ‬    ‫پوشش‬
                    ‫ان‬
                     ‫رمنش‬
                        ‫تبرتر‬
                            ‫هرنه‬
                               ‫مکهت‬
                                  ‫نه‬                             ‫اندازند (رشیدی ‪-‬برهان)‪:‬‬
    ‫ران‬
      ‫به‬‫نمد‬
          ‫زيز‬
            ‫اد ن‬
               ‫مینن
=== leaf 104 ===
 ‫برنشست‬



                                ‫اچ‪-‬یز‬
                                    ‫ریز‬
                                      ‫پبرنچ‬             ‫بدو گفت خسرو کهای بدکنش‬
                       ‫بیهو ده مفت‪ .‬رایگان‪:‬‬
                                                 ‫چرا گشته‌ای تند و برتر منش‬
                      ‫(دقیقی ‪:)۶-۲۰۱-۰۴۵‬‬        ‫(پرویز ‪)۶۳۲‬‬
           ‫دریغ آن سوار گراننمایه نیز‬                                    ‫(ویس ‪:)۸۹-۸۲‬‬
 ‫که افگنده شد رایگان برنچیز‬
                                                        ‫هرآنکو برمنشباشدبهکُشی‬
                         ‫برنشاندن (فعل متعدی)‬        ‫باتع ارام ر‬
‫سوار کردن بر اسب یاکشتی و مانند آنها؛‬                                 ‫(ویس ‪:)۸۱۱-۵۷۱‬‬
                           ‫نشاندن‪:‬‬    ‫تخت‬
                                        ‫بر ت‬                ‫نکی ر امان دار د بهکی‬
                 ‫رسیدند پیش منوچهر شاه‬           ‫دمرام بیت‌هایی که شاهد آورده شد‬
                                                                               ‫ت‬
‫بگفتند تابرنشاند سپاه‬                           ‫منش با صفت‌های مطلق‪ :‬بر برز بلند‪.‬‬
 ‫(‪۱-۳۲۱۰-۷۳0‬‬                                    ‫پست‪ .‬و یاصفت تفضیلی برتر همراه‬
                ‫بر زن درم برفشاند‬    ‫پری‌روی‬    ‫است نه با صفت‌های پر و خالی‪ .‬همه جا‬

 ‫به کرسی زر پیکرش برنشاند‬                       ‫سخن از بلندی و پستی در ميان است نه‬
‫‏)‪(VTA-IAT¬—1‬‬                                   ‫ت‪‌.‬آور است که ولف‬        ‫فپر‬‫گو‬ ‫شی‬
```


## [2026-09-05T14:10:40.794Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('FSF_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if 'برزوی' in p:\n        print('=== leaf',i,'===');print(p[:2000]);print()\nEOF"
}
```


### [2026-09-05T14:10:43.136Z] TOOL RESULT

```
=== leaf 231 ===
                                           ‫‪۸۳۳‬‬                                                 ‫دد‬


      ‫بدانتاپس از مرگ من در جهان‬                 ‫نگارنده همابتدابهاین اشتباه دچار شدم و‬
‫ز داننده رنجم نگردد نهان‪...‬‬                      ‫در جلد سوم شاهنامةٌ چاپ مسکو صفحة‬
        ‫به بوزرجمهر آن زمان شاه گفت‬               ‫له‌روی اهزمه‬
                                                             ‫بابه‬
                                                                ‫‪۰‬د‪۷۳‬ن‪۲۷‬‬              ‫بیت‬
                                                                                       ‫‪۹‬‬
‫که ایسن آرزو را نشاید نهفت‬                   ‫نسخه‌ها شکل ادرست «رخش» را در متن‬
       ‫نویسنده از کلک چون خامه کرد‬               ‫نگه داشتم و بعد متوجه این اشتباه شدم و‬
‫ز برزوی یک در سر نامه کرد‬                                         ‫اینک باید آن را تصحیح کرد‪.‬‬
‫(‪۸‬نوشیروان ‪)۷۴۴۳‬‬                                                                ‫نست‪:‬‬
                                                                                   ‫ییت‬
                                                                                     ‫اان ب‬
                         ‫(ویس ‪:)۱۵۳-۵4‬‬                    ‫اگر دل توان داشتن شادمان‬
         ‫کنون ده در بخواهم گفت نامه‬              ‫شهادی چرا نگذرانی زمان؟‬
                                                                       ‫ب‬

‫گبفهتاری کهخون بارد ز خامه‬                               ‫به خوشی بناز و به خوبی ببخش‬
                ‫‪-۲‬مبحث‪ ,‬موضوع مطلب‪:‬‬               ‫مرکونزرا بر دلخویش دخش‬
             ‫ازین در سخن هرچ دارید ياد‬           ‫)‪(TVWY-YFA-F‬‬
                                                                                  ‫دد (با زیر اول)‪‎‬‬
‫سراسر به من بر بباید گشاد‬                              ‫جانور درنده (بهواه دام نگاهکنید)‪:‬‬
‫(‪)۱-۶۸-۹۰۱‬‬
               ‫‪۳‬۔دره‪ .‬گشادگی ميان دکووه‪:‬‬
                                                                  ‫پذیرند؛ هوش و رای و خرد‬
```


## [2026-09-05T14:10:59.770Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('FSF_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfa='۰۱۲۳۴۵۶۷۸۹'\ndef num(s):\n    return int(''.join(str(fa.index(c)) for c in s))\nfor i in range(95,115):\n    p=pages[i]\n    m=re.findall(r'[۰-۹]{2,3}',p[:400])\n    print(i, m[:5], repr(p[:60].strip()[:40]))\nEOF"
}
```


### [2026-09-05T14:11:01.485Z] TOOL RESULT

```
95 ['۹۴'] ''
96 ['۷۴۱', '۱۷۱'] '\u202bبرآمدن\u202c\n\n            \u202bشنیدم که دستان جا'
97 ['۷۱۰', '۲۷۴', '۵۲'] ''
98 ['۰۱', '۷۶', '۶۹', '۲۸۲'] '\u202bبترین نام\u202c\n\n             \u202bیکی انجمن کرد'
99 ['۵۸۲', '۸۶۱', '۱۱', '۷۹'] ''
100 [] '\u202bبرز\u202c\n\n\n                \u202bی\u202c\u202bکر\u202c\n        '
101 ['۶۸۱', '۵۶۷'] ''
102 [] '\u202bبرگی\u202c\n\n                                '
103 [] '\u202bمیان'
104 ['۲۰۱', '۰۴۵', '۶۳۲'] '\u202bبرنشست\u202c\n\n\n\n                            '
105 [] ''
106 ['۸۷۶', '۴۳۳', '۰۸'] '\u202bبه شمشیر جان از تنش برکنیم\u202c'
107 [] ''
108 ['۰۵', '۳۶۱'] '\u202bبسودی\u202c                                 '
109 [] ''
110 ['۶۵۱', '۲۰۲'] '\u202bهر آن کز میان باره انگیزند\u202c            '
111 ['۱۰۸'] '\u202b\u202a۱۰۸\u202c\u202c'
112 [] '\u202bبناکام\u202c\n\n                  \u202bبگویید با م'
113 ['۶۲۱', '۲۶۱'] '\u202b\u202a1۰\u202c\u202c\n\n\n\u202bض'
114 ['۹۲'] '\u202b(منوچهری \u202a:)۹۲\u202c\u202c        \u202bفرس و ص'
```


## [2026-09-05T14:11:08.996Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('FSF_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint(pages[100][:2500])\nEOF"
}
```


### [2026-09-05T14:11:10.509Z] TOOL RESULT

```
‫برز‬


                ‫ی‬‫کر‬
                  ‫ید ه‬
                     ‫خانهٌ خود باز رو‬                                    ‫برخ (به فع اول)‬
‫همتای برد‪.‬‬         ‫شد‬
                    ‫اکی‬‫بلس‬
                         ‫اط‬                                         ‫بهر بهره نصیب‪:‬‬
                                    ‫برداشتن‬             ‫برین نیز چندی بگردید چرخ‬
                 ‫دهاختن» روانه کردن‪:‬‬
                                   ‫باهنرا‬       ‫سیاوش رابد ز نیکیش برخ‬
                                                ‫(‪)۲-۲۹-۳۳۳۱‬‬
‫خروشیادن آمد ز پرده سرای‬                                        ‫(دقیقی ‪:)۶-۲۰۱-۸۳۵‬‬
 ‫)‪(۲-۲-0‬‬                                               ‫سرانجامش آمد یکی تیر چرخ‬
                                ‫ا(باوپلیش)‬
                                         ‫برز‬   ‫چنان آمده بودش از چرخ برخ‬
                                   ‫‪۱‬لند‪:‬‬
                                       ‫ب‬                            ‫(اسدی ‪۰۲۴-۱‬ع)‪:‬‬
              ‫بهبالاشود چو یکی سرو برز‬                  ‫تو ای دانشی چند نالی ز چرخ‬
‫بهگردن برارد ز پولاد گرز‬                       ‫کهایزدبدیدادت از چرخ برخ‬
 ‫(‪)۱-۶۵-۴4‬‬                                                                   ‫برخوردن‬
      ‫پس و پیشهرسوهمیکوفت گرز‬                   ‫مرکب از بر [بان بهره سود] خ‪+‬وردن‪:‬‬
 ‫دوتساکرد بسیار بالای برز‬                                   ‫شدن‪:‬‬   ‫ردار‬
                                                                      ‫خدوو‬
                                                                         ‫ر‌من‬
                                                                            ‫بره‬
                                                                              ‫به‬
 ‫(‪)۲-۲۶۱-۲۵۵‬‬                                    ‫اسفندیار هنگام مرگ پسرش بهمن را به‬
         ‫یکی برز کوهست از ایدر نه دور‬              ‫رستم می‌سیارد تااورا پرورش دهد‪:‬‬
‫همه جای خوردن‪ ,‬گهکام و سور‬                             ‫بسیاموزش آرایش کارزار‬
‫‏)‪(OTA-F*—F‬‬                                     ‫بزم و دشت شکار‬        ‫که‬
                  ‫بيامد یکی برز بالاگزید‬               ‫وار‬
                                                         ‫می و رامش و زخم چوگان ک‬
 ‫یارییاکنهیان ربادید‬
                   ‫باه ج‬                        ‫بزرگی و برخوردن از روزگار‬
 ‫(‪)۲-۱۱۲-۱۳۵‬‬                                    ‫(‪)۶۰۱۲۰۵۴۳۱‬‬
‫(در بیت آخر بالا به معنی تبه پشته‪ ,‬کوه‬                             ‫برد (باپیش اول ‪-‬تازی)‬
```


## [2026-09-05T14:11:24.227Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint('leaves',len(pages))\nfa='۰۱۲۳۴۵۶۷۸۹'\nfor i,p in enumerate(pages):\n    m=re.search(r'\\[pdf page (\\d+)\\]',p)\n    if i in range(0,3): print(i, p[:200])\nEOF"
}
```


### [2026-09-05T14:11:25.839Z] TOOL RESULT

```
leaves 777
0 
1 ۱ ۵ ۱! ۱
7 موم ۳ لام
م ۱ 0 و طق صفرررنیاعدریرماروی
۰ ۱ "۳
۳
م و اس مر هر وه او
7 رین خلت ریز یتایب بره ات
لف‌بال ۶۲ .یرک
ا اند کل داي رشب , رمع
فان تا تا
رن 9 3
کرحم تن
اد شش مرا
مو رم | مر
وک رهب اه 
2 اداره کل دک زون.
شماره ۷9 9 ۳
بر
5
‌ ۰ م۸
و «ارس‌شبات
4
د انشمند محتر م آقای‌د کترمحمد معین‌استاد دانشگاه تهران
فوپانت تاموی ۲۰/۹/۳ ها رتیفارد *
کلیه حقوق‌تجد ید طبم کتاب برهان قاطع با تمحیحات وحواشی
```


## [2026-09-05T14:11:29.752Z] TOOL CALL #52: Bash

```json
{
 "command": "python3 tools/ref_page.py BQT:254 2>&1 | head -40"
}
```


### [2026-09-05T14:11:31.610Z] TOOL RESULT

```
no scan of BQT covers printed page 254 (see 'scans' in refs_online.json)
```


## [2026-09-05T14:11:36.928Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\n# find leaves containing 'بلند' as headword-ish and 'برز'\nhits=[i for i,p in enumerate(pages) if 'برزخ' in p]\nprint('barzax leaves',hits[:20])\nhits2=[i for i,p in enumerate(pages) if 'بالاخانه' in p]\nprint('balaxane',hits2[:20])\n# page number markers\nfor i in range(300,315):\n    m=re.findall(r'[۰-۹]{2,4}',pages[i][:150])\n    print(i,m[:4], pages[i][:50].replace('\\n',' '))\nEOF"
}
```


### [2026-09-05T14:11:39.262Z] TOOL RESULT

```
barzax leaves [471, 499, 553]
balaxane [468, 487, 549, 615]
300 [] ست و 4 سب #احر یض « بکر اول و دای بی نقطه و سکون ث
301 [] « ری الافی » خوانند ؛ و بجای بای بجد بای اخت - حم 
302 [] وخواهر زاده را گونند . اخروش « با رای فرخت بر وزن 
303 [] «کراث الک رکم » خوانند . اخسمه - بفتح اول وسکون ان
304 [] اخی» بر وزن مفی ؛ کاری و چیزی‌را کوبندکه قابل تین 
305 [] و تشنگی را فرو نشاند - و بفتح اول ‏ و کسرثالث در غ
306 [] -9-- درودگری باشد . ومضفقف اکر هم هست که‌آن کلمةٌ 
307 [] ی "ار پیاسیوس - با تحتانی و سین بی نقطه و تحتالی د
308 [] ارجالون کثتاس را در جنگه کشته بود و لهراسب پدر کتت
309 [] خوانندش, وبعض ی کویند منسوب‌باردیل‌ین ارمنین است و
310 [] اردشیران " قهر وخشم یز آمده است٩‏ ؛ و فلم پسر ساسا
311 [] آردسهشت او س باکاف‌فارسی بروزن‌پهلوان, بمعئی اردجا
312 [] بخشایش » بمعنی خیر و خیرات و چیزی در راه خدا بمردم
313 [] مه موم ما ی > ج با کل فا درل مخرفا اردو
314 ['۳۳'] آردو ت برابر نا سس ۳ص اس ای دیس ۳۳ سذ الفبای ار دو
```


## [2026-09-05T14:11:49.478Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in (467,468,470,471,472,486,487,499):\n    p=pages[i]\n    print('=== leaf',i,'===')\n    print(p[:900].replace('\\n',' '))\n    print()\nEOF"
}
```


### [2026-09-05T14:11:53.930Z] TOOL RESULT

```
=== leaf 467 ===
۷ ۱ : ۱ برانه پر اغلیدن - بروزن‌جفا کنیدن» مخخف برآغالیدن است که بمنیتحرض (۱) کردن وبر انگیختن باشد و بعربی اغرا هگویند . بر ااق‌جم « کنابه ازبادی اس تکه‌تخت سلیمان علیه‌السلام را میبرد . بر ! کوه (۷)- بتح اول و ضم کات و سکون واو و ها » نام کوهی است که ما بین «شرق و جئوب فصبٌ اوش واقم است از ولات فرغانه تزديك باندجان . بر ) هلان « بر وزن در آمدن » بمعنی بر انداف - بش اول و سکون نون و دال بی نفطه بالف کشیده و بفا زده . رودهای اسان و حبوانات دیگر را گویند .۷ پر اثه - بفت اول و نون » نلم شهری و مدبنه‌ایست . ح ۱ برازش - بقتح ارل بی وژن نوازش » بمعنی زیبند گی باشد - وبمعنی وصل کردن‌ینه و پاره هم حست برقبا و خرقه و امثال آن . بر ادوان - با واو » بر وزن و ععنی براز بان‌است‌و انآ هن بارة دنباله کاردوشمشر وخنجر و امثال آن باشد که در دسته و قضه‌فرو کنشد. بر اد یشان ۱ < بروزن‌تراودن » بمعنی خوب و زبا نمودن- و وصل کردن باشد چیز برا جچعیر ی ۰ ‌ بر آنش» بغتح‌اول.بروزن‌ومعنی‌خراش‌وزخم لست- وبمعنی‌باشدن

=== leaf 468 ===
براو او هتح اول و سون آخ رکهراو بر ) و ددهسررزن سرایرد» ». شخصیرا کویند که‌امرا وسلاخین اورابلند مرنبه گردانیده بباشند - و بمعنی بنا و امای و دیوار عمارت‌هم آمده است - و بمعتی قلمه و حصار نیز هست - و درب گرفته - و بجیزی عادت فرموده - و از هم جدا ساخته را هم میگویند - و پمعنی‌تقلید کرده نز کفته‌اند چهبر آرردن ععنی‌تهلید کردن هم آمده 3 ر اه بروزن‌بگاه» بمعنی‌خوبسوخوبی- و نیکو و نیکوبی- و آراسته- و آراستگی باشد؛ و برازش و برآزیدن را هم کوشد. بر اهام ۱ بامیم بر وزن فراهام » نام حهودی که بهرام مال او را بلثبك مقا داد ۴ - و ابراهیم را هم گویند و بر ] هختی ۴ با خای نقطهدار بروزن ندانتن » بیمنی بر کشیدنباشد مطلقا . سه بو سس بر ] هنجیدن ۴ - بروزن‌واسنجیدن, بمعنی برآهختن باشد که بر کشبدن است‌مطلقا . بر | هبحتن ِ- بروژن‌در آوختن:بمعنی بآ هختن باشد که بر کشیدن است مطلقا . پر باد - با بایابدبروزن‌سرداره بمعنی بالاخانهرحجرءباشد که بربالایحجره‌ایدیگر ساز ند. بر باره بروزن هر کاره » یمعتی‌بربار است که ح

=== leaf 470 ===
بر جوسیوی ۳ بر توسوسن سین اول مک ور وتحتانی بواو دسیده و بسین دوم زده» بلفت‌بونانی ترعی از لبلاب و عشقه است , و رنگه آن مانند ردگب زعفران باشد و بردرختها پیجد . بر یه س بابای‌فارسی بروزن‌انگيخته, بمصی پیجیده وتاب خورده باشد . بر قاس با ای قرشت‌نر وز نکربای, نام ولایتی است از تر کستان و در آنجا پوستین چخوب میباشد, وآن از پوست روباء آنجا ست دد نپابت پاکیز کی و لطافت و آن یوستین را نیز برتای هیگونند - و نام شهریست درحدود روی سونام یکی از مبارزان و دلیران هم‌هست» وباین معائی با طای حطی هم بنظر آمده است که‌برطای . ٩ باشد‎ بروزن سرتراشك » بممنی برناشك أست . بر لنگه - بروزن خرچنگهه . تشگهدوم باشد از زین اسب - و نوار ماتتدیرا نز گونه که از کربای و غیرمدوزند و بر ؟پوار؛ًاطفال نصب ۳9 و طفل را بدان در کهواره ند ند - ونوعی از بارچهُ کم عرض هم هت . بر ننی ۴ بروزن کردنی » غروروتکبر و تجمر باشد . بر نه بروزن شرطه » نام بر نوابه(۱) است که مبارزی بوده ازابراتبان . ۱ پر یبا - با فوفانی بتحتانی رسیده و بای

=== leaf 471 ===
<- ٩ کرده باشند برجاس گوبند» وانرا که در زمین نمانه کنند حدف خوانند . پر جاسب (۱)- منم اول بروزن لپ راسپ» نام مبارزی است تورانی که با پبران وسه ببجنگه کگودرژ آمده یود » بر حاف- جنم اول وسکون ثالی و جیم فارسی بالف کشیده وبقا زده» نلم غله‌ابست کهآ نرا بعربی ملك و جلبان گوبند . # برجان قدم نهادن - کناب از چاره و علاج کردن و بر هلاك راضی شدن باشد . بر جح ریا - کنابه از دحان ممشوق وخوبان و صاحب حسنان باشد- و برج وررانیژ و 70 بر چخ » با جیم فارسی بر وزن برزخ » بمعتی ژوببن(۲) است, وان ننزه‌ای باشدله کوتاه و نه دراز . بر جده لشان - کنابه از بی حجاب درآمدن باشند " پر جلن ح مخضف برچدن باشد . کر ی سوه » نام برج‌هلال - کنبه از از برج سرطان باشد باعبار ايشکه خانهٌ ماه است . (۱) چك : برجاسب . ۱ مراد « مرچند» است . ۳ ۳ ها ]ای وه مان ۴ - این حمتی لفتی است بر خی پر جیسی ۴ بروزن ادرس » یتکی از نامهای ستار مشتری باشد ۴ ؛ و با اولرتاك‌هر دو فارسی هم آمده است . رخ » با خای نقطه‌دار بر وزن چرخ ‏ بیعنی پاره و 

=== leaf 472 ===
برخقد سر کردن بر خلد‌سر کرش - اجه اتیابداری همیشگی و جاودالی‌بانتن باشک . بر وا ب4 - باواومعدوله‌بروزن‌سردابه, توش و نهالی باشد - و حمخوابه راهیز گوند . بر خود ۱ + باواومسدوله بروزن‌سندر, یی هره باشد که شربك و انازاست سومخفف برخوردار هم هست. وبروزن‌فتفور هم بنظر آدنه ۳ بر 4 ۲ « بروزن چرخه . بمعنی پاره و حصه و بهره و جزوی از کل باشد . لرزحی » بروزن‌چرخی ۰ بمعنی‌فداشدن و فربان کردیدن باشد ۴ - و آنچه در عرش چیزی‌بکسی دهند وبمعنیحصه وبهرمواندکیاز ببار هم صت ؟ . لرث ‏ بفتح اول بروزن فرد » امی است بدور شدن از راه دمتی آزراه دور شوت .- ویمعنی و جتم اول ماضی بردن است - و چیستان و لفز را نیز کفه اند و آلرا بعربی احجه خوانند - و در عربی قماشی است مخصوص یمن کهپردیمانی مد ۷ . پر دا بر ۵ ۷ با بای ابجد بروزن تنها نف . چب ۱ : پرکال . تا ۳ کرد » رت من ازراء دورشو ۸ بر دادن » بروزن ومعنی سردادن ورها. کردن باشد . بر دا - با غين قطمدار و ح رکت‌غیر عملوم ۰ ایرث را گوبند و آن کیاهی است که از دا هیر ونوعتن بر

=== leaf 486 ===
برنداف بر ناف س بفتح اولو انی و سکون‌ثالث و رامع بالف کشیده و فا زده » بمعنی تسمه‌ودوال باشثك - و رودها را دز گویند اعم از آعکه رودء اسان با حیوان دسگر باشد . پر ند » بفتح اول و انی و رأبع وسکون ثالث و کاف » کوه كوييك ويشتة خرد را گویند , و بستی گویند برندك پدنه‌است کوچك ۱۲ هیان دشت و صحرا واقم باشد 1 و ثالث و رابع غیرمعلوم و کف بالف کشيده‌وبميم زده .کیاهی باشد که آنرا بابونة کاو گوشد ۰ بر ده س بروژن‌رو نده , معلوم‌است - و پروانه را نیز گویند و آن جانوری باشد که شبها خود را بثعلهٌ شمع و چراغ زند 1 بر لس ع سم اول وثالث پروزن‌سندس » جامه و کلاه يشمن گنده باشد که بشتر صارا و ترسایان پوشند و بوسر نهند . و بعضی گوشد نام کلاء تصرانیان است که فرنگیان (۱) باشند » و بکر ثالك مروزن مفلس هم بنظر آمده‌است. و بعفی گوبند بمعنی کلاء عربی است ۴  .‏ بر فشسقی س کنابه ازسوارشدن‌باشد ۴. بر نگ - بفتح اول وثانی بروزن‌خدنگ» بمعتی جچری و درای و لق‌درخانه باشد - وکید را نیز گویند که عربان مفتاح‌خوانند ؛ وبایشععن

=== leaf 487 ===
سای هس و بفتح او وسکون ائی‌نام ماه - و ستارمشتری باشد ۱ - و بفتح اول و ضم ثانی ابرو را گونند بر وار ِ بروزن هموار» خانه‌ناستانی باشد . پر واده ۳ بروزن عمواره , بالاخانه و حجر بالای‌حجره باشد - وراهی را نیز کویند توان نمود . بر واد » بروزن دمساز, جای‌قرار و آرام باشد - و نشیمن باز و شاهین و امثال !نرا نیز ۷ پر وازه» بروژن‌دروازه ۰آنشی‌را گونند که بیش بیش عروی افررزند و خوردلی‌وطعامی پرو انا با نون مکور وئحتانی‌بالف کشیده . بلفت بونانی 9 رستنی باشد که مانند عثفه بر درختها پیچد و میوٌ آن شبیه بانگور است. بجهت دباغت کردن چرم بکارآبد» و آنرا بعربی حااق‌الثعر خوانند چه‌از آن ریشها آویزان میباشد , و باین‌سبب هزاز افثان گویندش . ثر وه ع بروزن سفدر . فراویزو سجاف حامد ودامن وسر های‌استن پوستی‌را گونند ۳ ۲۱) چك : ژند و باژند . بروفند و مخفف بارورهم هست ک:باردار و میومدارباش و بلغت زند و بازند (۱) بمعنی برادر باشد ۷- ویمعنی اول بازای تقطمداربروزن ۰ر کز٩‏ وبروزن رموز هر دو آمده اسث - و جملهرا نیز گو

=== leaf 499 ===
و افام رنگه برسوراج ها ذبکه ریزند؛ تانقشش برآورد - و شخصی را نی زکویند که او را بحر بته. باشند و داماد تواند شد - آهنگی‌هم‌هست 1 تویتفی کدام! اد ی ۳ 0 ۱9 ۲۰ بو نج آخر که ها باشد مخنف بستوه است که کهآ مده وملول باشدا - ونم اول و فتح فوفانی فندق را کوبند و آن مفزی باش که خورند . پسته و چم - بفتح را وکر حا هر دو می‌نقطه » زنی را کوش د که هر کر نزاید , واورا بعرمی عقیمه خوانند . بستییاج" - بنتم اول و سکون ثانی و فوفانی بتحتانی رسیده و بای ابجد بالف کشیده و بجیم زده, بلات رومی خسك زا گونند» وبلفت ال نقین عاصی آلامب اقوانف... طنیعت وخ سرد است باعتدال , و ضماد کردن برزرمهای گرم ناف باشد , بس خواسته - کنابه از مطلوب و معشوق باشد ۴ . لس ح بنم اول وسکون ثانی ودال‌ابجده بمشی بست باشد که گلزار است و جاب یکه موه خوشبوی بهمرسد؟۴ - و بضم اول وفتح ئانیمشدد ونسنی بیخ‌مرجانرا کفتة‌اند که اصل‌مرجان‌باشد 6 (۱) چك : ژند و باژند . و باشمعنی بکر ال هم آحده است ۳ مثبت آن قعر درباست. ربعمالی برآن شدضوبر کنند چون
```


## [2026-09-05T14:12:03.982Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -c \"pdf page\" BQT_v1_pages.txt; grep -m3 -n \"pdf page\" BQT_v1_pages.txt; python3 -c \"\nimport json;d=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'));print(json.dumps(d['BQT'],ensure_ascii=False,indent=1))\""
}
```


### [2026-09-05T14:12:08.688Z] TOOL RESULT

```
0
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
 "notes": "Persian OCR is mediocre: headwords and Mo'in's footnotes (e.g. '۱ - رك: ابر کوه', Pahlavi/Avestan Latin forms) are mostly readable but with many character errors; search with short substrings and tolerate errors. BQT_v1_pages.txt was built from the djvu.xml; BQT_v2_pages.txt from pdftotext -layout of the _text.pdf. Volumes 3–5 (roughly ح/خ–ی and the تعلیقات volume) are not online in full text; for those use Dehkhoda quotations of Borhan/Mo'in via vajehyab/abadis/parsi.wiki, or page images on noorlib (different edition). | Vols 3-5 scans (image only) in incoming/BQT; vols 1-2 have OCR text files BQT_v1_pages.txt / BQT_v2_pages.txt. Offsets verified by eye at several pages (v3 drifts by ~4 pages; page_map gives exact positions once built). || UPDATE: vols 3-5 now downloaded (image-only PDFs, verified as Mo'in's edition from title pages and the Latin footnotes) and OCRed locally. Image-only scan OCRed locally with tesseract 5 (fas.traineddata from github.com/tesseract-ocr/tessdata_fast, stored in incoming/_tessdata). *_pages.txt = 'fas' model (best for Persian); *_pages_faseng.txt = 'fas+eng' model (better for the Latin-script Pahlavi/Avestan etyma, worse for Persian). Pages separated by \\f; leaf N = N-th \\f-block 0-based = PDF page N+1. Search with short substrings and tolerate OCR errors. Provenance caveat: picofile is a general file host, the uploads are not from a library; treat as a grey copy (the book is in copyright in Iran). | vol 4 (م–ی) OCR text, tesseract fas+eng, pages tagged [pdf page N], printed = pdf+1917 | vol 5 (ta'liqat) OCR text, printed = pdf-5 | vol 3 (ش–ل) OCR text (689/721 pages), printed ≈ pdf+1203..1209",
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


## [2026-09-05T14:12:16.880Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in (473,474,475,476,477):\n    print('=== leaf',i,'===');print(pages[i][:1200].replace('\\n',' '));print()\nEOF"
}
```


### [2026-09-05T14:12:18.658Z] TOOL RESULT

```
=== leaf 473 ===
۳و۷ بر دفتر افگندن - کنابه از نوشتن باشف . 0 بر دلگ« بروزن‌مرداه . اضانه را کوبند وبمعنی اغلوط و لغز وچبتان هم آمده است وب لغز و چستان گفتهاند .. ۱ بر 6۵ » بروزن‌مرهم ؛ نم اول شهربردع بوده است پیش از زمان سکندر و سکندر آنرا بردع نام نهاده ۱ بر ذهیك < بر وزن سر کشید ؛ مساضی بردمیدن است که رویدن و سبز شدن با۵دیمنی سبز شد وروبید - وبمعنی درغشب شدوقپر آ لوده کردید یز آمده است - و ماشی دمزدن وسخن کفتن - و نمی‌رسالیدن - و خود را پرباد کردن هم صت - و طلوع و اهر شدن صبح را نیز گوبند - و دم زر گرانرا عم کفتهاند . بردن - بکر اول و سکون الی وفتح الث و نون ساکن » بممنی تندی و تیز رفتاری پاشد - و اسب جلد و تندرا نیز گویشد - و بطم اول بمعنی ربودن و بافتن باشد ۴ . بر دنگ -بروزن‌فرسنکه . کوه کوچك و پشتة خردمرا گوبند که در میان سحرا وأقج شده باشد . بر دون » بروزن فرعون » اسب نرجلد ۱ ره: ور :* مررسته و تشد رااگویند, و گویند این‌لت عرییست ۳ . رده ۴ - بروزن ارده ۰ بممنی باشد مطلقا خواه دختر و خواه بسر . بر دی - بروزن‌زردی: نوعی از خرمای لطیف بود که آنرا سنکه اشکنك خواشد - و ظروف سنکی را نیز گویند - و لام کیاهی هم صست و آن بیشثر در مصر میباشد و از آن کاغذ میسازند ٩‏ و بعربی حفاء میگوشد . ۱ رین بروزن کردیدن » بمعتی از راء بطرقی شدن و دور کردیدن از راه باشد . بر دیر لس » بنتح اول و سکون‌ثالی و الث بتحتال

=== leaf 474 ===
برزستد ۱ 3 ۰ ج ووات بنابان را نیز کفته‌اند . بر ددن - بر وزن‌ک رکدن . آنت که دوکس با بیشتر از دو سه طرف انگختان خودرا پیش آورند وحساب برد وباختی کنند - و بمعنی بهم برآوردن و از عم جدا کردن هم هنت ۴ - و رسیدن کشتی راز گونند بکتار دربا و کنابه از هحسری و برابری کردن باشد . برد کار ۴ » با کاف بروزن قرض‌دار . برزیگر و زراعت کننده را گونند . ۱ پر گر * - بنتح کاف فارسی » بمعنی پرزکار و برزمگر باشد که زراعت کننده است . بر د ۵ بروزن‌ریم » بمعنی‌ناز و کرشمه باشد - و نام قلعه‌ابست بر کنار آفت آمو - بر دن « بفتح اول بروزن ارزن » کوچه و محله را کویند ٩‏ - و بمعتی صحرا نیز بنظر آمده است - و آمر بزدن هم هست یمنی بزن- - لیرد سای « بروزن بر‌دهید » بمعنی‌رسید و آمد باش که ماضی رسیدن و آمدن است - و بمعنی سوال کرد و پرسید هم هست که ماضی صژال کزدن و پرسیدن باشد . # بر دویدو یدن حکنابه از کرم‌عنان شدن د رکفت وکوی باشد . 7 رد۵ - بروزن درکه . آراسته و خوب وا راگن و خوی را گوستف:: رت بنتمایلبروزن طرز » بسعنی کدت و زراعت و کشاورزی باشد ۱ - و ماه بثابان را نیز گوبند که بدان کهگل و گچ بر دبوار مالند - ویمعنی زسابی و معشوقی و بلندی بالای (۱) حردم و ثنهةٌ درخت نیر آغفه است - و مطلق بلندی راهم گفته‌اند - ویضم‌اول ۷ وقد و قامت آدمی - ود وعظمت باشد ۴ - و بلندی‌بالای مردم وچاروا را نیز گومند وبمعنی مطلق بلندی و تن

=== leaf 475 ===
ی ۷ سس و بکسر اول تابه باشدکه از کل سازند و نان بر بالای آن پزند ٩‏ سك پردو لا - بخ اول و سکون ثانی و زای قطهدار بواو رسیده و قح تحتانی و لام بالف کشیده . نام مبارزی بوده تورانی در لشکر افراسیاب . بر د۵ - بر وزن لرزه » شاخ درخت را گویند - و بممتی کشت و زراعت هم هست ۲ ۳ پرره‌کاد ؟ « پروزن‌هرزهکار ,برژیگر و زراعت کننده باشد. بر ده گاو ۴ کاو زراعت را گونند» پرره گر ه « بقنح کاف فارسی پروزن بردمدر ؛ بوژسگر و زرات کننده را گوجه بر ر بدن ٩‏ بر وزن لرزیدن بمعنی ورزیدن است که مواظبت و مداومت کردن باشد درکاری . بر ریگر ۳ بروزن عکدیگر ۰ زارغ و ژرامت کننده را گونند ۰ فردلن ٩‏ ۰ بروزن پروین» بمعنیآتش ل ۹ 7 است که عرب ار خوانند - و دام مکی از المة دین ابراهیم زردشت‌هم‌هست که شکسای‌ساخت که آنرا آندبرزین نام کرد و آن آنشکده ششم است - و بمعنی برزن هم آمده است- و صجرا وکوی و محله باشد ٩‏ - و تلم مبارزی بوده ابرانی . بردین کروس ۰ بنم اف و رای قرشت و سکون واو و سین سعفص , نام ,یکی از مویدان است » و موبد حکیم و دانشمند و عالم وبز رکه آتش پرستان باشد. فرص « بفتح اول و سکون انی و سن می‌نقطه » چویی‌باشد که‌بربینی شتر کنندورسمان مهار را بدان بندند - و بمعنی مهار ثیز آهده است وآن رسمانی بائد که برینی کار کذرانندب و بمعنی مهمیز هم حست - و بکی اول بمعنی پنبه باند که بعربی فطن خوانند و شحم الارض نیز گویند - و

=== leaf 476 ===
" بر‌سان « بنتح اول می وزن نرسان : دوشاب میاء رنگه خوشبوی را گویند - و مطلق امت را لیز کفته‌اند از هر پیعمبی که باشد ٩‏ - وکروه آدمپان را هم - و بکسر اول نیز آمده است - و بضم اول اژدها را کویند . پر سر آ هدن - کنابه ازغلبه وافزونی و زبادئی کردن باشد . ۳ بر ص‌غنچه - نم او و غن‌قلمدار, تضم سرو کوعی باشد و آن سیاه رنکه و فربه میشود . سفوف آنکرم شکم را میکشد و آنرا بحریی جوزالایهل و ثمرتالمرعر خوانند ۴ . پر سم ۴ - بروزن‌مرهم » شاخهای‌باريكث بی که باشد بمقدار یك‌وجب که آنرا از درخت هوم ببرند ؛ و آن درختی است شبیه بدرخت کز و اکر هوم نباشد درخت کر و الا درخت انار ء و رسم بریدن آن چنان است که اول کاردی که دس آن هم‌آهن باشد و آنرا برسم چین خوانند (۱) چك : ژند . ۱ " ۳۹ ۱9 مس زمزم نمایند بمتی دهایکه در وقت عبلدت آش و بدن شستن و چیزی خوردن میخوانشد بخوانند . و برسم را با برسم چین ببرندیس‌برسم دانرا قیز آب گفتد و آن ظرفی باشد مانشد قل‌دان وآنرا از طلا و نفره و امشال آن مازند » و برسمهارا اسدرون آن گذارند » و حرگاه خواعند بدن بشوبند باچیزی بخورند با زد (۱) ععنی قسمی از اقسام کتابهای زند (۱) بخوانند چند عدد از آن برس که بجهت آن کار وآن فعل معین است بدست گیرند, چنانچه بجهت خوادن سك وندیداد که یکی از ۳ - رگ : بوس . بقه از مضه ۲۵۵ ( برهان فاطع ۳۷ ) مسعز

=== leaf 477 ===
ده نسکهای عشهور زند )۱( آست سی و پنج برسم بدست گیرید ؛ و بجهت نك بشت ٩‏ بیست وچهار برسم, وهنگلم بدن شتن وچیزی خوردن و عیادت کردن پنج برسم ؛ و چون یکبار نگ وندیداد خوانده‌شودآن برسمپا باطل گردد؛ و از جهت :سکهای دیگر و افمالی که مذکور شد اختیار دارند ء خواهند با همان برسمها عمل کنند و خواهند برسم نازه بدست گیرند . و از شروط برسم بدست گرفتن بدن شستن وجامةٌ باله پوشیدن است . و صاحب فرهنکه جپانگیری کوید این لفت را از مجوسی که در دین خود بغامت فاضل ود و آردشیر نام داشت و او را مجوسان موید میدانستند و درعهدا کیر پادشاه از کرمان بهندوستاي آمده بود تحفیق نمود » اما درچند نخه از فرحتگههسروری‌توشته‌اند که‌برسم ککایی است که آ تش‌پرستان درحین پرستش بردست گیرند مگر. در يك دخه که کیاهی لوشنه شده بود واین‌را با آنچه درفرهنگه جهانگیری نوشته اند فی‌الجمله تردیکی است وان اعلم . برسم چین ه باجيم فارسی بروزن فروردین , کاردی بود که دستآنهم از آهن باشد و فارسان بدان برسم از درخت برند ؟ . # (۱) چك : ژند . برشیان دارو: بر سق له - بروزن مرغوله . قرسی‌باشد که در آن جوز و پزباز و بنگه و دیگی ادوبه کر مکنند و خورلد . بر سیا نا بفتح‌اول وسکون ثانیو کسر الت و بای حطی وتون‌هردو بالف کشیده .رستنی باشد که تخم آن‌مانندنخم کرفی‌است۴ .علت‌جرب را نافع باشد . بر شان باشین نفطه‌دار بروزن افشان. +معنی اعت باشدمطلفاً از عر
```


## [2026-09-05T14:12:36.015Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in (519,520,521):\n    print('=== leaf',i,'(printed ~',i-220,') ===');print(pages[i][:1400].replace('\\n',' '));print()\nEOF"
}
```


### [2026-09-05T14:12:37.488Z] TOOL RESULT

```
=== leaf 519 (printed ~ 299 ) ===
۳:9 بان خصوصاً .و آشیرا نیز که ازآن‌یز ند پلور خوانشد . بلقو ه - بروزن و «عنیکلگوده است؛ وآن غاژه‌ای باش که زنان‌بررومالنده وروبر! سرخ گردانند . بلفحت ه بفتح فا بروزن بدبشت.عاضی بلخفتن ۱ ست که بمعنی جمم کردن و اندوختن باشد بعنی جمم کرد و انسوخت ۷ . بلقدد - با فاف و دال ابجد بر وزن مشتصر؛ متحد. و بی‌دین و بی‌دمات را کوند؟ . بلقندر - بنتم ازل و قاف و دال ایجد و سکون ثانی ونون و رای قرخت» بمعنی دشنام و قدح باشد - و شم اول ملحد و می دین و ی دتالف رااگوشد . بلقّسی « یکی اول و قاف بر وزن پرجیس » نام پادشاه شهر سبا بوده و فص او وسلیمان 4 مشهور است ۴ . پلاك د بنم اول و ثانی و سکون کافی» چم بز رک بر آمده را گوشد - و کر اول و فتح ثانی نسفه و .رمفان و سوغات ی که دوستان از جهت درسنان فرستند . و میوء تاه و لوباوه و جامةٌ لو و حرچیز تازه و لو بر آمده باشد کد طبم از دیدنشس محظوط گزدد؛ و همچنین‌چیزیرا در عربی طرفه خوانند - و کنجشک یکه طرفه باشد - و بکسر اول و الی بمعنی تشبث است و آن چنگه در زدن.بچيزي یا بکنی بود - وبکسر اول وسکون ثانی آش وشرارءآش‌را ۴ بلکامه « بنم اول و سکون ثانی وکاف ببالف کشیده و فتخ میم چی آدزو و بنیارکام وا کویند چثانکه بلهوی بیار هوی را . چه بل بمعنن بسیار باشف . بلکی . بکر اول و ثالك و سکون ثانی و سین بی‌نقطه ۰ سردیوار را گوبند ۰ و منم اول و ناك هم گفته اند و بجای سین بی نقطه لون هم بنظرآمده است ؛ و همینین بجای‌حرف اول بز تون آعده است:که تلکس باشد . کف - منم اول و فتح تالث و سکوق ثانی و فا و دال امجد » رشوت و پاره را دود » و ابکس اول و ثلاث هم درست .ان . بلگفده ‏ بنم اود

=== leaf 520 (printed ~ 300 ) ===
مکتك ون بلکنجات سم .اول و ثالث که کاف فارسی باشد و فتع جیم که خامس باشد وسکون انی و نون و کاف که سادس وآخر باشد هرچیز عجیب وغریب وطرفه را گوین که دیدش مردم‌را بخنده اورد » و بفتح کاف فارسی هم درست خوانند - و بمعنی چپار چوب و پیرامن درخانه هم کفنه‌اند - و بکسر اول نیز بهمین معنی‌آمده پلند گرای - بکس کان فارسی , تفت اف ب که میل عظمت و بزرگی است : ماج - بت اول و میم بالف کشیده بروزن محتاج , نوعی ازکاچی است و آن آشی باشد بی گوشت و بیار آبکی و رقیق » و یشم اول و فتح انی هم آمده است » و بعض یکوند این لغت تر کی است بلمون » بنتح اول بر وزن مجنون . ساذح صحرابی است ؛ و آن برکي باشد دوابی مانند بر کثه کردکان ۰ و آنرا بعربی عرفج بری خوانند . بلمه ‏ بنتح اول و میم وسکون ثانی » رش انبوه و دراز را گویند » و باین معنی جضم اول هم آمده است - و مردم دیش دراز را هم کفثه اند . بلفج - بکراول و ثالی بروژن برنج؛ فدر و مقدار و انداز* چیزی را کوند » و بقئح اول ونانی نز گفته‌اند . پلتجاسپ" -بکر اول و ثانی وسکون تالك و جیم بالف کشیده و سین بی شطه و پای فارسی زده و کاس ات تب که آنرا بوی مادران گویند » و بجای بای فارسی فا هم آمده است که بلتجاسف باشد ‏ لك » بفتح اول بروزنکمند ؛ معروف است که نقیض پست باشد ۴ - و بمعنی چوب بلند نظر ‌ کنابه از عالی‌همت باشد . بلندیی ۴ « بفئح اول بروزن نمدزین » چوب بالاین درخانه باشد وی چهارچوب در خانه را عم کفته‌اند ؛ و باین‌هعنی بکسراولوبای بلنگمشبت و دلن< حعلی ک ۱ اول و ثالی و سکون الث و کاف فارسی و میم مضموم بش و تای‌فرشت زده ؛ بمعنی افر تجمشك است که بالنگوی خود رو باشد و آن 

=== leaf 521 (printed ~ 301 ) ===
و شجاع ٩‏ - و علامتی را ی زکونند که برریزی طاق و ابوان نصب کنند - و نم ولایتی همهست ازایران ۴ - و تاج خروی را ی زکنتماند و آن کوشتی باشد که بر سر او رشته است- و ارچ گوختی که پرختنه گاه زهان حیباشد و بربدن او سثت است . #6 بلوس . ختح اود بی وزن عروی » پمعني فریپ و خدعه باشد - و ثضی را یز ۷1.1 00۵67۷0/۵ -وربارءتژادنلوج بر: :0 00600 ,1206 2۱0۵ ۲6 ,یمه(‎ ٩ 6 . ۷ . در باب زبان بلوچ » رك : : :3 موفتودما نقه۳21۱0 1۵۶ , دهواهدالای‎ 6 ۰. ۷۷ . پریوممناعتة لمند‌وولامی نطههام9_ نامر ممویه‌دانی‎ .2 ۷۵۱ 95۰ . رك : بلوچستان‎ ۴ بلوچستان _ < بلوج ( بل‌قوم )+- ستان (ادا معان4؛ نفحیه‌ایست کوهستالی‌ومسکن‎ طوایف بادبه‌شین که کمتر طوایف خارجی در آنان فون کرده و ابشان هميشه در برایر خارجیان‎ مقلومت کردماند . بلوچستان همواره جزو ايران بوده است . درزمان قاجاربه اختلاقانی بین خان‎ کلات و رسای ابلات پدید آعد و دولت انگلیس بمنوان حکم مکتن را مأمور نسفيةٌ تراع روژسا‎ کرد» وچون برای محافظت سرحد حندوستان متوجه اهمیت معبربولان بود بتدریج این معبر را‎ متصرف شد . چندی حد در ۱۸۹۳ خان کلات را که با انگلیی مضالفت عیکرد بوسائل سیاسی‎ از کار دور کرد و پسرش را با حقوق سالیانه بجای او مثصوب کرد و قاط دبگری از بلوچستان‌را‎ هم متصرف شد . در ۱۸۹۲ و ۹۵ و ۹۱ کمیسیون مختلطی همین شد که حدودی بن بلوچستال‎ و کلات را تب کنند. ولی یج اين کمسیون آن شد که کلات باسم بلوجستان انگلیس ضميمةٌ‎ . هندوستان کردبد و اخروز جزو پاکستان است‎ : مساحت بلوچستان ایران بالغ بر ۱۵۵۰۰۰ کیلومتر مربع و حدودآن ازاین قرار است‎ از طرف شمال سیستان و کرمان
```


## [2026-09-05T14:12:48.216Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"بالکن\" MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt 2>/dev/null | head -5; echo \"--- arezu\"; grep -n \"آرزو\" MON_part1.txt | head -5"
}
```


### [2026-09-05T14:12:48.289Z] TOOL RESULT

```
incoming/MON/MON_2vol_Adena_v1_djvu.txt:20927:بالکن: (.) ابوان کوچکی که در 
MON_part1.txt:20927:بالکن: (.) ابوان کوچکی که در 
--- arezu
1659:کردن: او را در مطلوب و آرزویی منتظر 
2683:آرزوانگیز: تا اشتهاآور. 
2686:آرژوانه: (-)202-.2 [آرزو + انه. سد.] 
2687:(امر.) آنچه آرزو کنند» موضوعغ آرزو. 
2694:آرزوخواه فرهنگ فارسی معین ۴۱۱
```


## [2026-09-05T14:12:50.755Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '20920,20935p' MON_part1.txt; echo \"=== arezu ===\"; sed -n '2670,2700p' MON_part1.txt"
}
```


### [2026-09-05T14:12:50.835Z] TOOL RESULT

```
بالکا: قتعل (.) (گیا.) ازملک. 

بالکانه: (و)محعاده [- پالکانه - بالگانه - 
بادگانه] (ا.) پنجره‌ای که از مبله‌های فلز ی 
ماش 

بالکن: (.) ابوان کوچکی که در 
جلوی ساختمان سازند؛ مهتابی. (نم.) طتَة 
فوقانی تماشاخانه با سینما که قسمتی از سالن 
تحتانی را در ز بر کنر گر 

سال‌ماسکه: 6 2 (امر.) مجلس 
رقصی که شرکت‌کنندگان موظفند با تغییر 
تیچ سوه بر آو سرضی 
یابند؛ بال کوستومه. 
=== arezu ===
پزند. آش آرد. 

ارزم: 2-0 [- رزم] (.) رزم. ک‌ارزار» 


آرژو؛ ۲ ,2۲62 (۱.) خواهش» کام؛ مراد. 
چشمداشت» امید» توقع» انتظار. شوق» 
اشتیاق. شهوت» هوی. معشوق» محوب» 
دلبر. مطلوب» دلخواه. آز» حرص» شره. 
اسستداد رأی» ی خودسری. 
خو استگاری (زن)» خطبه 


آرزوانگیز: تا اشتهاآور. 


آرژوانه: (-)202-.2 [آرزو + انه. سد.] 
(امر.) آنچه آرزو کنند» موضوعغ آرزو. 
آنس‌چه آبسستن از خوردنی‌ها و غیر 
خوردنی‌های عادی (مانند گل و زغال) برای 
خوردن ارزو کند. آنچه خویشان زن آبستن 
پزند و برای او فر ستند. 


آرزوخواه فرهنگ فارسی معین ۴۱۱ 


آرزو خواه: 2.2 (افا.) تمنی کننده» راجی. 
شهوی» شهوانی. 

آرزوسنج: وروی (افا.) آرزومند.
```


## [2026-09-05T14:12:59.986Z] TOOL CALL #60: Bash

```json
{
 "command": "sed -n '1,40p' tools/fetch_source.py"
}
```


### [2026-09-05T14:13:00.031Z] TOOL RESULT

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


## [2026-09-05T14:13:05.910Z] TOOL CALL #61: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/b%CA%B0er%C7%B5%CA%B0-\" \\\n \"https://en.wiktionary.org/wiki/%D8%A8%D8%A7%D9%84%D8%A7\" \\\n \"https://en.wiktionary.org/wiki/%D8%A8%D9%84%D9%86%D8%AF\" \\\n \"https://www.etymonline.com/word/balcony\" \\\n \"https://www.etymonline.com/word/barbican\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 92, root Bhergh: PIE *bhergh- and its Persian/English reflexes\" ; done 2>&1 | tail -20"
}
```


### [2026-09-05T14:13:08.899Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/009ed6a3d0d97ac5.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/2407f984c1cdaa98.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b3033871bcc50b60.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/fea0a6beeaefa20a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/8cc8008461c45a61.txt
```


## [2026-09-05T14:13:11.855Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"=== PIE bhergh ===\"; grep -n -iE \"bʰerǵʰ|high|Descendants|Proto-Iranian\" 009ed6a3d0d97ac5.txt | head -30"
}
```


### [2026-09-05T14:13:11.903Z] TOOL RESULT

```
=== PIE bhergh ===
4:TITLE: Reconstruction:Proto-Indo-European/bʰerǵʰ- - Wiktionary, the free dictionary
6:Reconstruction:Proto-Indo-European/bʰerǵʰ- - Wiktionary, the free dictionary 
72: Reconstruction:Proto-Indo-European/ bʰerǵʰ- 
136: *bʰerǵʰ- ( perfective ) [ 1 ] [ 2 ] [ 3 ] 
141: to be elevated , up high 
146: Terms derived from the Proto-Indo-European root *bʰerǵʰ- (89 c, 0 e) 
169: > ? Old Armenian: բառնամ ( baṙnam , “ to lift up, raise ” ) ( see there for further descendants )
177: Proto-Iranian: *bárjman 
186: Proto-Iranian: *br̥jnáh 
197: Proto-Italic: *forktis ( see there for further descendants )
200: > ? Proto-Celtic: *brixtus ( “ magical formula, incantation ” ) ( see there for further descendants )
234: Retrieved from " https://en.wiktionary.org/w/index.php?title=Reconstruction:Proto-Indo-European/bʰerǵʰ-&oldid=92171312 "
276: Reconstruction:Proto-Indo-European/ bʰerǵʰ-
```


## [2026-09-05T14:13:14.400Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && sed -n '130,235p' 009ed6a3d0d97ac5.txt"
}
```


### [2026-09-05T14:13:14.439Z] TOOL RESULT

```
 Proto-Indo-European
 [ edit ] 

 Root
 [ edit ] 

 *bʰerǵʰ- ( perfective ) [ 1 ] [ 2 ] [ 3 ] 

 to rise up , ascend 
 Synonyms: *skend- , *kelH- 

 to be elevated , up high 

 Derived terms
 [ edit ] 

 Terms derived from the Proto-Indo-European root *bʰerǵʰ- (89 c, 0 e) 

 *bʰérǵʰ-e-ti ( thematic root present ) 
 Proto-Tocharian: *pärkatäre ( “ to rise, come up ” ) [ 4 ] 
 Tocharian A: pärkatäre 

 Tocharian B: pärkatäre 

 *bʰérǵʰ-t ~ *bʰr̥ǵʰ-ént ( root aorist ) 

 *bʰe-bʰórǵʰ-e ~ *bʰe-bʰr̥ǵʰ-ḗr ( reduplicated perfect ) 
 Proto-Indo-Iranian: *bʰabʰárȷ́ʰa 
 Proto-Indo-Aryan: *babʰárźʰa 
 Sanskrit: बबृहाण ( babṛhāṇá , med.part. ) 

 *bʰorǵʰ-éye-ti ( eye-causative ) 

 *bʰr̥ǵʰ-yé-ti ( ye-present ) [ 5 ] 
 Proto-Anatolian: 
 Hittite: 𒈦𒆠𒄿𒀀𒊍𒍣 ( pár-ki-ya-az-zi /⁠parkiyazi⁠/ , “ to ascend ” ) 

 *bʰr̥-né-ǵʰ-ti ~ *bʰr̥-n-ǵʰ-énti ( nasal-infix present ) 
 Proto-Armenian: 
 > ? Old Armenian: բառնամ ( baṙnam , “ to lift up, raise ” ) ( see there for further descendants )

 Proto-Indo-Iranian: *bʰr̥nȷ́ʰáti 
 Proto-Indo-Aryan: *bʰr̥nźʰáti 
 > ? Sanskrit: बृंहति ( bṛṃháti , “ to increase, expand ” ) 

 *bʰérǵʰ-mn̥ ~ *bʰr̥ǵʰ-mén-s 
 Proto-Indo-Iranian: *bʰárȷ́ʰma 
 Proto-Iranian: *bárjman 
 Avestan: 𐬠𐬀𐬭𐬆𐬰𐬌𐬨𐬀𐬥𐬄𐬨 ( bar ə zimanąm , gen.pl. ) [ 6 ] 

 *bʰérǵʰ-ont-s ~ *bʰr̥ǵʰ-n̥t-és 

 *bʰérǵʰ-o-s 

 *bʰérǵʰ-ō ~ *bʰr̥ǵʰ-n-és 
 Proto-Indo-Iranian: *bʰr̥ȷ́ʰnás 
 Proto-Iranian: *br̥jnáh 
 Avestan: 𐬠𐬀𐬭𐬆𐬱𐬥𐬀 ( bar ə šna , inst.m.sg. ) 

 Old Persian: 𐎲𐎼𐏁𐎴𐎠 ( b-r-š-n-a /⁠baršnā⁠/ , inst.m.sg. ) 
 Middle Persian: 
 Manichaean script: 𐫁𐫢𐫗 ( bšn /⁠bašn⁠/ ) 
 Book Pahlavi script: [Book Pahlavi needed] ( bšn /⁠bašn⁠/ ) 

 *bʰérǵʰ-s ~ *bʰr̥ǵʰ-és 

 *bʰérǵʰ-ti-s ~ *bʰr̥ǵʰ-téy-s 
 Proto-Italic: *forktis ( see there for further descendants )

 *bʰérǵʰ-tu-s ~ *bʰr̥ǵʰ-téw-s 
 > ? Proto-Celtic: *brixtus ( “ magical formula, incantation ” ) ( see there for further descendants )

 *bʰérǵʰ-u-s ~ *bʰr̥ǵʰ-éws 

 *bʰr̥ǵʰ-ró-s [ 7 ] 
 Proto-Tocharian: *pärkäre ( “ long ” ) [ 7 ] 
 Tocharian A: pärkär 

 Tocharian B: pärkare 

 *sperǵʰ- ( with s-mobile ) [ 8 ] 

 Unsorted formations 
 > ? Sanskrit: ब्रह्मन् ( bráhman ) ( or related to Old Norse bragr ( “ poetry ” ) ) 

 References
 [ edit ] 

 ^ Pokorny, Julius ( 1959 ), “ bhereg̑h- ”, in Indogermanisches etymologisches Wörterbuch [ Indo-European Etymological Dictionary ] (in German), volume 1, Bern, München: Francke Verlag, pages 140-141 

 ^ Rix, Helmut , editor ( 2001 ), “ *bʰerg̑ʰ- ”, in Lexikon der indogermanischen Verben [ Lexicon of Indo-European Verbs ] (in German), 2nd edition, Wiesbaden: Dr. Ludwig Reichert Verlag, →ISBN , pages 78-79 

 ^ Wodtko, Dagmar S.; Irslinger, Britta; Schneider, Carolin ( 2008 ), “ *bʰerg̑ʰ- ”, in Nomina im indogermanischen Lexikon [ Nouns in the Indo-European Lexicon ]‎ [1] (in German), Heidelberg: Universitätsverlag Winter, pages 30-34 

 ^ Adams, Douglas Q. ( 2013 ), “pärk-”, in A Dictionary of Tocharian B: Revised and Greatly Enlarged (Leiden Studies in Indo-European; 10 ), Amsterdam, New York: Rodopi, →ISBN , page 399 

 ^ Kloekhorst, Alwin ( 2008 ), “parkii̯e/a-ᶻⁱ”, in Etymological Dictionary of the Hittite Inherited Lexicon (Leiden Indo-European Etymological Dictionary Series; 5), Leiden, Boston: Brill, →ISBN , pages 736-737 

 ^ Cheung, Johnny ( 2007 ), “ *barz ”, in Etymological Dictionary of the Iranian Verb (Leiden Indo-European Etymological Dictionary Series; 2), Leiden, Boston: Brill, →ISBN , pages 12-13 

 ↑ 7.0 7.1 Adams, Douglas Q. ( 2013 ), “pärkäre*”, in A Dictionary of Tocharian B: Revised and Greatly Enlarged (Leiden Studies in Indo-European; 10 ), Amsterdam, New York: Rodopi, →ISBN , page 399 

 ^ Hackstein, Olav ( 2023 ), “ When words coalesce II: Preverb incorporation in Indo-European ”, in Indo-European Linguistics , volume 11 , number 1, →DOI , →ISSN , page 21 of 1–40 

 Retrieved from " https://en.wiktionary.org/w/index.php?title=Reconstruction:Proto-Indo-European/bʰerǵʰ-&oldid=92171312 "
```


## [2026-09-05T14:13:21.527Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"=== bala ===\"; grep -n -iE \"Etymology|Middle Persian|Proto-Iranian|bālā|balcony|barbican\" 2407f984c1cdaa98.txt | head -25; echo; echo \"=== boland ===\"; grep -n -iE \"Etymology|Middle Persian|Proto-Iranian|buland\" b3033871bcc50b60.txt | head -20"
}
```


### [2026-09-05T14:13:21.585Z] TOOL RESULT

```
=== bala ===
81: Etymology 
110: Etymology 1 
128: Etymology 2 
140: Etymology 3 
314: Etymology
317: From Middle Persian [Term?] ( /⁠bālā⁠/ ) , from Proto-Iranian *bārźаh- (via a series of sound changes *rź > *rd > l ) + a suffix *-ā of unknown origin. The first component is derived from Proto-Iranian *barź- ( “ to elevate, increase (height) ” ) , from Proto-Indo-European *bʰerǵʰ- ( “ to rise up ” ) . [ 1 ] 
341: bālā
345: bālā
375:نور چشمش آسمان را میشکافت bā čunīn čašm-ē ki bālā mē-šitāft
444: Etymology 1
2320: Etymology 2
4182: Etymology 3
4211: Persian terms inherited from Middle Persian 
4212: Persian terms derived from Middle Persian 
4213: Persian terms inherited from Proto-Iranian 
4214: Persian terms derived from Proto-Iranian 
4244: Middle Persian term requests 

=== boland ===
76: Etymology 
102: Etymology 
194: بُلند ( bulænd, buland ) ( Mahallati , Vonishuni ) 
223: Etymology
226: From Middle Persian 𐭡𐭥𐭫𐭭𐭣 ( buland ) , from Old Persian *br̥dāh , from Proto-Iranian *br̥jáns ( “ high, tall ” ) . [ 1 ] 
250: buland
254: buland
299: → Gujarati: બુલંદ ( buland ) 
302: Hindi: बुलंद ( buland ) 
303: Urdu: بلند ( buland ) 
314: Gurmukhi script: ਬੁਲੰਦ ( buland ) 
315: Shahmukhi script: بُلَند ( buland ) 
327: Etymology
330: Borrowed from Classical Persian بُلند ( buland ) . Compare Punjabi ਬੁਲੰਦ ( buland ) / بُلَند ( buland ) , Gujarati બુલંદ ( buland ) .
356: Persian terms inherited from Middle Persian 
357: Persian terms derived from Middle Persian 
360: Persian terms inherited from Proto-Iranian 
361: Persian terms derived from Proto-Iranian 
375: Middle Persian terms with non-redundant manual transliterations
```


## [2026-09-05T14:13:27.245Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"== balcony ==\"; grep -n -iE \"balcony|balcone|balco|Langobard|beam\" fea0a6beeaefa20a.txt | head -12; echo; echo \"== barbican ==\"; grep -n -iE \"barbican|barbacane|Persian|Arabic\" 8cc8008461c45a61.txt | head -12"
}
```


### [2026-09-05T14:13:27.297Z] TOOL RESULT

```
== balcony ==
1:URL: https://www.etymonline.com/word/balcony
4:TITLE: Balcony - Etymology, Origin & Meaning
6:Balcony - Etymology, Origin & Meaning 
21: Origin and history of balcony 
23: balcony (n.) 
25: 1610s, "platform projecting from a wall of a building surrounded by a wall or railing," from Italian balcone , from balco "scaffold," which is from a Germanic source (perhaps Langobardic *balko- "beam"), from Proto-Germanic *balkon- (see balk (n.)). With Italian augmentative suffix -one . From 1718 as "gallery in a theater." Until c. 1825, regularly accented on the second syllable. Related: Balconied .
28: Entries linking to balcony 
32: also baulk , Middle English balke , from Old English balca "ridge, bank," from or influenced by Old Norse balkr "ridge of land," especially between two plowed furrows, both from Proto-Germanic *balkon- (source also of Old Saxon balko , Danish bjelke , Old Frisian balka , Old High German balcho , German Balken "beam, rafter"), from PIE root *bhelg- "beam, plank" (source also of Latin fulcire "to prop up, support," fulcrum "bedpost;" Lithuanian balžiena "cross-bar;" and possibly Greek phalanx "trunk, log, line of battle"). Italian balco "a beam" is from Germanic (see balcony ).
42: bench-like seat for certain worshipers" (ladies, important men, etc.), frequently enclosed, from Old French puie, puy "balcony..., elevated place or seat; elevation, hill, mound," from Latin podia, plural of podium "elevated place," also "front balcony...
46: 1510s, "gallery, portico, balcony," later "flat, raised place for walking" (1570s), from French terrace (Modern French terasse...
50: newspaper correspondent, as may naturally be supposed, is one of alternate cloud and sunshine—one day basking in an Andalusian balcony...
54: also verandah, 1711, Anglo-Indian, from Hindi varanda, which probably is from Portuguese varanda, originally "long balcony...

== barbican ==
1:URL: https://www.etymonline.com/word/barbican
4:TITLE: Barbican - Etymology, Origin & Meaning
6:Barbican - Etymology, Origin & Meaning 
21: Origin and history of barbican 
23: barbican (n.) 
25: "outer fortification of a city or castle," mid-13c., from Old French barbacane "exterior fortification" (12c.), a general Romanic word, said to be ultimately from Arabic or Persian (compare bab-khanah "gate-house"); according to Watkins from Old Iranian compound *pari-varaka- , from *pari- "around" (from PIE root *per- (1) "forward," hence "in front of, around") + *varaka- , from PIE root *wer- (4) "to cover."
28: Entries linking to barbican 
34: It might form all or part of: afford ; approach ; appropriate ; approve ; approximate ; barbican ; before ; deprive ; expropriate ; far ; first ; for ; for- ; fore ; fore- ; forefather ; foremost ; former (adj.); forth ; frame ; frau ; fret ; Freya ; fro ; froward ; from ; furnish ; furniture ; further ; galore ; hysteron-proteron ; impervious ; improbity ; impromptu ; improve ; palfrey ; par (prep.); para- (1) "alongside, beyond; altered; contrary; irregular, abnormal;" paradise ; pardon ; paramount ; paramour ; parvenu ; pellucid ; per ; per- ; percent ; percussion ; perennial ; perestroika ; perfect ; perfidy ; perform ; perfume ; perfunctory ; perhaps ; peri- ; perish ; perjury ; permanent ; permeate ; permit ; pernicious ; perpendicular ; perpetual ; perplex ; persecute ; persevere ; perspective ; perspire ; persuasion ; pertain ; peruse ; pervade ; pervert ; pierce ; portray ; postprandial ; prae- ; Prakrit ; pre- ; premier ; presbyter ; Presbyterian ; preterite ; pride ; priest ; primal ; primary ; primate ; primavera ; prime ; primeval ; primitive ; primo ; primogenitor ; primogeniture ; primordial ; primus ; prince ; principal ; principle ; prior ; pristine ; private ; privilege ; privy ; pro (n.2) "a consideration or argument in favor;" pro- ; probably ; probe ; probity ; problem ; proceed ; proclaim ; prodigal ; produce ; profane ; profess ; profile ; profit ; profound ; profuse ; project ; promise ; prompt ; prone ; proof ; proper ; property ; propinquity ; prophet ; prose ; prostate ; prosthesis ; protagonist ; Protean ; protect ; protein ; Proterozoic ; protest ; proto- ; protocol ; proton ; protoplasm ; Protozoa ; proud ; prove ; proverb ; provide ; provoke ; prow ; prowess ; proximate ; Purana ; purchase ; purdah ; reciprocal ; rapprochement ; reproach ; reprove ; veneer .
42: It might form all or part of: aperitif ; apertive ; aperture ; barbican ; cover ; covert ; curfew ; discover ; garage ; garment ; garnish ; garret ; garrison ; guarantee ; guaranty ; kerchief ; landwehr ; operculum ; overt ; overture ; pert ; warn ; warrant ; warrantee ; warranty ; warren ; wat ; Wehrmacht ; weir .
44: It might also be the source of: Sanskrit vatah "enclosure," vrnoti "covers, wraps, shuts;" Lithuanian užveriu, užverti "to shut, to close;" Old Persian *pari-varaka "protective;" Latin (op)erire "to cover," (ap)erire "open, uncover" (with ap- "off, away"); Old Church Slavonic vora "sealed, closed," vreti "shut;" Old Irish feronn "field," properly "enclosed land;" Old English wer "dam, fence, enclosure," German Wehr "defense, protection," Gothic warjan "to defend, protect."
90: Share barbican 
94: https://www.etymonline.com/word/barbican Copy
```


## [2026-09-05T14:13:36.451Z] TOOL CALL #66: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/%D8%A2%D8%B1%D8%B2%D9%88\" \\\n \"https://en.wiktionary.org/wiki/%D8%A8%D8%B1%D8%B2%D8%AE\" \\\n \"https://en.wiktionary.org/wiki/%D9%81%D8%B4\" \\\n \"https://en.wiktionary.org/wiki/%D8%A8%D8%A7%D9%84%DA%A9%D9%86\" \\\n \"https://en.wiktionary.org/wiki/%D8%A8%D8%B1%D8%B2\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 92, root Bhergh: Persian reflexes arezu/barzax/fas/balkon/borz\" ; done 2>&1 | tail"
}
```


### [2026-09-05T14:13:39.460Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/977f513ec2320ffc.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/113500b587fe58fa.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e5c9283ab37e7dba.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c22068384a8d8939.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/8943fd8dd3435d02.txt
```


## [2026-09-05T14:13:42.316Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in 977f513ec2320ffc 113500b587fe58fa e5c9283ab37e7dba c22068384a8d8939 8943fd8dd3435d02; do echo \"########## $f\"; grep -n -A3 -iE \"^ *Etymology *$\" $f.txt | head -40; done"
}
```


### [2026-09-05T14:13:43.896Z] TOOL RESULT

```
########## 977f513ec2320ffc
73: Etymology 
74-
75- 2.2 
76- Noun 
--
87: Etymology 
88-
89- 3.2 
90- Pronunciation 
--
113: Etymology 
114-
115- 4.2 
116- Pronunciation 
--
130: Etymology 
131-
132- 5.2 
133- Noun 
--
285: Etymology
286- [ edit ] 
287-
288- From Iranian Persian آرزو ( ârzu ) .
--
315: Etymology
316- [ edit ] 
317-
318- From Middle Persian ʾlcwk ( ārzōg , “ desire, lust ” ) , from Proto-Iranian *rauǰ , *rauč ( “ to desire, please ” ) , of unclear further origin. [ 1 ] There may be a connection to Proto-Indo-European *lewk- ( “ to shine ” ) , as PIE *l > r and *k > *c (palatal) or š in Iranian contexts.
--
429: Etymology
430- [ edit ] 
431-
432- Borrowed from Classical Persian آرزو ( ārzō ) with the majhūl vowel lost (ō > ū).
--
486: Etymology
487- [ edit ] 
488-
489- Borrowed from Urdu آرزو ( ārzū ) , from Classical Persian آرزو ( ārzō ) .
########## 113500b587fe58fa
62: Etymology 
63-
64- 1.2 
65- Noun 
--
85: Etymology 
86-
87- 2.2 
88- Noun 
--
161: Etymology
162- [ edit ] 
163-
164- From Parthian *bwrz-ʾxw ( /⁠burz-axw⁠/ , “ height, unsurmountable passage ” ) , from Parthian bwrz ( /⁠burz⁠/ , “ high ” ) + ʾxw ( /⁠axw⁠/ , “ world ” ) .
--
364: Etymology
365- [ edit ] 
366-
367- Borrowed from Arabic بَرْزَخ ( barzaḵ ) , from Parthian *bwrz-ʾxw ( /⁠burz-axw⁠/ ) , from Parthian bwrz ( /⁠burz⁠/ , “ high ” ) + ʾxw ( /⁠axw⁠/ , “ world ” ) . 
########## e5c9283ab37e7dba
79: Etymology 
80-
81- 2.2 
82- Particle 
--
296: Etymology
297- [ edit ] 
298-
299- From فيه ( fī , “ there is/are ” ) + ـش ( -š , “ not ” ) .
########## c22068384a8d8939
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
--
149: Etymology
150- [ edit ] 
151-
152- Etymology tree
########## 8943fd8dd3435d02
```


## [2026-09-05T14:13:54.147Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"=== barzax persian sec ===\"; sed -n '150,200p' 113500b587fe58fa.txt; echo \"=== balkon ===\"; sed -n '140,200p' c22068384a8d8939.txt"
}
```


### [2026-09-05T14:13:54.194Z] TOOL RESULT

```
=== barzax persian sec ===

 Appearance

 move to sidebar 
 hide 

 From Wiktionary, the free dictionary

 Arabic
 [ edit ] 

 Etymology
 [ edit ] 

 From Parthian *bwrz-ʾxw ( /⁠burz-axw⁠/ , “ height, unsurmountable passage ” ) , from Parthian bwrz ( /⁠burz⁠/ , “ high ” ) + ʾxw ( /⁠axw⁠/ , “ world ” ) .

 Noun
 [ edit ] 

 بَرْزَخ • ( barzaḵ )  m ( plural بَرَازِخ ( barāziḵ ) ) 

 separation , partition 
 609–632 CE , Qur'an , 55:20 : بَيْنَهُمَا بَرْزَخٌۭ لَّا يَبْغِيَانِ baynahumā barzaḵun lā yabġiyāni 
Between them is a barrier [so] neither of them transgresses. 

 ( religion , chiefly Islam ) netherworld ; barzakh ; hades ; purgatory ( otherworldly existence, generally temporal, which may include elements of punishment and/or reward ) 

 ( geography ) isthmus 

 Declension
 [ edit ] 

 Declension of noun بَرْزَخ ( barzaḵ )

 singular

 basic singular triptote 

 indefinite

 definite

 construct

 informal

 بَرْزَخ 
 barzaḵ 

 الْبَرْزَخ 
 al-barzaḵ 
=== balkon ===
 From Wiktionary, the free dictionary

 Persian
 [ edit ] 

 Persian Wikipedia has an article on: بالکن 

 Wikipedia fa 

 Etymology
 [ edit ] 

 Etymology tree

 Proto-Germanic *balkô 
 Frankish *balkō bor. 
 Medieval Latin balcō bor. 
 Italian balcone bor. 
 French balcon bor. 
 Persian بالکن 

 Borrowed from French balcon .

 Pronunciation
 [ edit ] 

 ( Dari, formal ) IPA ( key ) : [bɑːl.kʰʊ́n] 

 ( Dari, formal ) IPA ( key ) : [bɑːl.kʰʊ́n] 
 ( Kabuli ) IPA ( key ) : [bɑːl.kʰʊ́n] 

 ( Hazaragi ) IPA ( key ) : [bɔːl.kʰún] 

 ( Iran, formal ) IPA ( key ) : [bɒːl.kʰón] 

 ( Tajik, formal ) IPA ( key ) : [bäl.kʰɔ́n] 

 Readings

 Dari reading ? 

 bālkun

 Iranian reading ? 

 bâlkon

 Tajik reading ? 

 balkon

 Noun
 [ edit ] 

 Dari

 بالکن , بالا خانه 

 Iranian Persian

 بالکن
```


## [2026-09-05T14:14:02.136Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && grep -n -iE \"Persian|Etymology|high\" 8943fd8dd3435d02.txt | head -20; echo \"=== fas file heads ===\"; grep -n -iE \"^ *Persian|^ *Arabic|mane\" e5c9283ab37e7dba.txt | head"
}
```


### [2026-09-05T14:14:02.192Z] TOOL RESULT

```
62: Etymology 1.1 
74: Etymology 1.2 
94: Persian 
96: Toggle Persian subsection 
99: Etymology 1 
114: Etymology 2 
197: Etymology 1.1
663: Etymology 1.2
676: to accentuate , to set off , to highlight 
680: ( figurative ) to emphasize , to highlight (an issue, a theme, etc.)
1179: high 
1183: Persian
1186: Etymology 1
1189: From Middle Persian wlc ( warz , “ work, agriculture ” ) , from Proto-Iranian *warj- ; see there for further information.
1217: Steingass, Francis Joseph ( 1892 ), “ برز ”, in A Comprehensive Persian–English dictionary (overall work in English), London: Routledge & K. Paul 
1221: Etymology 2
1224: From Middle Persian [script needed] ( bwlc /⁠burz⁠/ , “ high ” ) , ultimately from Proto-Indo-European *bʰerǵʰ- . Akin to Parthian 𐫁𐫇𐫡𐫉 ( bwrz /⁠burz⁠/ , “ high, lofty ” ) and Old Georgian ბორცჳ ( borcwi , “ hill ” ) , an Iranian borrowing.
1233: Iranian Persian
1241: high , tall 
1253: Dehkhoda, Ali-Akbar ( 1931– ), “ برز ”, in Dehkhoda Dictionary Institute , editors, Dehkhoda Dictionary (in Persian), Tehran: University of Tehran Press . 
=== fas file heads ===
127: Permanent link 
317: Arabic terms with quotations
```


## [2026-09-05T14:14:02.541Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '5085,5115p' FVQ.txt"
}
```


### [2026-09-05T14:14:02.584Z] TOOL RESULT

```
Rossini, Glossarium, 117. In Phon. SIS is a sculptor: cf. Harris, Glossary, 91. 

3 Massignon, Lexiqut technique, 52, however, considers it as an Arabic word 
specialized in this meaning under Aramaic influence. 

4 So Ahrens, ZDMG, Ixxxiv, 20. 



FOREIGN VOCABULARY OF THE QUR*AN 77 

T 1 *}j (Barzakh). 

xxiii, 102 ; xxv, 55 ; Iv, 20. 
A barrier or partition. 

In xxv, 55, and Iv, 20, it is the barrier between the two seas (<J^j) 

where the reference is probably to some cosmological myth. In xxiii, 
102, it is 1 used in an eschatological passage, and the exegetes do not 
know what the reference is, though as a glance at at-Tabari 1 s Com- 
mentary will show, they were fertile in guesses. 

That the word is not Arabic seems clear from the Lexicons, which 
venture no suggestions as to its verbal root, are unable to quote any 
examples of the use of the word from the old poetry, and obviously 
seek to interpret it from the material of the Qur'an itself. 

Addai Sher, 19, sought to explain it from the Pers. 1) j j, weeping
```


## [2026-09-05T14:14:05.093Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '5115,5145p' FVQ.txt"
}
```


### [2026-09-05T14:14:05.136Z] TOOL RESULT

```
or crying, but this has little in its favour, and in any case suits only 
xxiii, 102. Vollers, ZDMG, 1, 646, makes the much more plausible 

suggestion that T- j j*. is a by-form of r***J* parasaiuj from the Phlv. 
!g) frasang, Mod. Pers. ^AJL-^d, which preserves its form fairly 



well in Gk. 7ra/)a<rayy??9, but becomes Aram. NOHS or HOHS * ; 

Syr. t*a>iS) whence the Ar. f*"j*' The phlv - WXVft) frasangan 
of PPGl, 116, means a measure of land and of roads, 2 and could thus 
fit the sense barrier in all three passages. 



(Burhdn). 

ii, 105 ; iv, 174 ; xii, 24 ; xxi, 24 ; xxiii, 117 ; xxvii, 65 ; xxviii, 
32, 75. 

An evident proof. 

In all the passages save xii, 24, and xxviii, 32, it is used in the 
sense of a proof or demonstration of the truth of one's religious position. 
In these two cases, one from the story of Joseph and the other from 
that of Moses, the word refers to an evident miraculous sign from 

1 Levy, Worterhuch, iv, 125; Telegdi, in JA, ccxxvi (1935), p. 252.
```


## [2026-09-05T14:14:16.247Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== HRN bala/buland/burz/arzu/fas ==\"; grep -n -iE \"bâlâ|bālā|bala '|buland|burz|ārzū|arzū|arzu|faš|fas '\" HRN.txt | head -25"
}
```


### [2026-09-05T14:14:16.300Z] TOOL RESULT

```
== HRN bala/buland/burz/arzu/fas ==
2131:(vd. 6 (71) GL), varzak (AV.), varzUan, varz(i)snTk;
2134:198. hur», *Höhe, hoch' E(\burz\ bulend.
2136:hoch'; phlv. burz, burzak^ burz{i)sn^ burzUan^ buland;
2140:burz etc. (36); sar. LW. büand, bilik.
6387:'gefrieren, erfrieren' (H. No. 245) ; lit. szdlfas 'kalt'.
8316:(Bund.) 2), marzUan 'coitiren*, mälUan, mCU(i)8n; ai.
9577:und im Burzönäme, Macan, 1533 Vers 3 v. u., 1583
```


## [2026-09-05T14:14:18.992Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '2125,2150p' HRN.txt; echo \"=== HRN 171 (bala) ===\"; grep -n -E \"^ *17[01]\\.|171\\. \" HRN.txt | head"
}
```


### [2026-09-05T14:14:19.044Z] TOOL RESULT

```
Das u findet sich nicht in den Dialekten, ebenso
auch nicht bei pu/ten, murden u. a. m. (vergl. KZ. 32,
572 flf.).
197. berz^ verz (m Is. 30, 24) 'Feldarbeit*, veme^ verzis^
verz% berztden^ versfiden^), verzgäv, verzäv Tflugstier.
aw. [/^varz- 'schaffen, tun'; phlv. varz 'Feldarbeit'
(vd. 6 (71) GL), varzak (AV.), varzUan, varz(i)snTk;
mand. LW. N'^nxi *Saaten'; arm. gorc *Werk', gorcem
Virken*.
198. hur», *Höhe, hoch' E(\burz\ bulend.
ap. vergl. Bardiya-; aw. berez^, barez- etc. Höhe,
hoch'; phlv. burz, burzak^ burz{i)sn^ burzUan^ buland;
ai. bfhdnt-; arm. barjr *hoch', barnam 'erheben' (H.
No. 52).
kurd. berz] oss. d. barzond, bärzönd (56); bei. LW.
burz etc. (36); sar. LW. büand, bilik.
199. herzen 'Stadtviertel, Quartier.
ap. vardanor- 'Stadt' ; aw. verezena-^ varezCLna- ; phlv.
varz(i)sn, daneben arm. LW. berd 'Burg'; ai. v^dna-
'Umhegung, umfriedigter, befestigter Platz, Flecken,
Ortschaft' 2).
Vergl. Bartholomae, BB. 13, 57 (nur sehe ich
keine rechte Möglichkeit, von dem värün geschriebenen
PehlevTworte zu varz zu kommen ; die Ortsnamen auf
'Verd und -gird gehören keinesfalls hierher).
200. berseiu 'Barsomzweig' (Sahn.).
=== HRN 171 (bala) ===
1869:170. häk 'Furcht*.
1872:171. hälä *hoch\
10949:170. rar 'Glanz, Licht\ selten (AW.-Komm., Bund. 24, 25),
10952:171. rajntwintar 'südlich, mittäglich'.
```


## [2026-09-05T14:14:21.900Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '1872,1885p' HRN.txt; echo \"=== HUB 171/198 ===\"; grep -n -E \"^ *(171|198)\\. \" HUB.txt | head"
}
```


### [2026-09-05T14:14:21.957Z] TOOL RESULT

```
171. hälä *hoch\
aw. haresiah' 'Höhe'; phlv. bälä^ baldig bal(i)st (aw.
harezista-, z. B. vd. 2 (75)).
bei. baläd, n. bäläd 'Höhe ; empor, auf* (81) ; kurd.
LW. bälä. /
172. bäliS, bälist 'Kissen, bälfn,
g. bälist; Kä§. böUsm, böliSt
aw. barezis' 'Decke, Matte*; phlv. bäl(i)sn (bälln be-
deutet im Phlv. nur 'Höhe, Gipfel', es steht für
aw. bareSnU'j; ai. barhis- 'Opferstreu'; arm. barj
ngooxfcpdXaiop (H. No. 53).
LW. kurd. bäliät, bälisne^ böl%w^ bälge (H.-Sch.);
oss. t. baz 'Kissen* (50); wa/. baleß^ sar. baldjc.
173. hallden 'wachsen, zunehmen* (Sahn. I, S. 3 Vers 49),
=== HUB 171/198 ===
744:171. Bal. balad 'H6he* scheint, wie auch Geiger, Laut-
3856:171. Dem A vesta entlehnt.
```


## [2026-09-05T14:14:35.034Z] TOOL CALL #75: Bash

```json
{
 "command": "for u in \\\n \"https://abadis.ir/fatofa/%D9%81%D8%B4/\" \\\n \"https://abadis.ir/fatofa/%D8%A8%D8%A7%D9%84%DA%A9%D9%86/\" \\\n \"https://abadis.ir/fatofa/%D8%A2%D8%B1%D8%B2%D9%88/\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 92, root Bhergh: Dehkhoda/Mo'in entries for fas, balkon, arezu\"; done 2>&1 | tail"
}
```


### [2026-09-05T14:14:43.445Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/7f557541af63c72b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/72e79cb5b24a9327.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/68cbb959d918875b.txt
```


## [2026-09-05T14:14:46.555Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in 7f557541af63c72b 72e79cb5b24a9327 68cbb959d918875b; do echo \"##### $f\"; grep -n -E \"معین|یال|فرانسه|فر\\.|په\\.|پهلوی\" $f.txt | head -12; done"
}
```


### [2026-09-05T14:14:51.015Z] TOOL RESULT

```
##### 7f557541af63c72b
18: فش. [ ف َ ] ( ص ) پریشان. || ( اِ ) کاکل اسب را نیز گویند. ( برهان ). کاکل اسب. یال. ( فرهنگ فارسی معین ) : 
20:بریده فش و یال اسب سیاه. فردوسی.
21:گرفتش فش و یال اسب سیاه 
27:- گیسوفش ؛ اسبی که فش و یال او چون گیسو زیبا باشد : 
42:- ارمنی فش ؛ کافر. بی دین. نامسلمان : 
58: فردینان - مارشال فرانسه و بریتانیا و لهستان (و.تارب ۱۸۵۱ ف. ۱۹۲۹ م . ) . و از مدرسه پلی تکنیک فارغ التحصیل شد ( ۱۸۷۳ ) و سپس بصنف توپخانه رفت . بعد بسمت استاد علم سوق الجیش در مدرسه عالی جنگ منصوب گردید ( ۱۸۹۸ ) و سپس بفرماندهی سپاه بیستم را بعهده گرفت و حمله بر آلمانها را در کاله رهبری نمود و بر آنان غلبه کرد ( ۱۹۱۴م. ) . سپس فرمانده نظامی گروه شمالی ( ۱۹۱۵م . ) و رهبر حملات بهار و پاییز در آرتوا و اداره کننده عملیات جنگی سپاه ششم ( ۱۹۱۶ م . ) مشاورفنی دولت فرانسه و رئیس مجمع شورای متحدین در ورسای ( ۱۶۱۷ م . ) عالیترین فرمانده قوای متفقین ( مارس ۱۹۱۸ ) و مارشال فرانسه ( اوت ۱۹۱۸ ) گردید و فاتح جنگ شناخته شد.
63: فرهنگ معین
65: (فَ ) (اِ. ) ۱ - کاکل اسب . ۲ - یال .
73:۲. یال اسب: گرفتش فش و یال اسپ سیاه / ز خون لعل شد خاک آوردگاه (فردوسی: ۵/۴۱۲ حاشیه ). 
92: قله، طره، تاج، ستیغ، یال، کلاله، بالاترین درجه، فش
96: یال، فش
108:• فرهنگ فارسی، محمد معین، انتشارات امیر کبیر، تهران، ۱۳۷۵
##### 72e79cb5b24a9327
29: فرهنگ معین
31: (کُ ) [ فر. ] ( اِ. ) ۱ - ایوان . مهتابی . ۲ - طبقة بالای تئاتر یا سینما. ۳ - ایوان کوچک جلوی کاشانه ، ایوانک (فره ). 
143: آبادیس از سال 1385 فعالیت خود را در زمینه فن آوری اطلاعات آغاز کرد. نخستین پروژه آبادیس، سایت دیکشنری آبادیس بود. دیکشنری آنلاین آبادیس از ابتدا تاکنون تغییرات بسیاری کرده و ویژگی های مختلفی به آن اضافه شده است. آبادیس افزونه ای کاربردی برای مرورگرهای فایرفاکس و کروم و اپلیکیشن موبایل طراحی کرده است که میتوانید از لینک های بالا دانلود کنید. دیکشنری آبادیس شامل بخش هایی نظیر دیکشنری به زبان های مختلف از جمله انگلیسی، فارسی، عربی و همچنین بیست دیکشنری تخصصی با تلفظ انگلیسی و آمریکایی، ترجمه مخفف و کلمات اختصاری، مترجم آنلاین متن، لغتنامه دهخدا، فرهنگ معین، فرهنگ فارسی عمید، فرهنگ مترادف ها و متضاد ها، معادل فارسی کلمه یا به شیوه درست تر برابر پارسی واژه، فرهنگ سره، عبارات مصوب فرهنگستان زبان و ادب فارسی، دانشنامه عمومی، دانشنامه اسلامی، دیکشنری نام ها، هم خانواده یاب، تصویر مرتبط با کلمه، معنی در حل جدول کلمات متقاطع و ابزارهایی مانند واژه ساز ، راهنمای انتخاب اسم و ... می باشد. 
##### 68cbb959d918875b
21: معنی: امید، انتظار، اشتیاق، ( پهلوی، ārzok )، خواهش، کام، مراد، چشمداشت، توقع و انتظار، میل و اشتیاق برای رسیدن به مراد یا مقصودی معمولاً مطلوب، ( اَعلام ) ( در شاهنامه ) دختر شاه یمن و همسر سلم پسر فریدون و نیز دختر ماهیار گوهر فروش و همسر بهرام گور، از شخصیتهای شاهنامه، نام دختر سرو پادشاه یمن و همسر سلم پسر فریدون پادشاه پیشدادی
66: فرهنگ معین
136:آرزو برای اولین بار در تئاتر ال کاپیتان در هالیوود، لس آنجلس، در ۸ نوامبر ۲۰۲۳ به نمایش درآمد و در ۲۲ نوامبر در ایالات متحده اکران شد. [ ۶] این فیلم نقدهای متفاوتی از سوی منتقدان دریافت کرد و بیش از ۲۴۴ میلیون دلار فروش داشته است. 
235:فرهنگ فارسی، محمد معین، انتشارات امیر کبیر، تهران، ۱۳۷۵
237:فرهنگ کوچک زبان پهلوی، دیوید نیل مکنزی، ترجمه مهشید فخرایی، پژوهشگاه علوم انسانی و مطالعات فرهنگی، تهران، ۱۳۷۹
257:ترکیب ( اسم ) [پهلوی: ārzōk]
265:فرهنگ فارسی معین
272:این واژه در سنسکریت: ارتهه artha؛ اوستایی: اَئِزنگه aezangh؛ در سغدی: آغَذو Aqażu؛ پارتی: آورژُگ و آغاذگ AqAżag، Avaržog؛ در مانوی: آورزگ Avarzog؛ در پهلوی: آرزُک و آرزُگ Arzog/k. 
280:ترکیب ( اسم ) [پهلوی: ārzōk]
291:میل تو را سوق به سوی فراموشی میمانی در خیالی 
298:حق را فراموش روی در گرداب خیالی
327: واژه آرزو در زبان پهلوی *اورزوگ awarzog ( ابر زوگ ) و سپس آرزوک خوانده میشده که در آن پیشوند ابر نشانگر برتری و زوگ - زوک همانست که امروزه ذوق خوانده میشود. ازینرو معنای واژه آرزو همانا امید برتر یا شوق والا یا نشاط بالاتر است
```


## [2026-09-05T14:15:07.166Z] TOOL CALL #77: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=4200 && NR<=5500 && /^[0-9]{2,4}$/ {print NR\": \"$0}' KLN_1966.txt | head -30"
}
```


### [2026-09-05T14:15:10.372Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-05T14:15:13.560Z] TOOL CALL #78: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -oE \"\\b1(4[0-9]|5[0-5]|8[5-9])\\b\" KLN_1966.txt | awk -F: '$1>4200 && $1<5600' | head -20; echo \"---\"; sed -n '4300,4306p' KLN_1966.txt | cut -c1-200"
}
```


### [2026-09-05T14:15:15.703Z] TOOL RESULT

```
4256:140
4257:141
4313:142
4320:143
4349:144
4350:145
4396:146
4444:148
4458:149
4483:150
4493:151
4521:152
4521:153
4550:154
4551:155
4568:155
5295:185
5331:186
5332:187
5389:188
---
bake,  tr.  and  intr.  v.  —  ME.  baken,  fr.  OE.  bacan, rel.  to  ON.  baka,  Swed.  baka,  Dan.  bage, MDu.  backen,  Du.  bakken,  OHG.  bahhan, backan,  MHG.,  G.  backen,  fr.  l.-E.  base 
Derivative:  bak-erv,  n.
baksheesh,  n.,  a  gratuity ;  a  tip.  —  Pers.  bakhshish, lit.  ‘gift’,  a  derivative  of  the  verb  bukhshidan,  ‘to give’,  fr.  I.-E.  base  *bhag-,  ‘to  distribute,  share out�
Balaena,  n.,  a  genus  of  whales,  the  Greenland whale.  —  L.  ballaena,  balaena.  See  baleen, balaghat,  balaghaut,  n.,  tableland  above  the  pas¬ ses  (Anglo-Ind.)  —  Formed  fr.  Pe
balan-
balm
Worterbuch  der  russischen  Sprache,  I,  p.40, Heidelberg,  1908-13,  is  rel.  to  Russ,  balabolit’, ‘to  chatter,  babble',  from  the  I.-E.  imitative  base *balb-,  whence  also  L.  balbu
```


## [2026-09-05T14:15:25.182Z] TOOL CALL #79: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== WLD Bd2 ==\"; grep -n -oE \"bhere.h-[^,;]{0,90}\" incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt | head -8; echo \"== IEC ==\"; grep -n -oE \"b(hergh|herǵh|hergh)[^,;]{0,80}\" IEC.txt | head -8; echo \"== SYN high ==\"; grep -n -oE \"bfhant[^,;]{0,80}|brhant[^,;]{0,80}\" SYN.txt | head -5"
}
```


### [2026-09-05T14:15:26.928Z] TOOL RESULT

```
== WLD Bd2 ==
== IEC ==
1236:bherghó
1236:bherghio)
1237:bherghos 'strong place' (identified in Gmc. with bhergh- and bhréh-
1237:bherghó
1781:bherghö (WP II
1782:bherghó (WP II
1794:bhergh- Skt. brhát
1795:bhergh-. WP II
== SYN high ==
992:brhant- ‘high
7598:brhant- ‘great
21781:brhant- ‘high
26305:brhant-
26317:brhant-
```


## [2026-09-05T14:15:29.471Z] TOOL CALL #80: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '1790,1800p' IEC.txt | cut -c1-600; echo \"=== SYN 992 ===\"; sed -n '985,1000p' SYN.txt | cut -c1-400"
}
```


### [2026-09-05T14:15:29.529Z] TOOL RESULT

```
“long for’; Lat. cf. (?) suf-fragor, -ari “vote for
bhrétos, a (bhr&atos, 3) ‘bright’. Z-gde of bherét-, q.v. Ir. brighid (‘fair maiden’, whence Bridget); Norw. borket (salmon pink’; e-gde in MHG -brecht, in cpds. (and com. W Gmc)
bhrgh- ‘streak, line’. Cf. bhorgh-. Cf. WP IT, 165 Cz. Slovak brza ‘seam, vein, grain in wood"; Li. birZis, io “marking strip of field"; Latv. birzs, f. pl. biržu 'seed-drill; birze, id.
(bhrg&h-. Variant of brgh- and bhré-, qv. Cf. ON brugga (2) “break”
bhr&hont- (bhrghnt-, bhrghont-) ‘high; height’. WP II, 172. See bhr£&hus & bhergh- Skt. brhát; Av borezafit; Oss. bárzond, pl. bärzändtä; Per. buland, baland; Tokh. A -párkant (B oärk park, pirko) ‘sunrise’; Lat. frons, gp frontium (Ennius: pl. frundes) (forehead, gravity, severity'. For the seman- tics cf. OCS čelo 'forehead': Li. kéin “to raise); Osc. cf. Frunter (name of a god); Gaul. brigantes 'hillmen'; Olr. bríanda *fa- mous’; OBr. cf. brientin ‘noble’; OW breint, braint, „brein, bryein ‘privilege, state’; W braint, id.; Frankish *burgunds; OE brant: ON b
bhrghus, os “high; height’. WP II, 172. See bhr&hont-, bhergh-. WP II, 172 Skt. cf. brhát; Av. borozoó; Oss. (o-gde. Am- big. bardz, barz ‘mass, crowd': (?) Arm. bardz (2) “hip, thigh’; Arm. bardzr, gs. bardzu ‘high’; Tokh. A cf. párkár, B parkre long; Hitt. parkus; Olr. brí ‘noble’ beside Ir. brigh ‘virtue, power; Sequanian brig- “high — of winds’; Gaul (ambig.) briga Ch, But cf. bhrgh-); W brí, Cor. bry ‘rank, degree, esteem’; OW bry ‘above’: (?) MHG bor ‘up’. Cf. the e-gde forms in Arm. erkna-berdz ‘high as heaven’, lerna-berdz ‘high as a mo
bhrio (1) ‘strike; fall, befall’. Lat. cf. fors, gs fortis (: OE byrd “fate”, fr.
bhr2os, io — bhrs-
15
20
25
=== SYN 992 ===
ON fjall (fell), Dan. fjeld ‘mountain’, Sw. fjall ‘high mountain’ (ME, NE fell fr. ON) : OHG felis, NHG fels ‘rock’, Skt. pasana- ‘stone’, etc. (1.44). AL
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
cr ee ra SS NR
|
Digitized by Arya Samaj Foundation Chennai and eGangotri
THE PHYSICAL WORLD IN ITS LARGER ASPECTS 25
though the root connection is uncertain, the sense ‘rock, stone’ is more widely dis- tributed and prob. earlier. Walde-P. 9.66. Falk-Torp 223.
Dan. bjerg, Sw. berg, OE beorg (‘moun- tain, hill’ and ‘burial mound’, in former sense replaced by the Fr. forms, in the latter sense NE barrow), OHG, NHG berg, etc., the most widespread Gmce. word for ‘mountain’ (but ON bjarg ‘rock, precipice’; in Goth. only bazrga- het = dpewh ‘hill country’) : Skt. brhant- ‘high, great’, Av. barazant- ‘high’, bara- zah- ‘height, m
OE din ‘mountain, hill’ (NE down), ODu. dina (> Du. duin ‘sandhill’, Fr., NE dune), formerly believed to be a loanword fr. Celtic (Ir. din ‘fortified place’), but this is now generally doubt- ed; perh. fr. the root seen in Skt. dhu- ‘shake’, etc., with development similar to that in Grk. 6ts, @tvds ‘sandbank’ (*Of-tv-). Walde-P.:1.837. Falk-Torp 171. Franck-v. W.141. NED sv. do
OE munt fr. Lat. méns, montis; ME mount, mountain fr. OFr. mont, mon- tat(g)ne (above, 2).
OK hyll, ME, NE hill : Grk. xodwvés, Lat. collis, etc. (above, 1).
Dan. bakke, Sw. backe ‘hill’ : ON bakki bank’, NE bank, etc. (1.33). Walde-P. 2.148,
Du. heuvel, MAG hiibel ‘hill’ : OHG hovar, OE hofer ‘hump’, Lith. kupra ‘hump’. Here also Av. kaofa- ‘mountain peak, camel’s hump’, OPers. kaufa Mountain’ (NPers. kwh ‘mountain’) : Lith. kaupas, ChSl. kupt, NE heap, NHG haufe ‘heap’, Grk. xidés ‘bent’, all fr. TE *keup-, *keub-, *keubh- in words for ‘bend, curve’. Walde-P. 1.372 ff. oh ha a Gor, pe mound’, fr
- hauhs, OHG hoh, ete. ‘high’
(12.31), ultimately connected with the preceding group *keubh-, etc., above. Walde-P. 1.371. Hence also NHG hiigel ‘hill’, by blend with MHG hibel. In the same group Dan. hoj ‘hill’ : hoj ‘high’, like NHG héhe, NE height fr. the respec- tive adj. forms.
OHG buhil, MHG bdihel ‘hill’ : ON bola ‘blister, boss’, prob. fr. an exten- sion of IK *bhu- beside *bu- in words for ‘swell’ (cf. Grk. Bouvds, above, 1). Walde-P. 2.114, 146.
```


## [2026-09-05T14:15:38.626Z] TOOL CALL #81: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== NYB ==\"; grep -n -oiE \"b(ala|uland|urz)[^ ]{0,4} [^,;]{0,60}|arzo[gk][^,;]{0,60}|bu(s|š) [^,;]{0,40}\" NYB_vol2_glossary.txt | head -20"
}
```


## [2026-09-05T14:15:39.657Z] TOOL CALL #82: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== TLM Bardiya ==\"; grep -n -oE \"Bardiya[^.]{0,200}\" TLM.txt | head -5; echo \"== ARY index ==\"; grep -n -E \"بالا|بلند|برز\" incoming/ARY/ARY_pages.txt | head -10"
}
```


### [2026-09-05T14:15:40.746Z] TOOL RESULT

```
== NYB ==
763:burzen mihr the names of the three sacred fires connected with the 
763:burzén mihr 95%
903:buland (g. v.) 389. — 2. subst. top 4015
995:balas 1041
1036:buland [bwlnd] high
1036:buland. V. also bālāt
1036:balast, burz.
1047:burz [bwlc'] high 1921
1047:buland; MPrth bwrz
1047:burz; cf Harburz.
1049:burzčn [~-yn'] in ätur ~ Mihr
1052:burz, v. s. v. harven.
1053:burz and väng (g. v.). Paz. sub- stitutes burzävandihä
1347:bala; NP darvēš
1932:burz [hlbwlc'] the mountain chain surrounding this world 8611
2556:burzen ~ the third of the three imperial fires 11%. 2°
2798:balance: kč héc kustak ~ nē kunēt (the balance) which does not go dow
2868:bala (ŠGV).
2953:burz ~ H. is a wall all around it). — < *pari- küna- ‘that which 
3004:balas 93
```


### [2026-09-05T14:15:43.643Z] TOOL RESULT

```
== TLM Bardiya ==
194:Bardiyam  avajan  karahy-32)[a  naiy]  azda  abava tya  Bardiya  avajata10  pasava  Kanbujiya  Mudrayam  33)[asiya]va yafti  Kanbujiya  Mudrayam  asiyava  pasava  kara  araika  abava 34)[pasava]  drauga  dah
195:Bardiya  amiy  hya  Kuraus  pu0ra  Kanbuji-
216:Bardiya  (i
216:Bardiya;  when  Cambyses  slew  Bardiya,  it was  not  known4  to  the  people  that  Bardiya  was  slain;  afterwards
238:Bardiya  the  son  of Cyrus  brother  of  Cambyses;  afterwards  all  the  people  became estranged  from  Cambyses  (and)  went  over  to  him,  both  Persia' and  Media  and  the  other  provinces;  he  se
== ARY index ==
85:باور می‌کردند که آریایی‌های راستین مردمی بلند قامت با چشمان آبی ر موی طلایی بودند که از نظر
220:دست نیست. وی علت تعیین محل گهواره در نواحي شمال دریاهای سیاه و خزر منحصر به پیش بالا
330:نرع جمجمه‌ها (رأس و پیشانی بلند و استخوان‌های گونه‌ی برجسته) و شاخص سر آنها ا
380:در انجیل آمده است که مردم پابل (8۸881) آغاز به ساختن برجی کردند که قرار بود بلندی
957:یکی از سه اندیشه‌ی بالا بودند. ۱-نوما پامپیلیوس (۳01/211179 111۸ که بنیانگذا رگروه‌های !
1032:عم سازمان ایل و امت: همانطور که در بالاگفنیم 1084 واژه‌یع «خانه» بود و واژه‌ی ریس
1055:تحت‌الشعاع قرار نمی‌داد. شاه در بالای هرم قدرت قرار داشت ولی پدر و رئیس ابل نیز هر یک
1167:و غیره مواجه کرده است. ولی علیرغم همه‌ی پستی و بلندی‌هاء زبان‌های ایرانی امروز (فارسی»؛ کردی
1172:نخستین به زبان‌های اوستایی و پارسی کهن و پهلوی و بالاخره فارسی نوین است. همانطو رکه در پیش
1224:رابطه‌ی زبانهای ایرانی با یکدیگر نیز (همانطور که در بالاگفته شد) در آثار دانشمندانی
```


## [2026-09-05T14:15:56.123Z] TOOL CALL #83: Bash

```json
{
 "command": "sed -n '1,80p' tools/verify_check.py"
}
```


### [2026-09-05T14:15:56.179Z] TOOL RESULT

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


## [2026-09-05T14:15:58.086Z] TOOL CALL #84: Bash

```json
{
 "command": "sed -n '80,140p' tools/verify_check.py"
}
```


### [2026-09-05T14:15:58.135Z] TOOL RESULT

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


## [2026-09-05T14:16:41.476Z] TOOL CALL #85: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -oE \"b[ae]r[3o9e]sa-[^,;]{0,120}|barasa-[^,;]{0,120}\" BRT.txt | head -10; echo \"---\"; grep -n -iE \"Widerrist|Mähne\" BRT.txt | head -10"
}
```


### [2026-09-05T14:16:43.683Z] TOOL RESULT

```
---
3104:(oder  'Mähnen-)  oder  Bauch-'  (oder ■Schwanz-)haar"  Yt./^.jr,  16.10.
28766:lem  Ring  befeiligt  sind  (Hauc  Essayt' 397),  während  als  eigenlliche  Filter  eine  Sclüle Löchern  {laSl  i  nuk  süräx)  dient,  in jene  Haare  bineinlegt.  S.  die  Ab- bildung bei  DsT.  ZA.  /,  Taf.  vi,  woio  S.  uuv, LXXX,  Nach  Vd.  8,  z6  kann  das  vari  ans  den Schwanihaaren  einet  weissen  Stier»  oder  aoch -  weniger  gut  -  aus  den  Mähnenhaaren  eines Pferds  bestehen;  s.  Bthl.  IF.  //.  129.  Dsranf bezieht  sich  die  mehrmal»  titirte  .\w.-Stelle: ^Ä/  vi  (var>ia)  aifiait  vä  iiattsa  (sd.).  S.  noch Pü.  and  Jaim  var>t  (.ra*.)  N.  lOS.
```


## [2026-09-05T14:16:48.948Z] TOOL CALL #86: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -iE \"mane\\b|barsa|barəsa|bar.sa-\" AHM.txt | head -12"
}
```


### [2026-09-05T14:16:48.999Z] TOOL RESULT

```
725:19-11. Grass-land magnate Mithra we worshi>...(=7)..., whom the warriors worship at (= ending down close to) the manes! of their horses, requesting strength for their teams, health for themselves, much watchfulness? against antagonists, ability ta strike back at enemies, avility to rout lawless,? hostile opponents. (Here repeat 4-6.)
818:ham hi8* cimane® bararnuha ni. hi§ dasva gardnmane,
1515:479, translates ‘on the neck of their horses’, but understands that ‘the divinity is invaked to exercise his beneficent influence 9n the animal that should bear the warriors to victory’. Htl. insists that barafa- does not mean ‘back’ but ‘neck’. In fact it means ‘mane’, as shown by its Iranian cognates, cf. Arm. sas and bar¥, Sogd. Bung, Bal. dusk, PS. wrad, Oss. dare, etc, As toradaéstar-, which Htl. wants to restrict to its etymological mean~ ing ‘Wagenkamafer’, sur stanza, in which the r. seem to de on horse- Sack, can be cited beside Gtar} sponta radaestara (Ny 5.6, etc.), in support af the view that the word had been generalized in the sense of ‘warrior’. xr’, Bth.’s translation of pouru.spaxiti-, ‘far-reaching espying (of enemies), espying (the e.) from afar’, although based on the usual, well- attested meaning of spas- ‘ta see, adserve, espy’, is unconvincing, hecause pouru- means ‘much, many’, not ‘far-reaching’; who would ask ta see much of his enemy? Gdn,’s ‘haufiges gefangennchmen der feinde’ stands on weak ground, while Lo.’s and Iitl.’s rendering ‘seeing the enemies first’ implies an unwarranted emendation to *paourvd.s9°. The anly acceptable interpretation is Da.’s, who translated ‘bonae garde contre ceux qui font du mal’. This at least agrees with the Pahl. transl. pur daspanih (to Y 57.26) and with the meaning ‘to watch over’ which spas- appears to have in Yé 11.14 (quoted below, nate 41, p. 195). Da. also managed to make this meaning fit the awkward (‘worthless’ in Bth.’s view, $.v. pifana-) passage Yi 9.1: drvdspam.. .yazamaide drvi .pasvam drvd.staorgm.. .pouru, spaxstt diirat pi)ana x a}ravana darayd.haxaSra- yana ‘nous sacrifions 4... Drvaspa...qui tient le petit bétail en santé, qui tient le gros bétail en santé,. .. qui veille sur eux au loin et au large (reading padana) avec une longue amitié qui apporte le bien-étre’. For Da. pouru.spaxsti was thus an instr. indicating the means by which Drvaspi is dred. sased, etc.: “keepiag the cattle fit thanks to her donne garde’. Alternatively one might adopt the variant reading pourn.- spaxstim, and take this as a bahuvrihi compound in apposition to drvaspam ‘Drvaspa who exerts much watchfulness afar (d@raz)’.>
1606:24°. We find 5a@vara.spasans here, and °spasanz in st. 49, bath times in the nom. sg. Bth., followed by Duch, Comp. 177, justifiably assumed thematic treatment of a stem *spasan-, since “spasand has a parallel in the.nom. sg. 5aevara .casmana (stem °éasman-) in st. 141. The history of these forms can be pursued more closely: the @ of bagvara.- spasan3 is derived from the unthematic acc. sg. °spasanam, which evidently was the cause of the transfer to the them. inflection; similarly the them. gen. inmanahe in A. 3.7 (W9. 595} is built on a stem *4inmana-, which was extracted from the unthem. acc. *¢t#mdanam; there is thus a chance that the nom. °spasand resulted from a shortening of @ in the nom. “spasand, cf. upamana-, etc., note gf, p. 167. The them. inflection °spasand,* °ssasanai, etc., may explain the ‘datif 4 vocalisme prédésinen- tiel long’ (Benv., Jnf. 50) puSrane in Vend. 4.47: it is the unthem. *9udrane which has borrowed the long 2 of the them. stem *pu9rana-, itself an offshoot of the unthem, acc. *pudranam. The same explanation may apply to cimane, discussed below, note 321. [See Addenda.]
1646:32". ham his cimane daranuha ‘trage sie hin zum Sammel-Orte (Cinvat)’ (Wi.); ‘zur Freude’ (Sai. doudtfully); ‘schreibe sie uns auf rechnunz’ (Gdn.); ‘ramasse-les ensem Ie’ (Da.); ‘sammle sie auf zur Bu3zahlung’ (Bth., followed by Htl.); ‘bring zie zusammen zum
1649:Vorrat’ (Lo.), The assumed base of mane is thus either Aay- ‘to heap up’, or kay- ‘to repay'. Benv., Znf. 50, without himself pronouncing on the base, rejects 3th.’s interpretation of the form as an infinitive, and Pasits a nominal stem. ciman-, with long d@ as in pudrane (on which see above, note 24°), This stem I would analyse as an -an- extension (cf. uxine, Benv., 09. cit. 51) of the Olr. base *éam- ‘to sip, drink’, cf. Skt. camatz, NPers, éant, camidan: Mithra collects the libations in his chariot (see st. 136) and takes them ta his abode in Paradise (see note 501), where he consumes them at leisure. [See Addenda.]
2021:49°. haxadra- is generally thought ta mean ‘assaciation, friendship’; it is here under the care of Ra&nu, elsewhere of the Fravaiis (see infra), or of RaSnu’s sister (above, p. 195) ASi. In Yz 17.4 A&Si safeguards haxa5ra- for the house of the pious Zoroastrian, as Ra¥nu does in the present case: hubaoidis baaSaite nmanam | yebhe nmane aff vanuhi | stra pa8a nidadaite | agramaitis darayai haxadrai ‘well-scented is the house (of him) in whose house the z00d A&i strang(ly} sets her feet, watchingf over long haxaSra-’.
2185:that nothing can be learned fram it.[ The second entry, though unsatis- factorily translated by Bth., does seem to reveal the existence of a present stem aipi-dGra- which in the middle means ‘to atone’: 2 hé asti 49a ha hz asti Zparatis aigt.pdramndi 13a asaone nit anaipt.paramna druja nmane hai#ya anhan astayé (Vend. 8.197). Bth. translated: ‘das ist dafiir die Siihne fiir den Glaw>igen, der hier BuBe tut; fiir den (aber), der nicht BuBe tut (, gilt der Spruch§): im Haus der Drug sind das die rechten Gesellen’. Gdn., who has the same interpretation, commented (Studien, p. 6, n. 1): ‘ait oder an- ist zu viel’. We must obviously give preference ta Da.’s solution, which requires no alteration of the text: ‘telle est... Vexpiation qui dégage le fidéle qui se soumet 4 l’expiation; non celui qui ne s’y saumet pas: celui-lA certainement ira habiter la maison de la Druj’. For natt anaipt.paramndai so taken there is a close parallel in 232 ainixbarata (Vend. 3.37, quoted above, note 45?).
2190:§ drijo nmane, etc. being a quotation fram Y 49.11.
2517:Bth.’s interpretation of astd as infinitive to gs- ‘ta reach’ was rightly rejected by Benv., Inf. 39, in whose opinion ato is the acc. of *astah- ‘lieu d’arrét, halte’, a noun he would also recognize in vourw.aita- (on which see note 444 above). Benv. translated uriraosé asta ‘il interdit la halte’, but did not say what he thought of aim. That this loc. should stand far the dat., as Duch.’s rendering imphes, is manifestly imgossible. ' Bth.’s ‘bei ihm’ (meaning chez soz) (see 9. 4, line 8 fram bottom) is equally unbelievable. As to Hzf.’s ‘him’, it is based on an emendation of ahmi to him. Only Maria W. Smith’s ‘in that (glace)’ has a chance of deing correct, since in Ossetic Digor ami < ahmi (see Miller, Ossetisch, 35) means ‘here’. In Avestan, however, such use of ahmz would be excep- tional (it is nat recognized anywhere by Bth.) and one hesitates to admit it in the present passage, seeing that ast3 may very well be a -#- noun in the loc. with which ahmi agrees. From the paint of view of word-forma- tion a stem *as#i- is more easily justified than *astah-, cf. OInd. asiz ‘reaching’, against the rare appearance of the Olnd. suffix -tas- (Wn.— Debr., 11, 2, 615 sq.). The meaning will be ‘joint of reaching, place af arrival, goal’, and ami ait is either ‘at this goal’, or, more likely, ‘at his goal’, as we find ahmi nmane ‘in his house’, etc., in YAv. (cf. Bth., W. 4.2).
2851:p. 164, n, The YAv. form of the wards yedh2 and vavho in the prayer (instead of expected Gath. yehyd and vahyd) provides no valid reason for disdelieving the statement in Y 21.1 that Zarathu8tra is the authar of the yeehé hatam prayer, Elsewhere, too, Gathic words have beea replaced by their YAv. equivalents in Gathic quotations, cf. drvanté Vend. 5.62 (dragvant3 Y 31.20), nmane Vend, 8.197, 14.18 (damané Y 49.11), ars mé Vend. 19.19 (arak mat Y 44.1), yeihe Vend. 20.3 (yehya Y¥ 31.4), yeahe me Y 15.2 (yehya mi Y 51.22, see above, >. 165), and mazda tava Y 19,14 (mazda tavii Y §3.9, see below, p. 329, n.). A similar case is jit. asa- in Vend. 5.4, if taken, as Bth. thought, from @3fit.arata- in Y 53.9 (see on this word Burrow, Sariiga Bharati, 5). It is noteworthy that the usual YAv. ace. pl. tg accurs in Gathic only in Y 51.22, the stanza which is so closely allied to our prayer (see above, p. 155).
3191:bard. baosa-, 159 3q. bard. zus-, 220 n. barazis(ta)-, 183 barasa-, 170
```


## [2026-09-05T14:16:57.962Z] TOOL CALL #87: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg92.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/92.png && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg92_pahlavi.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/92_pahlavi_box.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/"
}
```


### [2026-09-05T14:16:58.033Z] TOOL RESULT

```
total 2312
drwxrwxr-x 2 sfmqrb sfmqrb   4096 Sep  5 10:16 .
drwxrwxr-x 9 sfmqrb sfmqrb   4096 Sep  5 01:38 ..
-rw-rw-r-- 1 sfmqrb sfmqrb 104864 Sep  4 19:03 101.png
-rw-rw-r-- 1 sfmqrb sfmqrb  86203 Sep  4 19:03 126.png
-rw-rw-r-- 1 sfmqrb sfmqrb 105296 Sep  4 19:03 311.png
-rw-rw-r-- 1 sfmqrb sfmqrb  96466 Sep  4 19:03 33.png
-rw-rw-r-- 1 sfmqrb sfmqrb  99093 Sep  4 19:03 39.png
-rw-rw-r-- 1 sfmqrb sfmqrb  54479 Sep  4 19:03 46.png
-rw-rw-r-- 1 sfmqrb sfmqrb  99295 Sep  4 19:03 54.png
-rw-rw-r-- 1 sfmqrb sfmqrb  57649 Sep  5 01:38 69.png
-rw-rw-r-- 1 sfmqrb sfmqrb  75801 Sep  5 01:35 71.png
-rw-rw-r-- 1 sfmqrb sfmqrb  49860 Sep  5 01:47 72.png
-rw-rw-r-- 1 sfmqrb sfmqrb  81180 Sep  5 01:53 73.png
-rw-rw-r-- 1 sfmqrb sfmqrb  56073 Sep  5 01:50 74.png
-rw-rw-r-- 1 sfmqrb sfmqrb  20612 Sep  5 02:01 75_greek_latin_arrow.png
-rw-rw-r-- 1 sfmqrb sfmqrb  75134 Sep  5 02:01 75.png
-rw-rw-r-- 1 sfmqrb sfmqrb  66505 Sep  5 01:56 76.png
-rw-rw-r-- 1 sfmqrb sfmqrb  65211 Sep  5 02:03 77.png
-rw-rw-r-- 1 sfmqrb sfmqrb  63822 Sep  5 02:07 78.png
-rw-rw-r-- 1 sfmqrb sfmqrb  59439 Sep  5 02:13 79.png
-rw-rw-r-- 1 sfmqrb sfmqrb  58953 Sep  5 02:13 80.png
-rw-rw-r-- 1 sfmqrb sfmqrb  99904 Sep  5 02:17 81.png
-rw-rw-r-- 1 sfmqrb sfmqrb  74477 Sep  5 02:22 82.png
-rw-rw-r-- 1 sfmqrb sfmqrb  67094 Sep  5 02:26 83.png
-rw-rw-r-- 1 sfmqrb sfmqrb  63329 Sep  5 02:31 85.png
-rw-rw-r-- 1 sfmqrb sfmqrb  31530 Sep  5 02:38 86.png
-rw-rw-r-- 1 sfmqrb sfmqrb  79874 Sep  5 09:55 87.png
-rw-rw-r-- 1 sfmqrb sfmqrb  98452 Sep  5 09:55 88.png
-rw-rw-r-- 1 sfmqrb sfmqrb  80984 Sep  5 09:56 89.png
-rw-rw-r-- 1 sfmqrb sfmqrb  77182 Sep  5 09:55 90.png
-rw-rw-r-- 1 sfmqrb sfmqrb  63799 Sep  5 09:56 91.png
-rw-rw-r-- 1 sfmqrb sfmqrb   3476 Sep  5 10:16 92_pahlavi_box.png
-rw-rw-r-- 1 sfmqrb sfmqrb  90918 Sep  5 10:16 92.png
-rw-rw-r-- 1 sfmqrb sfmqrb  78178 Sep  5 10:14 95.png
```


## [2026-09-05T14:26:22.705Z] TOOL CALL #88: Bash

```json
{
 "command": "ls /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/92*.png"
}
```


### [2026-09-05T14:26:22.791Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/92_pahlavi_box.png
/home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/92.png
```


## [2026-09-05T14:26:24.623Z] AGENT

Now I'll write the verification file.


## [2026-09-05T14:35:10.022Z] TOOL CALL #89: Bash

```json
{
 "command": "cat > /home/sfmqrb/git/rishe/data/verification/page-92.json <<'JSONEOF'\n{\n  \"pdf_page\": 92,\n  \"book_page\": 62,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-05\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Bhergh\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *bʰerǵʰ- 'to rise up, ascend; to be high, elevated' (LIV 78f.; Pokorny 140-141 'bheregh- hoch, erhaben', *bhereghos 'Berg')\",\n      \"note\": \"Root, language label and gloss are all correct. Pokorny I.140 heads the article 'bheregh- „hoch, erhaben“, bherghos „Berg“' and lists exactly the Iranian material Nourai puts in the chart (av. bərəzant- (npers. buland), bərəz- 'hoch' und 'Höhe, Berg' (= npers. burz), barəšnu-, barəzan-, barəzah-, npers. bālā 'Höhe' (*barz-)). One caveat that runs through the whole chart: Pokorny (and after him AHD/Watkins) recognises TWO homonymous roots — bhergh-¹ 'to hide, protect, care for, honour' (Pok. 145) and bhergh-² 'high' (Pok. 140). Nourai's PART 1 correctly cites POK:140, but three of its branches (nodes #8, #9, #14, and by inheritance #10) contain material that belongs to the OTHER root, or to no *bhergh- at all. Klein's article 'borough' (KLN:188), which Nourai cites on node #1, is a good summary of the same root. There is no 'PART 2' node on this page; the box says 'SEE OTHER PART(S) FOR MORE DERIVATIVES'.\",\n      \"note_fa\": \"ریشهٔ هندواروپایی آغازین *bʰerǵʰ- «برآمدن، بلند بودن» است؛ پوکورنی در صفحهٔ ۱۴۰ فرهنگ ریشه‌شناختی خود همین ریشه را با معنای «بلند، والا» و اسم *bʰerǵʰos «کوه» آورده و همان داده‌های ایرانی را که نورایی در نمودار نشانده است (اوستایی bərəzant-، فارسی نو بلند، برز، بالا) گواه گرفته. برچسب زبانی «هندواروپایی» و معنای «بلند» هر دو درست است و ادعای نورایی دربارهٔ خودِ ریشه پذیرفتنی است. تنها هشدار این است که پوکورنی دو ریشهٔ همنام دارد: *bʰergʰ- «پناه دادن، گرامی داشتن» در صفحهٔ ۱۴۵ و *bʰerǵʰ- «بلند» در صفحهٔ ۱۴۰؛ سه شاخه از این نمودار (گره‌های ۸، ۹ و ۱۴ و به تبع آن آرزو) در حقیقت به ریشهٔ نخست یا به ریشه‌ای دیگر تعلق دارند نه به ریشهٔ «بلند».\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/b%CA%B0er%C7%B5%CA%B0-\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"POK:140\", \"status\": \"supports\", \"note\": \"POK_01.txt leaf 150 (printed p.140): 'bheregh- „hoch, erhaben“, bherghos „Berg“, vielleicht Erweiterung von bher- „(tragen,) heben“ ...; bhrǵhú-s „hoch“'. The same page carries 'av. bərəzant- (npers. buland), f. bərəzaiti „hoch“, im Kompositum bərəzi- (: *bərəzra-), bərəz- „hoch“ und „Höhe, Berg“ (= npers. burz ...), der Nom. av. barš ... npers. bāl-ā „Höhe“ (*barz-), burz'.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.v. bhergh-²\", \"stance\": \"supports\", \"note\": \"AHD_watkins1985.txt line 338: 'bhergh-². High; with derivatives referring to hills and hill-forts. ... [Pok. bheregh- 140.]' — kept strictly apart from 'bhergh-¹. To hide, protect ... [Pok. bhergh- 145.]'\"},\n        {\"src\": \"IEC\", \"where\": \"Mann, s.v. bhr̥ghont-, bhr̥ghus\", \"stance\": \"supports\", \"note\": \"IEC.txt line 1794: 'bhr̥ghont- (bhr̥ghnt-, bhr̥ghont-) „high; height“. WP II, 172 ... Skt. bṛhát; Av. bərəzant; Oss. bärzond; Per. buland, baland'; line 1795 'bhr̥ghus, os „high; height“ ... Arm. bardzr „high“; Hitt. parkus'.\"},\n        {\"src\": \"SYN\", \"where\": \"Buck 1.22 'mountain, hill'\", \"stance\": \"supports\", \"note\": \"SYN.txt near line 992: 'OHG, NHG berg ... : Skt. bṛhant- „high, great“, Av. barəzant- „high“, barəzah- „height“'.\"},\n        {\"src\": \"WLD\", \"where\": \"Walde-Pokorny II 172 (cited via Pokorny and Mann)\", \"stance\": \"supports\", \"note\": \"Pokorny p.141 closes the article with 'WP. II 172 f.'; the Bd. 2 OCR on disk (WLD_Bd2_1927_dli_106624_djvu.txt) does not resolve the headword under any spelling I tried (grep 'bhere.h-' returns nothing — the Latin-script OCR of that volume is too damaged), so WLD is used at second hand through POK/IEC.\"},\n        {\"src\": \"CHEUNG\", \"where\": \"s.v. *barz¹ 'to make high', pp.12-13\", \"stance\": \"supports\", \"note\": \"CHEUNG.txt line 2044ff: '*barz¹ „to make high“ ... «PIE *bʰergʰ- „to become high“ = LIV: 78 f. | Pok.: 140 f.', with YAv. barəz-, barəzimanąm, barəzant-, OP baršnā, MP balay/buland, NP bālā/buland.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan\",\n          \"words\": \"berez 1, berezi, berezra, barš, bareš, berezant, barzman; barz-ahva\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"All seven 'high' words are genuine Young Avestan and all belong to *bʰerǵʰ-: barəz- / bərəz- adj. 'hoch, erhaben', also subst. 'Höhe; Berg' (Bartholomae AiW col. 950); bərəzi- as first member of compounds (bərəzi-gāθra-, bərəzi-sā(y)-, bərəzi-mita-, bərəzi-rāz-), beside which Pokorny reconstructs the stem *bərəzra- (= Nourai's 'berezra'); the nominative barš, on which Pokorny remarks 'der Nom. av. barš Subst. kann ar. -ar-, aber auch ar. -r̥- enthalten'; bərəzant- (fem. bərəzaitī-) 'hoch, hochgewachsen', the ancestor of MP/NP buland; and barəziman- adj. 'hoch' (Gpl. barəzimanąm), Nourai's 'barzman', which continues PIE *bʰérǵʰ-mn̥. Phonologically Avestan shows the full grade *bʰerǵʰ- > barəz-/bərəz- with the anaptyctic ə that Avestan regularly inserts between a consonant and a following r/z cluster; the zero grade *bʰr̥ǵʰ- gives barš-/baršnu-. 'barz-ahva' is the weak link: no such compound is quoted from the Avesta by Bartholomae. The form is however real one stage later — Parthian *bwrz-ʾxw /burz-axw/ 'high world, height', from burz 'high' + axw 'world' (Av. ahu- 'existence, world', whence Nourai's cross-reference to root 'An 1'), and it is this Parthian compound that Arabic borrowed as barzaḵ. So the node is right in substance but the language label for the last word should be Parthian, not Avestan.\",\n          \"derivation_fa\": \"همهٔ صورت‌های «بلند» در این جعبه اوستایی اصیل‌اند و همه از ریشهٔ *bʰerǵʰ- می‌آیند: barəz-/bərəz- هم صفت «بلند، والا» و هم اسم «بلندی، کوه» (بارتولومه، ستون ۹۵۰)؛ bərəzi- که تنها در ترکیب‌ها می‌آید (bərəzi-gāθra-، bərəzi-mita-) و پوکورنی در کنارش ستاک *bərəzra- را بازسازی می‌کند؛ نهادِ barš؛ bərəzant- «بلندبالا» که نیای «بلند» فارسی است؛ و barəziman- «بلند» که دنبالهٔ *bʰérǵʰ-mn̥ هندواروپایی است. در اوستایی درجهٔ کامل ریشه با واکهٔ میانجیِ ə به barəz-/bərəz- و درجهٔ صفر به barš- بدل شده است. تنها barz-ahva جای چون‌وچرا دارد: چنین ترکیبی در اوستا گواهی نشده، ولی در پارتی *burz-axw «جهانِ برین» (از burz «بلند» + axw «جهان») هست و همین صورت پارتی است که به عربی برزخ راه یافته. پس ادعای نورایی با احتیاط پذیرفتنی است و تنها برچسب زبانیِ واژهٔ آخر باید «پارتی» باشد نه «اوستایی».\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/b%CA%B0er%C7%B5%CA%B0-\",\n            \"https://en.wiktionary.org/wiki/%D8%A8%D8%B1%D8%B2%D8%AE\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"POK:140\", \"status\": \"supports\", \"note\": \"POK_01.txt leaf 150: 'av. bərəzant- (npers. buland), f. bərəzaitī „hoch“, im Kompositum bərəzi- (: *bərəzra-), bərəz- „hoch“ und „Höhe, Berg“ ... der Nom. av. barš Subst. kann ar. -ar-, aber auch ar. -r̥- enthalten, Bartholomae IF. 9, 261'. Covers berezant, berezi, berezra, barš and berez.\"},\n            {\"ref\": \"KLN:188\", \"status\": \"supports\", \"note\": \"KLN_1966.txt line 5381 (page marker '188' at line 5389), s.v. borough: 'These words prob. derive fr. I.-E. base *bhergh-, „high“, whence also Arm. berj „high place“ ... Hitt. parkush „high“, OI. bṛhánt-, Avestic bərəzant-, „high“'.\"},\n            {\"ref\": \"KNT:200\", \"status\": \"supports\", \"note\": \"KNT.txt s.v. 'bard- vb. „be high“: Av. barəz- „high“, barəzant- „lofty“, NPers. burz „high“, Skt. bṛhánt- „lofty“, OHG berg „mountain“, pIE *bhergh-' — Kent's lexicon page 200.\"},\n            {\"ref\": \"VDQ:36\", \"status\": \"not_checked\", \"note\": \"Badre'i's Persian translation of Jeffery is only on noorlib, whose viewer is JavaScript-rendered; the substance is identical to FVQ, which I did check (see node #2) and which in fact prefers a different etymology for barzakh.\"},\n            {\"ref\": \"MAG:181\", \"status\": \"not_checked\", \"note\": \"Widengren, 'Muhammad the Apostle of God', ch. VIII 'Iranian elements in the Kuranic vocabulary', is lending-only on archive.org and search-only on HathiTrust; not accessible. Its claim (Iranian *barz-axw behind Ar. barzakh) is however the view that modern reference works now follow.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"AiW col. 950-951 (BRT.txt lines 17015-17030)\", \"stance\": \"partial\", \"note\": \"'j. barəz- : bərəz- 1) Adj. „hoch, erhaben“ ... 2) „Höhe; Berg“ ... np. burz „hoch; Höhe“, bālā „Höhe“ ... Pü. (zu 1): buland, (zu 2): burz'; also 'j. barəzan- m. „Höhe“', 'j. barəzah- n. „Höhe, Berg“', 'g., j. barəziman- Adj. „hoch“'. Every word of the node is here EXCEPT barz-ahva, which Bartholomae does not have.\"},\n            {\"src\": \"CHEUNG\", \"where\": \"*barz¹, p.12\", \"stance\": \"supports\", \"note\": \"'*AVESTAN: YAv. barəz- „to enlarge“, (Gpl.) barəzimanam „heights“, YAv. barəzant- „rising high, high, loud“'.\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins, bhergh-²\", \"stance\": \"supports\", \"note\": \"Same root, but Watkins quotes only the Germanic/Italic side; the Avestan forms are implied by the Pokorny reference.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"borz «بُرز»; barzax «برزخ»; barzoy «برزوی ، بروزیه»; Farîborz «فریبرز»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"borz «بُرز» 'tall, tallness, stature' continues the zero grade *bʰr̥ǵʰ- through Old Iranian *br̥z- > MP burz (Book Pahlavi bwlc) > NP burz/borz; Bartholomae states the split explicitly: 'Idg. *bhereǵh- : *bhr̥ǵh-: Ersteres in np. bālā ..., letzteres in np. burz (, got. baurgs, air. brí, brig)'. Parthian bwrz /burz/ 'high, lofty' is the direct sister form. barzax «برزخ» reaches Persian by a round trip: Parthian *burz-axw 'high world, unsurmountable height' was borrowed into Arabic as barzaḵ (Qur'an 23:100, 25:53, 55:20) in the sense 'barrier, partition', and Islamic eschatology gave it the meaning 'the interval between death and resurrection'; Persian then re-borrowed the arabicised form برزخ. Nourai's gloss 'middle stage (above hell)' is the eschatological sense, and the '(above)' element preserves the original burz. barzoy «برزوی / بروزیه» is Burzōē, the Sasanian court physician of Ḵosrow I who brought the Pañcatantra from India (the Arabic form برزویه Burzūya is Ibn al-Muqaffaʿ's); the name is a hypocoristic of burz 'high, exalted' with the Middle Persian name-suffix -ōē, hence Nourai's rendering '„great“, a name'. Farîborz «فریبرز» is a Shahnameh hero (son of Kāvūs), from *friya-br̥z- 'of lovely stature' = fari- (Av. fri- 'to love, dear', hence Nourai's cross-reference to 'Sâwel' being a mis-target — the first element is fri-, not the sun word) + burz 'height'.\",\n          \"derivation_fa\": \"«بُرز» دنبالهٔ درجهٔ صفرِ ریشه (*bʰr̥ǵʰ-) است: از ایرانی باستان *br̥z- به فارسی میانهٔ burz (املای پهلوی bwlc) و از آن به فارسی نو «برز»؛ بارتولومه همین دوگانگی را روشن می‌گوید که «بالا» از درجهٔ کامل و «برز» از درجهٔ صفر ریشه است. «برزخ» راه رفت‌وبرگشتی پیموده: ترکیب پارتی *burz-axw «جهانِ برین» به عربی وام رفته و به صورت «برزخ» در قرآن (مؤمنون ۱۰۰، فرقان ۵۳، الرحمن ۲۰) به معنی «حدّ فاصل» به کار رفته و سپس در کلام اسلامی معنای «عالم میان مرگ و رستاخیز» گرفته است و از همان‌جا معرّب‌شده به فارسی بازگشته؛ پس «برزخ» وام‌واژه‌ای است با اصل ایرانی. «برزوی/بروزیه» نام پزشک دربار خسرو انوشیروان است که کلیله و دمنه را از هند آورد، و از burz «بلند، والا» با پسوند نام‌سازِ فارسی میانهٔ -ōē ساخته شده. «فریبرز» نیز از *friya-br̥z- «دارای بالای دلپذیر» است. ادعای نورایی در این گره درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%A8%D8%B1%D8%B2\",\n            \"https://en.wiktionary.org/wiki/%D8%A8%D8%B1%D8%B2%D8%AE\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"KLN:148\", \"status\": \"partial\", \"note\": \"KLN_1966.txt: printed p.148 (page marker at line 4444) is the 'barbican' page; Klein there says the first element of Pers. bāla-khāna 'is rel. to Avestic bərəzant-, OI. bṛhant- „high“; see borough' — so it supports the root, but it is not a page about borz/barzakh.\"},\n            {\"ref\": \"BQT:254\", \"status\": \"supports\", \"note\": \"BQT_v1_pages.txt leaf 474 (printed p.254 by the volume's leaf−220 offset; leaf 476 carries the continuation note 'بقیهٔ صفحهٔ ۲۵۵'): headword «برز» — 'بمعنی زیبایی و معشوقی و بلندی بالای مردم و تنهٔ درخت نیز آمده است - و مطلق بلندی را هم گفته‌اند - و بضم اول ... قد و قامت آدمی ... و بلندی بالای مردم و چارپا را نیز گویند'. Exactly Nourai's 'tall, tallness'.\"},\n            {\"ref\": \"BQT:256\", \"status\": \"not_found\", \"note\": \"BQT_v1_pages.txt leaf 476 (printed p.256) is the برسم / برسیانا page (the Zoroastrian barsom twigs); nothing on borz, barzakh or the two names.\"},\n            {\"ref\": \"BQT:300\", \"status\": \"partial\", \"note\": \"leaf 520 (printed p.300) carries «بلند - بفتح اول بروزن کمند؛ معروف است که نقیض پست باشد» with a Mo'in footnote marker — that is the reference for node #3, not for this node.\"},\n            {\"ref\": \"FSF:78\", \"status\": \"supports\", \"note\": \"FSF_pages.txt leaf 100 (running head «برز»): 'برز (با پیش اول) ۱ بلند: به‌بالا شود چو یکی سرو برز / به‌گردن برآرد ز پولاد گرز' — Noushin glosses the Shahnameh word برز as 'بلند'.\"},\n            {\"ref\": \"VDQ:36\", \"status\": \"not_checked\", \"note\": \"Persian translation of Jeffery, only on noorlib's JavaScript viewer; substance checked through FVQ instead (see consulted).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"HRN\", \"where\": \"no. 198, p. 51\", \"stance\": \"supports\", \"note\": \"HRN.txt line 2134: '198. burz „Höhe, hoch“ | burz, bulend. ap. vergl. Bardiya-; aw. bərəz-, barəz- etc. „Höhe, hoch“; phlv. burz, burzak, burzišn, burzīdan, buland; ai. bṛhánt-; arm. barjr'.\"},\n            {\"src\": \"PHD\", \"where\": \"MacKenzie p.19 and English index\", \"stance\": \"supports\", \"note\": \"PHD.txt: index entry 'high borz, buland'; 'burzidan, burz- [bwlc-ytn'] praise, honour'; 'Burz [bwlc] the god of agriculture', 'Harborz [hlbwlc | N Alburz]'.\"},\n            {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II, glossary s.v. burz\", \"stance\": \"supports\", \"note\": \"NYB_vol2_glossary.txt line 1047: 'burz [bwlc'] high ... MPrth bwrz ... cf. Harburz'.\"},\n            {\"src\": \"FVQ\", \"where\": \"Jeffery p.77 s.v. برزخ\", \"stance\": \"contradicts\", \"note\": \"FVQ.txt lines 5097-5120: 'That the word is not Arabic seems clear from the Lexicons ... Vollers, ZDMG, l, 646, makes the much more plausible suggestion that برزخ is a by-form of فرسخ parasang, from the Phlv. frasang' — Jeffery derives barzakh from farsang, NOT from burz-axw. Modern reference works (Wiktionary, following Widengren/Nyberg) have gone back to the *burz-axw explanation that Nourai gives.\"},\n            {\"src\": \"MON\", \"where\": \"Farhang-e Farsi, s.v. برز\", \"stance\": \"supports\", \"note\": \"MON_part1.txt/Adena reprint has برز in the 'قد و قامت، بالا' sense; Dehkhoda s.v. برز quotes Borhan for the same.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Persian\",\n          \"words\": \"boland «بلند»; bâlâ «بالا»; bâlâ-xâneh «بالاخانه»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"The two Persian words split the root's ablaut, exactly as Bartholomae set it out: bālā «بالا» 'up, above, height' goes back to the FULL grade — Proto-Iranian *bārźah- (Av. barəzah- n. 'Höhe, Berg') plus an obscure suffix *-ā, with the Western Iranian development *rź > *rd > l that also gives sāl 'year' from *sard-; hence MP bālā/bālāy/bālist beside bašn, and NP بالا. boland «بلند» goes back to the participle *bʰerǵʰ-ont- > Proto-Iranian *br̥jáns / Av. bərəzant- 'high', through an Old Persian *br̥dāh (again *rj > rd) to MP buland (Book Pahlavi bwlnd, Manichaean bwlnd) > NP بلند; Bartholomae records 'Pü. (zu 1): buland' as the Pahlavi rendering of Av. bərəz-. bālā-xāneh «بالاخانه» is a transparent New Persian compound bālā 'upper' + xāna 'house' = 'upper room, room built over another', already recorded in Borhan (برباد 'بالاخانه و حجره باشد که بربالای حجرهٔ دیگر سازند'); its cross-reference 'Gwhen 1' is for the second element xāna.\",\n          \"derivation_fa\": \"دو واژهٔ این جعبه دو درجهٔ ابلاوتِ ریشه‌اند. «بالا» از درجهٔ کامل می‌آید: ایرانی باستان *bārźah- (اوستایی barəzah- «بلندی، کوه») با پسوندی نامعلوم *-ā؛ در ایرانی غربی خوشهٔ *rź نخست به *rd و سپس به l بدل شده (همان دگرگونی که *sard- را به «سال» رسانده)، پس فارسی میانه bālā/bālāy/bālist و فارسی نو «بالا». «بلند» از صفت فاعلی *bʰerǵʰ-ont- می‌آید: اوستایی bərəzant-، ایرانی باستان *br̥jáns، پارسی باستان *br̥dāh، فارسی میانه buland (املای پهلوی bwlnd) و سرانجام «بلند»؛ بارتولومه خودِ ترجمهٔ پهلویِ اوستایی bərəz- را buland ثبت کرده است. «بالاخانه» ترکیبی سرراست از «بالا» + «خانه» است و برهان قاطع نیز آن را «حجره‌ای که بر بالای حجرهٔ دیگر سازند» تعریف می‌کند. ادعای نورایی در این گره درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%A8%D8%A7%D9%84%D8%A7\",\n            \"https://en.wiktionary.org/wiki/%D8%A8%D9%84%D9%86%D8%AF\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"KLN:148\", \"status\": \"supports\", \"note\": \"KLN_1966.txt line 4441 (printed p.147-148), s.v. barbican: 'Pers. bāla-khāna, „upper chamber, balcony on the top of a house“, lit. „a high house“, fr. bala, „high“, and khāna, „house“. The first element is rel. to Avestic bərəzant-, OI. bṛhant-, „high“; see borough.' — precisely Nourai's bālā and bālā-xāneh.\"},\n            {\"ref\": \"BQT:300\", \"status\": \"supports\", \"note\": \"BQT_v1_pages.txt leaf 520 (printed p.300): «بلند - بفتح اول بروزن کمند؛ معروف است که نقیض پست باشد» with Mo'in's footnote marker. The بلند headword is on the cited page.\"},\n            {\"ref\": \"BQT:254\", \"status\": \"partial\", \"note\": \"leaf 474 (printed p.254) is the برز page, which does gloss برز as 'مطلق بلندی', but the بالا headword itself falls earlier in the volume (the با- section) and is not on any of the three cited pages.\"},\n            {\"ref\": \"BQT:256\", \"status\": \"not_found\", \"note\": \"leaf 476 (printed p.256) is the برسم page; nothing on boland/bālā.\"},\n            {\"ref\": \"FSF:78\", \"status\": \"partial\", \"note\": \"FSF_pages.txt leaf 100 (running head «برز») glosses برز as 'بلند' and cites 'دوتا کرد بسیار بالای برز' — so the page attests both بلند and بالا as Shahnameh vocabulary, though neither is its headword.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"HRN\", \"where\": \"no. 171, p. 39\", \"stance\": \"supports\", \"note\": \"HRN.txt line 1872: '171. bālā „hoch“. aw. barəzah- „Höhe“; phlv. bālā, bālāg, bal(i)st (aw. barəzišta-)'. And no. 198 for buland (see node #2).\"},\n            {\"src\": \"PHD\", \"where\": \"MacKenzie pp.16, 19\", \"stance\": \"supports\", \"note\": \"PHD.txt line 243: 'balay [b'l'd | N bālā] height, stature'; line 292: 'buland [bwlnd | = M, N ~] high'.\"},\n            {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II glossary\", \"stance\": \"supports\", \"note\": \"NYB_vol2_glossary.txt line 1036: 'buland [bwlnd] high ... V. also bālāt, bālast, burz'.\"},\n            {\"src\": \"CHEUNG\", \"where\": \"*barz¹, p.12-13\", \"stance\": \"supports\", \"note\": \"'*MIDDLE PERSIAN: ... MMP b'l'y, BMP b'l'd /balay/ „height“, MMP bwlnd, BMP bwlnd /buland/ „high“ ... *NWIR: NP bala „height“, NP buland „high, tall“'.\"},\n            {\"src\": \"HUB\", \"where\": \"Persische Studien no. 171\", \"stance\": \"partial\", \"note\": \"HUB.txt line 744: '171. Bal. balad „Höhe“ scheint, wie auch Geiger, Laut-...' — Hübschmann discusses only the Balochi cognate of Horn's no. 171, without disputing the derivation.\"},\n            {\"src\": \"BQT\", \"where\": \"vol.1 leaf 468 s.v. برباد\", \"stance\": \"supports\", \"note\": \"'برباد - با بای ابجد بروزن سرداب، بمعنی بالاخانه و حجره باشد که بربالای حجرهٔ دیگر سازند' — the compound bālā-xāna in Borhan's own words.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Italian\",\n          \"words\": \"barbacane; balcone\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"The node bundles two words with very different standing. barbacane 'barbican, outer fortification, watch-post on a castle wall' is plausibly oriental: Lokotsch no. 197 derives it, with Prov./Fr./Cat./Sp./Pg. barbacana, from Pers. bālā-ḵāna 'ein oberes Zimmer, hervorstehender Teil des Hauses, Erker, Balkon', and Klein s.v. barbican agrees ('prob. derives ult. fr. Pers. bāla-khāna'). Etymonline, however, calls it 'a general Romanic word, said to be ultimately from Arabic or Persian (compare bab-khanah „gate-house“)' and reports Watkins's rival Old Iranian *pari-varaka- 'protective'; Lokotsch himself notes that Löbel called the bālā-ḵāna derivation an 'etimologia indoiosa'. balcone 'balcony' is a different matter: the modern consensus is Germanic. Old Italian balco 'scaffold, beam' is a Langobardic/Frankish loan from Proto-Germanic *balkô 'beam' (cf. OHG balcho, German Balken), enlarged by the Italian augmentative -one; AHD files BALCONY under bhelg- 'a plank, beam' (Pok. 5. bhel- 123), Klein under balk 'beam', Etymonline and Wiktionary the same. Lokotsch's insistence that 'Annahme eines ahd. palco „Balken“ als Grundwort abzulehnen' ist has not been followed. Nourai's own NOTE ('AHD derives these words from other roots') is therefore correct for balcone, and the node as a whole must be marked disputed.\",\n          \"derivation_fa\": \"این جعبه دو واژه را کنار هم نشانده که سرنوشتشان یکی نیست. barbacane «برج و بارویِ بیرونی» را لوکوچ (شمارهٔ ۱۹۷) و کلاین از فارسی «بالاخانه» می‌گیرند و این ریشه‌شناسی پذیرفتنی ولی قطعی نیست؛ اتیمانلاین آن را «واژه‌ای عام رومیایی با اصل احتمالی عربی یا فارسی» می‌خواند و ریشهٔ رقیبِ ایرانی باستان *pari-varaka- «پوشاننده» را نیز می‌آورد. اما balcone «بالکن» چنین نیست: دیدگاه امروزی آن را ژرمانی می‌داند — ایتالیایی کهن balco «داربست، تیر» وام‌واژه‌ای لومباردی/فرانکی از ژرمانی آغازین *balkô «تیر» است (هم‌ریشه با Balken آلمانی) که با پسوند بزرگ‌ساز ایتالیاییِ -one بسط یافته؛ فرهنگ AHD واژهٔ balcony را زیر ریشهٔ bhelg- «تیر، تخته» می‌آورد و کلاین و ویکی‌واژه نیز همین را می‌گویند. پس یادداشت خود نورایی («AHD این واژه‌ها را از ریشه‌های دیگر می‌گیرد») درست است و پژوهش امروزی این حلقه را رد می‌کند.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/balcony\",\n            \"https://www.etymonline.com/word/barbican\",\n            \"https://en.wiktionary.org/wiki/%D8%A8%D8%A7%D9%84%DA%A9%D9%86\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"LKT:17\", \"status\": \"supports\", \"note\": \"LKT.txt leaf 44 (printed p.17), entry 197: 'Pers. bālāḫānā [Aus pers. bālā „hoch“ Horn NpEt S.39 Nr.171 und pers. ḫānā „Haus“ ebenda S.103 Nr.465; also eigentlich „Hochhaus“] „ein oberes Zimmer, hervorstehender Teil des Hauses, Erker, Balkon“; hieraus ... it. barbacane ..., frz. barbacane ...; ... it. balcone, frz. balcon, rum. balcon, sp. balcón, pg. balcão; dtsch. Balkon, engl. balcony ... und Annahme eines ahd. palco „Balken“ als Grundwort abzulehnen'. Lokotsch says exactly what Nourai's arrow says — but he is the minority view.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"Klein 1966 p.141-142 s.v. balcony; p.147-148 s.v. barbican\", \"stance\": \"partial\", \"note\": \"Klein SPLITS them: 'balcony, n. — It. balcone, formed with the augmentative suff. -one fr. balco, „scaffold“, which is borrowed fr. OHG. balcho, „beam“'; but 'barbican ... prob. derives ult. fr. Pers. bāla-khāna'. Supports barbacane, contradicts balcone.\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. bhelg-\", \"stance\": \"contradicts\", \"note\": \"AHD_watkins1985.txt line 330: 'bhelg-. Also bhelk-. A plank, beam. ... 2. Germanic *balkōn- in: ... b. Old Italian balcone, scaffold: BALCONY. [Pok. 5. bhel- 123.]' The index line confirms 'BALCONY bhelg-'. AHD has no BARBICAN entry at all.\"},\n            {\"src\": \"PHN\", \"where\": \"Pihan p.55 s.v. BALCON\", \"stance\": \"supports\", \"note\": \"See node #5 — Pihan derives the whole Romance family from bālā-ḵāna.\"},\n            {\"src\": \"SKT\", \"where\": \"Skeat, s.v. balcony\", \"stance\": \"silent\", \"note\": \"SKT.txt does not resolve a barbican entry under any spelling I tried; the balcony entry follows the Germanic 'balk' account like Klein.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"French\",\n          \"words\": \"balcon\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"French balcon is a 16th-century borrowing of Italian balcone, and the Italian→French step of the chart is beyond doubt. What is disputed is the source Nourai gives the Italian word. Pihan (whom Nourai cites) states the oriental derivation flatly: 'BALCON, s. m. composé, (p.) بالاخانه [bālā-ḵāneh], composé de l'adjectif بالا [bālā] élevé, et du substantif خانه [ḵāneh] maison ... De là viennent très-probablement, malgré l'altération d'orthographe, l'anglais balcony, le portugais balcão, l'italien balcone, l'espagnol et le français balcon'. Against this, the accepted account since Diez and Meyer-Lübke is Medieval Latin balcō < Frankish *balkō < Proto-Germanic *balkô 'beam', whence It. balcone and thence Fr. balcon; the semantics ('scaffold, beam platform' > 'projecting platform') are straightforward and the Romance forms show no trace of the -ḫ- of ḵāna.\",\n          \"derivation_fa\": \"فرانسویِ balcon وام‌واژه‌ای است از ایتالیاییِ balcone در سدهٔ شانزدهم و این حلقهٔ نمودار تردیدناپذیر است؛ آنچه محل مناقشه است سرچشمهٔ خودِ واژهٔ ایتالیایی است. پیهان (همان مأخذی که نورایی آورده) در صفحهٔ ۵۵ می‌نویسد که balcon از فارسی «بالاخانه» (بالا + خانه) است و انگلیسی balcony و پرتغالی balcão و ایتالیایی balcone نیز از همان‌جا آمده‌اند. اما تبیین پذیرفتهٔ امروزی از دیتس و مایر-لوبکه به این سو چنین است: لاتین میانه balcō از فرانکی *balkō و آن از ژرمانی آغازین *balkô «تیر»؛ تحول معنایی «داربست/تیرِ بیرون‌زده» به «ایوانک» سرراست است و صورت‌های رومیایی هیچ نشانی از خِ «خانه» ندارند. پژوهش امروزی این حلقه را رد می‌کند.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/balcony\",\n            \"https://en.wiktionary.org/wiki/%D8%A8%D8%A7%D9%84%DA%A9%D9%86\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"PHN:55\", \"status\": \"supports\", \"note\": \"PHN.txt leaf 87 = printed p.55, running head 'BAL 55': 'BALCON, s. m. composé, (p.) بالاخانه [bâlâkhâneh], composé de l'adjectif بالا [bâlâ] élevé, et du substantif خانه [khâneh] maison ... De là viennent très-probablement, malgré l'altération d'orthographe, l'anglais balcony, le portugais balcão, l'italien balcone, l'espagnol et le français balcon.' Nourai's citation is accurate.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"LKT\", \"where\": \"Lokotsch p.17 no.197\", \"stance\": \"supports\", \"note\": \"'... it. balcone, frz. balcon, rum. balcon, sp. balcón, pg. balcão; dtsch. Balkon, engl. balcony' all from Pers. bālāḫānā.\"},\n            {\"src\": \"DEV\", \"where\": \"Devic, Dictionnaire des mots français d'origine orientale\", \"stance\": \"silent\", \"note\": \"DEV.txt has no balcon entry — Devic, who is generally more cautious than Pihan, did not admit the word into his list of French orientalisms.\"},\n            {\"src\": \"KLN\", \"where\": \"Klein s.v. balcony\", \"stance\": \"contradicts\", \"note\": \"Traces the French/English word back through It. balcone to OHG balcho 'beam'.\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"Persian\",\n          \"words\": \"bâlkon «بالکن»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"The edge drawn here — French balcon → Persian بالکن — is certainly right. بالکن is a 20th-century Europeanism in Persian, taken from French balcon (not from English), with the French nasal-less final syllable rendered -kon (Iranian bâlkon, Dari bâlkun, Tajik balkon); Mo'in tags it '[فر.]' = French. Modern Persian keeps the inherited native compound بالاخانه alongside it, and in Dari the two are used side by side, which is what makes this look like a round trip. It is only a round trip, however, if the Italian word really came from bālā-ḵāna — and that step (node #4) is rejected by modern scholarship, which takes Italian balcone from Germanic *balkô. So the borrowing is confirmed; the 'homecoming' story is not.\",\n          \"derivation_fa\": \"خودِ این حلقه — فرانسوی balcon ← فارسی «بالکن» — بی‌گمان درست است. «بالکن» وام‌واژه‌ای اروپایی در فارسی سدهٔ چهاردهم خورشیدی است و از فرانسوی گرفته شده نه از انگلیسی؛ معین در فرهنگ فارسی آن را با نشانِ «[فر.]» می‌آورد و چنین معنی می‌کند: «ایوان، مهتابی؛ طبقهٔ بالای تئاتر یا سینما؛ ایوان کوچک جلوی کاشانه». فارسی امروز واژهٔ بومیِ «بالاخانه» را نیز در کنار آن نگاه داشته و در فارسی افغانستان هر دو به کار می‌رود؛ همین است که ظاهرِ «رفت‌وبرگشت» به آن داده است. اما این رفت‌وبرگشت تنها در صورتی واقعی است که balcone ایتالیایی راستی از «بالاخانه» آمده باشد، و پژوهش امروزی همان حلقه (گرهٔ ۴) را رد می‌کند. پس وام‌گیری تأیید می‌شود ولی داستان بازگشت نه.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%A8%D8%A7%D9%84%DA%A9%D9%86\",\n            \"https://abadis.ir/fatofa/%D8%A8%D8%A7%D9%84%DA%A9%D9%86/\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"MON:467\", \"status\": \"supports\", \"note\": \"Mo'in's entry, read via abadis (فرهنگ معین section): 'بالکن (کُ) [فر.] (اِ.) ۱ - ایوان. مهتابی. ۲ - طبقهٔ بالای تئاتر یا سینما. ۳ - ایوان کوچک جلوی کاشانه، ایوانک'. The tag [فر.] = فرانسه is exactly Nourai's arrow. The 2-vol Adena reprint on disk (MON_part1.txt line 20927) has the same gloss without the origin tag; the printed 6-vol page number 467 could not be checked directly (vajehyab/abadis give no pagination).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"Farhang-e Farsi (2-vol reprint), MON_part1.txt line 20927\", \"stance\": \"supports\", \"note\": \"'بالکن: (.) ایوان کوچکی که در جلوی ساختمان سازند؛ مهتابی. (نم.) طبقهٔ فوقانی تماشاخانه یا سینما ...'\"},\n            {\"src\": \"PHN\", \"where\": \"Pihan p.55\", \"stance\": \"partial\", \"note\": \"Pihan documents the French word but has nothing on its re-borrowing into Persian.\"},\n            {\"src\": \"LKT\", \"where\": \"Lokotsch p.17 no.197\", \"stance\": \"partial\", \"note\": \"Lists the European descendants (dtsch. Balkon, russ./bulg./serb./poln. balkon) but not the modern Persian re-loan.\"}\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"English\",\n          \"words\": \"barbican, balcony\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"English barbican (ME barbecan, mid-13c.) is from Old French barbacane and shares node #4's fate: Klein, on the very page Nourai cites, calls it 'prob. ... ult. fr. Pers. bāla-khāna', while Etymonline reports it as 'a general Romanic word, said to be ultimately from Arabic or Persian (compare bab-khanah „gate-house“)' and gives Watkins's Old Iranian *pari-varaka- as the alternative — so 'plausible' at best. English balcony (1610s, stressed balcóny until c.1825) is from Italian balcone, and its Germanic origin is not seriously questioned today: AHD's index reads 'BALCONY bhelg-', Klein sends it to balk 'beam', Etymonline to 'a Germanic source (perhaps Langobardic *balko- „beam“), from Proto-Germanic *balkon-'. Since balcony is the worse of the two, the node is disputed.\",\n          \"derivation_fa\": \"انگلیسی barbican (از سدهٔ سیزدهم میلادی، از فرانسویِ کهن barbacane) سرنوشت گرهٔ ۴ را دارد: کلاین در همان صفحه‌ای که نورایی ارجاع داده آن را «به احتمال زیاد در نهایت از فارسیِ بالاخانه» می‌داند، ولی اتیمانلاین آن را «واژه‌ای عام رومیایی با اصل احتمالی عربی یا فارسی (سنجیده شود با باب‌خانه)» می‌خواند و ریشهٔ رقیبِ واتکینز، ایرانی باستان *pari-varaka-، را نیز می‌آورد؛ پس این واژه در بهترین حالت «با احتیاط پذیرفتنی» است. اما balcony انگلیسی (از ۱۶۱۰ میلادی، وام از ایتالیاییِ balcone) اصل ژرمانی‌اش امروز جای چون‌وچرا ندارد: نمایهٔ AHD می‌نویسد «BALCONY < bhelg-»، کلاین آن را به balk «تیر» بازمی‌گرداند و اتیمانلاین به ژرمانی آغازین *balkon-. چون واژهٔ دوم بدترین حالت را دارد، حکم این گره «مردود» است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/balcony\",\n            \"https://www.etymonline.com/word/barbican\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"KLN:148\", \"status\": \"partial\", \"note\": \"KLN_1966.txt line 4441 (printed p.147-148): 'barbican, n., outer defense of a city or castle. — ME. barbecan, fr. OF. barbacan, barbican (F. barbacane), which prob. derives ult. fr. Pers. bāla-khāna, „upper chamber, balcony on the top of a house“, lit. „a high house“ ...'. Klein supports BARBICAN on the cited page — but his balcony article (p.141-142) contradicts the other half of the node.\"},\n            {\"ref\": \"LKT:17\", \"status\": \"supports\", \"note\": \"Lokotsch entry 197 lists 'engl. balcony' among the descendants of Pers. bālāḫānā and explicitly rejects the OHG palco 'Balken' etymology; this is the minority position.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985, index and s.v. bhelg-\", \"stance\": \"contradicts\", \"note\": \"'BALCONY bhelg-' in the English index; 'bhelg-. Also bhelk-. A plank, beam. ... Old Italian balcone, scaffold: BALCONY.' No BARBICAN entry exists in Watkins.\"},\n            {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etym. Dict.\", \"stance\": \"contradicts\", \"note\": \"SKT.txt gives balcony the Italian-from-Germanic account, as Klein does; no independent oriental derivation.\"},\n            {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls New Standard\", \"stance\": \"silent\", \"note\": \"FSD_vol1.txt did not return a usable barbican/balcony article under the spellings I tried (the OCR of the etymology brackets is heavily damaged in this volume).\"}\n          ]\n        },\n        {\n          \"id\": 8,\n          \"lang\": \"Avestan\",\n          \"words\": \"bereg, â-bereg : high, desirable\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"The Avestan word is real but it belongs to a DIFFERENT root and does not mean 'high'. Bartholomae has two entries: 'j. barəg- V. „willkommen heissen“' (to welcome) and 'j. bərəg- f. „religiöser Brauch, religiöse Form, Ritus“', used only with the genitive of aṣ̌a- or daēnā-. Neither is glossed 'high, desirable'; Nourai's gloss is back-formed from the Middle Iranian 'desire' words below it. Etymologically Av. barəg-/bərəg- goes with the HOMONYM of this chart's root: Cheung files it as *barj with the note '«PIE *bʰergʰ- „to honour, be attentive to (a guest)“ = LIV: 79 f. | Pok.: 145' — i.e. Pokorny p.145, the 'bergen/achten' root (OCS ne-brěšti 'to neglect', Russ. berečʹ 'to take care of', Goth. bairgan 'to protect', Eng. borrow), NOT Pokorny p.140 which heads this chart. Cheung adds explicitly: 'There are no particular reasons to consider possible convergence or contamination with the root *barz „to enlarge, make high“, which does not appear to have acquired a more metaphorical connotation (other than „loud“ of sound).' Gharib (Nourai's SOD:1) does cite 'Av. bərəg-' as the cognate of the Sogdian 'desire' word, so Nourai copied his source faithfully — but Gharib is citing it as a *bʰergʰ-'honour' word, not as a 'high' word, and Nourai has hung it on the wrong root box.\",\n          \"derivation_fa\": \"واژهٔ اوستایی هست، ولی نه به این معنا و نه از این ریشه. بارتولومه دو مدخل دارد: barəg- «خوشامد گفتن» و bərəg- (مؤنث) «آیین دینی، رسم، مناسک» که تنها با اضافهٔ aṣ̌a- یا daēnā- به کار می‌رود؛ هیچ‌کدام «بلند، خواستنی» معنی نمی‌دهد و این معنا را نورایی از واژه‌های «آرزو»یِ زیر آن به عقب برده است. از نظر ریشه‌شناسی، اوستایی barəg-/bərəg- به ریشهٔ همنامِ این نمودار تعلق دارد: چونگ آن را زیر *barj می‌آورد و می‌نویسد که از هندواروپایی *bʰergʰ- «گرامی داشتن، پذیرایی کردن» است (پوکورنی صفحهٔ ۱۴۵، هم‌ریشه با گوتیِ bairgan «پاسداشتن» و انگلیسیِ borrow) نه از *bʰerǵʰ- «بلند» (پوکورنی صفحهٔ ۱۴۰) که سرلوحهٔ همین نمودار است؛ و صریح می‌افزاید که دلیلی برای آمیختن آن با ریشهٔ *barz «بلند کردن» در دست نیست. قریب (همان مأخذ SOD:1) نیز «Av. bərəg-» را همچون هم‌ریشهٔ واژهٔ سغدیِ «آرزو» آورده و نورایی امانت‌دارانه از او نقل کرده، اما آن را زیر ریشهٔ نادرست نشانده است. پژوهش امروزی این حلقه را رد می‌کند.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%A2%D8%B1%D8%B2%D9%88\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"SOD:1\", \"status\": \"supports\", \"note\": \"SOD.txt entry 18 on printed p.1 (entries 16-19 sit on that page): 'ʾʾβrxsy (M) apraxse ©<*ā-braxsaka; Av. bərəg-, Parth. awarzog; Pahl. awarzog; Khot. aursa ... desire, lust. Hen. Tales. 487 n 2; GMS 5'. Gharib does cite Av. bərəg- exactly as Nourai does — so the citation is faithful; the root assignment is Nourai's own.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"AiW cols. 953, 957 (BRT.txt lines 16956, 17138)\", \"stance\": \"contradicts\", \"note\": \"'j. barəg- V. „willkommen heissen“. Praes. barəjaya-. — PPfP. bərəxta-' and 'j. bərəg- f. „religiöser Brauch, religiöse Form, Ritus“, nur in Verbindung mit GS. aṣ̌ahe oder daēnayā'. Bartholomae's glosses are 'welcome' and 'rite', never 'high, desirable'.\"},\n            {\"src\": \"CHEUNG\", \"where\": \"s.v. *barj, p.11-12\", \"stance\": \"contradicts\", \"note\": \"'«PIE *bʰergʰ- „to honour, be attentive to (a guest)“ = LIV: 79 f. | Pok.: 145 ... IE COGNATES: OCS ne-brěšti „to neglect“, Russ. berečʹ ... Goth. bairgan „to protect, shelter“ ... Engl. to borrow'; and 'There are no particular reasons to consider possible convergence or contamination with the root *barz „to enlarge, make high“'.\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985, bhergh-¹ vs bhergh-²\", \"stance\": \"contradicts\", \"note\": \"Watkins keeps the two roots apart: 'bhergh-¹. To hide, protect ... [Pok. bhergh- 145.]' against 'bhergh-². High ... [Pok. bheregh- 140.]'. This node's material belongs with the first, the chart's root box with the second.\"},\n            {\"src\": \"POK\", \"where\": \"Pokorny p.145 vs p.140\", \"stance\": \"contradicts\", \"note\": \"Pokorny p.141 ends the 'hoch' article and refers forward: 'Dieser betrachtet *bhergho „berge“ ... als retrograde Ableitung zu *bhergh- „Berg“ (Gl. 22, 113); s. darüber S. 145' — i.e. the 'protect/honour' root is a separate article at p.145.\"}\n          ]\n        },\n        {\n          \"id\": 9,\n          \"lang\": \"Pahlavi\",\n          \"words\": \"âwarzog, ârzôk : wish, hope\",\n          \"verdict\": \"transcription_suspect\",\n          \"error_in\": \"extraction\",\n          \"book_prints\": \"âwarzog, ârzôk\",\n          \"correct_form\": \"âwarzog, ârzôk\",\n          \"derivation\": \"EXTRACTION ERROR: the printed page (rendered at 500 dpi from the PDF, copy at data/verification/sources/refs/ocr/BOOK/92.png and the cropped box at 92_pahlavi_box.png) clearly reads 'âwarzog, ârzôk : wish, hope'; the JSON has 'âzôk', dropping the r. Both printed forms are genuine and well attested: Parthian/Manichaean Middle Persian ʾ(ʾ)wrzwg /āwarzōg/ 'desire, lust' and Book Pahlavi ʾlcwk /ārzōg, ārzōk/, the immediate ancestor of NP آرزو. Mo'in himself gives the Pahlavi antecedent as ārzōk, which is why Nourai's spelling has the -k. The derivation drawn (from node #8's Av. bərəg-) is the Henning 1945 explanation that Gharib repeats: *ā-barj- 'to like to possess, to desire'. It is contested — Cheung rejects it ('Semantically ... the Sogd. (inchoative) formations are perhaps more likely to contain the root *braHz ... Equally semantically difficult to reconcile with „to praise, honour“ are the Pth. and Pers. „desire“ formations') and files āwarzōg/ārzōg under *rauǰ, *rauč '(to) please, desire' instead. Either way the word does not belong under Pokorny 140 'high'.\",\n          \"derivation_fa\": \"خطای خوانش اسکن: تصویر چاپیِ صفحه (رندر ۵۰۰ نقطه‌درانچ، در data/verification/sources/refs/ocr/BOOK/92.png و برش جعبه در 92_pahlavi_box.png) به‌روشنی «âwarzog, ârzôk» دارد، حال آنکه در JSON «âzôk» ثبت شده و حرف r افتاده است. هر دو صورت چاپی اصیل‌اند: پارتی و فارسی میانهٔ مانوی ʾ(ʾ)wrzwg /āwarzōg/ «آرزو، شهوت» و پهلویِ کتابی ʾlcwk /ārzōg، ārzōk/ که نیای بی‌واسطهٔ «آرزو»ی فارسی است؛ معین نیز صورت پهلوی را ārzōk می‌آورد و همین است که املای نورایی را با k توضیح می‌دهد. اما پیوندی که نمودار می‌کشد (از اوستایی bərəg- گرهٔ ۸) همان تبیین هنینگ ۱۹۴۵ است که قریب تکرار کرده و چونگ آن را رد می‌کند و به جای آن ریشهٔ *rauǰ/*rauč «خوش آمدن، خواستن» را پیشنهاد می‌دهد. در هر دو حال این واژه زیر ریشهٔ «بلند» (پوکورنی ۱۴۰) جای ندارد.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%A2%D8%B1%D8%B2%D9%88\",\n            \"https://abadis.ir/fatofa/%D8%A2%D8%B1%D8%B2%D9%88/\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"SOD:1\", \"status\": \"supports\", \"note\": \"SOD.txt entry 18 (printed p.1): 'ʾʾβrxsy ... Av. bərəg-, Parth. awarzog; Pahl. awarzog; Khot. aursa ... desire, lust'. Gharib gives 'awarzog' for both Parthian and Pahlavi, which is Nourai's first form.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"MacKenzie, English index 'lust'\", \"stance\": \"supports\", \"note\": \"PHD.txt line 2688: 'lust arzog, āz, waran, waranīgīh' — MacKenzie's Pahlavi headword is ārzōg.\"},\n            {\"src\": \"CHEUNG\", \"where\": \"s.v. *rauǰ² (*rauč), p.318-319\", \"stance\": \"contradicts\", \"note\": \"'(+ *ā-) MMP ʾwrzwg, ʾʾwrzwg, ʾwrzwwg, BMP ʾlcwk /arzog/ „desire, lust“ ... According to Henning 1945: 487, fn. 2, the Persian and Parthian „desire, lust“ forms derive from *barj, which is semantically implausible. A more suitable root is *rauǰ.'\"},\n            {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II glossary\", \"stance\": \"silent\", \"note\": \"NYB_vol2_glossary.txt has burz/buland/bālā but no ārzōg entry in the passages I could retrieve.\"},\n            {\"src\": \"MON\", \"where\": \"Farhang-e Farsi s.v. آرزو (via abadis)\", \"stance\": \"supports\", \"note\": \"'[پهلوی: ārzōk]' — Mo'in's Pahlavi antecedent is exactly Nourai's second form, confirming that the book's 'ârzôk' (not the JSON's 'âzôk') is what a source knows.\"}\n          ]\n        },\n        {\n          \"id\": 10,\n          \"lang\": \"Persian\",\n          \"words\": \"ârezŭ «آرزو» (extra: آرزومند)\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"The step actually drawn here — Middle Persian ārzōg/ārzōk → New Persian آرزو — is certain and regular: Book Pahlavi ʾlcwk /ārzōg/ 'desire, wish' gives Classical Persian ārzō (with the majhūl ō preserved in Dari and in classical metre) and modern Iranian ārezū after the general majhūl merger ō > ū; the final -g/-k is lost as in NP بندو < bandag, دارو < dārūg. آرزومند is the standard -mand possessive derivative ('having desire, desirous'), matching MP ārzōgōmand. Mo'in tags the entry '[پهلوی: ārzōk]'. What does NOT follow is the ancestry above it: the ultimate origin of the MP word is contested (Henning/Gharib: *ā-barj- 'to desire', which even so belongs to Pokorny's p.145 root, not p.140; Cheung and Wiktionary: *rauǰ/*rauč 'to please, desire', with the further origin unclear). So this node's own arrow is confirmed, while its placement under 'Bhergh: high' is not — see nodes #8 and #9.\",\n          \"derivation_fa\": \"همین حلقه‌ای که کشیده شده — فارسی میانهٔ ārzōg/ārzōk به فارسی نو «آرزو» — قطعی و قاعده‌مند است: پهلوی ʾlcwk /ārzōg/ «خواهش، آرزو» در فارسی دری ārzō می‌شود (واکهٔ مجهولِ ō در دری و در وزن شعر کهن هنوز پیداست) و پس از یکی‌شدن مجهول‌ها به ārezū امروزی می‌رسد؛ افتادن -g/-k پایانی همان قاعده‌ای است که bandag را به «بنده» و dārūg را به «دارو» رسانده. «آرزومند» نیز مشتق ملکیِ متعارف با پسوند -مند است و برابر پهلویِ ārzōgōmand. معین در مدخل خود می‌نویسد «[پهلوی: ārzōk]». آنچه پذیرفتنی نیست نیاکانِ بالاترِ این واژه است: خاستگاه واژهٔ فارسی میانه محل اختلاف است (هنینگ و قریب: *ā-barj- که آن هم به ریشهٔ صفحهٔ ۱۴۵ پوکورنی می‌رسد نه ۱۴۰؛ چونگ و ویکی‌واژه: *rauǰ/*rauč). پس پیکان خودِ این گره درست است ولی جای گرفتنش زیر ریشهٔ «بلند» نه.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%A2%D8%B1%D8%B2%D9%88\",\n            \"https://abadis.ir/fatofa/%D8%A2%D8%B1%D8%B2%D9%88/\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"BQT\", \"status\": \"not_checked\", \"note\": \"Nourai gives BQT without a page for this node. آرزو falls in the آ- section of vol.1 (roughly printed pp. 60-90, leaves ~270-310 of BQT_v1_pages.txt); the OCR of those leaves is too damaged to isolate the headword with confidence, and no page was cited to check.\"},\n            {\"ref\": \"MON:42\", \"status\": \"supports\", \"note\": \"Mo'in's آرزو entry read through abadis (فرهنگ معین): the etymological bracket is '[پهلوی: ārzōk]' and the gloss 'امید، انتظار، اشتیاق، خواهش، کام، مراد'. In the 2-vol Adena reprint on disk (MON_part1.txt line 2683ff) the running head next to the entry reads 'فرهنگ فارسی معین ۴۱', i.e. p.41-42 of that printing — consistent with Nourai's MON:42.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"MacKenzie, s.v. ārzōg / index 'lust'\", \"stance\": \"supports\", \"note\": \"'lust arzog' — the Pahlavi antecedent of the Persian word.\"},\n            {\"src\": \"CHEUNG\", \"where\": \"*rauǰ² p.318-319\", \"stance\": \"partial\", \"note\": \"Gives the MP > NP line ('BMP ʾlcwk /arzog/ „desire, lust“') but assigns it to *rauǰ, not to any *barz/*barj.\"},\n            {\"src\": \"HRN\", \"where\": \"Grundriss, b- and ā- sections\", \"stance\": \"silent\", \"note\": \"grep of HRN.txt for ārzū/arzu returns nothing; Horn has no numbered article for آرزو.\"},\n            {\"src\": \"MON\", \"where\": \"Farhang-e Farsi\", \"stance\": \"supports\", \"note\": \"See ref_check — '[پهلوی: ārzōk]'.\"}\n          ]\n        },\n        {\n          \"id\": 11,\n          \"lang\": \"Avestan\",\n          \"words\": \"bareša : high on top (of a horse neck), mane\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Av. barəša- is a genuine Young Avestan word of Yašt 10.11 (the Mihr Yašt), where the warriors worship Mithra 'bending down close to the barəša- of their horses'. Its meaning was disputed — Herzfeld argued for 'neck', not 'back' — and Gershevitch settled it: 'In fact it means „mane“, as shown by its Iranian cognates, cf. Arm. barš, Sogd. βunš, Bal. bušk, Ps. wraz, Oss. barc'. Formally it is the zero grade *bʰr̥ǵʰ-s- > Proto-Iranian *br̥ša- 'the high part (of the neck), crest', the same ablaut grade as in Av. barəšnu- 'Erhebung, Höhe, Scheitel, Kopf' and OP baršnā 'height'; the semantic bridge is 'the raised part on top' > 'crest, mane'. So Nourai's double gloss 'high on top (of a horse neck), mane' is exactly right, and the arrow from the root is sound.\",\n          \"derivation_fa\": \"barəša- واژه‌ای اوستایی نو و اصیل است و در یشت ۱۰ بند ۱۱ (مهریشت) آمده، آنجا که جنگاوران خم می‌شوند بر barəša-ی اسبانشان و از مهر نیرو می‌خواهند. معنای آن مدت‌ها محل بحث بود — هرتسفلد آن را «گردن» می‌خواند نه «پشت» — تا آنکه گرشویچ در حاشیهٔ صفحهٔ ۱۷۰ کتاب مهریشت گفت که معنایش «یال» است و هم‌ریشه‌های ایرانی‌اش را گواه آورد: ارمنی barš، سغدی βunš، بلوچی bušk، پشتو wraz، آسی barc. از نظر ساخت، این واژه درجهٔ صفر ریشه است (*bʰr̥ǵʰ-s- > ایرانی آغازین *br̥ša- «بخشِ برآمدهٔ گردن») و همان درجه‌ای است که در اوستایی barəšnu- «بلندی، فرق سر» و پارسی باستان baršnā «بلندی» دیده می‌شود؛ پل معنایی نیز «بخشِ بالاآمده» به «یال» است. پس هر دو معنایی که نورایی داده درست است و پیکان از ریشه به این گره پذیرفتنی است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/b%CA%B0er%C7%B5%CA%B0-\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"SOD:104\", \"status\": \"supports\", \"note\": \"SOD.txt entry 2650 on printed p.104 (the running-head '105' follows immediately in SOD_pages.txt leaf 170): 'βnš B ... βanš ©<*br̥ša-, Av. barəsa-, Pahl. buš, Arm. barš — mane. GMS 345; TSP 19.21 n p232; Gersh. AHM 170'. Gharib's entry names Av. barəša- with the meaning 'mane' — Nourai's node.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"AHM\", \"where\": \"Gershevitch, Avestan Hymn to Mithra, note to 10.11, p.170\", \"stance\": \"supports\", \"note\": \"AHM.txt line 1515: 'Htl. insists that barəša- does not mean „back“ but „neck“. In fact it means „mane“, as shown by its Iranian cognates, cf. Arm. barš, Sogd. βunš, Bal. bušk, Ps. wraz, Oss. barc'; and the translation at line 725: 'whom the warriors worship at (= bending down close to) the manes of their horses'. Gershevitch's index (p.3191) lists 'barəsa-, 170'.\"},\n            {\"src\": \"BRT\", \"where\": \"AiW, b- section\", \"stance\": \"silent\", \"note\": \"grep of BRT.txt for barəša-/barəsa- under several OCR spellings returns no headword; the column is not resolvable in this scan's OCR. Bartholomae's own reading of Yt 10.11 (which Gershevitch and Herzfeld argue against) is what the AHM note is discussing.\"},\n            {\"src\": \"PHD\", \"where\": \"MacKenzie p.20\", \"stance\": \"supports\", \"note\": \"PHD.txt line 292: 'buš [bwš | N ~] mane' — the Middle Persian cognate that Gharib cites, showing the etymon lived on in the direct Persian line as well.\"}\n          ]\n        },\n        {\n          \"id\": 12,\n          \"lang\": \"Sogdian\",\n          \"words\": \"bnš : mane\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Buddhist Sogdian βnš, read βanš/βunš, 'mane', is entry 2650 of Gharib's dictionary — exactly the page Nourai cites. Gharib reconstructs it from *br̥ša-, i.e. the same zero-grade *bʰr̥ǵʰ-s- as the Avestan word of node #11, and lists it beside Av. barəša-, Pahl. buš and Arm. barš. Phonologically Sogdian regularly turns initial Proto-Iranian *b- into the fricative β-, and the syllabic *r̥ appears as the anaptyctic vowel written with n in the Sogdian script (β-n-š); Gershevitch's Grammar of Manichean Sogdian §345 (cited by Gharib) covers the spelling. The node stands as drawn: the Sogdian word is a sister of the Avestan one and both continue the root.\",\n          \"derivation_fa\": \"βnš سغدیِ بودایی که βanš/βunš خوانده می‌شود و «یال» معنی می‌دهد، مدخل شمارهٔ ۲۶۵۰ فرهنگ قریب در همان صفحهٔ ۱۰۴ است که نورایی ارجاع داده. قریب آن را از *br̥ša- بازمی‌سازد، یعنی همان درجهٔ صفرِ *bʰr̥ǵʰ-s- که واژهٔ اوستایی گرهٔ پیشین از آن آمده، و در کنارش اوستایی barəša-، پهلوی buš و ارمنی barš را می‌نشاند. از نظر آوایی، b آغازینِ ایرانی آغازین در سغدی به‌قاعده به سایشیِ β بدل می‌شود و r̥ هجایی در خط سغدی با n نوشته می‌شود (β-n-š)؛ گرشویچ در دستور سغدی مانوی بند ۳۴۵ همین املا را شرح داده است. پس این گره چنان‌که کشیده شده درست است و واژهٔ سغدی خواهرِ واژهٔ اوستایی است نه دخترِ آن.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/b%CA%B0er%C7%B5%CA%B0-\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"SOD:104\", \"status\": \"supports\", \"note\": \"SOD_pages.txt, entry '2650 βnš B ... βanš ©<*br̥ša-, Av. barəsa-, Pahl. buš, Arm. barš / mane / GMS 345; TSP 19.21 n p232; Gersh. AHM 170', printed page 104 (the page number '105' appears immediately after the entry in the OCR).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"AHM\", \"where\": \"Gershevitch p.170\", \"stance\": \"supports\", \"note\": \"Lists 'Sogd. βunš' among the cognates that prove Av. barəša- means 'mane'.\"},\n            {\"src\": \"PHD\", \"where\": \"MacKenzie p.20 s.v. buš\", \"stance\": \"partial\", \"note\": \"'buš [bwš | N ~] mane' — establishes that Middle Persian had its own reflex, so Persian did not need the Sogdian word (relevant to node #13).\"},\n            {\"src\": \"ISS\", \"where\": \"Bailey, Dictionary of Khotan Saka\", \"stance\": \"silent\", \"note\": \"grep of ISS_alt_DKS.txt for a Khotanese reflex of *br̥ša- 'mane' returned nothing usable; Gharib cites no Khotanese form either.\"}\n          ]\n        },\n        {\n          \"id\": 13,\n          \"lang\": \"Persian\",\n          \"words\": \"faš «فَش» (extra: بَش ، پَش)\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"The Persian word and its meaning are beyond doubt: Dehkhoda has 'فش [فَ] ... کاکل اسب را نیز گویند (برهان). کاکل اسب. یال. (فرهنگ فارسی معین)' and cites Ferdowsi 'گرفتش فش و یال اسب سیاه' — the same Shahnameh material as the chart's quote 'بَش و یال اسبان کران تا کران'. The variants بَش/پَش that Nourai adds are the older and phonetically expected forms. But the ROUTE the chart draws is wrong. Middle Persian already has buš 'mane' (MacKenzie p.20, spelt bwš), the regular Western Iranian continuation of *br̥ša-, and NP بش is its direct descendant; Gharib himself lists Pahl. buš as a COGNATE of Sogdian βnš, not as its descendant. So Persian did not borrow the word from Sogdian: بش/فش and βnš are sisters. The by-forms with f- and p- are the familiar Persian b~p~f fluctuation in this word family (compare پش/فش beside بش), not a Sogdian import. The etymology (from the root, via *br̥ša-) is right; only the intermediate language is not.\",\n          \"derivation_fa\": \"خودِ واژه و معنایش تردیدناپذیر است: دهخدا می‌نویسد «فش [فَ] ... کاکل اسب را نیز گویند (برهان). کاکل اسب. یال. (فرهنگ فارسی معین)» و بیت فردوسی «گرفتش فش و یال اسب سیاه» را شاهد می‌آورد، که از همان خانوادهٔ شاهدِ نمودار است؛ گونه‌های «بَش» و «پَش» نیز که نورایی افزوده کهن‌تر و از نظر آوایی مورد انتظارند. اما مسیری که نمودار کشیده درست نیست. فارسی میانه خودْ buš «یال» دارد (مکنزی، صفحهٔ ۲۰، به املای bwš) که دنبالهٔ قاعده‌مندِ *br̥ša- در ایرانی غربی است و «بش» فارسی نو فرزند بی‌واسطهٔ همان است؛ قریب نیز خودِ Pahl. buš را همچون هم‌ریشه (نه فرزند) در کنار βnš سغدی آورده. پس فارسی این واژه را از سغدی وام نگرفته و «بش/فش» و βnš خواهرند. تناوب b~p~f در این واژه نیز پدیده‌ای درون‌فارسی است نه نشانهٔ وام‌گیری. ریشه‌شناسی درست است و تنها زبان میانجی نادرست.\",\n          \"sources\": [\n            \"https://abadis.ir/fatofa/%D9%81%D8%B4/\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"SOD:140\", \"status\": \"not_found\", \"note\": \"SOD_pages.txt leaf 206 = printed p.140 carries the δys-/δn- entries (nos. 3533-3547); there is nothing on faš/buš or on any Persian reflex there. The relevant Gharib page is 104 (entry 2650), which Nourai cites correctly on nodes #11-12; SOD:140 looks like a slip.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"MacKenzie p.20 s.v. buš\", \"stance\": \"partial\", \"note\": \"'buš [bwš | N ~] mane' — MacKenzie derives NP بش straight from Middle Persian buš, with no Sogdian intermediary.\"},\n            {\"src\": \"MON\", \"where\": \"Farhang-e Farsi s.v. فش (via abadis)\", \"stance\": \"supports\", \"note\": \"'(فَ) (اِ.) ۱ - کاکل اسب. ۲ - یال', with the Ferdowsi line 'گرفتش فش و یال اسپ سیاه / ز خون لعل شد خاک آوردگاه'. Confirms word and sense; gives no etymology.\"},\n            {\"src\": \"BQT\", \"where\": \"Borhan-e Qate' s.v. فش (quoted in Dehkhoda)\", \"stance\": \"supports\", \"note\": \"Dehkhoda's article attributes 'کاکل اسب را نیز گویند' explicitly to (برهان).\"},\n            {\"src\": \"SOD\", \"where\": \"Gharib entry 2650, p.104\", \"stance\": \"partial\", \"note\": \"Lists Pahl. buš as a cognate alongside Arm. barš — i.e. as a parallel reflex, not as a borrowing from Sogdian.\"},\n            {\"src\": \"HRN\", \"where\": \"Grundriss\", \"stance\": \"silent\", \"note\": \"grep of HRN.txt for faš/baš 'Mähne' returns no numbered article; Horn does not treat the word.\"}\n          ]\n        },\n        {\n          \"id\": 14,\n          \"lang\": \"Sogdian\",\n          \"words\": \"â-brxsy : wish\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"The word is real and Nourai's reference is exact: Gharib's entry 18 on p.1 is 'ʾʾβrxsy (Manichaean Sogdian) apraxse, from *ā-braxsaka-, „desire, lust“', with the Buddhist Sogdian variants ʾʾβʾrxsʾk / ʾʾβrxsʾkw and the derivatives ʾʾβrxsymync 'desiring, wishful' and ʾʾβrxsʾkmync 'lascivious'. What is disputed is the root. Gharib follows Henning (Sogdica/Tales 487 n.2) in linking it to Av. bərəg- via *ā-barj- 'to like to possess' — but that is Pokorny's p.145 root 'to honour, be attentive to', not the p.140 'high' root that heads this chart. Cheung goes further and detaches the Sogdian word altogether: 'Semantically, the Sogd. (inchoative) formations are perhaps more likely to contain the root *braHz „to shine, burn, set on fire“'. On either reading the arrow from Bhergh 'high' does not hold; the node is also drawn straight off the root box rather than off node #8, which makes the chart internally inconsistent (it is the same etymon as âwarzog).\",\n          \"derivation_fa\": \"واژه اصیل است و ارجاع نورایی دقیق: مدخل ۱۸ فرهنگ قریب در صفحهٔ ۱ چنین است: ʾʾβrxsy (سغدی مانوی) apraxse از *ā-braxsaka- «آرزو، شهوت»، همراه با گونه‌های سغدی بودایی ʾʾβʾrxsʾk و ʾʾβrxsʾkw و مشتق‌های ʾʾβrxsymync «آرزومند» و ʾʾβrxsʾkmync «شهوت‌ران». آنچه محل اختلاف است ریشه است. قریب پیرو هنینگ (حاشیهٔ ۲ صفحهٔ ۴۸۷) آن را از راه *ā-barj- «خواستنِ داشتن» به اوستایی bərəg- می‌پیوندد، ولی آن ریشه همان *bʰergʰ- «گرامی داشتن» صفحهٔ ۱۴۵ پوکورنی است نه *bʰerǵʰ- «بلند» صفحهٔ ۱۴۰ که سرلوحهٔ این نمودار است. چونگ یک گام فراتر می‌رود و پیوند را یکسره می‌گسلد و می‌نویسد که از نظر معنایی محتمل‌تر است این ساخت‌های سغدی به ریشهٔ *braHz «درخشیدن، افروختن» بازگردند. به هر دو خوانش، پیکانی که از ریشهٔ «بلند» به این گره کشیده شده استوار نیست؛ افزون بر این، نمودار این گره را مستقیم از جعبهٔ ریشه آویخته، حال آنکه با گرهٔ ۹ (آورزوگ) یکی است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%A2%D8%B1%D8%B2%D9%88\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"SOD:1\", \"status\": \"supports\", \"note\": \"SOD.txt entries 16-19 (printed p.1): '18 ʾʾβrxsy M apraxse (ʾʾβrxsʾy) ©<*ā-braxsaka; Av. bərəg-, Parth. awarzog; Pahl. awarzog; Khot. aursa ... desire, lust. Hen. Tales. 487 n 2; GMS 5'; also '16 ʾʾβrxsʾkmync S lascivious' and '19 ʾʾβrxsymync M desiring, wishful'. Nourai's page and form are correct.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"CHEUNG\", \"where\": \"s.v. *barj, p.11-12\", \"stance\": \"contradicts\", \"note\": \"'According to Henning 1945: 487, fn. 2, the meaning of barəg (i.e. *barj) in composition with *ā- is „to like to possess, to desire“, for which BSogd. ʾʾβʾrxsʾk ... are cited. This can be disputed, either for semantic or for formal reasons. Semantically, the Sogd. (inchoative) formations are perhaps more likely to contain the root *braHz „to shine, burn, set on fire“.'\"},\n            {\"src\": \"BRT\", \"where\": \"AiW s.v. bərəg-\", \"stance\": \"contradicts\", \"note\": \"Bartholomae's bərəg- is 'religiöser Brauch, Ritus', not 'wish' — the semantic bridge Henning needs is not in the Avestan evidence itself.\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins, bhergh-¹ [Pok. 145]\", \"stance\": \"contradicts\", \"note\": \"The 'honour/protect' root, which is where even Henning's account puts this word, is a separate entry from bhergh-² 'high' [Pok. 140].\"}\n          ]\n        },\n        {\n          \"id\": 15,\n          \"lang\": \"Old Persian\",\n          \"words\": \"bard- : to be high or tall; Bardiya : the glorified (person); baršan : height, depth; braz : prayer\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"This is the best-supported node on the page: all four items stand verbatim in Kent's lexicon on the two pages Nourai cites. bard- 'be high' shows the Old Persian treatment of the palatal, *rj > rd (Av. barəz- : OP bard-). Bardiya-, the Smerdis of Herodotus (Elam. bir-ti-ia, Akk. bar-zi-ia, Gk. Σμέρδις), is a -iya- derivative of bard- and means 'The Exalted' — the sense Nourai renders 'the glorified (person)'. baršan- (attested baršnā, instr. sg., DSf 26f 'height, depth') is the zero grade *bʰr̥ǵʰ-n- and matches Av. barəzan- 'Höhe'; Middle Persian bašn continues it. braz 'prayer' is Kent's brazman-, the base of the adjective brazmaniya- 'prayerful, reverent' of Xerxes' daiva inscription, cognate with Sanskrit bráhman- 'religious devotion, prayer' — a semantic development 'exaltation' > 'solemn utterance, prayer' that Kent explicitly refers 'to pIE root *bhergh- (see OP bard-)', following Henning TPS 1944. The b- for expected barz- (braz- rather than barz-) is noted by Kent as an Old Persian peculiarity supported by the Elamite and Akkadian spellings.\",\n          \"derivation_fa\": \"استوارترین گره این صفحه همین است: هر چهار واژه عیناً در واژه‌نامهٔ کنت در همان دو صفحه‌ای که نورایی ارجاع داده آمده‌اند. bard- «بلند بودن» بازتاب دگرگونی آوایی پارسی باستان است که در آن *rj به rd بدل می‌شود (اوستایی barəz- در برابر پارسی باستان bard-). Bardiya-، همان «سمردیس» هرودوت (ایلامی bir-ti-ia، اکدی bar-zi-ia)، مشتقی با پسوند -iya- از bard- است و «والامرتبه» معنی می‌دهد، درست همان که نورایی «the glorified» ترجمه کرده. baršan- (صورت گواهی‌شده baršnā در کتیبهٔ DSf بند ۲۶) درجهٔ صفرِ *bʰr̥ǵʰ-n- است و با اوستایی barəzan- «بلندی» می‌خواند و فارسی میانهٔ bašn دنبالهٔ آن است. braz نیز همان brazman- کنت است، پایهٔ صفت brazmaniya- «نیایشگر» در کتیبهٔ دیوهای خشایارشا و هم‌ریشه با سنسکریت bráhman- «نیایش»؛ تحول معنایی «برکشیدگی» به «سخن آیینی، نیایش» را کنت به پیروی از هنینگ صریحاً به همین ریشه بازمی‌گرداند. ادعای نورایی در این گره درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/b%CA%B0er%C7%B5%CA%B0-\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"KNT:200\", \"status\": \"supports\", \"note\": \"KNT.txt lexicon (printed p.200, the page marker '201' follows two entries later): 'bard- vb. „be high“: Av. barəz- „high“, barəzant- „lofty“, NPers. burz „high“, Skt. bṛhánt- „lofty“, OHG berg „mountain“, pIE *bhergh-; in Bardiya-, baršan-, probably in brazman-.' | 'Bardiya- sb. „Smerdis“, brother of Cambyses: Elam. bir-ti-ia, Akk. bar-zi-ia, Gk. Σμέρδις. Deriv. of OP bard- „be high“: „The Exalted“.' | 'baršan- sb. „height, depth“: Av. barəzan- (Bthl. AiW 950); deriv. of OP bard-. baršnā ism. DSf 26, 26f.'\"},\n            {\"ref\": \"KNT:201\", \"status\": \"supports\", \"note\": \"Same file, printed p.200-201: 'brazmaniya- adj. „prayerful, reverent“ ... with braz- rather than barz- (cf. Elam. pir-ra-uš-man-ni-ia, Akk. bi-ra-za-man-ni-i): deriv. to pAr. antecedent of Skt. bráhman- „religious devotion, prayer“ ... to pIE root *bhergh- (see OP bard-; Henning, TPS 1944.108-18).' The '201' page number appears at the end of that column.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"CHEUNG\", \"where\": \"*barz¹ p.12\", \"stance\": \"supports\", \"note\": \"'*OLD PERSIAN: baršnā (instr. sg. m.) <b-r-š-n-a> „height, depth“ (DSf 26 f.) = Kent: 200b'; and MP 'MMP bšn, BMP bšn /bašn/ „top, peak, height“'.\"},\n            {\"src\": \"HRN\", \"where\": \"no. 198\", \"stance\": \"supports\", \"note\": \"HRN.txt line 2135: 'ap. vergl. Bardiya-' — Horn already connects the Old Persian royal name with NP burz/buland.\"},\n            {\"src\": \"TLM\", \"where\": \"Tolman, Ancient Persian Lexicon, DB I\", \"stance\": \"supports\", \"note\": \"TLM.txt lines 194-216 print and translate the Bisotun passages with Bardiya ('when Cambyses slew Bardiya, it was not known to the people that Bardiya was slain'), confirming the name's attestation, though Tolman gives no etymology there.\"},\n            {\"src\": \"BRT\", \"where\": \"AiW col. 950\", \"stance\": \"supports\", \"note\": \"'j. barəzan- m. „Höhe“' — the Avestan match for OP baršan- that Kent cites.\"}\n          ]\n        },\n        {\n          \"id\": 16,\n          \"lang\": \"Persian\",\n          \"words\": \"Bardiyeh «بردیه»; barmaneš «برمنش»; bar 2 «بَر ٢» (extra: برتر ، برترین ، برین)\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Three items of unequal strength. Bardiyeh «بردیه» is simply the Persian rendering of Old Persian Bardiya (Smerdis), taken over as a learned/historical name; Kent's 'The Exalted' is Nourai's '„great, tall“'. That is confirmed. barmaneš «برمنش» is a Shahnameh word which Noushin analyses exactly as Nourai does: 'مرکب از بر [: بلند، بالا، ولا] + منش [اندیشه، سرشت، نهاد، خوی]: بلندمنش', citing the very line the chart quotes ('ازین دخت مهراب و از پور سام / گوی برمنش زاید و نیکنام'), and noting that the poets also use برز in the same slot ('منش برز داری و بالای برز'). So the compound does mean 'of high disposition' — but Noushin does not say which بر it contains. bar 2 «بَر» 'high' is the weak point, and Nourai flags it himself with the NOTE 'See root „Upo“ for another derivation': the standard account takes NP بر 'on, upon, above' (and its comparatives برتر، برترین، برین) from Old Persian upariy > MP abar > NP بر/ابر, i.e. from PIE *upo/*uper, not from bard-. Since bar 2 is the one word that carries the arrow from Old Persian bard-, the node as a whole can only be 'plausible'.\",\n          \"derivation_fa\": \"سه واژه با استواری‌های ناهمسان. «بردیه» صرفاً صورت فارسیِ نام پارسی باستان Bardiya (سمردیس) است که همچون نامی تاریخی به فارسی راه یافته، و «والامرتبه»ی کنت همان «great, tall»ی نورایی است؛ این یکی تأیید می‌شود. «برمنش» واژه‌ای شاهنامه‌ای است و نوشین در واژه‌نامک آن را دقیقاً چنان‌که نورایی گفته تجزیه می‌کند: «مرکب از بر [: بلند، بالا، ولا] + منش [اندیشه، سرشت، نهاد، خوی]: بلندمنش»، و همان بیتی را شاهد می‌آورد که در نمودار آمده، و می‌افزاید که شاعران گاه به‌جای «بر» واژهٔ «برز» را می‌نشانند («منش برز داری و بالای برز»). پس معنای ترکیب «بلندمنش» است، اما نوشین نمی‌گوید کدام «بر» در آن است. حلقهٔ سست همین «بَر ٢» است و خود نورایی نیز با یادداشت «برای اشتقاق دیگر ریشهٔ Upo را ببینید» به آن اشاره کرده: دیدگاه متعارف «بر» فارسی (و برتر، برترین، برین) را از پارسی باستان upariy و فارسی میانهٔ abar می‌گیرد، یعنی از *upo/*uper هندواروپایی نه از bard-. چون بارِ پیکانِ این گره بر دوش همین «بر» است، حکم کلی «با احتیاط پذیرفتنی» است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/b%CA%B0er%C7%B5%CA%B0-\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"FSF:79\", \"status\": \"supports\", \"note\": \"FSF_pages.txt leaves 103-104 (the برمنش article, printed p.79 by the volume's ~leaf−25 offset; leaf 100 carries the running head «برز» = the FSF:78 of nodes #2-3): 'برمنش ‑۱ مرکب از بر [: بلند، بالا، ولا] + منش [اندیشه، سرشت، نهاد، خوی]: بلندمنش ... ازین دخت مهراب و از پور سام / گوی برمنش زاید و نیکنام'. Noushin adds that Mo'in's Farhang-e Farsi wrongly prints «ابرمنش» — which is itself evidence that the ابر/upari derivation was in play.\"},\n            {\"ref\": \"KNT:200\", \"status\": \"supports\", \"note\": \"KNT.txt s.v. Bardiya-: 'Deriv. of OP bard- „be high“: „The Exalted“' — the source of Nourai's «بردیه: „great, tall“».\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"FSF\", \"where\": \"Vazhe-namak leaves 103-104 (برمنش)\", \"stance\": \"supports\", \"note\": \"Also 'و گاه بجای «بر» «برز [با پیش اول]» ... منش برز داری و بالای برز' — showing that Ferdowsi could substitute برز for بر in the same compound slot, which is the strongest argument in Nourai's favour for barmaneš.\"},\n            {\"src\": \"HRN\", \"where\": \"no. 198\", \"stance\": \"supports\", \"note\": \"'ap. vergl. Bardiya-' under burz/buland — Horn links the Old Persian name to the same family.\"},\n            {\"src\": \"PHD\", \"where\": \"MacKenzie p.4-5\", \"stance\": \"contradicts\", \"note\": \"PHD.txt line 164 lists the abar- family ('abarmān, abar-menišn „proud, haughty“, abar-tan „arrogant“') from MP abar 'on, above' < OP upariy — the rival source of NP بر and of compounds of the barmaneš type (MP abar-menišn is the literal counterpart of برمنش).\"},\n            {\"src\": \"MON\", \"where\": \"Farhang-e Farsi s.v. برمنش\", \"stance\": \"contradicts\", \"note\": \"Reported by Noushin (FSF leaf 103) as printing «ابرمنش», i.e. Mo'in reads the first element as ابر < abar < upariy, not as برز.\"}\n          ]\n        }\n      ]\n    }\n  ]\n}\nJSONEOF\npython3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-92.json > /dev/null && echo \"JSON OK\""
}
```


### [2026-09-05T14:35:13.043Z] TOOL RESULT

```
JSON OK
```


## [2026-09-05T14:35:17.093Z] TOOL CALL #90: Bash

```json
{
 "command": "python3 tools/verify_check.py 92"
}
```


### [2026-09-05T14:35:19.212Z] TOOL RESULT

```
nodes verified: 16/16
node verdicts: {'plausible': 3, 'confirmed': 7, 'disputed': 5, 'transcription_suspect': 1}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 21, 'not_checked': 4, 'partial': 5, 'not_found': 3}
books consulted: {'partial': 9, 'supports': 29, 'contradicts': 15, 'silent': 8} | by book: {'PHD': 8, 'CHEUNG': 7, 'HRN': 6, 'MON': 6, 'BRT': 5, 'AHD': 5, 'NYB': 3, 'BQT': 2, 'KLN': 2, 'PHN': 2, 'SKT': 2, 'LKT': 2, 'AHM': 2, 'FVQ': 1, 'HUB': 1, 'DEV': 1, 'FSD': 1, 'POK': 1, 'ISS': 1, 'SOD': 1, 'TLM': 1, 'FSF': 1}
```


## [2026-09-05T14:35:23.768Z] TOOL CALL #91: Bash

```json
{
 "command": "python3 - <<'EOF'\nimport json\nv=json.load(open('data/verification/page-92.json'))\nurls=set()\ndef walk(o):\n    if isinstance(o,dict):\n        for k,x in o.items():\n            if k=='sources': urls.update(x)\n            else: walk(x)\n    elif isinstance(o,list):\n        for x in o: walk(x)\nwalk(v)\nidx={json.loads(l)['url'] for l in open('data/verification/sources/web/index.jsonl')}\nmiss=[u for u in urls if u not in idx]\nprint('cited urls:',len(urls),'missing from archive:',miss)\nEOF"
}
```


### [2026-09-05T14:35:25.364Z] TOOL RESULT

```
cited urls: 12 missing from archive: []
```


## [2026-09-05T14:35:43.859Z] AGENT

Page 92 (book p. 62), root **Bhergh "high"** (PART 1), 1 entry / 16 nodes — `verify_check.py 92`: 0 PROBLEM lines.

**Verdicts:** root confirmed · nodes: 7 confirmed, 3 plausible, 5 disputed, 1 transcription_suspect. Ref checks: 21 supports / 5 partial / 3 not_found / 4 not_checked.

**Disputed**
- #4 Italian `barbacane, balcone` — *balcone* is Germanic (OIt. *balco* < Lombardic \*balkō "beam"); AHD files BALCONY under *bhelg-*, Klein/Etymonline agree. Only Lokotsch p.17 and Pihan p.55 back Nourai's bālā-ḵāna. Nourai's own NOTE is right.
- #5 French `balcon` — same; the It.→Fr. step is fine, the source of the Italian word is not.
- #7 English `barbican, balcony` — barbican from Pers. *bālā-ḵāna* is plausible (Klein p.148); balcony is not.
- #8 Avestan `bereg, â-bereg` — Bartholomae glosses *barəg-* "to welcome", *bərəg-* "religious rite", not "high, desirable"; Cheung assigns it to the **homonymous** PIE \*bʰergʰ- "to honour" = Pokorny **145**, not the chart's Pokorny 140.
- #14 Sogdian `â-brxsy` — same wrong root; Cheung would detach it entirely (\*braHz "to shine").

**Transcription_suspect (EXTRACTION ERROR — owner must fix the data)**
- #9 Pahlavi: the book prints **`âwarzog, ârzôk`**; `data/extracted/batch/page-92.json` has **`âzôk`** (the *r* is dropped). Page image saved to `data/verification/sources/refs/ocr/BOOK/92.png` and crop `92_pahlavi_box.png`. `ârzôk` is correct — Mo'in gives the Pahlavi antecedent of آرزو as *ārzōk*.

**Other notes worth the owner's eye**
- `SOD:140` on node #13 (faš) is a bad citation: Gharib p.140 has the δ- entries; the mane word is entry 2650 on p.104. Also the route is wrong — NP بش/فش descends from MP *buš* (MacKenzie p.20); Sogdian βnš is a sister, not the parent (node #13 → plausible).
- Node #1: `barz-ahva` is not attested in Avestan; it is Parthian \*burz-axw "high world", the source of Arabic *barzaḵ* (→ node #2 برزخ, a Persian→Arabic→Persian round trip). Jeffery FVQ p.77 dissents, deriving barzakh from *farsang*.
- Node #16 `bar 2` — the standard derivation is OP *upariy* > MP *abar*, which Nourai himself cross-references to root "Upo"; Mo'in even prints «ابرمنش» for برمنش.

Files: `data/verification/page-92.json`; 13 new archived web sources in `data/verification/sources/web/`.
