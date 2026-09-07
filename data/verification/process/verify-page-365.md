# Verification process log — verify-page-365


## [2026-09-07T19:29:15.187Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 365 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-365.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-365.json. Write /home/sfmqrb/git/rishe/data/verification/page-365.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 365` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-07T19:29:17.427Z] AGENT

I'll start by reading the instructions.


## [2026-09-07T19:29:18.085Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-07T19:29:18.096Z] TOOL RESULT

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


## [2026-09-07T19:29:18.838Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-365.txt"
}
```


### [2026-09-07T19:29:18.855Z] TOOL RESULT

```
1	=== PDF page 365 (book page 335) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Nî 1 : down, below  (refs KLN:1042)
4	#1 (parent #0) [Avestan / Old Persian] refs=KLN:1042 | ni 1 : down
5	  #2 (parent #1) [Avestan / Old Persian] refs=BQT:2134,2145,2147,2201; POK:884 | ni-jan : put down, sad ☞Gwhen 2 ; ni-had, ni-shidhaiti : to sit down ☞Sed ; ni-xšvaepâ : down slope ☞Xshvaepâ ; ni-pais : write down ☞Peig ; ni-part : fight down ☞Per 3 ; ni-vart : roll down ☞Wer 2
6	    #3 (parent #2) [Persian] refs=BQT | nažand «نژند» : sad, put down ; nešastan «نشستن» : to sit down ; našîb «نشیب» : down slope ; neveštan «نوشتن» : to write down ; nabard «نبرد» : fight ; navardîdan «نوردیدن» : to roll | extra: نشیمن ، نشیم ؛ نورد
7	  #4 (parent #1) [Avestan / Old Persian] refs=POK:235,454; BQT:2211; HRN:238 | ni-dâ : to lay down, hide ☞Dhě 2 ; ni-gaoša : to listen ☞Ôus 1 ; ni-gâma : (place for) inserting down ☞Gwa ; ni-kasa : look ☞Kwek ; ni-az : that which pushes you down, need ☞Angh
8	    #5 (parent #4) [Persian] refs=None | nahâdan «نهادن» : to lay down ; nîûšîdan «نیوشیدن» : to listen ; nîâm «نیام» : sheath ; negâh «نگاه» : look ; nîâz «نیاز» : need | extra: نهان
9	  #6 (parent #1) [Avestan / Old Persian] refs=BQT:2171; HRN:233 | ni-mâ : measure down, show ☞Me ; nî-gaona : downward ☞Gěu 1
10	    #7 (parent #6) [Persian] refs=MON:4812 | nemŭdan «نمودن» : to display ; nemâîdan «نماییدن» : to represent ; negŭn «نگون» : downward | extra: نمود ، نمودار ؛ نما ، نمایش ، نماینده ، نمایان ؛ نگونسار ، سرنگون
11	  #8 (parent #1) [Avestan] refs=SOD:237,244,252 | ni-gerepta : pressed down ☞Ghrebh ; ni-yaštâya : to settle down establish ☞Sta ; ni-paidhya : to lie down (step down) ☞Ped?
12	#9 (parent #0) [Germanic] refs=AHD; KLN:1042 | nith : below ; nist : place to sit down, nest
13	  #10 (parent #9) [English] refs=None | beneath, underneath ; nest
14	--- entry 1 ---
15	ROOT Ni 2 -> redirect to Nei 1
16	--- entry 2 ---
17	ROOT Nî 3 -> redirect to Nei 2
18	--- entry 3 ---
19	ROOT Nimatâ -> redirect to Nemata 2
20	
```


## [2026-09-07T19:29:22.300Z] TOOL CALL #3: Bash

```json
{
 "command": "python3 -m json.tool data/extracted/batch/page-365.json | head -200",
 "description": "Read source JSON for page 365"
}
```


## [2026-09-07T19:29:23.043Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-07T19:29:23.547Z] TOOL RESULT

```
{
    "pdf_page": 365,
    "book_page": 335,
    "entries": [
        {
            "root": {
                "name": "N\u00ee 1",
                "lang": "Indo-European",
                "refs": "KLN:1042",
                "gloss": "down, below"
            },
            "nodes": [
                {
                    "id": 1,
                    "parent": 0,
                    "lang": "Avestan / Old Persian",
                    "refs": "KLN:1042",
                    "words": [
                        {
                            "translit": "ni 1",
                            "gloss": "down",
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 2,
                    "parent": 1,
                    "lang": "Avestan / Old Persian",
                    "refs": "BQT:2134,2145,2147,2201; POK:884",
                    "words": [
                        {
                            "translit": "ni-jan",
                            "gloss": "put down, sad",
                            "script": null,
                            "see": [
                                "Gwhen 2"
                            ]
                        },
                        {
                            "translit": "ni-had, ni-shidhaiti",
                            "gloss": "to sit down",
                            "script": null,
                            "see": [
                                "Sed"
                            ]
                        },
                        {
                            "translit": "ni-x\u0161vaep\u00e2",
                            "gloss": "down slope",
                            "script": null,
                            "see": [
                                "Xshvaep\u00e2"
                            ]
                        },
                        {
                            "translit": "ni-pais",
                            "gloss": "write down",
                            "script": null,
                            "see": [
                                "Peig"
                            ]
                        },
                        {
                            "translit": "ni-part",
                            "gloss": "fight down",
                            "script": null,
                            "see": [
                                "Per 3"
                            ]
                        },
                        {
                            "translit": "ni-vart",
                            "gloss": "roll down",
                            "script": null,
                            "see": [
                                "Wer 2"
                            ]
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 3,
                    "parent": 2,
                    "lang": "Persian",
                    "refs": "BQT",
                    "words": [
                        {
                            "translit": "na\u017eand",
                            "gloss": "sad, put down",
                            "script": "\u0646\u0698\u0646\u062f"
                        },
                        {
                            "translit": "ne\u0161astan",
                            "gloss": "to sit down",
                            "script": "\u0646\u0634\u0633\u062a\u0646"
                        },
                        {
                            "translit": "na\u0161\u00eeb",
                            "gloss": "down slope",
                            "script": "\u0646\u0634\u06cc\u0628"
                        },
                        {
                            "translit": "neve\u0161tan",
                            "gloss": "to write down",
                            "script": "\u0646\u0648\u0634\u062a\u0646"
                        },
                        {
                            "translit": "nabard",
                            "gloss": "fight",
                            "script": "\u0646\u0628\u0631\u062f"
                        },
                        {
                            "translit": "navard\u00eedan",
                            "gloss": "to roll",
                            "script": "\u0646\u0648\u0631\u062f\u06cc\u062f\u0646"
                        }
                    ],
                    "script_extra": "\u0646\u0634\u06cc\u0645\u0646 \u060c \u0646\u0634\u06cc\u0645 \u061b \u0646\u0648\u0631\u062f",
                    "note": null,
                    "quote": {
                        "text": "\u0646\u0628\u0627\u0634\u062f \u0634\u0627\u062f\u0645\u0627\u0646\u06cc \u0628\u06cc \u0646\u0698\u0646\u062f\u06cc - \u0646\u0647 \u067e\u06cc\u0631\u0648\u0632\u06cc \u0628\u0648\u062f \u0628\u06cc \u0645\u0633\u062a\u0645\u0646\u062f\u06cc",
                        "poet": "Ferdows\u00ee"
                    }
                },
                {
                    "id": 4,
                    "parent": 1,
                    "lang": "Avestan / Old Persian",
                    "refs": "POK:235,454; BQT:2211; HRN:238",
                    "words": [
                        {
                            "translit": "ni-d\u00e2",
                            "gloss": "to lay down, hide",
                            "script": null,
                            "see": [
                                "Dh\u011b 2"
                            ]
                        },
                        {
                            "translit": "ni-gao\u0161a",
                            "gloss": "to listen",
                            "script": null,
                            "see": [
                                "\u00d4us 1"
                            ]
                        },
                        {
                            "translit": "ni-g\u00e2ma",
                            "gloss": "(place for) inserting down",
                            "script": null,
                            "see": [
                                "Gwa"
                            ]
                        },
                        {
                            "translit": "ni-kasa",
                            "gloss": "look",
                            "script": null,
                            "see": [
                                "Kwek"
                            ]
                        },
                        {
                            "translit": "ni-az",
                            "gloss": "that which pushes you down, need",
                            "script": null,
                            "see": [
                                "Angh"
                            ]
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 5,
                    "parent": 4,
                    "lang": "Persian",
                    "refs": null,
                    "words": [
                        {
                            "translit": "nah\u00e2dan",
                            "gloss": "to lay down",
                            "script": "\u0646\u0647\u0627\u062f\u0646"
                        },
                        {
                            "translit": "n\u00ee\u00fb\u0161\u00eedan",
                            "gloss": "to listen",
                            "script": "\u0646\u06cc\u0648\u0634\u06cc\u062f\u0646"
                        },
                        {
                            "translit": "n\u00ee\u00e2m",
                            "gloss": "sheath",
                            "script": "\u0646\u06cc\u0627\u0645"
                        },
```


### [2026-09-07T19:29:23.582Z] TOOL RESULT

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


## [2026-09-07T19:29:26.876Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -m json.tool data/extracted/batch/page-365.json | sed -n '200,400p'",
 "description": "Rest of source JSON"
}
```


### [2026-09-07T19:29:28.249Z] TOOL RESULT

```
                        },
                        {
                            "translit": "neg\u00e2h",
                            "gloss": "look",
                            "script": "\u0646\u06af\u0627\u0647"
                        },
                        {
                            "translit": "n\u00ee\u00e2z",
                            "gloss": "need",
                            "script": "\u0646\u06cc\u0627\u0632"
                        }
                    ],
                    "script_extra": "\u0646\u0647\u0627\u0646",
                    "note": null,
                    "quote": {
                        "text": "\u0628\u0647 \u06af\u0648\u0634 \u0647\u0648\u0634 \u0646\u06cc\u0648\u0634 \u0627\u0632 \u0645\u0646 \u0648 \u0628\u0647 \u0639\u0634\u0631\u062a \u06a9\u0648\u0634 - \u06a9\u0647 \u0627\u06cc\u0646 \u0633\u062e\u0646 \u0633\u062d\u0631 \u0627\u0632 \u0647\u0627\u062a\u0641\u0645 \u0628\u0647 \u06af\u0648\u0634 \u0622\u0645\u062f",
                        "poet": "H\u00e2fez"
                    }
                },
                {
                    "id": 6,
                    "parent": 1,
                    "lang": "Avestan / Old Persian",
                    "refs": "BQT:2171; HRN:233",
                    "words": [
                        {
                            "translit": "ni-m\u00e2",
                            "gloss": "measure down, show",
                            "script": null,
                            "see": [
                                "Me"
                            ]
                        },
                        {
                            "translit": "n\u00ee-gaona",
                            "gloss": "downward",
                            "script": null,
                            "see": [
                                "G\u011bu 1"
                            ]
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 7,
                    "parent": 6,
                    "lang": "Persian",
                    "refs": "MON:4812",
                    "words": [
                        {
                            "translit": "nem\u016ddan",
                            "gloss": "to display",
                            "script": "\u0646\u0645\u0648\u062f\u0646"
                        },
                        {
                            "translit": "nem\u00e2\u00eedan",
                            "gloss": "to represent",
                            "script": "\u0646\u0645\u0627\u06cc\u06cc\u062f\u0646"
                        },
                        {
                            "translit": "neg\u016dn",
                            "gloss": "downward",
                            "script": "\u0646\u06af\u0648\u0646"
                        }
                    ],
                    "script_extra": "\u0646\u0645\u0648\u062f \u060c \u0646\u0645\u0648\u062f\u0627\u0631 \u061b \u0646\u0645\u0627 \u060c \u0646\u0645\u0627\u06cc\u0634 \u060c \u0646\u0645\u0627\u06cc\u0646\u062f\u0647 \u060c \u0646\u0645\u0627\u06cc\u0627\u0646 \u061b \u0646\u06af\u0648\u0646\u0633\u0627\u0631 \u060c \u0633\u0631\u0646\u06af\u0648\u0646",
                    "note": null,
                    "quote": null
                },
                {
                    "id": 8,
                    "parent": 1,
                    "lang": "Avestan",
                    "refs": "SOD:237,244,252",
                    "words": [
                        {
                            "translit": "ni-gerepta",
                            "gloss": "pressed down",
                            "script": null,
                            "see": [
                                "Ghrebh"
                            ]
                        },
                        {
                            "translit": "ni-ya\u0161t\u00e2ya",
                            "gloss": "to settle down establish",
                            "script": null,
                            "see": [
                                "Sta"
                            ]
                        },
                        {
                            "translit": "ni-paidhya",
                            "gloss": "to lie down (step down)",
                            "script": null,
                            "see": [
                                "Ped?"
                            ]
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 9,
                    "parent": 0,
                    "lang": "Germanic",
                    "refs": "AHD; KLN:1042",
                    "words": [
                        {
                            "translit": "nith",
                            "gloss": "below",
                            "script": null
                        },
                        {
                            "translit": "nist",
                            "gloss": "place to sit down, nest",
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 10,
                    "parent": 9,
                    "lang": "English",
                    "refs": null,
                    "words": [
                        {
                            "translit": "beneath, underneath",
                            "gloss": null,
                            "script": null
                        },
                        {
                            "translit": "nest",
                            "gloss": null,
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                }
            ]
        },
        {
            "root": {
                "name": "Ni 2",
                "redirect": "Nei 1"
            },
            "nodes": []
        },
        {
            "root": {
                "name": "N\u00ee 3",
                "redirect": "Nei 2"
            },
            "nodes": []
        },
        {
            "root": {
                "name": "Nimat\u00e2",
                "redirect": "Nemata 2"
            },
            "nodes": []
        }
    ]
}
```


## [2026-09-07T19:29:28.529Z] TOOL CALL #6: Bash

```json
{
 "command": "ls data/verification/ | head -30 && echo ---- && cat data/verification/page-312.json | python3 -c \"import json,sys; d=json.load(sys.stdin); print(json.dumps(d['entries'][0], ensure_ascii=False, indent=1)[:4000])\"",
 "description": "Look at an example output file"
}
```


### [2026-09-07T19:29:29.940Z] TOOL RESULT

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
----
{
 "entry": 2,
 "root": "Leuk, Leuqos",
 "verdict": "confirmed",
 "modern_form": "PIE *leuk- (Pokorny leuk̂-) 'light, brightness; to shine, to see', with the thematic *leuk-o-s (Gk. leukós) that Nourai calls 'Leuqos'",
 "note": "Root, language label, gloss and page reference are all right. Pokorny, IEW 687-690, lemma leuk̂- (leuk-), Meaning 'bright, to shine; to see' (References: WP. II 408 ff.), listing exactly the material of this chart: Av. raocah-, OP raucah-, Av. raoxšna-, Lat. lūx/lūmen/lūna/lūstrum/lūstrāre, Goth. liuhaþ / OHG lioht / OE lēoht, Skt. loka-. Watkins/AHD: \"leuk-. Light, brightness. ... [Pok. leuk- 687.]\" — so POK:687 is the exact page. Kent (KNT:205), Nourai's second reference, gives the same root in the older notation pIE *leugos s.v. raucah-. 'Leuqos' is Nourai's spelling of the *leuk-o-s form (Gk. leukós 'white, bright', Skt. loka- 'open bright space, world', Lat. lūcus 'grove'); it is not a separate root. Cross-cutting remarks: (1) the chart's strongest link, Persian rūz/rōšan/afrūxtan and the Arabic loan rizq, is fully confirmed; (2) two Persian items in the Persian box (آرش, درفش ۱) and one Avestan item (a-raxša, plus the unattested raoč-xšaema) are not supported by modern sources; (3) the Sogdian box mixes an inherited word (rwxšn) with a Sanskrit loanword (δwk' < Skt. loka); (4) the Germanic box misprints the reconstruction (liuhtam for *leuhtam); (5) on the printed page the Old Persian box has an arrow into an empty, unlabelled box that the JSON does not record.",
 "note_fa": "ریشه، برچسبِ زبان، معنی و شمارهٔ صفحه هر چهار درست است: پوکورنی در «فرهنگ ریشه‌شناسیِ هندواروپایی» صفحه‌های ۶۸۷ تا ۶۹۰ ریشهٔ leuk̂- را با معنای «روشن، درخشیدن؛ دیدن» می‌آورد و همان داده‌های این نمودار را برمی‌شمارد: اوستایی raocah- و raoxšna-، پارسی باستان raucah-، لاتین lūx و lūmen و lūna و lūstrum، گوتیک liuhaþ و انگلیسی کهن lēoht، و سنسکریت loka-. واتکینز نیز ذیل leuk- همین ارجاع «پوکورنی ۶۸۷» را دارد. «Leuqos» صورتِ ستاک‌دارِ *leuk-o-s است (یونانی leukós، سنسکریت loka-، لاتین lūcus) و ریشهٔ جداگانه‌ای نیست. به‌طور کلی: پیوندِ فارسی «روز، روشن، افروختن» و وام‌واژهٔ عربیِ «رزق» کاملاً تأیید می‌شود؛ اما «آرش» و «درفش ۱» در جعبهٔ فارسی و «a-raxša» و «raoč-xšaema» در جعبهٔ اوستایی پشتوانهٔ امروزی ندارند؛ جعبهٔ سغدی یک واژهٔ میراثی (rwxšn) را با یک وام‌واژهٔ سانسکریت (δwk' از loka) درآمیخته؛ و در جعبهٔ ژرمنی صورتِ بازسازی‌شده غلط چاپ شده است (liuhtam به‌جای *leuhtam).",
 "sources": [
  "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/lewk-",
  "https://en.wiktionary.org/wiki/%D8%B1%D9%88%D8%B2"
 ],
 "ref_check": [
  {
   "ref": "POK:687",
   "status": "supports",
   "note": "POK_full.txt, block 'Root / lemma: lehuk- (*lehugh-)', Meaning 'bright, to shine; to see', Page(s): 687-690 — with \"rocas-, rocis-, Avestan raocah-, ap. raucah- n. 'light, radiance, esp. of heaven', Avestan raoxšna- 'gleaming'\", \"Latin lūmen 'light' from *leuk-s-men; lūna 'moon goddess' (*leuksna)\", \"lustrum ... lūstro, -are 'to light up, illuminate'\", \"Gothic liuhaþ 'light' ... Old English leoht\""
  },
  {
   "ref": "KNT:205",
   "status": "supports",
   "note": "Kent, Old Persian, Lexicon s.v. raucah- (KNT.txt leaf 229): \"raucah- sb. 'day': Av. raocah- 'light', Phl. rūč, NPers. rōz, Skt. rócas- 'light', pIE *leugos\"; cf. §156.II \"pIE *leugos, OP rauca, Skt. rócas\". Kent's *leug-/*leugos is the same root in pre-1959 notation."
  }
 ],
 "consulted": [
  {
   "src": "AHD",
   "where": "Watkins 1985, s.v. leuk-",
   "stance": "supports",
   "note": "\"leuk-. Light, brightness. I. Basic form *leuk- ... [Pok. leuk- 687.]\" with the Germanic, Latin and Greek branches of this chart"
  },
  {
   "src": "WLD",
   "where": "Walde-Pokorny Bd. II 408-411, s.v. leuq-",
   "stance": "supports",
   "note": "the same root under the older lemma leuq-: \"rocas-, rocis- n., av. raocah-, ap. raucah- n. 'Licht, Leuchte, bes. des Himmels', ai. rukṣá- 'glänzend', av. raoxšna- 'glänzend' ... (= lat. luna ...); auf diesem -es-St. beruhen auch lat.
```


## [2026-09-07T19:29:42.926Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Root / lemma: ni-\" POK_full.txt | head -20; echo \"=== ni,nei\"; grep -n \"^Meaning: down\" POK_full.txt | head",
 "description": "Find Pokorny ni- root"
}
```


### [2026-09-07T19:29:42.990Z] TOOL RESULT

```
=== ni,nei
```


## [2026-09-07T19:29:44.173Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',errors='replace').read()\ni=t.find('nether')\nprint(len(t))\nfor m in re.finditer(r'\\bni-,',t):\n    print(m.start(), t[m.start()-200:m.start()+600].replace('\\n',' '))\n    print('-----')\nEOF",
 "description": "Klein ni- entry"
}
```


### [2026-09-07T19:29:45.740Z] TOOL RESULT

```
10393096
5467374 r.  Pers.  lilak,  var.  of  nilak,  ‘bluish’,  fr.  nil,  ‘blue, indigo’,  fr.  OI.  nilah,  ‘dark  blue’,  which  is  of  un¬ certain  etymology.  It  possibly  derives  fr.  I.-E. Liliaceae base  *ni-,  ‘to  shine’.  See  neat,  adj.,  and  cp.  anil and  the  first  element  in  nilgai  and  in  nainsook. Derivative:  lilac ,  adj. Liliaceae,  n.  pi.,  the  lily  family  ( bot .)  —  ModL., formed  fr.  Li  limn  with  suff.  -aceae. liliaceous,  adj.  —  See  prec.  word  and  -aceous. Lilith,  n.,  a  female  evil  spirit.  —  Heb.  Lilith ,  fr. Akkad.  Lilitu  (whence  also  Syr.  Lelitha),  not  re¬ lated  to,  but  folk-etymologically  connected  with, Heb.  ldylah,  ‘night’,  and  explained  accordingly as  ‘night  demon’. Lilium,  n.,  a  genus  of  plants,  the  lily  (bot.) 
-----
6380422 dzdo,  Lith.  lizdas,  Lett,  ligzda,  OIr.  net,  W. nyth,  Co.  neid,  Bret,  nez,  neiz,  ‘nest’.  I.-E.  *niz- do-,  stands  for  *ni-zd-o-  and  lit.  means  ‘a  place to  sit  down  in’,  fr.  *ni-,  ‘down’,  and  zero  degree of  I.-E.  base  *sed-,  ‘to  sit"  [cp.  OI.  ni-satsuh, ‘sitting’,  ni-sidati,  ‘sits  down,  settles’,  and  Gk. 6^05  (metathesis  for  *oz-d-os),  ‘branch’.  Arm. ost,  Goth,  asts,  OHG.,  MHG.,  OS.  ast,  MDu. aesl,  Du.  nest,  ‘branch,  bough’,  OE.  ost,  ‘knot in  a  tree’,  fr.  I.-E.  *ozdos,  ‘that  which  sits  (close to  the  trunk)’,  fr.  zero  degree  of  *sed-,  ‘to  sit’]. See  nether  and  sedentary  and  cp.  eyas,  nidus, nidificate.  Cp.  also  nestle. Derivatives:  nest,  intr.  and  tr.  v.  nest-er,  n. nestitherapy,  n„  cure  by  
-----
```


## [2026-09-07T19:29:52.067Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"nizdo\\|ni-zdo\\|nisdo\" POK_full.txt | head -20; echo === ; grep -n \"Root / lemma: ni\" POK_full.txt | head -20",
 "description": "Pokorny nest/ni"
}
```


### [2026-09-07T19:29:52.116Z] TOOL RESULT

```
Exit code 1
(eval):1: == not found
```


## [2026-09-07T19:29:53.169Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"nether\" KLN_1966.txt | head -20",
 "description": "Klein nether"
}
```


### [2026-09-07T19:29:53.242Z] TOOL RESULT

```
4740:bene-,  combining  form  meaning  ‘well’.  —  L.  bene, ‘well’,  fr.  earlier  *dwene,  rel.  to  bonus,  earlier *dwenos,  ‘good’,  bellus,  earlier  *dwenelos,  *dwen- los,  ‘beautiful’.  See  bonus,  beauty, beneath,  prep,  and  adv.  —  ME.  benethe,  bene- othen,  fr.  OE.  beneopan,  fr.  be-,  ‘by’,  and  neopan, ‘below,  beneath’.  See  be-  and  nether  and  cp. underneath.
13523:Erebus,  n.,  a  place  of  nether  darkness  leading from  Earth  to  Hades  ( Greek  mythol.)  —  L.,  fr. Gk.  vEpe|3os,  fr.  Heb.  ‘ erebh ,  ‘sunset,  evening’. See  maarib  and  cp.  Europe.
13836:Europe,  n.  —  L.  Europa,  fr.  Gk.  Eupdjxr),  ‘Europa  ; Europe’,  which  is  prob.  of  Semitic  origin.  Cp. Akkad,  erebu ,  ‘to  enter,  go  in;  to  go  down,  set’ (said  of  the  sun),  ereb  shamshi,  ‘sunset’,  Heb. 'erebh,  ‘sunset,  evening’;  see  Heinrich  Lewy, Die  semitischen  Fremdwdrter  im  Griechischen, Berlin,  1895,  pp.  139-140.  Accordingly  Eupw— r, orig.  meant  ‘the  Region  of  the  Setting  Sun'.  Cp Hesychius,  who  renders  Eoptirr r,  with  the  words -/copx  t f,p  8'jaetop  (=  ‘the  Land  of  the  Setting Sun’).  Cp.  also  Gk.  ’'Epspop,  ‘place  of  nether darkness’,  which  derives  fr.  Heb.  'erebh.  See maarib  and  cp.  Erebus.  The  form  Eup  cutty;  (as  if the  name  meant  evp-com;,  ‘broad  face’)  is  due  - to  the  natural  tendency  of  the  Greeks  to  Grecize words  foreign  to  their  language.  For  the  sense development  of  Gk.  EupcoTrc;  from  a  Semitic word  meaning  ‘sunset,  evening’,  cp.  Asia.
19321:Derivative:  infer et  tial-ly,  adv. inferior,  adj.,  lower.  —  L.,  ‘lower  in  place,  under, nether’,  compar.  of  inferus.  See  infra  and  corn- par.  suff.  -ior.
24967:Naraka,  n.,  hell  ( Hinduism )  —  OI.  Narakah,  fr. I.-E.  base  *ner-,  ‘below;  to  the  left’,  whence  also Gk.  e-vspoi,  ‘those  below’,  e-vspffev,  ‘from  be¬ neath’,  vip-repo?,  c-vs pxepo;,  ‘nether,  infernal’, ON.  nordr,  OE.  nord,  ‘north’  (prop,  left,  when facing  east).  See  north.
25093:Nebuchadnezzar,  Nebuchadrezzar,  n.,  king  of Babylon  (604-562  B.C.E.).  —  Heb.  N^bhukhadh- netztzdr,  acollateral  (oimo(Nebhiikhadhretztzdr, fr.  Bab.  Nabu-kudurri-usur,  which  prob.  means lit.  ‘Nebo,  protect  the  boundary’.  Cp.  Gk.  Na- poxoSpooopo;  in  Strabo  15,1,6,  and  in  Josephus Flavius,  Contra  Apionem  1,146. nebula,  n.,  a  cloudlike  patch  in  the  sky  (astron.) —  L.,  ‘mist,  fog,  cloud’,  fr.  I.-E.  base  *(e)nebh-, ‘moist,  vapor,  mist,  cloud’,  whence'  also  OI. ndbhas-,  ‘vapor,  cloud,  fog,  sky’,  Avestic  nabah -, ‘air,  sky’,  Gk.  veipo?,  vcfpeXz],  ‘cloud,  mist’,  OS. nebal,  OFris.  nevil,  MDu.,  Du.  novel,  OHG. nebul,  MHG.,  G.  nebel,  ‘fog’,  ON.  nifl-  (in Niflheimr,  ‘abode  of  darkness’,  i.e.  ‘the  nether world’),  njol,  ‘night’,  OE.  nifol  (adj.),  ‘dark’, MW.  nyfel,  ‘cloud’,  W.  ttiwl,  Co.  niul,  ‘cloud, fog’,  OIr.  nem,  ‘sky’,  OSlav.  nebo  (gen.  nebese), ‘sky’,  Lith.  debesls  (for  *nebesis ),  ‘cloud’  (the d-  is  prob.  due  to  the  influence  of  dangits, ‘sky’),  Hitt,  nepish  (gen.  nepishash),  ‘sky’,  Aves¬ tic  napla-,  ‘moist,  humid’.  Cp.  nepheline,  nepho-, Neptune,  Nibelungs,  nimbus,  imbricate. Derivatives:  nebul-ar,  adj.,  nebul-iz-ation,  n., nebul-ize,  tr.  v.,  nebul-iz-er,  n.,  nebulous  (q.v.) nebulosity,  n.,  1)  condition  of  being  nebulous;  2) cloudiness;  3)  a  nebula.  —  F.  nebulosite,  fr. Late  L.  nebulositatem ,  acc.  of  nebuldsitas,  fr.  L. nebulosus.  See  nebulous  and  -ity. nebulous,  adj.,  1)  resembling  a  nebula ;  2)  clouded, cloudy,  misty;  3)  vague  —  L.  nebulosus,  ‘cloudy’, fr.  nebula.  See  nebula  and  -ous.
25295:See  nether  and  sedentary  and  cp.  eyas,  nidus, nidificate.  Cp.  also  nestle.
25303:net,  adj.,  free  from  all  deductions.  —  ME.,  fr. MF.  (=  F.),  ‘neat,  clean’.  See  neat,  pure’. Deriva'tive:  net,  tr.  v.,  to  gain  as  net  profit, nether,  adj.,  lower.  —  ME.  nethere,  nithere,  fr. OE.  neodera,  nidera,  ‘lower  ,  from  the  adverb neodor,  nider ,  ‘downward  ;  rel.  to  the  adverbs OS.  nithar,  ON.  nidr,  OFris.  milter,  Du.  neder, neer,  OHG.  nidar,  MHG.  nider,  G.  nieder (whence  the  adjectives  OS.  nithiri,  ON.  ned(ar)ri, Dan.,  Swed.  nedre,  OFris.  nithera,  Du.  neder , OHG.  nidari,  nidaro,  MHG.  nider(e),  G.  nieder ) ; prop,  comparatives  formed  fr.  I.-E.  *nl-,  down.
25473:Derivatives:  nit-t-er ,  n.,  nit-t-y,  adj. niter,  nitre,  n.,  nitrate  of  potassium  (chem.)  —  F. nitre,  fr.  L.  nitrum,  fr.  Gk.  vixpov,  ‘native  sodi¬ um  carbonate,  natron’,  fr.  Heb.  nether,  ‘carbon¬ ate  of  soda,  natron’  (stem  nithr-;  cp.  Aram. nithra).  Cp.  nitrogen,  natron, nithing,  n.,  a  cowardly  person  (archaic).  —  ME., fr.  OE.  niding,  ‘infamous  man’,  fr.  ON.  nidingr, fr.  nid,  ‘envy,  hatred’  (whence  also  Dan.  nid, ‘envy,  grudge,  jealousy’),  which  is  rel.  to  OE. nid,  ‘quarrel,  enmity,  hatred,  battle’,  OS.,  OFris. nith,  ‘hatred,  envy’,  Du.  nijd,  ‘envy’,  OHG.  nid, nidh,  nith,  ‘anger,  envy,  hatred’,  MHG.  nit,  nid, G.  Neid,  ‘envy,  grudge,  jealousy’,  Goth,  neifi, ‘ill-will,  envy,  jealousy’,  and  cogn.  with  OIr. nith,  ‘combat,  fight'.  Cp.  niddering. nitid,  adj.,  bright.  —  L.  nitidus,  ‘shining,  glitter¬ ing,  bright’,  fr.  nit  ere,  ‘to  shine’.  See  neat,  adj. niton,  n.,  a  chemical  element  —  A  Modi,  hybrid formed  on  analogy  of  argon  fr.  L.  nitere,  ‘to shine’  (see  neat,  adj.);  so  called  by  the  English chemist  Sir  William  Ramsay  (1 852- 1 9 1 6)  in  19 1 2, because  it  glows  in  the  dark, nitr-,  a  form  of  nitro-,  before  a  vowel, nitrate,  n.  (chem.),  1)  a  salt  of  nitric  acid;  2)  po¬ tassium  nitrate  or  sodium  nitrate.  —  Formed fr.  niter  with  chem.  suff.  -ate.
25619:north,  adv.,  n.  and  adj.  —  ME.,  fr.  OE.  nord,  adv., rel.  to  OS.  north,  adv.,  ON.  nor  dr,  OFris.  north, MDu.  nort,  noort,  adv.  and  n.,  Dan.  nord,  Swed. nord,  norr,  Du.  noord,  OHG.,  MHG.,  G.  nord, n.,  and  cogn.  with  OI.  narakah,  ‘hell".  Arm. nerk’in,  ‘the  lower  ODe’,  Gk.  e-vepoi,  ‘those below’,  E-vepffev,  ‘from  beneath’,  vlprspo^, E-vEpxspoi;,  ‘nether,  infernal’,  Oscan  nertrak, ‘left’,  Umbr.  nertru  (abl.  sing.),  ‘left’.  [OF.  north (F.  nord)  is  borrowed  fr.  OE.  nord.  It.  and  Sp. norte  are  French  loan  words.]  All  these  words are  derivatives  of  I.-E.  base  *ner-,  ‘left;  below’. Cp.  Nordic,  Norse  and  the  first  element  in  Nor¬ man,  Norwegian.  Cp.  also  Naraka.  For  sense development  it  should  be  borne  in  mind  that most  of  the  ancients  used  to  take  their  bearings by  turning  toward  the  rising  sun,  so  that  they had  north  to  their  left  hand.  Hence,  the  word denoting  north  in  many  languages  lit.  means
28265:Persephone,  n.,  the  wife  of  Hades  and  queen  of the  nether  world ;  identified  with  Kore,  the daughter  of  Zeus  and  Demeter  (Greek  mythol.) —  L.,  fr.  Gk.  Hepos^ovT].  See  person  and  cp. Proserpina.
28278:persistent,  adj.  —  L.  persistens,  gen.  -entis,  pres, part,  of  persistere.  See  persist  and  -ent. Derivative:  persistent-ly,  adv. person,  n.  —  ME.  persone,  persoun,  fr.  OF.  per- sone,  persoune  (F.  personae),  ft.  L.  persona , ‘mask,  masked  person,  character,  part,  role, person’,  which  prob.  derives  fr.  Etruscan  <persu, ‘masked  figure',  orig.  the  embodiment  of  a  god of  the  nether  world  whose  office  it  was  to  receive the  soul  of  the  dead  and  to  accompany  it  to
28282:Hades.  The  word  tpersu  itself  is  of  Greek  origin; cp.  Iloposcpovrj,  name  of  the  chief  goddess  of the  nether  world  (see  Persephone).  See  Franz Altheim,  Geschichte  der  lateinischen  Sprache, 328  ff.,  389.  Cp.  parson,  which  is  a  doublet  of person.
34959:Sheol,  n.,  the  grave,  hell.  —  Heb.  sheol,  ‘the netherworld’,  of  unknown  etymology, shepherd,  n.  —  ME.  schephirde,  schepherde, sheephirde,  sheepherde,  fr.  OE.  sceaphyrde. which  is  compounded  of  sceap,  ‘sheep’,  and hyrde,  ‘herdsman’.  See  sheep  and  herd,  ‘herds¬ man’.
35368:Sisyphean,  adj.,  resembling  the  labors  of  Sisy¬ phus.  —  Formed  with  suff.  -an  fr.  L.  Sisypheius, fr.  Gk.  Xtav-pEioc,  fr.  ’ZZcsoqo:.  See  next  word. Sisyphus,  n.,  a  crafty  king  of  ancient  Corinth, condemned  in  the  netherworld  to  roll  forever up  a  hill  a  rock,  which  constantly  rolled  down again.  —  L.,  fr.  Gk.  Elirjipop,  a  name  of  un¬ certain  origin.  Its  connection  with  0096?,  ‘wise, crafty’  (see  sophist),  is  based  on  folk  etymology. Stsyrinchium,  n.,  a  genus  of  plants,  the  blue-eyed grass  (hot.)  —  ModL.,  fr.  Gk.  anrjpLyy.ov,  a kind  of  plant,  which  is  of  uncertain  origin, sit,  intr.  and  tr.  v.  —  ME.  sitten,  fr.  OE.  sittan, rel.  to  OS.  siltian,  ON.  sitja,  Swed.  sitta,  Dan. sidde,  OFris.  sitta,  MDu.  sitten,  Du.  zitten, OHG.  sizzan,  MHG.,  G.  sitzen,  Goth,  sitan,  fr. Teut.  base  *set-,  corresponding  to  I.-E.  base *sed-,  ‘to  sit’,  whence  OI.  sidati,  ‘he  sits’,  Gk. E^Eaffai  (for  *sedyesthai),  ‘to  sit’,  s8px  (for *sedra),  ‘seat’,  L.  sedere,  ‘to  sit’,  sedes,  ‘seat’.  See sedentary  and  cp.  words  there  referred  to.  Cp. also  saddle,  seat,  set,  v.,  settle,  n.  and  v.,  soot and  the  second  element  in  Alsace  and  in  cosset. Derivatives:  sit,  n.,  sitt-er,  n.,  sitt-ing,  adj.
37164:Stygian,  adj.,  pertaining  to  the  Styx  or  the  nether world.  —  L.  Stygius,  fr.  Gk.  Sxiiyio?,  ‘Stygian’, fr.  2x-j;,  gen.  Sxoy<k,  ‘Styx  (a  river  of  the nether  world)’.  See  Styx  and  -ian. styl-,  form  of  stylo-  before  a  vowel, style,  n.,  1)  gnomon;  2)  part  of  the  pistil  bearing the  stigma  (bot.)  —  Gk.  axoXo?,  ‘pillar,  column’, rel.  to  otuclv,  ‘to  make  stiff,  erect;  to  place, set’,  fr.  I.-E.  base  *st(h)du-,  *st(h)u-,  ‘stiff,  up¬ right;  post,  pillar’.  See  steer,  ‘to  direct’,  and  cp. words  there  referred  to.
37184:Styx,  n.,  a  river  of  the  nether  world.  —  L.,  fr.  Gk. Lxu5,  gen.  Sxuyo?,  lit.  ‘the  horrible’,  rel.  to oxu;,  ‘chill,  frost;  hatred,  abhorrence’,  oxuyEiv, ‘to  hate,  abhor’  (orig.  ‘to  shudder  with  cold’), <yxuyv6<;,  ‘hated,  abhorred’,  and  cogn.  with Russ,  istygnut’,  stugnuf,  ‘to  freeze’.  Cp. — with -d-formative  element — OSlav.  studu,  ‘cold’, suable,  adj.  —  Formed  from  the  verb  sue  with suff.  -able.
38247:Tartarus,  n.,  the  abyss  below  Hades;  place  of punishment;  Hades,  netherworld;  hell  (Greek mythol.)  —  L.,  fr.  Gk.  Taprapoc,  prob.  a  word of  imitative  origin,  suggestive  of  something frightful.  Cp.  tartar.
40767:Derivatives:  underlie,  n.,  underli-er,  n. underneath,  adv.  and  prep.  —  ME.  undernethe,  fr. OE.  underneopan.  See  under  and  nether  and  cp. beneath.
```


## [2026-09-07T19:29:57.872Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '25303,25320p' KLN_1966.txt",
 "description": "Klein nether full"
}
```


### [2026-09-07T19:29:57.932Z] TOOL RESULT

```
net,  adj.,  free  from  all  deductions.  —  ME.,  fr. MF.  (=  F.),  ‘neat,  clean’.  See  neat,  pure’. Deriva'tive:  net,  tr.  v.,  to  gain  as  net  profit, nether,  adj.,  lower.  —  ME.  nethere,  nithere,  fr. OE.  neodera,  nidera,  ‘lower  ,  from  the  adverb neodor,  nider ,  ‘downward  ;  rel.  to  the  adverbs OS.  nithar,  ON.  nidr,  OFris.  milter,  Du.  neder, neer,  OHG.  nidar,  MHG.  nider,  G.  nieder (whence  the  adjectives  OS.  nithiri,  ON.  ned(ar)ri, Dan.,  Swed.  nedre,  OFris.  nithera,  Du.  neder , OHG.  nidari,  nidaro,  MHG.  nider(e),  G.  nieder ) ; prop,  comparatives  formed  fr.  I.-E.  *nl-,  down.
below’,  whence  OI.  ni,  ‘down’,  nitaram,  ‘down- wards’,  nica ,  ‘below,  down’,  nicah,  low  ,  Avestic ni,  ‘down’,  Arm.  ni,  n-,  ‘low’,  Gk.  veioUev,  ‘from below’,  vct6i ;  (scil.  yv)),  ‘field’,  prop,  ‘lowland  , OSlav.  ni-zu,  Tow,  down’,  ni-va,  ‘field’.  Cp.  I.-E. *ni-zdo-  (in  L.  nidus,  OE.  nest,  etc.),  ‘nest’,  lit.  ‘a place  to  sit  down  in’.  Cp.  nest,  nidus,  and  the second  element  in  Upanishad.  Cp.  also  beneath, underneath.
Nethinim,  n.,  pi.,  servants  who  performed  the lowest  service  under  the  Levites  in  the  Temple (Bible)  —  Heb.  nlthimm,  lit.  ‘those  given  (scil. to  the  sanctuary)’,  pi.  pass.  part,  of  ndthan,  ‘he gave’.  See  Nathan.
netsuke,  n.,  a  small  carved  object  of  ivory,  bone or  wood,  pierced  with  holes.  —  Jap.
Nettapus,  n.,  a  genus  of  very  small  geese,  the pygmy  goose  ( ornithol .)  —  ModE.,  compound¬ ed  of  Gk.  vrjTxa,  ‘duck’,  and  rcouc;,  gen.  noSot;, ‘foot’.  See  next  word  and  podal  and  cp.  the  sec¬ ond  element  in  Nesonetta.
Nettion,  n.,  a  genus  of  ducks,  the  teal  (ornithol)
—  ModL.,  fr.  Gk.  w,tt1ov,  dimin.  of  v^xxa, Att.  form  of  vrjaaa,  ‘duck’,  which  is  cogn.  with L.  anas,  ‘duck’.  See  Anas  and  cp.  prec.  word.
nettle,  n.  —  ME.  netle,  netel,  fr.  OE.  netle,  netele, netel,  rel.  to  OS.  nett  la,  dial.  Swed.  ndtla,  Norw. netla,  MDu.  netele,  netel,  Du.  netel,  OHG. ne33ila,  MHG.  ne33el,  G.  Nessel,  fr.  Teut.  base *natilon,  dimin.  of  *naton,  which  appears  in Icel.  notu  (gras),  Norw.  brenne-nata,  OHG. na33a,  ‘nettle’.  These  words  prob.  meant  orig. ‘the  textile  plant’,  and  are  derivatives  of  I.-E. base  *ned-,  ’to  twist,  tie,  knot’,  whence  also  Olr. ne-naid,  ‘nettles’,  and  possibly  also  Gk.  aSixvj, ‘nettle’  (if  derived  fr.  * nd-ika).  See  net,  n. neume,  also  neum,  n.,  musical  notation,  indi¬ cating  the  melody  to  be  sung  to  a  final  syllable (med.  music).  —  F.  neume,  fr.  ML.  neuma,  fr. Gk.  7iv£npa,  ‘breath’.  See  pneuma. neur-,  form  of  neuro-,  before  a  vow'ei. neural,  adj.,  pertaining  to  a  nerve  or  to  the  nerves.
—  Formed  with  adj.  suff.  -al  fr.  Gk.  vsdpov, ‘nerve’.  See  neuro-.
neuralgia,  n.,  pain  along  the  course  of  a  nerve (med.)  — ■  Medical  L.,  compounded  of  neur-  and Gk.  -aXvia,  fr.  SXvo c,  ‘pain’.  See  -algia. neuralgic,  adj.,  pertaining  to  neuralgia.  —  Form¬ ed  from  prec.  word  with  adj.  suff.  -ic. neurasthenia,  n.,  nervous  exhaustion  (med.)  — Medical  L.,  lit.  ‘weakness  of  the  nerves',  fr. neur-  and  Gk.  aoftcvcia,  weakness  .  See  as¬ thenia.
neurasthenic,  adj.,  suffering  from  neurasthenia.
_ Formed  from  prec.  word  with  adj.  suff.  -ic.
Derivative:  neurasthenic,  n. neuration,  n.,  nervation.  —  A  hybrid  coined  fr. Gk.  veupov,  ‘nerve’  (see  nerve),  and  -ation,  a suff.  of  Latin  origin.  The  correct  form  is  ner¬ vation  (q.v.)
neurectomy,  n.,  excision  of  a  nerve  (med.) Compounded  of  neur-  and  Gk.  -exxopia,  ‘a  cut¬
ting  out  of’,  fr.  sxxoprj,  ‘a  cutting  out’.  See -ectomy.
neurilemma,  n.,  the  sheath  covering  a  nerve  fiber (anat.)  —  Medical  L.,  fr.  neurilema,  a  word coined  by  the  German  anatomist  John  Christian Reil  (1759-1813)  fr.  Gk.  veupov,  ‘nerve’,  and >5jpa,  ‘will,  desire,  purpose",  which  was  con¬ fused  with  Xsppa,  ‘rind,  cover’  (lit.  ‘that  which is  peeled  off’).  The  correct  form  should  have been  neurolemma  (cp.  the  numerous  compounds beginning  with  neuro-).  See  neuro-  and  lepto-. neurine,  n.,  a  poisonous  ptomaine  obtained through  the  putrefaction  of  flesh,  C5H13ON (chem.)  —  Formed  fr.  neur-  with  chem.  suff. -ine.
neuritic,  adj.,  pertaining  to,  or  having,  neuritis.
—  See  next  word  and  adj.  suff.  -ic. neuritis,  n.,  inflammation  of  a  nerve  or  nerves
```


## [2026-09-07T19:30:06.797Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=25250 && NR<=25400' KLN_1966.txt | grep -n \"^[0-9]\\{3,4\\}\" | head -20; echo \"=== formfeeds count before\"; python3 - <<'EOF'\nt=open('KLN_1966.txt',errors='replace').read().split('\\n')\n# find lines that are pure numbers around\nimport re\nfor i in range(25100,25500):\n    if re.match(r'^\\s*\\d{3,4}\\s*$', t[i]):\n        print(i, t[i])\nEOF",
 "description": "Find page numbers in Klein OCR"
}
```


### [2026-09-07T19:30:08.123Z] TOOL RESULT

```
145:1046
=== formfeeds count before
25129 1036
25194 1039
25233 1040
25393 1046
```


## [2026-09-07T19:30:15.000Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Root / lemma: nī\" POK_full.txt | head; echo \"==A==\"; grep -n \"nizdo\\|ni-zd\\|nisd\" POK_full.txt | head; echo \"==B==\"; grep -n \"Meaning: nieder\\|Meaning: down\" POK_full.txt | head",
 "description": "Pokorny search ni"
}
```


### [2026-09-07T19:30:15.093Z] TOOL RESULT

```
==A==
72383:Armenian nst/m's\t, put myself (perhaps„/b-Praes. *ni-zdjd)\ hecanim^s\\. auf, reite' {c 
72522:ni-zd-os, -o/77'nest' (prefix /?/■ "low, base', or 'ein-' as "place zum Nieder- or Einsitzen'): 
==B==
```


## [2026-09-07T19:30:19.143Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && head -40 POK_full.txt; echo \"=== grep style\"; grep -c \"Root / lemma\" POK_full.txt POK_01.txt POK_02.txt POK_03.txt 2>/dev/null",
 "description": "Inspect POK file format"
}
```


### [2026-09-07T19:30:19.201Z] TOOL RESULT

```
List of language abbreviations in tlie lED 



Abbreviation Language name 


Aeq. 




Aequian 


Akk. 




Akkadian 


Alan. 




Alanian (=Old Ossetic) 


Alb. 




Albanian 


Anat. 
=== grep style
POK_01.txt:0
POK_02.txt:0
POK_03.txt:0
POK_full.txt:2231
```


## [2026-09-07T19:30:22.965Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Root / lemma: n\" POK_full.txt | sed -n '1,80p'",
 "description": "Pokorny n- lemmas"
}
```


### [2026-09-07T19:30:23.015Z] TOOL RESULT

```
26585:Root / lemma: neuos, -ios: new' + Root/ lemma: oRtd(u)\ eight'. 
56651:bark, outer covering of a tree, pod ' derived from *na/<{u), /a/<{u) of Root / lemma: nohg"-, 
56680:bark, outer covering of a tree, pod ' derived from *nak{u), laH^U) of Root / lemma: nohg"-, 
61762:Root / lemma: nak- 
61773:Root / lemma: nana, nena etc. 
61871:Root / lemma: nag^h- {* he-nag''h-) 
61883:Root / lemma: na-1{*he- na-1) 
61897:Root / lemma: na-2 {* he-na-2) 
61909:Root / lemma: nau-2: nau- : nu- {*he- nau-2) 
61944:Root / lemma: naus-1 {* he-nahus-1) 
61998:Root / lemma: ndo'^-l {*he- ndo^-f) 
62012:Root / lemma: ndo'^-2{*he- ndo^-2) 
62018:Root / lemma: ned-1 : ned- {*he- noud-1) 
62077:Root / lemma: ned-2{*he- ned-2) 
62109:Root / lemma: nedo- {*he- nedo-) 
62123:Root / lemma: negh- {*he- negh^ 
62133:Root / lemma: neid-1{*he- neid-f) 
62154:Root / lemma: neid-2: nid- {*he- neid-2) 
62162:Root / lemma: ned-2\ "to sound, roar, etc...' : Root/ lemma: neid-2. nid-\ "to flow, stream' 
62176:Root / lemma: neig"- {^hoing"^ 
62207:Root / lemma: neik- {*hoink-) 
62239:Root / lemma: nei-1, neie-. nT-{*hoin^ 
62257:Root / lemma: nei-2, neie- : m- {*hoin-) 
62277:Root / lemma: ne/-3, ni- {*houn-) 
62286:Root / lemma: neR- {*hounR-) 
62333:Root / lemma: nelc-fl-), nolc-t-s {* hounk'*-(t-}) 
62400:Root / lemma: ne1, ne, nei{*houn) 
62455:compound of Root / lemma: nel, ne, ne/: negative particle + Root/ lemma: Ar"©! : and 
62497:Root / lemma: ne-3, no-, Plur. nes-, nds-{*hounks-) 
62524:Root / lemma: nem-1 {*he- nem-f) 
62575:Root / lemma: nem-2 {* he- nem-2) 
62600:Root / lemma: nepot- {*he- nemot^ 
62647:Root / lemma: ner-1(t)-, aner- {aner-1) {*he- ner-1(t)-) 
62734:Root / lemma: ner-2{*he- ner-2) 
62751:Root / lemma: ner-3{*he- ner-3) 
62783:Root / lemma: nes- {*he- nes-) 
62820:Root / lemma: neu-6^- {*he- neu-dy-) 
62835:Root / lemma: neu-d- {*he- neu-d-) 
62863:Root / lemma: neu-ks-, neu-s- {*he- neu-ks-) 
62892:Root / lemma: neuk- {*he- neuk-) 
62910:Root / lemma: neu-1{*he- neu-f) 
62924:Root / lemma: neu-2{*he- neu-2) 
62953:Root / lemma: neuos, -ios i*he- neuos, -/os) 
62988:Root / lemma: neik- : nlk- : nik- {*he- neik-) 
63049:Root / lemma: niz-do- {*he- niz-do-) 
63054:Root / lemma: nog^o- or nag^o- {*he- nag^o-) 
63066:Root / lemma: nog"-, nog''od(h)o- nog^-no- {*he- neg^o^ 
63108:Root / lemma: nok^-(t)- {*he- nek^-Ct)-) 
63112:Root / lemma: no- {*he- no-) 
63119:Root / lemma: nomp {*he- nomp) 
63125:Root / lemma: not- not- {*he- not-) 
63139:Root / lemma: nu- {*he- nu-)
```


## [2026-09-07T19:30:28.589Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '62277,62290p' POK_full.txt; echo \"===== nizdo\"; sed -n '63049,63055p' POK_full.txt",
 "description": "Print Pokorny nei-3/ni- and niz-do-"
}
```


### [2026-09-07T19:30:28.657Z] TOOL RESULT

```
Root / lemma: ne/-3, ni- {*houn-) 



See also: see above S. 312 f. {en-). 
Page(s): 760 



Root / lemma: neR- {*hounR-) 

Meaning: death, dying; dead person 

Material: Old Indie nasyati, nasati^ gets lost, disappears, passes away ', nasayat/" makes 
===== nizdo
Root / lemma: niz-do- {*he- niz-do-) 
Meaning: nest' 
See also: see below sed-. 
Page(s): 769 

Root / lemma: nog^o- or nag^o- {*he- nag^o-)
```


## [2026-09-07T19:30:39.914Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Root / lemma: en-\" POK_full.txt | head; echo ===; grep -n \"Page(s): 311\\|Page(s): 312\\|Page(s): 311-314\\|Page(s): 312-314\" POK_full.txt | head",
 "description": "Pokorny en- lemma"
}
```


### [2026-09-07T19:30:39.972Z] TOOL RESULT

```
Exit code 1
26860:Root / lemma: en-2 
36219:n. year' prove that Root / lemma: en-2\ year' : Root/ lemma: at-, *atno- : "to go; year' : 
(eval):1: == not found
```


## [2026-09-07T19:30:43.266Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Root / lemma: en\" POK_full.txt | head -20; echo \"----\"; grep -n \"Page(s): 31[0-5]\" POK_full.txt | head -20",
 "description": "Pokorny en lemmas and page 311-315"
}
```


### [2026-09-07T19:30:43.327Z] TOOL RESULT

```
26411:Root / lemma: eneR-, neR-, enR-, nR- {*henek-) 
26618:Root / lemma: eng"-, gg^en {eng^h^ 
26659:Root / lemma: en1 {*hen1) 
26860:Root / lemma: en-2 
26895:Root / lemma: en(o)mQ-, (o)nomQ, nomij, {*hien h3(o)mij^ 
26945:Root / lemma: enos-or onos- 
27074:Root / lemma: eng-, onq- {*hok-) 
27124:Root / lemma: ent- {better ant-1) {*h-ent) 
29298:Root / lemma: eneu, enu 
29321:Root / lemma: en 
36219:n. year' prove that Root / lemma: en-2\ year' : Root/ lemma: at-, *atno- : "to go; year' : 
----
26251:Page(s): 310-311 
26305:Page(s): 314-315 
26409:Page(s): 315-316 
26858:Page(s): 311-314
```


## [2026-09-07T19:30:46.363Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '26659,26860p' POK_full.txt",
 "description": "Print Pokorny en-1 entry pp.311-314"
}
```


### [2026-09-07T19:30:46.413Z] TOOL RESULT

```
Root / lemma: en1 {*hen1) 

Meaning: in, *into, below 

Note: (: % Slavic also *ori7)\ em, n(e)i, perhaps also ^^/(ending as epi dol^ieic. perhaps 

related to Lok. in -/; if if not even created after it). 

Material: Old Indie in anika- n. " front ' (= Avestan ainika-6s.) from *eni-oq"'-, 



*/?/■ in Old Indie ni-Ja-^ inborn, inherent, fixed, own ', Avestan ni-zanta-^ innate, natural ', 
Old Indie nf-tya-^ continuous, fixed, own ' = gall. Nitio-broges, VN (contrast to Allo-broges) 
= Gothic /7/^/s "kinsman, relative'. Old Norse /?/(?/' "kinsman, relative'. Old English niddas 
PI. " men, people', also in verbal prefix Aryan ni- "in, into', e.g. Old Indie nfgam-, Avestan 
n/gam-^enter into a condition'; 

Armenian /(before vowel /and n-) from */n, older *en "in', adnominal m. Lok. and Akk.; 

gr. £v, dial, iv and (poet.) svi, evi (so hom. always as postposition; Attic only more £vi as 
predicate = svsgti) "in', adnominal with Dat. (= Lok.), Gen. and in part also still with Akk. 
("whereto, where'), in latter meaning elsewhere after £^ to ivq (Attic z\q; thereafter siau) 
extended as £^u), anti conservative out of it tq); zero grade a- {n) e.g. in a-A£yu) etc.; 

about the debatable egte, evte " until ' s. Schwyzer Gr. Gr. I 629 f.; 

maked. iv; 

Messapic /n; 

alb. //T/" until, in ' {*en/); 

Latin //?, oldest err, Oscan en, Umbrian en- {en-dendu^ stretch out, reach forth, extend 
'), postposition Oscan -en, Umbrian-e/r?, -e, adnom. with Dat. (= Lok.), Akk. and Gen. (of 
ambit); 

Old Irish //7-"in' adnominal m. Dat. and Akk.; nasalized), in- (derived from *eni, compare 
/ngenirom proto Irish //7/-^e/75 "daughter'; mixed with /nd-= gall, ande-, s. Thurneysen 
Grammar 531 f., Pedersen KG. I 45), acymr. abret. en, //7"in', corn. bret. en, ncymr. yn-, 
gall, essedon {*en-sedon) " chariot ', embrekton^ immersed (swallowed) bite ' (see below 
mereq-); 

Gothic //7"in', adnom. m. Dat., Akk., Gen.; Old High German Old Saxon Old English in. 
Old Norse /""in', adnom. m. Dat. and Akk., from *e/7/ (about derivatives as Gothic inn^\n, 
into', inna, innana, probably from *eni-n-, s. Brugmann IF. 33, 304 f.); (under the influence 
of common Celtic -ns-, -nt- > -nn-). 

Old Prussian e/7"in', adnom. m. Dat. and Akk., Latvian /e-(only prefix); zero grade */7in 
Lithuaniany~(older and nowadays dial, in, int) "in', adnom. m. Lok. and Akk.; 

Old Church Slavic on-{on-usta^ footwear', p-o'o/i. "valley'), zero grade vbn-, i/b"in', 
adnom. m. Lok. and Akk.; 



Tocharian AB y-, yn-, B in- (only prefix). 

^-dh/;Old Indie adhi^aboui, on', Old pers. ao'/j/'in'; gall, intensive prefix /4/7ofe-(PN 
Ande-roudus^ the very red '), cymr. an{ne)- in anne-T contrivance ' (common Celtic -ns-, - 
nt- > -nn-) = Old Irish /nde-/{*n6^/-/-om), cymr. an-daw^ eavesdrop ' (to taw^ 
closemouthed '); Old Irish ind- (partly from *indi-, partly from secondary *indo) in ind-reth " 
incursion ' {*indi-reto-), indnaide {see further under), etc. Pedersen (KG. I 45) will also 
place here Gothic und'up to'; s. about other possibilities above S. 50 and S. 1 81 . 

(ejnero-' inner': Armenian *nero-' the inside ', assumed from ner- ' within, in, into', 
nerk's' inside ', nerk'oy' inside, within '; perhaps gr. svspoi as " those below, those 
beneath the earth, of the dead and the gods below ', namely in the earth; or better 
Hypostase from oi £v spg? 

/?/-, /7e/-"low, base', comparative nitero-\o^' (in contrast to " upper '): 

Old Indie nf, Avestan nf down; downward ', Old Indie nitaram^ underneath ', Avestan 
nitama- " the lowest '; 

Armenian ni-, n- "low'; 

Celtic */7efrom */7e/in Old Irish ar-neut-sa, in-neut-sa^ I expect, anticipate ', (Proto Irish 
*-ne-sedLJ), verbal noun indn(a)ide ( *indo-ne-sodJon) and in ar-neigdeV\.o pray' ( *ari-ne- 
gedont); compare different Bergin Eriu 10, 111; 

Old High German nidar. Old Saxon nithar. Old English niPer, Old Icelandic nidr^ down; 
downward ', Old High German nidana. Old Saxon n/thana ' under' , Old English neodan, 
n/Pan 'down, downward, under'. Old Icelandic nedana' from here below ', preposition with 
Akk. "below'. Old Saxon nitheMv. 'under'. Old High German /7/b'a preposition with Dat. 
and Akk. "below, under'; 

Old Bulgarian nizh " down, downwards ' (formation as pre-zh etc.); 

in compound: 

Old Indie nTpa- " low lying ' {ni+ ap- "water'); 

*ni-ok"-as " holding down the eyes ' in: 

Old Indie mca' downwards ' (compare nyanc-' pointed down '); 



Old Bulgarian nicb " inclined forward, stooping forward; rushing down or past; 
precipitous, steep; inclined, well-disposed, favorable; easy ', {* po-niknqti) poniknqti, nicatT 
be inclined '; Wackernagel-Debrunner Old Indie Gr. Ill 230 f., Trautmann 198 f. 

with formants -uo-: 

gr. vEioc; f. "field, entryway ' (*lowland, depression'), vsiaroq, veqtoc; "the uttermost, 
lowest, extreme, outermost ', veioGev "from under, from the bottom ', veIoGi "below, at the 
bottom ', vsiaipa yaarrip " the lower part of the belly ', vniara saxara, KaTcbTara Hes., theb. 
NniTTQi nuAai (n seems to stand for efrom e/before pal. vowel); 

Old Bulgarian /7/V5 "farmland' ("*lowland, depression'), Serbo-Croatian /7y7Va (whence y?), 
Czech russ. /7/Vads. {*neiuaVj\ 

zero grade Old English neowol, neol, nihor inclined forward, stooping forward; rushing 
down or past; precipitous, steep; inclined, well-disposed, favorable; easy ' from *niwol. 
Middle Low German n/ge/'\o\N, base'; 

here probably also with full grade Lithuanian /7e/Vc»//"torment, smite', Latvian nievaV 
disdain, scorn ' (also Gothic *naiw^ eveTxsv ' Marc. VI 19?). 

Maybe alb. A7/Ve/" levelled ground'? 

compare Indo Germanic /7/-zo'c»s"nest' under 5e(/-"sit, place'. As "run down, tell off, 
rebuke' (as Latvian nievat) based on probably also neid- " reproach, rebuke, censure, 
blame, esp. by word ', neit-^ to be hostile towards, attack ' neiq-{see there), in ne/-, n/-. 

enter, pter' between - in', en-tero- " inward ': 

Old Indie antar, Avestan antars. Old pers. antar' between ', adnom. with Lok., Instr., 
Akk., Gen.; Old Indie antara- " internal ', Avestan antara- " inner ', Superl. Old Indie 
antama-'t\r\e closest ' (not to ant/, anta-), Avestan antsma-^ the most internal, intimate, 
inmost '; Old Indie antra-, also with Vrddhi antra- v\. " intestines, entrails '; 

Armenian 9nder-k'P\. " intestines, entrails ' (gr. loanword ? s. HiJbsehmann Arm. Gr. 
1447 f.); 

gr. EVTspov, mostly PI. ' intestines, entrails '; 

alb. nder, nder^ between, in', further ndjer, ngjereic. "until' {*entero-)\ (common Slavic 
dz\ Albanian dj, gl, ^yallophones) 



Latin enter, inter^ prep, with ace. between, among, amid; during, in the course of ', 
adnom. m. Akk. (solidified m. Gen. intervias, interdius), intro, intra, intrin-secus, interus^ 
internal ', interior, intimus, in tes tin us {see below), Oscan Entraf^* Interae ', zero grade, 
Oscan anter^ between, among, amid; during, in the course of, Umbrian anter, ander 
"during', adnom. m. Lok. and Akk.; 

Old Irish eter, etir, etar^ between ', adnom. m. Akk., corn, ynter, yntre, bret. entre{\.\\e 
ending after tre-, dre= cymr. trwy), acymr. ithr^ between, among, amid; during, in the 
course of; gall, inter ambes 'bebNeen streams'; 

Old High German untaretc. "under = between' = Oscan a/7/e'/'(differentfrom Germanic 
* under. Old High German etc untar'be\o\N' from *nd'^er, Latin infra); compare Gothic 
undaurni-mats ' lunch ' = " breakfast ', Old Norse undornn. "morning (at nine clock)'. Old 
Saxon undorn. Old English i//7o'e/77 "midday'. Old High German ^/7/o/77 "midday, lunch' (/?- 
suffix as in Latin internus); zero grade as gr. svTspa etc. Old Norse idrarP\. " intestines, 
entrails ' (from *innrar, *int^erdz), innre, idre^\he inner' (if not specific nord.-zio- has 
derivatived from inn= Gothic //7/7"hinein', see above); (under the influence of common 
Celtic -ns-, -nt- > -nn-). 

Slavic *§tro\n Old Church Slavic y^/AO "liver', ablaut, gtroba^ywer, *intestines, cavity of 
the body', gtrt ' eigw '. 

about Hittite anturiias^ inner, interior ', andurza^ inside, within ' s. Lohmann I. F. 51, 320 
f. 

Note: 

The inanimate suffix -ur-: Hittite anturiias^ inner, interior ' : 'lAAupioi , oi, lllyrians, 'lAAupia , 
n, lllyria, also'lAAupi? , n. Adj. 'lAAupiKO? , n, 6v, lllyrian: -Kr), the region or province of lllyria, 
lAAupi^U) , speak the lllyrian language, 'IAAupia:--hence Adv. 'lAAupiaii. 

e/7/'d5"(from) inside ' (compare Old Indie /-/a/? "from here', Latin caeiitus eic): 

gr. EVTOc; " inside ', whereof evtog-Gev, -0i and further evtogGiq, £VToa9i5ia " intestines, 
entrails ' (or latter with from svtogGs lengthened in 9 for *£VTOGTia, compare Old Indie 
antastya-r\. " intestines, entrails ', Pick I"* 363, Vendryes Rev. et. gr. 23, 1910, 74); 

Latin intuslrom inside, within; inside ', therefrom with analog metathesis intestmus 
"inward, internal; n. as subst., sing, and plur. the intestines'; 



Middle Low German Modern High German dial, inser^ eatable internal parts of animals 
', Old Norse Tstru., Tstrai., " the fat surrounding the intestine ' {*en-s-tro-)\ 

Old Prussian /nstran lat', Latvian ?striP\. " kidneys' {*en-s-tro-)\ Latvian leksa^ Inneres ', 
PI. ' intestines, entrails ' {*en-t-Ja), Old Lithuanian //75C/c»5 "heart', Lithuanian /sc/bs" 
intestines, entrails ' ( *en-s-tio-). 

About die compression Latin endo, indu^\v\\ wherefore gr. to £v5Tva, Old Irish inne^ 
intestines, entrails ', (common Celtic -ns-, -nt- > -nn-), see above S. 182 - About gr. £v-5ov 
"*in the house, indoors' (wherefore £v5o-0£v, -9i, Lesbian Doric £v5oi after oiko-0£v, -9i, 
oiKoi) s. dem-io build'. 

References: WP. I 125 ff., II 335 f., WH. I 687 f., 694, 708 f., 71 1 f., 870, Trautmann 69 f., 
198 f. W. Schuize Kl. Schr. 70 ff. 
Page(s): 311-314 

Root / lemma: en-2
```


## [2026-09-07T19:30:55.220Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^ni\\.\\|^ni-\\|\\bni-\\. \\|ni\\. Down\" AHD_watkins1985.txt | head -20; echo \"=== search 'Down. 1'\"; grep -n -i \"nizdo\\|ni-zdo\" AHD_watkins1985.txt | head",
 "description": "AHD Watkins ni-"
}
```


### [2026-09-07T19:30:55.327Z] TOOL RESULT

```
787:animal: NEAT2; b. compound form *ga-nauta- (*ga-, with, together; see kom), “he with whom one shares possessions,” companion, fellow, in (i) Middle Dutch ghenét, noot, fellow: MATELOTE (ii) Old High German ginéz, companion, in German Eidgenosse, confederate: HuGuEnot. [Pok. neu-d- 768.] newn. Nine. 1. Germanic *niwun, with variant *nigun, in Old English nigon, nine: NINE, NINETEEN, NINETY, NINTH. 2. Latin novem, nine (< *noven, with m for n by analogy with the m of septem, seven, and decem, ten): NOVEMBER, NOVENA; NONAGENARIAN. 3. Ordinal form *neweno- in Latin nénus, ninth: NONA-, NONES, NOON; (NONAGON), (NONANOIC ACID). 4. Prothetic forms *enewn, *enwn in Greek ennea, nine (> *ennewa, *enwa-): ENNEAD. [Pok. e-neuen 318.] newo-. New. Related to nu-. 1. Suffixed form *new-yo- in Germanic *neuja- in: a. Old English néowe, niwe, new: NEw; b. Old Norse njyr, new: SPAN-NEW. 2. Basic form *newo- in Greek newos, neos, new: NEO-, NEON, NEOTER- IC; MISONEISM. 3. Suffixed form “new-aro- in Greek nearos, young, fresh, contracted into néros, fresh (used of fish and of water), hence néron, water: ANEROID. 4. Basic form *newo- in Latin novus, new: NOVA, NOVATION, NOVEL!, NOVEL?, (NOVELTY), NOVICE; INNOVATE, REN- OVATE. 5. Suffixed form *new-er-ko- in Latin noverca, stepmother (< “she who is new”): NOVERCAL. [Pok. neuos 709.] ni. Down. 1. Suffixed form *ni-t- in Germanic *nith- in Old English nithan, neothan, below: BENEATH, UNDER- NEATH. 2. Suffixed (comparative) form *ni-tero-, lower, in Germanic *nitheraz in Old English nither, lower: NETHER. See compound root nizdo-. [In Pok. 1. en 311.] [niké. Victory. Greek noun of unknown origin. NIKE.] nizdo-. Bird’s nest. Compound root formed from ni + *sd-, zd-, zero-grade form of sed-; literally, “place where the bird sits down.” 1. Germanic *nist- in: a. Old English nest, nest: NEST; b. Germanic ‘*nistilon in Old English nestlian, to make a nest: NESTLE. 2. Latin nidus, nest: NICHE, NIDE, NIDUS; EYAS, NIDIFY. [In Pok. sed- 887.] nobh-. Also ombh-. Navel; later also “central knob,” boss of a shield, hub of a wheel. 1. Germanic *nabo in: a. Old English nafu, nafa, hub of a wheel: NAVE?; b. compound *nabé-gaizaz, tool for piercing wheel hubs (*gaizaz, spear, piercing tool; see ghaiso-), in Old Eng- lish nafogar, auger: AUGER. 2. Variant form *ombh- in Latin umbé, boss of a shield: uMBO. 3. Suffixed form *nobh-alo- in Germanic *nabalé in Old English nafela, navel: NAVEL. 4. Suffixed variant form *ombh-alo- in: a. Latin umbilicus, navel: UMBILICUS; NOMBRIL; b. Greek omphalos, navel: OMPHALOS. [Pok. 1. (enebh-) 314.] nogh-. Also enogh-, ongh-. Nail, claw. 1. Suffixed (diminutive) form *nogh-ela- in Germanic *nagla- in Old English negl, nail: NAIL. 2. Form *onogh- in Greek onux (stem onukh-), nail: ONYX; PARONYCHIA, PERIONYCHIUM, SARDONYX. 3. Variant form *ongh- in Latin unguis, nail, claw, hoof, with diminutive ungula, hoof, claw, talon (< ongh-eld-): UNGUIS. [Pok. onogh- 780.] nogv-. Naked. 1. Suffixed forms *nog’-eto-, *nog’-oto- in Germanic *nakweda-, *nakwada- in Old English nacod, naked: NAKED. 2. Suffixed form *nog~-edo- in Latin niidus, naked: NUDE, NUDI-; DENUDE. 3. Suffixed form *nog’-mo- differentiated or developed into Greek gum- nos, naked: GYMNASIUM, GYMNAST; GYMNOSOPHIST, GYMNOSPER\M. [Pok. nog¥- 769.] no-men-. Name. Earlier form *()noo-mn, zero-grade form *(g)na-men-. 1.Germanic *nam6n- in Old English nama, name: NAME. 2. Latin némen, name, reputation: NOMINAL, NOMINATE, NOUN; AGNOMEN, COGNOMEN, DENOMINATE, IGNOMINY, MISNOMER, NOMENCLATOR, NUNCUPATIVE, PRAENOMEN, (PRONOUN), RENOWN. 3. Greek onoma, onuma, name: ONOMASTIC, -ONYM, -ONYMY; ANONYMOUS, ANTONOMASIA, EPONYM, (EPON- YMOUS), EUONYMUS, HETERONYMOUS, HOMONYMOUS,
1172:*wer-ald., “life or age of man” (*-ald-, age; see al-3), in Old English weorold, world: woRLD; c. Frankish *wer- wulf, “man-wolf” (*wulf, wolf; see wikvo-), in French garou, werewolf: LOUP-GAROU. 2. Latin vir, man: VI- RAGO, VIRILE, VIRTUE, (VIRTUOSA), (VIRTUOSO); DECEM- VIR, DUUMVIR, TRIUMVIR. 3. Possibly Latin ciria, curia, court, if regarded as from *co-vir, “men together” (co-, together; see kom): CURIA. [Pok. uiro-s 1177.] wleik-. To flow, run. Zero-grade form *wlik-. 1. Adjective *wlik-u-, wet, in: a. suffixed form *wlik-w-d- in Latin liquare, to dissolve: LIQUATE; b. suffixed form *wlik-w-é- in Latin liquére, to be liquid: LIQUESCENT, LIQUID, LIQUOR; DELIQUESCE, LIQUEFY. 2. Suffixed form *wlik-s- in: a. Latin lixa, lye: LIXIVIATE; b. Latin prélixus, poured forth, stretched out in front, extended (pro-, forth; see per’): PROLIX. [In Pok. leiku- 669.] wlkwo-. Wolf. 1. Germanic *wulfaz in: a. Old English wulf, wolf: WOLF; b. Middle Dutch wolf, wulf, wolf: AARDWOLF; Cc. Old High German wolf, wolf, in German Wolfram, tungsten: WOLFRAM; d. Frankish *wulf, wolf (see wi-ro-). 2. Taboo variant */upo- in Latin lupus, wolf: LOBO, LUPINE!, LUPINE?; LOUP-GAROU. 3. Taboo variant *luko- in: a. Greek lukos, wolf: LYCANTHROPE, LYCOPO- piuM; b. Suffixed form */uk’-ya in Greek lussa, martial rage, madness, rabies (“wolf-ness”): LYTTA; ALYSSUM. [Pok. ulkvos 1178.] wip-6-. Fox. 1. Latin vulpés, fox: VULPINE. 2. Taboo variant *slépek- in Greek alépéx, fox: ALOPECIA. [Pok. ulp-, lup- 1179.] wogYh-ni-. Plowshare, wedge. 1. Probably Germanic *wagjaz in Old English wecg, wedge: WEDGE. 2. Prob- ably Latin vdmer, plowshare: vOMER. [Pok. wog¢hni-s 1179.] wokso-. Wax. Related to weg-!. Germanic *wahsam in Old English wex, weax, wax: WAX!. [Pok. uokso- 1180.] wopsa. Wasp. Metathesized form *wospd. 1. Germanic *wosp- in Old English wesp, weps, wasp: wAsP. 2. Latin vespa, wasp: VESPIARY. [Pok. yobhsd 1179.] wos. You (plural). Latin vds (> Old French vous), you: RENDEZVOUS. [In Pok. 1. iu- 513.] wrad-. Branch, root. I. Basic form *wrdd- in Germanic *wrét- in Old Norse rét, root: ROOT!; RUTABAGA. II. Zero-grade form *wred-. 1. Germanic *wurtiz in: a. Old English wyrt, plant, herb: wort; b. German Wurzel (< *wurzwala, rootstock; *-wala, a roll, round stem; see wel-3), root: MANGELWURZEL. 2. Latin rddix, root: RACE3, RADICAL, RADICLE, RADISH, RADIX; DERACI- NATE, ERADICATE. 3. Suffixed form *wrod-mo- in Latin rdmus, branch: RAMOSE, RAMUS; RAMIFY. 4. Suffixed reduced form *wr(e)d-ya perhaps in Greek rhiza, root: RHIZO-, RHIZOME; COLEORHIZA, LICORICE, MYCORRHIZA. [Pok. ufe)rad- 1167.] wragh-. Thorn, tip. Greek rhakhis, ridge, spine: RACHIS. [Pok. 1. uragh- 1180.] wreg-. To push, shove, drive, track down. I. Basic form *wreg- in Germanic *wrekan in: a. Old English wrecan, to drive, expel: WREAK; b. Old Norse rek (older form urek), wreckage, akin to the Scandinavian source of Anglo-Norman wrec, wreck: WRECK. II. O-grade form *wrog-. 1. Germanic *wrakjén-, “pursuer, one pursued,” in: a. Old English wrecca, exile: WRETCH; b. Frankish *wrakjo, “one pursued, an exile,” perhaps in French garce, a girl: GASKET. 2.Germanic *wrakaz in: a. Old English wrzc, exile, punishment, and Middle Dutch wrak, wreckage: WRACK}; b. Swedish rak, wreckage, akin to the source of Middle English rak, mass of driven clouds: RackK®. III. Zero-grade form “wrg-eyo-, “urg-eyo- in Latin urgére, to urge, drive: URGE. [Pok. ureg- 1181.] wrég-. To break. Suffixed form *wrég-nu- in Greek rhégnunai, to burst forth: -RRHAGIA. [Pok. urég- 1181.] [wrod-. Rose. A word (not common Indo-European) of unknown origin. 1. Suffixed form *wrod-o- in Greek rhodon, rose: RHODO-; (RHODIUM). 2. Suffixed form *wrod-ya- (perhaps via Etruscan) in Latin rosa, rose:
=== search 'Down. 1'
787:animal: NEAT2; b. compound form *ga-nauta- (*ga-, with, together; see kom), “he with whom one shares possessions,” companion, fellow, in (i) Middle Dutch ghenét, noot, fellow: MATELOTE (ii) Old High German ginéz, companion, in German Eidgenosse, confederate: HuGuEnot. [Pok. neu-d- 768.] newn. Nine. 1. Germanic *niwun, with variant *nigun, in Old English nigon, nine: NINE, NINETEEN, NINETY, NINTH. 2. Latin novem, nine (< *noven, with m for n by analogy with the m of septem, seven, and decem, ten): NOVEMBER, NOVENA; NONAGENARIAN. 3. Ordinal form *neweno- in Latin nénus, ninth: NONA-, NONES, NOON; (NONAGON), (NONANOIC ACID). 4. Prothetic forms *enewn, *enwn in Greek ennea, nine (> *ennewa, *enwa-): ENNEAD. [Pok. e-neuen 318.] newo-. New. Related to nu-. 1. Suffixed form *new-yo- in Germanic *neuja- in: a. Old English néowe, niwe, new: NEw; b. Old Norse njyr, new: SPAN-NEW. 2. Basic form *newo- in Greek newos, neos, new: NEO-, NEON, NEOTER- IC; MISONEISM. 3. Suffixed form “new-aro- in Greek nearos, young, fresh, contracted into néros, fresh (used of fish and of water), hence néron, water: ANEROID. 4. Basic form *newo- in Latin novus, new: NOVA, NOVATION, NOVEL!, NOVEL?, (NOVELTY), NOVICE; INNOVATE, REN- OVATE. 5. Suffixed form *new-er-ko- in Latin noverca, stepmother (< “she who is new”): NOVERCAL. [Pok. neuos 709.] ni. Down. 1. Suffixed form *ni-t- in Germanic *nith- in Old English nithan, neothan, below: BENEATH, UNDER- NEATH. 2. Suffixed (comparative) form *ni-tero-, lower, in Germanic *nitheraz in Old English nither, lower: NETHER. See compound root nizdo-. [In Pok. 1. en 311.] [niké. Victory. Greek noun of unknown origin. NIKE.] nizdo-. Bird’s nest. Compound root formed from ni + *sd-, zd-, zero-grade form of sed-; literally, “place where the bird sits down.” 1. Germanic *nist- in: a. Old English nest, nest: NEST; b. Germanic ‘*nistilon in Old English nestlian, to make a nest: NESTLE. 2. Latin nidus, nest: NICHE, NIDE, NIDUS; EYAS, NIDIFY. [In Pok. sed- 887.] nobh-. Also ombh-. Navel; later also “central knob,” boss of a shield, hub of a wheel. 1. Germanic *nabo in: a. Old English nafu, nafa, hub of a wheel: NAVE?; b. compound *nabé-gaizaz, tool for piercing wheel hubs (*gaizaz, spear, piercing tool; see ghaiso-), in Old Eng- lish nafogar, auger: AUGER. 2. Variant form *ombh- in Latin umbé, boss of a shield: uMBO. 3. Suffixed form *nobh-alo- in Germanic *nabalé in Old English nafela, navel: NAVEL. 4. Suffixed variant form *ombh-alo- in: a. Latin umbilicus, navel: UMBILICUS; NOMBRIL; b. Greek omphalos, navel: OMPHALOS. [Pok. 1. (enebh-) 314.] nogh-. Also enogh-, ongh-. Nail, claw. 1. Suffixed (diminutive) form *nogh-ela- in Germanic *nagla- in Old English negl, nail: NAIL. 2. Form *onogh- in Greek onux (stem onukh-), nail: ONYX; PARONYCHIA, PERIONYCHIUM, SARDONYX. 3. Variant form *ongh- in Latin unguis, nail, claw, hoof, with diminutive ungula, hoof, claw, talon (< ongh-eld-): UNGUIS. [Pok. onogh- 780.] nogv-. Naked. 1. Suffixed forms *nog’-eto-, *nog’-oto- in Germanic *nakweda-, *nakwada- in Old English nacod, naked: NAKED. 2. Suffixed form *nog~-edo- in Latin niidus, naked: NUDE, NUDI-; DENUDE. 3. Suffixed form *nog’-mo- differentiated or developed into Greek gum- nos, naked: GYMNASIUM, GYMNAST; GYMNOSOPHIST, GYMNOSPER\M. [Pok. nog¥- 769.] no-men-. Name. Earlier form *()noo-mn, zero-grade form *(g)na-men-. 1.Germanic *nam6n- in Old English nama, name: NAME. 2. Latin némen, name, reputation: NOMINAL, NOMINATE, NOUN; AGNOMEN, COGNOMEN, DENOMINATE, IGNOMINY, MISNOMER, NOMENCLATOR, NUNCUPATIVE, PRAENOMEN, (PRONOUN), RENOWN. 3. Greek onoma, onuma, name: ONOMASTIC, -ONYM, -ONYMY; ANONYMOUS, ANTONOMASIA, EPONYM, (EPON- YMOUS), EUONYMUS, HETERONYMOUS, HOMONYMOUS,
912:grade form *séd-yo- in Germanic *(ge)sétjam, seat (*ge-, *ga-, collective prefix; see kom), in Old Norse szti, seat: SEAT. 7. Form *sed-é- in Latin sedére, (third person plural perfect indicative sédérunt), to sit: SEANCE, SED- ENTARY, SEDERUNT, SEDILIA, SEDIMENT, SESSILE, SES- SION, SEWER?, SIEGE; ASSESS, ASSIDUOUS, DISSIDENT, HOSTAGE, (INSESSORIAL), OBSESS, POSSESS, PRESIDE, RESIDE, (SUBSIDY), SUPERSEDE. 8. Reduplicated form *si-zd- in: a. Latin sidere, to sit down, settle: SUBSIDE; b. Greek hizein, to sit down, settle down: SYNIZESIS. 9. Lengthened-grade form séd- in Latin sédés, seat, residence: SEE?. 10. Lengthened-grade form *séd-d- in Latin séddre, to settle, calm down: SEDATE!. 11. Suffixed o-grade form *sod-yo- in Latin solium, throne, seat: SOIL}. 12. Suffixed form *sed-rd- in Greek hedra, seat, chair, face of a geometric solid: -HEDRON; CATHEDRA, (CHAIR), EPHEDRINE, EXEDRA, SANHEDRIN, TETRAHE- DRON. 13. Prefixed and suffixed form *pi-sed-yo-, to sit upon (*pi-, on; see epi), in Greek piezein, to press tight: PIEZO-; ISOPIESTIC. 14. Basic form *sed- in: a. Greek edaphos, ground, foundation (with Greek suffix -aphos): EDAPHIC; b. Sanskrit sad- in upanigad, Upanishad: UPANISHAD. 15. Suffixed form *sed-G-, seat, in Welsh sedd, seat: EISTEDDFOD. See also compound root nizdo-. [Pok. sed- 884.] sed-?. To go. Suffixed o-grade form *sod-o- in Greek hodos, way, journey: -ODE; ANODE, CATHODE, EPISODE, EXODUS, HYATHODE, METHOD, ODOGRAPH, ODOMETER, PERIOD, STOMODEUM, SYNOD. [Pok. sed- 887.] segh-. To hold. 1. Suffixed form *segh-es- in Germanic *sigiz, victory (< “a holding or conquest in battle”), in Old High German sigu, sigo, victory: SIEGFRIED. 2. Greek ekhein, to hold, possess, be in a certain condi- tion (> hexis, habit): HECTIC; CACHEXIA, ECHARD, EN- TELECHY, EUNUCH, OPHIUCHUS. 3. O-grade form *sogh- in Greek epokhé, “a holding back,” pause, cessation, position in time (epi-, on, at; see epi): EPOCH. 4. Zero-grade form “sgh- in: a. Greek skhéma, “a hold- ing,” form, figure: SCHEME; b. Greek skhoié, “a holding back,” stop, rest, leisure, employment of leisure in dispu- tation, school: (SCHOLAR), SCHOLASTIC, SCHOLIUM, SCHOOL/. 5. Reduplicated form *si-sgh- in Greek iskhein, to keep back: ISCHEMIA. [Pok. segh- 888.] seib-. To pour out, sieve, drip, trickle. 1. Basic form in Germanic “sipon in Old English sipian, sypian, to drip, seep: SEEP. 2. Suffixed o-grade form *soib-on- in Ger- manic *saipén-, “dripping thing,” resin, in: a. Old Eng- lish sdpe, soap (originally a reddish hair dye used by Germanic warriors to give a frightening appearance): SOAP; b. Latin sdp6, soap: SAPONATE, SAPONIFY, SAPO- NIN, SAPONITE; SAPONACEOUS. 3. Variant Germanic form *sib- in: a. Old English sife, a filter, sieve: SIEVE. b. Old English siftan, to sieve, drain: sirt. [Pok. seip- 894.] seikw-. To flow. Extended expressive zero-grade form *sikko- in Latin siccus, dry (probably < “flowed out”): SACK3, SECCO, SICCATIVE; DESICCATE, EXSICCATE. [Pok. seiku- 893.] sek-. To cut. 1. Germanic *segithd, sickle, in Old English sithe, sigthe, sickle: SCYTHE. 2. Suffixed o-grade form *sok-d- in Germanic *sag6, a cutting tool, saw, in Old English sagu, sage, saw: SAW. 3. Suffixed o-grade form *sok-yo- in Germanic *sagjaz, “sword,” plant with a cutting edge, in Old English secg, sedge: SEDGE. 4. Suf- fixed o-grade form *sok-so- in Germanic *sahsam, knife, sword, traditionally (but quite doubtfully) regarded as the source of West Germanic tribal name *Saxon-, Saxon (as if “warrior with knives”), in Late Latin Sax6 (plural Saxonés), a Saxon: Saxon. 5. Extended root *skend-, to peel off, flay, in Germanic *skinth- in Old Norse skinn, skin: SKIN. 6. Basic form “sek- in Latin secdre, to cut: SECANT, -SECT, SECTILE, SECTION, SECTOR, SEGMENT; DISSECT, EXSECT, INSECT, INTERSECT, NOTCH, RESECT, (TRANSECT). 7. Lengthened-grade form *sék- in Latin
1489:EXTRACT tragh- EXTREME eghs EXTROVERSION wer-3 EXTROVERT wer-3 EXTRUDE treud- EXUBERANT euedh- EXUBERATE euedh- EXUDE sweid-2 EXULT sel-4 EXUVIAE eu-! EYAS nizdo-
1909:NEST nizdo- NESTLE nizdo- NET! ned-
1914:NIBBLE ken-2 NICE ne, skei- NICHE nizdo- NICKNAME aug-? NICTITATE kneigh- NIDDERING nei- NIDE_ nizdo- NIDIFY dhé-1, nizdo- NIDUS nizdo- NIECE nepot- NIELLO negW-ro- NIFLHEIM nebh-, tkei- NIGGARD_ ken-2 NIGH néhw-iz NIGHT nekw-t- NIGHTINGALE ghel-1 NIGHTMARE mer-2 NIGRESCENCE neg¥-ro- NIGRITUDE neg¥-ro- NIGROSINE negW-ro- NIHILISM ne NIHILITY ne
```


## [2026-09-07T19:31:23.118Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for p in \"ni-jan\" \"nijan\" \"nishaδ\" \"ni-had\" \"nihaδ\" \"nipaes\" \"ni-pae\" \"nixsvaep\" \"xsvaep\"; do echo \"### $p\"; grep -n -- \"$p\" BRT.txt | head -5; done",
 "description": "Bartholomae greps"
}
```


### [2026-09-07T19:31:24.412Z] TOOL RESULT

```
### ni-jan
### nijan
4688:•  j.  atnae.ni'gan-:  niyn-  Adj.  (auch  fem.) 'beim  Angriff,  Anlaut  niederschlagend': rfrf^raynsm  . .  -niyn^m  (als  Asn.)  Yt.  i<). 54;  —  mit  Akk.:  /ravasayö..  yn..  'nijanö (NPf.)  Aam^>>!  Yt  13.^5.
9983:mit  «f  i)  '(eine  Waffe)  niederschlagen, -schmettern  auf—'  {paiti  mit  Lok.):  ks (näml.  mi'hro)..gmqm(%A^  nijainti  aspaSta paiti  vTraii'a  Yt.  10.101,  3)  'nieder-, zu  Boden  schlagen,  er-,  entzweischlagen': yatcit  tdastaire  hindvd  (sd.)  ^ifgiurvayaiti yatcit  daosataire  niyne  (3SPM.)  Y.  57. 29;  —  %wqmca  drupmca  «»'/«« (iSPM,?) Yt.  4-5!  —  yalba  azim  nijanäni  dva 'irisva  .  .  daez'anqm  Yt  5.  22;  9.  22, 31^,  15.  3;  —  yat  niE  avavat  daljia- yasiianqm  nijattm  ya%a  ..  Yt^.  77; —  para  akmät  yat  .  .  aiimaoyB  . . *'ka%ra.jatö  nijanSite'^  V.5.  56;  y.  55;  — yö  .  .  stija  nijainti  kam^rT^l . .  na2',a.cim ymqm  sadayeiti  yavata  alm  nijainti  m>r>- zuca..  Yt,/o.7ij — yat  *n5  nsit  ni/anüt'^ ars'a  ..  Yt/5.  32;—  nij'ann'ctiS.)  buye vTspe  dusmainyü  K.i.\\;  —  yai:a  aspm aom  spähm  nijanäni  yö  .  .  Yt.  14.  58;  5. 54,  58;  —  mit  Dat  incomm. :  kahmäi  .. fraiaintim  kdi:ra.jata  (sd.)  nijanäni  Yt. 10. 110.  a)  sva.  'zerstören,  zu  Grunde richten';    l0   vispe   v^rfioinqm    vanat  nl
13109:—  izitu/  nämä"  'Ayätts  a%uräyi^  Bh.2, 10.  11)  im  Atw.:  Uta  at^m  nijanäni RyaonXnqm  'hyunqm  pancasayriäi  .  .  Yt j?.  3 1 ;  —  Uta  azmt  fraourvaisayeni  kumaya (sd.)  *väri'ikanatn  hyaonya  (sd.)  haca 'itihävBiOß.  statt  AblS.)  Ytp.si  \~ydka aztm  nijanäni  tüiryanqm  'hyunqm  panca- saynäi  . .  Yl  5.  54;  /,?-'i43'.  V.J.  42  PüZ., 5. 38PÜZ.;  —  airyanqm*  'Ryunqm*  .. sairimanqm'  'hyunqm'  . .  säininqm'  'hyu- nqm' ..  dählnqm'  'hyunqm''  ..  Dlspanqm* 'hyunqm*  Yt  i^.  i43ff.;  —  kä'ia  airyi' -irihävö  huyäiryh  bat'inti  Yt  8.  36;  56, 58 j;  —  nsit  .  .  airyä  'itihävö  (als  AP.) Art/ (sd.)  hyäi  hama  Yt  8.  56;  —  mi^rtm .  .  huiayamm  atryäbyö  'i^hubyB  Yt.  fo.4;
13110:—  hama<a  airyäbyB  'itihubyö  vBiynä  ja- santi Yt  8.61;  61'; — ya^a  vatm  nijanäma airyanqm  'hyunqm  pamasaynäi  Yt  5.  58 ; 117;  —  arsa  airyanqm  'hyunqm  ..  hao- srava   YL5.  49;    —   gayehe    mar.Ktnä  ..
13781:—  vanätna  vtspe  'yus'^  (AP.)  Yt.  70. 34; Ny.j.  10;  —  nijan?  buye  vJspe  °ya  (AP.)^'
### nishaδ
### ni-had
### nihaδ
### nipaes
### ni-pae
### nixsvaep
### xsvaep
```


## [2026-09-07T19:31:34.132Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for p in \"nipais\" \"nipis\" \"ni-pai\" \"nišad\" \"nisad\" \"niyasad\" \"^ni-\" \"nij\" ; do echo \"### $p\"; grep -n -- \"$p\" KNT.txt | head -6; done",
 "description": "Kent Old Persian ni- greps"
}
```


### [2026-09-07T19:31:35.498Z] TOOL RESULT

```
### nipais
### nipis
2967:$290. COORDINATION AND SUBORDINATION. Not infrequently the OP texts express by coordinate clauses ideas which are logically subordinate; the result is a series of short sentences, syntactically simple, independent of each other grammatically, but logically and semantically connected. Thus, for example, DB 446-8 vafnà Auramazdaha api- mary aniyascry vasiy astiy kartam ava ahydya diptya пазу nipistam avahyarddiy naty nipistam таша ... ‘by the favor of Ahuramazda indeed, much other (work) was done by me; that (work) is not inscribed in this inscription; for the following reason it is not inscribed, lest . . .’; this could have been expressed in one complex sentence somewhat as follows: ‘much other work was done by me, which has not been inscribed in this inscription for the following reason, lest ...’. Another excellent example is found in XPf 20-25 шій Vistáspa иа Arfüma ubā ajivatam асту Auramazdim арабӣ Ката aha Dérayavaum hya manā рий avam asdyabiyam akunaus ahydyd бата 'Hystaspes and Arsames both were living, then—unto Ahu- ramazda thus was the desire—Darius who (was) my father, him he made king in this land’; in the parallel passage DSf 13-5, yadzy ‘when’ is used . instead of асїу ‘then’, and instead of Auramazdém avatà Ката aha (found also XPf 29f, DSf 15f), we find in DNa 37f (and elsewhere) yada mim ата Gha ‘as unto me was the desire’. In dating sen- tences we regularly have expressions of the type seen in DB 1.42 Garmapadahya máhyà I X rauca- bi$ fakaia aha агава zšaçam agarbdyatd ‘of the month Garmapada, 9 days had passed—then he seized the kingship’; only in DB 1.38 the date is followed by a subordinated clause, yadiy udapa- tala ‘when he rose up in rebellion’. The same phenomenon is probably present where conjunc- tions are omitted as introductory to subordinate clauses, such as the absence of tya in РМ 20 and 50 (cf. DNa 39).
3144:(c) A relative and its antecedent are both omitted in XPh 30-2 astiy айат atā dahydva уату upariy nipistà ayauda ‘there is (= ‘was’, $285) among these provinces which (are) inscribed above (one which) was in turmoil’.
3841:47 m [ауа : ahy&y& : dipiyàf: палу : nipistam.: avahyarádiy : naiy : n
4153:57 : avasely : didiy : yaciy : nipistam : mà :
4586:31 :dahyáva : tyaly : upariy : nipistà : a
4656:9 framàátàram : adam : Xšayāršā : 10 x&àyafiya : vazraka : хёдуабуа : 11 xšāyaðiyānām : xšāyaðiya : da 12 hyünàm : paruv : zanànàm : x$ 13 àya8iya : ahy&yà : bümiyà : va 14 zrakày& : düraiy : apiy : Daraya 15 vahaus : xšāyaðiyahyā : риса : Ha 16 x&manisiya :0ütiy : XSayársá 17 : xSayabiya : Dārayavauš : xSiya 18 буа : һуа : manā : pitä : hauv : va 19 502 : Auramazdaha : vasiy : tya : 20 naibam : akunauég : uta : ima : st 21 änam : hauv : niyastdya : katanaiy 22 : yaniy : dipim : naiy : nipist 23 ām : akunaus : pasáva : adam : ni 24 yastéyam : та : dipim : піра 25 iStanaiy : màm : Auramazda : pa 26 tuv : hada : бадафт : utämai 27 y : zSaqam : Ша : атану : kartam
### ni-pai
1205:inf. ni-paistanaty; for cognates, see Lex. s.v.
1519:*peik- ‘cut’ in ni-paiStanaiy ‘to inscribe’; *pik- in pte. ni-piStam ‘inscribed’,
### nišad
### nisad
### niyasad
518:I. Apparently -iya- in the interior of words contracted to --; there are the following ex- amples: niyasadayam DNa 36, and nisàdayam XPh 34t. niyasidya DSn 1, XPh 50, XV 21, and nislaya
2503:OP imf. niyasadayam ‘I set down’ (on -&-, 5117). pAr. *aí&-aja- in Skt. egayati; OP imf. fraiSayam
### ^ni-
1439:ni-Sad- from ni- + sad- (Iran. had-), and the value $ š is extended to positions where the š is separated 1 from the т by the augment: ntyaštāyam ‘I com- : | manded’ (but avastayam ‘I restored"), niyašāda- d yam ‘I commanded’, So also the enclitic pronoun. 3
2857:ni- ‘down’, only in phrasal adverb nepadiy ‘down on the footstep, on the track of, close after’, itself functioning as a preposition governing the accusative tyaty (DB 3.73; for form, see $198).
5044:ni- + ar- ‘come down, descend’, with abiy and acc. of place: nirasãtiy subj. (5140.1; §289) DPe 24.
5237:ni- + kan- ‘destroy, obliterate’: пач imv. (§208, $237.IT) DB 4.80.
5606:ni- prep. and verbal prefix ‘down’: Ау. ni, Skt. ni-, pIE *ni; in adv. nipadiy, and with verbs ar-, kan-, cay-, pa10-, yam-, std-, had-.
5843:ni- + yam- ‘reach out and down; (caus.) set down’: niyasaya imf. caus. (823.I, $140.IIT, $215) DNb 5, 46, 49 (In. JAOS 38.123-4; MB Gr. $199; Johnson, Gr. $4780; Hz. ApI 359-61).
### nij
1286:On -j- in nijdyam, sec §120.
1491:The Aryan prefix *nii, from pIE *ni + s ($115), became nzz before voiced stops, as in Av. niz-borala- ‘carrying off! (nt. sb.), and is written mj- in OP nij-ayam “1 went forth’.
2378:(b) The following, not found as prepositions in the extant remains of OP, are found as verbal pre- fixes: apa-, ava-, ud-, nij-, fra-, vi-.
2396:pIE *ei-ti ‘he goes’, OP ату, Skt. éti; *i-te ‘go ye’, OP -itä in ратайа, Skt. itá; *7-dhi ‘go thou’, OP -idiy in paridiy, Skt. iht; imf. *é&-m ‘I went’, OP -dyam (for -am, 407.1) in nij-äyam [up]- üyam, Skt. dyam; imf. 3d sg. ОР а (on -S, $228.IIT) and atiy-ãiš; imf. 3d pl. with the- matic vowel from Ist sg., OP -йуа” in apariy- йуа”, -ài$a" (on -&а", 4282.1) in patiy-disa’, mid, dyad from *4-dya7ta.
2564:with -am from thematic -o-m: pIE *és-m Ч was’, Skt. dsam, OP dham; Skt. dkynavam, ОР akuna- vam; OP frdjanam avdjanam, viyakanam, avé- kanam, nij-dyam (ulpayam upariy-dlyalm, aor. niy- араат. The suffix -nd- has become -na- in adinam, in imitation of other first persons.
2826:nouns. E- ачат, prep. W. асе. ati-, pref, w. verbs. abiy, prep. W. ace. anu», prep. w. instr. and gen. apa-, pref. w. verbs and nouns. abiy, prep. w. acc.; pref. w. verbs and nouns. ava-, pref. w. verbs. ud-, pref. w. verbs and nouns. upd, prep. w. acc.; pref. w. verbs and nouns. upariy, prep. W, асс.; pref. w. verbs. lara, prep. w. acc. ni-, prep. W. loc. in phrasal adv.; pref. w. verbs, nij-, pref. w. verbs. nipadày, prep. W. ace. T patiy, prep. ж. асе.; postp. у. acc, inst, loe; .^
```


## [2026-09-07T19:31:45.860Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"\\[pdf page\" SOD_pages.txt | head -5; echo \"---\"; grep -c \"\" SOD_pages.txt; echo \"--- search\"; grep -n \"nyγrb\\|nyxrb\\|nyγ\\|nyst\\|nypd\\|nyptδ\" SOD_pages.txt | head",
 "description": "Inspect Gharib Sogdian dictionary"
}
```


### [2026-09-07T19:31:45.939Z] TOOL RESULT

```
---
45616
--- search
3106:                                                                             M nyst-. (destroyed) alternates with M nst- and B
6679:1020 'nyst- B                                 o^-^^j^
6685:1021 'nysty S                              <^u^<l^<<oL^J
7190:      anxast      ©pt. St. =*Jnxz-, 'ny'st-, 'nyst-                1203 'ny' B                                               JL>
14672:     fanes, fanes ©<fra-nasaya          =»fnyst-, Pn'ys-
14685:3862 fnyst- C                           Ooial^^-o io*^p o\j*5
14691:3863 fnysty      C
18560:                                                                    5214 m'nyst'n M, S                             jjm**^
18568:                                                                    5215 m'nyst'n 5'r'k S         (j/j^^J^^c— >T-r-
21103:                                                                   niste (nscO ©pp., f. pp. nisca =*ny§-, nystch,
```


## [2026-09-07T19:31:53.140Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^ *[0-9]\\{3,5\\} ny\" SOD_pages.txt | head -80",
 "description": "Sogdian ny- entries"
}
```


### [2026-09-07T19:31:54.375Z] TOOL RESULT

```
20485:        5839 ny C, S                                 0^* *,y olXi Vrr^     5851 n'zyny C                              J^O^
20494:       5840 nys-       B                                                        niPand ©prepos. postp. =>nPnd, nbnt(y), 'np'nt
20501:       5841 nyty ? S
20609: 5889 ny^kh B                                                    5900 ny'wnt'k B                                    jW,,;
20614: 5890 nyMin B ^ ny'm                                            5901 ny'wnt'y =* ny'wnt'k
20615: 5891 nyW C -» ny*'                                             5902 ny'ws- B, M, 5 yj^ ^)d^^            O^j^      < 0-^
20616: 5892 nyW M                                          U?Ur fUj
20627: 5893 ny'm B, M, C                                 uU><f&*
20634:                                                                5904 ny'ws'ky'kh M, S      ^u ^ Jj^ ijfxyJ^ {^r
20635: 5894 ny'mk S                                             ^          niyosakya(k) (nyw^kyh)
20639: 5895 ny'my      M, B =* ny'mk                                  5905 ny'wsn'k B                                     ^^
20657:                                                                5908 nyn- M, C                                        jb
20660:5898 ny'wnt B                                     fJj<S*             bread
20665:5899 nySvnt-       B                            o^^i^U)                26
20672:     5909 nynp'k S                                   j,jUJ>U       5923 nysn(h) B                           jUwo^UO^
20680:     5910 nynwp'c M                                  j-jUj*
20687:     5911 nyr^y- B                         ax-*^ *o>j^>
20689:                                                                   5925 nysyr B, S                 j^^/y.^^^
20694:    5912 nyr*my      C = n+ yr'my =» n-, yrWk
20696:    5913 nyr'n rwc S           (o^'-^j^)^^ \s*<jjj(iP
20703:                                                                   5927 nywp- B                                  ub*"Ju
20704:    5914 nyr'y- ■* nyr*y-
20706:    5915 nyrf C = n +yrf -> n-, yrf                                     excellent, kind, fine
20707:    5916 nyrn* rwc -» nyr'n rwc                                         BSTBL, Dhy. 153, 363; GMS 445
20708:    5917 nyrs- -* ^yrs-                                            5928 nywp'w'k B                                ><^>^
20709:    5918 nyrwps- S                  0-^»->^j> <ooiojjii                 nayuPawe
20714:                                                                   5930 nyw6n(>)/(h) B, M, S              jTU^^U
20715:    5919 nyrys- S(C)                              o*J> o~jjs"           niyoSan   (nywdn) ©Khwar. nYwdnyk  ©pi. -(
20720:    5920 nys'kt    M =* ny>ws>kt                                          BSOAS 12, 307.15; GMS 676, 1030; STi 16.9;
20721:    5921 nys'yrGi) B                                                      BSTii 843.25, 903.6; C2, 56R26, 68R25; pi.
20727:                                                                   5932 nywnty C                                 J^jj^
20731:    5922 nys'yr sk'rk B
20741:                                                               5948 nywst- C                             o-tju- i j.>
20742: 5934 nywst'k S                                      .juij,         niyust ©pt. st. ^ny'ws-
20748: 5935 nyws-   B, M, C =* nfws-
20749: 5936 nyws'k M                            S\^^l^^                   deep, profound
20756:5937 nywsVnc M            v                      o j J*li           STii 1.31; GMS 1111
20760:5938 nyws'k'st M
20766:5939 nywi^qpt'nc M                    OjO^li-j       -Vi^-         nikapd- paznyak
20771:5940 nyws'kyh =*» ny'ws'ky'kh                                 5955 nk'np- B                              ,^/t^/^
20772:5941 nywsdV- C                                                     ni- kanp =>nq(3t-
20776:5942 nywsk =» nyws'k                                                nikare   (nkVk) ®<*ni- kdraya
20777:5943 nywsk'ny M                      jf\^y^{<,^^J)
20783:5944 nywskpt M                        o^^j^^j
20793:5946 nywsny C                               ^j^t^J^
20798:5947 nywsnyy M                                      oxyi
21483:                                                               6198 ny M, C                                                    <■
21496:                                                               6200 ny»k(,) B                       *        o^.U
21533:                                                              6206 ny>d'r-     C                                      ^f
21545:6207 ny'k B =* ny»k(,)
21547:6208 ny'k m't B
21554:6209 ny's-                                                        necessity(w/zar is necessary)
21560:                                                             6222 ny'zk'yn B                                     jl^jU
21569:6210 ny'sd'r- =» ny»d»r-
21570:                                                             6223 ny'zqyn     C =* ny'zk'yn
21571:6211 ny't-                        (Jj*s**j>)^S
21577:6212 ny't'y B, S                                  &>f
21584:                                                             6227 ny'zwr    B =» nyz'wr
21585:6213 nyWr-         =» ny)d,r-
21586:                                                             6228 nyc' B
21587:6214 ny*tk =» ny^y                                                nee ©<*nahika; Khwar. nyC; Yaghn. cr^C
21590:6215 ny'tyy M =* ny^y
21591:6216 ny^S B, S                            Lv-.Lj>^b*jJ9           nose, nostril
21594:                                                             6229 nyc2 C
21599:6217 ny'wr M                       j^ ^oaj <^_.>jUSl$
21605:6218 ny'z M                                      ^L^I.jU          SCE 85
21607:                                                             6231 nyct'y B                                   u>^»
21612:6219 nyVnk     B                            o/b/ <c*&~            buried
21621:6232 ny5- B, M, S                              j^                      Dhu. 242, 284; GMS 1578; MSP b 134; S W,
21630:                                                                6244 nyy B, S                               &*><^jj*&~*
21631:6233 nyd-        C =» nyS-                                           nix =»nyy, nyyw
21633:6234 ny8Mk B                                        ^^               deep, profound, attentive
21639:                                                                6245 nyy'wnt-     B                                 OJuij*
21640:6235 nyS'm'nty B                        c    Vmi^S ^,.:j             niyund     (nyywnt-) ©impf.      =>ny'wnt-
21645:                                                               6246 nyy'ws- B, C
21646:6236 ny6V        B                                     <^j          ni-yos (nyyws) ©impf.
21651:                                                               6247 nyytm B
21652:6237 ny5y B                                                         nixtam =*nyy
21657:                                                               6248 nyyw                                           jLJth**
21660:6238 nyS'yc(h)      B
```


## [2026-09-07T19:32:06.497Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"ni- ?gr\\|ni-gr\\|nigr\\|ni- yr\\|nyyrb\\|nyrb\\|ny^rb\" SOD_pages.txt | head -20; echo \"=== nist / ni-st\"; grep -n \"ni- ?st\\|ni-st\\|nist'y\\|nyst'y\\|ni- št\\|ništ\" SOD_pages.txt | head -20; echo \"=== nipa\"; grep -n \"nypd\\|nyp8\\|ni- pad\\|nipad\\|ni- payd\" SOD_pages.txt | head -20",
 "description": "Sogdian ni-grab, ni-stay, ni-payd"
}
```


### [2026-09-07T19:32:06.568Z] TOOL RESULT

```
=== nist / ni-st
21105:      nars                                                            nysty1, nyst'y
21240:     nistay (nyst'y-) ©<*ni-staya; OP niyastaya                 GMS 1322, 1320
21819:       <*ni-drdma-Jca ?                                        6302 nyst'y B, S                                <^j
21834:       nis(t)ca (nscO ©f. pp. -^nyst'y, nsty                         niskaw     (nysq'w-) ©pres. & impf. =»nysqwyt-,
21895:       86.8, 412, 5; nypy&tt, SCE 529, 3sg. subj.                   nistat ©*ni-stdta ©pt. st. =*nysty-, nst*t-
21900:       ©impf. ? ^nsyw'y-                                       6329 nyst'y- => nsty-
21918:     nistay ©<*ni-staya; OP nistaya-, \Tsta =»nsty-            6344 nyw)y6- B                          j^J^td^J'^^
=== nipa
20981:                                                                    inf. np*sty =»nyp8-, npst'ny, np>y8-
20986:                                                                  nipastane =>nyp8-, np*st-, npst'ny
21016:        pcrf. st. ^np^s-, npxst-, np'xst-Cy)                        Pahl. nibdy-, nibdstan =*nyp8-, np»st-
27871:     pis-pa8u ©<*pasca-padam\ OP nipadiy                     8389 pytsr5 B                           ojl>> ijMoa <jJ*
```


## [2026-09-07T19:32:15.212Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '21230,21250p' SOD_pages.txt; echo \"#### 21885-21925\"; sed -n '21885,21925p' SOD_pages.txt; echo \"#### 21010-21020\"; sed -n '21008,21020p' SOD_pages.txt",
 "description": "Sogdian context lines"
}
```


### [2026-09-07T19:32:15.294Z] TOOL RESULT

```
                                                                  subj. nw*t, Anc. Lett. 227
     TSP 5.111; Hen. JRAS 1944, 138.22, 37; MDii           6102 nw-3 C                                     jlw^rif
6090 nsty B, M                            «jii*^«jLi.U-         boat, ship
                                                                naw, now ©ob. nwy =*nw*z, n'w, nwbry*
     niste ©pp. f. nsty =^nys-2, nst-, nysty
     destroyed                                                  BSTii 879.6, 8: C2, 87V6, 8
     nstw, TSP 5.111, 25, liii; nst\ TSP 7.142; BBB        6103 -nw C                                    ^jjlpju^^
       674, 722                                                 nu ©<*(a)nam <anam
                                                                numeral suffix
6091 nsty- S                  c»k£'&>t<d*kjjz~*'o>J'jJs.
     nistay (nyst'y-) ©<*ni-staya; OP niyastaya                 GMS 1322, 1320
       ©impf. nysty =»nysty-                               6104 nwwz M                         ^jA-^'l^'C^
     (/o)settle, (ro)order, (/<?)inform -                       nawaz ©<Av. navdza\ Skt. navaja; Parth.
     MDii p205; MDiii pl24
                                                                sailor
                                                                  nawaz =>n*wzy(y), nw-3
6092 nsyd-     C                        j&f i&Ax <od4>
 245                                                                                                             nwpznyy

       GMS 125                                                         TSP 7.14, 25; GMS 1316
                                                                  6115 nwy    B, S                                        y
#### 21885-21925
6314 nys-2 B, M, C                 j^j ^ }\to^^\j^
     nis ©<*nasya- ©intrans. St. «*nsty                              BSTii 8492, 851.4; Benv. JA 1955, 325; C2, 12R2,
     OcObe destroyed                                                   12V4
     GMS 193, 549; BSTii: C2, 102V21
                                                               6327 nyst-      M, C                   o-^XoL^j < a^v'>-
6315 nys'yS- B, M, S                  ^lT <^ ^lif                   nist- ©pt. st.; perf. nystwdyr- =»nysty, nst-
     niseS (nysyyS-, nysy5-) ©<*ni-sadaya-                          (to)destroy, (ro)spoil
       ©impf. =*nsyd-                                               BBB p8l, 674; Sund. AoFviii 1981 p216
     (ro)set, GcOplace
     GMS 545, 626; VJ 864, 1358; impf. Frag. Len.              6328 nyst't- B, M                    o>ty*rji <i>kuU^i
       86.8, 412, 5; nypy&tt, SCE 529, 3sg. subj.                   nistat ©*ni-stdta ©pt. st. =*nysty-, nst*t-
                                                                    (fo)order, 0o)fix, (reestablish
6316 nysyw'y- B                                    jju^
                                                                    GMS 122, 561; VJ 1416, nystWr-t AVS 93
     nisxway (nwsyw'y-) ©<*nis- xwahaya-
       ©impf. ? ^nsyw'y-                                       6329 nyst'y- => nsty-
     (ro)cut off                                               6330 nyst8>r-     C                                   ^tT
       TSP 1629; nwsYw'yU TSP 16.24, 3sg. pres.; pp.                nisSar ©<ndsiSdr-         ©trans, perf. ^nsydt'r-
         TSP 16.38; nsYwsU GMS 679
                                                                    (rc)plant
                                                                                                                        254

 nysty

         STi 19.15; GMS 434                                          BBB; GMS 1464; TSP; nyw>nty, Hen. Tales.
6331 nysty C                                      c-Jv'>               486.16; BSTBL p 117
     nistc =»nyst-, nsty                                        6343 nyw'yS B                                 jT^(jU
                                                                     niweS
         spoiled, destroyed
                                                                     to it, for it
         apud. Sund. AoFi 253.6
                                                                     GMS 1404, 1457; TSP; BSTBL, Dhy. 80
6332 nysty- M, C, S           jih^3~ <o>^ ' JJjt 0->'->j>^->
     nistay ©<*ni-staya; OP nistaya-, \Tsta =»nsty-            6344 nyw)y6- B                          j^J^td^J'^^
     (ro)order, (ftOfix, (/^announce                                niwe8 ©impf. ^nw^S-
     GMS 561, 677, 1605; BSTii 88.13, 873.12; impf.                 (r<?)invite, (ro)request
                                                                    BSTBL, Dhy. 181
          nysty, C2 gloss.
                                                               6345 *nywq ^ nywqst
6333 nysty*ty C                           «j£f}W «oi«3b^.
                                                               6346 nywqst     C                                  oJ;j<L^
#### 21010-21020
        Frag. Len. 93.11
                                                                  nipaxst (npyyst) ©pt. st. & pp. =>np>YSt-,
•020 nny M, S                             (^/ rb)J2                 npxsty, np}YStk, npYStk
     nanai -♦nnSP'mbn                                             OcOwrite, writing
     Nanai(a goddess)                                             Anc. Lett. 2.29, 3.26, 5.32; KG 390; MSP clO, 11,
     Hen. Sogdica. p7; BSOAS 28, 1965, 252 n 67                     np}xstw\ Frye 21, npxsty
«21 a^st-       B, S                                 ^       6033 np>y5- B, C                           j^^lif
      nipaxst (np'st ?) ©pt. st.; inf. -y-, npVstwS^r,            nipeS (npy8-) ©<*ni-padaya\ Av. ni- paidya\
        pcrf. st. ^np^s-, npxst-, np'xst-Cy)                        Pahl. nibdy-, nibdstan =*nyp8-, np»st-
```


## [2026-09-07T19:32:22.767Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"grb\\|yrbt\\|grab\\|grafta\\|yrft\\|grfta\" SOD_pages.txt | head -30",
 "description": "Sogdian grab forms"
}
```


### [2026-09-07T19:32:22.821Z] TOOL RESULT

```
3195:              YrP-                   *grba-
5723:                                                                              ayar(3an ©*a-grabana ©f. =»yrP-
15710:4196 yr'yk^ B                             J^^                   yarP, yorJ3 ? (yrb-, >yrp-) ©<*grb; <*grab; OP
15812:      yarfi-smarak                                                      4254 yrftyct M, C                             U>>- J^
15813:                                                                             yarft-est (yrftyst)
15819:4242 yrpzng'n M                                                         4255 yrftyst     C =» yrftyct
25202:                                                                   Aiam.psgrb* =*Yrvw
25760:                                                                  patyo/arP ©<*pati-garb-lgrab-\ Parth.
25781:                                                                  patyriPd ©<*pati-grfta-         ©pt. st. =*ptyrP-
36471:    11262 zy'yr't-                             qzJ'^lo^j^             zyarp, zyorp ? ©<*uz-grab
```


## [2026-09-07T19:32:30.396Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"\\*ni-\\|<\\*ni\\|©<\\*ni\" SOD_pages.txt | head -40",
 "description": "Sogdian *ni- compounds"
}
```


### [2026-09-07T19:32:30.473Z] TOOL RESULT

```
3236:  /nipes/     npys-        write         *ni-paisa-
20517:       5843 n'ywq =» n*ywk                                                     ni-Pend       ©<*ni-bandaya   ©impf. nyfl^ynt
20587:         890.43; C2 gloss.                                           nifriwan ©<*ni-friwana =»nfryyn
20604:      Hen. JRAS 1944, 143.26                                          niyund (nywnt-) ©<*nigunda ©impf.
20618:          niya6a (ny'dO ©*ni-gadaka ©f. n.                            niyos (nyws-, nyyws) ©<*ni~gausa-; Parth.
20628:      niyam (ny*m) ©<*ni-gama ©ob. -y                           5903 ny'ws'kt M, S                     ^l^oif*^
20642:      niyars ©Benv. <*ni karsa & Mack. zY>rs                         listener, hearer
20646:         TSP 7.33 apud. Hen. Texts. 733; BSTBL, Dhy.                 znixay ©<*ni-xwahaya ^nxw'y-, nyw}y-
20661:         nixund ? ©<*ni~xwdy-        ^ptyNvnt
20776:5942 nywsk =» nyws'k                                                nikare   (nkVk) ®<*ni- kdraya
20877:               nimarz     ©<*ni-marz-\ Khot. nimalys; Khwar.
20906:             nimay ®<*ni-mdya- ©impf. nym^y ^nnVny*                             Sogdica. 2.19, 3; BBB p75, 607; GMS 550, 828 n 1
20960:                                                                  writing (npxsty) ©<*nipixsta ©pp.
21015:      nipaxst (np'st ?) ©pt. st.; inf. -y-, npVstwS^r,            nipeS (npy8-) ©<*ni-padaya\ Av. ni- paidya\
21073:      nipaxst       ©<*ni- pixsta ©pt. st. ^np'ys-,               6056 nrmVnt      B                            ^ijujL
21115:                                                                   ni-say ©<*ni-0ray- ? =*Ps}y-
21124:       Narisaf yazd(a Manichean god, friend of                     niseS  ©<*ni-sadaya-      ©impf. nyPyS; perf.
21153:       BSTii 892.10; Benv. JA 1955, 325; C2 gloss. p232            nis-xway (nwsyw^-) ®<*ni$-xwahaya
21200:     n(i)sm(e), nisam(e) ©<*nisma-y A v. frasma            6096 nsyyS- M =» nsyd-
21240:     nistay (nyst'y-) ©<*ni-staya; OP niyastaya                 GMS 1322, 1320
21266:                                                                      ni-we6- (nwyd-) ©<*ni-vaid ©inf. -yy-t impf.
21343:     Noah                                                              niwart ©*ni-warta- ^nw'rtCy)
21453:     nosik                                                           niweSma (nwydm}, nwy5mh)          ©<*nivaid-mG
21508:     nixres ©<*ni- xrausaya; MP nixroh—, nixrost-                   TSP 8.172
21535:     ni-xway (nxwy-) ©<*ni-xwahaya ^nyw'y-,                        niya(s)5ar       (ny'tS'r-, ny'sd'r-) ©trans, pret. st.
21556:     niyas ©<*ni-ydsa\ Khot. nasa-;  Yag>^-  j^cpj'
21572:     niyat ®<*ni-yata\ Yaghn. nota ©pt. st; perf.            6224 ny'zkyn =$ ny^k'yn
21609:                                                                  nict(e) ©<*ni-kata ?; Khwar. nkndk; Parth.
21622:     niS (nyd-) <£)<*ni-hida; Shad-; Khwar. nyO\                       SGI 1986, 412-3
21683:     BBB 588; GMS 978                                               niz, nizay ©<*niz(a)ya-\ Yaghn. niz\ <*nis-ay-
21700:     niz(i)t (nyzt-, nyjt-) ©<*nizita     ©pt. st.
21718:6259 nykyr'n      B, M =» nykr'n                                      ni-yamt, nimt ? ©<*ni-yamt        ©pt. st.
21727:     nime ©<*nimaka                                              6274 nymy    S                                            -uj
21749:     ni-mo5 ©<*ni-maud-                                                                                       jj u^<
21778:     ni-m(i)z ©<*ni-miz <*ni maig =*L} nym2}y,
21819:       <*ni-drdma-Jca ?                                        6302 nyst'y B, S                                <^j
21891:     niseS (nysyyS-, nysy5-) ©<*ni-sadaya-                          (to)destroy, (ro)spoil
21895:       86.8, 412, 5; nypy&tt, SCE 529, 3sg. subj.                   nistat ©*ni-stdta ©pt. st. =*nysty-, nst*t-
21899:     nisxway (nwsyw'y-) ©<*nis- xwahaya-
21918:     nistay ©<*ni-staya; OP nistaya-, \Tsta =»nsty-            6344 nyw)y6- B                          j^J^td^J'^^
```


## [2026-09-07T19:32:44.877Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"nyyr\\|ny\\^r\\|niyra\\|niyarb\\|niyrb\\|ni-yarb\\|ni- yarb\" SOD_pages.txt | head -20; echo \"=== 20642 ctx\"; sed -n '20636,20650p' SOD_pages.txt",
 "description": "Sogdian ni-grab search"
}
```


### [2026-09-07T19:32:45.005Z] TOOL RESULT

```
20697:         niyran-rf3c (nyrn* rwc) ©Pahl. anagrdn; Av.               5926 nyw*y- B                          o±±£ iozJ'sJ*-
23520:     pancmik (pnemyq) ©<-myk <-*ma-ya-ka                                panxsri ? =^pnyyr}y
23556:                                                               pnyyr'y ^pnyry
=== 20642 ctx
      niyame (ny'my) ^n* nytoy, trny'my
      time                                                           lay community
      Anc. Lett. 2.56                                                GMS 547, 111 In 1; KG 580; MSP b76
 5895 ny'my      M, B =* ny'mk                                  5905 ny'wsn'k B                                     ^^
                                                                     niyosne =»nywsnyy
 5896 *ny>rs- B                            u^^j
      niyars ©Benv. <*ni karsa & Mack. zY>rs                         listener, hearer
                                                                     BSTBL, Dhu. 179
           ^zy^s-
         0o)knock down                                          5906 ny'y- B                    o-^./ < j^*la5 < J->^>-
         TSP 7.33 apud. Hen. Texts. 733; BSTBL, Dhy.                 znixay ©<*ni-xwahaya ^nxw'y-, nyw}y-
           231
                                                                     (fo)pound, (ro)crush, (ro)cut
5897 nY*w6n(h) B, S                   ^^x «^r <crM                   TSP 2298 nYyytw n pl73.298; Hen. Texts. 72.8
     niyoSan ©ace. -w, -y; pi. -t =»nyw5n(>)/(h)                5907 nyp- B                                0>J*<J*
```


## [2026-09-07T19:32:51.441Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"ni-grab\\|nī-grab\\|nigrab\\|ni-gərəpta\\|nigrfta\\|ni-grfta\" CHEUNG.txt BRT.txt HRN.txt 2>/dev/null | head -20; echo \"=== cheung grab\"; grep -n \"^\\*grab\\|\\*grab-\" CHEUNG.txt | head",
 "description": "Cheung grab- entry"
}
```


### [2026-09-07T19:32:51.514Z] TOOL RESULT

```
=== cheung grab
8554:*grabH 119 
8589:*grabH ‘to grab, seize, take’ 
55324:*grabH (s.v.), *uat, *zanH?
```


## [2026-09-07T19:32:54.328Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '8589,8680p' CHEUNG.txt",
 "description": "Cheung *grabH entry"
}
```


### [2026-09-07T19:32:54.379Z] TOOL RESULT

```
*grabH ‘to grab, seize, take’ 

*AVESTAN: grab- (garab-) ‘to grab, seize, take’ || (+ *a-) ‘to grab (to)’ || (+ *uz-) "to 
lift, raise; to stretch out; to take out’ || (+ *fra-) ‘to seize; to accept, receive’ || (+ 
*ham-) ‘to seize (with the hands)’. Q YAv. goropta- forms are very late, being 
transposed from BMP /griftan/. = Liste: 20f. 

Pres. {1} nä-: IND. 3sg. YAv. goroBnaiti (Yt 10.13), 3р1. YAv. "fragroBnonti (Yt 10.104), SUBJ. Zeg, 
Y Av. *gorofnat (F 21), 3р1. YAv. garoBnan (Y 57.25); Pres. {2} aja-: IND. 35р. YAv. hangouruuaiieiti (Y 
10.2), 3pl. med. YAv. uzgouruuaiieinte (Yt 13.147), INJ. 3sg. YAv. gouruuaiiat (He 5.65), med. YAv. 
hangouruuaiiata (Yt 19.35 f£), 3р1. YAv. fora gouruuain (Y 28.0), SUBJ. 3sg. ҮАУ. gouruuaiiat (Yt 8.60, 
Yt 14.52), YAv. uzgeuruuaiiat (V 19.23, V 19.25), 3pl. YAv. auua.gouruuaiian (Yt 11.6), ҮАУ. 
hangouruuaiian (V 6.29), OPT. 35р. YAv. gouruuaiiöit, IMPV. 2sg. YAv. gouruuaiia (Y 9.28); Pres. {3} 
ta-: IND. 3pl. goroptaiieinti (Vn 80), SUBJ. 35р. uzgoroptaiiat (FrK 16), Y Av. porogoroptaiiat (Nik 18), 
3pl. YAv. goroptaiianti (Vn 80); Aor. {1} athem.: INJ. 1sg. OAv. hongrabam (Y 31.8); Aor. {2} s- (or 
pres. inch.?): SUBJ. med. Isg. YAv. hangrofsane (Yt 19.49, Yt 19.51); Perf.: IND. 15р. YAv. "jayauruua 
(H 2.8), 3sg. ҮАУ. à.jayauruua (N 54); Partic.: pres. {1} YAv. *%әгәВпапі- (Fr.), aor. {2} med. YAv. 
hangrafSamna- (Yt 10.105), perf. ? YAv. jagorobus?(V 4.48) 

*OLD PERSIAN: grab- ‘to seize (as possesion), seize (as prisoner)’ — Kent: 183b 

Pres. aja-: impf. IND. 1sg. agrbayam <a-g-r-b-a-y-m> (DB 2.4, DB 4.7, DB 4.32), < a-g-r-b-a-y-[m]> 
(DNa 17), <[a]-g-r-b-a-y-[m]> (DSe 16), <a-g-r-b-a-[y]-m> (DZc 8), 35р. agrbaya <a-g-r-b-a-y> (DB 
2.88, DB 3.74, DB 5.12), <[a]-[g]-[r]-[b]-[a]-[y]> (DB 3.90), med. 3sg. agrbayata <a-g-r-b-a-y-t-a> (DB 
1.42 f, DB 1.81), <a-g-r-b-a-y-t-a> (DB 3.82), 3pl. agrbaya" <a-g-r-b-a-y> (DB 2.13, DB 3.48 f), 
<a-g-r-b-a-[y]> (DB 5.27); Pass.: impf. IND. 3sg. "agrbiya <a-g-r-b-i-y> (DB 2.73, v. Hoffmann 1956: 
18) 


120 *grabH 


*MIDDLE PERSIAN: MMP gyr-, BMP gyl- (OHDWN-) /gir-/ ‘to take, seize’ || (+ 
*pati-) MMP pdyr- ‘to take, receive, accept’, BMP ptgyl- (MKBLWN-) /padir-/ ‘to 
accept, receive’ = DMMPP: 170a, 272b 

Pres.: SUBJ. 25р. MMP gyr’y, 3sg. MMP gyr’d, 3р1. MMP "gyr’nd, IMPV. 2sg. MMP gyr, MMP gyyr, 
Partic.: perf. pass. MMP "gryptg, MMP grypt, grypt, gryft, gryft || (+ *pati-) Pres.: IND. 1sg. MMP 
pdyr’m, MMP pdyrym, 3sg. MMP pdyryd, BMP ptglyt /padiréd/, 3р1. MMP pdyrynd, MMP pdyrnd, 
BMP ptglynd /padirend/, SUBJ. jee MMP pdyr’y, 3sg. MMP pdyr’d, 1р1. MMP pdyr’m, 3pl. MMP 
pdyr’nd, IMPV. 2sg. MMP pdyr, 2pl. MMP pdyryd; Partic.: perf. pass. MMP pdyryft, pdyrypt; Inf.: 
MMP pdyrptn, BMP ptglptn /padiriftan/ 

*PARTHIAN: gyrw- ‘to take, seize’, grysp- (pass./inch.) ‘to be taken, be held’ || (+ 
*uz-) ‘zgyrw- ‘to take out’, 'zerysp- (pass./inch.) ‘to be removed, taken away, out’ || 
(+ *pati-) pdgyrw- ‘to receive; take’ = Ghilain: 79, 89 | DMMPP: 170a f., 102a, 
101b, 269a 

Pres.: IND. 3sg. "gyrwyd, 3р1. “gyrwynd; Partic.: perf. pass. gryft, Pass.(/Inch.): pres. IND. 3pl. gryspynd, 
SUBJ. 2sg. gryysp’, grysp’h; Inf.: gryfin || (+ *uz-) Pres.: IND. 3sg. ‘zgyrwyd, 3pl. ‘zgyrwynd, SUBJ. 
lsg. *‘zgyrw’n, IMPV. 2sg. *‘zgyrw, 2р1. ‘zgyrwyd; Partic.: perf. pass. ‘zgryft, ‘zgryftg, П inch. ‘zgrysp’d 
|| (+ *pati-) Pres.: IND. 35р. “pdgyrwyd, 3р1. pdgyrwynd, SUBJ. 2sg. "pdgyrw, pdgyrw’h, pdgyrw’h, 3sg. 
pdgyrw’, IMPV. 25р. pdgyrw; Partic.: perf. pass. pdgryft 

*KHOTANESE: (+ *ham-) hamgrih- ‘to raise; uphold’ = SGS: 138 

*SOGDIAN: SSogd. (yrB- BSogd. yrf-, CSogd. yrb-, MSogd. yrß- ‘to take, 
understand, know, be acquainted with’ || (+ *uz-) BSogd. zyrf- ‘to exalt’, BSogd. 
zyrwDs- (pass./inch.) ‘to be raised (?) || (+ *pati-) SSogd. ptyr(y)B-, BSogd. ptyrB-, 
BSogd. pcyrB- ‘to accept, receive; understand’ || (+ *fra-) BSogd. fryrB- ‘to offer’ 
Widely attested: Pres.: IND. 1sg. SSogd. ’yıß’m, SSogd. yrB'm, BSogd., MSogd. yıß’m, dur. CSogd. 
yrb’msq, CSogd. yrb’msqn, 2sg. MSogd. yrbyy, dur. SSogd. yrBy skwn, CSogd. yrbysq, 3sg. BSogd. 
yrBty, etc. || (+ *pati-) Pres.: IND. 3sg. BSogd. ptyrBty, SUBJ. 1sg. pcyrB’n, 3sg. BSogd. ptyrB’t, OPT. 
2р1. BSogd. pty’ysö, BSogd. pcyrBty, POT. 3sg. BSogd. pcyrB't wnty (SCE: 369); Impf.: IND. 3pl. 
BSogd. ptyyrB’nt, Partic.: pres. MSogd. (pl.) “ptyrBynyt (Sogdica: 25), perf. pass. SSogd. ptyryBt, Inf.: 
BSogd. ptyıß’y || (+ *fra-) Pres.: OPT. 3sg. BSogd. BryxB’y; Impf.: IND. 3pl. BSogd. fr’’yrß’nt 
*CHORESMIAN: xf- ‘to take, grasp; to befall (of illnesses)’ (*grfsa-), yBy- ‘to 
consider, take (for), regard as; to grab’ ( *grbaja-), yfs- (intr./inch.) ‘to be silent, keep 
quiet’, xFs- ‘to be covered’ || (+ *api- or *upa-) byBy- ‘to sense, find’. © On the 
different continuations of *grabH in Chor., see Humbach 1973: 95. = Samadi: 234 
f., 76 f., 236, 18 

*BACTRIAN: (+ *pati-) лібороВ- ‘to receive’ = S-W, Bact.: 218 f. 

*NWIR: Widely attested: NP giriftan/gir-, Bal. gipt/gir-, Kurd. girtin/gir-, Zaz. girewt, 
girotis/gén-, (subj.) gir-, Abyan. geratan, Anar. ha’m-igirif/ (impv.) ha-gir, Awrom. 
girtáy/ger-, Abz. grata/ger-, Abyan. gerata/ger-, Anar. girefte/gir-, Ard. girette/gir-, 
Fariz. -girät-/-gir-, Yar. -girit-/-gir-, Gil. (Rsht.) giftoen/gir-, Gur. (Kand) gird-/ 
-(g)ir-, Isfah. giftän/gir-, Jow. bam-gat/ha a-gi:r-, Meim. bem-ga/a-gi:r-, Ham. 
geftän/gir-, Mah. gir-/git, Nn. girefte/gir-, Natan. -geret-/-gir-, Qohr. gerata/yr-, ger-, 


*grait/grai0 ? 121 


Tal. gate, Tr. gata/ger- ‘to take, seize’, Mah. he-geftän/he-i-gir-, Sorkh. -git-/-gin- 
‘to buy; to take’, Semn. -git-/-gir-, Sang. -gird/gin-, Shamerz. -gít-/girám-, Lasg. 
-git-/gin, Soi gir-/a-ir- ‘to take, seize’ || (+ *pati-) NP paóiruftar/paóir- ‘to receive, 
accept’ 

*NEIR: Oss. I. argeevyn/ergevd, D. erguvun/arguvd ‘to lift up, settle at, with; to pull 
the trigger’, D. ergzevun/ergavd ‘to hit the target; to grab, seize’, Yghn. yirrw- ‘to
```


## [2026-09-07T19:33:03.180Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"grb-\\|garab\\|'grb\\|gsrsb\\|gorob\" BRT.txt | head -20",
 "description": "Bartholomae grab root"
}
```


### [2026-09-07T19:33:03.259Z] TOOL RESULT

```
11608:6o7  j^^garabuStara-
11614:•  j.  JägarabuS'tara-  Adj.  'der  besser  er- fasst,  begrifTea  hat',  mit  Akk.verb.:  hSuea ^afiayS  narä  vohu  matiB  °tarB  anhat  yS.. "und  der  von  den  beiden  Männern  hat den  guten  Sinn  besser  erfasst,  der  .." V.  4.  48.
```


## [2026-09-07T19:33:09.475Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"ni'gan\\|ni\\.g\\|ni'g\\|nl'g\\|nl\\.g\" BRT.txt | head -20; echo \"==== ni- headwords\"; grep -n \"^\\s*[0-9]* *[•·] *j\\..*\\bni\" BRT.txt | head -30",
 "description": "Bartholomae ni- headwords"
}
```


### [2026-09-07T19:33:09.558Z] TOOL RESULT

```
4688:•  j.  atnae.ni'gan-:  niyn-  Adj.  (auch  fem.) 'beim  Angriff,  Anlaut  niederschlagend': rfrf^raynsm  . .  -niyn^m  (als  Asn.)  Yt.  i<). 54;  —  mit  Akk.:  /ravasayö..  yn..  'nijanö (NPf.)  Aam^>>!  Yt  13.^5.
27642:•  j.  zaini'gav-  m.  EN.  eines  von  Frat»- rasyan  getöteten  Feinds  des  iranischen Volks:  yim  (näml.  wa^ä?«)  barat  fratirait iBrB  yat  drvä  'gaul  jaini  Yti^.  93,
==== ni- headwords
2547:•  j.  aetada  Adv.  i)  'hier,  da;  dort';  °ia'  •  j.  aeta'vant-  Adj.  'tantus,  so  gross,  so hl  uzbao'jitm  tanäm  nidai'iyqn  V.  5.  12;  viel',  nur  Neuir.  (mit  Gen.  part.):  'vat 45,59,  6'.46,Äii,  100, /Ö.2; —  'oa  an-  alsascit  ästnraytili  (sd.)  N./:i;  —  °%-at hava  asti-ainti  V.rf.i;  • —  bariinava  paiti  ^AuSkanqm  aismanqm  "vat  naptanqm  V.j.
2712:•  j.  aevo.pad-  m.  '^in  Fuss':  'pao?m\_  f^t  ai  vi  vinzyämahi  fracä  vmyä- niäaiaiU  aiU  aniar3.anvm  nmrmaheYtA^ahiya'ti  wJmarrti' (Konj.)*> "wir  wollen ''"^■"t-    ^  jes  betätigen  und  es  (anderen)  zum  Ver-
2743:•  j.  aesmö.barvtay-  f.  'Darbringuog  von  isa^ta  Yt.  i^.  53;  — yff  naeeim  isaiti  huna- Brennholz':  alvayacif  °niii  (IS.)'*  aiva-  ranqm'V.ij.i9;Aog.48;  —  äiä ..Ayämii , . yacit  bar7sm3.stir?iH  Y.24~  aiavanö  tnsyä  istsm^^  rJiVl'(sd,)  Y.  40. 4;
2899:•  j.,  g.  'ao}ah-  n.  '(physische)  Kraft,  Stärke': asistim  narl  alaotw  °Jö  Y.  60. 3;  —yakmi niyne  nars  'Jartha  Y.  /o.  a ;  —  ai-avaia '}arfka  yaia  yal  panca  narS  "mit  solcher Kraft,  als  wären  es  fünf  Männer"  V.  jj. loPaZ.;  Yt,2.i2,  14;  —  usla  U yd  ä"j 'jaiika  vasöjciairä  ahi  haoma  Y.9.25; —  kacaiti  dim  aspahe  "Jö  uitrahe  °Jö vlrahe  °j<>  Yt.  it).(i&;  8.2^^;  —  "jö  tanvö vispaya  Yt/.^.29;  —  -jö  vJspdMnüM  Y. 5.17;  —  drfahela  paiti  °)arakö  Yt,  i_j. 134;  ~-  y~'  itfsfro)  arinam  ..  matilüm 'jö  abaraiii  \t  14.12;  —  apa  .  .  buei'ä- °}5  , .  barahi  apa  pä',ayä  sävar»  Yt.  10. 23;  62;  —  haomö  asibil  yöi  ..  zävari "jssca  baxhili  Y.  9. 22; —  °Jasca  nn- S«)Wf'a..Y.  77.8,  yi.j.22,y.i,Y.  72.6;  — yS  nü  asSif  °janAil  vandayaÜJ  (sd.)  ., gae^am  Y.50,3.  a)  AS.  °jö  als  Adv,
2947:•  j.  aobg-  V,  'niederhalten,  -drücken'. Praes.  27  (Pass.)  ubjya-,
3038:•  j.  'a-karäta-  Adj.  'nicht  ausgesät'  sva..  \ syaaina  V.j.zi';  i.  ii,  12,  16;  —  'ya 'nicht  durch  Aussaat  gewonnen,  wild  ge-ljrätava  V.i.i^;  F. 7;  —  °y?mäi  vimanö.- wtLchstn':  j'ovanam  ..  aetavat  karstanam' AJtn  V.J.  7;  15;  —  'yanqm  ma^ranqm altavat  °tanam  "Getreide  ..  so  viel  vom  Vt.  10.  20;  —  -yqm  ifaaiirim  (sd.)  YL gesäten,  soviel  vom  wildgewachsenen"  V.   z^.  57;  V.  j().45;  —  'ya  danta  läsyä^  (sd.)
3043:•  j.  'a-karsta-  Adj.  (fem.  Uä-)  "nicht  be- pflügt, ungepflügt':  Tm  sä  .  .  yS  danya 'ta   salta  yä   karya   karsivata  (sd.)   V.
3121:•  j.  "^a-yzö.nvamna- ''  Adj.  'sich  nicht mindernd,  verkleinernd*;  mazdqmcä  ahu- rsm  yaa'byü  xsa^r»mca  "tum  varidaitl ärmaitis    "und    den  MAA.  und    (all)   die,
3143:•  j.  a-x§nüta-  Adj.  'nicht  zufrieden  ge- stellt': yezi  aesö  nn  yö  yaozdai:ryö ..tbistö "tö  paräili  V.  9. 40.
3162:•  j.  a-ciBra-  Adj.  "nicht  offenbar,  undeut- lich': '^nJ  F.  7.
3179:•  j.  a-]astay-  £  'Nichtbitte':  yat  nil  kasz'i- kqm.'ina  . .  'ta  (LS.)  . .  daoäiti  "wenn  er bei  Nichtbitte  (sva.  'ohne  darum  gebeten zu  sein')  '>  . ."  V.  /Ä37.
3181:•  j.  *a-}iÄyanma-  Adj.  'der  nicht  gebeten wird' ;  tiiirlm  ,  .  yö  daoäili  .  .  jaioyantäi ■•Uli/  Hiaryai  ".  .  der  dem  Bittenden  ohne Gegenbitte  schenkt'"»  YtÄ49.
3192:•  j.  a-tanu.maOra-  Adj.  'der  das  heilige Wort  nicht  in  sich  aufgenommen  hat': zaota  ana/ara  adahmö  'rö  Yt.  70. 138.
3242:•  j.  a-8avay-  Adj.  (auch  mask.)  'der  keinen Trug  übt,  nicht  trügt,  betrügt':  *''T'r/(NSm.) nama  aAmt  *vtöavl/  nqtna  ahmt  Yt.  /.  14; —  n^mö  voku  °vim  (ASm.  statt  n.)  aibai- hm  Vr. 21. 3,  Yt  luz;  —  yeiihe  vähm Äangryuinäili  "vil  (NSf.)  paoirls  (sd.)  .  . i4ä  *dämya  (sd.)  xlaztäi  Yt.  iO,  143.
3256:•  j.  adairi  Praep.  'unter,  unterhalb';  i)  mit Akk.:    ao'  hax>m  nivöiryeite  V.  <¥.  69;  —
3262:•  j.  aSairi.naema-  m.  'die  untere  Seite': "^wamca  drujitnca  niüamn  'ntpmca  Yt4-
3269:•  j.  a-dahma-  Adj.  'der  nicht  dahma- (sd.),  nicht  unterrichtet  ist';  saota  anasava "mö  atanu.tnai<r3  Vt./o.iaS;  —  jahi  .  . yö  xsudrh  ham.rasiwayeiti  dahmanam 'manamca  V.1S.62.
3272:•  j.  a-dätay-  f.  'Nichtgeben,  Nichtdar- bringen,  Verweigerung':  «J  gJu/  ml  vas- trahe  hatö  "oditlm  vaocöit  "man  soll  nicht das  Nichtgeben  eines  wirklich  vorhandenen Fleischstücks  oder  Kleids  behaupten"  V. 4.46'*; — paoiryeheca  nH  myazdake  'oätii {]Si.) yat  mai'iydi.sar^myeAe"\inA6.zi:iz,Aa:&s man  den  ersten  My.,  den  des  jW. -Festes, nicht  darbringt"  A.  j.?;  8-12  (,  SWienAW. (17,839);  —  kat  «3  *dazi'ayasnäi  vä  .  . giul  'iaitya'"  ästryeiti  "begeht  man  da- durch Sünde,  dass  man  einem  Z>. . .  kein Fleisch  gibt?"  N.  i(?; —  •oaiti  */rilraihya-
3279:•  j.  a-8äitya-  Adj.  'nicht  so  wie  es  dem Gesetz  entspricht,  ungesetzUch,  ungehörig': duityanam  raiwyanqm .."yanqnt  ard^wya- tiqm  ^ao^nanamYr.  ij.i.  [N.io-:lies äiiityö.]
3281:•  j.  a-Säityö.aDharaSra-  Adj.  'der  nicht  i
3286:•  j.  a-8äityo.]fratav-  Adj.  'der  nicht  den gehörigen  Verstand  besitzt,  nicht  recht  bei Verstand  ist'  (vom  Hund):  yat..  sp3  avacä (sd.)  V1I  bavat  "/wx"  V.  y,  29;  31;  — yat .  .  spii    a/iqm.baoii>mn5  vä   bavat  "tu/  V.
3288:•  j.  a-Jiäityö-draonah-  Adj.  'der  nicht die  gehörige  Nahrung,  Kost  hat':  dahmS niuruzdö  (sd.)  'nä  N.  77;  —  *gai-sstryaca vansna  *v»r3zyantö  .  .  'nauhasca  *hmtö N.52.
3302:•  j.  a-dsrata-  Adj.  'nicht  geemtet,  ge- schnitten': aäavat  dirttanqm  (sd.)  a^tai<at 'tanqm  (yavanqm)  V,  7.35.
3304:•  j.  a-daratö.tkaesa-  Adj.  'der  den  Lehrer nicht  achtet':  vlspe  drrantö  tanu.drujö yS'^ •sd'''  vXspe  'sS'*  yß'>  asnifs'ß'''  "alle  sind ungläubig  und  leibhaftig  mit  der  Dr.  ver- bunden, die  den  Lehrer  nicht  achten;  all die  achten  den  Lehrer  nicht,  die  (ihm) ungehorsam  sind"  \.i(J.i8.
3326:•  j.  a-dbi§ta-'>,  a-tbiäta-'>  Adj.  (fem. °/p-)  'nicht  angefeindet,  gekränkt':  iitar/.. xsnStä  °tö  \.62.^;  Yt  lO.iio,  V.(j.39,  Yt. '3-^5'  —  xsnataheat  'tahe  mi>ra  manS yaozayeiti  "(aber)  auch  des  befriedigten, ungekränkten  Sinn  bringt  er  durch  M.  in Aufruhr"  Yt  /o.  1 1 1 ;  —  xsnUth  ainili  °t^ ..  fravaiayö  Yt/y.si;  34i  63;  —  "'"^ (VS.)  Yt/2.8.
3354:•  j.  a-dnig-  Adj,  (auch  mask.)  'der  keinen Trug  ausübt';  lätn  (tümL mi^ rti)  ..nipJ/a ahi  'u'zam   (GPm.)   Yt /O.80;   80.
3406:•  j.  aS'ä-  f.,  Plur.  'Grund  und  Boden, HoP:  yö  nSit  nar>m  alavamm  hvahva ''iä&va  JasSntfm  xsnaoita  va  xsnävayeite vä  "wer  einen  Gläubigen,  der  auf  seinen Hof  kommt,  nicht  bewirtet  oder  bewirten lässt"  V.4g-
3413:•  j.  *a-ftTvayaDha-  n. 'NJchtgefahr,  Gefahr- \a%\^^\'C:*a'i:ra'"tih}m>''ya'i:raratui'i:wa- yar)k?m  ya^ra  apprmaynkö  3  *hg  "aini- iritim  starydti  ar,a  yat  v3  ya'^ra  '^waya- n/um  va  "»fum'^  t^S  "(ist)  daNichtgefahr, wo  der  R.,  Gefahr,  wo  der  Knabe  (sich befindet),  so  begeht  er  Sünde,  wenn  er ihn  (dem  Ratav)  nicht  anvertraut;  und (auch)  wenn  beide  (sich  an  einem  Ort befinden),  wo  sei  es  Gefahr  oder  Nicht- geiahr  (ist)"  N. /o'\
3493:•  j.  apaosB-m.  Name  eines  Z>ii^'a*\  beson- ders des  Gegners  des  Tisiry a  {sd.):  a  dim (näml.  tistrim)  paiti.yas  nizdvaraiti  dalvd yö  °sö  aspake  k)hrpa  sämake  Yt.  tV.  21; 22';  —  ä  dim  bavaiti  aiwi.vanya  tistryö . .  daFnm  yim  °S>m  Yt  <.V.  28;  —  tauna- yeiti  dalum  "sjm  Yt  /Ä  2;  6.
3508:•  j.  apa-j-zära-  m.  'Abfluss,  {Wasser)ab- zwejgung'  a)  des  VouruAasa:  srayä  vouru.- kasaya  .  .  yeäke  . .  Aazannm  -ranam  . . kasal  aSsqm  °ranqm  c(&war>.sat»m  ayan.- baranqm..*arihas(a  me  *afi:aAka  Spö 'rö *vt)asaiti  vispJis  aoi  karsvqn  Y.  65.  4  £; —  aija  käu  'rö  bvat  zrayanAs  vouru.- kaiahe  vairil  yH  Aaosravä  nqma  Yt  ig. 56;  —  zrayauhs  vouru.kasahe  ,  .  vTspJ rairi/  a^araiti  vlsp}sca..nimraoi!  vlspSsca srlr!  'äire (AP.)'> \i.8.i,f>;~ katiht kaüht •,lire(XS.)  Ytj.ioi.  b)  der  Ratfka:\ tipa  guoim  'r>m  ra»hayh  Yt/5. 27,  j
```


## [2026-09-07T19:33:20.284Z] TOOL CALL #34: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['BQT','MON','HRN','HUB','POK','KLN','SOD','AHD','PHD','ARY']:\n    print('==',k); print(json.dumps(d.get(k),ensure_ascii=False,indent=1)[:1500])\n\"",
 "description": "Check refs_online for page offsets"
}
```


### [2026-09-07T19:33:21.610Z] TOOL RESULT

```
== BQT
{
 "title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)",
 "kind": "archive_djvu+local_scan_ocr",
 "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.com (links from farhangoadabeirani.blogsky.com post-482): vol 3 https://s3.picofile.com/file/8230740968/borhane_ghatee_jelde_3.pdf.html (ش–ل, Ibn Sina 2nd ed. 1342, 721 pp), vol 4 https://s6.picofile.com/file/8230741184/borhane_ghatee_jelde_4.pdf.html (م–ی, 553 pp), vol 5 https://s3.picofile.com/file/8230741300/borhane_ghatee_jelde_5.pdf.html (تعلیقات, Amir Kabir 5th pr. 1376, 293 pp). Same set behind login on ketabnak.com/book/55304-55307 and /58249.",
 "lookup_hint": "grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \\f; leaf N = N-th \\f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={
== MON
{
 "title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)",
 "kind": "website+archive_djvu",
 "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)",
 "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different pagination from the 6-vol edition; OCR downloaded as MON_part1.txt / MON_part2.txt (no page breaks).",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf",
  "/home/sfmqrb/git/rishe/data/ver
== HRN
{
 "title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893",
 "edition_found": "1893 (Google scan, Univ. Michigan)",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/grundrissderneu00horngoog",
 "identifier": "grundrissderneu00horngoog",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt",
 "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.",
 "notes": "OCR of German Fraktur-free text is decent; Persian script is not OCRed.",
 "cites": "page number of Horn, Grundriss der neupersischen Etymologie (1893); entries are also numbered"
}
== HUB
{
 "title": "H. Hübschmann, Persische Studien, Strassburg 1895",
 "edition_found": "1895 (Google scan)",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/persischestudie00hbgoog",
 "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt",
 "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by paragraph (§). grep the transliterated Persian word or Horn's entry number.",
 "notes": "Built from djvu.xml (no hocr); OCR quality moderate.",
 "cites": "page number of Hübschmann, Persische Studien (1895)"
}
== POK
{
 "title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)",
 "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/indogermanisches01pokouoft",
 "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt",
 "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-dictionary/ (entry pages with page numbers) and StarLing https://starlingdb.org/cgi-bin/query.cgi?basename=\\data\\ie\\pokorny&root=config",
 "notes": "Nourai's page numbers are Band I 1959 pages, which match these scans. Band II (1969 index) is at pokorny-indogermanisch
== KLN
{
 "title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67",
 "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein",
 "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt",
 "page_offset": "KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.",
 "notes": "Other 1966 IA copies (comprehensiveety01klei/02klei etc.) are lending-only (401/403). local_files: /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt (paginated by leaf); /home/sfmqrb/git/rishe/data/verification/sources/refs/
== SOD
{
 "title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/SogdianDictionary",
 "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/SogdianDictionary for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD.txt"
 ],
 "page_offset": "printed page ≈ leaf − 66 in SOD_pages.txt (0-based \\f blocks; 645 leaves; English intro precedes)",
 "covers_etymology": true,
 "notes": "OCR: Sogdian transliterations, entry numbers, English glosses and bibliographic refs (GMS, BSOAS, VJ ...) are readable; the Persian glosses are garbage (OCR'd as Latin). Full scan, 1995 edition = the one Nourai used.",
 "cites": "entry number / page in Gharib's Sogdian dictionary"
}
== AHD
{
 "title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)",
 "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)",
 "kind": "archive_djvu+website+archive_restricted",
 "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only",
 "identifier": "watkins-american-heritage-dictionary-of-indo-european-roots-1985",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt",
 "page_offset": "1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page.",
 "lookup_hint": "Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru-' ; entries list English der
== PHD
{
 "title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971",
 "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/a-concise-pahlavi-dictionary",
 "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt",
 "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Headword = Pahlavi in transliteration at line start, followed by Pahlavi script (not OCRed) and gloss, e.g. grep -n '^abar '. Alternative PDF: https://www.parsianjoman.org/wp-content/uploads/2015/09/A-Concise-Pahlavi-Dictionary.pdf (8.4 MB).",
 "notes": "",
 "cites": "page number of MacKenzie, A Concise Pahlavi Dictionary (1971)"
}
== ARY
{
 "title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.",
 "kind": "local_scan_ocr",
 "url": "",
 "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY:<printed page> --image",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt"
 ],
 "page_offset": "printed page = pdf page + 1",
 "scans": [
  {
   "file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_aryanpur_kashani_rishehaye_hend_o_orupayi.pdf",
   "first_printed": 1,
   "last_printed": 546,
   "pdf_offset": -1,
   "lang": "fas+eng",
   "ocr_text": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_pages.txt"
  }
 ],
 "notes": "Image-only PDF provided by the owner (2026-09-04). Use as an additional modern source alongside Wiktionary/Cheung/Hasandust when judging Persian arrows; cite as ARY:<page>. | full OCR text fas+eng (headwords in Persian and Latin
```


## [2026-09-07T19:33:33.875Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nL=open('SOD_pages.txt',errors='replace').read().split('\\n')\ndef near(n):\n    out=[]\n    for i in range(max(0,n-400),min(len(L),n+400)):\n        s=L[i].strip()\n        if re.fullmatch(r'\\d{3}', s):\n            out.append((i,s))\n    return out\nfor target,label in [(21015,'np\\'yδ- 6033'),(21918,'nysty- 6332'),(21240,'nsty- 6091'),(20628,'ny\\'m niyam 5893'),(20906,'nimay')]:\n    print(label, near(target))\nEOF",
 "description": "Locate Gharib printed pages"
}
```


### [2026-09-07T19:33:35.268Z] TOOL RESULT

```
np'yδ- 6033 [(20646, '231'), (20669, '237'), (20735, '238'), (20806, '239'), (20882, '136'), (20945, '241'), (20970, '252'), (21021, '242'), (21099, '243'), (21172, '244')]
nysty- 6332 [(21537, '249'), (21614, '250'), (21690, '251'), (21757, '252'), (21830, '253'), (21904, '254'), (21978, '255'), (22046, '256'), (22115, '257'), (22180, '258'), (22255, '259')]
nsty- 6091 [(20882, '136'), (20945, '241'), (20970, '252'), (21021, '242'), (21099, '243'), (21172, '244'), (21537, '249'), (21614, '250')]
ny'm niyam 5893 [(20239, '231'), (20383, '233'), (20445, '183'), (20452, '234'), (20534, '235'), (20600, '236'), (20646, '231'), (20669, '237'), (20735, '238'), (20806, '239'), (20882, '136'), (20945, '241'), (20970, '252'), (21021, '242')]
nimay [(20534, '235'), (20600, '236'), (20646, '231'), (20669, '237'), (20735, '238'), (20806, '239'), (20882, '136'), (20945, '241'), (20970, '252'), (21021, '242'), (21099, '243'), (21172, '244')]
```


## [2026-09-07T19:33:48.025Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"########## PAGE 244\"; sed -n '21099,21172p' SOD_pages.txt | grep -v \"^\\s*$\" ; echo \"########## PAGE 252\"; sed -n '21690,21757p' SOD_pages.txt | grep -v \"^\\s*$\"",
 "description": "Print Gharib pages 244 and 252"
}
```


### [2026-09-07T19:33:49.356Z] TOOL RESULT

```
########## PAGE 244
                                                        .?^"j^*%^^                                   &&:
 243
                                                                                                              nsk'rt
        VM242                                                 6071 nsty C, S                                    ai~x
                                                                   niste (nscO ©pp., f. pp. nisca =*ny§-, nystch,
 6059 nrs B                                         J^j^
      nars                                                            nysty1, nyst'y
                                                                    seated
      blame
                                                                    STi 36.9; BSTii 889.22: C2 gloss.; f. pp. nsc\ C2,
      VJ223
                                                                      60R22, 25, 60V27, 87R12: BSTii 878.12; CII
6060 nrt(h) M, S                            (^')^>>^                  1990 G14
     nart
                                                              6072 ns'y- B            o^loi- <a>&l^>T t^jfj^j
       trunk
                                                                   ni-say ©<*ni-0ray- ? =*Ps}y-
       GMS 526, 1399; Sogdica. p 4.11; Frag. Len. 84a8
                                                                    (ro)put down
6061 nrystr C = n+rystr =# n-, rystr
                                                                    TSP 22.18 n p235; Schwartz. STSC 140 "to be
6062 nrysnxPvyy  M      c~~jj> :^yl> Jilj^ j0->>„ <~*~±J
                                                              6073 ns'yS- B, S                 -^ < jojUj <c»kJJ lo^
       nar(i)snax ^nr'ysp yz5                                         aborted"
       Narisaf yazd(a Manichean god, friend of                     niseS  ©<*ni-sadaya-      ©impf. nyPyS; perf.
         light ?, third Messenger ?)                                  nPStSyr- =»nsyd-
                                                                    (fo)set, (ro)place, (ro)piant
       BBB; W-Li 40.13, ii 540; nrsnx, W-Li 40.117;
                                                                    GMS 545; Frag. Len. nPyStdr-, 38.17, 7, 19.38.26;
         "Friend of light" ? Sund. KG pi 86, " Narisaf                VJ 864; AVS 78
         yazd", Tertius-Legatus; Sund. AoFvi 1976,
         101; Gcrsh. Amber. 213, El. narisanka                6074 ns'ySHch B                                  Jz-ai^
                                                                   ni-se8c ©pp. f.
6063 ns M                                    (^J^lo*^
     nas =>nns                                                      set, established
       nose                                                         VJ 1118; GMS 537
       BBB p79.659; GMS 338, 496                              6075 ni-se5te
                                                                   nFyStCk) B                                  j^,^
                                                                            ©pp.
6064 ns»t C = n+s>t => n-, s»t
                                                                    established
6065 nsc> C =» nsty                                                 TSP 8.196, 10.21
6066 nsnng M                                   S nS^^
     nasang ©Pahl. nisang ©f. n.                              6076 nsYwst- B                   o>J'*J»iJ>J'*^*b*
     little                                                        nis-xwast, nisxust (nsywst-) ©pt. st.
     Sogdica. 31.5b n p32
                                                                     ^nsyw'y-
                                                                   0<?)cut in pieces
6067 nst C                                              c~j
                                                                   VJ 1265, 780; TSP 16.37
     nest =>nyst
     is not                                                   6077 nsyw'y- B               j-i^p <ukS-uIo$ c Oi^p 6jL
       BSTii 892.10; Benv. JA 1955, 325; C2 gloss. p232            nis-xway (nwsyw^-) ®<*ni$-xwahaya
                                                                     ©impf. nysYwy ^nsy'wst-, nysyw'y-
6068 nst-1 M, C                                     j^j            (ro)cut in pieces
     nist ©pt. st. =*nyst-, ny5-
                                                                   BBB 505; GMS 679; AVS 95
     Go)sit down
     BBB 574                                                  6078 nsywst- => nsy'wst-
                                                              6079 nsywsty B
6069 nst-a C                          j^x «o*je j^U «jjuU          nis-xuste ©pp.                           oJb j> iaJU** jw
     nist?
       (/c>)stay, (rcOdwell                                        0c)cut in pieces
                                                                   VJ 1105
       Benv. JA 1955, 310; nsty, STii 1.18; BSTi 167;
         nsc\ BSTii: C2, 87R12                                6080 nskVt B, S
                                                                   nis-kart (nsqrt) =»nskrt
6070 nst'wy C                    ^jJ^IJs-t&jktj^                   meaning, explanation
     nestawe/e ©ace. -w; gen. -y; abl. -} =»nyst}wy                                                           C^*'^
                                                                   BBB; TSP 2.56, 945, 1071, 5.9, 9.138 & etc.; SCE
     perdition
     BSTii: C2, 40V 12, 52R4, 13                                     535; STii 7.4, 23; Frag. Len. 85.5; GMS 678;
########## PAGE 252
     VJ 23c, 8d; TSP 9.139, 15.23; BSTBL, Vim. 178,
 251
                                                                                                               nymyBw'dy
       nizene ©pi. -t ^nyz^y                                           GMS 626; Hen. Tales. 467.35; AVS 91
       emanating                                                  6268 nym'yS B, M, S
       GMS 895, 1249                                                   nimcS (nymy8, nymy8, -my5)                  yJ tf L* 'jM
                                                                       to it, to this
6256 nyjyt- M                                          0-C<£>-
                                                                                                                  'r*r*
                                                                       TSP 2.436 "in this"; GMS 1404, I486; BBB b88;
     niz(i)t (nyzt-, nyjt-) ©<*nizita     ©pt. st.
       =*nyzt-, nyzyt-, nzt-                                            MD
       (to)go out                                                6269 nymn'y B => V nymz'y
       GMS 539n 1, 568; BBB, pl30                                6270 nym nym M
6257 nyk B                                         ^_^<jC;             nem-nem
                                                                       half and half
     nek ©MP nek <*naiba-ka-
                                                                       GMS 1633
        good27.3a, 3-, Frag. Len. 44.11
       TSP                                                                                            jjLi-^^^-i ijjL^jli^f
                                                                 6271 nyms- B
                                                                      ni-yams ©inf. -}y, -7
6258 nykr'n B                (fjj" <Jj^)>=r <'-*?- <j' £j^
     nikran (nykyr'n) ©*niz A v. karan-                               GcObe caught
     apart, apart from, outside, except                               VJ p219; Hen. Texts. 715; TSP 2.858, 6.147; AVS
     BSTBL, Dhy. 122, 158; TSP 2.866, 6.67; GMS                         74
         1148, III; nykr>nwy Vim. 133                            6272 nymt- M, C                                     oj&J&J*
6259 nykyr'n      B, M =» nykr'n                                      ni-yamt, nimt ? ©<*ni-yamt        ©pt. st.
6260 nym S                                                            0o)be caught
       ncm    ©Av. naema     =>nymy(y)                     <r-        GMS 539.4; AVS 74, 101
       half                                                      6273 nymty M, C                                   <$^ tjss^
       MDii; Anc. Lett. 4.4, 5.25; GMS 81, nim                        niyamte ©pp.; pi. -/
                                                       "Sj^r          caught
6261 nym'k1 S =» nymy(y)
                                                                      GMS 835; STi 79.6, 78.13; BSTii 829.1: C2 gloss.
6262 nymV     B                         j^A
     nime ©<*nimaka                                              6274 nymy    S                                            -uj
                                                                      neme    =^nym, nymy(y)
     lower, innfcrior
     TSP 3.177 n pl97; Mack. BSOAS 33.119                             half
                                                                      MDii p206, MDiii pl24; CII 1990 B4 E18
6263 nym'n     B                          *xjf^j&c tj&j>
     niman ©ob. pi. -ty =»*nm-2                                  6275 nymyS    M, S =* nym'yS
     haughty, contemptuous                                       6276 nymyficyk M                  j^'^^'jjj**^^ ^y-s*
     GMS 291; SCE 370; TSP 5.61; BSTBL, Vim. 164                      nem-me0clk
6264 nynVntCy) B                        h^J c?L* '^J                  meridian                                          <jj^y
     nimand(eVnimandi                                                 GMS 81, 1014; BBBd3
     these, to these
                                                                 6277 nymy8(h)    M, S                   ^>
       TSP; GMS 1501
                                                                      neme9, nem-me9      ^nymyGw'dy
6265 nym'ntyh      B                                                  south, noon
       nimandya    =**nm-2                       ^Ay     i^JC^        GMS 81; BBB p69; W-Lii 546.13; MDii p206
       contempt
       SCE 75; TSP 5.52, 72; GMS 291                             6278 nymyS kyr'n M
                                                                      neme8-kiran =^kyr}n
6266 nym'wS- B                             JJLj^» LO$J> </lj          south
     ni-mo5 ©<*ni-maud-                                                                                       jj u^<
                                                                      BBB p99 d3; GMS 81
     (to)lament ?
     BSTBL, Dhu. 296                                             6279 nymyflw'dy C
                                                                      nem-me9-wa5e      =^kyr*n
6267 nym'y' M                                    O^J    OjUaS
                                                                      south
     nimay ©impf.       ^nnVy-1                                       BSTii 858.17: C2.23R17                   jjy*-?'
     GcOjudge
```


## [2026-09-07T19:33:59.903Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=20200 && NR<=22300' SOD_pages.txt | grep -n \"yr\\|grb\\|grab\" | head -40",
 "description": "Search grab forms in n section"
}
```


### [2026-09-07T19:34:01.148Z] TOOL RESULT

```
16:        5747 n'yrpty M
18:             na-yarPde, na-yrapde
25:             na-yarPene =»L} yrPyny
170:5795 n'myrync
237:5817 n^yrywzy C(S)                 (a/J
330:                                                                          5858 np'yr-  B, S              jj/^p^/^
331:            Sund. MHC 31                                                       niPer ©impf. nyfiyr =»npyr-
342: 5859 np'yr B                                   ^yjj^jj^             nap/fd/te (nptk) =4npty(y)
347:5860 nP'yr'kh      B, S                   •jj^^>Jj^j>^                naftca ©<*napdca', Av. napta-, Khwar. nflc
348:       nipera(k) =*nP}yr-                                               ©f. adj. =*nftt
353:5861 np'yrtk      S                                             5876 npty(y) M                                 jly<v>^
358:5862 npy- B                         jisv^^                      5877 nPyr-    M                                o^oj^
360:                                                                      niPer ©impf. nyfiyr ? ^nPyr't-, nP>yr-
365:                                                                5878 npyr't- M                                 O^/ojyL,
367:                                                                      niPerat ©pt. inf. **nP*yr-
487:                                                                         MDii B-3, 10; nYsyr crm, naxsir- carm, MDiii
488:     5911 nyr^y- B                         ax-*^ *o>j^>
489:          ni-yray (nyr'y-) ©<*m-£ra; Av. gar-gd; IE
490:                                                                   5925 nysyr B, S                 j^^/y.^^^
492:            SCE 542; BSTBL, Vim. l8lvDhy. 320, nYr*y>U                    -fypl24^nys'yrCh)
495:    5912 nyr*my      C = n+ yr'my =» n-, yrWk
497:    5913 nyr'n rwc S           (o^'-^j^)^^ \s*<jjj(iP
498:         niyran-rf3c (nyrn* rwc) ©Pahl. anagrdn; Av.               5926 nyw*y- B                          o±±£ iozJ'sJ*-
505:    5914 nyr'y- ■* nyr*y-
507:    5915 nyrf C = n +yrf -> n-, yrf                                     excellent, kind, fine
508:    5916 nyrn* rwc -» nyr'n rwc                                         BSTBL, Dhy. 153, 363; GMS 445
509:    5917 nyrs- -* ^yrs-                                            5928 nywp'w'k B                                ><^>^
510:    5918 nyrwps- S                  0-^»->^j> <ooiojjii                 nayuPawe
511:         nayrup/fs ©Av. nig2rdpta ©med, pass. st.                       excellence
512:           *»zyrwPs-                                                    BSTBL, Dhy. 109, 180; TSP 14, 28; GMS 1082
516:    5919 nyrys- S(C)                              o*J> o~jjs"           niyoSan   (nywdn) ©Khwar. nYwdnyk  ©pi. -(
522:    5921 nys'yrGi) B                                                      BSTii 843.25, 903.6; C2, 56R26, 68R25; pi.
525:           =»nysyr, nxsyr                                                 57R6; nYwSn\ GMS 974, nYwdnw, MDii p205
532:    5922 nys'yr sk'rk B
758:                           nimezisn                                 npyritw6*r-, MDii p205; AVS 125
926:         light ?, third Messenger ?)                                  nPStSyr- =»nsyd-
1102:       BBB p82, 679 b9; GMS 676; STii 8.7, zwyrty; Hen.
1126:6127 nw yrp>k B
1127:     nu-yarPe/ak (nw yrp'y, nw yrPk)                               6142 nwr B, S, C            (u>>>^    jj)JU<o^i
1131:6128 nw yrp*y =» nw yrP»k                                               now
```


## [2026-09-07T19:34:16.284Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^ *6[0-9]\\{3\\} nyp\\|nyp8\\|nypd-\\|nipe8\\|nipa8\" SOD_pages.txt | head -20",
 "description": "Sogdian nypδ- entries"
}
```


### [2026-09-07T19:34:16.794Z] TOOL RESULT

```
20981:                                                                    inf. np*sty =»nyp8-, npst'ny, np>y8-
20986:                                                                  nipastane =>nyp8-, np*st-, npst'ny
21016:        pcrf. st. ^np^s-, npxst-, np'xst-Cy)                        Pahl. nibdy-, nibdstan =*nyp8-, np»st-
21786:6283 nyp5- B                            jjl>j7 ^ojl^jI^              third month of the ycar(Nisan)
21797:6284 nypys- C, S                                      -i^
```


## [2026-09-07T19:34:24.966Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '21786,21800p' SOD_pages.txt; echo \"#### 5918 ctx\"; sed -n '20706,20720p' SOD_pages.txt",
 "description": "Print Gharib entries 6283 and 5918"
}
```


### [2026-09-07T19:34:25.031Z] TOOL RESULT

```
6283 nyp5- B                            jjl>j7 ^ojl^jI^              third month of the ycar(Nisan)
     nipe/a5 ©<Av. ni pai6ya-\ Khot. nuvad\                          BSTii 843.43: C2, 68V 11
       Khwar. ^bzy-, Pahl. nibastan-, Yaghn. nipid
                                                               6297 nysn'nc S                               JU^aUoW
       ^'np'stk, np}y6-                                             nisana/cnc/c (nysnync)
     (to)\ie down
                                                                     third month of the ytar(Nisan)
      GMS 544; VJ 1138; TSP 13.8, 2.535; BSTBL, Dhy.
        351; SCE 324; Bailey. Prolexis. 141; AVS 114                 Hen.
                                                                       Nov.JRAS
                                                                             6, 2 1945, 149.4; MDiii; nysnync, MDii
6284 nypys- C, S                                      -i^
     nipes ©impf. ^np*ys-                                      6298 nysnync M, S =* nysn'nc
     (/<?)write                                                6299 nyst                                (u>> ^*     j>)c~~j
      STi 30.1: MDii; Anc. Lett.; CII 1990 C3                        nest (nystt, nyyst) ©<*ne-asti ^sty1, nst
#### 5918 ctx
    5915 nyrf C = n +yrf -> n-, yrf                                     excellent, kind, fine
    5916 nyrn* rwc -» nyr'n rwc                                         BSTBL, Dhy. 153, 363; GMS 445
    5917 nyrs- -* ^yrs-                                            5928 nywp'w'k B                                ><^>^
    5918 nyrwps- S                  0-^»->^j> <ooiojjii                 nayuPawe
         nayrup/fs ©Av. nig2rdpta ©med, pass. st.                       excellence
           *»zyrwPs-                                                    BSTBL, Dhy. 109, 180; TSP 14, 28; GMS 1082
         0o)be pressed down
         Mack. AI 424.6 n p427                                     5929 nywdn C =* nyw6n(),/(h)
                                                                   5930 nyw6n(>)/(h) B, M, S              jTU^^U
    5919 nyrys- S(C)                              o*J> o~jjs"           niyoSan   (nywdn) ©Khwar. nYwdnyk  ©pi. -(
         nixres ~»nxrys-                                                  =>ny>w5n(h)
         GcOreproach
         Schwartz. STSC pi 44, 134.33                                   dress, garment
                                                                        TSP 7, 21, 1327, 21i 9; BBB; Tales. 478, 480;
    5920 nys'kt    M =* ny>ws>kt                                          BSOAS 12, 307.15; GMS 676, 1030; STi 16.9;
```


## [2026-09-07T19:34:31.304Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for p in 233 238; do echo \"########## HRN printed p.$p (leaf $((p+21)))\"; awk -v n=$((p+21)) 'BEGIN{RS=\"\\f\"} NR==n+1' HRN.txt; done",
 "description": "Print Horn pages 233 and 238"
}
```


### [2026-09-07T19:34:32.564Z] TOOL RESULT

```
########## HRN printed p.233 (leaf 254)
— 233 —
kurd. LW. tiem; afy. lünd 'feucht'; bei. wami *Tau,
Neber (252).
1040. nemäfi 'Gebet', TNOi: (Is. 1, 14).
aw. vergl. nemah- 'Gebet; ai. /ia/zias- ; phl v. nawäc
(päz. namaS).
LW. kurd. nimlz, nirm *Gebet'; afy. nmünj ; bei.
namäs, nawäs (251).
Da alle neuiranischen Formen auf die mittel-
persische charakteristische Neubildung natnäc zu-
rückgehen, so halte ich dieselben sämmtlich für
Lehnwörter.
Fr. Müller, (WZKM. 5, 67) nimmt als Grundform
ap. *namascij/ an; aber ap. sc konnte im Neuper-
sischen doch nicht zu ^ werden. Diesen Lautüber-
gang durch np. d^^, niz zu stützen, ist verfehlt.
1041. nemed grober Teppich, Filz', ar. LW. namat.
aw. netnata^j nimata- *Stroh, Gras'; phlv. nanmt
V
'Stroh, Gras*^); grober Teppich' (Säy. näääy. II, 101).
1042. numüdmi 'zeigen; erscheinen', Praes. numäy-em,
numüdar, numün^), Dt^'^NDi: (Qiss. Dan.).
ni + i^fnä-; phlv. n(i)mütan 'zeigen, erscheinen',
n(i)mayisn, n(i)mütär,
oss. d. niniäyun, t. njmam 'rechnen, zählen' (176);
sar. si/n. namäy-em 'sich zeigen, erscheinen*.
1048. numed 'hoffnungslos'.
phlv. anömet 'hoffnungslos'; vergl. ötwed, umed
(No. 109).
Der Bedeutung nach eine Doublette zu na-umed.
Die PehlevT-Schreibung D^DIWN, das doch gewiss
nicht anaumet gelesen werden kann, ergiebt wohl
auch für die Suffixendung I^DW die Lesung -ömajid,
^) Vd. 3 (121 J ist besser *auf lauter spitzige Gräser* als *auf'
lauter stachelichte Teppiche' (Geiger, ZDMG. 34, 425).
^) In den Dialekten ist die Praesensbildung auf -ün die alleinige,
vergl. Käs. V. bdnumön (Im^pt.)^ '/..bänemön^ K, ronmötr, ähnlich finden
sich im kauk.-bergjäd. vom Inf. f ermüde der Impt. ferrnün und das
Praes. mi-fermünum gebildet.
########## HRN printed p.238 (leaf 259)
— 288 —
1062. niyä 'Grossvater, Ahne (Plur. myagän),
ap. aw. nyäka- *Grossvater , vergl. ap. apangäka'
Ahne'; phlv. nyok.
af;'. nlka *6rossvater, LW. niya 'Grossmutter*;
bei. näkü, n. nüxö 'Oheim* (258), fwl^ *Grossnuitter'
(250).
1063. niymn 'Scheide*.
ap. *nigama', vergl. skr. w^ + l^f/am-, mgamd-
'Einfügung (aber nur als ritueller t. t.), vorgl. np.
peyam (de Lagarde, Ges. Abb. 79).
Unsicher ^).
1064. nirö {*n^rö) 'Kraft, Macht'.
aw, '^nairyava- 'Mannhaftigkeit', vergl. nrnrya-
mannhaft'; ai. ndrya-; phlv. nerök,
1065. ni» auch', hemz (Sahn. I, 167 Vers 691), ?:x (Is.
1, 15).
ap. *anyadadi^) 'irgend wie anders' (Säle mann,
Mel. asiat. IX, 241); phlv. mc (AV.?), päz. nfz.
Das Wort heisst aber nlz (nicht uez), es reimt
auf äz; ebenso hemz, das die Wörterbücher fälsch-
lich mit B sprechen lassen.
1066. ne»t *ist nicht*, vest^^),
päz. nestj nesU,
ap. naiy + asti,
1067. neS 'Spitze, Stachel; Gift (AM. S. 10 Zeile 5 v. u.)',
nester 'Lanzette'.
ai. vergl. neksana- spitzer Stab, Spiess', zu [/'neks-,
niksati 'durchbohren' (Hörn).
1068. nek 'schön, gut', nekö, nekt, new 'wacker, Held'
(Sahn, I, 416 Vers 555, HI, 1106 Vers 707, von einer
Frau).
*) Wenn phlv. n{i)käm^ vd. 7 f 192) Gl , wirklich 'matrice' bedeutet
— was ich bezweifle - so müsstc es nCOgüm gelesen werden, um mit
np. niyäm vereinigt werden zu können (Darm est eter, Et. ir. I, 61,
Note 4).
*) Lies *amyadäciih
«J Reimt auf yekesi (Öähn. I, 42 Vers 144; 170 Vors 750). Auch
in Indien spricht man heute nlst.
```


## [2026-09-07T19:34:46.786Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for w in \"nezend\" \"nizend\" \"nazend\" \"niSestan\" \"nisestan\" \"nesib\" \"nasib\" \"nivistan\" \"nevistan\" \"niwistan\" \"neberd\" \"nebard\" \"nawardTden\" \"navardiden\" \"nihaden\" \"niheden\" \"niyoSTden\" \"niyusTden\" \"nigah\" \"niyaz\" \"nigün\" \"nigun\"; do echo \"### $w\"; grep -n -- \"$w\" HRN.txt | head -4; done",
 "description": "Horn greps for Persian words"
}
```


### [2026-09-07T19:34:48.304Z] TOOL RESULT

```
### nezend
8939:1031. uiS&iidy nezend niedergeschlagen (trop.); elend,
13118:nezend 1031.
### nizend
334:gnMd (21, 17), hift auf jnft (32, 175), nizend auf erjum^nd
### nazend
### niSestan
### nisestan
### nesib
### nasib
### nivistan
### nevistan
### niwistan
### neberd
8899:1025. neberd "Kampf, newerd, neberde 'tapfer (Sahn. I, 93
### nebard
### nawardTden
### navardiden
### nihaden
### niheden
### niyoSTden
### niyusTden
### nigah
### niyaz
### nigün
6071:690. (2)-ÄÄr 'Kopf in nigün]sar^ sebuk]sar etc.
### nigun
5825:Die Vereinigung mit arm. gari (H. No. 65), lat.
```


## [2026-09-07T19:34:51.542Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '8930,8960p' HRN.txt; echo \"#### 1025\"; sed -n '8895,8915p' HRN.txt",
 "description": "Horn nezend and neberd entries"
}
```


### [2026-09-07T19:34:51.598Z] TOOL RESULT

```
nazlk, n. nazl/, nazi (256) ; sar. nizd.
*) Reimt auf niskerid, Öähn. I, 166 Vers 675.
2) Rücke rt hatte ZDMG. 8, 286 an ai. pidr (d. i. *pizd') ^drücken,
pressen' gedacht.
^) Die BelegstcUe vordanke ich Herrn Prof. Nöldeke.MI
— 231 -
WSO, niiad 'Geschlecht, Abstammung, Adel' *), nizade 'von
adeliger Abstammung 2).
aw. ^nizäti", vergl. skr. Jati-.
1031. uiS&iidy nezend niedergeschlagen (trop.); elend,
niedrig*.
ap. *ni -h l/yaw- niederschlagen*, also etwa ein ap.
*/ii/a«/M- 'niederschlagbar voraussetzend, vergl. indische
Bildungen auf -tti- bei B. Lind n er, Altindische Nomi-
nalbildung, 8 54, Ib (S. 80).
Unsicher.
1032. niSästen 'sich setzen lassen', Praos. uisän-em,
nisänden.
Causativ zu nisesten (No. 1083); phlv. n(i)sastan (vd.
16 (17) ÖL), n(i)sanet (M6n.).
1033. nisesten 'sitzen*, Praes. nisln-em,
g. senastmün 'sich setzen'.
ap. m + [/^had-, Caus. niyasädayam; aw. ni -\-
l^had-, mshiSaiti 'sitzen, sich setzen', Caus. niSädayöis;
phlv. n(i)sastan, n(i)$fnet (vd. 16 (1)) ; ai. ni + [/^sad-,
stdati,
kurd. LW. nisin 'sich setzen'; bei. nindag^ n. nin-
day^ Causat. nistainay (264).
Der Nasal der Wurzelsilbe in np. nism-em ist auf-
fallig (er findet sich auch in bei. nindag, ksl. sedq
(sösti), apr. midMs, ist also wohl alt), ebenso das
#### 1025
seine Lesung der betr. Gemme sprechen die voUständig deutlichen
Buchstaben auf dem Steine.
«j Vergl. Bartholomae, BB. XVII, 132.230 —
V
1025. neberd "Kampf, newerd, neberde 'tapfer (Sahn. I, 93
Vers 586).
aw. *ni -r l/^parU^ peretente sie kämpfen'; phlv.
n{i)part "Kampf (AV.).
Vergl. np. äwerd "Kampf (Sahn. I, 218 Vers 1506),
äwerdgäh (häufig), äweriden,
1025*»*« nebld, nebtd 'Fruchtsaft, Wein »).
ap. ^nipita- 'Trank', vergl. ai. pltd- etc. (Nöldeke,
mündliche Mitteilung) 2).
nehire "Enkel' siehe unter newade (No. 1047).
1026. ner, nerr (AM.) "Mann; männlich', nere [nerre), nenne
"männlich*.
aw. naV' "Mann ; phlv. war; ai. när-,
kurd. ner 'männlich'; afy. nar\ oss. d. nale, t. nal
'Männchen von Tieren' (197) ; bei. nar 'männlich'
(258); sangl. narak.
1027. nirx, nerx "Preis, Wert' (z. B. Schefer, Chresto-
```


## [2026-09-07T19:35:03.956Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^10[0-9][0-9]\\.\\|^ *10[0-9][0-9]\\.\\|^ *9[0-9][0-9]\\.\" HRN.txt | sed -n '1,200p' | grep -n \"10[0-9][0-9]\" | tail -70",
 "description": "List Horn entry headers"
}
```


### [2026-09-07T19:35:04.009Z] TOOL RESULT

```
124:8920:1028. nerm "weich, sanft', nerml,
125:8926:1029. ne^^d "nahe', nezdik^ nezdiki,
126:8939:1031. uiS&iidy nezend niedergeschlagen (trop.); elend,
127:8946:1032. niSästen 'sich setzen lassen', Praos. uisän-em,
128:8950:1033. nisesten 'sitzen*, Praes. nisln-em,
129:8965:1034. niseb Unteres; unten'.
130:8977:1035. neft ^Naphta .
131:8985:1036. fUgasten malen', Praes. nigär-em, nigarld^n^ nigär
132:8990:1037. nigäh 'Anblick, Aufmerksamkeit*.
133:8996:1038. nigertden 'betrachten', nigeristen.
134:9003:1039. nem 'feucht; Feuchtigkeit'.
135:9010:1040. nemäfi 'Gebet', TNOi: (Is. 1, 14).
136:9023:1041. nemed grober Teppich, Filz', ar. LW. namat.
137:9027:1042. numüdmi 'zeigen; erscheinen', Praes. numäy-em,
138:9033:1048. numed 'hoffnungslos'.
139:9050:1044. iiene *Mutter', nicht schriftgemäss, aber dialektisch
140:9058:1045. wf>, nev (Sahn. I, 130 Vers 19) neu*.
141:9065:1046. neva^terij tiuvä/ten *singen; schmeicheln', Praes.
142:9069:1047. newäde ^Enkel*, newäse, newa (vergl. newäzade),
143:9079:1048. nuväzdeh 'neunzehn*.
144:9087:1049. ueved neunzig .
145:9090:1050. neverdtden (neverden) *drehen, winden, wandern',
146:9098:1051. niwiSteu^ miwisten, nibistm, ]n2/2^ (jüd.-pers.)
147:9120:1052. nÜH jetzt, nun', vergl. ekniln, kunün.
148:9125:1053. uuved *frolie Botschaft.
149:9131:1054. nöylden 'klagen (Sahn. I, 183 Vers 986, Calc),
150:9135:1055. ne (geschrieben neh) nicht'.
151:9138:1056. nu (geschrieben nah) neun'.
152:9145:1057. nihäden ^hinlegen, hinsetzen', Praes. w/Ä-e/w, aber
153:9149:1058. nihän Verborgen, heimlich*.
154:9154:1059. nihuften , nuhuften Verbergen', Praes. nihuft-em,
155:9169:1060. nei 'Schilf, «af *Flöte\ näl; vergl. A-e/Te|wfl7, stlrjndT
156:9187:1061. ne 'nicht' (Öähn. I, 198 Anm. 2, Calc), vergl. nPsi
157:9193:1062. niyä 'Grossvater, Ahne (Plur. myagän),
158:9199:1063. niymn 'Scheide*.
159:9204:1064. nirö {*n^rö) 'Kraft, Macht'.
160:9207:1065. ni» auch', hemz (Sahn. I, 167 Vers 691), ?:x (Is.
161:9214:1066. ne»t *ist nicht*, vest^^),
162:9217:1067. neS 'Spitze, Stachel; Gift (AM. S. 10 Zeile 5 v. u.)',
163:9221:1068. nek 'schön, gut', nekö, nekt, new 'wacker, Held'
164:9233:1069. nem 'Hälfte, halb*.
165:9243:1070. niyöütden 'hören, horchen'; 2/'^v: (Is. 21, 7).
166:9273:1071. if, ü (§ähn. I, 25 Vers 37) und*.
167:9285:1072. väj 'sprich', vergl. vat 'Wort, Rede' (dialektisch^),
168:9298:1073. "WäTj -wäre, tver (ür)^), Suffix 'tragend, versehen
169:9312:1074. wäriin unglücklich, elend, schlecht*, tcärilne^).
170:9317:1075. valäne, velane (so im Gazophylacium S. 389)
171:9321:1076. veyiMür^ vu/sür 'Prophet' ).
172:9325:1077. vefif 'Grösse, Würde'.
173:9348:1078. vevd/kj 'Wachtel', rerdej, verflj, vertek.
174:9354:1079. verseng 'würdig, achtbar (unbelegt).
175:9361:1080. very 'Wasserwehr, hery.
176:9364:1081. vemste, beziste nur in nnon, nnDTZ (Is. 66, 8;
177:9367:1082. vei^ey Frosch', arab. LW. vazayat 'Eidechsenart'.
178:9371:1083. i^ezlden 'wichen'; bezän (Sahn. I, 284 Anm. 2).
179:9375:1084. ve^lr (arab. LW.) 'Vezir; Gelehrter ^), gezJr, gizlr*^),
180:9389:1085. veng, ving 'leer; arm'.
181:9403:1086. vir Sinn, Verstand; Gedächtniss'-), hir, her (8,
182:9411:1087. werän, werane wüst', heran.
183:9422:1088. hämün *Ebene'.
184:9425:1089. fiaven 'Mörser', (AM. 132 Zeile 6), kaukas.-bergjüd.
185:9432:1091. hurrä ^Geschrei' (äähn. I, 17 Vers 66).
187:14197:1073.
190:16405:1010.
192:16537:1053.
194:18979:1017.
195:18981:1040.
196:18983:1070.
197:22632:1078.
198:22746:1091.
```


## [2026-09-07T19:35:08.142Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '8965,8976p;8990,9002p;9090,9120p;9145,9155p;9243,9273p' HRN.txt",
 "description": "Horn entries niseb, nigah, neverdiden, niwisten, nihaden, niyousiden"
}
```


### [2026-09-07T19:35:08.198Z] TOOL RESULT

```
1034. niseb Unteres; unten'.
aw. *mxsvaepa-, vergl. x^^^W^' (No. 799) ; phlv.
n(i)Sep (AV.), n(i)sepitan^ n(i)sepmd 'sie gehen unter*
(Salemaifn, Mel. asiat. IX, 238), vergl. v(i)seft, 'Ver-
lorenes Sprachgut*, No. 229.
>) VergL Rückert, ZDMa. 10, 138.
2J Vergl. besonders äähn. II, 765 Vers 11 ; auch II, 611 Vers 1601.— 232 -
1034*>*» niseni *Nest* (Sahn. I, 137 Vers 146), nisemen i).
Doch wohl auch zu np. nisesten (No. 1033), wenn-
schon die Erklärung der Formen schwierig ist. Ge-
hört dazu etwa auch äsyäne *Nest' (No. 35)?
skr. LW. niglmana" (PärasTpr. ed. Weber, No. 433).
1037. nigäh 'Anblick, Aufmerksamkeit*.
aw. *nikasa- (vergl. ägäh, No. 40); phlv. n(i)käs.
LW. kurd. nekä; bei. nikäh (263).
Kä§. V. hat sogar als Verbum [/^kos- *sehen' noch
erhalten, nämlich in Praes. bitkesün, Impt. bikes, Inf.
bikasdn u. s. w. (s. v. nigäh kerden).
1038. nigertden 'betrachten', nigeristen.
Käs. Q. vergl. angastän^ batangastdn (s. v. nigc^
kerden),
Wohl zu derselben Wurzel wie aw. hankäray§mi,
siehe np. engärden (No. 123); phlv. n(i)karitan,
n(i)kar(i)sn,
kurd. nirin, nihirin 'betrachten.
1050. neverdtden (neverden) *drehen, winden, wandern',
ueoesten (AM. 2 Zeile 7), neverd.
ai. w/ f- Ki^ar^- zurückkehren, fortgehen, den
Kücken kehren etc.*.
Wenn die Etymologie richtig ist, so wäre die ur-
sprüngliche Form *mverdlden bezw. *nivesten,
nöx siehe hemz (No. 1108).
nöS, nöse 'lieblich' siehe enöse (No. 128).
1051. niwiSteu^ miwisten, nibistm, ]n2/2^ (jüd.-pers.)
schreiben, Praes. miw^s-em; nulje, nuwB^) *Wort
Gottes, Qorän*.
Käs. Z. vinemes,
ap. ni + [/^pais-, nipistanaiy 'schreiben* 2) — ai.
|X/>e^-, pincdti bedeutet nur 'schmücken'^); phlv.
n(i)p(i)stav, n(i)p(i)stak, n(i)p^k 'Schrift*; ksl. pisatL
kurd. LW. nivlsin schreiben; oss. d. finssun , t.
fissin, nifista 'Schrift' (287); bei. LW. nibTsay , pp.
nibista (261) ; wa/. si/n. sar. LW. neoisam.
Die Wörterbücher haben noch einige teils auf
falscher Punktation teils auf Analogiebildung be-
ruhende np. Formen wie nuwes (wertlos), miwesten.
Die Wurzel ist peikf, vergl. gr. tioiy.CKo^,
V) Salemaun, Noch einmal die seldsohukischen Verse, M61.
asiat. X, 217.
p{r|2?5 des Buches Ezra wird ebenfalls mit np. niivisten in Ver-
bindung gebracht.
'J In der Form vanlaaovjin bei Aristophanes, Acharner 100
(E. Kuhn, KZ. 31, 324).
*) Eine aw. \/^paes- kommt als Verbum nicht vor; yt. 13, 126
hat die Neuausgabc uapumitaic^m.- 236 —
1052. nÜH jetzt, nun', vergl. ekniln, kunün.
1057. nihäden ^hinlegen, hinsetzen', Praes. w/Ä-e/w, aber
neht (AM. 65 Zeile 10).
aw. ni + 1^2 da- {nidadät) 'hinsetzen'; phlv. n(i)hatan
(AV.); ai. m+ l^l dha- (nldadhäti),
1058. nihän Verborgen, heimlich*.
ap. ^nidäna- 'etwas (heimlich) hingelegtes*, vergl.
ind. ni -f- [/'dhä- 'niederlegen zur Aufbewahrung oder
um zu verbergen'; phlv. n(i)hän.
nehmär 'zahllos* siehe sumär (No. 791).
1059. nihuften , nuhuften Verbergen', Praes. nihuft-em,
niheirihiden ^), nnhumhtden ^).
1070. niyöütden 'hören, horchen'; 2/'^v: (Is. 21, 7).
aw. *n? — \/gaos-, vergl. apa gaosay^iti; phlv.
n(i)yösJtany n(i)yö/sltan bezw. n(i)gösltan'') 'hören'; ai.
[/"ghöS'^ ghösati mit d 'hören, horchen auf.
bei. mgösag, niyösay (262).
>) Vergl. Fr. Müller, WZKM. 5, 265.
Die jüngere phlv. Form tiek liest Justi fZDMG. 46, 288) zwoi
Mal auf Gemmen (die letztere derselben, JRAS. XIII No. 45, die ich
ZDMG. 44, 658 No. 48 N\a]kt/arnai lesen wollte, hat übrij^ens Levy,
ZDMG. 11, 320 als semitisch (!) entziffert, worauf mich Herr Cler-
mont-Ganneau aufmerksam macht).
*) de Lagarde^s CBeitr. zur altb. Lex. 76) von Darmesteter
f6t. ir. I, 85 Note 2) wiederholte Erklärung aus aw. yao^nti' ist ver-
fehlt ; phlv. ftffJyö/Sitan^ das auch gelegentlich n(i)ybHltan geschrieben
sein kann (aber wo?), beruht auf einer im Pchlevl häufigen graphischen
Eigentümlichkeit.
Ba wird schon im Pehlevl regulär zu « (z. B. aw. paHti'^ pusf;
l/kar8', kasiian u. s. w.), vergl. auch bereits aw. pä^no" gegen ai.
pärsni: Der Übergang von rs in /S ist dem gegenüber nur ein schein-
barer in äia^s aus ätars und Syäva^^ aus Si/ävarsati-; )^h soll hier bloss
eine scharfe oder wahrscheinlich etwas modificirte Aussprache des s
bezeichnen, wie sie in ^^ar^set (vergl. Hörn, Mitteiluiigen, Heft IV,
S. 34) berechtigt war. Diese Aussprache wurde dann weiter über-
tragen, z. B. phlv. Zartux^t (aw. Zara^usfra-), daraus Zerduhest etc. des
SähnSme, vielleicht kÜ^sUan (ältere Form nicht vorhanden), nCOyöxsitun
oder wohl nCi)yöxSUany vergl. nCOyo^s, wie nach MuqaddasI 418, 5 (Nöl-
d e k e ^ s Correktur nach mündlicher Mitteilung) die Bewohner Xüzistän^s
für *höre* sagten. Siehe auch Hörn, KZ. 82, 585 Xo. 18 und vorgl.
unter np. feyfere (No. 806).240 —
V, w.
1071. if, ü (§ähn. I, 25 Vers 37) und*.
```


## [2026-09-07T19:35:29.431Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"niyaz\\|niaz\\|nyaz\" HRN.txt HUB.txt | head -10; echo \"###### PHD\"; for w in \"^nih\" \"^nis\" \"^nib\" \"^nim\" \"^niy\" \"^nig\" \"^naw\" \"^nab\" \"^niz\" \"^nixw\" \"^nise\"; do echo \"## $w\"; grep -n -- \"$w\" PHD.txt | head -12; done",
 "description": "Horn niyaz and MacKenzie ni- entries"
}
```


### [2026-09-07T19:35:30.732Z] TOOL RESULT

```
HUB.txt:6330:apeniaz 'bediirfnisslos' = np. be-niyaz; apsparem *ich iiber-
HRN.txt:2170:g. niaz. varak; gel. velg, valk; Käö. valg^ velg\ (vergl.
HRN.txt:2525:be (ZPGl.), vergl. arm. LW. ape]niaz,
###### PHD
## ^nih
513:nihuftan 60 nizar
514:nihuftan, nihumb- [zhwptn', nhwmb- | = M, N <) cover, hide, conceal, clothe, nihumbidan [nhwmbytn'] = nihuftan. *nikóhidan, nikóh- [nkwh-ytn' | N ~] blame, execrate. ~išn: blame. ~išnīg : blameworthy, execrable. nil [nyl | N ~] indigo. nilópal [nylw(k)pl | N ~, nilēfar] lotus, water-lily. nimüdan, nimāy- [nmwtn', nmd- | M nmwdn, nm’y-, N ~] show, guide. nirfs- [nlps-] wane, decrease. ~išn: decrease, diminution. nirmad [nylmt'] profit, interest. ~ӧтапа [-’wmnd] profitable. P nisag [nys’k' | P nys’g] bright, splendid. niš- [nyi- | M nyyš-ydn, J ~] see, observe. nišān-, v. nišāstan. nīšān [ny$*x! | = M, N nisàn] sign, mark, banner. nišast [nsst! | N ~] association. nišastan, nišīn- [Y TY BWN-stn! < A V у; пт! | M nist, (nfyy-), N ~] sit. nišāstan, nišān- [Y TY BWN.stn!, 2n-; nP?stn!, nP?n- | M nf?st, (nP5y-), N ~] set, seat, plant, found. nišāyišn [n£ din! | M n$?y-, v. niSástan] foundation. nišēb [niyp | N ~] declivity; astr. dejection. ~ig [-yk'] declining. nišēm (nidm | M nšym, N ~an] seat, perch. ~ag [-k'] residence, abode. niSin-, v. niSastan. niwāģ [nw k! | M ng, N nawa] music, song, melody. *niwé [nwyk! | (N nuwéd)] good news. *niwéy-, -išn, v. niwistan, *niwéyénidan [nwykyn-ytn'] = niwistan. niwistan, *niwéy- [nwstn', nwyd- | nwyk-] announce, consecrate. —išn(ih): announcement. nixwār- [nswb’l- | M nyxw’r-] hasten. -išn: haste. niyübag [nyd’pk' | M ny’bg] becoming, fitting, suitable. ~th: suitability. niyāģ [nyd?k! | M nyg, N niya] grandfather, ancestor. niyāyišn [xyd?dšn! | N ~if] prayer, praise. niyāz [nyd?c | M ny’z, N ~] need, want, misery. —ómand [2wmnd | N ~mand] needy. ~6mandih: poverty. niyē(x)šidan, niyē(x)š- [n(y)duhš-ytn! | M nywi-, N niyófidan] hear. ~išn: hearing. І nizār [nz?l | (P nyz?*wr), N ~] weak, feeble.
5288:nihal, wahār, waxr
## ^nis
## ^nib
5156:nibāstan
5157:nibay-
5158:nibēg
5159:nibēm
## ^nim
2919:nimble čābuk, šēbāg.
## ^niy
129:niyāz, —omandih ... add necessity. read niyoxšīdan... по [TSA < A tě |... (not tē”).
5293:niyàzómand эго ү» VU niyāzūmandīh — ^45? 06 үу о y \ niyābagīh ^ $91 niyābag BOV wüxtan OV \ nihādag 14 vex» \ nay, này, *?way, way Del | уду. wb wāyendag 14» ГСУ \ wayendag 155 TO V git-!, kun-! DAT eh A kirih-t — UY I
5303:niyäyišn wihān, wiyān nāxun wihānag
5304:niyāg, wahāg
## ^nig
2916:niggardly pen.
2917:night Sab; last ~ dos.
2918:night raid $abixón.
5191:nigāhdārīh
5197:nigāhdārišnīh 49 KCI
5198:nigān
## ^naw
## ^nab
494:nab [np | N nawa] grandson. nabānazdišt [nb”nzdšt! = Av. nabünazdista-] next of kin. паї [w | M mp] family. ~ag [-R! | N náf(a)] navel. !naft [npt! | = M, N ~] moist, damp; naphtha. *naft [npt'] descendant. nahang [жле] province. *nakkira [nkyl’y] denying, repudiating. ~yih: repudiation. nāl- [wl- | P (n’r-), N ~] groan, complain. nam [nm | N ~] moisture. nám [SM < A £m; m | = M, N ~] name, fame. namad [nmt' | N <) felt. námag [MGLTA < A melt: ттк! | M пто, N пата] book, letter. namak [nmk! | M nmyhk, N ~] salt. namāz [OSGDE < A sgdh; nm’c | = M, N ~] reverence, prostration, prayer. ~ burdan: pay homage. nām-burdār [л?т bwlt?l | N ~] heir, preserving the father's name. nāmčišt [?жт-, ŠMcst'], (pad) ~: in particular, especially. ~ig [-yk'] famous, well known.
5154:nab
## ^niz
515:nizārīh 61 0$
## ^nixw
## ^nise
```


## [2026-09-07T19:35:39.016Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for w in \"nihādan\" \"nihād\" \"nibēsīdan\" \"nibēs\" \"nigāh\" \"nigūn\" \"nabard\" \"nižand\" \"nawardīdan\" \"nibardan\" \"nimāy\"; do echo \"## $w\"; grep -n -- \"$w\" PHD.txt | head -4; done",
 "description": "MacKenzie more lookups"
}
```


### [2026-09-07T19:35:40.408Z] TOOL RESULT

```
## nihādan
512:nest [LOY T! < А P?yty | M nyst, N ~] is not. ~ih : non-existence. néw [TB < A tb; nyw' | = M, N —] good, brave. ~-ardaxSir [nyw lthsyl | N nard !] backgammon. nézag [nyck! | N néza] lance. nēzūmān, —16 [nycwmn', -yk! | M nyzwm!n] dextrous, skilful. -~th: skill, artistry. nibard [nplt' | N nabard] fight, struggle, battle. ~ag [-k! | N ~a] tried, experienced. nibardīdan, nibard- [npit-ytn! | P nbrd'd] fight, do battle. nibastan, nibay- [SK BHWN-tn! < A У hb; npstn', npd- | M nbst] lie down, sleep. nibāstan, *nibày- [np'stn! | M nb’st, nb y-] lay down. nibég [npyk! | N niwé] writing, scripture, book. nibém [npdm | (P nbdm-)] lying, prostrate. nibištan, nibés- [VK TY BWN-stn! < A yktbwn, У КЬ; npstn' | M nbyšt, nbys-, N —] write. nidan, nay- [YD(B)LWN-tn! < A ydbrwn, V dbr | M nyydn, ny-] lead. nidom [nytwm] least, smallest. nifridag [nplytk' | N nifrid] accursed. nifrin [nplyn' | N <] curse. nigah [nk’s | M пол, N ~] look, attention. ~ dāštan: watch, keep. — kardan: look. ~-darih, —-dári&nih [-d?/(sn)yh | N —dārī] keeping, care. nigān [nk’n' | P ng’n] buried. nigar- [nk’l- | M ng’r-, N ~] draw, design, paint. ~ag [-h! | (M agin, N nigār)] image, picture, diagram. nigástar [nk?s I] guard; protective. nigeridan, niger- [nkyl-ytn! | N nigaridan] look, observe. --išn: observation. ~iSnig : evident, manifest. nigéxtan, nigéz- [nkyhtn!, nkyc-] expound. ~i$n: exposition. nigéz [nkyc] exposition. nigün [nkwn! | N ~] inverted, upside down. ~th: depth, downward direction. ~sar [-s?l | М ngwns’r] downwards. nihadag [nyd’tk' | M ny? dg] foundation. nihādan, nih- [TNH TWN-tn! < А hnht, ~ nht | M пуа, nyh-, N ~] put, place, establish. nihal [nbl | N ~] sapling, self-planted tree. nihān [nyh’n' | N ~] concealment, secrecy. ~ig [-yk! | N ~7] secret. nihang [nsng] small, few.
3300:put nihādan; ~ on pēšīdan, paymóx- tan.
## nihād
512:nest [LOY T! < А P?yty | M nyst, N ~] is not. ~ih : non-existence. néw [TB < A tb; nyw' | = M, N —] good, brave. ~-ardaxSir [nyw lthsyl | N nard !] backgammon. nézag [nyck! | N néza] lance. nēzūmān, —16 [nycwmn', -yk! | M nyzwm!n] dextrous, skilful. -~th: skill, artistry. nibard [nplt' | N nabard] fight, struggle, battle. ~ag [-k! | N ~a] tried, experienced. nibardīdan, nibard- [npit-ytn! | P nbrd'd] fight, do battle. nibastan, nibay- [SK BHWN-tn! < A У hb; npstn', npd- | M nbst] lie down, sleep. nibāstan, *nibày- [np'stn! | M nb’st, nb y-] lay down. nibég [npyk! | N niwé] writing, scripture, book. nibém [npdm | (P nbdm-)] lying, prostrate. nibištan, nibés- [VK TY BWN-stn! < A yktbwn, У КЬ; npstn' | M nbyšt, nbys-, N —] write. nidan, nay- [YD(B)LWN-tn! < A ydbrwn, V dbr | M nyydn, ny-] lead. nidom [nytwm] least, smallest. nifridag [nplytk' | N nifrid] accursed. nifrin [nplyn' | N <] curse. nigah [nk’s | M пол, N ~] look, attention. ~ dāštan: watch, keep. — kardan: look. ~-darih, —-dári&nih [-d?/(sn)yh | N —dārī] keeping, care. nigān [nk’n' | P ng’n] buried. nigar- [nk’l- | M ng’r-, N ~] draw, design, paint. ~ag [-h! | (M agin, N nigār)] image, picture, diagram. nigástar [nk?s I] guard; protective. nigeridan, niger- [nkyl-ytn! | N nigaridan] look, observe. --išn: observation. ~iSnig : evident, manifest. nigéxtan, nigéz- [nkyhtn!, nkyc-] expound. ~i$n: exposition. nigéz [nkyc] exposition. nigün [nkwn! | N ~] inverted, upside down. ~th: depth, downward direction. ~sar [-s?l | М ngwns’r] downwards. nihadag [nyd’tk' | M ny? dg] foundation. nihādan, nih- [TNH TWN-tn! < А hnht, ~ nht | M пуа, nyh-, N ~] put, place, establish. nihal [nbl | N ~] sapling, self-planted tree. nihān [nyh’n' | N ~] concealment, secrecy. ~ig [-yk! | N ~7] secret. nihang [nsng] small, few.
3300:put nihādan; ~ on pēšīdan, paymóx- tan.
5293:niyàzómand эго ү» VU niyāzūmandīh — ^45? 06 үу о y \ niyābagīh ^ $91 niyābag BOV wüxtan OV \ nihādag 14 vex» \ nay, này, *?way, way Del | уду. wb wāyendag 14» ГСУ \ wayendag 155 TO V git-!, kun-! DAT eh A kirih-t — UY I
## nibēsīdan
## nibēs
## nigāh
1159:care (n.) nigāhdār(išn)ih, pahrēz; témár.
2517:keeping nigāhdār(išn)īh.
2661:look (v.) nigeridan, nigāh kardan.
4273:watch (v.) nigāh dāštan, pādan, pās dāštan.
## nigūn
1687:downwards nigūnsār.
## nabard
512:nest [LOY T! < А P?yty | M nyst, N ~] is not. ~ih : non-existence. néw [TB < A tb; nyw' | = M, N —] good, brave. ~-ardaxSir [nyw lthsyl | N nard !] backgammon. nézag [nyck! | N néza] lance. nēzūmān, —16 [nycwmn', -yk! | M nyzwm!n] dextrous, skilful. -~th: skill, artistry. nibard [nplt' | N nabard] fight, struggle, battle. ~ag [-k! | N ~a] tried, experienced. nibardīdan, nibard- [npit-ytn! | P nbrd'd] fight, do battle. nibastan, nibay- [SK BHWN-tn! < A У hb; npstn', npd- | M nbst] lie down, sleep. nibāstan, *nibày- [np'stn! | M nb’st, nb y-] lay down. nibég [npyk! | N niwé] writing, scripture, book. nibém [npdm | (P nbdm-)] lying, prostrate. nibištan, nibés- [VK TY BWN-stn! < A yktbwn, У КЬ; npstn' | M nbyšt, nbys-, N —] write. nidan, nay- [YD(B)LWN-tn! < A ydbrwn, V dbr | M nyydn, ny-] lead. nidom [nytwm] least, smallest. nifridag [nplytk' | N nifrid] accursed. nifrin [nplyn' | N <] curse. nigah [nk’s | M пол, N ~] look, attention. ~ dāštan: watch, keep. — kardan: look. ~-darih, —-dári&nih [-d?/(sn)yh | N —dārī] keeping, care. nigān [nk’n' | P ng’n] buried. nigar- [nk’l- | M ng’r-, N ~] draw, design, paint. ~ag [-h! | (M agin, N nigār)] image, picture, diagram. nigástar [nk?s I] guard; protective. nigeridan, niger- [nkyl-ytn! | N nigaridan] look, observe. --išn: observation. ~iSnig : evident, manifest. nigéxtan, nigéz- [nkyhtn!, nkyc-] expound. ~i$n: exposition. nigéz [nkyc] exposition. nigün [nkwn! | N ~] inverted, upside down. ~th: depth, downward direction. ~sar [-s?l | М ngwns’r] downwards. nihadag [nyd’tk' | M ny? dg] foundation. nihādan, nih- [TNH TWN-tn! < А hnht, ~ nht | M пуа, nyh-, N ~] put, place, establish. nihal [nbl | N ~] sapling, self-planted tree. nihān [nyh’n' | N ~] concealment, secrecy. ~ig [-yk! | N ~7] secret. nihang [nsng] small, few.
## nižand
## nawardīdan
## nibardan
## nimāy
514:nihuftan, nihumb- [zhwptn', nhwmb- | = M, N <) cover, hide, conceal, clothe, nihumbidan [nhwmbytn'] = nihuftan. *nikóhidan, nikóh- [nkwh-ytn' | N ~] blame, execrate. ~išn: blame. ~išnīg : blameworthy, execrable. nil [nyl | N ~] indigo. nilópal [nylw(k)pl | N ~, nilēfar] lotus, water-lily. nimüdan, nimāy- [nmwtn', nmd- | M nmwdn, nm’y-, N ~] show, guide. nirfs- [nlps-] wane, decrease. ~išn: decrease, diminution. nirmad [nylmt'] profit, interest. ~ӧтапа [-’wmnd] profitable. P nisag [nys’k' | P nys’g] bright, splendid. niš- [nyi- | M nyyš-ydn, J ~] see, observe. nišān-, v. nišāstan. nīšān [ny$*x! | = M, N nisàn] sign, mark, banner. nišast [nsst! | N ~] association. nišastan, nišīn- [Y TY BWN-stn! < A V у; пт! | M nist, (nfyy-), N ~] sit. nišāstan, nišān- [Y TY BWN.stn!, 2n-; nP?stn!, nP?n- | M nf?st, (nP5y-), N ~] set, seat, plant, found. nišāyišn [n£ din! | M n$?y-, v. niSástan] foundation. nišēb [niyp | N ~] declivity; astr. dejection. ~ig [-yk'] declining. nišēm (nidm | M nšym, N ~an] seat, perch. ~ag [-k'] residence, abode. niSin-, v. niSastan. niwāģ [nw k! | M ng, N nawa] music, song, melody. *niwé [nwyk! | (N nuwéd)] good news. *niwéy-, -išn, v. niwistan, *niwéyénidan [nwykyn-ytn'] = niwistan. niwistan, *niwéy- [nwstn', nwyd- | nwyk-] announce, consecrate. —išn(ih): announcement. nixwār- [nswb’l- | M nyxw’r-] hasten. -išn: haste. niyübag [nyd’pk' | M ny’bg] becoming, fitting, suitable. ~th: suitability. niyāģ [nyd?k! | M nyg, N niya] grandfather, ancestor. niyāyišn [xyd?dšn! | N ~if] prayer, praise. niyāz [nyd?c | M ny’z, N ~] need, want, misery. —ómand [2wmnd | N ~mand] needy. ~6mandih: poverty. niyē(x)šidan, niyē(x)š- [n(y)duhš-ytn! | M nywi-, N niyófidan] hear. ~išn: hearing. І nizār [nz?l | (P nyz?*wr), N ~] weak, feeble.
555:rabih [/pyh | M rbyh] noon, midday (heat). rad [/t! | N —] (spiritual) chief, master. АҺ: office of rad. rad [Pu | P rd, N ~] generous, liberal. ~ih: generosity, liberality. radag [itk! | M rdg, N rada] line, rank, row. radómand [/t?^wmnd] having a rad. rad-passag [/tps’k'] ceremonies of the gáhanbar festivals. radunay [/twny = Av. ratunaya-] one under the guidance of a rad. raftan, raw- [SGY TWN-tn! < А V sg’; lwb- | M rptn, rw-, N ~] go, move, proceed. ~išn, v. rawišn. raftār [/pt?] | N ~] goer. rag А! | M rg, N ~] vein. «ЛЬ: disposition, character. ray [/gy | P rg] quick, swift. ray [Pg | N —] meadow, plain. rah [/s, lh, [hy | M rh(y)] chariot, wagon. rah-, у. rastan. rah [Ps | M rh, N ~] road, way. rahag [/hk! | P rhg] = rag. rāh-dār [lsd] | N ~] brigand, highway robber. ~ih: brigandage. rahig [/syk!, Ikyk' | M rhyg, N rahi] child, page. ~ih: childhood. rāh-nimāy [Psnm?d | (M r’-hnmwd’r), № ~numa] guide. ram [Pm | М әт, N ~] peace; cal. 21st day. ram(ag) [/m(k') | P rm, N ram(a)] herd, flock. ráménidan, rāmēn- [Pmyn-ytn! | M ?myn-] give peace, pleasure. rāmišn [P min! | M rmyfn, N rāmi$] peace, ease, pleasure. ~ig [-vk! | N —z#] peaceful, at ease. ran [Рп! | N ~] thigh. P rān- [/^n-] fight. randidan, rand- [/nd-ytn! | N —] scratch, grate, abrade. rang [/ng | M rng, N —] colour, dye. ranj [Inc | P rnj, (M rnz), N ~] toil, trouble. ~ag [-k' | N —a] troubled. ranjénidan, ranjén- [/ncyn-ytn'] trouble.
2175:guide (n.) parwānag, pēšār, rāhnimāy.
4970:rāhdār rähdārīh riycn- riyénag rayénidarih rāyēnīdan rāhnimāy rāyēnišn rahīgīh dort, rahīg dür!, rahīg
```


## [2026-09-07T19:36:02.356Z] TOOL CALL #47: Bash

```json
{
 "command": "sed -n '1,60p' tools/fetch_source.py",
 "description": "Inspect fetch_source.py"
}
```


### [2026-09-07T19:36:02.409Z] TOOL RESULT

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


## [2026-09-07T19:36:10.845Z] TOOL CALL #48: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/%D9%86%DB%8C%D8%A7%D8%B2\" \\\n \"https://en.wiktionary.org/wiki/%D9%86%DA%AF%D9%88%D9%86\" \\\n \"https://en.wiktionary.org/wiki/%D9%86%DA%98%D9%86%D8%AF\" \\\n \"https://en.wiktionary.org/wiki/%D9%86%D9%88%D8%B1%D8%AF%DB%8C%D8%AF%D9%86\" \\\n \"https://en.wiktionary.org/wiki/%D9%86%DB%8C%D8%A7%D9%85\" \\\n \"https://en.wiktionary.org/wiki/%D9%86%D8%A8%D8%B1%D8%AF\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 365 root Ni 1: Persian ni- compounds, verifying Nourai's Avestan/OP -> Persian arrows\"; done",
 "description": "Fetch Wiktionary Persian pages"
}
```


### [2026-09-07T19:36:16.534Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/0097c36e54f76601.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/fa4b881f788b94d0.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/1e1dde7ff515d65f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/9c5c4c5bb93a1ba1.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/6e5bcd50ac5dc00c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/2dda4fa85c460fcb.txt
```


## [2026-09-07T19:36:20.103Z] TOOL CALL #49: Bash

```json
{
 "command": "cd data/verification/sources/web && for f in 0097c36e54f76601 fa4b881f788b94d0 1e1dde7ff515d65f 9c5c4c5bb93a1ba1 6e5bcd50ac5dc00c 2dda4fa85c460fcb; do echo \"########## $f\"; grep -n -i -A18 \"Etymology\" $f.txt | head -60; done",
 "description": "Read Wiktionary etymologies"
}
```


### [2026-09-07T19:36:21.321Z] TOOL RESULT

```
########## 0097c36e54f76601
73: Etymology 
74-
75- 2.2 
76- Noun 
77-
78- 2.2.1 
79- Derived terms 
80-
81- 2.2.2 
82- Descendants 
83-
84- 2.3 
85- Further reading 
86-
87- 3 
88- Persian 
89-
90- Toggle Persian subsection 
91-
--
93: Etymology 
94-
95- 3.2 
96- Pronunciation 
97-
98- 3.3 
99- Noun 
100-
101- 3.3.1 
102- Synonyms 
103-
104- 3.3.2 
105- Derived terms 
106-
107- 3.3.3 
108- Descendants 
109-
110- Toggle the table of contents 
111-
--
196: Etymology
197- [ edit ] 
198-
199- Borrowed from Classical Persian نِیَاز ( niyāz , “ supplication, invocation ” ) .
200-
201- Noun
202- [ edit ] 
203-
204- نیاز • ( niyâz ) ( definite accusative نیازی ( niyâzı ) , plural نیازلر ( niyâzlar ) ) 
205-
206- invocation , supplication , entreaty , the act of calling for the assistance or presence of a superior being 
207- Synonym: دعا ( duʼâ ) 
208-
209- Derived terms
210- [ edit ] 
211-
212- نیاز ایتمك ( niyâz etmek , “ to use entreaty ” ) 
213- نیازكار ( niyâzkar , “ supplicant ” ) 
214- نیازمند ( niyâzmend , “ supplicant ” ) 
--
########## fa4b881f788b94d0
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Adjective 
69-
70- 1.3.1 
71- Derived terms 
72-
73- 1.4 
74- References 
75-
76- 1.5 
77- Further reading 
78-
79- Toggle the table of contents 
80-
--
144: Etymology
145- [ edit ] 
146-
147- From Middle Persian [Book Pahlavi needed] ( nkwn' /⁠nigūn⁠/ ) , which may be akin to Sanskrit न्यञ्च् ( nyañc , “ directed downwards ” ) . [ 1 ] Akin to Old Armenian նկուն ( nkun ) , an Iranian borrowing.
148-
149- Pronunciation
150- [ edit ] 
151-
152- ( Classical Persian ) IPA ( key ) : /ni.ˈɡuːn/ 
153-
154- ( Dari, formal ) IPA ( key ) : [nɪ.ɡuːn] 
155-
156- ( Dari, formal ) IPA ( key ) : [nɪ.ɡuːn] 
157- ( Kabuli ) IPA ( key ) : [nɪ.ɡuːn] 
158-
159- ( Hazaragi ) IPA ( key ) : [nu.ɡun] 
160-
161- ( Iran, formal ) IPA ( key ) : [ne.ɡuːn] 
162-
########## 1e1dde7ff515d65f
########## 9c5c4c5bb93a1ba1
########## 6e5bcd50ac5dc00c
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Noun 
69-
70- 1.3.1 
71- Derived terms 
72-
73- 1.3.2 
74- Descendants 
75-
76- 1.4 
77- References 
78-
79- Toggle the table of contents 
80-
--
148: Etymology
149- [ edit ] 
150-
151- Inherited from Middle Persian 𐫗𐫏𐫏𐫀𐫖 ( nyyʾm ) , 𐫗𐫏𐫀𐫖 ( nyʾm /⁠niyām⁠/ ) . Based on an Old Persian *nidāmān- ( “ covering, envelope ” ) .
152-
153- Cognate to Wakhi [script needed] ( naẟün , “ scabbard ” ) and Sanskrit निधानम् ( nidhānam , “ act of laying down, depositing, deposit; keeping; preserving; place where something is deposited or kept, receptacle ” ) .
154-
155- Also borrowed into Biblical Hebrew נָדָן ( nāḏā́n ) found in the Tanakh only in 1 Chronicles  21:27 and into Biblical Aramaic , Jewish Palestinian Aramaic , Jewish Literary Aramaic , נִידְנַה ( niḏnā ) , נִדְנַה ( niḏnā ) , נִדְנָא ( niḏnā ) , נְדָנָא ( nəḏānā ) , לדְנָא ( liḏnā ) , לְדָנָא ( ləḏānā ) , later contaminated Classical Syriac ܢܺܝܡܳܐ ( nīmā , “ sheath ” ) .
156-
157- Pronunciation
158- [ edit ] 
159-
160- ( Classical Persian ) IPA ( key ) : /ni.ˈjaːm/ 
161-
162- ( Dari, formal ) IPA ( key ) : [ni.jɑ́ːm] 
163-
164- ( Dari, formal ) IPA ( key ) : [ni.jɑ́ːm] 
165- ( Kabuli ) IPA ( key ) : [ni.jɑ́ːm] 
166-
--
249: Shapira, Dan D. Y. ( 2009 ), “Irano-Arabica: contamination and popular etymology. Notes on the Persian and Arabic lexicons (with references to Aramaic, Hebrew and Turkic)”, in Христианский Восток – Новая Серия , volume 5 (XI) , Moscow: Издательство Российской Академии Наук и Государственного Эрмитажа , pages 177–178 fn. 86 
250-
251- Wolff, Fritz ( 1935 ), Glossar zu Firdosis Schahname ‎ [5] (in German), Berlin: Reichsdruckerei, page 829b 
252-
253- “ ndn 2 ”, in The Comprehensive Aramaic Lexicon Project , Cincinnati: Hebrew Union College, 1986– 
254-
255- “ ldn 2 ”, in The Comprehensive Aramaic Lexicon Project , Cincinnati: Hebrew Union College, 1986– 
256-
257- “ nym 3 ”, in The Comprehensive Aramaic Lexicon Project , Cincinnati: Hebrew Union College, 1986– 
258-
259- Retrieved from " https://en.wiktionary.org/w/index.php?title=نیام&oldid=91032499 "
260-
261- Categories : Persian terms inherited from Middle Persian 
262- Persian terms derived from Middle Persian 
263- Persian terms inherited from Old Persian 
264- Persian terms derived from Old Persian 
265- Persian terms with IPA pronunciation 
266- Rhymes:Persian/aːm 
267- Rhymes:Persian/aːm/2 syllables 
########## 2dda4fa85c460fcb
73: Etymology 
74-
75- 2.3 
76- Pronunciation 
77-
78- 2.4 
79- Noun 
80-
81- 2.4.1 
82- Derived terms 
83-
84- 2.5 
85- References 
86-
87- Toggle the table of contents 
88-
89- نبرد 
90-
91- 6 languages 
--
190: Etymology
191- [ edit ] 
192-
193- Inherited from Middle Persian [Book Pahlavi needed] ( nplt' /⁠nipart⁠/ ) , derived via well-known prefix ni- from the stem of the verb which is in Neo-Persian بردن ( burdan ) .
194-
195- Pronunciation
196- [ edit ] 
197-
198- ( Classical Persian ) IPA ( key ) : /na.ˈbard/ 
199-
200- ( Dari, formal ) IPA ( key ) : [nä.báɹd̪] 
201-
202- ( Dari, formal ) IPA ( key ) : [nä.báɹd̪] 
203- ( Kabuli ) IPA ( key ) : [nä.báɹd̪] 
204-
205- ( Hazaragi ) IPA ( key ) : [nä.báɹd̪̥] 
206-
207- ( Iran, formal ) IPA ( key ) : [næ.bǽɹd̪̥] 
208-
```


## [2026-09-07T19:36:57.506Z] TOOL CALL #50: Bash

```json
{
 "command": "cd data/verification/sources/web && sed -n '215,275p' 0097c36e54f76601.txt",
 "description": "Read niyaz Persian section"
}
```


### [2026-09-07T19:36:57.558Z] TOOL RESULT

```
 نیازی ( niyâzi , “ pertaining to entreaty ” ) 

 Descendants
 [ edit ] 

 Turkish: niyaz 

 Further reading
 [ edit ] 

 Çağbayır, Yaşar ( 2007 ), “ niyaz ”, in Ötüken Türkçe Sözlük (in Turkish), volume 1, Istanbul: Ötüken Neşriyat, page 3557 

 Devellioğlu, Ferit ( 1962 ), “niyâz”, in Osmanlıca-Türkçe Ansiklopedik Lûgat ‎ [ Ottoman–Turkish Encyclopedic Dictionary ]‎ [1] (in Turkish), Istanbul: Türk Dil Kurumu, page 1008 

 Kélékian, Diran ( 1911 ), “ نیاز ”, in Dictionnaire turc-français ‎ [2] (in French), Constantinople: Mihran, page 1294 

 Meninski, Franciszek à Mesgnien ( 1687 ), “Supplicatio”, in Complementum thesauri linguarum orientalium, seu onomasticum latino-turcico-arabico-persicum, simul idem index verborum lexici turcico-arabico-persici, quod latinâ, germanicâ, aliarumque linguarum adjectâ nomenclatione nuper in lucem editum ‎ [3] , Vienna, column 1634 

 Meninski, Franciszek à Mesgnien ( 1680 ), “ نیاز ”, in Thesaurus linguarum orientalium, Turcicae, Arabicae, Persicae, praecipuas earum opes à Turcis peculiariter usurpatas continens, nimirum Lexicon Turkico-Arabico-Persicum ‎ [4] , Vienna, column 5294 

 Nişanyan, Sevan ( 2002– ), “ niyaz ”, in Nişanyan Sözlük 

 Redhouse, James W. ( 1890 ), “ نیاز ”, in A Turkish and English Lexicon ‎ [5] , Constantinople: A. H. Boyajian, page 2116 

 Persian
 [ edit ] 

 Etymology
 [ edit ] 

 Cognate with Sogdian [script needed] ( ‘ny’z(h) , “ need ” ) .

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /ni.ˈjaːz/ 

 ( Dari, formal ) IPA ( key ) : [ni.jɑ́ːz] 

 ( Dari, formal ) IPA ( key ) : [ni.jɑ́ːz] 
 ( Kabuli ) IPA ( key ) : [ni.jɑ́ːz] 

 ( Hazaragi ) IPA ( key ) : [ni.jɔ́ːz] 

 ( Iran, formal ) IPA ( key ) : [ni.jɒ́ːz] 

 ( Tajik, formal ) IPA ( key ) : [ni.jɔ́z] 

 Rhymes: -aːz 

 Readings

 Classical reading ? 

 niyāz

 Dari reading ? 

 niyāz

 Iranian reading ?
```


## [2026-09-07T19:37:09.420Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY && for w in \"نیاز\" \"نگون\" \"نژند\" \"نوردیدن\" \"نشیب\" \"نبرد\" \"نیام\" \"نهادن\" \"نمودن\" \"نیوشیدن\" \"نگاه\" \"نوشتن\" \"نشستن\"; do echo \"### $w\"; grep -n -- \"$w\" ARY_pages.txt | head -4; done",
 "description": "Aryanpur greps"
}
```


### [2026-09-07T19:37:10.729Z] TOOL RESULT

```
### نیاز
341:این پرسش منطقی نیاز به جواب دارد: کاوش‌های باستانشناسی و واژگان غیر هند و اروپایی
1049:خدایان بود. او نیاز انسان‌ها را (همراه با نیایش و قربانی) به خدایان اظهار می‌کرد و آنان در مقابل
1200:بی‌نیاز می‌کند.
1617:معنی این واژه در یونانی؛ نیاز» مشقت.
### نگون
20:بسیاری از آنها غیر هند و اروپایی باشند. بهمین دلیل از آوردن اینگونه واژه‌ها خودداری کرده‌ام.
34:ارائه شده است نیز کم نیست. مسئولیت درستی اینگونه واژه‌ها و به طورکلی همه مطالب این کتاب را
86:نژادی بر سایرین برتری کامل داشتند. چون در آلمان و اسکاندیناوی اینگونه مردم فراوان ترند؛ آنها
574:۱ طریق پیگیری پسگرایانه‌ی شکل واژه‌ها) تعبین کرده‌اند. نمونه‌ی زیر مسیر اینگونه بازسازی‌ها را در
### نژند
### نوردیدن
### نشیب
### نبرد
917:۱-برابری و اخوت.۲- رفتار نیمه جنونآمیز و سرمستانه هنگام نبرد یا تهاجم یا مراسم وابسته به
1616:۲ معلی این واژه در سانسکریت: آرزو؛ نبرد.
11785:۲- در فارسی واژه‌ی " کارزار" بعنی "محل نبرد؟: "کار" * نبرد و پا جنگ و آزار"< محل (مانند "گلزار").
15276:چم این واژه در زبان‌های ژرمنی و اسلاوی: جنگیدن» صدمه زدن) نبرد» خونریزی. "
### نیام
### نهادن
1339:سخت بیمار برد خوب شد و تب او «ریختء و لذا نام شهر را «تبریز» نهادند! باید پرسید قبل از این
### نمودن
14878:چم این واژه در اوستی: شمردن؛ حساب نمودن,
15605:چم این واژه در زبان‌های انگلیسی نرین: برازیدن» نمودن.
### نیوشیدن
### نگاه
363:محلی که گراینگاه آن در مرکز این موجهای کوچگری (یعنی شمال دریاهای خزر و سیاه) بوده به
1272:واژه‌های همریشه همه دارای معنی همسانی بودند آنگاه می‌توانستیم با اطمینان پیشتر ننیجه بگبریم؟ و
1897:این واژه با واژه‌های آنگاه" و "چشم " همریشه است. بازگشت به؛ نگاه. :
6614:> بازگشت به: چشم آگاه» نگاه,
### نوشتن
### نشستن
1282:(به معنی هستی دادن و پا روی تخم نشستن و جوجه آوردن) نیز از همین ريشه باشند.
7697:چم این واژه در زبان یونانی: نشستن» خود را شق نگهداشتن.
13387:۲ برخی واجریشه شناسان معتقدند که ریشه‌ی این واژه "محل نشستن" است و لذا با واژه‌ی انگلیسی 817 (به چم
14751:۸ ا نشست. نشاندن» نشستن ۱
```


## [2026-09-07T19:37:27.731Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && grep -n \"\\[pdf page\" BQT_v4_pages.txt | head -3; echo \"---- count\"; grep -c \"\\[pdf page\" BQT_v4_pages.txt; echo \"---- search nazand\"; grep -n \"نژند\" BQT_v4_pages.txt | head; echo \"--- nashib\"; grep -n \"نشیب\" BQT_v4_pages.txt | head -5",
 "description": "Inspect BQT vol 4 OCR"
}
```


### [2026-09-07T19:37:27.823Z] TOOL RESULT

```
1:[pdf page 1]
2:[pdf page 2]
23:[pdf page 3]
---- count
553
---- search nazand
8095:نجب ؟ « بنتح اول وئانی وسکون بای | سمند » بمعنی نژند اس ت که اندوهگین وغمناك
--- nashib
9162:نشیب ؟ - یکر اول و ثانی و سکون لشیمن دیق - کنابه از دنیا و عالم
```


## [2026-09-07T19:37:36.001Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && python3 - <<'EOF'\nimport re\nL=open('BQT_v4_pages.txt',errors='replace').read().split('\\n')\ndef tag(n):\n    for i in range(n,0,-1):\n        m=re.match(r'\\[pdf page (\\d+)\\]', L[i].strip())\n        if m: return int(m.group(1)), i\nfor t in [8095,9162]:\n    print(t, tag(t))\n# print first lines of some pages to find printed numbers\nfor pdfp in [478,479,480,500,540]:\n    idx=[i for i,l in enumerate(L) if l.strip()==f'[pdf page {pdfp}]']\n    if idx:\n        print('---pdf',pdfp, L[idx[0]+1:idx[0]+4])\nEOF",
 "description": "Map BQT v4 pdf pages"
}
```


### [2026-09-07T19:37:37.265Z] TOOL RESULT

```
8095 (202, 8089)
9162 (230, 9158)
---pdf 478 ['-۰ ۳۹ 1 هوش\u200cواژن', 'هوشنگ! - بانای مجپول وفتح | وکتاب جاویدان خرد که بجاوید نام اشتهار دارد', 'ثالك وسکون نون وکاف فارسی» بمعنی امر اول | آزوبادکارمانده ات۱ » ووجه تمیةٌ او به\u200cپیش']
---pdf 479 ['هوشیدن 8 -۳۹۹-', 'قیض وین راکشف ومشاهد»(۱) کویند 4 دوالی است که آنرا دازی رومی گوبند و آن', 'هوشیدن! - بروزن جوشیدن,بسمنی | حبی باشد سرخ برنگه سماق بقدادی و بمریی']
---pdf 480 ['نها حول', 'هوفسطیداس! - بنم اول وق\u200cفا | آنرا بفارسی شنکار وبمربی\u200cخمیرا خوانند. ب رکه', 'وسکون سبن بی\u200cقطه وطای حطی بتختانی رسیده آن سیاه بسرخی مایل\u200cاست. با سر که بربعق\u200cطلا']
---pdf 500 ['4۱۷ بلس', 'کنان واراده کنان (۱)- وییمانه کنان باشد . وهبات باشد.', 'پازد۱ بروزن سازد » بعنی آراده کند پاز نده؟ « بروزن سازنده, بمعنی قضد']
---pdf 540 ['<۷و)۲- بوسف روز', 'وجوینده وطلب کننده باشد۱ - ونام جانوری\u200cهم | شبیه به\u200cپلنگهه - ومعنی فلطیدن ومراغه کردن', 'هست شکاری کوچکتر ازپلنکه؟ - وسگه نولةٌ | جانوران هم هست9 - واسگه تولةٌ شکاربرا لیز']
```


## [2026-09-07T19:37:51.454Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && python3 - <<'EOF'\nL=open('BQT_v4_pages.txt',errors='replace').read().split('\\n')\nimport re\nfor pdfp in [200,201,202,203,229,230,231,239,240,241,269,270,279,280]:\n    idx=[i for i,l in enumerate(L) if l.strip()==f'[pdf page {pdfp}]']\n    if idx:\n        print('pdf',pdfp,'|',L[idx[0]+1][:80])\nEOF",
 "description": "BQT v4 printed page headers"
}
```


### [2026-09-07T19:37:52.886Z] TOOL RESULT

```
pdf 200 | ۳-۱۷ یه
pdf 201 | بیان سیم
pdf 202 | ۱۱۹۳- سیل
pdf 203 | بیان ششم
pdf 229 | شکرده -۱4۹-
pdf 230 | -۱۸۷- ات
pdf 231 | بیان سیز دهم
pdf 239 | ض ۱ -۱۹-<
pdf 240 | -۱۷- ره
pdf 241 | قره بآهن رسیدن ۸و۱
pdf 269 | نوراهان -۱۸۹-
pdf 270 | ده توروال
pdf 279 | نوی ۲۱۹۹۳
pdf 280 | ۱۹۷ نوشلو
```


## [2026-09-07T19:37:57.166Z] TOOL CALL #55: Bash

```json
{
 "command": "python3 tools/ref_page.py BQT:2134 2>&1 | head -40",
 "description": "Try ref_page for BQT 2134"
}
```


### [2026-09-07T19:38:03.390Z] TOOL RESULT

```
(no exact page map; using offset -1917 -> pdf page 217; check the printed number and re-run with --pdf-page if off)
REF: BQT:2134  PDF: data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf page 217  OCR-lang: fas

قزه ۹ -۲۱۳2-
نزه ۱ - بفتع اول و ثانی و ظپور ها » وتران ی کردنآب را یز گفته‌اند .
بمعنی سقف باشد ؛ وبسی کوبنگ چوبی باش دکه لزپدن * « بر وزن وزیدن » بمعنی
مسقف خانه را بدان پوشند - وجای درآمدن باد بیرون کعیدن باشد .
در نون با زای فارسی مشتّمل بر نه لغخت
قر « بفتح اول و کون ثانی » بیرون گوهری که اصیل باشد » و نژاده تفسیر اصیل
کشندءة چیزی راکوبند ۲ - و دندانه‌کلید راهم است *۱.
کنت‌ازد ۴ ۰ نزغار ۱ باغین نقطه‌داربروزن رفتار,
نراد ۰ < بکراول بروزن نخاط » اصل بانگه و فریاد ونعره راکوبند .
و نسب را گوبند ۱,- و بمعنی اسیل و نجیب رم ۱۳< بکسر اول وسکون نانی ومیم؛
وخداوند اصل ودب هم‌آمده است ۷ . بمعنی‌میغ‌است وآن بخاری باشد تاريك وملاصق
فژاده * - بکس اول بر وزن فتاده ۰ | زمین ؛ وبضم اول هم بنظر آمده است که عربان
بمعنی نژاد است که اصل ونب و اصیل ونجی | ضباب خوانند .
باغد ‎٩‏ ؛ و بفتح اول هم آمده است - و بمعنی ۰ قوف ۱۴سیکراول وفتح ثانی وسکون
۱ - رك : ره تژه (۱). ۲ - این‌کلمه صوره تربدن »۰ « تزیدن » و «تژیدن»
درين کناب آمده است )0( رك : نژ » نژددن . ۴ -رك : نژیدن .
۴ - در لغت فری (ص 44۲ ) « تزه » با شاهد بدین همتیآهده ۰ ور4: قره » تژه .
8 - اوستا 081221 , قی : سانکریت -1211[ :3 اسدق ۰.۹۱۰۳۰
‎٩‏ - من نناکوی توام زیرا تژادم نیت بد خود تکوکوی ترا هر‌کزنبوده بد نژاد.
سنائی غزنوی ص ۵۵۳ >.
۷ - بان معتی« نژاده» (ه.م.) قصبح است . ۸ از : نژاد (ه.م.) ۰1 ( پوند
سبت و اصاف ) رك : اسشق ۳۰
‎٩‏ - آزرده این وآن بحذر از من کوبی که از تژاده تنینم .
ناصر خسرو بلخی ص ۲۷۰ .
و رك : تارخ سیستان ص ۸۷ متن واح ۳
کمین دولت و در مرتبت کرفته مکان ملك نژاده و اسر مکان ملك مکین .
« فرخی سیستانی صس ۰۲۹۵
‎٩۱‏ مصحف « ژغار (ج م.) ‏ زغار («م.)
همچنین در پارسی باستان 081128110 ( خوار کردئی » فروافکندنی ) مفروض است. ر4: اسشق
۱ ؛ و رك : یبرگه س ۱۵۸ (52۳ - 26ماونده ).
```


## [2026-09-07T19:38:22.315Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && python3 - <<'EOF'\nimport re\nL=open('BQT_v4_pages.txt',errors='replace').read().split('\\n')\ndef page(p):\n    i=[k for k,l in enumerate(L) if l.strip()==f'[pdf page {p}]']\n    if not i: return ''\n    j=i[0]+1\n    out=[]\n    while j<len(L) and not re.match(r'\\[pdf page \\d+\\]',L[j].strip()):\n        out.append(L[j]); j+=1\n    return '\\n'.join(out)\nfor p,pr in [(218,2135),(228,2145),(254,2171),(284,2201),(294,2211)]:\n    t=page(p)\n    print('='*20,'printed',pr,'pdf',p)\n    print(t[:2200])\nEOF",
 "description": "Print BQT v4 cited pages from OCR"
}
```


### [2026-09-07T19:38:23.749Z] TOOL RESULT

```
==================== printed 2135 pdf 218
-و۲۱۳-< س‌
ون و دال ایجد » بمعتی اندوهگین و غمناکه قژه - بفتح اول و ثانی وظهور ها» خاخ
وفرومانده و افمرده و سرفرود افکنده و پژمرده | درختی راکوبند که بسیار نازك و لطیف برآمده
باشد ‎٩‏ - و بمعنی‌سر گشته وخشمکین وفهرآلود | باشد ۴ - و ورق طلا و نقره رانیز کوبند که
هم هست - وپست و حضرض را نیز کوبند که در | بهیأت بر که کل بریده باشند و برسر پادشاهان
مقابل بلند واوج باشد ۴ ؛ وبفتح اول هم آمده | و نودامادان نثارکنند ۴ - ونام ستاره‌ای هم‌هست
است . از ثوابت * - و چوبی که بدان سقف خانه را
نک ۴ - بفتح اول و دون بر وزن پوشند ۴ .
نغزك , دام و تله راکوبند که حیوانات را بدان فژیدان ‎٩‏ » بروزنومعنی کشیدن باشد.
گیرند.
بیان یاز دهم
در نون با سین بی‌نقطه مشتمل بر سی وهشت لغت و کنایت
: پوز باشد که گردا کرد لب و دهان امت ازجا
سس - بنم اول و سکون ثانی » بممنی درون و بیرون ۷ - و بمعنی هو وشمور وعقل
() چك : ژد ویاژند .
۱ - هربرکی از اوكونة رخار نژفدیست ‏ هوشاخی ازوزصورت انگفت نگارست ۰ :
« فرخی سیستالی ص ۲۶ *.
- بغاك اسر افکند خوار وتژند فرودآمد ودست کردش ببند +
فردوسی طوسی « شاهنامة پخ اج ۳ص ۰۸۹۵
۴ - در جهاتگیری « نژنگه > بفتح اول و اسکون دوم آهده ‏
۴ - موّلف فرهنگه نظام نویسد : « جهانگیری مه معنی دیگرهم ( شاخهٌ نازك درخت-
و ورق زرنثار - وتیر سقف ) برای « نژه> نوشته که تصحیف خوانی« تژه > است و درشعر شاهد
از سیف اسفرنگی برای معنی شاخه وزرورق هم باتاء‌است . شعر این آمت :
پنجةٌ سرو از طرب بر دست گیرد جام مل طرء بید آزتژه بر کلشن‌افمانده(افعاند) تژه .>
و رك : تژه » لزه- 8 - باین معنی در جهانگیری بدون شاهد آمده .
۹ - این کلمه صوره نزیدن »۰ « تریدن > و۸ تربدن > درین کناب آمده , و رك : ات .
۷ - در نخ متعدد لغت قری « لس » بهمین معنی آمده و این بیت رود کی (سمرقندی)
شاهدآورده شده :
کیرآلوده بیاری و هی د رکی‌من بوسه‌ای چند پتزویر دهی بر نی هن.
رك : لغت فرسی ص ۱۹۹ -
در رود کی مسحح نفیسی ج ۳ص ۱۳۹۹ :۱ بونه‌ای چند بتیرو پزلی بر نی هن -
وسوزنی سمرقندی کوید :
خرخر بنده بد لنچ ونی را پز بازی کر استا د کردم . « فرهنگه نظام >.
بقیه در حاشية صفحةٌ ۲۱۳۹
==================== printed 2145 pdf 228
ستنذها شکرد کازران
حال داری هم هست. نشخود ؟* - با وار معدوله بر وزن
نشخار ۱ » بنم اول و خای نقطله دار | کشور » بممنی نششوار است که کفته شد وینی
بالف کشیده برا وزن هشیار , آنچه شتر وکاز | مکررخاییدن وچانه برهم‌زدن شتران و کوسفندان
وگوسفند وامثال آن خورده باشند و باز از ممدم | را لیزگفته‌اند فرو بردة خود را ۰
بدهنآورند وبخایند وفروبرند وآثرا بعرهی جره نشرخ * طفلان - آنچه با زغران
کوبند - وبقید‌کاه وعلفیر| نیز کویند که ازدواب | وغیره پر روی تشنة اطفال تویسند .4
بازماند وآنرا بعربی تشوار خوانند ؛ وبکر اول نك ‎٩‏ « بفتح اول ‎)٩(‏ بروزن اغك.
هم‌آمده است . «رخت سنوبر وکاج راگویند .
نشخو‌ار ؟ - با راو معدوله . پمعنی نشکرد گازران ۷ (۷)- بممنی
نشغار است که نیم خوردة علف متوران و ا زکلو | اسفنج است که ابر مرده باشد و آن چیزی است
برآورده وخابيدة شتران وامثال آن باشد ۴ . ماشد نمد کرم خورده وآ ترا بعربی‌هرشفه ورغوة
() خم۱:- بفتح اول + () چش : کازران .
۱ - اسح « نشخوار » (ه.م.) است . ۴ - از : ند (نوش ()) )+ خوار(خوردن)
۳ شخور « رشیدی > قی : نشغار (ه.م.) نوششوار , نوششور (ه.م.) , نشخور , نشوار (معرب)
* فولرس ]1 ۰۱۳۹۷ ۰۱۳۲۰
۴ شش سال بکام دل وآسانی خوردند باید زدن امروز چو آشتر همه شخوار.
« فرخی سیستائی ض ۱۵۹ ۰
۴ «شخوار (هم.) - (عر) ۵ نشره بنم اول اقولی است که علاج کرده
میشود باو دیوانه و بیمار .» « شرح قاموی > . ۹« شك . درخت با («.م.) باشد .
رودکی ( سمرقندی کوید
آن که شك آفرید و سرو سهی وان که بید آفرید و لار و بهی.»
« لفت فری ی ۰۲۹۶
۷ -رك : گازر.
۰ نشتی - بکر اول وافتح دوم (در لهجهٌ مرکزی بکسر دوم ) و فتح چهارم » پارسمی
باستان - 83-۳۳24 . متمدی 737883248270 ؛ ارستا - 186 + 51 . 891002141
( شتن ) . متمدی تا8082(/818 ون . یخلوی 8)1(9025430 ۰ 1)1(8[17261 , هندی
باستان - 81920 . 514241 ۰ بلوچی 810028 . 812427 ۰ دی 81501012880 .
ر4 : اسشق ۱۶۳۳ ؛ زمان حال « تشینم » از ل(68151010820(1 ناشی‌است چنانکه « شکنم »از
ل(ص 09۵00 ۲ , اففنی 325421 - ( تن ) «هوبشمان۱۰۳۳*» کردی 1315010 (شتن)
« ژابا ی 2۲۰ ۰ نیز کردی 02-815[18 ( شتن ) «ژابااس۲:۱۷۲ »کیلکی 0180122 ۰
دراراك ( سلطان]آباد ) یز 8158128 * مکی‌نژاد » ؛ متعدی‌آن شاستن (ه.م.) » شاختن (ه.م.).
شاندن (ه.م.) ؛ فرا رگرفتن . مستقر شدن جاندار بر روی کفل وسرین خود برجایی - جا کرفتن
چیزی درچیزی (همچون تیربرشانه) - منزل کردن - جلوی برتخت سلطنت وامارت : «ایوالمپای
الممتند یال ... بامیری اشت وآنرو ز که پدر مرد معتند محبوی بود » چون بنشت اول چیزی
آن فرمو
==================== printed 2171 pdf 254
-۹۱۷۱- اموله
زده ‏ بمعنی‌نمایان ومرئیباشد۷ - وغبه ومانند- | نموسك است که تیهو باشد و درقارسی سین‌وشین
ودلیل و برهان را نیز کوبند ۲ .4 بهم تبدیل‌میيایند ؛ وجضم اول‌هم بنظر آمده است.

نموست ؟ » بروزن عروسك» پرندف نموك * - بنتح اول وتانی بوا و کشیده
ایست که آنرا تیهو میگوبند و کوچکتراست از | وبکاف زده , بشانةٌ تهر را کوبند که هدف باشد.
کبك . نموه ۱ - بفتح اول وفون آخر,بممنی
نموشات ۴ - بروزن خموعك. بممنی ناتمام و ناقص و بکار نیامده ۷ - و زشت ۸ -
۹ - نموداری که ازمه با بیاهی است طلسمی بر سر کنج الهی است .
نظامی کنجوی « کنجینه ص ۱۵۸ .
۲ - و نیزنونه , مقدارکم ازچیز ی که دال بربسیار باشد -
ی نموعك « جهانگیری» « محیط اعظم > رك : موعك .
۴ س تمونك (هم.) 8 - مصحف « تبو4 > (ه.م.)
‎٩‏ از : نمون ( از «نمودن» » قس : نمونش [ اسم مصدر بقلم انگارنده ی ۳۲-۳۱])

+ ( پوند سبت وانصاف)؛ معرب‌آن نیز «نمونه» «دزی اج ۲ص ۲:۷۳۷. کردی 2672086

« ژابا ص ۶۲۶ معنی اصلی‌آن : مثال» نموده ونموداز (۸.م.) » انمون ج :
نگاری کز او بت نمونه شود بیارایی او را » چگونه شود ؟!

عنصری بلخی « لفت فری ص 2۹۱ > ولی درین مأٌخذ برای معنی نابکار < شاهد‌آمده است.

۷ - « نمونه بابکار بود > « لغت فری صن*2۹ > ۸ - در اینکه تمونه بمعنی

زشت و ازکار افتاده است شکی‌لیت « اقبال . لفت فری ص*2۹ ح ۰

کتاب و كلك همه کاتبان نمونه شود چو كلك اوینگارد صحیفه‌های( کتیبه‌های) کتاب.

معزی لیشاپوری «رشیدی» «لفت فری ص *2۹ ح ۵ استاد هنینگه نوید : نموه ع 3
( 8018006 ) بمعنی مثال ونمودار معروف است » ونیز بمعتی « بیفایده و بیهوده ‏ زشت «خوار
و زیون > آمده . ر4 : امدی (چاپ هرن) ص ۱*۶۸ ۰ شمس فخری اس ۱۳4 ( 33 ۰ ۱۸۸) ‎٩‏
‏عبدالقادر ۸/۲۹۰۷ ؛ فولری ]1 . ص ۱۳۵۲ . معنی اخیر بنظر میرسد که باگروه لغات سغدی

بقیه ور حاشيةٌ صفحٌ بعد
نمودنی - لغة و در لهجةٌ مرکزی یکسر اول (نیز جشم وقتح اول تلفظ شود) وفتح -
چهارم ؛ از : نمو + دن ( پوند مصدری ) « دارمتر . تتبعات اج اص ۱۹۷ ۰ ۲۸۳ ۰ پپلوی

2 > ایرانی‌باستان.-(9) ۳122 83 ( جزو اول پیشوند بمعنی فرودء پایین ؛ وجزو دوم
بمعنی اندازه گرفتن و جمعاً پمعنی نمایش دادن ) «* بارتولمه ۶۱۱۹۵ «* لیب رکه ص ۳۵۹ ۰
استی 23832708 , 8180218 ( حاب کردن » شمردن ) » سربکلی » شغنی 670-/[881738
( نمودار شدن , ظاهرشدن) «اسشق ۱۰۸۷ > ؛ نشان دادن » اظهار کردن , اراله دادن +

صالح وطالح متاع خوبش نمودند تا که قبول افتد وکه در نظرآید؟
« حافظ غیرازی ص ۹۵۹۷ ۰

-کردن : احان نماید وننید منت منت نهاد هر که نمود احان .
فرخی سیستانی ص ۲۸4 ۰6
«گف
==================== printed 2201 pdf 284
۱ بوشدارو
نوشن - بکسر اول و ثانی : معروف پیچیده ودرلوردیدء باشد 8 .
است که چیزی نوشتن وکتابت کردن باشد ۱ ؛ نوش خور .> بروزن موش خور » نام
و بنم اول هم بنظرآمده است - ویفتح اودوئالی | روز پنجم است از ماههای ملکی.
بمعنی‌درلوردیدن وطی کردن وییچیدن باشد ؟ - نوشدارو - نرباق رپازمرراگوند ‎٩‏
‏و بر وزن دوختن» بمعنی نوشیدن و آخامیدن و ای تر باق وپازهررا
باشد ۴ . ۱ - و یکی‌ازنامهای شراب است ۷ ؛ وبعتی گوبند
نوشته - بکراول وتانی, بممنی کتابت ! نوغداروکنایه ازشراب است - و لام معجونی هم
کرده شده و رقم نموده ۴ - وبفتح اول » بمعنی هت ۸.
۹ نیشن * بیعتن » پپلوی 21015۳8188 (- 81885 ) ( تحریر کردن ) » پارسی
باستان -0215 ۳ 38 (نوشتن) «بارتولمه۸۱۷» «لیب رکه *۱۹*. درپارسی باستان/[83019101822,
هندی باستان-086. 0186411 فقط بمعنی‌آراستن وزبنت دادن است , اسلاوی کلیایی 81921,
استی 10890 , 51888 , 818 گنه ( نوشته » خط ) . بلوجی ع 2101928 » وخی و شغنی
و سریکلی م 86۷1912820 . رك : اسشق ۱*۵۱ ؛ کردی 8۷1918 ( تحربر ) «ژایا س 4۲۹*.
واه لپشتن با نوشتن چندین بار در سنگه‌لیشته‌های هخامنشیان بکار رفته است, مرکب است ازدو
جزه : لخت لی 8 جزئی ( پرفیکس » پیشاوند ) است بمعنی فرود و پایین که درسرلغات بهقتن
ونهادن وشتن و بمیاری ازلغات دیگر فارسمی هم دیده میشود. دوم از ربشةٌ 0218 درپارسی‌باستان
و 2269 دراوستا که بمعنی نگاشتن و نگاریدن و نفش کردن است . ازهمین بنیاد است عقاوم
که در پهلوی بممنی نش ونگار بسته وزینت شدماست؛ ودر قارسی «پیسه» شدء بمعی ابلق ودو
رنگه فاب‌اص ۰۱۱۳ ۴ بوردیدن (وم.)- نوردن (.م.)
۴ - باین هعنی « نوشیتن > ر4 : نوشیدن . ۴ - اسم مفعول از « فوشتن >
( یکر واو)-
8 - اسم مقعول از نوشتن ( بفتح واو). ‎٩‏ از : نوی ۳ دارو ؛ پهلوی<[8283
( کسیر » نوشدارو ) « منای ۲۹۹ و رك : نوش . ۷ - رك : رشیدی .
۸ - فردوسی در داستان جنکه رستم و سهراب وکشته شدن سهراب آردکه چون رستم
داست سهراب فرزند اوست که بدست وی هجروح کردیده »
بگودرز کفت آن زمان پپلوان که ای کرد با نام روشن روان
پیامی از امن سوی کاوی بر بگوش که ما را چه‌آمد بس
بدشنه چگرگاه یور دلیر دریدم که رستم مناد دی
گرت هیچ باد است کردار من یکی رنجه کن دل به نیمار من
ازآن نوشدار و که د رکنج تست کجا ختگان راکند تن‌درست
بنزديك من با یکی جام می مسزدکر فرستی هماکنون زیی-
بیامد اسپهید بکردار باد بکاروی بکسر پیامش بداد.
بدو کفت کاوس کز پیلتن کرا بیشترآب تزديك من ۲...
ولیکن اگر داروی نوش من دهم , زنده ماند پل پیلتن ۰
کند پست رستم بنیرو ترا هلاك‌آورد بی کمان مرمرا ...
ف
==================== printed 2211 pdf 294
-۲۱۱- هار
لای غفی هربی هم هست۱ + مهمانی ودیدن مردمان بزر که پوشند ویغیر از
نهاد؟ - بکسراول, ماضی‌نهادن‌است که | این روزها درجایی بسته نگاه دازند.*
بمعتی گذادتن باشد - وبنیاد و سرشت و خلفت نهاره بنتم اول بروزن بهارءمخغف باهار
وطیتت - وباطن را نیز کویند۴ - و بفتح اول » | است که چیزی اخوردن ازبامداد باشد تامدتی‌از
بمعنی طرز وروش ورسم وعادت باشد۴ . روز - ودر عربی از وقت طلوع صبم‌سادق‌است
نهادگی* «بر وزن فتادگی جامه | تاوقت برآمدن آفتاب"- وچ خرچال و سنگه
و لباسی راکوپند که در روزهای مید و روزهای خوارك را نیز گوبند ۷ - و بکر اول » بمعنی
۹ - فارسی جدید 288 ( امروزه 88 تلفظ شود م .م . ) -383 » پهلوی 88 (هز .
7 1) . ایرایی باستان 98811 . اوستا 2۵11 « بارتولمه ۱*۷۲ « لیب رکه ۱۵۹ > هرن
کوید : 86 ( 868 نوشته شود ) » اوستا 82 ۰ پازند 88 , هندی باستان 24 ۰ افغانی 22 ۰
آستی 36 ۰ 28 «اسفق ۱۶۵۵ ر4 : اه هوبشمان ۱*۵۵ کردی 88 (نه) » زازا 26 , 2606
« ابا ۰۰4۲۹ ۴ -رك : نپادن ۰ ۴ - باطن و درون : ۸« صاحبدلی بشنید ( فرمان
پادشاه را ) » فرباد ازنهادش برآمد .> «گلتان ص2۷ >. ۴ - ۵ نهادء رسم و آبین‌باشد.
رود کی ( سمرقندی ) گوید :
خدای عرش جهان را چنین نهاد. نهاد که گاه مردم شادان و که بود ناشاد .»
« لفت فری ۱۱۸ ۰
- نیز قرارداد و مواضعه : « اگر وی را امروز براین تهاد بل هکنیم آنچه خواسته آمده است از
غلام و پیل واسب واشتر وسلاح فرستاده‌آید :آنگاه فرستد که مهدی باشد که قصد خراسان کرده
لیاید .» « تاریخ پیهقی [ نامه مود بقدرخان ] مسحح دکتن فیاض ص۸۱ » - نیز بمعنی وضع:
« جنیش کرد - که کرد خود بود - از نهادی به نهادی بود » نه ازجای ( جایی ) به جایی ...»
« داشنامةٌ علائی . طبیعیات چاپ انجمنآثار ملی ص ۹۷ - از : نهاده ( نپادگه )
[ اسم مفعول ]ی ( حاصل مصدر واسم معنی ) [ جورت اسم مستعمل است ].
‎٩‏ - رل: تاهار_درزبان کنونیغذایی که‌وسط روزخورد. گیلکی2802۳ رك: نپاری فهاره.
۷ - (عر) ۶ نها رکجاب . روز ضد لیل یعنی دوشنی مابین طلوع فجر تاغوبپآفتاب »
با از طلوعآقتاب تا غروب‌آن ... وچوز؛ سنگخوار با جغدار با بچةٌ چوبینه و شوات‌ان » و مادة
آبرا لیل خوانند >. « منتهی‌الارب >. ۰
نهادن - یکسر اول وفتح چهپارم ۲ 81884022 . پهلوی اند (- طانه)
( کذاشتن . بهادن ) » ایرانی باستان - 81-448 ۸« بارتولمه ۷۲۱ > « نیب رکه ۹-۱۵۸ >. هرن
کوید : اوستا - 44+ 21 (21ط8484) (گذاشتن . بهادن ) » بهلوی 2)(04182 » هندی
باستان - 2ط14 + فد ( 214848520 ) ۵ اسشق ۱۶۵۷ > و رك : هوبشان ۱*۵۷ ؛ کردی
2 دانین » ناين» نپان «ژابا س ۶۱۶ + کیلکی 8887. رك:
```


## [2026-09-07T19:39:01.038Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && python3 - <<'EOF'\nimport re\nL=open('BQT_v4_pages.txt',errors='replace').read().split('\\n')\ndef page(p):\n    i=[k for k,l in enumerate(L) if l.strip()==f'[pdf page {p}]']\n    j=i[0]+1; out=[]\n    while j<len(L) and not re.match(r'\\[pdf page \\d+\\]',L[j].strip()):\n        out.append(L[j]); j+=1\n    return '\\n'.join(out)\nprint(page(230)[:2500])\nEOF",
 "description": "BQT printed page 2147 (nashib)"
}
```


### [2026-09-07T19:39:02.249Z] TOOL RESULT

```
-۱۸۷- ات
نام غهر خچوان اس ‎٩‏ . شتن‌است مطلفاً - وآشیان مرغ را لی زکویند.
نشیب ؟ - یکر اول و ثانی و سکون لشیمن دیق - کنابه از دنیا و عالم
تحتانی‌وبای ابجد » نفیضش فرازاست پعنی‌ت ۴ | است .
- وفروخزیده را نی زکوبند ۴ . نشیمه - بنتح اول بروزن جربمه,پوست
شید * - بکس اول و نانی و سکوت | ر باس خام پیراسته راکوبند ۸ که ازآن بند
تحتانی مجهول ودال » بمعنی سرود وخوانند کی کارد وامثال آن سازند -
تشون ‎٩‏ - یک اول رای »مخت 5 نُشَهِن - بروزن نگین . قطب را کوبند
اشانیدن بمعنی نهادن باشد . و آن نقطه‌ایت از فلك - و پوست درون مقعد
نشیم ۷ - بکر اول و تحتانی مجهول را هم کفته‌اند ‎٩‏ - و امن بنشستن هم هت‌پمنی
بروزن گلیم » بمعنی یمن باشد که جا و مقام | بنشین *۱.
۱- در قاموی نیز نشوی آورده ‏ وگفته که عوام نخچوان گوبند . « رشیدی >:
بار دیگر چنانکه میخواهم پرسالم بخطةٌ آنشوی .
صحاح الفری « فرهنگه نظام » ورك : نخجوان .
؟ - اوستا -0۳1811۷2608 , قی - 55۳0۷8602 ( رك : شیب )ءپپلوی8)1(5[087.
(فرود شدن) « اسشق ۰۱۰۳۸ پهلوی 81906021 (غروب [ آفتاب ومام] )»
پازند 21908۷۷۵ برای ۷888208 ( بهی ز که ) » کردی ع 0۷ 53۳ ( برگفته [ سر
بیایین] ) «هوبشمان ۰۶۱۰۳۶ کردی نیز ۵1980۷ ۰ 5[01#ف8 (شیب يك تیه ) ۰ 831۷ (دره)»
۷ ( پایین ) . 06983600 ( دره ) ‎٩‏ ژابا ی ۸۲۰ >.
۴ کی نه بیند فرو شده به شیب هر که را خواجه برکشد بفراز:.
فرخی سیستالی اس ۲۰۳ ۰
۴ -قی : عیبا (هم.) - (عر) ۵ شید بروزن امیر ‏ بلند کردن آواز است
وشعرست که درجواب با هم خوانده باشند . > « شرح قاموی > + ی
- اکر استعمال شده باشد بمعنی نشتن (۸.م.) است ۳ تن (۸.م.) و متمدی آن
نشاسدن * تشادن ( نهادن ) . ۷ - شیم طاطوند فارسی 1020-7۳ تطقاهه رك :
اسشق ۱۰۳۸ قاط ؛ فی : یمن , از« شتن» (هم.) . سانسکریت ع 816170888
( 433 310۰ , ۷۷/۵۳۵۶ . 60 ۰ 3278510۳) ۵ هوبشمان ۱۰۳۶ 5اطظ >.
۸ - ر4 : جهانگیری . درخراسان « مشیم > پوست بز دباغی کرده‌است «فرهنکه نظام».
‎٩‏ - نهرانی 8188170 (کون . سوراخ مقعد ) . در اراك ( سلطانآباد ) شین ( سوراخ
کون ) « مکی نژاد > ازه نشتن > و۵ شین >. *- رك : تن - ولیز آسم فاعل مرخم
درکلمات مر کب : صدر شین ؛ بالاشین » کرایه شین .
5 نصبی - رك : لغات متفرقهةٌ پایان کناب .
5 فضاره - رك4 : لغات متفرقةٌ پایان کتاب .
۵ نطاف - رك : لغأت متفرقهٌ پایان کناب .
نظارگی - رك : لغات متفرقهٌ پابان کناب +
```


## [2026-09-07T19:39:15.586Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -o \"نگون[^ ]* *\\[[^]]*\\]\" MON_part2.txt | head -10; echo \"---- nemudan\"; grep -n -o \"نمودن[^ ]* *\\[[^]]*\\]\" MON_part2.txt | head -10; echo \"---- context negun\"; grep -n \"نگون\" MON_part2.txt | head -3",
 "description": "Mo'in negun/nemudan"
}
```


### [2026-09-07T19:39:15.719Z] TOOL RESULT

```
---- nemudan
---- context negun
14153:و انگشتان مرد سخاو تمند. قلزم نگون: ( کد.) 
14158:استیصال. مسحوه نابودی. سرنگونی» 
18414:جام نرگس. کاس نگون: (کد.) آسمان. کاسة
```


## [2026-09-07T19:39:22.970Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Page(s): 235\\|Page(s): 235-\\|Page(s): 23[0-9]-2[34][0-9]\\|Page(s): 45[0-9]\\|Page(s): 88[0-9]\" POK_full.txt | head -20",
 "description": "Pokorny pages 235, 454, 884"
}
```


### [2026-09-07T19:39:23.025Z] TOOL RESULT

```
19734:Page(s): 233-234 
19777:Page(s): 235 
22276:Page(s): 235 
22510:Page(s): 235-239 
33232:Page(s): 450 
33259:Page(s): 450 
33279:Page(s): 451 
33363:Page(s): 451 
33404:Page(s): 451 
33437:Page(s): 452 
33450:Page(s): 452 
33499:Page(s): 453 
33521:Page(s): 453-454 
33549:Page(s): 454 
33583:Page(s): 453 
33602:Page(s): 452 
33661:Page(s): 455 
33733:Page(s): 455-456 
33766:Page(s): 456-457 
33795:Page(s): 457-458
```


## [2026-09-07T19:39:26.510Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for l in 22510 33521 33549; do echo \"===== $l\"; sed -n \"$((l-6)),$((l+1))p\" POK_full.txt; done; echo \"##### find sed lemma\"; grep -n \"Root / lemma: sed-\" POK_full.txt | head",
 "description": "Pokorny lemmas at pages 235,453-454,454"
}
```


### [2026-09-07T19:39:27.812Z] TOOL RESULT

```
===== 22510
extension would be attributed to Old Icelandic des {* dasjo) ' hay stick, hay rick ' (loanword 
from dem Old Irish?), Old Irish dais {* dasti-) 'heap, hay rick', wherewith E. Lewy (KZ. 52, 
310) compares rather osset. dasun^^We up, lump'. 

References: WP. I 826 ff , WH. I 266, 362 f , 439 ff , 863, Trautmann 47 ff , Schwyzer Gr. 
Gr. I 492, 686, 722, 725, 741, Pedersen Hittite 141 ff., 192. 
Page(s): 235-239 

===== 33521
variant assimilation and dissimilation, in addition Old Saxon gornon, gnomon, grornon^ 
grieve ', grun'm. " horror '; 

kiruss. zuryty 'affWct, sadden', zurba^ care ', russ. zurftb " scold '. 

References: WP. I 636, Feist 208. 
Page(s): 453-454 

===== 33549
skyth. EN DPaGaywaoq ' rattling, clashing by the war chariot ', Avestan zairi-gaosa-^W\Vc\ 
yellow ears'; 

about Latin heus^ hallo! ho, there! hark!' s. rather WH. I 643 f. 

References: WP. I 569, WH. I 643 f. 
Page(s): 454 

##### find sed lemma
72366:Root / lemma: sed- 
72560:Root / lemma: sed-: (to sit) derived from Root/ lemma: es-: (to sit). 
81278:derived from Root / lemma: sed- : (to sit). 
88989:see Root / lemma: sed- : to sit.
```


## [2026-09-07T19:39:33.452Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '22505,22520p' POK_full.txt | head -3; echo \"--- lemma head for 235-239\"; awk 'NR>=22400 && NR<=22520' POK_full.txt | grep -n \"Root / lemma\\|Meaning:\" | head; echo \"=== which lemma\"; grep -n \"Root / lemma\" POK_full.txt | awk -F: '$1<22510' | tail -3; echo \"=== sed- entry\"; sed -n '72366,72372p' POK_full.txt; sed -n '72515,72530p' POK_full.txt; echo \"=== 454 lemma\"; grep -n \"Root / lemma\" POK_full.txt | awk -F: '$1<33549' | tail -2",
 "description": "Identify Pokorny lemmas"
}
```


### [2026-09-07T19:39:34.728Z] TOOL RESULT

```
from dem Old Irish?), Old Irish dais {* dasti-) 'heap, hay rick', wherewith E. Lewy (KZ. 52, 
310) compares rather osset. dasun^^We up, lump'. 

--- lemma head for 235-239
115:Root / lemma: 6^6-3, d^^- 
117:Meaning: to disappear 
=== which lemma
22080:Probably from a fusion of Root / lemma: d'^eues- d^ues-, d'^eus-, d^us-'io dissipate, blow, 
22127:Root / lemma: d^e^/^- (besides d^-e/-?) 
22278:Root / lemma: d^e-2 
=== sed- entry
Root / lemma: sed- 

Meaning: to sit 

Grammatical information: originally only aoristisch, punctual "sich place' (Old Indie), later 

as duratives stative verb with e-suffix "sit' (Latin Germanic Balto-Slavic) 
4. More or less verdunkelte compositions: 

Old Indie nedJyas-^ nearer, closer', nedistha-^ uachsV = Avestan nazdyoadv. '(spacial) 
nearer, closer an-', nazd/sta-'t\r\e nachste', Avestan asna-M]. " near' {*6-zd-na-, 
participle Perf. Pass., compare full grade Old Indie asanna-^ near '). (under the influence 
of common Celtic -ns-, -nt- > -nn-). 

ni-zd-os, -o/77'nest' (prefix /?/■ "low, base', or 'ein-' as "place zum Nieder- or Einsitzen'): 
Old Indie n/da-m. n. 'Ruheplatz, lair', Armenian n/st^ position, seat, Residenz', Latin 
nldus'nest', Middle Irish net^nest', cymr. nyth^nest, dwelling', corn, ne/d, bret. nez, neiz 
ds.. Old High German Old English nestn. "nest'; 

Maybe zero grade of alb. Geg ( *ne/d) me ndejt'to sit' : corn, ne/d'nest'. 

with popular etymology Umgestaltungen Lithuanian lizdas, Latvian ligzda. Old Church 
Slavic ^/7ezo'c»"nest'; identical prefix in Old Indie nisTdati^ places sich', Avestan nishidaiti, 
=== 454 lemma
33501:Root / lemma: ghou-ro-s 
33523:Root / lemma: ghous-
```


## [2026-09-07T19:39:50.169Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '33523,33552p' POK_full.txt; echo \"===== sed page range\"; awk 'NR>=72366 && NR<=72560' POK_full.txt | grep -n \"Page(s)\\|References:\" | head",
 "description": "Pokorny ghous- and sed- pages"
}
```


### [2026-09-07T19:39:51.388Z] TOOL RESULT

```
Root / lemma: ghous- 
Meaning: to sound; hear 
Note: Only indoiranisch. 



Material: Old Indie ghosati^ sounds, announces aloud, hears ', ghosayatT fmae^momng 
lei (Akk.) ' (Geldner Rigveda in Auswahl I 58), ghosa-hru. " sound, clamor, shout, call, din, 
fuss, noise', Asvaghosa EN ' ear of the horse ', Harighosa EN " Yellow ear ' (= Avestan 
zairigaosa); 

Avestan ^aos-'hear', Kaus. in gusayal-uxda-^ sein Wort zu Gehor bringend ', npers. 
niyosTdan^heax, listen, eavesdrop ', Baluchi gosay^heax', n/yosay'hear, listen, eavesdrop 



Maybe alb. Geg n/gjoj, ndegoj {* nde-ghosa), Tosc degjoj, alb. Greece delgonj, alb. Arbersh 
dilingonj, ndelgonj, ndlegonj, glegonj^ I hear ' [common alb. gh- > gl- > gj- : Nth. gh- > dz-]. 

afgh. ngvaiar listen, obey ', Old pers. gausa-, Avestan gaosa-m. 'ear', npers. ^ds'ear', 
skyth. EN DPaGaywaoq ' rattling, clashing by the war chariot ', Avestan zairi-gaosa-^W\Vc\ 
yellow ears'; 

about Latin heus^ hallo! ho, there! hark!' s. rather WH. I 643 f. 

References: WP. I 569, WH. I 643 f. 
Page(s): 454 

Root / lemma: ghou(e)- 

===== sed page range
```


## [2026-09-07T19:39:59.591Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=72366 && NR<=72700' POK_full.txt | grep -n \"Page(s)\" | head -3; echo ---; sed -n '72366,72370p;72690,72700p' POK_full.txt",
 "description": "Find sed- Page(s)"
}
```


### [2026-09-07T19:40:00.956Z] TOOL RESULT

```
198:Page(s): 884-887 
212:Page(s): 887 
242:Page(s): 887-888 
---
Root / lemma: sed- 

Meaning: to sit 

Grammatical information: originally only aoristisch, punctual "sich place' (Old Indie), later 

Latin 5/5/"oup£T'; siare\s probably from *s/(75/'e after /77e5/'e"mingere' reshaped; siccus 
"dry'; 

gall, (goidel. orVenetic-lllyrian) FIN Sequana ^Se\ne', GN Sinquatis, FIN *S/par/s^Se\/re' 
= Irish FIN Sechair, 



Old High German sJhan 'strain ', Old English seon ds., intr. "ausflieften'; Old High 
German Old Saxon Old English 5/^a/7 "tropfeind fall, sink, flow'. Old Icelandic s/galow,
```


## [2026-09-07T19:40:09.335Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && grep -n \"nizdo\\|nĭ-zdos\\|ni-zdos\\|nitero\" WLD_Bd1_pages.txt WLD_Bd2_pages.txt 2>/dev/null | head -10; echo \"=== nether/nidar\"; grep -n \"nidar\" WLD_Bd1_pages.txt | head -6",
 "description": "Walde-Pokorny ni- section"
}
```


### [2026-09-07T19:40:09.407Z] TOOL RESULT

```
=== nether/nidar
34934:*hubbon in nhd. nidartl. hobbe(le)n .hinken" zu vereinigen, wenn es nicht
35749:nidartl. hrkh auch „Stoppel“, hekel (und skjekel
67893:abgestumpft“, norw. nidartl. stinta „knapp sein u u. dgl.          s. Falk-Torp u.                                 :
73268: tirr        norw. nidartl. tir „Ausguck, Spiihen, Leuchten, Glanz“, lira
```


## [2026-09-07T19:40:16.465Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && grep -n \"ni-, nei-\\|nĭ-, nei-\\|ni-, nei\\|nitaräm\\|nitama\" WLD_Bd1_pages.txt | head -10; echo \"=== find en- entry\"; grep -n \"^en-\\|^ en-\\|en-, n-\" WLD_Bd1_pages.txt | head -10",
 "description": "Walde-Pokorny Bd1 ni-"
}
```


### [2026-09-07T19:40:16.534Z] TOOL RESULT

```
30659:mittlung mit ni-, nei- „nieder“ s. d.
=== find en- entry
```


## [2026-09-07T19:40:20.792Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && grep -n \"nieder\" WLD_Bd1_pages.txt | grep -n \"ni\" | head -20; echo \"=== search nizdos alt\"; grep -n \"nĭzdo\\|nizdo\\|nlzdo\\|nizdas\" WLD_Bd1_pages.txt WLD_Bd2_pages.txt | head",
 "description": "WLD search nieder ni"
}
```


### [2026-09-07T19:40:20.868Z] TOOL RESULT

```
1:2249:wachsene“ aukuoju „hebe ein Kind auf und nieder       ukdvimas „Schaukeln,                            11
2:9284:   nltor aber nicht *ni-itor „mit den FuBen (z. B. auf den Boden) nieder-
3:15525:*ni- „nieder“), ghrtaci                             f.   „fettig taussehend);                         Opferl6ffel“, qvitict                  f.    „gliin-
4:17855:        ub- „d riingen. (nieder idriicken-
5:17856:           Ai.     ubjdti    ,,hiilt        nieder.         driickt          zusammen".                av.         nh)gni!c         ,,wird       nieder-
6:18127: mit m- „nieder, im Zaume halten" (Bartholomae Altiran. Wb. 1 2SS f. ver-
7:18157:lieh aucb xargcpgg „niedergesclilagen, besehamt" (eigentlich ,,die Augen
8:18158:niedergeheftet h abend" oder ,,untergekriegt‘- s. auch unten).
9:18163:schimpfenden Worten niedergedonnert"?) oder „bewegen. riihren", jebati
10:18267:                                            -ere       „(sieh dahingestreckt,           niedergeworfen haben                     =
11:21595:'percfikiu „bewaltige“, niederlit. veifcus „geschwind“, veiMus „tatig, geschitf-
12:28460:werfe   nieder" <*gi!cm aus          oder *gulcm aus *ttol- Meillot Msl.
13:28799:vom Regen niedergelegte (wie gewalzte) Getreide“. Vgl. von der i-Basis
14:29254:oder „sich zum Essen niederlassen"?).                    —
15:30659:mittlung mit ni-, nei- „nieder“ s. d.
16:32091:tayatietwa „haut ab, haut zusammen, wirft nieder", gr. y.evTsco, lett. situ,
17:32722:niederhangende Zotten“ als '*'k'->p-ron- die Deutung aus in caput prTmae
18:34912:,,sich legen“ (ursprgl. ,.sich zum Liegen niederbiicken"), sabin. cuniba „lec-
19:34985:ny-ubja- ,.niedergehalten“ usw., oder                                          fiir        danach aus lubhra- umgestaltet
20:41775:percello , -ere perculi „zu Boden sehlagen, niederschmettern
=== search nizdos alt
```


## [2026-09-07T19:40:28.909Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && python3 - <<'EOF'\nimport re\nL=open('WLD_Bd1_pages.txt',errors='replace').read().split('\\n')\ntags=[(i,int(re.match(r'\\[pdf page (\\d+)\\]',l.strip()).group(1))) for i,l in enumerate(L) if re.match(r'\\[pdf page \\d+\\]',l.strip())]\nprint(len(tags), tags[:3], tags[-3:])\n# print first line of some pages to find printed number\nfor want in [140,141,142,143]:\n    for i,p in tags:\n        if p==want:\n            print('pdf',p,'|', ' / '.join(x.strip()[:60] for x in L[i+1:i+4]))\nEOF",
 "description": "WLD Bd1 page map"
}
```


### [2026-09-07T19:40:30.435Z] TOOL RESULT

```
0 [] []
```


## [2026-09-07T19:40:34.318Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && head -5 WLD_Bd1_pages.txt; echo \"...\"; grep -c \"\" WLD_Bd1_pages.txt; python3 -c \"\nt=open('WLD_Bd1_pages.txt',errors='replace').read()\nprint('formfeeds', t.count(chr(12)))\n\"",
 "description": "WLD Bd1 format"
}
```


### [2026-09-07T19:40:35.793Z] TOOL RESULT

```
            GOVERNMENT OF INDIA
 ARCHEOLOGICAL SURVEY OF INDIA

               CENTRAL
            ARCHEOLOGICAL
...
81975
formfeeds 894
```


## [2026-09-07T19:40:40.912Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && python3 - <<'EOF'\nt=open('WLD_Bd1_pages.txt',errors='replace').read().split('\\f')\nprint(len(t))\n# find leaf containing 'ni-, nei-' cross-ref line and printed page numbers\nfor i,p in enumerate(t):\n    if 'nitaram' in p or 'nitama' in p or 'nizdos' in p or ('ni-, nei-' in p and 'nieder' in p):\n        print('LEAF',i, p[:200].replace('\\n',' | '))\nEOF",
 "description": "WLD Bd1 leaves search"
}
```


### [2026-09-07T19:40:42.196Z] TOOL RESULT

```
895
LEAF 331 ngni-s (besser egni-sl) „Feuer‘\ |    Ai. agni-h ,Feuer“,    lat. ignis, -is ds., ab. cgm, lit. ugms, altlit. ungnis, |  | lett. uguns (aus *ugns < *ngnis s. Buga KS. 1, 186). |    Die Grundform ist zweifelha
```


## [2026-09-07T19:40:50.220Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && python3 - <<'EOF'\nt=open('WLD_Bd1_pages.txt',errors='replace').read().split('\\f')\nimport re\nfor i,p in enumerate(t):\n    if re.search(r'nidar', p) and re.search(r'ni\\w*er|nidr', p) and i<300:\n        print('LEAF',i,'---')\n        print(p[:1500])\n        print()\nEOF",
 "description": "Search WLD for ni- section"
}
```


### [2026-09-07T19:40:51.524Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-07T19:40:55.505Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && python3 - <<'EOF'\nt=open('WLD_Bd1_pages.txt',errors='replace').read().split('\\f')\nimport re\nhits=[i for i,p in enumerate(t) if 'nidar' in p]\nprint(hits[:20])\nfor i in hits[:6]:\n    print('LEAF',i, t[i][:300].replace('\\n',' | '))\nEOF",
 "description": "WLD nidar leaves"
}
```


### [2026-09-07T19:40:56.848Z] TOOL RESULT

```
[382, 390, 728, 782]
LEAF 382                ,                                                                                                                                       .     -; |  |  |  |  | 374                                                                      qeu- |  |  | Suff. -to 7.o- naeh Solmsen Beitr. 1 7. oder Umbildung v
LEAF 390 382                                                                   kt'^r-.          keng-, kek-, kenk- |  |  | keg-, keng- und kek-, kenk- etwa kleiner Pflock, bes.        zum Aufhangen, |      Haken, Henkel *, Ygl. das iihnlicke kuk-, hunk-.     1 |  |  |  |  |    (Cymr. cenglu „to form into hanks      gehort woh
LEAF 728                         r |  |  |  |  | 720                                                               tem(a)- |  |  | ciqo „sehneiden, hauen, schlagen“, aruss. hint (hmefo ist Druckfehler), tjati | „schlagen a wonach auch Horn statt *tomz (= xojuog) in nsorb. ton „Aus- |                             , |  |  |  | hau“ usw. |  
LEAF 782 774                                                                 deia-, did-, dia-, di- |  |  |  | suneliai „Himmelssohne‘ , finn. |                                                       - |                                                                    Lw. tahvas „Himmel“), lett. d'levs, apr. dei- | w(a)s
```


## [2026-09-07T19:41:02.056Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && python3 - <<'EOF'\nt=open('WLD_Bd1_pages.txt',errors='replace').read().split('\\f')\nfor i in range(133,139):\n    print('#'*15,'LEAF',i)\n    print(t[i][:2600])\nEOF",
 "description": "Print WLD Bd1 printed pages 125-130"
}
```


### [2026-09-07T19:41:03.278Z] TOOL RESULT

```
############### LEAF 133
             ;                                                    )




                                               em-   en                           125

durch eine lautgesetzliche Entwicklung haben kann, s. J. Schmidt aaO.,
auch nicht mit ai. ydmati „halt“. idg. iem- zu vergleichen ist und nemt;!




letzteres darf nicht mit J, Schmidt auf ein idg.          (Praefix ut   cm-)
projiziert werden (stiitzt also auch nicht Entstehung von germ, ncman aus
niemo).    Nach Endzelin ware nemt Verquickung von nemt mit jemt, was
moglich ist jemt seinerseits ist wohl durch lit. Einfluh zu erklaren, da die
                 ;


Mehrzahl der lit. Mundarten den j-Yorschlag (jimti hat; oder Einwirkung
von russ. vz-jafa, za-njatb s-njeh (danach auch nemt direkt?i?

2.   em- „leise sprechen*??
  Eine nur nordgerm. Wz. altn. ymta „erwahnen, auBern“, norwT dial.
                                           ;                                  .



ymta „munkeln“, altn. ymtr „GemunkeP‘, norw.-dan. ymt ds. zu altn. nmi
„Gerede“, ymja „einen Laut von sich geben“; alte o-Stufe in altn. emja
(*amjon; Bed = ymja)..   S. auch umla „murmeln, leise sprechen" usw.
Dazu Falk-Torp 140S, 1580 und unten s. v. vab- „rufen“(?).

enipi- „Stechmucke, Biene“?
                                  i!
   Gr. epnig „Stechmiicke     ahd. imbi (al tester Beleg imp i piano) mlid. imbe
                                       ;


„Bienenschwarm, Bienenstock*', erst spat-mhd. „Biene“, nhd. Imnie, ah-
lautend ags. ymbe ( *umbia ) „Bienenschwarm“. Curtius 264. Bestritten von
Liden Stud. 73 f. wegen der iiltern germ. Bed. „Schwarm von Bienen“; er
vereinigt imbi, ymbe mit air. imbed acvmr. immet „Fulle, Menge“ unter einem
*embh- „Fiille, Menge“ (aber lat omnis und gr. dcpevog sind keine Stiitze
fiir eine solche Wz.); doch ware wenigstens Einmischung eines dem gr.
ijums entsprechenden Wortes kaum abweisbar (s. Kluge s. v ) und kann
nach Hirt IF. 32, 227 imbi, ymbe geradezu als Kollektiv *empi-o- „Bienen-
schwarm“ aufgefaBt werden (vgl. uotq-ov doT-yg); die Hinzufiigung von
                                                          :




piano in ahd. impi piano (auch spat mndl. noch immc van byhen „examen“)
kann nicht beweisen, daB imbi ohne Zusatz keine Beziehung gerade auf
einen Bienenschwarm gehabt hatte.
    Uber np. any „Biene“ und lat. apis „Biene“ (beide dunkel) s. noch Boi-
sacq 248, Vf. LEWb. 2 u. apis (letzteres nicht nacli Ilolthausen IF. 35, 132
zu opus van der Yelden Uber Urspr. und Ilerkunft der idg. Sprachen 1912,
         ;


43 erinnert an bask, abia „Stechfliege“).                 —
           
############### LEAF 134
126                                                                            en


d-Asyu},aorta^oyw (Solmsen KZ. 29, 97, Beitr. I 18f., Schulze KZ. 29, 264,
Lagercrantz KZ. 34, 3S4, Hermann IF. 35, 170).
      fiber das stiittige sots, evte „bis“ s. Boisacq 289 m. Lit.,                                                              Brugmann II 2 2,
                                                          4
S36,           Bgm. -Thumb GrGr.                              297,   Berneker 454.
    Alb. in „bis“                        (
                                           *eni nach G. Meyer                   AlbWb. 159).
      Lat. in, altest en; osk. en, umbr. en- (en-denda „intendito“), Postposition
osk. -en, umbr. -cm,                            -c,       adnom. mit Dat. (= Loc.), Ace. und Gen. (des Be-
reiches)
   air. i n- „in“ (adnominal m. Dat. und Acc.       nasalierend), in- (lenierend,               ;




aus *eni, ygl. ingen aus ogom. ini-gena „Tochter        vermengt mit ind- — gall.                   :!

                                                                                                         ;


undo-, s. Thurneysen Hdb. 467 f., Pedersen KG. I 45). acymr. abret. en, in
      :i
„in    corn. bret. en ncymr. (in Zs.) yn-, gall, esseda aus *en-seda, em-brekton
           ,

                               ::
      got. in „in                   ,
                                         adnom. m.            Dat., Aee., Gen., ahd. as. ags. in, anord. 7 „in“,
Adnom. m. Dat. und Acc., aus *eni (fiber Ableitungen wie got. inn „hinein“,
inna, innana, wolil aus *eni-n-, s. Brugmann IF. 33, 304 f.) apr. en „in“,
adnom. m. Dat. u. Acc., lett. ie- (nur Praefix) tiefstufig *n in lit. ? (alter                      :



und heute dial, in, Belege bei v. d. Osten-Sacken IF. 33, 218 f.) .,in“,
adnom. m. Loc. und Acc.
  Aksl. on- ( on-usta ,,Schuhwerk   n-dolb „Tar‘j raw-, n „in“, adnom. m.
                                                                      ::
                                                                           ,


Loc. und Acc., aus idg. on? oder *en ? ? Oder zu gr. dvd, idg. *aw? (siehe
Brugmann aaO. S2S).
      Ai. in          „Angesieht“ (=ao. ainika- ds.) aus *eni- 0 (ft-; *ni- in
                            dnika-         n.

ai.                       innewohnend, bestandig, eigen“, ao. ni-zonta „ein-
          ni-ja- „eingeboren,
geboren, ingenuus“, ai. ni-tya- „bestandig, eigen“ = got. nipji-s „Yerwandter“,
anord. nidr „Yerwandter“. ags. nippas pi. „Manner, Menschen“ (s. Schulze
KZ. 40, 41 Iff. 416), auch im Yer
############### LEAF 135
                                                       en    — eneu, enu                                                   127

entre    der Endvokal nach trc-, dre
            f                                                        =
                                         cymr. tnvy, Loth Ec. 17,438), acymr.
ithr „inter ahd. untar usw. „unter = zwischen“ (Behaghel Heliandsyntax 152;
                     :
                         ‘,


= oak. anter verschieden von germ. *under, ahd. usw. untar „unterhalb“
                               4

                               ,



aus *ndher, lat. infra), vgl. got. imdaurni-nuits „Zwischen-mahl“ = „Friih-
stiick“;   anord. undorn n. „Vormittag (um 9 Uhr)“, as. undorn, ags. andern
„Mittag“, ahd. untorn „Mittag, Mittagessen“ (der Bed. wegen nicht besser
zu ndher- „unter“, Osthoff MIT. 6 359 a 1, Feist GWb. 290 zw       w-Suff. wie                                  ;


in lat. interims)-, hochst. wie gr. evrega usw. anord. idrar pi. „Eingeweide“
(aus *innrar, *inperoz), innre,                             idre ,,der innere“                   (wenn diese nicht spez.
nord. -ro-Ableitungen von   inn = got. inn „hinein   s. o., sind); aksl. jqtro
                                                                                             :
                                                                                                 ‘,

                !:
„Leber (zu on-, vo- stellt sich qtroba „Eingeweide“, qtn Adv. ,,im innern".
  Eine gr. Ahl. mit -ero- ist vielleicht eveqoi „die Unterirdischen, Abge-
schiedenen“ (oder aus ev egg „in der Erde“ erwachsen? s. Bezzenberger
BB. 27., 154f., Giintert IF. 27* 49).
     *entos „(von) innen“ (vgl. ai. i-tdn „von bier", lat. caelitus usw.):
     gr. evzog „innen“, wovon evzoa-dev, - &t und weiter err oadia, ivzoo&idia  4




„Eingeweide“ (oder letztere mit aus evzoode verschlepptem & fiir *hzoozia,
                                        4
vgl. ai. antastyam „Eingeweide“, Fick I   363, Vendryes Rev. et. gr. 23,
1910, 74);
                                                             !
     lat.       intus „von drinnen;    (aber intestlnus nicht mit Suffixablaut
                                                 innen           ‘




zu         sondern aus *enter[o\-sto~, Brugmann IF. 28, 295);
      -tos-,
   Etwas unsicher, da eine Tiefstufe -ts- oder ~te i- des Adverbialformans
-tos voraussetzend, ist die Zuriickfuhrung von mnd. nhd. mdartl. inscr „eB-
bare innere Teile von Tieren“, anord. Istr n., istra f., ,,das die Eingeweide
umgebende Fett“ (apr. instran „Schmer‘ wohl 
############### LEAF 136
128                                eneuen, neun, enug            — enek-, nek-, enk-, nk-

mit       lat.    sine usw. (vgl. Yf. LEWb. s. v.)                          mag bestehen, docb keineswegs
sicber (Prellwitz 40).
        Ygl. Boisacq      6 f., Prellwitz 40, Horton Smith BB. 22,
                                   1                                                                  189ff.            Auch
Prellwitz           BB. 22, 78, Vf. LEWb. 2 715, Fick III * 25.

eneuen, neun, ennn „neun“.
  Ai. nova, av. nara „9“: arm. inn „9“               pi. in(n)unH (Hiibsch-

mann Arm. St. I 31, Arm. Gr. I 450f.), gr. *evj:a- in hom. elva-exeg -vv%eg.                                      ,


boot. sva-yg-dey.dxg,                        jon. slva-y.oaioi ,     att.   iva-y.ooioi,       ord. eivaxog   ,
                                                                                                                      att. aol.

e'vaxog, woneben noch nicht geklartes errefpja, und wohl h’fsv- in evev-
•gy.ovxa (Lit. zu don gr. Formen bei Boisacq 252, 254 f., 1109); alb. nsnde
„9“ (* neunti „Anzahl von neun“, wie si. dcvqtb „9“, anord. niund „Yeun-
zahl“ und ai. navatl-, av. navaiti- f. „90“, eigentbch Neunzahl von Zehnern;
G. Meyer Alb. St. II 66f., Alb. Wb. 304); lat. novem „9“ (-m lautgesetzlich
aus -n ? sonst nach septem, decern)-, air. noi n-, cymr. corn, naw, bret. nao
(zum a s. Pokorny IF. 38, 190f ); got. ahd. niun, anord. nio „9“, as. nigun,
                             (zum g dieser und der Ordinalia s. die Lit. bei
afries. ni(ti)gtm. ags. nit,on
Brugmann II 2 2, 20);                lett. devini («- noch im Ordinale apr.
                                               lit.   devyn\,
ilewTnts), aksl. dev eh „9“ (d- wohl durch Diss. gegen das ausl. n und durch
EinfluB der 10 festgeworden. Lit. bei Berneker 189).
    Ordinale; *noueno- in lat. nontts mit nach der 7 und 10 eingefiihrtem
                                                                 ,


in statt n umbr. niivime „nonum“, ai. navamd -, av. naoinci-; ap. navama -,

air. nomad cymr. nawfed (um -to- erweitert); -A)-Bildung gr. el'varog, evaxog
                     ,


               got. niunda, ahd. niunlo, anord. nionde     as. nigundo nigudo,
    :




( *enim-to -),                                                                             ,                      ,

afries. niugunda, ags. niyjda (s. o.), lit. devintas, apr. neivlnts, aksl. devqfo.
    Man vermutet Zusammenliang mit *neuo- „neu“, weil mit 9 ein neuer
 Ziihlabschnitt              begonnen habe, indem                      d
############### LEAF 137
yvexys „einen Speerwurf weit“                                =
                                   „soweit man mit einem geschleuderten
Speere   reicht“   oder  pass. „vom   Speer erreicht“,     wie y.evxQgvEy.gg
„vom Stachel ferreicht =) angetrieben“ (z. B. Boisacq 251, Bechtel
Lexil. 104), pass. aor. gveydgv „wurde getragen“, Pf. xax-yvoxa Hes        ev-                                                                 ,

                                                                             2
yvoya (ev- ist darin trotz xar-yvoxa kaum die Praep. ev, Brugmann II
3, 461, sondern wohl Reduplikation    ebenso im    Med.  iv-ijvey/uai, zu
                                                                        ;
                                                                          dem
sich  als 3. sg. ev-yveyaxai statt  *ev-rjvey.xai gesellte nach dem Aor.

eveyy.eTv);         *enk- im red. Aor. ev-eyy.-eiv „tragen“, *onk- in oyxog „Tracht.
Last“.
      tjveiy.a     dagegen Praep. ev + Wz. *seik- „langen“,                s. d. und Boisacq 251 f.

m. Lit,,          Brugmann II 2 3, 92             ;
                                                       durch Ivreuzung mit ihm wurde yveyxov zu
tfveyy.a,         rjveiyxa   ;




       nactus (und nanctus ) sum, nancisci (arch, auch nancio, -ire) „erlangen“
      lat.

(-a- = e s. Giintert Abl. 53, so dafi nactus = germ. nuJi-ta-; die Kasalierung
              ,




des Praes. hat trotz Brugmann IF. 12, 157 Anm. 1 keine Beziehung zur
Wzf, *enk -); air. ro-icc .,erreicht“, do-ice ,,kommt“, air-icc- „finden“, con -
icc- „konnen“ usw., Formenbestand bei Pedersen KG. II 552 ff.           zur Er-                                                       ;



klarung des Vokalismus s. Pokorny IF. 35, 339: in die themat. Konjugation
ubergefuhrtes dehnstufiges *euk-ti, woraus *lnk~, *Tnc-, icc- Yerbalnomina                                               ;



tlchtu, nchtu; s-Konj. -J aus *cnkst    Schwundstufe nk- in cymr. di-anc „ent-
                                                                    ;


fliehen“, cy franc ( *kom-pr\o]nko-) = air. comracc „Zusammentreffen“        fiir                                                              ;



anderes bei Fick II * 31 angereihte vgl. man Pedersen passim (ir. oc,
cymr. icnc, wng „bei“ aus *onko- „erreichend“?)                                                   :
                                                                                                      gall.      Selvanedes „qui ont
obtenu propriety? 11 (Yendryes Msl. 13, 394).
      Got. ganah       
############### LEAF 138
130                enedh-, endh-               — (enebh-) ombh-, nObh- (nebh-?), mbh
                                                               a
enedh-, eudh- „gehn, liervorkommen                                 .




  gr. av-yvo dev, ev-yvo&e „kommt (kam) hervor,                                      steigt        empor, sprudelt
empor“ (at/ua, y.vlaij; Horn.) ensv-rjvo'de {fkayyrj eigentlich „hervorgekommen
sein“ = „sich worauf befinden“; e laiov „sich worfiber verbreiten“ Horn.),
ep. y.aTev-tjvode        (   y.ovig , xo/nat, ,.herabfluten“),                  nagev-yvode („sich nahern“)
vielleicht    dor.-kret.-arkad.                      fjvOov,   ptc.      ev&cbv,    „kam‘ (att. lldelv wohl
                                                                                               :




daraus durch Kreuzung mit ij/.v()or von elev&co, wahrend Schulze Festschr.
f. Jagie 343   Anm. L [Zitat nach Jacobsohn KZ. 43, 170] el&eTv aus ek-dveTv
durch lautliche Aufsaugung des v durchs dunkle 2 erklaren will; fiber
andere Auffassungen von h’fttiv s. Prellwitz BB. 23, 75, Boisacq 242, Brug-
mann-Thumb GrGr. 4 95, 344 nicht iiberzeugend fiber avrjvode Prellwitz 2 40);
                                                 ;



   pali andhati ,.geht“; mit Tiefstufe *ndh- wahrscheinlich hierher ai adhvan-                            .



m. = av. advent- m. „Weg, Pfad, Bahn“, wozu vielleicht              mit r- neben                   —
M-Suffix     —
             ai. adhvard-h „religiose Handlung, lieiliger Dienst“ (ursprgl. „Gang

— feierlicher Gang — Feier“, vgl. dt. „begebn“ von gottesdienstlichen Feiern)
     qnchtrr m. „eine Art Schneeschuh“ (* ndhuro - mit Suffixablaut gegen-
     isl.

fiberadhvava- aus *ndhueru-; nicht wahrscheinlicher dachte Falk-Torp 5f.
an Bezieliung zu germ, mid „entgegen“ als „was entgegengesetzt wird,
was den StoB auffangen soll“) Johansson IF. 3, 203 ff. und S, IS Iff.

1.    (euebli-)    ombh-, nobli- (nebh-?), mbh- „Nabel                                -
                                                                                          ‘,   mehrfach mit Z-For-
        mantien.
      As. ndbliya- n. „Nabe“, nabhi- f. „Nabel, Nabe, Yerwandtschaft“, nablnla- n.
funbelegt)  ,,Schamgegend, Nabelvertiefung“ av. uabd-nazdista- „der ver-    ;



wandtschaftlich naehststehende“,  daneben mit ar. ph av. nufa-, np. naf
„Nabel“; gr. o/uipcdog „Nabel, Schildbuckel“, wohl auch opcpay.e? „die un-
reifen Weinbeeren oder Oliven oder andere Frfichte“ (als nabelartig vor-
gesttilpte Ivnopfchen), buwaxk „der Kelch der Eichel“ (deren Yergleic
```


## [2026-09-07T19:41:10.599Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && python3 - <<'EOF'\nt=open('WLD_Bd1_pages.txt',errors='replace').read().split('\\f')\nprint(t[134][1400:5000])\nEOF",
 "description": "Rest of WLD Bd1 p.126"
}
```


### [2026-09-07T19:41:11.879Z] TOOL RESULT

```
                                   adnom. m.            Dat., Aee., Gen., ahd. as. ags. in, anord. 7 „in“,
Adnom. m. Dat. und Acc., aus *eni (fiber Ableitungen wie got. inn „hinein“,
inna, innana, wolil aus *eni-n-, s. Brugmann IF. 33, 304 f.) apr. en „in“,
adnom. m. Dat. u. Acc., lett. ie- (nur Praefix) tiefstufig *n in lit. ? (alter                      :



und heute dial, in, Belege bei v. d. Osten-Sacken IF. 33, 218 f.) .,in“,
adnom. m. Loc. und Acc.
  Aksl. on- ( on-usta ,,Schuhwerk   n-dolb „Tar‘j raw-, n „in“, adnom. m.
                                                                      ::
                                                                           ,


Loc. und Acc., aus idg. on? oder *en ? ? Oder zu gr. dvd, idg. *aw? (siehe
Brugmann aaO. S2S).
      Ai. in          „Angesieht“ (=ao. ainika- ds.) aus *eni- 0 (ft-; *ni- in
                            dnika-         n.

ai.                       innewohnend, bestandig, eigen“, ao. ni-zonta „ein-
          ni-ja- „eingeboren,
geboren, ingenuus“, ai. ni-tya- „bestandig, eigen“ = got. nipji-s „Yerwandter“,
anord. nidr „Yerwandter“. ags. nippas pi. „Manner, Menschen“ (s. Schulze
KZ. 40, 41 Iff. 416), auch im Yerbalpraef. ar. ni- „hinein ‘, z. B. ar. nlgam-,                                            l




                                          u
ao. nigam- „in einen Zustand gelangen       (Brugmann II 2 2, 828,861).

      (
          e)nero           arm. *nero- „das Innere“, vorausgesetzt von ner-
                               „innerlich“            :




„intra, hinein“, nerks „innen“, nerkoy „drinnen“ (Brugmann II 2 2, 696, 698,
707 i; vielleicht gr. evegoi als „die drinnen, niimlich in der Erde“ (Sonne
KZ. 14, II, Gtintert IF. 27, 49; priignanter nimmt Bezzenberger BB. 27,
154 f. Hapostare aus ol iv eog an).

      enter nter „zwischen — hinein“, en-tero-
                        ,
                                                                                                         ,,innerlich“
      ai.                      antar ^zwischen ', adnom. mit Loc. Instr. Acc.
                   antar, uv. antara, ap.                                                   1



                                                                                                                  1
Gen.; ai. antara- „innerlich“, a w. antar a- ^innerer ', Sup. ai. dntama- „ der
nachste“ (trotz Fick I 4 to, 263 nicht zu anti anta -), av. antama- „der.                                ,

innerste, vertrauteste, intimus“; ai. antra-, auch mit Yrddhi antra- n. „Ein-
geweide“, arm. mder-k PI. „Eingeweide“ (gr. Lw.? s. Hiibschmann Arm.
Gr. I 447f.);
                                                                                                                                                 Ll
      gr. tvTEQOv,                      meist PI. „Eingeweide“ (fiber urtaov s. aber u. an- „hauchen                                                  ;



alb.           nder ,,zwischen, in“ (wolil nicht                                    lat.   Lw.,              s.       Pedersen Rom. Iber. 9,
213            ,
                   ferner (JokI SBWienAk. 168, I 59) ndjer, ntjer, nyera, ner, per „bis l<
{*entcro -); lat. enter, inter „zwischen'‘,                                          adnom. m. Acc.                            (orstarrte   m. Gen.
interivia-s, interdiiis ,                         intro, intra, intrin-secus , interns                                   „innerlich“, interior,
intimus             ,
                            intesinus (s. u.), osk. entrai ,,*Interae“, tiefstufig '
```


## [2026-09-07T19:41:21.982Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && python3 - <<'EOF'\nt=open('WLD_Bd2_pages.txt',errors='replace').read().split('\\f')\nprint(len(t))\nimport re\n# find offset: search a leaf with printed page number\nfor i,p in enumerate(t):\n    if 'nitaram' in p or 'nitama' in p or ('nei-' in p and 'nieder' in p and 'nidar' in p):\n        print('HIT leaf',i)\nfor i in range(340,360):\n    head=t[i][:120].replace('\\n',' | ')\n    print(i,head)\nEOF",
 "description": "WLD Bd2 locate ni- lemma"
}
```


### [2026-09-07T19:41:23.326Z] TOOL RESULT

```
725
HIT leaf 339
340 336                                                 nit    no- |  |  |  | niJiol„pronus“ aus "^niwol, mnd. nigel „niedrig^‘ (weg
341 Hip- neben                Jcio-     neben               evioi „einige‘‘ (s. Brugniami IP. 28, 355 f.); |  | umbr. enom      
342 33a                                                  &oqt^ |  |  |    Gr. vvi, vvxros „Nacht“ in Zs. wxti~, wxxo (dafl v fiir 
343                                  :                                     :                                                
344 340                                         nog^o- Oder uag^o-   — nu- |  | 483 ala s-Pormen mit anguis usw. verbunden) s. z
345                                                                              ; |  |  |  |  |                                      
346 342                                           ras-   —   re(i)-, rei- |  |  |  |  | ras- „ert6iien,         sclireieii“. |  |    Ai. r
347                                                       re(i)     rei-                                                   3
348 344                                                   rei- |  |  |  | schreiben"       Sommer Hdb.^ 231, Boisacq 274 Anm. 5), is
349                                                   rei-                                                345 |  |       reip-  
350                                ^ |  |  |  |  | 346                                        rei-, roi-   —   reiq- |  |  |  |            ris
351                                     reig-   —   (reig-), reig-                                 347 |  |  | ling“, nnd, auch ru
352 348                                      reid-   — reidh- | auch verwandt       air.   riag „Tortur‘‘, ringid jjfoltert, p
353                                                                                        ; |  |  |  |  |                            
354 350                                          reu-, reu-, ru- |  |  |  | Interjektion w sein, oder nach Brugmann, z. B. 11^ 2, 81
355                                                                                                           ; |  |  |  |  |         
356                                                                                  ; |  |  |  |  | 352                              
357                                                 reu-                                        353 |  |                 -a- zur
358                                                                                            ^   ; |  |  |  |  | 354                
359                                              reu-                                      355 |  | (*abgerissene) Ernte eines F
```


## [2026-09-07T19:41:27.429Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && python3 - <<'EOF'\nt=open('WLD_Bd2_pages.txt',errors='replace').read().split('\\f')\nprint('#### leaf 338'); print(t[338][:1500])\nprint('#### leaf 339'); print(t[339][:3000])\nEOF",
 "description": "WLD Bd2 p.335 ni-, nei-"
}
```


### [2026-09-07T19:41:28.858Z] TOOL RESULT

```
#### leaf 338
334                                    ner-'   —   nes-



Aufrec&t-Kirchhoff II 102, 219)   tiefstufig aftord. yiordr n. „Norden« ags.
                                   ;


norSerra ^inehr nordlich^*, ahd. 'nordroni „nordlich“ (Norden ist bei der
Kichtung des Betenden nach Osten = Links, Bugge BB. 3, 1 05, Brugmann
IF. 11, 274; 13, 163, Bezzenberger BB. 27, 155 a 1, Ostboff MU. VI 174,
Falk-Torp \i,nord)\ arm. nerJcin „unterer‘' (Meillet Msl. 10, 275).
  tJber mogliche Verwandtschaft von n-er mit *n-€i „nieder“ s d.
   Gegen Anreihung von germ. Nerthus „terra mater“ = anord, Njordr
(Horeen Ltl. 209) s. Tick III ^ 295.    Unsicher ist Zugehorigkeit von ai.
ndrdka- m. „Unterwelt, Holle“ (z. B. Uhlenbeck Ai. Wb. 143 zw.; von Persson
Beitr. 222 zu ner~ „eindringen“ gestellt, was im letzten Grunde auf das
gleiche hinausliefe, wenn letzteres mit ncr~ „unten‘‘ zshinge).


, nor- „eindringen, untertauchen, Versteck, H6hle‘‘.
     Gesichert nur furs Balt.-Slav.:   lit.    neriu, nerti „untertauchen, einschlupfen“,
           sinerti „in die Schuhe hineinschlupfen“ (ahnlich apr. nurtue „Hemd“,
I Jcurpesl
vgl. zur Bildung lit. atihivas „Schuh“: auti „Schuhe anziehen“, Trautmann
Apr. 387), lit. ndras „Tauclierente“,     uznarve „Yersteck“ narva „ZelIe der
Bienenkonigin“, nartas „Ecke, Winkek", lett. nirt^ nirddt „untertauchen“
(zur Scheidung von lit. nerti „einfadeln, einschlangen“ usw. s. u. sner- „drehen“),
abg. mra^ nreti „eindringen“, sloven. pondrHi „untertauchen“, klr. ponerfy
„t
#### leaf 339
                                               m, nei-                              335

des - 0- nach mit ai. nimsate vergleichharen unthem. Formen wie 2. 3. sg.
^vi-va^cai, -raif oder aus '^vt-vo'-ioixar, s. Brugmann BSGW. 1897, 196 Anm. 1,
Grdr.      3, 106)   reduktionsstufig (s. zuletzt Guntert Abl. 44,76 gegen
                       ;


Kretscliiners Gl. 3, 337 Abtrennungsversuch) ratco, fut. vdooojuac „wohnen,
sich befinden;  bewohnen, bewohnbar machen; ansiedeln“, vaierdco „wohTie;
bewohne    ;
            bewohnt sein“, *vao-j^6g dor. thess. vdog, lak. vdfogy lesb. vavog,
(d. L raffog), jon. vr]6g, att. vEcog „(G6tterwohnuDg =) Tempel, Heiligtum“;
schwundstufig dojuEvog „gerettet, geborgen'* (s. dazu u. sfjdd- ,j8u6‘‘); air.
ftiinim „gehe unter      (von der SonDe)“ (*7W-n€sd yyVJzo-vEEG&ai*' Tick II ^
194, Pedersen KG, II 526); sAh.Jcmtem „erhole mich, werde wieder leben-
dig“ (Praefix Jc-    ^nes^lo-; Jokl SBAk. Wien 168, 1 40); got. ganisan „ge-
nesen‘‘, ahd. as. ginesan „genesen, gerettet werden, am Leben bleiben“, ags.
genesan „gerettet werden, entkommen, iiberleben", got. ganists, ahd. as.
ginist „Genesung, HeiP; kans. got. nasjan „gesund machen“, ahd. nerimi,
nerrm „am Leben erhalten, retten, schutzen, ernahren” (nhd. ndhren) as.
nerian „retten“, ags. nerian „retten, schutzen“ (daneben mit e, d aisl. ncera
nnd fipra „beleben, erfnschen, emahren^, norw. nere, schwed. mdartl. nora
„Feueranmachen“) ; aisl. nara „Leben‘‘, aldr-nari m. „(Leben8erhalter =)
Feuer“, as. Uf-nara f. „Nahrimg“, ags. ealdor-ntru f. „Lebenserrettung“, ahd.
nara „Heil, Rettung, Nahrung“; letztere Bed. auch in ahd. wega-nest,
-nist n. „Reisekost‘', ags. 7i€St n. „Nahrungsmittel“, aisl. nest n. „Wegzehrung,
Eeisekost".
   Ygl. Curtins^ 314 f., Falk-Torp u. niste, ncere, ndre, Pick III ^ 296, Me-
ringer WS. I 168ff., IF. 18, 269f.; 21, 302f.; der Beigeschmack der Riick-
kehr ins schiitzende Haus rechtfertigt durchaus nicht Meringers Annahme,
daB „Hau8, Holzbau“ das ursprungliche und got. ans „Balken“ unter einer
zweisilbigen Wz. enes- damit zu vereinigen sei.


ni,   nei- „nieder“,       Komp. nitaro^ „nieder“          (im Gegensatz zu „oberer“)‘
  Ai. ni, av.    7ii   „nieder(warts)‘^,   ai.   nitaram jjUnterwarts^, av, nitama- „der
unterste^^*; arm. ni~, w- jjnieder*'; ahd. nidar, as. nithar, ags. niper, aisl.
nidr „niederwarts‘' (und Zubehor, s. J. Schmidt KZ. 26,31, Falk-Torp u.
ned), ahd. nidana, as. nitkana „unten“, ags. neodan, nipan „herunter, unter"',
aisl. nedana „Yon unten her“, Praep. mit Acc. „unterhalb"", as. niiTie Adv.

„imten"^ ahd. nida Praep. mit Dat. und Acc. ,,unterhalb, unter“; abg. niz-o
„hinab, hinunter“ (Bildung wie       usw.).
                                      +
   Ai.nipa- „tiefliegend“ (m ap- „Wa8ser""); nlca- „niedrig" (trotz nyanc-
„nach unten gerichtet“ vielleicht erst nachtraglich nach pratic^ praty-anc- :



mit dieser Hochstufe ausgestattet und dann als *ni-oq^6-s „niederblickend,
nach unten schauend“ deutbar, vgl.:) abg. nkh
```


## [2026-09-07T19:41:43.056Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== IEC nizdos\"; grep -n \"nizdo\\|nizd\" IEC.txt | head -5; echo \"=== SYN nest\"; grep -n \"nīzdo\\|nizdo\\|\\*ni-\" SYN.txt | head -8; echo \"=== NYB\"; grep -n \"nimūtan\\|nimutan\\|nihātan\\|nihatan\\|nikās\\|niyāz\\|nigūn\" NYB_vol2_glossary.txt | head -10",
 "description": "Mann, Buck, Nyberg"
}
```


### [2026-09-07T19:41:43.149Z] TOOL RESULT

```
=== IEC nizdos
11761:nisdos (nizdos) “seat, nest’. WP II, 485 Skt. nidáh, am. m. n. ‘abode, nest; Arm. nist, gs nsti, i-st. ‘seat’; Lat. nidus, gs -i, m. ‘nest; Mir net, n., Ir. nead, gs: nid, mf, id.; Br. neiz, pl: neisiu, m. id.; W nyth, pl: -au, -0d, f. id.; Cor. nyth, pl. -ow, m. id.; OHG, OE, Du. nest, n. id.; Sw. näste, id. (The ini- tial of Li. lizdas, Latv. lizds, m. id. unex- plained)
=== SYN nest
3699:4. Goth. (ga)nipjos, ON nidjar (OF mippas ‘men’), prob. : Skt. nitya- ‘in- nate, one’s own’, deriv. of an IE *ni- beside *eni- ‘in’. Formerly derived fr. *neptio- in Av. naptya- ‘descendant’, Grk. daveyids ‘cousin’ beside Skt. napat- ‘grandson’, etc. (2.48). Walde-P. 1.126. Feist 376 f.
13184:wok pase that is, *o-zd-o-s with Test’, and tik Sed- ‘sit’, like *ni-zd-o-s ence ty bir ue used orig. with ref- on, Perch’, » Damely, as ‘lace to wit
19283:Pol. (z)niszczyé, fr. nizki ‘low’ : ChSI. nistt ‘poor’, nizti ‘down’, fr. *ni- ‘down’ (cf. above, 5). Briickner 364.
21804:OE niberlic, fr. niber adv. ‘down, be- neath, below’ = OHG nidar, NHG nie- der adv. ‘down’, whence adj. OHG nidari, MHG nider(e), NHG (nieder) niedrig (Du. nederig ‘lowly, humble’) : Skt. nitaram ‘downwards’, comparative formation to IE *ni-, *nei- in Skt. n7-, Ay. ni- ‘down’, Av. nitama- ‘lowest’, ChSI. nizti ‘down’, etc. Walde-P. 2.335. Weigand-H. 2.297 f.
=== NYB
1205:dast [YDH, Prth YD’; dst'], with the indef. art. dast-ē [YDH + 1] 1. hand HajA:11.14. B:12.16. 9% and passim; power 1924, 24%. 304; — ~~ apar nihātan to put one's hand to 6215; — ~ avis burtan to deal with a th. 8119-29; — frac ~ Sustan to wash one’s hands 443-9, with hac to dissociate oneself from, to break off all relations with 384; — a ~ 4... rasitan to come to close quarters with a p. 24?, — pat ~ daštan to have a hold on, to hold sway over 87%, — 2. ~ i yāmak a set of clothes 2; FrP 29. — 3. game: 3 ~ hae ... burt he won three games (of chess) against... 11915; ~ 4 vat vāzītan
1878:handäcak [hnd’ck'] measure; ~ nimūtan to measure 1109. — From handāxtan (g. v.); NP andäzah; Talm. lw. hndz? ‘calcu- lation’; Syr. lw. handäzä ‘that. which is measured'.
4914:magu-: magū manā: man martiya-: mart Margu-: Marv ni-māy-: nimūtan mayūxa-: mēx mudräya-: muzräyik
```


## [2026-09-07T19:41:52.941Z] TOOL CALL #77: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"nimūtan\\|nimūt\" NYB_vol2_glossary.txt | head -5; echo \"=== nihātan\"; grep -n \"nihātan \\[\" NYB_vol2_glossary.txt | head -3; echo \"=== nikās/nigāh\"; grep -n \"nikās\\|nikāsīh\\|niyōxš\\|niyōšī\" NYB_vol2_glossary.txt | head -5; echo \"=== nišastan\"; grep -n \"nišastan \\[\" NYB_vol2_glossary.txt | head -3",
 "description": "Nyberg entries"
}
```


### [2026-09-07T19:41:53.037Z] TOOL RESULT

```
1878:handäcak [hnd’ck'] measure; ~ nimūtan to measure 1109. — From handāxtan (g. v.); NP andäzah; Talm. lw. hndz? ‘calcu- lation’; Syr. lw. handäzä ‘that. which is measured'.
2739:nimūtārēh abstr. v. n. of the preceding vb.: indication, act of establishing 45%; manifestation 71°; teaching 11220,
3258:rast [Pst'] right, righteous, true, fair; subst. the truth; epithet of Rašn (q. v.); vimand ~ nimūt indicated the boundary justly 4510-11; the balance ~ dārēt gives the accurate weight 7274; kē-š kirpak u vinds hakanén ~ whose virtue and sin weigh equally 79%; han ké-§ har 2 ~ are equal 937°, — MPrth rst (S, A-H III); MPrs r’st (A-H II, BBB); Ps. Psty; Paz. NP räst; Verbum 187; Ghilain 69.
4914:magu-: magū manā: man martiya-: mart Margu-: Marv ni-māy-: nimūtan mayūxa-: mēx mudräya-: muzräyik
=== nihātan
=== nikās/nigāh
=== nišastan
2763:nišastan [YTYBWN-stn', seldom nšstn'] nšin- to sit, to dwell, to reside, to seat oneself, to be seated; to be situated 4716; 6 asp ~ 434; api-§ andar o [KN] nisinet and he will reside in it 348; apar ~ to mount on horseback 261%; apar bärak i Zarer nišīnēt mounts the steed of Z. 295; hac asp bē ~ to dismount 272; bē ~ to make a halt 141%, to cease 2024-25, 2522, 6817-18, — Av. (1754) ni-šad- < ni-had- = OP (caus. ni-Sädaya-); Ps. nšstny nšyd- (for nišiy-); MPrth. nšstn nšyl- (!); MPrs nšstn nšyy-; but Paz. NP nišastan nišin-. Ghilain 50; Verbum 169.
```


## [2026-09-07T19:42:05.566Z] TOOL CALL #78: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && grep -n \"نوردیدن\" BQT_v4_pages.txt | head -6; echo \"=== nigun\"; grep -n \"نگون\" BQT_v4_pages.txt | head -6; echo \"=== niyaz\"; grep -n \"نیاز\" BQT_v4_pages.txt | head -4; echo \"=== niyam\"; grep -n \"نیام\" BQT_v4_pages.txt | head -4",
 "description": "BQT v4 more headwords"
}
```


### [2026-09-07T19:42:05.686Z] TOOL RESULT

```
10795:درچیزی افتد 8 - ونام افزاری است‌جولاهگایر۱ | مخفف نوردیدن است که بمعنی پیچیدن و طقی
10805:۴ * نرد (رك : نردبان ) ورك : نوردیدن . نی شروانی ص ۳۸۷
10817:*- همان معتی اول است. ۹۱ اسم فاعل مرخم . رك : نوردیدن .
10818:۴ ر4 : نوردیدن + ۴۳ با اول مضموم و واو مجپول و. رای موقوف, نام شهر
10819:کازرون کهنه است . «جپانگیری» ورك : رشیدی . ۱۴ * نوردیدن (۸.م.) ۷8 * نورد(ه.م.)
=== nigun
2199:۱ - چو رستم ورا دید زانگونه یز برآشفت زاسان که بور از مخیز .
6964:۱ - دل ناداشت پر زخون باشد ساغر عیش او انگون باشد .
9871:نگون - یک اول بروزن حون * | رسیده وسین بی قطه بالف کشیده ‏ دام بان
9876:نگون‌طشت ۴ - بفتم طای خطی نداشته وسرود خسروالی ازوست .38
9890:۴ - در رشیدی « نگون‌نشت >. ۴ - باین معنی « نگهدار» متعمل است :
9901:0 نگونی‌سار - از : نگون (۸م) ۲ سار (* سر ) رك : دارمتتر . تقبعات ج ۱ص
=== niyaz
3542:است دوائی و بوی خوشی دارد و در غابت تلخی | و محتاج ونیازمند - و کله‌مند وشکوه‌ناك را نیز
10339:فرهنکه نظام نویسد : « مشهور درشعر مذ کورنیازاده است بجای نوا زاده » ومعنی مصرع‌این‌است
11672:نو‌نیاز» با تستای بالف کدیده بروزن | وبضم اول » نیز بان معتی آمده است . و بفتح
12253:نیاز ۴ « بکراول بروزن‌حجاز,حاجت بود ؛ وهيچيك شاهد دامتند ۸ .
=== niyam
80:ج‌- افزودن لغات ی که لازم بنظر مرسیده ودرمتن برهان نیامده .
169:لغات فارسی و اعلام #رستاده‌|ند که در برهان نیامده . از اظهار نظر آقایان
317:درفهرست مآغذ مندرج درپایان سه مجلد قبل نیامده . اينك اسم آنهارا
501:۴ - در فپرست ولف نیامده . ۴ -ظ . مسحف «خاقان (چین)» .
```


## [2026-09-07T19:42:10.668Z] TOOL CALL #79: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && python3 - <<'EOF'\nimport re\nL=open('BQT_v4_pages.txt',errors='replace').read().split('\\n')\ndef tag(n):\n    for i in range(n,0,-1):\n        m=re.match(r'\\[pdf page (\\d+)\\]', L[i].strip())\n        if m: return int(m.group(1))\nfor t in [9871,10795,12253]:\n    p=tag(t); print(t,'pdf',p,'printed',p+1917)\n# print negun footnote region\nprint('---- negun page')\nprint('\\n'.join(L[9871:9905]))\nEOF",
 "description": "BQT negun page and footnotes"
}
```


### [2026-09-07T19:42:12.348Z] TOOL RESULT

```
9871 pdf 248 printed 2165
10795 pdf 269 printed 2186
12253 pdf 305 printed 2222
---- negun page

بممنی خم شده وکوز ‎)٩(‏ وسر در زبر افکنده ۱ ۲2 وسین بی ۹۹۳ + 7 ی

باشد ‎٩‏ : خسرو پرویز بوده و اوتیزمانند بارید عدیل ونظینر
نگون‌طشت ۴ - بفتم طای خطی نداشته وسرود خسروالی ازوست .38

(۱) خم۱ :کوژ ۰

۱ مخفف «نکون‌سار» (۸.م.) رك : نذ کرقالاولیاه چاپ اروپا جچ۱ص۱*۵ی۲۲.

۴ - پپلوی ۵16۵۵ . ارمنی ع 8۴۷0 . از : ۴۵-88 - 081 از 8۳2۷ ( در 5۳8
-- ۰ - 202-68۷8 . 112-۳۵۷28 ( ر4: كلمةٌ اخیر در لیب رک ص۷۱) «نیب رکس
۹ و رك : هویشمان ص ۰۱*۲

چوآمد بنزديك آن ژرف چاه بكايك دگون شد سربخت شاه .

فردوسی طوسی « شاهنامةٌ بخ ج۱ اص ۳۰ *.

۴ - در رشیدی « نگون‌نشت >. ۴ - باین معنی « نگهدار» متعمل است :

تن و جات یزدان نگهدار باد ! دلت شادمان بخت بیدار باد !

فردوسی طوسی« شاهنامةٌ بخ ج ۰4۱۳۱۱

* نکیا. کرستنن‌نوشته «ابران. ساسان. ترجمه, چاپ‌دوم ص0۰۸ح۱> : «اختراع
«خسروانی»رابه نگ ا 1۷810182 که بکی‌دیگر ازرامشگران‌عهد خسروپرویزاست. ونظامی کنجوی
وخواجه سلمان وبعنی‌لوسند کان دیگر ذ کری ازاو کرده‌اند , نسبت داده‌اند . رل: برهان‌قاطم»:
نوای پارید » لحن نکیا جبین زهره راکرده زمین‌سا. نظامی کنجوی « کنجینه ۰۱۵۸

0 نگونی‌سار - از : نگون (۸م) ۲ سار (* سر ) رك : دارمتتر . تقبعات ج ۱ص
۵ » پهلوی ۲ - 818۳206 ۵« نیب ر که صس ۸-۱۵۷ ۰ نگوسار (۸.م.) ؛ سرنگون :

یکی ایزه انداخت برپشت اوی نگودار شد خنجر از مشت اوی.
فردوسی طوسی « شاهنامة بخ ج ۱ص ۰۹۱۱۳
```


## [2026-09-07T19:42:22.071Z] TOOL CALL #80: Bash

```json
{
 "command": "python3 tools/ref_page.py BQT:2165 --image 2>&1 | tail -20",
 "description": "Render BQT page 2165 image"
}
```


### [2026-09-07T19:42:30.203Z] TOOL RESULT

```
نوای باربد » لخن نکیسا ‏ جبین زهره راکرده زمین‌سا. نظامی کنجوی« کنجینه ۰4۱۵۸

0 نگون‌سار - از : نگون (۸«م) + سار (* سر ) رك : دارمستتر . تتبعات جح ۱ص
۵ » پهلوی 52۴ - 8180886 ۵ نیب ر که ص ۸-۱۵۷ > نگوبار (۸.م.) ؛ سرنگون :

یکی نیزه انداخت برپشت اوی نگودار شد خنج از مشت اوی.
فردوسی طوسی « شاهنامة ۱ ۱۱۳ ۰
۵ ین - بفتح اول ,کوهر وسنگه قیمتی که برانگشتری با زبور دیگر کار گذارند :
نگین توبی وچوانگشتری است ملك جهان بها وقیمت انگشتری بود ز لگین .
۶ معزی لیشاپوری *۹۸ ۴ ۰
بفه ازحاشيهٌ صفحهٌ ۲۱۹۶
( اسفهانی ) که این روایت نالی ا زکتاب وی ترجمه شده است درین موردكلمهٌ « دفن > آورده و
گوید: « فدفنت بعد خروج القرمطی » (ص۱۳4) ولی پیداست که کسته را هم کشتةٌ که چندروز
مانده وبسرارهم باشد. نمی‌توان برطیق‌آیین دفن کرد وموّلف نیزبنا برهمین نکته دراین‌مورد لت
« دفن » را به « نگندن » ترجمه کرده است وبنظرحقیربابستی این لغت باکاقف فارسی باشدچنانکه
برهان گفته‌است, ولغت خوبی است» (پایان)*دفن» اعم از کور کردن طبقآبین باچاله کردن است,
بنابرین در هن « دفینه » درست است وظ . « دفه » و «دفتینه» مصحف آنت . اما « نگندن »
بنظر میرصد مرکب باشد از : ۱( پیشوند فعل )1888 (کندن ) قس : انگرستن و انگریدن
(ازجهت پیشوندفعل وتبدبل کاف به کاف ) و قس : فکندن وافکندن ( ازجهت ریشه ).
```


## [2026-09-07T19:42:37.935Z] TOOL CALL #81: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==153' HUB.txt | head -60",
 "description": "Hübschmann p.142"
}
```


### [2026-09-07T19:42:39.100Z] TOOL RESULT

```
— 142 -
= firSsta, arm. hrestaJc; xism (xasm^) Zorn' = zd. aesma-;
zinhdr *Schutz, Sicherheit, gieb Acht! hiite dichf = zinhar
[ztnehar); istadan stehn' ^= np. paz. estddan. Vgl. § 12 und
27 und Sal. Shuk. Gram. p. 15, Dazu hirun = herUn
aussen, heraus* (s. oben p. 33), pindastan 'dafiir halten' ^^
mp. pa in daStan; si *diei' = paz. se (s^) = zd. d^rayqm;
ki Ver, alter k\ paz. he = ap. *kai/a?
Dagegen wird ap. ai im Anlaut zu paz. np. ya- in:
yax *Eis, osset. yex, ix^ zd. a^a;a-; yoA: 'ein*, paz. yak, phi.
evai aus aiva -\~ ka (neben -e ein* = paz. ew-, ev- in Zu-
sammensetzungen Shk. 243 = ap. aiva-).
Kapitel 6: ap. au.
§ 31. Ap. au {^' idg. aw, ew, ou) wird im Mp. und
Np. zu 0: roz Tag = ap. raudah- u. s. w.
§ 32. Ap. au = phi. 6 wird vor w, m im Paz. und
Np. zu U: gun^) *Farbe, Art und Weise' — p^z. jrim, gUna^
arm. goin^ zd. gaona- ; paz. driew 'a consecrated cake' Min.
Gl. 64 — zd. draonah-; surun (surln) 'Hinterbacken' = zd.
sraoni"^ Faredunf i^^?., Fredun, arm, Hruden (sassanidisch,
aus *Hredun umgestellt) = zd. &ra^iaona-\ mUm 'Wachs',
arm. mom (5. Jhd.); rum (bei Vullers rom) 'Schamhaare*
= skr. rdman-; hum 'Homapflanze' (vgl. hUm bei Mu-
waffaq p. 268, s. Horn Nr. 1113) = paz. hum Min. Gl.
106, zd. haoma-, Vgl. auch Bum *das byzantinische Reich'
(reimt auf bum Fird. I, 403) =' Poi/nT], lat. Roma, — Ausser-
dem ist altes o z\i U geworden in : samur 'Zobel' = parth.
aifuoo (de Lag. G. A. 71, 226), arm. samoir (= phi. ^samor)
und np. kahUd blau = arm. kapoit *dunkelblau (vgl. Horn
Nr. 842).
») Vgl. pSz. xaim Min. Gl. 124, phi. x{a)8m und tism Gl. and
Ind. 29, 68, Bdh. Gl. 124. Ebenso mit a fur i (i, e): ahan 'Eisen* =
phi. aatn (reap. a«g«) s. oben p. 10; mazldan *8augen, schmecken' s. § 17.
*) Dazu ciguna, can *wie*, zaryun etc.
```


## [2026-09-07T19:42:48.091Z] TOOL CALL #82: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"gaona\" POK_full.txt | head -10",
 "description": "Pokorny gaona"
}
```


### [2026-09-07T19:42:48.135Z] TOOL RESULT

```
32047:Avestan gaona-v\. "hair (esp. the animal); (hair)farbe' (compare above Lithuanian gauraT 
32084:"pubic hair' (compare above Avestan gaona-n. "hair'); Lithuanian gurnasm. "hip, haunch, 
34360:gaona- m. "profit, gain' (see below Lithuanian gaunu);
```


## [2026-09-07T19:42:52.194Z] TOOL CALL #83: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Root / lemma\" POK_full.txt | awk -F: '$1<32047' | tail -2; sed -n '31990,32000p' POK_full.txt; awk 'NR>=32047 && NR<=32300' POK_full.txt | grep -n \"Page(s)\" | head -2",
 "description": "Pokorny lemma for gaona"
}
```


### [2026-09-07T19:42:54.910Z] TOOL RESULT

```
31722:Root / lemma: ge(i)- : gd(i)- : 57- 
31753:Root / lemma: geu-, gau-, gu-{*sgeu-) 
'valley' from abrit. */r^/77i6'o-s 'valley'). Middle Low German kumm(e)i. 'round, deep vessel, 
tub, paten ', Modern High German Kumme'6eep bowl', Swiss chumme' cistern '; *kump- 
(from *kumb-m\h consonant-sharpening) Middle Low German kump. Middle High German 
kumpryesse\, cup ', Modern High German Kumpf. 

In addition perhaps npers. gumbed^ bulge, cupola, goblet'; 

further presumably Lithuanian gumbasm. ' bulge, swelling, lump, growth, knag'; Latvian 
^i//77/75 'swelling, lump, growth'; 

Old Church Slavic ggba' sponge, fungus ', Serbo-Croatian guba' sponge, leprosy ', 
84:Page(s): 393-398 
107:Page(s): 409
```


## [2026-09-07T19:43:03.966Z] TOOL CALL #84: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"niyaz\\|niy'z\\|ni-az\" POK_full.txt HRN.txt HUB.txt CHEUNG.txt IEC.txt 2>/dev/null | head -10; echo \"=== POK angh\"; grep -n \"Root / lemma: ang^h\\|Root / lemma: aŋ\" POK_full.txt | head -5",
 "description": "Search niyaz in POK etc"
}
```


### [2026-09-07T19:43:04.032Z] TOOL RESULT

```
HUB.txt:6330:apeniaz 'bediirfnisslos' = np. be-niyaz; apsparem *ich iiber-
CHEUNG.txt:11809:*MIDDLE PERSIAN: (+ *ni-) BMP nyd’c /niyaz/, MMP ny’z ‘want, need, misery’ 
CHEUNG.txt:11823:*NWIR: ? NP javazah, Gz. yane ‘mortar’ || (+ *ni-) NP niyaz ‘need’ || (+ *ui-) Khuns. 
CHEUNG.txt:35427:nyd'c /niyaz/, 171 
CHEUNG.txt:41214:niyaz, 172 
=== POK angh
5060:Root / lemma: anghen- 
5074:Root / lemma: angh- {*hengh-)
```


## [2026-09-07T19:43:07.043Z] TOOL CALL #85: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '11780,11835p' CHEUNG.txt",
 "description": "Cheung entry for niyaz"
}
```


### [2026-09-07T19:43:07.116Z] TOOL RESULT

```
*NWIR: ? Gz. b-a5 ‘look !’ 

*NEIR: (+ *abi-, *ui- ?) Yghn. yaxs-/yáxsta ‘to be seen, visible’ 

*SANSKRIT: äksi- ‘eye’ (RV+) = EWAia I: 42 

9 The Ir. word *Has- ‘eye’, from which the apparently ancient denomin. *Haxs 
derives, has lost *x by analogy with *us- ‘ear’. 

«PIE *H3ek¥-s- ‘eye’ = LIV: 297 | Pok.: 775 ff. 

*IE COGNATES: Gr. 800€, OCS oči (du. tantum) ‘eyes’, Lat. oculus (m.), Lith. akis 
‘eye’, etc. 

*REFERENCES: WIM II/2: 642; Werba 1999: 615; Rastorgueva -Edel’man 2000: 281 f. 


*Haz ‘to drive, lead’ 

*AVESTAN: az- ‘to lead’ || (+ *aua-) ‘to lead down, chase away’ || (+ *para-) ‘to 
carry, take away’ || (+ *ni-) caus. ‘to straiten’ (cf. De Vaan 2003: 34) = Liste: 10 
Pres. them.: IND. 3sg. YAv. azaiti, med. 35р. YAv. azaite (Yt 10.38, V 5.37), med. 3d. ҮАУ. *azöide (V 
3.11), 3р1. YAv. parazenti (Yt 13.68), INJ. 3sg. YAv. auuazat ‘chased away’ (Yt 19.81, Hoffmann 1968: 
283, fn. 4), 3р1. ҮАУ. azon (Yt 13.37), SUBJ. 1sg. YAv. azani (Yt 5.34, Yt 9.14, Yt 9.30, etc.), 3sg. YAv. 
"azaiti (Fr.), med. 3sg. YAv. azaite (V 18.76), 3pl. ? OAv. aza0a (Y 50.7, Y 64.3), OPT. 3sg. Y Av. para 
... aZoit (V 18.12), med. 35р. azaéta (V 18.68); Partic.: pres. med. Y Av. azamna- (Yt 10.86); Caus.: pres. 
IND. 35р. Y Av. azaiiaiti (Vn 13, Vn 15; De Vaan 2003, 1.с.), INJ. med. 35р. YAv. niiazata (Yt 5.127), 
3pl. YAv. niiazaiion (V 13.30) 

*MIDDLE PERSIAN: (+ *ni-) BMP nyd’c /niyaz/, MMP ny’z ‘want, need, misery’ 
(LW) > DMMPP: 48b 


172 *Hgar 


*PARTHIAN: (+ *ni-) ny’z ‘want, need, misery’ = DMMPP: 48b 

*KHOTANESE: hays- ‘to drive, send’ (with sec. h- ?) = SGS: 148 

*SOGDIAN: (+ *ni-) CSogd. ny’z’wt ‘needing, needy’, MSogd. ny’z ‘need’ (GMS: 
§1060) 

*NWIR: ? NP javazah, Gz. yane ‘mortar’ || (+ *ni-) NP niyaz ‘need’ || (+ *ui-) Khuns. 
vis(s)/viz- (inch. ?) ‘to seek; [+ va] ‘to find’, Abyan., Abz. yösta/yüz-, Anar. usse/ 
(y)uz-, Ard. viyoste/viyoz-, Fariz. -juz-, Gz. yuz-/yus(s)-, Nn. yusse/yuz-, Tr. vósta/ 
vöz-, Varz. ose/oz-, Yar. -just-/-juz- ‘to find’, Qohr. vüsta/vüz- ‘to find, obtain’, 
Natan. -just/-juz-, Meim. bem-vi:ft/a-vi:z- ‘to discover; to find’. 0 NP javazah is 
from *jaua-a(n)za-ka-, on which see Tafazzoli ("do vazah-i parti az diraxt-i аѕшӣ" [= 
Two Parthian words from the "Draxt-i-Asuri"], unpubl.). Differently, Hasandoust 
2001-2002: 36: *iaya-baja- ‘barley breaker’ (see *baj). The reconstruction would be 
less suitable for Gz. yane though. || The forms with pref. *ui- may be contaminated 
with *yaid?. 

*NEIR: (+ *apa-) Pash. (aor.) boz-/ (inf.) bötlol ‘to lead away’, Sh. boz-/boxt, Rosh. 
aböz-/abüxt, Bart. aböz-/aböxt ‘to send’ || (+ *upa- ?) Yi. aväz-/aväzd, M. avaz-/
```


## [2026-09-07T19:43:16.111Z] TOOL CALL #86: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=11835 && NR<=11870' CHEUNG.txt",
 "description": "Cheung Haz PIE line"
}
```


### [2026-09-07T19:43:17.270Z] TOOL RESULT

```
aböz-/abüxt, Bart. aböz-/aböxt ‘to send’ || (+ *upa- ?) Yi. aväz-/aväzd, M. avaz-/ 
avézd ‘to bring (someone), fetch’ || (+ *para-) Pash. pryez-, prez- ‘to take out’ || (+ 
*pari-) Yghn. piráyZ-, paréZ- ‘to run away’ 

*SANSKRIT: aj ‘to drive’ = EWAia I: 50 

Q According to Schmeja 1976: 101ff., the substantive Av. āzi- (m.) ‘greed’, MP /az/ 
(MMP ’’z, BMP ’c, Pth. ’’z, etc. can be equated with Skt. aji- ‘race, battle’, which 15 
the nominal derivative of aj. This is semantically difficult to explain though, perhaps 
via *‘drive’ ? 

PIE *H5eé- ‘to drive’? = LIV: 255 | Pok.: 4 ff. 

*IE COGNATES: Gr. yo ‘I drive, lead, go’, Lat. ago ‘I drive, to lead, to commit’, 


Toch. ak-, Arm. acem ‘to lead’, Olrish agid ‘to drive’, ON aka ‘to ride’, etc. 
*REFERENCES: EVP: 16; IIFL II: 194; EVS: 22a; Werba 1997: 333; ESIJa I: 288 ff.; Lecoq 2002: 121, 
124, 126 (passim); NEVP: 65 


*Hgar ‘to be awake’ 

*AVESTAN: YAv. yar- ‘to guard, watch’ || (+ *а-) caus. ‘to wake up [tr.]’ || (+ *fra-) 
inch. ‘to awake’, caus. ‘to wake up [tr.]’ — Liste: 19 

Perf.: IND. 3sg. YAv. jayara ‘is watching’ (N 19); Partic.: pres. inch. med. ? YAv. frayrisomna- (H 1.13), 
pres. caus. YAv. "fra. yäraiiant- (N 19), perf. YAv. jayauruuah- (Yt 10.7, etc.); Caus.: pres. IND. Isg. 
Y Av. а... gäraiiemi (Any 2), 3sg. YAv. “fra. yaraiieiti (V 18.22, N 19), OPT. 25р. YAv. fra gäraiiöis (N 
19) 

*MIDDLE PERSIAN: (+ *ui-) MMP wygr's-, BMP wgl’s- /wigras-/ ‘to wake, awaken’ 
=> DMMPP: 353b 

(+ *ui-) Pres.: IND. 3pl. BMP wgl’synd /wigrasénd/; Partic.: perf. pass. MMP wygr’d; Caus.: pres. 3sg. 
MMP "wygr'synyd, partic. MMP wygr'syn'g
```


## [2026-09-07T19:43:26.820Z] TOOL CALL #87: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"(+ \\*ni-)\" CHEUNG.txt | head -60",
 "description": "Cheung all ni- prefixed forms"
}
```


### [2026-09-07T19:43:26.864Z] TOOL RESULT

```
1365:frauua- ‘to shine’ || (+ *ni-) ? YAv. -niuuä- ‘to radiate downwards’ || (+ *ui-) YAv. 
1399:*NEIR: Oss. bon ‘day’, Sariq. vuyn ‘light, radiance’, Wa. voyn ‘fire; light" || (+ *ni-) 
1499:*AVESTAN: b(a)il- ‘to fear [intr.]; to be scary, scare’ || (+ *ni-) ‘to be afraid of’, also 
1607:/parwand-/ ‘to surround, enclose, contain, comprise’ || (+ *ni-) ? MMP nwn- ‘to 
1618:(YK‘YWMWN-)yt /paywast éstéd/ || (+ *pari-) Partic.: perf. pass. BMP plwstk /parwastag/ || (+ *ni-) 
1636:‘burden’ || (+ *ni-) BSogd. nB’ynt ‘to attach’ || (+ *ui-) CSogd. wbnty (m.) ‘snare’ || 
1648:(+ *ni-) m/nBncy- ‘to swear (oath) || (+ *ham-) "nbncy- ‘to intend, have it mind’ 
1652:‘bundle’ || (+ *ni-) voBavdo, vaßavõo-, уоВоубо ‘beside, with” = S-W, Bact.: 
1672:*pati-) Rosh. padve60-/padvost ‘to knit (a broken bone) || (+ *ni-) Oss. I. 
1811:bB’ry- ‘to explain, expound; to inform’ || (+ *ni-) m/nB’ry- ‘to treat (wrongly), get 
1857:térafta “о give’ (see Sogd.) || (+ *ni-) Yi. navor-/navar-, M. never- ‘to take out, draw 
1865:Orm. ur-uk ‘to hold, keep’ || (+ 4-) Par. ar-/awur ‘to bring’ || (+ *ni-) Orm. 
2111:M. vizni ‘pillow’ (*brzanaka) || (+ *ni-) Oss. I. nyverzeen, D. niveerzen ‘bedside’ || 
2372:*KHOTANESE: (+ *ni-) OKh. nihujs- ‘to sink down, set’ || (+ *ham-) ha(m)bujs- 
2508:*CHORESMIAN: BX- ‘to give, bestow; to share’ || (+ *ni-) m/nBx- ‘to share’ 
2908:*pari-) MMP przyd (past stem) “о shut in, imprison; fix in, fasten in’ || (+ *ni-) 
2914:cynyhyd || (+ *ni-) Pres.: IND. 3sg. MMP nycynyd, MMP “ncynyd; Partic.: perf. pass. MMP ncyd 
2915:*PARTHIAN: cyn- ‘to gather, collect’ || (+ *ni-) ncyn- ‘to pile up, heap up together’ || 
2918:Pres.: IND. 3pl. cynynd || (+ *ni-) Pres.: IND. 3sg. ncynyd || (+ *ui-) Pres.: IND. 2sg. wycyn’h, 3sg. 
2957:‘enclosure for sheep’, parZini ‘thorn-hedge’ || (+ *ni-) Yi. laZino ‘pile of firewood? || 
3199:*MIDDLE PERSIAN: BMP cyhyn- /Cihen-/ ‘to teach, make known, inform’ || (+ *ni-) 
3203:Pass.: pres. IND. 1sg. BMP cyhywm /¢ihiyum/, pret. caus. 3sg. BMP cyhynyt /cihenid/ || (+ *ni-) Pres.: 
3450:perceive, see’ || (+ *pati-) OKh. päjsas- ‘to look at’ || (+ *ni-) nijsas- ‘to show’ || (+ 
3453:‘riddle’ || (+ *ni-) ’nc’h- ‘to show’, ? m/ncs(y)- ‘to look at’. o Henning 1958: 111 
3466:*NEIR: (+ *ni-) Yi. nisáZ-/nisaZi-, M. nijas-/nijast- ‘to show’ 
4051:*AVESTAN: see *daH! || (+ *à-) ‘to put, place in, on’ || (+ *uz-) ‘to erect’ || (+ *ni-) ‘to 
4067:with legal content’ || (+ *ni-) MMP nyh- (BMP HNHTWN-) ‘to lay, put down’ || (+ 
4078:(+ *ni-) Partic.: pres. MMP nyh’dg 
4090:halt’ || (+ *ni-) NP nihadan/nih-, Kurd. (Sor.) da-nan/da-né- ‘to lay, put down’, Zaz. 
4104:*MISC: (+ *ni-) Orm. niw-/nyök ‘to put down, place’ || (+ *ui-) Arm. (LW) угап 
4608:make stick’, Sariq. padafson- (caus.) ‘to raise’ || (+ *ni-) Sh. nidafc-/nidtuvd, Rosh. 
5108:*AVESTAN: daraz- ‘to attach’ || (+ *ni-) ‘to fasten’ || (+ *ham-) ‘to bind together’. > 
5164:polarz-/palisé-, M. polörz- ‘to wrap up (a bundle) || (+ *ni-) Sh. nióuyj ‘woollen yarn 
5301:pióówg (in pióowg woc- ‘to become apparent, noticeable, to appear’) || (+ *ni-) Wa. 
5429:perfume; burn’ || (+ *pari- ?) OKh. pathai- (pathu-) ‘to burn up’ || (+ *ni-) nado ‘fire’ 
5936:assure, make certain’ || (+ *ni-) nydrynj- ‘to keep down, subdue’ || (+ *ham-) 
5942:Pres.: SUBJ. 25р. drxs’h || (+ *abi-) Pres.: IND. 3sg. ’bdrynjyd, IMPV. 2pl. "bdrynjyd || (+ *ni-) Pres.: 
6415:|| + *pari-) ‘to run around’ || (+ *fra-) ‘to approach, engage’ || (+ *ni-) ‘to hasten’ 
6441:*PARTHIAN: (+ *ni-) nydf’r- ‘to hasten, hurry’ = Ghilain: 74 | DMMPP: 252b 
6469:move, quiver’ || (+ *ni-) LKh. *niphan- (naphan-) ‘to rejoice’ || (+ *nis-) OKh. 
6624:BMP Gul /afur-/ ‘to create; bless’ || (+ *ni-) BMP nplytk /nifridag/ (ppp.) ‘cursed’, 
6630:*PARTHIAN: бур ‘dear, beloved’ || (+ *a-) "fryn- ‘to bless’ || (+ *ni-) nfryd- (pret. 
6646:BSogd. ptßr’yn ‘to bless back’, MSogd. ptfryn ‘to send greetings’ || (+ *ni-) BSogd. 
6656:*NWIR: (+ *а-) NP 4faridan/afarin- ‘to create’ || (+ *ni-) NP nifrin, Nn. nifrin ‘curse’ 
7015:*AVESTAN: YAv. gah- ‘to gorge’ || (+ *ni-) ‘to digest’ || (+ *nis-) ‘to devour’ 
7261:*MIDDLE PERSIAN: (+ *ni-) BMP nkyc- /nigez-/ ‘to expound’ || (+ *ham-) BMP 
7265:(+ *ni-) Pres.: IND. 3sg. BMP nkycyt /nigézéd/; Inf.: BMP nkyhtn /nigextan/ || (+ *ham-) Pres.: IND. 3pl. 
7313:‘to go around, into, reach, approach’ || (+ *fra-) ‘to come to, reach’ || (+ *ni-) ‘to 
7409:*Hai) || (+ *fra-) SSogd. Вт, CSogd. f$’m (caus.) ‘to send’ || (+ *ni-) CSogd. 
7427:су-) || (+ *a-) m['z^my- (caus.) ‘to bring’ || (+ *fra-) fry’mk ‘adult’ || (+ *ni-) m/nys- 
7742:stiffen’, ? Gur. (Kand.) giris (in giri$ wärdän ‘to be stuck’) || (+ *ni-) ? Bal. nigérit/ 
7837:MSogd. ’zy’yr-, MSogd. jyyr- ‘to call, summon’ || (+ *ni-) BSogd. nyr’’y ‘to praise, 
7879:*AVESTAN: (+ *ni-) Y Av. niyr- ‘to throw down’. © For a discussion of this hapax 
7963:(m.) ‘indigestion’ || (+ *uz-) M. zoyóriy ‘thirsty’ || (+ *ni-) Pash. nyar(d)-/nyar- ‘to 
8272:muffle’ || (+ *ni-) ngwnd- ‘to cover, veil, cothe, hide? => Ghilain: 83 | DMMPP: 10a, 
8276:’bywnd,; Partic.: perf. pass. ’bgwst, *’bgwstg || (+ *fra-) Pres.: IND. 3р]. "fr'gwndynd || (+ *ni-) Pres.: 
8284:‘to cover’, CSogd. ptywnt ‘to cover, hide’, MSogd. ptywó ‘to conceal’ || (+ *ni-) 
8293:Pass.: perf. intr. IND. 3sg. MSogd. ptywstyy xcyy ‘is hidden’ || (+ *ni-) Pres.: IND. 3sg. BSogd. ny’wnt, 
8301:be constipated, blocked’ || (+ *pari-) prxsy- ‘to be concealed, unclear’ || (+ *ni-) 
8316:a blanket)’ || (+ *ni-) Yghn. nuyunt-/nuyust, Yzgh. noy"and-/noy"ost ‘to put on
```


## [2026-09-07T19:43:34.516Z] TOOL CALL #88: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"(+ \\*ni-)\" CHEUNG.txt | sed -n '60,200p'",
 "description": "Cheung ni- forms continued"
}
```


### [2026-09-07T19:43:34.568Z] TOOL RESULT

```
8316:a blanket)’ || (+ *ni-) Yghn. nuyunt-/nuyust, Yzgh. noy"and-/noy"ost ‘to put on 
8371:*MIDDLE PERSIAN: MMP gws ‘ear’ || (+ *ni-) MMP nyws-, BMP n(y)dw(h)s- 
8378:(+ *ni-) Pres.: IND. 3pl. MMP nywsynd, BMP ndwhsynd /niyosénd/, SUBJ. 3pl. MMP nywš nd, IMPV. 
8383:(LW) 'zgwl- ‘to listen’ || (+ *ni-) ngws- ‘to hear’. 0 The change Ir. *§ > I in 'zgwl- 
8388:(+ *ni-) Pres.: IND. 25р. ngws’, SUBJ. 25р. ngws’h, 3sg. псу”, IMPV. 2sg. ngwS-, 2р1. ngwSyd; Partic.: 
8395:‘to hear’ || (+ *ni-) SSogd. nyws, BSogd. ny’ws, CSogd. nyws, MSogd. nyws ‘to 
8399:2sg. SSogd. ptywsy, 3sg. BSogd. pty’wst, BSogd., CSogd. ptywst, etc. || (+ *ni-) Widely attested: Pres.: 
8404:(+ *ni-) m[nyws- ‘to hear’, m/nywsy- (caus.) ‘to cause to hear” > Samadi: 91 f., 19, 
8412:Yghn. düyüs-/düyüsta ‘to hear’ || (+ *ni-) Pash. nyaZ-/nyutol, nywatal ‘to obey, 
8452:*PARTHIAN: (+ *ni-) ngwz- ‘to hide, disappear’ = Ghilain: 64 | DMMPP: 241b 
8540:*BACTRIAN: (+ *ni-) ? vayat- (pret. stem) ‘to receive’ ? || (+ *ham-) ? wyytt- (pret. 
8939:*AVESTAN: hiö- ‘to sit, be seated’ || (+ *abi-) ‘to be seated on (a horse)’ || (+ *ni-) ‘to 
8948:*OLD PERSIAN: (+ *ni-) ni-sad- (caus.) ‘to establish’ = Kent: 212 
8957:*PARTHIAN: (+ *ni-) nšyd- ‘to sit (down), settle oneself’, also nšyl- (< Bact./Sogd. ?). 
8963:mount; ride’ || (+ *ni-) nät- ‘to sit down’, näta’s- (na’s-) (inch.) ‘to end’ = SGS: 39, 
8967:caus.) ‘to sit through, out’ || (+ *ni-) BSogd. пуб, CSogd. пуа, MSogd. пуб ‘to sit 
8970:(+ *pari-) Impf.: IND. 2sg. SSogd. prysyöy || (+ *ni-) Well attested: Pres.: IND. 3sg. BSogd. nyöt, 3pl. 
8973:*CHORESMIAN: (+ *ni-) ny0- ‘to sit; to be, become’, m/nh’zy- (caus.) ‘to place’ 
8980:*BACTRIAN: (+ *ni-) vipoApo, мролцо ‘seat (of the gods), throne, dwelling’. 0 Cf. 
8985:sit’ ?) || (+ *ni-) Widely attested: NP niSastan/nisin-, Bal. nist/nind-, Kurd. nistin, 
8996:I. badyn/badt, D. badun/badt ‘to sit’ || (+ *ni-) Pash. näst ‘seated, sitting’, Sh. n10-/ 
9003:*MISC: (+ *ni-) Orm. n-/nustuk, nastak ‘to sit down’ = ney-/nöstök, nóstok, nostok, 
9214:(+ *ni-) Pres.: IND. dur. 2sg. CSogd. ’sypysq, 3sg. BSogd. ’ns’ypt; Impf.: IND. 3pl. CSogd. msypnt, 
9261:break-fast) || (+ *ni-) Kurd. (Kurm.) nihér(t)in/nihér-, (Sor.) niwarin ‘to look, have a 
9504:*MIDDLE PERSIAN: BMP hwn- /hun-/ ‘to extract, express (höm)’ || (+ *ni-) ? MMP 
9507:Partic.: perf. pass. BMP hwnyt /hunid/; Inf.: BMP hwnytn /hunidan/ || (+ *ni-) Caus.: pres. IND. 3sg. 
9763:recall’, Yzgh. pamar- ‘to wait for’ || (+ *ni-) Oss. I. nymzr, D. (med)nimer ‘on 
10287:гых(ы)р(ы)у-/гох(р)оуа- ‘to put to sleep’ || (+ *ni-) Sh. nixäb-, (Baj.) nix(X)äb-/ 
10463:*KHOTANESE: hvaraka- ‘taker’, ‘robber’ || (+ *ni-) nähvarr- ‘to long for; grasp at’ 
11232:*NWIR: (+ *abi- NP yaftan/yab- ‘to find’ || (+ *ni-) ? Yzd. (Zor.) neftvun, 
11245:bring, convey’ || (+ *ni-) Sariq. niyup-/niyopt ‘to overtake, reach’, ? Sangl. niv-/nivö 
11302:|| (+ *ni-) ‘to go, fall down’ || (+ *ui-) caus. ‘to drive off. 0 Assuming a separate 
11322:go down to, arrive at’ || (+ *para-) parars(s)a- ‘to come to, arrive at’ || (+ *ni-) 
11356:send’, Nn. räsnä/räsn- ‘to cause to arrive, send’ || (+ *ni-) Kurd. (North.) hinärtin/ 
11369:stretch out, extend; to pour, flow out’ || (+ *ni-) ? Wa. nards (in nards di-, roč- ‘to run 
11777:*CHORESMIAN: (+ *abi-) ? mjByxy- ‘to learn from, apprehend, retain’ || (+ *ni-) 
11800:carry, take away’ || (+ *ni-) caus. ‘to straiten’ (cf. De Vaan 2003: 34) = Liste: 10 
11809:*MIDDLE PERSIAN: (+ *ni-) BMP nyd’c /niyaz/, MMP ny’z ‘want, need, misery’ 
11816:*PARTHIAN: (+ *ni-) ny’z ‘want, need, misery’ = DMMPP: 48b 
11820:*SOGDIAN: (+ *ni-) CSogd. ny’z’wt ‘needing, needy’, MSogd. ny’z ‘need’ (GMS: 
11823:*NWIR: ? NP javazah, Gz. yane ‘mortar’ || (+ *ni-) NP niyaz ‘need’ || (+ *ui-) Khuns. 
12252:*MIDDLE PERSIAN: ВМР myc- /mez-/ ‘to urinate’ || (+ *ni-) MMP nmyzysn ‘incite- 
12259:*PARTHIAN: (+ *ni-) nmyzysn ‘incitement, provocation, urging? > DMMPP: 244a 
12368:*pari-) ‘to brush, wipe around’ || (+ *fra-) ‘to wipe forth, away’ || (+ *ni-) ‘to sweep 
12395:*PARTHIAN: (+ *ni-) nmrz- ‘to clean, cleanse; make smooth’ = Ghilain: 53 | 
12402:vameys- ‘to rub down’ || (+ *ni-) nimals- ‘to rub down’ || (+ *ш-) ggumäls- 
12408:*SOGDIAN: (+ *fra-) MSogd. fr’mrz- ‘to spoil’ || (+ *ni-) BSogd. nm’rz- ‘to touch’ || 
12425:|| (+ *ni-) Anar. nimärzi, Gz. nemärzün, nimárzün, Varz. nemarzin ‘broom’ || (+ 
12441:‘weakened (by a wound)’ (МЕУР: 102) || (+ *ni-) Sariq. nimiZg, nümüzg ‘harrow, 
12587:*MIDDLE PERSIAN: MMP rw-, BMP rwb-, Iwb- /raw-/ ‘to go, proceed’ || (+ *ni-) 
12592:“rw’n, perf. pass. MMP rpt, MMP "rft || (+ *ni-) Pres.: SUBJ. 3sg. MMP nyrw’d {uncert. reading} 
13140:*AVESTAN: YAv. raoö- (ruö-) ‘to grow’ || (+ *fra-) ‘to grow to(wards)’ || (+ *ni-) ‘to 
13605:over, convert’ || (+ *ni-) nva(y)- ‘to grasp’ — SGS: 93 f., 39, 11, 62 
13657:*KHOTANESE: (+ *ni-) OKh. *nuvad- (nuvai-) ‘to make a noise’ (differently DKS: 
13660:*NEIR: Pash. lwast-/lwal- ‘to read’ || (+ *ni-) Yghn. novva ‘noise, sound’. Ọ 
13779:(+ *ni-) Wa. ni(y)-, nay-/nayat ‘to be blown out, go out (of fire, light)’, ni(sr)v-, 
13966:|| (+ *ni-) ? ‘encompass’ || (+ *ham-) ‘to cover’ = Liste: 50 
14006:|| (+ *ni-) Pash. nwaráy (m.) ‘garment’ 
14026:*AVESTAN: (+ *ni-) ? OAv. niuuar- ‘to defend’, YAv. niuuor- (pass.) ‘to be held 
14033:*KHOTANESE: OKh. batha- ‘cuirass’, be’sa- ‘shield’ || (+ *ni-) OKh. nyur- ‘to 
14266:along, to’ || (+ *ni-) ‘to keep, hold down’ || (+ *ham-) ‘to attend to’ = Liste: 46 
14278:as one’s own’ || (+ *ni-) ‘to set down’ — Kent: 205a 
14307:pttyy’m, etc. || (+ *fra-) Fut.: IND. (SUBJ. ?) 2pl. MSogd. fry’mö’k’m || (+ *ni-) Widely attested: Inch. 
14319:ayös-/ayöd- ‘to take away’ || (+ *ni-) Pash. nis-/niw-, Yi. nis- ‘to take out’, Yghn. 
14397:*MIDDLE PERSIAN: (+ *ni-) MMP nyys- ‘gaze, stare at, look into; (?) to mark’, nys’n, 
14408:*NWIR: (+ *ni-) NP шап ‘sign, mark, spot’. 0 The Nn. verb dinisayi/dinisi and Anar. 
14422:*MISC: (+ *ni-) Arm. (LW) nis ‘sign, mark, spot, speckle’, nsan “(miraculous) sign, 
14514:*AVESTAN: (+ *ni-) Y Av. niiu- ‘to (re)bind, hold’ = Liste: 47 
14574:*KHOTANESE: (+ *ni-) nyus- ‘learn’, (caus.) ‘teach’ = SGS: 61 
14723:*KHOTANESE: (+ *4-) Ayauys- ‘to be disturbed’ || (+ *ni-) nyauys- ‘to be defeated, 
14737:*NEIR: Oss. I. uzyn/wyzt, D. ozun/uzt ‘to shake, rock (a baby) to sleep’ || (+ *ni-) 
14827:*NEIR: (+ *ni-) Yi. niáské, M. niezye ‘yawn’ 
14862:*MIDDLE PERSIAN: BMP zd- /zay-/ ‘to ask, demand, implore’ || (+ *ni-) MMP nyz’y- 
14870:zst /zast/ || (+ *ni-) Pres.: IND. 2р1. MMP nyz’yd, 3р1. MMP nyz’ynd, SUBJ. 3pl. MMP *nyz’y’nd 
14871:*PARTHIAN: (+ *a-) 'g'dg, "y'dg ‘wish’ || (+ *ni-) ng’y- ‘to pray, supplicate’, ng’d 
14876:(+ *ni-) Pres.: IND. Ipl. ng’y’m, 1р1. ng’y’m, 1р1. ng’y’m, 2р1. ng’yd, 3р1. nyg’ynd, SUBJ. 1pl. ng’y’m, 
14882:"py ów ‘praise, fame’ || (+ *ni-) CSogd. ny’d’ (Е), MSogd. ny’ö’ ‘request, entreaty’ 
15049:upon’ || (+ *pati-) ‘to strike, hit (with a weapon) against’ || (+ *ni-) ‘to strike down’ 
15096:OKh. pajs(afi)- ‘to be struck, beaten’ || (+ *ni-) nijsa- ‘to befall, be struck with’ 
15342:*CHORESMIAN: (+ *ni-) m/ks- “о be pounded, trampled down’ = Samadi: 104 
15379:*PARTHIAN: (+ *ni-) nkmb- ‘to bend’ = DMMPP: 242b 
15385:43.9 f.) || (+ *ni-) BSogd. nk’np- ‘to bend; subdue’ 
15388:straight’ f. BSogd. ’’k’Btc-(h), BSogd. ’’k’Btcy-h ‘crooked’ || (+ *ni-) Pres.: IND. 35р. BSogd. nk’npt, 
15392:m['knby- ‘to bend, curve’ || (+ *us-) m/sknb- ‘to trip, stumble’ || (+ *ni-) m/nknby- 
15414:*AVESTAN: (+ *ni-) ? Y Av. ni kan- ‘to bury’ || (+ *ui-) YAv. vikan- ‘to destroy, ruin’ 
15423:*OLD PERSIAN: (+ *aua-) ? avakan- ‘to throw, place on’ || (+ *ni-) nika(n)- ‘to tear 
15476:(+ *ni-) nkn- ‘to bury’ || (+ *ui-) wkny- ‘to wear out, become old; be ruined’, 
15492:pargandah ‘dispersed, scattered’ || (+ *ni-) Kurd. (Kurm.) nikandin ‘to bury’ 
15495:regzd ‘to shake, spread (salt, pepper for seasoning)’ || (+ *ni-) Oss. I. nyganyn/ 
15556:around’ || (+ *ni-) ‘to dig in’ = Liste: 14 
15598:*BACTRIAN: (+ *ni-) vakav- ‘to dig’ = S-W, Bact.: 207b 
15609:‘building’ || (+ *ni-) Oss. D. nik zd ‘carve, cut’ 
15807:‘picture, image’, MMP phyk’r, BMP рік? /pahikar/ ‘battle, struggle’ || (+ *ni-) 
15823:BMP ptk’lynd /pahikarend/ || (+ *ni-) Pres.: IND. 3sg. MMP ng’ryd, 3р1. MMP ng rynd; Partic.: perf. 
15830:+ *fra-) ? ‘frg’r- ‘to be dejected’ || (+ *ni-) ng’r- ‘to paint, draw’, ng’rgr ‘painter’ || 
15836:kyrdn, qyrdn || (+ *pati-) Pres.: IND. 3pl. pdk’rynd || (+ *fra-) Pres.: IND. 1pl. ‘frg’r’m || (+ *ni-) Pres.: 
15883:paykar ‘picture, statue’ || (+ *ni-) NP nigastan/nigar- ‘to paint’ || (+ *ham-) NP 
15921:*PARTHIAN: (+ *ni-) ? ngwrc- ‘[pejorative] to baptize’ (-c- < ?). Ф According to 
16329:|| (+ *ni-) BMP nk’s /nigäh/ ‘look, attention’ 
16334:*pari-) prgs- ‘to observe, take care’, (?) Pth. prgst ‘God forbid!’ || (+ *ni-) ng’h 
16344:*KHOTANESE: OKh. kas- (or kas-) ‘to appear’ || (+ *ni-) OKh. nyas- ‘to despise’ 
16359:feed’ (< *‘to look after’) || (+ *fra-) škš- ‘to look to’ || (+ *ni-) nk’s(y)- ‘to (take a) 
16362:*NWIR: Khuns. kis-/kis(s)- ‘to look to’ || (+ *а-) NP agah ‘knowing, aware’ || (+ *ni-) 
16375:‘absit omer || (+ *ni-) Arm. (LW) nkat-em ‘to see, consider’ || (+ *nis-) Arm. (LW) 
16401:*NEIR: (+ *ni-) Oss. I. nyxeesyn/nyxest, D. nix&sun/nixast ‘to be attached, glued, 
16443:*KHOTANESE: (+ *ni-) nyassa- ‘deficient, bad’ 
16520:’kws-, "kwh- ‘to hang up, fasten’ || (+ *ni-) MMP ngwc- ‘to bow, prostrate, bend 
16526:(+ *ni-) Pres.: IND. 1р1. MMP ngwcym, 3р1. MMP ngwcynd; Partic.: perf. pass. MMP ngwcyd 
16545:*CHORESMIAN: (+ *4-) m['kwcy- ‘to submerge’ || (+ *ni-) m/nkwcy- ‘to slumber’ 
16580:*CHORESMIAN: m/kwby- ‘to churn (milk)’, kwbyk ‘dasher’ || (+ *ni-) m/kwby- ‘to 
16775:stoke’, (”)skwryk ‘poker’ (164.4) || (+ *ni-) m/nkwzy- ‘to dunk’. ç MacKenzie IV: 
16857:‘buttermilk’ || (+ *ni-) Sh. (Baj.) nimäö-/nimost ‘to prepare cream and sour milk’, 
16924:command’ || (+ *ni-) MMP nm’y- ‘to show’ || + *ui-) ? MMP gwm’y- ‘to suffer, 
16931:Pres.: IND. 1sg. BMP plm’ym /framayem/, 3sg. MMP prm’yd, etc. || (+ *ni-) Pres.: IND. 3sg. MMP 
16934:‘to contemplate, consider, believe’ || (+ *fra-) frm’y- ‘to order’ || (+ *ni-) nm’y- ‘to 
16941:prm’dn || (+ *ni-) Pres.: IND. 3sg. nm’yd, 3р1. "nm’ynd, nm’yynd, SUBJ. 1sg. nm’y’n, IMPV. 2pl. 
16952:(+ *ni-) SSogd. nm’y, CSogd. nm’y, MSogd. nm’y ‘to judge’. Ф Also attested 15 the 
16968:frmy, 3sg. BSogd. prm "yt, dur. 35р. SSogd. prm’ytskwn, CSogd. frmytg, etc. || (+ *ni-) Pres.: IND. 15р. 
16990:‘to order, command’ || (+ *ni-) NP nimäy-/nimüdan ‘to appear, show’, Kurd. (Sor.) 
17136:*KHOTANESE: (+ *ni-) OKh. nämäs- ‘to wink’ > SGS: 55 
17138:*SOGDIAN: (+ *ni-) BSogd. nymz- ‘to blink’, ? CSogd. nmzy’ ‘wink, blink’ 
17144:*NEIR: (+ *ni-) Yi. nomíZ ‘winking’, nemig-/nemosk' (Zarubin), Ishk. nu-mul- ‘to 
17169:move [intr.], to be swung’ || (+ *ni-) Yzgh. namoxs-/namoxt ‘to go out’, Yzgh. 
17470:*CHORESMIAN: (+ *ni-) ömn- ‘to tan (hide, leather)’ (< Pamiri ?) = Samadi: 65 f. 
17475:yzmast, D. ezmentun/ezmest ‘to minx, stir (upy || (+ *ni-) Rosh. (Orosh. ?) 
17873:*NEIR: (+ *ni-) Oss. L nymuzyn/nymygd, D. nimozun/nimugd ‘to point out; to carry 
18140:*AVESTAN: (+ *para-) OAv. mraoc- ‘to float, submerge’ || (+ *ni-) YAv. nimraoka- 
18538:*MISC: (+ *ni-) Огт. піт-/піпт ek ‘to descend’ 
18943:*AVESTAN: Y Av. paó/0- ‘to fall, be stuck in’ || (+ *ni-) ‘to lie, lay down (esp. to have 
18954:*MIDDLE PERSIAN: (+ *ni-) MMP nb’st- (pret. stem) ‘to throw down’ = DMMPP: 
18961:*PARTHIAN: (+ *ni-) ? nb’y- ‘to lay down’ = Ghilain: 70 | DMMPP: 239a 
18965:*KHOTANESE: (+ *ni-) nuvad- ‘to lie down’ = SGS: 58 
18967:*SOGDIAN: (+ *ni-) BSogd. nypö- ‘to lie down’, BSogd. np’yö (caus.) ‘to lay’ 
18972:*CHORESMIAN: (+ *ni-) ’nb’zy- ‘to lie down’ {hapax} = Samadi: 116 
18974:*NWIR: (+ *ni-) Kurd. (Kurm.) nivin, nivistin/niv-, (Sor.) nustin/nu- ‘to lie down, 
18977:*NEIR: ? Pash. post, (pl.) pasta ‘soft, yielding’ || (+ *ni-) M. naliv-/nuvost- ‘to lie 
19001:*AVESTAN: pà- ‘to protect’ || (+ *pati-) ‘to guard against; to guess’ || (+ *ni-) ‘to 
19021:prosperous, cultivated’, BMP ’p’tyh /abadih/ ‘prosperity; village’ || (+ *ni-) BMP 
19035:*KHOTANESE: pā- (pai-) ‘to protect’ || (+ *ni-) ? nvi ‘pledge’ = SGS: 86 
19040:perceive’ || (+ *pati-) SSogd. pcp’y ‘to expect, be ready for’ || (+ *ni-) SSogd. np’k, 
19052:*CHORESMIAN: (+ *ni-) nb’k ‘pawn, pledge’
```


## [2026-09-07T19:43:53.510Z] TOOL CALL #89: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for r in \"\\*uart\" \"\\*pais\" \"\\*par(H)\" \"\\*parH\" \"\\*paid\"; do echo \"### $r\"; grep -n \"^$r \" CHEUNG.txt | head -4; done; echo \"=== paid PIE\"; awk 'NR>=18940 && NR<=19000' CHEUNG.txt | grep -n \"PIE\\|IE COGNATES\" ",
 "description": "Cheung roots uart, pais, parH, paid"
}
```


### [2026-09-07T19:43:54.772Z] TOOL RESULT

```
### \*uart
27387:*uart 423 
### \*pais
19175:*pais 291 
19188:*pais ‘to adorn, paint; to write’ 
19265:*pais ‘to crush, grind’ 
58420:*pais 
### \*par(H)
### \*parH
### \*paid
=== paid PIE
52:«PIE *ped- ‘to move at a walking pace, be on one’s feet? = LIV: 458 | Pok.: 791 
54:*IE COGNATES: Lat. pessum ‘to the bottom, to the ground, downward’, OCS pasti ‘to
```


## [2026-09-07T19:44:00.473Z] TOOL CALL #90: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '19188,19215p' CHEUNG.txt; echo \"===== uart\"; sed -n '27387,27392p' CHEUNG.txt; grep -n \"^\\*uart ‘\" CHEUNG.txt | head",
 "description": "Cheung pais and uart"
}
```


### [2026-09-07T19:44:00.545Z] TOOL RESULT

```
*pais ‘to adorn, paint; to write’ 

*AVESTAN: YAv. paés- ‘to adorn’ || (+ *fra-) ‘to embellish’ = Liste: 34f. 

Partic.: pres. them. YAv. anku.paésomna- (Yt 17.10), perf. pass. YAv. frapixsta- (Yt 14.27) 

*OLD PERSIAN: рї??Ө- ‘to cut, engrave, adorn’ || (+ *ni-) ‘to engrave, inscribe’ 
= Kent: 194 

Pres. them. / n-: impf. IND. 3pl. api(")0a" <a-p-i-9> (DSf 54); Aor. s- IND. lsg. niyapaisam 
«n-i-y-p-i-0-m» (DB 4.71); Partic.: perf. pass. nipista- <n-i-p-i-8-t-> (DB 4.47), <[n]-[i]-p-i-8-t-> (DSe 
52, XV 22, XPh 31); Inf: nipistanaiy <n-i-p-i-S-t-n-i-y> (XV 24); Pass.: impf. IND. 35р. "niyapiOiya 
<n-i-y-p-i-[0]-i-[y]> (РВ 4.91 |) 

*MIDDLE PERSIAN: MMP pyys-, BMP pys- /pes-/ ‘to adorn, colour’ || (+ *ni-) MMP 
nbys-, BMP nps- /nibis-/ ‘to write, copy a book = DMMPP: 291b, 239b 

Pres.: SUBJ. 3sg. MMP pyys’d; Partic.: perf. pass. BMP pysyt /pésid/ ‘(-)coloured’ || (+ *ni-) Pres.: IND. 
35р. MMP nbysyd; Partic.: pres. MMP nbys’g’n (pl.), perf. pass. BMP npstk /nibistag/; Inf.: BMP npstn 
/nibistan/; Pass.: IND. 3sg. MMP nbyst, BMP npst /nibist/, 3р1. MMP nbystynd 

*PARTHIAN: (+ *ni-) nbys- ‘to write’ = Ghilain: 61 | DMMPP: 239b 

Pres.: IND. 35р. nbysyd, SUBJ. 15р. “nbys’n, 1р1. nbys’m, IMPV. 2pl. nbysyd; Partic.: perf. pass. nbyst, 
nbystg; Inf.: nbystn 

*KHOTANESE: pisaa- ‘painter’, pisa- ‘artistic work, painting’ 

===== uart
*uart 423 


*CHORESMIAN: (+ *pari-) prwr- ‘to rear, nourish, feed’ (LW). © Not from the root 
*bar ‘to carry, bring’, *pari-bar, as suggested by Samadi. || The Chor. forms cannot 
derive directly from *pari-uarza-, which would have yielded **prwZ- in Chor., cf.
```


## [2026-09-07T19:44:06.464Z] TOOL CALL #91: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"\\*uart\" CHEUNG.txt | sed -n '1,25p'; echo \"=== navard\"; grep -n -i \"navard\\|nawardidan\\|nabardidan\" CHEUNG.txt | head",
 "description": "Cheung uart entry"
}
```


### [2026-09-07T19:44:06.530Z] TOOL RESULT

```
7690:forms are from pres. *g(a)rna- (cf. Chor. yyrnyk), not from *uart- as assumed by 
7691:Cabolov, l.c., cf. *uarta- > Kurd. (Sor.) bard ‘stone’, v. *uart. 
8082:NP gardidan (< *uart- ?), (Tadj.) Selidan ‘to roll’ (LW, cf. Yghn. yil-), Abyan. va 
27387:*uart 423 
27481:*bei’ss- (bais-) ‘to make turn’ (*uart-s-aja-) || (+ *a-) OKh. äbeis- ‘to turn’ || (+ 
27514:wcy-. The form may be connected to the root *uart. > Samadi: 212, 217, 9 f., 30, 
55189:(s.v.), *tauf (s.v.), *uart 
55216:*pat, *san, *uart (s.v.), *xac, 
56036:(s.v.), *9ua(n)j (s.v.), *uart 
56883:(s.v.), *tauf (s.v.), *uart 
57639:*pat, *san, *uart (s.v.), *xac, 
=== navard
27519:Kurd. (Kurm.) zivirin ‘to turn, be spinning’ || (+ *ni-) NP nawardidan/naward- ‘to 
41189:nawardidan/naward-,
```


## [2026-09-07T19:44:10.016Z] TOOL CALL #92: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '27440,27470p;27514,27540p' CHEUNG.txt",
 "description": "Cheung uart entry text"
}
```


### [2026-09-07T19:44:10.062Z] TOOL RESULT

```
*yart ‘to turn’ 

*AVESTAN: Y Av. varat- ‘to turn’ > Liste: 51 

MED. (exc. Caus.); Pres. them.: INJ. 3sg. Y Av. varetata (F 8); Caus.: IND. 3pl. ? YAv. ham.varontaiionti 
(N 97) 


424 *yart 


«OLD PERSIAN: ? vart- ‘to turn’. 9 According to Gershevitch 1959: 184, OP 
<..-r-t-i-y-i-y> (DB 4.44) rather reads *vratiyaiy ‘I swear, take an oath’. = Kent: 
207 

Pres.: IND. 1sg. med. “vartaiyaiy OP <[v]-r-t-i-y-i-y-> (DB 4.44) 

*MIDDLE PERSIAN: MMP (intr.) wrd-, BMP wlt- /ward-/ ‘to turn; twist; writhe [intr. ], 
be tormented’, (caus.) BMP wit’n- /wardan-/, BMP wityn- /wardén-/ ‘to cause to 
change, turn, convert’ || (+ *uz-) ? MMP ‘zwrd- ‘to return to the body, be reborn; to 
turn back, revert, renege’ || (+ *ham-) MMP "mwrd- ‘to turn ёо’ = DMMPP: 344b, 
102b, 40b 

Widely attested: Pres.: IND. 1sg. BMP wltym /wardém/, 25р. BMP wityh /warde/, 3sg. MMP wrdyd etc. || 
(+ *uz-) Pres.: IND. 3pl. MMP ‘zwrdynd; Partic.: perf. pass. MMP ‘zwstg’n (pl.) || (+ *ham-) Pres.: IND. 
3sg. MMP ’mwrdyd, IMPV. 25р. ‘туга; Partic.: perf. pass. ’mwst 

*PARTHIAN: wrt-, wrd- ‘to turn, twist, writhe’? || (+ *a-) ’C)whr- ‘to turn to, be 
converted’ || (+ *uz-) ‘zwrt- ‘to turn back, return’ || (+ *ham-) ’mwrd- ‘to gather, 
collect, heap’ — Ghilain: 53 f. | DMMPP: 345a, 5b, 102b, 40b 
wcy-. The form may be connected to the root *uart. > Samadi: 212, 217, 9 f., 30, 
264 f., 156, 132, 216 f. 

*NWIR: NP gardun ‘wheel; chariot’, Kurd. (Kurm.) bar (m.), (Sor.) bard, Bakht. bard, 
berd, Siv. värd(e), Yzd. (Zor.) bard ‘stone’, ? NP /aj-vard ‘lapis lazuli’ || (+ *uz-) 
Kurd. (Kurm.) zivirin ‘to turn, be spinning’ || (+ *ni-) NP nawardidan/naward- ‘to 
fold, cease; to twist; to stroll’ 

*NEIR: Oss. I. waerdyn/weerst, D. waerdun/weerst ‘to felt’, Bart. warwar0-/warwuxt 
‘to turn round [intr.]’, warwax-/warwext ‘to turn round [tr.]’ (with redupl. ?), Yi. 
wor-/wusc- ‘to knit’, M. war-/wusk- ‘to stretch the warp on the loom’ (Zarubin) || (+ 
*а-) Pash. awustol/awarom ‘to turn, change, revolve’ || (+ *uz-) Yghn. ziwört-, 
züwört-/ziwörta ‘to turn around, return [intr.]’, zıwirt-/ziwirta ‘to turn back, around 
[tr.] || (+ *para-) Sh. (Baj.) parwar0-/parwuxt ‘to slide down, fall into water with an 
inflated skin for swimming’, parwáx-/parwáxt (caus.) ‘to push, force into water for 
swimming on an inflated skin’, Bart. parward-/parwext ‘to turn upside down’ (less 
likely from *рап-) || (+ *fra-) Oss. D. lewardun/lewarst ‘to go through a certain 
mass [snow, earth], sweeping with the feet’ || (+ *ni-) Oss. I. nywerdyn/nywerst, 
nordyn/norst, D. niweerdun/niwarst ‘to wrap up’, Pash. nwaray (m.) ‘a doubled-over 
hem; draw-string’ || (+ *ham-) Oss. L ewwerdyn/ewwerst, D. zwwardun/ 
zewwarst ‘to knead, smear, rub in’ 

*MISC: Orm. ger-/gerök ‘to roll’, (caus.) Orm. g(e)raw-/g(e)rawök ‘to cause to roll’ 
*SANSKRIT: vart ‘to turn (around), to roll’ (RV+) > EWAia II: 518 

PIE *uert- ‘to turn’ = LIV: 691 f. | Pok.: 1156 ff.
```


## [2026-09-07T19:44:18.552Z] TOOL CALL #93: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '15045,15060p' CHEUNG.txt; echo \"=== NWIR jan\"; awk 'NR>=15045 && NR<=15140' CHEUNG.txt | grep -n \"NWIR\\|nazand\\|nizand\\|PIE\" ; echo \"===== kas 16362\"; sed -n '16360,16372p' CHEUNG.txt",
 "description": "Cheung jan and kas"
}
```


### [2026-09-07T19:44:19.826Z] TOOL RESULT

```
Han ‘to kill, slay, strike’ 

*AVESTAN: jan- (yn-) ‘to kill, slay’ || (+ *aua-) ‘to kill’ || (+ *upa-) ‘to nudge, touch 
upon’ || (+ *pati-) ‘to strike, hit (with a weapon) against’ || (+ *ni-) ‘to strike down’ 
= Liste: 23 

Pres. {1} athem.: IND. 1sg. med. YAv. niyne (Yt 4.5), 3sg. YAv. jainti (V 13.8, Yt 17.20, Yt 3.10 ff., 
etc.), med. YAv. niyne (Y 10.2, Y 57.29, Yt 10.104), 3pl. YAv. "niyninti (Yt 10.133), 3р1. med. *niynaire 
(Yt 10.40), SUBJ. 1sg. ҮАУ. janani (V 19.5, Yt 4.5, Yt 15.28), 3sg. ҮАУ. janat (Yt 19.26, Yt 19.41 ff), 
Ipl. YAv. janama (Y 61.5), OPT. 2sg. YAv. janiià (Yt 10.2), 3sg. YAv. janiiat (V 18.12), YAv. 
auua.janiiat (V 14.5 f., V 16.12, V 18.73, V 19.41), Y Av. upa.janiiät (V 5.11), med. Y Av. paiti.ynita (Yt 
13.67), 3р1. med. ? Y Av. "jan(a)iianta (Vn 112), IMPV. 25р. ҮАУ. jaiói (Y 9.30 ff.), 3sg. YAv. jantu (V); 
Pres. (2) them.: IND. 3sg. YAv. janaiti (V 5.2, V 5.34, V 15.5), INJ. 3pl. YAv. janon (Yt 14.56), SUBJ. 
3sg. Y Av. janaiti (Yt 2.11), Y Av. janat (Y 9.24, Yt 3.14 ff., 9.18, etc.), 3sg. med. Y Av. nijanaite (V 9.56), 
ОРТ. 3sg. med. YAv. auua.janaöta (V 16.12), 3pl. YAv. айпа janaiion (V 8.74); Partic.: pres. ҮАУ. 
=== NWIR jan
74:*NWIR: Widely attested: NP zadan/zan-, Zaz. jinayis/jinen-, Gz. Zen-/Zent ‘to beat, 
===== kas 16362
look at’ © Samadi: 56, 4, 21, 192 f., 128 

*NWIR: Khuns. kis-/kis(s)- ‘to look to’ || (+ *а-) NP agah ‘knowing, aware’ || (+ *ni-) 
Meim. be-Agaft-, a-Agaft-/a-Ages- ‘to look to, gaze at’, NP пісар ‘look, attention’ || 
(+ *ham-) Fariz. -ängast-/-ängäs-, Yar. -ängäst-/-ingäs- ‘to look’, Qohr. t-ángis-/ 
angas, Soi at-ängis- ‘look to, perceive’, ? Jow. bam-gaft/afiges- ‘to paint’ 

*NEIR: Oss. I. k&syn/kast, D. keesun/kast ‘to look; to read; to wait; to appear’, Pash. 
katol, Sh. Cis-/Cuxt, Rosh. cas-/Coxt, Bart. Cas-/é6xt, Sariq. Cos-/EiXt, Yzgh. k'as-/ 
k’üxt ‘to see’, ? Yi. kös-/kist ‘to search for’ (rather *kau£? ?) || (+ *pari-) Oss. L 
felgesyn/felgest, D. felgasun/felgast ‘to look; survey’ || (+ *nis-) Oss. I. 
nykkesyn, D. nikkesun ‘to look (down)’ || (+ *ham-) Oss. І. angas, D. zngast 
‘look, appearance’
```


## [2026-09-07T19:44:30.402Z] TOOL CALL #94: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^NEST\\|^nest,\" SKT.txt | head -3; grep -n -A6 \"^NEST\" SKT.txt | head -20; echo \"=== PIE for Han\"; awk 'NR>=15045 && NR<=15140' CHEUNG.txt | grep -n \"PIE \\*\" ",
 "description": "Skeat nest, Cheung Han PIE"
}
```


### [2026-09-07T19:44:31.716Z] TOOL RESULT

```
12225:NEST.
12225:NEST.
12226-303
12227-Swed.  na/ve,  Dan.  ff«/tY.  Lit.  'dosed'  hand . allied  to  Gk.  nva^vrtiv,  to  crook,  bend. Neigh.  (E.)    M.  £.  MfVM-  A.S.AM«i>^M, to  neigh  ;  lui  imitative  word. 4-IceL ^1^070,
12228-fuym,  to  ucigh.
12229-nog  (i),  a  horse.  (O.  Low  G.)     M.  K. wa^v.  —  O.  Du.    nfSX^''    f^SS*'    •    MnuU horse,  lit.  '  ncigher.'    Irom  the  veib  above- Neighbour  ;  see  Nigh  aad  Boor.
12230-Neither;  sec  No(i).
12231-Nemesis ;  see  Nomad.
=== PIE for Han
```


## [2026-09-07T19:44:36.219Z] TOOL CALL #95: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Nest\\b\" SKT.txt | head -5; echo ---; grep -n \"nizdo\\|ni-zdo\\|nisdo\" SKT.txt | head -5; echo \"=== Han PIE\"; awk 'NR>=15045 && NR<=15160' CHEUNG.txt | grep -n \"«PIE\\|PIE \\*g\\|Pok\" ",
 "description": "Skeat nest entry, Cheung Han PIE"
}
```


### [2026-09-07T19:44:37.458Z] TOOL RESULT

```
---
=== Han PIE
98:«PIE *g""en- ‘to slay, kill’ > LIV: 218 f. | Pok.: 491 ff.
```


## [2026-09-07T19:44:48.160Z] TOOL CALL #96: Bash

```json
{
 "command": "ls site/pages/365.jpg 2>/dev/null || pdftoppm -f 365 -l 365 -r 150 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg365 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/",
 "description": "Render PDF page 365"
}
```


### [2026-09-07T19:44:49.662Z] TOOL RESULT

```
site/pages/365.jpg
total 32104
drwx------ 2 sfmqrb sfmqrb     4096 Sep  7 15:42 .
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
-rw-rw-r-- 1 sfmqrb sfmqrb   111897 Sep  7 13:57 340hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    24993 Sep  7 13:57 340-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    92337 Sep  7 13:59 342-mid.png
-rw-rw-r-- 1 sfmqrb sfmqrb    92697 Sep  7 13:56 343hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    30778 Sep  7 13:56 343-mid.png
-rw-rw-r-- 1 sfmqrb sfmqrb    61503 Sep  7 13:52 346-zoom.png
-rw-rw-r-- 1 sfmqrb sfmqrb    81599 Sep  7 14:37 350-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    99691 Sep  7 14:40 351-mid.png
-rw-rw-r-- 1 sfmqrb sfmqrb   115624 Sep  7 14:43 355-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    85914 Sep  7 14:35 358hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    19549 Sep  7 14:35 358-mid.png
-rw-rw-r-- 1 sfmqrb sfmqrb    74812 Sep  7 14:35 358-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb  1579505 Sep  7 14:24 afm76.png
-rw-rw-r-- 1 sfmqrb sfmqrb  1055262 Sep  7 14:23 afm77.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1297 Sep  7 15:29 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    14937 Sep  7 11:56 arrows.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1413 Sep  7 12:27 box1b.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1385 Sep  7 12:27 box1.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1132 Sep  7 12:27 box2b.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1988 Sep  7 12:27 box2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    85949 Sep  7 11:57 bqt2002_a.png
-rw-rw-r-- 1 sfmqrb sfmqrb    72256 Sep  7 11:58 bqt2002_f1.png
-rw-rw-r-- 1 sfmqrb sfmqrb   161214 Sep  7 11:57 bqt2002_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   153966 Sep  7 13:44 bqt2014_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   299343 Sep  7 15:34 bqt2173_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    79304 Sep  7 15:38 bqt2195_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    59998 Sep  7 15:38 bqt2210_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    63319 Sep  7 12:40 build333.py
-rw-rw-r-- 1 sfmqrb sfmqrb    83643 Sep  7 12:12 build.py
-rw-rw-r-- 1 sfmqrb sfmqrb     7075 Sep  7 12:13 c331_av1.png
-rw-rw-r-- 1 sfmqrb sfmqrb    10759 Sep  7 12:13 c331_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    11800 Sep  7 14:19 c355_arab2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     7474 Sep  7 14:19 c355_conn.png
-rw-rw-r-- 1 sfmqrb sfmqrb    10501 Sep  7 14:19 c355_runik2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     7270 Sep  7 14:19 c355_runik.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3537 Sep  7 11:53 c_migare2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1829 Sep  7 11:53 c_migare3.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2261 Sep  7 11:53 c_migare4.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3958 Sep  7 11:53 c_migare.png
-rw-rw-r-- 1 sfmqrb sfmqrb    46690 Sep  7 13:44 crop_av3.png
-rw-rw-r-- 1 sfmqrb sfmqrb    40759 Sep  7 13:44 crop_heb.png
-rw-rw-r-- 1 sfmqrb sfmqrb    94819 Sep  7 13:44 crop_pers0.png
-rw-rw-r-- 1 sfmqrb sfmqrb    19652 Sep  7 11:53 c_semita2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2639 Sep  7 11:53 c_semita.png
-rw-rw-r-- 1 sfmqrb sfmqrb    40259 Sep  7 11:50 ferdowsi2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    30950 Sep  7 11:51 ferdowsi3.png
-rw-rw-r-- 1 sfmqrb sfmqrb    28946 Sep  7 11:51 ferdowsi4.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4298 Sep  7 11:50 ferdowsi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    78732 Sep  7 13:40 ffd32.png
-rw-rw-r-- 1 sfmqrb sfmqrb    30152 Sep  7 15:34 ffd77_bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    61328 Sep  7 15:34 ffd77.png
-rw-rw-r-- 1 sfmqrb sfmqrb    61328 Sep  7 13:44 ffd82.png
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
-rw-rw-r-- 1 sfmqrb sfmqrb    83271 Sep  7 13:58 mk338.py
-rw-rw-r-- 1 sfmqrb sfmqrb    74349 Sep  7 13:57 mk340.py
-rw-rw-r-- 1 sfmqrb sfmqrb    59512 Sep  7 13:57 mk341.py
-rw-rw-r-- 1 sfmqrb sfmqrb    82502 Sep  7 13:57 mk342.py
-rw-rw-r-- 1 sfmqrb sfmqrb    66284 Sep  7 13:55 mk343.py
-rw-rw-r-- 1 sfmqrb sfmqrb    58811 Sep  7 13:57 mk344.py
-rw-rw-r-- 1 sfmqrb sfmqrb    36436 Sep  7 13:51 mk348b.py
-rw-rw-r-- 1 sfmqrb sfmqrb    20510 Sep  7 13:47 mk348.py
-rw-rw-r-- 1 sfmqrb sfmqrb    67410 Sep  7 14:53 mk353.py
-rw-rw-r-- 1 sfmqrb sfmqrb    87481 Sep  7 14:40 mk354.py
-rw-rw-r-- 1 sfmqrb sfmqrb    38634 Sep  7 14:34 mk358.py
-rw-rw-r-- 1 sfmqrb sfmqrb    61503 Sep  7 13:42 navak2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3021 Sep  7 13:42 navak.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1525 Sep  7 13:41 p342_box2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1759 Sep  7 13:41 p342_box3.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1703 Sep  7 13:41 p342_box.png
-rw-rw-r-- 1 sfmqrb sfmqrb   108903 Sep  7 13:41 p342hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    10531 Sep  7 13:39 p343_lat.png
-rw-rw-r-- 1 sfmqrb sfmqrb    30408 Sep  7 13:39 p343_mus.png
-rw-rw-r-- 1 sfmqrb sfmqrb   103027 Sep  7 14:19 p355hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    86505 Sep  7 14:27 p358_av.png
-rw-rw-r-- 1 sfmqrb sfmqrb   114524 Sep  7 14:19 p358hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    37883 Sep  7 14:20 p358_q2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    36134 Sep  7 14:20 p358_q3.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4274 Sep  7 14:19 p358_quote.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4789 Sep  7 15:38 p361_empty2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4152 Sep  7 15:38 p362_empty.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3458 Sep  7 15:35 p362_germ1.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2606 Sep  7 15:35 p362_germ2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   135659 Sep  7 15:34 p363_mid.png
-rw-rw-r-- 1 sfmqrb sfmqrb   223838 Sep  7 15:34 p363_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    13022 Sep  7 15:42 p366_empty.png
-rw-rw-r-- 1 sfmqrb sfmqrb    21223 Sep  7 13:47 part1.json
-rw-rw-r-- 1 sfmqrb sfmqrb    37635 Sep  7 12:04 part_a.json
-rw-rw-r-- 1 sfmqrb sfmqrb    58545 Sep  7 12:09 part_b.json
-rw-rw-r-- 1 sfmqrb sfmqrb     5736 Sep  7 14:43 patch354.py
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
-rw-rw-r-- 1 sfmqrb sfmqrb    63922 Sep  7 13:44 pg339.png
-rw-rw-r-- 1 sfmqrb sfmqrb   111897 Sep  7 13:44 pg340hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    64116 Sep  7 13:39 pg341.png
-rw-rw-r-- 1 sfmqrb sfmqrb    75149 Sep  7 13:40 pg342.png
-rw-rw-r-- 1 sfmqrb sfmqrb    64151 Sep  7 13:39 pg343.png
-rw-rw-r-- 1 sfmqrb sfmqrb    60735 Sep  7 13:42 pg344.png
-rw-rw-r-- 1 sfmqrb sfmqrb   168870 Sep  7 13:42 pg346hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    76794 Sep  7 13:39 pg346.png
-rw-rw-r-- 1 sfmqrb sfmqrb    59757 Sep  7 14:29 pg349.png
-rw-rw-r-- 1 sfmqrb sfmqrb    70743 Sep  7 14:25 pg350.png
-rw-rw-r-- 1 sfmqrb sfmqrb    86553 Sep  7 14:25 pg351.png
-rw-rw-r-- 1 sfmqrb sfmqrb    69045 Sep  7 14:18 pg355.png
-rw-rw-r-- 1 sfmqrb sfmqrb    78195 Sep  7 14:27 pg357.png
-rw-rw-r-- 1 sfmqrb sfmqrb    49496 Sep  7 14:19 pg358.png
-rw-rw-r-- 1 sfmqrb sfmqrb    82867 Sep  7 15:38 pg359.png
-rw-rw-r-- 1 sfmqrb sfmqrb    45536 Sep  7 15:36 pg360.png
-rw-rw-r-- 1 sfmqrb sfmqrb    57895 Sep  7 15:38 pg361.png
-rw-rw-r-- 1 sfmqrb sfmqrb   111691 Sep  7 15:34 pg362hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    76202 Sep  7 15:29 pg362.png
-rw-rw-r-- 1 sfmqrb sfmqrb    66511 Sep  7 15:33 pg363.png
-rw-rw-r-- 1 sfmqrb sfmqrb    49805 Sep  7 15:37 pg364.png
-rw-rw-r-- 1 sfmqrb sfmqrb    59224 Sep  7 15:34 pg367.png
-rw-rw-r-- 1 sfmqrb sfmqrb    49419 Sep  7 15:35 pg368.png
-rw-rw-r-- 1 sfmqrb sfmqrb        0 Sep  7 13:36 queue.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  3120575 Sep  7 14:24 skeat1882.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  2985742 Sep  7 14:25 skeatdli.txt
-rw-rw-r-- 1 sfmqrb sfmqrb       49 Sep  7 14:29 sns_0022.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb       49 Sep  7 14:29 sns_0158.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb       49 Sep  7 12:17 sns53.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4676 Sep  7 14:29 sns_meta.json
-rw-rw-r-- 1 sfmqrb sfmqrb   135853 Sep  7 14:30 sns_n157.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   129673 Sep  7 14:30 sns_n159.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   113320 Sep  7 14:30 sns_n21.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb    35039 Sep  7 12:17 sns_n53.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb    35039 Sep  7 12:17 sns_n54.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  1021826 Sep  7 12:18 sns_p54.png
-rw-rw-r-- 1 sfmqrb sfmqrb 12288786 Sep  7 12:18 sns_text.pdf
-rw-rw-r-- 1 sfmqrb sfmqrb      341 Sep  7 13:46 s.py
-rw-rw-r-- 1 sfmqrb sfmqrb   116699 Sep  7 14:30 t1.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb     1308 Sep  7 11:54 v2001.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    27253 Sep  7 12:02 z_maqd2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    63140 Sep  7 12:02 z_maqd3.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4293 Sep  7 12:01 z_maqd.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2895 Sep  7 12:01 z_meh.png
-rw-rw-r-- 1 sfmqrb sfmqrb    25378 Sep  7 12:01 z_mezna2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    33685 Sep  7 12:01 z_mezna.png
```


## [2026-09-07T19:44:53.222Z] TOOL CALL #97: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/site/pages/365.jpg"
}
```


### [2026-09-07T19:44:53.253Z] TOOL RESULT

```

```


## [2026-09-07T19:45:07.435Z] TOOL CALL #98: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && pdftoppm -f 365 -l 365 -r 300 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf pg365 && python3 - <<'EOF'\nfrom PIL import Image\nim=Image.open('pg365.png'); print(im.size)\nw,h=im.size\n# node 8 row approx y 830-910 of 1400-high render earlier (jpg was ~1400). scale\nim.crop((int(w*0.24),int(h*0.56),int(w*0.80),int(h*0.66))).resize((int(w*0.56*1.6),int(h*0.10*1.6))).save('p365_row8.png')\nEOF\nls -la p365_row8.png",
 "description": "Crop node 8 row"
}
```


### [2026-09-07T19:45:09.813Z] TOOL RESULT

```
(2550, 3300)
-rw-rw-r-- 1 sfmqrb sfmqrb 118891 Sep  7 15:45 p365_row8.png
```


## [2026-09-07T19:45:12.947Z] TOOL CALL #99: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/p365_row8.png"
}
```


### [2026-09-07T19:45:13.086Z] TOOL RESULT

```

```


## [2026-09-07T19:45:13.082Z] INPUT

[Image: original 2284x528, displayed at 2000x462. Multiply coordinates by 1.14 to map to original image.]


## [2026-09-07T19:45:23.850Z] TOOL CALL #100: Bash

```json
{
 "command": "mkdir -p data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg365.png data/verification/sources/refs/ocr/BOOK/365.png && for u in \"https://www.etymonline.com/word/nest\" \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/n%C3%AD\" \"https://en.wiktionary.org/wiki/%D9%86%D9%87%D8%A7%D8%AF%D9%86\" \"https://en.wiktionary.org/wiki/%D9%86%D9%88%D8%B4%D8%AA%D9%86\"; do python3 tools/fetch_source.py \"$u\" --note \"page 365 root Ni 1: nest/PIE *ni-/nihādan/nivištan\"; done",
 "description": "Archive more sources"
}
```


### [2026-09-07T19:45:28.602Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/0d03fff0f8ebeed1.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/6f4ea1e0551664dc.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/060cb2e73004300f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/0ce8302405d24324.txt
```


## [2026-09-07T19:45:34.113Z] TOOL CALL #101: Bash

```json
{
 "command": "cd data/verification/sources/web && echo \"#### etymonline nest\"; grep -n -i -m1 -A8 \"nest (n.)\" 0d03fff0f8ebeed1.txt | head -20; echo \"#### PIE ni\"; grep -n -m2 -A10 \"Etymology\\b\" 6f4ea1e0551664dc.txt | head -30; echo \"#### nihadan\"; grep -n -m1 -A8 \"^ Etymology$\" 060cb2e73004300f.txt | head; echo \"#### nivistan\"; sed -n '/Persian/,$p' 0ce8302405d24324.txt | grep -n -m1 -A10 \"Etymology\" | head -20",
 "description": "Read newly archived pages"
}
```


### [2026-09-07T19:45:35.413Z] TOOL RESULT

```
#### etymonline nest
23: nest (n.) 
24-
25- "structure built by a bird or domestic fowl for the insulation and rearing of its young," Old English nest "bird's nest; snug retreat," also "young bird, brood," from Proto-Germanic *nistaz (source also of Middle Low German, Middle Dutch nest , German Nest ; not found in Scandinavian or Gothic), from PIE *nizdo- (source also of Sanskrit nidah "resting place, nest," Latin nidus "nest," Old Church Slavonic gnezdo , Old Irish net , Welsh nyth , Breton nez "nest"), probably from *ni "down" + from PIE root *sed- (1) "to sit."
26-
27- From c. 1200 of an animal or insect. Used since Middle English in reference to various accumulations of things, especially of diminishing sizes, each fitting within the next (such as a nest of drawers , early 18c.). Nest egg "retirement savings" is from 1700; it was originally "a real or artificial egg left in a nest to induce the hen to go on laying there" ( nest ei , early 14c.), hence "something laid up as the beginning of a continued growth."
28-
29- nest (v.) 
30-
#### PIE ni
62: Etymology 
63-
64- 1.2 
65- Adverb 
66-
67- 1.2.1 
68- Derived terms 
69-
70- 1.2.2 
71- Descendants 
72-
--
137: Etymology
138- [ edit ] 
139-
140- Possibly from *h₁én / *én ( “ in ” ) . [ 1 ] 
141-
142- Adverb
143- [ edit ] 
144-
145- *ní [ 1 ] [ 2 ] [ 3 ] 
146-
147- down 
#### nihadan
146: Etymology
147- [ edit ] 
148-
149- From Middle Persian [script needed] ( HNHTWN-tn' /⁠nihādan⁠/ ) , from Proto-Iranian *ni- + *dádaHtī ( from Proto-Indo-Iranian *dʰádʰaHti , from Proto-Indo-European *dʰédʰeh₁ti ) . Compare Northern Kurdish nan , niyan , nihan ( “ to put ” ) , Central Kurdish نان ( nan , “ to put ” ) , Zazaki naene . Northern Luri نیاٸه ( nyae ) , Bakhtiari نݖاڊن ( naaḍen ) .
150-
151- Pronunciation
152- [ edit ] 
153-
154- ( Classical Persian ) IPA ( key ) : /ni.haː.ˈdan/ 
#### nivistan
9: Etymology 
10-
11- 1.3 
12- Pronunciation 
13-
14- 1.4 
15- Verb 
16-
17- 1.4.1 
18- Conjugation 
19-
```


## [2026-09-07T19:45:41.063Z] TOOL CALL #102: Bash

```json
{
 "command": "cd data/verification/sources/web && grep -n -A6 \"^ Etymology$\" 0ce8302405d24324.txt | grep -i -m3 -B1 -A4 \"Middle Persian\\|Old Persian\" | head -20",
 "description": "Read nivistan etymology"
}
```


### [2026-09-07T19:45:42.505Z] TOOL RESULT

```
169-
170- From Middle Persian npštn' ( nibištan , “ to write ” ) , from Proto-Indo-Iranian *ní ( “ downwards, into ” ) + Middle Persian *pištan- , the latter from Old Persian *pi⁽ⁿ⁾θ- , from Proto-Iranian *pais- ( “ to adorn, paint, write ” ) , from Proto-Indo-European *peyḱ- ( “ to cut out; to stitch; to paint, mark ” ) . [ 1 ] Doublet of نِبی ( nibī , “ scripture ” ) , and cognate with Russian написать ( napisatʹ , “ to write ” ) and English paint , picture . [ 2 ] 
171-
172- Pronunciation
173- [ edit ]
```


## [2026-09-07T19:46:43.516Z] TOOL CALL #103: Bash

```json
{
 "command": "sed -n '1,120p' tools/verify_check.py",
 "description": "Read verify_check.py"
}
```


### [2026-09-07T19:46:43.561Z] TOOL RESULT

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


## [2026-09-07T19:54:50.366Z] TOOL CALL #104: Write

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/page-365.json",
 "content": "{\n  \"pdf_page\": 365,\n  \"book_page\": 335,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-07\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Nî 1\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *ni- 'down, below' (adverb/verbal prefix), comparative *ni-tero- 'lower'; Pokorny treats it inside 1. en- 'in', IEW 311-314; Watkins/AHD lemma 'ni. Down.'\",\n      \"note\": \"Root, language label and gloss are all right, and KLN:1042 is the exact page. The only quibble is the vowel length: Nourai writes the root 'Nî' with a long/circumflexed vowel, which is the Avestan shape (Av. nī), while the reconstructed IE adverb is short *ni (Skt. ní, Arm. ni-, OCS ni-zŭ); Walde-Pokorny II 335 heads the lemma 'ni, nei- \\\"nieder\\\"'. Cross-cutting remarks: (1) the chart's whole Iranian side — ni- as a live verbal prefix producing nešastan, nevištan, nahādan, niyūšīdan, negāh, nemūdan, nabard, našib, niyāz, navardīdan — is exactly what Horn, Hübschmann, MacKenzie, Mo'in's footnotes in Borhan-e Qate', Cheung and Gharib all give, and Mo'in states the principle verbatim s.v. نوشتن (BQT 2201): «نخست نی ni جزئی (پیشوند) است بمعنی فرود و پایین که در سرِ لغات نهفتن و نهادن و نشستن و بسیاری از لغات دیگر فارسی هم دیده می‌شود»; (2) three of Nourai's own cross-reference roots are mis-assigned — 'Ôus 1' for ni-gaoša (Pokorny puts Av. gaoša- under an Indo-Iranian-only lemma ghous- 454, not under *ous- 'ear' 785) and, more seriously, 'Angh' for ni-az (Cheung derives niyāz from *ni-Haz 'to drive down, straiten', PIE *h₂eǵ-, Pokorny 4 ff., not from *anǵʰ- 'narrow', Pokorny 42); (3) three items in the Iranian boxes are unattested reconstructions marked with an asterisk in Horn but printed without one by Nourai (*ni-xšvaēpa-, *ni-parət-, *ni-gāma-); (4) on the printed page the Avestan/SOD box (node 8) has an arrow into an EMPTY, unlabelled box on the right which the JSON does not record.\",\n      \"note_fa\": \"ریشه، برچسب زبان و معنی هر سه درست است: پوکورنی این پیشوند را ذیل «1. en-» در صفحه‌های ۳۱۱ تا ۳۱۴ می‌آورد («ni-, nei- \\\"low, base\\\", comparative nitero-»: سنسکریت ní، اوستایی nī «فرود، به‌سوی پایین»، ارمنی ni-، آلمانی علیای کهن nidar) و والده-پوکورنی در جلد دوم صفحهٔ ۳۳۵ همان را با سرواژهٔ «ni, nei- \\\"nieder\\\"» ثبت کرده؛ واتکینز نیز ریشهٔ «ni. Down.» را دارد و کلاین در صفحهٔ ۱۰۴۲ ذیل nether می‌نویسد «prop. comparatives formed fr. I.-E. *nī-, \\\"down, below\\\", whence OI. ni, Avestic ni». تنها ایراد خردِ کتاب، کشیدگی واکه است: صورت بازسازی‌شدهٔ هندواروپایی *ni کوتاه است و «Nî» با واکهٔ کشیده صورت اوستایی است. سراسرِ بخش ایرانی نمودار — «نشستن، نوشتن، نهادن، نیوشیدن، نگاه، نمودن، نبرد، نشیب، نیاز، نوردیدن» — با هرن، هوبشمان، مکنزی، حواشی معین در برهان قاطع، چونگ و قریب یکسر همخوان است؛ خودِ معین در حاشیهٔ «نوشتن» (برهان ۲۲۰۱) همین اصل را صریح گفته است. سه ارجاعِ درون‌متنیِ نورایی نادرست است: «Ôus 1» برای ni-gaoša (پوکورنی gaoša- را ذیل ghous- ص ۴۵۴ می‌آورد، نه ذیل *ous- «گوش» ص ۷۸۵) و به‌ویژه «Angh» برای ni-az (چونگ «نیاز» را از *ni-Haz «به‌زیر راندن، در تنگنا نهادن»، هندواروپایی *h₂eǵ-، پوکورنی ص ۴ می‌گیرد، نه از *anǵʰ- «تنگ» ص ۴۲). همچنین سه صورت (ni-xšvaēpa-، ni-parət-، ni-gāma-) در هرن با ستاره و «نامسلّم» آمده ولی نورایی بی‌ستاره چاپ کرده است.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/n%C3%AD\",\n        \"https://www.etymonline.com/word/nest\"\n      ],\n      \"ref_check\": [\n        {\n          \"ref\": \"KLN:1042\",\n          \"status\": \"supports\",\n          \"note\": \"Klein 1966 vol. II s.v. 'nether' (KLN_1966.txt line 25303, between the OCR page markers 1040 and 1046, i.e. p.1042): \\\"nether, adj., lower. — ME. nethere, nithere, fr. OE. neodera ... prop. comparatives formed fr. I.-E. *nī-, 'down, below', whence OI. ni, 'down', nitaram, 'downwards', nica, 'below, down' ... Avestic ni, 'down', Arm. ni, n-, 'low', Gk. veioθεν, 'from below' ... OSlav. ni-zu, 'low, down'. Cp. I.-E. *ni-zdo- (in L. nidus, OE. nest, etc.), 'nest', lit. 'a place to sit down in'.\\\" The same page carries 'nest' (line 25295).\"\n        }\n      ],\n      \"consulted\": [\n        {\n          \"src\": \"POK\",\n          \"where\": \"IEW 311-314, lemma 1. en-, section 'ni-, nei-'\",\n          \"stance\": \"supports\",\n          \"note\": \"POK_full.txt lines 26659-26858: \\\"ni-, nei- 'low, base', comparative nitero- 'low' (in contrast to 'upper'): Old Indic ní, Avestan nī 'down; downward', Old Indic nitaram 'underneath', Avestan nitama- 'the lowest'; Armenian ni-, n- 'low'; ... Old High German nidar, Old Saxon nithar, Old English niþer, Old Icelandic niðr 'down; downward' ... compare Indo Germanic ni-zdos 'nest' under sed- 'sit, place'.\\\" References: WP. I 125 ff., II 335 f. Page(s): 311-314.\"\n        },\n        {\n          \"src\": \"WLD\",\n          \"where\": \"Walde-Pokorny Bd. II 335 (WLD_Bd2_pages.txt leaf 339)\",\n          \"stance\": \"supports\",\n          \"note\": \"\\\"ni, nei- 'nieder', Komp. nitaro- 'nieder' (im Gegensatz zu 'oberer'). Ai. ní, av. nī 'nieder(wärts)', ai. nitaram 'unterwärts', av. nitama- 'der unterste'; arm. ni-, n- 'nieder'; ahd. nidar, as. nithar, ags. niþer, aisl. niðr 'niederwärts' ... abg. nizŭ 'hinab, hinunter'.\\\"\"\n        },\n        {\n          \"src\": \"AHD\",\n          \"where\": \"Watkins 1985, s.v. ni\",\n          \"stance\": \"supports\",\n          \"note\": \"\\\"ni. Down. 1. Suffixed form *ni-t- in Germanic *nith- in Old English nithan, neothan, below: BENEATH, UNDERNEATH. 2. Suffixed (comparative) form *ni-tero-, lower, in Germanic *nitheraz in Old English nither, lower: NETHER. See compound root nizdo-. [In Pok. 1. en 311.]\\\"\"\n        },\n        {\n          \"src\": \"SYN\",\n          \"where\": \"Buck, Dictionary of Selected Synonyms, s.v. 'low/nether' (SYN.txt line 21804)\",\n          \"stance\": \"supports\",\n          \"note\": \"\\\"OE niþerlic, fr. niþer adv. 'down, beneath, below' = OHG nidar ... : Skt. nitaram 'downwards', comparative formation to IE *ni-, *nei- in Skt. nī-, Av. ni- 'down', Av. nitama- 'lowest', ChSl. nizŭ 'down', etc. Walde-P. 2.335.\\\"\"\n        }\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan / Old Persian\",\n          \"words\": \"ni 1\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Both Avestan and Old Persian keep the inherited adverb/preverb unchanged: Av. nī, OP ni- 'down' (< PIE *ni), used adnominally with the locative and, far more often, as a verbal prefix. Kent's Old Persian lexicon has the entry verbatim: \\\"ni- prep. and verbal prefix 'down': Av. ni, Skt. ni-, pIE *ni; in adv. nipadiy, and with verbs ar-, kan-, cay-, paiθ-, yam-, stā-, had-\\\" (KNT.txt line 5606); the phrasal adverb nipadiy 'down on the track of' (DB 3.73) is its only free-standing use in the inscriptions. Beside the plain prefix, Old Iranian also formed nij-/niž- < *ni + s (OP nij-āyam 'I went forth', Av. niz-bərəta-), which is not on this chart. So the arrow root → node is trivially right; the box is simply the Old Iranian reflex of the root.\",\n          \"derivation_fa\": \"پیشوندِ ارثی در هر دو زبانِ ایرانیِ باستان دست‌نخورده مانده است: اوستایی nī و پارسی باستان ni- «فرود، پایین»، از هندواروپاییِ آغازین *ni. کنت در واژه‌نامهٔ پارسی باستان می‌نویسد: «ni- حرف اضافه و پیشوندِ فعلی «پایین»: اوستایی ni، سنسکریت ni-، هندواروپایی *ni؛ در قید nipadiy و با فعل‌های ar-, kan-, cay-, paiθ-, yam-, stā-, had-». معین نیز در حاشیهٔ «نوشتن» (برهان قاطع ۲۲۰۱) همین را می‌گوید. ادعای نورایی در این جعبه درست است و تنها صورتِ ایرانیِ باستانِ همان ریشه را نشان می‌دهد.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/n%C3%AD\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"KLN:1042\",\n              \"status\": \"supports\",\n              \"note\": \"Klein s.v. 'nether' (KLN_1966.txt line 25303) lists exactly this reflex: \\\"whence OI. ni, 'down' ... Avestic ni, 'down'\\\".\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"KNT\",\n              \"where\": \"Kent, Old Persian, Lexicon s.v. ni- (KNT.txt line 5606); §115 and §120 for nij-\",\n              \"stance\": \"supports\",\n              \"note\": \"\\\"ni- prep. and verbal prefix 'down': Av. ni, Skt. ni-, pIE *ni; in adv. nipadiy, and with verbs ar-, kan-, cay-, paiθ-, yam-, stā-, had-\\\"; §115: \\\"The Aryan prefix *niš, from pIE *ni + s, became niž before voiced stops, as in Av. niz-bərəta- ... and is written nij- in OP nij-āyam 'I went forth'\\\".\"\n            },\n            {\n              \"src\": \"POK\",\n              \"where\": \"IEW 311-314 (1. en-), 'ni-, nei-' section\",\n              \"stance\": \"supports\",\n              \"note\": \"\\\"Old Indic ní, Avestan nī 'down; downward' ... also in verbal prefix Aryan ni- 'in, into', e.g. Old Indic nigam-, Avestan nigam- 'enter into a condition'\\\".\"\n            },\n            {\n              \"src\": \"BQT\",\n              \"where\": \"Borhan-e Qate' p. 2201, Mo'in's footnote 1 s.v. نوشتن\",\n              \"stance\": \"supports\",\n              \"note\": \"«نخست نی ni جزئی (پرفیکس، پیشوند) است بمعنی فرود و پایین که در سرِ لغات نهفتن و نهادن و نشستن و بسیاری از لغات دیگر فارسی هم دیده می‌شود» — Mo'in states the prefix and its meaning exactly as the chart does.\"\n            }\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Avestan / Old Persian\",\n          \"words\": \"ni-jan; ni-had, ni-shidhaiti; ni-xšvaepâ; ni-pais; ni-part; ni-vart\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Six Old Iranian prefix verbs, all independently attested or reconstructed by the standard handbooks. (1) ni-jan- 'to strike down': Av. jan-/γn- with ni- is amply attested (YAv. nijanaite V 9.56, niγne Y 10.2, Yt 4.5, *niγninti Yt 10.133) — Cheung, Etym. Dict. Iranian Verb s.v. *Han 'to kill, slay, strike', which lists precisely \\\"(+ *ni-) 'to strike down'\\\", from PIE *gʷʰen- (Pokorny 491 ff.) = Nourai's 'Gwhen 2'; the secondary sense 'put down > dejected' is the one that survives in NP nažand. (2) ni-had-/ni-šhiδaiti: Av. ni + √had- 'to sit', 3sg. nišhiδaiti, caus. nišādayeiti; OP ni-šad- (caus. imperf. niyašādayam 'I set down', DNa 36, nišādayam XPh 34) — Kent §120/§156 and Nyberg's glossary s.v. nišastan (\\\"Av. [AiW] 1754 ni-šad- < ni-had- = OP (caus. ni-šādaya-)\\\"); Pokorny's sed- (884-887) has \\\"Avestan nishiδaiti\\\" and the compound *ni-zd-os 'nest'. Nourai's spelling 'ni-shidhaiti' is a transliteration of nišhiδaiti. (3) ni-xšvaēpā 'down slope': not attested — Horn no. 1034 reconstructs \\\"aw. *ni-xšvaēpa-, vergl. xšvaēp- (No. 799)\\\" behind MP n(i)šēb, and Mo'in repeats it (BQT 2147 fn. 2); the asterisk belongs on the form. (4) ni-pais- 'to write down': the best-attested member — OP aor. niyapaišam <n-i-y-p-i-θ-m> (DB 4.71), ppp. nipišta- (DB 4.47, XPh 31), inf. nipištanaiy (XV 24), Av. paēs- 'to adorn'; Cheung s.v. *pais 'to adorn, paint; to write' has \\\"(+ *ni-) 'to engrave, inscribe'\\\". (5) ni-part- 'fight down': again reconstructed — Horn no. 1025 gives \\\"aw. *ni + √parət-, pərətənte 'sie kämpfen'; phlv. n(i)part 'Kampf' (AV.)\\\". (6) ni-vart- 'roll down': Av. varət- 'to turn', Skt. ni + √vart- 'to turn back'; Cheung s.v. *uart 'to turn' (PIE *wert-, Pokorny 1156 ff.) lists \\\"(+ *ni-) NP nawardīdan/naward- 'to fold ...; to twist; to stroll'\\\" and Oss. nywærdyn 'to wrap up'. Nourai's cross-refs Gwhen 2, Sed, Peig, Per 3, Wer 2 are all correct root assignments.\",\n          \"derivation_fa\": \"شش فعلِ پیشوندیِ ایرانیِ باستان که همه در دستنامه‌های معیار گواه یا بازسازی شده‌اند. ۱) ni-jan- «فروکوفتن»: در اوستا فراوان آمده (nijanaite، niγne)؛ چونگ ذیل *Han «کشتن، زدن» صریح «(+ *ni-) to strike down» دارد و ریشهٔ هندواروپایی را *gʷʰen- (پوکورنی ۴۹۱) می‌گیرد، یعنی همان «Gwhen 2»ی نورایی. ۲) ni-had-/nišhiδaiti: اوستایی ni + √had-، سببیِ nišādayeiti؛ پارسی باستان ni-šad- با صورتِ سببیِ niyašādayam؛ نیبرگ ذیل nišastan به بارتولومه ستون ۱۷۵۴ ارجاع می‌دهد و پوکورنی در ص ۸۸۴ ذیل sed- «Avestan nishiδaiti» را می‌آورد. ۳) ni-xšvaēpā «سراشیب»: گواه ندارد؛ هرن (شمارهٔ ۱۰۳۴) آن را با ستاره *ni-xšvaēpa- بازسازی کرده و معین همان را در حاشیهٔ «نشیب» (برهان ۲۱۴۷) نقل می‌کند؛ پس ستاره جای خود را می‌خواهد. ۴) ni-pais- «نوشتن»: مستندترین عضو؛ پارسی باستان niyapaišam، nipišta-، nipištanaiy در سنگ‌نبشته‌های داریوش و خشایارشا. ۵) ni-part- «نبرد»: بازسازیِ هرن (شمارهٔ ۱۰۲۵) از *ni + √parət- با پهلویِ n(i)part. ۶) ni-vart- «درنوردیدن»: اوستایی varət-، سنسکریت ni-vart-؛ چونگ ذیل *uart (هندواروپایی *wert-، پوکورنی ۱۱۵۶) «(+ *ni-) NP nawardīdan» را می‌آورد. ارجاع‌های درون‌متنیِ نورایی (Gwhen 2، Sed، Peig، Per 3، Wer 2) همه درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D9%86%D9%88%D8%B4%D8%AA%D9%86\",\n            \"https://en.wiktionary.org/wiki/%D9%86%D8%A8%D8%B1%D8%AF\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"POK:884\",\n              \"status\": \"supports\",\n              \"note\": \"Pokorny's lemma sed- 'to sit' is exactly pp. 884-887 (POK_full.txt line 72366, 'Page(s): 884-887'), and the entry contains both members Nourai needs: \\\"identical prefix in Old Indic niṣīdati 'places sich', Avestan nishiδaiti\\\" and \\\"ni-zd-os, -om 'nest' (prefix ni- 'low, base' ... as 'place zum Nieder- or Einsitzen')\\\".\"\n            },\n            {\n              \"ref\": \"BQT:2134\",\n              \"status\": \"supports\",\n              \"note\": \"Borhan-e Qate' p. 2134 (pdf 217 of BQT_v4, printed header ۲۱۳۴) is the نژ / نژاد / نژنگ page whose footnote block runs on to p. 2135 (headword نژند «اندوهگین و غمناک و فرومانده و سرفرود افکنده»); the footnote reads «همچنین در پارسی باستان *nijantu- (خوار کردنی، فروافکندنی) مفروض است» with a reference to Horn's numbered entry — i.e. Mo'in gives precisely Nourai's ni-jan → nažand.\"\n            },\n            {\n              \"ref\": \"BQT:2145\",\n              \"status\": \"supports\",\n              \"note\": \"p. 2145 (pdf 228), footnote 9 s.v. نشستن: «پارسی باستان *ni-šad-، متعدی niyašādayam؛ اوستا ni + √had-، nišhiδaiti (نشستن)، متعدی nišādayeiti؛ پهلوی n(i)šastan، n(i)šīnēt؛ هندی باستان ni + √sad-، sīdati ... رک: اشتقاق ۱۰۳۳ ... هوبشمان ۱۰۳۳» — the same forms as the chart, including 'ni-shidhaiti'.\"\n            },\n            {\n              \"ref\": \"BQT:2147\",\n              \"status\": \"supports\",\n              \"note\": \"p. 2147 (pdf 230), footnote 2 s.v. نشیب: «اوستا *ni-xšvaēpa-، قس nixšvaēpa (رک: شیب)، پهلوی n(i)šēb (فرود شدن) «اشتقاق ۱۰۳۴»» — Horn's no. 1034 quoted, so the Avestan form is Mo'in's/Horn's asterisked reconstruction.\"\n            },\n            {\n              \"ref\": \"BQT:2201\",\n              \"status\": \"supports\",\n              \"note\": \"p. 2201 (pdf 284), footnote 1 s.v. نوشتن: «پهلوی nipištan (= nibēs-)، پارسی باستان *ni-paiš- (نوشتن) «بارتولمه ۸۱۷» ... مرکب است از دو جزء: نخست نی ni پیشوند بمعنی فرود و پایین ... دوم از ریشهٔ paiš در پارسی باستان و paēs در اوستا که بمعنی نگاشتن و نقش کردن است». The same page has نوشتن (fatḥ) «بمعنی درنوردیدن و طی کردن و پیچیدن» with «رک: نوردیدن», covering ni-vart as well.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"CHEUNG\",\n              \"where\": \"Etym. Dict. of the Iranian Verb, s.v. *Han (p.~119), *pais (p.291), *uart (p.423), *hi(n)d\",\n              \"stance\": \"supports\",\n              \"note\": \"*Han: \\\"jan- (γn-) 'to kill, slay' || ... || (+ *ni-) 'to strike down'\\\", PIE *gʷʰen-, Pok. 491 ff.; *pais: \\\"OLD PERSIAN: pai(n)θ- 'to cut, engrave, adorn' || (+ *ni-) 'to engrave, inscribe' — Kent: 194 ... niyapaišam (DB 4.71), nipišta- (DB 4.47), nipištanaiy (XV 24)\\\"; *uart: \\\"(+ *ni-) NP nawardīdan/naward- 'to fold, cease; to twist; to stroll'\\\", PIE *uert-, Pok. 1156 ff.; *hi(n)d: \\\"Av. hiδ- 'to sit' || (+ *ni-) 'to sit down' ... OLD PERSIAN: (+ *ni-) ni-sad- (caus.) 'to establish' = Kent: 212\\\".\"\n            },\n            {\n              \"src\": \"HRN\",\n              \"where\": \"Horn, Grundriss, nos. 1025 (p.230), 1031 (p.231), 1033 (p.231), 1034 (p.231), 1051 (p.235)\",\n              \"stance\": \"supports\",\n              \"note\": \"1025 \\\"neberd 'Kampf' ... aw. *ni + √parət-, pərətənte 'sie kämpfen'; phlv. n(i)part 'Kampf'\\\"; 1031 \\\"nezend ... ap. *ni + √jan- 'niederschlagen', also etwa ein ap. *nijantu- ... Unsicher\\\"; 1033 \\\"nisesten 'sitzen' ... ap. ni + √had-, Caus. niyasādayam; aw. ni + √had-, nišhiδaiti\\\"; 1034 \\\"niseb 'Unteres; unten'. aw. *nixšvaēpa- ... phlv. n(i)šēp\\\"; 1051 \\\"niwišten ... ap. ni + √pais-, nipistanaiy 'schreiben'\\\".\"\n            },\n            {\n              \"src\": \"NYB\",\n              \"where\": \"Nyberg, Manual of Pahlavi II, glossary s.v. nišastan\",\n              \"stance\": \"supports\",\n              \"note\": \"\\\"nišastan [YTYBWN-stn'] nšīn- to sit ... — Av. (1754) ni-šad- < ni-had- = OP (caus. ni-šādaya-); Ps. nšstn nšyd-; MPrth. nšstn nšyl-; MPrs nšstn nšyy-; but Paz. NP nišastan nišīn-\\\" — gives the Bartholomae AiW column (1754) that the OCR of BRT.txt is too corrupt to retrieve.\"\n            },\n            {\n              \"src\": \"KNT\",\n              \"where\": \"Kent, Old Persian §120, §156, Lexicon (KNT.txt lines 518, 1439, 1519, 2503)\",\n              \"stance\": \"supports\",\n              \"note\": \"\\\"ni-šad- from ni- + sad- (Iran. had-)\\\"; \\\"niyašādayam DNa 36, nišādayam XPh 34\\\"; \\\"*peik- 'cut' in ni-paištanaiy 'to inscribe'; *pik- in pte. ni-pištam 'inscribed'\\\"; \\\"OP imf. niyasadayam 'I set down'\\\".\"\n            },\n            {\n              \"src\": \"BRT\",\n              \"where\": \"Bartholomae, AiW cols. 817 (paēs-), 1754 (had-) — cited at second hand\",\n              \"stance\": \"silent\",\n              \"note\": \"The local OCR (BRT.txt) is too degraded to retrieve prefixed headwords: grep for 'nijan', 'nihaδ', 'nipaes', 'xšvaep' returns only fragments (e.g. line 9983 under jan- with \\\"nijainti ... 'nieder-, zu Boden schlagen'\\\"). Mo'in cites AiW 817 for *ni-paiš- and Nyberg AiW 1754 for ni-šad-, both consistent with the chart.\"\n            }\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Persian\",\n          \"words\": \"nažand «نژند»; nešastan «نشستن»; našîb «نشیب»; neveštan «نوشتن»; nabard «نبرد»; navardîdan «نوردیدن» (+ نشیمن، نشیم؛ نورد)\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Five of the six New Persian words are securely the ni- compounds of node 2, all with attested Middle Persian intermediates in MacKenzie's Concise Pahlavi Dictionary (pp. 59-61): nišastan/nišīn- 'sit' > NP نشستن (with the derivatives nišēm 'seat, perch', nišēmag 'residence' > نشیم، نشیمن, which are the chart's parenthetical extras); nišēb 'declivity; astr. dejection' > نشیب; nibištan/nibēs- 'write' > نوشتن (OP nipišta- → MP nibišt, with intervocalic *p > b and *š kept, then NP -b- > -v-/-w-); nibard 'fight, struggle, battle', nibardīdan 'to fight' > نبرد (Av. *ni-parət- → MP nipart/nibard: *rt > rd, *p > b); and ni + *vart- > MP *nawardīdan > NP نوردیدن 'to roll, fold, traverse' (Cheung lists NP nawardīdan under *uart directly, and Mo'in's نوشتن entry, BQT 2201, glosses the fatḥ-vocalised نوشتن as «درنوردیدن و طی کردن و پیچیدن» with a cross-reference to نوردیدن). The weak link is نژند: Horn (no. 1031) proposes OP *ni-jantu- 'niederschlagbar' but expressly adds \\\"Unsicher\\\", and Mo'in only says an Old Persian *nijantu- «مفروض است» ('is assumed'); no attested Iranian form supports the -and suffix, and Cheung's *Han article does not list a nominal derivative. Hence the node is graded 'plausible': ni-jan → nažand is a reasonable but unproved reconstruction, the other five are confirmed. Note also that the Ferdowsi couplet printed under this box («نباشد شادمانی بی نژندی - نه پیروزی بود بی مستمندی») is the illustration for nažand, not evidence for the etymology.\",\n          \"derivation_fa\": \"پنج واژه از شش واژهٔ این جعبه بی‌گمان همان ترکیب‌های ni- ی جعبهٔ بالا هستند و همه واسطهٔ فارسی میانه دارند (مکنزی، صص ۵۹–۶۱): nišastan/nišīn- «نشستن» و مشتق‌های nišēm و nišēmag که همان «نشیم، نشیمن» درونِ کمانک‌اند؛ nišēb «سراشیب» ← «نشیب»؛ nibištan/nibēs- ← «نوشتن» (پارسی باستان nipišta- ← پهلوی nibišt: پِ ایرانی باستان در میان دو واکه به ب نرم شده و سپس در فارسی نو ب به و بدل گشته)؛ nibard و nibardīdan ← «نبرد» (اوستایی *ni-parət- ← پهلوی nipart/nibard با ابدال rt به rd)؛ و ni + *vart- ← «نوردیدن» که چونگ صریح ذیل *uart آورده و معین در حاشیهٔ «نوشتن» (برهان ۲۲۰۱) با «رک: نوردیدن» به آن ارجاع داده است. حلقهٔ سست «نژند» است: هرن (۱۰۳۱) پارسی باستان *ni-jantu- را پیشنهاد می‌کند اما خود می‌نویسد «نامسلّم» و معین هم تنها می‌گوید «مفروض است»؛ هیچ صورتِ گواه‌داری پسوندِ -and را توضیح نمی‌دهد. پس داوری این جعبه «با احتیاط پذیرفتنی» است: پنج واژه تأیید می‌شود و «نژند» بازسازیِ نااثبات‌شده می‌ماند.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D9%86%D9%88%D8%B4%D8%AA%D9%86\",\n            \"https://en.wiktionary.org/wiki/%D9%86%D8%A8%D8%B1%D8%AF\",\n            \"https://en.wiktionary.org/wiki/%D9%86%DA%98%D9%86%D8%AF\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"BQT\",\n              \"status\": \"supports\",\n              \"note\": \"The node's reference is the bare abbreviation BQT (no page), so the parent node's pages were used: p.2135 headword نژند «بمعنی اندوهگین و غمناک و فرومانده و افسرده و سرفرود افکنده و پژمرده باشد» with the OP *nijantu- footnote on p.2134; p.2145 نشستن; p.2147 نشیب and نشیم («رک: اشتقاق ۱۰۳۸ ... از نشستن»); p.2201 نوشتن and نوردیدن. All four Mo'in footnotes give ni- + verbal root, exactly as drawn.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"PHD\",\n              \"where\": \"MacKenzie, Concise Pahlavi Dictionary pp. 59-61 (PHD.txt lines 512-514)\",\n              \"stance\": \"supports\",\n              \"note\": \"\\\"nibard [nplt' | N nabard] fight, struggle, battle. ~ag tried, experienced. nibardīdan, nibard- [npit-ytn' | P nbrd'd] fight, do battle.\\\" · \\\"nibištan, nibēs- [npstn' | M nbyšt, nbys-, N —] write.\\\" · \\\"nišastan, nišīn- ... sit.\\\" · \\\"nišēb [nšyp | N ~] declivity; astr. dejection.\\\" · \\\"nišēm [nšym | M nšym, N ~an] seat, perch. ~ag residence, abode.\\\" No MP ancestor for نژند or for نوردیدن is listed.\"\n            },\n            {\n              \"src\": \"HRN\",\n              \"where\": \"Horn nos. 1025, 1031, 1033, 1034, 1034bis, 1050, 1051 (pp. 230-235)\",\n              \"stance\": \"partial\",\n              \"note\": \"Supports five words but hedges two: 1031 nezend \\\"... Unsicher\\\"; 1050 \\\"neverdīden (neverden) 'drehen, winden, wandern' ... ai. ni + √vart- ... Wenn die Etymologie richtig ist, so wäre die ursprüngliche Form *niverdīden bezw. *nivesten\\\"; 1034bis \\\"nišēm(an) 'Nest' ... Doch wohl auch zu np. nisesten (No. 1033)\\\".\"\n            },\n            {\n              \"src\": \"CHEUNG\",\n              \"where\": \"s.v. *uart (p.424, NWIR), *pais (p.291), *hi(n)d\",\n              \"stance\": \"supports\",\n              \"note\": \"\\\"(+ *ni-) NP nawardīdan/naward- 'to fold, cease; to twist; to stroll'\\\"; \\\"(+ *ni-) MMP nbys-, BMP nps- /nibis-/ 'to write, copy a book'\\\"; \\\"(+ *ni-) Widely attested: NP nišastan/nišīn-, Bal. nist/nind-, Kurd. nistin ...\\\". Nažand is absent (Cheung covers verbs only).\"\n            },\n            {\n              \"src\": \"MON\",\n              \"where\": \"Wiktionary Persian نژند / نوردیدن (checked as a modern substitute)\",\n              \"stance\": \"silent\",\n              \"note\": \"Neither the Persian نژند nor نوردیدن page on en.wiktionary carries an etymology section as of the fetch (files data/verification/sources/web/1e1dde7ff515d65f.txt and 9c5c4c5bb93a1ba1.txt contain no 'Etymology' heading for Persian), so no independent modern confirmation of nažand was found beyond Horn/Mo'in.\"\n            }\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Avestan / Old Persian\",\n          \"words\": \"ni-dâ; ni-gaoša; ni-gâma; ni-kasa; ni-az\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Four of the five are solid, one is contested. (1) ni-dā- 'to lay down, hide': Av. ni + √dā- (nidaδāt), Skt. ni-dadhāti; Cheung s.v. *daH² lists \\\"(+ *ni-) 'to lay, put down'\\\" with MMP nyh-/BMP HNHTWN- and NP nihādan. Nourai's cross-ref 'Dhē 2' is exactly Pokorny's lemma dhē-2 (pp. 235-239). (2) ni-gaoša- 'to listen': Pokorny's ghous- 'to sound; hear' (p. 454) itself prints \\\"Avestan gaoš- 'hear' ... npers. niyōšīdan 'hear, listen, eavesdrop' ... Old pers. gauša-, Avestan gaoša- m. 'ear'\\\"; Cheung s.v. *gauš has \\\"(+ *ni-) MMP nywš-, BMP n(y)ōw(h)s- ... Parthian ngwš-, Sogdian nyws\\\". Note that this is an Indo-Iranian-only root, so Nourai's cross-ref 'Ôus 1' (PIE *ous- 'ear') is not Pokorny's assignment. (3) ni-gāma- '(place for) inserting down': unattested; Horn no. 1063 offers \\\"ap. *nigāma-, vergl. skr. ni + √gam-, nigamá- 'Einfügung'\\\" but ends \\\"Unsicher\\\", while Gharib's Sogdian dictionary (entry 5893, p.237) does give ny'm \\\"niyām ©<*ni-gāma\\\" — real support for the reconstruction. Against it, en.wiktionary (citing Wolff, Glossar zu Firdosis Schahname 829b, and Shapira 2009) derives NP نیام from MP niyām \\\"based on an Old Persian *nidāmān- 'covering, envelope'\\\", cognate with Skt. nidhānam 'act of laying down, deposit', i.e. ni- + dhā- — the same prefix but a different second member. (4) ni-kasa- 'look': Av./OP kas- 'to look' (Cheung *kas), whence MP nigāh and Parthian ngʾh; Horn no. 1037 \\\"aw. *nikasa- (vergl. āgāh, No. 40); phlv. n(i)kās\\\". Cross-ref 'Kwek' (PIE *kʷeḱ-) is right. (5) ni-az 'that which pushes you down, need': confirmed as an arrow but with the wrong root pointer — Cheung s.v. *Haz 'to drive, lead' (pp.171-172) lists Av. az- with \\\"(+ *ni-) caus. 'to straiten'\\\" (YAv. niiazata Yt 5.127, niiazaiiən V 13.30) and then \\\"MIDDLE PERSIAN: (+ *ni-) BMP ny'c /niyāz/, MMP ny'z 'want, need, misery'\\\", PARTHIAN ny'z, SOGDIAN ny'z, \\\"NWIR: (+ *ni-) NP niyāz 'need'\\\"; the PIE root is *h₂eǵ- 'to drive' (Pokorny 4 ff.), not Nourai's 'Angh' (*anǵʰ- 'narrow', Pokorny 42). The node is therefore 'plausible': the ni- prefixation is right throughout, but ni-gāma- competes with *ni-dā-mān- and the 'Angh' pointer is wrong.\",\n          \"derivation_fa\": \"چهار عضو از پنج عضو استوارند و یکی مورد اختلاف. ۱) ni-dā- «فرو نهادن، نهفتن»: اوستایی ni + √dā- (nidaδāt)، سنسکریت ni-dadhāti؛ چونگ ذیل *daH «(+ *ni-) to lay, put down» با پهلویِ nyh- و فارسیِ «نهادن»؛ ارجاعِ «Dhē 2» همان سرواژهٔ dhē-2 پوکورنی (صص ۲۳۵–۲۳۹) است. ۲) ni-gaoša- «نیوشیدن»: پوکورنی خود در ص ۴۵۴ ذیل ghous- «شنیدن» می‌نویسد «Avestan gaoš- \\\"hear\\\" ... npers. niyōšīdan». ولی این ریشه تنها هندوایرانی است و ارجاعِ «Ôus 1» (هندواروپایی *ous- «گوش») از آنِ پوکورنی نیست. ۳) ni-gāma-: گواه ندارد؛ هرن (۱۰۶۳) *nigāma- را پیشنهاد و «نامسلّم» می‌خواند، ولی قریب در واژه‌نامهٔ سغدی (شمارهٔ ۵۸۹۳، ص ۲۳۷) ny'm را «niyām <*ni-gāma» می‌آورد و همین پشتوانهٔ واقعی آن است؛ در برابر، ویکی‌واژه به پیرویِ ولف و شاپیرا «نیام» را از پارسی باستان *nidāmān- «پوشش، غلاف» (ni + dhā-، هم‌ریشه با سنسکریت nidhānam) می‌گیرد. ۴) ni-kasa- «نگاه»: اوستایی/پارسی باستان kas- «نگریستن»، پهلوی nigāh، پارتی ngʾh؛ هرن (۱۰۳۷) «اوستا *nikasa-، پهلوی n(i)kās». ۵) ni-az «نیاز»: پیکانِ نورایی درست است اما ارجاعِ ریشه نادرست؛ چونگ ذیل *Haz «راندن» (صص ۱۷۱–۱۷۲) اوستایی az- را با «(+ *ni-) caus. to straiten» (niiazata، niiazaiiən) و سپس پهلوی و پارتی و سغدی ny'z و فارسی «نیاز» می‌آورد و ریشهٔ هندواروپایی را *h₂eǵ- (پوکورنی ص ۴) می‌داند، نه *anǵʰ- «تنگ» (ص ۴۲) که «Angh» نورایی است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D9%86%DB%8C%D8%A7%D9%85\",\n            \"https://en.wiktionary.org/wiki/%D9%86%DB%8C%D8%A7%D8%B2\",\n            \"https://en.wiktionary.org/wiki/%D9%86%D9%87%D8%A7%D8%AF%D9%86\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"POK:235\",\n              \"status\": \"supports\",\n              \"note\": \"Pokorny's lemma dhē-2 'to set, put' runs pp. 235-239 (POK_full.txt line 22278 head, 'Page(s): 235-239' at line 22510), so p.235 is its first page; it is the root of Av. ni-dā- / Skt. ni-dadhāti, i.e. Nourai's 'Dhē 2'.\"\n            },\n            {\n              \"ref\": \"POK:454\",\n              \"status\": \"supports\",\n              \"note\": \"Pokorny p.454 is the lemma ghous- 'to sound; hear' (Note: 'Only indoiranisch'), and the entry itself says: \\\"Avestan gaoš- 'hear', Kaus. in gušayat-uxda- 'sein Wort zu Gehör bringend', npers. niyōšīdan 'hear, listen, eavesdrop', Baluchi gōšay 'hear', niyōšay 'hear, listen' ... Old pers. gauša-, Avestan gaoša- m. 'ear', npers. gōš 'ear'\\\" — precisely Nourai's ni-gaoša.\"\n            },\n            {\n              \"ref\": \"BQT:2211\",\n              \"status\": \"supports\",\n              \"note\": \"Borhan-e Qate' p.2211 (pdf 294 of BQT_v4), footnote s.v. نهادن: «نهادن ... پهلوی nihātan (گذاشتن، نهادن)، ایرانی باستان *ni-dā- «بارتولمه ۷۲۱»، «لیبرکه ۱۵۸-۹». هرن گوید: اوستا ni + dā (nidaδāt) (گذاشتن، نهادن)، پهلوی n(i)hātan، هندی باستان ni + dhā (nidadhāti) «اشتقاق ۱۰۵۷»» — exactly the chart's ni-dā.\"\n            },\n            {\n              \"ref\": \"HRN:238\",\n              \"status\": \"partial\",\n              \"note\": \"Horn p.238 is no. 1063 \\\"niyām 'Scheide'. ap. *nigāma-, vergl. skr. ni + √gam-, nigamá- 'Einfügung' (aber nur als ritueller t. t.), vergl. np. peyām (de Lagarde, Ges. Abh. 79). Unsicher.\\\" The page supports Nourai's gloss '(place for) inserting down' verbatim (Einfügung) but Horn himself marks it uncertain; the same page has no. 1062 niyā, 1064 nirō, 1070 niyōšīdan is on p.240.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"CHEUNG\",\n              \"where\": \"s.v. *daH² (p.~100), *gauš (p.~123), *kas (p.~239), *Haz (pp.171-172)\",\n              \"stance\": \"supports\",\n              \"note\": \"*daH²: \\\"|| (+ *ni-) 'to ...' ... MMP nyh- (BMP HNHTWN-) 'to lay, put down' ... NP nihādan/nih-, Kurd. (Sor.) da-nān\\\"; *gauš: \\\"(+ *ni-) MMP nywš-, BMP n(y)ōw(h)s- ... Parthian ngwš- 'to hear' ... Sogdian nyws\\\"; *kas: \\\"(+ *ni-) ... NP nigāh 'look, attention'\\\" and \\\"(+ *ā-) NP āgāh\\\"; *Haz: \\\"(+ *ni-) caus. 'to straiten' ... BMP ny'c /niyāz/ 'want, need, misery' ... NP niyāz 'need'\\\", PIE *h₂eǵ- 'to drive'?, Pok. 4 ff.\"\n            },\n            {\n              \"src\": \"HRN\",\n              \"where\": \"Horn nos. 1037 (p.232), 1057 (p.236), 1058 (p.236), 1070 (p.240)\",\n              \"stance\": \"supports\",\n              \"note\": \"1037 \\\"nigāh 'Anblick, Aufmerksamkeit'. aw. *nikasa- (vergl. āgāh, No. 40); phlv. n(i)kās\\\"; 1057 \\\"nihāden 'hinlegen, hinsetzen' ... aw. ni + √2dā- (nidaδāt) 'hinsetzen'; phlv. n(i)haδan; ai. ni + √1dhā- (nidadhāti)\\\"; 1058 \\\"nihān 'verborgen, heimlich'. ap. *nidāna- 'etwas (heimlich) hingelegtes'\\\"; 1070 \\\"niyōšīden 'hören, horchen'. aw. *nī-√gaoš-, vergl. apa-gaošayeiti; phlv. n(i)yōšītan bezw. n(i)gōšītan\\\".\"\n            },\n            {\n              \"src\": \"SOD\",\n              \"where\": \"Gharib, Sogdian Dictionary, entries 5893 (p.237), 5902 (p.237), 6218\",\n              \"stance\": \"supports\",\n              \"note\": \"5893 ny'm: \\\"niyām (ny'm) ©<*ni-gāma ©ob. -y\\\" — an independent Iranologist's backing for Nourai's *ni-gāma; 5902 ny'ws-: \\\"niyōš (nyws-, nyγws) ©<*ni-gauša-; Parth. ...\\\" · 'listener, hearer' ny'ws'kt; 6218 ny'z 'necessity'.\"\n            },\n            {\n              \"src\": \"PHD\",\n              \"where\": \"MacKenzie pp. 60-61 (PHD.txt lines 512-514)\",\n              \"stance\": \"supports\",\n              \"note\": \"\\\"nihādan, nih- [TNH TWN-tn' | M nyh'd, nyh-, N ~] put, place, establish. nihān concealment, secrecy.\\\" · \\\"nigah [nk's | M ng'h, N ~] look, attention. ~ dāštan: watch, keep. — kardan: look.\\\" · \\\"niyāz [ny'c | M ny'z, N ~] need, want, misery. ~ōmand needy.\\\" · \\\"niyē(x)šīdan, niyē(x)š- [n(y)ōxš-ytn' | M nywš-, N niyōšīdan] hear.\\\" No MP form corresponding to *ni-gāma is listed under 'ny-' — the MP word is nyām (Wiktionary's 𐫗𐫏𐫀𐫖).\"\n            }\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Persian\",\n          \"words\": \"nahâdan «نهادن»; nîûšîdan «نیوشیدن»; nîâm «نیام»; negâh «نگاه»; nîâz «نیاز» (+ نهان)\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Four New Persian outcomes of node 4 are secure, and each has an attested Middle Persian intermediate: (a) نهادن < MP nihādan/nih- (Book Pahlavi TNH TWN-tn', Man. MP nyh'd, nyh-) < Old Iranian *ni-dā-; the *d of *ni-dā- goes to Middle Persian -h- exactly as in Av. daδāiti → MP dahēd, and the derivative نهان continues MP nihān 'concealment' < OP *ni-dāna- 'something laid down (in hiding)'; (b) نیوشیدن < MP niyē(x)šīdan/niyōšīdan (also spelt n(i)gōšītan) < *ni-gauša-, the Iranian *š of *gauš- surfacing as -xš-/-š-, and Pokorny p.454 prints the New Persian form itself; (c) نگاه < MP nigāh (nk's) 'look, attention', Parthian ngʾh, from *ni-kāsa-, sister of آگاه < *ā-kāsa- (the verb survives dialectally, Horn 1037 quoting Kāšān bi-kes 'look!'); (d) نیاز < MP/Parthian ny'z, Sogdian ny'z, from *ni-āza- to *Haz 'to drive' — the semantics 'be driven down, be straitened' → 'need' is Cheung's, and Nourai's gloss 'that which pushes you down' catches it. The fifth, نیام 'sheath', is the contested one: MP nyām/nyyʾm is certain, but its Old Iranian shape is either *ni-gāma- 'insertion' (Horn 1063 'unsicher', Gharib s.v. ny'm) or *ni-dā-mān- 'covering' (Wiktionary after Wolff/Shapira, with Skt. nidhānam and Wakhi naẟün as cognates). Either way the word belongs on this root; only the second element is in doubt — hence 'plausible'. The Hāfez couplet printed in the box («به گوش هوش نیوش از من ...») is the citation for نیوشیدن.\",\n          \"derivation_fa\": \"چهار برآمدِ فارسی نو استوارند و هر یک واسطهٔ فارسی میانه دارند: «نهادن» از پهلوی nihādan/nih- از ایرانی باستان *ni-dā- (دالِ ایرانی باستان در فارسی میانه به ه بدل شده، همچون daδāiti ← dahēd) و «نهان» از پهلوی nihān از پارسی باستان *ni-dāna- «چیزِ پنهان‌نهاده»؛ «نیوشیدن» از پهلوی niyōšīdan/n(i)gōšītan از *ni-gauša- که پوکورنی خودِ صورتِ فارسی نو را در ص ۴۵۴ آورده است؛ «نگاه» از پهلوی nigāh و پارتی ngʾh از *ni-kāsa-، خواهرِ «آگاه» از *ā-kāsa-؛ «نیاز» از پهلوی و پارتی ny'z و سغدی ny'z از *ni-āza- به ریشهٔ *Haz «راندن»، با تحول معنایی «به‌زیر رانده‌شدن، در تنگنا افتادن» ← «حاجت» که تعبیرِ چونگ است و ترجمهٔ نورایی («آنچه تو را به زیر می‌راند») همان را می‌رساند. پنجمی، «نیام»، مورد اختلاف است: فارسی میانهٔ nyām قطعی است اما صورتِ ایرانیِ باستانش یا *ni-gāma- است (هرن، «نامسلّم»؛ قریب) یا *ni-dā-mān- «پوشش» (ویکی‌واژه به پیرویِ ولف و شاپیرا، با هم‌ریشه‌های سنسکریت nidhānam و وخی naẟün). در هر دو حال واژه به همین ریشه می‌رسد و تنها جزء دوم محلِ گفت‌وگوست؛ از این‌رو داوری «با احتیاط پذیرفتنی» است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D9%86%D9%87%D8%A7%D8%AF%D9%86\",\n            \"https://en.wiktionary.org/wiki/%D9%86%DB%8C%D8%A7%D9%85\",\n            \"https://en.wiktionary.org/wiki/%D9%86%DB%8C%D8%A7%D8%B2\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"None\",\n              \"status\": \"not_checked\",\n              \"note\": \"The printed box carries no reference of its own (the JSON has refs=null, and the page image confirms there is no book icon in this Persian box). Its parent's citations POK:235,454; BQT:2211; HRN:238 were checked instead, and all four bear on these words.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"PHD\",\n              \"where\": \"MacKenzie pp. 60-61\",\n              \"stance\": \"supports\",\n              \"note\": \"\\\"nihādan, nih- ... put, place, establish\\\"; \\\"nihān concealment, secrecy. ~īg secret\\\"; \\\"nigah [nk's | M ng'h, N ~] look, attention\\\"; \\\"niyāz [ny'c | M ny'z, N ~] need, want, misery\\\"; \\\"niyē(x)šīdan, niyē(x)š- [n(y)ōxš-ytn' | M nywš-, N niyōšīdan] hear\\\".\"\n            },\n            {\n              \"src\": \"HRN\",\n              \"where\": \"Horn nos. 1037, 1057, 1058, 1063, 1070\",\n              \"stance\": \"partial\",\n              \"note\": \"Supports نهادن، نهان، نگاه، نیوشیدن outright; for نیام (1063) it ends \\\"Unsicher\\\" and adds in a footnote that Pahlavi n(i)kām (Vd. 7) would have to be read *n(i)gām to be joined to np. niyām (after Darmesteter, Ét. ir. I 61 n.4). Horn has no entry for niyāz.\"\n            },\n            {\n              \"src\": \"BQT\",\n              \"where\": \"Borhan-e Qate' p.2211 (نهادن) and p.2222 (نیاز)\",\n              \"stance\": \"supports\",\n              \"note\": \"p.2211 footnote: «نهادن ... پهلوی nihātan ... ایرانی باستان *ni-dā- «بارتولمه ۷۲۱» ... هرن گوید: اوستا ni + dā (nidaδāt) ... «اشتقاق ۱۰۵۷»»; p.2222 headword «نیاز - بکسر اول بروزن حجاز، حاجت بود».\"\n            },\n            {\n              \"src\": \"CHEUNG\",\n              \"where\": \"s.v. *Haz (pp.171-172), *gauš, *kas, *daH²\",\n              \"stance\": \"supports\",\n              \"note\": \"\\\"*NWIR: ... || (+ *ni-) NP niyāz 'need'\\\"; \\\"*SOGDIAN: (+ *ni-) CSogd. ny'z'wt 'needing, needy', MSogd. ny'z 'need'\\\"; \\\"(+ *ni-) NP nihādan/nih- ... 'to lay, put down'\\\"; \\\"(+ *ni-) ... NP nigāh 'look, attention'\\\".\"\n            }\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"Avestan / Old Persian\",\n          \"words\": \"ni-mâ; nî-gaona\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"ni-mā- 'to measure down, show' is well founded. Old Iranian *ni-mā(y)- is ni- + the root *mā- 'to measure' (Av. mā-, Skt. mā-, PIE *meh₁-, Nourai's 'Me'); Cheung s.v. the *mā(H) article lists \\\"(+ *ni-) MMP nm'y- 'to show'\\\" beside \\\"(+ *fra-) frm'y- 'to order'\\\" and gives \\\"NP nimāy-/nimūdan 'to appear, show'\\\"; Nyberg's Old-Iranian→Pahlavi index equates \\\"ni-māy-: nimūtan\\\"; Mo'in's footnote in Borhan (p.2171) spells the analysis out — «ایرانی باستان *ni-mā (جزو اول پیشوند بمعنی فرود، پایین؛ و جزو دوم بمعنی اندازه گرفتن و جمعاً بمعنی نمایش دادن)» with a reference to Bartholomae AiW 1195 — and Horn no. 1042 has \\\"ni + √mā-\\\". The semantic path is 'measure out (for someone) → point out → show'. nī-gaona 'downward' is weaker: it is not an attested Avestan word but a back-formation from MP nigūn 'inverted, upside down'. Mo'in (BQT 2165 fn. 2) does analyse نگون as ni- + gaona-, citing Hübschmann p.142, where §32 establishes exactly the sound law needed: \\\"Ap. au = phl. ō wird vor w, m im Pāz. und Np. zu ū: gūn 'Farbe, Art und Weise' — pāz. gūn, gūna, arm. goin, zd. gaona-\\\" (with the footnote \\\"Dazu čigūna, čun 'wie', zargūn etc.\\\"), and Pokorny puts Av. gaona- 'hair; (hair)colour' under geu- 'to bend' (pp. 393-398) = Nourai's 'Gěu 1'. But en.wiktionary prefers a different second element, comparing Skt. nyañc- 'directed downwards' (i.e. ni- + *h₃ekʷ-, the analysis Pokorny gives for Skt. nīca- as *ni-okʷ-os 'looking downward'). Both readings agree on ni-; the node is graded 'plausible' for the second member of nī-gaona.\",\n          \"derivation_fa\": \"ni-mā- «فرو اندازه گرفتن، نمودن» استوار است: ایرانی باستان *ni-mā(y)- از ni- و ریشهٔ *mā- «پیمودن، اندازه گرفتن» (اوستایی mā-، سنسکریت mā-، هندواروپایی *meh₁- که همان «Me» نورایی است). چونگ «(+ *ni-) MMP nm'y- to show» و «NP nimāy-/nimūdan» را می‌آورد؛ نیبرگ در فهرستِ ایرانی باستان به پهلوی «ni-māy-: nimūtan» دارد؛ معین در حاشیهٔ برهان (ص ۲۱۷۱) صریح می‌نویسد «ایرانی باستان *ni-mā (جزو اول پیشوند بمعنی فرود، پایین؛ و جزو دوم بمعنی اندازه گرفتن و جمعاً بمعنی نمایش دادن) «بارتولمه ۱۱۹۵»»؛ و هرن (۱۰۴۲) «ni + √mā-». مسیر معنایی «پیمودن ← نشان دادن ← نمودن» است. اما nî-gaona «سرنگون» صورتی گواه‌دار در اوستا نیست و بازسازی از پهلویِ nigūn است. معین (برهان ۲۱۶۵، حاشیهٔ ۲) نگون را ni- + gaona- می‌گیرد و به هوبشمان ص ۱۴۲ ارجاع می‌دهد که همان قانونِ آوایی لازم را ثبت کرده است: «پارسی باستان au = پهلوی ō پیش از w و m در پازند و فارسی نو به ū بدل می‌شود: gūn «رنگ، گونه» — پازند gūn، gūna، ارمنی goin، اوستایی gaona-»؛ پوکورنی نیز gaona- را ذیل geu- «خم کردن» (صص ۳۹۳–۳۹۸) می‌آورد که همان «Gěu 1» است. در برابر، ویکی‌واژه جزء دوم را با سنسکریت nyañc- «رو به پایین» می‌سنجد (یعنی ni- + *h₃ekʷ-). هر دو خوانش بر ni- هم‌داستان‌اند؛ داوری این جعبه به‌خاطر جزء دومِ nî-gaona «با احتیاط پذیرفتنی» است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D9%86%DA%AF%D9%88%D9%86\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"BQT:2171\",\n              \"status\": \"supports\",\n              \"note\": \"Borhan-e Qate' p.2171 (pdf 254 of BQT_v4, printed header ۲۱۷۱), footnote to نمودن: «نمودنی ... از: نمو + دن (پیوند مصدری) «دارمستتر، تتبعات ج ۱ ص ۱۹۷، ۲۸۳»، پهلوی [nimūtan]، ایرانی باستان *ni-mā (جزو اول پیشوند بمعنی فرود، پایین؛ و جزو دوم بمعنی اندازه گرفتن و جمعاً بمعنی نمایش دادن) «بارتولمه ۱۱۹۵»، «لیبرکه ص ۳۵۹»، آستی nimāyun، شغنی nimāy- (نمودار شدن، ظاهر شدن) «اشتقاق ۱۰۴۲»؛ نشان دادن، اظهار کردن، ارائه دادن» — exactly Nourai's ni-mā 'measure down, show'.\"\n            },\n            {\n              \"ref\": \"HRN:233\",\n              \"status\": \"supports\",\n              \"note\": \"Horn p.233 is no. 1042: \\\"numūdan 'zeigen; erscheinen', Praes. numāy-em, numūdar, numūn ... ni + √mā-; phlv. n(i)mūtan 'zeigen, erscheinen', n(i)mayišn, n(i)mūtār; oss. d. nimāyun, i. nimajun 'rechnen, zählen'; šar. sign. namāy-em 'sich zeigen, erscheinen'\\\" — the page Nourai cites, and it says exactly what the arrow says. (The same page has no. 1041 nemed = the 'Nimatâ → Nemata 2' redirect on this page.)\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"CHEUNG\",\n              \"where\": \"Etym. Dict. Iranian Verb, the *mā(H)/framā article (CHEUNG.txt lines 16924-16990)\",\n              \"stance\": \"supports\",\n              \"note\": \"\\\"MIDDLE PERSIAN: ... || (+ *ni-) MMP nm'y- 'to show'\\\"; \\\"PARTHIAN: ... || (+ *ni-) nm'y- 'to show'\\\"; \\\"SOGDIAN: (+ *ni-) SSogd. nm'y, CSogd. nm'y, MSogd. nm'y 'to judge'\\\"; \\\"NWIR: ... || (+ *ni-) NP nimāy-/nimūdan 'to appear, show'\\\".\"\n            },\n            {\n              \"src\": \"NYB\",\n              \"where\": \"Nyberg, Manual of Pahlavi II, Old-Iranian index (NYB_vol2_glossary.txt line 4914); glossary s.v. handāčak\",\n              \"stance\": \"supports\",\n              \"note\": \"The index equates \\\"ni-māy-: nimūtan\\\", i.e. Pahlavi nimūtan continues Old Iranian *ni-māy-; the glossary's \\\"handāčak [hnd'ck'] measure; ~ nimūtan to measure\\\" preserves the original 'measure' sense of the verb.\"\n            },\n            {\n              \"src\": \"HUB\",\n              \"where\": \"Hübschmann, Persische Studien p.142 §32 (cited by Mo'in in the نگون footnote)\",\n              \"stance\": \"supports\",\n              \"note\": \"\\\"Ap. au = phl. ō wird vor w, m im Pāz. und Np. zu ū: gūn 'Farbe, Art und Weise' — pāz. gūn, gūna, arm. goin, zd. gaona-\\\", footnote \\\"Dazu čigūna, čun 'wie', zargūn etc.\\\" — the sound law and the equation gūn = Av. gaona- on which BQT's ni- + gaona- analysis of نگون rests.\"\n            },\n            {\n              \"src\": \"POK\",\n              \"where\": \"IEW 393-398, lemma geu-, gau-, gu- (POK_full.txt lines 31753, 32047)\",\n              \"stance\": \"supports\",\n              \"note\": \"\\\"Avestan gaona- n. 'hair (esp. the animal); (hair)colour'\\\" stands inside Pokorny's geu- 'to bend, curve' (Page(s): 393-398), so Nourai's cross-reference 'Gěu 1' for the second element of nī-gaona is Pokorny's own assignment.\"\n            }\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"Persian\",\n          \"words\": \"nemŭdan «نمودن»; nemâîdan «نماییدن»; negŭn «نگون» (+ نمود، نمودار؛ نما، نمایش، نماینده، نمایان؛ نگونسار، سرنگون)\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"نمودن / نماییدن are a single verb with the usual New Persian doublet of stems: MP nimūdan, pres. nimāy- (Book Pahlavi nmwtn', nmd-; Man. MP nmwdn, nm'y-) < Old Iranian *ni-māy-; the past stem gave nemūd- (whence نمود، نمودار) and the present stem was re-verbalised as نماییدن (whence نما، نمایش، نماینده، نمایان). MacKenzie prints \\\"nimūdan, nimāy- [nmwtn', nmd- | M nmwdn, nm'y-, N ~] show, guide\\\", and Horn no. 1042 notes that in the dialects only the -ūn present survives (Kāšān bä-numōn). نگون continues MP nigūn 'inverted, upside down' (MacKenzie: \\\"nigūn [nkwn' | N ~] inverted, upside down. ~īh: depth, downward direction. ~sar [-s'l | M ngwns'r] downwards\\\"), and the chart's extras نگونسار / سرنگون are MP nigūnsār and its inversion; the semantic core is 'head bowed down', which is how Borhan glosses it («بمعنی خم شده و کوز و سر در زیر افکنده باشد»). The reason for grading the node 'plausible' rather than 'confirmed' is the second element of نگون, exactly as for node 6: Mo'in's footnote (BQT 2165) analyses it as ni- + gaona- via Hübschmann §32, while en.wiktionary says only that MP nigūn \\\"may be akin to Sanskrit न्यञ्च् (nyañc, 'directed downwards')\\\" and notes Old Armenian նկուն (nkun) as an Iranian loan; Pokorny's own analysis of the Indic congener nīca- is *ni-okʷ-os 'looking down'. The prefix ni- is not in question in any account.\",\n          \"derivation_fa\": \"«نمودن» و «نماییدن» یک فعل‌اند با دوگانگی ستاک که در فارسی نو معمول است: فارسی میانهٔ nimūdan با ستاک حال nimāy-، از ایرانی باستان *ni-māy-؛ ستاک گذشته «نمود» را داد (و از آن «نمود، نمودار») و ستاک حال دوباره مصدر ساخت: «نماییدن» (و از آن «نما، نمایش، نماینده، نمایان»). مکنزی می‌نویسد «nimūdan, nimāy- ... show, guide» و هرن (۱۰۴۲) یادآور می‌شود که در گویش‌ها تنها ستاک حالِ -ūn مانده است (کاشانی bä-numōn). «نگون» ادامهٔ پهلویِ nigūn «سرنگون، وارونه» است (مکنزی: «nigūn ... inverted, upside down؛ nigūnsār downwards») و «نگونسار» و «سرنگون» همان nigūnsār پهلوی و قلبِ آن‌اند؛ برهان نیز آن را «بمعنی خم شده و کوز و سر در زیر افکنده» می‌آورد. داوری «با احتیاط پذیرفتنی» است، دقیقاً به همان دلیلِ جعبهٔ پیشین: جزء دومِ «نگون». معین (برهان ۲۱۶۵) آن را ni- + gaona- می‌گیرد و به هوبشمان ص ۱۴۲ ارجاع می‌دهد، ولی ویکی‌واژه تنها می‌گوید nigūn «شاید هم‌ریشه با سنسکریت nyañc «رو به پایین» باشد» و ارمنی کهن nkun را وام‌واژهٔ ایرانی می‌شمارد. در هیچ روایتی پیشوند ni- محل تردید نیست.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D9%86%DA%AF%D9%88%D9%86\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"MON:4812\",\n              \"status\": \"not_checked\",\n              \"note\": \"Mo'in's 6-volume Farhang-e Farsi is not available on disk in its original pagination — only the 2-volume Adena abridgement (MON_part1/2.txt), which has no page breaks and drops the Latin-script Pahlavi/Avestan forms; vajehyab/abadis carry the entry text but, as refs_online.json records, 'Page numbers cannot be mapped online'. Grepping MON_part2.txt for نگون returns only compounds (قلزم نگون، کاس نگون), no headword entry. The content of the claim was instead verified from BQT p.2165/2171, PHD p.60-61, HRN no.1042 and Nyberg's index.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"PHD\",\n              \"where\": \"MacKenzie, Concise Pahlavi Dictionary pp. 60-61 (PHD.txt lines 512, 514)\",\n              \"stance\": \"supports\",\n              \"note\": \"\\\"nimūdan, nimāy- [nmwtn', nmd- | M nmwdn, nm'y-, N ~] show, guide.\\\" · \\\"nigūn [nkwn' | N ~] inverted, upside down. ~īh: depth, downward direction. ~sar [-s'l | M ngwns'r] downwards.\\\" Both New Persian words therefore have the Middle Persian ancestor the chart implies.\"\n            },\n            {\n              \"src\": \"BQT\",\n              \"where\": \"Borhan-e Qate' p.2165 (نگون, footnote 2) and p.2171 (نمودن)\",\n              \"stance\": \"supports\",\n              \"note\": \"p.2165: headword «نگون - بکسر اول بروزن چون، بمعنی خم شده و کوز و سر در زیر افکنده باشد»; footnote 2 gives the Pahlavi and Armenian forms with «رک: هوبشمان ص ۱۴۲» (= the gūn < Av. gaona- section) and «لیبرکه ص ۷۱»; footnote 5 «نگونسار - از: نگون + سار (= سر)». p.2171 is the نمودن footnote quoted under ref_check.\"\n            },\n            {\n              \"src\": \"HRN\",\n              \"where\": \"Horn no. 1042 (p.233) and its footnote 2\",\n              \"stance\": \"supports\",\n              \"note\": \"\\\"numūdan 'zeigen; erscheinen' ... ni + √mā-; phlv. n(i)mūtan ... n(i)mayišn\\\"; footnote: \\\"In den Dialekten ist die Praesensbildung auf -ūn die alleinige, vergl. Kāš. v. bänumōn (Impt.), Ž. bänemōn, K. numūn\\\".\"\n            },\n            {\n              \"src\": \"CHEUNG\",\n              \"where\": \"the *mā(H)/framā article, NWIR section\",\n              \"stance\": \"supports\",\n              \"note\": \"\\\"(+ *ni-) NP nimāy-/nimūdan 'to appear, show', Kurd. (Sor.) ...\\\" — a modern Iranist confirming the same MP→NP line for نمودن/نماییدن.\"\n            }\n          ]\n        },\n        {\n          \"id\": 8,\n          \"lang\": \"Avestan\",\n          \"words\": \"ni-gerepta; ni-yaštâya; ni-paidhya\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"All three forms and all three glosses come straight out of Gharib's Sogdian dictionary, on precisely the three pages Nourai cites, and each is there labelled or paralleled as Avestan/Old Persian: (1) entry 5918, p.237, \\\"nyγrwβs- S : nayγruβs / nayrufs ©Av. niγərəpta ©med. pass. st. ⇒zyrwβs- · (to) be pressed down\\\" — the gloss 'pressed down' is Gharib's own words, and the Avestan past participle nī-gərəpta- is ni- + the past participle of grab- 'to seize' (PIE *gʰrebʰ- = Nourai's 'Ghrebh'); Cheung cautions that YAv. gərəpta- forms \\\"are very late, being transposed from BMP /griftan/\\\" and does not list *ni- among the Avestan prefixations of *grabH, so 'Avestan' here means Young/late Avestan at best. (2) entries 6091/6332, pp.244/254, \\\"nsty- S : nistāy (nyšt'y-) ©<*ni-stāya; OP niyastāya ©impf. nyšty · (to) settle, (to) order, (to) inform\\\" and \\\"nystāt- ©*ni-stāta ... (to) order, (to) fix, (to) establish\\\" — Nourai's gloss 'to settle down establish' is a conflation of Gharib's two glosses, and the form is properly Old Persian niyaštāya- (Kent §115: \\\"ni-šad- from ni- + sad- ... niyaštāyam 'I commanded'\\\"; XPh 21 niyaštāyam), from ni- + stā- 'to stand' (PIE *steh₂- = 'Sta'). (3) entry 6283, p.252, \\\"nypδ- B : nipe/aδ ©<Av. ni-paiδya-; Khot. nuvad; Khwar. ...; Pahl. nibastan-; Yaghn. nipid · (to) lie down\\\" — Gharib explicitly cites Av. ni-paiδya-, and Cheung s.v. *paid confirms the whole family: \\\"YAv. paiθ- 'to fall, be stuck in' || (+ *ni-) 'to lie, lay down' ... MMP nb'st- 'to throw down' ... Sogdian nypδ- 'to lie down'\\\", from PIE *ped- 'to move at a walking pace, be on one's feet' (Pokorny 791) — which resolves Nourai's own query mark on 'Ped?'. Two caveats: the box's label 'Avestan' fits (1) and (3), which Gharib cites as Avestan, but not (2), which is Old Persian and Sogdian; and on the printed page this box has an arrow into an empty, unlabelled box that the extraction does not record.\",\n          \"derivation_fa\": \"هر سه صورت و هر سه معنی مستقیماً از واژه‌نامهٔ سغدیِ بدرالزمان قریب برآمده‌اند، درست از همان سه صفحه‌ای که نورایی ارجاع داده است. ۱) شمارهٔ ۵۹۱۸، ص ۲۳۷: «nyγrwβs- : nayγruβs ©اوستایی niγərəpta ... (to) be pressed down» — «pressed down»ی نورایی عیناً معنیِ قریب است؛ اوستایی nī-gərəpta- اسم مفعولِ grab- «گرفتن» با پیشوند ni- است (هندواروپایی *gʰrebʰ- = «Ghrebh»). چونگ هشدار می‌دهد که صورت‌های gərəpta- در اوستای متأخر از پهلویِ griftan گرته‌برداری شده‌اند و *ni- را در فهرست پیشوندهای اوستاییِ *grabH نمی‌آورد. ۲) شمارهٔ ۶۰۹۱ و ۶۳۳۲، صص ۲۴۴ و ۲۵۴: «nistāy (nyšt'y-) ©<*ni-stāya؛ پارسی باستان niyastāya» با معنی‌های «to settle, to order, to establish»؛ صورتِ درست پارسی باستان niyaštāyam «فرمان دادم» است (کنت، بند ۱۱۵؛ خشایارشا XPh ۲۱)، از ni- + stā- «ایستادن» (هندواروپایی *steh₂- = «Sta»). ۳) شمارهٔ ۶۲۸۳، ص ۲۵۲: «nypδ- : nipeδ ©<اوستایی ni-paiδya-؛ ختنی nuvad؛ پهلوی nibastan-؛ یغنابی nipid · (to) lie down» — قریب خود اوستایی ni-paiδya- را نام می‌برد و چونگ ذیل *paid همین خانواده را با هندواروپایی *ped- «گام زدن، بر پا بودن» (پوکورنی ۷۹۱) تأیید می‌کند، که علامت پرسشِ خودِ نورایی («Ped؟») را برمی‌دارد. دو یادداشت: برچسبِ «اوستایی» برای دو صورت نخست و سوم درست است ولی صورت دومی پارسی باستان و سغدی است؛ و در صفحهٔ چاپی از این جعبه پیکانی به یک جعبهٔ خالی و بی‌برچسب کشیده شده که در استخراج ثبت نشده است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/n%C3%AD\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"SOD:237\",\n              \"status\": \"supports\",\n              \"note\": \"Gharib, Sogdian–Persian–English Dictionary, entry 5918 on printed p.237 (SOD_pages.txt line 20710, in the block that opens at the '237' page marker on line 20669): \\\"5918 nyrwβs- S | nayγruβs/nayrufs ©Av. niγərəpta ©med. pass. st. ⇒zyrwβs- | (to) be pressed down | Mack. AI 424.6 n p427\\\". Both Nourai's form and his gloss are Gharib's.\"\n            },\n            {\n              \"ref\": \"SOD:244\",\n              \"status\": \"supports\",\n              \"note\": \"Gharib entry 6091 on printed p.244 (SOD_pages.txt line 21240, block opening at the '244' marker, line 21172): \\\"6091 nsty- S | nistāy (nyšt'y-) ©<*ni-stāya; OP niyastāya ©impf. nyšty ⇒nyšty- | (to) settle, (to) order, (to) inform | MDii p205; MDiii p124\\\"; cf. 6328 nystāt- \\\"©*ni-stāta ... (to) order, (to) fix, (to) establish\\\".\"\n            },\n            {\n              \"ref\": \"SOD:252\",\n              \"status\": \"supports\",\n              \"note\": \"Gharib entry 6283 on printed p.252 (SOD_pages.txt line 21786, block opening at the '252' marker, line 21757): \\\"6283 nypδ- B | nipe/aδ ©<Av. ni-paiδya-; Khot. nuvad; Khwar. ...; Pahl. nibastan-; Yaghn. nipid ⇒'np'stk, np'yδ- | (to) lie down | GMS 544; VJ 1138; TSP 13.8; SCE 324; Bailey, Prolexis 141\\\"; cf. entry 6033 np'yδ- \\\"nipeδ (npyδ-) ©<*ni-padaya; Av. ni-paiδya; Pahl. nibāy-, nibastan\\\".\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"CHEUNG\",\n              \"where\": \"s.v. *paid (pp.~318-319), *grabH (pp.119-120)\",\n              \"stance\": \"partial\",\n              \"note\": \"*paid supports fully: \\\"AVESTAN: YAv. paiθ- 'to fall, be stuck in' || (+ *ni-) 'to lie, lay down (esp. to have sexual intercourse)' ... MIDDLE PERSIAN: (+ *ni-) MMP nb'st- 'to throw down' ... KHOTANESE: (+ *ni-) nuvad- 'to lie down' ... SOGDIAN: (+ *ni-) BSogd. nypδ- 'to lie down'\\\", PIE *ped-, Pok. 791. *grabH is the caveat: Cheung lists Avestan grab- with *a-, *uz-, *fra-, *ham- but NOT with *ni-, and notes \\\"YAv. gərəpta- forms are very late, being transposed from BMP /griftan/\\\".\"\n            },\n            {\n              \"src\": \"KNT\",\n              \"where\": \"Kent, Old Persian §115 (KNT.txt line 1439), text XPh 21-24\",\n              \"stance\": \"supports\",\n              \"note\": \"\\\"ni-šad- from ni- + sad- (Iran. had-), and the value š is extended to positions where the š is separated from the n by the augment: niyaštāyam 'I commanded' (but avastāyam 'I restored'), niyašādayam\\\"; the Xerxes daiva-inscription has \\\"ima stānam hauv niyaštāya kantanaiy\\\" (XPh 21) — the Old Persian home of Nourai's 'ni-yaštâya'.\"\n            },\n            {\n              \"src\": \"PHD\",\n              \"where\": \"MacKenzie p.60 (PHD.txt line 512)\",\n              \"stance\": \"supports\",\n              \"note\": \"\\\"nibastan, nibay- [SK BHWN-tn' < A škb; npstn', npδ- | M nbst] lie down, sleep. nibāstan, *nibāy- [np'stn' | M nb'st, nb'y-] lay down. nibēm [npδm] lying, prostrate.\\\" — the Middle Persian continuation of *ni-paiδya- that Gharib cites.\"\n            },\n            {\n              \"src\": \"BRT\",\n              \"where\": \"Bartholomae, AiW s.v. grab-, paiθ-, stā- (BRT.txt)\",\n              \"stance\": \"silent\",\n              \"note\": \"Not retrievable: the local OCR of Bartholomae loses Avestan diacritics and prefixed sub-headwords; grep for 'grb-', 'garab', 'gərəb', 'nixšvaep' returns nothing usable (only line 11608 'garəbuštara-'). The Avestan status of nī-gərəpta- and ni-paiδya- therefore rests on Gharib and Cheung here.\"\n            }\n          ]\n        },\n        {\n          \"id\": 9,\n          \"lang\": \"Germanic\",\n          \"words\": \"nith; nist\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Two Proto-Germanic stems, both standard (Nourai prints them without the asterisk they need). *nith- is the t-suffixed form of *ni-, seen in OE niþan/neoþan 'below' and, with the comparative suffix, *nitheraz > OE niþer, OS nithar, OHG nidar, ON niðr 'downward', whence the adjectives OE neoþera > ME nethere > nether. Watkins has it in so many words: \\\"ni. Down. 1. Suffixed form *ni-t- in Germanic *nith- in Old English nithan, neothan, below: BENEATH, UNDERNEATH. 2. Suffixed (comparative) form *ni-tero-, lower, in Germanic *nitheraz in Old English nither, lower: NETHER.\\\" *nist- 'nest' is the Germanic outcome of PIE *ni-zd-o- 'place to sit down in' (*ni- 'down' + zero grade of *sed- 'to sit'), with the regular Germanic devoicing/assimilation *-zd- > -st-: OE nest, OHG/MDu./Du./Ger. Nest, and the denominative *nistilōn > OE nestlian 'to make a nest'. Watkins: \\\"nizdo-. Bird's nest. Compound root formed from ni + *sd-, zd-, zero-grade form of sed-; literally, 'place where the bird sits down.' 1. Germanic *nist- in: a. Old English nest, nest: NEST ... [In Pok. sed- 887.]\\\" Nourai's gloss for nist ('place to sit down, nest') is that literal rendering. The word is not attested in Gothic or in Scandinavian, so *nist- is West Germanic in practice.\",\n          \"derivation_fa\": \"دو ستاکِ ژرمنیِ آغازین، هر دو معیار (نورایی ستارهٔ بازسازی را نگذاشته است). *nith- صورتِ پسوندیِ *ni- با -t است که در انگلیسی کهن niþan/neoþan «پایین» دیده می‌شود و با پسوندِ برترساز *nitheraz به انگلیسی کهن niþer، ساکسون کهن nithar، آلمانی علیای کهن nidar و نورس کهن niðr «به‌سوی پایین» می‌رسد و از آن‌جا صفتِ nether انگلیسی. واتکینز عیناً می‌نویسد: «ni. Down. صورتِ پسوندیِ *ni-t- در ژرمنیِ *nith- در انگلیسی کهن nithan، neothan «below»: BENEATH، UNDERNEATH؛ صورتِ برترسازِ *ni-tero- در ژرمنیِ *nitheraz در انگلیسی کهن nither: NETHER». *nist- «آشیانه» برآمدِ ژرمنیِ هندواروپاییِ *ni-zd-o- «جای فرو نشستن» است (*ni- «پایین» + ستاکِ صفرِ *sed- «نشستن») با تحول آواییِ منظمِ *-zd- به -st-: انگلیسی کهن nest، آلمانی Nest، و فعلِ برساخته *nistilōn ← انگلیسی کهن nestlian. معنیِ نورایی برای nist («جای فرو نشستن، آشیانه») همان ترجمهٔ تحت‌اللفظیِ واتکینز است. این واژه در گوتیک و زبان‌های شمالی گواه ندارد و در عمل ژرمنیِ باختری است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/nest\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"AHD\",\n              \"status\": \"supports\",\n              \"note\": \"Watkins 1985 (AHD_watkins1985.txt leaf ~787) s.v. ni: \\\"1. Suffixed form *ni-t- in Germanic *nith- in Old English nithan, neothan, below: BENEATH, UNDERNEATH. 2. Suffixed (comparative) form *ni-tero-, lower, in Germanic *nitheraz in Old English nither, lower: NETHER. See compound root nizdo-.\\\" And s.v. nizdo-: \\\"1. Germanic *nist- in: a. Old English nest, nest: NEST; b. Germanic *nistilōn in Old English nestlian, to make a nest: NESTLE.\\\" Both of Nourai's Germanic forms, with his glosses.\"\n            },\n            {\n              \"ref\": \"KLN:1042\",\n              \"status\": \"supports\",\n              \"note\": \"Klein p.1042 s.v. nether lists the whole Germanic set: \\\"OE. neodera, nidera, 'lower', from the adverb neodor, nider, 'downward'; rel. to the adverbs OS. nithar, ON. niðr, OFris. nither, Du. neder, neer, OHG. nidar, MHG. nider, G. nieder\\\", and the neighbouring entry 'nest' (line 25295) has \\\"I.-E. *niz-do-, stands for *ni-zd-o- and lit. means 'a place to sit down in', fr. *ni-, 'down', and zero degree of I.-E. base *sed-, 'to sit'\\\".\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"POK\",\n              \"where\": \"IEW 311-314 (1. en-, ni- section) and 884-887 (sed-)\",\n              \"stance\": \"supports\",\n              \"note\": \"\\\"Old High German nidar, Old Saxon nithar, Old English niþer, Old Icelandic niðr 'down; downward', Old High German nidana, Old Saxon nithana 'under', Old English neodan, niþan 'down, downward, under'\\\"; and under sed-: \\\"ni-zd-os, -om 'nest' ... Old High German Old English nest n. 'nest'\\\".\"\n            },\n            {\n              \"src\": \"IEC\",\n              \"where\": \"Mann, Indo-European Comparative Dictionary, s.v. nisdos (IEC.txt line 11761)\",\n              \"stance\": \"supports\",\n              \"note\": \"\\\"nisdos (nizdos) 'seat, nest'. WP II, 485 Skt. nīḍáḥ ... 'abode, nest'; Arm. nist, gs nsti 'seat'; Lat. nīdus 'nest'; MIr net; Br. neiz; W nyth; Cor. nyth; OHG, OE, Du. nest, n. id.; Sw. näste, id. (The initial of Li. lizdas, Latv. lizds unexplained)\\\".\"\n            },\n            {\n              \"src\": \"WLD\",\n              \"where\": \"Walde-Pokorny Bd. II 335\",\n              \"stance\": \"supports\",\n              \"note\": \"\\\"ahd. nidar, as. nithar, ags. niþer, aisl. niðr 'niederwärts' (und Zubehör, s. J. Schmidt KZ. 26,31, Falk-Torp u. ned), ahd. nidana, as. nithana 'unten', ags. neodan, niþan 'herunter, unter'\\\".\"\n            }\n          ]\n        },\n        {\n          \"id\": 10,\n          \"lang\": \"English\",\n          \"words\": \"beneath, underneath; nest\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"All three English words are textbook cases. beneath < ME benethe, beneothen < OE beneoþan, a compound of be- 'by' + neoþan 'below, beneath' (< Gmc *nith-, node 9); underneath < ME undernethe < OE underneoþan, likewise under + neoþan — Klein treats them together and cross-refers both to 'nether'. nest < OE nest 'bird's nest; snug retreat', from PGmc *nistaz < PIE *nizdo-, whence also Lat. nīdus, Skt. nīḍá-, OIr. net, W nyth, OCS gnězdo (with a folk-etymological g-), Lith. lizdas; the modern spelling and sense are unchanged since Old English, with the transferred senses ('nest of drawers', 'nest egg' 1700) all late Middle English and later. Etymonline: \\\"Old English nest 'bird's nest; snug retreat' ... from Proto-Germanic *nistaz ... from PIE *nizdo- ... probably from *ni 'down' + from PIE root *sed- (1) 'to sit'.\\\" The box carries no reference of its own, but the two arrows drawn (Gmc nith → beneath, underneath; Gmc nist → nest) are exactly Watkins's own word lists under ni and nizdo-.\",\n          \"derivation_fa\": \"هر سه واژهٔ انگلیسی نمونه‌های درسی‌اند. beneath از انگلیسی میانهٔ benethe و انگلیسی کهنِ beneoþan، ترکیبِ be- «به، نزد» و neoþan «پایین، زیر» (از ژرمنیِ *nith- جعبهٔ پیشین)؛ underneath از انگلیسی میانهٔ undernethe و انگلیسی کهنِ underneoþan، به همان‌سان under + neoþan؛ کلاین هر دو را با ارجاع به nether می‌آورد. nest از انگلیسی کهنِ nest «آشیانهٔ پرنده، کُنجِ آسوده»، از ژرمنیِ آغازینِ *nistaz از هندواروپاییِ *nizdo- که لاتینِ nīdus، سنسکریتِ nīḍá-، ایرلندی کهن net، ولزی nyth، اسلاوی کلیسایی gnězdo (با گِ ریشه‌شناسیِ عامیانه) و لیتوانیِ lizdas نیز از آن‌اند؛ املا و معنیِ آن از انگلیسی کهن تا امروز دست‌نخورده مانده و معناهای گسترش‌یافته («nest of drawers»، «nest egg» ۱۷۰۰) همه متأخرند. این جعبه ارجاعی از خود ندارد، ولی دو پیکانی که کشیده شده دقیقاً همان فهرستِ واژه‌هایی است که واتکینز ذیل ni و nizdo- می‌آورد.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/nest\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"None\",\n              \"status\": \"not_checked\",\n              \"note\": \"The English box prints no reference (JSON refs=null, confirmed on the page image: the box header 'English' carries no book icon). The parent's AHD; KLN:1042 were checked instead and both cover these three words.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein 1966 s.v. beneath (KLN_1966.txt line 4740), underneath (line 40767), nest (line 25295)\",\n              \"stance\": \"supports\",\n              \"note\": \"\\\"beneath, prep. and adv. — ME. benethe, beneothen, fr. OE. beneoþan, fr. be-, 'by', and neoþan, 'below, beneath'. See be- and nether and cp. underneath.\\\" · \\\"underneath, adv. and prep. — ME. undernethe, fr. OE. underneoþan. See under and nether and cp. beneath.\\\" · \\\"nest ... I.-E. *niz-do-, stands for *ni-zd-o- and lit. means 'a place to sit down in' ... See nether and sedentary and cp. eyas, nidus, nidificate. Cp. also nestle.\\\"\"\n            },\n            {\n              \"src\": \"AHD\",\n              \"where\": \"Watkins 1985, s.v. ni and nizdo-; index entries NEST, NESTLE, NICHE, NIDE, NIDUS, EYAS\",\n              \"stance\": \"supports\",\n              \"note\": \"s.v. ni the English derivatives listed are exactly \\\"BENEATH, UNDERNEATH\\\" and \\\"NETHER\\\"; s.v. nizdo- \\\"Old English nest, nest: NEST\\\" plus the Latin branch \\\"nīdus, nest: NICHE, NIDE, NIDUS; EYAS, NIDIFY\\\".\"\n            },\n            {\n              \"src\": \"SKT\",\n              \"where\": \"Skeat, Concise Etymological Dictionary (SKT.txt)\",\n              \"stance\": \"silent\",\n              \"note\": \"Skeat's 'Nest' entry could not be located in the local OCR: the N-section around line 12225 is badly scrambled (grep for 'Nest', 'nizdo', 'nisdo' returns nothing), so the English side rests on Klein, Watkins and Etymonline here.\"\n            }\n          ]\n        }\n      ]\n    }\n  ]\n}\n"
}
```


### [2026-09-07T19:54:50.398Z] TOOL RESULT

```
File created successfully at: /home/sfmqrb/git/rishe/data/verification/page-365.json (file state is current in your context — no need to Read it back)
```


## [2026-09-07T19:54:54.105Z] TOOL CALL #105: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-365.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 365",
 "description": "Validate and run verify_check"
}
```


### [2026-09-07T19:54:56.751Z] TOOL RESULT

```
JSON OK
nodes verified: 10/10
node verdicts: {'confirmed': 5, 'plausible': 5}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 17, 'partial': 1, 'not_checked': 3}
books consulted: {'supports': 31, 'silent': 4, 'partial': 3} | by book: {'CHEUNG': 7, 'HRN': 5, 'PHD': 5, 'KNT': 3, 'POK': 3, 'BQT': 3, 'NYB': 2, 'BRT': 2, 'MON': 1, 'SOD': 1, 'HUB': 1, 'IEC': 1, 'WLD': 1, 'KLN': 1, 'AHD': 1, 'SKT': 1}
```


## [2026-09-07T19:55:23.810Z] AGENT

Done. `data/verification/page-365.json` written; `verify_check.py 365` reports **0 PROBLEM lines** (10/10 nodes).

**Page 365 (book p. 335) — root Nî 1 "down, below" [Indo-European], 3 redirect entries skipped**

- Verdicts: root **confirmed**; nodes **5 confirmed** (#1, #2, #8, #9, #10) / **5 plausible** (#3, #4, #5, #6, #7). No `disputed`, no `transcription_suspect`.
- Ref checks: 17 `supports`, 1 `partial`, 3 `not_checked`. Nourai's citations are unusually accurate here: KLN:1042 = Klein s.v. *nether*; POK:884 = `sed-` (884–887, with `ni-zd-os` and Av. *nišhiδaiti*); POK:235 = `dhē-2`; POK:454 = `ghous-`, which itself prints "npers. niyōšīdan"; HRN:233 = Horn no. 1042 *numūdan* "ni + √mā-"; HRN:238 = no. 1063 *niyām* "ap. *nigāma-, Unsicher"; BQT:2134/2145/2147/2201/2211/2171 all land on the right Mo'in footnotes; **SOD:237/244/252 are exactly Gharib's pages for nyγrwβs- "©Av. niγərəpta", nsty- "<*ni-stāya; OP niyastāya", nypδ- "<Av. ni-paiδya-"**.
- `not_checked`: MON:4812 (only the 2-vol Adena abridgement is on disk; the 6-vol pagination cannot be mapped) plus nodes #5 and #10, which print no reference at all.

Word-level problems worth the owner's attention (all argued in the JSON, none severe enough for `disputed`):
- **نژند (nažand)** — rests only on Horn no. 1031's *ni-jantu-*, expressly "Unsicher", repeated by Mo'in as «مفروض است»; no attested form explains -and.
- **نیام / ni-gāma** — Horn "Unsicher"; Gharib does back *\*ni-gāma* (Sogd. ny'm), but Wiktionary (after Wolff 829b, Shapira 2009) prefers OP *\*ni-dā-mān-* "covering" (cf. Skt. *nidhānam*). Prefix agreed, second member contested.
- **نگون / nî-gaona** — Mo'in (BQT 2165) + Hübschmann §32 (p. 142) support ni- + *gaona-*; Wiktionary only compares Skt. *nyañc-* (= ni- + *\*h₃ekʷ-*).
- **Two wrong cross-reference roots in the book**: "☞Angh" for *ni-az* (Cheung: *\*ni-Haz* "to drive down, straiten", PIE *\*h₂eǵ-*, Pok. 4 ff., not *\*anǵʰ-* Pok. 42) and "☞Ôus 1" for *ni-gaoša* (Pokorny files Av. *gaoša-* under the Indo-Iranian-only `ghous-` 454, not *\*ous-* 785). Nourai's own "Ped?" query on *ni-paidhya* is resolved: Cheung gives PIE *\*ped-*, Pok. 791.
- Three Avestan forms are printed without the asterisk Horn gives them: *\*ni-xšvaēpa-*, *\*ni-parət-*, *\*ni-gāma-*. Node 8's box is labelled "Avestan" but *ni-yaštāya* is Old Persian/Sogdian.

**Extraction error for the owner to fix:** on the printed page (verified on `site/pages/365.jpg` and a 300 dpi render, copied to `data/verification/sources/refs/ocr/BOOK/365.png`) the Avestan/SOD box (node #8) has an arrow into an **empty, unlabelled box** on the right; `data/extracted/batch/page-365.json` records no node for it. Everything else in the JSON matches the page exactly, including all Persian-script extras and the two poet quotes (Ferdowsī, Hāfez).
