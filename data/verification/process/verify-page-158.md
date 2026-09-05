# Verification process log — verify-page-158


## [2026-09-05T20:29:15.065Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 158 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-158.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-158.json. Write /home/sfmqrb/git/rishe/data/verification/page-158.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 158` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-05T20:29:16.607Z] AGENT

I'll start by reading the instructions.


## [2026-09-05T20:29:17.317Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-05T20:29:17.332Z] TOOL RESULT

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


## [2026-09-05T20:29:17.687Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-158.txt"
}
```


### [2026-09-05T20:29:17.708Z] TOOL RESULT

```
1	=== PDF page 158 (book page 128) ===
2	--- entry 0 ---
3	ROOT [Akkadian] Erěbu : to enter, to go down (sunset)  (refs AKD:64; KLN:550)
4	#1 (parent #0) [Arabic] refs=AKD:640,854 | ğ.r.b : to set (sun) ; mağreb : sunset, west ; Mağreb al aqsâ : "west of the extreme", Morocco
5	  #2 (parent #1) [Persian] refs=MON | ğarb «غرب» : west | extra: مغرب ، غروب
6	  #3 (parent #1) [Italian] refs=AHD:854 | Marocco : Morocco
7	    #4 (parent #3) [Arabic] refs=None | Marâkeš
8	      #5 (parent #4) [Persian] refs=None | Marâkeš «مراکش» : Morocco | NOTE: MON6:1946 derives this from a different Arabic root.
9	    #6 (parent #3) [English] refs=AHD:854; NAT:163 | Morocco
10	#7 (parent #0) [Hebrew] refs=AKD:64; KLN:550 | `erebh : sunset, west
11	  #8 (parent #7) [Greek] refs=KLN:550; AHD:452 | europa : land of sunset
12	    #9 (parent #8) [Latin] refs=AHD:452 | eurôpa : Europe
13	      #10 (parent #9) [French] refs=None | Europe
14	        #11 (parent #10) [Persian] refs=None |  «اروپا»
15	      #12 (parent #9) [English] refs=AHD | Europe
16	--- entry 1 ---
17	ROOT [Indo-European] Ered, Erdh, Weredh, Werdh : to grow, high  (refs POK:339,1167; KLN:1097)
18	#1 (parent #0) [Avestan] refs=POK:339,1167 | eredva : high ; vared, vard, ward : up, high, growing
19	  #2 (parent #1) [Persian] refs=HRN:39,210; BQT:227,1848; FFD:35 | vâlâ «والا» : great, high ; bâlîdan «بالیدن» : to grow, boast | extra: بال ۲ ، بالش ۲ | NOTE: See root "Bhel" for derivation of Persian "bâlesh 1: pillow".
20	#3 (parent #0) [Avestan / Sanskrit] refs=POK:1167 | vi-vard : to grow out ☞Wi
21	  #4 (parent #3) [Persian] refs=BQT:1848; HRN:210; MON:3427 | govâlîdan «گوالیدن» : to grow | extra: گوالاندن ، گوال | NOTE: FFD:75 derives these words from Old Persian "wi-ward"
22	#5 (parent #0) [Old Persian] refs=FFD:75 | ward : to grow ; wi-ward : to grow out
23	#6 (parent #0) [Greek] refs=POK:1167; KLN:1097 | orthos : correct, right
24	  #7 (parent #6) [English] refs=None | ortho- : correct ; orthodox, orthogonal, orthodontics, orthopedics
25	
```


## [2026-09-05T20:29:20.779Z] TOOL CALL #3: Bash

```json
{
 "command": "cat /home/sfmqrb/git/rishe/data/extracted/batch/page-158.json",
 "description": "Read source JSON for page 158"
}
```


### [2026-09-05T20:29:20.817Z] TOOL RESULT

```
{
  "pdf_page": 158,
  "book_page": 128,
  "entries": [
    {
      "root": {
        "name": "Erěbu",
        "lang": "Akkadian",
        "refs": "AKD:64; KLN:550",
        "gloss": "to enter, to go down (sunset)"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Arabic",
          "refs": "AKD:640,854",
          "words": [
            {"translit": "ğ.r.b", "gloss": "to set (sun)", "script": null},
            {"translit": "mağreb", "gloss": "sunset, west", "script": null},
            {"translit": "Mağreb al aqsâ", "gloss": "\"west of the extreme\", Morocco", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "MON",
          "words": [
            {"translit": "ğarb", "gloss": "west", "script": "غرب"}
          ],
          "script_extra": "مغرب ، غروب",
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 1,
          "lang": "Italian",
          "refs": "AHD:854",
          "words": [
            {"translit": "Marocco", "gloss": "Morocco", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Arabic",
          "refs": null,
          "words": [
            {"translit": "Marâkeš", "gloss": null, "script": null}
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
            {"translit": "Marâkeš", "gloss": "Morocco", "script": "مراکش"}
          ],
          "note": "MON6:1946 derives this from a different Arabic root.",
          "quote": null
        },
        {
          "id": 6,
          "parent": 3,
          "lang": "English",
          "refs": "AHD:854; NAT:163",
          "words": [
            {"translit": "Morocco", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 0,
          "lang": "Hebrew",
          "refs": "AKD:64; KLN:550",
          "words": [
            {"translit": "`erebh", "gloss": "sunset, west", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 7,
          "lang": "Greek",
          "refs": "KLN:550; AHD:452",
          "words": [
            {"translit": "europa", "gloss": "land of sunset", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "Latin",
          "refs": "AHD:452",
          "words": [
            {"translit": "eurôpa", "gloss": "Europe", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 9,
          "lang": "French",
          "refs": null,
          "words": [
            {"translit": "Europe", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 10,
          "lang": "Persian",
          "refs": null,
          "words": [
            {"translit": null, "gloss": null, "script": "اروپا"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 9,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "Europe", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Ered, Erdh, Weredh, Werdh",
        "lang": "Indo-European",
        "refs": "POK:339,1167; KLN:1097",
        "gloss": "to grow, high"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:339,1167",
          "words": [
            {"translit": "eredva", "gloss": "high", "script": null},
            {"translit": "vared, vard, ward", "gloss": "up, high, growing", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "HRN:39,210; BQT:227,1848; FFD:35",
          "words": [
            {"translit": "vâlâ", "gloss": "great, high", "script": "والا"},
            {"translit": "bâlîdan", "gloss": "to grow, boast", "script": "بالیدن"}
          ],
          "script_extra": "بال ۲ ، بالش ۲",
          "note": "See root \"Bhel\" for derivation of Persian \"bâlesh 1: pillow\".",
          "quote": {"text": "تاکه بنشست خواجه دربالش ۱ - بالش ۱ آمد زناز در بالش ۲", "poet": "Sanâî"}
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Avestan / Sanskrit",
          "refs": "POK:1167",
          "words": [
            {"translit": "vi-vard", "gloss": "to grow out", "script": null, "see": ["Wi"]}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Persian",
          "refs": "BQT:1848; HRN:210; MON:3427",
          "words": [
            {"translit": "govâlîdan", "gloss": "to grow", "script": "گوالیدن"}
          ],
          "script_extra": "گوالاندن ، گوال",
          "note": "FFD:75 derives these words from Old Persian \"wi-ward\"",
          "quote": {"text": "بزرگان گنج و سیم و زرگوالند - تو از آزادگی مردم گوالی", "poet": "Tîyân"}
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Old Persian",
          "refs": "FFD:75",
          "words": [
            {"translit": "ward", "gloss": "to grow", "script": null},
            {"translit": "wi-ward", "gloss": "to grow out", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 0,
          "lang": "Greek",
          "refs": "POK:1167; KLN:1097",
          "words": [
            {"translit": "orthos", "gloss": "correct, right", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "ortho-", "gloss": "correct", "script": null},
            {"translit": "orthodox, orthogonal, orthodontics, orthopedics", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    }
  ]
}
```


## [2026-09-05T20:29:21.315Z] TOOL CALL #4: Bash

```json
{
 "command": "cat /home/sfmqrb/git/rishe/data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-05T20:29:21.356Z] TOOL RESULT

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


## [2026-09-05T20:29:58.115Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['AKD','KLN','AHD','NAT','MON','POK','HRN','BQT','FFD','WLD','BRT','KNT','PHD','IEC','SYN','SKT','LKT','FVQ','AFM','PLA','ARY','HUB','CHEUNG','NYB','WEB','FSD','PEI','TAD','ARB','DEV','PHN','SIN','IRN']:\n    v=d.get(k)\n    print('==',k, json.dumps(v,ensure_ascii=False)[:700])\n\""
}
```


## [2026-09-05T20:29:58.321Z] TOOL CALL #6: Bash

```json
{
 "command": "sed -n 1,80p tools/verify_check.py && ls data/verification/ | head -50"
}
```


### [2026-09-05T20:30:00.054Z] TOOL RESULT

```
== AKD {"title": "H. Zimmern, Akkadische Fremdwörter als Beweis für babylonischen Kultureinfluss, Leipzig 1917 (2nd ed.)", "edition_found": "1915 first edition (1917 is the 2nd, enlarged ed.; pagination may differ slightly)", "kind": "archive_djvu", "url": "https://archive.org/details/akkadischefremdw00zimmuoft", "identifier": "akkadischefremdw00zimmuoft", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AKD.txt", "page_offset": "leaf = printed + 8 (e.g. leaf 21 = p.13). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Organised by semantic field; Akkadia
== KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt", "page_offset": "KLN_1966: TWO pri
== AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only", "identifie
== NAT {"title": "C. Berlitz, Native Tongues, New York 1982", "edition_found": "2005 Castle Books reprint (open); 1982 original lending-only (nativetongues00berl)", "kind": "archive_djvu", "url": "https://archive.org/details/native-tongues-charles-berlitz-book-sales-ca-1997-3-printing-2005-castle-books-9", "identifier": "native-tongues-charles-berlitz-book-sales-ca-1997-3-printing-2005-castle-books-9", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NAT_2005.txt", "page_offset": "2005 reprint: leaf = printed + 15 (e.g. leaf 17 = p.2); reprint pagination may differ slightly from 1982. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf on
== MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol 
== POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index 
== HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or grep the 
== BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.c
== FFD {"title": "Mohsen Abolghasemi, Fe'l-ha-ye Farsi-ye Dari, Qoqnus, Tehran 1374/1995", "kind": "local_scan_ocr", "url": "https://asmaneketab.ir/product/کتاب-ماده-های-فعلهای-فارسی-دری-محسن-اب/ -> https://dl.eliteraturebook.com/app/public/attachments/6925d29630b83.PDF (free PDF site; grey)", "lookup_hint": "Searched archive.org (Persian/Latin titles, author), ketabnak, noorlib, general web (pdf/download): nothing; only a related paid e-book 'واژگان زبان فارسی دری' (fidibo). ketabnak.com/book/45024 is a different book (فهرست فعلهای فارسی).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_asmaneketab.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/ref
== WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.39015066210397 (browser only from this host)", "identifier": "in.gov.ignca.20339 (Band 3); also in.ernet.dli.2015
== BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \\f between 
== KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt", "page_offset": "leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archiv
== PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<ident
== IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Reconstruct
== SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<i
== SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<i
== LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Numbered entries: 'NNNN. word (language) meaning' - Lokotsch is usually cited by entry number, but Nourai cites pages.
== FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ.txt"], "page_offset": "printed page = leaf − 17 (0-based \\f blocks in FVQ_pages.txt; 
== AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM.txt"], "page_offset": "19
== PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt"], "page_offset": "301 leaves (pdftotext -layout, \\f-separated): printed page = leaf(1-based) − 15 (leaf 291 = p.276).", "loo
== ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY:<printed page> --image", "local_file": ["/home/sfmqrb/git/rishe/
== HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by parag
== CHEUNG null
== NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Nourai's 'NYB' nu
== WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w (restricted full copies: webstersnewtwent00webs_0 1977, webstersnewtwent01webs 1983)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/WEB_vol1.txt", "page_offset": "not reliably detected (page_numbers.json sparse); grep headword. local
== FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-Dive), in.ernet.dli.2015.272042 (vol II), in.ernet.dli.2015.83695 (vol III), in.ernet.dli.2015.147440 (vol IV Sabi-Z)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt", "page_offset": "vol1: leaf = p + 41..56 (drifts; e.g. leaf 87 = p.46, leaf 612 = p.556); vol3: le
== PEI {"title": "M. Pei, The Families of Words, New York 1962", "edition_found": "1962 (open copy)", "kind": "archive_djvu", "url": "https://archive.org/details/familiesofwords00inpeim", "identifier": "familiesofwords00inpeim (lending copies: familiesofwords00peim, bwb_FS0-ABP-200)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PEI.txt", "page_offset": "leaf = printed + 18 (e.g. leaf 21 = p.3). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Popular prose; grep the word.", "notes": "1 citation."}
== TAD {"title": "Tobia al-Unaysi (طوبيا العنيسي), Tafsir al-alfaz al-dakhila fi al-lugha al-'arabiyya ma'a dhikr asliha bi-hurufihi (2nd ed. Cairo 1932, ed. Yusuf Tuma al-Bustani; later Library of Lebanon reprint) — Nourai lists it under Arabic authors ('Unaysi T.'); its Table IV line was lost in the OCR", "kind": "archive_djvu", "url": "https://archive.org/details/TOB1932ARAR (1932 ed.); also https://archive.org/details/ar113lang79 and https://archive.org/details/elshandawily14640", "lookup_hint": "Alphabetical Arabic headwords; grep the Arabic headword in TAD_pages.txt (86 leaves) or TAD.txt; inside.php search works.", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/TAD_pag
== ARB {"title": "al-Jawaliqi, al-Mu'arrab min al-kalam al-a'jami, Tehran 1966 (reprint of Ahmad M. Shakir's Cairo 1361/1942 edition)", "kind": "archive_djvu", "url": "https://archive.org/details/mo3rb (probably the Shakir edition) ; https://archive.org/details/almo3rab_gwaliqy_f_abduraheem (F. 'Abd al-Rahim ed., Damascus 1990) ; also uc1.aa0003615705 / AAlexandrina-148752 (Sachau's Leipzig 1867 ed.) ; text on shamela.ws", "lookup_hint": "Alphabetical Arabic headwords; grep in ARB_mo3rb.txt / ARB_abdulraheem.txt (raw, no page breaks); edition of mo3rb not confirmed — check its title page image.", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/ARB_mo3rb.txt", "/home/sfmqrb/git
== DEV {"title": "L. M. Devic, Dictionnaire étymologique des mots français d'origine orientale, Paris 1876", "edition_found": "1876", "kind": "archive_djvu", "url": "https://archive.org/details/dictionnairety00devi", "identifier": "dictionnairety00devi (also dictionnairetym02devigoog, fr105comparative41)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/DEV.txt", "page_offset": "leaf = printed + 26 (pp. <80) to +30 (pp. >84), e.g. leaf 29 = p.3, leaf 118 = p.88. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "French headword in caps at line start.", "no
== PHN {"title": "A. P. Pihan, Dictionnaire étymologique des mots de la langue française dérivés de l'arabe, du persan ou du turc, Paris 1866", "edition_found": "1866", "kind": "archive_djvu", "url": "https://archive.org/details/dictionnairetym01pihagoog", "identifier": "dictionnairetym01pihagoog (others: bub_gb_QnsSAAAAIAAJ, dictionnairetym00pihagoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHN.txt", "page_offset": "leaf = printed + 31 (e.g. leaf 33 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "French headword in caps at line start;
== SIN {"title": "B. Laufer, Sino-Iranica, Chicago 1919 (Field Museum Anthr. Ser. XV.3, pp. 185-630)", "edition_found": "1919", "kind": "archive_djvu", "url": "https://archive.org/details/sinoiranicachine153lauf", "identifier": "sinoiranicachine153lauf (also sinoiranicachin00laufgoog, jstor-29782155)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SIN.txt", "page_offset": "leaf = printed - 172 (e.g. leaf 15 = p.187). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Running page numbers 185-630 (the volume's series pagination, which Nourai uses). Sectio
== IRN {"title": "Bahram Farahvashi, Iranvij, Tehran University Press 1368/1989", "kind": "local_scan_ocr", "url": "https://asmaneketab.ir/product/کتاب-ایرانویج-بهرام-فره-وشی/ -> https://dl.eliteraturebook.com/storage/img/ایرانویج.pdf (free PDF site; grey) ; Google Books kP8bAAAAIAAJ (1368 ed., no view)", "lookup_hint": "archive.org 'Iranvej' item is a radio programme, not the book; nothing on ketabnak/noorlib. | For pages in a scanned volume use: python3 tools/ref_page.py IRN:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/IRN/IRN_eliteraturebook.pdf", "/home/sfmqrb/git/rishe/data/verific
```


### [2026-09-05T20:30:00.094Z] TOOL RESULT

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
page-133.json
page-135.json
page-136.json
page-137.json
page-138.json
page-139.json
page-140.json
page-141.json
page-142.json
page-144.json
page-146.json
page-311.json
page-31.json
page-32.json
page-33.json
page-345.json
page-34.json
page-35.json
```


## [2026-09-05T20:30:18.673Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK grep eredh ===\"; grep -n \"eredh\" POK_full.txt | head -30\necho \"=== POK grep u̯erdh / uerdh ===\"; grep -n \"u̯er-dh\\|u̯erdh\\|u̯redh\\|u̯re-dh\" POK_full.txt | head -30"
}
```


### [2026-09-05T20:30:18.770Z] TOOL RESULT

```
=== POK grep eredh ===
=== POK grep u̯erdh / uerdh ===
```


## [2026-09-05T20:30:19.684Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN 1966 Europe ===\"; grep -n \"Europe\\b\" KLN_1966.txt | head -20\necho \"=== KLN ortho ===\"; grep -n \"^ortho-\\|orthodox\" KLN_1966.txt | head -20"
}
```


### [2026-09-05T20:30:19.792Z] TOOL RESULT

```
=== KLN 1966 Europe ===
94:Loan  translations  are  important  guideposts  on  the  road  on  which  civilization  and  culture  trav¬ eled  in  the  course  of  centuries  from  nation  to  nation.  Through  them  we  learn  e.g.  that  the chief  elements  of  the  science  of  grammar  developed  in  ancient  Greece  and  reached  Western Europe  through  the  medium  of  the  Romans.  (T  he  overwhelming  majority  of  grammatical  terms in  the  modern  languages  are  loan  translations  of,  or  derive  directly  from,  Latin  words h  which themselves  are  loan  translations  of  Greek  words.  Cp.  e.g.  the  words  subject,  verb,  adverb,  nomi¬ native,  accusative,  genitive,  dative  in  this  dictionary.)
2189:algology,  n.,  the  study  of  algae.  —  A  hybrid  coin¬ ed  fr.  L.  alga  and  Gk.  -Xoyla,  fr.  -Xoyo;,  ‘one who  speaks  (in  a  certain  manner) ;  one  who  deals (with  a  certain  topic)’.  See  alga  and  -logy. Derivatives:  algolog-ical,  adj.,  algolog-ist,  n. algor,  n.,  cold;  chill.  —  L.,  fr.  algere,  ‘to  be  cold’. See  algid  and  -or.  For  the  mode  of  formation cp.  terror,  ‘fright’,  fr.  terrere,  ‘to  frighten’,  albor, ‘white  color’,  fr.  albere,  ‘to  be  white’, algorism,  n.,  the  Arabic  system  of  numerals.  — ME.  algorisme,  fr.  OF.  algorisme  (F.  algorith- me),  fr.  ML.  algorismus ,  from  the  inexact  trans¬ literation  of  Arab.  al-Khowarizmi,  ‘the  man  of Khowarizm  (the  modern  Khiva),  surname  of Abu  Jafar  Mohammed  ibn  Musa,  great  mathe¬ matician  of  the  9th  cent.  His  famous  work  Al- jabr  w’al  muqdbalab  (‘Reunion  and  compar¬ ison’),  introduced  the  use  of  Arabic  numerals  in Europe,  which  denoted  a  turning  point  in  the history  of  mathematics.  Cp.  algebra, algous,  adj.,  pertaining  to  algae.  —  L.  algosus, fr.  alga,  ‘seaweed’.  See  Alga  and  -ous. alguazil,  n.,  peace  officer  in  Spain.  —  Sp.  alguacil, fr.  earlier  alguazil,  fr.  Arab,  al-wazfr,  fr.  al-, ‘the’,  and  waztr,  ‘vizier’.  See  vizier, algum,  n.  —  See  almug.
3357:arcto-,  before  a  vowel  arct-,  combining  form meaning  ‘bear’,  or  ‘the  north’.  —  Gk.  dpxro-, tipxT-,  fr.  SpxTO?,  ‘bear;  the  north’.  See  arctic. Arctogaea,  Arctogea,  n.,  a  zoogeographical realm,  comprising  North  America,  Europe,  Asia and  Africa.  —  ModL.,  compounded  of  arcto- and  Gk.  yr),  ‘earth’.  See  geo-  and  cp.  Neogaea, Notogaea.
3612:Ashkenaz,  n.,  the  eldest  son  of  Gomer  (Gen. 10:3);  also  name  of  a  people  mentioned  in  Jere¬ miah  (51:27);  in  the  Middle  Ages  applied  to Germany.  —  Heb.  Ashkenaz.  Cp.  Euxine. Ashkenazim,  n.  pi.,  the  Jews  of  Germany,  central and  northern  Europe.  —  Heb.  Ashkenazzxm, pi.  formed  fr.  Ashkenaz.  See  prec.  word, ashlar,  n.,  1)  a  squared  building  stone;  2)masonry of  squared  stones.  —  ME.  ascheler,  fr.  OF.  ais- selier,  fr.  L.  axillaris,  fr.  axis,  ‘board,  plank’,  a collateral  form  of  ass  is,  of  s.m.,  which  is  rel.  to asset, ‘pole,  stake,  post’.  Axis,  axle  ,  is  not  rel.  to axis  in  the  above  sense.  Cp.  as,  n.,  atelier.  For the  ending  see  suff.  -ar.
3618:Asia,  n.  —  L.  Asia,  fr.  Gk.  ’Asia,  ‘Asia’,  fr.  Ak¬ kad.  a$u,  ‘to  go  out;  to  rise’  (said  of  the  sun), which  is  rel.  to  Heb.  yatzd',  ‘went  out;  rose’ (said  of  the  sun),  Aram.  ye‘a,  ‘went  forth;  burst forth,  bloomed’,  Ethiop.  wadaa,  ‘went  out’, Arab,  wadu'a,  ‘was  or  became  beautiful,  neat or  clean’.  Accordingly  Asia  orig.  denoted  ‘the Region  of  the  Rising  Sun’,  in  contradistinction to  Europe ,  which  orig.  meant  ‘the  Region  of  the Setting  Sun’  (see  Europe ).  Cp.  hamotzi.  Cp.  also wudu.
4226:Derivative:  baboon-ery,  n. babouche,  n.,  a  heelless  Oriental  slipper.  —  F., fr.  Arab,  babiish,  fr.  Pers.  papush,  lit.  ‘foot- covering’,  fr.  pa,  ‘foot’,  and  the  verb  pushiden, ‘to  cover’.  Pers.  pa  is  rel.  to  Avestic pad-,  ‘foot’ ; see  foot.  The  change  of  p  to  b  proves  that  the word  came  into  Europe  through  the  medium  of the  Arabic,  which  having  no  p,  regularly  chan¬ ges  the  p  of  foreign  words  into  b. baby,  n.  - —  Dimin.  of  babe.
5171:Blighty,  n.,  England,  home  ( British  army  slang). —  Hind,  bilaiti,  a  word  used  in  India  to  de¬ note  England  or  Europe,  fr.  Arab,  wildyat, ‘kingdom,  province’,  a  derivative  of  wdliya,  ‘he reigned,  governed’.  See  vilayet  and  cp.  blatti, vali.
9353:union  in  Europe  and  near-by  parts  of  Asia, noted  as  horsemen.  —  Russ,  kozak,  kazak,  fr. Turk,  qazaq,  qazaq,  ‘nomad,  vagabond’, cosset,  n.,  a  lamb  reared  by  hand,  a  pet  lamb.  — Prob.  fr.  OE.  cot-sieta,  ‘cottage  dweller,  house dweller’,  fr.  cot,  ‘cot,  house’,  and  sita,  ‘dweller’, fr.  sittan,  ‘to  sit,  to  dwell’.  See  cot,  ‘cottage’,  and sit.  For  sense  development  cp.  G.  Hauslamm , ‘pet  lamb’,  fr.  Haus,  ‘house’,  and  Lamm,  ‘lamb’, and  It.  casiccio,  ‘pet  lamb’,  fr.  casa,  ‘house’. Derivative:  cosset,  tr.  v.,  to  treat  as  a  pet.
10170:Derivatives:  dabbl-er,  n.,  dabhl-ing,  adj.,  dabbl- ing-ly,  adv.,  dabbl-ing-ness,  n. dabchick,  n.,  i)  the  little  grebe  of  Europe;  2)  the pied-billed  grebe  of  America.  —  Fr.  earlier  dap- chick,  lit.  ‘dipping  chick’.  See  dap  and  chick and  cp.  didapper.
13523:Erebus,  n.,  a  place  of  nether  darkness  leading from  Earth  to  Hades  ( Greek  mythol.)  —  L.,  fr. Gk.  vEpe|3os,  fr.  Heb.  ‘ erebh ,  ‘sunset,  evening’. See  maarib  and  cp.  Europe.
13825:Eurafrica,  n.,  Europe  and  Africa  taken  together.
13826:—  A  blend  of  Europe  and  Africa.
13828:Eurasia,  n.,  Europe  and  Asia  taken  together.  —
13829:A  blend  of  Europe  and  Asia.
13835:Europa,  n.,  a  daughter  of  Agenor,  king  of  Phoe¬ nicia  (Greek  mvthol.)  —  L.,  fr.  Gk.  Eupoirrr . See  Europe.
13836:Europe,  n.  —  L.  Europa,  fr.  Gk.  Eupdjxr),  ‘Europa  ; Europe’,  which  is  prob.  of  Semitic  origin.  Cp. Akkad,  erebu ,  ‘to  enter,  go  in;  to  go  down,  set’ (said  of  the  sun),  ereb  shamshi,  ‘sunset’,  Heb. 'erebh,  ‘sunset,  evening’;  see  Heinrich  Lewy, Die  semitischen  Fremdwdrter  im  Griechischen, Berlin,  1895,  pp.  139-140.  Accordingly  Eupw— r, orig.  meant  ‘the  Region  of  the  Setting  Sun'.  Cp Hesychius,  who  renders  Eoptirr r,  with  the  words -/copx  t f,p  8'jaetop  (=  ‘the  Land  of  the  Setting Sun’).  Cp.  also  Gk.  ’'Epspop,  ‘place  of  nether darkness’,  which  derives  fr.  Heb.  'erebh.  See maarib  and  cp.  Erebus.  The  form  Eup  cutty;  (as  if the  name  meant  evp-com;,  ‘broad  face’)  is  due  - to  the  natural  tendency  of  the  Greeks  to  Grecize words  foreign  to  their  language.  For  the  sense development  of  Gk.  EupcoTrc;  from  a  Semitic word  meaning  ‘sunset,  evening’,  cp.  Asia.
13838:European,  adj.  and  n.  —  F.  europeen,  fr.  L.  Euro- paeus,  fr.  Gk.  Eupcomxiop,  ‘European’,  fr.  Eupci- 7rr),  ‘Europe’.  See  prec.  word  and  -an. Derivatives:  European-ism,  n.,  European-ize, tr.  v.,  European-iz-ation,  n.
13839:europium,  n.,  name  of  a  rare  metallic  element (chem.)  —  ModL.,  named  by  its  discoverer,  the French  chemist  Eugene  Demarpay  (1852-1903) in  1896  after  the  continent  Europe.  For  the  end¬ ing  of  europium  see  suflf.  -ium.
14397:farrago, n., a  medley. — L.  farrago, ‘mixed  fodder’, fr.  far,  gen.  farris,  ‘coarse  grain,  corn,  meal’. See  farina  and  cp.  prec.  word, farrier,  n.,  1)  one  who  shoes  horses ;  a  blacksmith ; 2)  ( archaic )  a  veterinary  surgeon.  —  ME.  fer- rour,  fr.  OF.  ferrier,  fr.  L.  ferrarius,  ‘black¬ smith’,  fr.  ferrum,  ‘iron’,  fr.  *fersom,  a  word of  Sem.  origin.  Cp.  Heb.-Phoen.  barzel,  Syr. parzlld,  Akkad,  parzillu,  ‘iron’.  According  to my  opinion,  the  loss  of  the  Sem.  ending  -el, resp.  -illu  is  prob.  due  to  its  having  been  mis¬ taken  for  the  Latin  dimin.  suff.  -elhts,  -Ulus  and consequently  dropped.  It  is  very  probable  that the  Etruscans  who  coming  from  Asia  Minor settled  in  Etruria,  served  as  mediators,  a  sup¬ position  rendered  probable  by  the  circumstance that  in  Europe,  iron  appears  for  the  first  time in  Etruria.  Cp.  ferro-.  Cp.  also  brass,  brazen. Derivatives:  farrier,  intr.  v.,  farrier-y,  n. farrow,  n.,  a  litter  of  pigs.  —  OE.  fearh,  ‘young pig’,  rel.  to  OHG.  farh,  farah,  ‘pig’,  farhili(n ), MHG.  verhelin,  G.  Ferkel,  ‘little  pig’,  and  cog¬ nate  with  L.  porcus,  ‘pig’.  See  pork  and  cp.  the second  element  in  aardvark.
15864:Gaul,  n.,  1)  name  of  an  ancient  country  of  W. Europe;  2)  one  of  the  natives  of  Gaul;  3)  (used facetiously)  a  Frenchman.  —  F.  Gaule,  ‘the country  of  Gaul’,  fr.  Gallia,  fr.  Callus,  ‘a  Gaul’. See  Gallic.
=== KLN ortho ===
10494:take,  accept,  receive,  receive  hospitably,  hold’, SoxeTv,  ‘to  seem  good,  to  seem,  think,  believe’, Soxeoeiv,  ‘to  watch  closely’,  86^a  (for  *S6x-<ra), ‘notion;  opinion;  honor,  glory’,  S6y|za,  ‘that which  one  thinks  true,  opinion,  doctrine,  decree’, 86xi[20?,  ‘tried ,  assayed,  genuine’,  86x0?,  a  wood¬ en  beam’  (lit.  ‘that  which  holds  the  roof’),  8e!;i6?, ‘on  the  right’,  SiSdoxetv,  ‘to  teach’,  Mir.  dech, the  best’.  Cp.  Adoxa,  choledoch,  condign,  Cymo- doce,  dainty,  Daksha,  decorate,  decorous,  deign, dexter,  diadoche,  Diadochi,  didactic,  dignify, dignity,  diksha,  Diplodocus,  disdain,  docent, Docetism,  docile,  docimasy,  docimology,  Doco- glossa,  doctor,  doctrine,  document,  dogma,  doxa- stic,  doxology,  heterodox,  orthodox,  pandect, paradox, synecdoche.
12181:doxastic,  adj.,  pertaining  to  opinion.  —  Gk. So^acmxoi;,  ‘forming  an  opinion,  conjecturing’, from  the  verbal  adj.  stem  of  8o!;at[etv,  ‘to  think, imagine,  to  form  an  opinion’,  fr.  So'a,  ‘notion; opinion;  honor,  glory’,  which  stands  for86x-0ot and  derives  fr.  Soxciv,  'to  seem  good,  to  seem, think,  believe’  (whence  also  Soypa,  ‘that  which one  thinks  true,  opinion,  doctrine,  decree’),  fr. I.-E.  base  *dek-,  *dok-,  ‘to  take,  receive,  accept; acceptable,  becoming,  good',  whence  also  L. decere,  ‘to  be  seemly  or  fitting’.  See  decent  and cp.  dogma,  the  first  element  in  doxology  and  the second  element  in  heterodox,  orthodox,  paradox, doxology,  n.,  a  hymn  of  praise.  —  Eccles.  L. doxologia,  fr.  Eccles.  Gk.  So^oXoyia,  ‘praise, laudation’,  which  is  compounded  of  Gk.  86i;ac, ‘glory’,  and  -Xoyta,  fr.  -Xoyot;,  ‘one  who  speaks (in  a  certain  manner);  one  who  deals  (with  a certain  topic)’.  See  prec.  word  and  -logy.  Cp. also  next  word.
12182:doxy,  n.,  opinion,  doctrine  ( colloq .)  —  Back formation  from  words  ending  in  -doxy  (as heterodoxy,  orthodoxy,  etc..)  See  prec.  word, doxy,  n.,  a  wench ;  a  mistress  (slang).  —  Of  un¬ known  origin.
17632:heresiologist,  n.,  a  student  of  heresies.  —  Formed from  next  word  with  suff.  -ist. heresiology,  n.,  the  study  of  heresies.  —  Com¬ pounded  of  heresy  and  Gk.  -Xcyia,  fr.  -X6yoi ;, ‘one  who  speaks  (in  a  certain  manner);  one  who deals  (with  a  certain  topic)’.  See  -logy, heresy,  n.,  unorthodox  belief  or  doctrine.  —  ME.
17696:heterodox,  adi.,  unorthodox.  —  Gk.  ExepoSo'ot;, ’holding  opinions  other  than  the  right’,  com¬ pounded  of  iixEpop,  'the  other’  (see  hetero-),  and 864a,  ‘opinion’,  fr.  Soxeiv,  ’to  think’.  See  decent and  dogma  and  cp.  doxastic  and  words  there referred  to.
26616:ortho-,  before  a  vowel  orth-,  combining  form meaning  ‘straight;  rectangular;  regular;  true, correct’.  —  Gk.  op-9-o-,  fr.  op-Ddc;,  ‘straight; right,  true,  exact;  genuine;  upright,  righteous’, for  *  Fop&Foq  (cp.  Dor.  (3op&6-);  cognate  with OI.  urdhvah,  ‘high’,  vdrdhate,  ‘causes  to  grow’, L.  arduus,  ‘high,  lofty,  steep’.  See  arduous  and cp.  vriddhi.
26622:orthodox,  adj.,  having  the  correct  opinion  (esp. in  religion).  —  Late  L.  orthodoxus,  fr.  Gk. opDoSo^o?,  ‘having  the  right  opinion’,  fr. op{36?,  ‘right’  (see  ortho-),  and  86i;a,  ‘opinion’, which  stands  for  S6x-aa  and  is  rel.  to  Soxetv,  ‘to seem  good,  to  seem,  think,  believe’.  See  doxas- tic  and  cp.  dogma,  doxology.  Cp.  also  the  second element  in  heterodox,  paradox, orthodoxy,  n.,  right  opinion  (esp.  in  religion).  — Late  L.  orthodoxia,  fr.  Gk.  6pffo8o!;Ea,  ‘right opinion’,  fr.  6p&<58oi;o?.  See  prec.  word  and  -y (representing  Gk.  -Ea).
37467:sunn,  n.,  name  of  an  Indian  plant,  India  hemp.  — Hind,  san,  fr.  OI.  sanah,  ‘a  kind  of  hemp",  which derives  from  the  same  source  as  Gk.  xdvv ajit?, OHG.  hanaf,  OE.  heenep,  ‘hemp’.  See  hemp. Sunna,  Sunnah,  n.,  orthodox  Mohammedan  law based  on  Mohammed's  actions  and  teachings. —  Arab.  siinnah,  ‘way,  custom,  course,  tradition  . Sunni,  n.,  an  orthodox  Mohammedan.  —  Lit. ‘adherent  of  the  Sunnah’  (i.e.  ‘traditionist’),  fr. Arab,  sunnt,  which  is  formed  fr.  sunna1'  with  -l, a  suff.  expressing  relationship.  See  Sunna. Sunnite,  n.,  Sunni.  —  Formed  fr.  Sunna  with subst.  suff.  -ite.
```


## [2026-09-05T20:30:27.339Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN maarib ===\"; grep -n \"maarib\" KLN_1966.txt | head -5\necho \"=== KLN Morocco/morocco ===\"; grep -n \"morocco\\|Morocco\\|Marrakesh\\|Marrakech\" KLN_1966.txt | head -10"
}
```


### [2026-09-05T20:30:27.404Z] TOOL RESULT

```
=== KLN maarib ===
13523:Erebus,  n.,  a  place  of  nether  darkness  leading from  Earth  to  Hades  ( Greek  mythol.)  —  L.,  fr. Gk.  vEpe|3os,  fr.  Heb.  ‘ erebh ,  ‘sunset,  evening’. See  maarib  and  cp.  Europe.
13836:Europe,  n.  —  L.  Europa,  fr.  Gk.  Eupdjxr),  ‘Europa  ; Europe’,  which  is  prob.  of  Semitic  origin.  Cp. Akkad,  erebu ,  ‘to  enter,  go  in;  to  go  down,  set’ (said  of  the  sun),  ereb  shamshi,  ‘sunset’,  Heb. 'erebh,  ‘sunset,  evening’;  see  Heinrich  Lewy, Die  semitischen  Fremdwdrter  im  Griechischen, Berlin,  1895,  pp.  139-140.  Accordingly  Eupw— r, orig.  meant  ‘the  Region  of  the  Setting  Sun'.  Cp Hesychius,  who  renders  Eoptirr r,  with  the  words -/copx  t f,p  8'jaetop  (=  ‘the  Land  of  the  Setting Sun’).  Cp.  also  Gk.  ’'Epspop,  ‘place  of  nether darkness’,  which  derives  fr.  Heb.  'erebh.  See maarib  and  cp.  Erebus.  The  form  Eup  cutty;  (as  if the  name  meant  evp-com;,  ‘broad  face’)  is  due  - to  the  natural  tendency  of  the  Greeks  to  Grecize words  foreign  to  their  language.  For  the  sense development  of  Gk.  EupcoTrc;  from  a  Semitic word  meaning  ‘sunset,  evening’,  cp.  Asia.
22427:ma’am,  n.  —  Contraction  of  madam, maarib,  n.,  the  daily  evening  prayer  (Jewish  lit¬ urgy ).  _  Heb.  ma'artbh,  lit.  ‘bringing  evening’, Hiph‘11  (=  causative)  partic.  of  the  verb  'ardbh, ‘it  became  evening’,  denominated  fr.  ‘erebh, ‘sunset,  evening’,  which  is  rel.  to  Arab,  gharaba , Ethiop.  ‘ardba,  ‘(the  sun)  has  set’,  Arab,  gharb, ‘place  of  sunset,  west’,  Akkad,  erebu,  ‘to  enter, go  in’,  ereb  shamshi ,  ‘sunset’.  The  name  maarib is  taken  from  the  text  of  the  first  benediction. Cp.  Maghrib.  Cp.  also  Erebus,  Europe.
22517:Maghrib,  n.,  Barbary.  —  Arab.  Maghrib,  ‘the West’,  fr.  gharaba,  ‘(the  sun)  has  set ,  whence gharb,  ‘place  of  the  sunset,  west’.  See  maarib. Maghribi,  n.,  a  nativeofBarbary.  —  Arab.  Magh¬ rib!  ‘an  inhabitant  of  the  West’,  formed  fr. Mdghrib  (see  prec.  word)  with  -f,  asuff.  express¬ ing  relationship  and  corresponding  to  Heb. suff.
=== KLN Morocco/morocco ===
14651:fr.  I.-E.  base  *peik-,  ‘evil-minded,  treacherous, hostile’.  See  foe  and  cp.  feud,  ‘enmity’, fez,  n.,  a  red  felt  cap  with  a  long  black  tassel.  — Fr.  Fez ,  a  town  in  Morocco, fiacre,  n.,  a  French  hackney  cab.  —  F.,  fr.  the Hotel  St.  Fiacre,  rue  St.  Antoine,  Paris,  where carriages  were  first  hired  (since  1640).  Fiacre  is the  French  form  of  the  name  of  the  Celtic  saint Fiachra.
16874:‘a  viscid  substance’,  and  -ferous. gum  mogador,  Morocco  gum.  —  So  called  from Mogador,  a  seaport  in  Morocco,  whence  it  is exported.
22973:marocain,  n.,  a  dress  material  made  of  silk.  — F.,  lit.  ‘of  Morocco’,  fr.  Maroc,  ‘Morocco’;  so called  because  this  material  was  orig.  manufac¬ tured  in  Morocco.  Cp.  morocco.
24370:Derivatives:  moor-age,  n.,  moor-ings,  n.  pi. Moor,  n.,  1)  a  native  of  Morocco ;  2)  one  of  the Moslem  invaders  of  Spain  or  their  descendants.
24423:Moro,  n.,  a  member  of  a  group  of  Moslems  in  the southern  Philippine  Islands.  —  Sp.,  ‘Moor’. See  Moor  and  cp.  Morisco. morocco,  n.,  a  kind  of  fine  flexible  leather.  — Named  fr.  Morocco,  a  city  of  NW.  Africa, where  this  kind  of  leather  was  originally  made, moron,  n.,  a  feeble-minded  person.  —  Gk.  jzcopov, neut.  of  (Jtcapoq,  ‘foolish’,  prob.  cogn.  with  OI. miird(i,  ‘idiotic’.  L.  morus,  ‘foolish’,  is  a  loan word  fr.  Gk.  ptcopoq.  Cp.  the  second  element  in oxymoron.
33550:Salix,  n.,  a  genus  of  trees  and  shrubs,  the  willow (bot.)  —  L.  salix,  ‘willow’.  See  sallow,  n. salleeman,  n.,  also  sallyman,  1)  a  Morocco  pirate; 2)  a  velella  ( zool .)  —  Lit.  Sallee  man,  i.e.  ‘a  man from  Sallee’,  a  town  in  Morocco,  formerly  the home  of  pirates.
38138:tangent  (geom.),  adj.,  touching:  meeting  at  a point  without  intersecting;  n.,  a  tangent  line.  — L.  tangens,  gen.  -ends,  pres.  part,  of  tangere,  ‘to touch’,  which  is  prob.  cogn.  with  Gk.  Te-Tay- <!>v,  ‘grasping’,  and  with  OE.  paccian,  ‘to  pat, flap’;  first  used  by  the  Danish  mathematician Thomas  Fincke  in  his  Ceomelria  Rotundi  (in 1583)  and  adopted  by  the  German  mathemati¬ cian  Bartholomaus  Pitiscus  (1561-1613)  in  1 595. Cp.  tact,  tactile.  Cp.  also  attain,  contact,  con¬ tagion,  contaminate,  contiguity,  contiguous,  con¬ tingent,  entire,  intact,  intangible,  integer,  integri¬ ty,  noli-me-tangere,  task,  tasse,  taste,  tax. Derivatives :  tangent-ial,  adj.,  tangent-ial-ly,  adv. Tangerine,  adj.,  pertaining  to  Tangier;  n.,  an  in¬ habitant  of  Tangier.  —  Formed  fr.  F.  Tanger, ‘Tangier’,  seaport  in  Morocco,  fr.  L.  Tinge  or Tingi.  For  the  ending  see  suff.  -ine. tangerine,  n.,  a  Tangerine  orange.  —  From  prec. word.
```


## [2026-09-05T20:30:28.487Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"--- POK files ---\"; ls -la POK*.txt\necho \"=== grep eredh variants ===\"; grep -n \"eredh\\|ered-\\|redh-\" POK_02.txt | head -20\necho \"=== grep arduus ===\"; grep -n \"arduus\" POK_full.txt | head -20"
}
```


### [2026-09-05T20:30:28.557Z] TOOL RESULT

```
--- POK files ---
-rw-rw-r-- 1 sfmqrb sfmqrb  981836 Sep  4 14:06 POK_01.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 1137861 Sep  4 14:06 POK_02.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 1170809 Sep  4 14:06 POK_03.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 3971883 Sep  4 14:06 POK_full.txt
=== grep eredh variants ===
3692:(Icered-:)  kerd-,  kerd-,  krd-,  kred-  ,Herz'. Arm.  sirt,  Instr.  srti-v  ,Herz'  [*kerdi-)]
4365:kred-  s.  oben  S.  579  f.  unter  kered-.
=== grep arduus ===
27634:Latin arduus^Wxqh, upright';
```


## [2026-09-05T20:30:35.270Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"###### POK_01 leaf 347 (p.339) ######\"; awk 'BEGIN{RS=\"\\f\"} NR==348' POK_01.txt | head -60"
}
```


## [2026-09-05T20:30:35.934Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"### POK_03 offset check: find 1167 ###\"; grep -n \"1167\" POK_03.txt | head -10"
}
```


### [2026-09-05T20:30:36.808Z] TOOL RESULT

```
###### POK_01 leaf 347 (p.339) ######
ibe',   auch   als    PN,    cjmr.    efiür  ,Bärenklau',   mhd.    eberboum    3 nhd.  Eber-esche]
aisl.  iarpi-  ,braun',  ahd.  er2:;/,fuscus'  (oft  in  FIN),  ags.  eorp  ,dunkelfarbig, schwärzlich';  davon  aisl.  iarpi  , Haselhuhn'  und  ndd.  erpel  ,Enterich'  (im Gegensatz  zum  helleren  Weibchen) ;  mit  Vollstufe  der  2.  Silbe  ahd.  repa-^ reba-huon,  schwed.  rapp-höna  ,Rebhuhn'  <  mnd.  raphön :
lett.   irbe   in    meza    irbe   , Haselhuhn',  lauka-ifbe  ,Feldhuhn'   (s.  darüber Mühlenbach-Endzelin,  Lett.-D.  Wb.  I  708  f. :   kaum  slav.  Lehnwort  wie  lit.    ^ ierbe  erube,  jerubl,  jerubl^  , Haselhuhn',  vgl.  klr.  jarubic) ;
slav.  mit  Nasalierung:  mbg.  jer^bh,  r.-ksl.  jafabh,  *jerabh,  skr.  järeb usw.  , Rebhuhn',  von  der  Farbe  benannt,  wie  klr.  ordbyna,  orobynd,  sloven. jerebikaj  cech.  jefdb  usw.  , Vogelbeere';  ohne  anlaut.  Vokal  russ.  rjaböj ,scheckig'  (vgl.  oben  rjabinövaja  noch,  abg.  r^bi,,  russ.  rjdbka  ,Rebhuhn', rjabina  ,Vogelbeerbaum',  rjdbcik  ,Haselhuhn',  usw.).
Ob  hierher  auch  spätanord.  raf  n.  ,Bernstein',  aisl.  refr  ,Fuchs'  als ,der  rote'?    Aber  wohl  hierher  aisl.  arfr  ,Ochs'  usw.  als   ,der  rotbraune'.
Vgl.  Specht  Dekl.  115 f.,  der  von  einer  Farbwurzel  er-  ausgeht;  s.  auch rei-,  reu-b-  , buntgestreift' ;  zum  b  :  bh  s.  Specht  261  f.
WP.  I  146,  Jokl  Symb.  gramm.  Rozwadowski  II  242  f.,  Trautmann  104  f.
ered-  ,(zer)  fließen,  Feuchtigkeit'.
Ai.  drdati,  rddti  , fließt  (in  Kompositis),  zerstiebt,  löst  sich  auf;  beun- ruhigt, arddyati  ,macht  fließen,  löst  auf,  bedrängt,  quält,  tötet',  ärdrd- , feucht,  naß',  fdü'  (in  Kompositis)  , Feuchtigkeit',  av.  arddvi-  f.  Name eines  mythischen  Flusses,  meist  als  weibliche  Gottheit  gedacht.
Ob  dazu  gr.  liQda  ,Schmutz',  ägöaXog  ,schmutzig'?
Vielleicht  hierher  der  häufige  kelto-ligur.  FIN  Rodanos  (frz.  Rhone  == nhd.  der  Rotten j  ital.  Rodano  usw.)  als  ,der  fließende'  (gräzis.  ^Hgidavog aus  iberisiert.  *Errodanos),  dazu  die  Rednitz  (Bayern)  aus  *Rodantia.
WP.  I  148,   Pokorny  Mel.  Boisacq  II  193  ff.
335
eregai.h)0',  erog^{h)o'  ,Erbse,  Hülsenfrucht^
Gr.  b'goßog  m.  (aus  ^eooßog  nach  dem  Gen.  usw.  doößov);  vgl.  aber ^V.  Schulze  Kl.  Sehr.
```


### [2026-09-05T20:30:36.861Z] TOOL RESULT

```
### POK_03 offset check: find 1167 ###
5839:1167 ii(e)räd-,   Uersd-  ursd-  ,Zweig,  Rute;  Wurzel^
```


## [2026-09-05T20:30:45.277Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '5800,5900p' POK_03.txt"
}
```


### [2026-09-05T20:30:45.327Z] TOOL RESULT

```
8.  uer- , gewahren,  achtgeben*;  tjord-s  , aufmerksam*,  ar orä  , Aufmerksamkeit*
Gr.  nur  foQ-,  mit  spiritus  asper-  6q-  :  hom.  irtl  oQOvrcci  ,Hie  beaufsichtifen* OQsr  tpvldaasL  Hes.,  uorös  in  iftlovQog  (f��r  STtiogog  nach  o^gog)  ,£gjoooc Aufseher',  cpqovqog  ,Wächter*  {^Ttqo-bqoq),  (fQOvqä  , Schutz',  o^Qog  ,Wächter* (aus  Kompositis  abstrahiert),  dor.  zli^iäogog,  att.  rlf.ia}QÖg  ,Ehrenwäcbter Retter'  {föqog  =  germ.  wara-  s.  u.),  bqaci)  (iwowv,  eögGTia)  ,sehe*  (Denominativ eines  auch  in  cpQovqd  steckenden  *foQ&  =  ahd.  as.  wara,  ags.  waru ,  Aufmerk- samkeit') äol.  freilich  ^Qrjiiiy  ähnlich  wie  lat.  vereri]  dehnstufig  att.  Ö^a,  ion. ÜQTi  ,Hut,  Sorge'  hom.  o-bdsvög-wqogy  ovösvdg  öjgav  e^wv, nichtsnutzig',  dhycjQdtii _,vernachlässige'  von  ^öXLycoQÖg  ^dXlyrjv  öjgav  l'^w^  allenfalls  d^vQwgögj  nvX(aQ6^ ,Tür-,  Torhüter*  (eher  wegen  hom.  Ttvlscogög  an  -d-VQrj-,  TtvXrj-OQÖgj  ent- sprechend dem  Tl^cüQÖg)]  (hgeveiv  ,cavere';  ßwqoi  dq}d^aX(AoL  Hes.  Suid.
lat.  vereor,  -erl,  -itus  sum  , verehren,  fürchten';  zur  Form  vgl.  gr.  äol. {J^)i)Qr]^L  ,sehe';
air.  cö{a)ir  ,passend,  richtig':  cymr.  cywair  ds.  (*Äom-WeHos);
germ.:  uorösingot.iüar(5),behutsam',aisl.vörrr, behutsam, vorsichtig, scheu*, ags.  wcer  , gewahr,  aufmerksam,  vorsichtig,  behutsam*,  as.  war  ,vorsichtig,  auf der  Hut*,  ahd.  giwar  , aufmerksam,  vorsichtig*  ==  (J^ögog)]  üorä  in  got.  warai »Behutsamkeit,  List',  mhd.  wer  (ahd.  *wari)  , Vorsicht';  ags.  waru^  as.  ahd. wara  , Aufmerksamkeit,  Obhut*,  wara  neman  ^wahrnehmend ,  aisl.  vara  f. , Handelsware,  Zahlungsmittel',  ags.  loaru,  spätmhd.  war^  nhd.  Ware)  ahd. hewarön  fiewahren',  as.  warön  »beobachten,  wahren,  behüten*,  ags.  loarian ,bewahren,  hüten*,  aisl.  vara  ,aufmerksam  machen,  wahren,  vermuten*,  refl. jSich  hüten';  *uortos  (*uordhos)  in  got.  daurawards  , Torwart',  ahd.  wari , Wächter,  Wärter,  Hüter',  warto,  got.  wardja  ds.,  as.  wardön  ,auf  der  Hut sein,  behüten',  ahd.  warten  , achten,  spähen,  wahrnehmen,  warten,  erwarten*, warta  , Beobachtung  usw.',  nhd.  Warte  u.  dgl.;  "^iiorn-  in  ahd.  furiwama ,Vorbereitung'  (ags.  wearn  f.  »Widerstand,  Verweigerung,  Vorwurf,  nhd, warnen  usw.  durch  Einmischung  von  Angehörigen  von  *warjan  wehren  us^.*, und  Wz.  *wer-  »verschließen') ;
lett.  veru,  vert  ,schauen,  bemerken'  (meist  reflexiv  verties),  rM^a »Aufmerksamkeit' ;
toch.  A  war-,  B  wär-sk-  »riechen*.
WP.  I  284  f.
1165
9.  uer-  :  Ugru-s  Adj.  ,weit,  breit',      eros-  n.  ,Breite'.
Ai.  urü-,  av.  vouru-  (aus  H'aru-,  [dg.  *Ueru-),  jav.  auch  uru-  ,weitS westoss.  uruxj  Kompositionsform  av.  uru-  (aus  *wrzt-^  wie  ai.  gru-  neben ^itn^-,  oben  S.  476);  Komparativ  vdrlyas-,  Superlativ  vdn§tha-,  dazu  ai. urüci  f.  ,die  Erde*,  Femin.  zu  uru-vydnc:  urüc-  ,weitreichend'  vo-l.  den  av. Bergnamen  Vourusa-,  vielleicht  =  ai.  *urücya- ;  ai.  urvata-  m.  ,Jahr'  *uru.- ata-  ,weit  umherschweifend';  PN  Urvdsl  f.  aus  *uru-väii-  »starkes  Ver- langen';   dazu   ulükhala-   ^Mörser*   aus    *urü-khara-   ,mit  breitem  Boden'-
mit  Metathese  gr.  si-  (wie  in  c^/cjxw,  4.  uer--  vgl.  £%ö-/-  unter  5.  uer-) in  fit'^^g  (statt  Vs^vg) , breit',  sowie  in  sigogn. , Breite' (s.  darüber  Seh wyzer  Gr. Gr.  1,  412  Anm.  1);  vielleicht  toch.  A  ivärts^  B  aurtse  ,weit,  breit'.
Neutrum:   ueros-  in  ai.  vdras-  n.  ,Breite,  Raum'  (gv.  sdgog  statt  ^fsgog);
unsicher  Uetos-  , Brust'  in  ai.  uras-  (aus  *vuras),  av.  varö  ds.  und  ai. vdriman-  m.  n.  ,Weite,  Umfang',  vdrivas-  n.  ,Raum,  Weite,  Behaglichkeit', die  eine  schwere  Basis  voraussetzen.
WP.  I  285,  Mayrhofer  109  f.,  Thieme  Lg.  31,  439.
10.  wer-  ,Fluß,  fließen',  s.  oben  auer-  S.80f.;dazu  F«r- in  vielen  FIN  (%er-).
11.  uer-,  uer9-   ,Freundlichkeit  (erweisen)';  ueros  , vertrauenswert,  wahr'.
A.  Wurzelnomen  uer-:  gr.  J-rjg-  in  hom.  (ircl)  '^ga  cpegsiv  ,einen  Gefallen tun',  Pherek.  ^ga  üa-d-L,  Bacchyl.  rjga  mit  Gen.  „xocgiv" ;  srcii^gavog  ,wohl- gefällig,  angenehm';  Nom.  PI.  igL-7]g6g  »Vertraute',  Sg.  o-Stamm  igirjgog ,traut,  lieb';  ßgir]gov'  fxsydlcjg  v.e%agLa^ivov  Hes.;  PN  Hegirigrig^  Jicjgrjg aus  /JLO-J^rjgrjg.
B.  Ableitung  uerä:  germ.  *wera  , Vertrag,  Gelübde,  Bündnis'  im  aisl. GN  Vär  jGöttin  der  Treuschwüre',  PL  värar  ,Treuegelübde',  ags.  wxr  f. ,Vertrag,  Treue,  Schutz',  ahd.  icära  ds.,  mnd.  iväre  , Vertrag,  Friede';  aksl. vära  f.  , Glaube'.
C.  Komposita  auf -uero-s, -ueri-s,  formal  wie  gr.  igirjgog,  ßgirigog:  lat. se-verus  ,ohne  Freundlichkeit',  d.  i.  , streng',  davon  asseveräre  »versichern', perseveräre  ,beharren';  Gegenstück  gall.  PN  Co-vlrus,  cymr.  cywir  ,recht, treu';  *ueri-s  in  got.  alla-toerei  »schlichte  Güte',  aisl.  glväerr  ,freundlich, gastlich',  ags.  eal-ioerlic  ,benigne',  ahd.  alauuari,  mhd.  alwssre  ,schlicht, einfältig,  albern^,  ahd.  zur-ioäri  ,verdächtig'  =  got.  Huzwers  (tuzwerjan , zweifeln'),  *unioers  (un-ioerjan  ,unwillig  sein'),  ahd.  miti-wäri  , sanft'.
1166  ^
D.  Adjektiv  uero-s  ,wahr^:  lat.  verus,  air. /«-,  cymr.  gwiv  as.  ahd  mv» nhd.  wahr.  '
E.  VerbalableituDgen :  gr.  fio^r?}  (^fsJ^oquä)  ,Feier,  Fest*,  äol.  bootiq  d {*J^£QorLg?  eher  angeglichen  an  igozög,  hom.  igazog  ,lieblich');   l'^ctvoc  da*
ahd.  weren,  ghoerBn,  giwerön,  nhd.  gewähren,  as.  waron  gleisten'.  **
Hierher  wahrscheinlich  auch  germ.  werditz  (=  idg.  ^uertüA  in  aisl.  t?€rÄ
(Dat.  Sg.  virpe   neben    häufigerem   ve7-jbe)    ,Mahlzeit',   got.  wairdus    f^yoc*
as.  werd,  ahd.  TFiVi  , Hausherr,  Eheherr,  Wirt',  afries.  hus-werda  ,Hauswirh
Hausherr'.  _
WP.  I  285  f.,  WH.  II  528,  768,  Wissmann  Nom.  postverb.  115  ff..   Die
ältesten  Postverb.  des   Germ.  45,   Frisk  531,  547  f.,  565,  Trautmann  351
Vasmer  1,  184.
13.  uer-  , brennen,  verbrennen,  schwärzend
Arm.  varem  , zünde  an^,  varim  , brenne';  vielleicht  alb.  vorhe  ,Kochtop(* und  (?)  germ.  ^uarma-  ,warm'  in  got.  warmjan  ,wärmenS  aisl.  varmr  afr. as.  ahd.  warm  ,warm',  ablautend  ahd.  lolrma  ,Wärme'  (^wirmia)  und  wirmina mhd.  wirme  und  wirmen-^  vgl.  (?)  aisl.  orna  ,warm  werden,  wärmen'» aksl.  var^  ,Hitze',  variti  ,kochen'  (anders  oben  S.  81);  dazu  auch  balto* slav.  uarna-  m.  ,Rabe'  in  lit.  vafnas,  apr.  Vok.  warnis,  Akk.  PI.  t/xzmtnt aksl.  vram,  russ.  vöron,  wohl  ein  substantiviertes  Adjektiv  *uama' , schwarz,  verbrannt'  in  aksl.  vram,  russ.  voronöj  , schwarz*  usw.;  mit Dehnstufe  (Vriddhi)  femin.  bsl.  *uärnä-  ,Krähe*  in  apr.  loarne  (sekundärer e-Stamm),  lit.  vdrna,  russ.  ksl.  vrana,  serb.  vräna,  russ.  voröna  (Stoßton durch  Vriddhi);  hitt.  uar-  , brennen,  verbrennen',  Partiz.  uarant-  »brennend* (Intrans.),  uar-nu-  , anzünden,  verbrennend
WP.  I  269,  Trautmann  343,  361,  Vasmer  1,  169,  228  f.,  Szemer^nyi Kratylos  2,  121  f.,  der  auch  germ.  *swarta- , schwarz^  (anders  oben  S.  1062) dazustellt.
13.  uer-  in  den  sicher  Zugehörigen  mit  Redupi.  uer-uer-j  ue-utr-j  uai-^iVf ui-uer-  nä-uer  , Eichhorn,  auch  Iltis,  Marder  u.  dgl.^
Npers.  varvarah  , Eichhorn';  lat.  vlverra  f.  , Frettchen'  (*vi-uei'-sa)]  cymr, gwiweVj  bret.  gwiher  aus  dem  Lat.;  unklar  nir.  iora  rüadh^  schott.-gäl.  feorag]
baltoslav.  "^ueuer-  und  *uäuer-  *uaiuer-  f.  , Eichhörnchen*  in  lit.  vatver^ {yaivaraSj  vaivarys)  , Männchen  vom  Iltis  oder  Marder',  vaiverl,  vovtrl , Eichhorn^;  lett.  vävere,  väveris  ds.;  apr.  weware  ds.;  aruss.  vivertea, nslov.  v^verica  , Eichhorn',  klr.  vyvirka,  öech.  veverka,  bulg.  verrerica  df.;
unredupliziert  im  2.  Gliede  von  ags.  äc-weorna,  aschwed.  ekorne,  ahd. eihhurno,  eihhorn  usw.  ,Eichhorn'  (s.  u.  *a{g-  ,sich  heftig  bewegen*).
WP.  I  287  f.,  WH.  III  808,  Trautmann  356,  Vasmer  1,  176.
1167 ii(e)räd-,   Uersd-  ursd-  ,Zweig,  Rute;  Wurzel^
Gr.  ^dölS,  -ixog  .Zweig,  Rute^  (=  lat.  rädlx),  ^ada^vog  m.,  äol.  ^J^Qddafxvog (aus  ÖQ6dai.Lvog  zu  erschließen)  ,junger  Zweig-  (über  qcxdivöq,  ^adaUq  uer-, tired-  .drehen');  vgl.  gl^a  lesb.  ßgiada  ,WurzeP  (*J'q9Sicc?)',
alb.  rrdnze  ,Wurzel*  (Mann  Lg.  26,  388;  28,  37);^  kt.  rädlx,  -icis  f. ,Wurzer;  wahrscheinlich  rämus  ,Ast,  Zweigt  (als  *urädmos)  und  racZiW ,Stab,  Speiche,  Strahl  leuchtender  Körper,  Weberschiffchen'-
cymr.  givraidd  ,Wurzeln^  {*urddio-),  Singulativ  gwreiddyn,  acorn.  grneiten gl.  radix,  mbret.  gruizyenn,  nbret.  grisienn;  cymr.  ^lürys^  ,Äste,  Zweige* (*urd-sko-)',  air.  mir.  /ren  ,WurzeF  (*wrci-7zo-),  jünger /rem;  cym'r.  greddf , Instinkt,  Natur'  (*urd-mä-',  also  vielleicht  ursprüngl.  -wn-Suffix,  vgl.  oben gr.  Qccdafivog)]
got.  waürts  ,WurzelS  ags.  ivyrt,  ahd.  würz  ,Kraut,  Pflanze',  mhd.  auch ,Wurzel^  ahd.  wurzala,  ags.  wyrtwalu  (eig.  ,Kraut-stock')  , Wurzel'  (hierher auch  as.  wurtia,  mhd.  loilrze  ,Würze',  woneben  ablautendes  as.  icirtea,  mhd. vnrze  ds.;  neben  diesen  auf  ^u^rdd-  beruhenden  Formen  steht  *ur{9)d-  in aisl.  urt  ,Kraut*;  aisl.  röt  ,Wurzel';
toch.  B  vntsako  , Wurzel'.
WP.  I  288,  WH.  II  414,  415,  416,  Pokorny  ZcP.  26,  Iff.
uerdh-,  uredh-  , wachsen,  steigen;  hoch^
Ai.  vdrdhatij  vdrdhate,  vrdhdti  , wächst,  mehrt  sich',  vdrdha-  m.  ,das Fördern',  vardhdyati  , macht  wachsen*,  vrddhd-  ,erwachsen,  groß,  alt',  VT^d- dhi-  f.  , Stärkung';  av.  vardd-  , wachsen  machen*;  ai.  ürdhvd-  ,hoch'  (*Wor- dh-uo-)',  ai.  vrädhant-  , emporsteigend';
gr.  ÖQd-ög,  dor.  ßoQ&6-  ,auf recht,  gerade,  richtig,  wahr'  {*Uordh-uo-)j  dazu auch  OQ^Qog  ,der  frühe  Morgen',  bQ^giog^  ÖQ^gtrog  ,früh',  öq^qs^^ü)  ,bin  früh auf,  wofür  anlaut.  /  durch  lakon.  ßoQd-ayoqlay.og  Hes.,  sonst  ögS^ayogiaxog (aus  *dQ^Q-)  , Spanferkel'  (iftsl  nqdg  töv  b'Q-d-gov  7tLrtgdoy.ovTai)  gesichert wird;  ge^og  , Glied,  Leib,  Antlitz';
alb.  rit  ,wachse,  mache  groß';
vielleicht  got.  ^aw^ris^an  ,Frucht  bringen*,  aisl.  r^skr  ,tüchtig',  rgskvask , auf  wachsen,  reifen',  rqskinn  , er  wachsen*;
aksl.  usw.  rod^  ,partus,  generatio,  gens,  natura',  roditi,  raidati  ,parere', red^  , Speise,  Nahrung',  nslov.  rediti  ,nähren',  lett.  radit  ,erschaffen,  gebären' (wohl  Lw.),  raia  , Gedeihen,  reiche  Ernte*  {*radia),  rasma,  rasme  , Ge- deihen, Ergiebigkeit',  lit.  rasml  ds.;  unsicher  lit.  resnas  , stark,  tüchtig*, lett.  resns  ,dick,  dickleibig,  dickstämmig'  (russ.  Lw.  ?);  aksl.  ram  „^gd'gog", 6ech.  poln.  rano  ,die  Zeit  frühmorgens,  die  Frühe'  (vgl.  bulg.  ra^da  se ,(die  Sonne)  geht  auf,  (sol)  oritur')  aus  *urödhno-.
WP.  I  289  f.,  Trautmann  234,  Vasmer  2,  491,  527  f.,  Mayrhofer  1,  117.
1168
9
1.  uerg^-,  ureg^- , abschließen,  einschließen;  Hürde';  Erweiteruncr  von  5
Ai.  vrajd-  m.  ,Hürde,  UmhegungS  vrjana-  m.  .Umhegung,  Einfriedigt^* abgeschlossene   Niederlassung*,    gthav.    vdi-dzdna-,   jav.   vardzäna-    an dana-  n.   .Gemeinwesen^   (daraus   entlehnt   ai.  vardhana-    Stadt*    Wa  V nagel  KZ.  67,   168 f.);  av.  vardz-  , absperren*;    oss.  aeruaez  {*tcraza- ss^     ' vrajd-)  jRudel  Hirsche';
hom.  eoyw,  sqyä^ü)  {f-)  und  (mit  Vorschlags  £-)  UQyo),  att.  B^iqyo)  ,schlieCe ein,  aus,  halte  ab*,  att.  «l^xr?;,  ion.  Iq-attj  , Gefängnis',  att.  eigyiiög    GefänffTi* Verschluß',  kypr.  ka-te-vo-ro-ko-ne  ,sie  belagerten';  dazu  air.  fraig   Wand*' nir.  fraigh  ,Wand  aus  Flechtwerk,  Dach,  Hürde',  wegen  mcymr.  ach-vi^ ,wattled  fence'  aus  "^uregi-  (Loth  RC.  38,  301).
WP.  I  290,  Frisk  465 f.;  Benveniste  BSL.  52,  34;  vgl.  uergh-  oben  S.  11B4.
2.  uerg-j  ureg-  ,wirken,  tun';  uergom  n.  ,Werk'.
Av.  vardz-  {vdrdzyeiti  =  got.  lüaürkeip-^  s.  auch  gr.  ^iCu))  , wirken  tun machen',  Partiz.  varsta-,  var9za-  m.  , Wirken,  Verrichten  von,  Tätigkeit' (npers.  ra?'^,  barz  , Feldarbeit,  Ackerbau'),  varsti-  f.  , Handeln,  Tun',  varitva- Adj.  ,was  zu  tun  ist';  arm.  goi-c  ,Werk'  (mit  sekundärem  o);  gr.  foy(^ fiqyov  ,Werk,  Arbeit'  (=  dt.  Werk),  igyd^ofxaL  ,arbeite^,  danach  ^^chiyy , Arbeiter'  (für  *eQyÖTr]g),  egdio  (vereinzelt  egöcü)  ,tue,  opfere'  (V«^zdw,  *'^erSiö Hochstufe  nach  fiqyov  wie  in  as.  wirkian)^  Fut.  i'jofw,  Aor.  I'io^cr,  Perf.  ^o^a), qe^o)  ,tue'  (aus  qi^ai  neugebildet,  hom.  äqs'/.Tog  ,ungetan*  umgestellt  aal *&'[/] €^xros);  ÜQyavov  ,Werkzeug',  b'gyia  , (geheimer)  Gottesdienst',  d^icfcfw ,feiere  Mysterien',  öqysibv  ,Mitglied  einer  religiösen  Brüderschaft';  <3^cfjw, ion.  dqy&ü),  ögyiCco  , knete,  rühre  durch,  gerbe'  (wie  nhd.  Teig  wirkm^ mit  Bed.-Verengerung  in  der  Berufssprache),  wozu  iöqyr]  , Quirl'  (wohl redupl.  S^e-fögyo)]
alb.  rregj  , reinigen',  Mediopassiv  rregjem  , mühen,  streben'  (St.  E.  Maon Lg.  26,  382 f.);  abret.  guerg  ,efficax',  gall.  vergo-hretus  , oberste  Behörde der  Aeduer',  auch  verco-breto  (Pokorny,  Vox  Romanica  10,  266  f.) ;  mcjmr. gwreith  ,Tat*  (*ureg-tu-),  1.  PI.  Imper.  acymr.  guragun^  jünger  gionawn  u»w. {n  statt  r  durch  Einfluß  von  "^grn-  ,machen',  S.  373),  corn.  gruen,  mbr. gr(u)eomp  (*ureg-  , machen'),  Lewis-Pedersen  S.  336 f.;
as.  wirkian  (Neubildung  nach  werk),  warhta,  ahd.  (fränk.)  wirkan,  wirchtn, iüar(a)hta  , arbeiten,  tätig  sein,  wirken';  got.  waürkjan  (=  av.  V9r9zyeiti), aisl.  yrkja,  orta,  ags.  wyrcan,  worhte,  ahd.  (obdt.)  wurchen,  wor(a)hta  ,wirkeny tun,  machen,  bewirken',  ahd.  gaiourht  f.  ,Tat,  Handlung',  got.  frawaürhts , sündig',  f.  , Sünde'  usw.,  got.  waürsiw  n.  ,Werk'  {^waürh-stwa-]  ähnlich av.  varstva-);  ahd.  iverc,  iverah,  as.  iverk,  aisl.  werk  n.  (=  egyov)  ,Werk, Tätigkeit,  Arbeit',  ags.  weorc  auch  , Mühsal,  Qual',  weshalb  auch  aisl.  verkr, Gen.  verkjar  (m.  i-St.)  ,Schmerz,  Leid'  hierhergehören  kann;
1169
ahd.  wirken  , nähend,  stickend,  webend  verfertigen*  ==  as.  loirkian,  ags. icircan,  und  das  davon  nicht  trennbare  ahd.  loerih  in  der  Bed.  Wer<^ stuppa',  awirihhij  äwurihhi  ,Werg^  zeigen  Anwendung  unserer  Wz.  auf die  Weberei;  s.  dagegen  Marstrander  IF.  22,  332 f.  (der  Werg  und  wirken ,weben'  der  Wz.  *uerg-  ,drehen,  winden'  zuteilen  möchte);  an  nhd.  Werg erinnert  cjmr.  cy-warch  ,Hanf,  Flachs'  =  bret.  koarc'h,  abret.  coarcholion gl.  jcanabina*;  Marstrander  ZcP.  7,  362  sucht  darin  ein  idg.  *tier-k-  drehen' s.  oben  S.  1155.  .  »  ,
WP.  I  290f.,  Frisk  548  f.
3,  uerg-,  uorg-  ^strotzen,  schwellen  vor  Saft  und  Kraft  oder  Zorn*.
Ai.  urj-,  ürjä  f.,  ürjd-  m.  ,Saft  und  Kraft,  Nahrung'  (*Uorg-?),  ürjdyati ,nährt,  kräftigt',  ürjasvant-  , strotzend';
gr.  ÖQyrj  , seelischer,  heftiger  Trieb,  Affekt,  Zorn*  (ögyll^u)  ,erzürne  je- manden' u.  dgl.),  ögyao)  ,von  Feuchtigkeit  und  Saft  strotzen,  heftig  be- gehren, in  leidenschaftlicher  Stimmung  sein',  ÖQydg,  -ddog  (yfj)  ,üppiger  frucht- barer Erdboden,  Marschland,  Au*;
e-stufig  air.  ferc,  mir.  ferg  f.  ,Zorn*  vermutlich  auch  der  (hycsdvog  Oieg- yiovLog  bei  Ftol.  (d.  i.  vergivios  ,der  zornige'?  oder  noch  ,der  schwellende, wogende'?);  mcjmr.  y  werit  ,Meer*  (d.  h.  y  werydd)  eher  aus  "^Ugrio-  zu *auer-  oben  S.  80  und  1165;  vgl.  Federsen  Kelt.  Gr.  II,  669 f.
WP.  I  289,  Mayrhofer  1,  116.
uer-g-,  uer-gh-,  ner-k-  s.  oben  S.  1154  f.
uer-(e)nä  ,Erle,  Pappel'  (,Sumpfbaum'?),  danach  , Stange,  Balken'.
Arm.  geran  (*uer^na)  ,trabs,  tignum';
alb.  verre  f.  (*iternä)  ,Populus  alba';
bret.  gwern  f.  (*uernä)  , Schiffsmast;  Erle',  acorn.  guern  ,Mast',  guern-en ,Erle',  cymr.  givernen  ,Schiffsmast,  Erle',  PL  koll.  gwern,  Erlen,  Sumpf,  mir. fern  f.  ,Erle,  Mast',  gall.  Vernoduhrum  (,Erlenwasser';  aus  dem  Kelt. stammen  piemontes.   verna,  prov.  uerna,  verno,   frz.  verne,  vergne  ,Erle*).
WP.  I  292,  Meyer-Lübke  REW^  §  9232,  Vendryes  RC.  46,  137  und oben  S.  81.
uers-  ,am  Boden  schleifen'.
Lat.  verrö  (älter  vorrö),  verri,  versum  ,schleifen,  am  Boden  schleppen, fegen' ;
über  gr.  eqqu)  ,gehe  weg,  schwinde*  s.  Frisk  566;
aisl.  vgrr  ,Ruderschlag* ;  kaum  hierher  as.  ahd.  toerran  »verwirren, durcheinanderbringen*  usw.;
74
1170  #
lett.  värsms  ^Haufen  Getreide';  russ.-ksl.  vhvchu,  vrästi  , dreschen*   abl vracH  ,das  Dreschen^  (geschah  ursprüngl.  durch   Schleifen),  russ!  v6r    h jHaufen  (von  Getreide)';
hitt.  uarHia-j  uar§-  , abwischen,  pflücken,  ernten*.
WP.  i  267,  292  f.,  WH.  II  761  f.,  Trautmann  361,  Vasmer  1,  230.
Ueren-  ,Widder,  Schaf,  Lamm^
Ai.   *uran-  (aus  *vuran-),  Akk.  *uranam,  Nom.  urä,  woraus  urana-  rn ,Lamm,  Widder',  urä  f.  , Schaf*,  dazu  urahhra-  m.  ,Widder'  für  *ura'bha' (wie  vrsabha-  zu  vrsan-);  vgl.  npers.  barra  (*varnak)  ,Lamm''  pehl.  varak ,Widder*;   iran.   värdn-jar-y    vär9-yna-    , Lämmerschläger'  (Humbach  DLZ 78,  299 f.);
arm.  garn,  Gen.  garin  ,Lamm*;
gr.  hom. X'F)ccQi^y,  Gen.  agvög  ,Lamm*,  kret.  J^agrjv]  auch  in  tsakon.  vanna aus  lakon.  J^aqviov  ,Lamm',  dazu  -J^qtjv  in  hom.  noXvQQrjv  ,schafreich*  daraus spät  qrjv)j  mit  Ablaut.  äqvsLÖg  ,Widder',  falls  nicht  eher  aus  *äQ0vEi6q  (*aQijy^ rjfoq)  zu  Ixqariv  , männlich'  (oben  S.  336);
Ableitung  *urenön-  in  lat.  (als  germ.  Lw.)  reno  , Tierfell  als  Kleidung,  Pela**
unklar  als  Ableitung  lat.  vervex^  -ecis  (-Ix,  -Icis)  , Hammel*;  unklar  ut auch  das  Verhältnis  zu  den  auf  *enio(s)-, Wolle'  rückführbaren  gr.  Worten slqoq  n.  , Wollfließ',  abgeleitet  eYqlov,  att.  eqlov  , Wolle',  att.  e^eqog^  st%^^ ,schönwollig',  äol.  en-eqog  ,Widder'  (, worauf  Wolle  ist*),  ion.  elgtrsogf  att. iQlveog  ,von  Wolle';  anlautendes  /  lässt  sich  nicht  nachweisen.
WP.  I  269  f.,  WH.  II  429,  Specht  Idg.  Dekl.  33  f.,  Frisk  137  f.,  468  f.
1,  ues-  jverweilen,  wohnen,  übernachten*;  ues-ti-s  ,Aufenthalt'.
Ai.  vdsati  (Partiz.  sekundär  usita-)  ,verweilt,  wohnt,  übernachtet'  (mit  dx jSchläft  mit  einer  Frau*,  mit  wpa:  , fastet')  =  av.  vaidhaiti  , wohnt,  ver- weilt', ai.  Kaus.  väsayati  ,beherbergt';  vdstu-,  vasati-  m.  f.,  väsd-  m.  , Auf- enthalt, Übernachten*,  apers.  ä-vahanam  ,Wohnplatz,  Flecken',  ai.  dehn- stufig västu-  n.  , Stätte,  Haus',  jünger  vdstu-  n.  ^Ding,  Sache*  (yastuka-  m. ,eine  Pflanze',  eigentlich  ,Hof unkraut') ;  väsa-vesman  n.  , Schlafzimmer*;
arm.  goy  ,ist,  existiert,  ist  vorhanden*,  goy  (i-St.)  ,seiend.  Sein,  Gut,  Habe';
gr.  ^eaa  ep.  Aor.  (stets  mit  wxra  verbunden)  ,zubringen*,  dazu  Präs. «fVxw,  dsaxovro ;  vielleicht  iarla  f.  ,Herd,  Altar*,  übertragen  ,Haus,  Familie usw.',  mit  sekundärem  l  ion.  latlrjj  äol.  böot.  lokr.  dor.  ark.  laria  durch Assimil.  an  das  betonte  l  der  zweiten  Silbe,  das  Fehlen  des  /  vielleicht durch  Einfluß  von  Var^^t;  Ableitung  von  *ues-ti-  ,Bleiben,  Wohnung',  also ,zum  Heim  gehörig';  mit  unerklärtem  a- Vokalismus  {/)Ua%v  n.  ,Stadt* {äatog  , Städter,  äoTelog  ,städtisch*);
1171
messap.  vastei  (Dat.);
lat.   Vesta  , Göttin  des  häuslichen  Herdes^;
mir.  fö(a)id  .nächtigt  (auch  ,mit  einer  Frau*),  hleibt,  verweilt,  wacht  in der  Nacht^  {*uoseti\  3.  Sg.  Prät./m  {''ui-iLös-t),  3.  PL  ßotar  {*ui-iios-ont-r\ Verbalnomen  fess,  feiss  t  »Schlafen,  coitus,  Aufenthalt',  ablaut?  foss  m. , Bleiben,  Ruhe*,  i  foss  ,zu  Rause^  fossad  ,fest,  standhaft;  Wohnung,  Auf- enthalt'; cymr.  gwas  ,Heimstätte*,  mcymr.  gwest,  kyioest  ,Ruheplatz',  gicest, cywestach  , coitus',  givesti  , Wohnung*,  dirwest  (*di-ro-ues-t-")  und  darwest  (Ho- are-ues-t-)  ,Fasten*;
```


## [2026-09-05T20:30:54.413Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor n in 350 351 352 353; do echo \"##### leaf $n #####\"; awk -v N=$n 'BEGIN{RS=\"\\f\"} NR==N' POK_01.txt | grep -n \"^[0-9][0-9][0-9]$\\|^ *3[0-9][0-9]\" ; awk -v N=$n 'BEGIN{RS=\"\\f\"} NR==N' POK_01.txt | head -25; done"
}
```


### [2026-09-05T20:30:56.278Z] TOOL RESULT

```
##### leaf 350 #####
11:337
ebenfalls aus  *rös-)]
gr.  dTt-sQcca)  (*er9so)  ,gieße  eine  Flüssigkeit,  speie  weg'  (?),  i^-egdo)  ,schütte aus,  speie  aus',  %ar-eQda)  ,gieße  hinein',  ^sT-egdü)  ,gieße  um^,  Gwaoato  ,gieße zusammen';  nach  Dehrunner  IF.  48,  282  wäre  die  Grundbed.  von  ^Qdut ,auf  die  Erde  ausschütten'  und  das  Verh  von  eqa  ,Erde'  (oben  S.  332) abgeleitet ;
aksl.  rosa  ,Tau',  lit.  rasa  ds.
2.  Wurzelform  ers-,  rs-]  rsen  , männlich'.
ai.  drsati  ,fließt';  ferner  mit  der  Bed.  ,männlich'  (aus  ,benetzend,  Samen ergießend')  ai.  fsa-JÄa-Ä  , Stier',  aja-rsahhd-h  , Ziegenbock',  av.  apers.  arsan ,Mann,  Männchen',  gr.  hom.  ^qotjv,  att.  ^qqtjv,  ion.  äol.  kret.  eqotjV  (ohne J^- !)  , männlich'  (dazu  "^aQvrjJ^ög,  hom.  dgreiög  , Widder'  =  att.  äovecjg,  äol. dQvrjadsQ  f.,  dazu  dQvsvo)  , mache  einen  Luftsprung,  tauche',  eigentlich  ,mache einen  Bocksprung',  dcQvevTrjQ  ,wer  einen  Purzelbaum  schlägt,  einen  Luft- sprung macht',  Lit.  bei  Boisacq  u.  dqvsiög  und  dQve.vTTjQ  Nachtr.),  wohl auch  ahd.  or[re]huonj  anord.  oo^re  ,Auerhahn'  (daraus  durch  Kreuzung  mit ahd.  ür,  ürohso  das  mhd.  ürhan,  nhd.  Äuerhahn).
3.  Zugehörigkeit  unserer  Wz.  *eres-  zu  *er-,  '*or-  ,in  Bewegung  setzen, lebhafte  Bewegung'  ist  erwägenswert.  Andere  s-Formen  von  Wz.  er-,  or- zeigen weitere  Bedeutungen:
x\rm.  eram  (*ersä-iö ;  vgl.  oben  ai.  arsati)  , siede,  walle ;  bin  in  unruhiger Bewegung;  wimmle;  bin  leidenschaftlich  erregt;  bin  oder  werde  eifrig, zornig',  erandn  , Wallen  usw. ;  Erreg'ung',  z-efam  , bewege  mich  umher, bin  stark  bewegt,  erregt,  schwimme  usw.';
gr.  äq(x)ri  , Schwung,  Andrang'  {*rösä'j  davon  aber  auch  igcoeo)  ,fließe, ströme,  eile');
lat.  rörärii  ,leicht  bewaffnete  Plänklertruppe'  (Ableitung  von  *rösä , Schwung'  =  ßeXecjv,  dovQÖg  igcoi^)',
anord.  ras  f.  ,Lauf',  mndd.  ras  n.  ,heftige  Strömung',  ags.  rces  m.  ,Lauf, Anfall'  (engl,  race  skand.  Lw.),  mhd.  rasen  , rasen',  ags.  rcesan  ,anstürmen', anord.  rasa  ,einherstürzen';  anord.  ras  n.  ,Eile',  rasa  , stürzen,  gleiten' (Ablaut  *rös-  ;  *res-  :  *r9s-  ?) ;    got.  res  im  PN  Res-mer ;
337
dazu  mit  dem  Begriffe  teils  der  unruhigen,  auch  ziellosen  Beweguno- teils der  Aufgeregtheit,  des  gewalttätigen  Zornes:  *"
einerseits:  lat.  errö  (*ersä{ö)  ,irre'  (=  arm.  eram),  got.  airzeis  ,irre verführt^,  ahd.  irri  ,irreS  got.  airzipa  f.  ,Irrtum,  Betrugt,  ahd.  irrida  ds.'
irr(e)ön  (*erziön)  girren']
anderseits:  as.  irri  ,zornig',  ags.  eorre,  yrre  ^zornig,  erbittert^  eot^sian, iersian  , übelwollen',
4
##### leaf 351 #####
16:338  ,
.  e^'es-  in  ai.  irasydti  ,zürnt,  will  übel^  benimmt  sich  gewalttätig'  (*,res-), irasyä-  ,das  Übel\7ollen'  und  irsyati  ,\si  neidisch^  (V-^s-);  av.  Partiz. ai^syant-  .neidisch',  ai.  Irsyä-  ,Neid,  Eifersucht'  av.  aras-ka-  ,Neid',  mpers. npers.  arask  ,Neid,  Eifer',  tief  stufig  av.  drdsi-  ,Neid';  ved.  fsi-  m.  , Dichter Seher'  (*Rasender);
arm.  her  ,Zorn,  Neid,  Hader';
gr.  ^(Qog '  dKovGLOv  ßUßog  Hes.,  hom.  ägsLi}  ,Schmähwort'  (==  ai.  irasyä), dazu  ^TT^^fim, gewalttätige,  feindselige  Handlung'  (urgr.  ö,  vgl.  ark.  iTtrjQsiä^sv, mit  Dehnung  im  Kompositum  auf  Grund  eines  *in;-äQrjg),  vgl.  auch  igsa- XTjXeiü  ,treibe  Neckerei';  ^!^Qrjg  ,Gott  der  Rache'  scheint  Personifizierung des  verwandten  Subst.  dgi^  ,yerderben,  Gewalttat',  wovon  ägruisvog  ,be- troffen,  versehrt,  gequält';
lit.  arsiis  , heftig';
hitt.  arsaniya-  ,beneiden,  eifersüchtig  sein',  Denom.  von  *arsana-  ,eifer- süchtig'  (vgl.  oben  ai.  irsyä  ,Neid'),  Benveniste  BSL.  33,  139;
nach  Pedersen  REtlE.  3,  18  hierher  toch.  A  är§al  ,giftiges  Gewürm', B  arsäklai  , Schlange'  {^rsätla)-^
zu  ai.  drsati  ,fließt'  (oben  S.  336)  stellt  Couvreur  JJ  96  hitt.  a-ar-a§-zi {arszi)  ,fließt';
toch.  A  yär-s-,  B  yar-s-  ,baden'  (-s-  aus  -sk-),  ohne  sÄ:-Suffix  A  yär-  ds., wird  mit  hitt.  arra-  , waschen'  verglichen  (?).
WP.  I  149  ff.,   WH.  I  416  f.,  863,    Trautmann  237.
I.  ereu'  , nachsuchen,  forschen,  fragen'.
Gr.  *£Qev(xif  *£Qvi.isv,  thematisch  geworden  :  i^f  [J^]w,  igel/lofiat,  (äol.  igsvw) und  el'gofxaL  (gjo/o/fai)  , frage,  suche',  kret.  igevTal  fyTTjial,  Ttgav.Togeg^j .auf  Grund  eines  en-St.:  "^egef-wv  ,Frager,  Sucher',  igsvvdo)  ,spüre,  forsche nach'  und  hom.  igssivü)  , forsche,  frage'  {^sgsJ^ev-io)),  endlich  auf  Grund eines  *egJ^-ü)g:  igcordco  hom.  eigwTdiü  ,frage';  hom.  igslonsv  ist  nach  Risch (briefl.)  künstliche  Analogiebildung;
anord.  raun  f.  , Versuch,  Probe,  Untersuchung',  reyna  ,prüfen,  erfahren'.
WP.  II  356,  Schwyzer  Gr.  Gr.  I  680.
22
i
338  ,
2.  ereu'  , aufreißend
Ai.  drus'  n.  , Wunde';
anor d.  ervj  err  n.  ,Narbe'  {*arwaZj  "^arwiz),  als  finn.  Lw.  arpi,  Gen.  ar}^^ mnd.  arey  nhd.  dial.  arhe  ,Narbe';  ,'
s.  auch  unter  2.  reu-  ,aufreißen^,  das  wohl  dazugehört. WP.  II  352,  Holthausen  Altwestn.  Wb.  355.

##### leaf 352 #####
15:339
1.  ero-,  re-,  er(e)-  , rudern;  Ruder';  ero-ter-  , Ruderer'.
Ai.  ari-tra-  m.  , treibend;  Ruder',  n.  (auch  a?'i7ra-)  , Steuerruder',  aritdr ,Ruderer';
gr.    igs-TTjg    ^Ruderer',    Ersatz    für    *iQSTrjQ   (=  ai.    aritdr-)    wozu   fem 'EgevQicc  ON  erhalten,  egiaaci),  att.  iosTToj  , rudere'  (*€gsT-i(x),  Denominativ)  ,J.- iosTfiög,  PL   igsTf-id    (statt   *6Qfji.iog  =  lat.    remus,    nach    igsTrjg,    Schwyzer  '^ Gr.  Gr.  I  493 2)  , Ruder',   hom.  elgsalrj   (sl-  metr.  Dehnung)  ,das  Rudern'  >''"<' UTTTj^srjyg  , Ruderknecht,  Matrose';   übertragen:  , schwer  arbeitender  Diener' Tievrrjgrjg  ,Fünfdecker';    slyiöa-ogogf   Tgiay-öw-ogogy    ion.   Tgirj-aörT-egog   usw. (die  -o^og-Formen  durch  gr.  Assimihation  von  o  aus  £?);  äh-rjgrjg  ,das  Meer durchrudernd',  dixcp-T^grjg  ,doppelruderig',  Tgirjgrjg  ,Dreidecker';
lat.  remus  , Ruder',  triresmom,  septeresmom  Columna  rostrata  (Gruudf. eher  *re-smo-  als  *ret-smo-) '^
air.  o'ä-  , rudern',  imb-rä-  »rudern,  zu  Schiffe  fahren'  (z.  B.  Impf,  -raad, Perf.  imm-rerae  ,profectus  est',  Verbn.  imram  ,das  Rudern'),  räme  , Ruder';
anord.  röa,  ags.  röivan,  mhd.  rilejen  , rudern';  ahd.  ruodar^  ags.  rödor  n. ,Ruder',  anord.  röpr  (w-St.  *röpru-)  ,das  Rudern';
lit.  iriiXy  irti  , rudern',  irklas  , Ruder',  ablaut.  apr.  arttoes  f.  PL  ,Schiffsreise'.
WP.  I  143  f.,  Trautmann  105.
2.  era-,  re-  , ruhen*;  re-uä,  rö-uä  ,Ruhe'.
Av.  airime  adv.  , still,  ruhig'  {^et^-mo-),  armae-iad,  -Uä  , ruhig  sitzend,  !| still  stehend'  (*e?--mo-  oder  *e7'a-mo-;  bloß  graphisches  -i-  sieht  in  airime  % Meillet  Dial.  indoeur.  Q^) ;  ^^  '
gr.  ^gtori  (7tol€[.iOLo)  »(Kampfes) ruhe',  egwiw  , lasse  ab'  =  anord.  ?'ö,  ags. röw,  ahd.  ruoica^  nhd.  Ruhe  (*röwö),  ablautend  mit  ahd.  räwa  ds. ;  dgd-fisvai' j)avxd^€Lv  Hes.  (?) ;
cymr.  araf  , ruhig,  mild,  langsam'  {*er9-mo-) ;
nach  Rozwadowski  R.  Sl.  6,  58  f.  angeblich  hierher  der  Name  der  Wolga Pä  als  , ruhiges,  stehendes  Wasser'  aus  *Rava  (mordvin.  Ravo)  zu  lit. rova  (=  germ.  *röuö  ,Ruhe'),  lett.  räwa  , stehendes  Wasser',  lit.  FlN Rova  =  slav.  Ravu]  besser  oben  S.  336.
Anreihung  von  gr.  egcjg  , Liebe',  sga^ac  , liebe'  (vgl.  ai.  rdmate  ,ruht, steht  still,   läßt  sich   genügen,  findet  Gefallen,  pflegt  der  Liebe')  ist  eine
339
höchstens  ganz  schwache  Möglichkeit  (s.  Boisacq  m.  Lit.,  Persson  Beitr. 667).
Eine  s-Erw.  *r-e-s-,  r-o-s-  in  got.  rasta  ,Meile'  (,Rast'),  anord.  r^s^  f. ^Wegstrecke',  ahd.  rasta  L  ,Ruhe,  Rast,  Wegstrecke,  Zeitraum',  as.  rasta und  resta  (*rastja)  ,Ruhe,  Lager',  ags.  rcest  und  rest  ,Ruhe,  Ruhelager, Grab';  ablautend  m
##### leaf 353 #####
23:340  9
nd.  o-uste,  roste  ,Ruhe,  Wegstrecke',  spätmhd.  o-ust ,Ruhe';  got.  razn  n.  ,Haus',  anord.  rann  ds.^  ags.  cern,  ren  n.  ,Haus'  (mit merkwürdiger  Bed.  o^cßsn  n.  ,Planke,  Zimmerdecke'),  afries.  ern  in  ßä-ern ,Vieh-haus';  unsicher  ags.  reord  {^rezdo)  f.,  gereord  n.  , Mahlzeit,  Fest, Futter',  anord.  greddir  , Fütterer,  Sättiger'  {^garazdlz),  grenna  , füttern' {*ga-raznian).
Vgl.  rem-,  das  wie  res-  mit  (e)rd-  zusammengestellt  wird.
WP.  I  144  f.
er(9)d-  {,r{d)d-\  er{9)dh-  ,hoch;  wachsen'.
Av.  drddva-  ,hoch';
lat.  arduus  ,hüch,  steil' ;
gall.  Arduenna  silva,  air.  ard  (*fduo-)  ,hoch,  groß';  cjmr.  hardd  , schön';
aisl.  grdugr  , steil'  setzt  (wie  allenfalls  auch  drddva-)  eine  Parallelform auf  dh-  fort,  indem  verschiedene  Erweiterungen  von  er-  ,(in  Bewegung setzen)   hochbringen'  durch   dh   (vgl.  ÖQodvvcj  ,treibe  an'  usw.)  vorliegen.
Sicher  mit  dh  lat.  ai-hor  ^^-^n^'»  wozu  kurd.  är-  aus  *ard-  ,Baum'  in ärzang  ,die  durch  Wind  und  Wetter  verursachte  dunkle  Färbung  auf  den Bäumen*,  eig.  ,Baumrost' ;
alb.  rit  , wachse',  aus  fd-  oder  fdh-'^
slav.  *orstg,  abg.  rastg,  russ.  rastü,  cech.  rostu  usw.  , wachse*  (*ord-, ordh-to) ;
toch.  A  orto  , empor'.
WP.  I  148  f.,  II  289  f.,  WH.  I  64  f.
ergh'  , schütteln,  erregen,  beben'  od.  dgl.,  wohl  Erweiterung  von  er-  ,in Bewegung  setzen'.
Ai.  2'^Ä^y«^i  »bebt,  tost,  stürmt';
gr.  ÖQXEO)   ,7tall(x),  %Lve(x)\   meist  ÖQxaonai   ,tanze,   hüpfe,  springe,   bebe'.
Wegen  der  in  3.  er-  ebenfalls  vorliegenden  Bed.  ,1'^fg'  u.  dgl.  können  dazu in  Beziehung  stehen:
av.  drdyant-  ,arg,  abscheulich*;
ahd.  ar{a)g  ,feig,  träge,  böse,  arg',  ags.  earg  ds.,  aisl.  argr  und  mit Metathese  ragr  ,unmännlich,  wollüstig,  schlecht' ;
lit.  ariüs  ,lüstern,  sinnlich*.
WP.  I  147  f.
22*
340  9
erk"'  , strahlen;  hell  klingen,  lobpreisen'.
Ai.  drcati  , strahlt;  lobsingt,  begrüßt,  ehrt',  arkd-  m.  ,Strahl,  BlitzstraL)      1 Sonne,    Feuer;   Lied,   Sänger'   (=  arm.  erg),    rc-,    Nom.  Sg.  fÄ  f.  ,GlaiuI Gedicht;  Vers',  j-kvan-  ,lobpreisend,  jubelnd';  *
```


## [2026-09-05T20:31:16.171Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"##### HRN leaf 60 (p.39) #####\"; awk 'BEGIN{RS=\"\\f\"} NR==61' HRN.txt\necho \"##### HRN leaf 231 (p.210) #####\"; awk 'BEGIN{RS=\"\\f\"} NR==232' HRN.txt"
}
```


### [2026-09-05T20:31:17.990Z] TOOL RESULT

```
##### HRN leaf 60 (p.39) #####
- ^^9 —
aw. uhdaena- 'gewebt*; skr. vergl. ürna^vdbhi^
'Spinne* ^).
aty. üdal, ödal 'weben ; oss. vafpi (75) ; bei. gvapag,
n. ^vafay (134); wa;^. vufam, sar. väfam.
Arische (bezw. indogermanische) Doppelformen vaph-
und vahh-, vergl. Bartholomae, ZDMG. 44, 552,
Hübschmann, ib. 557.
' 169. bäy *6arten*.
Wohl aw. bäga- Xoos' (y. 51, 1); ai. hhägd- 'Teil,
Eigentum*; phlv. häg (PPGl.).
de Lagarde's Bemerkung bezüglich Nathans aus
Rom (Semitica I, 52) vermag ich nicht zu kontroliren.
170. häk 'Furcht*.
ar. '^bhäyaka-, von V^hhay' 'erschrecken, sich fürchten'
(aw. Jay-, ai. hhay-),
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
bäliä 'Wachstum*-'); vergl. guvöllden (No. 939).
*) Die indogermanische Wurzel vehh'^ veph', vtra'rtü. wthen^ zuerst
Aufrecht KZ. 4, 282, fehlt auch in der neuesten Auflage von Fick*8
indogermanischem Wörterbuch, erster Theil.
') FR citirt als Beleg einen wortspielreichen Vers Senäl's
(Metr. Xeflf):
tä kl hhisesf /^äjS der bcUis
hälei ämed zt näz^ der hälis
##### HRN leaf 231 (p.210) #####
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


## [2026-09-05T20:31:37.569Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD wāl ===\"; grep -n \"wāl\\|wālīdan\\|wālēn\\|wāly\" PHD.txt PHD_mackenzie.txt | head -30\necho \"=== PHD wardīdan / wardag ===\"; grep -n \"wardīdan\\|wardēn\" PHD.txt | head -10"
}
```


### [2026-09-05T20:31:37.640Z] TOOL RESULT

```
=== PHD wāl ===
PHD.txt:310:das [d’s | N ~] sickle. dàs?r [d’sl = Av. dātra-) gift, reward. dast [Y DE < A yd-h; dst! | = M, N ~] hand. dastag [dstk! | N —a] bunch, bundle, group. dast(a)gird [Y DE., dst-krt! | M dstygyrd, N dastgird] estate. dast- gir [dst OH DWN, (v. griftan) | N ~] 1. helper; 2. captive. dast-graw [dstglwb!] captivity. dast-kàrih [ҮЛЕ ГУА | N ~7] handiwork. dast-šūy [dstšwd] = ģūmēz. dastwar [dstwbl | М dstwr, N dastür] authority, priest, minister. ~th: custom; authority. dastyar [dstyd?l | (P dstd’r), N ~] helper. ~th: help, assistance. dašn [dšn! | = M] right hand. dāšn [d”$n' | M d’s(y)n] gift. dašnaģ [dsnk' | N ~a] 1. right hand; 2. dagger. dašt [dst! | = M, N —] plain, open ground. daštān [dft?n! | N ~] menstruation; menstruous. „estān [-st?n'] secluded place for menstruous women. -—--màh [-m?h] menstrual cycle. -ūmand [-’wmnd] menstruous. dāštan, dar- [YHSNN-tn! < А V ben: d^ftn', Pl- | M d'An, ar-, N ~] have, hold, keep, preserve. pad . . . dāštan: hold by, to; take for. pad éd dāštan [cf. N pindāštan] consider. --išn: preservation, maintenance. dāštār [4° #1 keeper, preserver. daw-, v. dawidan, dawistan. idawāl [dwb’l | N ~] leather, skin. ždawāl [dwbl | N ~] deceit, trickery. idawīdan, daw- [LH TWN-tn! < A Vrht; dwytn', dwb- | M dw-, N ~] run. *dawidan, daw- [dw-ytn'] speak (daevic). 1, 2 dawistan [LH TWN-stn!, dwstn'] = 1 * dawidan. daxmag [dhmk' | P dxmg, N ~a] tomb, dakhma (a building where corpses are exposed for destruction). „estān [-si?n!] cemetery. dax$ag [dhšk! | M dxsg] mark, sign, characteristic; memory. pad ~ dàštan : remember. az — hištan: forget. ~6mand [-’wmnd] marked. Day [ddw' | M dyy, N ~] Creator; cal. roth month; 8th, 15th, 23rd days. dayag [d^yk! | M d?yg-, N ~aj (wet-)nurse. „ānīh [nyh] | (N dāyagī)] nursing, nurture. dazidan, daz- [dc-ytn'] burn, scorch. --išn : burning.
PHD.txt:542:~ AZ: free (oneself) from. pargandan, pargan- [plkn-, plgn-dn! | (P pr'gnd, N parāgandan)] scatter, distribute, disperse. pargast [plgst' | N ~] let it not happen! Heaven forbid! pargüd [plgwt' | P prgwdg], ~ az: free, exempt from. parig [plyk' | M pryg, N pari] witch. paristag [pistk! | N pirista] servant. ~th: service; worship. paristar [plsť] | N parastár] maidservant. paristidan, parist- [plst-ytn' | M pryst-, N parastidan] serve, worship. ~išn: service, worship. paristog/k [plstwk' | P prstwg, N piristū(k)] swallow. рагпабап [pinyE?n! | M prng?n, N parniyān] polychrome damask. parr [pl | M pr, N ~] feather, wing. parrag [plk', pig | P prg, N ~a] wing. ~ig [-vk'] winged. parréxtan, parréz- [plyhin', plyc-] remain over, be superfluous. parrón [plwn' | M prwn] hence, away. parrwar [plwl | M prwr] winged. parsig [p’lsyk' | N pārsī] Persian. pars [5/f] spotted, speckled. parwāl [plwl | (P prwrz)] refreshment, nourishment. parwal- [plw���l- | (P prwrz'dn)) foster, nourish, -išn: nourishment. parwanag [phonk! | M prw’ng, N ~a] guide, leader. ^h : guidance, leadership. parwand [plwnd | N —] enclosure, comprehension. parwand-, v. parwastan. P parwānģāh [*plw?ng’s] throne. parwār [plyw?l | N ~] citadel; circumvallation; suburb, surroundings. parwardan, parwar- [plwl-tn' | M prwrdn, N ~) foster, nourish, cherish, educate. ~išn: nourishment, fostering, education. parwast [plwst'] enclosure. parwastan, parwand- [plwstn', plwnd-] surround, enclose, contain, comprise. parwāz [plw’c | N ~] flight. parzin [picyn' | M prcyn, J przyn, (N parčīn)] fence, hedge. pas [AHL < A?hr; BATL < Ab2tr; ps| = M, N ~] then, afterwards, behind. ~ az: after. ~ih: rear. pas [p’s | = M, N ~] guard, watch. ~ dāštan: keep watch, guard. pāsbān [p’sp’n' | M p’sb’n, N ~] guardian, watcher. ~ih: defence, protection.
PHD.txt:605:wad-baxt [wtP ht! | N badbaxt] unfortunate. wad-dil [wtdyl | M wddyl, N baddil] coward(ly). wadgarih [wtglyh] evil-doing. wād-ģirdaģ [w° tgltk' | (N gird-bād)] whirlwind. wad-góhr [wtgwhl | N bad-gauhar] ill-, low-born. wad-kamag [wtk’mk'] malevolent. ~ih: malevolence. wadrang [w’ ting | N bādrang] citron. cc Dë [-bwd | N -bóya] lemon balm. wad|-tóhm [wttwhm] = wad-góhr. ~-wazag [-w’ck! | (N gawāža)] abuse. --.Xém [-hym] ill-natured. waf- [wp- | Р wf-, (N bàf-)] weave. ~išn: weaving. wafr [wp! | M wpr, N barf] snow. ~énag [-ynk!] а sweetmeat. waydān [wy?n! = Av. waybana-] head (ahuric). wahāg [wP?k! | M тор, N baha] trading; value. — burdan: value, estimate. wahār [wh], (bj?l) | M wkr, № bahar] spring. ~ig [-уЁ! | N -z] spring, vernal. wahig [ZZLA < A Semi (?); whyk' | M whyg, N *bahi] kid; astr. Capricorn. wahist [ол | M whyst, N bihist] paradise. ~Ig [-yk! | N -1] (worthy) of paradise. Wahman [whwmn' | M whmn, N bahman] Good Mind, the first Amahra- spand, guardian of cattle; cal. 11th month; 2nd day. wāhmān [*w-n! = whmn' | MOw^hmn, J whmn, N bahman] so-and-so. Wahrām [wlhl?’n', whPm | M whr’m, N bahram] god of war, victory; astr. Mars; cal. zoth day. ātaxš 1~: a major sacred fire. wak [wk! | N bak] frog. wālan [zo n! | (IN barzan)] settlement, community walg [wlg] = warg. walidan, wāl- [w]-ytn! | N bdlidan] grow, increase, prosper. ~išn: growth. wümidan, wam- [w’m-yin'] vomit. wan [wn' | N bun] tree; stock, stem. ~ i $urgünig : pistachio tree. ~ 1 was-téhmag: the Tree of Many Seeds. wān-, ~išn, v. wanidan. wanafšag [zvnpšk! | N bunafša) violet. Wanand [wnnd] astr. Vega. wandaģ [wndk'] rope, cord. wang [KALA < А ql’; wng | = M, N bang] voice, cry. wānīdan, wan- [wn-ytn! | M w’n-yst] conquer, overcome, destroy.
PHD.txt:663:xwāb [hw’b | N ~] sleep. xwābar [hw’l | M xwbr] beneficent. ~ig [-yk!] beneficial. —ih: beneficence, benefit. xwad [BNPSE < A b-nps-h; hwt' | M xwd, N ~] self; indeed. САҢ: selfhood, essence. xwaday [лору | M xwd'y, N ~] lord. ~th: lordship, sovereignty. ~war [-w’/] lordly. xwad-dósag [hwtdwsk'] self-indulgent. 7h : self-indulgence. xwah [AH TE < A *hth | N ~] sister. 1, ?x wüh-, ~išn, v. xwastan, xwāstan. xwahar [AH TEL v. xwah ; hw'hl | (M xwr), N xwdhar] sister. xwahl [eo hl | (M xwhr), № ~] bent, crooked. xwā(h)rīh [hw (h)yh | M xw'ryy] happiness, bliss. xwālist [hw’lyst' | (M xw’ryst)] sweetest. xwamn [hwmn', hmn' | M xwmn] sleep, dream. ~-wizar [-wc'/] interpreter of dreams, oneirocritic. xwān [hw!n! | M xw’n, N ~] tray, table. xwandan, xwān- [KRY TWN-, KLY TWN-tn! < А У д | M xwnd, xw'n-, N xwāndan) call, summon. Xwanirah [hwnyls = Av. x"aniraüa-] the central, inhabited continent of the earth. !xwar [kwl | M xwr, N ~] sun; cal. 11th day. Zwar [kwl = Av. x"ara-] a degree of sin. xwar-, —išn, v. xwardan. lxwàr [kw] | M xwr, N ~] light, easy; mean, abject. ~ih: ease; v. also x wührih. *xwar [%w/ | M xwr] food. xwür-, —išn, v. xwārīdan. xwaran [%w/n! | M xwrn] banquet. xwarāsān [hwlsn! | M xwr'?n, N ~] sunrise, east. xwār-bār [how?1b?l | M xwr w Pr, N ~] food and drink. xwardan, xwar- [OS TEN-tn! < Ath, V fth; hwltn! | M xwrdn, xwr-, N ~] eat, consume. ~išn: food. ~ignig : edible. ~išnīh: eating, consumption. xwardār [hwit?I] (legally) edible, not murdār. xwardig [hwityk' | M xwrdyg, N ~i] food. xwārēn [hw’lyn'] edible. xwārēn- [hw’lyn-] cause to eat, drink; feed; irrigate. xwarģ [wig | J xwwrg] ember. xwārīdan, xwār- [heo?1-ytnt] drink. —išn: drink, drinking.
PHD.txt:1296:community hanjaman; wālan.
PHD.txt:1508:deceit dawāl, drē, fréb, pa(č)čībāgīh.
PHD.txt:2022:foster parwardan, parwāl-.
PHD.txt:2167:growth ārēyišn, rēyišn; (increase) abzāyišn, abzón, wālišn, waxšišn.
PHD.txt:2411:increase (vi)  abzüdan, wālidan, waxšīdan; (vt.) mehénidan.
PHD.txt:3602:settlement wālan.
PHD.txt:3685:skin Carm, dawāl, pēst; tēz; (a.) post- én; ~bag hambān, mašk; ~ 'table- cloth! maškīzag.
PHD.txt:3912:sweetest xwālist.
PHD.txt:4681:frawahr - PO o parwāngāh 595 ep o parwanagih ^5 e» Ф parwanag 13 ? o frawār, parwāl M o frawār-, parwāl- ANN CH parwālišn e» O frawārdan wed > оу franàm- - PO v franāmišn Irv’ > vo parwāz о» ro franāftan мү оу \ o Farrobag Yo (read pin-) Farróbag | 23 » a) piring E N a palang 3 М оз рагпарап w as» QJ palangmusk VU re N) Q) parwand E R Фу parwand- - 9 i a parron Ў оу frogih- -45?o frogihistan Us 4» оу frog Po parrwar N М P
PHD.txt:5269:A wālīdan, waridan we» ` wālan (DA 1
PHD.txt:5273:wālišn
=== PHD wardīdan / wardag ===
4096:turn (vi.) gardidan, waštan; (vt.) gardánidan, wardēnīdan; ~ ¿nto abaz waštan 6.
5166:awešant nirfs- nirfsišn l-2warz warz- warzāwand waržāg warzbūm warzīgar warzīdan warzišn warčašm warišn ward- wardānāg wardēn- wardénidan wardyiin F*wardagih wardag
```


## [2026-09-05T20:31:39.550Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT ərəδwa ===\"; grep -n \"arədva\\|ərəδwa\\|arəδwa\\|eredva\\|ardva\" BRT.txt | head -20\necho \"=== CHEUNG WARD ===\"; grep -n \"WARD\\|\\*uard\\|vard-\" CHEUNG.txt | head -30"
}
```


### [2026-09-05T20:31:39.619Z] TOOL RESULT

```
=== BRT ərəδwa ===
26822:paiti  irista  bazaiti  V.ij.g;  — spanaÄe'\ V.y.48  PüZ.;  —  Sing,  in  koUekL  SbnJ äal . .  ahe  tunanahe  . .  /rapi'iwS  (sd.)  spä  ! V.^.j;  —  taiHl  ya  bavainti  aos5.tarash .  .  yäha  anya  spa  V.  13.  42  (?).  a)  im Gegensalz  zu  Menschen  und  zu  andern Tieren :>'((/ii>4mi  spanasca  narasta  para.- irtiinti  V.5.  ij^.s,  u,  36,  8. 14;  —  yai ahmi  nmäne..spa  va  na  va  iri^yai  V.Ä  4; '>  5-  39;  —  y^  asiim  upanhanzaiii  sBnS va  para.irittahe  maryehe  vä  y.6.  10;  12, 7.23; —  *näirikayä  hhrpa  ..sunü  kihrpa N.jp;  —  pasvamca  slaoranqmca  masya- nqmca  saiiamla  vayqmca  V.  2.  8; — pasca . .  nasäum  ava.kar>i>nti  spstum  vä  raoz»m va  v>hrk3m  va  V,  5.  5;  6.50;  —  yahöit dim  . .  avaxanan  süns  (NP.)  va  hnß.- ifardvayB  va  V.ö.^s;  46,7.29,  30;  — j/J vä..vay5vä  hn/sji^aroFr'W.li.  A)  mit Bezeichnung  der  besonderen  Art:  spä pasusJtaurvS^''  .  .  spä  vU.kaurvS''''  .  .  spa vohuna^B^^ ..spa  taurunö'''^..spa  sukurmd*''> . .  spa  jaiui^^ . .  spa  aiwinu/'''' . .  spa  vltus''^ ..spa  urupis"'^'  V.  5,  29-33;  —  späntm slidnm  urvUarsm  yim  vat»hapar>m^^  V. 13.3;  —  ys  aSa^qm  sünam  Jainti  yim pa^us.kaurvqmca  viLhaurvqmca  vohuna- sgqtnea  draxtS.hunaranqmia^^  V.  13. 8,  42 ;
=== CHEUNG WARD ===
```


## [2026-09-05T20:31:52.765Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== CHEUNG head ===\"; head -c 600 CHEUNG.txt; echo; echo \"=== CHEUNG wardh ===\"; grep -n \"u̯ardH\\|\\*uardH\\|vardaiti\\|várdhati\" CHEUNG.txt | head -20\necho \"=== CHEUNG bālīdan ===\"; grep -n \"bālīdan\\|wālīdan\\|gu(w)āl\\|guwālīdan\" CHEUNG.txt | head -20"
}
```


### [2026-09-05T20:31:52.835Z] TOOL RESULT

```
=== CHEUNG head ===
Etymological 
Dictionary 


of the Iranian Verb 


Johnny Cheung 


Etymological Dictionary of the Iranian Verb 


Leiden Indo-European 
Etymological Dictionary Series 


Edited by 
Alexander Lubotsky 


VOLUME 2 


Etymological Dictionary 
of the 


Iranian Verb 


By 


ohnny Cheun 
y g 


LEIDEN : BOSTON 
2007 


This publication has been made possible by the financial support of the 
Netherlands Organization for Scientific Research (NWO), and Leiden Unwersity. 


This book is printed on acid-free paper. 


Library of Congress Cataloging-in-Publication Data 


A СІР. record for this book
=== CHEUNG wardh ===
=== CHEUNG bālīdan ===
```


## [2026-09-05T20:31:53.848Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== FFD grep بالیدن ===\"; grep -n \"بالید\\|بالیدن\" incoming/FFD/FFD_pages.txt | head -20\necho \"=== FFD grep گوالید ===\"; grep -n \"گوالید\\|گوال\" incoming/FFD/FFD_pages.txt | head -20"
}
```


### [2026-09-05T20:31:53.905Z] TOOL RESULT

```
=== FFD grep بالیدن ===
979:بالیدن
981:بالید + فارسی میانه ۷۷3170 ۷31704 مادهٌ ماضی جعلی است. از مادهٌ مضارع ساخته
2051:گوالیدن (:بالیدن)
2054:صورت بالاندةٌ ۷۵7۵ به معنی «بالیدن» است و خود («بالیدن» هم از ۷۵7۵ آمده است >
2055:بالیدن.
2629:5 (ريشه < بریدن) ۴۶ 4 (ريشه < بالیدن رشد کردن) ۰۳۵ ۷۵
=== FFD grep گوالید ===
2051:گوالیدن (:بالیدن)
2053:گوال < ایرانی باستان ۷3۲4-2-/۷*. برای ۵ -> آرای. ۷ پیشوند فعلی است. ۷۷374
```


## [2026-09-05T20:31:57.880Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== FFD lines 965-995 ===\"; sed -n '965,995p' incoming/FFD/FFD_pages.txt\necho \"=== FFD lines 2040,2060 ===\"; sed -n '2040,2062p' incoming/FFD/FFD_pages.txt\necho \"=== page tags near ===\"; grep -n \"pdf page\" incoming/FFD/FFD_pages.txt | awk -F: '$1>900 && $1<1000' | head; grep -n \"pdf page\" incoming/FFD/FFD_pages.txt | awk -F: '$1>2000 && $1<2100' | head"
}
```


### [2026-09-05T20:31:59.589Z] TOOL RESULT

```
=== FFD lines 965-995 ===
شده است.

بار ج فارسی میانه ۷۷27 + ایرانی باستان ۷۷3۶. ۷۷27 در ایرانی باستان اسم است و
«باران» معنی می‌دهد.
[pdf page 40]
ماده‌های ماضی و مضارع فارسی دری ۳۵
بافتن

بافت < ایرانی باستان ۹۷31-۵*. برای 12 -> آراست. ]۷3 صورت بالاندةٌ ريشةٌ ۷:۵۲
است. ريشةٌ ۷۷2۶ به معنی «بافتن» است.

باف + فارسی میانه و پهلوی اشکانی ۴3۲+ ایرانی باستان ۷3۶۵*. برای 8 ->
آرای.

بالیدن

بالید + فارسی میانه ۷۷3170 ۷31704 مادهٌ ماضی جعلی است. از مادهٌ مضارع ساخته
شده است.

بال < فارسی میانه ۷31 < ایرانی باستان ۹۷374-8*. برای 2 -» آرای. ۲۷374 صورت
بالاندةٌ ريشهٌ ۷۷27۵ است بهُ معنی «رشد کردن».

بایستن

بایست + فارسی میانه 2032191. 202181 مادهٌ ماضی جعلی است و از مادهٌ مضارع
ساخته شده است.

بای < فارسی میانه 203 < ایرانی باستان 8ر3م* < 2-ر02-4*. برای ۵ -> آرای.
4 پیشوند فعلی است. 2۷ به معنی «حرکت کردن» است. «آی» مادهٌ مضارع «آمدن» از
9 آمده است > آمدن.

=== FFD lines 2040,2060 ===

گمار + فارسی میانه ۰801037

گواردن

گوار + فارسی میانه 6۳837 < ایرانی باستان ۷1-127-۵*. برای 2-> آرای. 137 صورت
بالاندةٌ ريشهٌ ۴۵۲ به معنی «کردنْ» است. ۷۷1 پیشوند فُعلی است.

مادهٌ ماضی در فارسی میانه 8083770 بوده که جعلی است. «گوارد» فارسی دری
بازماندة ۹1-137-1۵* ایرانی باستان است. برای 1۵ -> آراست.

گوالیدن (:بالیدن)

گوال < ایرانی باستان ۷3۲4-2-/۷*. برای ۵ -> آرای. ۷ پیشوند فعلی است. ۷۷374
صورت بالاندةٌ ۷۵7۵ به معنی «بالیدن» است و خود («بالیدن» هم از ۷۵7۵ آمده است >
بالیدن.

لرزیدن
لرزید < فارسی میانه 1272۵» مادةٌ ماضی جعلی و از مادةٌ مضارع ساخته شده است.
لرز + فارسی میاته 1372 + ایرانی باستان ۲۵۲2-۵*. برای 2 آرای.
[pdf page 81]
وا فعلهای قارسی دری
دا 2 لشت.
=== page tags near ===
909:[pdf page 38]
935:[pdf page 39]
969:[pdf page 40]
2027:[pdf page 80]
2060:[pdf page 81]
2084:[pdf page 82]
```


## [2026-09-05T20:32:12.606Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BQT v1 search بالیدن ===\"; grep -n \"بالیدن\" BQT_v1_pages.txt | head -20\necho \"=== page tags ===\"; grep -n \"pdf page\" BQT_v1_pages.txt | head -3"
}
```


### [2026-09-05T20:32:12.671Z] TOOL RESULT

```
=== BQT v1 search بالیدن ===
17038:۵ - ره 0 بالیدن ۰
17092:بالیدن و نموکردن هم آمده است ۸
17109:۸ - اسم مصدر از بالیدن, سنابی‌غزنوی
17166:افزودن و بالیدن و نمو کردن و بز رکه شدن
17179:پالیك - بر ون ناهید . ماضی بالیدن
17181:بالیدن بروزن‌مالیدن ؛ بمعنی‌بز رکه
17217:۴ - اسم مفمول از بالیدن . ۴ - در بهلری۵2110 ۱ مت ) « منای۲۹۹ او
23513:شدن و بالیدن وافز ابش باشد؟ .
23579:بالیدن؟ بر وزن حالیدن ؛ بمسنی
24866:کردبده باشد - وبا کاف نازی کنابه از درمانده | یمنی دراز کردن - و نمو و بالیدن هم هست -
26340:بالیدن است که بمهنی جستجو کردن و تفحص
=== page tags ===
```


## [2026-09-05T20:32:14.760Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KNT ward ===\"; grep -n \"vard\\|ward\" KNT.txt | head -20\necho \"=== BRT try ===\"; grep -n \"ar»Öwa\\|arSwa\\|ərəδ\" BRT.txt | head -10; grep -cn \"\" BRT.txt"
}
```


### [2026-09-05T20:32:14.845Z] TOOL RESULT

```
=== KNT ward ===
345:88. New Iranian includes the Iranian lan- guages from about 900 лр. onward; its greatest monument is the national epic of Persia, the Shih Namah or Book of Kings, composed by Firdausi about the year 1000. The languages of this period are the following:
415:$14. EARLY STEPS IN THE DecipHERMENT. ОР inscriptions and writing are mentioned in a num- ber of ancient authors, from Herodotus onward, and are remarked upon and described by certain modern travelers early in the seventeenth century, who published parts of inscriptions from Per- sepolis in the accounts of their travels. The first inscription to be published in complete form was DPe, given by Chardin in 1711. Better copies of several were given in 1778 by Carsten Niebuhr, who recognized that the inscriptions were com- posed in three systems of writing, and that the writing ran from left to right: the direction of the writing was shown by two copies of XPe with somewhat differmg line-divisions. О. б. Tychsen in 1798 discovered that the three systems of writing represented three different languages, and that a recurrmg diagonal wedge in the simplest of the three types was a word-divider; but he wrongly assigned the inscriptions to the Parthian period. Friedrich Münter in 1802 inde- pendently identified the word-divider, and thought that a frequently recurring series of characters must be the word for ‘king’; he as- signed the mscriptions to the Achaemenian pe- riod
556:arlavd, ArtaxSaga, Artavardiya, by the Elamite
580:vardanam = opj-, GAV. vorozóna, LAV. varozüna-, Skt. opjdna-; see Lex. s.v.
584:By the Elam. writings: Атта (or Araza), Arbairé-, Armina, Asagaria, Paréava, Fravartis (also РЫ. fravartikdn), Margu&, Marduniya, -vard- in Ar- tavardiya, Vidafarna (also Av. хатто), Vidarna, Sparda, haumavargd: many of these confirmed also by Greek forms, ete.
1183:in adánd, vardana-; from plE gh in gaud-, Bar- diya; from pIE ĝ or gh in yaud-. For materials
1793:IV. Other formations, ineluding some personal names: agr-iya- to agra- (5148.1), батшап-їуа-, daran-ija-, brazman-iya-, mart-iya- to marta-, haš- iya- to hat- (8240), ha-mic-iya- to mitra-; Artavard- iya-, Ka"büj-iya-, Bard-iya-, M ardun-tya-.
1805:Expressing place: apa-dd-na-, daiva-di-na-, à- yada-na-, fem. us-tasa-nd-, d-vaha-na-, std-na-, varda-na-.
1897:Arta-vardiya- ‘Justice-worker’.
1941:b. Names of other Persians: Artavardiya-, Ardumants-, Aspacanah- (M), Ulana-, Өилта-, Dàtwahya-, Dédar&i-, Bagübigna-, BagaburSa-, Marduniya-, Vaumisa- (with -s- which is not Per- sian nor Median), Vayaspara-, Vahauka-, Vahyaz- dáta-, Vidafarnah- (M), Vidarna-, Vivina-, Hazà- manis-.
1966:‘city’, generic word not given in OP; vardanam
2162:2 The tendency in OP is to level toward changed forms of the stem-consonant, not back to the original sound; cf. Lex.s.vv. gddu- хтаби-, aradan-.
2676:A. Possessive, as in DB 2.19f тапа badaka ‘my - subject’; DB 4.82f anusiyà mand ‘my followers’, 3 whence also with its opposite m DB 2.79f haup. E | maty hamigiya abava ‘he became rebellious toward 3 me’ (also DB 3.11, 4.12, instead of hacéma ‘from “$ me’ and the like, DB 1.40, 2.6f, 3.27, 8.78, 3.810); «4 DB 1.4 mand pita, 1.29f Kabujiyahya brátà, and “$ with other words of relationship. This is found also 3 in the predicate: DB 3.9f pasiva dahyäuš manā 4 abava ‘afterwards the province became mine’, cf, 4 DB 5.19f, 35f, and DB 3.58f avam Катат hya ` Dérayavahaus х&ауабтуаћуа goubataiy ‘that army ‘$
2702:A. Expressing place where, without a preposi- tion, as in DB 1.34f pasdva drauga dahyauvā vasiy abava щй Parsaty ша Madaty ша aniyãwā dah- yusued ‘afterwards the Lie waxed great in the country, both in Persia and in Media and in the other provinces’; DB 2.75 duvarayãmaiy basta аййттуа ‘he was held bound at my palace en-
2704:trance’; DB 2.76 pasávasim Hagmatinary uzmayā- patiy akunavam ‘afterwards I put him on the stake (= impaled him) at Ecbatana’; DB 1.15 уату drayahyü ‘(those) who (dwell) by the sea’ (not ‘islanders’, since the term denotes the sa- trapy of which Dascylium was the capital, JNES 2.304). With ‘king’, singular nouns are in the loca- tive, as in DB 1.2 xSéyatiya Pérsary ‘king in Persia’, though plurals are in the genitive (§250.C); similarly DB 1.81 zšaçam tya Babtrauy ‘the kingship in Babylon’. It is a substitute for the genitive in DB 2.23f hya Madaisuvd тайа dha ‘who was chief among the Medes’ (cf. §250.D).
2716:Е. With or without prepositions, to denote place where or within which: DB 1.92 vardanam amu» Ufrātwã ‘a town beside the Euphrates’; DB 3.26 kära Parsa hya vapatüj ‘the Persian army which (was) in the palace’; XPa 13f vasiy aniyaSciy naibam kartam ana Parsé ‘much other good (construction) was built within this (city) Persepolis’.
2760:67. ApPosrTIVES occur in the following cases; lack of examples in the other cases is accidental: nom. DB 1.1, 1.53, and almost everywhere; ace. DB 1.54, DPd 2, DNb 4, etc.; gen. DB 3.59, DPd 9-11, XPe 14, etc.; loc. infrequent, DB 1.34f. More often the appositive, if more than а single word or if to an oblique ease, is expressed by an anacoluthie nominative phrase, followed by a resumptive pronoun or adverb ($314a; 8312). Partial appositives occur as in DB 1.34f pasdva drauga dahyawd vasiy аата щй Parsaiy ша Mädaiy utü aniyãwā dahyušuvā ‘afterward the Lie became great in the country, both in Persia and in Media and in other provinces’; also DB 1.401, 1.48f, DSf 25f ikä avaniya aniyā XL ara- Santis baránà ата X X атаќаті bar snd ‘the rubble
2811:§264. Tug DEMONSTRATIVE ava- ‘that’ is simi- larly either pronoun or adjective; it commonly refers to something already mentioned, but some- times has a forward reference, as in naimd ava ката tya tunuvd skaubars radiy miła kariyars ‘that is not my desire, that the mighty should have wrong done to him by the weak’ (DNb 10f; also DB 3.58, 5.21, DNa 39, DNb 20, 53, 55, 57, DSa 4, DSe 34, XPh 49, 51f). It has also the meaning ‘yonder’ as applied to the sky: Auramazdà hya imam bümim ada hya атат asmdénam айй ‘Ahura- mazda, who created this earth, who created yonder sky’ (DNa 1-3, eto.).
2820:IV. The antecedent of a relative pronoun is commonly repeated after the clause by a resump- tive pronoun in its immediate context, such as DB 1.21 avam (see above, I); DB 4.75f tya kuna- vähy ava-taiy Auramazdā ucãram kunautuy ‘what thou shalt do, that may Ahuramazda make suc- cessful for thee’.? In one passage the resumptive pronoun is repeated: DNb 16f martiya hya ha- taxsalaty anu-dim [ha]kartahyà avaéd-dim pariba- rámiy ‘the man who cooperates, him according to his cooperative service, him thus do I reward’.
3066:position, standing either at the beginning ог be- 4 tween the subject and the verb or at ће end: resp, = DB 1.8 hacà parwviyata, 1.45 hacà paruviyata, 1.82 5 Uvjam and abiy mam. The phrase тайпа Aura- — mazdüha ‘by the favor of Ahuramazda’ stands first in its clause in 63 of its 77 occurrences. Resump- tive pronouns (haw and forms of ava-) and ad- verbs (avadà, араба) stand first after a nominative phrase; pasdva ‘afterward’ leads off its clause in 77 of its 82 occurrences, standing last in DB 1.27, 4.5, 5.3, XSc 3, before yada ‘when’, while in DSe 48 the text is uncertain. Other adjuncts are vari- able in position; thus the goal may precede or follow the verb: DB 2.3 pasdva adam Babirum axtyavam ‘afterward I set forth to Babylon’, DB 2.30 avam adam früisayam. Arminam ‘him I sent forth to Armenia’.
=== BRT try ===
30725
```


## [2026-09-05T20:32:26.373Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nprint('total lines',len(lines),'ff count',t.count('\\f'))\n# find page of line 17179\nimport re\nfor ln in (17038,17092,17179,17181,17217):\n    pre='\\n'.join(lines[:ln])\n    print(ln,'-> ff page', pre.count('\\f')+1)\nEOF"
}
```


### [2026-09-05T20:32:28.146Z] TOOL RESULT

```
total lines 32486 ff count 776
17038 -> ff page 445
17092 -> ff page 446
17179 -> ff page 448
17181 -> ff page 448
17217 -> ff page 448
```


## [2026-09-05T20:32:31.017Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==448' BQT_v1_pages.txt | head -60"
}
```


### [2026-09-05T20:32:32.748Z] TOOL RESULT

```
با لو س ت برءزن‌سالوی ء,کافورمخشوش,ا
و
۳۹
پا لوش - با شن‌قرشت . بروزن‌وممنی
بالوس است که کافورمفدوش باشد» چد درفارسی
سین بشن و برعکس تبدیل می‌باید .
باله - بروزن لاله . قسمی از جوالباشد
که چیز ها را در آن کنند 4
پالیك - بر ون ناهید . ماضی بالیدن
است یمنی افزون کردید و نمو کرد وبزر که شد
بالیدن بروزن‌مالیدن ؛ بمعنی‌بز رکه
شدن و افزون کردیدن و نمو کردن باشد ۴ .
با لیكه - بروزن‌نادیده. آدمی‌ودرخت‌را
گومند که تتومند و بلشد شده باشد ؟ .
با لیات - بروزن تاربك .کفش و پاپوش
بالات - بررزن تاين » بالئی راکوند
که درزس سرنبند ۴ 9
بای بر ست - کنابه از بردم تتبل
و بکاز و هیحکاره باشد .
فا لیس « بر وزن خاکبوی . ولابت
فندهار راگویند :
(۱) چپ ۱: چش : بگاه ,
ام ه بر وزن کام » طرف بیردنی سقف
خائه را گوبند ۵ ؛ و بعضی طرف دروني خانه را
کفه‌اند بقربنة پشت بام. وظاهرآکه نمام پوشش
خانه را بام مگویند - و مخفف بامداد هم‌هست
که صبح پگاء (۱) باشد ۱۷ - ونر بم را یز
کوبند و آن تارکنده ای بنشد که در ساز ها
بندند ۷ - و نام قلعه است در ماوراه اللهر -
و بمعنی فرض و وام غم آمده است .
یام دنشست ه کابه از این است که
خراب شد و ویزان کودید .
بامچشم - یک مم : يك چم را
کوبند و بعربی جفن خوانند . *
بام‌ر و اق بدیع -کنابه ازكعری
و کرسي باشد .
یام‌رد - بکون ات و فتح زای.هوز
و سکون دال ابجذ کوی و نفاره را گویند .
یام ماه مه کنابه از آ-مان اولاست .
که فلك فمر باشد  .‏
پامس « ببنتح الك و سکون سین بی
نقطه . ششصی را گو,ن که ازبودن شهری‌ودباری
که غیر وطن او باشد دلگیر شدء و بتنگآمده
باشد و پتابر مائمي نتواند از آنجا بجای دیگر
رفت - وکسی را ليز گویند که در وطن پای‌بند
هندی قدیم۵۷۵۲۵. ۷۵۲02 ( نم وکردن, بز رکه شدن ) « اسشق۱۷۳». رك : بالش. بالا.
۴ - اسم مفمول از بالیدن . ۴ - در بهلری۵2110 ۱ مت ) « منای۲۹۹ او
0 . پازند ۰02110 دریارسی باستان 032۳003992 «ب رگ۳۱۵». ۵ _ دریهلوی
0 «تاواد,۱۵۹* «بونکر*۰۵ ۰ گیلکی ۰۵200 فریزندی 968 ۰ برنی 0۷18 ۰ نطنزی 11۳0
« . ۱ص ۰۲۹۰ . سمنانی 0سبکسری 0 . لاسگردی 0 , خهمرزادی۵20264
«ل2 . ۲ سر ۱۸۸ . نهرانی 00۲0 . ۲ - دراوستا 081112 ( درخشان ) و درسانسکریت
۱2( . رك : بامداد - .
۲ - بسوز لاله زارم زعشاق نوای زیر + بامی‌برنباید . خواجوی کرمانی. رگن بم.
ه باه‌داد _ م رکب از:بم ۲ داد. در پهلوی 02۳14026, صبح. ۵ بامزه د
ختح‌سوم وچهارم , مر کب از : با -هزه . درپهلوی۳3*1۳9602 , دارای‌طمم خوش *اونوالاد۵۵*.
```


## [2026-09-05T20:32:40.521Z] TOOL CALL #25: Bash

```json
{
 "command": "sed -n 1,60p tools/ref_page.py"
}
```


### [2026-09-05T20:32:40.563Z] TOOL RESULT

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
```


## [2026-09-05T20:32:45.503Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== v4 گوالیدن ===\"; grep -n \"گوالید\\|گوالان\\|گوال \" incoming/BQT/BQT_v4_pages.txt | head -20\necho \"=== v4 pages tags ===\"; grep -n \"pdf page\" incoming/BQT/BQT_v4_pages.txt | head -3"
}
```


### [2026-09-05T20:32:45.562Z] TOOL RESULT

```
=== v4 گوالیدن ===
=== v4 pages tags ===
1:[pdf page 1]
2:[pdf page 2]
23:[pdf page 3]
```


## [2026-09-05T20:32:50.430Z] TOOL CALL #27: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:1848 --image 2>&1 | head -60"
}
```


## [2026-09-05T20:32:52.274Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON گوالیدن ===\"; grep -n \"گوالید\\|گوالان\" MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt incoming/MON/MON_2vol_Adena_v2_djvu.txt | head -20\necho \"=== MON مراکش ===\"; grep -n \"مراکش\" MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt incoming/MON/MON_2vol_Adena_v2_djvu.txt | head -20"
}
```


### [2026-09-05T20:32:58.473Z] TOOL RESULT

```
IMAGE: /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/1848.png
REF: BQT:1848  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 645  OCR-lang: fas

کوازه ۱۸۸
گوازه <- بفتح اول بروزن‌هملازه»بمعنی | و بمعنی مالش و مالیدن هم هت ام از آنکه
گواز است وآن چوبی باشد که ستوران را بدان چیز برابرچیزی بمالند با کسی‌را مالندگی کنند؛
رانند - و هاون چوبی را هم کوبند (۱). وبفتح اول نیز کفته‌اند - و بزبان هندی گاوبانرا
گواش - بنم (۲) اول بروزن قملنی, | کویندیمنی شخصی که محافظت کاوکند ٍ
بمعنی صفت و رنگه ولون باشد ۱ ؛ و بفتم‌اول گوالیدن ۷ بنم اول وفتح اولهر
هم آمده است . دوآمده است » بمعنی بالیدن و نمو کردن ام
گواشمه < بفتح اول و میم بر وزن | ازانسان وحیوان . :
نداشته , دامنیرا کوبند و آن مقنعه و روپاکی گوان - بنتح اول بروزن روان, جمع
باشد که زنان برسر اندازند ۲ . کواست ۸ که پپلوانان و دلیران و شجاعان با
گواشیر « بفتح اول۰ بر وزن تباشیر ۰ | شکوه ونهیب باشند .
نام ولایتی است و در آن فیروزه سفید رنگ هکم گو] نجی - بفتح اول و سکون رابع
بها بهم میرسد ۴ - و بستی کاوشیر هت ۴ و جیم بتحتانی کشیده » بمعنی دلیر و پهلوان
و آن صمغ درختی است که در ۱ باشد - و سردارکوانرا نیز کویند که سپه سالار
دواها بکار برند .کرم و خشعك #8 باشد ‎٩‏ .
است در دویم وسیم - 2 و انگله - بنم ار وتح ثاك,تکده
گوال - بطم اول ابر ۱ رد و حلقه‌ای را گویند که بر گریبان پیراهن وغیره
وزن ومعنی‌جوال امت و جوال ۱ ی دوزند چه گو بمعنی تکمه و انگله حلقه‌ای‌باشد
معرب آنت9 - وبمسی‌بالدن ‏ ها | کهدکوری را درآن اندازند وگاهی آن حلقه را
و نمو کردن ‎٩‏ - و اندوختن بی کوی هم کوانگله میگوبند و همچنی نکوی
وجمم‌نمودن هم آمده امت - کوال - جوال | رانیز بی‌انگله *۱- و جوزکره را هم گفته‌اند
(۱) چش : -گوازه ... هم کوبند . (۲) چش : بفتح .
۱ - رك : جهانگیری . ۴ - رك : جهانگیری . ۴ - گواشیر نام قدییم
شهر کرمان مرکز حکومت ایالت کرمان است . رك4 : ترهةالقلوب صس ۱۳۹ - * ۱2 ؛ور4: کیپان,
جغرافیای سیاسی ص ۲۸۵ ۰ ۲۸۷ . ۴ - ره : گاوشیر . ۵ - کاله . پپلوی
اطع و 8341 ۰« پونکر۷٩»‏ »کردی [02از «اسفا ۷:۱ ص ۲۵۹ طبری [82۷2 (جوال):
مازندرانی کنوبی 8۵۷21 , 80۷/21 . آفع . أ2ْطع « واژه نامه ۹۹۱ ۰ گلبایگانی آ2ناج
( کیه‌ای که در آن پپن‌ريزند . کاله ) « قاسمی » » معرب آن جوال ۰
‎٩‏ - رك4 :گوالیدن . ۷ - از :کوال (ه.م.)+یدن ( پوند مصدری ) » فقس :
بالیدن » هندی باستان ۷1 + ]۷870 ( نموکردن » رشدکردن ) « اسشق ۹۳۹ ۰
۸ - رد4 :گو. ‎٩‏ -ظ . از :گوان ( جمع کو )+ جی ( پوند اتصاف. قس :
میانجی ) . رك : گونجی :
بدرگاه شاهت میانجی منم که در شهر ایران کوانجی منم
فردوسی‌طوسی « فرهنگه نظام > .
۰ کوی‌انگل < گوی‌انگله * رك : انگل » انگله .
```


### [2026-09-05T20:32:58.558Z] TOOL RESULT

```
=== MON گوالیدن ===
MON_part2.txt:35778:گوال: 8۱ ۱- گوالیدن] (امسص.) بالش» 
MON_part2.txt:35786:گوالیدن: 0۷2۱-10 زنمو کردن. م 
MON_part2.txt:35787:گوالاندن» گوالانیدن) (مصرل.) 0 
MON_part2.txt:35788:گوالد؛ خو اهد گوالیدء ابو ال |» گوالنده؛ 
MON_part2.txt:35789:گوالان» گوالیده» گوالش). نمو کردن» نشو 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:35778:گوال: 8۱ ۱- گوالیدن] (امسص.) بالش» 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:35786:گوالیدن: 0۷2۱-10 زنمو کردن. م 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:35787:گوالاندن» گوالانیدن) (مصرل.) 0 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:35788:گوالد؛ خو اهد گوالیدء ابو ال |» گوالنده؛ 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:35789:گوالان» گوالیده» گوالش). نمو کردن» نشو 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:18518:گوالانیدن. (امص.) بالیدگی» نمو. 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:22569:گوالیدن. فزونی» بسیاری. خجستگی» یمن. 
MON_part1.txt:18518:گوالانیدن. (امص.) بالیدگی» نمو. 
MON_part1.txt:22569:گوالیدن. فزونی» بسیاری. خجستگی» یمن. 
=== MON مراکش ===
MON_part2.txt:1075:از مردم شمال آفریقا. مراکشی. در اصطلاح 
MON_part2.txt:64711:دریایی. ملخ مراکشی: (جان.) گو نه‌ای ملخ که 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:1075:از مردم شمال آفریقا. مراکشی. در اصطلاح 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:64711:دریایی. ملخ مراکشی: (جان.) گو نه‌ای ملخ که
```


## [2026-09-05T20:33:08.753Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON گوالیدن ctx ===\"; sed -n '35770,35800p' MON_part2.txt\necho \"=== MON غرب ===\"; grep -n \"^غرب\\|غرب:\" MON_part2.txt | head -10"
}
```


### [2026-09-05T20:33:08.831Z] TOOL RESULT

```
=== MON گوالیدن ctx ===
گواژه: (0) 0-۷322 [ ۳ (۱.) طعنه؛ 
سرزنش:مزاح» شوح طبعی: 
گواس: 5 [ و ان کون - گواشه 
- کواس - کواسه - کواش - کواشه] (ا.) 
طرز» روش. 
کواشمه: (0-)۷25۵0۸ج (۱.) مقنعة زنان. 
کته افت‌نه: (تح) ۱۱50۱۸ (.) آسانی» 
سهولت. (ص.) اسان سهل. 
گوال: 8۱ ۱- گوالیدن] (امسص.) بالش» 
نموء بالیدگی. [- گوالنده] (افا.) در ترکیب به 
معنی « گوالنده» (نمو کننده) ای 
گوال: 21 (امص.) اند و ختن» جمع کردن. 
۱ کنعالتتاه] زاف کر ی 
رگو النده» (اندوزنده» نت وف ر 
کول ذ-0۷81: (امص.) عمل که 
نما؛ نمو» نشو و نما. . فزونی» ریع. مر گنت 
گوالیدن: 0۷2۱-10 زنمو کردن. م 
گوالاندن» گوالانیدن) (مصرل.) 0 
گوالد؛ خو اهد گوالیدء ابو ال |» گوالنده؛ 
گوالان» گوالیده» گوالش). نمو کردن» نشو 
و نما بافتن» بالیدن. اندوختن جمع اتف 
گوانجی: 1 20۷-21701 اگو ۱ (جمع) 
جی» س. اتصاف. قس. میانجی ] (ص‌مر 
اشنا ست‌ددان کون سا دی فسات 
دلاور؛ پهلوان. 
گواه: (ند.0۷250)82۸ع [< گوا - گوه| (رص.) 
کسی که شهادت به امری دهد؛ شاهد؛ ج. 
گواهان. آنجه که در هریز وقوع کاری با 
ِِ ی دلیل» برهان؛ 
م. گو اه‌ها» گواهان .واه دروع: : شاهد 
۲ گواه عادل: شاهد عادل . گواه 
=== MON غرب ===
682:غربال بند. فالگیر. 
1008:غرباء: 2۶ دف. غربا] (ص. 1) ج. 
1012:غربال: ۲۵۲ ,۱۵۲۵21 [- کربال - غرییل - 
1013:غربال؛ معر.] (.) آلتی است دارای سطحی 
1025:غربیل‌بند] (ص‌فا.) ضربال‌ساز» غربال‌باف. 
1033:غربال کر دن: 7۵۲۵2۰ (مص‌م.) الک 
1036:غربالی: -۲۸۲۵2۱ (ص‌نستته.) منسوت به 
1037:غربال. غربالفروش. طشت غربالی: (کد.) 
1058:غربت: ۰۲۳۵۱ (ع. غربة] (مصل.) دور 
1065:غربی: آ-7۵۲۰ (ص نسد.) مسوبت به غرت»
```


## [2026-09-05T20:33:15.058Z] TOOL CALL #30: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-05T20:33:15.062Z] TOOL RESULT

```


```


## [2026-09-05T20:33:16.236Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '990,1012p' MON_part2.txt"
}
```


### [2026-09-05T20:33:16.286Z] TOOL RESULT

```
فصن عقفت) طی شمان علات 
غران: ۵۲۲-0 (ص فا.) آواز گران و مهب 
بر آورنده؛ غرنده. (حا.) در حال غریدن» 
بانگ و فریادکنان. 

غسراورنگ: ۷۸۲-۵ [- خراورنگک] 
(امر.) تخت بزرکگک» سر بر یادشاهی. 

غظرب: ۳۳0 [ع. ۰] (مسصل 0( پنهان شسدن» 
غایب گر دیدن. نابدید گشتن. دور شدن. (ا.) 
جای فرو شدن آفتاب» مغرب؛ مق. مشرق ق. 
همه ممالک و بلادی که نسبت به بلاد دیگر 
در جهت غرب واقع شده‌اند؛ مق. شرق. 
(پز.) آماسی کوچک که در گوشة چشم 
میان چشم و بینی پدید آید. هرگاه این 
آماس بگشاید نا آن را «غعرب» 
گو بند. (ذخیرة خوارزمشاهیء لذ.) 

غرباء: 2۶ دف. غربا] (ص. 1) ج. 
غریب. دوران از بار و دیار. مسافران. 
یگانگان 

غربال: ۲۵۲ ,۱۵۲۵21 [- کربال - غرییل -
```


## [2026-09-05T20:33:25.741Z] TOOL CALL #32: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Europa",
 "prompt": "Give the full etymology section for the Ancient Greek Εὐρώπη / Latin Europa: what origins are proposed (Semitic *ʿerebu/erebu \"sunset\", or Greek eurys+ops, or Pre-Greek), and which does the entry favour? Quote the text."
}
```


## [2026-09-05T20:33:28.113Z] TOOL CALL #33: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%BA%D8%B1%D8%A8#Arabic",
 "prompt": "Give the Arabic etymology of غرب (gharb) and the root غ ر ب: proto-Semitic root, cognates in Hebrew (ערב ʿereb), Akkadian erēbu, Ugaritic, etc. Quote the etymology text."
}
```


### [2026-09-05T20:33:31.551Z] TOOL RESULT

```
# Etymology of Europa

Based on the Wiktionary content provided, the entry does not discuss competing etymological theories for Ancient Greek Εὐρώπη or Latin Europa.

The entry only states:

**For English:** "From Ancient Greek _Εὐρώπη_ (Eurṓpē), a character name in Greek mythology."

**For Latin:** "Borrowed from Doric Greek _Εὐρώπα_ (Eurṓpa); cognate with Attic Greek _Εὐρώπη_ (Eurṓpē)."

The source material makes no mention of proposed origins such as Semitic roots (*ʿerebu/erebu meaning "sunset") or alternative Greek derivations (such as eurys + ops). It presents the term as ultimately deriving from Greek mythology without exploring deeper etymological debates about pre-Greek or Semitic sources.
```


### [2026-09-05T20:33:34.678Z] TOOL RESULT

```
# Arabic Etymology of غرب (gharb)

## Root: غ ر ب (ḡ r b)

The Wiktionary entry indicates that غرب belongs to the **Semitic root غ ر ب**, with 17 terms derived from this root in Arabic.

## Etymology Text

According to the article: "From West Semitic _\*ḡarab-_, cognate with Biblical Hebrew _עֲרָבָה_ (ʿărāḇā́), _עָרָב_ (ʿārāḇ, 'poplar, willow'), Aramaic _עַרְבָּא_ (ʿarəbā)..."

The entry further notes cognates in **Akkadian** (_ur-ba-tu_, "reed, rush" and _ṣar-ba-tu2_, "Euphrates Poplar") and **Soqotri** (_ʿarhíeb_).

## Primary Meaning

In Classical Arabic, غرب (gharb) means "west" or "occident," though the root originally referred to types of trees (poplars and willows) in related Semitic languages, reflecting the botanical significance of these plants across the ancient Near East.
```


## [2026-09-05T20:33:40.718Z] TOOL CALL #34: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%BA%D8%B1%D8%A8#Etymology_2",
 "prompt": "List every Etymology section on this page for Arabic غرب: for each, give the headword (gharb / gharab / gharuba / ghariba etc.), its meaning, and the etymology text verbatim, especially any that says \"west, sunset\" and mentions Proto-Semitic *ġrb or Hebrew ערב ʿereb \"evening\" or Akkadian erēbu."
}
```


## [2026-09-05T20:33:41.506Z] TOOL CALL #35: WebSearch

```json
{
 "query": "Beekes Etymological Dictionary Greek Εὐρώπη Europe pre-Greek Semitic erebu etymology"
}
```


### [2026-09-05T20:33:48.844Z] TOOL RESULT

```
# Etymology Sections for Arabic غرب

## Etymology 1
**Headword:** غَرَبَ (ḡaraba) - verb
**Meanings:** 
- to go away, depart, withdraw, leave
- to set (of the sun, moon, etc.)
- to be a stranger; to be strange, odd, obscure

**Etymology text:** "Root غ ر ب (ḡ r b)" with "17 terms" listed in the category.

## Etymology 2
**Headword:** غَرَب (ḡarab) - noun
**Meanings:**
- Euphrates poplar (*Populus euphratica*)
- willow (*Salix* spp.)

**Etymology text:** "From West Semitic *ḡarab-, cognate with Biblical Hebrew עֲרָבָה (ʿărāḇā́), עָרָב (ʿārāḇ, 'poplar, willow'), Aramaic עַרְבָּא (ʿarəbā)... with possible further connections to Akkadian ur-ba-tu, 'reed, rush'... GIŠṣar-ba-tu2 'Euphrates Poplar'."

## Etymology 3
**Headword:** غُرْب (ḡurb) - noun
**Meaning:** plural of غُرَاب (ḡurāb)
**Etymology text:** No etymology section provided; only pronunciation listed.

**Note:** The noun غَرْب (ḡarb) meaning "west" appears under Etymology 1 but lacks separate etymology documentation beyond the root reference.
```


### [2026-09-05T20:33:50.415Z] TOOL RESULT

```
Web search results for query: "Beekes Etymological Dictionary Greek Εὐρώπη Europe pre-Greek Semitic erebu etymology"

Links: [{"title":"Frühe semitische Lehnwörter im Griechischen – Bryn Mawr Classical Review","url":"https://bmcr.brynmawr.edu/2013/2013.11.54/"},{"title":"Robert S. P. Beekes","url":"https://en.wikipedia.org/wiki/Robert_S._P._Beekes"},{"title":"Beekes Etymological Dictionary Greek","url":"https://www.scribd.com/document/698401131/Beekes-Etymological-Dictionary-Greek"},{"title":"Etymological Dictionary of Greek (2 vols.) (Leiden Indo-European Etymological Dictionary Series, 10): Beekes, Robert: 9789004321861: Amazon.com: Books","url":"https://www.amazon.com/Etymological-Dictionary-Leiden-Indo-European-English/dp/9004321861"},{"title":"Pre-Greek By ROBERT S. P. BEEKES, Leiden","url":"https://www.robertbeekes.nl/wp-content/uploads/2019/08/b121.pdf"},{"title":"Etymological Dictionary of Greek Online","url":"https://dictionaries.brillonline.com/greek"},{"title":"Beekes’ (2010) Etymological Dictionary of Greek","url":"https://koine-greek.com/2017/04/23/beekes-2010-etymological-dictionary-of-greek/"}]

Based on the search results, I found information about Beekes' Etymological Dictionary of Greek and his approach to etymologies, though the results don't specifically address the Europa/erebu etymology you asked about.

Robert S. P. Beekes authored the Etymological Dictionary of Greek for the Leiden Indo-European Etymological Dictionary series. In this work, Beekes derives several words from "Pre-Greek", i.e., the non-Indo-European substrate language that has left numerous traces in the Greek vocabulary. Beekes accepts less Semitic loan material than some other scholars, instead declaring about twenty words as Pre-Greek and some others as Indo-European (including Anatolian).

The search results show that Beekes has a distinctive approach emphasizing Pre-Greek origins over Semitic etymology for many Greek words. However, the specific etymology connecting the Greek name Εὐρώπη (Europa) to Semitic erebu is not addressed in these results. You may need to consult Beekes' dictionary directly or search for more specialized sources on this particular etymology.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-05T20:33:54.386Z] TOOL CALL #36: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/Europe",
 "prompt": "Quote the full Etymonline entry for Europe, including any discussion of the Semitic erebu/erebu \"sunset\" derivation and the eurys+ops alternative, and whether the origin is called uncertain."
}
```


## [2026-09-05T20:33:55.677Z] TOOL CALL #37: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/Morocco",
 "prompt": "Quote the Etymonline entries for Morocco (country) and morocco (leather): what is the origin — Marrakesh, Berber, Arabic maghrib? Give the text verbatim."
}
```


### [2026-09-05T20:33:59.570Z] TOOL RESULT

```
# Etymology of Europe

The Online Etymology Dictionary identifies Europe's origin as **uncertain**. The entry states:

> "from Greek *Europē*, which is of uncertain origin"

The entry presents multiple competing theories:

**"Broad face" theory:** Derived from *eurys* "wide" + *ops* "face/eye"

**Mythological link:** Connected to Europa, a Phoenician princess in Greek mythology

**Semitic theories:** Klein suggests possible origins including:
- Akkadian *erebu* "to go down, set" (referencing the sun)
- Phoenician *'ereb* "evening," meaning "west"

These Semitic proposals parallel the etymology of "occident" (western). The dictionary presents all explanations as possibilities rather than definitive answers, reflecting scholarly uncertainty about the name's true origin.
```


### [2026-09-05T20:34:02.013Z] TOOL RESULT

```
# Etymology of Morocco

**For the country:**

"from Italian, from Berber _Marrakesh_ (properly the name of the city of _Marrakesh_), from Arabic _Maghrib-al-Aqsa_ 'Extreme West.'"

**For the leather:**

"kind of fine flexible leather," originating "ultimately from Morocco, the country in northwest Africa, where the sumac-tanned goatskin leather first was made."

The etymological chain traces back through three linguistic layers: the Arabic term _Maghrib-al-Aqsa_ ("Extreme West"), which entered Berber as _Marrakesh_ (the city name), then passed into Italian and subsequently English, acquiring its current form through the influence of the word "Moor."
```


## [2026-09-05T20:34:10.998Z] TOOL CALL #38: Bash

```json
{
 "command": "ls site/pages/158.jpg 2>/dev/null; pdftoppm -f 158 -l 158 -r 200 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg158 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/"
}
```


## [2026-09-05T20:34:12.463Z] TOOL CALL #39: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Marrakesh",
 "prompt": "Give the etymology of Marrakesh verbatim: Berber amur n akush \"land of God\"? Arabic مراكش? Is a derivation from Arabic Maghrib al-Aqsa mentioned or rejected?"
}
```


### [2026-09-05T20:34:13.183Z] TOOL RESULT

```
site/pages/158.jpg
total 15988
drwx------ 2 sfmqrb sfmqrb    4096 Sep  5 16:34 .
drwx------ 4 sfmqrb sfmqrb    4096 Sep  5 16:02 ..
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
-rw-rw-r-- 1 sfmqrb sfmqrb   67648 Sep  5 16:29 build128.py
-rw-rw-r-- 1 sfmqrb sfmqrb  105345 Sep  5 16:30 build132.py
-rw-rw-r-- 1 sfmqrb sfmqrb   56126 Sep  5 16:29 build136b.py
-rw-rw-r-- 1 sfmqrb sfmqrb   13830 Sep  5 16:22 build136.py
-rw-rw-r-- 1 sfmqrb sfmqrb   66341 Sep  5 16:28 build139.py
-rw-rw-r-- 1 sfmqrb sfmqrb   53260 Sep  5 16:29 build142.py
-rw-rw-r-- 1 sfmqrb sfmqrb   76989 Sep  5 16:32 build145.py
-rw-rw-r-- 1 sfmqrb sfmqrb   21485 Sep  5 16:29 build148.py
-rw-rw-r-- 1 sfmqrb sfmqrb  944060 Sep  5 16:18 kent.txt
-rw-rw-r-- 1 sfmqrb sfmqrb     222 Sep  5 16:30 leaf.py
-rw-rw-r-- 1 sfmqrb sfmqrb   57617 Sep  5 16:20 mk129.py
-rw-rw-r-- 1 sfmqrb sfmqrb   74680 Sep  5 16:26 mk131.py
-rw-rw-r-- 1 sfmqrb sfmqrb   33365 Sep  5 16:25 mk133.py
-rw-rw-r-- 1 sfmqrb sfmqrb   42635 Sep  5 16:29 mk140.py
-rw-rw-r-- 1 sfmqrb sfmqrb   51288 Sep  5 16:30 mk143.py
-rw-rw-r-- 1 sfmqrb sfmqrb   11831 Sep  5 16:32 node4.png
-rw-rw-r-- 1 sfmqrb sfmqrb    7427 Sep  5 16:32 node7.png
-rw-rw-r-- 1 sfmqrb sfmqrb  944060 Sep  5 16:13 oldpers_djvu.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   22067 Sep  5 16:29 part0.json
-rw-rw-r-- 1 sfmqrb sfmqrb   14156 Sep  5 16:22 part1.json
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
-rw-rw-r-- 1 sfmqrb sfmqrb   39131 Sep  5 16:28 pg153.png
-rw-rw-r-- 1 sfmqrb sfmqrb   63033 Sep  5 16:30 pg154.png
-rw-rw-r-- 1 sfmqrb sfmqrb   77057 Sep  5 16:32 pg155.png
-rw-rw-r-- 1 sfmqrb sfmqrb   80624 Sep  5 16:34 pg158.png
-rw-rw-r-- 1 sfmqrb sfmqrb  124379 Sep  5 16:31 pg159_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb   27814 Sep  5 16:31 pg159.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4694 Sep  5 16:31 pg159_word.png
-rw-rw-r-- 1 sfmqrb sfmqrb   25911 Sep  5 16:32 pg163.png
-rw-rw-r-- 1 sfmqrb sfmqrb   59398 Sep  5 16:33 pg164.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4868 Sep  5 16:14 prt.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  333088 Sep  5 16:16 sod135_c.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1817364 Sep  5 16:16 sod135.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  101641 Sep  5 16:15 sod136_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1892712 Sep  5 16:15 sod136.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   56398 Sep  5 16:26 write144.py
```


### [2026-09-05T20:34:17.204Z] TOOL RESULT

```
# Etymology of Marrakesh

Based on the Wiktionary content provided, the etymology states:

"Derived from French _Marrakech_, from Moroccan Arabic _مَرَّاكُش_ (Marrākuš)."

The document does not mention the Berber origin "amur n akush" or discuss any connection to Arabic "Maghrib al-Aqsa." It only traces the word back through French to Moroccan Arabic.
```


## [2026-09-05T20:34:18.890Z] TOOL CALL #40: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/site/pages/158.jpg"
}
```


### [2026-09-05T20:34:18.916Z] TOOL RESULT

```

```


## [2026-09-05T20:34:35.269Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && pdftoppm -f 158 -l 158 -r 600 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf pg158_600 && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg158_600.png'); print(im.size)\nw,h=im.size\nim.crop((int(0.20*w),int(0.135*h),int(0.60*w),int(0.175*h))).save('crop_arabic_refs.png')\nim.crop((int(0.20*w),int(0.195*h),int(0.85*w),int(0.30*h))).save('crop_morocco.png')\n\""
}
```


### [2026-09-05T20:34:40.576Z] TOOL RESULT

```
(5100, 6600)
```


## [2026-09-05T20:34:42.923Z] TOOL CALL #42: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/crop_arabic_refs.png"
}
```


### [2026-09-05T20:34:42.985Z] TOOL RESULT

```

```


## [2026-09-05T20:34:42.981Z] INPUT

[Image: original 2040x264, displayed at 2000x259. Multiply coordinates by 1.02 to map to original image.]


## [2026-09-05T20:34:49.009Z] TOOL CALL #43: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/crop_morocco.png"
}
```


### [2026-09-05T20:34:49.192Z] TOOL RESULT

```

```


## [2026-09-05T20:34:49.190Z] INPUT

[Image: original 3315x693, displayed at 2000x418. Multiply coordinates by 1.66 to map to original image.]


## [2026-09-05T20:34:58.606Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AKD leaves ===\"; awk 'BEGIN{RS=\"\\f\"} END{print NR}' AKD.txt\necho \"=== AKD leaf 72 (p.64) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==72' AKD.txt | head -40\necho \"=== AKD erebu ===\"; grep -n \"erebu\\|ereb\\b\\|Europa\" AKD.txt | head -20"
}
```


## [2026-09-05T20:34:59.499Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== NAT Morocco ===\"; grep -n \"Morocco\\|Marrakesh\\|Maghrib\" NAT_2005.txt | head -20"
}
```


### [2026-09-05T20:35:00.522Z] TOOL RESULT

```
=== AKD leaves ===
111
=== AKD leaf 72 (p.64) ===
agung auf  entsprechende  griechische  imd  römisclie  Göttergostalten  ge- wandert, nämlich:  1)  'Eq/x^s,  Merctirius ,  2)  AqsQoShtj,  Venus,  3)  AQtje, Mars,  4)  Zevg,  Juppiter,  5)  Kqövos,  Saturnus.
1)  Vokalisation  unsicher.  2)  Falls  nicht  vielmehr  pflanzlicher  Herkunft.
3)  Und  zwar  ist  die  viell.   zugrunde  liegende  Pflanze   *amämu  dann  wohl  iden- tisch mit  aram.  hamämil,  IpmämSy  arab.  hamamä,  griech.  äfimftor,  Ämomum.
4)  S.  oben  S.  61  unter  amämii.
5)  So  außer  im  Aram.  auch  im  Hebr.  an  der  Stelle  Am.  5,  26,  woraus  durch  Ent- stellung Patipav,  Pe/i(pav  der  LXX  und  des  NT;  ferner  auch  Kaiwan  im  Arab.-Pers.
      62        ,
Ebenso  sind  mit  der  ganzen  Vorstellung  auch  die  Namen  der  Tier- kreisbilder, hier  allerdings  so  gut  wie  durchweg  in  Übersetzung,  von den  Babyloniern  wie  zu  andern  orientalischen  Völkern,  so  zu  den  Griechen und  Kömern  und  damit  bis  zu  uns  gewandert.  Im  Einzelnen  entsprechen hier  ohne  weiteres  akk.  od.  sum.  2)  gu{-anna)  (Himmels-)Stier,  3)  mas- tahba  galgala,  Zwillinge,  5)  ur-gula  od.  ä.  eig.  großer  Hund  d.  i.  wohl Löwe,  7)  sibanUu  Wage,  S)  gir-tah,  zuqaq/jm  Skorpion,  9)  der  Schütze  Pa- hil-sag,  10)  sulmr-mas,  suhunnasu  „Scliraubenhornzickleinfisch",  12)  min? Fische,  den  griech.-röm.  usw.  Namen  2)  r«Ppoj,  taurus,  Stier,  3)  SiSvf/oi, geniini,  Zwillinge,  5)  X^wp,  leo,  Löwe,  7)  ^vyös,  Ultra,  Wage,  8)  axoQniot, scorpius,  Skor]}ion,  9)  j-o|or>;?,  arcitenens,  Schütse,  10)  atyöxiQwg,  capricormis (caper),  Steinbock,  12)  t'x^vi?,  pisces,  Fische.  Aber  auch  1)  xQtög,  arics, Widder,  4)  xuQxlvog,  Cancer,  Krebs,  6)  naQ&ivog,  virgo,  Jungfrau,  11)  iSQoxöog (ü^p/a),  aquarius  (amphora),  Wassermann,  haben  im  Babylonischen  un- mittelbar oder  wenigstens  mittelbar  ihre  Vorlage,  wenn  hier  auch  der Sachverhalt  etwas  verwickelter  ist,  und  darum  im  Einzelnen  hier  nicht vorgeführt  werden  kann.
Ähnlich  hegt  die  Sache  für  das  arain.  Sprachgebiet,  wie  auch  für das  Arabische  und  für  andere  orientalische  Sprach-  und  Kulturkreise,  in- dem hier  die  Namen  der  Tierkreisbilder  teils  direkt  als  Übersetzungen  der babylonischen,  teUs  auch  durch  das  Grriechische  hindurchgegangen,  vor- liegen. Wirkliche  Wortentlehnungen  finden  sich  hier  nur  vereinzelt,  so zunächst  der  Gesamtname  für  die  Tierkreissterne  aram.  (syr.  u.  mand.) malwrisä,  wolil  <[  akk.  (sum.)  *nml-mas;  —  ebenso  liebr.  PI.  mazsalöt'^ 2  Kön.  23,  .5,  jüd.-arani.  mazzald,  syr.  manzaltä,  mand.  PI.  manzalCitci,  arab. mansil^  <C  akk.  mazzaltu  für  manzaztu  (von  nazä
=== AKD erebu ===
326:Zu  ina  libbi  ade  erebu  sich  verpflichten  s.  oben  S.  11.
1016:akk.  ersbu  allg.  eintreten,  hineingehen  (z.  B.  in  ein  Haus),  dann  spez. untergehen  (von  der  Sonne  und  den  Gestirnen^),  ereb  samsi  Sonnen- untergang, Westen  :  >  viel!.,  dann  allerdings  schon  Mih,  hebr.  'äreh Abend,  aram.  'arab,  "arah,  arab.  gariha,  äth.  'arha  untergehen  (von  der Sonne),  hebr.  maärah,  aram.  marabä,  arab.  magrah,  magrib,  äth.  maräb Westen.  Desgl.  wird  der  Gebrauch  des  hebr.  6ö(').  »läbdO  und  des  aram. 'all,  meül-  eig.  hineingehen,  Eingang,  für  Untergang  der  Sonne,  auf  An- lehnung an  das  akk.  erebu  in  diesem  Sinne  beruhen.  akk.  am  allg. herausgehen  (=  allg.  semit.  ««/'),  dann  spez.  aufgehen  (von  der  Sonne  und den  Gestirnen^),  M  samsi  Sonnenaufgang,  Osten  :  in  Anlehnung  hieran wohl  hebr.  jäsäC),  mömC),  phön.  nt-f,  altaram.  mwqCi,  ägypt.-aram.  mivsä eig.  herausgehen,  Ausgang,  für  Aufgang  der  Sonne.
```


### [2026-09-05T20:35:00.563Z] TOOL RESULT

```
=== NAT Morocco ===
1195:Malaya melayu, “those who fled” or ‘‘the fleers”’ Morocco | maghrib, ‘“‘the west” Singapore “Lion City” (from the many statues of the British Lion) Somalia “Land of Hospitality” Sudan “Land of the Blacks” Taiwan “Terrace Bay”’ Tanganyika “Land of Many Tribes” (now Tanzania) Thai (Thailand) ‘Free’ . Togo “The other side of the lake” Vietnam ‘The Far South.” The older name
1915:After a long and arduous campaign ending in 1926, French colonial troops finally defeated the Moroccan Riff leader, Abd-el-Krim, who had been attempting, with initial success, to free Morocco from French and Spanish domination. For security reasons his place of exile was Reunion Island, an isolated spot in the southern Indian Ocean. Abd-el-Krim’s reaction, upon learning of his place of exile, was simply: Réunion? Mais avec qui? (‘‘Reunion? But with whom?”)
```


## [2026-09-05T20:35:10.714Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nfor f,lns in (('AKD.txt',[326,1016]),('NAT_2005.txt',[1195])):\n    t=open(f,encoding='utf-8',errors='replace').read()\n    lines=t.split('\\n')\n    for ln in lns:\n        pre='\\n'.join(lines[:ln])\n        leaf=pre.count('\\f')  # 0-based\n        print(f,ln,'0-based leaf',leaf,'printed(AKD leaf-8)=',leaf-8,'printed(NAT leaf-15)=',leaf-15)\nEOF"
}
```


### [2026-09-05T20:35:12.401Z] TOOL RESULT

```
AKD.txt 326 0-based leaf 33 printed(AKD leaf-8)= 25 printed(NAT leaf-15)= 18
AKD.txt 1016 0-based leaf 73 printed(AKD leaf-8)= 65 printed(NAT leaf-15)= 58
NAT_2005.txt 1195 0-based leaf 182 printed(AKD leaf-8)= 174 printed(NAT leaf-15)= 167
```


## [2026-09-05T20:35:30.701Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== LKT Marokko/maroquin ===\"; grep -n \"Marokko\\|Marrakesch\\|maroquin\\|Maghrib\\|Magrib\" LKT.txt | head -15\necho \"=== DEV maroquin ===\"; grep -n -i \"maroquin\\|maroc\\b\\|MAROC\" DEV.txt | head -10\necho \"=== PHN maroquin ===\"; grep -n -i \"maroquin\\|Maroc\" PHN.txt | head -10"
}
```


### [2026-09-05T20:35:30.784Z] TOOL RESULT

```
=== LKT Marokko/maroquin ===
463:Im  Vulgärarabischen  des  Magrib  [Nord- westafrika] Interjektion  zum  Antreiben der  Tiere  [JAs  1843,  II,  216],  vielleicht
844:[Sskr.  badara,  vadara].  einer  der  am weitesten  verbreiteten  Charakterbäume Indiens,  Ficus  indica  oder  bens^alensis. Im  Gebiete  von  Birma  bis  zum  Pänd- schäh  heimisch,  findet  er  sich  jetzt  von Queensland  und  China  bis  nach  Marokko und  Guinea  angepflanzt.  Angloind. burr  tree,  engl,  gewöhnlich  banian-tree [von  französischen  Reiseschriftstellern oft  falschlich  bananier  genannt]  nach der  Bezeichnung  der  indischen  Ein- geborenen als  Banianen  [aus  hind. banyä  'Kaufmann,  Händler'].  [Hobson- Johson  77.
907:.320.  Ar.  bizzäf : 'Sehr',  vulgärer  Ausdruck  im  Magrib [Algier,  vgl.  Ad.  Wahrmund,  Praktisches Handbuch  der  neu-arabischen  Sprache. Gießen  1898.  S.  214,  Nr.  7*;  Marokko, vgl.  G.  Kampffmeyer,  Marokkanisch- arabische Gespräche.  Berlin  1912.  S.  17, Z.  3  V.  u.],  mit  Imäla  gesprochen: bizzef;  hieraus  it.  a  bizzeffe,  siz.  a  biz- zeffi  'reichlich',  frz.  (Argot)  bizef  'dass.'. [De  Gregorio  in  Romania  XXXI,  110  f. GrSVociSic  228.    ML  1143.
1500:N.  pr.,  Hauptstadt  von  Marokko:  hieraus die  Bezeichnung  der  Kopfbedeckung  der Muslimen ;  über  tk.  fes  wurde  rum.  fes, iTZ.fez;  fiel,  pheci  {—  kepi\,  dtsch.  Fez usw.  —  ,Die  heute  in  Europa  allgemein gebräuchliche  Bezeichnung  Fez  für  die in  den  verschiedensten  Formen  vor- kommende, fast  in  der  ganzen  muham- medanischen  Welt  übliche  rote  Kopf- bedeckung hat  mit  Fes,  der  Hauptstadt von  Marokko,  nichts  mehr  zu  tun,  wenn auch  der  Name  auf  Fes  als  dem  ursprüng- lichen Fabrikationsort  hindeuten  mag. Die  heutigen  Fese  stammen  fast  durch- weg aus  Europa,  insbesondere  aus  Öster- reich. In  der  Stadt  Fes  werden  nur spitz  zulaufende  Tarbusche  aus  grobem, rotem  Filz  mit  kleiner  blauer  Seiden- quaste hergestellt,  welche  hauptsächlich von  den  marokkanischen  Soldaten  unter einem  großen  weißen  Turban  getragen werden. "  Max  Freiherr  von  Oppenheim,
1521:Adj.  zu  Tafilet,  Taßalet,  N.  pr.,  Name einer  Stadt  in  Marokko,  wo  feine  Leder- waren und  Gewebe  hergestellt  wurden. Hieraus  sp.  tafilete  'Maroquinleder',  frz. filali  'Lederarbeit'  und  sp.  fileli  'Art feinen  Gewebes',  rum.  filalin  'starker, feiner  Seidenstoff'.  [DEFREMERY  in JAs  1861,  1,  90.  DE  268.  Devic  DEt 1 20.
1669:'Westlich';  hieraus  il.garbino,  frz. garbin 'Südwestwind'  auf  dem  Mittelmeere, prov.  garbin,  sp.  garbino  'Süd-  oder Westwind',  sp.  pg.  algarve  'fruchtbar', pg.  garabia  'Westen'.  Aus  dem  It. wurde  serb.  garbin  'Südwind'.  Jeden- falls mit  Kontamination  von  al-  arabija 'die  arabische  Sprache'  entstand  pg.  al- garabia,  pg.  algravia,  frz.  charabia  'un- verständliches Zeug,  Kauderwelsch',  frz. insbesondere  'Dialekt  der  Auvergne'.  — Aus  demselben  Stamme  ar.  garaba 'untergehen  (Sonne)'  ist  mit  präfigiertem ma-  zur  Angabe  des  Ortes  magrib  ge- bildet; der  Magreb  ist  Nordwestafrika von  Tunis  bis  Marokko;  ms  al-magribl 'der  Bewohner  des  M.'  wurde  irz. maugrebin  'dass.'.  —  Auch  der  Name der  pg.  Provinz  Algarve  ist  ar.  garb 'Westen',  daher  sp.  algarabio,  algarabia, pg.  algaravio  'Bewohner  von  Algarve'. [DE  119.  241.  Eguilaz  178.  Devic  DEt 125.    ML  3683.    Bern  SlEtWb  295.
1699:689.  Ar.  garräfa: 'Weitbauchige  Flasche'  [vom  Vb.  garafa 'schöpfen';  das  Subst.  ist  nicht  klassisch- ar.,  sondern  scheint  nur  vulgär  imMagrib, s.  hier  Nr.  674,  gebräuchlich  zu  sein] ; hieraus  sp.  pg.  garrafa,  frz.  caraffe, carafe,  it.  caraffa,  siz.  carrabba  'Wasser- flasche, Flasche  für  Wein  od.  ähnl.'; dtsch.  Karaffe,  Karaffine,  ndl.  karaf, engl,  caraffe;  russ.  grafin,  poln.  karafka, ßech.  karafina,  bulg.  karafa.  —  [Ab- leitung aus  ar.  kar'a  'Kürbis,  Kürbis- flasche' geht  für  kat.  carbassa,  sp.  cala- baza,  pg.  cabaga  'Flasche'  ebensowenig wie  die  Gruppe  caraffe  aus  angeblichem ar.  karä'a  ML  4676  u.  6900].  —  [DE 274.  Dozy  Oost  48/50.  Hobson-Jobson 160.    Gorjajew  78.
1795:N.  pr.,  ein  tk.  Stamm,  dessen  Angehörige von  den  Almohaden  in  Marokko  und Spanien  (1 130—1269)  zu  Henkersdiensten gebraucht  wurden ;  hieraus  mit  ar.  Art. pg.  algoz,  sp.  algoce  'Henker,  Scharf- richter', sp.  pg.  algozaria  'Grausamkeit, grausame  Handlung'.  [DE  128/129. Eguilaz  182.    ML  3826  a.
1821:Vulgäre  Aussprache  des  klass.-ar.  kaum 'Truppe,  Schar',  im  Magrib  [s.  hier Nr.  674]  gebräuchlich;  hieraus  frz.  goum 'Raubkarawane',  nach  Devic  DEt  131 auch  jContingent  militaire  des  tribus alg^riennes".
2033:rauchen  in  Ägypten  verbreitet.  In Marokko  wird  der  Hanf  klf  genannt, klein  geiiackt  und  mit  Tabak  vermischt oder  auch  unvermengt  in  winzig  kleinen Tonköpfchen  aus  etwa  1  Fuß  langen Pfeifen  sehr  viel  geraucht."  Max  Frei- herr V.  Oppenheim,  Vom  Mittelmeer  zum Persischen  Golf  I,  74.  Genaueres  über die  in  Marokko  benutzten  Pfeifen  und die  Art  des  Hanfrauchens  sowie  die  ar. Ausdrücke  dafür  vgl.  MSOS  H,  231 u.  232.  —  Auf  das  oben  erwähnte haMM  hat  SILVESTRE  DE  SAGY  ein weit  verbreitetes  romanisches  Wort zurückgeführt  [de  S.,  Memoire  sur  la dynastie  des  Assassins  et  sur  l'origine de  leur  nom.  Lu  ä  la  seance  publique de  l'Institut  du  7  juillet  1809.  Im  Mo- niteur  no.  210,  an  1809  und  Lettre  de M.  de  S.  au  redacteur  du  Moniteur  sur I'etymologie  du  nom  des  Assassins. Ebenda  no.  359,  an  1809].  Aus  der  Ge- schichte der  Kreuzzüge  ist  der  ,AIte vom  Berge"  bekannt,  der  das  Haupt einer  Sekte  war,  deren  neue  Mitglieder, durch  den  Hanfrausch  fanatisiert,  auf Befehl  ihrer  Obern  selbst  Mordtaten begingen;  aus  dem  ar.  Namen  dieser Sekte  hassäsln  entstand  it.  assassino 'Meuchelmörder',  prov.  asasi,  ansesi, frz.  assassin,  sp.  asesino,  pg.  assassino, rum.  asasin  und  die  dazugehörigen Verba  assassinare  usw.  und  andere  Ab- leitungen. It.  (dial.  Parma)  sasinä  'be- raubt, elend;  Weinbergschnecke'.  — Autiallend  ist,  daß  in  allen  Formen  die beiden  s  verschwunden  sind,  daher schlägt  Lammens  Rem  28  als  Grund- wort den  Namen  des  Gründers  jener meuchelmörderischen  Sekte,  Hasan  ihn §abäh,  vor;  jedoch  scheint  diese  An- nahme nicht  notwendig,  da  im  MA Namen,  die  über  das  Lateinische  ver- breitet wurden,  allgemein  das  s  durch einfaches  s  ersetzten.  [DE  207.  Egui- laz  293.   ML  4074.
2097:Im  Magrib  haill;  hieraus  mit  ar.  Art. sp.  aleli,  alheU  'Levkoje,  Matthiola',  pg. alleli  'dass.'  [Gonstancio  Dicc  54  a].  — DE  98.
2339:'Stamm' ;  hieraus  asp.  cabila,  alcavera, sp.  gabilla,  apg.  cabilla,  cabilda,  pg.  al- cdbella,  alcavale  'Schar',  frz.  kabyle  Be- zeichnung der  Berberstämme  Algeriens und  Marokkos,  la  Kabylie  ihre  Heimat, engl,  kabyle,  dtsch.  Kabyle  'Angehöriger dieser  Stämme'.  [DE  77.  244.  271. Eguilaz  332.    ML  6894.
2912:Vulg.,  bes.  in  Marokko  kummlja,  'ein Dolch',  etwa  38  cm  lang  und  2  bis  3  cm breit,  nach  auswärts  gekrümmt,  den  der gewöhnliche  Marokkaner,  Städter  wie Beduine,  stets  trägt  [FISCHER  in  MSOS II,  224/227];  hieraus  sp.  gumia,  cumia, pg.  gomia,  agomia,  agumia  'Art  Üolch'. —  [Als  andere  Grundwörter  werden  lat. acumen  und  guvia  'Meißel'  genannt, Eguilaz  416;  eine  ganz  lächerliche  Ab- leitung gibt  Schapiro  Revel  41.]  [Dozy Suppl  II,  487.    DE  282.
2963:Ein  Gericht  aus  Mehl  und  Fleisch,  bei armen  Leuten  aus  Mehl  und  Wasser, das  in  einem  Teile  Nordafrikas  fast  als Nationalspeise  gelten  kann  [daß  es  je- doch keineswegs  im  ganzen  Magrib bekannt  oder  gebräuchhch  ist,  zeigt KAMPFFMEYER  in  MSOS  VIII,  229, Anm.  6];  hieraus  sp.  alcuzcuz,  alcuzcü, coscucho,  frz.  couscous,  auf  St.  Domingo: coussecouche,  siz.  cüscusu  'Gries',  als Interjektion  oh  cuscusti  'potztausend!'; ndl.  koeskoes  'Ragout,  Gemengsei',  auch in  übertragenem  Sinne.  [Dozy  Oost  53/54. ZfromPh  XXX,  465.  DE  96.  Devic DEt  99.    ML  4796.
3244:Jetzt  Marrähes,  die  frühere  südliche Hauptstadt  Marokkos;  hiernach  wird  das Ziegenleder  genannt,  das  in  Marokko hergestellt  und  jetzt  in  Europa  imitiert wird:  pg.  marroquim  [Gonstancio  Dicc 679  c],  frz.  maroquin,  ndl.  marohijn, dtsch.  Maroquin;  engl,  morocco  'feines dünnes  marokkanisches  Leder'.  —  [Frz. maroquin  'Tau,  welches  vom  Topp  des Fockmastes  zum  Topp  des  grofsen  Mastes geht  und  dazu  dient,  eine  Ladetakel daranzuhängen,  um  vermittelst  der- selben Güter  aus-  und  einzuladen',  also dtsch.  'Toppreep',  fi'z.  surpente,  ist  wohl mit  ndl.  marren  'festbinden'  in  Zusam- menhang zu  bringen,  vgl.  Behrens  ßeitr. 373/374].
=== DEV maroquin ===
531:Argan  ou  Argane.  Genre  de  plantes  (arbres  et  arbris- seaux) dont  le  type  est  l'argan  du  Maroc  [sideroxylon  spi- nosum  de  Linné).  c^Les  forêts  d'argans  qu'on  traverse  en voyageant  dans  l'Atlas  font  grand  plaisir  à  rencontrer, tant  à  cause  de  la  variété  des  bois  dont  elles  sont  plan- tées, que  parce  qu'elles  reposent  l'œil  fatigué  de  la  stéri- lité du  reste  du  pays,  w  (Relation  du  D'  Lemprière  ^)  ^he pays  est  magnifique,  semé  de  superbes  forêts  d'argans.w (James  Richardson^.)  C'est  l'arabe  ij^)^  ardjân  ou  argân.
681:rie  et  au  Maroc  dans  le  sens  de  chacal,  dlnb  (précédé  de l'article  adii  pour  al)  a  donné  en  portugais  adibe,  en  espa- gnol adive,  qui  a  passé  en  français.  Nos  dictionnaires d'histoire  naturelle  donnent  aussi  adil  On  peut  voir,  là- dessus,  Dozy  (^Gloss.  p.  /i5)  et  Defrémery  (^Journ.  asiat. janvier  1862 ,  p.  87).
1353:Fez.  La  coiffure  ainsi  appelée  tire  son  nom  de  la  ville marocaine  de  Fez  ,j-U,  oii  elle  se  fabrique.  Le  terme  mi- litaireyèci  ou  'phéci  (képi)  est  un  adjectif  de  même  prove- nance, f^lifëci,  de  Fez.  Inutile  de  chercher  yè^;,  féci  (ni même  kéjn)  dans  le  Dictionnaire  français- arabe  j)Our  la  con- versation en  Algérie,  de  M.  Cherbonneau.
1354:FiLALi.  ^^  Industrie  ])articulière  de  la  côte  méditerra- néenne de  l'Afrique  et  dont  le  siège  principal  est  Tafilet, dans  le  Maroc;  elle  a  pour  objet  la  préparation  des  cuirs et  maroquins,  la  fabrication  des  chaussures,  brides,  selles, etc.  On  trouve  des  ouvriers  en  fdali  dans  toute  l'Algérie,  w (Bouillet,  Dictionn.  des  scienc}j  C'est  l'adjectif  arabe  <j!^ fdcdi,  de  Tafilet  ou  Tafdalet.  En  espagnol ,  yî'/f// désigne une  sorte  de  tissu  fabriqué  originairement  dans  le  même pays.  M.  Defrémery^  a  le  premier  établi  cette  étymologie, abondamment  confinnée  par  M.  Dozy  dans  son  Glossaire, p.  268.  L'espagnol  a  aussi  tafilete  dans  le  sens  de  maro- quin, peau  de  Tafdet.
1700:De  ce  mot  vient  l'espagnol  mazmorra,  cachot,  fosse, prison.  On  peut  voir,  dans  la  Relation  du  sieur  Mouette"^, qui  fut  captif  au  Maroc  de  16-70  à  1681,  la  description de  la  mazmorra  où  on  le  renfermait  la  nuit  avec  les  autres esclaves  :  ^^  C'étaient  de  vrais  silos  creusés  sous  terre  .  .  . on  faisait  descendre  les  esclaves  dans  ce  trou  par  une échelle  de  corde.  ??
1768:xMoLLAH  ^  De  l'arabe  J^  maulâ,  maître,  seigneur,  ma- gistrat, écrit  souvent  ^y>  et  prononcé  vulgairement  en Turquie  mollâ.  C'est  de  ce  même  mot,  suivi  du  pronom  <^ ~i  de  la  première  personne,  <^i|^  maulâ-i,  mon  seigneur, que  nous  avons  fait  muley,  titre  précédant  le  nom  des  em- pereurs du  Maroc  et  souvent  pris  à  tort  pour  un  nom propre.
=== PHN maroquin ===
1568:tagne et la mer. En 1079, ils fondèrent la ville de Maroc;
1575:Almohades, et chassés d'abord d'Aghmat et de Maroc, de 1190
1950:mier quart du xii* siècle, Averroès vint à Maroc, et fut nommé
1952:11 mourut à Maroc, on 1 198 suivant les uns, en 1 906 suivant
2067:de bottines en maroquin portées par les deux sexes, est d'un
2130:par exemple, du mot maroquin, en parlant d'un genre de cuir
2131:fabriqué particulièrement dans la ville de Maroc.
2331:les pays de Sous, Tafilet et Sédjelmassat dans le Maroc; au nord»
2850:nomme ainsi, dans le Maroc, une troupe de marchands qui
3301:que les Arabes de l'Afrique occidentale pour le maroquin. Aussi
```


## [2026-09-05T20:35:33.510Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SKT Europe/ortho ===\"; grep -n \"^Europe\\|Europe,\\|ORTHO\\|ortho-\" SKT.txt | head -10\necho \"=== WLD uerdh ===\"; grep -n \"uerdh\\|u̯erdh\\|urdhva\\|ürdhva\\|ördhva\" WLD_band3.txt incoming/WLD/WLD_Bd1_pages.txt 2>/dev/null | head -10\necho \"=== AHD watkins werdh ===\"; grep -n \"werdh\\|wredh\\|ered\\b\" AHD_watkins1985.txt | head -20"
}
```


### [2026-09-05T20:35:33.590Z] TOOL RESULT

```
=== SKT Europe/ortho ===
=== WLD uerdh ===
incoming/WLD/WLD_Bd1_pages.txt:7616:ai. urdhva-, ioedco, sgedtCto, ooodvvo) erwiihnt, die aber in ganz andere
incoming/WLD/WLD_Bd1_pages.txt:13487:oodog, ai. urdhva- !s. ueredh-) umgebildet, sondern setzt (wie allenfalls
=== AHD watkins werdh ===
48:Speaking to the Asiatick Society in Cal- cutta on February 2, 1786, the English orien- talist and jurist Sir William Jones uttered his famous pronouncement:
54:French scholar Antoine Meillet, ‘we will term Indo-European language every lan- guage which at any time whatever, in any place whatever, and however altered, is a form taken by this ancestor language, and which thus continues by an uninterrupted tradition the usage of Indo-European.”
75:It is noteworthy that no single language in the family preserves this word intact. In every language, in every tradition in the Indo-European family, the word has been altered in some way from its original shape. It is the comparative method that permits us to explain the different forms in this variety of languages by the reconstruction of a uni- tary common prototype, a common ancestor.
102:The comparative study of Indo-European poetics has shown that such compounds were considered particularly apt for elevated, for- mal styles of discourse; they are a salient characteristic especially of Indo-European poetic language. In addition, it is amply clear that in Indo-European society the names of individual persons—at least in the priestly and ruling (or warrior) classes—were formed by such two-member compounds. Greek names like Sophocles, “famed for wisdom,” Celtic names like Vercingetorix, “warrior- king,” Slavic names like Wenceslas, “having greater gory,” Old Persian names like Xerxes, “ruling men,” Germanic names like Bertram, “bright raven,” are all compounds. The type goes as far back as Proto-Indo-Huropean, even if the individual names do not. English family names continue the same tradition with such types as Cartwright and Shake- speare, as do those of other languages, like Irish (O’)Toole, “‘people’s valor.”
105:A word of caution should be entered about the semantics of the roots. It is perhaps more hazardous to attempt to reconstruct meaning than to reconstruct linguistic form, and the meaning of a root can only be extrapolated from the meanings of its descendants. Often these diverge sharply from one another, and the scholar is reduced in practice to inferring only what seems a reasonable, or even merely possible, semantic common denominator. The result is that reconstructed words and particulary roots are often assigned hazy, vague, or unspecific meanings. This is doubt- less quite illusory; no human society from Proto-Indo-European times to the present day would be viable if conversation were limited to vague generalities. The apparent haziness in meaning of a given Indo- European root often simply reflects the fact that with the passage of several millennia the different words in divergent languages de- rived from this root have undergone semantic changes that are no longer recoverable in detail.
133:wes-pero-. The Indo-Europeans oriented themselves by facing east. Therefore the root deks-, “right,” could also denote “south.” “Right” was considered lucky; the terms for “left” vary from language to language (one Indo-European term is laiwo-) and were evi- dently subject to taboo.
193:For this essay, we have given only the information about Indo-European culture that could be derived from language and lexicon alone. Other disciplines serve to fill out and complete the picture to be gathered from the study of vocabulary: archaeology, prehistory, comparative religion, and the his- tory of institutions.
194:Archaeologists have not in fact succeeded in locating the Indo-Europeans. An artifact other than a written record is silent on the language of its user, and prehistoric Eurasia offers an abundant choice of culture areas. Archaeologists are generally agreed that the so-called Kurgan peoples, named after the Russian word for their characteristic “bar- row” or “tumulus” grave structure, spoke an Indo-European language. Some time around the middle of the fifth millennium B.c., these people expanded from the steppe zone north of the Black Sea and beyond the Volga into the Balkans and adjacent areas. These Kur- gan peoples bore a new mobile and aggressive culture into Neolithic Europe, and it is not unreasonable to associate them with the coming of the Indo-Europeans. But the Kur- gan peoples’ movement into Europe took place in distinct waves from the fifth to the third millennium B.c. The earliest so far discovered might be compatible with a rea- sonable date for Proto-Indo-European, that is, a date sufficiently long ago for a single language to develop into forms as divergent as Mycenean Greek and Hittite as they are historically attested by the middle of the second millennium B.c. But the later Kurgan immigrations after 4,000 B.c. are too late to be regarded as incursions of speakers of un- differentiated Proto-Indo-European. The archaeological evidence for the later waves of Kurgan migrations points to their having had an Indo-European culture, but the lan- guages spoken by the later Kurgan peoples must have been already differentiated Indo- European dialects, some of which would doubtless evolve into some of the historical branches of the family tree. We must be content to recognize the Kurgan peoples as speakers of certain Indo-European languages and as sharing a common Indo-European cultural patrimony. The ultimate “cradle” of the Indo-Europeans may well never be known, and language remains the best and fullest evidence for prehistoric Indo- European society.
244:variant form. A form altered in any way other than in the above categories.
251:In order to emphasize the fact that English belongs to the Germanic branch of Indo- European and to give precedence to directly inherited words in contrast to words bor- rowed from other branches, the intermediate stages in Germanic etymologies are covered in fuller detail. The Common or Proto- Germanic (called simply Germanic) forms
264:agh-?. A day (considered as a span of time). Germanic *dagaz (with initial d- of obscure origin), day, in: a. Old English deg, day: DAY; (DAISY), TODAY; b. Old English denominative dagian, to dawn: DAWN. [Pok. agher- 7.]
330:3. O-grade form *bhol- in Germanic *ball- in: a. Old English beallucas, testicles: BOLLIX; b. Old Norse bdllr, ball: BALL; c. Danish bolle, round roll, akin to the probable Scandinavian source of BILBERRY; d. Middle High German baile (> Italian balla, palla), ball: BAL- LOON, BALLOT; PALL-MALL; e. French baile, ball: BAL- LOTTEMENT; f. Old French baie, rolled-up bundle: BALE!. 4. Suffixed o-grade form *bhol-to- possibly in Germanic *balthaz, bold, in: a. Old English bald, beald, bold: BOLD; b. Old High German bald, bold: BAWD. 5. Suffixed o-grade form *bhol-n- in Latin follis, bellows, inflated ball: FOLLICLE, FOOL!; (FOLLICULITIS). 6. Possibly Greek phalaina, whale: BALEEN. 7. Conceivably (but more likely unrelated) Greek phellos, cork, cork oak: PHEL- LEM; PHELLODERM, PHELLOGEN. (The following deriva- tives of this root are entered separately: bhel-?, bhelgh-, bhlei-, bhleu-.) [Pok. 3. bhel- 120.} bhel-3, To thrive, bloom. Possibly from bhel-?. I. Suffixed o-grade form *bhol-yo-, leaf. 1. Latin folium, leaf: ForL?, FOLIAGE, FOLIO, FOLIUM; CINQUEFOIL, DEFOLIATE, EX- FOLIATE, FEUILLETON, FOLICOLOUS, MILFOIL, PORTFO- LIO, TREFOIL. 2. Greek phullon, leaf: (-PHYLL), PHYLLO-, -PHYLLOUS; GILLYFLOWER, PODOPHYLLIN. II. Extended form *bhlé- (< *bhlea-). 1. O-grade form *bhl6- in: a. suffixed form *bhlé-w- in Germanic *bl6-w- in Old English bléwan, to flower: BLOWS; b. Germanic suffixed form *bl6-m6n- in (i) Old Norse blém, blémi, flower, blossom: BLOOM! (ii) Old English bléma, a hammered ingot of iron (semantic development obscure): BLOOM?; c. Germanic suffixed form *bl6-s- in Old English bléstm, bléstma, flower, blossom: BLOssoM; d. Latin flés (stem flor-), flower: FERRET?, (FLORA), FLORA, (FLORAL), FLOR- IATED, FLORID, FLORIN, FLORIST, -FLOROUS, FLOSCULUS, FLOUR, FLOURISH, FLOWER; CAULIFLOWER, DEFLOWER, EFFLORESCE, ENFLEURAGE, FLORIGEN. 2. Germanic suf- fixed form *blé-do- in Medieval Latin bladium, produce of the land: EMBLEMENTS. 3. Suffixed zero-grade form *bhib-to- in Germanic *bladaz in Old English bled, leaf, blade: BLADE. [Pok. 4. bhel- 122.] bhel-4. To cry out, yell. Germanic *bell- in: a. Old English bellan, to bellow, bark, roar: BELL?; b. Old English belle, a bell: BELL!; c, Old English belgan, bylgan, to become enraged: BELLOW; d. perhaps Old English bealcan, *b(iJelcan, to utter, belch forth: BELCH; e. Middle High German buldern, boldern, to make noise: POLTERGEIST; f. Icelandic baula, to low, akin to the Scandinavian source of Middle English baulen, to howl: BAWL. [Pok. 6. bhel- 123.] bheld-. To knock, strike. Zero-grade form *bhid- in Germanic *bult-, missile, in Old English bolt, heavy arrow, bolt: BouT!. [Pok. bheld- 124.] bhelg-. Also bhelk-. A plank, beam. 1. Germanic *balku- in Old English balc(a), ridge: BALK. 2. Germanic *balk6n- in: a. Old French bauch, beam: DEBAUCH; b. Old Italian balcone, scaffold: BALCONY. 3. Suffixed zero-grade form *bhik-yo- in Latin fulcire, to prop up, support: FULCRUM. 4. Possibly Greek phalanx, beam, finger bone, line of battle: PHALANGE, PHALANX. [Pok. 5. bhel- 123.] bhelgh-. To swell. Extension of bhel-2. 1. Germanic *balgiz in Old English bel(ijg, belig, purse, bellows: BELLOWS, BELLY. 2. Germanic *bulgjan in Old Norse bylgja, a wave: BILLOW. 3. Germanic *bolgstraz in Old English bolster, cushion: BOLSTER. 4. Celtic *bolg- in Latin bulga, leather sack: BUDGET, BULGE. [Pok. bhelgh- 125.) bhelu-. To harm. Germanic *balwaz in Old English bealo, b(e)alu, harm, ruin, bale: BALE?. [Pok. bheleu- 125.] bhendh-. To bind. 1. Germanic *bindan in Old English bindan, to bind: BIND; WOODBINE. 2. O-grade form *bhondh- in Germanic *band- in: a. Old English bend, band, ribbon, akin to the Germanic source of Old French bende, band: BEND?; b. Old English bendan, to bend: BEND!; c. Old Norse band, band, fetter: BAND!, BOND; d. Old French bande, bond, tie, link: BAND!. 3. Zero-
455:ered-. High. Suffixed zero-grade form red-wo- in Latin arduus, high, steep: ARDUOUS. [Pok. er(e)d- 339.]
603:kel-2. To cover, conceal, save. I. O-grade form *kol-. 1. Germanic *haljé, the underworld (< ‘concealed place’), in: a. Old English ell, hell: HELL; b. Old Norse Hel, the underworld, goddess of death: HEL. 2. Germanic *halld, covered place, hall, ini a. Old English heal, hall: HALL; b. Old Norse Adil, hall: VALHALLA. 3. Suffixed form *kol-eyo- in Greek koleon, koleos, sheath: COLEUS; COLEOPTERA, COLEOPTERAN, COLEOPTILE, COLEORHIZA. II. Zero-grade form *k/-. 1.Germanic *hul- in: a. Old English Aulu, husk, pod (< “that which covers”): HULL; b. Old English hol, a hollow: HOLE; c. Old English holh, hole, hollow: HOLLOW; d. Old English healh, secret place,
621:hréc, rook: RooK!. 4. Germanic *hraban, *hrabnaz, raven, in Old English hrefn, raven: RAVEN}. 5. Extended form *krep- in Latin crepdre, to crack, burst, creak: CREPITATE, CREVICE; DECREPIT, DECREPITATE, QUEBRA- cHo. 6. Extended form *kri- in Germanic *krik- in Old French criquer, to creak, click: CRICKET!. II. Variant form *skr-. 1.Germanic *skrik- in Old English scric, thrush: SHRIKE. 2. Germanic *skrékjan- in Old Norse skrekja, to shriek: SCREAK, SCREECH. 3. Germanic *skrainjan, to shout, shriek, in Old Norse screma, to scream, perhaps akin to the possible Scandinavian source of Middle English scremen, to scream: SCREAM. III. O-grade form *kor-. 1. Latin corvus, raven: CORBEL, CORBINA, CORMORANT, CORVINE, Corvus. 2. Greek ko- rax, raven (> korakias, chough): CORACIIFORM, CORA- com. [Pok. 1. ker- 567.] ker-3. To grow. 1. Suffixed form *ker-es- in Latin Cerés, goddess of agriculture, especially the growth of grain: CEREAL, CERES. 2. Extended form *kré- (< *krea-) in: a. suffixed form *kré-yd- in Latin credre, to bring forth, create, produce (< “to cause to grow”): CREATE, CREOLE; PROCREATE; b. suffixed form *kré-sko- in Latin créscere, to grow, increase: CRESCENDO, CRESCENT, CREW!; AC- CRUE, CONCRESCENCE, CONCRETE, DECREASE, EXCRES- CENCE, INCREASE, RECRUIT. 3. Suffixed o-grade form *kor-wo-, “growing,” adolescent, in Greek kouros, koros, boy, son: DIOSCURI, HYPOCORISM. 4. Compound *sm-kéro-, “of one growth” (*sm-, same, one; see sem-'), in Latin sincérus, pure, clean: SINCERE. [Pok. 2. ker- 577.) ker-4, Heat, fire. 1. Suffixed form *ker-té in Germanic *herthé in Old English heorth, hearth: HEARTH. 2. Zero-grade form *kr- in: a. Latin carbé, charcoal, ember: CARBON, CARBUNCLE; b. extended form *krem- in Latin cremdre, to burn: CREMATE. 3. Possibly suffixed and extended form *kera-mo- in Greek keramos, potter’s clay, earthenware: CERAMIC. 4. Possibly variant ex- tended form *krds- in Russian krasa, beauty (< “bril- liance of fire”): CRASH?. [Pok. 3. ker(a)- 571.] ker-5. Also kere-. To injure. Suffixed zero-grade form *kro-yé- in Latin cariés, decay, caries: CARIES. [Pok. 4. her- 578.] ker-8. A kind of cherry. 1. Suffixed zero-grade form *kr-no- in Latin cornus, cornel tree: CORNEL. 2. Full- grade form *ker- probably in Greek kerasos, cherry: CHERRY. [Pok. 4. ker- 572.] kerd-', Heart. 1. Suffixed form *kerd-en- in Germanic *hertén- in Old English heorte, heart: HEART. 2. Zero-grade form *krd- in: a. Latin cor (stem cord-), heart: CORDATE, CORDIAL, COURAGE, QUARRY!; ACCORD, CONCORD, CORDIFORM, DISCORD, MISERICORD, RECORD; b. suffixed form *krd-yd- in Greek kardia, heart, stom- ach, orifice: CARDIA, CARDIAC, CARDIO-; DIPLOCARDIAC, ENDOCARDIUM, EPICARDIUM, MEGALOCARDIA, MYOCAR- DIUM, PERICARDIUM. 3. Possibly *kred-dha-, “‘to place trust” (an old religious term; *dho-, to do, place; see dhé-'), in Latin crédere, to believe: CREDENCE, CREDI- BLE, CREDIT, CREDO, CREDULOUS, GRANT; MISCREANT, RECREANT. [Pok. kered- 579.] kerd-2. Craft. Suffixed form *kerd-d in Old Irish cerd, art, artist: CAIRD. [Pok. 2. kerd- 579.] kerdh-. Row, herd. Suffixed form *kerdh-d@ in Germanic *herdo in Old English heord, herd: HERD. [Pok. kerdho- 579.] kere-. To mix, confuse, cook. 1. Variant form *kra- (< *kraa-) in Germanic *hrdr- in: a. possibly Old English hrér, lightly boiled, half-cooked: RARE?; b. Middle Dutch roer, motion: UPROAR. 2. Zero-grade form “krp- in: a. suffixed form *kro-ti- in Greek krasis, a mixing: IDIOSYNCRACY; b. suffixed form *kro-ter- in Greek kra- ter, mixing vessel: CRATER. [Pok. hero- 582.] kerp-. To gather, pluck, harvest. Variant karp-. 1. Ger- manic *harbistaz in Old English herfest, harvest: HAR- VEST. 2. Latin carpere, to pluck: CARPET; EXCERPT,
665:leg-'. To collect; with derivatives meaning “to speak.” 1. Perhaps Germanic */ékjaz, enchanter, one who speaks magic words, in Old English /éce, physician: LEECH). 2. Latin legere, to gather, choose, pluck, read: LECTERN, LECTION, LECTURE, LEGEND, LEGIBLE, LEGION, (LES- SON); (COIL!), COLLECT!, DILIGENT, ELECT, INTELLIGENT, NEGLECT, PRELECT, SACRILEGE, SELECT, SORTILEGE. 3. Greek legein, to gather, speak: LEXICON; ALEXIA, ANALECTS, BRADYLEXIA, CATALOGUE, DIALECT, (DIA- LOGUE), DYSLEXIA, ECLECTIC, EPILOGUE, PROLEGOM- ENON. 4. Suffixed form */eg-no- in Latin lignum, wood, firewood (< “that which is gathered”): LIGNEOUS, LIGNI-. 5. Lengthened-grade form */ég- possibly in: a. Latin léx, law (? < “collection of rules”): LEGAL, LEGIST, LEGITI- MATE, LEX, LOYAL; LEGISLATOR, PRIVILEGE; b. Latin denominative légdre, to depute, commission, charge (< “to engage by contract”; but possibly from legh-): LEGACY, LEGATE; ALLEGE, COLLEAGUE, (COLLEGIALITY), DELEGATE, RELEGATE. 6. Suffixed o-grade form *log-o- in Greek logos, speech, word, reason: LOGIC, LOGISTIC, LOGO-, LOGOS, -LOGY; ANALOGOUS, APOLOGUE, APOLOGY, DECALOGUE, HOMOLOGOUS, LOGARITHM, PARALOGISM, PROLOGUE, SYLLOGISM. [Pok. leg- 658.]
904:saus-. Dry. 1. Extended form *sauso- in Germanic *sau- saz in: a. Old English séar, withered: SEAR!, SERE!; b. Frankish *saur, dry, whence Old French saur, sor, red-brown: SORREL?; SURMULLET. 2. Suffixed form *saus-t- in Greek austéros, harsh: AUSTERE. [Pok. saus- 880.]
943:(s)keu-. To cover, conceal. Zero-grade form *(s)ku-. Variant *(s)keua-, zero-grade form *(s)kua-, contracted to *(s)kii-. 1. Suffixed basic form in Germanic *skeu-jam, cloud (“cloud cover’), in Old Norse sky, cloud: sky. 2. Zero-grade form *skd- in: a. suffixed form *ski-mo- in Germanic *skiimaz, foam, scum (< “that which covers the water’), in (i) Old High German sciim, scum (> German Schaum, foam): MEERSCHAUM (ii) Middle Dutch schiim, scum: SCUM; Db. suffixed form *ski-ro- in Latin obsciirus, “covered,” dark (ob-, away from; see epi): OBSCURE; CHIAROSCURO. 3. Zero-grade form *ku- in: a. suffixed form “ki-ti- in Germanic *hidiz in Old Eng- lish Ayd, skin, hide: HIDE?; b. suffixed form *ku-ti- in Latin cutis, skin: CUTANEOUS, CUTICLE, CUTIS; CUTIN; c. possibly suffixed form *kd-lo- in Latin cilus (> French cul), the rump, backside: CULET, CULOTTES; BASCULE, RECOIL; d. suffixed form *ku-to- in Greek kutos, a hollow, vessel: -cyTE, cyTo-. 4. Extended zero-grade form *kus- in: a. Germanic *huson- in Old English hosa, hose, covering for the leg: HOSE; b. suf- fixed form *kus-dho- (or suffixed extended form *kudh- to-) in Germanic *huzdam in Old English hord, stock, store, treasure (< “thing hidden away”): HOARD; c. Rus- sian kishka, gut (< “sheath”), akin to the Slavic source of Yiddish kishke, kishke: KISHKE. 5. Suffixed extended zero-grade form *kut-no- in Latin cunnus, vulva (< “sheath”): CUNNILINGUS. 6. Extended root *keudh- in: a. Germanic suffixed lengthened zero-grade form *hiid- Jan in Old English hydan, to hide, cover up: HIDE}; b. Germanic suffixed zero-grade form *hid-jdn- in French hutte, hut: HuT. [Pok. 2. (s)keu- 951.] skeubh-. To shove. 1. Germanic *skeuban and derivative lengthened zero-grade form *skdban in: a. Old English sciifan, to shove: SHOVE; b. Old Norse skifa, to push, perhaps akin to the probable Scandinavian scource of SCUFF, SCUFFLE!, 2. Germanic suffixed form *skub-ilé- in: a. Old English scofl, a shovel: SHOVEL; b. Middle Dutch schoffel, schuffel, a shovel, hoe: SCUFFLE?. 3. Ger- manic *skub-, *skuf-, *skup- in: a. Danish skof, jest, teasing, probably akin to the Scandinavian source of Middle English scof, mocking: scoFF; b. possibly (but quite doubtfully) Old English scop, poet (< “jester’): scoP; c. Low German schiiffeln, to walk clumsily, shuffle cards, probably akin to the source of SHUFFLE. [Pok. skeub- 955.] skeud-. To shoot, chase, throw. 1. Germanic *skeutan, to shoot, in: a. Old English scéotan, to shoot: SHOOT; b. Old Norse skj6ta, to shoot: SKEET. 2. Germanic *skutaz, shooting, shot, in: a. Old English sceot, scot, shooting, a shot: sHOT!; b. Old High German scuz, shooting, a shot: scHuss; C. Old Norse skot and Old French escot, contri- bution, tax (< “money thrown down”): SCOT, (SCOT AND Lot). 3. Germanic *skutjan probably in Old English scyttan, to shut (by pushing a crossbar): sHUT. 4. Ger- manic *skutilaz in Old English scytel, a dart, missile: SHUTTLE. 5. Germanic *skautj6n- in: a. Old English scéata, corner of a sail: SHEET?; b. Old English scéte, piece of cloth: SHEET!. 6. Germanic *skut- in Old Norse skita, mockery (< “shooting of words”), akin to the Scandinavian source of scouT*. 7. Germanic “skaut-, perhaps in Old French escoutille, hatchway: SCUTTLE}, [Pok. 2. (s)keud- 956.] skeup-. Cluster, tuft, hair of the head. 1. Germanic *skauf- in Old English scéaf, bundle, sheaf: SHEAF. 2. Possibly Germanic *hupp- in Middle Dutch hoppe, the hop plant (having tuftlike inflorescence): HoP?. [Pok. (s)keup- 956.]
983:spréot, pole (< “sprout, stem”): sPRIT; d. Middle English bouspret, bowsprit: BOwsPRIT. 3. Extended form *spreit- in Germanic *spraidjan in Old English sprédan, to spread: SPREAD. II. Basic form *sper-. 1. Suffixed form *sper-yo- in Greek speirein, to scatter: Diaspora. 2. Suf- fixed form *sper-mn in Greek sperma, sperm, seed (< “that which is scattered”): SPERM}. III. O-grade form *spor-. 1. Suffixed form *spor-d- in Greek spora, a sowing, seed: SPORE, SPORO-. 2. Suffixed form *spor-nd- in Greek sporas (stem sporad-), scattered, dispersed: SPORADIC. [Pok. 2. (s)p(hJer- 993.]
992:(s)preg-. To jerk, scatter. 1. Germanic *sprek-, *frek- in: a. Middle Dutch sprenkelen, to sprinkle, akin to the possible source of Middle English sprenklen, to sprinkle: SPRINKLE; b. Old Norse freknur, freckles (< “that which is scattered on the skin”): FRECKLE; C. Swedish dialectal spragg, twig (< “that which is jerked off a branch”), akin to the Scandinavian source of sPpRAG; d. Swedish dialec- tal sprygg, brisk, active, akin to the Scandinavian source of sPRY. 2. Zero-grade form *sprg- in variant *sparg- in Latin spargere, to strew, scatter: SPARGE, SPARSE, SPURRY; ASPERSE, DISPERSE, INTERSPERSE. [Pok. (s)p(h)ereg- 996.]
```


## [2026-09-05T20:35:43.607Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== LKT 3235-3248 ===\"; sed -n '3235,3248p' LKT.txt\necho \"=== LKT 1663-1670 ===\"; sed -n '1663,1670p' LKT.txt\necho \"=== AHD werdh ===\"; grep -n \"werdh\\|wredh\" AHD_watkins1985.txt | head -5"
}
```


### [2026-09-05T20:35:43.677Z] TOOL RESULT

```
=== LKT 3235-3248 ===
1401.  Ar.  manzil: 'Ab.-teigequartier,  Wirtshaus'  [vom  Vb. nazala  'absteigen'  und  Präfix  ma-  des Ortes],  tk.  ebenso  memil;  hieraus  rum. inizil,  inezil,  nienzil  'Poststation',  serb. niezil  Tost'.  [Löbel  EITAP  64.  Mikl SJEtWb  94.
140^.  Hebr.  uiä'ös: 'Verächtliches,  Gebrechen,  Fehler', rihebr.  mpis  Sviderhch,  widerwärtig, veräciitlich' ;  hieraus  jüd.-dtsch.  mies, Vb.  vermiesen,  Miesmacher  'Flaumacher', [mit  der  slav.  Endung  -nik\  Mießnik 'fauler Kopf. [ Ave-L I V,  574.  MWil)  47/48.
1403.  Ar.  inar'a:
[S.  hier  Nr.  169c,  dazu  präfigiertes  ma des  Ortes  wie  z.  B.  hier  Nr.  1401] 'Weide',  ebenso  tk.  mera;  hieraus  rum. miiiRfe  'Stoppelfeld'
1404.  Ar.  itiarad:
'Kiankheit',  ebenso  tk.  maraz;  hieraus rum.  maraz  'geistige  oder  seelische  Ver- stimmung oder  Krankheit' ;  serb.  maraz 'Krankheit'.
1405.  Ar.  maräkk:
Plr.  'die  zarten  und  empfindlichen  Teile des  Leibes';  hieraus  pjj.  mirac  'Bauch, Leib'.  [DE  314.  Eguilaz  453.  Constan- cio  Dicc  696  a.
1406.  Ar.  Maräkiis:
Jetzt  Marrähes,  die  frühere  südliche Hauptstadt  Marokkos;  hiernach  wird  das Ziegenleder  genannt,  das  in  Marokko hergestellt  und  jetzt  in  Europa  imitiert wird:  pg.  marroquim  [Gonstancio  Dicc 679  c],  frz.  maroquin,  ndl.  marohijn, dtsch.  Maroquin;  engl,  morocco  'feines dünnes  marokkanisches  Leder'.  —  [Frz. maroquin  'Tau,  welches  vom  Topp  des Fockmastes  zum  Topp  des  grofsen  Mastes geht  und  dazu  dient,  eine  Ladetakel daranzuhängen,  um  vermittelst  der- selben Güter  aus-  und  einzuladen',  also dtsch.  'Toppreep',  fi'z.  surpente,  ist  wohl mit  ndl.  marren  'festbinden'  in  Zusam- menhang zu  bringen,  vgl.  Behrens  ßeitr. 373/374].
1407.  Ar.  maraninia: 'Ausbesserung',    tk.   meremet;  hieraus rum.   meremet  'dass',    Vb.  meremetisi 'ausbessern'.
1408.  Ar.  niaras:
'Schnur';  hieraus  [mit  häufigem  Wechsel von  m  und  b]  pg.  kat.  barago  'Schnur', pg.  barafa,  baraza  'Strick  an  der Schlinge,  mit  der  man  wilde  Tiere fängt'.    [DE  236.   Eguilaz  3-^9.
1409.  Ar.  innrassi:
=== LKT 1663-1670 ===
'Steuer' ;  hieraus  sp.  pg.  garrama  'Steuer, Abgabe,  Raub,  Erpressung'.  [DE  275. Eguilaz  410.    ML  3680.
672.  Ar.  garas:
'Glocke,  Klingel';  hieraus  mit  ar.  Art. sp.  aljaraz.  (dial.)  nljarges,  aljorses. [DE  145.    Eguilaz  203.    ML  3943  a.
673.  Ar.  garbäl:
Klassisch-ar.  girbäl  'Sieh'  [dem  lat.  cri- öeZZtw  merkwürdig  ähnlich] ;  hieraus  siz. garhula  'Sieb,  Kasten  der  Trommel',  it. garhellare  'durchsieben'  (z.  B.  die  klein- sten Stücke  einer  Droge),  gavhellatura 'die  kleineren  Stücke  einer  Ware,  die durch  das  Sieb  hindurchfallen',  ebenso frz.  grabeler,  graheaii,  sp.  garhillo  'Sieb'. —  Aus  mit  Imäla  gesprochenem  garbel ergab  sich  sp.  arel  'großes  Sieb'. [GrSVociSic  238.  DE  188.  198.  274. Devic  DEt  132.    ZtVlWf  XI,  9/10.
674.  Ar.  garbi:
'Westlich';  hieraus  il.garbino,  frz. garbin 'Südwestwind'  auf  dem  Mittelmeere, prov.  garbin,  sp.  garbino  'Süd-  oder Westwind',  sp.  pg.  algarve  'fruchtbar', pg.  garabia  'Westen'.  Aus  dem  It. wurde  serb.  garbin  'Südwind'.  Jeden- falls mit  Kontamination  von  al-  arabija 'die  arabische  Sprache'  entstand  pg.  al- garabia,  pg.  algravia,  frz.  charabia  'un- verständliches Zeug,  Kauderwelsch',  frz. insbesondere  'Dialekt  der  Auvergne'.  — Aus  demselben  Stamme  ar.  garaba 'untergehen  (Sonne)'  ist  mit  präfigiertem ma-  zur  Angabe  des  Ortes  magrib  ge- bildet; der  Magreb  ist  Nordwestafrika von  Tunis  bis  Marokko;  ms  al-magribl 'der  Bewohner  des  M.'  wurde  irz. maugrebin  'dass.'.  —  Auch  der  Name der  pg.  Provinz  Algarve  ist  ar.  garb 'Westen',  daher  sp.  algarabio,  algarabia, pg.  algaravio  'Bewohner  von  Algarve'. [DE  119.  241.  Eguilaz  178.  Devic  DEt 125.    ML  3683.    Bern  SlEtWb  295.
675.  Pers.  gärdän:
=== AHD werdh ===
1176:wrédh-. To grow straight, upright. Suffixed zero-grade form *wrodh-wo- in Greek orthos, straight, correct, right: ORTHO-, ORTHOTICS; ANORTHITE. [In Pok. werdh- 1167.]
```


## [2026-09-05T20:35:55.056Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nfor ln in (13836,26616,22517,24423):\n    pre='\\n'.join(lines[:ln]); leaf=pre.count('\\f')\n    print(ln,'leaf',leaf,'-> printed pages approx',2*leaf-?? if False else (leaf,))\nEOF\ngrep -n \"page_offset\" -A2 /dev/null; python3 -c \"\nimport json;d=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'));print(d['KLN']['page_offset']);print(d['KLN'].get('lookup_hint'))\""
}
```


### [2026-09-05T20:35:56.794Z] TOOL RESULT

```
  File "<stdin>", line 5
    print(ln,'leaf',leaf,'-> printed pages approx',2*leaf-?? if False else (leaf,))
                                                          ^
SyntaxError: invalid syntax
KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.
```


## [2026-09-05T20:36:00.525Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nfor ln,label in ((13836,'Europe'),(26616,'ortho-'),(22517,'Maghrib'),(24423,'morocco'),(22427,'maarib'),(13523,'Erebus')):\n    pre='\\n'.join(lines[:ln]); leaf=pre.count('\\f')\n    print(label, 'leaf', leaf, '-> printed ~', (leaf-12)*2, 'or', (leaf-12)*2+1)\nEOF"
}
```


### [2026-09-05T20:36:02.409Z] TOOL RESULT

```
Europe leaf 299 -> printed ~ 574 or 575
ortho- leaf 587 -> printed ~ 1150 or 1151
Maghrib leaf 495 -> printed ~ 966 or 967
morocco leaf 538 -> printed ~ 1052 or 1053
maarib leaf 493 -> printed ~ 962 or 963
Erebus leaf 292 -> printed ~ 560 or 561
```


## [2026-09-05T20:36:18.553Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor n in 287 288 299 300; do echo \"--- leaf $n ---\"; awk -v N=$n 'BEGIN{RS=\"\\f\"} NR==N+1' KLN_1966.txt | head -4 | cut -c1-160; done\necho \"=== leaf 587/588 (ortho) ===\"; for n in 560 561 587; do echo \"--- leaf $n ---\"; awk -v N=$n 'BEGIN{RS=\"\\f\"} NR==N+1' KLN_1966.txt | head -3 | cut -c1-120; done"
}
```


### [2026-09-05T20:36:20.372Z] TOOL RESULT

```
--- leaf 287 ---
nter-.  —  Fr.  F.  entre, ‘between,  among’,  fr.  L.  inter,  of  s.m.  See  ist enter-.
entreat,  tr.  and  intr.  v.  —  ME.  entreten,  fr.  OF. entraiter,  ‘to  treat’,  fr.  ist  en-  and  trailer,  ‘to treat’.  See  treat.
Derivatives :  entreat- ing,  adj.,  entreat-ing-ly,  adv. entreaty,  n.  —  Formed  fr.  entreat  on  analogy  of treaty.
entree,  entree,  n.,  1)  entrance,  right  to  enter; 2)  a  course  of  meal.  —  F.  entree.  See  entry, entremets,  n.,  side  dish,  extra  dish.  — 
--- leaf 288 ---
  and  £v8iisiv,  ‘to  put  on (clothes)’  (whence  6v8up.a,  ‘garment’);  see  en- dysis.  Considering  the  fact  that  this  membrane consists  of  
Derivative:  ependym-al,  adj. ependymitis,  n.,  inflammation  of  the  ependyma (med.)  —  Medical  L.,  formed  fr.  prec.  word with  suff.  -itis.
ependymoma,  n.,  diseased  condition  of  the  epen¬ dyma  (med.)  —  Medical  L.,  formed  fr.  epen¬ dyma  with  suff.  -oma.
epenthesis,  n.,  insertion  of  a  letter  or  a  syllable in  a  word  ( gramm .)  —  Late  L.,  fr.  Gk.  tnbv- beou;,  ‘insertion’,  fr.  invrn&txai, 
--- leaf 299 ---
in  and  cp.  words  there  referred  to.  For  the ending  see  suff.  -ia.
eupeptic,  adj.,  having  good  digestion;  promoting digestion.  —  Formed  with  suff.  -ic  fr.  Gk. ecmemoi;.  See  prec.  word  and  cp.  peptic  and wor
Euphemia,  fem.  PN.  —  L.,  fr.  Gk.  Eu<pr,pix,  lit. ‘speech  of  good  omen,  good  repute’,  fr.  eu  (see eu-)and  ipif)pir),  ‘prophetic  saying
euphemism,  n.,  substitution  of  a  mild  word  or  ex¬ pression  for  a  harsh  or  vulgar  one  (rhet.)  — Gk.  e6<f>T)pu<j[i6i;,  ‘use  of  an  auspic
--- leaf 300 ---
idnem,  acc.  of  evacuatio,  ‘an  evacuating’,  fr. L.  evacuatus,  pp.  of  evacuare.  See  prec.  word and  -ion.
evade,  tr.  v.,  to  avoid.  —  L.  evadere,  ‘to  go  out; to  escape’,  fr.  e-  and  vddere,  ‘to  go’,  which  is rel.  to  vadum,  ‘a  shallow
Evadne,  1)  the  wife  of  Capaneus,  one  of  ‘the Seven  before  Thebes’  (Greek  mythol)-,  2)  fern. PN.  —  L.,  fr.  Gk.  EuaSwj,  a  word  of  unc
evaginate,  tr.  v.,  to  turn  (a  tube)  inside  out.  — L.  evaginatus,  pp.  of  evaginare,  ‘to  unsheathe’, fr.  e-  and  vagina,  ‘sheath’.  Se
=== leaf 587/588 (ortho) ===
--- leaf 560 ---
s  (in  a  certain  manner); one  who  deals  (with  a  certain  topic)’.  See  nidus and  -logy.  The  correct  form 
nidorous,  adj.,  smelling  like  something  burning (rare).  —  Late  L.  nidorosus,  ‘steaming’,  fr.  L. nidor.
nidus,  n.,  a  nest;  a  breeding  place;  a  place  where germs  of  disease  are  developed.  —  L.  nidus, ‘nest
--- leaf 561 ---
�.
Nilotic,  adj.,  pertaining  to  the  Nile,  the  Nile  re¬ gion  or  the  Negroes  who  live  in  the  valley  of  the
nim,  tr.  and  intr.  v.,  to  take;  to  steal  {archaic)  — OE.  niman,  ‘to  take’,  fr.  I.-E.  base  •nem-
--- leaf 587 ---
�orris  root’,  which  is  identical  with  Gk. Epecoe,  gen.  of  Iptc,  ‘iris’.  See  iris.
Orson,  masc.  PN.  —  Fr.  F.  ourson,  dimin.  of  ours, ‘bear’,  fr.  L.  ursus  (see  Ursus).  The  spelling O
Ortalidae,  n.  pi.,  a  family  of  Diptera  (entomol.) —  ModL.,  formed  with  suff.  -idae  fr.  Gk.  op- ■zolaI
```


## [2026-09-05T20:36:36.421Z] TOOL CALL #53: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A8%D8%A7%D9%84%DB%8C%D8%AF%D9%86",
 "prompt": "Give the Persian etymology of بالیدن (bālīdan) verbatim: Middle Persian form, Proto-Iranian root, PIE root, cognates (Avestan, Sanskrit), and any mention of Old Persian or *ward-."
}
```


## [2026-09-05T20:36:38.199Z] TOOL CALL #54: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%88%D8%A7%D9%84%D8%A7",
 "prompt": "Give the Persian etymology of والا (vālā) verbatim: what Middle Persian / Proto-Iranian form is it derived from, is it linked to bālīdan / *ward- \"to grow\" or to *bard- \"high\" (Avestan barəz-)? Also note any doublet relationship with بالا."
}
```


### [2026-09-05T20:36:38.436Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-05T20:36:43.788Z] TOOL RESULT

```
# Persian Etymology of والا (vālā)

According to the Wiktionary entry, the second etymology derives from Middle Persian **wʾl-ytn' (wāl-īdan, "to grow, to prosper")**, which connects to the modern verb بالیدن (bâlidan, "to grow, to brag").

The entry explicitly states: **"Doublet of بالا (bâlâ), derived with the same suffix from a different form of the same verb."**

So both والا and بالا stem from the same Middle Persian verbal root but employ different suffix formations. The etymology links the word to concepts of growth and prosperity rather than to a separate "high/exalted" root. The modern adjective meaning "high, exalted, great, eminent" appears to be a semantic development from this growth/elevation sense.
```


## [2026-09-05T20:36:49.210Z] TOOL CALL #55: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/بالیدن",
 "prompt": "Give the Persian etymology of بالیدن (bālīdan) verbatim: Middle Persian form, Proto-Iranian root, PIE root, cognates (Avestan varəd-, Sanskrit vardhati), and mention of the initial w->b change."
}
```


### [2026-09-05T20:36:51.047Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-05T20:36:51.654Z] TOOL CALL #56: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%E1%BD%80%CF%81%CE%B8%CF%8C%CF%82",
 "prompt": "Give the etymology of Ancient Greek ὀρθός verbatim: which PIE root (*h₃erdʰwós / *wrodʰwos?), cognates (Sanskrit ūrdhvá-, Avestan ərəduua-, Latin arduus), and any mention of Doric βορθός / initial digamma."
}
```


### [2026-09-05T20:36:56.862Z] TOOL RESULT

```
# Etymology of Ancient Greek ὀρθός

## PIE Root
The documented PIE root is **\*h₃r̥dʰwós**, derived from **\*h₃erdʰ-** meaning "upright."

## Cognates
According to the source, cognate languages include:
- **Latin**: "arduus"
- **Sanskrit**: "ūrdhvá"

The article does not mention Avestan ərəduua- or any Doric variant (βορθός) with initial digamma.

## Proto-Hellenic Ancestor
The word descends from "Proto-Hellenic *ortʰwós," which developed from the PIE root noted above.

## Mycenaean Connection
The source notes a possible relationship to Mycenaean Greek 𐀃𐁍𐀸𐀃 (o-two-we-o), though this connection remains uncertain rather than definitive.
```


## [2026-09-05T20:37:11.605Z] TOOL CALL #57: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A8%D8%A7%D9%84%DB%8C%D8%AF%D9%86#Persian",
 "prompt": "Give the Persian etymology of بالیدن (bālīdan, to grow) verbatim: Middle Persian wālīdan, Proto-Iranian *Hwardaya-, PIE *h1werdh-, cognates."
}
```


### [2026-09-05T20:37:13.700Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-05T20:37:14.886Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT arədva variants ===\"; grep -n \"ar»dva\\|ar»Sva\\|ardSva\\|ar>dva\\|aroSva\\|arddva\" BRT.txt | head -20\necho \"=== BRT vartd / var»d ===\"; grep -n \"vari>d\\|var»d-\\|vardaiti\\|vartd\" BRT.txt | head -10\necho \"=== BRT 'wachsen machen' ===\"; grep -n \"wachsen\" BRT.txt | head -20"
}
```


### [2026-09-05T20:37:14.968Z] TOOL RESULT

```
=== BRT arədva variants ===
6486:•  j.  aäti.masah-  Adj.  'von  der  Grösse einer  A.':  äat  pitSus  ydi:a  cdijiciärS  'sS N.  (7^(?);  —  taltim  dauru  . . nyäzaym  (sd.) +°jj')  xraoidvaAe  bti'  altavatö  var>dvahe "ein  .  .  Stück  Holz  .  .  von  der  Grösse" einer  Ä.  aus  hartem,  doppelt  so  gross'' aus  weichem"  V.  13. 30.
7661:*ar»dvaya
=== BRT vartd / var»d ===
7410:•  g.  a-radah-  Adj.  'der  etwas  bereit  macht,  |  k»hrp3m  utayoUis  dadat  -tU  atmä  (sd.)  V. zu  Stande  bringt',  mitAkLij-J  vi  titq'irs  :jo.T,43.6;~..ahur?myaliiy5 xsa^nmcä sravim  -d.i  (NS.)  "dass  euer  Prophet  ■  '^ayiSMvamrum  (sd.)  vartdaitt  'Hs  V.  2^. (auditum  perficiens  sil  sva.)  sich  Gehör  3;  _  ntmlhaxs  *'iil  mainya  *pfnsaiu verschaffe"  Y.2Ä7'>.  \ya^ra  ma^^a  (sd.)  Y.31.13;  —  vankius
18130:asaone  V.  2J.  i.  a)  bes.  mit  Beziehung a.\^gai%ä-  gebraucht'':  aAam  (Sp,  107  m.) dadäl  ahurö  ahmäi  gatisi  vohB  frädat manavha  ^.46- 13;  —  damam  . .  yä  mit gat^i  asa  fradöit  ha^mnä  (sA.)  Y. 44.10; —  vaM  manaivha yehyä  syao%anilis gaU'^S aia  frädfntl  (als  Pass.)  "mit  VAf.,  durch des  Tätigkeit  Haus  und  Hof  von  Asa  ge- fördert werden"  Y.4J.6;  —  Jat  ml ga^^t'r /rO^aya . .  var^aya  V.  2. 4 ; — az»m  tl  gaf^a Jrälayfni ..  vari^ayeai  V.  2.  5.  2)  Med. 'wachsen,  gedeihen':  haoma  raose  gara paiti  Uta  /rä^aS^a  vifpaiia  Y. /o.  4;  — neben  vartd-'.frainmnahe^  vanifmna/ie xrahwsmtiahe  suyamnaAe  V.4-2  Gl.
22877:Yt  19. 9;  4S;  ->«i  *"«« ■  ■  w^A  v^»Ä»,«/a  ,  .      var»d- V.'augere'.  Praes.  2  v^r^da-,
22905:•  j.  varaSant-  (,  vartdani-)  Adj.,  PPA.:
=== BRT 'wachsen machen' ===
2514:-  g.  'a-  Pron,  ident.  'ich,  du,  er  selbst',  humata  'ta'  ..  aat  mam  narö  paskat  ya- nur  NS. :  yi  maibya  yaos  (sd.)  akmai  astu  g3„ie . .  "um  dieses  (deines)  guten  Denkens vakUta  mahyä  isfois  voha  eöihm  mananM  willen  .  ."  H.2.14''.        2)  substantivisch: ".  .  dem  verspreche   auch  ich  selber  das  ,  ^tai  ti  .  .  avayam  *danmaM  Y.  öS.  i  '>;  — beste  meines  Besitzes  durch  VM."  y.4''-   am  yasna  .  .  ''ta  patti    ava.jasa  .  .  aoi \Z;    —    ai   -3    vaocal  ahurö  mazda    ''da  zam  ".  .    um    dessentwülen  (was  hier  ge- sprach er  selbst,  ^/iM."  Y.sp.ö.  [schiebt)    komm  . ."  Yt. 5.132  (s.  i);   — zBed._s.  Gdn.  GIrPh.   '  52      Ich   '^'^^<=^'^^'- -faimat puir.lt  (sUtt  AS.)  Kimar^xsaf^u/ia dass  f.  as'  aus  einerrart.  idg.  'n  'selber  er-    ,    ,  ,   ,.,       .,•.,..'        ,     .  ,        „ wachsen  ist,  die  in  aUi;  (aus  'a-u-r,  wie , (sd-)    damit  (was  ich  dir  gebe)  such  ..' eJroiaus*jn-H-/°)steckl.Dochs.B(;M,GrGr.3244-    V.  1^.  14;  —  in  Kongruenz  mit  dem  Prae-
3038:•  j.  'a-karäta-  Adj.  'nicht  ausgesät'  sva..  \ syaaina  V.j.zi';  i.  ii,  12,  16;  —  'ya 'nicht  durch  Aussaat  gewonnen,  wild  ge-ljrätava  V.i.i^;  F. 7;  —  °y?mäi  vimanö.- wtLchstn':  j'ovanam  ..  aetavat  karstanam' AJtn  V.J.  7;  15;  —  'yanqm  ma^ranqm altavat  °tanam  "Getreide  ..  so  viel  vom  Vt.  10.  20;  —  -yqm  ifaaiirim  (sd.)  YL gesäten,  soviel  vom  wildgewachsenen"  V.   z^.  57;  V.  j().45;  —  'ya  danta  läsyä^  (sd.)
3479:langen zu  — ,  teilhaftig  werden',  mit  Al;k. : voAa  xsa^nm  toi  mazdJ ..  apaimä  vTspai yai'l  Y.41.2^'';  — yaiU  .  .  apan5  äangS.- Jyäinm  ä  xia^rnn  . .  Y.^.s  (s.  bei  ä)*i; —  yaha  aam  avat  3^ar»nS  apayemi  Yt. 5.43.  3)  'treffen', vom Geschoss:  yatUt (aHHf)  tanüm  apaynli\X.io.2\.  4)'(ei- nem  Gebot  usw.)  nachkommen',  sva.  'es erfüllen,  befolgen':  abmaoyahe  .  .  aiiihn äainay&  mas  (sd.)  vaca  da'isanakt  mit iyaohnäis  apayantaAei^  "der  die  Worte . .,  aber  in  seinem  Handeln  nicht  befolgt" Y.p-3i.  s)'(^'°^"i  Gegner,  Akk.)gleich- kommen,  sich  gewachsen  zeigen,  bemei- stem':  äal  mqm  aivs  zaraiustrS  anusm- hm  apayeiti  Yt.77. 19.  6)  '(einem  Ge- räusch usw.  mit  derStimme)  gleichkommen, es  gleichtun  können'  (ohne  Obj.) :  yS  gä'^ä srävayeiü  aps  v3  faiti^-sfatne  (sd.) . .  ye%i .  .  fisit  M>asibya  usibya  aiwisurunvaiU apayät  yezi  apffis(sd.)  ..  "..  wenn  er  (den Vortrag)  mit  seinen  eigenen  Ohren  nicht hören  kann,  soll  er  es  (dem  Geräusch) gleichzutun  versuchen  .  ."  N.  2Ö*'.
4009:'nicht  hervorwachsend,  spricssend'. Pflanzen:  urvaranqm  . .  yä  para  ahmat histfitta  .  .  ^'yäntis  (NPf.)  hamaya  gätvS Yt.7J.SS-
4935:Pii.  (inS.  /):  äiin  vitüjt,  (lu  Vr.):  ayächutS). —  >)  Aus  der  sjmlakt.  Verb,  ayä  xhisUm  (sd.) erwachsen;  s.  zu  i^uK^mazdäh:  Man  er- wartete ayöjcs'.  Wie  man  zur  Schreibung ayaoxi'  (Yt.  //;  s.  auch  Var.  zu  S-,  Vr.  und Yt.  3.  2,  7)  kam,  verstehe  ich  nicht.  —  ')  S. iiilay-*^.  —  SI  GelW. ;  s.  auch  jj.  ayuxsusl  'Me- tair, ZDMG.  36.  61.
5128:Aus  der  sjnt.  Fügung  01-11«  g1>:is  (oder  ähtil,) erwachsen,  d.i. 'Hilfe  des  Rinds'');  vgl.räiiarj.- ra-ffn/i:  Die  Schaffung  des  Namens  geht  von Y.  SQ.  Itc  aus,  s.  unter  avat:  —  ')  Justis Deutung  NB.  53  halte  ich  für  unmöglich.
6271:—  '/äum  spitama  Yt.5.89,  91,  72.2,  77. 21.  aa)  auch  kät'  i^.  (ohne  Nennung des  Namens,  s.  i  a  a):  paiti  dim  psr»sat 'hva  asäum  afiura  masda  .  .  äat  mraot ahurS  mazdä  axtm  bä  tl  tat  fratnraväni ,  .  asäum  spitama  Yt  72.  i  f.  ß)  Sing. koU.  sva.  die  gläubige  Gemeinde  im  Gegen- satz zum  amtirenden  Zaotar^^:  ya^ä  ahU vairyS  saota  (sd.)  fra  ml  mrüti  .  .  a^ä ratus  .  .  fra  °lava  vütva  mraotu  Y.j. 25.  f)  GP-  mit  fravasay-  (sd.,  auch fdSt):  'laonqm  {'launqm)  JravalayS  Y. 2.6,  Yt  7^.1,  usw.  0)  insbes.  mit  nar-'>> m.  und  näirl-'^^,  näirikä-'>'>  t  'der,  die Gläubige',  von  den  erwachsenen  Mitglie- dern der  zara^ustnscAitn  Religionsgemein- schaft; Sing,  und  Plur.:  narsm  'savatum ys  anhat .  .  mqhr^m  p}r>sS  'sava  V.5.2;
6893:KompA. ;  Ableif .  (s.  ^äh,',irya.\  -  Das  Wort J  gehört  etym.  mit 'a^J'- lusammen,  aus  dem  es 3*11.  in  Anschluss  an  'aAura-  erwachsen  ist.  —
7738:•  j.  «rszvant-  Adj,  (fem.  'vaiti-)  'gerad- gewachsen, stramm':  kainind  k;>hrpa  srJraya .  .  uskäi  yäslaya  'vai>yB  (GSf.)  Yt.  5. 64.
8173:•  j.  uxsne  Inf.  'wachsen  zu  lassen,  zu mehren';  w  xrdhwe'^  vJdrvänahe  asilt "um  die  Weisheit  des  zu  mehren,  der  am Asa  festhäir  V.  ^45;  45.
8177:'das  heilige  Recht  wachsen  lassend,  mehrend'.
8180:Eig. 'die  Verehrung  wachsen  lassend,  mehrend'.
8182:•  j,  uxsyat-urvarä-  Adj.  (mask.  •ra-')  'bei dem,  durch  den  die  Pflanzen  wachsen': salavalsS  .  .  "rö  Yt.  /^-44;  43;  —  mC^nrn .  .  °r?m  Yt.io.6i;  —  xh'iua  äzüitt  .  . tacat.,ipa  'ra  (ADm.)  Y./6.8.
8333:SoperL  zum  V.  iraod- 1).  —  ai.  vgl.  uparodAa- m.,  ufaeoäAin-  Adj,  —  D  Nach  Sp.  'der  auf- gewachsenste',  Dst.  'tshi  baut  de  taille'  viel- mehr mm  V.  'raad:
8471:'  'um  "ranqm  uzuxfyenlinam  srlranqm zairi^aoiianqm  vaxsA  (sd.)  apayasaite  V. /Ä63;  Yt. /Ä6;  —  at  aRyäi  (näml.  dem Rind)  mazdä.  'rä  vaxiaj  (sd.)  Y.4S.6;  — avi  racynyq/H  varauhmt  azuitlmca  'ranam Yt.  ^2.3;  —  nima  'vaire  (VS.)  varMhi masdaöäte  asaone'V.  ig.ii;  Vyt.22,  N.7/, f)7.  a)  Plut.,  im  Gegens.  zu  alxa-  Plur., 'pflanzenbewachsener Boden';  ahond  una 'rlhuca  paiti  *baooisca  vTdtnanmnS  saoa- yäti  . .  ärvatS  urva  *aexahuea  (sd.) . .  "der Seele  des  Gläubigen  ist  es  so,  als  ob  sie auf  Wiesengiund  (stehe)  und  Wohlgerüche empfinde,  .."H.  2. 7— 25.  b)  sva, 'Baum', a)  im  Gegens.  zu  var^ä-.  pairi  van>'>iJ- byasca  'räbyas^a  atsmaiibyS  (sd.)  V.  16. s.  ß)  sonst:  v3r»ynahe  . .  yS  .  .  sainif marisat  'ranqm  ". .  der ..  im  Flug  der  Bäume Wipfel  streift'"  Yt./.4.2i''.  c)  'Pflanzen- Stengel,  Reis':  yavat  akmUi  paitinqm •ranqm  aetavat . .  "so  viel  es  ihm  einzelne Reiser  gibt,  (als  ob)  er  so  viel  .  ."  V.  iV. 86,  a)  bes.    der   zum  Barisman    ge-
11326:•  j.,  g.  'äiSra-  (,  p.eßi''a-)  n.  i)  'Same', im  eig.  Sinn  (nur  Komp.).  2)  'Urspmng, Herkunft,  Abstammung':  *JhiaJi^ra  .  . Ajiiii  iristanqm  un'qitH?  .  .  spmtäl  haca mainyaot . .  aisqm  'rsm  FrW,  10.  39  f.;  Yt. 8.  4;  —  kainlnS  . .  pritiiaikyS  ratvat  "/vm  '* äzätayh  "eines  Mädchens,  . .  eines  gerad- gewachsenen —  reich  die  Herkunft  —  eines adeligen"  YL5,  64;  —  mmS  huci^r>m  .  . yetihl  n>manhg  °r>m  kumatimcä  . .  Y.  5Ä  ]
12101:ai.  tdruffa-  Adj. ;  np.  vgl.  lar.  —  Wegen  np. eh  'jniiEer  Hund'  s.  IFAni.  10.  22.  —-  Pü.! faranai,  Sfi.:  JiSuA.  —  >)  ifiä  'no  bezeichnet nach  meiner  Ansicht  den  un ausgewachsenen Hund  jeder  beliebigen  Basse  (vgl.  V.  /j.  10  fT.), '. der  eben  wegen  seiner  Jugend  noch  nicht  in  1 bestimmter  Richtung  Tervrendet  werden  kann.  | DST.  ZA.  3.  197  meint  mit  Andern,  ea  sei  . der  Jagdhund  darunter  lu  verliehen,  vgl, draxlB-kunara-,  s.  aber  die  Riv.- Stelle  bei  Sp. Ober*.  2.  :uxui  No.  z ,  wo  fürüi  (für  mp.  I laranak;  s.  V.  /j.  27]  gleich  baia  gesetzt wird.     Bd.  14.  19  hat  larSi  in  Aw.-Buchat.
15656:•  j.  paouru.fraväxS-  Adj.  (auch  fem.) 'an  mehreren,  verschiedenen  Stengeln  ge- wachsen' :  urvaram  . .  '^hamS.vanlajim  (sd) 'Am  (ASQÜ.qS;  —  paoiris*-iS  (APt, aMoLurvaräy^  frastirmU  *vlJ>arasca  avJ.- barasca  *raiufrii  "wenn  er  deren  mehrere an  verschiedenen  Stengeln  gewachsene spreitet,  ist  er  r.,  gleichviel  ob  er  sie  zerteilt oder  nicht"  N.50.
16370:—  saurva  *duziiq  (sd.)  *f}%rS  (AP.)  k^n- naoitiV .ig.AiZ-  Aa)  Du.,  ellipt 'Eltern'»: satäyus  (näml.  asti  mihrö)  antari  pitars (AD.)**  pu%r>mca  ". .  zwischen  Eltern  und Sohn"  Yt.  10.  117.  b)  Plur.,  ellipt.  'der Vater  und  die  Erwachsenen  seiner  Familie, die  erwachsenen  Familienangehörigen'»; yezica    alla  yU   katne  .  .  s^atö  gartwim
16371:irifyeiti  pt>r?byS*'>  astryäti  ptaribyS^'^ iri^fiti  ptpribys  irisintam  ralä  cikam baodS.varstahe  Whaya  ".  .  so  fällt  auf  die (envachsenen)  Familienangehörigen  die Sünde,  die  sie  tut,  und  der  Schaden,  den sie  zufilgt;  an  den  erwachsenen  Familien- angehörigen soll  man  die  Schädigungen der  Geschädigten  strafen  mit  . ,"  V.  75. la.  Wertlos:  yesi  narS..pairi  in%yHti
```


## [2026-09-05T20:37:22.550Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT 22870-22885 ===\"; sed -n '22870,22885p' BRT.txt | cut -c1-400\necho; echo \"=== BRT 7655-7670 ===\"; sed -n '7655,7670p' BRT.txt | cut -c1-400"
}
```


### [2026-09-05T20:37:22.616Z] TOOL RESULT

```
=== BRT 22870-22885 ===
nicht  (aus  dem  Haus)    heraus   können:
6/.  S50.  ZZ,   VON  STAC  KELBEIG  ZDMG.  4S.  493'
•  j.'varaeah- Adj.'' 'Utkräftig,  energisch':  ay^rt  „j  van'ia/si!  (s±)  nire  jasmti  V. v'äfNSm.)  Y.8'\  S.4.
Vgl  iz-flwfflA..  —  Pü. :  vai  var/än.  —  '}  VgL  Eig.  -wo  die  Menschen  gefangeii  sind'.  —  P&. :
aber  Pü.,  die  aJ.varf/ä  erwarten  lie»»e.  ^^  _  _  vatiai  vlrlh  mal  istei.
•  j.  varadah'vant-  Adj.  i)  'tatkräftig,,,  j.  varat5.ra9-a-  Adj.  (fem.  -äj-)  'mit energisch':  tiitrlm  .  .  ^^amanarikunUm  rollendem  Wagen':  ärväspqm  .  .  yuxta.- *'caahutU3m'''  yaoxstivanüm  YtÄ'.4g;  —  aspam  ''^am  Yto.a.
uyr)m    kavaim   s^artnö  .  .  'canuhantim'^  Vgl.  m  iiia-.
Yt  19. 9;  4S;  ->«i  *"«« ■  ■  w^A  v^»Ä»,«/a  ,  .      var»d- V.'augere'.  Praes.  2  v^r^da-,
kat  •JaT.hunttm^  Yt.  12.  i;  -  mapänam  \  _  pp^p  ^,^^j  ppfA.  (vi.)vantdavant- ..'canuhatqm  V.20.1  z)    «"rdevoU,   ^^^^^^j.  j^j.  ,,^„^„^„    *v,r«iyi.
erhaben':  rnä^^A^m  .  .  *'^a,»iu^i>fn'i  \t.\  .^^chsen  machen",  gedeihen  lassen. ^■/6.:.^^«-W(oder.«..™«.Aeri.,^j»i*.S^°!f/Pösser)  machen,  mehren':  a^^me
ägdn  kävuii).  -  ■)So  Fi.-  »>  ASm.  stait  gal^ä  fräoaya  .  .var^aya  \.2.^-    ¥.8;
J&n.  —  j)  Vgl.  Yt.  j.  4S,  Ai.  ».  —  azim  tl  gai%S  frmayeni  . .  var^aymt
dby  Google
1369
var«8a-
var«8«-

=== BRT 7655-7670 ===
•  j,  »radva-fana-  Adj,,  nur  fem,  'ni-  'deren Brüste  in  die  Höhe  stehen,  mit  straffen Brüsten':   kainTiiö  hhrpa  sriraya  .  .  'r/yä
H.2.9.
/hta-  ist  Komp.-Form  lU  /sfäna-;  s.  Bthl.  IF. 7,  6>  (wogegen  das  WZKM.  9.  167  (iesagle nichts  beweist).  —  ai.  vgl.  äriilivasfaiii-  fem. Adj.  —  Pü.:  *i/fiiU  filtin.
•  j.  araSwan-  Adj,  'der  gedeihen  lüsst, fördert':   mürS   vups  masdayamanam  .  .
dby  Google
351
*ar»dvaya
■»«zav-
35«
,  denen  .
"wäca  kiniwäca  "M.   ist  aller  J/aaÄi- i  würdig  erkannt  hast,  o  MAA. yasnei  Förderer  und  HUter"  Yt/0.120.    1Y.2Ä10,
Zum  V.  and:  \     El.?  —  Vü.:/r.irSn.   —   »  So  Ji,  K5;  NA.
I      ''iioB,  mit  uiii,'ii%isch«in  i\  s.  auch  Fu. •  j.  ''■«radvaya "  Adv.  'in  aufgerichteter  j        :  „j„äüii  p.  40:  lies  irinaxä. Stellung,    im    Stehen':    yat    allqm    ^J^d'  ^  .    \^^^^^.  „.  .gilber*:  car^ma  (sd)  .  . gavastrya  *var,smi  yr7zya,,tqm  . .     dass  ^^.^^  _  _  ,^  ^^^^^.^  Ylc  129;  '7-H, ■hnen.  wenn  sie  un  Stehen  landw
Afl//d».  -     ■)  Hds.  «««%.«/;    fl^  ist  möglich  P'l^ska   (sd.)    V.  i^.  1 1.  [Aog.  /?    llCSl
(s.  unter  jjjjrmi-),    aber   nicht   gerade    wahr- |  J/-»fl/J/(7l'i(.]
scheinlich;    i   falschlich    statt  ya   (wie  nach       KompA.;  Ableit.  —  Vßl.  ai.  rajaiä-  n.;  ann. Konsonanten,  S  ^^.J.  31);  s.  Bthl.  IF. //.  133. ;      arcaf.  —  Pü.:  asim.
```


## [2026-09-05T20:37:30.644Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"aufgerichtet\\|'hoch'\\|,hoch'\\|aufrecht\" BRT.txt | head -20"
}
```


### [2026-09-05T20:37:30.692Z] TOOL RESULT

```
7652:KompA, —  S.  ^iri^aa-  EN. —  Aus  aT.*/-!^-})««-; vgl.  ai.  ürdivä-  Adj.  (woiu  ].pr>iia- ;  ai./nr«<7. und  JScHMtDT  KZ.  32.  383,  Wn.  AiGr.  /.  262, Bt]TL.  IF.  7.  107)  oder  laL  arduut  (B(JM. Grdr.»  /.  323);).  —  Pü,  (lu  Y.  57):  awräsl, in  Komp.;  sUtiii,  luxsäi.  —  ')  Vgl.  iird/n-i.. äslhäl  RV.  2.  30.  3  (uö.).  —  =)  Zu  ooss.  ///v/;~ 'aufrecht',  soss.  iiri/a^  'Steilweg'  s.  Hau.  Oss. Spr,  62,  88,  US-
7667:I      ''iioB,  mit  uiii,'ii%isch«in  i\  s.  auch  Fu. •  j.  ''■«radvaya "  Adv.  'in  aufgerichteter  j        :  „j„äüii  p.  40:  lies  irinaxä. Stellung,    im    Stehen':    yat    allqm    ^J^d'  ^  .    \^^^^^.  „.  .gilber*:  car^ma  (sd)  .  . gavastrya  *var,smi  yr7zya,,tqm  . .     dass  ^^.^^  _  _  ,^  ^^^^^.^  Ylc  129;  '7-H, ■hnen.  wenn  sie  un  Stehen  landwirtschaft-   ^       g^  _  ^^^,„^  .^^^  ^J^^^^  z<,ramm; hche  Arbeiten  verrichten  ..'  N.^j  ,^^^  .^^,  -         ^^   ^^^^,  ^^^^
7675:•  j.  «rsSwö.drafSa-  Adj.  (fem.  'sä-)  'mit hoch  aufgerichtetem  Banner':  Aa»tayäsca,. °/ajni  Yt.  /,  1 1 ;  —  bäxölm  srJram  "sam V.J.6.
7679:•  j.aradwö.zvnga-,  *«radvö.zflnga-'*  Adj. (fem.  'gä-)  'mit  aufgerichtetem  Knöchel' sva.  '(immer)  auf  den  Füssen,  Beinen'": mi'ir»m  ..  'g^m  2amaahunt9m  Yt/o.6i; —  nairyam  kqm.varjÜJm  'gqm  a:^afnyqm Y.  62.  5 ; '  —  any3  *'g3  V.  5.9  PüZ.
7754:Eig.  'gerade  aufgerichtet,  ipiii',  vgl.  ari/a-, ?risya-;  aber  in  der  Bed.  durch  >r3s  beein- flusst.  —  ai.  /■jT'ii-  Adj.  'hoch'.  —  Pu.:  läsi; Sü.:  salya»,  (lU  Y.  5/.  S):  S'iralai.
8603:•  j,  *uz-arsta-'>  Adj,  (fem.  -/J-)  'gerade aufgerichtet,  von  gerader,  aufrechter  Figur': kaiiiTnS  kihrpa  °tayä  hr?::aitya  H.  2.9.
9945:■>  Die  Lesung  des  vorletzten  Buchstabens  {f* oder  m'?)  ist  unsicher;  s.  KZ.  J/.  518. Übrigens  kann  Juetis  Deutung  des  Namens als  'Weiienland'  (GIrPh.  a.  430,  ZDMG,  51. i\o),  die  auf  . ,  m"  .  .  fusst  -  gifduma'va-  - nur  unter  der  VoiaussetzuDg  aufrecht  erhalten werden,  dass  in  jener  Landschaft  der  Ober- gang dei  Tenues  in  Mediae  nach  Nasal  um vieles  früher  stat^efunden  habe  als  sonst;  s. xantunia:  —  ')  Wie  aus  Bh.  J.    12  folgt.
13482:•  j.  däuru.-upa.darana-  d.  'aus  Holz (-Stangen  od.  dgl.)  aufgerichtete  Hütte">: yat  'tu  vä  *tumats.aiwi.varane  vä  spS  nS vä  iri>yai  V.  cV.  1.
17021:•  g.,  j.  baraziman- Adj. 'hoch':  imä  raeüa bartziit^m  •zimanqm  avat  (sd.)  yai  hvarJ avaaY.36.6i  —  Avan  bar7zisi?m  'zima- nqm Vr.  IQ,  2.
17184:•  j,  b^rszant-  Adj.  (fem.  -«aiff-)''  'hoch'; a)  von  a)  Menschen,  ß)  Göttern  und Y)  Tieren,  'hochgewachsen,  von  hoher Statur'  '* :  a)  nari  hhrpa  .  .  'satS  . .  ama- vatB  Yt<P.  13;  —  kaintnS  hArpa  ..  -xaiiyä  ^ a  2. 9 ;  ät  Vyt  56,  wo  'zantyä  i>.  ß)  am»-  j /anam  sptntanqm  . .  'zatam  Y.  26. 3 ;  zit Yt/5,15,  wo  •zantami'';  —  mi^nm  ahu-\
17203:•  j.  b^razi-gäSra-*  'hoch'  oder  'laut singend':  yim  zaotärttn  stayala  ahurS  ,  . °r}nt;  yazata  zaeta  .  .  'rd  b)r»zata  vaca YL  lo.  89.
25797:•  j.  saeni.kaofa-  Adj.  '(mit  spitzem,  d.  i.) gerade  aufgerichtetem,  steifem  Höcker' '\ vom  Kamel:  uäräaha  .  .  'Ja  YLr7. 13; —  u/tranqm  .  .  'fanqm  V.  22. 3.
29236:avä  yä  da  asts  (sd.)  .  .  "wann  durch  die Hand,  in  der  du  jene  Lose  hältst,  die  . ." Y.  43.  4.  a)  'aufrecht  erhalten,  stützen': voAa  Avö  xsa%r3  asfm  vacargha  ^aokanäiS Aaptl  (3S.)  "er  stützt  das  Asa  sammt  dem guten  Reich  durch  sein  Reden  und  Tun" Y._;i,  aa.
```


## [2026-09-05T20:37:41.456Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== ARY بالیدن/والا ===\"; grep -n \"بالیدن\\|والا\\b\" incoming/ARY/ARY_pages.txt | head -15\necho \"=== ARY latin index WERDH/ERED ===\"; grep -n -i \"WERDH\\|WREDH\\|ERED\\b\\|ERDH\" incoming/ARY/ARY_latin_index_pages.txt | head -15\necho \"=== HUB 173 ===\"; grep -n \"^ *173\\.\\|balid\\|bälid\" HUB.txt | head -10"
}
```


### [2026-09-05T20:37:41.532Z] TOOL RESULT

```
=== ARY بالیدن/والا ===
259:والامیزان همسانی زبانهای مجاور به گونه‌ای دیگر مي‌بود.
393:کند. برعکس» عبری زبانی والا و اصبل است که طی قرون تغییر نکرده است و هر کسی که غبری
628:کیفیت والای این اثر در سطحی است که امروزه هم برای شناخت زبان سانسکریت از آن استفاده
981:مورد به قربانی کردن انسان اشاره شده است. ظاهراً در نظر هندیان پاستان» انسان والاترین جانداری
1054:هسرش) پیامد دیگری نیز داشت: مقام او والاتر از مقام پدر و رئیس ابل بود ولی آنها راکاملاً
1118:[. البته ارج اجتماعی آنها با مقام والای لبیدهای باستانی قابل مقایسه نیست. متاسفانه اختراع رادیو و
2600:آلمانی کهن (0880/۸ لوالا 2ام): اترا رن
9322:آلمانی کهن (/(058/2 لوالا ).۲ 5 (3۲) +7 ملظ
14141:آرمنی (4/48/14۷): لوالا ۸
15241:والانه ولانه (به چم *زخم", *جراحت") / ۵۱۵ ٍ
=== ARY latin index WERDH/ERED ===
406:BUGS te pS tas crc ered acl s 2llels elite! bik WS
3095:rrr igbG Oey VERED (RUSSIAN) g3)
6890:COaS cape dail ered ee CT pees LT
11413:LEPAROS, LEPERDHI LAIBA, LIBAN, BILEIBAN, BILAIBJAN
=== HUB 173 ===
751:173. Np. bdltdan Vachsen' zu phi. caus. voimttan Phi.
```


## [2026-09-05T20:37:43.110Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== IEC uerdh ===\"; grep -n \"uerdho\\|werdh\\|urdhuos\\|orthos\" IEC.txt | head -15\necho \"=== SYN grow/high ===\"; grep -n \"vardhate\\|ūrdhvá\\|urdhva\\|orthos\" SYN.txt | head -15\necho \"=== MON اروپا ===\"; grep -n \"اروپا\" MON_part1.txt | head -5"
}
```


### [2026-09-05T20:37:43.209Z] TOOL RESULT

```
=== IEC uerdh ===
=== SYN grow/high ===
=== MON اروپا ===
288:متداول در فارسی؛ لغات اروپائی که بتدریج در فارسی وارد شده و اعلام 
10276:اروپایی: 0۳25 (ص‌نسب.) منسوب به 
10277:ارو با. هر چیز که در اروپا سازند و از اروبا 
10278:آورند: اجناس اروپایی: امل اروبا؛ مردم 
10281:۱۳ فرهنگک فارسی معین اروپایی‌ماب
```


## [2026-09-05T20:37:48.617Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HUB 745-765 ===\"; sed -n '745,765p' HUB.txt\npython3 - <<'EOF'\nt=open('HUB.txt',encoding='utf-8',errors='replace').read().split('\\n')\npre='\\n'.join(t[:751]); print('leaf',pre.count('\\f'),'printed',pre.count('\\f')-10)\nEOF"
}
```


### [2026-09-05T20:37:50.420Z] TOOL RESULT

```
=== HUB 745-765 ===
lehre p. 19 (wegen I aus rd = rz) annimmt, altes
Lehnwort zu sein. Doch ist das Suffix aS, ad echt
balu5i, vgl. drazad Lange' (neben drazt) von drag lang- 24 —
(Dames, Grammar p. 14). Np. ftai^a *hoch, H5he* ist
wohl mit Suffix a aus ok (= phi. *bardak) gebildet
wie garma etc. (Darmesteter, Etud. iran. I, 267).
173. Np. bdltdan Vachsen' zu phi. caus. voimttan Phi.
Vend. 9, Z. 6 (vahn) ^) = zd. varedaya- Vachsen machen ,
Mann- Andreas, ZDMG. 47, 702.
174. Zu ham Morgen =paz. ham Aogemad. 114, vgl. phi.
hosbam 'daybreak' Gl. and Ind. p. 52, Min. Gl. 104,
Aogemad. 129, paz. bomdaS *dawn* Min. Gl. 40, bal.
gvarbOm *Dammerung' (Geiger Nr. 138). Afgh. bam
*Dach des Hauses* gehort zur folgenden Nummer. Zd.
bdmya- (im Metrum dreisilbig : botniya-) heisst trotz
Geldner nie sublimis*, sondern glanzend, strahlend,
heir (vgl. yt. 5, 64, 78, 101 ; 10, 44, 50 ; 13, 59 etc.)
und ist ~ phi. hamik glanzend' Gl. and Ind. p. 76,
auch *njorgentlich, ostlich' (wie die Armenier es iiber-
setz6n: Bahl i bamik^ = „das morgentliche Balch**).
175. Ich finde iiberall in Wb. und Glossarien nur hdtn
leaf 34 printed 24
```


## [2026-09-05T20:37:50.930Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== IEC try ===\"; grep -n \"uerdhö\\|uerdh\\|vrdhati\\|ürdhvas\\|orthös\\|ordhuos\" IEC.txt | head -10\necho \"=== IEC grow ===\"; grep -n \"Skt. vardhati\\|vardhati\" IEC.txt SYN.txt | head -10\necho \"=== SYN 'to grow' section ===\"; grep -n \"Grk. orthos\\|orthos, \" SYN.txt | head -5"
}
```


### [2026-09-05T20:37:51.038Z] TOOL RESULT

```
=== IEC try ===
19951:ueldho “grow strong, thrive, succeed'. (Skt. ambig. cf. urdh- (1)). Cf. uoldh-, uldh- (1) Skt. (ambig.) várdhami, tr. (increase; exalt'. ? uerdh-, urdh-); várdhe, mp. 'grow, get strong’; Av. (ambig.) voroó-, tr. ‘promote’; (z-gde in) Gk. álthomai, v. “get strong, re- cover’; Li. véldZiu, veldéti, v. succeed — to a legacy; possess’. (Isophones: MHG wilt, wilde ‘wild’; wilt, gs: wildes, sn. 'game-ani- mal": o-gde in walt, gs: waldes, m. ‘wood’, with cognates in general WGmc.)
20035:ueredh- (uerdh-) 'seethe, boil, stir, rouse, rile, anger Gk. erétho, erethízo, v. ‘rile’; OCS vrézdo, vréditi, v. “harm, injure’; vréZdajo, -ati, v. id.; vrédü, m. ‘wound, sore, harm’; R veredit, v. “Tile? beside vèred, m. ‘boil, abscess’; Ukr. cf. veredlivyj ‘harmful’; Cz. cf. vřed, Pol. wrodek, m. ‘boil, sore; MHG wirt, m. ‘eddy in seg’. (But for Go. fra-wardjan; OE for-wierdan 'des- troy’; OHG *wartjan, werten ‘harm’, see uert-; uort-, in view of Go. fra-wairpan ‘perish’, etc. Li. cf. vérdu, inf. virti, Latv. verdu, virt, v. “boil” where -d- occurs only in the pres. t.)
=== IEC grow ===
=== SYN 'to grow' section ===
```


## [2026-09-05T20:38:07.649Z] TOOL CALL #65: WebFetch

```json
{
 "url": "https://en.wikipedia.org/wiki/Marrakesh",
 "prompt": "Quote the \"Etymology\"/\"Name\" section: what is the origin of the name Marrakesh (Berber amur n Akush \"Land of God\"? mur akush? Murr-Akush?), and does the article say Morocco's name in European languages derives from Marrakesh? Any mention of Maghrib al-Aqsa?"
}
```


## [2026-09-05T20:38:09.560Z] TOOL CALL #66: WebFetch

```json
{
 "url": "https://en.wikipedia.org/wiki/Europe",
 "prompt": "Quote the \"Name\"/\"Etymology\" section on the origin of the name Europe: the Semitic erebu/ereb theory (Akkadian, Phoenician), the Greek eurys+ops theory, and what modern scholars (e.g. M. L. West, Beekes) say about whether the Semitic derivation is accepted."
}
```


### [2026-09-05T20:38:14.926Z] TOOL RESULT

```
# Origin of Marrakesh's Name

According to the article, one proposed etymology derives from "the [Berber](https://en.wikipedia.org/wiki/Berber_language "Berber language") (Amazigh) words _amur n akuc_, which means 'Land of God'."

However, historian Susan Searight offers an alternative interpretation, suggesting "the town's name was first documented in an 11th-century manuscript in the [Qarawiyyin](https://en.wikipedia.org/wiki/Qarawiyyin "Qarawiyyin") library in [Fez](https://en.wikipedia.org/wiki/Fez,_Morocco "Fez, Morocco"), where its meaning was given as 'country of the sons of Kush'."

## Connection to Morocco's European Names

Yes, the article confirms this connection: "Various European names for Morocco (Marruecos, Marrocos, Maroc, Marokko, etc.) are directly derived from the name _Murrākuš_." The text explains that from medieval times until the early 20th century, "the entire country of Morocco was known as the 'Kingdom of Marrakesh.'"

**Note:** The article does not mention "Maghrib al-Aqsa" in the provided content.
```


### [2026-09-05T20:38:16.910Z] TOOL RESULT

```
# Etymology of "Europe"

## Three Main Theories

**Greek Theory (eurys + ops):**
"'wide, broad', and ὤψ (_ōps_) 'eye, face, countenance', hence their composite _Eurṓpē_ would mean 'wide-gazing' or 'broad of aspect'."

**Semitic Theory (erebu/ereb):**
Scholars have attempted connecting the name "to a Semitic term for _west_, this being either [Akkadian](https://en.wikipedia.org/wiki/Akkadian_language "Akkadian language") _erebu_ meaning 'to go down, set' (said of the sun) or [Phoenician](https://en.wikipedia.org/wiki/Phoenician_language "Phoenician language") _'ereb_ 'evening, west'".

## Modern Scholarly Consensus

**Rejection of Semitic Origin:**
Martin Litchfield West concluded that "phonologically, the match between Europa's name and any form of the Semitic word is very poor." Beekes similarly "considers a connection to Semitic languages improbable," instead proposing a pre-Indo-European origin with geographical parallels in ancient Greece rather than Semitic linguistic roots.
```


## [2026-09-05T20:38:40.187Z] TOOL CALL #67: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A7%D8%B1%D9%88%D9%BE%D8%A7",
 "prompt": "Give the Persian etymology of اروپا (Orupâ / Urupâ, Europe) verbatim: is it borrowed from French Europe or from Russian/another language?"
}
```


## [2026-09-05T20:38:41.322Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '10266,10282p' MON_part1.txt"
}
```


### [2026-09-05T20:38:41.370Z] TOOL RESULT

```
بخواهند نا کامی و عدم موفقیت کسی را در 
کاری به رخ او بکشند و او را سرزنش کنند. 
ارواح دراب : (عم.) قسم به روح پبدرم» 
سوگند به روان پد‌رم. این جمله را در مقام 
سوگند و بیان حق بودن کار و نظر خود 
می‌آورند. دنیای دیگر دنیای مردگان؛ 
دنیای روان‌ها. (عم.) گاه به معنی مرده و 
بی‌جان و در متام دشنام به آدم بی‌حال و 
سست و مات , ر می بر ند. 

اروپایی: 0۳25 (ص‌نسب.) منسوب به 
ارو با. هر چیز که در اروپا سازند و از اروبا 
آورند: اجناس اروپایی: امل اروبا؛ مردم 


۱۳ فرهنگک فارسی معین اروپایی‌ماب
```


### [2026-09-05T20:38:44.270Z] TOOL RESULT

```
Based on the provided content, there is **no etymology section** in this Wiktionary entry for اروپا (Orupâ/Urupâ). 

The page only includes pronunciation information and the definition that it refers to "Europe (a continent located west of Asia and north of Africa)," but it does not specify whether the Persian word is borrowed from French, Russian, or another language source.

To answer your question about the etymology, you would need to consult additional sources or a more complete dictionary entry.
```


## [2026-09-05T20:38:55.478Z] TOOL CALL #69: Bash

```json
{
 "command": "for u in \\\n \"https://www.etymonline.com/word/Europe\" \\\n \"https://www.etymonline.com/word/Morocco\" \\\n \"https://en.wikipedia.org/wiki/Europe\" \\\n \"https://en.wikipedia.org/wiki/Marrakesh\" \\\n \"https://en.wiktionary.org/wiki/%D9%88%D8%A7%D9%84%D8%A7\" \\\n \"https://en.wiktionary.org/wiki/%E1%BD%80%CF%81%CE%B8%CF%8C%CF%82\" \\\n \"https://en.wiktionary.org/wiki/%D8%BA%D8%B1%D8%A8\" \\\n \"https://en.wiktionary.org/wiki/Marrakesh\" \\\n \"https://en.wiktionary.org/wiki/Europa\" \\\n \"https://en.wiktionary.org/wiki/%D8%A8%D8%A7%D9%84%DB%8C%D8%AF%D9%86\" ; do\n timeout 120 python3 tools/fetch_source.py \"$u\" --note \"pdf page 158 (book p.128), roots Erebu / Ered-Werdh: Europe, Maghrib/Morocco, orthos, valâ/bâlîdan\" 2>&1 | tail -2\ndone"
}
```


### [2026-09-05T20:39:01.673Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/9403f76aa5831576.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a6dfc02a268997a6.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c094a113adea61a1.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/3d4474940b62a36e.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f395d299256bc367.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/8f6ed1247b67b135.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d6988f00066dd4a8.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/1e0a6b9b8909e6d3.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d51d343108bfe212.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f58ea5d233ae33c6.txt
```


## [2026-09-05T20:39:04.685Z] TOOL CALL #70: Bash

```json
{
 "command": "grep -n -i -m1 \"etymology\" data/verification/sources/web/f58ea5d233ae33c6.txt | head; echo ---; sed -n '1,10p' data/verification/sources/web/f58ea5d233ae33c6.txt; echo ---; grep -n -A12 -i \"Etymology\" data/verification/sources/web/f58ea5d233ae33c6.txt | head -40"
}
```


### [2026-09-05T20:39:04.752Z] TOOL RESULT

```
---
URL: https://en.wiktionary.org/wiki/%D8%A8%D8%A7%D9%84%DB%8C%D8%AF%D9%86
FETCHED: 2026-09-05T20:39:01Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 404: Not Found---
```


## [2026-09-05T20:39:36.331Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== RCH gharb ===\"; grep -n \"gharb\\|maghrib\\|maghrab\" RCH.txt | head -8\necho \"=== MON مغرب/غروب ===\"; grep -n \"^مغرب:\\|مغرب: \\|^غروب:\\|غروب: \" MON_part2.txt | head -6\necho \"=== FSD Europe ===\"; grep -n \"Eu-ro-pe\\|Europe, n\\|erebu\" FSD_vol2.txt | head -5\necho \"=== WEB morocco ===\"; grep -n \"Morocco\\b\" WEB_vol1.txt | head -3"
}
```


### [2026-09-05T20:39:36.437Z] TOOL RESULT

```
=== RCH gharb ===
7182:V   ashbah^i  maghrably  Sarsaparilla.
8842:A   aghribnty  (pi.  of  L^jB  gharb)  Showers  of  team.  The lachrymal  glands  or  ducts.  The  extremities  of  the  eyes.  .   Tu- mourn  in  the  corners  of  the  eyes.  Principal  parts  of  any  thing. Acrimonies,  acidities.  Cheerful  dispositions.  Largo  buckels made  of  ox-leather.  Eloquent  (tongues).  Settings  (of  the  sun). The  first  startings  of  young  horses  in  a   coume.  (Horses)  run- ning often.  Departures.  (People)  excelling  (in  any  thing). Spittles.  of  f^\jB  ghirab)  Swords,  hatchets,  or  rather  the curved  parts  of  their  edges  (with  which  the  blow  is  struck), (pi.  of  ghurdb)  Crows,  ravens.  The  prominertt  parts  of the  hips  of  horses  or  camels.
29463:yinuHjdniby  Gentle,  of  amiable  manners, jdnibuU  gharblyy  The  western  part  of  Mount  Sinai  (where  God appeared  to  Moses).  (Kur’an.)  %
39684:maghrib,  The  Western  Ocean.  J-5  darya-i  nil,  Th river  Nile.  JCyfc  darya4  Ilindy  The  Indian  Ocean, p   dnrydb^  Know  thou.  Knowing.  The  sea.
45385:zfir-i  mt4shi»qfs'hdrj  A   soft  kind  of  ffold  which  might  be  moulded into  any  shnpi  ,jj  zar^i  maghribl^  Purest  gold.  The
52006:ear  of  a   sheep.  The  east.  The  rising  sun.  A   fissure.  Light shining  through  a   crevice.  <-r^  J   shark  zoa  gharbf  The east  and  west.  Shirks  Light  transmitted  through  a   crevice. Sharak  (from  Being  slit  in  the  ear  (a  sheep).  Being
56580:LJy.  Tardbulus^i  gharby  Tripoli  in  Barbary.
61522:gharby  Sun-set.  The  west.  Africa.  The  flowing of  tears.  A   lachrymal  vein  or  duct.  The  sharpest  parts  of  the teeth;  also  their  brightness.  The  most  prominent  part  of  any thing;  as  the  curvature  of  a   sword.  Quickness  or  vehemence of  speech.  A   large  bucket.  The  first  course,  race,  or  starting of  a   horse.  (A  horse)  running  much.  A   distemper  in  the  cor- ners of  the  eye.-  The  poplar-tree.  The  mountain-pine.  A silver  goblet.  Wine.  The  stone  of  a   grape.  Gharaby  Silver. Plate.  Wine.  Water  dripping  from  the  bucket  whilst  drawing up  from  the  well.  A   distemper  incident  to  cattle,  making  the hairs  to  drop  from  their  eye-lids.  Whiteness  of  the  hair  of  the eye-lid.  A   large  bucket.  A   willow.  Strange. sahm^i  gharaby  An  arrow  of  which  one  loses  sight,  and  knows not  where  it  has  struck.  Ghuruby  A   foreigner,
=== MON مغرب/غروب ===
1395:غروب: «تت۰« (ع.] (مصل.) فرو شدن 
=== FSD Europe ===
51798:Mosaic  purificatory  and  sacrificial  rites: thought  by  some  to  have  been  a   species  of marjoram  (OTiganummaru);  by  others,  the caperebush  (Coppcrissplnosa).  Probably  the  ,2 term  was  used  as  the  name  of  any  common article  in  the  form  of  a   brash  or  a   broom. l<  AS.  i/sope,  <   h.hussopim,  <   Qt.hyssSpos,  M aromatic  plant,  <   Heb.  Sebpli,  aromatic'^ plant,]  -   anise  hyssop,  a   species  of  giant hyssop  (Agasiache  anethiodora  of  the  north- western United  States,  with  anise-scented leaves.—  bastard  h.,  a   small  germander  (I'ea- cHiim  poHum)  of  southern  Europe:  cultivated in  gardens.— fraisrant  giant  h.,  the  anise hyssop.— giant  n.,  any  species  of  Agauache,  , a   genus  of  tall,  perennial,  chiefly  American  ■ herbs  of  the  mint  family,  with  serrate  leaves, and  blue  or  purplish  flowers  clustered  in  termi- nal spikes.
73403:Lead  was  known  to  the  ancients,  and  is  mentioned  In  the Book  of  Job.  It  is  seldom  found  native;  but  its  ores  are common,  especially  the  sulftd,  the  mineral  galena,  which,  it is  said,  was  useti  as  a   glaze  for  earthenware  in  the  time  of Solomon.  The  Romans  smelted  Its  ores  and  casfr  the  metal into  pigs;  and  water-pipes,  weights,  etc.,  of  their  manufac- ture are  frequently  found.  It  now  finds  extensive  use  in  the manufacture  of  water-pipes,  and  its  compounds  are  used  in medicine  and  .as  pigments.  Its  ore  occurs  largely  in  Europe, notably  in  Great  Britain.  Germany,  and  Spain,  while  in  the United  States  its  frequent  occurrence  with  silver  makes  its smelting  one  of  the  foremost  metallurgical  industries.
=== WEB morocco ===
5422:2. the wood of the sandaractree of Morocco. Al-ex-an/dri-in, n. a citizen of Alexandria. a. (Fr. alerte; It. all’ eria, on the watch; Al-ex-an/drine, 7. in prosody. an iambic line
25333:frica. Otis tetrax, the little bustard, inhabits southern Europe and Morocco. There are about twenty species.
72408:feyne, v.t. to feign. (Obs.j fez, n.; pl. fez'zeş, (Turk. fez, from Fez, the city in Morocco, where they were made] a Ge felt cap, usu- ally red, with a black tassel hanging from the crown: formerly worn by Turkish men. fi, ». [arbitrary modifi- cation of fa.] in music, a syllable representing the tone intermediate between fa and sol of the diatonic scale: see solfeggio. fi-ä’cre (-kér), n. [Fr., after the Hotel St. Fiacre in Paris.] in France, a small carriage for hire. _ fi/ance, v.t.; fianced. pt., pp.; fiancing, poen (Fr. fiancer, to betroth.] to betroth. (Obs, i fiancé’ (fé-dn-si’, fe-an/sa), n. (Fr. pp. of fiancer, from fiance, a promise.) the man to whom a woman is engaged to be married. fi-an-cée’ (fz-äñ-sã’. f€-iin’sa), n, [Fr., fem, of fiancer; see fiancé.) the woman to whom man is engaged to be married. Fi/An-na, n. the Fenians. í fi/Ants, n. [Fr. fiente, dung.] the dung of a wolf, badger, or certain other animals. fi/dr, n. 1. the person to whom belongs in fee. subject to a life ri 2. {pl.] the price of grain, as fi counties of Scotland, by the sheriffs and a jury. [Scot.} fi-as’cd, n.; pl. fi-as’cdes, fi-as’c6s, [It. bottle.| a complete failure; action that to a ridiculous end, = fiat, n. [L. fiat, 3rd pers. sing. pres. sul fieri, to become, come into existence.
```


## [2026-09-05T20:39:38.224Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SKT europe/ortho lower ===\"; grep -n -i \"europe\\|ortho-, prefix\\|ORTHO\" SKT.txt | head -8\necho \"=== IEC urdh ===\"; grep -n \"urdh-\\|ordhuos\\|orthós\" IEC.txt | head -8\necho \"=== SYN high/grow ===\"; grep -n \"Skt. vardh\\|Av. vared\\|ürdhva\" SYN.txt | head -8"
}
```


### [2026-09-05T20:39:38.309Z] TOOL RESULT

```
=== SKT europe/ortho lower ===
1284:(XV  cent  ha£hU\  to  Tnifr.«-Lo«t hauth^  baugk,  baach  iwith  euttutat gk),  insolhcicnt.  dull  f*Ki<i  nftotiU), poor,  tired,  jadeil micKKiV  <•  Icel biigr,aaeasy.biigr,^v>i.,. ,  ..<> to  hinder,  oppress.  Prob. V.bcJ7^,  to  mock. Bag.  (E.)  Put  for  ba/f  ME.  hi O.  Northomfarian  b^fic*  ^g>  Loke^  I 35.+Goth.  balgs,  a  wine-sLin:  G  htk skin  ;  Icel.  Ar^,  a  skin,  a  bog.  So  j GaeL  ha!gt  ^/f,  also  ^^,  a  liTithem  \ Lit.  'that  which  swells  out.'  CTNJ BALG.)    See  Bulse.  1
4320:oreole,  one  bom  in  the  W.  Indies,  but of  European  blood.  ^F  — Span.*L.)  F. rrA'/r.  —  Span.  (rioHo,  a  neyro  corruption of  creadi//a,  dimin.  olcriado,  one  educated, instructed,  or  brought  up;  hence  a  child of  European  blood.  CriaJo  is  pp.  otin'art, to  cieatc,  aUo,  to  educate.->L-  crtarr,  to create,  make.
11915:Moslem,  a  Mussulman.  (Arab.)  Arab. moslim,  *a  mnsulmao,  a  true  believer  in the  Mohammedan  faith ; '  Richardson.  Cf. Arab.  mtualUm,  oat  who  aoqniesces.  A mussuiman  is  one  who  professes  ii/dm, i.  e.  submission  to  the  will  of  God  and  to the  orthodox  faith. —  Arab,  sa/ama,  to  sub- mit %  The  E.  words  mosUm,  mussuiman, islam,  and  talaam  are  all  from  the  &ame Arab,  root  satama,  to  submit.
11916:mussuiman,  a  true  believer  in  the Mohammedaa  laith.  (Fers.  — Arab.)  Pers. musuhndn,  an  orthodox  believer.  — Arab. mcsiim,  ptuiiim  (above).
12892:Orthodox,  of  the  ri^ht  faith.  (L  -Gl Late  L.  orthodcxus.  —  Ck.  ^^i^^Ae^et,  dT right  opinion.  aaGIc  6pB6-9,  upright,  li^ Su£a.  an  opinion,  from  Soncir,  to
12893:orthoepy,  correct  pronnodatioo.  (O From  (>k.  6pdo4wfia^  orthoepy. ••Gk.ifN right ;  iw-ns,  a  won! ;  sec  Epto.
12894:Orthography,  correct  anting.  (F. -Gk.)     M.  E.  erte^raphit.^J  pritintk —  L.  orikcgrxt^Jiia.^Cik.  6p»tripafm.^^ ipBo-f,  right ;  ypcht»«iv,  to  write.
12895:Orthopterous,    lit.     straight (Gk.)    Gk.  6peC-s.  straight :  wr^pSv,  aWi
=== IEC urdh ===
1769:bhrdhos (4) ‘soft, feeble, crumbly’. Cf. bhurdh- Alb. 1 brydhët “soft, mellow; m-brydh, v. *mellow'; W brydd “feeble, ailing'. (paralleled ` in Arm. brdem ‘crumble’, fr. bhurdh-, q.v.) '
2579:duk- — durdholos (durdh-, drudhol-)
2595:durdholos (durdh-, drudhol-) (1) ‘tufted; tuft'. (Same as (2)?) NGer. or LG (> G) Troddel ‘tassel, bob’; Sw. cf. torda Choopoe or sim. bird, infi. by Lat. tarda?); Cz. drdol ‘crest, plume, bun of hair (ambig.); drdlice ‘crested lark’; cf. also drdat ‘pluck, plume?
2596:durdholos (durdh-, drudhol-) (2) ‘tremulous,
3321:dhurdh- ‘shake, tremble’. See dhudhro- and durduro-, dhrdh- Arm. cf. (ambig.) drdvem; MHG turd *brome- grass; EMG (WG or Frankish) Dort, id.
4431:(grdh- “noise; audible’, etc. see gurdh-; “weak, sluggish’, etc. see gurd-, gurd-)
4944:grunnr, adj. & s. ‘bottom; shallow’; R grjadà ‘bed, layer’; Srb. greda (2) ‘sandbank’; Blg. gred ‘baulk of field’; LW in Rum. grindă ‘beam’ and in Hung. gerenda ‘beam, joist’; Li. grindà, grindis, f. & griñdas, m. “floor- board”; pl. ‘floor’; Latv. grīda “floor” ghrobh-, see ghrabh-. For a variant *ghrobh-, cf. Li. gruobstas ‘armful; sheaf ghrodio “shout, resound, blare, cry Skt. hrade, id.; hradayami ‘make sound": Alb. cf. (ambig.) n-gredh, (Cincite', but cf. gurdh-); MHG gruos; (3) ‘lament’; OE gretan (3) ‘to
5399:gur- (3) ‘appellation, song, praise; revere, sacrifice, worship’. Cf. gurdh- (1) and gurtos Skt. giráh, gir ‘praise’; Lat. au-gur, gs -guris, au-guria (here despite WH); Li. giriü, ti ‘praise’; gyrà ‘boasting’
=== SYN high/grow ===
32879:OPers. vardana- prob. : Av. varazana- ‘community, state, common people’, Skt. vrjana- ‘inclosure, settlement’, etc., fr. the root in Av. varaz- ‘shut off’, Grk. elpyw ‘shut in (out)’, etc. Walde-P. 1.290. Barth. 1424f. But the OPers. word could also correspond to Skt. vardhana- in town-names like Pundra- vardhana-. R. A. Hall, Jr., Language 12.297 ff. (suggesting deriv. fr. the root of OE wardén ‘watch over, protect’). Still otherwise on Skt. vardhana- (as loanword fr. OPers.) Wackernagel-De- brunner) KZ 67.168 f.
```


## [2026-09-05T20:40:05.924Z] AGENT

Now let me write the verification file.


## [2026-09-05T20:48:07.004Z] TOOL CALL #73: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build158.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW_ETYM_EUROPE = \"https://www.etymonline.com/word/Europe\"\nW_ETYM_MOROCCO = \"https://www.etymonline.com/word/Morocco\"\nW_WP_EUROPE = \"https://en.wikipedia.org/wiki/Europe\"\nW_WP_MARRAKESH = \"https://en.wikipedia.org/wiki/Marrakesh\"\nW_WT_VALA = \"https://en.wiktionary.org/wiki/%D9%88%D8%A7%D9%84%D8%A7\"\nW_WT_ORTHOS = \"https://en.wiktionary.org/wiki/%E1%BD%80%CF%81%CE%B8%CF%8C%CF%82\"\nW_WT_GHARB = \"https://en.wiktionary.org/wiki/%D8%BA%D8%B1%D8%A8\"\nW_WT_MARRAKESH = \"https://en.wiktionary.org/wiki/Marrakesh\"\nW_WT_EUROPA = \"https://en.wiktionary.org/wiki/Europa\"\n\ndoc = {\n  \"pdf_page\": 158,\n  \"book_page\": 128,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-05\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Erěbu\",\n      \"verdict\": \"plausible\",\n      \"modern_form\": \"Akkadian erēbu 'to enter, go in; (of the sun) to go down, set' (ereb šamši 'sunset, west'); ultimately Proto-Semitic *ġrb 'to enter, to set (of the sun)'\",\n      \"note\": \"The Akkadian headword, its language label and its gloss are all correct: erēbu is the ordinary Akkadian verb 'to enter', used of the sun setting, whence ereb šamši 'sunset, the West'. Two structural reservations. (a) The chart makes Arabic ġ-r-b and Hebrew ʿerebh DESCEND from Akkadian; modern Semitists treat all three as sister reflexes of one Proto-Semitic root *ġrb (Akkadian lost the gutturals, so *ġarābu > erēbu; Hebrew merged *ġ into ʿ, so *ġereb > ʿereb; Arabic alone keeps ġ). Nourai's own source Zimmern (AKD 64) writes the borrowing arrow with 'viell.' ('perhaps'), and Klein s.v. maarib says only 'is rel. to'. (b) The point of the whole chart — Greek Eurṓpē from this Semitic word — is rejected by current scholarship (M. L. West: 'phonologically the match is very poor'; Beekes: Pre-Greek). REFERENCE MISPRINT IN THE BOOK (not an extraction error): the Arabic node #1 is cited as 'AKD:640,854', but Zimmern's Akkadische Fremdwörter has only ~85 printed pages. The printed page (checked at 600 dpi) really does read AKD:640,854; it is Nourai's misprint, almost certainly for AHD:640,854, i.e. the American Heritage Dictionary pages he cites twice more on this same chart (AHD:854 Morocco, AHD:452 Europe). The JSON reproduces the page faithfully.\",\n      \"note_fa\": \"ریشهٔ اکدی erēbu «درآمدن، وارد شدن؛ فرو رفتن (خورشید)» واژه‌ای واقعی و برچسب زبانی و معنای آن درست است؛ ترکیب ereb šamši در اکدی یعنی «غروب آفتاب، باختر». اما دو ایراد ساختاری هست: نخست آنکه نورایی عربی «غ‌ر‌ب» و عبری ʿereb را زادهٔ اکدی نشان داده، حال آنکه زبان‌شناسان امروزی هر سه را بازتاب یک ریشهٔ سامی آغازین *ġrb می‌دانند (اکدی حروف حلقی را از دست داده و *ġarābu به erēbu بدل شده؛ عبری ġ را با ʿ یکی کرده؛ تنها عربی غین را نگاه داشته است)؛ خودِ تسیمرن (مأخذ AKD ص ۶۴) این وام‌گیری را با قید «شاید» آورده و کلاین هم فقط می‌گوید «هم‌ریشه است». دوم آنکه بنیادِ کل نمودار، یعنی گرفتن یونانی Eurṓpē از این واژهٔ سامی، در پژوهش امروزی رد شده است (وست و بیکس). همچنین ارجاع «AKD:640,854» در چاپ کتاب نادرست است — کتاب تسیمرن حدود ۸۵ صفحه بیشتر ندارد — و خطای چاپی خودِ نورایی است، نه خطای خوانش اسکن.\",\n      \"sources\": [W_ETYM_EUROPE, W_WP_EUROPE],\n      \"ref_check\": [\n        {\"ref\": \"AKD:64\", \"status\": \"supports\", \"note\": \"Zimmern, Akkadische Fremdwörter, printed p. 64 (AKD.txt leaf 73, grep -n 'erebu'): 'akk. erēbu allg. eintreten, hineingehen (z. B. in ein Haus), dann spez. untergehen (von der Sonne und den Gestirnen), ereb šamši Sonnenuntergang, Westen : > viell. ... hebr. ʿāreb Abend, aram. ʿarab, arab. ġariba, äth. ʿarba untergehen (von der Sonne), hebr. maʿarab, aram. maʿrabā, arab. maġrab, maġrib, äth. maʿrāb Westen.' Exactly Nourai's root box and his Arabic/Hebrew arrows — but note Zimmern's own 'viell.' (perhaps).\"},\n        {\"ref\": \"KLN:550\", \"status\": \"supports\", \"note\": \"Klein s.v. Europe (KLN_1966.txt leaf 299): 'L. Europa, fr. Gk. Eurṓpē ... which is prob. of Semitic origin. Cp. Akkad. erebu, \\\"to enter, go in; to go down, set\\\" (said of the sun), ereb shamshi, \\\"sunset\\\", Heb. ʿerebh, \\\"sunset, evening\\\" ... Accordingly Eurṓpē orig. meant \\\"the Region of the Setting Sun\\\".' The claim is Klein's, verbatim. (My leaf→page mapping puts this nearer p. 574 than p. 550, but the leaf-offset drifts in this scan; the entry itself is unambiguous.)\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"AKD\", \"where\": \"printed p. 64 (leaf 73)\", \"stance\": \"supports\", \"note\": \"'akk. erēbu ... ereb šamši Sonnenuntergang, Westen : > viell. ... arab. ġariba ... arab. maġrab, maġrib ... Westen' — Zimmern's own hedge 'viell.' is why I grade the root plausible rather than confirmed.\"},\n        {\"src\": \"KLN\", \"where\": \"s.v. Europe, Erebus, maarib (leaves 299, 292, 493)\", \"stance\": \"supports\", \"note\": \"s.v. maarib: Heb. ʿerebh 'which is rel. to Arab. gharaba, Ethiop. ʿaraba, \\\"(the sun) has set\\\", Arab. gharb, \\\"place of sunset, west\\\", Akkad. erebu, \\\"to enter, go in\\\", ereb shamshi, \\\"sunset\\\"' — 'rel. to', i.e. cognate, not descended.\"},\n        {\"src\": \"FSD\", \"where\": \"grep of vols 1-4 for 'erebu'\", \"stance\": \"silent\", \"note\": \"Funk & Wagnalls' Europe entry did not surface in the OCR; no independent statement found there.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1, \"lang\": \"Arabic\", \"words\": \"ğ.r.b; mağreb; Mağreb al aqsâ\", \"verdict\": \"plausible\",\n          \"derivation\": \"Arabic ġ-r-b is a genuine triliteral root: ġaraba 'to depart, to withdraw; (of the sun) to set', whence ġarb 'sunset, west' and, with the ma- prefix of place/time, maġrib 'place and time of sunset; the West' (also the sunset prayer). Al-Maġrib al-Aqṣā 'the farthest West' is the standard term of the medieval Arab geographers (Ibn Ḥawqal, al-Idrīsī, al-Bakrī) for the westernmost of the three Maghribs (al-Adnā = Ifrīqiya, al-Awsaṭ = Algeria, al-Aqṣā = Morocco), so the gloss is right. The DERIVATION arrow, however, is not: Arabic did not borrow this root from Akkadian. Akkadian erēbu and Arabic ġaraba are parallel reflexes of Proto-Semitic *ġrb; Akkadian, which lost *ġ and *ʿ, shows e- where Arabic keeps ġ-, and the sound correspondence is regular in both directions, so nothing marks the Arabic as a loan. Zimmern, Nourai's source, prints the equation with 'viell.' (perhaps).\",\n          \"derivation_fa\": \"ریشهٔ سه‌حرفی عربی «غ‌ر‌ب» اصیل است: غَرَبَ «دور شدن؛ فرو رفتن (خورشید)» و از آن غَرْب «باختر» و با پیشوند مکان/زمانِ مَـ، مَغْرِب «جای و هنگام غروب؛ باختر». ترکیب «المغرب الأقصی» اصطلاح جغرافی‌نویسان مسلمان (ابن حوقل، ادریسی، بکری) برای دورترین مغرب یعنی کشور مراکش است، پس معنایی که نورایی داده درست است. اما پیکانِ اشتقاق درست نیست: عربی این ریشه را از اکدی وام نگرفته؛ erēbu اکدی و غَرَبَ عربی هر دو بازماندهٔ سامی آغازین *ġrb اند و چون اکدی غین و عین را از دست داده، e- در برابر غ‌ـ عربی نشسته است. خودِ تسیمرن نیز این برابری را با قید «شاید» آورده است. حکم: با احتیاط پذیرفتنی است، ولی به‌عنوان هم‌ریشگی نه وام‌گیری.\",\n          \"sources\": [W_WT_GHARB, W_ETYM_MOROCCO],\n          \"ref_check\": [\n            {\"ref\": \"AKD:640\", \"status\": \"not_found\", \"note\": \"Impossible page: Zimmern's Akkadische Fremdwörter runs to about 85 printed pages (111 scanned leaves). The printed chart really reads 'AKD:640,854' (verified on a 600-dpi render of pdf p. 158), so this is Nourai's own misprint — on internal evidence for AHD:640,854, since the same chart cites AHD:854 for Italian Marocco and English Morocco.\"},\n            {\"ref\": \"AKD:854\", \"status\": \"not_found\", \"note\": \"Same as above — out of range for AKD. The substance of the claim is however on AKD p. 64: 'ereb šamši Sonnenuntergang, Westen : > viell. ... arab. ġariba ... arab. maġrab, maġrib ... Westen'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"AKD\", \"where\": \"printed p. 64 (leaf 73)\", \"stance\": \"partial\", \"note\": \"Zimmern lists exactly these Arabic forms (ġariba, maġrab/maġrib) beside Akkadian erēbu, but marks the borrowing 'viell.'\"},\n            {\"src\": \"KLN\", \"where\": \"s.v. Maghrib (leaf 495)\", \"stance\": \"supports\", \"note\": \"'Maghrib, n., Barbary. — Arab. Maghrib, \\\"the West\\\", fr. gharaba, \\\"(the sun) has set\\\", whence gharb, \\\"place of the sunset, west\\\". See maarib.' — the internal Arabic morphology is exactly Nourai's.\"},\n            {\"src\": \"LKT\", \"where\": \"no. 674 (Ar. ġarbī)\", \"stance\": \"supports\", \"note\": \"Lokotsch: 'Aus demselben Stamme ar. ġaraba \\\"untergehen (Sonne)\\\" ist mit präfigiertem ma- zur Angabe des Ortes maġrib gebildet; der Maġreb ist Nordwestafrika von Tunis bis Marokko.'\"}\n          ]\n        },\n        {\n          \"id\": 2, \"lang\": \"Persian\", \"words\": \"ğarb «غرب»\", \"verdict\": \"confirmed\",\n          \"derivation\": \"غرب ġarb, together with the chart's extras مغرب maġreb and غروب ġorūb, is a straightforward Arabic loanword taken into New Persian in the Islamic period; all three are ordinary Arabic derivatives of ġ-r-b (ġarb 'west', maġrib nomen loci/temporis, ġurūb the maṣdar 'setting of the sun'). Persian keeps the Arabic ġayn غ, which is why the borrowing is transparent — an inherited Iranian word could not begin with ġ. Mo'in flags the entry '[ع.]' (Arabic).\",\n          \"derivation_fa\": \"«غرب» و واژه‌های افزودهٔ نمودار، «مغرب» و «غروب»، هر سه وام‌واژهٔ عربی‌اند که پس از اسلام وارد فارسی نو شده‌اند: غَرْب «باختر»، مَغْرِب اسم مکان و زمان، و غُروب مصدر «فروشدن خورشید». نگه داشتن حرف «غ» خود نشان وام‌بودن است، زیرا واژهٔ ایرانیِ اصیل با غ آغاز نمی‌شود. معین در فرهنگ فارسی این مدخل را با نشانِ «[ع.]» آورده است. ادعای نورایی درست است.\",\n          \"sources\": [W_WT_GHARB],\n          \"ref_check\": [\n            {\"ref\": \"MON\", \"status\": \"supports\", \"note\": \"Mo'in, Farhang-e Farsi s.v. غرب (MON_part2.txt): 'غرب: [ع. غ.] (مصدر لازم) پنهان شدن، غایب گردیدن، ناپدید گشتن، دور شدن. (اِ.) جای فرو شدن آفتاب، مغرب؛ مقابل مشرق' — Arabic origin tag [ع.] and the sense 'place where the sun goes down, west'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"s.v. غرب and غروب (MON_part2.txt lines ~996, 1395)\", \"stance\": \"supports\", \"note\": \"غروب too is tagged '[ع.] (مصل.) فرو شدن' — Arabic infinitive 'to go down'.\"},\n            {\"src\": \"RCH\", \"where\": \"Richardson s.v. gharb\", \"stance\": \"supports\", \"note\": \"'gharb, Sun-set. The west. Africa. The flowing of tears ...' — the word is listed in a Persian-Arabic-English dictionary as an Arabism current in Persian.\"}\n          ]\n        },\n        {\n          \"id\": 3, \"lang\": \"Italian\", \"words\": \"Marocco\", \"verdict\": \"disputed\",\n          \"derivation\": \"Italian Marocco (Sp. Marruecos, Fr. Maroc, Ptg. Marrocos) really is the source of the European name of the country, but it does not come from Arabic maġrib / al-Maġrib al-Aqṣā. It comes from Marrākuš, the Almoravid capital founded in 1070, which from the 12th to the early 20th century gave its name to the whole kingdom ('the Kingdom of Marrakesh'). Phonetically maġrib could not yield Mar(r)occo — there is no route from ġ+b to rr+k. The name Marrākuš itself is Berber, not Arabic: the usual explanation is Tashelhit amur n akuš 'land of God' (Searight records an 11th-c. Qarawiyyin manuscript glossing it 'country of the sons of Kush'). Etymonline repeats Nourai's short-cut ('from Berber Marrakesh ... from Arabic Maghrib-al-Aqsa'), but that last step is a folk equation, not an accepted derivation.\",\n          \"derivation_fa\": \"نام اروپاییِ کشور (ایتالیایی Marocco، اسپانیایی Marruecos، فرانسوی Maroc) در اصل از «مرّاکش» می‌آید، پایتخت مرابطون که در ۱۰۷۰ م. بنیاد شد و از سدهٔ دوازدهم تا آغاز سدهٔ بیستم نامش بر سراسر کشور نهاده می‌شد. از «مغرب» به‌هیچ‌روی نمی‌توان Marocco را گرفت؛ هیچ دگرگونی آواییِ شناخته‌ای غ و ب را به رّ و ک بدل نمی‌کند. خودِ «مرّاکش» هم واژه‌ای بربری است نه عربی: توضیح رایج آن amur n akuš در تاشلحیت به معنی «سرزمین خدا» است. پژوهش امروزی این پیکان نورایی (از ریشهٔ غ‌ر‌ب) را رد می‌کند و به جای آن نام شهر مرّاکش را می‌گذارد.\",\n          \"sources\": [W_ETYM_MOROCCO, W_WP_MARRAKESH],\n          \"ref_check\": [\n            {\"ref\": \"AHD:854\", \"status\": \"not_checked\", \"note\": \"A page of the AHD New College Edition (1975/76) dictionary text, not of the Indo-European appendix; the only AHD on disk here is Watkins 1985 (IE roots only), which has no 'Morocco'. The New College scans on archive.org are lending-only.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"LKT\", \"where\": \"no. 1406 'Ar. Marākuš'\", \"stance\": \"contradicts\", \"note\": \"Lokotsch: 'Ar. Marākuš: Jetzt Marrākeš, die frühere südliche Hauptstadt Marokkos; hiernach wird das Ziegenleder genannt ... pg. marroquim, frz. maroquin ... engl. morocco.' He derives the European words from the CITY NAME and says nothing about maġrib.\"},\n            {\"src\": \"KLN\", \"where\": \"s.v. morocco, marocain (leaves 538, 511)\", \"stance\": \"contradicts\", \"note\": \"'morocco, n., a kind of fine flexible leather. — Named fr. Morocco, a city of NW. Africa' — Klein too anchors the name in the city, not in maġrib al-aqṣā.\"},\n            {\"src\": \"DEV\", \"where\": \"grep 'Maroc' in Devic\", \"stance\": \"silent\", \"note\": \"Devic mentions Maroc only in passing (s.vv. Argan, Filali, Mollah); he gives no etymology of the country name.\"}\n          ]\n        },\n        {\n          \"id\": 4, \"lang\": \"Arabic\", \"words\": \"Marâkeš\", \"verdict\": \"disputed\",\n          \"derivation\": \"The arrow is drawn backwards. Arabic مرّاكش Marrākuš is the ELDER form and the source of Italian Marocco, not a borrowing from it: the city was founded by the Almoravid Abū Bakr ibn ʿUmar in 462/1070 and appears in Arabic geographers from the 11th century, long before any Italian mercantile form. As Lokotsch (no. 1406) puts it, the Romance words marroquim / maroquin / morocco come 'hieraus', i.e. out of the Arabic name. Arabic itself took the name from Berber (amur n akuš 'land of God'), so Marrākuš is a Berberism in Arabic, not an Italianism. The word and its reference are real; only the direction of Nourai's arrow is wrong.\",\n          \"derivation_fa\": \"جهت پیکان وارونه است. «مرّاكش» عربی صورت کهن‌تر و خاستگاه Marocco ایتالیایی است، نه وام‌گرفته از آن: شهر را ابوبکر بن عمرِ مرابطی در ۴۶۲ ق/۱۰۷۰ م. بنیاد نهاد و نامش از همان سدهٔ پنجم در جغرافی‌نویسان عرب آمده است، بسیار پیش از آنکه صورتی ایتالیایی در کار باشد. لوکوچ (شمارهٔ ۱۴۰۶) به‌روشنی می‌گوید واژه‌های رومی (marroquin، maroquin، morocco) «از این» نام عربی برآمده‌اند. عربی خود این نام را از بربری گرفته است. پس واژه درست است ولی سویهٔ اشتقاق در کتاب نادرست است.\",\n          \"sources\": [W_WP_MARRAKESH, W_WT_MARRAKESH],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Nourai gives no reference for this node.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"LKT\", \"where\": \"no. 1406\", \"stance\": \"contradicts\", \"note\": \"'Ar. Marākuš ... hiernach wird das Ziegenleder genannt ... pg. marroquim, frz. maroquin, ndl. marokijn, dtsch. Maroquin; engl. morocco' — Arabic is the source of the European forms, i.e. the reverse of the chart's arrow.\"},\n            {\"src\": \"DEV\", \"where\": \"Devic, s.v. Filali and passim\", \"stance\": \"silent\", \"note\": \"no entry for Marrakesh/Maroc as a headword.\"},\n            {\"src\": \"MON\", \"where\": \"MON_part1/part2 (2-vol Adena lexicon)\", \"stance\": \"silent\", \"note\": \"grep 'مراکش' finds only مراکشی 'Moroccan' and ملخ مراکشی; the proper name itself belongs to Mo'in's aʿlām volumes 5-6, which are not in the local library.\"}\n          ]\n        },\n        {\n          \"id\": 5, \"lang\": \"Persian\", \"words\": \"Marâkeš «مراکش»\", \"verdict\": \"confirmed\",\n          \"derivation\": \"The edge actually drawn here — Arabic Marrākuš > Persian مراکش Marākeš 'Morocco' — is right, and is the only route the Persian word could have taken: Persian took the country's name in its Arabic shape (with the Arabic gemination of the r and the final š), not in the European shape Maroc/Morocco, which is why Persian says مراکش and not *ماروکو. Nourai's own NOTE that MON6:1946 derives it from a different Arabic root is a fair warning: Mo'in's aʿlām volume connects the name to Arabic/Berber material of its own rather than to ġ-r-b, and modern scholarship agrees that the name is Berber (amur n akuš) taken over by Arabic. So the immediate link is sound while the chain above it (Italian > Arabic) is not.\",\n          \"derivation_fa\": \"خودِ این پیوند — «مرّاكش» عربی به «مراکش» فارسی — درست است و تنها راه ممکن هم همین بوده: فارسی نام این کشور را در صورت عربی‌اش گرفته است (با تشدید رِ عربی و شینِ پایانی)، نه در صورت اروپایی Maroc/Morocco؛ به همین سبب در فارسی «مراکش» می‌گوییم نه «ماروکو». یادداشت خودِ نورایی که «معین ج۶ ص۱۹۴۶ آن را از ریشهٔ عربیِ دیگری می‌گیرد» هشدار به‌جایی است: پژوهش امروزی هم این نام را بربری (amur n akuš «سرزمین خدا») می‌داند که از راه عربی به فارسی رسیده است. پس این حلقه درست است، هرچند زنجیرهٔ بالای آن (ایتالیایی ← عربی) نادرست است.\",\n          \"sources\": [W_WP_MARRAKESH],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"No reference given by Nourai for this node; his in-node NOTE cites MON6:1946, which is in Mo'in's aʿlām volume 6 — not among the volumes available on disk or online, so the note itself could not be verified.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"MON_part2.txt line 1075\", \"stance\": \"partial\", \"note\": \"the lexicon volumes have only the nisba مراکشی 'a person from northern Africa; Moroccan', confirming the Arabic shape of the name in Persian; the proper noun is in vol. 6, unavailable.\"},\n            {\"src\": \"LKT\", \"where\": \"no. 1406\", \"stance\": \"supports\", \"note\": \"confirms Marrākuš as the Arabic form of the name, which is what Persian has borrowed.\"}\n          ]\n        },\n        {\n          \"id\": 6, \"lang\": \"English\", \"words\": \"Morocco\", \"verdict\": \"confirmed\",\n          \"derivation\": \"English Morocco is taken from Italian Marocco (attested in English from the 16th century, at first often Marocco/Marroco), the form being later assimilated to Moor/Moorish. The leather sense (morocco, 'sumac-tanned goatskin') is named from the country, exactly as Klein and Lokotsch say; French maroquin, Portuguese marroquim, German Maroquin are the parallel formations. Only the ultimate step of the chart's chain (that Marocco is from maġrib) is wrong; the Italian > English step itself is standard.\",\n          \"derivation_fa\": \"انگلیسی Morocco از ایتالیایی Marocco گرفته شده و از سدهٔ شانزدهم در انگلیسی دیده می‌شود (نخست بیشتر به صورت Marocco/Marroco) و بعدها زیر تأثیر Moor «مورِ مسلمان» شکل امروزی را یافته است. معنی «چرم بزِ دباغی‌شده» نیز از نام کشور آمده، همان‌گونه که کلاین و لوکوچ می‌گویند؛ maroquin فرانسوی و marroquim پرتغالی هم‌ساخت‌های آن‌اند. تنها حلقهٔ آغازینِ زنجیرهٔ نورایی (مغرب ← Marocco) نادرست است و همین گام ایتالیایی به انگلیسی پذیرفتنی است.\",\n          \"sources\": [W_ETYM_MOROCCO],\n          \"ref_check\": [\n            {\"ref\": \"AHD:854\", \"status\": \"not_checked\", \"note\": \"AHD New College Edition dictionary page; only Watkins 1985 (IE roots) is on disk, and the New College scans are lending-only.\"},\n            {\"ref\": \"NAT:163\", \"status\": \"partial\", \"note\": \"Berlitz, Native Tongues, in the table of country-name meanings (NAT_2005.txt leaf 182, printed p. 167 of the 2005 reprint = p. 163 of the 1982 original): 'Morocco | maghrib, \\\"the west\\\"'. Berlitz gives the popular maghrib equation Nourai relies on, but it is a one-line popular list, not an etymological argument.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"s.v. morocco (leaf 538)\", \"stance\": \"supports\", \"note\": \"'morocco, n., a kind of fine flexible leather. — Named fr. Morocco, a city of NW. Africa, where this kind of leather was originally made.'\"},\n            {\"src\": \"LKT\", \"where\": \"no. 1406\", \"stance\": \"supports\", \"note\": \"'engl. morocco \\\"feines dünnes marokkanisches Leder\\\"' derived from Ar. Marākuš.\"},\n            {\"src\": \"WEB\", \"where\": \"Webster's New Twentieth Century, vol. 1 s.v. fez\", \"stance\": \"silent\", \"note\": \"vol. 1 stops before M; only incidental mentions of Morocco were found.\"}\n          ]\n        },\n        {\n          \"id\": 7, \"lang\": \"Hebrew\", \"words\": \"`erebh\", \"verdict\": \"plausible\",\n          \"derivation\": \"Hebrew עֶרֶב ʿereb 'evening, sunset' (and maʿarāb 'west', the Hiphʿil participle maʿarīb 'bringing on evening' = the evening prayer) is a real word with the meaning given. It is genuinely of the same Semitic root as Akkadian erēbu, but as a cognate, not as a loan: Proto-Semitic *ġ merged with *ʿ in Hebrew, so *ġereb regularly gives ʿereb, while Akkadian, which lost the gutturals altogether, shows erēbu; Arabic ġarb preserves the original ġ and proves the reconstruction. Klein s.v. maarib puts it exactly this way ('is rel. to'), and Zimmern hedges his loan-arrow with 'viell.' The chart's second gloss 'west' is by extension (maʿarāb), not the primary meaning of ʿereb, which is 'evening'.\",\n          \"derivation_fa\": \"عبری עֶרֶב ʿereb «شامگاه، غروب» (و maʿarāb «باختر») واژه‌ای واقعی با همین معناست و به‌راستی از همان ریشهٔ سامیِ erēbu اکدی است، اما به‌عنوان هم‌ریشه نه وام‌واژه: در عبری غین سامی با عین یکی شده و *ġereb به‌قاعده ʿereb داده، حال آنکه اکدی حروف حلقی را یکسره از دست داده و erēbu شده است؛ غَرْب عربی با نگه‌داشتن غین همین بازسازی را ثابت می‌کند. کلاین نیز در مدخل maarib همین را می‌گوید («هم‌ریشه است») و تسیمرن پیکان وام‌گیری را با «شاید» آورده است. معنای دومِ نمودار، «باختر»، معنای گستردهٔ maʿarāb است نه معنای اصلی ʿereb که «شامگاه» است.\",\n          \"sources\": [W_ETYM_EUROPE],\n          \"ref_check\": [\n            {\"ref\": \"AKD:64\", \"status\": \"supports\", \"note\": \"Zimmern p. 64: '... : > viell., dann allerdings schon [früh], hebr. ʿāreb Abend' — the arrow is there, but hedged.\"},\n            {\"ref\": \"KLN:550\", \"status\": \"partial\", \"note\": \"Klein s.v. maarib (KLN_1966.txt leaf 493): 'Heb. maʿarībh ... denominated fr. ʿerebh, \\\"sunset, evening\\\", which is rel. to Arab. gharaba, Ethiop. ʿaraba, \\\"(the sun) has set\\\", Arab. gharb, \\\"place of sunset, west\\\", Akkad. erebu, \\\"to enter, go in\\\", ereb shamshi, \\\"sunset\\\".' — 'rel. to', i.e. cognate, so Klein supports the family but not the descent.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"s.vv. maarib, Erebus (leaves 493, 292)\", \"stance\": \"partial\", \"note\": \"s.v. Erebus: 'Gk. Erebos, fr. Heb. ʿerebh, \\\"sunset, evening\\\"' — Klein does allow Greek borrowings from Hebrew ʿerebh, but treats the Semitic words themselves as cognates.\"},\n            {\"src\": \"AKD\", \"where\": \"printed p. 64\", \"stance\": \"partial\", \"note\": \"Zimmern's whole section is about Akkadian influence, so the arrow is his thesis; the 'viell.' shows he did not regard it as proven.\"},\n            {\"src\": \"FVQ\", \"where\": \"grep of Jeffery for ʿarb/ġarb\", \"stance\": \"silent\", \"note\": \"The Foreign Vocabulary of the Qur'an treats loans INTO Arabic; it has nothing on ġ-r-b, which it regards as native.\"}\n          ]\n        },\n        {\n          \"id\": 8, \"lang\": \"Greek\", \"words\": \"europa\", \"verdict\": \"disputed\",\n          \"derivation\": \"That Greek Εὐρώπη is a borrowing of Semitic ʿereb/erēbu 'sunset' is a 19th-century proposal (Heinrich Lewy, Die semitischen Fremdwörter im Griechischen, 1895, pp. 139-140), which Klein repeats and Nourai follows; Hesychius' gloss chōra tēs dyseōs 'land of the setting sun' is the ancient support usually cited. Modern scholarship rejects it: M. L. West concluded that 'phonologically, the match between Europa's name and any form of the Semitic word is very poor' — Semitic ʿ-r-b gives no source for the -ōp- and the Greek diphthong eu-; and Beekes, who is the current authority on the Greek lexicon, considers a Semitic connection improbable and treats Eurṓpē as Pre-Greek, i.e. from the pre-Indo-European substrate, alongside the old native folk-etymology eurýs 'wide' + ṓps 'face' ('broad-faced'), which is itself a Grecising reshaping. Wiktionary and Etymonline both label the origin uncertain. Nourai gives the Semitic account as fact and adds a gloss ('land of sunset') that is Hesychius' explanation, not the word's demonstrated meaning.\",\n          \"derivation_fa\": \"این‌که Εὐρώπη یونانی وام‌واژه‌ای از ʿereb سامی یا erēbu اکدی به معنی «غروب» باشد، پیشنهادی از سدهٔ نوزدهم است (هاینریش لِوی، ۱۸۹۵، ص ۱۳۹–۱۴۰) که کلاین آن را بازگفته و نورایی از او گرفته است؛ گواهِ کهنِ همیشگی‌اش هم تفسیر هسیخیوس است: «سرزمین خورشیدِ فرورونده». اما پژوهش امروزی آن را رد می‌کند: مارتین وست می‌گوید سازگاری آوایی میان نام Europa و هیچ صورتی از آن واژهٔ سامی بسیار ضعیف است (ریشهٔ ع‌ر‌ب نه -ōp- را توضیح می‌دهد نه دوواکهٔ eu- را) و بیکس، مرجع امروزیِ واژگان یونانی، پیوند سامی را نامحتمل می‌شمارد و Eurṓpē را واژه‌ای پیشایونانی (بازماندهٔ زیرلایهٔ پیشاهندواروپایی) می‌داند؛ ریشه‌شناسیِ عامیانهٔ یونانیِ eurýs «پهن» + ṓps «چهره» هم بازسازیِ ثانویِ خودِ یونانیان است. حکم: پژوهش امروزی ادعای نورایی را رد می‌کند.\",\n          \"sources\": [W_WP_EUROPE, W_ETYM_EUROPE, W_WT_EUROPA],\n          \"ref_check\": [\n            {\"ref\": \"KLN:550\", \"status\": \"supports\", \"note\": \"Klein s.v. Europe (leaf 299) states precisely Nourai's claim and cites 'Heinrich Lewy, Die semitischen Fremdwörter im Griechischen, Berlin, 1895, pp. 139-140' and Hesychius — but Klein himself writes only 'prob. of Semitic origin'.\"},\n            {\"ref\": \"AHD:452\", \"status\": \"not_checked\", \"note\": \"AHD New College Edition dictionary page (the entry 'Europe'), not the IE appendix; the local AHD file is Watkins 1985 (roots only) and the New College scans are lending-only.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"s.v. Europe, Erebus (leaves 299, 292)\", \"stance\": \"supports\", \"note\": \"the source of Nourai's arrow, hedged with 'prob.'\"},\n            {\"src\": \"AKD\", \"where\": \"grep of Zimmern for 'Europa'\", \"stance\": \"silent\", \"note\": \"Zimmern discusses erēbu > Semitic 'west' words but does not mention Europa at all, so AKD does not back the Greek step.\"},\n            {\"src\": \"PEI\", \"where\": \"Pei, The Families of Words\", \"stance\": \"silent\", \"note\": \"no entry found on the name Europe.\"}\n          ]\n        },\n        {\n          \"id\": 9, \"lang\": \"Latin\", \"words\": \"eurôpa\", \"verdict\": \"confirmed\",\n          \"derivation\": \"Latin Eurōpa is a straight learned borrowing of Greek Εὐρώπη / Doric Εὐρώπα, taken over with the Doric long -ā as usual for Greek proper names entering Latin (cf. Asia, Africa), and used both of the Phoenician princess of the myth and, from Ennius and the geographers onwards, of the continent. The step is uncontroversial whatever the ultimate origin of the Greek name.\",\n          \"derivation_fa\": \"لاتینی Eurōpa وام‌گیری مستقیم و کتابیِ Εὐρώπη یونانی (صورت دُریِ Εὐρώπα) است و مانند دیگر نام‌های خاصِ یونانی با ـā کشیدهٔ دُری به لاتین رفته است (سنجید با Asia، Africa)؛ هم بر شاهدختِ اسطوره‌ای فنیقی به کار می‌رفته و هم، از انیوس و جغرافی‌نویسان به بعد، بر قاره. این حلقه، جدا از این‌که خاستگاه نهاییِ نام یونانی چه باشد، بی‌مناقشه است.\",\n          \"sources\": [W_WT_EUROPA],\n          \"ref_check\": [\n            {\"ref\": \"AHD:452\", \"status\": \"not_checked\", \"note\": \"AHD New College dictionary page, not available (see node 8).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"s.vv. Europa, Europe (leaf 299)\", \"stance\": \"supports\", \"note\": \"'Europa, n., a daughter of Agenor, king of Phoenicia (Greek mythol.) — L., fr. Gk. Eurṓpē'; 'Europe, n. — L. Europa, fr. Gk. Eurṓpē'.\"},\n            {\"src\": \"LEW\", \"where\": \"Walde, Lateinisches etymologisches Wörterbuch\", \"stance\": \"silent\", \"note\": \"proper names of this kind are not treated in Walde's dictionary.\"}\n          ]\n        },\n        {\n          \"id\": 10, \"lang\": \"French\", \"words\": \"Europe\", \"verdict\": \"confirmed\",\n          \"derivation\": \"French Europe continues Latin Eurōpa as a learned (non-popular) form: it is attested from Old French onwards in translations of Latin geography, with the regular learned treatment of Latin -pa > -pe and no trace of the sound changes a popular inheritance would have produced. It is the form from which most modern European and, in turn, Near Eastern languages took the name.\",\n          \"derivation_fa\": \"فرانسوی Europe دنبالهٔ لاتینی Eurōpa است، اما به‌صورت واژهٔ عالمانه نه موروثی: از فرانسویِ کهن در ترجمه‌های جغرافیای لاتینی دیده می‌شود و پایانهٔ ‑pa لاتینی به‌شیوهٔ واژه‌های عالمانه به ‑pe بدل شده و هیچ‌یک از دگرگونی‌های آواییِ واژه‌های موروثی در آن رخ نداده است. همین صورت فرانسوی است که بیشتر زبان‌های اروپایی و سپس زبان‌های خاور نزدیک نام قاره را از آن گرفته‌اند.\",\n          \"sources\": [W_WT_EUROPA],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Nourai gives no reference for this node.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"s.v. European (leaf 299)\", \"stance\": \"supports\", \"note\": \"'European, adj. and n. — F. européen, fr. L. Europaeus, fr. Gk. Eurōpaios' — Klein routes the English adjective through French, presupposing F. Europe.\"},\n            {\"src\": \"DEV\", \"where\": \"Devic, Dictionnaire étymologique des mots français d'origine orientale\", \"stance\": \"silent\", \"note\": \"Europe is not among Devic's oriental-origin French words.\"}\n          ]\n        },\n        {\n          \"id\": 11, \"lang\": \"Persian\", \"words\": \"«اروپا»\", \"verdict\": \"confirmed\",\n          \"derivation\": \"Persian اروپا Orupā/Urupā is a modern European loan of the Qajar period, and French is the right source: the Persian vowels reproduce French Europe [øʁɔp] — the initial ö of French, which Persian has no letter for, is written with alef + vāv (ارو-), and the final -pe is heard as -pā. A borrowing from Latin or English would have given something like *ایوروپ / *یوروپ; a Russian source would have given *یوروپا with initial y-. French was in fact the language of the first Persian geography textbooks and of the Dar al-Funun curriculum, which is where the name entered Persian, displacing the older فرنگ Farang for 'Europe'.\",\n          \"derivation_fa\": \"«اروپا» وام‌واژه‌ای نوین از دورهٔ قاجار است و منبع آن، چنان‌که نورایی نشان داده، فرانسوی است: واکه‌های فارسی بازتاب تلفظ فرانسوی Europe اند — واکهٔ ö آغازین که در فارسی حرفی برای آن نیست با «ارو» نوشته شده و پایانهٔ ‑pe به «‑پا» شنیده شده است. اگر از لاتین یا انگلیسی گرفته شده بود صورتی مانند «ایوروپ/یوروپ» می‌داشتیم و اگر از روسی، «یوروپا» با یِ آغازین. زبان کتاب‌های نخستینِ جغرافیا و برنامهٔ دارالفنون فرانسوی بود و همان‌جا این نام جای واژهٔ کهن‌تر «فرنگ» را گرفت. ادعای نورایی درست است.\",\n          \"sources\": [W_WT_EUROPA],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Nourai gives no reference for this node.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"MON_part1.txt line 10276, s.v. اروپایی\", \"stance\": \"partial\", \"note\": \"'اروپایی: (ص‌نسب.) منسوب به اروپا. هر چیز که در اروپا سازند و از اروپا آورند' — Mo'in's lexicon volumes carry only the nisba; the proper noun اروپا itself is in the aʿlām volumes, which are not on disk, so Mo'in's origin tag (expected [فر.] = French) could not be read.\"},\n            {\"src\": \"ARY\", \"where\": \"Aryanpur, grep 'اروپا' in ARY_pages.txt\", \"stance\": \"silent\", \"note\": \"occurrences are all the ordinary use of the continent's name in running text; Aryanpur treats Indo-European roots, not modern European loans.\"}\n          ]\n        },\n        {\n          \"id\": 12, \"lang\": \"English\", \"words\": \"Europe\", \"verdict\": \"confirmed\",\n          \"derivation\": \"English Europe is from Latin Eurōpa, in practice through French Europe (Klein routes the derivative European through French européen < L. Europaeus). It is attested in English from the late Middle English period in geographical writing and displaced Old English Europe/Europa forms taken directly from Latin. The chart's arrow Latin > English is thus right in substance, with French as the usual intermediary.\",\n          \"derivation_fa\": \"انگلیسی Europe از لاتینی Eurōpa آمده است، در عمل از راه فرانسوی Europe (کلاین صفتِ European را از européen فرانسوی < Europaeus لاتینی می‌گیرد). این نام از پایان دورهٔ انگلیسی میانه در نوشته‌های جغرافیایی به کار رفته است. پس پیکانِ «لاتین ← انگلیسی» در جوهر درست است، با این افزوده که میانجیِ معمول، فرانسوی بوده است.\",\n          \"sources\": [W_ETYM_EUROPE],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"not_checked\", \"note\": \"Citation without a page; the AHD New College dictionary text is not on disk and the scans are lending-only.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"s.vv. Europe, European, europium (leaf 299)\", \"stance\": \"supports\", \"note\": \"'Europe, n. — L. Europa, fr. Gk. Eurṓpē'; 'European, adj. and n. — F. européen, fr. L. Europaeus'.\"},\n            {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etymological Dictionary\", \"stance\": \"silent\", \"note\": \"Skeat's Concise has no entry for Europe (grep -i 'europe' returns only incidental occurrences).\"}\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 1,\n      \"root\": \"Ered, Erdh, Weredh, Werdh\",\n      \"verdict\": \"plausible\",\n      \"modern_form\": \"two roots, not one: PIE *h₃erdʰ- 'high, upright' (Pokorny er(ə)d-, er(ə)dh- 'hoch; wachsen', IEW 339) and PIE *h₁werdʰ- 'to grow' (Pokorny u̯erdh-, u̯redh- 'wachsen, steigen; hoch', IEW 1167)\",\n      \"note\": \"All four of Nourai's root shapes are real Pokorny headwords and both cited pages are exactly right: IEW 339 has 'er(ə)d- (ṛ(ə)d-), er(ə)dh- \\\"hoch; wachsen\\\"' with Av. ərəδwa- 'hoch', Lat. arduus, OIr. ard, Alb. rit, Slav. rastǫ; IEW 1167 has 'u̯erdh-, u̯redh- \\\"wachsen, steigen; hoch\\\"' with Skt. várdhati, ūrdhvá-, Av. varəd-, Gk. orthós. Two caveats. (a) Pokorny himself keeps the two entries apart, 828 pages apart, and modern handbooks keep them apart too: *h₃erdʰ- gives the 'high' words (Skt. ūrdhvá-, Av. ərəδwa-, Lat. arduus, Gk. orthós per Beekes/Wiktionary) and *h₁werdʰ- the 'grow' words (Skt. vardhati, Av. varəd-, MP wālīdan > NP bālīdan). Nourai's single box, glossed 'to grow, high', merges them; the merger is Pokorny's own suggestion at IEW 339 ('verschiedene Erweiterungen von er- durch dh') but is not the current view. (b) In consequence Greek orthós (node 6) hangs from the box by whichever of the two roots one prefers — Watkins puts it under wrēdh- (Pok. 1167), Beekes under *h₃r̥dʰwós — so the node is safe either way. Nothing on this chart is a transcription problem; the Persian script, the Sanā'ī and Ṭayyān verses and all references match the printed page.\",\n      \"note_fa\": \"هر چهار صورتی که نورایی برای ریشه آورده مدخل‌های واقعیِ پوکورنی‌اند و هر دو شمارهٔ صفحه هم دقیقاً درست است: در ص ۳۳۹ فرهنگ ریشه‌شناختیِ پوکورنی مدخل er(ə)d-، er(ə)dh- «بلند؛ رشد کردن» با ərəδwa- اوستایی، arduus لاتینی، ard ایرلندی و rastǫ اسلاوی آمده و در ص ۱۱۶۷ مدخل u̯erdh-، u̯redh- «رشد کردن، بالا رفتن؛ بلند» با várdhati و ūrdhvá- سنسکریت، varəd- اوستایی و orthós یونانی. دو نکته: نخست آنکه خود پوکورنی این دو را دو ریشهٔ جدا می‌داند و ریشه‌شناسی امروزی نیز آن‌ها را جدا نگاه می‌دارد — *h₃erdʰ- «بلند» در برابر *h₁werdʰ- «رشد کردن» — و یکی‌کردن آن‌ها در یک جعبه، هرچند اشاره‌ای از خودِ پوکورنی پشتوانهٔ آن است، دیدگاه امروزی نیست. دوم آنکه orthós یونانی به هر دو تحلیل باز به همین مجموعه می‌رسد، پس گره ششم در هر حال درست است. هیچ خطای خوانشِ اسکنی در این نمودار نیست؛ املای فارسی، بیت‌های سنایی و طیّان و همهٔ ارجاع‌ها با صفحهٔ چاپی می‌خوانند.\",\n      \"sources\": [W_WT_ORTHOS],\n      \"ref_check\": [\n        {\"ref\": \"POK:339\", \"status\": \"supports\", \"note\": \"Pokorny IEW p. 339-340 (POK_01.txt leaf 353): 'er(ə)d- (ṛ(ə)d-), er(ə)dh- \\\"hoch; wachsen\\\". Av. ərəδva- \\\"hoch\\\"; lat. arduus \\\"hoch, steil\\\"; gall. Arduenna silva, air. ard (*ṛduo-) \\\"hoch, groß\\\" ... alb. rit \\\"wachse\\\" ... slav. *orstǫ, abg. rastǫ ... \\\"wachse\\\".' Exactly the root name, language label and gloss of the chart.\"},\n        {\"ref\": \"POK:1167\", \"status\": \"supports\", \"note\": \"Pokorny IEW p. 1167 (POK_03.txt, page marker '1167'): 'u̯erdh-, u̯redh- \\\"wachsen, steigen; hoch\\\". Ai. várdhati, várdhate ... vṛddhá- \\\"erwachsen, groß, alt\\\"; av. varəd- \\\"wachsen machen\\\"; ai. ūrdhvá- \\\"hoch\\\" (*u̯ordh-u̯o-) ... gr. orthós, dor. borthó- \\\"aufrecht, gerade, richtig, wahr\\\" (*u̯ordh-u̯o-).'\"},\n        {\"ref\": \"KLN:1097\", \"status\": \"supports\", \"note\": \"Klein s.v. ortho- (KLN_1966.txt leaf 587): 'Gk. orthós, \\\"straight; right, true, exact; genuine; upright, righteous\\\", for *worthwos (cp. Dor. borthó-); cognate with OI. ūrdhvaḥ, \\\"high\\\", várdhate, \\\"causes to grow\\\", L. arduus, \\\"high, lofty, steep\\\".' Klein combines both of Pokorny's roots in exactly the way Nourai's box does.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"WLD\", \"where\": \"Walde-Pokorny Bd. I (WLD_Bd1_pages.txt lines 7616, 13487)\", \"stance\": \"supports\", \"note\": \"the older Walde-Pokorny already links 'ai. ūrdhva-' with Gk. orthós and cross-refers 's. u̯eredh-', i.e. the same double treatment.\"},\n        {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.vv. ered-, wrēdh-\", \"stance\": \"partial\", \"note\": \"'ered-. High. Suffixed zero-grade form *ṛd-wo- in Latin arduus, high, steep: ARDUOUS. [Pok. er(e)d- 339.]' and 'wrēdh-. To grow straight, upright. Suffixed zero-grade form *wrodh-wo- in Greek orthos ...: ORTHO-. [In Pok. werdh- 1167.]' — Watkins keeps them as two separate roots, as the modern view does.\"},\n        {\"src\": \"IEC\", \"where\": \"Mann, s.v. ueldho (col. corresponding to IEC.txt line 19951)\", \"stance\": \"partial\", \"note\": \"'ueldho \\\"grow strong, thrive, succeed\\\" ... Skt. várdhāmi ... Av. varəd-, tr. \\\"promote\\\" ... (? uerdh-, urdh-)' — Mann files the 'grow' family under *ueldh- and marks *uerdh- with a query, a third opinion again distinct from Nourai's single root.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1, \"lang\": \"Avestan\", \"words\": \"eredva; vared, vard, ward\", \"verdict\": \"plausible\",\n          \"derivation\": \"Both Avestan items exist, but they belong to the two different roots the chart has merged. (i) ərəδwa- 'high, upright' is well attested in Younger Avestan compounds — ərəδwa-fštāna- 'with upright breasts' (Hādōxt Nask 2.9), ərəδwō.drafša- 'with the banner raised high' (Yt. 1.11), ərəδwō.zaṇga- 'upright of ankle' (Yt. 10.61) — and Bartholomae's note at AiW col. 351 derives it 'aus ar. *ṛ-dh-wa-, vgl. ai. ūrdhvá- ... oder lat. arduus', i.e. from PIE *h₃erdʰ-. (ii) varəd- is the Avestan verb 'to make grow, to increase' (AiW col. 1369: 'varəd- V. \\\"augere\\\", Praes. varəda-, ... \\\"wachsen machen, gedeihen lassen, mehren\\\"'), matching Skt. várdhati and PIE *h₁werdʰ-. Nourai's Latin transliterations 'vared, vard, ward' are the stem varəd- with the schwa written out and with the w/v spelling variants; his gloss 'up, high, growing' compresses the two roots' senses. The forms are real; the implication that ərəδwa- and varəd- come from one and the same root is Pokorny's guess, not modern doctrine.\",\n          \"derivation_fa\": \"هر دو صورت اوستایی واقعی‌اند، ولی به دو ریشهٔ جداگانه‌ای تعلق دارند که نورایی در یک جعبه ادغام کرده است. نخست ərəδwa- «بلند، برافراشته» که در ترکیب‌های اوستایی متأخر فراوان است — ərəδwa-fštāna- «سینه‌برافراشته» (هادُخت نسک ۲٫۹)، ərəδwō.drafša- «درفش‌برافراشته» (یشت ۱٫۱۱)، ərəδwō.zaṇga- «برپای‌ایستاده» (یشت ۱۰٫۶۱) — و بارتولومه در ستون ۳۵۱ فرهنگ ایرانی باستان آن را از آریایی *ṛ-dh-wa- می‌گیرد و با ūrdhvá- سنسکریت و arduus لاتینی می‌سنجد، یعنی از *h₃erdʰ-. دوم varəd- که فعل اوستایی «رویاندن، افزودن» است (ستون ۱۳۶۹: «augere… رشد دادن، بالیدن‌دادن، افزودن») و برابر várdhati سنسکریت از *h₁werdʰ-. آوانوشت‌های نورایی («vared, vard, ward») همان ستاک varəd- اند. پس صورت‌ها درست‌اند، اما یکی‌دانستن این دو، گمانِ پوکورنی است نه دیدگاه امروزی.\",\n          \"sources\": [W_WT_ORTHOS],\n          \"ref_check\": [\n            {\"ref\": \"POK:339\", \"status\": \"supports\", \"note\": \"IEW 339: 'er(ə)d- ... er(ə)dh- \\\"hoch; wachsen\\\". Av. ərəδva- \\\"hoch\\\"' — literally Nourai's Avestan eredva 'high'.\"},\n            {\"ref\": \"POK:1167\", \"status\": \"supports\", \"note\": \"IEW 1167: 'av. varəd- \\\"wachsen machen\\\"' — literally Nourai's vared/vard 'growing'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"Bartholomae, AiW cols. ~351 and 1369\", \"stance\": \"supports\", \"note\": \"col. 351 note: 'Aus ar. *ṛ-dh-wa-; vgl. ai. ūrdhvá- Adj. ... oder lat. arduus'; col. 1369: 'varəd- V. \\\"augere\\\". Praes. varəda- ... \\\"wachsen machen, gedeihen lassen, (grösser) machen, mehren\\\"'. Both Avestan items confirmed, and Bartholomae too separates them.\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.vv. ered-, wrēdh-\", \"stance\": \"partial\", \"note\": \"confirms both roots but as two, not one.\"},\n            {\"src\": \"AVG\", \"where\": \"Jackson, Avesta Grammar\", \"stance\": \"silent\", \"note\": \"a grammar, not a lexicon; no entry for either stem.\"}\n          ]\n        },\n        {\n          \"id\": 2, \"lang\": \"Persian\", \"words\": \"vâlâ «والا»; bâlîdan «بالیدن»\", \"verdict\": \"confirmed\",\n          \"derivation\": \"Both Persian words go back to the *werdʰ- half of the root, through Middle Persian, exactly as drawn. Old Iranian *warda-ya- 'to make grow' (the causative-type stem of *ward-, Av. varəd-) gives Middle Persian wālīdan, wāl- — MacKenzie's Concise Pahlavi Dictionary has it verbatim: 'wālīdan, wāl- [wʾl-ytn' | N bālīdan] grow, increase, prosper; ~išn: growth'. The Old Iranian cluster -rd- regularly becomes -l- in Middle Persian (cf. *ward > wāl), and Middle Persian initial w- splits in New Persian: it hardens to b- in بالیدن bālīdan and stays as v- in the doublet والا vālā, so the two are two treatments of one Middle Persian word. Wiktionary states this outright for والا: from Middle Persian wāl-īdan 'to grow, to prosper', 'doublet of بالا (bālā), derived with the same suffix from a different form of the same verb'. Horn no. 173 gives 'bālīden \\\"wachsen, zunehmen\\\" (Šāhn. I p.3 v.49), bāliš \\\"Wachstum\\\"' and cross-refers to guwālīden (no. 939); Hübschmann no. 173 adds the Pahlavi causative 'zu phl. caus. wālēnītan ... = zd. varədaya- \\\"wachsen machen\\\"'. Mo'in's footnote in Borhān-e Qāṭeʿ derives بالیدن from Old Indic vardh- 'to grow'. Abolqāsemi (FFD p. 35) writes 'بال < فارسی میانه wāl < ایرانی باستان *ward(a)ya-'. The chart's extras بال ۲ and بالش ۲ are the deverbal noun 'growth' — correctly kept apart from بالش ۱ 'pillow' (< Av. barəziš-), which is what Nourai's cross-reference to root 'Bhel' is about, and Horn indeed treats بالش 'Kissen' separately at no. 172. The gloss 'boast' for bālīdan is the ordinary Persian idiom بالیدن به 'to pride oneself on', a natural extension of 'to grow, swell'.\",\n          \"derivation_fa\": \"هر دو واژهٔ فارسی از نیمهٔ *werdʰ- این ریشه و از راه فارسی میانه آمده‌اند، درست همان‌گونه که نورایی کشیده است. ایرانی باستان *warda-ya- «رویاندن» (ستاکِ سببیِ *ward-، اوستایی varəd-) در فارسی میانه wālīdan/wāl- شده است؛ مکنزی در فرهنگ کوچک پهلوی عیناً می‌آورد: «wālīdan, wāl- ... N bālīdan: رشد کردن، افزودن، کامیاب شدن». خوشهٔ -rd- ایرانی باستان در فارسی میانه به‌قاعده به «ل» بدل می‌شود و «و» آغازیِ فارسی میانه در فارسی نو دو سرنوشت می‌یابد: در «بالیدن» به «ب» سخت می‌شود و در دوگانهٔ آن «والا» همان «و» می‌ماند؛ پس این دو، دو پرداختِ یک واژهٔ واحدِ پهلوی‌اند. ویکی‌واژه نیز «والا» را از wāl-īdan فارسی میانه و «دوگانهٔ بالا» می‌داند. هرن (شمارهٔ ۱۷۳) «بالیدن: رشد کردن، افزودن (شاهنامه ج۱ ص۳ بیت ۴۹)» را با ارجاع به «گوالیدن» آورده و هوبشمان همان شماره را با سببیِ پهلوی wālēnītan = varədaya- اوستایی کامل می‌کند. معین در حاشیهٔ برهان قاطع بالیدن را به vardh- هندی باستان می‌رساند و ابوالقاسمی (فعل‌های فارسی دری، ص ۳۵) می‌نویسد: «بال < فارسی میانه wāl < ایرانی باستان *ward(a)ya-». «بال ۲» و «بالش ۲» همان اسم‌مصدرِ «رشد» است و به‌درستی از «بالش ۱» به معنی متکا (< barəziš- اوستایی) جدا شده است. ادعای نورایی درست است.\",\n          \"sources\": [W_WT_VALA],\n          \"ref_check\": [\n            {\"ref\": \"HRN:39\", \"status\": \"supports\", \"note\": \"Horn, Grundriss der neupersischen Etymologie p. 39 (HRN.txt leaf 61) no. 173: 'bālīden \\\"wachsen, zunehmen\\\" (Šāhn. I, S. 3 Vers 49), bāliš \\\"Wachstum\\\"; vergl. guwālīden (No. 939).' Horn's footnote there even quotes the same Sanāʾī couplet Nourai prints in this node ('tā ki nišest ḫwāja der bāliš / bāliš āmed ze nāz der bāliš').\"},\n            {\"ref\": \"HRN:210\", \"status\": \"supports\", \"note\": \"Horn p. 210 no. 939 is the cross-referenced guwālīden entry (see node 4).\"},\n            {\"ref\": \"BQT:227\", \"status\": \"supports\", \"note\": \"Borhān-e Qāṭeʿ, ب section (BQT_v1_pages.txt leaf 448) s.v. بالیدن 'بروزن مالیدن؛ بمعنی بزرگ شدن و افزون گردیدن و نمو کردن باشد', with Moʿin's footnote: 'هندی قدیم wardh-, vardh- (نمو کردن، بزرگ شدن) ... رک: بالش، بالا' — the same derivation Nourai draws.\"},\n            {\"ref\": \"BQT:1848\", \"status\": \"supports\", \"note\": \"the گوالیدن page (see node 4), where Moʿin's footnote explicitly says 'قس: بالیدن'.\"},\n            {\"ref\": \"FFD:35\", \"status\": \"supports\", \"note\": \"Abolqāsemi, Feʿlhā-ye Fārsi-ye Darī p. 35 (FFD_pages.txt, pdf p. 40, header 'ماده‌های ماضی و مضارع فارسی دری ۳۵'), s.v. بالیدن: 'بال < فارسی میانه wāl < ایرانی باستان *ward(a)ya-. wardā صورت بالاندهٔ ریشهٔ ward است به معنی «رشد کردن».'\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"MacKenzie, Concise Pahlavi Dictionary s.v. wālīdan\", \"stance\": \"supports\", \"note\": \"\\\"wālīdan, wāl- [wʾl-ytn' | N bālīdan] grow, increase, prosper. ~išn: growth\\\" — the Middle Persian link Nourai's chart skips over.\"},\n            {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien p. 24, no. 173\", \"stance\": \"supports\", \"note\": \"'Np. bālīdan \\\"wachsen\\\" zu phl. caus. wālēnītan Phl. Vend. 9 ... = zd. varədaya- \\\"wachsen machen\\\", Mann-Andreas, ZDMG. 47, 702.'\"},\n            {\"src\": \"MON\", \"where\": \"Moʿin, Farhang-e Fārsi s.vv. بالیدن، بالش\", \"stance\": \"supports\", \"note\": \"the lexicon has بالیدن 'نمو کردن، رشد کردن' with the same Pahlavi transcription; Moʿin's own footnote in Borhān is the fuller statement quoted above.\"},\n            {\"src\": \"HRN\", \"where\": \"Horn no. 171 bālā, no. 172 bāliš\", \"stance\": \"partial\", \"note\": \"Horn derives بالا 'hoch' from Av. barəzah- and بالش 'Kissen' from Av. barəziš- — i.e. from *bʰerǵʰ-, NOT from this root. That is precisely why Nourai's NOTE sends the reader to root 'Bhel' for bāleš 1 'pillow'; the note is well judged, though Horn's source for the pillow is barəziš- rather than *bhel-.\"}\n          ]\n        },\n        {\n          \"id\": 3, \"lang\": \"Avestan / Sanskrit\", \"words\": \"vi-vard\", \"verdict\": \"confirmed\",\n          \"derivation\": \"The compound is the preverb *wi- 'apart, out' (Av. vī-, OP viy-, Skt. vi-, from PIE *wi- 'apart') prefixed to the root *ward- / vardh- 'to grow', giving 'to grow out, grow up, thrive'. Sanskrit ví-vardhate is well attested in this sense, and Horn cites the Indic compound directly as the etymon of the Persian verb: 'ai. vi + √vardh- \\\"heranwachsen, gedeihen\\\"'. Avestan has the same preverb freely with varəd- (Bartholomae AiW col. 1369 lists varəd- with preverbs). Pokorny 1167 gives the root; the compound as such is a normal Indo-Iranian formation rather than a reconstructed novelty, so the node is sound. The chart's ☞Wi cross-reference to Nourai's root 'Wi' is the right place for the prefix.\",\n          \"derivation_fa\": \"این ترکیب از پیشوندِ *wi- «جدا، بیرون» (اوستایی vī-، پارسی باستان viy-، سنسکریت vi-) و ریشهٔ *ward-/vardh- «رشد کردن» ساخته شده و معنای «بیرون رُستن، برآمدن، بالیدن» می‌دهد. در سنسکریت ví-vardhate به همین معنا نیک گواهی شده و هرن همین ترکیب هندی را یکراست ریشهٔ فعل فارسی می‌شمارد: «ai. vi + √vardh- (بالیدن، بالنده شدن)». در اوستایی نیز varəd- با همین پیشوند به کار می‌رود (بارتولومه، ستون ۱۳۶۹). پس این گره درست است و ارجاعِ نمودار به ریشهٔ «Wi» برای پیشوند هم بجاست.\",\n          \"sources\": [W_WT_ORTHOS],\n          \"ref_check\": [\n            {\"ref\": \"POK:1167\", \"status\": \"supports\", \"note\": \"IEW 1167 s.v. u̯erdh-, u̯redh-: 'Ai. várdhati, várdhate, vṛdháti \\\"wächst, mehrt sich\\\" ... av. varəd- \\\"wachsen machen\\\"' — the simplex; the vi- compound is the regular preverbal formation of it.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"HRN\", \"where\": \"Horn no. 939, p. 210\", \"stance\": \"supports\", \"note\": \"'ai. vi + √vardh- \\\"heranwachsen, gedeihen\\\"' — Horn cites exactly Nourai's compound as the source of the Persian verb.\"},\n            {\"src\": \"BRT\", \"where\": \"Bartholomae, AiW col. 1369 s.v. varəd-\", \"stance\": \"supports\", \"note\": \"Bartholomae's varəd- entry 'augere ... wachsen machen, gedeihen lassen' with preverbal constructions; the compound with vī- is unexceptional.\"},\n            {\"src\": \"FFD\", \"where\": \"Abolqāsemi p. 75\", \"stance\": \"supports\", \"note\": \"'گوال < ایرانی باستان *wi-warda-ya. ... wi پیشوند فعلی است. wardā صورت بالاندهٔ ward به معنی «بالیدن» است' — the Iranian counterpart of the Sanskrit compound.\"}\n          ]\n        },\n        {\n          \"id\": 4, \"lang\": \"Persian\", \"words\": \"govâlîdan «گوالیدن»\", \"verdict\": \"confirmed\",\n          \"derivation\": \"گوالیدن govālīdan 'to grow' (with گوالاندن govālāndan, the causative, and گوال govāl 'growth') is the prefixed doublet of بالیدن. Old Iranian *wi-warda-ya- gives the Persian verb by two regular changes: the preverb *wi- appears in New Persian as gu-/go- (the same development as in گواردن govārdan < *wi-gard-, گواژه, گوارش — Iranian *wi- > MP wi- > NP gu-), and the stem *ward(a)ya- gives -vāl- exactly as in bālīdan. Horn no. 939 states it in one line: 'guwālīden, gevālīden \\\"wachsen\\\" (unbelegt); vergl. bālīden (No. 173). ai. vi + √vardh- \\\"heranwachsen, gedeihen\\\"; ist schon im Pehlevī verschwunden' — note his 'unbelegt' and the observation that the verb had already disappeared in Middle Persian, so the New Persian form is a survival known only from the lexicographers and from verses like the Ṭayyān couplet Nourai prints. Moʿin's footnote at Borhān 1848 gives the same account and cites Horn by his entry number ('اسشق ۹۳۹'). The chart's NOTE that FFD:75 derives these from Old Persian wi-ward is accurate in substance (Abolqāsemi writes 'ایرانی باستان *wi-warda-ya', i.e. Old Iranian rather than Old Persian specifically).\",\n          \"derivation_fa\": \"«گوالیدن» با «گوالاندن» و اسم‌مصدر «گوال»، دوگانهٔ پیشونددارِ «بالیدن» است. ایرانی باستان *wi-warda-ya- با دو دگرگونیِ قاعده‌مند به این صورت رسیده است: پیشوند *wi- در فارسی نو «گُ/گو» می‌شود (همان تحولی که در «گواردن» < *wi-gard-، «گوارش» و «گواژه» می‌بینیم) و ستاک *ward(a)ya- درست مانند «بالیدن» به «‑وال‑» بدل می‌شود. هرن در شمارهٔ ۹۳۹ همین را در یک سطر می‌گوید: «گوالیدن/گوالیدن «رشد کردن» (بی‌شاهد)؛ سنجید با بالیدن (شمارهٔ ۱۷۳). سنسکریت vi + √vardh-؛ این فعل در پهلوی از میان رفته است» — و همین که در پهلوی از میان رفته توضیح می‌دهد چرا واژه تنها در فرهنگ‌ها و بیت‌هایی مانند بیتِ طیّانِ نقل‌شده در نمودار مانده است. حاشیهٔ معین در برهان قاطع (ص ۱۸۴۸) همین را می‌گوید و به شمارهٔ هرن («اسشق ۹۳۹») ارجاع می‌دهد. یادداشت نمودار دربارهٔ FFD:75 نیز در جوهر درست است، جز آنکه ابوالقاسمی «ایرانی باستان» نوشته نه «پارسی باستان».\",\n          \"sources\": [W_WT_VALA],\n          \"ref_check\": [\n            {\"ref\": \"BQT:1848\", \"status\": \"supports\", \"note\": \"Borhān-e Qāṭeʿ p. 1848 (fetched with tools/ref_page.py BQT:1848 → BQT_v3_picofile.pdf p. 645, image cached at data/verification/sources/refs/ocr/BQT/1848.png): headword 'گوالیدن ... بمعنی بالیدن و نمو کردن هم از انسان و حیوان', footnote 7: 'از: گوال (ه.م.) + یدن (پیوند مصدری)؛ قس: بالیدن، هندی باستان vṛdh + vardh (نمو کردن، رشد کردن)؛ اسشق ۹۳۹.' The page also has گوال 'وبمعنی بالیدن و نمو کردن'.\"},\n            {\"ref\": \"HRN:210\", \"status\": \"supports\", \"note\": \"Horn p. 210 no. 939: 'guwālīden, gevālīden \\\"wachsen\\\" (unbelegt); vergl. bālīden (No. 173). ai. vi + √vardh- \\\"heranwachsen, gedeihen\\\"; ist schon im Pehlevī verschwunden.'\"},\n            {\"ref\": \"MON:3427\", \"status\": \"supports\", \"note\": \"Moʿin, Farhang-e Fārsi s.v. گوالیدن (MON_part2.txt line 35786): 'گوالیدن: gvālīdan (نمو کردن، م. گوالاندن، گوالانیدن) (مصدر لازم) ... نمو کردن، نشو و نما یافتن، بالیدن، اندوختن، جمع کردن'; the preceding entries give گوال 'بالش، نمو، بالیدگی' and گوالش 'نمو، نشو و نما' — i.e. Nourai's extras گوالاندن and گوال.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"FFD\", \"where\": \"Abolqāsemi p. 75 (FFD_pages.txt, pdf p. 80)\", \"stance\": \"supports\", \"note\": \"'گوالیدن (:بالیدن). گوال < ایرانی باستان *wi-warda-ya. ... wi پیشوند فعلی است. wardā صورت بالاندهٔ ward به معنی «بالیدن» است و خود «بالیدن» هم از ward آمده است > بالیدن.' Note 'ایرانی باستان' (Old Iranian), where the chart's NOTE says 'Old Persian'.\"},\n            {\"src\": \"PHD\", \"where\": \"MacKenzie, s.v. wālīdan and the wi- prefixed verbs\", \"stance\": \"partial\", \"note\": \"MacKenzie has the simplex wālīdan but no *wi-wālīdan, which agrees with Horn's remark that the compound had already vanished in Middle Persian.\"},\n            {\"src\": \"BQT\", \"where\": \"Borhān p. 1848 s.v. گوال\", \"stance\": \"supports\", \"note\": \"'گوال ... و بمعنی بالیدن و نمو کردن' with footnote 6 'رک: گوالیدن'.\"}\n          ]\n        },\n        {\n          \"id\": 5, \"lang\": \"Old Persian\", \"words\": \"ward; wi-ward\", \"verdict\": \"plausible\",\n          \"derivation\": \"The forms and the meanings are right, but the language label is not quite. *ward- 'to grow' and *wi-ward- 'to grow out' are Proto-/Old IRANIAN reconstructions, not attested Old Persian: Kent's Old Persian lexicon has no verb ward- 'to grow'; the only OP -vard- is the second member of the personal name Artavardiya- 'Justice-worker', which Kent takes to a different root. Nourai's own source says as much — Abolqāsemi (FFD p. 75) writes 'ایرانی باستان *wi-warda-ya' ('Old Iranian'), which Nourai has rendered 'Old Persian'; his in-chart NOTE on node 4 repeats the same rendering. As a reconstruction the node is correct and is the necessary ancestor of both bālīdan and govālīdan; only the box's language heading overstates the evidence. The asterisk that a reconstruction requires is also missing on the printed page (the book prints 'ward' and 'wi-ward' bare) — but that is Nourai's house style throughout, not a misprint, and the extraction is faithful.\",\n          \"derivation_fa\": \"صورت‌ها و معناها درست‌اند ولی برچسب زبانی دقیق نیست. *ward- «رشد کردن» و *wi-ward- «بیرون رُستن» بازسازی‌های ایرانیِ باستان‌اند نه صورت‌های گواهی‌شدهٔ پارسی باستان: در واژه‌نامهٔ کنت از پارسی باستان چنین فعلی نیست و تنها ‑vard- موجود، جزءِ دومِ نام خاصِ Artavardiya- «کارگزارِ داد» است که کنت آن را به ریشهٔ دیگری می‌برد. خودِ مأخذ نورایی هم همین را می‌گوید: ابوالقاسمی (ص ۷۵) نوشته «ایرانی باستان *wi-warda-ya» و نورایی آن را «پارسی باستان» برگردانده است. پس این گره به‌عنوان بازسازی درست است و نیای ضروری «بالیدن» و «گوالیدن» است؛ تنها عنوان زبانیِ جعبه بیش از آنچه گواه اجازه می‌دهد ادعا می‌کند. نبودِ ستاره هم شیوهٔ همیشگی کتاب است، نه خطای چاپ یا خوانش.\",\n          \"sources\": [W_WT_VALA],\n          \"ref_check\": [\n            {\"ref\": \"FFD:75\", \"status\": \"partial\", \"note\": \"Abolqāsemi p. 75 s.v. گوالیدن gives 'ایرانی باستان *wi-warda-ya' — Old IRANIAN with an asterisk, not Old Persian. The reconstruction is his; the language label in the chart is Nourai's own.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KNT\", \"where\": \"Kent, Old Persian, Lexicon\", \"stance\": \"contradicts\", \"note\": \"grep of KNT.txt for ward/vard finds only 'Arta-vardiya- \\\"Justice-worker\\\"' and vardana- 'city' (which Kent connects with Av. varəzāna-, root varəz- 'to shut off'). There is no Old Persian verb ward- 'to grow', so the label 'Old Persian' is not supported by the standard OP lexicon.\"},\n            {\"src\": \"SYN\", \"where\": \"Buck, s.v. OPers. vardana-\", \"stance\": \"partial\", \"note\": \"'OPers. vardana- prob. : Av. varəzāna- \\\"community, state\\\" ... fr. the root in Av. varəz- \\\"shut off\\\" ... But the OPers. word could also correspond to Skt. vardhana-' — even the one OP form that looks like it is disputed and is not a verb 'to grow'.\"},\n            {\"src\": \"BRT\", \"where\": \"Bartholomae, AiW col. 1369\", \"stance\": \"supports\", \"note\": \"the Avestan verb varəd- 'augere' is the real Old Iranian attestation of what this box calls Old Persian.\"}\n          ]\n        },\n        {\n          \"id\": 6, \"lang\": \"Greek\", \"words\": \"orthos\", \"verdict\": \"confirmed\",\n          \"derivation\": \"Greek ὀρθός 'straight, upright; right, correct, true' belongs to this root complex on any current analysis, and the semantic path 'upright' > 'straight' > 'right, correct' is the ordinary one (cf. Latin rectus from *h₃reǵ- 'straighten'). The two competing derivations both land inside Nourai's box: Pokorny (IEW 1167) and Watkins take it from *u̯ordh-u̯o- / *wrodh-wo-, the o-grade of u̯erdh- 'grow, rise, high' — the Doric gloss βορθαγορίσκος in Hesychius shows the lost initial digamma that this requires — while Beekes and current Wiktionary derive it from *h₃r̥dʰ-wó- from *h₃erdʰ- 'upright', making it the exact cognate of Sanskrit ūrdhvá- 'high', Avestan ərəδwa- and Latin arduus, via Proto-Hellenic *ortʰwós. Either way the word descends from the material in the root box, and Nourai's gloss 'correct, right' is the classical sense that the English derivatives continue.\",\n          \"derivation_fa\": \"یونانی ὀρθός «راست، برافراشته؛ درست، صحیح» بر پایهٔ هر دو تحلیل امروزی به همین مجموعهٔ ریشه‌ای تعلق دارد و سیر معنایی «برافراشته > راست > درست» سیری معمول است (سنجید با rectus لاتینی از *h₃reǵ-). دو تحلیل رقیب هر دو در همین جعبه جای می‌گیرند: پوکورنی (ص ۱۱۶۷) و واتکینز آن را از *u̯ordh-u̯o-، درجهٔ o ی ریشهٔ u̯erdh-، می‌گیرند — و صورت دُریِ βορθ‑ در هسیخیوس نشانِ همان «و»ی آغازینِ افتاده است — و بیکس و ویکی‌واژه آن را از *h₃r̥dʰ-wó- از *h₃erdʰ- «برافراشته» می‌دانند و بدین‌سان هم‌ریشهٔ دقیقِ ūrdhvá- سنسکریت، ərəδwa- اوستایی و arduus لاتینی، از راه هلنیِ آغازین *ortʰwós. در هر دو حال واژه از همان مواد جعبهٔ ریشه برآمده است و معنایی که نورایی داده همان معنای کلاسیکی است که مشتق‌های انگلیسی آن را ادامه می‌دهند. ادعای نورایی درست است.\",\n          \"sources\": [W_WT_ORTHOS],\n          \"ref_check\": [\n            {\"ref\": \"POK:1167\", \"status\": \"supports\", \"note\": \"IEW 1167: 'gr. orthós, dor. borthó- \\\"aufrecht, gerade, richtig, wahr\\\" (*u̯ordh-u̯o-)' — including the Doric b- form.\"},\n            {\"ref\": \"KLN:1097\", \"status\": \"supports\", \"note\": \"Klein s.v. ortho- (leaf 587): 'Gk. orthós, \\\"straight; right, true, exact; genuine; upright, righteous\\\", for *worthwos (cp. Dor. borthó-); cognate with OI. ūrdhvaḥ, \\\"high\\\", várdhate, \\\"causes to grow\\\", L. arduus.'\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. wrēdh-\", \"stance\": \"supports\", \"note\": \"'wrēdh-. To grow straight, upright. Suffixed zero-grade form *wrodh-wo- in Greek orthos, straight, correct, right: ORTHO-, ORTHOTICS; ANORTHITE. [In Pok. werdh- 1167.]'\"},\n            {\"src\": \"WLD\", \"where\": \"Walde-Pokorny Bd. I (line 13487)\", \"stance\": \"supports\", \"note\": \"'orthós, ai. ūrdhva- (s. u̯eredh-)' — the same equation in the older handbook.\"},\n            {\"src\": \"SKT\", \"where\": \"Skeat s.vv. Orthodox, orthoepy, Orthography\", \"stance\": \"supports\", \"note\": \"'Gk. orthos, upright / right / straight' consistently glossed; Skeat gives no deeper root, so he is neutral between the two reconstructions.\"}\n          ]\n        },\n        {\n          \"id\": 7, \"lang\": \"English\", \"words\": \"ortho-; orthodox, orthogonal, orthodontics, orthopedics\", \"verdict\": \"confirmed\",\n          \"derivation\": \"All four words are learned formations on Greek orthós, mostly of the modern scientific period, and each is transparent. orthodox: Late Latin orthodoxus < Greek orthódoxos 'having the right opinion' (orthós + dóxa 'opinion'), in English from the 16th century. orthogonal: Greek orthogṓnios 'right-angled' (orthós + gōnía 'angle'), through Latin/French, first in geometry. orthodontics: coined in the 19th century from orthós + odoús, odónt- 'tooth' — literally 'straightening the teeth'. orthopedics: F. orthopédie, coined by Nicolas Andry in 1741 from orthós + paidíon 'child', 'the straightening of children', later generalised to the skeleton. The combining form ortho- itself is Klein's headword. The node is an unproblematic list of derivatives.\",\n          \"derivation_fa\": \"هر چهار واژه ساخت‌های عالمانه بر پایهٔ orthós یونانی‌اند، بیشترشان از دورهٔ علمِ نوین، و هر یک روشن است. orthodox از لاتینیِ متأخر orthodoxus < یونانی orthódoxos «دارندهٔ رأی درست» (orthós + dóxa «رأی») که از سدهٔ شانزدهم در انگلیسی است؛ orthogonal از یونانی orthogṓnios «قائم‌الزاویه» (orthós + gōnía «زاویه») از راه لاتین و فرانسوی؛ orthodontics ساختهٔ سدهٔ نوزدهم از orthós و odoús/odónt- «دندان» یعنی «راست‌کردنِ دندان»؛ و orthopedics از فرانسوی orthopédie که نیکلا آندری در ۱۷۴۱ از orthós و paidíon «کودک» ساخت، یعنی «راست‌کردنِ کودکان»، که بعدها به کل استخوان‌بندی تعمیم یافت. پس این گره فهرستی بی‌اشکال از مشتق‌هاست و ادعای نورایی درست است.\",\n          \"sources\": [W_WT_ORTHOS],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Nourai gives no reference for this node; the parent Greek node carries POK:1167 and KLN:1097, both of which check out (see node 6).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"s.vv. ortho-, orthodox, orthodoxy (leaf 587)\", \"stance\": \"supports\", \"note\": \"'ortho-, before a vowel orth-, combining form meaning \\\"straight; rectangular; regular; true, correct\\\" — Gk. ortho-, fr. orthós'; 'orthodox ... Late L. orthodoxus, fr. Gk. orthódoxos, \\\"having the right opinion\\\", fr. orthós, \\\"right\\\", and dóxa, \\\"opinion\\\".'\"},\n            {\"src\": \"SKT\", \"where\": \"Skeat s.vv. Orthodox, orthoepy, Orthography, Orthopterous\", \"stance\": \"supports\", \"note\": \"'Orthodox, of the right faith. Late L. orthodoxus. — Gk. orthodoxos, of right opinion, from orthós, upright ... doxa, an opinion'; 'Orthopterous ... Gk. orthós, straight'.\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. wrēdh-\", \"stance\": \"supports\", \"note\": \"lists ORTHO-, ORTHOTICS, ANORTHITE as the English descendants of Greek orthos under this root.\"}\n          ]\n        }\n      ]\n    }\n  ]\n}\n\nwith io.open('/home/sfmqrb/git/rishe/data/verification/page-158.json','w',encoding='utf-8') as f:\n    json.dump(doc, f, ensure_ascii=False, indent=2)\n    f.write('\\n')\nprint('ok')\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build158.py"
}
```


### [2026-09-05T20:48:09.282Z] TOOL RESULT

```
ok
```


## [2026-09-05T20:48:13.815Z] TOOL CALL #74: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-158.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 158"
}
```


### [2026-09-05T20:48:15.905Z] TOOL RESULT

```
JSON OK
nodes verified: 19/19
node verdicts: {'plausible': 4, 'confirmed': 12, 'disputed': 3}
root verdicts: {'plausible': 2}
ref checks: {'not_found': 2, 'supports': 16, 'not_checked': 10, 'partial': 3}
books consulted: {'partial': 9, 'supports': 27, 'contradicts': 4, 'silent': 12} | by book: {'KLN': 9, 'LKT': 5, 'MON': 5, 'AKD': 3, 'DEV': 3, 'SKT': 3, 'BRT': 3, 'AHD': 3, 'PHD': 2, 'HRN': 2, 'FFD': 2, 'RCH': 1, 'WEB': 1, 'FVQ': 1, 'PEI': 1, 'LEW': 1, 'ARY': 1, 'AVG': 1, 'HUB': 1, 'BQT': 1, 'KNT': 1, 'SYN': 1, 'WLD': 1}
```


## [2026-09-05T20:48:23.987Z] TOOL CALL #75: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg158_600.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/158.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/158.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/1848.png && python3 tools/verify_check.py 158 2>&1 | grep -c PROBLEM || echo \"0 PROBLEM lines\""
}
```


### [2026-09-05T20:48:26.043Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 169880 Sep  5 16:48 /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/158.png
-rw-rw-r-- 1 sfmqrb sfmqrb 166992 Sep  5 16:32 /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/1848.png
0
0 PROBLEM lines
```


## [2026-09-05T20:48:45.052Z] AGENT

Page 158 (book p. 128) verified — `data/verification/page-158.json` written, `verify_check.py 158` shows 19/19 nodes and 0 PROBLEM lines.

**Verdicts:** roots 2 × plausible; nodes 12 confirmed, 4 plausible, 3 disputed. Ref checks: 16 supports, 3 partial, 2 not_found, 10 not_checked (all AHD New-College dictionary pages + un-referenced nodes). 23 books consulted.

**Disputed**
- *Erěbu* #3 Italian **Marocco** — not from Arabic *maġrib/al-Maġrib al-Aqṣā*; it is from **Marrākuš**, the city founded 1070, itself Berber (*amur n akuš*). No sound change takes ġ+b to rr+k. Lokotsch 1406 and Klein both anchor it in the city name.
- *Erěbu* #4 Arabic **Marâkeš** — arrow drawn backwards: Arabic Marrākuš is the source of Italian Marocco, not a loan from it (Lokotsch: the Romance forms come "hieraus").
- *Erěbu* #8 Greek **europa** — the Semitic derivation is Klein's (after H. Lewy 1895) but is rejected today: M. L. West ("phonologically… very poor"), Beekes (Pre-Greek); Etymonline/Wikipedia call the origin uncertain.

**Plausible (with reasons)**
- Root *Erěbu*: word and gloss right, but Arabic/Hebrew are Proto-Semitic **cognates** (*ġrb), not descendants; Zimmern himself writes "viell.". Same for nodes #1 and #7.
- Root *Ered/Werdh*: POK 339 and POK 1167 both check out verbatim, but Pokorny and all modern handbooks keep *h₃erdʰ- "high" and *h₁werdʰ- "grow" apart; Nourai merges them. Node #1 (Avestan *ərəδwa-* + *varəd-*) inherits this.
- Node #5 "Old Persian ward/wi-ward": Kent has no such OP verb; Nourai's own source (FFD 75) writes *ایرانی باستان* (Old Iranian), which he rendered "Old Persian".

**Transcription suspects:** none. **Extraction errors:** none — the JSON matches the printed page (checked at 600 dpi; page copied to `sources/refs/ocr/BOOK/158.png`).

**One book misprint for the owner's notes (not a data fix):** node #1's refs print as `AKD:640,854`, but Zimmern's *Akkadische Fremdwörter* has only ~85 pages. The page really reads AKD, so it is Nourai's misprint — on internal evidence for `AHD:640,854` (the same chart cites AHD:854 twice and AHD:452). The substance is on AKD **p. 64**, which I verified and which does support the Arabic/Hebrew forms (hedged with "viell.").

Strong confirmations on the Iranian side: MacKenzie `wālīdan, wāl- [wʾl-ytn' | N bālīdan]`; Horn 173/939 (whose footnote carries the very Sanā'ī couplet Nourai prints); Hübschmann 173 (*wālēnītan* = Av. *varədaya-*); Mo'in's Borhān footnote at p. 1848 citing Horn 939 by number; Abolqāsemi pp. 35 and 75; Bartholomae cols. 351 and 1369; Watkins *ered-* / *wrēdh-*.
