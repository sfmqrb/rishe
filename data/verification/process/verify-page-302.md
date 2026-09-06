# Verification process log — verify-page-302


## [2026-09-06T22:50:13.424Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 302 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-302.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-302.json. Write /home/sfmqrb/git/rishe/data/verification/page-302.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 302` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-06T22:50:15.104Z] AGENT

I'll start by reading the instructions.


## [2026-09-06T22:50:15.827Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-06T22:50:15.845Z] TOOL RESULT

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


## [2026-09-06T22:50:16.443Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-302.txt"
}
```


### [2026-09-06T22:50:16.456Z] TOOL RESULT

```
1	=== PDF page 302 (book page 272) ===
2	--- entry 0 ---
3	ROOT [Persian] Lâl : red color  (refs BQT:1879; KLN:904)
4	#1 (parent #0) [Persian] refs=BQT:1879; MON:3536 | lâleh «لاله» : a red flower (tulip) ; âlâleh «آلاله» : a red flower
5	#2 (parent #0) [Persian] refs=BQT:1880; MON:3536 | lâlak «لالک ( لالکا )» : red leather and shoes made from it
6	#3 (parent #0) [Persian] refs=BQT:1880 | lâleh-sâr «لاله سار» : a red-headed bird ☞Ker 1 ; lâlas «لالس» : a red silk fabric
7	#4 (parent #0) [Arabic] refs=AFM:142; PLA:241; TAD:66 | la`l : red, a red stone, red ruby
8	  #5 (parent #4) [Persian] refs=BQT:1879 | la`l «لعل» : red ruby, also used to describe lips
9	#6 (parent #0) [Hindustani] refs=KLN:904 | lâl : red ; lâl-šarâb : red wine ☞Š.r.b
10	  #7 (parent #6) [English] refs=KLN:904 | loll sharob : red wine
11	--- entry 1 ---
12	ROOT [Indo-European] Lanğ : to droop, be sad, sorrow  (refs IEC:663)
13	#1 (parent #0) [Sanskrit] refs=BQT:963 | rdjyate : to be in pain, disturbed
14	  #2 (parent #1) [Pahlavi] refs=BQT:963 | ranz, ranj : pain, suffering
15	    #3 (parent #2) [Persian] refs=MON:1676; IEC:663 | ranj «رنج ( رنجور ، رنجبر ، رنجش )» : pain, suffering ; ranjândan «رنجاندن ( رنجانیدن ، رنجیدن )» : to hurt
16	#4 (parent #0) [Greek] refs=IEC:663 | laggazô, laggeô : to droop
17	--- entry 2 ---
18	ROOT Lap-aro -> redirect to Lep
19	--- entry 3 ---
20	ROOT [Akkadian] Laqalaqa : flamingo, stork  (refs AKD:52)
21	#1 (parent #0) [Arabic] refs=MON:3616; AKD:52 | laqlaq : stork ; laqlaqeh : stork's cry
22	  #2 (parent #1) [Persian] refs=BQT:1902 | laklak, laqlaq «لکلک ( لقلق ، لغلغ )» : stork ; laqlaqeh «لقلقه ( لغلغه )» : slang speech
23	
```


## [2026-09-06T22:50:16.471Z] TOOL CALL #3: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/extracted/batch/page-302.json"
}
```


### [2026-09-06T22:50:16.482Z] TOOL RESULT

```
1	{
2	  "pdf_page": 302,
3	  "book_page": 272,
4	  "entries": [
5	    {
6	      "root": {
7	        "name": "Lâl",
8	        "lang": "Persian",
9	        "refs": "BQT:1879; KLN:904",
10	        "gloss": "red color",
11	        "script": "لال"
12	      },
13	      "nodes": [
14	        {
15	          "id": 1,
16	          "parent": 0,
17	          "lang": "Persian",
18	          "refs": "BQT:1879; MON:3536",
19	          "words": [
20	            {"translit": "lâleh", "gloss": "a red flower (tulip)", "script": "لاله"},
21	            {"translit": "âlâleh", "gloss": "a red flower", "script": "آلاله"}
22	          ],
23	          "script_extra": null,
24	          "note": null,
25	          "quote": {
26	            "text": "دو لب چو نار کفیده، دو رخ چو سوسن سرخ - دو رخ چو نار شکفته، دو لب چو لالهٔ لال",
27	            "poet": "Onsorî"
28	          }
29	        },
30	        {
31	          "id": 2,
32	          "parent": 0,
33	          "lang": "Persian",
34	          "refs": "BQT:1880; MON:3536",
35	          "words": [
36	            {"translit": "lâlak", "gloss": "red leather and shoes made from it", "script": "لالک ( لالکا )"}
37	          ],
38	          "script_extra": null,
39	          "note": null,
40	          "quote": {
41	            "text": "دریغ از ان شرف و خوبی و فضایل او - که عاشق است بر ان لاله روی لالک دوز",
42	            "poet": "Sŭzanî"
43	          }
44	        },
45	        {
46	          "id": 3,
47	          "parent": 0,
48	          "lang": "Persian",
49	          "refs": "BQT:1880",
50	          "words": [
51	            {"translit": "lâleh-sâr", "gloss": "a red-headed bird", "script": "لاله سار", "see": ["Ker 1"]},
52	            {"translit": "lâlas", "gloss": "a red silk fabric", "script": "لالس"}
53	          ],
54	          "script_extra": null,
55	          "note": null,
56	          "quote": {
57	            "text": "گه در قدم باغ کشد فضل تو دیبا - گه بر سر کهسار نهد حکم تو لالس",
58	            "poet": "Badr Jâjermî"
59	          }
60	        },
61	        {
62	          "id": 4,
63	          "parent": 0,
64	          "lang": "Arabic",
65	          "refs": "AFM:142; PLA:241; TAD:66",
66	          "words": [
67	            {"translit": "la`l", "gloss": "red, a red stone, red ruby", "script": null}
68	          ],
69	          "script_extra": null,
70	          "note": null,
71	          "quote": null
72	        },
73	        {
74	          "id": 5,
75	          "parent": 4,
76	          "lang": "Persian",
77	          "refs": "BQT:1879",
78	          "words": [
79	            {"translit": "la`l", "gloss": "red ruby, also used to describe lips", "script": "لعل"}
80	          ],
81	          "script_extra": null,
82	          "note": null,
83	          "quote": {
84	            "text": "لعل تو که هست جان حافظ - دور از لب مردمان دون باد",
85	            "poet": "Hâfez"
86	          }
87	        },
88	        {
89	          "id": 6,
90	          "parent": 0,
91	          "lang": "Hindustani",
92	          "refs": "KLN:904",
93	          "words": [
94	            {"translit": "lâl", "gloss": "red", "script": null},
95	            {"translit": "lâl-šarâb", "gloss": "red wine", "script": null, "see": ["Š.r.b"]}
96	          ],
97	          "script_extra": null,
98	          "note": null,
99	          "quote": null
100	        },
101	        {
102	          "id": 7,
103	          "parent": 6,
104	          "lang": "English",
105	          "refs": "KLN:904",
106	          "words": [
107	            {"translit": "loll sharob", "gloss": "red wine", "script": null}
108	          ],
109	          "script_extra": null,
110	          "note": null,
111	          "quote": null
112	        }
113	      ]
114	    },
115	    {
116	      "root": {
117	        "name": "Lanğ",
118	        "lang": "Indo-European",
119	        "refs": "IEC:663",
120	        "gloss": "to droop, be sad, sorrow"
121	      },
122	      "nodes": [
123	        {
124	          "id": 1,
125	          "parent": 0,
126	          "lang": "Sanskrit",
127	          "refs": "BQT:963",
128	          "words": [
129	            {"translit": "rdjyate", "gloss": "to be in pain, disturbed", "script": null}
130	          ],
131	          "script_extra": null,
132	          "note": null,
133	          "quote": null
134	        },
135	        {
136	          "id": 2,
137	          "parent": 1,
138	          "lang": "Pahlavi",
139	          "refs": "BQT:963",
140	          "words": [
141	            {"translit": "ranz, ranj", "gloss": "pain, suffering", "script": null}
142	          ],
143	          "script_extra": null,
144	          "note": null,
145	          "quote": null
146	        },
147	        {
148	          "id": 3,
149	          "parent": 2,
150	          "lang": "Persian",
151	          "refs": "MON:1676; IEC:663",
152	          "words": [
153	            {"translit": "ranj", "gloss": "pain, suffering", "script": "رنج ( رنجور ، رنجبر ، رنجش )"},
154	            {"translit": "ranjândan", "gloss": "to hurt", "script": "رنجاندن ( رنجانیدن ، رنجیدن )"}
155	          ],
156	          "script_extra": null,
157	          "note": null,
158	          "quote": {
159	            "text": "درخت دوستی بنشان که کام دل بیار آرد - نهال دشمنی برکن که رنج بیشمار آرد",
160	            "poet": "Hâfez"
161	          }
162	        },
163	        {
164	          "id": 4,
165	          "parent": 0,
166	          "lang": "Greek",
167	          "refs": "IEC:663",
168	          "words": [
169	            {"translit": "laggazô, laggeô", "gloss": "to droop", "script": null}
170	          ],
171	          "script_extra": null,
172	          "note": null,
173	          "quote": null
174	        }
175	      ]
176	    },
177	    {
178	      "root": {
179	        "name": "Lap-aro",
180	        "redirect": "Lep"
181	      },
182	      "nodes": []
183	    },
184	    {
185	      "root": {
186	        "name": "Laqalaqa",
187	        "lang": "Akkadian",
188	        "refs": "AKD:52",
189	        "gloss": "flamingo, stork"
190	      },
191	      "nodes": [
192	        {
193	          "id": 1,
194	          "parent": 0,
195	          "lang": "Arabic",
196	          "refs": "MON:3616; AKD:52",
197	          "words": [
198	            {"translit": "laqlaq", "gloss": "stork", "script": null},
199	            {"translit": "laqlaqeh", "gloss": "stork's cry", "script": null}
200	          ],
201	          "script_extra": null,
202	          "note": null,
203	          "quote": null
204	        },
205	        {
206	          "id": 2,
207	          "parent": 1,
208	          "lang": "Persian",
209	          "refs": "BQT:1902",
210	          "words": [
211	            {"translit": "laklak, laqlaq", "gloss": "stork", "script": "لکلک ( لقلق ، لغلغ )"},
212	            {"translit": "laqlaqeh", "gloss": "slang speech", "script": "لقلقه ( لغلغه )"}
213	          ],
214	          "script_extra": null,
215	          "note": null,
216	          "quote": {
217	            "text": "هست دربند لقلقه مانده - از در معنی و خبر رانده",
218	            "poet": "Sanâî"
219	          }
220	        }
221	      ]
222	    }
223	  ]
224	}
225	
```


## [2026-09-06T22:50:21.947Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md | head -100",
 "description": "Read source matrix"
}
```


### [2026-09-06T22:50:21.988Z] TOOL RESULT

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
```


## [2026-09-06T22:50:24.228Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['BQT','KLN','MON','AFM','PLA','TAD','IEC','AKD','POK','WLD','AHD','ARY','HRN','HUB','PHD','NYB','SYN','FVQ','LKT','SKT','FSD','WEB','HJB','AID','CHEUNG','BRT','KNT']:\n    print(k, json.dumps(d.get(k), ensure_ascii=False)[:600])\n    print()\n\"",
 "description": "Dump ref metadata"
}
```


### [2026-09-06T22:50:26.058Z] TOOL RESULT

```
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په

AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/

PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt"], "page_offset": "301 lea

TAD {"title": "Tobia al-Unaysi (طوبيا العنيسي), Tafsir al-alfaz al-dakhila fi al-lugha al-'arabiyya ma'a dhikr asliha bi-hurufihi (2nd ed. Cairo 1932, ed. Yusuf Tuma al-Bustani; later Library of Lebanon reprint) — Nourai lists it under Arabic authors ('Unaysi T.'); its Table IV line was lost in the OCR", "kind": "archive_djvu", "url": "https://archive.org/details/TOB1932ARAR (1932 ed.); also https://archive.org/details/ar113lang79 and https://archive.org/details/elshandawily14640", "lookup_hint": "Alphabetical Arabic headwords; grep the Arabic headword in TAD_pages.txt (86 leaves) or TAD.txt; insi

IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 

AKD {"title": "H. Zimmern, Akkadische Fremdwörter als Beweis für babylonischen Kultureinfluss, Leipzig 1917 (2nd ed.)", "edition_found": "1915 first edition (1917 is the 2nd, enlarged ed.; pagination may differ slightly)", "kind": "archive_djvu", "url": "https://archive.org/details/akkadischefremdw00zimmuoft", "identifier": "akkadischefremdw00zimmuoft", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AKD.txt", "page_offset": "leaf = printed + 8 (e.g. leaf 21 = p.13). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://

POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_

WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,

ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it 

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 

HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) fol

PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-

NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf

SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves

FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sou

LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Numbered entries: 

SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves

FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-Dive), in.ernet.dli.2015.272042 (vol II), in.ernet.dli.2015.83695 (vol III), in.ernet.dli.2015.147440 (vol IV Sabi-Z)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt

WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w (restricted full copies: webstersnewtwent00webs_0 1977, webstersnewtwent01webs 1983)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/W

HJB {"title": "H. Yule & A. C. Burnell, Hobson-Jobson, 2nd ed. by W. Crooke, London 1903 (Delhi reprint 1968)", "edition_found": "1903 Crooke edition (pagination identical to the 1968 reprint)", "kind": "archive_djvu", "url": "https://archive.org/details/hobsonjobsonagl02croogoog", "identifier": "hobsonjobsonagl02croogoog (others: bub_gb_6Z5iAAAAMAAJ, hobsonjobsonglos00yulerich, india.history.resource.89053)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HJB.txt", "page_offset": "leaf = printed + 35..51 (plates inserted; e.g. leaf 83 = p.32, leaf 319 = p.270, leaf 535 = p.4

AID {"title": "G. C. Whitworth, An Anglo-Indian Dictionary, London 1885", "edition_found": "1885 (DLI scan); also 1981 reprint scan", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.45332", "identifier": "in.ernet.dli.2015.45332 (also anglo-indiandictionary, 1981 reprint)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AID.txt", "page_offset": "leaf = printed + 18 (e.g. leaf 20 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lo

CHEUNG null

BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1

KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt", "page_offset": "leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \\
```


## [2026-09-06T22:50:52.546Z] AGENT

Now let me start the reference lookups. First, the local books.


## [2026-09-06T22:50:54.683Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN 1966 'loll' ===\"; grep -n -i \"loll shr\\|loll sha\\|lollshr\" KLN_1966.txt | head -20\necho \"=== KLN 1966 lal ===\"; grep -n -i \"^loll\\|Hind. lāl\\|Hind. lal\\b\" KLN_1966.txt | head -20\necho \"=== KLN 1971 loll ===\"; grep -n -i \"loll shr\\|loll sha\" KLN_1971.txt | head -20",
 "description": "Grep Klein for loll shraub"
}
```


### [2026-09-06T22:50:54.771Z] TOOL RESULT

```
=== KLN 1966 'loll' ===
35355:sirup,  syrup,  n.  —  ME.  sirop,  sirup,  fr.  OF.  (=  F.) sirup,  fr.  ML.  sirupus,  syrupus,  fr.  Arab,  sharab, ‘drink,  beverage’,  from  the  stem  of  shariba,  ‘he drank’,  whence  also  Sp.  jarabe,  jarope,  and OProven?.  eissarop.  It.  sciroppo  is  also  borrowed fr.  ML.  sirupus.  See  sherbet  and  cp.  shrub,  ‘a drink’,  sorbet,  and  the  second  word  in  loll shraub.
=== KLN 1966 lal ===
22046:Lollard
22086:Lollard,  n.,  member  of  a  sect  of  reformers,  follow¬ ers  of  John  Wycliffe.  —  MDu.  Lollaerd,  lit. ‘mutterer  (scil.  of  psalms)’,  formed  fr.  lollen,  ‘to hum,  mumble’.  See  lull  and  -ard  and  cp.  loll.
22087:lollipop
22090:loll  shraub,  loll  shrob,  claret  (India).  —  Hind,  lal sharab,  ‘red,  wine’,  fr.  Pers.  lal,  ‘red’,  and  Arab. sharab,  ‘drink,  wine’  (see  sirup), loma,  n.,  a  membranous  fringe  ( zoo! .)  —  ModL., fr.  Gk.  Xoifj.a,  ‘hem,  fringe,  border’,  which  prob. stands  for  *  f Xoi  ux  and  is  cogn.  with  L.  lorum (for  *wlorum ),  ‘strap,  thong’.  See  lore,  ‘space between  the  eyes  and  beak  of  birds’,  and  cp. next  word  and  the  second  element  in  Cycloloma, Isoloma,  Tricholoma.
=== KLN 1971 loll ===
139960:loll shraub, loll shrob, claret (India). — Hind. Idl 
220473:word in loll shraub.
```


## [2026-09-06T22:50:55.790Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AKD laqlaq ===\"; grep -n -i \"laqlaq\\|laklak\\|laqalaqa\\|Storch\" AKD.txt | head -40",
 "description": "Grep Zimmern for stork"
}
```


### [2026-09-06T22:50:55.844Z] TOOL RESULT

```
=== AKD laqlaq ===
799:Weihe  od.  ä.  akk.  JnqoMqa  eiu  Vogel  :  fraglich,  ob  dazu  arab.  laqlaq
800:Storch  gehört,  oder  beiderseits  unabhängig  ein  onomatop.  Name  vor- liegt, akk.  paü  eiu  Vogel,  der  aber  kaum  zusammeugestellt  werden daii  mit  griech.  raüg  O  aram.  taiisä,  arab.  täwüs,  tatls^\  lat.  pavo,  Ff  au.
```


## [2026-09-06T22:51:02.525Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nd=open('AKD.txt',encoding='utf-8',errors='replace').read()\npages=d.split('\\f')\nfor i,p in enumerate(pages):\n    if 'laqoMqa' in p or 'laqlaq' in p or 'JnqoMqa' in p:\n        print('leaf index',i,'printed approx',i-8)\n        print(p[:2500])\nEOF",
 "description": "Locate AKD stork page"
}
```


## [2026-09-06T22:51:04.031Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== IEC 663 area: search lang / laggaz ===\"; grep -n \"laggaz\\|langgaz\\|λαγγ\\|lagge\" IEC.txt | head -20\necho \"=== IEC ranj ===\"; grep -n \"ranj\\b\" IEC.txt | head -20",
 "description": "Grep Mann IEC"
}
```


### [2026-09-06T22:51:04.348Z] TOOL RESULT

```
leaf index 61 printed approx 53
 so  aucli  bei  den  Pflanzen  und  Mineralien,  ist  in  den  Fällen, wo  das  Wort  auch  im  Akk.  selbst  wahi-sch.  nicht  einheimisch  ist,  und  wo  es  auch  un- sicher bleibt,  ob  das  Aram.  (oder  Arab.)  zunächst  aus  dem  Attad.  entlelmt  hat  oder umgekehrt,  oder  beide  aus  einer  dritten  Quelle,  dies  dui-ch  bloße  Gegenüberstellung  (:) ausgedrückt.
      52      
Weihe  od.  ä.  akk.  JnqoMqa  eiu  Vogel  :  fraglich,  ob  dazu  arab.  laqlaq
Storch  gehört,  oder  beiderseits  unabhängig  ein  onomatop.  Name  vor- liegt, akk.  paü  eiu  Vogel,  der  aber  kaum  zusammeugestellt  werden daii  mit  griech.  raüg  O  aram.  taiisä,  arab.  täwüs,  tatls^\  lat.  pavo,  Ff  au.
akk.  urnu  eine  Eidechsen art  (auch  im  Akk.  wohl  Fremdw.)  :  aram. Warna,  arab.  tvaran  (>  (mit  irrtümlicher  Auffassung  des  arab.  "Wortes) die  deutsche  Bez.   Warner,  u.  darnach  sogar  Monitor).  akk.  hul-
mittu  eine  Eidechsenart  :  >  wohl  syr.  hulmntä,  während  hebr.  hörnet vieU.  urverwandt  ist.  akk.  mümi,  umünu  viell.  eine  Eidechsen-
art :  ^  wohl  syr.  'ämfiiiä.  akk.  mtitqu  ein  Tier  niederer  Ordnung :
>>  viell.  syr.  'fimaqtä  wahrsch.  eine  Eidechsenart.  [akk.  namsuhu
(od.  tumsuhu?),  viell.  auch  tamSahu,  Krokodil,  ebenso  wie  arab.  timsäh  <^ ägypt.  msh.]  akk.  ne.?  qaqqarl  wörtl.  „Erdlöwe",  ein  Tier  niederer
Ordnung,  viell.  Chamäleon  :  dann  griech.  xauaile'cov  Übers,  von  akk. nei'  qaqqari,  wie  andererseits  syr.  'arjä  cb-'ar'd  od.  cb-'april  tJhevs.  von xaftaiklutv  i.  S.  V.  Chamäleon-Pflanze.  akk.  suräru,  suririUu  eine
Art  Salamander  :  ^  syr.  saröritä.
akk.  nünu  Fisch  :  >  vieU.  aram.  nüml  O  arab.  nmi)\  hebr.  um' als  N.  pr.  'Nim  und  im  kanaan.  Buchstabenn.  ISim,  Nu,  N.  akk.
hqmfi  ein  Fischname  (wohl  <;  sum.  guhe)  :  >  jüd.-aram.  Jcöpjä,  augebl. Steinbutt  O  wahrsch.  arab.  güfijj).  akk.  qarsu  ein  Fischname  :
>  viell.  aram.  Imrsä,  arab.  qars,   qars  Haifisch.  akk.  gingurra
ein  Fischname  :  >  wohl  mand.  singürä  ein  Fischname.  akk.  kis-
siigu  ein  Fischuame  (auch  im  Akk.  wohl  Fremdw.)  :  dazu  viell.  arab. jMttsag,  hüsuß,  pers.  hüsag  Schwertfisch.
akk.  kalmatu  "Wurm,  Ungeziefer  :  ]>■  vieU.  aram.  lalnidtä,  qalmdtn Laus,  Wurm,  während  arab.  qaml,  äth.  qüemäl  Laus  urverwandt  sein könnten  akk.  näbii  Ungeziefer  :  >  aram.  naba  Laus.  akk.
snsu  Motte  :  >  wohl  hebr.  säs,
```


### [2026-09-06T22:51:04.417Z] TOOL RESULT

```
=== IEC 663 area: search lang / laggaz ===
=== IEC ranj ===
```


## [2026-09-06T22:51:10.627Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nls -la IEC.txt; wc -l IEC.txt\npython3 - <<'EOF'\nd=open('IEC.txt',encoding='utf-8',errors='replace').read()\npages=d.split('\\f')\nprint('leaves',len(pages))\n# leaf ~= p/2+15 -> p 663 -> leaf ~346\nfor i in (345,346,347):\n    print('=== leaf',i,'===')\n    print(pages[i][:3000])\nEOF",
 "description": "Inspect Mann IEC around p.663"
}
```


### [2026-09-06T22:51:12.171Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 3311889 Sep  4 14:06 IEC.txt
20498 IEC.txt
leaves 858
=== leaf 345 ===
�speak, order’; Ober, cf. 0àtiy, 3s ‘says’; a-0aham ‘I said’; Arm. asem, osem (‘say, speak, tel. Phonology obscure); Tokh. A känts- ‘vow, admit’; Alb. thom, them, 3s. thotë ‘say’; Lat. censeo, Gre ‘consider, think’; OFris. (?) henzia “approve, ratify’; OCS (defec- tive) sétü “he says?
Kensos, à, us 'utterance, opinion, state- ment. Cf. Kens- (and Kés-). WP I, 403 Skt. $ámsab ‘pronouncement, cal? beside $asah “order”; Per. cf. fa-sana ‘fable’; Lat. cén- sus, gs -us 'polltax, census’; LW in Gk. kén- sos, id.; Osc. cf. censaum, inf. ‘to vote, ad-
609 judge’; Alb. cf. e thânë, f, (“saying”, fr. a type *Kons-)
Kent- ‘prick, point, spike’. WP I, 402. Cf. Kentrom Oss. síndz, Dig. sindzä ‘thorn, splinter beside síngin, Dig. singin, adj. ‘prickly’; Gk. cf. ken- táð, kentéð, v. ‘prick’; Alb. thind ‘beak’; Br. cf. kentel, pl. -téliu, f. ‘point, time, hour, les- son’; MHG cf. hint-ber ‘raspberry’; G Him- beer, id.; OE hind-berge, EME hind-berry, id. (Isophones: Gaul. cintu- “first; OW cynt, W cyn ‘before’; Ir. céad- cpds. “first-?; céadamh “of the first of May’: W cyntaf ‘first’; Go. hindum-, beside hindana, OHG hintana ‘be- hind’; OE hindema ‘hindmost’, doubtfully also to Lat. re-cēns, -centis ‘recent’. See WH: LEW)
Kentrom, à (Kütr-) ‘point, spike, spur’. Cf. Kent-. WP I, 402 Arm. santr, gs santer (‘comb’, fr. Kütrə, but gs vocalism obscure); Gk. kéntron ‘spur, prickle, goad, sting’; LW in LLat. centria ‘sting’; Alb. thundër, f. (hoof, heel, talon, thorny plant’, fr. *Kntrá); Gaul. centron (part of a mountain- name); Br. kentr, pl. -u, f. ‘spur’; Cor. kentr, pl. ow, f. ‘spike’; Olr. centir, cintir ‘spur’; Du. (?) hinder, m. ‘annoyance’; Fris. ‘obstacle, catch’; Sw. hinder, n. id. (Gmc. cognates doubtful)
Keng (Kop-) ? ‘obtrude, bristle’. (The Alb. forms are ambig. cf. Kap- & Koip-) Alb thep ‘sharpen’; cf. o-gde gë-thapë ‘claw’; Li. Septi, pres. Sempu, pf. šepau ‘bristle’; cf. o-gde šãpas ‘bristle, awn’. Only the Lith. forms are explicit
Kephelos (Kepolos) "a fish". (IE?) Sk. $apharah ‘cyprinus sophore'; Scyth. (?) cf. sapérdes (groundling' (err. for *sepár-?); Gk. képhalos *mullet; Li. Sápalas ‘roach’; Latv. sapals ‘Danubian carp’
Kequros, see Kekuros
Ker- (1) (Kerā, ios, iə. Cf. Kerið, and Kerus as a separate entry). WP I, 408, 410, 427, 454, and II, 576 Skt. sáryah ‘arrow’; Sáryà ‘cane, shaft, arrow’; EMAIb. therrë, therë, f. ‘briar; MHG hir, smfn. ‘pang; violence’; Li. Serys, m. ‘bristle’
Ker- (2) (e-grade form of type Kr-, Kor-
Kent- — Kerdhos, à
15
20
25
30
35
40
45
610
‘head’, q.v. Cf. Kerosr-). WP I, 404
Per. sar (&head', prob. fr. *Kor- in view of Skt. Síras, id.); Tokh. cf. sår, prp. & postp. ‘above’; Sarye (Cupper Lat. primi-cerius *chief); Lat. cf. also cer-nuus (‘face downward’, lit. 'head- turned??); pro-cer, pl. -ceres, gp -cerum *dig- nitary; beam-head in wall; cer-vix, gs -vicis, f. ‘nape’; uncertainly in Lat. car-ceres *marker- posts, benchmarks’; Br. cf. kern, f. (top, tip, crown of head”, fr. Kerosno-, q. v.);
Ker- (3) (Kr-, Kra-) ‘mix, 
=== leaf 346 ===
atera-, Gk. krétér, krátér (mixing bowl". LW in Lat. cràter, crà- tera); OHG hruorjan, OS hrorjan, OE hreran ‘stir, shake’; OE, OS hror “active, lively’, cf. E dial. a roosing fire (paroxytonic prototype)
Kerd- (Kerdis, à, io) “heart, core, centre’. Cf. Krd-. WP I, 424 Vedic $ardih, f. (mng. uncertain, cf. AV 18, 3, 16); Go. hairto, OHG hérza, OS hérta, ON hjarta, pl. hjortu, n. ‘heart’; Cz. střed ‘middle’; OCS sréda, id.; Li. šerdis, -iés, f. (core, pith; bell-clapper'. Gp: Serdü. Also: "heart of a tree”); Latv. serde ‘pith, marrow?
Kerdhos, à “herd, crowd, drove'. Cf. Ker- ‘head’. WP I, 424 Skt. Sardhah “host, army? beside $ardhas, n. id.; Av. saroóo (2) ‘kind, sort’; Go. haírda, f. ‘herd’, wm. ‘herdsman’; OE heord, f., hierde, wm. as Go.; OHG hërta, f., hirti, m. as Go.; ON hjoró, f. ‘herd’; hirðir, gs hiróis, m. ‘herdsman’, cf. hirð, f. ‘bodyguard’. (Gk. kór- thus, f. ‘pile’, and W cordd, m. pl. -ion ‘circle; tribe’ are no more than potential o-gde iso- phones, despite FK: EWDS 17: Herde. OCS éréda (2) “herd” and Li. kerdZius, m. 'shep- herd? are Germanic LWs because of the initial.
611
SF:GEW regards Gmc. Sl. ànd Li. forms as cognate, and omits Indo-Iranian)
ĉerəd- (1) (Kerd-) ‘season, period, year”. Ambig. phonology.
Skt. śarád, f. “autumn. Pl. ‘years’; Av. sarəðð, m. ‘year’; OPer. Bard, f. id.; Oss. särd ‘sum- mer’; Per. sal ‘year’; Lydian sárdis, id. (Hes.)
Eerad. (2) (Kerd-) ‘horned animal’. (Cpd. of
Ker- “head”, q.v. Cf. Kernt-) Gk. kéras, gs kérados and kéraos, f. ‘two-year- old sheep or goat’; MHG, G hirz, Hirz, m. “hart, stag’; OE heorot, id.; ON hjortr, ds hir- ti, cpds. hjart-, id.; Sw. hjort, id.
Kerosr-, obl. Kerosno-; adj: Keresnios 'head,
crown of the head, brain; of the head', etc. WP I, 406. Cf. Ker- “head? beside Krn-, etc. (Variant: Krsn- in Indo-Iranian, Greek and Welsh) Skt. Sirsnáb, adj. "of the head"; Per. sarán “heads, chiefs’; Oss. sárán ‘inventive’; Gk. ká- rena, npl. ‘heads, peaks’; káranos, m. 'sover- eign’; cf. Hes. karara ‘head’; Lat. cerebrum “brain”; cf. cerritus (*mad', if for *Kersito-); Br. kern, f. “top, tip, crown of head); W caran, pl. -au, f. ‘crown of the head’; Du. hersenen, f. ‘brain’; OHG hirni, n. ‘brain’; ME hernes ‘brain’; ON hersir, gs hirsis, m. ‘chief’; hjar- si ‘crown of the head? beside hjarni ‘brain’; Sw. hjässa, f. ‘crown of the head? beside hjárn “brain”
Kerəuos (Keruos) ‘horned; horn, horned beast’. WP I, 406. Cf. Kerod-, Ker- (2), Kro- Av. srva-, ds sraoe, pl. srvao ‘nail, horn’; srvaro “horny, horned'; Per. (alleged) surü ‘horn’; Oss. siwàá, sí ‘horn’; Hiero-Hitt. cf. name: Karhuhas ('Stag-god'. H. Bossert); Gk. kera(w)ós fhorned'; but Myc. keraa (! sic) ‘horns’; Lat. cervus ('stag'. LW in MIr. cerb, Ir. cearbh, id. on account of vocalism); Gaul. carvos, id.; W carw, Cor. carow, Br. karó & karv, pl. kerved, id.; LWs in Finn. sarvas *male deer”, sarvi “horn” and in Hung. szarvas ‘deer. *Scythian in Hes. sergoi (for *serwoi 'stags")?
Kerið (1) “strike, stab, cut, sever’. Cf. Ker- (1) and 
=== leaf 347 ===
I, 463 Alb. i thjermé ‘grey’; Li. Sermuó, gs -efis ('stoat. See Kormó(n); MHG cf. hermel-, cpds. 'ermine-' beside (o-gde) harm, harme, id.; Latv. cf. sermuls ‘weasel’
Kermn- (1) “timber, log? Ober, cf. 0armis, id.; Arm. sern ‘axle, axis’; Gk. (ambig.) kérna ‘vertebrae, spondyls'; Br. karvan, f. (2) ‘roller, beam of loom’; W car- fan, f. 'support-beam, rail, bar
Kermn- (2) “clear, plain, straightforward" Arm. setn ‘clear, plain; W carn ‘downright, arrant
(Kermuks-, see keromuso(n), etc. Li. šermukšnis, Sermuksne ‘rowan’
Kern- “bone, horn”. Cf. Krn-, Kersno- and WP I, 405 Per. sarne ‘horn, clarion’; Gk. (ambig.) kérna ‘vertebrae, spondyls"; Ir. cearn, pl. -a & ceirn, m. ‘corner, angle’; W cern, pl. au f. jowl; Br. (isophonic extn. of type Ker- ‘head’: kern, f. “top, tip, crown of head’. Here?); Cz. střen, m. ‘pith, bone-marrow’ (beside tfen, m. ‘stem of fungus’ here ?); Li. Sernas, Sérnas (‘wild boar’, i.e. ‘horned animal). (The semantics of some of the above forms are obscure)
Kernt- ‘horn, horned animal’. Cf. Kern-, Krn-, Kersno- Gk. kéras, gs kératos, n. ‘hore’; OHG hrind, n. or OS hrió, id.; OE cf. hrióer, n. (old pl. *cattle")
613
Keros, om, å (1) (variant of type ker- ‘heag’, cf. also Kər-. WP I, 427 & 449) Av. sārō, m., sarom, n. ‘head’; MIr. cír, f., Ir. cíor, f. ‘comb, crest, top, summit’; OHG hår, n. ‘hair’ (and com. Gmc.)
Kéros, à (2) ‘combustible substance’. Cf. WP L 360 Myc. (queried) kero-; Gk. kerós (Doric: -ē-), m. (‘beeswax’. LW or inherited (?) in Lat. cera wart OCS (and com. Sl.) séra ‘sulphur’; cf. also Blg. sěrěj, m. ‘tallow, lanoline'; Latv. sērs, m. (‘suiphur’. But Lithuanian siera, f. id. is a Slav LW)
Keros (3) ‘dapple, marked with grey or black’. WP I, 360 & 420 Skt. Saráb ‘motley’; Per. sar ‘starling’; Gk. cf. kerülos “blue kingfisher’; Ir. ciar, MIr. cíar “dark, brown, black’; OCS sérü (and com. SI. *grey^); Li. cf. šeřkšnas ('greyish', from a type *Kersnos); Scots cf. haar (/sea-mist, from Norse?). Cf. OHG harinc, sm. ‘herring’
Kersnos, om, ios, à (Ker?sno-) “crust of snow or ice’. WP I, 409 Arm. sarn, gs sarin, absg -amb “ice, frost’; ON hjarn, n. “hard snow'; OHG cf. (zero-gde) horn ‘January’ and G Hornung ‘February’ be- side Ger. Harsch, Harst ‘crust of snow’; OCS srénü ‘hoary, frosty’; Slovene sren, m. “crust of snow? and sre$ ‘tartar’; Slovak srieň, m. *hoarfrost'; Latv. sersnis “crust on snow’; Li. (with implied glottal stop) Serk$nas, Serk$nà ‘crust of snow, rime’
Kertios, io (?) “cloth, rag’. Cf. kert- Skt. Satah “strip of cloth’; Ir. (ambig.) ceart ‘rag, cloth?
Kerto “hit, encounter, stab, strike’. Cf. Kerið (1), kert-, kort- Skt. Satami ‘pierce’; Lat. certo, are “fight
Kertos, is firm, hard, solid". Cf. kertos, kerd-. (Gmc. & Celt. ambig.) Oss. särt-, cpds. “firm-?; (Iran. LW in Tk. sert “hard, strong, severe'?); Arm. sert, Let (‘solid, firm, sincere, rich, fertile"; Ir. ceart, m. “justice, right; W certh ‘evident; MHG (?) hért, gs hérdes “earth, soil, hearth, home? (qua terra firma?); OE heoró 'hearth, home?
```


## [2026-09-06T22:51:18.714Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nd=open('IEC.txt',encoding='utf-8',errors='replace').read()\npages=d.split('\\f')\nfor i in (371,372,373):\n    print('=== leaf',i,'===')\n    print(pages[i][:3500])\nEOF",
 "description": "Print IEC leaves near p.663"
}
```


### [2026-09-06T22:51:20.407Z] TOOL RESULT

```
=== leaf 371 ===
atsche “slut”, and Icel. laska, v. *damage'; laski 'flaw")
ladstos “weak, faint, immature, frail’. Cf. lados (ladsKó) Lat. cf. sub-lestus “weak, faint, slim, slender, trivial; Alb. i lashtë “immature, premature, early’; cf. the superlatives: OS lezto (letsto) ‘last’; OHG lezzist, OE latost, Du. laatst, etc.
lādh- (?) “lying, lurking, resting’. Ambig. cf. lendh- Gk. lóthð (Dor. -à-) ‘lurk’; lethe, f., léthos, n. ‘forgetting’; cf. also a-l&thés (lit. 'unhidden', hence “evident, true’); MHG cf. (?) lette, wm (soil, loam’, fr. *ladhjo?) and Swiss lóter (flat, of wine”, fr. *ladhrio-?)
lag- (1) limp, weak; be limp, slack’, etc. (Gk. ambig. Cf. slag-). Cf. WP II, 381 & 712 (For Gk. lagaíó ‘release’; lagarós ‘Hmp, loose? see slag-); Olr. laigiu, adj. “less; Ir. lag ‘weak, low, base’; lagaim, tr. ‘weaken’; intr. ‘relax, flag’; laige, f. ‘weakness, swoon’; W Ilai, adj. ‘less’; Cor. 18, id. (: Olr. laigiu, id.); LG lack, m. ‘flaw, fault; ME lack, wd: ON lakr, adj. ‘deficient’ beside lakra, v. ‘deteriorate’; G lech ‘parched’; cf. MHG lechezen, v. ‘pant, thirst’; G lechzen, id.; OFris. bi-leka, id. For Sequan- jan lagit, also written lag-, la- ‘damp; damp- ness’: W llaith, adj. & s. m. damp; moisture’. See next entry
lag- (2) ‘wet, damp; drip, run, flow’. Cf. lag- (1) and ulg- Alb. (ambig.) lag, v. ‘wet; Gaulish (Sequanian of Coligny weather diary) lag-, la-, lagit *damp; dampness’; W llaith, adj. & s. id. MHG lecken, tr. ‘wet’; G lecken “leak? beside leck, adj. ‘leaking’; OE leccan, tr. ‘water’; G dial. lack, adj. (D ‘leaking’; (2) ‘stagnant’; Du. lek, n. “leak, outlet’; Sw. laka, v. ‘run, drip, flow’; lake, w. n. ‘sap’. The Albanian form may derive from a type ulg-, q. v.)
lag- (3) ‘seize’. Cf. slag- and WP II, 507 Gk. (ambig.) lázomai, lázumai, id. beside ko-
659
lázo (?) ‘restrain’; OE læccan, id.
lag- (4) (?) ‘kick. Cf. slag- Gk. (ambig.) lázo, id. beside láx “with the heel; MHG lecken (2) ‘kick’
lag- (5) ‘hollow, lake, puddle’. WP II, 423. Cf. laküs It. (ambig.) lag, m. pl. -a, m. *hollow, cavity’; W cf. lleyn, pl. -oedd, m. (“low strip of land’, fr. *lagino-); OHG lahha, G Lache (1) ‘puddle’
lag- (6) (?) Skt. cf. lagnah ‘shameful’; OS lack, m. ‘flaw, fault; ME lack, id.; Du. laken, Fris. lekje “blame”
lag- (1), lagaio “look, see, watch". WP I, 381 OS lokoian look"; OE locian, id.; OHG (west- ern dial.) lokén ‘peep out; MHG (W. dial.) luoke, wf. *hideout'; Latv. lagot, inf. ‘notice’; laga, f. “sense, insight'. Ambiguously to Skt. ragah, m. “colour? and Latvian lags, adj. “fine, noble’
lāg- (2) ? (leg-? legh-?) Per. ray ‘meadow, slope’; ON lækt, pl. lækir, m. ‘brook’; Alb. (ambig.) log, m. ‘green, grass plot’ (but Mod. Gk. lóggos ‘thicket, wood? is said to be fr. Slav. *logü as in Cz. luh “low- land meadow’. A variant of type *lag- may arise in Srb. laz, m. ‘field’; Slovak laz *upland', Cz. iaz ‘meadow’)
lagos, lagos, lágaio , etc. see lag- above, lāg- (1)
laĝ- ‘wind, creep; twist, winding object, creeper’ Per. raz ‘grapevine, vineyard’; OCS loza, Blg. lozà ‘vine’; Ukr. loza, f. ‘willow’; R lozà, f. ‘branch’; Norw. cf. (?) lakke ‘draw near’
(lag- ‘stop, flag’, see slag-. Gk. lego ‘cease’: Alb. lodh ‘tire’ ambig.)
laiuos ‘awry, left-handed, crooked; lefthand' WP II, 378 Gk. laiós “left-hand; sinister’; Lat. laevus, id.; Ir. laobh ‘crooked’; OCS. and com. SI. lévü ‘left-hand’
laið ‘roar, bellow, bark’. WP II, 377 Skt. rāyāmi, id.; Per. lāyam, id.; Oss. räin, räjun (w. short vowel: ‘bellow’); Arm. lam ‘weep’; Hitt. cf. sar-làmi ‘cry up, praise’; 
=== leaf 372 ===
o, ati, id. and com. Sl.; Li. loju, loti, id. Nominal forms: R laj, Blg. laj ‘barking, scolding’; Ukr. taja, id.; Cz. láje, f. ‘mob, pack’; Li. lojà “abuse”
láiskð (lasK-) (variant of laio, q.v.) Hitt. sar-lesk- ‘cry up, praise’; Alb. leh, lef ‘bark’; Gk. lásko, v. ‘howl, bay’
lak- (1) ‘têar, rag’. Cf. lakt- (1) Gk. lakís, f. ‘rag, rip, têar’; Lat. cf. lacer, adj. ‘tearing, torn, ragged’; cf. lacinia (2) ‘rag’; Li. laka f. (?) “hole, opening’; cf. lakatas ‘rag’; lakišiai, pl. (a pricky planť; Latv. cf. lakats *kerchief, shawl
lak- (2) ‘kick’. Cf. lakt- (2) Gk. cf. láx (^with the heel". Ambig. cf. lag-); laktízo ‘kick’; Per. cf. lakd, s. ‘kick’; Lat. cf. lacertus “lizard?
lak- (3) “lap up, gulp, gobble’. WP II, 380 Arm. lakem, id.; lak ‘porridge, pap’; W (long- gde) llawg, f. ‘gulp’; OCS loco, lokati ‘lap’; R inf. lokàt, id.; Cz. lokat, id.; lok, m. ‘gulp’; Li. laku, làkti “lap up’; Latv. loku, lakt, id. (pres. tense fr. *lank-); laka ‘swill, mash’. (The composition of Gk. ko-lax, gs -lakos ‘flatterer’ is uncertain)
lak- (4) ‘shout, bawl, abuse’ Gk. aor. élakon, fut. lakēsomai ‘bark, shout, din’; OHG, OS lahan “abuse, scold’; OE lean, p.t. loh, log ‘blame’; cf. OE leahtor, m. ‘vice, evil’; Du. lachter, id. (beside OHG lastar, n. cf. also prob. Gk. lásthé ‘mockery, insult. Cf. also ON lostr “evil, wrong, harm")
lak- (or laK-? Cf. lako. Gk. ambig.) Gk. lēkéō ^womanize'; lëkó, gs lekoüs *phal- lus’; Skt. cf. raka ‘goddess of fertility’. (Doric: -à-)
laks- (?) jump; lumping horse’ It. lacca “leg, haunch’; cf. Lat. lacertus ‘fore- arm; leg-muscle; lizard, newt? (?); Sw. lägg, m. pl. -ar ‘calf, thigh-bone'; Ukr. cf. loSak, m. ‘colt, foal; loša ‘filly’; Latv. cf. lakstu, -it Sump’.
làks- (?) variant of lásik-, q. v. W cf. Iochi, 3s. fut. llawch ‘fondle, cherish’
laksos, us ‘loose, slack, limp, flabby’. WP IL, 712 Lat. laxus “loose; wide; open’; W Hac limp! m.
661
‘quicksand’; OIr. lacc, adj. ‘feeble, sluggish’; OBrit. cf. am-lais ‘limp’ beside Br. laosk, adj. (ax, loose’. Vowel?); ON lọskr (^weak, good for nothing’. Here? cf. *ladsKo above); LG lasch ‘tired, faint; R cf. (?) lox- in lox-maàtyj, adj. (shaggy', but cf. *lak- (1) and *lakt-). (Am- big: Blg. Srb. loš “bad”, perh. fr. *loksios, q. v.). Cf. Lat. laxare ‘loosen, release’: Olr. lacaim ‘weaken’
lakstis, à (lakt-) ‘stick, stem, branch, bar. Cf. variant slaKtis Prakritic, Pali latthi ‘stick’ (cf. Skt. lakutah *cudgel); Arm. laxt, Let ‘stick; cudgel’; Gk. laktis, gs -os, f. ‘pestle’; Alb. las&, Ilasë ^wash- ing-stick'; Sw. läckt, pl. -er, m. ‘stick, slat, lath’; Blg. lost, m. Char, bolt. LW in Mod. Gk. lostós, id.); Li. lakstà, laktà ‘perch’; Latvian laksts, m. ‘shoot, sucker’ beside lakta “perch?
lakt-, lakot- “rag, scrap, tatter'. Cf. lak- (1) Skt. (dim. type) laktakah ‘rag’; Per. laxt, laxd ‘scrap’; Arm. lať ‘garment, cloth, rag! beside lati ‘scrap’; Li. lákatas ‘rag’: Latv. lakats "ker. chief; cf. also Li. lákStas ‘sheet of paper, quire’
lakt- (2), see lak- (2) ‘kick and cf. slak-
lakús, lakuos ‘lake, pool, puddle, pond’. WP II, 380 Gk. lákkos, m. ‘pit, puddle, tank’; Lat. lacus, gs. -üs, id.; Olr. lac, Ir. lag, m. *water-hole, pooľ beside (augmentative) lagán ‘puddle’; Br. Cor. cf. lagen, pl. lagennu, lagennow, f. ‘marsh, pond’; OE lagu, m. n. (lake, flood’; pl. ‘surface of the sea’); OS cf. lagu-stróm ‘waters’; ON lọgr, gs. lagar, ds legi, m. ‘sea, water; OCS loky, gs loküve, m. ‘puddle’; lokva, f. ‘rain’; Blg. lókva, Srb. lókva ‘puddle’
laKəsos (laksos) “salmon”. See next. WP II, 38
=== leaf 373 ===
ME lax, id.; ON lax, m. id.; R lososi, Cz. losos, m. id. cf. R (doublet, fr. Finno-Ugr.?) lox, m. ‘male salmon"; Li. lasiSas, -a, m. f. beside lašaša, f., id.; Latv. lasis, id.; OPr. lasaso, id.; Finn. LW (?) lohi, id. (whence R lox?) For laka, Da (qua *Jeaper?), see laKüs & cf. lakó
lakstis, à (lakt-) — làmos, a (ulàm- ?)
20
25
30
35
40
45
662
lako, ið (variant: las-) jump, dance’. Cf. laKosos, laKüs, (lakitio) Skt. cf. (variant) lasāmi (2) ‘dance’; lásayami, id. (and “cause to dance; ply an art'. The se- cond form given also as lasSayami); Oss. lásín (drag, lead; take; weigh". Semantics obscure); Gk. lekáo (‘dance to music’; vulg. ‘coire’); Alb. los, v. (play, fr. lakið); Pol. tasic ‘swirl, twirl; R dial lásit', id.; Li. lóSiu, ti ‘play’; cf. at-si-losti “rear, jump up”. Variants include Romani loSanav man ‘rejoice’ (with -š- for IE *-K-); Latv. lakstit, inf. “jump”; cf. perh. Lat. lacerta ‘lizard’? beside lacri-müusa ‘green li- zard’; Gk. lakáo Churst Cf. G springen in this sense) beside Hes. *lakertizo (misspelt lik- jump?)
laKos “drip, gum, resin’. (Variant of las-, q. V.) Skt. lasah ‘gum, resin’; Li. lásas ‘droplet’; Latv. lāse, f. id. (from a type *laKjo, with tonal lengthening)
laküs, (aka, laKitio) ‘bounding animal, weasel’. Cf. laKo, laKosos Per. rāsū ‘weasel’; Srb. lasa, id.; OCS. Cz. lasica, lasice, id. (an echo of this root may be present in Li. lašvaras "rout?
lal- (expressive: lall-) “dle, twaddly; idling, twaddle’. WP II, 376 Skt. cf. lalami ‘lisp’. Cf. Cz. Slovak lalolat, lalolat, inf. ‘prattle’; Hitt. cf. lalas or lala (queried: «tongue; Arm. cf. lalonk, s. pl. type ‘dirge’; Gk. lále ‘prattle’; laléo, v. id.; Lat. cf. lallus, 1, m. ‘lullaby’; lallo, are ‘lull — an in- fant; LLat. lalla ‘prattle’; MHG lallen, tellen, v. ‘twaddle’; G Lälle, f. ‘tongue’; cf. Lall- wort ‘childword’; Du. lellen, v. ‘prattle’; Sw. lali, n. id.; Srb. lola ‘vagabond’ beside lolati se “lounge, laze'; Li. lalu, ett ‘whoop, cheer’; laluoti, inf. ‘twaddle’; Latv. cf. lalināt, inf. *prattle, lisp’. (W 101, f. ‘prattle’, Holio, inf. id. seems to represent a variant of type *lol-)
(lam-, see lem- and lom-. Only thus in Osc. lamatir “let be broken? or sim.)
(lamb- “hang”, etc. see lembos, lomb-)
là-mi ‘seize’. Cf. lou-, lau- Skt. Jami, id.; Gk. cf. leízomai, id. (but perh. *lau- in view of Myc. rāw-, in some cpds.)
làmos, à (ulàm- ?) “depression, bog, morass,
663
mess”, Cf. WP II, 385 Oss. lámi ‘mud’; Gk. lëmë ‘rheum’; Alb. llom (mud'. The initial suggests a type *ulam-); Lat. làma ‘marsh, puddle’; MLG cf. (?) wlom (muddy. See ulàm- as a variant); Blg. lam, m. “hole, ditch’; Li. lomà *towland'; lomus, adj. ‘low-lying’; Latv. làma ‘puddle’
lang- ‘drooping, sad; droop, be sad; sad- ness'. All evidence ambig. Per. ranja, ranjiš ‘sorrow, annoyance’; ranji- dan, inf. “be sad’; Gk. laggázo, laggéo ‘droop, flag’ beside lagarós, adj. ‘sunken, slack’. (For Lat. langueo, *slangu- and for Gk. lego: Alb. iodh, see slāĝ-)
lank- (1) ‘pair, liken’ Hes. lágko ‘resemble’; Pol. łączyć, tr. "on: Ukr. lučyty, archaic Cz. loučiti, id.; W cf. llaing, pl. lleingiau, m. ‘clasp, enclosure’
lank- (2) ‘thrust, fling’ Lat. cf. lancind, are ‘penetrate; têar, lay waste’; OCz. lučiti, lučeti, Slovak lučiť ‘throw’. (For OCS lọčiti ‘separate’. See lenquo, lonqu-.)
lank- (3) (?) ‘platter, dish’. A wanderword? Gk. gloss: lágkē, lágkla, f. id.; Lat. lanx, gs lancis, f. id.; Srb. lónac, Blg. lónec, m. id. (Srb. gs: lonca)
lànos, is (1) ‘flat; surface, plain’. (For Celtic lann, etc. see p
```


## [2026-09-06T22:51:30.508Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nls incoming/BQT/ ; wc -l incoming/BQT/BQT_v3_pages.txt 2>/dev/null; head -c 600 incoming/BQT/BQT_v3_pages.txt",
 "description": "Check BQT v3 pages file"
}
```


### [2026-09-06T22:51:30.553Z] TOOL RESULT

```
BQT_v3_pagemap.json
BQT_v3_pages.txt
BQT_v3_picofile.pdf
BQT_v4_pages.txt
BQT_v4_pages.txt.pages
BQT_v4_picofile.pdf
BQT_v5_pages.txt
BQT_v5_pages.txt.pages
BQT_v5_picofile.pdf
51425 incoming/BQT/BQT_v3_pages.txt
[pdf page 1]
[NOT OCRED - use tools/ref_page.py]
[pdf page 2]
7
Ub
sits k ge
AS ۱۰۶۲ ‏نتف‌بال‎
‏ومع‎ ‘oo ‏داي و‎ el Oe

far
en rotons ‘ ‘ ths ۰ ‏دیهان‎
‎۳ 2 7
۰ SF Ps
On Awe
۰
‏-ل‎ 9 ‘il
۱۳۴۳ ‏چاپ دوم فروردین‎
‏با تجدید نظر کامل‎
‏بسرمایه کتاپفروشی ابن سینا- تهران‎

|

چاپ افست ر شدیه
[pdf page 3]
اداره ‎“oes‏
‏ساره و6۷ ۲۰۹

pe ۰ ay sf s ‏ار بخ‎
‏سرام ودارت‌شسات‎

د انشمند محتر ,آقای‌د
```


## [2026-09-06T22:51:30.566Z] TOOL CALL #13: Bash

```json
{
 "command": "sed -n '1,80p' tools/ref_page.py",
 "description": "Read ref_page tool head"
}
```


### [2026-09-06T22:51:30.603Z] TOOL RESULT

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


## [2026-09-06T22:51:34.922Z] TOOL CALL #14: Bash

```json
{
 "command": "ls data/verification/sources/refs/ocr/ 2>/dev/null && ls data/verification/sources/refs/ocr/BQT 2>/dev/null | head -50",
 "description": "List cached OCR pages"
}
```


### [2026-09-06T22:51:34.972Z] TOOL RESULT

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
TAD
0001.png
0001.txt
0049.png
0049.txt
103.vision.txt
1092.jpg
1092.vision.txt
1187.png
1187.vision.txt
1219.png
1219.txt
1219.vision.txt
1223.png
1223.txt
1225.png
1225.txt
1225.vision.txt
1226.png
1226.txt
1237.png
1237.txt
1237.vision.txt
1261.png
1261.txt
1266.png
1266.txt
1266.vision.txt
1267.png
1267.txt
1267.vision.txt
1272.png
1272.txt
1275.png
1275.txt
1279.png
1279.txt
1280.png
1280.txt
1280.vision.txt
1294.png
1294.txt
1294.vision.txt
1296.png
1296.txt
1296.vision.txt
1297.png
1297.txt
1298.png
1298.txt
1299.png
```


## [2026-09-06T22:51:37.865Z] TOOL CALL #15: Bash

```json
{
 "command": "for p in 1879 1880 1902; do echo \"########## BQT:$p\"; python3 tools/ref_page.py BQT:$p --image 2>&1 | head -60; done",
 "description": "Fetch BQT pages 1879 1880 1902"
}
```


### [2026-09-06T22:51:55.168Z] TOOL RESULT

```
########## BQT:1879
IMAGE: /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/1879.png
REF: BQT:1879  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 676  OCR-lang: fas

-۱۸۷۹- لالاسرا
میگویند۱ - و درعربی بمعنی‌خابیدن وجاویدن | معرب لال امت ۷ .
باشد ۳ #۰ ال < پر وزن کالا» بمعنی غلام و بنده
لاعچه ۲ - بر وزن باغچه ۰ بمعنی وخدمکار باشد ۸ - و پر کوبی وهرزه چالگیرا
تتماج باشد وآن آشی است معروف . نیز کوبند ‎٩‏ - وگیاهی‌هم هست کهآ ترا ازجانب
لاکن < بفتح ثالك بروزن لادن» بممنی | مکه‌آورند وبخورآن دفع علت بواسیرکند *۱-
لاشکن است ۴ و آن کوهی باشد نزديك بملك و بمعنی درخشنده هم آمده است چنانکه گونند
روی . لولوی لالا بعنی مروارید درخکنده هگ وداته
لال - بر وزن مال » ممروف است که ایست مانندکنجد - و بعنی کوبند باین هعنی
کنگه و زبان گرفته باشد ‎٩‏ - و رنه سرخ‌زا و ممتی دکزار در لفی عربی است. ۰۱۴
نیز گفته اند ‎٩‏ - و بمعنی لمل هم آمده است لالاسر! - بفتح سین بی نقطه.خواجه
وآن کوهربت گرانهایه که معدنآن دریدخشان | سرا را کویند بعنی غلامی که آلت تناسل او را
است و بعربی لعل کویند . و یی کویند لعل | بریده باشند .
۱ نلکه * لکات « اسراج نا
با مردم لک با بتوانی بمیامیز زیرا که جز از عار نیاید زلك و لاکه .
عیوقی . حاشیهٌ فرهنگه اسدی «لغت نامه ».
۲ - در عربی خایدن « لو که » است و « لا4 » فعل ماضی آنت . « لغت نامه >.
۳ «لاکده * لاخده * لاخشته < لخشه . ۴ ره : لاشکن .
* -کردی [12 « ژابا س ۳۷۹ در راك ( سلطان]آ باد) یز 18[1«مکی‌نژاد» کیلکی[4ا.
۹ - دو لب چو نار کفیده . دورخ چو سوسن سرخ
دو رخ چو لار شکفته . دو الب چو لاله لال -
عنصری بلخی « لغت نامه » .
۷ <لمل معرب «لال» است « نخب ۱۶ . « لال » لعل باشد » « لغت فری ۰.۳۲۹
۸ دلله :
قیصر از روم ونجاشی‌ازحیش ‏ بردرش‌فیروز ولالا دیده‌ام. ‏ خاقانی شروانی « لغت نامه > .
‎٩‏ - بدین معنی « هرزه ۷ > است . سراح‌اللغات بنقل فرهنگه نظام چ ۵ ص م -
۴ رك : تحفةٌ حکیم موْمن . لغت نامه . بمعنی اخیر عربی است . سراج‌اللغات بنقل
فرهنگه نظام چ ۵ ص م - ۹ از عربی 0۸ >« لغت نامه > .
اریگ درعر ی بمعن ی گیاه مذ کور آمده ‌- والالا» بمعنی نه‌نه (تکرار درنقی ( است.
۴ از : لاله ( خواجه . غلام )+ سرا (سرای) * لاله سرا (ه.م.)
۰ لاك پشت - بضم چهارم . (رك : لاکه) . جانوربت از راستة لاک پشتان » پرنکه
زرد مایل ببز با لکهٌ سیاه . خوراك : چ
ال مرن« َ- ور رت ترجه جاهد.
ه ع ۰ - ِ ۹ ۹۹۴ ۹ / 6 5
ری علف و ربعة گیاهان است « ری ۹ جر 0 کي ن
نیز از حغرات تغذریه میکند . بهنگام رز 0 اکن
خطر اعضای خارجی خودرا داخل لا4 : اساط ی یت ۲ ار
میکند . تخم لاد پست ازپوستة آهکی [ سس یگ وی بیس وه اه
سفید پوشیده شده است .

########## BQT:1880
IMAGE: /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/1880.png
REF: BQT:1880  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 677  OCR-lang: fas

لالی - ۱۸
که خودرو باشد عموماً - و لاله داغدا رکه آترا
لاس - بفتح لام وسکون سین‌بی نقطه, ۶ خودرو باشد. عمو - و لاله داغدار اس
ی : لاله نممان‌خوانند خصوصا.
نوعی از پارچهٌ ابربشمی خوش قماش نازك لطیف وآن برچند نوع است: لالةٌ
8 هی ‎٩‏ ‌ + باه 1 ۰ ۰ ۳
و سرخ باشد و بزبان علمی اهل‌هند بمعنی کوهی ولالهٌ صحرائی‌ولالةٌ
روی باشد که بعربی وجه خوانند ۴ - و دوستی: شقایق ولالةٌ دل سوخته
دا ده د. 8 ۷
ومحبت را نیز گوبند ولالهٌ دلور و لاله خطائی
لا زد الا , کنه :
لش - بروزن کالك , کفش وپای‌افزار و لاله خود روی ؛ و بعضی
راکویند ۳ سا وتاج خروی‌را هم گفته‌اند وعر بان بدیشگوته آورده‌اند : لاله
تاجرا | کلبل خوانند ۴ . ۱ لاله درد ولا اه
هن راع سرخ‌و زرد ولاله سفید
ارچ - بفتح ثالث وکاف‌بالف کشید» | ولال‌آن و لاله دوروی‌ولال لاله
بمعنی‌لالك‌است که کفش وپای افزار- وناج‌خروی | نعمان - وکنایه از لب معشوق هم هست: .
ادن لاله دختری - بن‌دادبی‌ضله. نوعی
لا لفگت - بروزن پاسنکه . بمعنی زله از لاله است که کنارهای آن بغایت سرخ رنگه
باشد و آن‌طمامی‌است که مردم فرومایه‌ازمپمانیها | باشد و میانش میاه وآنرا آذرگون‌خوانند ۸ -
بردارند ‎٩‏ - و نان پارهای کداییرا نیز کویند. | وبعربی شقایق‌اللممان گویند .
لاله ۷ - بروزن هاله, هر کلیراگویند لاله‌سار ‎٩‏ - با سین بی نقطه بروزن
۱ -که در قدم باغ کشد فضل تو دیبا که بر سرکهسار نهد حکم تو لالی.
بدر جاجرمی « لغت نامه » .
۴ - «لالی بمعنی روی در هیچ لغت سنسکرت یافت نشد .> « چك ص ۹۹۵ ح >.
۴ - شاید در اصل بهای افزار لال ( سرخ ) رنگه اطلاق میشده « هرمزدنامه ص 2۱۳۲
< لا < لالکه ( ممرب ) « معجم الادباء چاپ مارگلیوث ج ۳ ص ۱۹۶ > لالجه ( معرب )
« معجم‌آلادباء اساً ج ۱ص ۳۳۵ :
دربغ ازان شرف و خوبی و فتایل او که عاشق‌است برآن لاله روی لالك دوز.
سوزنی سمرقندی « هرمزدنامه ص ۱۳۳ 3« لغت نامه » .
۴ سلاح د لت نامه » . ۰ «لالکه (هم.) :
بل تا کف پای تو پبوسم انگار که مهر لالکاییم . «سنایی غزنوی ص۹۹۱ ۰
‎٩‏ - مرئیه سازم که مردی شاعرم تا ازینجا ب رکه و لالنگی برم.
مولوی بلخی رومی « لغت نامه ‎ »‏
‏۷ « آلاله. درپهلوی بافته نشد؛. وشغك نیست که این کلمه با « لال > ( سرخ ) رابطه
دارد و کلی که لاله خوانده شدء بمناست رنگه آنت « هرمزدنامه ص ۱۳۷ »» کردی لاله ط
(لاله ) « ژابا ی *40 4 ۰ نی زکردی ع 1816 « ژابا س ۳۷۹ ؛ لاله ( 70628 ۳808۷۵۲)
« هرمزدنامه ص ۱۲۹ . 11106 از دستهٌ سوسنها از تبرء سوسنی‌ها ( 0669هالشآً ) است
که کاسه و جام‌آن تشکیل جامی قشنگه و کامل میدحد « کل کلاب اس ۲۸۱ .
۸ - رد : آنرکون . ‎٩‏ - از: لاله (سرع) سار (< سر)؛ لاله سارباید مرغی
باشد سرسرخ » چنالکه خشنار مرغی‌است سرسفید :
آسدی طوسی باخطیری « هرمزدنامه سس ۳۵۱ >

########## BQT:1902
IMAGE: /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/1902.png
REF: BQT:1902  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 699  OCR-lang: fas

عائی ۱۹۳۳
- وآلت تناسل را نیز کوبند ‎٩‏ . و سردیگرآن درگلوی‌آسیا باشد وبوفت گردش
لکانی - بروزن هوائی . بممتی سرخی | آسیا صدائی از آن ظاهر کردد و دول بسبب‌آن
و رلگه سرخ باشد » چه کل سرخ را لکا چوب حر کت کند وکندم درکلوی آسیا ریزد .
میگوند . لگن ‎٩‏ - بروزن جمن ؛ طخت بی‌آفتابه
لک ۴ - بکراول وفتح‌نانی وسکون باشد ؛ و باین معنی با کاف فارمی هم آمده‌است
کاف ۰ آلوی ترش راگوبند . - و شممدانرا نی ز کوبند - و بمعنی عود سوزهم
: نظر آمده است که عربانمجمره خوأند ی
کل « بکس اول و فتح ثانی و سکون ظرا ۳ مر‌بانمجس, شوش وم
لام . میوه ایست که آنرا امرودکوبند و بمریی ۱ اش دا هم میخوشد - و جامه شاوی دا یز
کمتری خوانند گفته‌اند و معرب آن لفن باشد .
کل - بنتح هر دو لام و سکون هر لك و پك - بنتح اول و بای فارسی
دوکاف, سخنان هرزه وباوه راگوبند۴ - وبکس و بضم ثانی و اسکون کاف درآخر » این لغت از
هر دولام ۰ چوبکی باشد که بر دول آسیابعنوانی توابم است و تفیر عبارتی که در غربی جات
نصب کنند که چون آسیا بگردش درآید سر آن مزجات گوبند و بمعنی اسباب و ضروربات خانه
چوب حر کت کند وبدول خورد ودول‌را بجنباند از فرش رده وگستردنی و پوشیدئی و غیره که
و دانه دی درگلوی آسیا ریزد ۴ . قی‌الجمله کهنه و مندری شده باشد ۷ -وبمعنی
لکلکه؟ - بنتم‌هردولاء بروزن وسوسه. پیپشن هم آمده است که درمقابل هنرمند است -
سخنان هرزه و بیهوده باشد - و بکسر هردولام» و تکاپوی و آمد وشد با تعجیل را نی ز کوش ۸
چوبکی‌باشد که يك سر آنرا بر دول‌آسیا بندید | -وجنم اول وبای قارسی» هرچیز کنده ناتراشیدهرا
(۱) چش : فروش .
۱ - بهردو معمی :
گر زانکه لکانه است آرزویت ( لکانه‌ت آرزوست ) ابنك بمیان ران . لکانه .
طیان مرغزی « لغت فرس ص 4۳۲ » « لغت نامه >.
۴ - عربی‌است . رك : منتهی‌الارب » محیطالمحیط . ۴ «دلکلکه .
۴ -چون لكلك است کلکت برآسپای معنی ‏ طاحون زآب کردد . از لکلکه معین
زان لکلك ای برادر کندم زدول بجپد در آسیا در افتد معنمی زهی هبن ۰
مولوی بلخی رومی «لغت‌نامه». (جگ
- ونیز لكلك * لگلگه (م.م.) < لقلق (عر) . اکدی 120421802 (نام پرنده) (
دیمرن . لفات دخیلهٌ کدی ص۵۲ ؛ پرنده‌است ازدرازپایان باگردن وپای :۹
دراز سفید رنگه بابالهای سیاه که در بهار بر بالای خانه های بلند با درختان لانه 1 ی
سازد . * «لكك . ‎٩‏ - اسح «لگن» (هم.) است . 1
۷ - آورد لك وايك ز برای من مسکین :۳
با آنکه لکیس داده‌ام از بهر جناعت ۰ ی ی
امیر خسرو دهلوی « جهانگیری ». ۳
۸ - صجدی لام او نو نیز مبر چه کنی خیره گرد اولك و پك. َ
مجدی مروزی « لغت نامه ». لکنك
```


## [2026-09-06T22:52:50.471Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BQT v2 963 ===\"\npython3 - <<'EOF'\nimport re\nd=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\n# find pdf page tags\nidx=[m for m in re.finditer(r'\\[pdf page (\\d+)\\]',d)]\nprint('num tagged pages',len(idx))\nEOF\ngrep -n \"رنج\" BQT_v2_pages.txt | head -5",
 "description": "Inspect BQT v2 text"
}
```


## [2026-09-06T22:52:51.317Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['MON','AFM','PLA','TAD']:\n    print('=====',k); print(json.dumps(d[k],ensure_ascii=False,indent=1))\n\"",
 "description": "Full metadata for MON AFM PLA TAD"
}
```


### [2026-09-06T22:52:52.158Z] TOOL RESULT

```
=== BQT v2 963 ===
num tagged pages 0
1537:           ‫و کاف » محنت و رنج و بلارا گویند ‪.‬‬             ‫جتن و گریختن باشد و طم اول ماضی‌جتن‬
2026:‫ساحران ‪ -‬و کنایه ازکی است که رنج کش‬                           ‫و‬
2849:‫و مبرآخور را هم کفته‌اند که رش سفید طوبله‬              ‫رنجوریرا گویند که ابام قاهت او باشد و بوفت‬
2920:       ‫چون کرنجی که فر وکوفته باشد بجواز ‪.‬‬                   ‫ای بکوپال کران کوفته پبلان رایشت ‏‬
4274:  ‫پایین تر ازآن‌کلمة «ابرنجین تورجی» لقب گمیغخوالتیوودرمیانه‌دابره‌ای کشیده و ازنیم درهم تا‬
```


### [2026-09-06T22:52:53.950Z] TOOL RESULT

```
===== MON
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
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt"
 ],
 "page_offset": null,
 "covers_etymology": true,
 "notes": "covers_etymology = partial: origin-language tag visible online, Latin etyma missing. The a'lam volumes (MON5/MON6 citations, e.g. MON5:528) are NOT online: vajehyab's Mo'in has no proper-name entries (tested افراسیاب — only compounds returned); abadis shows Dehkhoda and 'فرهنگ اسم‌ها' instead, which do give Avestan forms (e.g. Frangrasyan) and can serve as a cross-check. noorlib has no Mo'in 6-vol entry found. The 6-vol edition itself was not found on archive.org, Google Books or HathiTrust full view. || RE-SEARCH 2026-09: still no scan of the 6-vol Amir Kabir edition (incl. vols 5-6 اعلام) on archive.org, Google Books (API quota-limited; WebSearch found no record with preview), HathiTrust (no record surfaced), noorlib, ketabnak (author page persons/6040 lists 34 Mo'in titles, none the 6-vol فرهنگ), tarikhema, picofile, scribd, Commons/Wikisource. Only the 2-vol Adena condensation exists (archive.org, mirrored on ketabnak 65980/65981, picofile, persianpdf, scribd); its image PDFs were downloaded to incoming/MON/ (the _text.pdf variants with OCR layer are at the same archive.org identifiers). The 6-vol set is purchase-only (in print: iketab.com, bookroom.ir/book/97022, 30book.com/Book/32100).",
 "cites": "page number of Mo'in's six-volume Farhang-e Farsi; MON5:… / MON6:… = volume 5 / 6 (proper names)"
}
===== AFM
{
 "title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)",
 "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM.txt"
 ],
 "page_offset": "198 leaves; page numerals OCR'd unreliably — offset approx leaf − 8 (front matter); confirm on page image",
 "covers_etymology": true,
 "notes": "Arabic OCR fair; Syriac/Latin etyma partially garbled.",
 "cites": "page number of Addi Shir, al-Alfāẓ al-fārisiyya al-muʿarraba (1908)"
}
===== PLA
{
 "title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988",
 "edition_found": null,
 "kind": "archive_djvu",
 "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)",
 "identifier": null,
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt"
 ],
 "page_offset": "301 leaves (pdftotext -layout, \\f-separated): printed page = leaf(1-based) − 15 (leaf 291 = p.276).",
 "lookup_hint": "HathiTrust search-only; Google Books id q_ErAAAAMAAJ snippet view; DDB has only the table of contents. No full text online. | For pages in a scanned volume use: python3 tools/ref_page.py PLA:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)",
 "notes": "Open full text obtained. Alphabetical Arabic headwords with Persian/MP etyma; OCR fair (German + transliteration), Arabic script mostly garbled. Provenance: a user upload of an in-copyright 1988 Harrassowitz book — grey copy; publisher sells it (harrassowitz-verlag.de).",
 "scans": [
  {
   "file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf",
   "first_printed": 1,
   "last_printed": 300,
   "pdf_offset": 0,
   "lang": "deu+ara"
  }
 ],
 "cites": "page number of Asbaghi, Persische Lehnwörter im Arabischen (1988), alphabetical by Arabic word"
}
===== TAD
{
 "title": "Tobia al-Unaysi (طوبيا العنيسي), Tafsir al-alfaz al-dakhila fi al-lugha al-'arabiyya ma'a dhikr asliha bi-hurufihi (2nd ed. Cairo 1932, ed. Yusuf Tuma al-Bustani; later Library of Lebanon reprint) — Nourai lists it under Arabic authors ('Unaysi T.'); its Table IV line was lost in the OCR",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/TOB1932ARAR (1932 ed.); also https://archive.org/details/ar113lang79 and https://archive.org/details/elshandawily14640",
 "lookup_hint": "Alphabetical Arabic headwords; grep the Arabic headword in TAD_pages.txt (86 leaves) or TAD.txt; inside.php search works.",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/TAD_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/TAD.txt"
 ],
 "page_offset": "86 leaves (small book, ~80 printed pages); offset ≈ leaf − 4..6, verify against the printed numeral on the page image",
 "covers_etymology": true,
 "notes": "Arabic OCR fair. Nourai's exact edition unknown; the Beirut reprint reproduces the 1932 pagination."
}
```


## [2026-09-06T22:52:58.831Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 tools/ref_page.py BQT:963 --image 2>&1 | head -70",
 "description": "Fetch BQT page 963"
}
```


## [2026-09-06T22:53:00.389Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AFM لعل ===\"; grep -n \"لعل\" AFM_pages.txt | head -20\necho \"=== TAD لعل ===\"; grep -n \"لعل\" TAD_pages.txt | head -20\necho \"=== TAD لقلق ===\"; grep -n \"لقلق\" TAD_pages.txt | head -20\necho \"=== AFM لقلق ===\"; grep -n \"لقلق\" AFM_pages.txt | head",
 "description": "Grep Addi Shir and Unaysi"
}
```


### [2026-09-06T22:53:00.458Z] TOOL RESULT

```
no scan of BQT covers printed page 963 (see 'scans' in refs_online.json)
```


### [2026-09-06T22:53:00.533Z] TOOL RESULT

```
=== AFM لعل ===
140:9 تلك اللفظة ܬ ܟ احد العلهاء قد صرح 13
704:(النْد) العلّم الكبير والميلة ومن المدش عشرة لاف ومن ܐܢ الفصل او
844:® ( نيط المحيط ) . ! في لم !( هذه بار ذلعلها تصحيف اليونالي
1133:نوع من اللعل »
1585:* (الدرفس ) العللم الكمير والعظيم ٠‏ )0 والضخم ܣ الرجال فارستة
1747:0 ( الدهتج ) 1 تعر يب دهنه ولعلة ܪ وهو ݀ܧ المتكون
1951:* ( + الشر بين ` 6 لغة فيه: لعلّة تعريب £ وهو
2148:= + (السبرَة) طائر ܕܬ يزيدوا عليه ٠‏ فلعلة معرب سباروك وهو الام
2219:من العليود واميوانات فيد بطون على أرجل كل منها حزمة من حشيش ثم يطلقومسا
2325:آبنوس وغيرهم الشيزى او شجر تعمل ܘܬܘ ܐܢܝܢ ( حيط الحيط ٠)‏ لعل معنى ساسم
2510:ولعلها ععناها
2601:تكن العامة ܡ ܚ به طائرًا كثير الوثوب يشمه المراد ( حيط الحيط ) فلعل قول
2663:منعهم وقال: حيث ان اليوم يوم العدل والانصاف لعل هذه الليّة لها حاجة 5 0
2729:الصابون صغة ارامية ٠‏ والعليم عند "اللهل ابت
2731:العسكر وهو ايضأ | سم وعلم ܙ 2:0 ٠فلعل‏ الاصهمذانة نسبة الى اسيهيد
2886:لاوا ن العلاء والمشايخ وهو ܨ ܨ ٠وه‏ 33 0 ܐ
3075:( العلا تج 7000 من اليب واحلوز وغير ذلك ܢ ܝܢ فلا نه
3246:ان ̈ܐܢ ܕܝܪ £ والعلَكُوم ,)£ ; )6 ܕ 7 9 ܕܐܐ حكد
3456:وحماء فلعل التكلمة من ثوافق اللغات
3564:لعل 5
=== TAD لعل ===
32: ‫الى الكير بروحه ونكرة‬        ‫الى من حك العلويغاد على الاادب‬
554:‫العلاملكيير‪--‬فارسي ‪ 2‬بند ‪ 26‬ممنأه عقدة ورباط دعي كذا لانه‬
651:                        ‫يدق ‪ -‬فارسي « ييراق » وهو الرايةوالعلمواللواء‬
654: ‫سموآأ يذلك لاجم علموا | نقفهم بعلامات ‪.‬عر فون ‪ 5‬لان الشرط العلامه ‪ .‬ومثابا الشحنة اى‬
674:‫بمارستان ‪ -‬فارسيمركب من « بما» أي مريض و ‪١‬‏ ستان »أداة تدلعلى‬
1009: ‫معنأه فى الاصل كان العليل وبطلق على المقلسين‬      ‫خورس ل وتاي ‪8‬‬
1057:‫دوّاق ودُرائن لعل العامة حتت هذا الاسمكراقاً مأخورذا عن الباق‬
1101:  ‫فارسي « دوسر » معناه ذو رأسين وبراد بهمسمارمحدد العلرفين‬                               ‫دار‬
1135:‫دمغة ‏ عامي ‪ -‬ترك ( دامغهوطمفه ومنًا» معناهالسمة والوسموالعلامة‬
1140:  ‫‪ 6‬وهو التراب الأتلن او تام العلين اليابس اوأنطينامنك الذيلانها لطّدرمل واحدتدمةنة‬
1552: ‫ومعتاهالاسود لانه فى الاصلكان جلدا مجلد أسود ‪ .‬قال العلامة القرداحي معناه‬
2050:                                                                 ‫االعلرامبعفمىودية‬
2145:‫‪١‬‏‬                                         ‫االعلنباسود الا ان فىلبه عجمة واحدة‬
2527: ‫يمس معئاه سيال وعصارة وف العلب هو‬              ‫وين ‪ -‬وونابي ‪5‬‬
2547:                     ‫لعل حجركم أجمر س‪ -‬فارسبي ‪ 2‬لال » معنا أحمر‬
2710:‫وماس وق ‪ 71‬موميا لعله مأخوذ منوم الفارسي الذي معتاه شمم‬
2963:  ‫قندفمىته ‪ :‬الانبرذور ولعلالمتوج معنى لنفلة الانبرذور‬
3036:                                 ‫العلمية العصر نة تأليفجرجس هام‬
=== TAD لقلق ===
=== AFM لقلق ===
```


## [2026-09-06T22:53:08.489Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== TAD around 2547 ===\"; sed -n '2535,2555p' TAD_pages.txt\necho \"--- pdf page tags near ---\"; awk 'NR<=2547 && /\\[pdf page/ {p=$0; n=NR} END{}' TAD_pages.txt; grep -n \"\\[pdf page\" TAD_pages.txt | awk -F: '$1<2560' | tail -3\necho \"=== AFM search headword al-la'l ===\"; grep -n \"( اللعل\\|(اللعل\\|اللمل\\|الّلعل\" AFM_pages.txt | head",
 "description": "Context for TAD la'l and AFM"
}
```


### [2026-09-06T22:53:10.423Z] TOOL RESULT

```
=== TAD around 2547 ===
                                              ‫الحمّئ ومنشأها بلاد ابرط‬


                          ‫عل النارسة كوه الاراية‬
                                               ‫ل ان س اممز‬

                                     ‫ل‬
      ‫لازورد ‪ -‬فارسي « لازورد ولاجورد ‪ 6‬وهو حجر ‪ 3 1‬أزرق اللون‬
‫اللات ‪ -‬صم هو مؤنث إل األياله افلىاشورية فيكون معنىاللات الالة‬
‫‪,‬لأمع‪ 1‬معناه فرقة‬    ‫وناني لمعم وى الللانيتي‪9‬‬    ‫ا لحنة ولدة ولاجدون ‪0‬‬

                                                             ‫عسكر وجيش‬
                     ‫لعل حجركم أجمر س‪ -‬فارسبي ‪ 2‬لال » معنا أحمر‬
‫ىليونانية معناه حمْرة‬
                    ‫ل م ‪ -‬تركي « (لن »م معناه قناةوعهرى و ‪807‬هلاه ف ا‬
                ‫والمرادبه حشوة‪ 0‬ندس فى ثقب الص<ور فتنسفبا مرادفه نسفة‬

‫لعن و[لكوت فقالارشية ‪ 2‬لكن ‪ 6‬وف اليونانية ‪ 888101‬وى الارامية‬
                                 ‫ف أفنا© ممناه ست من محاس يفسل فيه‬
‫ا وقد يكال‬        ‫الث ‪ -‬فارسي‪ 0‬نك © وهوصبغأجمريصبغبهويطلى‬
                                      ‫الابطالية و‪ 21‬والى الافر نسية ‪6921‬‬
--- pdf page tags near ---
=== AFM search headword al-la'l ===
1949:ورق اللملاب زهره مائل الى السياض و بذره هدورء وفيه لغات بالعرمة 9" ور بعري
3107:* (المْنْك) الساعة من اللمل او القطعة منه تعر يب ܐܥ والفج ܐܝܐ
```


## [2026-09-06T22:53:17.053Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nd=open('AFM_pages.txt',encoding='utf-8',errors='replace').read()\npg=d.split('\\f')\nprint('leaves',len(pg))\nfor i in range(147,154):\n    print('=== leaf',i,'===')\n    print(pg[i][:1600])\nEOF",
 "description": "Print AFM leaves near p.142"
}
```


### [2026-09-06T22:53:19.073Z] TOOL RESULT

```
leaves 198
=== leaf 147 ===
ܕ 311 تب
( الأست) كامة فارسية اسم للبن ومنة التكردي ,)ܝܝ و ܡܣܬܐ بالسريايّة
الدارحة
(ل) ل قيل فارسي ° ( يط الحيط) والصواب !2 تري
0 المس) النحاس 7
+ ܢ الغلام اسن 85 والوحه 39 00 7 5 امن ܘܟ 0
~ ÷
( !]ܚܝ ) فاسي خض وهو 3 الكف ومنة - بالتركة » 2
0 نوع من اطيب :9 فاسي ܕܫܐ ܐܘ ام ام اللرذان ܠܝ الفرس ]
سمعوا بام جرذان وهي كع صفراء قالوا ܐ جاغوا:« اين موثمان» ( اقرب
ܬܕܐܙܒ) ܕܐܐ ܐ نه
( | هد ) اللقاح 09 وقيل 00 ( 3 .قال في شفاء الغليل 1 `
عق الباذجان معرب
(اللان) 3 مان ܕܬܕ كل عار مانع
(الأملم) دواء ٠‏ وهو ܳܨ ܚܨ ينبت في الهند معرب 11
(النج) منك ك وهو حب اذا أكل < 1 وغير عمَلهُ
1 ܨ ܐܥܘ معرب" ܐܥ وهو ܬܐ )ܒܐ ܐܝܕܒ واضاا
مسه
( | ܐ̈ܫܢܟ ) آلة 2 ܨ 007 ` }1 ܝ اي اناما د
مق ٠‏ وقال ܐ دص :1م 00 0 39
< من 00 وهذه 0 0 ` الواسطة .
ايخ ] ܡܝܓܢܝܩܐ ܐܥ ® ٠و‏ ثممل ان يكون اصل اتكلمة فارسا ` 31
الام مأعذة ع مهنيد يك كا سبى اقول مةئ لك له 001
اساوب ܗ ܐܗܨܢ أو ܚ 5 5 الارتفاع الى فوق وكان
اسم ܬ 06 !]£ ماء £ ويضعون فيه دق 20:03 3 ܢ
2 ان ܣ واحدة فواحدة من الإناء وذلك لا نهم كانوا يطمقون £ الاناء متجتونا
=== leaf 148 ===
< 3:(+ 3 3
يضعون عليه قليلا من اللح ٠‏ فبقدر ما كان يذوب الملح كان الماجنون يخاو ܬܨ تلك
الاحجار الدقيقة الى الخارج
مانيذ ) الجرية: بقيتها مأخوذة من مأرنيده اي 01
+ 0 5144 ܨܢ منش )3 10 الهّة ويوافقفة ܨ 1165
والانتكليزي 11170 ܕܐ ريق 14 اي فكر ونأ ܨ
0 )ܕܐ )381 05 7 موتر اي‎ ١
ܢ‎ 491 3
1 2 ܝ الغنى مأخوذ من معيكار اي دأ به العظمة
1 الخاتم فارسي 59 فعا وقالوا مهرَ
ܫ 0 الور ܟ واصل 1 0 حافظ |
7 0 0 6 90 49577 35 610 والعاؤقة
جان) عد الفرس مركب من 3309 331
06 (3061 ܚܚ اول الشماء 0 نقدم عند ܨ 3 0:3 0-3 بق في ܡ
وهو اليوم السادس عشر من شهر « ܝܢ * وذلك عند نزول ܐܚܨ ا >
للفرس عيدان كبيران ررك 795 56 0 7 5( 5 أن الله
580 فرش فيه 000 9 ܗ يع الأجسام 77 للارواح ܐܨ 105
6 0 الازك واكم م كانوا يترون فيه على جميع الرعايا وال بايا
فيقدمون خم الطعام ܝܢ ب قوم الى 0 11 42 7 ني ذلك اليوم ٠‏
فل كارا لنجاتهم ܦ 4 4 من ظلم ܡܓܢ 31 4:83 01 سئة : ܐ 0
اردشير بن بابك وضع ܝ هذا ܟ .0 رأسه تأجة 31 الذي كان 0750 مثل
الشمس ٠‏ وسن على خلفائه من الملوك ان يعقدوا في ذلك اليوم نفسه التاج على روس
اولادهم ويطلوا أجساءهم بدهن البان٠وكان‏ اأوابذة في المهرجان يدخاون على الماوك
كل ` حاملين 4 ج .ܗܘ ܝܐ 50:4 ܐܝܝ ܐܝܢ والعنب الابيض
1 ܫ 0 في ذلك اليوم من تلك الاثار ودهن 250
00 البان :03 عليه ماء الورد سلم حى م 00 منْ جميع الأوجاع 26
=== leaf 149 ===
د < 35
3010 رةه كامت النساء 3 1011 لعة فيها ܐܠܝ تمر يبب هر رهي
خرزة لوا ` كاون المرجان
ܢ مره
# ( مضل ) 5 5 مركب من مه اي كبير وسالي لي .مسن
1 ܨܝ § البأورة تعريب مما وهو حجر شه 5 وقيل هر ܐܐ تبه
ملو ول يوان فقيه الفرس ܠ المجوس 3:5( وججعة
ܨ
( لوم ) ببى الشبع فارسي تكلموا 4 0:27 ܨ
(ليَة) فشر بشىء من ܇ الأدرية ܣ من ܐܝ اي الخير 1:0 يبه اي
ܝ
( الميبحتج » العنب المطبوخ مركب من تمي )1١(‏ اي <> ومن إبخته اي مطبوخ
وهو عسبل العنب ١‏ كن الاطباء يغلونة مرة ثانية »= والعسل
4 فشحة مجبهة همده 18 رلم اليل قل كلمن انام 1ه
ܨܐܘ واضبطرابه عند السباق٠وقيل‏ هو من الوَدْن لان الل رون فيه «بحبط
الجيط ‏ ܢܘܛ رأبي ان الميدان ܠܚܢ الاصل وهر مركب من ,مي اي الشراب ومن
:0 وهى : الأدوات ܐܛ تاحق الاسماء ܐ¿ على 5 13 £ اول الام
5 3 5 .يشر بون فيه امن ثم اطلتوم على الفسيعة المدء اسان
واعب الخيل ٠‏ وهر مردان بالتركية والكردبة
(( ܨ » الطعام والحوان عليه الطعام ٠‏ قيل ܐܬܐܬ مشتقّة من ܘ ععنى اعطاه
دعي فاعلة ܬܶܢ مفعولة لان الماك ]ܪܬܐ للنامن اي اعطاهم اياها , «وقيل من ماد كيد
اذا تحرك ( اقرب الموارد ) انها | معربة عن ܚܬܪܘ وهو خبز المسميذ با لفارسة 1
܀ لإن صاحب البيت اذا ܐܘ ضيف ܪܟ له من خْبز ܢܒ ܐܰܢ على الموان وأطلقت
5 * بالفارسة على الموان والذي يخدم ( 55 المانيدة 7450("
)١‏ وشرب الفاريي مي 0 0 4 اي سك واامونالي 40¡ أي
1
ܝ
=== leaf 150 ===
_ 4¿ ܙ -
وا لندة 80( 3 اما فرتكل 5 ان اللاندة تعريب 1 `
(ص: ܥ )
6( بالياء 9 بهمزة ܓ 5( فيها الماء والمثقب ويقال
2 وصفها ابن السكيت والفراء وابو حاتم ٠‏ وفي التهذيب عن ابن الاعرابي : ويقال
اللمازاب 3 0 يتقديم الراء المهمة وتاخيرها ونقله الليث وجساعة ( اقرب
الوارد» :قات ان ܐܠ ܐܢ ܨ ܝܢ من ܘܬ اي بول ومن آب اي ماء ܕܝܙܝ النسمية
ظاهر (راجع ` لكل :4 )
ܣ 10 ® 099 2 من مي اق شراب بم الى"
.܀
ܗܐ
9
١‏ ابابا 6 فول الذي 'يككل به فارسيّة ميل ` = ܟ اله
معرب عن اليونافي «</نم٠‏ فالفارمي ايضاً ܨܕ ܝ عن اليونافى وملة ايضاً
ܡܝܠܐ بالارامسية .وما الم للمسافة فهو تعر يب 00 509 (© ܘܐ
بالارامية
*« (المثاء) عق جوقر الزجاج تريب الفارسي مثا وير به 4 الفرني 0081
والايطا ليالي 56 ܙ 1܀] اذى مرمئ السيةء+ة فأخرذ 9 ن الادائي ° ܠܡܐܢܐ والارائي
4 4 مالحوذ من اليوالي ܬܨ(
( ® نات له ورق سُدِيهِ بورق الكر رم البري تعر بيب 8596
باب النون
± 7
» ( الا نوب) ما بين الكعبين م الل اي ܝ النبات ما بين عقدتنه
ويستعار كن ܥܕܝ وسيب ل لر ܟܝܢ ܚ ܨܝ || ܀ ^ له . ܘ ,ܝܝ ܐܟ ܢܬ
المسداة 90 4 :3 ويطاق ايأ على ܐܳܝܰܐܺܝܢ الاناء واللولى ٠‏ والا تنب 0477
=== leaf 151 ===
ܢ ܀ © | ܝܝܚ
لغتان فيه ٠‏ والظاهر ان الافظة ارامية الاصل ذعي ܐܢܒܘܒܐ باللغة البابليَة
ܕ ܐܝܟ ܨܐܬ و > دنه حدم ܐܬܐ .ܕ % ܨܝ ܨ ܝܨ 811 )ܙ(
ومعئاها الأننوبة والمزمار ܨ ܐ من ܢܒܒ اي صرخ وتخ ٠‏ .وان ܒܝܒܐ
و ܒܘܒܝܐ اى المجرى والة: ناة 885 | ܗ ܐܐ ܨ ]711 (راجع كلمة
ندب في هذا ܐܐܝ “راجع @ فرئكل ص 7١:‏ )
ܨ عر شجرة 0 و يم عاد ܐܒ وتفاحي مكلك انع
(الأنار) فارسي محض اي 21( واصل 0 المت ومنسة الارائئ”
ܐܡܒܪܐ ܙ !ܚܐ او عشمار بالتركة والكردنة 87 ܐܕ 27 000 متنا 101
اواليو الي بومتومن؟ 9 ܬܘ
ܪ الذي يد 90 صوف تعر يس الإريده أي غير روز
ومنه ܢܒܪܢܢܢܐ بالارامسة
( التبهرج ) الدرهم ازيف الردي تعر يبب ܘ واصل ܫܐ د
( |( ;| ) 7 اسود وابيض واصلة اغلظ من الاصبع يتفرع كثيرا معرب
كدان .ܕܠܐ لغة فيه ومنة السر بالى ܐܓܕܢܐ
# ( الجر والتخر) الاصل والمسب تعريب ܐ¿(
1 وقال فلك 1 ل
عن اليوناللي »ܕ«
53( 5 تمر يت نكل وهو 3088 دقار ف) 305
اي ولده
( النخ ) بساط طولة 7 من عرضه معرب 3
( ||[ 1 0 ننس 4:0 مأخوذ .0 6 وهو ا من ܐܕ 3 ܚܬܐ ومن
0 3 صاحب
0010( 0 هراس ܬܐܘ ܇ : 10801:11 1 56200020
110001 ,12ع0116ه 111011023[211111/
.5 11116 ,011 ه11
=== leaf 152 ===
ܒ ܙ( ܘ | --
+ (الكراز) الشرف المتكير واعلبان 35 ` 72410 97 }܆
المهذار ܐܬܐ
ܣܣ معرب مرك ومنة 0 0
01200010004 واللاتيني 05 والفرة سي 15 و الايطاليالي 1121150
والاتكايزي 115 واطرمالي 11 ܥ و ككردي ܥ والارائي
ܢܪܩܝܣ ܙܝ ܢܪܩܘܣ والارمنى /7///404 0 عر 5 كس وان
دان اي وعاء الأرجس :
التأرجيل ) ܐܧ( الهددي 0 اردق 3 9775 2% م
53 0 | تتخذ © وهو ܡܠ "5 ` ® 5 < 7( 27
® ܬܐ ܀ 05 ±
( |« ) ܝ معرؤف يلعب 7 2 5 ܝܕ وضع اردسير ܢ بابك ܟ ن ماوك
الفرس ولهذا 3 اليه فقيل 1 ( حيط المحيط ) ٠‏ 0 هو وضع زرجهر
قبل لا بل اقدم منه والترد عبارة ܧ عن سبع ܐܐ وهي بالفارسية فارد وزياد وستاره
وخانه كير وطويل ودهزار ومنصو به ( البرهان القاطع ) 979 الفارسي يطلق ܐܢܒܐ على
طلاء مرك فنة:ايضا المركي اد دي الطلة؟
(التأوّرد ) لفظ فارسي هو في لغتهم بعنى < وجولان < في اللدان
( شفاء الغليل )
( التوروز والبيدُوز) اوّل يوم من السئة الشمسيّة تكن عند الفرس عند نزول
ܨ اول ܥܐ 2 ܝ بوم جديل ٠ورمًا‏ ܡ 4 بوم فرح 0039
قبل ܨ الى علي شي ء من 592 0 0( للنيروز: فقال ܓ 9 16 بوم ٠‏
دفي المهرجان قال: مهر جوناً كل 0 ٠قال‏ في البرهان ܐܟܐ ܨ ما تعريمسة:«التوروز
ومعناه اليوم الحديد يطلق على يومين من ايام السنة .يقال 1 وروز العامة £
ورور الخاضة 1 العامة هو اليوم الاول ܨ 0 : 86:3
,0 ܬ ٠‏ والداعي الى تسميته بالنوروز ان الله تعاللى فيه 6 العالم والانسان الاوّل
وفيه وجدت جر بع الكواكب في برج الحمل وفيه اخذت › وذهب قوم 201
0 ܗ العرب ممتوشلخ وهو من البيشداديان واصل. اسمه جم ) بعد
=== leaf 153 ===
هه 00 ܐܓ
أن طاف اقطار المسكونة اتتهى الى اذور 9 وأعر 43" 0.33
حل عالتفى اعلهة الشرقية منة عرش مرضع .2 لس نا به الملوكة ووضع على رأسه
تاج المرضع ܬܐܨ النفيسة وجاس على العرش امنصوب له ܶܪ | طلعث الشمس
فضر بث ܣ التابم 057 امنتلاً ذلك الوضع نورًا وضماء ٠‏ فاستبدع :3
المدظر فاستسغدوا ܛ || ܐܕܬ ا نورورًا ܥ انه يوم ܶܕ ܠܐܒ ܐܬܐ £
« شبد £ باللغة المهاوية تطلق على الشعاع أضافوها لى اسم ` كثالوا ܝܟܝܠ ٠‏
0 وروز ܐܟ فهو اليوم السادس من سهر « فروردين » الذي" ܠ ܨܢ « ܢܐܪ ¢
5 7 تسسته بنوزوذ اخاضة أن 33 0 على ضر يذ ©
استدعى اليه جيع اركان _ وخواض دادرة ساطنته د عليهم قواعءد ܓܗ - ܢ
وقوانين مستحسنة . فاستصوبوا ¥ -( ذلك 9.41 3 ويروى ايضاً
8 اعيان الفرس في الايام السنّة التى بين نوروز 3 ܣ 3 يحيبون الى
سؤل جميع الحتاجين و يطلقرن الحموسين ܣ مع ذلك يتعكفهون على !ܠ ܐܙ اث
والعشرة ܕ ومن الفارسي وروز مأخوذ السر إلى ܢܘܣܪܕܐ واضافوه الى ܐܢܠ
ذالوا مه هد » مل ان عيد الله وهو لي طقس © يان الشرقيين الأحد 0
فم الس ليم ١‏
( النرْق) اليد ( شفاء الغذيل ) ٠‏ معرب نزخ وهعناه السعد والرونق
١‏ النارَمْسْك ) ܙܘ ضغيرة مفتحة كأنها وردّة لونها الى الساض ‹1 ܠܟܕ والضترة
في ذسطها نوار لونة كذالك وطعمة نض وراتة طيية ومعناها بالفارسيّة هسك
ا زهان
( | ܕ ) اللين ܐܐܬܐ ܩܢ مريب ܝܝ هُ الكردي زم
ܨ ܟܝܢ هن اللسمون معرب نارناك واصل معناة 3 ر اللون ܀ وفتة ܘ
ܫܫ 3 0
+ ( ×« © 815 تصن ين لزه
١‏ 363 ܝ القصيد تعريب يزه والتيزق لغة فيه ومنة فعل ترك اي طعن
بالنيرك ٠‏ ومنه الاراعي. ܨ =
+ ( الشيسب) ܐܟܟ بق ن الواضح الستقيم او ما وجد 7 الطريق ܥܕ !$
```


## [2026-09-06T22:53:25.753Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"باب اللام\\|باب الميم\\|باب الكاف\" AFM_pages.txt | head\npython3 - <<'EOF'\nd=open('AFM_pages.txt',encoding='utf-8',errors='replace').read()\npg=d.split('\\f')\nfor i,p in enumerate(pg):\n    if 'باب اللام' in p or 'باب الميم' in p:\n        print('leaf',i, 'has', 'اللام' if 'باب اللام' in p else '', 'الميم' if 'باب الميم' in p else '')\nEOF",
 "description": "Find AFM lam section"
}
```


### [2026-09-06T22:53:27.382Z] TOOL RESULT

```
3344:باب الكاف
```


## [2026-09-06T22:53:30.287Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nd=open('AFM_pages.txt',encoding='utf-8',errors='replace').read()\npg=d.split('\\f')\nfor i in range(138,147):\n    t=pg[i]\n    print('=== leaf',i,'===')\n    print(t[:1400])\nEOF",
 "description": "Print AFM leaves 138-146"
}
```


### [2026-09-06T22:53:31.982Z] TOOL RESULT

```
=== leaf 138 ===
_ ܙ -
د (تكاتان ) آلة من حديد ܓ 9 3( ܓ <
وهنه ܬܝ ܥ » 350
)ܝ اياقب في انبر ,0003 54450 -
` © 50 )ܐܢ 39 ܛܘܦܐ
× 0 القطعة ܐܐܳܐܬܟܳܐܘ̈ من الأرض م :0
وقالوا فيها تكد الى غير ذلك
لاط _ 0:43047 وحهها 5 0-0 اي ورد ومن كون ܒ
لون
زاكك كا عد مدال الذي خالط حرقة قار قنو* أي سواد غير خالص ܝܢܐ بين
911 5:7 ابو عنيدة : :* فرق بسين ܐܳܚ والأشقر بالعرف والذائب ٠‏
:ܡܫ( أحمرين فهو الاشقر وان كانا 33 فهو 0 وهو تصعار 2 1
غير قياس »> ٠‏ وعن الأصمعي "انار حر اذالم يخالط 3 0 > خالط ¬ 47
݂ܕ 9 0 5 ابضا. «قات وفارسية كتيت ت ܐܢܐ وهو ܐܵܕ 5-0
ܐܫܟ التي (1:, ةزعل اليل 9801 ܛ ܕܪ نه اسودان٠‏ 07
٠ 0‏ كيت ܪܕܫܕ المختلط › وقالت ف افيه العرنت »كسك المرمن ܝ
ܕܝ ثوبةُ اي صبغة باون الكمر وهو حمرة في سواد 37 واس 0
وكاتة الى غير ذلك
ܟ اشر ) لل والتضين تعر ين كزتن وهو مر 9 ܝ ܪ
ومن ” 0 رهي اداة التفضيل ٠‏ ,ܟ والكماً ܛ 0 والكنتال راك كال
ܣ ت لغات فيه
( كير ) اسم ككل بناء فيه العقد كبناء المسور والقناطر _-
الواص والعوام > ÷“ ܥ
(الكامخ ) إدام ܨ به يقال 4 ا أري 60:37 ܕ الاراعي ° ܕܡܟܐ
ويرادفة ܐ ܨܐ ١غ‏
 '*‏ ذات اوتار تعر 0 كانه بالتركية والكردية
وااسر ܨܐܬ الدارجة
(
=== leaf 139 ===
-_ ,)| لس
ܐ ܀# 3 وب ܝ مت و
8( لكر الببذعة ܗ سرع الفرس مركبة هن كن اي ذبر ومن
ܣ اي غطاء
او 1 الوم اختلطوا 85 500 : ܢ 25111
والعمل
(ألكنك ) 7 1 عد 3 العد رد
04005 1759 38 30945 وهر كه 9 كدان
+ [ الكتدجة) فعرية كله وه لمعه كاله تر 0 و ا
الحدران والطيقان
( الكندوج) 7:02 ܨ سمه حزن من تراب او خحشب توضع فيه
)213 9[ ها١٠ومئه‏ ظنج هو مها
# ( ܥܐ ܕܙ ) الغليظ القصير مع شدة. واككُتدر ܚܕ فيه ٠و(‏ :ܝ ) اليار
الغليظ . ܕ ( ܐܥ( 0 ! الغليظ ٠‏ و( الكنديرة ) 83 والضخامة ٠و‏ (الكَنْدَرَة)
ما 85 من الأرض: كل ذلك راجع الى معنى الكلمة: الفارسة ܐܒ 500
0033[
الشجيع 0 31
( :13 ) الشجاع المسور فارسيتة كنداكر
( أمكندبن ) 979 ومن عرو 85575 1 11 .0
ܝܪ )| ± 7 0 ܨ ܐܟܐܠ أ (6001137:76)
( اككْئار) ܢܝܨ حض قال في الإرهان القاطع : « كنار اسم عر لذيذ حكثيرا
.1 العناب وهو ܠܝܡ الوحدود لي امعد يقال ]0 سدرا وبافئد ܪ ܨ لك £
جميع المفردات ܝ ان السدر شجر ويقال 4 ܕ ̈ܝ »
ܫ | ) ܣ اي صغير ومن بال اي
4
المنظر
( الكهرياء ) صمع سحرة اذا نيك 302 7»ܣ 3 ܐ زمعقى كأه الثن
=== leaf 140 ===
لاوم( -
ومعنى ¥ الماذب ٠‏ ويرادفة 6 :)10 `
القاطع : « قيل ان ܦ صمغ ܣܨ الرومي وهو في بلاد البلغار: وقيل صمغ
الدَوْم ٠‏ وقيل ضرب من الاؤلو يوجد في سواحل بجر المغرب ٠وقيل‏ صمغ شجر يشبه
شجر الفستق يشتعل بالنار مثل الكبريت ولهذا قيل له سيّد الكباريت ٠‏ وقيل يأبع
من ܐܐܟ في بلاد الروس واول مسا يضر به اللهواء يحمد مثل المرمر وهذا الحكهر باء
اقيق ويقال له بالعربّة مصباح الروم ٠‏ وقيل اله من انواع ܝ  -:‏ 50
ܟܗܪܒ̄ܐ
نكر 2 ) الذل الطغيد المخضر 6 6
٠ 1‏ 0 ير اراس لاحرؤة 4 او لآ حرظوم ل وهو معرب عن كوب ,
والثلاهر ان الكلمة من موافتات اللغات وهر حه كمط" بالارامية ( ¥+ 9 ]
ܐܟ ) ܕ ܟܘܦܐ بالسريانّة الدارجة وكرب بالتركّة والكردنة و :080 ܝ 4:80«
® ܕ ([011 باأرومسة و ¬ بالايطاليانئة و مناه بالاتكليزية و : 03
بالمرمانسة و 3 7 ® ܕ 0116 ¢ بالفرنسة و باس »ܨ بالارمنية ٠‏ والفعل
15 20000 روت 9 في كثير من 30 5( 063 493
¬ وهو حث 55 6.535 ( ± باليونانية
ܕ ¢€1100 ±7® ܕ 0211 بالرمانمة ܣ 0 ܕ 00120 ܐܠܬܝܐ
( آلكوقٍ ) تعريب ܰܘ وهو التصير
سنو كينت مس من قصب 990
3 الزارع على زرعه - والككاخ ܩܣ فيه »^ ܟܘܟܐ لعن رانحية الدارجة ܨ
بالتركيّة والكردبة
١ *‏ 5 وفي القاموس 5 ما جمعت من تراب ونحوه تعريب كود -
لعل 5
: وقال فيه الشاعر الفارسى‎ )١
ܥܐ كربي & مر ازو بردار خويشانرا يصبرده ܢܓ
3 | ܐ( )6 تيرد ܥܘ كلد كاه ܐܢܘ مسكين
=== leaf 141 ===
9:4
# ( كرارة) النحل وتكسر وكؤارتها بتشديد الواو شيء ܡܳܐ ܐܗܐ من
القضبان او الطين ضيّق الراس ٠وقيل‏ هي عسلها في الشمع وقيل ܐ( الخلايا
الاهلءة وهي ܘܨ بة عن كْوَارَه ومعناها 965 وتطلق 0 على سهد العسل
* (الكارَة) ما يحمل على الظهر من الثياب ٠‏ وفي اللسان:« والكارة عكم
الثبات قاكارة التصار سيت لاله يكور نا شتف يون راح اياي كتوق را
فوق بعض ٠»‏ قلت والاصح انْ الكلمة فارسيّة ܬܨ بها كارّه وه وكل ما يحل على
الظهر من الثياب والمماب واككلا وغير 0 مركّة من كار اي عمل شغل
ومن هاء التخصيص ٠‏ ومنها ܪ فمل” كار 4 5 77 | ܟܪܬܐ
ܐܝܟ ܨܬ
5 5:5 له عروة و بلبل تعر ب ب كاز 9( (فرتكل :078 .
` ܫܫ اي شرب بالكوز واكتّازٌ ومئةُ ܟܘܙܐ
ܨ الال م1 جسن وهي طاولة كيرة نظير الكربة ار
أثناء المحاربة: واضل ܐܫܝ 30 ارا
بالفارسسة
( المُوسَح » الاثط والناقص 7 ٠‏ قال الأزهري لا أصل له في 3 `
وقال عضهم معرب واصلة كرسق او كوسه ٠وقيل‏ هوعرلي من ܚܝܢ الرجل ايم
بشت له .4 ( خبط الحيط)٠قلت‏ ان كُمَج مشتق من أ ܚܝ والكوسج معرب
01 َه وهو ال ܝܐ تظ والذى 3 عأ نبة وعشرون ٠‏ ܕ 4 4 كوسه ܓ والسر ±
الدارجة والكردنة
( انكر كع لانن عر كا نزي
* ( كاش يكوش ) اجتَهّد مثل أكوشيدن لفظاً ومعنى
* ( ألُولان ) فارسيّتة ܠ وهو ننت البردي
002390) | 32 ® 810 جسلئيوس في معجمه العبرائي 00
الكلمة ® ܘܐ من ܠ جدى ± اي عادل (ܟܐܢܝܐ) ܠܚܟ 20300
فارسّة الاصل 0 0 أي رفيع القدر ومن وان اي رقيب < ܨ
حى
=== leaf 142 ===
‫ 1
ܢ ܐܟܟ - + 97 315 355 :انث كك بالقارشئة
ܘܚܐܘ الرفيع القدر ويطلق على الاك التهار المار وهو كنية عندهم عن ملك الاوك .
وار بعة من 46 دولتهم الثانية لُيَُوا به وهم كيكاوس وكيخسرو وكيتباد وى
هراسب ثم ; بق الغلبة على ܬܝܟ ܨ الدولة الثانية فقيل لهم ܫ
وهو جمع ‏ قي ( البيعان القاطع )
(اتكال) الة معوجة ܝ تهدم 0 ܟܒ 7 فارسّة فاذا صح
ذلك ك1 ادن 1 لشات :0600
+« ( الكلحَة ) كيل معروف لاهل العراق وهى 0 ܝܫܐ 0:00 ܦ
والفارسى ܝ ܨ ܟܝܠܐ :
لكا ) المطكى فارسيّة كنا
05
(اللازورد) 3 0
ال 1 الطرة معرب ليت
ܐ اللجام ) تعريب لكام وهو بالارامسة ܠܓܡܐ ܠܘܓܡܐ وباحدشة 1010 +
وبرادفة ܐܐܐܠ 4 (١‏ فرد ܀ \ ) ܕܝܢ 13100 ا 0 صل
< 1 ® ܐܪܝܐ من ܥ ܢ ® طلق 3 على الفك
ܨ
* (اللَج) الياعة الكثيرة ومعظم الماء تعريب 3 وهو اليش البالغ عدده
قات العك قر وتلق @) علي كل ما بلغ عدده مائة الف
([35) .27 ܥ وهو ضرب من الطيوب مر 3 ܨ العود ܕ ܐܫܡ
والمسك واللادن والكافور
=== leaf 143 ===
ܒܝ <
(اللاخشة ) الاإطربة وهي طعام كاخيوط من الدقيق . واللاخوشة ܕ )ܪܫܐ
ܬܰܝܨܳܐ رهى .7 اك
15063 21411 30 54890
)1:00 واللكن لغة فيه تعريب لَكَن ومنة السر 0 ܝܐ 6(
والكردي 1:3 ¢ 2
+ ( اللقّازق ) ويقال ثقائق اسم لأحد الأمعاء وبه سي معى | ام ابعشو و ܐܠܨ .
دس ععاوم 1 م مرب يكبا الغليل ) .قات وهو معرب ܐ نه وهو العصب
بد ( الك ) صبغ 7 ` ܟܝܬ به جاود المعزى تعر يب لك
1 ܫ الرأة القصيرة الذميمة وقيل الطوية الحزية وقيل مقاوب الرهلة
وهي الت لا 5 ܇ ` ني مشا تقلا ( اقرف الوارة؟؟ اتلتهنا وده
عن ܐܚ̈ܐ ܬ ومعناها المرأة الحممّاء
± (اللادّة ) ثوب حرير 598 لاد
(اللوياء » 90547 7( 0108 10595( 109433803
فرنكل ( ص : £ \ ) | ܝܐ مأخوذة من الارامي لله صم" . ويقريا !"ܨ +0084
اي ܐܝܢ
* ( الأور) أبن متوسط في الصلابة بين ابن واللبأ واهل الشام ستول
ܳܐ تعر يب 0 ومنه 1 26 ܠܘܪܐ ܐܝܟ ܨܐ الدارجة 3
ܟ %
(اللُوزِسم ) من اللاواء سمه القطائف ܘ بدهن 3 501
* 5 تعريب لوله 37 2 ± الدارجة ولرله بالارئة
ܕ
¦ 35 35 فيقال 5 وهذا 95 )¬ 3 وهو
05 3 بالتركة 3 <( يانيّة الدارجة
=== leaf 144 ===
د ܨ¿ ܙ عا
ܐܝ اليم
(الألي) آلة من حديد يطين بها تعريب ماله ْ ܝ ܐ فيه
¥= #1 تَميضين مانا ܙܐ فيه عاك اك اكاب 110
* ( المرونة ) ܡܚ ܡ من منت القوم اذا احتملت مُوُوتتهم ( اقرب
ܝ 90 01:3 ± 73000 0003 $ ان المرونة
معر بة عن 2 < ܨ أمدث ٠‏ ܨܐ ܡܐܢܐ بالارامسة
ْ المتراس) ما تست به من حائط ووه من العدو وخشة توضع خلف الباب‎ ١
3 قال ,”ܝܨ 630 تعريب اليونالي 0 - وعلى ظني‎
الفارسي مترس واصل معناه :لا تيكف . وسبس التسمية ظاهر‎
* (المثك) الاتريم ربح فارسّة -
(الج) حب امش 2 ماش ونه الارامي "فح داا 3
0 )080 لغة في الماش او معرب الارائي | تتح" . ومنة ماش بالتركيّة
7 3 00 2
( الأجشون) السفيثة ܐܝ مصبغة تعريب ܘܬܘܨ واصل ا
(الكّدةِ) المعونة تعريب ܢܫܝ
( ܐܠ ܥܳܨܨ ) لس الفسّاق وبيت الريبة 4 ; ما خور وهو عرب من مي
3 اي شرب الخمر
7 01 00 مر قة هوه × 10 الانعري : المخرقفة مأخوذة من
مخاريق الصبيان من ارق المفتولة » .وقال الوهري : اما المخرقة = ` مولّدة ٠.‏ وقال
غيده المخرقة اختلاق التكذب وهي كلمة ܙܝ على الخراق كاك.سكن على المسكين
و تمل ان يكون تركيبها من حروف 6 وهو خلق الكذب 00 ܐܬܘܛܝܠܬܐ الج
23 ® 1 على زيادة العنى ( حيط المحيط ) ٠‏ قلت والصحر بح ان المخرقة
معر بة عن ماخ ره ومعناها الطريقة الكاذية ومنها مشتق فعل محرق
=== leaf 145 ===
ܓ 1 ܐܐܠ
( ܕܙ يون ) سجر ورقة ܐ الزيتون وزهره الى !ܐܩ له ثر كالكير تعريب
2س © ܣܦ
مازر بون
83 اكرت) . 5( بلا ننات وقتل الارض لا مجن 355 ` مرعاها‎ (١+
ܨܝ‎ 3
> ماخوذة عن مرده ܕܘܫܐܐܬܐ‎
* ( !]ܨ ܢ ܣܣ رس ج فقيل ܝܣܝܣ ܤܣ
قات فان كان ܥܠ المرداسنج فهو ܨ عن ܗ ع ܕܬܕ | ܝ امرداسنج ٠‏ وان كان
ون و اموه رج ار ܣ اطبا رن
الفارسى عروه تصحيف العرلي الأروح
15 صغار ,+ شيل كيار الدر ܡ وقبل 2 جان 1 , 0 :
وقال 3990 لا ܨ تانق هو ام م داعي ܨ تقدير زيادة < ܝ 3
5 58 الاصل ٠‏ قلت 0 1 قيل هو مر ‫ من مر وهي من ادوات
التريين ومن جان ومعثاها الروح ٠‏ وهده لكايه موحودة 0 اللغفات فى
مرجان ܙܡ 40 والكر د و تش لحدداة ܐܐ بالارامية 0 أو 03
15 .2 ( 5 : ` 1 ܕܢ 95:5 00 5 26 ܕ 1113101101116
(ننات) بالفرنسة ٠‏ ومرواريد بالنارسة و ܡܪܓܠܝܬ و ܡܪܓܠܝܬܐ ܨ 1
باللعة ;+ والم ابلمة 5 ܐܠܘ ٠‏ ܢܦܐ 9 اصلها فارسي ܨ 87
اله ول. ܚܝ .1 وهو ܥܐ من 00000 5 15 ܀ وعنلدي 0 اصل الكلمة
ܨ ܢܨ ܐ ܡܝ فعل © < 5 35 289 وا سم الفاعل لودل
دح حنسط »ع فخدفت الماء ونقات ܐ الى > وحركة الراء الى اليم فصارت
3 1 7 عن 9 صبغة }1 9
المحرق
( الرْرَئحوسُ ) من الرياحين دقيق الورق بزهر ابض عطري تعريب عرزن كرش
=== leaf 146 ===
ܚܝܚ @ ܛ¿ | ܝܚ
ܕܪ | آذان الفار. وقال فى البرهان || 3 0 غريثة حق ܝ ܐܢܐ :31
5 3 ابن ܩܙ ; 1 ( 1:10 عرز و 0 وهو فاسي 3 ܬ
بالعر بَة السمسق والعبقر فحق القئا ». والسمسق تعر ܢ اليونالي « ܘܘ
3070 الرماح وهو شجر :> 7 ول ثر 0 0
حجم التوت © كن داغلة نواة مستطية تعريب مران 5 له سجر الرماح لان
كات 09 7 والسهام وهذا الشجر كثير الوجود في قرى 33 في قضاء
109 ديسو ¦[ وت زعم 4 ܨ[ ܡ̄ܘܪܢܝܬܐ وهو نوع من من الرماح ܢ اصل
3 + ; 1
)04( 0 036 ܡ ومن بان اي حافظ 95 وبال
)9 01 الَأ ومرزبالي. ازا
( ܐܠܝ ) دار المرضى تصحيف بوارستان وهو عركب من يار اي مريض
ومن ܚ اي حل المريض ٠و‏ يقال 4 ܢ ܠ خستهخانه
(المرك) المأ برن مأختوذ عن رك اي اموت
د (المزو) ` بيض دقاق برَاقة تقدح منها النار. 71 ايضاً اسم جا
لانراع. الرياحين فارسيتة عزو وقيل هو ضرب من الرياحين يقال له بالعر يّة ران
الشيوخ ٠‏ وقيل اسم جنس للميع انواع الرياحين ٠‏ و يطآق ايضاً على حجارة القَسدَاح
١‏ ܐܬܐ القاطع ٠)‏ وهوؤ 112211111 بالفرلسمة
( 311 ܨ ) الف تعريب مُوده ٠‏ ولوق واكوقآن ܗ ٠‏ وهف ة ܡܘܩܐ
0
* ( ܐܬܪ ܨ) باتكسر ܕܝ اللوز ܐܨ معزب اك
* ( ܐܬ ) ܢܝܠ الشعير والمنطة ܕ[ ܐܝܢܝ تغريب ܨ
(مز 4 3 5 ` فاه مص < و سوم
41 دض بالاراممّة و ديشن اف )> بالمونامة و 5110 بالروم.ة و 1106
10 ` © 5 © 3 3 داغؤننهه 7 ¥ (3§
ܧܥ وم اندن بالكردة
ܟ ܙ
```


## [2026-09-06T22:53:46.637Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nd=open('AFM_pages.txt',encoding='utf-8',errors='replace').read()\npg=d.split('\\f')\nfor i in (142,143):\n    print('=== leaf',i,'full ==='); print(pg[i])\nEOF",
 "description": "Full AFM leaves 142-143"
}
```


### [2026-09-06T22:53:48.302Z] TOOL RESULT

```
=== leaf 142 full ===
‫ 1
ܢ ܐܟܟ - + 97 315 355 :انث كك بالقارشئة
ܘܚܐܘ الرفيع القدر ويطلق على الاك التهار المار وهو كنية عندهم عن ملك الاوك .
وار بعة من 46 دولتهم الثانية لُيَُوا به وهم كيكاوس وكيخسرو وكيتباد وى
هراسب ثم ; بق الغلبة على ܬܝܟ ܨ الدولة الثانية فقيل لهم ܫ
وهو جمع ‏ قي ( البيعان القاطع )
(اتكال) الة معوجة ܝ تهدم 0 ܟܒ 7 فارسّة فاذا صح
ذلك ك1 ادن 1 لشات :0600
+« ( الكلحَة ) كيل معروف لاهل العراق وهى 0 ܝܫܐ 0:00 ܦ
والفارسى ܝ ܨ ܟܝܠܐ :
لكا ) المطكى فارسيّة كنا
05
(اللازورد) 3 0
ال 1 الطرة معرب ليت
ܐ اللجام ) تعريب لكام وهو بالارامسة ܠܓܡܐ ܠܘܓܡܐ وباحدشة 1010 +
وبرادفة ܐܐܐܠ 4 (١‏ فرد ܀ \ ) ܕܝܢ 13100 ا 0 صل
< 1 ® ܐܪܝܐ من ܥ ܢ ® طلق 3 على الفك
ܨ
* (اللَج) الياعة الكثيرة ومعظم الماء تعريب 3 وهو اليش البالغ عدده
قات العك قر وتلق @) علي كل ما بلغ عدده مائة الف
([35) .27 ܥ وهو ضرب من الطيوب مر 3 ܨ العود ܕ ܐܫܡ
والمسك واللادن والكافور
=== leaf 143 full ===
ܒܝ <
(اللاخشة ) الاإطربة وهي طعام كاخيوط من الدقيق . واللاخوشة ܕ )ܪܫܐ
ܬܰܝܨܳܐ رهى .7 اك
15063 21411 30 54890
)1:00 واللكن لغة فيه تعريب لَكَن ومنة السر 0 ܝܐ 6(
والكردي 1:3 ¢ 2
+ ( اللقّازق ) ويقال ثقائق اسم لأحد الأمعاء وبه سي معى | ام ابعشو و ܐܠܨ .
دس ععاوم 1 م مرب يكبا الغليل ) .قات وهو معرب ܐ نه وهو العصب
بد ( الك ) صبغ 7 ` ܟܝܬ به جاود المعزى تعر يب لك
1 ܫ الرأة القصيرة الذميمة وقيل الطوية الحزية وقيل مقاوب الرهلة
وهي الت لا 5 ܇ ` ني مشا تقلا ( اقرف الوارة؟؟ اتلتهنا وده
عن ܐܚ̈ܐ ܬ ومعناها المرأة الحممّاء
± (اللادّة ) ثوب حرير 598 لاد
(اللوياء » 90547 7( 0108 10595( 109433803
فرنكل ( ص : £ \ ) | ܝܐ مأخوذة من الارامي لله صم" . ويقريا !"ܨ +0084
اي ܐܝܢ
* ( الأور) أبن متوسط في الصلابة بين ابن واللبأ واهل الشام ستول
ܳܐ تعر يب 0 ومنه 1 26 ܠܘܪܐ ܐܝܟ ܨܐ الدارجة 3
ܟ %
(اللُوزِسم ) من اللاواء سمه القطائف ܘ بدهن 3 501
* 5 تعريب لوله 37 2 ± الدارجة ولرله بالارئة
ܕ
¦ 35 35 فيقال 5 وهذا 95 )¬ 3 وهو
05 3 بالتركة 3 <( يانيّة الدارجة
```


## [2026-09-06T22:53:58.106Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; ls data/verification/sources/refs/ocr/AFM | head -30; python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'));print(json.dumps(d['AFM'].get('scans'),ensure_ascii=False,indent=1))\"",
 "description": "Check AFM scans config"
}
```


### [2026-09-06T22:53:59.538Z] TOOL RESULT

```
0120.png
0120.vision.txt
0123.png
0123.vision.txt
0141_try143.png
39.vision.txt
null
```


## [2026-09-06T22:54:03.162Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; ls -la | grep -i afm; ls incoming/ 2>/dev/null; ls incoming/AFM 2>/dev/null",
 "description": "Look for AFM pdf"
}
```


### [2026-09-06T22:54:03.211Z] TOOL RESULT

```
Exit code 2
-rw-rw-r--  1 sfmqrb sfmqrb   383664 Sep  4 13:59 AFM_alt.txt
-rw-rw-r--  1 sfmqrb sfmqrb   342401 Sep  4 14:06 AFM_pages.txt
-rw-rw-r--  1 sfmqrb sfmqrb 14780832 Sep  4 14:01 AFM.pdf
-rw-rw-r--  1 sfmqrb sfmqrb   354548 Sep  4 14:06 AFM.txt
AHD
ARY
BLY
BQT
CEL
FFD
IRN
ISS
KGW
MAG
MFL
MON
OEW
PLA
PRT
_tessdata
TTS
TYL
VIE
WLD
ZAW
فرهنگ ریشه های زبان فارسی (2).pdf
```


## [2026-09-06T22:54:08.743Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"لعل\\|اللعل\" AFM_alt.txt | head -20\necho \"---- alt around lam\"\ngrep -n \"اللازورد\\|اللجام\" AFM_alt.txt | head",
 "description": "Grep AFM_alt"
}
```


### [2026-09-06T22:54:08.830Z] TOOL RESULT

```
166:الصماء لاله سه حوض ( سفاء ء العلل ) 
196:( الإ درون » العلف والارى والوطن وهو إما معرب اندر ومعناه الداخل وفي او 
682:# (الرسترك) فر بسك ري ءولعل معنا کی الفارتی ستو او 
885:# (النك والكا) فر بات کاطرجیر. لعلَهُ ماخوذ من بك وهو نات م 
913:3 ااا اشطان والقصير والعلام الغاط للب تعر ات ااجة 5 اه 
987:(النْد) العلم الكبير واليلة ومن الاش عشرة آلاف ومن الكتاب الفصل او 
1054:عدي ال او عن تبره وهو چعنی ارج . قال ف شفاء ء العلل :0 برج معرب نهر ه 
1411:3¥ ( الأب ) ا ال لعل مل ا لھا ا وکل - جاف غاہظ تعر د اب 4 a‏ 
1412:الاي العلرظ 
1614:د ( اللذاء ) ey‏ العلطة ک6 الى ععنا ها . ومڌما n‏ ات 
1673:وع من اللعل > 
2089:2 اصار E‏ ره عند وجوده ف العلاف شه قرن a‏ با مرن 
2281:والعلوان 
2739:سلہهة بارجل العلکوت وی راسه قران 9 وران اران حت نره ان ان الفارسي 
3183:معنا ھا O‏ د لع فر ( سماء العلل ) ويرادفها لواف AN SPOS‏ ° 
3200:(الرهزهة) گعى اأتحسان 0 ن قول ان رھی زھی اء العلل ) 
3379:CD‏ عة اللصدان قل 8 عن e‏ اي ثلاثة ابواب (تماء العلل). 
3764:# (السَنْدَرى) الرئ والعلويل والشديد والأسد (٠‏ والسَنْدَر) الري التشيّع . 
3765:(والسندأو والسندآوة ) اللفرف واطرى القدم ٠١‏ والنداب ) صاب شدید لعل کل 
3970:اسیا ا کار ا (شاء العلل ) : فقيل 0 ردنك ای تا 
---- alt around lam
3344:ا ما صنع من الذهب والفضّة من السرج واللجام والركاب ١او‏ عن استون ومعناه 
5592:(اللازورد) معدن مشهور تعر یب لاژورد
```


## [2026-09-06T22:54:11.124Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npdftoppm -f 143 -l 143 -r 200 -png -singlefile AFM.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/afm143 && echo ok",
 "description": "Render AFM leaf 143"
}
```


### [2026-09-06T22:54:17.226Z] TOOL RESULT

```
ok
```


## [2026-09-06T22:54:19.760Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '5580,5660p' AFM_alt.txt",
 "description": "AFM_alt lam section"
}
```


### [2026-09-06T22:54:19.808Z] TOOL RESULT

```
ذلك د 1 من ع کالىدن ONE‏ وانیزامه 

٭ (الكىلجة ) كمل معروف لاهل العراف رهی 3 وسعة امان ا تعر یب کله 

والفارسي مأخوذ من الارايَ حلا 

( لكا ) الصملکی فارستۂ كا 


!اب الام 


(اللازورد) معدن مشهور تعر یب لاژورد 
( ا اة مرب لت 
( اللجَام ) تعریب لام وهو بالارامیة 8 لېد وبالشة صژاعء! 
ويرادفه السوناف ۸۷6 ( فرد ٠‏ .وعندى ان اللفظة N‏ ا صل 
وان الفارسة اخذتها من الارامة 1 د بالارامىة بطلق ايضاً على الفك 
الاعلی 
+ (الأج ) الراعة الكثيرة ومعظم الماء تعريب أك وهو اليش البالغ علده ددن 
اتتا ق ضا علي کل ما ETN‏ 
+ ( اللحْلَحَة ) فارساته 1 وهو ضرت ۰ه ر م رک من العود والعنار 
والسك واللادن والكافرر 


ت ۲۳ = 

( اللاخشة) الإ طر به رهي طعام كالخوط من الدقق ‏ واللا خوشة واللاخشة 
لعتان وها رهی عر اس اا 

للل و رج وري لال اتوت الل 

ا واللكن لغة فيه تعريب لكن ومنة السر باذ حص .والترك لن 
والکر دي لحن ويرادفة البوناف XA»‏ 

٭ (اللعَا نى ) وقال انق اسم لحد الأمعاء ۽ و س یفن القع للحشو القلى . 

گعاوم عر ری ا اللطیل ) مات ت لكا نه وهو العصلت 

٭ ( الك ) صغ ا يدغ به جاود المعری ریب 0 

4 ( اللهبرة) امرأة القصيرة الذمسمة وقبل الطوبلة الهربلة وقرل مقاوب ار هبل 
وهر الى تفهم جلبا تما او التق ثي مشا قيا ( اقرب الموارد ) اظنها معر بة 
E‏ هله ومعناها رأة المةاء الاه 

+ ( اللادة) ٹوں حر ہر ار فارستة لاد 

(اللوريا- )وات لوب تاا الاسع ا 1 
فرتکل ( ص: (٠٤١‏ انا مأخوذة من الارامى له دم . وبقرہا البوتان مه٠‏ 
ا 

* (الأور) أن متوسط في الصلابة بين البن واللا واهل الشام يستونة 
ر دعر رت ورا ممه بال زکة ولەد منت الدارجة ولور 
بالکرد به 

(الأوزريتج ) من الاواء شبه القطانف يردم بدهن الاوز تعر يب وريه 

٭ (اللولیا ریب لوک پک ب کیہ بے انا رار اا کے 
والکرد به 

(الآنمُون) وقد سقط نوت فيقال اليو وهذا أصح لان فارسة لبو وهر 
»عروف ٠‏ ومنة َيون بال ركة والكرد ة والسر يانة الدارجة 


س04 0 یو 


۳ = 


باب کے 

(الا) ال من حدید بطین ہا تعر يب ماله ٠‏ ولاق لغة فيه 

تصحف اناف ٠‏ وقالوا فه مان ای اصاب مما 

3 ( المونة ) اقوت قل فمو 0 ما نت القوم ااا ک0 ا موونتهم ( اقرب 
ازارد ن ن os‏ من الموونة لا مو وة من مان ءواظر ان المڑونة 
معر بة عن e‏ رازم البيت. ومنها دت د بالارامة 

د اراس )ما تا به من حاط ووه من العدو وخشة توضع خلف الباب. 
قال فرنکل Ns‏ تعريب اليوناني Dunes‏ على ظنی اله مأخوذ من
```


## [2026-09-06T22:54:31.996Z] TOOL CALL #30: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/afm143.png"
}
```


### [2026-09-06T22:54:32.693Z] TOOL RESULT

```

```


## [2026-09-06T22:54:32.689Z] INPUT

[Image: original 1942x3267, displayed at 1189x2000. Multiply coordinates by 1.63 to map to original image.]


## [2026-09-06T22:54:40.805Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npdftoppm -f 144 -l 144 -r 200 -png -singlefile AFM.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/afm144 && echo ok",
 "description": "Render AFM printed p.142"
}
```


### [2026-09-06T22:54:47.310Z] TOOL RESULT

```
ok
```


## [2026-09-06T22:54:49.878Z] TOOL CALL #32: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/afm144.png"
}
```


### [2026-09-06T22:54:50.456Z] TOOL RESULT

```

```


## [2026-09-06T22:54:50.455Z] INPUT

[Image: original 1942x3267, displayed at 1189x2000. Multiply coordinates by 1.63 to map to original image.]


## [2026-09-06T22:55:19.000Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nmkdir -p data/verification/sources/refs/ocr/AFM\ncp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/afm144.png data/verification/sources/refs/ocr/AFM/0142.png\ncp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/afm143.png data/verification/sources/refs/ocr/AFM/0141.png\ncat > data/verification/sources/refs/ocr/AFM/0142.vision.txt <<'EOF'\nAddi Shir, al-Alfāẓ al-fārisiyya al-muʿarraba, printed page ١٤٢ (= AFM.pdf pdf-page 144; leaf 143 0-based in AFM_pages.txt).\nRead from the page image (the OCR text files drop this line entirely).\n\nHeadwords on the page, in order:\n( اللاخِشَة ) الإطرِيَة وهي طعام كالخيوط من الدقيق . واللاخوشة واللاخِشتَة لغتان فيها وهي تعريب لَخْشَك\n٭ ( اللَعْل ) حجر كريم تعريب لال واصل معناه الأحمر\n( اللَقَن ) واللَكَن لغة فيه تعريب لَكَن ومنه السرياني ܠܩܢܐ . والتركي لَكَن والكردي لَكَن ويرادفه اليوناني λακάνη\n٭ ( اللَقَانِق ) ويقال نقانق اسم لأحد الأمعاء وبه سُمّي معى الغنم المحشوّ المقليّ . ليس بمعلوم أعربيّ ام معرّب ( شفاء الغليل ) . قلتُ وهو معرّب لَكَّانه وهو العصيب\n٭ ( اللَكُّ ) صبغ أحمر يُصبَغ به جلود المعزى تعريب لَكْ\n٭ ( اللَهْبَرَة ) المرأة القصيرة الذميمة ... أظنّها معرّبة عن لَهْبَلَه ومعناها المرأة الحمقاء الجاهلة\n٭ ( اللاذَة ) ثوب حرير أحمر فارسيّته لاد\n( اللُوبِياء ) تعريب لُوبِيَه ... وقال فرنكل ( ص: ١٤٥ ) انّها مأخوذة من الارامي ...\n٭ ( اللُور ) لَبَن متوسط في الصلابة بين الجبن واللبأ ... تعريب لُورا\n( اللَوْزِينَج ) من الحلواء شبه القطائف يُؤدَم بدهن اللوز تعريب لُوزِينه\n٭ ( اللَوْلَب ) تعريب لُولَه ...\n( اللَيْمُون ) ... فارسيّته لَيْمُو ...\n\nKey line for the verification: ٭ ( اللَعْل ) حجر كريم تعريب لال واصل معناه الأحمر\n= \"al-laʿl: a precious stone, Arabicized from (Persian) lāl, the original meaning of which is 'red'.\"\nEOF\necho saved",
 "description": "Save AFM p.142 vision transcription"
}
```


### [2026-09-06T22:55:19.079Z] TOOL RESULT

```
saved
```


## [2026-09-06T22:55:24.262Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nd=open('incoming/PLA/PLA_pages.txt',encoding='utf-8',errors='replace').read()\npg=d.split('\\f')\nprint('leaves',len(pg))\n# printed = leaf(1-based) - 15 -> printed 241 -> leaf 256 (1-based) -> index 255\nfor i in (254,255,256):\n    print('=== index',i,'(printed ~',i+1-15,') ===')\n    print(pg[i][:2000])\nEOF",
 "description": "Asbaghi PLA p.241"
}
```


### [2026-09-06T22:55:26.081Z] TOOL RESULT

```
leaves 302
=== index 254 (printed ~ 240 ) ===
lädan                                                                          240                                                                 ladg


©>V - 1ädan:                   "Ladanumt                     pers. >                griech >           lat.
      \

a)         -       läranf:          ägypt.           Ar.     lärang           = ar.        näranf         a. v.      2,


a)             -    läzward:              "Lapislazuli"                        pers.           >.)        lazward         3,
          lazulith:                "Blauspat"              (pers.            ladschuward)              4
          Lapislazuli:                   Lasurstein,                   blauer        Halbedelstein             pers.             >      ar.       > lat.
          lasieren:                mit     Lasur          versehen                   pers.      —>lat.         roman.            us
          Azur:          "das       Himmelsblau,                  Himmelsbläue"                        pers.         Dar.       >frz.        u.
          Azurlejos:                "bunte            (bes.       blaue)            in    Spanien         hergestellte
          Wandfliessen"<                             pers.        >ar.         >».
          Azuri:          Bez.          für     italien.               Sportmannschaften,                     eigentlich          "die       Blauen"
          (nach          der       Farbe        der       Sportbekleidung)                           pers.        > ar. >             it.
          Lasurit:             "blaues              Mineral,            das    den        Lasurstein           od.    Lapislazuli             bildet"
          <T pers.> ar.> lat.                                          >
           %

G,»,Y              - lazwardi:                 "lasurblau",



      Br
     -.
aIy-               lakiyya:             "Lack,         Flüssigkeit,                  die       an   der    Luft      bei       dünnem       Au
=== index 255 (printed ~ 241 ) ===
118m                                                                              2eal                                                      lukäna


rle’- ligam
      11%3m:               "Zügel            des
                                              n        Pferdes" as
                                                                 aus                 pers,        FI legam
                                                                                                     legäm,            vielleicht           aus     al-
                                                                                                                                                    al
       gäm mp.                  segäm             “, aram. OR                      ‚ mand.        lugma 3, syr.              a&-

9 -      ußum: Pl. v. pls, Ligam a. v.

 .                                                                                                2
aa) -     ugna:            "Geschlechtsorgan"                               aus     pers.      „N     legan,         mand.    lugiana

       ob)                     *, syr.'ay 5,

a>l5) - 1ahlaha:                  "aromat.              Kugel"              pers.        6,

          c                                             7               =
JJ-     la’l:        "Rubin"             pers.               s.        läla.
       lala:        "Tulpe"             pers.,          im    Ar.           heißt        die   Tulpe          Pa SUPER       süsan-al-mu°           amam
       "eine        Turban             tragende             Lilie"           s.     süsan.
       Tulpe        ist        wiederum            eine        Übersetzung                  für     ar.       süsan-al-muaman           ,     die       aus
       pers.        tülbant             "Turban!             u, dorband                  od.   dilband          Bentstanden        ist «
       Tulipan:            "Tulpe" u                   pers.           >     tk. 
=== index 256 (printed ~ 242 ) ===
lakan                                                                                  242                                                 laimün



5)    - lakan                   =       lagan          a. v.        ı     syr.        is          hebr.      138°.


us)            -       luhräsb:                   "Eigenname"                     mp.                 >   lohrasp,    mand.     luhrasp     3,


Gr sl) - lawäwin:                                 Pl.        v. Ql,J liwan q. v.

sL )- lübä = lübiyä "Bohne".

 L.)-                  lübiyä:               "Bohne"              aus   pers.          l., lubiyä           a


A,J-               Jubiya:                   nom.        un.       v.   lubiyä_q.                v.


es                 -        außzina$                    = lauzinaf             q. v.         5

H     -    lauz:                "Mandel"                 ist       selbst        ein    Fremdwort            6, möglicherweise            al-Bauz
                       v
          Se           gauz.



>              -       lauzinag:                     "Mandelkonfekt,                   Marzipan"            < mp.      )r$Pp    lauzenag     7 Ss.
          laußzinaß.

 w-                                                           _

2.)        -       lauziyya                     = lauzinaß              q. v.


&=-            lilaß = nilag a. v. <                                       pers. Sus 1ilak                  "Flieder"     — engl.         lilac,
          afrz.             lilac,                nfrz.           lilas     8,

     _                 -            _

sl) - lilaki:                                "blaßviolett,                  fliederfarben",                  dtsch.     lila
                                                                                                                          skr. >pers>>
           ar.             > sp.                2,


©,         - laimün,                         limün:            "Zitrone"
```


## [2026-09-06T22:55:38.703Z] TOOL CALL #35: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-06T22:55:38.712Z] TOOL RESULT

```


```


## [2026-09-06T22:55:43.184Z] TOOL CALL #36: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%84%D8%A7%D9%84%D9%87",
 "prompt": "Give the full Persian etymology section for لاله (lāla) 'tulip' — any proposed origin, Middle Persian form, relation to لعل/لال 'red', Hasandust or other citations. Also any Arabic/Ottoman Turkish sections."
}
```


## [2026-09-06T22:55:44.396Z] TOOL CALL #37: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%84%D8%B9%D9%84",
 "prompt": "Give the etymology sections for لعل in Persian and Arabic — origin, meaning 'ruby', whether it is said to be from Persian لال 'red', and any Sanskrit connection."
}
```


### [2026-09-06T22:55:49.939Z] TOOL RESULT

```
# Persian Etymology for لاله (lāla) "Tulip"

## Etymology Section Summary

The Persian etymology provided is incomplete. According to the Wiktionary entry, the origin is "Likely from _لال_ (lâl, literally 'red')." The article explicitly notes: "This etymology is missing or incomplete. Please add to it, or discuss it at the Etymology scriptorium."

The entry suggests comparative forms: Persian _الاله_ (alâle, "Anemone") and Persian _آلاله_ (âlâle, "Ranunculus").

## Limitations

The document contains **no citations from Hasandust or other scholarly sources** regarding the etymology. There are no Middle Persian forms provided, and no detailed linguistic analysis of the relationship between لاله and لال (red).

## Arabic & Ottoman Turkish Sections

- **Arabic**: One descendant is listed: _لَعْلَع_ (laʕlaʕ)
- **Ottoman Turkish**: Detailed noun declensions exist for two meanings—(1) tulip and (2) a heavy iron neck ring for convicts—but no separate etymology section is provided for the Ottoman Turkish entry beyond borrowing from Classical Persian.
```


### [2026-09-06T22:55:51.296Z] TOOL RESULT

```
# Etymology of لعل (la'l) - Ruby

## Arabic Etymology

The Arabic لعل (laʕl) meaning "red gemstone" is "borrowed from Persian لال (lâl)." The word refers to various red stones including "cornelian, garnet, spinel, tourmaline."

## Persian Etymology

Persian لعل (la'l) has a circular etymological path: it was "borrowed from Arabic لَعْل (laʕl), from Persian لال (lâl)." This indicates the term originated in Persian as لال, entered Arabic, then returned to Persian usage.

## Meaning

In both languages, لعل denotes red gemstones. Persian usage extends poetically to "the beautiful lips of the beloved" and "red wine" through figurative language.

## Sanskrit Connection

The provided Wiktionary content contains **no mention of Sanskrit origins** for either the Arabic or Persian forms of this word. The etymology traces only to Persian لال as the ultimate source.
```


## [2026-09-06T22:55:59.576Z] TOOL CALL #38: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%84%D8%A7%D9%84",
 "prompt": "List all Persian etymologies and senses for لال (lâl) — especially (a) 'mute/dumb' and (b) 'red'. Give the origin proposed for the 'red' sense, descendants (Hindi/Urdu लाल lāl, Arabic لعل), and any Middle Persian forms."
}
```


## [2026-09-06T22:56:00.826Z] TOOL CALL #39: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%E0%A4%B2%E0%A4%BE%E0%A4%B2",
 "prompt": "Give the Hindi etymology of लाल (lāl) 'red' — is it borrowed from Classical Persian لال, or inherited from Sanskrit? Quote the etymology text."
}
```


### [2026-09-06T22:56:06.096Z] TOOL RESULT

```
# Persian Etymology and Senses of لال (lâl)

## Senses

**Sense 1 (Mute/Dumb):** The adjective means "mute" or "speechless," with etymology marked as missing or incomplete.

**Sense 2 (Red):** The adjective signifies "red," with synonyms including سرخ (sorx) and قرمزی (qermezi). The noun refers to "a red gemstone, cornelian, garnet, spinel, tourmaline."

## Origin of 'Red' Sense

The source states the etymology is "Of unknown origin" and poses a speculative question: "Is the gemstone sense or the color sense the original? Could this be an extremely reduced and colloquially distorted derivative of Proto-Indo-European *h₁rewdʰ- ('red')?"

## Key Descendants

- **Hindi/Urdu:** लाल/لال (lāl, "red")
- **Arabic:** لَعْل (laʕl, "gemstone")
- **Bengali, Gujarati, Odia, Punjabi, Sylheti:** Various forms for "red"

## Middle Persian Forms

The document contains no specific Middle Persian attestations for لال, though it references Classical Persian and multiple modern Persian dialects (Dari, Iranian, Tajik).
```


### [2026-09-06T22:56:06.152Z] TOOL RESULT

```
# Hindi Etymology of लाल (lāl) 'red'

According to the Wiktionary entry, लाल has **two distinct etymologies** in Hindi:

**Etymology 1 (Color meaning):** This sense is borrowed from Classical Persian. The text states: "Borrowed from Classical Persian لَال (lāl)."

**Etymology 2 (Endearment/Dear one):** This sense is inherited from Sanskrit. The entry explains: "Inherited from Sanskrit लाल्य (lālya, 'to be caressed'). Cognate with Old Awadhi लाल (lāla, 'woman')."

So the "red" meaning comes from Persian, while the "dear/beloved" sense derives from Sanskrit roots, making लाल a word with dual etymological origins depending on its specific meaning.
```


## [2026-09-06T22:56:16.715Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HJB loll ===\"; grep -n -i \"loll shrub\\|loll shraub\\|LOLL SHRAUB\\|Loll-shrub\" HJB.txt | head\necho \"=== AID loll ===\"; grep -n -i \"loll\" AID.txt | head\necho \"=== SKT loll ===\"; grep -n -i \"loll shr\" SKT.txt | head\necho \"=== FSD vol lal ===\"; ls FSD*; ",
 "description": "Grep Hobson-Jobson etc for loll shrub"
}
```


### [2026-09-06T22:56:16.800Z] TOOL RESULT

```
=== HJB loll ===
=== AID loll ===
=== SKT loll ===
=== FSD vol lal ===
FSD_vol1.txt
FSD_vol2.txt
FSD_vol3.txt
FSD_vol4.txt
```


## [2026-09-06T22:56:19.149Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD ranj ===\"; grep -n \"ranz\\|ranj\\|rnc\" PHD.txt PHD_mackenzie.txt | head -20\necho \"=== NYB ranj ===\"; grep -n \"ranz\\|ranj\" NYB_vol2_glossary.txt | head -20\necho \"=== HRN ranj ===\"; grep -n \"randsch\\|ranj\\|Kummer\" HRN.txt | head -20\necho \"=== CHEUNG ranj ===\"; grep -n \"ranǰ\\|ranj\\|RANJ\" CHEUNG.txt | head -20",
 "description": "Grep Iranian dictionaries for ranj"
}
```


### [2026-09-06T22:56:19.247Z] TOOL RESULT

```
=== PHD ranj ===
PHD.txt:214:a-pus [' BRE] without a son, childless. ár-, v. árdan. 5 āranj "Inc | N ~] elbow.. 9-43. "Ant *a-rāst Prst'] untruth. ārāstan, ārāy- [Pstn!,^Pd- | N ~] prepare, arrange, adorn. ~ién: arrangement, adornment. a-rawüg [”/wbk!] immobile. Ard р | M?yrd, N ~] a goddess; cal. 25th day. ard [KHM A < А gm; п | N ~] flour. агаа [py | (M rd?w)] righteous, truthful. ardan, ār- [THNN-tn' < А V thn; ?l-tn'] grind, mill. ardāyīh ['i?dyh | M?rd?yyh] righteousness, rectitude. ardig [/tyk! | M ?rdyg] battle. ardikkar рук], -kl | M?rdyqr] warlike, warrior. ~ith: doing battle. arduš [”ldwš = Av. aroduš-] a degree of sin. Ardwahišt Prtwhst' | M ?rdywhyst, (N urdībihist)] Right, the second Amahraspand, guardian of fire; cal. 2nd month; 3rd day. arešk [lysk' | M ()rysk, N rašk] envy, jealousy. ~én [-yn'] envious, jealous. ārešn Pim! | M ”7ysn-, N (a)rif] cubit. aryand [?/епа | N ~] horrible. arģawān [*/gwk'*n! | N aryawān] purple. armēšt ["/myst'] inactive, infirm. ~ih: infirmity. armēšt-ģāh [-g’s] secluded place for the infirm. агбуї&п [/wdšn'] growth. ~ig [-y&!] growing, vegetable. ars Dis | M?rs, N ~] tear (drop). artēštār УЯ? | N artēšdār!] warrior. „īh: warriorhood. arus [2/00] white. arwand [wnd] swift, valiant; river Orontes. ~ih: swiftness, valour. arwés [lwys | M ?rwys, N ~] rope. arz [KSP! < А Ар; с | N ~] worth, value. Arzah [Iz h == Av. arazahi-] the eastern continent of the earth. arzan [PE < А prg’; len! | N <) millet. arzàn Plen | M *rz'n, N ~] valuable, worthy. ~ig [-yk'] worthy. ~igih: value, worth, worthiness. arzidan, arz- [?/с-уїп! | N ~] be worth. ~išn: value, worth. arziz (сус | M ?rzyz, N ~] tin, lead. —ën [-yn'] tin, leaden. ārzōg Picwk! | M'wrzwg, N àrzó] desire, lust,
PHD.txt:298:čāšt [ой | N ~] lunch, meal. 1~ag [-k'] food. &а$їар [c'štk'] doctrine. čāštan, čāš- [c?s-tn'] teach. ~išn: teaching. čatrang [cting | (Ar. šatranj)] chess. *taw(la)gan [cwpk'n!! | Ar. sawlajan, N čaugān] (curved) polo-stick ; polo. CaxSágih [ch kyh] (sense of) taste. čaxšišn [chsfn! | M, J схі, N ¿aš-] taste, flavour. 148 [ME < A mh | M cy, N či] what, which. ~ ray: for what, why. ~ih: quiddity, essence. tčē [ME, v. 166] for, because, since, as, that. &ë-ëwënag [ME ^ dwynk!] how. ~ith : circumstances. čegām-iz [су?т-с | M cyg^myc], —-6(w): a little; whatever. Cegámag [cyk”mk! | N &(ag)áma] song, snatch. €éh- , —išn, v. idan. *téhag [cyhk'] grief. čehel [40 | N chil] forty. Céh-widarag [cyhwtlg] = činwad puhl. čēlān [cy”x! | = M, N ~] dagger. ~gar [-kl, -gl | N ~] swordsmith. Cér [cyl | M cyr, N —] victorious, triumphant, brave. —Ih: bravery. Cérihistan, Cérih- [cylyh-stn'] triumph, be victorious. īčīdan, čīn- [cytn', cyn- | M cyydn, cyn-, N ~] gather, pile up. ~išn: gathering. *čīdan, čēh- [cytn', cyh- | M cy-] mourn, lament, grieve. ~i8n : lamentation. ~i$nig¢ : mournful. ihr [cyhl | M cyhr, № ~] form, shape, appearance, face. žčihr(aģ) [cyhl(k') | M сулу, P -g, № ~] seed, origin; nature, essence. Cihrénidan, čihrēn- (cyhlyn-ytn'] form. Cihrig [cyhlyk'] natural. čihr-šnāsīh [суйру] physics. čim [c(y)m | M сут, N ~] reason, cause, purpose, meaning. ~ (ray): why? Cim-gó6wáàgih [сут gwh’kyh] logic. čimīģ [cymyk!] purposeful. čīn-, ~i8n, v. idan. čīnag [cynk! | P cyng, N ~a] grain, bait. Cinàr [су | N ~] oriental plane tree. činwad [cynw(p)t'], ~ puhl: the ‘divider bridge’ which separates the souls of the righteous dead, who cross, from those of the wicked, who fall off.
PHD.txt:314:~th: friendship, love. 140$ [dws | N ~] shoulder. 2108 [duš | N ~] last night, previous evening. dēš-, —išn, v. Ł 2 dēšīdan, !doxtan. dēšag [dwsk'] dear, loving. —ih: love. došaram [dwi?m | M dw%’rm] love. dēšastar [dušstl] west. īdēšīdan, 458- [dws-ytn!] like, love. ~ign: liking, pleasure. *došidan [dwsytn'] = *dóxtan. dēšīzap [dwsyck' | (M дох, ] dwskyzh), N —a] maiden, virgin. “АҺ: maidenhood, virginity. dówom [2wm | N ~] -second (in compound numerals). 1dóxtan, dēš- [dwhtn', dws | N ~] milk. *dóxtan, döz- [dwhtn', dwc- | N ~] sew. dóys?r [dwysl = Av. dõiðra-} eye. dēz-, v. ?dóxtan. drafš [dips | P drfš, N ~] banner. drafšīdan, drafš- [dipi-ytn! | P drfi-, N ~] 1. shine; 2. tremble. drahm [ZWZN! < А zwza | M drhm, N dir(h)am] drachm. dra(h)nāy [di(k)rd) length. dramanag [dimnk! | N dirmana] wormwood. dranģ [ding | N dirang] period, duration. dranjidan, dranj- [dInc-ytn!] speak. ~išn: speech. draxt [4/0)А | M drxt, N diraxt] tree. drày-, ~išn, v. drāyīdan. drayā(b) [dlyd?(p) | M dry?b, N darya(b)] sea. ~-bār LI | N -bàr] sea-shore. агауӣп-јбуіёп [did?n ywdsn'] one who speaks while eating. ~ih: (the sin of) speaking while eating. drayidan / drayistan, drāy- [dPd-ytn!, -stn! | M dryst, dPy-, N daráyidan] speak (daevic), chatter. —išn: chatter. drāz [dlc | N diráz] long. *drém [dlym] phlegm. driyó$ [41220 | N daryūš, darwé§] poor, needy. ~th: poverty. dró [KDBA < А kdb’; dlwb! | M drw, (N daróy)] lie, deceit. drd [SRM < A šim; dlwt! | M атта, N daród] health, well-being, prosperity, peace. dró-dadwarih [KDB A d'twblyh] false judgement. īdron [dlwn' | N dariina] bow. *drón [dlwn' | N darūn] consecrated bread, ceremony in which c.b. is used.
PHD.txt:321:ë ру | (M hyb)] particle giving the present tense optative sense. é, v, éd, éw. ēbāraģ [*dyp'lk', ^dwlk! | N éwàr] evening. ébgat(ih) ['ybgt!, -yh = Av. aifi.gati-] (onslaught of) Evil; the Adver- sary. ēbsrūsrim [>ур-, ?ybslwslym = Av. atBisrūdrima-) the gah from sunset to midnight. ébyünghan [>ур-, ?ywby?nghn!, etc. = Av. aiBydshana-] sacred girdle, = kustig. ёё Pye | (P ?ушус), N héc] (with a negative) not any. ēčand, v. éw-Cand. éd (HN A < A hr? | M? yd] this; v. dāštan. ~ ray ёё [cf. N z-é-rá] because, since. édar [LTME < À I-tnh | M?ydr, N ~] here. édin [ytwn'! | N ēdūn] thus, so. ~ih: (correct) manner. ëg [ADYN' < А *dyn | М ?yg] then, thereupon. ëk Pywk' | M yk, N yak] one. ëkanag [Pywk’nk! | N yagana) submissive, obedient. ^h : submission, obedience. ēk-dād [ywkd’t'] sole-created. ēmēd [*dmyt'] hope. ēn [ZNE < A znh | M *yn, N in] this. -ën [-yz! | = M, N -in] suffix forming adjectives of material or quality. -endag [-ndk! | M -yndg, N -anda] suffix forming present participles. -én-idan [-yn-ytn' | M -yn-ydn, (N -àn-)] suffixes forming causative and transitive denominative verbs. *énókén Pynw(k)kyn' = Av. *aēnē.kaēnā-) heiress (under the obligation of continuing her father's line). enya рулу | (M ?n’y)] otherwise, moreover. lër [d] | M Zur, v. azér] down, below; low; under. — ud abar: upside down. tēr Pyl] noble; hero, ~ih: nobility, good conduct. Eran [y”x! | N ~] Eran, (land of) the Aryans. ~ag [-k'] an Eranian, Aryan. érang [”y/ng] blame, condemnation; error, heresy. ~ih: = érang. éranj-, v.  * éraxtan. Ērān|-šahr (yPnitr! | N ~] land of the Aryans. —-wëz [-wyc] (original) home of the Aryans. 1ёгахќап, ёгапј- Pylhtn!, ?уЇпс- | J ?yrxt] blame, condemn, damn.
PHD.txt:552:puštag 70 ranjfénidan
PHD.txt:555:rabih [/pyh | M rbyh] noon, midday (heat). rad [/t! | N —] (spiritual) chief, master. АҺ: office of rad. rad [Pu | P rd, N ~] generous, liberal. ~ih: generosity, liberality. radag [itk! | M rdg, N rada] line, rank, row. radómand [/t?^wmnd] having a rad. rad-passag [/tps’k'] ceremonies of the gáhanbar festivals. radunay [/twny = Av. ratunaya-] one under the guidance of a rad. raftan, raw- [SGY TWN-tn! < А V sg’; lwb- | M rptn, rw-, N ~] go, move, proceed. ~išn, v. rawišn. raftār [/pt?] | N ~] goer. rag А! | M rg, N ~] vein. «ЛЬ: disposition, character. ray [/gy | P rg] quick, swift. ray [Pg | N —] meadow, plain. rah [/s, lh, [hy | M rh(y)] chariot, wagon. rah-, у. rastan. rah [Ps | M rh, N ~] road, way. rahag [/hk! | P rhg] = rag. rāh-dār [lsd] | N ~] brigand, highway robber. ~ih: brigandage. rahig [/syk!, Ikyk' | M rhyg, N rahi] child, page. ~ih: childhood. rāh-nimāy [Psnm?d | (M r’-hnmwd’r), № ~numa] guide. ram [Pm | М әт, N ~] peace; cal. 21st day. ram(ag) [/m(k') | P rm, N ram(a)] herd, flock. ráménidan, rāmēn- [Pmyn-ytn! | M ?myn-] give peace, pleasure. rāmišn [P min! | M rmyfn, N rāmi$] peace, ease, pleasure. ~ig [-vk! | N —z#] peaceful, at ease. ran [Рп! | N ~] thigh. P rān- [/^n-] fight. randidan, rand- [/nd-ytn! | N —] scratch, grate, abrade. rang [/ng | M rng, N —] colour, dye. ranj [Inc | P rnj, (M rnz), N ~] toil, trouble. ~ag [-k' | N —a] troubled. ranjénidan, ranjén- [/ncyn-ytn'] trouble.
PHD.txt:556:ranjwar 71 rëš
PHD.txt:557:ranjwar [Incwl | (M rnzwr), N ranjūr] troubled, distressed. rapihwin [/pys-, Ipyt-pyn!, -wyn' = Av. rapiüfina-] the afternoon gah; south. ~tar [-tl] southern. rasan [/sn' | N ~] rope. rasénidan, rasén- [/syn-yin'] bring. rasidan, ras- [YHMTWN-tn' < А yhmtwn, V mt^; ls-ytn! | M rs-ydn, N ~] arrive, mature. raspig [Pspyk!] second officiating priest. rast [Pst! | M rst, N ~] true, straight, direct. ~ih: truth, rastaģ [lstk! | N rasta] series, row, progression; element, газап, rah- [Istn', Ї(?)А- | N ~] escape. rastarih [/st?/y%] escape. rasüg [/swk! | (N rāsū)] weasel. Rašn [/@! | M ri, N ~] god of Justice; cal. 18th day. ra&tan, *raz- [/ftn'] colour, dye. raw-, v. raftan. rawag [/wP^k! | N rawá] current. ~ih: currency. rawügenidan, rawagén- [/zob)hyn-ytn!] set in motion, propagate. rawénidan, rawén- [SGYTWNyn-ytn', v. raftan] cause to go, extend. rawišn [lwbin', SGYTWNsn', v. raftan | N rawif] going, motion. ^h : behaviour; as a suffix, forms abstract nouns. ray [Pd | M ry, N ra] postposition, for, for the sake of. rāyēnāģ [Pdym bi | M r’yn’g] arranger. rayénidan, rāyēn- [Pdyn-ytn! | M r'yn-ydn] lead, direct, arrange, organize. ~išn: action, function; arrangement. rāyēnīdārīh [/”*dynyt?lyh | M r!ynyd?ryh] direction, organization, rāyišn [”dsn'] order, arrangement. rāyomand [Pd^wmnd] rich, majestic. raz [/c, lz | N ~] vine; vineyard. raz [Pc | M Pz, N ~] secret, mystery. ~ig [-yk'] secret. rāz-kirrēģ [Pc kylwk' | M г qrwg] architect, builder. razm [/cm | M rzm, N —] battle. —--$àh [-g's | P -g’h, (M rzm?h), N ~] battlefield. razor [lcw] | M rzwr] forest. rédak [lytk' | N ~] lad, page. тёр [/yā! | N ~] sand. rëm [lym | M rym, N —] dirt, filth, purulence. réman [lymn' | M rymn, N ~] dirty, filthy, purulent. ^b : filth. 1r€§ []yf | N ~] wound, sore. *rēš [/yf | N —] beard.
PHD.txt:1656:distressed ranjwar, sto.
PHD.txt:1745:elbow aranj.
PHD.txt:3760:speak dranjidan, guftan, P wāxtan; (daevic) dawidan, drayidan.
PHD.txt:3766:speech dranjišn, gēwišn, guftārīh, saxwan, waz; v. good, evil.
PHD.txt:4025:toil ranj.
PHD.txt:4076:trouble (v.) āyēzīdan, ranjénidan.
PHD.txt:4077:troubled ranjag, ranjwar.
PHD.txt:4102:ranj, sēj,
PHD.txt:4917:rozag ranjēn-, rūzēn-
PHD.txt:4918:ranjēnīdan, rozēnīdan
PHD.txt:4919:lawzēnag rūzīg rozwürag rozan ranjwar rozward rozgar ranjag, rozag rozbinag roz-Saban rosnih rēšn rūšnag rūšngar rodbar rodigan rodig 12го rüdan abàg! rūstūg
PHD.txt:4933:ranj, róz
=== NYB ranj ===
1323:dranj
1333:dranj [dlne'] *persevering, persistent: zuästan ~ būt hend they continually,
1336:dranj.
1338:dranjišn [dlnešn'] recitation (by heart), recital 7315. 7519.19, — From Av. (772 sq.) 2drang-; Paz. drenžešn, Skr. v. vākya (Mx), pralapa (SGV).
1339:dranjišnčh det. v. n. = the preceding w.: xup ~ eloquence, rhetorical power 7022,
1451:age DkM 6989; tat pat dātistān(ūman>- deh či veh tuvän zatan u éraxtan cigón ka-š pat davreh u drusteh apäk gēbāh through righteousness thou art better able to defeat him and make him lose the case than if thou speakest to him coarsely and roughly (cf s. v. davr) PR 573; — pres. pass. 3d p. sg. éraxtét he is pronounc- ed guilty, opp. buxtet he is acquitted, v. Bthl, ZsR IV, 8; Paz. buxted ... érexted SGV III, 26; kē rāstēh rad pat xudstak eraxtet, ah veh cigon kē družeh rād pat ruvān éraxtét he who suffers loss of prop- erty because of his righteousness is better than the one who suffers the loss of his soul (forfeits his soul) because of his falsity PR 26$-9.] — Two vbs. seem to have coalesced here: 1) črtatan ērēc-, cf Paz. érexted and the caus. érezinidan ‘to condemn’ SGV XI, 257, most probably < abi- + Av. (1479 sq.) raék- ‘to leave in the lurch, to abandon to destruction’ (Bthl IF XII, 112sqq.); 2. éraxtan érang-, most probably a denom. of érang, črangčh 'trouble, delusion' (Paz. ŠGV X, 58 ete.) < *abi-ranga-, cf. an-črang, ranj, ranjak; MPrs ‘yrat, “yrnz- ‘to combat’, Verbum 199. (Bthl, l.c. adopted the reading érazt).
1492:frac [pr’c, pc] 1. adj. forward; promi- nent, distinguished, comp. ~-tar 14, sup. ~-tom 1021?.19, — 2. adv.: ē tigriyaf ~-tar one bowshot further 212’. 222; m 1094, hac nun ~ 611? henceforth; hac han ~ thenceforth 985; ~ 6 P2:9. — 3. prev. ahead, along, forth, forward, on (-ward), up, ete., or denoting the perfec- tive aspect, both in a local and in a figurative sense, with a great many vbs., v. each separately; also together with v. nouns: ~ guftür, ~ ranjakēh, ~ tuxšākēh,
2286:kém-ranj [kymlne] having little pain, almost: having no pain, painless, healthy 714, v. ranj.
2365:mà PL] not, with the imp. and the subju. in an optative sense: mà kun! mā baš etc. ; imp. with the ending -ē: mā 6 änöd rave! 441; ma framäye 5774-5, ete.; pl. mā dārēt! mà ranjénét! ma ‘BYDWN-x, = kunēt 82-13; — subju.: hàn rēc mà bavā ku may that day never come when 13%; -t garān mā sahät 35%, v. sahistan; mà xin YHMTWN-d = rasünd 26% etc. — Com- mon Iranian.
3219:ranjihistan
3240:ranj [Inc'] trouble, toil, grief 1313. 5629, ete. — MPrth rnj; MPrs rnz (A-H II), rnzwr ‘distressed’ (S); Paz. ranj, rand; NP ranj. V. raxtan.
3241:ranjak distressed, exhausted, jaded 8!?. 5622,
3242:ranjakčh tiredness, exhaustion 923; labour, pain 5671; frac ~ 5674.
3243:ranjénitan (Incynytn'] to weary, to harass: aspān mā ranjēnēt! 8%,
3244:ranjihistan [Incyhstn'] to be exhausted, to tire oneself out, to strive in vain for (pat) 46. — Pass. of the preceding vb.
3289:raxtan [Ihtn'] ranj- [Inc-] to vex, to grieve, to exhaust: pt. pass. raxt exhausted 3319.
3291:NP razt ‘sadness, grief’, raxtah ‘wounded, sick, diseased’, ef ranjidan ‘to be sad, vexed’, ‘to fret’; MPrs ratrnz (= raxt- ranz) ‘troubles, pains’ (A-H II), v. also ranj, ranjak, ranjēnītan and cf éraxtan.
4382:xučš [NPŠH; hwyš] 1. refl. pron. self, valid for all persons, a) referring to the agent = the logical subj.: -š ~ hécak hac cäh ul hixt he himself hauled up 1519; b) as an obj.: ~ hac ranj äsän kartan to relieve oneself of trouble 1313-14; c) after a prep.: vinäskäreh andar ~ bē guft 3474; (šmāh) ~ rād 45°; d) as a refi. poss. pron.: 4 ~, passim, e.g. hac avatdi i avēš 51"; ruvün i ~ rädY F:2; hac har i ~ F:3; or ~ alone, or kan i ~, both placed before their subst.: pat ~ casm 80%; hac ~ xünak ŠPrs: 10; api-š ~ GfrinY kart" and he praised himself Pl: 10-11; hàn i ~ xvatāt 5%; also fravahr ēt i ~ 88%; har kas õi i dit ētūn döst bavet cigon i ~ everyone will be as friendly to the other as to himself 10412-15; e) as an attr.: ~ Zartuxšt 5228; — emphatic form ~-tan or (659. 928) tan 4 ~ (v. tan): ~-tan u asvārān ranjak mā dārēt 8? ; —-tan o marg
4568:Zrang [zlng; inscr. zlngy] the old name of Sakistàn (before the invasion of the Sakas); in P1:7 it has its own satrap and seems to designate a subprovince of Sakistan; 116? the name of the town called by Yagut 2,926 Zaranj, which was the capital of Sakistan. — In the OP inscriptions Zranka-, but Gr Apayyıavn, Lat. Drangiana with the SW develop- ment of z- > d-.
5130:ldrang-: dranj
=== HRN ranj ===
607:phlv. äranj (PPGL).
4315:karanjäl, kalanjär).
6600:756. sog 'Trauer, Kummer.
9302:'tvar, war in nmetwär, öjwar^ ranjfwar; arm. -ber^
10368:71. dranjttan 'hersagen*, droifjfwJfau , dranj(i)sn (päz.
15891:dranjltan 71.
=== CHEUNG ranj ===
1957:ultimately yields the meaning ‘cultivation’. Pth. 'brng, 'brnng is rather from *Hranj. 
5960:*NWIR: Bal. draht, dratk, dranjit, tranjit/dranj-, tranj- ‘to hang up’ 
5974:Shahbakhsh: s.v. dranj- 
12947:saved’, CSogd. zrync ‘to save, deliver’ (caus., ? supplet. *ranj-) 
13001:*Hranj 191 
13043:*Hranj ‘to take action, spur, urge (often with negative consequences) ?’ 
13051:*MIDDLE PERSIAN: BMP Incyn- /ranj-/ (sec. caus./denomin.) ‘to trouble’, MMP rnz 
13053:31], to conquer, defeat [Boyce 1977: 21]’, BMP ’ylnc- /éranj-/ 1. ‘to blame, 
13056:(+ *abi-) Pres.: IND. 3pl. BMP ’ylncynd /éranjénd/, SUBJ. 1sg. MMP ’yrnz’’n; Partic.: perf. pass. BMP 
13075:*NWIR: NP ranjidan ‘to exert effort’, (old ppp.) raxtah ‘wounded, ill’, ranj ‘effort, 
20601:*OLD PERSIAN: (+ *4-) ? El-OP /äranjanam/ <ha-ra-an-za-na-um> ‘decoration’ (cf. 
20621:NP abranjan ‘a bracelet or anklet (of gold or silver)’ (also auranjan), NP aurang 
23935:*stranj ? 367 
23984:*stranj ? ‘to become stiff, stiffen’ 
25746:*NWIR: NP taranjidan/taranj- ‘to press’ (< Sogd.) 
25748:*NEIR: Ishk. tsranj-/tsrayd- ‘to compress’, M. tro(n)jv-/tardyd- ‘to stretch’, Yi. 
25749:traz-/trayd- ‘to tie’, Wa. tranj-/tranjd, tranZ-/tranZd-, trayd-, trayn- ‘to press, 
33687:ranj-, 191 
34154:/aranjanany «ha-ra-an- 
35002:"yInc- /eranj-/, 191
```


## [2026-09-06T22:56:26.352Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '13040,13090p' CHEUNG.txt",
 "description": "Print Cheung *Hranj entry"
}
```


### [2026-09-06T22:56:26.396Z] TOOL RESULT

```
Cheung 2002: 218, 233 


*Hranj ‘to take action, spur, urge (often with negative consequences) ?’ 

*AVESTAN: Y Ау. ronj- ‘to spur (?)’ = Liste: 56, 58 

Pres. them.: IND. 35р. YAv. ronjaiti (Y 10.8); Partic.: fut. YAv. ()raxSiiant- ‘defiant’ (Y 12.4); Caus.: 
pres. IND. 35р. YAv. (fra) ronjaiieiti (Vr 7.2). © On the connection of Y Av. (^)raxsiiant- to ronj- see also 
Kellens 1984: 160 f., n. 4; De Vaan 2003: 387. 

*MIDDLE PERSIAN: BMP Incyn- /ranj-/ (sec. caus./denomin.) ‘to trouble’, MMP rnz 
‘toil, labour, trouble’ || (+ *abi-) MMP ’yrnz- ‘to fight, dispute [MacKenzie 1971: 
31], to conquer, defeat [Boyce 1977: 21]’, BMP ’ylnc- /éranj-/ 1. ‘to blame, 
condemn, damn [in court]’, 2. ‘to fight, dispute’ > DMMPP: 296a 

(+ *abi-) Pres.: IND. 3pl. BMP ’ylncynd /éranjénd/, SUBJ. 1sg. MMP ’yrnz’’n; Partic.: perf. pass. BMP 
’ylhtk /eraxtag/, ВМР ’ylhtk /eraxtag/ 


192 *Hrau 


*PARTHIAN: rnj ‘toil, labour, trouble’ {hapax} || (+ *abi-) ’brng, *brnng ‘zeal’ 
= Ghilain: 296a | DMMPP: 14a 

*KHOTANESE: (+ *4-) LKh. ärramj- (arraj-) ‘to contract, diminish, shrink’ || (+ *pati-) 
pàris- ‘to diminish [intr.]’, päramj- (caus.) ‘to diminish [tr.] > SGS: 10, 82, 81 
*SOGDIAN: SSogd. rxn-, BSogd. ryn-, CSogd. rxn- ‘to dare’ (with metathesis) 

Pres.: IND. 15р. SSogd. L’ rxn’m ‘I don’t dare’, 35р. dur. CSogd. rxntysqwn, SUBJ. 3sg. CSogd. rxn’t, 
Impf.: IND. Isg. BSogd. ryn’w; ’z-Impf.: IND. 3sg. CSogd. rxn’z, 3р1. CSogd. "rxn'nt 

*CHORESMIAN: rnj’wy- ‘to exert effort’, rnj ‘effort? (LW ?) © Samadi: 172 

*NWIR: NP ranjidan ‘to exert effort’, (old ppp.) raxtah ‘wounded, ill’, ranj ‘effort, 
‘to afflict, torment, cause to suffer’, Ham. ränjayän/ränj- ‘to be offended’ 

*NEIR: Yghn. raxn-/räxnta ‘to dare, be bold’, Sariq. rinj, rinc ‘light [of weight], fast’ 
*SANSKRIT: ramh ‘to hasten’ (RV+) = EWAia II: 421 f., 473 

«PIE *H,leng""- ‘to spur, impel, incite (to act, work, run, etc.)’ = LIV: 247 | Pok.: 
660 f. 

*IE COGNATES: Olrish lingim ‘I jump’, OHG gi-lingan ‘to take place, succeed, have 
success’, NHG gelingen 

*REFERENCES: Christensen, Contributions I: 163, 260; Christensen, Contributions II: 57, 115; Abrahamian 
1936: 119; Andreev — PeSéereva: 313a; Gershevitch, Mithra: 181 f.; EVS: 68a; Nyberg II: 71b Ё; Werba 
1997: 223
```


## [2026-09-06T22:56:53.576Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== v2 ranz ===\"; grep -n \"ranz\\|ranj\\|rnz\" BQT_v2.txt BQT_v2_pages.txt | head -20\necho \"=== v2 rdjyate/rjyate ===\"; grep -n \"jyate\\|rdjy\" BQT_v2.txt BQT_v2_pages.txt | head -20\necho \"=== v2 'رنج ' headword ===\"; grep -n \"‫رنج\\|رنج -\\|رنج ‪\" BQT_v2_pages.txt | head -20",
 "description": "Grep BQT v2 for ranj"
}
```


### [2026-09-06T22:56:53.679Z] TOOL RESULT

```
=== v2 ranz ===
BQT_v2.txt:38594:و بادشاه است » از رشة rinj ranj 4 raj‏ بمعنی ساطنت کردن ۰ حکومت کردن « ولامز 
=== v2 rdjyate/rjyate ===
=== v2 'رنج ' headword ===
2849:‫و مبرآخور را هم کفته‌اند که رش سفید طوبله‬              ‫رنجوریرا گویند که ابام قاهت او باشد و بوفت‬
7158:  ‫)‪ :‬جنگال‪.‬‬  ‫کهک‬‫رنج‬
13223:                                                         ‫میباشه ‪ -‬وبکراول وثالی بروزن برنج ‪ .‬گرفتن‬
13606:‫حتج = بفتح اول بر وزن رنج ‪ ۰‬بمءنی‬                               ‫خنبور ‪ = ۷‬هتح اول و ضم بای فارسی‬
14573:              ‫سابة خورشید سواران طلب ‪.‬‬              ‫رنج خود و راحت باران طلب‬
17178:                                             ‫رح‬                                   ‫رنج ومشفت کشیدن باشد ‪.‬‬
21104:                                                             ‫عشاق ‪ -‬وسختی ودرشتی وکلفت ورنج ‪ -‬و محل‬
24221:‫شهری است از ولایت کیلانکه آنرا «بیه پس»‬                         ‫از سردوش است نا آرنج ‪ - ۴‬ومسافت ميان دو‬
24919:‫سکون ثالی وجیم»‬        ‫رنج ‌‪ -‬بقتح اول و‬                      ‫ر نبه ‌ = ْم اول پروزن دلبه» بم‌عنی‬
24992:   ‫رنجه › بپلری [‪« 12۲‬باروچا ‪( 2[71۵۲ ۰ ۹۵۲‬غم » درد ‪ ۰‬تاراحتی) » دراوراق‬ ‫‪۱‬‬
28402:    ‫‪ = ۴‬زرتك = ‪ « 51۲60۲61‬ثابتی ‪.*4۸۱‬‬                      ‫ص‪ > 4۸‬ورك ‪ :‬همان کناب ‪ :‬زرنج ‪.‬‬
32088:                     ‫‪ - ۸‬مخفف آن «سا» ‪:‬‬                   ‫‪.‬‬   ‫سارنگه‪‎‬‬   ‫سارنج ‪۰‬‬       ‫سالنج »‬   ‫‪:‬‬   ‫رك‬   ‫‪-‬‬    ‫‪۷‬‬
40167:    ‫‪ - ۴‬سیجمند بمعتی دارنده رنج ‪۰‬‬                  ‫‪ ( 600۵5‬فر ) « لك ‪ ۲‬ص ‪۱۱۳٩‬‏ ‪.‬‬          ‫‪= ۴‬‬
```


## [2026-09-06T22:56:56.857Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '24910,25010p' BQT_v2_pages.txt",
 "description": "BQT v2 ranj entry"
}
```


### [2026-09-06T22:56:56.906Z] TOOL RESULT

```
                                                     ‫بیان بیستم‬

            ‫در رایبی نقطه بانون مشتمل برسی و شش لغت و کنایت‬
‫رب است که موی زهار باشد ؛ و بفتح اول هم‬                      ‫رفت ^ ‪ ۰‬بنم اول وسکون انیو بای‬
                                        ‫کفته اند (‪. )۳‬‬                               ‫ایچد » موی زهار را گویشد ‪.‬‬


‫سکون ثالی وجیم»‬        ‫رنج ‌‪ -‬بقتح اول و‬                      ‫ر نبه ‌ = ْم اول پروزن دلبه» بم‌عنی‬

   ‫(‪)۳‬خم‪۶ ۱‬‬                 ‫‪.‬‬    ‫‪ +۲ :‬یز‬       ‫‪ ,‬چش‬    ‫چك‬    ‫(‪)۷‬‬             ‫‪ :‬رند ویاژند ‪.‬‬       ‫)‪ (۱‬جك‬

                                                                                                  ‫ویفتح‪ ...‬گفته‌اند ‪۰‬‬


  ‫را‬   ‫خاش مولف ‪kãma ۰‬‏‬             ‫و‬      ‫ما «بوتکر ‪۵‬‬             ‫بهلوی ‪1‬‬          ‫هر ‪namr„ ۰‬‏‬           ‫‪۱‬‬

  ‫‪ . °‬رك؛ رمه‪.‬‬        ‫‪ «9‬باروچا ‪۸‬‬       ‫ات‬     ‫‪10۷‬‬         ‫‏‪ hamãk‬خوانده بمعتی همه (ه م ( حزوارش همه‬

                                                                                            ‫بایف دالت که فرائت‬


             ‫«سه رك‪ :‬زیون » اربون ‪ ۰‬ارمون ‪.‬‬            ‫‪۳‬‬              ‫باروچا ‪۹۱۲۰‬‬     ‫‪ ۷۰‬ورك‬            ‫بمعئی ما ‪2‬‬

 ‫تفس ‪٩.۰‬‏‬   ‫‪ :‬رم» رمكڭ؛ معرب آن رمق‬
                                  ‫سشق ‪ ۰۲1۰‬رك ‪:‬‬             ‫داد‬       ‫‪۰1‬‬            ‫‪ -‬بهلوی‪2۳13۲ 6‬‬
   ‫‪( -‬عر) رمه (حنم اول وتشدید دوم ‪ .‬بارء رسن بوسیده»‬                                     ‫رك ‪ :‬رفه‬         ‫‪۴‬‬

   ‫استخوان‌پو‪-‬یده» مورچۀ پردار» کرمك‌چوبشواره‬                ‫پیشالی؛ جمله وسائر؛ رمه (بکسراول ‪e‬‏‬
                                ‫رك‪ :‬رمن ‪.‬‬      ‫‪- ۱‬‬           ‫خاك مناك » مغز استخوان » «منتهی الارب <‪.‬‬
  ‫رك‪ :‬رلب‪.‬‬     ‫‏‪- ٩‬‬             ‫رلبة» رمعان‪.‬‬     ‫رك‪ :‬روم » روههه‬        ‫‪۸‬‬            ‫‪ :‬رامیار ‪.‬‬    ‫رك‬      ‫‪۴‬‬


  ‫(پوند مصدری)؛ ترسان شدن‪ ,‬احتراز کردن‬                     ‫دن‬
                                                            ‫‪ #‬رمیدی ‪ -‬بفتح‌اول وسوم؛از‪ :‬ربم‪۳‬‬
                                              ‫از فرت وکراهت ‪ -‬پربدن از بیم‪ -‬آشفته ویربشان شدن ‪.‬‬
  ‫رند افریس‬                                                                                                         ‫وت‬
 ‫خوشبو وخوشگوار حم آمده است‪ -‬وبممنی گرد‬
‫وفبار باشد چه خاکے رند کردیرا کوبن که از‬                                                    ‫و بممنی خشم و قهر وب‬
                                                                    ‫حم هست‪ -‬و رنگه‬
‫روی خاک برخیزد ‪ -‬و مورد را نکیفزته‌اند که‬                                                     ‫‪.‬‬   ‫‪۴‬‬   ‫ولون را نیز گویند‬


 ‫بعر بی آی خواند ‪٩‬‏ ‪ .‬وبعضی گوبند رلد درخت‬
                                                                    ‫ر نحال س بروزن‌چنگال‪ ,‬طمعام‌رخوردلی‬
 ‫غار است ‪٩۱۰‬‏ وآن درختی باشد برزکه وربکه‬
                                                                                                               ‫رگاونند ‪.‬‬
 ‫آن بزرکتر از برکه بید میشود وآنرا بیونالی‬
 ‫ذاقی‪۱‬اخوانند‪ -‬وربودن ودزد‪:‬دن راهممیگویند‬
 ‫وهرچیز زمخت رانیز گوبند همچو مازو وحلیله‬                                                             ‫مرض دق باشد ‪. ۴‬‬
 ‫ووست انار و امثال آن‪ -‬و بکر اول‪ .‬مردم‬
                                     ‫پ‬
 ‫محیل وزیر کے وبا که ومنکر ولابالی وبی‌قید‬
                                                                    ‫‪ -‬بروزن‌ینجه» بمعتی | زرده ‪e‬‏‬

                                                                    ‫نازو تبختر‬    ‫)‪ (۱‬باشد‪ -.‬واز روی‬
                                                                                                           ‫ره ‪۴‬‬
                                                                                                              ‫نج‬
                                                                                                           ‫وسماری‬   ‫وزحمت‬

 ‫باشد» وایشالر! ازاین جهت‌رند خوانند که منکر‬                                                  ‫خرامیدن را نیزکوبند ‪.‬‬
 ‫اهل قد و صلاح اند وشخ که ظاهر خود رادر‬
                                                                    ‫ر ثد = بنتح اول و سکرن الی و دال‬
        ‫د‪. )۲( ۴۱2‬‬
                 ‫ملامت دارد وباطتش سلامت با‬                                                           ‫أبجد ‪ ,‬بمع‬
                                                                                                    ‫وتی‬
                                                                                                 ‫‪ .‬حر‬
                                                                                                ‫خف‬
                                                                    ‫باشد ‪ -‬و تراشه را‬         ‫ن_‬
 ‫با همزه و فا ورای‬                ‫ر ندافریس ‪-‬‬                       ‫کوبند که از چوب جدا شود ‪ -‬و دست افزاری‬
 ‫فرشت )س( وبای حطی )‪ (£‬وسفن سمفص(‪)٥‬‏ ر‬                              ‫رودگران بدان چوب و نخته تراشند ‪- ۷‬‬ ‫کده‬
 ‫بادشاه‬   ‫بمعنی‬           ‫انگیز ‪E‬‏‬               ‫ت‬
                                                 ‫اع >‬    ‫وون‬
                                                                    ‫وامر برندیدن هم هت یعتی برند‪ - ۷‬وچوب‬
   ‫بادشاهان باشد که کنابه از پرورد گار اک‬                           ‫و معلی‬           ‫تراش و تراشنده را نز گفته اند ‪۸‬‬

                      ‫‪-‬خصیکه ‪ ...‬سلامت باشد‪.‬‬
                                           ‫وش‬‫(‪ )۲‬خم ‪: ۱‬‬                                 ‫‪:‬بیمار ‪.‬‬
                                                                                               ‫(‪ )۱‬خم‪ ۱‬و‬
                        ‫() چك‪ - :‬سعفص ‪.‬‬                        ‫)‪(٤‬‏ چك ‪ :‬وبا‬                ‫(‪ )۳‬چك‪ :‬و را ‪.‬‬

   ‫رنجه › بپلری [‪« 12۲‬باروچا ‪( 2[71۵۲ ۰ ۹۵۲‬غم » درد ‪ ۰‬تاراحتی) » دراوراق‬ ‫‪۱‬‬
             ‫تورفان ‪( 212۲‬درد) ازماسکریت ‪ ( 612۷[۲‬در اضطراب شدن) رك ‪ :‬سر که ‪:۱۹۱‬‬
         ‫که له رات رسد زخلق» نه رنج‪.‬‬                                          ‫کر کزندت رسد ز خلق مرلج‬
   ‫«کلتان ‪. ۷۲1۰‬‬
                                                                                        ‫‪:‬‬   ‫رنگ‬   ‫؛‬   ‫رك‬      ‫‪۳‬‬


                ‫ابن برنج ازعفیق وآن از در‪.‬‬                                    ‫پهلو از پبه و کردن ازخون پر‬
       ‫نظامی کنجوی دروصف کورخر « هفت یکر ‪ ۰‬چاپ‌ارمغان ‪۳.2‬‬

                                                     ‫رلج («‪.‬م‪ ).‬چ‬    ‫اب‬   ‫‪۳۴‬‬            ‫ترجمه «دق» ‪.‬‬          ‫‪۴‬‬
                ‫‪.‬‬   ‫کرد‬   ‫را رنسه‬      ‫خود‬   ‫سممین‬    ‫ساعد‬
                                                                     ‫*ر‪-‬که باپولاد بازو پنجه کرد‬
                                                                                               ‫ه‬
   ‫« کلستان ‪. ۳1۰‬‬
        ‫ارندندم؟ ‪.‬‬                ‫‪ ۸‬مضفف‬         ‫‪:‬لدندن ‪.‬‬
                                                        ‫‪ - ۷‬رك ر‬     ‫‪ -‬رك‪ :‬رنده ‪-‬‬ ‫‪۹‬‬

                          ‫‪. ۸۳‬‬        ‫‏‪ ٩‬رید = مورد ‏ ‪sutryM 51۵۷۵۲۳۳06‬‏ ت«ایتی‬
```


## [2026-09-06T22:57:30.129Z] TOOL CALL #45: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%84%D9%82%D9%84%D9%82",
 "prompt": "Give the Arabic etymology and senses of لقلق (laqlaq) 'stork' and لقلقة (laqlaqa). Is it said to be onomatopoeic or borrowed from Akkadian/Aramaic? Also give the Persian section for لقلق if present."
}
```


## [2026-09-06T22:57:31.789Z] TOOL CALL #46: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%84%DA%A9%E2%80%8C%D9%84%DA%A9",
 "prompt": "Give the Persian etymology of لک‌لک (laklak) 'stork' — borrowed from Arabic لقلق? onomatopoeic? Any Turkish leylek connection?"
}
```


### [2026-09-06T22:57:36.767Z] TOOL RESULT

```
# Arabic Etymology and Definition of لقلق

## Etymology
The word **لقلق (laqlaq)** meaning "stork" has a documented linguistic heritage. According to the Wiktionary entry, scholars "Compare Akkadian _laqlaqqu_ ('stork') and Persian _lak-lak_." The source suggests the term possibly "came from Akkadian via unattested Aramaic," though this transmission route remains speculative.

The etymology is **not described as onomatopoeic**—rather, it's presented as a borrowing from ancient Akkadian, potentially transmitted through Aramaic languages.

## Definition
**لقلق (laqlaq)** is defined simply as: a large wading bird known for its long legs and migratory patterns. The plural form is **لقالق (laqāliq)**.

## Note on لقلقة
The web content provided does not include a separate entry for **لقلقة (laqlaqa)**. The page only covers the noun **لقلق**.

## Persian Section
No Persian-language section appears in this English Wiktionary entry. However, the etymology notes Persian **لک‌لک (lak-lak)** as a cognate term, indicating related vocabulary exists across languages.
```


### [2026-09-06T22:57:37.152Z] TOOL RESULT

```
# Etymology of لک‌لک (laklak)

According to the Wiktionary entry, the word's origin is described as: "Probably ultimately from Semitic." The entry provides cognates including Akkadian *laqlaqqu*, Arabic *لَقْلَق* (laqlaq), and Assyrian Neo-Aramaic *ܠܲܩܠܵܩܵܐ* (laqlāqā)—all meaning "stork."

The source does not indicate whether the term is onomatopoeic. Rather, it traces the Persian word back through a Semitic language family connection.

Regarding Turkish: The descendants section shows that Persian *laklak* influenced Turkish *leylek*, demonstrating a borrowing pathway from Persian into Turkish, not the reverse. The Turkish form descended through Old Anatolian Turkish intermediaries.
```


## [2026-09-06T22:57:45.219Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON part2 لاله ===\"; grep -n \"لاله\" MON_part2.txt | head -8\necho \"=== MON part2 لالک ===\"; grep -n \"لالک\\|لالكا\\|لالک\" MON_part2.txt | head -5\necho \"=== MON part2 لعل ===\"; grep -n \"لعل\" MON_part2.txt | head -8\necho \"=== MON part2 لکلک ===\"; grep -n \"لکلک\\|لك لك\\|لقلق\" MON_part2.txt | head -8\necho \"=== MON part1 رنج ===\"; grep -n \"^رنج\\| رنج \\[\" MON_part1.txt | head -8",
 "description": "Grep Mo'in 2-vol OCR"
}
```


### [2026-09-06T22:57:45.349Z] TOOL RESULT

```
=== MON part2 لاله ===
2197:غلاله: (ه‌هاقاهر [ع. غلاله ] (۱.) بالشجه‌ای 
2200:غلاله؛ (6-)01212 [- کلاله - کلاله] (۱.) 
4663:فُالق: 102 [ع. (افا.) لاله بیرون 
8879:فند قه ند شده باشند مانند موه آ لاله و 
20424:سوراخ‌هایی که در زیر صفحه کلاله واقع 
24675:کلال: 2۱۶۱ [تس. کلاله] (ا۰) قسمتی از سر 
24685:کلاله: (-)۵۱2۱2! [ع. کلالة] (.) کسی که نه 
24691:کلاله 
=== MON part2 لالک ===
24703:طرء گلالک] (.) موی بیچیده» مجعد. 
38220:لالکاء لاله گوش. شمعدانیی دارای کاسه‌ای 
=== MON part2 لعل ===
6183:معدنی (لعل. یاقوت و غیره). فرزند خاور: 
18516:طلب چیزی را می‌رساند؛ لعل» بوکت» ب وکه 
26632:کار تسلطی ندارد. شراب لعل انگوری که به 
33852:(گی.) گل پیاده. گل لعل: ( کی نوعی کل 
38107:۳ ۱2۱ اقس. لاله» آلاله» لعل» معر.] (ص.) 
38108:سرخ؛ احمر. (4) (زه.) لعل. 
38527:اصطلاحات). لب لعل: (تص.) بطون کلام 
39052:زدن: 107- 111-111 ل لعلعه؟ ] 
=== MON part2 لکلک ===
8996:آواز لقلق و قلقل بر آید. 
25403:آسا رود؛ لکلکه. ۱ 
39944:لقلقو : تناها (ص.) (عم.) آنکه از شدزتا 
39947:لقلقه: (م)«هاها (ع. لقلقة] (مصل.) 
39948:سخت آواز کردن لکلکك (غم.) (.) اواز 
39949:لکلک (غم.) ) آوازی همراه با جنش و 
39950:اضطرات. فصاحت عاری از بلاعت. لقلقه 
40087:لعلی؛: ۱:۸۲ [- لکلکه) (.) سجن بهوده؛ 
=== MON part1 رنج ===
2857:رنجیدگی» رنجش» شکراب. اندوه» عم 
2902:رنجش» رنجیدگی. خشم» غضب. صدمه» 
2906:رنجانیدن» رنجه کردن» گزند رسانیدن. به 
4282:رنج‌های سدنی. آلام روحانی» روحی: 
21216:رنج» مشقت. (ص.) ز شت» قبیح. 
24670:رنج» گزند؛ مسحنت. نعدی؛ جوره آزار. 
25200:رنج: ازار. ازمایش؛ ج. بلایا. 
34247:رنج دیدن؛ عدذاب دیدن جزا بافتن» به سرا
```


## [2026-09-06T22:57:47.178Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK 660 area lengh ===\"; grep -n \"leng[uv]h\\|leg[uv]h-\\|lengṷh\" POK_full.txt | head -20\necho \"=== POK slēg ===\"; grep -n \"λαγγάζω\\|laggazo\\|lagaró\\|slēg-\" POK_full.txt | head -20",
 "description": "Grep Pokorny"
}
```


### [2026-09-06T22:57:47.247Z] TOOL RESULT

```
=== POK 660 area lengh ===
=== POK slēg ===
```


## [2026-09-06T22:58:01.356Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nls POK*; python3 - <<'EOF'\nd=open('POK_02.txt',encoding='utf-8',errors='replace').read()\npg=d.split('\\f')\nprint('leaves',len(pg))\nfor i in (315,316,317):\n    print('=== leaf',i,'(printed ~',i+344,') ===')\n    print(pg[i][:1800])\nEOF",
 "description": "Pokorny p.660 area"
}
```


### [2026-09-06T22:58:03.194Z] TOOL RESULT

```
POK_01.txt
POK_02.txt
POK_03.txt
POK_full.txt
leaves 434
=== leaf 315 (printed ~ 659 ) ===
_,  m.)  ,Lohn,  Vergeltung^,  anord.  laun  n.  PI., ags.  lean  ds. ;
aksl.  lov^  ,Fang,  Jagd^,  loviti  ,fangen,  jagen^;  lit.  lävinti  ,abrichten^ usw.  ist  russ.  Lw.
WP.  II  379  f.,  WH.  I  826,  Trautmann  153.
laukip)-  (buk-)  ,Kehle,  Schlund',  , schlucken,  schlingen^?
Hom.  XavKaviTj  ,Kehle,  Schlund',  lit.  pa-laükis  ,die  Wamme  des  Rindes', wruss.  ikac  (*hkati)j  Iter.  lykac  ,schlucken,  trinken'  usw.  (klr.  iyhaty ,schlucken'  mit  h  aus  ursl.  g,  vgl.  die  wohl  verwandte  Wz.  {s)leug- ,schlucken').
WP.  II  380.
ie-  s.  1.  lä-.
iBb-,  ihb-,  lab-,  leb-  , schlaff  herabhängen',  auch  , Lippe'  (?),  z.  T.  mit  anlaut. s- ;  daneben,  aber  weniger  häufig  (s.  dazu  lep-  , abschälen'  am  Schlüsse) Formen  auf  -p-;  nasaliert  {s)lemb(h)-.  Viele  expressive  Bildungen. Gr.  Xoßög  , Schotenhülse,  Samenkapsel;    Ohrläppchen',  l'Uo/Jog  ,schoten- tragend',   Xs^iVjQlg   , Schlangenhaut,   Bohnenhülse'    Hes.,   Xsßivd-oi   , Erbsen'; lat.  nur  mit  n:  läbö,  -äre  ,wanken,  schwanken',  läbor,  -t,  lapsus  , gleiten, sinken,  fehlgehen*;  läheSj  -is  , Einsinken,  Fall,  Erdrutsch;  Untergang,  Ver- derben' und  , Makel,  Schandfleck';  vielleicht  lahor,  -öris  ,Mühe,  Last;  An- strengung;  dann:   Arbeit',   lahöräre  ,sich  mühen,  geplagt  sein'  (eigentlich
656
,(ias  müde  Wanken  unter  einer  Last*);    wohl  lahium  (laheum),  lahrum (meist  PL  labia,  lahra)  ,Lippe,  Rand';
reich  entwickelt  im  Germ. :
1.  isl.  norw.  lapa  , schlaff  herabhängen',  isl.  lajpi  ,homo  sui  negligens*! mhd.  erlaffen  , erschlaffen*,  nhd.  Za^  , schlaff,  matt*;  geminiert:  aisl.  lepp^ m.  (Happja-)  , Lappen,  Locke*,  as.  lappo  , Zipfel,  Lappen*,  mnd.  lapp^ , Stück,  Lappen,  Wamme*,  ags.  Iceppa,  la
=== leaf 316 (printed ~ 660 ) ===
.  labbe  ,(hängende)  Lippe*,  ahd.  (aus  dem  Ndd.)  lappa  f.,  mhd.  läppe f.  m.  , niederhängendes  Stück  Zeug,  Lappen* ;
2.  mit  der  Bedeutung  _,Lippe'  als  ,die  hängende*^  (wie  lat,  labium):  mnl. lippe  i.j  nhd.  Lippe,  afries.  ags.  lippa  m.  , Lippe',  (*lepi-an-),  norw.  lepe (Hep-an-),  ahd.  leffui^^  as.  lepiir  ds.,  ahd.  lefs  ,Lefze^  (*lep-s);
3.  mit  anlaut.  s- :  got.  slepan,  saizlep,  as.  släpan,  ahd.  släfan,  ags.  slcepan , schlafen*,  got.  sleps  usw.  , Schlaf*,  aisl.  släpr  , träger  Mensch*,   ndl.  slaap, ahd.  släf  m.,  nhd.  .Schläfe']  mnd.  ndl.  slap  ,schlaff*,   ahd.  slaf  (ff-),  nhd. schlaff,   isl.   norw.   slapa  (=  lapa)    ,schlaff   herabhängen*;    geminiert  aisl.  ^ slappi  ,langer,  verwachsener  Mensch*,  schwed.  slapp  ,arm,  untätig';  ^
mit  idg.  -p-:  aisl.  slafask  ,  erschlaffen*  und  —  von  der  Vorstellung  - herabhängenden  Schleimes  aus  —  wohl  auch  isl.  slafra  , geifern',  mengl. slaveren,  engl,  slave?-  ds.,  isl.  slevja  f.  , Geifer*,  norw.  slevjen  , schleimig, kotig';  norw.  slabbe,  schwed.  slabba  , sudeln',  mndl.  slabben  , besudeln, schlürfen',  nhd.  schlappen  (auch  ,geifern*),  mengl.  slabben  ,sich  im  Kot wälzen',  nhd.  (ndd.)  schlappern,  schlabbern,  schwed.  dial.  slabb  , Schlamm- wasser*, engl.  dial.  slab  ,schleimig,  schlüpfrig',  Subst.  , Schlammpfütze' ;
lit.    slobstü,    slöbti   ,  seh  wach    werden*,   lit.    iem.    släbnas,    ostlit.    sldbnas , schwach',  lett.  släbet  , zusammenfallen'  (von  einer  Geschwulst);
aksl.  slab^  usw.  , schwach'.
Nasaliert  lemh(h)-:
Ai.    rdmbate,    lambate    ,hängt   herab,   hängt   sich   an',    lambana-   ,herab- hängend',  n.  ,herabhängender  Schmuck,  Phlegma';
lat.  limbu
=== leaf 317 (printed ~ 661 ) ===
pa,  slapp  , entfallen,  entgleiten'  (*slemp-),  Kaus.  sleppa  {*slampian) ]'  ,  fahren  lassen',  engl.  dial.  slemp  , aus  weichen,  wegschleichen,  sich  herab- senken'; von  einer  Wurzelf.  auf  germ.  h  (vgl.  gr.  leficpog  , Schleim,  Rotz'); mnd.  mhd.  slam  (-mm-),  nhd.  Schlamm  (*slamba-),  spätmhd.  slemmen .schlemmen',  norw.  slemba  f.  , Schlampe',  slemha  ,klatschen',  isl.  ,baumeln'; ferner  vielleicht  die  Gruppe  von  mhd.  slimp  (-mb-),  slim  {-mm-)  , schief, schräg'  u.  dgl. ;  vielleicht  zu  lett.  sllps  aus  *slimpas  , schräg,  steil',  lit. nu-sUmpa  , entschlüpft'.
WP.  II  431  ff.,  WH.  I  738 ff.,  802  f.,  Trautmann  270.
leg-  ,tröpfeln,  sickern,  zergehen'. •  Arm.  Ii6  , Sumpf  (*legia)j
air.  legaim  ,löse  mich  auf,  zergehe,  schmelze',  fo-llega  ,(die  Tinte)  läuft aus*,  dl-leg-  (3.  Sg.  do-lega)  ,zerstören,  vernichten',  dllgend  , Vernichtung', mcymr.  dilein  (*de-leg-ni-)  ds.,  dileith  ds.,  cymr.  llaith,  bret.  leiz  (*lekto-) , feucht',  cymr.  dad-leithio  ,schmelzen',  air.  lecht  ,Tod',  cymr.  llaith  ,letum, caedes,  nex*  als  ,*Auflösung',  lleas  ,Tod'  (*leg-astu-)  ]  vielleicht  auch  als Kaus.  air.  do-luigim  {Hogeio)    ,lasse   nach,  verzeihe',  dilgud  ,Verzeihung';
aisl.  lehr  ,leck',  leki  m.  ,Leck',  ags.  hlec  (mit  falschem  h)  ,leck',  nhd. (eigentlich  ndd.)  Lech,  Adj.  lech  und  (ndd.)  leck,  mnd.  Iah,  aisl.  leka  stark.  V. ,das  Wasser  durchlassen',  mnd.  leken  ds.,  ahd.  ze(r)lechen  , zerlechzt,  leck', mhd.  lechen  , Flüssigkeit  durchlassen,  vor  Trockenheit  Risse  bekommen, verschmachten'  {lechezen  ,austrocknen',  eigentlich  ,ausrinnen',  nhd.  lechzen); Kaus.  Hakjan  in  ags.  leccan  , benetzen',  mnd.  lecken  , seihen',  mhd.  lecke
```


## [2026-09-06T22:58:09.803Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nd=open('POK_02.txt',encoding='utf-8',errors='replace').read()\npg=d.split('\\f')\nfor i in (319,320,321):\n    print('=== leaf',i,'===')\n    print(pg[i][:2200])\nEOF",
 "description": "Pokorny leaves 319-321"
}
```


### [2026-09-06T22:58:12.092Z] TOOL RESULT

```
=== leaf 319 ===
aimm  ,verberge' ;  air.  fo-lach  n.  , Versteck',  cymr.  bret.  go-lo  ds., o-all.  logan  Akk.  Sg.  ,Grab';  nasaliert  und  in  Abtönung  zu  slav.  l§gq Avahrscheinlich  air.  im-fo-lngai  ,bewirkt',  in-loing  , vereinigt'  =  mcymr. ellivng,  ncymr.  gollwng  ,to  let  go,  to  drop' ;  über  air.  lese  s.  unten;  dehn- stufig gall.-rom.  liga  {Hegha)  ,  Ablagerung' ;
hierher  sehr  wahrscheinlich  air.  lese  ,piger',  cymr.  llesg  ,infirmus,  langu- idusS  Grundf.  Hegzgho-  aus  Hegh-sko-]
wahrscheinlich  als  ,sich  legen' :  ahd.  lescan,  irlescan,  as.  lesJcan  ^erlöschen, löschen''  (die  trans.  Bed.  muß  dann  sekundär  sein);
got.  ligan  fliegen'  (Neubildung);  altes  t-Präs.  ags.  licgan,  afries.  lidza, as.  liggian,  ags.  licgan,  ahd.  ligen,  licJcen,  ,liegen'  (liggiu  =  abg.  lezo), Kaus.  got.  lagjan  , legen'  (==  abg.  loHti),  ahd.  leg(g)en,  as.  leggian,  afries. ledza,  ags.  lecgan,  aisl.  leggja  ds. ;  got.  ligrs  , Lager',  ahd.  as.  legar  n.  ds. ; aisl.  lag  n.  ,Lage,  Stellung',  PL  Igg  »Gesetz,  staatliche  Gemeinschaft'; ags,  ge-lxg  .Fläche' ;  aus  dem  Urnord.  ags.  lagu,  engl,  law  mnd.  lach , Lager';  as.  aldar-lagu  PL  n.  ,die  bestimmte  Lebenszeit',  gi-lagu  n.  PL , Bestimmung,  Schicksal^  Los'  (:  gr.  loxog)]  postverbal  sind  erlqg  N.  PL , Schicksal',  as.  orlag,  orleg  ,ds.',  ags.  orlceg  n.,  ahd.  urlag  m.  ds. ;  mhd. urlage  , Schicksal'  Krieg'  (letztere  Bed.  wohl  von  ahd.  urliugi,  mncl.  orloge herstammend,  s.  leugh-)]  ahd.  lehter  , Gebärmutter,  Nachgeburt'  (:  gr.  Xsy.- TQOv)f  aisl.  lätr  (*logh-tro-)  n.  , Lagerstelle  von  Tieren^;  dehnstufig  aisl. lag  ahd.  läga  ,Lage'  (:  lit.  pa-legys),  mit  Abtönung  ags.  afries.  log  n.  , Platz', lögian  ,disponere,   anordnen',   ahd.  luog  , Höhle,   Lager',   aisl.   legi  ,Ruhe';
über  ahd.  lescan  s.  oben;
lit.  pa-Ugys  , Bettlägerigkeit' ;
abg.  le£g  (=  ahd.  liggiu),  le^ati  {Hegeti)  ,liegen',  nasaliert  legq,  leUi ,sich  legen',  Kausat.  loziti  {=  got.  lagjan)  ,legen',  Iter.  Ugati  ,sich  legen*, Iter.  vz  lagati  , einlegen'  usw. ;  loze  , Lager,  Gebärmutter',
=== leaf 320 ===
sicher  ob  hierher  aksl.  loza  , Weinrebe,  Schößling',  serb.  Ibza  ds. usw.  (*hga)',  s.  auch  unter  log-  ,Rute,  Gerte'.
WP.  II  378,  442,  WH.  I  766,  Trautmann  153,  Jokl  L.-k.  ü.  203  ff.^ Machek  Recherches  25  ff.
2.  legh-  :  l9gh-  ,am  Boden  kriechen,  niedrig'.
Aisl.  lägr  ,niedrig'  (daraus  engl,  low)^  mhd.  Icßge  , flach',  nd.  lagt , niedrig' ;
lett.  l^zns  jflach',  lezet,  le^dt  , rutschen',  lit.  llkstas  ,flach',  lüo£as  , Nieder- beugen des  Getreides',  jünger  loSl  ds. ;  apr.  Ilse  , kriecht';
slav.  (abg.  usw.)  Uzq,  Usti  , kriechen,  schreiten,  steigen',  zu  russ.  lazina , Gereut',  skr.  läz  , Steig'  usw.
Ist  legh-  eine  Variante  von  legh-  , liegen'?
WF.  II  425  f.,  Trautmann  161.
leg^h-  jleicht  in  Bewegung  und  Gewicht',  verbal  ,sich  leicht,  flink  bewegen', nasaliert  lengY^h-\  leng^Aho-  , leicht,  flink';  Ing^b-ro-  ds.
1.  Ai.  laghü-,  ved.  raghü-  , rasch,  leicht,  gering',  Kompar.  läghlgams-, Superl.  Idghistha- ;  av.  ragu-,  i.  rdvl  , flink' ;  Kompar.  rdujyö,  .  Superl. rdnjiUa-  (vom  Stamme  *leng^h-)'j
schwundstufig  ai.  fhdnt-  , schwach,  klein'  (,*leicht');  av.  rdnjaiti,  r9nja- yeiti  , macht  leicht,  flink,  läßt  sich  bewegen',  ai.  rdmhate,  rdidghati,  Idraghati , rinnt,  eilt,  springt  auf,  springt  über';
gr.  ilaxvg  , gering',  Kompar.  iXdaocjv,  att.  iXdTTiov  (mit  sekundärem  a, s.  Schwyzer  Gr.  Gr.  1,  538  und  Anm.  4),  Superl.  ild^Laroq  {ela%vQ  aus idg.  Heg^hü-,  wie  slav.  lhg^k^  und  kelt.  *lag-\  ai.  laghü-  vielleicht  ebenso oder  hochstufig  wie  lat.  levis)]  slaq)o6g  ,leicht,  flink'  (wohl  aus  Hi^gVirös =  ahd.  lungar)]  nach  Schwyzer  Gr.  Gr.  1,  302  jedoch  kontaminiert  aus *klaxq6g  (=  ahd.  lungar)  und  *iXaq)6g  (aus  *-yfog  =  lit.  lengvas)]  viel- leicht ion.  XcDcpäv  ,sich  erholen,  ausruhen,  nachlassen,  trans.  erleichtern, entlassen,  befreien';
illyr.  lemhus  {Heng^ho-s)  , leichtes  Fahrzeug',  daraus  gr.  Is^ißog,  lat. lembus  ds. ;  oberital.  FIN  Lamhrits  (:  iXacpQÖg).  Krabe,  Gymnasium  59 (1952),  79;
lat.  levis  , leicht,  schnell,  leise'  (beruht  auf  dem  f.  
=== leaf 321 ===
 >^achahmuug  der  p  :  ^-Reduplikation),  air.  Uimm,  cymr.  usw.  llam  , Sprung' (*lng-smen-) ;
got.  leihts,  ags.  leoht,  aisl.  Ze^^r,  ahd.  llht(i)  , leicht',  nndl.  licht  n.  ,Nach- o-eburt'  {Hinxta-,  idg.  ^leng^h-to-)  ]  as.  lungo7\  ahd.  lungar  ,schnell',  ags. lungre  Adv.  , schnell,  bald'  (Hi^g^hro-,  s.  oben):  ahd.  gilingan  , vonstatten irehen,  Erfolg  haben,  gelingen*,  mhd.  lingen  ,vorwärtskommen' ;
lit.  leügvas,  lengvüs,  lett.  liegs  , leicht' ;
aksl.  lhg^k^  {Hgg^hu-,  s.  oben)  ,leicht*,  hgota  , Leichtigkeit',  aksl.  {je) Ibze  ,es  ist  erlaubt*  (Dat.  Sg.  zu  hga),  po-hdza,  po-hza  , Nutzen',  russ. Ibzja,  alt  hz§  ,es  ist  möglich,  man  darf,  neben  hga,  ds.  (usw.).
2.  Hierher  auch  Bezeichnungen  der  Lunge  (leichter  als  die  übrigen Fleischteile,  schwimmt  im  Wasser  oben):  ahd.  lungün  FL,  ags.  hingen,  anord. lunga  n.  , Lunge',  engl,  lights  , Tierlungen',  russ.  legJcoje  ,Lunge';  daher  auch arm.  lanjJt  , Brust*  (älter  ,*Lunge' ;  Hng'^hio-).
WP.  II  426  f.,  WH.  I  788  f.,   Trautmann  158  f.,  Kuiper  Nasalpräs.   143.
1.  lei-,  lek-  , biegen',  s.  oben  S.  307  ff.  unter  elei-.
2.  lei-    (aus    '*el-ei-)    , eingehen,    abnehmen,    schwinden;    mager,    schlank';
leibho-  , schwach',  lei-no-  ,matt*,  lei-ro-  , schlank*,  loi-si-s  , weniger*.
a.  Gr.  Xlva(.iaL'  tQSJtoiiaL  Hes.,  Xid^of-iai  , weiche  aus,  sinke  hin',  Xsigög (handschr.  leiQwg)'  b  la%vög  y,al  d)XQ6g  Hes.  (=  lit.  lellas),  Xifxög  m. , Hunger',  loii^iög  , Seuche,  Pest*;  Xivd-aagycog  ,von  zartem  Fleisch';
mir.  lian  (*lei-no-)  , sanft* ;  leine  f.  ,Hemd'  (,*weiches  Untergewand');
mhd.  Vtn  ,lau,  matt',  ahd.  Lino  PN,  nid.  lenig  , geschmeidig',  aisl.  linr ,zart,  weich,  schwach' ;  lina  ,lindern,  nachlassen' ;
got.  af-linnan  , ablassen,  fortgehen',  aisl.  Unna  , aufhören  lassen,  hemmen', ags.  Unnan  ,aufhören',  ahd.  hi-linnan  , weichen,  aufhören',  mit  -nn-  aus  -nu-]
aisl.  Ix  n.  (*laiwa-)  , Schade,  Unglück,  Betrug',  ahd.  Gen.  lewes  , leider', ags.  Ixw  ,Verstümmelung' ;  ags.  as.  lef  , seh  wach'  (*lei-bho-) ;
aus
```


## [2026-09-06T22:58:23.987Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nd=open('POK_03.txt',encoding='utf-8',errors='replace').read()\npg=d.split('\\f')\nprint('leaves',len(pg))\nfor i,p in enumerate(pg):\n    if 'layyaCco' in p or 'schlaff' in p and 'lag' in p:\n        pass\n# find the page containing (s)leg-\nfor i,p in enumerate(pg):\n    if re.search(r'l[eè]g-\\s*,?\\s*schlaff|schlaff  sein', p):\n        print('candidate leaf',i)\nEOF\ngrep -n \"λαγγ\\|layyd\\|lagga\\|laggazo\\|schlaff  sein\" POK_03.txt | head",
 "description": "Find Pokorny slēg-"
}
```


### [2026-09-06T22:58:25.753Z] TOOL RESULT

```
leaves 430
candidate leaf 199
candidate leaf 203
2617:Aisl.  slag  n.  , Nässe  (von  Regen)',  sleginn  ,benetzt',  norw.  slagen  , feucht', -schwed.  slaga  , Sumpf;  mnd.  slagge  ^schlackiges,  regnerisches  Wetter^, schwed.  slagga-väder  ds. ;  nhd.  dial.  slaclc  ,Schneequatsch';  nd.  slack  ,große und  schwere  Tropfen',  slackern  ,verschütten,  sudeln',  besleckern  ,beklecken'; ablaut.  ags.  sloh  , Morast^,  mnd.  slöch  ds. ;
2709:Nd.   slük   ,schlaff*,   ndl.    sluih  ,mager,   hager,   glatt*,   engl,   slouch  ^] Kopf  hängen,  träge  und  nachlässig  gehen';  aisl.  slohinn  ,erloschen*,  fiWi , erlöschen,  sterben*;  slekkva  ,löschen,  töten^;   norw.   sloka  ,faul  sein*, slokeren  ,schlaff  sein,   schlottern*,   mit   kk:  slukkern  ds.   (nhd.   Schluckt^ slukk   ,traurig',   slokh  ,schlaff,   schwach',  norw.   slauk   ,schlaffer   Men8< slauka   ,sich   schleppen',   ags.   sleac  ,schlaff';   ohne  s-:   aisl.   loka  ,scl herabhängen    lassen',    norw.    lukr,    lugr   ,lose,   schlotternd';    daneben  mit expressiver   Media   geminata   norw.    schwed.   slugga   ,sch werfällig  gehj (engl,  slug,  slug-gish  ,schläfrig,  träge'  ist  skand.  Lw.),  mnd.   luggich vermutlich  lit.  slügstu,  slügau,  slügti  , abnehmen,  kleiner  werden*.
```


## [2026-09-06T22:58:40.585Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HJB shraub/lal ===\"; grep -n -i \"shraub\\|shrob\\|LOLL\\|Loll\" HJB.txt | head -10\necho \"=== HJB lal ===\"; grep -n -i \"\\blal\\b\" HJB.txt | head -10\necho \"=== HRN Tulpe/lala ===\"; grep -n -i \"Tulpe\\|lâla\\|lala 'Tul\" HRN.txt | head -10\necho \"=== HUB Tulpe ===\"; grep -n -i \"Tulpe\" HUB.txt | head -10\necho \"=== LKT lal/laqlaq ===\"; grep -n -i \"laklak\\|laqlaq\\|leylek\\|Storch\" LKT.txt | head -10\necho \"=== TTS leylek ===\"; grep -n -i \"leilek\\|leylek\\|laklak\" TTS.txt 2>/dev/null | head",
 "description": "Grep HJB, HRN, HUB, LKT"
}
```


### [2026-09-06T22:58:40.700Z] TOOL RESULT

```
=== HJB shraub/lal ===
2327:[1832.— "The  lollah,  known  to  many  by the  name  of  haver-dewatt,  is  a  beautiful little  creature,  about  one-third  the  size  of a  hedge-sparrow." — Mrs  Meer  UoMan  Ali, Obaervat.  ii.  54.]
3261:The  lolling   couch,   the   joys  of   bottled beer."
6684:1768. — "  II  est  k  remarguer  qU'apr^  mon deport  d'Ayder  Abad,  Salabet  Zingue  a nomm€  un  PkosdcWy  ou  Gouvemeur,  pour lea  quatrea  Cerkan."— ATAiMwrc,  by  Bussy, in  Lettret  de  MM,  de  Busay^  de  Lolly  et autre*,  Paris,  1766,  p.  24.
8543:DELOLL.
8554:DELOLL,  8.  A  broker;  H.  from Ar.  dalldlj  the  literal  meaning  being one  who  directs  (the  buyer  ana  seller to  their  bargain).  In  Egypt  the  word is  now  also  used  in  particular  for  a broker  of  old  clothes  and  the  like,  as  de- scribed by  Lane  below.  (See  also  under NEELAM.)
8556:1684.— "Five  Delolls,  or  Brokers,  of Decoa,  after  they  had  been  with  me  went to  Mr.  Beard's  chamber.  .  .  ."-^Hedges, niary,  July  25  ;  [Hak.  Soc.  i.  152].
12926:[c.  1780. — "To  every  plate  are  set  down two  glasses  ;  one  pyramidal  (like  hobnob glasses  in  England)  for  Loll  Shnib  {seilicel, claret) ;  the  other  a  common  sized  wineglass for  whatever  beverage  is  most  agreeable." — Diary  of  Mrs.  Fay,  in  Busteed,  Echoes,  128.]
17286:[1772.— "PykArs  {Dellols  (see  DELOLL) and  Gomastahs)  are  a  chain  of  agents through  whose  hands  the  articles  of  mer- chandize pass  from  the  loom  of  the  manu- facturer, or  the  store-house  of  the  cultivator, to  the  public  merchant,  or  exporter." — Verelst,  View  of  Bengal,  Gloss,  s.v. J
19651:1759. — "De  quinze  mille  Cipayes  dont I'ami^e  est  cens^e  compost,  j*en  compte ^  peu  pr^s  huit  cens  sur  la  route  de  Pondi- chery,  chaiig^  de  sucre  et  de  poivre  et  autres marchandises,  quant  aux  Coiilis,  ils  sont tous  employ^  pourle  mftme  objet." — Letter of  Lolly  to  the  Oovemor  of  Pondicherry,  in Cambridge's  Account,  p.  150.
19947:*  draught,'  it  is  uot  a  word  now  speci- ally in  Anglo-Indian  use.  The  Arabic seems  to  have  entered  Europe  by several  different  doors.  Thus  in Italian  and  French  we  have  mrbetto and  sorbet,  which  probably  came  direct from  the  Levantme  or  Turkish  form shurbat  or  shcrbat;  in  Sp.  and  Port, we  have  ocarahe,  cucarabe  (ash-shardby the  standard  Ar.  thardby  *wine  or  any beverage '),  and  xaroM,  and  from  these forms  probably  Ital.  sciroppoy  nroppOy with  md  French  ynerop  and  mod. French  strop;  also  English  syrup,  and more  directly  from  the  Snanish,  ^rub. Mod.  Span,  again  gets,  oy  reflection from  Fi'ench  or  Italian,  sorbete  and strop  (see  Dozy,  17,  and  Marcel  Devic, 8.  v.  strop).  Our  sherbet  looks  as  if  it had  been  imported  direct  from  the Le\'ant.  The  form  shrdb  is  applied in  India  to  all  wines  and  spirits  and prepared  drinks,  e,g.  FoTt-skravby BheTTY-shraub,  Lakll-Baraab,  Brandy- shratii,  Beer-shraub.
=== HJB lal ===
12445:rks  01  its  introduction  in  place  of red  uniform  which  cave  the British  soldier  the  name  of  *^Lal  Ooortee Wallahs.'']
19724:b.  Savandrug ;  a  remarkable  double hill-fort  in  Mysore,  standing  on  a two-tonped  bare  rock  of  granite,  which was  taken  bv  Lord  Comwallis's  anuv in  1791  (LaL  12"  550.  [Wilks  (HU. Sketches,  Madras  reprint,  i.  228,  ii. 232)  calls  it  Savendy  Droog,  and  Saren- droog.]
25732:AdxKOty  4996 Laknau,  524a Lakravagh,  524a LaUchia,  5136 Lal]a,5016 Lall-shraub,       5016,
=== HRN Tulpe/lala ===
=== HUB Tulpe ===
=== LKT lal/laqlaq ===
3016:1294.  Ar.  laklak:
3017:'Storch'  [onomatopoetische  Bildung  nach dem  Klappern  des  Schnabels,  ebenso  wie ass.  lakalaka  Del  HWB  885  a],  ebenso tk.  leklek,  vulg.  lejlek  [mit  Erweichung des  Gutturals  wie  in  Beg  >  bej,  s.  hier Nr.  282]  'Storch,  Kranich';  hieraus  rum. liliac  'Fledermaus';  serb.  lelek,  lilak, Cech.  lelek,  klruss.  lelek,  russ.  leklek 'Storch'.    [Gorjajew  184.
3251:'Gebunden'  [pari.  pass.  von  rahata 'binden,  fromm  sein'];  hieraus  frz. marabout  'Einsiedler',  ein  heiligmäßiger Mann,  der  nach  seinem  Tode  in  einer Kapelle  begraben  wird  und  dort  Ver- ehrung findet;  das  Wort  wird  auch fälschlich  auf  diese  Grabkapelle  selbst bezogen ;  sp.  morabito,  pg.  marabuto, rum.  marabut  'Einsiedler',  siz.  mura- bitu  'Abstinenzler';  engl,  maraboot; ferner  wegen  des  ernsthatten  Aussehens des  Vogels  sp.  marabA  'Riesenstorch vom  Senes^al  oder  aus  Indien,  Lepto- ptilus  argaia  Gray.',  dtsch.  Marabu,  engl. marabou.  —  Dagegen  muß  sp.  morabito 'Seemann'  auf  ar.  muräkibi  'dass.'  zu- rückgehen. [Devic  DEt  157.  Eguilaz  443. GrSVociSic  242.
=== TTS leylek ===
```


## [2026-09-06T22:58:51.255Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"Lall\\|LALL\\|lal shardb\\|lal  sharab\\|LOLL-SHRAUB\\|LOLL SHRAUB\" HJB.txt | head -20\necho \"---\"\ngrep -n -i \"claret\" HJB.txt | head -20",
 "description": "Find Hobson-Jobson lall-shraub entry"
}
```


### [2026-09-06T22:58:51.318Z] TOOL RESULT

```
584:De  Bussy,  Lettres  de  M.,  de  Lally  et  autres.
1845:Moore,  Lalla  Bookh.
2301:c.  1780. — ".  .  .  .  having  detected  various frauds  in  the  management  of  the  Amuldar or  renter  .  .  .  .  (M.  Lally)  paid  him  40,000 rupees."— <Vot«,  iii.  496  (ed.  1808).
2694:1792.— "The  officer  (of  Tippoo's  troops) who  led,  on  being  challenged  in  Moon answered  {Aaari  que  logiu\  *  We  belong  to the  advance  —the  title  of  Lally's  brig^e, supposing  the  people  he  saw  to  be  their  own Europeans,  whose  uniform  also  is  red ;  but soon  discovering  his  mistake  the  com- mandant called  out  (Feringhy  Banchoot  I— chelow)  *  they  are  the  rascally  English ! Make  off ' ;  in  which  he  set  the  corps  a ready  example,"— Dirom't  Narrative,  147.
3682:The  phrase  is  in  use  among  natives, we  know  not  whether  originating  with them,  or  adopted  from  the  usage  of the  foreigner.  But  Kala  Odmi  'black man,'  is  often  used  by  them  in  speak- ing to  Europeans  of  other  natives.  A case  in  point  is  perhaps  worth  record* ing.  A  statue  of  Lord  William Bentinck,  on  foot,  and  in  bronze, stands  in  front  of  the  Calcutta  Town ELall.  Many  years  ago  a  native  ofiELcer, returning  from  duty  at  Calcutta  to Barracbpore,  where  his  regiment  was, reportect  himself  to  his  adjutant  ^from wnom  we  had  the  story  in  later  aays).
7059:"...  Lightly  latticed  in With  odoriferous  woods  of  Comorin.'* Lalla  Rookkf  Mokanna.
10388:chime." — Lalla  Kookh,  Mokanna, Tremendous  sham  poetry !
10925:HALALLCUR.
12902:LALLA.
12925:LALL-SHBAXJB,  s.  Englishman's Hind.  Idl-shardby  *red  wine.'  The universal  name  of  claret  in  India.
12927:LALLA,  s.  P.— H.  2(2^.  In  Persia this  word  seems  to  be  used  for  a  kind of  domestic  tutor ;  now  for  a  male nurse,  or  as  he  would  be  called  in India,  ^child's  bearer.'  In  N.  India it  is  usually  applied  to  a  native  clerk writing  the  vernacular,  or  to  a  respect-
19494:1758.— "The  Captain  of  the  troop  .  .  . made  a  cut  at  his  head  with  a  spymetar which  Mr.  Lally  parried  with  his  stick, and  a  Coffree  (Galx«r)  servant  who  attend him  shot  the  I^njerine  dead  with  a  pistol. '* —OriM,  i.  328.
25732:AdxKOty  4996 Laknau,  524a Lakravagh,  524a LaUchia,  5136 Lal]a,5016 Lall-shraub,       5016,
---
83:silver  tankard,  which,  after  drinking  claret  and  sherry,  he  threw  in,  and
12925:LALL-SHBAXJB,  s.  Englishman's Hind.  Idl-shardby  *red  wine.'  The universal  name  of  claret  in  India.
12926:[c.  1780. — "To  every  plate  are  set  down two  glasses  ;  one  pyramidal  (like  hobnob glasses  in  England)  for  Loll  Shnib  {seilicel, claret) ;  the  other  a  common  sized  wineglass for  whatever  beverage  is  most  agreeable." — Diary  of  Mrs.  Fay,  in  Busteed,  Echoes,  128.]
16401:1848. —  "Constant  dinners,  tiffins,  pale ale,  and  claret,  the  prodigious  labour  of cutchery,  and  the  refreshment  of  brandy pawnee,  which  he  was  forced  to  take  there, had  this  effect  upon  Waterloo  Sedley." — Vaniiy  Fair,  ed.  1867,  ii.  258.
19787:SHADE  (TABLE-SHADE. WALL-SHADE),  &  A  glass  gaard to  protect  a  candle  or  simple  oil-lamp from  the  wind.  The  oldest  form,  in use  at  the  beginning  of  the  last century,  was  a  tall  glass  cylinder which  stood  on  the  table,  the  candle- stick and  candle  being  placed  bodily within  in.  In  later  days  the  universal form  has  been  that  of  an  inverted dome  fitting  into  the  candlestick, which  has  an  annular  socket  to  receive it  The  walUskade  is  a  bracket  at- tached to  the  wall,  bearing  a  candle or  cocoa-nut  oil  lamp,  protected  by such  a  shade.  In  the  wine-drinking days  of  the  earlier  part  of  last  century it  was  sometimes  the  subject  of  a challenge,  or  forfeit,  for  a  man  to empty  a  wall-shade  filled  with  claret. The  second  quotation  below  fives  a notable  description  of  a  captain^  outfit when  taking  the  field  in  the  18th century.
20431:1782.— "On  Monday  the  29th  inst  will be  sold  by  auction  ...  a  hay  Buggy Horse,  a  Buggy  and  Harness  .  .  .  some  cut Diamonds,  a  quantity  of  China  Sucarvandy ...  a  (quantity  of  the  best  DaniSi  Claret .  .  .  dehverable  at  Serampore;  two  Slave Girls  about  6  years  old  ;  and  a  great  varieiv of  other  articles."- /jufta  Gazette,  July  27.  "
22043:\xnt With  wholsome  wares:  and  as  the  con- duits ran With  claret  at  the  Coronation, So  let  your  channels  flow  with  single  tiff, For  John  I  hope  is  crown'd.  ...
```


## [2026-09-06T22:58:59.704Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON لال ===\"; sed -n '38100,38115p' MON_part2.txt\necho \"=== MON لقلق ===\"; sed -n '39940,39960p' MON_part2.txt\necho \"=== MON لکلکه ===\"; sed -n '40080,40092p' MON_part2.txt\necho \"=== MON لاله ===\"; grep -n \"لاله:\" MON_part2.txt | head",
 "description": "Mo'in entries context"
}
```


### [2026-09-06T22:58:59.801Z] TOOL RESULT

```
=== MON لال ===
(ل.) 

لال: ۱۱ (ص.) آنکه کلمات را نامفهوم ادا 
کند و مکرر سازد؛ الکن. لال پتی: (عم.) 
آنکه نتواند بعض حروف را از مخرج خود 
ادا کند؛ الکن. 

۳ ۱2۱ اقس. لاله» آلاله» لعل» معر.] (ص.) 
سرخ؛ احمر. (4) (زه.) لعل. 

لالا: قاةا [- لله] ((.) غلام بنده» خدمتکار. 
لالای چشم: ( کن.) مردمکث چشم (تشییه به 
غلام سیاه). مربی بز رت زادگان. 

لالا: 125 (.) خفتن در زبان اطفال (- لالا 

=== MON لقلق ===

ات ۱0۳۱۸۱۵ [ع. . لقطه | (.) آنجه 
بر چیه و بر داشته شود (خوشه و جر آن): 
ج. لقطات. بجه‌ای که او را از سر راه بر داشته 
لقلقو : تناها (ص.) (عم.) آنکه از شدزتا 
پیری» ضعف یا ناخوشی, اندامش لرزان 
باشد و نتواند تعادل خود را حفظ کند. 
لقلقه: (م)«هاها (ع. لقلقة] (مصل.) 
سخت آواز کردن لکلکك (غم.) (.) اواز 
لکلک (غم.) ) آوازی همراه با جنش و 
اضطرات. فصاحت عاری از بلاعت. لقلقه 


۵ ۵ ۱ 
73 (زبان): گرفتگی زبان. (ف.) 
ببهوده گویی. فصاحتی بی‌بلاغت (لذ.) 
لشمه: (ه-)مها [ع. لقمه ]| (.) آنجه از 
خوردنی که در یک وهله در دهان نهند و 
جوند؛ نواله» تکه. خوراکك» غذا. لقمه 
حرام: طعامی که از راه حرام بتلافیت. | سل 
دشنامی است که معمولا به فرزندانی دهند 
=== MON لکلکه ===
بر اثر ضر به. 
لی زدد: ۱-0 (مص‌ل.) لکد زدن 
سو ۵. : (عم.) بت بررداشتن میوهه برابر رسیدان 


و پخته شدن قسمتی از میوه به رنگ دیگر 
در آمدن. لک زدن دل کسی برای چیزی: 
لعلی؛: ۱:۸۲ [- لکلکه) (.) سجن بهوده؛ 
گفتار هرزه. 

لکلیک: ۱۸۸۱۸۶ (- لکلکك - معر. لقلق | (.) 
(جاد.) (امر.) پر نده‌ای است از راستة پابلندان 
که دارای ۵ گونه است و در ارویا و آسیا و 
=== MON لاله ===
2197:غلاله: (ه‌هاقاهر [ع. غلاله ] (۱.) بالشجه‌ای 
24685:کلاله: (-)۵۱2۱2! [ع. کلالة] (.) کسی که نه 
24702:کلاله: (0۱21:)۵ [- گلاله» قس. کلال؛ 
34250:گلاله: (م«اقامي | - کلاله - غلاله | (ا.) 
34254:کلاله: («اقاهع [ع. (معر.) غلاله ] (ا.) 
38122:لاله: (-):۱2 (- آلاله - قس. لال» سرخ|
```


## [2026-09-06T22:59:30.899Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npdftoppm -f 302 -l 302 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg302 && echo ok; ls site/pages/302.jpg 2>/dev/null",
 "description": "Render dictionary page 302"
}
```


### [2026-09-06T22:59:33.018Z] TOOL RESULT

```
ok
site/pages/302.jpg
```


## [2026-09-06T22:59:36.117Z] TOOL CALL #56: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg302.png"
}
```


### [2026-09-06T22:59:36.462Z] TOOL RESULT

```

```


## [2026-09-06T22:59:36.458Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-06T23:00:02.007Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nS=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad\npdftoppm -f 302 -l 302 -r 600 -png -singlefile EtymologicalDictionary-persian-english.pdf $S/pg302hi\npython3 - <<'EOF'\nfrom PIL import Image\nS='/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad'\nim=Image.open(S+'/pg302hi.png'); print(im.size)\nw,h=im.size\n# Sanskrit node approx at x 0.22-0.40, y 0.47-0.52 of page\nim.crop((int(0.20*w),int(0.465*h),int(0.42*w),int(0.515*h))).save(S+'/crop_skt.png')\n# English node loll sharob approx x 0.60-0.80 y 0.36-0.40\nim.crop((int(0.58*w),int(0.365*h),int(0.80*w),int(0.400*h))).save(S+'/crop_loll.png')\nEOF\necho done",
 "description": "Crop regions from page 302"
}
```


### [2026-09-06T23:00:06.419Z] TOOL RESULT

```
(5100, 6600)
done
```


## [2026-09-06T23:00:09.016Z] TOOL CALL #58: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/crop_skt.png"
}
```


### [2026-09-06T23:00:09.031Z] TOOL RESULT

```

```


## [2026-09-06T23:00:13.230Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 - <<'EOF'\nfrom PIL import Image\nS='/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad'\nim=Image.open(S+'/pg302hi.png')\nw,h=im.size\nim.crop((int(0.20*w),int(0.505*h),int(0.42*w),int(0.560*h))).save(S+'/crop_skt2.png')\nim.crop((int(0.58*w),int(0.355*h),int(0.82*w),int(0.405*h))).save(S+'/crop_loll2.png')\nEOF\necho ok",
 "description": "Recrop"
}
```


### [2026-09-06T23:00:15.736Z] TOOL RESULT

```
ok
```


## [2026-09-06T23:00:19.626Z] TOOL CALL #60: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/crop_skt2.png"
}
```


### [2026-09-06T23:00:19.659Z] TOOL RESULT

```

```


## [2026-09-06T23:00:24.225Z] TOOL CALL #61: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/crop_loll2.png"
}
```


### [2026-09-06T23:00:24.239Z] TOOL RESULT

```

```


## [2026-09-06T23:00:28.282Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 - <<'EOF'\nfrom PIL import Image\nS='/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad'\nim=Image.open(S+'/pg302hi.png'); w,h=im.size\nim.crop((int(0.60*w),int(0.395*h),int(0.85*w),int(0.435*h))).save(S+'/crop_loll3.png')\nEOF\necho ok",
 "description": "Crop English node"
}
```


### [2026-09-06T23:00:30.253Z] TOOL RESULT

```
ok
```


## [2026-09-06T23:00:32.631Z] TOOL CALL #63: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/crop_loll3.png"
}
```


### [2026-09-06T23:00:32.642Z] TOOL RESULT

```

```


## [2026-09-06T23:00:40.434Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nmkdir -p data/verification/sources/refs/ocr/BOOK\ncp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg302.png data/verification/sources/refs/ocr/BOOK/302.png\nls -la data/verification/sources/refs/ocr/BOOK/302.png",
 "description": "Save page 302 image for audit"
}
```


### [2026-09-06T23:00:40.492Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 91158 Sep  6 19:00 data/verification/sources/refs/ocr/BOOK/302.png
```


## [2026-09-06T23:00:42.692Z] TOOL CALL #65: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B1%D9%86%D8%AC",
 "prompt": "Give the Persian etymology of رنج (ranj) 'pain, toil' — Middle Persian form, Proto-Iranian reconstruction, PIE root, and any cited sources (Cheung, Hasandust, MacKenzie). Also list related verb رنجیدن/رنجاندن."
}
```


### [2026-09-06T23:00:48.961Z] TOOL RESULT

```
# Persian Etymology of رنج (ranj)

Based on the Wiktionary content provided, here's what can be determined:

**Middle Persian Form:** The entry states the word is "Inherited from Middle Persian [script needed] (lnc /⁠ranǰ⁠/, 'toil')."

**Etymology Source:** MacKenzie's *A Concise Pahlavi Dictionary* (1971, page 70) is cited as a reference for the Middle Persian origin.

**Proto-Iranian & PIE Reconstruction:** The document does not provide Proto-Iranian reconstructions or Proto-Indo-European roots for this term.

**Related Verb:** While the page lists related terms like رنجبر (ranjbar, "toiler") and رنجور (ranjūr, "ill; afflicted"), it does not mention the verbs رنجیدن or رنجاندن.

**Citation:** D. N. MacKenzie's dictionary entry is the primary etymological source referenced in the article.

The document's etymological information is limited and does not extend to deeper Proto-Iranian or PIE-level analysis.
```


## [2026-09-06T23:00:52.486Z] TOOL CALL #66: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/laggazo",
 "prompt": "Is there an Ancient Greek entry λαγγάζω? Give its meaning and etymology."
}
```


## [2026-09-06T23:00:52.499Z] TOOL CALL #67: WebSearch

```json
{
 "query": "Akkadian laqlaqqu raqraqqu stork CAD onomatopoeic Aramaic laqlaqa"
}
```


### [2026-09-06T23:00:54.357Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-06T23:01:02.330Z] TOOL RESULT

```
Web search results for query: "Akkadian laqlaqqu raqraqqu stork CAD onomatopoeic Aramaic laqlaqa"

Links: [{"title":"لک‌لک - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%D9%84%DA%A9%E2%80%8C%D9%84%DA%A9"},{"title":"لقلق - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%D9%84%D9%82%D9%84%D9%82"},{"title":"BIBLICAL ANTHROPOLOGY: Akkadian Lexicon","url":"http://biblicalanthropology.blogspot.com/2017/10/akkadian-lexicon.html"},{"title":"Akkadian language","url":"https://en.wikipedia.org/wiki/Akkadian_language"},{"title":"Ninkarrak","url":"https://en.wikipedia.org/wiki/Ninkarrak"},{"title":"Akkadian literature","url":"https://en.wikipedia.org/wiki/Akkadian_literature"},{"title":"Filling the Gaps in Ancient Akkadian Texts: A Masked Language Modelling Approach","url":"https://arxiv.org/pdf/2109.04513"},{"title":"Genesis and Gilgamesh - Biblical Archaeology Society","url":"https://www.biblicalarchaeology.org/daily/ancient-cultures/genesis-and-gilgamesh/"},{"title":"Canaano-Akkadian language","url":"https://en.wikipedia.org/wiki/Canaano-Akkadian_language"}]

The search results provide relevant information about these terms. Here's what I found:

The Akkadian word laqlaqqu means "stork," and similar words appear in Arabic (laqlaq, "stork") and Assyrian Neo-Aramaic (laqlāqā, "stork").

Regarding raqraqqu, this is used onomatopoetically in Akkadian poetry to describe "the clatter of the stork", demonstrating that Akkadian employed alliterations and assonance using animal sounds to create poetic effects.

The word appears in the Chicago Assyrian Dictionary (CAD), as referenced in the search results. These terms are probably ultimately from Semitic origins, showing linguistic connections across multiple Semitic languages including Akkadian, Arabic, and Aramaic.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-06T23:01:07.992Z] TOOL CALL #68: WebFetch

```json
{
 "url": "https://logeion.uchicago.edu/%CE%BB%CE%B1%CE%B3%CE%B3%CE%AC%CE%B6%CF%89",
 "prompt": "Give the LSJ definition of λαγγάζω and λαγγεύω, and any etymology (relation to λαγαρός, *sleg-)."
}
```


## [2026-09-06T23:01:10.299Z] TOOL CALL #69: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%E0%A4%B0%E0%A4%9C%E0%A5%8D",
 "prompt": "Give the Sanskrit root रज्/रञ्ज् (raj/rañj): meanings of the passive rajyate, and etymology. Does any sense mean 'to be in pain' or 'to be agitated/disturbed'?"
}
```


### [2026-09-06T23:01:12.793Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-06T23:01:13.101Z] TOOL RESULT

```
I cannot provide the requested information because the web page content provided is empty (indicated by the dashes with no text between them).

To answer your question about the LSJ (Liddell-Scott-Jones Greek Lexicon) definitions of λαγγάζω and λαγγεύω, along with their etymology and relation to λαγαρός and the PIE root *sleg-, I would need access to:

1. The actual LSJ lexicon entries
2. Etymological sources discussing these terms
3. Relevant scholarly materials on their linguistic connections

If you can provide the specific lexicographic or scholarly sources containing these definitions and etymologies, I'd be happy to summarize them according to your guidelines.
```


## [2026-09-06T23:01:16.689Z] TOOL CALL #70: WebFetch

```json
{
 "url": "https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A1999.04.0057%3Aentry%3Dlagga%2Fzw",
 "prompt": "Give the LSJ entry for λαγγάζω and any neighbouring entries λαγγεύω, λαγαρός."
}
```


## [2026-09-06T23:01:17.631Z] TOOL CALL #71: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/rajyate",
 "prompt": "Sanskrit rajyate — meanings and root. If not present, say so."
}
```


### [2026-09-06T23:01:22.549Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-06T23:01:26.182Z] TOOL RESULT

```
# LSJ Entry: λαγγάζω and Related Terms

## λαγγάζω
This verb means "to slacken" (equivalent to ἐνδίδωμι). According to Photius, the form λαγγάζει means "he hesitates" (ὀκνεῖ). Hesychius provides additional glosses: λαγγεῖ means "he hesitates," while λαγγάσαι means "to escape" (περιφυγεῖν). The related term λαγγανώμενος describes someone "standing aside" or "being wrung out."

## λαγγαρεῖ
This related form signifies "he flees away" or "escapes" (ἀποδιδράσκει), per Hesychius.

## λαγγεύει
This variant means "he flees" (φεύγει), according to the same source.

The entry cites *Antiph.37* and references from Photius and Hesychius as primary sources for these definitions.
```


## [2026-09-06T23:01:31.153Z] TOOL CALL #72: WebFetch

```json
{
 "url": "https://www.sanskritdictionary.com/?q=rajyate",
 "prompt": "What does Sanskrit rajyate mean (Monier-Williams)? Give the senses and the root."
}
```


### [2026-09-06T23:01:33.169Z] TOOL RESULT

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-06T23:01:37.532Z] TOOL CALL #73: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%E0%A4%B0%E0%A4%9E%E0%A5%8D%E0%A4%9C%E0%A5%8D",
 "prompt": "Sanskrit रञ्ज् (rañj) — give the meanings (including the passive rajyate) and the etymology / PIE root."
}
```


## [2026-09-06T23:01:37.805Z] TOOL CALL #74: WebSearch

```json
{
 "query": "Monier-Williams rajyate \"to be dyed\" \"to be excited\" रज्यते meaning root ranj"
}
```


### [2026-09-06T23:01:43.170Z] TOOL RESULT

```
# Sanskrit Root रञ्ज् (rañj)

## Meanings

The root has two primary definitions:
1. "to redden"
2. "to dye or colour"

The passive form **rajyate** represents the present passive voice construction of this root.

## Etymology

The term derives from Proto-Indo-European **(s)reg-**, meaning "to dye." Related forms appear across language families, including Proto-Iranian *ra(n)ǰ-* and Persian *raxš* ("red"), as well as Ancient Greek *rhézō* ("to dye, paint").

This etymological connection demonstrates the root's consistent association with coloring and reddening across Indo-European languages, reflecting a shared ancestral meaning from thousands of years ago.
```


### [2026-09-06T23:01:49.771Z] TOOL RESULT

```
Web search results for query: "Monier-Williams rajyate "to be dyed" "to be excited" रज्यते meaning root ranj"

Links: [{"title":"Monier-Williams Sanskrit-English Dictionary --र","url":"https://sanskrit.inria.fr/MW/214.html"},{"title":"Raj, Raaj, Rāj: 15 definitions","url":"https://www.wisdomlib.org/definition/raj"},{"title":"Monier-Williams Sanskrit-English Dictionary","url":"http://cbeta.buddhism.org.hk/wm/172"},{"title":"Monier-Williams Sanskrit-English Dictionary -- r","url":"https://tuninst.net/SED-MW/download-prem/r.htm"},{"title":"Monier-Williams Sanskrit-English Dictionary -- s - tuninst.net","url":"http://www.tuninst.net/SED-MW/download-prem/s.htm"},{"title":"raj<!-- --> - Sanskrit Dictionary | Kosha.App (KST)","url":"https://kosha.sanskrit.today/word/sa/raj"},{"title":"Ranj, Rañj: 9 definitions","url":"https://www.wisdomlib.org/definition/ranj"},{"title":"Raj, Rāj, Raaj: 15 definitions","url":"https://www-wisdomlib-org.translate.goog/definition/raj?_x_tr_sl=en&_x_tr_tl=hi&_x_tr_hl=hi&_x_tr_pto=tc"},{"title":"Rañjayati - Sanatana Dharma Glossary | Shastra Deep","url":"https://www.shastradeep.com/glossary/ranjayati"}]

Based on the Monier-Williams Sanskrit-English Dictionary search results, here's what I found about rajyate and the root ranj:

## Root: Raj/Rañj

The root raj/rañj (classes 1 and 4, parasmaipada and atmanepada) means "to be dyed or coloured, to redden, grow red, glow" and also "to be affected or moved, be excited or glad, be charmed or delighted by."

## Rajyate (रज्यते)

Rajyate means "to be dyed or coloured, become red" and also "to be affected with any passion." This is the passive voice form (Ā. = Ātmanepada).

## Causal Forms and Extended Meanings

The causative forms (rajayati and rañjayati) mean "to dye, colour, paint, redden, illuminate" and also "to rejoice, charm, gratify, conciliate."

## Intensives and Etymology

The intensive forms (rārajīti, rārajyate, and rāraṅkti) mean "to be greatly excited, exult." The root has cognates in Greek meaning "to dye" and "dyer."

So the dual meanings you mentioned—both "to be dyed" (literal, referring to color) and "to be excited" (emotional/metaphorical)—are both well-established in the Monier-Williams dictionary for this root.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-06T23:02:05.331Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nd=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\ni=d.find('loll  shraub')\nprint(repr(d[i-3000:i+300])[:1500])\nEOF",
 "description": "Check Klein page marker near loll shraub"
}
```


### [2026-09-06T23:02:07.423Z] TOOL RESULT

```
"oin’,  fr.  ML.  *lumbea,  fern,  of *lumbeus,  adj.  used  as  a  noun,  fr.  L.  lumbus, ‘loin’.  See  lumbar  and  cp.  the  second  element  in sirloin.\nloir,  n.,  a  species  of  dormouse.  —  F.,  fr.  VL.  gll- rem,  corresponding  to  L.  glirem,  acc.  of  glis, ‘dormouse’,  which  is  cogn.  with  OI.  girih,  girikd, ‘mouse’,  Gk.  yaXsr),  ‘weasel,  polecat,  marten’. See  galea  and  cp.  lerot.\nLoiseleuria,  n.,  a  genus  of  plants,  the  Alpine  aza¬ lea  (bot.)  —  ModL.,  named  after  the  French  bo¬ tanist  J.  L.  A.  LoAe/ewr-Delongchamps  (1774- 1849).  For  the  ending  see  1st  suff.  -ia. loiter,  intr.  and  tr.  v.  —  ME.  loitren,  fr.  MDu. loteren,  ‘to  be  loose’  (whence  Du.  leuteren,  ‘to delay,  linger,  loiter’),  which  is  rel.  to  OE.  lod- dere,  ‘beggar',  ME.  lodder,  ‘good-for-nothing’, OHG.  lotar,  ‘empty,  vain’,  MHG.  loter,  ‘loose, vain,  frivolous’,  G.  Lotterbube,  ‘vagabond,  ras¬ cal',  OE.  lydre,  ‘base,  bad,  wicked'.  Seelither. Derivative:  loiter-er,  n.\nloka,  n.,  open  space,  universe,  world  (Hinduism). —  OI.  loktih,  lit.  ‘a  clear  place,  clearing’,  rel.  to lokdyati,  locayati,  ‘regards,  looks  at’,  fr.  I.-E. base  *leuq-,  ‘to  see,  behold’,  which  is  identical with  base  *leuq-,  ‘to  emit  light,  shine;  bright’. See  light,  ‘brightness’,  and  cp.  the  first  element in  lokapala.\nlokapala,  n.,  a  guardian  of  the  world,  prop,  one of  the  eight  deities  who  guard
```


## [2026-09-06T23:02:33.769Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== ARY لاله/لال/رنج ===\"; grep -n \"لاله\\|رنج\\b\\|لکلک\" incoming/ARY/ARY_pages.txt | head -12\necho \"=== AHD legwh ===\"; grep -n -i \"legwh\\|leguh\\|lengwh\\|elaphros\\|lungs.*light\" AHD_watkins1985.txt | head -10\necho \"=== LKT Rubin/lal ===\"; grep -n -i \"Rubin\\|Balas\\|balais\" LKT.txt | head -10\necho \"=== TAD leaf for لعل ===\"; python3 - <<'EOF'\nd=open('TAD_pages.txt',encoding='utf-8',errors='replace').read()\npg=d.split('\\f')\nprint('leaves',len(pg))\nfor i,p in enumerate(pg):\n    if 'لعل حجر' in p or 'فارسبي ‪ 2‬لال' in p or 'معنا أحمر' in p:\n        print('leaf',i)\nEOF",
 "description": "More reference greps"
}
```


### [2026-09-06T23:02:35.979Z] TOOL RESULT

```
=== ARY لاله/لال/رنج ===
1483:۴ ۲ آرنج آرنگ, آران :
1524:۴ معلی اين واژه در برخی زبان‌های رومانس: زند زبرین؛ استخوان آرنج.
2046:اوستی (0838716): لاله ,۸۷0۸ آلمانی (4۸ق058): وال۲۱
2324:این واژه با "آرنج " از یک واجریشه است. ۹
2343:یرنانی (0/65) 58 لاله
2880:کردی(شاید) (07821877): لاله ادن ساکسونی کهن (542:07 صضا0): ,87۸8۲0۸31
3839:ایتالیایی (لاله1): 00 ایرلندی کهن (87ل#/ 01.2): 80710 ,لاتا8ظ
7705:بلرچی (1ل۲لاله8): 87 ,026 پرومی کهن (/۲۸۷-39140 ۵0): 2۸615
7742:انگلیسی کهن (5لا8(0 صل0): -0817 :۸0215 ۷ لالهلا
7782:۸۷ لاله برهان قاطع + ۸۹
7826:بلوچی (الللالهه): 02 ولزی (لاقا78): 20
8423:بلرچی (القلاله8): ت01 هتبت (27177178): 7۸
=== AHD legwh ===
668:legwh-. Light, having little weight. 1. Suffixed form *legeh-t- in Germanic */iht()az in: a. Old English Jiht, léoht, light: LicHT?; b. Old English /ihtan, to lighten: LIGHTER?. 2. Suffixed form *legvh-u-i- in Latin levis (> Old French Jeger), light, with its derivative levdre, to lighten, raise: LEAVEN, LEVER, LEVITY; ALLEVIATE, CARNIVAL, ELEVATE, LEGERDEMAIN, LEVIGATE, (MEZZO-RELIEVO), RELIEVE. 3. Variant form *lagvh- in Old Irish /i-, small: LEPRECHAUN. 4. Nasalized form *l(e)ngeh- in Germanic *lung- in Old English lungen, lungs (from their lightness): LUNG. 5. Attributed by some to this root is Latin oblivisci, to forget, which is more likely from lei-. [Pok. legzh- 660.]
1739:LEAGUER! legh- LEAK leg-2 LEAN! klei- LEAP klou- LEARN leis-1 LEASING leu-! LEAST leis-2 LEATHER letro- LEAVE! leip- LEAVE? §leubh- LEAVEN legWh- LECHER leigh- LECTERN leg-1 LECTION leg-1 LECTURE leg-' LEDGE legh- LEDGER legh- LEE kele-1 LEECH! feg-1 LEECH? leig-1 LEEK leug-! LEER kleu-! LEES legh- LEGACY leg-1 LEGAL leg-1 LEGATE leg-1 LEGATO leig-1 LEGEND leg-1 LEGERDEMAIN leg¥h- LEGIBLE leg-1 LEGION leg-1 LEGISLATOR leg-1, tele- LEGIST leg-1 LEGITIMATE leg-1 LEITMOTIF leit-2 LEMAN leubh- LEMMA! (s)lag¥- LEMMA? lep-t LEMURES_ lem-2 LEND leikw- LENGTH del-1 LENIENT [6-2 LENIS [6-2 LENITIVE |@-2 LENITY 16-2 LENT del-1 LENTO lento-, lep-1. LEPIDO- lep-1 LEPIDOTE lep-1 LEPRECHAUN kWrep-, legwh- -LEPSY (s)lag¥- LEPTO- lep-1 LEPTON! lep-1
1748:LIFT leup- LIGASE leig-1 LIGATE leig-1 LIGHT! = leuk- LIGHT2 legwh-
1750:LIGHTER? legwh- LIGNEOUS  leg-! LIGNI- leg-1 LIGNUM VITAE gWei- LIGULE dngha LIKE! [ik- LIKE? [ik- LIKELY lik- LILAC nei- LIMACINE  lei- LIME = lei- LIMICOLINE lei- LIMN leuk- LIMP kel-1, leb-1 LINDEN _ lento- LINE! lino- LINE? fino- LINEN fino- Linc! del-1 LING? lenk- LINGER del-1 LINGERIE lino- LINGO dnghi LINGUA dnghd LINGUIST dngha LINIMENT lei- LININ lino- LINK! kleng- LINK? Jeuk- LINKS kleng- LINNET fino- _ LINOLEIC ACID [ino- LINSEED lino- LINT Tino-
2269:SLAUGHTER  slak- SLAVER! |leb-1 SLAY slak- SLED sleidh- SLEDGE sleidh- SLEDGEHAMMER slak- SLEEP sléb- SLEET sleu- SLEEVE sleubh- SLEIGH sleidh- SLEIGHT slak- SLEW! sloug- SLICK lei- SLIDE sleidh- SLIGHT lei- SLIM leb-1 SLIME lei- SLING! slengWh- SLINGSHOT slengh- SLINK sleng’h- SLIP! lei-
=== LKT Rubin/lal ===
563:N.  pr.  Name  des  nordöstlichen  Teiles des  lieutigeii  Afgänistän.  Von  hier  be- zot,'  man  in  früheren  Zeiten  Edelsteine [MP  12ü/lt241.  Über  das  ar.  balaM  er- ^ab  sich  als  Bezeichnunjj;  iür  eine  Rubin- art ndat.  bahiscius,  it.  halascio,  halasso, sp.  halaju,  balaja,  pg.  balais,  bedache, kat.  balaix,  frz.  prov.  balais;  dtsch. Ballasrubin.  [Devic  DEt  57.  DE  S!33. ML  891.
2235:930  Ar.  jaküt: 'Edelstein',  nämlich  'Rubin  oder  Saphir'
2737:HWB  188  a  von  einem  Stamme  *karuha, parallel  dem  ar.  karuma  'edelmütig  sein', also  'Glanzerscheinung'  als  Repräsentant undVermittler  derWeltgegenwart  Gottes] ; in  alle  europäischen  Sprachen  überge- gangen: engl.  Cherub  'Engel,  hübsches Kind'  [plr.  in  der  letzteren  Bedeutung: Cherubs],  dtsch.  Cherub,  Cherubin;  frz. cherubin;  russ.  heruwim.
2957:1263.  Sskr.  kuruvinda: 'Rubin',  bind,  zu  kurand,  kurund  zu- sammengezogen; hieraus  engl,  corun- dum,  dtsch.  Korund,  frz.  corindon,  sp. corindön,  corundo,  härtester  Edelstein nach  dem  Diamant;  zu  den  Korunden zählt  man  u.  a.  Rubin,  Saphir,  Amethyst.
3025:'Hochrot',  dazu  tat.  lalä  'Rubin';  hier-
3026:aus serb.  lal  'rot',  russ.  lal  'Rubin'. [Gorjajew  180.  Mikl  SlEtWb  160  a. Bern  SlEtWb  687.
5723:Ballasrubin  151
6346:balais  151
6925:balascio  151
6928:balasso  151
=== TAD leaf for لعل ===
leaves 87
leaf 69
```


## [2026-09-06T23:02:44.782Z] TOOL CALL #77: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== LKT context ===\"; sed -n '3015,3030p' LKT.txt\necho \"=== TAD leaf 69 ===\"; python3 - <<'EOF'\nd=open('TAD_pages.txt',encoding='utf-8',errors='replace').read()\npg=d.split('\\f')\nprint(pg[69][:2500])\nEOF\nls | grep -i tad",
 "description": "LKT lal entry and TAD leaf"
}
```


### [2026-09-06T23:02:47.091Z] TOOL RESULT

```
=== LKT context ===
'Zange'  [vom  Vb.  lakat  'fassen,  auf- heben']; hieraus  mit  ar.  Art.  sp.  alicates, alicantes  'Biegzange',  frz.  alicate  'kleine Zange,  Heren  sich  die  Klempner  bedienen'. [DEFREMERY  in  JAs  1862,  I,  92.  DE 140.  DevicDEt22.  Lammens  Rem  14/15.
1294.  Ar.  laklak:
'Storch'  [onomatopoetische  Bildung  nach dem  Klappern  des  Schnabels,  ebenso  wie ass.  lakalaka  Del  HWB  885  a],  ebenso tk.  leklek,  vulg.  lejlek  [mit  Erweichung des  Gutturals  wie  in  Beg  >  bej,  s.  hier Nr.  282]  'Storch,  Kranich';  hieraus  rum. liliac  'Fledermaus';  serb.  lelek,  lilak, Cech.  lelek,  klruss.  lelek,  russ.  leklek 'Storch'.    [Gorjajew  184.
1295.  Sskr.  läksä:
'Marke,  Fleck;  hunderttausend',  [und nach  den  100000,  d.h.  unzähligen  In- sekten Cocca  ilicis,  welche  durch  ihren Stich  auf  quercus  coccifera  die  harzige Absonderung  bewirken]  'Lack';  hieraus in  der  urspiünglichen  Bedeutung  bind. läkh  '100000',  engl,  lack  'dass.,  bes. 100000  Rupien'  und  ferner:  sp.  pg.  laca 'Lack',  ZßCT-e 'Siegellack',  frz  Jag?«e 'Lack', it.  lacca  'Lack,  Siegellack',  rum.  lac; engl,  lac,  ndl.  lak,  dtsch.  Lack  und  engl. shellac  [eigentlich  'Schalenlack',  da  er zu  kleinen,  dünnen  Täfelchen  geformt wird],  ndl.  schellak,  dtsch.  Schellack; russ.  lak,  Vb.  lakirowat',  bulg.  serb.  lak, Vb.  serb.  lakowati,  Cech.  lak,  Vb.  lako- vaü,  poln.  lakier,  Vb.  lakierowac.  [Hob- son-Jobson  499/501.  Dozy  Oost  57/59. Kluge  274.  DE  295/296.  Devic  DEt 150/151.    Gorjajew  180.
1296.  Tk.  laksa:
'Nudeln,  kleine  l'eigstücke,  die  in  Brühe gekocht  werden'  [nicht  osm.,  nordtk.]; hieraus  russ.  lapsa  'Nudeln,  Faden- nudeln', klruss.  lapsa,  loksa  'dass.'. [MiklSlEtWb  160b.  Bern SlEtWb  690/691.
1297.  Tk.  lakyrdy:
'Gespräch,  Plauderei,  Wort'  [ob  verwandt mit  lat.  loquor,  nach  Walde,  Lateinisches Etymologisches  Wörterbuch.  Heidelberg 1906/10.  S.  348  aus  Zrt^Mor?];  hieraus bulg.  lak^rdija  'Wort,  Unterhaltung', serb.  lakrdija  'Wort,  Tändelei,  Scherz'. [Mikl  SlEtWb  160  a.   Bern  SlEtWb  687.
1298.  Pers.  läl:
'Hochrot',  dazu  tat.  lalä  'Rubin';  hier-
aus serb.  lal  'rot',  russ.  lal  'Rubin'. [Gorjajew  180.  Mikl  SlEtWb  160  a. Bern  SlEtWb  687.
1299.  Pers.  lälä:
'Haus-  und  Hofmeister',  tk.  ebenso  lala 'Diener,  Hofmeister'  [Kölekian  Kämüs 1072];  hieraus  rum.  (dial.)  lalä  'Onkel'; serb.  lala  'tk.  Würdenträger,  Hofmann', bulg.  lala  'Gouverneur',  lalo  'älterer Bruder'.  [Mikl  SlEtWb  160  a.  Bern SlEtWb  688.
1300.  Pers.  lälä:
'Tulpe,  Tulipa  persica'  [s.  auch  hier Nr.  544],  ebenso  tk.  lale;  hieraus  rum. lalea  'dass.';  serb.  lale  'dass.',  bulg.  lale 'dass.,  Mohn'.  [Mikl  SlEtWb  160  a. Bern  SlEtWb  688.
=== TAD leaf 69 ===
                               ‫اخسب سد‬
                            ‫الكشك مرادفه المبضوم أي مطبوخ المعدة والخثارة‬
 ‫بوناني تسطنةمعم‪ -‬أواتك معناه الف غرام وهو بساوي ؟الم‬        ‫كيلوغرام‬    ‫[ْ‬


          ‫‪.٠‬‏‬   ‫‪73‬‬                    ‫ة‬   ‫‪8‬‬           ‫‏‪٠.‬‬
 ‫يمس معئاه سيال وعصارة وف العلب هو‬              ‫وين ‪ -‬وونابي ‪5‬‬
‫استحالة الطعام فى المدة بعد الحضم الجوعر اشر هو مادة عتنة” الى الامقراد‬
          ‫تأخذ لونها غالبامنلونالغذاء الذي تتحلبمنهمرادفه عصارة الحضم‬
 ‫كيميا ‏ في اليونانية ‪#‬نسيرا معنا اختلاط وامئزاج وهو الاكير عند‬
                               ‫القدماء كانوا حولون به المعادن الى ذهب وفضبة‬
‫م كيورة فثر هامر الطعم يطرد‬        ‫كيناوكينهوقينااوري‬

                                      ‫فى امريكا‬
                                              ‫الحمّئ ومنشأها بلاد ابرط‬


                          ‫عل النارسة كوه الاراية‬
                                               ‫ل ان س اممز‬

                                     ‫ل‬
      ‫لازورد ‪ -‬فارسي « لازورد ولاجورد ‪ 6‬وهو حجر ‪ 3 1‬أزرق اللون‬
‫اللات ‪ -‬صم هو مؤنث إل األياله افلىاشورية فيكون معنىاللات الالة‬
‫‪,‬لأمع‪ 1‬معناه فرقة‬    ‫وناني لمعم وى الللانيتي‪9‬‬    ‫ا لحنة ولدة ولاجدون ‪0‬‬

                                                             ‫عسكر وجيش‬
                     ‫لعل حجركم أجمر س‪ -‬فارسبي ‪ 2‬لال » معنا أحمر‬
‫ىليونانية معناه حمْرة‬
                    ‫ل م ‪ -‬تركي « (لن »م معناه قناةوعهرى و ‪807‬هلاه ف ا‬
                ‫والمرادبه حشوة‪ 0‬ندس فى ثقب الص<ور فتنسفبا مرادفه نسفة‬

‫لعن و[لكوت فقالارشية ‪ 2‬لكن ‪ 6‬وف اليونانية ‪ 888101‬وى الارامية‬

TAD_pages.txt
TAD.txt
```


## [2026-09-06T23:02:54.121Z] TOOL CALL #78: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; sed -n '1,200p' tools/verify_check.py",
 "description": "Read verify_check.py"
}
```


### [2026-09-06T23:02:54.157Z] TOOL RESULT

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


## [2026-09-06T23:02:55.969Z] AGENT

Now let me archive the web sources I used.


## [2026-09-06T23:03:00.945Z] TOOL CALL #79: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/لاله' --note 'page 302, root Lâl, node #1: Persian lāleh \"tulip\" — Wiktionary derives it from لال lāl \"red\"' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/لعل' --note 'page 302, root Lâl, nodes #4,#5: Arabic laʿl borrowed from Persian lāl; Persian لعل re-borrowed from Arabic' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/لال' --note 'page 302, root Lâl: Persian lāl \"red\" — of unknown origin; descendants Hindi लाल, Arabic لعل' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/लाल' --note 'page 302, root Lâl, node #6: Hindi लाल lāl \"red\" borrowed from Classical Persian لال' 2>&1 | tail -3",
 "description": "Archive Wiktionary pages (entry 0)"
}
```


### [2026-09-06T23:03:04.332Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/c75cd6dc1566d41c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/be22d88778b5db6d.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/78a5e8f9d0dcdc95.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/0145d303dda35a86.txt
```


## [2026-09-06T23:03:13.629Z] TOOL CALL #80: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/رنج' --note 'page 302, root Lanğ, node #3: Persian ranj inherited from MP lnc /ranǰ/ (MacKenzie 1971:70)' 2>&1 | tail -2\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/रञ्ज्' --note 'page 302, root Lanğ, node #1: Sanskrit rañj-/rajyate \"to redden, be dyed, be excited\" — PIE *(s)reg- \"to dye\", not a \"pain\" root' 2>&1 | tail -2\npython3 tools/fetch_source.py 'https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A1999.04.0057%3Aentry%3Dlagga%2Fzw' --note 'page 302, root Lanğ, node #4: LSJ λαγγάζω \"to slacken\", λαγγεύει \"he flees\"' 2>&1 | tail -2\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/لقلق' --note 'page 302, root Laqalaqa, node #1: Arabic laqlaq \"stork\", cf. Akkadian laqlaqqu, possibly via unattested Aramaic' 2>&1 | tail -2\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/لک‌لک' --note 'page 302, root Laqalaqa, node #2: Persian laklak \"stork\", probably ultimately Semitic; Akk. laqlaqqu, Ar. laqlaq, Neo-Aram. laqlāqā; > Turkish leylek' 2>&1 | tail -2",
 "description": "Archive remaining web sources"
}
```


### [2026-09-06T23:03:17.643Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/5ff01eabefa0dc54.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ca5b88e27fa71d94.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/774b054ac565faeb.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/192e9a70a6cca456.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/1724e382a254a4eb.txt
```


## [2026-09-06T23:03:23.930Z] TOOL CALL #81: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 tools/fetch_source.py 'https://sanskrit.inria.fr/MW/214.html' --note 'page 302, root Lanğ, node #1: Monier-Williams s.v. रज्/रञ्ज् — rajyate \"to be dyed or coloured, redden; to be affected/excited/charmed\", no \"pain\" sense' 2>&1 | tail -2\ngrep -c . data/verification/sources/web/index.jsonl",
 "description": "Archive MW page"
}
```


### [2026-09-06T23:03:32.675Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/825a5237723dbd09.txt
3401
```


## [2026-09-06T23:03:36.468Z] TOOL CALL #82: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; grep -o '\"rajyate[^\"]*\"\\|rajyate[^<]\\{0,200\\}' data/verification/sources/web/825a5237723dbd09.txt | head -5; echo ---; grep -o 'rajyate.\\{0,300\\}' data/verification/sources/web/825a5237723dbd09.txt | head -3",
 "description": "Check MW archived content"
}
```


### [2026-09-06T23:03:38.277Z] TOOL RESULT

```
rajyate ] ; aor. [ arañji ] or [ arāñji ] ) , to dye , colour , paint , redden , illuminate Lit. AV. ; to rejoice , charm , gratify , conciliate Lit. MaitrUp. Lit. Mn. Lit. MBh. ; to worship Lit. Naigh. iii 
rajyate ] and [ rāraṅkti ] ) , to be greatly excited , exult Lit. RV. ix , 5 , 2 ( others " to shine bright " ) . ( cf. Gk. 1 , " to dye " , 2 , " dyer. " ) 
rajyate ] ; aor. [ arañji ] or [ arāñji ] ) , to dye , colour , paint , redden , illuminate Lit. AV. ; to rejoice , charm , gratify , conciliate Lit. MaitrUp. Lit. Mn. Lit. MBh. ; to worship Lit. Naigh. iii 
rajyate ] and [ rāraṅkti ] ) , to be greatly excited , exult Lit. RV. ix , 5 , 2 ( others " to shine bright " ) . ( cf. Gk. 1 , " to dye " , 2 , " dyer. " ) 
---
rajyate ] ; aor. [ arañji ] or [ arāñji ] ) , to dye , colour , paint , redden , illuminate Lit. AV. ; to rejoice , charm , gratify , conciliate Lit. MaitrUp. Lit. Mn. Lit. MBh. ; to worship Lit. Naigh. iii , 14 ( [ rajayati mṛgān ] = [ ramayati mṛgān ] Lit. Pāṇ. 6-4 , 24 Vārtt. 3 Lit. Pat.) : Desid. [ rir
rajyate ] and [ rāraṅkti ] ) , to be greatly excited , exult Lit. RV. ix , 5 , 2 ( others " to shine bright " ) . ( cf. Gk. 1 , " to dye " , 2 , " dyer. " ) 
rajyate ] ; aor. [ arañji ] or [ arāñji ] ) , to dye , colour , paint , redden , illuminate Lit. AV. ; to rejoice , charm , gratify , conciliate Lit. MaitrUp. Lit. Mn. Lit. MBh. ; to worship Lit. Naigh. iii , 14 ( [ rajayati mṛgān ] = [ ramayati mṛgān ] Lit. Pāṇ. 6-4 , 24 Vārtt. 3 Lit. Pat.) : Desid. [ rir
```


## [2026-09-06T23:04:21.357Z] AGENT

Now I'll write the verification file.


## [2026-09-06T23:11:16.798Z] TOOL CALL #83: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build302.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW = \"https://en.wiktionary.org/wiki/\"\n\ndoc = {\n \"pdf_page\": 302,\n \"book_page\": 272,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-06\",\n \"entries\": []\n}\n\n# ---------------------------------------------------------------- entry 0\ne0 = {\n \"entry\": 0,\n \"root\": \"Lâl\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"New Persian لال lāl 'red; a red gemstone (ruby, spinel)' — a genuine Persian colour word of unknown ultimate origin\",\n \"note\": (\"The root box is right on every point that it actually asserts: لال lāl is a New Persian word meaning \"\n          \"'red' (and, as a noun, 'ruby / balas spinel'), and the whole family on this page hangs together. \"\n          \"Borhan-e Qate' p.1879 s.v. لال: 'معروف است ... و رنگ سرخ را نیز گفته‌اند - و بمعنی لعل هم آمده است ... \"\n          \"و بعضی گویند لعل معرب لال است', with Mo'in's footnote 7 «لعل معرب «لال» است «نخبه ۱۶»؛ «لال» لعل باشد «لغت فرس ۳۲۹»»; \"\n          \"Mo'in's own Farhang s.v. لال ۳ has '[قس. لاله، آلاله، لعل، معر.] (ص.) سرخ؛ احمر. (اِ.) (زه.) لعل' — i.e. Mo'in \"\n          \"groups exactly the same words Nourai groups. Lokotsch no.1298 'Pers. lāl: Hochrot'. What Nourai does not say, and \"\n          \"what no source can supply, is where lāl itself comes from: Wiktionary marks it 'of unknown origin' and merely \"\n          \"wonders whether it could be a heavily reduced reflex of PIE *h₁rewdʰ- 'red'. Treating لال as an unanalysed Persian \"\n          \"root is therefore the honest choice. Note that the homophone لال 'mute, tongue-tied' (BQT 1879, Mo'in لال ۱) is a \"\n          \"different word and is correctly kept out of this chart.\"),\n \"note_fa\": (\"سرِ نمودار «لال» است، واژه‌ای فارسی به معنی «سرخ» و نیز «گوهر سرخ (لعل، بدخشی)». برهان قاطع ص ۱۸۷۹ ذیل «لال» \"\n             \"همین دو معنی را می‌آورد و در حاشیهٔ معین آمده که «لعل معرّب لال است». معین نیز در فرهنگ فارسی ذیل لال ۳ می‌نویسد \"\n             \"«[قس. لاله، آلاله، لعل، معرّب] سرخ، احمر»، یعنی همان خانوادهٔ واژگانی که نورایی ساخته است. اما ریشهٔ خودِ «لال» \"\n             \"ناشناخته است؛ ویکی‌واژه آن را «of unknown origin» می‌داند و تنها به احتمال پیوند با هندواروپایی آغازین *h₁rewdʰ- \"\n             \"«سرخ» اشاره می‌کند. پس ادعای نورایی در همین حد که «لالِ فارسی به معنی سرخ» ریشهٔ این خانواده است، درست است.\"),\n \"sources\": [W+\"لال\", W+\"لعل\"],\n \"ref_check\": [\n   {\"ref\": \"BQT:1879\", \"status\": \"supports\",\n    \"note\": \"Borhan-e Qate' (Mo'in ed.) p.1879, entry لال: «لال - بر وزن مال ... و رنگ سرخ را نیز گفته‌اند - و بمعنی لعل هم آمده است وآن گوهری است گرانبها که معدن آن در بدخشان است و بعربی لعل گویند؛ و بعضی گویند لعل معرب لال است»; fn.7 «لعل معرب «لال» است «نخبه ۱۶»». Read from data/verification/sources/refs/ocr/BQT/1879.png/.txt (ref_page.py BQT:1879, pdf page 676 of BQT_v3_picofile.pdf).\"},\n   {\"ref\": \"KLN:904\", \"status\": \"supports\",\n    \"note\": \"Klein 1966 vol.2 p.904 s.v. 'loll shraub': «Hind. lal sharab, 'red, wine', fr. Pers. lal, 'red', and Arab. sharab, 'drink, wine'» — Klein too takes Persian lāl 'red' as the source word (grep 'loll  shraub' in KLN_1966.txt).\"}\n ],\n \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"s.v. لال ۳ (Adena 2-vol OCR, MON_part2.txt l.38107)\", \"stance\": \"supports\",\n    \"note\": \"«۳ lāl [قس. لاله، آلاله، لعل، معر.] (ص.) سرخ؛ احمر. (اِ.) (زه.) لعل» — Mo'in cross-refers لال to لاله، آلاله and (Arabicized) لعل, exactly Nourai's grouping.\"},\n   {\"src\": \"LKT\", \"where\": \"no. 1298, p. ~245\", \"stance\": \"supports\",\n    \"note\": \"Lokotsch: «1298. Pers. lāl: 'Hochrot', dazu tat. lalä 'Rubin'; hieraus serb. lal 'rot', russ. lal 'Rubin'» (grep 'Hochrot' in LKT.txt).\"},\n   {\"src\": \"HRN\", \"where\": \"grep 'Tulpe', 'lâl' in HRN.txt\", \"stance\": \"silent\",\n    \"note\": \"Horn's Grundriss has no entry for لال / لاله; the word is not treated in his Neupersische Etymologie.\"},\n   {\"src\": \"HUB\", \"where\": \"grep 'Tulpe' in HUB.txt\", \"stance\": \"silent\",\n    \"note\": \"Hübschmann, Persische Studien: nothing on لال / لاله.\"}\n ],\n \"nodes\": []\n}\n\ne0[\"nodes\"].append({\n \"id\": 1, \"lang\": \"Persian\", \"words\": \"lâleh; âlâleh\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"NP لاله lāleh 'tulip (Tulipa), and by extension anemone/poppy' and its by-form آلاله ālāleh \"\n   \"(ranunculus/anemone) are formed on lāl 'red' — the flower is named from its colour, with the common Persian \"\n   \"nominal suffix -a/-eh (as in سبزه sabze from سبز, سرخه from سرخ); the ā- of آلاله is the well-known prothetic/\"\n   \"reduplicative variation of the same stem (لاله ~ آلاله are given as one word by Mo'in). Mo'in's own footnote in \"\n   \"Borhan-e Qate' p.1880 (fn.7 to لاله) says it plainly: «آلاله. در پهلوی یافته نشد؛ و شگفت نیست که این کلمه با «لال» \"\n   \"(سرخ) رابطه دارد و گلی که لاله خوانده شده بمناسبت رنگ آن است» ('ālāla is not attested in Pahlavi; it would not be \"\n   \"surprising that this word is related to lāl (red), the flower being so called on account of its colour'), citing \"\n   \"Hormozdnāme p.137 and Kurdish lāla. Wiktionary's Persian entry says the same, 'Likely from لال (lâl, literally red)'. \"\n   \"No Middle Persian antecedent is attested, so the derivation is a Persian-internal one; from Persian the word passed \"\n   \"to Ottoman Turkish lale and thence to the European tulip words (via tülbend 'turban'). The Onsori couplet Nourai \"\n   \"prints ('دو رخ چو نار شکفته، دو لب چو لالهٔ لال') is BQT p.1879 fn.6 and itself pairs lāleh with lāl.\"),\n \"derivation_fa\": (\"«لاله» (گل سرخ‌رنگ) و گونهٔ دیگر آن «آلاله» از همان ستاک «لال» (سرخ) با پسوند اسم‌ساز ـه ساخته شده‌اند، \"\n   \"درست مانند «سبزه» از «سبز». معین در حاشیهٔ برهان قاطع ص ۱۸۸۰ می‌نویسد: «آلاله. در پهلوی یافته نشد و شگفت نیست که این \"\n   \"کلمه با «لال» (سرخ) رابطه دارد و گلی که لاله خوانده شده بمناسبت رنگ آن است» و به هرمزدنامه ص ۱۳۷ و لالهٔ کردی ارجاع می‌دهد. \"\n   \"در فارسی میانه صورتی برای آن گواهی نشده است، پس این ساخت درون‌فارسی است؛ از فارسی به ترکی عثمانی (lale) و از آنجا به \"\n   \"زبان‌های اروپایی رفته است. ادعای نورایی درست است.\"),\n \"sources\": [W+\"لاله\", W+\"لال\"],\n \"ref_check\": [\n   {\"ref\": \"BQT:1879\", \"status\": \"partial\",\n    \"note\": \"The headword لاله is actually on p.1880, not 1879 (p.1879 has لال, لالا, لالاسرا); Nourai's page number is one off. BQT p.1880 fn.7 does carry the etymology quoted above (data/verification/sources/refs/ocr/BQT/1880.txt).\"},\n   {\"ref\": \"MON:3536\", \"status\": \"supports\",\n    \"note\": \"Mo'in's Farhang s.v. لاله: «لاله [= آلاله - قس. لال، سرخ]» (MON_part2.txt l.38122) — the Adena condensation preserves the cross-reference to لال 'red'; the 6-vol page number itself cannot be checked (no scan of the 6-vol edition exists).\"}\n ],\n \"consulted\": [\n   {\"src\": \"BQT\", \"where\": \"p.1880 fn.7 (ocr/BQT/1880.txt)\", \"stance\": \"supports\",\n    \"note\": \"«آلاله. در پهلوی یافته نشد؛ و شگفت نیست که این کلمه با «لال» (سرخ) رابطه دارد ... «هرمزدنامه ص ۱۳۷»؛ کردی lāla».\"},\n   {\"src\": \"MON\", \"where\": \"s.v. لاله (MON_part2.txt l.38122)\", \"stance\": \"supports\",\n    \"note\": \"«لاله: [- آلاله - قس. لال، سرخ]».\"},\n   {\"src\": \"LKT\", \"where\": \"no. 1300\", \"stance\": \"partial\",\n    \"note\": \"«1300. Pers. lālā: 'Tulpe, Tulipa persica', ebenso tk. lale; hieraus rum. lalea, serb. lale, bulg. lale 'Tulpe, Mohn'» — Lokotsch records the word and its spread but gives no internal etymology.\"},\n   {\"src\": \"HRN\", \"where\": \"HRN.txt, grep 'Tulpe'\", \"stance\": \"silent\", \"note\": \"Horn has no article on لاله.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 2, \"lang\": \"Persian\", \"words\": \"lâlak\",\n \"verdict\": \"plausible\",\n \"derivation\": (\"NP لالک lālak (also لالکا lālakā) is glossed in Borhan-e Qate' p.1880 as «کفش و پای‌افزار» 'shoe, \"\n   \"footwear' — the gloss 'red leather and shoes made from it' is a fuller version of the same entry. Formally it is \"\n   \"lāl + the diminutive/appurtenance suffix -ak (as in پشمک, نمکک), so 'the little red thing / the red(-dyed) one'. \"\n   \"Mo'in's footnote 3 on that page says only «شاید در اصل بهای‌افزار لالِ (سرخ) رنگ اطلاق میشده» ('perhaps it was \"\n   \"originally applied to footwear of lāl (red) colour', Hormozdnāme p.132) and adds the Arabicized doublets لالکه / \"\n   \"لالجه from the Muʿjam al-udabāʾ. So the colour etymology is offered by Mo'in himself but marked as a guess (شاید), \"\n   \"and no independent modern treatment of lālak exists; hence 'plausible' rather than 'confirmed'. The Suzani verse \"\n   \"Nourai prints («که عاشق است بر آن لاله‌روی لالک‌دوز») is BQT p.1880 fn.3, from Hormozdnāme p.133.\"),\n \"derivation_fa\": (\"«لالک (لالکا)» در برهان قاطع ص ۱۸۸۰ «کفش و پای‌افزار» معنی شده است. از نظر ساخت، «لال» + پسوند تصغیر/نسبت «ـک» \"\n   \"است، یعنی «(چیزِ) سرخ‌رنگِ کوچک». معین در حاشیه تنها با احتیاط می‌نویسد: «شاید در اصل به پای‌افزار لال (سرخ) رنگ اطلاق می‌شده \"\n   \"«هرمزدنامه ص ۱۳۲»» و صورت‌های معرّب «لالکه» و «لالجه» را نیز می‌آورد. چون هیچ منبع مستقل امروزی این واژه را بررسی نکرده و \"\n   \"خود معین هم با «شاید» سخن گفته، ادعای نورایی با احتیاط پذیرفتنی است.\"),\n \"sources\": [W+\"لال\"],\n \"ref_check\": [\n   {\"ref\": \"BQT:1880\", \"status\": \"supports\",\n    \"note\": \"BQT p.1880: «لالک - بروزن کالک، کفش و پای‌افزار را گویند»; fn.3 «شاید در اصل بهای‌افزار لال (سرخ) رنگ اطلاق میشده «هرمزدنامه ص ۱۳۲»؛ لالک > لالکه (معرب) «معجم الادباء چاپ مارگلیوث ج ۳ ص ۱۹۶» > لالجه (معرب)» plus the Suzani couplet (ocr/BQT/1880.txt).\"},\n   {\"ref\": \"MON:3536\", \"status\": \"partial\",\n    \"note\": \"Mo'in's لالک entry in the Adena condensation (MON_part2.txt l.38220) gives «لالکا، لاله گوش» (earlobe) and the geranium, i.e. a different sense-group; the footwear sense is not carried there, so the page could not be confirmed.\"}\n ],\n \"consulted\": [\n   {\"src\": \"BQT\", \"where\": \"p.1880 and fn.3\", \"stance\": \"partial\", \"note\": \"gives the colour etymology, but hedged with «شاید».\"},\n   {\"src\": \"MON\", \"where\": \"s.v. لالک (MON_part2.txt l.38220)\", \"stance\": \"silent\", \"note\": \"no etymology for the 'shoe' sense in the two-volume abridgement.\"},\n   {\"src\": \"ARY\", \"where\": \"incoming/ARY/ARY_pages.txt, grep لالک\", \"stance\": \"silent\", \"note\": \"Aryanpur's IE-roots dictionary has no entry for لالک.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 3, \"lang\": \"Persian\", \"words\": \"lâleh-sâr; lâlas\",\n \"verdict\": \"plausible\",\n \"derivation\": (\"Two words of unequal standing. (a) لاله‌سار lāleh-sār 'a red-headed bird' is well founded: BQT p.1880 \"\n   \"fn.9 analyses it «از: لاله (سرخ) + سار (< سر)؛ لاله‌سار باید مرغی باشد سرسرخ، چنانکه خشن‌سار مرغی است سرسفید» — 'from \"\n   \"lāleh (red) + sār (< sar 'head'); lāleh-sār must be a red-headed bird, just as xašn-sār is a white-headed one', \"\n   \"citing Asadi Tusi and Hormozdnāme p.351. That is exactly Nourai's cross-reference ☞Ker 1 (sar 'head' < PIE *ḱerh₂-). \"\n   \"(b) لالس lālas is glossed by Borhan simply as «نوعی از پارچهٔ ابریشمی خوش قماش نازک لطیف» — 'a kind of fine, delicate \"\n   \"silk fabric' — with no colour at all, and Mo'in's footnote 2 on that entry only rejects the Indian 'face' sense \"\n   \"(«لالس بمعنی روی در هیچ لغت سنسکرت یافت نشد»). The word 'red' in Nourai's gloss is his own addition, made to fit the \"\n   \"root; the fabric name may just as well be a foreign textile term. Hence the node as a whole is only plausible.\"),\n \"derivation_fa\": (\"این گره دو واژه دارد. یکم «لاله‌سار» «مرغی سرخ‌سر»: حاشیهٔ ۹ برهان قاطع ص ۱۸۸۰ آن را چنین تحلیل می‌کند: \"\n   \"«از: لاله (سرخ) + سار (< سر)؛ لاله‌سار باید مرغی باشد سرسرخ، چنانکه خشن‌سار مرغی است سرسفید»؛ این همان ارجاع نورایی به \"\n   \"ریشهٔ Ker 1 («سر») است و درست است. دوم «لالس»: برهان آن را تنها «نوعی از پارچهٔ ابریشمی خوش قماش نازک لطیف» معنی می‌کند و \"\n   \"هیچ سخنی از سرخی نیست؛ حاشیهٔ معین هم فقط معنیِ «روی» را در سنسکریت رد می‌کند. پس صفت «سرخ» در معنیِ نورایی افزودهٔ خود \"\n   \"اوست و پیوند «لالس» با «لال» اثبات‌نشده است؛ ازاین‌رو این گره در مجموع «با احتیاط پذیرفتنی» است.\"),\n \"sources\": [W+\"لال\"],\n \"ref_check\": [\n   {\"ref\": \"BQT:1880\", \"status\": \"partial\",\n    \"note\": \"Supports لاله‌سار fully (fn.9, quoted above) but not the 'red' in لالس: the entry reads «لالس - بفتح لام و سکون سین بی نقطه: نوعی از پارچهٔ ابریشمی خوش قماش نازک لطیف ... و بزبان علمی اهل هند بمعنی روی باشد که بعربی وجه خوانند», fn.2 «لالس بمعنی روی در هیچ لغت سنسکرت یافت نشد «چک ص ۹۹۵ ح»» (ocr/BQT/1880.txt; the Badr Jājarmi couplet Nourai prints is fn.1 of the same entry).\"}\n ],\n \"consulted\": [\n   {\"src\": \"BQT\", \"where\": \"p.1880 fnn.1, 2, 9\", \"stance\": \"partial\", \"note\": \"explicit colour etymology for لاله‌سار; none for لالس.\"},\n   {\"src\": \"MON\", \"where\": \"MON_part2.txt, grep لالس / لاله‌سار\", \"stance\": \"silent\", \"note\": \"neither word survives in the two-volume abridgement of Mo'in.\"},\n   {\"src\": \"FRS\", \"where\": \"FRS_pages.txt (Asadi's Loghat-e Fors)\", \"stance\": \"silent\", \"note\": \"Borhan's fn.9 attributes لاله‌سار to Asadi Tusi, but the word could not be located in the OCR of the Mojtaba'i–Sadeqi edition.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 4, \"lang\": \"Arabic\", \"words\": \"la`l\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"Arabic لَعْل laʿl 'a red gemstone, ruby/balas spinel; red' is a muʿarrab of Persian lāl. Since Arabic \"\n   \"phonotactics disfavour a bare CaaC loan of this shape and Arabic likes a triliteral skeleton, the long ā of lāl was \"\n   \"resolved into a strong ʿayn plus short vowel, giving the root-shape l-ʿ-l — the same kind of ʿayn-insertion seen in \"\n   \"other Persian loans. Addi Shir states it in one line (AFM p.142): «(اللَعْل) حجر كريم تعريب لال واصل معناه الأحمر» \"\n   \"'al-laʿl, a precious stone, Arabicized from lāl, whose original meaning is red'. Tobia al-ʿUnaysi (TAD p.66) has \"\n   \"«لعل حجر كريم أحمر - فارسي «لال» معناه أحمر». Asbaghi (PLA p.241) lists «لعل laʿl: 'Rubin' pers. [lāl], s. lāla» — \"\n   \"and, notably, cross-refers it to لاله, i.e. he groups the ruby word with the tulip word exactly as Nourai does. \"\n   \"Wiktionary: 'borrowed from Persian لال (lâl)'. The stones so called were the balas spinels of Badaxšān, which is \"\n   \"also why Borhan says «معدن آن در بدخشان است».\"),\n \"derivation_fa\": (\"عربی «لَعْل» (گوهر سرخ، لعل بدخشی) معرّبِ «لال» فارسی است. چون ساخت CāC در عربی جا نمی‌افتاد، مصوّت بلند \"\n   \"«ا» به «ع» بدل شده و ریشهٔ سه‌حرفی ل‑ع‑ل پدید آمده است؛ همان‌گونه که در چند وام‌واژهٔ فارسی دیگر نیز «ع» افزوده شده است. \"\n   \"أدّي شير در «الألفاظ الفارسیة المعرّبة» ص ۱۴۲ می‌نویسد: «(اللَعْل) حجر كريم تعريب لال واصل معناه الأحمر»، و طوبیا العنیسی \"\n   \"(ص ۶۶) «لعل حجر كريم أحمر ـ فارسي «لال» معناه أحمر». اسبقی نیز در «واژه‌های فارسی در عربی» ص ۲۴۱ آن را فارسی و هم‌خانوادهٔ \"\n   \"«لاله» می‌داند. ادعای نورایی درست است.\"),\n \"sources\": [W+\"لعل\", W+\"لال\"],\n \"ref_check\": [\n   {\"ref\": \"AFM:142\", \"status\": \"supports\",\n    \"note\": \"Addi Shir p.142 (verified on the page image; the line is dropped by both OCR files): «٭ ( اللَعْل ) حجر كريم تعريب لال واصل معناه الأحمر». Image and transcription saved as data/verification/sources/refs/ocr/AFM/0142.png and 0142.vision.txt (AFM.pdf pdf-page 144; the printed numeral ١٤٢ is on the page).\"},\n   {\"ref\": \"PLA:241\", \"status\": \"supports\",\n    \"note\": \"Asbaghi, Persische Lehnwörter im Arabischen, p.241 (incoming/PLA/PLA_pages.txt leaf index 255): «لعل - la'l: \\\"Rubin\\\" pers. [لال] s. lāla» followed by «lāla: \\\"Tulpe\\\" pers.» — Persian origin, and cross-referenced to lāla.\"},\n   {\"ref\": \"TAD:66\", \"status\": \"supports\",\n    \"note\": \"al-ʿUnaysi, Tafsīr al-alfāẓ al-dākhila, ل section (TAD_pages.txt leaf 69, printed p.66): «لعل حجر كريم أحمر - فارسي «لال» معناه أحمر».\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"vol.2 p.904 s.v. loll shraub\", \"stance\": \"partial\", \"note\": \"Klein derives the Anglo-Indian phrase from Pers. lāl 'red' but does not discuss Arabic لعل itself.\"},\n   {\"src\": \"LKT\", \"where\": \"no. 1298\", \"stance\": \"partial\", \"note\": \"«Pers. lāl 'Hochrot', dazu tat. lalä 'Rubin'» — Persian source affirmed, Arabic route not treated.\"},\n   {\"src\": \"FVQ\", \"where\": \"FVQ_pages.txt, grep لعل / la'l\", \"stance\": \"silent\", \"note\": \"Jeffery's Foreign Vocabulary of the Qur'an has no entry (the word is not Qur'anic).\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 5, \"lang\": \"Persian\", \"words\": \"la`l\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"Persian لعل laʿl 'ruby; (of lips) ruby-red' is the Arabicized form re-borrowed into Persian — a classic \"\n   \"Persian→Arabic→Persian round trip, so that لال and لعل are doublets in the same language. Borhan-e Qate' p.1879 says \"\n   \"it outright: «و بمعنی لعل هم آمده است ... و بعضی گویند لعل معرب لال است», with Mo'in's fn.7 citing Noxba p.16 and \"\n   \"Loghat-e Fors p.329 («لال» لعل باشد). Mo'in's Farhang tags لال with «معر.» pointing at لعل. Wiktionary states the \"\n   \"circular path explicitly: Persian لعل 'borrowed from Arabic لَعْل, from Persian لال'. In classical poetry the word is \"\n   \"conventional for the beloved's lips (Hafez's «لعل تو که هست جان حافظ», which Nourai prints), the extension being \"\n   \"'red gem' → 'red lips' → 'red wine'.\"),\n \"derivation_fa\": (\"«لعل» فارسیِ نو همان صورت معرّبِ «لال» است که دوباره به فارسی بازگشته؛ یعنی «لال» و «لعل» در فارسی دوگانه \"\n   \"(doublet) اند و این یک وام‌گیریِ رفت‌وبرگشتی فارسی ← عربی ← فارسی است. برهان قاطع ص ۱۸۷۹ می‌نویسد «بعضی گویند لعل معرّب \"\n   \"لال است» و معین در حاشیه به «نخبه ۱۶» و «لغت فرس ۳۲۹» ارجاع می‌دهد. در شعر فارسی «لعل» استعارهٔ لبِ معشوق است (بیت حافظ که \"\n   \"نورایی آورده) و از آنجا به «شراب سرخ» نیز کشیده شده است. ادعای نورایی درست است.\"),\n \"sources\": [W+\"لعل\", W+\"لال\"],\n \"ref_check\": [\n   {\"ref\": \"BQT:1879\", \"status\": \"supports\",\n    \"note\": \"p.1879 s.v. لال: «... و بمعنی لعل هم آمده است وآن گوهری است گرانبها که معدن آن در بدخشان است و بعربی لعل گویند؛ و بعضی گویند لعل معرب لال است»; fn.7 «لعل معرب «لال» است «نخبه ۱۶». «لال» لعل باشد «لغت فرس ۳۲۹»» (ocr/BQT/1879.txt).\"}\n ],\n \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"s.v. لال ۳ (MON_part2.txt l.38107)\", \"stance\": \"supports\", \"note\": \"«[قس. لاله، آلاله، لعل، معر.]» — Mo'in explicitly marks لعل as the muʿarrab of لال.\"},\n   {\"src\": \"PLA\", \"where\": \"p.241\", \"stance\": \"supports\", \"note\": \"Asbaghi lists laʿl among the Persian loanwords in Arabic, which entails the Persian form as the source of the re-borrowed لعل.\"},\n   {\"src\": \"ARY\", \"where\": \"incoming/ARY/ARY_pages.txt, grep لعل\", \"stance\": \"silent\", \"note\": \"not in Aryanpur's IE-roots dictionary (as expected, since the word is not treated as inherited IE).\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 6, \"lang\": \"Hindustani\", \"words\": \"lâl; lâl-šarâb\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"Hindi-Urdu लाल / لال lāl 'red' is a straight borrowing of Classical Persian لال, taken over with the \"\n   \"Persianate administrative and courtly vocabulary of the Delhi Sultanate and Mughal period; Wiktionary's Hindi entry \"\n   \"says so ('Borrowed from Classical Persian لَال (lāl)') and distinguishes it from the homograph lāl 'dear one', which \"\n   \"is inherited from Sanskrit lālya-. The compound lāl-śarāb 'red wine' is Persian lāl + Arabic šarāb 'drink, wine' \"\n   \"(root š-r-b), the Arabic word having reached Hindustani through Persian — which is exactly Nourai's cross-reference \"\n   \"☞Š.r.b. Klein p.904 gives the same analysis: «Hind. lal sharab, 'red, wine', fr. Pers. lal, 'red', and Arab. sharab». \"\n   \"Hobson-Jobson p.501b calls lāl-sharāb 'Englishman's Hind.' — i.e. the compound is largely a sahib coinage — and lists \"\n   \"the parallel formations Port-shraub, Sherry-shraub, Brandy-shraub, Beer-shraub.\"),\n \"derivation_fa\": (\"«لال» در هندی‑اردو (लाल) وام‌واژه‌ای است از فارسی کلاسیک که همراه با واژگان دیوانی و درباریِ فارسی در دورهٔ \"\n   \"سلطنت دهلی و گورکانیان به هند رفته است؛ ویکی‌واژه صریحاً می‌نویسد «Borrowed from Classical Persian لال» و آن را از \"\n   \"همنگارِ lāl «عزیز» (از سنسکریت lālya-) جدا می‌کند. ترکیب lāl-šarāb «شراب سرخ» از «لالِ» فارسی + «شرابِ» عربی (ریشهٔ ش‑ر‑ب) \"\n   \"ساخته شده که خودِ شراب نیز از راه فارسی به هندوستانی رسیده است؛ همان ارجاع نورایی به ریشهٔ Š.r.b. کلاین ص ۹۰۴ نیز همین \"\n   \"تحلیل را دارد. ادعای نورایی درست است.\"),\n \"sources\": [W+\"लाल\", W+\"لال\"],\n \"ref_check\": [\n   {\"ref\": \"KLN:904\", \"status\": \"supports\",\n    \"note\": \"Klein 1966 vol.2 p.904: «loll shraub, loll shrob, claret (India). — Hind. lal sharab, 'red, wine', fr. Pers. lal, 'red', and Arab. sharab, 'drink, wine' (see sirup)» (grep 'loll  shraub' in KLN_1966.txt).\"}\n ],\n \"consulted\": [\n   {\"src\": \"HJB\", \"where\": \"Hobson-Jobson p.501b s.v. LALL-SHRAUB\", \"stance\": \"supports\",\n    \"note\": \"«LALL-SHRAUB, s. Englishman's Hind. lāl-sharāb, 'red wine.' The universal name of claret in India» (HJB.txt l.12925); s.v. SHRUB: «The form shrāb is applied in India to all wines and spirits ... Port-shraub, Sherry-shraub, Lall-Shraub, Brandy-shraub, Beer-shraub».\"},\n   {\"src\": \"AID\", \"where\": \"AID.txt, grep 'loll' / 'lal'\", \"stance\": \"silent\", \"note\": \"Whitworth's Anglo-Indian Dictionary (1885) has no entry for the phrase.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 7, \"lang\": \"English\", \"words\": \"loll sharob\",\n \"verdict\": \"transcription_suspect\",\n \"derivation\": (\"The Anglo-Indian word is real, but the printed form on this page is corrupt. The attested English \"\n   \"spellings are 'loll shraub' / 'loll shrob' (Klein p.904, which is the reference Nourai himself cites) and \"\n   \"'Lall-shraub' / 'Loll Shrub' (Hobson-Jobson p.501b, with a c.1780 quotation from Mrs Fay's Calcutta diary: 'one \"\n   \"pyramidal ... for Loll Shrub (scilicet, claret)'). The book prints 'loll sharob', with the r and the vowel \"\n   \"transposed — a metathesis of shraub/shrob that no source knows. The extraction is faithful to the page (checked on \"\n   \"the 600-dpi render of pdf page 302, saved as data/verification/sources/refs/ocr/BOOK/302.png), so the error is \"\n   \"Nourai's own. On the substance the node is right: British residents in Bengal from the later 18th century took over \"\n   \"Hindustani lāl-sharāb as the standard name of claret, and the phrase died out with the Raj.\"),\n \"derivation_fa\": (\"واژهٔ انگلیسیِ هندی‑بریتانیایی واقعی است، اما صورت چاپ‌شده در کتاب نادرست است. املای گواهی‌شده \"\n   \"«loll shraub / loll shrob» (کلاین ص ۹۰۴، همان مأخذی که نورایی به آن ارجاع می‌دهد) و «Lall-shraub / Loll Shrub» \"\n   \"(هابسن‑جابسن ص ۵۰۱ب، با شاهدی از حدود ۱۷۸۰) است. کتاب «loll sharob» چاپ کرده، یعنی «ر» و مصوّت جابه‌جا شده‌اند (قلب). \"\n   \"بررسی تصویر صفحهٔ ۳۰۲ نشان می‌دهد که خوانش اسکن درست است و خطا از خودِ کتاب است. از نظر معنایی گره درست است: انگلیسیان \"\n   \"بنگال از اواخر سدهٔ هجدهم «لال‌شراب» هندوستانی را نام معمول شرابِ سرخ (claret) کردند.\"),\n \"error_in\": \"book\",\n \"book_prints\": \"loll sharob\",\n \"correct_form\": \"loll shraub / loll shrob (Klein); Lall-shraub, Loll Shrub (Hobson-Jobson)\",\n \"sources\": [W+\"लाल\"],\n \"ref_check\": [\n   {\"ref\": \"KLN:904\", \"status\": \"partial\",\n    \"note\": \"Klein p.904 has the entry but spells it «loll shraub, loll shrob», not 'loll sharob'; the derivation Klein gives («Hind. lal sharab ... fr. Pers. lal ... and Arab. sharab») is the one drawn on the chart, so only the spelling is at fault.\"}\n ],\n \"consulted\": [\n   {\"src\": \"HJB\", \"where\": \"p.501b s.v. LALL-SHRAUB; index p.'Lall-shraub, 501b'\", \"stance\": \"partial\",\n    \"note\": \"«LALL-SHRAUB ... The universal name of claret in India»; quotation c.1780 «for Loll Shrub (scilicet, claret)» — again no spelling 'sharob'.\"},\n   {\"src\": \"SKT\", \"where\": \"SKT.txt, grep 'loll shr'\", \"stance\": \"silent\", \"note\": \"Skeat's Concise Dictionary does not carry the Anglo-Indian word.\"},\n   {\"src\": \"AID\", \"where\": \"AID.txt, grep 'loll'\", \"stance\": \"silent\", \"note\": \"Whitworth (1885) does not have it either.\"}\n ]\n})\ndoc[\"entries\"].append(e0)\n\n# ---------------------------------------------------------------- entry 1\ne1 = {\n \"entry\": 1,\n \"root\": \"Lanğ\",\n \"verdict\": \"disputed\",\n \"modern_form\": \"No PIE root *lang- 'droop, be sad' is recognised today; Persian ranj goes back to Proto-Iranian *Hranj- (Av. rənj-) < PIE *h₁lengʷʰ- 'to move lightly, spur, impel' (LIV 247; Pokorny 660 f. legʷh- 'leicht in Bewegung und Gewicht')\",\n \"note\": (\"The root box reproduces S. E. Mann, IEC p.663, faithfully — and Mann's entry is itself explicitly marked as \"\n   \"unreliable: «lang- 'drooping, sad; droop, be sad; sadness'. **All evidence ambig.** Per. ranja, ranjiš 'sorrow, \"\n   \"annoyance'; ranjidan, inf. 'be sad'; Gk. laggázo, laggéo 'droop, flag' beside lagarós, adj. 'sunken, slack'» \"\n   \"(IEC.txt leaf 373 = printed pp. 662–663). Mann's whole root rests on the two branches drawn here and on nothing \"\n   \"else; there is no Indo-Iranian, Italic, Germanic, Balto-Slavic or Celtic support, and Pokorny, Walde-Pokorny and \"\n   \"Watkins/AHD have no such root. Modern Iranian etymology puts the Persian word somewhere quite different: Cheung, \"\n   \"Etymological Dictionary of the Iranian Verb, p.191, sets up *Hranj- 'to take action, spur, urge (often with negative \"\n   \"consequences)' with Young Avestan rənjaiti, MMP rnz, BMP lnc, Parthian rnj, Khotanese ārraṃj-, Sogdian rxn- 'to \"\n   \"dare', NP ranjidan, and refers it to PIE *h₁lengʷʰ- (LIV 247; Pok. 660 f.), the 'light, nimble, quick' root — \"\n   \"Pokorny p.660 f. legʷh- 'leicht in Bewegung und Gewicht, verbal sich leicht, flink bewegen; nasaliert lengʷh-', with \"\n   \"av. rənjaiti 'macht leicht, flink', ai. ráṃhate 'rinnt, eilt'. Greek λαγγάζω, by contrast, is grouped with λαγαρός \"\n   \"'slack' under *(s)leg- 'to be slack'. Nourai's gloss 'to droop, be sad, sorrow' is thus a semantic reading-back from \"\n   \"the Persian word, and the root as drawn is not accepted.\"),\n \"note_fa\": (\"این ریشه دقیقاً از فرهنگ تطبیقی هندواروپاییِ مان (IEC ص ۶۶۳) گرفته شده است، اما خودِ مان زیر همان مدخل نوشته \"\n   \"«All evidence ambig.» یعنی «همهٔ شواهد مبهم‌اند»؛ تمام بنیاد این ریشه همین دو شاخهٔ فارسی و یونانی است و پوکورنی، \"\n   \"والده‑پوکورنی و واتکینز چنین ریشه‌ای ندارند. ریشه‌شناسی امروزی «رنج» را جای دیگری می‌نشاند: چونگ در فرهنگ ریشه‌شناختی \"\n   \"فعل ایرانی (ص ۱۹۱) ستاک ایرانی *Hranj- را با اوستایی rənjaiti، پارتی rnj، فارسی میانهٔ ranz/ranj، ختنی ārraṃj- و سغدی \"\n   \"rxn- بازسازی می‌کند و آن را به هندواروپایی آغازین *h₁lengʷʰ- «سبک و چابک حرکت کردن، برانگیختن» (پوکورنی ۶۶۰ـ۶۶۱) \"\n   \"بازمی‌گرداند، نه به ریشه‌ای به معنی «افسردن». یونانیِ λαγγάζω نیز امروز با λαγαρός «شل» زیر *(s)leg- می‌آید. پس معنیِ \"\n   \"«افسردن، اندوهگین شدن» تعمیم معنیِ فارسیِ «رنج» به ریشه است و پژوهش امروزی این ریشه را نمی‌پذیرد.\"),\n \"sources\": [W+\"رنج\", \"https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A1999.04.0057%3Aentry%3Dlagga%2Fzw\"],\n \"ref_check\": [\n   {\"ref\": \"IEC:663\", \"status\": \"supports\",\n    \"note\": \"Mann, An Indo-European Comparative Dictionary p.663 (IEC.txt leaf 373): «lang- 'drooping, sad; droop, be sad; sadness'. All evidence ambig. Per. ranja, ranjiš 'sorrow, annoyance'; ranjidan, inf. 'be sad'; Gk. laggázo, laggéo 'droop, flag' beside lagarós, adj. 'sunken, slack'.» The reference does say what Nourai's root box says — but with Mann's own caveat, which the chart drops.\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"Pokorny pp.660–661, s.v. legʷh- (POK_02.txt leaves 320–321)\", \"stance\": \"contradicts\",\n    \"note\": \"«legʷh- 'leicht in Bewegung und Gewicht', verbal 'sich leicht, flink bewegen', nasaliert lengʷh- ... av. rənjaiti, rənjayeiti 'macht leicht, flink, läßt sich bewegen', ai. ráṃhate, ráṃghati 'rinnt, eilt, springt auf'». No root *lang- 'droop, be sad' exists in Pokorny.\"},\n   {\"src\": \"CHEUNG\", \"where\": \"Cheung 2007 p.191 s.v. *Hranj\", \"stance\": \"contradicts\",\n    \"note\": \"«*Hranj 'to take action, spur, urge (often with negative consequences)?' ... « PIE *h₁lengʷʰ- 'to spur, impel, incite' — LIV: 247 | Pok.: 660 f.» with YAv. rənjaiti, MMP rnz, Parth. rnj, NP ranjidan, Skt. ramh- 'to hasten'. Greek λαγγάζω is not among the cognates.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. legʷh- (AHD_watkins1985.txt l.668)\", \"stance\": \"contradicts\",\n    \"note\": \"«legwh-. Light, having little weight ... [Pok. legʷh- 660.]» — Watkins knows only the 'light' root at Pokorny 660; there is no AHD root meaning 'droop, be sad'.\"},\n   {\"src\": \"WLD\", \"where\": \"Walde-Pokorny (WLD_band3 index; Bd. II)\", \"stance\": \"silent\",\n    \"note\": \"no root *lang- 'droop, be sad' in the Walde-Pokorny register; the material at WP II 426 f. is the 'light' root legʷh- referred to by Pokorny.\"}\n ],\n \"nodes\": []\n}\n\ne1[\"nodes\"].append({\n \"id\": 1, \"lang\": \"Sanskrit\", \"words\": \"rdjyate\",\n \"verdict\": \"disputed\",\n \"derivation\": (\"Three things are wrong here. (i) The form: 'rdjyate' is not a possible Sanskrit transliteration; the \"\n   \"600-dpi render of pdf page 302 shows the book itself prints 'rdjyate' with a plain d, so the extraction is faithful \"\n   \"and the misprint is Nourai's. What he is reproducing is Mo'in's footnote to رنج in Borhan-e Qate' («... از سانسکریت \"\n   \"rjyate (در اضطراب شدن)»), i.e. Sanskrit रज्यते rajyate. (ii) The gloss: Monier-Williams gives rajyate (passive/middle \"\n   \"of रञ्ज् rañj) as 'to be dyed or coloured, redden, glow' and 'to be affected or moved, be excited or glad, be charmed \"\n   \"or delighted', and the intensive rārajyate 'to be greatly excited, exult' — nowhere 'to be in pain'. Mo'in's Persian \"\n   \"«در اضطراب شدن» ('to become agitated') renders the second sense, and Nourai has hardened it into 'pain'. (iii) The \"\n   \"arrow: rañj- belongs to PIE *(s)reg- 'to dye' (Gk. ῥέζω), a completely different root, and in any case an Iranian \"\n   \"word cannot descend from a Sanskrit one — the two are sister languages. Modern work (Cheung 2007: 191) makes MP ranj \"\n   \"a native Iranian continuant of *Hranj- < PIE *h₁lengʷʰ-, whose Indic cognate is ráṃhate 'to hasten', not rajyate.\"),\n \"derivation_fa\": (\"این گره سه اشکال دارد. نخست صورت واژه: «rdjyate» آوانگاریِ ممکنی در سنسکریت نیست؛ بررسی تصویر ۶۰۰ نقطه‌ایِ \"\n   \"صفحهٔ ۳۰۲ نشان می‌دهد که خودِ کتاب همین را چاپ کرده، پس خطا از نویسنده است نه از خوانش اسکن. آنچه نورایی نقل می‌کند حاشیهٔ \"\n   \"معین بر «رنج» در برهان قاطع است: «از سانسکریت rjyate (در اضطراب شدن)»، یعنی रज्यते rajyate. دوم معنی: مونیه‑ویلیامز \"\n   \"rajyate را «رنگین/سرخ شدن» و «برانگیخته و شیفته شدن» معنی می‌کند، نه «درد کشیدن»؛ «در اضطراب شدنِ» معین برگردانِ معنیِ دوم \"\n   \"است و نورایی آن را به «درد» سخت کرده است. سوم جهت اشتقاق: ریشهٔ रञ्ज् به هندواروپاییِ *(s)reg- «رنگ کردن» می‌رسد و اصولاً \"\n   \"واژهٔ ایرانی از واژهٔ سنسکریت مشتق نمی‌شود، بلکه هم‌ریشه‌اند. پژوهش امروزی (چونگ ۲۰۰۷ ص ۱۹۱) «رنج» را دنبالهٔ ایرانیِ \"\n   \"*Hranj- می‌داند. پس پژوهش امروزی این گره را رد می‌کند.\"),\n \"error_in\": \"book\",\n \"book_prints\": \"rdjyate\",\n \"correct_form\": \"rajyate (Skt. रज्यते, passive of रञ्ज् rañj)\",\n \"sources\": [\"https://sanskrit.inria.fr/MW/214.html\", W+\"रञ्ज्\"],\n \"ref_check\": [\n   {\"ref\": \"BQT:963\", \"status\": \"partial\",\n    \"note\": \"The رنج / رنجه entries in Borhan-e Qate' vol. 2 (BQT_v2_pages.txt around l.24919–24992) carry Mo'in's footnote «رنجه، پهلوی [rnc] «باروچا ...» (غم، درد، ناراحتی)، در اوراق تورفان ranz (درد)، از سانسکریت rjyate (در اضطراب شدن)». So Mo'in does derive the Pahlavi from a Sanskrit rjyate — but he writes rjyate, not 'rdjyate', and glosses it «در اضطراب شدن» ('to become agitated'), not 'to be in pain'. The printed page number could not be confirmed: BQT_v2_pages.txt carries no [pdf page] tags and ref_page.py has no scan covering printed p.963.\"}\n ],\n \"consulted\": [\n   {\"src\": \"CHEUNG\", \"where\": \"Cheung 2007 p.191 s.v. *Hranj\", \"stance\": \"contradicts\",\n    \"note\": \"The Indic cognate Cheung lists is «*SANSKRIT: ramh 'to hasten' (RV+) = EWAia II: 421 f., 473», not rajyate; and the Iranian forms are inherited, not borrowed from Indic.\"},\n   {\"src\": \"POK\", \"where\": \"Pokorny p.660 f.\", \"stance\": \"contradicts\",\n    \"note\": \"the Indic member of the root is «ai. ráṃhate, ráṃghati, láṅghati 'rinnt, eilt, springt auf, springt über'» — no rajyate.\"},\n   {\"src\": \"IEC\", \"where\": \"Mann p.663 s.v. lang-\", \"stance\": \"silent\",\n    \"note\": \"Mann's own entry for the root cites no Sanskrit at all, only Persian and Greek — so the Sanskrit node has no support in the reference Nourai uses for the root.\"}\n ]\n})\n\ne1[\"nodes\"].append({\n \"id\": 2, \"lang\": \"Pahlavi\", \"words\": \"ranz, ranj\",\n \"verdict\": \"plausible\",\n \"derivation\": (\"The two forms are exactly right and well attested: Book Pahlavi writes the noun <lnc> = ranj 'toil, \"\n   \"trouble' (MacKenzie, Concise Pahlavi Dictionary p.70: «ranj [lnc | P rnj, (M rnz), N ~] toil, trouble», with the \"\n   \"derivatives ranjag 'troubled', ranjēnīdan 'to trouble', ranjwar > NP ranjūr), while Manichaean Middle Persian, \"\n   \"written in a script that distinguishes the affricate from the sibilant, spells it rnz — hence Nourai's doublet \"\n   \"'ranz, ranj', which he takes from Mo'in's footnote ('in the Turfan leaves ranz'). Nyberg II p.171 has «ranj [lnc'] \"\n   \"trouble, toil, grief ... MPrth rnj; MPrs rnz; Paz. ranj, rand; NP ranj», linking it to the verb raxtan/ranj- 'to vex, \"\n   \"grieve, exhaust'. What is not right is the arrow: Middle Persian ranj is not derived from a Sanskrit word but \"\n   \"continues Old Iranian *ranj- (YAv. rənjaiti), the two Indo-Iranian branches being sisters. Hence 'plausible' — the \"\n   \"node's forms and glosses are correct, its parentage is not.\"),\n \"derivation_fa\": (\"هر دو صورت درست و گواهی‌شده‌اند: در پهلویِ کتابی اسم را <lnc> یعنی ranj می‌نویسند (مکنزی، فرهنگ کوچک پهلوی \"\n   \"ص ۷۰: «ranj [lnc] toil, trouble» با مشتقات ranjag، ranjēnīdan و ranjwar > رنجورِ فارسی)، و در فارسی میانهٔ مانوی که خط آن \"\n   \"«ج» و «ز» را جدا می‌نویسد، صورت rnz آمده است؛ همان دوگانهٔ «ranz, ranj» که نورایی از حاشیهٔ معین («در اوراق تورفان ranz») \"\n   \"گرفته است. نیبرگ (ج ۲ ص ۱۷۱) نیز «ranj ... MPrth rnj؛ MPrs rnz؛ پازند ranj, rand؛ فارسیِ نو رنج» را با فعل raxtan/ranj- \"\n   \"پیوند می‌دهد. آنچه درست نیست پیکانِ نمودار است: «رنجِ» فارسی میانه از سنسکریت نیامده، بلکه دنبالهٔ ایرانی باستان *ranj- \"\n   \"(اوستایی rənjaiti) است. پس صورت‌ها درست‌اند ولی نسبِ ترسیم‌شده نه.\"),\n \"sources\": [W+\"رنج\"],\n \"ref_check\": [\n   {\"ref\": \"BQT:963\", \"status\": \"supports\",\n    \"note\": \"Mo'in's footnote to رنجه (BQT vol.2, ر section, BQT_v2_pages.txt l.24992) reads «رنجه، پهلوی [rnc] «باروچا» (غم، درد، ناراحتی)، در اوراق تورفان ranz (درد) از سانسکریت rjyate (در اضطراب شدن)» — the Pahlavi forms ranj/ranz on the chart come straight from here.\"}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"MacKenzie, Concise Pahlavi Dictionary p.70 (PHD.txt l.557)\", \"stance\": \"supports\",\n    \"note\": \"«ranj [lnc | P rnj, (M rnz), N ~] toil, trouble. ~ag [-k' | N ~a] troubled. ranjēnīdan, ranjēn- [lncyn-ytn'] trouble.» and p.71 «ranjwar [lncwl | (M rnzwr), N ranjūr] troubled, distressed».\"},\n   {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II, glossary s.v. ranj (NYB_vol2_glossary.txt l.3240)\", \"stance\": \"supports\",\n    \"note\": \"«ranj [lnc'] trouble, toil, grief 13¹³. 56²⁹ etc. — MPrth rnj; MPrs rnz (A-H II), rnzwr 'distressed' (S); Paz. ranj, rand; NP ranj. V. raxtan.»\"},\n   {\"src\": \"CHEUNG\", \"where\": \"Cheung 2007 p.191\", \"stance\": \"partial\",\n    \"note\": \"«*MIDDLE PERSIAN: BMP lncyn- /ranj-/ ... MMP rnz 'toil, labour, trouble' ... *PARTHIAN: rnj» — same forms, but as inherited Iranian, not from Sanskrit.\"}\n ]\n})\n\ne1[\"nodes\"].append({\n \"id\": 3, \"lang\": \"Persian\", \"words\": \"ranj; ranjândan\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"New Persian رنج ranj 'pain, toil, suffering' is the regular continuation of Middle Persian ranj (<lnc>) — \"\n   \"an unchanged inheritance, since MP -anj gives NP -anj directly; Wiktionary states 'Inherited from Middle Persian lnc \"\n   \"/ranǰ/ \\\"toil\\\"' citing MacKenzie 1971: 70. The derivatives in the chart's parenthesis are all transparent: رنجور \"\n   \"ranjūr 'ill, afflicted' < MP ranjwar (ranj + -war 'bearing'), رنجبر ranjbar 'toiler, labourer' (ranj + bar- 'to \"\n   \"carry'), رنجش ranješ 'offence' (verbal noun in -eš), رنجیدن ranjīdan 'to be pained, take offence' (the intransitive), \"\n   \"and the causatives رنجاندن / رنجانیدن ranjāndan / ranjānīdan 'to hurt, offend', formed with the Persian causative \"\n   \"-ān- exactly as MP ranjēnīdan was formed with -ēn-. Cheung 2007: 191 lists NP ranjidan under *Hranj-. The Hafez \"\n   \"couplet Nourai prints ('نهال دشمنی برکن که رنج بیشمار آرد') is a standard attestation of the noun.\"),\n \"derivation_fa\": (\"«رنج» فارسیِ نو دنبالهٔ بی‌واسطهٔ «ranj» فارسی میانه (نوشتهٔ <lnc>) است؛ خوشهٔ ‑نج در گذر از فارسی میانه به \"\n   \"فارسی نو دگرگون نمی‌شود، ازاین‌رو صورت واژه یکسان مانده است (ویکی‌واژه، به نقل از مکنزی ۱۹۷۱ ص ۷۰). مشتقات داخل پرانتز نیز \"\n   \"همه روشن‌اند: «رنجور» از ranjwar پهلوی (رنج + ‑ور)، «رنجبر» (رنج + بردن)، «رنجش» (اسم مصدر با ‑ش)، «رنجیدن» (فعل لازم) و \"\n   \"«رنجاندن/رنجانیدن» که مانند ranjēnīdan پهلوی، سببیِ همان ستاک است، منتها با پسوند سببی‌سازِ ‑ان‑ فارسی نو. چونگ (۲۰۰۷ ص ۱۹۱) \"\n   \"نیز «رنجیدن» را ذیل *Hranj- می‌آورد. ادعای نورایی در این گره درست است.\"),\n \"sources\": [W+\"رنج\"],\n \"ref_check\": [\n   {\"ref\": \"MON:1676\", \"status\": \"partial\",\n    \"note\": \"Mo'in's Farhang has the expected entries (رنج، رنجش، رنجیدن، رنجاندن: e.g. MON_part1.txt l.2857 «رنجیدگی، رنجش، شکراب، اندوه، غم», l.2906 «رنجانیدن، رنجه کردن، گزند رسانیدن»), and Mo'in's own etymological footnote on the word is the BQT one quoted above; the 6-vol page 1676 itself cannot be verified because no scan of the six-volume edition exists (see refs_online.json s.v. MON).\"},\n   {\"ref\": \"IEC:663\", \"status\": \"supports\",\n    \"note\": \"Mann p.663 lists exactly «Per. ranja, ranjiš 'sorrow, annoyance'; ranjidan, inf. 'be sad'» — the Persian material of this node.\"}\n ],\n \"consulted\": [\n   {\"src\": \"CHEUNG\", \"where\": \"Cheung 2007 p.191, *NWIR section\", \"stance\": \"supports\",\n    \"note\": \"«NP ranjidan 'to exert effort', (old ppp.) raxtah 'wounded, ill', ranj 'effort' ... Ham. ränjayän/ränj- 'to be offended'».\"},\n   {\"src\": \"PHD\", \"where\": \"MacKenzie p.70–71\", \"stance\": \"supports\",\n    \"note\": \"gives the New Persian outcome explicitly with the tilde: «ranj [lnc | ... N ~]», «ranjwar ... N ranjūr».\"},\n   {\"src\": \"HRN\", \"where\": \"HRN.txt, grep 'ranj', 'randsch'\", \"stance\": \"silent\",\n    \"note\": \"Horn's Grundriss treats āranj 'elbow' (no. ~, phlv. āranj) and dranjītan (no. 71) but has no article on رنج itself.\"},\n   {\"src\": \"HUB\", \"where\": \"HUB.txt\", \"stance\": \"silent\", \"note\": \"Hübschmann's Persische Studien has no entry for رنج.\"}\n ]\n})\n\ne1[\"nodes\"].append({\n \"id\": 4, \"lang\": \"Greek\", \"words\": \"laggazô, laggeô\",\n \"verdict\": \"plausible\",\n \"derivation\": (\"Both Greek verbs exist, though they are rare glossary words rather than classical vocabulary. LSJ s.v. \"\n   \"λαγγάζω: 'to slacken', = ἐνδίδωμι (Antiph. 37), with Photius λαγγάζει· ὀκνεῖ 'he hesitates', Hesychius λαγγεῖ· ὀκνεῖ, \"\n   \"λαγγάσαι· περιφυγεῖν 'to escape', and the by-forms λαγγαρεῖ· ἀποδιδράσκει, λαγγεύει· φεύγει. Mann's gloss 'droop, \"\n   \"flag' is a fair rendering of 'slacken, hold back'. The problem is the affiliation: Mann himself files them beside \"\n   \"λαγαρός 'slack, sunken', and λαγαρός/λαγγάζω are today referred to the root *(s)leg- 'to be slack' (Pokorny s.v. \"\n   \"(s)lēg-, whence also Lat. langueō, laxus and Gk. λαγαίω 'release') — a root with no Iranian member and no connection \"\n   \"to Persian ranj. So the words and the sense are right, but they belong to the chart only because Mann's ad hoc *lang- \"\n   \"yoked them to the Persian branch.\"),\n \"derivation_fa\": (\"هر دو فعل یونانی واقعی‌اند، هرچند واژه‌هایی نادر و بیشتر فرهنگ‌نامه‌ای‌اند تا کلاسیک. لیدل‑اسکات ذیل \"\n   \"λαγγάζω می‌آورد «to slacken» (= ἐνδίδωμι، آنتیفانس ۳۷)، و فوتیوس و هزیخیوس صورت‌های λαγγεῖ «درنگ می‌کند»، λαγγάσαι \"\n   \"«گریختن»، λαγγεύει «می‌گریزد» را ثبت کرده‌اند؛ پس معنیِ «افسردن/سست شدن» که مان داده تقریباً درست است. اشکال در نسب است: \"\n   \"خودِ مان این فعل‌ها را کنار λαγαρός «سست، فرورفته» می‌گذارد و امروز این خانواده را ذیل ریشهٔ *(s)leg- «سست بودن» \"\n   \"(پوکورنی، هم‌ریشه با languēo و laxus لاتین) می‌آورند، ریشه‌ای که هیچ عضو ایرانی ندارد و با «رنج» بی‌ارتباط است. پس \"\n   \"واژه‌ها درست‌اند اما پیوندشان با شاخهٔ فارسی تنها بر ساختهٔ مان استوار است.\"),\n \"sources\": [\"https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A1999.04.0057%3Aentry%3Dlagga%2Fzw\"],\n \"ref_check\": [\n   {\"ref\": \"IEC:663\", \"status\": \"supports\",\n    \"note\": \"Mann p.663: «Gk. laggázo, laggéo 'droop, flag' beside lagarós, adj. 'sunken, slack'» — the node reproduces Mann exactly (IEC.txt leaf 373).\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"Pokorny, (s)lēg- 'schlaff sein' (pp.~959 f.); legʷh- pp.660 f.\", \"stance\": \"contradicts\",\n    \"note\": \"Pokorny places the λαγαρός / λαγγ- family with the 'slack' root, and puts no Greek verb of this shape under the 'light/quick' root that carries the Iranian ranj-material at pp.660 f. (POK_02.txt leaves 320–321).\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985, root index\", \"stance\": \"silent\",\n    \"note\": \"no root corresponding to Greek λαγγάζω appears in the AHD appendix (the appendix indexes only roots with English reflexes).\"},\n   {\"src\": \"SYN\", \"where\": \"Buck, Dictionary of Selected Synonyms\", \"stance\": \"silent\",\n    \"note\": \"Buck's chapters on 'pain, grief, sorrow' do not connect Greek λαγγάζω with Persian ranj.\"}\n ]\n})\ndoc[\"entries\"].append(e1)\n\n# ---------------------------------------------------------------- entry 3\ne3 = {\n \"entry\": 3,\n \"root\": \"Laqalaqa\",\n \"verdict\": \"plausible\",\n \"modern_form\": \"Akkadian laqlaqqu (also raqraqqu) 'stork', an onomatopoeic bird-name; the Arabic and Persian words are either borrowed from it (possibly through Aramaic) or independent imitations of the same clatter\",\n \"note\": (\"The Akkadian word is real and means 'stork': CAD registers laqlaqqu / raqraqqu, and Assyrian Neo-Aramaic has \"\n   \"ܠܲܩܠܵܩܵܐ laqlāqā. Nourai's headword-shape 'Laqalaqa' follows Zimmern's own spelling (AKD p.52: «akk. laqalaqa ein \"\n   \"Vogel»); Lokotsch no.1294 writes it «ass. lakalaka» after Delitzsch HWB 885a. Two caveats keep this from being \"\n   \"'confirmed'. (i) The gloss 'flamingo, stork' is not Zimmern's: on p.52 he writes only «ein Vogel» ('a bird') and the \"\n   \"word 'Weihe od. ä.' ('kite or similar') on that line belongs to the preceding entry. (ii) The very reference Nourai \"\n   \"cites doubts the arrow: Zimmern continues «fraglich, ob dazu arab. laqlaq 'Storch' gehört, oder beiderseits \"\n   \"unabhängig ein onomatop. Name vorliegt» — 'it is questionable whether Arabic laqlaq belongs with it, or whether an \"\n   \"onomatopoeic name arose independently on both sides'. Lokotsch takes the second view outright. Wiktionary is \"\n   \"cautious in the same way ('possibly came from Akkadian via unattested Aramaic'). So the Akkadian root box is a \"\n   \"reasonable but not a demonstrated starting point.\"),\n \"note_fa\": (\"واژهٔ اکدی واقعی است و «لک‌لک» معنی می‌دهد: فرهنگ آشوریِ شیکاگو (CAD) صورت‌های laqlaqqu و raqraqqu را ثبت \"\n   \"کرده و در آرامیِ نوِ آشوری نیز ܠܲܩܠܵܩܵܐ آمده است. املای «Laqalaqa» در کتاب از خودِ زیمرن گرفته شده (ص ۵۲: «akk. laqalaqa \"\n   \"ein Vogel») و لوکوچ (شمارهٔ ۱۲۹۴) آن را «ass. lakalaka» می‌نویسد. اما دو نکته مانع پذیرشِ کاملِ ریشه است: نخست آنکه معنیِ \"\n   \"«فلامینگو، لک‌لک» از آنِ زیمرن نیست؛ او تنها «ein Vogel» (پرنده‌ای) نوشته است. دوم آنکه همان مأخذِ مورد استناد در درستیِ \"\n   \"پیکان تردید می‌کند: «تردیدآمیز است که آیا laqlaqِ عربی به آن مربوط است یا در هر دو سو نامی آوایی (onomatopoeic) به‌طور \"\n   \"مستقل پدید آمده است». لوکوچ نیز همان دیدگاه دوم را می‌پذیرد. پس ادعای نورایی با احتیاط پذیرفتنی است.\"),\n \"sources\": [W+\"لقلق\", W+\"لک‌لک\"],\n \"ref_check\": [\n   {\"ref\": \"AKD:52\", \"status\": \"partial\",\n    \"note\": \"Zimmern, Akkadische Fremdwörter (1917) p.52 (AKD.txt leaf 61): «akk. laqalaqa ein Vogel : fraglich, ob dazu arab. laqlaq Storch gehört, oder beiderseits unabhängig ein onomatop. Name vorliegt». The page has the word and the Arabic comparison, but explicitly leaves the derivation open — and does not gloss the Akkadian word 'flamingo, stork'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"LKT\", \"where\": \"Lokotsch no. 1294\", \"stance\": \"contradicts\",\n    \"note\": \"«Ar. laklak: 'Storch' [onomatopoetische Bildung nach dem Klappern des Schnabels, ebenso wie ass. lakalaka Del HWB 885a], ebenso tk. leklek, vulg. lejlek ... hieraus rum. liliac, serb. lelek, russ. leklek» — Lokotsch derives Arabic and Assyrian independently from the bill-clatter, i.e. no borrowing chain.\"},\n   {\"src\": \"FVQ\", \"where\": \"FVQ_pages.txt, grep لقلق\", \"stance\": \"silent\", \"note\": \"not a Qur'anic word; Jeffery has no entry.\"},\n   {\"src\": \"AFM\", \"where\": \"Addi Shir, ل section pp.141–142 (AFM.pdf pdf-pages 143–144)\", \"stance\": \"silent\",\n    \"note\": \"the only near headword is «( اللَقَانِق ) ... اسم لأحد الأمعاء» (a sausage/intestine word); Addi Shir does not treat لقلق, i.e. he does not regard it as a Persian loan in Arabic.\"}\n ],\n \"nodes\": []\n}\n\ne3[\"nodes\"].append({\n \"id\": 1, \"lang\": \"Arabic\", \"words\": \"laqlaq; laqlaqeh\",\n \"verdict\": \"plausible\",\n \"derivation\": (\"Arabic لَقْلَق laqlaq (pl. لقالق laqāliq) 'stork' is a reduplicated CaCCaC form of the kind Arabic uses \"\n   \"for animal cries and noisy things, and لَقْلَقَة laqlaqa is its regular maṣdar, 'clattering, clacking' — used both of \"\n   \"the stork's bill-clatter and, figuratively, of loud empty talk (Mo'in: «لقلقه [ع. لقلقة] (مصدر) سخت آواز کردن؛ آواز \"\n   \"لکلک ... فصاحت عاری از بلاغت» — 'eloquence devoid of rhetoric'). Wiktionary compares Akkadian laqlaqqu and Persian \"\n   \"lak-lak and suggests the word 'possibly came from Akkadian via unattested Aramaic'; Neo-Aramaic laqlāqā would be the \"\n   \"missing link. Zimmern (the reference cited) leaves open whether Arabic borrowed it or coined it independently from \"\n   \"the same sound, and Lokotsch no.1294 opts firmly for independent onomatopoeia. Since a reduplicated bird-cry name \"\n   \"can arise anywhere, the borrowing arrow is likely but not provable — 'plausible'.\"),\n \"derivation_fa\": (\"«لَقْلَق» عربی (جمع: لقالق) «لک‌لک» بر وزنِ مکرّرِ فَعْلَل است، همان الگویی که عربی برای بانگِ جانوران و \"\n   \"صداهای پرهیاهو به کار می‌برد، و «لَقْلَقَة» مصدرِ قاعده‌مندِ آن است: «سخت آواز کردن، آوازِ لک‌لک» و به‌طور مجازی «سخنِ \"\n   \"بیهوده» (معین: «فصاحتی عاری از بلاغت»). ویکی‌واژه آن را با اکدی laqlaqqu و فارسی «لک‌لک» می‌سنجد و احتمال می‌دهد که از \"\n   \"راهِ آرامیِ گواهی‌نشده از اکدی گرفته شده باشد؛ صورت آرامیِ نو ܠܲܩܠܵܩܵܐ حلقهٔ گمشده است. اما زیمرن (همان مأخذی که نورایی \"\n   \"آورده) در وام‌گیری تردید می‌کند و لوکوچ آن را ساختی آوایی و مستقل می‌داند. چون چنین نام‌های آوایی در هر زبانی جداگانه \"\n   \"می‌توانند پدید آیند، این پیکان محتمل است ولی اثبات‌ناشدنی؛ یعنی با احتیاط پذیرفتنی.\"),\n \"sources\": [W+\"لقلق\"],\n \"ref_check\": [\n   {\"ref\": \"AKD:52\", \"status\": \"partial\",\n    \"note\": \"Zimmern p.52 raises the Arabic word only to question the connection: «fraglich, ob dazu arab. laqlaq Storch gehört, oder beiderseits unabhängig ein onomatop. Name vorliegt» (AKD.txt leaf 61).\"},\n   {\"ref\": \"MON:3616\", \"status\": \"supports\",\n    \"note\": \"Mo'in s.v. لقلقه (MON_part2.txt l.39947): «لقلقه: [ع. لقلقة] (مصدر) سخت آواز کردن؛ آواز لکلک ... آوازی همراه با جنبش و اضطراب؛ فصاحت عاری از بلاغت» — the Arabic origin tag [ع.] and both senses Nourai gives. The 6-vol page number itself is unverifiable (no scan of the six-volume Farhang exists).\"}\n ],\n \"consulted\": [\n   {\"src\": \"LKT\", \"where\": \"no. 1294\", \"stance\": \"contradicts\",\n    \"note\": \"«Ar. laklak: 'Storch' [onomatopoetische Bildung nach dem Klappern des Schnabels, ebenso wie ass. lakalaka]» — independent creation, not a loan.\"},\n   {\"src\": \"AFM\", \"where\": \"Addi Shir ل section (pp.141–142)\", \"stance\": \"silent\",\n    \"note\": \"no entry for لقلق — Addi Shir does not list it among the Persian loans in Arabic, consistent with the word being Semitic.\"},\n   {\"src\": \"PLA\", \"where\": \"Asbaghi p.241–242 (PLA_pages.txt leaves 255–256)\", \"stance\": \"silent\",\n    \"note\": \"Asbaghi's ل section runs لجام, لقن, لخلخه, لعل, لاله, لكن, لهراسب, لوبيا, لوز, لوزينج, ليلك, ليمون — لقلق is absent, i.e. he does not treat it as a Persian loan either.\"}\n ]\n})\n\ne3[\"nodes\"].append({\n \"id\": 2, \"lang\": \"Persian\", \"words\": \"laklak, laqlaq; laqlaqeh\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"NP لک‌لک laklak 'stork' (with the variants لقلق laqlaq and لغلغ laġlaġ that the chart's script field \"\n   \"records) is the Arabic word taken into Persian, the Arabic qāf being domesticated to k in the everyday form — hence \"\n   \"the doublet laklak (popular) beside laqlaq (learned, straight from the Arabic spelling). Mo'in states the whole chain \"\n   \"in his footnote to Borhan-e Qate' p.1902: «و نیز لکلک > لگلگه (ه.م.) < لقلق (عر). اکدی laqlaqu (نام پرنده) (زیمرن، \"\n   \"لغات دخیلهٔ اکدی ص۵۲)؛ پرنده‌است از درازپایان با گردن و پای دراز سفیدرنگ با بالهای سیاه که در بهار بر بالای خانه‌های بلند \"\n   \"یا درختان لانه سازد» — Persian laklak from Arabic laqlaq, from Akkadian, citing the very Zimmern page Nourai cites. \"\n   \"لقلقه laqlaqeh 'idle chatter, slang speech' is the Arabic maṣdar in its Persian use, with the by-form لغلغه (Mo'in: \"\n   \"«لغلغه [= لکلکه] (اِ.) سخن بیهوده، گفتار هرزه»); the Sanā'i couplet Nourai prints uses it in exactly that sense. From \"\n   \"Persian the bird-name went on to Ottoman Turkish leylek.\"),\n \"derivation_fa\": (\"«لک‌لک» فارسی (با گونه‌های «لقلق» و «لغلغ» که در نمودار آمده) همان واژهٔ عربی است که به فارسی راه یافته و \"\n   \"«ق» عربی در صورت عامیانه به «ک» بدل شده؛ ازاین‌رو دوگانهٔ «لک‌لک» (عامیانه) در برابر «لقلق» (کتابی، بر پایهٔ املای عربی). \"\n   \"معین در حاشیهٔ برهان قاطع ص ۱۹۰۲ همهٔ زنجیره را می‌آورد: «و نیز لکلک > لگلگه < لقلق (عر). اکدی laqlaqu (نام پرنده) \"\n   \"(زیمرن، لغات دخیلهٔ اکدی ص ۵۲)». «لقلقه» نیز مصدر عربی است که در فارسی به معنی «سخن بیهوده» به کار رفته، با گونهٔ «لغلغه» \"\n   \"(معین: «لغلغه [= لکلکه] سخن بیهوده، گفتار هرزه»)؛ بیت سنایی که نورایی آورده دقیقاً همین معنی را دارد. از فارسی این \"\n   \"نامِ پرنده به ترکی عثمانی (leylek) رفته است. ادعای نورایی درست است.\"),\n \"sources\": [W+\"لک‌لک\", W+\"لقلق\"],\n \"ref_check\": [\n   {\"ref\": \"BQT:1902\", \"status\": \"supports\",\n    \"note\": \"Borhan-e Qate' p.1902 has the entries «لکلک ... لکلکه - بضم هر دو لام بروزن وسوسه: سخنان هرزه و بیهوده باشد» with Mo'in's fn.5 «و نیز لکلک * لگلگه (ه.م.) < لقلق (عر). اکدی laqlaqu (نام پرنده) (زیمرن، لغات دخیلهٔ اکدی ص۵۲)». Read via ref_page.py BQT:1902 (pdf page 699 of BQT_v3_picofile.pdf); image and OCR at data/verification/sources/refs/ocr/BQT/1902.png/.txt.\"}\n ],\n \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"s.v. لکلک and لغلغه (MON_part2.txt ll.40087, 40090)\", \"stance\": \"supports\",\n    \"note\": \"«لکلک [... معر. لقلق] (اِ.) (جانورشناسی) پرنده‌ای است از راستهٔ پابلندان ...» and «لغلغه: [= لکلکه] (اِ.) سخن بیهوده، گفتار هرزه» — both the bird and the 'idle talk' sense, with the Arabic connection.\"},\n   {\"src\": \"LKT\", \"where\": \"no. 1294\", \"stance\": \"partial\",\n    \"note\": \"records tk. leklek / lejlek and the Balkan reflexes from the same word, but explains the whole group as onomatopoeic rather than as a chain of loans.\"},\n   {\"src\": \"AKD\", \"where\": \"Zimmern p.52\", \"stance\": \"partial\",\n    \"note\": \"supplies the Akkadian end-point that Mo'in's footnote cites, while doubting the link (see the root's ref_check).\"}\n ]\n})\ndoc[\"entries\"].append(e3)\n\nwith io.open(\"data/verification/page-302.json\", \"w\", encoding=\"utf-8\") as f:\n    json.dump(doc, f, ensure_ascii=False, indent=2)\n    f.write(\"\\n\")\nprint(\"written\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build302.py",
 "description": "Build page-302.json"
}
```


### [2026-09-06T23:11:19.014Z] TOOL RESULT

```
written
```


## [2026-09-06T23:11:25.877Z] TOOL CALL #84: Bash

```json
{
 "command": "ls -la data/verification/page-302.json && python3 -m json.tool data/verification/page-302.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 302",
 "description": "Validate and run verify_check"
}
```


### [2026-09-06T23:11:27.793Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 66974 Sep  6 19:11 data/verification/page-302.json
JSON OK
nodes verified: 13/13
node verdicts: {'confirmed': 6, 'plausible': 5, 'transcription_suspect': 1, 'disputed': 1}
root verdicts: {'confirmed': 1, 'disputed': 1, 'plausible': 1}
ref checks: {'partial': 7, 'supports': 12}
books consulted: {'supports': 10, 'partial': 9, 'silent': 17, 'contradicts': 4} | by book: {'MON': 5, 'LKT': 4, 'BQT': 3, 'CHEUNG': 3, 'HRN': 2, 'ARY': 2, 'PLA': 2, 'HJB': 2, 'AID': 2, 'POK': 2, 'PHD': 2, 'FRS': 1, 'KLN': 1, 'FVQ': 1, 'SKT': 1, 'IEC': 1, 'NYB': 1, 'HUB': 1, 'AHD': 1, 'SYN': 1, 'AFM': 1, 'AKD': 1}
```


## [2026-09-06T23:11:40.641Z] TOOL CALL #85: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== FRS لاله سار ===\"; grep -n \"لاله سار\\|لالهسار\\|لاله‌سار\\|لالس\" FRS_pages.txt | head\necho \"=== ARY لالک/لعل ===\"; grep -n \"لالک\\|لعل\" incoming/ARY/ARY_pages.txt | head\necho \"=== FVQ la'l/laqlaq ===\"; grep -n -i \"la'l\\|laql\\|laʿl\" FVQ_pages.txt | head\necho \"=== HUB ranj ===\"; grep -n -i \"randsch\\|ranǰ\\|ranj\" HUB.txt | head\necho \"=== SYN pain/grief lagg ===\"; grep -n -i \"laggazo\\|λαγγ\\|ranj\" SYN.txt | head\necho \"=== WLD band3 lang ===\"; grep -n -i \"^lang-\\|lang- \" WLD_band3.txt | head",
 "description": "Verify the 'silent' claims"
}
```


### [2026-09-06T23:11:40.760Z] TOOL RESULT

```
=== FRS لاله سار ===
7320:‫خروشان ‪,‬همشارك! و لاله سار‬            ‫پراگنده بامشکدم سنک خوار‬
15415:                             ‫لالس‬         ‫ی‬       ‫رف‬              ‫‪1‬‬
=== ARY لالک/لعل ===
3212:۹ فریزی کین (زنلعلم ضام: 880001۸ گالی (ب3لتلا0۸): ۸۸
6840:بلوچی (1للعلاءلم8): اند انا آلبانی (4(مشتم: شاهاة شیر
13075:ایتالیایی (/(0744): ها00 6 (31380۸5) :23/لعل مهر
=== FVQ la'l/laqlaq ===
7040:" A page of writing from Laqlt to whatever lyadites are in al-Jazirah." l
=== HUB ranj ===
893:') Vullers giebt biranj neben birinj an, aber auoh die Lehn-
4377:^ewordeii ware und beziohe mich auf up. abranjan^ avranjan^ afravjan,
4378:baranjan (§ 62 und 72j *Armband* = arm. aparanjan *Armband' (5. Jhd.)
6010:mxmr Shk. 270, ranjur Fird. I, 501, 1128,
6132:ospnjfakan *Wirt'; abranjan 'Armband' = baranjan {dast-
6133:baranjan), arm. aparanjan (s. § 3); azbar oben' — zabar
6228:Vein*, phi. apecak oder apejak; abranfan *Spange* = avranjan
6309:afgh. kasap ; fdm *Schuld* = vam s. § 66 ; afranjan = avran-
6327:aparanfan 'Arrnband* = np. abranjan ^), dasUbaranJan ; apa-
6350:*) Auch afranjan (JRA.8. 1894, 443), avranjan (Vis u Ramin
=== SYN pain/grief lagg ===
10327:Pol. farbowad (barwié) Russ. krasit’ Skt. ranjaya-
29539:SCr. prijevara, fr. vb. prevariti ‘de- celve, cheat? (also varanje fr. vb. varati a Prob. : ChSl. variti ‘go before, an-
33838:Grk. — Eévos Goth. gasts Lith. svetimas NG tas ON gestr Lett.  sveSinieks Lat. —peregrinus, hospes, Dan. fremmed ChSl._ strantnit advena Sw. frémling SCr..  stranac, tudinac It. Sorestiere, straniero OE cuma, giest Boh.  cizinec Fr, étranger ME strangere, gest Pol. cudzoziemiec Sp. extranjero NE stranger Russ. éuzoj Rum. - siréin Du. _—_—vreemdeling Skt. _ vatdecika-, videcin- Ir, echirann OHG  gast NIr. — duine iasachta MHG gast, vremdelinc W. _—dieithr, estron NHG fremde(r), fremdling Br. estren, diavesiad, divroad
33850:It. straniero, Fr. étranger (> Sp. er- tranjero), derivs. of It. strano, Fr. étrange ‘strange’, fr. Lat. extraneus (mostly post-Aug.) ‘external, strange, foreign’, also sb. ‘stranger’ : extré ‘on the out- side, without’, exter ‘from without, for-
33860:Br. estranjour, fr. OF r. estrange, Fr. étranger (above, 2).
35127:WARFARE 1405 20.36 TOWER Grk. bpyos, rbpots Goth. kélikn Lith. bok3tas NG arbpyos ON turn Lett. turnis Lat. turris Dan. taarn ChSl.  stlitptt, syn It. torre Sw. torn SCr. toranj Fr. tour OE stépel, stypel, torr Boh. vé Sp. torre ME ltoure Pol. wieza Rum. turn NE tower Russ. bainja Ir. tor, tur Du. toren NIr. tor, tar OHG  turri W. twr MHG turn Br. tour NHG turm
35133:MHG, MLG torn, turn, Du. toren, fr. an OFr. torn (cf. Fr. tournelle ‘small tower’), a by-form or tor, tour by con- fusion with torn, tour ‘turning lathe’. MLG (or in part MHG) tom, turn > ON (late) turn, Dan. taarn, Sw. torn, Lett. tuornis, turnis, Rum. turn, SCr. toranj. MHG turm (beside turn), NHG turm, with m for n, as in MHG harm be- side harn ‘urine’, etc. Hence Lith. tur- mas (‘tower’ Kurschat; now dial. ‘jail’), Pol. turma ‘dungeon’, Russ. tjur’ma ‘prison, jail’ (21.39). Franck-v. W. 703. Falk-Torp 1239. Weigand-H. 2.1089. Kluge-G. 635 (but OFr. torn, not fr. Lat. acc, turrim).
=== WLD band3 lang ===
```


## [2026-09-06T23:11:57.318Z] TOOL CALL #86: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== FRS 7315-7325 ===\"; sed -n '7310,7326p' FRS_pages.txt\necho \"=== FRS 15405-15425 ===\"; sed -n '15405,15425p' FRS_pages.txt\necho \"=== HUB 6005-6015 ===\"; sed -n '6005,6015p' HUB.txt",
 "description": "Check FRS and HUB contexts"
}
```


### [2026-09-06T23:11:57.383Z] TOOL RESULT

```
=== FRS 7315-7325 ===
                         ‫کوارت بیارمکهورزد شیار [کذا ]‬


                          ‫هیا‬
                                          ‫براگاه باشد » اسدی کود ‪:‬‬
   ‫بگاه کهنیار هوشنگ شنگ‬              ‫بفر فریدون و هنگ نهنگ‬

                        ‫لاله ساز‬
                   ‫آواز » خطیری گوید ‪:‬‬          ‫ناممرغی است خوش‬

‫خروشان ‪,‬همشارك! و لاله سار‬            ‫پراگنده بامشکدم سنک خوار‬

                              ‫سا‬
               ‫ناممرغی است سخنکوی و سیاه» محلدی گوید ‪:‬‬
                       ‫آن زنگی زلفین بدان رنگین رخسار‬
               ‫چون سایراه‌است و‬
  ‫کل اندردهن سار‬
=== FRS 15405-15425 ===
                                  ‫لکُن‬
‫مانند طبقی بود و دیوارش بلند بود وازمس سازند » و دبگر شمعدان بود‬

                                                  ‫[رخی وید ‪:‬‬ ‫ف‬
                                 ‫ماهی‌بکش(در کش چوسی‌ین ستون‬




  ‫وشکسته چمی]‬       ‫لك‬    ‫هتان‬
                             ‫لالس‬         ‫ی‬       ‫رف‬              ‫‪1‬‬


 ‫‪ :- ۲‬چون ریا ک[ذا]‬            ‫‪ ۵ - ۱‬برن ستارة پروین است » سایر ی‬
‫گروشت دبای بود وخادنیز گویند (بدون‌شال) » س ‪ :‬زغن مرغ‬      ‫»فن م‬ ‫‪ - ۳‬ل ز‬
     ‫گوشت و موش ربای بود و خاد نگیوزیند ؛چ ‪ :‬زغن مرغ گوشت دبای بود‬
‫اهتغاریبود از روی بامس و هرچه‬            ‫‪۰ -‬‬          ‫وش و‬   ‫مما‬
                                                               ‫و ‪۰‬‬ ‫چ‪ -‬س‬ ‫‪4‬‬
 ‫بدان ماند » س ‪ :‬لکن طبقی ‪1۳‬دیوارش بلند از سیم و زر و مس و غیرها اوورا‬
‫شمعدان گویند» چ‪ :‬لکن‌تشتی بودسبمین‌با روبینوآ نچهبدین‌اند ‪٩‬‏ ‪ -‬کش یعنی بفل‬
 ‫بود ساخته در میان درختان ‪ ۰‬چ ‪ :‬چمن راه ساخته بود در‬   ‫ست‬
=== HUB 6005-6015 ===
ap. b (= w) entstandenen v (alter w) statt. So wird
-ewa- zu 5 in nek gut, seh5n* = phi. nevak, ap. naiba-
d. i. naiwa-);
ap. -a, -i, 'U -j- 'bara = -wara (vgl. § 75, b) = nip.
"'war, -war zu Ur (neben var) in vaxmr = paz.
mxmr Shk. 270, ranjur Fird. I, 501, 1128,
ganjur (skr. ganjavara-), dastUr = paz. dastur,
phi. dastuvar; muzdur, afgh. LW. mazdUr =
phi, muzduvar Gl. and Ind. 217; fl^^wr und a^^vor
^ phi. ^et?r Gl. and Ind. 16. Vgl. VuUers,
Grammatica ling. pers. p. 246 — 247.
```


## [2026-09-06T23:11:59.775Z] TOOL CALL #87: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"langueo\\|langueö\\|langue.,\\|Xayaqog\\|layaqog\\|Xayagog\\|lagai\\|Xayaiq\" POK_03.txt POK_full.txt | head -20\necho \"---- slēg- entry search\"\ngrep -n \"slēg-\\|släg-\\|(s)leg-\\|slög-\" POK_03.txt | head -20",
 "description": "Find Pokorny slack root"
}
```


### [2026-09-06T23:11:59.842Z] TOOL RESULT

```
POK_03.txt:2658:'IS  , schlaff,  weit,  geräumig',  nas.  langueö,  -ere,  ,matt,  schlaff,  ab- sein';
POK_full.txt:78257:Latin /axus's\ack, wide, capacious ', nasaNzea langueo, -ere "faint, languid, slacl<, 
POK_full.txt:90232:"humid, wet become', russ. volgnutb6s., ablaut. *udlga\v\ Old Church Slavic vlagai. " 
---- slēg- entry search
```


## [2026-09-06T23:12:12.980Z] TOOL CALL #88: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK_03 2645-2675 ===\"; sed -n '2645,2678p' POK_03.txt\necho \"=== POK_full 78240-78270 ===\"; sed -n '78248,78268p' POK_full.txt",
 "description": "Pokorny slack root context"
}
```


### [2026-09-06T23:12:13.047Z] TOOL RESULT

```
=== POK_03 2645-2675 ===
Igen,  hämmern'';  nur  irisch  und  orermanisch.
,  ..V..  ..    ^..^  j^.
cc  ^Schwerf^^  nir.  slacaire  , Schläger^  (mit  expressivem  -/^A:-);  mir. eschlagen''^  nir.  slaclit  m.  ;gute  Erscheinung,  von  gutem  Schlagt, daim  , schlage  mit  dem  Hammer^^  slachdan  ^Keule^ ; 'lAan,  aisl.  slä,  ags.  sleaii^  as.  ahd.  slahan  (sluoc,  sluogen,  geslagen) ahd.  slagon,  afries.  slagia  ds. ;  aisl.  slä  f.  , Stange,  Riegel'^  ags. a  jWeberkamm',  mhd.  sla^  dage  ,Schlagwerkzeug^,  mnd.  slawe lag'',  mhd.  slouice  ,Spur,  Fährte'  (^slagtcö);  dehnstufig  aisl.  slegr
g'  (*^ verschlagen^);  got.  slauhts  f.  , Schlachtung^  (*slk-ti-)]  aisl. lahd^,  slätr  L  ^Schlachtfleisch',  ahd.  slahta  ^Tötung,  Schlachtung';
Bedeutung  wie  nhd.  jemandem  nachschlagen,  Schlag  ,Art^:  ahd. del  geartet^,   gislahti  n.    , Stamm,    Eigenschaft'^    nhd.    Geschlecht.
706  f.,  Wissmann  Nomina  postverb.  74.
7o5-,  (s)lep-,  (s)lop-,  s.  oben  S.  655  ff.^  wozu  vielleicht  mir. xp  [p  =  b)y  lenah  {h  =  w)  , kleines  Kind''.
iQg-  und  {s)leg-  , schlaff,  matt  sein'  (aus  Joslassen'),  nas.  (s) leng- eng- , schaukeln,  schwanken^?);  sl9g-on-  , Herabhängendes' ;   aus
ff^  über  , weichlich'  auch  , wollüstig'.
xja-  ,lahm' ;  gr.  XjJ^'w  ,lasse  ab,  höre  auf  (*ermatte);  trans.  , mache
[*slegö),  aXXrjy,Tog  (*gX-)  , unaufhörlich',  Xay&ooai'  dcpsTvat  Hes., 'chlaff,  schmächtig,  dünn^,  hom.  laycoög,  ion.  Xayög,  att.  Xaycog,  -d) 's)ldg-öusos  ,mit  schlaffen  Ohren*),  Xaywv,  -ovog  gewöhnlich  PI. Jien,  Dünnen'  (formell  =  aisl.  Uiki  , Faltmagen'),  Xdyavov  , dünner ichen*  (formell  =  as.  laJcan  usw.  ,Tuch'),  XfxjydvLOv  , Wamme'  (vgl. iöJca  , schlaff  herabhängen'),  nasaliert  vermutlich  hierher  Xayycc^co Xayychv  , Zaudern',  Xayysvai '  cpevyat  Hes.  (*,matt  sein,  schlaff  und ^  sein') ;   mit   der   Bedeutung  ,Tvollüstig' :  Xdyvog  ,geil',  Xayvsveiv
sein',   Xayveia  , Geilheit,  Wollust',   Xujydg-    noQrrj    Hes.   (daneben
.  Xeyai  de  yvvatyisg  =  dy.öXaOTOi  ArchiL,  eXsyalvaiv  „daeXyalvsiv'^
'IS  , schlaff,  weit,  geräumig',  nas.  langueö,  -ere,  ,matt,  schlaff,  ab- sein';
(mit  expressivem  gg) , schlaff,  schwach';  mcymr.  llacc,  ncjmr.  Uac ammt  wegen  seines  cc  statt  ch  aus  engl,  slack; ik  , schlaff,  lose',  ndl.  lak,  nhd.  mdartl.  lack  ds.,  mndl.  lak  auch :,  aisl.  lakr  und  (vollstufig)  Wer  ^schlecht,  gering' ;  mit  Abtönung dial.  löka  , schlaff  herabhängen',  aisl.  lökr  , Dummkopf,  Faulpelz' ; ana- , baumelnder  Lappen.  Zipfel'  in  as.  lakan  ,Tuch',  ahd.  lahhan
960
#
ds.  (nhd.  Laken  aus  dem  Nd.,  formell  vgl.  gr.  Xayavov),  aisl.  lalcim.  ,Quan der  dritte  Magen  der  Wiederkäuer,  Faltmagen^  (=  Xaywv),  Mangel,  Fehl!.
mit  S-:   aisl.   5ZaÄ:r  ^schlaff"    (poet.),   slakna   ^erschlaffen',    as.    mn^,   ./^ ,schlaff,    schwach',    Fartiz.    as.    gislekit   , stumpf    gemacht',    mnd.    «Zaifc-uJ , Bauchseite'  (wie  laycbv  und  nhd.  Weichen),  ags.  sJ(SC  ^schlaff,  träge,  lan^^s^^t ahd.  slah-  ^schlaff,  träge',  ags.  sleccan  (*slekjan)  , schwächen';  *
mit  Abtönung  ö:  aisl.  slökr  ,ein  schlaffer  Bursche^norw.  slöken  ,schUff* schwed.  slöka  , schlaff  herabhängen  lassen',  dial.  ,träge  sein',  slök  und  (m^  jj släk  ^leichtsinniges  Weib',  aschwed.  slökifrip,  -frilla  ,Kebsweib';
nasaliert  wohl  schwed.  slinka  , nicht  fest  ansitzen,  schlottern,  hinken* ahd.  sUnc,  ndl.  slink  ,link',  mhd.  link,  nhd.  link]  ahd.  lenka  ,die  Linkft** schwed.  linka  und  lanka  ,etwas  hinken',  lunka  , langsam  gehen',  dän.  sZi^nii^ , schlaff,  schlotterig'  (*  schlaff  dahergehen');  vielleicht  schwed.  dial.  ilatik süddt.  schlank  ,Fetzen';
lett.  legens  , schlaff,  weich';  ,.
unsicher  russ.  pere-slega  , Fehler  im  Gewebe'  (*, Auslassen  des  Fadens'? ?1 sloven.  preslegast  , fadenscheinig,  kahl';
ob  auch  toch.  A  släkkär  , traurig'?
WP.  II  712  ff.,  WH.  I  7ö8f.
sleg^-  , drücken,  bedrücken,  mißhandeln' ;  slög^ä  , Plage'.
Gr.  X(bßrj  f.  , schimpfliche  Behandlung,  Schmach,  Mißhandlung,  Schaden^ Verderben',  Xcüßdojxai  , behandle  schimpflich,  mißhandle,  verstümmle,  frevle, schädige';
lit.  slogä  , Plage,  Landplage',  mit  sekundärem  Ablaut.:  lett.  sZä^a , Schaden, Beschwerde';  lit.  slogiis  , beschwerlich',  sloginti  ,plagen',  sluogal  , Hölzer zum  Beschweren  eingeweichten  Flachses';  mit  uo:  lit.  slüogas,  lett.  sluog$ jKlotz,  Stein,  Last',  sluodzit  ,beschweren,  niederpressen,  prügeln',  sluogdt^ sluoguot  ds. ;  mit  e:  lit.  sleg-iu,  -ti  , bedrücken,  pressen',  lett.  siegt  , schließen' (*,zudrücken'),  lit.  sUgtis,  siegte  , Presse,  Kelter',  lett.  at-slega  ,Schloß', slegs  , Bürde'.
WP.  II  714.
{s)leih-  , schlüpfrig,   gleiten'  s.  oben   S.   663;   dazu  vielleicht  (nach  Morris- Jones  WGr.  125)  cymr.  llithr  m.  ,das  Gleiten'  (*slib-tro-).
(s)leidh-  ^schlüpfrig,   gleiten';   Erweiterung  von   3.  lei-,  slei-  ohen  S.  662 f,
Ai.   sredhati  , gleitet   ab,    geht    fehl,    irrt';    gr.    öhaMvco,    Aor.    Öjlta^Of
,gleite',  dXta^TjQÖg  ,schlüpfrig',  HXio&og  m.  ,Glätte,  Schlüpfrigkeit'  (Hidh-to-t)
beruhen  auf  einem  -dhö-  oder  -tö-  Präsens ;  Anlaut  wie  in  dXißQÖg  von  der
=== POK_full 78240-78270 ===
Awyaviov " dewlap ' (compare Swedish s/o/ra "schlaff herabhangen'), nasalized 
presumably here Aayya^u) " hesitate ', Aayycbv "Zaudern', Aayysuai cpsuyai Hes. (*"faint, 
languid sein, schlaff and unschliJssig sein'); with the meaning " lustful ': ka\/\/oq "horny, 
lustful', AayvEusiv " lustful sein', Aayvsia "lust, desire, sensuality, voluptuousness', Awyaq 
nopvri Hes. (besides with e-Vok. Asyai 5s YuvaiKzq = aKoAaaroi Archil., sAsyaivEiv 
"aasAyaivsiv' EM.; 



Latin /axus's\ack, wide, capacious ', nasaNzea langueo, -ere "faint, languid, slacl<, 
abgespannt sein'; 

Old Irish /ace (with expressive gg) "slack, weak'; mcymr. Ilacc, ncymr. //ac "slack' derives 
because of seines cc instead of c/7from engl. slack. 

Middle Low German /5/r"slack, loose ', Dutch lak. Modern High German Dialectal lack 
ds.. Middle Dutch laka\so " lustful ', Old Icelandic lakrav\6 (full grade) lakr^evW, bad, 
small'; with gradation d Swedish dial. /oAa "schlaff herabhangen'. Old Icelandic lokr^ 
blockhead, Faulpelz'; Germanic 7a/ra/7a-"baumelnder rag, corner, tail' in Old Saxon lakan 
"kerchief, cloth'. Old High German lahhanAs. (Modern High German Lakenirovn dem Low 
German, formal compare gr. Aayavov), Old Icelandic laklm. " tadpole, frog or toad larva ';
```


## [2026-09-06T23:12:29.262Z] TOOL CALL #89: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"لالس\" FRS_pages.txt FRS.txt | head\necho \"--- around headword list\"\nsed -n '15380,15418p' FRS_pages.txt",
 "description": "Check FRS لالس"
}
```


### [2026-09-06T23:12:29.326Z] TOOL RESULT

```
FRS_pages.txt:15415:                             ‫لالس‬         ‫ی‬       ‫رف‬              ‫‪1‬‬
--- around headword list
    ‫سکار او سرخرویی کنم‬                      ‫پدل گفت اکر جنکجویی کنم‬

   ‫که بی سربببنند خسته تنم ]‬                 ‫و میهنم‬        ‫‪۸‬‬   ‫بنگریند مر دوده‬

‫‪ - ۱‬چ؛ زابفنتهدد باشد و بیمدادنکسی را بگفتار و اشارت » س ‪ :‬زلبفن تهدد‬

       ‫‪ - ۲‬چ ؛ عنصری و س نامقائلرا ندارد ‪.‬‬                 ‫باشد ‪+‬ن ‪ :‬زلیفننهدید بود‬
 ‫ّسخ‪:‬ی‪ ۰‬‏ ‪ - 4‬چ؛ روئین نایروئین باشد[کذا؛ ] س مثلمتن ‪ +‬ن‪.‬‬         ‫‪-‬س‬‫‪۳‬ر‬‫ف‬
 ‫یده بوده‬  ‫ش عسجدی افزصيك‬    ‫یببت‬
                                ‫پتبا‬‫اين‪,‬لفت را ندارد ‪ ۵ .۰‬ظ‪-‬اهراً اين بی‬
 ‫‪ : 7‬میهن خان و مان و وطن بود» سس ؛ میهن جای باشد و خان و مان و زاد‬
‫‪ - ۷‬نامقاثلدر س که‌فقط بیت‬    ‫وپوم وخوش » چ ‪ ۰‬میهن‌خان ومانوجای زادبود‬

                             ‫‪- ۸‬یی؛ بگرید مرا دوده ‪.‬‬                ‫دوم را دارد نیست‬
                                   ‫پردا‬
                                              ‫پروین بود [فرخی گوید‬
 ‫تا چو خورشید نباشد ناهید ‪ .‬چون‌دوپیکر؟ نبودنجم پرن ]‬
                                   ‫‪۳‬‬    ‫سای‬


                                       ‫زغعن‬

                         ‫و خاد مرخگوشت ربای بود[ روذکی کوید ‪:‬‬
‫کرث برسان ز غی]‬
              ‫جله صید این جهانیم ای پسر ماچوصعوه؛ م‬
                                  ‫لکُن‬
‫مانند طبقی بود و دیوارش بلند بود وازمس سازند » و دبگر شمعدان بود‬

                                                  ‫[رخی وید ‪:‬‬ ‫ف‬
                                 ‫ماهی‌بکش(در کش چوسی‌ین ستون‬




  ‫وشکسته چمی]‬       ‫لك‬    ‫هتان‬
                             ‫لالس‬         ‫ی‬       ‫رف‬              ‫‪1‬‬


 ‫‪ :- ۲‬چون ریا ک[ذا]‬            ‫‪ ۵ - ۱‬برن ستارة پروین است » سایر ی‬
```


## [2026-09-06T23:13:16.574Z] TOOL CALL #90: Bash

```json
{
 "command": "python3 - <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\np=\"data/verification/page-302.json\"\nd=json.load(open(p,encoding=\"utf-8\"))\nE={e[\"entry\"]:e for e in d[\"entries\"]}\n\n# --- entry 0, node 3: FRS\nn=[x for x in E[0][\"nodes\"] if x[\"id\"]==3][0]\nn[\"consulted\"]=[c for c in n[\"consulted\"] if c[\"src\"]!=\"FRS\"]\nn[\"consulted\"].append({\n \"src\":\"FRS\",\"where\":\"Asadi Tusi, Loghat-e Fors, s.v. لاله سار (FRS_pages.txt l.7317-7320)\",\"stance\":\"partial\",\n \"note\":\"«لاله سار: نام مرغی است خوش‌آواز» ('lāleh-sār: the name of a sweet-voiced bird'), with Khatiri's couplet «پراگنده بامشکدم سنگ‌خوار / خروشان همشارک و لاله‌سار» — this is the source Borhan's fn.9 cites, and it shows that the oldest attestation glosses the bird by its SONG, not by a red head; 'red-headed' is Mo'in's own inference from the compound (لاله 'red' + سار < سر 'head'), not an attested gloss.\"})\nn[\"derivation\"]=n[\"derivation\"].replace(\n \"citing Asadi Tusi and Hormozdnāme p.351.\",\n \"citing Asadi Tusi and Hormozdnāme p.351. It is worth noting that Asadi's own Loghat-e Fors glosses لاله سار merely as «نام مرغی است خوش‌آواز» 'a sweet-voiced bird', so 'red-headed' is Mo'in's inference from the compound rather than an attested sense.\")\nn[\"derivation_fa\"]=n[\"derivation_fa\"].replace(\n \"این همان ارجاع نورایی به ریشهٔ Ker 1 («سر») است و درست است.\",\n \"این همان ارجاع نورایی به ریشهٔ Ker 1 («سر») است و از نظر ساخت درست است؛ هرچند خودِ لغت فرسِ اسدی «لاله سار» را تنها «نام مرغی است خوش‌آواز» معنی کرده و «سرخ‌سر» استنباط معین از ساختِ واژه است.\")\n\n# --- entry 1 root: Pokorny 959 detail\nr=E[1]\nr[\"note\"]=r[\"note\"].replace(\n \"Greek λαγγάζω, by contrast, is grouped with λαγαρός 'slack' under *(s)leg- 'to be slack'.\",\n \"Greek λαγγάζω, by contrast, is put by Pokorny himself under a different root altogether — pp.959 f. «(s)lēg- und (s)leg- 'schlaff, matt sein'», where he writes «nasaliert vermutlich hierher λαγγάζω, λαγγών 'Zaudern', λαγγεύαι· φεύγειν Hes.» beside λαγαρός 'schlaff, schmächtig', Lat. laxus and langueō.\")\nr[\"note_fa\"]=r[\"note_fa\"].replace(\n \"یونانیِ λαγγάζω نیز امروز با λαγαρός «شل» زیر *(s)leg- می‌آید.\",\n \"یونانیِ λαγγάζω را نیز خودِ پوکورنی در صص ۹۵۹ـ۹۶۰ ذیل ریشهٔ دیگری، «(s)lēg-/(s)leg- سست و بی‌رمق بودن»، کنار λαγαρός «شل» و laxus و langueō لاتین آورده است.\")\nfor c in r[\"consulted\"]:\n    if c[\"src\"]==\"POK\":\n        c[\"where\"]=\"Pokorny pp.660–661 s.v. legʷh- and pp.959–960 s.v. (s)lēg-/(s)leg- (POK_02.txt leaves 320–321; POK_03.txt l.2645–2665)\"\n        c[\"note\"]=(\"p.660 f.: «legʷh- 'leicht in Bewegung und Gewicht', verbal 'sich leicht, flink bewegen', nasaliert lengʷh- ... \"\n                   \"av. rənjaiti, rənjayeiti 'macht leicht, flink, läßt sich bewegen', ai. ráṃhate, ráṃghati 'rinnt, eilt, springt auf'» — \"\n                   \"this is where the Iranian ranj-material belongs. pp.959 f.: «(s)lēg- und (s)leg- 'schlaff, matt sein' ... gr. λαγαρός \"\n                   \"'schlaff, schmächtig, dünn' ... nasaliert vermutlich hierher λαγγάζω, λαγγών 'Zaudern', λαγγεύαι· φεύγειν Hes. ... \"\n                   \"lat. laxus 'schlaff, weit, geräumig', nas. langueō» — this is where the Greek material belongs. Pokorny has no root \"\n                   \"*lang- 'droop, be sad', and the two branches Nourai joins are kept 300 pages apart.\")\n\n# --- entry 1, node 4: POK precise\nn4=[x for x in r[\"nodes\"] if x[\"id\"]==4][0]\nfor c in n4[\"consulted\"]:\n    if c[\"src\"]==\"POK\":\n        c[\"where\"]=\"Pokorny pp.959–960 s.v. (s)lēg-/(s)leg- 'schlaff, matt sein' (POK_03.txt l.2645–2665)\"\n        c[\"stance\"]=\"contradicts\"\n        c[\"note\"]=(\"«(s)lēg- und (s)leg- 'schlaff, matt sein' (aus 'loslassen') ... gr. λαγαρός 'schlaff, schmächtig, dünn' ... \"\n                   \"nasaliert vermutlich hierher λαγγάζω, λαγγών 'Zaudern', λαγγεύαι· φεύγειν Hes. (*'matt sein, schlaff und \"\n                   \"unschlüssig sein') ... lat. laxus 'schlaff, weit, geräumig', nas. langueō» — Pokorny assigns exactly these two \"\n                   \"Greek verbs to the 'slack' root, which has no Iranian member, and not to the root that carries Persian ranj.\")\nn4[\"derivation\"]=n4[\"derivation\"].replace(\n \"λαγαρός/λαγγάζω are today referred to the root *(s)leg- 'to be slack' (Pokorny s.v. (s)lēg-, whence also Lat. langueō, laxus and Gk. λαγαίω 'release')\",\n \"Pokorny pp.959 f. files exactly λαγγάζω, λαγγών 'Zaudern' and λαγγεύαι· φεύγειν under «(s)lēg- und (s)leg- 'schlaff, matt sein'», together with λαγαρός 'schlaff, schmächtig', Lat. laxus and langueō\")\nn4[\"derivation_fa\"]=n4[\"derivation_fa\"].replace(\n \"امروز این خانواده را ذیل ریشهٔ *(s)leg- «سست بودن» (پوکورنی، هم‌ریشه با languēo و laxus لاتین) می‌آورند\",\n \"پوکورنی نیز در صص ۹۵۹ـ۹۶۰ همین دو فعل را ذیل ریشهٔ «(s)lēg-/(s)leg- سست و بی‌رمق بودن» کنار λαγαρός و laxus و langueō لاتین آورده است\")\n\n# --- entry 1, node 3: HUB precise\nn3=[x for x in r[\"nodes\"] if x[\"id\"]==3][0]\nfor c in n3[\"consulted\"]:\n    if c[\"src\"]==\"HUB\":\n        c[\"where\"]=\"Hübschmann, Persische Studien, §75 b (HUB.txt l.6010)\"\n        c[\"stance\"]=\"partial\"\n        c[\"note\"]=(\"Hübschmann cites NP ranjūr only as a phonological example of the suffix -war > -ūr («vaxūr = paz. mxwr Shk. 270, \"\n                   \"ranjur Fird. I, 501, 1128, ganjur (skr. ganjavara-), dastūr ...»), which incidentally confirms ranjūr < ranj-war; \"\n                   \"he gives no etymology of رنج itself.\")\n\njson.dump(d, io.open(p,\"w\",encoding=\"utf-8\"), ensure_ascii=False, indent=2)\nio.open(p,\"a\",encoding=\"utf-8\").write(\"\\n\")\nprint(\"patched\")\nPYEOF\npython3 -m json.tool data/verification/page-302.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 302",
 "description": "Patch and revalidate"
}
```


### [2026-09-06T23:13:18.432Z] TOOL RESULT

```
patched
JSON OK
nodes verified: 13/13
node verdicts: {'confirmed': 6, 'plausible': 5, 'transcription_suspect': 1, 'disputed': 1}
root verdicts: {'confirmed': 1, 'disputed': 1, 'plausible': 1}
ref checks: {'partial': 7, 'supports': 12}
books consulted: {'supports': 10, 'partial': 11, 'silent': 15, 'contradicts': 4} | by book: {'MON': 5, 'LKT': 4, 'BQT': 3, 'CHEUNG': 3, 'HRN': 2, 'ARY': 2, 'PLA': 2, 'HJB': 2, 'AID': 2, 'POK': 2, 'PHD': 2, 'FRS': 1, 'KLN': 1, 'FVQ': 1, 'SKT': 1, 'IEC': 1, 'NYB': 1, 'HUB': 1, 'AHD': 1, 'SYN': 1, 'AFM': 1, 'AKD': 1}
```


## [2026-09-06T23:13:25.916Z] TOOL CALL #91: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 - <<'EOF'\nimport json\nd=json.load(open('data/verification/page-302.json',encoding='utf-8'))\ntxt=json.dumps(d,ensure_ascii=False)\nfor m in [\"959\",\"sweet-voiced\",\"§75 b\",\"λαγγών\",\"خوش‌آواز\"]:\n    print(m, txt.count(m))\n# check every node has the required fields\nfor e in d[\"entries\"]:\n    assert e.get(\"note_fa\"), e[\"entry\"]\n    for n in e[\"nodes\"]:\n        for f in (\"derivation\",\"derivation_fa\",\"ref_check\",\"consulted\",\"verdict\",\"words\",\"lang\"):\n            assert n.get(f), (e[\"entry\"],n[\"id\"],f)\n        assert len(n[\"consulted\"])>=2, (e[\"entry\"],n[\"id\"])\nprint(\"all fields present\")\nEOF\ngit status --short data/verification/page-302.json data/verification/sources/refs/ocr/AFM data/verification/sources/refs/ocr/BOOK",
 "description": "Final field check"
}
```


### [2026-09-06T23:13:28.632Z] TOOL RESULT

```
959 5
sweet-voiced 2
§75 b 1
λαγγών 4
خوش‌آواز 3
all fields present
 M data/verification/page-302.json
```


## [2026-09-06T23:13:34.187Z] TOOL CALL #92: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\ngit log --oneline -1 -- data/verification/page-302.json\ngit show HEAD:data/verification/page-302.json 2>/dev/null | head -20\necho \"=== status ===\"\ngit status --short | head -30\ncat .gitignore 2>/dev/null | head -20",
 "description": "Check prior version of page-302.json"
}
```


### [2026-09-06T23:13:34.262Z] TOOL RESULT

```
77e1808 Verify page 305 (Legwh/lâğar, light, carnival; Lěi/lây, slime); add blank box
{
  "pdf_page": 302,
  "book_page": 272,
  "verified_by": "claude-opus-5",
  "verified_on": "2026-09-06",
  "entries": [
    {
      "entry": 0,
      "root": "Lâl",
      "verdict": "confirmed",
      "modern_form": "New Persian لال lāl 'red; a red gemstone (ruby, spinel)' — a genuine Persian colour word of unknown ultimate origin",
      "note": "The root box is right on every point that it actually asserts: لال lāl is a New Persian word meaning 'red' (and, as a noun, 'ruby / balas spinel'), and the whole family on this page hangs together. Borhan-e Qate' p.1879 s.v. لال: 'معروف است ... و رنگ سرخ را نیز گفته‌اند - و بمعنی لعل هم آمده است ... و بعضی گویند لعل معرب لال است', with Mo'in's footnote 7 «لعل معرب «لال» است «نخبه ۱۶»؛ «لال» لعل باشد «لغت فرس ۳۲۹»»; Mo'in's own Farhang s.v. لال ۳ has '[قس. لاله، آلاله، لعل، معر.] (ص.) سرخ؛ احمر. (اِ.) (زه.) لعل' — i.e. Mo'in groups exactly the same words Nourai groups. Lokotsch no.1298 'Pers. lāl: Hochrot'. What Nourai does not say, and what no source can supply, is where lāl itself comes from: Wiktionary marks it 'of unknown origin' and merely wonders whether it could be a heavily reduced reflex of PIE *h₁rewdʰ- 'red'. Treating لال as an unanalysed Persian root is therefore the honest choice. Note that the homophone لال 'mute, tongue-tied' (BQT 1879, Mo'in لال ۱) is a different word and is correctly kept out of this chart.",
      "note_fa": "سرِ نمودار «لال» است، واژه‌ای فارسی به معنی «سرخ» و نیز «گوهر سرخ (لعل، بدخشی)». برهان قاطع ص ۱۸۷۹ ذیل «لال» همین دو معنی را می‌آورد و در حاشیهٔ معین آمده که «لعل معرّب لال است». معین نیز در فرهنگ فارسی ذیل لال ۳ می‌نویسد «[قس. لاله، آلاله، لعل، معرّب] سرخ، احمر»، یعنی همان خانوادهٔ واژگانی که نورایی ساخته است. اما ریشهٔ خودِ «لال» ناشناخته است؛ ویکی‌واژه آن را «of unknown origin» می‌داند و تنها به احتمال پیوند با هندواروپایی آغازین *h₁rewdʰ- «سرخ» اشاره می‌کند. پس ادعای نورایی در همین حد که «لالِ فارسی به معنی سرخ» ریشهٔ این خانواده است، درست است.",
      "sources": [
        "https://en.wiktionary.org/wiki/لال",
        "https://en.wiktionary.org/wiki/لعل"
      ],
      "ref_check": [
        {
          "ref": "BQT:1879",
=== status ===
 M data/verification/page-302.json
# regenerable from the PDF via pdftoppm (see tools/)
data/pages/

# built site (regenerate with tools/build_site.py)
site/risheh.html
__pycache__/

# Verification: OCR texts of copyrighted reference works (local audit copies only)
data/verification/sources/refs/
```


## [2026-09-06T23:14:03.715Z] AGENT

Done. `python3 tools/verify_check.py 302` reports **0 PROBLEM lines** (13/13 nodes).

**Page 302 (book p. 272) — 3 charts (+1 redirect `Lap-aro → Lep`, skipped)**

Verdicts — roots: 1 confirmed, 1 plausible, 1 disputed. Nodes: 6 confirmed, 5 plausible, 1 disputed, 1 transcription_suspect. Ref checks: 12 supports, 7 partial. Books consulted: BQT, MON, AFM, PLA, TAD, KLN, HJB, LKT, FRS, IEC, POK, AHD, WLD, CHEUNG, PHD, NYB, HRN, HUB, ARY, FVQ, SYN, AKD, SKT, AID.

Flagged items:
- **Lanğ (ROOT) — disputed.** Mann IEC 663 does print `lang- 'drooping, sad'` but adds "All evidence ambig."; the root rests only on the two branches drawn. Cheung 2007:191 derives Iranian *Hranj- (Av. rənjaiti, MP ranz/ranj) from PIE *h₁lengʷʰ- = Pokorny 660 f. `legʷh-` "light, nimble", while Pokorny 959 f. files Greek λαγγάζω/λαγγεύαι under `(s)lēg-` "slack" with λαγαρός, laxus, langueō. The two branches belong to different roots.
- **Lanğ #1 `rdjyate` — disputed.** Form impossible; gloss wrong (MW: rajyate = "be dyed, redden; be excited/charmed", never "in pain"); rañj- belongs to PIE *(s)reg- "to dye"; and an Iranian word cannot descend from Sanskrit. Nourai is garbling Mo'in's BQT footnote (`rjyate`, «در اضطراب شدن»).
- **Lâl #7 `loll sharob` — transcription_suspect.** Klein 904 prints "loll shraub, loll shrob"; Hobson-Jobson 501b "Lall-shraub / Loll Shrub". `error_in: book` — the 600-dpi render of pdf p.302 shows the book itself prints "loll sharob"; extraction is faithful.

Notable partials (not flagged): `lâlas` is glossed by Borhan only as "a fine silk fabric", with no colour — Nourai's "red" is his own addition; Asadi's Loghat-e Fors glosses `lâleh-sâr` as "a sweet-voiced bird", so "red-headed" is Mo'in's inference. `BQT:1879` for node #1 should be 1880. Zimmern (AKD 52) himself doubts the Akkadian→Arabic arrow ("or an onomatopoeic name arose independently on both sides"), and Lokotsch 1294 rejects it outright.

**No extraction errors** — the JSON matches the printed page everywhere I checked.

Two ancillary notes: (1) I recovered Addi Shir p.142 «(اللَعْل) حجر كريم تعريب لال واصل معناه الأحمر» from the page image (both OCR files drop the line) and saved it as `data/verification/sources/refs/ocr/AFM/0142.png` + `0142.vision.txt`; the page render is at `data/verification/sources/refs/ocr/BOOK/302.png` (both under the gitignored refs tree). (2) `data/verification/page-302.json` was already committed at HEAD (commit 77e1808 swept it in mid-run); my later corrections — the Pokorny 959 f. quote, the Loghat-e Fors finding, the Hübschmann §75 b citation — are in the working tree as an uncommitted modification.
