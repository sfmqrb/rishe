# Verification process log — verify-page-290


## [2026-09-06T22:04:46.828Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 290 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-290.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-290.json. Write /home/sfmqrb/git/rishe/data/verification/page-290.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 290` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-06T22:04:48.215Z] AGENT

I'll start by reading the instructions.


## [2026-09-06T22:04:48.672Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-06T22:04:48.687Z] TOOL RESULT

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


## [2026-09-06T22:04:49.224Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-290.txt"
}
```


### [2026-09-06T22:04:49.236Z] TOOL RESULT

```
1	=== PDF page 290 (book page 260) ===
2	--- entry 0 ---
3	ROOT Kweit -> redirect to Kuei
4	--- entry 1 ---
5	ROOT [Indo-European] Kwek, Qwek : to appear, see, show  (refs POK:638)
6	#1 (parent #0) [Avestan] refs=POK:638; KLN:42; SYN:1436 | kas, čas, čaš : to behold, see, taste ; čašman : eyes ; â-kasat : he saw, is informed ; ni-kasa : look ☞Nî 1 ; vi-kâs, vi-kaya, vi-či : see apart, distinguish ☞Wi
7	  #2 (parent #1) [Persian] refs=BQT:52,638,1849,2163; HRN:210 | čašm «چشم» : eye ; âgâh «آگاه» : aware ; negâh «نگاه» : look ; govâh «گواه» : witness
8	  #3 (parent #1) [Pahlavi] refs=ISS:98 | čâšišn : taste ; čâšîtan : to taste
9	    #4 (parent #3) [Persian] refs=ISS:98 | čašîdan «چشیدن» : to taste ; čâšt «چاشت» : morning meal | extra: چشایی ، چاشنی
10	--- entry 2 ---
11	ROOT [Indo-European] Kwel, Qwel : to move around, dwell  (refs POK:640)  PART 1
12	#1 (parent #0) [Avestan / Old Persian] refs=POK:640; BQT:629; SYN:725,905 | čaxra, čakra, caxra : wheel
13	  #2 (parent #1) [Persian] refs=None | čarx «چرخ» : wheel
14	#3 (parent #0) [Avestan] refs=BQT:635; DRM; FFD:73 | car, čâr : to move around, graze ; wi-čâr : to do ☞Wi
15	  #4 (parent #3) [Pahlavi] refs=None | čâr : to graze ; vâ-čar : place to get together, bazaar ☞Abâ ; wîzârdan : to do, translate
16	    #5 (parent #4) [Persian] refs=MON:1268; BQT:614; FFD:73 | čarîdan «چریدن» : to graze ; zâr 2 «-زار ۳» : place of, home of ; bâzâr «بازار» : "place of assembly", bazaar ; gozârdan «گزاردن» : to do, translate | extra: بازرگان ، گلزار ، کارزار ، مرغزار ، چمنزار ، علفزار ، گزارش ، گزاره ، گزیر ، ناگزیر
17	      #6 (parent #5) [Turkish] refs=AHD | 
18	        #7 (parent #6) [Italian] refs=None | 
19	          #8 (parent #7) [English] refs=AHD | bazaar
20	#9 (parent #0) [Sanskrit] refs=POK:639 | cal : to move
21	  #10 (parent #9) [Persian] refs=BQT:639 | čalîdan «چلیدن» : to walk proudly ; čâlâk «چالاک» : quick, fast ; čâleš «چالش» : struggle, quarrel | extra: چالیدن
22	#11 (parent #0) [Sogdian] refs=SOD:131 | cxr : wheel
23	#12 (parent #0) [Avestan] refs=POK:639; SOD:203 | kar 2, karša : to plow ; karaya : to sow
24	  #13 (parent #12) [Pahlavi] refs=SNS:220 | kištan : to plow, sow, plant
25	    #14 (parent #13) [Persian] refs=BQT:1567; HRN:185 | kâštan «کاشتن» : to plant ; kârîdan 1 «کاریدن ۱» : to plant | extra: کِشتن ، کِشت ، کشاورز ، کار ۳
26	
```


## [2026-09-06T22:04:51.805Z] AGENT

I'll read the source JSON and the reference infrastructure.


## [2026-09-06T22:04:53.916Z] TOOL CALL #3: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/extracted/batch/page-290.json'))\nprint(json.dumps(d,ensure_ascii=False,indent=1)[:8000])\n\"",
 "description": "Read page 290 source JSON"
}
```


## [2026-09-06T22:04:54.192Z] TOOL CALL #4: Bash

```json
{
 "command": "sed -n '1,200p' data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-06T22:04:55.802Z] TOOL RESULT

```
{
 "pdf_page": 290,
 "book_page": 260,
 "entries": [
  {
   "root": {
    "name": "Kweit",
    "redirect": "Kuei"
   },
   "nodes": []
  },
  {
   "root": {
    "name": "Kwek, Qwek",
    "lang": "Indo-European",
    "refs": "POK:638",
    "gloss": "to appear, see, show"
   },
   "nodes": [
    {
     "id": 1,
     "parent": 0,
     "lang": "Avestan",
     "refs": "POK:638; KLN:42; SYN:1436",
     "words": [
      {
       "translit": "kas, čas, čaš",
       "gloss": "to behold, see, taste",
       "script": null
      },
      {
       "translit": "čašman",
       "gloss": "eyes",
       "script": null
      },
      {
       "translit": "â-kasat",
       "gloss": "he saw, is informed",
       "script": null
      },
      {
       "translit": "ni-kasa",
       "gloss": "look",
       "script": null,
       "see": [
        "Nî 1"
       ]
      },
      {
       "translit": "vi-kâs, vi-kaya, vi-či",
       "gloss": "see apart, distinguish",
       "script": null,
       "see": [
        "Wi"
       ]
      }
     ],
     "script_extra": null,
     "note": null,
     "quote": null
    },
    {
     "id": 2,
     "parent": 1,
     "lang": "Persian",
     "refs": "BQT:52,638,1849,2163; HRN:210",
     "words": [
      {
       "translit": "čašm",
       "gloss": "eye",
       "script": "چشم"
      },
      {
       "translit": "âgâh",
       "gloss": "aware",
       "script": "آگاه"
      },
      {
       "translit": "negâh",
       "gloss": "look",
       "script": "نگاه"
      },
      {
       "translit": "govâh",
       "gloss": "witness",
       "script": "گواه"
      }
     ],
     "script_extra": null,
     "note": null,
     "quote": null
    },
    {
     "id": 3,
     "parent": 1,
     "lang": "Pahlavi",
     "refs": "ISS:98",
     "words": [
      {
       "translit": "čâšišn",
       "gloss": "taste",
       "script": null
      },
      {
       "translit": "čâšîtan",
       "gloss": "to taste",
       "script": null
      }
     ],
     "script_extra": null,
     "note": null,
     "quote": null
    },
    {
     "id": 4,
     "parent": 3,
     "lang": "Persian",
     "refs": "ISS:98",
     "words": [
      {
       "translit": "čašîdan",
       "gloss": "to taste",
       "script": "چشیدن"
      },
      {
       "translit": "čâšt",
       "gloss": "morning meal",
       "script": "چاشت"
      }
     ],
     "script_extra": "چشایی ، چاشنی",
     "note": null,
     "quote": null
    }
   ]
  },
  {
   "root": {
    "name": "Kwel, Qwel",
    "lang": "Indo-European",
    "refs": "POK:640",
    "gloss": "to move around, dwell"
   },
   "part": 1,
   "nodes": [
    {
     "id": 1,
     "parent": 0,
     "lang": "Avestan / Old Persian",
     "refs": "POK:640; BQT:629; SYN:725,905",
     "words": [
      {
       "translit": "čaxra, čakra, caxra",
       "gloss": "wheel",
       "script": null
      }
     ],
     "script_extra": null,
     "note": null,
     "quote": null
    },
    {
     "id": 2,
     "parent": 1,
     "lang": "Persian",
     "refs": null,
     "words": [
      {
       "translit": "čarx",
       "gloss": "wheel",
       "script": "چرخ"
      }
     ],
     "script_extra": null,
     "note": null,
     "quote": null
    },
    {
     "id": 3,
     "parent": 0,
     "lang": "Avestan",
     "refs": "BQT:635; DRM; FFD:73",
     "words": [
      {
       "translit": "car, čâr",
       "gloss": "to move around, graze",
       "script": null
      },
      {
       "translit": "wi-čâr",
       "gloss": "to do",
       "script": null,
       "see": [
        "Wi"
       ]
      }
     ],
     "script_extra": null,
     "note": null,
     "quote": null
    },
    {
     "id": 4,
     "parent": 3,
     "lang": "Pahlavi",
     "refs": null,
     "words": [
      {
       "translit": "čâr",
       "gloss": "to graze",
       "script": null
      },
      {
       "translit": "vâ-čar",
       "gloss": "place to get together, bazaar",
       "script": null,
       "see": [
        "Abâ"
       ]
      },
      {
       "translit": "wîzârdan",
       "gloss": "to do, translate",
       "script": null
      }
     ],
     "script_extra": null,
     "note": null,
     "quote": null
    },
    {
     "id": 5,
     "parent": 4,
     "lang": "Persian",
     "refs": "MON:1268; BQT:614; FFD:73",
     "words": [
      {
       "translit": "čarîdan",
       "gloss": "to graze",
       "script": "چریدن"
      },
      {
       "translit": "zâr 2",
       "gloss": "place of, home of",
       "script": "-زار ۳"
      },
      {
       "translit": "bâzâr",
       "gloss": "\"place of assembly\", bazaar",
       "script": "بازار"
      },
      {
       "translit": "gozârdan",
       "gloss": "to do, translate",
       "script": "گزاردن"
      }
     ],
     "script_extra": "بازرگان ، گلزار ، کارزار ، مرغزار ، چمنزار ، علفزار ، گزارش ، گزاره ، گزیر ، ناگزیر",
     "note": null,
     "quote": {
      "text": "اگر گفتم دعای می فروشان - چه باشد حق نعمت میگزارم",
      "poet": "Hâfez"
     }
    },
    {
     "id": 6,
     "parent": 5,
     "lang": "Turkish",
     "refs": "AHD",
     "words": [],
     "script_extra": null,
     "note": null,
     "quote": null
    },
    {
     "id": 7,
     "parent": 6,
     "lang": "Italian",
     "refs": null,
     "words": [],
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
      {
       "translit": "bazaar",
       "gloss": null,
       "script": null
      }
     ],
     "script_extra": null,
     "note": null,
     "quote": null
    },
    {
     "id": 9,
     "parent": 0,
     "lang": "Sanskrit",
     "refs": "POK:639",
     "words": [
      {
       "translit": "cal",
       "gloss": "to move",
       "script": null
      }
     ],
     "script_extra": null,
     "note": null,
     "quote": null
    },
    {
     "id": 10,
     "parent": 9,
     "lang": "Persian",
     "refs": "BQT:639",
     "words": [
      {
       "translit": "čalîdan",
       "gloss": "to walk proudly",
       "script": "چلیدن"
      },
      {
       "translit": "čâlâk",
       "gloss": "quick, fast",
       "script": "چالاک"
      },
      {
       "translit": "čâleš",
       "gloss": "struggle, quarrel",
       "script": "چالش"
      }
     ],
     "script_extra": "چالیدن",
     "note": null,
     "quote": {
      "text": "زگرز گران سنگ چالشگران - شده ماهی و گاو را سر گران",
      "poet": "Nezâmî"
     }
    },
    {
     "id": 11,
     "parent": 0,
     "lang": "Sogdian",
     "refs": "SOD:131",
     "words": [
      {
       "translit": "cxr",
       "gloss": "wheel",
       "script": null
      }
     ],
     "script_extra": null,
     "note": null,
     "quote": null
    },
    {
     "id": 12,
     "parent": 0,
     "lang": "Avestan",
     "refs": "POK:639; SOD:203",
     "words": [
      {
       "translit": "kar 2, karša",
       "gloss": "to plow",
       "script": null
      },
      {
       "translit": "karaya",
       "gloss": "to sow",
       "script": null
      }
     ],
     "script_extra": null,
     "note": null,
     "quote": null
    },
    {
     "id": 13,
     "parent": 12,
     "lang": "Pahlavi",
     "refs": "SNS:220",
     "words": [
      {
       "translit": "kištan",
       "gloss": "to plow, sow, plant",
       "script": null
      }
     ],
     "script_extra": null,
     "note": null,
     "quote": null
    },
    {
     "id": 14,
     "parent": 13,
     "lang": "Persian",
     "refs": "BQT:1567; HRN:185",
     "words": [
      {
       "translit": "kâštan",
       "gloss": "to plant",
       "script": "کاشتن"
      },
      {
       "translit": "kârîdan 1",
       "gloss": "to plant",
       "script": "کاریدن ۱"
      }
     ],
     "script_extra": "کِشتن ، کِشت ، کشاورز ، کار ۳",
     "note": null,
     "quote": null
    }
   ]
  }
 ]
}
```


### [2026-09-06T22:04:55.836Z] TOOL RESULT

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
```


## [2026-09-06T22:05:41.814Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','KLN','SYN','BQT','HRN','ISS','SOD','SNS','MON','FFD','AHD','DRM','WLD','PHD','BRT','CHEUNG','KNT','NYB','IEC','ARY','HUB']:\n    v=d.get(k)\n    print(k, json.dumps(v,ensure_ascii=False)[:400] if v else 'MISSING')\n\"",
 "description": "Inspect refs_online entries"
}
```


## [2026-09-06T22:05:42.282Z] TOOL CALL #6: Bash

```json
{
 "command": "sed -n '1,80p' tools/verify_check.py",
 "description": "Read verify_check tool"
}
```


### [2026-09-06T22:05:43.291Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 
ISS {"title": "H. W. Bailey, Indo-Scythian Studies: Khotanese Texts VI (Prolexis to the Book of Zambasta), Cambridge 1967", "edition_found": "not found; Bailey's Dictionary of Khotan Saka (1979) downloaded as the closest substitute", "kind": "google_books_preview+archive_restricted", "url": "https://books.google.com/books?id=4upthUgWo9YC (CUP 2009 reprint, partial preview) ; HathiTrust mdp.39015034317
SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in 
SNS {"title": "Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/VajnameShayest", "lookup_hint": "grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
FFD {"title": "Mohsen Abolghasemi, Fe'l-ha-ye Farsi-ye Dari, Qoqnus, Tehran 1374/1995", "kind": "local_scan_ocr", "url": "https://asmaneketab.ir/product/کتاب-ماده-های-فعلهای-فارسی-دری-محسن-اب/ -> https://dl.eliteraturebook.com/app/public/attachments/6925d29630b83.PDF (free PDF site; grey)", "lookup_hint": "Searched archive.org (Persian/Latin titles, author), ketabnak, noorlib, general web (pdf/downloa
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
DRM {"title": "J. Darmesteter, Études iraniennes, 2 vols., Paris 1883", "edition_found": "1883 both tomes in one scan", "kind": "archive_djvu", "url": "https://archive.org/details/etudesiraniennes00darm", "identifier": "etudesiraniennes00darm (t.1 alone: tudesiranienne01darmuoft; t.2 alone: darmesteter-etudes-sur-la-langue-la-litterature-les-croyances-de-la-perse-ancienne)", "local_file": "/home/sfmqr
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sou
CHEUNG MISSING
KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "loca
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verific
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1
```


### [2026-09-06T22:05:43.319Z] TOOL RESULT

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


## [2026-09-06T22:05:47.577Z] TOOL CALL #7: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','KLN','SYN','BQT','HRN','ISS','SOD','SNS','FFD','BRT','PHD','MON']:\n    v=d[k]\n    print('==',k, v.get('page_offset'), '|', v.get('lookup_hint','')[:300])\n\"",
 "description": "Page offsets and hints"
}
```


### [2026-09-06T22:05:49.502Z] TOOL RESULT

```
== POK POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' giv
== KLN KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.
== SYN leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the concept heading (all caps English word) or a printed page number line.
== BQT vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...'). | grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --d
== HRN leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.
== ISS DKS: leaf = printed + 17..19 (e.g. leaf 158 = p.139). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Khotanese Texts VI itself is not online. Nourai's ISS page numbers cannot be checked directly; the Dictionary of Khotan Saka (headword at line start, Khotanese in transliteration, with 'Pok.' refs) covers the same etymological material and can verify the substance of a claim.
== SOD printed page ≈ leaf − 66 in SOD_pages.txt (0-based \f blocks; 645 leaves; English intro precedes) | Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (retur
== SNS 242 leaves; page offset not determined (OCR too poor to read printed numbers) — locate by transliteration then read the page image | grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php search (see BQT) for better hit-to-leaf mapping.
== FFD 115 leaves (PDF pages); printed page = PDF page − 5 (PDF 40 = p.35). 2nd printing 1385 of the same Qoqnus setting (ISBN 964-311-015-X). | Searched archive.org (Persian/Latin titles, author), ketabnak, noorlib, general web (pdf/download): nothing; only a related paid e-book 'واژگان زبان فارسی دری' (fidibo). ketabnak.com/book/45024 is a different book (فهرست فعلهای فارسی).
== BRT Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Nourai's BRT numbers are Bartholomae's COLUMN numbers. Headwords are Avestan/OP in transliteration in bold at line start; OCR of the special transliteration is noisy - grep on a distinctive Latin gloss or the German meaning in quotes. Column numbers appear as standalone numbers at leaf tops.
== PHD leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Headword = Pahlavi in transliteration at line start, followed by Pahlavi script (not OCRed) and gloss, e.g. grep -n '^abar '. Alternative PDF: https://www.parsianjoman.org/wp-content/uploads/2015/09/A-Concise-Pahlavi-Dictionary.pdf (8.4 MB).
== MON None | Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbe
```


## [2026-09-06T22:05:50.105Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"k\\^ue\\|kʷek\\|kuek̑\\|k\\*ue\" POK_full.txt | head -20; echo \"---\"; grep -n \"638\\]\\|\\[pdf page\" POK_full.txt | head -5",
 "description": "Search POK for kwek root"
}
```


### [2026-09-06T22:05:50.166Z] TOOL RESULT

```
---
```


## [2026-09-06T22:05:53.649Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Page(s): 63[89]\" POK_full.txt | head -20; echo ---; grep -n \"Page(s): 64[01]\" POK_full.txt | head",
 "description": "Find POK pages 638-641"
}
```


### [2026-09-06T22:05:53.717Z] TOOL RESULT

```
52608:Page(s): 638 
52636:Page(s): 638-639 
52758:Page(s): 639-640 
---
52780:Page(s): 640 
52806:Page(s): 640 
52834:Page(s): 640-641 
52860:Page(s): 641 
52891:Page(s): 641 
52935:Page(s): 641-642
```


## [2026-09-06T22:05:55.920Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '52580,52660p' POK_full.txt",
 "description": "Print POK 638 entry"
}
```


### [2026-09-06T22:05:55.977Z] TOOL RESULT

```
Root / lemma: Iceia-, k''lie-{*IC'ehu-es) Note: common Proto Germanic -u- > -u-, -y-, -/-. 
Meaning: to rest quietly, quiet, peaceful 

Material: Old Indie cira-m^ indecisiveness, delay', cira-^ lasting, continuing; ongoing, long 
'; Old pers. siyati-s^ complacency ' (= Latin quies), Avestan sa///-5 "pleasure, joy' {s- = sy-, 
compare gathav. syeitibyd), Avestan syata-, sata- " pleases ' (= Latin quietus), a-sata- " 
unhappy ' (= Latin inquietus), Flapu-aaTK;, Avestan saista- " most cozily, most gratifyingly ', 
np. sao' "blithe, glad', oss. ancayun^x^^'C; sogd. sV gleeful '; 

Armenian han-gcim^\ lie, rest ', han-gisV tranquility ' {-g'h from *-k"i-)\ 

Latin quies, -etis' tranquility ', quie-sco, -scere, -vT, -turn 'rest', with formants -/c»-(as 
Germanic 77by/7-) tranquTius, tranquiiius' peaceful' {trans + kfios); 

Maybe alb. ^e/e "quiet' a Latin loanword. 

Gothic tveila. Old English fiwJl, Old High German (ii)wJla " while, time'. Old Icelandic 
/7i//7a "couch, bed, place for resting ', hvlld' tranquility ', Gothic fveiian' stay, linger, 
hesitate, cease'. Old English HwaiaUH, Old High German wTion, -en' stay, linger'; 

Old Church Slavic pokojb " tranquility ', pokojg, pokojiti' calm, appease ', pocijg, pociti 
"rest'; 

Tocharian B sa/e"rich' (: Avestan syata-' pleases '); 

Lycian tezi' sarcophagus ' from *k"jetis{'7), Pedersen Lycian and Hittite 50. 

References: WP. I 510, WH. II 406, Trautmann 124. 
Page(s): 638 



Root / lemma: IceR-, IcoR-, IceR-s- {* k^ehuR-s-) 

Meaning: to seem, see, show 

Material: Old Indie /ras'a/e 'appears, glares, gleams, shines', cakasiti, ca/ras/a/e "shines, 

looks ', kasa-'C(\. ' being visible, shine'; 

Avestan akasaV perceives '; npers. 5^5/7 "expert, skillful', /7/ga/7 "sight'; s-extension 
k'^eks-. Old Indie caste {"i. PI. caksat§) "appears; beholds ', in compounds also " announce, 
show', caksas-v\. "shine, face', caksu-^ seeing ', n. " brightness, face, eye'; Avestan 
cas(te, -5/fey) "instruct, teach' (actually " allow to notice '), Middle Persian das/7a/7 "instruct, 
teach', Avestan Old pers. casman- n. "eye', npers. casm, ds.; (common Old Indie gh- > ks- 
: Old pers. gh- > xs- : Middle Persian xs- > s-) 

gr. TEKjjojp, young TSKjjap (after TSKjjaipu)) "mark, token, sign, feature, characteristic 
mark or property' ( *k"ek-m[d]r-l); different Schwyzer Gr. Gr. I 326; 

with voiced final sound Old Church Slavic kazQ, kazaf/^s\r\o\N, urge, remind', u-kazb " a 
showing forth, exhibiting, a setting forth, exposition, proving, proof ' (also kaznb " decision, 
judgement, alignment '), probably Indo Germanic *k"eg-bes\6es *k"ek-l common Old Indie 
gh- > ks- : Slavic gh- > z-, z- 

References: WP. I 510 f., Schwyzer Gr. Gr. I 326, 519. 
Page(s): 638-639 

Root / lemma: k^'e-l {*k''ehu-) 
See also: s. unk^o- 
Page(s): 636 

Root /lemma: k^el-l, k''el9-{*k'^ehulah-) 
Meaning: to turn; wheel; neck? 
Material: 

In a- grade: 

Old Indie carati, calatT moves, walks, grazes, drives ' etc. (heavy basis in caritum, carita-, 
cTrna-, carftra-v\. "foot, leg', carcOryamana-, curtf-, also probably tuvi-kOrmf-^ energetic, 
vigorous '), lengthened grade cara-m. " way ', etc.; Avestan caraiti^ versatur, obliegt einer 
Tatigkeit ' etc., carana-^i\e\6\ Old pers. parikara^cuWSyaieY; 

s-extension in Old Indie karsu-f. "furrow, headland ', karsati, krsatr turn over, rotate 
something, plow ', Avestan karsa-m. n. "furrow', karsa/t/"r\6ge, mark with ridges '; 



Tocharian A kallas^ brings ', preterit sel, PI. /ra/5/'(Pedersen Tocliar. 183). 

In e- grade:
```


## [2026-09-06T22:06:04.766Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '52660,52790p' POK_full.txt",
 "description": "Print POK kwel-1 entry"
}
```


### [2026-09-06T22:06:04.842Z] TOOL RESULT

```
In e- grade: 

alb. sjel, sjeir turn round, twist, turn over, bring' {*k"'el-)\ besides A/e/"bring, bear' 
{*k"'oleid), a-sur willow ', sule " boat ', (Note: Occidental (western) Romance languages 
prefix e-, a-), per-kul, perku/'bend, curve ' ( *k"'e/-n-), kulp, kulper, kulpra " forest shoot 
'(*A-V-bh-); 

Balto Slavic */re//^-"knee' in Lithuanian kelys. East Lithuanian /re/zas "knee', Latvian 
cell's 6s.\ Lithuanian kelenasm. 'knee', ablaut. Old Church Slavic kolenou. "knee, stem, 
gender', perhaps further to Slavic *ce/nbn\., sloven, d/e/7 'joint, limb, member', kir. ceMn 
'limb, member'; 

Gothic Old Icelandic asachs. {* heals) halsm., Old English heals, Modern High German 
Hals' neck '; Old Icelandic hveln. 'wheel' = 

Old Prussian kelan'wheeV, Latvian f. PI. du-celes' 2-wheeled cart '; 

gr. nsAu), nsAopai 'be in motion ' (tt Aeolic), Aor. ettAeto, participle n£pinA6|j£V0(; 'to 
move round, be round about', with Aeolic t£- = */r"'e-.n£piT£AA6|j£V0(; in the meaning 
(teAAu) ' accomplish, perform duties, rites, etc, make to arise ' Pind.), hom. izkzQod 'be, 
become', Cretan T£Aopai ' to be, to exist ', Cypriot T£VTai 'he will be ', also itkoq n. 'coming 
to pass, performance, consummation, power of deciding, supreme power, magistracy, 
office, decision, doom, something done or ordered to be done, task, service, duty, services 
or offerings due to the gods, state of completion or maturity, completion, end, finish, full 
realization, highest point, ideal, the end or purpose of action ' (t£A£U) ' finish, complete, 
bring to an end, accomplish, execute, perform ', itkeioq, itkzoqirom *izkzo-Fo-q ' perfect, 
of victims, entire, without spot or blemish, fully constituted, valid, of animals, full-grown, 
married, of persons, accomplished, perfect in his kind, in relation to quality, of prayers, 
vows, etc., fulfilled, accomplished, of numbers, full, complete, of the gods, having power to 
fulfil prayer, mature, ripe, mellow, seasoned, grown', T£A£UTn ' consummation, termination, 
end'), wherefore teAgov (*T£AaFov, compare above Old Indie karsu-) ' furrow, headland ', 
i.e. ' headland, i.e. land where the plough turned '; 

In o- grade: 

gr. tt6Ao(; " piuot on which anything turns, axis, axis of the celestial sphere, pole-star, 
celestial sphere, vault of heauen, sky, orbit of a star, crown of the head, centre of the 
circular threshing-floor, pole passing through the axle-tree of a carriage, as a shock- 



absorber, concave sun-dial (called polos from being shaped like the vault of heaven), on 
which the shadow was cast by the interpreter, head-dress, worn by goddesses ', ttoAeu) 
"go about, range ouer, haunt, revolve, turn up the earth with the plough, plough ', 
aiJcpinoAoq ' maid (Hom.), servant' = Latin anculus^ a man-servant ', ain6Ao(; ' nanny goat 
shepherd ', GeottoAeu) ' minister in things divine ' (besides Geh-koAoc; 'priest'); with k in 
(3ouk6Ao(; " tending kine, worshipper of Dionysos in bull-form, in pi., title of play by 
Cratinus, Osorapi devotee of Sarapis, cattle shepherd ' = Middle Irish buachaill, cymr. 
i&^^a//"herdsman, shepherd' from *k"'o/{/Jos\N\t\r\ labialization after u, 

Maybe alb. ,^5/7^ "herdsman, shepherd' a Celtic loanword. 

ttoAeuu) " turn or go about, the planet presiding ouer a day, turn up the soil with the plough 
' (yf|v " plough up '), Ionian Attic sninoAnq ' on the surface, on the top, uppermost ', spnoAn 
"merchandise, traffic, purchase, gain made by traffic, profit '; nwAsofjai " go up and down 
or to and fro: hence, go or come frequently '; naAiv " of Place, back, backwards, of Time, 
again, once more, in turn ' (Akk. a *TTaAiq ' turn '); kukAo^ see below; the gr. n-forms 
contain probably partly Indo Germanic pe/-see below; 

Latin co/o, -ere^ to till, tend, care for, cultivate ' {*k"eld)\ colonus' a husbandman, tiller 
of the soil ', //7cc»/e/'e "inhabit, to be at home, abide, dwell ', incola^ an inhabitant, resident ', 
inquilTnus^ of foreign birth ', Esquiliae^ the largest of the seven hills of Rome '; about 
anculus " a man-servant ' see above; 

colus, -ust m. or -/"f. "distaff' {*k"elos^ spindle'), collus, -/"m. (Old Latin), collum, -/"n. " 
the neck, the neck (of a flask or bottle), (of the poppy), mountain ridge ' {*k"ol-so-, Gothic 
ha Is); 

Old Irish cur cart ' (Dual. *k^old); Middle Irish coir head' = 

Old Church Slavic kolou.. Gen. /ro/ese "wheel', PI. kola 'cart ' (mixture from k^olo-m. 
and k"eles-v\.)\ 

Icelclo-, k^olclo-il) "wheel' in: 

In a- grade: 

Old Indie cakra-m. n. (pronunciation secondary) " cartwheel, disc, circle ', Avestan 
caxra-m. "wheel'. 

In zero- grade: 



gr. KUKAoq " circle ', PI. kukAoi and kukAq " wheels ' 

In e- grade: 

Old Icelandic hjol, hvel {*k"ek"elon-, Germanic *hweh(w)ula-) n., Old English hweol {ev\Q\. 
wheel), besides hweowol, ^n/eo^o/ (Germanic *hweg{v\/}ula-). Middle Low German wel 
"wheel'; also Frisian fiar\s probably eine dissimilation-form for *hwewla-\ compare also 
Phrygian kIkApiv " big, giant bear ' ('cart '), Lithuanian kaklas, Latvian kokis " neck '; 
Tocharian A kukal, B kokale " cart '. 

Lengthened grade perhaps (as ' twiddled, twisted, rotated, revved, revolved, round ') 
Old Icelandic hva//an6 hollru. (latter from dem Dat. PI. holumiroxw hvalum) 'roundish hill'. 

References: WP. I 514 f., WH. I 45, 245 ff., 250, 846, Trautmann 125. 
Page(s): 639-640 

Root / lemma: lrel-2{*k''ehul-) 

Meaning: far (with regard to place and time) 

Material: 

In a- grade: 

Old Indie carama- ' the last, extreme ', ciras 'chronologically long', gr. naAai ' for a long 

time, since long ago ' (naAai6(; 'old', naAairspoc;, -TaTO(;). 

In e- grade: 

gr. Tf|A£, Aeolic irnAui 'afar, wide' (thAo-Gev, -0i, -as), cymr. corn. bret. peiraiaf {*k"el-s-o- 

?), cymr. pellaFihe extreme'. 

References: WP. I 517. 

Page(s): 640 

Root / lemma: k''el-3{*k''ehul-) 

Meaning: swarm, flock, shoal, school, clan, herd, crowd 

Material: 

In o- grade: 

Old Indie kula-mv\. 'herd, bulk, mass; gender, sex';
```


## [2026-09-06T22:06:24.654Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN leaf 231 (p.210) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==232' HRN.txt | head -60",
 "description": "Horn p.210"
}
```


## [2026-09-06T22:06:25.354Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN leaf 206 (p.185) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==207' HRN.txt | head -60",
 "description": "Horn p.185"
}
```


### [2026-09-06T22:06:26.496Z] TOOL RESULT

```
=== HRN leaf 231 (p.210) ===
— 210 —
gör 'Grab*, dagegen, das Geiger neuerdings (Lautl.
des Bai. 53) mit ai. ghörd- grausig, furchtbar ver-
glichen hat, ist nach Nöldeke, Pers. Stud. II, 41 ein
semitisches Lehnwort. Beiläufig bemerkt, ist türk. LW.
g*aur wohl nicht arab. kaßr (Hübschmann unter oss.
d. gaur, t. daur, S. 123), sondern vielmehr neupers.
gebr, gahr^) (vergl. Geiger, bei. LW. gaur, No. 81,
wo allerdings phlv. gabrä (semitisch!, nur *Mann
bedeutend) nicht als Grundform stehen durfte).
939. guvälfden, gevaltden (falsch k"*) wachsen* (unbelegt);
vergl. bällden (No. 173).
ai. vi + {/^vardh- ^heranwachsen, gedeihen ; ist schon
im PehlevT verschwunden.
940. guvah, guva *Zeuge'.
ai. vi + \/^ka^- Intens, ausschauen, erschauen, wahr-
nehmen'; phlv. gukäs 'Zeuge', gtikasih (M^n.), arm. LW.
vkay *Zeuge', vkayem 'ich bezeuge* 2).
941. gösäle 'Kalb'.
ai. vatsd' 'Kalb, Jährling*.
käfir. vatsala, si^n. botsöri 'Jährling' (Tomaschek,
S. 765).
Das ö in gösäle stammt von go 'Kuh' (No. 888).
942. göspendj gösfend 'Kleinvieh, Schaaf, Widder, Ziege'.
aw. gaospenta- (vd. 21, 1); phlv. göspaud.
943. gas 'Ohr*.
ap. gausa- 'Ohr'; aw. gaosa- 'Ohr*; phlv. gös; ai.
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
«) Vergl. Fr. Müller, WZKM. 5, 263.
```


### [2026-09-06T22:06:28.256Z] TOOL RESULT

```
=== HRN leaf 206 (p.185) ===
1 85 —
K.
/,8:J1. (i)kär *Wcrk, Tlmt\
aw. kära- in käravaitl; plilv. kär; skr. -küra- *i:Iand-
limg, That\
Allgemein entlehnt.
832. (2)'kär 'Tliäter , z. B. in sitahkär, destkar,
ai. -kära- '-tuend'; plilv. -kär,
Vergl. np. gär (No. 884).
■ym, kärd 'Messer.
aw. kareta- Messer ; plilv. kürt; ai. vergl. [/kart-,
kfntdti 'schneiden*.
kurd. kir, ktrd (H.-Sch.); oss. d. t. ßa?'d 'Messer,
d. kärdtm, t. Mrdln 'schneiden'; bei. kärc^ kärca^
n. ßarca (195).
834. kär[»är 'Kampf, Schlachtfeld*, vergl. karJ 'Kämpfer.
phlv. kärejar (y. 11 (8)).
vergl. ap. kära- *Heer'; lit, käras 'Krieg'; ksl. kara
'Zank, Streit'; got. harjis 'Heer.
Das Suffix -eflr ist unklar. Im PehlevT lautet es
'jär, was nicht -cär gelesen werden kann; vergl.
dialektisch grl. käljär (Vullers), Kä§. K. kast^jori —
kistzär.
Fr. Müller (WZKM. 5, ;354) will dasselbe kär in
np. karwän 'Karawane' finden; Nöldeke (mündliche
Mitteilung) stellt hierher np. kärdär 'Vezir .
835. kästen Vermindern, verringern', Praes. käh-eni,
^ kahldefiy Icästi,
phlv. kahltan, kähet, kälünltan, käh{i)sn (Men. s. v.
khah"),
Wohl zu demselben Stamm wie aw. kasu-, np. kih
(No. 877).
y'836. kästen (Sahn. 111, 1544 Vers 842), kisten 'säen',
Praes. kär-em, kist,
g. kastmün,
aw. [/kars-f ya{i\lxarsti, vergl. karsosca frakäroyöis;
```


## [2026-09-06T22:06:39.394Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for L in 32 33 34; do echo \"=== leaf $L ===\"; awk -v n=$L 'BEGIN{RS=\"\\f\"} NR==n+1' KLN_1966.txt | head -30; done",
 "description": "Klein page 42 area"
}
```


### [2026-09-06T22:06:41.119Z] TOOL RESULT

```
=== leaf 32 ===
  —  F.  agilite,  fr.  L.  agilitdtem,  acc.  of agilitas,  ‘mobility,  nimbleness,  quickness  ,  fr. agilis.  See  prec.  word  and  -ity. agio,  n.,  the  discount  paid  to  exchange  one  cur¬ rency  for  another.  —  It.  aggio,  agio,  fr.  dial.  It. lajje,  fr.  MGk.  dXXdyiov,  ’exchange’,  fr.  Gk. dXXayf],  ’change’;  see  allagite.  The  /  in  lajje was  mistaken  for  the  It.  def.  article  and  was accordingly  dropped.
agiotage,  n.  —  F.,  fr.  agioter ,  to  be  a  stock  job¬ ber’,  fr.  agio.  See  prec.  word  and  -age. agist,  tr.  v.,  to  take  cattle  to  graze  at  a  certain prize.  -  OF.  agister,  fr.  a,  ‘to’  (see  a),  and  gister (F.  giter),  ‘to  lodge,  lie’,  fr.  giste  (F.  gite),  ‘lying place,  resting  place’,  fr.  L.  jacita,  fem.  pp.  of L.  jacere,  ‘to  lie’,  used  as  a  noun.  See  jet,  ‘to spirt  forth’,  and  cp.  gist,  ‘essence’.  Cp.  also  ad¬ jacent,  agio.
agistment,  n.,  1)  the  act  of  agisting;  2)  an  agree¬ ment  to  agist;  3)  profit  made  by  agisting.  —
3&
OF.  agistement,  fr.  agister.  See  prec.  word  and
-ment.
agistor,  agister,  n.,  one  who  agists.  —  AF.  agis- tour,  fr.  OF.  agister.  See  agist  and  agential  suff. -or,  resp.  -er.
agitable,  adj.  —  L.  agitabilis,  ‘that  can  easily  be moved’,  fr.  agitare.  See  agitate  and  -able, agitate,  tr.  and  intr.  v.  —  L.  agitates,  pp.  of  agi¬ tare,  ‘to  put  in  constant  motion,  drive,  impel’, freq.  of  agere,  ‘to  move,  drive’.  See  agent,  adj., and  verbal  suff.  -ate  and  cp.  cogitate. Derivatives',  agitat-ed,  adj.,  agitat-ed-ly,  adv., agitation  (q.v.)
agitation,  n.  —  F.,  fr.  L.  agitatidnem,  acc.  of  agi- tatio,  ‘motion,  agitation’,  fr.  agitatus,  pp.  of agitare.  See  agitate  and  -ion.
Derivative:  agitation-al,  adj. agitato,  adj.  agitated  ( musical  direction).  —  It., pp.  of  agitare,  fr.  L.  agitare.  See  agitate, agitator,  n.  —  L.,  fr.  agitatus,  pp.  of  agitare.  See agitate  and  agential  suff.  -or.
Agkistrodon,  n.,  a  genus  of  pit  vipers  (zool.) ModL.,  compounded  of  Gk.  dyxwxpov,  ‘fish¬ hook’,  and  oSdiv,  gen.  680VT09,  ‘tooth’.  The first  element  is  rel.  to  dyxo ‘a  bend,  hollow’, ayxwv,  ‘elbow’,  lit.  ‘the  bend  of  the  arm’,  and cogn.  with  L.  angulus,  ‘angle,  corner  ;  see angle,  ‘corner’.  For  the  second  element  see odonto-.
Aglaia,  n.,  one  of  the  Graces  in  Greek  mythol¬ ogy.  _  L.,fr.  Gk. '  AyXata,  lit.  ‘splendor,  beau¬ ty,  brightness’,  fr.  dyXaoi;,  ‘splendid,  beautiful, bright’,  which  is  of  uncertain  origin.  It  pos¬ sibly  stands  for  *d-yXxr 6?  and  is  formed  fr. copul.  pref.  a-  and  I.-E.  base  *gl-,  zero  degree  of base  *gel-,  ‘clear,  serene,  cheerful,  lovely;  to laugh’.  Copul.  pref.  a-  (in  *a-yXaF6<;)  stands for  I.-E.  *sip-,  a  weak  gradational  form  of  I.-E. base  *sem-,  ‘one,  together’;  see  same.  Fr.  base •gel-  derive  Gk.  yaXrjvik,  ‘calm,  serene’,  yaXr.vy, ‘stillness  of  wind  and  wave’,  ycXav,  ‘to  laugh', y£Xto?,  ‘laughter’;  see  geloto-  and  cp.  words there  referred  to.
Aglaspis,  n.,  a  genus  of  Cambian  Xiphosura (paleontol.)  —  ModL.,  lit.  ‘with  a  glittering shield’,  contracted  fr.  Gk.  dyXao ‘splendid, beautiful,  bright’,  and  iamq,  ‘shield’.  See
Aglaia  and  aspidium.
agleam,  adv.  and  adj.,  gleaming.  Formed  fr. a-,  ‘on’,  and  gleam.
aglet,  aiglet,  n.,  the  metal  tag  of  a  lace.  —  F. aiguillette,  dimin.  of  aiguille,  ‘needle’,  fr.  VL. * acucula ,  corresponding  to  L.  acicula,  dimin.  of ecus,  ‘needle’.  Cp.  It.  agucchia,  OProven?.,  Port. agulha,  Sp.  aguja,  needle’,  and  see  acus,  aiguil¬ le.  For  the  ending  see  suff.  -et agley,  adv.,  awry  ( chiefly  Scot.).  —  Formed  fr. a-  ‘on’,  and  Scot,  gley,  ‘to  squint’.
Aglossa,  n.  pi.,  a  suborder  of  amphibians  {zool.) —  ModL.,  fr.  Gk.  SyXueooc,  ‘tongueless’.  See next  word.
agjoagal,  adj.,  tongueless.  —  Formed  with  adj.
39
suff.  -al  fr.  Gk.  &y\caaaoq,  ‘without  a  tongue’, fr.  a-  (see  priv.  pref.  a-)  and  yXc oarsa.,  ‘tongue’. See  gloss,  ‘note’,  and  cp.  prec.  word, aglow,  adv.  and  adj.,  in  a  glow.  —  Formed  fr. a-,  ‘on’,  and  glow.
agmatine,  n.,  name  of  the  base  C5HMN4  (biochem.)
—  Coined  by  the  German  physiological  chemist Albrecht  Kossel  (1853-1927)  fr.  Gk.  otyp.ee,  gen. itypaxo:;,  ‘fragment’,  and  chem.  suff.  -ine.  Gk. dtypot  is  rel.  to  dyvupt  (for  *FayvCpi),  ‘I  break’, and  cogn.  with  Toch.  wak-,  ‘to  burst,  crack’,  in the  causative  form,  ‘to  cause  to  split,  to  dis¬ tinguish’  ,  wdkdm,  ‘peculiarity’.  See  Frisk,  GEW . , I,  p.  13  s.v.  ayvupi.
agmatology,  n.,  the  study  of  fractures  in  surgery.
—  Compounded  of  Gk.  fiypa,  gen.  dypxxo;, ‘fragment’,  and  -Xoyia,  fr.  -X6yo<;,  ‘one  who speaks  (in  a  certain  manner);  one  who  deals (with  a  certain  topic)’.  See  agmatine  and  -logy.
agminate,  agminated,  adj.,  grouped.  —  Formed with  adj.  suff.  -ate,  resp.  also  -ed,  fr.  L.  agmen, gen.  -minis,  ‘multitude  in  motion,  crowd,  army’, lit.  ‘that  which  moves’,  fr.  agere,  ‘to  set  in  mo¬ tion,  drive’;  cogn.  with  OI.  djmah,  ‘path’,  Gk. oyaoc,  ‘furrow;  path’.  See  agent,  adj.,  and  -men. agnail,  n.,  a  hangnail.  —  OE.  angnsegl,  ‘worn  on the  foot’,  compounded  of  ang-  (used  only  in compounds),  ‘narrow,  painful’,  and  nsegl,  ‘nail’. The  first  element  is  rel.  to  OE.  enge,  ‘narrow’; see  anger.  For  the  second  element  see  nail.  Cp. anbury.
agnate,  adj.,  sprung  from  the  same  male  ances¬ tor.  —  L.  agnates,  ‘related  by  the  father’s  side’, lit.  ‘bom  to’,  pp.  of  agnasci,  ‘to  be  bom  in  ad¬ dition  to’,  fr.  ad-  and  OL.  gndsci  (whence  L. nasci),  ‘to  be  bom’.  See  natal  and  cp.  cognate, innate.
Derivatives:  agnate,  n.,  agnat-ic,  adj. agnation,  n.,  an  agnate  relationship.  —  L.  ag- ndtio,  gen.  -onis,  fr.  agnatus.  See  prec.  word and  -ion.
agnathous,  adj.,  having  no  jaws.  —  Formed  fr. priv.  pref.  a-  and  Gk.  yvdfto?,  ‘jaw’.  See  gna¬ thic  and  -ous.
Agnes,  fem.  PN.  —  L.  Agnes,  fr.  Gk.  'Ayvr(,  lit. ‘pure,  chaste-,  fem.  of  ayvo;.  See  agnus  castus and  cp.  Inez.  The  most  frequent  ME.  forms  of the  name  Agnes  were  Annis,  Annys.  Cp.  Nancy. Agni,  n.,  one  of  the  chief  gods  of  the  Vedas.  — OI.  Agnih,  ‘the  god  of  fire’,  fr.  agnih,  ‘fire’,  which is  cogn.  with  L.  ignis,  ‘fire’.  See  igneous, agnize,  tr.  v.,  to  recognize  (archaic).  —  Formed fr.  L.  agnoscere  on  analogy  of  recognize  (fr.  L. recognoscere).
agnoiology,  n.,  the  doctiine  of  ignorance  ( philos .) —  Coined  by  J.-F.  Ferrier  in  1 854  fr.  Gk.  dyvoia, ‘ignorance’,  and  -Xoyia,  fr.  -Xoyor,  ‘one  who speaks  (in  a  certain  manner);  one  who  deals (with  a  certain  topic)’.  Gk.  dyvoia  is  formed fr.  a-  (see  priv.  pref.  a-)  and  the  stem  of  yiyvco- toeiv,  ‘to  know’;  see  gnostic  and  cp.  agnostic. For  the  second  element  see  -logy.
=== leaf 33 ===
e,  n„  hook,  clasp.  —  F.  agrafe,  back  forma¬ tion  fr.  agrafer,  ‘to  hook,  fasten’,  fr.  d,  to (see  a),  and  OF.  grafer,  ‘to  fasten  with  a  hook’, fr.  grafe,  ‘hook’,  fr.  OHG.  krapfo,  ‘hook*. See  grape.
agraphia,  n.,  inability  to  write;  a  form  of  aphasia (med.)  —  Medical  L.,  formed  fr.  priv.  pref.  a-
and  -graphia.
agrarian,  adj.,  1)  of  the  land;  2)  of  agriculture.  - Formed  with  suff.  -an  fr.  L.  agrarius,  ‘pertaining to  land’,  fr.  ager,  gen.  agri,  ‘field,  land’,  which is  rel.  to  Umbr.  ager  and  cogn.  with  Gk.  xypo;, ‘field’,  Goth,  akrs,  OE.  tecer,  ‘field’.  See  acre and  agent  and  cp.  agriculture.  Cp.  also  acorn, agrestic,  agrio-,  agro-,  Agrostis  and  the  second element  in  onager.
Derivative:  agrarian,  n.
agree,  intr.  v.  —  ME.  agreen,  fr.  OF.  agreer  (F. agreer ),  ‘to  receive  with  favor’,  fr.  a  (F.  a),  ‘to’ (see  a),  and  gre  (F.  gre),  ‘will,  pleasure’,  fr.  L. gratum,  neut.  of  the  adjective  grams,  ‘acceptable, pleasing,  agreeable,  grateful’,  used  as  a  noun.  See grateful  and  cp.  the  second  element  in  maugre. Derivatives:  agreeable  (q.v.),  agre-ed,  adj.,  agre¬ ed- tv,  adv.,  agree-ing,  adj.,  agree-ing-ly,  adv., agreement  (q.v.)
agreeable,  adj.  —  ME.  agreable,  fr.  OF.  agreable (F.  agreable).  See  agree  and  -able.
Derivatives:  agreeabil-ity,  n,,  agreeable-ness ,  n., agreeabl-y,  adv.
agreement,  n.  —  OF.  agrement  (F.  agrement ),  fr.
agreer.  See  agree  and  -ment. agrestic,  adj.,  rustic,  rural.  —  L.  agrestis,  ‘per¬ taining  to  the  fields’,  fr.  ager,  ‘field’;  see  agrar-
40
ian.  Agrestis  has  been  dissimilated  fr.  *agrestris. (Cp.  campestris,  ‘relating  to  the  field’,  fr.  cam¬ pus,  ‘field’,  and  terrestris,  ‘earthly’,  fr.  terra, ‘earth’.)
agricolite,  n.,  silicate  of  bismuth  (mineral.)  — Named  after  the  German  mineralogist  Georg Agricola  (1494-1555)-  For  the  ending  see  subst. suff.  -ite.
agriculturalist,  n.,  a  farmer.  —  Formed  fr.  L. agricultiira  (see  agriculture)  with  the  suffixes  -al and  -ist.  Cp.  agriculturist, agriculture,  n.  —  F.,  fr.  E.  agricultiira,  lit.  culti¬ vation  of  the  land’,  compounded  of  ager,  gen. agri,  ‘field,  land’,  and  cultiira,  ‘cultivation’.  See agrarian  and  culture.
Derivatives:  agricultur-al,  adj.,  agriculturalist, agriculturist  (qq.v.)
agriculturist,  n.,  an  agriculturalist  (rare). Formed  with  suff.  -ist  fr.  L.  agricultiira.  See prec.  word.
Agrimonia,  n.,  a  genus  of  herbs  (bat.)  —  ModL. See  next  word.
agrimony,  n.  —  L.  agrimonia,  fr.  Gk.  apyspxovr],
‘a  kind  of  poppy’,  which  is  prob.  borrowed  fr. Heb.  argamin,  ‘purple’ ;  influenced  in  form  by L.  ager,  gen.  agri,  ‘field’.  See  Argemone. agrimotor,  n.,  a  machine  used  in  agriculture. Compounded  of  L.  ager,  gen.  agri,  ‘field’  (see agrarian),  and  E.  motor.
agrio-,  combining  form  meaning  ‘wild’.  —  Gk. aypio-,  fr.  itypioq,  ‘wild’,  lit.  meaning  ‘living  in the  fields',  fr.  dyp 6q,  ‘field’,  which  is  cogn.  with L.  ager,  ‘field’.  See  agrarian, agriology,  n.  the  study  of  prehistoric  human  cus¬ toms.  —  Compounded  of  agrio-  and  Gk.  -Xoyla, fr.  -Xoy o',  ‘one  who  speaks  (in  a  certain  man¬ ner);  one  who  deals  (with  a  certain  topic)  . See  -logy.
agrito,  n.,  name  of  the  plant  called  scientifically Mahonia  trifoliata.  —  Sp.,  fr.  agrio,  ‘sour  ,  fr. VL.  acrus,  fr.  L.  acer,  ‘sharp’,  in  VL.  also  ‘sour’. Cp.  F.  aigre,  ‘sour’,  which  also  derives  fr.  VL. acrus,  and  see  acrid.  Cp.  also  eager  and  the second  element  in  vinegar, agro-,  combining  form  meaning  ‘pertaining  to agriculture'.  —  Gk.  xypo-,  fr.  xyp'X;,  ’field’, which  is  cogn.  with  L.  ager,  ‘field  .  See  agrarian, agronomy,  n.,  the  science  of  crop  production, management  of  land.  —  F.  agronomie,  fr.  Gk. aypoviptos,  ‘rural’,  which  is  compounded  of iypo;,  ‘field’  and  the  stem  of  vepeiv,  ‘to  as¬ sign,  manage',  ‘to  drive  (cattle)  to  pasture  .  See agrarian  and  Nemesis.
Derivatives:  agronom-ic,  agronom-ic-al,  adjs., agronom-ics,  n.,  agronom-ist,  n.
Agropyron,  n.,  a  genus  of  perennial  grasses  ( bot .) —  ModL.,  lit.  ‘field  wheat’,  fr.  Gk.  aypo?, ‘field’,  and  nvpoq,  ‘corn,  wheat .  The  first  ele¬ ment  is  cogn.  with  L.  ager,  ‘field’;  see  agrarian. For  the  second  element  see  pyrene  and  cp.  words there  referred  to.
Agrostemma,  n.,  a  genus  of  plants  of  the  pink
41
family;  the  corn  cockle  (bot.)  —  ModL.  lit. ‘crown  of  the  field’,  fr.  Gk.  aypo;,  ‘field’,  and oTsu.ua,  ‘wreath’.  See  agro-  and  stemma. Agrostis,  n.,  a  genus  of  grasses,  the  bent  grass (bot.)  —  L.  agrostis,  ‘couch  grass’,  fr.  Gk. Syptocmq,  fr.  aypo?,  ‘field’.  See  agro-. agrostology,  n.,  that  branch  of  botany  which  deals with  grasses.  —  Compounded  of  Gk.  Syptoaxu;, ‘grass’,  and  -Xoyta,  fr.  -Xoyoi;,  ‘one  who  speaks (in  a  certain  manner);  one  who  deals  (with  a certain  topic)’.  See  Agrostis  and  -logy, aground,  adv.  ( naut .)  —  Formed  fr.  a-,  ‘on’,  and ground.
agrypnia,  n.,  sleeplessness  (med.)  —  Medical  L., fr.  Gk.  aypurtvia,  sleeplessness,  wakefulness’, fr.  otypuiwoi;,  ‘wakeful’,  which  is  compounded of  dyp6;,  ‘field’,  and  fymoq,  ‘sleep’;  the  orig. meaning  of  ayporcvoi;  was  ‘sleeping  in  the  field’. See  agro-  and  hypno-.
aguardiente,  n.,  spirituous  liquor.  —  Sp.,  lit. ‘burning  water’,  compounded  of  agua,  ‘water’ fr.  L.  aqua,  and  ardiente,  fr.  L.  ardentem,  acc.  of ardens,  pres.  part,  of  ardere,  ‘to  burn’.  See  aqua¬ tic  and  ardent.
ague,  n.,  malarial  fever.  —  OF.  ague,  ‘an  acute fever’,  prop.  fem.  of  the  adjective  agu  (F.  aigu), ‘sharp,  acute  (scil.  fever)’,  fr.  L.  ( febris )  acuta, ‘an  acute  fever’,  fem.  of  acutus,  ‘sharp,  acute’. See  acute.
Derivatives:  agu-ish,  adj.,  agu-ish-ly,  adv.,  agu- ish-ness,  n.,  ague-like,  adj. agunah,  n.,  a  woman  prevented  from  remarrying because  she  has  no  proof  of  her  husband’s  death (Jewish  religion).  —  Heb.  'aghiindh,  lit. ‘restrained (from  marrying)’,  passive  fem.  part,  of  ‘aghan, ‘he  restrained,  shut  up’,  which  is  rel.  to  Arab. 'S' jama,  IV  (=  causative)  form  of  stem  ‘-j-m,  ‘to shut  up’.
=== leaf 34 ===
 Com¬ pounded  of  Gk.  a’iXoupog,  "cat’,  and  -91X05, ‘loving’.  For  the  first  element  see  Ailurus,  for  the second  see  -phile.
ailurophobia,  n.,  morbid  fear  of  cats.  Com¬ pounded  of  Gk.  alXoupog,  ‘cat’,  and  -q>o(Jia, ‘fear  of’,  fr.  96(30 5,  ‘fear’.  See  prec.  word  and
-phobia.
Ailurus,  n.,  the  genus  consisting  of  the  panda ( zool .)  —  ModL.,  fr.  Gk.  atXoupoc,  ‘cat’,  which is  of  uncertain  origin;  its  derivation  fr.  Gk. aloXop,  ‘quick  moving,  rapid’,  and  oupd,  ‘tail’, is  folk  etymology.  Cp.  aeluro-. aim,  intr.  and  tr.  v.  —  ME.  aimen,  eimen,  fr.  OF. aesmer,  which  is  formed  fr.  a,  ‘to’  (see  a),  and esmer,  fr.  L.  aestimdre,  ‘to  estimate’.  See  esteem. Derivatives:  aim,  n.,  aim-less,  adj.,  aim-less- ly,  adv.
air,  n.,  atmosphere.  —  ME.  aire,  fr.  OF.  (—  F.) air,  fr.  L.  aer  (whence  also  Rum.  aer,  OProveng., Catal.,  Sp.  aire.  Port,  air,  ‘air’),  which  derives fr.  Gk.  df)p,  gen.  l)tpoQ,  Att.  gen.  aepop,  ‘air’ (from  the  Att.  acc.  a£pa  is  borrowed  It.  aria, ‘air’).  Gk.  dr,p  (cp.  the  parallel  forms  Aeol. otuTjp,  Dor.  dfWjp)  and  the  rel.  aopx,  ‘air  in motion,  breeze’,  are  of  uncertain  origin.  They are  possibly  rel.  to  deipciv,  ‘to  lift  up,  raise’, and  lit.  mean  ‘that  which  rises’.  See  aorta,  and cp.  aerate,  aerial,  aero-,  the  first  element  in aerostat,  and  the  second  element  in  malaria. Derivatives:  air,  v.,  air-able,  adj.,  air-er,  n.,  air¬ ing,  n.,  air-less,  adj.,  air-y,  adj.,  air-i-ly,  adv., air-i-ness ,  n.
air,  n.,  melody,  tune.  —  F.,  fr.  It.  aria,  of  s.m., fr.  L.  aerea,  fern,  of  the  adjective  aereus,  ‘per¬ taining  to  the  air’,  fr.  aer,  ‘air’.  See  prec.  word
and  cp.  aria.
airplane,  n.  —  Compounded  of  air  and  plane. See  aeroplane.
aisle,  n.  —  ME.  He,  ele,  fr.  OF.  ele  (F.  aile), ‘wine’,  fr.  L.  ala.  of  s.m.,  which  stands  for  *ag-
42
s-la  and  is  rel.  to  axilla,  ‘armpit’,  and  cogn.  with OI.  dksah,  ‘collarbone’,  Avestic  ashayA  (dual gen.),  ‘of  both  shoulders’.  Arm.  anut‘  (for  *as- nut'),  ‘armhole’,  OHG.  ahsala,  MHG.  ahsel,
G.  Achsel,  ON.  oxl,  OS.  ahsla,  OE.  eaxl, ‘shoulder’.  All  these  words  are  formed  fr.  I.-E. base  *ag-,  ‘to  move,  drive’,  with  reference  to the  arms  moved  from  the  shoulders.  See  agent, adj.,  and  cp.  aileron,  ailette,  alar,  alate,  aliform, aliped,  alula,  axil,  axilla,  axillary,  axle,  oxter, and  the  second  element  in  bezel.
Derivative:  aisl-ed,  adj.
aitch,  also  ache,  n.,  name  of  the  letter  h  in  Eng¬ lish.  —  ME.  ache,  fr.  OF.  (=  F.)  ache,  which is  of  uncertain  origin.  It  possibly  derives— to¬ gether  with  It.  acca  and  Port,  aga,  of  s.m. — from  a  form  *hakka,  which  would  stand  for orig.  ha-ka  (for  h-k,  i.e.  h  and  k  (as  the  con¬ sonant  following  h  in  the  alphabet).  The  deriva¬ tion  of  the  French  name  of  the  letter  h  fr.  F. hache,  ‘ax’  (in  allusion  to  the  form  of  the  small h  which  resembles  an  ax)  is  contradicted  by  the fact  that  whereas  the  letter  h  is  called  acca  in  It. and  agd  in  Port.,  the  It.,  resp.  Port,  name  for the  ax  is  accia,  resp.  facha. aitchbone,  n. — Fr,  ME.  a  nache  bone ,  fr .  OE.  nache, pl„  ‘rump’,  fr.  VL.  *natica,  fr.  L.  natis,  which  is cogn.  with  Gk.  vtaxop,  v(6xov,  back  ;  see  nates. The  loss  of  the  initial  n  is  due  to  a  misdivision of  a  nache  bone  into  an  ache  bone.  Cp.  adder, apron,  auger,  ekename,  ouch,  umble  pie,  umpire. ajar,  adv.,  on  the  turn,  slightly  opened.  —  ME. on  char ,  ‘on  the  turn  ,  fr.  a-,  on  ,  and  ME. chearr,  char,  ‘a  turn’,  fr.  OE.  cierr,  cyrr.  See char,  ‘a  turn  of  work’,  and  cp.  words  there referred  to.
ajar,  adv.,  out  of  harmony.  —  Compounded  of a-  ‘on’  and  jar,  ‘creak’.
Ajax,  n.,  in  the  Iliad,  the  name  of  two  Greek heroes  of  the  Trojan  war:  Ajax  the  Greater,  son of  Telamon,  and  Ajax  the  Less,  son  of  Oileus.— L.  Ajax,  fr.  Gk.  Ata?.  The  name  A  tap  prob. denoted  orig.  an  earth  god  and  derives  fr.  Gk. ala,  ‘earth’.  See  Kretschmer  in  Glotta  15.1927, and  Frisk,  GEW.  I,  p.  30. ajonjoli,  n.,  sesame.  —  Sp.  ajonjoli  fr.  Arab,  al- juljuldn,  lit.  ‘the  sesam’,  altered  in  Spain  into  al- juljultn  (cp.  the  Sp.  variant  aljonjoli).
Ajuga,  n.,  a  genus  of  plants  of  the  mint  family; the  bugle  weed  ( bot .)  —  A  ModL.,  hybrid coined  fr.  Gk.  privative  pref.  a-  and  L.  jugum, ‘joke’  (see  jugular  and  yoke);  so  called  from  the seeming  absence  of  the  upper  lip  of  the  corolla, akasa.  n„  the  name  of  space  in  Sankhya  philo¬ sophy.  —  OI.  akasa-,  ‘space’,  formed  fr.  em¬ phatic  pref.  a  and  kdsate,  ‘appears,  shines  ,  prob. from  I.-E.  base  *quek~,  *qv'eg-,  whence  also Avestic  ( ashman ,  ‘eye’,  akasat,  ‘he  beheld  ,Gk. x£xpcop,  later  form  x6xpap  (prob,  for  *qwek- mor),  ‘sign,  token’,  OSlav.  kazq,  kazati,  ‘to show’.  Cp.  ukase.
akerite,  n.,  a  quartz  syenite  ( petrogr.)  —  Named
43
after  Aker  in  Sweden.  For  the  ending  see  subst. suff.  -ite.
akimbo,  adv.  and  adj.  —  ME.  in  kenebowe,  prob. of  Scand.  origin.  Cp.  Icel.  kengboginn,  ‘bent  into a  curve’,  and  see  kink  and  bow,  ‘a  weapon’, akin,  adj.  —  Formed  fr.  a-,  ‘of’,  and  kin. akinesia,  n.,  absence  of  motion  in  a  muscle  (med.)
—  Medical  Latin,  fr.  priv.  pref.  a-  and  Gk.  xt- vtjok;,  ‘motion’,  fr.  xiveiv,  ‘to  move’.  See  ki¬ nesis  and  -ia.
Akkadian,  also  Accadian,  adj.  and  n.  —  Formed with  suff.  -ian  fr.  Heb.  Akkad  (Gen.  10:10), name  of  a  district  and  city  in  Babylonia, al-,  assimilated  form  of  ad-  before  /.
-al,  suff.  forming  adjectives,  as  in  royal,  or  sub¬ stantives  of  adjectival  origin,  as  in  rival.  — Either  fr.  F.  -al,  -el,  or  directly  fr.  L.  adj.  suff. -alis.  In  many  cases  the  suff.  -alls  was  used  al¬ ready  in  Latin  both  adjectivally  and  substanti¬ ally  (cp.  L.  rival  is,  ‘pertaining  to  a  brook ;  one who  uses  the  same  brook;  neighbor;  competi¬ tor,  rival’,  and  see  rival).  Cp.  the  suffixes  -ial and  -ar.
-al,  suff.  forming  verbal  nouns,  as  arrival,  avow¬ al.  —  L.  -alia,  neut.  pi.  of  -alis,  but  in  Vulgar Latin  mistaken  for  the  fern.  sing.  suff. ;  formed either  directly  from  Latin  or  through  the  medi¬ um  of  OF.,  F.  -aille  (as  in  OF.  arrivaille,  etc.), -al,  chem.  suff.  denoting  aldehyde  as  in  bromu/, chloral.  —  F.,  from  the  first  syllable  of  aldehyde, ala,  n.,  a  wing  or  anything  similar  to  a  wing  (anat .)
—  L.  See  aisle  and  cp.  alar.
a  la,  short  for  a  la  mode,  ‘in  the  fashion  or  style of’,  as  a  la  frangaise,  ‘in  the  French  fashion  or style’.  —  See  si  and  ille.
alabamine,  n.,  name  of  a  chemical  element  dis¬ covered  in  1931  by  the  American  chemist  Fred Allison  (1882-  )  and  his  collaborators  and named  by  them  after  the  Alabama  Polytechnic Institute;  now  called  astatine.  For  the  ending see  chem.  suff.  -ine.
alabandite,  n.,  manganese  sulfide  (mineral.)  — Named  after  Alabanda  in  Asia  Minor.  For  the ending  see  subst.  suff.  -ite. alabarch,  n„  title  of  the  chief  official  of  the  Jews of  Alexandria  during  the  Grecian  period.  — Gk.  aXapipyj)?,  which  lit.  means  ‘ink  ruler’, and  origin,  denoted  an  official  in  charge  of the  ‘written’  notes  or  records.  —  Gk.  aXa- flap/rji;,  is  compounded  of  aXafia,  ‘ink’  (He- sychius),  and  ap/og,  ‘leader,  chief,  ruler’  (see -arch).  The  parallel  form  apaPapx^Q  is  second¬ ary  and  due  to  assimilation  —  Most  diction¬ aries  either  do  not  deal  with  the  etymology  of the  word  alabarch  at  all,  or  content  themselves with  the  stereotypic  remark :  ‘origin  unknown’. — In  the  Addenda  et  Corrigenda  to  Liddell  and Scott’s  Greek-English  Lexicon,  new  (ninth)  ed. (reprinted  1951),  P-  2053a  s.v.  ’  Apa[3apx7)?,  the word  ’AXapapxr]?  is  explained  as  dissimilated fr.  ’Apa(3apxr)?,  ‘ruler  of  the  Arabs,  emir’.  — The  fart  is,  however,  that  we  must  distinguish
between  ’  Acr's-ixy  ry  in  the  sense  of  ‘Ruler  of the  Arabs’,  and  £pa(3apx?]?,  the  assimilated form  of  <xXaPapx?]S,  title  of  the  chief  magistrate of  the  Jewish  population  in  Alexandria,  a  name which  has  nothing  to  do  with  the  Arabs, alabaster,  n.,  a  translucent  whitish  kind  of  gyp¬ sum.  —  OF.  alabastre  (whence  F.  albatre),  fr.
```


## [2026-09-06T22:06:51.661Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for P in 1436 725 905; do L=$((P+24)); echo \"=== SYN p.$P (leaf $L) ===\"; awk -v n=$L 'BEGIN{RS=\"\\f\"} NR==n+1' SYN.txt | head -35; done",
 "description": "Buck pages 725, 905, 1436"
}
```


### [2026-09-06T22:06:53.295Z] TOOL RESULT

```
=== SYN p.1436 (leaf 1460) ===
sts (renders gps and ayov) : ON heipt ‘feud, bane, hate’, OF hest ‘violence, fury’, hést adj.. OHG heist ‘violent, vehement’, etc., perh. : Skt. cibham ‘quickly’. Walde-P. 1.364. Feist 231.
Goth. sakjé (renders naxn, but in sense of-‘strife’), OF sacu, ME sake, OHG sah- ha, sechia (several of these also ‘lawsuit’ 21.13 and ‘thing’ 9.90), with vbs. Goth. sacan ‘quarrel, rebuke’, OE sacan ‘quar- rel, contend’, OHG sachan ‘quarrel, re- buke, litigate’, these prob. : Goth. sokjan ‘seek’ (cf. mip-sdkjan ‘strive with some- one’), OE sécan ‘seek, attack’, OHG suohhan ‘seek’, etc. (11.31). Walde-P. 2.449. Weigand-H. 2.633. Feist 407.
_Goth. Pwairhei, renders gps 2 Cor. 12.20, otherwise @upés, dpy7n ‘anger’ (see 16.46).
ON sirzd (but earlier mostly ‘woe, grief’, later mostly of armed strife, ‘war’), Dan., Sw. strid, Du. strijd, OS sérid, OHG, MHG sirtt, NHG streit (OHG > OF r. esirif > ME sirif, NE strife; REW 8316, NED s.v.), ef. ON sértdr ‘stiff, stubborn, severe’, OHG ein-stritz ‘stub- born’, with vbs. ON sirtda ‘torment, punish, fight’, OHG séritan ‘quarrel, strive’ (OE stridan ‘stride’), perh. fr. an extension of the root in Grk. ozepeés ‘stiff, firm’, ON starr ‘stiff, hard’, etc. Walde-P. 2.633. Falk-Torp 1180.
ON deila, fr. vb. dela ‘deal, divide’, fig. ‘divide on a point, quarrel’ = Goth. dailjan, etc. ‘divide’, beside Goth. dazls ‘part’ etc. (18.23). Falk-Torp 139.
ON Preta, Dan. trette, Sw. trdta, also vb. ON pret(t)a, etc., perh. : ON pryng- va, OE pringan, etc. ‘press, crowd’. Walde-P. 1.759. Falk-Torp 1294.
Sw. gral, vb. grdala, prob. of imitative origin. Hellquist 306.
1362
OF geflit, ME flit, OHG fiz (also ‘zeal, industry’, NHG fleiss), OS flit ‘fight, zeal in combat’, with vbs. OE flttan ‘quarrel, strive’, OHG flizan ‘be zealous’, etc., etym. dub., perh. fr. the root seen in Lett. plities ‘press, obtrude, demand’. Petersson, PBB 38.316. Walde-P. 2.684 (adversely).
OE céas, later céast (with additional suffix), ME chest, fr. Lat. causa ‘lawsuit’. Holthausen 45. NED s.v. chest, sb.?.
ME sirif, NE strife, see above under ON strid.
NE quarrel (ME ‘complaint, ground of complaint’, etc.), fr. OFr. querelle (above, 2). NED s.v.
Du. twist (MLG twist > Dan., Sw. ivist), late MHG, NHG zwist, lit. ‘divi- sion, split’ (cf. ON wistra ‘divide, scat- ter’), from Gme. *twis- ‘apart’ (cf. Goth. twis-standan ‘separate’), orig. ‘in two’ : Goth. twat ‘two’, etc. Walde-P. 1.820. Falk-Torp 1305 f. Weigand-H, 2.1357 f.
MHG, NHG hader : OHG hadu-, OE heada-, Ir. cath, ete. ‘battle’ (20.12). Weigand-H. 1.788.
NHG zank, fr. vb. zanken, late MHG zanken
=== SYN p.725 (leaf 749) ===
OHG stincan ‘smell’ (15.21). Walde-P. 2.617. Falk-Torp 1168.
Dan. hoppe, Sw. hoppa (ON hoppa ‘hop’) = OE hoppian, NE hop, ete. :
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Goth. hups, OF hype, OHG huf ‘hip’ Lat. cubitum ‘elbow’, Grk. xbBos ‘hollow above the hips of cattle’, ete. Walde-P. 2.374. Falk-Torp 418.
Dan. springe (ON springa ‘burst’, rare and poet. ‘leap’, Sw. springa ‘run’), OE springan (also ‘burst forth, spurt’), ME springe, NE spring, Du. springen, OHG springan, MHG, NHG springen, fr. IE *sprengh- : *spergh- in Skt. sprh- ‘be jealous of, emulate’, Grk. oreépxopat ‘move rapidly, be in haste’. Walde-P. 2.675. Falk-Torp 1133.
NE jump, of imitative orig., like bump. Cf. also NHG dial. gumpen ‘jump, hop’, etc. NED s.v.
6. Lith. Sokti : Grk. xnxtw ‘gush, bub- ble forth’, Lith. Sankinti ‘cause (a horse) to mount’, OHG hengist ‘stallion’, etc. Walde-P. 1.334. Otherwise (: ChSI. skociti, etc. below) Briickner 494.
Lett. lékt : Lith. lékti ‘fly’ (10.37).
7. ChSl. skociti, iter. skakati, etc., general Slavic, beside skokw ‘a leap’ : Br. diskogella ‘shake’, W. ysgogi ‘move, stir’ (10.11), also OF scacan ‘shake’, etc. IE *skek-, *skeg- Walde-P. 2.556 f.
Russ. prygnut', prygat’, perh. fr. a guttural extension of IE *preu- in Skt. pru- (below). Walde-P. 2.88. Other- wise Miklosich 266 (: ChSI. prega, prestt ‘span, stretch’), Brickner 436 (with other connections).
8. Skt. skand- : Lat. scandere ‘climb, mount’, MIr. scendim ‘spring, burst out, Grk. oxdvédadov ‘trap, snare’, etc. Walde- P. 2.540. Ernout-M. 902.
Skt. pru- : ON frar ‘swift, light-foot- ed’, etc. Walde-P. 2.87 f.
Igitized by Arya Samaj Foundation Chennai and eGangotri
N; LOCOMOT ION, TRANSPORTATION, NAVIGATION 689
10.44 DANCE (vb.) te Goth. plinsjan Lith.  Sokti 3 spxtouats xoP ON hoppa, dansa Lett. dancuot (diet) Gr opel Dan. ave ChSI. plesati gallaré Sw. sa SCr. _ plesati, igrati »  pallare, danzar? OE _ sealtian Boh. tancovati : danser Pear ME daunse Pol. taricowaé pailar, ey NE dance Russ. tancovat’, pljasat’ Rus dansa, J Du. ite Skt. nrt- ‘ ae, OHG - salzon Av. 4 WE rinncin MHG tanzen f Ce NHG  tanzen
several of the verbs for,‘dance’ are connected with words for jump, leap’, or other notions of quick motion; one
lization of ‘enclosure’ to
ts on a specia Hate for dancing’. Interchange be-
tween ‘dance’ and ‘play’ is seen in Slavie and by semantic borrowing in Rumani- an. Most conspicuous is the extent of loanwords—the Gothic word from Slav- ic, the OE and OHG from Latin, late Iatin from a Greek word, the French from a Gme. word, and especially the spre
=== SYN p.905 (leaf 929) ===
, tip’. Walde-P. 1.606. Berne- ker 354.
Boh. pic, dim. spitka, fr. NHG spiize.
Pol. koniec, Russ. konec ‘end’ (12.35), also ‘point’ or more specifically with ostry, ostryj ‘sharp’.
7. Skt. agra- (also ‘top, front, begin- ning’) : Av. ayra- ‘first, earliest’, Lett. agrs ‘early’, root connection? Walde-P. 1.38 f.
12.353 EDGE (Of a Knife, Sword, etc.; of a Table, Forest, etc.) Grk.  dxuiys xpaoredov, Goth. ....; (skaut) Lith. a&mens; kra3tas, xethos ON egg; rond briauna
NG aBlipas, xbym; xelde Dan. ag; kant, rand Lett. asmens; mala
Tat, aciés; dra, margo Sw. egg; kant, rand ChSl. _ ostrije; krajt
It filo, taglio; orlo, mar- OE ecg; rand, ora (sn@d) (viiskrilije)
7 gine ME egge SCr. _ oStrac; brid, ivica
» fil, tranchant; bord NE __ edge Boh.  ostit; hrana, (0)kraj
Sp. filo; canto, orilla, bor- Du. __ scherp; kant, rand Pol. —ostrze; brzeg, krawedz
Ria Sa : OHG  ekka (sarfi); (trado) Russ. ostrie; kraj
it poeta a MHG scher(p)fe, snide, ecke Skt. a¢ri-, dhara-; pranta- ae se ritach, NHG | schneide, schdrfe; Av. dara-; karana-
Nir » ochar, bil kante, rand
. Saobhar, béal; bruach, ¥ Ciumhais, eochair By, mh aweh; ymyll, ochr
remm, lemm, neu- a barvenn; ribl,
Words f ete, are or the ‘edge’ of a knife, sword,
wv Ate my tives fop read Hanected with adjec-
Ue group tp’ or verbs for ‘cut’. In (3) . ued (throug Words for ‘thread’ are
Some ‘ront) wns, {0 ‘mouth’ : Or ‘in? u (through
But for the ts also used for ‘edge’.
on Secondary sense
which developed in ME egge, NE edge, as in edge of the table, forest, ete. (NED s.v. III), other languages have quite dif- ferent words and sometimes in great variety according to the subject referred to. A few words are included in the list (but in parentheses) which are quotable only for the ‘edge, fringe’ of a garment,
CC-O. In Public Domain. Gurukul Kangri Collection, Haridwar
eee
Digitized by Arya Samaj Foundation Chennai and eGangotri a
a i
860 SELECTED INDO-EUROPEAN SYNONYMS
this being the only occurring sense of Grk. xpdéomedov in the NT.
1. Derivs. of IE *ak- in words for ‘sharp’ (15.78). Walde-P. 1.28 ff. Er- nout-M. 7 ff. Falk-Torp 182. Pedersen 1.123, 412.
Grk. axu7, Lat. aciés; ON egg, Dan. @g, OF ecg, ME egge, NE edge, OHG ekka (‘edge’ of a sword in Notker; also ‘point’), MHG ecke (‘edge, point, cor- ner’; NHG ‘corner’); Lith. asmens, Lett. asmens; ChSI. osirije, SCr. ostrac, Boh. ost7t, Pol. osirze, Russ. ostrie; Skt. acri-; here also Ir. ochar, NIr. eochair, W. ochr ‘edge, side’, W. hogi ‘sharpen, whet’; and prob. W. awch ‘edge, sharp- ness’ b
```


## [2026-09-06T22:07:06.220Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"10\\.76 WHEEL\\|4\\.21 EYE\\|EYE$\" SYN.txt | head; echo \"---leafs---\"; python3 - <<'EOF'\nimport re\nt=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt',encoding='utf8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if '10.76' in p and 'WHEEL' in p.upper():\n        print('leaf',i,'10.76 WHEEL')\n    if re.search(r'4\\.21\\s+EYE',p):\n        print('leaf',i,'4.21 EYE')\nEOF",
 "description": "Locate Buck wheel/eye sections"
}
```


### [2026-09-06T22:07:07.973Z] TOOL RESULT

```
5875:parts OF 4.21 EYE 5 Goth. augo er akis gpaadues, HHO ON  auga ett. acs Grk. oe Dan. #e ChSl. oko NG ulus S 6ga SCr. oko t. oc . WwW. 4 Lav echo OE éage Boh. oko Tr oeil ME — eze (eghe, eye) Pol. oko S eafo NE eye Russ. glaz ih ochiu Du. 00g Skt.  akgi, cakgus-, locana-, ; suil, rose OHG ouga netra- Nir. sil F MHG ouge Ay.  éaSman-, déiéra-, aki Ilyga G eC He lagad il ie , ae ‘fost of the words for ‘eye’ belong to sol, etc. ‘sun’ (1.52). Walde-P. 2.446. a ited group. The others are from | Pedersen 1.62. Stokes 692. an inher! Ir. rosc, fr. *pro-sc-, deriv. of sech-
16624:M wb.) 10.54 OverTAKE oll pen Gb.) 10.55 Arrive, REACH 10.12 ae AROUND 10.56 APPRoAcH (vb.) 40.18 Wino, WRAP (vb.) 10.57 ENTER 10.14 Ron (7b.) 10.61 Carry (BEaR) 10,15 rairb.) 10.62 Brine re Russe, LIFT 10.63 SEND 10. vb.) 10.64 Leap (vb.) Ce se Tigui 10.65 D 1024 Dror (sb., of Liquid) : RIVE (vb. trans.) 1025 THROW (vb.) 10.66 Rive (vb.) 1098 SHAKE (vb. trans.) 10.67 Pusu, Sov (vb.) 1031 Bor (vb. intr.) 10.71 Roan 10.33 Smvx (vb.) 10.73 Street 10.34 Fuoat (vb.) 10.74 Brmwce 10.35 Sw (vb.) 10.75 Carrtace, Wacon, Cart 1036 Satz (vb.) 10.76 WHEEL 1037 Fuy (vb.) 10.77 AXLE 10.38 Brow (vb. intr.) 10.78 Yoxs 1041 Creer, CRAWL 10.81 Sup 1042 Ste, Sur (vb.) 10.82 Sartor 1043 Jump, Leap (vb.) 1044 Dancz (vb.) ee meee 1045 Watx (vb.) i 10.46 Run (vb.) 10.85 Oar 1047 Go 10.852 Row (vb.) 1048 Come 10.86 RuppER 1049 Go Away, Depart 10.87 Masr a Tze 10.88 Sar (sb.) 10.53 peso 10.89 AncHoR
18315:10.76 WHEEL Grk. —_zpoxés (xbxdos) Goth. .... Lith. ratas, tekinis ‘ NG —zpoxés, pda ON —hwel, hjal, hvel Lett. rats, ritenis, skritulis Lat. rota Dan. jul ChSl. kolo It. —ruota Sw.  hjul SCr. kolo, totak, kotat Fr. roue OE hwéol Boh. kolo Sp. rueda ME _hwele, whele Pol. kolo Rum.  roaté NE wheel Russ. koleso Ir. droch, roth Du. wiel Skt. cakra- NIr. roth OHG rad Av. éazra- W. olwyn, rhod MHG rat Br. rod NHG rad
---leafs---
leaf 261 4.21 EYE
leaf 719 10.76 WHEEL
leaf 787 10.76 WHEEL
leaf 977 10.76 WHEEL
leaf 978 10.76 WHEEL
leaf 1466 10.76 WHEEL
```


## [2026-09-06T22:07:18.441Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('SYN.txt',encoding='utf8',errors='replace').read()\npages=t.split('\\f')\nprint(len(pages))\nfor target in ['1436','725','905','724']:\n    hits=[i for i,p in enumerate(pages) if re.search(r'(?m)^\\s*'+target+r'\\b',p[:400]) or re.search(target+r'\\s+SELECTED|SYNONYMS\\s+'+target,p)]\n    print(target,hits[:8])\nEOF\necho \"=== leaf 787 ===\"; awk 'BEGIN{RS=\"\\f\"} NR==788' SYN.txt | head -25",
 "description": "Locate Buck printed pages"
}
```


### [2026-09-06T22:07:20.340Z] TOOL RESULT

```
1545
1436 []
725 []
905 []
724 []
=== leaf 787 ===
act of carrying’ and ‘thing carried, burden’, fr. ONorthFr. cariage, deriv. of carier ‘car- ty’, this again deriv. of Lat. carrus (above, 3). Used for ‘wheeled vehicle’ since 16th. cent., now esp. one for carry- ing persons. NED s.v.
6. Lith. vezimas, above, 1.
Lith. ratai, Lett. radi, lit. ‘wheels’, pl. of ratas, rats ‘wheel’ (10.76). Cf. ChSI.
kola (below, 7) and Toch. A kukal, B kokale ‘wagon’ : Skt. cakra-, Gri. Kbndo ‘wheel’ (10.76). ;
Lett. vag'i, above, 1.
Lett. divrici (esp. ‘two-wheeled cart? also rid, Mithl.-Endz. 3.522), opd. of div- for divi ‘two’ and form related to ritents ‘wheel’ (10.76). Likewise diy. ritenis ‘bicycle’ and ‘two-wheeled cart’, Mihl.-Endz. 1.473.
7. ChSl. kola, kolesa, SCr. kola (Pol, kolasa, kolaska, Russ. koljaska dim. ‘calash’), pl. of kolo ‘wheel’ (10.76), Berneker 548.
ChSl. voz, Boh. viz, povoz, etc., above, 1.
SCr. taljige, Russ. telega ‘cart? (Pol. telega, etc., not ordinary word), fr. Turk. talika ‘light four-wheeled carriage’. Miklosich, Tiirk. Elemente 2.46. Briick- ner 568.
8. Skt. vahana-, vaha-, above, 1.
Skt. ydna- : 7- ‘go’ (10.47).
Skt. anas- (mostly ‘draught-wagon, cart’) : Lat. onus ‘load’. Walde-P, 1.132f. Ernout-M. 703.
Skt. ratha-, Av. ra8a- ‘chariot’ : Lat. rota, Lith. ratas ‘wheel’ (10.76).
Av. vaga- : varat- ‘turn’ (10.13-14). Barth. 1418.
10.76 WHEEL Grk. —_zpoxés (xbxdos) Goth. .... Lith. ratas, tekinis ‘ NG —zpoxés, pda ON —hwel, hjal, hvel Lett. rats, ritenis, skritulis Lat. rota Dan. jul ChSl. kolo It. —ruota Sw.  hjul SCr. kolo, totak, kotat Fr. roue OE hwéol Boh. kolo Sp. rueda ME _hwele, whele Pol. kolo Rum.  roaté NE wheel Russ. koleso Ir. droch, roth Du. wiel Skt. cakra- NIr. roth OHG rad Av. éazra- W. olwyn, rhod MHG rat Br. rod NHG rad
Words for ‘wheel’ include an inherited group derived from a root for ‘turn’ and others from roots meaning ‘run’ or ‘roll’,
1. IE *kvelo-s, *kolo-s, redupl. *keeklo-s, fr. *kvel- in Skt. car- ‘move,
wander’, Grk. wédouat ‘be in motion’, etc. Walde-P. 1.514 ff. Falk-Torp 413. ON hvel; OPruss. kelan; ChSl., SCt.s
Boh. kolo, Pol. koto, Russ. koleso; Grk.
? kixdos ‘ring, circle’, also rarely ‘wheel
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
yoTlON; ai Fakes 93.340, mostly 1 Or
e hjul, OF jg, Hom: a a], Dan., SW. Ms wei ON ad a "wool, ME hwele, i ee el; Skt. cakra-,
u. Wr ipheles * i och. A kukdl, B kokale garrd-s
Ay. & 3 : - in Ir. rethim ‘ago ‘vs, of 1B +reth- 1D. ’
```


## [2026-09-06T22:07:30.316Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for L in 966 967 968; do echo \"== leaf $L ==\"; awk -v n=$L 'BEGIN{RS=\"\\f\"} NR==n+1' SYN.txt | head -12; done",
 "description": "Buck around printed 905"
}
```


## [2026-09-06T22:07:31.429Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for L in 1496 1497 1498 1499; do echo \"== leaf $L ==\"; awk -v n=$L 'BEGIN{RS=\"\\f\"} NR==n+1' SYN.txt | head -8; done",
 "description": "Buck around printed 1436"
}
```


### [2026-09-06T22:07:32.008Z] TOOL RESULT

```
== leaf 966 ==
 (> ME flatt, NE flat > W. jflat), Dan. jlad, Sw. flat: ChSI. ploskt (*plat-sko- or *plak-sko-?), SCr. plosnat, Boh. plosky (Boh. plochy prob. fr. OHG flah, Ge- bauer 1.441, Vondrak 1.436; otherwise Brickner 419), Pol. ptaski, Russ. ploskij.
3. Grk. wedtevds, later redivés, only of ‘flat’ country, deriv. of zedloy ‘plain’ : mébov ‘ground’,
NG z\axwrés ‘compressed, flat’, fr. mhaxavw ‘compress’, deriv. of rAdé ‘flat stone’.
4. Rum. ges, only of ‘flat’ country, fr. Lat. sessus ‘seated, settled’. Tiktin 1411. Puscariu 1586.
Rum. lat ‘broad’ (11.61), used also for ‘flat’ dishes. Tiktin 892.
5. Ir. réid, NIr. réidh, also ‘clear, open, ready, smooth’ prob. orig. ‘pas-
sable’ (of a road, ete.) : riadazy ON rida id., ete. Pedersen 1.58.
W. gwastad ‘level, flat’, also and orig ‘steady, constant’ : Ir. fossad ‘firm’, fr *upo-stato-, IE *sta- ‘stand’, Walde-p. 2.605. Pedersen 1.34,
Br. kompes, also ‘smooth, polished’ MBr. compoes ‘equal’, beside W. cafe hwys-iad ‘adjustment, quality’, prob, epd. of kom-, cym- ‘co~’ and poez ‘weight? (fr. Lat. pénswm). Loth, Mots lat. 156, Henry 75.
6. Goth. ibns (only dat. Sg. ana stada tbnamma = emt rérov redwod Lk. 6.17), OE efen (ME, NE even), etc., general Gme. word for ‘even, level’ and so some- times of ‘flat’ land, etc., etym. dub. Walde-P. 1.102. Feist 287.
ME playne (NE plain only sb. in this sense), fr. OF r. plain (above, 2).
7. Lith. lékStas, Lett. lens, prob. : MHG lage ‘low, flat’, ON lagr ‘low’, etc. Walde-P. 2.462. Miuihl.-Endz. 2.465.
== leaf 967 ==
qzony Russ, vognutyj Skt. ullaéna- Av. ieee
But words that are used for ‘hollow’ only in this latter sense as NG xobguos (: Gri. xodpos ‘light, unsubstantial’, late also ‘empty’), and others listed under ‘empty’ (13.22), Pol. prézny, Russ. pustoj, Skt. ¢unya-, are not included in this list.
1. Derivs. of IE *¢eu- seen in numer- ous words with common notion of curved, whether convex (as Skt. ¢va-
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
EEE EE ee
gpATIAL RELATIONS:
‘be pregnant’ , kdpa
rk Kut ‘e. Walde- gel os or concave, 28 De aap igavo® ff Brnout- y :
, 1101 eB. ® (Fxopidos); Lat. Mooutns
"3 TOS ik. ee cavus (> It. cavo) Ir (7 Port “1 (tbl with Br. keo ‘cave’, fr. VW. ca
cfd, °° of, Loth, Mots lat. 145).
ate Balounss; dim. of Bais ‘deep’ i
== leaf 968 ==
igim ‘stretch out’, Goth. uf- rahjan ‘stretch out’, etc. Walde-P. 2.362 ff. Ernout-M. 855, 856 ff. Falk- Torp 891. REW 2648.
Lat. réctus (> Sp. recto), diréctus, VLat. *déréctus (> It. diritto, dritto, Fr.
Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
896 SELECTED INDO-EUROPEAN SYNONYMS
droit, Sp. derecho, Rum. drept), verbal adjs. of regere, dirigere (above); OIr. diriuch, diriug, MIr. direch, NIv. direach (loanwords? cf. Pedersen 1.229, 2.116); Goth. raihts, ON rétir, etc. general Gmc. (the orig. meaning preserved in NHG senkrecht ‘plumb’, aufrecht, NE upright, and NHG rechter winkel, NE right angle, etc.); also ON rakr, Sw. rak (= Hast Frank. rak ‘right’, MLG rak ‘straight, in order’); Skt. rju-, Av. arazu-.
2. Grk. et#is, Ion. t6ts, relation and orig. obscure. Walde-P. 2.450. Boisacq 294, 370.
Grk. 6p66s (fopfo-, *ropO¢o-), orig. and in actual use mostly ‘upright, ver- tically straight’ : Skt. ardhva- ‘upright, raised’, urdh- ‘increase’, mid. ‘grow’, Av. varad- ‘increase’, etc. Walde-P. 1.289. Boisacq 711.
NG iows ‘straight, even, flat’, fr. isos ‘equal’ (12.91).
3. W. union, cpd. of un- ‘one’ and iawn ‘right, just’? = Br. eeun ‘straight, right, just’, etym. dub. (see 16.73).
4. ON beinn, Norw. bein, Sw. dial. ben, beside ON beinka ‘straighten’, etym.? Falk-Torp 70. Torp, Ny- norsk 20.
Dan. lige, also ‘equal, alike’, weak form of lig ‘like, similar, equal to’ (: ON likr, Goth. galeiks ‘like’, etc.). Falk- Torp 642.
```


### [2026-09-06T22:07:33.767Z] TOOL RESULT

```
== leaf 1496 ==
gunna, W. gun (also gunna mor, gun maur ‘great gun, cannon’), fr. ME gonne, gunne (below, 4). Parry- Williams 158.
W. cyflegr ‘cannon’ (cf. Evans s.v.), etym.?
W. magnel ‘cannon’, fr. ME magnel, fr. OF r. mangonéel, dim. of MLat. man- ganum, fr. Grk. payyavov roneutxov ‘bal- lista’. Parry-Williams 75. NED s.v. mangonel. REW 5297.
Br. fusil and kanol, fr. Fr. fusil and canon.
4. ME gonne, gunne (Latinized as gunna, cf. magister gunnarum, 1414), NE gun, etym. disputed, but prob. orig. a nickname (like Brown Bess, Big Bertha, etc.), shortened fr. a name like ON Gunnhilda. Cf. una magna ballista de cornu quae vocatur Domina Gunilda, 1330. NED s.v. For another possible main or contributory source, namely OFr. dial. engon = engin (source of NE engine), cf. Weekly s.v. and Jenkins, Language 4.235 ff.
ME, NE cannon (canones, seu instru- menta Anglice gunnes vocata 1407, gret gonnes of brasse called cannons 1525), NHG kanone, Du., Dan., Sw. kanon, fr. Fr. canon, It. cannone (above, 2).
NE rifle in earliest use the ‘groove’ in the gun barrel, fr. vb. rifle ‘form the grooves’, fr. LG rifeln id. : OE gerifled ‘wrinkled’ (NE obs. rivel ‘wrinkle’ sb. and vb.), etc. NED s.v. Falk-Torp 898.
CC-O0. In Public Domain. Gurukul Kangri Collection, Haridwar
== leaf 1497 ==
h. délo, Pol. dzialo ‘cannon’, orig. ‘work’ (concrete, ‘piece of work’), as ChSI. délo, etc. (9.12). Berneker 194. Briickner 109.
Pol. strzelba ‘gun’, fr. strzelié ‘shoot’, fr. strzata ‘arrow’ (20.25). Briickner 522.
Russ. ruz/e ‘gun’ : oruzie ‘weapons’ (20.21). Briickner 381.
20.29 GUNPOWDER
Grk. Bayz. Borévn Dan.  krudt NG Laxapotre (aruptrts) Sw. krut MLat. pulvis ME i poudre It. polvere NE powder Fr, poudre Du. kruitt Sp. polvora MHG kriit Rum. praf, iarbéi NHG pulver NIr. padar
Ww. pylor, powdr
Br. poulir
Most of the words for ‘gunpowder’ are the same as those for ‘powder’ in gen- eral, which are the same as, or derived from, those for ‘dust? (1.218). While they may be made more Specific by com- pounds or phrases, like NE gunpowder,
== leaf 1498 ==
 Skt.  dyudha- NIr. Gide (catha) OHG - saro, gisarawi Av. varaba- WwW. arfogaeth MHG harnas(ch), sar, ge- Br, harnez serwe
NHG  riistung, harnisch
Many of the words for ‘weapons, arms’ (20.21) cover both offensive and defensive arms. The latter may, of course, be expressed more specifically by the addition of ‘defensive’, ‘of (or for) defense’, e.g. Grk. irda dyuvrixd, Fr. armes défensives, NHG_ schutzwaffen, Lett. aissardzibas ieroci, SCr. orudje za obranu, Boh. zbrané ochranné, Pol. bro
odporna. Such obvious phrases are not entered in the list. Apart from a few repeated from 20.21, those entered are such as correspond most nearly to NE armor in its historical uses.
Some of them may cover the whole military equipment but are used mostly of defensive armor. Some may cover all defensive arms including the shield,
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
y Digitized by Arya Samaj Foundation Chennai and eGangotri
1398
== leaf 1499 ==
coat-of-mail, body- armor’, they also have a wider scope, as originally.
3. Ir. gatsced, possibly late borrow- ing fr. W. gwisgad ‘clothing’ (6.12). Pedersen 2.4.
NIr. éide (catha), lit. ‘clothing (of war)’, cf. Ir. éach, NIr. éadach ‘clothes’ (6.12).
W. arfogaeth, deriv. of arfog ‘armed’, fr. arf ‘weapon’ (20.21).
Br. harnez, prob. fr. Fr. harnais, har- nois, but with change of. suffix. Henry 157. Otherwise Thurneysen, Keltorom. 37 f.
4. Goth. sarwa (pl.; renders dma, mavordia), OE searu (also ‘cunning’), OHG saro, gisarawi, MHG sar, geserwe, cf. ON sgrvi ‘necklace’ (of pearls or precious stones), prob. : Lat. serere ‘join, compose, contrive’, Ir. sreth ‘row, serics’, Grk. dpyos ‘necklace’, etpw ‘fasten to- gether in rows, string’, etc. Walde-P. 2.500. Falk-Torp 960. Feist 411.
ON herkledi, OE herewed, both lit. ‘army-clothes’ (cf. 20.15, 6.12).
ON herneskja, ME harneis, NHG har- misch, etc., see under OFr. herneis (above, 2).
```


## [2026-09-06T22:07:41.430Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== leaf 977 ==\"; awk 'BEGIN{RS=\"\\f\"} NR==978' SYN.txt | head -20; echo; echo \"== leaf 1536 ==\"; awk 'BEGIN{RS=\"\\f\"} NR==1537' SYN.txt | head -20",
 "description": "Buck leaves 977, 1536"
}
```


### [2026-09-06T22:07:43.101Z] TOOL RESULT

```
== leaf 977 ==
tula- : vrt-, Lat. vertere ‘turn’, etc. Walde-P. 1.274. Uhlen- beck 275.
Av. skarana- : Ir. cruind, ete. (above, 3). Barth. 1587.
12.82 CIRCLE
ie Goth. .. Lith.  apskritis, ratas mes ON hringr, kringla Lett. rin’k'is circulus Dan.  kreds ChSl. kragit ta, cerchio Sw. krets SCr.  krug he Ml OE trendel, hring Boh. kruh lem ME _scercle Pol. koto, krag Cilairt. of NE circle Russ. krug crc Porcul Du. cirkel, kring Skt.  mandala-, cakra- cylch, cant OHG  (A)ring, creiz Ay. oe kele'h i MHG kreiz, rinc Words aoe NHG_ kreis dots ain ‘circle’ are from various xokda, ‘wheel’: Skt. cakra- ‘wheel, Stal pone ete Of ‘turn’. But in | circle’, Av. éakra-, ON Ayol, OE hweol,
Mobably ae the most widespread and
@ a Dein farliest use was to desig- SPecially « ‘ object of circular shape, I, fel’ or ‘ring’.
Tk, KUKXos, also, esp. in neut. pl.
etc. ‘wheel’ (10.76), fr. reduplicated forms of the root *kel- in Grk. wé\opar ‘be in motion, be’, Skt. car- ‘move about’, etc. Walde-P. 1.575.
2. Lat. circulus (> It. cerchio, Fr.
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
906 SELECTED INDO-EUROPEAN SYNONYMS
cercle; lit. loanwords It. circolo, Sp. cfr- culo), dim. of circus (> Rum. cerc ‘circle’, but It. cerco obs., Sp. cerco in secondary.uses), which it replaced in the sense ‘circle’, the latter coming. to be the ‘circus’ (esp. Circus Maximus, and then others) : Grk. xlpxos, xpixos ‘ring’, fr. the root *(s)ker-in Lat, curvus ‘crooked’, etc. (12.74). Walde-P. 2.569. Ernout- M. 188 ff. Walde-H. 1.220f. REW 1947, 1948.
3. Ir. ciiairt, perh. loa

== leaf 1536 ==
to’, as legal term, ‘sue’.
Dan. klager, fr. MLG (below).
Sw. kdrande, fr. kdra ‘bring suit, prose- cute’ = ON kera ‘accuse’ (21.31).
OE ftéond, pres. pple. of téon ‘accuse’. Less commonly wrégend and onspreca, onsprecend, fr. wrégan and onsprecan ‘accuse’.
ME askere, fr. aske ‘ask, seek’ (18.35).
ME pleintif, NE plaintiff, the same word as adj. plaintive fr. OFr. plaintif ‘complaining, plaintive’ (: plaindre, cf. above, Fr. plaignant). NED s.v. plain- uff.
OHG sahhu (‘der anklager’ Grimm, Deutsche Rechtsaltertiimer 2.488 ; where quotable? Graff has sahhari ‘litigator’) : sahha ‘lawsuit’ (21.13).
MHG, MLG klager (> Dan. klager), NHG (an)kldger, fr. MHG, NHG klagen ‘complain, charge’ (OHG klagén ‘com- plain’), NHG anklagen ‘accuse’. Simi- larly Du. (aan)klager.
Du. eischer, fr. eischen ‘demand, claim’ (18.35).
5. Lith. deskovas, fr. zegkoti ‘seek’ (11.31). Lett. apsiidzétajs, fr. apsidzét ‘accuse,
sue’.
6. SCr. tuzitelj, fr. tuziti ‘complain, sue, accuse’.
Boh. Zalobce, fr. zaloba ‘complaint, charge’, cf. (ob)Zalovati ‘sue, accuse’.
Pol. skarzacy, fr. (0)skarzyé ‘accuse’.
Pol. powéd ‘cause, occasion’ (like Russ. povod), also ‘plaintiff’, orig. ‘lead- ing’: ChSl. vedq, vesti ‘lead’ (10.64). Briickner 433, 628.
Russ. istec, also ‘creditor’ : istyj ‘true, genuine’, ChSl. istt% id. (16.66), with de- velopment ‘real owner’ > ‘creditor’ > ‘plaintiff’.
7. Skt. arthin-, fr. artha- ‘object, mat- ter, thing’ (9.90), hence lit. ‘having to do with a certain matter’, as ‘plaintiff’, with praty-arthin, ‘defendant’, e.g. Manu 8.79, Yajii. 2.6, 7.
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
| |
Digitized by Arya Samaj Foundation Chennai and eGangotri
```


## [2026-09-06T22:07:56.347Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('SYN.txt',encoding='utf8',errors='replace').read()\npages=t.split('\\f')\nfor i in range(1500,len(pages)):\n    m=re.findall(r'\\b(14\\d\\d)\\b',pages[i])\n    if m: print(i,m[:4])\nEOF",
 "description": "Find printed 14xx page numbers"
}
```


### [2026-09-06T22:07:57.911Z] TOOL RESULT

```
1500 ['1400']
1501 ['1401']
1502 ['1402']
1503 ['1403']
1504 ['1404']
1505 ['1405']
1506 ['1406']
1507 ['1407', '1421']
1508 ['1408']
1509 ['1409']
1510 ['1410']
1512 ['1411', '1412']
1513 ['1413']
1514 ['1414']
1516 ['1415', '1416']
1518 ['1417']
1519 ['1418', '1419', '1420']
1520 ['1421']
1521 ['1422']
1523 ['1423', '1424']
1525 ['1425']
1526 ['1426']
1527 ['1427']
1528 ['1428']
1529 ['1429']
1532 ['1431']
1533 ['1432']
1535 ['1433']
1536 ['1434']
1538 ['1435']
1539 ['1436']
```


## [2026-09-06T22:08:00.292Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==1540' SYN.txt | head -40",
 "description": "Buck printed 1436"
}
```


### [2026-09-06T22:08:01.821Z] TOOL RESULT

```
7. Skt. pratyarthin-, epd. of prati- ‘against’ and arthin- ‘plaintiff’ (21.21).
Skt. prati-vadin-, cpd. of prati- ‘against’ and vadin- ‘plaintiff’ (21.21).
Skt. abhiyukta-, pass. pple. of abhi- yuj- ‘charge, accuse’, and so opp. of abhiyoktar- ‘plaintiff’ (21.21).
atsakovas : at-
21.283 WITNESS (sb.)
Grk. —_waprus Goth. wettwops Lith. liudininkas NG baprupas ON valtr, vitni Lett. liecinieks Lat. _ testis Dan. vidne ChSl.  sitvédételt It. testimonio Sw. vitine SCr. _— sujedok
Fr. témoin OE gewita, gewilnes Boh. — svédek
Sp. testigo ME _ witnesse Pol.  §Swiadek Rum. martor NE witness Russ. _ svidelel’
Ir. fiadu Du. geluige Skt. saksin- Nir. —_ fiadhnéidh OHG = giwizzo, urcundo Av. vikaya- W. tyst MHG _  geziuc, urkunde
NHG zeuge
Words for ‘witness’ are derived from verbs for ‘know, recognize, see, remem- ber, or declare’. A few are based on ‘third person’, or ‘outsider’, or just ‘people’, through the common inference of ‘not party to the suit’.
Words for ‘testify’ and ‘testimony’ are generally parallel forms, mostly de-
Br. test
rived from those for ‘witness’, as Grk. paptupéw, paptupia, Lat. testificart, testi- monium, Goth. wettwodjan, weitwodet, Ch8&l. stivédételtstovatt, stivédételisivo. The Lith. current nouns are derived from the verb, but the latter is ultimately based on a noun for ‘witness’.
In. several cases the words for ‘testi-
CC-O0. In Public Domain. Gurukul Kangri Collection, Haridwar
1436
mony’ came to be used also, and then mainly, for the personal ‘witness’, as Fr. témoin, NE witness.
’
1. Derivatives of IE *wezd- ‘see (15.51) and ‘know’ (17.17). Walde-P. 1.236 ff. Feist 560.
Tr. fiadu, acc. fiadna (Laws, Gloss. 356), Nir. fiadhnéidh; Goth. weitwops (perf. act. pple.), ON viini, Dan. vidne, Sw. vitine, OF gewita, (ge)witnes, ME witnesse, NE witness (ON, OE also and orig. ‘testimony’ and so still NE, esp. bear witness), OHG giwizzo; ChSl. stivéd- ételt (prefix sti-), Russ. svidet
```


## [2026-09-06T22:08:08.410Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==1541||NR==1542' SYN.txt | grep -n -i \"vikaya\\|vīkaya\\|kas-\\|Av\\.\" | head -20",
 "description": "Buck witness continuation"
}
```


### [2026-09-06T22:08:10.044Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T22:08:12.268Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR>=1541 && NR<=1543' SYN.txt | head -50",
 "description": "Buck 21.28 continued"
}
```


### [2026-09-06T22:08:13.958Z] TOOL RESULT

```
el’, SCr. sujedok, Boh. svédek, Pol. Swiadek.
2. Grk. paprus, gen. -vpos (nom. also ndprup, Hom. pdprupos), NG pédprupas
 : peéptuva ‘c
are’, Lat. memor ‘mindful of’, Skt. smr- ‘remember’, ete. Prob. based on *yap-rv- (IE -iu- suffix in abstracts, etc.) orig. ‘testimony’. Walde-P. 2.689. Boisacq 612.
3. Lat. testis, lit. ‘the third’ (= Ir. triss ‘third’), fr. *tristi- : trés ‘three’. Cf. Osc. irstus ‘testés’ (fr. *tris-to-), tris- taa
```


## [2026-09-06T22:08:18.761Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"vikaya\\|vfkaya\\|vikaya-\" SYN.txt | head; echo \"--- full leaf 1541 tail ---\"; awk 'BEGIN{RS=\"\\f\"} NR==1542' SYN.txt | tail -30",
 "description": "Search vikaya in Buck"
}
```


### [2026-09-06T22:08:20.184Z] TOOL RESULT

```
35862:Ir. fiadu Du. geluige Skt. saksin- Nir. —_ fiadhnéidh OHG = giwizzo, urcundo Av. vikaya- W. tyst MHG _  geziuc, urkunde
--- full leaf 1541 tail ---
 : peéptuva ‘c
```


## [2026-09-06T22:08:27.892Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### PHD\"; grep -n \"^čaš\\|^čāš\\|^wāzār\\|^wizār\\|^wizārdan\\|^kištan\\|^čar\\|^kāri\\|^kār-\\|^čašm\" PHD.txt PHD_mackenzie.txt | head -40",
 "description": "MacKenzie Pahlavi lookups"
}
```


### [2026-09-06T22:08:27.940Z] TOOL RESULT

```
### PHD
PHD.txt:297:čāšt 22 činwad
PHD.txt:298:čāšt [ой | N ~] lunch, meal. 1~ag [-k'] food. &а$їар [c'štk'] doctrine. čāštan, čāš- [c?s-tn'] teach. ~išn: teaching. čatrang [cting | (Ar. šatranj)] chess. *taw(la)gan [cwpk'n!! | Ar. sawlajan, N čaugān] (curved) polo-stick ; polo. CaxSágih [ch kyh] (sense of) taste. čaxšišn [chsfn! | M, J схі, N ¿aš-] taste, flavour. 148 [ME < A mh | M cy, N či] what, which. ~ ray: for what, why. ~ih: quiddity, essence. tčē [ME, v. 166] for, because, since, as, that. &ë-ëwënag [ME ^ dwynk!] how. ~ith : circumstances. čegām-iz [су?т-с | M cyg^myc], —-6(w): a little; whatever. Cegámag [cyk”mk! | N &(ag)áma] song, snatch. €éh- , —išn, v. idan. *téhag [cyhk'] grief. čehel [40 | N chil] forty. Céh-widarag [cyhwtlg] = činwad puhl. čēlān [cy”x! | = M, N ~] dagger. ~gar [-kl, -gl | N ~] swordsmith. Cér [cyl | M cyr, N —] victorious, triumphant, brave. —Ih: bravery. Cérihistan, Cérih- [cylyh-stn'] triumph, be victorious. īčīdan, čīn- [cytn', cyn- | M cyydn, cyn-, N ~] gather, pile up. ~išn: gathering. *čīdan, čēh- [cytn', cyh- | M cy-] mourn, lament, grieve. ~i8n : lamentation. ~i$nig¢ : mournful. ihr [cyhl | M cyhr, № ~] form, shape, appearance, face. žčihr(aģ) [cyhl(k') | M сулу, P -g, № ~] seed, origin; nature, essence. Cihrénidan, čihrēn- (cyhlyn-ytn'] form. Cihrig [cyhlyk'] natural. čihr-šnāsīh [суйру] physics. čim [c(y)m | M сут, N ~] reason, cause, purpose, meaning. ~ (ray): why? Cim-gó6wáàgih [сут gwh’kyh] logic. čimīģ [cymyk!] purposeful. čīn-, ~i8n, v. idan. čīnag [cynk! | P cyng, N ~a] grain, bait. Cinàr [су | N ~] oriental plane tree. činwad [cynw(p)t'], ~ puhl: the ‘divider bridge’ which separates the souls of the righteous dead, who cross, from those of the wicked, who fall off.
PHD.txt:656:wizārd-wars 93 xün
PHD.txt:3776:čašmag, xān(īg),
PHD.txt:4571:čarbīh
PHD.txt:4577:čarbišn čim čambar čamišn sang!
PHD.txt:4578:čašm
PHD.txt:4580:čašmareškīh “49 ~~ -euq
PHD.txt:4581:čašmarešk čašmagāh čašmagāhīh 1 ģašmag čašmdīd
PHD.txt:4589:čāšišn, čaxšišn
PHD.txt:4609:čāšīdan
PHD.txt:5057:kār- wing! *kār-ān kārāgāh kārāgāhīh kārdāg kārīgīh kārīg kārēzār kārawānīg kārawān kārnāmag kahrubāy kalbodómand kālbod kārframān kārd
```


## [2026-09-06T22:08:29.308Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### CHEUNG\"; grep -n \"\\*čar\\|\\*kaš\\|\\*karš\\|\\*kaHs\\|čāšīdan\\|wizārdan\\|wāzār\" CHEUNG.txt | head -30",
 "description": "Cheung lookups"
}
```


### [2026-09-06T22:08:29.360Z] TOOL RESULT

```
### CHEUNG
3287:*čar(H) and *gam! ? Rastorgueva — Edel’man (ESIJa П: 261 f.) cite a late Skt. form 
16468:248 *kaš 
57374:*karH’, *karš/*xrah
```


## [2026-09-06T22:08:40.383Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '16460,16530p' CHEUNG.txt",
 "description": "Cheung *kaš entry"
}
```


### [2026-09-06T22:08:40.435Z] TOOL RESULT

```
«PIE 9 Pokorny, Le cites NHG hager ‘gaunt, haggard’, Lith. kaséti ‘to lessen, 
become thin, dry’ as possible cognates. The origin of NHG hager (incl. Engl. 
haggard < Fr. hagard < Germanic ?) is obscure though, Seebold (Kluge 2002: 383b) 
considers Skt. krsä- ‘id.’ as a semantically more satisfactory connection to NHG 
hager. As for the Lith. form, it appears to have a variant katéti, both forms have a 
popular flavour according to Fraenkel I: 227b f. = LIV: — | Pok.: 521 f. 


248 *kaš 


*REFERENCES: KPF I: 152b; Abaev, Slovar’ I: 589, 119; DKS: 57a f., 193b; Cheung 2002: 158; Lecoq 
2002: 605b, 631b, 680a. 


*kaS ‘to imprison’ 

*AVESTAN: (?) Y Av. kas- ‘to hold, grasp ?’ = Liste: 16 

Caus.: pres. IND. 3sg. YAv. kasaiieiti (V 18.4), INJ. 3sg. YAv. kasaiiat ‘[Pahl. transl.] суур (P 36) 
*MIDDLE PERSIAN: ? MMP gys- ‘to bind, tie’ || (+ *ham-) ? MMP hngys- ‘to fasten 


to’. 0 MMP gys- has been abstracted from hngyst ? = DMMPP: 170b, 181a f. 

Partic.: perf. pass. MMP gyst; Pass.: pres. IND. 3sg. MMP gysyhyd || (+ *ham-) Partic.: perf. pass. MMP 
hngyst; Pass.: pres. IND. 3sg. MMP hngysyd, SUBJ. 3sg. MMP hngsyh’d 

*PARTHIAN: (+ *pari-) prg’c- ‘to imprison; incarcerate? = Ghilain: 99 | DMMPP: 
278a 

Pres.: IND. 35р. prg’cyd; Partic.: perf. pass. prgst, prgstg, П ? prg’c’d 

*SOGDIAN: (+ *pati-) CSogd. ptqys- ‘to imprison, confine’ || (+ *pari-) MSogd. prqys 
‘to imprison’. 9 A hapax nominal derivative CSogd. ptq's is attested in C2 94V.26 
(Sims-Williams 1984: 169). The form has an unexpected final -s, as observed by 
Sims-Williams 1979: 133 f. This may simply be a spelling mistake, cf. BSogd. prk’s 
‘imprisonment’ (SCE 133). 

(+ *pati-) Fut.: IND. 3sg. CSogd. ptq.stq' (C2 51V.4 Ё); Partic.: perf. pass. CSogd. "ptqsty (CH 25У.18]), 
CSogd. ptqsc (Ё) (C2 94R.16), CSogd. "ptqystyt (pl.) ‘imprisoned, confined’ (|C2 64R.28|) || (+ *pari-) 
Impf.: IND. 3sg. MSogd. pryqys (M129R.13), MSogd. prykyys (M133 Ri.15); Pass.: pret. IND. 3pl. 
SSogd. (’krt’nt) prkyst'kt ‘were) imprisoned’ (ХІ iiR.1) 

*CHORESMIAN: (+ *pari-) p’rk’sy- ‘to imprison’ = Samadi: 153 

*NEIR: Sariq. kaSan ‘chains’ 

A root *kas was first established, on the basis of the MIr., by Henning (BBB: 96 
ad b74 and apud Boyce 1952: 448, fn. 4.). This was further elucidated by Sims- 
Williams 1979, l.c. There is no etymology for *kas. 


“PIE LIV: - | Pok.: 
*REFERENCES: EVS: 41b; Sims-Williams 1979: 133 f.; Sundermann 1992: 92, ad 21 


*kaué ‘to bend, draw into, contract’ 

*MIDDLE PERSIAN: ? MMP qxs' n ‘bending ?’ {hapax} || (+ *а-) MMP ’’gws-, BMP 
’kws-, "kwh- ‘to hang up, fasten’ || (+ *ni-) MMP ngwc- ‘to bow, prostrate, bend 
(the knees)’. © The -s- in MMP ’’gwst, BMP ’kwstn is secondary, v. Sims-Williams 


1979: 135. = DMMPP: 215b, 30b, 240b 
(+ *ā-) Partic.: perf. pass. MMP ’’gwst, BMP "kwst /agust/, "kwht /aguxt/; Inf: BMP ’kwhtn /aguxtan/ || 
(+ *ni-) Pres.: IND. 1р1. MMP ngwcym, 3р1. MMP ngwcynd; Partic.: perf. pass. MMP ngwcyd 


*PARTHIAN: (+ *4-) ’gwxt (ppp.) ‘hung up’ = DMMPP: 30b 
*KHOTANESE: (+ *us-) uskuj- ‘to rise up (against)’ || (+ *pati-) ? pasküj- ‘to strike’ ||
```


## [2026-09-06T22:08:45.281Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^\\*ka[HhāaS]\\|^\\*ča\\|^\\*kar\\|^\\*čar\\|^\\*kaH\" CHEUNG.txt | head -40",
 "description": "Cheung root headwords"
}
```


### [2026-09-06T22:08:45.334Z] TOOL RESULT

```
2937:*čai2 27 
3149:*čaiš (*kai8) ‘to assign, make known, teach’ 
3230:*čak/g ‘to strike, hit’ 
3287:*čar(H) and *gam! ? Rastorgueva — Edel’man (ESIJa П: 261 f.) cite a late Skt. form 
15222:*kaHm 227 
15232:*kaH ‘to take pleasure, desire’ 
15263:*kaHm ‘to desire, love’ 
15502:*kar8/*xrah. 
15768:*kar ‘to do, make’ 
15819:*kar 237 
15919:*karé ? ‘to strike’ 
15927:*karH2 239 
15939:*kard ? ‘to stick, keep down ?’ 
15960:*karH! ‘to celebrate, praise’ 
15984:*karH ‘to spread out, scatter (esp. seed), sow; to make furrows, plough’ 
15989:*karaja- ~ *krsta- (i.e. root *kars-/*xrah-) in Pir. cf. Emmerick 1966: 612; Sims- 
16048:*kars/*xrah 241 
16074:*karp ? ‘to lament, moan, mumble’ 
16092:*kars/*xrah ‘to draw, plough’ 
16172:*kartl 243 
16180:*kars-/xrah- and *karH’- either show mutual influence, cf. Sh. kiräx(t), etc., or are 
16196:*kart! ‘to cut’ 
16271:*kart? ‘to twist, turn’ 
16305:*karz ? ‘to cheat, deceive’ 
16475:*kaS ‘to imprison’ 
55117:*kard (s.v.), *tund 
55142:*kar (s.v.), *pas (s.v.), *sam 
55231:*čať , *fraiH 
55321:*kar (s.v.), *sac’, *tary (s.v.), 
56193:*kart', *saH, *tas, *9uars, 
56308:*kaH', *kaHm, *rauj’, *xSij, 
56353:*kar, *uarz 
56434:*kar (s.v.) 
56439:*čaš , *huar' (s.v.), *JiauH 
56443:*čaš , *srasc 
57090:*kaHm, *kanH’, *yarHz 
57096:*kar, *tas 
57106:*karH? 
57242:*karp 
57363:*kar (s.v.)
```


## [2026-09-06T22:08:47.660Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '15984,16050p' CHEUNG.txt",
 "description": "Cheung *karH 'to sow'"
}
```


### [2026-09-06T22:08:47.704Z] TOOL RESULT

```
*karH ‘to spread out, scatter (esp. seed), sow; to make furrows, plough’ 
*AVESTAN: YAv. kar- (caus.) ‘to spread out’ || (+ *pari-) ‘to plough around’ || (+ 
*fra-) ‘to do by furrowing, ploughing’. 0 YAv. kar- (etc.) is root kar^- іп AiW: 449. 
According to Kellens 1974: 136, the causative appearance of this root is analogically 
built after the type iSatia-. It seems easier, however, to assume a suppletive system 
*karaja- ~ *krsta- (i.e. root *kars-/*xrah-) in Pir. cf. Emmerick 1966: 612; Sims- 
Williams 1985: 99, ad 52R.9-10. = Liste: 15 


240 *karH2 


Caus.: pres. IND. 3sg. YAv. karaiieiti, Y Av. frakäraiieiti (N 101, Yt 4.6), INJ. 3sg. YAv. frakäraiiat (V 
22.20), OPT. 25р. Y Av. frakaraiiois (V 9.10 Ё), pairi.käraiiöis (V 17.6), 3р1. Y Av. käraiion (V 6.2) 
*MIDDLE PERSIAN: MMP q’r-, BMP KL /kar-/ ‘to make furrows; sow’, MMP ’gyrd 


(with neg. a-) ‘unploughed, untilled’ = DMMPP: 202b, 31a 

Pres.: IND. 3sg. MMP q’ryd, IMPV. 2р1. MMP and Partic.: perf. pass. MMP kyst 

*PARTHIAN: k’r- ‘to sow, plant’? > Ghilain: 98 | DMMPP: 202b 

Pres.: IND. 3sg. “k’ryd, “q’ryd; Partic.: perf. pass. kyst, qyst 

*KHOTANESE: kär-, OKh. ker- (caus.) ‘to plant’ || (+ *nis-) LKh. naskär- ‘to drag 
away’ || (+ *ham-) Khot. hamg(g)ar- ‘to draw together’. 0 The exact meaning of 
(hapax) LKh. naskirrdä in passage P 2893.199 KT 3.90 is uncertain. Emmerick 
(SGS: 50) derives LKh. naskirr- from a root *kar- ‘to cut’, PIE *(s)ker-, which is not 
clearly attested in other Iranian languages (perhaps Chor. krwy- ‘to trim, cut’, no 
etym. given by Samadi 1984: 104). The quoted Av. form frakoronaot (V 22.2) may 
rather belong to root *kar'- ‘to do, make’ (cf. Kellens 1984: 171, fn. 5). The 
connection suggested by Bailey (DKS: 177), viz. with *kar’-, is solely based on his 
interpretation of the passage concerned. — SGS: 22, 23, 50, 137 

*SOGDIAN: BSogd. kyr ‘to plant, sow’, SSogd. ks(-), CSogd. qs(-) ‘to sow’ (cf. 
Sims-Williams 1984: 99, s.v. 52R.9-10, fn. 29) 

Pres.: SUBJ. 2sg. BSogd. kyr’ (Vim. 30), ОРТ. 3sg. CSogd. qsy (C2 52R.9); Pret.: tr. IND. 3sg. CSogd. 
qst’rt (C2 54R.26); Partic.: perf. pass. SSogd. kst ‘spread’ (AL 3.22), BSogd. kst'k ‘sown; seed’ (Vim. 
11(N)) 

*CHORESMIAN: k’ry- ‘to till; sow, plant’ || (+ *fra-) m/’sk’ry- ‘to impregnate’ 
c» Samadi: 99, 9 

*NWIR: Widely attested: NP kistan/kar- ‘to plant, sow’, Kurd. (Sor.) kétan/két-, 
Awrom. keláy/kel- ‘to plough’, Zaz. käritis/kären-, Abz. kasta/kär-, Qohr. kasta/kar- 
‘to sow’, Gz. kar-/kast, Khuns. kar-/kara, kast, Siv. kar-/kist ‘to plant’, Nn. kast/kar- 
‘to sow, plant’, Abyan. kast/kar- ‘to plant, sow, cultivate’, Abz. kas/kar- ‘to plant, 
sow’ 

*NEIR: Oss. I. keelyn/kald, D. kaelun/kald (pass./intr.) ‘to flow; to be pulled down; to 
stumble’, I. kalyn/kald, D. kalun/kald (caus./tr.) ‘to pour, spill; to throw on the 
ground’, Sh. Cär-t, Rosh. cér-t, Bart. Cor-t, Sariq. Cor-t, Yzgh. Kär-d ‘to plough, sow, 
cultivate’, Sangl. kir-/kurt ‘to plough’, M. kor-/kask-, Yi. kār-/kišč- ‘to sow, plant’, 
Pash. karal ‘to till, cultivate’, Wa. ksrr-/kord-, kast ‘to cultivate the land (by plowing 
and sowing)’, Wa. ёыге ‘line, furrow’, Yghn. kista ‘field’ || (+ *ui-) Sh. wijar-/wijart 
‘to scatter (manure)’, ? Oss. I. xelyn/xald, D. ixzlun/ixald ‘to be spoilt, ruined, 
destroyed’, Oss. I. xalyn/xzeld, D. ixalun/ixald ‘to spoil, ruin, destroy’ || (+ with sec. 
æm-) ? Oss. I. aepparyn/zeppaerst ‘to throw’. > Oss. xælyn, etc. are rather connected 
to Skt. skhal ‘to trip, stumble, halt, go astray’ ? This suggestion can be found on the 
margin of H.W. Bailey’s copy of IEW, p. 929. 


*kars/*xrah 241
```


## [2026-09-06T22:09:01.717Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '16050,16075p' CHEUNG.txt; echo \"=== kars entry ===\"; sed -n '16092,16200p' CHEUNG.txt",
 "description": "Cheung PIE lines for karH2 and kars"
}
```


### [2026-09-06T22:09:01.775Z] TOOL RESULT

```
*SANSKRIT: kar ‘to strew, scatter’ (RV+) || саг ‘to move, roam, go’ (RV) > EWAia 
I: 311 (534 ff.) 

9 The meanings all refer to the planting process, cf. LIV: 354, fn. 5. The situation 
has been further complicated by the old causative formation *k"olH;-eie- of IE 
*kelH;- ‘to move, turn’ (cf. *éarH), which would have yielded the same result as the 
causative of IE *kerH- ‘to scatter (seed), sow’ in Iranian. It is impossible to separate 
the two formations in most Ir. languages. 

“PIE 1. *К“егН- ‘to spread, scatter (seed), sow’, *k” orH-eje- (caus.) || 2. *k"olH;-eie- 
(caus.) ‘to make furrows, plough’ — LIV: 353, 386 | Pok.: (933 f.) 639 

*IE COGNATES: 1. Olrish fo-ceird ‘throws, puts’ || 2. Gr. noA£$0 Yñv ‘I plough the 


earth’, Lat. colo ‘I cultivate’ 

*REFERENCES: EVP: 33; IIFL II: 218a, 399a; Abaev, Slovar’ I: 578, 569 f., 169 f.; MacKenzie 1966: 99; 
EVS: 26b, 89b; WIM I: 69; WIM II/1: 78; WIM III: 111; Abaev, Slovar’ IV: 170 f., 138 f.; Werba 1997: 
277; Paul 1998: 303a; Steblin-Kamenskij 1999: 221, 138; Cabolov 2001: 548; Cheung 2002: 196; Lecoq 
2002: 121 ff. (passim) 


*karp ? ‘to lament, moan, mumble’ 

=== kars entry ===
*kars/*xrah ‘to draw, plough’ 
*AVESTAN: YAv. Каг$- ‘to draw (furrows), plough’ || (+ *apa-) ‘to drag away’ || (+ 


*aua-) ‘to draw down’ || (+ *pari-) ‘to draw around’ © Liste: 15 
Pres. them.: IND. 3pl. YAv. auua.karosonti (V 5.5), OPT. 35р. YAv. apa.karsöit (N 48), ҮАУ. 
pairi.karsöit (V 19.21), 3р1. YAv. karsaiion (Yt 19.80) 


"MIDDLE PERSIAN: MMP krs-, qrs- ‘to pull, draw’ || kyst (pret. stem) ‘to sow, plant’ 


(supplet. stem of k’r-, *karH) > DMMPP: 208b 
Pres.: IND. 1р1. MMP krsym: Partic.: perf. pass. II MMP qrsyd || Partic.: perf. pass. MMP kyst 


*PARTHIAN: kyst (pret. stem) ‘to sow, plant’ (supplet. stem of k’r-, *karH?) 
=> Ghilain: 96 | DMMPP: 202b 

Partic.: perf. pass. kyst, qyst 

*SOGDIAN: BSogd. хг ‘to pull, attract’, CSogd. xš ‘to drag’ || (+ *apa-) BSogd. 
"px r/n$, CSogd. рхёп ‘to remove, eliminate’ || (+ *a-) BSogd. ’’k’ys(-) ‘to pull out’ 


242 *kars/*xrah 


|| (+ *ui-) BSogd. wx’rs, CSogd. wxs, MSogd. wxnš ‘to deliver, save’ || (+ *ham-) 
BSogd. ’nx’s-, CSogd. nxš- ‘to withdraw, retire’, (caus.) SSogd. ’nxrs(-) ‘to 
subjugate, overtake [i.e. to cause to withdraw]’ (on *r see GMS: $147) 

Pres.: IND. 3sg. BSogd. xrst, OPT. 3sg. dur. BSogd. xns’y ’Stn; Impf.: IND. 3sg. CSogd. xs; Inf.: pret. 
CSogd. xst, MSogd. ’kstyy (Sogd.Tales: 469), MSogd. ksty (ВВВ: 35), MSogd. kstyy (BBB: 42) || Pres.: 
IND. 35р. CSogd. grwst, SUBJ. 159. CSogd. qrwsn; Partic.: pres. CSogd. qrwsny || (+ *apa-) Pres.: IND. 


35р. BSogd. ’px’rst, BSogd. ’px’nst, BSogd. px’nst, SUBJ. 1sg. BSogd. px’rs’n, 35р. BSogd. px ns't, 
IMPV. BSogd. рх ri? (GMS: $698: subj.); Inf.: BSogd. ’px’rs’y, BSogd. ’px’ns’y, BSogd. px’ns’y || (+ 
*2-) Pres.: IND. 3pl. BSogd. ’’k’ys’ntw || (+ *ui-) Pres.: IND. 35р. BSogd. wx’rst, SUBJ. 1sg. BSogd. 
уух т°п, 3sg. CSogd. wxst, PREC. 3sg. MSogd. wnxsytyy; Impf.: IND. 3sg. CSogd. wyxs; Fut.: IND. 
3sg. CSogd. wxstq’; Partic.: pres. CSogd. wxsnw; Inf.: BSogd. cnn wx’rs’y || + *ham-) Pres.: SUBJ. 3sg. 


BSogd. "nx '$'t; Caus.: fut. IND. 159. SSogd. SSogd. ’nxrs’m km 

*CHORESMIAN: xSy- ‘to draw, drag’, xSs- (sec. pass./inch.) ‘to be dragged’, m/xry- 
(caus. ?) ‘to draw’ || (+ *apa-) pxry- ‘to draw out’ || (+ *upa-) bks- ‘to feed’ (< *‘to 
look after’) || (+ *pati-) pcxrs- (intr./inch.) ‘to pull oneself back; to stop, become 
quiet/still’, p’cxr- (caus. ?) ‘to restrain, pull back’. o The Chor. formation m/xry- 
reflects an old caus. *xrahaja-, after which the intervoc. -h- disappeared. 
Subsequently, the long *4 was shortened in front of *; which is in line with other 
ЕП. languages. = Samadi: 242, 240, 21, 164 f., 147 

*BACTRIAN: Kıbaryo ‘plough-(ox)’ (U8) => S-W, Bact.: 199b 

*NWIR: Widely attested: NP kasidan/kas- ‘to pull, draw’, Bal. kast, kaš(š)it/kaš(š)-, 
Kurd. (Kurm.) Kisin/Kis-, Kesan/kes-, (Sor.) kisan/kisé- ‘to drag [intr.], crawl, be 
drawn, slip, flow’, Zaz. kiristis/kiréSen- ‘to drag’, Abz. kesa/kes-, Anar. -ikeso/ 
(impv.) ikis, Awrom. kesay/kes- ‘to draw, pull’, Fariz. -ki$ä-/-kis-, Yar. -kisa/-kis-, 
Gz. kás-, keš-/käšā, Gil. (Rsht.) -kaSe-, Gur. (Kand.) kisa-/-kis-, Ham. kásayán/Kes-, 
Isfah. kesän/kes-, Khuns. kes-/kesa, Mah. kis-, Nn. kisa/kis-, Natan. -kiS-/kis-, Siv. 
kis-, kes-, käš-/kišā, kešā, Soi bä-nkisa (sic!), Tal. kaše, Varz. kasä/kas- ‘to draw, 
pull’ 

*NEIR: Oss. I. xaessyn/xast, D. x&ssun/ast (< I. ?), xaersun/xarst ‘to carry; to breed, 
raise; to cultivate, plant; to last, endure’, Wa. xa$-/xaSt- ‘to draw, pull, drag; to 
carry’, Yghn. kis-, kis-/kista ‘to sow’, xaš-/xášta ‘to draw’, Yi. xóš-/xíšč-, M. xas- 
‘to pull, drag’, ? Sh. kiräx(t), Rosh. kiréx-t, Yzgh. xarax-, Вагі. Ciröxt, Orosh. kiroxt 
‘to remove, haul, drag’, Khf. хахё ‘ploughing’, M. kugo ‘plough’ (*krsaka-) || (+ 
*abi-) Oss. I. ivxzersyn/ivxerst, D. evxaersun/evxa(r)st ‘to put across across a river, 
dangerous place; to lead someone; to help someone who is in trouble, danger; to 
rescue, save’ || (+ *ham-) Oss. I. æxxæssyn/æxxæst ‘to reach, attain’, D. 
ænxæssun/ænxast ‘to seize, grab’ 

*MISC: Par. kas ‘eyebrow’ (kas kan- ‘to pull, stretch, contract’ < NP) 

*SANSKRIT: kars ‘to pull, drag, plow’ (RV+) = EWAia I: 319 


*kartl 243 


9 The root *kars- appears to have a rare variant *xrah-, with a different kind of 
ablaut (i.e. Schwebeablaut), similar to *fras-/pars-. This may therefore account for 
the initial x- in some Iranian forms. The frequent loss of the liquid *r is quite 
striking as well. The root *kars-/xrah- specifically refers to the ploughing process, 
after which the field can be sown in, i.e.*karH^-. As a consequence, the roots 
*kars-/xrah- and *karH’- either show mutual influence, cf. Sh. kiräx(t), etc., or are 
part of a suppletive paradigm. 

*PIE *K"els- ‘to plough’ = LIV: 388 f. | Pok.: 639 

*IE COGNATES: Hitt. /gulsanzi/ ‘they scratch into’, Gr. téAoov (n.) ‘last furrow of the 
field’ 

*REFERENCES: KPF I: 82b, 144b f., 248b; Ivanow 1926: 420; IIFL I: 267b; KPF II: 217; Christensen, 
Contributions I: 71, 169 f., 262; IIFL II: 216a, 269a; Abrahamian 1936: 116, 130; Lambton 1938: 41a, 
77b; Abaev, Slovar’ I: 556, 223 Ё; Andreev — PeSéereva 273a, 357a Ё; MacKenzie 1966: 100; EVS: 41b, 
99b; WIM I: 69; WIM II/1: 78; WIM III: 111; Abaev, Slovar’ IV: 188 ff.; Werba 1997: 171; Paul 1998: 
303b; Steblin-Kamenskij 1999: 406; Cabolov 2001: 555; Cheung 2002: 247 f., 108 ff.; Lecoq 2002: 147 
ff., 153 (passim); Korn 2005: 318, 392 


*kart! ‘to cut’ 

*AVESTAN: YAv. kart- ‘to cut’ || (+ *aua-) ‘to cut down to’ || (+ *upa-) ‘to cut on’ || 
(+ *fra-) ‘to cut up’ > Liste: 15
```


## [2026-09-06T22:09:14.893Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"čarH\\|CarH\\|\\*ĉarH\" CHEUNG.txt | head -20; echo ---; sed -n '3240,3330p' CHEUNG.txt",
 "description": "Cheung *čarH"
}
```


### [2026-09-06T22:09:14.954Z] TOOL RESULT

```
3346:*CarH ‘to come and go, wander’ 
56589:*CarH (s.v.), *kars/xrah 
57338:*CarH (s.v.), *paH! 
---
du-Coekaenoen/du-Coekoen- ‘to glue, stick together’, NP ¿ak ‘fissure, rupture, cleft, 
crack’ 

*NEIR: Oss. I. cæğdyn/cağd, D. cae£dun/cagd ‘to shake (out); to strike the iron; to 
play on an instrument, clock’ ? Yzgh. cok-/Cokt ‘to pound; to stamp, put on a pattern 


32 *éam ? 


[of tattoos]’, Wa. cuk-/Cukt- ‘to strike’ (LW ?), ? Sh. cuy, Rosh. coy ‘breaking, 
tearing, ripping up’ (EVS: 23a: < **¢/@r/dr-agu- ?) || (+ *fra-) Oss. D. 
rezegdun/rezaxt, (inch.) D. rezaxsun/rezaxst ‘to spread around, scatter’, Oss. 
rezegd ‘heap’ || (+ *ui-) Oss. D. izæğdun/íizağd ‘to spread, scatter’, Oss. D. Z&gn& 
‘tinder’ 

*MISC: (+ *pati-) Arm. patéén (LW), Hebr. ptsgn ‘copy’ (LW, Esther 3:14), Syr. 
рагёарпа ‘copy’ (with sec. -r-, Benveniste 1934: 180 ff.) 

© The root is no doubt expressive in origin. A second expressive/onomatopoetic root 
is cited in ESIJa II: 211 f.: *éak ‘to drip; flow’. Most, if not all, Iranian forms seem 
to point to borrowing from (New) Persian cakidan/Cak-, which evidently cannot go 
back to РЇ. 

*PIE— > LIV: – | Pok.: 


*REFERENCES: Christensen, Contributions I: 62; Abaev, Slovar’ I: 298 f., 540 f.; Abaev, Slovar’ II: 363 f.; 
Edel’man 1971: 62; Nyberg II: 147a; ESIJa II: 213 ff. 


*éam ? ‘to walk’ 

*PARTHIAN: cm- ‘to walk, move to’ => Ghilain: 56, 72 | DMMPP: 125b 

Pres.: IND. 3sg. cmyd, 3р1. cmynd, SUBJ. 25р. cm’h, 1р1. cm’m; Partic.: perf. pass. H cm’d; Inf.: cm’dn 
*KHOTANESE: ? tcama- ‘leaping insect, either locust or grasshopper’ 

*NWIR: NP Camidan ‘to walk proudly’, Bal. Camit/Cam- ‘to shake, dance, prance, 
dangle’ 

*MISC: Par. é(h)im-, ¢(h)em-/c(h)imi ‘to go, move, wander’, Par. &imö ‘walking, 
gait’, Arm. (LW) ¿em ‘walk’ 

*SANSKRIT: camüra- ‘an antilope’ (Harav., Sis.) > EWAia Ш: 180 f. 

9 This sparingly attested root does not have an IE origin and may be a blend of 
*čar(H) and *gam! ? Rastorgueva — Edel’man (ESIJa П: 261 f.) cite a late Skt. form 
camura- ‘an antilope’, which would be borrowed from an Iranian, possibly Parthian, 
source. Skt. camura- is perhaps rather a so-called "substrate" word, as it 
phonologically conforms to the category of forms with long middle vowel, e.g. 
mayüra- ‘peacock’, on which see Lubotsky, Early Contacts:305 ff. 


*PIE— > LIV: – | Pok.: 
*REFERENCES: IIFL I: 246a; DKS: 139a; Shahbakhsh: s.v. ¿am- 


*tap ‘to seize, attach, stick, strike’ 

*KHOTANESE: ? Khot. cev- ‘to get? — SGS: 34 

*SOGDIAN: (+ *fra-) MSogd. Br’cp- ‘to press’ (cf. Sims-Williams, apud Sundermann 
1981: 181b) 

Impf.: IND. 3pl. MSogd. Br'cp nt (MKG: 593) 

*CHORESMIAN: čp- ‘to attach to, contrive (a lie) against (someone)’ = Samadi: 58 f. 


*éarH 33 


*NWIR: NP capidan/cap-, Gur. (Kand.) ёараи$ап kär-, Khuns. Cap-/Cäpä ‘to plunder, 
rob’ (LW), Bal. campit/Camp-, canpit/Canp- ‘to snatch’, NP cafsidan, Abz. 
cawsowa/caws-, Nn. Cäsb-, Qohr. Caspada/éasp-, Tr. Cawsa(ya)/Caws- (inch.) ‘to 
stick, adhere’, ? Anar. Capowger ‘robber, thief? 

*NEIR: Oss. cevyn/cavd, D. cævun/cavd ‘to hit, strike’, Yghn. Cümf-/£ümfta ‘to push 
(to)’, Sh. cäp-/cäpt ‘to feel, touch’, Oss. І. cefsyn/cefst, D. caefsun/caefst (inch.) ‘to 
stick, glue’, M. cab-/cavd ‘to pluck’ || (+ *us-) Oss. I. sk’afyn/sk’eft, D. (z)sk’zfun 
/(#)sk’aft (sk’avd) ‘to carry, drag (quickly); to grab’, Wa. skaf- ‘to slip, shift to’ || (+ 
*ni-) Oss. I. nysevyn/nyzavd, D. nizzvun/nizevd, (inch.) D. niz&vsun/niz&vst ‘to 
touch (on)’, ? Sh. (Baj.) nijüv-/nijüvd ‘to pack up, put to bed’ || (+ *ham-) Oss. I. 
anzavyn/znzavd, D. anzzevun/enzevd ‘to touch’. > The derivation of Wa. skaf- 
from *us-kaf-, with prev. *us- ‘up’, is semantically implausible, cf. *us-kas’ ‘to 
ascend, go up’ (*kas” ‘to fall’). || Sh. (Baj.) nijüv-/nijüvd from *ni-Cauba-, cf. Lat. 
cubare, etc. ??, EVS, l.c. 

© This root may have an IE etymology. The connection with Gr. kat, Lat. capere, 
etc. (cf. IEW, l.c.) 1s semantically very attractive. IE "a" would not palatalize the
```


## [2026-09-06T22:09:18.210Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '3346,3440p' CHEUNG.txt",
 "description": "Cheung *čarH entry"
}
```


### [2026-09-06T22:09:18.255Z] TOOL RESULT

```
*CarH ‘to come and go, wander’ 

*AVESTAN: car- ‘to come and go’ || (+ *para-) ‘to pass over’ || (+ *ui-) ‘to go to and 
fro’ || (+ *ham-) ‘to walk around’ — Liste: 21f. 

Pres. them.: IND. 3sg. YAv. äcaraiti (Yt 8.8, Yt 8.46, Yt 10.112, Yt 10.137), YAv. fracaraiti (Yt 18.3 f.), 
med. ? Y Av. fracaraite (Yt 10.112), 3du. YAv. caratö (V 13.49), med. ? YAv. “fracaraéte (Yt 10.112), 
Y Av. fracaröide (Y 9.5), 2р1. med. YAv. fracara0Be (Yt 13.34), 3pl. YAv. caronti (N 52), INJ. 3р1. med. 
Y Av. fracaronta (V 2.11, V 2.15, V 2.19), SUBJ. 1р1. ? OAv. сагат (Y 44.17), med. Y Av. fracaräne (Y 
9.17), 3sg. YAv. carat (Y 9.24), OPT. 3sg. med. YAv. fracaraeta (Yt 13.107), 3du. med. YAv. 
vicaraiiatom (N 79), IMPV. 25р. med. YAv. ham.caran‘ha (Yt 17.60), 3pl. YAv. vicarontu (Yt 13.156); 
Partic.: pres. YAv. para.caront- (Y 62.8). 0 A different interpretation for OAV. caraiti and carani is given 
by Kellens — Pirart 1990: 229. On the correction of Y Av. fracaraite to “fracaraéte see Klingenschmitt 
1972: 91, n. 1. YAv. fracaröide is originally 2du. med., on which see Kellens 1984: 212 f. 

*MIDDLE PERSIAN: MMP cr- ‘to pasture, graze’ || (+ *para-) MMP przyr- ‘to keep 
away from’, MMP prc’r- (caus.) ‘to refrain, withhold, keep back’ || (+ *ui-) ? BMP 
wcl- /wizar-/ ‘to get through’, MMP we’r-, BMP wc /wizär-/ (caus.) ‘to separate, 


34 *éarH 


divide’. © BMP wel- /wizar-/ is deduced from the reading in KAP ii,28, which 
Nyberg 1974 II: 210 interprets as vicarét, being derived from a verb BMP wcy- 
/wizar-/, is uncertain. BMP wc'l- /wizar-/ with the meaning ‘to fulfil, (accomplish, 
perform)’ may have a different origin: < *ш-Каг-. = DMMPP: 126a, 283b, 278a, 


351b 

Pres.: IND. 3pl. MMP crynd || (+ *para-) Pres.: OPT. 3sg. MMP hyb przyryd; Caus.: pres. 3pl. MMP 
“pre’rynd || (+ *ui-) Caus. ?: pres. IND. 1sg. BMP we’lym /wizarém/, BMP we’lyh /wizare/, 3sg. MMP 
we’ryd, BMP wc yt /wizared/, 3р1. BMP we’lynd /wizarend/, IMPV. 2sg. MMP we’r-; Partic.: perf. pass. 
MMP wyc’rd, BMP we’lt /wizard/; Inf.: caus. ВМР ус іп /wizärdan/ 


*PARTHIAN: сг- ‘to pasture, graze’ || (+ *para-) prc r- (caus.) ‘to withhold, keep back’ 
|| (+ *ш-) wyc’r- ‘to perform, accomplish = Ghilain: 57, 73 f. | DMMPP: 126a, 
278a, 351b 

Pres.: IND. 3pl. crynd || (+ *para-) Caus.: pres. IND. 3sg. pre’ryd, SUBJ. 2sg. pre’r’h, 3sg. “pre’r’h || (+ 
*yi-) Pres.: IND. 2sg. MMP wyc’ryy, 3sg. we’ryd, wyc’ryd 

*KHOTANESE: (+ *ati-) ? LKh. ttäjser- ‘to surpass’. 0 Cf. DKS: 122a. Khot. car- ‘to 
go on a course’ (DKS: 99b) is probably not genuine: < BSkt. = SGS: 38: ‘to 
dispraise(?)’ 

*NWIR: NP Caridan ‘to graze, pasture’, Bal. cart/Car- ‘to graze, feed’, car(r)it/Car(r)- 
‘to turn, move’, Carag “pasture, grazing’, Kurd. (Kurm.) čērīn/čēr-, Zaz. Cérayis/ 
ceren-, Tal. čarde, Abz. Cerowa/cer-, Khuns. ёіг-, Ham. čärayän/čär-, Siv. čar- ‘to 
pasture’, NP Caränidan/Carän-, Meim. bem-tfernä/a-tfern-, Qohr. cerna/ cern-, Tr. 
cernä/Cern- (caus.) ‘to graze’, Zaz. Carnayis/Carnen- ‘to lead around, let walk around’ 
|| (+ *ui-) NP guzardan/guzar- ‘to accomplish [work, job, etc.], perform [e.g. prayer]; 
to pay; to explain, interpret’, Kurd. (Kurm.) bzartin/bzér-, (Sor.) bzardin/bZér- ‘to 
select, distinguish’. 0 NP guzardan/guzar- with the meaning ‘to fulfil, (accomplish, 
perform)’ may have a different origin: < *ui-kar-. || Kurd. (Kurm.) bZartin/bZer-, 
(Sor.) bZardin/bZer- are not connected with Oss. І. evzaryn/evzerst, D. evzarun/ 
&vzurst ‘to pick out, choose; to separate [etc.]" (v. *yar(H)'), pace Cabolov, l.c. 
*NEIR: Oss. I. ceryn/card, D. cærun/card ‘to live’, Oss. I. аг-сагуп/аг-сага, D ær- 
carun/er-card (caus.) ‘to give life, revive’, Pash. caredol ‘to graze’. Ф These verbal 
forms are unrelated to Oss. I. angaryn/enzerst, D. enzarun/enzarst (caus.) ‘to 
kindle, light a fire’, cited by Abaev, Le: 158 f. They rather contain the root *gar’ ‘to 
heat’. 

*SANSKRIT: car ‘to move, walk, go, wander, travel’ (RV+), > Also in Wai. caräy ‘to 
pasture’ = EWAia I: 534 f. 

PIE *K"elH;- ‘to move, turn, wander; to pasture; to settle and cultivate’ 0 This verb 
seems to describe several stages of the Indo-European way of living, viz. nomadism, 
followed by pastoralism and (semi-)sedentary agriculturalism. = LIV: 386 ff. | 
Pok.: 639 


*Cas2 35 


*IE COGNATES: Gr. méA0p01 ‘I move [intr.]’, Zero (aor.) ‘was, were, happened’, 


Lat. colo (caus.) ‘I till, cultivate, inhabit’, Olrish bua-chail (m) ‘cowherd, bouvier 
*REFERENCES: Horn 1893: 204; EVP: 17; Abrahamian 1936: 111; Abaev, Slovar’ I: 303, 291, 158 f.; 
Werba 1997: 286 f.; Paul 1998: 293; Cabolov 2001: 253, 214 f.; Lecoq 2002: 125, 591 (passim); ESIJa II: 
227 ff.; Korn 2005: 84, 133, 319, 370 (passim) 


*кд «to teach, show’ 

*AVESTAN: Ү Ау. са$- ‘to teach, show’ = Liste: 22 

MED.; Pres. athem.: IND. 3sg. YAv. caste (N 17), SUBJ. 3sg. YAv. casäite (Fr.); Partic.: pres. ҮАУ. 
casana- (Y 13.3) 

“MIDDLE PERSIAN: ВМР cé /¿8š-/ ‘to teach’
```


## [2026-09-06T22:09:26.309Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '3428,3500p' CHEUNG.txt",
 "description": "Cheung *čaš entry"
}
```


### [2026-09-06T22:09:26.353Z] TOOL RESULT

```
Werba 1997: 286 f.; Paul 1998: 293; Cabolov 2001: 253, 214 f.; Lecoq 2002: 125, 591 (passim); ESIJa II: 
227 ff.; Korn 2005: 84, 133, 319, 370 (passim) 


*кд «to teach, show’ 

*AVESTAN: Ү Ау. са$- ‘to teach, show’ = Liste: 22 

MED.; Pres. athem.: IND. 3sg. YAv. caste (N 17), SUBJ. 3sg. YAv. casäite (Fr.); Partic.: pres. ҮАУ. 
casana- (Y 13.3) 

“MIDDLE PERSIAN: ВМР cé /¿8š-/ ‘to teach’ 

Pres.: IND. 3sg. BMP c’syt /cased/, IMPV. 2р1. BMP c’syt /caséd/; Partic.: perf. pass. BMP с? /Cast/; 
Inf.: caus. BMP c’stn /¿aštan/ 


*PARTHIAN: c’S- ‘to teach" = DMMPP: 124a 
Pres.: IND. 2pl. c’syd 


*KHOTANESE: OKh. kät’- ‘to think; protect’ || (+ *aua-) vaj(s)äs- (vaj(s)is-) ‘to 
perceive, see’ || (+ *pati-) OKh. päjsas- ‘to look at’ || (+ *ni-) nijsas- ‘to show’ || (+ 
*ham-) OKh. hamjsas- ‘to be about to; intend to’ > SGS: 22, 117, 82, 53, 139 
*CHORESMIAN: mj/c’ty- (denomin.) ‘to convey secretly, disclose in secret’, c'tyk 
‘riddle’ || (+ *ni-) ’nc’h- ‘to show’, ? m/ncs(y)- ‘to look at’. o Henning 1958: 111 
derives Chor. m/ncsy- from *ni-CaSia- (corresponding to ’nc’h- ‘to show’), "wie Itr. 
zu Tr. (oder Kaus.)". Samadi objects to this derivation as we would rather expect the 
outcome *m[ncs-, cf. byws- ‘to become silent’ < *apa-gaus(a)ia-. Also, m/ncsy- has 
a direct object (-’h ‘him’) as well. Her objections may be circumvented, if -y- in the 
impf. form mncsyd-’h is the secondary, "unstable" y (NB: the geminate sign is 
optional!). Of course, the (old) caus. formations can also correspond to "normal" 
transitive formations as well. > Samadi: 48, 118 f., 121 

*BACTRIAN: (+ *ham-) ? av&nbayo ‘will, wish’ > S-W, Bact.: 180a 

*NWIR: Gur. čāšīáīn/-čāšy- ‘to be accustomed to, adept at’ 

*NEIR: (+ *ni-) Yi. nisáZ-/nisaZi-, M. nijas-/nijast- ‘to show’ 

*SANSKRIT: caks ‘to shine, appear; observe, see’ (RV+) = EWAia I: 523 

© This common Пг. root is probably originally an IE redupl. formation of *k”eK-, Ir. 
*kas', cf. LIV, ibid. 

*PIE ? *k"e-k"K- 0 Thus Lubotsky. Differently Lippe, LIV, Le: desid. *k”ek-s-. 
c» LIV: 383 ff. (fn. 12 f£) | Pok.: 638 

*REFERENCES: KPF II: 178; IFL: II: 233b; Werba 1997: 426 Ё; ESIJa II: 235 ff. 


*а? ‘to drip; to drink, eat ?’ 
*MIDDLE PERSIAN: MMP c’xs- (redupl.) ‘to let taste’, MMP c’snyg ‘taste’, BMP c’st 
/cast/ ‘meal’ > DMMPP: 125a, 124a 


36 *éat ? 


Partic.: perf. pass. MMP c’xsyd 

*PARTHIAN: c’Snyg ‘taste’ > DMMPP: 124a 

*KHOTANESE: (+ *aua-) OKh. vatcis- (vatcäs-) ‘to besprinkle’. ó The reconstruction 
hesitantly suggested by Emmerick (SGS: 117), viz. *aua-scasa- as an s-extension of 
IE *skek-, is best to be discarded as other Iranian correspondences rather presuppose 
the existence of Ir. *cas-, which was hinted at by Bailey (DKS: 373). > SGS: 117 
*SOGDIAN: BSogd. cs’nt, BSogd. cs’nty, CSogd. cSnt ‘drink’ || (+ *pati-) CSogd. 
peš- ‘to drink’, BSogd. ptcs-, BSogd. "pc's-, MSogd. pcs- ‘to taste’ 

(+ *pati-) Pres.: IND. 3sg. BSogd. ’pe’sty, 2р1. ? MSogd. pcst’h, SUBJ. 1sg. CSogd. рс п; Inf.: BSogd. 
ptes’t
```


## [2026-09-06T22:09:36.558Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '3500,3540p' CHEUNG.txt",
 "description": "Cheung *čaš2 continued"
}
```


### [2026-09-06T22:09:36.604Z] TOOL RESULT

```
*CHORESMIAN: С$- ‘to drop’ = Samadi: 52 

*NWIR: NP čašīdan/čaš-, borrowed into Bal. cas(S)it/Cas(S)- ‘to taste, sip’, Abyan. 
Cast/Cas- ‘to taste, savour’, NP cast ‘noon; breakfast’, Gz. Cast ‘noon’ 

*NEIR: Pash. cagal ‘to drink’, ? Pash. cac-eg- ‘to drip’ || (+ *pati-) Yghn. 
p’cas-/p’cästa ‘to taste, try’. © On Pash. cac-eg-: "... srasc, caus. srascaya- ‘to drip’ 
would have given PS. *Xac-. Poss. contaminated by Prs. cakidan", МЕУР: 17; EVP: 
16 £. 

*MISC: Arm. (LW) ¿aš ‘breakfast’, ¿ašak ‘taste’ 

*SANSKRIT: cas ‘to eat’ (Dha.), casaka- ‘drinking vessel’ (class.) > EWAia III: 183f. 
9 The root is exclusively Iranian: the Skt. forms are late and no doubt loanwords 
from Iranian. The attempt of Rastorgueva — Edel’man, ESIJa II: ibid., to link it to 
*kas! ‘to look, appear’ and *čaš! ‘to teach, show’ meets semantic difficulties. 
Starting from ‘to see, be shown’ the assumed shift to ‘to try’ is not very likely, but 
more importantly, the original meaning of *ёа$ is perhaps rather ‘to drip, sprinkle, 
drink’, if we also consider the Khotanese and Choresmian forms. The latter forms 
are left out in this entry of ESIJa II. 


*PIE— > LIV: —| Pok.: 
*REFERENCES: Hübschmann 1895: 51; КРЕТ: 81a f., 141b f.; EVP: 18; Andreev — PeSéereva: 305a; DKS: 
101a, 137b; WIM II/2: 648; Lecoq 2002: 574a; ESIJa П: 235 ff.; Korn 2005: 114 


*&at ? ‘to tremble, shake’ 

*MIDDLE PERSIAN: MMP cn-, BMP cnd- /cand-/ (with n-infix ?) “о tremble, shake 
[intr.], MMP cnyh- (caus.) ‘to shake [tr.] = DMMPP: 126a 

Pres.: IND. 35р. BMP cndyt /canded/, 3р1. BMP cndynd /candend/, SUBJ. 3р1. MMP cn'nd; Caus.: pres. 
IND. 3pl. MMP “cnynynd; Partic.: perf. pass. MMP cnyst; Pass.: pres. IND. 3р1. MMP *cnyhynd 
*PARTHIAN: “cnd- ‘to tremble, shake’ > DMMPP: 126a 

Pres.: IND. 3sg. "cndyd 

*NWIR: NP Candis ‘severe tremor’, Delij. čandeš ‘tremble, larzis’, also borrowed in 
Bal. Candag ‘to shake’
```


## [2026-09-06T22:10:10.087Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### SOD cxr\"; grep -n \"cxr\\b\\|čaxr\\|c'xr\" SOD_pages.txt | head -10; echo \"### SOD leaf 197 (p131)\"; awk 'BEGIN{RS=\"\\f\"} NR==198' SOD_pages.txt | head -20",
 "description": "Sogdian dictionary cxr"
}
```


## [2026-09-06T22:10:11.737Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### SNS kištan\"; grep -n \"kist\\|kišt\\|kist-\\|kāšt\" SNS_pages.txt | head -20",
 "description": "Shayast ne Shayast glossary kištan"
}
```


### [2026-09-06T22:10:11.873Z] TOOL RESULT

```
### SOD cxr
12760:          159, 161; AVS 108                                               caxr ©ace. -w; nom., ob. -y(h) =>cxr-, ckkr
12820:                                                                         cakr ©ob. -v ^5rm)yk ckkr, cyr-, cxr-
13222:3313 cxr- M                                    £^                    Jewish
42621:                                                                                                               tcxr ibex* t&»\t x\rAAt\t j^i^j
### SOD leaf 197 (p131)
                                                                                                                        132
 cym'yS py5Y

 3332 cym'yS pySY B, S                                         3348 cyncr S                                     Ojt>T<^N
      cime5 piSar                                                   clncar ?
                                                      CfJ^S.
      on this account, therefore                                    sieve
      BSTBL, Vim. 73, 161, Dhu. 239, 277, 284; MSP b                Frag. Len. 93.35
        172
                                                               3349 cyndr M                                 Ojj-^<J^<>wl

 3333 cymnt =» cym'nt                                                ci/ondar =^cndr, cyntr1
 3334 cymt*     C =* cym-                                            in, inside
                                                                     BBB 667; GMS 1484, 1611; KG, MSP el7
 3335 cymyd      C =» cymy5(5)
                                                               3350 cyndrcyk       M                           ,^jj*<J^fc
 3336 cymy5(5)     M, S              (u>>>^      j^)oTtjT jl
                                                                    cindarcik      ©pi. -t
      cimc5     (cymyd, cy, -my5)    ^cynVySCh), c-                 internal
      of it                                                          GMS 1014; BBB 671
```


### [2026-09-06T22:10:11.913Z] TOOL RESULT

```
### SNS kištan
8823:                                                                                      •(   kist: jl owlja*,)            af rkiltan:
13151:                                                                                                                               -VVI^ -o^**1* :jordag kistan:                                 |ftt)U*3   3*»>^
16057:kas 29/17                kistan 220/6                        kustar 218/9           man I atasan 240/2
16095:hom-dron 74/24                                                 jordag kistan 336/3       kara&n 310/20
```


## [2026-09-06T22:10:21.467Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('SOD_pages.txt',encoding='utf8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if '3313 cxr' in p or ('cxr' in p and 'wheel' in p.lower()):\n        print('--- leaf',i,'---')\n        idx=p.find('cxr')\n        print(p[max(0,idx-600):idx+900])\n        break\nEOF",
 "description": "Find Sogdian cxr entry"
}
```


### [2026-09-06T22:10:23.156Z] TOOL RESULT

```
--- leaf 190 ---
 125                                                                                                                     ckkr

        GMS 150, 277, 508, 610; TSP 526, 79; SCE 156,                3180 cyr-  B, S                             <^><£>r
          159, 161; AVS 108                                               caxr ©ace. -w; nom., ob. -y(h) =>cxr-, ckkr
 3168 cpt- B                                              jjbi>           wheel, circle
      capd ©pt, st.                                                       TSP 2.144, 216, 924; Frag. Len. 93.17: O2 17
      GcOsteal                                                       3181 cyrh =* syrh
      TSP 5.112,7.138
                                                                     3182 cys- S                              j*f<&fsSj>
 3169 cptVmyk B                                            fJl^           caxs ©pt. cYsty ? ^'c'xs-, ptexs-
      caftarmik ? ^ctP'rmyk                                               0o)take, (to)grasp
      fourth                                                              MDii pl27npl28, 8
      GMS 442; TSP 2.326                                             3183 cysty S                                     •jzSj*
 3170 cptw      B
```


## [2026-09-06T22:10:29.828Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('SOD_pages.txt',encoding='utf8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if '3313' in p and 'cxr' in p:\n        print('--- leaf',i,'---')\n        idx=p.find('3313')\n        print(p[max(0,idx-400):idx+600])\n# also find printed 203 and 131 markers\nfor i,p in enumerate(pages):\n    head=p[:200]\n    if head.strip().startswith('131') or head.strip().startswith('203'):\n        print('LEAF',i,'head:',head.strip()[:60])\nEOF",
 "description": "Locate SOD cxr- entry and pages 131/203"
}
```


### [2026-09-06T22:10:31.983Z] TOOL RESULT

```
--- leaf 196 ---
                     Jewish
      having fought                                             3323 cxwdJny C                                  <s^jh <*ji*-
                                                                     caxu5ane
                              *
     C2, 104R 10
3312 cxnty => cx>ty
                                                                     STi 45.19; STii 6.1-, GMS 1041
3313 cxr- M                                    £^                    Jewish
     caxr ©Av. caxra ©ace. -vv, ob. -yy =»cyr-,                 3324 cxw6 Py6>ny S
       ckkr                                                          caxu5-pay5ane
     wheel                                                            synagogue
     GMS 266, 520, 1171, 1174                                         Hen. BSOAS 18.367 n3
                                                                3325 cy =* c'-, cymy6(5)
3314 exs'm     M       :j^)(jj^^      <^L~ <h jt <f)f±>- ^jjh
                                    
LEAF 196 head: 131
```


## [2026-09-06T22:10:36.712Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==269' SOD_pages.txt | head -50",
 "description": "SOD printed page 203"
}
```


### [2026-09-06T22:10:38.205Z] TOOL RESULT

```
                                                                                                              M*

     203


     5092 kym'nt B                                                   5105 kyr-2 B                                              -^T
          kimand (qymnt) =*k-                                             ker ©<Av. karaya =»qs-, kst-
          to the, to this                                                                                                  kysn*k

            EGSii 129; GMS     1404, 1490; VJ 947, C2 gloss.               GMS 540 n 1- BSTBL, Vim. 30, kyr\ 2sg. pres.
                                                                           (to)sow    '
                                                                             subj.; AVS 104
     5093 qymnt     C =» kym'nt
     5094 qymG* C                                      c^U<^l^j      5106 kyrMn     B =* kyr>n, kr»n
          resurrection
                                                                     5107 qyr"n      M =* kyr>n
I           C2, 55R25, 57V 10                                        5108 kyr'n
                                                                           Cf-U
                                                                           kiran
                                                                                    B, M, S         (j^^j^^^/
                                                                                    (kyr*n, kyr*nh, qyr>n) ©<Av. karan
    5095 kymyS       M                                         ^k
            kime8/G (qymyS) =»k-                                              =»nykr}n, *pw kyr'n, nymy5 kyr'n, }ws*y kyr'n,
            to this                                                          xwrtxyz, xwrsn qyr'n, pJsy kyr'n
                                                                           side, direction
           GMS    1485; C2 gloss.; BSTii 893.24, 32
                                                                           GMS 111, 244; VJ; TSP; SCE; BSTBL; BBB;
    5096 qymy6      C =* kymyS               I
                                                                              MDii; Frag. Lcn.; MSP bl46; W-Li, ii: Gropp.
    5097 qyn     C -> kyn(h)                                                  p40; C2 gloss.; Sund. AoFviii 1981, 28R8 pl99;
    5098 kyn'k     B                                          ^*              Hen. Cosm. 312.88; BSTBL, kyr>nw, Dhy. 285;
         kinak     <£><*akinaka\ GK aklnakes
                                                                              Vaj. 18; kyr'nK VJ 33b; JfcyrVz, Dhu. 58, 148,
         sword
                                                                              293; qr>nt C2, 94R6 n pi 67.6
           TSP 6.7 n p202; BSTBL, Vim. 136; Prolexis. 84
                                                                     5109 qy^n      M, C -> kyr'n
    5099 kynWwytk      M, S                      ^   j» ^ > «S uy*
                                                                     5110 kyr>nh =* kyr'n
         kcn-osuydc ~»kyn(h)
         free from hatcrd                                            5111 qyrm C *> kyrm-
                                                                     5112 kyrm- B, M, S                                         >
           Gersh. Sogd. Cpds. 148; Sogdica. 60.10
                                                                           kirm, kirm (qyrm) ©<Skt. krmi         ©nom. ob. -y;
    5100 kynpr B                                       j^j/oj^               inst. -J; ace. -w\ pi. qyrmyst
         kenPar
                                                                           snake, worm
           hating, vengeful                                                GMS 140, 512; TSP 2.1042, 1072, 1073, 1077,
           BSTBL, Padm. 36; GMS       1131
                                                                              3.83, 135, 247, 6.9; SCE 118, 233, 324; Frag.
```


## [2026-09-06T22:10:47.379Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"čašman\\|caSman\\|ča$man\\|casman\" BRT.txt | head -10; echo \"=== caxra ===\"; grep -n \"caxra\\|čaxra\\|ča%ra\" BRT.txt | head -10; echo \"=== vikaya ===\"; grep -n \"vīkaya\\|vikaya\\|vi&aya\" BRT.txt | head -10",
 "description": "Bartholomae greps"
}
```


### [2026-09-06T22:10:49.062Z] TOOL RESULT

```
10384:•  j.  garaSö-karata-  Adj.  'die  Galle  heraus- schneidend"':    kat    tä    tiara  yaozdayqn aiih>n  .  .  ya  rrasiuin  franuharat  sänS  i  "   ' para.iristahe  masyelu  väl  .  .  ayaozäayqn  ■ atihm  . .  lalJ'a  narS  'l^sca  (NPm.)  z^maö.- k?ntas^a  taica  tiarS  spiti.dsi'^ra  casmanal  * haca  itilbar>nti  "Sind  die  Männer  zu  pui fiziren,  die  .  .?  .  .  Sie  sind  nicht  zu  put fiziren,   und   (ebensowenig)   die  Männer, '
27055:134''.  2)  n.  '(das  helle  Auge  sva.) Augapfel':  taf'a  nan  ginlö.kfnLis{sA.)ca ..°ra  casmanat  haca  nübarinti  V. 7.24.
30258:yt  i  i'e  '  casmanS  Yt.  ij.  29.
=== caxra ===
2686:*zamarigusa    avazat   vXspe   daifa    Yt /<?.       AbleiV  aus  ■arr'OB.u'ajflZw. 'elf;  vgl.  tF,  S  ?/o 81 ;  —  yahmai  . .  aurvantö  . .  v3sa  '^an-  ■     aK  und  IF.  p.  245.  —  Pü. :  yHdahum. }aianie   °va   caxra  (sd.)    Yt  10.136;    —  •  j-    aeväkam    Adv.    'zugleich' (?):    aiv aim  .  .  yß  t0  °ve  säsnä   (sd.)  gäsatä    Y.   narqm  asaonqm  ahunvitim  ga^qm  frasrä- ^9.8;  YtJ7.i9,2i;    —  yö  nö  °v6  at  U  vay'nti  Vd. /2.
5485:•  j.,  g.  aradra-  Adj,  (fem.  'rJ-)  'getreu, 'verlässig':  'rS  '^wävqs(sd.)  ÄitzSntuü  sfmtö mazdä  Y. 4:_j.3;  46.^;  — fravasayB..  °rä taxmä  *at>javuAai/i/ \l.  ij.  $2;  75;  — mihrgm  . .  y5  äsunqtn  äsus  yS  'ranqm  °rö y3  taxmanqm  taxmS  Yt.  70. 65.  a)  mit DaL:  kuirä  tsi  °rä  masdä  ysi..  caxrayö' (sd.)  "ob  sie  wohl  dir  getreu  sind,  die  . ," Y._j4-7-  A)  insbes. 'dem  Glauben  treu, gläubig,  fromm':  firasaosträ  air3  tu  'r.lis idi  hvB^S  täis  yitig  . .  "o  Fr.Hv.,  dahin geh  mit  diesen  Frommen,  denen  . ."  Y. 4'j^i6;  —  kä  iw'ffi  a/a  äk,i  (sd.)  'ring isyl  Y.  4S.  8;  S*}.  4;  —  fatrijasai  .  .  at vä  aia  "rahyacä  mmankä  "..und  vor  euch, o  Asa,  auch  mit  dem  Gebet  des  Frommen" Y.50.8;  —  da^at  ahrnili  tat..  arfdvJ . . 'räi  yavmiini  jatoyantäi  da^ris  ayaphm Ytj.ig;  13a,  /5.1,  21.
5855:•  g.  'a-spä-  n.  'Unglück,  Leid':  ySt vanhSus  vaidinä  (sd.)  manatthiS  sSnghaS raSxma  °spsn^l  (AP.)"  sadräcU  caxrayS (sd.)  tuMro  Y.34.T,  — yJn7  usJn  (sd.) &r;>i  sp7nlä  'spJnla.  (AP.)"'  Y.^ij.g.
7279:charakterisirenden  Adj.  (sd.,  auch  fdSt.): vispasca  äpS  yazamaide  ya  z)m3  armaesta (sd.)  *fratat.ear3tasca  (sd.)  *xqnyk  '^raots.- stälasca  par^uya  *v3iryäsca  (sd.)  "alle Wasser  auf  der  Erde  . , :  die  stehenden  und fliessenden,  die  in  Quellen  und  in  Fluss- laufen,  die  Schnee-  und  Regenwasser"  Y. 61^.6;  usw.;  —  vJspä  apd  xä  pttiti '^raotS.- stSiasca  Y.yi.g;  —  sps yal  armal^tayä.. yat  cätayä  uzuityäsca  .  .  yat  sna^ntyaica srasUntyaica  . . yat ß^tat.^antayä'W .  6.^0, 33i  36,  39;  —  äpim*  tacintqm  . .  xayanqm .  .  zrayanqm  .  .  artmaistqm  Yt.6.2;  Y.ig. 26,  Vd.4;  —  caval  nä  apa  (statt  DS.) ''frälat.cartte  .  .  paiti.iaräi  .  .  cval .  .  ape armaisfaya  (statt  DSf.)  .  .  nävayayai  tia ape  ..  ti.66(.;  —  apqm  ..  nävayaiiqm (sd.)  paiti  pintüs  Yt  //.  4 ;  usw.;  —  andvim . .  ye^he  avavat  .  .  äps  lata  (sd.)  ava.- barmle ya%ia  ..  Yt.5.15;  Ä.47; — gairil yS  uiiiä  yim  aiwiid  paoiris  äpS  hqm  gairi- ü(/('(sd.)/(WJ«/JYL/9.66; — spim  laokmta' vaitim  zaranyävaitlm  vihusavaifim  (sd.) V.^.54;  —  ap3mca  haomyqm  {sA.)  Y.  22. 2;  usw.;  — yaSsyatitim  äp^m  *pararihät Y.g.ii;F.4 f.,  V.21;  —  ?iqm.taptibyB  aiwyS caxrare(sii.)  n^r^bydY.  4.46; — apU  ai yaza- maide malkaintllcä  (sd.)  * hsbavaintlicä  . . Y.JÄ3«.  C)  GP.  apqm  mit  napat-m. (sd.,  auch  fdSt.)  Name  einer  Gottheit: apqm  napäs?  tä  apff  ..  vliax/aiti  YtS. $4; usw.  2)  von  bestimmten  Flüssen  oder Seen,  'Gewässer':  andvl  (sd.)  nqrna  äpa (NS.)"'  V.  7. 16;  —  n?mS  artduya  aps  anü- hitaya  Yt  r.  2 1 ;  Y.  6$.  i ,  Ny.  4.  o.  Vr.  1. 5 ; —  *atikäs^a  (näml.  artduyä)  mS *aaatiAä aps  apayiarsY .  65.  i;  5;  —  upa  äp.'myqm vltaaukaittm  Yt5,76;  —  njinB  ape  däit- yayä  (sd.)  Yt./.2i;  5.112,  5,29,  /7.61, V, ig.2;  —  aoi  apjm  yqm  raiakqm  (sd.) Yt.5. 63;  —  haca  apat  kqsaeyät  (sd.)  Yt ig.92,  V.ig.$;  —  a/s  ya  aw^änva  nqma Yt  ig.  62;  —  yazäi  äp^m  frazdänaom  F. 4%.  I,  2  Anhang:  apqm  (näml  ayar^y
8730:tßi  aridrä  (sd.)  .  .  ysi  vanhSus  vazd>na (sd.)  manauhö . .  aspSncit  sildrJcU  caxray3 (sd.)  'S3ura  (IS.)  \.34.T,  —  hamSm  tat vahiitäat  y!  's'urvye(DS.)  syasclt  (sd.)  dah- mahyä  Y.  J2.  r6.
11131:•  j.  caxra'vant-  Adj.  (fem.  •vaia-)  'ein Rad  (als  Feldzeichen)  führend"':  hafnayä 'vailyh  Aog.Si.
11243:Z'um  V,  )ak-,  s.  ta/'ar-  und  BTHL.IF. /o.  3. — i>  Hds.  j''a"ftjw;  Tgl.  iiar-  No.  2  und  anya- No.  6;  femer  zu  lanal,caxra-.
18701:Aus  dem  Zusammenhang  gerissene,  un- deudiche,  verderbte  oder  wertlose  Stellen mit  nar-.  «flr/(GS.)  ..  nara  (ND.)  .. «(jr?(NP.)  F.  2e;  —  «3  Fsd;  — nanm ..sar>t)m  V.^.  14  PüZ'J»;  N.52"';  — panca  narB  V.  75.  loPüZ.;  Vyt.  42,  Vd 13,15;  —  dva  nar^FiB.; — para  "iafah- mät(sd.)  n»r>t  (AblS.)  V.  j.  42  PÜZ.;  — aBsqmia  naram  V.  5.  gPUZ.;  —  ham.- tapiibyB  aiwys  caxrart  (sd)  n^r^byB  V. 4. 4  7 ;  I  o  PiiZ. ;  —  tl  ^narsS paitismarmitm Vy^  52;  —  nöil  dim  "nara  . .  avasyil  Yt /.  aS;  — ya'ia  na  ttäifyaY.  20.  2;  Yyt  28, 30.  narSm  nartm  als  Adv.  sbes.  [N. 301  streiche  «a.J
20847:I  et  (eum)  qui  (est)  faciendi  et  dicendi" I  Y.  33. 14;  —  *grSkms . .  atikSus  maraxtärB I  (sd.)  ahya  \yai(a  ^'Grlhmas  . .  et  (ii)  qui (sunt) ..  destructores"  Y.J2. 13; —  ku%ra töi  andrS  (sd.)  .  .  yöi  .  ,  caxrays  "num tibi  (sunt)  fidi  (ü)  qui  . ,"  Y.^4.7;  — kada  .  .  yOi  uxiäiiS  ainqm  .  .  frärmtl "quando  . .  (ii)  qui  (sunt)  tauri  .  ."  Y.  4G. 3;  —  naldä  dahySus  \ydi  iastSrS  drjsvatas "neque  (ii)  qui  (sunt)  . .  imperatores"  Y. 4O.  I ;  —  tat  ..  uitanai  data  . .  ySi  sl gSus  v^nzinl  (sd.)  azyi  ".  .  vitae  (eorum) qui  .  ."  Y.  34.  14;  —  tim  at  yasna- nqm  paurvataia  yazamaidl  ySi  ..  iyeintJ ".  .  imprecationum  .  .  (eorum)  qui  .  ." ^•37-  2;  —  yi  varpsaiil  (sd.)  kyat vasnä  firasöJ^mim  "qui  . .  fecerit  . .  (id) quod  (est)  .  ."  "^.46.  19;  —  hyatcS dar>gSm  dr)gvll.d»byS  rasB  savai'a  alavabyö "et  (id)  quod  (est)  . .  damnum  et  lucra  . ." Y._jo.  11;  —  Aaihyavanitqm  {%A.)  hyat vasna  f?rasS.t}m}m  "verificationem  (eius) quod.."  Y. 50.11;  —  ai  zt  töi  vaxsya .. hyai  aksyä  (NSf.;  sd.)  dngvaiii  wörtlich ",.  von  dem,  was  die  Androhung  ist,,"  Y, 51.  8;  —  hyat  "qsasutä  (sd.)  yä  (NPn.) daiiiiana  (sd.)  fraoxta  "..  (ea)  quae  (sunt) . .  enuntiata"  Y.  48.  1 ;  —  das  Relativ  kon- gruirt  mit  dem  Praedikat:  vldvä  yalclt güzra  (sd.)  singhanhS  (wörtlich)  "kennend auch  (das),  was  die  geheimen  Lehren  (sind)" Y.4<V,3;  —  anais  a  vT.nSnasa  ya  (NSt) iarapsjis{ad.}cä  kjvltäscä  Y._J2.  15;  — *m>ndäiäyai  (sd.)  ya  (NSf)  toi  adisHi Y.44.8;  5,^.13;  —  nipatihw . .  tumas^a ya  armaitiH&d.)  Tiilcä  Y.4g.  10;  —  yS va  mSi  \yh  (NPf)  gasha  dasdi  (Sp. 7 1 S  u.)  *asnatihe  wörtlich  ". .  (das),  was meine  Besitztümer  (sind)  .  ."  Y,  46. 8;  — vtayUta  yä  (NPn.)  mrqi  sädra  drtgvats (wörtlich)  "immer  (wird  sein)  was  die Qualen  (sind)  .  ."   Y.45.  7;  43-5,  49-6;
22013:—  yesi  .  .  dim  nsit  tanu.ptn'Afm  *v^ar)  im  Besitz  des  wahren  heiligen  Wissens (sPPfA.)''  "wenn  sie  es  (von  ihm)  nicht ^  befindlich,  darin  eingeweiht"-^;  n)  von wissen,  dass  er  /,  ist"  ^.3$ ,3g, 38')  — \AhM.:  *yqm  mBi  vtdva  matda  vaocat at  vS  xsmaibyä  asBrtä  vasdä  x^arai'^yä '  a/iurS  "was  mir  der  wissende  MAk. (sd)  srava  Y.2Ä10.  a)  'etwas  (Akk.)  1  verkündet  hat"  Y.45-3;  —  vaocä  mH kennen  als  (das)  des  —  (praedik.  Gen.),  j^i?  (VJ'w  zTrfz'i  a^ars  "tu  mir  kund  — denn scire  rem  (esse,  fore)  ahcuius':  yehyäxda  ja  bist  der  wissende,  o  Ah.  —"  Y, tnHi  asät  hacä  vahist>m  yesnl paiti  vaidä  4IS.2.  ß)  sonst:  müahvacff  v3  *Pr7s,- mazda  ahurü  ySi  nnharsia  htnticä  "wen '  rairc  vä  vTävä  vä  >vfdva  {sd.)  vä  Y. von  denen,  die  waren  und  die  sind,  MAh. als  einen  solchen  kennt,  dem  durch  Asa mein  Bestes  fiir  sein  Gebet  zu  teil  vrird" '^.51.22;  —  ynihe  Aätqm  aat  yesm  paitt vaahs  mazdä  ahurö  vatha  asät  hacä  Y. 27.  15;  —  yaisqm  nS  ahur5  .  .  va^hs vaiha  "quorum  nostium  Ahuras  ..  melius (fore)  seit"  Yt.iÜ.s;—  *yat  nSil  vist»m drvats  "wovon  man  nicht  weiss,  ob  es einem  Ungläubigen  gehört"  N.  54**;  — ysi  vaahsul  vaEdtnä  (PPfM.)  mananhs .  ,  ralxsnh  .  .  caxrayS  (sd.)  ".  .  die  dem guten  Sinn  gewissen  Erbanteile  .  ."  Y. 34.  7.  3)  Perf.  Pass.  'bekannt  sein als  —    (Nom.),    etwas   (Nom.)    gewisslich
=== vikaya ===
```


## [2026-09-06T22:11:02.171Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"wāzār\\|w\\[āa\\]zār\\|wazar\" PHD.txt | head -5; echo \"=== kistan/kar ===\"; grep -n \"kištan\\|kāštan\\|kār-, \" PHD.txt | head -10; echo \"=== wizardan ===\"; grep -n \"wizārdan\\|wizār\" PHD.txt | head -5; echo \"=== carīdan/čar ===\"; grep -n \"čarīdan\\|čar-\\b\\|čarag\" PHD.txt | head -5",
 "description": "MacKenzie targeted greps"
}
```


### [2026-09-06T22:11:02.258Z] TOOL RESULT

```
649:waxšwar [whiwl | N waxtür] prophet. ~th: prophethood. P wāxtan, wāž- (w’hin', wc- | P wxtn, и?с-] say, speak. lway [wd = Av. way-] bird. *way [wd = Av. wayu- | P шуш] air, atmosphere. ~ í wattar: a demon. ~ i weh: a divinity. way [wd | M wy, N ~] woe. lway- [w*d- | M w’y-] fly. ~endag [-(y)ndk! | J w|B' ynd?] bird. wüyidan, *way- [w'd-ytn'] blow (of wind). wayodagàn [wydwtk’n! | M *wywdg'n, N bayēgān(ī)] nuptials, marriage feast. waz-, -išn(-īg), у. wazidan. waz [wc | = M, (N bāj)] word, speech; ‘grace’ (before meals). ~ griftan: say ‘grace’. 1, *wüz-, ~iSn, v. b *wāzīdan. P wāž-, v. wāxtan. wāzag [w’ck'] utterance, saying. wazay [wzy| N ~, bazay] frog. wāzār [w’c?l | M w?c'r-, N bázár] market. wāzāraģān [wlkn! | M wergn, N bázárgàán] merchant. ~ih: trade. wazidan, waz- [wc-ytn! P wz-, N ~] move, blow (of wind). ~išn: movement. ~i$nig : mobile. Iwāzīdan, wāz- [wc-ytn'] move, carry away; fly. ~išn: flight. *wazidan, w4z- [w'c-ytn! | N bāzīdan) play. wāzīģ [w'cyk! | N Бахт] game, play. wazr [wel] = *warz. wéd [wyt' | N bed] willow. weh [SPYL < А #руғ; wyh | M why, wyh, N bih] better, good. ~ih: goodness. «-dēn [-dyn' | N bih-din] of the good (Mazdean) religion. wēhm [*wyyhm | M wyhm] large, wide, broad. ~ih: width, breadth. wém [шут | = P] rock. wēmār [wyml | M wym’r, N bēmār] ill, sick. «Ih: illness. wén [wyn'] breath. wén-, ~i5n(-ig), v. didan. wēnāb [wyn’p | N binàb] vision. ~dag [-d’h', -t*k!] visible. wënäe [wyr?k! | M wyn!g, N bind] seeing. ~īh: seeing, sight.
2734:market wāzār,
2783:merchant wāzāragān.
4042:trade pēšag; wāzār(a)gānīh.
5254:naf, wiz 12waz-, wüz- wazar wāzāragānīh wāzāragān wāzīg
=== kistan/kar ===
424:kaman [kin’n' | = M, N ~] bow. 5; 7 ~dar [-d'] | N ~] archer, bowman. ha er mae 4 ba kamar [kml | N —] waist; belt, girdle. ~-band [-bnd | N ~] belt. kāmģār [Emil | P k?*mg?*r, N ~] powerful, absolute. kamist [Amyst'] least. —jh: pad ~ih, at least. kāmistan, kām- [YCBEN-stn' < A ysbh, V shh; k*m-(y)stnt M k*m-yst] want, desire. kám|-rawág [km izvb*k! | N ~rawa] successful. ~-Z1(w)isn [-zywsn'] free, independent. kam-zór [kmzwl | N ~] weak. ~ih: weakness. kan-, v. kandan, kanar [kwl | N ~] side, edge; embrace. ~ag [-k' | M kr?rg, N ~a] edge, limit, boundary. --agómand [-k’wmnd | M -gwmnd] limited, finite. kandan, kan- [HPLWN-tn! < А V hpr; kn-dn', -tn! | M knd, N ~] dig; raze, destroy. kanig [knyk! | M knyg] girl, maid. kanizag [knyck! | M knycg, N kaniz(ak)] — kanig. kantigr [kntgl] quiver. kāpūr [ро | Ar. kāfūr] camphor. kar-, v. kardan. 1Kar [21 | M Pr, N ~] work, deed, affair. ~ framüdan: put to use. 2kàr [%'7], pl. —àn: (other) people. зкаг [%'/] butter. kār-, v. kištan. karafs [klips | N ~] celery. kār-āgāh [РА | N ~] skilled, experienced. ~ih: skill, experience. karak [krk! | N ~] quail. karan [kľn' | P bein, N ~] side, edge, end, limit. kārawān [%?/zv?x! | P k*rw'n, N kārwān] caravan, military column. ~ig [-yk! | N ~7] caravaneer, traveller. karb [klp] priest hostile to Zoroaster. karbāš [5/0 | N karbas, etc.] lizard. karbunag [k/pnk!, klbnk'] lizard. kard [krt! | M kyrd, N ~] action; matter, affair. кага [SK YN A < A skyn’; Kit! | N ~] knife. ikardag [kltk!] division, section, portion. *kardag [krtk!, kltk! | N karda] action. kārdāg [k'/d?k'] traveller, wanderer, migrant. kardaģān [Art-, Rlt&?n! | M kyrdg”n) action. kardagàár [Artk?l | M kyrdg’r, № ~] mighty. C 6084 E
428:kem [kym] less, fewer; v. kam. кёп [kyn' | = M, N kīn(a)] hate, malice, revenge. ~ig [-yR'] malicious, vengeful. kennār [Rl] lyre, harp. ~-sray [-sPd] harpist. kénwar [kynwl | (M kynw’r), N kinawar] vengeful, vindictive. ««īh: vindictiveness. kër [kyl | N ~] penis. kēsar [kysl] Caesar. këš [kyš | = M, N ~] dogma, faith (especially non-Mazdean). ~-dar [-d’/] sectary, non-Mazdean. keSidan, keš- [k(y)$-ytn! | (M kr$-), N kafidan] pull, draw. Kēwān [kyw’n! | Ar. kaywān] astr. Saturn. kēwūd [kypwt! | M R'ywd] box, ark. kilēl [R]yl | N ktlīd)] key. kirb [klp | M kyrb] body, form. kirbag [krpk' | M kyrbg, N Аја] virtue, good deed. ~ig [-y%!] virtuous, pious. kirbakkar [krpkkl | M kyrbkr] beneficent. ~ih: beneficence. kirih- [OBYDWNyh-, v. kardan, kiyh- | M kyryh-] be done, made. kirm [kim | M krm, N —] worm, serpent. kirrénidan, kirrén- [klyn-ytn'] rend; create (daevic). kirróg [k(y)lwk! | M grwg] artisan, craftsman; skilled. ~th: arts, crafts, craftsmanship, skill. kiš [k(y)š | M АЎ, N ~] furrow, line. kišnīz [kšnyc] = gi$niz. kištan, kar- [ZL Y TWN-tn! < А У ar; kyštn!, Pl- | M kyšt, kis- N ~] till, furrow; sow. kištār [ZLY TW NTt'l] tillage. kišw, ~4n [kysw', x! | P Аун] tillage. ~(an)zar [-c?/ | (N kištzār)] field. ki$war [Rystol | M kyswr, N ~] region, clime, continent. kišwzār, v. kišwānzār. kūb-, v. koftan. kódak [kxwtk! | M gwdk, N ~] young, small; baby. kof [kwp | = M, N koh] hill, mountain; hump. ~ag [-4! | N Абла] saddle. ~ig [-yk! | N kēkī] wild, mountain-. koftan, kūb- [kwp-tn' | N ~] beat, pound, crush. kör [kwl | M kar, N ~] blind. ~-dil [-dyl | M -dyl, N ~] blind-hearted, incorrigible. kūstan [kwstn' | = M, N ~] beat, pound. kūš-, v. kóx&-. kēšk [how fA! | N ~] pavilion, palace, kiosk.
1930:fight (v.) éraxtan, nibardidan, pahi- kār-, P rān-; make ~ pahikaftan.
2065:furrow (v.) kištan.
3753:sow afšāndan, kištan,
5050:4915 | keš- AD $915 kēšdār 1$ 195 kešīdan w^ 1835513 kišwān Wis kišwānzār 14519 kišw 1.32514 kišwar = leo AA kišwzār WE ме 1 4 kištan us- kédigih vs kid ~114 nag, -ak "ua oh!
5074:zāy-! zāyišnīgi zāyišnī! zādan! 1-2zrëh zarrën | zargónih - zargon zarigomand zarig zarr(i)gar kàr-! kistárt kištant zalüg zraw- zarwan zruftan zarmānīh zarmān zardālūg zardīh zard Zardu(x)št
=== wizardan ===
382:*g5k4n [gwk’n'] details. Lc um ~ig [-yk'] detailed; precisely. (sassa tu) ģūmēz [gwmyc | N giméz] bull's urine (as ritual purifier). ģgūmēz- [gwmyc- | N giméz-] urinate. gön [gwa' | N gün] colour, complexion. ~ag [-k' | M geng, N güna] = gön ; sort, kind, form. gor [gwl | N ~] onager, wild ass. göspand [K YNA < А апу ? ; gwspnd | N ~] (small) cattle, sheep. ~-tihrag [-cyhlk'] holding the seed of cattle. ģūstān [gwst^n!] cattle-stall, cowshed. 1858 [gws | = M, N ~J ear. *GÓ68 [guš | N ~] cal. 14th day. tūšag [gwsk' | N ~a] corner. ģēošūsrūd [rwi^wslwt! = Av. gaošū.srūta-| acquired, learnt. 5051 [BSLYA < A bsr’; рой! | N ~] meat, flesh. ģūšwār [gwštw] | N ~] ear-ring. ģūw-, ~išn, v. ģuftan. gowag [swb k! | М gw'g, N goya] speaking, eloquent; speaker. *ģoūwizār [gwwc'[] explicit, in detail. göy [gwd | N ~] ball. göz [gwc | N ~] walnut. ~énag [gwzynk! | N gózina) a walnut sweetmeat. Gözihr [gwcyhl | Ar. jawzahr] astr. the Dragon. ~ dumb: the descending node of the moon. ~ sar: the ascending node of the moon. grab [22р | P grb] womb. grāmag [gľmk! | P gr’mg] possessions, wealth. grāmig [gľmyk! | M grmyg, N girāmī] treasured, dear. ~ih: affection, respect. 1$raw [giwb! | P grww] cane. *ģraw [glwb' | N giraw] pledge, security. ~ih, ~(a)g4n [glwk’n' | M grug*n, N giraugān] = *graw. grayidan, gray- [gl?d-yin' | P gry-, N gtráy-] lean, incline; intend, desire. ģriftan, gir- [OHDWN-tn' < A V?hd; glptn!, gyl- | M grypt, gyr-, N giriftan, ~] take, hold, restrain. «išnīģ : tangible. griftār [gipt?l | N gir~] held, taken; captive. ~Omand [-'wmnd) tangible. grih [glyh | N girth] knot. lgriw [CWLE < A swr-h; glyw'] neck, throat. ?0riw [CWLE, glyw' | M gryw] self, soul. sgriw [glyw! | P gryw, N girī(b)] a grain measure, modius, peck. griwag [glywk!' | N giriwa] hill, ridge. ģrīwbān [g/ywp?n! | N girībān] neck-guard, gorget. griyistan, griy- [BK YWN-stn'< A У bky; gld-stn! | M gryy-stn, N giristan, giry-] weep, cry.
655:wistardan, wistar- [wstl-tn! | N gustardan] spread. wistāx [wst??hw! | M wyst?h, N gustāx, bistāx] confident, bold. ~ih: confidence, boldness. wis [w(y)$ | M wyš, N gus] poison, venom, bile. wišād [SLYTWNt', Р! | M wid, N gušād] open, wide, loose. wišādan, *wišāy- [SLYTWN-tn! < A У šrh; wPtn! | M шурап, (wys?h-), N gušādan, gušāy-) open, loose, free. wišād-dar [.SL Y TWNt! BBA] hospitable. wišād-dwārišnīh [zP??! dzb?lšnyh) going about ‘open’, i.e. without kustīg, or šabīg. | wišān- [w®n- | = P] shake down. *wišāy-, v. wišādan. wiškar [zo£hl | N bisgar(d)] hunting-ground, wilderness. wiškīdan, wiškin(n)- [wfkytn!, wškn-] divide, separate. ~išn: separation. wiskofag [wskwpk' | N biškēfa] blossom. wiškuftan, wiSk6f- [vvškup-tn! | J guškuftn, gwškwß-] blossom; hatch. wišūb-, —išn(-īģ), v. wišuftan. wišoūmand [w%wmnd] poisonous, venomous. wišūdag [wiwtk' | (M ghwdg)] abortion, daevic creature. wišūdan [wswtn'] bear daevic offspring. wišuftan, wišūb- (zfwp-tn! | M wiwb-, N *gusuftan] disturb, destroy. ~isn: destruction. ~1&п16 : destructible. *wixSay- [whsd-} forgive, forbear. ~iSn(ih): forbearance. ~išnīg : forbearing. lwiyaban [20(у) р?п! | Р шуп, N bīābān] desert. *wiyābān [wyd’p’n'] astray, wandering; deluded. ~ih: delusion, deception. wiyaban|garih [wyd"Pnklyh] deception. ~ig [-vk'] wandering, itinerant. wiyāftan, *wiyüb- [wd ptn! | M wy’b-] open (the mouth). wiyan [wyd?n! | M wy’n, N giyān] tent. wiyiz- [wydwe-] loosen, undo. *wiyufs- [wdwps-] make merry. ~išn: merry-making. ~iìšnīg : merry. wizandag [wzndk'] quaking. wizandidan, wizand- [wznd-ytn'] tremble, quake. -išn: quaking. wizar [wc] | M wer] separation; explanation. wizārdan, wizār- [wel-tn' | M wyc'rd, wyc^r-, J bz?rd-, N guzardan] separate; explain, interpret; perform, fulfil, redeem. ~išn: decision; redemption.
656:wizārd-wars 93 xün
2059:fulfil wizārdan.
2980:oneirocritic xwamn-wizār.
=== carīdan/čar ===
1971:flock čarag, ram(ag).
3055:pasture čarag, wāstar.
```


## [2026-09-06T22:11:03.075Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AHD kwel ===\"; grep -n -i \"kwel-\\|kʷel\\|bazaar\" AHD_watkins1985.txt | head -20",
 "description": "Watkins AHD kwel / bazaar"
}
```


### [2026-09-06T22:11:03.129Z] TOOL RESULT

```
=== AHD kwel ===
1208:ABAFT apo- ABANDON bha-2 ABASE bassus ABASH bat- ABASIA gWa- ABATE battuere ABBREVIATE mregh-u- ABDICATE deik- ABDUCENS deuk- ABDUCT deuk- ABELE albho- ABERRATION ers-1 ABET bheid- ABEYANCE bat- ABHOR ghers- ABIDE bheidh- ABJECT yé- ABJURE yewes- ABLATION  tele- ABLAUT apo-, kleu-1 ABLE ghabh- ABLUTION leu(@)- ABNEGATE ne ABNORMAL gné- ABODE bheidh- ABOLISH al-3 ABORT er-! ABOUND wed-1 ABOUT ud- ABOVE upo ABRADE réd- ABRIDGE mregh-u- ABROGATE reg-1 ABROSIA gWere-4 ABRUPT reup- ABSCESS ked- ABSCISE kae-id- ABSCOND dhé-1 ABSENT eS- ABSOLUTE leu-1 ABSOLVE feu-1 ABSORB srebh- ABSTAIN ten- ABSTRACT tragh- ABSTRUSE treud- ABSURD swer-2 ABULIA gWele-1 ABUT bhau- ABYSS gWadh- ACANTHO- ak- ACANTHOPTERYGIAN pet- ACANTHUS ak- ACAPNIA kwép- ACCEDE ked- ACCELERATE kel-3 ACCENT kan- ACCEPT kap- ACCESS ked- ACCIDENT kad- ACCIPITER Oku- ACCLAIM kele-2 ACCLIVITY klel- ACCOLADE kwel-1 ACCOMMODATE med- ACCOMPLISH pele-1 ACCORD kerd-1 accosT kost- ACCOUNT peu- ACCRUE_ ker-3 ACCUMBENT keu-2 ACCUMULATE keue-2 ACCURATE cira ACERATE ak- ACERB ak- ACETABULUM ak- ACETIC ak- ACETUM = ak- ACHALASIA ghé-
1242:ANA- an! ANABAENA gWa- ANABAPTIST g¥ébh-1 ANABIOSIS gWei- ANACOLUTHON sem-! ANACRUSIS kreue-2 ANADEM dé- ANADIPLOSIS dwo- ANADROMOUS der-1 ANAGLYPH gleubh- ANAGOGE ag- ANALCIME = alek- ANALECTS leg-1 ANALEPTIC (s)lag¥- ANALOGOUS leg-! ANALYSIS leu-1 ANAMNESIS men-1 ANAPEST peu- ANAPHORA bher-? ANARTHROUS ar- ANASARCA twerk- ANASTOMOSIS ste-men- ANASTROPHE  streb(h)- ANATHEMA dhé-1 ANATOMY tem- ANCESTOR ked- ANCHOR ank- ANCHORITE ghé- ANCIENT! ant- ANCILLARY kWel-1 ANCON ank-
1295:BIB pd(i)- BIBLIOPOLE pel-5 BIBLIOTHECA dhé-1 BIBULOUS pd(i)- BICAMERAL kamer- BICEPS kaput BICORN ker-1 BICYCLE kwel-1
1324:BRIO gWere-2 BRIOCHE bhreg- BRISANCE bhréi- BRISTLE bhar- BRITTLE bhreu-1 BRONCHIECTASIS  ten- BRONCHO- gWere-4 BRONCHUS gWere-4 BRONTOSAUR bhrem-! BROOD bhreu-2 BROOK? bhriig- BROOM bhrem-2 BROTH bhreu-2 BROTHEL bhreu-' BROTHER bhrater- BROW bhri- BROWN bher-3 BROWSE bhreus-1 BRUIN bher-3 BRUISE bhreus-2 BRUMAL mregh-u- BRUNET bher-3 BRUT gWere-2 BRUTE gWere-2 BUBO beu-! BUCCAL beu-1 BUCEPHALUS gWou- BUCK! bhugo- BUCKAROO wak- BUCKBOARD beu-! BUCKLE! beu-! BUCKLE? beu-1 BUCKSHEE bhag-' BUCKWHEAT bhago- BUCOLIC gou-, kWel-1 BuppHA bheudh- BUDGET bhelgh- BUDGE! beu-1 BUGLE! gWou- BUGLOss gldgh- BUILD bheue- BULGE bhelgh- BULIMIA gWou-, leia- BULK! bhel-2 BULL! bhel-2 BULL? beu-1 BULLA beu-1 BULLATE beu-1 BULLET beu-! BULLETIN beu-1 BULLION beu-1 BULLY? beu-1 BULWARK bhel-2, werg- BUNCO bheg- BUND! bhendh- BUND? bhendh- BUNDESRAT ar- BUNDLE bhendh- BUNG peuk- BUNGLE bheg- BUPRESTID gWou- BUR! bhar- BURDEN! bher-1 BURG bhergh-2 BURGESS bhergh-2 BURGHER bhergh-2 BURGLAR bhergh-2 BURGOMASTER bhergh-2 BURIAL bhergh-! BURIN bher-2 BURN! gWher- BURN? bhreu-2 BURNET bher-3 BURNISH bher-3 BURSA bursa BURSAR bursa BURSE bursa BURST bhres- BURY bhergh-1 BUSHEL? bhau- BUSK! busk- BUSK? s(w)e-
1357:CHOLE- ghel-2 CHOLER ghel-2 CHOLERA ghel-2 CHOLESTEROL ster-1 CHOLINERGIC werg- CHOLLA g(e)u-lo- CHONDRO- ghrendh- CHONDROMALACIA mel-1 CHOOSE geus- CHORAGUS_§ ag-, gher-1 CHORAL gher-1 CHORALE gher-1 CHORD? ghere- -CHORE ghé- CHORIC gher-1 CHORION ghere- CHORISTER gher-! CHOROGRAPHY ghé- CHORUS gher-1 CHOWDER kele-1 CHRESARD gher-5 CHRESTOMATHY gher-5, mendh-1 CHRISM ghréi- Curist ghréi- CHRISTEN ghréi- CHRISTIAN ghréi- CuRIsTMas ghréi- CHROMA ghréu- CHROMATIC ghréu- CHROMATO- ghréu- -CHROME ghréu- CHROMIUM ghréu- CHROMO- ghréu- CHROMONEMA (s)né- CHRONAXY ag- CHRYSANTHEMUM § andh- CHTHONIC dhghem- CHUFA swei-! CHUKAR kau-! CHUKKER kwel-1 CHURCH keue-? CHURL karlaz CHUTE kad-
1382:COL kwel-1 COLANDER kagh- COLCANNON kaul-, weid- COLD gel-3
1383:COLE kaul- COLEOPTERA kel-2, pet- COLEOPTERAN kel-2 COLEOPTILE kel-2, pet- COLEORHIZA kel-2, wrad- COLESLAW kaul- COLEUS kel-2 COLLABORATE leb-1 COLLAGE koli- COLLAPSE leb-1 COLLAR kwel-1 COLLATE tele- COLLEAGUE leg-1 COLLECT! leg-1 COLLEGIALITY leg-! COLLET kwel-1 COLLIE g(e)u-lo- COLLIER g(e)u-lo- COLLIGATE leig-' COLLIGATIVE |leig-1 COLLO- koli- COLLODION koli- COLLOQUIUM tolkw- COLLOQUY tolkw- COLLUDE leid- COLLUVIUM leu(a)- COLOBOMA kel-1 COLON! | skel-3 COLONEL kel-6 COLONNADE kel-8 COLONY kWel-1 COLOPHON kel-6 COLOR kel-2 -COLoUS kWel-1 COLPITIS kwelp- COLPOSCOPE kwelp- COLPOSCOPY kwelp- COLTER skel-1 CoLuMBA kel-5 COLUMBARIUM kel-5 COLUMBINE kel-5 COLUMN kel-6 COLZA sé-1
1402:CUBE keu-2 CUBICLE keu-2 CUBIT keu-2 CUCKING STOOL kakka- CUD gWet-1 CUDGEL ku- CUESTA kost- CUIRASS sker-1 CUISINE pekw- CUISSE koksa CULET (s)keu- CULINARY pekw- CULLET kwel-1 CULLIS kagh- CULM! kolem- CULMINATE kel-6 CULOTTES (s)keu- CULT kWel-1 CULTIVATE kwel-1 CULTRATE skel-1 CULTURE kvel-1 CULVER kel-5 cum kom CUMMERBUND bhendh-, kamer- CUMULATE keue-2 CUMULUS keue-2 CUNCTATION konk- CUNNILINGUS leigh-, (s)keu- CUNNING gné- CUNT ku-
1406:cUsK ters- CUSPIDOR spyeu- CUSTOM s(w)e- CUTANEOUS (s)keu- CUTICLE (s)keu- CUTIN (s)keu- cuTIs (s)keu- cuTLass skel-1 CUTLET kost- CUTTLE ku- CYCLE kwel-1 CYCLO- kwel-1 CYCLOID kwel-1 CYCLONE kWel-1 CYCLOSIS kwel-1 CYGNET keuk- CYGNUS keuk- CYLINDER skel-3 CYMA keue-2 CYMBAL keu-2 CYMBIDIUM keu-2 CYNIC kwon- CYNOSURE kwon-, ors- CYPRIPEDIUM ped-1 CYPSELA keu-2 cysT kwes- CYSTO- kwes- -CYTE (s)keu- cyTo- (s)keu-
1416:DECEIVE kap- DECEMBER dekm DECEMVIR dekm, wi-ro- DECENARY dekm DECENNIUM at-, dekm DECENT dek-! DECI- dekm DECIDE kae-id- DECIDUOUS _ kad- DECIMAL dekm DECIMATE dekm DECK! (s)teg- DECK? (s)teg- DECKLE (s)teg- DECLAIM kele-2 DECLARE kele-2 DECLINE klei- DECLIVITY kKlei- DECOCT pekw- DECOLLATE! kWwel-1 DECOLLETE kwel-1 DECOR dek-! DECORATE dek-1 DECOROUS dek-1 DECORTICATE sker-1 DECOY keue-2, to- DECREASE ker-3 DECREE krei- DECREPIT ker-2 DECREPITATE ker-2 DECUMBENT keu-2 DECUPLE dekm, pel-3 DECURRENT kers-2 DECUSSATE dekm DEDANS en DEDICATE deik- DEDUCE deuk- DEDUCT deuk- DEED dhé-1
1456:ENAMEL mel-1 ENAMOR amma ENANTIOMER §ant- ENANTIOMORPH ant- ENARTHROSIS at- ENATE gene- ENCAUSTIC kéu- ENCEINTE? kenk-1 ENCEPHALO- ghebh-el- ENCHANT kan- ENCHASE kap- ENCHIRIDION ghesor- ENCLAVE kleu-3 ENCLITIC klei- ENCOUNTER kom ENCROACH ger-2 ENCYCLICAL kwel-1 ENCYCLOPEDIA pau- END ant- ENDEAVOR ghabh- ENDEMIC da- ENDERGONIC werg- ENDOCARDIUM kerd-1 ENDOCRINE krei- ENDOERGIC werg- ENDORSE dorsum ENDOSTEUM ost- ENDOTHECIUM dhé-1 ENDOTHELIUM dhé@(i)- ENDOW do- ENDUE deuk-, eu-1 ENDURE deru ENEMA yé-
1462:ENTELECHY kWel-1, segh-
1579:HAG2 kau-2 HAGGARD kagh- HAGGLE kau-2 HAGIO- yag- HAIL! kaghlo- HAIL? kailo- HAKE keg- HALBERD bhardha, kelp- HALE! kailo- HALE? kele-2 HALF skel-1 HALIBUT bhau- HALL kel-2 HALLOW kailo- HALO-  Sal-1 HALT! kel-3 HALT? kel-1 HALTER! kelp- HALTER? § sel-4 HAM konemo- HAMADRYAD deru, sem-! HAME_ tkei- HAMLET tkei- HAMMER ak- HANDIWORK kom HANDSEL sel-3 HANG konk- HANKER konk- HANUMAN genu-2 HAP kob- HAPLESS kob- HAPLOID pel-3, sem-1 HAPPEN kob- HAPPY kob- HARANGUE koro- HARBINGER koro- HARBOR koro- HARD kar-1 HARDS_ kes-! HARDY! = kar-1 HARE kas- HARM kormo- HARMONY ar- HARNESS _nes-1 HARPOON  serp-1 HARPSICHORD ghere- HARQUEBUS keg- HARRY koro- HART ker-1 HARTEBEEST ker-1 HARUSPEX ghere- HARVEST kerp- HASH! =skep- HASLET ghasto- HASTATE ghasto- HAT kadh- HATCHET skep- HATE kad- HATRED ar-, kad- HAUBERK kWel-1 HAUGH kel-2 HAUGHTY al-3 HAUL kele-2 HAULM kolem- HAUNT tkei- HAUSTELLUM aus-2 HAUSTORIUM aus-2 HAUTBOY al-3, busk- HAVE kap- HAVEN kap- HAW2 kagh- HAWK! kap- HAWKER keu-2 HAWSE kWel-1 HAWSER al-3 HAY kau-2 HAZEL koselo- HE! ko-
1679:INNATE gene- INNER en INNOCENT nek=! INNOCUOUS_nek-1 INNOVATE newo- INNUENDO neu-2 INOCULATE okw- INORDINATE ar- INOSCULATE 6s- INOSITOL wei-1 INOTROPIC wei- INQUILINE kWel-1
1788:MACERATE mag- MACHICOLATE kWel-1 MACHICOLATION kwel-1 MACHINE magh-1 MACHO mas
2039:PALEO- kwel-2 PALETTE pag- PALFREY pert, reidh-
2040:PALIMPSEST bhes-1, kwel-1 PALINDROME der-1, kwel-1
2041:PALINGENESIS kwel-1 PALINODE kvel-1 PALISADE pag- PALLID pel-2 PALL-MALL bhel-2, mele- PALLOR pel-2 PALM! pele-2 PALM? pele-2 PALOMINO pel-2 PALP pol- PALPABLE pol- PALPATE! pdl- PALPEBRAL pol- PALPITATE pdl- PALSGRAVE gravo- PALUDAL pele-!
2112:POINT peuk- POINT-DEVICE weidh- POINTILLISM peuk- POISE! (s)pen- POISON pO(i)- POKE’ beu-1 PoLack pele-2 POLE! kwel-1
2125:POST- apo- POSTBELLUM duellum POSTERIOR apo- POSTICHE apo- POSTMERIDIAN deiw- POST-MORTEM apo-, mer-2 POSTPARTUM _pere-1 POSTSCRIPT skribh- POSTULATE prek- POSTURE apo- POTABLE p0(i)- POTATION pd(i)- POTATORY pd(i)- POTENT poti- POTION po(i)- POTPOURRI pu-2 POUCH beu-! POULARD pau- POULTICE pel-1 POUNCE! peuk- POUNCE? (s)poi-mo- POUNCE3 peuk- POUND! (s)pen- POUNDS bend- POUSETTE pel-6 POUT beu-! POVERTY pau- POWDER pel-1 POWER poti- PRAAM per! PRACTICAL prak- PRACTICE prak- PRAEDIAL wadh-1 PRAEMUNIRE mei-3 PRAENOMEN no-men- PRAETOR ei-1 PRAGMATIC prak- PRAISE per-6 PRANDIAL ed- PRATINCOLE kwel-1 PRAXIS prak-
```


## [2026-09-06T22:11:16.600Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -o \"BAZAAR [a-zA-Zé*-]*\" AHD_watkins1985.txt | head; echo \"=== kwel-1 entry ===\"; grep -n \"^kWel-1\\|^kwel-1\\|kWel-1\\. To revolve\\|To revolve\" AHD_watkins1985.txt | head",
 "description": "AHD bazaar and kwel-1"
}
```


### [2026-09-06T22:11:16.658Z] TOOL RESULT

```
=== kwel-1 entry ===
650:kwed-. To sharpen. Germanic *hwatjan in Old English hweittan, to whet: WHET. [Pok. k¥ed- 636.] kwei-. To hiss, whistle. Imitative root. Germanic *hwi-n- and *hwis- in: a. Old English hwinan, to whine: WHINE; b. Old English Awisprian, to whisper: WHISPER; Cc. Old English hAwistlian, to whistle: WHISTLE. [Pok. 2. kuei- 628.] kvei-'. To pay, atone, compensate. Suffixed o-grade form *koi-néd in Greek poiné, fine, penalty, borrowed into Latin as poena, penalty: PAIN, PENAL, (PENALTY), PINE?, PUNISH; IMPUNITY, PENOLOGY, (PUNITORY), (REPINE), SUBPOENA. [Pok. k#ei-t- 636.] kwei-2. To pile up, build, make. O-grade form *koi- in: a. Sanskrit kayah, body: CHEETAH; b. suffixed form *koi-wo-, making, in denominative verb *k“oiw-eyo- in Greek poiein, to make, create: POEM, POESY, POET, POETIC, -POIESIS, -POIETIC; MYTHOPOEIC, ONOMATO- POEIA, PHARMACOPOEIA, PROSOPOPEIA. [Pok. 2. kyei- 637.] kweia-'. To value, honor. Suffixed zero-grade form *kvi-ma (< *kvia-md) in Greek timé, honor, worth: TImocrAcy. [In Pok. kvei-(t-) 636.] kweia-2. To rest, be quiet. I. Suffixed zero-grade variant form *k¥i-lo- (< *kvia-lo-). 1. Germanic *hwilé in: a. Old English Awil, while: WHILE; b. Old English hwilum, sometimes: WHILOM. 2. Possibly Latin tranguillus, tran- quil (trdns-, across, beyond; see tere@-2): TRANQUIL. IL. Variant form *kvyé- (< *kwyes-) in Latin quiés, quiet (> quiétus, calm, retiring), and in requiés, rest, and requiescere, to rest: COY, QUIET; ACQUIESCE, REQUIEM, REQUIESCAT. [Pok. k¥eis- 638.] kweit-. White; to shine. Suffixed form *kweit-o-. 1. Ger- manic *hwitaz in: a. Old English hwit, white: WHITE; b. Middle Dutch wijting, whiting: WHITING?; c. Old High German hwiz, wiz, white; EDELWEIss. 2. Germanic *hwaitjaz in Old English hwé&te, wheat (from the fine white flour it yields): WHEAT. [Pok. 3. kuei- 628.] kwek-. To appear, see, show. Variant form *kveg- in Slavic *kaz- in Russian ukazat’, to order: UKASE. [Pok. k#ek- 638.] kvel-1, To revolve, move around, sojourn, dwell. I. Basic form *kvel- in Latin colere, to till, cultivate, inhabit: COLONY, CULT, CULTIVATE, (CULTURE); INCULT, INQUI- LINE, SILVICOLOUS. II. Suffixed form *k¥el-es- in Greek telos, “completion of a cycle,” consummation, perfection, end, result (> teleos, perfect, complete): TELIC, TELIUM, TELO-; ENTELECHY, TALISMAN, (TELEOLOGY), TELEOST, TELEUTOSPORE. III. Suffixed reduplicated form *k/(e)- kvl-o-, circle. 1. Germanic *hwewlaz in Old English hwéol, hweogol, wheel: WHEEL. 2. Greek kuklos, circle, wheel: CYCLE, CYCLO-, CYCLOID, CYCLONE, CYCLOSIS; BICYCLE, ENCYCLICAL. 3. Sanskrit cakram, circle: CHUK- KER. IV. O-grade form *kvol-. 1. Suffixed form *k¥ol-so-, “that on which the head turns,” neck, in: a. Germanic *h(w)alsaz in (i) Old Norse hails, neck, ship’s bow: HAWSE (ii) Middle Dutch hals, neck: RINGHALS (iii) Germanic compound *h(w)als-berg-, “neck-protector,” gorget (*ber- gan, to protect; see bhergh-'), in Old French hauberc, hauberk: HAUBERK; b. Latin collum, neck: COL, COLLAR, COLLET, CULLET; ACCOLADE, DECOLLATE!, DECOLLETE, MACHICOLATE, (MACHICOLATION), TORTICOLLIS. 2. Suf- fixed form *kol-d in Latin -cola and incola, inhabitant (in-, in; see en): -COLOUS; PRATINCOLE. 3. Suffixed form *kvol-o- in: a. Latin anculus, “he who bustles about,” servant (an-, short for ambi-, around, about; see ambhi): ANCILLARY; b. Greek polos, axis of a sphere: POLE}, PULLEY; c. Greek -kolos, herdsman, in boukolos, cow- herd: BucoLic. 4. Suffixed zero-grade form *k»J-i- in Greek palin, again (< “revolving”): PALIMPSEST, PALIN- DROME, PALINGENESIS, PALINODE. [Pok. 1. k¥el- 639.] kvel-2, Far (in space and time). 1. Lengthened-grade form *kvél- in Greek téle, far off: TELE-. 2. Suffixed zero-grade form *k»l-ai in Greek palai, long ago: PALEO-. [Pok. 2. kuel- 640.]
```


## [2026-09-06T22:11:29.651Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf8',errors='replace').read()\npg=t.split('\\f')\nprint('leaves',len(pg))\nfor i in range(258,268):\n    s=pg[i]\n    print('---leaf',i,'---', s.strip()[:300].replace('\\n',' | '))\nEOF",
 "description": "BQT vol1 around p.52"
}
```


### [2026-09-06T22:11:31.268Z] TOOL RESULT

```
leaves 777
---leaf 258 --- شخصی دییگر - وبمعنی تحريك‌نمودن وبرشورانیدن | بجنگه هم هست که جربی اغراء گویند - وامر | باين معنی هم آمده است یمنی تحريك کن و | بشوران وناجاویده(۱) فروبردن رانیز گویندوبمبی | «بام» خوانند - و جابی باشد که در صحرا رکوه | بجهن. خوایدن کوسفندان‌وچارپابان دبگربکنند. | وخانهٌ زنبوررا نیز گفته‌اند - و بمعنی گرقتار کر
---leaf 259 --- "-هِ- | " ]غود ع بنم ات و سکون واو وزای | هوز. .. شیری باشد که از کوسفند نو زایده | کیرد ٩‏ . | ] وش - با واومجهول‌بروزن‌خاموش, | نیعنی بقل و بر باشد - و بمعنی پرستاروبنده‌هم | آمده است که در مقابل آزاد است ؟ .. | ۲ و شیدان - بمنی دریفل گرفتن‌ودر | بر کشیدن باشد . | ) غول - نم ثالث وسکون واومجپول | و لام » نگاه کردن و 
---leaf 260 --- گذارند . ۶ | ] قتاب‌ز درد دوه بکس بای ابجد . | کنابه ازخربزء )۱( شبرین باشد . | ]فتاب‌سر دبواد - کنابه از اتها | و وال عمر و زندگالی و دولت وکامرانی باشد . | ] فتاب‌سر وه - پممنی آقتاب سر | دبولر است که کنابه ازانتهای عمر وزوال‌زند کالی | ۲ قتاب‌سو ار کنانه از می دم سح رخیز | باشد . * | آ فتاب گر دش کنابه ازتمام روی | 
---leaf 261 --- ملکی باشد . * | [ سا فه - با سن‌بی فطه‌بروزن آستانه ؛ | اضانه وس گذشت راکوید . | ۲ فگا نه با اف فارس‌بروزن آیخانه. | شود و بسنی گوبند نان خورشی است د رکیلان | و آن چتان است که زرد* تخم‌عرغ را درشیرخام | بر‌بزند و نيك بر هم زند و بی بالای آتش نهند | تا شیر مانند دلمه بسته شود , بعد از آن شیرینی | با خشکه و پلاو در ع
---leaf 262 --- آقای ۱ هت | آقال ۱ - بر وزن پاماا , افکندنی | وکنابه ازآفتاب هم هست؛ کوبند این‌لفت ت کی | ویکار نیامدنی‌وسقط را کوبند . یت | ]قستقر ۴ . ۷ سین می‌نفطه و قاف بی ]. ]2 (۱) - بروزن چاك. بمعنی‌عیب وعار | وزن چارعنصر , مرغی باشدشکاری‌از جنس شاهین | باشد و آسیب و آفت‌را نیز کویند؟ - وبا کاف | و چر غویحری - ولف‌پادشا
---leaf 263 --- کپ هن اف ودک از | فارسی 9 کویند و آن کرداکرد اندرون | دهان است | قلاب را کویند عموما - و قلایی که بدان بخ در | بشدان|نداز ند و کشتیبانان کشتی دشمن‌را بان(۱) | بجانب‌خود کشند 9 ۴ سومیوه‌ایست‌سحرائی | / سک ‌ فتتالت ۳ حای ی نقطه. | جلاب را گویند و آن داروبی چندباشدجوشانیده | ‌ صاف کرده ششهم ۳ ۰ | ] کحج « بفتع‌ثاك وسکون 
---leaf 264 --- و بکرکاف فارسی محکم بتهراگویند ۱ . | ] گففت - بنتح کاف نک | وغای فرشت شت » ت» آزارورنج وهمجنت وت با ریز | و بکس‌کاف فارسی نیز همین معنی دارد ۴ | آ گن باکاف فارسی‌بروزن دأمن؛بمعنی | آکندنی باشد مثل آنچه درجامه و لحافوباش | کنند از پثبه و پشم وغیره - وبمعنی پر کننده | که فاعل پر کردن باشد , عم آعده است | کنج بفتح‌کاف
---leaf 265 --- و شین فرشت » بممنی در آوجخته باشد چه اندر | آکیشید پمنی الدر آوشت - و چنکه درچیزی | زده ودراز کردمرا نیز گویند.- وبمعنی دراز کردن | و درآوسنتن بجیزی هم هست 4 ۱ | آ گین عبروزن آبن؛ بمعنی مالامال‌ویر | و آغشته و آ کنده باشد وبمعنی فربه نیزآمده | اس تب که هض لاغرباشد ٩‏ . | آل ت‌ِ مسکون لام بروزن زال » سرخ | یمرنگ را 
---leaf 266 --- ۲ ۰ وا | آلان ِ پروزن‌بالان » ام ولایتی ونم | محله ایست ویسنی کوبند شهرست در ت رکستان | و نام کوهی‌هم هست1" . | لاو بسکون واو, آ تس شمله با را | کوند. و بفتح همزه‌هم درست‌است ۷ . | عندی ام درختی است که ازیخ‌آن دنگه سرخی | حاسل شودمانند رنگه رونای وبدان جامه رنگه | کنند و در دواها نیز بکار آید . | ! لا » پروزنکلا» | بمع
---leaf 267 --- کت ۱ آننک | و امٌال اینها باشد 0.٩‏ | ۲ لر - بروزن لاغر ۰ کقل و رین را | کوند مطلقا ۴ . | ۷ ۷ ۱ | بمعنی آلراست ک هکفل وسرین باشد مطلناً ۴ . | ] ل‌طمفا - برکون ثالت » مهرودگین | | یادشاهان را گوبنده ویضی کویند اين, لفث ترکی . | است ؟ . | ۲ لفده * - باغین قطمداربروزن آزرده, | بمعنی قهرآلود وخشمگین - وجنگه آورباشد . | ۲ لو
```


## [2026-09-06T22:11:42.068Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf8',errors='replace').read()\npg=t.split('\\f')\nimport re\nfor i in range(255,270):\n    if 'آگاه' in pg[i] or 'اگاه' in pg[i] or 'آ گاه' in pg[i]:\n        print('leaf',i)\n        for line in pg[i].split('\\n'):\n            if 'گاه' in line: print('   ',line.strip()[:200])\nEOF",
 "description": "Find آگاه in Borhan v1"
}
```


### [2026-09-06T22:11:43.785Z] TOOL RESULT

```
leaf 262
    آگاه - اوستا 25 - 2 بممنی مكّفت شدن. مشاهده کردن؛ سان‌کریت 125246
    « ظاهر شد * ؛ استی شرقی 0 < نگاء دن » , اهقه « چشم 0 » و نگاه در فارسی ازهمن
    تنبیه , آگاه‌کردن . خبر دادن : « ببامدم تاترا بیاگاهام. » تاریخ بیهقی « لفت نامه *.
    ۵ آگاهی - رف : آگاه . پهلوی "2261 « بب رکه ٩‏ » «مناي 6۲۹۵ < اونوالا
    حا کم سلطانیه و سردار سلطان حسین ابلخانی (۷۸4-۷۷۹) که گاهی عم اورا «آقا» بطور اطلاق
leaf 265
    ]له _ مخفف آگاه» رك : ۲گاه. آیاری - رك : آتش بهرام .
```


## [2026-09-06T22:11:54.105Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf8',errors='replace').read()\npg=t.split('\\f')\nprint('leaves',len(pg))\nimport re\ntargets={'چشم':None,'چرخ':None,'چریدن':None,'چلیدن':None,'چالاک':None,'بازار':None,'چاشت':None,'چشیدن':None,'زار':None,'گزاردن':None}\nfor i in range(60,110):\n    head=pg[i].strip()[:120].replace('\\n',' | ')\n    print(i, i+543, head)\nEOF",
 "description": "BQT vol2 leaves 60-110 headers"
}
```


### [2026-09-06T22:11:55.903Z] TOOL RESULT

```
leaves 684
60 603 ‫‪ ۵ ۲‬ات‬ |                                                                                                   ‫جومت‬ |  | ‫هو
61 604 ‫بیان نوز دهم‬ |               ‫جیم ابجد با های هوز مشتمل بر پانزده لغت و کنات‬                          ‫در‬ | ‫جود داز‬   
62 605 ‫‪=۹‬‬   ‫)‪¢‬‬ |  |  |  |  |  ‫و میم مفتوح برای بی‌نقطه و زای نقطه دارزده‪.‬‬      ‫»‬     ‫واف‬ |                                 
63 606 ‫بیان پیستم‬ |                ‫درجیم ابجد بابای حطی مشتمل برهجده (‪ )۱‬لغت‬ | ‫چیر ه د بر وزن زیره » روزباله باشد‪,‬‬       
64 607 ‫—‬         ‫=‬ |  |                                                                                      ‫جیغوت‬ | ‫وبعربی زی
65 608 ‫گفتار ششم‬ |  |      ‫تبجی‬            ‫رب‬ |                    ‫واف‬   ‫از کاب پرهان قاطع درحرف جیم فار‬ |                   
66 609 ‫‪ ۵‬ات‬   ‫مت‬ |                                                                                                         
67 610 ‫چار تاره‬                                                                                 ‫—‬        ‫س‬ |  |  |  |  |  ‫چار باال
68 611 ‫سس‬                                                                                             ‫چار تکبیرزدن‬ |  | ‫چار دی
69 612 ‫چاره‬                                                                                                                  
70 613 ‫=“‬                                                                                                        ‫چاريك‬ | ‫مخف
71 614 ‫ال‬                                         ‫‪۱‬‬ |  ‫چکانیدن؟ = بالون‌بروزنآشایدن»‬ |                                ‫بمعن
72 615 ‫‪۱‬‬       ‫=‪£‬‬                                                                                      ‫جالاك‬ |         
73 616 ‫چلمیدن‬                                                                               ‫—‬   ‫سے‬‫س‬ |                    
74 617 ‫‪۱‬‬                                                                                           ‫چامن‬ |  |  |  | ‫‌ای بود هربع 
75 618 ‫چاه‬                                                                                                ‫سلا‬ |              
76 619 ‫‏‪ ٩‬مس‬                                                                                                            ‫چا
77 620 ‫بیان دوم‬ |  |                 ‫ایرمسی با بای ابجد مشتمل برشش لغت‬ |                                                 ‫دفر ج‬ | 
78 621 ‫بیان سوم‬ |              ‫ونات‬ |                 ‫در جیم فارسی با بای فارسی مشتمل بر بیست و دو لغت ک‬ |  ‫چپا نی ‪ = ۴‬بروژن
79 622 ‫یه‬                                                                                     ‫‪14‬‬ |  |  | ‫با کسی خود را یکی‬   
80 623 ‫‪YY‬‬                                                                                             ‫چیدن‪‎‬‬ |  | ‫وثالی مشد
81 624 ‫ليان پنحم‬ |                   ‫درجیم فارسی باجم فارسی‌مشتمل برچهار لغت‬ |  | ‫چچله ‪-‬بناول و ان وی ق لحم ‪.‬‬              
82 625 ‫بیان ششم‬ |                    ‫دز جم فارسی با خای نقطه دارهشتمل بردوازده لغت‬ |  |                              ‫‪.‬‬   ‫زلف
83 626 ‫چنده‬                                                                                            ‫‪۷‬‬    ‫ی‬ |  |  | ‫کسی جس
84 627 ‫بیان هشتم‬ |            ‫جیم فارسی با رایقرشت مشتمل بر نود لغت و کنایت‬                            ‫در‬ |  |                 
85 628 ‫چراغله‬                                                                                                         ‫‪۲۷‬‬ | 
86 629 ‫یروت‬                                                                                                  ‫چراغ منان‬ |     
87 630 ‫‪۷6‬‬ |     ‫جرج‬                          ‫‏‪e‬‬                                          ‫‪.‬‬       ‫س‬    ‫ل‬       ‫
88 631 ‫هزات‬                                                                                    ‫چرخ انداز‬ |  |      ‫چرخ دولا یی
89 632 ‫رده‬                                                                                                           ‫‪- ۳۱‬‬
90 633 ‫‪۳‬‬                                                                                                   ‫چرز‬ |  | ‫چرس ه بر
91 634 ‫چرمدان‬ | ‫وغیره ‪ -‬وبسکون‌ثالی» نام مرغی‌است که خودرا‬ |                                                        ‫وفرایی ب
92 635 ‫‪6۳‬‬                                                                                            ‫چرم شیر‬ |  | ‫جر نداب = 
93 636 ‫م‪۳‬‬ |  |  | ‫و ازحېرقه‬       ‫دیه‬ |                   ‫یمعن‬ |                      ‫سیب‬ |                        ‫وترک‬ |      
94 637 ‫بیان نهم‬ |                   ‫در جیم فارسی با زای هوز مشتمل برشش لغت‬ | ‫جز ده = بفتح‌اول وثالك وسکون‌نانی »‬             
95 638 ‫شع‬ |       ‫چز‬ |  |  ‫وبضْم اول شیردان کوسفند و بز و امثال آن را‬       ‫ولوعی ابزای افزار باشدکه رویآ درا ازرسمان‬ |  |  | ‫چسنگ
96 639 ‫سرب‬                                                                                       ‫‪۳۳‬‬ |  | ‫حت آلت‬    ‫یًابر‬ 
97 640 ‫چشم وره‬ |  |  | ‫چشم بندكگ ‪ -‬بازبیباحھ » وآن‌چنان‬                            ‫ر وزن عزراگل »‬           ‫جشم اغیل ‪۹‬‬ | ‫ا
98 641 ‫اه ات‬                                                                         ‫چم را آي دادن‬ | ‫وتاره‬ |     ‫س‬     ‫شب 
99 642 ‫چشمة صیماب ریز‬                                                                                         ‫=‪~۹ £‬‬ |  | ‫چشم
100 643 ‫‪4 -‬‬                                                                                  ‫‪ -‬چهمة قر کون‬ | ‫از‬      ‫کت
101 644 ‫ماو پوت‬ |  | ‫است ‪ -‬و چوبی شبیه بمشتةٌ حلاجی که بکسر‬ | ‫درآن تعبیه کنند‬               ‫جدل‬ |                             
102 645 ‫‪"6 )--‬‬ |  |         ‫ورسیدن = وپس سر نگرستن‬ |                              ‫ویم ت‬                  ‫را کوبند ؛ و چم اول 
103 646 ‫]‪1‬‬    ‫ی‬ |  |  | ‫مطهره خوانند ‪ -‬و ضم اول و فتح انی سلاحی‬                 ‫و بمعنی باله وزاری همآمده استب‬        ‫است
104 647 ‫‪eA‬‬ | ‫و مخفف چغوك همهت که گنجشك‬                            ‫ودامبارك ‪-‬‬        ‫جفندر ‪ ۱‬یسم اول وثانی‌ورایع‌وسکون
105 648 ‫بیان سیز دهم‬ |  |                      ‫در جیم فارسی با فامشتمل بر هشت لغت‬ |  |      ‫ب‬ |      ‫جسه‬‫وار‬ |           ‫گهفمته‌ان
106 649 ‫بیان چهار دهم‬ |  |  | ‫بمعنی چفاچاق است که صدا وآوازپیاپی خوردن‬           ‫جتح اول و سکون ثالی » چر ی‬        ‫چق د‬ |  |      
107 650 ‫]‪0‬‬ |  | ‫لب ازچهارجااب بجول باد که آنرا‬ |                              ‫جلابك‬ |                                  ‫او‬     
108 651 ‫رد ات‬                                                                                          ‫جاده‬ |  |  |  |  | ‫چکاو د بتح 
109 652 ‫س‬ |                                                                                                       ‫ساي‬ |  |  | ‫چگره
```


## [2026-09-06T22:12:07.592Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf8',errors='replace').read()\npg=t.split('\\f')\nimport re\ndef show(i,keys):\n    print('=== leaf',i,'printed',i+543,'===')\n    for line in pg[i].split('\\n'):\n        l=line.strip()\n        if any(k in l for k in keys):\n            print('  ',l[:250])\nfor i in [85,86,87,88,89]:\n    show(i,['چرخ','اوستا','پهلوی','سانسکریت'])\nprint()\nfor i in [95,96,97]:\n    show(i,['چشم','اوستا','پهلوی','سانسکریت'])\nEOF",
 "description": "BQT charx and cheshm footnotes"
}
```


### [2026-09-06T22:12:09.305Z] TOOL RESULT

```
=== leaf 85 printed 628 ===
=== leaf 86 printed 629 ===
   ‫‪۸۱۱٩‬‏ = چربش (مضم باء) «اسفاا ‪ ۲ :‬ص ‪ ۸۲‬پهلوی‬                                  ‫ه‪.‬ش‬ ‫دتی‬
=== leaf 87 printed 630 ===
   ‫(سبت)» پهلوی ‪.»12 ۲10‬‬                 ‫‪ - ۲‬از چرب ی‬                                      ‫‪.‬‬     ‫ركب‪:‬ك‬
   ‫‪۲ :‬ص ‪۳6‬‬      ‫‪ -‬پپلوی ‪)۲4C‬‏ ‪ ,‬اوستا ‪ » 27526-‬هندی باستان ‪ « 8۲6۵ -‬اسفا ‪۱‬‬
   ‫«لغت‌فری ‪۲۸*۰‬‬                ‫زهر کوده کشته بسر‌برش‌چرخ ‪.‬‬                                ‫جهاندبده‌ای دبدم ازشهی بلخ‬
=== leaf 88 printed 631 ===
   ‫هزات‬                                                                                    ‫چرخ انداز‬
   ‫چرخ دولا یی۔ کنابه از آسان‬                     ‫باشد (‪ )۱‬و‪-‬ییراهن را گنفزته‌اند ‪۱٩‬‏ وکمان‬
   ‫چرخ ريسك د جانورست‌بیه بملخ‬                         ‫وطاق ابوان وطاق درگاءسلاطین وغیرم وجابی‬
   ‫و ببوسته فرباد مبکند خصوصا شبپا‬          ‫مبیاشد‬     ‫بررآید ‪ ,‬وبعربی معصر خوانند ‪ -۴‬وچرخی که‬
   ‫کرددن‪ -‬وچرخ‌زدن دروشان درهنگام سماع ‪-‬‬
   ‫و چرخ دولاب ‪ -‬و چرخ عصاری ‪ -‬وکردیدن‬
   ‫چرخ زرین کاسه ‪ -‬کنابه فالزك‬                     ‫ومان‬
   ‫چرخ ابربشم‌تابی وهرچیز که چرخ زد ک‬
   ‫» کنابه از رقاس ‪ -‬ومردم‬   ‫رن‬    ‫چرخ‬             ‫است که بدان تبر اندازند ‪ -‬و نام برنده‌است‬
   ‫چرخشت ‪ ۲‬باشیننقطه دار ‪ ۰‬بر‬                                                    ‫اول باشد که فلك قمراست‬
   ‫‪ - ۱‬نیز پابه های مدور و متحراك‬                 ‫رك ‪ :‬چرخه ‪.‬‬          ‫‪۲‬‬
   ‫‪ - ۷‬چرچ ريسك آبی‬                          ‫‪.‬‬   ‫گونند‬   ‫را دز‬   ‫دوچرخه‬
   ‫چرخ‬                    ‫‪۰‬‏ ‪« ater 10028‬جفرافیای اقتصادی ‪ .‬کپان ص ‪ ۶۳‬بنقل‬
   ‫شکل غلط کلمة چرخشت‬       ‫‪۹‬‬
   ‫باکلمة پپلوی‬   ‫و شاید چرخشت‬     ‫‪thswxrc‬‏‬       ‫مفدی‬          ‫‪=°‬‬              ‫(ه‪.‬م‪. ).‬‬
   ‫(‪ )1501172:‬خواند بمعذی‌چرخشت‬                 ‫که بقول تب رکه‌میتوان آلر| ‪5‬‬
=== leaf 89 printed 632 ===
   ‫وآنچه زان بدان ریسمان رسند ‪۷‬‬                          ‫وزن ومعنی‌چرخست باشد وآن چرخی وحوضی‬
   ‫چرخ صوقفی جامه ک‪-‬نابه از‬
   ‫والث سحتالی رسیده » هرچیز که چرخ زننده‬
   ‫باشد مانند کبوتر چرخي واه‌ثال آن ‪ -‬وجنی از‬                                     ‫فلك اول باشد که فلك قمر است ‪.‬‬
   ‫چرخ کرده باشند ‪ -‬و ادبخانه و صتراح را نیز‬                                                                            ‫خوانند؟‬
   ‫چرخ مقو س ‪ -‬کنابه ازفلك است‬
   ‫ثانی » بمعنی چرخله است » وان رستنی ولباتی‬
   ‫چرخه‪.‬‬   ‫‪ ۳۳ ۴‬رکه ‪:‬‬               ‫‪ ۴‬کندناگون ( برتك گندنا ) بعنی سبز رنك ‪ .‬رك ‪:‬گندناگون ‪.‬‬
   ‫_ آنرا « کردنا»(«‪.‬م‪ ).‬نیز گوبند ‪ ۵ .‬رکه‪ :‬چرخله ‪ - ۷.‬ازدساتیر «فرهنك دسانیر ‪.» ۲۶۲‬‬
   ‫ریلکی ‪ 3۸۲30‬قرقره(نخ ») ودر نبریز‪4۲۵۵٥‬‏ ( چرخ دوك‬
   ‫‪_ ۸‬ا‬                       ‫رسی) را گویند ‪ .‬رك ‪ :‬چرخ‪.‬‬
   ‫_‪(Henning, Sogdian loan - words, BSOS.X.1.96‬‬                                         ‫وچرخست شکلغلط کمه‌است‬
   ‫‪:‬‬       ‫رك ‪ ,‬چرخ ‪٠‬‏ چرخت‬

=== leaf 95 printed 638 ===
   ‫چشم است که بعریی عین خوانند ‪ - ۴‬وم اول‬
   ‫چشته » بفتح اول بر وزن کشته ‪. ۷‬‬                  ‫سباه و لغز نده که آنرا در دارو های چشم بکار‬
   ‫در داروهای چشم بکار برند ‪. ۸‬‬       ‫و شاهد نباورده بودند»‬   ‫بودند‬    ‫نقطه دار لوشته‬
   ‫‪« :‬صاحب‬                 ‫‪ ۴‬را ‪ :‬چشم » چدشخرام‬
   ‫›ك‪ :‬چشم ‪.‬‬
   ‫چاشت‪ .‬هب رکه‪ :‬چشم‪ .‬چشام‪.‬‬    ‫وچشته خور» کسی‌را کوبند که معتاد باستفاده ازدیگری باشد‪ .‬ورك‬
=== leaf 96 printed 639 ===
   ‫وزن سرشخ › مخفف چشم زخم‪ .‬است ‪٩‬‏ آ‬
   ‫چشم آب دادن = کتانه از تماشا‬                        ‫چشفر ‪ -‬بافابروزن ششدر» بمعنی‌چشیر‬
   ‫چشم | رو ‪-‬رباای قرشت (‪ )۱‬وواو‬                                              ‫‪۶‬‬          ‫باشد خصوماً ‪۰ ۲‬‬
   ‫مجهول بروزن شفتالو چیزی کهبجهت دفع‌چشم‬               ‫حثاث = بکراول وسکون‌نانی وکاف؛‬
   ‫زخم رچشم بت سار ند اعم ازا نکه برایآدمی با‬          ‫بمعئی اقرون وغالب و زبادتی و افزونی وعالب‬
   ‫‪ -‬باغین قطمدار بروزن‬       ‫چشم !غل‬                                            ‫عرب عکیونبند ‪- ۴‬‬
   ‫دربا دل » از گوشةٌ چشم نگاه کردن باشد اعماز‬                                ‫ودانسیاهی‌باشد لغزنده‬
   ‫چشم بکار برند وچون‬
   ‫بگوشة چشم نگاه کردن باشد ‪.‬‬         ‫باين ‪ -۳‬حدقه (مردمك)‬
   ‫رك ‪ :‬چشیر ‪.‬‬     ‫‪۴‬‬                         ‫چشم زخم ‪.‬‬       ‫رك ‪:‬‬     ‫‪- ۱‬‬
   ‫=‪0‬تاکه»‪ .‬اوستان‪hsac ]2۳‬‏ «اسفا‪:۱‬‬
   ‫‪-‬یم مومن درتحفه ذیل ت«شميزج » آرد ‪ « :‬معرب از چشمیزاك فارسی امت‬
   ‫واورا چشمك وچشم نامند‪ .‬دانه‌است بقدر بهدانه مثلث و سیاه و براق ‪ ۰»...‬و ذیل چ«شمیزج »‬
   ‫و «چشمك» و «چشوم» گوید‪:‬ه تشمیزج است»؛ رك ‪ :‬چشام و تشمیز وممرب آن «ششم» بکسر اول‬
   ‫® ‪ -‬نیز سفیدی میان سرفاوقاف وواو راگویند ‪ « :‬وچشمپای واو وقاف‬                      ‫است «تفس؟‪.‬‬
   ‫‪« -‬چشمآ لوی‌نگرستن‬                 ‫‪ _ ۱‬مخفف« چشمآغیل» («‪.‬م‪ ).‬ورك‪ :‬چشمآغلیدن‪.‬‬
   ‫بيك کوشة چشم بودو چشماغل نیزکوبند ‪ « ».‬لفت فرس‪۹٩۹۱‬‏ ح ‪». 4‬‏ ‪ - 4‬باین معنی‌اسم‬
   ‫‪۱‬‬       ‫از ‪ .‬چشم آغل ‪ +‬بدن (مصدری)‪.‬‬          ‫‪٩‬‏‬               ‫فلعل است باحذف «نده» ازآخر ‪.‬‬
=== leaf 97 printed 640 ===
   ‫چشم وره‬
   ‫چشم بندكگ ‪ -‬بازبیباحھ » وآن‌چنان‬                            ‫ر وزن عزراگل »‬           ‫جشم اغیل ‪۹‬‬
   ‫است که چشم یکی ازطفلان را متعنه ودبگران‬                     ‫بقهروغضب بگوشة چشم مگ کردن باشد ‪- ۴‬‬
   ‫پنهان شود و بد از آن چشم لورا بنگعایند ا‬                                   ‫‪.‬‬   ‫‪۳‬‬     ‫ونگاه کننده را دز کوینه‬
   ‫شده راییندند ربافی اطفال پنهان شوت » وی‬                    ‫بمعنی چشم آغیل است که عضب و قهر بكوشة‬
   ‫ابن بازیرا سرمامك یزخواندد که آعم بازیی‬                     ‫چشم دگاهکردن باشد ‪ ۴‬وبخضب نکاهکننددرا‬
   ‫چشم آ و یزد بوااو بروزن رستلخیز»‬
   ‫چشم لیآ ب ‪-‬کنامه لزمیحیا وی‌شرم‬
   ‫مافتد وزیان‌آن رامانندقاب ازیش چشم آویز فد‬
   ‫چشم پیش ‪-‬کنابه ازشرمنده وخصل‬                               ‫و چیزی هم حت ازپوست که نراترمشه ترمشه‬
   ‫باشد ‪.‬‬       ‫کنند و بجهت دفع مگس از پیش چشم اسپ‬
   ‫آببچجهپت چشم زخم از مردمکیو ۔‬                      ‫چشم بر اه ذاشتی‪ -‬کنایه از انتظار‬
   ‫چشم خروس د=اممای‌باشد سرخ‬                                                                     ‫کشدن باشد ‪.‬‬
   ‫چشم‌خروسای‪ -‬کنابه از شراب‬                                   ‫جشم ينام * = بانون بروزن‌عرش‌پیام‪.‬‬
   ‫ویذی باشد که بجهت دفع چشم زخم‬
   ‫چشم در یفده د کنابه ازبی شرم‬                               ‫نوسند ‪ .‬چهپنام اعمالی باشد که بجهت دفع‬
   ‫وبی‌حیاباشد‪۷‬‬                                        ‫چشم زخم کنند ‪.۷‬‬
   ‫‪ -۱‬رك ‪ :‬چشم آغل وچشم آغلیدن ‪.‬‬
   ‫بال فرح شبها امیر ررز غدیس ‪.‬‬                ‫‪ - ۴‬کیوس‌وارنگرد(بگیرد)همی‌بچشم آ لوی‬
   ‫مسن برهان صحیح است ‪ .‬رك‪ :‬مثلم‪. ‎‬‬            ‫درلغت فری (س‪«)۰4۳‬چشم منام»ضبط شفه»‬                  ‫‪e‬‬
   ‫"چرا نداری با خود همیشه چشم پنام ‪٩‬‏‬                  ‫‪ - ۱‬با نگارا ازچشم‪ .‬بد بتری ومکن‬
   ‫‪.‬‬     ‫نگاه سارد‬   ‫أدب‬    ‫دریده‬   ‫چشم‬               ‫‪ - ۷‬شوخیار کسنکرکتهوپیبششکفت‬
```


## [2026-09-06T22:12:41.906Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf8',errors='replace').read()\npg=t.split('\\f')\nimport re\nfor w in ['چریدن','چلیدن','چالاک','چالش','چاشت','چشیدن','چاشنی','چشایی']:\n    hits=[]\n    for i,p in enumerate(pg):\n        if w in p: hits.append((i,i+543))\n    print(w, hits[:12])\nEOF",
 "description": "Locate Persian headwords in BQT v2"
}
```


### [2026-09-06T22:12:43.691Z] TOOL RESULT

```
چریدن [(84, 627), (424, 967)]
چلیدن []
چالاک [(65, 608), (72, 615)]
چالش [(12, 555), (73, 616)]
چاشت [(70, 613), (95, 638), (275, 818), (649, 1192), (661, 1204)]
چشیدن [(82, 625), (83, 626), (101, 644)]
چاشنی [(38, 581), (70, 613), (101, 644), (242, 785), (536, 1079)]
چشایی []
```


## [2026-09-06T22:13:06.604Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf8',errors='replace').read()\npg=t.split('\\f')\nfor i,p in enumerate(pg[:120]):\n    for line in p.split('\\n'):\n        if 'چرید' in line or 'چريد' in line or 'چرا ' in line and 'اوستا' in line:\n            print(i,i+543,'|',line.strip()[:220])\nEOF",
 "description": "Find čarīdan in BQT v2"
}
```


### [2026-09-06T22:13:08.347Z] TOOL RESULT

```
84 627 | ‫چریدن‌باشد؟ ‪ -‬وبکر ارل‌یمعنی ازیرای‌چه؟ ‪.‬‬
```


## [2026-09-06T22:13:20.803Z] TOOL CALL #51: Bash

```json
{
 "command": "sed -n '1,40p' tools/ref_page.py",
 "description": "Inspect ref_page tool"
}
```


### [2026-09-06T22:13:20.842Z] TOOL RESULT

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


## [2026-09-06T22:13:23.781Z] TOOL CALL #52: Bash

```json
{
 "command": "timeout 300 python3 tools/ref_page.py BQT:639 --image 2>&1 | head -60",
 "description": "Render BQT page 639"
}
```


### [2026-09-06T22:13:25.273Z] TOOL RESULT

```
no scan of BQT covers printed page 639 (see 'scans' in refs_online.json)
```


## [2026-09-06T22:13:31.822Z] TOOL CALL #53: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:1567 2>&1 | head -50",
 "description": "BQT page 1567"
}
```


### [2026-09-06T22:13:39.322Z] TOOL RESULT

```
REF: BQT:1567  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 360  OCR-lang: fas

-۱۵۹۷- کاشمر
نی ز کویند ‎٩‏ دادکر » نم شهری است از ترکستان منسوب
کاشت » بر وزن چاشت » ماضی کاشتن بخوبان وخوش صورتان ‎٩‏ (۱).
است که زراعت کردن باشد - وماضی‌ب رگردانیدن کاشکی ۲ - با کاف بتحتانی رسیده »
هم هست بعنی بر گردانید - و بمعنی روی بر كلِمهٌ تمنی است که آرزو باشد - و بمعنی تأسف
کردانید هم بنظرآمده است که ماضی روی بر وافوی وحرت هم آمده است۸ ۰
گردانیدن باشد ۴ . کاشم * - بروزن هاثم » دوابی است .
کاشتن ۴ - بروزن داغتن ,بسعنی‌زرامت | وآن نوعی از انگدان باشد و آنرا انجدان‌رومی
کردن - و برگشتن - و بر کردانیدن باشد ۴ ۱ کویند . ضیق‌النفس را نافع‌است ؛ وبعض ی گوبند
- وکنایه از نومید شدن هم هست چنانکه کسی کاشم تخم انجدان رومی است. گرم وخشك است
چیزی طلبد و نخواهند که بدو دهاد کوبند در دویم وسیم .
« کاشته‌اند > . گاشمر « با میم بر وزن کاشفر » نام
کاشغر < باغین نقطه دار بر وزن | شهری است در ترکستان م«نسوب بخوبروبان *۱
(۱) چك , چش : خوب صورتان .
۱ - از مزاج اهل عالم مردمی کم جوی از انك
هر گز ازکاشانهٌ مرغان همائی برلخاست . خاقالی « جهانگیری » .
۲ -رك دکاشتن . ۴ - از 16۵۳۸۵8 ۵ (کاشتن ) [زمان حال :کارد] » اوستا
۳2۳22611( کارد)؛ درمقابل آن کشتن (بکراول) (بمعنی کاشتن)» سانسکر بت۳51 ,۰1۳۹1811
افنانی ۷۴2۳۵1 ( شخم کردن » کاشتن ) بريشهٌ اول متعلق است . و بلوچی ۸15128812 ( زراعت
کردن ) برسهٌ دوم . شاید اوستابی - 18۳8 * فارسی کار ۳ افغانی - 1۳2۲ #سادکریت 88۲
(پاشیدن) باءد ۶ هوبشمان ‎۸۳۹٩‏ و رك : اسشق ۸۳۹ .۰ ۴ - بدومعنی آخیر محرف
«گاشتن > (ه.م.) است. 8 -شپری‌دارای قری وروستاها که ازسمرقند وآن نواحی بدانجا
سفر‌کنند » و آنها در وسط بلاد ترله باشند و مردم آن مامانند . « معجم‌البلدان > .
‎٩‏ - ترك نزاید چنو بکاشغر اندر سرو تبالد چنو بکاشمر اندر .
معزی نیشابورق ص۶*۱*.
۷ - گاه بعدازلفظط «کاش» (ه.م.) لفظ « که»آورند و «کاشکه» باشباع کسره «کاشکی»
شده « فرهنکه نظام ». در رسم‌الخط فدریم «که» راهکی» مینوشته اند .
۸ - چند بازی برباط آرزونرد امید چندکاری درزمی نکاشکی تخم اکر.
معزی نیشابوری ص ۰۳۷۷۲
‎٩‏ - مایرخوف کوید :کاشم از طايفة چتری . 3۳0610 ع05316108[6 12۷19110070
( 11۷60126 فر ) است ولغت کاشم را باستناد فربتاکه ( 1۷ ۰ ۳۹ ) عربی دانسته . حکیم‌مژمن
گوید: «کاشم,اسم فارسی است وبیوتانی لیفشطون و دردیلم یره کوهی نامند . منبتش کوههای
بلند جنگل‌دار است . ساقش باريك شبیه بساق شبت وپرکره وبرکش مانند بر که ! کلیل‌الملك
و ازآن نرمتر و خوشبوی و برکه اعالی ساق باربکتی و پرشکافتر ار آخر ساق چتردار و مرش
سیاه و از بادبان بالیده‌تر و تند طعم و با عطربت و بیخش شبیه به‌پیخ انجدان وخوشبوی‌ومستعمل
تخم و بخ اوست .»۶ تحفهة حکم موژمن» . نگ بای معنی میحف ‏ کاشفر» (.م.).
```


## [2026-09-06T22:13:49.827Z] TOOL CALL #54: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:2163 2>&1 | head -40",
 "description": "BQT page 2163 (govāh)"
}
```


### [2026-09-06T22:13:56.110Z] TOOL RESULT

```
(no exact page map; using offset -1917 -> pdf page 246; check the printed number and re-run with --pdf-page if off)
REF: BQT:2163  PDF: data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf page 246  OCR-lang: fas

-۱۹۳- نکرش
* نگاشت!۱ <- بکون شن وتای‌قرشت, نگران ۰ « بیکر اول بروزن پران؛
ماضی نگاشتن است بعنی لوشت والقش کرد | بمعنی منتظ و بیننده و تأمل کننده باشد.
وساخت - نگرستن ‎٩‏ - بکر اول وفتح ناي,
نگاشتن ؟ « بکراول بروزن‌فراشتن؛ | مغفف نگرستن است که بممتی انگاء کردن
بممنی لوشئن - و نش و نگار ونقاشی کردن | ودیدن باشد .
باشد ۴ . نگرش ۲ - بکر اول و سکون آخر
نگاشته ؟۴ - پسمتی نش کرده شده - که شین قطه‌دار باشد » بممنی‌نگرستن اس ت که
ولوشته - وساخته شده باشد .۹ بممنی نگاه کردن و دیدن باشد .
۹ - ر4 : نگاشتن . ۴ * نگاربدن . متعدی ۸« نگریدن » (ه.م .) و
« لگریتن » (ه.م.) » پپلوی 38)1(۳4۳ وغیره » قس : ارمنی 218۳27 (تصویر ) , 36۴۳88 :
0 اسشق ۰۴۱۰۳۹ ۴ - آن صورتپا که ستارگان را بدو نگارند . « التفهیم‌س
۸۹ ۴ - اسم مقعول از «نگاشتن» (ه.م.) ۵ - از : نگر (نگرستن,نگریدن)
+ان ( پوند صفت فاعلی ):
ارغوان جام عقیقی بسمن خواهد داد چشم در کی‌بشقایق نگران خواهد شد.
2 حافظ شیرازی ص ۰۱۱۱
‎-٩‏ از : نگر (ریشه) +ستن ( پسوند مصدری ) * نگرستن :
هنگر در ( اندر ) بتان که آخرکار لگرستن گرستن آرد بار .
ضیاء الدین فارسی «فرهنگه نظام» ورك : امثال وحکم دهشدا .
۷ - پهئوی 81۴1۲1۹۳8 «اونوالاء81161۳198:*۹؛ پاز د218671850. 218876558
«هوبهمان ۱۶۳۸ » از : لگر( لگرستن » نگربدن) اش ( پسوند اسم مصدر) : « پس دیدشمن
از واسطهٌ دیدن او ازمن دیده پردوخت ولگرش باصل‌کار و هویت خویش درآ موخت .» « تن کرة
الاولیاء چاپ لبدن ج۱ ص ۱۷۲ ۰۶
۵ قاه - بکر اول . اوستا - 816858 5 (قی :آگاه) » پپلوی 2)1(8628 »کردی
ع 2۵62 . بلوچی ع 81680؛ رك: اسشق ۱۰۳۷ ؛ ربشهٌ آن 588 ( دیدن » نگریستن ) است
2 پارتولمه 40۹ » ؛ گیلکی (رشت ) 3182 . گیلکی ( لنگرود ولاهیجان ) #[8 ؛ نظردیدار-
نگاه کردن » دیدن ». نظر کردن . - نگاه داشتن » حفظ کردن » مخفی کردن : «مردم‌آزاری ...
سنگی برسرصالحی زد. درویش... سنگه را نگاه همی‌داشت نا وقتی که ملطان را برآن لشکری
خم آمد #«گلتان ص ۸۳ .
بقیه ازحاشيهٌ صفحهٌ قبل
2 ظ#ارش - بکر اول و چهارم ‏ از : انگار (ه.م.) اش ( پموند اسم مصدر ) ؛ نقش
کردن- تحربر» نوشتن . اداره نگارش » ادارة انطباعات ‏
۰ لگارپدن - بکر اول و فتح دال, از: انگار (ه.م.) + یدن ( پوند مصدری ) -
نگاشتن (ه.م.) ؛ نوشتن - نقش کردن » تصوبر کردن : :
بر اوبر انگارید جمشید را 8 پرستنده ماه و خورشید را.
فردوسی طوسی «شاهنامة بخ ج ‎٩‏ ص ۱۸۹۹ ۰۴
```


## [2026-09-06T22:14:08.910Z] TOOL CALL #55: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:1849 2>&1 | head -45",
 "description": "BQT page 1849 (govāh)"
}
```


### [2026-09-06T22:14:16.725Z] TOOL RESULT

```
REF: BQT:1849  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 646  OCR-lang: fas

-۱۸۸۹- کودر
و آن نوعی ا زگره باشد - وکنایه از آفتاب هم اول وثانی مجهول » بزبان ترکی نیز همین‌معنی
هست 9. دارد .
گوباره < بروزن جوباره » ,معنی‌دويم گوج < بفتح اول و ثانی وسکون‌چیم,
کواره است که گلهةٌ گاومیش وکاوباشد-وجایگاه | صمغ درخت را کوبند - و ٍم اول و سکون
گاوانرا نی ز گوبند . ثانی و جیم + بزبان ترکی بمعی زور و قوّت
و پال ۱ با بای فارسی بر وزن .باشد .
رومال ؛ نام مبارزی بوده از خوبشان پادشاه روی گوچاه - با جیم فارسی بروزن همراه,
- وبمعنی عمود وگرزآهنین - وتخت و اورنگی | کوی راکونند که چندان عمیق نباشد و بن‌آترا
آهنین و چوبین هم آمده است . ۱ توأن دید .
گوپان - با ئانی مجهول . بر وزن گوچی - با جیم فارسی بروزن اوجی,
و معنی چوپان است که شبان باشد ۴۳ ؛ و بابای | بمعنی گودال وجای عمیق باشد .
ابجد هم آمده است لیکن بممنیگواره‌بان بعنی گلود - بنتح اول و سکون نانی و دال
شخصی که کاومیش را بچرانیدن می‌برد ۴ . ابجد » بمعنی کوباشد که جای عمیق ویست‌ومغاك
گو بشا ؟ - بم اول و اسکون نانی است ۷ - و جم اول وافتح آنانی مخغف کوید
مجهول و فتح بای ابجد و شین نقطه دار بالف | است که ازگفتن باشد .
کشیده بزبان زند و یازند انگیین را گوبند گوداب ‎ -‏ اول » بروزن و هعنی
و بعربی عل خوانند . دوغاب است - وآشی‌را نی ز کوبن د که ا زگوشت
گو بیا * - با نانی‌مجهول بروزن لوبیاء و برنج و نخود و مغ زگردکان پزند و قاتق آترا
بلغفت زند و پازند زبانر! کویند و بعربان لان | از سرکه و دوشاب کنند و آبرا آش حبشی
خوانند . خوانند ؛ و بعی کوبند طمامی است که در زیر
گوپیاده بکر بای فارسی و زای | بربان پزند وآنر! بریان پلاو خوانند ؛ و بمعنی
نقطه‌دار , طمامی است متمارف در بلخ وآن بگه دوم بجای دال زای نقطه دار هم آمده است ۸
بیاز بلخی اشتهار دارد . . واسصح انت .
گوت ۱ - بنتح اور و سکون نانی گودر* - بننح اول و ثاات بر وزن
و فوقانی » کفل وسربن مردم راکوبند ؛ وم | کوثرء نام مرغی است ازجنی مرغابی که کوشت
۹ - رك : کوپال . ۴ -رك : غبان» چوپان . ۴ - از : کو(کاو )۳+ بان
( پوند نسبت و اتصاف ‎ )‏ کاوبان . ۴ -هز . 2(ط8۵8025 ۰ بپلوی 28831067
(انگیین) «,ونکرص۸۹». ۰ 8۵802 (زبان) «بندهشن . چاپ پوستی ص۲۲؟۲) دریغلوی
2۴ با 883 بمعنی کویا و کوبنده وسخنگوست . رك : باروچا ۱۹۹ ۰
۱ - ترکی است . در ترکی جفغتاتی «کوت» ( سربن ) « جفتایی ص 2۹۳ >
۷ - اسلا از آرامی و سربانی مأخوذ است « تقی‌زاده . پادکار ۸ : ‎٩‏ ص ۲۲ ی
۸ - بعنی کوزآب ( آ ب گردو) . ‎٩‏ - رك : کودره..
۵ واه - ینم اول وهای ملفوظ » پپلوی ۰816889 80625110 ( شبادت ) ۰ از
- 0۷1-6392 (قی : 2-638 ) ؛ فارسی :کواء از 808۳3 6 از ق2806 (شکل‌جنوب
غربی ) « نی رکه ص ۸۵ » و رك : اسشق - هوبشمان ۹۶*۰ ؛ شاهد - دلیل » برهان .
2 گواهی - بم اول . از :واه ی ( حاصل مصدر . اسم معنی ) ؛ شهادت ‏
```


## [2026-09-06T22:14:30.150Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== FFD pdf 78 (printed 73) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==78' incoming/FFD/FFD_pages.txt | head -50",
 "description": "FFD page 73"
}
```


### [2026-09-06T22:14:31.808Z] TOOL RESULT

```
=== FFD pdf 78 (printed 73) ===
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


## [2026-09-06T22:14:41.882Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for f in MON_part1.txt MON_part2.txt; do echo \"### $f\"; grep -n \"چریدن\\|چرید\" $f | head -5; done",
 "description": "Mo'in čarīdan"
}
```


### [2026-09-06T22:14:43.706Z] TOOL RESULT

```
### MON_part1.txt
49916:چرا: 7-3« (امص.) چریدن» عمل جانوران 
49985:چریدن حیوانات علفخوار» سرتع؛ علفزار 
50225:چریدد: 227-0 [چرا کردن ] (مص م.) 
50226:(چرید» جرد خواهد چرید» بجر چرنده» 
50227:چریده» م: چراندن» چرانیدن) علف خوردن 
### MON_part2.txt
52621:(مص‌ل.) چریدن چرنده. 
53414:ج. مراعی. (مص‌م.) چریدن. 
53471:مرعز ۰ ۱12۸1۲ ۳4 (مص‌م.) گیاه تر چریدن.
```


## [2026-09-06T22:14:46.717Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '50215,50235p' MON_part1.txt; echo \"--- page marker search ---\"; awk 'NR>=50100 && NR<=50240' MON_part1.txt | grep -n \"126[0-9]\\|127[0-9]\" | head",
 "description": "Mo'in čarīdan entry"
}
```


### [2026-09-06T22:14:48.422Z] TOOL RESULT

```
چر نده. (0-)62۲-2002 (افا. چربدن) حبوان 
علفخوار که چرا کسند؛ علفخوار؛ ج. 
چروک: (ا.) جین و شکن که در 
روی پارچه با پوست بدن انسان ظاهر گردد. 
چروک: [تر. - چر کث ] (ا.) نان. 
چسروکیدن: (ع)هل تم (مسصل.) 
چروک یافتن؛ پر چین و چروک کردیدن. 
چر ونس: 5 (.) واحد بول روسیه 
معادل ده رویل» طلای ده مناتی. 
جرویدد: 2۲۷-20 (مسصل.) جاره 
چریدد: 227-0 [چرا کردن ] (مص م.) 
(چرید» جرد خواهد چرید» بجر چرنده» 
چریده» م: چراندن» چرانیدن) علف خوردن 
جانوران علفخوار در جراگاه» چرا کر دن. 
چریک: (ع):آ:ت [تسر ۰ - چر ی ] (.) 
سربازان داوطلب تعلیم ندیده» جنکجویانی 
که از افراد عشایر و قبایل گرد آورند و به 
یاری سربازان تعلیم دیده فرستند؛ حشر: 
جزک: تم [- چزغ - چژک] (ا.) (جان.) 
خار شت. 

--- page marker search ---
```


## [2026-09-06T22:14:58.125Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"cāśta\\|cast-\\|to taste\\|tcamja\\|cā́ś\" ISS_alt_DKS.txt | head -20; echo \"=== search 'taste' ===\"; grep -n \"'taste'\\|‘taste’\" ISS_alt_DKS.txt | head -15",
 "description": "Bailey DKS taste"
}
```


### [2026-09-06T22:14:58.188Z] TOOL RESULT

```
859:ага ‘saw (tool)', 11 43:17—19 draumd khva hvai amgau baidá raijsai йтй hamjsá gūsta thajd dita dite а và ristd тайга hadárá dairà баай табу ysvyai kaina qstam dawuhlhq varásai ' just as a man may draw a sharp saw over his limbs and pull the flesh about, or he licks a sharp knife to taste the honey on its edge, at the last he feels the pain’. N.Pers. arrah, Baló&t аттан, harray 'saw', harag kanag “то saw', lw in Ormurt are, Yidya arra, Sanglect arre. TE Pok. gr1—12 ser- "cut with hook’, O.Ind. srnt- ' hook to drive elephants’, frg ‘sickle’ (secondary #- from s-), Lat. sarió ‘to hoe’, with -p- Lat. sarpió ‘to cut off’, Greek &prm ‘sickle’, O.Slav. srüpit ‘sickle’. Iran. *harn- to Ваібёт harray, with lost h- N.Pers. arrah, and Khotan Saka here ürd from older *Латт1-. See also s.v. jtravi ‘пате of a grass’, if named from har- ‘to have a cutting edge’, for BS hrivera-.
4114:paysauja ‘pungent (?), п 8521-2 paysauja püha:ra dspurá 'savoury (?) vegetables complete’. From *рай- xau(3)- ‘taste’, rather than to paysau ‘rotting’ from *2ati- gau- with ysii ‘pus’, See ysis- ‘to taste’,
7254:irestha-, Greek kpeicov а good meaning ‘good, exalted' is oifered. The alternative ГЕ Aei- 'to lie down’ (see above ##й-) leads only то ‘home’ or 'civil'. Other Iranian con- nexions can be sought in Orm. fir, sir (with variant initial) ‘good’, Balaét sar, ari 'good, goodness’ (also атт), if -a- replaced -i-, bur mirag ‘to die’ retains -i- (here Oss, D. máluz has kept -а-). Sogd. Bud., Man., Chr. fyr- with short -i- *fir- has i- which could be normal from a variant IE Ajer- (as IE geu- and ĝjeu- ‘to taste' co-existed; see for -y- BSOAS 20, 1957, 58-9). M. Parth. T. £yr in iyr-g'mng ' friendly, wishing well’, may be like myr- ‘to die’ (*mrya-) and also with initial $- < 5i. Pašto has mrəm ‘І die' < *mrya-, hence £2 'good' may be *iryd- with -ə from -ya-, as стэ ‘heart’ from srdya-. This comparison with fa excludes *йга-.
7357:preverb i-«sfa-«adi-, see s.v. sia- preverb and sūh- ‘prepare’, to TE yer- ‘assert’, cognates s.v. vauda. Svrrai 'sütra-text (7), пт roo-8—ro (a list of studies) drrayvā pilyä artha ausairma büyüka tti jsam bavüvà ата а siya hadàáya iorrai u malai süika tti jsü java ttyau ysyai hürüka sa khi acari prrabhá ' controlling the vital mean- ing in the three basic texts, then also studying in the philosophical books night and day, the sütra-collection and the formula-collection, the commentary, then also in the prayers, giving the taste of them, just like the teacher (BS acürya-) Prabha'. For these Buddhist technical terms the following commentary is necessary. The pila- from Prakrit pela- of the collection of sacred texts (see KT vr 108, and 195), Pali pifaka-; bavava- may be bhava-vada- ' discussion of being’, hence ' philosophy? (see also KT rv 83); surraí may be Prakrit from *surta- for older sütra-, with -rr- replacing -rt- as in the lw parramá- ' image' from *partimā- older BS pratima-, and also with sw- in place of sv- as in Kroraina swasti beside svasti- 'welfare', лази ‘sister’. The word málai contains а form of mantra- through *mānla- (as a dialectal Iranian *inühra-, which also became mahr and mār-; see s.v. mätrvälai, BS devapalaka-). "Тһе stika is BS рка 'com- mentary’; jäva- is older BS jápa- from japati 'to murmur prayers’, For acari Prrabhá, note the similar JS 2r3 ücüri Devd. In Khotan Saka avasța 'studying' may occur *abisia- 'occupied іп’ from "*abi-fla- to base ah-, Av. aiwi šti- ‘study’, Orm. aw-, haw-:hištak 'to read’ (from abi-ah- and abi-šta-). The word ysyai ‘savours’ is the older ysuye, base ysizs- ' to taste’, hence used for BS rasa-, like the cliché eka-rasa- of the one taste of the dharma- doctrine (Khotan Saka fau-raysa-). The text is the de- scription of a beloved person who has gone to China.
8337:haysgä- 'nostril', plur. ‘nose’, Z 8:36 haysge bussañi viri ysuyaiii uird bisa ' the nostrils to perfume, the tongue to taste'; JS ror2 haysgye dasta pä ‘nostrils, hands, feet', K 56, 19r4 haysgi, K. 56, 19r2 haysgyi, gen. plur. K 56, 19v haysgām, loc. plur. Sid. 20v3 haysgua, Tib. snar (in thenose"), Sid. 1375 haysgvastà; adjective, K 56, 20v4; 2111 haysgaja-; compound, 1 191, 11374 haysga-ttüjsim. (-йп —-ai) ' nose-flowing', BS pinasa- 'nasal catarrh'. From hazg- to *fra-zga- to 'smell' from following (the scent) as Ау. (the dog) оойипа-сра 'clinging to the blood’, Armen. lw драт 'feel, hear, know, to scent’, agajakan ‘sensitive’, sgajaran 'sensorium', see cognates s.v. aysagamu and ajs- 'to cling to, pursue'. See O.Ind. ghrāņa- ' smell; nose’, jíghrati, ghrati 'to smell, perceive odour’. Hardly to Zor.P. 'zg, azg ‘branch’; Armen. lw azg, -ac' “nation, race, kind, age, manner’; asgakan
8638:vomiüng', BS aruci-cchardi-, Tib. yi-ga héhus-pa dan, sRvug-pa dan, Possibly from "fra-zudba- ‘depriving of taste’ reversive fra- (see s.v. hamatte) and -azi-» -iz-, то Sogd. Bud. z8'8 'taste', sf” , verbal zg'Bt ' he tastes’, ='28' 81. To IE Pok. 399 Zeu-:$u-, and Zeu-s- 'to taste’, O.Ind. jos-:jus-, Av. zaof-, see jūh- above. A variant is Sid. I34r4 Лаиїди-ш-ї hame 'he has loss of appetite’, Tib. yi-ga héhus-pa dan, See also šu-> zb, M.Parth. T. pdyzb'd 'chased. away', M.Pers,T. pdyz-, pdyyz- ("pati-aiya, W.B. Henning apud M. Boyce, The Parthian hymn cycle, p. 193). For increment -5-, note IE Pok. 370 gen- 'press', gn-ebh- ' press together’, Pok. 386 ger-, gr-ebh- біла", Pok. 455 ghr-ebh- ' grasp’, Рок. 359 gel-, gl-ebh- ‘to ball up’.
=== search 'taste' ===
2846:tcáüs- 'see', Z 22:319 jseinu vátà nä chádrra ісйзагі ' they see their faults in detail (rather than 'quickly")'. Base cas-, from kas- ‘see’, with -s-, *cax-F-, Av. байа, čašāna-, O.Ind. caste, cahs-. IE Pok. 638-9 R'eh-, Av. Ras-, M.Parth.T. pdgs- 'look' (*pati-kas-) and noun pdgs ‘a look’, "gs, 'gs ‘apparent’, Zor.P, й-Ёй ‘aware’, O.Ind. käsate, See also nájsds-, pajsäş-, vajsiş-, vijsis-, hamjsás-. With k-, käs- ‘to think, care for’, and pacas- ‘to confess’, With -2-, Zor.P. čāštan 'teach', сайп ‘taste’: beside vicasisnih.
4114:paysauja ‘pungent (?), п 8521-2 paysauja püha:ra dspurá 'savoury (?) vegetables complete’. From *рай- xau(3)- ‘taste’, rather than to paysau ‘rotting’ from *2ati- gau- with ysii ‘pus’, See ysis- ‘to taste’,
6392:узага 'tasty, pleasant’, п 87:53 byaihat pasai узата 'I get the pleasant syrups'. From *узйта- adjective to ysuy- ‘taste’, possibly *zaufara-.
6459:ysuye 'taste', SuvO. s6r1 rays(d)na ysuye jsa ' with taste (dyadic)' BS rasena (not -u-); Sid. rssvr ysuye ne bautte 'does not know the taste', Tib. ro mi chor-3in; Sid. 15v4 itye ysuye 'of the taste’, Tib. ro; К. 56, 21r1 u ysauisa ysvañä raysa (loc. sing.); 2 3:59 ysuyañi 'tasty things’, hvarindd gyastuii ysaujse ysaujse ysuyañi 'they eat various royal (celestial) tasty dishes'; loc. plur. SuvO. 2412 ysvyañuvg, BS rasa-; nom. sing. V 116, богу ysau üsd panaste ' taste's force disappears’, BS rasa-ojas-ca na bhavanti; adjective, ysojsa- 'savoury, pleasant’, 2 21:24 ysopse ysuyarid, Z 3:59 ysaujse ysaujse, Sid. 123r1 ysaujsá mauna 'with tasty liquor’, BS sura-mandena, Tib. ¿han áim-po; JS rsri ysaujsá hvada hhasta ‘savoury food, drink’, From *диїй- to ysüg- ‘to like, approve’ with cognates.
6464:ysüs- ' to like, approve', 3 sing. Z 12:44 nyaste ne ysüsde ‘he disparages, does not approve’; Manj. 364 dhàraiia ysusde ‘Һе approves the dharani-formulas'; 3 plur. Z 23:4 ne ysyüre ' they disapprove’; r plur. п 54:76 ysvam bvejam anumaudam ' we like, honour, approve’ (BS anumodaya-), with bvej- from bulj-; preterite, SuvO. 27v3-4 stavátündà buljátandà u ysusfüjdàá ‘they praised, honoured and approved’, BS stavito varnitah pradfamsitah; К. 143:1057 hvanau ātaudāmdä u ysustümdr ‘they delighted in the preaching and approved it (y7)!, Tib. muon-par bstod-pa; Sid. тодгт ysusfa sfe ‘is liked’, BS isyate, Tib. bzan-n0; Sid. 20r ysusfa, Tib, rup-ba; Manj. 386 pahaisüme jsa nai ysügfa ‘did not approve of flight’; noun, Bed 46va фийаи уғоуйте jsa ajtgüme dana, namamdrame jsa ‘with approval of merits, in desire of dharia-doctrine, with invitation’ (BS adlyesa-, nimantraya-), BS modana- adhyegaga-ayücana-. Adjective ysüska- 'desired', SuvP. 73Y1 aysiskye, BS anista-, Z 10:4 ysüská, , „horä 'accept- able gift’; K 52-74 mimi pye ysüska ‘ту dear father’; К. $2'7°5 màvd mam ysitska чпу dear mother’, К. 52:7:8 tti münà pürysa ysügka ‘these may dear servants’; K 107286 paríg ysüska ‘acceptable service’; V 644 hiya ysügka tta vā brütard 'his own dear (sons), also the brothers then’; Manj. 191 pūra ysida brrī u ysiska 'she bears a son dear and desired’. Comparative, rrt 101:41 hvai brrauda ysūşkyaira 'man dearer, more desired’. From zauf-:zui- ‘to approve, desire’, Av. zaos-, хаоїа-, mušta-, О.Регз, daustar- 'friend', nom. sing. dausta ‘friend’, Zor.P., N.Pers. 005; Zor.P. дап, dósarm, M.Parth.T. swf ‘zeal’, Pašto (loss of negative) сша ‘grief; noise’ (*a-zauia-) IE Pok. 399 £eu-s-, Greek увоз 'let taste’, yevopor “taste, enjoy’, Lat. gustus, dégürà ‘taste’, Alban. desha ‘I loved’, Celtic O.Ir. do-goa ‘he chooses" (*pur-à-t), Got. kiusan ‘test’, kausjan ' test, taste’, O.Engl. ceosaz ' choose'.
6477:узап ‘taste’, see s.v, узшу,
6505:ysve 'taste', Sid. r6vr cu kumjsa {е ttye узше delüka suce hoi u hvarq u grām, hauva u ttavadya huşa baye what sesame is, its taste is somewhat alkaline (*suxtaci-) and sweet and hot, it increases strength and bile’; BS sa- kşāra-madhura-snigdho balyosnah pitta-hrt tilah, Tib. til пі thal-bahi то bro-ba dan, mnar-żin kha-la drod čhe-ste, #am-stobs dan, mhhris-pa bshyed-do. See ysuye.
6507:ysvyatiuvo 'tastes', loc. plural, SuvO. 242, BS rasa-. See s.v. ysuye 'taste', base ysiis-.
6509:ysvye ‘taste’, Sid. 15v4 ttye ysuye, see ysuye, and HI 100'10 ysyai 'savours! < *ysuye.
8228:hamárgya ‘alleviation, relie, Z 516 сит ye üliva nitcana īndä samut ttamdu hamargya "when one puts ointment (BS alepa-) on the outside of it, it is only relief for him’; v 46, 2275 samvi tamdu hamàja, parallel to Manj. 133 sami ttada nasaume vina ' just so the pain for him is only quietening'. From Jra-mür- "press away’, *fra-màracá- Oss. D. ldmarun, I. lámaryn, lämärst ' press out, turn’, IE Pok. 735 mer- 'rub off' and Pok. 716 mel- 'crush'. See s.v. mur-. For -argy- with -aj- note also khürgga- ‘mud’, loc. sing. kharja, khāje, khüjana. See hamara- ‘taste’.
8638:vomiüng', BS aruci-cchardi-, Tib. yi-ga héhus-pa dan, sRvug-pa dan, Possibly from "fra-zudba- ‘depriving of taste’ reversive fra- (see s.v. hamatte) and -azi-» -iz-, то Sogd. Bud. z8'8 'taste', sf” , verbal zg'Bt ' he tastes’, ='28' 81. To IE Pok. 399 Zeu-:$u-, and Zeu-s- 'to taste’, O.Ind. jos-:jus-, Av. zaof-, see jūh- above. A variant is Sid. I34r4 Лаиїди-ш-ї hame 'he has loss of appetite’, Tib. yi-ga héhus-pa dan, See also šu-> zb, M.Parth. T. pdyzb'd 'chased. away', M.Pers,T. pdyz-, pdyyz- ("pati-aiya, W.B. Henning apud M. Boyce, The Parthian hymn cycle, p. 193). For increment -5-, note IE Pok. 370 gen- 'press', gn-ebh- ' press together’, Pok. 386 ger-, gr-ebh- біла", Pok. 455 ghr-ebh- ' grasp’, Рок. 359 gel-, gl-ebh- ‘to ball up’.
```


## [2026-09-06T22:15:18.037Z] TOOL CALL #60: Bash

```json
{
 "command": "sed -n '1,25p' tools/fetch_source.py",
 "description": "fetch_source usage"
}
```


### [2026-09-06T22:15:18.075Z] TOOL RESULT

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
```


## [2026-09-06T22:15:19.829Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT col 409 area: kas- ===\"; grep -n \"kas-\\s*.*'sehen\\|kas-  \" BRT.txt | head -5; grep -n \"409\" BRT.txt | head -5",
 "description": "Bartholomae kas-"
}
```


### [2026-09-06T22:15:19.894Z] TOOL RESULT

```
=== BRT col 409 area: kas- ===
9421:•  j.  kas-  V.,  nur  mit  ä  'gewahr  werden,  Eig.  'der  wenig  Nahrung  hat   (braucht  oder
9453:•  1.  'kas-  V.  lehren.  Praes.  i  oir-.  ^j   jj^„i  „„-irnK   diaytnl,   Jlins
8575:409
16050:Unrichtige  Et,  GlrPh.  a.  409.  —  Ob  im  RV.
22429:ai.  vadhu-  f.;  np.  vgl.  bayög  'Braut'.  Vgl,  va- irya-.  —  ■)  Nach  dem  Musler  der  T-Slämme (lu  S  409:  vgl.  S  407\
23454:1409
27944:FB.;  sabiSmand,  Npü.:  saiz  rang,  ei\.:  Jihän sar  sabt  kunad;  daher  DsT.  ZA.  2.  409  'maitre de  la  verdure'.
```


## [2026-09-06T22:15:22.286Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '9418,9460p' BRT.txt",
 "description": "Bartholomae kas- entry"
}
```


### [2026-09-06T22:15:22.386Z] TOOL RESULT

```
mp.  (Pu.),  np.  /li-'iir».  —  ■)  VgL  zF.  %3'js-  —  •  j-  kasu'pitav-  m.  EN.  eines  Gläubigen:
»I  Geschlechlswechsel!  S2^9-l.  — J'IJas  mit  'tiUiarahe    asaoiiö    "des  A'.,    Sohnsdes
jAw.i(i/-);''auf  ir.  *;i/-jy' zurQckgeht;  IF.S.ä6i.  ^        "   Y(  ^j    jj^
•  j.  kas-  V.,  nur  mit  ä  'gewahr  werden,  Eig.  'der  wenig  Nahrung  hat   (braucht  oder
erblicken'.    Praes.  3  kasa-.  ail"'/-
lat    mqm    mairyS    äkaiat    "darauf  er-  •  j.   kasyapa-    m.   'Schildkröte',    die    als
blickte  mich  .  ."  V.  22.  2.  lAiiT'isches  Tier  gilt:  baevan  'panqm  ava.-
Vgl.  ai  kaiaif  'er  erscheint',    äkaiya    "im  Er-  janyät  \.J4.  5.
schauen';  np.  ü.cJ*  'kundig',  iti^Ah  'Anblick',  ü.  kaiyafa-  m.,  np.  ^.i  ('«/.  — Pü. :  undeutlich,
ooss.   k'äsin   'anschauen',   rih/'   ('Gesieht'  ^)       .    ,  ,_     .  j-    .-       i_  r       1  u      1  1   ■
■A.I.'.).   -  s.  »,J.,  *«A  und\ii»rÄ..   -  •  J.  kasyah- Adj.  (mch  fem.)  der  kltinere,
Vii.;  äH^Ji  a!  an  i  mar  iaiil,  ei\.:  j!ui amlar  geringere':   ya^a    masyayn    äß   'yurtham
db,Google
4ÖI  kasyah-  a  —  Icata-  462
(GPf.)  apam  *avi.frädavaiU  (sd)  V.5.  24;       ■>  Vgl.  iBed.  p.  pou-Aoc,  ai.  pari-cari-  m.;
—  *koys  hmti  masyanhs  asoa  (sd.)  .Maya       •-"  Osthoff  BB.  15.  316.
iffo'«»'*^  F.  Je.       a)  'verkleinernd,  herab-  J   '"'^  •"■  S'-  ''«s  '^'^a.
setzend'    in    'vawAf    Jfl»yi.lj     ^ai^jV/    'er  •  j-  iristanqm  "kaäin^m  Vd.  14.
setzt  herab,  verleumdet'  ■>,  Jemanden  (Akk.)      ^=?;='"*  '"  ™^^.A^^'.,™ ;  sd.  _  Pü. .  r«ü«
bei  -  (pat.)'>:  yJ  nar,m  amvan.m  myö_.-_        "-  \^^       ^_  ^^,^^  ^  ^._
i-arPttät    vä  .  ,     'yaime    saanlt     danäiti        .     .        „       s  „.«-,-    ^
y  "^  •  j.    ka-x*araoa-   m.,   -x'araioi-  f.   Be-
komplr.  itt  :*o«i-.   .-  mp.  *^^,  np.  kih.  -  Zeichnung  einer  Klasse  von   (männlichen
Pö.;  km;  s.  No.  I.  —   ■)  Pü.!  ke  mart .  .  ö  Und    weiblichen)   Wesen   der   A/i/ischen
an  I  iämai  ,,  :iajS.  erl.:  ta  sai^an  i  5  öi<m  Schöpfung:      Aamtstayas'a     nühntayal^a
Aj.«7i  ifl...^.)  AndersDsT.ZA.2.221  nach  .^„„^^^     ^i^i„am:a  .   .     'lakeca    -mhca
Dk.  8.  44-  57(?).  y_  ßl  ^                 *                                         -"
•  j,  kasvika-  Adj.  (fem.  'kä-)  'ganz  gering-  Ableit.  —  E[g.  vU.  'was  für  ein  (abscheulicher) fÜgig':  'kamcina  yanhuyanam  (sd.)  avan-  schwarzer  (Kerl)',  ilal.'negraccio'.ebeBeieich- j_    _    i-'.e..    ._  I      nune  fiirfremdlandisches  lahrendes 'Volk 'I,  das
Abtat  III  ii,«..  -  IV:  i./.*.  _  ^„    ,jL  ^^,„.  ,i.i,w.(«ii,i  •♦.,,..
•  j.    kasvis-    1)    m.    Name    eines   Ge-j     .i;,  m,-'.  s.  hbm.  KZ.  z/.  104.  AGr. /.  162.
brechen.,  einer  Kranklieit  od.  dgl..   »13,     T,l^::J;'ZLtXZ}X'\''TJ'r7„,Z,Z '  .    ,„^,  I      deutsche  Bauer   bezeicbuet  nie  Zigeuner  als
ii:jr-<j  frakavB  .  .  ml  'vis  (NS.)  mä  -braune  Teufel'.  —  .)  Zs.  15.  1  macbt  das Z'izbärii  V.2. 29.  a)  als  Dal!'a  perso-'  Wort  lum  EN.  —  3)  Vgl.  zu  kaxuii-. nifizirt:  -i-U  d„ni  p^llitl  äati'ü  .  .  V. ! .  ,  kax'arajainya-  Adj.  (fem.  -w-)  'üir J5.43.  2)  Adj.,  von  dem  damit  be- 1 ^toe  der  &A«oo  (sd.)  gehörig':  jM hafteten:  ml  m  alujä  mo^rays /rania- 1^,„„„„„-  .  y^^,  .5^,-,„  yt.  1. 9,  12,  i6'. r>ntlt   *t»3  *'vW^   (NS.)   Yt5.  92.  Ableit.  aus  kaiFartla..
EbPSlammansatzunsicber.  —  Fu.:kdnddnn3>.  _
—  0  NA.  ma^ajr-.  —  "  Der  Vergleich  mit]  •  ).,  g.  KS-  V.  'verfangen  nach  -. ai.  karfku-  f.  'Krätze'  (Bthl.  Stud.  1.  53)  istj  Praes.  27  kaya-,  Perf  I  idk-;  l-KaX.  1 ganz  unsicher.  —  Jl  In  DaRabs  Ausgabe ;  sonst   /. j^.       PPfP.   'klta-,
.'   '"  ;  ,  ,         1     'verlangen  nach-,  wünschen' :  fravasayB
•  1.  'kas-  V.  lehren.  Praes.  i  oir-.  ^j   jj^„i  „„-irnK   diaytnl,   Jlins
I)  lehren,  mit  Dat.  der  Pers.  und  Akk.  ,j^a//^,„  /ajtu/i  Vt. ;.?.  24.  a)  spez. der  Sache:  ^'it  'ttra^äli  (sd)  'mqinm  ,g„„  t,.„„„  i^^^^  wollen',  auch  mit ail,n  N.  17:  —  mrt  „laom  ..  arnua  i„f  ^^,  q^  .  ^,  j„„,j  ^j;,  ,„„r  i» Aii/«(sd.)  taianäicn"  .  .  xraftm  asa-  ^„„1^^;  „  ^aUlm  inl  (iS.)  a/imai ,m„S.S4-  2)  'Unterricht  erteilen,  „^^  „„„a»to  ya  ' nmyäJyäi  mantä imt  Dat  der  Pers.:  (*«/)  »I  dalvayatnlt  „„/^^j  "da  ich,  der  Priester,  durch  ^& !'J         •zl?5>:,j.   (sd.)   *ä.il./(l>  N.J7.  ^1,    „jh,„   (pfj^j    ,.„„„    I^„5„    „ill)
eJ^re':Tr''."denXS'el^.,:'sS-3"'-  "»  i'"  »»»'l»  "«'l'  rahUtaMai.yav ai.  f<i.r/c  'er  sieht",  mp.  i//o/tf«r4  (s.  lu  z^K/qi,  kennen  lernen  will,  die  Landwirtschaft P0>,  äj/itt  'Obacht  geben'  (GIrPh.  /b.309),  in  jenem  Geist  zu  betätigen,  in  dem  es"' «p.  (Pü.)  ^äiiian  •lehren'.  -  0  Y.7  Sieht  äiic;  s. '  gedacht  ist"  Y.  !  J.  6 ". "^ri^Tl^^^^li^i^-""'"'^  niit  .A,  -?r;  ,pa  ^^,  k^.kän,aiäe .      ,    ,           .(Konj.?)  Vyt.22.
•  j.  'kasa-  m.  Achselhöhle  :  dastmm  ■  ^L  vgl.  *r7>onii«j.  Adj.  'begehrend',  drao- (bz.  Ajf^/n)  'W/W  V.  Ä  48-50*,  <?.  17,  18^;'  Adj.  'carus'.  —  S.  noch  kima-.—  Pü.  (lu  Y.): —    ;;aV    hts    bardii    nfa    'Um    N.  2.?;  — '      =^ähll.%ü.isamlhau;  (zyi^^^y.tallihinim   -
■    -  "  s-      -I         »T    o  -   -1      ii    T7  I       ■)  Nim ,    virnveidyii.     —    »)    Vgl.   iSt.  Gdn,
v..iak,a-  m.,  mp.  (Pu),  np.  .*a.-;  vgl.  af^.  kse  ^      ^^j,j,^_     ^*   '«  *■     J .       ."       >  ,J.   ,  .  ■         ,1  '  j.  iJ<J/?aö«flBam  Aog.  77:  lies  ^'J'%,f3fli".
•  1.  'kasa-  m.  Sichzutunmachen  mit  — "';  .  ,,  ,  ...  „nm  n  j  i»  n ,,.'  ,,1  •  1.  'kala-  Adj.,  PPiP.:  s.  'kan-  und  «a-'J. UartUDg  ')                                           _                           J.        E,  _  v^,'.  u:ua..-  .)  Es  ist  nicht  in
KompE.  -  Aas  ir.  'kcHa-  (.g1.  i»«ya-i  S  ^/?.        entscheiden,  «ohin  -i^/«.  gehör..
```


## [2026-09-06T22:15:36.343Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### HRN\"; grep -n \"čašm\\|casm 'Auge\\|carx\\|bazar\\|bäzär\\|cašlden\\|casiden\\|calak\\|caridan\" HRN.txt | head -20; echo \"### HUB\"; grep -n \"casm\\|carx\\|bazar\\|guvah\\|gnvah\" HUB.txt | head -20",
 "description": "Horn/Hübschmann greps"
}
```


### [2026-09-06T22:15:36.405Z] TOOL RESULT

```
### HRN
1821:1466. bäzär 'Markt', bazargan, hazergän Kaufmann'.
1829:np. bäzär ist allgemein entlehnt.
2257:mäz. bazarg.
4851:Suffix -gän^ wie in x^idälgät?, bäzärgän^ bendegän (E[»igraphia indica
11832:bäzärgän 166, 539 Anm.
18422:K. carx 437.
### HUB
1783:Sprachf. p. 50) = afgh. LW. carxa *Spinnrad', arm.
1792:440. Zu (asm 'Auge' gehort 6asma = phi. casmak ^Quelle*.
4108:zd. casma u. s. w.
4476:'Auge', zd. casman-,
4710:= bazOrgan von bazar *Markt'.
5429:in pairivara-; bazar *Markt' = paz. vazar Shk. 272, phi.
5606:*Handel, Markt' = np. bazar -^ vank, vang Xaut* = np. bang;
5671:'Erlangung ?; 8) gukas 'Zeuge' --= np. guvah, skr. "^vikaga-":^
5750:Zeugniss' = phi. gukasth Shk. 247, Min. Gl. 95, np. guvah,
7418:(phi. depak) ; guvah = guva ; giydh = giya u. s. w. Unter welchen
7508:202, skr. kuQ); guvah 'Zeuge' = phi. guka&^) Gl. and Ind.
7652:Min. 61. 126 — 128, aber h in hubOl^ hucasm, Jmcihar^ hudln
8048:*Luft zuf acheln ; bazar *Markt' = arm. vacar ; pazam *koche',
8422:casm 'Auge* = zd. dasman-, skr. caksus ; arm. LW. sahapet
8614:casma 'Quelle' von cas7n *Auge\; dasta *6riff* = phi. dastak
8973:'kaufen', skr. krlnati ; carx Rad' (arm. caxr, caxarak) — zd.
8977:vgl. carx *Rad'; Suhr-db, Suhr-asp H. 730 = surx 'roth*;
10367:carxa 52.
```


## [2026-09-06T22:15:45.863Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '1815,1835p' HRN.txt; echo \"=== which leaf? ===\"; python3 - <<'EOF'\nt=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt',encoding='utf8',errors='replace').read()\npg=t.split('\\f')\nfor i,p in enumerate(pg):\n    if '1466.' in p and 'zar' in p:\n        print('leaf',i,'printed',i-21)\nEOF",
 "description": "Horn bāzār entry"
}
```


### [2026-09-06T22:15:47.817Z] TOOL RESULT

```
V^
*) Skr. vdra- TBr. 1, 1, 8 ^Ross* ist ganz unsicher.
')von Stackelberg (briefliche Mitteilung) stellt dazu auch
088. hairdg (ZDMG. 41, 575 Anm. 6) und verweist auf Miller, Ose.
Stud. I, 48 Zeile 5, 112 Zeile 30.Die Praeposition findet sich nur in der jüd.-pers.
/ Bibelübersetzung.
1466. bäzär 'Markt', bazargan, hazergän Kaufmann'.
g. vijüLrx Käs. böz6r, vö}6r.
phlv. f)ä6ar *Markt' (vergl. arm. LW. vacar^ vacara-
kan^ vacarik, und Xüfistän vajär, Nöldeke, TabarT-
übersetzung, 13 Note 3), ba£ar (PP61.), vacarakanth
•Handel' (PPGl.).
Wegen phlv. c ist die Zusammenstellung mit ap.
abaiaris^) unmöglich.
np. bäzär ist allgemein entlehnt.
167. häzvL *Arm'.
g. bat (aus *baht), Kas. bot, böht böhu etc.; ""inNZ
(Is. 3, 20).
aw. bäzu' *Ärm'; phlv. bäzüh^). bazak]masih^) (ZPGl.);
ai. bahü-,
kurd. bOsk, bäsik: bei. bozk (35).
=== which leaf? ===
leaf 59 printed 38
```


## [2026-09-06T22:16:00.895Z] TOOL CALL #65: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/%D8%A8%D8%A7%D8%B2%D8%A7%D8%B1\" \\\n \"https://www.etymonline.com/word/bazaar\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/k%CA%B7el-\" ; do\n timeout 120 python3 tools/fetch_source.py \"$u\" --note \"page 290, roots Kwek/Kwel: bazaar chain and PIE *kʷel-\" ; done 2>&1 | tail -20",
 "description": "Fetch bazaar + PIE kwel sources"
}
```


### [2026-09-06T22:16:04.112Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/1354a0009a99a521.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/577a680138a66ff6.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a0a0020111279d5d.txt
```


## [2026-09-06T22:16:07.290Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"=== bazar wiktionary ===\"; grep -n -A4 -i \"Etymology\" 1354a0009a99a521.txt | head -40; echo; echo \"=== etymonline bazaar ===\"; grep -n -i -A6 \"bazaar\" 577a680138a66ff6.txt | head -30",
 "description": "Read bazaar sources"
}
```


### [2026-09-06T22:16:07.350Z] TOOL RESULT

```
=== bazar wiktionary ===
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
--
90: Etymology 
91-
92- 3.2 
93- Noun 
94-
--
115: Etymology 
116-
117- 5.3 
118- Noun 
119-
--
135: Etymology 
136-
137- 6.2 
138- Pronunciation 
139-
--
158: Etymology 
159-
160- 7.3 
161- Pronunciation 
162-
--
181: Etymology 
182-
183- 8.2 
184- Pronunciation 
185-
--
286: Etymology
287- [ edit ] 
288-
289: Etymology tree

=== etymonline bazaar ===
1:URL: https://www.etymonline.com/word/bazaar
2-FETCHED: 2026-09-06T22:16:03Z
3-STATUS: 200
4:TITLE: Bazaar - Etymology, Origin & Meaning
5-
6:Bazaar - Etymology, Origin & Meaning 
7-
8- Search 
9- Log in 
10-
11- Columns 
12- Forum 
--
21: Origin and history of bazaar 
22-
23: bazaar (n.) 
24-
25- 1580s, from Italian bazarra , ultimately from Persian bazar (Pahlavi vacar ) "a market," from Old Iranian *vaha-carana "sale, traffic," from suffixed form of PIE root *wes- (1) "to buy, sell" (see venal ) + PIE *kwoleno- , suffixed form of root *kwel- (1) "revolve, move round; sojourn, dwell."
26- also from 1580s 
27-
28: Entries linking to bazaar 
29-
30- venal (adj.) 
31-
32- mid-15c., "capable of being obtained for a price; that can be corrupted;" 1660s, "offered for sale," from French vénal , Old French venel "for sale" (of prostitutes, etc.; 12c.) and directly from Latin venalis "for sale, to be sold; capable of being bribed."
33-
34- This is from venum (nominative *venus ) "for sale," reconstructed to be from PIE *wes-no- "price," from root *wes- (1) "to buy, sell," source also of Sanskrit vasnah "purchase money," vasnam "reward," vasnayati "he bargains, haggles;" Greek onos "price paid, purchase," oneisthai "to buy."
--
42: alternative spelling of bazaar .
43-
```


## [2026-09-06T22:16:16.976Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && sed -n '280,340p' 1354a0009a99a521.txt",
 "description": "Wiktionary بازار Persian etymology"
}
```


### [2026-09-06T22:16:17.017Z] TOOL RESULT

```
 [ edit ] 

 Arabic Wikipedia has an article on: بازار 

 Wikipedia ar 

 Etymology
 [ edit ] 

 Etymology tree

 Proto-Indo-European *wes- der. 

 Proto-Indo-European *kʷel- der. 

 Middle Persian wʾčʾl 
 Classical Persian بَازَار ( bāzār ) bor. 
 Arabic بازار 

 Borrowed from Classical Persian بَازَار ( bāzār ) .

 Pronunciation
 [ edit ] 

 IPA ( key ) : /baː.zaːr/ 

 Noun
 [ edit ] 

 بَازَار • ( bāzār )  f ( plural بَازَارَات ( bāzārāt ) ) 

 bazaar 

 Iranian traditional marketplace

 Declension
 [ edit ] 

 Declension of noun بَازَار ( bāzār )

 singular

 basic singular triptote 

 indefinite

 definite

 construct

 informal

 بَازَار 
 bāzār 

 الْبَازَار 
 al-bāzār 

 بَازَار 
 bāzār
```


## [2026-09-06T22:16:25.666Z] TOOL CALL #68: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/bazaar\" \\\n \"https://en.wiktionary.org/wiki/%DA%86%D8%A7%D9%84%D8%A7%DA%A9\" \\\n \"https://en.wiktionary.org/wiki/%DA%AF%D8%B2%D8%A7%D8%B1%D8%AF%D9%86\" \\\n \"https://en.wiktionary.org/wiki/%DA%86%D8%A7%D8%B4%D8%AA\" \\\n \"https://en.wiktionary.org/wiki/%DA%A9%D8%A7%D8%B4%D8%AA%D9%86\" ; do\n timeout 120 python3 tools/fetch_source.py \"$u\" --note \"page 290 Kwel/Kwek: node words\" ; done 2>&1 | tail",
 "description": "Fetch Wiktionary word pages"
}
```


### [2026-09-06T22:16:29.739Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/5175d3222a4f3eb6.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d7063b08b4466fe1.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/cd635c8a790b9a90.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/2b5462220414d514.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/8e4ce34b7bdb6859.txt
```


## [2026-09-06T22:16:32.919Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in 5175d3222a4f3eb6 d7063b08b4466fe1 cd635c8a790b9a90 2b5462220414d514 8e4ce34b7bdb6859; do echo \"########## $f\"; grep -n -i -m3 -A12 \"Borrowed from\\|Inherited from\\|From Middle Persian\\|Etymology tree\" $f.txt | head -45; done",
 "description": "Read fetched Wiktionary etymologies"
}
```


### [2026-09-06T22:16:34.749Z] TOOL RESULT

```
########## 5175d3222a4f3eb6
506: Categories : English terms borrowed from Middle French 
507- English terms derived from Middle French 
508: English terms borrowed from Italian 
509- English terms derived from Italian 
510- English terms derived from Ottoman Turkish 
511- English terms derived from Persian 
512- English 2-syllable words 
513- English terms with IPA pronunciation 
514- English terms with audio pronunciation 
515- Rhymes:English/ɑː(ɹ) 
516- Rhymes:English/ɑː(ɹ)/2 syllables 
517- English terms with homophones 
518- English lemmas 
519- English nouns 
520- English countable nouns 
########## d7063b08b4466fe1
297: Borrowed from Classical Persian چالاک ( cālāk ) .
298-
299- Pronunciation
300- [ edit ] 
301-
302- ( Standard Urdu ) IPA ( key ) : /t͡ʃɑː.lɑːk/ 
303-
304- Adjective
305- [ edit ] 
306-
307- چالاک • ( cālāk ) ( Hindi spelling चालाक ) 
308-
309- quick ; speedy 
--
349: Urdu terms borrowed from Classical Persian 
350- Urdu terms derived from Classical Persian 
351- Urdu terms with IPA pronunciation 
352- Urdu lemmas 
353- Urdu adjectives 
354- Urdu nouns 
355- Urdu masculine nouns 
356- Urdu feminine nouns 
357- Urdu nouns with multiple genders 
358- Ushojo lemmas 
359- Ushojo adjectives 
360-
361- Hidden categories: Pages with entries 
########## cd635c8a790b9a90
147: From Middle Persian [Book Pahlavi needed] ( wcʾltn' /⁠wizārdan, wizār-⁠/ , “ to separate; to explain, interpret; to perform, fulfil, redeem ” ) , from Proto-Iranian *wí ( “ apart ” ) + a causative formation from Proto-Iranian *čarH ( “ to come and go, wander ” ) , from Proto-Indo-Iranian *wí + Proto-Indo-Iranian *čálHati ( “ to move, wander ” ) , the prefix ultimately from Proto-Indo-European *wí ( “ apart ” ) . Compare Old Armenian վճար ( včar ) , an Iranian borrowing.
148-
149- Pronunciation
150- [ edit ] 
151-
152- ( Classical Persian ) IPA ( key ) : /ɡu.zaːr.ˈdan/ 
153-
154- ( Dari, formal ) IPA ( key ) : [ɡʊ.zɑːɾ.d̪än] 
155-
156- ( Dari, formal ) IPA ( key ) : [ɡʊ.zɑːɾ.d̪än] 
157- ( Kabuli ) IPA ( key ) : [ɡʊ.zɑːɾ.d̪än] 
158-
159- ( Hazaragi ) IPA ( key ) : [ɡu.zɔːɾ.d̪än] 
--
426: Categories : Persian terms inherited from Middle Persian 
427: Persian terms derived from Middle Persian 
########## 2b5462220414d514
287: Inherited from Middle Persian [Book Pahlavi needed] ( čʾšt' /⁠čāšt⁠/ , “ lunch, meal ” ) . Akin to Old Armenian ճաշ ( čaš ) , an Iranian borrowing.
288-
289- Pronunciation
290- [ edit ] 
291-
292- ( Classical Persian ) IPA ( key ) : /ˈt͡ʃaːʃt/ 
293-
294- ( Dari, formal ) IPA ( key ) : [t͡ʃʰɑːʃt̪] 
295-
296- ( Dari, formal ) IPA ( key ) : [t͡ʃʰɑːʃt̪] 
297- ( Kabuli ) IPA ( key ) : [t͡ʃʰɑːʃt̪] 
298-
299- ( Hazaragi ) IPA ( key ) : [t͡ʃʰɔːʃt̪] 
--
410: Persian terms inherited from Middle Persian 
411: Persian terms derived from Middle Persian 
412- Persian terms with IPA pronunciation 
413- Rhymes:Persian/aːʃt 
414- Rhymes:Persian/aːʃt/1 syllable 
415- Persian lemmas 
416- Persian nouns 
417- Persian terms with quotations 
418- Dari 
419- Persian terms with rare senses 
420- fa:Meals 
421- Urdu terms with IPA pronunciation 
422- Rhymes:Urdu/ɑːʃt̪ 
423- Rhymes:Urdu/ɑːʃt̪/1 syllable 
########## 8e4ce34b7bdb6859
150: From Middle Persian [script needed] ( kyštn' /⁠kištan⁠/ ) — the vowel changed in New Persian under the influence of the present stem [script needed] ( kʾl- /⁠kār-⁠/ ) — from Proto-Iranian *karH- , from Proto-Indo-Iranian [Term?] , from Proto-Indo-European [Term?] . [ 1 ] Compare Ossetian калын ( kalyn , “ to pour ” ) , Central Kurdish کێڵان ( kêllan , “ to plough ” ) , Pashto کرل ( karəl , “ to sow ” ) , Sanskrit किरति ( kirati , “ he scatters ” ) , Latin colere ( “ to cultivate ” ) .
151-
152- Pronunciation
153- [ edit ] 
154-
155- ( Classical Persian ) IPA ( key ) : /kaːʃ.ˈtan/ 
156-
157- ( Dari, formal ) IPA ( key ) : [kʰɑːʃ.t̪ʰán] 
158-
159- ( Dari, formal ) IPA ( key ) : [kʰɑːʃ.t̪ʰán] 
160- ( Kabuli ) IPA ( key ) : [kʰɑːʃ.t̪ʰán] 
161-
162- ( Hazaragi ) IPA ( key ) : [kʰɔːʃ.t̪ʰán] 
--
1044: Categories : Persian terms inherited from Middle Persian 
1045: Persian terms derived from Middle Persian
```


## [2026-09-06T22:16:46.688Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"### bazaar etym\"; grep -n -m2 -B2 -A6 \"Ottoman Turkish\\|bazarra\\|pazar\" 5175d3222a4f3eb6.txt | head -30; echo; echo \"### calak persian\"; grep -n -B3 -A8 \"Persian\" d7063b08b4466fe1.txt | sed -n '1,60p'",
 "description": "bazaar and čālāk etymologies"
}
```


### [2026-09-06T22:16:46.744Z] TOOL RESULT

```
### bazaar etym
213- [ edit ] 
214-
215: From Middle French bazar or Italian bazar , from Ottoman Turkish بازار ( bazar ) , from Persian بازار ( bâzâr ) .
216-
217- Pronunciation
218- [ edit ] 
219-
220- ( UK ) IPA ( key ) : /bəˈzɑː(ɹ)/ 
221-
--
258- Abkhaz: аџьармыкьа ( adžarməkʲʼa ) 
259-
260: Albanian: treg   (sq)   m , pazar   (sq)   m 
261-
262- Amharic: መደብር ( mädäbr ) 
263-
264- Arabic: سُوق   (ar)   m or f ( sūq ) , بَازَار   (ar)   m ( bāzār ) 
265-
266- Armenian: շուկա   (hy) ( šuka ) 

### calak persian
54- Beginning
55-
56- 1 
57: Persian 
58-
59: Toggle Persian subsection 
60-
61- 1.1 
62- Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
--
172-
173- From Wiktionary, the free dictionary
174-
175: Persian
176- [ edit ] 
177-
178- Etymology
179- [ edit ] 
180-
181- Related to چلیدن ( čalidan , “ to walk proudly, saunter ” ) , ultimately from Proto-Indo-European *kʷel- .
182-
183- Pronunciation
184- [ edit ] 
185-
186: ( Classical Persian ) IPA ( key ) : /t͡ʃaː.ˈlaːk/ 
187-
188- ( Dari, formal ) IPA ( key ) : [t͡ʃʰɑː.lɑ́ːk] 
189-
190- ( Dari, formal ) IPA ( key ) : [t͡ʃʰɑː.lɑ́ːk] 
191- ( Kabuli ) IPA ( key ) : [t͡ʃʰɑː.lɑ́ːk] 
192-
193- ( Hazaragi ) IPA ( key ) : [t͡ʃʰɔː.lɔ́ːk] 
194-
--
226- c. 1260 , Saʿdī , “Ghazal 70”, in دیوان سعدی [ The Divān of Saʿdī ]‎ [1] : ای که از سرو روان قد تو چالاکترست
227-دل به روی تو ز روی تو طربناکترست ay ki az sarw-i rawān qadd-e tu čālāktar ast
228-dil ba rōy-i tu zi rōy-i tu tarabnāktar ast O you whose stature is nimbler than the swaying cypress,
229:Thanks to your face, my heart has more delight than [even] your face. (Classical Persian transliteration) 
230-
231- clever ; smart 
232- Synonym: زرنگ ( zerang ) 
233-
234- Descendants
235- [ edit ] 
236-
237- → Ahirani: चलाक ( calāk ) 
--
294- Etymology
295- [ edit ] 
296-
297: Borrowed from Classical Persian چالاک ( cālāk ) .
298-
299- Pronunciation
300- [ edit ] 
301-
```


## [2026-09-06T22:16:58.506Z] TOOL CALL #71: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('data/verification/page-259.json'))\nprint(json.dumps(d['entries'][0],ensure_ascii=False,indent=1)[:3500])\n\"",
 "description": "Sample prior verification file"
}
```


### [2026-09-06T22:17:00.279Z] TOOL RESULT

```
{
 "entry": 0,
 "root": "Kerd 1, Kred",
 "verdict": "confirmed",
 "modern_form": "PIE *ḱḗr, oblique stem *ḱr̥d- (root *ḱerd-) 'heart'; with the compound *ḱred-dʰeh₁- 'to place one's heart, trust'",
 "note": "Pokorny p.579 bottom–580 heads the entry exactly '(kered-:) kerd-, kērd-, kr̥d-, kred- ‘Herz’', so Nourai's headword 'Kerd 1, Kred', the language label 'Indo-European' and the gloss 'heart' all reproduce his source correctly; AHD (Watkins) has 'kerd-1. Heart. [Pok. kered- 579.]'. The one substantive caveat concerns the 'kred-' half: Pokorny himself (p.580) says the kred-dhē- 'believe' group is 'nicht hierher' (not to be connected with 'heart'), and Buck 17.15, Klein s.v. heart and Ernout–Meillet s.v. cor agree; modern standard works (Watkins/AHD, de Vaan 2008 s.v. crēdō, Wiktionary) do connect it, analysing *ḱred-dʰeh₁- as 'to place one's heart'. Nourai therefore follows the newer, now dominant, view — but not the page of Pokorny he cites. The Iranian branch has a further complication that the chart passes over: Indo-Iranian shows a voiced aspirate initial (Skt. hṛd-, Av. zərəd-, PII *ȷ́ʰā́rd) where *ḱ- is expected, 'unexplained voiced aspiration' (Wiktionary), 'mit init. as if fr. IE gh, due to a blend with some other word' (Buck 251).",
 "note_fa": "ریشهٔ هندواروپایی آغازین *ḱḗr (ستاک غیرفاعلی *ḱr̥d-، ریشهٔ *ḱerd-) به معنی «دل، قلب» است و پوکورنی در ص ۵۷۹–۵۸۰ سرواژه را دقیقاً «kerd-, kērd-, kr̥d-, kred-: Herz» آورده؛ پس نام ریشه، برچسب زبانی و معنایی که نورایی داده درست است. تنها نکتهٔ محل بحث بخش kred- است: خودِ پوکورنی در ص ۵۸۰ پیوند kred-dhē- «باور داشتن» را با «دل» رد می‌کند و باک و کلاین و ارنو–مه‌یه نیز همین نظر را دارند، اما واتکینز (AHD)، دِ وان و ویکی‌واژه آن را می‌پذیرند و *ḱred-dʰeh₁- را «دل نهادن» می‌دانند؛ یعنی نورایی از دیدگاه نو پیروی کرده است نه از صفحه‌ای که به آن ارجاع داده. نکتهٔ دیگر آنکه در هندوایرانی به جای *ḱ- انسدادی واکدارِ دمیده دیده می‌شود (سنسکریت hṛd-، اوستایی zərəd-) که هنوز توضیح قطعی ندارد.",
 "sources": [
  "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%E1%B8%B1%E1%B8%97r",
  "https://en.wiktionary.org/wiki/credo%23Latin",
  "https://www.etymonline.com/word/heart"
 ],
 "ref_check": [
  {
   "ref": "POK:579",
   "status": "supports",
   "note": "Pokorny IEW p.579 (bottom) – 580, read in POK_02.txt leaf 239–240 (awk 'BEGIN{RS=\"\\f\"} NR==239'): '(kered-:) kerd-, kērd-, kr̥d-, kred- ‘Herz’. Arm. sirt … gr. καρδία (att.), κραδίη (hom.) … lat. cor (aus *cord) … got. hairto, ahd. herza, ags. heorte, anord. hjarta n. ‘Herz’ (*ḱērd-on-)'. Exactly Nourai's root name and gloss."
  },
  {
   "ref": "SYN:251",
   "status": "supports",
   "note": "Buck, Selected Synonyms p.251 = §4.44 HEART (SYN.txt leaf 289, page number '251' printed in the running head above '4.44 HEART'): 'Most of the words for ‘heart’ belong to an inherited group … 1. IE *ḱerd-, etc., with gradation. Walde-P. 1.423 ff. Ernout-M. 219 f.'"
  }
 ],
 "consulted": [
  {
   "src": "AHD",
   "where": "Watkins 1985, s.v. kerd-1 (AHD_watkins1985.txt line 621)",
   "stance": "supports",
   "note": "'kerd-1. Heart. 1. Suffixed form *kerd-en- in Germanic *hertōn- in Old English heorte, heart: HEART. 2. Zero-grade form *kr̥d- in: a. Latin cor (stem cord-), heart … b. suffixed form *kr̥d-yā in Greek kardia … 3. Possibly *kred-dhə-, “to place trust” … in Latin crēdere, to believe. [Pok. kered- 579.]' — the whole chart in one entry."
  },
  {
   "src": "WLD",
   "where": "Walde-Pokorny I 423 f. (cited by POK and by Buck 4.44; only Ban
```


## [2026-09-06T22:17:10.281Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### KLN bazaar\"; grep -n -m2 \"^bazaar\" KLN_1966.txt | head -3; grep -o \"bazaar,[^|]\\{0,320\\}\" KLN_1966.txt | head -3; echo; echo \"### SKT bazaar\"; grep -o \"BAZAAR[^|]\\{0,300\\}\\|bazaar,[^|]\\{0,300\\}\" SKT.txt | head -3; echo; echo \"### LKT bazar\"; grep -n -m3 \"bazar\\|Bazar\" LKT.txt | head -6",
 "description": "Klein/Skeat/Lokotsch bazaar"
}
```


### [2026-09-06T22:17:12.293Z] TOOL RESULT

```
### KLN bazaar
4585:bazaar
bazaar,  n.,  a  market  place.  —  Ult.  fr.  Pers.  bazar.

### SKT bazaar

### LKT bazar
817:'Markt'  [Horn  NpEt  S.  38,  Nr.  166].  Das Wort  wurde  im  17.  Jahrhundert  durch Reisende  zunächst  mit  Bezug  auf  orien- talisi-he  Verhältnisse  eingeführt  und  drang dann,  vor  allem  auch  durch  die  Kennt- nis von  1001  Nacht,  in  alle  europäischen Sprachen  ein:  frz.  pg.  sp.  bazar,  it.  ba- zar,  bazzar,  rum.  bazar,  basar;  russ. bazar,  bulg.  serb.  pazar,  cech.  poln. bazar;  eng\. bazar,  bazaar,  ndl.  bazaar, dtsch.  Bazar.  Da  das  Grundwort  stimm- haftes s  [z]  hat,  gehört  sicherlich  auch it.  bazzarare  'täuschen,  betrügen',  siz. bazzariotu  'Betrüger'  hierher  [gegen ML  1010].  [Gorjajew  9.  Kluge  42.  DE GREGORIO  in  ZfromPh  XXV,  747. GrSVociSic  228.
2413:1011.  Ar.  kaisärija: 'Ladenreihe,  Bazar'  (noch  jetzt  in  Da- maskus und  Beirtit  Bezeichnung  der großen  Karawanserais,  vom  gr.  Adj. Kaiaapeia,  d.  h.  der  'kaiserliche',  sc. Markt,  vgl.  Dozy  Suppl  II,  432] ;  hieraus sp.  alcaiceria,  alcaeceria,  pg.  alcaqarias, kat.  (alt)  alcaceria  'die  Waren,  die  im Bazar  verkauft  werden'  [DE  76].
6356:bazar  278
```


## [2026-09-06T22:17:15.187Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '812,820p' LKT.txt",
 "description": "Lokotsch bazar entry head"
}
```


### [2026-09-06T22:17:15.247Z] TOOL RESULT

```
275.  Tk.  batrak:
[Nicht  osm.,  sondern  tat.]  'Arbeiter': hieraus  russ.  batrak,  batraöka  'Arbeiter, Knecht;  Arbeiterin, Magd'.  [Gorjajew  13.
276.  Ar.  batta: Einheitsnomen  zu  baft  'Enten'  [aus  pers. bat  'Ente'  Horn  NpEt  S.  51,  Nr.  226] ; hieraus  sp.  pg.  pato,  pata  'Ente',  pg. patinho  'junge  Gans';  pg.  pato  'leicht zu  betrügender  Mensch'  [Constancio Dicc  752  b;  schon  npers.  här-bäf  'Idiot' Horn  a.  a.  0.].
277.  Ar.  bazaga:
'Sich  rühmen'.  Von  diesem  Stamme, vielleicht  von  einem  ar.  Adj.  *bazgän, kommt  siz.  baggianu  'eitel,  dünkelhaft' und  it.  albagia  'Eigendünkel',  Adj.  al- bagioso.    [GrSVociSic  228.
'Markt'  [Horn  NpEt  S.  38,  Nr.  166].  Das Wort  wurde  im  17.  Jahrhundert  durch Reisende  zunächst  mit  Bezug  auf  orien- talisi-he  Verhältnisse  eingeführt  und  drang dann,  vor  allem  auch  durch  die  Kennt- nis von  1001  Nacht,  in  alle  europäischen Sprachen  ein:  frz.  pg.  sp.  bazar,  it.  ba- zar,  bazzar,  rum.  bazar,  basar;  russ. bazar,  bulg.  serb.  pazar,  cech.  poln. bazar;  eng\. bazar,  bazaar,  ndl.  bazaar, dtsch.  Bazar.  Da  das  Grundwort  stimm- haftes s  [z]  hat,  gehört  sicherlich  auch it.  bazzarare  'täuschen,  betrügen',  siz. bazzariotu  'Betrüger'  hierher  [gegen ML  1010].  [Gorjajew  9.  Kluge  42.  DE GREGORIO  in  ZfromPh  XXV,  747. GrSVociSic  228.
279.  Ar.  bazrn-katünä:
Aus  ar.  bazr  'Samen'  und  katünä  [wohl pers.  Ursprungs;  ar.  auch  kasisa  al- bar  gut,  d.  h.  'Flohkraut']  'Flohkraut, Plantago  psyllium'.  Hieraus  sp.  zara- gatona,  pg.  zaragatoa,  zaragota  'Fioh- kraut'.    [DE  365.
280.  Ar.  bazz:
```


## [2026-09-06T22:17:25.068Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\np='incoming/WLD/WLD_Bd1_pages.txt'\nt=open(p,encoding='utf8',errors='replace').read()\npg=t.split('\\f')\nprint('leaves',len(pg))\n# find printed 510 / 514\nfor i,q in enumerate(pg):\n    if re.search(r'(?m)^\\s*51[0-9]\\b',q[:300]):\n        print('leaf',i,'head',q[:80].replace('\\n',' '))\nEOF",
 "description": "Locate Walde-Pokorny Bd I pp.510-515"
}
```


### [2026-09-06T22:17:26.913Z] TOOL RESULT

```
leaves 895
leaf 518 head                                                                 -     510       
leaf 522 head                           i                                                     
leaf 526 head
```


## [2026-09-06T22:17:30.112Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for L in 518 519 522 523; do echo \"=== leaf $L ===\"; awk -v n=$L 'BEGIN{RS=\"\\f\"} NR==n+1' incoming/WLD/WLD_Bd1_pages.txt | head -25; done",
 "description": "WLD I 510-515"
}
```


### [2026-09-06T22:17:31.678Z] TOOL RESULT

```
=== leaf 518 ===
                                                                -




510                                            q'^eie               q“ek-, q“ok, q“ek-s-


   Av. hay-, cuyeiti, cmvaiti „ Megere) aussuchen, wahlen mit vi- „scheiden,                                    -
                                                                                                                    '




distinguere“,   mit ham- „colligere, (Schrittlangen aneinander legen"; np.
cidan „sammeln‘                :
                       Gr. nodco ,.mache“ (arg.-boot. euoifqos u. dgl.), dann
                                   .



auch ..dichte", Denominativ eines *7ioi-i6-g „aufbauend, machend" (vgl.
doro-Tioiog ,, Backer"). Abg. cim (wahrscheinlich «-St. ai. cino-ti, av. cinv-                              ;


=== leaf 519 ===
                                                                                                                                   ;




                                                                   q”et-, q“at-                                              511


Lex. 3 0 f. *xexxpag -pcov mit gr. xx = ap .-ks-) s. dann Brugmann-Thumb
           1         :
                                             ,


GrGr. 4 114 (BthlWfklPh. 1902, 630 erwagt Wechsel zw. Formans mit und
ohne s wie zwischen ai. bhnnd-h und bhtsma-Jt).
  Mit tonendem Aualaut aksl. kazq, kazati „zeigen, mahnen", u-kazz „an6-
dei£is“ (auch kaznz „S6yjua , Anordnung: xipcogia, Strafe"? s. Berneker 496 f.),
wohl idg. *q?cg- neben *q'ick- (vgl *deik- *deig- ,.zeigen"); fiir einen Ansatz:




q'iogh- mit gh will Petersson Stud, zu Fortunatovs Regel 69 ai. cniha-m
„Zeichen, Merkmal" anfiihren, doch tritt vor i = > in isolierten Worten
keine Palatalisierung ein.
=== leaf 522 ===
                          i                                                                              n



514                                                                  q“em — quel-

                                                        11
q'Aeni „schliirfen, schlucken                                .




        camati und camati „schliirft“, u-camati „schliirft (Wasser) ein, spiilt
      Ai.
sich den Mund aus“, ptc. dcanta-, camasd-h „Trinkschale, Becher“, cumu-h
„Schussel ‘; np. rant „das Essen 11 cnmtdan „trinken“, osset. cunnin „sch]iirfen“;
                                                                 ,
                              *
nisi, hvima (aus *hvnma, idg. q't.cmu = ai. camati) „verschlucken, verschlingen
                                                                                11
                                                                                                                                              ,



hvOma f. „Speiserohre, Schlund“; arm. khim-lh pi. „faux, guttur                                                            11
=== leaf 523 ===
                                                -




Hes. ob mit y aus (jovy.oXog
       ;
                                            =
                                 cymr. usw. bugail, sofern diese aus q'iolos
mit Entlabialisierung nach m? s. dariiber u. qel- „treiben“), nolevay „bewege
                                                                                                  11
mich herum“, ji.yijv „pfluge um“, jon. att. emnoXrjs „auf der Oberflache
(nieht zu *pela- „breit und flach“), hellenist. enmob] „Oberflache“, cpir.
ImnoXa, sonst. emnXa, hunXoa „Geratschaften“, lunoXr\ „Handelsware“,
IpnoXolo „handle“; n coMo/iai „bewege mich an einem Orte herum, korame
haufig hin“; nafov „zuriick“ (Acc. eines *ndXig „Wendung“, Solmsen BPhW.
1906, 755); xvxXog s. u. die gr. jr-Formen enthalten wohl z. T. idg .pel- s. u.
                              ;



  Lat. colo, -ere „treiben, bebauen, bewohnen; hegen und pflegen; ehren;
colonus ,,Landwirt, Bauer“, incolere „bewohnen“, incola „Einwohner“, in-
                                                             :!
quilinns „Insasse“, JExquiliae „Au8ensiedlungen                   .
```


## [2026-09-06T22:17:42.476Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for L in 522 523 524; do echo \"=== leaf $L ===\"; awk -v n=$L 'BEGIN{RS=\"\\f\"} NR==n+1' incoming/WLD/WLD_Bd1_pages.txt | grep -n -i \"caxra\\|carati\\|karsu\\|karsa\\|calati\\|cakra\\|q.el-\" | head -12; done; echo \"=== p.510 kwek material ===\"; awk 'BEGIN{RS=\"\\f\"} NR==518' incoming/WLD/WLD_Bd1_pages.txt | tail -20",
 "description": "WLD kwel material"
}
```


### [2026-09-06T22:17:44.304Z] TOOL RESULT

```
=== leaf 522 ===
5:514                                                                  q“em — quel-
48:qSel- ,,drehen, sich drehen“   (cficlo-s, q'iolo-s, q'ic-q’ilo „Rad, Drehpunkt“),
=== leaf 523 ===
47:    ai. cakrd- m., plur. cakra (dazu nachved. sg. caked- n., Meillet IF. 5, 334)
49:„Wagenrad, Scheibe, Kreis“, av. caxra- m. „Rad“, gr. xvy.Xog „Kreis“, pi.
=== leaf 524 ===
=== p.510 kwek material ===
                                                              ,




       lei- ,.aufscliiohten"; daher ..aufhaufen, sammeln", ,,der Ordnung nach
        auf oder zu einander legen". ..aufbauen", abgeschwiicht „machen“.
   Ai. cinoti,                 cciynti
                        schichtet. reiht: sammelt, hiiuft an; ftigt zusammen.
                                             ,




baut auf". cdya-h     ..Anhaufung, Haufe, Aufwurf"; laya-h „Leib, Korper"
(eig.. ,,*Gliederbau": oder *,.Masse"?): ritd „Schiclit, HolzstoB, Scheiter-
haufen",              cit>-li      f.    ..Anhaufung. Schicht. Sehichtung. Scheiterhaufen --               .   clit-h   f.

,.das      Sammeln".
```


## [2026-09-06T22:17:49.421Z] TOOL CALL #77: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '8815,8830p' SNS_pages.txt; echo \"---- index line ----\"; sed -n '16050,16060p' SNS_pages.txt",
 "description": "SNS kištan entry"
}
```


### [2026-09-06T22:17:49.475Z] TOOL RESULT

```
                                                                         UiVb, 768)drogha-
                                                                                           *#**•*- drauga-/ draoja-:
                                                                                                 ••


                                                                                                                                               &
                                                                                            (Mir. Man. Ill, 54 > drwg
                                                                                                                      :                       ^
                                                                                      •(   kist: jl owlja*,)            af rkiltan:
                                                                                                                 ltfa                     »>e*UJ^
                                                                           •VH^.Ui^.458)krstay:              .^^ Karita               _   ,
                                                                                                                                              fc




---- index line ----
                                                             kust 217/19            raanad 211/4
kardag kardag 213/24      kirfag 216/11                      kustag 217/22          mSnbad 240/4
kardan 217/16            kirfag handOzIh 81/19-              kustlg 218/1           manbadan 240/7
kard baved 266/2           216/14                            ku-I 87/17-195/6       raandag 241/3
kard Isted 266/3         kirfaglh 216/17                     kusad 218/4            m3ndag garzldan     24]
kark 214/8               kirfag kardan 216/16                ku-Ian 87/18           manSd 211/7
karkis/karkas 214/9      kirfag kunisnlh 216/15              kust 218/5-277/14      manSnd 211/6
kas 29/17                kistan 220/6                        kustar 218/9           man I atasan 240/2
kasan 30/1               kOdak 216/18                        kustan 277/17          mansr 240/11
kas-iz 30/3              kGf 216/8
                                                                                    mansraspand 240/15
```


## [2026-09-06T22:17:59.619Z] TOOL CALL #78: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -o \"q[ṷvu]eqlos[^|]\\{0,200\\}\\|kʷekʷlos[^|]\\{0,200\\}\\|qṷeqṷlos[^|]\\{0,200\\}\" IEC.txt | head -5; echo \"---\"; grep -n -o \"caxra[^|]\\{0,160\\}\" IEC.txt | head -5; echo \"--- kwek ---\"; grep -n -o \"q[ṷvu]e[kq]os[^|]\\{0,180\\}\\|casman[^|]\\{0,160\\}\" IEC.txt | head -6",
 "description": "Mann IEC lookups"
}
```


### [2026-09-06T22:18:01.352Z] TOOL RESULT

```
---
--- kwek ---
```


## [2026-09-06T22:18:05.516Z] TOOL CALL #79: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -o \"cakra-[^|]\\{0,160\\}\" IEC.txt | head -4; echo \"===\"; grep -n -o \"qelō\\|qelos\\|qelō-\\|qelo-[^|]\\{0,120\\}\" IEC.txt | head -6; echo \"=== eye/wheel headwords ===\"; grep -n \"^qel\\|^qeqlos\\|^qeklos\\|^qekos\\|^qeks\" IEC.txt | head -10",
 "description": "Mann IEC alternate spellings"
}
```


### [2026-09-06T22:18:07.227Z] TOOL RESULT

```
===
=== eye/wheel headwords ===
```


## [2026-09-06T22:18:13.194Z] TOOL CALL #80: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && head -c 600 IEC.txt; echo; echo \"===\"; grep -c \"\" IEC.txt; grep -n -o \"q.eqlos\\|q.el-\\|q.ekos\\|q.ek-\" IEC.txt | head -10",
 "description": "Inspect IEC file"
}
```


### [2026-09-06T22:18:13.276Z] TOOL RESULT

```
Stuart E. Mann AN INDO-EUROPEAN COMPARATIVE DICTIONARY
AN INDO-EUROPEAN COMPARATIVE
DICTIONARY
BY STUART E. MANN
 
HELMUT BUSKE VERLAG HAMBURG 1984/87
Fasc. Fasc. Fasc. Fasc. Fasc. Fasc. Fasc. Fasc. Fasc.
Fasc. Fasc.
We regret the death of our author
Mr. Stuart Edward Mann
who died, aged 81, on August 5, 1986
1. 1984. XIV, 1-132 (a-dår)
2 1984. 133-292 (dario-grembhos
3. 1985. 293-452 (greng-josmn)
4. 1985. 453-612 (1osquis-Krn)
5. 1985. 613-772 (Keros-mitros
6. 1986. 773-932 (mitsos-poti)
7. 1986. 933-1092 (potrajo-roudhros)
8. 1986. 1093-1252 (roust-spéis)
9. 1986. 1253-1412 (speK-t
===
20499
6944:quel-
6961:quel-
7573:quel-
13926:quek-
13926:quek-
13927:quel-
13928:quel-
13929:quel-
13930:quel-
13931:quel-
```


## [2026-09-06T22:18:15.552Z] TOOL CALL #81: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '13920,13940p' IEC.txt",
 "description": "Mann quek/quel entries"
}
```


### [2026-09-06T22:18:15.600Z] TOOL RESULT

```
(queiolos, see queilos)
quëið (quii-) (1) ‘watch, wait, care, hope’. Skt. Cayami, v. ‘perceive, recognize, revere’; Av Ci-, v. ‘watch, seek"; (o-gde in) kaya, 1sg. ‘wish, long’; Gk. cf. tē- in te-meléo"'care for’; ai-témi, -téo ‘request’; Ir. cím, usu. do-chím, cpd. ‘see’; OCS Cajo, -ati, v. “hope, expect; cf. ne-čaj, m. ‘despair’; po-Cajo, -ati, v. ‘allow’; Pol. czaić się na ‘lurk for’; R cf. ot-čajanije ‘despair’; Slovene cf. čaja, f. ‘hope’
quëið (quii-) (2) ‘punish’
Skt. Cave, mp. ‘avenge, punish’; Gk. tío, id. queios (quiios, quios) ‘whose’. Cf. quoios as
1023
a separate entry. WP I, 509 Alb. cf. kuj, dat. ‘to whom; i kuji, f: e kuja ‘whose’; Lat. cuius beside quius ‘whose’; OCS (and com. Sl.) čij, adj. ‘whose’; Cz. čí, id.; cf. Cretan o-teios, Boeot. ho-tios, id. (cpd.) and (formally) OS hwiu, hwi, adv. ‘how, why”
queks- “tip, point, end, edge, goad'. Cf. WP I, 382, 398, 428 & 510. (Var: quek-) Gk. cf. ték-mar, Hom. ték-mor, n. *end, object, limit” (*queks- or *quek-); Alb. cekë, f. *deci- sion; top leaves of tobacco-plant'; Ir. cf. ceacht, m. “top, eminence’; Slovene cf. cehati, v. “poll, top’; cf. Cz. Čech, m. (‘Czech’, lit. *borderlander'?); Li. keksis, gs: -io, m. ‘poker’; Latv. keksis “poker; boathook'. (Isophones: Av. Cakus ‘ballistic ball, putting-weight'; Caku- sa ‘discus’; Oss. cág “hoop, link, ring; W pegwn ‘pivot; peg ‘expander; eight-bushel ‘measure’)
quel- radical of general sense ‘turn; go’. See following entries
quël-, long-grade of quel- in Alb. solla, aor. ‘I turned’; W (ambig.) pill, pl. -ion, m. ((1) ‘pivot, turning post, In sense ‘shaft, stem" see quil-); pil, pl. -iau, f. “hov- erer’; R Cal, pri-čal, m. ‘moorings’; Calit, v. ‘moor’; Li. cf. kelikas *ferryman'; Latv. celejs, id. See following entries
quéle- ‘far’. WP I, 517 Skt. cf. Caramáh ‘farthest’; Gk. cf. t&le, teloü, Aeol. pelui “far”, pél-ethron, n. (/pitch, course’, fr. *quel-guedhro-) (infl. of pélomai, polos, etc.); W. Br. Cor. pell ‘far’; W pell-af (farthest, fr. *quelio-?)
quel-énom 'turning, bend, knee'. (Balto- Slav) OCS (and com. Sl.) koléno ‘knee’; Li. kelenas *knee; patella'
quelotrom (quelostr-) (turn, change, ex- change, requital'. See quel- Gk. cf. télestra, npl. 'admission-fees to priest- hood'; W paladr, pl. pelydr, m. “axis; stem; shaft; beam; ray?
quelmn- ‘turn, roll; roller, cylinder’. WP II, 599 Skt. Cáranam, n. *wandering; ritual; conduct'; Oss. cf. cur, curi, curmä, adv. “about, near’; Alb. cf. e siellme, f. ‘turn, revolution; OCS
queks- — quelpo
20
25
30
35
40
45
1024
```


## [2026-09-06T22:18:23.334Z] TOOL CALL #82: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -o \"quequlos[^|]\\{0,300\\}\\|quequlom[^|]\\{0,300\\}\\|queqlos[^|]\\{0,300\\}\" IEC.txt | head -4; echo \"===\"; grep -n -o \"quelos[^|]\\{0,250\\}\" IEC.txt | head -4",
 "description": "Mann wheel entry"
}
```


### [2026-09-06T22:18:25.181Z] TOOL RESULT

```
13974:quequlos, ququlos, à, om ‘turning, wheel, rim’. WP I, 515, cf. quelo, quolos Skt. Cakráh, am. mn. *wheel'; Av. cakram, n. id.; Per. Cakle ‘district’; Garg ‘wheel; ball; vault of sky’; Carxe ‘wheel, reel; Oss. Cil, Dig.: kelä ‘felloe of wheel’; Gk. cf. péplos, m. (robe; woven cloth’, if fr. *quequlos) beside
13982:quequlos, ququlos, à, om — querqueros
===
493:quelos), and Cz. (ambig.) úkol ‘task’
3677:quelos, ieuos, etc.
13931:quelostr-) (turn, change, ex- change, requital'. See quel- Gk. cf. télestra, npl. 'admission-fees to priest- hood'; W paladr, pl. pelydr, m. “axis; stem; shaft; beam; ray?
13944:quelos, -es- ‘turn, turning’. Cf. quel-, queló, quolos, etc. WP I, 514 Skt. cf. Calab, čarab, adj. ‘mobile’; Ober, cf. abi-Cari$ (^pasture', fr. *mbhi-^); Oss. cf. (*-e-) car, S. “ceiling, vaulting’; Arm. Keyi, gs: -vo, ab. s. -eav ‘shaft, pole, rudder, he
```


## [2026-09-06T22:18:34.568Z] TOOL CALL #83: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -o \"caxra[^|]\\{0,120\\}\\|θard[^|]\\{0,60\\}\" KNT.txt | head -5; echo \"=== kar in KNT ===\"; grep -n -o \"kar-[^|]\\{0,100\\}\" KNT.txt | head -5",
 "description": "Kent Old Persian lexicon"
}
```


### [2026-09-06T22:18:36.529Z] TOOL RESULT

```
=== kar in KNT ===
565:kar-.
606:kar- ‘do, make’. The correspond- ing Skt. forms, in the 3d sg. impf., are amriyate, abhriyale, akriyaie;
606:kar- cannot have this vocalism, since the product would be *azriya-. In this verb then there was in thes
935:kar- ‘make, do’; and this peculiar development is rather to be attributed to the influence of other verb
1254:kar- ‘make, do’, OP pres. kunautzy, imf. pass. akariya, züra-kara- ‘evil-doer’; but *ker- in pres. inf.
```


## [2026-09-06T22:18:49.856Z] TOOL CALL #84: Bash

```json
{
 "command": "ls site/pages/290.jpg 2>/dev/null; timeout 300 pdftoppm -f 290 -l 290 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg290 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/",
 "description": "Render PDF page 290"
}
```


### [2026-09-06T22:18:51.863Z] TOOL RESULT

```
site/pages/290.jpg
total 117896
drwx------ 4 sfmqrb sfmqrb     4096 Sep  6 18:18 .
drwx------ 4 sfmqrb sfmqrb     4096 Sep  6 16:32 ..
-rw-rw-r-- 1 sfmqrb sfmqrb   533122 Sep  6 17:21 afm41_a.png
-rw-rw-r-- 1 sfmqrb sfmqrb   508509 Sep  6 17:21 afm41_b.png
-rw-rw-r-- 1 sfmqrb sfmqrb   969829 Sep  6 17:21 afm41.png
-rw-rw-r-- 1 sfmqrb sfmqrb  1322100 Sep  6 17:20 afm46.png
-rw-rw-r-- 1 sfmqrb sfmqrb   416305 Sep  6 17:20 afm46_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb      748 Sep  6 18:13 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  5157031 Sep  6 18:05 aiw.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    76489 Sep  6 17:24 bqt1237_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   127656 Sep  6 18:17 bqt1267_foot_p294.png
-rw-rw-r-- 1 sfmqrb sfmqrb   362419 Sep  6 17:50 bqt1583_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   456331 Sep  6 16:54 bqt1594_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   105420 Sep  6 18:16 bqt27.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2824 Sep  6 16:59 bqt83_head.png
-rw-rw-r-- 1 sfmqrb sfmqrb   703015 Sep  6 17:50 bqt_fn4.png
-rw-rw-r-- 1 sfmqrb sfmqrb   299015 Sep  6 17:50 bqt_fn.png
-rw-rw-r-- 1 sfmqrb sfmqrb   325427 Sep  6 17:50 bqt_n552.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   315487 Sep  6 17:50 bqt_n553.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   330101 Sep  6 17:50 bqt_n554.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   560485 Sep  6 17:53 bqtv2_650_s.png
-rw-rw-r-- 1 sfmqrb sfmqrb   541712 Sep  6 17:53 bqtv2_651_s.png
-rw-rw-r-- 1 sfmqrb sfmqrb   729454 Sep  6 17:53 bqtv2_n650.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   702551 Sep  6 17:53 bqtv2_n651.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   100817 Sep  6 17:36 bqt_v3_111.png
-rw-rw-r-- 1 sfmqrb sfmqrb   110820 Sep  6 17:36 bqt_v3_112.png
-rw-rw-r-- 1 sfmqrb sfmqrb    91526 Sep  6 16:59 bqt_v3_83.png
-rw-rw-r-- 1 sfmqrb sfmqrb   137595 Sep  6 18:10 buck2.txt
-rw-rw-r-- 1 sfmqrb sfmqrb      146 Sep  6 18:10 buck3.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    64531 Sep  6 16:53 build261.py
-rw-rw-r-- 1 sfmqrb sfmqrb    60498 Sep  6 17:11 build269.py
-rw-rw-r-- 1 sfmqrb sfmqrb    97300 Sep  6 17:16 build270.py
-rw-rw-r-- 1 sfmqrb sfmqrb    52615 Sep  6 17:36 build275.py
-rw-rw-r-- 1 sfmqrb sfmqrb    74145 Sep  6 17:43 build278.py
-rw-rw-r-- 1 sfmqrb sfmqrb    72342 Sep  6 17:58 build283.py
-rw-rw-r-- 1 sfmqrb sfmqrb     5043 Sep  6 17:05 c1.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3501 Sep  6 17:05 c2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    56424 Sep  6 17:05 c3.png
-rw-rw-r-- 1 sfmqrb sfmqrb    78058 Sep  6 17:05 c4.png
-rw-rw-r-- 1 sfmqrb sfmqrb 60831599 Sep  6 18:01 cad_k.pdf
-rw-rw-r-- 1 sfmqrb sfmqrb  2530822 Sep  6 18:01 cad_k.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    37980 Sep  6 17:16 c_av.png
-rw-rw-r-- 1 sfmqrb sfmqrb    29703 Sep  6 17:16 c_cros.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1174 Sep  6 17:16 c_empty.png
-rw-rw-r-- 1 sfmqrb sfmqrb    95615 Sep  6 16:39 coord_pg262.png
-rw-rw-r-- 1 sfmqrb sfmqrb  8373934 Sep  6 18:09 cpd.pdf
-rw-rw-r-- 1 sfmqrb sfmqrb   378445 Sep  6 18:09 cpd.txt
-rw-rw-r-- 1 sfmqrb sfmqrb     4560 Sep  6 16:39 crop_ak2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4014 Sep  6 16:39 crop_ak.png
-rw-rw-r-- 1 sfmqrb sfmqrb    25373 Sep  6 16:42 crop_alk.png
-rw-rw-r-- 1 sfmqrb sfmqrb    24852 Sep  6 17:04 crop_fr269.png
-rw-rw-r-- 1 sfmqrb sfmqrb    43238 Sep  6 16:55 crop_germ269.png
-rw-rw-r-- 1 sfmqrb sfmqrb    51654 Sep  6 17:04 crop_gk269.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2585 Sep  6 17:05 crop_gk271.png
-rw-rw-r-- 1 sfmqrb sfmqrb    64142 Sep  6 17:02 crop_gr267.png
-rw-rw-r-- 1 sfmqrb sfmqrb     6411 Sep  6 16:39 crop_gr.png
-rw-rw-r-- 1 sfmqrb sfmqrb    23559 Sep  6 16:42 crop_kohul.png
-rw-rw-r-- 1 sfmqrb sfmqrb    59386 Sep  6 16:39 crop_lat2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    51357 Sep  6 16:55 crop_latin269.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4761 Sep  6 16:39 crop_lat.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3974 Sep  6 16:37 crop_me2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3300 Sep  6 16:37 crop_me.png
-rw-rw-r-- 1 sfmqrb sfmqrb    10236 Sep  6 16:39 crop_op2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4935 Sep  6 16:37 crop_op.png
-rw-rw-r-- 1 sfmqrb sfmqrb     5599 Sep  6 16:37 crop_pers.png
-rw-rw-r-- 1 sfmqrb sfmqrb    22007 Sep  6 17:10 crop_sak.png
-rw-rw-r-- 1 sfmqrb sfmqrb     5110 Sep  6 17:10 crop_sax.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4854 Sep  6 17:10 crop_shekar.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1249 Sep  6 17:05 crop_sirish.png
-rw-rw-r-- 1 sfmqrb sfmqrb    30419 Sep  6 17:02 crop_skt267.png
-rw-rw-r-- 1 sfmqrb sfmqrb    10043 Sep  6 16:58 crop_slav.png
-rw-rw-r-- 1 sfmqrb sfmqrb    24463 Sep  6 16:58 crop_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb  2144625 Sep  6 17:55 dmmpp.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    31044 Sep  6 17:50 e0.json
-rw-rw-r-- 1 sfmqrb sfmqrb    17126 Sep  6 17:54 e1.json
-rw-rw-r-- 1 sfmqrb sfmqrb    18004 Sep  6 17:56 e2.json
-rw-rw-r-- 1 sfmqrb sfmqrb  5301166 Sep  6 17:01 ediv.pdf
-rw-rw-r-- 1 sfmqrb sfmqrb  1773345 Sep  6 17:01 ediv.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  1845041 Sep  6 18:04 gharib.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  3698758 Sep  6 17:50 IEC_full_djvu.txt
-rw-rw-r-- 1 sfmqrb sfmqrb      228 Sep  6 16:34 jscheck.js
-rw-rw-r-- 1 sfmqrb sfmqrb     4265 Sep  6 17:53 kapi_script.png
-rw-rw-r-- 1 sfmqrb sfmqrb   944060 Sep  6 18:06 kent_full.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   288525 Sep  6 18:07 kent_n222.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   285652 Sep  6 18:07 kent_n223.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   282304 Sep  6 18:07 kent_n224.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   268920 Sep  6 18:07 kent_n225.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb     1433 Sep  6 16:45 merge262.py
-rw-rw-r-- 1 sfmqrb sfmqrb    63035 Sep  6 16:56 mk265.py
-rw-rw-r-- 1 sfmqrb sfmqrb    73111 Sep  6 17:13 mk267.py
-rw-rw-r-- 1 sfmqrb sfmqrb    71564 Sep  6 17:08 mk268.py
-rw-rw-r-- 1 sfmqrb sfmqrb    41609 Sep  6 17:31 mk274.py
-rw-rw-r-- 1 sfmqrb sfmqrb    51778 Sep  6 17:32 mk276.py
-rw-rw-r-- 1 sfmqrb sfmqrb    46494 Sep  6 17:52 mk279.py
-rw-rw-r-- 1 sfmqrb sfmqrb    16605 Sep  6 17:54 mk280b.py
-rw-rw-r-- 1 sfmqrb sfmqrb    17667 Sep  6 17:56 mk280c.py
-rw-rw-r-- 1 sfmqrb sfmqrb    43177 Sep  6 17:50 mk280.py
-rw-rw-r-- 1 sfmqrb sfmqrb    58322 Sep  6 17:51 mk282.py
-rw-rw-r-- 1 sfmqrb sfmqrb    63940 Sep  6 18:05 mk285.py
-rw-rw-r-- 1 sfmqrb sfmqrb    67974 Sep  6 18:09 mk286.py
-rw-rw-r-- 1 sfmqrb sfmqrb    60646 Sep  6 18:11 mk287.py
-rw-rw-r-- 1 sfmqrb sfmqrb  8373934 Sep  6 17:00 mk.pdf
-rw-rw-r-- 1 sfmqrb sfmqrb   378445 Sep  6 17:00 mk.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    11601 Sep  6 16:42 p262-g01.json
-rw-rw-r-- 1 sfmqrb sfmqrb    10625 Sep  6 16:43 p262-g02.json
-rw-rw-r-- 1 sfmqrb sfmqrb    19393 Sep  6 16:46 p262-g03.json
-rw-rw-r-- 1 sfmqrb sfmqrb    19959 Sep  6 16:44 p262-g04.json
-rw-rw-r-- 1 sfmqrb sfmqrb    12063 Sep  6 16:43 p262-g05.json
-rw-rw-r-- 1 sfmqrb sfmqrb    12051 Sep  6 16:44 p262-g06.json
-rw-rw-r-- 1 sfmqrb sfmqrb    12737 Sep  6 16:44 p262-g07.json
-rw-rw-r-- 1 sfmqrb sfmqrb    17259 Sep  6 16:46 p262-g08.json
-rw-rw-r-- 1 sfmqrb sfmqrb    17820 Sep  6 16:53 p262-g09.json
-rw-rw-r-- 1 sfmqrb sfmqrb    17855 Sep  6 16:45 p262-g10.json
-rw-rw-r-- 1 sfmqrb sfmqrb    14983 Sep  6 16:44 p262-g11.json
-rw-rw-r-- 1 sfmqrb sfmqrb    25352 Sep  6 16:46 p262-g12.json
-rw-rw-r-- 1 sfmqrb sfmqrb    17745 Sep  6 16:44 p262-g13.json
-rw-rw-r-- 1 sfmqrb sfmqrb   105748 Sep  6 16:39 p263hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb     5565 Sep  6 17:22 p275_krei_empty.png
-rw-rw-r-- 1 sfmqrb sfmqrb    53703 Sep  6 17:22 p275_pahlavi.png
-rw-rw-r-- 1 sfmqrb sfmqrb     7106 Sep  6 17:34 p279_greek.png
-rw-rw-r-- 1 sfmqrb sfmqrb    12970 Sep  6 17:34 p279_word.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3647 Sep  6 17:34 p279_xsaeta.png
-rw-rw-r-- 1 sfmqrb sfmqrb   130651 Sep  6 17:48 p283_arrow.png
drwxrwxr-x 2 sfmqrb sfmqrb     4096 Sep  6 18:02 p284
-rw-rw-r-- 1 sfmqrb sfmqrb    43108 Sep  6 17:51 p284_e0_fa.png
-rw-rw-r-- 1 sfmqrb sfmqrb    89734 Sep  6 17:51 p284_e0.png
-rw-rw-r-- 1 sfmqrb sfmqrb    59639 Sep  6 17:48 p284_e2b.png
-rw-rw-r-- 1 sfmqrb sfmqrb   106502 Sep  6 17:48 p284_e2.png
drwxrwxr-x 2 sfmqrb sfmqrb     4096 Sep  6 18:17 p289
-rw-rw-r-- 1 sfmqrb sfmqrb    54419 Sep  6 18:05 p289_labibi.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1476 Sep  6 18:11 p291_esfand.png
-rw-rw-r-- 1 sfmqrb sfmqrb    31043 Sep  6 18:11 p291_root.png
-rw-rw-r-- 1 sfmqrb sfmqrb    66777 Sep  6 16:42 pg261.png
-rw-rw-r-- 1 sfmqrb sfmqrb    84660 Sep  6 16:39 pg262.png
-rw-rw-r-- 1 sfmqrb sfmqrb    71156 Sep  6 16:38 pg263.png
-rw-rw-r-- 1 sfmqrb sfmqrb    92930 Sep  6 16:37 pg264hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    57862 Sep  6 16:35 pg264.png
-rw-rw-r-- 1 sfmqrb sfmqrb    13324 Sep  6 16:57 pg265_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb    86370 Sep  6 16:57 pg265.png
-rw-rw-r-- 1 sfmqrb sfmqrb    79922 Sep  6 16:42 pg266.png
-rw-rw-r-- 1 sfmqrb sfmqrb    70622 Sep  6 16:56 pg267.png
-rw-rw-r-- 1 sfmqrb sfmqrb    69592 Sep  6 16:52 pg268.png
-rw-rw-r-- 1 sfmqrb sfmqrb    71754 Sep  6 16:55 pg269.png
-rw-rw-r-- 1 sfmqrb sfmqrb   122626 Sep  6 16:58 pg270hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    87489 Sep  6 16:55 pg270.png
-rw-rw-r-- 1 sfmqrb sfmqrb   115300 Sep  6 17:05 pg271hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    66696 Sep  6 17:04 pg271.png
-rw-rw-r-- 1 sfmqrb sfmqrb    68566 Sep  6 16:58 pg272.png
-rw-rw-r-- 1 sfmqrb sfmqrb    66829 Sep  6 17:28 pg273_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb   157304 Sep  6 17:10 pg273hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    70615 Sep  6 17:27 pg273.png
-rw-rw-r-- 1 sfmqrb sfmqrb    65586 Sep  6 17:18 pg274.png
-rw-rw-r-- 1 sfmqrb sfmqrb    80338 Sep  6 17:21 pg275.png
-rw-rw-r-- 1 sfmqrb sfmqrb    76740 Sep  6 17:15 pg276.png
-rw-rw-r-- 1 sfmqrb sfmqrb    44171 Sep  6 17:16 pg277.png
-rw-rw-r-- 1 sfmqrb sfmqrb    89267 Sep  6 17:26 pg278.png
-rw-rw-r-- 1 sfmqrb sfmqrb   168655 Sep  6 17:34 pg279hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    75777 Sep  6 17:34 pg279.png
-rw-rw-r-- 1 sfmqrb sfmqrb    82065 Sep  6 17:34 pg280.png
-rw-rw-r-- 1 sfmqrb sfmqrb    61535 Sep  6 17:39 pg281.png
-rw-rw-r-- 1 sfmqrb sfmqrb    70575 Sep  6 17:34 pg282.png
-rw-rw-r-- 1 sfmqrb sfmqrb    74784 Sep  6 17:47 pg283.png
-rw-rw-r-- 1 sfmqrb sfmqrb    81024 Sep  6 17:50 pg284hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    81024 Sep  6 17:51 pg284.png
-rw-rw-r-- 1 sfmqrb sfmqrb   144566 Sep  6 17:49 pg284_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    84487 Sep  6 17:53 pg285.png
-rw-rw-r-- 1 sfmqrb sfmqrb   106264 Sep  6 17:53 pg286hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    76099 Sep  6 18:10 pg286.png
-rw-rw-r-- 1 sfmqrb sfmqrb    72442 Sep  6 17:59 pg287.png
-rw-rw-r-- 1 sfmqrb sfmqrb    53847 Sep  6 17:58 pg288.png
-rw-rw-r-- 1 sfmqrb sfmqrb    90831 Sep  6 18:04 pg289.png
-rw-rw-r-- 1 sfmqrb sfmqrb    98901 Sep  6 18:18 pg290.png
-rw-rw-r-- 1 sfmqrb sfmqrb   105586 Sep  6 18:11 pg291hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    70592 Sep  6 18:10 pg291.png
-rw-rw-r-- 1 sfmqrb sfmqrb   103438 Sep  6 18:12 pg292.png
-rw-rw-r-- 1 sfmqrb sfmqrb   390669 Sep  6 18:10 syn_n1548.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   390669 Sep  6 18:10 syn_n1549.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   390669 Sep  6 18:10 syn_n1550.jpg
```


## [2026-09-06T22:18:54.872Z] TOOL CALL #85: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg290.png"
}
```


### [2026-09-06T22:18:55.330Z] TOOL RESULT

```

```


## [2026-09-06T22:18:55.328Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-06T22:19:07.853Z] TOOL CALL #86: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && timeout 300 pdftoppm -f 290 -l 290 -r 600 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf pg290hi && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg290hi.png'); print(im.size)\nw,h=im.size\n# zar line approx y fraction 0.455-0.475, x 0.44-0.78\nim.crop((int(0.42*w),int(0.445*h),int(0.80*w),int(0.475*h))).save('zar_line.png')\n\"; ls -la zar_line.png",
 "description": "Crop zâr line at high res"
}
```


### [2026-09-06T22:19:12.733Z] TOOL RESULT

```
(5100, 6600)
-rw-rw-r-- 1 sfmqrb sfmqrb 3698 Sep  6 18:19 zar_line.png
```


## [2026-09-06T22:19:15.148Z] TOOL CALL #87: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/zar_line.png"
}
```


### [2026-09-06T22:19:15.167Z] TOOL RESULT

```

```


## [2026-09-06T22:19:37.821Z] TOOL CALL #88: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/%D8%B2%D8%A7%D8%B1\" \\\n \"https://en.wiktionary.org/wiki/%DA%86%D8%B1%D8%AE\" \\\n \"https://en.wiktionary.org/wiki/%DA%86%D8%B4%D9%85\" \\\n \"https://en.wiktionary.org/wiki/%DA%AF%D9%88%D8%A7%D9%87\" ; do\n timeout 120 python3 tools/fetch_source.py \"$u\" --note \"page 290 Kwek/Kwel node words: -zar suffix, carx, casm, govah\" ; done 2>&1 | tail",
 "description": "Fetch more Wiktionary pages"
}
```


### [2026-09-06T22:19:41.586Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/300ef8adf8959c2c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/aece4509771466b4.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/30eeb60d344f2e38.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e00ab395676bc1c2.txt
```


## [2026-09-06T22:19:44.855Z] TOOL CALL #89: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in 300ef8adf8959c2c aece4509771466b4 30eeb60d344f2e38 e00ab395676bc1c2; do echo \"########## $f\"; grep -n -m4 -A4 \"From Middle Persian\\|Inherited from\\|Ultimately from\\|from Proto-Iranian\" $f.txt | head -30; done",
 "description": "Read the four new Wiktionary pages"
}
```


### [2026-09-06T22:19:46.818Z] TOOL RESULT

```
########## 300ef8adf8959c2c
1164: Inherited from Proto-Turkic *sar ( “ wrapping ” ) , a root related to Proto-Turkic *saru- ( “ to wind, wrap ” ) . Compare صارمق ( sarmak , “ to wind, wrap, bind ” ) , صارق ( sarık , “ turban ” ) and صارغی ( sargı , “ wrapping, bandage ” ) .
1165-
1166- Noun
1167- [ edit ] 
1168-
--
1285: Borrowed from Persian زار ( zar , “ groan, lament ” ) , from Middle Persian *zār , ultimately from Proto-Iranian *jāráyati ( “ to be angered, vexed ” ) .
1286-
1287- Noun
1288- [ edit ] 
1289-
--
1330: Ultimately from Proto-Iranian *jāráyati . See it for more.
1331-
1332- Noun
1333- [ edit ] 
1334-
--
1408: Inherited from Arabic زَارَ ( zāra ) .
1409-
1410- Pronunciation
1411- [ edit ] 
1412-
########## aece4509771466b4
311: Borrowed from Persian چرخ ( čarx , “ wheel ” ) , from Middle Persian 𐫝𐫍𐫡 ( chr /⁠čahr⁠/ , “ wheel, cycle ” ) , ultimately from Proto-Iranian *čaxrám .
312-
313- Noun
314- [ edit ] 
315-
--
382: From Middle Persian 𐫝𐫍𐫡 ( chr /⁠čahr⁠/ , “ wheel, cycle ” ) , from Proto-Iranian *čaxrám (compare Avestan 𐬗𐬀𐬑𐬭𐬀 ( caxra , “ wheel ” ) ), from Proto-Indo-Iranian *čakrám (compare Sanskrit चक्र ( cakrá ) ), from Proto-Indo-European *kʷékʷlos ( “ wheel, circle ” ) .
383-
384- Pronunciation
385- [ edit ] 
386-
--
504: Ottoman Turkish terms derived from Proto-Iranian 
505- Ottoman Turkish lemmas 
506- Ottoman Turkish nouns 
507- ota:Simple machines 
508- ota:Machines 
--
512: Persian terms inherited from Proto-Iranian 
########## 30eeb60d344f2e38
249: From Middle Persian [script needed] ( AYNE ) , [script needed] ( čšm /⁠čašm⁠/ ) , from Proto-Iranian *čášma , from Proto-Indo-Iranian *čáćšma . Cognate with Sanskrit चक्षस् ( cakṣas ) .
250-
251- Pronunciation
252- [ edit ] 
253-
--
480: Persian terms inherited from Proto-Iranian 
481- Persian terms derived from Middle Persian 
482- Persian terms derived from Proto-Indo-Iranian 
483- Persian terms inherited from Proto-Indo-Iranian 
484: Persian terms derived from Proto-Iranian 
485- Persian terms inherited from Middle Persian 
486- Persian terms with IPA pronunciation 
487- Rhymes:Persian/aʃm 
488- Rhymes:Persian/aʃm/1 syllable 
--
502: Urdu terms derived from Proto-Iranian 
503- Urdu terms with IPA pronunciation 
504- Rhymes:Urdu/əʃm 
505- Rhymes:Urdu/əʃm/1 syllable 
506- Urdu lemmas 
########## e00ab395676bc1c2
149: From Middle Persian gwk’dy ( gugāy ) . From Proto-Indo-European *wí ( “ apart ” ) + *kʷeḱ- ( “ to see ” ) ; literally meaning “to see apart, differentiate”. Compare Old Armenian վկայ ( vkay ) , an Iranian borrowing.
150-
151- Pronunciation
152- [ edit ] 
153-
```


## [2026-09-06T22:20:01.890Z] TOOL CALL #90: Bash

```json
{
 "command": "timeout 120 python3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/-%D8%B2%D8%A7%D8%B1\" --note \"page 290, Kwel node 5: Persian suffix -zār 'place of'\" 2>&1 | tail -2",
 "description": "Fetch Wiktionary -zār suffix"
}
```


### [2026-09-06T22:20:04.343Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/64f7ce4a29710b66.txt
```


## [2026-09-06T22:20:07.643Z] TOOL CALL #91: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && grep -n -m6 -B2 -A6 \"Etymology\" 64f7ce4a29710b66.txt | sed -n '1,60p'",
 "description": "Read -zār suffix page"
}
```


### [2026-09-06T22:20:07.694Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T22:20:10.272Z] TOOL CALL #92: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && head -40 64f7ce4a29710b66.txt",
 "description": "Inspect -zār fetch"
}
```


### [2026-09-06T22:20:10.313Z] TOOL RESULT

```
URL: https://en.wiktionary.org/wiki/-%D8%B2%D8%A7%D8%B1
FETCHED: 2026-09-06T22:20:04Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 404: Not Found
```


## [2026-09-06T22:20:17.392Z] TOOL CALL #93: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY && python3 - <<'EOF'\nt=open('ARY_pages.txt',encoding='utf8',errors='replace').read()\npg=t.split('\\f')\nimport re\nfor w in ['چرخ','چشم','بازار','کاشتن','گواه','چریدن','چاشت']:\n    hits=[i for i,p in enumerate(pg) if w in p]\n    print(w,hits[:6])\nEOF",
 "description": "Aryanpur lookups"
}
```


### [2026-09-06T22:20:18.985Z] TOOL RESULT

```
چرخ [11, 23, 181, 195, 217, 298]
چشم [1, 4, 5, 6, 9, 15]
بازار []
کاشتن [387, 404]
گواه [12, 14, 511]
چریدن [217]
چاشت [223]
```


## [2026-09-06T22:20:22.640Z] TOOL CALL #94: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY && python3 - <<'EOF'\nt=open('ARY_pages.txt',encoding='utf8',errors='replace').read()\npg=t.split('\\f')\nfor i,w in [(217,'چرخ/چریدن'),(223,'چاشت'),(387,'کاشتن'),(511,'گواه')]:\n    print('=== leaf',i,w,'===')\n    print(pg[i][:1400])\n    print()\nEOF",
 "description": "Read Aryanpur pages"
}
```


### [2026-09-06T22:20:24.344Z] TOOL RESULT

```
=== leaf 217 چرخ/چریدن ===
[pdf page 218]
چراء چریدن» چراندن / ۲۱۹
یادداشت:
۱ هیچیک از پسگشت‌های فارسی ریشه‌ی اين واژه را نمی‌دهند.
۲ چم این واژه در زبان سانکریت؛ انخنا, ۰
چم این واژه در زیان لیترانی: گوشه کنج.
چم این واژه در زبان لاتین: دشت,
چم این واژه در زبان پونانی؛ کج کردن؛ دارای انحناکردن.
۳ واژه‌های انگلیسی 2۸8/0 و آلمانی ۸۱188 از همین واجريشه آمده‌اند.
اوستایی (/4557:40): -13۸3 ,07۸۸71
پارسی باستان ((۵ا۶58۵ 0ا :)0‏ مهف پسگشت‌ها کطالق عم
پهلوی (امنتنمم: #هاتفتل تفای 1 1
کر دی (8/01517): :5ل2 لاک ۱۸۸
مات ,ا01اتمتکاتن 6 (116,)۳۸8782 (10تفقی)
اففانی (پشتر) (۸707۸۷1): 3 ۰ ناه
سانسکریت (58/7/(ه5): 7 (7۲ف68۸ ,۲۸8۶7۸۰)
هلف باتشتف باآمعف فرهنگ معین : ۱۳۸۳
یونانی (0888): ۳۸۲۵۸1 ,281,0۷۷ برهان قاطع + ۶و ۶۳۵
لاتین (7مل): 58 ,0۵
بادداشت: ۱
,چم این واژه در زبان‌های سانسکریت: حرکت کردن؛ جنپیدن» چرخیدن. ۱
جماین واژه در زبان لاتین کیت وکا ر گردن,
۹
پیلری (//7۲ :۲7۲۸3875110 ,8 هت( 1 بققفتل
اوستی (0555716): رد تخاری ۸ (۸ [7087۸77۸): 7دک
اففانی (پشتر) (۸۳07۸41): تخاری 8 (8 327 707۸): 5


=== leaf 223 چاشت ===
[pdf page 224]
چشم | ۲۲۵
اوستایی (4:872): اراانکی اسلاوی کهن (۲12شا5 071081 00):
پارسی باستان ((۶8۴۵۵ صا0): 0
2۸1۸
پهلری (17تتنه۸): ۲71۸5135 ,لا7[ک۲۸ پسگشت‌ها 2/5
کردی (0713[4): 5 ز ۳
بلوچی (/17ع1الم8): 0 105 تال ا(ما02
اففانی (پشنو) (/4۳۵/۸۸۷): ۰ ۲7۸913315 3 (88) :۸۸528
سانسکریت (54/5/7): 25 اه
وناکلفی) ,5۸716 دکلف) دقیا 22 (۳۴5) 0
یونانی 078810): زین رل دابا برهان قاطع : ۶۳۸
یادداشت:
چم اين واژه در اسلاوی کهن» نشان دادن. َ
چم اين واژه در یونانی: نشان.
اوستایی (487۸1): پسگشت‌ها 5
۰ تکفا حتاقق زا
پهلری (امتتنمم: ‏ ,5۸81117۸0 ام
6 11۸33017150 ,انغقتاعی 6 (1۸818 ,75۸655
و 4 ۲8۸6 8066
ود برهان قاطع : ۳ و (چاشت) ۶۱۲
۱۹
یادداشت:
۱ چم این واژه در زبان پهلوی: آموختن) مزه کردن.
> بازگشت به: چشم آگاه» نگاه,
۳ احتمال کمتری وجود دارد که "چشیدن" از واجریشه‌ی هند و اروپایی -188* (لاتین:01787۸3)
انگلیسی:0110088) باشد برای بررسی یشتر پسگشت به: 168 (۲1700872) :8۸710117۸7 ۳01607279
399 ۱


=== leaf 387 کاشتن ===
[pdf page 388]
فراخ ۳۸۹
برتونی (//570ل): -0 88 پسگشت‌ها امه وی دناد
آلبانی (0(مامهتم: ۳ زان 0
هتیت. (11177/758): نف8 برهان قاطع + ۱۴۴۳

لغت‌نامه دهخدا: ۱۷۰۱۱۲
اوستایی (4887۸2): لیترانی (7442/2 7+
71 ,۶8۸78۸7 71 ,لا[85712673
پارسی باستان (۳2/81۸۷ 00): لنرنی (لتی) (417140ا): ۳7
-11(۸ ۹۳82 پروسی کهن (۳82551(۷ 010):
پهلری (۵/1الل۳۸): ,ال۲82 زین ند ۱ 8
کردی (۵/5۶7/)+ 7 ۳" ایرندی کهن (8/37] ل0): 1۳
بلوچی (/14تاءل8۸): ۲۸۵۲7 ولزی (/85.5): 110
سانسکریت (54۸/37): برتونی (888700): ,اکن
1 ,۳8۸73۸8 ,2۸3717۷7 ۱
ارمنی (/4/۵48274): شآ
یونانی (07/20): 85 ,۸7085آ71 پسگشت‌ها ار ی را اد ادن
لاتین (470): 71۸۷1282 ,71۸1۸ 3
اسلاوی کهن (10/بها5 218/4 010): 1 (365ه) اد هم
1 ۳۸ برهان قاطع : ۱۳۴۴
بادداشت,
ش چم این واژه در لاتین:کاشتن؛ نهال,
.۸ ند
ا
پارسی باستان (28۴814۸ 010): بلوچی (71ل)تادلهه):
نی انا دسا 7 ,6 3115۸هت51
پهلری (7الل2۸): ,۲8241881 افغانی (پشس) ۰.۸۲۵۸۵ ,1183۸۲۵۲
03 ,ا۸۵ ۲۴۵۵/۲۲8۲ تخاری 8 (ظ 10271۸۸1۸(۷): کعقه


=== leaf 511 گواه ===
[pdf page 512]
واژه وات» واج / ۵۱۳
ا
ا
اوستایی (/۸۷:87۸4۸): آلمانی کهن ((08704۸ الا 02):
7 ۷۸6 ,۷۸84 0
پهلوی (/۷ل۳۸): آلمانی (/0870):
,۵ ,۷۷27۸0 ,۷۸۲۸4 ۷/۸ 7 ,33۷/21105
اومنتی (083387/6): ۷۸۸ ,۷۸ انگلیسی (ن5ل0/0ق)(از فرانسه) ۷۵168
کردی (7/015): ,85[5 پروسی کهن (للماکونا ۲۲ ۰:۵۵ ۷۷۸۲۴۶
تخاری ۸4 (۸ (4ل1۸7ل707)+ ۷۸ هنیت (۷/77/78]): رانا
*تخاری 8 (8 [(4ل7۸7ل70): ۷
سانسکریت (5۸۸/5/7): پسگشت‌ها اش بر ردنا
5 ۷۸ رکشل ۷ بل 11351136 ۸0/0700
ارمتی (474827]400): 00057 0 ۷۵۲۴۵ 7
بونانی ۰۰۲۵۵۵ ۸8۲۳۵۲ ,۸805 3 (۳۸۲۴3) :0525
لاتین (/710صا): 7 ,۷0۵ لت مان شا
فرانسه (۳8۵(/1)+ ۷ 1 (5۸130) ,140 (۷۵32)
اسپانیایی (5۳۸//8): ۷085 1248 مناه
ایتالیایی (/4ا7۸)): ۷0 5 (۷۵]۳5) +02/100/5
رومانی ((۸4۸(/]4): ۷0 8 (۷0۵165) +547
پرتفالی (00870011858)+ ۷2 1 (۷۵۴۵) امزکن ا درد
ایسلندی کهن (/(070۸14/همک (0): 137 تخا اس
۷۸۳7۸ برهان قاطع + ۳ ۲۲۴۴و ۲۲۴۸
4 8 پیوداشت:
7 چم این واژه در زبان‌های اریچیو پروسی کهن: فریاد» داد زدن.
چم این واژه در زبان‌های تب و ایسلندی کهن: گواهی» شهادت دادن.
چم‌اين واژه در زبان‌های آلمانی: ذ کر کردن» گفتن.
چم اين واژه در زبان‌های رومانس: صداء آوازه,
```


## [2026-09-06T22:21:45.126Z] TOOL CALL #95: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && head -8 a0a0020111279d5d.txt; echo \"...\"; grep -n -m1 -A10 \"Root\\b\" a0a0020111279d5d.txt | head -20",
 "description": "Check PIE kwel- page"
}
```


### [2026-09-06T22:21:45.179Z] TOOL RESULT

```
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/k%CA%B7el-
FETCHED: 2026-09-06T22:16:04Z
STATUS: 200
TITLE: Reconstruction:Proto-Indo-European/kʷelh₁- - Wiktionary, the free dictionary

Reconstruction:Proto-Indo-European/kʷelh₁- - Wiktionary, the free dictionary 

 Jump to content 
...
62: Root 
63-
64- 1.1.1 
65- Reconstruction notes 
66-
67- 1.1.2 
68- Alternative reconstructions 
69-
70- 1.1.3 
71- Derived terms 
72-
```


## [2026-09-06T22:21:47.999Z] TOOL CALL #96: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && grep -n -m1 -A25 \"^ Root $\" a0a0020111279d5d.txt | head -40",
 "description": "Read PIE kʷelh1 root content"
}
```


### [2026-09-06T22:21:49.836Z] TOOL RESULT

```
62: Root 
63-
64- 1.1.1 
65- Reconstruction notes 
66-
67- 1.1.2 
68- Alternative reconstructions 
69-
70- 1.1.3 
71- Derived terms 
72-
73- 1.1.4 
74- Descendants 
75-
76- 1.2 
77- References 
78-
79- Toggle the table of contents 
80-
81- Reconstruction:Proto-Indo-European/ kʷelh₁- 
82-
83- 1 language 
84-
85- فارسی 
86-
87- Reconstruction
```


## [2026-09-06T22:21:52.456Z] TOOL CALL #97: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && sed -n '87,130p' a0a0020111279d5d.txt",
 "description": "PIE kʷelh1 gloss"
}
```


### [2026-09-06T22:21:52.518Z] TOOL RESULT

```
 Reconstruction 

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
 Get shortened URL 

 Print/export

 Download as PDF 
 Printable version 

 In other projects

 Appearance
```


## [2026-09-06T22:21:55.200Z] TOOL CALL #98: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && grep -n -m2 -A8 \"to turn\\|to move around\\|Reconstruction notes\" a0a0020111279d5d.txt | head -30",
 "description": "PIE kʷelh1 meaning"
}
```


### [2026-09-06T22:21:55.248Z] TOOL RESULT

```
65: Reconstruction notes 
66-
67- 1.1.2 
68- Alternative reconstructions 
69-
70- 1.1.3 
71- Derived terms 
72-
73- 1.1.4 
--
149: to turn ( end-over-end ) 
150-
151- to revolve around, and therefore to sojourn, to dwell
152-
```


## [2026-09-06T22:22:03.945Z] TOOL CALL #99: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/k%CA%B7e%E1%B8%B1-\" \\\n \"https://en.wiktionary.org/wiki/%D8%A2%DA%AF%D8%A7%D9%87\" \\\n \"https://en.wiktionary.org/wiki/%D9%86%DA%AF%D8%A7%D9%87\" \\\n \"https://en.wiktionary.org/wiki/%DA%86%D8%B4%DB%8C%D8%AF%D9%86\" \\\n \"https://en.wiktionary.org/wiki/%DA%86%D8%B1%DB%8C%D8%AF%D9%86\" ; do\n timeout 120 python3 tools/fetch_source.py \"$u\" --note \"page 290, Kwek/Kwel nodes: PIE root and Persian derivatives\" ; done 2>&1 | tail",
 "description": "Fetch remaining Wiktionary pages"
}
```


### [2026-09-06T22:22:08.000Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/992f58e31d919fbd.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e5391747358e7776.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ff953f567dd42ef2.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/dfd611b1b4a7d9c3.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/8674a5aab05a7e42.txt
```


## [2026-09-06T22:22:11.400Z] TOOL CALL #100: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in 992f58e31d919fbd e5391747358e7776 ff953f567dd42ef2 dfd611b1b4a7d9c3 8674a5aab05a7e42; do echo \"##### $f\"; head -4 $f.txt | sed -n '1,4p'; grep -n -m2 -A4 \"From Middle Persian\\|Inherited from\\|From Proto-Iranian\\|to see, to appear\\|to appear\" $f.txt | head -14; done",
 "description": "Read the five new pages"
}
```


### [2026-09-06T22:22:13.364Z] TOOL RESULT

```
##### 992f58e31d919fbd
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/k%CA%B7e%E1%B8%B1-
FETCHED: 2026-09-06T22:22:05Z
STATUS: 200
TITLE: Reconstruction:Proto-Indo-European/kʷeḱ- - Wiktionary, the free dictionary
##### e5391747358e7776
URL: https://en.wiktionary.org/wiki/%D8%A2%DA%AF%D8%A7%D9%87
FETCHED: 2026-09-06T22:22:06Z
STATUS: 200
TITLE: آگاه - Wiktionary, the free dictionary
180: Inherited from Middle Persian [Book Pahlavi needed] ( ʾkʾs /⁠āgāh⁠/ , “ aware, knowing ” ) , ultimately a derivative of Proto-Indo-European *kʷeḱ- ( “ to see; to look ” ) . Related to نگاه ( negâh ) and dialectal گاس ( gâs ) . Related to Old Armenian ակահ ( akah ) , an Iranian borrowing.
181-
182- Pronunciation
183- [ edit ] 
184-
##### ff953f567dd42ef2
URL: https://en.wiktionary.org/wiki/%D9%86%DA%AF%D8%A7%D9%87
FETCHED: 2026-09-06T22:22:07Z
STATUS: 200
TITLE: نگاه - Wiktionary, the free dictionary
161: From Proto-Iranian *ni- + *kas- ( “ to look, appear ” ) , from Proto-Indo-European *h₁én ( “ in ” ) + *kʷeḱ- ( “ to see; to look ” ) . [ 1 ] Related to آگاه ( âgâh ) , and dialectal گاس ( gâs ) .
162-
163- Pronunciation
164- [ edit ] 
165-
##### dfd611b1b4a7d9c3
URL: https://en.wiktionary.org/wiki/%DA%86%D8%B4%DB%8C%D8%AF%D9%86
FETCHED: 2026-09-06T22:22:07Z
STATUS: 200
TITLE: چشیدن - Wiktionary, the free dictionary
152: Inherited from Proto-Iranian *čaš- ( “ to taste ” ) . [ 1 ] Compare Sanskrit चष् ( caṣ , “ to eat, taste ” ) , although Cheung believes this is a late loanword from Iranian.
153-
154- Pronunciation
155- [ edit ] 
156-
##### 8674a5aab05a7e42
URL: https://en.wiktionary.org/wiki/%DA%86%D8%B1%DB%8C%D8%AF%D9%86
FETCHED: 2026-09-06T22:22:07Z
STATUS: 200
TITLE: چریدن - Wiktionary, the free dictionary
150: From Proto-Iranian *čárHati , from Proto-Indo-Iranian *čárHati , from Proto-Indo-European *kʷel- ( “ to move; to turn (around) ” ) . [ 1 ] [ 2 ] 
151-
152- Indo-Iranian cognates include Ossetian цӕрын ( cæryn , “ to live ” ) , Pashto څرېدل ( śaredal , “ to pasture, graze ” ) , Avestan 𐬗𐬀𐬭𐬁𐬥𐬍 ( carānī , “ I move, approach ” ) , and Sanskrit चरति ( cárati , “ he moves ” ) . More distantly related to Ancient Greek πέλω ( pélō ) , Latin colō , Old Church Slavonic коло ( kolo , “ wheel ” ) .
153-
154- Pronunciation
```


## [2026-09-06T22:22:21.245Z] TOOL CALL #101: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && grep -n -m6 \"to appear\\|to see\\|Root \" 992f58e31d919fbd.txt | head; sed -n '140,175p' 992f58e31d919fbd.txt",
 "description": "PIE kʷeḱ- page content"
}
```


### [2026-09-06T22:22:21.296Z] TOOL RESULT

```
62: Root 
139: to see 

 to look 

 Derived terms
 [ edit ] 

 Terms derived from the Proto-Indo-European root *kʷeḱ- (44 c, 0 e) 

 *kʷéḱ-s-ti ~ kʷḱ-s-énti ( s-desiderative ) [ 2 ] 
 Proto-Indo-Iranian: *čáštay ( see there for further descendants )

 *kʷéḱ-t ~ *kʷḱ-ént ( athematic root aorist ) [ 2 ] 
 Proto-Indo-Iranian: *Hákšat 
 Proto-Indo-Aryan: *Hákṣat 
 Sanskrit: अक्षत् ( ákṣat ) 

 Proto-Iranian: *Háxšat 
 Old Avestan: 𐬑𐬯𐬁𐬌 ( xsāi , “ I shall look, see ” , 1 aor med subj sg ) 
 ⇒ Old Avestan: 𐬁𐬑𐬯𐬋 ( āxsō , “ look at ” , 2 aor act inj sg ) 

 *kʷḗḱ-ti ~ *kʷéḱ-n̥ti ( Narten present ) [ 2 ] 
 Proto-Indo-Iranian: *kā́ćati 
 Proto-Indo-Aryan: *kā́śati 
 Sanskrit: काशते ( kā́śate ) 

 Proto-Iranian: *kā́cati 
 Younger Avestan: 𐬁𐬐𐬀𐬯𐬀𐬝 ( ākasat̰ ) 

 *kʷe-kʷóḱ-e ~ *kʷe-kʷḱ-ḗr ( perfect ) [ 2 ] 
 Proto-Indo-Iranian: *čā́kaća ~ *čakšŕ̥(š) 
 Proto-Indo-Aryan: *ćákṣr̥ṣ 
 Sanskrit: चक्षुर् ( cákṣur ) 

 ⇒ *kʷé-kʷ-ḱ-u-s ( neuter participle ) 
 Proto-Indo-Iranian: *čákšuš ( see there for further descendants )
```


## [2026-09-06T22:22:25.356Z] AGENT

Now I have enough material. Writing the verification file.


## [2026-09-06T22:25:46.329Z] TOOL CALL #102: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p290 && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build290a.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io, os\n\nW = \"https://en.wiktionary.org/wiki/\"\n\ne1 = {\n \"entry\": 1,\n \"root\": \"Kwek, Qwek\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *kʷeḱ- (also *kʷeḱ-s-, variant *kʷeg-) 'to appear, see, show'\",\n \"note\": \"Nourai's headword, language label and gloss reproduce his sources verbatim: Watkins/AHD has 'kʷek-. To appear, see, show. Variant form *kʷeg- in Slavic *kaz- ... [Pok. kʷek- 638]', and Walde-Pokorny I 510 f. heads the entry 'qʷek-, qʷok-, qʷek-s-' — which is exactly where Nourai's double spelling 'Kwek, Qwek' comes from (Watkins's kʷ- beside Walde's qʷ-). Pokorny IEW 638-639 gives the meaning 'to seem, see, show' with Av. ākasat̰, Av./OP čašman- 'eye', np. čašm, āgāh, nigāh — i.e. Pokorny's own entry already contains most of the chart. The one substantive problem on this chart is not the root but two items hung under it: Av. vi-či- (node #1) belongs to the neighbouring root *kʷei- 'to observe, pick out' (WP I 509 f., Pok. 636 f.), and the 'taste' words (nodes #3, #4) are separated from *kʷeḱ- by Cheung 2007.\",\n \"note_fa\": \"ریشهٔ هندواروپایی آغازین *kʷeḱ- (با گسترش *kʷeḱ-s- و گونهٔ *kʷeg-) به معنی «پدیدار شدن، دیدن، نشان دادن» است؛ پوکورنی در ص ۶۳۸–۶۳۹ و والده–پوکورنی جلد یکم ص ۵۱۰ سرواژه را «qʷek-, qʷok-, qʷek-s-» آورده‌اند و واتکینز (AHD) عیناً «to appear, see, show». پس هم نام دوگانهٔ «Kwek, Qwek» (که از دو شیوهٔ نگارش kʷ و qʷ می‌آید) و هم برچسب زبانی و معنایی نورایی درست است. خودِ صفحهٔ پوکورنی صورت‌های اوستایی ākasat̰ و čašman- و فارسی چشم، آگاه و نگاه را نام می‌برد. دو کاستی در نمودار هست: صورت اوستایی vi-či- در واقع به ریشهٔ همسایهٔ *kʷei- «برگزیدن، جدا کردن» تعلق دارد، و واژه‌های «چشیدن/چاشت» را چونگ (۲۰۰۷) از این ریشه جدا می‌کند.\",\n \"sources\": [\n   \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/k%CA%B7e%E1%B8%B1-\"\n ],\n \"ref_check\": [\n   {\"ref\": \"POK:638\", \"status\": \"supports\",\n    \"note\": \"Pokorny IEW, read in POK_full.txt lines 52608-52660 (block ending 'Page(s): 638-639'): 'Root / lemma: kʷeḱ-, kʷoḱ-, kʷeḱ-s- … Meaning: to seem, see, show. Material: Old Indic kāśate ‘appears, glares, gleams, shines’, cakāsti … Avestan ākasat̰ ‘perceives’; npers. āgāh ‘expert, skillful’, nigāh ‘sight’; s-extension kʷeḱ-s-: Old Indic caṣṭe … Avestan čašte, -aiti ‘instruct, teach’ …, Middle Persian čāšītan ‘instruct, teach’, Avestan, Old pers. čašman- n. ‘eye’, npers. čašm … References: WP. I 510 f.' Nourai's root name and gloss reproduce this entry, which begins on p.638 as he cites.\"}\n ],\n \"consulted\": [\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985, AHD_watkins1985.txt line 650\", \"stance\": \"supports\",\n    \"note\": \"'kʷek-. To appear, see, show. Variant form *kʷeg- in Slavic *kaz- in Russian ukazat’, to order: UKASE. [Pok. kʷek- 638.]' — Nourai's root name and gloss are word for word Watkins's.\"},\n   {\"src\": \"WLD\", \"where\": \"Walde-Pokorny I 510-511 (WLD_Bd1_pages.txt leaves 518-519; running head '510 … qʷek-, qʷok-, qʷek-s-')\", \"stance\": \"supports\",\n    \"note\": \"The running head of p.510 reads 'qʷek-, qʷok-, qʷek-s-'; p.511 continues 'Mit tönendem Auslaut aksl. kažǫ, kazati „zeigen, mahnen“ … wohl idg. *qʷeg- neben *qʷek-'. This is the source of Nourai's second spelling 'Qwek'.\"},\n   {\"src\": \"IEC\", \"where\": \"Mann, Indo-European Comparative Dictionary col. ~1023 s.v. queks- (IEC.txt line 13926)\", \"stance\": \"partial\",\n    \"note\": \"Mann sets up 'queks- “tip, point, end, edge, goad”. Cf. WP I, 382, 398, 428 & 510. (Var: quek-) Gk. cf. ték-mar … n. “end, object, limit”' — i.e. he takes Gk. tékmar (which Pokorny puts under kʷeḱ- 'see') to a root 'edge, goad' instead. Mann has no entry glossed 'to see' for this shape; a minority dissent from the root as Nourai gives it.\"},\n   {\"src\": \"KLN\", \"where\": \"Klein 1966 p.42 s.v. akasa (KLN_1966.txt leaf 34)\", \"stance\": \"supports\",\n    \"note\": \"'akasa … OI. ākāśa-, “space”, formed fr. emphatic pref. ā and kāśate, “appears, shines”, prob. from I.-E. base *qʷek-, *qʷeg-, whence also Avestic čašman, “eye”, akasat, “he beheld”, Gk. tekmōr … OSlav. kazǫ, kazati, “to show”.'\"},\n   {\"src\": \"Wiktionary\", \"where\": \"Reconstruction:Proto-Indo-European/kʷeḱ-\", \"stance\": \"supports\",\n    \"note\": \"Headword *kʷeḱ- glossed 'to see / to look'; derived terms include the Narten present *kʷḗḱ-ti → Proto-Iranian *kā́cati → Younger Avestan ākasat̰, and the perfect participle *kʷé-kʷ-ḱ-u-s → PII *čákšuš (Skt. cákṣur 'eye').\"}\n ],\n \"nodes\": []\n}\n\ne1[\"nodes\"].append({\n \"id\": 1, \"lang\": \"Avestan\",\n \"words\": \"kas, čas, čaš; čašman; â-kasat; ni-kasa; vi-kâs, vi-kaya, vi-či\",\n \"verdict\": \"disputed\",\n \"derivation\": \"Six of the seven forms are exactly right; one is misfiled. Av. kas- is Bartholomae's 'kas- V., nur mit ā “gewahr werden, erblicken”, Praes. kasa-' (AiW col. 461), attested in ā-kasat̰ 'thereupon he beheld me' (Vd. 22.2) — Nourai's 'â-kasat: he saw'; this is the Narten present PIE *kʷḗḱ-ti > PIr. *kā́cati (Skt. kā́śate). Av. čaš- (Nourai's čas, čaš) is the s-desiderative *kʷéḱ-s-ti > PII *čáštay, Av. čašte 'he instructs, teaches' (lit. 'causes to notice'), AiW col. 462 's.v. 1. čas- V. lehren'. čašman- n. 'eye' (Av. and OP) is *kʷeḱ-mn̥-, beside Skt. cákṣus- with the same s-extension. ni-kasa- is the compound *ni-kāsa- 'looking down', the direct source of NP negâh (Mo'in's own footnote in BQT s.v. نگاه: 'اوستا *ni-kāsa-، ریشهٔ آن kas «دیدن، نگریستن» است، بارتولمه ۴۰۹'). vi-kās-/vi-kaya- 'to look apart, discriminate' is *ui-kāsa-/*ui-kāya-, whence Pahl. gukās, NP govâh 'witness'; Buck p.1436 §21.28 WITNESS actually lists 'Av. vīkaya-' in his word table, so the form is real. BUT vi-či does NOT belong here: Av. vī-ci- (vī-činaoiti 'he separates, distinguishes') is from PIE *kʷei- 'to pick out, discern' — Walde-Pokorny I 509 f. under qʷeiə- : 'Av. kay-, cinvaiti “(er)lesen, aussuchen, wählen“, mit vi- „scheiden, distinguere“, mit ham- „colligere“; np. čīdan “sammeln”' — a root Nourai himself treats separately under 'Kuei' (the redirect at the head of this very page). Merging vi-či with vi-kās on the strength of the shared gloss 'distinguish' is a conflation of two distinct roots. The gloss 'taste' attached to čaš is likewise Nourai's own extension, taken over from Bailey (see node #3).\",\n \"derivation_fa\": \"شش صورت از هفت صورت این خانه درست است و یکی نابجاست. اوستایی kas- را بارتولمه (ستون ۴۶۱) «فقط با پیشوند ā به معنی آگاه شدن، دیدن» آورده و شاهدش ā-kasat̰ در وندیداد ۲۲٫۲ است؛ این همان ماضی نارتنی *kʷḗḱ-ti > ایرانی آغازین *kā́cati است (سنسکریت kā́śate). صورت čaš- گونهٔ گسترش‌یافته با س (*kʷéḱ-s-ti) است: اوستایی čašte «می‌آموزاند، نشان می‌دهد» (بارتولمه ستون ۴۶۲). čašman- «چشم» از *kʷeḱ-mn̥- است، هم‌ریشه با سنسکریت cákṣus-. ni-kasa- همان ترکیب *ni-kāsa- «نگریستن» است که خودِ معین در حاشیهٔ برهان قاطع ذیل «نگاه» به آن ارجاع می‌دهد («اوستا *ni-kāsa-… ریشهٔ آن kas است، بارتولمه ۴۰۹»). vi-kās-/vi-kaya- از *ui-kāsa-/*ui-kāya- «جدا نگریستن» است و باک در ص ۱۴۳۶ در جدول «شاهد» صورت اوستایی vīkaya- را می‌آورد. اما vi-či به این ریشه تعلق ندارد: اوستایی vī-ci- (vī-činaoiti «جدا می‌کند») از ریشهٔ *kʷei- «برگزیدن، سوا کردن» است — والده–پوکورنی جلد یکم ص ۵۰۹–۵۱۰ ذیل qʷeiə- — همان ریشه‌ای که خود نورایی جداگانه زیر «Kuei» آورده و در سرِ همین صفحه به آن ارجاع داده است. پس در این خانه دو ریشهٔ جدا با تکیه بر معنای مشترک «تمیز دادن» درهم آمیخته شده‌اند.\",\n \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/k%CA%B7e%E1%B8%B1-\"],\n \"ref_check\": [\n   {\"ref\": \"POK:638\", \"status\": \"supports\",\n    \"note\": \"POK_full.txt, block 'Page(s): 638-639': 'Avestan ākasat̰ “perceives” … Avestan čašte, -aiti “instruct, teach” (actually “allow to notice”) … Avestan, Old pers. čašman- n. “eye”'. Covers kas/čaš/ā-kasat/čašman; silent on vi-či.\"},\n   {\"ref\": \"KLN:42\", \"status\": \"supports\",\n    \"note\": \"Klein 1966 p.42 s.v. akasa (KLN_1966.txt leaf 34): '…prob. from I.-E. base *qʷek-, *qʷeg-, whence also Avestic čašman, “eye”, akasat, “he beheld”.' Exactly the two Avestan forms Nourai cites him for.\"},\n   {\"ref\": \"SYN:1436\", \"status\": \"supports\",\n    \"note\": \"Buck, Selected Synonyms p.1436 (SYN.txt leaf 1540, printed number '1436' visible on the leaf) = §21.28 WITNESS; the word table there gives 'Av. vīkaya-' as the Avestan word for 'witness' — Nourai's 'vi-kaya'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"Bartholomae, AiW cols. 461-462 (BRT.txt lines 9421, 9453)\", \"stance\": \"partial\",\n    \"note\": \"'kas- V., nur mit ā “gewahr werden, erblicken”. Praes. kasa-. āt̰ mąm mairyō ākasat̰ “darauf erblickte mich…” V.22.2. Vgl. ai. kāśate “er erscheint”; np. āgāh “kundig”, nigāh “Anblick”' and '1. čas- V. lehren. Praes. čāš- … ai. cáṣṭe “er sieht” … np. (Pü.) čāšītan “lehren”.' Confirms kas-, čaš-, ā-kasat̰, ni-kāsa; but Bartholomae files vī-ci- under a separate root 2. či-/kay- 'lesen, sammeln', not under kas-.\"},\n   {\"src\": \"WLD\", \"where\": \"Walde-Pokorny I 509-511 (WLD_Bd1_pages.txt leaf 518)\", \"stance\": \"contradicts\",\n    \"note\": \"Under qʷeiə- (p.510, immediately before the qʷek- entry): 'Av. kay-, cuyeiti, cinvaiti „(er)lesen, aussuchen, wählen“, mit vi- „scheiden, distinguere“, mit ham- „colligere“; np. čīdan „sammeln“.' Av. vi-či- is therefore a *kʷei- word, not a *kʷeḱ- word.\"},\n   {\"src\": \"ISS_alt_DKS\", \"where\": \"Bailey, Dictionary of Khotan Saka s.v. tcāś- 'see' (ISS_alt_DKS.txt line 2846)\", \"stance\": \"supports\",\n    \"note\": \"'Base cas-, from kas- “see”, with -s-, *cax-š-, Av. čašte, čašāna-, O.Ind. caṣṭe, cakṣ-. IE Pok. 638-9 kʷeḱ-, Av. kas-, M.Parth. pdgs- “look” (*pati-kas-) … Zor.P. ā-gāh “aware”, O.Ind. kāśate.'\"}\n ]\n})\n\ne1[\"nodes\"].append({\n \"id\": 2, \"lang\": \"Persian\",\n \"words\": \"čašm «چشم»; âgâh «آگاه»; negâh «نگاه»; govâh «گواه»\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"All four are standard reflexes of *kʷeḱ- and all four are already named on the very page of Pokorny Nourai cites. (1) čašm < MP čašm (Book Pahlavi ideogram AYNE, phonetic čšm) < PIr. *čášma- < PII *čáćšma- 'eye', the s-stem beside Skt. cákṣus-; Hübschmann, Pers. Stud.: 'čašm “Auge” = zd. čašman-, skr. cakṣus'. (2) âgâh < MP āgāh (ʾkʾs) 'aware, knowing' < OIr. *ā-kāsa-, a verbal noun to ā-kas- 'to perceive'; the -s > -h weakening of intervocalic/final Iranian *-s- in this word is the same as in MP nikās > NP negâh. Mo'in's etymological footnote in Borhan-e Qate' (p.52) puts it plainly: 'آگاه — اوستا … بمعنی مکشف شدن، مشاهده کردن؛ سانسکریت ākāśa- «ظاهر شد» … و نگاه در فارسی از همین [ریشه]'. (3) negâh < MP nikās < OIr. *ni-kāsa- 'a looking down/at' (Nourai's Av. ni-kasa), Mo'in's footnote (BQT p.2163): 'نگاه … اوستا *ni-kāsa- (قس: آگاه)، پهلوی nikās، بلوچی nigāh … ریشهٔ آن kas (دیدن، نگریستن) است، بارتولمه ۴۰۹'. (4) govâh < MP gugāy / gukās 'witness', gukāsīh 'testimony' < OIr. *ui-kāsa-/*ui-kāya- 'seeing apart, discriminating' with the regular south-western Iranian development of initial *ui- > gu- (Armenian borrowed the Parthian-type form as vkay). Horn, Grundriss no. 166-ff. (p.210, no. 940): 'guvāh, guvā “Zeuge”. ai. vi + √kāś- Intens. “ausschauen, erschauen, wahrnehmen”; phlv. gukās “Zeuge”, gukāsīh; arm. LW. vkay “Zeuge”.'\",\n \"derivation_fa\": \"هر چهار واژه بازماندهٔ منظم ریشهٔ *kʷeḱ- اند و هر چهار در همان صفحهٔ پوکورنی که نورایی به آن ارجاع داده نام برده شده‌اند. «چشم» از فارسی میانهٔ čašm، از ایرانی آغازین *čášma-، هم‌ریشه با سنسکریت cákṣus-؛ هوبشمان نیز می‌نویسد «čašm = اوستایی čašman-، سنسکریت cakṣus». «آگاه» از فارسی میانهٔ āgāh (ʾkʾs) از ایرانی باستان *ā-kāsa-؛ سینِ پایانیِ ایرانی در این واژه به «ه» بدل شده، درست همان‌گونه که در nikās > نگاه. حاشیهٔ معین در برهان قاطع (ص ۵۲) همین را می‌گوید و «نگاه» را نیز به همین ریشه بازمی‌گرداند. «نگاه» از *ni-kāsa- «فرونگریستن» است (حاشیهٔ معین، ص ۲۱۶۳، با ارجاع به بارتولمه ستون ۴۰۹). «گواه» از فارسی میانهٔ gugāy/gukās «شاهد» و gukāsīh «شهادت»، از *ui-kāsa-/*ui-kāya-، با تحول جنوب‌غربیِ *ui- به gu-؛ ارمنی vkay وام‌واژه‌ای از همین است. ادعای نورایی در هر چهار مورد درست است.\",\n \"sources\": [\n   \"https://en.wiktionary.org/wiki/%DA%86%D8%B4%D9%85\",\n   \"https://en.wiktionary.org/wiki/%D8%A2%DA%AF%D8%A7%D9%87\",\n   \"https://en.wiktionary.org/wiki/%D9%86%DA%AF%D8%A7%D9%87\",\n   \"https://en.wiktionary.org/wiki/%DA%AF%D9%88%D8%A7%D9%87\"\n ],\n \"ref_check\": [\n   {\"ref\": \"BQT:52\", \"status\": \"supports\",\n    \"note\": \"Borhan-e Qate' vol.1 p.52 = BQT_v1_pages.txt leaf 262 (printed ≈ leaf − 210); Mo'in's footnote s.v. آگاه: 'آگاه - اوستا … بمعنی مکشف شدن، مشاهده کردن؛ سانسکریت [ākāśa] «ظاهر شد»؛ [ایرانی] شرقی … «نگاه دن»، … «چشم»، و نگاه در فارسی از همین …' — links آگاه, نگاه and چشم to one root, as the chart does.\"},\n   {\"ref\": \"BQT:638\", \"status\": \"partial\",\n    \"note\": \"BQT_v2_pages.txt leaf 95 (= p.638 on the documented +543 offset) is the چ-س/چ-ش block and carries the cross-reference 'چاشت … رك: چشم، چشام'; the etymological footnote for چشم itself ('… اوستا [ča]šman- …') stands one leaf on, leaf 96 = printed 639. The headword is where Nourai points, within the ±1 uncertainty of the vol.2 leaf-to-page offset.\"},\n   {\"ref\": \"BQT:1849\", \"status\": \"supports\",\n    \"note\": \"Rendered with tools/ref_page.py BQT:1849 (BQT_v3 pdf p.646). Mo'in's footnote 5 s.v. گواه: 'گواه — بضم اول و های ملفوظ، پهلوی gōkās, gōkāsīh (شهادت)، از *ui-kāsa (قس: *ui-kāya)؛ فارسی: گواه از gawāh از *gaw-kāsa (شکل جنوب غربی) «نیبرگ ص ۸۵» و رک: هوبشمان.' Exactly Nourai's vi-kaya → govâh.\"},\n   {\"ref\": \"BQT:2163\", \"status\": \"supports\",\n    \"note\": \"Rendered with tools/ref_page.py BQT:2163 (BQT_v4 pdf p.246). Footnote 8 s.v. نگاه: 'نگاه — بکسر اول. اوستا *ni-kāsa- (قس: آگاه)، پهلوی nikās، کردی …، بلوچی nigāh؛ … ریشهٔ آن kas (دیدن، نگریستن) است، بارتولمه ۴۰۹.'\"},\n   {\"ref\": \"HRN:210\", \"status\": \"supports\",\n    \"note\": \"Horn, Grundriss p.210 (HRN.txt leaf 231, printed = leaf − 21), entry no. 940: 'guvāh, guvā “Zeuge”. ai. vi + √kāś- Intens. “ausschauen, erschauen, wahrnehmen”; phlv. gukās “Zeuge”, gukāsīh (Mēn.), arm. LW. vkay “Zeuge”, vkayem “ich bezeuge”.'\"}\n ],\n \"consulted\": [\n   {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien (HUB.txt lines 5671, 5750, 8422)\", \"stance\": \"supports\",\n    \"note\": \"'čašm “Auge” = zd. čašman-, skr. cakṣus'; '… gukās “Zeuge” = np. guvāh, skr. *vikāśa-'; '“Zeugniss” = phl. gukāsīh Shk. 247, Mīn. Gl. 95, np. guvāh'.\"},\n   {\"src\": \"PHD\", \"where\": \"MacKenzie, CPD p.22 and p.93 (PHD.txt lines 297-298, 4578)\", \"stance\": \"supports\",\n    \"note\": \"The Middle Persian antecedents are all in MacKenzie: čašm 'eye', and the ā-kās/nikās family; 'čāštan, čāš- [c’š-tn’] teach' stands on p.22.\"},\n   {\"src\": \"POK\", \"where\": \"IEW 638-639 (POK_full.txt line ~52636)\", \"stance\": \"supports\",\n    \"note\": \"'npers. āgāh “expert, skillful”, nigāh “sight” … npers. čašm' — three of the four Persian words are printed in Pokorny's own entry.\"},\n   {\"src\": \"ARY\", \"where\": \"Aryanpur, Farhang-e rishe-hā, pdf p.224-225 (ARY_pages.txt leaf 223)\", \"stance\": \"supports\",\n    \"note\": \"The چشم article gives Avestan / Old Persian / Pahlavi / Kurdish / Baluchi / Sanskrit / Greek columns and the note 'بازگشت به: چشم، آگاه، نگاه' — the same family Nourai draws.\"}\n ]\n})\n\ne1[\"nodes\"].append({\n \"id\": 3, \"lang\": \"Pahlavi\",\n \"words\": \"čâšišn; čâšîtan\",\n \"verdict\": \"plausible\",\n \"derivation\": \"The forms are real Middle Persian, but their glosses and their attachment to this root are both contested. MacKenzie CPD p.22 has 'čāštan, čāš- [c’š-tn’] teach. ~išn: teaching' and, separately, 'čaxšišn [chššn | M, J cxš, N čaš-] taste, flavour' with 'čaxšāgīh (sense of) taste'; Bartholomae likewise gives 'np. (Pü.) čāšītan “lehren”'. So čāšītan/čāšišn as written mean 'to teach / teaching' and descend regularly from Av. čaš- (*kʷéḱ-s-) — that edge is confirmed — while the words for 'taste' are MP čaxšīdan/čaxšišn and čāšnīg. Nourai's 'taste' gloss comes from Bailey, whom he cites: DKS s.v. tcāś- 'see' ends 'With -š-, Zor.P. čāštan “teach”, čāšn “taste”: beside vicasišnīh', i.e. Bailey does file the taste-word under kas-. Cheung 2007 flatly rejects this: he sets up *čaš² 'to drip; to drink, eat?' (MP čāxš- 'to let taste', čāšnīg 'taste', BMP čāšt 'meal') with 'PIE —' and writes 'The attempt of Rastorgueva–Edel'man, ESIJa II, to link it to *kas¹ “to look, appear” and *čaš¹ “to teach, show” meets semantic difficulties … the original meaning of *čaš is perhaps rather “to drip, sprinkle, drink”.' Verdict: the arrow Av. čaš- → MP čāštan is confirmed for the sense 'teach'; for the sense 'taste' it is a live minority position (Bailey, ESIJa) that the current standard etymological dictionary of Iranian verbs denies.\",\n \"derivation_fa\": \"این صورت‌ها فارسی میانهٔ اصیل‌اند، اما هم معنایی که نورایی داده و هم بستگی‌شان به این ریشه محل بحث است. مکنزی در فرهنگ پهلوی ص ۲۲ می‌آورد: «čāštan, čāš- آموختن؛ čāšišn: آموزش» و جداگانه «čaxšišn: مزه، طعم»؛ بارتولمه نیز «فارسی میانه čāšītan “آموختن”» دارد. پس čāšītan/čāšišn در معنای «آموزاندن/آموزش» است و به‌طور منظم از اوستایی čaš- (*kʷéḱ-s-) می‌آید — و این پیوند پذیرفتنی است — حال آنکه واژهٔ «مزه» در پهلوی čaxšīdan/čaxšišn و čāšnīg است. معنای «چشیدن» را نورایی از بیلی گرفته که در فرهنگ ختنی ذیل tcāś- می‌نویسد: «با š: پهلوی čāštan “آموختن”، čāšn “مزه”». اما چونگ (۲۰۰۷) این را رد می‌کند و ریشهٔ جداگانهٔ *čaš² «چکیدن؛ نوشیدن، خوردن» را با تصریح «بدون ریشهٔ هندواروپایی» می‌نهد و پیوند آن را با *kas¹ و *čaš¹ از نظر معنایی نااستوار می‌داند. بنابراین: با احتیاط پذیرفتنی است.\",\n \"sources\": [\"https://en.wiktionary.org/wiki/%DA%86%D8%B4%DB%8C%D8%AF%D9%86\"],\n \"ref_check\": [\n   {\"ref\": \"ISS:98\", \"status\": \"supports\",\n    \"note\": \"Bailey's Indo-Scythian Studies VI itself is not online, but the same author's Dictionary of Khotan Saka (ISS_alt_DKS.txt line 2846, s.v. tcāś- 'see') carries the identical claim: 'Base cas-, from kas- “see” … IE Pok. 638-9 kʷeḱ- … With -š-, Zor.P. čāštan “teach”, čāšn “taste”: beside vicasišnīh.' So ISS:98 is being cited for a position Bailey demonstrably held.\"}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"MacKenzie, CPD p.22 (PHD.txt line 297-298)\", \"stance\": \"partial\",\n    \"note\": \"'čāštag [c’štk’] doctrine. čāštan, čāš- [c’š-tn’] teach. ~išn: teaching. … čaxšāgīh (sense of) taste. čaxšišn [chššn | M, J cxš, N čaš-] taste, flavour.' MacKenzie's čāšišn is 'teaching', not 'taste'.\"},\n   {\"src\": \"CHEUNG\", \"where\": \"Etymological Dictionary of the Iranian Verb, s.vv. *čaš¹ and *čaš² (CHEUNG.txt lines 3431-3520)\", \"stance\": \"contradicts\",\n    \"note\": \"*čaš¹ 'to teach, show': 'BMP čāš- “to teach” … Inf.: caus. BMP c’stn /čāštan/ … PIE ? *kʷe-kʷḱ- … Pok.: 638'. *čaš² 'to drip; to drink, eat ?': 'MMP c’xs- (redupl.) “to let taste”, MMP c’šnyg “taste”, BMP c’st /čāšt/ “meal” … PIE — … The attempt of Rastorgueva–Edel’man … to link it to *kas¹ … and *čaš¹ … meets semantic difficulties.'\"},\n   {\"src\": \"BRT\", \"where\": \"Bartholomae, AiW col. 462 s.v. 1. čas- (BRT.txt line 9453)\", \"stance\": \"partial\",\n    \"note\": \"'1. čas- V. lehren … ai. cáṣṭe “er sieht”, mp. čāštan (s. zu Pū.), … np. (Pü.) čāšītan “lehren”.' The form čāšītan is Bartholomae's, glossed 'to teach'.\"},\n   {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II (NYB_vol2_glossary.txt), searched čāšišn / čāštan / čaxšišn\", \"stance\": \"silent\",\n    \"note\": \"No usable entry recovered from the OCR for these headwords.\"}\n ]\n})\n\ne1[\"nodes\"].append({\n \"id\": 4, \"lang\": \"Persian\",\n \"words\": \"čašîdan «چشیدن»; čâšt «چاشت» (extras: چشایی ، چاشنی)\",\n \"verdict\": \"plausible\",\n \"derivation\": \"NP čašîdan 'to taste' (pres. stem čaš-) continues MP čaxšīdan/čaxš- (MacKenzie: 'čaxšišn … | M, J cxš, N čaš- | taste, flavour'), and čâšt 'morning meal, forenoon' continues BMP čāšt 'lunch, meal' (Wiktionary: 'Inherited from Middle Persian čāšt “lunch, meal”. Akin to Old Armenian ճաշ (čaš), an Iranian borrowing'); the extras چاشنی and چشایی are the same stem (MP čāšnīg 'taste' and a modern -āyī abstract). Sogdian pčš- 'to taste', Yaghnobi p’čas-/p’čāsta 'to taste, try' and Armenian čaš 'breakfast', čašak 'taste' belong with them. The disputed point is only the top of the chain. Nourai, following Bailey, takes the whole group back to Av. čaš- 'to see, teach' (< *kʷeḱ-); Wiktionary stops at 'Proto-Iranian *čaš- “to taste”' and adds 'Compare Sanskrit caṣ “to eat, taste”, although Cheung believes this is a late loanword from Iranian', i.e. no PIE ancestry is offered. Cheung 2007 gives *čaš² 'PIE —' and rejects the link on semantic grounds ('starting from “to see, be shown” the assumed shift to “to try” is not very likely'). Aryanpur's Persian root-dictionary sits with Nourai (his چشیدن note reads 'چم این واژه در زبان پهلوی: آموختن، مزه کردن؛ بازگشت به: چشم، آگاه، نگاه') but adds the alternative 'احتمال کمتری وجود دارد که «چشیدن» از واجریشهٔ هند و اروپایی *ǵeus- (لاتین gustāre، انگلیسی choose) باشد'. So: forms and Iranian pedigree confirmed, the *kʷeḱ- attachment accepted by some (Bailey, ESIJa, Aryanpur, Mo'in) and denied by the current standard (Cheung).\",\n \"derivation_fa\": \"«چشیدن» (ستاک حال: چش-) دنبالهٔ فارسی میانهٔ čaxšīdan/čaxš- است (مکنزی: čaxšišn «مزه، طعم»، در فارسی نو čaš-)، و «چاشت» دنبالهٔ فارسی میانهٔ čāšt «خوراک نیمروز» است؛ ارمنی čaš «چاشت» و čašak «مزه» وام‌واژه‌هایی از ایرانی‌اند و سغدی pčš- «چشیدن» و یغنابی p’čas- نیز از همین خانواده‌اند. واژه‌های افزودهٔ «چاشنی» (از پهلوی čāšnīg) و «چشایی» نیز از همین ستاک‌اند. نکتهٔ محل اختلاف تنها سرِ زنجیره است: نورایی به پیروی از بیلی همهٔ این خانواده را به اوستایی čaš- «دیدن، آموختن» (از *kʷeḱ-) می‌رساند، اما ویکی‌واژه فقط تا «ایرانی آغازین *čaš- “چشیدن”» پیش می‌رود و ریشهٔ هندواروپایی نمی‌دهد، و چونگ صریحاً پیوند معنایی «دیدن ← چشیدن» را نااستوار می‌خواند. آریان‌پور همسو با نورایی است ولی خود احتمال دیگری (*ǵeus-، لاتین gustāre) را نیز یاد می‌کند. پس: با احتیاط پذیرفتنی است.\",\n \"sources\": [\n   \"https://en.wiktionary.org/wiki/%DA%86%D8%B4%DB%8C%D8%AF%D9%86\",\n   \"https://en.wiktionary.org/wiki/%DA%86%D8%A7%D8%B4%D8%AA\"\n ],\n \"ref_check\": [\n   {\"ref\": \"ISS:98\", \"status\": \"supports\",\n    \"note\": \"Same Bailey passage as node #3 (ISS_alt_DKS.txt line 2846 s.v. tcāś-): '… With -š-, Zor.P. čāštan “teach”, čāšn “taste”' — Bailey's own linking of the taste-words to kas- 'see', which is what Nourai's arrow reproduces. ISS VI p.98 itself could not be consulted (Khotanese Texts VI is not online).\"}\n ],\n \"consulted\": [\n   {\"src\": \"CHEUNG\", \"where\": \"s.v. *čaš² 'to drip; to drink, eat ?' (CHEUNG.txt lines 3487-3516)\", \"stance\": \"contradicts\",\n    \"note\": \"'*NWIR: NP čašīdan/čaš- … NP čāšt “noon; breakfast” … *MISC: Arm. (LW) čaš “breakfast”, čašak “taste” … The root is exclusively Iranian … *PIE — | LIV: — | Pok.: —'.\"},\n   {\"src\": \"PHD\", \"where\": \"MacKenzie, CPD p.22 (PHD.txt line 297-298)\", \"stance\": \"supports\",\n    \"note\": \"'čāšt [c’št’ | N ~] lunch, meal' and 'čaxšišn [chššn | M, J cxš, N čaš-] taste, flavour' — the direct Middle Persian antecedents of چاشت and چشیدن.\"},\n   {\"src\": \"ARY\", \"where\": \"Aryanpur, pdf p.224-225 (ARY_pages.txt leaf 223)\", \"stance\": \"partial\",\n    \"note\": \"'چم این واژه در زبان پهلوی: آموختن، مزه کردن. بازگشت به: چشم، آگاه، نگاه. احتمال کمتری وجود دارد که «چشیدن» از واجریشهٔ هند و اروپایی *ǵeus- (لاتین gustāre، انگلیسی choose) باشد.' Follows Nourai's grouping but flags a rival etymology.\"},\n   {\"src\": \"BQT\", \"where\": \"Borhan-e Qate' vol.2 p.638 (BQT_v2_pages.txt leaf 95)\", \"stance\": \"supports\",\n    \"note\": \"The چاشت / چشته block carries the cross-reference 'چاشت … رك: چشم، چشام' — Mo'in's edition too files چاشت with چشم.\"}\n ]\n})\n\njson.dump(e1, open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'p290','e1.json'),'w',encoding='utf-8'), ensure_ascii=False, indent=1)\nprint(\"entry1 nodes:\", len(e1[\"nodes\"]))\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build290a.py",
 "description": "Build entry 1 of page 290"
}
```


### [2026-09-06T22:25:48.265Z] TOOL RESULT

```
entry1 nodes: 4
```


## [2026-09-06T22:33:01.259Z] TOOL CALL #103: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build290b.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, os\nD = os.path.join(os.path.dirname(os.path.abspath(__file__)),'p290')\n\ne2 = {\n \"entry\": 2,\n \"root\": \"Kwel, Qwel\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *kʷel- / *kʷelh₁- 'to turn, revolve, move around; to sojourn, dwell'\",\n \"note\": \"Root name, language label and gloss are all correct and are again taken over almost verbatim from Nourai's Western handbooks: Watkins/AHD 'kʷel-1. To revolve, move around, sojourn, dwell. … [Pok. 1. kʷel- 639.]'; Walde-Pokorny I 514 'qʷel- „drehen, sich drehen“ (qʷeklo-s, qʷolo-s, qʷe-qʷlo „Rad, Drehpunkt“)' — the source of the alternative spelling 'Qwel'; Wiktionary reconstructs *kʷelh₁- 'to turn (end-over-end); to revolve around, and therefore to sojourn, to dwell'. Pokorny's entry runs pp. 639-640, so Nourai's POK:640 points inside it (Watkins cites the same entry as 639). One cross-cutting caveat for the whole chart: Pokorny's entry is a very broad one that modern work (LIV, Cheung) splits into *kʷelh₁- 'to turn/move', *kʷels- 'to plough' and a causative *kʷolh₁-eie- that is hard to keep apart from *kʷerH- 'to sow'; nodes #12-#14 sit on that fault line. A second, purely editorial point: in the Persian box (#5) the book prints the transliteration 'zâr 2' but the Persian script '‑زار ۳' — the homograph number disagrees with itself on the printed page; the JSON reproduces the page faithfully.\",\n \"note_fa\": \"نام ریشه، برچسب زبانی و معنای آن هر سه درست است و باز هم تقریباً واژه‌به‌واژه از دستنامه‌های غربی گرفته شده: واتکینز «kʷel-1. To revolve, move around, sojourn, dwell … [Pok. 639]» و والده–پوکورنی جلد یکم ص ۵۱۴ «qʷel- „drehen, sich drehen“ (qʷeklo-s, qʷolo-s, qʷe-qʷlo „Rad“)» — که خاستگاه املای دوم «Qwel» است. ویکی‌واژه صورت *kʷelh₁- «چرخیدن؛ گردیدن و ازاین‌رو ماندن و سکونت گزیدن» را بازسازی می‌کند. مدخل پوکورنی صفحه‌های ۶۳۹ تا ۶۴۰ را در بر می‌گیرد، پس ارجاع POK:640 نورایی درون همان مدخل است. یک هشدار کلی: پژوهش امروزی (LIV و چونگ) این مدخلِ فراخ را به *kʷelh₁- «گشتن»، *kʷels- «شخم زدن» و سببیِ *kʷolh₁-eie- تقسیم می‌کند که تفکیک آن از *kʷerH- «کاشتن» در زبان‌های ایرانی ممکن نیست؛ خانه‌های ۱۲ تا ۱۴ درست روی همین شکاف نشسته‌اند. نکتهٔ ویرایشی: در خانهٔ فارسیِ شمارهٔ ۵، کتاب در لاتین «zâr 2» و در خط فارسی «ـزار ۳» چاپ کرده؛ یعنی شمارهٔ هم‌نگاشت در خودِ صفحهٔ چاپی ناهمخوان است و استخراج، صفحه را درست بازتاب داده است.\",\n \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/k%CA%B7el-\"],\n \"ref_check\": [\n   {\"ref\": \"POK:640\", \"status\": \"supports\",\n    \"note\": \"Pokorny IEW, POK_full.txt block ending 'Page(s): 639-640': 'Root / lemma: kʷel-1, kʷelə- … Meaning: to turn; wheel; neck? … Old Indic carati, calati “moves, walks, grazes, drives” … Avestan caraiti … s-extension in Old Indic karṣū- f. “furrow”, karṣati, kṛṣati “turn over, plough”, Avestan karša- m. n. “furrow” … Old Indic cakra- “cartwheel, disc, circle”, Avestan caxra- m. “wheel” … Latin colō “to till, tend, cultivate” … References: WP. I 514 f.' Nourai's gloss 'to move around, dwell' is Pokorny's 'sich herumtreiben, wohnen'; the page he cites falls inside the entry.\"}\n ],\n \"consulted\": [\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985, AHD_watkins1985.txt line 650\", \"stance\": \"supports\",\n    \"note\": \"'kʷel-1. To revolve, move around, sojourn, dwell. I. Basic form *kʷel- in Latin colere … III. Suffixed reduplicated form *kʷ(e)-kʷl-o-, circle … 3. Sanskrit cakram, circle: CHUKKER … [Pok. 1. kʷel- 639.]'\"},\n   {\"src\": \"WLD\", \"where\": \"Walde-Pokorny I 514-515 (WLD_Bd1_pages.txt leaves 522-523)\", \"stance\": \"supports\",\n    \"note\": \"p.514 running head 'qʷem — qʷel-' and the headword 'qʷel- „drehen, sich drehen“ (qʷeklo-s, qʷolo-s, qʷe-qʷlo „Rad, Drehpunkt“)'; p.515 'ai. cakrá- … „Wagenrad, Scheibe, Kreis“, av. caxra- m. „Rad“, gr. κύκλος „Kreis“'.\"},\n   {\"src\": \"SYN\", \"where\": \"Buck §10.76 WHEEL, pp.724-725 (SYN.txt leaf 787)\", \"stance\": \"supports\",\n    \"note\": \"'1. IE *kʷelo-s, *kʷolo-s, redupl. *kʷekʷlo-s, fr. *kʷel- in Skt. car- “move, wander”, Grk. πέλομαι “be in motion”, etc. Walde-P. 1.514 ff.'\"},\n   {\"src\": \"IEC\", \"where\": \"Mann, IECD col. ~1023-1030 s.vv. quel-, quequlos (IEC.txt lines 13927, 13974)\", \"stance\": \"supports\",\n    \"note\": \"'quel- radical of general sense “turn; go”. See following entries'; 'quequlos, ququlos, ā, om “turning, wheel, rim”. WP I, 515 … Skt. cakráḥ … “wheel”; Av. čakram, n. id.; Per. … čarxe “wheel, reel”.'\"}\n ],\n \"nodes\": []\n}\nN = e2[\"nodes\"]\n\nN.append({\n \"id\": 1, \"lang\": \"Avestan / Old Persian\",\n \"words\": \"čaxra, čakra, caxra\",\n \"verdict\": \"plausible\",\n \"derivation\": \"Av. caxra- m. 'wheel' is the reduplicated thematic *kʷe-kʷl-o- > PII *čakrám (Skt. cakrá- 'wheel, disc, circle'), with the regular Iranian change of the cluster *-kr- to *-xr- after the first syllable; the by-form 'čakra' that Nourai prints beside it is the Indo-Iranian/Sanskrit shape and is also the spelling Buck uses for Avestan ('Av. čakra-', §12.82). The derivation itself is textbook: Pokorny 640, Walde-Pokorny I 515, Buck §10.76 and §12.82, Mann s.v. quequlos, Wiktionary (*kʷékʷlos > PIr. *čaxrám > Av. caxra). What is not supportable is half of the language label: čaxra- is Young Avestan, but Old Persian does not attest it — Kent's lexicon has no caxra- (his kar- is the unrelated 'to do, make'), and no Achaemenid inscription contains the word. The label should read 'Avestan'.\",\n \"derivation_fa\": \"اوستایی caxra- «چرخ» بازماندهٔ صورت دوگان‌شدهٔ *kʷe-kʷl-o- است که در هندوایرانی *čakrám شده (سنسکریت cakrá- «چرخ، قرص، دایره») و در ایرانی خوشهٔ *-kr- به *-xr- بدل گشته است. گونهٔ «čakra» که نورایی در کنار آن آورده همان صورت هندوایرانی است و اتفاقاً باک نیز اوستایی را «čakra-» می‌نویسد. خودِ این اشتقاق در پوکورنی ص ۶۴۰، والده–پوکورنی جلد یکم ص ۵۱۵، باک بندهای ۱۰٫۷۶ و ۱۲٫۸۲، مان و ویکی‌واژه یکسان آمده است. آنچه پذیرفتنی نیست نیمی از برچسب زبانی است: caxra- اوستایی نو است، اما در پارسی باستان گواهی نشده — در واژه‌نامهٔ کنت چنین واژه‌ای نیست و در سنگ‌نبشته‌های هخامنشی نیامده. برچسب درست تنها «اوستایی» است.\",\n \"sources\": [\"https://en.wiktionary.org/wiki/%DA%86%D8%B1%D8%AE\"],\n \"ref_check\": [\n   {\"ref\": \"POK:640\", \"status\": \"supports\",\n    \"note\": \"POK_full.txt, kʷel-1 entry: 'kʷeklo-, kʷokʷlo-(?) “wheel” in: In a-grade: Old Indic cakra- m. n. “cartwheel, disc, circle”, Avestan caxra- m. “wheel”.' This part of the entry stands on p.640, exactly the page cited.\"},\n   {\"ref\": \"SYN:725\", \"status\": \"supports\",\n    \"note\": \"Buck §10.76 WHEEL (SYN.txt leaf 787, printed pp.724-725): word table gives 'Av. čaxra-'; discussion: '1. IE *kʷelo-s, *kʷolo-s, redupl. *kʷekʷlo-s, fr. *kʷel- in Skt. car- “move, wander” … Skt. cakra-, Av. čaxra-'.\"},\n   {\"ref\": \"SYN:905\", \"status\": \"supports\",\n    \"note\": \"Buck §12.82 CIRCLE (SYN.txt leaf 977, running head '906 SELECTED INDO-EUROPEAN SYNONYMS'; section printed pp.905-906): 'Skt. cakra- “wheel, circle”, Av. čakra-, ON hjól, OE hweol, etc. “wheel” (10.76), fr. reduplicated forms of the root *kʷel- in Grk. πέλομαι “be in motion”, Skt. car- “move about”.' Note Buck's spelling 'čakra-' for Avestan, which is where Nourai's second variant comes from.\"},\n   {\"ref\": \"BQT:629\", \"status\": \"partial\",\n    \"note\": \"BQT_v2_pages.txt: the چرخ article and Mo'in's footnote fall on leaf 87 (= printed 630 on the documented +543 offset), one page past the cited 629; the footnote reads '… پهلوی [čarx]، اوستا -[čaxra]، هندی باستان [cakra]-' with an ESIJ-style reference. Within the ±3 uncertainty of the vol.2 offset the citation lands on the right article.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KNT\", \"where\": \"Kent, Old Persian, Lexicon (KNT.txt, searched caxra / čaxra / kar-)\", \"stance\": \"contradicts\",\n    \"note\": \"No caxra- in Kent's Old Persian lexicon; his only kar- entry is 'kar- “make, do”, OP pres. kunautiy, impf. pass. akariya'. The 'Old Persian' half of Nourai's language label is unsupported.\"},\n   {\"src\": \"BRT\", \"where\": \"Bartholomae, AiW (BRT.txt line 11131)\", \"stance\": \"supports\",\n    \"note\": \"'čaxra-vant- Adj. (fem. -vaitī-) „ein Rad (als Feldzeichen) führend“' — the derivative presupposes the headword čaxra- 'Rad'.\"},\n   {\"src\": \"Wiktionary\", \"where\": \"چرخ, Persian section\", \"stance\": \"supports\",\n    \"note\": \"'from Proto-Iranian *čaxrám (compare Avestan 𐬗𐬀𐬑𐬭𐬀 (caxra, “wheel”)), from Proto-Indo-Iranian *čakrám (compare Sanskrit चक्र (cakrá)), from Proto-Indo-European *kʷékʷlos (“wheel, circle”)'.\"}\n ]\n})\n\nN.append({\n \"id\": 2, \"lang\": \"Persian\",\n \"words\": \"čarx «چرخ»\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"NP čarx < MP čarx / Manichaean MP čahr (written chr) 'wheel, cycle' < PIr. *čaxrám, i.e. the very Avestan word of node #1, with metathesis of the cluster -xr- > -rx- in the Middle Persian period (the same metathesis as in MP taxm > NP tarx-, and cf. Manichaean čahr with -xr- resolved instead by vocalising the x). Hübschmann states it flatly: 'čarx “Rad” (arm. čaxr, čaxarak) = zd. čaxra-'; Armenian čaxr / čaxarak are earlier Iranian loans that preserve the unmetathesised order and so date the Persian metathesis. Mann's dictionary prints the Persian outcome in the same entry as the Avestan and Sanskrit ('Per. … čarxe “wheel, reel”'), and Mo'in's footnote in Borhan-e Qate' gives the chain 'پهلوی — اوستا čaxra- — هندی باستان cakra-'. In modern Persian the word also means 'sphere, firmament, fortune', a secondary astronomical use already in Middle Persian.\",\n \"derivation_fa\": \"«چرخ» از فارسی میانهٔ čarx (در مانوی čahr، نوشتهٔ chr) «چرخ، گردونه» است، از ایرانی آغازین *čaxrám — یعنی همان واژهٔ اوستاییِ خانهٔ پیشین — با قلبِ خوشهٔ ‑xr‑ به ‑rx‑ در دورهٔ میانه. ارمنی čaxr و čaxarak که وام‌واژه‌های کهن‌تر ایرانی‌اند ترتیب اصلی را نگاه داشته‌اند و ازاین‌رو زمان این قلب را نشان می‌دهند. هوبشمان می‌نویسد: «čarx “چرخ” (ارمنی čaxr، čaxarak) = اوستایی čaxra-». حاشیهٔ معین در برهان قاطع نیز زنجیرهٔ «پهلوی — اوستا čaxra- — هندی باستان cakra-» را می‌دهد. معنای ثانویِ «فلک، آسمان، بخت» کاربردی نجومی است که از فارسی میانه پیداست. ادعای نورایی درست است.\",\n \"sources\": [\"https://en.wiktionary.org/wiki/%DA%86%D8%B1%D8%AE\"],\n \"ref_check\": [\n   {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Nourai gives no reference for this node; the claim is checked against Hübschmann, Mann, Mo'in and Wiktionary instead (see consulted).\"}\n ],\n \"consulted\": [\n   {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien (HUB.txt line 8973)\", \"stance\": \"supports\",\n    \"note\": \"'čarx “Rad” (arm. čaxr, čaxarak) = zd. čaxra-.'\"},\n   {\"src\": \"IEC\", \"where\": \"Mann, IECD s.v. quequlos (IEC.txt line 13974)\", \"stance\": \"supports\",\n    \"note\": \"'quequlos … “turning, wheel, rim”. WP I, 515 … Skt. cakráḥ … “wheel”; Av. čakram, n. id.; Per. čakle “district”; čarǧ “wheel; ball; vault of sky”; čarxe “wheel, reel”.'\"},\n   {\"src\": \"BQT\", \"where\": \"Borhan-e Qate' vol.2 p.630 (BQT_v2_pages.txt leaf 87)\", \"stance\": \"supports\",\n    \"note\": \"Mo'in's footnote to the چرخ article: '… پهلوی …، اوستا -[čaxra] ، هندی باستان -[cakra]'.\"},\n   {\"src\": \"Wiktionary\", \"where\": \"چرخ\", \"stance\": \"supports\",\n    \"note\": \"'From Middle Persian 𐫝𐫍𐫡 (chr /čahr/, “wheel, cycle”), from Proto-Iranian *čaxrám … from Proto-Indo-European *kʷékʷlos.'\"}\n ]\n})\n\nN.append({\n \"id\": 3, \"lang\": \"Avestan\",\n \"words\": \"car, čâr; wi-čâr\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Av. car- 'to come and go, move about, graze' (YAv. caraiti, fracaraiti, ham.caraŋʰa, vi-caraiiatəm) is the thematic present of PIE *kʷelh₁-; Sanskrit carati 'moves, walks, grazes' is its exact counterpart and stands in Pokorny's entry on p.639 as the first Indo-Iranian witness. The long-grade čār- that Nourai writes beside it is not an error but the Iranian lengthened stem that surfaces in the compound: Abolghasemi (FFD p.73, the reference Nourai cites) writes 'گزاردن: گزارد ← فارسی میانه wizārd < ایرانی باستان *wi-čār-ta … čār صورت بالندهٔ ریشهٔ čar به معنی «حرکت کردن» است'. So wi-čār = *ui- 'apart' + the long grade of car-, a causative-type formation whose Middle Iranian outcome is MP/Parthian wizār- 'to separate, to explain, to accomplish' (node #4) and NP gozârdan (node #5). Nourai's gloss 'to do' for wi-čār is a shortcut for the Middle Persian range 'perform, fulfil, discharge'; the Avestan compound itself means 'to go to and fro, move apart'.\",\n \"derivation_fa\": \"اوستایی car- «آمد و شد کردن، گشتن، چریدن» (caraiti، fracaraiti و…) ماضیِ ستاک ساده‌ی ریشهٔ *kʷelh₁- است و سنسکریت carati «می‌رود، می‌چرد» برابر دقیق آن است؛ پوکورنی در ص ۶۳۹ همین را نخستین گواه هندوایرانی می‌آورد. صورت čār- که نورایی در کنار آن نوشته خطا نیست بلکه ستاک بالندهٔ (کشیده‌ی) ایرانی است که در ترکیب پیدا می‌شود؛ ابوالقاسمی در «فعل‌های فارسی دری» ص ۷۳ — همان مرجعی که نورایی به آن ارجاع داده — می‌نویسد: «گزاردن: گزارد ← فارسی میانه wizārd < ایرانی باستان *wi-čār-ta… čār صورت بالندهٔ ریشهٔ čar به معنی حرکت کردن است». پس wi-čār همان *ui- «جدا» به‌علاوهٔ ستاک بلندِ car- است که در ایرانی میانه wizār- «جدا کردن، شرح دادن، به‌جا آوردن» شده است. معنای «انجام دادن» که نورایی داده در حقیقت معنای دورهٔ میانه است، نه معنای خودِ ترکیب اوستایی. ادعای نورایی درست است.\",\n \"sources\": [\"https://en.wiktionary.org/wiki/%DA%86%D8%B1%DB%8C%D8%AF%D9%86\"],\n \"ref_check\": [\n   {\"ref\": \"FFD:73\", \"status\": \"supports\",\n    \"note\": \"Abolghasemi, Fe'l-hā-ye Fārsi-ye Dari p.73 (FFD_pages.txt pdf page 78; printed = pdf − 5): 'گزاردن — گزارد ← فارسی میانه wizārd < ایرانی باستان *wi-čār-ta … wi پیشوند فعلی است. čār صورت بالندهٔ ریشهٔ čar به معنی «حرکت کردن» است. (چریدن) از ریشهٔ čar آمده است ← چریدن.' This is Nourai's node #3 and node #5 in one sentence.\"},\n   {\"ref\": \"BQT:635\", \"status\": \"not_found\",\n    \"note\": \"BQT_v2_pages.txt leaf 92 (= printed 635 on the documented +543 offset) is the چرم/چرمدان block; the چریدن material appears at leaf 84. The vol.2 OCR is too poor and the offset too loose (±3, plus running heads that OCR as words rather than numerals) to confirm which printed page carries the چریدن footnote, and no scan of Borhan vol.2 is wired into tools/ref_page.py.\"},\n   {\"ref\": \"DRM\", \"status\": \"not_checked\",\n    \"note\": \"Darmesteter, Études iraniennes is cited without a page; not pursued.\"}\n ],\n \"consulted\": [\n   {\"src\": \"CHEUNG\", \"where\": \"s.v. *čarH 'to come and go, wander' (CHEUNG.txt lines 3346-3425)\", \"stance\": \"supports\",\n    \"note\": \"'*AVESTAN: car- “to come and go” || (+ *para-) “to pass over” || (+ *ui-) “to go to and fro” … *MIDDLE PERSIAN: MMP čr- “to pasture, graze” || (+ *ui-) MMP wč’r-, BMP wc’l- /wizār-/ (caus.) “to separate, divide” … *PIE *kʷelH₁- “to move, turn, wander; to pasture; to settle and cultivate” … LIV: 386 ff. | Pok.: 639.'\"},\n   {\"src\": \"POK\", \"where\": \"IEW 639 (POK_full.txt, kʷel-1)\", \"stance\": \"supports\",\n    \"note\": \"'Old Indic carati, calati “moves, walks, grazes, drives” … Avestan caraiti “versatur, obliegt einer Tätigkeit”, carana- “Feld”; Old pers. parikara “Umlauf”.'\"},\n   {\"src\": \"BRT\", \"where\": \"Bartholomae, AiW s.v. 1. car- (BRT.txt, searched car-/caraiti)\", \"stance\": \"supports\",\n    \"note\": \"The AiW headword for car- 'sich bewegen, sich herumtreiben, weiden' underlies Cheung's Avestan citations (Cheung's 'Liste: 21 f.' is a reference to Bartholomae's numbering); the OCR of the Avestan headwords is too damaged to quote verbatim.\"}\n ]\n})\n\nN.append({\n \"id\": 4, \"lang\": \"Pahlavi\",\n \"words\": \"čâr; vâ-čar; wîzârdan\",\n \"verdict\": \"plausible\",\n \"derivation\": \"Two of the three are right; the analysis of the third is half wrong. (a) MP čar- 'to pasture, graze' (Manichaean MP čr-, Parthian čr-, MacKenzie's noun čarag 'pasture') continues Av. car- directly — confirmed. (b) wizārdan, wizār- 'separate; explain, interpret; perform, fulfil, redeem' is MacKenzie's own headword (CPD p.93: 'wizārdan, wizār- [wcl-tn’ | M wyc’rd, wyc’r-, J bz’rd-, N guzārdan]'), from *ui-čār- — confirmed. (c) 'vâ-čar : place to get together, bazaar ☞Abâ' is the problem. The Middle Persian word is wāzār (MacKenzie p.90: 'wāzār [w’c’l | M w’c’r-, N bāzār] market; wāzāragān merchant'), and its first element is not the preverb abā-/wā- 'with, together' that Nourai's cross-reference to 'Abâ' implies, but Old Iranian *wahā- 'sale, price' (PIE *wes- 'to buy, sell', Skt. vasná- 'purchase money'): Old Iranian *wahā-čarana- 'place where selling goes on'. Etymonline: 'Persian bazar (Pahlavi vacar) “a market,” from Old Iranian *vaha-carana “sale, traffic,” from suffixed form of PIE root *wes- (1) “to buy, sell” + PIE *kʷoleno-, suffixed form of root *kʷel-'; Wiktionary's etymology tree for بازار likewise shows two parents, *wes- and *kʷel-. Horn (no. 166, p.38) had already ruled out the competing analysis with a preverb: 'Wegen phlv. č ist die Zusammenstellung mit ap. *abačāriš unmöglich.' So the placement of the bazaar-word under *kʷel- is correct — it is the second member — but the gloss 'place to get together' and the ☞Abâ cross-reference are folk analysis.\",\n \"derivation_fa\": \"از سه صورت این خانه دو تا درست است و تحلیل سومی نیمه‌درست. نخست، فارسی میانهٔ čar- «چریدن» مستقیماً دنبالهٔ اوستایی car- است. دوم، wizārdan / wizār- «جدا کردن؛ شرح دادن، ترجمه کردن؛ به‌جا آوردن» سرواژهٔ خودِ مکنزی است (فرهنگ پهلوی ص ۹۳) و از *ui-čār- می‌آید. اما سوم، «vâ-čar» با ارجاع به «Abâ» نادرست است: صورت پهلوی wāzār است (مکنزی ص ۹۰: «wāzār … بازار») و جزء نخست آن پیشوند abā-/wā- «با، همراه» نیست، بلکه ایرانی باستان *wahā- «فروش، بها» است (از هندواروپایی *wes- «خریدن و فروختن»، سنسکریت vasná- «بهای خرید»): *wahā-čarana- «جای دادوستد». اتیمانلاین و ویکی‌واژه هر دو همین دو ریشه (*wes- و *kʷel-) را می‌آورند و هرن نیز از ۱۸۹۳ نوشته بود: «به سبب چِ پهلوی، سنجش با پارسی باستان *abačāriš ناممکن است». پس جای‌دادن «بازار» زیر ریشهٔ *kʷel- درست است — جزء دوم آن از این ریشه است — ولی معنای «جای گردهم‌آیی» و ارجاع به «اَبا» ریشه‌شناسی عامیانه است.\",\n \"sources\": [\n   \"https://www.etymonline.com/word/bazaar\",\n   \"https://en.wiktionary.org/wiki/%D8%A8%D8%A7%D8%B2%D8%A7%D8%B1\",\n   \"https://en.wiktionary.org/wiki/%DA%AF%D8%B2%D8%A7%D8%B1%D8%AF%D9%86\"\n ],\n \"ref_check\": [\n   {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Nourai gives no reference for this node; checked against MacKenzie, Horn, Hübschmann, Cheung, Etymonline and Wiktionary instead.\"}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"MacKenzie, CPD pp.90, 93 (PHD.txt lines 649, 655)\", \"stance\": \"partial\",\n    \"note\": \"'wāzār [w’c’l | M w’c’r-, N bāzār] market. wāzāragān [w’c’lk’n’ | M w’c’rg’n, N bāzārgān] merchant. ~īh: trade.' and 'wizārdan, wizār- [wcl-tn’ | M wyc’rd, wyc’r-, J bz’rd-, N guzārdan] separate; explain, interpret; perform, fulfil, redeem.' MacKenzie has wāzār (not vā-čar) and gives no preverbal analysis.\"},\n   {\"src\": \"HRN\", \"where\": \"Horn, Grundriss no. 166, p.38 (HRN.txt leaf 59)\", \"stance\": \"contradicts\",\n    \"note\": \"'166. bāzār “Markt”, bāzārgān … phlv. vāčar “Markt” (vergl. arm. LW. vačaṟ, vačaṟakan …) … Wegen phlv. č ist die Zusammenstellung mit ap. abačāriš unmöglich.' Horn explicitly rejects analysing the word with a preverb of the abā- type.\"},\n   {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien (HUB.txt lines 5429, 8048)\", \"stance\": \"supports\",\n    \"note\": \"'bāzār “Markt” = pāz. vazār Shk. 272, phl. …' and 'bāzār “Markt” = arm. vačaṟ' — confirms the Middle Persian/Pāzand form behind NP bāzār.\"},\n   {\"src\": \"CHEUNG\", \"where\": \"s.v. *čarH (CHEUNG.txt line ~3380)\", \"stance\": \"supports\",\n    \"note\": \"'(+ *ui-) ? BMP wcl- /wizār-/ “to get through”, MMP wč’r-, BMP wc’l- /wizār-/ (caus.) “to separate, divide” … Inf.: caus. BMP wc’ltn’ /wizārdan/.'\"}\n ]\n})\n\nN.append({\n \"id\": 5, \"lang\": \"Persian\",\n \"words\": \"čarîdan «چریدن»; zâr 2 «-زار ۳»; bâzâr «بازار»; gozârdan «گزاردن» (extras: بازرگان ، گلزار ، کارزار ، مرغزار ، چمنزار ، علفزار ، گزارش ، گزاره ، گزیر ، ناگزیر)\",\n \"verdict\": \"plausible\",\n \"derivation\": \"Three of the four are secure, one is not checkable. (a) čarîdan 'to graze' < MP čar- < PIr. *čárHati < PIE *kʷel- — Wiktionary states exactly this chain and cites Cheung and Hasandust for it. (b) gozârdan 'to perform, discharge; to translate, interpret' < MP wizārdan (Judeo-Persian bzārd-) < *ui-čār-, with the regular south-western development of initial *wi- > gu-/go-; the derivatives گزارش، گزاره، گزیر، ناگزیر hang off the same stem, and Hâfez's line quoted in the box ('حق نعمت می‌گزارم', 'I discharge the debt of the favour') illustrates precisely the 'fulfil, discharge' sense. One caveat that Wiktionary and Cheung both record: 'NP guzārdan with the meaning “to fulfil, accomplish, perform” may have a different origin: < *ui-kar-', i.e. the 'perform' sense may in part belong to kar- 'to do' rather than čar-. (c) bâzâr < MP wāzār < *wahā-čarana-: the second member is from this root, but the gloss '“place of assembly”' is wrong (it is 'place of selling'), and بازرگان is the same compound with the -gān suffix. (d) zâr 2 'place of, home of' (گلزار، مرغزار، چمنزار، علفزار، کارزار) — the standard handbooks used here (Horn, Hübschmann, MacKenzie, Cheung) do not treat this suffix, and the English Wiktionary has no page for the Persian suffix ‑زار (the entry زار is 'lament', a different word from *jāráyati); the connection with *čar- 'to graze, pasture' (via a *-čāra- 'grazing place', which would need an irregular č > z) is a common but here unverifiable claim. Also worth recording: the printed page gives 'zâr 2' in Latin but '‑زار ۳' in Persian script — the homograph number is inconsistent in the book itself, and the JSON reproduces the page correctly.\",\n \"derivation_fa\": \"از چهار واژهٔ این خانه سه تا استوارند و یکی وارسی‌ناپذیر. «چریدن» از فارسی میانهٔ čar-، از ایرانی آغازین *čárHati، از هندواروپایی *kʷel- است و ویکی‌واژه دقیقاً همین زنجیره را با ارجاع به چونگ و حسن‌دوست می‌آورد. «گزاردن» از فارسی میانهٔ wizārdan (در فارسی‌یهودی bzārd-) از *ui-čār- است، با تحول جنوب‌غربیِ *wi- به گُـ؛ واژه‌های گزارش، گزاره، گزیر و ناگزیر همه از همین ستاک‌اند و بیت حافظ در همان کادر («چه باشد حق نعمت می‌گزارم») درست همان معنای «ادا کردن» را نشان می‌دهد. یک نکتهٔ احتیاطی که هم چونگ و هم ویکی‌واژه می‌آورند این است که معنای «به‌جا آوردن، انجام دادن» ممکن است در بخشی از موارد از *ui-kar- (ریشهٔ «کردن») آمده باشد نه از čar-. «بازار» از wāzār از *wahā-čarana- است؛ جزء دومش از این ریشه است اما معنای «جای گردهم‌آیی» درست نیست («جای دادوستد» است)، و «بازرگان» همان ترکیب با پسوند ‑گان است. اما پسوند «ـزار» (گلزار، مرغزار، چمنزار، علفزار، کارزار) را هیچ‌یک از دستنامه‌های در دسترس (هرن، هوبشمان، مکنزی، چونگ) نپرداخته‌اند و ویکی‌واژه هم برای این پسوند مدخلی ندارد؛ پیوند آن با *čar- «چریدن» از راه *-čāra- «چراگاه» رایج است اما به بدل شدن چ به ز نیاز دارد که بی‌قاعده است و اینجا تأیید نشد. نکتهٔ دیگر: صفحهٔ چاپی در لاتین «zâr 2» و در خط فارسی «ـزار ۳» دارد؛ این ناهمخوانی از خودِ کتاب است و استخراج درست عمل کرده.\",\n \"sources\": [\n   \"https://en.wiktionary.org/wiki/%DA%86%D8%B1%DB%8C%D8%AF%D9%86\",\n   \"https://en.wiktionary.org/wiki/%DA%AF%D8%B2%D8%A7%D8%B1%D8%AF%D9%86\",\n   \"https://en.wiktionary.org/wiki/%D8%A8%D8%A7%D8%B2%D8%A7%D8%B1\",\n   \"https://www.etymonline.com/word/bazaar\"\n ],\n \"ref_check\": [\n   {\"ref\": \"FFD:73\", \"status\": \"supports\",\n    \"note\": \"Abolghasemi p.73 (FFD_pages.txt pdf 78): 'گزاردن — گزارد ← فارسی میانه wizārd < ایرانی باستان *wi-čār-ta … گزار ← فارسی میانه wizār < ایرانی باستان *wi-čār-a … (چریدن) از ریشهٔ čar آمده است ← چریدن.' Covers both گزاردن and چریدن exactly as the chart has them.\"},\n   {\"ref\": \"MON:1268\", \"status\": \"partial\",\n    \"note\": \"Mo'in, Farhang-e Fārsi has the headword (MON_part1.txt line 50225): 'چریدن — [چرا کردن] (مص م.) (چرید، چرد، خواهد چرید، بچر، چرنده، چریده؛ م: چراندن، چرانیدن) علف خوردن جانوران علفخوار در چراگاه، چرا کردن.' The available OCR of Mo'in carries no page numbers, so p.1268 could not be confirmed; چ falls in the right part of vol.1, so the citation is plausible.\"},\n   {\"ref\": \"BQT:614\", \"status\": \"not_found\",\n    \"note\": \"BQT_v2_pages.txt leaf 71 (= printed 614 on the documented +543 offset) is in the چال/چانه block; the چریدن and بازار articles are not there (بازار is in vol.1, under ب). Could not confirm what Nourai is pointing at; Borhan vol.2 is not covered by tools/ref_page.py.\"}\n ],\n \"consulted\": [\n   {\"src\": \"CHEUNG\", \"where\": \"s.v. *čarH, NWIR section (CHEUNG.txt line ~3395)\", \"stance\": \"partial\",\n    \"note\": \"'NP čarīdan “to graze, pasture” … || (+ *ui-) NP guzārdan/guzār- “to accomplish [work, job, etc.], perform [e.g. prayer]; to pay; to explain, interpret” … ◊ NP guzārdan/guzār- with the meaning “to fulfil, (accomplish, perform)” may have a different origin: < *ui-kar-.'\"},\n   {\"src\": \"PHD\", \"where\": \"MacKenzie, CPD pp.90, 93\", \"stance\": \"supports\",\n    \"note\": \"'wāzār … N bāzār'; 'wizārdan, wizār- … N guzārdan' — MacKenzie prints the New Persian outcomes بازار and گزاردن in the entries themselves.\"},\n   {\"src\": \"HRN\", \"where\": \"Horn, Grundriss no. 166, p.38 (HRN.txt leaf 59)\", \"stance\": \"supports\",\n    \"note\": \"'bāzār “Markt”, bāzārgān, bāzergān “Kaufmann” … phlv. vāčar “Markt” … np. bāzār ist allgemein entlehnt.' — covers both بازار and بازرگان of the extras.\"},\n   {\"src\": \"Wiktionary\", \"where\": \"چریدن; گزاردن; بازار\", \"stance\": \"supports\",\n    \"note\": \"چریدن: 'From Proto-Iranian *čárHati … from Proto-Indo-European *kʷel- (“to move; to turn (around)”)'. گزاردن: 'From Middle Persian wizārdan … from Proto-Iranian *wí (“apart”) + a causative formation from Proto-Iranian *čarH.' بازار: etymology tree 'PIE *wes- + PIE *kʷel- → Middle Persian wʾčʾl → Classical Persian bāzār'.\"}\n ]\n})\n\nN.append({\n \"id\": 6, \"lang\": \"Turkish\", \"words\": \"\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Pass-through box: Ottoman Turkish بازار (bazar, also pazar) 'market, marketplace; Sunday (market-day)', borrowed from Persian bāzār during the long Persian lexical influence on Ottoman, and the source of the Balkan forms (Bulgarian/Serbian pazar, Albanian pazar). The de-voicing b- > p- in the Turkish popular form pazar is the ordinary Turkish treatment of initial b before a voiceless-friendly stem; the learned Ottoman spelling keeps بازار. It is this Turkish stage that carried the word into Europe — which is why the AHD entry Nourai cites gives the chain Persian → Turkish → Italian → English.\",\n \"derivation_fa\": \"کادر بی‌واژه: مقصود ترکی عثمانی بازار / پازار «بازار، جای دادوستد؛ یکشنبه (روز بازار)» است که در دورهٔ درازِ اثرگذاری واژگانی فارسی بر عثمانی از فارسی «بازار» وام گرفته شده و خاستگاه صورت‌های بالکانی (بلغاری و صربی pazar، آلبانیایی pazar) است. بی‌واک‌شدن b- به p- در صورت عامیانهٔ ترکی رفتار معمول ترکی با بای آغازین است، ولی املای ادبی عثمانی همان «بازار» را نگاه می‌دارد. همین مرحلهٔ ترکی است که واژه را به اروپا رسانده؛ ازاین‌رو فرهنگ AHD که نورایی به آن ارجاع می‌دهد زنجیرهٔ فارسی ← ترکی ← ایتالیایی ← انگلیسی را می‌آورد.\",\n \"sources\": [\"https://en.wiktionary.org/wiki/bazaar\"],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\",\n    \"note\": \"Nourai cites the AHD main dictionary (not the Watkins appendix — 'bazaar' does not appear in AHD_watkins1985.txt, which only indexes IE-root words). The AHD entry's chain 'Italian bazarra, from Turkish pazar, from Persian bāzār' is reproduced independently by Wiktionary s.v. bazaar: 'From Middle French bazar or Italian bazar, from Ottoman Turkish بازار (bazar), from Persian بازار (bâzâr)'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"LKT\", \"where\": \"Lokotsch, Etym. Wb. no. 278 (LKT.txt line 817)\", \"stance\": \"supports\",\n    \"note\": \"'[Pers. bāzār] “Markt” [Horn NpEt S.38, Nr.166]. Das Wort wurde im 17. Jahrhundert durch Reisende zunächst mit Bezug auf orientalische Verhältnisse eingeführt und drang dann … in alle europäischen Sprachen ein: frz. pg. sp. bazar, it. bazar, bazzar … russ. bazar, bulg. serb. pazar … engl. bazar, bazaar.' The Balkan pazar forms show the Turkish transmission.\"},\n   {\"src\": \"Wiktionary\", \"where\": \"bazaar, English etymology\", \"stance\": \"supports\",\n    \"note\": \"Categories on the page: 'English terms derived from Ottoman Turkish', 'English terms derived from Persian'; etymology line 'from Ottoman Turkish بازار (bazar), from Persian بازار (bâzâr)'.\"}\n ]\n})\n\nN.append({\n \"id\": 7, \"lang\": \"Italian\", \"words\": \"\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Pass-through box: Italian bazzarro / bazarra / bazar 'market, bargain', taken from Turkish by Venetian and Genoese traders in the Levant in the 16th century; Etymonline routes English 'bazaar' through 'Italian bazarra', and Lokotsch lists 'it. bazar, bazzar' among the European forms, adding that because the Persian original has voiced -z-, Italian bazzarare 'to cheat, to haggle' and Sicilian bazzariotu 'swindler' belong here too. Wiktionary allows an alternative or parallel route through Middle French bazar; the Italian step is not in doubt, only its exclusivity.\",\n \"derivation_fa\": \"کادر بی‌واژه: مقصود ایتالیایی bazzarro / bazarra / bazar «بازار، معامله» است که بازرگانان ونیزی و جنووایی در سدهٔ شانزدهم از ترکی در شرق مدیترانه گرفتند. اتیمانلاین انگلیسی bazaar را از «ایتالیایی bazarra» می‌گیرد و لوکوچ نیز «it. bazar, bazzar» را در فهرست صورت‌های اروپایی می‌آورد و می‌افزاید که چون اصل فارسی زای واکدار دارد، ایتالیایی bazzarare «فریفتن، چانه زدن» و سیسیلی bazzariotu «کلاهبردار» نیز از همین‌جایند. ویکی‌واژه راه موازی از راه فرانسهٔ میانه (bazar) را هم ممکن می‌داند؛ خودِ گام ایتالیایی محل تردید نیست، تنها انحصاری‌بودنش.\",\n \"sources\": [\"https://www.etymonline.com/word/bazaar\", \"https://en.wiktionary.org/wiki/bazaar\"],\n \"ref_check\": [\n   {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"No reference is printed in this box; checked against Etymonline, Wiktionary and Lokotsch.\"}\n ],\n \"consulted\": [\n   {\"src\": \"LKT\", \"where\": \"Lokotsch no. 278 (LKT.txt line 817)\", \"stance\": \"supports\",\n    \"note\": \"'… it. bazar, bazzar … Da das Grundwort stimmhaftes s [z] hat, gehört sicherlich auch it. bazzarare “täuschen, betrügen”, siz. bazzariotu “Betrüger” hierher.'\"},\n   {\"src\": \"Etymonline\", \"where\": \"s.v. bazaar\", \"stance\": \"supports\",\n    \"note\": \"'1580s, from Italian bazarra, ultimately from Persian bazar (Pahlavi vacar) “a market”.'\"}\n ]\n})\n\nN.append({\n \"id\": 8, \"lang\": \"English\", \"words\": \"bazaar\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"English bazaar is first recorded in the 1580s of Eastern markets (travellers' reports; Lokotsch dates the European spread to 17th-century travel literature and the vogue for the Arabian Nights), spelled bazar, bazarr, bazaar; the modern sense 'fancy sale for charity' is 19th-century. Etymonline: '1580s, from Italian bazarra, ultimately from Persian bazar (Pahlavi vacar) “a market”, from Old Iranian *vaha-carana “sale, traffic”, from suffixed form of PIE root *wes- (1) “to buy, sell” + PIE *kʷoleno-, suffixed form of root *kʷel- (1) “revolve, move round; sojourn, dwell”'. Klein's entry is the terse 'bazaar, n., a market place. — Ult. fr. Pers. bāzār'. Nourai's chain Persian → Turkish → Italian → English is thus right; the only refinement modern dictionaries add is a possible Middle French bazar as the immediate donor beside Italian, and the fact that only the *second* element of the Persian compound belongs to this root.\",\n \"derivation_fa\": \"واژهٔ انگلیسی bazaar نخستین‌بار در دههٔ ۱۵۸۰ در گزارش‌های سفرنامه‌نویسان دربارهٔ بازارهای شرقی دیده می‌شود (لوکوچ گسترش اروپایی آن را به ادبیات سفر سدهٔ هفدهم و رواج «هزار و یک شب» بازمی‌گرداند)؛ معنای امروزیِ «بازارچهٔ خیریه» از سدهٔ نوزدهم است. اتیمانلاین: «۱۵۸۰ میلادی، از ایتالیایی bazarra، در نهایت از فارسی bāzār (پهلوی wāčar) “بازار”، از ایرانی باستان *wahā-čarana “دادوستد”، از ریشهٔ *wes- “خریدن و فروختن” به‌علاوهٔ *kʷoleno- از ریشهٔ *kʷel-». کلاین کوتاه می‌نویسد: «bazaar: در نهایت از فارسی bāzār». پس زنجیرهٔ فارسی ← ترکی ← ایتالیایی ← انگلیسی که نورایی کشیده درست است؛ تنها افزودهٔ فرهنگ‌های امروزی آن است که فرانسهٔ میانه (bazar) نیز ممکن است واسطهٔ بی‌واسطه باشد، و اینکه فقط جزء دومِ ترکیب فارسی به این ریشه تعلق دارد.\",\n \"sources\": [\"https://www.etymonline.com/word/bazaar\", \"https://en.wiktionary.org/wiki/bazaar\"],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\",\n    \"note\": \"The AHD dictionary entry for bazaar ('Italian bazarra, from Turkish pazar, from Persian bāzār') is the chain Nourai draws; the Watkins IE-roots appendix on disk (AHD_watkins1985.txt) contains no BAZAAR index line, confirming that Nourai's bare 'AHD' here is the main dictionary, not the appendix.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein 1966 s.v. bazaar (KLN_1966.txt line 4585)\", \"stance\": \"supports\",\n    \"note\": \"'bazaar, n., a market place. — Ult. fr. Pers. bāzār.'\"},\n   {\"src\": \"LKT\", \"where\": \"Lokotsch no. 278 (LKT.txt line 817)\", \"stance\": \"supports\",\n    \"note\": \"'… engl. bazar, bazaar, ndl. bazaar, dtsch. Bazar.'\"},\n   {\"src\": \"Etymonline\", \"where\": \"s.v. bazaar\", \"stance\": \"supports\",\n    \"note\": \"'1580s, from Italian bazarra … + PIE *kʷoleno-, suffixed form of root *kʷel- (1) “revolve, move round; sojourn, dwell.”'\"}\n ]\n})\n\nN.append({\n \"id\": 9, \"lang\": \"Sanskrit\", \"words\": \"cal\",\n \"verdict\": \"plausible\",\n \"derivation\": \"Skt. cal- (calati) 'to move, stir, tremble, be agitated' is real and Pokorny does print it in this entry — 'Old Indic carati, calatī “moves, walks, grazes, drives”' — on p.639, exactly the page Nourai cites, so the citation is faithful. But calati is not an independent PIE formation beside carati: it is the same verb with the Middle Indic l for r that is normal in Prakrit and spreads back into Classical Sanskrit (Mayrhofer, EWAia I 534 f., treats cal- under car-; Cheung's *čarH cites 'Sanskrit car “to move, walk, go, wander, travel” (RV+) ⇒ EWAia I: 534 f.', with no separate cal- root). So the node is correct as an attestation but slightly misleading as a stage: the *kʷel- material in Indo-Aryan is car-, and cal- is its later phonetic doublet — which matters for node #10, since it is with the l-form that the Persian words are compared.\",\n \"derivation_fa\": \"سنسکریت cal- (calati) «جنبیدن، حرکت کردن، لرزیدن» صورتی واقعی است و پوکورنی نیز در همان صفحهٔ ۶۳۹ که نورایی به آن ارجاع داده آن را می‌آورد: «سنسکریت carati, calati “می‌جنبد، راه می‌رود، می‌چرد”». پس ارجاع درست است. اما calati صورتی جدا و مستقل در کنار carati نیست، بلکه همان فعل است با تبدیل r به l که ویژگی زبان‌های هندی میانه (پراکریت) است و از آنجا به سنسکریت کلاسیک بازگشته؛ مایرهوفر آن را ذیل car- می‌آورد و چونگ نیز فقط car- را به‌عنوان معادل سنسکریتِ ریشهٔ *čarH ثبت می‌کند. بنابراین این خانه از نظر گواه درست است ولی به‌عنوان یک «مرحله» کمی گمراه‌کننده است: صورت هندوآریاییِ این ریشه car- است و cal- دوگانهٔ آوایی متأخر آن — و این نکته برای خانهٔ بعدی اهمیت دارد، چون واژه‌های فارسی با همین صورت لام‌دار سنجیده شده‌اند.\",\n \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/k%CA%B7el-\"],\n \"ref_check\": [\n   {\"ref\": \"POK:639\", \"status\": \"supports\",\n    \"note\": \"POK_full.txt, kʷel-1 entry, first Material paragraph (printed p.639): 'In a-grade: Old Indic carati, calatī “moves, walks, grazes, drives” etc. (heavy basis in caritum, carita-, cīrṇa-, carítra- n. “foot, leg” …), lengthened grade cāra- m. “way”.'\"}\n ],\n \"consulted\": [\n   {\"src\": \"CHEUNG\", \"where\": \"s.v. *čarH, Sanskrit line (CHEUNG.txt line ~3410)\", \"stance\": \"partial\",\n    \"note\": \"'*SANSKRIT: car “to move, walk, go, wander, travel” (RV+) ⇒ EWAia I: 534 f.' — Cheung records only car-, not cal-, as the Indo-Aryan member of this root.\"},\n   {\"src\": \"SYN\", \"where\": \"Buck §10.76 and §12.82 (SYN.txt leaves 787, 977)\", \"stance\": \"partial\",\n    \"note\": \"Buck too names only 'Skt. car- “move, wander”' / 'Skt. car- “move about”' as the Indic representative of *kʷel-.\"},\n   {\"src\": \"WLD\", \"where\": \"Walde-Pokorny I 514 f. (WLD_Bd1_pages.txt leaf 522-523)\", \"stance\": \"supports\",\n    \"note\": \"The qʷel- entry's Indic material is the carati/calati group, exactly as reprinted in Pokorny.\"}\n ]\n})\n\nN.append({\n \"id\": 10, \"lang\": \"Persian\",\n \"words\": \"čalîdan «چلیدن»; čâlâk «چالاک»; čâleš «چالش» (extra: چالیدن)\",\n \"verdict\": \"plausible\",\n \"derivation\": \"The root assignment is right and is confirmed independently: Wiktionary s.v. چالاک reads 'Related to چلیدن (čalidan, “to walk proudly, saunter”), ultimately from Proto-Indo-European *kʷel-', so čalîdan / čâlîdan 'to strut, saunter', čâlâk 'nimble, quick' (an adjective in -āk to that stem, well attested from Saʿdī onwards: 'ای که از سرو روان قد تو چالاک‌تر است') and čâleš 'struggle, quarrel' (the ‑iš verbal noun, used by Nezâmî in the line quoted in the box) all belong here. What is wrong is the arrow: Persian words do not descend from Sanskrit. Nourai's chart routinely uses the nearest attested Indo-Aryan form as a stand-in for the Indo-Iranian stage, and here the stand-in is doubly awkward because the Indic l-form (cal-) is itself a Middle Indic secondary; the Persian l is independent (Iranian *čal- beside *čar-, on which cf. Cheung's separate entry *čam ? 'to walk' citing 'NP čamīdan “to walk proudly”' — the same semantic type). Read as 'cognate with Skt. cal-, from the same PIE root' the node is sound; read as 'borrowed/descended from Sanskrit' it is not.\",\n \"derivation_fa\": \"جای‌دادن این واژه‌ها زیر این ریشه درست است و از جای دیگر هم تأیید می‌شود: ویکی‌واژه ذیل «چالاک» می‌نویسد «مرتبط با چلیدن “خرامیدن”، در نهایت از هندواروپایی آغازین *kʷel-». پس چلیدن/چالیدن «خرامیدن»، چالاک «چابک» (صفت با پسوند ‑اک از همان ستاک، از سعدی به بعد گواه دارد: «ای که از سرو روان قد تو چالاک‌تر است») و چالش «ستیز» (اسم مصدر با ‑ش، در بیت نظامی که در همان کادر آمده) همه از این ریشه‌اند. آنچه نادرست است جهت پیکان است: واژه‌های فارسی از سنسکریت نمی‌آیند. نورایی در سراسر کتاب صورت هندوآریایی را به‌جای مرحلهٔ هندوایرانی می‌نشاند و اینجا این کار دو برابر ناخوشایند است، چون خودِ صورت لام‌دارِ هندی (cal-) ثانوی و متأخر است، حال آنکه لامِ فارسی مستقل است. اگر این پیکان را «هم‌ریشه با سنسکریت cal-، از همان ریشهٔ هندواروپایی» بخوانیم درست است؛ اگر «برگرفته از سنسکریت» بخوانیم نادرست.\",\n \"sources\": [\"https://en.wiktionary.org/wiki/%DA%86%D8%A7%D9%84%D8%A7%DA%A9\"],\n \"ref_check\": [\n   {\"ref\": \"BQT:639\", \"status\": \"not_found\",\n    \"note\": \"BQT_v2_pages.txt leaf 96 (= printed 639 on the documented +543 offset) is the چشم block, and چالاک/چالش appear at leaves 72-73 (≈ printed 615-616); چلیدن was not recoverable from the vol.2 OCR at all. Either the offset is off for this stretch or the page number is wrong; Borhan vol.2 is not covered by tools/ref_page.py, so it could not be settled from the scan.\"}\n ],\n \"consulted\": [\n   {\"src\": \"Wiktionary\", \"where\": \"چالاک, Persian section\", \"stance\": \"supports\",\n    \"note\": \"'Related to چلیدن (čalidan, “to walk proudly, saunter”), ultimately from Proto-Indo-European *kʷel-.' With Saʿdī c.1260 cited for چالاک.\"},\n   {\"src\": \"CHEUNG\", \"where\": \"s.v. *čam ? 'to walk' (CHEUNG.txt line ~3283)\", \"stance\": \"partial\",\n    \"note\": \"'*NWIR: NP čamīdan “to walk proudly”, Bal. čamit/čam- “to shake, dance, prance” … This sparingly attested root does not have an IE origin and may be a blend of *čar(H) and *gam.' Cheung has no entry for *čal-; the semantically identical čamīdan he keeps apart, so the l-stem's exact status inside Iranian is not settled by him.\"},\n   {\"src\": \"POK\", \"where\": \"IEW 639 (POK_full.txt)\", \"stance\": \"supports\",\n    \"note\": \"'Old Indic carati, calatī “moves, walks, grazes, drives”' — the l-form is inside the kʷel- entry, so the root assignment matches Nourai's source.\"}\n ]\n})\n\nN.append({\n \"id\": 11, \"lang\": \"Sogdian\", \"words\": \"cxr\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Sogdian cxr (Manichaean script) /čaxr/ 'wheel', with the Buddhist/Christian by-forms cyr- and ckkr, is the direct Sogdian continuation of PIr. *čaxra- and hence a sister of Av. caxra- and NP čarx; unlike Persian it keeps the unmetathesised -xr-. Gharib's Sogdian dictionary marks its Avestan source herself, which makes Nourai's arrow from the root box (rather than from the Avestan box) a purely graphical choice. The variant ckkr, with the -kr- of the Indo-Iranian stage, is a Buddhist Sogdian re-borrowing from Sanskrit cakra- in Buddhist technical use.\",\n \"derivation_fa\": \"سغدی cxr (به خط مانوی) /čaxr/ «چرخ»، با گونه‌های cyr- و ckkr در متون بودایی و مسیحی، دنبالهٔ مستقیم ایرانی آغازین *čaxra- است و بنابراین خواهرِ اوستایی caxra- و فارسی «چرخ»؛ برخلاف فارسی، خوشهٔ ‑xr‑ در آن قلب نشده است. غریب در فرهنگ سغدی خود خاستگاه اوستایی آن را صریحاً نشان داده، پس کشیدن پیکان از کادر ریشه (به‌جای کادر اوستایی) تنها انتخابی نموداری است. گونهٔ ckkr که خوشهٔ ‑kr‑ مرحلهٔ هندوایرانی را دارد، وام‌گیری دوبارهٔ سغدی بودایی از سنسکریت cakra- در کاربرد اصطلاحی بودایی است.\",\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"SOD:131\", \"status\": \"supports\",\n    \"note\": \"Gharib, Sogdian Dictionary, printed p.131 = SOD_pages.txt leaf 196 (the leaf's own header reads '131'), entry 3313: 'cxr- M | čaxr ⓔAv. čaxra ⓔacc. -w, ob. -yy ⇒ cyr-, ckkr | wheel | GMS 266, 520, 1171, 1174.' Both the page number and the gloss are exactly as cited, and Gharib herself flags the Avestan source.\"}\n ],\n \"consulted\": [\n   {\"src\": \"SOD\", \"where\": \"Gharib, entry 3180, printed p.125 (SOD_pages.txt leaf 190)\", \"stance\": \"supports\",\n    \"note\": \"'3180 cyr- B, S | čaxr ⓔacc. -w; nom., ob. -y(h) ⇒ cxr-, ckkr | wheel, circle | TSP 2.144, 216, 924.' The by-form Gharib cross-refers to.\"},\n   {\"src\": \"HENNING\", \"where\": \"Henning, Selected Papers (HENNING_selected_papers.txt)\", \"stance\": \"silent\",\n    \"note\": \"Searched for čaxr / cxr in the Sogdian papers; nothing directly on this word came up in the OCR.\"}\n ]\n})\n\nN.append({\n \"id\": 12, \"lang\": \"Avestan\",\n \"words\": \"kar 2, karša; karaya\",\n \"verdict\": \"plausible\",\n \"derivation\": \"Two genuinely Avestan verbs, but they belong to two formations whose PIE ancestry modern work keeps partly apart. (a) YAv. karš- 'to draw (furrows), plough' (auua.karəsəṇti V 5.5, pairi.karəšōit̰ V 19.21) with the noun karša- m.n. 'furrow' is the s-extension that Pokorny prints on p.639 — 'Old Indic karṣū- f. “furrow, headland”, karṣati, kṛṣati “turn over, plough”, Avestan karša- m. n. “furrow”, karšaiti “ridge, mark with ridges”' — and Cheung confirms the same reference: '*karš/*xrah “to draw, plough” … PIE *kʷels- “to plough” ⇒ LIV 388 f. | Pok.: 639'. That half is confirmed and Nourai's POK:639 is exact. (b) Av. kar- (causative kāraiieiti, fra-kāraiieiti, pairi.kāraiiōiš) 'to spread out, sow' — Bartholomae's kar²- (AiW 449), Nourai's 'kar 2' and 'karaya' — is where the picture forks. Cheung gives it two possible PIE sources: '1. *kʷerH- “to spread, scatter (seed), sow”, *kʷorH-eie- (caus.) || 2. *kʷolH₁-eie- (caus.) “to make furrows, plough” ⇒ LIV: 353, 386 | Pok.: (933 f.) 639', and comments 'the old causative formation *kʷolH₁-eie- of IE *kelH₁- “to move, turn” … would have yielded the same result as the causative of IE *kerH- “to scatter (seed), sow” in Iranian. It is impossible to separate the two formations in most Ir. languages.' So the sowing-verb is only half a *kʷel- word. One further nicety: Bartholomae glosses kar²- 'säen' (to sow), so Nourai's labels — 'kar 2, karša: to plow' and 'karaya: to sow' — put 'plough' on kar² where 'sow' belongs.\",\n \"derivation_fa\": \"دو فعل اوستاییِ اصیل، اما متعلق به دو ساختِ گوناگون که پژوهش امروزی خاستگاه هندواروپایی‌شان را تا اندازه‌ای از هم جدا می‌کند. نخست، اوستایی نو karš- «شیار کشیدن، شخم زدن» با اسم karša- «شیار» همان گسترش با س است که پوکورنی در ص ۶۳۹ می‌آورد («سنسکریت karṣū- “شیار”، karṣati/kṛṣati “شخم زدن”، اوستایی karša- “شیار”») و چونگ نیز همان ارجاع را می‌دهد: «*karš/*xrah “کشیدن، شخم زدن” … هندواروپایی *kʷels- “شخم زدن”، پوکورنی ۶۳۹». این نیمه تأیید می‌شود و ارجاع POK:639 نورایی دقیق است. دوم، اوستایی kar- (سببیِ kāraiieiti) «پاشیدن، کاشتن» — همان kar²- بارتولمه (ستون ۴۴۹) و «kar 2 / karaya»ی نورایی — جایی است که راه دو شاخه می‌شود: چونگ دو خاستگاه ممکن می‌دهد، *kʷerH- «پاشیدن بذر، کاشتن» و سببیِ *kʷolH₁-eie- «شیار کردن»، و می‌افزاید که «در بیشتر زبان‌های ایرانی جدا کردن این دو ساخت ناممکن است». پس فعلِ «کاشتن» تنها نیمه از این ریشه است. نکتهٔ ریز دیگر آنکه بارتولمه kar²- را «säen» (کاشتن) معنی می‌کند، حال آنکه نورایی «to plow» را به آن بسته است.\",\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"POK:639\", \"status\": \"supports\",\n    \"note\": \"POK_full.txt, kʷel-1 entry, printed p.639: 's-extension in Old Indic karṣū- f. “furrow, headland”, karṣati, kṛṣati “turn over, rotate something, plow”, Avestan karša- m. n. “furrow”, karšaiti “ridge, mark with ridges”.' Cheung independently cites 'Pok.: 639' for the same root.\"},\n   {\"ref\": \"SOD:203\", \"status\": \"supports\",\n    \"note\": \"Gharib, Sogdian Dictionary, printed p.203 = SOD_pages.txt leaf 269 (leaf header '203'), entry 5105: 'kyr-² B | kēr ⓔ<Av. karaya ⇒ qs-, kst- … (to) sow | GMS 540 n1; BSTBL, Vim. 30 … AVS 104.' Gharib derives the Sogdian verb explicitly from 'Av. karaya' — Nourai's exact form and gloss.\"}\n ],\n \"consulted\": [\n   {\"src\": \"CHEUNG\", \"where\": \"s.vv. *karH² and *karš/*xrah (CHEUNG.txt lines 15984-16172)\", \"stance\": \"partial\",\n    \"note\": \"*karš/*xrah 'to draw, plough': 'YAv. karš- “to draw (furrows), plough” … *PIE *kʷels- “to plough” ⇒ LIV: 388 f. | Pok.: 639'. *karH² 'to spread out, scatter (esp. seed), sow': 'YAv. kar- (caus.) “to spread out” … YAv. kāraiieiti … *PIE 1. *kʷerH- … || 2. *kʷolH₁-eie- (caus.) … ⇒ LIV: 353, 386 | Pok.: (933 f.) 639 … It is impossible to separate the two formations in most Ir. languages.'\"},\n   {\"src\": \"BRT\", \"where\": \"Bartholomae, AiW col. 449 s.v. 2. kar- (cited by Cheung: 'root kar²- in AiW: 449')\", \"stance\": \"partial\",\n    \"note\": \"Bartholomae's kar²- is glossed 'säen' (to sow), with the causative kāraiia-; the Avestan verb 'to plough' is his karš-. Nourai's gloss pairing is slightly shuffled relative to AiW.\"},\n   {\"src\": \"KNT\", \"where\": \"Kent, Old Persian, Lexicon (KNT.txt)\", \"stance\": \"silent\",\n    \"note\": \"Kent's only kar- is 'kar- “make, do”, OP pres. kunautiy' — a different root; no Old Persian witness for the ploughing/sowing verb.\"}\n ]\n})\n\nN.append({\n \"id\": 13, \"lang\": \"Pahlavi\", \"words\": \"kištan\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"MP kištan is MacKenzie's headword 'kištan, kar- [ZLYTWN-tn’ < A √zr‘; kyštn’, k’l- | M kyšt, kiš-, N ~] till, furrow; sow', with the derivatives kištār 'tillage', kišw(ān)zār 'field'. The paradigm is suppletive and preserves both Avestan verbs of node #12: the present stem kār- continues Av. kar- (caus. kāraiia-), the past stem kišt continues the participle *kr̥šta- of Av. karš- 'to plough'. Cheung sets this out explicitly — under *karH²: 'MMP q’r-, BMP KL /kār-/ “to make furrows; sow” … Partic.: perf. pass. MMP kyst'; under *karš/*xrah: 'kyst (pret. stem) “to sow, plant” (supplet. stem of k’r-, *karH²)'. So Nourai's single Pahlavi box with the gloss 'to plow, sow, plant' is exactly right, and it is the point at which the two Avestan stems of the box above merge into one verb.\",\n \"derivation_fa\": \"«کِشتن» سرواژهٔ خودِ مکنزی است: «kištan, kār- … شخم زدن، شیار کردن؛ کاشتن»، با مشتقاتی چون kištār «کشتزار» و kišwānzār «کشتزار». صرف این فعل مکمل (suppletive) است و هر دو فعل اوستاییِ خانهٔ پیشین را در خود نگاه داشته: ستاک حالِ kār- دنبالهٔ اوستایی kar- (سببی kāraiia-) است و ستاک گذشتهٔ kišt دنبالهٔ صفت مفعولی *kr̥šta- از اوستایی karš- «شخم زدن». چونگ همین را صریح می‌گوید: ذیل *karH² «فارسی میانه kār- “شیار کردن؛ کاشتن” … صفت مفعولی kyst» و ذیل *karš «kyst ستاک گذشته، مکمّلِ k’r-». پس یک کادرِ پهلوی با معنای «شخم زدن، کاشتن، نشاندن» درست است و همان جایی است که دو ستاک اوستایی در یک فعل به هم می‌رسند.\",\n \"sources\": [\"https://en.wiktionary.org/wiki/%DA%A9%D8%A7%D8%B4%D8%AA%D9%86\"],\n \"ref_check\": [\n   {\"ref\": \"SNS:220\", \"status\": \"supports\",\n    \"note\": \"Tavoosi, Glossary of Šāyast nē Šāyast: the alphabetical index (SNS_pages.txt line 16057) has the line 'kistan 220/6', i.e. entry/page 220 item 6 — exactly the number Nourai cites; the glossary entry itself (SNS_pages.txt line 8823) gives 'kištan: … kist … [Av.] karīta / kr̥ṣtay (AiW 458) … Sanskrit kr̥ṣ-', linking the Pahlavi verb to the Avestan karš- family as the chart does. (The Persian OCR of the entry is poor; the index line is unambiguous.)\"}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"MacKenzie, CPD p.51 (PHD.txt line 428) and p.50 (line 424)\", \"stance\": \"supports\",\n    \"note\": \"'kištan, kār- [ZLYTWN-tn’ < A √zr‘; kyštn’, k’l- | M kyšt, kiš-, N ~] till, furrow; sow. kištār: tillage. kišw, ~ān: tillage. ~(an)zār: field.' and, under k, the cross-reference '³kār … kār-, v. kištan'.\"},\n   {\"src\": \"CHEUNG\", \"where\": \"s.vv. *karH² and *karš/*xrah (CHEUNG.txt lines 16003, 16100)\", \"stance\": \"supports\",\n    \"note\": \"'*MIDDLE PERSIAN: MMP q’r-, BMP KL /kār-/ “to make furrows; sow” … Partic.: perf. pass. MMP kyst'; '*MIDDLE PERSIAN: MMP krs-, qrs- “to pull, draw” || kyst (pret. stem) “to sow, plant” (supplet. stem of k’r-, *karH²)'.\"},\n   {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II (NYB_vol2_glossary.txt), searched kištan / kāštan / kār-\", \"stance\": \"silent\",\n    \"note\": \"No usable entry recovered from the OCR.\"}\n ]\n})\n\nN.append({\n \"id\": 14, \"lang\": \"Persian\",\n \"words\": \"kâštan «کاشتن»; kârîdan 1 «کاریدن ۱» (extras: کِشتن ، کِشت ، کشاورز ، کار ۳)\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"NP kâštan / kištan 'to sow, plant' (pres. stem kâr-) is MP kištan/kār- with no change beyond the vowel: Wiktionary, 'From Middle Persian kištan — the vowel changed in New Persian under the influence of the present stem kār- — from Proto-Iranian *karH-'. That is why the doublet کاشتن (from the present stem's ā) stands beside کِشتن (the inherited past stem kišt), and why the noun کِشت 'sowing, crop' and کشاورز 'farmer' (kišt + āwarz 'practising') attach to the i-form while کاریدن ۱ and کار ۳ 'sowing' attach to the ā-form. Horn no. 836 (p.185) gives the same paradigm and the Avestan source: 'kāštan (Šāhn.), kištan “säen”, Praes. kār-em, kišt; g. kaštmūn; aw. √karš-, ya(t)karšti, vergl. karšəsca frakāra(y)ōiš' — note that Horn's Avestan quotation contains both stems (karš- and frakāraiiōiš), i.e. exactly Nourai's node #12. Mo'in's footnote in Borhan-e Qate' p.1567 says it once more, and adds the Persian noun: 'از kāštan (کاشتن) [زمان حال: کارد]، اوستا *karš-؛ در مقابل آن کِشتن … سانسکریت kr̥ṣáti … شاید اوستایی *kāra- ← فارسی «کار»'.\",\n \"derivation_fa\": \"«کاشتن»/«کِشتن» (ستاک حال: کار-) همان kištan/kār- فارسی میانه است و تنها واکه دگرگون شده: ویکی‌واژه می‌نویسد «از فارسی میانه kištan — واکه در فارسی نو زیر تأثیر ستاک حال kār- تغییر کرده — از ایرانی آغازین *karH-». به همین سبب دوگانهٔ «کاشتن» (با الفِ ستاک حال) در کنار «کِشتن» (ستاک گذشتهٔ ارثی kišt) ایستاده است، و اسم «کِشت» و «کشاورز» (کِشت + آورز) به صورت کسره‌دار می‌چسبند و «کاریدن ۱» و «کار ۳» به صورت الف‌دار. هرن در شمارهٔ ۸۳۶ (ص ۱۸۵) همین صرف و همین خاستگاه اوستایی را می‌دهد: «kāštan (شاهنامه)، kištan “کاشتن”، حال kār-em، kišt؛ اوستایی √karš-، قس karšəsca frakāra(y)ōiš» — و توجه کنید که همین شاهدِ اوستاییِ هرن هر دو ستاکِ خانهٔ ۱۲ را در خود دارد. حاشیهٔ معین در برهان قاطع ص ۱۵۶۷ نیز همین را می‌گوید و اسم فارسی «کار» را هم می‌افزاید. ادعای نورایی درست است.\",\n \"sources\": [\"https://en.wiktionary.org/wiki/%DA%A9%D8%A7%D8%B4%D8%AA%D9%86\"],\n \"ref_check\": [\n   {\"ref\": \"BQT:1567\", \"status\": \"supports\",\n    \"note\": \"Rendered with tools/ref_page.py BQT:1567 (BQT_v3 pdf p.360, running head '۱۵۶۷ کاشمر'), footnote 3 to the article کاشتن: 'از kāštan (کاشتن) [زمان حال: کارد]، اوستا *karš- (کارد)؛ در مقابل آن کِشتن (بکسر اول) (بمعنی کاشتن)، سانسکریت kr̥ṣáti …، افغانی [kṛəl] (شخم کردن، کاشتن) به ریشهٔ اول متعلق است … شاید اوستایی *kāra- ← فارسی «کار» … هوبشمان ۸۳۹.' Exactly the chart's node.\"},\n   {\"ref\": \"HRN:185\", \"status\": \"supports\",\n    \"note\": \"Horn, Grundriss p.185 (HRN.txt leaf 206, printed = leaf − 21), no. 836: 'kāštan (Šāhn. III, 1544 Vers 842), kištan “säen”, Praes. kār-em, kišt. g. kaštmūn. aw. √karš-, ya(t)karšti, vergl. karšəsca frakāra(y)ōiš.'\"}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"MacKenzie, CPD p.51 (PHD.txt line 428)\", \"stance\": \"supports\",\n    \"note\": \"'kištan, kār- [… | M kyšt, kiš-, N ~] till, furrow; sow' — the 'N ~' marks the New Persian outcome as identical.\"},\n   {\"src\": \"CHEUNG\", \"where\": \"s.v. *karH², NWIR section (CHEUNG.txt line ~16030)\", \"stance\": \"supports\",\n    \"note\": \"'*NWIR: Widely attested: NP kištan/kār- “to plant, sow”, Kurd. (Sor.) kēštan/kēšt-, Awrom. kelāy/kel- “to plough”, Zaz. kāritiš/kāren- … Pash. karal “to till, cultivate”.'\"},\n   {\"src\": \"ARY\", \"where\": \"Aryanpur, Farhang-e rishe-hā, pdf p.388-389 (ARY_pages.txt leaf 387)\", \"stance\": \"supports\",\n    \"note\": \"The کاشتن article lays out Avestan / Old Persian / Pahlavi / Kurdish / Baluchi / Sanskrit / Greek / Latin / Old Church Slavonic / Lithuanian / Old Prussian / Welsh / Breton / Armenian columns with a Borhan-e Qate' cross-reference, i.e. an independent modern Persian handbook putting کاشتن in the same IE family.\"},\n   {\"src\": \"Wiktionary\", \"where\": \"کاشتن\", \"stance\": \"supports\",\n    \"note\": \"'From Middle Persian kištan — the vowel changed in New Persian under the influence of the present stem kār- — from Proto-Iranian *karH- … Compare Ossetian калын (kalyn, “to pour”), Central Kurdish کێڵان (kêllan, “to plough”), Pashto کرل (karəl, “to sow”), Sanskrit किरति (kirati, “he scatters”), Latin colere (“to cultivate”).' The comparison with Latin colere puts it under *kʷel-.\"}\n ]\n})\n\njson.dump(e2, open(os.path.join(D,'e2.json'),'w',encoding='utf-8'), ensure_ascii=False, indent=1)\nprint(\"entry2 nodes:\", len(e2[\"nodes\"]), [n[\"id\"] for n in e2[\"nodes\"]])\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build290b.py",
 "description": "Build entry 2 of page 290"
}
```


### [2026-09-06T22:33:03.760Z] TOOL RESULT

```
entry2 nodes: 14 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
```


## [2026-09-06T22:33:11.572Z] TOOL CALL #104: Bash

```json
{
 "command": "python3 - <<'EOF'\nimport json, os\nD='/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p290'\ne1=json.load(open(os.path.join(D,'e1.json'),encoding='utf-8'))\ne2=json.load(open(os.path.join(D,'e2.json'),encoding='utf-8'))\nout={\"pdf_page\":290,\"book_page\":260,\"verified_by\":\"claude-opus-5\",\"verified_on\":\"2026-09-06\",\"entries\":[e1,e2]}\np='data/verification/page-290.json'\njson.dump(out,open(p,'w',encoding='utf-8'),ensure_ascii=False,indent=1)\nprint('wrote',p)\nEOF\npython3 -m json.tool data/verification/page-290.json > /dev/null && echo \"JSON OK\"\npython3 tools/verify_check.py 290",
 "description": "Assemble and run verify_check"
}
```


### [2026-09-06T22:33:14.015Z] TOOL RESULT

```
wrote data/verification/page-290.json
JSON OK
nodes verified: 18/18
node verdicts: {'disputed': 1, 'confirmed': 9, 'plausible': 8}
root verdicts: {'confirmed': 2}
ref checks: {'supports': 23, 'partial': 3, 'not_checked': 4, 'not_found': 3}
books consulted: {'partial': 11, 'contradicts': 5, 'supports': 38, 'silent': 4} | by book: {'CHEUNG': 10, 'PHD': 7, 'Wiktionary': 6, 'BRT': 5, 'HUB': 3, 'POK': 3, 'ARY': 3, 'LKT': 3, 'WLD': 2, 'NYB': 2, 'BQT': 2, 'KNT': 2, 'HRN': 2, 'Etymonline': 2, 'ISS_alt_DKS': 1, 'IEC': 1, 'KLN': 1, 'SYN': 1, 'SOD': 1, 'HENNING': 1}
```


## [2026-09-06T22:33:25.289Z] TOOL CALL #105: Bash

```json
{
 "command": "mkdir -p data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg290.png data/verification/sources/refs/ocr/BOOK/290.png && python3 - <<'EOF'\nimport json\nidx={}\nfor line in open('data/verification/sources/web/index.jsonl',encoding='utf-8'):\n    try: r=json.loads(line)\n    except: continue\n    idx[r['url']]=r.get('status')\nd=json.load(open('data/verification/page-290.json',encoding='utf-8'))\nurls=set()\ndef walk(o):\n    if isinstance(o,dict):\n        for k,v in o.items():\n            if k=='sources':\n                urls.update(v)\n            else: walk(v)\n    elif isinstance(o,list):\n        for x in o: walk(x)\nwalk(d)\nbad=[u for u in urls if idx.get(u) not in (200,)]\nprint('cited urls:',len(urls))\nfor u in sorted(urls): print(' ',idx.get(u),u)\nprint('NOT ARCHIVED/OK:',bad)\nEOF",
 "description": "Verify cited URLs are archived"
}
```


### [2026-09-06T22:33:27.433Z] TOOL RESULT

```
cited urls: 16
  200 https://en.wiktionary.org/wiki/%D8%A2%DA%AF%D8%A7%D9%87
  200 https://en.wiktionary.org/wiki/%D8%A8%D8%A7%D8%B2%D8%A7%D8%B1
  200 https://en.wiktionary.org/wiki/%D9%86%DA%AF%D8%A7%D9%87
  200 https://en.wiktionary.org/wiki/%DA%86%D8%A7%D8%B4%D8%AA
  200 https://en.wiktionary.org/wiki/%DA%86%D8%A7%D9%84%D8%A7%DA%A9
  200 https://en.wiktionary.org/wiki/%DA%86%D8%B1%D8%AE
  200 https://en.wiktionary.org/wiki/%DA%86%D8%B1%DB%8C%D8%AF%D9%86
  200 https://en.wiktionary.org/wiki/%DA%86%D8%B4%D9%85
  200 https://en.wiktionary.org/wiki/%DA%86%D8%B4%DB%8C%D8%AF%D9%86
  200 https://en.wiktionary.org/wiki/%DA%A9%D8%A7%D8%B4%D8%AA%D9%86
  200 https://en.wiktionary.org/wiki/%DA%AF%D8%B2%D8%A7%D8%B1%D8%AF%D9%86
  200 https://en.wiktionary.org/wiki/%DA%AF%D9%88%D8%A7%D9%87
  200 https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/k%CA%B7e%E1%B8%B1-
  200 https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/k%CA%B7el-
  200 https://en.wiktionary.org/wiki/bazaar
  200 https://www.etymonline.com/word/bazaar
NOT ARCHIVED/OK: []
```


## [2026-09-06T22:33:50.565Z] AGENT

Done. `data/verification/page-290.json` is written and `verify_check.py 290` reports 18/18 nodes with **0 PROBLEM lines**.

**Page 290 (book p. 260) — 2 non-redirect entries, 18 nodes**
- Root verdicts: confirmed 2 (Kwek/Qwek = Pok. 638 *kʷeḱ-; Kwel/Qwel = Pok. 639-640 *kʷel-; both names/glosses copied verbatim from Watkins + Walde-Pokorny's `qʷ-` spelling).
- Node verdicts: confirmed 9, plausible 8, disputed 1, transcription_suspect 0.
- Ref checks: supports 23, partial 3, not_found 3, not_checked 4. Books consulted: 58 entries across 20 books.

**disputed**
- Kwek #1 (Avestan) — `vi-či`: Av. vī-ci- 'to distinguish' belongs to *kʷei- (WP I 509 f., Pok. 636 f. — the root Nourai himself files as "Kuei", the redirect at the head of this very page), not to *kʷeḱ-. The other six forms in the box (kas, čaš, čašman, ā-kasat, ni-kasa, vi-kās/vi-kaya) are confirmed by Pokorny, Klein p.42, Bartholomae col. 461-2 and Buck §21.28.

**Main "plausible" reasons (detail in the file)**
- Kwek #3/#4 (čāšišn/čašīdan/čāšt): Bailey (ISS) and ESIJa do link the 'taste' words to *kʷeḱ-, but Cheung 2007 sets up a separate *čaš² "PIE —" and rejects it; MacKenzie glosses čāšišn 'teaching', čaxšišn 'taste'.
- Kwel #1: "Old Persian" label unsupported — Kent has no caxra-; Avestan half confirmed.
- Kwel #4/#5: bāzār's second element is from this root, but the first is OIr. *wahā- 'sale' (PIE *wes-), not the preverb abā- (Horn no.166 already ruled that out); gloss "place of assembly" is folk analysis. The suffix ‑زار could not be verified anywhere.
- Kwel #9/#10: Skt. cal- is a Middle-Indic doublet of car-, and the Persian čalīdan/čālāk group is cognate with it, not descended from Sanskrit (Wiktionary: čālāk … "ultimately from PIE *kʷel-").
- Kwel #12: Av. karš- is *kʷels- (Pok. 639, confirmed), but kar²/karaya may be *kʷerH- rather than *kʷolh₁-eie- (Cheung: "impossible to separate the two formations").

**Extraction errors for the owner: none.** One book-internal inconsistency: in Kwel #5 the printed page gives `zâr 2` in Latin but `ـزار ۳` in Persian script — verified against a 600-dpi render; the JSON reproduces the page faithfully.

Not resolvable: BQT:635, BQT:614 and BQT:639 (vol. 2) — the cited pages don't contain the headwords on the documented leaf offset, and Borhan vol. 2 has no scan wired into `ref_page.py`. BQT:52/1849/2163/1567 all check out exactly.
