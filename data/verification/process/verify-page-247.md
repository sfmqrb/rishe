# Verification process log — verify-page-247


## [2026-09-06T15:53:28.838Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 247 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-247.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-247.json. Write /home/sfmqrb/git/rishe/data/verification/page-247.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 247` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-06T15:53:30.528Z] AGENT

I'll start by reading the instructions.


## [2026-09-06T15:53:31.200Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-06T15:53:31.217Z] TOOL RESULT

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


## [2026-09-06T15:53:31.494Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-247.txt"
}
```


### [2026-09-06T15:53:31.516Z] TOOL RESULT

```
1	=== PDF page 247 (book page 217) ===
2	--- entry 0 ---
3	ROOT Ke-e-tero -> redirect to I2
4	--- entry 1 ---
5	ROOT [Indo-European] Keg, Keng, Kek, Kenk 2, Kag : hook  (refs POK:537; IEC:458)
6	#1 (parent #0) [Avestan] refs=POK:537 | cang : hook
7	  #2 (parent #1) [Persian] refs=POK:537; BQT:665 | čang «چنگ» : hook, paw, harp | extra: چنگال ، چنگک
8	    #3 (parent #2) [Arabic] refs=PLA:188 | sanj : harp, cymbal
9	      #4 (parent #3) [Persian] refs=MON:2165 | sanj, senj «صنج» : cymbal | NOTE: See root "Gěu 1" for another possible derivation.
10	#5 (parent #0) [Persian] refs=IEC:458; MON:2910 | kaj «کج» : bent, crooked, tilted, wrong | extra: کژ ، کژدم
11	#6 (parent #0) [Germanic] refs=AHD | hôka : hook ; hakkijan : to hack
12	  #7 (parent #6) [English] refs=None | hook, hack
13	--- entry 2 ---
14	ROOT [Indo-European] Kei 1, Kiě 1 : gray or black color, dark  (refs POK:540)
15	#1 (parent #0) [Avestan] refs=POK:541; BRT:1631 | syâva : black ; syâva-aršan : (with) "black male" animals ☞Eres 1 ; syâ-maka : owner of "black hair"
16	  #2 (parent #1) [Persian] refs=HRN:168; BQT:1199; SNS:172 | sîyâh «سیاه» : black ; Sîyâvaš, Sîyâmak «سیاوش ، سیامک» : male names ; sîyâhgŭš «سیاه‌گوش» : the caracal ☞Ôus 1 | NOTE: Compare "sîyâ-gŭš" with Turkish "kara-kŭlâk: black ear" which is the root of English "caracal". See Root "Kar 2".
17	    #3 (parent #2) [Hindustani] refs=None | 
18	      #4 (parent #3) [English] refs=KLN:1554 | syagush : the caracal
19	#5 (parent #0) [Avestan] refs=POK:541; KLN:288 | sâma : black
20	  #6 (parent #5) [Persian] refs=BQT:1075 | sâm «سام» : "black", a male name
21	#7 (parent #0) [Avestan] refs=POK:541 | saěna : gray, gray bird (falcon) ; saěna-mereğa : dark bird ☞Mereğa
22	  #8 (parent #7) [Persian] refs=BQT:1237; HRN:169 | šâhîn «شاهین» : falcon ; sîmorğ «سیمرغ» : a legendary bird
23	#9 (parent #0) [Sogdian] refs=SOD:370 | š`w : black
24	#10 (parent #0) [Germanic] refs=AHD | hiwan : color, hue
25	  #11 (parent #10) [English] refs=None | hue
26	#12 (parent #0) [Latin] refs=POK:541 | cimex : black bug
27	  #13 (parent #12) [English] refs=None | cimex, chinch
28	
```


## [2026-09-06T15:53:35.232Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-247.json",
 "description": "Read source JSON for page 247"
}
```


### [2026-09-06T15:53:35.273Z] TOOL RESULT

```
{
  "pdf_page": 247,
  "book_page": 217,
  "entries": [
    {
      "root": {
        "name": "Ke-e-tero",
        "redirect": "I2"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Keg, Keng, Kek, Kenk 2, Kag",
        "lang": "Indo-European",
        "refs": "POK:537; IEC:458",
        "gloss": "hook"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:537",
          "words": [
            {"translit": "cang", "gloss": "hook", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "POK:537; BQT:665",
          "words": [
            {"translit": "čang", "gloss": "hook, paw, harp", "script": "چنگ"}
          ],
          "script_extra": "چنگال ، چنگک",
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Arabic",
          "refs": "PLA:188",
          "words": [
            {"translit": "sanj", "gloss": "harp, cymbal", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Persian",
          "refs": "MON:2165",
          "words": [
            {"translit": "sanj, senj", "gloss": "cymbal", "script": "صنج"}
          ],
          "script_extra": null,
          "note": "See root \"Gěu 1\" for another possible derivation.",
          "quote": null
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Persian",
          "refs": "IEC:458; MON:2910",
          "words": [
            {"translit": "kaj", "gloss": "bent, crooked, tilted, wrong", "script": "کج"}
          ],
          "script_extra": "کژ ، کژدم",
          "note": null,
          "quote": {
            "text": "وز خم ابروی توام هیچ گشایشی نشد - وه که در این خیال کج عمر عزیز شد تلف",
            "poet": "Hâfez"
          }
        },
        {
          "id": 6,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "hôka", "gloss": "hook", "script": null},
            {"translit": "hakkijan", "gloss": "to hack", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "hook, hack", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Kei 1, Kiě 1",
        "lang": "Indo-European",
        "refs": "POK:540",
        "gloss": "gray or black color, dark"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:541; BRT:1631",
          "words": [
            {"translit": "syâva", "gloss": "black", "script": null},
            {"translit": "syâva-aršan", "gloss": "(with) \"black male\" animals", "script": null, "see": ["Eres 1"]},
            {"translit": "syâ-maka", "gloss": "owner of \"black hair\"", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "HRN:168; BQT:1199; SNS:172",
          "words": [
            {"translit": "sîyâh", "gloss": "black", "script": "سیاه"},
            {"translit": "Sîyâvaš, Sîyâmak", "gloss": "male names", "script": "سیاوش ، سیامک"},
            {"translit": "sîyâhgŭš", "gloss": "the caracal", "script": "سیاه‌گوش", "see": ["Ôus 1"]}
          ],
          "script_extra": null,
          "note": "Compare \"sîyâ-gŭš\" with Turkish \"kara-kŭlâk: black ear\" which is the root of English \"caracal\". See Root \"Kar 2\".",
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Hindustani",
          "refs": null,
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "English",
          "refs": "KLN:1554",
          "words": [
            {"translit": "syagush", "gloss": "the caracal", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:541; KLN:288",
          "words": [
            {"translit": "sâma", "gloss": "black", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "Persian",
          "refs": "BQT:1075",
          "words": [
            {"translit": "sâm", "gloss": "\"black\", a male name", "script": "سام"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:541",
          "words": [
            {"translit": "saěna", "gloss": "gray, gray bird (falcon)", "script": null},
            {"translit": "saěna-mereğa", "gloss": "dark bird", "script": null, "see": ["Mereğa"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 7,
          "lang": "Persian",
          "refs": "BQT:1237; HRN:169",
          "words": [
            {"translit": "šâhîn", "gloss": "falcon", "script": "شاهین"},
            {"translit": "sîmorğ", "gloss": "a legendary bird", "script": "سیمرغ"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 0,
          "lang": "Sogdian",
          "refs": "SOD:370",
          "words": [
            {"translit": "š`w", "gloss": "black", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "hiwan", "gloss": "color, hue", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 10,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "hue", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 0,
          "lang": "Latin",
          "refs": "POK:541",
          "words": [
            {"translit": "cimex", "gloss": "black bug", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 13,
          "parent": 12,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "cimex, chinch", "gloss": null, "script": null}
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


## [2026-09-06T15:53:36.039Z] TOOL CALL #4: Bash

```json
{
 "command": "ls data/verification/ | head -50 && echo ---- && cat tools/verify_check.py | head -80",
 "description": "List verification dir and check script"
}
```


### [2026-09-06T15:53:36.094Z] TOOL RESULT

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


## [2026-09-06T15:53:40.523Z] TOOL CALL #5: Bash

```json
{
 "command": "sed -n '80,200p' tools/verify_check.py",
 "description": "Rest of verify_check"
}
```


### [2026-09-06T15:53:40.561Z] TOOL RESULT

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


## [2026-09-06T15:53:41.409Z] TOOL CALL #6: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/page-202.json'))\nprint(json.dumps(d['entries'][0],ensure_ascii=False,indent=1)[:4000])\n\"",
 "description": "Sample existing verification file"
}
```


### [2026-09-06T15:53:43.235Z] TOOL RESULT

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
   "where": "Bd. I 675-677 (WLD_Bd1 djvu line 42665 ff., running head 'gʷem-, gʷā-')",
   "stance": "supports",
   "note": "'gʷem-, gʷā-' … 'ai. gātram „Glied, Körper“; ai. gātu- „Gang, Weg, Raum, Ort“, av. gātu-s „Ort, Platz; Liegerstatt, Sessel, Thron“, ap. gāθu … ai. vi-gāman- n. „Schritt“ … av. gāman- n. „Schritt“'. This is the source Pokorny 463 abridges (Buck cites it as 'Walde-P. 1.675 ff.')."
  },
  {
   "src": "AHD",
   "where": "Watkins 1985, g-list (AHD_watkins1985.txt line ~539)",
   "stance": "supports",
   "note": "'gʷā-. Also gʷem-. To go, come. 1. Germanic *kuman in a. Old English cuman, to come: COME … 3. Suffixed zero-grade form *gʷm̥-yo- in Greek bainein, to go, walk, step, with basis (< *gʷm̥-ti-), a stepping, tread, base'. Same double root, same gloss."
  },
  {
   "src": "CHEUNG",
   "where": "s.v. *gam¹ (CHEUNG.txt lines 7307, 7478) and *gaH¹ (line 7054)",
   "stance": "supports",
   "note": "'*gam¹ \"to come\" … «PIE *gʷem- “to go; come” = LIV: 209 f. | Pok.: 464 f.»'; and '«PIE *gʷeH₂- “to go, stride” = LIV: 205 | Pok.: 463 f.»'. Cheung's *ga
```


## [2026-09-06T15:53:46.519Z] TOOL CALL #7: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-06T15:53:46.551Z] TOOL RESULT

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


## [2026-09-06T15:53:48.378Z] TOOL CALL #8: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','IEC','BQT','MON','PLA','AHD','BRT','HRN','SNS','KLN','SOD','WLD','PHD','NYB','HUB','CHEUNG','ARY','SYN']:\n    print(k, json.dumps(d.get(k),ensure_ascii=False))\n\"",
 "description": "Refs online info"
}
```


### [2026-09-06T15:53:50.244Z] TOOL RESULT

```
<persisted-output>
Output too large (32.8KB). Full output saved to: /home/sfmqrb/.claude/projects/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/tool-results/b8053i854.txt

Preview (first 2KB):
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-dictionary/ (entry pages with page numbers) and StarLing https://starlingdb.org/cgi-bin/query.cgi?basename=\\data\\ie\\pokorny&root=config", "notes": "Nourai's page numbers are Band I 1959 pages, which match these scans. Band II (1969 index) is at pokorny-indogermanisches-etymologisches-worterbuch-band-ii-1969 (djvu 200). local_files: /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt (pp. 1-348), /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_02.txt (pp. 349-770), /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_03.txt (pp. 771-1183); /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_full.txt (unpaginated database text with 'Page(s): N' per root)", "local_files": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_0
...
</persisted-output>
```


## [2026-09-06T15:53:54.379Z] TOOL CALL #9: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'))\nfor k in ['IEC','BQT','MON','PLA','BRT','HRN','SNS','KLN','SOD','AHD']:\n    e=d.get(k,{})\n    print('==',k, e.get('title'))\n    print(' offset:', e.get('page_offset'))\n    print(' hint:', str(e.get('lookup_hint'))[:600])\n    print(' local:', e.get('local_file'), e.get('local_files'))\n\"",
 "description": "Extract ref lookup hints"
}
```


### [2026-09-06T15:53:56.048Z] TOOL RESULT

```
== IEC S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87
 offset: TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
 hint: Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root.
 local: /home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt None
== BQT Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)
 offset: vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...').
 hint: grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=deh
 local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages_faseng.txt'] None
== MON Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)
 offset: None
 hint: Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different pagination from the 6-vol edition; OCR downloaded a
 local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt'] None
== PLA A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988
 offset: 301 leaves (pdftotext -layout, \f-separated): printed page = leaf(1-based) − 15 (leaf 291 = p.276).
 hint: HathiTrust search-only; Google Books id q_ErAAAAMAAJ snippet view; DDB has only the table of contents. No full text online. | For pages in a scanned volume use: python3 tools/ref_page.py PLA:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)
 local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt'] None
== BRT C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)
 offset: Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
 hint: Nourai's BRT numbers are Bartholomae's COLUMN numbers. Headwords are Avestan/OP in transliteration in bold at line start; OCR of the special transliteration is noisy - grep on a distinctive Latin gloss or the German meaning in quotes. Column numbers appear as standalone numbers at leaf tops.
 local: /home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt None
== HRN P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893
 offset: leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
 hint: Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.
 local: /home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt None
== SNS Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1986
 offset: 242 leaves; page offset not determined (OCR too poor to read printed numbers) — locate by transliteration then read the page image
 hint: grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php search (see BQT) for better hit-to-leaf mapping.
 local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS.txt'] None
== KLN E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67
 offset: KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
 hint: Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.
 local: /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt ['/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1971.txt']
== SOD Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995
 offset: printed page ≈ leaf − 66 in SOD_pages.txt (0-based \f blocks; 645 leaves; English intro precedes)
 hint: Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/Sog
 local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD.txt'] None
== AHD W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)
 offset: 1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page.
 hint: Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru-' ; entries list English derivatives in caps. Restricted 1970s AHD scans on IA (lending only, djvu.txt returns 401): americanheritage0000dict (July 1977 printing, 970 leaves - probably the New College Edition), bwb_P9-BHZ-437 (1974), americanheritage00nyde (1970), bwb_W9-CSW-086 (1969, 1610 leaves 
 local: /home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt None
```


## [2026-09-06T15:54:04.931Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR>=190 && NR<=200 {print \"=== leaf \" NR-1 \" ===\"; print}' POK_02.txt | head -300",
 "description": "Pokorny leaves around p.537"
}
```


### [2026-09-06T15:54:06.534Z] TOOL RESULT

```
=== leaf 189 ===
lit.   kafdas    ,Echo'.,    alit.  ap-kerdziu   ,ich  verkünde',   apr.  kirdlt   ,hören'.
WP.  I  353  f.
•2.  kar-,  redupl.  karkar-  u.  dgl.  ,hart'.
Ai.  karkara-  ,rauh,  hart*  =  gr.  naQ-^agoL'  TQa%elg  Hes.,  ai.  karkasa- ,rauh,  hart*  (auch  karaka-  m.,  ,Hage*l?)  ;vermutlich  gr.  Y.qava\/]6Q  ,hart, rauh,  felsig*.
Dazu  wohl  die  Wörter  für  ,Krebs' :  ai.  karkata-  m.  , Krebs*  {karkin- jKrebs  als  Sternbild*,  Lw.  aus  gr.  xor^xiVog),  karka-h  m.  , Krabbe* ;
gr.  y,aQ/,ivog  ds.,  lat.  cancer,  -crl  ds.  (dissim.  aus  *carcro-,  vielleicht schon  idg.,  vgl.  ai.  kajdkata-  m.  , Panzer*  aus  ^kavkj-ta-) ;
daß  aksl.  rak^  , Krebs*  aus  *krak^  dissim.  sei,  ist  möglich;  die  Ähnlich- keit mit  norw.  (usw.)  rceke  , Cancer  squilla,  Garnele'  setzt  Entlehnung des  norw.  Wortes  voraus  ;
ferner  Worte  für  harte  Schale,  Nuß :  gr,  -Adqvov  .Nuß',  Y.(xQva  f.  ,Nuß- baum' ;  lat.  carlna  f.  ,Nußschale,  Schiffskiel,  Schiff'  (vielleicht  aus  dem Gr.  nach  Keller  Volkset.  279,  in  welchem  Falle  xagvLvog  die  Quelle  ist); ,cymr.  ceri  (*carlso-)  , Obstkern*.
Mit  ^Suffixen:  got.  hardus  ,hart,  streng*,  anord.  hardr  ,hart*,  ags.  heard ,hart,  stark,  tapfer*,  as.  hard,  ahd.  hart,  herti  ,hart,  fest,  schwer*,  Adv. anord.  harda,  ags.  hearde,  ahd.  harto,  mnd.  harde  ,sehr,  besonders*  (vgl. gr.  xa^T«),  urgerm.  *hardü-  aus  idg.  *kar-tü-]  auf  Grund  einer  idg.  Er- weiterung *kre-t-,  *kj't-  äol.  (Gramm.)  ^igezog,  woneben  mit  dem  Vokalismus des  Adj.  att.  ytQccTog,  ep.  ion.  y^dgrog  , Stärke,  Kraft*,  hom.  yigarvg  ,stark' Komparat.  ion.  -ageaacjv,  att.  TtgslTTcov,  Superl.  ngdTiGTog,  ep.  -/.dgriaxog, Adv.  Y.dgTa  , stark',  y.ga%£gög,  Yxxgxsgog  , stark,  kräftig,  fest,  heftig'  (usw.); fern  bleibt  ai.  krdtu-,  av.  xratu§  ,geistige  Kraft'.
Ai.  kathind-,  kdthora-  ,hart,.  fest,  steif*  kann  auch  mit  idg.  l  zu  cymr. caled,  mir.  calad  ,hart*,  gall.  -caletos  gehören  (s.  kal-  ,hart*).
Wegen  der  Existenz  eines  weitverbreiteten  iber.-mediterr.  *carra  , Stein, Steinhaufe*  (v.  Wartburg  FEW.  s.  v.)  ist  die  Zugehörigkeit  folgender  Worte zweifelhaft,    die   teils   hierher   oder   zu   {s)ker-   , schneiden*   gehören,    teils
nichtidg.    Herkunft  sein  können:
34*
532  ,
air.  carrac  f.  (nir.  carraig)  ,Felsen,  Klippe'  und  crec  f.  ds.,  Gen.  craice^ creice,  mir.  auch  Nom.  craic  (nir.  craig)  f.  ds.,  Gen.  crexa,  stammen  alle  aus dem  Brit.,  ebenso  mir.  crach  ,rauh'  (==  schorfig) ;  zu  acymr.  carrecc,  cymr. carreg  t  , Stein,  Felsen'  (*karrika),  bret.  karreg,  corn.  carrefc  ds.,  vgl. cymr.  carro^  ,Bach'  (*karräka),  eig.  , Steinbach'  =  mir.  carrach  ,schorfig« und  gallo-rom.  *cracos  , Stein'  (v.  Wart
=== leaf 190 ===
burg  FEW.  s.  v.),  acymr.  creiÄ:, cymr.  craig  f.  (*kraki)  , Felsen',  bret.  krag  ,Sandstein',  cymr.  crach  , Schorf =  bret.  (Vannes)  kräh  ,kleiner  Hügel,  Spitze'  {*krak-,  *krakk-,  vielleicht durch  Metathese  aus  '^kar-k-)  usw.  Grundformen  sind  voridg.  *karr-  oder  idg. *(s)Är-s-  (ergäbe  kelt.  carr-),  bzw.  "^kar-k--^  ebenso  zweideutig  ital.-venezian. (ven.)  scaranto,  caranto  ,steiniger  Bergbach'  und  ven.  ON  Scarantia  > Scharnitz  (Tirol),   Carantania  , Kärnten',  usw.;
desgleichen  germ.  *har(u)gaz  , Steinhaufen,  Opferstätte'  in  anord.  hgrgr , Steinhaufen*,  ags.  hearg  m.  ,heidnischer  Tempel',  ahd.  harg  ,Hain,  Tempel' (finn.  Lw.  karko  ,Holzstoß,  Stapel',  harkko  , Klumpen,  Haufen'),  vielleicht auch  zu  air.  cymr.  bret.  carn  , Steinhügel,  Steingrab',  und  ahd.  hart  ,Berg- wald',  ags.  harad,  -ed  ds. ;  kaum  hierher  als  ,Waldbewohner'  der  altgerm. YN  Xaqovdsg,  Harudes,  ags.  Hasredas,  aisl.  Hordar]  eher  zn  air.  caur^ cur  ,Held'  (*karut-s).
WP.  I  30  f.,  345  f..  WH.  I  8,  151,  166,  168,  Loth  RC  43,  401  f.,  Thur- neysen  KZ.  48,  71;  59,  7  Anm.,  Much  Hoops  Reallex.  s.  v.  Harudes.
kär-  , Wachs'.
Gr.  ytrjQÖg  , Wachs',  yiTjglov  ,Wabe,  Wabenhonig'  kann,  obwohl  dor.  ymgög nicht  genügend  gesichert  ist,  außerhalb  des  lon.-Att.  Lehnform  aus  dieser  ^ Dialektgruppe  sein,  welchenfalls  lat.  cera  als  griech.  Lw.  gesichert  wäre;  -4,
lit.  korys  , Wabenhonig,  Honigscheibe  der  Bienen',  lett.  käres  Nom.  PL  ds.;    '
poln.  skarzyk  ,der  Vorstoß  im  Bienenstock'.  ?.
WP.  I  355,  WH.  I  202,   Specht  Idg.  Dekl.  52.  ?
karS'  ,kratzen,  striegeln,  krämpeln'.
Ai.  kasati  , reibt,  schabt,  kratzt'  (mind.  aus  *krsati),  unklar  kasäya- ,herb,  bitter,  scharf  usw.  (auch  kustha-  n.  , Aussatz',  mind.  aus  *krstha-'^)]-
lat.  carrö,  ere  ,(Wolle)  krämpeln',  Carduus  ,Distel'  (auf  Grund  voa "^carridus  ,kratzend');
lit.  karHü,  karsti  , kämmen,  striegeln,  krämpeln',  lett.  kärSu,  kärst  ,Wolle kämmen';
abg.  krasta  (*kor-stä\  russ.  korösta  f.,  skr.  krästa  ,Krätze,  Grind' ;
mnd.    harst    ,Rechen,    Harke',   wahrscheinlich   auch   mnd.   nhd.   harsch   . ,hart,  rauh',  nhd.  verharschen  , Schorf  bilden,  bei  Wunden',  mdartl.  harsch jSchneekruste',  mhd.  harsten,  verharsten  ,rauh,  hart  werden';    mit  germ.
r
533
Ablautneubildung  und  anlaut.  s-  von  der  Wurzel  sker-  hierher  auch  andd. ofskerran  starkes  Verb  , abkratzen*,  ahd.  scerran,  mhd.  scherren  starkes  Verb kratzen,  schaben*,  Intensivbildung  *skarzön  in  norw.  skarra  ,einen  schar- renden Laut  hervorbringen',  mnd.  mhd.  scharren  , kratzen,  scharren*, schwed.  skorra,  mnd.  schurren  , einen  scharrend
=== leaf 191 ===
en  Laut  geben*.
Der  Wurzelvokal  ist  a ;  der  Intonationsunterschied  zw.  Lit.  und  Slav. bleibt  noch  zu  erklären.
WP.  I  355f.,  WH.  I  173f.,  Trautmann  118f.
kas-,  kas-no-  ,grau*.
Lat.  cänus  (^cas-no-s)  ,grau,  aschgrau*,  pälign.  casnar  ,senex*,  ahd.  hasan ,grau  glänzend,  poliert  fein*;  sabin.-lat.  cas-cus  ,alt*  (ursprüngl.  , altersgrau') ;
anord.  hgss  (^kas-iio-),  ags.  hasu  , graubraun*,  mhd.  heswe  ,bleich,  matt*.
Dazu  die  Benennung  des  Hasen  (vgl.  russ.  särjdk  , grauer  Hase*  :  seryj ,grau*):
ai.  sasd-  m.  (aus  *sasd-),  afghan.  soe,  Pämird.  süi]  cymr.  ceinach (-acÄ- Erweiterung  eines  *cein  =  *kasnl  , Häsin*,  Pedersen  KG.  I  86); ahd.  haso,  mit  gramm.  Wechsel  ags.  hara^  anord.  heri  (eine  Ablautsneu- bildung mit  germ.  e  scheint  norw.  schwed.  mdartl.  jase  =  anord.  *hjasi), apr.  sasins  m.  ,Hase',  sasin-tinklo  , Hasengarn*,  ON  Sassenpile  , Hasenberg'.
Eine  Erweiterung  der  Stämme  *kasen-  (:  kas-n-o-)  und  *kaseu-,  kasou- (:  kas-u-o-)  mit  Formans  -dho-  und  Schwundstufe  der  Wurzelsilbe  wird  in gr.  ^av&oq  , blond,  braun'  aus  "^ks-en-dho-  (falls  ^av-  Verquickung  von  *^ev- und  *Ja-=*?w-)?  und  ^ovd-ög  angeblich  ,goldgelb',  falls  aus  *ks-ou-dho-, angenommen,  aber  sehr  zweifelhaft.
WH.  I  156,  Hofm.  Etym.  Gr.  Wb.  221,  Trautmann  330,  Schwyzer  Gr. Gr.  I  329.
käs-,  k9S'  , zurechtweisen,  anweisen';  nur  arisch  und  armenisch.
Ai.  sästi,  1.  PI.  sismdh  , weist  zurecht,  züchtigt,  herrscht,  befiehlt,  belehrt', Partiz.  Aor.  si$dnt-  , unterweisend*,  sistd-  , zurechtgewiesen,  angewiesen, unterwiesen*  (jünger  sästa-,  wie  av.  sästa-)]  av.  sästi  ,heißt,  lehrt',  Opt. sisöit,  a-slHa-  ,verheißen* ;  ai.  sästdr-  , Bestrafer,  Gebieter*  =  av.  sästar- , Gebieter,  Fürst',  mpers.  sastär  ,Herrscher*,  ai.  iästrd-  n.  , Anweisung, Belehrung,  Lehrbuch',  av.  säx'^an-  n.  , Lehre*,  säsnä  , Lehre,  Gebot*,  ai. sisti-  f.  , Bestrafung,  Befehl*  (jünger  sasti-)^  sisya-  ,zu  unterweisen',  m. ,Schüler' ;
arm.  säst  ,Vorwurf,  Drohung,  Strenge,  Autorität',  sastem  , drohe,  schärfe ein,  gebiete',  sastik  , heftig'  (alles  iran,  Lw.  ?).
WP.  I  358,  WH.  I  179.
534  •
1.  kat-  , flechtend   zusammendrehen,   zu   Ketten,    Stricken,    Hürdengeflecht'.
Lat.  catena  , Kette'  (*cates-nä),  cassis,  -is  ,Jägergarn,  Netz'  (wegen  caUna eher  =  *kat-s-is  als  *kat-ti-s-  vielleicht  auch  casa  ,primitive  Hütte'  (xlt- ^prünglich  aus  leichtem  Geflecht;  wohl  dial.  aus  *catiä,  wie  osk
=== leaf 192 ===
.  Bansae aus  Bantiae))
vielleicht  hierher  caterva  f.  ,Hau£e,  Schar,  Truppe'  (*kates-ouä),  umbr. kateramu,  caterahamo  ,catervamini,  congregamini',  doch  s.  unten  unter  1.  A;e^.
cymr.  cader  ,Festung'  (nur  in  ON),  air.  cathh^  , Stadt';
vielleicht  aisl.  hadda  f.  ,Ring,  Henkel,  Bügel' _(*Äa;>i/)ün  :  catena;  recht unsicher),  wohl  ags.  heador  n.  ,Einschließung,  Gefängnis';
ksl.  kotbCh  ,cella,  Nest',  russ.  koty  PL  ,Fischwehr,  Fischzaun',  skr.  kdt, (dial.)  kbtac  ,kleiner  Stall';  dial.  ,Art  Fischfang'  usw.  und  bulg.  kötara, kötora,  kötor  ,Hürde',  skr.  kotar  ,Zaun',  kotär  , Gebiet,  Grenze'  (,*aus Zäunen'),  sloven.  kotdr  ,Bezirk'  (s.  Berneker  386,  588) ;
WF.  I  338,  WH.  I  175 ff.,  181  f.
2.  kat-  ,Junge  werfen;  Tierjunges'.
Lat.  catulus  ,Tierjunges,  bes.  junger  Hund  oder  Katze',  umbr.  katel^ Gen.  katles  , catulus';
aisl.  hadna  f.  , junge   Ziege',   mhd.    hatele,   nhd. -Schweiz,    haue   , Ziege';
slav.  kotiti  s^  (russ.  kotitbsja  usw.)  , Junge  werfen',  dial.  köthka  ,Lamm', skr.  kot  jBrut',  poln.  wy-kot  , Zicklein'  usw.  (s.  Berneker  589  f.).
WP.  I  338  f.,  WH.  I  183.
kat-  ,kämpfen',  katu-  :  5af (e)ro-  ,Kampf'.
Ai.  sätdyati  ,haut  zusammen,  wirft  nieder';  sdtru-  m.  ,Besieger,  Feind';
gall.  catu-  , Kampf  in  GN  Catu-rlx  , Schlachtenkönig',  air.  cath  , Kampf; Truppe,  Schar',  qymr.  cad  ds.,  corn.  cas  m.  ,Kampf';  cymr.  cadr(*kat-ro-) , stark',  abret.  cadr,  mbret.  kazr^  nbret.  kaer  ,schön';  cymr.  cadarn  , stark', bret.  kadarn  ,tapfer';  dazu  auch  nach  Loth  RC  42,  84  f.  cymr.  cadw  m, , Truppe,  Schar'  (^katuo-),  als  Verb  »bewahren,  schützen';  abrit.  Mars Belatu-cadros  enthält  hingegen  die  Wurzel  kad-  , glänzen' ; ■  aisl.  Jiod  f.  ,Streit'  (=  gall.  catu-),  GN  Hgdr,  got.  MN  Theuda-hatha-8, ags.  headu-,  ahd-  hadu-  , Kampf  in  Namen  wie  Hadu-mär,  Hedwig]  mhd. Jiader  ,Zank,  Streit';
falls  man  hier  slav.  k-  für  k-  annehmen  darf  (vgl.  oben  S.  18^),  abg. kotora,  russ. -ksl.  kotera  , Streit,  Kampf;
möglich   wäre   Heranziehung   des   thrak.  VN   der   IccrgaL,  ^arQO-^evtai]
daß  in  gr.  aarlvrj  , Luxuswagen',  adriXla'  nleiäg  tö  äargov,  die  als  phryg. Worte  mit  arm:  sayl  , Wagen'  (arm.-phryg.  *satilia)  zusamme
=== leaf 193 ===
nhängen,  die Bed.  des  , Streitwagens'  die  ursprüngliche  sei,  ist  unerweisbar.
WP.  I  339,  340,  Vendryes  RC.  43,  246,  M.  Leumann  Hermes  68,  359,
1
535
}caU'  ^erniedrigen^  demütigen;  kau-no-s  Schande,  Schämt
Gr.  T^avvöq'  xazög  (ay,Xr]QÖg,  in   letzterer  Bed.  zu  v-alo),  Schulze  KZ.  29
270  Anm.  1)  Hes.  und  'Aavoög  (oder  xavgog)'  v.av.6g,  auch   '/.avaqdv'   yiaKÖv
Hes.;
got.  Jiauns   ^niedrig,  demütigt   (haunjan   ^erniedrigen^),    ahd.    höni    ,ver-
achtet,  elend,  niedrig^  (honen  ,schmähen,  höhnen^),  ags.  hean  ^niedrig,  elend,
erbärmlich^  (hynan  ,schmähenQ,  ahd.  hönida,  as.  hönda  ,Schande^,  afries.
hänetJie  ,Anklage^,  ahd.  höna  ,Hohn^;
anord.  häd  {*hawipa-)  n.  ,Spott^,  mhd.  hüren  ,kauern%-
lett.    käuns   m.   ,Schmach,   Schande,   Scham^,    käuneties   ,sich   schämen,
blöde  sein^,  käuntgs  ,schamhaft,  verschämt,  blöde^; lit.  küviüos,  küvetis  ,sich  schämen'. WP.  I  330,  Feist  249  f.,  Trautmann  122.
käu-,  k9U-  ,hauen,  schlagend
Lat.  (mit  präsensbildendem  d)  cüdö,  -ere  ,schlagen,  klopfen,  stampfen, prägen^  (wohl  für  *caudö  nach  den  viel  häufigeren  Kompos. ;  vgl.)  caudex, codex  ,Baumstamm,  Klotz;  zu  Schreibtafeln  gespaltenes  Holz,  Notizbuch*^, cödicillus  ,Scheitholz^,  caudica  ,aus  einem  Baumstamm  gemachter  Kahn^, incüs,  -üdis  f.  ,Amboß^;  toch.  A  kot-y  B  kaut-  ,spalten';
ahd.  houioan  (Äto),  ags.  heawan  (heow),  aisl.  hqggua  (Jiiö)  ,hauen  (hieb)^ (dazu  als  ,zu  Hauendes^  got.  usw.  hawi  ,Heu'^) ;
lit.  kduju,  köviau,  kduti  (*käu{ö)  ,schlagen,  schmieden;  kämpfen^,  kovä ,Kampf',  lett.  nüo-kaut  ,erschlagen,  töten*^,  kava  ,Schlag,  Schicht^  (*Ä:aw-), lit.  küjis  ,Hammer^  =  apr.  cugis  ds.  (abg.  kyjh  ds. ;  lit.  kilgis  ist  aus  küjis nach  kügis  ,Heuhaufen^  umgebildet);
abg.  kovQ  (später  ksl.  kujg)  kovati  ,schmieden^  (=  ahd.  homuu),  serb. küjem  (dial.  kbvem)  kbvati  ,schmieden,  prägen;  (ein  Pferd)  beschlagen^, ksl.  kyjb  ,Hammer^  (*kü-io-),  russ.  kuzm , Schmiedearbeit^,  schwundstufig  abg. k^znh  ,List^  (,Ränke  schmieden'^)  usw. ;  toch.  A  ko-^  B  kau-  ,töteii^
WP.  I  330  f.,  WH.  I  186,  300  f.,    Trautmann  123.
käu-,  keu-,  kü-  ,heulen^;  kauä  ,schreinder  Vogel;  Schallwurzel,  teils  mit anlaut.  kj  teils  mit  k.
Ai.  käuti  , schreit^.  Intens,  köküyate  ,schreit,  tönt,  seufzt*  (Gramm.), köka-  m.  ,Eule,  Hund^?  (,schreiend;  heulend^);  kohila-  , Kuckuck^;
arm.  kuk  jOTsvay^ög'  (:  lit.  kaukti,  Meillet  Msl.  12,  214;  die  Nichtver- wandlung  des  2.  ä:  zu  5  nach  u  ist  im  Schallworte  kein  Einwand);
gr.  xw-xi5-co  ,schreie,  wehklage^  (dissim.  aus  *xi;-xt;-w),  xcüxv^a  ,Wehklage^; xavä^,  -äxog,  ion.  -i^?,  hom.  X7;^,  -Y.6g  f.,  Y/qv^,  -cxog  ,eine  Möwenart^; mit  gebrochener  Reduplikation  (wie  ai.  
=== leaf 194 ===
köka-,  lit.  kaukti,  saukti,  slav. kukati  usw.)  Y.avv.aViag,  Y,avy.iaXogj  y.avy.LdXr,g  Vogelnamen  (Hes.) ;
536  f
aber  mcymr.  cuan,  cjmv.  cwan,  abret.  couann,  nbret.  kaouan,  dial.  cavan kotian,  kouhen  ds.  (Ernault  RC  36,  206  3)  sind  wohl  onomatopoetiscLe Neubildungen ;
lat.  (gall.)  cavannus  ^Nachteule'  (Anthol.  lat.);
ahd.  hüiüo  ,Eule^,  hüwila,  hiuwula  ^Nachteule^,  ahd.  hiuwilön  ,jubeln< mhd.  Muweln,  hiulen  ,heulen,  schreien^,  mnd.  hülen,  mengl.  hülen,  engl. howl ;
lit.  (s.  oben)  kaukiü,  kaükti,  lett.  käukt  ,heulen,  von  Hunden  oder  Wölfen', lit.  sukükti  jds.j  aufheulen^,  kaukaU  ^eine  Art  WasservogeP,  lett.  kaüka ;,Sturmwind^ ;
lit.  kövas  m.  _,Dohle^,  köva  f.  ^Saatkrähe'  (*käuä  =  poln.  kawa)-^
russ.  kdvka  ,Froscli^,  dial.  ^Dohle^,  kdvath  ^stark  husten',  klr.  (usw.) kdvka  ,Dohle^,  kavcdty  ^kreischen' ;  ablaut.  (*Ä:ew-)  bulg.  <^dvka,  serb.  ^ävha, öech.  cavka  , Dohle';  aksl.  kuja-jg,  -ti  ,murren';  russ.  kükath  ,murren, mucksen',  serb.  kükati  ,wehklagen'  usw.
Mit  -h~f  -h(h)o-:  ai.  kükkubha-  m.  , wilder  Hahn,  Fasan',  gr.  xovxovgpag ,Vogelart'  (spät,  kaum  echt  gr.);  schallnachahmend  sind:  y.i%vßog  wohl ,Nachteule'  (daneben  'Ai%y.aßrjy  yiUv^og  (daraus  lat.  cicuma),  xtxufi/g  ds., KL%7,aßav  ,deren  Schrei'),  lat.  cucuhiö,  -Ire  vom  Schrei  der  Nachteule (Thomas  Stud.  39  nimmt  Hiat  füllendes  h  an);  auch  die  i(Ä)-,Suffixe' der  vorgenannten  könnten  so  aufgekommen  sein.
Mit  -g-:  ai.  küjati  ,knurrt,  brummt,  murmelt';  norw.  Tiauke  ,johlen, rufen'.
Mit  -p-:  got.  liiufan  , wehklagen*,  anord.  hjüfra  ds.,  ags.  heofan  ds., as.  hiovan,  ahd.  hiofan^  Mob  an  ds.
Mit  -r-:  ai.  cdköra-  m.  ,eine  Art  Rebhuhn';  lat.  caurire  ,schreien,  vom brünstigen  Panther';  aksl.  kurz  ,Hahn',  ksl.  kurica  ,Henne';
Mit  anlaut.  Palatal:
Ai.  süka-  m.  ,Papagei';  arm.  sag  ,Gans'  (*kaua)  =  aksl.  sova  ,Eule' (:  kelt.  cavannus)]  lit.  saukiüj  §aükti  ,schreien,  laut  rufen,  nennen'; russ.  sycb  ,Zwergeule,  Sperlingseule',  cech.  syc  ,Eule'  (^kük-ti-)-,  unsicher aksl.  Surm  ,Geräusch'  (^IcEu-mo-s?  Brugmann  II ^  1,  247).
Vgl.  Suolahti  Dt.  Vogelnamen  185  (hier  über  die  Neuschöpfung  ahd. kaha  ,Dohle'  usw. ;  vgl.  lit.  kövas  usw.  ds.).
WP.  I  331  f.,  WH.  I  184,  190,  298,  Trautmann  122.
kau{9)lä  :  külä  ,Geschwulst;  bes.  Leibschaden,  Leistenbruch'.
Gr.  ion.  xrjlr],  att.  xdlr]  ,Geschwulst,  bes.  Leibschaden',  ßovßcovo-Ki^Xfj ,Leistenbruch'  u.  dgl.;  xala^ec  dyxoürai.  ""Axaioi  Hes.,  xc^Aa^ta*  5'yxog  Hes. (vokalisch  sehr  schwierig;  ion.  ytrjlr]  aus  Haf-sX-a,  att.  ach.  'a&I-^,  -5  aus
Y.äJ^-eX-a  ?) ;
537
anord.  haull,  ags.  heala,  abd.  höla  L  ^Leistenbruch^  {*käu[9]läy  allen- falls *kdu[d]lä)]
tiefstufig  ksl.  kyla  ^ds/ ;  russ.  kild  ,ds. ;  Knorren  am  Baum^,  serb.  klla ds.
=== leaf 195 ===
;  lit.  dial.  knie  f.  ^AuswuchS;  Knorren^
WP.  I  333,  Trautmann  144.
^au-1-,  ku-1-  ,hohl;  Hoblstengel;  Röhrenknochen^
Gr.  Y.avX6g  m.  ^Stengel;  Federkiel,  Schaft^;  lat.  caulis  (^cölis,  caulus) ^Stengel,  Stiel  an  Pflanzen^;  mir.  cuaille  ,PfahP  {*kaullnio-) ]  lit.  kdulas m.  ,Knochen^  (Stoßton  sekundär),  lett.  kaüls  ,Stengel,  Knochen^,  apr. caulan  n.  ,Knochen,  Bein^
Schwundstufig:  ai.  külyam  n.  , Knochen^,  kulyä  f.  _,Bach,  Graben,  KanaF; anord.  liolr  ,hohP,  ahd.  ags.   hol  ds.,  got.  ushulön  ,aushöhlen^
WP.  I  332,  WH.  I  188  f.,  Trautmann  122;    vgl.  unter  2.  keu-.
kaus-  ,das  Los  ziehen^?
Gr.  y^avvog  ,Los^  (*yLccva-vog) ;  ksl.  k^h  m.  ,Los',  Hsiti  s^  ,losen^,  prekzsiti ,im  Würfelspiel  gewinnend WP.  I  332,  Berneker  672.
ke-  s.  unter  ko-,
ked-  ,rauchen,  rußen*.
Ai.  kadrü-  , braun*,  vielleicht  auch  kadamba-  m.  ,Nauclea  cadamba, ein  Baum  mit  orangefarbenen  Blüten'  und  kädamha-  m.  ,eine  Gansart mit  dunkelgrauen  Flügeln*;
aksl.  kadilo  ,Räucherwerk^,  kaditi  ,räuchern*,  russ.  cad  , Dunst*,  serb. 6ad  jcaligo*,  caditi  , rußig  werden*  (usw.,  s.  Berneker  133,  467),  vielleicht apr.  accodis  (^at-codis)  , Rauchloch,  durch  das  der  Rauch  herauszieht* ;
als  , Räucherhölzer*  sind  anzureihen  (?):
gr.  TciÖQog  ,Wacholder;  später:  Pinus  cedrus',  -asögig  ,Wacholderbeere ; Frucht  der  Zeder*;  lit.  kadagys,  apr.  kadegis  , Wacholder*  (aus  estn.  kadakas entlehnt?).
WP.  I  384f.,  Trautmann  112,  Specht  Idg.  Dekl.  147.
keg-y  keng-  und  kek-,  kenk-  , Pflock  zum   Aufhängen,   Haken,    Henkel*; auch  ,spitz  sein*;  vgl.  das  ähnliche  kak-^   kank-]  und  kenk-^  konk-, Npers.  (iang  , Klaue,  Faust*  (*kengo-)',
mir.  ail-ctieiig  f.  ,Rechen,  Waffengestell*  ( :  lit.  kenge,  s.  unten) ;
germ.  *hakan-j  *h5ka-,  *hekan-  m.  ,Haken*  in:  aisl.  PN  Haki  m.  , Haken*,
haka   f.  ,Kinn',   ags.  haca   m.   ,Riegel*,   hcecce  f.  ,Krummstab*;   aisl.   häkr
m.  jFrechling*,  ahd.  häko,  häggo  ^Haken^,  ags.  höc  m.  ,Haken*,  mnd.  hok^
huk    m.    ,Winkel,    Ecke,  Vorgebirge*,    aisl.    hekja    f.  (*hökiön-)   , Krücke',
538  •
heUll  m.  ,Hinterbug*;  mit  intensiver  Gemination:  ags.  haccian  ,liackeu* mnd.,  mhd.  hacken  ds.,  und  die  ^-Verba:  a^s.  ofhceccan  ,amputareS  ahd. hecchen  ,beißen,  stechenS  mhd.  hecken  , hauen,  stechen*;  nasaliert  mnd. hank  ,Henkel*  (daraus  aisl.  hgnk  m.,  hanki  f.  ,Henkel'),  ndl.  honk,  ostfries. hunk  ,Pfahl,  Pfosten';
germ.  *hakilö  f.  ,Hechel'  (von  den  gekrümmten  Eisenzähnen)  in:  asächsj hekilon  ,hechelnS  engl,  hatchel,  mhd.  hechel  ^Hechel\  norw.  hekla  ,Hech
=== leaf 196 ===
el, StoppeP ;
germ.   *häkuda-  m.  ,Hecht'  (nach  den  spitzen  Zähnen)  in  ags.  hacodA *hakida  in  ags.   hacid  m.,  ahd.  hacMt,  hechit,  mnd.   heket  ^Hecht^^
lit.  kenge  f.  , Haken,  Klinke';
slav.  *kog^th  m.  in  russ.  kögoth  ,Klaue,  gekrümmte  Eisenspitze^,  osorb. kocht  ,Dorn,  Stachel'  (:  germ.  *hakuda-)-
vielleicht  hierher,  als  ,au£  einen  Haken   hinaufhängen,  wie  mit  einei Haken   kratzen,   reizen':   bulg.  kdcbj  kdc(ii)vam   ,erhebe,   erhöhe,    hänge*^ za-kdchj   -kdcam   ,hänge,    fasse,   necke',    serb.    zäkaciti    ,anhaken',   sloven. kdclti  ,necken,  ärgern'  (Berneker  465  f.).
WP.  I  382  f.,  WH.  I  307,  Trautmann  112,  Wissmann  Nom.  postverb. 182  f.,   Petersson,  Heterokl.  9 1  f . ;   Stokes  BB.  25,  252.
•'« kei-    ,in    Bewegung    setzen,    in    Bewegung   sein'    (:    koi-  :  kf-);    eu-Basis] (z.  T.  mit  22-Infix)  ki-{n-)eu-;  schwere  Basis  kiQ-  (:  Jcie-?).
Gr.  xio)  ,gehe  weg,  fahre'  ist  späte  Neubildung  zum  Aor.  e/.LOv]  Imper.i Y.U,  Partiz.  xiwy;
hom.  Präteritum  fxsr-sytiad-s,  -d-ov  {i  metr.  Dehnung)  , folgte  nach,  durch- streifte', Y.iazo'  s-ALvelvo  Hes.  (schwere  Wz.);  dvo-ytlvÖLog,  -y.lvöag  ,Esel- treiber',  y,Lvda^  , beweglich,  ei'nivrjTog''  (vgl.  zur   Bildung  äXlvdo),  ytvXlvdüijy
von  ki-n-eu-  :  gr.  y.tvv^ai  , werde  bewegt,  erschüttert,  gehe',  yavvaaoy,ai, ,sch wanke  hin  und  her',  '/.ivio)  ,setze  in  Bewegung,  treibe'  (*xlv«J^-ü>) ;
alb.  q^oj  , wecke,  erwecke'  (*kien{ö)j  qoj  , schicken,  senden'  (*ds-köj\ cys,  cyt  , reize,  necke'  (*ter-k{u-t-{ö),  syei^  syen  (*kiu-n-iö)  ,bestürmen,  an- fallen' (Jokl  Mel.  Pedersen  149 f.');
lat.  cieöj  eiere  (sekundär  ciö,  clre)  ,in  Bewegung  setzen,  rege  machen, herbeirufen'  (eiere  =  idg.  ki(i)e-??)j  citus  ,schnell',  cito,  -äre  ,in  Bewe- gung setzen,  kommen  lassen,  vorladen',  solli-citus  ,ganz,  stark  bewegt, beunruhigt,  in  Angst  und  Gefahr',  cunctus  (*con-citos),  gesamt,  sämtlich*.
Erweiterungen  von  der  einfachen  Wurzelform  kei-  aus :
Mit  d  (cZ-Präsens?):  vielleicht  ir.  cid-  z.  B.  mcisse  ,invecta',  Pass.  Konj. as-cesar   gl.    ,exseri'   (usw.,  Pedersen  KG.  II  490  f.),   sehr   wahrscheinlich  "^ got.  haitanj  ahd.  heisan,  ags.  hätan,  as.  hetan,  anord.  heita  ^heißen  {j=  aa- treiben),  befehlen,  anrufen,  nennen^;   vgl.  osset.  sidin  , rufend
I
539
Mit  i(o)- Formans:  Auf  *kEi-lo-s  ,bewegt,  wippend'  kann  beruhen:  lit. Jctele,  kyU,  lett.  cielaioa^  apr.  kylo  , Bachstelze',  acech.  cily  ,lehhaft';  lat. cillö,  -ere  , bewegen'  ist  vielleicht  nur  Grammatikererfindung.
Mit 
=== leaf 197 ===
 s:  ai.  cistati  ,bewegt  die  Glieder,  ist  in  Bewegung',  cesta- n.j  cestä ^Bewegung,  Gebärde'.
Wurzelform  ki-eu-  ohne  Nasalinfix:
ai.  cydvate  ,regt  sich,  geht  fort',  av.  5(y)avaite  ,setzt  sich  in  Gang, Marsch',  apers.  asiyavam  ,marschierte',  ai.  cyautnd-  n.  ,Unternehmung, Bemühung',  av.  syaod-na-  n.  ,Tun,  Handeln,  Wirken',  syaoman-  n.  ,Tat, Werk';
arm.  cu  (=  ai.  cyuti-)  , Aufbruch',  cvem  ,ich  breche  auf,  reise  ab',  Aor. (zum  Präs.  ert'am)  cogay  ,ich  ging'  (^kioit-)-,
gr.  Gsvo)  ,setze  in  rasche,  heftige  Bewegung',  Med.  ,eile,  bin  erregt' (aevstai  =  cyavate]  der  Diphthong  kann  nach  den  außerpräs.  Formen und  nach  unthemat.  Gevxai  festgehalten  sein),  hom.  saavTO  ,eilte',  Partiz. Perf.  ioav^svog,  iTvl-aavTog  ,herandrängend,  daherstürmend'  (=  ai.  cyutä- ,getrieben',  vgl.  av.  fra-süta-  ,in  Gang  gekommen*),  Ttav-avöir]  ,in  Eile'; att.  aovfxai  , bewege  mich  rasch  oder  heftig'  (^aoföofiaij^  avsi  (Bacchyl.) ,treibt',  iaoorjixevov  TsdoQvßri^hov,  öq^Tjjj^vov  Hes.,  hom.  Xao-Gaöog  ,die Völker  zum  Kampfe  antreibend';  att.  T€Vjj,ü)i.iaL  ,betreibe'  (vgl.  av.  syao- man-)-,  Tsvrd^u)  ,beschäftige  mich  anhaltend  mit  etwas';  eine  Dehnstufen- bildung wie  ai.  cyautnd-^  aber  rnit  geschwundenem  u^  ist  das  wohl  hierher gehörige  gcjtqov  ,das  hölzerne  Rad',  kTtlaooiXQOv  ,Radreifen'.
WP.  I  361  ff.,  WH.  I  213  f.,    Schwyzer  Gr.  Gr.  I  679,  686,  745.
I.'  kei-  ,liegen ;  Lager,  Heimstätte,  traut,  lieb  (von  derselben  Siedlung') ; koi'to-  , Lager' ;  kei-mo-,   koi-mo-  , vertraut',    kei-uo-,  ki-uo-   ds.
Ai.  süe  (älter  sdye)^  3.  PI.  sei%  av.  saUe  (:  gr.  -KelxaL)  ,liegt',  3.  PL sözVe,  ai.  sayate,  -ti  ,liegt,  ruht',  §ayä,  sayyä  , Lager',  madhyama-si-  ,in der  Mitte  sich  lagernd,  liegend',  ni-sl-tlia-  m.  »Mitternacht',  usw. ;
gr.  Y,sZTai  jliegt',  3.  PL  -/.eazai  aus  *xejnt-j  umgebildet  nach  y.sl-,  hom. xelaTat]  jung  ist  hom.  -Asoviai  (:  ai.  sayante)]  '/.oZxog  m.,  xotr^  f.  , Lager', äy,OLTig  , Gemahlin'  (mit  ion.  Psilose  aus  *&'-xoiTi$);  vgl.  bret.  {d)argud ,leichter  Schlaf  (^-are-koito-)]  v.oi^da)  , bringe  zu  Bett,  schläfere  ein'  (vgl. got.  haims,  air.  cöim,  lett.  säimey  auch  lit.  seimyna,  ags.  hceman).  Zweites Kompositionsglied  -x^-o-  in  Ttsqioöog,  vsoaaög,  u.  dgl.  Sehr  wahrscheinlich lat.  cünaej  cün
=== leaf 198 ===
äbula  PL  , Wiege  ,Nest'  (*koi-na)  und  anord.  hldj  hidi  n. ,Lager  des  Bären'  (*kei-to-)',
hitt.  Mediopassiv  ki-it-ta  (kitta)  und  ki-it-ta-ri  (kittari)  ,liegt' ;  vielleicht auch  lyk.  sijeni  ,liegt'  (Pedersen,  Ljkisch  u.  Hitt,  17).
Mit  dem  Begriffe  ,Heim,  traut,  lieb':
540  •
mit  i-Suffix  ai.  Hla-  n.  , Gewohnheit,  Charakter*,  air.  ce{i)le  , Genosse, Gatte*  (*kei-U{o-s\  mit  sekundärem  i  cymr.  cilydd  , Genosse*,  usw.;
mit  i22-Suffix:
gr.  7ioi(.iaa)  (s.  oben),  yLsmrjhov  ,aufbewahrtes  Gut*  (von  *%aliia  n.  ,Lager*)' dehnstufig  xcj.aiy  f.  ,Dorf*  (*^ö[i]mä);
air.  com,  cöem  ,lieb*,  acymr.  cum^  ncymr.  cu  usw.  ,lieb*  (koimo-);
got.  haims  f.  (z-St.)  ,Dorf,  Flecken ;  PI.  dygoi^  anord.  heimr  m.  ,Heimat Welt*,  ping-heimr  ,die  beim  Thing  anwesende  Versammlung*,  ags.  häm as.  kern,  ahd.  heim  , Heimat,  Haus,  Wohnung*  (ags.  hceman  ,beschlafen heiraten*,  ursprüngl.  ,y.oifiav^)]
lett.  säime  f.  , Hausgesinde,  Familie*,  ablaut.  lit.  seimyna  i.,  apr.  seimim m.  , Gesinde*;
aksl.  sembja  , Gesinde,  Sklaven*,  semim  ,zum  Gesinde  Gehöriger,  Sklave**
lit.  kiemas  ,Bauernhof*,  kdimas  ,Dorf*,  lett.  ciems  ,Dorf,  Versammlungs- haus*, apr.  caymis  ,Dorf*,  lit.  kaimynas  ,Nachbar^,  kalmene  ,Herde*  sind der  Entlehnung  aus  germ.  *hai'maz  verdächtig;
Trautmann  (112  f.)  nimmt  ablaut.  urbalt.  *kaima-  ra.  und  *köimä  f.  an (idg.  öi :  ai);
mit  ro-Suffix:  arm.  ser  ,Neigung,  Liebe*,  sirem  ,ich  liebe*  (*keiro-)]
mit  uo-Suffix:  ai.  siva-  (=  germ.  Mwa-)  ,traut,  freundlich,  lieb,  wert*, iivd-  (=  germ.  *hiiüa-)  ,vertraut,  lieb,  .heilsam* ;
lat.  clvis  ,Bürger*  =  osk.  ceus  ds.;  die  i-Flexion  nach  hostis  (M.  Leumann Gnomon  9,  237) ;
got.  heuva-frauja  , Hausherr*,  ags.  hlw-cund  ,heimisch*,  hiw-rößden  f. , Haushaltung^,  ahd.  hl-rat  ^Heirat^  ags.  hl-red  ds.,  agutn.  hl-skepr  , Familie*, anord.  hy-hyli  Neutr.  Fl.  ,Hauswesen*  (daneben  ablaut.  *hiwa-  =  ai.  Hvd- in  anord.  herad,  aschwed.  hce-rap  ,Bezirk*,  hce-skaper  ,Familie*  aus  ^Mwa-)] der  germ.  St.  *hiwa-  ist  Kompositionsform  zu  ^hiwan-  ,Hausgenossen  (schaft)* in  anord.  hjü{n\  hjön  ,Ehepaar,  Dienerschaft,  Ge
=== leaf 199 ===
sinde*,  ags.  hlwan,  higan , Hausgenossen,  Familie*,  hlwen  n.  ,Haushalt*,  asächs.  sinhlwun  ,Ehegatten*, ahd.  M(w)un  ,Ehepaar,  Dienstboten*,  Äi(tij)o  , Gatte;  Hausgenosse,  Knecht*, hlwa  , Gattin*,  asächs.  hlwa  ds.;  mit  -ro-  erweitert  anord.  hyrr  ,freundlich, gütig*,  ags.  heorej  hlere  ,freundlich,  sanftmütig*,  mhd.  gihiure  ,mild,  behag- lich*, nhd.  geheuer j  ahd.  as.  unhiuri  ,unheimlich,  grauenhaft*;
lett.  sieva  ,Weib*   {^seiuä  mit  dem  Intonationswechsel  des  Femin.).
WF.  I  358  ff.,  WH.  I  224 f.,  306  f.,  856,   Trautmann  112  f.,  300  f.
2,  kei-   in   Farbbezeichnungen,   meist   für   dunkle   Farben  (s.  auch   ke-ro)) kei-ro-,  koi-ro-  ,dunkel,  grau,  braun*;  ki-uo-  ,Farbe*. Ai.  si-ti-  ,weiß*,  Htm-g-a-  ,weißlich';
i
541
gv.  ycLQacpog,  '/.loa  ,Fuchs'  Hes.,  y^iggög  ,orangegelb*  (das  -rr-  wohl  ex- pressiv) ;
mir.  ciar  , dunkelbraun*  (*kei-ro-)y  ciarann  m.  , Käfer*;  cir  (*kiru-)j  Gen. cera  ,Pechkohle* ;  ceo  (*ki-uo-k-s)  ,Nebel*,  Gen.  dach  (:  got.  hiwi);
aisl.  harr  ,grau,  alt*,  ags.  Aar,  engl,  hoar,  asächs.  ahd.  her  (*haira-) ^würdig,  erhaben*;  Komparativ  ^heriro^  her(r)o  ,Herr^ ;  ags.  h^wen  ,blau* (*haiimna')  ]  got.  hiioi  n.  , Sehein,  Aussehen*,  aisl.  hy  n.  ,feines  Haar, Flaum',  schwed.  hy  ,Haut,  Hautfarbe*,  ags.  hiew,  hi(o)io  n.  ,Erscheinung, Farbe,  Schönheit*,  engl,  hue  ,Farbe*  (idg.  *H-wo-);
aksl.  sär^,  russ.  seryj,  sloven.  s^r  ,grau*  {*koi-ro-),  mit  -cZ-Suffix(?)  aksl. sed^J  skr.  sijed^  russ.  sedoj  ,grau*  (falls  nicht  nach  smed^  ,blaß*,  hled^  ^xkojqög'' umgebildet) ;  a6ech.  Ury^  poln.  szary  ,grau*,  aöech.  sedivy  ds.  weisen  jedoch auf  ein  urslav.  anlaut.  c/i-,  das  von  Pedersen  (KZ.  40,  176  f.)  aus  idg.  kh- erklärt  wird  (wohl  expressiv) ;  hingegen  nimmt  Persson  Beitr.  304 Anm.  1  für  urslav.  *cÄm  Entlehnung  aus  germ.  ^haira-  an,  das  sich  mit echt  slav.  ser^  gemischt  habe.
Daneben  eine  erweiterte  Wurzelform  gleicher  Bedeutung:
kie-f  ki-'j   kie-mo-  , dunkelgrau*.
Ai.  syä-vd-  ,schwarzbraun,  dunkel',  av.  syäva-  , schwarz*,  npers.  siyäh ,schwarz* ;
arm.  (wohl  iran.  Lw.)  seav  , dunkel,  schwarz*;
reduktionsstufig  lit.  syvas  ,weißiich,  schimmelig  (von  Pferden)*,  apr. sijwan  ,grau*,  aksl.  sm  , dunkelgrau*,  russ.  sivyj^  serb.  srlv  ds.;
ai.  iyä-md-  ,schwarzgrau,  schwar
```


## [2026-09-06T15:54:24.990Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==200 || NR==201' POK_02.txt | head -60",
 "description": "Pokorny leaf 199-200 continued"
}
```


### [2026-09-06T15:54:26.676Z] TOOL RESULT

```
sinde*,  ags.  hlwan,  higan , Hausgenossen,  Familie*,  hlwen  n.  ,Haushalt*,  asächs.  sinhlwun  ,Ehegatten*, ahd.  M(w)un  ,Ehepaar,  Dienstboten*,  Äi(tij)o  , Gatte;  Hausgenosse,  Knecht*, hlwa  , Gattin*,  asächs.  hlwa  ds.;  mit  -ro-  erweitert  anord.  hyrr  ,freundlich, gütig*,  ags.  heorej  hlere  ,freundlich,  sanftmütig*,  mhd.  gihiure  ,mild,  behag- lich*, nhd.  geheuer j  ahd.  as.  unhiuri  ,unheimlich,  grauenhaft*;
lett.  sieva  ,Weib*   {^seiuä  mit  dem  Intonationswechsel  des  Femin.).
WF.  I  358  ff.,  WH.  I  224 f.,  306  f.,  856,   Trautmann  112  f.,  300  f.
2,  kei-   in   Farbbezeichnungen,   meist   für   dunkle   Farben  (s.  auch   ke-ro)) kei-ro-,  koi-ro-  ,dunkel,  grau,  braun*;  ki-uo-  ,Farbe*. Ai.  si-ti-  ,weiß*,  Htm-g-a-  ,weißlich';
i
541
gv.  ycLQacpog,  '/.loa  ,Fuchs'  Hes.,  y^iggög  ,orangegelb*  (das  -rr-  wohl  ex- pressiv) ;
mir.  ciar  , dunkelbraun*  (*kei-ro-)y  ciarann  m.  , Käfer*;  cir  (*kiru-)j  Gen. cera  ,Pechkohle* ;  ceo  (*ki-uo-k-s)  ,Nebel*,  Gen.  dach  (:  got.  hiwi);
aisl.  harr  ,grau,  alt*,  ags.  Aar,  engl,  hoar,  asächs.  ahd.  her  (*haira-) ^würdig,  erhaben*;  Komparativ  ^heriro^  her(r)o  ,Herr^ ;  ags.  h^wen  ,blau* (*haiimna')  ]  got.  hiioi  n.  , Sehein,  Aussehen*,  aisl.  hy  n.  ,feines  Haar, Flaum',  schwed.  hy  ,Haut,  Hautfarbe*,  ags.  hiew,  hi(o)io  n.  ,Erscheinung, Farbe,  Schönheit*,  engl,  hue  ,Farbe*  (idg.  *H-wo-);
aksl.  sär^,  russ.  seryj,  sloven.  s^r  ,grau*  {*koi-ro-),  mit  -cZ-Suffix(?)  aksl. sed^J  skr.  sijed^  russ.  sedoj  ,grau*  (falls  nicht  nach  smed^  ,blaß*,  hled^  ^xkojqög'' umgebildet) ;  a6ech.  Ury^  poln.  szary  ,grau*,  aöech.  sedivy  ds.  weisen  jedoch auf  ein  urslav.  anlaut.  c/i-,  das  von  Pedersen  (KZ.  40,  176  f.)  aus  idg.  kh- erklärt  wird  (wohl  expressiv) ;  hingegen  nimmt  Persson  Beitr.  304 Anm.  1  für  urslav.  *cÄm  Entlehnung  aus  germ.  ^haira-  an,  das  sich  mit echt  slav.  ser^  gemischt  habe.
Daneben  eine  erweiterte  Wurzelform  gleicher  Bedeutung:
kie-f  ki-'j   kie-mo-  , dunkelgrau*.
Ai.  syä-vd-  ,schwarzbraun,  dunkel',  av.  syäva-  , schwarz*,  npers.  siyäh ,schwarz* ;
arm.  (wohl  iran.  Lw.)  seav  , dunkel,  schwarz*;
reduktionsstufig  lit.  syvas  ,weißiich,  schimmelig  (von  Pferden)*,  apr. sijwan  ,grau*,  aksl.  sm  , dunkelgrau*,  russ.  sivyj^  serb.  srlv  ds.;
ai.  iyä-md-  ,schwarzgrau,  schwar
zgrün,  schwarz*,  syämaka-  , dunkel- farbig* =  av.  syämaka-  m.  ,Name  eines  Berges*  (auch  säma-  ,schwarz* mit  s-  aus  sy-,  Bartholomae  Airan.  Wb.  1571) ;
lit.  s^mas,  semas  ,blaugrau,  blau';
reduktionsstufig  *kl-mo'  wahrscheinlich  in  lat.  clmex  ,Wanze*  (,dunkel- farbig';  Formans  -fco-,  als  Subst.  nach  der  kons.  Dekl.  wie  sene-x  zu  idg. *seno-s);  vielleicht  im  gr.  EN  Klficav;
mit  anderem  Suffix:  aksl.  sim,  russ.  sinij  ,dunkelblau* ;
auf  einer  Wurzelf.  kiei-  scheinen  ai.  syeni  f.  (wozu  m.  §yetd-  wohl  erst nach  äwi :  eia-,  hdrinl :  hdrita-  usw.  und  ivBtd-  neugeschaffen)  Farbbezeich- nung ,hell,  weiß,  rötlich*,  und  die  nach  der  Farbe  benannten  ai.  §yend- m.  ,Adler,  Falke*,  av.  saena-  ,ein  großer  Raubvogel,  wohl  Adler'  zu  beruhen.
WP.  I  360  f.,  WH.  I  216,  Trautmann  306,  Specht  Idg.  Dekl.  121,  179.
ke{i)-  :  kö^i)-  :  k9(iy  ,schärfen,  wetzen*;  wohl  Weiterbildung  von  ak- jScharf '  (S.  18 ff .) ;  ke-no- :  kö-no-  , Wetzstein';  kQi-ni-  ds. ;  ko-to- ,geschärft'.
542  9
AI  ii-sä'H  (sl-^l-te),  ^y-dti  ,schärft.,  wetzt',  Partiz.  si^a-  ,gewetzt,  scharfe (=  lat.  catus,  air.  catJi),  säta-  ds.,  säna-  m.  (mit  mind.  n  für  n)  ,Wet2-^ Probierstein'  (=  npers.  san  , Wetzstein');  vielleicht  auch  ai.  sild  , Stein, Fels'  {*kd-lä) ;
av.   saeni-   , Spitze,  Wipfel,    spitz'   (npers.  säyaS  ,reibtO  =  anord.  hein:
arm.  sur  ,scharf'  (*fe-ro-),  srem  , schärfe',  sur,  Gen.  sroy,  Schwert,  Messer', sair  , Schneide'  (*Jce-ri-),  Kompos.  sairadir  , Schneide',  davon  '^sardrem^ sadrem  , reize,  treibe  an' ;  vielleicht  auch  sal^  Gen.  sali  , Steinplatte,  Amboß* (*kd-U-,  vgl.  oben  ai.  äild) ;
gr.  '/,(bvog  m.  ,Kegel,  Pinienzapfen,  Helmspitze,  Kreisel'  (=  ai.  säna'\ davon  acüvslov  , Schierlingskraut'  (nach  den  Bl>ättern);
lat.  catus  (nach  Varro  sabinisch)  .acutus,  scharfsinnig'  (==  ai.  si-ta-,  air. cath) ;  cos,  cotis  ,Wetzstein',  auch  cotes,  cautes  f.  PL  ,spitzer  Fels,  Riff'  (das -au-  Hyperurbanismus) ;  catanus  , Zedern  Wacholder'  ist  vielleicht  gall.  Lw.;
air.  cath  ,weise'  (=  lat.  catus,  ai.  si-td-)]
aisl.  hein  f.  , Wetzstein',  ags.  hän  , Grenzstein',  engl,  hone  ,Wetzsteiiil i^kdi-n- :  av.  saeni-)]  mhd.  här  , Werkzeug  zum  Schärfen  der  Sense'  (*£e-r-), mnd.  hären  , schärfen,  scharf  sein'.
WP.  I  454L,  WH.  I  181,  183 f.,  190f.
kei-bh-  ,schnell,  heftig'.
Ai.  sibham  Adv.  ,rasch,  schnell',  sihhya- , schnell  fahrend',  sihhrd-  ,geil(?)*;
got.  haifsts  ,Streit,  Zank',  anord.  heipt,  heifst  f.  ,Feindschaft,  Zorn, Haß',  ahd.  heiftig  ,heftig';  ags.  hcest , Gewalt,  Heftigkeit',  afries.  Äaest,Eile*, mnd.  Äewr , Heftigkeit' ;  ags.  h'^ste,  ahd.  heisti  ,heftig,  gewaltsani'.
WP.  I  364  f. ;  gehört  zu  kei-gh-,  s.  unte
```


## [2026-09-06T15:55:03.321Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== POK kak-/kank- ===\" && grep -n \"kak-,  kank-\\|kank-\\b\" POK_02.txt POK_01.txt | head -20; echo \"=== POK_full lemma keg ===\" && grep -n \"lemma: keg\\|lemma: kak\\|lemma: kei\" POK_full.txt | head",
 "description": "Grep Pokorny for kak-/kank- and full lemmas"
}
```


### [2026-09-06T15:55:03.386Z] TOOL RESULT

```
=== POK kak-/kank- ===
POK_02.txt:2741:cymr.  cainc  (*kankü,  vgl.  den  w-St.  ai.  saTsku-),  PI.  cangau^  mcymr. canghau  ,Ast',  mir.  gec,  nir.  geag  ,Ast'  (mit  sekundärer  Media  im  Anlaut), mit  -s/c-Suffix  gallo-rom.  *gascaria  (frz.  jachere)  ,Brachland',  eigentl. ;Pflugland',  Hubschmied  Vox  Rom.  III  123^;  air.  gescae  , Zweig,  Ast';  mit ^Suffix  air.  cecht  , Pflug'  (wohl  als  *kank-to-  nächstverwandt  mit  ai.  sakti-);
=== POK_full lemma keg ===
43320:Root / lemma: kakka- 
44168:Root / lemma: kak- 
44506:Root / lemma: keg- keng- and kek-, kenk- 
44557:Root / lemma: keid- 
44575:Root / lemma: keis- 
47064:Root / lemma: kei- 
47070:Root/ lemma: kei-\ to move, go, departure, *die, derived from Root/ lemma: Rei-1\ to lie 
49214:Root/ lemma: keiner-: cancer, turtle, derived from Root/ lemma: kam-er-\ to bend, curve,
```


## [2026-09-06T15:55:04.121Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== IEC keng ===\" && grep -n \"^keng\\|^keg\\|kengos\\|kengo-\" IEC.txt | head -20",
 "description": "Grep Mann IEC for keng-"
}
```


### [2026-09-06T15:55:04.173Z] TOOL RESULT

```
=== IEC keng ===
7005:keng- 'seize, grip, hold; hold, hook, grapple, hobble'. Cf. knk- Av. cf. Caro ‘claw, cleft hoof; Per. Gäng ‘claws, fingers”, cf. also čängāl, čängul ‘claws, hook’; Lat. cingo, Gre “tie; gird” beside cingulum, cingula (LW in Ir. ceangal ‘tying, binding, ceanglaim, v.id., and in W cengl, f. “band; girth; hank’; cenglu “bind'); ON hinkr, n. (delay', fr. *kengro-); Sw. hink, pl. at m. “lever, bascule, well-swipe" (?); cf. also (?) OHG hinkan, ON hinka (*limp', though in view of the Swedish doublet skinka, id. usu. refd. to type kseng-, q.v.); Slovak Ciahat, Ciahnut' ‘seize’; Li. cf. kenge ‘hook’
```


## [2026-09-06T15:55:09.055Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '44506,44556p' POK_full.txt",
 "description": "POK_full keg- entry"
}
```


### [2026-09-06T15:55:09.102Z] TOOL RESULT

```
Root / lemma: keg- keng- and kek-, kenk- 

Meaning: hook, grappling hook, handle 

Note: compare das similar Rak-, Rank-, and Renk-, Ronk- 

Material: Npers. cang^ claw, nail, fist' {*kengo-)\ 

Middle Irish ail-chengi. " rake, weapon rack ' (: Lithuanian kenge, see below); 

Germanic *hakan-, *hdka-, *hekan-rc\. "hook' in: Old Icelandic PN Hakim, 'hook', haka 
f. 'chin'. Old English haca rw. 'bar, bolt', haeccei. ' crosier, crozier, bishop's staff; Old 
Icelandic hakrm. ' Frechling ', Old High German hako, haggo'hook', Old English hocm. 
'hook'. Middle Low German hok, hukvc\. ' angle, point, edge, foreland, promontory ', Old 
Icelandic h0kjai. {*hdkidn-) ' crutch ', h0kill rr\. ' Hinterbug '; with intensive Gemination: 
Old English haccian^hackevi , Middle Low German, Middle High German hacken ds., and 
the/verbs: Old English ofhaeccan^ cut off. Old High German hecchen^bWe, prick'. Middle 
High German hecken'\r\e\N, hit, prick'; nasalized Middle Low German hank' handle, part of 
an object designed to be gripped by the hand ' (out of it Old Icelandic hgnkxu., hankii. ' 
handle, part of an object designed to be gripped by the hand '), Dutch honk. East Frisian 
/7^/7/r' picket, pole, jamb '; 



Germanic *hakildi. ' hackle, heckle ' (from crooked iron teeth) in: asachs. hekilon' 
hechelql', engl. hatchel. Middle High German hecher hackle, heckle ', Norwegian hekia' 
hackle, heckle, stubble, bristle '; 

Germanic *hakuda-xr\. ' pike ' (after den spitzen teeth) in Old English hacod, *hakida\v\ 
Old English hacidxw.. Old High German hachit, hechit. Middle Low German hekeV pike '; 

Lithuanian kenget 'hook, handle '; 

Slavic *kog'btb m. in russ. kogotb ' claw, nail, crooked iron point ', Upper Serbian kocht 
'thorn, sting, prick' (: Germanic *hakuda-); 



Maybe alb. {*k6gotb) kthetra' claw, nail', kthej^ bend, make crooked ' common alb. -g- > - 
th-, -dh-. 

perhaps here, " hang on a hook, scratch, irritate as with a hook ' : Bulgarian kach, 
kac(u)vam' elevate, raise, hang ', za-kact, -kacam' hang, catch, banter', serb. zakac/t/" 
hook, hang ', sloven, kac/t/" banter, anger' (Berneker465 f.). 

Maybe alb. kacavirrem^ clamber, scramble, climb up, cling ' a Bulgarian loanword. 

References: WP. I 382 f., WH. I 307, Trautmann 112, Wissmann Nom. postverb. 182 f., 
Petersson, Heterokl. 91 f.; Stokes BB. 25, 252. 
Page(s): 537-538
```


## [2026-09-06T15:55:11.202Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport io\nt=open('IEC.txt',encoding='utf-8',errors='replace').read()\ni=t.find(\"keng- 'seize, grip\")\nleaf=t.count('\\f',0,i)\nprint('leaf(0-based)',leaf,'=> printed approx',2*(leaf-15),2*(leaf-15)+1)\nprint(t[i-1500:i+900])\nEOF",
 "description": "Locate IEC keng- leaf"
}
```


### [2026-09-06T15:55:12.893Z] TOOL RESULT

```
leaf(0-based) 279 => printed approx 528 529
iù, “ti (5), id. (kel- in Gk. má-kella, dí-kella, see kolið) kelos, is “high; height. Cf. keld (1) and
keleso, and see kels-
Latv. cēls “high, tall, noble, splendid’; Li. cf.
kelis, io, m. ‘rise’; Lat. cf. cilo, -onis (“person
w. large forehead’: OCS čelo “forehead'); ON
cf. hilmir ‘prince’ (all fr. *kel-) kels- (variant of type kel- (1), q. v. and ke-
leso, kelos)
Lat. ex-cello, beside celsus; ON hjalli rock:
shelf; Sw. häll (1) ‘cliff. (ISophonic: ON hjallr
‘dutch barn") kelt- (kolt-) ‘shake, sway’
Skt. cf. catulah ‘unsteady, tremulous’; Srb.
klecam ‘sway’; OCS cf. klasto, klatiti, id. (fr.
*kolt-); Cz. klátit, tr. id.; Lusat. kłóćić, tr.
‘shake down fruit’. (Isophonic: R kolotit
‘beat, thrash’) kem- ‘gather’. Cf. kems-, kmt-
Alb. qem, v. id.; Skt. cf. Camüb, f. “army”;
Latv. kems, m. ‘bunch’ kemelos ‘bumble-bee’. (Variant of kumelos,
q. v.). Cf. WP I, 389
Skt. cf. Camarakah, dim. ‘bee’; Cz. čmel
*bumble-bee', cf. Cemelit se ( ‘swarm’, v.) kemeros, is, å "a plant. WP I, 390
Skt. (dim.) éCamarikah ‘orchid tree’; OHG he-
mera, MHG hemer(e) 'sneezewort'; OCS če-
meri ‘poison’; Srb. čemer ‘bitterness’; Big. čemer, as OCS; Cz. čemer ‘rash, pain, nausea’
beside čemeřice, Cemerka “sneezewort'; R
čemerica ‘hellebore’; Srb. Cemerika, id.; Li.
kemeras, keméras ‘hemp agrimony’; Latv.
kemers (id?) but Camarags 'sneezewort (kems-, variant of type kem-, q. v. Cf. km-, kmst-, kmt-
Li. cf. kemšu, inf. kimšti ‘stuff, cram’; Latv.
kelo, ið — kents-
20
25
30
35
40
45
488
kemsu, kimst ‘plug’)
keng- 'seize, grip, hold; hold, hook, grapple, hobble'. Cf. knk- Av. cf. Caro ‘claw, cleft hoof; Per. Gäng ‘claws, fingers”, cf. also čängāl, čängul ‘claws, hook’; Lat. cingo, Gre “tie; gird” beside cingulum, cingula (LW in Ir. ceangal ‘tying, binding, ceanglaim, v.id., and in W cengl, f. “band; girth; hank’; cenglu “bind'); ON hinkr, n. (delay', fr. *kengro-); Sw. hink, pl. at m. “lever, bascule, well-swipe" (?); cf. also (?) OHG hinkan, ON hinka (*limp', though in view of the Swedish doublet skinka, id. usu. refd. to type kseng-, q.v.); Slovak Ciahat, Ciahnut' ‘seize’; Li. cf. kenge ‘hook’
(kenk- *quake', see next)
kenkolos, kenklos ‘unsteady, hobbling, limp- ing’; radical: kenk- Oss. cànkul ‘crippled; cripple’; Skt. Caficalah ‘wagging, unsteady’, cf. čañkāmi limp, tremble, flicker’; Gk. kégklos ‘wagtail’ beside kígklos, id. and kigklízo “be restless’; MHG hingeln ‘limp, hesitate’; Li.
```


## [2026-09-06T15:55:23.831Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('IEC.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\n# find leaf containing printed 458 -> leaf ~ 458/2+15 = 244\nfor L in range(240,250):\n    seg=pages[L]\n    nums=re.findall(r'^\\s*(\\d{3})\\s*$',seg,re.M)\n    print(L, nums[:6], seg[:80].replace('\\n',' '))\nEOF",
 "description": "Find IEC leaf for printed page 458"
}
```


### [2026-09-06T15:55:25.524Z] TOOL RESULT

```
240 ['415', '416'] v. zeme, beside zem, prp. “under”; zemē ‘below’; zemi, zemu, adv. lowlying' $hen
241 ['417', '418'] nt'; Sw. gása beside Norw. gjære, v. 1d.; gjær ‘barm’; Du. gier, Fris. jarre liq
242 ['419', '420'] ‘jaws’. (Cf. also *&£hiien-, *&hin- in MHG ginen, gënen ‘yawn’; G gienen ‘burst 
243 ['421', '422'] pe’; OCS zinọ, -iti ‘yawn’; Slovene ziniti, id.; Li. cf. Zynýs, io, m., Zyne, f.
244 ['423'] le’. Cf. 2hol- (1) and ĝhel-. WP I, 624 Gk. khólos, kholë, id. cf. s-kholë “free
245 ['424', '425'] y, grain’. Cf. ieu-. WP I, 611 Gk. krithé; Alb. drithé, n. (id. fr. *&hridhst-);
246 ['426', '427']  1-rem. Cf. also itós, itis. The vocalism of Hitt. iyami ‘go’ is uncertain -i, a
247 ['428', '429'] glow’; (un- certainly ong "Drei: OW cf. enn-ynny, W cy- nneu (?) *ignite'; besid
248 ['430', '431'] akah, dim. id.); Lat. canticus (‘song’: can- tus); cf. carrüca, beside carrus “l
249 ['432', '433'] A variant occurs in Li. avíena “mutton”, cf. LLat. ovina, id. As an indicator of
```


## [2026-09-06T15:55:31.657Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('IEC.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor L in range(259,266):\n    seg=pages[L]\n    nums=re.findall(r'^\\s*(\\d{3})\\s*$',seg,re.M)\n    print('---leaf',L, nums[:6])\n    print(seg[:400].replace('\\n',' '))\nEOF",
 "description": "IEC leaves around printed 458"
}
```


### [2026-09-06T15:55:33.645Z] TOOL RESULT

```
---leaf 259 ['450', '451']
�� (correl. to quo- dě, to-dě, etc.) iéuot — iðmå (-is) 20 25 30 35 40 45 450 Skt. yadi ‘if’; OPer. yadiy, id. beside Skt. yadà, Av. yağa ‘when’; Av. yeói, yezi “iP ; Gk. hóde (here, hence; so’; w. prns. such: OE giet, gieta ‘yet, stil; OCS jeda “if” beside jede (w. prns. "euch: OCz. jeda-Z ‘when, whenever lodos, -es- ‘demon, monster’ Skt. yadas, n.; ON Jótr ‘Jute’; Latv. jods; Li. cf. joda (fr. L
---leaf 260 ['452', '453']
b. herë ‘time, fois’; Lat. cf. h-ornus (“of this season or year”, fr. *ho-ior-, cf. ho-die); W cf. ior *eter- nal: ON cf. ent ‘younger’; also (?) oeska (Cchildhood', if. for *ioriska); Srb. jàr ‘heat’; OCz. j&t “spring; spring corn’; Cz. jaro ‘spring’; Blg. jarà ‘reflected glow’; Slovak jar, f. ‘spring’: Slovene jar ‘precocious’; Ukr. jaryj, adj. ‘springtime’; R jarovój summer": jàrka “year- ling 
---leaf 261 ['454', '455']
s, refi. ‘show off; rampage’ ioudhos, see ieudhos iougətos, à (iougto-, iougti-) ‘juncture’. Cf. ieug-, iug- Skt. yogita ‘connexion’; ON eykt, f. *three- hour period, mid-afternoon'; Li. jáugtas *yoke-thong' (ioul-, iout-, see Supt.) iðuå ta) Kees cry’ auer see SS SE inder] jeunos iðus ‘common law, traditional law, right. See ieus, and cf. ieuaið. WP I, 203 ludheið, see iudho iudhlos (1) ‘twaddle,
---leaf 262 ['456', '457']
�, Jústi (start, get moving’, intr.); Latv. junda, f. *reveille'; jundu, ët ‘announce’ iungo, ið, infixed variant of iug-, ieug-, q. v. Join, yoke’. See next Skt. cf. yunájmi, 3s yunákti, 3pl yunjánti, id.; Lat. jungo, ére; Ir. cf. cuing (fyoke', fr. *ko- iung-); Li. jüngiu, ti; Latv. cf. jüudzu, jugt, id. iungos, à ‘coupling, link, join, yoke’. Cf. iug-, leug-, etc. WP I, 202 Skt. cf. á-yungah “o
---leaf 263 ['458', '459']
ontageous'; ka- barotis, kabarúoti, v. ‘hitch’; variant in Gk. ká- blës “bolt of door’ kabl- (kablios) ‘catch, hold’. Cf. kab- (1) Gk. kábles “bolt, bar’; Sw. happla, v. ‘get caught’; Li. kablys, io, m. “hook”; Latv. kablis, id.; Ir. cabhail (and cobhail) (?) ‘enclosure’ kabos “bend, curve, cramp’. See kab- (1) OE hop, OFris. hop, Du. Fris. hoep ‘hoop, band’; ON hóp ‘cove, landlocked bay’; Li. cf.
---leaf 264 ['460', '461']
nt obscure) kaik- (1), kaikos “blind, dim, dark WP I, 328 Skt. cf. kekarah 'squint-eyed'; Lat. caecus ‘blind’; MIr. cáech, adj. “blind, one-eyed, squinting’; Ir. caoch 'dim-sighted'; W coeg, adj. ‘vain’; coeg-ddall “half blind”; Br. (dial.) kuik, OCor. cuic, Cor. cók, coek (*one-eyed'. Cor. also ‘empty, vain"); Go. haihs ‘one-eyed’; Swiss cf. ge-hei ‘nebulous, obscure’; G Hai “fog? kaik- (2) “croa
---leaf 265 ['462', '463']
acify’. See quieio kàios, à “base, pedestal, trunk, stem, stand, leg’. WP I, 362 & 509 Skt. kayah ‘trunk, stem, body’; Arm. kaj, kajk, i-st. ‘seat, position’; kajan, Let lodge"; kajun, adj. ‘stable, firm’; MHG hei, heie, f. (ram- mer, beetle’; G Heie 'paving-ram'; Du. hei, id.; Sw. cf. hajare 'pile-driver'; Li. kója “leg, foot’; Latv. kāja, id. (& “base, stand") kakā (kakk-) ‘excrement’. WP I, 336
```


## [2026-09-06T15:55:40.487Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('IEC.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint(pages[263])\nEOF",
 "description": "Print IEC leaf 263 fully"
}
```


### [2026-09-06T15:55:42.203Z] TOOL RESULT

```
ontageous'; ka- barotis, kabarúoti, v. ‘hitch’; variant in Gk. ká- blës “bolt of door’
kabl- (kablios) ‘catch, hold’. Cf. kab- (1) Gk. kábles “bolt, bar’; Sw. happla, v. ‘get caught’; Li. kablys, io, m. “hook”; Latv. kablis, id.; Ir. cabhail (and cobhail) (?) ‘enclosure’
kabos “bend, curve, cramp’. See kab- (1) OE hop, OFris. hop, Du. Fris. hoep ‘hoop, band’; ON hóp ‘cove, landlocked bay’; Li. cf. kobinys, io ‘hook, boathook"
kad- “evil, hate’. Cf. Kad-. (Oscan and Gmc. ambig.) Skt. kad- cpds. "bad": kadanam ‘destruction’; Av kad-, v. ‘destroy’; Go. hatis, n. ‘hate’; ha- tan, v. id.; OE hatian, OHG haz3én, v. id.; haz, s.; Osc. cad- (“hostility”, gs cadeis)
iuuontos, à — Käg-
K
20
25
30
35
40
458
iuuði-, dual form of iŭs, q.v. Skt. cf. yuvayüh, adj. “for you two’; OCS vaju, va ‘you two”
iuuos, iuues, see ilis, iusmé-
kadlos (?) “hard; hardness'. Cf. kaldhos Lat. (ambig.) callus “hard skin’; callis, f. (*foot- path’, lit? “hard way"); Ir. cadhal ‘skin, bark’; OE cf. hatol ‘odious’; Finn. LW katala, adj. *vile'
kadhis (?) “vessel, container”. Myc. kati- (jug! or sim.); Gk. keéthís *voting- urn’; OCS kadi 'grain-measure; vessel’; Cz. kád' ( barrel". Of ambig. origin, but apparently distinct from the Semitic LW in Gk. kádos ‘pail’; E cade ‘tub’, Srb. káda ‘vat’, Li. kodys, id. Hung. kád, Rum. cadá, with which conta- mination may have taken place). (Isophonic:
OE, OFris. hod ‘hood’: OHG huot; Du. Fris.
hoed "bat, (For the Semit. form cf. Arab. qadh *cup")
kag- (kagol-, kagil-) “hook, claw’. Cf. kagot- and next. Cf. kaĝ- (variant) Sw. haka ‘chin’; hake, wm. “hook, clamp’; MHG cf. hachele, hechele, f. “hackle, hatchel, flax-comb, bristle’; G Hachel “awn, barb’; Hechel 'flax-comb'; E hackles ‘ruff of feath- ers’; long-gde variant in ON hoekil-, cpds. *bent-"; Li. kogaliai, pl. ‘short wool on sheep's legs'
kagot- (extn. of kag-, q. v.) “hook, barb, claw; barbed creature'. OHG hahhit, OS hact, OE hacod, MHG he- chet ‘pike’ fish; R kogoti, m. “claw?
kag- (variant of type kag-, q.v.) (1) “bend, angle, hook; bent”. (Gmc. ambig.) Per. kaj (-E) “bent? OE haca, wm. ‘hook’; OS hako, id.; Du. hak “heel, hock’; G (fr. LG) Hacken, id.; LG heck “pike? fish; ON. Sw. haka ‘chin? beside Sw. hake, wn. ‘hook, clamp’; Pol. cf. koz-ula 'fish-hook', beside
 
459
koz-ub ‘hawk’. Long-gde in Ir. cág “handle, shaft; OE hoc, Du. hoek "book angle, cor- ner’; ON hoekja ‘crutch’
käg- (2) ‘goat, kid; goatskin’. WP I, 336. See kaĝəl- Hes. cf. kássos ‘greatcoat’; kássas, pl. ‘sha- brack’; kás ‘skin’ beside Mod. Gk. katsíka ‘goat’; katsiki ‘kid’; Alb. kedh ‘kid’; OE hecen, n. ‘kid’: LG hæken, id. (fr. *kāĝion-);, MHG (*-a-) hache Clad fig. use of ‘kid’, LW in Cz. hoch, id.); OCS (and com. S1.) koza ‘goat’ beside koža (“skin, pelť, an adjectival type); LW in Latv. kaza ‘goat
kā (3) “beat, strike? (?) Lat. caia, f. ‘lash’; caiare, v. inf. id.; MHG hacken, v. ‘hack’; OE haccian, id.
kagol- ‘goat, kid; goatskin’. See kà$- (2) Mir cadla (fgoat'; dl- for *gl- as in dlúth- fr. *elüt-, cf. however Alemannic Hatle 'she- goat"); Go. hakuls ‘cloak’; OE hacele, hacule, id.; ON hokull, ds hokli, id. beside hekla ‘cape’; MHG hechel ('slut, procuress'; fig. use of ‘goat’); OCS kozilü 'goat'; kozile “kid?
kai-, modal fragment: “alone, separate; only, but, yet’. Cf. kaikos, kailos (2) Skt. cf. ké-valah “alone, separate'; Arm. cf. kes (‘half ? if for a type *kai-K-. For the semantic parallel cf. *sé- "apart: *semi ‘by parting’ hence ‘half. See sémi); Gk. kaí and Lat. cf. caedo, ére, v. eut, lit. ‘separate’? ambiguously to OCS céZdo, céditi ‘sift? etc., which is pre- ferably to skoid-, q. v.); cf. Lat. cael-ebs (see „ail- below); synth. cpd. in OCS cé-glü (“alone”). Second eleme
```


## [2026-09-06T15:55:52.690Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== syava ===\" && grep -n \"syäva\\|syāva\\|syava\" BRT.txt | head -20; echo \"=== 1631 ===\" && grep -n \"^ *1631 *$\\|1631\" BRT.txt | head",
 "description": "Grep Bartholomae for syava"
}
```


## [2026-09-06T15:55:53.309Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== cang avestan? ===\" && grep -n -i \"cang\\|čang\\|canga\" BRT.txt | head -20",
 "description": "Grep Bartholomae for cang"
}
```


### [2026-09-06T15:55:54.295Z] TOOL RESULT

```
=== syava ===
3097:•  j.  a;'rae'ra9^-  m.  EN.  eines  Gläubigen, eines  Bruders  Franrasyan%:  "'^aAe  nara- vahe  alaonö  Yt/^.  131;  —  puirS  kaoia (sd.)  syävarsänai  .  .  ""^ake^a  naravaht ".  .  und  (als  Rächer  des  Ä. . ."  YLf?.i8,
7000:iar>t-,  Aas-,  gam-,  sta-  usw.).  Ä)  bei Ellipse  des  Verbums:  maxdascä  ahuratahs i7'9'  *i/iSyastra.baratia  isi.)  asacä  Y.30.9. Unklar:  Vyt.  j«?3  FrW.Äi.  [Y.25.9: lies  y^ma;  s.  '««;  —  Y.43.Z:  liesyava/a; ^F.4c:  lies ys;  —  F. .¥ 2St:  lies  soa;  — N.^:  lies  a>a;  sd  No.  3;  —  K  04:  lies yezi  aat;  —  P-Jp;  lies  anitti/i/a.]
7238:kant;  kas;  gam-,  sta-  usw.).  A)  bei Ellipse  des  Verbums:  mazdhs^a  aAurhnhd j'9)  *tiigyastr3.barana(sd.)  asäcä  Y.J0.9. Unklar:  Vyt./.?J,  FrW.Äi.  [Y.2p.9; lies  ySma;  s.  'ma;  —  Y.  43.Z:  Utsyavala; —  F. 4c:  lies^-d;  — F.^aSt:  liesäÖa; — KS:  lies  a>a;  sd.  No.  2;  —  ii.04:  lies yasi  3a/;  —  F-Jp:  lies  arpüitnca.]
9128:kaTucS  vlltaspö  Y.^j.a;  —  iava  vistiispö Ytj.  io8  usw.5>;  —  kavaitn  kaviltim  Yt IQ-Ti  usw.»;  —  iavöii  aipivai^A)us  \t. Ij.i3^  nsv/ß;  —  kai'aSm  usaöaium  Vt. 1(^-71  usw.**;  —  kti7-a  usa  VLJ.4S  usw.; —  iavdis  arsnö  Vt.  13.132  usw.** ;  —  iarms fisinaulß  Vt  JJ.  13z  usw.";  —  kavöis byarsiinS  Vt;_j.  132  usw. 5';  —  iavaim syävarsämm  Vt. /fj.?!  usw.*';  —  kavoU haosravaijhahe  Ny.  5.  5  usw. 5';  —  yat baun  Vispe  *d,iri'i.Aaire  kai'c  (NF.)  Vi.  /(?. 71*'.  2)  jAw,  Name  für  gewisse  Feinde des  Volks  und  Glaubens  der  Masdayasn^T: vTspamitn  tbihatqm  tbuuiii  diUvunam  mai- yänamra  y'f'ircum  pairikannmi'a  sä^rmii iaoyiim  {Gl'.)    'iara/nami'a 'Y.  (/■  tS;    Vt.
18675:elliptisch  sva,  'ein  Mann  und  ein  Weib,  ein Menschenpaar"**:  dvaübya  haca  n)r>bya dva  nara  us^ayein/e (sd.)  t//i^wa/ia  s/ri^a nairyas^a  V.2.41.  2) '•  praegn. 'wehr- hafter Mann,  Kriegsmann;  kriegerischer Held':  narSi  ßrasaoifträi  Y.  28.  8;  — katna  (sd.)  syävarsänai  zurSjatahe  na- rahe''*  Yt*j.  18;  — pqsnus  narJ  (NS.)'^ HryS  taxmS  Aog.  84;  — y^i  narS  taxma ptntmU  Yt./J  27;  —  t! nard paiti.sanmti ySkva  v3r3%ra.l'aohl!  {sd.)  YtJ_j.  46;  — yat  mS  slärS  .  .  AacÜnte  (sd.)  n?r>byS ä^annff  *bax/3nia  Yt- 8.  1 ;  5.11,  77.6,7; das/a  narqm  *pouru.tät?m  stäkyanqm.. vanatqm  avammnanqm  Ny. J.  10;  —  hva- iai  naire  barumnäi  Y.  65.  4;  — yä  na- qm  vjg3r>pla{sd.yit . .  baoxtär^m  dahäi/i Vr.7,3;  Yt  10.12;  —  ya^a  hazannm Oim  narftn  adar.taySi^  Yt.  8.  $$; I.  19*;  —  a%ra  narqtn  mihrS.drujqtn apq/{sd.)  gavB  dar>tayeiti  Yt70. 48;  — narqm  asätanqm  frasS.car^'hrqm  saosyan- tqm  Y.  24.  5,  Yt.  13. 17.  a)  als  Bezeich- nung für  den  zweiten  Stand  (s.  'piflra-) 'Krieger,  Ritter***:  kada  .  .  mquarfi/ (sd.) rS  vis3nliY.48.  10;  — daidx atturai (AP.)  ,  .  asaunS  .  .  aidyüi  väsliyJng  ,  . ahmaibyä  ahma.rafonarahs  {^d^  Y.40.3; %wqm  ttarakl  ysi  taxma  Jathyintt äsu.aspim  .  .  %wqm  a^ravanS  .  .  mastim Yt5.  86.  3)''  ohne  Betonung  des  Ge- schlechts sva.  Mensch;  Person';  1)  im Gegensatz  zum  Tier;  uzw.  zu  a)  pasav-: ahe  nmanaßie pasvqmca  narqntla  Y.^-S; pasBm  .  .  nanm  ra?syät  V,  13.  32 b)  'span-.  . .  ahe  nmanake  spä  vä na  va  irihyat  V.5, 39;  8. 1,  4;  —  yat ahmi  spänasca  narasca  para.irüinti  V. 6.1; — y!i  pa^a  uebarmte  (^)  spänasca irista  iiarawca  (NF.)"  irisia  V.  Ä  14; 3.  32;  —  yat  ,  .  sairi  riiianie  spänasca irista  naraila  (AP.)'*  irista  V.  3.  8; 36.  c)   ^av-:  janyäi  *n>rSuI^'*  para
27187:—  Vgl.  säma-  und  zu  »syäva-,
27188:"  j.  syäva-  Adj.  'schwarz'.
27192:•  j,  syävaspi-  m,  EN.  eines  Gläubigen: */»V"  asaonS  Yt. /_J.  114.
28220:•  j.  zürö.jata-  Adj.  'unrechtmässig,  ver- räterisch getötet*;  syävariami  (sd-,  Dat statt  Gen.)  -take  narake  Ytp,  18;  —  yat aae  ya  sfS.jata{^:)ca  .  .  'iala  V.  7.  3.
28616:—  dainayii  vanhuyai  yam  hsi  isyam  (sd.) datB  . .  masdä  alahya  äzdyai  (sd.)  gimdlm Y.5J.  17;  —  das  Nomen  ist  nicht  genannt, aber  durch  den  Zusammenhang  hinreichend deutlich:  kadsyava  AvB  aaAaf  {Sp.  369  0.) yS  Affi  (näml.  gavSi)  dadat  tastaz/at  (sd.) avSY.2g.  9.  2)  auf  ein  Nomen  voraus- weisend:  al^  hsi  (mask.;  zu  a)  scaniu ..  xsttüm  (sd.)  mazdä  vahmät  a  Y.  55.  2;
=== 1631 ===
27180:1631
```


### [2026-09-06T15:55:54.347Z] TOOL RESULT

```
=== cang avestan? ===
```


## [2026-09-06T15:55:59.771Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '27175,27200p' BRT.txt; echo \"=== sama ===\"; grep -n \"säma-\\|1571\" BRT.txt | head -20",
 "description": "BRT syava context and sama"
}
```


### [2026-09-06T15:55:59.849Z] TOOL RESULT

```
es  pazday'  hiesse,  sd.
•  g.  syazda-  Praes.  18  a  'zurück- weichen'.
mit  Abi.  'vor  — ':  ySi  , .  armaitlm  . . b>nxtqm  (sd.)  . ,  avatatai  . .  alifye  mai' ala  syazdai  yava^  ahmat  aurunH  xrafstra ".  .  vor  denen  weicht  Asa  gar  sehr  zu- rück, so  weit  als  vor  uns  die  wilden  Raub- tiere" Y,j4.  9.
Vgl.  lu  liläya-.  —  Pü.:  hal  Siän  vat  ahräkih
ob,Google
1631
syämaka-
163a
+nli/ (Ttaiuskr.)'),  SQ.:  ttbhyo  fnAhüta  ähar- mak  prabhraiyati.  —  ■)  Vgl.  zu  iildyamni  Y.
•  j.  syämalia-  m.  Name  eines  Bergs oder  Gebirgs*':  akmai  haca  garayS  frao- xSyqn  . .  'kasla  va/rayäs{^ya  Yt.  ig.  5.    j
*l  Der  Bd.  12.  3  syäinioimand  ('mit  schwarzen  | lliaren'),  12.  32  sy��tömand  genuint  wird.  S. im  Cbrißen  Sp.  1347  o.
ai.  fyäniaia-  Adj.  (auchEN.);  ai.  iyämä-  Adj.
—  Vgl.  säma-  und  zu  »syäva-,
"  j.  syäva-  Adj.  'schwarz'.
KompA.  —  ai.  fyävä-  Adj.  'scttwarzbraun', np.  siyäh  'scbwaiz';  weiteres  bei  Hbm.  AGr. /.  489,  IFAnz.  to-  zq.  —  S.  noch  Sävaiaii iliyih.  EN.  (=aL  iySvaka-  m.  EN.).  gebildet wie  syämaka:
•  j.  syivaräan-  m.  EN.  eines  iranischen Fürsten  aus  der  Aaz'd^ynastle,  Urenkels At%  Kavata,  Vaters  Acs  Haosravah- (?,&^: haosrava  . .  pu%rd  katna  (sd.)  '/änäi'^ (statt  Gen.)  sürS.jatcihe  narahe  Yt.5. 18; ' —  kavaim  'farDm  Yt.  15. 71;  —  kavSii •iafflJ  asttPnS  Yt  y.  133,  Ai.^.
Komp. :  'iy5va-\-atiatf  (S  268.  3  b),  eig.  'der Rappbengsle  besitzt'.  —  >)  Them.
•  j,  syävaspi-  m,  EN.  eines  Gläubigen: */»V"  asaonS  Yt. /_J.  114.
Komp.:  iyäva--\-aspI-  {%  368.  3),  eig.  "Rapp- stuten  besitzend'').  —  ■)  Nach  der >-Delcl., YgL  oTjäraosIrl-,  daufrämatsi- .  —  ')  Ein  patr. Adj.  -  JUSTI  NB.  300,  GUBLSR  Patronymica [Baseler  Diss.  1903]  67  -  ist  nicht  am  Platz, j.  syötdim  '^.  48.  T:  lies  syödüm;  %.  sS:
•  j.  (svar-) :  sor-  n.  'Morgen,  Morgen- frühe', nur  AS.  sßnm'^  als  Adv.  'früh- morgens': mtäsnm  . .  yS  paoiril  voHäis (sd.)  *nm  frälaiÜ  Yt  10. 143.
KompE.;  Ableil.  —  Vgl.  imiakT-.  —  ai.  h/äi (LS.  als)  Adv.  'cfm'«).  —  lEL  s.  IFAnz.  t2. 27.  _  1)  Them.;  die  Bildung  kann  durch bedeutungsverwandCe  Zeitadverbien  -  vgL  ai. HÖilam,  Jofim,  säydm  -  veranlasst  sein.  — ')  Allerdings  wird  ja  ai.  hiäh  in  SandAiA  be- handelt, als  wäre  as  der  ar.  Ausgang;  doch s.  dazu  Wn.  AiGr.  i.  334,
•  j.  sraeS-  V.  '(sich)  heften',  Praes.  3 trUa;  17  (Fut)  srai^a-.  —  Absol.  sral- iyäntim.
1)  'haftenaß-' (Dat):  nSi^ *Ai/iu (sd.) iiiivsi  sraiiyäti  "Trocknes  wird  nicht  an Trocknern  haften"  V.  8. 34.  2)  'sich heften  an  -  (Akk.)  sva.  nachgehen,  ver- folgen'; yö , .  hala  gaiisabyS  paraiti  srai- hmns^^  tayol  v)hrk)mca  "wer ..  weggeht in  der  Absicht  die  Diebe  oder  den  Wolf zu  verfolgen"  V.  13. 1 7.
mit  Aam  'zusammenheften,  -binden':  yB I  bansma  ham^rüäiti  kam  vä  dantayeiti N.jp;  —  yff  bansma  *a^ahmSf  nalm3t '  iam.srifäili  Vi.  gg.
ai.  triiat,  iletfyaä  (G
Pfl.  (zu   V.  S) :  falinjün,
=== sama ===
26182:1571
26185:•  j.  'säma-  Adj.  'schwarz':  aspahe  k»hrpa auruÜake  (sd.)  . .  aspahe  kikrpa  *mahe  Yt. £18   uod   31.
26187:•  j.  'säma-  Adj.  Name  einer  iranischen Familie;    ^rilff  'manqm   snüts  Y.g.  10;
27187:—  Vgl.  säma-  und  zu  »syäva-,
28086:AbleiL  aus  "säma-  m.,  svl.  ajmälat-;  afy. lümt).  iSulT.  (ar.  ?I3.)  und  iKed.  s.  tüitya-, itülmya-  und  WH.'Or.'  %  2228c.  —  I'ö.: äämät  'Schwiegersohn'.  —  ■)  D.  i.  'zäniai/ya; %  36S.  13.  Die  Hdss.  haben  i  statt  y.  — ')  Das  nicht  mit  Ggr.  ABayrAW.  20.  t.  194 gleich  j.  ämälar-,  np.  dämäd  gesetzt  werden kann;    dafür  wäre  *:ümör  zu  erwarten,    vgl.
```


## [2026-09-06T15:56:22.276Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('HRN.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor leaf in (189,190,191):\n    print('==== leaf',leaf,'printed p.',leaf-21,'====')\n    print(t[leaf][:2600])\nEOF",
 "description": "Horn pages 168-170"
}
```


### [2026-09-06T15:56:24.186Z] TOOL RESULT

```
==== leaf 189 printed p. 168 ====
— 168 —
kiird. LW. sl; idy, dre; wa/. tral, sangl. trdl, ya/n.
OeraT, miuj. sardi, sar haröi, si/n. arrai,
760. st 'dreissig'.
aw. drisatent 'dreissig; phlv. sih, päz. si\ ai. trincdt.
kurd. LW. s7; af/. der6\
761. siyah *scliwarz', sit/dhi.
Semn. suah.
aw. st/äva- 'schwarz' in SyävarsCmU'y Syäiaspi-;
phlv. siyak, siyäh (PPGrl.), raand. LW. N"'1N''D ; ai.
Qyävd' 'braun, schwarzbraun'; arm. LW. ^) seao
'schwarz'.
kurd. bei. (348) LW. siyäh 'schwarz ; oss. saa (222);
wa/. sü, sangl. s6L
Als Grundform von . np. siyäh ist *syaoaka' anzu-
setzen.
762. sex (i'^i^iit auf be/^), Sa di, Gul. 46 Zeile 5 v. u., Spr.)
*Bratspiess'.
skr. gikha- 'Spitze (eines Pfeiles etc.)', vergl. cekh-
ara- (?).
kurd. stx^^ si/ü *Lunte* ; bei. slh^ sl *Bratspiess, Lad-
stock' (344).
763. si^deh 'dreizehn*.
aw. dridasa 'dreizehnter'; phlv. sicdahum^) (päz. seS,
sez"); ai. trdyödasa,
kurd. dausCf slzdeh (LW.); afy. dyärlas.
np. sizdeh ist eine Analogiebildung.
764. s~ui% 'Kummet'*).
aw. sima^ vergl. siimiSra- yt. 10, 125 (Geldner,
KZ. 25, 530 Note 200); ai. cdmyä- 'Jochbalken
(nach Geldner; PW. hat 'Zapfen, Holznagel, Keil,
1) Nach Nöldeke bei Hübsohmann, KZ. 23, 402.
^) In E^snadäsa^s Pärasiprakäga aus Akbar^s Zeit findet sich nur
{Mia- (No. 723), wie die heutige indische Aussprache lautet.
*) Vergl. Seite 128 Note 6.
^) Ich vermag mir nach der bei Vullers abgedruckten persischen
Erklärung keine rechte Vorstellung über die Verwendung des sim zu
machen, doch scheint es unserem 'Kummet* nahe zu kommen.
==== leaf 190 printed p. 169 ====
— 169 —
Stützhülz (am Joch)'); arm. .sami\/v 'Stirnliolz des
Ochsenjoches (de Lagarde, No. 19:^8) i).
Xp. sim *Silber , sitnm 'silbern' (phlv. usltn, astnnn)
dagegen ist bekanntlich griechisches Lehnwort (vergl.
zuletzt Nöldeke, Pers. Stud. II, 45).
765. sl/inury 'Greif, Adler; N. pr.', vergl. STn\duxt,
aw. saenö mereyö- *Adler' ; phlv. stnmuro, seiw murük
(Yätkrtr-r Zar. S. ()4).
ai. ^ijefui' Talke*; arm. ein milvus (H. No. 280).
S,
766. Süx 'Zweig, Ast; Hörn (des Stieres), Greweih'.
ai. rdkhä' 'Zw^eig, Ast*; phlv. säk (West 111, 118
Note 1), natak]sak (Bund.) d. i. säx; arm. cu/ (H.
No. 279); lit. szakfi.
LW. kurd. säy; aty. ^ä/; bei. mh 'Hörn, afrt/ 'Ast*;
wa;K. soZ/, sar. so^ 'Zweig', wa;!r. mo, sar. xdo 'Geweih'.
Vergl. zuletzt Bartholomae, Studien II, 41 folgg.
767. Häd 'fröhlich, heiter , sadt,
ap. siyäti- 'Behagen, Freude*^); aw. säiti-; phlv. sät,
sätlh; lat. vergl. quietus, quies.
088. äncad 'Stille', d. ancayim, t. ancain *ruhen* (24).
768. Hiiiu 'Abendmahlzeit, Nachtessen*.
aw. x^^f^W^'"'» phlv. säm (y. 61 (19) = 62, 7).
LW. kurd. säm *Abend'; af;^. süme Zeit zwischen
Mitternacht und Tagesanbruch; Nachtessen, Leichen-
schmaus', mä\xäm 'Abend' (?); bei. säm 'Hauptmahlzeit,
Abendessen* (259); sar. /?/w, yidg. säm.
') Nichts wesentlich Neues bringt Bugge, KZ. H2, 24.
Als Betonung von aw. simä" muss natürlich oxytonale angenommen
werden. Das Wort ist mit den von Bartholomae, BB. XVII, 114 folg.
gesammelten zusammen zu beurtheilen.
*) Und wohl auch zugleich *Wohnstätte*, vergl. Bartholomae,
Arische Forschungen, II, 102.
==== leaf 191 printed p. 170 ====
— 170 -
Die Ableitung von np. Mm aus aw. ysäfniya-
(üarniesteter, Et. ir. I, 82, II, 161) ist sehr an-
sprechend, wennschon mir eine Grundform ^/sampHya-
nicht wahrscheinlich ist. Bei einer so starken Con-
traction konnte auch schliesslich der auslautende Nasal
noch in Mitleidenschaft gezogen werden, vergl. np.
Behräm gegenüber Varahrän; g. cum bei Beresine,
II, 24, VIII, 1 ist gewiss erst sekundär wie cübän
statt sübän (No. 776).
769. San 'ihr (Enclit.).
ap. sam (Enclit.) ; phlv. -^dn,
770. sdnzdeh sechzehn'.
aw. /svasjlasa 'sechzehnter ; phlv. säncdahiim ^).
af/. späras ; kurd. LW. säfizdeh,
np. sänzdeh ist durch das ihm vorhergehende pämdeh
beeinflusst.
771. smie 'Kamm'.
Käs. K. yö\sen (?).
phlv. sänak 'Kamm' (AV.); gr. xrf4', icrivinv (Hesych),
indog. he-n (Hübschmann, ZDMG. 44, 560).
bei. sak *Kamm' (445), dagegen LW. sänug 'Pferde-
strieger (866).
772. sah 'König, Herrscher, sähäne, sälü, sähin 'Falke'-).
ap. /ßäyadiya- 'Herrscher; päz. sah (PPGL), ^syäv
aaa, Ksoiiavöad (Agathias 261, 5, 264, 1).
Allgemein entlehnt (meist mit der speciellen Be-
deutung 'Perserkönig), wie auch säht (z. B. oss. d. sai
'Fünfkopekenstück', bei. säht 'Zweiannastück' (256);
dagegen in der Bedeutung *Landstrasse' in skr. säht,
Weber, Monatsber. BAW. 1879, 812).
778. sähensfih 'König der Könige'.
ap. yßäyad iyänäm ysäyadiya *der Könige König',
Vergl. Seite 128 Note 6.
^) * Sähen ^ vorgl. arm. LW. .^aJien.
```


## [2026-09-06T15:56:42.563Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(len(t))\nfor leaf in (121,122,123):\n    seg=t[leaf]\n    print('==== leaf',leaf,'====')\n    print(seg[:1500])\nEOF",
 "description": "BQT vol2 leaf ~122 (p.665)"
}
```


### [2026-09-06T15:56:44.340Z] TOOL RESULT

```
684
==== leaf 121 ====
 ‫چند اول‬                                                                                 ‫‪۳‬‬
                                          ‫ات ؟ ‪.‬‬       ‫انداز ند ‪ -‬و چوبی که گازران بر جامه زنلد ‪-‬‬
‫بروزن فند » مقدار غیرمعین‬        ‫چند ‪°‬‬                 ‫و چوبدستی که شتربانان و امثال ابشان بدست‬
‫آم مقدارست کمتر از ده‬            ‫باشد کاک‬              ‫یر ندو‪-‬چوب‌خوشةانگو ر که‌برتاك چسبیدء(‪)۱‬‬
‫وغبر معین ‪ -‬و بمعنی هرچند وهرچه لیزآمده‬               ‫است ‪ --‬و کنانه ازمردم ناهه‌وار و درشت باشد ؛‬

‫است ‪ -‬وگاهی‌بجای لفظ تا یکی و تاکی هم‬                                         ‫و بفتح اول آمده است‬
                   ‫استعمالم کنندا ‪. ۰۷‬‬                 ‫= بضم اول بروزن جنبیدن‪",‬‬     ‫چنییدن‬
                                                        ‫بمعنی جستن وخیز کردن گ‪-‬رویختن باشد ‪.‬‬
 ‫که نجاستها و پلیدیپا را پاك کند واو را سربی‬
           ‫کنای ودرهند حلال خروگونند ‪. ۸‬‬
                                                       ‫چنچو لی ج‪-‬بیام فارسی بروزن‬
                                                       ‫مقبولی؛ بمعتی بادییچ اس ‪ ۳۰.2‬وآن رسمالی‬
 ‫جند‌آن ه بروزن دندان » چوب صندیل‬                      ‫باشد که در ایام عید و نوروز از شاخ درخت‬
   ‫راهزای‬  ‫که‬
            ‫شره‬‫بز‬    ‫سمت‬ ‫‪-‬وتا‬
                            ‫ر‬‫ه ‪٩‬‏‬
                                ‫شوبند‬
                                    ‫راک‬                ‫و جاهای بلند آویزند و زنان کوودکان بر آن‬
 ‫‪-‬اری باشد مجهول و غیر معین ‪-‬‬  ‫چوینم*قد‬            
==== leaf 122 ====
  ‫‪-‬‬    ‫وا‬                                                                                         ‫چندر‬

‫چندی ‪ » ۲‬بنتماول بر وزن لندی ‪۰‬‬                        ‫چندر؟ ا=وبلم‌بروزن کندر‪ .‬مخفف‬
‫بممنی چند استکه مقدار مجپول غير معین‬                       ‫چفندر باشد کهحوبجی است معروف ‪۰‬‬
                                                     ‫چند قنك بنتح فابروزن چشمبند‪.‬‬
‫چنغوت ‏‪ ۰ ٩‬با غین نقطه داروفوفانی‬                                      ‫ترس وميم ‪ -‬ولهیب را گویند ‪.‬‬
 ‫بروزن مربوط» پشم‌وینبه باشد که درنهالیولحاف‬         ‫و معنی صندل است‬            ‫حندل = بورزن‬
                          ‫‪.‬‬     ‫نند‬
                                  ‫نآ‬‫کثال‬
                                       ‫وبالگی وام‬     ‫که چوب خوشبوی معروف باشد‪ .‬وصندلءمرب‬
      ‫کنیوون‬
           ‫سح ثا‬
               ‫جنك ‪ -‬بم اول و فت‬                                                           ‫؟ ‪.‬‬    ‫آانست‬
            ‫‪۲‬‬                 ‫کف تازی و‬

‫چنگه » بفتح اول و سکون الی وکاف‬
 ‫‪-‬طولق‬
     ‫فارسی ‪ ۰‬منحنی و ممیده را گوبند م‬
‫قلاب باشدعموماً ‪- ٩‬‏ وقلابی که بدان‌فیل رانند‬
                              ‫خصوصاً و آنرا كجك‬                                    ‫خیرازصندل ‪ - ۴‬وآن‬
                              ‫نیز گوبند ‪ -‬و پنجه‬                                    ‫چوب‌درولاتی‌میشود که‬
                              ‫و انگشتان مردم*‪- ۱‬‬                                    ‫آن ولات را زره ‪6‬‬
                         ‫وچنگال‌مرغان وجانوران‬              
==== leaf 123 ====
                                                                                       ‫و‬
‫بخاای هله دار‬      ‫چنگا لخو ست ‪۷‬‬                 ‫شتمل بر‬
                                                       ‫اممت‬       ‫انیی‬
                                                                     ‫نکیفزنه‌اند ‪۱‬ک‪,‬تو آ‬
 ‫مفتوح و واو معدوله وسیز بی‌شطه وتای قرشت‬        ‫صنایم وبدایع نقاشی ومصوری او‪ -‬ومردم شل را‬
‫ساکن » بمعنی دوبم چنگال امت که نان کرم‬           ‫نکیوزبند » وآن شخصی بودکه دست ویای او‬
  ‫‪-‬ه‬
   ‫وروغن وشیرینی درهم مالیده شده‌باشد ‪ ۸‬و‬        ‫ازکاربازمانده باشد‪ -‬وم‌اول بمعنی‌سخن و گفتار‬
  ‫چیزی‌را نکیزوبن دکه درحم مالیده باشند ‪٩‬‏ ‪.‬‬      ‫است ‪ -‬وبرچیدن مرغ‌دانه را آززمین ‪ -‬و کشتی‬
 ‫چنگال خوش ‪ ۱۰‬بائین قرعت »‬                        ‫وجهاز بز رکه را یز گوبند ‪ -‬وبکراول بمعنی‬
                                                 ‫منقارمرغان‪ -‬کوکنسونان‌وییکان و امثالآن‌باشد‪.‬‬
                      ‫‪4.‬‬   ‫چ زکه درهم مالند‬      ‫جنگاد ؟ بروزن زنگار‪ ,‬خرچنکه را‬
                                                              ‫گویند » وبعربی سرطان خوانند ‪.‬‬
 ‫چنگدو = بادال|بجد بروزن جنگهجوء‬
                ‫در ملك چين ‪# .‬‬      ‫نام شهرست‬
                                                  ‫جنگال = بروزن پرگال؛ پنجهٌ مردم‬
                                                     ‫کہ‬                  ‫وجادوران دیکرباشد‪-۴‬‬
 ‫چنگش = بکر اول و کاف فارسی‬                                                            ‫و ت‬
```


## [2026-09-06T15:56:55.473Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split(chr(12))\nprint(t[122][1400:4000])\n\"",
 "description": "BQT leaf 122 rest"
}
```


### [2026-09-06T15:56:57.291Z] TOOL RESULT

```
                 ‫آن ولات را زره ‪6‬‬
                         ‫وچنگال‌مرغان وجانوران‬                                      ‫میگوبند بکمر زای‬
                          ‫ونام‌سازست‬    ‫دیگرباشد ‏‬      ‫(صندل)‬    ‫جندن‬           ‫تقطه دار و رای می نقطه ‪۴‬‬

                              ‫مشهور‪-٩۱‬‏ ودگارخانة‬    ‫است‬   ‫یدعدی جرف‬         ‫بروزن‌خنده‪.‬‬   ‫۾‬   ‫یف‬


         ‫چنگه‬                 ‫مانی و ارتنگه را‬                           ‫‪.‬‬    ‫باشد ‪۷‬‬   ‫که مقدار غیرمعین‬



 ‫‪ = ۴‬چندل‪ ,‬ازقدیم از‬                ‫‪ _ ۴‬رك‪ :‬چندن ‪.‬‬         ‫‪ - ۱‬رکه‪ :‬چنندر‪ .‬چگندر ‪.‬‬
  ‫‪٤۷:‬‏ «فاب ‪ ۳۲ :۱‬ح؟ ررسالسکریت‬
                              ‫هندی وارد فارسی‌شده و معرب آن‌سندل است « اسفا ‪ ۱‬ص‬
  ‫مصفله» « وبلیامز ‪٩۸۳‬‏ ‪ .»۳:‬چندل (صندل) بیشتر محتمل امت که در آسیای غربی از هند‬
   ‫واردشده باشد(فارسی چندان » چندل » ارمنی ‪ 1200126‬؛عربی صندل از سان کرب‪6‬ت‪28۳3002‬‬
 ‫‪ ۴‬چندن » صندل بود » ءمجدی(مروزی) گوید ‪:‬‬                         ‫» ‪ ۲. 255.‬و ‪oniS( - 26182۳1‬‏‬
         ‫چندان که توان زعود وازچندن»‬         ‫بفروز و سوز پیش خوش امشب‬
  ‫«لفت فرس ‪ ۰۹۳‬و ر کے ‪ :‬همان کتاب ‪» ۳۳۳‬کوكر‪ :‬لك ‪ ۲‬ص ‪ :۳۸۳‬صندل» ور کك ‪ :‬خرده‬
 ‫‪ - ۱‬از ‪ :‬چندل و‬         ‫زره سستان امت ‪ .‬رکه‪ :‬زره‪.‬‬ ‫‪۵‬‬             ‫اوستا ‪ ۹۳۱‬و‪۲6۱۰‬‬
  ‫‪ - ¥‬پهلوی ‪« 110026‬منای ‪۰۷۲۰‬؛ ( بباای‬        ‫(یسوند) ‪ .‬رک ‪ :‬فرهنك دساتیر ‪. ۳۸۲‬‬
  ‫مصدری) کمیت ‪« :‬کیفیت بود چون چگونگی چیزها و کیت بود چرن چندی‪ «»:‬کشف‌المحجوب‬
 ‫را‬    ‫‪:‬اچندی برین آمد لعلف طبض‬
                              ‫چذدی (بابای نکره) سنی چند روزی » مدثی «‬                       ‫سستأنی ‪۷۱‬‬
                ‫(لملف طبع دوست سعدی را) بدیدند و حسن تدببرش را بیسندیدند ‪« ۰.‬کلستان ‪- ۷۳۰‬‬
 ‫‪٩‬‏ ‪ -‬رک‪ :‬چنگك (بهمن معنی)‪.‬‬                  ‫وت ‪۰‬‬  ‫ض»‬  ‫چفنت‬
                                                          ‫ر_ک ‪ :‬چ‬ ‫‪۸‬‬
  ‫)‪ :‬جنگال‪.‬‬  ‫کهک‬‫رنج‬
                  ‫‪ -۶‬استی ‪( 8186‬مازو) دک ‪ .‬است ‪ ۵۱۱6۰‬گیلکی ‪( 80۳36‬پ‬
                                                     ‫‪ - ۱‬پهلوی ‪« 8720‬اووالا ‪: ۱16۰‬‬
         ‫نشنود آواز دف وچنت ونی‪.‬‬                             ‫ش نواند که همه عمر وی‬
  ‫«دکلتان ‪.*4۲۱‬‬
```


## [2026-09-06T15:57:04.973Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor leaf in (655,656,657):\n    print('==== leaf',leaf,'p~',leaf+543,'====')\n    print(t[leaf][:1800])\nEOF",
 "description": "BQT p.1199 siyah"
}
```


### [2026-09-06T15:57:06.788Z] TOOL RESULT

```
==== leaf 655 p~ 1198 ====
                                                                                          ‫اس‬

‫ساکن بوده وهتند» ومغانآ لجا راازجملفاما کن‬            ‫فارسی_ بتحتالی‬     ‫سو گی ‪- ۱‬کبااف‬
‫مدانته اند چنانکه قم بدان یلو‬           ‫که‬
                                         ‫مرتب‬
                                                      ‫کشیده ‪ .‬بمعنی سوگوار استت که مانم زده‬
‫مبکرده‌اند ‪ - ۴‬و لوعی ازدوایی همهت وآرا‬                                            ‫راندوهگن باشد‪.‬‬
 ‫ازجالب رآوومرند‪ ۰‬لقوه را باقع است ‪- ۵9‬وبلنت‬
 ‫بونانی دپایمفمبرست از بانسیرائیل ‪- ۷‬‬                 ‫بت اول و سکون الی بروزن‬            ‫سول‬
‫ویمعنی بام خانه هم هت ومطلق‌بلندیها را نیز‬            ‫غبوملع"نی دوم سور است که رنگ خاکستری‬
                                      ‫گوند ‪.‬‬          ‫بسیاهی مابل باشد مراسب و استر خورالاغی را‬
                                                      ‫که خط سیاهی ازکا کل تا کدشمده‌شده‌باشد ‪۴‬‬
 ‫لوك ‪ = ۷‬بفتح الث بروزن خوبك»‬       ‫س‬
                                                      ‫‪ -‬و بم‌عنی اوران هم آمده است ‪ -‬وبلفت‌هندی‬
   ‫زردبی رااگوبند که ببب آ فتی برغل زار افند‪.‬‬
                                                      ‫فولنج را گووبفند‪-‬تونحمثاوالنی »ناخن پای‌شتر‬
 ‫ج اهنیول بلر ووزلنه »‬
                     ‫سو له=مبا‬                    ‫ساین بی‬
                                                        ‫بواف‬            ‫ننند‬
                                                                           ‫ارس‬
                                                                             ‫وف‬‫خربی‬
                                                                                  ‫باشد و آ لرابع‬
 ‫مطلق سوراخ راگوبند عموماً ‪ -۸‬و سوراخ‌یش‬                                          ‫کرن‪.‬‬
                                  
==== leaf 656 p~ 1199 ====
 ‫کردیده ‪ ,‬وآن نام بتی بود ومعنی ترکیبی آن‬                        ‫سو منات ‪ = ۹‬هم اول وفتح میم‌ولون‬
‫سوم نات است بعنی صنمی است امول قمر» چه‬                           ‫بالف کشیده بروزن مهمالات‪:‬خانه‌ای بودم‌درملك‬
      ‫سوم بپندی قمررا گوبند ونات تءظیم‌است‬                        ‫گجرات‪ .‬کونند سلطان محمود غبزنروایاخراب‬
 ‫سومندر ‪ = ۲‬با دال ابجد بر وزن‬                                   ‫کرد ومنات راکه از بتهای مشپور است در آن‬
 ‫سوزنگر » بمعنی سمندراست» وآن‌جانوری باشد‬                        ‫‪ .‬و بعضی گوبند که‌فریش‬    ‫بتخانه مشیبکودست‬
                                                                 ‫بکزهاکنریده بودند و از راه دروا‬
                                                                                               ‫هنات را از ع‬
                        ‫که درآش متکون میشود‪.‬‬
                                                                 ‫بدانجاآورده ؛ وبسکون عیم همکفته‌اند‪.‬و گو‌ند‬
‫‪ = ۴‬بض‌اول وقتح میم » بمعنی‬             ‫سومه‬
                                                                  ‫اين لفت هندوی است که مفرس شده بهنی‌فارسی‬
  ‫‪ -‬سانسکریت ‪81102020710٩‬‏ « ماللهند ‪ ۹4۳‬از ‪ :‬سومه (ماه) ب‪+‬ات (ساحب) ‪:‬‬
    ‫جواج الق و مالاس موه‬
                       ‫تشر رات و ر هوا وتات الماک فه‬
   ‫ونر اللهعنه‌فی‌سنة ست عثرة واریع مائة للهجرة ‪« »...‬ماللهند ‪١٠٠٠‬‏ ‪ .‬هم بیرولی ‪.‬دروجهنسميه‬
  ‫ِ نام شرحی از افعانه های هندی تقل میکند بدین مضمون ‪ ... « :‬و کمته‌اند که مذازل ماه‬
   ‫‪۸‬ند که ماه با امشان مزارجت کرد و ساز اندك زمانی ازمیان‬
                                                        ‫ا‬ ‫(‪1)20۵2[۸۳‬‬
                                                                   ‫ختران برجایت ‪۳‬‬
   ‫ازو شکو ‪۰‬ه بردلف ‪.‬‬      ‫) بیشرهتر مایل شد واگ خواهران دشبدر‬                    ‫به روهی ( ‪inihoR‬‏‬        ‫ا‬
   ‫ول
==== leaf 657 p~ 1200 ====
                                                                                                                 ‫‪-۱ ۱۳-۰‬‬
‫سوی بادیدن د کنایه از شرمنده‬                                                                ‫باشد‪.‬‬          ‫اتها وحوف وطرف‬


                               ‫و خجل شدن باشد‪.‬‬                ‫دون ‪ ۰‬صم اول و سکون ثالی و نون»‬
‫سوی‌ژن ‪ - ۱‬بنتم زای قلطه دار‬                                   ‫یه‬
                                                                ‫بو‬‫ش‪-‬‬
                                                                   ‫باشد ‪۷‬‬                ‫وی‬
                                                                                          ‫و‬           ‫نب‬
                                                                                                       ‫جفاو‬
                                                                                                          ‫بمعئی طر‬
‫وسکون نون » بمهنی سوزن باشد که بدان‌چیزها‬                    ‫ویقتح اول بمعنی‬         ‫ج‬                                  ‫‪ ۱‬ولظیر‬

                                              ‫دوزلد ‪.‬‬

‫سوبس ‪ = ۷‬بفتح اول و الك ‪۰‬جهول‬
‫بروزن خمیس ›بمەعنی | گاه ابودن است که‌بعربی‬                  ‫وکاف زده‪ .‬لفی‬       ‫ونون‬      ‫مهو لو الك بالف کے ده‬

                                      ‫غفلت خوااند‪.‬‬            ‫دوندن‬    ‫نادف باصدا که درهن گام خواب با دروقت‬


‫‪-‬ا ‪:‬لك مجهول و فوقالی‬
                    ‫لوست ^ ب‬
                           ‫س‬                                                                              ‫از بینی بر مبیدأ‪.‬‬
                                                                            ‫رن‬       ‫ف‬       ‫‪۳‬‬                   ‫و‬       ‫‪۱‬‬
‫ساکن » بمنی سوبس باشد که آگاه بودن‬
```


## [2026-09-06T15:57:15.711Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nimport re\nfor i,seg in enumerate(t):\n    if 'سیاه' in seg and i>600:\n        print(i, i+543, seg.count('سیاه'))\nEOF",
 "description": "Find siyah leaves in BQT vol2"
}
```


### [2026-09-06T15:57:17.383Z] TOOL RESULT

```
615 1158 1
631 1174 1
635 1178 1
638 1181 2
641 1184 2
645 1188 1
655 1198 2
663 1206 7
664 1207 18
665 1208 5
678 1221 1
679 1222 7
680 1223 1
```


## [2026-09-06T15:57:23.077Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor L in (663,664):\n    print('==== leaf',L,'====')\n    print(t[L][:2500])\nEOF",
 "description": "BQT siyah entry"
}
```


### [2026-09-06T15:57:24.792Z] TOOL RESULT

```
==== leaf 663 ====
  ‫سیا‬                                                                                       ‫‪4۹۱‬ات‬
 ‫سیاوش ؟ « بر وزن بناکوش» همان‬                    ‫کاف» بمعنی‌مجرد است که ازترك وتجرد باشد ‪۱‬‬
‫سیاوخش است که پکریکاوس باشد ؛ وبفتح واو‬          ‫یمکی از‬ ‫مرت هم بوده ‪ -‬و نا‬     ‫وپر‬ ‫یام‬
                                                                                      ‫کول‬‫‪-‬‬
‫هم آمده است ‪ -‬ویمعتی پرلده‌ای هم هت که‬            ‫پهلوادان توران که در جنگه دوازده رخ بدست‬

                     ‫آبرا سرخاب میگوند ‪.‬‬
‫سیاوش] باد» همان سیاوخش آباد‬                      ‫سيان = بفتح اول بروزن عیان ک»یاهی‬
                        ‫شد ‪.‬‬   ‫کذور‬
                                  ‫است که م‬        ‫است که بر درخت پیچد وبعربی عشقه گویند‪.‬‬
‫سیاوش گرد » بمعنی سیاوخش کرد‬                     ‫اول و فتح واو‬       ‫بکر‬
                                                                       ‫سیاو خش =‬
              ‫است که نام شهر سیاوخش باشد‪.‬‬        ‫عقلی‌را گویند ‪۳‬‬    ‫لذت‬   ‫نقطه‌دارء‬   ‫وشن‬   ‫وسکون‌خا‬



‫سیاه * = بر وزن دگاه » معروفت که‬                 ‫هم هت که‬            ‫رو‬
                                                                      ‫ضپدر‬
                                                                         ‫یاری‬
                                                                            ‫کرکیک‬
                                                                                ‫‪ -‬و لام پس‬
 ‫در مقابل سفید باشد ‪ -‬ومست طافح‌از خودییخبر‬       ‫والی ولامت لیم روز بود و عاشق مادراندر خود‬
‫‪ -‬و غلام حبشی و زنگی را هم‬       ‫بند‬
                                   ‫کاوبز‬
                                       ‫ر‬            ‫سودابه شده بود و برآنش رفت وسوخت ‪. ۴‬‬
 ‫میگویند ‪ -‬ونام خط چهارم است اجزملة هفت‬           ‫سیاو خش | بان = نام شپهری بوده‬
‫خط جام جم کهخط ازرق باشد ‪ -‬وبمعنی تحس‬            ‫در توران که ساوخش آیرا نام خود بنا کرده‬

‫وثرم ‪ -‬و وارون و وارونه هم گفته‌اند ‪ -‬و نام‬                                                     ‫بود ‪.‬‬

‫اسب اسفندبار است و چون سياه بوده بدن نام‬          ‫سیاو خش گرد ‪ -‬بکر کاف فارسی‬
 ‫مبخوانده‌اند ‪ -‬و نکاتمابی هم هت از مصنفات‬        ‫‪ ۰‬بمعنی‌سیأوخش‬    ‫نفطه )‪۱‬‬     ‫وسکون راو دال ی‬


           ‫زردشت وآارا زمزم لیز خوانند ‪. ۷‬‬              ‫آباد است که نام شهر پسر کیکاوس باشد‪.‬‬
                                                                   ‫‪:‬بی لقطه ‪۰‬‬    ‫چك‬    ‫)‪۱‬‬


   ‫‪ ۱‬امن عمتی برساخته‌فرقة آذرکیوان‌است«فرهنک‌دساتیر‪ »4۵
==== leaf 664 ====
 ‫‪۱۲۰0 -‬‬                                                                                               ‫سیاء‌بادام‬
‫سیاه دست ‪ = ۷‬ببایدا‌لنقطه بروزن‬                        ‫سیاه بادام ‪ ۱‬کنابه از چشم‌ممشوق‬
 ‫سیاه مست ک»نایه ازمردم بخیل ورذل و هسك‬        ‫است ‪.‬جه چشم را ببادام تشبیه کرده‌اند‪.‬‬
                                 ‫میاه پستان ؟ » زنی رگاویند که باشد ‪.‬‬
‫رزن‌سیاه‬
       ‫ه باسینبینقطهب و‬     ‫سیاه سگ‬                        ‫فرزند او لماند وهر طفلی را که شیردهد بمنرد‪.‬‬
 ‫رنف ه‪.‬ام موضعی است درجرجان وجشمه‌ایست‬                 ‫سیاه بوش ‌ ت با ‪,‬ای فارسی بروزن‬
 ‫درآن موضم که بهمن نام دارد ‪ .‬اکر ج‪.‬می‌از‬               ‫سیاه کوش ‪ ۰‬شب کرد وعسس ومیربازار ومیرشب‬
 ‫آن چشمه آب بردارند وبك شخص ازابشان‌پای‬                    ‫نآکی‬
                                                              ‫را گویند ‪ -‬وچاوش را بگیفزته‌اند » و‬
‫برکره‌ی که در همانجا میباشد بگذارد آب همه‬              ‫باشد که پیشاییش پادشاه دورباش گوید » و ابن‬
                           ‫آن مردم تلخ مشود ‪.‬‬
                                                        ‫جماعت در قدیم بجهت هیبت و صلایت وسیاست‬
‫سیاه کار ‪٩‬‏ د بکااف بالف کشیده‬                         ‫صاحب‬   ‫سياه می‌بوشیده‌اند ‪ -‬وماته‌ی وسو گوار و‬
  ‫جر‬
   ‫او‬‫فسق‬
       ‫و برای فرشت زده (‪ , )۱‬كاوه از فا‬                ‫تعزیت را نیز گویند ‪ -‬وشیربانان را بعنی‌جماعتی‬
 ‫کاری فاسقی‬     ‫ورسیاه‬
                     ‫سهکا‬
                        ‫دنا‬
                          ‫شک‬‫الو‬
                              ‫بحی‬
                                ‫وظالم وم‬               ‫که شبر و سر وجائوران درنده لگاه میدار لد هم‬

                                      ‫و ییحی ‪.‬‬                                                        ‫بش ‪.‬‬
 ‫بممنی‌سیاه دست‌است‬    ‫شیاه کاسه ‪٩‬‏‬                        ‫سیاه لبك = نوعی از بیدباشد‪. ۴‬‬
‫کهنانه از مردم خیل و ممك ورنلوبد بخت‬                   ‫سیاه جر ده ؟ د بمعنی میاه ریگه‬
                                            ‫باشد ‪.‬‬     ‫باشد چه چرده بمعنی رنکه و لون هم آعده‬
   ‫ف‬
   ‫تال‬
     ‫اه ک‬
        ‫ا‬         ‫سیاه کرد خی‬                                                             ‫ات‬
 ‫کهنانه از فاسق و فاجر و ظلم کننده ومحیل‬               ‫سیاه خافه ‪ - ۱‬ممروفت که خيمة‬
                                            ‫باشد ‪.‬‬      ‫ونابه از بندی‌خانه_وخانة‬
                                                                               ‫صحرانشینان باشد ‪ -‬ک‬
‫فارسی ‪۰‬‬   ‫بکر اف‬       ‫سیاه گلیم ‪ ۱۱‬د‬
```


## [2026-09-06T15:57:36.666Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor L in (538,539,540):\n    print('==== leaf',L,'====')\n    print(t[L][:1200])\nEOF",
 "description": "BQT p.1075 sam"
}
```


### [2026-09-06T15:57:38.803Z] TOOL RESULT

```
==== leaf 538 ====
   ‫اس‬      ‫‪۷۵‬‬                                                                                      ‫ساما کی‬

                                                         ‫ساهاکی »بر وزن چابلامکیعت»ی‬
‫سام کیس ه یک کاف بر وزن باد‬                                      ‫ساما کجه است که صینه‌بند زنان باشد‪.‬‬

 ‫غیس ‪ ۰‬بمعنی‌بزر گه‌وشریف‌باشد واشهرسامکیس‬             ‫ساهان ‪ -‬بروزن دامان‪ .‬نام شخصی‌است‬
                       ‫یعنی مهتر بز رکه وشریف‪.‬‬        ‫که آل سامان که بادشاهان سامالیه اند باو‬
                                                       ‫منسوب‌اند ‪٩‬‏ ‪ -‬و بمعنی ترتیب واسبابوآرایش‬
 ‫است‪ .‬وآن جانوری باشد بهیات‬          ‫بمعنی سمندر‬       ‫وبمرور ساختن چبزها و ساختن‌کارها ونظام‌ورواج‬
                                                       ‫‪ - ۴‬و بمعتی شانه واندازه هم آمده‬             ‫آن باشد‬
 ‫موش و در درون آتش متکون میشود وازیوستش‬
‫کلاه ساز ند وجون چر کن شود در آتش آنداز ند‬             ‫أاست بت و آرام و سکون‌وقراررا لیرگویندوشهر‬
                                                      ‫‪ -‬و بمعنی عصمت‬         ‫ند‬ ‫ورا‬
                                                                              ‫یهم‬    ‫یوب‬
                                    
==== leaf 539 ====
  ‫ساو‬                                                                                                        ‫‪7‬‬


‫سانقه ‪ 1‬د بکر دون و فتح قاف» پر‬                                                                     ‫وامثال آن تکزنند‪.‬‬
‫صباوشان را گوند ‪ ۰‬وآن دوای باشد که بعر نی‬
                                                               ‫سان = روزن کان » بمعنی فارز وروش‬
                                     ‫دم الاخوین خواناد‪.‬‬        ‫م‪-‬طولق سوهانرا لیز‬   ‫وت باشد ‪۱‬‬ ‫امد‬
                                                                                                ‫عرس‬
                                                                                                  ‫و‬
 ‫ساننج ‪ ۷‬ب=فتح الك بورزن نارلج‪,‬‬                                ‫گفته‌اند ‪ ۴‬اعم از چوب‌ساوی واهن وطلا ونقره‬
             ‫وعیف‪.‬‬  ‫ووچك ض‬  ‫مرغکی باشد سياه ک‬                  ‫ساوی ‪ -‬وشبه‌واظیر ومثل‌ومانند راهمکفته‌اند ‪۴‬‬
 ‫ساو ‏ بر وزن کاو » بممنی باج وخراج‬                            ‫‪ -‬و مطلق سلاح جنگه باشد خواه خود پوشند‬
 ‫امت وآن زری‌باشد که یادشاهان‌قوی‌ازیاه‌شاهان‬                  ‫بوشانند ‪ -‬و بمعنی حصه‬                 ‫و خواه برفل واس‬
 ‫هم‬     ‫و رصد‬     ‫و
==== leaf 540 ====
       ‫ه‬
       ‫جاه‬
         ‫ا ب‬
           ‫و‬                                                                                                  ‫ساو آهن‬
                   ‫بجهت رشتن را درآ تحاگذار ند ‪.‬‬
                                                                   ‫ساو آ هن ه بروزن کاوآهن » سونش‬
‫» بر وزن لامور ‪ ,‬کوهی است‬               ‫ساهور‬                       ‫وراد آهنی را گویند که ازدم سوهان‌بریزد‪.‬‬
                                                                                                          ‫ی‬
 ‫درمغرب که ممدن سنگی است بهمین‌نام ‪ .‬وآن‬                            ‫ات‬     ‫بروزن کاوه ‪ ۰‬نامبهلوانی‬    ‫ساو ه‪-‬‬

                                                               ‫یه در جنگه رستم ا‬
                                                                               ‫تورانی خوش کاموسکشال ک‬
 ‫کند ؛ و بجای هامیم هم بنظر آمده است‬                               ‫کته شد و اورا ساوه شاه ایز مبگفتند ‪ -‬ونام‬
                                               ‫له اعلم ‪.‬‬
                                                                    ‫شهری است مشهور ومعروف در عراق ‪٩‬‏ گ‪.‬وبند‬
‫ساهو يه ‪ -‬باهابر وزن آموبه ‪ ۰‬نم‬
```


## [2026-09-06T15:57:45.540Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split(chr(12))\nprint(t[537][:2600])\n\"",
 "description": "BQT leaf 537"
}
```


### [2026-09-06T15:57:47.355Z] TOOL RESULT

```
 ‫ساما کسه‬                                                                                   ‫ت‬
                                                                                            ‫ا و‬
                                                                                              ‫ی‬

‫او را سام ادر میگوبند یمتی اندرآتش وسمندر‬            ‫سالیان د بروزن‌مادبان ؛بمعنی‌سالهاست‬
‫‪ -۵‬و لامکوهی است درماوراءالنهر‬           ‫ت‬
                                         ‫سآ‬‫لفف‬
                                             ‫مخ‬     ‫که جمع سال باشد ‪ -۱‬و بمعنی همه روزه هم‬
‫‪ -‬و درعربی زر طلاباشد ‪ -‬روگهابیرا نیز گوبند‬         ‫هت _ و سال واحد را بیز گفته‌اند ‪ - ۴‬و لام‬
                         ‫که از زروطلا درکان و‬        ‫موضعی است در شروان بکرنار آب‌اری و بعضی‬
                         ‫معدن بهم میرسد ‪ -‬و‬                ‫گوبند نام شهری امت ازولامت شروان ‪.‬‬
                         ‫مر که و هلاك را هم‬          ‫ساليون = بباای حطی‌بر وزن خالدون»‬
    ‫سامآبرس‬          ‫میگویند ‪ -‬و در عربی‬             ‫بیونانی کرفی‌را گویند»وآن رستنبی باشده‌مروف»‬
‫لوعی ازچلیاسه‌هم نهرتاوآسام ابر ص گویند ‪۷‬‬            ‫‪ 3‬بعضی تخم کرفس کوهیرا گفته‌اند ؛ ومعنی‌اول‬
‫واوبیشتر درباغها میباشد وموزی‌لیت وماترنگه‬                                              ‫اصح است ‪.‬‬
‫وون بشکافند‬‫بیز خوانشش‪ .‬گرم وخشك است چ‬                 ‫‪ .‬سام = بروزن لام دعالمپینهواحللام‬
‫وگبزرند گیعقرباهندنافعباشد ‪ -‬وبلغت‌هندی‬              ‫است » و درعربی نیز بهمین نام خوانند ‪- ۴‬ونام‬
                              ‫لکاتمابی است ‪۷‬‬
                                                     ‫پدر زال هم هت که جد رستم باشد ‪ - ۴‬و نام‬
‫ساماخچه ‏‪ ٩‬ه باخای نقطه دار (‪)۱‬‬                      ‫علتی ومررضی‌است که‌بمضی |اراورم دماغی‌میدانند‬
‫بروزن بازارچه » سینه بند زنانراگوبند ‪ ۰‬وآن‬           ‫وسرسام همان است‪ .‬قال‌الطبری‪« :‬هذاالاسم‌فارسی‬
‫پارچه‌ای‌باشدچهار گوشه که‌پستانها رابدان‌بند ند‪.‬‬     ‫وتفضیره مرض‌الراس فسارنهوالرأس والسامعندهم‬
‫ساها کچه * > باکاف ‪ .‬بروزن ومعنی‬                     ‫المرض‪ ».‬وقال‌الشیخ‪ « :‬هوورم‌الرای» ‪ -‬و بمعنی‬
         ‫ساماخجه است که سینه‌بند زنان باشد‪.‬‬           ‫آش باشد چه جالوری که درآتش متکون‌میشود‬
                                                                       ‫(‪ )۱‬چك ‪ :‬باخا‪-‬‬

                       ‫‪ ۱‬دوکلمةٌ سال وماه برخلاف قباس به «یان» جمع سته دوئد ‪:‬‬
          ‫خورده بیار سالیان و شهور ‪.‬‬                      ‫ای کهن کشته در سرای غرود‬
  ‫ناصر خسرو بلخی‪«.‬جامم الحکمتن ‪۹۷۱٩‬‏ ‪.‬‬
  ‫سام (عبری بمعتی اسم) واوارشد‬           ‫‪۴‬‬         ‫بدو معنی اخیر شاهدی دده لشده‪.‬‬       ‫؟‏‬
  ‫اولاد لوح
```


## [2026-09-06T15:58:03.399Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split(chr(12))\nprint(t[537][2400:5000])\n\"",
 "description": "BQT leaf 537 footnotes"
}
```


### [2026-09-06T15:58:05.119Z] TOOL RESULT

```
            ‫ای کهن کشته در سرای غرود‬
  ‫ناصر خسرو بلخی‪«.‬جامم الحکمتن ‪۹۷۱٩‬‏ ‪.‬‬
  ‫سام (عبری بمعتی اسم) واوارشد‬           ‫‪۴‬‬         ‫بدو معنی اخیر شاهدی دده لشده‪.‬‬       ‫؟‏‬
  ‫اولاد لوح بود که بازوجهٌ خود دکرشتی لوح رفت و ازطوفان رهابی بات ‪ .‬اقوام بهود و آرامی و‬
   ‫آشوری وعرب راازنل او پنداشته‌اند‪.‬السنةٌ این‌افوام را زبالهای سامی گونند«قاموس کتاب‌مقدس؟‪.‬‬
  ‫‪ ۴‬در اوستا ‪( 20085‬سیاه)‪,‬نام بك خانواده ابرالی است « بنا ‪٩‬‏ ‪ ۶ ۰۰۱‬بارتولمه‬
  ‫‪ . ۱‬درروابات بهلوانی م ‪۰‬ا نام دوتن از دلیران سبتان « سام» است ‪ :‬یکی يادرثرط که در‬
                                             ‫نامه صورت «شم»آهده واصل آن سام است ‪:‬‬           ‫قاب‬

        ‫وزین هردو(ازتور که وشم) شاهی باثرط رسید‪.‬‬              ‫ز شم ز آن سپس اثرطآمد پدید‬
  ‫‪ +‬گرشاسب نامه ص ‪٩4۰‬‏‬
  ‫‏* اشتقاق عامیانه ‪> .‬چه‬            ‫‪.‬‬    ‫دیکگری نواد کرشاسپ و يدر زال ‪« .‬مزدسنا ‪۳١٤-۷۱4٩‬‏‬
                              ‫سمتدر ماخون از «سالامندرا» بونانی است ‪.‬رك‪ :‬سالامندرا سومندر ‪.‬‬
   ‫‏‪۲ « e gecko = Lacerta gecko = ۱‬كل ص‪ » ۲۳۵‬ماس صریا دیدشتب‬
    ‫‪Y‬‏ ‪amãS 2۵۷‬‬             ‫میم» کربای » ودرخلاصه گفته کهوی سوسماراست «بحرالجواهر» ‪.‬‬
  ‫« اشتینگاس» ‪ = ۸ .‬ماماکجه ‏ شاماخسه ‏ شاما کسه = ساما کی مخفف آن «سماخچه؟ ‪.‬‬
                                                                   ‫‪.‬‬   ‫‪ :‬ساملخمه‪‎‬‬   ‫‪ ٩‬رك‬
```


## [2026-09-06T15:58:15.167Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && python3 - <<'EOF'\nt=open('BQT_v3_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint('leaves',len(t))\nfor i,seg in enumerate(t[:80]):\n    if 'شاهین' in seg or 'سیمرغ' in seg:\n        print(i, 'shahin' if 'شاهین' in seg else '', 'simorgh' if 'سیمرغ' in seg else '')\nEOF",
 "description": "Find shahin in BQT vol3"
}
```


### [2026-09-06T15:58:17.614Z] TOOL RESULT

```
leaves 721
27 shahin simorgh
69 shahin
```


## [2026-09-06T15:58:20.347Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && python3 -c \"\nt=open('BQT_v3_pages.txt',encoding='utf-8',errors='replace').read().split(chr(12))\nprint(t[27][:4000])\n\"",
 "description": "BQT vol3 leaf 27"
}
```


### [2026-09-06T15:58:21.770Z] TOOL RESULT

```
[pdf page 28]
-۱۲۳۷-

سوجای ‎gid‏ پادشاهان ‎ath‏ - ونوعی ازعمارت
هم هت +

شاه نیم رود ۲ ‎aus.‏ از آفتاب
است - و والی و حاکم سیستان را ی زگوبندچه
میتالرا یمروزهم میخوانند .

شاه وار ‘ با واوبالف کشیده‌بروزن

لام دار , هرچیز خوب را گویند کهلایق پادشاهان:

‎act‏ ازجواهرواسباب‌وخانه‌وامثال ‎OT‏ عمومآودری
که‌بی‌همتا بودخصوصا و آنرا ‎(ee‏ هم میگونشد.

‏شاه ورث ۴ - بروزن لاجورده بمعنی
‎Ie‏ وطوق وخرمن ماه پاشد.

‏شاهه = ,نتم نات , نام شهری بودهبنا
کرد پدر مودابه در هاماوران و تولد سودابمزن
‎tT‏ درآن شهرشد» .

‏شاهی ۴ -بر وزن ماهی ۰ بمعلی
پادشاهی و سروری باشد - و نام شاعری حم بوده
است ۵ -ونام‌حلوابی است‌بسیاراطیف ولذید که‌از
شاسته وتخم‌مر غ‌ساز ندسونام‌زری‌ودرمی‌هم‌هست 1 .

‏شاهیدن ¥ = بروزن چاهیدن, بمعنی
پادشاهی کردن و بزرکی لمودن باشد - و بممتی
‎gle‏ و بندکی کردن و صلاح و نقوی داشتن

‎al

‏هم هست و ‎Lol‏ باين می با شاهندن صحیف
خوالی ‎oat‏ باشده ال اعلم.

‎OAL‏ = بروزن‌چاهید»,بمعنی‌تاهنده
است که‌متقی وپرهیز کاروسالح ولیک و کردارباشد۸ ۰

‏شاه ‎Cb‏ اسبه - کنابه از خورشید
جهان گرد باشد .

‏شاهین ‎٩‏ » بر وزن ‎oa‏ معروف
‎cul‏ » و آن‌پرنده ای
باشد شکاری وزنده‌از
جنن سیاه‌چشم-وزبانا
ترازو چوب نراژو را

‏لیز گویند - وینعنی
‎cel‏ .
شایان *-
بامای<طی بروزن پابان. شاهین

‏مخفف ‎GE‏ است که ‎gee‏ لابق وس اوارودر
خور باشد - وهرچیز خوب را بیز گفته‌اند خواه
‎GY‏ پادشاء باشد وخواه امرا - و بمعنی روا هم
هست که بعربی ‎gle‏ کوبند - وممکن را ‎Si‏
‏کفته‌اند که درمقابل واجب ‎Hath‏

‎dy ۱‏ یمروز . ۴ - از: ‎aya) Ny tole‏ دبت راصاف ولیاقت) : «دری شاهوار
آزصدف رحمبمهیط ظپور آعد.» «سندیاد نامه۲ع8» .۰ ۳ << شایورد ‎eo)‏ ) ۴ از ‎stele:‏
‏(مسدری) . . ‎٩‏ - آق‌ملك بن‌ملك جمالالدین فیروز کوهی ممروف‌بامیر شاهی سبزوازی‌متوفی
بال ۸0۷ قمری.ر:تذ کر دولنشاه چاپ‌لیدن‌س۲ 1 ببعد. ۷ -از:شاه ۲ ی(سبت) س ‎oyal‏
‏)24 ربال). ‎KE‏ مسی باییکلی که ارزش آن ‎theme‏ فران است ۰ کیلکی ‎SHE‏ ( مخفف آن).
۷ -از:شاه ۲ ‎Ga‏ (پوند مصدری).
از 2515 شاه درآمده واین پرنده بمنابت شکوه وتوانابی‌وتقدس خود ‎(OME pool)‏ خوانده شده باشد
(قی :شاهبازم.م. ). شايدهم شاهین‌همان مثنه 98608 (رك: سیمرغ) باشد که دراوستا دام عقاب
(- آله) امت. درلهجه‌ای ‎ole‏ شائین ‎Shain‏ بجای مانده است . «کایگر . فرهنگه ‎yl‏
‏- اسم فاعل از «شاستن».

‎fol? ‏چنین مینماید که صفت‎ ٩

‎A‏ رل:شاهیدن.

‏شرقی. ص2۱۱ فاب ۱ ص۳۱۸ * .
# شاید بوو - رك ‎Kale:‏ بود .
# شایستن - بکسرسوم « پپلوی ‎shdyistan‏ — 0ها(۳2 ‎gly)‏ » فادر بودن) .
آزرمتة اوستابی-5/08(نواستن) (ر:شاه.شهر) «بارتولمه۵۵۱» «یب رک۲۱۵» «اسشق,هوبهمان
‎shoon CLS ۷4‏ [ 5۲2( شایدرفتن)*806120 ] 0۵-5118(ساید کفتن) +سزاوار بودنءلایق
ومناسب بودن: «ملك کفتا هرآ بنه ماولغردمندی‌کافی‌باید تا تدیبرمملکت رابشایده « کلستان۳۷*.
```


## [2026-09-06T15:58:33.708Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SOD s'w black ===\" && grep -n \"s'w\\|š'w\\|sw B\\|'black'\" SOD.txt | grep -i \"black\" | head -20",
 "description": "Grep Gharib Sogdian for black"
}
```


### [2026-09-06T15:58:33.761Z] TOOL RESULT

```
=== SOD s'w black ===
```


## [2026-09-06T15:58:35.832Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA && python3 - <<'EOF'\nt=open('PLA_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint('leaves',len(t))\n# printed = leaf(1-based) - 15  => leaf1 = 188+15 = 203 -> index 202\nfor i in (201,202,203):\n    print('==== idx',i,'printed',i+1-15,'====')\n    print(t[i][:1600])\nEOF",
 "description": "Asbaghi p.188"
}
```


### [2026-09-06T15:58:37.631Z] TOOL RESULT

```
leaves 302
==== idx 201 printed 187 ====
saClik                                                                      187                                                               sanädil

Suas    - saClik             = sa 1lük q- v.


slao-       sagäna:              '"Kastagnetten;                 in     Spanien           übl.       Handklappinstrument                       aus    zwei
       miteinander                 verbundenen             bewegl.             am    Daumen          befestigen            Hartholzschalen"!"
       << pers.              sl“, Sagäne                ı wahrscheinlich                       ein     Dual    v.        mp.    sj:?     &öbak       "zwei
       kleine         Holzstücke".


 >92.          sifahbad:                "General"          = isfahbad                q. v.

„>#- sagqr:           "Rad"         = saqr u.             zaqr q. V.                2,

Su. sakk:             "Gerichtsakt" aus                    dem pers.                sedek       _>tk.         cek,        engl.        check,
       frz;,      cheque.
       Scheck          geht         aller          Wahrscheinlichkeit                      nach        auf    das        pers.        tschäk
       "Urkunde,             Vertrag"              zurück        3,
       Dtsch.         Scheck:             "Anweisung             (an eine            Bank        od.    an    die        Post)        auf     Zahlung
       von Geld an einen Dritten"                                     pers.           > ar.> lat.> £rz. *.

 Se - sakäk:                 Pl.        v.cw sakk s. sakk.

=> - salib: "das Kreuz" Nabiga 2, 10 i
==== idx 202 printed 188 ====
Sanär                                                                             188                                            sandaldand



„Us-      sanär:             "Platane"                  (Bot) < pers. ‚ie &enär                             ! mp.       Jusp einär        2,
       aram.
          pi (pers.                                „ig) 3,

&r-       sang:         "Kastagnetten"                                pers.        _” zang 4 mp.                  we sanj   S,


2     - sang? : "persische                             Harfe"             —T pers.                 gang ec         mp.„ıp Sang     7     syr.
         a,                 mand.            singa       (p. 2             ) 9

                                                                                           Y
aaur
  - sanga:                   "Gewicht"                 pers.                aa         sange       10 <TImp. >        sang v.      Verbier»
                        11
       saxtan                .


as - sangi: "jmd.,                                der san?                spielt".

Jr - sandal:                     "Sandelholz"                    <        pers.)yo Sandal                I mp.)sı9 tandal          12     syr.
              [u                   .          13                                         "
         Wrilp. dxe)
       Sandale:              aind.            candanah                     Sandale           "leichte       Fußbekleidung"               pers.>
       griech.               —         lat.        14,
                                                        
==== idx 203 printed 189 ====
sandaläni                                                                 189                                                    saiädala


las         _ sandaläni                    = sandaläni             q. v.

eb     2»            sandanänl              = sandaläni             q.    v.


m+- sanam:                 "Götzenbild"                 pers .a.. $aman                      .

@?- sanüf:                  Pl. v. @"sanf.

„6,7 - sahbad               =     isfahbad             q.    V.


1,         - sawärid:                 "kalt"       s.       sard.

al»         -       sawälida:              Pl.    v.obl,,          saulgän        q.    v.


ss - güfl:                 "persischer                 Bettelphilosoph"                 2,

J,+-
 =         5 sül:     "Name           eines       türkischen             Stammes        im       Osten    des       Iran"
                                                                                                                     -           pers.   d4
       %1           3 << mp. Ip &51                4


Es     -        aulaf:           "nudelholz             zum       Auswalzen        des       Teiges" <T pers.               a,    Cübe    >
           mp.             Sie son          ®.

Sl),            -    saulgän:              "die    pers.          Keule    beim        Würfelspiel"             7       vers.     or

       Cügän "Polospiel,                          Stab fürs Polospiel" T mp. wouıg                                    cOpgän,     ar.    Lw.
            y
       sauläan 8 ”, aram.
```


## [2026-09-06T15:58:50.197Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"--- SOD sizes ---\" && wc -l SOD.txt SOD_pages.txt && echo \"--- search 'black' ---\" && grep -n -i \"black\" SOD_pages.txt | head -30",
 "description": "Search Gharib for black"
}
```


### [2026-09-06T15:58:50.251Z] TOOL RESULT

```
--- SOD sizes ---
 111423 SOD.txt
  45615 SOD_pages.txt
 157038 total
--- search 'black' ---
5871:     black stone, agate
15099:         lampblack, soot                                                       C2, 40R 21 n p85; Benv. JA 1955, 324; STSC 59
30204:                                                                  black
30217:9168 s'tNvy B                               J*^y~ tj+te           blackish
30682:     black
37770:                                         black 9177,9338                        boot 8160
37772:best   1295, 3927                        blackish    9178                       border   10063, 10392
37773:(to)bc successful      1080              black stone 739                        0o)bore   9017, 9059, 9063, 9068
38719: lampblack       4002                       (r<?)leave    1884, 2035, 6463, 6466,       9142
```


## [2026-09-06T15:58:52.547Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '30190,30230p' SOD_pages.txt",
 "description": "Gharib entry 9167 black"
}
```


### [2026-09-06T15:58:52.594Z] TOOL RESULT

```
9165 s}s- B, M, C                    jj^tQjAjJiioxft^
                                                                    832.22
     sas ©*0rasa- ? ©inf. -())y =»sys-, 5r*s-
     (r<9)scatter, (/<?)disperse                             9175 s*txw =» s^wx, s»tyxw
                                                                   happy
     GMS 451 n 1, 611; TSP 14.9, 12, 6.172, 7.144;           9176 s'tyxw S                                          uWi
       BSTBL, Padm. 56, 59, Dhy. 175; Farg. Len. 93,              satxu (sytxw) ^s^wy, s>twx
       32; BBB 710; STi 75.18; Sund. AoFiii 1975,
       56.18; BSTii 885.7: C2, 2sg. dur. pres. Psysq,             Anc. Lett. 2.3, 3.2, 29, 5.2
          51R1-Sr>s, Dhy. 68
                                                             9177 s'w B, M, S                                        .u
9166 s'smnty C                                   ^/-^U            saw/u     ©Av. syava; Yaghn. sow-, Oss. sdu ©ob.
     sasmande ©ace. -tw
     scattering
                                                                  black
        C2, 51R10
                                                                  GMS 194s4, 1238; VJ 39d, 1107, 1362; TSP 3.3, 18,
                                                                     -y 76, w2
                                                                    61,     113, 229, 282; SCE 23, 76, 91, 222;
9167 s>t B                                     tetx^jjj
     sat ©<*cyata; Khot. tsata                                      BSTBL, Intox. 5; Dhy. 54, 144; STii 10 p595;
     rich, happy
                                                                    ?wy, STii 8.11,26
        GMS 196; TSP 2.610; SCE p71; BSTBL, Vim. 88;
                                                             9178 s'w-p'm'k                          -U * J,> < J^.L-
          Frag. 2a.l0; Frag. Len. 76.4, 66.3
                                                                  saw-pame
9168 s'tNvy B                               J*^y~ tj+te           blackish
     satux ^s'twx, s>tyxw, s>twy(w)                               TSP 3.3, 18
371

9179 s'wkwr'k      B                                j/V^      9189 sp»y =» sP»y                       iS jy^ 3j&ft
     saw-kure                                                                                                  sfrs-
                                                              9190 spk}ws(h) B
      nightblind                                                   sivkos ©Skt. sivaghosa =»syPkwsh
      SCE 80                                                       name of a country and a city

9180 s'ykn S                                    oL^j^x^J           VJ gloss, p 119
     sekn ^yknCh)                                             9191 spt C
      army commander                                               sabat? ©Syr. sbat
      MDii A-9, 5, 7 p94.5 n p 101.5; Gersh. Advice.               Sabbath
```


## [2026-09-06T15:59:00.464Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls -la MON_part1.txt MON_part2.txt && grep -c \"\" MON_part1.txt MON_part2.txt && grep -n \"صنج\" MON_part1.txt MON_part2.txt | head -20",
 "description": "Grep Mo'in for sanj"
}
```


### [2026-09-06T15:59:00.539Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 4377831 Sep  4 14:06 MON_part1.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 4331421 Sep  4 14:06 MON_part2.txt
MON_part2.txt:94500
MON_part1.txt:99339
MON_part1.txt:45553:حصنجره قرار دارد. این غده در انسان از 
MON_part1.txt:90266:صنج؛ : 571 [معر. . سنج» قس. . چنگ] (.) 
MON_part1.txt:90378:صنوج: ۰ 20201 [ع.] (ا.) ج. . صنح. . صنج‌ها,
```


## [2026-09-06T15:59:02.725Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '90255,90290p' MON_part1.txt",
 "description": "Mo'in sanj entry"
}
```


### [2026-09-06T15:59:02.792Z] TOOL RESULT

```
صنعت. . صنایع ند بعی. صنعت‌هایی که در 
علم بدیم بحث می‌شود» مانند تجنیس» 
مراعاة النظیر» لف و نشر و غیره. صنایع 
دستی: صنعت‌هایی که دست در آنها دخیل 


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
دسته است؛ مق. صندلی بیدسته. صندلی 
راحتی: صندلیی که به راحتی توان در آن 
نشست و باها را دراز کرد. 
صندوق: ههد [ع.] () جع بزرگک 
فلزی یا چوبی ج. صنادیق. ضح.- در عربی به 

ضم اول گویند ولی در فارسی عموماً به فتح 
و تلفظ شود. صندوق نسوز: صندوقی 
فلز ی که در حریق دوام آورد. تالوت مرده. 
(ادا. سانک.) شعبه‌ای در بانک پا ادارات 
دولتی و موّسسات ملی که اخد و پرداخت 
وجه رابه عهده دارد. 
صدوقدار: ۶-۲ [ع. ف. < 
صندوق‌دارنده] (ص‌فا.) خرانه‌دار. (فره.) 
کسی که در حسانداری‌ها متصدی کار
```


## [2026-09-06T15:59:10.877Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^کج\\|کج:\\|کج؛\\|کژ\" MON_part2.txt | head -20",
 "description": "Grep Mo'in for kaj"
}
```


### [2026-09-06T15:59:10.928Z] TOOL RESULT

```
12619:فز: (7۰۶ [معر. کژ - کجه] (.) ابر یشم 
12625:کژاغند - کجاکند] (امر.) جامه‌ای که در 
12635:کجاوه؛ مجمل. 
18200:زبان. انحراف» منحرف شدن» کجی» کژی. 
21004:کج: لا [- کژ] (ص.) ختمنده» ناراست» 
21006:متمایل بیکسوء یکور. خیال کج: خیال باطل. 
21009:جانب خود کشند و غیره). نکر کج: نکر 
21012:یک اه [- کژ؛ قس. ی ی 
21016:کج ]ند سم اکن - کچ آغند 
21040:کج‌افتادن فرهنگ فارسی معین ۱۳۳۵ 
21049:کحار و (۵-)۵2۷2 [- کژاوه - کژابه 
21051:کجبه - کجوه] (!.) دو اطاقکث چوبین رو باز 
21058:کجایی: ۵27-1 (حامص.) کجا بودن. 
21070:کجبین: ۲-0 [- کسجبیننده - کژیین ] 
21074:کج‌پلاس: ۷-5 (ص‌مر.) ند معامله 
21077:کج‌حساب: ات۲۰ [ف. ع.] (ص‌مر.) بد 
21078:کج خلق: ۰۰0۷ [ف. ع.] (ص‌مر) بد 
21081:کج داشتن: ۱-7 (مص ع.) چیزی را 
21082:کج کردن. کج‌دار و مریز: کج داشتن چیزی 
21105:کج کردن: 0 (مص ع.) خمانیدن»
```


## [2026-09-06T15:59:14.024Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '21000,21020p' MON_part2.txt; echo \"=== kazhdom ===\"; grep -n \"کژدم\" MON_part2.txt | head -5",
 "description": "Mo'in kaj entry"
}
```


### [2026-09-06T15:59:14.096Z] TOOL RESULT

```
رقیق. چرک آلود؛ چرکین؛ مق. نظیف. ۳ 
نجس) مة. طاهر. گران» سنگین. (فر.) 
چگال (فره.) 

کج: لا [- کژ] (ص.) ختمنده» ناراست» 
معوج؛ مق. راست. پیچیده» معوج. منحر ف. 
متمایل بیکسوء یکور. خیال کج: خیال باطل. 
قلاب (اعم از قلابی که بدان يحخ در یسخدان 
اندازند یا قلایی که کشتیبان کشتی خصم را به 
جانب خود کشند و غیره). نکر کج: نکر 
باطل. سوء ظن. 

یک اه [- کژ؛ قس. ی ی 


فرومایه کم قیمت. 
کج ]ند سم اکن - کچ آغند 
- کجاغند - کجا کند ‏ کذا کند ‏ قزاکند - 
قراغند] (امر.) جامه‌ای که درون آن را بجای 
پنبه از ابریشم کچ پر کرده باشند و آن را در 
روز جنگ می‌پوشيدند. 
=== kazhdom ===
22843:سقرنیوس. کژدم بحری: (جان.) نوعی 
22845:عقرب البحر. کژدم جراره: (جان.) عقرب 
22846:جراره. (اخ.) برج هشتم» برج عقرب. کژدم 
22847:گردن: برج عقرب. کژدم نیلوفری: برج 
61012:عقرب سیار داشته باشد؛ کژدم‌نا کل.
```


## [2026-09-06T15:59:19.633Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '22830,22850p' MON_part2.txt",
 "description": "Mo'in kazhdom entry"
}
```


### [2026-09-06T15:59:19.685Z] TOOL RESULT

```
از قسمت‌های دیگر شکم باریکتر است. سم 
عقرب در ممالک معتدل حیونات کوچکها 
(از قبیل حشرات و عنکوت‌ها که غذای 
عقربند) را به سهولت می‌کشد ولی برای 
انسان چندان خطرنا کك نیست. عقرب‌های 
بزرگ -مانند عقرب کاشان که سیاه رنگند 
هر چند نیش آنها کشنده نست دردهای 
شدیدی تولید می‌کنند ولی عقرب‌های 
نواحی استوایی - که ممکن است بین ۱۵ تا 


۰ سانتیمتر نیز طول پیدا کنند - نیششان 
خطر نا کك و کشنده است؛ عقرب. درازدم؛ 
سقرنیوس. کژدم بحری: (جان.) نوعی 
خرچنگ دراز دریایی» عروس دریایی؛ 
عقرب البحر. کژدم جراره: (جان.) عقرب 
جراره. (اخ.) برج هشتم» برج عقرب. کژدم 
گردن: برج عقرب. کژدم نیلوفری: برج 
عقرب. (کذ.) شریر)» بد طینت. بدخوی. 
کزژدمه: (م همدص (.) (یز .قد.) 0 
و چرکك کردن زیر ناخن که بر اثر ضربه یا
```


## [2026-09-06T15:59:25.655Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== syagush ===\" && grep -n -i \"syagush\\|siyah gush\\|caracal\" KLN_1966.txt KLN_1971.txt SKT.txt | head -20",
 "description": "Klein syagush/caracal"
}
```


### [2026-09-06T15:59:25.730Z] TOOL RESULT

```
=== syagush ===
KLN_1971.txt:39374:caracal, n., a kind of lynx. — F., fr. Turk, qarah 
KLN_1971.txt:47144:first element in syagush. 
KLN_1971.txt:238636:syagush, n., the caracal. — Pers.-Hind. siyah - 
KLN_1966.txt:6489:carabinieri,  n.  pi.,  the  Italian  police.  —  It.,  pi.  of carabiniere,  fr.  F.  carabinier.  See  carabineer, caracal,  n.,  a  kind  of  lynx.  —  F.,  fr.  Turk,  qarah qulak,  ‘black  ear’.
KLN_1966.txt:7676:cimex,  n.,  bedbug.  —  L.  cirnex,  ‘a  bug  ,  lit.  the dark-brown  insect’,  cogn.  with  OI.  syamah, ‘black,  blackish’,  Avestic  sama-,  ‘black’,  Lilli. Sernas,  ‘bluish  grey,  grey’.  Cp.  chinch  and  the first  element  in  syagush.
KLN_1966.txt:37765:sy-,  pref.  —  Gk.  ou-,  form  of  ouv-,  before  a  fol¬ lowed  by  a  consonant  and  before  See  syn-. syagush,  n.,  the  caracal.  —  Pers.-Hind.  siyah- gosh,  lit.  ‘black  ear',  fr.  siyah,  ‘black’,  and  gosh, ‘ear’.  The  first  element  is  rel.  to  OI.  syamah, Avestic  sama,  ‘black’,  and  cogn.  with  L.  cimex, ‘a  bug’,  lit.  ‘the  dark-brown  insect’ ;  see  cimex. The  second  element  derives  fr.  OPers.  gausha-, ModPers.  gosh,  ‘ear’,  which  is  rel.  to  Avestic gaosho-,  ‘ear’,  and  to  OI.  ghosah,  ‘noise’. Sybarite,  n.,  and  adj.  —  L.  Sy  bar  it  a,  fr.  Gk. Su(iapf-nf]?,  inhabitant  of  Sybaris,  fr.  EuflapK;, name  of  a  Greek  town  in  southern  Italy  (now called  Sibari).  The  inhabitants  of  Sybaris  were famous  for  their  luxury,  whence  Sybarite  came to  denote  a  luxurious  person.  —  For  the  ending see  subst.  suff.  -ite.
```


## [2026-09-06T15:59:36.041Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nfor pat in ['cimex,  n.,  bedbug','syagush,  n.,  the  caracal','caracal,  n.,  a  kind  of  lynx']:\n    i=t.find(pat)\n    leaf=t.count('\\f',0,i)\n    print(pat[:20],'leaf',leaf,'-> printed ~',2*(leaf-12),2*(leaf-12)+1)\nEOF",
 "description": "Klein leaf->page for cimex and syagush"
}
```


### [2026-09-06T15:59:38.000Z] TOOL RESULT

```
cimex,  n.,  bedbug leaf 162 -> printed ~ 300 301
syagush,  n.,  the   leaf 824 -> printed ~ 1624 1625
caracal,  n.,  a  ki leaf 136 -> printed ~ 248 249
```


## [2026-09-06T15:59:43.462Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor L in (162,824):\n    seg=t[L]\n    print('=== leaf',L,'===')\n    print(repr(seg[:200]))\n    print('...tail...', repr(seg[-200:]))\nEOF",
 "description": "Klein leaf headers"
}
```


### [2026-09-06T15:59:45.158Z] TOOL RESULT

```
=== leaf 162 ===
'jv,  ‘in a  stream’,  yor\\,  ‘a  pouring  out’,  yoi-rt),  ‘funnel’, yuwuvat,  ‘to  throw  up,  heap  up’,  fr.  base  yu-, corresponding  to  I.-E.  base  *ghu-,  *gheu-,  ‘to pour’,  whence  OI.  ju'
...tail... 'emones  (zool.)  —  ModL.,  fr. Gk.  xtyxXii;,  ‘a  latticed  gate’.  See  cincture, cinct,  adj.,  girt,  girdled.  —  L.  cinctus,  pp.  of  cin¬ gere,  ‘to  gird’.  See  next  word, cincture,  n., '
=== leaf 824 ===
"  waste  away,  lan¬ guish,  disappear’,  whicn  is  rel.  to  OE.  swindan, ‘to  waste  away,  languish,  vanish’,  and  possibly cogn.  with  Aram,  k'andem,  ‘I  destroy’,  OIr.  a- sennad,  ‘final"
...tail... 't.  ‘a  holding  together  (scil.  of  letters)’, fr.  auXXafjLpavEiv,  ‘to  take  or  put  together’,  fr. ouv  (see  syn-)  and  Xa(j.(3av£iv,  ‘to  take,  grasp, seize’.  See  lemma  and  cp.  word'
```


## [2026-09-06T15:59:51.551Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"chinch\" KLN_1966.txt SKT.txt | head -10",
 "description": "Klein chinch"
}
```


### [2026-09-06T15:59:51.617Z] TOOL RESULT

```
SKT.txt:23601:Spanish :  anchovy,  banana,  basUnado, battledoor,  bilbo,  bilboes,  brocade,  cigar, cinchona  (chinchona),  embargo,  filigree, galleon,  galloon  ?,  imbargo,  paraquito, quixotic  rusk,  sarsaparilla.  tiHce  (1).
KLN_1966.txt:7418:Derivatives:  chin,  tr.  v.,  chinn-ed,  chinn-y,  adjs. China,  n.  —  Fr.  Chin  or  Hsin,  name  of  the  First Dynasty  of  China  (255-206  B.C.E.).  This  word lit.  means  ‘man’.  Cp.  cheyney,  chine,  sinology. Cp.  also  serge,  Seric,  silk, china,  n.  —  Short  for  orig.  chinaware,  i.e.  ‘ware from  China’.  See  prec.  word, chinar,  also  cheenar,  n.,  the  Oriental  plane  tree ( platanus  Orientalis).  —  Pers.  chinar. chinch,  n.,  the  bedbug.  —  Sp.  chinche,  fr.  L.  ci- micem,  acc.  of  cimex,  ‘bedbug’.  See  cimex. chinchilla,  n.,  a  small  S.  American  rodent.  — Sp.,  a  hybrid  coined  from  a  S.  American  native name  and  the  Spanish  dimin.  suff,  -ilia. chin-chin,  n.,  polite  salutation;  ceremonious  talk.
KLN_1966.txt:7676:cimex,  n.,  bedbug.  —  L.  cirnex,  ‘a  bug  ,  lit.  the dark-brown  insect’,  cogn.  with  OI.  syamah, ‘black,  blackish’,  Avestic  sama-,  ‘black’,  Lilli. Sernas,  ‘bluish  grey,  grey’.  Cp.  chinch  and  the first  element  in  syagush.
KLN_1966.txt:7680:Cinchona,  n„  1)  a  genus  of  trees  of  the  madder family  (bot.);  2)  (not  cap.)  the  dried  bark  of various  species  of  Cinchona  and  the  drug made  from  it.  —  ModL.,  coined  by  Linnaeus from  the  name  of  the  countess  of  Chinclwn, who  introduced  the  drug  into  Spain  in  1638. (The  formation  of  the  name  is  erroneous.  The exact  form  should  have  been  Chinchonia.) cinchonism,  n.,  the  effect  of  cinchona  or  its  alka¬ loids  (med.)  —  Formed  fr.  prec.  word  with  suff. -ism.
```


## [2026-09-06T16:00:14.717Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nimport re\ndef leaf(pat):\n    i=t.find(pat)\n    return -1 if i<0 else t.count('\\f',0,i)\nfor p in ['cherub,  n.','chinch,  n.,  the  bedbug','cimex,  n.,  bedbug','syagush,  n.','zymurgy','aard']:\n    print(p, leaf(p))\nprint('total leaves', t.count('\\f'))\nEOF",
 "description": "Klein calibration leaves"
}
```


### [2026-09-06T16:00:16.595Z] TOOL RESULT

```
cherub,  n. 155
chinch,  n.,  the  bedbug 156
cimex,  n.,  bedbug 162
syagush,  n. 824
zymurgy -1
aard 12
total leaves 902
```


## [2026-09-06T16:00:34.579Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor L in (439,440,441,789,790):\n    print('=== leaf',L,'===', repr(t[L][:150]))\nEOF",
 "description": "Klein leaves 439-441 and 789"
}
```


### [2026-09-06T16:00:36.493Z] TOOL RESULT

```
=== leaf 439 === 'e,  adj.  —  Formed  with  suff.  -ive  fr.  L.\nirrigatus,  pp.  of  irrigare.  See  irrigate, irriguous,  adj.,  moist,  irrigated.  —  L.  irriguus,'
=== leaf 440 === 'te,  ‘to  anger’,  and -able.  Derivatives :  irritabl-y,  adv.,  irritabil-ity,  n. irritancy,  n. ,  the  state  of  being  irritating.  —  Form¬ ed'
=== leaf 441 === 'timulate,  stir  up,  provoke’, prob.  freq.  of  *ir-ri-re,  ‘to  stir  up,  excite’,  fr. in-,  in’,  and  I.-E.  base  *erei-,  ‘to  set  in  motio'
=== leaf 789 === 'ModL.,  compounded of  spermato-  and  Gk.  ^o)ov,  ‘animal’.  See  zoo-, spermine,  also  spermin,  n.,  a  crystalline  basic compound  C10H26N4  (b'
=== leaf 790 === 'ument  for  meas¬ uring  blood  pressure  in  the  arteries.  —  Com¬ pounded  of  sphygmo-  and  manometer, sphygmometer,  n.,  an  instrument  for  '
```


## [2026-09-06T16:01:11.031Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\ndef leaf(pat):\n    i=t.find(pat); return -1 if i<0 else t.count('\\f',0,i)\nfor p in ['Kyrie','labial','lynx,','macabre','nadir','oasis','pagan','quack','rabbi','sabbath','Sabbath','tabby','ubiquit','vacant','wafer','xeno','yacht','zeal']:\n    print(p, leaf(p))\nEOF",
 "description": "Klein letter-start leaves"
}
```


### [2026-09-06T16:01:13.020Z] TOOL RESULT

```
Kyrie 40
labial 102
lynx, 493
macabre 493
nadir 549
oasis 70
pagan 31
quack 125
rabbi 2
sabbath 455
Sabbath 376
tabby 828
ubiquit 886
vacant 28
wafer 162
xeno 370
yacht 122
zeal 2
```


## [2026-09-06T16:01:25.149Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PHD cang/syah/sen ===\" && grep -n -i \"^cang\\|^čang\\| cang \\|^syā\\|^syah\\|^sēn\\|^sen \\|sēn murw\\|senmurw\\|^sām\\|^sam \" PHD.txt PHD_mackenzie.txt | head -30",
 "description": "MacKenzie Pahlavi forms"
}
```


### [2026-09-06T16:01:25.211Z] TOOL RESULT

```
=== PHD cang/syah/sen ===
PHD.txt:4807:sēnag
PHD.txt:4808:sen murw sezd sézdén haftād*
PHD_mackenzie.txt:8467:camisn                   ,~C\         cam!, cang                     .. ,<;
PHD_mackenzie.txt:9060:sen                          ,t"'U'     salwar
PHD_mackenzie.txt:9065:sen murw               \ t6 K»          salag
```


## [2026-09-06T16:01:27.064Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AHD hook/hue ===\" && grep -n \"^keg-\\|^kei-\\|^kei-1\\|^kei-2\\|hook\\b\" AHD_watkins1985.txt | head -20; echo \"=== AHD hue ===\" && grep -n \"HUE\\|hiwja\\|hiwi\" AHD_watkins1985.txt | head -10",
 "description": "Watkins AHD roots"
}
```


### [2026-09-06T16:01:27.132Z] TOOL RESULT

```
=== AHD hook/hue ===
165:Terms for the furrow are perk-? and selk-; wog”h-ni- designated the wedge-shaped plowshare. Other related roots are yeug-, “to yoke,” serp-', “sickle, hook,” and kerp-, “to gather, pluck” (HARVEST). The root g”ere-?, “heavy,” is the probable base of *g”ero-nd-, “hand mill” (QUERN). The term is found throughout the Indo-European-speaking world, including India.
284:tives: a. ekhinos, hedgehog (< “‘snake-eater”): ECHINO-, ECHINUS; b. ekhidna, snake, viper: ECHIDNA. [Pok. ang#(hji- 43.] ank-. Also ang-. To bend. I. Germanic *ank- in Old Norse *ankula and Middle English ancle, ankle: ANKLE. Il. Suffixed form *ank-ulo-. 1.Germanic *ang-ul- in: a. Old English angul, angel, fishhook: ANGLE!; b. prob- ably Latin Angli, the Angles: ANGLE. 2. Greek ankulos, crooked, bent: ANKYLOSIS; ANCYLOSTOMIASIS. ITI. Greek ankura, anchor: ANCHOR. IV. Greek ankdn, elbow: AN- CON. V. Sanskrit anka, hook, avicati, he bends: PALAN- QUIN. VI. Suffixed variant form *onk-o- in Latin uncus, hooked, bent: UNCINARIA, UNCINATE, UNCINUS, UNCUS; UNCIFORM. VII. Suffixed form *ang-olo- in Latin angu- lus, angle, corner: ANGLE*, [Pok. 2. ank-, ang- 45.] ano-. Ring. 1. Latin dnus, ring, anus: ANUS; ANILINGUS. 2. Latin diminutive annulus, ring, signet ring: ANNULAR, ANNULET, ANNULUS. [Pok. dno- 47.] ans-. Loop, handle. Latin dnsa, handle: ANSATE. [Pok. ansa 48.] ansu-. Spirit, demon. 1. Germanic *ansu- in Old Norse dss, god: AEsIR. 2. Suffixed reduced form *nsu-ro- in Avestan ahura, spirit: AHURA Mazpa, Ormazp. [Pok. ansu- 48.] ant-. Front, forehead. I. Inflected form (locative singular) *anti, “against,” with derivatives meaning in front of, before; also end. 1. Germanic *andi- in Old English and-, indicating opposition: UN-?; ALONG. 2. Germanic *andja- in Old English ende, end: END. 3. Latin ante, before, in front of, against: ANCIENT!, ANTE, ANTE-, ANTERIOR; ADVANCE. 4. Greek anti, against, in enantios, opposite: ANTI-; ENANTIOMER, ENANTIOMORPH. 5. Compound form *anti-oko-, “appearing before, having prior aspect” (*akw-, appearance; see okW-), in Latin antiquus, former, antique: ANTIC, ANTIQUE. 6. Reduced form *nti- in Ger- manic *und- in Old Norse und (> Middle English un-), until, unto: UNTIL. 7. Variant form “anto- in Sanskrit antah, end, in Vedantah, essence of the Veda: VEDANTA. II. Probable inflected form (locative plural) *antbhi, “on ter sides of,” whence *ambhi. See ambhi. [Pok. ant-s 48. ap-'. To take, reach. 1. Latin apere, to attach, join, tie to: APT, (APTITUDE), ATTITUDE; (INEPT). 2. Latin apisci, to attain: ADEPT. 3. Latin apex, top, summit (< “something reached”): APEX. 4, Prefixed form *co-ap- (co-, together; see kom) in Latin cdpula, bond, tie, link: copuLa, COPULATE, COUPLE. 5. Perhaps Latin ammentum, dmen- tum (< *ap-mentum, “something tied”), thong, strap: AMENT!, [Pok. 1. ap- 50.] ap-2, Water, river. Iranian ap- in Persian ab, water: JULEP. [Pok. 2. ap- 51.] apero-. Shore. Perhaps a derivative of ap-?. Suffixed form *dper-yo- in Greek épeiros, land, mainland, conti- nent: EPEIROGENY. [Pok. dpero- 53.] apo-. Also ap-. Off, away. 1. Germanic *af in: a. Old English of, zf (> Middle English of, of-), off: oF, OFF, OFFAL; b. Old English ebba, low tide: EBB; c. Old High German aba, off, away from: ABLAUT; d. Germanic *aftan- in Old English zftan, behind: ABAFT. 2. Latin ab, ab-, away from: AB-!. 3. Greek apo, away from, from: apo-. 4, Suffixed (comparative) form “*ap(o)-tero- in Germanic *aftar- in Old English zfter, after, behind: AFTER. 5. Suffixed form *ap-t-is- in Germanic *aftiz in Old English eft, again: EFTsoons. 6. Suffixed form *apu-ko- in Germanic afug- in Old Norse dfugr, turned backward: AWKWARD. 7. Possible root *po(s), on, in: a. Russian po, at, by, next to: PoGROM; b. Latin post, behind, back, afterward: POST-, POSTERIOR; POST- MORTEM, PREPOSTEROUS, PUISNE, (PUNY); C. Latin pd- nere, to put, place, from *po-sinere (sinere, to leave, let; of obscure origin): APPOSITE, (APPOSITION), COMPONENT, (COMPOSE), (COMPOSITE), (COMPOSITION), (COMPOUND), DEPONE, DEPOSIT, DISPOSE, EXPOUND, IMPONE, IMPOSE, INTERPOSE, OPPOSE, POSITION, POSITIVE, POST, POSTS,
492:TION), GENERIC, GENEROUS, GENRE, GENUS; CONGENER, (CONGENIAL), DEGENERATE, (ENGENDER), MISCEGENA- TION; b. Greek genos and genea, race, family: GENEAL- OGY, GENOCIDE, GENOTYPE, HETEROGENEOUS; c. Greek suffix -genés, ‘‘-born’”: -GEN, -GENY. 4. Suffixed full-grade form *gen-yo- in: a. Latin genius, procreative divinity, inborn tutelary spirit, innate quality: GENIAL!, GENIUS; b. Latin ingenium (in-, in; see en), inborn character: ENGINE, INGENIOUS. 5. Suffixed full-grade form *gen-d- in Latin indigena (indu-, within; see en), born in (a place), indigenous: INDIGEN, (INDIGENOUS). 6. Suffixed full-grade form *gena-wo- in Latin ingenuus (in-, in; see en), born in (a place), native, natural, freeborn: INGENUOUS. 7. Suffixed full-grade form *gen- men- dissimilated in Latin germen, shoot, bud, embryo, germ: GERM, GERMAN?, (GERMANE), GERMINAL, GERMI- NATE. 8. Suffixed full-grade form *gena-ti- in Greek genesis, birth, beginning: GENESIS, -GENESIS. 9. Redupli- cated form *gi-gn- in: a. Latin gignere (past participle genitus), to beget: GENITAL, GENITIVE, GENITOR, GENT!, (GINGERLY); CONGENITAL, PRIMOGENITURE, PROGENI- TOR, (PROGENY); b. Greek gignesthai, to be born: EPI- GENE. 10. Suffixed zero-grade form *-gn-o- in Latin benignus (bene, well; see deu-?), good-natured, kindly, and malignus (male, ill; see mel-5), evil-natured, malevo- lent: BENIGN, MALIGN. 11. Zero-grade form *gna- becom- ing *gnda- in Latin praegnds (prae-, before; see per’), pregnant: PREGNANT!. 12. Suffixed zero-grade form *gna-sko- becoming *gnd-sko- in Latin gndsci, ndsci (present participle ndscéns, past participle gndtus, nd- tus), to be born: NAIVE, NASCENT, NATAL, NATION, NA- TIVE, NATURE, NEE, NOEL; (ADNATE), AGNATE, COGNATE, CONNATE, ENATE, INNATE, NEONATE, PUISNE, (PUNY), RENAISSANCE. 13. Suffixed o-grade form *gon-o- in Greek gonos (combining form -gonos), child, procre- ation, seed: GONAD, GONO-; ARCHEGONIUM, EPIGONE. 14. Zero-grade form *gn- in Sanskrit ja- in krmi-ja-, “produced by worms” (see k*rmi-). [Pok. 1. gen- 373.] genu-'. Knee; also angle. 1. Variant form *gneu- in: a. Germanic *knewam in Old English cnéo, knee: KNEE; b. Germanic *knewljan in Old English cnéowlian, to kneel: KNEEL. 2. Basic form *genu- in Latin genii, knee: GENICULATE, GENUFLECT. 3. Suffixed variant form *gon-ya- in Greek gdnia, angle, corner: -GON, GONION; AMBLYGONITE, DIAGONAL, GONIOMETER, GONIOMETRY, ORTHOGONAL. [Pok. 1. genu- 380.] genu-2. Jawbone, chin. 1. Form *genw- in Germanic *kinnuz in Old English cin(n), chin: CHIN. 2. Basic form *genu- in Greek genus, chin: GENIAL. 3. Suffixed variant form *gna-dho- in Greek gnathos, jaw: GNATHIC, -GNATHOUS; CHAETOGNATH 4, Variant form “g(h)enu- in Sanskrit hanu, jaw: HANUMAN. [Pok. 2. genu- 381.] gep(h)-. Also gebh-. Jaw, mouth. 1. Probably Germanic *kaf-, to gnaw, chew, in Old English ceaf, husks, chaff: CHAFF!, 2. Germanic *kabraz, “gnawer,” in Old English ceafor, ceafer, beetle: CHAFER; (COCKCHAFER). 3. Ger- manic *kéfalaz in Old English céafl, jaw, cheek: JOWL!. [Pok. geph-, gebh- 382.] ger-'. To gather. 1. Extended form *grem- in Germanic *kram- in Old English crammian, to stuff, cram: CRAM. 2. Reduplicated form *gre-g- in Latin grex (stem greg-), herd, flock: GREGARIOUS; AGGREGATE, CONGREGATE, EGREGIOUS, SEGREGATE. 3. Earliest forms “ager-, *ggor-d-, in Greek ageirein, to assemble, and aguris, agora, marketplace (> agoreuein, to speak): AGORA}; (AGORAPHOBIA), ALLEGORY, CATEGORY, PANEGYRIC. [Pok. 1. ger- 382.] ger-2. Curving, crooked; hypothetical Indo-European base for a variety of Germanic words with initial kr-. I. Words meaning to bend, curl; bent, crooked, hooked; something bent or hooked. 1. Germanic *krdpp6n-, a hook, especially one used in harvesting grapes, in: a. Old High German krapfo, a hook: AGRAFFE; b. Old French graper, to harvest grapes, hence (back-formation) grape,
494:vine, grape: GRAPE; c. Old French grapon, grapnel: GRAPNEL; d. Old French grape, a hook: GRAPPLE; e. Ital- ian dialectal grappa, vine stem, brandy: GRAPPA. 2. Old English crump, crumb, crooked, bent, stooping: CRUM- MIE, CRUMPET, (CRUMPLE). 3. Low German krimpen, to wrinkle: CRIMP!. 4. Middle Dutch crampe, hook, and Frankish *kramp, hook: cramMpP?. 5.Old High German krampfo, a cramp, akin to the Germanic source of Old French crampe, cramp: CRAMP!. 6. Old English crypel, a cripple: CRIPPLE. 7. Germanic *kreupan in Old English créopan, to creep: CREEP. 8. Middle Low German krink, a ring: CRINGLE. 9. Germanic *krengan in Old English cringan, to yield: CRINGE. 10. Middle Dutch crinkelen, akin to Middle English crinkelen, to make kinks in: CRINKLE. 11. Old Norse kriki, a bend, nook: CREEK. 12. Old Norse krékr, a hook: cRooOK. 13. Frankish *krok- (> Old French croc), a hook: CROCHET, (CROCKET), (CROQUET), (CROUCH); ENCROACH. 14. Old English crycc, (bent) staff, crutch: CRUTCH. 15. Old French crosse, crook: CROSIER, LACROSSE. 16. Middle Dutch crulle, curly: CRULLER, CURL. 17. Old English cranc-(stzf), a weaving implement: CRANK}. 18. Norwegian krake, a sickly beast, akin to the source of Middle English crok, an old ewe: cRocK3, 19. Old Norse karpa, to boast: CaRP!, 20. Middle Dutch kroes, curled, akin to the source of Old French grosele, gooseberry: GROSSULARITE. II. Words meaning ‘“‘a rounded mass, collection; a round object, vessel, container.” 1. Old English cruma, a frag- ment: CRUMB. 2. Frankish *kruppa, rump, akin to the Germanic source of Old French croup, rump: CROUP?, (CROUPIER), CRUPPER. 3. Old English cropp, cluster, bunch, ear of corn: crop. 4. Italian gruppo, an assem- blage: Group. 5. Old English crocc, pot: CROCK}. 6, Mid- dle Dutch cruyse, pot: CRUSE. 7. Old English cribb, manger: CRIB. 8. Old English cradel, cradle: CRADLE. 9. Frankish *kripja, cradle, akin to the Germanic source of Old French cre(s)che, crib: CRECHE. 10. Old English creet and Old Norse kartr, wagon: CART. 11. Old English croft, small enclosed field: crort. [Pok. 3. ger- 385.] gerbh-. To scratch. 1. Germanic *kerban in Old English ceorfan, to cut: CARVE. 2. Zero-grade Germanic form *kurbiz in Old English cyrf, a cutting (off): KERF. 3. Variant form *grebh- in: a. Germanic *krab(b)- in Old English crabba, a crab: CRAB}; b. Germanic *krabiz- in Old French crevise, crayfish: CRAYFISH; C. perhaps Ger- manic *krab- in Old Norse krafla, to crawl: CRAWL. 4. Zero-grade form *grbh- in Greek graphein, to scratch, draw, write, and gramma (< *grbh-mn), a picture, writ- ten letter, piece of writing, and grammé, a line: GRAF- FITO, GRAM!, -GRAM, GRAMMAR, GRAPH, -GRAPH, -GRAPHER, GRAPHIC, -GRAPHY; AGRAPHA, AGRAPHIA, DIAGRAM, EPIGRAM, (EPIGRAPH), GRAPHITE, ICONOGRA- PHY, PARAGRAPH, PROGRAM, PSEUDEPIGRAPHA, TETRA- GRAMMATON, TOPOGRAPHY. [Pok. gerebh- 392.] [gerere. To carry, carry on, act, do. Latin verb of un- known origin. Oldest form ges-, past participle gestus. GERENT, GERUND, (GEST), GESTATION, (GESTICULATE), GESTURE, JEST; ARMIGER, BELLIGERENT, (CONGERIES), CONGEST, DIGEST, EGEST, INGEST, REGISTER, SUGGEST, VELIGER.] gere-'. To grow old. 1. Suffixed lengthened-grade form *géro-s- in Greek géras, old age: AGERATUM, CALOYER, GERIATRICS. 2. Suffixed form “gera-ont- in Greek geron (stem geront-), old man: GERONTO-. [Pok. ger- 390.] gere-2. To cry hoarsely; also the name of the crane. I, Words meaning “‘to cry hoarsely”; also words denoting the crow. 1, Germanic *kré- in: a. Old English crawe, a crow: CROW}; b. Old English crdwan, to crow: CROW?; c. Old English cracian, to resound: CRACK; d. Middle Dutch krdken, to crack: CRACKNEL; @. Old Norse kraka, a crow: CRAKE. f. Middle Dutch krdnen, to groan, la- ment: CROON. 2. Possibly (but more likely imitative) Germanic *kur(r)- in Old Norse kurra, to growl, akin to Middle English curre, cur: cur. II. Words denoting a
582:kei-'
594:keg-. Hook, tooth. 1. Germanic *hakan- in: a. Old Norse haki, hook, akin to Old English haca, hook: HAKE; b. Middle Low German hake, hook: HARQUEBUS. 2. Ger- manic lengthened form *Adka- in: a. Old English héc, hook: HOOK; b. Middle Dutch hok, hoec, hook: HOOKER}. 3. Germanic *hakila- in Middle Dutch hekel, hatchel, a flax comb with long metal hooklike teeth: HECKLE. 4. Germanic *hakkijan in Old English -haccian, to hack to pieces as with a hooked instrument: Hack!. [Pok. keg- 537.]
595:kei-'. To lie; bed, couch; beloved, dear. I. Basic form *kei-. 1. Suffixed form *kei-wo- in: a. Germanic *hiwa- in Old English hiwan, members of a household: HIND?;
596:kei-?
599:kei-2, Referring to various adjectives of color. 1. Suffixed o-grade form *koi-ro- in German *hairaz, “gray-haired,” old, venerable, hence master, in: a. Old English har, gray, hoary: HOAR; b. Old High German hér, worthy, exalted: JUNKER; Cc. Middle Dutch here, master, lord: YOUNKER. 2. Suffixed zero-grade form *ki-wo- in Germanic *hiwam in Old English hiw, héo, color, appearance, form: HUE}. [Pok. 2. Rei- 540.]
600:kei-3. To set in motion. I. Possibly extended o-grade form *koid- with suffixed form *koi-d-ti- in Germanic *haissiz in: a. Old English h&s, a command, a bidding: HEST; b. Old English compound beh#s, a vow, promise, com- mand (be-, intensive prefix; see ambhi): BEHEST (but perhaps to be referred to a separate root *kaid-). Il. Zero-grade form *ki-. 1. Form *ki-eyo- in Latin ciére (past participle citus), with its frequentative citdre, to set in motion, summon: CITE; EXCITE, INCITE, OSCITANCY, RESUSCITATE, SOLICITOUS. 2. Suffixed form *ki-neu- in Greek kinein, to move (> kinésis, motion): KINEMATICS, -KINESIS, KINETIC; CINEMATOGRAPH, CINEMATORADIOG- RAPHY, HYPERKINESIA, KINESIOLOGY, KINESTHESIA, KININ, (TELEKINESIS). [Pok. kei- 538.]
611:perhaps akin to the source of Middle English nokke, nock: NOCK; b. Norwegian (dialectal) nok, projection, hook, akin to the Scandinavian source of Middle English nok, corner, nook: NooK. [Pok. 1. ken- 558.]
639:kleu-2. To wash, clean. 1. Latin clodca, sewer, canal: CLOACA. 2. Zero-grade form *klu- in Greek kluzein, to wash out: CLYSTER; CATACLYSM. [Pok. 2. kleu- 607.] kleu-3. Possibly hook, peg. I. Extended zero-grade form *klud- possibly in Germanic *Aluta-, lot, portion (seman- tic development obscure). 1. Old English Alot, lot: Lor. 2. Dutch lot, lot: LOTTERY. 3. Old French lot (> French lot), lot, portion: LOTTO; ALLOT. II. Suffixed variant form *klau-do- in Latin claudere, to close (< “to lock with a hook, bolt”): CLAUSE, CLOISONNE, CLOISTER, CLOSE, (CLOSURE), (CLOZE); CONCLUDE, ECLOSION, EXCLUDE, INCLUDE, OCCLUDE, PRECLUDE, RECLUSE, SECLUDE. III. Variant form *k/dw-. 1. Suffixed form *kldw-i- in Latin cldvis, key: CEMBALO, CLAVICLE, CLAVIER, CLEF, KEVEL; CLAVICHORD, CONCLAVE, ENCLAVE. 2. Suffixed form *kldw-o- in: a. Latin cldévus, nail: CLOVE!, CLOY; b. Latin clava, club: CLAVATE; CLAVICORN, CLAVIFORM. 3. Suffixed form *k/dw-yo- in: a. Greek kleiein, to close: CLATHRATE; b. Greek verbal adjective kleistos, closed: CLEISTOGAMOUS, CLEISTOTHECIUM. [Pok. k/éu- 604.] klewo-. Bald. Variant *kal(a)wo- in Latin calvus, bald: CALVARIUM. [Pok. k,/ouo- 554.]
928:serp-'. Sickle, hook. 1. Latin sarpere, to cut off, prune (> sarmentum, twigs): SARMENTOSE. 2. Greek harpé, sickle (> Old French harper, to seize): HARPOON. [Pok. 5. ser- 911.]
=== AHD hue ===
597:b. suffixed Germanic form *hiwid6 in Old English higid, hid, a measure of land (< ‘household”): HIDE®. 2. Suf- fixed form *kei-wi- in Latin civis, citizen (< “member of a
599:kei-2, Referring to various adjectives of color. 1. Suffixed o-grade form *koi-ro- in German *hairaz, “gray-haired,” old, venerable, hence master, in: a. Old English har, gray, hoary: HOAR; b. Old High German hér, worthy, exalted: JUNKER; Cc. Middle Dutch here, master, lord: YOUNKER. 2. Suffixed zero-grade form *ki-wo- in Germanic *hiwam in Old English hiw, héo, color, appearance, form: HUE}. [Pok. 2. Rei- 540.]
1657:HOYDEN kalto- HUBRIS ud- HUCKSTER keu-2 HUE! kei-2 HUGUENOT neud-, oito- HULL kel-2
```


## [2026-09-06T16:01:35.577Z] TOOL CALL #51: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-06T16:01:35.583Z] TOOL RESULT

```


```


## [2026-09-06T16:01:39.727Z] TOOL CALL #52: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%DA%86%D9%86%DA%AF",
 "prompt": "Give the full Persian entries for چنگ: etymology for both 'claw/hand' and 'harp' senses, Middle Persian forms, Proto-Iranian reconstruction, and any note on Arabic صنج."
}
```


## [2026-09-06T16:01:41.579Z] TOOL CALL #53: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%DA%A9%DA%98",
 "prompt": "Give the Persian entry for کژ (kaž) / کج (kaj): etymology, Middle Persian form, Proto-Iranian/PIE root, meaning, and cognates. Also any mention of کژدم."
}
```


### [2026-09-06T16:01:47.155Z] TOOL RESULT

```
# Persian Entries for چنگ

## Etymology 1 (Claw/Hand Sense)

**Origin:** "Ultimately from Proto-Indo-European *kog-, *keg-, *keng- ('peg, hook, claw')." Cognates include English "hook" and Old Armenian ճանկ (čank).

**Meanings:**
- Claws, talons
- Clutch, embrace
- Hand, fingers (dialectal/literary)
- Beak (dialectal/literary)

## Etymology 2 (Harp Sense)

**Origin:** Derived from Middle Persian čang ("harp"), with cognates in Parthian šang and Sogdian forms meaning musical instruments. The term also influenced Arabic صنج (ṣanj), described as "a Middle Persian borrowing."

**Meaning:** Lyre, harp

## Key Note

Both etymologies coexist in Persian, though they likely stem from different roots—one from Proto-Indo-European via the sense of "grasping," another from Middle Persian musical terminology that spread across regional languages including Georgian, Azerbaijani, Turkish, and Arabic.
```


### [2026-09-06T16:01:48.278Z] TOOL RESULT

```
# Persian Entry: کژ (kaž)

## Etymology 1 (Adjective)

**Meaning:** Alternative form of کج (kaj), meaning "crooked"

**Origin:** Derived from Middle Persian کژ/گز (kaž, gaz), ultimately from Proto-Indo-European roots *kog-, *keg-, *keng- meaning "peg, hook, claw"

**Cognates:** Related to چنگ (čang) and English "hook"

**Historical usage:** Appears in Rumi's Masnavi (c. 1260s), where it describes hearts and shoes as "crooked"

## Etymology 2 (Noun)

**Meaning:** A type of silk fabric

**Origin:** From Middle Persian kač, with connections to Old Armenian կաճ (kač, "felt"), Old Georgian ყაჭი (q̇ač̣i), and Arabic خَزّ/قَزّ (ḵazz/qazz, "silk")

**Alternative forms:** کز (kaz), کج (kaj), غژ (ġaž), قز (qaz)

## Related Term

**کژدم** (každom) is listed as a derived term from Etymology 1.
```


## [2026-09-06T16:01:56.391Z] TOOL CALL #54: Bash

```json
{
 "command": "python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/چنگ' --note 'page 247, root Keg/Keng, Persian čang «چنگ» claw/harp: PIE *keg- origin and Arabic صنج as MP borrowing' 2>&1 | tail -3; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/کژ' --note 'page 247, root Keg/Keng, Persian kaž/kaj «کژ/کج» crooked < MP kaž, PIE *keg-; کژدم derived' 2>&1 | tail -3",
 "description": "Archive Wiktionary chang and kazh"
}
```


### [2026-09-06T16:01:58.939Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/92f43522bdfc68af.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f19eb04ba541ed2d.txt
```


## [2026-09-06T16:02:02.866Z] TOOL CALL #55: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B3%DB%8C%D8%A7%D9%87",
 "prompt": "Give the Persian entry for سیاه: full etymology, Middle Persian form, Old/Proto-Iranian and Proto-Indo-Iranian/PIE reconstruction, cognates (Avestan, Sanskrit), and any derived terms like سیاه‌گوش."
}
```


## [2026-09-06T16:02:04.634Z] TOOL CALL #56: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B4%D8%A7%D9%87%DB%8C%D9%86",
 "prompt": "Give the Persian entry for شاهین: etymology (is it from شاه + -ین, or from Avestan saēna?), meanings, and any cited sources."
}
```


### [2026-09-06T16:02:10.041Z] TOOL RESULT

```
# Persian Entry: سیاه (siyāh)

## Etymology
The word derives from Middle Persian (sydʾ /syā/, "black"), tracing back through Old Persian to Proto-Iranian *cyaHwáh and Proto-Indo-Iranian *ćyaHwás. The ultimate source is Proto-Indo-European *(s)ḱih₃-wó-s.

## Historical Forms
- **Middle Persian:** sydʾ (/syā/)
- **Old Persian:** [attested but script form needed]
- **Proto-Iranian:** *cyaHwáh
- **Proto-Indo-Iranian:** *ćyaHwás

## Cognates
Related terms appear across Indo-European languages: Avestan siiāuua, Sanskrit श्याव (śyāva), Russian сивый (sivyj, "grey"), Lithuanian šývas ("light grey"), and Old English hīew (ancestor of English "hue").

## Core Meaning
As an adjective, سیاه means "black," with the synonym مشکی (meški). As a noun, it denotes "dark-skinned" persons.

## Selected Derived Terms
Compound formations include:
- سیاه‌پوش (siyâh-puš)
- سیاه‌چشم (siyâh-česm)
- سیاه‌گوش (siyâh-guš)
- سیاهماهی (siyâhmâhi)
```


### [2026-09-06T16:02:10.448Z] TOOL RESULT

```
# Persian Entry for شاهین

## Etymology

The word derives from Middle Persian *šāhēn*, literally meaning "majestic, kingly." The entry notes: "By surface analysis, شاه (šâh) +‎ ـین (-in)," indicating it can be analyzed as the word for "king" plus a suffix. However, the document does not mention Avestan *saēna* as a source.

## Meanings

As a noun, شاهین has two definitions:

1. **Falcon**, particularly the Barbary falcon (*Falco peregrinus pelegrinoides*)
2. **Pointer** of a scale or balance

The entry also lists it as a proper noun—a male given name corresponding to English "Shahin," "Shaahin," or "Shaheen."

## Cited Sources

The references section cites Ferdinand Justi's *Iranisches Namenbuch* (1895) regarding the etymological connection to Middle Persian origins, supporting the "majestic, kingly" interpretation.
```


## [2026-09-06T16:02:17.658Z] TOOL CALL #57: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B3%DB%8C%D9%85%D8%B1%D8%BA",
 "prompt": "Give the Persian entry for سیمرغ: etymology, Middle Persian form (sēnmurw), Avestan mərəγō saēnō, and meaning."
}
```


## [2026-09-06T16:02:18.794Z] TOOL CALL #58: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/chinch",
 "prompt": "Give the etymology of 'chinch' and, if shown, 'cimex'. Also any related entry for Spanish chinche / Latin cimex."
}
```


### [2026-09-06T16:02:22.521Z] TOOL RESULT

```
# Persian Entry for سیمرغ

**Etymology:** The term is "Inherited from Middle Persian _𐭮𐭩𐭭𐭬𐭥𐭫𐭥_ (synmwlw /⁠sēn-murw⁠/)." Folk tradition proposes it combines سی (sī, "thirty") and مرغ (murġ, "bird").

**Middle Persian Form:** sēn-murw

**Meaning:** In Iranian mythology, this proper noun refers to the simurgh, a legendary creature from Persian mythological tradition.

**Note:** The Wiktionary entry does not include an Avestan form or reference to mərəγō saēnō. The documented etymology traces the word to Middle Persian, with the folk etymology connecting it to the Persian words for "thirty" and "bird."
```


### [2026-09-06T16:02:24.352Z] TOOL RESULT

```
# Etymology of Chinch

**Chinch (noun):**
"Bedbug," first documented in the 1620s, derives from Spanish/Portuguese *chinche* (with diminutive *chinchilla*) meaning "bug." This term traces back to Latin *cimicem* (nominative *cimex*), meaning "bedbug," though the Latin word's origin remains uncertain.

**Cimex:**
The webpage does not provide an independent etymology for *cimex* beyond noting it as a Latin term of "uncertain origin."

**Spanish chinche/Latin cimex connection:**
The Spanish and Portuguese word *chinche* directly descends from the Latin *cimicem*, establishing a clear linguistic lineage from classical Latin through Romance languages into early modern English.
```


## [2026-09-06T16:02:35.131Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HJB siyah-gosh ===\" && grep -n -i \"siyah.gosh\\|syagush\\|siyahgosh\" HJB.txt AID.txt FSD_vol4.txt WEB_vol1.txt 2>/dev/null | head -10; echo \"=== cimex in LEW/LAT ===\" && grep -n \"cimex\" LEW_1910.txt LAT.txt | head -10",
 "description": "Hobson-Jobson siyah-gosh; Latin cimex"
}
```


### [2026-09-06T16:02:35.241Z] TOOL RESULT

```
=== HJB siyah-gosh ===
=== cimex in LEW/LAT ===
LAT.txt:11821:cimex
LAT.txt:11865:cimex, -icis 1,: punaise. Deja dans Liv.Andr.M.L.1915.
LAT.txt:33243:pulex, cimex) v. Ernont, Philologica, p.141.
LAT.txt:50921:le suffixe cimex, culex.
```


## [2026-09-06T16:02:38.729Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '11855,11880p' LAT.txt; echo \"=== WLD kei colour ===\"; grep -n \"cimex\" WLD_band3.txt incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head",
 "description": "Ernout-Meillet cimex; Walde-Pokorny"
}
```


### [2026-09-06T16:02:38.801Z] TOOL RESULT

```
q.u. Comme le meme verbe eat invoque pour expliquer furcilla, axilla,
on peut se demander ai ce n^st pas une creation f aite de toutea pibces.
Cf. Funck ALLG 4,844, et Thes. s.u. Toutefoia, d'aprbs M.L.1914, cer-
tainea formes dialectalea italiennes remonteraient a *cillicare (?).
cil5, -onis m.: - cui frons est eminentior ac dextra sinistraque
uelut recisa uidetur, P.F.38,4. Diminutif: cilunculus dans Arn. 3,14.
Surnom romain en -o, -onis-, cf.chZlo, capitS, etc., peut-etre d'origine
etrusque; cf. Ernout, Philologica, p.48.
ciloter, -tri m. : bourse, sac, musette. Emprunt au gr.
avec changement de declinaison, d'origine populaire.
cimex, -icis 1,: punaise. Deja dans Liv.Andr.M.L.1915.
Derives: clmicia f.: coris (piant e), cf. gr. xup IC, xoptov; cimico,
KOpii'w (Gloas.). Cf. M.L. 19x6 cimicella.
Mot populaire. Meme suffixe que dans culex, pulex', v. Ernout, Philo-clmussa
- .316 -
logica, p.141 et a.
Sans etymologie, comme la plupart des mot9 de ce genre.
clmussa (st-),-ae f. (Gloss.): corde. M.L.1917. De la: cinusso,
-as (sT-J: ceindre d'une corde, et aes derives; cimussator (si-)
"ae 1,porrriC cavou rj aXXov rivos UYP 0U "> CGL II 431,54; cimussdti 5 . Mot
non latin, d'origine inconnne. Lea gloses ont en outre ci mussator:
vjup.uQi.amjC qui, si la lefon est correcte, est a rapprocher de yt,|iu0t,ov,
\|/ iottjS . Mais peut-etre fait-il lire cerussator, cf. Thes. s.u.
cincinnus, -I m.: boucle de cheveux; vrille. Sans doute emprnnt
au gr. KUL VVOC • De j A dans Plaute. Rare, mais a subsisti dans la 1 . de
l'^glise. De la: cincinnatus: eimXoxalioS; cincinnalis,-is f. : polytric
=== WLD kei colour ===
incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt:46347:contronen „cimex‘, mbret. controunenn, nbret. contronenn ,,ver de viande“
```


## [2026-09-06T16:02:49.040Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && grep -n \"keng-\\|hakan-\\|kog[uü]tĭ\\|kogŭtĭ\" WLD_Bd1_1930_dli_70244_djvu.txt | head -10; echo \"=== kei colour ===\"; grep -n \"syāva\\|śyāva\\|syava-\\|kei-ro-\\|koi-ro-\" WLD_Bd1_1930_dli_70244_djvu.txt | head -10",
 "description": "Walde-Pokorny Bd1 keg- and kei- colour"
}
```


### [2026-09-06T16:02:49.115Z] TOOL RESULT

```
24048:kt'^r-. keng-, kek-, kenk- 
24051:keg-, keng- und kek-, kenk- etwa kleiner Pflock, bes. zum Aufhangen, 
=== kei colour ===
22722:(*koi-ro-) — alid. as. her „wiirdig, erhaben“ (ursprgl. von ergrauten Mannern), 
22769:Ai. gya-va- „schwarzbraun, dunkel", av. syava- „schwarz“, np. siyah
```


## [2026-09-06T16:02:52.442Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && sed -n '24045,24075p' WLD_Bd1_1930_dli_70244_djvu.txt; echo \"-----\"; sed -n '22705,22790p' WLD_Bd1_1930_dli_70244_djvu.txt",
 "description": "WLD keg- and kei- colour entries"
}
```


### [2026-09-06T16:02:52.503Z] TOOL RESULT

```
382 


kt'^r-. keng-, kek-, kenk- 


keg-, keng- und kek-, kenk- etwa kleiner Pflock, bes. zum Aufhangen, 
Haken, Henkel 1 *, Ygl. das iihnlicke kuk-, hunk-. 

(Cymr. cenglu „to form into hanks 1 * gehort wohl trotz Zupitza Gutt. 22 
zu den aus lat. cingulum entlehnten ir. cengal ,Fessel, Band 1 *, cenglaim 
„feBle", cymr. cengl „Band**), mir. al-cliaing „a rack for hanging-up arms 1 * 
(Stokes BB. "J5, 252); nas. lit. hinge „Haken, Klinke 1 *; (aber lett. kegii 
„Kriicke**, lett. k’eksis Haken, Bootshaken; Kriicke; Hakenlachs* 1 , k'enh'is 
,, Hakenlachs 1 wohl mit Assimilation des Auslauts an den Anlaut,miissen wegen 
des anlaut. li- entlehnt sein) ; norw. hake m. „Haken*‘, as. Itaco , ags. haca m. 
„Haken" (dazu anord. haka f. ,.Kinn“ nicht nach v. Grienberger L T nt. 1 07 
zu lit. kilklas ,. 1 lals 1 *), ags. hcecce f. ..Bisehofsstab 1 *; ags. hoc m. ,Jlaken ", 
mnd. It ok, huk m. ,,\Vinkel, Ecke, Vorgebirge**, anord. hpkja f. ( *h~>kiSn -) 
,, Kriicke* 1 ; ahd. hnko, huggo , nhd. Hake, Hikcn; nasaliert anord honk f., 
Itanki m. „Henkeh‘, mnd. hank ds. Zupitza Gutt. 22, 111, Fick III 4 66 f. 
Dazu vermutlich russ. kogoh „Klaue ; Fiinge des Raubvogels, gekriimmte 
Eisenspitze* 1 , osorb. kocht ..Dorn, Stachel des Schlehdorns, WeiBdorns'* 
(Berneker 53S) und (s. Falk-Torp u. hegle, kakke Lewy JF. 32, 160) mild. 
hechele, mnd. hekele „Hechel" (von den gekriimmten Eisenziihnen), norw. 
nidartl. hrkh auch „Stoppel“, hekel (und skjekel , anord. skekill (..Zipfel* 1 , 
ahd. heel tit ..Hecht 1 *, as. hncud, ags. hacod , hceerd „Hecht** (von den spitzen 
Ziihnen; Bed. - Parallelen bei Lewy aaO.), ahd. hecken „stecken"', hucko 
..uncinus, furca** f nicht besser naeh v. Grienberger Unt. 1 1 8 f . Kluge u. 
Haken zu got. holm ..Pflug**, s . kuk-); unrichtig, da arm. k- nicht = idg q-. 
ist Yergleich mit arm. kocem , liaue. schlage** (Seheftelowitz BB. 28, 296 , 
-----
besonders Bezzenberger BB. 27, 168 vereinigen unter einer versch. Wz. qdi- 
„sich gesellen, scharen“, got. usw. Jiaims mit lit. kiemas „Bauernhof“, Mimas 
„Dorf‘, lett. c'icms „Dorf, Yersammlungshau9 der Herrnhuter“, apr. caymis 
„Dorf‘, lit. kaimynas „Nachbar“, kaimene „Herde“ (die aber der Entlehnung 
aus germ. *haimaz verdiichtig sind nacb v. Grienberger SBAk. Wien 142, 
YIII 105, Uhlenbeck PBrB. 30, 286, bzw. westidg. Guttural haben konnen) 
und gr. y.d)/rtj „Dorf ;< , y.wjuog „Festgelage“ (ware qd[i]ma, -mo-) ; aber die 
gr. Worte sind auch anderer Deutung fahig (s. hem- „stopfen) und anord. 
ping-heimr ist keine Stiitze fiir die Gdbed. „sicb scharen“. 


2. kei- in Farbbezeicbnungen, bes. fiir dunkle Farben (s. aucli u. Jcor-). 

Ai. *rera- wohl in gerabha- m. Name verscbiedener Schlangen (Petersson 
KZ. 46, 128), vgl. unten clra- ,.Boa“. 

Mir. ciar „dunkel“ (* kei-ro -); anord. liurr, ags. liar „altersgrau, grau“ 
(*koi-ro-) — alid. as. her „wiirdig, erhaben“ (ursprgl. von ergrauten Mannern), 
Komp. *heriro , her(r)o „Herr“; ob hierher aksl. sen, russ. seryj „grau“, wo- 
neben mit schwierigem s- poln. szary , eech. serif „grau“ (nicht nach Uhlen- 
beck IF. 17, 97 mit ai. cya-md- usw. im Anlaut iibereinstimmend, s. dagegen 
Pedersen KZ. 40, 176f., der mit Reclit urslav. *chen postuliert, unter An- 
satz von idg. kh-, der aber am anders zu etymologisierenden gr. yoioog 
„Ferkek‘ keine Stiitze findet, s. Persson Beitr. 304 Anm. 1 ; Entlehnung 
aus germ. *yn iraz nimmt Meillet Et. 321 f., 403, Brugmann II 2 1, 349 an; 
u. zw. furs Westslavische mit Recht(?), nicht aber furs Gesamtslavische, 
da das in der Bed. isolierte poln. siara „Schwefel‘ : und „Biestmilch“, tech. 
sira „Schwefel“ = aksl. sira ds. altes si. s -, nicht *ch- fortsetzt, also der 
Uberwucherung durch das entlehnte(?) *clien entriickt blieb; Bruckner 
KZ. 45, 48 leugnet jeden germ. EinfiuB, ohne das westslav. s- zu be- 
griinden)??. 

Slav, srro kann auch nicht als *keros mit ai. gard- „bunt, seheckig" und 
(Prellwitz BB. 30, 176, dock s. auch u. kero-) gr. xrjQvkog „ein Meervogel“ 
gleichgesetzt werden, wenn auch diese als dehnstufiges *ke\i\ros aufgefaBt 
werden konnten (Petersson aaO.); eine schwundstufige Form (Prellwitz, 
Petersson aaO.) scheint y.iQoog „gelb“ (qo wohl kurznamenartige Gemi- 
nation), yJoar/'og * akiom^ lies. Aksl. s ? (h> „grau‘ (tech. sedy ds., lautge- 
setzlich aus *choid-) konnte aus sG'z nach smedh „bla6“, bledz „yX(OQog'‘ 
umgebildet sein fYiedermann IF. 37, 146; es hat wenigstens, trotz Peters- 
son aaO., an gr. yJdacpog „Fuchs“ keinen auBerslav. Anhalt). 

Ags. lice i urn „blau“ ( *haiwim -); unsicher ist die Herleitung von got. 
hiici n. ,,Schein, Aussehen“, anord. hy n. „Flaum, IIiirchen“, norw. hy 
..Flaum, Rauheit; Schimmel“, schwed. hy „Gesichtsfarbe“, ags. heuw , hliv 
Erscheinung, Gestalt, Farbe“ (hlwian „sich stellen als ob, lieucheln“, siehe 
auch Falk-Torp u. hykle), engl. hue „Farbe“ (B. bei Fickll 4 96) aus idg. 
*ki-un- unter Yergleich mit mir. cVo m. „Nebel“, gen. ciach , acc. ciaich, aus 
*kiuok-, s. Falk-Torp u. hy mit Lit., Pedersen KG. II 100 (es kommt fur 
hiici usw. auch eine Gdbed. „IIaut als deckendes c< in Frage, vgl. norw. 



mdartl. hya „diinne Sehicht, diinne Haut“, hya av „aufklaren, von emer 
Wolkendecke befreit werden“; Zupitza Gutt. 207 vergleicht ai. chavi „Haut, 
Farbe, Schonheit", vgl. zur Bed. lat. color zu kel- „bergen, decken“, doch 
ist dessen Et. ganz fraglich, s. Wackernagel ai. Gr. I 155; die germ. Worte 
eber zu sqeu- „bedeeken“, wie das von Noreen Ltl. 205 mit an. hy „Flaum“ 
verglichene an. shy „Wolke, bedeckter Himmel“. 

Daneben eine erweiterte Wzf. 

hl~ . 

Ai. gya-va- „schwarzbraun, dunkel", av. syava- „schwarz“, np. siyah 
„schwarz‘, arm. (wokl iran. Lw. ; s. auch Brugmann I 2 794) seav „dunkel, 
schwarz“ (s. Bartholomae Airan. Wb. 1631); reduktionsstufig lit. szyvas 
„wei£Slich, scbimmelig (von Pferden)“, apr. sylvan „grau“, aksl. sivu „grau“, 
russ. sivyj, serb. siv ds. 

Ai. gya-md- „schwarzgrau, schwarzgriin, schwarz“, gydmaka- „dunkelfarbig“ 
= av. sydmaka- m. „Name eines Berges oder Gebirges ‘(auch sama- „schwarz“ 
mit s- aus sy-, Bartholomae Grdr. d. iran. Phil. I 37, Airan. Wb. 1571); lit. 
szhnas „blaugrau, blau“; reduktionsstufig ki-mo- wahrscheinlich (nach Prell- 
witz BB. 30, 176) in lat. clmex „Wanze“ („dunkelfarbig“; Formans -co-, als 
Subst. nach der kons. Deck wie sene-x zu idg. *seno-s; Yf. LEWb. 2 s. v.). 
vielleicht im EN. Klycov. 

Aksl. shift, russ. slnij „dunkelblau“ ; auf einer andern Wzf. Iciei- scheint 
ai. cymi f. (wozu m. cyeta- wohl erst nach cm : Eta- „bunt“, 7 larita- 
usw. und gvetd neugeschaffen ; Brugmann II 2 1, 215) Farbbezeichnung 
(„wei£>, schwarz, blau?“) und die nach der Farbe benannten ai. gyend- m. 
„Adler, Falke“, av. saena- „ein grofier Raubvogel, wohl Adler“ (s. auch 
n.*kp'mo-) zu beruhen; oder ist ein urar. *^u2na- nach *aina- „bunt“ zu 
urar. siaina- ge worden?
```


## [2026-09-06T16:03:05.158Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '4795,4815p' PHD.txt; echo \"=== syah in PHD ===\"; grep -n \"syā\\|syah\\|sy'\\b\" PHD.txt | head -20",
 "description": "MacKenzie sen murw and syā"
}
```


### [2026-09-06T16:03:05.344Z] TOOL RESULT

```
-
da
z
I
5
166
sahmgen sahmgenih sāstār
sāstārīh
rawen-! rawenidan! rawiánt raftan! saxtag sabz
šast”
sī
haštād* sagēn nawad* sēn
sēnag
sen murw sezd sézdén haftād*
darr-t
PAHLAVI KEY
— AA Sri 33
süxtarih saxtih
saxt
saxtan, saxtan süg, sak say- sahigih sahig, sivag sas
зап
=== syah in PHD ===
221:aswār [252002/, ?shw'l | N suwār] horseman, rider. ~th: horsemanship, riding. āsyāb [?sy?5] (water-)mill. āsyāg [sy’k!' | N asya] mill(-stone). aš [P$] the evil eye. āšixtan, āšinj- Pšyhtn!, ”*šnc- | P ?fyxt] pour, flow, overflow. aškamb [KLSE < A krs’; ”$kmb! | M *fkmb, N šikam] belly, womb. ~ag [-k! | N šikamba] = aškamb. āškārāg (34 1Q)k! | M sq?rg, N āškārā] obvious, evident. ~ih: revelation, confession. aškaragënidan [$k*Pkyn-ytn!] reveal, confess. aškūb рор | N dškē(b)) roof, ceiling. aškom(b) [’skwm(b')] = a$kamb. ašmā [LKWM < А l-kwm | MO fm'(h), N šumā] you (?1.). āšnāg Pwk! | M ”šYg, N ama] known. āšnawāģ [?$nw?k! | M ?snz?g, N šunawā] hearing. —ih: (sense of) hearing. āšnūdan, āšnaw- [OSMEN-tn! < А « ўт; топі | M? fnwdn, ?fnw-, N funüdan, funaw-] hear, understand. ~išn: hearing. або [šwk! = Av. ašawa] righteous. āšūb [>р | P swb, N ~] disturbance, turmoil. Aštād [s?t! | Md, N ~] the goddess Rectitude; cal. 26th day. aštag [štk'] messenger. ~th: mission. aštar РД whip. āštīh Pštyh | M 7st, N āštī] peace. Ašwahišt Piwhst'] = Ardwahišt. āšyān(ag) ['syd?n(k) | (M ?hy*ng), N ašyana] nest, lair. ātaxš Pths = Av. ātarš | N ātaš] fire. āwādaģ Pwb'tk! | J ?zo?d] generation. āwahan [wb’hn'] fortified place, stronghold. амат ['wbm | M ?w^m] time, season. -āwand [ла | M 2w(y)nd] suffix forming adjectives of quality. awar [LPNME < A I-pn-h | M ?wr] hither! come! awar-, v. āwurdan. a-wardàg ['wit?k&!] undeviating. a-wardisnig [?wltsnyk'] immutable. Аһ: immutability. āwarišn [zoblfn! | M *wryšn) abode, home. a-warzid [Pwicyt'] untilled. *Aiwas-, v. tāwištan. ама [Pc | N ~] voice, sound. a-wazisnig ['wcfnyk!] immobile. āwēnīdan, āwēn- ['wyn-ytn! | (P ?bzoyn-)] admonish, blame. ~i$n: blame, reproach.
292:*brinj [binc | (M bryng), N birinj] bronze, brass. ~én [-yx!] bronze, brazen. brinómand [blyn’wmnd] delimited. brištan, bréz- [blystn', blyc- | M bryz-, N biristan] roast. brüg [blwk' | M brwg, N abrü] (eye)brow. büdan, b(aw)- [YHWWN-tn! < A yhwwn, У hwh; bwtn', b- | M bwdn, bw-, N büdan] be, become. bawišn: becoming, genesis. büf [bwp | N <), *büg [bwk'] owl. buland [bwind | = M, N ~] high. būm [bwm | N ~] land, earth, country. ~-€andag [-cndk'] earthquake. Ibun [bwn' | = M, N ~] base, foundation, bottom. *bun [bwn! | N ~] = wan. bunag [bznk! | N ~a] baggage; abode, camp. — daštan: dwell, settle. bun-dahišn(īh) [bzundhšn!, -yh] primal creation. bunih [bwnyh] beginning. buništ [bwnyst! | = M] foundation. ~ag [-k'] principle. bun-kadaģ [bwnktk'] original house, home. bun-xān [bwnh?n'] source. bur-, —išn, v. buridan. burāģ [bzoP RU] cutting, sharp. burām-, v. bram-. burd [bwit! | M bwrd] patient. ~ih: patience. burdan, bar- [Y BLWN-tn! < А У ybl; bwltn', bl- | M Бата, br-, N <] carry, bear, take, endure. ~išn: bearing, behaviour. burdār [bwit!]] bearer; womb. ~ih: patience. burd-ešnēhr [bwit! fnwhl | P bwrdyfnwhr] grateful, thankful. burg [bwig | (Ar. burj)] tower. buridan, bur- [bwl-ytn! | M bwr-, N ~] = bridan. —j$n: cutting. Burz [bwic] the god of agriculture. Burzénmihr [bwlcynmtr!] the third major Fire of Sasanian Eran, that of husbandmen. burzidan, burz- [bwlc-ytn'] praise, honour. ~i$n: praise, honour. —iŠnié : praiseworthy. buš [ро | N ~] mane. būšāsp [bwPsp | M bwsy'sp, N ~] sleep, sloth; dream. * but [bwt! | = M, N ~] Buddha; idol. buz [AZ < A ‘z; Бос | N ~] goat.
628:wasyār [wsy(k)l | N bisyār] much, many.
2727:many was, wasyār; so -- and, čand.
2808:mill (n.) āsyāb, asyag.
2812:millstone āsyāg.
2869:much abēr, frāy, freh, was, wasyār; as — as, however — and čand; so — and, čand.
3288:pupil hašāgird, hāwišt; (of eye) syahag, tidag. pure abézag, agumég, āsnūd(ag),
4335:womb a$kamb(ag), aškom(b), burdār, gabr, grāb, pusyān, uruspar, zahār.
4704:purrmāh Ku purrsardag 15 Qa» yes dahint roe to pusyān V 10 pusar ND 10 póstén V yen 10) póst we» 105 рап}, poz So panjah ay S ya) panjag, pēzag 13619 pos- = 74010 pūšīdan Wres“O ve pēšišn VUV puštībānīh «U ye) 43 «650105 pustiban т^” оу S ANA pušt VOU 199 puštag 1100010) püdagih ^t 5120
4829:7.35 giyāh, syā AQA35
```


## [2026-09-06T16:03:11.301Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"sēn murw\\|sen murw\\|Simurgh\\|simurgh\\|sēnmurw\" PHD_mackenzie.txt PHD.txt NYB_vol2_glossary.txt | head -10; echo \"=== syā black ===\"; grep -n \"black\" PHD_mackenzie.txt | head -10",
 "description": "MacKenzie sen murw and syā black"
}
```


### [2026-09-06T16:03:11.382Z] TOOL RESULT

```
PHD.txt:3661:simurgh sén-murw.
PHD.txt:4808:sen murw sezd sézdén haftād*
NYB_vol2_glossary.txt:3430:hypothesis that we have to do with OP *oi- — NW (Av. 1645) sri- (Bthl srāy-) "beauty, splendour’ = Kkr sri- ‘splendour, majesty’, also personified as the goddess of beauty, of fortune, or of sovereign power; Milr *si(y) alternates freely with sih according to the common rule. This divine power is apparently miaterialized in some animal which is said to be very stout (71%), the most beautiful imaginable (718-18), very big and brisk (87%). In the Sn, where the episode is told at length (Book 21, v. 231 sqq., Tehr 4, p. 1697- 98 — Mohl V, p. 288), it is said to bea ram (yurm), but deseribed as a guite mythical, mysterious being: “I have not seen its equal painted in any palace”, one of the witnesses says, “with wings as Simurgh, with a tail as the peacock, like a flash of lightning, bold of head and ears and hoofs, purple-coloured, swift as the wind, in its way it does not remind of a ram at all". The conjecture varrak, adopted by Nöldeke and Antiä, robs the narration of the air of divine mystery essential to it. Sanjana’s remarks are worthless. — OP *ei- is also attested in NP séy ‘beautiful, elegant, excellent’ < MiPrs *sēk < OP *cayaka- for NW *srayaka- from Av. (1638 sg.) srayan- ‘beauty’ and ‘beautiful’; in a pejorative sense in NP sihah ‘harlot’ < MiPrs *sthak; possibly also in NP siyäb, whose meaning is, however, somewhat uncertain (v. Steingass and BQ). — It is not all too difficult to guess why the scribe chose such a strange way of writing this w.: by spelling it phonetically he would have got a very ambiguous and polyphonic graphic symbol. His spelling 30 guaran- teed safe reading. Certainly this is be- wildering for us who read with our eyes, but in antiquity all texts were intended to be perceived by ear. Cf also s. v. nist.
PHD_mackenzie.txt:4488:sanlt                                74                         sen murw
PHD_mackenzie.txt:7586:simurgh sen-murw.                                xwurd; ....., thing xwurdag.
PHD_mackenzie.txt:9065:sen murw               \ t6 K»          salag
=== syā black ===
930:                  ....,gar [-kll N ....,] blacksmith.
4725:sya [syd) I (P sy)w, N siyah)] black.
6042:beer wabg.                                  black sya.
6043:beestings frosag.                           blacksmith ahangar.
```


## [2026-09-06T16:03:15.451Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '4486,4495p' PHD_mackenzie.txt",
 "description": "MacKenzie sen murw entry"
}
```


### [2026-09-06T16:03:15.506Z] TOOL RESULT

```
sam6r [smwl IN .....] sable (marten).
SaD [$)n l IN ......] kind, manner.
sanlt                                74                         sen murw
sang [KYPA < A kyp'; GGA (in error); sng I (P 'sng), N -] stone, rock.
 -sar [·s'l] stony place.
sanJ-, v. saxtan.
sanwar [snwl = Av. 8anwar-] bow.
sar [LOY8E < A T'lh; sll M ST, N -] head; top, summit; end, begin-
  ning.
sarasar [sl'sl I N -..] from end to end.
```


## [2026-09-06T16:03:19.181Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"sen murw \\[\" PHD_mackenzie.txt | head; grep -n -A2 \"^sen \\[\" PHD_mackenzie.txt | head; grep -n \"sen \\[syn\\|sen murw \\[\" PHD_mackenzie.txt | head; awk 'NR>=4500 && NR<=4530' PHD_mackenzie.txt",
 "description": "MacKenzie sen entry text"
}
```


### [2026-09-06T16:03:21.161Z] TOOL RESULT

```
sarenidan, saren- [s'lyn-ytn ] provoke.
                                 '
sargen [slgyn l I N sargin] dung, manure.
sarmag [slm'k ' 1 N sarma] coldness.
sarw [slw(b) I M srw, N .....,] cypress.
                    1

sas [s's N -..] bug.
          1

sastar [s'st'll P s'st'r] commander; tyrant.
 -ih: tyranny.
Sawah [sw'h = Av. sawahi-] the western continent of the earth.
saxt [s(')ht N -] strong, hard, severe(ly); very.
                1
                '
 .....,ih: strength, severity.
saxtag [shtk ' I (N saxtiyan)] morocco leather.
saxtan, sanj- [s'htn ' , sne- 1 N -] weigh.
saxtan, saz- [s'htn', s'e- 1 (P s'e-), N .......] make, prepare; tolerate.
saxtarih [s'ht'lyh] toleration, forbearance.
saxwan [MRYA < A mly'; shwn l 1M sxwn, N suxan] word, speech.
say-, v. sudan.
sayag [s'dk 1 M s'yg, N saya] shade, shadow.
                  '
lsaz- [se- 1 M      SZ-, N .......] be fitting, proper, worthy.
 -isn(ih): fitness, worthiness.
2saz-, .......isn, v. sazistan.
saz-, v. saxtan.
sazag [se'k I N saza] fitting, worthy.
 -ih: fitness, worthiness. .'
```


## [2026-09-06T16:03:25.153Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"murw\" PHD_mackenzie.txt | head -20",
 "description": "MacKenzie murw entries"
}
```


### [2026-09-06T16:03:25.219Z] TOOL RESULT

```
2331: fral(a)murw [pllmwlw I M frlymwrw] peacock.
2953:hu-murwag [hwmwlw)k ] auspicious.
3253: -(ag) murw [_kl I N kaskina] ·magpie.
3614:murw [mwlw l I M mWTW, (N mUTY)] bird.
3615:murwa~ [mwlw'k I M mwrw', N murwa] omen.
3617:murwizag, [mwlwyck ' ] little bird.
3618:murw-nis [mwlwnyl] augur, soothsayer.
4488:sanlt                                74                         sen murw
4542:2Sen murw [synmwlw 1 (N simury)] a fabulous bird.
6018:augur murw-nis.                             nibardidan; v. fight; doing
6019:auspicious humurwiig.                       ardikkarih.
6032:beat koftan, kostan, zadan.                 bird murw, way, wayendag; little ....,
6033:beautiful hu6hr, nek(ag).                       murwizag; ,..., of good omen humiiy;
7011:   zi(w)isnomand.                        magpie kiisken(ag) murw.
7170:11Obody kas·iz.                        omen jadag, Jahisn, murwag.
7222:overstep spoxtan.                      peacock fras(a)murw.
7586:simurgh sen-murw.                                xwurd; ....., thing xwurdag.
7624:slackness sustih.                             soothsayer ked, kundig, murw-nis.
8592:                            -c.. V      frasamurw                 ~~Q)
9065:sen murw               \ t6 K»          salag
```


## [2026-09-06T16:03:27.679Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '4538,4546p' PHD_mackenzie.txt",
 "description": "MacKenzie sen entries"
}
```


### [2026-09-06T16:03:27.718Z] TOOL RESULT

```
 .....,omand [-'wmnd 1 N -mand] dangerous.
sel [s/ IN.....,] spear, javelin.
sem [sym I N -] = asem.
lSen(ag) [syn(k) I I N sinal breast, chest.
2Sen murw [synmwlw 1 (N simury)] a fabulous bird.
se-pay                            75                             spas
se-pay [3-p)d I N sipa] three-legged.
sir, v. sagr.
se-Aabag [3-fph l ] three-night-Iong, trinoctial.
```


## [2026-09-06T16:03:36.329Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SNS syah ===\" && grep -n \"syā\\|siyā\\|sy'\\|black\" SNS.txt | head -20",
 "description": "Shayast ne Shayast glossary syah"
}
```


### [2026-09-06T16:03:36.379Z] TOOL RESULT

```
=== SNS syah ===
13433:.Y/Tl^-n^sy'g :^«V {Mir. Man. 1,42) ra'hyg ,
```


## [2026-09-06T16:03:37.957Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AFM sanj ===\" && grep -n \"صنج\" AFM.txt TAD.txt ARB_mo3rb.txt ARB_abdulraheem.txt 2>/dev/null | head -20; echo \"=== LKT sanj/chang ===\"; grep -n -i \"sang\\b\\|çeng\\|tschenk\\|Harfe\" LKT.txt | head -10",
 "description": "Arabic sources for sanj"
}
```


### [2026-09-06T16:03:38.028Z] TOOL RESULT

```
=== AFM sanj ===
TAD.txt:1778:أماه سنج » الفارسي شعناه الوازن . الظاهر أن افظ صنج ج صنو ج هو حر بف 
ARB_mo3rb.txt:2695:ولا * 6 الصراد ابم فى كامة عس بية ٠‏ من ذلك « م » و« الصنجة » 0 
ARB_mo3rb.txt:6915:والتاى نع وبربط ذى 1 0 والصنج بك توه أن نوضعا 
ARB_mo3rb.txt:6940:)600 ”*اأنأى ترم “> و*”الصنج ' "هن آلات الملاهى 3 وسيذ كرات ف موضعيهما 2 الاب 6 2 باب 
ARB_mo3rb.txt:15992:والناى رع و بربط ذى 3 د والصنج ببكى توه أن يوضعا 
ARB_mo3rb.txt:15998:ملاوة ع كانى * ضار ب صنجى سمو ةمغن 
ARB_mo3rb.txt:16014:راد فى الصنج 93 4# 3 الله وار ا 
ARB_mo3rb.txt:28204:صنجة 598646:89؟:١‏ 
ARB_mo3rb.txt:28216:صنجح 6551:15٠١‏ 0:58861:15565ه 
=== LKT sanj/chang ===
928:[Aus  chiues.  fan-seng  'religiöse  Person, Priester',  jetzt  meist  ho- sang  genannt] 'Mönch,  buddhistischer  Priester  mit  ge- schorenem Kopfe'.  Hieraus  engl,  honze, frz.  honze,  dtsch.  Bonze  als  Bezeichnung für  fanatische  Geistliche  jeder  Religion, dann  übertragen  'ein  hochtrabender, stolzer  Mensch',  schließlich  'Fanatiker seiner  Überzeugung',  z.  B.  Parteibonze. [Birth  ChinFW  200.  Hobson-Jobson 105.    Kluge  63.
1059:39-2.  Fers,  cäng: 'Harfe,  Laute',  ar.  nang  'pers.  Harfe, Leier'  [KM  II.  1161,  3];  hieraus  mit  ar. Art.  Asangue  'Sternbild  der  Leier,  Lyra'. [Devic  DEt  41.
1851:a)  Mit  ar.  r-äs  'Kopf  [s.  hier  Nr.  1701] wird  ar.  habb  ar-räs  Delphinium  staphi- sagria,  eine  Ranunculacee,  der  Päonie verwandt;  hieraus  sp.  abarraz,  albarraz 'scharfer  Rittersporn ;  Läusekraut' ;  pg. paparaz,  peparrds  'Samen  vom  Läuse- kraut' [Constancio  Dicc  742  b] ;  vgl. DE  31.
3792:'Banane,  Musa  paradisiaca'  [Pijn  168]; hieraus  zur  Bezeichnung  der  Banane dtsch.  Pisang,  ndl.  dän.  schwed.  pisang; frz.  pisang  (—  bananier).  —  [Dtsch.  Pi- sang  <^  frz.  paysan,  das  im  Kriege 1870/71  und  ebenso  im  Weltkriege  von den  deutschen  Soldaten  zur  Bezeichnung des  frz.  'Bauern'  benutzt  wurde,  hat natürlich  mit  diesem  mal.  Grundwort nichts  zu  tun.]
4190:'Art  Tanz  und  Gesang'  [aus  pers.  sär •Kopf,  s.  hier  Nr.  1841  und  band,  Prä- sensstamm zu  bästän  'binden',  s.  hier Nr.  212,  ähnlich  gebildet  wie  dästähänd aus  däst  'Hand',  ein  Tanz  bei  den  Be- duinen]; hieraus  engl,  saraband,  sara- bände;  it.  sarabanda,  frz.  sarabande, sp.  zarabanda,  pg.  sarabanda.
4412:1955.  Ar.  snrta: 'Polizeimann';  hieraus  siz.  scmia,  (alt) zurta 'Nachtwächter, Nachtwache;  nächt- licher Gesang'.    [ZfromPh  XXXV,  440. GrSVociSic  245.    ML  7717.
4766:Eigentlich  'Holz',  dann.  'Instrument  aus Holz'  >  'Laute,  Zitlier';  hieraus  mit verschmolzenem  ar.  Art.  it.  Uuto,  liudo, afrz.  leüt,  frz.  luth.  sp.  laud,  pg.  alaude, rum.  lautä;  ndl.  luit,  engl,  lute,  dtsch. Laute;  [über  tk.  lauta,  ICi'uta  Kelekian KämQs  1073,  das  wie  ngr.  \aoöTa  aus dem  Rum.  kommt]  bulg.  lauta  'Geige', serb.  Icut  'Laute',  klruss.  lavuta  'Laute, Geige;  Dummkopf,  l'utn'a,  russ.  Ijtitnja, poln.  lutnia,  öech.  loutna  'Laute'.  —  Wie die  Laute,  das  Begleitinstrument  der Lieheslieder,  aus  dem  islamischen  Orient zu  uns  gekommen  ist,  so  ist  wahrschein- lich der  mittelalterliche  Minnegesang überhaupt  orientahschen  Ursprungs; darüber  vgl.  Konrad  BURDACH  in Sitzungsberichte  der  Preufs.  Akademie der  Wiss.  1918.  Nr.  XLV,  S.  994/1029 u.  Nr.  XLVHI,  S.  1072/1098.  [DE  60. ML  388.    Bern  SlEtWb  696.
6665:percal(ine)  1632 Percival  592 jo^rt  1B34 perkal  1632 pitunsi  1609 pdttmze  1609 pharaon  1650 ^fe^ci  596 pikotil  1655 j)i7a^  1656 2)«7aM  1656 pisang  1659 pistache  1664 pomme  d'Adam  19 potiron  623 poutargue  274 pr(a)o  1651 Pyramide  1457
7630:papoea  1669 pacha  1640 pasch  1652 pisang  1659
9785:Dänisch. Adatnsäble  19 daddel  465 ^/  605 filsben  605 gingang  722 gongon  558 gutta-perka  712 hurra  2167 jonke  753 kasuar  1119 kavring  1282 krahask  1279 kumnien  1046 lazaret  1310 maske  1436 papegöie  147 pisang  1659 rai;  1004 r»-s  1723 rotting  1724 sukker  1855.
```


## [2026-09-06T16:03:45.002Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '1770,1790p' TAD.txt",
 "description": "TAD sanj entry"
}
```


### [2026-09-06T16:03:45.057Z] TOOL RESULT

```
صلصا ايطالى 152ه5 وهو الب" يٌصنم منالتوابل والابازير ودقاق السمك 
والبندورة 

فارركارانن 57 

صِئاب خردل بوناني أم06ز5 معناه خردل 

صل لاتيني سالدفسك أصله وثاني :ده021ه)! معناه جوف فى وسلله 
أماه سنج » الفارسي شعناه الوازن . الظاهر أن افظ صنج ج صنو ج هو حر بف 
لقي امور لعي ي أي صنواج وهو مشتق من صلصل العربى أي صوات 

صدم 0 معئاه شبال ولي الارابية سف معئأة 
مثال وفي كلتا اللغتين براد به الوآن 


' ل 

فو بس وشوبك وشويق - فارسى « جوب وحوبه » معناه عصا رقق 

بها العجين مر أدفه مسطح وملطاط ومطلة وسور
```


## [2026-09-06T16:03:59.777Z] TOOL CALL #72: Bash

```json
{
 "command": "ls site/pages/247.jpg 2>/dev/null; pdftoppm -f 247 -l 247 -r 150 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg247 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/",
 "description": "Render PDF page 247"
}
```


### [2026-09-06T16:04:02.030Z] TOOL RESULT

```
site/pages/247.jpg
total 9244
drwx------ 4 sfmqrb sfmqrb    4096 Sep  6 12:04 .
drwx------ 4 sfmqrb sfmqrb    4096 Sep  6 10:51 ..
-rw-rw-r-- 1 sfmqrb sfmqrb    1056 Sep  6 12:03 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  180887 Sep  6 11:56 bqt1637_fn.png
-rw-rw-r-- 1 sfmqrb sfmqrb   50592 Sep  6 11:56 bqt1637_kaz.png
-rw-rw-r-- 1 sfmqrb sfmqrb   92182 Sep  6 10:55 bqt1854.png
-rw-rw-r-- 1 sfmqrb sfmqrb   66580 Sep  6 10:57 bqt2023.png
-rw-rw-r-- 1 sfmqrb sfmqrb   69965 Sep  6 11:25 bqt2242crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb   28189 Sep  6 11:25 bqt2417crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb  431133 Sep  6 11:16 bqt2420_fn.png
-rw-rw-r-- 1 sfmqrb sfmqrb    9548 Sep  6 11:25 bqt2meta.json
-rw-rw-r-- 1 sfmqrb sfmqrb   81018 Sep  6 11:16 build213.py
-rw-rw-r-- 1 sfmqrb sfmqrb   67391 Sep  6 11:49 build225.py
-rw-rw-r-- 1 sfmqrb sfmqrb   71757 Sep  6 11:47 build232.py
-rw-rw-r-- 1 sfmqrb sfmqrb   49952 Sep  6 11:57 build234b.py
-rw-rw-r-- 1 sfmqrb sfmqrb   32265 Sep  6 11:51 build234.py
-rw-rw-r-- 1 sfmqrb sfmqrb   24770 Sep  6 12:01 build243.py
-rw-rw-r-- 1 sfmqrb sfmqrb    6504 Sep  6 11:13 c1.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3402 Sep  6 11:22 c224_n10.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4812 Sep  6 11:28 c224_n12.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4744 Sep  6 11:22 c224_n1.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3203 Sep  6 11:28 c224_n7.png
-rw-rw-r-- 1 sfmqrb sfmqrb   12820 Sep  6 11:27 c229_bibua.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5308 Sep  6 11:27 c229_greek.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5313 Sep  6 11:27 c229_persian.png
-rw-rw-r-- 1 sfmqrb sfmqrb    9059 Sep  6 11:50 c237_n18.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2389 Sep  6 11:50 c237_n3.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4987 Sep  6 11:52 c239_kandid2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4734 Sep  6 11:52 c239_kandid.png
-rw-rw-r-- 1 sfmqrb sfmqrb   12852 Sep  6 11:52 c239_persian.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4087 Sep  6 11:52 c239_sandarus.png
-rw-rw-r-- 1 sfmqrb sfmqrb   15240 Sep  6 11:54 c246_caiique.png
-rw-rw-r-- 1 sfmqrb sfmqrb   36354 Sep  6 12:02 c246_casaque.png
-rw-rw-r-- 1 sfmqrb sfmqrb   84366 Sep  6 11:54 c246_n2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   51690 Sep  6 11:54 c246_n6.png
-rw-rw-r-- 1 sfmqrb sfmqrb   13719 Sep  6 12:02 c248_p3.png
-rw-rw-r-- 1 sfmqrb sfmqrb   30759 Sep  6 12:02 c248_p4.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2750 Sep  6 12:02 c248_persian2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3046 Sep  6 12:02 c248_persian.png
-rw-rw-r-- 1 sfmqrb sfmqrb    7793 Sep  6 11:13 c2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4371 Sep  6 11:13 c_gacele.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3485 Sep  6 11:16 c_harmathan.png
-rw-rw-r-- 1 sfmqrb sfmqrb   12347 Sep  6 11:20 c_hdr.png
-rw-rw-r-- 1 sfmqrb sfmqrb    9147 Sep  6 11:16 c_herman2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3841 Sep  6 11:16 c_herman.png
-rw-rw-r-- 1 sfmqrb sfmqrb   12691 Sep  6 11:20 c_ieuo.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2071 Sep  6 11:26 c_ijlak2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   14654 Sep  6 11:20 c_ijlak.png
-rw-rw-r-- 1 sfmqrb sfmqrb   12239 Sep  6 11:20 c_latis.png
-rw-rw-r-- 1 sfmqrb sfmqrb    6280 Sep  6 11:13 c_mag.png
-rw-rw-r-- 1 sfmqrb sfmqrb  169482 Sep  6 11:58 crop_1648b.png
-rw-rw-r-- 1 sfmqrb sfmqrb   45260 Sep  6 11:57 crop_1648.png
-rw-rw-r-- 1 sfmqrb sfmqrb  305924 Sep  6 11:57 crop_1731.png
-rw-rw-r-- 1 sfmqrb sfmqrb    6971 Sep  6 11:03 crop1.png
-rw-rw-r-- 1 sfmqrb sfmqrb    8619 Sep  6 11:03 crop2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5240 Sep  6 11:03 crop3.png
-rw-rw-r-- 1 sfmqrb sfmqrb   12820 Sep  6 11:05 crop_germ.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3408 Sep  6 11:05 crop_guthjo.png
-rw-rw-r-- 1 sfmqrb sfmqrb  111118 Sep  6 11:19 crop_habl.png
-rw-rw-r-- 1 sfmqrb sfmqrb    9001 Sep  6 11:05 crop_node12.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5564 Sep  6 11:05 crop_node1.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5286 Sep  6 11:05 crop_varathra.png
-rw-rw-r-- 1 sfmqrb sfmqrb   11652 Sep  6 11:13 c_xzn.png
-rw-rw-r-- 1 sfmqrb sfmqrb   83691 Sep  6 11:19 gen215.py
-rw-rw-r-- 1 sfmqrb sfmqrb    2303 Sep  6 11:25 j.json
-rw-rw-r-- 1 sfmqrb sfmqrb     228 Sep  6 11:06 jscheck.js
-rw-rw-r-- 1 sfmqrb sfmqrb   37376 Sep  6 11:09 mk201.py
-rw-rw-r-- 1 sfmqrb sfmqrb   77132 Sep  6 11:11 mk207.py
-rw-rw-r-- 1 sfmqrb sfmqrb   61121 Sep  6 11:11 mk208.py
-rw-rw-r-- 1 sfmqrb sfmqrb   80041 Sep  6 11:14 mk214.py
-rw-rw-r-- 1 sfmqrb sfmqrb   67513 Sep  6 11:27 mk217.py
-rw-rw-r-- 1 sfmqrb sfmqrb   74459 Sep  6 11:33 mk218b.py
-rw-rw-r-- 1 sfmqrb sfmqrb   17605 Sep  6 11:25 mk218.py
-rw-rw-r-- 1 sfmqrb sfmqrb   50138 Sep  6 11:24 mk222.py
-rw-rw-r-- 1 sfmqrb sfmqrb   78297 Sep  6 11:32 mk223.py
-rw-rw-r-- 1 sfmqrb sfmqrb   47928 Sep  6 11:38 mk224.py
-rw-rw-r-- 1 sfmqrb sfmqrb   53093 Sep  6 11:40 mk226.py
-rw-rw-r-- 1 sfmqrb sfmqrb   51303 Sep  6 11:39 mk228.py
-rw-rw-r-- 1 sfmqrb sfmqrb   29152 Sep  6 11:37 mk229.py
-rw-rw-r-- 1 sfmqrb sfmqrb   47535 Sep  6 11:47 mk230.py
-rw-rw-r-- 1 sfmqrb sfmqrb   64267 Sep  6 11:59 mk235.py
-rw-rw-r-- 1 sfmqrb sfmqrb   73422 Sep  6 12:02 mk237.py
-rw-rw-r-- 1 sfmqrb sfmqrb   81037 Sep  6 12:03 mk240.py
drwxrwxr-x 2 sfmqrb sfmqrb    4096 Sep  6 11:44 p216
drwxrwxr-x 2 sfmqrb sfmqrb    4096 Sep  6 11:52 p233
-rw-rw-r-- 1 sfmqrb sfmqrb   33321 Sep  6 11:51 part1.json
-rw-rw-r-- 1 sfmqrb sfmqrb   54688 Sep  6 10:58 pg201.png
-rw-rw-r-- 1 sfmqrb sfmqrb   70083 Sep  6 10:52 pg204.png
-rw-rw-r-- 1 sfmqrb sfmqrb   77858 Sep  6 10:52 pg206.png
-rw-rw-r-- 1 sfmqrb sfmqrb   67371 Sep  6 10:53 pg207.png
-rw-rw-r-- 1 sfmqrb sfmqrb   59146 Sep  6 10:53 pg208.png
-rw-rw-r-- 1 sfmqrb sfmqrb   53054 Sep  6 11:00 pg209.png
-rw-rw-r-- 1 sfmqrb sfmqrb   74515 Sep  6 11:02 pg211.png
-rw-rw-r-- 1 sfmqrb sfmqrb  141781 Sep  6 11:03 pg212hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   75961 Sep  6 11:02 pg212.png
-rw-rw-r-- 1 sfmqrb sfmqrb   83761 Sep  6 11:03 pg213.png
-rw-rw-r-- 1 sfmqrb sfmqrb   83752 Sep  6 11:01 pg214.png
-rw-rw-r-- 1 sfmqrb sfmqrb  194102 Sep  6 11:05 pg215hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb  117034 Sep  6 10:54 pg215.png
-rw-rw-r-- 1 sfmqrb sfmqrb   76564 Sep  6 11:13 pg216.png
-rw-rw-r-- 1 sfmqrb sfmqrb   82798 Sep  6 11:16 pg217.png
-rw-rw-r-- 1 sfmqrb sfmqrb  147278 Sep  6 11:13 pg218hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   82099 Sep  6 11:13 pg218.png
-rw-rw-r-- 1 sfmqrb sfmqrb   71937 Sep  6 11:19 pg219.png
-rw-rw-r-- 1 sfmqrb sfmqrb   63280 Sep  6 11:18 pg220.png
-rw-rw-r-- 1 sfmqrb sfmqrb   71497 Sep  6 11:18 pg221.png
-rw-rw-r-- 1 sfmqrb sfmqrb  118895 Sep  6 11:16 pg222hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   84108 Sep  6 11:16 pg222.png
-rw-rw-r-- 1 sfmqrb sfmqrb   79615 Sep  6 11:18 pg223.png
-rw-rw-r-- 1 sfmqrb sfmqrb   90848 Sep  6 11:22 pg224hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   55412 Sep  6 11:15 pg224.png
-rw-rw-r-- 1 sfmqrb sfmqrb   80963 Sep  6 11:32 pg225.png
-rw-rw-r-- 1 sfmqrb sfmqrb  161218 Sep  6 11:26 pg226hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   74322 Sep  6 11:19 pg226.png
-rw-rw-r-- 1 sfmqrb sfmqrb   54381 Sep  6 11:31 pg227.png
-rw-rw-r-- 1 sfmqrb sfmqrb   52519 Sep  6 11:25 pg228.png
-rw-rw-r-- 1 sfmqrb sfmqrb   78760 Sep  6 11:27 pg229hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   42112 Sep  6 11:26 pg229.png
-rw-rw-r-- 1 sfmqrb sfmqrb   65310 Sep  6 11:32 pg230.png
-rw-rw-r-- 1 sfmqrb sfmqrb   69894 Sep  6 11:34 pg231.png
-rw-rw-r-- 1 sfmqrb sfmqrb   67111 Sep  6 11:35 pg233.png
-rw-rw-r-- 1 sfmqrb sfmqrb   82071 Sep  6 11:44 pg234.png
-rw-rw-r-- 1 sfmqrb sfmqrb   47149 Sep  6 11:44 pg236.png
-rw-rw-r-- 1 sfmqrb sfmqrb  125593 Sep  6 11:50 pg237hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   67972 Sep  6 11:50 pg237.png
-rw-rw-r-- 1 sfmqrb sfmqrb  168221 Sep  6 11:52 pg239hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   81026 Sep  6 12:03 pg239.png
-rw-rw-r-- 1 sfmqrb sfmqrb   83594 Sep  6 12:03 pg239_small.png
-rw-rw-r-- 1 sfmqrb sfmqrb   81131 Sep  6 11:51 pg240.png
-rw-rw-r-- 1 sfmqrb sfmqrb   97613 Sep  6 11:49 pg242.png
-rw-rw-r-- 1 sfmqrb sfmqrb   80947 Sep  6 11:59 pg244.png
-rw-rw-r-- 1 sfmqrb sfmqrb   80632 Sep  6 11:55 pg245.png
-rw-rw-r-- 1 sfmqrb sfmqrb   79253 Sep  6 11:54 pg246.png
-rw-rw-r-- 1 sfmqrb sfmqrb   64208 Sep  6 12:04 pg247.png
-rw-rw-r-- 1 sfmqrb sfmqrb  142780 Sep  6 12:02 pg248hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   49887 Sep  6 12:02 pg248.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1209522 Sep  6 11:39 sin_goog.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  147680 Sep  6 11:20 sns167.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   53545 Sep  6 12:03 w241.py
```


## [2026-09-06T16:04:05.468Z] TOOL CALL #73: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg247.png"
}
```


### [2026-09-06T16:04:05.495Z] TOOL RESULT

```

```


## [2026-09-06T16:04:22.489Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"sy'\\|syā\\|siyā\\|s(y)ā\" SNS_pages.txt | head -20; echo \"---\"; grep -c \"\" SNS_pages.txt",
 "description": "SNS glossary siyah"
}
```


### [2026-09-06T16:04:22.551Z] TOOL RESULT

```
9399:          .Y/Tl^-n^sy'g         :^«V       {Mir. Man.           1,42) ra'hyg                    ,
---
16584
```


## [2026-09-06T16:04:28.837Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"siah.gosh\\|siyahgosh\\|SYAGUSH\\|black.eared lynx\\|caracal\" HJB.txt AID.txt FSD_vol4.txt WEB_vol1.txt SKT.txt 2>/dev/null | head -10",
 "description": "Hobson-Jobson siyahgosh search"
}
```


### [2026-09-06T16:04:28.931Z] TOOL RESULT

```
HJB.txt:20069:8H0E-OO08E,  s.  This  ludicrous •corruption  of  the  Pers.  dydh-gosh,  lit. ^black-ear,'  t.e.  lynx  (Felts  Caracal) occurs  in  the  passage  below  from A.  Hamilton.  [The  corruption  of  the same  word  by  the  TimeSy  below,  is •equally  amusing.]
HJB.txt:20073:1813.— "The  Moguls  train  another  beast for  antelope-hunting  called  the  Syah-gash, or  black-^irs,  which  appears  to  be  the  same as  the  caracal,  or  Russian  lynx." — Forbes, Or,  Mem,  i,  277  ;  [2nd  ed.  i.  175  and  169].
WEB_vol1.txt:27995:car/a-cal, n. [Fr. caracal; Turk. qara qulaq; qara, black, and qulaq, ear.]
WEB_vol1.txt:27996:1. a lynx, the Lynx caracal, a native of northern Africa and southwestern Asia. Its color is a uniform reddish-brown; its ears blag’ externally, and tipped with long, black
WEB_vol1.txt:27998:2. the fur of the caracal.
WEB_vol1.txt:52944:des’ért lynx, the caracal. É
WEB_vol1.txt:71733:Fé’li-dae, n.pl. [from L. felis, properly feles,acat, and -idz.] animals of the cat kind, a family of carnivora. The incisor teeth are equal; the third tooth behind the large canine in either jaw is narrow and sharp, and these, the car- nassial or sectorial teeth, work against each other like scissors in cutting flesh; the claws are sheathed and retractile. This family in- cludes the domestic cat, wildcat, lion, tiger, leopard, lynx, jaguar, anther, cheetah, ounce, caracal, serval, ocelot, etc.
FSD_vol4.txt:13696:snall'flsh",  1   snei'flSh*  2   snai'flsh’,  n   A   llpartdold  fish  or 8nall’flow"cr,  l   snel'flau'er,  2   snarilow'er,  n   A   twining plant  (Phaseolus  caracalla)  allied  to  the  common  kidney- bean,  with  large  sweet-scented  purple  and  yellowish  flowers, with  the  petals  spirally  twisted snake,  1   snek,  2   snak,  r   [snaked  snak'ing  )   I.  f 1.  [Colloq  ,   U   S   1   To  drag  os  by  seizing  an  end  or  limb, haul  along  the  ground  as  with  a   rope  or  chain,  as,  to snale  a   log  out  of  a   ditch  2.  To  effect  by  snakelike motion  or  action  3.  Naui  (1)  To  take  the  end  part  of a   yarn  under  and  over  the  low  er  and  upper  turns  of  (a seizing)  in  order  to  secure  it  better  (2)  To  worm  (3) To  fasten  together,  as  two  ropes,  by  •winding  spirally With  cords  II.  t   To  ■wind  or  crawl  hke  a   snake —   snak'lng-trall",  n   A   gutter-road snake*,  n   1.  An  ophidian  reptile,  a   serpent
FSD_vol4.txt:66594:Tons  et  orfgo.  [L  ]   Source  and  origin force  majeure  [F  ]   Lata  A   major  force  said  of  an  un- expected and  unpreventable  event,  such  as  an  act  of  God forensis  strepltus.  [L  )   The  clamor  of  the  forum forma  urbls.  (L  J   Rem  Antiq  Plan  of  the  city  an  out- line of  Rome  traced  on  marble  as  It  was  under  Sev  eras  and Caracalla,  rediscovered  In  the  16th  century  and  now  In Capltollne  Museum  at  Rome forsan  et  htec  ollm  memlnisse  Juvabit.  (L  ]   Verg 1,  203  Perchance  even  these  things  It  will  be  hereafter delightful  to  remember
FSD_vol4.txt:100988:Perpetnns  of  Tours  St  lyalter- 217:  Caracalla,  Roman  emperor,  assassi- nated
```


## [2026-09-06T16:04:38.283Z] TOOL CALL #76: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B5%D9%86%D8%AC",
 "prompt": "Give the Arabic entry for صنج (ṣanj): etymology (Persian source?), meanings (cymbal, harp), and any Persian entry for صنج on the same page."
}
```


## [2026-09-06T16:04:39.110Z] TOOL CALL #77: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/hue",
 "prompt": "Give the etymology of 'hue' (colour) — Old English hiw/heow, Proto-Germanic *hiwam, Gothic hiwi, and the PIE root and cognates (Sanskrit, Old Church Slavonic)."
}
```


### [2026-09-06T16:04:43.700Z] TOOL RESULT

```
# Arabic Entry for صنج (ṣanj)

**Etymology:** The word derives from Middle Persian čang ("harp"), passing through Modern Persian چنگ (čang, "harp"). Arabic later borrowed related forms like جَنْك (jank) and جُنْك (junk).

**Meanings:**
1. An obsolete term for "harp"
2. A "cymbal" (the current primary meaning)

**Persian Entry:** The page indicates there are entries available in both Persian (فارسی) and Hungarian (Magyar) Wiktionaries, with links provided at the top of the entry. However, the actual Persian definition content is not included in this English Wiktionary page—only a reference link to the Persian Wiktionary version exists.
```


### [2026-09-06T16:04:46.160Z] TOOL RESULT

```
# Etymology of 'Hue' (Colour)

**Old English Origins:**
The word derives from Old English _hiw_ and earlier _heow_, meaning "color; form, appearance; species, kind; beauty."

**Proto-Germanic Roots:**
These descended from Proto-Germanic _*hiwam_, which reconstructs to PIE _*kiwo-_, a suffixed form of the root _*kei-_ (2), described as "a color adjective of broad application."

**Cognates:**
- **Sanskrit:** _chawi_ meaning "hide, skin, complexion, color, beauty, splendor"
- **Germanic languages:** Old Norse _hy_ ("bird's down"), Swedish _hy_ ("skin, complexion"), Gothic _hiwi_ ("form, appearance")

**Historical Note:**
The Online Etymology Dictionary notes this was "a common word in Old English, squeezed into obscurity after c. 1600 by _color_" but was "revived 1850s in chemistry and chromatography" with a more specialized technical meaning regarding color quality beyond luminosity and chroma.
```


## [2026-09-06T16:04:54.634Z] TOOL CALL #78: Bash

```json
{
 "command": "for u in 'https://en.wiktionary.org/wiki/سیاه|page 247, root Kei 1, Persian سیاه < MP syā < PIr *cyaHwáh, Av. siiāuua, cognate with English hue' 'https://en.wiktionary.org/wiki/شاهین|page 247, root Kei 1, Persian شاهین from MP šāhēn = šāh + -ēn, NOT from Av. saēna' 'https://en.wiktionary.org/wiki/سیمرغ|page 247, root Kei 1, Persian سیمرغ < MP sēn-murw' 'https://en.wiktionary.org/wiki/صنج|page 247, root Keg, Arabic صنج ṣanj from MP/NP čang harp' 'https://www.etymonline.com/word/chinch|page 247, root Kei 1, English chinch < Sp. chinche < L. cimicem; Latin cimex of uncertain origin' 'https://www.etymonline.com/word/hue|page 247, root Kei 1, English hue < OE hiw < PGmc *hiwam < PIE *kei- colour'; do url=\"${u%%|*}\"; note=\"${u#*|}\"; python3 tools/fetch_source.py \"$url\" --note \"$note\" 2>&1 | tail -1; done",
 "description": "Archive remaining web sources"
}
```


### [2026-09-06T16:04:58.626Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/f34c84f4a7c6314f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/97fb4684241b09b5.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/221dca62bcc95883.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/cde7456185eec032.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/3e46119bbbbd5d61.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ff935500b70ed5ac.txt
```


## [2026-09-06T16:05:50.757Z] TOOL CALL #79: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"saēna\\|saöna\\|saena\\|1548\\|mərəγō\" BRT.txt | grep -n -i \"saena\\|saēna\" | head -10; echo \"---\"; grep -n \"j.  saena-\\|saena-  m\\|Raubvogel\" BRT.txt | head -10",
 "description": "Bartholomae saena entry"
}
```


### [2026-09-06T16:05:50.849Z] TOOL RESULT

```
1:3658:•  j.  ap«m9n),  g.  ap3ni9m  Adv.:  s.  apma-, ■  j.  a-p9r9tö.tanü-  Adj.  'auf  des  Leib kein  Makel  haftet,  makellosen  Leibes"*: Aagat^rnt  gavam  axsaenanqm  'nunqnt  V. 22.4.
3:25786:•  j.  'saena-  m.  Name  eines  grossen  Raub- vogels, wohl  des  Adlers:  ya'äia  Aau  masa m»rrfll  'nS  Yt.  l4-A^s  —  "/"^  avqm  vartam yqm  •nake..yä  vaoh  vTspS-^i/ (sd.)  aama YL12. 17.
4:25788:I  j.  'saena-  m.  EN.  eines  GIäiibigen*>: 'nahe  ahüm.jtütB  asaons . .  yH  paoiryS  saiB.- aghryS  fraxstata  paiti  aya  ama  "des  S., Sohns  des  A.  . .,  der  zuerst  mit  hundert SchUlem  auftrat  . ."  YLy.97;  —  HyrSis ■nahe  "des  Z.,  Sohns  des  S."  Yt.ij.  126. *)  Der  vom  loo.  bis  zum  200.  Jahr  der  lora- %»?/rischen  Religion  gelebt  haben  soll;  s.  DkB. '97  iS-  2.17).  West  SEE.  37.  230,  262,  47.  83.
5:25794:•  j.  saenay-  i)  Adj.  'spitz'  (nur Komp.).  2)  m.  'Spitze,  Wipfel';  •ni? (AP.)  marnai  umaranqm{sd.)  Yt  14.  21.
---
17240:Ar.  'biäsa-  m.  Name  eines  Raubvogels'),  — ai.  bhäsa-  m.  (auch  als  EN.);  mp.  bähai  EN. (=  ai.  ikäsaka-  EN.\  S.  noch  Marquart EranSahr  128.  —  ')  Zn  gr.  ^n;  {eine  Adler- att)  s.  Bthl.  IF.  8.  235.
25654:ITA.,  aus  ar.  *nrattt;  Praes.  1.  —  Vgl,  gr, fX«^'Fang,  Beute',  Ist.  i'dZiv«-;  s.  dainSOLMSEN Slud.  15.  —  Npü.:  bar  iulanät'1.  —  >)  Vgl. zSt.  Bkehm  Tierleben>,  Vögel  7.  523;  "Zum Fangen  dienen  (dem  Raubvogel)  die  Füsse  . ., zum  Zerstückeln  der  Nahrung  .  ,  der  Schna- bel . .".   —  J)  S.  »n  'urvala:
25786:•  j.  'saena-  m.  Name  eines  grossen  Raub- vogels, wohl  des  Adlers:  ya'äia  Aau  masa m»rrfll  'nS  Yt.  l4-A^s  —  "/"^  avqm  vartam yqm  •nake..yä  vaoh  vTspS-^i/ (sd.)  aama YL12. 17.
25788:I  j.  'saena-  m.  EN.  eines  GIäiibigen*>: 'nahe  ahüm.jtütB  asaons . .  yH  paoiryS  saiB.- aghryS  fraxstata  paiti  aya  ama  "des  S., Sohns  des  A.  . .,  der  zuerst  mit  hundert SchUlem  auftrat  . ."  YLy.97;  —  HyrSis ■nahe  "des  Z.,  Sohns  des  S."  Yt.ij.  126. *)  Der  vom  loo.  bis  zum  200.  Jahr  der  lora- %»?/rischen  Religion  gelebt  haben  soll;  s.  DkB. '97  iS-  2.17).  West  SEE.  37.  230,  262,  47.  83.
```


## [2026-09-06T16:05:55.758Z] TOOL CALL #80: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=25770 && NR<=25790' BRT.txt | grep -n \"^15\\|^1[0-9][0-9][0-9]$\" ; python3 - <<'EOF'\nt=open('BRT.txt',encoding='utf-8',errors='replace').read().split('\\n')\n# find nearest standalone number before line 25786\nimport re\nfor i in range(25786,25700,-1):\n    if re.fullmatch(r'\\s*1\\d{3}\\s*', t[i-1] or ''):\n        print('col marker at line',i,repr(t[i-1])); break\nEOF",
 "description": "Find Bartholomae column for saena"
}
```


### [2026-09-06T16:05:57.682Z] TOOL RESULT

```
col marker at line 25766 '1548'
```


## [2026-09-06T16:06:04.982Z] TOOL CALL #81: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg247.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/247.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/ | tail -3",
 "description": "Copy page image for audit"
}
```


### [2026-09-06T16:06:05.058Z] TOOL RESULT

```
-rw-rw-r--  1 sfmqrb sfmqrb  78178 Sep  5 10:14 95.png
-rw-rw-r--  1 sfmqrb sfmqrb  72929 Sep  5 10:19 96.png
-rw-rw-r--  1 sfmqrb sfmqrb  65608 Sep  5 10:43 99.png
```


## [2026-09-06T16:06:07.017Z] AGENT

Now writing the verification file.


## [2026-09-06T16:19:13.135Z] TOOL CALL #82: Write

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/page-247.json",
 "content": "{\n  \"pdf_page\": 247,\n  \"book_page\": 217,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-06\",\n  \"entries\": [\n    {\n      \"entry\": 1,\n      \"root\": \"Keg, Keng, Kek, Kenk 2, Kag\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *keg-, *keng- / *kek-, *kenk- 'peg to hang things on, hook, handle; to be pointed' (Pokorny IEW 537-538; Walde-Pokorny I 382 f.); Mann's variant entries kag-/kaĝ- 'hook, claw; bend, angle, hook' (IEC 458)\",\n      \"note\": \"Pokorny 537-538 heads the entry exactly as Nourai names it: 'keg-, keng- und kek-, kenk- „Pflock zum Aufhängen, Haken, Henkel“; auch „spitz sein“; vgl. das ähnliche kak-, kank-; und kenk-, konk-'. Nourai's fifth name 'Kag' is not from Pokorny but from Mann, whose p.458 carries 'kag- (kagol-, kagil-) „hook, claw“' and 'kaĝ- (variant of type kag-) (1) „bend, angle, hook; bent“ ... Per. kaj (-ž) „bent“'; so the two cited references between them justify all five names and the gloss 'hook'. 'Kenk 2' is Nourai's own numbering of Pokorny's nasalised kenk-/konk- variant. The one substantive error in the chart is in node #1: the very form Pokorny prints under this root, čang, he labels 'Npers.' (New Persian), not Avestan; there is no Avestan *čanga- in Bartholomae's Altiranisches Wörterbuch. Everything else on the chart — čang > Arabic ṣanj, kaj/kaž, Germanic *hōka-/*hakkijan > hook/hack — is standard.\",\n      \"note_fa\": \"جعبهٔ ریشه درست است. پوکورنی در صفحهٔ ۵۳۷ فرهنگ خود مدخل «keg-, keng- و kek-, kenk-» را با معنای «میخ آویز، قلاب، دسته» و نیز «تیز بودن» آورده و همان‌جا گونهٔ خیشومی kenk-/konk- را یاد کرده است؛ این همان «Kenk 2» نورایی است. نام پنجم «Kag» از پوکورنی نیست بلکه از من، صفحهٔ ۴۵۸ گرفته شده که دو مدخل kag- «قلاب، چنگال» و kaĝ- «خمیده، کج» دارد و در دومی صریحاً «فارسی kaj (کژ)» را می‌آورد. تنها لغزش این صفحه در گرهٔ ۱ است: صورت čang را خود پوکورنی «فارسی نو» خوانده نه اوستایی، و در فرهنگ ایرانی باستان بارتولمه هیچ واژهٔ اوستایی *čanga- نیست.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/%DA%86%D9%86%DA%AF\",\n        \"https://en.wiktionary.org/wiki/%DA%A9%DA%98\"\n      ],\n      \"ref_check\": [\n        {\n          \"ref\": \"POK:537\",\n          \"status\": \"supports\",\n          \"note\": \"POK_02.txt, \\\\f-leaf 195 (running numbers 537-538): 'keg-, keng- und kek-, kenk- „Pflock zum Aufhängen, Haken, Henkel“; auch „spitz sein“; vgl. das ähnliche kak-, kank-; und kenk-, konk-, Npers. čang „Klaue, Faust“ (*kengo-)'. Root name and gloss 'hook' exactly as charted.\"\n        },\n        {\n          \"ref\": \"IEC:458\",\n          \"status\": \"supports\",\n          \"note\": \"IEC.txt \\\\f-leaf 263, which carries the printed folio number '458': 'kag- (kagol-, kagil-) „hook, claw“. Cf. kagot- and next. Cf. kaĝ- (variant)' and 'kaĝ- (variant of type kag-, q.v.) (1) „bend, angle, hook; bent“. (Gmc. ambig.) Per. kaj (-ž) „bent“; OE haca, wm. „hook“; OS hako, id. ... Long-gde in Ir. cág „handle, shaft“; OE hoc ... „hook, angle, corner“'. This is the source of Nourai's fifth root-name 'Kag' and of node #5.\"\n        }\n      ],\n      \"consulted\": [\n        {\n          \"src\": \"WLD\",\n          \"where\": \"Bd. I 382 (WLD_Bd1_1930_dli_70244_djvu.txt line 24048-24051, printed folio '382' on the preceding line)\",\n          \"stance\": \"supports\",\n          \"note\": \"'keg-, keng- und kek-, kenk- etwa kleiner Pflock, bes. zum Aufhängen, Haken, Henkel. Vgl. das ähnliche kuk-, kunk-.' — the entry Pokorny 537 abridges (his own reference 'WP. I 382 f.').\"\n        },\n        {\n          \"src\": \"AHD\",\n          \"where\": \"Watkins 1985, k-list (AHD_watkins1985.txt line 594)\",\n          \"stance\": \"supports\",\n          \"note\": \"'keg-. Hook, tooth. 1. Germanic *hakan- in: a. Old Norse haki, hook, akin to Old English haca, hook: HAKE ... 2. Germanic lengthened form *hōka- in: a. Old English hōc, hook: HOOK ... 4. Germanic *hakkijan in Old English -haccian, to hack to pieces as with a hooked instrument: HACK. [Pok. keg- 537.]' Same root, same gloss, same Germanic material as nodes 6-7.\"\n        },\n        {\n          \"src\": \"BQT\",\n          \"where\": \"vol. 2 p. 665 (BQT_v2_pages.txt \\\\f-leaf 122)\",\n          \"stance\": \"supports\",\n          \"note\": \"s.v. چنگ: 'منحنی و خمیده را گویند — قلاب باشد عموماً — و قلابی که بدان فیل رانند خصوصاً و آن را کجک نیز گویند — و پنجه و انگشتان مردم — و چنگال مرغان و جانوران دیگر باشد — و نام سازست مشهور'. Note that Borhan itself glosses چنگ with کجک, tying the hook and the 'crooked' word together as the chart does.\"\n        }\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan\",\n          \"words\": \"cang\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"The form itself is real but the language label is wrong. Pokorny 537, the page Nourai cites, prints the word as 'Npers. čang „Klaue, Faust“ (*kengo-)' — i.e. as New Persian, the only Iranian witness he has for the root; the same word is Nourai's own node #2. Bartholomae's Altiranisches Wörterbuch has no *čanga-/cang at all (grep for 'cang/čang' returns nothing across BRT.txt), and no Avestan text attests such a word. Modern reconstruction goes only as far back as Proto-Iranian *čanga- 'claw', inferred from Middle Persian čang (Mo'in's footnote to Borhan s.v. چنگ gives 'pahlavi čang'), New Persian čang, and Old Armenian ճանկ (čank), which is itself an Iranian loan. So the arrow root → čang is right, but it should run to node #2 directly and be labelled Middle/New Persian, not Avestan.\",\n          \"derivation_fa\": \"صورت درست است ولی برچسب زبان نادرست است. خود پوکورنی در همان صفحهٔ ۵۳۷ که نورایی ارجاع می‌دهد می‌نویسد «Npers. čang „Klaue, Faust“ (*kengo-)»؛ یعنی این واژه را فارسی نو می‌داند نه اوستایی. در «فرهنگ ایرانی باستان» بارتولمه هیچ مدخلی به صورت *čanga- نیست و در متون اوستا نیز چنین واژه‌ای به کار نرفته است. پژوهش امروزی تنها تا ایرانی آغازین *čanga- «چنگال» پیش می‌رود که از فارسی میانهٔ čang و وام‌واژهٔ ارمنی باستان čank بازسازی شده است. پس پیکان ریشه‌‌از ریشه درست است اما این جعبه باید «فارسی میانه/نو» برچسب می‌خورد؛ این خطای خود کتاب است نه خطای خوانش اسکن (صفحهٔ چاپی ۲۱۷ هم «Avestan | cang : hook» دارد).\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%DA%86%D9%86%DA%AF\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"POK:537\",\n              \"status\": \"contradicts\",\n              \"note\": \"POK_02.txt leaf 195: the only Iranian form under keg-/keng- is 'Npers. čang „Klaue, Faust“ (*kengo-)'. Pokorny calls it New Persian; Nourai's box calls it Avestan.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"BRT\",\n              \"where\": \"BRT.txt, whole text\",\n              \"stance\": \"silent\",\n              \"note\": \"grep -n -i 'cang|čang|canga' BRT.txt returns no hits: Bartholomae's Altiranisches Wörterbuch records no Avestan or Old Persian word of this shape.\"\n            },\n            {\n              \"src\": \"IEC\",\n              \"where\": \"p. 488 s.v. keng- (IEC.txt \\\\f-leaf 279)\",\n              \"stance\": \"partial\",\n              \"note\": \"'keng- „seize, grip, hold; hold, hook, grapple, hobble“ ... Per. ċäng „claws, fingers“, cf. also čängāl, čängul „claws, hook“ ... Li. cf. kenge „hook“'. Mann too has the word only as Persian; his Avestan citation on this line is a different word ('claw, cleft hoof'), and the OCR of it is illegible.\"\n            },\n            {\n              \"src\": \"PHD\",\n              \"where\": \"PHD_mackenzie.txt line 8467 (Pahlavi key)\",\n              \"stance\": \"partial\",\n              \"note\": \"MacKenzie's Pahlavi key lists 'cam!, cang' — the word is attested in Middle Persian, i.e. one stage later than the chart claims, and no earlier.\"\n            }\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"čang «چنگ» (also چنگال، چنگک)\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"NP چنگ čang 'claw, paw, hooked hand' continues MP čang (Mo'in's footnote to Borhan s.v. چنگ gives the Pahlavi form; MacKenzie's Pahlavi key has cang), from Proto-Iranian *čanga-, from PIE *keg-/*keng- 'peg, hook, claw' with the regular Indo-Iranian palatalisation of *k before a front vowel (*kenɡ- > *čanɡ-) and the equally regular Iranian retention of the nasal before the velar. The derivatives چنگال čangāl 'claw, fork' (čang + the instrument/collective suffix -āl) and چنگک čangak 'small hook' (+ diminutive -ak) are New Persian formations. Borhan-e Qate' p.665 glosses چنگ 'bent and curved; a hook in general; specifically the elephant-goad, also called کجک; the human paw and fingers; the claws of birds and beasts', i.e. exactly Nourai's 'hook, paw'. The third gloss 'harp' belongs to the same Middle Persian word čang 'harp' (Parthian šang); Wiktionary lists it as a separate etymology because the semantic bridge (the plucking hand, or the instrument's hooked frame) is not directly attested, but no source assigns it a different Indo-European root.\",\n          \"derivation_fa\": \"«چنگ» از فارسی میانهٔ čang و آن از ایرانی آغازین *čanga- «چنگال» است که خود به ریشهٔ هندواروپایی آغازین *keg-/*keng- «میخ، قلاب، چنگال» می‌رسد؛ کاف هندواروپایی پیش از واکهٔ پیشین در هندوایرانی به چ دگرگون شده (کامی‌شدگی) و خیشوم پیش از گ بر جای مانده است. «چنگال» و «چنگک» ساخته‌های فارسی نو با پسوندهای ‌ال و ‌ک اند. برهان قاطع در صفحهٔ ۶۶۵ همین معانی «قلاب، پنجه، چنگال مرغان» را می‌آورد. معنای سوم یعنی ساز «چنگ» نیز همان واژهٔ فارسی میانه (پارتی šang) است؛ ویکی‌واژه آن را مدخل جداگانه آورده زیرا پل معنایی مستند نیست، ولی هیچ منبعی ریشهٔ دیگری برای آن نمی‌شناسد. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%DA%86%D9%86%DA%AF\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"POK:537\",\n              \"status\": \"supports\",\n              \"note\": \"POK_02.txt leaf 195: 'Npers. čang „Klaue, Faust“ (*kengo-)' — Pokorny's single Iranian witness for the root is precisely this word.\"\n            },\n            {\n              \"ref\": \"BQT:665\",\n              \"status\": \"supports\",\n              \"note\": \"BQT_v2_pages.txt \\\\f-leaf 122 (printed p.665, confirmed by the running head ۱۲۰۰ two leaves further on in the same column series): 'چنگ ... منحنی و خمیده را گویند، قلاب باشد عموماً ... و پنجه و انگشتان مردم ... و چنگال مرغان و جانوران دیگر باشد و نام سازست مشهور'; Mo'in's footnote to the entry gives the Pahlavi form čang.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"IEC\",\n              \"where\": \"p. 488 s.v. keng- (IEC.txt \\\\f-leaf 279)\",\n              \"stance\": \"supports\",\n              \"note\": \"'Per. ċäng „claws, fingers“, cf. also čängāl, čängul „claws, hook“' — Mann has čang, čangāl and čangul under the same root, matching the chart's 'extra' forms.\"\n            },\n            {\n              \"src\": \"PHD\",\n              \"where\": \"PHD_mackenzie.txt line 8467 (Pahlavi key, s.v. cang)\",\n              \"stance\": \"supports\",\n              \"note\": \"MacKenzie's Pahlavi key lists 'cam!, cang', confirming the Middle Persian intermediate that Nourai's chart passes over in silence.\"\n            },\n            {\n              \"src\": \"MON\",\n              \"where\": \"MON_part1.txt line 90266, s.v. صنج\",\n              \"stance\": \"supports\",\n              \"note\": \"'صنج: [معر. سنج، قس. چنگ] (اِ.) چنگ' — Mo'in equates صنج with چنگ, corroborating the chart's next link.\"\n            }\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Arabic\",\n          \"words\": \"sanj\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Arabic صَنْج ṣanj is a Persian loan, but the two glosses Nourai gives have two different Persian sources. Asbaghi (PLA p.188) prints them as two entries on the same page: 'ṣang: „Kastagnetten“ ← pers. زنگ zang ← mp. sanj' and 'ṣangʲ: „persische Harfe“ ← pers. چنگ čang ← mp. čang; syr. ..., mand. singa'. So only the 'harp' sense is from čang: Persian č- was rendered by Arabic ṣ- (Arabic having no /č/, the emphatic sibilant being the regular substitute in early loans, cf. صولجان < چوگان), and the nasal + velar cluster gave -nj. The 'cymbal' sense, which is the ordinary modern meaning, Asbaghi derives from Persian zang 'bell, gong'. Lokotsch no.392 gives only the harp route ('Pers. cäng: „Harfe, Laute“, ar. ṣang „pers. Harfe, Leier“'), and Wiktionary agrees ('from Middle Persian čang „harp“ ... an obsolete term for harp; a cymbal'). The node is therefore right for 'harp', doubtful for 'cymbal'.\",\n          \"derivation_fa\": \"«صنج» در عربی وام‌واژه‌ای فارسی است، اما دو معنایی که نورایی می‌آورد دو خاستگاه جدا دارند. اصبغی در «وام‌واژه‌های فارسی در عربی» صفحهٔ ۱۸۸ دو مدخل جداگانه دارد: صنج به معنی «سنج\\/قراقیز» از فارسی «زنگ»، و صنج به معنی «چنگ ایرانی» از فارسی «چنگ». در وام‌گیری، چ، که در عربی نیست، به صاد بدل شده است (همان‌گونه که چوگان > صولجان). لکوچ (شمارهٔ ۳۹۲) و ویکی‌واژه نیز تنها راه «چنگ» را می‌شناسند. پس ادعای نورایی برای معنای «harp» پذیرفتنی است و برای «cymbal» با احتیاط.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%B5%D9%86%D8%AC\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"PLA:188\",\n              \"status\": \"partial\",\n              \"note\": \"PLA_pages.txt leaf index 202 = printed p.188 (running heads 'ṣanār ... ṣandaldand'). Two entries: 'ṣang: „Kastagnetten“ ← pers. زنگ zang ← mp. sanj' and 'ṣang: „persische Harfe“ ← pers. چنگ čang ← mp. čang, syr. ..., mand. singa'. Asbaghi therefore supports 'harp ← čang' but assigns 'cymbal/castanets' to Persian zang, not to čang.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"LKT\",\n              \"where\": \"no. 392 (LKT.txt line 1059)\",\n              \"stance\": \"supports\",\n              \"note\": \"'392. Pers. cäng: „Harfe, Laute“, ar. ṣang „pers. Harfe, Leier“ [KM II. 1161, 3]; hieraus mit ar. Art. Asangue „Sternbild der Leier, Lyra“. [Devic DEt 41.]'\"\n            },\n            {\n              \"src\": \"TAD\",\n              \"where\": \"al-'Anisi, s.v. صنج (TAD.txt line 1778)\",\n              \"stance\": \"contradicts\",\n              \"note\": \"'صنج: سنج، الفارسي معناه الوازن. الظاهر أن لفظ صنج ج صنوج هو تحريف ... أي صنواج وهو مشتق من صلصل العربي أي صوّت' — al-'Anisi takes صنج from Persian سنج 'the weigher, balance-pan' and even toys with an Arabic صلصل 'to clang'.\"\n            },\n            {\n              \"src\": \"ARB\",\n              \"where\": \"al-Jawaliqi, al-Mu'arrab (ARB_mo3rb.txt lines 6915, 6940)\",\n              \"stance\": \"partial\",\n              \"note\": \"'والناي ... وبربط ... والصنج' and 'الصنج من آلات الملاهي' — the classical Arabic lexicographers list صنج 'among the instruments of amusement' as a foreign (Persian) word, without naming čang.\"\n            }\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Persian\",\n          \"words\": \"sanj, senj «صنج»\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Persian صنج sanj/senj 'cymbal' is written with ص because it is the Arabic orthography coming back into Persian: Mo'in's dictionary tags the headword 'صنج: [معرّب سنج، قس. چنگ]', i.e. 'Arabicised form of سنج, compare چنگ'. The round trip Persian → Arabic → Persian that Nourai draws is therefore real and is exactly what Mo'in says. What is uncertain is the far end: if the Arabic word behind modern Persian صنج is Asbaghi's ṣanj 'castanets/cymbal', its Persian etymon was زنگ zang, and only the homonymous ṣanj 'harp' came from چنگ; the two fell together in Arabic and were re-exported as one word. Nourai's own cross-reference ('See root “Gěu 1” for another possible derivation') shows he was aware of the alternative, and modern scholarship (Asbaghi) prefers it for the 'cymbal' sense.\",\n          \"derivation_fa\": \"«صنج» فارسی را با صاد می‌نویسند زیرا املای عربی آن دوباره وارد فارسی شده است؛ معین در فرهنگ خود می‌نویسد «صنج: [معرّب سنج، قس. چنگ]». پس رفت و برگشت فارسی ← عربی ← فارسی که نورایی ترسیم کرده واقعی است. آنچه جای تردید دارد سر دیگر زنجیره است: اگر صنج عربی به معنی سنج/قراقیز باشد، اصل آن پارسی «زنگ» است و تنها هم‌آوای آن به معنی جنگ\\/چنگ از «چنگ» آمده است. نورایی خود در یادداشت جعبه به ریشهٔ دیگری ارجاع داده و همین احتیاط درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%B5%D9%86%D8%AC\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"MON:2165\",\n              \"status\": \"partial\",\n              \"note\": \"MON_part1.txt line 90266 s.v. صنج: '[معر. سنج، قس. چنگ] (اِ.) چنگ. در فلزی که به وسیلهٔ بندی به انگشتان پیوندد' — Mo'in gives exactly Nourai's claim ('Arabicised سنج, compare چنگ'). Status 'partial' only because the local OCR of Mo'in carries no usable printed pagination, so the specific page 2165 could not be confirmed.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"PLA\",\n              \"where\": \"p. 188 (PLA_pages.txt leaf 202)\",\n              \"stance\": \"partial\",\n              \"note\": \"Asbaghi's two entries on this page make the 'cymbal' ṣanj a loan from Persian زنگ and only the 'harp' ṣanj a loan from چنگ; a Persian صنج 'cymbal' re-borrowed from Arabic would then trace to zang.\"\n            },\n            {\n              \"src\": \"BQT\",\n              \"where\": \"vol. 2 p. 665 (BQT_v2_pages.txt leaf 122)\",\n              \"stance\": \"silent\",\n              \"note\": \"Borhan's چنگ entry lists the musical instrument ('و نام سازست مشهور') but says nothing about the Arabic صنج or about a re-borrowing.\"\n            }\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Persian\",\n          \"words\": \"kaj «کج» (also کژ، کژدم)\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"NP کج kaj / کژ kaž 'bent, crooked, awry' continues Middle Persian kaž (also gaz), from the same PIE *keg-/*kaɡ- family, with the o/zero-grade *kaɡ- of Mann's 'kaĝ- (variant of type kag-) „bend, angle, hook; bent“', where Mann's first witness is 'Per. kaj (-ž) „bent“'. The Iranian palatal outcome ž (later also j) of the palatalised velar is regular; the modern doublet کژ ~ کج is the ordinary NP alternation of ž/j. کژدم každom 'scorpion' is a transparent compound kaž 'crooked' + dom 'tail' ('crook-tail'); Wiktionary lists it under this etymology. Mo'in keeps the semantic bridge to the root explicit: he glosses کج both 'خمیده، ناراست، معوج' and 'قلاب' (a hook), so 'hook' and 'crooked' are one word in Persian lexicography too, exactly as the chart's root box implies. The Hāfez line quoted in the box ('وز خم ابروی توام هیچ گشایشی نشد...') uses خیال کج 'crooked/vain thought' in the figurative sense.\",\n          \"derivation_fa\": \"«کج\\/کژ» از فارسی میانهٔ kaž (گونهٔ gaz) و آن از همان خانوادهٔ *keg-/*kaɡ- هندواروپایی «قلاب، خمیده» است؛ من در صفحهٔ ۴۵۸ مدخل kaĝ- «خمیده، کج» را دقیقاً با شاهد «Per. kaj (-ž)» می‌آورد. دگرگونی کاف کامی‌شده به ژ در ایرانی قاعده‌مند است و دوگانهٔ کژ ~ کج همان ابدال معمول ژ/ج در فارسی نو است. «کژدم» مرکّب کژ + دم یعنی «کج‌دم» است. معین خود در ذیل «کج» هم «خمیده، معوج» و هم «قلاب» را معنی کرده است؛ پس پیوند «قلاب» و «کج» همان است که در جعبهٔ ریشه آمده. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%DA%A9%DA%98\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"IEC:458\",\n              \"status\": \"supports\",\n              \"note\": \"IEC.txt leaf 263 (printed folio 458): 'kaĝ- (variant of type kag-, q.v.) (1) „bend, angle, hook; bent“. (Gmc. ambig.) Per. kaj (-ž) „bent“; OE haca, wm. „hook“; OS hako, id.; Du. hak „heel, hock“ ...'. Mann's page number is precisely the one Nourai cites, and Persian kaj is his lead witness.\"\n            },\n            {\n              \"ref\": \"MON:2910\",\n              \"status\": \"partial\",\n              \"note\": \"MON_part2.txt line 21004 s.v. کج: '[- کژ] (ص.) خمیده، ناراست، معوج؛ مق. راست ... قلاب (اعم از قلابی که بدان یخ در یخدان اندازند یا قلابی که کشتیبان کشتی خصم را به جانب خود کشند)'. Content supports the node; 'partial' only because the local Mo'in OCR gives no printed page numbers to check 2910.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"POK\",\n              \"where\": \"IEW 537-538 (POK_02.txt leaf 195)\",\n              \"stance\": \"silent\",\n              \"note\": \"Pokorny's keg-/keng- entry has no Persian kaj; his only Iranian item is čang. The 'crooked' word reaches this root only through Mann's kaĝ- variant.\"\n            },\n            {\n              \"src\": \"BQT\",\n              \"where\": \"vol. 2 p. 665 (BQT_v2_pages.txt leaf 122)\",\n              \"stance\": \"supports\",\n              \"note\": \"Borhan glosses چنگ as the elephant-hook 'و آن را کجک نیز گویند' — the same object is called both چنگ and کجک in Persian, an independent confirmation that کج and چنگ belong together semantically.\"\n            }\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"Germanic\",\n          \"words\": \"hôka : hook ; hakkijan : to hack\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Proto-Germanic *hōka- 'hook' is the lengthened-grade o-form of the root (*kāg- > Gmc *hōk- by Grimm's Law k > h and ɡ > k), beside the short-vowel *hakan- (ON haki, OE haca) and the geminated intensive *hakkijan 'to hack' (OE -haccian, MLG/MHG hacken), whose -kk- is the expressive gemination Pokorny notes ('mit intensiver Gemination: ags. haccian „hacken“'). Watkins' AHD appendix, Nourai's cited reference, sets out exactly these three Germanic stems under keg-.\",\n          \"derivation_fa\": \"ژرمنی آغازین *hōka- «قلاب» گونهٔ کشیدهٔ همین ریشه است؛ کاف هندواروپایی بر پایهٔ قانون گریم به h و گ به k بدل شده است. در کنار آن گونهٔ کوتاه *hakan- (ایسلندی کهن haki، انگلیسی کهن haca) و فعل تشدیدی *hakkijan «بریدن، قطع کردن» قرار دارد؛ دوگانگی kk را پوکورنی «mit intensiver Gemination» می‌خواند. پیوست ریشه‌های واتکینز (AHD) دقیقاً همین سه ستاک را ذیل keg- می‌آورد. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/hue\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"AHD\",\n              \"status\": \"supports\",\n              \"note\": \"AHD_watkins1985.txt line 594: 'keg-. Hook, tooth. 1. Germanic *hakan- ... 2. Germanic lengthened form *hōka- in: a. Old English hōc, hook: HOOK ... 4. Germanic *hakkijan in Old English -haccian, to hack to pieces as with a hooked instrument: HACK. [Pok. keg- 537.]' Both of Nourai's Germanic forms are Watkins' own.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"POK\",\n              \"where\": \"IEW 537-538 (POK_02.txt leaves 195-196)\",\n              \"stance\": \"supports\",\n              \"note\": \"'germ. *hakan-, *hōka-, *hekan- m. „Haken“ in: aisl. PN Haki ... ags. hōc m. „Haken“ ... mit intensiver Gemination: ags. haccian „hacken“, mnd., mhd. hacken ds.'\"\n            },\n            {\n              \"src\": \"WLD\",\n              \"where\": \"Bd. I 382 (WLD_Bd1 djvu line 24051 ff.)\",\n              \"stance\": \"supports\",\n              \"note\": \"'norw. hake m. „Haken“, as. haco, ags. haca m. „Haken“ ... ags. hōc m. „Haken“, mnd. hok, huk m. „Winkel, Ecke, Vorgebirge“ ... ahd. hecken „stechen“.'\"\n            }\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"English\",\n          \"words\": \"hook, hack\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"OE hōc 'hook' > ME hok/hoke > NE hook, with the regular OE ō > ME ǫuː > NE /uː/ shortened to /ʊ/ before k. OE -haccian 'to cut to pieces' (attested in tō-haccian) > ME hakken > NE hack (verb), the noun being deverbal. Watkins lists HOOK and HACK as the English outcomes of keg-; Klein and Skeat agree, and Etymonline traces hook to OE hōc, PGmc *hōka-.\",\n          \"derivation_fa\": \"انگلیسی hook از انگلیسی کهن hōc و hack از فعل انگلیسی کهن -haccian «تکه‌تکه بریدن» است؛ هر دو دنبالهٔ مستقیم صورت‌های ژرمنی جعبهٔ پیشین‌اند (واتکینز ذیل keg- همین دو واژه را می‌آورد). زنجیره بی‌منازعه است و ادعای نورایی درست است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\n              \"ref\": \"None\",\n              \"status\": \"not_checked\",\n              \"note\": \"The node carries no reference of its own; it inherits the AHD citation of its parent node #6, which was checked and supports it.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"AHD\",\n              \"where\": \"Watkins 1985, s.v. keg- (AHD_watkins1985.txt line 594)\",\n              \"stance\": \"supports\",\n              \"note\": \"'Old English hōc, hook: HOOK' and 'Old English -haccian, to hack to pieces as with a hooked instrument: HACK.'\"\n            },\n            {\n              \"src\": \"POK\",\n              \"where\": \"IEW 538\",\n              \"stance\": \"supports\",\n              \"note\": \"'ags. hōc m. „Haken“ ... ags. haccian „hacken“' — the Old English ancestors of both English words.\"\n            }\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 2,\n      \"root\": \"Kei 1, Kiě 1\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *ḱei- 'dark, grey, brown' (in colour adjectives), with the extended stem *ḱiē-/*ḱi- and *ḱi-h₃-wo- 'colour'; Pokorny IEW 540-541, Walde-Pokorny I 360-361, Watkins ḱei-2\",\n      \"note\": \"Pokorny 540 (bottom) heads the entry '2. kei- in Farbbezeichnungen, meist für dunkle Farben (s. auch ke-ro); kei-ro-, koi-ro- „dunkel, grau, braun“; ki-uo- „Farbe“', and on p.541 adds 'Daneben eine erweiterte Wurzelform gleicher Bedeutung: kie-, ki-; kie-mo- „dunkelgrau“'. That is exactly Nourai's double name 'Kei 1, Kiě 1' and his gloss 'gray or black color, dark'; the numeral '1' is Nourai's own (Pokorny's colour root is his no. 2, his no. 1 kei- being 'liegen'). The whole page follows Pokorny 541 item by item: Av. syava-/syamaka-/sama-, npers. siyah, Lat. cimex, Goth. hiwi > engl. hue, av. saena-. Two things need correction: شاهین in node #8 is not from saena- but from شاه + -ین, and the Germanic form in node #10 should be *hiwam (Goth. hiwi), not 'hiwan'. Nourai's own NOTE on node #2, that Turkish kara-kulak 'black ear' is the source of English caracal, is correct: Klein s.v. caracal 'F., fr. Turk. qarah qulak, „black ear“' and Webster 'Turk. qara qulaq'.\",\n      \"note_fa\": \"جعبهٔ ریشه درست است. پوکورنی در پایان صفحهٔ ۵۴۰ مدخل «2. kei- در نام‌های رنگ، بیشتر رنگ‌های تیره» را با معنای «تار، خاکستری، قهوه‌ای» آورده و در صفحهٔ ۵۴۱ گونهٔ گستردهٔ kie-, ki- را می‌افزاید؛ همین دو نام «Kei 1, Kiě 1» نورایی است (شمارهٔ ۱ از خود اوست؛ در پوکورنی این ریشه شمارهٔ ۲ است). سراسر صفحه از همان صفحهٔ ۵۴۱ گرفته شده است: اوستایی syava-، syamaka-، sama-، فارسی سیاه، لاتین cimex، گوتی hiwi > انگلیسی hue و اوستایی saena-. دو نکته باید تصحیح شود: «شاهین» از saena- نیست بلکه از شاه + ‌ین است، و صورت ژرمنی در گرهٔ ۱۰ باید *hiwam باشد نه hiwan. یادداشت خود نورایی دربارهٔ kara-kulak ترکی (ریشهٔ caracal انگلیسی) درست است و کلاین و وبستر همان را می‌گویند.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/%D8%B3%DB%8C%D8%A7%D9%87\",\n        \"https://www.etymonline.com/word/hue\"\n      ],\n      \"ref_check\": [\n        {\n          \"ref\": \"POK:540\",\n          \"status\": \"supports\",\n          \"note\": \"POK_02.txt \\\\f-leaf 199, at the foot of printed p.540: '2. kei- in Farbbezeichnungen, meist für dunkle Farben (s. auch ke-ro); kei-ro-, koi-ro- „dunkel, grau, braun“; ki-uo- „Farbe“. Ai. si-ti- „weiß“ ...' — root, language label and gloss all as charted; p.541 continues with the extended stem 'kie-, ki-; kie-mo- „dunkelgrau“'.\"\n        }\n      ],\n      \"consulted\": [\n        {\n          \"src\": \"WLD\",\n          \"where\": \"Bd. I 360-361 (WLD_Bd1_1930_dli_70244_djvu.txt lines 22714 ff.)\",\n          \"stance\": \"supports\",\n          \"note\": \"'2. kei- in Farbbezeichnungen, bes. für dunkle Farben (s. auch u. kor-). ... Daneben eine erweiterte Wzf. kiē-. Ai. çya-va- „schwarzbraun, dunkel“, av. syava- „schwarz“, np. siyah „schwarz“ ... (s. Bartholomae Airan. Wb. 1631)'. This is the entry Pokorny 540-541 abridges, and it is where Bartholomae column 1631 (the number Nourai cites at node #1) comes from.\"\n        },\n        {\n          \"src\": \"AHD\",\n          \"where\": \"Watkins 1985, k-list (AHD_watkins1985.txt line 599)\",\n          \"stance\": \"supports\",\n          \"note\": \"'ḱei-2. Referring to various adjectives of color. 1. Suffixed o-grade form *koi-ro- in Germanic *hairaz, “gray-haired” ... HOAR ... 2. Suffixed zero-grade form *ḱi-wo- in Germanic *hiwam in Old English hīw, hēo, color, appearance, form: HUE. [Pok. 2. ḱei- 540.]'\"\n        },\n        {\n          \"src\": \"KLN\",\n          \"where\": \"s.v. cimex (KLN_1966.txt line 7676)\",\n          \"stance\": \"supports\",\n          \"note\": \"'cimex, n., bedbug. — L. cimex, „a bug“, lit. „the dark-brown insect“, cogn. with OI. śyamah, „black, blackish“, Avestic sama-, „black“, Lith. šernas ... Cp. chinch and the first element in syagush.' Klein assembles the same family as the chart.\"\n        }\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan\",\n          \"words\": \"syâva ; syâva-aršan ; syâ-maka\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Young Avestan siiiāuua- (transliterated syāva-) 'black' = Sanskrit śyāvá- 'dark brown', from PIE *ḱih₃-wo- / *ḱyē-wo-, the extended colour stem of Pokorny's kie-. The compound Siiiāuuaršan- (syāva-aršan-) is the name of the Kayanid prince, Bartholomae analysing it 'Komp.: syava- + arsan-, eig. „der Rapphengste besitzt“' — literally 'owning black stallions', which is what the chart's '(with) “black male” animals' with the cross-reference to Eres 1 (aršan- 'male, stallion') means. syamaka- is the -ka- derivative, in Avestan the name of a mountain (Bartholomae col. 1631-32) but in Sanskrit an ordinary adjective 'dark-coloured'; the gloss 'owner of “black hair“' Nourai takes from Bartholomae's own footnote, which reports that the Bundahišn calls that mountain syāmō.gaonō 'with black hair'.\",\n          \"derivation_fa\": \"اوستایی متأخر siiiāuua- (به آوانویسی syāva-) «سیاه» هم‌ریشه با سنسکریت śyāvá- «تیره، قهوه‌ای» و بازماندهٔ ستاک گستردهٔ *ḱih₃-wo- است. ترکیب Siiiāuuaršan- را بارتولمه در ستون ۱۶۳۱ چنین می‌کاود: «syava- + arsan-، یعنی دارندهٔ اسبان سیاه»؛ همین معنای «جانوران نر سیاه» در نمودار است. syāmaka- ساختهٔ پسوند -ka- است که در اوستا نام کوهی است و در سنسکریت صفت «تیره‌رنگ»؛ معنای «سیاه‌موی» را نورایی از پاورقی خود بارتولمه گرفته که می‌گوید بندهش آن کوه را syāmō.gaonō «با موی سیاه» خوانده است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%B3%DB%8C%D8%A7%D9%87\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"POK:541\",\n              \"status\": \"supports\",\n              \"note\": \"POK_02.txt leaf 199/200 (printed 541): 'Ai. syave-vd- „schwarzbraun, dunkel“, av. syava- „schwarz“, npers. siyah „schwarz“ ... ai. syame-md- ..., syamaka- „dunkelfarbig“ = av. syamaka- m. „Name eines Berges“ (auch sama- „schwarz“ mit s- aus sy-, Bartholomae Airan. Wb. 1571)'.\"\n            },\n            {\n              \"ref\": \"BRT:1631\",\n              \"status\": \"supports\",\n              \"note\": \"BRT.txt lines 27180-27195: the column number '1631' stands at line 27180, and immediately under it are 'j. syamaka- m. Name eines Bergs oder Gebirgs', 'j. syava- Adj. „schwarz“ ... ai. syava- Adj. „schwarzbraun“, np. siyah „schwarz“', and 'j. syavarsan- m. EN. eines iranischen Fürsten aus der Kavi-Dynastie ... Komp.: syava- + arsan-, eig. „der Rapphengste besitzt“'. All three of Nourai's Avestan words stand on precisely the cited column.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"WLD\",\n              \"where\": \"Bd. I 361 (WLD_Bd1 djvu line 22769)\",\n              \"stance\": \"supports\",\n              \"note\": \"'Ai. çya-va- „schwarzbraun, dunkel“, av. syava- „schwarz“, np. siyah „schwarz“, arm. (wohl iran. Lw.) seav „dunkel, schwarz“ (s. Bartholomae Airan. Wb. 1631)'.\"\n            },\n            {\n              \"src\": \"KNT\",\n              \"where\": \"Kent, Old Persian lexicon\",\n              \"stance\": \"silent\",\n              \"note\": \"No Old Persian *siyāva- is attested in Kent's lexicon; the colour word is known only from Avestan on the Old Iranian side, which is why the chart hangs the Persian word directly on the Avestan box.\"\n            }\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"sîyâh «سیاه» ; Sîyâvaš, Sîyâmak «سیاوش ، سیامک» ; sîyâhgŭš «سیاه‌گوش»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"NP سیاه siyāh 'black' goes back through MP syā / siyāh (MacKenzie: 'syā [syʼ] | (P syʼw, N siyāh) black') to Old Iranian *syaHwa-/*syaHwaka-; Horn's no. 761 states the base form outright: 'Als Grundform von np. siyāh ist *syavaka- anzusetzen', the -aka- suffix giving the final -h after loss of intervocalic -k- and -a. سیاوش Siyāvaš is the regular NP reflex of Av. Siiiāuuaršan- (MP Siyāwaxš, with -rš- > -xš- and then NP -š), and سیامک Siyāmak of syamaka-. سیاه‌گوش siyāh-gūš 'caracal' is a NP compound siyāh + gūš 'ear' (< OP gauša-), i.e. 'black-ear', named for the animal's black ear-tufts. On the chart's own NOTE: it is correct — Turkish qara qulaq 'black ear' is a calque of exactly the same idea and is the etymon of English/French caracal (Klein s.v. caracal; Webster 'Turk. qara qulaq'), so Persian siyāh-gūš and Turkish qara-qulaq are parallel formations, not borrowings of one another.\",\n          \"derivation_fa\": \"«سیاه» از فارسی میانهٔ syā/siyāh (مکنزی: «syā [syʼ] black») و آن از ایرانی باستان *syaHwaka- است؛ هرن در شمارهٔ ۷۶۱ (صفحهٔ ۱۶۸) صریحاً می‌نویسد «صورت اصلی فارسی نوی siyāh را باید *syavaka- نهاد»؛ هـ پایانی بازماندهٔ پسوند -aka- است. «سیاوش» دنبالهٔ اوستایی Siiiāuuaršan- (فارسی میانه Siyāwaxš) است که در آن -rš- به -xš- و سپس به ش بدل شده، و «سیامک» دنبالهٔ syamaka-. «سیاه‌گوش» مرکّب فارسی نو است (سیاه + گوش < پارسی باستان gauša-). یادداشت نورایی دربارهٔ qara qulaq ترکی درست است: این دو ساخت موازی‌اند نه وام‌گیری از یکدیگر.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%B3%DB%8C%D8%A7%D9%87\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"HRN:168\",\n              \"status\": \"supports\",\n              \"note\": \"HRN.txt \\\\f-leaf 189 = printed p.168, entry '761. siyah „schwarz“, siyahi. Semn. suah. aw. syava- „schwarz“ in Syavarsan-, Syavaspi-; phlv. siyak, siyah (PPGrl.), mand. LW. ...; ai. çyava- „braun, schwarzbraun“; arm. LW. seao „schwarz“ ... Als Grundform von np. siyah ist *syavaka- anzusetzen.' Horn even names Syāvaršan, i.e. the chart's سیاوش.\"\n            },\n            {\n              \"ref\": \"BQT:1199\",\n              \"status\": \"supports\",\n              \"note\": \"BQT_v2_pages.txt \\\\f-leaf 663; the next leaf carries the running head ۱۲۰۰, so this leaf is printed p.1199. It holds, side by side, 'سیاوش: بر وزن بناگوش، همان سیاوخش است که پسر کیکاوس باشد' and 'سیاه: بر وزن دگاه، معروفست که در مقابل سفید باشد' — both of Nourai's first two Persian items on the cited page.\"\n            },\n            {\n              \"ref\": \"SNS:172\",\n              \"status\": \"not_checked\",\n              \"note\": \"Tavoosi's Shayast-ne-Shayast glossary is on disk only as an unusable OCR (SNS_pages.txt / SNS.txt); greps for 'syʼ', 'syā', 'siyā' return a single garbled line (SNS_pages.txt:9399) and the printed page numbers are not legible in the OCR, so p.172 could not be located.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"PHD\",\n              \"where\": \"MacKenzie, Concise Pahlavi Dictionary (PHD_mackenzie.txt line 4725)\",\n              \"stance\": \"supports\",\n              \"note\": \"'syā [syʼ] | (P syʼw, N siyāh)] black' — the Middle Persian stage the chart omits.\"\n            },\n            {\n              \"src\": \"KLN\",\n              \"where\": \"s.v. syagush (KLN_1966.txt line 37765)\",\n              \"stance\": \"supports\",\n              \"note\": \"'Pers.-Hind. siyah-gosh, lit. „black ear“, fr. siyah, „black“, and gosh, „ear“. The first element is rel. to OI. syamah, Avestic sama, „black“ ... The second element derives fr. OPers. gausha-, ModPers. gosh, „ear“.'\"\n            },\n            {\n              \"src\": \"WEB\",\n              \"where\": \"Webster's New Twentieth Century Dict., s.v. caracal (WEB_vol1.txt line 27995)\",\n              \"stance\": \"supports\",\n              \"note\": \"'carʹa-cal, n. [Fr. caracal; Turk. qara qulaq; qara, black, and qulaq, ear.] 1. a lynx, the Lynx caracal ... its ears black externally, and tipped with long, black [hairs]' — confirms the chart's NOTE about Turkish kara-kulak.\"\n            }\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Hindustani\",\n          \"words\": \"\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"A deliberately empty pass-through box: the printed page (p.217) shows the Hindustani frame with no word in it, so the extraction is faithful. Its function is to mark the route by which the Persian compound reached English — Persian siyāh-gūš was taken into Urdu/Hindustani unchanged (سیاہ گوش siyāh-goš) as the ordinary name of the caracal in Mughal India, and Anglo-Indian usage picked it up from there. Klein labels his headword 'Pers.-Hind.' for exactly this reason, and Hobson-Jobson documents the Anglo-Indian stage.\",\n          \"derivation_fa\": \"این جعبه در کتاب عمداً تهی است (تصویر صفحهٔ ۲۱۷ هم قاب خالی «Hindustani» را نشان می‌دهد؛ پس خطای خوانش نیست) و تنها گذرگاه را نشان می‌دهد: مرکّب فارسی «سیاه‌گوش» بی‌تغییر وارد اردو\\/هندوستانی شد و از آنجا به انگلیسی هندواروپایی‌نشینان راه یافت؛ کلاین نیز همین را با برچسب «Pers.-Hind.» می‌آورد.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\n              \"ref\": \"None\",\n              \"status\": \"not_checked\",\n              \"note\": \"Empty pass-through node with no reference of its own; the claim is carried by KLN:1554 at the child node #4, which was checked.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"HJB\",\n              \"where\": \"Hobson-Jobson s.v. SHOE-GOOSE (HJB.txt line 20069)\",\n              \"stance\": \"supports\",\n              \"note\": \"'SHOE-GOOSE, s. This ludicrous corruption of the Pers. siyāh-gosh, lit. „black-ear“, i.e. lynx (Felis Caracal) occurs in the passage below from A. Hamilton'; and the 1813 quotation 'The Moguls train another beast for antelope-hunting called the Syah-gash, or black-ears, which appears to be the same as the caracal' — documents precisely the India-to-English route this empty box stands for.\"\n            },\n            {\n              \"src\": \"KLN\",\n              \"where\": \"s.v. syagush (KLN_1966.txt line 37765)\",\n              \"stance\": \"supports\",\n              \"note\": \"Klein's source label is 'Pers.-Hind. siyah-gosh', i.e. he too routes the English word through Hindustani.\"\n            }\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"English\",\n          \"words\": \"syagush\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English syagush (also siyahgosh, and in 18th-century sailors' folk-etymology 'shoe-goose') is a direct Anglo-Indian borrowing of Persian-Hindustani siyāh-goš, with the Persian -h- lost in the English spelling and the compound reduced to three syllables. Klein's entry gives the word and analyses it exactly as the chart does; Hobson-Jobson dates the English use to the 17th-19th centuries (A. Hamilton; Forbes, Oriental Memoirs i.277, 1813). It is a doublet of caracal, which reached English via French from the semantically identical Turkish qara qulaq.\",\n          \"derivation_fa\": \"انگلیسی syagush وام‌واژه‌ای مستقیم از «سیاه‌گوش» فارسی–هندوستانی است که هـ میانی در املای انگلیسی افتاده است. کلاین همین تحلیل را دارد و هابسن–جابسن شواهد سدهٔ ۱۹ را می‌آورد (و ریشه‌شناسی عامیانهٔ خنده‌دار shoe-goose را نیز). این واژه دوگانهٔ caracal است که از راه فرانسه از ترکی qara qulaq آمده است. ادعای نورایی درست است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\n              \"ref\": \"KLN:1554\",\n              \"status\": \"supports\",\n              \"note\": \"KLN_1966.txt line 37765 (vol. II, s-section): 'syagush, n., the caracal. — Pers.-Hind. siyah-gosh, lit. „black ear“, fr. siyah, „black“, and gosh, „ear“. The first element is rel. to OI. syamah, Avestic sama, „black“, and cogn. with L. cimex, „a bug“, lit. „the dark-brown insect“; see cimex. The second element derives fr. OPers. gausha-, ModPers. gosh, „ear“.' Klein says exactly what the chart's arrow says. Caveat: the archive OCR of Klein carries no printed folio numbers, so the page 1554 itself could not be verified — only the entry.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"HJB\",\n              \"where\": \"s.v. SHOE-GOOSE (HJB.txt lines 20069-20073)\",\n              \"stance\": \"supports\",\n              \"note\": \"'This ludicrous corruption of the Pers. siyāh-gosh, lit. „black-ear“, i.e. lynx (Felis Caracal)'; 1813 Forbes: 'the Syah-gash, or black-ears, which appears to be the same as the caracal, or Russian lynx.'\"\n            },\n            {\n              \"src\": \"WEB\",\n              \"where\": \"s.v. caracal (WEB_vol1.txt line 27995)\",\n              \"stance\": \"partial\",\n              \"note\": \"Webster records the animal only under caracal '[Fr. caracal; Turk. qara qulaq]'; syagush is the rarer of the two English names.\"\n            }\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Avestan\",\n          \"words\": \"sâma\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Young Avestan sāma- 'black' is the same colour word as syama-/syava-, with the cluster sy- simplified to s- and compensatory lengthening of the vowel; Pokorny states this explicitly on the cited page ('auch sama- „schwarz“ mit s- aus sy-, Bartholomae Airan. Wb. 1571'), the analysis going back to Bartholomae's Grundriss der iranischen Philologie I 37. Bartholomae's column 1571 in fact carries two entries: '¹sāma- Adj. „schwarz“' (used of a horse: aspahe kǝhrpa ...) and '²sāma- Adj. Name einer iranischen Familie', which is the bridge to the Persian name Sām in the next box. Klein reaches the same form from the other end, citing 'Avestic sama-, „black“' as the cognate of Latin cimex.\",\n          \"derivation_fa\": \"اوستایی sāma- «سیاه» همان واژهٔ syama-/syava- است که خوشهٔ sy- در آغاز به s- ساده شده و واکه به جبران کشیده شده است؛ خود پوکورنی در صفحهٔ ۵۴۱ می‌نویسد «sama- با s- از sy-، بارتولمه ستون ۱۵۷۱». در ستون ۱۵۷۱ دو مدخل هست: یکی صفت «سیاه» و دیگری نام خاندانی ایرانی — همین پل به «سام» فارسی است. ادعای نورایی درست است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\n              \"ref\": \"POK:541\",\n              \"status\": \"supports\",\n              \"note\": \"POK_02.txt printed p.541: 'ai. syamaka- „dunkelfarbig“ = av. syamaka- m. „Name eines Berges“ (auch sama- „schwarz“ mit s- aus sy-, Bartholomae Airan. Wb. 1571)'.\"\n            },\n            {\n              \"ref\": \"KLN:288\",\n              \"status\": \"partial\",\n              \"note\": \"Klein's entry that carries the form is 'cimex, n., bedbug. — L. cimex ... cogn. with OI. syamah, „black, blackish“, Avestic sama-, „black“' (KLN_1966.txt line 7676); the neighbouring page has 'chinch, n., the bedbug. — Sp. chinche, fr. L. cimicem ... See cimex' (line 7418). The content is Nourai's claim, but the archive OCR of Klein has no printed folio numbers and the two entries fall roughly a dozen pages apart, so which of them p.288 is could not be settled.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"BRT\",\n              \"where\": \"col. 1571 (BRT.txt lines 26182-26187)\",\n              \"stance\": \"supports\",\n              \"note\": \"The column marker '1571' at line 26182 is immediately followed by 'j. ¹sama- Adj. „schwarz“: aspahe kǝhrpa aurusahe ... aspahe kǝhrpa *mahe Yt. 8.18 und 31' and 'j. ²sama- Adj. Name einer iranischen Familie'.\"\n            },\n            {\n              \"src\": \"WLD\",\n              \"where\": \"Bd. I 361 (WLD_Bd1 djvu line 22771)\",\n              \"stance\": \"supports\",\n              \"note\": \"'(auch sama- „schwarz“ mit s- aus sy-, Bartholomae Grdr. d. iran. Phil. I 37, Airan. Wb. 1571)'.\"\n            }\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"Persian\",\n          \"words\": \"sâm «سام»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"The Shahnameh hero Sām, son of Nariman, father of Zāl and grandfather of Rostam, bears the family name that Avestan knows as ²sāma- (Bartholomae col. 1571), literally 'the black one'. Mo'in's own etymological footnote in his edition of Borhan-e Qate', on the very page Nourai cites, says so in as many words: 'در اوستا sāma (سیاه)، نام یک خانواده ایرانی است ... بارتولمه'. The name passes into MP and NP unchanged (the long ā is stable), and Mo'in adds that heroic tradition knows two Sāms, one the father of Aṭrat and one the descendant of Garšāsp and father of Zāl. He also warns that the homophonous سام 'Shem son of Noah' is a separate Hebrew word — a distinction the chart does not need to make.\",\n          \"derivation_fa\": \"«سام» نام پهلوان شاهنامه، پدر زال و نیای رستم، همان نام خاندانی است که اوستا آن را ²sāma- می‌خواند (بارتولمه، ستون ۱۵۷۱) و معنای تحت‌اللفظی آن «سیاه» است. حاشیهٔ ریشه‌شناختی معین در برهان قاطع، در همان صفحه‌ای که نورایی ارجاع می‌دهد، صریحاً می‌نویسد: «در اوستا sāma (سیاه)، نام یک خانواده ایرانی است، بارتولمه». واژه با آی کشیده بی‌دگرگونی به فارسی نو رسیده است. ادعای نورایی درست است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\n              \"ref\": \"BQT:1075\",\n              \"status\": \"supports\",\n              \"note\": \"BQT_v2_pages.txt \\\\f-leaves 537-538 (the سام entry runs across the column break; leaf 538's running head reads ۱۰۷۵). Text: 'سام: بروزن نام ... و نام پدر زال هم هست که جد رستم باشد'. Mo'in's footnote to it: 'در اوستا sāma (سیاه)، نام یک خانواده ایرانی است «بنا ... بارتولمه» ... دیگری نوادهٔ گرشاسپ و پدر زال، مزدیسنا'. This is precisely Nourai's arrow.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"BRT\",\n              \"where\": \"col. 1571 (BRT.txt line 26187)\",\n              \"stance\": \"supports\",\n              \"note\": \"'j. ²sama- Adj. Name einer iranischen Familie; ... samanqm Y.9.10' — the Avestan family name behind Persian Sām.\"\n            },\n            {\n              \"src\": \"FSF\",\n              \"where\": \"Noushin, Vazhe-namak (Shahnameh glossary)\",\n              \"stance\": \"silent\",\n              \"note\": \"The Shahnameh glossary treats Sām only as a proper name of the Nariman line and gives no etymology, so it neither supports nor contradicts the colour derivation.\"\n            }\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"Avestan\",\n          \"words\": \"saěna ; saěna-mereğa\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Avestan saēna- 'a large bird of prey, probably the eagle' is built on Pokorny's variant root form kiei-, beside Sanskrit śyená- 'eagle, falcon' and śyenī- 'light-coloured' — i.e. the bird is named after its colour, which is why it sits under this root. Bartholomae col. 1548 gives '¹saēna- m. Name eines grossen Raubvogels, wohl des Adlers', citing Yt.14.41 mǝrǝgō saēnō. One correction of form: Avestan has the two-word phrase mǝrǝgō saēnō 'the bird saēna', not a compound *saēna-mǝrǝga- in that order; the univerbation is Middle Persian (sēn-murw), so Nourai's 'saēna-mereğa' is a normalisation of the Avestan phrase rather than an attested Avestan compound. The chart's cross-reference to root 'Mereğa' (Av. mǝrǝga- 'bird') is correct.\",\n          \"derivation_fa\": \"اوستایی saēna- «پرندهٔ شکاری بزرگ، احتمالاً عقاب» بر گونهٔ kiei- همین ریشه ساخته شده و هم‌ریشه با سنسکریت śyená- «عقاب، باز» است؛ یعنی این پرنده را به رنگش نام داده‌اند و به همین سبب ذیل این ریشه جا گرفته است. بارتولمه در ستون ۱۵۴۸ آن را با شاهد یشت ۱۴، بند ۴۱ (mǝrǝgō saēnō) می‌آورد. یک نکتهٔ صوری: در اوستا این دو واژهٔ جدا است نه ترکیب saēna-mǝrǝga-؛ یکی‌شدن آن دو در فارسی میانه (sēn-murw) رخ داده است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\n              \"ref\": \"POK:541\",\n              \"status\": \"supports\",\n              \"note\": \"POK_02.txt printed p.541: 'auf einer Wurzelf. kiei- scheinen ai. syeni f. ... Farbbezeichnung „hell, weiß, rötlich“, und die nach der Farbe benannten ai. syena- m. „Adler, Falke“, av. saena- „ein großer Raubvogel, wohl Adler“ zu beruhen.'\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"BRT\",\n              \"where\": \"col. 1548 (BRT.txt lines 25766, 25786)\",\n              \"stance\": \"supports\",\n              \"note\": \"Column marker '1548' at line 25766; at 25786: 'j. ¹saena- m. Name eines grossen Raubvogels, wohl des Adlers: ... mǝrǝgō saenō Yt.14.41'. Note the Avestan wording is the phrase 'bird saēna', not a compound in the chart's order.\"\n            },\n            {\n              \"src\": \"WLD\",\n              \"where\": \"Bd. I 361 (WLD_Bd1 djvu, end of the kei- entry)\",\n              \"stance\": \"supports\",\n              \"note\": \"'ai. syena- m. „Adler, Falke“, av. saena- „ein großer Raubvogel, wohl Adler“ ... oder ist ein urar. *syaina- nach *aina- „bunt“ zu urar. siaina- geworden?' — Walde-Pokorny accept the connection but flag the vocalism as uncertain.\"\n            }\n          ]\n        },\n        {\n          \"id\": 8,\n          \"lang\": \"Persian\",\n          \"words\": \"šâhîn «شاهین» ; sîmorğ «سیمرغ»\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"The two words in this box do not have the same fate. سیمرغ sīmorġ is confirmed: it continues MP sēn-murw (MacKenzie p.75: '²sēn murw [synmwlw | (N sīmurġ)] a fabulous bird'), which univerbates the Avestan phrase mǝrǝgō saēnō; Horn's no. 765, on the page Nourai cites, has 'sīmurġ „Greif, Adler; N. pr.“ ... aw. saenō mereγō- „Adler“; phlv. sīnmurō, sēn murūk (Yātkār-ī Zarērān p.64); ai. çyena- „Falke“'; the modern popular reading 'سی مرغ = thirty birds' is a folk etymology and Wiktionary labels it as such. شاهین šāhīn is not: the standard etymology is MP šāhēn 'royal, kingly' = شاه šāh (< OP xšāyaθiya-) + the adjectival suffix -ēn/-īn, i.e. 'the royal bird', which is also how Horn classifies it — not under sīmurġ (no.765) but under šāh (no.772, p.170: 'šāh „König, Herrscher“, šāhāne, šāhī, šāhīn „Falke“'), with the Armenian loan šāhēn as witness. Wiktionary agrees, citing Justi's Iranisches Namenbuch. Nourai's derivation from saēna- is not his invention — Mo'in's footnote in Borhan p.1237 offers it as a secondary possibility ('شاید هم شاهین همان ... saena (رک: سیمرغ) باشد که در اوستا نام عقاب است') — but even Mo'in gives شاه as the primary source, and the phonology favours it: Av. saēna- would give NP *sēn/sīn (as it does inside sīmurġ), never šāhīn with initial š- and long ā. Because one of the two words in the box is wrongly derived, the node takes the worse verdict.\",\n          \"derivation_fa\": \"دو واژهٔ این جعبه سرنوشت یکسان ندارند. «سیمرغ» درست است: ادامهٔ فارسی میانهٔ sēn-murw است (مکنزی، صفحهٔ ۷۵) که خود یکی‌شدهٔ عبارت اوستایی mǝrǝgō saēnō است؛ هرن در شمارهٔ ۷۶۵ (صفحهٔ ۱۶۹) همین زنجیره را می‌آورد و خوانش عامیانهٔ «سی مرغ» ریشه‌شناسی عامیانه است. اما «شاهین» از saena- نیست: ریشه‌شناسی پذیرفته آن را از فارسی میانهٔ šāhēn «شاهانه»، یعنی شاه (از پارسی باستان xšāyaθiya-) + پسوند ‌ین می‌داند؛ هرن نیز آن را نه در مدخل سیمرغ بلکه در مدخل «شاه» (شمارهٔ ۷۷۲، صفحهٔ ۱۷۰) آورده است. معین در حاشیهٔ برهان قاطع (صفحهٔ ۱۲۳۷) احتمال saena را تنها با «شاید هم» می‌آورد و ریشهٔ اصلی را شاه می‌داند. از دید آوایی نیز saēna- در فارسی نو باید *سین می‌شد (چنان‌که در سیمرغ شده) نه شاهین.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%B4%D8%A7%D9%87%DB%8C%D9%86\",\n            \"https://en.wiktionary.org/wiki/%D8%B3%DB%8C%D9%85%D8%B1%D8%BA\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"HRN:169\",\n              \"status\": \"partial\",\n              \"note\": \"HRN.txt \\\\f-leaf 190 = printed p.169 carries only sīmurġ: '765. sīmurġ „Greif, Adler; N. pr.“, vergl. Sīn-duxt. aw. saenō mereγō- „Adler“; phlv. sīnmurō, sēn murūk (Yātkār-ī Zarērān S.64). ai. çyena- „Falke“; arm. cin milvus'. شاهین is not on this page at all: Horn puts it on p.170, no. 772, under šāh — 'šāh „König, Herrscher“, šāhāne, šāhī, šāhīn „Falke“. ap. xšāyaθiya- „Herrscher“', with the footnote '„Sāhen“, vergl. arm. LW. šahen'. So Horn supports the sīmorġ arrow and contradicts the šāhīn arrow.\"\n            },\n            {\n              \"ref\": \"BQT:1237\",\n              \"status\": \"partial\",\n              \"note\": \"BQT_v3_pages.txt pdf page 28, whose head reads '-۱۲۳۷-': 'شاهین: بر وزن ... معروف است، و آن پرنده‌ای باشد شکاری ... و زبانه ترازو ...'. Mo'in's footnote: 'از ... شاه درآمده و این پرنده بمناسبت شکوه و توانایی و تقدس خود ... خوانده شده باشد (قی: شاهباز). شاید هم شاهین همان ... saena (رک: سیمرغ) باشد که در اوستا نام عقاب (= آله) است'. Mo'in therefore offers Nourai's derivation, but only as a 'perhaps', after deriving the word from شاه.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"PHD\",\n              \"where\": \"MacKenzie p.75 (PHD_mackenzie.txt line 4542)\",\n              \"stance\": \"supports\",\n              \"note\": \"'²sēn murw [synmwlw | (N sīmurġ)] a fabulous bird' — the Middle Persian link for sīmorġ (and note that the reflex of saēna- in Middle Persian is sēn-, with s- and ē, not šāh-).\"\n            },\n            {\n              \"src\": \"HUB\",\n              \"where\": \"Hübschmann, Persische Studien\",\n              \"stance\": \"silent\",\n              \"note\": \"Hübschmann has no separate treatment of شاهین; his Persian-Armenian material for šāh and its derivatives (including Arm. šahen) is what Horn no. 772 cites.\"\n            }\n          ]\n        },\n        {\n          \"id\": 9,\n          \"lang\": \"Sogdian\",\n          \"words\": \"š`w\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Sogdian šʼw (Gharib's transcription sʼw, read šāw/šāu) 'black' is the eastern Iranian cognate of Avestan syāva-: Proto-Iranian *syāwa- gives Sogdian šāw by the regular Sogdian development of initial *sy- to š-, while the same cluster gives s- in Persian (siyāh) — the two branches diverge exactly here. Gharib herself glosses the entry with the Avestan etymon and the living cognates. The derivative šʼw-pʼmʼk 'blackish' (entry 9178) confirms the reading.\",\n          \"derivation_fa\": \"سغدی šʼw «سیاه» هم‌ریشهٔ شرقی اوستایی syāva- است: خوشهٔ آغازین *sy- در سغدی به ش بدل شده در حالی که در فارسی به س مانده است (سیاه)؛ همین‌جا دو شاخهٔ ایرانی از هم جدا می‌شوند. بدرالزمان قریب در فرهنگ سغدی خود (مدخل ۹۱۷۷) همین اشتقاق را می‌آورد. ادعای نورایی درست است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\n              \"ref\": \"SOD:370\",\n              \"status\": \"supports\",\n              \"note\": \"SOD_pages.txt, the leaf whose foot carries the printed number '371' (so the entry itself sits on the p.370/371 opening): entry '9177 sʼw B, M, S / saw/u ⊙Av. syava; Yaghn. sow-, Oss. səu ⊙ob. / black', followed by '9178 sʼw-pʼmʼk / saw-pame / blackish'. Gharib's own etymological note names Avestan syava-, exactly Nourai's parent.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"SOD\",\n              \"where\": \"entry 9177 (SOD_pages.txt line 30204 ff.)\",\n              \"stance\": \"supports\",\n              \"note\": \"As quoted; Gharib also gives the Yaghnobi (sow-) and Ossetic (səu) cognates, both continuing the same *syāwa-.\"\n            },\n            {\n              \"src\": \"POK\",\n              \"where\": \"IEW 541\",\n              \"stance\": \"silent\",\n              \"note\": \"Pokorny cites no Sogdian for this root; his Iranian evidence is Avestan and New Persian only, so Gharib is the sole check on this node.\"\n            }\n          ]\n        },\n        {\n          \"id\": 10,\n          \"lang\": \"Germanic\",\n          \"words\": \"hiwan : color, hue\",\n          \"verdict\": \"transcription_suspect\",\n          \"derivation\": \"The root and the meaning are right, but the Germanic form is not the one the sources know. The Germanic word for 'colour, appearance' is neuter *hiwam (Gothic hiwi 'Schein, Aussehen', OE hīw/hēo, ON hý, Swedish hy), from PIE *ḱi-wo-; Watkins, the very reference the box cites, prints 'Suffixed zero-grade form *ḱi-wo- in Germanic *hiwam in Old English hīw, hēo, color, appearance, form: HUE'. A Germanic *hiwan- does exist, but it is a different word belonging to Pokorny's other root 1. kei- 'to lie, home': OE hīwan 'members of a household' (Watkins, ḱei-1: 'Germanic *hiwa- in Old English hīwan, members of a household: HIND'). Nourai's 'hiwan' therefore looks like *hiwam with -m misread or miscopied as -n, which happens to collide with the household word. I checked the printed page (pdf p.247 = book p.217, image saved as data/verification/sources/refs/ocr/BOOK/247.png): the book itself prints 'hiwan : color, hue', so the extraction is faithful and the slip is Nourai's own.\",\n          \"derivation_fa\": \"ریشه و معنا درست است ولی صورت ژرمنی نادرست. صورت شناخته‌شده *hiwam (خنثی) است که گوتی hiwi «نمود، ظاهر»، انگلیسی کهن hīw/hēo و سوئدی hy ادامهٔ آن‌اند؛ واتکینز در همان پیوست AHD که نورایی ارجاع می‌دهد می‌نویسد «Germanic *hiwam in Old English hīw, hēo». صورت *hiwan- وجود دارد اما از ریشهٔ دیگری (kei- «خوابیدن، خانه») است و معنای «اهل خانه» می‌دهد. تصویر صفحهٔ چاپی ۲۱۷ را دیدم: خود کتاب «hiwan» چاپ کرده؛ پس این خطای چاپی کتاب است نه خطای خوانش اسکن.\",\n          \"error_in\": \"book\",\n          \"book_prints\": \"hiwan\",\n          \"correct_form\": \"*hiwam (Gothic hiwi, Old English hīw/hēo)\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/hue\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"AHD\",\n              \"status\": \"partial\",\n              \"note\": \"AHD_watkins1985.txt line 599, s.v. ḱei-2: '2. Suffixed zero-grade form *ḱi-wo- in Germanic *hiwam in Old English hīw, hēo, color, appearance, form: HUE.' Watkins supports the root, the meaning and the English outcome, but writes *hiwam, not 'hiwan'; his 'hīwan' (line 595, under ḱei-1) is the unrelated household word.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"POK\",\n              \"where\": \"IEW 541\",\n              \"stance\": \"partial\",\n              \"note\": \"'got. hiwi n. „Schein, Aussehen“, aisl. hy n. „feines Haar, Flaum“, schwed. hy „Haut, Hautfarbe“, ags. hiew, hi(o)w n. „Erscheinung, Farbe, Schönheit“, engl. hue „Farbe“ (idg. *ki-wo-)' — Gothic hiwi, no n-stem.\"\n            },\n            {\n              \"src\": \"WLD\",\n              \"where\": \"Bd. I 360-361 (WLD_Bd1 djvu lines 22738 ff.)\",\n              \"stance\": \"partial\",\n              \"note\": \"'got. hiwi n. „Schein, Aussehen“, anord. hy n. „Flaum, Härchen“ ... engl. hue „Farbe“ ... aus idg. *ki-un-'; Walde-Pokorny call the derivation 'unsicher' and float an alternative connection to sqeu- 'bedecken'.\"\n            },\n            {\n              \"src\": \"KLN\",\n              \"where\": \"s.v. hue (Klein, English section)\",\n              \"stance\": \"partial\",\n              \"note\": \"Klein likewise gives OE hīw, hēow with Goth. hiwi, ON hý; no Germanic n-stem is on offer anywhere for the colour word.\"\n            }\n          ]\n        },\n        {\n          \"id\": 11,\n          \"lang\": \"English\",\n          \"words\": \"hue\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"OE hīw/hēow 'colour; form, appearance; species; beauty' > ME hewe > NE hue, the OE īw/ēow diphthong giving ME /iu/ and then NE /juː/. Etymonline: 'from Proto-Germanic *hiwam, which reconstructs to PIE *kiwo-, a suffixed form of the root *kei- (2)', with Gothic hiwi 'form, appearance' and Swedish hy 'skin, complexion' as cognates; it notes the word was 'a common word in Old English, squeezed into obscurity after c. 1600 by color', then revived in the 1850s as a technical term of chromatics. Watkins lists HUE as the English outcome of ḱei-2.\",\n          \"derivation_fa\": \"انگلیسی hue از انگلیسی کهن hīw/hēow «رنگ؛ شکل، نمود؛ زیبایی» است که از ژرمنی آغازین *hiwam و آن از *ḱi-wo- هندواروپایی می‌آید؛ هم‌ریشه با گوتی hiwi و سوئدی hy. ایتیمانلاین می‌افزاید که این واژه پس از حدود ۱۶۰۰ میلادی در برابر color کم‌کاربرد شد و در سدهٔ ۱۹ دوباره اصطلاح فنی رنگ‌شناسی شد. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/hue\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"None\",\n              \"status\": \"not_checked\",\n              \"note\": \"No reference of its own; it inherits the AHD citation of node #10, which lists HUE explicitly.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"AHD\",\n              \"where\": \"Watkins 1985, s.v. ḱei-2 and the English index (AHD_watkins1985.txt lines 599, 1657)\",\n              \"stance\": \"supports\",\n              \"note\": \"'... in Old English hīw, hēo, color, appearance, form: HUE'; the reverse index confirms 'HUE¹ ḱei-2'.\"\n            },\n            {\n              \"src\": \"POK\",\n              \"where\": \"IEW 541\",\n              \"stance\": \"supports\",\n              \"note\": \"'ags. hiew, hi(o)w n. „Erscheinung, Farbe, Schönheit“, engl. hue „Farbe“ (idg. *ki-wo-)'.\"\n            }\n          ]\n        },\n        {\n          \"id\": 12,\n          \"lang\": \"Latin\",\n          \"words\": \"cimex\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Latin cīmex, -icis 'bedbug' is derived by Pokorny (on the cited page) and by Klein from the reduced grade *kī-mo- of this colour root, the insect being named 'the dark-coloured one', with the -c- formant and consonantal declension of sene-x beside *seno-s; Prellwitz first proposed it (BB 30, 176) and Walde-Pokorny I 361 repeat it. Modern Latin etymology is more reserved: Ernout-Meillet, s.v. cimex, class it as 'mot populaire, même suffixe que dans culex, pulex' and conclude flatly 'sans étymologie, comme la plupart des mots de ce genre'; Etymonline likewise calls the Latin word 'of uncertain origin'. The chart's arrow is thus a respectable older view rather than a settled one, and the gloss 'black bug' is Nourai's rendering of Pokorny's parenthetical '„dunkelfarbig“', not a dictionary meaning.\",\n          \"derivation_fa\": \"لاتین cīmex «ساس، کیک تختخواب» را پوکورنی و کلاین از گونهٔ کاهیدهٔ *kī-mo- همین ریشهٔ رنگ می‌دانند، یعنی «جانور تیره‌رنگ»، با پسوند -c- و گردان همخوانی مانند sene-x. اما ریشه‌شناسی امروزی لاتین محتاط‌تر است: ارنو–مییه ذیل cimex می‌نویسد «mot populaire ... sans étymologie» و ایتیمانلاین نیز آن را «نامعلوم‌الاصل» می‌خواند. پس ادعای نورایی با احتیاط پذیرفتنی است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/chinch\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"POK:541\",\n              \"status\": \"supports\",\n              \"note\": \"POK_02.txt printed p.541: 'reduktionsstufig *kī-mo- wahrscheinlich in lat. cīmex „Wanze“ („dunkelfarbig“; Formans -co-, als Subst. nach der kons. Dekl. wie sene-x zu idg. *seno-s); vielleicht im gr. EN. Kīmōn.' Note Pokorny's own hedge, 'wahrscheinlich'.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"LAT\",\n              \"where\": \"Ernout-Meillet s.v. cimex (LAT.txt lines 11865-11871)\",\n              \"stance\": \"contradicts\",\n              \"note\": \"'cimex, -icis m.: punaise. Déjà dans Liv. Andr. ... Mot populaire. Même suffixe que dans culex, pulex; v. Ernout, Philologica, p.141. ... Sans étymologie, comme la plupart des mots de ce genre.'\"\n            },\n            {\n              \"src\": \"KLN\",\n              \"where\": \"s.v. cimex (KLN_1966.txt line 7676)\",\n              \"stance\": \"supports\",\n              \"note\": \"'L. cimex, „a bug“, lit. „the dark-brown insect“, cogn. with OI. syamah, „black, blackish“, Avestic sama-, „black“, Lith. šernas, „bluish grey, grey“. Cp. chinch and the first element in syagush.'\"\n            },\n            {\n              \"src\": \"WLD\",\n              \"where\": \"Bd. I 361 (WLD_Bd1 djvu line 22773)\",\n              \"stance\": \"supports\",\n              \"note\": \"'reduktionsstufig ki-mo- wahrscheinlich (nach Prellwitz BB. 30, 176) in lat. cīmex „Wanze“ („dunkelfarbig“ ...; Vf. LEWb.² s.v.)' — with the same 'wahrscheinlich'.\"\n            }\n          ]\n        },\n        {\n          \"id\": 13,\n          \"lang\": \"English\",\n          \"words\": \"cimex, chinch\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Two different kinds of English word from the same Latin etymon. cimex is a learned zoological borrowing of the Latin nominative, the genus name of the bedbug (Cimex lectularius, Linnaeus 1758), taken directly into scientific and then general English. chinch 'bedbug' (and in America the chinch bug of wheat) came in about the 1620s through Spanish/Portuguese chinche, which continues the Latin accusative cīmicem by the ordinary Ibero-Romance treatment (-īc- > -č-, whence Sp. chinche; cf. the diminutive chinchilla). Klein and Etymonline give exactly this chain.\",\n          \"derivation_fa\": \"دو واژهٔ انگلیسی از یک اصل لاتین: cimex وام‌واژه‌ای عالمانه و مستقیم از صورت فاعلی لاتین است (نام جنس جانورشناختی Cimex)، ولی chinch در حدود ۱۶۲۰ میلادی از راه اسپانیایی\\/پرتغالی chinche وارد شده که خود ادامهٔ صورت مفعولی cīmicem است (دگرگونی معمول -īc- > -č- در رومانی ایبری). کلاین و ایتیمانلاین همین زنجیره را می‌آورند. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/chinch\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"None\",\n              \"status\": \"not_checked\",\n              \"note\": \"The node carries no reference of its own; it inherits POK:541 from node #12, and Klein's cimex/chinch entries were consulted instead.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"KLN\",\n              \"where\": \"s.v. chinch and s.v. cimex (KLN_1966.txt lines 7418, 7676)\",\n              \"stance\": \"supports\",\n              \"note\": \"'chinch, n., the bedbug. — Sp. chinche, fr. L. cimicem, acc. of cimex, „bedbug“. See cimex.' and 'cimex, n., bedbug. — L. cimex ...' — both English headwords are in Klein exactly as the box has them.\"\n            },\n            {\n              \"src\": \"WEB\",\n              \"where\": \"Webster's New Twentieth Century Dictionary\",\n              \"stance\": \"supports\",\n              \"note\": \"Webster carries cimex as the zoological genus of the bedbug and chinch/chinch bug as the Spanish-derived popular name, matching the split described above.\"\n            }\n          ]\n        }\n      ]\n    }\n  ]\n}\n"
}
```


### [2026-09-06T16:19:13.172Z] TOOL RESULT

```
File created successfully at: /home/sfmqrb/git/rishe/data/verification/page-247.json (file state is current in your context — no need to Read it back)
```


## [2026-09-06T16:19:17.972Z] TOOL CALL #83: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-247.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 247",
 "description": "Validate JSON and run verify_check"
}
```


### [2026-09-06T16:19:20.469Z] TOOL RESULT

```
JSON OK
nodes verified: 20/20
node verdicts: {'disputed': 2, 'confirmed': 14, 'plausible': 3, 'transcription_suspect': 1}
root verdicts: {'confirmed': 2}
ref checks: {'contradicts': 1, 'supports': 14, 'partial': 7, 'not_checked': 5}
books consulted: {'silent': 7, 'partial': 8, 'supports': 29, 'contradicts': 2} | by book: {'POK': 6, 'WLD': 6, 'KLN': 5, 'BRT': 4, 'PHD': 4, 'WEB': 3, 'IEC': 2, 'BQT': 2, 'AHD': 2, 'HJB': 2, 'MON': 1, 'LKT': 1, 'TAD': 1, 'ARB': 1, 'PLA': 1, 'KNT': 1, 'FSF': 1, 'HUB': 1, 'SOD': 1, 'LAT': 1}
```


## [2026-09-06T16:19:25.748Z] TOOL CALL #84: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"KNT:\"; grep -c -i \"siyava\\|syava\" KNT.txt; echo \"HUB shahin:\"; grep -c -i \"sahin\\|šāhīn\\|schahin\" HUB.txt; echo \"FSF sam:\"; grep -c \"سام\" FSF.txt; echo \"KLN hue:\"; grep -n \"^hue,\\|hue,  n\\.\" KLN_1966.txt | head -3",
 "description": "Verify silent-source claims"
}
```


### [2026-09-06T16:19:25.832Z] TOOL RESULT

```
KNT:
18
HUB shahin:
0
FSF sam:
85
KLN hue:
8157:Cohosh,  n.,  name  of  several  N.  American  medic¬ inal  plants.  —  Of  Algonquian  origin, cohue,  n.,  rout,  mob,  tumult.  —  F.,  orig.  ‘hall’, fr.  MBret.  cochuy.
18195:hue,  n.,  color.  —  ME.  hew,  hewe,  fr.  OE.  hlw, hiew,  ‘form,  shape,  appearance;  color’,  rel.  to ON.  hy,  ‘bird’s  down’,  Swed.  hy,  ‘skin,  com¬ plexion’,  Goth.  him. ,  ‘form,  appearance’,  OE. hxwen,  ‘bluish  gray,  blue’,  prob.  also  to  OE. har,  ‘gray’  (see  hoar),  and  prob.  cogn.  with OSlav.  sivu,  ‘gray’.  Lith.  syvas,  ‘white’,  OPruss. sywan,  ‘gray’,  OI.  syavas,  ‘blackish  brown’. Derivatives:  hue,  tr.  and  intr.  v.,  to  color,  hu-ed, hue-less,  adjs.,  hue-less-ness,  n.
18196:hue,  n.,  an  outcry.  —  ME.,  fr.  OF.  hu,  fr.  huer, ‘to  cry  out,  shout’,  which  is  of  imitative  origin. Cp.  hoot.  Cp.  also  howlet.
```


## [2026-09-06T16:19:31.530Z] TOOL CALL #85: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"siyava\\|syava\" KNT.txt | head -8; echo \"=== FSF sam ===\"; grep -n \"^سام\\|سام \" FSF_pages.txt | head -6",
 "description": "Check Kent siyava and FSF sam"
}
```


### [2026-09-06T16:19:31.589Z] TOOL RESULT

```
1402:‘death’, cf. -30- in OP martiya ‘man’. adurujiya ‘he lied’, cf. drauga ‘the Lie’. asiyava ‘he went forth’, Skt. (mid.) deyavala.
2583:II. The secondary ending was pIE -nt, which - lost the final ¢ in pAr. unless sentence phonetics ` permitted its retention; for in pAr. only a single consonant could stand at the end of a word. In OP, also, the final n was not written (§112). Be- fore this ending the thematic vowel was -o-: pIE *ebheront, Gk. égepov, Skt. dbharan, OP abara”; OP abava", anaya”, ayauda", asiyava", alarsa”, agar- báya"; passive арата", ayadiya". Non-thematic stems would normally have pIE -nt after conso- nants, becoming pAr. -at; but this was commonly replaced by -an(t) after the -am of the Ist sg.: pIE *és-nt, but Skt. азат, ОР аһа”; OP apariy- diya”, avájana",
2668:G. To express the goal; names of places are often used thus without a preposition (regularly with fra-ais-, ar-, ava-ar-, pard-ar-, Siyav-), but names of persons always have the preposition: DB 8.82 abiy avam Аттат asiyava Babirum; exception DB 5.21f a&yavam abiy Saküm, cf. DB 2.72, 3.73f (Styav-), 2.721 (fra-ats-), DB 5.23f (ava-ar-), DPe 24 (ni-ar-). With ay- ‘go’ places as well ав persons take prepositions, ef. DB 1.91f, 3.73, DZe 11 for places, DB 1.93, 2.32f for persons.
3487:31 büjiya : avam : Bardiyam : avàja * уаба : Kabüjiya : Bardiyam : avaja : kürahy 32 à : пазу : azdà : abava : (уа : Bardiya : avajata : раѕауа : Kabijiya : Mudráyam 33 : akiyava : уада : Kabūjiya : Mudrayam : aSiyava : pasáva : kara : апка : abava 34 : pasava : drauga : dahyauvi : vasiy : abava : uta : Parsaiy : ша : Mádaiy : ut 35 d:aniy&uvà : dahyuSuvà ; 0àtiy : Dàrayavaus :х3йуайуа : pa
3490:40 àt& : pasiva : kira : haruva : hamigiya : abava : haeà : Kabüjiyà : abiy : avam : 4] aSiyava : uta : Parsa : ша : Mada : uta : aniyà : dahyáva : xfagam : hauv
3527:72 iya : ima : tya : adam : akunavam : pasiiva : уай : xSayabiya : abavam ‚ 73 : Dürayavaus : xSdyabiya : уа : adam : Gaumatam : tyam : magum : avüjanam : ра 74 sīva : I martiya : Agina : пата : Upadarmahya : puça : hauv : udapatalá : Uujai 75 y : kàrahyà ; ava : afaha : adam : Üvjaiy : xiiiyasiya : amiy : pasdva : Uv 76 пуй: hamigiya : ауа :abiy : avam : Aginam : aSiyava : hauv : xšđyaðiya . TI :abava : Üvjaiy : uti : I martiya : Babiruviya : Naditabaira : патол : Ainatrahy
3529:78 à : puça : hauv : udapatatà : Babirauv : káram : ауада : adurujiya : adam : Nab 79 uk"dracara : amiy : hya : Nabunaitahy& : риса : pasava : kära : һуа : Babiruviya 80 : hamva : ably : avam : Naditabairam : aSiyava : Babirus : hamigiya : abava : x
3535:84 birum : asiyavam : abiy : avam : Naditabairam : hya : Nabuk'dracara : agaubatà 85 : kara : пуа : Naditabairahya : Tigrám : adàraya : avada : aistatà : uta : i abiš : nāviyā : dha : pasiva : adam : küram : maškāuvā : avakanum : aniyam : usa : 87 bürim : akunavam : aniyahyà : asam : frinayam : Auramazdàmaiy : upastim 88 : abara : vaSnà : Auramazdaha : Tigrām : viyatarayama : avadà : avam : kàram : 80 tyam : Naditabairahyà : adam : ajanam : vasiy : ыз MR E rau
=== FSF sam ===
1336:   ‫از آفاق عالم اجسام است کهدنیا باشد‪»...‬‬                        ‫ادزمکلنیلهه(و‪:)۱۰۱-۴۱‬‬
1458:        ‫صیغۀ امر از آلودن به معنی مالیدن‪:‬‬                         ‫جو آگاهی آمد به سام دلیر‬
2022:                            ‫‪۳۲۴۱‬‬                                ‫سام دربارة زال گوید‪:‬‬
3511:                 ‫بیامد بر سام یل پرده‌دار‬
3698:            ‫بیامد کتهوید گنزردان برد‬                       ‫می‌گشاید‪ .‬سام نرم می‌شود و می‌گوبد‪:‬‬
4125:                                                              ‫بجای خرد سام سنگی بود‬
```


## [2026-09-06T16:19:41.382Z] TOOL CALL #86: Edit

```json
{
 "replace_all": false,
 "file_path": "/home/sfmqrb/git/rishe/data/verification/page-247.json",
 "old_string": "              \"note\": \"No Old Persian *siyāva- is attested in Kent's lexicon; the colour word is known only from Avestan on the Old Iranian side, which is why the chart hangs the Persian word directly on the Avestan box.\"",
 "new_string": "              \"note\": \"Kent's Old Persian lexicon has no colour word *siyāva-; every hit for 'siyava' in KNT.txt is the verb form ašiyava 'he went forth' (Behistun, e.g. DB 3.31-33 'Kabūjiya Mudrāyam ašiyava'), from šiyav- 'to go', a homograph of no relevance. On the Old Iranian side the colour word is known from Avestan only, which is why the chart hangs the Persian word directly on the Avestan box.\""
}
```


### [2026-09-06T16:19:41.428Z] TOOL RESULT

```
The file /home/sfmqrb/git/rishe/data/verification/page-247.json has been updated successfully. (file state is current in your context — no need to Read it back)
```


## [2026-09-06T16:19:46.532Z] TOOL CALL #87: Edit

```json
{
 "replace_all": false,
 "file_path": "/home/sfmqrb/git/rishe/data/verification/page-247.json",
 "old_string": "          \"note\": \"The Shahnameh glossary treats Sām only as a proper name of the Nariman line and gives no etymology, so it neither supports nor contradicts the colour derivation.\"",
 "new_string": "          \"note\": \"Noushin's Shahnameh glossary carries سام only inside quoted verses ('جو آگاهی آمد به سام دلیر', 'بیامد بر سام یل پرده‌دار', FSF_pages.txt leaves 1458, 3511) as the proper name of Zāl's father, with no etymological note, so it neither supports nor contradicts the colour derivation.\""
}
```


### [2026-09-06T16:19:46.558Z] TOOL RESULT

```
The file /home/sfmqrb/git/rishe/data/verification/page-247.json has been updated successfully. (file state is current in your context — no need to Read it back)
```


## [2026-09-06T16:19:49.337Z] TOOL CALL #88: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-247.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 247",
 "description": "Re-validate after edits"
}
```


### [2026-09-06T16:19:51.234Z] TOOL RESULT

```
JSON OK
nodes verified: 20/20
node verdicts: {'disputed': 2, 'confirmed': 14, 'plausible': 3, 'transcription_suspect': 1}
root verdicts: {'confirmed': 2}
ref checks: {'contradicts': 1, 'supports': 14, 'partial': 7, 'not_checked': 5}
books consulted: {'silent': 7, 'partial': 8, 'supports': 29, 'contradicts': 2} | by book: {'POK': 6, 'WLD': 6, 'KLN': 5, 'BRT': 4, 'PHD': 4, 'WEB': 3, 'IEC': 2, 'BQT': 2, 'AHD': 2, 'HJB': 2, 'MON': 1, 'LKT': 1, 'TAD': 1, 'ARB': 1, 'PLA': 1, 'KNT': 1, 'FSF': 1, 'HUB': 1, 'SOD': 1, 'LAT': 1}
```


## [2026-09-06T16:20:09.860Z] AGENT

Page 247 (book p. 217) verified. `verify_check.py 247`: 20/20 nodes, **0 PROBLEM lines**.

**Verdicts** — roots: 2 confirmed. Nodes: 14 confirmed, 3 plausible, 2 disputed, 1 transcription_suspect.

**Disputed**
- *Keg/Keng* #1 **[Avestan] cang "hook"** — no Avestan *čanga- exists (Bartholomae silent); Pokorny 537, Nourai's own citation, prints the form as **"Npers. čang"**. The word and root are right, the language stage is wrong (it duplicates node #2).
- *Kei 1* #8 **šâhîn «شاهین»** — not from Av. saēna-. Horn puts it on p.170 under **šāh** (šāh + -īn, MP šāhēn "kingly"), and Wiktionary/Justi agree; Av. saēna- yields NP *sēn-* (as inside سیمرغ), never šāhīn. Mo'in (BQT 1237) offers Nourai's derivation only as a "شاید هم". The other word in the box, **sîmorğ**, is fully confirmed (MP sēn-murw, MacKenzie p.75; Horn no. 765).

**transcription_suspect**
- *Kei 1* #10 **Germanic "hiwan"** — the colour word is *hiwam (Goth. hiwi, OE hīw); *hiwan- is the unrelated household word under Pokorny's 1. kei- "to lie". `error_in: book` — I read the printed page (image saved to `data/verification/sources/refs/ocr/BOOK/247.png`); the book itself prints "hiwan", so the extraction is faithful.

**plausible**
- #3 Arabic **ṣanj** and #4 Persian **صنج** — Asbaghi (PLA 188, the cited page) splits two homonyms: ṣanj "harp" ← čang (Nourai's route), but ṣanj "cymbal/castanets" ← Persian **zang**. Nourai's own note flagging root "Gěu 1" points the right way for the cymbal sense.
- #12 Latin **cimex** — Pokorny/Klein connect it to *ḱī-mo- "dark-coloured", but Ernout-Meillet says "sans étymologie" and Etymonline "of uncertain origin".

**No extraction errors found.** The JSON matches the printed chart everywhere I checked (incl. the empty Hindustani box, which is empty in the book too).

Notable confirmations: IEC:458 is exact — Mann's p.458 has both `kag- "hook, claw"` and `kaĝ- ... Per. kaj "bent"`, which is where Nourai's fifth root-name "Kag" and node #5 come from. BQT:1199 and BQT:1075 are exact page hits (Mo'in's footnote at 1075 reads "در اوستا sāma (سیاه)، نام یک خانواده ایرانی است، بارتولمه"). SOD:370 = Gharib entry 9177 with her own "⊙Av. syava". One ref not checkable: **SNS:172** — the Shayast-ne-Shayast glossary OCR on disk is unusable and its printed page numbers are illegible.
