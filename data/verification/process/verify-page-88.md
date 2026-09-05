# Verification process log — verify-page-88


## [2026-09-05T13:45:14.259Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 88 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-88.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-88.json. Write /home/sfmqrb/git/rishe/data/verification/page-88.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 88` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-05T13:45:15.824Z] AGENT

I'll start by reading the instructions.


## [2026-09-05T13:45:16.537Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-05T13:45:16.552Z] TOOL RESULT

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


## [2026-09-05T13:45:16.674Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-88.txt"
}
```


### [2026-09-05T13:45:16.691Z] TOOL RESULT

```
1	=== PDF page 88 (book page 58) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Bhengh : thick, fat  (refs POK:127)
4	#1 (parent #0) [Avestan] refs=POK:127; KLN:1109 | bazah : height, depth
5	  #2 (parent #1) [Persian] refs=MON:452 | bâz «باز ۱» : distance between stretched hands | extra: بازه ، باژ ۱
6	#3 (parent #0) [Sogdian] refs=SOD:137 | db`nz : wide, coarse
7	#4 (parent #0) [Greek] refs=AHD | paxus : tick
8	  #5 (parent #4) [English] refs=AHD | pachy- : thick ; pachyderm : thick-skinned animals ☞Der 1
9	--- entry 1 ---
10	ROOT [Indo-European] Bher 1, Bhrâ-tar : Bher 1: to carry. Bhrâ-tar: load carrier (of family), brother ☞ Ter 3  (refs POK:128,163; KAS:10; PRT:234; SYN:107)  PART 1
11	#1 (parent #0) [Avestan / Old Persian] refs=POK:128 | bar : to carry, ride a horse ; baraiti : carries
12	  #2 (parent #1) [Pahlavi] refs=BQT:253 | burtan : to carry away ; bâr 1 : load ; xâyak-bâr : egg carrying fish, caviar ☞Aw
13	    #3 (parent #2) [Persian] refs=POK:128; BQT; AEF:208,212 | bordan «بردن» : to carry, take ; bâr 1 «بار ۱» : load, fruit (tree load) ; xâvîyâr «خاویار» : caviar ; barîd «بَرید» : mail carrier ; bâreh «باره» : carrier, horse | extra: بَر ۳ ، برخوردار | NOTE: PLA:48, TAD:9 and AFM:18 claim "barîd" is from Pahlavi "burtan". BQT, MON and AKD:50 claim it is from Latin "veredus: carrier".
14	#4 (parent #0) [Avestan] refs=BQT:821, 1773, 1858, 2245; HRN:68,240; FFD:42 | aspa-bâra : horse load, horse rider ☞Ekwos ; xar-bâra : donkey load, unit of weight ☞Kar 1 ; gâtu-bâra : bed carrier ☞Gwa ; gaoša-vare : carried by ear ☞Ôus 1 ; duš-vare : difficult to carry ☞Dus ; pari-bhar, pari-bar : carry around, raise (a child) ☞Per 1
15	  #5 (parent #4) [Persian] refs=BQT; SNS:133 |  «گهواره ، خروار ، سوار ، ـوار ۱» ;  «امیدوار ، دشوار ، گوشواره» ;  «پروردگار ، پرورش ، پروردن»
16	#6 (parent #0) [Avestan] refs=BQT:66; MON:1395; DRM:292; FFD:28 | â-vare, â-bar-a : bring ☞Apo ; mîžda-vare : wage earner ☞Miždho ; dâtô-vare : carrier of justice ☞Dhě 2 ; hvare-varân : where sun goes, west ☞Sâwel
17	  #7 (parent #6) [Persian] refs=BQT; FSF:58 |  «رنجور ، دستور ، داور ، مزدور ، آوردن ، جانور ، گنجور ، جنگاور ، پیامبر ، خاور» | NOTE: For a discussion on "dastŭr:priest" see "Dhě 2"
18	
```


## [2026-09-05T13:45:19.821Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-88.json",
 "description": "Read source JSON for page 88"
}
```


### [2026-09-05T13:45:19.856Z] TOOL RESULT

```
{
  "pdf_page": 88,
  "book_page": 58,
  "entries": [
    {
      "root": {
        "name": "Bhengh",
        "lang": "Indo-European",
        "refs": "POK:127",
        "gloss": "thick, fat"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:127; KLN:1109",
          "words": [
            {"translit": "bazah", "gloss": "height, depth", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "MON:452",
          "words": [
            {"translit": "bâz", "gloss": "distance between stretched hands", "script": "باز ۱"}
          ],
          "script_extra": "بازه ، باژ ۱",
          "note": null,
          "quote": {"text": "بلندیش با چرخ همباز بود - ستبریش بیش از چهل باز بود", "poet": "Asadî"}
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Sogdian",
          "refs": "SOD:137",
          "words": [
            {"translit": "db`nz", "gloss": "wide, coarse", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Greek",
          "refs": "AHD",
          "words": [
            {"translit": "paxus", "gloss": "tick", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "pachy-", "gloss": "thick", "script": null},
            {"translit": "pachyderm", "gloss": "thick-skinned animals", "script": null, "see": ["Der 1"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Bher 1, Bhrâ-tar",
        "lang": "Indo-European",
        "refs": "POK:128,163; KAS:10; PRT:234; SYN:107",
        "gloss": "Bher 1: to carry. Bhrâ-tar: load carrier (of family), brother ☞ Ter 3"
      },
      "part": 1,
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan / Old Persian",
          "refs": "POK:128",
          "words": [
            {"translit": "bar", "gloss": "to carry, ride a horse", "script": null},
            {"translit": "baraiti", "gloss": "carries", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "BQT:253",
          "words": [
            {"translit": "burtan", "gloss": "to carry away", "script": null},
            {"translit": "bâr 1", "gloss": "load", "script": null},
            {"translit": "xâyak-bâr", "gloss": "egg carrying fish, caviar", "script": null, "see": ["Aw"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "POK:128; BQT; AEF:208,212",
          "words": [
            {"translit": "bordan", "gloss": "to carry, take", "script": "بردن"},
            {"translit": "bâr 1", "gloss": "load, fruit (tree load)", "script": "بار ۱"},
            {"translit": "xâvîyâr", "gloss": "caviar", "script": "خاویار"},
            {"translit": "barîd", "gloss": "mail carrier", "script": "بَرید"},
            {"translit": "bâreh", "gloss": "carrier, horse", "script": "باره"}
          ],
          "script_extra": "بَر ۳ ، برخوردار",
          "note": "PLA:48, TAD:9 and AFM:18 claim \"barîd\" is from Pahlavi \"burtan\". BQT, MON and AKD:50 claim it is from Latin \"veredus: carrier\".",
          "quote": {"text": "یکی ترگ رومی به سر برنهاد - یکی باره زیراندرش همچو باد", "poet": "Ferdowsî"}
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Avestan",
          "refs": "BQT:821, 1773, 1858, 2245; HRN:68,240; FFD:42",
          "words": [
            {"translit": "aspa-bâra", "gloss": "horse load, horse rider", "script": null, "see": ["Ekwos"]},
            {"translit": "xar-bâra", "gloss": "donkey load, unit of weight", "script": null, "see": ["Kar 1"]},
            {"translit": "gâtu-bâra", "gloss": "bed carrier", "script": null, "see": ["Gwa"]},
            {"translit": "gaoša-vare", "gloss": "carried by ear", "script": null, "see": ["Ôus 1"]},
            {"translit": "duš-vare", "gloss": "difficult to carry", "script": null, "see": ["Dus"]},
            {"translit": "pari-bhar, pari-bar", "gloss": "carry around, raise (a child)", "script": null, "see": ["Per 1"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Persian",
          "refs": "BQT; SNS:133",
          "words": [
            {"translit": null, "gloss": null, "script": "گهواره ، خروار ، سوار ، ـوار ۱"},
            {"translit": null, "gloss": null, "script": "امیدوار ، دشوار ، گوشواره"},
            {"translit": null, "gloss": null, "script": "پروردگار ، پرورش ، پروردن"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 0,
          "lang": "Avestan",
          "refs": "BQT:66; MON:1395; DRM:292; FFD:28",
          "words": [
            {"translit": "â-vare, â-bar-a", "gloss": "bring", "script": null, "see": ["Apo"]},
            {"translit": "mîžda-vare", "gloss": "wage earner", "script": null, "see": ["Miždho"]},
            {"translit": "dâtô-vare", "gloss": "carrier of justice", "script": null, "see": ["Dhě 2"]},
            {"translit": "hvare-varân", "gloss": "where sun goes, west", "script": null, "see": ["Sâwel"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "Persian",
          "refs": "BQT; FSF:58",
          "words": [
            {"translit": null, "gloss": null, "script": "رنجور ، دستور ، داور ، مزدور ، آوردن ، جانور ، گنجور ، جنگاور ، پیامبر ، خاور"}
          ],
          "script_extra": null,
          "note": "For a discussion on \"dastŭr:priest\" see \"Dhě 2\"",
          "quote": {"text": "مهر دیدم بامدادان چون بتافت - از خراسان سوی خاور میشتافت", "poet": "Rŭdakî"}
        }
      ]
    }
  ]
}
```


## [2026-09-05T13:45:20.631Z] TOOL CALL #4: Bash

```json
{
 "command": "sed -n '1,200p' data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-05T13:45:20.679Z] TOOL RESULT

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


## [2026-09-05T13:45:46.237Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -i \"bhengh\\|bheng̑h\\|bheng-h\" POK_full.txt | head -30; echo \"=== AHD\"; grep -n -i \"bhengh\\|pachyderm\\|bhen.h-\" AHD_watkins1985.txt | head -20",
 "description": "Grep Pokorny and AHD for bhengh"
}
```


### [2026-09-05T13:45:46.331Z] TOOL RESULT

```
=== AHD
184:Another aspect of the function of sover- eignty is the sphere of the law. There is an old word, yewes-, probably for “religious law,” in Latin jus. Latin léx is also ancient (leg-'), though the details of its etymology are uncertain. In a society that emphasized the principle of exchange and reciprocity, it is scarcely surprising that the notion of con- tractual obligation should be well repre- sented. Several roots specify the notion of “bond”: bhendh-, ned-, leig-', all of which have derivatives with technical legal mean- ings in various languages. The word for “a pledge,” wadh-', exists in western Indo- European, whence the English verb for mak- ing a particular kind of contract, WED. An oath then as now was important: the roots *serk- and oito- are found in Celtic and Ger- manic. The verb k”ei-' meant “to pay com- pensation for an injury.” Its derivative noun, *k“oind, was borrowed from Doric Greek into the most ancient Roman law as Latin poena, punire, whence English PUNISH and a host of legal terms. The Greek word for jus- tice, diké, is derived from the notion of “boundary marker” (deik-; compare also ter-, “termen-).
330:3. O-grade form *bhol- in Germanic *ball- in: a. Old English beallucas, testicles: BOLLIX; b. Old Norse bdllr, ball: BALL; c. Danish bolle, round roll, akin to the probable Scandinavian source of BILBERRY; d. Middle High German baile (> Italian balla, palla), ball: BAL- LOON, BALLOT; PALL-MALL; e. French baile, ball: BAL- LOTTEMENT; f. Old French baie, rolled-up bundle: BALE!. 4. Suffixed o-grade form *bhol-to- possibly in Germanic *balthaz, bold, in: a. Old English bald, beald, bold: BOLD; b. Old High German bald, bold: BAWD. 5. Suffixed o-grade form *bhol-n- in Latin follis, bellows, inflated ball: FOLLICLE, FOOL!; (FOLLICULITIS). 6. Possibly Greek phalaina, whale: BALEEN. 7. Conceivably (but more likely unrelated) Greek phellos, cork, cork oak: PHEL- LEM; PHELLODERM, PHELLOGEN. (The following deriva- tives of this root are entered separately: bhel-?, bhelgh-, bhlei-, bhleu-.) [Pok. 3. bhel- 120.} bhel-3, To thrive, bloom. Possibly from bhel-?. I. Suffixed o-grade form *bhol-yo-, leaf. 1. Latin folium, leaf: ForL?, FOLIAGE, FOLIO, FOLIUM; CINQUEFOIL, DEFOLIATE, EX- FOLIATE, FEUILLETON, FOLICOLOUS, MILFOIL, PORTFO- LIO, TREFOIL. 2. Greek phullon, leaf: (-PHYLL), PHYLLO-, -PHYLLOUS; GILLYFLOWER, PODOPHYLLIN. II. Extended form *bhlé- (< *bhlea-). 1. O-grade form *bhl6- in: a. suffixed form *bhlé-w- in Germanic *bl6-w- in Old English bléwan, to flower: BLOWS; b. Germanic suffixed form *bl6-m6n- in (i) Old Norse blém, blémi, flower, blossom: BLOOM! (ii) Old English bléma, a hammered ingot of iron (semantic development obscure): BLOOM?; c. Germanic suffixed form *bl6-s- in Old English bléstm, bléstma, flower, blossom: BLOssoM; d. Latin flés (stem flor-), flower: FERRET?, (FLORA), FLORA, (FLORAL), FLOR- IATED, FLORID, FLORIN, FLORIST, -FLOROUS, FLOSCULUS, FLOUR, FLOURISH, FLOWER; CAULIFLOWER, DEFLOWER, EFFLORESCE, ENFLEURAGE, FLORIGEN. 2. Germanic suf- fixed form *blé-do- in Medieval Latin bladium, produce of the land: EMBLEMENTS. 3. Suffixed zero-grade form *bhib-to- in Germanic *bladaz in Old English bled, leaf, blade: BLADE. [Pok. 4. bhel- 122.] bhel-4. To cry out, yell. Germanic *bell- in: a. Old English bellan, to bellow, bark, roar: BELL?; b. Old English belle, a bell: BELL!; c, Old English belgan, bylgan, to become enraged: BELLOW; d. perhaps Old English bealcan, *b(iJelcan, to utter, belch forth: BELCH; e. Middle High German buldern, boldern, to make noise: POLTERGEIST; f. Icelandic baula, to low, akin to the Scandinavian source of Middle English baulen, to howl: BAWL. [Pok. 6. bhel- 123.] bheld-. To knock, strike. Zero-grade form *bhid- in Germanic *bult-, missile, in Old English bolt, heavy arrow, bolt: BouT!. [Pok. bheld- 124.] bhelg-. Also bhelk-. A plank, beam. 1. Germanic *balku- in Old English balc(a), ridge: BALK. 2. Germanic *balk6n- in: a. Old French bauch, beam: DEBAUCH; b. Old Italian balcone, scaffold: BALCONY. 3. Suffixed zero-grade form *bhik-yo- in Latin fulcire, to prop up, support: FULCRUM. 4. Possibly Greek phalanx, beam, finger bone, line of battle: PHALANGE, PHALANX. [Pok. 5. bhel- 123.] bhelgh-. To swell. Extension of bhel-2. 1. Germanic *balgiz in Old English bel(ijg, belig, purse, bellows: BELLOWS, BELLY. 2. Germanic *bulgjan in Old Norse bylgja, a wave: BILLOW. 3. Germanic *bolgstraz in Old English bolster, cushion: BOLSTER. 4. Celtic *bolg- in Latin bulga, leather sack: BUDGET, BULGE. [Pok. bhelgh- 125.) bhelu-. To harm. Germanic *balwaz in Old English bealo, b(e)alu, harm, ruin, bale: BALE?. [Pok. bheleu- 125.] bhendh-. To bind. 1. Germanic *bindan in Old English bindan, to bind: BIND; WOODBINE. 2. O-grade form *bhondh- in Germanic *band- in: a. Old English bend, band, ribbon, akin to the Germanic source of Old French bende, band: BEND?; b. Old English bendan, to bend: BEND!; c. Old Norse band, band, fetter: BAND!, BOND; d. Old French bande, bond, tie, link: BAND!. 3. Zero-
332:grade form *bhndh- in Germanic *bund- in: a. Middle High German bunt, league: BUND?; b. Middle Dutch bondel, sheaf of papers, bundle: BUNDLE. 4. Suffixed form *bhendh-na-, “tied structure” (as of wicker), in Celtic *benna, manger, in Old English binn(e), manger: BIN. 5. Persian band, band, bandage, also a river levee: BUND!; CUMMERBUND. 6. Sanskrit badhndti (Sanskrit root bandh-), he ties: BANDANNA. [Pok. bhendh- 127.] bhengh-. Thick, fat. Extended zero-grade form *bhnghu- in Greek pakhus, thick, fat: PACHYDERM, PACHYSANDRA. [Pok. bhengh- 127.]
1276:BABA baba- BABBLE baba- BABE baba- BABKA baba- BABU baba- BABUSHKA baba- BABY baba- BACILLUS bak- BACTERIUM bak- BACULIFORM bak- BAGEL bheug-3 BAGUETTE bak- Bails bheug-3 BAIRN bher-1 BaIT! bheid- BAKE bhé- BAKSHEESH bhag-' BALALAIKA baba- BALCONY bhelg- BALE! bhel-2 BALE? bhelu- BALEEN bhel-2 BALK bhelg- BALL! bhel-2 BALL2 gWele-1 BALLAD gWele-1 BALLAST bhoso-, kla- BALLET gWela-1 BALLISTA gWele-1 BALLOON bhel-2 BALLOT bhel-2 BALLOTTEMENT bhel-2 BAMBINO _baba- BAN! bha-2 BANAL bha-2 BAND! bhendh- BANDANNA bhendh- BANDIT bha-2 BANDOLEER bha-1 BANDORE pandoura BANE gWhen-1 BANG! bheg- BANIAN wen-1 BANISH bha-2 BANK! bheg- BANK? bheg- BANK? bheg- BANKRUPT bheg-, reup- BANNER bha-! BANNERET bha-1 BANNS bha-? BANQUET bheg- BANQUETTE bheg- BANSHEE gWen- BANTLING bheg- Baptist gébh-!
1288:BEND! bhendh- BEND? bhendh- BENEATH ni BENEDICTION deik-
1299:BILBERRY bhel-2 BILINGUAL dnghi BILIRUBIN reudh-1 BILIVERDIN virére BILL! beu-1 BILL? bhei-2 BILLS = bhei-2 BILLET! beu-1 BILLET-DOUX = dik-u- BILLOW bhelgh- BILTONG bhel-2, dnghi BIMESTRIAL mé-2 BIN bhendh- BINAL dwo- BINARY dwo- BIND bhendh- BINNACLE ghabh- BINOMIAL nem- BIO- gW¥ei-
1313:BOLD bhel-2 BOLE! bhel-2 BOLL bhel-2 BOLLIX bhel-2 BOLOMETER gW¥ele-1 BOLSHEVIK bel- BOLSTER bhelgh- BOLT! bheld- BOMB bamb- BOMBARD bamb- BONANZA deu-2 BONBON deu-2 BOND bhendh- BONDAGE bheue- BONHOMIE deu-2, dhghem- BONITO deu-2 BONNE deu-2 BONNYCLABBER band- BONTEBOK bhugo- BONUS deu-2 BOOBY baba- BOODLE bheue- BOOK bhago-
1324:BRIO gWere-2 BRIOCHE bhreg- BRISANCE bhréi- BRISTLE bhar- BRITTLE bhreu-1 BRONCHIECTASIS  ten- BRONCHO- gWere-4 BRONCHUS gWere-4 BRONTOSAUR bhrem-! BROOD bhreu-2 BROOK? bhriig- BROOM bhrem-2 BROTH bhreu-2 BROTHEL bhreu-' BROTHER bhrater- BROW bhri- BROWN bher-3 BROWSE bhreus-1 BRUIN bher-3 BRUISE bhreus-2 BRUMAL mregh-u- BRUNET bher-3 BRUT gWere-2 BRUTE gWere-2 BUBO beu-! BUCCAL beu-1 BUCEPHALUS gWou- BUCK! bhugo- BUCKAROO wak- BUCKBOARD beu-! BUCKLE! beu-! BUCKLE? beu-1 BUCKSHEE bhag-' BUCKWHEAT bhago- BUCOLIC gou-, kWel-1 BuppHA bheudh- BUDGET bhelgh- BUDGE! beu-1 BUGLE! gWou- BUGLOss gldgh- BUILD bheue- BULGE bhelgh- BULIMIA gWou-, leia- BULK! bhel-2 BULL! bhel-2 BULL? beu-1 BULLA beu-1 BULLATE beu-1 BULLET beu-! BULLETIN beu-1 BULLION beu-1 BULLY? beu-1 BULWARK bhel-2, werg- BUNCO bheg- BUND! bhendh- BUND? bhendh- BUNDESRAT ar- BUNDLE bhendh- BUNG peuk- BUNGLE bheg- BUPRESTID gWou- BUR! bhar- BURDEN! bher-1 BURG bhergh-2 BURGESS bhergh-2 BURGHER bhergh-2 BURGLAR bhergh-2 BURGOMASTER bhergh-2 BURIAL bhergh-! BURIN bher-2 BURN! gWher- BURN? bhreu-2 BURNET bher-3 BURNISH bher-3 BURSA bursa BURSAR bursa BURSE bursa BURST bhres- BURY bhergh-1 BUSHEL? bhau- BUSK! busk- BUSK? s(w)e-
1402:CUBE keu-2 CUBICLE keu-2 CUBIT keu-2 CUCKING STOOL kakka- CUD gWet-1 CUDGEL ku- CUESTA kost- CUIRASS sker-1 CUISINE pekw- CUISSE koksa CULET (s)keu- CULINARY pekw- CULLET kwel-1 CULLIS kagh- CULM! kolem- CULMINATE kel-6 CULOTTES (s)keu- CULT kWel-1 CULTIVATE kwel-1 CULTRATE skel-1 CULTURE kvel-1 CULVER kel-5 cum kom CUMMERBUND bhendh-, kamer- CUMULATE keue-2 CUMULUS keue-2 CUNCTATION konk- CUNNILINGUS leigh-, (s)keu- CUNNING gné- CUNT ku-
2031:PACHISI penkwe, wikmti PACHYDERM bhengh- PACHYSANDRA bhengh- PACIFIC pag- PACIFY pag-
```


## [2026-09-05T13:45:47.021Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== BRT bazah\"; grep -n -i \"bąz\\|bazah\\|bāzah\" BRT.txt | head -30",
 "description": "Grep Bartholomae for bazah"
}
```


### [2026-09-05T13:45:47.078Z] TOOL RESULT

```
=== BRT bazah
17243:•  j.  bazah-  n.  'Höhe,  Tiefe':  avervaitya °zas/a  fra%as{a  .  .ya^a  im  z3,  astica  tm zä  avaiti  °z5  yavaiti  /raiiascit  "soviel  an
```


## [2026-09-05T13:45:53.373Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"b.engh\\|bhengh\\|bhen'gh\\|bhenĝh\" POK_0*.txt POK_full.txt | head -20; echo \"=== try dick dicht feist\"; grep -n \"dick, dicht, feist\\|dicht, feist\" POK_0*.txt POK_full.txt | head",
 "description": "Grep Pokorny variants"
}
```


### [2026-09-05T13:45:53.434Z] TOOL RESULT

```
POK_full.txt:11066:lemma: b'^eg-, b'^eng-: "to break', Root/ lemma: b^engh-, b'^pgh-iM]. b'^pghu-s) : "thick, 
POK_full.txt:12128:Root/ lemma: b^engh-, b^Qgh-{M]. b^pghu-s) 
=== try dick dicht feist
```


## [2026-09-05T13:45:55.008Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '17235,17260p' BRT.txt; echo \"=== find page marker near\"; awk 'NR<=17243 && /^[[:space:]]*[0-9]{3,4}[[:space:]]*$/ {p=$0; n=NR} END{}' BRT.txt | tail -3",
 "description": "Context around bazah in Bartholomae"
}
```


### [2026-09-05T13:45:56.494Z] TOOL RESULT

```
•  j.  böit  Part,  der  Beteuerung  und  Her- vorhebung, hinter  dem  ersten  Wort  im Satz;  a)  hinter Nom. :  nanm  b°  alavamm.. V. y.  22;  —  iuinm  b'  yäsamHi  x''annö ..  dayata  Ny.j.  ii-  b)  hinter  dem Pron.:  aztm  böit  ..  tä  nipayemi  Ytj.Sg.
Komp.!  M(sd.)+Ä.  —  Pü.  (in  V.  13):  itar.
•  j.  boiwrra-  m.  'Kampf,  Streit':  'ranqm dmitanamca  ..  %wa^sh  (sd.)  Yt/y.  so.
Mit  Int. -Red.  gebildet,  S  103  n.  6.  —  ai.  vgl. bhira-  m.  'Kampf;  Bthl.  IF.  IO.  aoo.
•  j.  banha-  m.  EN.  eines  Gläubigen: '»hahe  sä»ha»hahe  asaonö  "des  ß.,  Sohns des  S.  .."  Yty.  124-
Ar.  'biäsa-  m.  Name  eines  Raubvogels'),  — ai.  bhäsa-  m.  (auch  als  EN.);  mp.  bähai  EN. (=  ai.  ikäsaka-  EN.\  S.  noch  Marquart EranSahr  128.  —  ')  Zn  gr.  ^n;  {eine  Adler- att)  s.  Bthl.  IF.  8.  235.
•  j.  baSra-  m.''  (vll.)  'Krankheit':  'rs  F.  16. Zum'V.  batt:  —  Pü.:  bann,  angeblich  bahüa 'ditficult' >),  wahrscheinlich  i.Ji-  (vgl.  np.  lär 'Faden',  GlrPh.  /  b.  23).  —  'I  ?  Eher  dürfte 'rS  von  einem  Komp.  abgerissen  sein.  — »  Was  ist  banntnn  {iarlan)  im  PPGI.?;  s. Salemann  GIrPh,  /.  327.  15,
•  j.  baz-  V.:  s,  unter  d»bqz-.
•  j.  bazah-  n.  'Höhe,  Tiefe':  avervaitya °zas/a  fra%as{a  .  .ya^a  im  z3,  astica  tm zä  avaiti  °z5  yavaiti  /raiiascit  "soviel  an
[Höhe  und  Breite  als  die  Erde;  und  es  ist I  die  Erde   so   gross  an  Höhe  (Tiefe)  wie
dby  Google
963
b^i^lnav-
bipaitiä^na-
964
an  Breite"  Y.ig-T, —  ovaiH  '«ff  V.  2.19 PuZ.
Vgl.  tqhtav-.  —  ai.  vgl,  bahulä-  Adj.  —  Pü.
zakäk.  Sä.:  J*a^ai.
•  j,  bi^äoav-  m.  Ilöhe,  Tiefe';  yahmat haia  . .  sna<^  (sA)  va/ra  snaiiäj  ..°n. anduyä  "..  Schncetnassen  ..  bis  zu  Tiefen, wie  sie  die  ArxivJ  hat"  V,  2.  32.
Vgl.  iqzaA:  —  PQ.  :  fia  iäj  i  land  arin'i 'mit  der  Tiefe  mehrerer  Ellen',  Daiu  die Erl.:  ä«  j/äi  hi  kam  nainel  ezai  vilasi  11  2 angusi  ape  niSintt  "wo  wenig  (Schnee)  liegt, liegt  er  eine  Spanne  und  zwei  Finger  hoch". —  ')  So  lu  lesen,  -^^  j.  ari%na-%  E  hat  das synonyme  ari.
•  j.  bi.ayar-  n.  'Zeit  von  zwei  Tagen': °r>m^^  bi.xsafanm  lanum  frasnayayatita "während  zweier  Tage  . ."  Yt.  io.  122.
I)  Them,
•  j.  bixatra-  n.  Name  eines  zu  Ritual- zwecken dienenden  Gefässes:  gaomaiigm ayasSil  .  .  gaom  pairi  uxlätam  'lr>m dllityS.kgrfism  "Rindsurin  sollst  du  sammeln bei  (von)  einem  Stier  in  ein  rite  hergestelltes Ä"  V.T5.21-).
VII.  ti-xilra-  eig.  'was  zwei  Glieder,  d.  i. Henkel  hat,  Henkelgefass' ;  'jtiira-  (aus  ar. Hlra-),  Nullform  lu  ai.  gifa-  n-  'Glied'.  — Pü.i  undeullichi  b')naark.  —  ■)  Ich  fasse die  Stelle  nach  V.  g.  14-  S.  übrigens  Hauc ZPGl.  106,  DsT.  ZA.  2.  266.  —  ')  S.  daiu Saleuann  GIrPh.  /.  288.
•  j.  bi.xiapar-''  n.  'Zeit  von  zwei  Näch- ten', wobei  i)  Nacht  im  Gegensatz  zu Tag  gilt:  bi.ayarsm  •rpm'''  tanäm  framaya- yanta  "während  zweier  Tage  und  Nächte  .." Yt.  jo,  132.  2)  Nacht  als  Zeit  von Sonnenuntergang  bis  Sonnenuntergang: agta^a  .  .  tanüm  nidai^yqn  °r^m'*  vä %ri.xSapar?m  vä  ". .  auf  die  Dauer  von zwei  oder  drei  Tagen"  V.5. 12.
Pü.:  2  sapak.—  ')  NA.  auch  ohne  Trennung. —  J)  Them.
=== find page marker near
```


## [2026-09-05T13:46:04.157Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '12128,12180p' POK_full.txt",
 "description": "Pokorny bhengh entry"
}
```


### [2026-09-05T13:46:04.198Z] TOOL RESULT

```
Root/ lemma: b^engh-, b^Qgh-{M]. b^pghu-s) 
Meaning: thick, fat 

Material: Old Indie bahu-'der\se, rich, much, a lot of "compounds Sup. barhhlyas-, 
batfihistha- {= gr. naxu(;); 

bahula-^Mck, dense, vast, spacious, big, large, rich, much, a lot of (= gr. naxuAwq Adv. 
by Aristot., if these not newer formation); bambate {ur\covered) ' increase, multiply ', 
bhaifihayate^ clamps, fastens, strengthens'; 

Avestan b^zah-r\. 'height, depth', bqsnu-rr\. ds., Baluchi it'az'much, a lot of, baz 
'dense'; 

gr. TTaxu(; 'thick, dense, fat, obese' (compounds naaawv), "rraxoq n. 'thickness, 
fatness' (occurs after naxu(; for *n£YX0(; = Avestan bqzah-), jrdx^ioq, 'thick; thickness, 
fatness'; 

Old Icelandic bingr^bea'^\ Old Swedish binge 6s., Old High German bungo^\uber, bulb', 
Modern High German Bachbunge, in addition with intens. consonant-sharpening Old 
Icelandic bunki^ stowed away shipload', Norwegian bunka{ar\6 bunga) ^sruaW heap, 
swelling, blister', Dutch it'o/?/: 'clump, lump' ; 

Note: 

Alb. bunge^ kind of edible oak fruit ' : with -^- grade alb. {*beuka) buka'brea6' : Phrygian 
pEKoc; 'bread', actually ' crumb ' prove that from an extended Root/ lemma: b(e)u-1, 
b^(e)u-\ 'expr. sound of hitting' derived Root/ lemma: b'^eg-, b^eng-: 'to break'. Root/ 
lemma: b'^engh-, bh^^^-(Adj. b'^ijghu-^ : thick, fat'. Root/ lemma: b'^eug-l: to flee, *be 
frightened'. Root/ lemma: b'^eug-2, b'^eugh-: to clear away, free'. Root/ lemma: b^eug-3, 
b^eugh-: 'to bow', Root/ lemma: b^eug-4\ 'to enjoy, *consume, bite' as taboo words. 



Latvian b/ezs'dense, thick', i6'/e'z^/77s"tliicl<ness, fatness'; 

Latin pinguis^ fat; oily; ricli, fertile; n. as subst. fatness, fat. Transf. thick, dense; heavy, 
stupid; easy, quiet ' has perhaps originated through hybridization of *fingu-is= naxuc;, 
bahu-mVc\ that to opTmus, niwv respective words; 

Tocharian B pkante, /0/ra//e "greatness, bulk, extent' (Van Windekens Lexique 96); 

Hittite pa-an-ku- {panku-) 'all,ingenerar. 

References: WP. 111 51, Couvreur H 177. 
Page(s): 127-128 

Root / lemma: b^e/?- 

Meaning: to hit, wound 

Material: Avestan bqnayan^W makes me sick', banta- "sickens, waste away'; 

Gothic ban/a 'b\o\N, knock, wound, ulcer'. Old Icelandic ben, Old English benni., (under
```


## [2026-09-05T13:46:06.718Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== SOD 137\"; awk 'BEGIN{RS=\"\\f\"} /\\[pdf page 1[0-9][0-9]\\]/' SOD_pages.txt >/dev/null; grep -n \"δβʾnz\\|dβʾnz\\|db.nz\\|ẟβʾnz\" SOD*.txt | head -20; echo \"=== SOD page area\"; grep -n \"\\[pdf page 137\\]\\|\\[pdf page 138\\]\\|\\[pdf page 139\\]\" SOD_pages.txt | head",
 "description": "Grep Sogdian dictionary"
}
```


### [2026-09-05T13:46:08.406Z] TOOL RESULT

```
=== SOD 137
SOD.txt:53409:pa5panz  (p5p>zn,  p5Pnz)  ©<*apa-dbanz-\ 
SOD_pages.txt:23188:     (rc)stick                                                         pa5panz (p5p>zn, p5Pnz) ©<*apa-dbanz-\
=== SOD page area
```


## [2026-09-05T13:46:16.845Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources; python3 -c \"\nimport json\nd=json.load(open('refs_online.json'))\nfor k in ['SOD','MON','BQT','POK','AHD','KLN','SNS','FSF','FFD','AEF','DRM','HRN','PLA','TAD','AFM','AKD','KAS','PRT','SYN','BRT']:\n    print(k, json.dumps(d.get(k), ensure_ascii=False)[:600])\n\"",
 "description": "Reference metadata"
}
```


### [2026-09-05T13:46:18.336Z] TOOL RESULT

```
SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id=
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h
SNS {"title": "Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/VajnameShayest", "lookup_hint": "grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php search (see BQT) for better hit-to-leaf mapping.", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS.txt
FSF {"title": "Abdolhossein Noushin, Vazhe-namak: Farhang-e Vazheha-ye Doshvar-e Shahnameh (Farhang-e Shahnameh), Donya 1363/1984", "kind": "archive_djvu", "url": "https://archive.org/details/20220809_20220809_1444", "lookup_hint": "grep the headword in FSF_pages.txt (alphabetical glossary); use inside.php search for leaf numbers. Also https://archive.org/details/nooshinshahnameh is a different Noushin book (گزارشی چند درباره شاهنامه).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF.txt"], "page_offs
FFD {"title": "Mohsen Abolghasemi, Fe'l-ha-ye Farsi-ye Dari, Qoqnus, Tehran 1374/1995", "kind": "local_scan_ocr", "url": "https://asmaneketab.ir/product/کتاب-ماده-های-فعلهای-فارسی-دری-محسن-اب/ -> https://dl.eliteraturebook.com/app/public/attachments/6925d29630b83.PDF (free PDF site; grey)", "lookup_hint": "Searched archive.org (Persian/Latin titles, author), ketabnak, noorlib, general web (pdf/download): nothing; only a related paid e-book 'واژگان زبان فارسی دری' (fidibo). ketabnak.com/book/45024 is a different book (فهرست فعلهای فارسی).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/s
AEF {"title": "Jalal Khaleqi Motlaq, Asas-e Eshteqaq-e Farsi, vol. I (آ–خ), Bonyad-e Farhang-e Iran 1356/1977 — this is the Persian TRANSLATION of Paul Horn's Grundriss der neupersischen Etymologie (HRN) with Hübschmann's Persische Studien (HUB) notes and added Persian/Pahlavi evidence", "kind": "catalog", "url": "https://openlibrary.org/works/OL38785552W (vol. 1, 1356) ; 2015 complete ed. «فرهنگ ریشه‌شناسی فارسی» (مهرافروز) print-only: https://www.gisoom.com/book/11154690/ ; German original: https://archive.org/details/grundrissderneu00horngoog", "lookup_hint": "Not online (searched archive.org, 
DRM {"title": "J. Darmesteter, Études iraniennes, 2 vols., Paris 1883", "edition_found": "1883 both tomes in one scan", "kind": "archive_djvu", "url": "https://archive.org/details/etudesiraniennes00darm", "identifier": "etudesiraniennes00darm (t.1 alone: tudesiranienne01darmuoft; t.2 alone: darmesteter-etudes-sur-la-langue-la-litterature-les-croyances-de-la-perse-ancienne)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/DRM.txt", "page_offset": "Tome I: leaf = p + 22 (e.g. leaf 26 = p.4); Tome II (starts ~leaf 364): leaf = p + 364 (e.g. leaf 368 = p.4). Nourai does not say w
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 
PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt"], "page_offset": "301 lea
TAD {"title": "Tobia al-Unaysi (طوبيا العنيسي), Tafsir al-alfaz al-dakhila fi al-lugha al-'arabiyya ma'a dhikr asliha bi-hurufihi (2nd ed. Cairo 1932, ed. Yusuf Tuma al-Bustani; later Library of Lebanon reprint) — Nourai lists it under Arabic authors ('Unaysi T.'); its Table IV line was lost in the OCR", "kind": "archive_djvu", "url": "https://archive.org/details/TOB1932ARAR (1932 ed.); also https://archive.org/details/ar113lang79 and https://archive.org/details/elshandawily14640", "lookup_hint": "Alphabetical Arabic headwords; grep the Arabic headword in TAD_pages.txt (86 leaves) or TAD.txt; insi
AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/
AKD {"title": "H. Zimmern, Akkadische Fremdwörter als Beweis für babylonischen Kultureinfluss, Leipzig 1917 (2nd ed.)", "edition_found": "1915 first edition (1917 is the 2nd, enlarged ed.; pagination may differ slightly)", "kind": "archive_djvu", "url": "https://archive.org/details/akkadischefremdw00zimmuoft", "identifier": "akkadischefremdw00zimmuoft", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AKD.txt", "page_offset": "leaf = printed + 8 (e.g. leaf 21 = p.13). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://
KAS {"title": "M.A. Hasani Da'i al-Eslam, Khod-amuz-e Zaban-e Sanskrit, Danesh 1361/1982", "kind": "website", "url": "https://ketabnak.com/book/108067 (131 pp. PDF, login)", "lookup_hint": "Not on archive.org.", "local_file": null, "page_offset": null, "covers_etymology": false, "notes": "PDF page exists; not fetched."}
PRT {"title": "E. Partridge, Origins: A Short Etymological Dictionary of Modern English, New York 1958", "edition_found": "1958 (lending-only copies)", "kind": "archive_restricted", "url": "https://archive.org/details/originsshortetym00part (1958 1st ed.) ; originsetymologi0000part_j9t3 (4th ed. 1966) ; originsetymologi0000part (Routledge 2009) — all lending", "identifier": "originsshortetym00part (also originsshortetym0000unse, bwb_P8-AVM-445, 1958)", "local_file": null, "page_offset": null, "lookup_hint": "Borrow via IA lending; in-book search https://archive.org/details/originsshortetym00part?q
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1
```


## [2026-09-05T13:46:24.849Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"[85dS][pP]['ʾ]nz\\|8β'nz\\|5p'nz\\|dp'nz\" SOD_pages.txt | head -20; echo \"---coarse\"; grep -n \"coarse\" SOD_pages.txt | head -20",
 "description": "Search Sogdian dictionary for dbanz"
}
```


### [2026-09-05T13:46:24.917Z] TOOL RESULT

```
5559:    can =^cnn                                                    a5Pa(n)z    OSP'nz)   ©<*0waja-
13652:                                                                            3473 5b*nzkwy                       B =» SP'nzq'wyy
13716:                                                                    8Panstar ®<*61Pnz-str         ^SP'nz
23186:                                                                  6785 pSp'nz B                     *;£"*, mJ>*jJ>
32001:9790 w'pyz'ywksth B                l_jJ^ J^A>- <CooJb 4z*-        9801 w'Sp'nz =* 6p>n?
---coarse
8594:                                                                              coarse, rough
13642:      GcOcollect, 0o)gain                                                        wide, coarse                     SPnstr
29650:     sare (sryy) ©in compd. =»sr}k, sr-                         coarse
37858:(f6>)cease   950, 958                      childlish     9520                       coarse    1679, 3471, 8986
```


## [2026-09-05T13:46:29.439Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '13625,13665p' SOD_pages.txt; echo \"=== pdf page tag near\"; awk 'NR<=13642 && /\\[pdf page/ {t=$0; n=NR} END{print n, t}' SOD_pages.txt",
 "description": "Context for Sogdian dbanz entry"
}
```


### [2026-09-05T13:46:35.133Z] TOOL RESULT

```
          Mem. vol. 1971, 290 n47a; TSP 13.23; Benv.
                                                                                         (a)5Pane ^'SP'nk
          Sfi'z, n p228; S W, IIJ 1976, 55.23                                                                                                        4*sy
                                                                                         grain, seed
                                                                                         MDii pl99;MDiii  pll9
                                                                                                                                                                   i^
 3457 5p»r-     B -» 5p>r                                                                                                                                               6p't
 3458 8pwr Spr'yn'y B                           .ju^*^ «jui**                3469 5p}npn B, S => SP'mpnCw), Sp'mb'n
      8par- 8Parene «*8p,r                                                   3470 db'n(y) B
      giver of gifts                                                                                                                                               *j>j^
                                                                                         9/5Pan(e)
                                                                                         extension =»*8p>y-
      SCE 496; -Sprrik, SCE 46
                                                                                         STi 75.18; Sund. AoFiii 1975, 56
 3459 6p>Yst- B                      ( j&jji rJLJ-^j^-jJul
      Spaxst, Gfaxst (6Pj-) ©*0wax.?-; /"/wa^ ®pt.                          3471 5p>nz B, S
        st, =»9fyz-, 8p'yz-, 8pxsty(y), SPystc                                   SPanz ©<*debazah; Av. bazah
      GcOcollect, 0o)gain                                                        wide, coarse                     SPnstr
      GMS 293; Hen. LW 105; VJ 241, 243 pp., n p92;                              TSP 2.1018; Hen. Texts. 738; GMS 1310; MSP
        AVS 130                                                                              bl89; Frag. Len. 97a3
 3460 8p»m>n    B, S ~> db'mn                                               3472 6p}nzqVyy M                         Jz*^
                                                                                                                          Uw>
 3461 db,m)nqy> C                                   J£<JL*f                      5Panzkawc (8b)nzkwy)
                                                                                 thickness
      SPamankya ^SPm'nky*
      doubt                                                                      GMS 999; Hen. BSOAS 12.312, 91; BBB
      STii 3.21
                                                                            3473 5b*nzkwy                       B =» SP'nzq'wyy
3462 fip'mb'n M                           j^a ^ '^                          3474 8p»r B, M, S                            c^^-u
     Spamban    (5p>npn, S^mbn) ©<* demand- pad ni\                              8Par, 9far (8p»r-) ^Gb'r, 8p'r 8pr>yn>y
       Pahl. banbisn -^db'mn, SP}mpn(w)
     lady, wife                                                                         GMS 957, 1511; BBB 751 f34; VJ; TSP; BSTBL,
     GMS 14, 43, 466, abl. -\ 1224; Benv. Titers et                                         Vaj.; SCE; Frag. Len. 45.3; KG 414; Talcs. 481,
       Noms Proprcs. 29; Gersh. Sogd. Cpds. 137
                                                                                            48; 6fi*ry VJ 190, 58d, 988
3463 6p>mbn =» 5P,mb,n                                                     3475 6pV-gift B                                  (Jjzs ^r,f,,,, j->) q»lj<u-U *Jjb

3464 db>mn C, S                                                                         8Par, Gfar ©OP fra-bam Khwar. hfir-,
                                                    y,
     SPamman (SP'nVn) ^SP'mb'n, b}mn                                                     Yaghn. tifar ©inf. J>}y =>9br-, SPr-1
     lady, wife
=== pdf page tag near
```


## [2026-09-05T13:46:45.427Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'NR<=13642 && /pdf page/ {t=$0; n=NR} END{print n\": \"t}' SOD_pages.txt; grep -n \"pdf page\" SOD_pages.txt | awk -F: '$1<13700 && $1>13000' | tail -5",
 "description": "Find pdf page marker"
}
```


### [2026-09-05T13:46:47.725Z] TOOL RESULT

```
:
```


## [2026-09-05T13:46:51.010Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; head -3 SOD_pages.txt; echo \"---\"; awk 'BEGIN{RS=\"\\f\"} {n++; if (index($0,\"3471 5p>nz\")) print \"formfeed page:\", n}' SOD_pages.txt",
 "description": "Locate leaf of Sogdian entry"
}
```


### [2026-09-05T13:46:54.528Z] TOOL RESULT

```
 SOGDIAN
DICTIONARY
Sogdian - Persian - English
---
formfeed page: 203
```


## [2026-09-05T13:47:10.226Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== HRN baz\"; grep -n \"bāz\\b\\|baz 'Klafter'\\|Klafter\" HRN.txt | head -20; echo \"=== HUB\"; grep -n \"Klafter\" HUB.txt | head -10; echo \"=== BRT bazu\"; grep -n \"bāzu\\|bazav\\|bāzav\" BRT.txt | head -10",
 "description": "Grep Horn/Hübschmann for Klafter (fathom)"
}
```


### [2026-09-05T13:47:10.292Z] TOOL RESULT

```
=== HRN baz
1838:Gehört hierher auch np. boz 'Klafter (Vullers: 8),
=== HUB
329:die Bedeutung von drstya- fDaumen* oder *Klafter etc. ?)
=== BRT bazu
6493:die  Peitsche  knaÜt'  Yt,  /o.  1 1 3 ;  —  j«/ . . , ,  j.  as.bazav-  Adj.  'mit  tUchtigen,  starken 'rä  kakvqn  (sd)  Vtio.113;    —   Ja/  -4?  Vorderbeinen,  -schenkein':    uströ .  .   'zSus iyimai)  zaya  frabanm^  aum  y5  ahurö  .  .    (fjs.)  aii.kaüß  Vt  14- 12. suwram   (sd.)  .  .    'ramca  '>   zaramo.paisim  I      Kpü.;  läMib  biryär  zur  az-ar  bäsuvän. V.2.6;-»^Ä0,™)  .,y«/(sdL)  -ra,^  .    -    ^.t,„,.   ^dj.    (auch    fem.)    'rid, V.2  10.  .)    inb»    dit    pntsteihcht   ,^iai\A   bringsnd':  /r.valml .  .    ,4    ■Is
12906:darttgö.bazav-
```


## [2026-09-05T13:47:11.182Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== POK bhaghus\"; grep -n \"b\\^ā?g\\|bhāghu\\|b\\^āg\\^u\\|Meaning: arm\" POK_full.txt | head -20",
 "description": "Pokorny arm root"
}
```


### [2026-09-05T13:47:11.234Z] TOOL RESULT

```
=== POK bhaghus
23340:Meaning: arm 
44576:Meaning: arm; thigh 
48771:Meaning: arm
```


## [2026-09-05T13:47:16.453Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '1820,1850p' HRN.txt; echo \"=== leaf\"; awk 'BEGIN{RS=\"\\f\"} {n++; if (index($0,\"np. boz \\047Klafter\")) print \"leaf(0-based):\", n-1}' HRN.txt",
 "description": "Horn context for baz Klafter"
}
```


## [2026-09-05T13:47:16.910Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '23330,23360p' POK_full.txt",
 "description": "Pokorny arm root entry"
}
```


### [2026-09-05T13:47:19.667Z] TOOL RESULT

```
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
LW. arm. bazuk (H. No. 48); oss. d. bäzug (Hübsch-
mann, S. 120, v. Stackeiberg, 3AMSTKA 5).
Gehört hierher auch np. boz 'Klafter (Vullers: 8),
'Spanne' (Vullers: 9)^), vergl. boze, also ursprünglich
'Armlänge, Elle'? Dann würde np. yüz 'Elle' (vergl.
sestyazt kernend. Sahn. I, 59 Vers 474) wohl nur auf
falscher Punktation beruhen und phlv. väz (AV.)
müsste für bäz stehen.
\;i68. haften 'weben', baf, n^ND 'Garbe' (Jer. 9, 21).
g. vaftmün.
Nach Bezzenberger bei Fick, Vergl. Wörtbch.*, I, 326
'Gemeindeweide', zu ai. sabhä- *Sippe*, das auch schon Darmesteter)
^t. ir. II, 131 in abä gesacht und wogegen Bartholomae, Litbl. f.
or. PhiL I, 19 sich ausgesprochen hatte.
Bartholomae schlägt mir brieflich für ap. ahäcuris die folgende
=== leaf
leaf(0-based): 59
```


### [2026-09-05T13:47:19.709Z] TOOL RESULT

```
Tocharian A kantu. Gen. kantwis, B kantwo. Obi. kantwa sa {*kantwa, reconverted with 
metathesis from *tankwa, Indo Germanic *dnghua). 

References: WP. I 1792, WH. I 806 f., Trautmann 104, Specht Dekl. 83, Havers 
Sprachtabu 123f. 
Page(s): 223 



Root / lemma: dous- 
Meaning: arm 

Note: 

Root/ lemma: dous-\ "arm' derived from an archaic root *^^e:/5'hand, arm' (see below). 

But she shift gh- > £/- is a unique Old pers., Baltic, celt., Illyrian-alb.. 

Material: Old Indie dos-n. (m.). Gen. dosnah^ forearm, arm, lower part of the forefoot with 

animals', Avestan daos- m. ' upper arm, shoulder', npers. f/ds "shoulder'; Old Irish doe 

{*dous-nt-s). Gen. o'oa/'arm'; Latvian pa-duse {zero grade) ' Achselhohle; Busen des 

Kleides '; sloven, pazduha, pazdiha besides pazuha, paziha 'armpit', and with the same d- 

loss (ein Erklarungsversuch by Berneker233 f.) Old Bulgarian etc pazucha'Koknoc;'. 



Note:
```


## [2026-09-05T13:47:32.985Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"Ellbogen\\|elbow, forearm\\|b\\^āg\\^u\" POK_full.txt | head -10; echo \"===\"; grep -n \"Page(s): 108\" POK_full.txt | head",
 "description": "Pokorny 108 bhaghu"
}
```


### [2026-09-05T13:47:33.047Z] TOOL RESULT

```
10620:gr. nnxuc;, Aeolic-Doric ttoxu^ " elbow, forearm ', Old Icelandic bogr, Akk. PL bogu^arm, 
===
10545:Page(s): 108-109 
86809:Page(s): 1080-1085 
86950:Page(s): 1086-1087 
87066:Page(s): 1088-1089
```


## [2026-09-05T13:47:35.006Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"بازه\" MON_part1.txt MON_part2.txt 2>/dev/null | head -10; echo \"=== BQT baz measure\"; grep -n \"باز . مقدار\\|فاصله میان دو دست\\|فاصلهٔ میان دو دست\" BQT_v1_pages.txt BQT_v2_pages.txt 2>/dev/null | head",
 "description": "Grep Mo'in and Borhan for bāzeh"
}
```


### [2026-09-05T13:47:35.147Z] TOOL RESULT

```
MON_part2.txt:221:غاز: 22 (.) نبازه حاجت؛ مق. ناز. 
MON_part2.txt:609:غباز: 7۵۳22 [- غبازه - گواز - گوازه - 
MON_part2.txt:4218:فاز: 7۶ |- فاژه] (.) خمبازه ۳ اش 
MON_part2.txt:12331:شکاری از دستة بازها که جثه‌اش از باز 
MON_part2.txt:28982:کیک در پاچه (بازه» شلوار) کسی افتادن: 
MON_part2.txt:35760:- غباز - غبازه| (ا.) چوبدستی باشد که گاو و 
MON_part2.txt:37211:بنفش رنگ است و در برابر بازها آبی رنگ 
MON_part2.txt:37973:لاطی: :۱2 (ع. لاطیْ] (افا.) امردبازه غلام 
MON_part2.txt:40058:زنی منقوش است (نظیر بی‌بی در بازهای 
MON_part2.txt:67085:منگ؛: ۸۵ (.) خمبازه؛ دهان دره. 
=== BQT baz measure
```


## [2026-09-05T13:47:38.248Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '10605,10640p' POK_full.txt",
 "description": "Pokorny bhaghu entry"
}
```


### [2026-09-05T13:47:38.298Z] TOOL RESULT

```
with ablaut Gothic botat "benefit'. Old Icelandic Old English bot' improvement, 
replacement ', Old High German buoz(a)i. "improvement, penance, atonement '. 

References: WP. II 151 f.. Feist 83, 103, 174, J. Weisweiler Bufte (1930). 
Page(s): 1 06 

Root / lemma: b^aghu-s 

Meaning: elbow, arm 

Material: Old Indie bahu-hm. "arm, esp. forearm; with animals forefoot ', Avestan bazau-s 

"arm'. Gen. it'azi/d (Armenian bazukirom dem Iran.); 

gr. nnxuc;, Aeolic-Doric ttoxu^ " elbow, forearm ', Old Icelandic bogr, Akk. PL bogu^arm, 
shoulder'. Old English it'o^ "shoulder, arm; twig, branch'. Old High German ,6*^0^ (Modern 
High German Bug) "shoulder, hip, haunch, point of shoulder of animals '; 

Tocharian A B poke, B pauke "arm'. 

References: WP. II 130. 
Page(s): 1 08 

Root / lemma: b^agh- 
Meaning: " mud, marsh ' 
See also: s. b^ogh-. 
Page(s): 1 08 



Root / lemma: b^ago-s 

Meaning: beech 

Grammatical information: f.
```


## [2026-09-05T13:48:28.573Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for p in \"aspa.bāra\\|aspa\\.bara\\|aspabāra\" \"xara\\.bāra\\|xarabāra\" \"gātu\\.bara\\|gātu\\.bāra\" \"gaoša\\.bara\\|gaosa\\.bara\" \"duš\\.bara\\|duz\\.bara\" \"mižda\\.bara\\|mizda\\.bara\" \"dātō\\.bara\\|dato\\.bara\" \"pairi\\.bar\\|pairi\\.baraiti\"; do echo \"### $p\"; grep -n \"$p\" BRT.txt | head -4; done",
 "description": "Grep Bartholomae for bara compounds"
}
```


## [2026-09-05T13:48:29.874Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== PHD burdan\"; grep -n \"burdan\\|bārag\\|bār \\[\\|xāyag\" PHD.txt PHD_mackenzie.txt | head -30",
 "description": "MacKenzie Pahlavi burdan bārag"
}
```


### [2026-09-05T13:48:30.762Z] TOOL RESULT

```
### aspa.bāra\|aspa\.bara\|aspabāra
### xara\.bāra\|xarabāra
### gātu\.bara\|gātu\.bāra
### gaoša\.bara\|gaosa\.bara
### duš\.bara\|duz\.bara
### mižda\.bara\|mizda\.bara
### dātō\.bara\|dato\.bara
### pairi\.bar\|pairi\.baraiti
2541:■ätfhö  °t(tt  sraolim  . .  pairi.barSmaAi  Yt //.?;  7(i')'
16856:barjttti  yä  ar^dulat  *apaititat  *ajayaurva   aSat    sraaäm    .  .  pairi.barämaiäe  Yt  //.
```


### [2026-09-05T13:48:30.814Z] TOOL RESULT

```
=== PHD burdan
PHD.txt:161:a- P- | M ?-] privative prefix, un-, Jess, а D] then (generally with a suffixed pronoun, e.g. 8-š). ab [M YA < А my';?p | M >b, N ~] water. B Soy 277 abad рр? | M Ра, N ~] populous, thriving, prosperous. ~ih: prosperity. ābādān [f*?t?*n' | N ~] thriving, prosperous, cultivated. ~ih: prosperity, cultivation. abādixšā(y) 'P?th? (d), v. pādixšā(y)] without authority, powerless. ~ih: powerlessness; anarchy. abādyāwand Pf?tyd”wnd | J ?b’dywn<d>] powerless, weak. ~ih: powerlessness, weakness. арар [LW TE < A lwt-h | M?Pg, N (a)bā] with. ~ih Dë kuk) company, assistance. abāgēnīdan, abāģēn- [^P'kyn-ytn!] accompany. a-bahr РРА] portionless, deprived. abām Pf?m | P ?bmyh, N (a)wàm] loan, debt. Abàn PPn! | M'0x, N ~] cal. 8th month; roth day. aband (nd, v. рапа | M ?bnd] erring. “АҺ: error. 'abar [ODM < А дат; bl | M "be, N bar] up; on, over. ~ āmadan: rise (sun). ~ āxistan: rise up. ~ āxrāmīdan: step up. — burdan : undertake. ~ madan: cope with, comprehend. ~ nigeridan: consider. ~ nihumbidan: conceal. ~ niSastan: sit, be enthroned. ~ nišāstan: seat, install. ~ rasidan: come to, upon. ~ rasidan б: attain. tabar Dél higher, superior. ~ag [-g | MP brg] superior. ~agan(ag) [-k’n(k)'] superior. --dar [-t, Zenit | M ?brdr] higher. ~dom [-twm | M ?brdwm] highest. —domih [-twmyh] superiority. abargar [5/21 god, divinity. abarig(àn) ['Bblyk( ny] = abarag. abarig DPryk! | M ?Pryg, J ?Pry] other.
PHD.txt:191:amāwandīh: power, strength. ambag [’mbk' | N anbajat] a preserve, conserve. ambar [mbl, ?nbl | Аг. ‘праг ambergris. ambarag [?mblk! | N anbara] hairless (animal). Р amburdan [h/^mbwultn! | Р ?mPr-] = hambārīdan. a-menīdār [^mynyt!l] unthinking. āmēxtan, āmēz- Pmyhtn', ?тус- | M *myxtn, ?myz-, N ~] mix. ~išn: mixture; element. āmiz [^myc] side dish, vegetables. āmēxtan, āmēz-, read hammóxtan, hammoóz-. Amurdād [?m(w)rdt' | N murdád] Immortality, the sixth Amahraspand, guardian of plants and food; cal. sth month; 7th day. āmurzīdan, āmurz- [mewlc-ytn! | M?mwrz-yd, N ~) forgive, pity, have mercy on. ~išn: mercy, forgiveness. Р amwaštan [h|mwstn! | P ?mwst] gather, collect. an- Pn- | M ’n-] prevocalic privative prefix, un-, -less. ап [ZK < A zk;?n! | M Ап, N ~] that, he. ~ 1: that of; with a qualifier preceding a noun, equivalent to a following 1 e.g. ап i ahlawàn ruwān = ruwan i ahlawān, the souls of the righteous. -ап [2s! | M An N ~] suffix forming (i) present participles, (ii) adverbs, (iii) plurals. ānāb-, —išn, v. ānāftan. an-ābādān Ppp’ rn'] uncultivated. an-abaxšāwand [m ph} wnd] unrepentant. ~ih: unrepentance. an-abāy Pr’ Pd) unfitting, improper. an-abēdān [”7?5yt?x'] useless, unwanted. ~th: uselessness. anübublag [9 fwhlk' = Av. anüpers0a-] inexpiable, unatonable; the highest degree of sin. an-abzār Pwi] unskilled, incapable. ~th: inability. an-ādān [*77:?x!] insolvent. ^h : insolvency. an-ádüg [tk] incapable. an-afsēnišn [”77?syx$n!] indestructible. ānāftan, ānāb- [77ftn',*775- | M ?w pt, Qn m-)] avert, reject, frustrate. ~išn: avoidance, warding off. anág [77 k! | M >ре} evil. ~th: evil, harm. an-ügàh и: | N ndgah] unaware, unwitting. anüg-kardàr [RU АРД, -kunisn [-kwnšn'] evil-doer, maleficent. anagr Pngl) infinite. ~an [”x! | M?nyr^n] Infinite Light; cal. 30th day.
PHD.txt:252:bāmdād [6’md’t' | М bmd?d, N ~] dawn, morning. bāmīģ [P myk!] brilliant, glorious. -bān [-??s! | M Aa, N ~] suffix, -keeper, -guard. band [bnd | = Р, N ~] bond, link. band-, v. bastan. bandag [bndk! | P bndg, N ~a] servant. bang [bng | N ~] henbane. bānūg [Pnwk! | N Бапи) lady. bar [b] | N ~] fruit, produce, profit. bar-, —išn, v. burdan. ībār [Pl | N ~] time, occasion. *bār [P1 | N ~] bank, shore. заг [D] | M P?r, N ~] fruit. ‘bar [b] | M br, N ~] load, burden; duty. bāraģ [5/А! | N ~a] mount, horse. barbut [blbwt! | N ~] lyre. bārestān [b/st?n'] patient, resigned. ~ih: patience, resignation. barig/k [b’lyk' | N bārīk (cf. tārīg)) thin, fine, subtle. bar-jamag [bly mk! | N ~a] saddle-bag. barómand [b wmnd | N ~] fruitful, prolific. barsom [blswm | M brswm] the bunch of twigs used in the Yasna cere- mony. baršnūm [b/s2wm] the major purification ritual. bastan, band- [ASLWN-tn! < A Vier bstn', bnd- | M bstn, (bn-), P bnd-, N ~] tie, bind. bāstān [b’st?n' | M PysPn, N ~] always, often. bas [YHWWNS | M P, N ~] be! (imperative of büdan, q.v.) baSkué [bskwe] gryphon. bašn [bén' | = P] top, peak; stature; mane (v. buš). baw-, —i$n, v. büdan. baxš-, —išn, v. baxtan. baxt [b()At! | N ~] fortune, fate. baxtan, baxš- [HLKWN-tn! < А У hig; bC)htn', bhf- | M bxt, bx$-, N baxsidan] apportion, distribute. ~išn: bestowal, distribution. bay [ORHY A < A */h; bk', bg | M by] god, lord. im ~: his Majesty. бу ~: his late Majesty. bayaspān [by’sp’n'] messenger, envoy.
PHD.txt:256:bayaspānļīh: mission, embassy. ~ig [-yk'] post-(horse). Бах [Pc | N ~] hawk, falcon. bāzā [b’c’y | (N bāzū)] arm. ~banag [-p'nk'] arm-guard, brassard. bazaģ [bck' | М beg, N ~a] sin, evil. —ih: = bazag. bazakkar [bckkl | M bzkr] sinful, sinner. bāzā-zanišnīh [by znfnyh = Av. bázu.jata-] a degree of sin. bazišn [dcšn'] division, part. bazm [bzm | — M, N —] meal, feast. ~-awurd [-zolt! | N ~] a sort of canapé. 1bë [BRA < A br | MP] but; out; ~... (enya), except. ~...enya...né: except... (otherwise)... not. ~ az: without. m 2be [BRA | M P, N bi-] particle with verbs, with 6, of indefinable function. -bed [-pt' | M -byd, N -balilud] suffix, -lord, -master. bēdom [bytwm | M bydwm] furthermost. béganag [byk’nk' | N ~a] strange; stranger. bégar [byk”/ | N ~] corvée, forced labour. béh [byh | N bih] quince. bel [by] | (M. Бу), N ~] spade. bélür [bylwl | M bylwr, N bilür] crystal. bérón [bylwn' | M byrwn, N bérün] outside. bëš [bys] pain, sorrow; harm, hostility. — burdan: bear hostility. bēš-, —i&n, v. bištan. bēšāz [byš(*)z] healing, medicinal. bēšāz(ēn)- [by?z(yn)-, byf?)c(yn)- | M byP?z-] heal, cure. —išnih: healing. bēš-burdār [byšbwlť’[] hostile. bëšidan [bysytn'] = bištan, bēšūmand [byš?*wmnd] sorrowful. béwar [Буш | M bywr, N ~] myriad, ten thousand. P bid [руй | P byd] again. bidaxš [byths] viceroy. *bifagàn [bch'n!] medicinal. bim [bym | = M, N ~] fear, terror. ~gén [-kn'] fearful, terrible. ~génih: fearfulness. --6mand [-'wmnd] fearful. *bistag [bstk! | N busta] hazelnut. biš [byf | N —] aconite. bištan, bé&- [bys-in' | M by$t, bys-] hurt, torment. ~išn: harm, torment. bize&k [dešk! | M bzyšk, N pizišk] doctor, physician.
PHD.txt:292:*brinj [binc | (M bryng), N birinj] bronze, brass. ~én [-yx!] bronze, brazen. brinómand [blyn’wmnd] delimited. brištan, bréz- [blystn', blyc- | M bryz-, N biristan] roast. brüg [blwk' | M brwg, N abrü] (eye)brow. büdan, b(aw)- [YHWWN-tn! < A yhwwn, У hwh; bwtn', b- | M bwdn, bw-, N büdan] be, become. bawišn: becoming, genesis. büf [bwp | N <), *büg [bwk'] owl. buland [bwind | = M, N ~] high. būm [bwm | N ~] land, earth, country. ~-€andag [-cndk'] earthquake. Ibun [bwn' | = M, N ~] base, foundation, bottom. *bun [bwn! | N ~] = wan. bunag [bznk! | N ~a] baggage; abode, camp. — daštan: dwell, settle. bun-dahišn(īh) [bzundhšn!, -yh] primal creation. bunih [bwnyh] beginning. buništ [bwnyst! | = M] foundation. ~ag [-k'] principle. bun-kadaģ [bwnktk'] original house, home. bun-xān [bwnh?n'] source. bur-, —išn, v. buridan. burāģ [bzoP RU] cutting, sharp. burām-, v. bram-. burd [bwit! | M bwrd] patient. ~ih: patience. burdan, bar- [Y BLWN-tn! < А У ybl; bwltn', bl- | M Бата, br-, N <] carry, bear, take, endure. ~išn: bearing, behaviour. burdār [bwit!]] bearer; womb. ~ih: patience. burd-ešnēhr [bwit! fnwhl | P bwrdyfnwhr] grateful, thankful. burg [bwig | (Ar. burj)] tower. buridan, bur- [bwl-ytn! | M bwr-, N ~] = bridan. —j$n: cutting. Burz [bwic] the god of agriculture. Burzénmihr [bwlcynmtr!] the third major Fire of Sasanian Eran, that of husbandmen. burzidan, burz- [bwlc-ytn'] praise, honour. ~i$n: praise, honour. —iŠnié : praiseworthy. buš [ро | N ~] mane. būšāsp [bwPsp | M bwsy'sp, N ~] sleep, sloth; dream. * but [bwt! | = M, N ~] Buddha; idol. buz [AZ < A ‘z; Бос | N ~] goat.
PHD.txt:376:gabr [gpl, gwbl | M gbr, N ? gór] hollow, cavity, womb. ~ih: hollowness. баё [gc | N ~] plaster, gypsum. -ёп [-yn!] (made of) plaster. gad [gt! = Av. gada-] club, mace. gādan, gày- [SL Y TWN-tn! < А V sry ?; g'tn! | N ~] copulate with. gadar [g??]] husband. gadwar [gtwl = Av. gaóawara-] bearing a club. 1gàh [gs | M ek, N ~] place, throne, bed. ?6àh [g’s | N ~] time; a fifth division of the day; = ģāhānbār. збаһ [gs] а Gatha, hymn. gah4n [g’s’n'] the Gathas; those scriptures dealing with spiritual and theological matters. ģāhānbār [gnb] | N gáhanbár] the six divisions of the year, the five-day festivals celebrated at the ends of these. ģāhānīg [g?snyk!] relating to the Gathas; spiritual; the five epact days at the end of the year. gahbed [g’spt' | N *gahbad] treasurer, banker. ~ih: treasurership. gahl [г()А | N gal] sorghum, giant millet. gāhüg [p hwk'] bier. gāhwārag [g’swlk' | N gāhwāra] cot, cradle. ģāl [2° household, following.
PHD.txt:390:hambār [kmb’l | N anbdr] store. hambārīdan, hambār- [hm-, hnb'l-ytn! | M hmb'r-, N anbürdan] fill, collect. hambasān [Anbs?n! | M *mbs*n] enemy, opponent. ~ig [-yk'] inimical, opposing. hambast [Ambst' | N anbast] compact. !hambastag [Ambstk' | N anbasta] formed, composed. shambastag [hnbstk' | М hmbst] collapsed, fallen. hambāstag [hmb’stk'] *all. īhambastan, hamband- [hmbsin', hmbnd-] form, compose; bind to- gether, intertwine, encircle. ~i8nih : binding together, intertwining. žhambastan, hambah- [%xbstn!, hnb?h- | M hmbst, hmbh-] collapse, fall down. VW "E. hambāstan, hambāh- [hnb’stn', hnb’d- | M hmb’stn, hmb’h-] cast down, demolish. ~išn: felling, demolition. ham-bašn [hmbén'] of the same stature. hambaw-, —išn, v. hambüdan. hambāy [hmb?g | (M hmb’w)] companion, partner; adversary. hambāz [hm-, hnb’c | M ?mP?z, N anbáz] partner. hambedig [%mbytyk!] = hambadig. hambēš-, —išn [hnbwi-, -£n! | N anbūšif] = hambüs-, ~išn, hambdy- (hnbwd- | M hwmbwy-, N anbóy-idan] smell (tr.). —ügih [-*kyh], —iŠn: (sense of) smell. hambüdan, hambaw- [hm-YHWWN-tn', v. büdan; hmbwtn'] be united, composed. „«išn(īh): union, composition. hambun [hmbwn'] (with a negative) not at all, not in the least. hambüsidan, hambūs- [hnbws-ytn' | N anbüsidan] come into being, be conceived. ~išn: conception. ham-dádestàn (hm-D YN A, -d'tsn! | N ham-dástán] agreeable, of the same opinion. hamdam [hmdm | N ~] intimate. ham-désag [hmdysk'] of the same form, homomorphous. hamë [hm’y | M Атуш, N ~] always. ^ ka: whenever. ham-ēdēn [m)ytwn! | N hamédün] likewise, similarly. bamé|ig (/um)yyk! | M тушур] eternal. ~iha [-yh’] eternally. hamémiil [mym] | = J] opponent, adversary. --īh: opposition. haménidan, hamén- [hmyn-ytn'] unite, compose. hamē-rawišnīh, hamē-ud-hamē-rawišnīh [(Amy W) hwy lwbsnyh) eternity.
PHD.txt:494:nab [np | N nawa] grandson. nabānazdišt [nb”nzdšt! = Av. nabünazdista-] next of kin. паї [w | M mp] family. ~ag [-R! | N náf(a)] navel. !naft [npt! | = M, N ~] moist, damp; naphtha. *naft [npt'] descendant. nahang [жле] province. *nakkira [nkyl’y] denying, repudiating. ~yih: repudiation. nāl- [wl- | P (n’r-), N ~] groan, complain. nam [nm | N ~] moisture. nám [SM < A £m; m | = M, N ~] name, fame. namad [nmt' | N <) felt. námag [MGLTA < A melt: ттк! | M пто, N пата] book, letter. namak [nmk! | M nmyhk, N ~] salt. namāz [OSGDE < A sgdh; nm’c | = M, N ~] reverence, prostration, prayer. ~ burdan: pay homage. nām-burdār [л?т bwlt?l | N ~] heir, preserving the father's name. nāmčišt [?жт-, ŠMcst'], (pad) ~: in particular, especially. ~ig [-yk'] famous, well known.
PHD.txt:538:pādīrān [p'igP n!] restrained, held back. pādīrān(ēn)īdan, pādirān(ēn)- [þptgľn(yn)-ytn'] restrain, impede. padīriftan, padir- [MK BLWN-tn!Ü < A mqbl, V qbl; ptgl-ptn! | M pdyr-yptn, N paóiruftan] receive, accept. ~išn: reception, acceptance. īpadisār [ptys' | N padīsār ?] beginning, basis. tpadisār [ptys’/] bridle, halter. padisāy [pts’d | M рдуу] on account of, for the sake of. padist [ptst! | P pdyst] promise, vow. & (abar) burdan: promise. padistadan, padist- [ptyst-”tn! | (P pdystwd)] promise, vow. padistā(£) [ptyst*k! | (M pdystw)] = padist. padiš (pts | M pdys] to him, it; postposition (= pad) to, etc. padištān [pryst?n' | P pdyst??n] leg. padišxwar [ptshwl] dish, bowl. pādixšā(y) [SL Y TA < A йур; p’ths?(d) | M раху] ruler; powerful, authoritative, authorized. ~ЛЬ : sovereignty, authority. pādixšīr [p’thsyl] agreement, treaty. pad-néróg [PW Nnylwk!] strong. pad-niģerišn [PWNnkylin'] cared for, guarded. pādofrāh [p’twpl’s) = pādifrāh. pad-panag [PWNpnk!] guarded, protected. Р pádrazm [p’tlcm] battle. pàd-rózag [p’tlwck' | M p'drweg] fasting. pād-uzwān [p’??wzw’n'] reticent. ~ih: reticence. pad-wizén [PW Nwcyn!] choice, select. pādyāb [pty | N ~] ritually clean; ceremonial ablution. ~ih : ceremonial ablution. pādyāwand [p?tyd’wnd | J p'dywnd] strong, powerful. cAh : strength, superiority. pádzahr [p’tzhl | N pa(d)zahr] bezoar, antidote. pad-zyān [PWNzyd"?n'] harmful. pafšār- [pps?/-] shame. pafšīr- [ppsyl-] be ashamed. ~i8n(ih): shame. pah [p’h] sheep. ~ast [-st'] sheep-fold, -pen. pahikaftan, pahikaf- [ptkp-tn! | M phykf-] fall on, touch, hit, attack. ~išn: attack, fight. pahikāftan, pahikāf- [ptk’p-in'] throw on, make fight. pahikar [ptk] | M phykr, N paykar] picture, image. pahikār [ptk?! | M phyk”r, N paykār] struggle, battle, dispute. īpahikār- [ptk?/-] fight, contend with, defeat. pahikardan, *pahikār- [ptk’/-tn'] request, claim, consult.
PHD.txt:605:wad-baxt [wtP ht! | N badbaxt] unfortunate. wad-dil [wtdyl | M wddyl, N baddil] coward(ly). wadgarih [wtglyh] evil-doing. wād-ģirdaģ [w° tgltk' | (N gird-bād)] whirlwind. wad-góhr [wtgwhl | N bad-gauhar] ill-, low-born. wad-kamag [wtk’mk'] malevolent. ~ih: malevolence. wadrang [w’ ting | N bādrang] citron. cc Dë [-bwd | N -bóya] lemon balm. wad|-tóhm [wttwhm] = wad-góhr. ~-wazag [-w’ck! | (N gawāža)] abuse. --.Xém [-hym] ill-natured. waf- [wp- | Р wf-, (N bàf-)] weave. ~išn: weaving. wafr [wp! | M wpr, N barf] snow. ~énag [-ynk!] а sweetmeat. waydān [wy?n! = Av. waybana-] head (ahuric). wahāg [wP?k! | M тор, N baha] trading; value. — burdan: value, estimate. wahār [wh], (bj?l) | M wkr, № bahar] spring. ~ig [-уЁ! | N -z] spring, vernal. wahig [ZZLA < A Semi (?); whyk' | M whyg, N *bahi] kid; astr. Capricorn. wahist [ол | M whyst, N bihist] paradise. ~Ig [-yk! | N -1] (worthy) of paradise. Wahman [whwmn' | M whmn, N bahman] Good Mind, the first Amahra- spand, guardian of cattle; cal. 11th month; 2nd day. wāhmān [*w-n! = whmn' | MOw^hmn, J whmn, N bahman] so-and-so. Wahrām [wlhl?’n', whPm | M whr’m, N bahram] god of war, victory; astr. Mars; cal. zoth day. ātaxš 1~: a major sacred fire. wak [wk! | N bak] frog. wālan [zo n! | (IN barzan)] settlement, community walg [wlg] = warg. walidan, wāl- [w]-ytn! | N bdlidan] grow, increase, prosper. ~išn: growth. wümidan, wam- [w’m-yin'] vomit. wan [wn' | N bun] tree; stock, stem. ~ i $urgünig : pistachio tree. ~ 1 was-téhmag: the Tree of Many Seeds. wān-, ~išn, v. wanidan. wanafšag [zvnpšk! | N bunafša) violet. Wanand [wnnd] astr. Vega. wandaģ [wndk'] rope, cord. wang [KALA < А ql’; wng | = M, N bang] voice, cry. wānīdan, wan- [wn-ytn! | M w’n-yst] conquer, overcome, destroy.
PHD.txt:663:xwāb [hw’b | N ~] sleep. xwābar [hw’l | M xwbr] beneficent. ~ig [-yk!] beneficial. —ih: beneficence, benefit. xwad [BNPSE < A b-nps-h; hwt' | M xwd, N ~] self; indeed. САҢ: selfhood, essence. xwaday [лору | M xwd'y, N ~] lord. ~th: lordship, sovereignty. ~war [-w’/] lordly. xwad-dósag [hwtdwsk'] self-indulgent. 7h : self-indulgence. xwah [AH TE < A *hth | N ~] sister. 1, ?x wüh-, ~išn, v. xwastan, xwāstan. xwahar [AH TEL v. xwah ; hw'hl | (M xwr), N xwdhar] sister. xwahl [eo hl | (M xwhr), № ~] bent, crooked. xwā(h)rīh [hw (h)yh | M xw'ryy] happiness, bliss. xwālist [hw’lyst' | (M xw’ryst)] sweetest. xwamn [hwmn', hmn' | M xwmn] sleep, dream. ~-wizar [-wc'/] interpreter of dreams, oneirocritic. xwān [hw!n! | M xw’n, N ~] tray, table. xwandan, xwān- [KRY TWN-, KLY TWN-tn! < А У д | M xwnd, xw'n-, N xwāndan) call, summon. Xwanirah [hwnyls = Av. x"aniraüa-] the central, inhabited continent of the earth. !xwar [kwl | M xwr, N ~] sun; cal. 11th day. Zwar [kwl = Av. x"ara-] a degree of sin. xwar-, —išn, v. xwardan. lxwàr [kw] | M xwr, N ~] light, easy; mean, abject. ~ih: ease; v. also x wührih. *xwar [%w/ | M xwr] food. xwür-, —išn, v. xwārīdan. xwaran [%w/n! | M xwrn] banquet. xwarāsān [hwlsn! | M xwr'?n, N ~] sunrise, east. xwār-bār [how?1b?l | M xwr w Pr, N ~] food and drink. xwardan, xwar- [OS TEN-tn! < Ath, V fth; hwltn! | M xwrdn, xwr-, N ~] eat, consume. ~išn: food. ~ignig : edible. ~išnīh: eating, consumption. xwardār [hwit?I] (legally) edible, not murdār. xwardig [hwityk' | M xwrdyg, N ~i] food. xwārēn [hw’lyn'] edible. xwārēn- [hw’lyn-] cause to eat, drink; feed; irrigate. xwarģ [wig | J xwwrg] ember. xwārīdan, xwār- [heo?1-ytnt] drink. —išn: drink, drinking.
PHD.txt:947:bear (v.) burdan; ~ offspring zādan,
PHD.txt:1166:carry burdan; ~ away wāzīdan.
PHD.txt:1767:endure burdan, pattüdan, (i)dan.
PHD.txt:1806:estimate wahāg burdan.
PHD.txt:1810:evening ēbārag; previous — dēš.
PHD.txt:2297:homage, pay — namaz burdan.
PHD.txt:2325:hostility ех; bear ~ bēš burdan.
PHD.txt:2856:mount bārag, stor.
PHD.txt:3013:oval xāyagdēs.
PHD.txt:3245:promise (v.) padist (abar) burdan, padistādan.
PHD.txt:3929:take burdan, griftan, stadan; — for pad... daštan.
PHD.txt:4123:undertake abar burdan, fraz griftan, pardaxtan 6.
PHD.txt:4191:value (v.) wahāg burdan.
PHD.txt:4207:vessel jām(ag), kabārag, takók.
PHD.txt:4782:gáy- gādanī wattart wattarīh! srawēn- srawēnīdan srūwēn ` sarw, sraw, srü srūwar sarw bar-! burdan! srub srubén Srūš srūšīg srūd srūdan sarmāg srub srešk srištan sardīh sard, srat
PHD.txt:4988:kaf- "kabāh kabārag kabīg kabiz
PHD_mackenzie.txt:679: - burdan: undertake.
PHD_mackenzie.txt:1008:P amburdan [hj>mbwltn' I P )mb)r-] = hambaridan.
PHD_mackenzie.txt:1493:bar-, ,,-,iin. v. burdan.
```


## [2026-09-05T13:48:44.729Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"== xwarbaran/dadwar/dastwar/muzdwar in PHD\"; grep -n \"xwarbarān\\|xwar-barān\\|dādwar\\|dastwar\\|muzdwar\\|mizdwar\\|jānwar\\|ganjwar\\|xāyag\" PHD.txt | head -20",
 "description": "MacKenzie for -war compounds"
}
```


### [2026-09-05T13:48:44.777Z] TOOL RESULT

```
== xwarbaran/dadwar/dastwar/muzdwar in PHD
306:īdabr [dpi] sinner, deceiver. *dabr [dpl] *dark-coloured. dad [dt' | M dd, N ~] wild animal. 1ааа [d't! | M d?d, N ~] law, justice; those scriptures dealing with legal matters. даа [d’t' | N ~] age. зааа [d>1!] tooth. tdād, v. ahlaw-dād. dādan, dah- [YH BWN-tn! < A Vyhb; d*tn!, dh- | M d'dn, (dy-), P dh- N ~, dih-] 1. give; 2. create. —išn [dh(y)sn'] giving, donation; creation. dādār [d’t?l | N ~] creator. -- ih : creatorship. dādestān [DYNA < А dyn; d'ts?n! | M d'(d)ys?n, N dá(de)stan] judgement, justice, law; case, process. dàd-gàh [2^? gs] proper place, fire temple; = daxmag. dādīg [d'tyk'] legal, concerned with the Law. dad-meh (d"tms] adult, elder. dādwar [d?twbl | (M d^ywr, P d'dbr), N da(d)war] judge. ~ih: judgement. daftan, dam- [dptn', dm- | M dm-, N dam-idan] breathe, blow. «dišn: breath. daftar [dptl | N —] register, account-book. dagr [AL YK < А ryk; dgl | M dgr > dur, N dër] long. dagrand [дата | N dërand] long. ~«xwaday [-hwt’y] eternal, of long dominion. daģr|-pattāy [dgl pt'd] long-lasting. -—-zamáàn [-2т?п!] a long time. ^-zi(w)isn [-zywsn'] long-lived. dah [ro, ASLY A < A ә | M dh, N ~] ten. dah-, —išn, v. dádan. Юаһаӣр [dř k' | (N Dahàk)] = Azdahág. dahān [РИМЕ < A p(w)m-h | M dhyn, N даһап] mouth. dahibed [dhywpt! | M dhybyd] ruler, lord of the land.
310:das [d’s | N ~] sickle. dàs?r [d’sl = Av. dātra-) gift, reward. dast [Y DE < A yd-h; dst! | = M, N ~] hand. dastag [dstk! | N —a] bunch, bundle, group. dast(a)gird [Y DE., dst-krt! | M dstygyrd, N dastgird] estate. dast- gir [dst OH DWN, (v. griftan) | N ~] 1. helper; 2. captive. dast-graw [dstglwb!] captivity. dast-kàrih [ҮЛЕ ГУА | N ~7] handiwork. dast-šūy [dstšwd] = ģūmēz. dastwar [dstwbl | М dstwr, N dastür] authority, priest, minister. ~th: custom; authority. dastyar [dstyd?l | (P dstd’r), N ~] helper. ~th: help, assistance. dašn [dšn! | = M] right hand. dāšn [d”$n' | M d’s(y)n] gift. dašnaģ [dsnk' | N ~a] 1. right hand; 2. dagger. dašt [dst! | = M, N —] plain, open ground. daštān [dft?n! | N ~] menstruation; menstruous. „estān [-st?n'] secluded place for menstruous women. -—--màh [-m?h] menstrual cycle. -ūmand [-’wmnd] menstruous. dāštan, dar- [YHSNN-tn! < А V ben: d^ftn', Pl- | M d'An, ar-, N ~] have, hold, keep, preserve. pad . . . dāštan: hold by, to; take for. pad éd dāštan [cf. N pindāštan] consider. --išn: preservation, maintenance. dāštār [4° #1 keeper, preserver. daw-, v. dawidan, dawistan. idawāl [dwb’l | N ~] leather, skin. ždawāl [dwbl | N ~] deceit, trickery. idawīdan, daw- [LH TWN-tn! < A Vrht; dwytn', dwb- | M dw-, N ~] run. *dawidan, daw- [dw-ytn'] speak (daevic). 1, 2 dawistan [LH TWN-stn!, dwstn'] = 1 * dawidan. daxmag [dhmk' | P dxmg, N ~a] tomb, dakhma (a building where corpses are exposed for destruction). „estān [-si?n!] cemetery. dax$ag [dhšk! | M dxsg] mark, sign, characteristic; memory. pad ~ dàštan : remember. az — hištan: forget. ~6mand [-’wmnd] marked. Day [ddw' | M dyy, N ~] Creator; cal. roth month; 8th, 15th, 23rd days. dayag [d^yk! | M d?yg-, N ~aj (wet-)nurse. „ānīh [nyh] | (N dāyagī)] nursing, nurture. dazidan, daz- [dc-ytn'] burn, scorch. --išn : burning.
897:authority dastwar(ih), sálárih.
1473:ar. custom dastwarih, éwén(ag). customary šūnīg.
2286:hireling mizdwar.
2816:minister dastwar; prime — wuzurg- framádar.
3013:oval xāyagdēs.
3220:priest āsrē, asrén, dastwar, hérbed, mowbed, māns?rbar; ~ hostile to Zoroaster karb; first officiating ~ zēt; second officiating ~ rāspīg.
4059:treasurer gahbed, ganjwar.
4861:mizdwar fro(x)s-t
5345:dastwar dastwarih jastan dastag dast(a)gird
5420:dūz-, duz- duzih gozihr duzdih duzidan duzidag ganjwar
5543:dādwar Sy тех dādwarīh xD у мехо Чачап, gādan 19545 āy-! - ot āmadan! VV Wrens jādūgīh AD SAMA jādūg VS MAT jādag-gūwīh A yr SU jadag-gow — SP 5tex5 jadag (EI EI dādmeh +36 ONS dādestān w^ FO) Per
```


## [2026-09-05T13:48:47.643Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"== BRT aspa bara\"; grep -n \"aspa\\.b\\|asp3\\.b\\|aspö\\.b\" BRT.txt | head -10; echo \"== BRT mizda\"; grep -n \"mizd3\\.b\\|mMa\\.b\\|mizda\" BRT.txt | head -10; echo \"== BRT data bara\"; grep -n \"dätö\\.b\\|dat3\\.b\\|d5t5\\.b\" BRT.txt | head -10; echo \"== BRT gaosa\"; grep -n \"gaoSö\\.\\|gaosa\\.\" BRT.txt | head -10",
 "description": "Bartholomae compounds attempts"
}
```


### [2026-09-05T13:48:47.743Z] TOOL RESULT

```
== BRT aspa bara
== BRT mizda
6189:Gen.  subj.  und  obj.:  alsm  *d>nidyäi{iA.) .  .  rayS  'st/  ". .  jrXoiiTOU  fioi'pai"  Y.  4J.  i ; —  abifra  (sd.) . .  ya  vaahsus  'sis  mananha Y._3i5.i3;  —  aiahya  yasa  {%A:)  'slm  y am iiyam  Y.  54.1;  —  °M/a  ^ae^ananqm viäu/(sd.)  ahurakya  mazdS  ".  .  des  AhM. Belohnungen  fiir  die  Taten  . ."  Y.2<V,4; — ■  nöit  kl  "M  *^ao^nanqm  vimysit  N. 16  ij);  —  zard>!ustrahe  .  .  asatinS  'itmia fravaiimca  yazamatde  Vr.  16. 2 ;  2,  Yt  13. 95;  —  tti  ahmt  nmane  Jamyarps  yh  asao- nqm  xshätas/a  'sayasca  . .  paitisatitayasla Y.  60. 2.  a)  mit  vanAav-  Adj.  und  aka^ Adj.  näher  bestimmt:  vatfkttyascä  °Ssi/ .. yS  ns  ara^ä  (sd.)  irmavaia^a  asanhäxs ^■5^-3't  —  syao^ana  mizdavqn  (sd.)  .. akfm  akai  vamthlm  'stm  vanhaavi  Y. 43. 5 ;  —  tSm  vatmklm  yasä  (sd.)  °sim  Y. 5;. ai;  —  maifyn  siaya  ahm  vaaAuya 'st  gaui  (sd)  Y.5/.  10«;  —  xmBth  afn- n>ntu  ahmya  nmsne  vawtklm  °/lm  i^a- parqm  Yt.  /J. i  S 7 ;  —  vaauAlsca  aöa  vaau- klsca  'sayS  Y.53.3;  —  yhca  tsi  gmh *aiura.mazda  ..  iSä  . .  vanukim  iihl/  'lim . .  ihm  .  .  *panndlm  yazamaidi  Y.^S. if  b)  Du.  'die  beiden,  beiderlei  Lose', d.  i.  (das)  gute  und  (das)  böse:  tmnanha (sd.) y5  dä%alibyd  priLratüm  xsayqs  'äfä*"^ üista  ". .,  der  über  beiderlei  Lose  gebietend den  Klugen  den  wahren  Ratav  versprochen hat"  Y.57.5.  A)  als  Gottheit,  die  die Lose,  insbesondere  die  guten  verteilt,  im jAw.  als  Göttin  des  durch  Frömmigkeit  ver- dienten Wohlstands*';  I)  im  gAw,:  Siraosö 'sfi  mqza.raya  (sd.)  Aacimnif  ya  vT  altl *ran3ibya  savlfi(sd.)  vldayäi  \ .  4j.  1 2 ; -^ sraosS  .  .  yU  *'li^  haiaiti  *mqxaraya  V. 27.6,  Vr. /2.1;  —  ya  vldayaf  'sts' (HS.) räshqm  (sd.)  Y.j^.  la;  —  ys  fta  'sSis aojaifha  var>dayaita  yqm  ,  .  gai^qm  .  . Y.  so.  3.  a)  Du,  in  Verbindung  mit armaiay-  Du.  ^A.  und  Arm.':  yads  ahm zivlm  (sd.)  .  ,  mazdasca  .  .  'sicil  armaitl Y.31.^.  II)  im  jAw.:  yö  'lim  yazäite ..k5  mihnm  yazaiieY\..i-j.2;  —  -/j  (VS.) srlre  'si  banumaili  .  .  °li  dä'ire  vehäm i^arifiilYt.sy.^;  6of.*;  —  hm  hacSl  'Hl pourvsj^ä'iira'Yt  /j?.54;  — /rä  mqm  aiwt.- urvalsayatfuha  marsdik?m  'al  (als  VS.) hnzaiti  Yl  77. 1 5 ;  —  'lim  . .  darr/S.- variiman3m..bartntltn  vispä  baSlazsY.S'i. 2;  —  sraohmla  'lim  nairXmca  sauh>m IVyt.40;   —  fravalays   .  .    'Isil  balsaza
6412:•  j.  asö.mizda-  Adj.  (fem.  °dä^  'den Lohn  der  Gerechtigkeit  eintragend':  ta (näml,  gai:ä)  nS  buyan  humizda  (sd.)  .  . 'da  Y.  5J.  3.
10442:fravartis  agarbäyatä  "Fr.  wurde  gefangen  i genommen"  Bh.  2. 13.  E  3)  'etwas  weg- 1 nehmen  von— (Abi.)':  g}urvaya  Äipälai'e. sävar»  Y.  r).  28.  4)  'einen  Anteil  be- ! kommen  von  — '  (Gen.):  tnä  hl  mairyö'. giurvayöit  "nicht  soll  davon  was  be- kommen , ."  Yt.  8. 59;  —  yezi  se  mairys gfurvay.V  Yt.Äöo;  —  mizdahe  .  .  g>r)W- 1 ytiti  yS  girswyaUe  VyL  JO  (?).  5)  'i^-
20563:•  j.,  g.  mizda-''  n.  i)  TLohn'  als  das  ver- abredete oder  zugesicherte  oder  gebührende Äquivalent  einer  Leistung  (usw.) :  kaiä  . . tal  'dim  Aan^nl{sd.)  äasä  aspa  arinavattjs (sd.)  ..hyat  m5i ..  aj/hai/r {sd.)  \.44-i&;
20570:•  g.  mizda'vant-  Adj.  'mit  dem  (gebühren- den) Lohn  (in  beiderlei  Sinn,  Lohn  tind Strafe)  versehen':  hyat  da  syaokana  'von (APn.)  yäiä  uxiä  akSm  akäi  vanuAlm asim  vanhaov?  "wie  du  den  Taten  ihren Lohn  bestimmtest''  und  den  Worten,  das böse  Los  dem  Bösen,  das  gute  dem  Guten"
30412:humizda-
30445:•  j.  hu-mizda-  Adj.  (fem.  'da-)  'schönen, guten  Lohn  bringend ,  eintragend' :  tä (nämL^aSi)  nS  buyan  °da  aijniidä  a^.-
== BRT data bara
13305:•  j.  dätö.baeSaza-  Adj.  '(Arzt,)  der  mit dem  Gesetz  heilt' :  a!5.balsaz3  -zö . .  inq'irB.- balsasd  (sd.)  Yt^.  6.
== BRT gaosa
9895:•  j.  gaoSö.baraz-  f.  'Höhe  des  Ohrs': ä^ritlM  xsa'hrS.k^ntake  (sd.)  'zS  us.iäva- yuit{%±)  "^.46.
```


## [2026-09-05T13:49:04.074Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"== KNT asabara\"; grep -n \"asabāra\\|asabara\\|asa-bāra\" KNT.txt | head -5; echo \"== HRN leaf 89 (p68)\"; awk 'BEGIN{RS=\"\\f\"} NR==90' HRN.txt | head -40",
 "description": "Kent asabara; Horn p.68"
}
```


### [2026-09-05T13:49:06.174Z] TOOL RESULT

```
== KNT asabara
1788:VI. The vocalism of the root varies in these for- mations, being either -a- (pIE -e- or -о- or -a-), as in baga-, bara-, daiva-; or à zero grade, as in karša-, u-zma-, darga- (see Lex. s.vv.); or a vriddhied or lengthened grade (§126), as in kdma-, asa-bāra-, Margava-.
3586:Техт or DB, Сошмх П: 1 :98ty : Dárayavaus : xSayafiya : paeüva : Naditabaira : ha 2 dà : kamnaibis : asabaraibis : amufa : Bübirum : ašiya 3 va: pasàva : adam : Babirum : ašiyavam : vasnd : Auramazdiha : uta : Ba 4 birum : agarbiyam : uta : avam : Naditabairam : agarbüyam : pasáva : ava 5 m : Naditabairam : adam : Babirauv : avüjanam —— :0ütüy : Dārayavauš : x 6 Sdyabiya : yātā : adam : Bübirauv : àham : ima : dahydva : tyà : hacàma : ha 7 migiyà : abava : Рагва : Üvja : Mada : Aðurā : Mudráya : Parfava : Margus : Өз 8 tagui:Saka : абу : Dārayavauš : x8dyabiya : I martiya : Martiya : nā Q ma : Cicixrais : puca : Kuganakà : пата : vardanam : Pársaty : avada : adaraya : 10 hauv : udapatatà : Uvjaiy : Кагаһуй : avaðā : afaha : adam : Imanis : amiy : 0 11 vjeiy :xSdyafiya —— : @atiy : Darayavaus : zsayattya : adakaiy : adam : asna 12 iy : àham : abiy : Üvjam : pasáva : hac&ma : alarsa : Üvjiy& : avam : Marti 13 yam :agarbaya : hyašām : mafista : dha : шат : avàjana — : 00у: D 14 árayavaus : xSiyafiya : І martiya : Fravartiá : пата : Мада : hauv : udapatat 15 à : Madaiy : Катаһуй : ауаба : абала : adam : XSa6rita : amìy : Uvaxdtrah 16 уй : taumàyá : pasáva : kāra : Mada : hya : v'àpaliy : haw : hacáma : hamiciya : a 17 bava : abiy : avam : Fravartim : aSiyava : hauv : тёйуайтуа : abava : Madaiy 18 9àtry : Dárayavaus : xšāyaðiya : kara : Parsa : ша : Мада : bya : ира : mim : 4 19 ha : hauv : kamnam : aha : раѕауа : adam : kdram : fraiSayam : Vidarna : пата : Pársa : man 7 20 à : badaka : avam&àm : mafistam : akunavam : avataSaám : afaham : parait : avam : К 2] dram : tyam : Madam : jatà : hya : mand : пау : gaubataiy : pasiva : hauv : Vidarna : ha 22 dà : kara : айуауа : yafà : Madam : parárasa : Māruš : пата : vardanam : Ma 23 дау : ауада : hamaranam : akunaus : hada : Мада : һуа : Màdaisuvà 24 :ma(iSta : dha : hauv : adakaiy : пау : avadà : аһа : Auramazdimary : u 25 раѕійт : арага : vasnà : Auramazdáha : kāra : hya : тара : avam : kàram : t 26 yam : hamiciyam : aja : vasiy : Animakahya : mähyä : XXVII : raueabis : fakat 27 à : аһа : avatüsám : hamaranam : kartam : pasáva : hauv : Ката : һуа : manā : Карада : пат 28 à : dahydus : Mádaiy : avadà : mam : amánaiya : y8tà : adam : arasam : Mada ' 20m : 08у : Dàrayavaus : xšāyaðiya : адаг х : nàma : Arminiya : man 30 à : badaka : avam : adam : frāišayam : Árminam : avafasazy : aaham : paraidiy : ka 31 ra : һуа : hamigiya : mană : naiy : gaubataiy : avam : jadiy : pasiva : Dadarsi 32 š : aSiyava : yafà : Arminam : parárasa : pasáva : hamigiya : hagmatà : paral 33 tà : patiš : Dādaršim : hamaranam : cartanaiy : Züzahya : пата : àvahanam : А 34 rmíniyaiy : avadà : hamaranam : akunava : Auramazdimaiy : upastàm : a 35 bara : vasnà : Auramazdàha : kāra : һуа : manā : avam : küram : {уаш : hamigiyam : 36 aja : vasiy : Oüravaharahya : máhya : VIII : raucabis : 09akatà : dha : ava 87 à$üm : hamaranam :kartam : бабу : Dárayavaus : z3àyaffya : patiy : duv 38 itiyam : hamigiyà : hagmatà : paraitd : patiš : Dàdar&im : hamaranam : carta 3€ nay : Tigra : пата : didà : Arm‘niyavy : avadà : hamaranam : akunava : А 40 uramazdàmaiy : upastàm : арага : vašnā : Ашатагдаћа : kāra : һуа : тапа :a 41 vam : káram : tyam : hamigiyam : aja : vasiy : G9üravüharahya : mihya : ХҮШ 42 :raueabiá : бакаќа : аһа : ауабадат : hamaranam : kartam —— : 00у : Daraya 43 vaus : xšāyaðiya : patiy : citiyam : hamictyd : hagmatà : paraita : pat 44 iš : Dádar&im : hamaranam : cartanaiy : Uyama : nama : didi : Arm'myaty :a 45 vadā : hamaranam : akunava : Auramazdimaiy : upastam : арага : vaSnà : Aurama 46 zdàha : kāra : һуа : manā : avam : küram : tyam : ham?giyam : aja : vasiy : Oàigarea 7 d :mábyà : IX : raucabis : Nakata : dha : ауада ат : hamaranam : kartam : pasava 48 : Dadarsis : citā : mim : amánaya : Arm/niyaiy : yiti : adam : arasam : Ма
3614:71 šāyaðiya : pasàva : hauv : Fravarüs : hada : kamnaibi$ : asabāraibiš : amufa : Ra _
3751:72 15 : asabaraibis : айтуауа : Aršādā : пата : didà : Harauvatiyà : а 73 vapara : atiy&i$g pasáva : Vivàna : hada : kara : nipadiy : tyaiy :aNya © 7777 74 va : avadāšim : agarbaya : ula : martiya : tyaisaly : fratama : anuSiya :
5215:wasabdra- sb. ‘good horseman’: u- ‘good’ + asabāra- ‘horseman’, with vriddhi ($126). uvāsa- bara nsm. DNb 42.
== HRN leaf 89 (p68)
— 68 —
kurd, per e; af}'. parün; oss. vergl. /ar- (274, 1);
bei. paran- 'darüber hinaus gehend' (284).*
304. pervär *Stair^).
aw. *2)airivära?ia-, vergl. pairi.vära- 'Wall*, 'Stall'
(vd. 2, 26 vielleicht, Bartholomae); phlv. {pä-amün-)
parvär,
eS05. perväi^ 'Flug .
aw. pairi (oder para) — V^vciz-, 'herum- bezw. weg-
fliegen , vergl. vazaiti er fliegt*.
306. jyerwerden ernähren, erziehen*, periveris, perwer'tden,
pari -f- y^hhar-; phlv. partoarfan, partvar(i)sn,
307. pervez 'siegreich*.
phlv. aparvej 'siegreich'; wohl zu «r^i, be.ze (No. 253)?
Dann perwez.
308. pervfn 'Plejaden*.
aw. paoiryaeinyas\ca (yt. 8, 12), de Lagarde, Beitr.
z. altb. Lex. 56.
af/. peröne; bei. panvar 'Plejaden (Dam es, 54).
309. perhey(ten 'sich enthalten ; sich hüten', Praes. perliez-etn^
perhez, perheztden^).
aw. palti + [/ra^c- 'verlassen'; phlv. pahre/tan
'sich enthalten', pahrej, pahrej(i)sn.
kurd. pärlstin, dispärise 'ist enthaltsam, enthält sich*.
^) Die persischen Original Wörterbücher geben für hervär (No. 210)
und pervär (die de Lagarde schon geschieden hat) zusammen die
folgenden Formen an : pervär^ perräre, perbär, perbärff perbäl, perbcUe^
fervür^ ferväre (vergl. No. 82S)^ fet'väl^ ferväle . von denen die mit/
beginnenden in dieser Bedeutung gewiss falsch sind. Als Beleg für
die Bedeutung *Stall* dient ein Vers des Xäqänl (Metrum: Munsarih).
röz^ beperrär^ büd^ färbe ez an sude cünin
seb tSn-t himär^ däst läylr ez an sude dun an
^) Die Annahme , dass np. pärsä 'enthaltsam , fromm*, aus
*perhezä (eine solche Form construirt sich Darmesteter, Et. ir. I,
115, NB. ohne Stern) contrahirt sei, ist durchaus unstatthaft. Pärsä
bedeutet überhaupt nicht 'enthaltsam', sondern ursprünglich nur *brav*
(vergl. Sahn. I, 35 Vers 15, 70 Vers 158 u. o.), es bezeichnet gewiss
eigentlich den Pärsen.
```


## [2026-09-05T13:49:14.177Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==262' HRN.txt | head -50",
 "description": "Horn p.240"
}
```


### [2026-09-05T13:49:16.494Z] TOOL RESULT

```
240 —
V, w.
1071. if, ü (§ähn. I, 25 Vers 37) und*.
ap. tää auch, und'; aw. uta; phlv. u (päz. ?/).
Bei diesem vielgebrauchten Worte ist die nicht
lautgesetzliche starke Verkürzung durchaus erklärlich.
Die Aussprache ve (die wohl AM. noch nicht hat,
vergl. z. B. S. 82, Zeile 3 v. u.) ist Nachahmung des
arab. va und* oder dieses ist selbst entlehnt worden.
Oder gehört np. ü und' zu gr. av, got. auk etc.
(vergl. Kluge, Wörterbuch s.v. auch)? Man sollte
aber doch wohl eine Anknüpfung der Partikel im
iranischen Gebiete erwarten können.
wä *offen', siehe baz (No. 163).
1072. väj 'sprich', vergl. vat 'Wort, Rede' (dialektisch^),
guväze 'Schmähung*, gtwäSzden, schelten' (unbelegt).
g. vätrnun 'sprechen' (vergl. Justi, ZDM6. 36,
403, 404) ; Käs. Q. K. vöj^ 7j, vaz (s. v. f^eda kerden),
Käs. V. bivötdn, Impt. böj, Q. vötin, bavöten, Praes.
avöjün, K. vötmün^ Impt. hSvöJtd^ Z. bSvöt, Praes. vözön
'sprechen' (s. v. giiften).
aw. {/"vac-y vaocat 'sprechen' ; phlv. väöak 'Stimme',
väc (päz. väz) *Gebet'; ai. l/vac-^ vivakti, vdc- *Wort\
kurd. vdtin, vergl. bezium 'ich sage, spreche' etc.
(Justi, No. 408.)
Das in den Dialekten noch heute allein gebräuch-
liche Verbum ist schon im PehlevT fast verschwunden.
1073. "WäTj -wäre, tver (ür)^), Suffix 'tragend, versehen
mit'.
ap. -bara- in taka]bara' 'tragend'; aw. gada^vara-;
phlv. 'bar in datbar (neben datwar), dastbar, m(i)zdbar,
'tvar, war in nmetwär, öjwar^ ranjfwar; arm. -ber^
z. B. Insaber, -avor^ z. B. lusavor.
M Belegt durch einen Vers des Mir NezmI.
V
*J In mizdür Sahn. (M oh 1) VI, 152 Vers 330, genjür^ renjür u. a. m.
```


## [2026-09-05T13:49:25.484Z] TOOL CALL #29: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 3
}
```


### [2026-09-05T13:49:25.490Z] TOOL RESULT

```


```


## [2026-09-05T13:49:27.949Z] TOOL CALL #30: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/caviar",
 "prompt": "Full etymology of caviar, including the Persian and Turkish forms and the meaning of each element."
}
```


## [2026-09-05T13:49:29.551Z] TOOL CALL #31: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AE%D8%A7%D9%88%DB%8C%D8%A7%D8%B1",
 "prompt": "Etymology of Persian خاویار (xāviyār): what elements is it analysed into, and what sources are cited?"
}
```


### [2026-09-05T13:49:34.363Z] TOOL RESULT

```
# Etymology of Caviar

The word **caviar** entered English around the 1550s, referring to "roe of certain large fish, salted and served as food." It traveled through multiple languages before reaching English:

The term derives from French *caviar*, which came from Italian *caviaro* or Turkish *khaviar*. These ultimately trace back to Persian *khaviyar*, composed of two elements:

- **khaya** ("egg") — from Middle Persian *khayak*, itself descended from Old Iranian *qvyaka-*
- **dar** ("bearing") — a Persian suffix

The Persian root connects to an ancient Proto-Indo-European word meaning "egg" (*ōwyo-* or *ōyyo-*), which may derive from a root (*awi-*) associated with "bird."

Interestingly, Russian adopted a completely different term: *ikra*, which does not share this etymological path. The word's journey from Persian through Turkish and Italian before entering European languages reflects the historical trade routes through which this luxury food traveled westward.
```


### [2026-09-05T13:49:36.067Z] TOOL RESULT

```
# Etymology of Persian خاویار (xāviyār)

According to the Wiktionary entry, the Persian word is analyzed as a compound formed in another Indo-Iranian language. Specifically, it consists of:

1. **"Ossetian کӕف (kæf, 'fish')"** compounded with
2. **"Romani jaro"** (which derives from Proto-Indo-Aryan *Hāndrám, related to Sanskrit आण्ड (āṇḍa, "egg"))

This composition yields the literal meaning **"fish-eggs."**

## Sources Cited

Two academic sources are referenced:

1. Szemerényi, Oswald (1967) — "Славянская этимология на индоевропейском фоне" in *Вопросы языкознания*

2. Shukurov, Rustam (2016) — *The Byzantine Turks, 1204–1461*, published by Brill (page 325)
```


## [2026-09-05T13:49:45.867Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"== PLA barid\"; grep -n -i \"barīd\\|barid\\|بريد\" incoming/PLA/PLA_pages.txt | head -20",
 "description": "Asbaghi on barid"
}
```


### [2026-09-05T13:49:45.915Z] TOOL RESULT

```
== PLA barid
2721:»%- burud: Pl. v. »; barid s. barid.
3005: ap2-          barid:           "Post,           Bote"         pers.     8 aus          dem    pers.          ©,»    burdan    "tragen"       mp.
6503:#23                - bumbaridi = humbardi s. humbardi.
```


## [2026-09-05T13:49:47.213Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"== AFM barid\"; grep -n \"البريد\\|بريد\" AFM_pages.txt | head -10; echo \"== TAD\"; grep -n \"بريد\" TAD_pages.txt | head -10; echo \"== AKD veredus\"; grep -n -i \"veredus\\|barid\" AKD.txt | head -10",
 "description": "Addi Shir, Unaysi, Zimmern on barid"
}
```


### [2026-09-05T13:49:47.280Z] TOOL RESULT

```
== AFM barid
470:( البريد) قبل اصله متا" 80 0360 5 85 ܙܥ̈ܝܐ. - وقبل ܓ اصلة
472:الرومي على ܐܢܚܨܢ ٠‏ والبريد الرسول ومئة قول بعض العرب « ܨܢ بريد الوت >
473:اي رسوله ثم استعمل في المسافة التي يقطعها وهي ¥( ميا وخيل البريد اسل
475:على دواب البريد
3098:الفرنيذ) معرب بريد وهو نوع من الملواء 'يصّع من السك ودقيق الشعير
5350:نبريده ١6١‏
== TAD
626:        ‫اوسطة ‪ -‬ايطالي ‪ 85‬وهو البريد ومعناه في الاصل موضم ومحطة‬
645:                           ‫معناه طابعم رأدفه طابعبريد‬       ‫ول | ايطاللي ‪0‬‬
1920: ‫فابريدازا معناه أحاط بالثيء‬           ‫فردوس‪ -‬لفظ فارسي قددم نهم‬
== AKD veredus
85:akk.  purldu,  peredu  eilig  :  >  wohl  arab.-pers.  band  Eilbote  und viell.  auch  spätlat.  veredus  Eilpferd  (s.  hierzu  noch  unten  S.  50).  Zu
770:„Bein",  als  „Eilbote"  i  :  >  viell.  arab.-pers.  barid  Eilbote,  Eilpferd  (>  vieU. lat.  veredus  (spätgriech.  ßigaiSog)  Eilpferd  O,  bezw.  aus  paraveredus, deutsch  Pferd);  falls  nicht  umgekehrt  hier  das  Arab.-Pers.  <;  Griech.-Lat. <;  Gall.).     Vgl.  auch  oben  S.  7  zu  pundu  Eilbote.  Zu  akk.  tire
```


## [2026-09-05T13:50:03.316Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"PLA leaf:\"; awk 'BEGIN{RS=\"\\f\"} {n++; if (index($0,\"\\\"Post,\")) print n}' incoming/PLA/PLA_pages.txt; echo \"AFM leaf:\"; awk 'BEGIN{RS=\"\\f\"} {n++; if (index($0,\"( البريد)\")) print n}' AFM_pages.txt; echo \"AKD leaf:\"; awk 'BEGIN{RS=\"\\f\"} {n++; if (index($0,\"purldu\")) print n; if (index($0,\"als  „Eilbote\\\"\")) print \"p50cand:\",n}' AKD.txt; echo \"PLA offset hint:\"; python3 -c \"\nimport json;d=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'));print(d['PLA'].get('page_offset'));print(d['AFM'].get('page_offset'))\"",
 "description": "Locate leaves/pages of found entries"
}
```


## [2026-09-05T13:50:04.416Z] TOOL CALL #35: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A8%D8%B1%D9%8A%D8%AF",
 "prompt": "Etymology of Arabic بريد (barīd): what origin is given (Latin veredus? Persian burdan? Akkadian?) and what sources are cited?"
}
```


### [2026-09-05T13:50:05.641Z] TOOL RESULT

```
PLA leaf:
63
AFM leaf:
20
AKD leaf:
16
p50cand: 60
PLA offset hint:
301 leaves (pdftotext -layout, \f-separated): printed page = leaf(1-based) − 15 (leaf 291 = p.276).
198 leaves; page numerals OCR'd unreliably — offset approx leaf − 8 (front matter); confirm on page image
```


### [2026-09-05T13:50:14.530Z] TOOL RESULT

```
# Etymology of Arabic بريد (barīd)

The primary etymology given is **Latin origin**. The word traces back through Byzantine Greek *βέρηδος* (bérēdos) from Ancient Greek *βέρεδος* (béredos), which borrowed from Latin *verēdus*. This ultimately derives from Gaulish *werēdos* and Proto-Celtic *uɸoreidos* ("horse").

## Alternative etymologies discussed but rejected:

The references section addresses several competing theories:

1. **Persian origin**: A persistent folk etymology claiming connection to Persian *بریده* (burida, "docked"), supposedly referencing horses marked by Darius the Great. This is "refuted" by historical scholarship.

2. **Akkadian origin**: Zimmern proposed borrowing from Akkadian *PAP.ḪAL* (purīdu, "leg; roaming one"), though this remains speculative.

3. **Hebrew connection**: Lane's suggestion linking it to Hebrew *פֶּרֶד* (péreḏ, "mule") is noted as "another false etymology."

## Key sources cited:

- Ullmann, Manfred (1997) - "tracks the history of the word by two hundred quotes"
- Quatremère (1845) - "already recognized the Roman derivation"
- Sourdel (1960) - Confused analysis in Encyclopaedia of Islam
- Lane (1863-1893) - Arabic-English Lexicon
- Corriente et al. (2017) - French dictionary acknowledging Latin origin

The Latin/Greek pathway is the scholarly consensus presented here.
```


## [2026-09-05T13:50:24.653Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== PLA leaf63\"; awk 'BEGIN{RS=\"\\f\"} NR==63' incoming/PLA/PLA_pages.txt | sed -n '1,40p'; echo; echo \"=== AKD leaf 60 head\"; awk 'BEGIN{RS=\"\\f\"} NR==60' AKD.txt | head -12",
 "description": "Read Asbaghi and Zimmern entries"
}
```


### [2026-09-05T13:50:26.852Z] TOOL RESULT

```
=== PLA leaf63
barwäna                                                                           48                                                 bazädara



ls.            -    barwäna:              "Portier,             Türhüter,              Pförtner,          Wächter"         pers.   1, wahr-
          scheinlich                eine         verfälschte             Form          für    pers.      ol_, darban          <T mp.), dar
                    aw.    dvar,            ap.       duvara         + mp.        ru Pän v.             Verb       pätan   "schützen"     Toaw.,
          ap.       pay.


ls»            - barwanag:                  "Wegführer,                Führer"          aus    dem       pers.       ol.      parwana mp.
                         n                                                9,                                                  TE———
           3?»            parwänak,                 syr.       Lw.     }010'% 2, mand.                   paruanga.


2210                 -     bar$äwa$:                  "Koriander"           = barsiyäwaßän                    s.    barsiyawasan     3,

      u
ob,                , - barkäwalän                     = barsiyäwajäan                  s. barsiyäwaßän                4,

2          -       burüunz:         "Bronze"               =   burunz        s.    burunz          5,


G#»>-               burünzi:              Nisba          v.    burünz        s.    burünz          6,


_22>- barwiz:                       Pl. v. >). barwaz                        s. barwäz.

 ale. - barhanänaf:                                   "Pflanzenart"               pers.       7.

 ap2-          barid:           "Post,           Bote"         pers.     8 aus          dem    pers.          ©,»    burdan    "tragen"       mp.
           (2) burtan                     a.               / ep.      bar     >>         verdus          !°


rer barigam                         - abrisam s.                 abrisam

 o»1»- bazädara:                            "Falkner"            s.,|,,\               bäzdär il,




=== AKD leaf 60 head
inrühren,  mengen  (spez.  von  Heilkräutern
u.  ä.)  :  >■  vieU.  jüd.-aram.  rahiMa  Eingerühi'tes  O  viell.  späthebr.  rühak, sowie  arab.  rabaJca,  rabiJcat).  Zu  akk.  stpu  Paste,  s.  unten
S.  61.
      50      
13.   Tiere.
akk.  sisü  Pferd  wird  im  Babyl.  ebenso  Fi-emd"w.  sein,  wie  süsjä im  Aram.,  säs  im  Hebr.  O  ägypt.  ssm-(  für  säsim).  Über  Herkunft  des "Wortes  und  gegenseitiges  Verhältnis  der  Entlehnungen  läßt  sich  aber  noch nichts  Sicheres  sagen.  akk.  pundu,  piridu  eig.  „Eiler",  daher  sowohl
„Bein",  als  „Eilbote"  i  :  >  viell.  arab.-pers.  barid  Eilbote,  Eilpferd  (>  vieU. lat.  veredus  (spätgriech.  ßigaiSog)  Eilpferd  O,  bezw.  aus  paraveredus, deutsch  Pferd);  falls  nicht  umgekehrt  hier  das  Arab.-Pers.  <;  Griech.-Lat. <;  Gall.).     Vgl.  auch  oben  S.  7  zu  pundu  Eilbote.  Zu  akk.  tire
Hengste,  uräti  Stuten  s.  oben  S.  42  unter  urü  Stall.  akk.  kudänu,
Jcudannu,  Jcudtnu,  Jcudiinu  Maultier  (viell.  auch  im  Akk.  Fremdw.)  :  ^ wohl  aram.  hödna,  ködanjä,  tem.  hödantä  Oarab.  Jcaudan,  desgl.  mittelpers. kötlna).
akk.  immerti  Lamm  :  >  wahrsch.  aram.  ^immdrä,  "emmar  O  arab. 'immar).  akk.   niqü  Trankopfer,    Opfer,    Schafopfer   :   >>   wohl
sj'r.  neqjä  Schaf.     Vgl.  noch  unten  S.  65f.  zu  akk.  naqü  opfern, akk.  humstru  Schwein,  Eber,  als  N.   pr.  auch  hamziru  und  haba.flru  : ob  damit  hebr.  häztr,  aram.  Ijäsira,  hezlrä,  auch  hmsirä,  urverwandt  sind oder  entlehnt,   ist  nicht  leicht  zu  entscheiden.     Arab.  Jiinzir,   dial.  lumzlr, desgl.  äth.  hanzir  sind  dagegen  wohl  sicher  <i  aram.
[akk.  gammalu,  gammallu  Kamel,  wohl  <;  westsem.  (hebr.  gämäl, aram.  gamlä,   arab.  gamal,  >  griech.  xdfA.ifkos,  Kamel).]  [akk.  ihiln
```


## [2026-09-05T13:50:42.394Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== AFM leaf20\"; awk 'BEGIN{RS=\"\\f\"} NR==20' AFM_pages.txt | sed -n '1,25p'",
 "description": "Addi Shir page with barid"
}
```


## [2026-09-05T13:50:44.280Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== POK bher1\"; grep -n \"Root / lemma: b\\^er-1\\|Root / lemma: b\\^er-l\" POK_full.txt | head; grep -n \"Page(s): 128\\|Page(s): 163\" POK_full.txt | head",
 "description": "Pokorny bher-1 page"
}
```


### [2026-09-05T13:50:44.493Z] TOOL RESULT

```
=== AFM leaf20
:9 `
- من 9 3 ظاهر. والاصح انْ 45 3 13
الخمر والنمذ
(البدنوز): معرات كه بوذ وهو احتبيث ܝܘ
( البربط ) العود تعريب برت واصل معناه صدر ܐܠ( لاله يشبهة ٠‏ ومنة
اليونائي ومجمةامهة
* (البربيطاء ) الثياب معرب ܨ ܢܝܐ ومعناها الصدربة وهي ثاب يلسها
اللا ناك والنساء * على صدورهم
* ( الت ) بعنى الدليل مشتق من ب تو ومعناة الضياء
(البَرَنتَ ) السئ الخلق تعريب بَرتني ومعناه الغرور والعجب <
* 3 الإبريج ) 45 بها 5 السّمن منها < ابيز
واصل ܘܚܐܘ يصب الماء و يطآق على الدلو والسطل وغير ذلك
+ 5 سفيعة كيرة 512 ان = 7 95 عن اركاء 35
بلاط اللك والمضرب 50 وحطة الرحال اوعن بركرك اي قصر عال ٠او‏ الارجح
ܣ
05225 غرض في الهواء على رأس رمح او نوه فارسيتها برجاس ومعناما
هدف السهم ܬ اصل اللفظة يونالي 90
0 ( البرجس ( نم او هو الشتدى ويأتي يض ععنى الناقفة $
بر كيس وهو الشترى واصل معناه المتلى' سُعرا
١‏ ( اليِرْخْدَاة) المرأة التارّة الناععة معربة إما عن 'برخور ند اي الممتلى' 0
5 وما :3( ` المارك او عن السر 06 ܝܡܐ ܓ®
( البرخآش ܕܡ بآش) الازاع تعريب _يرخآش .و يقال وقعوا في ÷ ܟܢ
وبرخاس
( البريد) قبل اصله متا" 80 0360 5 85 ܙܥ̈ܝܐ. - وقبل ܓ اصلة
35 وهو دابة |« ܢܐܝ ( الاب ميسن في كتاب العروق ) ܀ وهنا ܐܢܟܝ ܐ الاصل
```


### [2026-09-05T13:50:44.542Z] TOOL RESULT

```
=== POK bher1
12569:Root / lemma: b^er-1 
12758:Root / lemma: b^er-1 
13042:Page(s): 128-132 
15201:Page(s): 163-164
```


## [2026-09-05T13:50:51.356Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '12758,12790p' POK_full.txt; echo \"...\"; sed -n '15180,15205p' POK_full.txt",
 "description": "Pokorny bher-1 and bhrater"
}
```


### [2026-09-05T13:50:51.427Z] TOOL RESULT

```
Root / lemma: b^er-1 

Meaning: to bear, carry 

Grammatical information: The root b'^er-, forms the exceptional both themat. and athemat. 

present, because the durative recognizes neither Aor. nor Perf. in Indo Germanic 

Note: Beside b^er-, with them, vowel b^ere-, sees a heavy basis b^erg: b^re- 

Material: Old Indie bharat/" cames', Avestan baraiti6s. (and "ride"). Old pers. barantiy 3. PI. 

ds. (= Armenian berem, Phrygian ap-pspsr, gr. (pspu), Latin fero. Old Irish biru, alb. bie, 

Gothic baira. 

Old Church Slavic berg); Old Indie bharti{a\so as gr. cpspTS, Latin ferto\6 unthem. form), 

bibharti, bfbharti, bibhrmah, b/bbrat/ {compare that probably with nicppapsv = bibhrme 

derived sa-nicppavai "bring in, take in'), them, abibhran, bibhramana-h av\6 Avestan - 

bTbaramr, 

Perf. ba bha ra av\6 jabhara {bybn6\zaWov\ o^ babbara wltb Jabara kom harti); 

participle Old Indie bhrta-h, Avestan berate-, Supin. Old Indie bhartum, Kaus. Old 
Indie bbarayat/ = \ter. Avestan baraya-, 

Sup. Avestan ba/r/sta-'be cherishes best, cares, looks after' (= gr. cpspiGTOc; " most 
superior, best', probably ' he carries the richest, most fertile '); 

Old Indie M/Y/-/? 'carrying, sustenance, livelihood, food, wage ' = Avestan baretis 
...
Old English MN Bofa, Bdja{> engl. boy), Norwegian dial. ,6*05 'brother' etc; further Old 
High German MN Buole, Middle High German it'^o/e 'kinsman, relative, lover'. Middle Low 
German M/e 'kinsman, relative, brother' etc (see Kluge'''' under Bube, Buhle), Old 
Prussian bratnyok. brote) 'brother', Lithuanian broterelis, short form brozis, batis, brolis, 
Latvian b(r)alis ' baby brother ', bratantis ' dear brother!'; 

Old Church Slavic bratrb, bratt^ brother', short form serb. baca, acech. bat'a6s., russ. 
batja, backa 'father, priest'. 

Also alb. Geg bace^iather, leader' : serb. baca lather, priest'. 

compare noch Old Indie bhratra-m' brotherhood '; gr. cpparpa, jon. cppnipri ds.; Old 
Indie bhratrya-m: gr. cpparpia. Old Church Slavic bratrtja, bratbja6s., Latin fratria^W\ie, 
woman of brothers'. 

Tocharian A pracar{Du3\ pratri), B procer. 



References: WP. II 193, WH. I 541 f., 866, Specht KZ 62, 249, Fraenkel REtlE 2, 6 f., 
Risch Mus. Helv. 1, 118. 
Page(s): 163-164 

Root / lemma: b^red(h?)- 

Meaning: to wade, wander
```


## [2026-09-05T13:50:59.640Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources; python3 -c \"\nimport json;d=json.load(open('refs_online.json'))\nfor k in ['BQT','FSF','SNS','FFD','DRM','SYN','KLN']: print(k, d[k].get('page_offset'), '|', str(d[k].get('lookup_hint'))[:300]); print()\n\"",
 "description": "Page offsets for BQT/FSF/SNS/FFD/DRM/SYN/KLN"
}
```


### [2026-09-05T13:51:01.660Z] TOOL RESULT

```
BQT vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...'). | grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --d

FSF 484 leaves; edition/printing of this scan not identified — determine offset from printed page numbers on the page text/image when checking | grep the headword in FSF_pages.txt (alphabetical glossary); use inside.php search for leaf numbers. Also https://archive.org/details/nooshinshahnameh is a different Noushin book (گزارشی چند درباره شاهنامه).

SNS 242 leaves; page offset not determined (OCR too poor to read printed numbers) — locate by transliteration then read the page image | grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php search (see BQT) for better hit-to-leaf mapping.

FFD 115 leaves (PDF pages); printed page = PDF page − 5 (PDF 40 = p.35). 2nd printing 1385 of the same Qoqnus setting (ISBN 964-311-015-X). | Searched archive.org (Persian/Latin titles, author), ketabnak, noorlib, general web (pdf/download): nothing; only a related paid e-book 'واژگان زبان فارسی دری' (fidibo). ketabnak.com/book/45024 is a different book (فهرست فعلهای فارسی).

DRM Tome I: leaf = p + 22 (e.g. leaf 26 = p.4); Tome II (starts ~leaf 364): leaf = p + 364 (e.g. leaf 368 = p.4). Nourai does not say which tome - try both. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Tome I is the historical grammar of Persian (numbered §§); Tome II contains the 'Études sur la langue...' incl. etymological notes on Persian words. grep the Persian word in transliteration.

SYN leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the concept heading (all caps English word) or a printed page number line.

KLN KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.
```


## [2026-09-05T13:51:05.267Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== KLN pachy\"; grep -n \"^pachy-\\|^pachyderm\" KLN_1966.txt | head; echo \"=== SYN 107 leaf 131\"; awk 'BEGIN{RS=\"\\f\"} NR==132' SYN.txt | head -30",
 "description": "Klein pachy-, Buck p.107"
}
```


### [2026-09-05T13:51:08.350Z] TOOL RESULT

```
=== KLN pachy
26881:pachy-,  combining  form  meaning  ‘thick,  dense’.
26884:pachyderm,  n.,  a  thick-skinned  animal,  as  the elephant,  rhinoceros  and  hippopotamus.  —  F. pachyderme,  fr.  Gk.  rrayuSeppog,  ‘thick-skin¬ ned’,  which  iscompounded  of  wxxbi;,  ‘thick’,  and Sepp.a,  gen.  S^pjzaTog,  ‘skin’.  See  pachy-  and derma.
26885:pachydermatous,  adj.,  1)  thick-skinned;  2)  insen¬ sitive.  —  See  prec.  word  and  -ous. pachydermia,  n.,  abnormal  thickness  of  the  skin (med.)  —  Medical  L.,  fr.  Gk.  nayoSepiita, ‘thickness  of  the  skin’,  fr.  7taxbSepjxog,  ‘thick- skinned’.  See  pachyderm.
=== SYN 107 leaf 131
dding’.
Lith. (7S)tekéti uz vyro (b), lit. ‘run after a man’, similarly Lett. cet pie vira, are modeled on the Pol. and Russ. phrase, below, 6. Hence Lith. sb. igteké- jumas ‘marriage’ (woman’s).
Lett. precét, orig. ‘bargain’, deriv. of prece ‘wares’. Hence precéSands ‘mar- riage’. Miihl.-Endz. 3.384.
6. ChSI. (0)zeniti se (a), etc., general Slavic, deriv. of Zena ‘wife’ (2.32). Hence sb. SCr. Zenidba, Boh. zenitba, Russ. Zenitba ‘marriage’ (man’s).
ChSI. posagati (b), also posagit ‘wed- ding’, ORuss. posjagat’ : ChSl. segnatt
‘stretch out’ (the hand). Refers to the bride’s reaching out for the hand of the bridegroom at the wedding ceremony, Cf. Skt. pani-graha- ‘marriage’, lit. ‘grasping the hand’ (of the bride in this case). Briickner, KZ 45.318 ff. Walde- P. 2.482 ff.
SCr. udati se, Boh. vddati se (both b) : ChSl. vii-datz, etc. ‘give’, hence ‘give a woman in marriage’ and reflex. ‘be giv- en in marriage’, like ON giftask, above, 4, Hence sb. SCr. udaja, Boh. vdaj, vdavky (pl.) ‘marriage’ (woman’s).
Pol. 28é za mqz, Russ. vyiti (or vydtt) za muz (both b), lit. ‘go after a man (hus- band)’, that is, follow him. Briickner, KZ 45.319. Hence sb. Russ. zamudzestvo ‘marriage’ (woman’s).
7. Skt. vah- ‘lead, bring’ and ‘marry’ (orig. a, like Lat. dicere uxdrem, Lith. vedu, but also b already in Rigveda), vivaha- ‘marriage’, Av. vaz- (once as ‘marry’ a): Lat. vehere ‘carry’, etc. Walde-P. 1.249.
Av. upa-vad- (in caus. form) ‘give in marriage’: Skt. vadhi- ‘bride’, Lith. vedu, etc. (above, 5). Barth. 1343.
Skt. pari-ni-, lit. ‘lead (the bride) around (the fire)’, hence ‘take a wife’, fr. n7- ‘lead’.
Skt. pari-grah- ‘seize, take a wife’, fr. grah- ‘seize,’
: CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar SSS eee oe
MAN
2.34 MARRIAGE; WEDDING
Digitized by Arya Samaj Foundation Chennai and eGangotri
KIND: SEX, AGE, FAMILY RELATIONSHIP 101
} Goth. luga Lith. (apsi-)vedimas, 18tek- a Lie ON giptung, pple éjimas (b); vestu- N Hee Said ridkaup, brullaup vés
```


## [2026-09-05T13:51:14.824Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} {n++; if (index($0,\"pachyderm,  n.,  a  thick\")) print \"KLN leaf(1-based):\",n}' KLN_1966.txt; echo \"=== SYN BROTHER\"; grep -n \"2\\.4[0-9] BROTHER\\|BROTHER\" SYN.txt | head -6",
 "description": "Klein leaf; Buck BROTHER section"
}
```


### [2026-09-05T13:51:17.235Z] TOOL RESULT

```
KLN leaf(1-based): 593
=== SYN BROTHER
2908:MANKIND: SEX, AGE, FAMILY RELATIONSHIP 107 2.44 2.45 BROTHER SISTER Grk. 4ded¢ds abehon NG abeAdeds, pop. Abephés 4deAH7, POP- d5epon s Lat. frdter soror It. fratello sorella Fr. frére se@ur Sp. hermano hermana Rum. frate sora Ir. brathir siur Nir.  dearbrathatr deirbhshiur W. brawd chwaer Br. breur c’hoar Goth. brépar swistar ON brddir systir Dan. _broder sdster Sw. broder syster (0) 0) brddor sweostor ME brother sister, suster NE brother sister Du. broeder zuster OHG  bruodar swestar MHG_bruoder swester NHG _ bruder schwester Lith.  brdlis sesuo Lett. bralis masa ChSl.  bratrii, brati sestra SCr. brat sesira Boh.  brair sestra Pol. brat siostra Russ. brat sestra Skt. bhratar- svasar- Av. bratar- x’ anhar-
3455:2.65 BROTHER-IN-LAW : ; Jife’s Husband’s Brother; b, W Veter: c, Sister’s Husband; d, Husband’s Sister’s Husband; éf Husbands of Sisters) Grk. Sane (a); vauBpds (b, c), aédior (e), avdpds
```


## [2026-09-05T13:51:29.103Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for L in 566 567 568; do echo \"--- leaf $L\"; awk -v l=$L 'BEGIN{RS=\"\\f\"} NR==l' KLN_1966.txt | head -3; done",
 "description": "Klein leaves near p.1109"
}
```


### [2026-09-05T13:51:31.440Z] TOOL RESULT

```
--- leaf 566
orman-ize,  intr. and  tr.  v.,  Norman-iz-ation,  n.
Norn,  n.,  one  of  the  three  goddesses  of  fate  in Scandinavian  mythology.  —  ON.  norn  (pi. nornir),  rel.  to  Swed.  dial,  noma,  nyrna,  ‘to warn,  to  communicate  secretly',  ME.  nyrnen,  ‘to recite’,  MHG.  narren,  ‘to  growl,  snarl’.  All  these words  are  of  imitative  origin.
Norse,  adj.,  1)  Scandinavian;  2)  Norwegian.  — Obsol.  Du.  Noorsch,  ‘Scandinavian,  Norwegian’ (now  Noors,  ‘Norwegian’),  fr.  Noordsch  (now Noords),  ‘Nordic’,  fr.  Du.  noord,  ‘North’.  See next  word  and  cp.  Northman.
--- leaf 567
  Sir  Richard  Owen  (1804-92)  in  1848  fr. vcoxo.;  (also  vcotov),  ‘the  back’,  and  yopSr),  ‘a string’.  See  noto-  and  chord, notodontid,  adj.,  pertaining  to  the  Notodontidae ; n.,  any  moth  of  the  family  Notodontidae.  — See  next  word.
Notodontidae,  n.  pi.,  a  family  of  moths  ( entomol .) —  Formed  with  suff.  -idae  fr.  not-  and  the  stem of  Gk.  68cov,  gen.  686vxo<;,  ‘tooth’.  See  odonto-. Notogaea,  n.,  a  zoogeographical  realm,  com¬ prising  the  Australian,  New  Zealand  and  Neo¬ tropical  regions.  —  Gk.,  compounded  of  v6 to;, ‘the  south  wind,  the  south’,  and  y aicc,  ‘earth’. The  first  element  prop,  means  ‘the  rainy  wind’, and  is  rel.  to  votio;,  voT£p6;,  ‘damp,  moist’, voxtc,  ‘moisture,  damp’,  voxtcc,  ‘moisture, rain’ ;  see  natation  and  cp.  Notus.  For  the  second element  in  Notogaea  see  geo-, notonectid,  adj.,  pertaining  to  the  Notonectidae-, n.,  one  of  the  family  Notonectidae.  —  See  next word.
Notonectidae,  n.  pi.,  a  family  of  aquatic  insects (entomol.)  —  ModL.,  formed  with  suff.  -idae  fr. noto-  and  Gk.  vt)xt7)<;,  ‘swimmer’.  See  necto- and  cp.  words  there  referred  to. notoriety,  n.,  1)  the  quality  of  being  notorious; 2)  a  well-known  person.  —  F.  notoriete,  fr.  ML. notorietatem,  acc.  of  notorietas,  fr.  notorius, ‘well-known’.  See  next  word  and  -ity. notorious,  adj.,  well-known,  widely  known  (usu¬ ally  in  an  unfavorable  sense).  —  ML.  notorius, ‘well-known’,  fr.  L.  notus,  ‘known’.  See  know and  cp.  words  there  referred  to.  For  the  ending see  suff.  -orious.
--- leaf 568
 alpha¬ bet. —  Gk.  vu,  shortened  fr.  Heb.  nun,  name  of the  letter  n.  See  nun,  the  letter, nuance,  n.,  a  slight  difference.  —  F.,  ‘shade,  hue; a  slight  difference’,  fr.  MF.,  fr.  nuer,  ‘to  shade’, fr.  nue ,  ‘cloud’,  fr.  L.  nubes  (see  nubilous  and -ance);  so  called  with  reference  to  the  different colors  of  the  clouds.
nub,  n.,  a  knob,  lump  (rare)  —  Cp.  LG.  knubbe, ‘knob,  protuberance’,  and  see  knob,  knub. nubble,  n.,  a  small  nub.  —  Formed  fr.  nub  with dimin.  suff.  -le.
Derivative:  nubbl-y,  adj.
```


## [2026-09-05T13:51:46.800Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==748' KLN_1966.txt | head -2; echo \"=== 1971 edition pachy\"; grep -n \"^pachyderm\" KLN_1971.txt | head -2",
 "description": "Validate Klein leaf offset"
}
```


### [2026-09-05T13:51:48.895Z] TOOL RESULT

```
  ON.  skarpr, OE.  scearp ,  ‘sharp’  (see  sharp).  Cp.  Dan.  skurv, Swed.  skorv,  MDu.  scorf(t),  Du.  schurft,  OHG. scarf,  MLG.,  MHG.,  G.  schorf,  ‘scurf’.  Cp. also  scurvy,  adj.
Derivatives:  scurf-y,  adj.,  scurf -i-ness,  n. scurrile,  adj.,  scurrilous  (archaic).  —  L.  scurrilis, ‘like  a  buffoon’,  fr.  scurra,  ‘buffoon’,  an  Etrus¬ can  loan  word;  not  cogn.  with  Gk.  oxalpav,  ‘to skip,  dance,  bound’.
=== 1971 edition pachy
170849:pachyderm, n., a thick-skinned animal, as the 
170851:pachyderme, fr. Gk. 7TaxuSepp.os, ‘thick-skin-
```


## [2026-09-05T13:51:57.435Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"== BQT v1 xaviyar\"; grep -n \"خاویار\\|خاوير\\|خاويار\" BQT_v1_pages.txt BQT_v2_pages.txt 2>/dev/null | head; echo \"== BQT v1 bareh/bar\"; awk 'BEGIN{RS=\"\\f\"} {n++} /باره/ && n>440 && n<500 {print n\": \"substr($0,1,300)}' BQT_v1_pages.txt | head -5",
 "description": "Borhan-e Qate for xaviyar and bareh"
}
```


### [2026-09-05T13:52:00.583Z] TOOL RESULT

```
== BQT v1 xaviyar
== BQT v1 bareh/bar
442: اک
بار یجه‌رو م ود نگ - سخرتروز
و شب را کونند - و کنابه از دیا و روز کار هم
حست باعتبار شب و روز .3۶
با د ثر ۵ - باتحتالی‌مجمول بروژن‌کاجیر»»
```


## [2026-09-05T13:52:06.210Z] TOOL CALL #46: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:253 2>&1 | head -60",
 "description": "Fetch Borhan page 253"
}
```


### [2026-09-05T13:52:08.476Z] TOOL RESULT

```
no scan of BQT covers printed page 253 (see 'scans' in refs_online.json)
```


## [2026-09-05T13:52:15.491Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for L in 466 470 474; do echo \"--- leaf $L\"; awk -v l=$L 'BEGIN{RS=\"\\f\"} NR==l' BQT_v1_pages.txt | head -12; done",
 "description": "Inspect Borhan leaves near p.253"
}
```


### [2026-09-05T13:52:17.484Z] TOOL RESULT

```
--- leaf 466
مودن باشث .
بد ندان‌خوش هدن « کنابماز
لذت بافتن و محظوظ شدن باشد .
بو » بنتم اول و ثانی و سکون واو »
اسب تندرو را گویند .
بدواد - بر وزن پرواز » بال کشودن
طیور را گوند ‏ و یمن و قرارگاه و آرام
جای باز و شاهی و امثال آبرا نیز گفته اند ۷ .
یدو ره بروزن‌تنوره » طعلمیرا گویند
باشند - و بروزن مسخره عم کنته ابد - و باین
وزن بمعی حصه و بهره نیز آمده ات ؟ .
پلمه » بنتح اول و ثانی» خشکه پلاو را
--- leaf 470
تب ۷46 سه
نیز گوبند - و بعرمی نلم ولابتی است در عغرب
که مردم آنجا سبزچهره میباشنه ۷ .
بر پروشان ۴ با بای فارسی بروزن
پرده پوشان . مطلق امت راکوندازهر بیفمبری
که باشد .
بر لست " با سین بی تفمله بروزن‌سر مست»
بمعنی طرز و روش و قاعده و قانون باشد ۳ .
بر بستگان - بروزن‌سربتکان » جمع
بر لسته - بروزن‌برجته » تقیض‌بررسته
است و آن چیزیرا گوین که روح نبانی در وی
اثر نکند و نشو و نما تتواند کرد وژداوه از ا نسعه
--- leaf 474
۳و۷
بر دفتر افگندن - کنابه از نوشتن
باشف .
0 بر دلگ« بروزن‌مرداه . اضانه را کوبند
وبمعنی اغلوط و لغز وچبتان هم آمده است
وب
لغز و چستان گفتهاند .. ۱
بر 6۵ » بروزن‌مرهم ؛ نم اول شهربردع
بوده است پیش از زمان سکندر و سکندر آنرا
بردع نام نهاده ۱
بر ذهیك < بر وزن سر کشید ؛ مساضی
بردمیدن است که رویدن و سبز شدن با۵دیمنی
```


## [2026-09-05T13:52:25.228Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} {n++} n>=470 && n<=478 {if (match($0,/بر دن|بردن/)) print \"leaf \"n; }' BQT_v1_pages.txt; echo \"---leaf473\"; awk 'BEGIN{RS=\"\\f\"} NR==473' BQT_v1_pages.txt | head -20",
 "description": "Find bordan in Borhan"
}
```


### [2026-09-05T13:52:27.920Z] TOOL RESULT

```
leaf 473
leaf 474
leaf 475
---leaf473
برخقد سر کردن
بر خلد‌سر کرش - اجه اتیابداری
همیشگی و جاودالی‌بانتن باشک .
بر وا ب4 - باواومعدوله‌بروزن‌سردابه,
توش و نهالی باشد - و حمخوابه راهیز گوند .
بر خود ۱ + باواومسدوله بروزن‌سندر,
یی هره باشد که شربك و انازاست سومخفف
برخوردار هم هست. وبروزن‌فتفور هم بنظر آدنه
۳
بر 4 ۲ « بروزن چرخه . بمعنی پاره
و حصه و بهره و جزوی از کل باشد .
لرزحی » بروزن‌چرخی ۰ بمعنی‌فداشدن
و فربان کردیدن باشد ۴ - و آنچه در عرش
چیزی‌بکسی دهند وبمعنیحصه وبهرمواندکیاز
ببار هم صت ؟ .
لرث ‏ بفتح اول بروزن فرد » امی است
بدور شدن از راه دمتی آزراه دور شوت .- ویمعنی
و جتم اول ماضی بردن است - و چیستان و لفز
را نیز کفه اند و آلرا بعربی احجه خوانند -
و در عربی قماشی است مخصوص یمن کهپردیمانی
```


## [2026-09-05T13:52:41.172Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"== FSF خاور\"; grep -n \"خاور\" FSF_pages.txt | head -6; echo \"== FSF leaf of خاور\"; awk 'BEGIN{RS=\"\\f\"} {n++} /خاور/ {print \"leaf\",n; print substr($0,1,400); exit}' FSF_pages.txt",
 "description": "Noushin Shahnameh glossary on khavar"
}
```


### [2026-09-05T13:52:43.400Z] TOOL RESULT

```
== FSF خاور
376:‫دانشکدة خاورشناس فرهنگستان علوم شوروی (‪ ۹۴۸‬هجری) ‪-‬نسخهة خطی‬
3295:     ‫خاور را بهمعنی مغرب بکار می‌برد‪.‬‬              ‫از فخر گرگانی (ویس و رامین ‪:)۴۶-۲۸‬‬
3298: ‫اخزراسان سوی خاور می‌شتافت‬                                                         ‫بابک‬
3310:‫خورآسد پهلوی باشد‪ :‬خور آید‬                      ‫خوروران [خاوران» خاور] مغرب‪ .‬باختر‬
3329:                          ‫از حافظ (غزل ‪۲‬‬                    ‫ز بالا همی سوی خاور گذشت‬
3342:‫همی رفت ناشاد و دل پر زباد‬                                    ‫چو خور برکشیدی به خاور فرود‬
== FSF leaf of خاور
leaf 15
‫مقدمة تالف‬                           ‫‪5‬‬

‫از دست نداده‌ام‪ .‬از سویی باآنها مشورت کرده‌ام و از سوی دیگر اگر ‪-‬به گمان‬
 ‫خود ‪-‬به خطایی در انها پی برده‌ام انها را یاداور شده‌ام کهنمونه‌هایی در پیش‬

 ‫ر صحیح و معنای د
```


## [2026-09-05T13:52:43.520Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"== SNS war\"; grep -n \"aswār\\|asvār\\|\\-wār\\|parwardan\\|gōšwārag\" SNS.txt | head -10; echo \"== FFD bar\"; grep -n \"بردن\\|آوردن\\|پروردن\" incoming/FFD/FFD_pages.txt | head -10",
 "description": "SNS and FFD greps"
}
```


### [2026-09-05T13:52:43.573Z] TOOL RESULT

```
== SNS war
== FFD bar
284:درآوردند. در ایران پس از اسلام زردشتیان برخی از نوشته‌های خود را که به فارسی
305:3 ۵7 57 : بردن
318:27 بردن
330:۵ -ريشه مضاعف می‌شد و آن درآوردن هجای آغازی ريشه بوده در آغاز ریشه»
351:آغاز ريشه برای مضاعف کردن می‌آوردند. اغلب تغییراتی داده می‌شده است:
376:مادهٌ آینده از افزودن لیا لا به ريشه و آوردن 2 پس از 57و 83 ساخته می‌شده است:
383:و 4 بردن 4 برده‌شدن
400:: نماز 8 نمازبردن
402:مادهٌ آغازی از پیوستن ۶به ريشه و آوردن 2 پس از 5 ساخته می‌شده است:
430:۲ - آوردن هجای نخستین ريشه با 8 یا 21 یا 2۷ پیش از ریشه (فعل تشدیدی با
```


## [2026-09-05T13:52:51.746Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} {n++; if (index($0,\"خوروران\")) {print \"FSF leaf:\",n; print substr($0,1,1200)}}' FSF_pages.txt | head -40",
 "description": "FSF khavar page"
}
```


### [2026-09-05T13:52:53.861Z] TOOL RESULT

```
FSF leaf: 74
                                          ‫‪۷.‬‬                                         ‫بابزن‬


 ‫([شمال ]»‪( .‬مارکوارت‪ .‬ایرانشهر‬   ‫‪۲‬‬            ‫(باب در این بیت پدر گیو است و گیو پدر‬
                        ‫‪(AF FV‬‬     ‫‏‪۷‬‬                                       ‫بیژن است)‬
     ‫در تاریخ سیستان نیز چنین آمده است‪:‬‬                                             ‫‪ .‬بایزن‬
‫«هر چه حد شمالست باختر گویند و هر‬                                           ‫سیخ کباب‪:‬‬

 ‫چه حد جنوبست نیمروز گویند و میانه‬                       ‫بسزد نیزه بر بند درع و زره‬
 ‫اندر بدو قسمت شود هر چه حد‬                     ‫زره را ن‌ماند ايچ بند وگره‬
 ‫مشرقست خراسان گویند هور چه حد‬                            ‫ز زینش جداکرد و برداشتش‬
                     ‫مغربست ایرانشهر»‬            ‫گراشتش‬
   
FSF leaf: 469
‫هفت کشور‬                                    ‫‪۳۹۵‬‬

  ‫کشور‬
     ‫«وئوروبرشت» ‪ ۳5۲۵۵۵۷۲۷۵۷‬و‬                    ‫‪-۳ ۵۷25‬‬      ‫‪۲‬سوهی‬
                                                                   ‫‪- ۱‬ارزهی ‪- 19۵26۲۸‬‬
‫«وئورو جرش ‪ 4157۵7۷۵۷‬است و آن که‬                   ‫‪-۴‬وید ذفشو‬     ‫فرد ذفشو ‪56۵0۵۵۵۳‬‬
  ‫در میان آنهاست «خونیرس» خواننده‬                  ‫و بسرشتی‬     ‫‪-‬وشور‬
                                                                    ‫‪۵ ۵/2۱0۵2۱۷‬‬
 ‫(ترجمة پورداوده ویسپرد ‪ )۲۱۱‬همچنین‬                ‫‪-۶ ۵۵۲2۵-۵۲۵۵۷‬ونور وجسرشتی‬

‫در نامه‌های دیگر به زبان پهلوی‪ ,‬از‬                 ‫‏‪-۷ Vêuru-Jareshti‬خو نیرت ‪2102۲10۵۷62‬‬

‫آنجمله خسرو و ویدک [ص ‪۱‬ب‪۱‬ند ‪ ]۳‬به‬                                          ‫(ویسپرد ‪)۰۱۱‬�
```


## [2026-09-05T13:53:02.557Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'NR<=3310{n+=gsub(/\\f/,\"\")} END{print \"formfeeds before line 3310:\",n}' FSF_pages.txt; sed -n '3285,3320p' FSF_pages.txt",
 "description": "FSF khavar leaf and text"
}
```


### [2026-09-05T13:53:04.806Z] TOOL RESULT

```
formfeeds before line 3310: 73
 ‫چه حد جنوبست نیمروز گویند و میانه‬                       ‫بسزد نیزه بر بند درع و زره‬
 ‫اندر بدو قسمت شود هر چه حد‬                     ‫زره را ن‌ماند ايچ بند وگره‬
 ‫مشرقست خراسان گویند هور چه حد‬                            ‫ز زینش جداکرد و برداشتش‬
                     ‫مغربست ایرانشهر»‬            ‫گراشتش‬
                                                      ‫چو بر بابزن مرغ» ب‬
 ‫سخنوران پیشین گاه باختر را به معنی‬            ‫‏)‪(VAT-114-1‬‬
  ‫ور رابه‌معنی مغرب آورده‌اند‪:‬‬ ‫او‬‫خرق‬
                                   ‫مش‬                  ‫از اسدی ( گرشاسب‌نامه ‪:)۷۱۲-۷۱‬‬
 ‫رودکی خراسان را به معنی مشرق‬                                 ‫بر آن آهنی نیزة یل فکنن‬
‫[چنانکه در زبان پهلوی نیز چنین است] و‬           ‫زد آگنور چون مرغ بر بابزن‬
     ‫خاور را بهمعنی مغرب بکار می‌برد‪.‬‬              ‫از فخر گرگانی (ویس و رامین ‪:)۴۶-۲۸‬‬
                 ‫(نفیسی بیت ‪:)۹۲۸-۰۲۸‬‬                       ‫سنان نیزهگفتی بابزن بود‬
      ‫مهر دیدم بامدادان چون بتافت‬              ‫بروبر مرغگرد تیغزن بود‬
 ‫اخزراسان سوی خاور می‌شتافت‬                                                         ‫بابک‬
      ‫نیم روزان بر سر ما برگذشت‬                ‫مرکب از باب [‪:‬پدر] ‪+‬ک [‪:‬نشانه تصغیر ]‪:‬‬
‫چون به حاور شد زمانادید گشت‬                                                      ‫پدرک‪:‬‬

 ‫تک ن رای نها خراسان‬                                          ‫بپرسید ازو راه فرزند خرد‬
         ‫معنیمی‌کند (ویس ‪:)۵ ۱۷۱-۱‬‬              ‫سوی بابکش راه بنمود گرد‬
 ‫خوشاجایاسرو بوم خراسان‬                         ‫(دقیقی ‪)۶-۱۱-۷۶۶‬‬
 ‫راهی‌خور آسان‬ ‫درو باش و جهام‬                                                  ‫اوور‬
                                                                                  ‫خختر‬
                                                                                     ‫با‬
 ‫زب ان پسهلوی هرکو شناسد‬                        ‫نام‌های جهات چهارگانه به زبان پهلوی‬
‫خراسان‌ ان شوه کز وی خور آسد‬                    ‫چنین است‪ :‬خوراسان [خراسان] مشرق‬
‫خورآسد پهلوی باشد‪ :‬خور آید‬                      ‫خوروران [خاوران» خاور] مغرب‪ .‬باختر‬
 ‫رس را خور زو برآید‬   ‫او‬ ‫پاق‬‫عر‬                                    ‫شمال و نیمروز جنوب‪.‬‬
    ‫ان‬    ‫ینی‬
            ‫آد مع‬
                ‫رابو‬
                   ‫وان ر‬
                       ‫ر اس‬
                          ‫خ‬ ‫خو‬                 ‫«خربران» پهلوی‪[ ۲۵۲۵۵۲۵۳ :‬مغرب ]؛‬

 ‫کجااز وی ور آید سوی ایسران‬                    ‫نیمروز‪ .‬پهلوی‪[ ۶۵:۳۵۷۱ :‬جنوب |‬
‫چه خوش نامست و چه خوش آب و خاکست‬                ‫خراسان پهلوی‪« .‬ةئةاه× [مشرق]‬
```


## [2026-09-05T13:53:21.568Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for LN in 305 318 383; do echo \"--- line $LN\"; awk -v t=$LN 'NR<=t{n+=gsub(/\\f/,\"\")} END{print \"leaf(1-based):\",n+1}' incoming/FFD/FFD_pages.txt; sed -n \"$((LN-4)),$((LN+4))p\" incoming/FFD/FFD_pages.txt; done",
 "description": "FFD bordan/avardan leaves"
}
```


### [2026-09-05T13:53:23.995Z] TOOL RESULT

```
--- line 305
leaf(1-based): 15
افزوده صورتی از واژه بوده» که در آن 2 وجود داشته و صورت بالانده صورتی از واژه
بوده» که در آن 5 به جای 2 می‌آمده است. اگر در صورت افزودة واژه یا 18 وجود
۱ داشته» حذف آن دو سیب ضعیف شدن واژه می‌شده است:
صورت ضعیف صورت افزوده صورت بالانده
3 ۵7 57 : بردن
120 1 40 : بستن
822 3رد نحرکت کردن
در ایرانی باستان اسم و صفت و ضمیر صرف می‌شده‌اند. اسم و صفت و ضمیر
هشت حالت: فاعلی, مفعولی» مفعولی‌له. مفعولی‌عنه» مفعولی معهء مفعولی فیه. اضافی
--- line 318
leaf(1-based): 15
آلف -مادةٌ مضارع
مادةٌ مضارع به راههای زیر ساخته می‌شده است:
۱-به ريشه 2 افزوده می‌شده است:
ریشه ماده ۹
27 بردن
-به ريشه 18 افزوده می‌شده است:
ريشه ماده
03 8 پاییدن
[pdf page 16]
--- line 383
leaf(1-based): 18
ه-مادةٌ مجهول
مادهٌ مجهول از پیوستن 2به صورت ضعیف ريشه ساخته می‌شده است. در ماده
مجهول 72 و در مادهٌ مضارع که با 2 ساخته می‌شده است» ريشه تکیه داشته است:
ريشه مادهٌ مضارع مادة مجهول
و 4 بردن 4 برده‌شدن
و -مادةٌ واداری
مادةٌ واداری از پیوستن 278 به صورت بالاندةٌ ريشه ساخته می‌شده است:
[pdf page 19]
ک ‏ ای فعلهای فارسی دری
```


## [2026-09-05T13:53:28.187Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for P in 33 47; do echo \"=== pdf page $P (printed $((P-5)))\"; awk -v p=$P 'BEGIN{RS=\"\\f\"} NR==p' incoming/FFD/FFD_pages.txt | head -30; done",
 "description": "FFD printed pages 28 and 42"
}
```


### [2026-09-05T13:53:30.457Z] TOOL RESULT

```
=== pdf page 33 (printed 28)
[pdf page 33]
فعلهای فارسی دری
است.

آموز < فارسی میانه 38162 < ایرانی باستان 2 + 3-۵06*. برای 2 آرای. در
6 به جای 1 آمده است.

َ در فارسی میانه مانوی 178۳۱671 به جای 30071 و 127302 به جای 3782 آمده
است. از ريشهٌ 13201 با پیشوند 1278.
امیختن

آمیخت < فارسی میانه 270884 < ایرانی باستان 3-080۳12*. برای 3 و 18->
آراست. *8 در اصل 818 است» 8 پیش از ۲ به #بدل شده است. ريشهٌ 118 به معنی
«آمیختن» است.

آمیز + فارسی میانه 37082 < ایرانی باستان ۵-[3-0۵1*. برای 2 -> آرای. [ در [0۵
به‌جای 8 آمده است.

آوردن

آورد + فارسی میانه 2۳070 < ایرانی باستان 3-07-12*. برای و1۵ - آراست. 3
صورت ضعیف ريشةٌ 087 به معنی «حمل کردن» است و با پیشوند فعلی 2: «حمل کردن
به سوی متکلم» -> بردن. :

آو ر < فارسی میانه 20۵7 < ایرانی باستان 3-087-۵*. برای 2 > آرای.

1 هختن, آ هیختر

آهمخت + فارسی میانه 30804 < فارسی باستان 2-00۳1۵*. + ایرانی بباستان
2 برای 3و 13 > آراست. 8 صورت اصلی 9۵5 است. #۴ پیش از به «بدل شده
=== pdf page 47 (printed 42)
[pdf page 47]
فعلهای فارسی دری
ایستادن.
مادة ماضی 027191 در فارسی میانه 02719136 آمده است» از ۳27-513-1* ایرانی
باستان. برای 1۸ > آراست. «پرستید» در فارسی جعلی است و از مادهٌ مضارع و «ید»
: ساخته شده است.
پرسیدن
پرسید < فارسی میانه 00781#. 005810 مادهٌ ماضی جعلی است. از مادهٌ مضارع
ساخته شده است.
پرس < فارسی میانه 0078 < ایرانی: باستان 0788* ج ۴۹7-2 برای 2 -> آرای. 5
برای ساختن مادهٌ آغازی از ريشه به کار می‌رفته است.078 ريشه است, به معنی «پرسیدن».
پروردن
پرورد ج فارسی میانه 40 << ایرانی باستان 02۳-۵-[۳۵7*. برای 13 -> آراست.
1 پیشوند فعلی است. ريشهٌ 7 به معنی «حمل کردن» است. «آوردن» و «بردن» هم از
ريشهٌ ۳27 آمده‌اند.
پرور < فارسی میانه 0278۷27 < ایرانی باستان 271-027-8م۴. برای 8 > آرای.
پرهیختن
پرهیز < فار سی میانه 020762 < ایرانی باستان 812-28د027۵*, 271۳۵212-8 *. برای
2 آرای, علقبه معتی «پاییدن» است و با پیشوند فعلی 2272 به معنی «دوری گزیدن» و
با پیشوند فعلی 8351 به معنی «خدمت کردن» است. 020782 جانشین 278787 و
027172 شده است.
پرهیخت < فارسی میانه 0287871 در فارسی میانهٌ مانوي 0287181 به عنوان ماضی
برای 2 * 02713812 به کار رفته است. 027871 به قیاس با 782 و 7381و مانندهایش
به وجود آمده است.
```


## [2026-09-05T13:53:41.423Z] TOOL CALL #55: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A8%D8%A7%D8%B2%D9%88",
 "prompt": "Etymology of Persian بازو (bāzu) 'arm': Middle Persian, Old Iranian, Avestan and PIE forms. Also list any related Persian words mentioned (e.g. باز as a measure of length)."
}
```


## [2026-09-05T13:53:42.336Z] TOOL CALL #56: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B3%D9%88%D8%A7%D8%B1",
 "prompt": "Etymology of Persian سوار (savār) 'rider': give the Middle Persian, Old Persian/Avestan forms and the elements it is composed of."
}
```


### [2026-09-05T13:53:47.974Z] TOOL RESULT

```
# Etymology of Persian بازو (bāzu) 'arm'

## Historical Lineage

According to the Wiktionary entry, Persian بازو descends from "Old Persian 𐎲𐎠𐏀𐎢 (bāzu), from Proto-Indo-Iranian *bʰaHȷ́ʰúš, from Proto-Indo-European *bʰeh₂ǵʰús."

## Related Forms

The page identifies several cognates across ancient and modern languages:
- **Avestan**: 𐬠𐬁𐬰𐬬𐬋 (bāzvō)
- **Khotanese**: bāysū
- **Sanskrit**: बाहु (bāhu)
- **Ancient Greek**: πῆχυς (pêkhus, "forearm")
- **Old Armenian**: բազուկ (bazuk)

## Related Persian Words

The entry lists an "Alternative form": باهو (bâhu), suggesting historical variant spellings within Persian itself.

## Descendants

Persian بازو has entered numerous languages, including Hindi, Urdu, Bengali, Turkish, and Malay, demonstrating its historical linguistic influence across South and Central Asia.
```


### [2026-09-05T13:53:49.993Z] TOOL RESULT

```
# Etymology of Persian سوار (savār)

Based on the Wiktionary entry, here's the etymological breakdown:

**Middle Persian form:** ʾswbʾl / ʾsp̄wʾl (aswār), meaning "horseman, rider"

**Old Persian form:** 𐎠𐎿𐎲𐎠𐎼 (a-s-b-a-r /asabāra-/), also meaning "horseman"

**Composition:** The word traces back through Proto-Iranian *Hacwabāráh and ultimately to Proto-Indo-Iranian *Haćwabʰāras. The entry notes the connection to "horse" (asb-) combined with an agent suffix forming the occupational term for one who rides.

The Persian term descended from these ancient Indo-European roots that specifically denoted a person engaged in horsemanship, with the morphological structure combining the base for "horse" with elements indicating an agent or practitioner of that activity.
```


## [2026-09-05T13:53:59.228Z] TOOL CALL #57: Bash

```json
{
 "command": "ls site/pages/88.jpg 2>/dev/null; pdftoppm -f 88 -l 88 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg88 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/",
 "description": "Render PDF page 88"
}
```


## [2026-09-05T13:54:01.063Z] TOOL CALL #58: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A8%D8%A7%D8%B2",
 "prompt": "List ALL the etymology sections for Persian باز (bāz). In particular, is there an entry meaning 'fathom / span of outstretched arms / a measure of length'? What origin is given for it?"
}
```


### [2026-09-05T13:54:02.087Z] TOOL RESULT

```
site/pages/88.jpg
total 29888
drwx------ 2 sfmqrb sfmqrb     4096 Sep  5 09:54 .
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
-rw-rw-r-- 1 sfmqrb sfmqrb 18949704 Sep  5 02:30 mw1872.htm
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
-rw-rw-r-- 1 sfmqrb sfmqrb    98452 Sep  5 09:54 pg88.png
-rw-rw-r-- 1 sfmqrb sfmqrb   171528 Sep  5 02:45 pg89_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4628 Sep  5 02:45 pg89_ambor.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4924 Sep  5 02:45 pg89_berijan.png
-rw-rw-r-- 1 sfmqrb sfmqrb    80984 Sep  5 09:49 pg89.png
-rw-rw-r-- 1 sfmqrb sfmqrb    77182 Sep  5 09:48 pg90.png
```


### [2026-09-05T13:54:08.145Z] TOOL RESULT

```
# Persian باز (bāz) - Etymology Sections

The Wiktionary entry lists **four etymology sections** for Persian باز:

1. **Etymology 1** - Adjective meaning "open" (possibly related to Etymology 2, but relationship uncertain)

2. **Etymology 2** - Adverb meaning "again/re-" (inherited from Middle Persian, ultimately from Proto-Iranian and Proto-Indo-European roots meaning "back/away")

3. **Etymology 3** - Noun meaning "hawk/falcon" (inherited from Middle Persian, related to Sanskrit भास meaning "bird of prey")

4. **Etymology 4** - Adjective and verb forms derived from باختن (bāxtan, "to lose/play")

## Answer to Your Question

**No**, there is no entry in this Wiktionary page for باز meaning "fathom" or "span of outstretched arms" as a unit of length measurement. The documented meanings are limited to: open (adjective), again (adverb), hawk/falcon (noun), and participial forms related to the verb "to lose."
```


## [2026-09-05T13:54:12.408Z] TOOL CALL #59: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg88.png"
}
```


### [2026-09-05T13:54:12.885Z] TOOL RESULT

```

```


## [2026-09-05T13:54:12.882Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-05T13:54:28.904Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && pdftoppm -f 88 -l 88 -r 400 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf pg88_400 && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg88_400.png'); print(im.size)\n# left spine region: x 600-1300, y 1350-2900 at 400dpi\nim.crop((600,1350,1400,2900)).save('pg88_spine.png')\n\"",
 "description": "Crop left arrow spine"
}
```


### [2026-09-05T13:54:32.256Z] TOOL RESULT

```
(3400, 4400)
```


## [2026-09-05T13:54:34.537Z] TOOL CALL #61: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg88_spine.png"
}
```


### [2026-09-05T13:54:34.564Z] TOOL RESULT

```

```


## [2026-09-05T13:54:49.301Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg88_400.png')\nim.crop((600,380,1500,1180)).save('pg88_e0spine.png')\n\"",
 "description": "Crop entry 0 spine"
}
```


### [2026-09-05T13:54:51.961Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-05T13:54:54.297Z] TOOL CALL #63: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg88_e0spine.png"
}
```


### [2026-09-05T13:54:54.328Z] TOOL RESULT

```

```


## [2026-09-05T13:55:11.661Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg88_400.png')\nim.crop((680,1550,1000,2000)).resize((640,900)).save('pg88_join.png')\n\"",
 "description": "Zoom spine origin"
}
```


### [2026-09-05T13:55:14.137Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-05T13:55:16.368Z] TOOL CALL #65: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg88_join.png"
}
```


### [2026-09-05T13:55:16.382Z] TOOL RESULT

```

```


## [2026-09-05T13:55:28.063Z] TOOL CALL #66: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%A8%D8%A7%D8%B2/",
 "prompt": "In the فرهنگ معین (Moin) section, list the senses given for باز. Is there a sense «فاصلهٔ میان دو دست گشوده» / a unit of length (like fathom/باژ/بازه)? Quote it and any bracketed origin tag."
}
```


### [2026-09-05T13:55:32.836Z] TOOL RESULT

```
# Senses of باز in Farhang-e Moein

Yes, the فرهنگ معین section includes a sense for a unit of length:

**Quote:** "واحد اندازه گیری طول برابر با امتداد دو دست درحالی که دست ها به صورت افقی از هم بازشده"

**Translation:** A measurement unit for length equal to the span of two hands extended horizontally apart.

There is no bracketed origin tag provided for this particular sense in the Moein dictionary entry shown above.
```


## [2026-09-05T13:55:50.197Z] TOOL CALL #67: Bash

```json
{
 "command": "for u in \"https://www.etymonline.com/word/caviar|page 88, Bher 1 node 3: caviar/xâvîyâr etymology (khaya 'egg' + dar 'bearing')\" \\\n\"https://en.wiktionary.org/wiki/%D8%AE%D8%A7%D9%88%DB%8C%D8%A7%D8%B1|page 88, Bher 1 node 3: Wiktionary etymology of Persian خاویار (Szemerenyi: kaef+jaro)\" \\\n\"https://en.wiktionary.org/wiki/%D8%A8%D8%B1%D9%8A%D8%AF|page 88, Bher 1 node 3: Arabic barid < Latin veredus, refutation of Persian burdan origin\" \\\n\"https://en.wiktionary.org/wiki/%D8%A8%D8%A7%D8%B2%D9%88|page 88, Bhengh node 2: Persian bazu 'arm' < PIE *bheh2ghus (separate root from bhengh-)\" \\\n\"https://en.wiktionary.org/wiki/%D8%B3%D9%88%D8%A7%D8%B1|page 88, Bher 1 node 5: Persian savar < OP asabara-\" \\\n\"https://en.wiktionary.org/wiki/%D8%A8%D8%A7%D8%B2|page 88, Bhengh node 2: Persian baz has no 'fathom' etymology on Wiktionary\" \\\n\"https://abadis.ir/fatofa/%D8%A8%D8%A7%D8%B2/|page 88, Bhengh node 2: Mo'in's baz = length unit of two outstretched arms (MON:452)\"; do\nurl=\"${u%%|*}\"; note=\"${u##*|}\"; python3 tools/fetch_source.py \"$url\" --note \"$note\" 2>&1 | tail -2; done",
 "description": "Archive web sources"
}
```


### [2026-09-05T13:55:53.634Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/29f4f9f1a161789d.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/9c0ea7b5784dd78d.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/15cfd831ad676ea7.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/7321751ed099d444.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/497d45dd26538c8b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/2347a7eacc81d31c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c2c11b87300594fb.txt
```


## [2026-09-05T13:55:59.654Z] TOOL CALL #68: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg88.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/88.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/ | head; sed -n '1,120p' /home/sfmqrb/git/rishe/tools/verify_check.py",
 "description": "Copy page PNG and read verify_check"
}
```


### [2026-09-05T13:55:59.718Z] TOOL RESULT

```
total 1992
drwxrwxr-x 2 sfmqrb sfmqrb   4096 Sep  5 09:55 .
drwxrwxr-x 9 sfmqrb sfmqrb   4096 Sep  5 01:38 ..
-rw-rw-r-- 1 sfmqrb sfmqrb 104864 Sep  4 19:03 101.png
-rw-rw-r-- 1 sfmqrb sfmqrb  86203 Sep  4 19:03 126.png
-rw-rw-r-- 1 sfmqrb sfmqrb 105296 Sep  4 19:03 311.png
-rw-rw-r-- 1 sfmqrb sfmqrb  96466 Sep  4 19:03 33.png
-rw-rw-r-- 1 sfmqrb sfmqrb  99093 Sep  4 19:03 39.png
-rw-rw-r-- 1 sfmqrb sfmqrb  54479 Sep  4 19:03 46.png
-rw-rw-r-- 1 sfmqrb sfmqrb  99295 Sep  4 19:03 54.png
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


## [2026-09-05T13:56:06.627Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD; ls; echo \"=== Bd2 leaf for p151\"; awk 'BEGIN{RS=\"\\f\"} {n++} /bhengh|bheng\\^h|bhngh/ {print \"leaf\",n,\":\",substr($0,1,300)}' WLD_Bd2_pages.txt | head -5",
 "description": "Walde-Pokorny Bd II bhengh"
}
```


### [2026-09-05T13:56:08.790Z] TOOL RESULT

```
WLD_Bd1_1930_dli_70244_djvu.txt
WLD_Bd1_1930_dli_70244_text.pdf
WLD_Bd1_pages.txt
WLD_Bd2_1927_dli_106624_djvu.txt
WLD_Bd2_1927_dli_106624_text.pdf
WLD_Bd2_pages.txt
=== Bd2 leaf for p151
leaf 79 : 74                                    poi-, pi



   lAi, papijusi 'kdrve „Kuh, die beim Melken die Milch nicht zuruckhalt“,
```


## [2026-09-05T13:56:14.101Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD; echo \"=== leaf 156\"; awk 'BEGIN{RS=\"\\f\"} NR==156' WLD_Bd2_pages.txt | head -22; echo; echo \"=== leaf 198\"; awk 'BEGIN{RS=\"\\f\"} NR==198' WLD_Bd2_pages.txt | head -20",
 "description": "Walde-Pokorny II pp.151, 193"
}
```


### [2026-09-05T13:56:16.114Z] TOOL RESULT

```
=== leaf 156
                                                                    ;                                                  ;




                                                bLongh-j bhngb            bhend-                                 151


    Granz fragwurdig eriunert Weigand-Hirt u. Bengel an                                       lit,   biize   „Keule,
Kloppel am Dreschfleger^                         (nasallos, Palatal!).


bhengh-, bhngh- (Adj. blw^ghiUs) ,,dick, dicht, feist'^
  Ai. baliiU „diclit reichlicli, vier* (Komp. Sup. bijilyas-^ bfjiistha-'^ == gr.
nayvg ) bahidci- „dick, dicht, ausgedehnt, groB, reichlich, viel“ (= gr. na-
            ;


%vXcbg Adv. bei Aristot.,                       wenn dies nicht jiingere Bildung); bqliate (unbe-
legt) ,,mehrt sich“, buhagate „befestigt, starkt'^,                                badhd-   „fest, stark‘‘;
    av.     bazali- n.            „Hohe,    Tiefe'‘,      bq^nu- m.       ds.,   bal. baz „Yiel“, haz „dicht“;
    sehr zw. arm. baztim                        „Yiel'‘   (da aus bJingh-           yielmehr      banjiun zu er-

=== leaf 198
                                              ;




                                                        bhrag-   — bhrator-                                     193

 bhrag- „krachen'‘; Gleichheit mit bhreg „brechen“ (Schallvorstellung beim
     Brechen; vgl. Osthoff MU. Y 100, Persson Beitr. 330 A. 1) ist be-'
          senders          wegen des schwerlich                      analogisch   {egi : fregi:   — amb-ages    :
                                                                                                                    's)

          erklarbaren a von lat. suffragium unannehmbar, zudem gibt es in
          der Schallbed. keine Worte mit e- oder eindeutigem o-Yokalismus.
          Hochstens ist bhreg- „brecben^‘, wenn einst aus einer Schallvorstellung
          entsprungen, eine Parallelbildung neben bhrUg-,                               Ygl. noch die Schall-
          sippen bher-^ bherg- „bruinmen“.
       Lat. fragor „Krachen, Getose“ (nicht nach Kretschmer                                   KZ. 31, 405 mit
               zu ocpagayEOfiai, Wz. ^^spheng-)', suffragium „Abstimmung,
fr- aus s['ph]r-
```


## [2026-09-05T13:56:25.514Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD; for L in 158 159; do echo \"=== leaf $L\"; awk -v l=$L 'BEGIN{RS=\"\\f\"} NR==l' WLD_Bd2_pages.txt | head -14; done; echo \"=== leaf198 more\"; awk 'BEGIN{RS=\"\\f\"} NR==198' WLD_Bd2_pages.txt | sed -n '20,40p'",
 "description": "Walde-Pokorny bher- and bhrater-"
}
```


### [2026-09-05T13:56:27.850Z] TOOL RESULT

```
=== leaf 158
                                                        bher                                            153

 1.    l)her „tragen, bringeii“ usw. (auch Leibesfrucht tragen; med. „ferri“),
         auch „aufheben, erbeben“ (Persson Beitr. 607 f. Anm. 2). Neben bher-^^
      mit tbem. Vokal bhere-, stebt eine set-Basis bhere-, s. Bgm, IF. 12, 153 f.
      Anm., Scbwyzer IF. 23, 309 und bes. Persson Beitr. 642, 687, 693 (auch
      gegen Reicbelt’s KZ. 39, 20, 35 Ansatz ^bherei-; ein "^bherd wird weder
      durch aksl. bhvati erwiesen, nocb durcb "^bhrater- „Bruder‘‘, dessen
      WzYerwandtschaft unerwiesen ist).
   Ai. bhdrati „tragt‘‘, av, baraiti ds. (und „reiten‘^, s. zuletzt Cbarpentier
IP. 29, 377 a 4), ap. barantiy 3. pi ds. (= arm. b^rem, pbryg. a^-fisgery gr.
(pegcoy lat. fero, air. biru, alb. bie^ got. baira, aksL ber(^\ ai. bharti (ebenso
wie gr. cpegzE, lat. fert kaum alte unthem. Form, s. Sommer Hdb.^ 542 f.,
Kr. Erl. 159f.; gegen Yendryes IF. 26, 135; aucb ein av. Praes. "^barti gibt
=== leaf 159
         ;                                                                                                                              ;




154                                                           bher


bardtar- „ein Unterpriester“ (vgl.                           lat.   fertor-ms, umbr. arsfertur),                               fern   ai.
bhartrt^           av. baro'^ri „Tragerin,        Mutter^; dehnstufig (wie bha-
                                                     Erhalterin,
rdyaii, s. o.) ai. bhard-h ^Biindel, Arbeit, Last'', bharin- „tragend‘‘, bhdrman-
(n.) „das Bringen, Aufwartung", bharya-h „zu tragen, zu ernahren" (= ahd.

=== leaf198 more
fr- aus s['ph]r-
Urteil, Zustimmung, BeifalU (eig. „das Dabeilosbrechen des Larma der
beistimmenden Meoge^)
       air.     hraigim „pedo“, schott.-gal, hraim^ cymr.                         corn, bram^        bret.   bramm
 „Furz‘^ (weitere               Anreihungen bei Pick II ^ 183,                    s.   auch die Lit. bei Ost-
hoff ZfceltPh. 6, 396).
   Aisl. bralc n. „Gekrach, Larm“, braha „larmen'‘, mnd. brah m. auch

„ Gekrach,  Laim“, mhd. brack m. ^Gekrach, Larm‘‘, ahd. mhd. as. braht
„Larm, Geschrei^* (mhd. brehtcn „rufen, schreien, larmen‘‘, breht „Wort-
wechseU), ags. breahim m. ds., as. brahtum m. „Larm^ larmende Menge“;
   lit,        braszhcti       „prasseln,              krachen‘‘     (^bhrag-sqo\      Trautmann       brieflich),
wohl auch,               trotz etwas andern Bedeutungsfarbung, lett. brdst
                                    der    z.     T.
„brausen, toben, larmen“, brdzet „sturmen, brausen, tosen“ (Pick I^ 495).
Ygl. die Lit. u. bhreg- „brechen^‘.



bhrator- (auch bhrdter- nach poter-^ mater-^ dhvg(h)dter-) j.Bruder^.
       Ai.      bhrcdar-,       av.     ap.       braiar-      „Bruder“;      arm. dbair,     gen.    elbaiir   ds.
```


## [2026-09-05T13:56:37.653Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"== IEC bhengh\"; grep -n \"bhṇghus\\|bhenghos\\|bhengh\" IEC.txt | head -5; echo \"== IEC bhero\"; grep -n \"^bherō\\|bherō \\|bhero \" IEC.txt | head -5; echo \"== SKT pachyderm\"; grep -n -i \"pachyderm\" SKT.txt | head -3; echo \"== NYB burtan\"; grep -n \"burtan\\|bwltn\" NYB_vol2_glossary.txt | head -5; echo \"== HUB xavar/barid\"; grep -n -i \"khāwar\\|xāvar\\|barīd\\|gāhwāra\" HUB.txt | head -5",
 "description": "Mann, Skeat, Nyberg, Hübschmann greps"
}
```


### [2026-09-05T13:56:37.745Z] TOOL RESULT

```
== IEC bhengh
== IEC bhero
1261:bhertos *born, carried; burden'. Cf. bhero Skt. cf. bhártum, inf.; Gk. phertós ‘bearable’; Lat. fertus; MIr. bert, Ir. beart ‘burden’; OBr. cf. aperth (for *at-berth “sacrifice'): W ad- ferth ‘comfort’; OHG bérd ‘progeny’: OE cf. beorbor, n. -es- st. ���childbirth; newborn child"
1262:bherulà (bherlà) ‘stick, staff. Cf. bhero Lat. ferula; Cz. berla ‘crutch’. (A semantic link with bherió is also possible)
1527:bhorm- (bhormos, à, is, io) “burden; bearer, holder, container’. Cf. bhero Gk. phormós "basket, corn-measure'; Alb. barrë “load; Go. barms (i-st.); OHG OS barm ‘Jap’; OE bearm ‘lap; possession’; G (uml.) Berme (‘ramp of bulwark’. LW in Fr. berme, OFr. barme); ON cf. barmtog “haul-rope. (Isophonic forms, of uncertain kinship, are the following: Gk. phormís ‘faggot; Alb. barmë “inner bark’; Ger. Barm, Barmen ‘crowd, pack’; Barmen, Bärme ‘barm, yeast’; ON barmr ‘brim’; barmi ‘brother’; Ukr. brama sic ‘gate’). WP II, 164
1529:bhorn- (2) ‘son, fellow’. Cf. bhero Per. (ambig.) barna 'lad'; OHG ON barn, OE bearn ‘child’; Li. cf. (e-gde) bérnas ‘youth’; Latv. berns “child?
1536:bhorus, uos, uis (1) ‘smal! domestic animal". Cf. bhero Lydian bórus, gs -uos (an unknown animal. Hes.); Alb. cf. berr ‘small domestic animal’; OCS bravi, id.; Cz. brav “sheep? or ‘goat; Slovak ‘pig’ or ‘boar’; Srb. “tan” or 'castrat- ed boar’
== SKT pachyderm
== NYB burtan
445:motion: šutan, dväristan, opastan, ete., and with ēstātan and nisastan (also ~ 6). — 2. prep. in, local, temporal and figura- tive: ~ Pārs; ~ im xünak P1:6; ~ miyàn i in the middle of 865; ~ han hangam at the time 613; ~ ham zamān at the same time 127°; ~ zamān in due time 221, etc.; ~ sap in the night 529, 614; ~ hàsr for a single moment 663; ~ hàn in the meantime 5615-17; — xtatäyeh + Xösrör 1184; ~ Vistasp šāh kisvarikan when V. was the emperor of the world 365; — freftür ~ : concerning 3419-20, 10923; spasdārēh ~ , an-ispās ~ : to, against; with other substantives, v. these separately ; — together with another prep.: ~ 6 into, on to, up to: ~ 6 nun 404; with apakandan, burtan, guméxtan (also without 6), hištan, kartan (v.s.v. kar); apar ~ 402, — Av. (131 sq.) antara, antarš, OP antar (better read antara^); MPrthPrs ’ndr; Paz. NP andar; v. also niyandar.
505:lapar [’pl; MDM, v. 2apar] adj. situated above, lying above: évak ~, apäk dit, v.s.v. žapāk (2); — heavenly, often in compounds: apar-apükeh etc., v. below; comp. ~-tar [’pltl] higher 5426, 581°, highest 1097; sup. ~-tom highest 415. 102°; v. also apartaréh; — adv. empha- sizing an adj.: highly, extremely: apar- aržānīk, v. aržānīk. — Av. (393) upara-, adv. upara (instr.), uparam; MPrth ’br adj. and adv. (MHC), comp. ’brdr, sup. ’brdwm; Ps. ?pldl; Paz. awartar, awardar (SGV); NP bar ‘height, top, summit’, bartar ‘higher’. ?apar [MDM, erroneous reading of OAram QDM] 1. adv. above: (3 päs) i-m guft ~ of which I spoke above 65°; či nümak" cé hac ~ nipišt" éstat the inscription that had been written here above P2:3, cf hacapar; — prev. over, on, upon, up, or simply expressing the initiation of the action, with varying vbs., cf esp. (@)ma- tan, burtan, grätan, raftan, rasitan ; follow- ed by enclitics: apar-p-im ravišn I must needs ascend 4076, v.s.v. -p(i); — refer- ring back to an encl. pron.: api-š Vidrafš . ~ mšast and V. got on it (the horse) 25W5; cē-t avdom margéh ~ raset for at the end Death will come upon thee 726-7; (martömän) tāi-šān āmēcišn ~ nē barend as long as one does not impart instruction to them 801. — 2. prep. a) local: over, on, on to, down on: Krisäsp ~ én damik raset K. is roaming all over this earth 3318; ~ giyāk on the spot 3", 102; ~ ki Zartuxst bé dahém where we shall deposit Z. 3957; ~ pad ēstāt rose to his feet 1821; asp ... — rahy vartét harness the horse! 5418-14; srišk ~ srišk drop after drop 214
510:apar-barišnēh ['plbišnyh, MDM blšnyh, MDM YBLWN-šnyh, MDM YDLWN- Snyh] the act of ascending, ascension; transport, ecstasy 5121-25. 524.9, 5319; cf taš. — < apar + burtan (q.v.); opp. frēt-barišnēh (g. v.).
511:apar-burtārēh [MDM bwlt'lyh] the act of procuring, or the state of having procured 4425-26, — V, s. v. burtan.
671:aržānīkēnītan [~-ynytn'] to consider a p. worthy, governing a subordinated clause without an introducing particle, 5318 in a very complicated passage 5317-21, which only seems possible to understand on the following suppositions: a) kū-t bahr hac man bé burt l. 19 is not a gloss, as I have marked it, but is governed by anak tč bavat l. 17 ‘it shall be unhappy for thee that thou hast bereft ...'; b) the clause kē ... aržānīkēnīt hom 1.17-19 is loosely attached to tē l.17; c) for MNW-t L<y> (MS very clearly MNWtl) read MNW kw) LY» = kē tē man, to man being the exact counterpart of LK ^NH = tč an (v. žan) 1. 19 and both signifying ‘thou and I’; d) YBLWN-m l. 18 and 20, and HWH'-m 1. 19, are the Ist. p. pl. coinciding with the Ist p. sg.; e) there is a wordplay between *š = dé ‘food’ l. 18 and ’$ = as (demonic) eye’ 1. 20 (as burtan 'to have a vision', v. 'aš; bahr ‘ministry’, v. this w.). Text: anàk tč bavat, marak, ke t(0» man fratom hac ax" i astomand andar Rdg u Notar hac bahr barišneh āš barom frac aržānīkēnīt hom, kū-t bakr hac man bē burt. niin-ip tē an pat apar-barišneh aš barom u et bavēt kū-t dušcašmiha al zänak nikēram i-t nest ‘unhappy shall it be for thee, little scoundrel, (that thou) — as thou and I first of all men in the material world between Räg and Notar have been found worthy of earning food by perfor- mance of ministry — that thou hast bereft me of the ministry. Now thou and I shall be enraptured in an ecstatic vision, and then it will happen that I shall see thee evil-minded in another house that is not thine’. The passage is the immediate continuation of the incident related in 537-15, Zsprm XII, 7 epitomizes 5316-21 as follows: dwlyslwb BR’ L zltwšt gwpt' "VK cygwnt pltwm HWH'-m b’hl wlweyk BR’ ’pknd HWH'-m ZK tw "NH KR?
== HUB xavar/barid
```


## [2026-09-05T13:56:44.220Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"^burtan\\|burtan \\[YBLWN\\|burtan \\[\" NYB_vol2_glossary.txt | head -3; grep -n \"bārak\\|bālak \\[\" NYB_vol2_glossary.txt | head -3",
 "description": "Nyberg burtan headword"
}
```


### [2026-09-05T13:56:44.275Z] TOOL RESULT

```
1044:burtan [bwltn'; YBLWN-, YDLWN-tn'; forms v. I, 178] bar-, to carry, to bring, to bear, to wear, to procure; to take away, to remove (6 or pat ‘to’); arišk ~ to bear envy 691. 8419; !a&, bes, dast, dašn, gobišn, nam, namāc, nipart, paitäk, srav, stēžak, vāng, pat xrat ~: v. these ws.; bahr ~ v. barišneh; — to place on the top of (apar) 444; to lay a p. on (6) 4720-21; — andar 6 tan ~ to bring into corporeal existence 92t; — andarg ~, v. göbisn; — apar ~ to send out against 3711; to bring 6016; dmdcisn apar ~ to give instruction, to teach 80%; v. also apar-barisneh and apar-burtäreh ; — frac ~ to bring, to present 411; to bring forth, to light (a fire) 44°; — fröt ~ to bring down, to shed (water) 417°; v. also fröt- barišneh; — 6 ham ~ to collect, to amass 4815; pret. construed as an act. 187% Common Iranian; Av. OP (933 sqq.) also — (act. and middle) ‘to ride’, cf barak and asvār; cf also apar-barišneh from bar- ‘to move’.
920:ībārak [b'lk'] adj. of ?bàr in compounds: 2-— sāk double tax 119?.
1875:hanbārak [hnb’lk'] storehouse, larder 973-8.9.10, . MPrth ’mb’rg; Arm. lw. (h)ambar, Talm. ’mbr’, NP anbār; v. Telegdi 229.
2347:kurušk [kwlwšk'] ewe, of a big species of sheep 509-11, — Zsprm X, 20 in telling this story: meš kurušk i šīr-pistān "with milk in her udder’. Also kwryšk' = Paz. kurišk, koriák, BdA, p. 959-1? = BdJ2918— 303: meš 5 sratak: han i pat-dumb, han 4 a-dumb, u sak meš, u meš *takilé [tkly ; Paz. tagr, tgar] <u> kurišk tmeš, ke srub vazurg, asp homänäk, 3 köf [BdA corrected from tan, BdJ Paz. koh] dārēt api-š 6 bārak girénd, cigēn gobet ku Mānušcihr + amāh niyak kurišk-ē pat bārak dāšt [sak
```


## [2026-09-05T13:58:00.387Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"== HRN burden\"; grep -n \"burden 'tragen\\|^[0-9]*\\. burden\\|burden.*tragen\" HRN.txt | head -5; echo \"== HRN bar/xarwar/gehwareh\"; grep -n \"gehwäre\\|gehware\\|xarwär\\|charwär\\|dischwär\\|göschwäre\" HRN.txt | head -8; echo \"== BRT bar- verb\"; grep -n \"j\\., g\\.  bar-\\|g\\.,  j\\.  bar-\\|bar-  V\\.\" BRT.txt | head -5",
 "description": "Horn bordan and compounds; Bartholomae bar-"
}
```


### [2026-09-05T13:58:00.469Z] TOOL RESULT

```
== HRN burden
== HRN bar/xarwar/gehwareh
== BRT bar- verb
16793:*  i-t  Sj  P-  'bar-  V.  'tragen*.  Praes.  i iar^'\  2  bara-,  5  bjbar-  [,  25  barSit\, 27  (Pass.)  bairya-,  30  (Itcr.)  baraya-; Perf.  I  {bä)bar-'\  bavar- :  i^ar-.  —  PPfP. b»r>ta-;  PFP.  'barata-,  tipa.bsr^wa-  (nur Ableit.);  Inf.  'bgritse,  °hrftaya!-ca,  b»r»la, 'bfnte,  b?n%i,  bin^e,  barere,  'baral, 'baire;  AbsoL  b?r»t)m,  bar»nt)m,  bar»tn- lum,  i'>'b»rfntO,  •btrsis,  'bmth,  'birttam^'^.
16911:•  j.  'bar-  V.  'sich  rasch  bewegen'  (von Wind  und  Wasser)''.     Praes.  3  iara-.
```


## [2026-09-05T13:58:08.523Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'NR<=16793 && /^[[:space:]]*9[0-9][0-9][[:space:]]*$/ {c=$0;n=NR} END{print \"last col marker before bar-: line\",n,\"=\",c}' BRT.txt; sed -n '16780,16795p' BRT.txt | grep -n \"^[0-9]\" ; awk 'NR>16700 && NR<16800 && /^[[:space:]]*[0-9]{3}[[:space:]]*$/ {print NR\": \"$0}' BRT.txt",
 "description": "Bartholomae column number for bar-"
}
```


### [2026-09-05T13:58:10.505Z] TOOL RESULT

```
last col marker before bar-: line 16787 = 934
8:934
16743: 939
16746: 930
16763: 931
16766: 932
16787: 934
```


## [2026-09-05T14:04:56.563Z] TOOL CALL #76: Bash

```json
{
 "command": "cat > /home/sfmqrb/git/rishe/data/verification/page-88.json <<'JSONEOF'\n{\n  \"pdf_page\": 88,\n  \"book_page\": 58,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-05\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Bhengh\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *bʰenǵʰ- / *bʰn̥ǵʰ- (adj. *bʰn̥ǵʰú-s) 'thick, dense, fat'\",\n      \"note\": \"Pokorny 127-128 b'engh-, b'ngh- (Adj. b'nghu-s) 'dick, dicht, feist' = Walde-Pokorny II 151; Watkins/AHD 'bhengh-. Thick, fat.' Nourai's root name, the 'Indo-European' label and the gloss 'thick, fat' are all exactly the standard ones, and POK:127 is the right page. Note that the Greek adjective is a zero-grade *bʰn̥ǵʰú-s, while the Avestan s-stem bązah- continues *bʰn̥ǵʰ-es-; Pokorny explicitly equates Gk. πάχος (for *πένγχος) with Av. bązah-, so Nourai's two branches are genuinely the same root. Extraction is faithful to the printed page except that the printed gloss of the Greek node reads 'tick' (see node #4).\",\n      \"note_fa\": \"ریشهٔ هندواروپایی آغازین *bʰenǵʰ- «ستبر، انبوه، فربه» است که پوکورنی در صفحهٔ ۱۲۷–۱۲۸ و والده-پوکورنی در جلد دوم صفحهٔ ۱۵۱ آن را با همین معنا آورده‌اند و واتکینز (پیوست ریشه‌های هندواروپایی فرهنگ American Heritage) نیز همان را تکرار می‌کند. نام ریشه، برچسب زبانی و معنایی که نورایی داده درست است و ارجاع POK:127 نیز دقیق است. صورت یونانی paxús از ستاک کوتاه *bʰn̥ǵʰú- و صورت اوستایی bązah- از ستاک ـas (*bʰn̥ǵʰ-es-) می‌آید؛ پوکورنی خودِ πάχος یونانی را برابر bązah اوستایی می‌داند، پس دو شاخهٔ نمودار به‌راستی از یک ریشه‌اند. ادعای نورایی دربارهٔ ریشه درست است.\",\n      \"sources\": [],\n      \"ref_check\": [\n        {\"ref\": \"POK:127\", \"status\": \"supports\", \"note\": \"POK_full.txt line 12128: 'Root/ lemma: b^engh-, b^ngh-(Adj. b^nghu-s) / Meaning: thick, fat ... Page(s): 127-128'; material列 lists 'Avestan bązah- n. height, depth' and 'gr. παχύς thick, dense, fat'. Exactly Nourai's root and gloss.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"WLD\", \"where\": \"Bd. II p. 151 (WLD_Bd2_pages.txt leaf 156)\", \"stance\": \"supports\", \"note\": \"'bhengh-, bhngh- (Adj. bhnghu-s) \\\"dick, dicht, feist\\\": Ai. bahú- ... av. bazah- n. \\\"Höhe, Tiefe\\\", bąznu- m. ds., bal. baz \\\"viel\\\" ... gr. παχύς'. This is the WP II 151 that Pokorny cites.\"},\n        {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.v. bhengh- (AHD_watkins1985.txt line 332)\", \"stance\": \"supports\", \"note\": \"'bhengh-. Thick, fat. Extended zero-grade form *bhnghu- in Greek pakhus, thick, fat: PACHYDERM, PACHYSANDRA. [Pok. bhengh- 127.]'\"},\n        {\"src\": \"IEC\", \"where\": \"Mann, grep 'bhengh'/'bhnghus'\", \"stance\": \"silent\", \"note\": \"Mann's comparative dictionary has no lemma for this root under any spelling I tried (bhengh, bhnghus, bhenghos); he does have the bhero family (line 1261 ff.).\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan\",\n          \"words\": \"bazah\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Avestan bązah- (Nourai prints bazah, without the nasal hook) is a neuter s-stem 'height, depth', PIE *bʰn̥ǵʰ-es-, i.e. the zero grade of *bʰenǵʰ- 'thick' plus the -as-/-es- abstract suffix; the semantic step is 'thickness, bulk' > 'extent in the vertical dimension' > 'height, depth'. Bartholomae col. 963 glosses it 'Höhe, Tiefe' and cites Yasna 19.7 ('so gross an Höhe (Tiefe) wie an Breite'), with the by-form bąznu- m. and the comparison ai. bahulá-. Pokorny 127 makes the equation explicit: Greek πάχος n. 'thickness' stands for an older *πένγχος = Avestan bązah-. So both the form and Nourai's arrow from the root are correct; only the transliteration lacks the nasal.\",\n          \"derivation_fa\": \"«بَزَه» اوستایی bązah- (نورایی بدون خیشومی، bazah، نوشته است) اسمی است خنثی از گونهٔ ستاک ـah، برگرفته از صورت صفرِ ریشهٔ هندواروپایی *bʰn̥ǵʰ-es- «ستبری»؛ تحول معنایی از «ستبری، حجم» به «بلندی/ژرفا» است. بارتولومه در ستون ۹۶۳ فرهنگ ایرانی باستان آن را «Höhe, Tiefe» معنی کرده و شاهد یسنا ۱۹٫۷ را آورده و گونهٔ bąznu- و هم‌ریشگی با سنسکریت bahulá- را یاد کرده است. پوکورنی نیز πάχος یونانی را دگرگون‌شدهٔ *πένγχος و برابر bązah اوستایی می‌داند. پس ادعای نورایی درست است و تنها آوانگاری او خیشومی ą را نشان نمی‌دهد.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"POK:127\", \"status\": \"supports\", \"note\": \"POK_full.txt (Page(s): 127-128): 'Avestan bązah- n. height, depth, bqsnu- m. ds.' — the very form and gloss of the node.\"},\n            {\"ref\": \"KLN:1109\", \"status\": \"not_found\", \"note\": \"Klein 1966 has no Avestan headwords; by the leaf/page mapping in refs_online.json (leaf ≈ p/2 + 12) p.1109 falls in the range 'Norman-ize … nuance' (KLN_1966.txt leaves 566-568), which has nothing to do with this root. Klein's relevant entries, 'pachy-' and 'pachyderm', are at leaf 593 ≈ p.1161. Either the page number is a misprint or it belongs to a different edition.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"col. 963 (BRT.txt line 17243)\", \"stance\": \"supports\", \"note\": \"'j. bazah- n. \\\"Höhe, Tiefe\\\": … Y.19.7 … Vgl. bąznav-. — ai. vgl. bahulá-. — Pü. zakāk.' Bartholomae also has bąznav- m. 'Höhe, Tiefe' in the next column.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. II p. 151\", \"stance\": \"supports\", \"note\": \"'av. bazah- n. \\\"Höhe, Tiefe\\\", bąznu- m. ds.' listed directly under bhengh-.\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. bhengh-\", \"stance\": \"silent\", \"note\": \"Watkins cites only the Greek reflex; no Iranian material.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"bâz «باز ۱»\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"The word is real: New Persian باز is a length measure = the span between the two outstretched arms (a fathom), with the variants بازه and باژ that Nourai lists in the 'extra' line. But modern scholarship does not derive it from Avestan bązah- 'height, depth'. Horn, Grundriss no. 167 (p. 38-39) treats it under bāzū 'Arm' (Av. bāzu-, Skt. bāhú-, Arm. lw. bazuk, Oss. bäzug) and says expressly: 'Gehört hierher auch np. bāz \\\"Klafter\\\" (Vullers: 8), \\\"Spanne\\\" (Vullers: 9), vergl. bāze, also ursprünglich \\\"Armlänge, Elle\\\"?' — i.e. bāz/bāze is a derivative of the word for ARM, PIE *bʰeh₂ǵʰu-s 'elbow, arm' (Pokorny 108: Skt. bāhú-, Av. bāzau-, Gk. πῆχυς, OHG buog), a root Pokorny keeps strictly apart from *bʰenǵʰ- 'thick' (p. 127). Semantically 'arm-length' is the obvious source of 'span of two outstretched arms', while 'height, depth' is not. Nourai has attached the word to the wrong (though superficially similar) root.\",\n          \"derivation_fa\": \"واژه واقعی است: «باز ۱» در فارسی نو یکای درازا به اندازهٔ فاصلهٔ دو دستِ گشوده است و گونه‌های «بازه» و «باژ ۱» نیز همان‌جا آمده‌اند. اما ریشه‌شناسی امروزی آن را از bązah- اوستایی «بلندی، ژرفا» نمی‌گیرد. هرن در بند ۱۶۷ «مبانی ریشه‌شناسی فارسی نو» (ص ۳۸–۳۹) این واژه را ذیل «بازو» می‌آورد و می‌نویسد که np. bāz «قُلاج/باز» و «وَجَب» و نیز bāze به همین خانواده تعلق دارند و در اصل به‌معنی «درازای بازو، ذراع» بوده‌اند. یعنی «باز» از ریشهٔ هندواروپایی *bʰeh₂ǵʰu- «بازو، آرنج» (پوکورنی ص ۱۰۸: سنسکریت bāhú-، اوستایی bāzav-، یونانی πῆχυς) است، ریشه‌ای که پوکورنی آن را از *bʰenǵʰ- «ستبر» (ص ۱۲۷) کاملاً جدا می‌داند. از نظر معنایی هم «درازای بازو» سرچشمهٔ طبیعی «فاصلهٔ دو دستِ گشوده» است نه «بلندی و ژرفا». پس پژوهش امروزی ادعای نورایی را رد می‌کند و «باز» را هم‌ریشهٔ «بازو» می‌داند.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%A8%D8%A7%D8%B2%D9%88\",\n            \"https://en.wiktionary.org/wiki/%D8%A8%D8%A7%D8%B2\",\n            \"https://abadis.ir/fatofa/%D8%A8%D8%A7%D8%B2/\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"MON:452\", \"status\": \"partial\", \"note\": \"Mo'in's entry for باز (read via abadis.ir/fatofa/باز, section فرهنگ معین) does give the sense 'واحد اندازه‌گیری طول برابر با امتداد دو دست در حالی که دست‌ها به صورت افقی از هم باز شده' — i.e. Nourai's gloss is Mo'in's. But Mo'in attaches no origin tag to that sense, so the reference supports the WORD and its meaning, not the derivation from bązah-.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"HRN\", \"where\": \"no. 167 'bāzū Arm', p. 38-39 (HRN.txt leaf 59, line 1838)\", \"stance\": \"contradicts\", \"note\": \"'Gehört hierher auch np. bāz \\\"Klafter\\\" (Vullers: 8), \\\"Spanne\\\" (Vullers: 9), vergl. bāze, also ursprünglich \\\"Armlänge, Elle\\\"?' — Horn puts bāz and bāze under bāzū 'arm' (aw. bāzu-, phlv. bāzūh, ai. bahú-), not under bązah-.\"},\n            {\"src\": \"POK\", \"where\": \"p. 108 (POK_full.txt line 10610 ff.)\", \"stance\": \"contradicts\", \"note\": \"'Root/lemma: b^aghu-s, Meaning: elbow, arm. Old Indic bahú-h m. arm, Avestan bāzau-s arm ... gr. πῆχυς ... Page(s): 108' — a root Pokorny keeps entirely separate from bhengh- (p.127).\"},\n            {\"src\": \"BQT/MON via web\", \"where\": \"Wiktionary باز (all four etymology sections) and بازو\", \"stance\": \"partial\", \"note\": \"Wiktionary has no 'fathom' sense for باز at all (only 'open', 'again', 'falcon', and the participle of باختن), while بازو is derived from Old Persian bāzu- < PII *bʰaHȷ́ʰúš < PIE *bʰeh₂ǵʰús — confirming the arm-root, not bązah-.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Sogdian\",\n          \"words\": \"db`nz\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Buddhist and Christian Sogdian δβʾnz (Gharib's transcription δβanz) 'thick, wide, coarse', with the comparative δβʾnstr and the abstract δβʾnzkwy 'thickness'. Gharib reconstructs it as *dwa-bazah-, i.e. a compound/prefixed formation on the same *bazah- 'thickness, height' as the Avestan node, and cross-refers to 'Av. bazah'; the initial δβ- reflects the Sogdian development of the cluster and the -nz spelling the nasalized ą of *bąz-. Nourai's transliteration 'db`nz' is a plain ASCII rendering of δβʾnz (d = δ, b = β, ` = ʾ aleph), and the gloss 'wide, coarse' is verbatim Gharib's.\",\n          \"derivation_fa\": \"واژهٔ سغدی δβʾnz (در آوانگاری قریب: δβanz) در متون بودایی و مسیحی به‌معنی «ستبر، پهن، درشت» است؛ صورت برتری آن δβʾnstr و اسم معنای آن δβʾnzkwy «ستبری» است. قریب آن را از *dwa-bazah- می‌داند و صریحاً به bazah اوستایی ارجاع می‌دهد؛ خوشهٔ آغازین δβ- تحول سغدی و املای ـnz بازتاب خیشومی ą در *bąz- است. آوانگاری «db`nz» نورایی همان δβʾnz است (d برای δ، b برای β و ` برای الف) و معنای «wide, coarse» عیناً از قریب گرفته شده. ادعای نورایی درست است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"SOD:137\", \"status\": \"supports\", \"note\": \"Gharib entry 3471 (SOD_pages.txt form-feed page 203; printed page = leaf − 66 = 137, exactly Nourai's number): '3471 δβʾnz B, S / δβanz ©<*dwabazah; Av. bazah / wide, coarse  δβʾnstr'. Neighbouring entry 3472 δβʾnzqʾwyy 'thickness'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"SOD\", \"where\": \"entries 3471-3473 and the English index s.v. 'coarse' (1679, 3471, 8986)\", \"stance\": \"supports\", \"note\": \"The index confirms 3471 is one of the entries glossed 'coarse'; 3473 δβʾnzkwy is cross-referred to 3472.\"},\n            {\"src\": \"POK\", \"where\": \"p. 127-128 s.v. bhengh-\", \"stance\": \"silent\", \"note\": \"Pokorny lists Old Indic, Avestan, Baluchi, Greek, Germanic, Latvian, Latin, Tocharian and Hittite, but no Sogdian; the Sogdian reflex is Gharib's addition and is not contradicted.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Greek\",\n          \"words\": \"paxus\",\n          \"verdict\": \"transcription_suspect\",\n          \"derivation\": \"The Greek word is right: παχύς pakhús 'thick, stout, fat', from the zero grade *bʰn̥ǵʰú-s (Pokorny 127; Watkins s.v. bhengh-), with the comparative πάσσων and the noun πάχος 'thickness' (= Av. bązah-). Nourai's 'paxus' is his usual ASCII transliteration (x = χ). What is wrong is the gloss: the box reads 'tick', which is a printer's slip for 'thick' — the child node immediately below glosses English pachy- as 'thick'. I rendered PDF page 88 at 300/400 dpi and read the Greek box directly: the printed page itself shows 'paxus : tick', so the extraction is faithful and the error is the book's. Page image saved to data/verification/sources/refs/ocr/BOOK/88.png.\",\n          \"derivation_fa\": \"خودِ واژهٔ یونانی درست است: παχύς (pakhús) «ستبر، فربه» از صورت صفرِ *bʰn̥ǵʰú-s (پوکورنی ص ۱۲۷؛ واتکینز ذیل bhengh-)، با صفت برتری πάσσων و اسم πάχος «ستبری» که برابر bązah اوستایی است. آوانگاری «paxus» شیوهٔ خودِ نورایی است (x برای χ). اما معنای چاپ‌شده «tick» غلط چاپی به‌جای «thick» است؛ در همان صفحه، خانهٔ فرزندِ انگلیسی pachy- را «thick» معنی کرده است. تصویر صفحهٔ ۸۸ کتاب را با دقت ۴۰۰ نقطه بر اینچ بازخوانی کردم: در خودِ کتاب «paxus : tick» چاپ شده است؛ پس خطای چاپی کتاب است نه خطای خوانش اسکن.\",\n          \"error_in\": \"book\",\n          \"book_prints\": \"paxus : tick\",\n          \"correct_form\": \"paxus (παχύς) : thick\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 (AHD_watkins1985.txt line 332): 'bhengh-. Thick, fat. Extended zero-grade form *bhnghu- in Greek pakhus, thick, fat: PACHYDERM, PACHYSANDRA.' — the AHD appendix Nourai cites gives 'thick', which is what the box should read.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"p. 127\", \"stance\": \"supports\", \"note\": \"'gr. παχύς \\\"thick, dense, fat, obese\\\" (compounds πάσσων), πάχος n. \\\"thickness, fatness\\\" (occurs after παχύς for *πένγχος = Avestan bązah-)'.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. II p. 151\", \"stance\": \"supports\", \"note\": \"gr. παχύς equated with ai. bahú-, with the comparative/superlative bahīyas-, baṃhiṣṭha- = gr. παχύς.\"},\n            {\"src\": \"KLN\", \"where\": \"leaf 593 ≈ p. 1161, s.v. pachy-\", \"stance\": \"supports\", \"note\": \"'pachy-, combining form meaning \\\"thick, dense\\\"' — Klein too glosses it 'thick'.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"English\",\n          \"words\": \"pachy-; pachyderm\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English pachy- is the learned combining form of Greek παχύς 'thick', taken directly into scientific Latin/English nomenclature. pachyderm is a 19th-c. borrowing of French pachyderme, coined by Cuvier (1797) from Greek παχύδερμος 'thick-skinned' = παχύς + δέρμα 'skin' (gen. δέρματος), and used as the name of Cuvier's order Pachydermata (elephant, rhinoceros, hippopotamus); hence also pachydermatous and (US) pachysandra. The cross-reference ☞Der 1 for the second element (δέρμα, PIE *der- 'to split, flay') is correct.\",\n          \"derivation_fa\": \"جزء ترکیبی pachy- در انگلیسی همان παχύς یونانی «ستبر» است که مستقیماً وارد اصطلاح‌سازی علمی لاتینی-انگلیسی شده است. واژهٔ pachyderm در سدهٔ نوزدهم از فرانسویِ pachyderme گرفته شده که کوویه (۱۷۹۷) از παχύδερμος یونانی «ستبرپوست» (παχύς + δέρμα «پوست») ساخت و نام رستهٔ Pachydermata (فیل، کرگدن، اسب آبی) شد؛ از همین‌جا pachydermatous و pachysandra. ارجاع نورایی برای جزء دوم به ریشهٔ «Der 1» (δέρμα از *der- «شکافتن، پوست کندن») نیز درست است. ادعای نورایی درست است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 s.v. bhengh- ends '…in Greek pakhus, thick, fat: PACHYDERM, PACHYSANDRA', and the AHD index (line 2031) has 'PACHYDERM bhengh-'. Exactly the arrow drawn.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"leaf 593 ≈ pp. 1161-1162, s.vv. pachy-, pachyderm, pachydermatous, pachydermia\", \"stance\": \"supports\", \"note\": \"'pachyderm, n., a thick-skinned animal, as the elephant, rhinoceros and hippopotamus. — F. pachyderme, fr. Gk. παχύδερμος \\\"thick-skinned\\\", which is compounded of παχύς \\\"thick\\\", and δέρμα, gen. δέρματος, \\\"skin\\\". See pachy- and derma.'\"},\n            {\"src\": \"SKT\", \"where\": \"Skeat, grep 'pachyderm'\", \"stance\": \"silent\", \"note\": \"Skeat's Concise Etymological Dictionary has no entry for pachyderm (it omits most technical Greek coinages).\"}\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 1,\n      \"root\": \"Bher 1, Bhrâ-tar\",\n      \"verdict\": \"plausible\",\n      \"modern_form\": \"PIE *bʰer- 'to carry, bear' (Pok. 128-132); PIE *bʰréh₂tēr 'brother' (Pok. 163-164)\",\n      \"note\": \"Both roots are real and both page numbers are right: POK 128-132 'b^er-1, Meaning: to bear, carry' (with 'Avestan baraiti ds. (and \\\"ride\\\")' and 'Old pers. barantiy'), and POK 163-164 'b^rāter-, brother'. Buck's SYN:107 is indeed §2.44 BROTHER (Av. brātar-, Skt. bhrātar-, Lat. frāter). What is only plausible is Nourai's semantic bracketing of the two as one entry, glossing Bhrâ-tar as 'load carrier (of family)': that old derivation of *bʰréh₂tēr from *bʰer- is explicitly rejected by Walde-Pokorny II 153 ('… noch durch *bhrāter- \\\"Bruder\\\", dessen Wzverwandtschaft unerwiesen ist'), and Pokorny lists bhrāter- as an independent lemma. Modern handbooks (Beekes, Kroonen, Wiktionary) treat *bʰréh₂tēr as of unknown further origin. EXTRACTION ERROR to fix in the source JSON: on the printed page the vertical connector that feeds the Pahlavi box and the two lower Avestan boxes springs from the BOTTOM EDGE of the 'Avestan / Old Persian' box (verified on a 400-dpi crop), so nodes #4 and #6 are children of node #1, not of the root; the JSON gives them parent 0.\",\n      \"note_fa\": \"هر دو ریشه واقعی‌اند و شماره‌های ارجاع نیز درست: پوکورنی ص ۱۲۸–۱۳۲ ذیل *bʰer- «بردن، حمل کردن» (با baraiti اوستایی «می‌برد» و نیز «سوار شدن» و barantiy پارسی باستان) و ص ۱۶۳–۱۶۴ ذیل *bʰrāter- «برادر»؛ باک نیز در ص ۱۰۷ بخش ۲٫۴۴ «برادر» را آورده است. آنچه تنها «با احتیاط پذیرفتنی است» گره زدن این دو در یک مدخل و معنی‌کردن Bhrâ-tar به «بارکشِ خانواده» است: والده-پوکورنی در جلد دوم ص ۱۵۳ صریحاً می‌گوید هم‌ریشگی *bhrāter- با bher- اثبات‌نشده است و پوکورنی آن را مدخلی مستقل می‌آورد؛ ریشه‌شناسی امروزی نیز خاستگاه دورتر *bʰréh₂tēr را ناشناخته می‌داند. نکتهٔ داده‌ای: در صفحهٔ چاپی، خط عمودی که به خانه‌های «پهلوی» و دو خانهٔ «اوستایی» پایین می‌رسد از لبهٔ زیرین خانهٔ «اوستایی/پارسی باستان» بیرون می‌آید، پس گره‌های ۴ و ۶ فرزند گرهٔ ۱ هستند نه فرزند ریشه.\",\n      \"sources\": [],\n      \"ref_check\": [\n        {\"ref\": \"POK:128\", \"status\": \"supports\", \"note\": \"POK_full.txt line 12758: 'Root / lemma: b^er-1 / Meaning: to bear, carry … Old Indic bharati carries, Avestan baraiti ds. (and \\\"ride\\\"), Old pers. barantiy 3. Pl. ds. (= Armenian berem, Phrygian ab-beret, gr. φέρω, Latin fero, Old Irish biru, alb. bie, Gothic baira, OCS berǫ)'. Page(s): 128-132.\"},\n        {\"ref\": \"POK:163\", \"status\": \"supports\", \"note\": \"POK_full.txt Page(s): 163-164 = lemma b^rāter- 'brother' (Skt. bhrātar-, Av./OP brātar-, Lat. frāter, Goth. brōþar, Toch. A pracar).\"},\n        {\"ref\": \"SYN:107\", \"status\": \"supports\", \"note\": \"SYN.txt line 2908 (leaf 131 = printed p. 107): 'MANKIND: SEX, AGE, FAMILY RELATIONSHIP 107 | 2.44 BROTHER … Skt. bhrātar-, Av. brātar-, Lat. frāter …'. The page number is exactly right.\"},\n        {\"ref\": \"KAS:10\", \"status\": \"not_checked\", \"note\": \"Da'i al-Eslam's Persian Sanskrit primer (Khod-amuz-e Zaban-e Sanskrit); refs_online.json records no copy on archive.org and only a login-walled PDF at ketabnak.\"},\n        {\"ref\": \"PRT:234\", \"status\": \"not_checked\", \"note\": \"Partridge, Origins (1958) is lending-only on archive.org (refs_online.json 'archive_restricted'); no local text.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"WLD\", \"where\": \"Bd. II p. 153 (WLD_Bd2_pages.txt leaf 158)\", \"stance\": \"partial\", \"note\": \"'1. bher \\\"tragen, bringen\\\" usw. (auch Leibesfrucht tragen; med. \\\"ferri\\\") … Ai. bhárati \\\"trägt\\\", av. baraiti ds. (und \\\"reiten\\\", s. zuletzt Charpentier), ap. barantiy'. But the same paragraph denies the link Nourai assumes: 'ein *bherē wird weder durch aksl. bĭrati erwiesen, noch durch *bhrāter- \\\"Bruder\\\", dessen Wzverwandtschaft unerwiesen ist'.\"},\n        {\"src\": \"WLD\", \"where\": \"Bd. II p. 193 (leaf 198)\", \"stance\": \"supports\", \"note\": \"'bhrator- (auch bhrāter- nach poter-, māter-, dhugh(a)ter-) \\\"Bruder\\\". Ai. bhrātar-, av. ap. brātar- \\\"Bruder\\\"' — a separate lemma, as in Pokorny.\"},\n        {\"src\": \"AHD\", \"where\": \"Watkins 1985, index (line 1276 'BAIRN bher-1') and s.v. bhrāter-\", \"stance\": \"supports\", \"note\": \"Watkins likewise keeps bher-1 'to carry' and bhrāter- 'brother' apart (BROTHER is indexed to bhrater-, BURDEN to bher-1).\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan / Old Persian\",\n          \"words\": \"bar; baraiti\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Avestan bar- 'to carry' is the direct continuant of PIE *bʰer-; Bartholomae col. 934 lists '¹bar- V. \\\"tragen\\\"' with pres. bara-, bibar-, barəiti (3sg.), passive bairya-, iterative bāraya-, perf. (bā)bar-, ppp. bərəta-. baraiti is exactly that 3sg. present, formed with thematic *-e/o- + primary ending, = Skt. bhárati, Gk. φέρει, Lat. fert/ferit. Old Persian has the same stem in barantiy (3pl.) and in the nominal derivative asabāra- 'horseman'. Nourai's second gloss 'ride a horse' is not an invention: Pokorny 128 and Walde-Pokorny II 153 both note 'av. baraiti ds. (und \\\"reiten\\\")' after Charpentier, and Nyberg's glossary says of burtan '— Common Iranian; Av. OP also (act. and middle) \\\"to ride\\\", cf. barak and asvār'; the sense arises from the horse 'carrying' its rider, whence Middle Persian bārag 'mount'.\",\n          \"derivation_fa\": \"ستاک اوستایی bar- «بردن، حمل کردن» دنبالهٔ مستقیم ریشهٔ هندواروپایی *bʰer- است؛ بارتولومه در ستون ۹۳۴ آن را «¹bar- V. tragen» آورده با مضارع bara-، bibar-، سوم‌شخص barəiti، مجهول bairya-، تکراری bāraya- و اسم مفعول bərəta-. صورت baraiti همان سوم‌شخص مفرد مضارع است، برابر با bhárati سنسکریت، φέρει یونانی و fert لاتینی. در پارسی باستان همین ستاک در barantiy (سوم‌شخص جمع) و در مشتق asabāra- «سوارکار» دیده می‌شود. معنی دومی که نورایی داده («سوار شدن») ساختگی نیست: پوکورنی (ص ۱۲۸) و والده-پوکورنی (ج ۲ ص ۱۵۳) هر دو به پیروی از شارپانتیه می‌نویسند baraiti اوستایی معنی «سوار شدن» هم دارد، و نیبرگ نیز ذیل burtan همین را می‌گوید و به barak و asvār ارجاع می‌دهد؛ خاستگاه این معنی آن است که اسب سوار را «می‌بَرَد» — از همین‌جا bārag «مرکب» در فارسی میانه. ادعای نورایی درست است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"POK:128\", \"status\": \"supports\", \"note\": \"'Avestan baraiti ds. (and \\\"ride\\\"). Old pers. barantiy 3. Pl. ds.' — both the form baraiti, the gloss 'carries' and the extra sense 'ride' that Nourai gives.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"col. 934 (BRT.txt line 16793)\", \"stance\": \"supports\", \"note\": \"'¹bar- V. \\\"tragen\\\". Praes. 1 bara-, bibar-, barəiti, (Pass.) bairya-, (Iter.) bāraya-; Perf. (bā)bar-, bavar-; PPfP. bərəta-…' (a homonymous ²bar- 'sich rasch bewegen' is kept separate at line 16911).\"},\n            {\"src\": \"KNT\", \"where\": \"Kent, Old Persian, §126 and Lexicon (KNT.txt lines 1788, 5215)\", \"stance\": \"supports\", \"note\": \"'a vriddhied or lengthened grade (§126), as in kāma-, asa-bāra-' and 'uvasabāra- sb. \\\"good horseman\\\": u- \\\"good\\\" + asabāra- \\\"horseman\\\", with vriddhi. uvāsabara nsm. DNb 42' — the Old Persian bar-stem is attested.\"},\n            {\"src\": \"NYB\", \"where\": \"Glossary s.v. burtan (NYB_vol2_glossary.txt line 1044)\", \"stance\": \"supports\", \"note\": \"'burtan [bwltn'; YBLWN-, YDLWN-tn'] bar-, to carry, to bring, to bear … Common Iranian; Av. OP (933 sqq.) also — (act. and middle) \\\"to ride\\\", cf. barak and asvār'.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. II p. 153\", \"stance\": \"supports\", \"note\": \"'Ai. bhárati \\\"trägt\\\", av. baraiti ds. (und \\\"reiten\\\") … ap. barantiy 3. pl.'\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Pahlavi\",\n          \"words\": \"burtan; bâr 1; xâyak-bâr\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"Two of the three words are solid. (a) burtan/burdan is the Middle Persian infinitive to the present stem bar-: MacKenzie p. 20 'burdan, bar- [YBLWN-tn' < Aram. ybl; bwltn', bl- | M burdan, br-, N ~] carry, bear, take, endure', formed on the ppp. *bṛta- (Av. bərəta-) + -tan; Nourai's spelling burtan is Nyberg's transliteration of the same word. (b) bār 'load, burden' is MacKenzie's '³bār [b'l | M b'r, N ~] load, burden; duty', a *bāra- noun of the same root. (c) xāyak-bār is NOT attested: neither MacKenzie nor Nyberg has it. Middle Persian has xāyag 'egg' (MacKenzie xāyagdēs 'oval'), but the caviar-word is not recorded before New Persian, and the standard analysis of its second element is dār 'holding' (< *dar- 'to hold'), not bār: Etymonline gives 'Persian khaviyar, from khaya \\\"egg\\\" (from MP khayak) + dar \\\"bearing\\\"'; Wiktionary prefers Szemerényi's quite different account (an Iranian compound of an Ossetic-type kæf 'fish' with an Indo-Aryan jaro 'egg', literally 'fish-eggs'). Since one of the node's three words is a reconstruction with a disputed second element, the node takes the worst verdict.\",\n          \"derivation_fa\": \"دو واژه از سه واژه استوارند. الف) burtan/burdan مصدر فارسی میانه از ستاک مضارع bar- است؛ مکنزی (ص ۲۰) می‌آورد: «burdan, bar- … carry, bear, take, endure»؛ ساخت آن از اسم مفعول *bṛta- (اوستایی bərəta-) به‌علاوهٔ ـtan است و املای burtan نورایی همان آوانگاری نیبرگ است. ب) bār «بار، وظیفه» نیز در مکنزی هست: «³bār … load, burden; duty»، اسمی از همان ریشه با پسوند *-āra-. ج) اما xāyak-bār در هیچ‌یک از فرهنگ‌های پهلوی (مکنزی، نیبرگ) نیامده است. فارسی میانه xāyag «تخم» دارد (مکنزی: xāyagdēs «بیضی»)، ولی واژهٔ خاویار پیش از فارسی نو ثبت نشده و جزء دوم آن را ریشه‌شناسان امروزی «دار» (از ریشهٔ *dar- «داشتن») می‌دانند نه «بار»: Etymonline می‌نویسد «Persian khaviyar، از khaya \\\"تخم\\\" + dar \\\"دارنده\\\"»؛ ویکی‌واژه حتی تحلیل یکسره دیگری از سمرنیی می‌آورد (ترکیبی ایرانی از kæf «ماهی» و jaro «تخم»). چون یکی از سه واژهٔ این خانه بازسازی‌ای با جزء دوم مورد اختلاف است، حکم کلی خانه «رد‌شده/مورد اختلاف» است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/caviar\",\n            \"https://en.wiktionary.org/wiki/%D8%AE%D8%A7%D9%88%DB%8C%D8%A7%D8%B1\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"BQT:253\", \"status\": \"partial\", \"note\": \"BQT vol. 1 printed p. 253 = BQT_v1_pages.txt form-feed page 473 (leaf − 220, the offset given in refs_online.json for the middle of vol. 1). That page carries برخوردار، برد، «ماضی بردن است» — i.e. it is indeed the بردن/برخوردار neighbourhood Nourai is pointing at, and برخوردار is one of the words in his 'extra' line for node #3. The Persian OCR of the vol.-1 text is too corrupt to read Mo'in's Pahlavi footnote itself, so I can confirm the page but not the wording; nothing on it mentions xāyak-bār.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"MacKenzie pp. 18-20, s.vv. burdan, ³bār, bārag, xāyagdēs (PHD.txt lines 292, 252, 3013)\", \"stance\": \"partial\", \"note\": \"'burdan, bar- [YBLWN-tn' < A ybl; bwltn', bl- | M burdan, br-, N ~] carry, bear, take, endure. ~išn: bearing, behaviour' and '³bar [b'l | M br, N ~] load, burden; duty' — both supported; but MacKenzie has no *xāyag-bār (only 'oval xāyagdēs').\"},\n            {\"src\": \"NYB\", \"where\": \"Glossary s.v. burtan (line 1044) and apar-burtārēh (line 511)\", \"stance\": \"supports\", \"note\": \"'burtan [bwltn'; YBLWN-, YDLWN-tn'] bar-, to carry, to bring, to bear, to wear, to procure' — Nourai's exact form and gloss; no xāyak-bār.\"},\n            {\"src\": \"Etymonline\", \"where\": \"s.v. caviar\", \"stance\": \"contradicts\", \"note\": \"'from Persian khaviyar, from khaya \\\"egg\\\" (from Middle Persian khayak \\\"egg\\\", from Old Iranian *qvyaka-) + dar \\\"bearing\\\"' — the second element is dār, not bār.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Persian\",\n          \"words\": \"bordan «بردن»; bâr 1 «بار ۱»; xâvîyâr «خاویار»; barîd «بَرید»; bâreh «باره»\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"Three words are confirmed, two are not. (a) بردن bordan < MP burdan, pres. stem bar- (بَر, Nourai's 'extra' بَر ۳), the ordinary Iranian *bar- verb; برخوردار is bar-xwardār, also on this stem. (b) بار ۱ 'load' < MP bār; the sense 'fruit (of a tree)' is a Persian metaphor 'what the tree carries', already classical. (c) باره 'steed' < MP bārag 'mount, horse' (MacKenzie), a *bāraka- 'the carrying one'; the Ferdowsī couplet Nourai quotes ('یکی ترگ رومی به سر برنهاد / یکی باره زیراندرش همچو باد') uses it in exactly that sense. (d) خاویار is disputed: see node #2 — the received analysis is xāya 'egg' + dār 'bearing', and Wiktionary follows Szemerényi in taking it out of the Persian bar- family altogether. (e) بَرید is disputed and is in fact the classic counter-example: modern scholarship derives Arabic بريد barīd 'post, courier' from Latin verēdus 'post-horse' (itself Gaulish *werēdos) through Byzantine Greek βερέδος, and Persian برید is a re-borrowing from Arabic — a round trip in the opposite direction from the one Nourai draws. Nourai's own NOTE fairly reports the two camps, but its second half is inaccurate (see the entry note and ref_check on AKD).\",\n          \"derivation_fa\": \"سه واژه پذیرفتنی‌اند و دو واژه نه. الف) «بردن» از burdan فارسی میانه با ستاک مضارع bar- («بَر ۳» در فهرست خودِ نورایی) و «برخوردار» نیز بر همین ستاک ساخته شده است. ب) «بار ۱» از bār فارسی میانه؛ معنی «میوهٔ درخت» استعاره‌ای فارسی است («آنچه درخت برمی‌دارد») و از متون کلاسیک شاهد دارد. ج) «باره» از bārag فارسی میانه «مرکب، اسب» (مکنزی)، از *bāraka- «برنده/کشنده»؛ بیت فردوسی که نورایی آورده دقیقاً همین معنی را دارد. د) «خاویار» مورد اختلاف است (نگاه کنید به گرهٔ ۲): تحلیل رایج xāya «تخم» + dār «دارنده» است و ویکی‌واژه به پیروی از سمرنیی آن را یکسره از خانوادهٔ bar- بیرون می‌برد. ه) «بَرید» نیز مورد اختلاف و در واقع نمونهٔ کلاسیک نقض این نمودار است: پژوهش امروزی «بريد» عربی را از verēdus لاتینی «اسب چاپار» (خود از گالی *werēdos) از راه یونانی بیزانسی βερέδος می‌داند و «برید» فارسی وام‌گیری دوبارهٔ آن از عربی است — یعنی درست خلافِ جهتی که نورایی رسم کرده. یادداشت خودِ نورایی دو اردوگاه را منصفانه گزارش می‌کند، اما نیمهٔ دوم آن نادرست است (بنگرید به ref_check دربارهٔ AKD).\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%A8%D8%B1%D9%8A%D8%AF\",\n            \"https://www.etymonline.com/word/caviar\",\n            \"https://en.wiktionary.org/wiki/%D8%AE%D8%A7%D9%88%DB%8C%D8%A7%D8%B1\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"POK:128\", \"status\": \"supports\", \"note\": \"Pokorny's bher-1 material covers the Iranian verb (av. baraiti, ap. barantiy) from which بردن/بار descend; it says nothing about barīd or xāviyār.\"},\n            {\"ref\": \"BQT\", \"status\": \"not_checked\", \"note\": \"Nourai gives no page for BQT here. The neighbouring page BQT:253 (checked at node #2, = BQT_v1_pages.txt leaf 473) does carry برخوردار/برد.\"},\n            {\"ref\": \"AEF:208,212\", \"status\": \"not_checked\", \"note\": \"Khaleqi Motlaq's Asās-e Eshteqāq-e Fārsi (the Persian version of Horn+Hübschmann) is print-only; refs_online.json records no scan. The underlying Horn material was checked directly instead (HRN nos. 306 and 1073).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"MacKenzie s.vv. burdan, ³bār, bārag\", \"stance\": \"supports\", \"note\": \"'bārag [b'lk' | N ~a] mount, horse' — the direct ancestor of باره; and the English index 'mount bārag, stōr'.\"},\n            {\"src\": \"PLA\", \"where\": \"Asbaghi p. 48 (PLA_pages.txt leaf 63)\", \"stance\": \"supports\", \"note\": \"Running head 'barwāna 48 bazādara'; entry: 'barīd: \\\"Post, Bote\\\" pers., aus dem pers. burdan \\\"tragen\\\", mp. burtan / ap. bar >> verēdus'. Asbaghi does derive it from Persian burdan and even makes Latin verēdus the borrower.\"},\n            {\"src\": \"AKD\", \"where\": \"Zimmern p. 50 (AKD.txt leaf 60, the page number '50' is printed at the head of the passage)\", \"stance\": \"contradicts\", \"note\": \"'akk. purīdu, pirīdu eig. \\\"Eiler\\\", daher sowohl \\\"Bein\\\", als \\\"Eilbote\\\" : > viell. arab.-pers. barīd Eilbote, Eilpferd (> viell. lat. veredus (spätgriech. βερέδος) Eilpferd, bezw. aus paraveredus, deutsch Pferd); falls nicht umgekehrt hier das Arab.-Pers. < Griech.-Lat. < Gall.).' Zimmern derives barīd from AKKADIAN and makes Latin veredus the possible borrower; he only admits the reverse route as an alternative. Nourai's note, which says 'BQT, MON and AKD:50 claim it is from Latin veredus', misreports AKD.\"},\n            {\"src\": \"AFM\", \"where\": \"Addi Shir p. 18 (AFM_pages.txt leaf 20, the page with البربط، البرجاس، البرخداة، البريد)\", \"stance\": \"supports\", \"note\": \"'( البريد ) قيل أصله … وقيل أصله … وهو دابّة …' — Addi Shir lists al-barīd among the Persian words arabicized, as Nourai's note reports; the OCR of this Arabic/Syriac page is too broken to quote the full sentence, but the headword is on the cited page.\"},\n            {\"src\": \"Wiktionary\", \"where\": \"s.v. بريد (Arabic)\", \"stance\": \"contradicts\", \"note\": \"'from Byzantine Greek βέρηδος, from Latin verēdus, from Gaulish *werēdos'; the Persian derivation (from بریده 'docked', of Darius' horses) is listed as a folk etymology 'refuted' by Ullmann 1997 and Quatremère 1845; Zimmern's Akkadian proposal is called speculative.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Avestan\",\n          \"words\": \"aspa-bâra; xar-bâra; gâtu-bâra; gaoša-vare; duš-vare; pari-bhar, pari-bar\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"The morphology Nourai is pointing at is right — Old Iranian *-bara- 'carrying' as a compound second member, which becomes Persian -vār/-vāre/-var/-ūr — but most of the six forms are not attested Avestan words. Checked in Bartholomae: there is no aspa.bāra-, xara.bāra-, gātu.bāra-, gaoša.bara- or duš.bara-; what is there is gaošō.barəz- 'Höhe des Ohrs' and gaδa-vara- 'club-bearing' (MacKenzie's gadwar = Av. gaδawara-), which does prove that -vara- compounds are genuinely Avestan. aspa-bāra is in fact OLD PERSIAN asabāra- 'horseman' (Kent, Lexicon; DB II 98 asabāraibiš; uvasabāra- DNb 42), a vrddhi formation on *(H)acwa-bāra- 'horse-borne'. xar-bāra and gātu-bāra are Middle/New Persian formations (xarwār 'ass-load', MP gāhwārag 'cradle'), not Avestan. Only pari-bar- is directly Avestan: Bartholomae has pairi.barāmaide (Yt. 11.3, 17). Horn no. 306 gives the etymology Nourai wants ('perwerden \\\"ernähren, erziehen\\\", pari + √bhar-; phlv. parwardan'), and Horn no. 1073 states the whole rule: '-vār, -vāre, -ver (-ūr), Suffix \\\"tragend, versehen mit\\\"; ap. -bara- in taka-bara-; aw. gaδa-vara-; phlv. -bar in dātbar (neben dātwar), dastbar, mizdbar'. So: right root, right suffix, wrong language label on four of the six citation forms.\",\n          \"derivation_fa\": \"آنچه نورایی نشان می‌دهد از نظر ساخت‌واژی درست است — جزء دوم *-bara- «برنده» در ایرانی باستان که در فارسی به ـوار / ـواره / ـور بدل شده — اما بیشتر این شش صورت واژهٔ اوستایی ثبت‌شده نیستند. در بارتولومه نه aspa.bāra- هست نه xara.bāra- نه gātu.bāra- نه gaoša.bara- و نه duš.bara-؛ آنچه هست gaošō.barəz- «بلندی گوش» و gaδa-vara- «گرزدار» است (همان gadwar در مکنزی)، که دست‌کم نشان می‌دهد ترکیب‌های ـvara- در اوستایی واقعی‌اند. صورت aspa-bāra در حقیقت پارسی باستان asabāra- «سوارکار» است (کنت، فرهنگ؛ بیستون ستون ۲ سطر ۹۸ asabāraibiš و uvasabāra- در DNb ۴۲). صورت‌های xar-bāra و gātu-bāra ساخت‌های فارسی میانه و نو هستند (خروار، gāhwārag «گهواره»). تنها pari-bar- مستقیماً اوستایی است: بارتولومه pairi.barāmaide را از یشت ۱۱ می‌آورد. هرن در بند ۳۰۶ همان ریشه‌شناسی مورد نظر نورایی را می‌دهد («پروردن» = pari + √bhar-، پهلوی parwardan) و در بند ۱۰۷۳ قاعدهٔ کلی را: «ـوار، ـواره، ـور پسوندِ \\\"برنده، دارنده\\\"؛ پارسی باستان ـbara- در taka-bara-؛ اوستایی gaδa-vara-؛ پهلوی ـbar در dātbar (کنار dātwar)، dastbar، mizdbar». پس ریشه و پسوند درست‌اند ولی برچسب «اوستایی» بر چهار صورت از شش صورت نادرست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%D8%B3%D9%88%D8%A7%D8%B1\"],\n          \"ref_check\": [\n            {\"ref\": \"HRN:68\", \"status\": \"supports\", \"note\": \"Horn, Grundriss p. 68 (HRN.txt leaf 89), no. 306: 'perwerden \\\"ernähren, erziehen\\\", perweriš, perwerden, pari + √bhar-; phlv. parwardan, parwar(i)šn.' Exactly Nourai's pari-bhar/pari-bar.\"},\n            {\"ref\": \"HRN:240\", \"status\": \"supports\", \"note\": \"Horn p. 240 (leaf 262), no. 1073: '-vār, -vāre, -ver (-ūr), Suffix \\\"tragend, versehen mit\\\". ap. -bara- in taka-bara- \\\"tragend\\\"; aw. gaδa-vara-; phlv. -bar in dātbar (neben dātwar), dastbar, m(i)zdbar, -war, war in nmētwār, ōjwar, ranjwar; arm. -ber…' with the footnote 'in mizdūr Šāhn. VI,152 v.330, ganjūr, ranjūr u. a. m.' — the exact rule the two Persian daughter boxes need.\"},\n            {\"ref\": \"FFD:42\", \"status\": \"supports\", \"note\": \"Abolghasemi, Fe'l-hā-ye Fārsi-ye Dari p. 42 (FFD_pages.txt pdf page 47), s.v. پروردن: 'پرورد < فارسی میانه parwar(d) < ایرانی باستان *pari-bṛ-ta … pari پیشوند فعلی است. ريشهٔ bar به معنی «حمل کردن» است. «آوردن» و «بردن» هم از ريشهٔ bar آمده‌اند.'\"},\n            {\"ref\": \"BQT:821, 1773, 1858, 2245\", \"status\": \"not_checked\", \"note\": \"p. 821 is in BQT vol. 2 (leaf ≈ 278) and pp. 1773/1858/2245 in vols 3-4, which exist only as low-quality scans; refs_online.json's ref_page.py reports no OCR coverage for these and the Persian OCR of vols 1-2 is too corrupt to locate footnotes reliably. Not checked.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"grep for aspa.bāra / xara.bāra / gātu.bara / gaoša.bara / duš.bara in BRT.txt; found gaošō.barəz- (col. ~1090?, line 9895), gaδa-vara-, pairi.barāmaide (lines 2541, 16856)\", \"stance\": \"partial\", \"note\": \"None of the five nominal compounds Nourai prints as Avestan is in Bartholomae. What is there is 'j. gaošō.barəz- f. \\\"Höhe des Ohrs\\\"' and the verb form 'pairi.barāmaide' (Yt. 11.3, 17) — so only pari-bar- is Avestan as drawn.\"},\n            {\"src\": \"KNT\", \"where\": \"Kent, Old Persian, §126 and Lexicon s.v. uvasabāra- (KNT.txt lines 1788, 3586, 5215)\", \"stance\": \"supports\", \"note\": \"OP asabāra- 'horseman' is attested (DB II 98 'hadā kamnaibiš asabāraibiš'), and Kent analyses uvasabāra- as 'u- good + asabāra- horseman'. So aspa-bāra is real, but Old Persian, not Avestan.\"},\n            {\"src\": \"PHD\", \"where\": \"MacKenzie s.vv. gāhwārag, gadwar, bārag\", \"stance\": \"supports\", \"note\": \"'gāhwārag [g'shwlk' | N gāhwāra] cot, cradle' (= Nourai's gâtu-bâra 'bed carrier') and 'gadwar [gtwl = Av. gaδawara-] bearing a club' — the -war/-wārag element in Middle Persian.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Persian\",\n          \"words\": \"«گهواره ، خروار ، سوار ، ـوار ۱»; «امیدوار ، دشوار ، گوشواره»; «پروردگار ، پرورش ، پروردن»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"All nine items are formations in the suffix -vār/-vāre/-var < Old Iranian *-bara- 'carrying' (Horn no. 1073). گهواره gahvāre 'cradle' < MP gāhwārag = gāh 'place, bed' + -wārag 'carrier'. خروار xarvār 'ass-load, a unit of weight' = xar 'donkey' + bār. سوار savār 'rider' < MP aswār < OP asabāra- < PIr *Hacwa-bāra- 'horse-borne', with the regular MP loss of initial a- and NP s(a)w- from asw-. ـوار ۱ is the productive suffix itself. امیدوار omīdvār 'hopeful' = omīd + -vār 'bearing hope' (Horn's phlv. type nmētwār). دشوار došvār 'difficult' < MP dušwār = duš- 'ill-' + -wār, literally 'hard to carry' — Nourai's Avestan duš-vare. گوشواره gušvāre 'earring' = gōš 'ear' + -wāre, literally 'ear-borne'. پروردن parvardan / پرورش parvareš / پروردگار parvardegār all continue MP parwardan < OIr *pari-bar- 'to carry around, tend, rear' (Abolghasemi p. 42; Horn no. 306), with parvardegār 'the Nourisher, God' the agent noun in -gār.\",\n          \"derivation_fa\": \"هر نُه واژه ساخته‌شده با پسوند ـوار/ـواره/ـور از *-bara- ایرانی باستان «برنده» هستند (هرن، بند ۱۰۷۳). «گهواره» از gāhwārag فارسی میانه یعنی gāh «جای، بستر» + wārag «برنده». «خروار» = خر + بار، یکای وزن. «سوار» از aswār فارسی میانه از asabāra- پارسی باستان از *Hacwa-bāra- «اسب‌برده»، با افتادن قاعده‌مندِ a- آغازی در فارسی میانه و تبدیل asw- به sav- در فارسی نو. «ـوار ۱» خودِ پسوند است. «امیدوار» = امید + ـوار «امیددارنده» (از گونهٔ nmētwār پهلوی نزد هرن). «دشوار» از dušwār فارسی میانه: duš- «بد» + ـوار، تحت‌اللفظ «سخت‌بردنی» — همان duš-vare نورایی. «گوشواره» = گوش + ـواره «آویختهٔ گوش». «پروردن، پرورش، پروردگار» همه دنبالهٔ parwardan فارسی میانه از *pari-bar- ایرانی باستان «پیرامون بردن، پروریدن» هستند (ابوالقاسمی ص ۴۲؛ هرن بند ۳۰۶) و «پروردگار» اسم فاعل با ـگار است. ادعای نورایی درست است.\",\n          \"sources\": [\"https://en.wiktionary.org/wiki/%D8%B3%D9%88%D8%A7%D8%B1\"],\n          \"ref_check\": [\n            {\"ref\": \"SNS:133\", \"status\": \"not_found\", \"note\": \"Tavoosi's Shāyast nē Shāyast glossary: grepped SNS.txt/SNS_pages.txt for aswār, asvār, -wār, parwardan, gōšwārag — no hits. refs_online.json records that the page offset for this scan could not be determined (OCR too poor to read the printed numerals), so I could not confirm what stands on printed p. 133.\"},\n            {\"ref\": \"BQT\", \"status\": \"not_checked\", \"note\": \"No page number is given for BQT in this box.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"HRN\", \"where\": \"no. 1073, p. 240\", \"stance\": \"supports\", \"note\": \"'-vār, -vāre, -ver (-ūr), Suffix \\\"tragend, versehen mit\\\" … phlv. -war, war in nmētwār, ōjwar, ranjwar' — the suffix of امیدوار/دشوار/گوشواره, derived from ap. -bara-.\"},\n            {\"src\": \"PHD\", \"where\": \"MacKenzie s.v. gāhwārag\", \"stance\": \"supports\", \"note\": \"'gāhwārag [g'shwlk' | N gāhwāra] cot, cradle' — the direct MP ancestor of گهواره, with the -wārag element.\"},\n            {\"src\": \"FFD\", \"where\": \"Abolghasemi p. 42 (pdf 47), s.v. پروردن\", \"stance\": \"supports\", \"note\": \"'پرورد < فارسی میانه parwar(d) < ایرانی باستان *pari-bṛ… ريشهٔ bar به معنی «حمل کردن» است' — پروردن/پرورش/پروردگار.\"},\n            {\"src\": \"Wiktionary\", \"where\": \"s.v. سوار (Persian)\", \"stance\": \"supports\", \"note\": \"'Middle Persian ʾswbʾl / aswār \\\"horseman, rider\\\", Old Persian 𐎠𐎿𐎲𐎠𐎼 asabāra- \\\"horseman\\\", from Proto-Iranian *Hacwabāráh' — exactly the aspa-bāra > سوار arrow.\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"Avestan\",\n          \"words\": \"â-vare, â-bar-a; mîžda-vare; dâtô-vare; hvare-varân\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Same picture as node #4: the *bar- element is right, the 'Avestan' label is loose. (a) ā-bar- 'to bring' is genuine Old Iranian: Abolghasemi p. 28 s.v. آوردن gives 'āwurd < MP āwurd < Old Iranian *ā-bṛ-ta … the root bar means \\\"to carry\\\", and with the preverb ā \\\"to carry towards the speaker\\\"'. (b) mīžda-vare is not attested in Avestan (Bartholomae has mīžda- n. 'Lohn' and the adjectives mīžda-vant-, ašō.mīžda-, hu-mīžda-, but no *mīžda.bara-); the actual word is Middle Persian mizdwar 'hireling' (MacKenzie), whence مزدور. (c) dātō-vare is likewise not Avestan — Bartholomae has dātō.baēšaza- '(a physician) who heals with the law' but no *dātō.bara-; the real word is MP dādwar 'judge' (MacKenzie: 'dādwar [d'twbl | M dādwar, P dādbar, N dā(d)war] judge'), whence داور. (d) hvare-varān is not Avestan at all but Middle Persian xwarbarān 'west', literally 'where the sun is carried (away)', the counterpart of xwarāsān 'sunrise, east' (MacKenzie s.v. xwarāsān). So the derivations are sound as Iranian etymologies; only three of the four headwords belong to a later stage than the box claims.\",\n          \"derivation_fa\": \"وضع همانند گرهٔ ۴ است: جزء *bar- درست است ولی برچسب «اوستایی» دقیق نیست. الف) ā-bar- «آوردن» به‌راستی ایرانی باستان است: ابوالقاسمی (ص ۲۸، ذیل آوردن) می‌نویسد «آورد < فارسی میانه āwurd < ایرانی باستان *ā-bṛ-ta … ريشهٔ bar به معنی «حمل کردن» است و با پیشوند فعلی ā: «حمل کردن به سوی متکلم»». ب) mīžda-vare در اوستایی ثبت نشده؛ بارتولومه mīžda- «مزد» و صفت‌های mīžda-vant-، ašō.mīžda-، hu-mīžda- را دارد ولی *mīžda.bara- را نه؛ صورت واقعی mizdwar فارسی میانه «مزدبگیر» است (مکنزی) که «مزدور» از آن است. ج) dātō-vare نیز اوستایی نیست — بارتولومه dātō.baēšaza- «پزشکی که با قانون درمان می‌کند» دارد نه *dātō.bara-؛ صورت واقعی dādwar پهلوی «داور» است (مکنزی: «dādwar … judge»). د) hvare-varān اصلاً اوستایی نیست بلکه xwarbarān فارسی میانه «مغرب» است، لفظاً «جایی که خورشید برده می‌شود»، در برابر xwarāsān «مشرق» (مکنزی). پس ریشه‌شناسی‌ها به‌عنوان ریشه‌شناسی ایرانی درست‌اند، ولی سه صورت از چهار صورت به لایهٔ زبانی متأخرتری از آنچه در کادر آمده تعلق دارند.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"FFD:28\", \"status\": \"supports\", \"note\": \"Abolghasemi p. 28 (FFD_pages.txt pdf page 33), s.v. آوردن: 'آورد < فارسی میانه āwurd < ایرانی باستان *ā-bṛ-ta … bar صورت ضعیف ريشهٔ bar به معنی «حمل کردن» است و با پیشوند فعلی ā: «حمل کردن به سوی متکلم» ← بردن.' Exactly Nourai's â-vare / â-bar-a 'bring'.\"},\n            {\"ref\": \"BQT:66\", \"status\": \"not_checked\", \"note\": \"BQT vol. 1 printed p. 66 ≈ BQT_v1_pages.txt leaf 276 (offset −210 near the start of the dictionary); the Persian OCR of vol. 1 is too corrupt to read Mo'in's etymological footnotes, and ref_page.py has no scan coverage for vol. 1.\"},\n            {\"ref\": \"MON:1395\", \"status\": \"not_checked\", \"note\": \"Mo'in vol. 2/3 p. 1395; the online vajehyab/abadis text of Mo'in is keyed by headword, not by page, and Nourai does not say which word he means, so the citation cannot be located.\"},\n            {\"ref\": \"DRM:292\", \"status\": \"not_checked\", \"note\": \"Darmesteter, Études iraniennes; refs_online.json notes Nourai does not say which tome, and DRM.txt would need the word he means. Not resolvable from the page reference alone.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"MacKenzie s.vv. dādwar, mizdwar (English index 'hireling mizdwar'), xwarāsān, dastwar\", \"stance\": \"supports\", \"note\": \"'dādwar [d'twbl | (M dādwar, P dādbar), N dā(d)war] judge. ~ih: judgement'; 'hireling mizdwar'; 'xwarāsān [hwl's'n' | M xwarāsān, N ~] sunrise, east' — the -war compounds are Middle Persian, and xwarāsān presupposes the xwarbarān of Nourai's hvare-varân.\"},\n            {\"src\": \"BRT\", \"where\": \"s.vv. mīžda- (line 20563), mīžda-vant- (20570), ašō.mīžda- (6412), dātō.baēšaza- (13305)\", \"stance\": \"partial\", \"note\": \"'j., g. mižda- n. \\\"Lohn\\\"' and 'j. dātō.baēšaza- Adj. \\\"(Arzt,) der mit dem Gesetz heilt\\\"' are attested, but there is no *mīžda.bara- or *dātō.bara- in Bartholomae — the compounds Nourai labels Avestan are not.\"},\n            {\"src\": \"FSF\", \"where\": \"Noushin, Vāzhe-nāmak, leaf 74 (printed p. ~58), s.v. باختر\", \"stance\": \"supports\", \"note\": \"'نام‌های جهات چهارگانه به زبان پهلوی چنین است: خوراسان [خراسان] مشرق، خوروران [خاوران، خاور] مغرب، باختر شمال و نیمروز جنوب. «خوربران» پهلوی: xwarbarān [مغرب]' — i.e. Nourai's hvare-varân is the Pahlavi xwarbarān.\"}\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"Persian\",\n          \"words\": \"«رنجور ، دستور ، داور ، مزدور ، آوردن ، جانور ، گنجور ، جنگاور ، پیامبر ، خاور»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"All ten are -var/-ūr/-bar compounds on *bar- 'to carry'. آوردن āvardan < MP āwurdan < *ā-bar- 'bring' (Abolghasemi p. 28). داور dāvar < MP dādwar 'judge' = dād 'law' + -war, exactly Nourai's dātō-vare. مزدور mozdūr < MP mizdwar 'hireling' = muzd 'wage' + -war; گنجور ganjūr 'treasurer' < MP ganjwar; رنجور ranjūr 'sick, suffering' < ranj + -ūr — Horn no. 1073 names precisely this trio ('in mizdūr Šāhn. VI,152 v.330, ganjūr, ranjūr u. a. m.') and derives the -ūr from *-bara-. دستور dastūr < MP dastwar 'authority, priest, minister' = dast 'hand' + -war (MacKenzie), which is why Nourai's note sends the reader to 'Dhě 2'; both MacKenzie and Horn put dastwar with dātbar/dātwar, so the note's cross-reference is sound. جانور jānvar 'living creature' = jān 'soul' + -var 'bearing'; جنگاور jangāvar 'warrior' = jang + -āvar (the ā-bar- variant); پیامبر payām-bar 'message-bearer, prophet' = payām + bar. خاور xāvar < MP xwarbarān 'where the sun is carried off', i.e. WEST in classical Persian — Noushin's Shahnameh glossary gives 'خوروران [خاوران، خاور] مغرب' and quotes the very Rūdakī couplet Nourai prints ('مهر دیدم بامدادان چون بتافت / از خراسان سوی خاور می‌شتافت'), where خراسان = east and خاور = west; in modern Persian the sense has been reversed to 'east' by analogy with باختر.\",\n          \"derivation_fa\": \"هر ده واژه ترکیب‌های ـور/ـاور/ـبر بر ستاک *bar- «بردن» هستند. «آوردن» از āwurdan فارسی میانه از *ā-bar- (ابوالقاسمی ص ۲۸). «داور» از dādwar پهلوی «قاضی» = داد + ـور، همان dātō-vare نورایی. «مزدور» از mizdwar پهلوی، «گنجور» از ganjwar، «رنجور» از رنج + ـور — هرن در بند ۱۰۷۳ دقیقاً همین سه واژه را نام می‌برد و ـور را از *-bara- می‌گیرد. «دستور» از dastwar پهلوی «صاحب‌اختیار، موبد، وزیر» = دست + ـور (مکنزی)، و همین است که نورایی خواننده را به مدخل «Dhě 2» ارجاع می‌دهد؛ هم مکنزی و هم هرن dastwar را کنار dātbar/dātwar می‌نشانند، پس ارجاع درست است. «جانور» = جان + ـور؛ «جنگاور» = جنگ + ـاور (گونهٔ ā-bar-)؛ «پیامبر» = پیام + بر. «خاور» از xwarbarān پهلوی «جایی که خورشید برده می‌شود»، یعنی در فارسی کلاسیک «مغرب» — نوشین در واژه‌نامک می‌نویسد «خوروران [خاوران، خاور] مغرب» و همان بیت رودکی را می‌آورد که نورایی نقل کرده و در آن خراسان = مشرق و خاور = مغرب است؛ در فارسی امروز این معنی به قیاسِ «باختر» وارونه شده و «خاور» را «مشرق» می‌گیرند. ادعای نورایی درست است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\"ref\": \"FSF:58\", \"status\": \"supports\", \"note\": \"Noushin, Vāzhe-nāmak (Farhang-e Shāhnāme), leaf 74 of FSF_pages.txt (printed p. ≈58, the running head numeral is OCR'd as '۷.'), s.v. باختر: 'نام‌های جهات چهارگانه به زبان پهلوی چنین است: خوراسان [خراسان] مشرق، خوروران [خاوران، خاور] مغرب … «خوربران» پهلوی xwarbarān [مغرب]' and 'رودکی خراسان را به معنی مشرق … و خاور را به‌معنی مغرب بکار می‌برد. (نفیسی بیت ۹۲۸): مهر دیدم بامدادان چون بتافت / از خراسان سوی خاور می‌شتافت' — the exact couplet Nourai quotes with the exact sense.\"},\n            {\"ref\": \"BQT\", \"status\": \"not_checked\", \"note\": \"No page number given for BQT in this box.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"MacKenzie s.vv. dādwar, dastwar, ganjwar, mizdwar\", \"stance\": \"supports\", \"note\": \"'dastwar [dstwbl | M dastwar, N dastūr] authority, priest, minister'; 'dādwar … judge'; 'treasurer gahbed, ganjwar'; 'hireling mizdwar' — the Middle Persian ancestors of دستور، داور، گنجور، مزدور.\"},\n            {\"src\": \"HRN\", \"where\": \"no. 1073, p. 240 and its footnote\", \"stance\": \"supports\", \"note\": \"'-vār, -vāre, -ver (-ūr), Suffix \\\"tragend\\\"… phlv. -bar in dātbar (neben dātwar), dastbar, m(i)zdbar' + footnote 'in mizdūr Šāhn. VI,152 Vers 330, ganjūr, renjūr u. a. m.' — Horn derives دستور، داور، مزدور، گنجور، رنجور from *-bara- exactly as the chart does.\"},\n            {\"src\": \"FFD\", \"where\": \"Abolghasemi p. 28, s.v. آوردن\", \"stance\": \"supports\", \"note\": \"'آورد < فارسی میانه āwurd < ایرانی باستان *ā-bṛ-ta … با پیشوند فعلی ā' — آوردن on this root.\"}\n          ]\n        }\n      ]\n    }\n  ]\n}\nJSONEOF\npython3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-88.json > /dev/null && echo \"JSON OK\"",
 "description": "Write page-88 verification JSON"
}
```


### [2026-09-05T14:05:00.148Z] TOOL RESULT

```
JSON OK
```


## [2026-09-05T14:05:06.064Z] TOOL CALL #77: Bash

```json
{
 "command": "python3 - <<'PY'\nimport io\np='data/verification/page-88.json'\ns=io.open(p,encoding='utf-8').read()\ns=s.replace(\"material列 lists\",\"material section lists\")\nio.open(p,'w',encoding='utf-8').write(s)\nPY\ngrep -c \"material列\" data/verification/page-88.json; python3 tools/verify_check.py 88",
 "description": "Fix stray char and run verify_check"
}
```


### [2026-09-05T14:05:08.271Z] TOOL RESULT

```
0
nodes verified: 12/12
node verdicts: {'confirmed': 6, 'disputed': 3, 'transcription_suspect': 1, 'plausible': 2}
root verdicts: {'confirmed': 1, 'plausible': 1}
ref checks: {'supports': 11, 'not_found': 2, 'partial': 2, 'not_checked': 8}
books consulted: {'supports': 26, 'silent': 3, 'contradicts': 5, 'partial': 4} | by book: {'PHD': 6, 'BRT': 4, 'WLD': 3, 'HRN': 3, 'POK': 3, 'KLN': 2, 'KNT': 2, 'NYB': 2, 'Wiktionary': 2, 'FFD': 2, 'AHD': 1, 'BQT/MON via web': 1, 'SOD': 1, 'SKT': 1, 'Etymonline': 1, 'PLA': 1, 'AKD': 1, 'AFM': 1, 'FSF': 1}
```


## [2026-09-05T14:05:28.305Z] AGENT

Done. `python3 tools/verify_check.py 88` → **0 PROBLEM lines**, 12/12 nodes verified.

**Page 88 (book p. 58) — verdicts**
- Roots: 1 confirmed (Bhengh), 1 plausible (Bher 1 / Bhrâ-tar)
- Nodes: 6 confirmed, 2 plausible, 3 disputed, 1 transcription_suspect
- Ref checks: 11 supports · 2 partial · 2 not_found · 8 not_checked · 34 `consulted` entries across 19 books

**Disputed / flagged**
- *Bhengh* #2 Persian `bâz` "distance between stretched hands" — Horn no. 167 (p. 38) and Pokorny 108 put باز/بازه under **bāzū 'arm'** (*bʰeh₂ǵʰu-, Av. bāzu-), a root Pokorny keeps separate from *bʰenǵʰ-. MON:452 supports only the gloss, not the derivation.
- *Bher 1* #2 Pahlavi `xâyak-bâr` — unattested; MacKenzie/Nyberg have no such compound. Second element is **dār 'bearing'** (Etymonline), or Szemerényi's *kæf+jaro* (Wiktionary).
- *Bher 1* #3 Persian `barîd` — modern consensus: Lat. *verēdus* → Byz. Gk. βερέδος → Ar. بريد → NP; the Persian-burdan route is the folk etymology. Also: Nourai's own NOTE **misreports AKD:50** — Zimmern (verified, p. 50) derives *barīd* from Akkadian *purīdu* and makes Latin *veredus* the borrower, not the source. PLA:48 and AFM:18 check out as described.
- *Bhengh* #4 Greek `paxus : "tick"` — **book misprint** for "thick" (`error_in: "book"`); the 400-dpi page render shows "tick" on the printed page, so extraction is faithful. Page PNG saved to `data/verification/sources/refs/ocr/BOOK/88.png`.
- Nodes #4/#6 of Bher 1 marked *plausible*: the *-bara-* > Persian -vār/-ūr rule is right (Horn no. 1073, verified verbatim), but `aspa-bâra` is Old Persian *asabāra-*, and `gâtu-bâra`/`mîžda-vare`/`dâtô-vare`/`hvare-varân` are Middle Persian (gāhwārag, mizdwar, dādwar, xwarbarān) — none attested in Bartholomae as Avestan.

**Extraction error for the owner to fix** (`data/extracted/batch/page-88.json`): in entry 1, nodes **#4 and #6 have `"parent": 0` but should be `"parent": 1`**. On the printed page the vertical connector feeding the Pahlavi box and both lower Avestan boxes springs from the bottom edge of the "Avestan / Old Persian" box (confirmed on a 400-dpi crop, same convention as the root spine in entry 0).

7 web pages archived via `fetch_source.py`; no other data changes.
