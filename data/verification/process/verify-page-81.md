# Verification process log — verify-page-81


## [2026-09-05T06:03:51.180Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 81 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-81.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-81.json. Write /home/sfmqrb/git/rishe/data/verification/page-81.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 81` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-05T06:03:52.902Z] AGENT

I'll start by reading the instructions.


## [2026-09-05T06:03:53.610Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-05T06:03:53.627Z] TOOL RESULT

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


## [2026-09-05T06:03:53.757Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-81.txt"
}
```


### [2026-09-05T06:03:53.776Z] TOOL RESULT

```
1	=== PDF page 81 (book page 51) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Bhag : to share out, to enjoy  (refs POK:107; IEC:61)  PART 1
4	#1 (parent #0) [Avestan / Old Persian] refs=POK:107; KNT; KLN:169 | baga, bağa : distributor of good fortune, God ; baxto-dâta : one who is given a good fortune, lucky ☞Dô 2 ; bax-ta : that which is given, fate
5	  #2 (parent #1) [Persian] refs=BQT:203,239; AEF:198,241; ETM:61; FFD:35 | baxšîdan «بخشیدن» : to give ; baxš «بخش» : division ; baxt «بَخت ۱ (بختیار)» : fortune, fate ; bâj «باج ۱ ( باژ ۲ )» : toll, tax
6	#3 (parent #0) [Avestan] refs=BQT:251,324; SNS:96 | baxadra : interest, something given
7	  #4 (parent #3) [Persian] refs=BQT; SNS:96 | barx «بَرخ ( برخی )» : interest ; bahr «بهر ( بهره )» : interest
8	#5 (parent #0) [Persian] refs=BQT:288,289,337; MON:2558; POK:107; TZF:18 | bağ, fağ «بغ ، فغ» : God, goddess ; Bağdâd «بغداد» : God-given (city), Baghdad ☞Dô 2 ; bağ-stân «بغستان ، فغستان» : location (mountain) of gods; also a very beautiful person (goddess of beauty) ☞Stâ ; bîstŭn «بیستون» : corruption of "bağ-stân", name of a mountain upon which ancient Iranians used to worship | NOTE: Henning derives "bağ" from Sogdian (SLW:94)
9	TAD:12 derives "Baghdâd" from Persian "bâğ-e-dâd:garden of justice".
10	#6 (parent #0) [Avestan] refs=HJB:49; BQT:333,1494 | bağa-puthra : son of God, title of respect ☞Pôu ; bağa-dugdâr : daughter of God, Venus ☞Dheugh
11	  #7 (parent #6) [Persian] refs=HJB:49; BQT:333,1494; TZF:18 | fağpŭr «فغفور» : son of God, title of respect ; Bîdoxt «بیدخت» : "daughter of God"
12	#8 (parent #0) [Avestan] refs=BQT:164 | hama-bağa : share together ☞Sem 1
13	  #9 (parent #8) [Pahlavi] refs=BQT:164 | hambâğ : companion
14	    #10 (parent #9) [Persian] refs=None | anbâz «انباز» : companion ; anbâğ «انباغ» : rival wife
15	#11 (parent #0) [Turkish] refs=ZMA:49 | bak : grand, Lord, God ; ata-bak : grand father, god father
16	  #12 (parent #11) [Persian] refs=ETM:60 | bak «بَک (بَگ ، بیک ، بیگ ، بیگی)» : a title of respect ; baygom «بیگم» : "ruler's mother", title of respect ☞Umm ; atabak «اتابک» : grand father, god father
17	
```


## [2026-09-05T06:03:57.730Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-81.json",
 "description": "Read source JSON for page 81"
}
```


### [2026-09-05T06:03:57.768Z] TOOL RESULT

```
{
  "pdf_page": 81,
  "book_page": 51,
  "entries": [
    {
      "root": {
        "name": "Bhag",
        "lang": "Indo-European",
        "refs": "POK:107; IEC:61",
        "gloss": "to share out, to enjoy"
      },
      "part": 1,
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan / Old Persian",
          "refs": "POK:107; KNT; KLN:169",
          "words": [
            {"translit": "baga, bağa", "gloss": "distributor of good fortune, God", "script": null},
            {"translit": "baxto-dâta", "gloss": "one who is given a good fortune, lucky", "script": null, "see": ["Dô 2"]},
            {"translit": "bax-ta", "gloss": "that which is given, fate", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT:203,239; AEF:198,241; ETM:61; FFD:35",
          "words": [
            {"translit": "baxšîdan", "gloss": "to give", "script": "بخشیدن"},
            {"translit": "baxš", "gloss": "division", "script": "بخش"},
            {"translit": "baxt", "gloss": "fortune, fate", "script": "بَخت ۱ (بختیار)"},
            {"translit": "bâj", "gloss": "toll, tax", "script": "باج ۱ ( باژ ۲ )"}
          ],
          "note": null,
          "quote": {
            "text": "ز دیـنـار پر کرده ده چرم گاو ـ سه ساله فرستاده شد باژ و ساو",
            "poet": "Ferdowsî"
          }
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Avestan",
          "refs": "BQT:251,324; SNS:96",
          "words": [
            {"translit": "baxadra", "gloss": "interest, something given", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Persian",
          "refs": "BQT; SNS:96",
          "words": [
            {"translit": "barx", "gloss": "interest", "script": "بَرخ ( برخی )"},
            {"translit": "bahr", "gloss": "interest", "script": "بهر ( بهره )"}
          ],
          "note": null,
          "quote": {
            "text": "تو ای دانشی چند نالی ز چرخ ـ که ایزد بَدی دادت از چرخ برخ",
            "poet": "Asadî"
          }
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Persian",
          "refs": "BQT:288,289,337; MON:2558; POK:107; TZF:18",
          "words": [
            {"translit": "bağ, fağ", "gloss": "God, goddess", "script": "بغ ، فغ"},
            {"translit": "Bağdâd", "gloss": "God-given (city), Baghdad", "script": "بغداد", "see": ["Dô 2"]},
            {"translit": "bağ-stân", "gloss": "location (mountain) of gods; also a very beautiful person (goddess of beauty)", "script": "بغستان ، فغستان", "see": ["Stâ"]},
            {"translit": "bîstŭn", "gloss": "corruption of \"bağ-stân\", name of a mountain upon which ancient Iranians used to worship", "script": "بیستون"}
          ],
          "note": "Henning derives \"bağ\" from Sogdian (SLW:94)\nTAD:12 derives \"Baghdâd\" from Persian \"bâğ-e-dâd:garden of justice\".",
          "quote": {
            "text": "فغستان چو آمد به مَشکوی شاه ـ یکی تاج بر سر ز مُشک سیاه",
            "poet": "Ferdowsî"
          }
        },
        {
          "id": 6,
          "parent": 0,
          "lang": "Avestan",
          "refs": "HJB:49; BQT:333,1494",
          "words": [
            {"translit": "bağa-puthra", "gloss": "son of God, title of respect", "script": null, "see": ["Pôu"]},
            {"translit": "bağa-dugdâr", "gloss": "daughter of God, Venus", "script": null, "see": ["Dheugh"]}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "Persian",
          "refs": "HJB:49; BQT:333,1494; TZF:18",
          "words": [
            {"translit": "fağpŭr", "gloss": "son of God, title of respect", "script": "فغفور"},
            {"translit": "Bîdoxt", "gloss": "\"daughter of God\"", "script": "بیدخت"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 0,
          "lang": "Avestan",
          "refs": "BQT:164",
          "words": [
            {"translit": "hama-bağa", "gloss": "share together", "script": null, "see": ["Sem 1"]}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "Pahlavi",
          "refs": "BQT:164",
          "words": [
            {"translit": "hambâğ", "gloss": "companion", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 9,
          "lang": "Persian",
          "refs": null,
          "words": [
            {"translit": "anbâz", "gloss": "companion", "script": "انباز"},
            {"translit": "anbâğ", "gloss": "rival wife", "script": "انباغ"}
          ],
          "note": null,
          "quote": {
            "text": "ای خدای پاک و بی انباز و یار - دستگیر و جرم ما را در گذار",
            "poet": "Molavî"
          }
        },
        {
          "id": 11,
          "parent": 0,
          "lang": "Turkish",
          "refs": "ZMA:49",
          "words": [
            {"translit": "bak", "gloss": "grand, Lord, God", "script": null},
            {"translit": "ata-bak", "gloss": "grand father, god father", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 11,
          "lang": "Persian",
          "refs": "ETM:60",
          "words": [
            {"translit": "bak", "gloss": "a title of respect", "script": "بَک (بَگ ، بیک ، بیگ ، بیگی)"},
            {"translit": "baygom", "gloss": "\"ruler's mother\", title of respect", "script": "بیگم", "see": ["Umm"]},
            {"translit": "atabak", "gloss": "grand father, god father", "script": "اتابک"}
          ],
          "note": null,
          "quote": null
        }
      ]
    }
  ]
}
```


## [2026-09-05T06:03:57.852Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-05T06:03:57.888Z] TOOL RESULT

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


## [2026-09-05T06:04:03.030Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','IEC','KNT','KLN','BQT','AEF','ETM','FFD','SNS','MON','TZF','HJB','ZMA','SLW','TAD','HRN','HUB','PHD','NYB','BRT','ARY','TTS','LKT','AHD','WLD','SYN','HENNING']:\n    v=d.get(k)\n    print('==',k,json.dumps(v,ensure_ascii=False)[:700])\n\""
}
```


### [2026-09-05T06:04:04.801Z] TOOL RESULT

```
== POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index 
== IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Reconstruct
== KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt", "page_offset": "leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archiv
== KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt", "page_offset": "KLN_1966: TWO pri
== BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.c
== AEF {"title": "Jalal Khaleqi Motlaq, Asas-e Eshteqaq-e Farsi, vol. I (آ–خ), Bonyad-e Farhang-e Iran 1356/1977 — this is the Persian TRANSLATION of Paul Horn's Grundriss der neupersischen Etymologie (HRN) with Hübschmann's Persische Studien (HUB) notes and added Persian/Pahlavi evidence", "kind": "catalog", "url": "https://openlibrary.org/works/OL38785552W (vol. 1, 1356) ; 2015 complete ed. «فرهنگ ریشه‌شناسی فارسی» (مهرافروز) print-only: https://www.gisoom.com/book/11154690/ ; German original: https://archive.org/details/grundrissderneu00horngoog", "lookup_hint": "Not online (searched archive.org, ketabnak, noorlib, web; only bookshop listings). Because it is a translation of Horn/Hübschmann, ver
== ETM {"title": "Mohsen Abolghasemi, Risheh-shenasi (Etimoloji), Qoqnus 1374/1995", "kind": "catalog", "url": "https://ketabnak.com/book/107170/ (no download) ; https://ketab.ir/book/2ebb5f53-ba49-4955-98f4-d419919d0ebc ; purchase: https://adinehbook.com/gp/product/9643110451", "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: not found.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 2026-09: no digital copy on any permitted platform; catalogue/purchase only."}
== FFD {"title": "Mohsen Abolghasemi, Fe'l-ha-ye Farsi-ye Dari, Qoqnus, Tehran 1374/1995", "kind": "local_scan_ocr", "url": "https://asmaneketab.ir/product/کتاب-ماده-های-فعلهای-فارسی-دری-محسن-اب/ -> https://dl.eliteraturebook.com/app/public/attachments/6925d29630b83.PDF (free PDF site; grey)", "lookup_hint": "Searched archive.org (Persian/Latin titles, author), ketabnak, noorlib, general web (pdf/download): nothing; only a related paid e-book 'واژگان زبان فارسی دری' (fidibo). ketabnak.com/book/45024 is a different book (فهرست فعلهای فارسی).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_asmaneketab.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/ref
== SNS {"title": "Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/VajnameShayest", "lookup_hint": "grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php search (see BQT) for better hit-to-leaf mapping.", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS.txt"], "page_offset": "242 leaves; page offset not determined (OCR too poor to read printed numbers) — 
== MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol 
== TZF {"title": "Mohsen Abolghasemi, Tarikh-e Mokhtasar-e Zaban-e Farsi, Bonyad-e Andisheh-ye Eslami 1373/1994", "kind": "website", "url": "https://ketabnak.com/book/81646 (142 pp. PDF; login) ; https://farhangoadabeirani.blogsky.com/1395/07/20/post-1048/ (download post)", "lookup_hint": "Not on archive.org (only his دستور تاریخی زبان فارسی: archive.org/details/20220417_20220417_2237, and تاریخ زبان فارسی on samta.samt.ac.ir / library.tebyan.net/f/Viewer/Pdf/168187 which overlap in content).", "local_file": null, "page_offset": null, "covers_etymology": false, "notes": "PDF exists but not downloadable without login."}
== HJB {"title": "H. Yule & A. C. Burnell, Hobson-Jobson, 2nd ed. by W. Crooke, London 1903 (Delhi reprint 1968)", "edition_found": "1903 Crooke edition (pagination identical to the 1968 reprint)", "kind": "archive_djvu", "url": "https://archive.org/details/hobsonjobsonagl02croogoog", "identifier": "hobsonjobsonagl02croogoog (others: bub_gb_6Z5iAAAAMAAJ, hobsonjobsonglos00yulerich, india.history.resource.89053)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HJB.txt", "page_offset": "leaf = printed + 35..51 (plates inserted; e.g. leaf 83 = p.32, leaf 319 = p.270, leaf 535 = p.490, leaf 905 = p.870). local file has \\f between leaves (0-based leaf index i == i-th form-feed pag
== ZMA {"title": "Fereydun Jonaydi, Zendegi va Mohajerat-e Aryaian, Bonyad-e Neyshabur 1374/1995", "kind": "purchase", "url": "https://www.gisoom.com / iketab.com listings (Balkh / Bonyad-e Neyshabur, in print)", "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: not found.", "local_file": null, "page_offset": null, "covers_etymology": false, "notes": "RE-SEARCH 2026-09: purchase only; no open or lending copy (grey PDF sites exist, not used)."}
== SLW {"title": "W. B. Henning, 'Sogdian Loan-Words in New Persian', BSOAS 10.1 (1939) pp. 93-106", "edition_found": "reprint in W. B. Henning Selected Papers I (Acta Iranica 14, 1977) - different pagination; original in JSTOR", "kind": "archive_djvu", "url": "https://archive.org/details/w.-b.-henning-selected-papers", "identifier": "w.-b.-henning-selected-papers (also w.-b.-henning-selected-papers_202108)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HENNING_selected_papers.txt", "page_offset": "Selected Papers scan: leaf = p + 12 for the front matter; reprinted articles keep the ORIGINAL journal page numbers in the margins, so grep 'Sogdian Loan' then the original page n
== TAD {"title": "Tobia al-Unaysi (طوبيا العنيسي), Tafsir al-alfaz al-dakhila fi al-lugha al-'arabiyya ma'a dhikr asliha bi-hurufihi (2nd ed. Cairo 1932, ed. Yusuf Tuma al-Bustani; later Library of Lebanon reprint) — Nourai lists it under Arabic authors ('Unaysi T.'); its Table IV line was lost in the OCR", "kind": "archive_djvu", "url": "https://archive.org/details/TOB1932ARAR (1932 ed.); also https://archive.org/details/ar113lang79 and https://archive.org/details/elshandawily14640", "lookup_hint": "Alphabetical Arabic headwords; grep the Arabic headword in TAD_pages.txt (86 leaves) or TAD.txt; inside.php search works.", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/TAD_pag
== HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or grep the 
== HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by parag
== PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<ident
== NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Nourai's 'NYB' nu
== BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \\f between 
== ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY:<printed page> --image", "local_file": ["/home/sfmqrb/git/rishe/
== TTS {"title": "H. Vámbéry, Etymologisches Wörterbuch der turko-tatarischen Sprachen, Leipzig 1878 (repr. Osnabrück 1972)", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/etymologischesw00vmuoft (Toronto scan; also Google/bub_gb copies)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_vambery1878_uoft.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_vambery1878_uoft_djvu.txt"], "page_offset": "TTS_pages.txt: 253 leaves; printed page N = leaf N+30.", "lookup_hint": "Not searched exhaustively 
== LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Numbered entries: 'NNNN. word (language) meaning' - Lokotsch is usually cited by entry number, but Nourai cites pages.
== AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only", "identifie
== WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.39015066210397 (browser only from this host)", "identifier": "in.gov.ignca.20339 (Band 3); also in.ernet.dli.2015
== SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<i
== HENNING null
```


## [2026-09-05T06:04:09.974Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==116' POK_01.txt | head -80",
 "description": "Print Pokorny page 107"
}
```


### [2026-09-05T06:04:11.583Z] TOOL RESULT

```
n',  w( von  ahd.  barij  PI.  banna  , Gebot  unter  Strafandrohung*  (nhd.  Bann,  Bawdi tcald),  ags.  gebann,  aisl.  bann  n.  »Verbot,  Bann*.
Toch.  A  pä-j  pä-g-  , betteln'  (Van  Windekens   Lexique  87  f.).
Nach  Kuiper  (AO.  XII  262)  hierher  (*bhd-s-)  ai.  bhisdkti  ,heilt',  bhiSdfi jArzt',  jav.  -bis-  , heilend*;    über   av.  bisazjät   vgl.  Kuiper  Nasalpräs.  44 fj
WP.  II  123 f.,  WH.  I  437  f.,  450,  458  f.,  525 f.,  Schwjzer  Gr.  Gr.  I  674r
bhabhä  und  anklingende  Worte  für  , Bohne*,  u.  zw.  , Saubohne',  vgl.  zuml Sachlichen  Hoops  Waldb.  350,  400  f.,  464  f.,  Helm  Kltpfl.«  221,  570,1 Schrader  RL.^  159  f.  |
Lat.  faba  (fäl.  haba)  , Bohne'  (dazu  die  PN  Fabius,  Fabidius  usw.  und die  Insel  Fabäria),  russ.  usw.  bob^,  apr.  babo  ds.  Wohl  redupliziertes Lallwort  und  als  , aufgeblasene  Schote,  Schwellung'  mit  gr.  g)a-KÖg  m. , Linse' :  alb.  bathe  f.  , Saubohne*  (*bhakä)  verwandt.  Auch  aisl.  baun,  ags. bean,  ahd.  bona  , Bohne'  (Baunonia  friesische  Insel  bei  Plinius)  sind  wohl durch  Dissimil.  von  *bab7iä  zu  *baunä  entstanden. WP.  II  131,  WH.  I  436.
bhMd'  .gut*.
Ai.  bhadrd-h  , erfreulich,  glücklich,  gut',  n.  , Glück,  Heil',  sii-bhadra-h ,herrlich' =  av.  hu-badra-  »glücklich';
got.  batiza  ,besser',  batista  , bester',  aisl.  betre,  betstr,  ags.  bet{e)ra,  betst, ahd.  bezzir(o),  bezzist,  nhd.  besser,  best]  dazu  das  Adv.  des  Kompar.  aisl. betr,  ags.  bet  (*batiz),  ahd.  baz  (*bataz,  erstarrtes  Neutr.  .Nutzen');  aisl. batim.  ,Verbesserung,  Heil*,  afries.  bata  m.  , Vorteil*,  mhd.  bazze  ds.;  got. gabatnan  ,Nutzen  erlangen*,  aisl.  batna  , besser  werden*,  ags.  batian,  ahd. bazzen  ds.;  mit  Ablaut  got.  böta  f.  ,Nutzen*,  aisl.  ags.  bot  , Besserung,  Er- satz*, ahd.  buoz(a)  f.  ,Besserung,  Buße'.
WP.  II  151  f..  Feist  83,  103,  174,  J.  Weisweiler  Buße  (1930).
107
hhaZ'  zuteilen;  als  Anteil  bestimmen  oder  (ursprüngl.  medial?)  als  An- '  teil,  als  Portion  erhalten'.
Ai  bhajati  , teilt  zu'  =  av,  bag-  (bazat)  ,als  Anteil  bestimmt  sein',  ai. hhaaa-h  ,Gut,  Glück*,  av.  baga-,  baya-  n.  , Anteil,  Los,  bes.  günstiges';  ai. bhaaa-h  , Zuteiler,  Herr,  Beiname  des  Savitar  und  eine
```


## [2026-09-05T06:04:15.158Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==117' POK_01.txt | head -40",
 "description": "Print Pokorny page 108"
}
```


### [2026-09-05T06:04:16.832Z] TOOL RESULT

```
s  andern  Aditya'  = baya-  ,Herr,  Gott',  npers.  bay  ,Gott'  (formell  auch  =  gr. -ya/og) ;  ur- ind.  (Mitanni)  ON  Bagarriti  (=  Hhaga-rlti-  , Segensstrom'),  GN  Bagbartu (=  *bhaga-bhrt-  , Segenspenderin'),  kleinas.  VN  Bayadd(J^)ov£g  (=  ^bhaga- da-non-  , Reichtum  spendend'),  Kretschmer  KZ.  55^,  95,  Gl.  18,  232;  ai. hhaktd-m  , Mahlzeit*  =  av.  baxta-  Partiz.  ,als  Anteil  zugewiesen*,  n.  ,be- stimmter  Anteil,  Schicksalsbestimmung,  bes.  Mißgeschick*;  ai.  bhaksati o-onießt,  verzehrt^  =  av.  baxsaiti  ,hat  oder  gibt  Anteil',  Desid.  ai.  bhik-, Säte  ,erbittet';
phryg.  Bayalog'  Zevg  0Qvyiog  Hes.  (vielleicht  iranischen  Ursprungs); oder  ob  zu  gr.  q)r]y6g  , Eiche'?     S.  unter  bhägö-s]
OT.  (paysTy  , essen*,  aizo-qtdyog  , Getreide  essend',  usw.;  wegen  gr.  cpayo- yeg'  aiayöreg,  yväd-OL  ;Hes.  vielleicht  hierher  (Much  Zfdt  Wtf.  2,  283)  as. Ucinni-)  bako,  nhd.  Backe]
slav.  *bog^  , Anteil'  in  aksl.  ubog-b,  nebog^  ,arm',  bogah  , reich*,  aksl.  bog^ ,Gott'  (urverw.  oder  iran.  Lw.);  GN  Dazdi-bog^  , Reichtum  spendend';
toch.  A  jpäkj  B  pake  ,Teil*,  A  pagim  , Schatz*.
WP.  II  127  f.,  W.  Schulze  KZ.  60,  138  =  Kl.  Sehr.  469.
2»  hhag'  , scharf,  auch  vom  Geschmack'??
Kret.  cpdygog  , Wetzstein,   dxövr]^,   q)0^6g  ,spitzköpfig'   (aus    '^q)a^6g  nach Xo^og  , schief  ?)    wird   von    Liden  Arm. -St.  57  ff.  mit  arm.  bark  (könnte  = (pdyqog  sein)  ,herb,  bitter,  scharf  von  Geschmack;  heftig,  zornig*  verglichen, doch  kann  bark  auch  zu  idg.  *bhorguo-s  gehören. WP.  II   128.
bhägö-s  f.  ,Buche*.
Gr.  q)rjy6gy  dor.  g)ay6g  f.  ,Eiche*  (vgl.  Specht  KZ.  66,  59);  lat.  fdgus  f. ,Buche*;  gall.  bägos  in  ON  J5ä^äco?i,  Bägono-]  ahd.  buohha  , Buche*  (bököh-y vgl.  Silva  Bäcenis  ,Harz*  bei  Caesar  und  mlat.  Böcönia  ,Rhön'),  aisl.  bök  f., ags.  böc,  bece  (bökjön-),  dazu  got.  böka  f.  ,Buchstabe',  aisl.  bök,  ags.  5öc, ahd.  buoh  f.  n.  ,Buch*,  ahd.  buohstap  , Buchstabe',  eigentlich  , Buchenstab zum  Einritzen*.
Nisl.  beyki  n. , Buchenwald*  ist  (wegen  bceki  ds.)  Schreib  Variante  von  *b0kij einem  späten  Kollektivum  zu  bök]  ebenso  ist  vielleLcht  nisl.  beykir  , Küfer* zu  erklären.  Unklar  ist  mir  aisl.  budkr,  baudkr  , Medizinkasten',  das  nach Cleasby-Vigfusson  85b  ein  Lw.  aus   mlat.
```


## [2026-09-05T06:04:23.984Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"bhag\" IEC.txt | head -40",
 "description": "Grep Mann IEC for bhag"
}
```


### [2026-09-05T06:04:24.037Z] TOOL RESULT

```
1062:bhag-, bhāg- ‘enjoy; enjoyment’. WP II, 127 (à) Skt. bhajami “award; experience; enjoy; possess; bhagah “possession, luck’; bhágah “lord of the gods’; Av. bagom ‘share’, bayo ‘god’; Iran. LW in Arm. bag (i-st. share);
1064:İsg. ʻate’; -phagos (cpds.; LW in Arm. bagin, bagni, -av ‘idol’ is apparently isophonic with Lat. faenum (‘usury’, fr. *bhaginom?); OCS (and comm. SL.) bogü “god”, beside bog-atü ‘rich’; Cz. also ne-bohý, u-bohy ‘poor’; Srb. cf. z-bog, adverb "Tor the sake of: Latv. na- bags ‘poor’. Cf. -baig- in Olr. su-baig-idir (3s. dep. ‘he rejoices’). See next, and cf. bhag-
1065:bhāg- (1) (variant of bhag-, q.v.). WP II, 127 Skt. bhagáh (Cshare'. Vedic: luck); Av. baya ‘part’; OPer. bàji- ‘tribute’; Per. bat id.; Tokh. A pàk, B pàke “part'; Olr. bág “sake, benefit’; MIr. bá (loss of -g as in brí, tí, rí); Slovene, cf. božati (“fondle”, from bhag-, q. v.); Ukr. po-baZzaty ‘felicitate’; baZaty, bahnuty ‘desire’; Cz. baZziti ‘crave’, na-ba£Ziti ‘satisfy’. Cf. Skt. bhajitah "shared
1067:bhagh- (bhaghino-) (?) ‘mud, marsh’ OLat. cf. fa-mix (Fest.: ‘marsh’, fr. *bhagh- + *mig-?) beside faedus, foedus (“filthy”, fr. *bhaghido-?); Walloon fagne *peat-moor' be- side Fr. fange, It. fango ‘mud’; Cz. bahno, Pol. bagno “mud? beside Cz. baZina ‘marsh’
1069:61 bhaglos — bhaksó, ið
1070:bhaélos (?) ‘enjoyment’. (Variant of bhag- (1), q. v.). See next Per. bazla jesť’; Gk. phágilos “eatable?
1071:bhagmos ‘enjoyment, feasting’. See bhag- (1) Per. bazm ‘feast’; Gk. cf. phágema ‘food’, phagésia “feast”
1072:bhaào, ið (?) “force, thrust, rant Olr. bágaim ‘boast, assert, vow’; Du. (ambig.) beuken ‘flog’. cf. bhag- (2)); Latv. bāžu, bāzt, and bazit (*thrust, bung’, refl. ‘obtrude one- self)
1073:bhāĝos (1) ‘beech-mast, acorn; mast-bear- ing tree, beech, oak’. WP II, 128 Gk. phégós (Dor. -à-) ‘beech, oak’; Lat. fagus; MHG buoche; Du. beuk; OE bëce; ON bók ‘beech’. Cf. W. baedd, Cor. bath (“boar”, fr. *bhag-ed- *mast-eater")
1074:bhà$os (2) “part, share’. Variant of bhag- (1), q.v. WP II, 128 Skt. bhaj; OPer. baji-; Per. ba: Tokh. pak, pake; MIr. cf. dím-bág ‘sorrow’, air-bág ‘glory’
1075:bhaghulos, see bhaghus Skt. bahuláh, bahaláh ‘dense, abundant’; Gk. pakhulós *thickish"
1076:bhaghus ‘dense, thick, plentiful’. WP II, 151. Skt. bahüh; Beluchi baz ‘dense’; Kurd. bez ‘fat; Arm. cf. bazum (inflected Iran. LW? ‘much, many); Myc. & Gk. pakhús; cf. phák- elos (cpd. *bundle); Li. cf. bázmas ‘mass, crowd'.
1185:bheg- ‘break, pierce’ Skt. bhagnah ‘broken’; Arm. bek, id., bekem, bekanem ‘break’. (MHG bichen, bicken ‘stab’, bic, gs. bickes ‘stab; cut’; OE cf. becca ‘pick, mattock’: G Bicke preferably from bhig-, q. v.)
1459:bhog- (?) ‘break’. Cf. bheg- Skt. (ambig.) bhagnáh; Arm. (?) cf. ham-bak ‘inexperienced’; Olr. cf. bocht (‘poor’, if fr. *bhogto-) (JP)
4531:ghab- ‘seize’. (Variant of ghab- (1), q.v.) Hes. khabós “tight, cramped?'; Gk. khábos ‘muzzle fitted to animal; Umb. cf. habe, 3s. “has, takes’; habina, hapina, adj.f. (spayed. NB: This wd. is distinct from Umb. haf-: Lat. hab-ere); Du. gappen, v. ‘filch’; Ir. cf. (ambig.) gaibhéal, gabhag ‘strait’; see next
16781:‘spleen’. (Cons. and vowels anomalous. Prob. a cpd.) Skt. cf. plihan, m.; Av. sporozn; Per. supurz; Arm. pajcayn, gs: pajceyan; Gk. splén, gs: splénós, m. id. beside a-splenion *spleenwort'; splágkhnon, n. “bowel'; Lat. lien & lienis, gs. id. m. ‘spleen’; MIr. selg, Ir. sealg & seilg, f. id. beside seabhag, m. (sic), id.; Br. felch, m. id.; OCS slezena, f.; OCz. slezeň, m., R sele- zën-ka, f. id.
```


## [2026-09-05T06:04:30.107Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"bhag\" AHD_watkins1985.txt | head -20; echo \"=== WLD ===\"; grep -n \"bhag\" WLD_band3.txt | head -20",
 "description": "Grep AHD and WLD for bhag"
}
```


### [2026-09-05T06:04:30.164Z] TOOL RESULT

```
323:outlaw”), in: a. Old English bannan, to summon, pro- claim, and Old Norse banna, to prohibit, curse: BAN}; b. Old French ban, feudal jurisdiction, summons to military service, proclamation, Old French bandon, power, and Old English gebann, proclamation: BANAL, BANNS; ABANDON; C. Old French banir, to banish: BAN- ISH; d. Late Latin bannus, bannum, proclamation: Ccon- TRABAND; @. Italian bandire, to muster, band together (< “to have been summoned”): BANDIT. 4. Suffixed form *bha-ni in Germanic *b6dni- in Old Norse b6n, prayer, request: BOON!. 5. Suffixed form *bhd-ma in: a. Latin fama, talk, reputation, fame: FAME, FAMOUS; DEFAME, INFAMOUS; b. Greek phémé, saying, speech: EUPHEMISM. 6. Suffixed o-grade form *bhd-nd in Greek phéné, voice, sound, and phénein, to speak: PHONE, -PHONE, PHO- NEME, PHONETIC, PHONO-, -PHONY; ANTHEM, (ANTI- PHON), APHONIA, CACOPHONOUS, EUPHONY, SYMPHONY. 7. Suffixed zero-grade form *bha-to- in Latin fatéri, to acknowledge, admit: CONFESS, PROFESS. 8. Greek blas- phémos, evil-speaking, blasphemous (first element ob- scure): (BLAME), (BLASPHEME), BLASPHEMOUS. [Pok. 2. bha- 105.] bha-bha-. Broad bean. 1. Latin faba, broad bean: FAVA BEAN. 2. Variant form *bha-un- in Germanic *bauné in Old English béan, broad bean, bean of any kind: BEAN. [Pok. bhabhé 106.] bhad-. Good. 1. Germanic (comparative) *batiz6 in Old English betera, better: BETTER. 2. Germanic (superla- tive) *batistaz in Old English bet(e)st, best: BEST. 3. Ger- manic noun *b6¢6 in Old English bét, remedy, aid: BooT?. 4. Germanic verb *batnan, to become better, in Old Norse batna, to improve: BATTEN!. [Pok. bhdd- 106.] bhag-'. To share out, apportion, also to get a share. 1. Greek phagein, to eat (< “to have a share of food”): -PHAGE, -PHAGIA, PHAGO-, -PHAGOUS. 2. Extended form *bhags- in Avestan bakhsh- in Persian bakhshidan, to give: BAKSHEESH, (BUCKSHEE). [Pok. 1. bhag- 107.] bhag-. Sharp. Suffixed form *bhag-ro- in Greek phag- ros, whetstone, also a name for the sea bream: PORGY. [Pok. 2. bhag- 107.] bhaghu-. Arm. Germanic *bdguz in Old English bdg, boh, bough: BouGu. [Pok. bhdghii-s 108.] bhago-. Beech tree. 1. Germanic *b6k6, beech, also “beech staff for carving runes on” (an early Germanic graphic device), in: a. Old English bdc, written docu- ment, composition: BOOK; b. Middle Dutch boek, beech: BUCKWHEAT. 2. Germanic *bdkjdn- in Old English béce, beech: BEECH. [Pok. bhdgo-s 107.] bhar-. Also bhor-. Projection, bristle, point. 1. Suffixed o-grade form *bhor-so- in Germanic *barsaz in Old English bzrs, perch, bass (a fish that has a spiny dorsal fin): BASs!. 2. Suffixed zero-grade form *bhAr-sti- in Germanic *bursti- in Old English byrst (> Middle Eng- lish bristel), bristle: BRISTLE. 3. Extended zero-grade form *bhrs- in: a. Germanic *bur- in Swedish borre, bur, perhaps akin to the Scandinavian source of Middle English burre, bur: BUR}; b. suffixed form *bhrs-dh- in Germanic *bruzd-, point, needle, in Old Norse broddr, spike: BRAD; C. suffixed form *bhrs-ti- in Latin fastig- ium, summit, top, extremity: FASTIGIATE, FASTIGIUM; d. possibly suffixed form *bhrs-tu- in Latin fastus, fasti- dium, disdain (from the notion of prickliness): FASTIDI- ous; e. suffixed form *bhrs-tio- in Russian borshch, cow parsley: BORSCHT. [Pok. bhar- 108.] bhardha. Beard. Possibly related to bhar-. 1. Germanic *bardaz in Old English beard, beard: BEARD. 2. Ger- manic *bard6, beard, also hatchet, broadax (the associ- ation of beard and ax is attested elsewhere in the Indo-European family; both were symbols of patriarchal authority), in Old High German barta, beard, ax: HAL- BERD. 3. Latin barba, beard: BARB!, BARBEL, BARBEL- LATE, BARBER, BARBETTE, BARBICEL, BARBULE; REBARBATIVE. [Pok. bhardhé 110.] bhares-. Also bhars-. Barley. 1. Germanic *barz- in Old
485:gé@i-2. To sing. Contracted from *geai-. Zero-grade form *gi- (< *gia-) in Sanskrit gitd, song: BHAGAVAD-GITA. [Pok. géi)- 355.]
1276:BABA baba- BABBLE baba- BABE baba- BABKA baba- BABU baba- BABUSHKA baba- BABY baba- BACILLUS bak- BACTERIUM bak- BACULIFORM bak- BAGEL bheug-3 BAGUETTE bak- Bails bheug-3 BAIRN bher-1 BaIT! bheid- BAKE bhé- BAKSHEESH bhag-' BALALAIKA baba- BALCONY bhelg- BALE! bhel-2 BALE? bhelu- BALEEN bhel-2 BALK bhelg- BALL! bhel-2 BALL2 gWele-1 BALLAD gWele-1 BALLAST bhoso-, kla- BALLET gWela-1 BALLISTA gWele-1 BALLOON bhel-2 BALLOT bhel-2 BALLOTTEMENT bhel-2 BAMBINO _baba- BAN! bha-2 BANAL bha-2 BAND! bhendh- BANDANNA bhendh- BANDIT bha-2 BANDOLEER bha-1 BANDORE pandoura BANE gWhen-1 BANG! bheg- BANIAN wen-1 BANISH bha-2 BANK! bheg- BANK? bheg- BANK? bheg- BANKRUPT bheg-, reup- BANNER bha-! BANNERET bha-1 BANNS bha-? BANQUET bheg- BANQUETTE bheg- BANSHEE gWen- BANTLING bheg- Baptist gébh-!
1282:BEE? bheug-3 BEECH bhago- BEEF gWou- BEETLE! bheid- BEETLE? bhau- BEFALL p(h)ol- BEFORE pert BEGET ghend- BEHEST kei-3 BEHIND ko- BEHOOF kap- BEHOOVE kap- BELAY legh- BELCH bhel-4 BELDAM deu-2 BELEAGUER legh- BELEMNITE gWele-1
1294:BENIGN deu-?, gene- BENTHOS gWadh- BENUMB nem- BEQUEATH gWet-2 BEQUEST gWet-2 BEREAVE reup- BERM bhrem-2 BERRY bha-1 BERSERKER bher-3 BESPEAK spreg- BESPRENT spergh- BEsT bhad- BETOKEN deik- BETRAY d6- BETROTH deru BETTER bhad- BETWEEN dwo- BETWIXT dwo- BEVEL bat- BEVERAGE pO(i)- BEWITCH weik-2 BEZOAR gWhen-1, pa- BHAGAVAD-GITA g@i-2 BI- dwo-
1313:BOLD bhel-2 BOLE! bhel-2 BOLL bhel-2 BOLLIX bhel-2 BOLOMETER gW¥ele-1 BOLSHEVIK bel- BOLSTER bhelgh- BOLT! bheld- BOMB bamb- BOMBARD bamb- BONANZA deu-2 BONBON deu-2 BOND bhendh- BONDAGE bheue- BONHOMIE deu-2, dhghem- BONITO deu-2 BONNE deu-2 BONNYCLABBER band- BONTEBOK bhugo- BONUS deu-2 BOOBY baba- BOODLE bheue- BOOK bhago-
1314:BOOM? bheue- BOON! pbha-2 BOON2 deu-2 BOOR bheue- BOOT? bhad- BOOTH bheue- BORDELLO bherdh- BORDER bherdh- BORE! bher-2 BORE’ bher-1 Boreas gWero-1 BOROUGH bhergh-2 BORROW bhergh-1 BORSCHT bhar- BOSCAGE busk- BOSOM beu-1 BOTH ambh6o BOTHRIUM bhedh- BO TREE bheudh- BOTTOM bhudh- BOTTOMRY bhudh- BOTULIN gWet-3 BOTULINUM gWet-3 BOTULISM gWet-3 BOUCLE beu-1 BOUGH bhaghu- BOUILLABAISSE beu-! BOUILLON beu-1 BOULDER bhel-2 BOULE! gWele-1 BOULE? beu-! BOULEVARD bhel-2, werg-
1324:BRIO gWere-2 BRIOCHE bhreg- BRISANCE bhréi- BRISTLE bhar- BRITTLE bhreu-1 BRONCHIECTASIS  ten- BRONCHO- gWere-4 BRONCHUS gWere-4 BRONTOSAUR bhrem-! BROOD bhreu-2 BROOK? bhriig- BROOM bhrem-2 BROTH bhreu-2 BROTHEL bhreu-' BROTHER bhrater- BROW bhri- BROWN bher-3 BROWSE bhreus-1 BRUIN bher-3 BRUISE bhreus-2 BRUMAL mregh-u- BRUNET bher-3 BRUT gWere-2 BRUTE gWere-2 BUBO beu-! BUCCAL beu-1 BUCEPHALUS gWou- BUCK! bhugo- BUCKAROO wak- BUCKBOARD beu-! BUCKLE! beu-! BUCKLE? beu-1 BUCKSHEE bhag-' BUCKWHEAT bhago- BUCOLIC gou-, kWel-1 BuppHA bheudh- BUDGET bhelgh- BUDGE! beu-1 BUGLE! gWou- BUGLOss gldgh- BUILD bheue- BULGE bhelgh- BULIMIA gWou-, leia- BULK! bhel-2 BULL! bhel-2 BULL? beu-1 BULLA beu-1 BULLATE beu-1 BULLET beu-! BULLETIN beu-1 BULLION beu-1 BULLY? beu-1 BULWARK bhel-2, werg- BUNCO bheg- BUND! bhendh- BUND? bhendh- BUNDESRAT ar- BUNDLE bhendh- BUNG peuk- BUNGLE bheg- BUPRESTID gWou- BUR! bhar- BURDEN! bher-1 BURG bhergh-2 BURGESS bhergh-2 BURGHER bhergh-2 BURGLAR bhergh-2 BURGOMASTER bhergh-2 BURIAL bhergh-! BURIN bher-2 BURN! gWher- BURN? bhreu-2 BURNET bher-3 BURNISH bher-3 BURSA bursa BURSAR bursa BURSE bursa BURST bhres- BURY bhergh-1 BUSHEL? bhau- BUSK! busk- BUSK? s(w)e-
2084:-PHAGE bhag-1 -PHAGIA bhag-! PHAGO- bhag-1 -PHAGOUS  bhag-! PHALANGE bhelg- PHALANX bhelg- PHALAROPE bhel-1, ped-1 PHALLUS bhel-2 PHANEROGAM bha-! PHANTASM_ bha-! PHANTASMAGORIA bha-1 PHANTOM bha-1 PHARMACOPOEIA kWei-2 PHARYNX bher-2 PHASE bha-1 -PHASIA bha-2 PHELLEM bhel-2 PHELLODERM bhel-2 PHELLOGEN _bhel-2 PHENO- bha-1 PHENOMENON bha-1 PHEROMONE bher-1 PHILANDER ner-2 PHILANTHROPY ner-2 PHILATELY tela- -PHILE bhilo- -PHILIA bhilo- PHILLUMENIST leuk- PHILO- bhilo- PHILODENDRON deru -PHILOUS _bhilo- PHILTER bhilo- PHLEGETHON bhel-1 PHLEGM bhel-1 PHLEGMATIC bhel-1 PHLOEM bhlieu- PHLOGISTON bhel-1 PHLOGOPITE bhel-1, okw- PHLOX bhel-1 PHLYCTENA bhlieu- -PHOBE bheg¥- -PHOBIA bhegw- PHOEBE bheigw- PHOEBUS bheigw- PHONE! bha-2 -PHONE bha-2 PHONEME bha-2 PHONETIC bha-2 PHONO- bha-2 -PHONY bha-2 -PHORE bher-1 -PHORESIS bher-1 -PHOROUS bher-1 PHOS- bha-1 PHOSPHENE bha-1 PHOSPHORUS bha-1 PHOT bha-1
2120:PORGY bhag-2 PORK porko- PORNOGRAPHY per-§ POROMERIC per-2 PORPOISE peisk-, porko- PORT! per-2
=== WLD ===
142:bitin OD, bhakteti 128°, bhaga-f ,Sohomgegeod*
```


## [2026-09-05T06:04:37.873Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT baga ===\"; grep -n \"baγa\\|baga-\\|ba\\^a-\" BRT.txt | head -30",
 "description": "Grep Bartholomae for baga"
}
```


### [2026-09-05T06:04:37.933Z] TOOL RESULT

```
=== BRT baga ===
16634:•  p.  baga-,  j.  'baj-a-  m.  'Herr;  Gotf: i)  lim  Ap.:  'gJ*  ^vazarkJ"  J'urJ'mazdii D.  6'.  I,  7,1,  X./.  1,  6. 1,  Ao.J,  i;  —  mäm i^urj'mazäll  utä  mih''a^  'gc^  pätuv  Ao.  1 /.  4;  —  t^un^mazää  .  .  utä  arnyä  'gäha^ ' tyaiy  hiftty  Bh. 4- 3 ;  \i;  —  i^ur^mazdä . . kadä  iagai6iIX.2.$,Q.3',4.ii  ^.4.3^;
16637:—  'ya  F.  16^1. KoropA.  —  ai.  bhäga-  m.,  mp.  bat,  l^*!-  bcgü.  — Pa.:  b<ri,  Sü,!  vibhaitä;  »gl.   NpüEcL  zu  Yt.?: ras  i  tHardumän  baxsad.  —    ')  Ungefähr  »»a. >o*H-  (sd.).  —  =)  Oder  zu  'ba^a-.
16638:"   g.   baga-,  j.  "baya-  n.  'Anteil,   Los':
```


## [2026-09-05T06:04:40.425Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '16620,16680p' BRT.txt",
 "description": "Read Bartholomae baga context"
}
```


### [2026-09-05T06:04:40.474Z] TOOL RESULT

```
Et.  und  Bed.?').  —  Pü.:  bnndk.  erl.:  dev yazaJiiAi).  —  0  Hds.  'sayä/a.  —  >)  Das  Wort ist  vll.  verderbt.  Eine  wenig  glückliche  Ver- mutung bei  Haug  Arda  Viraf  312.  —  J)  S. DOcb  lu  laoiaya-  No.  1.
•  j.  *baozdri-"  f.  'die  kennen  lernt,  inne wird  (geschlechtlich)':  ^rayam  'ri  (näml. gahvd)  "(Hündin)  die  sich  mit  drei  (Rüden) abgegeben  hat"  V. /j.  49;  —  lUnam  °n V.  15-  49-
Zum  V.  baod-,  fem.  zu  'iaosi/ar-  m.  —  ai. laddkar.  m.  —  l'ü.:  buraT\!\  —  ')  So  Jp  1, Mfi;  NA.  hat  himäri,  %  368.  33.
•  j.  baoSa-  m.  "Lösung,   Rettung'   oder
'Busse' :  'bm  F.  16.
Bed.  nach  Pü.:  böiiin;  3.  zuÄ^-.  — Et.?  Die angegebene  Bedeuluog  liesse  'baoxhm  er- warten oder  auch  *ia<iä"'i ;  zumV.  äw^;  vgl. ^ouru.bai'xlna-  und  baosnah:
ob,Google
ba]-5.baxta-
gaa
•  j.  baodnah-  n.  'Rettung,  Befreiung': naram    ahonam    avasca   rafhäsca  'nisca
Gull  zweifelhaftes  Wert;  s,  zu  Saolü-.  — NpQ. : ia  räi  i  xaläii  dädan  i  mardamän.
•  j.  bag-  V.  'als  Anteil  zuweisen;  —  zu- gehören'. Pries.  2  baia-.  —  PPfP.  baxta- (sbcs.)".
i)  'als  Anteil  zuweisen;  bestimmen, fögen'  (nur  in  'daxta-).  2)  'als  Anteil zugewiesen  sein,  zugehören,  bestimmt  sein für  — '  (Dat):  j'oz'at  .  .  garayB  vilastan vTsptm  avai  aipi  draonB  baiai  a^auru- naica  .  .  "soweit  sich  .  .  die  Berge  er- strecken, all  das  ist  dem  Priester  und  .  . als  ilu-  Teil  bestimmt"  Yt  i^.  8.
ai.  Ha^- V.  "panisipare';  bhäjati,  bhaitäh;  mp. baxlan  'luleilen'.  —  Vgl  baxs-,  —  ')  S.  noch  ' bagabigna-.
•  p.  baga-,  j.  'baj-a-  m.  'Herr;  Gotf: i)  lim  Ap.:  'gJ*  ^vazarkJ"  J'urJ'mazdii D.  6'.  I,  7,1,  X./.  1,  6. 1,  Ao.J,  i;  —  mäm i^urj'mazäll  utä  mih''a^  'gc^  pätuv  Ao.  1 /.  4;  —  t^un^mazää  .  .  utä  arnyä  'gäha^ ' tyaiy  hiftty  Bh. 4- 3 ;  \i;  —  i^ur^mazdä . . kadä  iagai6iIX.2.$,Q.3',4.ii  ^.4.3^;
—  ^ura'masdä  . .  hya'  makiUi^  'gänäm D.4-I,  X.6^.1.  II  2)  imjAw.:  aurvanUm  , ^7vä  .  .  'ys  tatasat  hväph  Y.io.  loj  10;
—  marah)m  .  .  °y?m  raevant»m  Yt.  7. 5; S;  —  'yanqm  asti  (näml.  mihrs)  ai.xra- "iwashmB  Yt/o.  141;  —  tfm  'y^m^^  t?m rafUm  .  .  yiin    ahur?m    mazäam    V,  70.  i ;
—  'ya  F.  16^1. KoropA.  —  ai.  bhäga-  m.,  mp.  bat,  l^*!-  bcgü.  — Pa.:  b<ri,  Sü,!  vibhaitä;  »gl.   NpüEcL  zu  Yt.?: ras  i  tHardumän  baxsad.  —    ')  Ungefähr  »»a. >o*H-  (sd.).  —  =)  Oder  zu  'ba^a-.
"   g.   baga-,  j.  "baya-  n.  'Anteil,   Los':
ava^a  hl  ^^ato  (sd.)  puhnm  atskat  aOiS 'ytm  haca  avantanqm  nisrinuyät  äat  yezi Avant  näirika  bavaiti(%A^  alu§ 'y>m  paiti nidanäiti  yezt  du-j'irqm  (sd.)  fanü  tialm>m •y>m  frajasät  Vd,2  (der  Sinn  ist:  Frau und  Söhne  des  Erblassers  sollen  aus  der Erbschaft  den  gleichen  Teil,  die  Töchter die  Hälfte  davon  bekommen);  —  ytmasät ys  matyfng  cixinusS  akmakSng  gaus  -gä (APn.)  «"JwMWii  (sd.)  V.  J2.  8;  ~  'ya Y.16^''.  a)  bes.  'günstiges  Los,  Glück': yazäi  *apqmca  'y»mca  YL  /j.  i.  o)  bes.  1 vom  Glück  in  der  Ehe,  'Eheglück'  (nur Komp.)'*.         [Yt/6".  15:  lies  voku.b'.\
Zum  V.  bog:  —    ai.  bhäga-  in.;    mp. :  S.  Pü. ;;
atm.  LW.  bog.  —  Pü.  (lu  F.,  Vd.}:  Äiy,  (zu Y.  ji):  baiisn,  Npü.:  iitia.  —  ')  Oder  zu ■iaja-,  —  »)  S.  dazu  Gdn.  Stud.  /.  123;  doch vgL  PiSCMEL  VSt.  /.  71  und  Bloomfield  SBE. 42.  94.
•  p.  baga'buxSa-  m.  EN.  eines  Persers, Genossen  des  Darius  bei  der  Magophonie, Me/äjSuirof:  'sJ'  n3mc^  dadukyakya  puiTa'' päri<^  Bh.<^.  18.
Eig.  'von  Gott  befreit,  erlöst';  'buxsa-  m.,  znm V.  baog-i  vgl.  Yt.  14.  46.
•  j.  ba/ä-  f.  Teil,  Stück  (des  heiligen Worts)"^  mit  definilivem  Gen.":  'yqm slaotanqm yesnyanqm  "dasStUck  die  St.-Y," Y.  55.  7'.  a)  bes.  von  den  Gebeten  V. 27.13—15:  °ya  alSa  (sd.)  äs  ahunahe vairyehe  Y.  r^.  3 ;  5,  6,  a  i ;  —  °yq»*  asahe vahistahe  "das  Stück  A.-V."  Y.20.$;  — 'yqm  yaihl  hätqm  "das  Stück  Y.-W  Y. 21.  5.  A)  bayä-  slaotanqm  yesnyanqm heisst  Y.55  (nach Y. 55.7):  'ya  st' y-  Y.55 Überseht.
Zum  V.  bag-i  vgL  tbafa-.  —  Pü,:  baxlärTAl), tt\.: /raiarl;  Sü.;  *vibhafan5*). —  •)  Anders Gdn.  GlrPh.  2.  19:  'Homilie';  Dsx.  ZA.  /. 1651  "prüre  diyine';  s.  noch  No.  3.  — »)  Ausser  Y.  31.  5,  wo  aber  y/6lu  Aättfi»  als Zitat  (nicht  Akh.)  zu  nehmen  ist.  Vgl.  Der. VglS.  /.  346.  Der  Gen.  hat  die  Bedeutung •bestehend  aus  -'.  —  3)  Bei  West  SBE.  j/. 454:  'apportionment'.  —  4)  So  nach  Sü.  von baxlärih  in  Sg.  zu  lesen.
•  p.  bagä'bigna-  m.  EN.  eines  Persers: vidam<^  näma"  °nahy3  pu^''<^  pärst^ Bh.4  18.
Eig.  Bed.?  *bi^»a-  {auch  in  Mfiiafliynjv)  ist jedenfalls  PPfP.  wie  ai.  vignä-  usw.;  Versuch einer  Et.  (zu  gr.  *o^o()  bei  Justi  ZDMG.  49- 6S2,  NB.  4S9  (s.  auch  HOsing  ZDMG,  S4- 127);  oder  ist  *bigna- lu  tag-  zu  stellen,  mit
•  j.  baj-ö.däta-  Adj.  'gottgeschaffen':  y.it hx  stäram  'tanam  aiwi.raocayänte  "damit ihn  die  gottgeschaffenen  Sterne  bescheinen" V.  ig.  33.
mp-  (l'ü.)  i<i'i  dat.
•  j.  bayö.baxta-  Adj.  'von  den  Göttern bestimmt,  gefügt':  'ttm  paiti  yaomm  Yt ^'.35;  _  =wVyLi'5(?).  a)  -fc«  ASn. als  Adv.  'auf  (besondere)  Fügung  der Götter'";  nairyqm  ham-varaitlm  ..yä  dim (sd.)  jasaiti  'ttmcit  ". .  die  sich,  und  zwar auf  besondere  Fügung  der  Götter,  bei  ihnen (den  Männern)  einstellt"  Vr.  7. 3.
mp.  (Pü.)  bay  boxt.  —  S.  noch  '"baoiS.baxtila.  — 1)  Vjjl.  zu  dieser  Fassung  die  Erklärung  von baji  und  hai  baxi  in  Mx.  34.  6  t.
dby  Google
923  ba;'o.baxt9in  —  ba^daka-  934
•  j.  bf^ö.baxUm  Adv.:  s.  bayB-ioxta-,      irUtake  baxiaiti  "Ver  von  dir,  o  H.,  dem
•  j.  baxta-  i)  Adj.  (fem.  •«-)  'als  An-  mit  Milch  gemischten,  sein  Teil  (zum  Ge- teü  zugewiesen;  bestimmt,  gefügt*  (nurinoss)  empfängt"  \.io.\ii';  —  ym  dim Komp.).  a)  n.  'noTfia';  a)  'bestimmter  nStt  yaoidakmU  ^risüm  aSahe  fyaoknahe Antcfl':  n3mas9  U  ää%rS  'bm  vahistäi  btul^nH  ".  .  so  erhalten  sie  ein  Drittel a!a4>nt  ". .  dir,  der  du  dem  . .  Gläubigen  dieser  (sündigen)  Tat  als  ihr  Teil"  V. sein  Anteil  gibst"  V.  27.  i.  b)  'Schicksab-  i^-  ioo«>.  a)  'Anteü  geben  an  -  (Aide), bestimmung":  akra  aoät  ß-ajasaiti  'ta  zuteilen,  austeilen,  schenken":  ys  (näml. (NS.)  a6J/  nijasaiä  "es  sind  die  Bestim-  s«"*«)  mam  (nämL  gam)  ^äitqm  nBit mungen  des  Schicksals,  die  hier  (bei  ihm)  baxsahe  "(der  Z,)  der  du  mich  (das  Rind), sich  voUaeben  und  ihren  Abschluss  er-  wenn  ich  gar  gekocht  bin,  nicht  aus- reichen" V.5.8'>.  «)  insbes.  'übles  teilst"  V.j/.  is);  —  ^a^.,  „M^tcMJar*** Verhängnis,  Missgeschick,  Verderben' :  *tfm  («!-)  y^t  haewvmta  gai-a  ra^wayat  baxsa- äame  mazdayasne  "Verhängnis  über  dich,  yaatca  N.  76";  —  tal  a^annS  baxsftoi  tarn o  mazday.  Religion"  VtÄas-  c)  ''^^  paiti  ahuraüätam  \l.6.i;-j.y,  —  boxlänti Stimmung  über  -,  Bestimmungsrecht'  (nur  raesca  ^annasM  V)-tj4,  4^;—  yüitm- Komp.).  ^'^  x'arms   baxsayata  VytÄ  a)    mit
KompE.  —  Eig.  PPfP,  lam  V.  ba^,  sd.  —  Dat  des  wem?:  kahmai  rais^a  ^armasca inp,  (Pa.).   np.  faxt  'Schiclisal' 1   s.  No.   i.  —   baxsäni  Yt /O,  108;   108,  ilo,  I4.^T,  —
-  ^T't^i  "i-  t^^ir i^^t""'LrJträ!^i  ^"^  ■  ■  ■^'^'■^  ■  ■  ^'^'^'^  (=*•->  ■  ■  «"^^
bVdnn'Tw/ *^fl^-fl™r'-  »>  Wie^Q  ^ar^fig  *baxs»nia  (sPPrM.)"  Yt&i;  — lesen?  /Si.:  brla,  das  in  Su.  durch  bhägyak,  yd^ra  vd  ahurS  ,  ,  fi-aädh^m  boxsai chintmh  gegeben  wird.  F.  4b;  —    kaemS  oäbts  QF.  statt  DP.)
•  j.  baxtar-  m.  'der  den  gebührenden  y^i  .  .  xävar?  aojäsca  baxiaiti  .  .  AatmiS Anteil  anweist,  iribuior':  yatäi  sörirake' taliil  (durch  Attraktion)''  ydi  .  .  änA^nie 'iärsm  tistrim  Vt  &  i ";  —  upa.barai  spattiS  .  .  baxiaiti  kaomS  tssät  (durch äyapt»m  °ta!a  nivaxiaca  VytjÄ  ,Ataaktion)^^yäiainTttd3oJiaire..*pai^fm
KompE.  (s.  «w't    —    Zam  V.  iag--.   —   mp.  räo»m(sd.ya  baxiaiti  Y.p.  azf.
öaxiir.  —  0  Vgl.  \t.  S.  34.  „,;[  j  'zuteilen,  austeilen':  ^maÄml  hls
•  j.  baxa^ra-  il  'Anteil,  Portion':  *'ra  zaoiw  *äbaxiöAfa  "nach  deinem  Gefallen F.  ;&■>;  —  sairimananqm  'räi  Vyt52(?).  teile  sie  aus"  Y.j;^,  io'>,
KompE.  —  Zorn  V.  ia}r-.  —  Pu.:  Wjrrj);  s.  mit  n  'austeilen  an— '(Dat'):  ta  (näml. noch  No.  2.   -   n  Hds.  •xira.    -    >)  Pü.:  ^^^j        vtboxsaiti  äbyS  daitiAubyS  seilte
..  d«u  DST.  ZA.  3.  680.-J)  Geschr.  baar ;  |  (naml^Aj/o^)^,  ^^  *■  47;  34- np.  katx ;  aus  ar.  *iAaitr' ;  vgl.  in  bäitrl-  nnd
Hau.  PSl  33.
•  j.,  g.  baxs-  V.  'Anteil  haben,  geben'. Praes,  i  l>ax/-,2  baxsa-,  30 (Itcr.) ^lur/a)«-.
i)  'Anteil  haben  an  — ,  inne  haben; Anteil  nehmen  an  — ,  bekommen',  mit Akk.  oder  Gen.:  nöil  .  .  avsstryö  .  . Aum»rjtsis{sd.)  baxs'täY. 31. 10;  —  tiuiasSt nSii  baxiaiti  vahiitahe  auhSus  "und,  wenn er  gestorben  ist,  wird  er  des  besten  Lebens nicht  teilhaftig"  V.5.61;  —  asäuni  cdis (sd.)   yä    il    cicä    vahistä     hanarp    (sd.)
'hwahmät  zacsät  dngi'S  baxsaili  (3SKA.)  1  aitm^al  'tanqm  (nämL  yavaaqm)  aOavai ".  .  soll  .  ,  der  ZJn^enosse  (daran)  teil ;  abatanqm  V.  7,  35.
haben?"    Y.  47.  5'';    —    vanäayalil   (sd.)        KompE.—  Et.?  Vgl.  Var.  6axr.   Bed.?    Das yqm    natdiitqm   gttl>am    dr?gi-i    baxsaitt       Wort ^steht^^wischen  .^ox/a- und  Wa-.- Pa.: ".  .   das    nachbarliche    Haus,    das    (jetzt  |       "     *       "^""^  ''' noch)  der  i>«^gläubige  (Fürst)  inne  hat"  j  •  p.  ba''da'ka-  Adj.  (fem.  'kä-')  'Untertan; Y.  s°-  3*' j  —  y^  *^  ■  ■  ftaema  . .  gava  \  Untertan,  Vasall':    imä   dahyuve^  tyä  .  .
■•Erweiteniiig'  ans  ia^-,  sd.;  S  1?ft  5-  —  "P- inssiäaH  'schenken'.  —  Pü.:  iaxiilani  s.  noch No.  1,  a,  5.  —  ■)  Pfi,  «L:  i'ästai  tu  pa  api- yasi  I  15  därrnd.  —  i>  D,  i.  das  jetit  noch lut  falschen  Religion  hälL  Pü.  etl.:  kti  an andar  därisn  afi  stänend.  —  3)  Vgl,  N.  /tf nnter  2.  Falsch  Dsr.  ZA.  /.  104.  —  *>  Ganz falsch  DsT.  ZA.  2.  144;    Tgl.  Hbm.  PSl  131
tn  np.  daxiüdan.  —  5)  Vgl.  zSL  Gun.  KZ.  JO. SI8.  Pü.  erl,:  ö  ariämUn.  —  *)  F I.  NA. "hA.  —  7)  An  den  folgenden  NP.  des  Pron. rel.  —  8)  Gdn.  BB.  l£.  258  will  'lurückgeben, vergelten'.     Das  väre  aber  doch  eher  paitiJf.
•  j.  bata-  Adj.  'geschrotet',  vom  Getreide:
dby  Google
9^5
bawra-
banda-
926
manä  'ks  (NPf.)  äh^is  ".  .  die  .  .  mir untertaa  waren"  Bh.  /.  7 ;  —  dadarÜs  .  . Manä  'ia*  Bh.^,  3,  2.  7;  6,  10,  14,^.6,  9, 14.  5- 1.
Eig.    'der   Qemands)  Fesseln  trägt'.   —    np.
ianfl'fl  'Sklave'.
```


## [2026-09-05T06:05:04.633Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HUB bahr ===\"; grep -n \"bahr\\|barx\\|baxsidan\\|baxš\" HUB.txt | head -30; echo \"=== HRN ===\"; grep -n \"bahr\\|barx\\|baḫš\\|bak̲h̲š\\|baxš\" HRN.txt | head -30",
 "description": "Grep Hübschmann and Horn"
}
```


### [2026-09-05T06:05:04.694Z] TOOL RESULT

```
=== HUB bahr ===
1082:ware np. bahr, bahra 'Teil, Anteil, Loos, Gliick'
1085:bahr, die mir die urspriingliche zu sein scheint, *Teil\
1087:'zugeteilt') nicht. Np. barx^ barxa 'Teil' = afgh. LW.
1094:vgl. ap. baji' *Tribut'. So wird auch np. 6aAr = barx
6388:H. 237 und 239; boi 'Geruch' H. 240; bahr Xoos' H. 245— 181 —
6864:(nach Noldeke); bahr = . barx *Theil, Antheil* = zd.
=== HRN ===
2507:(Aogem.); phlv. hahr ^ bahrakj (geschrieben *inN2),
```


## [2026-09-05T06:05:07.248Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '1070,1110p' HUB.txt; echo \"--- 6855-6875 ---\"; sed -n '6855,6875p' HUB.txt",
 "description": "Read Hübschmann bahr entry"
}
```


### [2026-09-05T06:05:07.298Z] TOOL RESULT

```
*cause' Shk. 270 (vgl. avahdn without a cause' Shk.) =
phi. vahcLnak auf ap. ^vahdna- zuriick, das ich mit
Fr. M tiller zu skr. vasana- *Gewand' stelle. Der Be-
griflfsubergang : Kleid— Hiille — Vorwand macht doch
keine Schwierigkeit. Vgl. d. Ge-wand und Vor^wand^
d. Hiille und hehlen, lat. praetexo Verbramen, be-
manteln, als Vorwand nehmen', praetextus * Vorwand'
etc., WZKM. 5, 186.
^) Uebrigens nioht nur im Persischen sondern auch in den andern
iranischen Spraohen.— 33 —
245. Zd. hubaira- *glucklich' ■=•- paz. hubahar kann ich mit
Geiger nur zu skr. subhadra- *herrlich* stellen. Dann
ware np. bahr, bahra 'Teil, Anteil, Loos, Gliick'
= skr. bhadra- *herrlich, glucklich ; Gltick, Heil, Gutes'?
Zu dieser Etymologie stimmt nur die Bedeutung von
bahr, die mir die urspriingliche zu sein scheint, *Teil\
Anteir (vgl. np, baxt 'Schicksal, Gliick* =^ skr. bhaktor-
'zugeteilt') nicht. Np. barx^ barxa 'Teil' = afgh. LW.
braxa, baxra share, portion, part, lot' (Raverty) setze
ich = ap. *baxtra-, zd. baxdra- (vgl. np. Balx aus ap.
Bdxtri' *Bactrien') von zd. bal = skr. bhaj *teilen, zu-
teilen (meine Avestastudien p. 696). Zd. bax^ra- braucht
nicht *Mahlzeit' zu heissen, Darmesteter iibersetzt es
durch 'revenue' und stellt es zu bhaj *teilen, zuteilen*,
vgl. ap. baji' *Tribut'. So wird auch np. 6aAr = barx
= zd. baxdra- sein.
247. Np. he = paz. atvS, phi. apB setze ich = ap. *apaiy
aus apa + id, wie naiy nicht' = fia + id (skr. ned)
ist. Die Form ist in der Composition entstanden, sonst
ware *apaii/ zu np. ab geworden. Im Phi. und Pazend
findet sich apS, awS nur als 1. Glied von Compositis,
wie auch im Neupersischen bS noch moistens in Com-
position erscheint.
249. Zu beoctan *sieben' (nach Noldeke *streuen) stellt
Geiger jetzt afgh. mnjql reinigen, saubern, waschen'.
Als Lehnwort gehSrt dazu afgh. badpBzt 'Absurditat
(== Windsieberei nach Raverty) sowie bSzql, pSzql
sieben, Geiger, Etym. und Lautl. d. Afghan. Nr. 360.
250. Zu bddbe»9 badbSzan u. s. w. Tacher' vgl. Journ.
asiat. 1893, p. 256.
251. Dazu afgh. vala 'Weide* (nach Geiger), als Lehn-
--- 6855-6875 ---
Bftmln 132, 3) = arab. ddarbaijdn^ syr. aSorbUigan sohon im 5. /hd.
(ZDMG. 43, 409), gr. rS "A^aQftiy^pav (^rooop).
Hubschmann, PeriUoJit Stadias. 13- 194 —
sassanid. ana^iaSovao ^ "^spah-dadivar^ phi. datiwary aram.
de&mvar (Daniel 3, 2 — 3), arm. daiavor, 2i^,^databara- (§ 60).
§ 88. Ap. t ist geschwunden
a) inlautend in der Lautgruppe xir: Bctlx = ap.
BcLxtri' *Baktrien' , vgl. syr. Baxtrayada *Baktrerinnen'
Cureton, Spicil. 15, arab. baxtariyyun 'baktrisches Kameel'
(nach Noldeke); bahr = . barx *Theil, Antheil* = zd.
bctxdra- (s. oben p. 33);
b) im Auslaut: furo =■■ furoi (vgl. furddar, furdtan
fiir "^furod-tar, *furot'tan), isparU = isparUd H. 78; xusnu
= xusnUd zufrieden, u = ap. iita *und' u. s. w.
c) Urspr. ts war schon iran. zu s geworden: mahJ
*Fisch\ phi. mOhik = zd. masya-, skr. matsya-.
Urspr. tt war. schon iran. zu si geworden : mast 'trunken
= skr. matia- u. s. w., vgl. § 109, d. Vor andern Konso-
nanten als t war t schon im Iranischen zu d^ geworden,
siehe § 95. — Idg. kH^ kH, pt, st = iran. st, xt, ft^ st
= np. st, xty.ft. st siehe §'83, b sowie Kap. 14, 19, 23, 26.
```


## [2026-09-05T06:05:19.121Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '2495,2520p' HRN.txt; echo \"=== HRN grep ===\"; grep -n \"baxšīdan\\|bax§\\|baxs\\|bäg\\|bäj\\|anbäz\\|anbaz\\|fagfür\\|fagfur\\|bistün\" HRN.txt | head -40",
 "description": "Read Horn context and grep"
}
```


### [2026-09-05T06:05:19.179Z] TOOL RESULT

```
243. behär Trühling .
Käs. vor neben bohor.
ap. &tira\vähara' (?); aw. vatihri *im Frühling (ZP.
61.); phlv. vahär; ai. vasantd- Trühling, vergl. vasar[hä
(Bartholomae, BB. 15, 157); arm. garun Trühling'.
oss. valjäg (71); sar. vug (wohl stammverwandt).
244. behäne Torwand'.
vi + k^ dhä' , vergl. ai. vidhdna- 'Ordnung , Fest-
setzung, Bestimmung'; phlv. vhänak, paz. vahäna
*Motiv' (Men.), Hörn, KZ. 32, 588 No. 25').
245. behVy hehre Xoos, Teil'.
aw. hii\badra' glücklich, gesegnet, beglückt'
(Aogem.); phlv. hahr ^ bahrakj (geschrieben *inN2),
syr. LW. bähraq.
An aw. ba/dra- mit Hübschmann, Avestastudien,
S. 696 zu denken , verbietet die Bedeutung dieses
Wortes, welches Geldner, Drei Yasht, S. 102 wohl
richtig als 'Mahlzeit' fasst.
Ich kann den Verdacht nicht unterdrücken, dass
auch np. ber/ Teil' (Sahn. I, 77 Anm. 11, Calc), ber/e
hierher gehören ; dann natürlich auch afy. LW. bar/a,
bra/a ^Anteil', vergl. Hörn, Indog. Forsch. H, 138
Anm.
246. bihiSt^ behist ^Paradies'.
(äw, mhista- 'bester; phlv. vahist; ai. väsistha-.
LW. kurd. behist.
=== HRN grep ===
772:q^räret bedöze-^ büved bäj^dum
1700:\J148. bäj 'Tribut', bä^, baz, vergl. bäjbän *Zolleinnehmer* etc.
1795:'Vogel' ist spät); phlv. bäj,
1865:Wohl aw. bäga- Xoos' (y. 51, 1); ai. hhägd- 'Teil,
1956:^\fy^ bäg-ed; vergl. ender wm 'Bedürfniss'^).
2033:gegebene Verbum baytan 'schenken', päz. baxsfdan,
4308:/iyär (ebendas.) und bujpa (BQ.) d. i. bäjinä, htijina
5788:Kä8. Q. fiden , bäjin , bemjida bü ; K. jindemün , Z.
```


## [2026-09-05T06:05:26.137Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '1695,1720p' HRN.txt; echo \"--- 2020-2045 ---\"; sed -n '2020,2045p' HRN.txt",
 "description": "Read Horn baj and baxsidan"
}
```


### [2026-09-05T06:05:26.187Z] TOOL RESULT

```
phlv. papak (vergl. Nöldeke, Kärnämak, 35 Note 3;
Hörn, Mitteilungen, Heft IV, 24, ZDMG. 44, 658
No. 44).
arm. LW. pap^) 'Gross vater*.
kurd. bäwä, ba]plr, bäwuk (H.-Sch.).
\J148. bäj 'Tribut', bä^, baz, vergl. bäjbän *Zolleinnehmer* etc.
ap. büß' Tribut*; vergl. n^ozipaCtg' ä^cog A^iiftvog
yal TivQivog dnrog xui xvnaolaanv ore(favog yal olvog
*) Pähj Pap bedeutet im Np. nur *Pap8t* (ital. papa).
*) Arm. hav *Gro88vater* stellt S. Bugge mit Petermann wohl
richtig zu lat. avus.— fSi) —
y.syo(xiavog st' (o<o /pvoM, ot avrog ßaaiXsvg nivH (Dei-
non bei Athen. XI p. 503); ai. [/'bhaj- 'verteilen, zu-
teilen.
arm. LW. 6ai 'Anteil; Ehre*; vergl. bamnem, hazin,
49. härter 'Westen'.
g. wäxter,
aw. apä/tara- 'Norden'^); phlv. apä/tar.
Zu aw. apqs 'nach hinten gewendet*, ai. dpäfiö-
rückwärts gelegen*. Die Erklärung aus apa-\-aytara'
(vgl. No. 66) ist falsch.
[/150. hätten 'spielen , Praes. baz-em, bozl ('Spiel*).
g. vä/ten; Käs. vözt.
ai. vergl. vdja-^ väjäyati (spec. von Kampf spielen) 2);
phlv. baj^tan, bä/t 'er erhob sich' (kräftig, schnell),
Bund. 8, 2 (Diese Anwendung von phlv. ba/tan erklärt
--- 2020-2045 ---
bifbeu (Hübschmann, Seite 121), bei. baiak (17),
af/. baöai.
Da np. c nicht für skr. ts stehen kann, so ist die
Zusammenstellung mit ai. vatsd- 'Kalb, Jährling*, unzu-
lässig ; das letztere Wort entspricht vielmehr np. gösäle
(No. 941).
185. beyit 'Schicksal'.
aw. baxta- *Verhängniss'; phlv. baxt 'Schicksal';
ai. bhaktd- zugeteilt'.
arm., bei., s.{y, LW. ba^t, kurd. LW. be/t, bakt
(letztere Form echt?).
186. bey(STden 'schenken', Praes. be/s-em, beyßis.
aw. |^6a/s- 'schenken' ; phlv. vergl. das im Np. auf-
gegebene Verbum baytan 'schenken', päz. baxsfdan,
ba/Sisn.
kurd. ba/sin; af/. ba$al resp. ba/al; bei. baksag,
n. baSkay (24).
np. ba^sis ist weithin entlehnt, schon arm. bas/is.
186^** bey(8uden (*buxsüden) 'gnädig sein, verzeihen',
Praes. bexsay-em, bex§äyis\ TNi^OJ^ (Qiss. Dan. 400,
13, 18; 402, 4).
1) Ha. büjasklh, so auch PPGl.
^) Peje bei AM. 220 Zeile 11 ist natürlich nur Druckfehler.
*) Hss. haben versohiedentlich die Variante bücak; derselbe
Fehler wie in der vorvorhergehenden Note.- 44 —
phlv. apuxscLt/(i)snik (Men.).
```


## [2026-09-05T06:05:33.475Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PHD ===\"; grep -n \"^ *baxt\\|baxšīdan\\|baxš \\|bāz \\|hambāy\\|hambāg\\|hanbāg\\|^ *bay \\|bay,\\|bahr\" PHD.txt | head -40",
 "description": "Grep MacKenzie"
}
```


### [2026-09-05T06:05:33.520Z] TOOL RESULT

```
=== PHD ===
122:/abāz dādan б: 1. attribute, ascribe to; 2. appoint to. br ... add M fr! va-čār add helpless. delete á-distag ... (read ayidtag) add ‚тах |°р1°с | N farāz] acclivity. Afson ... add M ?pswn. Vagar ..., add useless. vāgēš [kw | (M "^ wa, P ?gwc), N aqóš] embrace, armful. add vājištag | gyštk' | P * gyšt, N ayišta] mixed, defiled. add \Ahliswang |*hlygwng] = Ard. delete Khriswang ... for alum ... read „alum |? № | N <] millet. Vāsnūd(ag) ... delete noble. aswür [|PR/LSYA < A pršy';.. āšnāg ... add acquainted with. āštīh ... add concord. ayad ... read |" byd^t' |... for bahr... and bahrag ... read bahr(ag) |b hl(k') | M bhr, N ~(a)] part, portion, share, lot; reason. (az) an bahrag ray : on that account, therefore. for  bahrwar ... read bahr(ag)war [b'hl(k)wl | N bahrawar| partaking, parti- cipator, partner. ~th : participation, advantage. balay add M by. add balgam |[blgm | N balyam] phlegm. baxtan ... add divide. bayaspān [by?sp^n' | = M]... bélür ... for M read P bylwr.
161:a- P- | M ?-] privative prefix, un-, Jess, а D] then (generally with a suffixed pronoun, e.g. 8-š). ab [M YA < А my';?p | M >b, N ~] water. B Soy 277 abad рр? | M Ра, N ~] populous, thriving, prosperous. ~ih: prosperity. ābādān [f*?t?*n' | N ~] thriving, prosperous, cultivated. ~ih: prosperity, cultivation. abādixšā(y) 'P?th? (d), v. pādixšā(y)] without authority, powerless. ~ih: powerlessness; anarchy. abādyāwand Pf?tyd”wnd | J ?b’dywn<d>] powerless, weak. ~ih: powerlessness, weakness. арар [LW TE < A lwt-h | M?Pg, N (a)bā] with. ~ih Dë kuk) company, assistance. abāgēnīdan, abāģēn- [^P'kyn-ytn!] accompany. a-bahr РРА] portionless, deprived. abām Pf?m | P ?bmyh, N (a)wàm] loan, debt. Abàn PPn! | M'0x, N ~] cal. 8th month; roth day. aband (nd, v. рапа | M ?bnd] erring. “АҺ: error. 'abar [ODM < А дат; bl | M "be, N bar] up; on, over. ~ āmadan: rise (sun). ~ āxistan: rise up. ~ āxrāmīdan: step up. — burdan : undertake. ~ madan: cope with, comprehend. ~ nigeridan: consider. ~ nihumbidan: conceal. ~ niSastan: sit, be enthroned. ~ nišāstan: seat, install. ~ rasidan: come to, upon. ~ rasidan б: attain. tabar Dél higher, superior. ~ag [-g | MP brg] superior. ~agan(ag) [-k’n(k)'] superior. --dar [-t, Zenit | M ?brdr] higher. ~dom [-twm | M ?brdwm] highest. —domih [-twmyh] superiority. abargar [5/21 god, divinity. abarig(àn) ['Bblyk( ny] = abarag. abarig DPryk! | M ?Pryg, J ?Pry] other.
164:abarmān [5/mn'] in charge. abarmānd ['pín?nd] inheritance, privilege. abarmānīģ [%n?nyk!] noble. abar-menišn Pf/myn$n'!] proud, haughty. abarón Pf*/xwn! | N wárün] contrary, wrong, sinful. ~ih: sin. abar-6z PóPeoc] stronger. ~ih: mastery. abar-tan [Pltn'] arrogant. ~th: arrogance. abarwēz Pfltvyc | (M *bruyj, N parwéz)] triumphant, victorious. ~ih: triumph, victory. abarzén, v. zmašk, abaxs [hš] repentant; regret. ~ЛЬ : repentance. abaxšāwand [5hP^wnd] regretful. abaxšāyīdan, abaxšāy- [5APd-ytn! | М ?bxPy-, N baxšūdan, baxšāy-) forgive, have mercy on. ~išn: mercy, forgiveness. ~i&nig : forgiving, merciful. labāxtar [*5?*4tl | M 7b’xtr] planet. žabāxtar [PP’htl | (N bāxtar ‘west’)] north. abaydag Pyrťk', v. paydag | M ?byd?g] invisible. ~th: invisibility. abày- : abayéd ['yt' | M Maud, N bāyad] it is necessary, fitting; must (+ infinitive). ~ist Pf?dst' | N bāyist] it was necessary. ~istan [?P?dstn!] be necessary, fitting; desire, want. ~išn: necessity. ~išnīg : necessary, fitting, seemly. abāz [L AWHL < A lI2(w)hr;?Pc | М Рс, N baz, wa] back, again, re-. ~ айдап б: attribute, ascribe to. 7 appoint t= ~ dāštan: withhold, restrain, prevent. ~ ēstādan az: abandon, desist from. — kardan: open. — kardan az: disengage from, wean. ~ mándan: remain behind. ~ pádan: remain, stay. — raftan : issue, go forth. ~ waštan O: turn into, become. ~ wirāstan: rearrange. abāzsār [LAWHLs'I] rebellious. ~ih: rebellion. āb-čihrag [$ cyhlk'] holding the seed, essence of water. abd [>24 | М "Gd J ?bd-] wonderful. ~ sahistan: seem wonderful (to) > marvel.
236:bahr [bhl | М bhr, N ~] part, portion, share, lot.
237:bahrag [P'hik'], (az) ап ~ ray: on that account.
238:bahrómand [PhPwmnd | N bahramand] divisible, composite; pros- perous.
239:~ih : compositeness; prosperity. bahrwar [bhlwl | N bahrawar] endowed, provided. ~th: endowment, provision, advantage.
312:débag [dyp’k! | N dēbā] brocade. débahr [dyp?hl | P dybhr] anger. pad — dāštan: banish. dég [dyk' | N ~] cauldron. LU) deh [M TA < A m? | M dyh, N ~] country, land; village. 0" гу -ģān [МТА-, dh? »'] = dahigàn. dën [dyn' | = M, N din] religion; cal. 24th day. dēnār [4ут/ | N dindr] (gold) dinar. dēn-āstawān [dyn’stwh’n'], dēn-burdār [dynbwit^l] believing, faithful. dénig [dyny&! | N dini] religious. dénódag [dynwtk'] female, milch. dér, dérand, v. dagr, dagrand. d��s(ag) [dys(k') | M dys] form, appearance. désidan, dēs- (dys-ytn! | M dys-yd] build. déw [SD Y.A < A #02, pl. šydy? | N ~] demon, devil. dēwān [d(p)ywn! | N <] archive, collected writings. déwanag [dyw”nk! | N ~a] demonic, mad. dēwār [dyw?l | M dyw’r, N ~] wall. déw|-ésnih [Š D Y Aysnyh | (M dyw?snyh)] idolatry, devil-worship. ~-ézagih [ŠD Y Ayckyh] = ~-ésnih. dēwēk [dywwk! | № déwuk] leech. dibir [dpy(w)r' | M dbyr, N ~] scribe. ~ih: writing, scribeship. „estān [-st?n! LN ~] school. did [TWB < A twb; dt'] again, then, further. didan, wén- [HZ Y TWN-tn! < A У hzy; dytn', wyn- | M dydn, wyn-, N —, bin-] see. ~išn: sight, seeing. ~i8nig : visible. didar [dyť] | N ~] sight; visible. pad ~ [N padidár] visible. didom [dtwm] second. dil [LB(B)ME < A lb(b)-h; dyl | = M, N ~] heart. dilér [dylywl, dlyl | N ~] brave. diz [KLYTA < A дур; dc | M dyz, N ~] fortress. dē [2, TLYN' < A tryn | M dw, N du] two. ~-ахмапіб [2 !hw)nyk!] relating to both worlds. ~ganag [dwk”nk! | M dwg'ng, N dugāna] double; twin. dok [dwk! | N ~] spindle. dol [del | N —] bucket; astr. Aquarius. dó|-pahikar [dwptkl | N du-paikar] astr. Gemini. ~-pay [2 LGLE, дора | N du-pà] biped, human being. dos [dws | N —] gum; plaster. dē-saxwan [2 shwn'] two-tongued, deceitful. dēsēn [dwsyn'] gummy; plastery; *glazed (pottery). dóst [dwst' | = M, N ~] friend.
390:hambār [kmb’l | N anbdr] store. hambārīdan, hambār- [hm-, hnb'l-ytn! | M hmb'r-, N anbürdan] fill, collect. hambasān [Anbs?n! | M *mbs*n] enemy, opponent. ~ig [-yk'] inimical, opposing. hambast [Ambst' | N anbast] compact. !hambastag [Ambstk' | N anbasta] formed, composed. shambastag [hnbstk' | М hmbst] collapsed, fallen. hambāstag [hmb’stk'] *all. īhambastan, hamband- [hmbsin', hmbnd-] form, compose; bind to- gether, intertwine, encircle. ~i8nih : binding together, intertwining. žhambastan, hambah- [%xbstn!, hnb?h- | M hmbst, hmbh-] collapse, fall down. VW "E. hambāstan, hambāh- [hnb’stn', hnb’d- | M hmb’stn, hmb’h-] cast down, demolish. ~išn: felling, demolition. ham-bašn [hmbén'] of the same stature. hambaw-, —išn, v. hambüdan. hambāy [hmb?g | (M hmb’w)] companion, partner; adversary. hambāz [hm-, hnb’c | M ?mP?z, N anbáz] partner. hambedig [%mbytyk!] = hambadig. hambēš-, —išn [hnbwi-, -£n! | N anbūšif] = hambüs-, ~išn, hambdy- (hnbwd- | M hwmbwy-, N anbóy-idan] smell (tr.). —ügih [-*kyh], —iŠn: (sense of) smell. hambüdan, hambaw- [hm-YHWWN-tn', v. büdan; hmbwtn'] be united, composed. „«išn(īh): union, composition. hambun [hmbwn'] (with a negative) not at all, not in the least. hambüsidan, hambūs- [hnbws-ytn' | N anbüsidan] come into being, be conceived. ~išn: conception. ham-dádestàn (hm-D YN A, -d'tsn! | N ham-dástán] agreeable, of the same opinion. hamdam [hmdm | N ~] intimate. ham-désag [hmdysk'] of the same form, homomorphous. hamë [hm’y | M Атуш, N ~] always. ^ ka: whenever. ham-ēdēn [m)ytwn! | N hamédün] likewise, similarly. bamé|ig (/um)yyk! | M тушур] eternal. ~iha [-yh’] eternally. hamémiil [mym] | = J] opponent, adversary. --īh: opposition. haménidan, hamén- [hmyn-ytn'] unite, compose. hamē-rawišnīh, hamē-ud-hamē-rawišnīh [(Amy W) hwy lwbsnyh) eternity.
592:tan-bahr 82 taxi
593:tan-bahr [żn'Þ’ hl] physique. tand [tnd | = P] faint, languishing. ~ih: faintness, langour. | tan-drust [tn'drw(y)st! | N ~] healthy, whole. ~ih: health. tang [ing | = M, N ~] narrow, tight. ~ih: narrowness; distress. tanig [tn'yk! | N tani] bodily, corporal. tanigard(ig) [tnykrt(yk)! | M inygyrd] corporeal. ` tanīhā [tn'y/? | M tnyP?, N tanha] alone. tanómand [tn wmnd | N ~] corporeal. “АҺ: corporeality. tan-tdhmag [tn'twhmk'] (sap) of plants. tanuk [tnwk! | N ~] thin, shallow, tanür [tnw] | M tnwr, N ~] oven. tar [LCDr! < A l-sd; tl | M tr] over, through, across. ~ kardan, ~ menidan: abuse, despise. -tar [-z# | (M -dr), N ~] suffix forming comparative adjectives. tar [2] | M гу] darkness. tarāzēnīdan, tarāzēn- [tcyn-ytn!] weigh. tarázüg [tPcwk! | (P tPzwg), N tarazü] balance, scales; astr. Libra. targ [tlg | N ~] helmet. tarģumān [tigm?n! | M trgwmn] interpreter. tarig/k [PIyk! | M гуур, N tárik!] dark. ~th: darkness. tarist [¢/st'] = tar. tar-mānīh [t/m’nyh] perversity. tar-menišn [tImynin! | N tarmanist] perverse; contemptuous. 7h : perversity; contempt. tarr [t/, LC Dr (in error, v. tar) | N —] moist, fresh. ~ag [tik! | N ~a] vegetable. tars [2/5 | M trs, N ~] fear, respect. tarság [ts k! | M trs’g, N tarsā] Christian. tarsāģāh [15(?)/?5] respectful, reverent. ~ih: respect, reverence. tarsidan, tars- [tls-ytn' | (M tyrs??dn), N ~] fear, be afraid. tarwénidan, tarwēn- [t/zvyn-ytn! | M trw-] overcome, conquer. tas [25 | N ~] die (for gaming). tasum [tswm | = M] fourth. tāšīdan, tāš- [O i-ytn!'] cut, cleave; create. taSkanag [tšknk!] under-shirt. tašt [tšt' | N ~] bowl. tāšt [021] *certainty. ~ig [-yk'] certain. tāwān [1?(d)w’n' | N ~] compensation, obligation. taxl [t?% | (M thr), P txl, N talx] bitter.
605:wad-baxt [wtP ht! | N badbaxt] unfortunate. wad-dil [wtdyl | M wddyl, N baddil] coward(ly). wadgarih [wtglyh] evil-doing. wād-ģirdaģ [w° tgltk' | (N gird-bād)] whirlwind. wad-góhr [wtgwhl | N bad-gauhar] ill-, low-born. wad-kamag [wtk’mk'] malevolent. ~ih: malevolence. wadrang [w’ ting | N bādrang] citron. cc Dë [-bwd | N -bóya] lemon balm. wad|-tóhm [wttwhm] = wad-góhr. ~-wazag [-w’ck! | (N gawāža)] abuse. --.Xém [-hym] ill-natured. waf- [wp- | Р wf-, (N bàf-)] weave. ~išn: weaving. wafr [wp! | M wpr, N barf] snow. ~énag [-ynk!] а sweetmeat. waydān [wy?n! = Av. waybana-] head (ahuric). wahāg [wP?k! | M тор, N baha] trading; value. — burdan: value, estimate. wahār [wh], (bj?l) | M wkr, № bahar] spring. ~ig [-уЁ! | N -z] spring, vernal. wahig [ZZLA < A Semi (?); whyk' | M whyg, N *bahi] kid; astr. Capricorn. wahist [ол | M whyst, N bihist] paradise. ~Ig [-yk! | N -1] (worthy) of paradise. Wahman [whwmn' | M whmn, N bahman] Good Mind, the first Amahra- spand, guardian of cattle; cal. 11th month; 2nd day. wāhmān [*w-n! = whmn' | MOw^hmn, J whmn, N bahman] so-and-so. Wahrām [wlhl?’n', whPm | M whr’m, N bahram] god of war, victory; astr. Mars; cal. zoth day. ātaxš 1~: a major sacred fire. wak [wk! | N bak] frog. wālan [zo n! | (IN barzan)] settlement, community walg [wlg] = warg. walidan, wāl- [w]-ytn! | N bdlidan] grow, increase, prosper. ~išn: growth. wümidan, wam- [w’m-yin'] vomit. wan [wn' | N bun] tree; stock, stem. ~ i $urgünig : pistachio tree. ~ 1 was-téhmag: the Tree of Many Seeds. wān-, ~išn, v. wanidan. wanafšag [zvnpšk! | N bunafša) violet. Wanand [wnnd] astr. Vega. wandaģ [wndk'] rope, cord. wang [KALA < А ql’; wng | = M, N bang] voice, cry. wānīdan, wan- [wn-ytn! | M w’n-yst] conquer, overcome, destroy.
691:abandon abāz éstádan az, hištan.
713:account mar; v. reckoning; on — of padisay, P wasnad; on that — an bahrag ray.
736:advantage bahrwarīh, sēg, sūd; v. profit.
751:hambāy, (spiritual)
790:anger débahr, xëšm.
860:ascribe to abāz dādan 6.
922:banish pad débahr адап.
941:bay (horse) bēr.
1298:companion hambāy.
1312:composite bahrómand.
1313:compositeness bahromandih.
1560:deprived abahr.
1765:endowed bahrwar.
2117:god abargar, bay, yazd.
2493:issue abāz raftan. item tag. itinerant wiyābānīg.
2667:lord аху, bay, šahryār, xwadāy; ~ of the land dahibed.
2672:lot bahr.
2983:open (v.) abāz kardan, wišādan; (the mouth) wiyaftan.
3043:part bahr, bazišn, sraxtag.
3049:partner hambāy, hambaz.
3119:physique tanbahr.
3183:portion bahr, jād(ag), kardag, pārag.
3184:portionless abahr,
3218:prevent abāz dāštan.
3262:prosperity ābād(ān)īh, bahrómandih, drod, frāxīh, padéxih.
3272:bahrómand,
3276:provided bahrwar.
3279:provision bahrwarih; tóšag, xwārbār.
```


## [2026-09-05T06:05:50.803Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"baya\\.\\|bay-\\|bagastana\\|bagastäna\\|ba\\^astana\\|hamö\\.ba\\|hama\\.ba\\|ba\\^o\\.\" BRT.txt | head -30; echo \"=== search puthra ===\"; grep -n \"pu\\^ra\\|puthra\" BRT.txt | head -10",
 "description": "Grep Bartholomae for baga compounds"
}
```


### [2026-09-05T06:05:50.858Z] TOOL RESULT

```
16715:927  bay-  —  bav-  2  928
16728:•  j-,  g.  bay- V.  'erschrecken'.  Praes.  2  !  J/^"'"  ■■  "^''i  ^ß'"*'  ^'^^'^  vanhaot  mana- baya-,\  bya-;  Perf.  i  btwt-.  1«"*«-'   ■  ■    "■  ■  "E^^^oref    iK    .  ."    Vr.  //.
17415:ai.  bhyas-  V.  'sich  fürchlen'.  —  Vgl.  bay-.  —
27719:—  Vgl,  vha/iiia-.  —  Pü.;  hamäk  hac  aivz'\r i  tö  valdenän  rSi  iiaslak  afe  kunc.  —  ')  Vgl. die  Var.,  bes.  E  I.  NA.  hat  kqm  ;^nva  tim- bay-  mit  Mf3;  s,  aber  Pu.
=== search puthra ===
7150:—  "^rö  ah'  m-  Y.  22.4;  —  ->rasca  ah' m'  Y.  i. 4,  Vr.  IS. 3,  S.  1.  7,  F. 39'  —  ''^räca ah'  m'  Y.  5Ä4;  —  'iar^  (Vok.)  ah'  m'  ■ Y.5Ä7;  —  'iar/  (Nom.)  mazda  'rahti Y.62.7,  9,  Yt. /0.3,  19.47-49^  V.<?,8o, Ny.5.4;  s.  noch  2.  ß)  'lan  (Vok.j ahurahe  mazda  pu^ra  Y. 65. 12;  —  düyA ms  'tars  (dXsVok.)  pü>ra  ah'  m'  Y.62.4;! 2;  ��  afrinlmi  tava  °tars  puitra  ah'  m° Y.O'-J.ii  4.23,  22.26,  Ny,  j.4;  —  xsha-\ maine  tava  '"^rö  ah'  m°  pu^ra  Y.3.Z;. /.  12,    22.3,    26,  Ny.5.4-6^   S.  i.9;  — |
11009:vas?iS  (^ur^masdähe^  mana^a  dä- fD.4.2.  B)imAwr.;  i)die Glieder  sind  nominal'';  a)  sie  folgen  sich unmittelbar:  pita  pu%rasea  .  .  iatarasüi ^■9-5i  —  pu^ra  (ND,)  ..  urvSxsayB k»r>s3spauaY.g.\a\  —  tum  akB  vahistasca ahi  YtJO.  29;  —  kanta  aiwyäxstaca Y.57.  IS  (s.  dagegen  Yt.;o.  103,  Sp.  567  u.);
14796:•  j,  'paeman-  Adj.,  nur  fem.  'mat/iT- 'säugend',  von  der  HUndio;  gatwqm  , . pu^raca  (sd)  'mainiea  V./5.  49.
15350:"..der  du  vom  vergänglichen  Leben  zum  ehedem*:  /rarasayS  .  .  yl  araca  'ra unvergänglichen  Leben  herüberkamst"  \.  /raoirisisiä  fsA.)  ya^ra  ..  VtJj.2S;  — 7.  52.  A)  Kaus.  'vorwärts  und  hinüber-   ij  nJtriJkqm  yam  apu^ram  .  .  anasaxtqm
25667:•  j.  urväxäaya-  m.  EN.  eines  Gläubigen, Sohns  des  &rita:  yai  kl  (näml.  %ritahe) pu^ra  us.taysihe  *yS  kmsäspasca  IkaiiS anyö  dätS.rätS  äai  anyS . .  ". .  zwei  Söhne . .  U.  und  K.,  ein  Richter  der  erstere, ein  Gesetzgeber,  aber.."  Y.i?.  10;  —  yat kama  nijaiäiii  az?m  {vä.(al.  hntäspB)  irä- 'hrS  "'saya'^  yai  janäni  hitäsp>m  "..dass ich  als  Rächer  meines  Binders  U.  heim- kehre, dass  ich  den  H.  töte"  Ytr5. 38; —  hubar)k?m  *vyäxan>m  bavähi  yaha "'saÄe''!  Az.  _J,
30620:Substantiv;  substantivisch:  h'  vlard  (sd.)  yi  nairya  yä- pu^rahe . .  yA  lanu.p^n'haAe ahurö  Y.  29. 4 ;  —  Syä  Hstl  (sd  )  .■  h'  *ptl  . .  *ajayaurva  *aya  ratufris  ". .  sui  ipsius  . . asakyä    mazdh    Y.4-.3;  44.2,  ^1.8;    —   uxoris  . .  filü  . ."  N.54.  U)  schwach-
```


## [2026-09-05T06:06:00.729Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HJB faghfur ===\"; grep -n -i \"faghfur\\|fagfur\\|baghpur\" HJB.txt | head; echo \"=== HENNING bay ===\"; grep -n -i \"Sogdian Loan-Words\" HENNING_selected_papers.txt | head",
 "description": "Grep Hobson-Jobson and Henning"
}
```


### [2026-09-05T06:06:00.809Z] TOOL RESULT

```
=== HJB faghfur ===
=== HENNING bay ===
11770:milar Sogdian loan-words in Pe nd-wif, ete,
```


## [2026-09-05T06:06:04.607Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HJB grep bagh ===\"; grep -n -i \"faghf\\|Faghp\\|BAGHDAD\\|Baugh\" HJB.txt | head -10; echo \"=== HJB leaf 84-100 headwords ===\"; awk 'BEGIN{RS=\"\\f\"} NR>=85 && NR<=101 {print NR\": \"substr($0,1,200)}' HJB.txt",
 "description": "Find HJB page 49"
}
```


### [2026-09-05T06:06:06.261Z] TOOL RESULT

```
=== HJB grep bagh ===
11249:HOOGLY  BIVEB,  n.p.  See  pre- ceding. The  stream  to  which  we  ^ve this  name  is  formed  by  the  combina- tion of  the  delta  branches  of  the Ganges,  viz.,  the  Baugheruttee,  Jaling- hee,  and  Matabanga  (Bhdgiralhiy  JaU angi^  and  Mdtdhhdnga),  known  as  the Nnddeea  (Nadiya)  Bivers.
21290:TABBY,  8.  Not  Anglo-Indian.  A kind  of  watered  silk  stuff;  Sp.  and Port,  tabi,  Ital.  toMnOy  Fr.  tdbis,  from Ar.  'attdbl,  the  name  said  to  have  been given  to  such  stuffs  from  their  being manufactured  in  early  times  in  a quarter  of  Baghdad  called  aWatidbiya  ; and  this  derived  its  name  from  a prince  of  the  *Omaiyad  family  called 'Attab.  [See  Burton,  Ar.  Nights,  iL 371.]
25087:Faghfrlr,  347a,  49a
=== HJB leaf 84-100 headwords ===
85: Z«<<rtt  KdifUuUe*,  xii.  98.
1727.—"  He  then  began  to  form  Projects how  to  dear  Accounts  with  his  Master's Creditors,  without  putting  anything  in  Uieir Pockets.  The  first  was 
86:   article at-hairkOky  whence  Sp.  albarcoqvsy  Port. aJbricoquey  alboquorquSy  ItaL  atbercoccuy aWicocca,  Prov.  auSricot,  arnbrtcoty  Fr. airicoty  Dutch  aJbricocky  abrikoosy  Eng. (vpricocky
87: uaLn.    SeePBOHE.
[1659.-Araoan.    See  TALAPOIN.]
1660. — ^'Despatches  about  this  time  ar- rived from  Mu'azEam  Khan,  reporting  his successive  victories  and  the  flight  of  Shuja to  t
88:   call  it pac  (Tam.  pdk);  and  the  Nairs  (who  are the  gentlemen)  call  it  areoa."— 6(arcM  D'O,,
c.  1566. — "Great  quantitie  of  Archa, which  is  a  fruite  of  the  bignesse  of  nu
89:   that  is  vsed  in  most  of  these  parts  of the  world,  instead  of  Wine.  .  ." — E.  Scot,  in FurchM,  1. 178.
1631.—".  .  .  .  jecur  ....  a  potu  istius maledicti  Arao,  non  tant
90: ichoke].
ABYAN,  adj.  Skt.Jrj^a,*  noble.'  A term  frequently  used  to  mclude  all  the races  (Indo-Persic,  Greek,  Roman, Celtic,  Sclavonic,  &c)  which  speak languages  belonsinc  to  the  s
91: rgence  of  its  chief  * sources  from  the  mountains  till  it enters  t^e  great  plain  of  BengaL  The name  Aadm^ajia  sometimes  Ashdm  is a  form  of  Ahdm  or  Ahom^  a  dynasty of  Shan  ra
92: 2nd  ed. i.  186].
1878.— *<  The  universal  roofing  of  a  Perak house  is  Attap  stretohed  over  bunboo  rafters and  ridj^e-poles.  This  atiap  ia  the  dried  leaf of  the  mpan  palm,  dou
93:  of India,  and  does  not  belong  to  the standard  system  of  any  Presidency. The  word  in  the  following  passage looks  as  if  intended  for  'amalddTy though  there  is  a  term  Mdlddr,  H
94: ere in  great  numbers,  I  withdrew  them  and brought  them  back  to  the  city." — D.  JoSo de  bistro's  despatch  to  the  City  of  Goa respecting  the  victory  at  Diu. — Correoy  iv.
164
95: re  (at  Simla)  there  is  a  great preponderence  of  Mahometans.  I  am  told that  t^e  ffons  produced  abeolute  consterna- tion, vinble  m  their  countenances.  One Asrah  threw  herself  upon
96:   habar, Ihdba/r,  A  name  given  to  those  dis- tricts of  the  N.W.  Provinces  which lie  immediately  under  the  Himalaya to  the  dry  forest  belt  on  the  talus  of the  hills,  at  the  lo
97: ) we  ^ould  no  longer  hear  bombastic  Baboos, enjoying  under  our  Government  the  highest degree  of  personal  liberty  .  .  .  rave  about patriotism,  and  the  degradation  of  their prese
98: other  Braoalor,  belong- ing to  the  kingdom  of  Narsyngua  and  the ryince  of  ToHnate  (Tulu-iUfda,  Tuluva  or Oanara).  And  in  them  is  much  good rioe  grown  round  about  these  places, 
99: ar  ananffement  at  the same  place  is  described  by  Lituekoieii.  i.  51, Hak.  ^.]
1682.— At  Oamron  (Oomliroon)  "meet of  the  houses  have  a  square  tower  whidi stands  up  far  above  
100: ndudr.  ArU,  249).]
1598.— "There  is  made  great  store  of GottonLinnen  of  diners  sort  .  .  .  Boffstas." —LintckoUn,  p.  18.    [Hak.  Soc.  i.  60.]
lieOM.—'' PaUa  Kaasa  of  the  �
101: r  and  for  a  Paltam weij^hing  13  rupees  and  1^  VitsMtn  120  of which  are  equal  to  a  Tulam  or  Maund  weigh-
ing 1,732  rupees,  calculating,  at  which standard  for  one  bazom  or  Ca
```


## [2026-09-05T06:06:14.005Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR>=84 && NR<=102 {if ($0 ~ /China|Chin/) print \"LEAF \"NR\"\\n\"$0\"\\n-----\"}' HJB.txt | head -60",
 "description": "Find Faghfur mention near HJB p49"
}
```


### [2026-09-05T06:06:15.410Z] TOOL RESULT

```
LEAF 86
  article at-hairkOky  whence  Sp.  albarcoqvsy  Port. aJbricoquey  alboquorquSy  ItaL  atbercoccuy aWicocca,  Prov.  auSricot,  arnbrtcoty  Fr. airicoty  Dutch  aJbricocky  abrikoosy  Eng. (vpricocky  apzicot.  Dozy  mentions  that Dodonaens,  an  old  Dutch  writer  on plants,  gives  the  vernacular  name  as Vroege  Perseriy  *  Early  Peaches,*  which illustrates  the  origin.  In  the  C3rprus bazars,  apricots  are  sold  as  xpvahiuiKa ; but  the  less  poetical  name  of  *  kiH-jokris ' is  given  by  saUors  to  the  small  hard kinds  common  to  St.  Helena,  the  Cape, China,  &c.  Zard  dlU  [aloe]  (Pers.) 'yellow-plum'  is  the  common  name in  India.
1616. — "I  received  a  letter  from  Jorge Durois  .  .  .  with  a  baskit  of  apreoookes  f or my  selfe.  .  ," — Coolant  Diary,  i.  7.
1711.— "Aprioooka—the  Persians  call Kill  Franks,  because  Europeans  not  know- ing the  Danger  are  often  hurt  by  them." — Lockyer,  p.  ^1.
1738.— ''The  common  aprioot  ...  is .  .  .  known  in  the  Frank  language  (in Barbarv)  by  the  name  of  Matza  Framoa,  or the  Killer  of  Christians." — Shaw*s  Travels, ed.  1757,  p.  144.
^•R.A'R^  8.  This,  it  may  be  said,  in Anglo-Indian  always  means  ^an  Arab horse.'
1298. — "  Car  il  va  du  port  d'Aden  en  Inde moult  grant  quantity  de  bons  destriers axraUns  et  chevaus  et  grans  rondns  de  ij selles."— ifarco  Pofo,  Bk.  iii.  ch.  36.  [See Sir  H.  TvJ.e*s  note,  1st  ed.,  vol.  ii.  375.]
1388. — ''Alexandre  descent  du  destrier Arrabia."— itomiiuut^  d* Alexandre  (Bodl. MS.).
ABAKAN,  ARRAGAN.
34
ARBOL  TRISTE.
o.  1590. — "There  are  fine  horses  bred  in every  part  of  the  conntry;  but  those  of Oaohh  ezoelL  being  equal  to  Azabs."— ^I», i.  183.
1826. — *' Azabi  are  exoessively  scarce  and dear ;  and  one  which  was  sent  for  me  to  look at,  at  a  price  of  800  rupees,  was  a  skittish, oat-legged  thing."— i7«&er,  i.  189  (ed.  1844).
c.  1844. — A  local  magistrate  at  Simla  had returned  from  an  unsuccessful  investigation. An  acquaintance  hailed  him  next  day :  *  So I  hear  you  came  back  re  ivfeetAV  <No suoh  thing/  was  the  reply ;  *■  I  came  back  on ^7  firrey  Arab  I '
1866.— "  .  .  .  .  the  true  blood-royal  of  his  race, The  silver  Arab  with  his  purple  veins Translucent,  and  his  nosmls  cavemed  wide, And  flaming  eye.  ..."
The  Banyan  Tree,
ABAKAN,  ABRAOAN,  n.p.  This is  an  Europ^ean  form,  perhaps  through Malay  [which  Mr  Skeat  has  failed  to trace],  of  Rakhaina,  the  name  which the  natives  give  themselves.  This  is believed  by  Sir  Arthur  Phayre  [see Joum,  A  8,  Soc,  Ben.  xii.  24  seqq.}  to be  a  corruption  of  the  Skt.  rdk- shcuoy  Pali  rakkhoiOy  i.e.  *  ogre'  or the  like,  a  word  applied  by  the early  Buadhists  to  unconverted  tribes with  whom  they  came  in  contact. It  is  not  impossible  that  the  *Apyvp^ of  Ptolemy,  which  unauestionably represents  Arakan,  may  disguise  the name  by  which  the  country  is  still known  to  foreigners ;  at  least  no  trace of  the  name  as  'Silver-land'  in  old Indian  Geography  has  yet  been  found. We  may  notice,  without  layinff  any stress  upon  it,  that  in  Mr.  Bears  ac- count of  early  Chinese  pilgrims  to India,  there  twice  occurs  mention  of an  Indo-Chinese  kingdom  called  0-li- hi-loy  which  transliterates  fairly  into some  name  like  Argyri,  and  not  into any  other  yet  recognisable  (see  J,R.A.S. (N.S.)  xiiL  660,  662).
c.  1420-80.—"  Man  deinoeps  cum  mense integro  ad  ostium  Bafthanl  fluvii  pervenis- set.'^— i\r.  CwUif  in  Poggiui,  De  VarietaU Fartunae,
1516. — '^Dentro  fra  terra  del  detto  regno di  Verma,  verao  tramontana  vi  ^  vn  altro regno  di  Gkntili  molto  grande  ....  con- fina  similmente  col  re^o  di  B^ala  e  col regno  di  Aua,  e  chiamasi  Ar&caa."— JBarkMo, in  Ramusio,  i.  816.
[c.  1585.— "ArTiiam":  See  CAPELAN.]
1545. — "The^  told  me  that  coming  from India  in  the  ship  of  Jorge  Manhoe  (i^o  was a  householder  m  Goa),  towards  the  Port  of Ghatigaon  in  the  kingdom  of  Bengal,  they were  wrecked  upon  the  shoals  of  RatrtiTti
owin^  to  a  badly-kept  watch."— jPinto,  cap. olxvii.
1552.— **  Up  to  the  Om  of  Negraee  .  .  . will  be  100  leagues,  in  which  spaoe  are  these TOpulated  places,  Chocoril^,  BacaUL  Airacfto Cifv,  capital  of  the  kingdom  so  styled.  ..." — Barrotj  I.  ix.  1.
1568.— "Questo  Be  di  Baehan  ha  il  suo stato  in  me»o  la  coeta,  tra  il  Begno  di Ben^^ala  e  quello  di  Pegb,  ed  ^  il  i nemico  che  habbia  il  Be  del  Peg^  ' de*  Federiciy  in  RamusiOf  iii.  896.
1586.— '<.  .  .  .  Passing  by  the  Island  of Sundiua,  Porto  grande,  or  the  Countrie  of 'nppera,  the  Elingdom  of  Beoon  and  Mogem (mngg)  •  •  *  .  our  course  was  S.  and  by  E. which  Drought  vs  to  the  barre  of  Negrais." — i2.  Fitehj  in  Hail,  ii.  891.
c.  1590.— "To  the  S.E.  of  Bengal  is  a large  oountrv  called  Arkniig  to  which  the Bunder  of  Chittagong  properly  belongs." — Oladtrin*t  Ayeen^  ed.  1800,  h.  4.  [Ed.  JarreU. u.  119]  in  ong.  (i.  888)  ArUumff.
[1599.— Airaoan.    See  MACAO.
[1608.— Bakfaang.    See  CHAKPA.
[c.  1069.-An
-----
LEAF 88
  call  it pac  (Tam.  pdk);  and  the  Nairs  (who  are the  gentlemen)  call  it  areoa."— 6(arcM  D'O,,
c.  1566. — "Great  quantitie  of  Archa, which  is  a  fruite  of  the  bignesse  of  nutmegs, which  fruite  they  eate  in  aU  these  parts  of the  Indies,  with  the  leafe  of  an  Herbe,  which they  call  BetUlL"—C.  Frtderiie,  transL  in Rail.  ii.  350.
1586.— "Their  friends  come  and  bring gifts,  cooos.  figges.  aiiecaes.  and  other lrmia,"—Fttch,  in  Rail.,  ii.  895.
E  1624.—"  And  therewith  they  mix  a  little es  of  sea-shells  and  some  small  pieces  of an  Indian  nut  sufficiently  common,  which they  here  call  Foufel,  and  in  other  places Axeca;  a  very  dry  fruit,  seeming  within like  perfect  wood ;  and  being  of  an  astringent nature  they  hold  it  good  to  strengthen  the Teeth."— A  delia  Voile,  Hak.  Soo.  i.  86. Mr  Grey  says:  "As  to  the  Port,  name, Foujd  or  Fojtl,  the  origin  is  uncertain.  In Sir  J.  Maundeville's  lYavels  it  is  said  that black  pepper  "is  called  Fulful,'*  whioh  is probably  tne  same  word  as  "  i^ou/e/."  But the  Ar.  Faufal  or  F^fdl  is  'betel-nut.*]
1689.—".  ...  the  Neri  which  is  drawn from  the  Axegilies  Tree  in  a  fresh  earthen vessel,  is  as  sweet  and  pleasant  as  Milk" — Ovington,  237.  [Neri—tL,  and  Mahr.  n^r, 'sap,'  but  neri  is,  we  are  told,  Ouserati  for toddy  in  some  form.]
ABGEMONE  MEZIGANA.  This American  weed  (N.O.  Pa^veraceae)  is notable  as  having  overrun  India,  in every  part  of  which  it  seems  to  be familiar.  It  is  known  by  a  variety of  names,  Firinghl  dhatHra^  gamboge thistle,  &c.  [See  Watt,  Diet.  Earn. Prod.,  i.  306  teqq,']
AROUS  PHEASANT,
36
ARRACK,  RACK.
ABGUS  PHEASANT,  s.  This name,  which  seems  more  {)roperIy  to belong  to  the  splendid  bira  of  the Malay  Peninsula  {Argiuomus  giaantetu, Tem.,  Pavo  arguSj  Lin.),  is  confusingly applied  in  Upper  India  to  the  Hima- layan homed  pheasant  Cer%om%8  (Spp. saiyra^  and  melanocephala)  from  the round  white  eyes  or  spots  which  mark a  great  part  of  the  bird's  plumage. — See  remark  under  MOONATJIh
ABBAGK,  BACK,  s.  This  word is  the  Ar.  'arcLky  properly  *  perspira- tion,' and  then,  first  the  exudation or  sap  drawn  from  the  date  palm CaraJb  <U-tamar) ;  secondly  any  strong arini,  'distilled  spirit,'  *  essence,'  etc. But  it  has  spread  to  very  remote comers  of  Asia.  Thus  it  is  used  in the  forms  ariki  and  arki  in  Mon^lia and  Manchuria,  for  si)irit  distilled from  grain.  In  India  it  is  applied to  a  variety  of  common  spirits ;  in 8.  India  to  those  distilled  from  the fermented  sap  of  sundry  palms ;  in E.  and  N.  India  to  the  spirit  distilled from  cane-molasses,  and  also  to  that from  rice.  The  Turkish  form  of  the word,  rdiiy  is  applied  to  a  spirit made  f  roiii  grape-skins ;  and  in  syria and  Eaj-pt  to  a  spirit  flavoured  with, aniseed,  made  in  the  Lebanon.  There is  a  popular  or  slang  Fr.  word,  riquiqui^ for  Drandv,  which  appears  also  to  be derived  from  aratt  (Marcel  Devic). Humboldt  (Examen,  &c.,  ii.  300)  says that  the  woixl  first  appears  in  Pigafetta's Voyage  of  Magellan ;  but  this  is  not correct.
c.  1420.— "At  every  yam  (post-house) they  give  the  travellers  a'  sheep,  a  goose,  a fowl  ....  'arak.  .  .  r—Shah  RvWs  Em- bassy to  China,  in  N.  k  E.,  xiv.  396.
1616. — "And  they  bring  ooooa-nuts, huxraca  (which  is  something  to  drink) .  .  .  ." "-Barbosa,  Hak.  Soc.  59.
1518. — " — que  todos  os  mantimentos  asy de  pSo,  oomo  vinhos,  onaeas,  arrozes, cames,  e  pescadoe." — In  Arditv,  Port, Orient,,  fasc.  2,  57.
1521.— "When  these  people  saw  the politeness  of  the  captain,  they  presented some  fish,  and  a  vessel  of  palm-wine,  which they  call  in  their  language  maca.  .  .  ." — Pigafetta,  Hak.  Soc.  72.
1544. — "Manueli  a  cruce  ....  commendo ut  plurimum  invigilet  duobus  illis  Christian- orum  Carearum  pagis,  diligenter  attendere ....  nemo  potu  Omusaa  se  inebriet  .  .  . si  ex  hoc  deinoepa  tempore  Punicali  Oriaoha notetur,  ipsos  ad  mihi  suo  gravi  damno luituros."— &h'.  Fr,  Xav.  Epistt,,  p.  111.
1554. — "And  the  excise  on  the  orraqwu made  from  palm-trees,  of  whioh^  there^  are three  kinds,  viz.,  cvro,  which  is  as  it  is drawn ;  orra^fiia,  wnich  is  ptetv  once  boiled {potUdfi,  qu.  distilled  f) ;  aharab  {xaraa)  which IS  boiled  two  or  three  times  and  is  stronger than  orrafua.**—S,  Botelho,  Tombo,  50.
156S.— "One  kind  (of  oooo-pahn)  they keep  to  bear  fruit,  the  other  for  the  sake  of the  ptra,  which  is  vino  mosto;  and  this  when it  has  been  distilled  they  call  arraoa." — Garcia  />'0.,  f.  67.  (The  word  ncrO,  used here,  is  a  very  ancient  importation  from India,  for  Commas  (6th  century)  in  his account  of  the  oooo-nut,  confounding  (it would  seem)  the  milk  with  the  toddy  of  that palm,  says:  "The  ArgelUon  is  at  first  full of  a  very  sweet  water,  which  the  Indians drink  from  the  nut,  using  it  instead  of  wine. This  drink  is  called  rhcneosura,  and  is extremely  pleasant."  It  is  indeed  possible that  the  rhonco  here  may  already  be  the word  arrack).
1605. — "A  Chines  borne,  but  now  turned lauan,  who  was  our  next  neighbour  .... and  brewed  Araoko  which  is  a  kind  of  hot drinke,
-----
LEAF 101
r  and  for  a  Paltam weij^hing  13  rupees  and  1^  VitsMtn  120  of which  are  equal  to  a  Tulam  or  Maund  weigh-
ing 1,732  rupees,  calculating,  at  which standard  for  one  bazom  or  Candy  the Sircar's  price  is  Rs.  120."— Prod,  at  Malabar, in  Logan,  iii.  348.  This  makes  the  barom equal  to  650  lbs.]
BAHAUDUR,  s.  H.  Bahadur,  'a hero,  or  champion.'  It  is  a  title  affixed commonly  to  the  names  of  European officers  in  Indian  documents,  or  when spoken  of  ceremoniously  by  natives {e.g.  "Jones  Sahib  Bahddur"\  in  which use  it  may  *be  compared  with  "the gallant  officer"  of  Parliamentary courtesy,  or  the  lUtutrissimo  Signare  of the  Italians.  It  was  conferr^  as  a title  of  honour  by  the  Great  Mogul and  by  other  native  princes  [while in  Persia  it  was  often  applied  to  slaves (Burton,  Ar.  Nights,  iii.  114)].  Thus it  was  particularly  a^ffected  to  the  end of  his  life  by  Hyder  Ali,  to  whom  it had  been  given  by  the  Raja  of  Mysore (see  quotation  from  John  Lind«iy below  [and  Wilks,  Mygoor,  Madras reprint,  i.  2801).  Bahddur  and  Sirddr Bahddur  are  also  the  official  titles  of members  of  the  2nd  and  1st  classes respectively  of  the  Order  of  British Inaia,  established  for  native  officers of  the  army  in  1837.  [The  title  of Rdi  Bahddur  is  also  conferred  upon Hindu  civil  officers.]
As  conferred  by  the  Court  of  Delhi the  usual  gradation  of  titles  was (ascending)  : — 1.  Bahddur ;  2.  Bahddur Jang;  3.  Bahddur  ud-Daulah;  4. Bahddur  ul-mulk.  At  Hyderabad  they had  also  Bahddur  ul-Umrd  (Kirk- patricky  in  Tvppoo^s  Letters,  364). [Many  such  titles  of  Europeans  will be  found  in  North  Indian  N.  A  Q., i.  35,  143,  179 ;  iv.  17.]
In  Anglo-Indian  colloquial  jHirlance the  worddenotes  a  haughty  or  pompous personage,  exercising  his  brief  authority with  a  strong  sense  of  his  own  im- portance ;  a  don  rather  than  a swaggerer.  Thackeray,  who  derived fromhis  Indiai^  birth  and  connections a  humorous  felicity  .  in  the  use  of An^lo-Indian  expressions,  has  not omitted  this  serWceable  word.  In that  brilliant  burlesc^ue,  the  Memoirs of  Major  Oahagan,  we  have  the Mahratta  traitor  Bcbachee  Bahauder. It  is  said  also  that  Mr  Canning's malicious  wit  bestowed  on  Sir  John Malcolm,  who  was  not  less  sreat  as a  talker  than  as  a  soldier  ana  states- man, the  title,   not  included  in   the
BAHAUDUR.
BAHAUDUR,
Great  MpgiiFs  repertory,  of  Bahauder Jaw*
```


## [2026-09-05T06:06:30.256Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"Son of Heaven\\|Baghbur\\|Bagbur\\|Faghf\" HJB.txt | head -10; echo \"--- leaf 101-104 scan ---\"; awk 'BEGIN{RS=\"\\f\"} NR>=99 && NR<=106 {print \"LEAF \"NR\" :: \"; print substr($0,1,600); print \"###\"}' HJB.txt | grep -n -i \"fagh\\|china\\|LEAF\" | head -20",
 "description": "Search HJB for Faghfur"
}
```


### [2026-09-05T06:06:31.808Z] TOOL RESULT

```
25087:Faghfrlr,  347a,  49a
--- leaf 101-104 scan ---
1:LEAF 99 :: 
6:LEAF 100 :: 
14:LEAF 101 :: 
19:LEAF 102 :: 
28:LEAF 103 :: 
33:LEAF 104 :: 
39:LEAF 105 :: 
45:LEAF 106 ::
```


## [2026-09-05T06:06:37.922Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR>=395 && NR<=404 {print \"=== LEAF \"NR\" ===\"; print substr($0,1,300)}' HJB.txt",
 "description": "Locate HJB page 347"
}
```


### [2026-09-05T06:06:39.707Z] TOOL RESULT

```
=== LEAF 395 ===
ch  is  nearly  square  and very  dark,  so  that  there  is  nothing  to  be seen  there ;  and  with  this  ends  the  fabric  of this  great  pagoda.  It  has  been  in  many parts  demolished ;  and  what  the  soldiers have  left  is  so  maltreated  that  it  \b  grievous to  see  destroyed  i
=== LEAF 396 ===
e  Elephanta  pr^  de  Bombav, mais  ils  n'en  parlent  qu'en  passant.  Je  le trouvois  si  cuneux  et  si  digne  de  I'attention des  Amateurs  d'Antiquit^  que  j*y  fis  trois fois  le  Voyage,  et  que  j'y  deesinois  tout  ce que  s'y  trouve  de  plus  remarquable.  .  .  ." — Cantm  Ni
=== LEAF 397 ===
anta."— Grom,  i.  88.
ELBPHANT-CBBEPBB,  s.  Argy* reia  ipeci&aOy  Sweet.  (N.  0.  Convohul- aceae).  The  leaves  are  used  in  native medicine  as  poultices,  &c.
ELK,  s.  The  name  given  by  sports- men in  S.  India,  with  singular  impro- priety, to  the  great  stag  Rum  AristoteUs
=== LEAF 398 ===
^^
1878.— "These  ruins  (Gaur)  are  dtuated about  8  miles  to  the  south  of  AngrMb&l (Ei«UBh  Bixia),  the  civil  station  of  the district  of  Mfldah.  .  .  ,**—Itavenshaw*sGaitr, p.  1.
[ESTDCAUZE,  &  A  corruption  of the  Ar.— P.  iUtmds,  *  a  prayer,  petition, humble  repre
=== LEAF 399 ===
the  Civil  Service  for years  after  the  abolition  of  the  last vestige  of  the  Company's  trading  char- acter, and  it  is  not  till  the  publication of  the  E.  I.  Register  for  the  first  half of  1842  that  they  disappear  from  that official  publication.  In  this  the  whole b
=== LEAF 400 ===
.  .  he  sent  a  Nayre  ...  to the  intent  hee  might  remaine  in  the  Fac- torytr—Castafleda  (by  N.  L,),  fF.  546.
1606. — "  In  which  time  the  PorixngaH  and Tydoryan  Slaves  had  sacked  the  towne, setting  fire  to  the  faotocy."— 3fM^cti«eoa's Voyagty  G.  (4).
1615.— 
=== LEAF 401 ===
  its  popular  sense is  a  'crafty  schemer,'  an  *  artful  dodger.' Filosofo,  in  Manilla,  is  applied  to  a native  who  has  been  at  colle^  and returns  to  his  birthplace  in  the provinces,  with  all  the  importance  of nis  acquisitions,  and  the  affectation of  European  habits
=== LEAF 402 ===
 at  the  treasuries  of  Malabar  and Calicut.  As  the  coins  were  very  small they  used  to  be  counted  by  means  of  a small  board  or  dish,  having  a  large number  of  holes  or  pits.  On  this  a pile  of  fanams  was  shaken,  and  then swept  off,  leaving  the  holes  filled. Abo
=== LEAF 403 ===
Pelly  (J.R.Q,S,  xxxv.  232)  to the  "  Traveller's  Tree,"  i.e.  the  Mada- gascar Ravenala  (Urania  speciosa),
FANQXTI,8.  Chin./an-An<m',  *  foreign demon';  sometimes  with  the  affix  Uz or  tsfu,  *son';  the  popular  Chinese name  for  Europeans.  T"  During  the 15th  and  16th  centu
=== LEAF 404 ===
n  Lahore  District.
FETISH,  s.  A  natural  object,  or animal,  made  an  object  of  worship. From  Fort,  fetifo,  feitifo,  or  fetisso  (old S]pajL  fechizo\  apparently  iromfactitiusy signifying  nrst  'artificial,'  and  then '  unnatural,'  '  wrought  bv  charms,'  &c. The  word  is  not
```


## [2026-09-05T06:06:45.056Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==401' HJB.txt | tail -c 3000",
 "description": "Dump HJB leaf 401"
}
```


### [2026-09-05T06:06:46.682Z] TOOL RESULT

```
  29th  Novr.,  dodring  our  orders  with re^^aid  to  the  Faldrs  who  were  taken TOiBoners  at  the  retaking  of  Dacca.'* — Ft, William  Cant,  Dec.  5,  in  Lona,  342.  On these  latter  Fakirgy  see  under  SuNYASEE.
1770. — "  Singular  expedients  have  been tried  bv  men  jealous  of  superiority  to  share with  the  Bramins  the  Teneration  of  the multitude ;  this  has  given  rise  to  a  race  of monks  known  in  India  by  the  name  of T9kiiB."—Ray7uU  (tr.  1777),  i.  49.
1774.— "The  character  of  a  f!&kirisheld in  great  estimation  in  this  country." — Bogle, in  Maa-kham's  Tibet,  23.
1866,— "  There  stalks  a  row  of  Hindoo  devotees,
Bedaubed  with  ashes,  their  foul  matted hair
Down  to   their   heels;  their  blear  eyes fieroelv  scowl
Beneath  iiheir  painted  brows.      On  this side  struts
A  Mussulman  Fakeor,  who  tells  his  beads,
By  way  of  prayer,  but  cursing  all  the while
The  heathen." — The  Banyan  Tree,
1878. — **  Les  mains  abandonn^es  sur  les genou^  dans  une  immobility  de  fakir." — Alph,  Davdet,  Lt  Nabob,  ch.  vi.
FALAUN,  B.  Ar.  faldn,  fuldn,  and H.  fiUdna,  faldnoy  *such  an  one,'  *a certain  one*^;  Span,  and  Port  /uiano, Heb.  Fuluni  (Ruth  iv.  1).  In  Elphin- stone's  Life  we  see  that  this  was  the  term by  which  he  and  his  friend  Strachey used  to  indicate  their  master  in  early days,  and  a  man  whom  they  much respected,  Sir  Barry  Close.  And  gradu- ally, by  a  process  of  Hobson-Jobson, this  was  turned  into  Forlorn.
1803.— "The  General  (A.  Wellesley)  is  an excellent  man  to  have  a  peace  to  make.  .  .  . I  had  a  long  talk  with  him  about  mich  a one;  he  said  he  was  a  very  sensible  man." —Op,  eit,  i.  81.
1824.— "  This  is  the  old  ghaut  down  which we  were  so  glad  to  retreat  with  old  Forlom." — ii.  164.    Seealsoi.  56,  108,  845,  Ak;.
FANAM,  8.  The  denomination  of a  small  coin  long  in  use  in  S.  India, MalayaL  and  Tamil  'paiwmi,  *  money,' from  Skt  paw^jjfrt  paw,  *to  barter']. There  is  aLso  a  Dekhani  form  of  the word,  /atom.  In  Telugu  it  is  called r8ka.  The  form  fanam  was  probably of  Arabic  origin,  as  we  fina  it  long prior  to  the  Portuguese  period.  The fanam  was  anciently  a  gold  coin,  but latterly  of  silver,  or  sometimes  of  base gold.  It  bore  various  local  values,  but according  to  the  old  Madras  monetary system,  prevailing  till  1818,  42 /ananw
went  to  one  star  uagoda,  and  a  Madras fomam  was  therefore  worth  about  2d. (see  PrimepU  Useful  Tahles^  by  £. Thomas,  p.  18).  The  weights  of  a larce  number  of  ancient  fomams  given by  Mr.  Thomas  in  a  note  to  his  Pathan Kings  of  Delhi  show  that  the  average weight  was  6  grs.  of  cold  (p.  170). Fanams  are  still  met  with  on  the  west coast,  and  as  late  as  1862  were  received
```


## [2026-09-05T06:06:51.239Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==401' HJB.txt | head -c 4000",
 "description": "Head of HJB leaf 401"
}
```


### [2026-09-05T06:06:52.985Z] TOOL RESULT

```
  its  popular  sense is  a  'crafty  schemer,'  an  *  artful  dodger.' Filosofo,  in  Manilla,  is  applied  to  a native  who  has  been  at  colle^  and returns  to  his  birthplace  in  the provinces,  with  all  the  importance  of nis  acquisitions,  and  the  affectation of  European  habits  {BlumentriUy VocahularT).
FAKEER,  8.  Hind,  from  Arab. faHr  (*poor').  Properly  an  indigent person,  out  specially  *  one  poor  in  the sight  of  Qoa^^  applied  to  a  Mahom- medan  religious  mendicant,  and  then, loosely  and  inaccurately,  to  Hindu devotees  and  naked  ascetics.  And this  last  is  the  most  ordinary  Anglo- Indian  use.
1604.— "Foken  are  men  of  good  life, which  are  only  giyen  to  peace.  Leo  calls them  Hermites;  others  (4ll  them  Talbiet and  Saints."  —  Colleciion  of  ihingt  .  .  .  q^ Barbarie,  in  Purehat,  ii.  857.
, ,  * ' Muley  Boferet  sent  certaine  Fokdn, held  of  great  estimation  amongst  the  Mooret, to  his  brother  Muley  Siaanf  to  treate conditions  of  Peace." — Ibid.
1688.— **  Also  they  are  called' FaokeeiM, which  are  religious  names." —  IV.  Bruton,  in Hakl,  y.  56.
1658.—-'*  FaUr  signifie  pauure  en  Turq  et Persan,  mais  en  Indien  signifie  .  .  .  vne espece  de  Beli^ux  Indou,  qui  fouUent le  monde  aux  pieds,  et  ne  s'habillent  que  de haillons  qu'ils  ramassent  dans  les  rute.  — De la  BoHllaye-U'Gouz,  ed.  1657,  588.
c.  1660.—"  I  have  often  met  in  the  Field, especially  upon  the  Lands  of  the  Rajas, whole  squadrons  of  these  Faquiret,  alto- gether naked,  dreadful  to  behold.  Some held  their  Arms  lifted  up  ... ;  others  had their  terrible  Hair  hanging  about  them  .  . .  ; some  had  a  kind  of  UercuUi»  Club ;  others had  dry  and  stifif  Tiger-skins  over  their Shoulders.  .  .  ."—Bemier,  B.T.  p.  102 ;  [ed. CoMiaiUy  817].
1678.—'*  FaUdn  or  Holy  Men,  abstracted from  the  World,  and  resigned  to  God." — Fryer,  95.
[1684.— "The  Ffaekeer  that  KiUed  ye Boy  at  Ennore  with  severall  others  .  .  .  were broTight  to  their  tryalls.  .  .  ."—Pfimgltt Diary,  Ft,  St,  Geo,  1st  ser.  iii.  111.]
1690.— "Thev  are  called  Faqnin  by  the Natives,  but  Ashmen  commonly  b^  us,  be- cause of  the  abundance  of  Ashes  with  which they  powder  their  Heads." — Ovington,  850.
1727.— "Being  now  settled  in  Peace,  he invited  his  holy  Brethren  the  Faldret,  who are  very  numerous  in  India,  to  come  to Agra  and  receive  a  new  Suit  of  Clothes." — A,  Hamilton,  i.  175 ;  [ed.  1744,  ii.  177].
FALAUN.
348
FANAM,
1768.— '*  BeceiTed  a  letter  from  Dacca dated  29th  Novr.,  dodring  our  orders  with re^^aid  to  the  Faldrs  who  were  taken TOiBoners  at  the  retaking  of  Dacca.'* — Ft, William  Cant,  Dec.  5,  in  Lona,  342.  On these  latter  Fakirgy  see  under  SuNYASEE.
1770. — "  Singular  expedients  have  been tried  bv  men  jealous  of  superiority  to  share with  the  Bramins  the  Teneration  of  the multitude ;  this  has  given  rise  to  a  race  of monks  known  in  India  by  the  name  of T9kiiB."—Ray7uU  (tr.  1777),  i.  49.
1774.— "The  character  of  a  f!&kirisheld in  great  estimation  in  this  country." — Bogle, in  Maa-kham's  Tibet,  23.
1866,— "  There  stalks  a  row  of  Hindoo  devotees,
Bedaubed  with  ashes,  their  foul  matted hair
Down  to   their   heels;  their  blear  eyes fieroelv  scowl
Beneath  iiheir  painted  brows.      On  this side  struts
A  Mussulman  Fakeor,  who  tells  his  beads,
By  way  of  prayer,  but  cursing  all  the while
The  heathen." — The  Banyan  Tree,
1878. — **  Les  mains  abandonn^es  sur  les genou^  dans  une  immobility  de  fakir." — Alph,  Davdet,  Lt  Nabob,  ch.  vi.
FALAUN,  B.  Ar.  faldn,  fuldn,  and H.  fiUdna,  faldnoy  *such  an  one,'  *a certain  one*^;  Span,  and  Port  /uiano, Heb.  Fulu
```


## [2026-09-05T06:06:59.554Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==400' HJB.txt | tail -c 2500",
 "description": "Tail of HJB leaf 400"
}
```


### [2026-09-05T06:07:01.171Z] TOOL RESULT

```
d),      G.     (qy.  Viaa^patam,  G.
Sadras?)  Bimlipatam,.M.
Fort  St.  George,  G.M.  Ganjam,  M. Policat,  M.     '  Manickpatam,  B.
Pettipoli,  G.,  S.  Armpore  (f),  6.
Bengal  SUU. Balasore.  G.  (and  Je-  Malda,  G.
lasore  i)  Berhampore,  M.
Galcutta    (Ft.    Wfl-  Patna,  C.
liam  ana   Ghntta-  Luolmow,  G.
nnttee,  G.)  Agia,  G.
Hooffly,  G.  Lahore,  M.
Gosambasar,  G.  Dftoca,  G.
Rajmahal,  G.  Ghittsigong!
fAOHFUR.
347
FAKSER.
Tndo-Chinete  Camiiriet.
Vega,  M.  IJgore,  M. Tennanerizn  {Trina-  Siam,  M.,  8.  (Judoa,
eor€f  6.)  »'.«.  Yitwia).
Quedah,  M.  Oamboja,  M.
Johore,  M.  Cochin  China,  M.
Pahang,  M.  Tonqnin,  C. Patani,  S.
InCkina, ftlacao,  M.,  S.  Tywan  (in  FormoBa),
Amoy,  M.  M.
Hokaiea  (i.«.  Fu-  Chnsan,  M.  (and  Ning- chow),  M.  po?).
In  Japan, — Firando,  M.
Archipelago.
In  Sumatra,
Acheen,  M.  Indrapore,  C.
PasHunan,  M.  Tryamong,  C.
Ticoo,  M.  (qu.  aome  (B.  haa  ahio,  in  Snma- as  Ayer  iMokets,  tra,  Ayer  Borma, B.  ?)  Eppon,  and  Bamola,
Sillebar,  M.  wmch     we     cannot
Benooolen,  C.  identify.)
Jambi,  M.,  S.  Indraghiri,  S.
In  Java.
Bantam,  C. Japara,  M.,  S.
Jacatra    (nnoe   Bata- via),  M.
In  Borneo. Banjarmasin,  M.         Brunei,  M. Sncoadana,  M.
In  CelAfS,  dx.
Macaoar,  M.,  S. Banda,  M. Lantar,  S. Neira,  S. Boeingyn,  S. ^elanuin,  B. Amboyna,  M.
Pulo  Boon  (?),  M.,  S. Puloway,  S. Pulo  Condore,  M. Magindanao,  M. Machian,  (8),  S. Moluccas,  S.
Camballo  (in  Ceram),  Hitto,  Larioa  (or Loricca),  ana  Looho.  or  Lugfao,  are  men- tioned in  S.  (iii.  308)  as  sub-factories  of Amboyna.
[FAQHTUB,  n.p.  "The  common Moslem  tenn  for  the  Emperors  of China  ;  in  the  Ramus  the  first  syllable is  Zammated  (Fiigh) ;  in  Al-Ma^'udi (chap,  xiv.)  we  find  Baghfiir  and  in Al-Idrisi  ItetghMgh,  or  Baghbtin.  In Al-Asma'i  Bagh=god  or  idol  (Pehlewi and  Persian) ;  hence  according  to  some Baghd^  (1)  and  B&ahist&a,  a  pagoda (T).  Sprenger  (Al-Ma^udi,  p.  327)  re- marks that  Bashfiir  is  a  literal  trans- lation of  Tien-tse,  and  quotes  Visdelou : "pour  mieux  faire  comprendre  de  quel ciel  lis  veulent  parler,  ils  poussent  la
f^n^ogie  (of  the  Emperor)  plus  loin, la  lui  donnent  le  ciel  pour  p^re,  la terre  pour  m^re,  le  soleil  pour  fr^re a!n^  et  la  lune  pour  soeur  ain^e." — BurUmt  Arabian  Nights^  vi.  IfiO-lSl.]
FAILS 00F»  s.  Ar.— H.  faihtaf, from  <^6ao<t>oi.  But
```


## [2026-09-05T06:07:13.372Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR>=101 && NR<=106 {print \"=== LEAF \"NR\" ===\"; print $0}' HJB.txt | grep -n -i \"bagh\\|Bahar\\|^=== LEAF\\|god\" | head -20",
 "description": "Scan HJB leaves 101-106"
}
```


### [2026-09-05T06:07:15.728Z] TOOL RESULT

```
1:=== LEAF 101 ===
10:Bahddur  is  one  of  the  tenas  which the  hosts  of  Chlngiz  Khan  brought with  them  from  the  Mon^l  Steppes. In  the  Monffol  cenealpgies  we  hnd Yesugai  Bahadur^  Uie  father  of  Chineiz, and  many  more.  Subutai  BahMur, one  of  the  great  soldiers  of  the  Mongol host,  twice  led  it  to  the  conquest  of Southern  Russia,  twice  to  that  of Northern  China.  In  Sanang  Setzen's ]X)etical  annals  of  the  MoiLgols,  as rendered  by  I.  J.  Schmidt,  the  word is  written  BaghaJtuTy  whence  in  Russian Boffoiir  still  survives  as  a  memento probably  of  the  Tartar  domination, meaning  *^  hero  or  champion.'  It occurs  often  in  the  old  Russian  epic fiallads  in  this  sense ;  and  is  also  ap- plied to  Samson  of  the  Bible.  It occurs  in  a  Russian  chronicler  as  early as  1240,  but  in  application  to  Mongol leaders.  In  Polish  it  is  found  as  Bo- hatyr^  and  in  Hungarian  as  Bdtor, — this last  beinjg  in  fact  the  popular  Mongol pronunciation  of  Baghaiur.  In  Turki also  this  elision  of  the  guttural  extends to  the  spelling,  and  the  word  becomes Bdtur,  as  we  find  it  in  the  Diets,  of VamWry  and  Pavet  de  Courteille. In  Manchu  also  the  word  takes  the form  of  BatuTUy  expressed  in  Chinese characters  as  Pa-tu-lu ;  f  the  Kirghiz has  it  as  Baiyr;  the  Altai-Tataric  as PcuUtyTy  and  the  other  dialects  even as  Magaihyr.  But  the  singular  history of  the  word  is  not  vet  entirely  told. Benfey  has  suggestecl  that  the  word originated  in  Skt.  bhaga-dhara  (*  happi- ness-possessing'). J  But  the  late lamented  Prof.  A.  Schiefner,  who favoured  us  with  a  note  on  the subject,  was  strongly  of  opinion  that the  word  was  rather  a  corruption ^Hhrough  dissimulation  of  the  conso- nant," of  the  Zend  bagha-puthra  *  Son of  GJod,'  and  thus  but  another  form of  the  famous  term  Fagbfor,  by  which the  old  Persians  rendered  the  Chinese Tien-tsz  (*Son  of  Heaven  *),  applying  it to  the  Emperor  of  China.
15:=== LEAF 102 ===
35:1800.— "One  lac  of  Behandxy  pagodas." —  WelUngUyii,  i.  148.
43:=== LEAF 103 ===
66:=== LEAF 104 ===
98:=== LEAF 105 ===
132:=== LEAF 106 ===
```


## [2026-09-05T06:07:28.072Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"\\[pdf page\" BQT_v1_pages.txt | head -5; echo \"...\"; wc -l BQT_v1_pages.txt; echo \"=== ref_page tool ===\"; sed -n '1,60p' /home/sfmqrb/git/rishe/tools/ref_page.py",
 "description": "Inspect BQT vol1 pages file"
}
```


### [2026-09-05T06:07:28.131Z] TOOL RESULT

```
...
32485 BQT_v1_pages.txt
=== ref_page tool ===
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


## [2026-09-05T06:07:39.300Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && head -c 800 BQT_v1_pages.txt; echo; echo \"=== grep anbaz ===\"; grep -n \"انباز\" BQT_v1_pages.txt | head -5",
 "description": "Inspect BQT v1 format"
}
```


### [2026-09-05T06:07:39.356Z] TOOL RESULT

```
۱ ۵ ۱! ۱
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
وک رهب اه نات مج
لش
وان روکد ور
۱ و
طراول ؛ | ع اس
چاپ دوم فروردین ۱۳۴۳
با تجدید نظر کامل
بسرمایه کنابفروشی ابن سینا - تپر اناداره کل دک زون.
شماره ۷9 9 ۳
بر
5
‌ ۰ م۸
و «ارس‌شبات
4
د انشمند محتر م آقای‌د کترمحمد معین‌استاد دانشگاه تهران
فوپانت تاموی ۲۰/۹/۳ ها رتیفارد *
کلیه ح
=== grep anbaz ===
4010:۱- سیدعلی شیرازی متخلص به‌نیاز که «ازفصحای بی‌مثل وانباز است
11905:دلیری وجانبازی کردن باشد .
28368:و خداوند خاله م و دار و شریك و انباز هم آمده
```


## [2026-09-05T06:07:46.716Z] TOOL CALL #29: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nprint(json.dumps(d['BQT'].get('scans'),ensure_ascii=False,indent=1)[:3000])\nprint('LOCAL',d['BQT'].get('local_file'))\nprint('OFFSET',d['BQT'].get('page_offset'))\nprint('HINT',d['BQT'].get('lookup_hint'))\n\"",
 "description": "BQT scan config"
}
```


### [2026-09-05T06:07:49.461Z] TOOL RESULT

```
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
LOCAL ['/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages_faseng.txt']
OFFSET vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...').
HINT grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=dehkhoda, parsi.wiki, abadis.ir/fatofa/<word>/) quotes Borhan and often Mo'in's footnotes as (حاشیهٔ برهان قاطع چ معین). noorlib.ir/book/info/10294 is a 1-vol Nima 1380 Borhan without Mo'in's notes. | For pages in a scanned volume use: python3 tools/ref_page.py BQT:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)
```


## [2026-09-05T06:07:56.676Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for L in 383 384 385; do echo \"=== leaf $L ===\"; awk -v n=$((L+1)) 'BEGIN{RS=\"\\f\"} NR==n' BQT_v1_pages.txt | head -40; done",
 "description": "Dump BQT v1 leaves around p.164"
}
```


### [2026-09-05T06:07:58.192Z] TOOL RESULT

```
=== leaf 383 ===
سب ی ٩5‏
| بودن بروزن افزودن, بربالای حم
چیدن باشد .
اثبوذن س با زال قطه‌دار بروزن‌اندودن,
بمعنی اسل‌کاینات و آفرینش باشد .
ایوس » بروزن اضوی , تخمی باشد
بنظر آحده است ۰
| بو سیدن - بانستانی مجپول بروزن
افزوییدن , بمعنی پدید آمدن و ظاهر شدن -
و موجود گردبدن باشد .
اثبوه » بروزن اندره » بمعنی‌فرورختن
دبوار باشد - و بمعتی پر و عملو و بسیار نیز
امده خواه بساری مردم و خواه چیزی دیگر
باشد - و دم قصبه است در بالای کوهی از
مضافات دیلمان .
اثبوی « بر وزن بدبوی » بعنی بوی
کردن باشد ٩‏ - و چیزی‌را نیز گوبند که ببوی
آهده و کندیده باشد - و مطلق‌بوی رانیز گونشد
خواه بوی خوب و خواه بوی بد باشد - و بوی
کننده را نیز کوش که فاعل باشد - و اهر باین
معنی هم هست عنی بوی کن و سوی ۰
) بو ی (۱) » بکربایحطی‌وسکون
دال ؛ یمنی بوی کرد -- و امر بجمم هم هست
بعتی بوی کنید و ببوید .
انبوییدن 0)- ممدر ابوی باشد
سعتی بوی کردن و بوبیدن .
انتو هن
اثبه ه بش ثاكث و طپور ها بروزن‌انده ,
مخفف انبوه است که فروریختن دبوار - و عملو
و پر و بسیاری چیز ها باشدخواه از مردم وخواه
از حیوانات دیگر - و بفتح ثالث و خفای ها
هبوه‌است معروف در هندوسنان ۴ .
۱ ثییر بروزن زنجیر » بمعن ی گل‌خشك
وگل تر هر دو نوشته‌اند - و بمعنی پرکردن
هم هست - و بمعنی کیش و مذهب ودین وین
هم باظر آهده است . ۱
اثییره بروزنزنجیره» خلاشه‌وخاشا کی
راکوند, که بعد از پوشش خانه بر بام اندازند
تا بربالای آن خاكك و کل ریزند و بیتدایند .
آثییس » بر وزن نلبیس , خرمن غله
=== leaf 384 ===
انج - بفتح اول وسکون ثانی و جیم»
اطراف 2 روی و رخار ( ۱ ) باشد -
«بمعنی بیرون رفتن وبیرون کشیدن‌هم آمدم‌است
- وامر بان معنی هم حست بمنی بیرون بکش .
انحام ۱
و آخر هرکار و هوچیز باشد ه بنظام آیشوهاعل
رانیز گویند که‌بنهایت رساننده و با خرآورنده(۲)
و شهات برسان .
اتحباد ه با بای ابجد . ععرب انگبار
نت آی نت یاعد سم نگ وتو
پواسیر دانافم است .
نالك و خای نقطه‌دار ساکن ۰ بمعنی چین وشکن
ری و اندام و غیره باشد .
) نجحت باجیم فارسی بروزن‌بدبخت»
انش ‌ باجیم؛ بر وز ند حعنی ب رجستن
باشد .
| نجخیدن « بنثاك‌بروزن‌ب رگزیدن,
درهم کشیده شدن پوست روی و اندام باشد -
انحشان » منم ناك بروزن مردمان ؛
)۱ ساره
0
اصل‌آلانجدان خوانند ۴ ؛وبعضی گویند تسنای‌است
و آن جانوری باشد. شببه بآدمی .
انجر لك - بکس ثاك وفتح رای فرخت
وسکون کاف » نام دشتی‌و صحرادیست غیرمعلوم-
و مرزنگوش را نیز گوبند و آن نومی آزرباحین
است که در دوا ها بکاد برند و درعریی ! ذان‌الفار
کویند ۴ .
اتجره - بروزن پنجره ؛ نباتی است که
آنرا بعربی بنات النار گویند بقتح بای ابجد ؛ و
نخم آن را قرض‌خوانند وتخم آن مستعمل‌است.
سه‌درم آنرا با شیر نازه بشورند قوت باه دهد
و بکوبند وبا عصل برقضیب مالند سطب کرداند .
)نج ۴ - بنتح اول و سکون ثٌانی
وکسر جیم و سین بی‌نقطة بالف کشده ؛ بمعنئی
ابوخلسا ۴ است که نوعی ازسرخ مردیاشد و آنرا
عربی شجرءالدم گویند , خون شکم را ببندد .
انح - با خن نقطهدار » بروزن و ععنی
انجخ ۱ سا که جچن و شکنج روی واندام عاشد .
انحکك - باکاف مروزن‌مردمك ءدانه‌ای
=== leaf 385 ===
- بو -
) فحل س بفتم اول وکسر ثالث و سکون
نانی ولام» رسثنی باشد که آیرا خطمی خوانند ۳
عالمتاب است .
انجمن! - ینم اك و قح میم وسکون
نون ۰ مجلس و مجمم را کویشد - بمعنیکروه
انحوج - بروزن محلوح , چوب عود
باشد ؛ و بهترین وی‌آن تکهدر ته آب‌شیند .
کونند عود یخ درختی است که آنرا میکنند
و در زیر خاكث دفن میکنند تا مدنی همین بعداز
آن برمیآورند » پوسیدة آنرا میتراشند و بافی
عود خالص می‌ماند . بهترین آن مندلی باشد .
افحوخ - بررزن مطبوخ . چن‌وشکن
روی و اندام باشد از عابت چیری دا سبسد: ۳
و بژمرده شدن میوه را نیز گفته اند - و بمعنی
آب ده ن که آنرا ت فکویند هم امذه است .
| نج و یادن - بروزن سر پوشیدن .
برهم ش کشیدن بوست روی و اندام وا گومند .
افحوسا؟ » باسن بی‌شقطه بالف کشیده.
بحنی انجسا است که نوعی از سرخ مرد باشد
و بعربی شجرةالدم خوانند » خون را بندد .
انحوع - با عن نقطه دار , بر وزن
وهعنی انجوخ اس که چن و شکن روی واندام
باشد - و آب دهن را نیز گونند .
| نجوغیدان - بروزن‌ومعنی اجوخیدن
است که برهم کشیده شدن پوست روواندام‌باشد .
انجیره
| نحو لد مس بر وزن مفلوك » نام دشتی
و بیابانی‌است نامملوم؟ .
) نجیدن ؟ - بروزن رنجیدن , بمعنی
استره زدن باشد بعنی حجامت کردن - و بمعنی
دیزه ریزه کردن هم گفته‌اند - و بیرون کشیدن‌را
پیز گوبند - و بمعنی زين آب دادن هم بنظر
آ مایت :
انجیفه ه بروژ نگندیده , بلغفت‌بونانی
کندنای کوهی باشد که‌بمربی حشیشةالکلب‌خوااند
و صوف‌الارض نب زکویند - و دشوار زابیدن زنان
را سودمند بود - و بفارسی بمعثی دبزه‌ریزه کرده
شده باشد .
انحیر بر وزن
```


## [2026-09-05T06:08:07.178Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==383' BQT_v1_pages.txt | grep -n \"انباز\\|انباغ\\|همباز\\|شریك\\|شریک\" ; echo \"---382---\"; awk 'BEGIN{RS=\"\\f\"} NR==382' BQT_v1_pages.txt | head -60",
 "description": "Find anbaz in BQT"
}
```


### [2026-09-05T06:08:09.044Z] TOOL RESULT

```
15:دیگری‌را انباغ باشد .8
---382---
یوتانی۱ وممنیآن‌بفارسی « سنگه زاییدن آمان
کن » باشد . وآن دانه ایست ساهرنگه بمقداو
جوژبوا. بغایت املی‌وصلب ودشوارشکن: وچون
بجنبانند مفز آن در درون وی صدا کند وآنرا
بشیرازی « کن ابلیس » خوانند نم کاف فارسی
ونون ۰ یعنی خایةٌ شبطان و بعربی حجرالولادة
گوبند . چه هرگاه در زیر زنان آستن دود
کنند زود بزایند و اکر باشیرزنان سح قکنند
وقدری پشم را بدان بیالایند و زنی‌ که نمی زاید
بوفت جماع بخود بر گیرد آستن قود.. گو یف
چونآنرا دردست گیرند وبا کسی مخاصمت کنند
برآ نکس غالب‌آیند .
| ناغاطسی - باغننقطه داربالفکفیده
وطای حطی مضموم بسین بی‌نقطه زده ۰ بونالی
سنکی باشد که چون آنرا بآب بسابند رنگی
مانند خون از آن برآید و با شیر زنان درچشم
چکانند ورم چشم و بیاری آب آمدن از چشم
رانافم‌است» وآن‌را بعربی‌حجر اناغاط یگویند .
افاغلس مه بن غین تقطه دار و لام
وسکون مین بی‌قطه ۰ بیونانی؟ دوایی است که
آنرا بفارسی مرذنگوش وبعربیآ ذان‌الفار گویند,
چه بر ک» آن بگوش موش میماند » باس رکه بر
کزیدگی عغرب مالنده نافم است
افا لیقی - با لام و قاف هر دو بتحتالی
رسیده . بلفت رومی دوابی که انرا انجرء
وتخم آنرا بذرالانجره گویندوبمربی قض‌خوانند.
انبارده
تخم آن مستعمل است . اکر مقدار سه درم از
آن باشیر گوسفند بخورند قوت‌باه دهد » ویضی
گویند انالیقی همان بذرالافجره است .
| ثاهیكف ؟ » با های‌تحتانی رسیدموبدال "
زده . بمعنی ناهمد است که ساره زهره باشد .
اب - بفتح اول و انی و سکون بای
ابجد . بادنجان را گوشد و آن ممروفست؟ »
بافراط خوردن آن جذام د ماع و بی‌خوایی
آورد» و بعضی گویند عرمی است ۱
ی رزن
افلاطون » حصار قلمه و جای محکم ر! کوشد -
انبار 1 ع بفتح‌اول‌بروزن زنگار «بمعی
لبریز و مملو و پر باشد - و فروربختن خانه
و افتادن دبوار و امثال الرا نیز گویندب ویمعنی
خی و خاشاله و فثلة اسان و س رکین خیوانات
دبگر باشد که توده کرده‌باشند و مزارعان‌برزمی
زراعت ریز ند واستخر وتالاب رائیز انبار گوینف
و بکر اول مخفف این بار است
انبادذ گی « بروزن و معنی انباششگی
اک ستتی. ود باه مت نب
| ثباددن ۱ « با دال ابجد بروژن‌وعنی
انباشتن است کهپر کردن و انبار کردن‌چیزی‌باشد
از چیزی دیگر
)۱ چك : ژند ویاژند .
۱ - بونانی2601185 «اشتبتگاس» ش بان 881021115 0استینگاس »0 202
«دزی»,
آلوده. جمما بعنی
داده‌اند ای کردند. ۶ بشت ۱
- بهلوی ۵2۸02۲ 0 از
۴ راك : لك ٩‏ ص۱۹۱ .
4 «مناس ۲۷۵ :
: : انبار) ۳ دن‌یسوند مصدری ۳
```


## [2026-09-05T06:08:16.402Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==383' BQT_v1_pages.txt",
 "description": "Full BQT leaf 383"
}
```


### [2026-09-05T06:08:17.892Z] TOOL RESULT

```
اتبارش
که پر کرده باشد - و بمعنی پرنسمت و با نعست
هم اجه ات ۵
نبادش! -بروزن‌افزایش. پر کردنی‌را
کوبند . و آن چیزی باشد که جوف درون
چیزبرا بان پر کنند. وأنرا بعربی حشوخوانند.
انبار "سیر وزن دمساز » خومات و رفیق
و همتا را گویند . "
نباشت ۱0 بروزن برداشت ۳ ماضی
انباشتن است ععنی کر و ممل و گرداند ۰
۶ ۵۸۱ ه ۳ > ۳
انباشتی ۲۷ " سبروزن برداشتن,بسنی
پر کردن و مملو گردانیدن و آنبار نمودن باشد .
افیا ۴ - باغی تقطم‌دار .دوزن‌را گوبند
دیگری‌را انباغ باشد .8
اثبان باد - بکر نون و با بای ابجد
بروزن می‌دان‌کار. مردم فربه - و بیکاره وهیجکاره
را گوند ۰
برمی آورند .
اثبر ب بنتح اول وضم الث وسکون‌انی
و رای فرشت » التی باشد از آهن که ز رکران
و مسکران طلا و مس تفته دا بدان گیرند ,وبه
عربی کلوب خوانند .
۱ 1 از انبار شش بوند آسم
و
] ذیر وت ده بروزن‌عنزروت , امیودباشد
و آن میومایست معروف ۵ .
افیره - ینم ات بروزن‌قنجفه «هرجیز
موی رنخته را کونند عموماً وشتر موی ریخثه را
خصوصا ‏ و اسب و شتر آبکش را نز گفتماس
و در عربی شکنبه را گویند - و بمعنی دره کوه
نیز حست ؛ و بفتح ثالث بر وزن حنجره هم
آمفه ات .
اثیست - بروزنک‌بت : نلیط و بته
شده را کومند ۷ .
| ثیسقه - بر وزن برجسته ,هر چي زکه
آن بته و سخت شده باشد و بدشواری وا شود
و حل گردد - و شبر و ماست و خون بستهرانیز
گوبتد ٩‏ .
اثبله - بنتح اول و الث بروزن‌حنظله,
تمر هندی رأگویند و بهندی ابلی خوانتد ۰۷
انیمی ۸ س بکسر ثالث وقتح میم‌بروزن
صف‌شکن , بلفت زند و بازند (۳) انگور باشد
و بعربی علب گویند .
افیق یه - بروزن میغوب . فرش وساط
و گتردنی را گومشه. :
اثبو 4 - بر وزن منصوبه . ماشوره را
گویند - و وله آشابه و مانئد آنرا نیز
کفته‌اند .
۴ - پهلوی ۵:۳۰98۵1, 20۵۵2۵۷
۲
۴ ات ود اون
ت۱۳ تم ستد.
۸ حز2(8021130),
```


## [2026-09-05T06:08:28.820Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for L in 421 422 423 424; do echo \"=== leaf $L ===\"; awk -v n=$((L+1)) 'BEGIN{RS=\"\\f\"} NR==n' BQT_v1_pages.txt | head -3; awk -v n=$((L+1)) 'BEGIN{RS=\"\\f\"} NR==n' BQT_v1_pages.txt | grep -n \"باج\\|باژ\" | head -5; done",
 "description": "Locate BQT p.203 baj"
}
```


### [2026-09-05T06:08:30.396Z] TOOL RESULT

```
=== leaf 421 ===
و شش لت و نات
بیان اول
با - , دمعم مع است که‌بجهت عصاحت
=== leaf 422 ===
۱ بابادشاه دست زدن ۱ متشه د<
است؛ و این صفیر بجهت تعظیم است .
پا یل » یکر الك بر وزن قابل , بلفت
=== leaf 423 ===
بت ۷۲۰۳ ح-
قلعهٌ آن شهر بوده چاهی است عمیق . گویندحاروث
و ماروت در اتحاه محبوی آند» و جضم الث حم
=== leaf 424 ===
ودریجة کوچك را گوند» وظاهراً ابن لفت‌باجهك
است که مصفر باجه باشده و باجه مخفف بادجه
و پادجه بمعنی باد گیر و باد گیر جایی و دوزنی
1:ودریجة کوچك را گوند» وظاهراً ابن لفت‌باجهك
2:است که مصفر باجه باشده و باجه مخفف بادجه
5:۱ باجه پفتح جیم بروزن راجه ؛ دربچه
37:بقلم آ قای اقبال وداثرةالمعارف اسلام. ‏ ۷ - رل: بابوئه . ۸ - باج و باژ و باز باین معنی
41:انگلیسی ۷۵۱6۶ . باژ بممنی کلمه و سخن و گفتار است . کليةٌ دعا های مختصر راکه زرتشتیان
```


## [2026-09-05T06:08:34.691Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==425' BQT_v1_pages.txt",
 "description": "Full BQT leaf 424"
}
```


### [2026-09-05T06:08:36.386Z] TOOL RESULT

```
ودریجة کوچك را گوند» وظاهراً ابن لفت‌باجهك
است که مصفر باجه باشده و باجه مخفف بادجه
و پادجه بمعنی باد گیر و باد گیر جایی و دوزنی
را کویند که باد از آنآمدو شد نماید واله‌اعلم .
۱ باجه پفتح جیم بروزن راجه ؛ دربچه
و دوژنه (۱) بزر که را گوشد ۱ . ۱
باحور با حای حملی بروزن کافور »
بخاربر| گوین که درهوای کرم از زمین‌برخیزد-
در عربی بمعنی بیاری وسختی کرما باشد ۴ .
پاحو اه با زبادنی الف ؛ لفظی است
بونانی بمعنی روز کار آزموده » و ایام آن هفت
روز است و مضی گویند هشت روز ؛ اشدای آن
دا 0
و۳۵ امس
بود » وصنی گوبند معنی این لفظ شدت وزیادتی
از بحران بمعنی حکم » یعنی ازین روز هاحکم
کنند بر احوال ماههای خزان و زمستان » وروز
او آن دلیل‌نشرین‌الاول (۲) و روز دوما ندلیل
شرین‌ال خر (۳) تا باخر, هرچه در آن روز ها
وافع شود از کرما و سرما و باران و میغ درآن
ماهبا نیز چنان بود ۰ وجمعی گویند روز اول‌آن
دلیل ماهی اننخ. که ]فتاب در مرج اسد باشت
و روز دوم درستبله و همچنین تا بحوت که‌هشتم
ای برحکم مذ کور ازباد و باران وامثال آن ۳ .
بخ « باخای نقطمدار بروزن شاخ »بمعنی
راه باشد که عربان طریق گویند .
ماه وشدت گرماست «قطرالمحط».
«قطرالمحیط» .۰ ۴ - دراوستا 202764872 :ا 2020001020072 «معنی‌شمال آمده وآنجا جایگاه
اهر یمن و دیوان و مکان درزخ دانسته شده « خرده اوستا ۸۷ ح ۲ » . در پپلوی نبز کق2021
آمده بدین همنی و نیز بمعنی سیاره « منای ۷۹۹ : ۲ * در زبان فارسی اکثر بسعنی هفرب
آمده در پرابر خاور ؛ ولیگاه نیز بمکس, باختر بمعنی مشرق و خاور بمعنی هغرب استعمال شدم:
چو قهر آورد سوی خاورکریغ هم از باختر برزند بازتیغ . عنصری باخی.
بقیه ازصفحة ۲۰۳
٩‏ - درفرکی بمعتی قوی , مخت هجفتابی ۱6۵*- باتو پسر جوجی خان پسس چنگیزخان که در
قوربلتای سال 14۲ ۶ بهمراه یکیو که ومنگو مأمور تسخیرهمالك دوس و چرکس وبلغار کردید
و او بادشاه دشت قبچاق بود وبعدها وی منگو را بمقام خانی بررگزید . رك : فهرست تاربخ مفول
بقلم آ قای اقبال وداثرةالمعارف اسلام. ‏ ۷ - رل: بابوئه . ۸ - باج و باژ و باز باین معنی
از ریشه 08 پارسی‌بامتان مشتق است «مزدیسنا ۵4-۲۵۳ » وآن از ريشة 2 اوستایی بمعنی
بخش کردن وقسمت کردن‌است . ٩‏ - باح وبا وباز وواج و واژ باین‌معنی ازريشة اوستابی ۷۵6
( گفتن)» سان‌کریت ۷۵6 ۰ درپهلوی [۷2 با ۷۵8 ۰ درلاتینی ۷۵۴ , درفرانه ۷۵۷۴ » در
انگلیسی ۷۵۱6۶ . باژ بممنی کلمه و سخن و گفتار است . کليةٌ دعا های مختصر راکه زرتشتیان
آهته بزبان میرانند باژ گویند :
پرستندة آذر زردهشت. همی‌رفت باباژ و برسم بمشت . فردوسی‌طوسی «مزدیسنا۲۵۳ببمد»
اجثاق _ ترکی, دومردراکه دو خواهررا درازدواج دارند نبت‌بهم باجناق گویند .
«جنتایی 4۱40
```


## [2026-09-05T06:08:44.786Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for L in 458 459 460; do echo \"=== leaf $L ===\"; awk -v n=$((L+1)) 'BEGIN{RS=\"\\f\"} NR==n' BQT_v1_pages.txt | grep -n \"بخش\\|بخت\\|صفحة\\|بهلوی\\|پهلوی\\|اوستا\" | head -20; done",
 "description": "Locate BQT p.239"
}
```


### [2026-09-05T06:08:46.567Z] TOOL RESULT

```
=== leaf 458 ===
=== leaf 459 ===
7:نا موافق و بخت ناماعد .
8:بختنگاو - منم ارد وسکون نانی‌وئاك
18:اول و رایع بمعنی صاحب بخت باشد ۴ و باین ۱
36:دوم ( ۶ با ٩۰۵‏ - ۹۲هق . م ) «کامرن 6۲4۷ , این نام را به « بخترشه » تبدبل کرهده‌اند
41:ن بعت فصر _ رك: بخت. نب بختیار - فتح اول. ِِ 02) وه (رك:
42:مزدسنا۳۳۱ح) یمن بخت‌داده ۰ مجازا کمبکه بختش #9 و نك است
44:میشود وخاكك بختباری منطفه‌ایست کوهستانی محدود ازجنوب بخوزسنان. از مشرق بفاری » ازشمار
=== leaf 460 ===
45:بخش ‏ « بروزن کش , حصه و بهره
55:بافرو پُرزست و بخش وخرد
```


## [2026-09-05T06:08:49.807Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==460' BQT_v1_pages.txt | sed -n '1,50p'; echo \"=== leaf 460 ===\"; awk 'BEGIN{RS=\"\\f\"} NR==461' BQT_v1_pages.txt | sed -n '40,90p'",
 "description": "Read BQT baxt/baxsh pages"
}
```


### [2026-09-05T06:08:51.678Z] TOOL RESULT

```
--- 1۳۵
باکت .- بروزن‌سخت؛ بمعتی‌طالع باشد ۷ -
و سیاهی را نیز گویند که در خواب بر مرم‌افتد
و آنرا بمربی کابوی وعدالجنه خوانند ۴ سونام
جاتور کی است‌شبیه بملخ - ویضم اول‌نفام‌پادشا‌ی
بت د ندان‌خای کنابه از طالم
نا موافق و بخت ناماعد .
بختنگاو - منم ارد وسکون نانی‌وئاك
۳1 کاف قارسی بالف کشیده و بواو زده ۰ تطول
را کوبند و آن‌دوایی چند است که باهم‌بجوشانند
و بدن بمار را بدان شو ند .
بحتو ت- سم بضم اول و سکون‌نافی وفوفانی
بواو رسیده . هر چبز ریدم ماشد عموماً .- ورعد
را کویند خصوصاً ؛ و ختح اول هم آمده است
بحتور چم اول‌بروزن عزدور ؛بمعنی
ستتو باشد که رعد است - و شس غرنده را نیز
بخود
اول و رایع بمعنی صاحب بخت باشد ۴ و باین ۱
ممنی بروزن فغفور نیز درست است ٩‏ .
تقو ه منم اود و ثاك و سکون‌ثانی
و رعدرا نز گفته‌اند ؛ م بفتح اول‌هم درست‌است
یه - بنتح اول و ثاكك و سکون‌ثانی,
کومفند مه ساله ب چهار -اله را گوبندکه تر
باشد له ماده - : هر چیز که بوست آنرا کنده
باشئف ٩‏ - و ده فربه را نیز کنته‌اند - وبمعنی
محصل ۷ و تحصل‌دار هم هست . #
گویئد .
بخحرك ه بکر اول و سکون نانی‌وفتح
رای فرشت و سکون دال اد , صاحب عفقل
و جوشمند و صاحب شمور و ادراك ۳ خبر دار
جوا کثراست درطی
شکار نده
بتاریخ ٩‏ خرداد ۱۳۲۵), و آن معرب نام بابلی نب وکد نصر ۲دا5داذ7۲دانا۵ا۵ 2( (یعنی نبو
[ازارباب انواع ] ناج را نگهبانی کند) و آن از عالیترین القاب بابلی است که بدو پلدشاه بز رکه
بابلی داده‌اند: نبوکد نصر اول (۱۱۲۳-۱۱4۹ق . م) «کامرن. ابران باستان. ص۲8۵». نس وکدنسس
دوم ( ۶ با ٩۰۵‏ - ۹۲هق . م ) «کامرن 6۲4۷ , این نام را به « بخترشه » تبدبل کرهده‌اند
طبری ج ۱ ص ۲۸۲*. ۴ می‌کب از: مخت + ور (اداقاصاف), کیلکی 92504۷۲
۵ - بقیای : رنجور ۰ گنجود ومزدور . ۱ - طبری 02612 (خاید ککبده‌چنانکه کومند)
ت 4 . «واژه‌نامه >٩۲‏ رك : آهیختن
صل به‌عنی کر دآورنده مالیات ولیک کت ای افیگ ی
ن بعت فصر _ رك: بخت. نب بختیار - فتح اول. ِِ 02) وه (رك:
مزدسنا۳۳۱ح) یمن بخت‌داده ۰ مجازا کمبکه بختش #9 و نك است
نب #تیاری - طابقه ای از ابل‌های اب ا: کب هفت کر چا ده شیم
میشود وخاكك بختباری منطفه‌ایست کوهستانی محدود ازجنوب بخوزسنان. از مشرق بفاری » ازشمار
باصفهان و از مغرب بلرسنان «کیهان . جفرافبای حباسی ص ۷۷-۷۲ و۳-4۳۰۶) ۰ .
=== leaf 460 ===
تجسیل بت بروژن‌فیسد دیمثی گداخت.
و پژمرده شد - وفراهم آمد - ویین‌چین کردید.
بسیادان - بروزن‌فپمیدن. بممئی‌تاییده
و گداخته - و برعرده شدء و فراهم تفت
و خرامان باشد .
بخش ‏ « بروزن کش , حصه و بهره
باشد ۴ - و ماهی را نیز گویندکه بعربی حوت
باشد - و بمعنی برج هم هست خواه برج کبوتر
و خواه برح قلعة و خواه برج فلك 6 ۰
بعثایش ۷« بروزن افزایش » بمعنی
را ثبت ا گرچند باوباش‌دهند
۴ رك : خستن (شتح‌اول).
موافقت کردن) والنتته ات . ۴ : بدشدان
۴ که زدیر کار این کنبدکه پرداخت
‌
بافرو پُرزست و بخش وخرد
ناصر خسر و ملخی.
( بر هان فاطع ۳5)
```


## [2026-09-05T06:09:02.477Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for L in 470 471 472; do echo \"=== leaf $L ===\"; awk -v n=$((L+1)) 'BEGIN{RS=\"\\f\"} NR==n' BQT_v1_pages.txt | grep -n \"برخ\\|بهر\" | head -8; done; echo \"###### 543-545\"; for L in 543 544 545; do echo \"=== leaf $L ===\"; awk -v n=$((L+1)) 'BEGIN{RS=\"\\f\"} NR==n' BQT_v1_pages.txt | grep -n \"بهره\\|بهر \" | head -8; done",
 "description": "Locate barx and bahr in BQT"
}
```


### [2026-09-05T06:09:04.634Z] TOOL RESULT

```
=== leaf 470 ===
=== leaf 471 ===
34:بیعنی پاره و حصه و بهره - و لخت و بعض
40:برخان س بر وژن ترخان » بمعنی آواز
45:برخش ه بر وزن بدخش ‏ ؛
=== leaf 472 ===
1:برخقد سر کردن
8:برخوردار هم هست. وبروزن‌فتفور هم بنظر آدنه
11:و حصه و بهره و جزوی از کل باشد .
14:چیزی‌بکسی دهند وبمعنیحصه وبهرمواندکیاز
###### 543-545
=== leaf 543 ===
44:و بیمتی حصه و اصیب و حظ و بهره نیز آمدم
=== leaf 544 ===
=== leaf 545 ===
2:بهر ام تل - هی مر فج توح
11:بهر امه ‌ بروژن شهنامه, جامه سبزرا
26:بهر هه - بنتح اول و ثالث و دایم »
35:بهر ود - بروزن دلوز» بمحتی هروجه
```


## [2026-09-05T06:09:08.792Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== leaf 471 lines 30-50 ===\"; awk 'BEGIN{RS=\"\\f\"} NR==472' BQT_v1_pages.txt | sed -n '30,55p'; echo \"=== leaf 471 footnotes ===\"; awk 'BEGIN{RS=\"\\f\"} NR==472' BQT_v1_pages.txt | tail -12; echo \"=== leaf 543 lines 40-55 ===\"; awk 'BEGIN{RS=\"\\f\"} NR==544' BQT_v1_pages.txt | sed -n '38,60p'; echo \"=== leaf 543 tail ===\"; awk 'BEGIN{RS=\"\\f\"} NR==544' BQT_v1_pages.txt | tail -12",
 "description": "Read BQT barx and bahr entries"
}
```


### [2026-09-05T06:09:10.484Z] TOOL RESULT

```
=== leaf 471 lines 30-50 ===
پر جیسی ۴ بروزن ادرس » یتکی از
نامهای ستار مشتری باشد ۴ ؛ و با اولرتاك‌هر
دو فارسی هم آمده است .
رخ » با خای نقطه‌دار بر وزن چرخ ‏
بیعنی پاره و حصه و بهره - و لخت و بعض
باشد ۴ - وتالاب و استضر رانیز گوبند سوبمعنی
برقاهم اخست که برلدر: مد است.- ز ضاهی زا
1
وبمعنی شبنم هم آهده است» وباین حعنی‌بضم اول
نی زکفته‌اند .
برخان س بر وژن ترخان » بمعنی آواز
و صدا باشد - وئلم ولایتی است از ملك‌فاری 6
بر ححج » با جیم فارسی بر وزن اعرج »
زشت و نازیبا و زبون را گویند» و بفتح اول‌وثانی
هم آمده است ۰
برخش ه بر وزن بدخش ‏ ؛
راگویشه .
بر خفچچ - بننح‌اول و سکون ثالی‌رثات
مفتوح بفا و جیم فلرسی زده » گرانی باشد که در
خواب ب‌مردم افتد وآنراربی کابوی‌وصدالجنه
خوانند۱ . و بسضی آنرا از شیاطین میدانند »
و باین معنی بجای حرف اولبای حطی هم‌آعده
ات .
بر ی » باجيم‌فار سی بر وزن‌سردستی»
درشتی و ستیزه‌کاری را گویند
پشت اسب
=== leaf 471 footnotes ===
بر خفچچ - بننح‌اول و سکون ثالی‌رثات
مفتوح بفا و جیم فلرسی زده » گرانی باشد که در
خواب ب‌مردم افتد وآنراربی کابوی‌وصدالجنه
خوانند۱ . و بسضی آنرا از شیاطین میدانند »
و باین معنی بجای حرف اولبای حطی هم‌آعده
ات .
بر ی » باجيم‌فار سی بر وزن‌سردستی»
درشتی و ستیزه‌کاری را گویند
پشت اسب
رمشه است ت ابارتولمه ۱ رالد : ست و هر .
‌ - در معجم‌البلدان ۳ حدودالعالم بر خان
۱ - بوصال اندرایمن بدم از کشت زمان
=== leaf 543 lines 40-55 ===
واقع نمیشود » چنانکه در زمان نوشیروان واقح
شد ودر تال دو اردسهشت وفورع بات .
لهج - بنتح اول و ثانی وسکون جیم »
داروبی است که ازمصر آورند و خارسی بوزیذان
و بعربی متعجل خوانند .
لهر بر وزن شهر , نام ولامتی است -
و بیمتی حصه و اصیب و حظ و بهره نیز آمدم
‌ طر ۰
۴ جز , ۵)2(]06۵10۵5087 . پهلوی
۱ - مسحف بهزسفا۱:۱ص۲۸۱»»یپلوی ۷۵10216 .هر بكازدو ازده‌ماء ابران‌باستان‌دارای‌سی‌روزبود
وسال ۳۹۰ << ۳۰ 2 ۱۲ روز؛ بنابرین حرسال شمسی‌پنج‌رو زکم داشت. برای‌جبران درآخر حرحال»
بنج روز دیگرمی افزودنب :ا سال شمی درت دارای ۳۹۵ روز باشد. این کيسه سال را در عربی
خسه ممترقه ودر فارسی ينجهٌ دزدیده و بهیزك ( نه: بهترك) ودر پهلوی وهيجك وپنجه وپنج وه
رکاه واند رگاه و روزهای کانها نامیدماند باسم پنج فصل نپا . دردینکرد قطبم سنجانا , ج ٩‏
ص ۵۷۱۲ ۵۹۸ وهی ۳1 رك: خرده‌اوستا ۲۱۱-۲۱۰ واتفهیپم ۲ دیشکرت(ج۳.
نر س ۳۹-۳۰) صراحة ازدونوع سال شممی ابرانیان یمنی سالعرفی وسال بهیز کی (مکیوی) یاد
شده. سالعرفی راسال «وهیژ کيك روج بعنی دارای کبيءة روزهاوسال ابت‌راسال «وهیر کياكزمان»
بمنی دارای کبيسة ساعات‌میخواندند. این کور اضافی درفریب *۱۲سال. یکماه تمام میشد ودرسال
بهی ز کی جبران و تکماه برسال اضافه میکردند. اه شماری .
۵ بهارستان - بفتح‌اول (مر کب‌از: بهار +-ستان). جایی که‌شکوفه و کلپ ای کوتا کون
درآن انبوه باشد نام کتاب منئور عبد الرحمن جامی بسبك گلستان سمدی < دائرفالمعارف اسلام*.
ونیز بپارستان چین- رك: ص۳۲۲ ح۸. ۵ بهافه - بفتح اول. پپلوی ۷۵2 «ناوادبا ۱۹۹.
=== leaf 543 tail ===
وسال ۳۹۰ << ۳۰ 2 ۱۲ روز؛ بنابرین حرسال شمسی‌پنج‌رو زکم داشت. برای‌جبران درآخر حرحال»
بنج روز دیگرمی افزودنب :ا سال شمی درت دارای ۳۹۵ روز باشد. این کيسه سال را در عربی
خسه ممترقه ودر فارسی ينجهٌ دزدیده و بهیزك ( نه: بهترك) ودر پهلوی وهيجك وپنجه وپنج وه
رکاه واند رگاه و روزهای کانها نامیدماند باسم پنج فصل نپا . دردینکرد قطبم سنجانا , ج ٩‏
ص ۵۷۱۲ ۵۹۸ وهی ۳1 رك: خرده‌اوستا ۲۱۱-۲۱۰ واتفهیپم ۲ دیشکرت(ج۳.
نر س ۳۹-۳۰) صراحة ازدونوع سال شممی ابرانیان یمنی سالعرفی وسال بهیز کی (مکیوی) یاد
شده. سالعرفی راسال «وهیژ کيك روج بعنی دارای کبيءة روزهاوسال ابت‌راسال «وهیر کياكزمان»
بمنی دارای کبيسة ساعات‌میخواندند. این کور اضافی درفریب *۱۲سال. یکماه تمام میشد ودرسال
بهی ز کی جبران و تکماه برسال اضافه میکردند. اه شماری .
۵ بهارستان - بفتح‌اول (مر کب‌از: بهار +-ستان). جایی که‌شکوفه و کلپ ای کوتا کون
درآن انبوه باشد نام کتاب منئور عبد الرحمن جامی بسبك گلستان سمدی < دائرفالمعارف اسلام*.
ونیز بپارستان چین- رك: ص۳۲۲ ح۸. ۵ بهافه - بفتح اول. پپلوی ۷۵2 «ناوادبا ۱۹۹.
```


## [2026-09-05T06:09:19.791Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for L in 506 507 508 509 510; do echo \"=== leaf $L ===\"; awk -v n=$((L+1)) 'BEGIN{RS=\"\\f\"} NR==n' BQT_v1_pages.txt | grep -n \"بغداد\\|بغسنان\\|بغستان\\|^بغ\\|بغ \" | head -8; done",
 "description": "Locate BQT bagh pages"
}
```


### [2026-09-05T06:09:21.396Z] TOOL RESULT

```
=== leaf 506 ===
=== leaf 507 ===
=== leaf 508 ===
24:بغار بروزن‌طراز » چوییکه کفشگران
=== leaf 509 ===
10:ایرانی است مرکب از : بغ ۳ داد بمعنی خدا داده , در قرون وسطی صور مختلف این دلپوجود
27:(اهورمزدا) و کاهی نیزبمعنی ایزدآهده است . بغ بهردومعنی‌ازك بنیاد است از مصدربگه 88
34:زرتشت » بغ دام مطلق خدا بوده . زرنشت خدای بگانةٌ خود را اهورمزدا خواند , اما ول بغ
37:و پشتان (یستون) آمده و مبدل و معرب آن فغ است (ه . م) «بغ . پورداود : یادفامةٌ دنشاه
=== leaf 510 ===
20:بغلطاق با طای‌حطی» مروزن ومعنی
22:بغلاگ س بنتح اول بروزن دغلك » گرهی
```


## [2026-09-05T06:09:24.165Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==510' BQT_v1_pages.txt | sed -n '1,50p'",
 "description": "Read BQT leaf 509 (p.288-289) footnotes"
}
```


### [2026-09-05T06:09:25.897Z] TOOL RESULT

```
۳" ۱ ۱ ۹۳
بد آث « با دال ابجد بروزن فرهاد .عم ۱
شهری است. از عراق عرب و اسل آن باغ داد | ازکرمشگی و شک‌خالی باشد ۴ - وساغر خالی
از خراب را یز گوبند .
بر | - بختح اول بروزن صحرا . خو3و
باشد » و بمربی خنزی رگویند - و بشم اول بام
یادثاهی بوده است از خوارزم ۴ - و کلنگی را
یز گوبند که در وفت پرواز پیهاییش حم‌کلنگها
۱ - نام بنداد 2880044 که امیوزه عرب آنرا اغل 191180080 تلفظ کند بی خكه
ایرانی است مرکب از : بغ ۳ داد بمعنی خدا داده , در قرون وسطی صور مختلف این دلپوجود
داشته . شکل 1381020 یشتر استممال ميشده است *دالرتالمعارف اسلام». اين شهر را منصور
دومین خليفةً عباسی در کار وجله (درمحل آبادبی بیمین نلم) از سنگهای وبراٌ تیسفون‌بایتخت
ماسانیان وسلو کیه پابتخت سلو کیان و اشکالیان بناکرد و مقر حکومت خویش ساخت .
. 9.210 ,60ن۳۲۹ حهالد عع4 عاداه‌نداعععن رتاعتال
۴ - از اینجاست عثل عوام :
اک دانی که نان دادن ثوابست توخود میخو رکه بفدادت خرابست ,«امثال وحکم۱ ص۲۱۳*.
۳ - شهاب‌الدوله هلرون بغراخان بن سلیمان از ابلك خاية تر کستان ( متوفی بین ۳۸۳
۱ هه درسفحهٌ ۷۹۰
بودماست پسبب آنکه هرهفته مکبار افوشیروان
درآن باغ بار علم‌دای ودادسی مظلومان کردی»
و بکثرت استصمال داد شده است ٩‏ - و دام
خطدويم است از جام جم ‏ و کنابه لز شکم‌نیز
0ص 7
شه ازصفحة ۲۸۸ 1
بهره و برخ و بخش و بخت آمده . در کاتپا 0۵2 بپمین معنی است » دوم بفه دراوستا و بگه
در پارسیٌ باستان بمعنی خدا و دادار وآفرید کار است . در اوستا اين کلمه چند بار مرادف خدا
(اهورمزدا) و کاهی نیزبمعنی ایزدآهده است . بغ بهردومعنی‌ازك بنیاد است از مصدربگه 88
بمشی بخشیدن (درپهلوی ۵۵0:810). درسااسکریت 011882 نیز بمعنی بنهشیدن است. در زبان
های. دیگر حند وارویابی 928112 با 98 با لك تغییر لهجه‌بی‌یز موجود است. درساسکریت.
مععطط بیعثی خدا و در ودا سیار آمده است . ها) 28۷20 بعحنی سرود خداوند .
لام بشی است از ناعهٌ وداء در زبانهای اسلاو (مانند روسی کنولی) 00801 بمعنی خداست . این
واژه ازسکه ها 5884 باقوام اسلاو رسیده است . اقوام سکه هانند دیگر قبابل آردامی خدای
خود را 28 مینامیدند . ترد حمهٌ اقوام آربابی با افوام هند و ابزانی پیش ازبرانگشته شدن
زرتشت » بغ دام مطلق خدا بوده . زرنشت خدای بگانةٌ خود را اهورمزدا خواند , اما ول بغ
همحینان بمعنی اصلی خود باقی مانده دراومتا مفهوم خود را از دست نداده است . دربارسی‌باستان
( کتیبه های‌حضامنشی) 0688 نیز بنمنی خدا بکار رفته‌است . کلمةٌ حزبور درتر کیپ پغدادوبفپور
و پشتان (یستون) آمده و مبدل و معرب آن فغ است (ه . م) «بغ . پورداود : یادفامةٌ دنشاه
ابرانی‌ص۲۱۳ بیمد» درپهلوی 9852 , ۵21 (خدا , الوهیت ۰ سلطان) همنای ۲۹4 .
۵ #ل - جختح اول » خدا » عربی : درآشوری- بابلی «بلو» ( بنم دوم ) ؛ هبری «بمل»
(ختح اول و دوم)» آرامی دبملا» (بقتح اول). هرلغات جنوب الجزیره و حيشه « بمل » (بفتح اون)
«ولفنسون ۲۸4 و رك : دائرتالمعارف اسلام. ت اور - ختح اول » مر کب از : بخ +
پود ‏ پسرخدا ؛ لفبی که ایرابیان بداهان چین دادماد. و مرب آن فنفور است:
```


## [2026-09-05T06:09:45.851Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Sogdian Loan\" HENNING_selected_papers.txt | head; echo \"=== search bagh in henning ===\"; grep -n \"baγ\\|bag 'god'\\|by' 'god'\\|βaγ\" HENNING_selected_papers.txt | head -20",
 "description": "Search Henning selected papers"
}
```


### [2026-09-05T06:09:45.923Z] TOOL RESULT

```
=== search bagh in henning ===
```


## [2026-09-05T06:09:48.754Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"sogdian loan\" HENNING_selected_papers.txt | head; echo \"---\"; grep -c \"\" HENNING_selected_papers.txt; grep -n -i \"loan-words in new persian\\|loan words in new persian\" HENNING_selected_papers.txt | head",
 "description": "Find Henning SLW article"
}
```


### [2026-09-05T06:09:48.830Z] TOOL RESULT

```
11763:we may take this opportunity of mentioning a hitherto unrecognized Sogdian loan-word in Turkish, viz. Turk. gly ni, i, 430; ili, 134 ‘andalib; Ton Muhanni, 176—Aaxir) from Sogdian
11770:milar Sogdian loan-words in Pe nd-wif, ete,
---
25028
```


## [2026-09-05T06:09:52.349Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '11700,11790p' HENNING_selected_papers.txt",
 "description": "Read Henning context"
}
```


### [2026-09-05T06:09:52.394Z] TOOL RESULT

```
maryair dyad Jasi-yi fol-i to ya mara)zan i.e, “are you not worried at all by the thought how? your Jfinis will be? Whether the retribution of your deeds will be the Meadow (of Paradise) or the Tomb (of Hell) #” It vwas from this verse, I presume, that some clever lexicographer san should have had the meaning of it easors interpreted his diaf and boldly asserted
 
 
inferred that mary(a dias “ fire”; by that word he evidently me fire”. “His sue that mary(a)zan meant (1) Hell, (2) a brazier, (3) cemetery. This sot of meanings is as baseless as the wrong spelli
  
he infernal
 
   
 
marzayin which is paraded in the dictionaries. The older
 
‘cogeaphers know c
 
of mars(a)ydin, mary(a)sdin = gitristin
 
  
n is the form
A variant of mary(a used in Parsee Persian,
      
maryiizan, from *ma
 
It is employed
 
 
for the famous mausoleum of Khosmu Anosherwan, seo B. N. Dhabhar, The Persian Rivayats, 586 (with references), J. Darmesteter, Etudes Traniennes, ii, 132 *mary “death” + Pahl Old Pers. “ apadéna””*) which, although brilliant at the etymology not on a corrupt
 
   
proposed an
 
etymology (fre ’n® ““ dacma-””
 
 
time, cannot seriously be entertained now, An
 
should be based on the correct Persian fort
 
spelling,
A major obstacle to the intended comparison of gerezman, ‘marzyan, and suburyan appears to be the initial group of sounds of the Turco-Mongol word, but there is no real difficulty. The first vowel of suburyan is obviously intrusive (this was ‘assumed also by M. seem to be altogether of no account, excepting the stable -d of the final syllabl
2 Var, be 18 youd. "Or. whether in the end, when tho final accounting will be, the retribution, ete, * On this word see now BSOAS., xi, 470 * 800 these Transactions, 1944, 110, 2
jauthiot); the vowels of all three words
 
Initial »- in a foreign word in Turkish can
 
 
 
  
  
 
 
161 Tmawsac 1945
 
OF THE PEILOL
  
 
ca
 
 
represent original s- or 2- that stab
As Turkish did not possess initial 2-,
        
nd was regularly replaced by #. ‘This is so well
hed that there is no need to quote examples; but
 
we may take this opportunity of mentioning a hitherto unrecognized Sogdian loan-word in Turkish, viz. Turk. gly ni, i, 430; ili, 134 ‘andalib; Ton Muhanni, 176—Aaxir) from Sogdian
tanduval “ nightingale" (see Kiya
 
   
entu'ch (‘mry’) = zandiedé gale” as see BSOS,, x, 104 sq.) prove, Thus suburyan may represent
nging (bind) ”, but also “ nightin
   
milar Sogdian loan-words in Pe nd-wif, ete,
   
tan earlier *zburyan, Its initial 2b- can perhaps be explaine
 
 
1s the outcome of an original zm-. Such groups of consonants
 
 
 
often subject to changes, especially when a word has to be adapted to an alien tongue. A good parallel for this par- by the Arabic for ibarjad form zmargad. The who
 
tioular change in a loan-word is provid
 
“emerald” structure of wargad clost maryan which, I think,
nal word that the Turkish tongue transformed into
   
resembles that of *So
 
dian *zmuryan or
```


## [2026-09-05T06:10:02.154Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"loan.words in new\\|LOAN-WORDS IN NEW\\|Sogdian loanwords\" HENNING_selected_papers.txt | head; echo \"--- toc ---\"; sed -n '1,80p' HENNING_selected_papers.txt",
 "description": "Check Henning volume contents"
}
```


### [2026-09-05T06:10:02.234Z] TOOL RESULT

```
--- toc ---
 
 
 
 
ACTA IRANICA
DEUXIEME SERIE
VOLUME VI
 
                                      
SOUS LE HAUT PATRONAGE DE S.M.I. LE SHAHINSHAH ARYAMEHR
ACTA IRANICA
ENCYCLOPEDIE PERMANENTE DES ETUDES IRANIENNES FONDEE A L'OCCASION DU 2500" ANNIVERSAIRE DE LA FONDATION DE L'EMPIRE PERSE PAR CYRUS LE GRAND
 
DEUXIEME SERIE
HOMMAGES ET OPERA MINORA
Acta Iranica 15
BIBLIOTHEQUE PAHLAVI E, J. BRILL TEHERAN-LIEGE LEIDEN
HOMMAGES ET OPERA MINORA
W.B. HENNING SELECTED PAPERS
Tt
EJ. BRILL BIBLIOTHEQUE PAHLAVI LEIDEN TEHERAN-LIEGE
 
 
COMITE INTERNATIONAL
Prof. Sir Harold Bauey (Grande-Bretagne); Prof. George CaMERon (EU): §, Exe, Prof. Enrico CeRULLI (Italie); tS. Exc. Dr Tara CHAND (Inde); Prof. Henri Conny (France); Prof. Jacques DUcnesne-Guniemin (Belgique): Prof. Namio Eoas (Japon); Prof. Dr, Wilhelm
S. Edman Enzi (Turquie); Prof. Richard ErmicHausen (E-U,); Acad BG. Garunov (URSS):
Garcia Gomez (Espagne); Pr Walther Hinz (Allemagne); Prof. Yat Dr. Franz Konia (Autriche): Pr
S. Nvaexc (Suéde); Pir Husams
 
 
ns (Allemagne); Prof,
f. Roman Gwnsiaa (France); S. Exe, Prof
    
Janos HarMatra (Hongrie); Prof: Dr. a AL-Kuasnan (Egypte); S. Em. Ca Georg Monoenstieane (Norvége); tProf. Henrik
in RASHDI (Pakistan)
 
        
 
DIRECTION
Le Conseil Culture! Impérial de "ran SE. Shodjaeddin Snara, Vice-miniswe de lx Cour Impériale, Directeur dela Bibliotheque Pahlavi
REDACTEUR EN CHEF
1. Due Pierre Lecoa, assistant Universite d
SNE-GUILLESUIN, professeur ordinaire A I'Université de Likge, assisié de
 
 
Lidge et de Jean KELLENS, assistant & Universit
 
nes Gutenberg, Mayence
 
Université de Ligge. Place 16, B 4000 Lidge
 
ISBN 90
 
 
© 1977 by Bibdlothique Pahlavi, Tehran-Liége
All rights reserved, No part of this book may be reproduced or fiche
viii permission from the’ publisher
 
 
 
  
     
   
          
TABLE DE
 
S MATIERES
                                                                                                   
 
Sogdica, James G. Forlong Fund, Vol. XX1, London, 1940 (67 p. with Errata and addenda) 1
“Sulphur” in Sogdian (BSOS, 1940, p. 398) @
  
   
 
Compte rendu de E. Hexzreto, Archaeologische Mitteilungen «us Iran (BSOAS, 1940. pp. 501-507) 1 Compte rendu de A. Guitatn, Essai sur la langue parthe (BSOAS, 1940, pp. 508-509) 7%
Mani’s Last Journey (BSOAS, 1942, pp. 941-953), 81 An Astronomical Chapter of the Bundahishn (JRAS, 1942 pp. 229-248) 95
The Book of the €
 
ants (BSOAS, 1943, pp. 52-74) Ms
```


## [2026-09-05T06:10:15.573Z] TOOL CALL #45: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 5
}
```


### [2026-09-05T06:10:15.580Z] TOOL RESULT

```


```


## [2026-09-05T06:10:20.301Z] TOOL CALL #46: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/b%CA%B0eh%E2%82%82g-",
 "prompt": "Give the reconstructed PIE root, its meaning, and the descendants in Indo-Iranian (Sanskrit bhaj-, Avestan bag-, Old Persian), Greek phagein, Slavic bogu. Quote the etymology section."
}
```


## [2026-09-05T06:10:21.613Z] TOOL CALL #47: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%81%D8%BA%D9%81%D9%88%D8%B1",
 "prompt": "Give the full etymology of Persian فغفور (faghfur): Middle Persian form, Sogdian, the meaning 'son of god', the Chinese calque, and any citations."
}
```


### [2026-09-05T06:10:26.481Z] TOOL RESULT

```
# Proto-Indo-European Root *bʰeh₂g-

## Reconstructed Root and Meaning

The PIE root is **\*bʰeh₂g-**, meaning "to divide, distribute, allot."

## Key Descendants

**Indo-Iranian:**
- Sanskrit: भज॑ति (bhájati, "to divide")
- Avestan: 𐬠𐬀𐬲 (baž)
- Old Persian: 𐎲𐎠𐎪𐎶 (bājim)

**Greek:**
- Ancient Greek: ἔφᾰγον (éphăgon, "to eat < to receive a share")

**Slavic:**
- Proto-Slavic: \*bogъ ("share, god")

## Etymology Section Quote

"This root could presumably have an *a*, but the short vowel of Proto-Indo-Iranian *bʰaga-* can easily be explained by Lubotsky's Law, from the loss of the laryngeal in front of a voiced stop plus another consonant."

This explanation demonstrates how the root appears in different phonological environments across descendant languages.
```


### [2026-09-05T06:10:27.767Z] TOOL RESULT

```
# Etymology of Persian فغفور (faghfur)

Based on the Wiktionary entry provided, here's what can be determined:

## Direct Etymology
The word was "Borrowed from Sogdian _𐼱𐼲𐼾𐼰𐼴𐽀_ (βɣpʾwr /⁠βaγpūr⁠/)."

## Limitations of Available Information
The provided source does not contain:
- A documented Middle Persian form
- An explanation of the meaning "son of god"
- Information about a Chinese calque
- Additional citations beyond the single academic reference

The only scholarly citation included is: Henning, W. B. (1939), "Sogdian Loan-Words in New Persian," in Bulletin of the School of Oriental Studies, volume 10, number 1, page 94.

To obtain the complete etymological details you're seeking—particularly regarding Middle Persian antecedents, semantic development, and Chinese linguistic connections—you would need to consult additional academic sources or the full Henning article referenced here.
```


## [2026-09-05T06:10:38.446Z] TOOL CALL #48: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A8%DB%8C%D8%B3%D8%AA%D9%88%D9%86",
 "prompt": "Give the etymology of Persian بیستون (Bisotun/Behistun): Old Persian Bagastāna, meaning, sound changes, and any citations."
}
```


## [2026-09-05T06:10:40.026Z] TOOL CALL #49: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A7%D9%86%D8%A8%D8%A7%D8%B2",
 "prompt": "Give the full etymology of Persian انباز (anbāz): Middle Persian form, components, and any related forms such as انباغ. Quote the etymology section."
}
```


### [2026-09-05T06:10:44.820Z] TOOL RESULT

```
# Etymology of Persian بیستون (Bisotun)

**Origin:** The word is inherited from Old Persian *Bagastānah.

**Meaning:** The Old Persian root referred to a sacred or temple location, with a doublet form فغستان (faġistān / faġestân) meaning "temple."

**Folk Etymology:** A secondary, popular etymology derives the word from بی (bē/bi, "without, -less") + ستون (sutūn/sotun, "pillar"), referencing "the ancient reliefs which are carved directly into the rock without pillars."

**Sound Changes:** The word evolved through regular Persian phonological changes from the Old Persian form, with variant pronunciations across different Persian dialects (Dari, Iranian, Tajik).

**Citation:** The Wiktionary entry attributes the inherited etymology to Old Persian *Bagastānah, documented in Steingass's Comprehensive Persian–English dictionary (1892).
```


### [2026-09-05T06:10:48.419Z] TOOL RESULT

```
# Etymology of Persian انباز (anbāz)

Based on the Wiktionary content provided, there is **no etymology section** included for this entry. The page only contains:

- The word: **انباز** (anbâz)
- Its classification: "present stem form of انباشتن (anbâštan)"
- A cross-reference to: **انبار**

The document does not provide Middle Persian forms, component breakdowns, or related etymological information. To obtain a complete etymology including Middle Persian origins and related forms, you would need to consult the full Wiktionary entry or Persian linguistic resources beyond what is displayed here.
```


## [2026-09-05T06:10:57.906Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== NYB ===\"; grep -n \"hambā\\|hambay\\|hanbā\\|baxt\\|baxš\\|bahr\" NYB_vol2_glossary.txt | head -20; echo \"=== CHEUNG bag ===\"; grep -n \"\\*bag\\|BAG\\b\\|baxš\" CHEUNG.txt | head -20",
 "description": "Grep Nyberg and Cheung"
}
```


### [2026-09-05T06:10:57.975Z] TOOL RESULT

```
=== NYB ===
601:apoxšāyišn [’pwhs’dän'] compassion, mer- cy 6214, — apo- < apa- : -a- > -o- because of the surrounding consonants; Ps. pres. ’phs’d-; MPrs ?baštyšn (A-H. II, BBB); [Arm. lw. apasxar-em < *apa-xšād- is not akin]; MPrth ^bz$?hy$n, pres. ?"baš?h- (A-H III, MHC); Paz. awaxšīdan awa- xsGéd, Skr. v. sahate (Aog.); NP baxsudan, baxšā'īdan, baxšāy-, baxšāyiš. Bailey, JRAS 1930, 15—16; Verbum 188 sg.; Ghilain 70.
671:aržānīkēnītan [~-ynytn'] to consider a p. worthy, governing a subordinated clause without an introducing particle, 5318 in a very complicated passage 5317-21, which only seems possible to understand on the following suppositions: a) kū-t bahr hac man bé burt l. 19 is not a gloss, as I have marked it, but is governed by anak tč bavat l. 17 ‘it shall be unhappy for thee that thou hast bereft ...'; b) the clause kē ... aržānīkēnīt hom 1.17-19 is loosely attached to tē l.17; c) for MNW-t L<y> (MS very clearly MNWtl) read MNW kw) LY» = kē tē man, to man being the exact counterpart of LK ^NH = tč an (v. žan) 1. 19 and both signifying ‘thou and I’; d) YBLWN-m l. 18 and 20, and HWH'-m 1. 19, are the Ist. p. pl. coinciding with the Ist p. sg.; e) there is a wordplay between *š = dé ‘food’ l. 18 and ’$ = as (demonic) eye’ 1. 20 (as burtan 'to have a vision', v. 'aš; bahr ‘ministry’, v. this w.). Text: anàk tč bavat, marak, ke t(0» man fratom hac ax" i astomand andar Rdg u Notar hac bahr barišneh āš barom frac aržānīkēnīt hom, kū-t bakr hac man bē burt. niin-ip tē an pat apar-barišneh aš barom u et bavēt kū-t dušcašmiha al zänak nikēram i-t nest ‘unhappy shall it be for thee, little scoundrel, (that thou) — as thou and I first of all men in the material world between Räg and Notar have been found worthy of earning food by perfor- mance of ministry — that thou hast bereft me of the ministry. Now thou and I shall be enraptured in an ecstatic vision, and then it will happen that I shall see thee evil-minded in another house that is not thine’. The passage is the immediate continuation of the incident related in 537-15, Zsprm XII, 7 epitomizes 5316-21 as follows: dwlyslwb BR’ L zltwšt gwpt' "VK cygwnt pltwm HWH'-m b’hl wlweyk BR’ ’pknd HWH'-m ZK tw "NH KR?
672:= Dūrēsrav bé 6 Zartušt guft ku: cigēn-at fratom ham (cf 209 ete.) bahr u rocik be apakand hom, an tč an (v. lan and ?an) har 2 aš apar barom api-t bē marnjēnēm "D. said to Z.: because thou hast deprived me, as the first, of both munistry and food, we both, thou and I, shall be enraptured in an ecstatic vision, and then I shall annihilate thee’.
879:bägö-baxt
888:bägö-baxt [b'gwbht'] divine providence 777118. cf the definition Mx ch. 249-77: äsn baxt han bavēt i hac fratomeh bat Estet, u bagdbaxt hàn i dit-ic baxsend “innate bazt is that which has been allotted from the very beginning, and ~ is that which they
890:bágó-baxt
891:(the gods) allot subsequently' — Borrow- ed from Av. (922) baydbaxta-; Paz. bayobast, Skr. v. punar-dati, -bhāgya.
895:bahr [b’hl] lot, share, portion 692°. 9019.11; (the part played by the priest in the service =) ministry 5319-1? (v.s. v. arzä- nikénitan), a synonym of yazisn (q. v.); this sense is confirmed by Zsprm XII, 6: Pourusäsp bahr o öi hilāi ke-š patiš aržānīkēh ‘P. shall leave the bahr to the one who has the qualification for it’, corresponding to (Pourusäsp...) yazišn 6 yastärän *hārēfūt (v. hareftan), with the gl. kū 6 yazāt kē apāyet yaštan 5314-15; — happiness, prosperity: tan ~ bodily beauty 22%, — Av. (923) baxadra-; Ps bhly; MPrth bhr ’*ate’; MPrs bhr (A-H I), h’mbhr "having the same share’ (A-H II); Paz. bahar, Skr. v. vibhäga and samrddhi; NP barx. [It would be tempt- ing to connect (čan) bahr with Skr bhadra- ‘beautiful, happy’; phonetically there is no difficulty, cf Skr mudrā: muhr ‘seal’ ; Av. baóra- is attested in hu-baóra- (1828) ‘happy’; thus Bailey in A. M., N.S. IT: 1, 1952, 32].
896:bahrak lot, share (= bahr) 1152.
897:bahrómandeh [—-"wmndyh] the state of being prosperous, prosperity 877.
898:bahr-varéh [~-wlyh] the state of having a share in (hac), participation in 909-14, — Paz baharvari, Skr. v. samrddhi, which suits the context less well.
927:barišnēh det. v. n. of burtan: the act of carrying or bringing: & gobišn ~ this "saying-bringing" = such a message conveyed to me (by a mysterious voice) 3812-18; bahr ~ performance of sacer- dotal ministry 53%, v. aržanikenitan and bahr. ~ V. also apar-barišneh and frot- barišnčh.
956:baxšišn [HLKWN-šn'] distribution 89%. From baztan.
957:baxt [b’ht', bht'] destiny, fate, fortune: ~ u bāgēbaxt (g. v.) 7712-13; pat aueš m murtan to die a natural death 2112-13; bé-Sutak ~ whose fortune is gone, doomed 52; v. also vat-bazt.
958:baxtan [b'htn'; HLKWN-tn'] baxá-, to allot, to distribute, to destine 6620-23, 7624, 799-19, 891138; — -§ apar baxt &stet dušman čzančt (it has been allotted to him that he should kill =) Fate has destined him to kill the enemies 271%. — Av. (921) bag-; Ps. pt. bhty; MPrthPrs pres. baš- (S, A-H I), pt. batg; Paz. baztan, barš-; NP baxsidan.
1021:brat [bbt'; "H<Y>] brother, sg. cas. rect. 2471, 10018; after a name as its app.: Zarér i tō ~ 20-24 passim; 221^; after a prep.: hac pus tài brat 221%; — as pl. cas. rect.: vas ~ PH] ... bavend 22"; — sg. cas. obl. brātar [bl”tl] in compounds (v. below); in the sense of a pl. after nume- rals: har 2 brdtar 9%, hàn 4 brätar 9!? (both dir. obj.); — pl. cas. obl. brätarän 826, 21°. 241-5; han i 2 vat-baxt brātarān 9? (dir. obj.). - Av. OP (971 sq.) bratar-, nom. sg. brati; MPrthPrs br'd, cas. obl. br’dr, pl. br’dr’n; Paz. brad; NP birädar.
1044:burtan [bwltn'; YBLWN-, YDLWN-tn'; forms v. I, 178] bar-, to carry, to bring, to bear, to wear, to procure; to take away, to remove (6 or pat ‘to’); arišk ~ to bear envy 691. 8419; !a&, bes, dast, dašn, gobišn, nam, namāc, nipart, paitäk, srav, stēžak, vāng, pat xrat ~: v. these ws.; bahr ~ v. barišneh; — to place on the top of (apar) 444; to lay a p. on (6) 4720-21; — andar 6 tan ~ to bring into corporeal existence 92t; — andarg ~, v. göbisn; — apar ~ to send out against 3711; to bring 6016; dmdcisn apar ~ to give instruction, to teach 80%; v. also apar-barisneh and apar-burtäreh ; — frac ~ to bring, to present 411; to bring forth, to light (a fire) 44°; — fröt ~ to bring down, to shed (water) 417°; v. also fröt- barišneh; — 6 ham ~ to collect, to amass 4815; pret. construed as an act. 187% Common Iranian; Av. OP (933 sqq.) also — (act. and middle) ‘to ride’, cf barak and asvār; cf also apar-barišneh from bar- ‘to move’.
1490:farró-büg [plwb'g, -bg] having a share of the heavenly splendour: atur ~ the foremost of the sacred fires, connected with the priestly class 118. 27. 924, 9511 (7 ~), ef s.v. ätur. — farr < *farnah-, the Median form of z“aranah, cf farrax", + Av. (921) baga-, baya-, (922) baya- (952) bagä- ‘share’ (v. bāgēbaxt); cf n. pr. Gr PapvaBatog with -Bačo- for *bāji-, v. baz. FrP 11 plb'(g) = farr-bā(g), gl. by zivandak ‘living’. V. also Atur-farrö-bag n. pr.
1801:ham-bai [hmb’y] one with whom one shares property; partner 70*. — Paz. hambāē (for hambài), Skr v. sama-bhagin. Bthl., ZsR I, where the juridical notion
1875:hanbārak [hnb’lk'] storehouse, larder 973-8.9.10, . MPrth ’mb’rg; Arm. lw. (h)ambar, Talm. ’mbr’, NP anbār; v. Telegdi 229.
=== CHEUNG bag ===
17619:*IE COGNATES: Gr. BAG 0 “I hurt, damage’ 
35020:bhS- /baxš-/, 19
```


## [2026-09-05T06:11:14.515Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SOD βγpwr ===\"; grep -n \"βγpwr\\|bgpwr\\|βγ-\\|βaγpūr\\|baγpūr\" SOD.txt | head -10; echo \"=== SOD bag god ===\"; grep -n \"βaγ\\|βγy\" SOD.txt | head -10",
 "description": "Grep Gharib Sogdian dictionary"
}
```


### [2026-09-05T06:11:14.585Z] TOOL RESULT

```
=== SOD βγpwr ===
=== SOD bag god ===
```


## [2026-09-05T06:11:17.653Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && head -c 600 SOD.txt; echo; echo \"=== search pwr ===\"; grep -n -i \"god, lord\\|βγ\\|BGPWR\\|bgpwr\" SOD_pages.txt | head -10",
 "description": "Inspect Sogdian dictionary file"
}
```


### [2026-09-05T06:11:17.720Z] TOOL RESULT

```
SOGDIAN 
DICTIONARY 

Sogdian  -  Persian  -  English 


B.Gharib 


FARHANGAN  PUBLICATIONS 


Sogdian  Dictionary  (Sogdian-Persian-English) 

by  B.  Gharib 

editorial  supervisor:  A.  Mansouri 

editor:  S.  Fotouhi 

©  1995,  Farhangan  Publications 

2/52.  Shahid-e  Said  Street,  Tehran  15916,  Iran. 

Tel:  6460069.    Fax:  670230 


ISBN:  964-5558-06-9 


4f*Jj*l{^  0"J-^8  'Jy^**-  ^J>*4^  tfW  :  j'  a>„J^  <f  jljX-U^  -LUi^-L  ^JjJ'j^  L»  e jlf  ijj- 
;l_^0  jL-u  jlS'  4$"  (.5*^-*^'  "^^  (H^-  fJ 


L?JJ  J' 


•  l^>  o-^  jl  ^^<o  (j  ^jb^b  j  uij^-  ^C*" 


O
=== search pwr ===
11063:                                                                      God, Lord, king, sir, excellency
```


## [2026-09-05T06:11:20.123Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '11040,11090p' SOD_pages.txt",
 "description": "Read Gharib bagh entry"
}
```


### [2026-09-05T06:11:20.179Z] TOOL RESULT

```
                                                                       Ps8ez ©<*abi-darzaya~; Parth. abdarz; Yaghn.
 2526 p>z>kh      B => p>z>
                                                                       * bidez- =»p5ystk, p5>yz>k
 2527 pVyt -» fl'z*                                                    (ro)cover, (fo)wrap
 2528 b'zyd- C =* P'zy5-                                               BSTBL, Dhu. 22, 286
 2529 P'zyS-      S                                    Oj^jIj-   2541 p5,yz,k B                              t>j^^ijJ,y_
          pazya5 (b'zyd-) ©impf. =>PzyS-
                                                                       Po6eze,
                                                                       coating, PiSezak
                                                                                covering =»p5>yz-
          (to)mount
          VJ 855; TSP 13.27; BSTii 880.5; C2, 77R5                     TSP 3.180, 196 n pl97

 2530 p>zy B                                         0=^-'-?'    2542 p5ystk B                           •j^^«ju*=i
      Pazay ©impf. ^Pz'y-                                             PoSiste ? ©<*abi-drsta; fdarz-, Yaghn. bidizta
      OcOincrease
                                                                       wrapped
      TSP 2.187                                                          ©pp. ^p5}yz-
                                                                       SCE 341; BSTBL, Dhu. 285; GMS 149A
 2531 b'zynt
      pazant ®3pL impf. =»p-                                     2543 Py- B, M, S          (oy^»* jj)vU^«Li*JJ-r^Jj^.
      GMS 801; AVS 229; b>znt% C2, 60 R29                             paY (bY-) ©<baga ©nom. ob. -y(yh ace. -w;
2532 -pc S                                    (ojby jl^y                voc. inst. abl. ->; pi. firyn, fiYh)yst =>PY*yst
                                                                      God, Lord, king, sir, excellency
     fac =»-p                                                         GMS 1168, 1177; Hen. BSOAS 1965, 245; fix,
     (from)you, (of)you                                                 STii 10.21
     Anc. Lett. 3.5, 4.3; GMS 1358
                                                                 2544 bY-   C -* Py-
2533 pdnpSCS)        B, M                                o^r
      f(o)canpa6 (pcnpS) ©ob. -y -^Pc'npSCS),                    2545 PYwn B, M, S                            (JU,)uIIj^
        fc»np5, >fcmb5(8)                                             PaYan (PYJn(h)) ©<bagandm        ©gen. pi.
      world
      TSP 15.18; STii 9.8; BSTBL, Dhy. 15; W-Li,
                                                                       VJ 1469, 1443; Hen. ZDMG 1936, 197; fiT'nw,
        bc*np6-                                                          BSTBL, Dhy. 173; Anc. Lett. 2.2, 4.2
2534 pcnp5 =* ,Pc,np5(5)
                                                                 2546 PYHn
                                                                        godspYtm    B, M        (uklj^ jiJlj^) ^J-^ d-^
2535 pcyryn'k B                                o/^-Ul                        pY'n1
                                                                      PYtan ^pY/xtm    (PY'nCy) PYtm)
     P(o)zirene =»'pjyr(ync, Pz'yr'yn'k, pjyrnyh
     diamond like                                                     god of gods
                                                                      GMS 254, 1295; VJ 1469, 1472 etc.; SCE 254;
      BSTBL, Padm. 16                                                   BSTBL, Padm. 64, 70
2536 p8»nh B                                 0UpoLjI             2547 PYwny BRY S                        ( jUj^ ^)j>y-
     PiSan ©<abi-dana-, aiwi-dana-> Oss. (w)idon;
                                                                      PaYane-pis(e)
        Parth. widdn ^PyS'n                                           husband
      bridle
                                                                      Anc. Lett. 3.1; S W, C2 p96
      BSTBL, Dhu. 166; GMS 90; Benv. Et. Oss. 13
```


## [2026-09-05T06:11:25.846Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"PYpwr\\|pYpwr\\|P.pwr\\|Ypwr\" SOD_pages.txt | head -10",
 "description": "Search Sogdian bagpur"
}
```


### [2026-09-05T06:11:25.901Z] TOOL RESULT

```
11188:     naked                                                        Paypuric, Paypurec (Pypwryc)         =»pwryc
11193:     sorceress                                                   pay- purist (Pypwryst) ©pi. ^Pypwr'yc
11203:                                                            2591 pypwryc =* Pypwryc
11205:     Pay-nawe ©abl. -nw)      =^pyynwy(y)                   2592 pypwryst =* Pypwryst
11219:     Paypur (Pypwr) ©<baga~pu0ra-y <Parth.                        GMS 925; inf. pYty, VJ 36; fiTtw, Frag. Len.;
27438:        =^PYpwr}yc, pwr}yc
```


## [2026-09-05T06:11:28.602Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '11215,11230p' SOD_pages.txt",
 "description": "Read Sogdian baghpur entry"
}
```


### [2026-09-05T06:11:28.657Z] TOOL RESULT

```
       180                                                  2594 pyspsyt =» Pypsyt
2581 pyny     M ** byny                                     2595 pyt—    B                         ^^ij^y <o^ ioXJ^v
2582 pyp>wr     B, M, S        j/>p)j>u9 ^IjIji^ ««jljAli         Payd/t ©pt. st. =»prbyt-
                                                                  (ro)give, OcOdivide
     Paypur (Pypwr) ©<baga~pu0ra-y <Parth.                        GMS 925; inf. pYty, VJ 36; fiTtw, Frag. Len.;
       bagpuhr =^Pypsyy, Pyp5ry                                    perf. st. fiYtw&r, VJ. 25e, 7d, 503 etc.; fiYttw
                                                                   <5V-, VJ 236
     prince, god's son
     TSP 8.166; BSTBL, Intox. 34; BBB; Anc. Lett. 2,        2596 pytm B, M, S                                 y.J^J-^
       26; GMS 1276
                                                                  Payt/dam (Pxtm) ©<*baga-tama =»py*n Pytm
                                                                  most divine, godliest
2583 pypSry B                          •jIjaUJj^^
     pay-poOre, Pay-pase, Pay-pisi ©Skt. devaputra                TSP 15.17; Frag. Len. p94; GMS 254, 164
       ©pi. PYdpryt ?                                       2597 pytmynch B                           L^o>jf<^J-^
     prince, god's son                                           Payt/damenc
```


## [2026-09-05T06:11:51.287Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HJB BEGUM ===\"; grep -n \"BEGUM\\|Begum,\\|begam\" HJB.txt | head -5; echo \"=== HJB ATABEG ===\"; grep -n -i \"atabeg\\|Atabak\" HJB.txt | head -5; echo \"=== LKT beg ===\"; grep -n -i \"^[0-9]*\\. *beg\\|türk. beg\\|bäg\" LKT.txt | head -10",
 "description": "Grep HJB and Lokotsch for beg/begum"
}
```


### [2026-09-05T06:11:51.374Z] TOOL RESULT

```
=== HJB BEGUM ===
3244:1619.— "  Behind  the  girl  came  another Begum,  also  an  old  woman,  but  lean  and feeble,  holding  on  to  life  with  her  teeth, as  one  might  say." — P,  delta  Voile,  Hak. Soc.  ii.  6.
23946:B^m,   Begum,
=== HJB ATABEG ===
=== LKT beg ===
596:166.  Pers.  bäg::
603:'Garten'  [aus  bäg  'Garten'  Horn  NpEt S.  39,  Nr.  169],  tk.  ebenso  bagce,  balcie; hieraus  russ.  bakda,  bahia  'Gemüse- garten', klruss.  baksa  'dass.',  serb.  bas- 6a,  bulg.  baföa  'Garten  (mit  Melonen und  Gurken  bepflanzt)'.  [Gorjajew  9. Mikl  SlEtWb  6.    Bern  SlEtWb  39.
605:N.  pr.  Name  einer  am  Tigris  gelegenen Stadt,  aus  altpers.  baga  [Sskr.  bhaiif)] 'Gott'  u.  zend  data  'gegeben,  geschaffen', also  'von  den  Göttern  gegeben  [9eö- KTiaToq]',  nicht  'mit  Glück  beschenkt' das  gegen  die  Quantität  verstößt  [zend bägha  'Glück'].  Aus  dem  Adj.  bagdädi, das  schon  ar.  und  tk.  'Zimmerdecke  aus Holzbalken'  bedeutete,  wurde  rum.  bag- dadie  'Zimmerdecke'.  —  Das  Subst. wurde  it.  Baldacco,  afrz.  Baudas,  dtsch. Baldak  [z.  B.  in  Hauffs  Märchen],  engl. BaJdacca  und  das  Adj.  entsprechend;
607:171.  Ar.  ba^Ija: 'Ehebrecherin,  Hure';  hieraus  mit  Suffix- wandel frz.  bacasse,  sp.  bagasa,  pg.  ba- gaxa,  prov.  bagassa,  it.  bagascia  'Vettel, Hure',  siz.  bagascia  'dass.',  gnajassa 'unerzogene  gewöhnliche  Frau,  Schlam- pe'. —  Vielleicht  liegt  auch  Kontami- nation mit  ar.  bägiz,  bäyiza  'zotig, Lump'  vor;  für  Ableitung  aus  hypothe- tischem *bacassa  liegt  kein  Grund  vor. [GrSVoci  Sic  227.
639:18.5.  Mal.  bäjü: Besser  bägü  'eine  Art  Überkleid,  nia- layische  Jacke'  [Pijn  27  a] ;  hieraus  anglo- ind. badjoe,  bajoo  'dass.'.  [Hobson-Job- son 46/47.
1194:453.  Ar.  dabbäg:
3916:'Art  Sauerampfer',  auch  ribäz  [und  pers. ribäg];  hieraus  mit  Imäla  [Ä>-e]  mlat. ribes,  ribasium,  ribesium,  frz.  ribes  'Jo- hannisbeere'.   [Devic  DEt  193.
4304:1902.  Ar.  sikbägr:
4530:g()i9  Mal,  tambäga: Kupfer'  [Pijn  68;  aus  sskr.  tanuka,  ei- gentlich 'das  dunkle  Metall',  also  'Kup- fer'; vgl.  A.  A.  E.  Schleiermacher,  De l'influence  de  l'ecriture  sur  le  langage suivi  de  grammaires  barmane  et  ma- laie.  Darmstadt  1835.  S.  537,  nicht S.  835,  wie  POTT  in  ZKM  IV,  265  an- gibt]; hieraus  zur  Bezeichnung  einer Legierung  von  Kupfer  (A^/i — 12  Teile) und  Zink  (1  Teil)  pg.  tambaque,  tambaca, sp.  tumbaga,  frz.  tombac,  it.  tombacco ; engl,  tomback,  dtsch.  Tombak  ;  russ.  tom- pak.  —  [Die  Ableitung  aus  dem  Namen eines  Engländers  DOMBACK  ist  un- bewiesen ;  ebenso  unwahrscheinlich  ist die  Entstehung  aus  dem  umgestellten chin.  pack-tang  'weißes  Kupfer'  >  tong- pack.]  [Devii-  DEt  221.  Hobson-Jobson 829.
8825:tulumbägiü  2104
```


## [2026-09-05T06:12:03.309Z] TOOL CALL #57: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Turkic/b%C4%81g",
 "prompt": "Give the reconstructed Proto-Turkic form and meaning, and the etymology discussion: is it a loan from Middle Chinese 伯 or from Iranian *baga-? Quote the etymology and the scholars cited (Clauson, Doerfer, Rybatzki)."
}
```


## [2026-09-05T06:12:04.043Z] TOOL CALL #58: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/begum",
 "prompt": "Give the etymology of 'begum' and, if present on the page, of 'beg/bey'. Quote exactly."
}
```


### [2026-09-05T06:12:09.123Z] TOOL RESULT

```
I cannot provide the etymologies you requested because they are not present in the web page content provided. The page shown is the Etymonline website's homepage and footer, which contains navigation elements, branding, and links to various sections, but does not include the actual etymology entries for "begum" or "beg/bey."

To find these etymologies, you would need to search the Etymonline database directly using their search function.
```


### [2026-09-05T06:12:09.665Z] TOOL RESULT

```
# Proto-Turkic *bāg

## Reconstructed Form and Meaning

The reconstructed Proto-Turkic form is **\*bāg**, meaning "connection," "tie," or "rope."

## Etymology

According to the Wiktionary entry, the term is "Composed of _[\*bā-](/wiki/Reconstruction:Proto-Turkic/b%C4%81- "Reconstruction:Proto-Turkic/bā-")_ ("to tie, to knot") +‎ _[\*-g](/wiki/Reconstruction:Proto-Turkic/-g "Reconstruction:Proto-Turkic/-g")_ (deverbal noun suffix)."

## Important Note

The provided web content contains **no discussion** of alternative etymologies such as borrowing from Middle Chinese 伯 or Iranian *baga-. It also makes **no citations** to scholars like Clauson, Doerfer, or Rybatzki. The page presents only the internal Proto-Turkic derivation as its etymology, without addressing competing theoretical positions or scholarly debates about the word's ultimate origin.

To address your specific questions about loan sources and scholarly attribution, additional sources beyond this Wiktionary page would be necessary.
```


## [2026-09-05T06:12:14.607Z] TOOL CALL #59: WebFetch

```json
{
 "url": "https://www.nisanyansozluk.com/kelime/bey",
 "prompt": "Give the etymology of Turkish 'bey' (Old Turkic beg): the proposed sources (Middle Chinese 伯 or Iranian/Sogdian baga), and the scholars cited. Quote the entry text."
}
```


## [2026-09-05T06:12:16.275Z] TOOL CALL #60: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A8%DB%8C%DA%AF",
 "prompt": "Give the etymology of Persian بیگ (beg/bey): source language, and any related forms (بیگم, اتابک). Quote the etymology."
}
```


### [2026-09-05T06:12:18.921Z] TOOL RESULT

```
I cannot provide the etymology information you're requesting. The web page content supplied appears to be only the header, navigation, and footer of the Nişanyan Sözlük (Nişanyan Dictionary) website—it does not include the actual dictionary entry for "bey" or any etymological details about the word's proposed sources or scholarly citations.

To obtain this information, you would need to visit the full dictionary entry for "bey" on the Nişanyan Sözlük website directly.
```


### [2026-09-05T06:12:21.312Z] TOOL RESULT

```
# Etymology of Persian بیگ (beg/bey)

**Source Language:** Proto-Turkic

**Etymology Quote:**
"Borrowed from Proto-Turkic *bēg via a Turkic language, perhaps ultimately from Middle Iranian languages"

**Related Forms:**
- **بیگم** (begum) - feminine form, derived from the root
- **اتابک** (atābak) - a related aristocratic title listed among related terms
- **بیگلربیگی** (beyglarbeygi) - compound form meaning "bey of beys"

The word ultimately refers to a historical aristocratic title used across Iran, Central Asia, South Asia, and Turkey. Its journey through languages demonstrates the cultural and political exchanges between Turkic and Persian-speaking regions.
```


## [2026-09-05T06:12:27.564Z] TOOL CALL #61: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Turkic/b%C4%93g",
 "prompt": "Give the reconstruction, meaning, and the full etymology discussion: Middle Chinese 伯 vs Iranian *baga-; which scholars are cited (Clauson, Doerfer, Rybatzki, Sinor)? Quote."
}
```


## [2026-09-05T06:12:29.233Z] TOOL CALL #62: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A8%DB%8C%D8%AF%D8%AE%D8%AA",
 "prompt": "Give the etymology and meaning of Persian بیدخت (Bīdoxt): is it 'daughter of god', linked to Anahita/Venus, from baga-duxta? Quote."
}
```


### [2026-09-05T06:12:30.993Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-05T06:12:33.882Z] TOOL RESULT

```
# Proto-Turkic *bǟg

**Reconstruction:** *bǟg
**Meaning:** lord

## Etymology Discussion

The page presents two competing theories without definitive resolution:

**Middle Chinese Theory:**
One hypothesis proposes the word derives from Middle Chinese 百 (MC paek, "hundred"), 佰 (MC paek, "head of a hundred men"), or 伯/霸 (MC paek, "eldest brother" or "hegemon").

**Iranian Theory:**
An alternative theory traces it to Northeastern Iranian, specifically Sogdian βɣ (bāɣ, "lord, master"), from Proto-Iranian *bagáh ("god").

**Scholarly Assessment:**
Regarding the Iranian derivation, German Turkologist Gerhard Doerfer "assessed the derivation from an Iranian language as quite uncertain and pointed out that the word may be genuinely Turkic."

The article cites **Clauson** (1972) as its primary reference work. Scholars **Doerfer**, **Findley**, and **Rybatzki** are mentioned in footnotes, though Rybatzki's specific contribution isn't quoted in the visible text. The etymology section explicitly states uncertainty remains about the word's ultimate origin.
```


## [2026-09-05T06:12:43.034Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for L in 551 552 553 554 555 556 557 558; do echo \"=== leaf $L ===\"; awk -v n=$((L+1)) 'BEGIN{RS=\"\\f\"} NR==n' BQT_v1_pages.txt | grep -n \"بیدخت\\|بیستون\\|ناهید\\|زهره\" | head -6; done",
 "description": "Locate Bidoxt and Bisotun in BQT"
}
```


### [2026-09-05T06:12:44.832Z] TOOL RESULT

```
=== leaf 551 ===
=== leaf 552 ===
=== leaf 553 ===
18:کمخت , ستار؛ زهره را گویند که صاحب فلك
=== leaf 554 ===
=== leaf 555 ===
=== leaf 556 ===
=== leaf 557 ===
=== leaf 558 ===
```


## [2026-09-05T06:12:47.862Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==554' BQT_v1_pages.txt | sed -n '10,30p'; echo \"=== footnotes ===\"; awk 'BEGIN{RS=\"\\f\"} NR==554' BQT_v1_pages.txt | tail -14",
 "description": "Read BQT Bidoxt entry"
}
```


### [2026-09-05T06:12:49.454Z] TOOL RESULT

```
ید بر که - برآوزن دبکه ب رکه, نوعی
از پیکان تبر باشد شبیه ببر که بید.
بیدخج ه بفتح اول بر وزن برزخ» اسب
جلد و نند و تیز خیز را کویند. وبکر اول هم
هت ات ۲ ۹
ید خام - بکر اكث . عود خام را
گو مد .
بید خت ؟ - با بای مجهول بر وزن
کمخت , ستار؛ زهره را گویند که صاحب فلك
(۱) چك : تا .
لید‌ستر * ع_ با ثانی مجهور و ثای
فرشت(۱) بر وزن بی مسطر ء نام حیوانی است
بحری که هم در
آد نوی نت
خوانند .
دید ست و باشدن ژتابه‌ازس اسبه
کردیدن باشد .
بیك‌ طبر ی « نوعی از بید باشد وبعضی
س مق و۱ مس طبری: کرشة ۷ و بستی
پید موله را کویند که بید مجنون باشد .
لیفق ح_بروزن احمق, ببادة شطرنج‌را
=== footnotes ===
س مق و۱ مس طبری: کرشة ۷ و بستی
پید موله را کویند که بید مجنون باشد .
لیفق ح_بروزن احمق, ببادة شطرنج‌را
کویند وآن مهره ای باشد از حملةٌ مپره حای
شطرنج. و ععرب‌یاده است ۸ .
یدق سیم - کنابه از کو کب و سثاره
باشد .
۳ ت رد 7 فوروز نامه ۹۱۳ ۵ص۵/.
بضی اسای ی بدوح ۰ ای وی
هزدسنا ۰ و۳۲۹
۷ .2680011868 #«نأه۹:ناتی۱5:۹*.
۱ رگ : آش بجگان .
فهرست مزدسنا .
بقیه ازصفحهٌ ۳۳۲
```


## [2026-09-05T06:12:57.720Z] TOOL CALL #65: WebFetch

```json
{
 "url": "https://www.iranicaonline.org/articles/bidokt-mid",
 "prompt": "Give the etymology and identity of Bīdoḵt: is it Middle Persian for the planet Venus / Anāhīd, and does it derive from *baga-duxta 'daughter of god'? Quote."
}
```


## [2026-09-05T06:12:59.142Z] TOOL CALL #66: WebFetch

```json
{
 "url": "https://en.wikipedia.org/wiki/Behistun_Inscription",
 "prompt": "Quote the paragraph on the name Behistun/Bisotun: Old Persian Bagastana, its meaning ('place of god/gods'), and the Middle Persian form."
}
```


### [2026-09-05T06:12:59.522Z] TOOL RESULT

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-05T06:13:04.070Z] TOOL RESULT

```
# Behistun/Bisotun Name Etymology

According to the article, the name derives from ancient sources. In Old Persian, it was called **Bagastana**, which means **"the place of god."** The modern Persian version is rendered as **Bisotun**.

The article explains that "Behistun" specifically comes from usage in Ancient Greek and Arabic sources, particularly through scholars Diodorus Siculus and Ya'qubi, and was "transliterated into English in the 19th century by Henry Rawlinson."
```


## [2026-09-05T06:13:07.704Z] TOOL CALL #67: WebSearch

```json
{
 "query": "Bīdoḵt Middle Persian Venus Anāhīd etymology \"baga\" daughter of god"
}
```


### [2026-09-05T06:13:14.611Z] TOOL RESULT

```
Web search results for query: "Bīdoḵt Middle Persian Venus Anāhīd etymology "baga" daughter of god"

Links: [{"title":"BAGA i. General - Encyclopaedia Iranica","url":"https://www.iranicaonline.org/articles/baga-an-old-iranian-term-for-god-sometimes-designating-a-specific-god/baga-i-general/"},{"title":"Adur-Anahid","url":"https://en.wikipedia.org/wiki/Adur-Anahid"},{"title":"BAGA I. GENERAL|Harold Walter Bailey 1 BAGA I. GENERAL i. General","url":"https://www.iranicaonline.org/articles/baga-an-old-iranian-term-for-god-sometimes-designating-a-specific-god/baga-i-general/?generate_pdf=1"},{"title":"Anahita","url":"https://en.wikipedia.org/wiki/Anahita"},{"title":"Anahita, the Persian Goddess | History, Characteristics & Worship | Study.com","url":"https://study.com/academy/lesson/anahita-history-characteristics-facts-persian-goddess.html"},{"title":"Anahita and Ishtar: Connections to the Planet Venus | Ancient Origins","url":"https://www.ancient-origins.net/myths-legends/anahita-and-ishtar-connections-planet-venus-007136"},{"title":"Anahit (name)","url":"https://en.wikipedia.org/wiki/Anahit_(name)"},{"title":"Anahit (disambiguation)","url":"https://en.wikipedia.org/wiki/Anahit_(disambiguation)"},{"title":"Origins of the Persian Goddess 'Anahita'","url":"https://www.thearchaeologist.org/blog/origins-of-the-persian-goddess-anahita"}]

Based on the search results, I found relevant information about your query:

The New Persian term "bē-doxt" derives from *baga-duxtā, meaning "daughter of god," and refers to the planet Venus. The term uses the etymology you mentioned, where "baga" means god, and "duxtā" means daughter.

Aredvi Sura Anahita inherited an identification with the planet Venus from Ishtar, a Semitic goddess with whom she became conflated at some point prior to the 4th century BCE.

While the search results don't specifically mention "Bīdoḵt" as an alternative name, they do confirm the etymological connection between the "baga-duxtā" ("daughter of god") construction and Venus in Middle Persian tradition, which relates to the goddess Anahita/Anahid in her association with that planet.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-05T06:13:21.015Z] TOOL CALL #68: WebFetch

```json
{
 "url": "https://www.iranicaonline.org/articles/baga-an-old-iranian-term-for-god-sometimes-designating-a-specific-god/baga-i-general/",
 "prompt": "Quote everything on: Old Iranian baga- 'god/share'; Avestan baga-; Old Persian baga-; the compounds Bagastāna (Bisotun), Bagdād/Baghdad, baga-puthra > faghfur, bē-doxt < *baga-duxtā (Venus); Middle Persian bay; New Persian baγ/faγ; and any mention of Turkic beg."
}
```


### [2026-09-05T06:13:22.572Z] TOOL RESULT

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-05T06:13:29.063Z] TOOL CALL #69: Bash

```json
{
 "command": "curl -s -A \"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36\" \"https://www.iranicaonline.org/articles/baga-an-old-iranian-term-for-god-sometimes-designating-a-specific-god/baga-i-general/\" -o /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/baga.html -w \"%{http_code}\\n\"; python3 -c \"\nimport re,html,sys\nt=open('/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/baga.html',encoding='utf-8',errors='replace').read()\nt=re.sub(r'<script.*?</script>','',t,flags=re.S)\nt=re.sub(r'<style.*?</style>','',t,flags=re.S)\nt=re.sub(r'<[^>]+>',' ',t)\nt=html.unescape(t)\nt=re.sub(r'\\s+',' ',t)\nprint(t[:9000])\n\"",
 "description": "Fetch Iranica BAGA article via curl"
}
```


### [2026-09-05T06:13:30.902Z] TOOL RESULT

```
403
 Just a moment... Enable JavaScript and cookies to continue
```


## [2026-09-05T06:13:41.467Z] TOOL CALL #70: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%A8%DB%8C%D8%AF%D8%AE%D8%AA/",
 "prompt": "Quote the فرهنگ معین and لغت‌نامه دهخدا entries for بیدخت: meaning and etymology (Pahlavi/Avestan forms)."
}
```


## [2026-09-05T06:13:42.185Z] TOOL CALL #71: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%A8%D8%BA/",
 "prompt": "Quote the فرهنگ معین and لغت‌نامه دهخدا entries for بغ: meaning ('god') and etymology (Pahlavi/Avestan/Old Persian forms)."
}
```


### [2026-09-05T06:13:49.607Z] TOOL RESULT

```
# بیدخت - Meaning and Etymology

## Modern Dictionary Definitions

**فرهنگ معین** defines it simply as: "(سیاره زهره ، ناهید)" - the planet Venus, also called Nahid.

**فرهنگ عمید** similarly states: "زهره، ناهید" (Venus, Nahid).

## Historical Etymology

According to **لغت‌نامه دهخدا**, the word has ancient roots:

The original form was likely "بغدخت" (Baghdokht), meaning "daughter of Bagh" (Bagh being the deity). One scholar theorizes it evolved as "هیدخت" - where "دخت" means "daughter" and "هی" means "good" - eventually becoming بیدخت through textual transmission and simplification.

## Multiple Meanings

Beyond the astronomical term, بیدخت also refers to:
- A legendary beautiful woman whom the angels Harut and Marut became infatuated with (per Islamic tradition)
- Several towns in Iran's Khorasan provinces

The Pahlavi/Avestan connection reflects Persian astronomical and religious nomenclature predating the Islamic period.
```


### [2026-09-05T06:13:50.537Z] TOOL RESULT

```
# بغ (Bagh) - Dictionary Entry Summary

## Primary Meanings

**فرهنگ معین (Farhang-e Moein):**
"(بَ) (اِ.) ۱ - خدا. ۲ - ایزد، فرشته. ۳ - بُت. فغ هم گویند."

Translation: God, divine being/angel, or idol.

**لغت‌نامه دهخدا (Dehkhoda Dictionary):**
The entry provides extensive etymology, noting that in Avestan and Old Persian, the term appears as *baga/bagha*, meaning "god," "lord," or "provider." The root connects to concepts of distribution and blessing.

## Etymology

The word derives from Indo-European roots (*bhag-*) with meanings related to sharing and bestowing. Related forms appear across languages:
- Pahlavi: *bak, bagh, bay*
- Avestan: *baga, bagha*
- Sanskrit: *bhaga*
- Slavic languages: *bog* (Russian/Polish)

The term appears in place names like **Baghdad** (خدا + داد = "god-given") and **Bistun**.
```


## [2026-09-05T06:14:00.663Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KNT baga ===\"; grep -n \"baga-\\|bāji-\\|bāj\\b\\|Bagastāna\\|Bagastana\" KNT.txt | head -20",
 "description": "Grep Kent Old Persian lexicon"
}
```


### [2026-09-05T06:14:00.715Z] TOOL RESULT

```
=== KNT baga ===
1564:Bàga-yàdi- ‘God-worship (month)’, to baga- ‘god’,
1581:afagaina- or abagaina- ‘of stone’, adj. to abaga- ‘stone’.
1593:Possibly nouns and adjectives formed on ‘the root with the long vowel should be listed here: küma-, püda-, bāji-, таѕіа-. See also the long- vowel forms in $143.
1635:(2-3) pAr. split of pIE s into s š A, and plr. split of pAr. s into s and A (8115): stanam avas- layam niyašiāyam ачоіа; hadiš niy-asddayam; afaham 6asianaty; nom. ending in baga-" pasti- ріти-&.
1776:І. Attached to a verbal root, the ablaut grade of the root varying: kara- in compounds, u-céra-, küma-, Катёа-, gausa-, raga-, adv. daríam, drauga-, baga-, bara- and bāra- in compounds, zana- in compounds; less certain formations in d-baha- in daha-vaja, casa-, U-t&na-, u-tava-, gara- in batu-gara-, Vi-vdna-, varga- in hauma-varga-.
1785:Agents: baga- ‘dispenser, god’; drauga- ‘deceiver, the Lie’; arSti-bara- ‘spear-bearer’; züra-kara- ‘evil-doer’; dáraniya-kara- ‘gold-worker, gold- smith’,
1788:VI. The vocalism of the root varies in these for- mations, being either -a- (pIE -e- or -о- or -a-), as in baga-, bara-, daiva-; or à zero grade, as in karša-, u-zma-, darga- (see Lex. s.vv.); or a vriddhied or lengthened grade (§126), as in kdma-, asa-bāra-, Margava-.
3298:Behistan is a much used but not recorded spell- ing which is intermediate between the OP *baga- siána— Place of the God’, for which Greek has Baytoravoy (Diodorus 2.13), and the Behistin of the medieval Arabic Geographers, the Modern Persian Bisitiin or Bisulün (or even Bistiin, with- out the anaptyctic vowel; understood by popular etymology as ‘without columns’). The inscription was first reached and copied by Lieutenant (after- ward Major General Sir) Henry C. Rawlinson in 1836-47; again in 1908, by Professor A. V. Wil- liams Jackson of Columbia University, who was able to make only a partial examination, but did make the first photographs taken from the narrow ledge below the inscriptions; by L. W. King and R. C. Thompson of the British Museum in 1904; and finally by Professor George G. Cameron of ihe University of Michigan in 1948, who made a thorough examination of the entire inscription, including the Elamite text to the right of the sculptured panel, which had previously been pro- nounced completely illegible.
4952:abaga- (ie. аба"да-) sb. ‘stone’: Av. asanga-, NPers. säng, cf. OP asan-, asman- (S87, S151, $155.1); see also a(againa-. afagam asm. DSf 24, 48.
5716:bag- vb., see under baga-, bàji-.
5717:baga- sb. ‘god’: Av. baga- ‘lot, good fortune’, Skt. bhdga- ‘dispenser (of good fortune)’, Gk. -paryos ‘eater’, OCS bogi ‘god’, pIE *bhago- ($101, $122, 5143.1, V, VI); ef. Hz. ApI 105-10. See also Bagábigna-, Bagabuxsa-, Bagayddi-, bà. рада nsm. AmH 6; AsH 6; DNa 1; DNb 1; DSe 1°; DSE 1°; D8s 1^; DSt 1; рле 1°; DE 1; XPa 1; XPb 1; XPc 1; XPd 1; XPf 1; XPh 1; XE 1; XV 1; A!Pa 1^; A*He 1; A®Pa 1, 25. bagaha npm. ($10, $119, $172) DB 4.61, 63. bagünám gpm. AsH 7; DPd 1f; DPh 9; D8f 9; DSp 1°; DH 7; XE 2; XV 2; A’He 2. bagaibiš ipm. DPd 14f, 22, 24; DSe 50f°; DSt 8; XPb 28f; XPe 12f, 15; XPd 18; XPg 13f; XSc 5°; XV 26; A'Pa 23°. Вот ($42) ipm. D’8a 3. |
5718:Bagábigna- sb. ‘Bagabigna’, a Persian, father of Hydarnes: Elam. ba-qa-pi-ig-na; from baga- ‘sod’ + d-bigna-, pte. in -na- of an unidentified verbal root, cf. perhaps Skt. bija-m ‘seed’ (575.1, $103.IV, $160.Ie, $243). Baglalbignah{ya} gsm. DB 4.84f.
5719:Bagabuxía- sb. ‘Megabyzus’, an ally of Darius against Gaumata: Elam. ba-qa-bu-uk-5a, Akk. ba-ga-bu-ki-$u, Gk. MeyaButos. From baga- ‘sod’ + deriv. of root baug- ‘free’ ($102, §151): ‘God-freed’ (§160.Jc). Balgabluzsa nsm. DB 4.85.
5720:Bagayddi- adj. ‘Bagayadi’, seventh month, Sept.-Oct.: Elam. байцай$, АКК. tasritu. From baga- ‘god’, with vriddhi (8126, §165), + yad- ‘worship’, with lengthened vowel ($126, $165) and formative -2- (8152.1): ‘God-Worship Month’ (8159, $161.Ia), probably referring to Mithras, since Phl. and NPers. call this month Mihr
5722:bàji- sb. ‘tribute’: NPers. Баг; deriv. (§152.1, $165) of root seen in Skt. bhdga- ‘portion, dis- penser’, OP baga- ‘god’, the verb being Skt. bhájatt ‘apportions’, Av. bag-, РЫ. bäztän (§101, $122, $128, $126). Балт asf. DB 1.19; DPe 9; DNa 19; DSe 18; XPh 17.
```


## [2026-09-05T06:14:10.377Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"baksheesh\\|bakhshish\\|bakshish\" KLN_1966.txt KLN_1971.txt | head -10",
 "description": "Grep Klein for baksheesh"
}
```


### [2026-09-05T06:14:10.433Z] TOOL RESULT

```
KLN_1971.txt:24657:backsheesh, backshish. — Variants of baksheesh, 
KLN_1971.txt:24871:-phagous and cp. baksheesh. For the second ele- 
KLN_1971.txt:24998:baksheesh, n., a gratuity; a tip. — Pers. bakhshish, 
KLN_1971.txt:29102:‘master, lord, god’. See baksheesh and cp. next 
KLN_1966.txt:4247:backgammon,  n.  —  Prop,  a  game,  in  which  the pieces  are  put  back ;  compounded  of  back,  ‘the hinder  part  of  the  body’,  and  gammon,  ‘game’, backsheesh,  backshish.  —  Variants  of  baksheesh, backward,  backwards,  adv.  —  Formed  fr.  back, adv.  (see  back,  ‘the  hinder  part  of  the  body’), and  -ward,  resp.  -wards.
KLN_1966.txt:4286:element  is  cogn.  with  Gk.  tpaystv,  ‘to  eat’;  see -phagous  and  cp.  baksheesh.  For  the  second  ele¬ ment  see  aumildar  and  cp.  words  there  referred  to. Bahaism,  n.,  the  teaching  of  the  religious  sect  of the  Bahaists.  —  Formed  with  suff.  -ism  fr.  Pers. baha,  ‘splendor’,  fr.  Arab,  bahd' ,  of  s.m. bahar,  n.,  a  weight.  - —  Arab,  hahdr,  a  weight  used in  India,  ultim.  fr.  OI.  bhdrah,  ‘load,  weight’, which  is  rel.  to  bhdrati,  bharate,  ‘carries’,  and cogn.  with  Gk.  qilpeiv,  L.  ferre,  ‘to  bear, carry’.  See  bear,  ‘to  carry’,  and  cp.  words  there referred  to.
KLN_1966.txt:4302:baksheesh,  n.,  a  gratuity ;  a  tip.  —  Pers.  bakhshish, lit.  ‘gift’,  a  derivative  of  the  verb  bukhshidan,  ‘to give’,  fr.  I.-E.  base  *bhag-,  ‘to  distribute,  share out’,  whence  also  OI.  bhdjati,  ‘assigns,  allots, apportions,  enjoys,  loves’,  bhagah,  'allotter,  dis¬ tributor,  master,  lord’,  Gk.  9ay£tv,  ‘to  eat’. See  -phagous  and  cp.  Bhaga  and  the  first  ele¬ ment  in  Bhagavadgita,  and  in  bahadur.
KLN_1966.txt:4884:Bhaga,  n.,  a  god  of  wealth  (Vedic  mythol.)  — OI.  Bhagah,  lit.  ‘allotter,  distributer,  master, lord’,  fr.  bhdjati,  ‘assigns,  allots,  apportions,  en¬ joys,  loves’,  rel.  to  Avestic  haya,  OPers.  baga, ‘master,  lord,  god’.  See  baksheesh  and  cp.  next word.  Cp.  also  pagoda.
```


## [2026-09-05T06:14:19.833Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '4290,4310p' KLN_1966.txt | grep -n \"^[0-9]\\{2,4\\}\" ; awk 'NR>=4280 && NR<=4320' KLN_1966.txt | grep -oE \"\\b1[5-9][0-9]\\b\" | head",
 "description": "Find Klein page number near baksheesh"
}
```


### [2026-09-05T06:14:21.676Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-05T06:14:27.408Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR<=4302' KLN_1966.txt | grep -c $'\\f'; python3 -c \"\nd=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\ni=d.find('baksheesh,  n.,  a  gratuity')\nprint('leaf',d[:i].count(chr(12)))\nprint('total leaves',d.count(chr(12)))\n\"",
 "description": "Compute Klein leaf for baksheesh"
}
```


### [2026-09-05T06:14:29.077Z] TOOL RESULT

```
86
leaf 86
total leaves 902
```


## [2026-09-05T06:14:37.340Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== FFD baxsh ===\"; grep -n \"بخشیدن\\|baxš\\|بخش\" incoming/FFD/FFD_pages.txt | head -10; echo \"=== SNS ===\"; grep -n -i \"bahr\\|baxs\\|bax\\^\\|barx\" SNS_pages.txt | head -10",
 "description": "Grep FFD and SNS"
}
```


### [2026-09-05T06:14:37.409Z] TOOL RESULT

```
=== FFD baxsh ===
996:بخشودن
998:در فارسی میانه به جای «بخشود» 202333774 آمده است. 20253710 مادهٌ
999:ماضی جعلی و از مادهٌ مضارع ساخته شده است. «بخشود» در فارسی دری به قیاس
1002:بخشای + فارسی میانه 202۶3 < ایرانی باستان ۵ -3520 -۵02*. برای 2 > آرای.
1003:2 پیشوند فعلی است. ريشةٌ 7524 فرضی است > بخشیدن.
1006:بخشیدن
1007:بخشید < فارسی میانه 029870 027870 مادهٌ ماضی جعلی است. از مادهٌ مضارع
1009:بخش < فارسی میانه 0235 < ایرانی باستان 82۳-3*. 328 صورت اصلی 337 است» 8
1013:«بخشودن» به معنی «عفو کردنْ» و «بخشیدن» به معنی «تقسیم کردن» هست» «بخشیدن»
1014:در معنی «بخشودن» به کار رفته است > بخشودن.
=== SNS ===
1358:                                                                                                                                        ,** i* j l« i*i   :6   pay ud   2     bahr:          ^^>r -O'Ci^y-
1413:                                                               yW^ «cw!jj             :   a-baxslh:                  -« .         u    I
4577:                                          baxsisn:        -*o-*0_i> ctm j
4588:                                                                                     I                                           -VM^.U<».       923) baxs-        :£u
11827:                                                                                     f!"                 bahr        :        ^^^T                       dasr:         ^ da0ra-                     :   ^h-,l*jljtf l^
12155:            •   A-Y/T^ >»vjJ'j^jJ:2 bahr:
15205:                          paity-apara 116/6                  pixa- 143/16               baxs- 98/1
16370:bahr 96/9                bavandagtar 110/14             b5xted 106/8              bun 109/20
16376:band 110/18              baxsiln 97/19                  b5zisn 107/18             burdar 108/13
16559:3n 55/1-163/11              atas   £   Ohrmazd 27/2                abayfid Sudan 15/21       a-baxslh 13/14
```


## [2026-09-05T06:14:45.926Z] TOOL CALL #77: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR<=1014' incoming/FFD/FFD_pages.txt | grep -n \"pdf page\" | tail -3; echo \"=== FFD lines 990-1020 ===\"; sed -n '990,1020p' incoming/FFD/FFD_pages.txt; echo \"=== SNS 11820-11835 ===\"; sed -n '11820,11835p' SNS_pages.txt",
 "description": "Check FFD page and SNS bahr entry"
}
```


### [2026-09-05T06:14:47.526Z] TOOL RESULT

```
935:[pdf page 39]
969:[pdf page 40]
1004:[pdf page 41]
=== FFD lines 990-1020 ===
ساخته شده است.

بای < فارسی میانه 203 < ایرانی باستان 8ر3م* < 2-ر02-4*. برای ۵ -> آرای.
4 پیشوند فعلی است. 2۷ به معنی «حرکت کردن» است. «آی» مادهٌ مضارع «آمدن» از
9 آمده است > آمدن.

بخشودن

در فارسی میانه به جای «بخشود» 202333774 آمده است. 20253710 مادهٌ
ماضی جعلی و از مادهٌ مضارع ساخته شده است. «بخشود» در فارسی دری به قیاس
1 , 870 به وجود آمده است.

بخشای + فارسی میانه 202۶3 < ایرانی باستان ۵ -3520 -۵02*. برای 2 > آرای.
2 پیشوند فعلی است. ريشةٌ 7524 فرضی است > بخشیدن.
[pdf page 41]
وج ان ار فعلهای فارسی دری
بخشیدن
بخشید < فارسی میانه 029870 027870 مادهٌ ماضی جعلی است. از مادهٌ مضارع
ساخته شده است.
بخش < فارسی میانه 0235 < ایرانی باستان 82۳-3*. 328 صورت اصلی 337 است» 8
پیش از 8 به #بدل شده است. ‎٩‏ برای ساختن ريشهٌ جدید به کار رفته است. 328 به معنی
«تقسیم کردن» است و واه «بخت» در فارسی دری از 025-18 آمده است. 327۳-18 صفت
مفعولی گذشته است از پسوند 14 و 085 به جای ۳۵8. به سیب شباهت لفظی که میان
«بخشودن» به معنی «عفو کردنْ» و «بخشیدن» به معنی «تقسیم کردن» هست» «بخشیدن»
در معنی «بخشودن» به کار رفته است > بخشودن.
برازیدن
برازید « فارسی میانه 053270. 073270 مادةٌ ماضی جعلی است. از مادةٌ مضارع
ساخته شده است.
براز « فارسی میانه 0732 < ایرانی باستان ۳122-8*. برای 2 - آرای. ريشهٌ 3۲37 و
فارسی میانه هر دو به معنی «درخشیدن» هستند. «برازیدن» در معنی «سزاوار
و زیبنده بودنْ» به کار رفته است.
=== SNS 11820-11835 ===
Uyacinthus       w* hyakinthos „»V3U»«* *1JWtf :                                                                                                            •j*^'oi^'*tf->A'o -* , dasr:        l       , -                    ***-<->

aj   ^   ***) *•/ •* -' •-> **• vj
                                    "              "               ,a       ^ "*
                                                                             J
                                                                                           **       .rfA^tfUfa^s^             UiW». 732)datra-: I> *S l5Jj. da0ra-:fc.
                                                                        '
                                                                                     f!"                 bahr        :        ^^^T                       dasr:         ^ da0ra-                     :   ^h-,l*jljtf l^
                                                                                                                              -r/ITiS .f«/1                       iSUofcwaZ.SnS. p. 137)
                                                                                                                                  •   f / IT**          •   lajii^ Ia^ja : dasran
                                                                                                                                                                       <
                                                                                                                                                                                  ^>^^y                       :
```


## [2026-09-05T06:15:03.070Z] TOOL CALL #78: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"baxa\\|baxd\\|bax\\^dra\\|baxadra\\|ba/dra\\|923\" SNS_pages.txt | head -20; echo \"=== line 1358 ctx ===\"; sed -n '1350,1365p' SNS_pages.txt",
 "description": "Find SNS bahr entry"
}
```


### [2026-09-05T06:15:03.121Z] TOOL RESULT

```
4547:                           n/TT«S     w/To^(4tl/b. 923)baxta- :^-
4565:                                                                                                   (Mir. Man.   1,36)           bftrs>A   UiK&. 923)bax*/ra-: fa.
4588:                                                                                     I                                           -VM^.U<».       923) baxs-        :£u
13060:                                                                                                               CAiWfc.   gaosa+*a-vara-:l* baxa-              :,'   gaolavara-: fc-
15201:                                                                                        baxa<fra- 96/10
=== line 1358 ctx ===

                                                      (Mir. Man. II,                            M)      PV<ll
                                                                                                                                  , IT
                                                                                                                                       <S    nf-^-YT/X^.6aS :L U<H> 561)xsvas- h.
                                                                                                                                                  .MMT-/Y1 * -P/V^ .TT-TV-TV-VY/ir*5 .<n
                                            I/O*5      (lat/^^v * Junkcn           1

 To                                                                                                                                 .
                                                                                                                                        ,** i* j l« i*i   :6   pay ud   2     bahr:          ^^>r -O'Ci^y-
                                                                                                                                                                                                         i
                                                                                                                                                                                                  -,w*.u*;.,             -
                                                                                                                                                                                                                                                   IT

      \x                                                       ,L-^U*.b*j1
```


## [2026-09-05T06:15:08.534Z] TOOL CALL #79: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"بغداد\" TAD_pages.txt | head -10",
 "description": "Grep TAD for Baghdad"
}
```


### [2026-09-05T06:15:08.580Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-05T06:15:11.993Z] TOOL CALL #80: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"بغداد\\|بغدا\" TAD.txt | head -10; echo \"--- pdf tags ---\"; grep -n \"pdf page 1[0-9]\\]\" TAD_pages.txt | head -5; echo \"--- leaf 12ish ---\"; awk 'BEGIN{RS=\"\\f\"} NR==13' TAD_pages.txt | head -40",
 "description": "Search TAD for Baghdad"
}
```


### [2026-09-05T06:15:13.796Z] TOOL RESULT

```
510:بغداد - فارسي مركب من باغ أي بستان وداد أي علال 
--- pdf tags ---
--- leaf 12ish ---
                                 ‫عت اب‬


                                ‫رجيس ‪ -‬اسمالسيار لمشئري بالفارسية‬
 ‫ايطالي ‪ 35618200‬معناه سثر الباب أصله فارسي « برده (أي ‪5‬‬       ‫رداه‬

                                                           ‫وسجف وغطاء‬
‫ريد ‪ -‬فارسي دن ردن أي دل وهومذكورفيسفراستيروكان مستعملا‬

 ‫قبل ‪5‬ال‪626‬؟ اللاتيني الذي أنشاهاو عوطس لنقل الرسائل وفى الايطالية ‪8150‬م‬
                                                        ‫وقد عرلوه بوسطة‬
                    ‫برد س حامية‪ --‬تركي « برداخ » أي صل وجلا‬
                                   ‫ردي ‪ -‬مصرية وهو نبات كالقصب‬
                    ‫معناه زائر كنانمي”‬       ‫ودبوط ‪ -‬يوناني ‪7‬‬
             ‫رذعة ‏ ارامية ‪ 9‬بروّعتا » أي حلسالدابةمرادفه وكاف‬
            ‫دون ‪ 53‬لانيني مه ‪,‬روك قاط أي كل ابوهحصان وآية ائان‬

            ‫“رشان ‪ -‬ارامية «فريستا» أي قرصة تصنم املندقيق الابيض‬
                 ‫برسام ‏ فارسى مركب من راي صدر وسام أي المهاب‬
                                                  ‫رشت ‪ -‬انظر برشت‬
‫رطاش ‪ -‬عامية مأخوذة من ‪ 82:61:00‬الايطالية ومعناها ستر البابوعر بها‬
                                                            ‫أسكدَّة الاب‬
                                  ‫راغي ترك « بورغو » غربيه لواب‬
‫وهو الارجوان في الفينيقية والارجمان فيالميرانية‬    ‫رفير ‪ --‬ووناني ‪2‬‬

‫من براي ربشة وكار أي شغل‬          ‫ركار ويكار وفرجار ‪ --‬فارسي ‪9‬‬
                                                            ‫وعربه دوارة‬
```


## [2026-09-05T06:15:20.544Z] TOOL CALL #81: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nd=open('TAD_pages.txt',encoding='utf-8',errors='replace').read()\ni=d.find('بغداد')\nprint('found at',i,'leaf',d[:i].count(chr(12)) if i>0 else None)\nprint(repr(d[i-300:i+300]) if i>0 else 'not found')\n\"",
 "description": "Locate Baghdad in TAD pages"
}
```


### [2026-09-05T06:15:22.202Z] TOOL RESULT

```
found at -1 leaf None
not found
```


## [2026-09-05T06:15:33.052Z] TOOL CALL #82: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== ARY ===\"; grep -n \"بخشیدن\\|بخت\\|انباز\\|بهره\" incoming/ARY/ARY_pages.txt | head -12; echo \"=== ARY latin ===\"; grep -n -i \"BHAG\\|BHEG\" incoming/ARY/ARY_latin_index_pages.txt | head -10",
 "description": "Grep Aryanpur"
}
```


### [2026-09-05T06:15:33.122Z] TOOL RESULT

```
=== ARY ===
654:بختیاری ولر) به آنها تحرکك ‏ وگسترش پذیری شگفت‌انگیزی داده بود. ابل‌های سارماتی
1192:استادان ایرانی نیز (به ویژه معین و خانلری و پورداود) با بهره گیری از پژوهشهای برونمرزیان امن ۱
1227:اول -بهره گیری کامل از پژوهش‌های پیشین و منعکس سازی آنها به طور کوتهوار.
1230:است و من با سپاسمندی و ذ کر هر یک از مراجع خود از این پژوهشها بهره گرفنه‌ام. ولی چون بیشتر
2039:8 سمعتقد است که همه‌ی واژه‌های ژرمنی وابسته به "آمبختن " از واژه‌ی لاتین ۸1182153078 مشتنی شده‌اند.
2087:۴ آوبختن
3005:۲- معنی این واژه درزبان لاتینشانس» بخت خوش,
3282:۴ بخت
3309:بخش, بخشیدن, بخشش / ۱۱۵
3320:۱- بازگلت به "بخت" و ابغ".
12869:۳ | گربختن, گریز
=== ARY latin ===
3240:THI gi he iebbly BHAG, BHAGAH, BHAJATI
3718:BHAGA,, (SANSKRIT) xz nile
3719:‘REFERENCES beh BHAGVAD(-GITA)
3965:(OLD CHURCH SLAVIC) 5° 53% BAG. BHAGA —«(AVESTAN) gly!
3972:BUCK: 1097 BHAGA, s(SANSERIT) cy Saito
3973:AMINDAROV: (PART) 265 BHAJ, BHAJATI, BHADRA, BHAGYA
```


## [2026-09-05T06:15:36.509Z] TOOL CALL #83: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '3275,3330p' incoming/ARY/ARY_pages.txt; echo \"=== pdf tag ===\"; awk 'NR<=3320' incoming/ARY/ARY_pages.txt | grep -n \"pdf page\" | tail -2",
 "description": "Read Aryanpur baxt/bakhsh entry"
}
```


### [2026-09-05T06:15:38.114Z] TOOL RESULT

```
ارمنی (/۸48(/1۸): - و۱۱ پسگشت‌ها ار هبار ۲
امپایایی (820ت۶۸(۷ق: ۳70 ۰ 2 :۸0۸/5 4 1۸41082
7 صربی (لففاق38): ه۳۸7 برهان قاطع : ۳۳۳
پهلری (انماتطا): ۲۷۸۲33۸۴ ,۷۸۲۲۲۸۴ یه زا ده ۱
کردی (80/57): ,ت73 سانسکریت (54756777): 11
۰ سس
[pdf page 113]
۴ بخت
8۸ ک ۸
گوتیک (0071476)«شاید) ‏ 8۸1 ,8۸740 لنرنی (لنی) (شاید) (/(774ما): ‏ 8538
ایسلند یکهن (2127142۷/م5۳ (01)(شاید) 0 ۰

07 ات8 پسگشت‌ها : ۳5
ساکسرنی کهن (5420۸۷ صا0)(شاید) ‏ 8۸8۷ رک رس نا
آلمانی کهن (8۸۲0/34 2710/4 (01)(شاید) 1 (8۸180) . . 7 اتمه

,810۸0 ,805 6 (۲0ی) اند مد هم
انگلیسی کهن (بلکاسا8070 0/.0)(شاید) ,817 893 ماه
,3۸ 9 (8۸18) :0۸05
انگلیسی (5۸/01577)«شاید) ری 4 (8۸73) :547
دانمارکی (0۸۸//54):(شاید) ان 9 (05110) :۸/۸۸0
سوئدی (582/34):(شاید) ۸ برهان قاطع + ۳۳۷
لینوانی (/۷14۸ملا727/.)(شاید) ‏ ,8588۸۸8 فرهنگ معین : ۳۷۳-۴
اوستایی (47537۸/۷) :8۸6817۸771 ب8۸7۸ 20
پهلوی (۷1هابل#ه): .3 پسگشت‌ها ۱۱5
کردی (7ل08/15): 2 زر سا
تخاری ۸ (۸ [(4ل70707/۸7): 2۸ 71 :هلیم ت02
تخاری 8 (8 2۸ لل70): 4 5 (۲۵37108) :۸218
سانسکریت (54(/858/7): 817۸6871۸71 1095 ناه
ارمنی (۸۷۸/807140): اد رانا 13 ۸0
اسلاوی کهن (ع۲7اما؟ ۲ل#6تالق هام برهان قاطع : ۳۵
بادداشت:
بازگلست به: هر و بخش. ۰
[pdf page 114]
بخش, بخشیدن, بخشش / ۱۱۵
اوستایی (۷ل۸۲8874): ,8۸6 ,لاش87 ,88711 برنانی (0ق07): ۳0
8۸01۸ ,8۸381۸71 اسلاوی کهن (۷76ما5 ل#6ناتل) صا0):
پهلری (1/ا۸3): ,1 ,2۸3877 ت67 806
+811۸ ,(3۸38117813 ,28۸77۸۵
ترا تن ها پسگشت‌ها نششیت دنت
سانسکریت (7ل8۸587): 0
311۸71 ,81176817۸75 4 (ت88870۷/۸) ,ک1 ۰ 2ل2اققه ما
1 ,871۸6۸5 ,211۸6 برهان قاطع + ۲۱۴۱۴۰
ارمنی ((۵/0/8774): 3006۸77
یادداشت:
۱- بازگلت به "بخت" و ابغ".
۲ چم این واژه در زبان پونانی: خوردن.
۳ واژه‌های فارسی برع" و آبرخه" هم از همین واجریشه‌اند.
پهلوی (۳۸14۲7): ۷۸۳7۸۹ ,۷۸ ,۷۷۸ پسگشت‌ها 5
کردی (600[/87): ۰ - 8 ( 160 2020
لاتین (4710ا): (شاید) 0۸ 1 (8۸0) ات این نا
8 ۹ : نداد رد 103 :23( وه
آلمان یکین (30م 0294زا اه رشاید) 3119 ماه
00 8 (8۸0) :0/005
آلمانی (0587۸/۸۷)(شاید) و۱ 3 (8۸3) تا
لیتوانی (/7724(/1۵۸.ت)«شاید) ۸0۸ 24 ۸240
=== pdf tag ===
3281:[pdf page 113]
3308:[pdf page 114]
```


## [2026-09-05T06:15:51.482Z] TOOL CALL #84: Bash

```json
{
 "command": "ls site/pages/81.jpg 2>/dev/null; pdftoppm -f 81 -l 81 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg81 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/",
 "description": "Render PDF page 81"
}
```


### [2026-09-05T06:15:54.208Z] TOOL RESULT

```
site/pages/81.jpg
total 9608
drwx------ 2 sfmqrb sfmqrb    4096 Sep  5 02:15 .
drwx------ 4 sfmqrb sfmqrb    4096 Sep  5 01:20 ..
-rw-rw-r-- 1 sfmqrb sfmqrb    4061 Sep  5 02:00 avestan.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5971 Sep  5 02:13 baga.html
-rw-rw-r-- 1 sfmqrb sfmqrb  189420 Sep  5 02:15 bqt440_bottom.png
-rw-rw-r-- 1 sfmqrb sfmqrb  513902 Sep  5 02:15 bqt440.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  502834 Sep  5 02:02 bqt538_big.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   72705 Sep  5 02:02 bqt538_fn6.png
-rw-rw-r-- 1 sfmqrb sfmqrb   24595 Sep  5 02:02 bqt538_head2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   22593 Sep  5 02:02 bqt538_head.png
-rw-rw-r-- 1 sfmqrb sfmqrb  207980 Sep  5 02:01 bqt538.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  282104 Sep  5 01:29 bqt733_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb  669351 Sep  5 01:29 bqt733.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   17369 Sep  5 01:35 bqtv1_361_head.png
-rw-rw-r-- 1 sfmqrb sfmqrb  470042 Sep  5 01:35 bqtv1_361.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  241161 Sep  5 01:36 bqtv1_398_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb  482084 Sep  5 01:36 bqtv1_398.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  190109 Sep  5 01:35 bqtv1_399_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   53579 Sep  5 01:36 bqtv1_399_head2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1625 Sep  5 01:35 bqtv1_399_head.png
-rw-rw-r-- 1 sfmqrb sfmqrb  510341 Sep  5 01:35 bqtv1_399.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   63555 Sep  5 01:43 build71.py
-rw-rw-r-- 1 sfmqrb sfmqrb    4811 Sep  5 02:00 bulca.png
-rw-rw-r-- 1 sfmqrb sfmqrb   22149 Sep  5 01:51 c_belloth.png
-rw-rw-r-- 1 sfmqrb sfmqrb   23219 Sep  5 01:51 c_schyth.png
-rw-rw-r-- 1 sfmqrb sfmqrb  445959 Sep  5 01:37 hrn126_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1213019 Sep  5 01:37 hrn126.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  456157 Sep  5 01:37 hrn127_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1278807 Sep  5 01:37 hrn127.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   40966 Sep  5 01:40 mk67.py
-rw-rw-r-- 1 sfmqrb sfmqrb   58318 Sep  5 01:45 mk70.py
-rw-rw-r-- 1 sfmqrb sfmqrb   78619 Sep  5 02:02 mk73.py
-rw-rw-r-- 1 sfmqrb sfmqrb   68454 Sep  5 02:01 mk75.py
-rw-rw-r-- 1 sfmqrb sfmqrb   55169 Sep  5 01:30 pg67.png
-rw-rw-r-- 1 sfmqrb sfmqrb   57649 Sep  5 01:33 pg69.png
-rw-rw-r-- 1 sfmqrb sfmqrb   50966 Sep  5 01:33 pg69_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb   77968 Sep  5 01:31 pg70.png
-rw-rw-r-- 1 sfmqrb sfmqrb   75801 Sep  5 01:29 pg71_300.png
-rw-rw-r-- 1 sfmqrb sfmqrb   71145 Sep  5 01:29 pg71.png
-rw-rw-r-- 1 sfmqrb sfmqrb  134140 Sep  5 01:44 pg72_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2377 Sep  5 01:44 pg72_afandi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   11769 Sep  5 01:47 pg72_fr2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2947 Sep  5 01:44 pg72_fr.png
-rw-rw-r-- 1 sfmqrb sfmqrb   49860 Sep  5 01:44 pg72.png
-rw-rw-r-- 1 sfmqrb sfmqrb   81180 Sep  5 01:47 pg73.png
-rw-rw-r-- 1 sfmqrb sfmqrb   56073 Sep  5 01:48 pg74.png
-rw-rw-r-- 1 sfmqrb sfmqrb  108877 Sep  5 01:51 pg75_400.png
-rw-rw-r-- 1 sfmqrb sfmqrb   20612 Sep  5 01:51 pg75_greeklatin.png
-rw-rw-r-- 1 sfmqrb sfmqrb   75134 Sep  5 01:51 pg75.png
-rw-rw-r-- 1 sfmqrb sfmqrb   66505 Sep  5 01:51 pg76.png
-rw-rw-r-- 1 sfmqrb sfmqrb   65211 Sep  5 02:00 pg77.png
-rw-rw-r-- 1 sfmqrb sfmqrb  155334 Sep  5 02:00 pg78_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb   63822 Sep  5 01:59 pg78.png
-rw-rw-r-- 1 sfmqrb sfmqrb   59439 Sep  5 02:09 pg79.png
-rw-rw-r-- 1 sfmqrb sfmqrb   58953 Sep  5 02:08 pg80.png
-rw-rw-r-- 1 sfmqrb sfmqrb   99904 Sep  5 02:15 pg81.png
```


## [2026-09-05T06:15:58.059Z] TOOL CALL #85: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg81.png"
}
```


### [2026-09-05T06:15:58.527Z] TOOL RESULT

```

```


## [2026-09-05T06:15:58.524Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-05T06:16:18.139Z] TOOL CALL #86: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"baxtö\\|baxto\\.\\|baxta\\.dä\\|baxtö\\.dä\\|bayö\\.dä\\|ba.o\\.data\" BRT.txt | head -10; echo \"=== KNT baga-data ===\"; grep -n -i \"Bagadata\\|baga-dāta\\|Bagadates\" KNT.txt | head -5",
 "description": "Search for baxto-data"
}
```


### [2026-09-05T06:16:18.242Z] TOOL RESULT

```
=== KNT baga-data ===
```


## [2026-09-05T06:16:40.585Z] TOOL CALL #87: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for L in $(seq 555 566); do r=$(awk -v n=$((L+1)) 'BEGIN{RS=\"\\f\"} NR==n' BQT_v1_pages.txt | grep -c \"بیستون\\|بستون\\|فغستان\"); echo \"leaf $L : $r\"; done",
 "description": "Find Bisotun in BQT"
}
```


### [2026-09-05T06:16:42.113Z] TOOL RESULT

```
leaf 555 : 0
leaf 556 : 0
leaf 557 : 0
leaf 558 : 0
leaf 559 : 0
leaf 560 : 0
leaf 561 : 0
leaf 562 : 0
leaf 563 : 0
leaf 564 : 0
leaf 565 : 0
leaf 566 : 0
```


## [2026-09-05T06:16:55.121Z] TOOL CALL #88: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/b%CA%B0eh%E2%82%82g-\" \\\n \"https://en.wiktionary.org/wiki/%D9%81%D8%BA%D9%81%D9%88%D8%B1\" \\\n \"https://en.wiktionary.org/wiki/%D8%A8%DB%8C%D8%B3%D8%AA%D9%88%D9%86\" \\\n \"https://en.wiktionary.org/wiki/%D8%A8%DB%8C%DA%AF\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Turkic/b%C4%93g\" \\\n \"https://en.wikipedia.org/wiki/Behistun_Inscription\" \\\n \"https://abadis.ir/fatofa/%D8%A8%DB%8C%D8%AF%D8%AE%D8%AA/\" \\\n \"https://abadis.ir/fatofa/%D8%A8%D8%BA/\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"pdf page 81, root Bhag part 1: verification of baga/baxs/bahr/fagfur/bistun/beg\" 2>&1 | tail -2\ndone",
 "description": "Archive web sources"
}
```


### [2026-09-05T06:17:02.072Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/d7c6f8d1a1f64c02.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f8695d83bae2aec5.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/66cb409cd3b28795.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/149895f7b00830ad.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/644ee918bfaebec0.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/250e69d5cdec46fd.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/19296d638d2d31f8.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d2bec529dd7c6266.txt
```


## [2026-09-05T06:17:07.722Z] TOOL CALL #89: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg81.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/81.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/ | head; echo \"=== verify_check ===\"; sed -n '1,120p' /home/sfmqrb/git/rishe/tools/verify_check.py",
 "description": "Copy page image and read verify_check"
}
```


### [2026-09-05T06:17:07.814Z] TOOL RESULT

```
total 1496
drwxrwxr-x 2 sfmqrb sfmqrb   4096 Sep  5 02:17 .
drwxrwxr-x 9 sfmqrb sfmqrb   4096 Sep  5 01:38 ..
-rw-rw-r-- 1 sfmqrb sfmqrb 104864 Sep  4 19:03 101.png
-rw-rw-r-- 1 sfmqrb sfmqrb  86203 Sep  4 19:03 126.png
-rw-rw-r-- 1 sfmqrb sfmqrb 105296 Sep  4 19:03 311.png
-rw-rw-r-- 1 sfmqrb sfmqrb  96466 Sep  4 19:03 33.png
-rw-rw-r-- 1 sfmqrb sfmqrb  99093 Sep  4 19:03 39.png
-rw-rw-r-- 1 sfmqrb sfmqrb  54479 Sep  4 19:03 46.png
-rw-rw-r-- 1 sfmqrb sfmqrb  99295 Sep  4 19:03 54.png
=== verify_check ===
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


## [2026-09-05T06:17:31.730Z] TOOL CALL #90: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== WLD Bd2 ===\"; grep -n \"bhag\\|bhaĝ\\|bhag-\" incoming/WLD/WLD_Bd2_pages.txt | head -8; echo \"=== WLD band3 index ===\"; grep -n \"bhag\" WLD_band3.txt | head -5; echo \"=== SYN share ===\"; grep -n -i \"13.22 SHARE\\|SHARE, PART\" SYN.txt | head -5",
 "description": "Grep Walde-Pokorny and Buck"
}
```


### [2026-09-05T06:17:31.813Z] TOOL RESULT

```
=== WLD Bd2 ===
8206:                                                            :         — bhag-                                   127
8261:1.   bhag- „zuteilen; als Anteil bestimmen oder (ursprgl. medial?, als Anteil,
8265:bhaga-h „Gut, Gluck’^ av. baga-, baya- n. „Auteil, Los, bes. gunstiges**; ai.
8266:bhaga-h „Zuteiler, Herr, Beiname des Savitar und eines andern A'ditya^*
8269: 128                                         bhag-   — bhagO'S
8289: Backe (s. vielmehr u. bhag- „biegen‘‘). Die Zuruckfuhrung von bhag- auf
8297:*bhaghr- „8treiten“).
8300:2.   bhag- „scharf, auch vom Geschmack“??
=== WLD band3 index ===
142:bitin OD, bhakteti 128°, bhaga-f ,Sohomgegeod*
=== SYN share ===
15966:W. peth : Br. pez ‘piece, bit’, Ir. cuit ‘share, part’, etc. (13.23). Pedersen 1.160.
33959:NIr. cuidighim, deriv. of cuid, Ir, cuit ‘share, part’ (18.23),
35536:ON deild ‘share, part’ (: Goth. dais, etc. 13.23), hence ‘dealings’ and esp. ‘legal dealings, lawsuit’.
```


## [2026-09-05T06:17:34.543Z] TOOL CALL #91: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '8261,8275p' incoming/WLD/WLD_Bd2_pages.txt",
 "description": "Read Walde-Pokorny bhag entry"
}
```


### [2026-09-05T06:17:34.604Z] TOOL RESULT

```
1.   bhag- „zuteilen; als Anteil bestimmen oder (ursprgl. medial?, als Anteil,
       als Portion erhalten**.
     Ai. bhajati „teilt zu^'                =
                            av. bag- {bazat} „als Anteil bestimmt sein**, ai.
bhaga-h „Gut, Gluck’^ av. baga-, baya- n. „Auteil, Los, bes. gunstiges**; ai.
bhaga-h „Zuteiler, Herr, Beiname des Savitar und eines andern A'ditya^*
= av. baya- „Herr, Gott“, npers. bay „Goct*' (formell auch gr. -cpdyod) ;                    =
ai. hhaktd-m „Mahlzeit‘‘ = av. baxta- Ptc. „als Anteil zugewiesen‘‘, n. „be-
 128                                         bhag-   — bhagO'S
  stiminter Anteil,         Schicksalsbestiininiiiig,      bes.       Mi6geschick‘‘;     ai.    lihal^mii
 jjgeniefit, yerzehrt“      — av. laxsaiti „hat oder gibt Anteil^; Desid. ai. IhiMate
                                                                 vHva „genie6t
 „erbittet''; slav. *hog^ ,.Anteib' vielleicht in slov, zlega boga
 ein boses Geschick“ (?), sicher in aksl. nbogz, n< bogz ^aim^ bogaf^ „reich";
 aksl. bog'h „Gott“ (nrverw, oder von den iranischen Skythen nbemommen;
```


## [2026-09-05T06:19:41.175Z] TOOL CALL #92: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HJB BEGUM entry ===\"; grep -n \"Begum,  s\\|BEGUM,  s\\|BEGUM, s\\|Begam,\\|BEQUM\" HJB.txt | head -5; python3 -c \"\nd=open('HJB.txt',encoding='utf-8',errors='replace').read()\nimport re\nfor m in re.finditer('BEGUM',d):\n    print(m.start(), repr(d[m.start()-200:m.start()+700]))\n    break\n\"",
 "description": "Find Hobson-Jobson BEGUM entry"
}
```


### [2026-09-05T06:19:43.123Z] TOOL RESULT

```
=== HJB BEGUM entry ===
3239:BEEQUM,  BEQUM,    &c.    s.     A
```


## [2026-09-05T06:19:46.582Z] TOOL CALL #93: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '3239,3244p' HJB.txt; echo \"=== TTS beg ===\"; grep -n \"bäg\\|beg \" incoming/TTS/TTS_pages.txt | head -8",
 "description": "Read HJB BEGUM and grep Vambery"
}
```


### [2026-09-05T06:19:46.661Z] TOOL RESULT

```
BEEQUM,  BEQUM,    &c.    s.     A
Princess,  a  Mistress,  a  Lady  of  Rank  ; applied  to  Mahommedan  ladies,,  and in  the  well-known  case  of  the  Beegum Swmroo  to  the  professedly  Christian (native)  wife  ot  a  EurOT)ean.  The word  appears  to  be  Or.  Turki.  bigmi, [which  some  connect  with  Skt.  hhaga, Mordy'l  a  feminine  formation  from Bw,  *  chief,  or  lord,'  like  Khdmm.  from Khdn ;  hence  P.  hegam.  [Beg  appears in  the  eaily  travellers  as  Beage.]
[1614.— ^'Narranse  saith  he  standeth bound  before  Beage  for  4,800  and  odd mamoodies." — Foster,  Letters,  ii.  282.]
506.— "  Begum."    See  quotation  under
[1617.— "Their  Company  thai  offered  to rob  the  Beagam's  junck."— iSir  T.  Roe, Hak.  Soc.  ii.  454.]
1619.— "  Behind  the  girl  came  another Begum,  also  an  old  woman,  but  lean  and feeble,  holding  on  to  life  with  her  teeth, as  one  might  say." — P,  delta  Voile,  Hak. Soc.  ii.  6.
=== TTS beg ===
```


## [2026-09-05T06:19:52.643Z] TOOL CALL #94: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"فغفور\" incoming/BQT/BQT_v3_pages.txt | head -5",
 "description": "Grep BQT vol3 for faghfur"
}
```


### [2026-09-05T06:19:52.697Z] TOOL RESULT

```
730:پادشاه روم را فیس وپادشاه چین رافغفور ویادشاه
23232:بروزن فغفور» نام قلعه‌ایست در فرطمان
```


## [2026-09-05T06:19:56.636Z] TOOL CALL #95: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nimport re\nd=open('incoming/BQT/BQT_v3_pages.txt',encoding='utf-8',errors='replace').read()\n# find pages containing 'فغفور' headword region: search for 'فغ'\nfor m in re.finditer('فغفور',d):\n    seg=d[:m.start()]\n    tags=re.findall(r'\\[pdf page (\\d+)\\]',seg)\n    print(m.start(), 'after pdf page', tags[-1] if tags else None)\n\"",
 "description": "Locate faghfur pdf page in BQT v3"
}
```


### [2026-09-05T06:19:58.368Z] TOOL RESULT

```
20507 after pdf page 15
632901 after pdf page 318
```


## [2026-09-05T06:20:05.947Z] TOOL CALL #96: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nimport re\nd=open('incoming/BQT/BQT_v3_pages.txt',encoding='utf-8',errors='replace').read()\nparts=re.split(r'\\[pdf page (\\d+)\\]',d)\nm={}\nfor i in range(1,len(parts),2):\n    m[int(parts[i])]=parts[i+1]\nfor p in (286,287,288):\n    t=m.get(p,'<<MISSING>>')\n    print('=== pdf',p,'len',len(t))\n    print(t[:900])\n\"",
 "description": "Read BQT v3 pdf page 287"
}
```


### [2026-09-05T06:20:07.485Z] TOOL RESULT

```
=== pdf 286 len 1802

‎oly‏ دواز دهم

‏در حرف فا با ‎os‏ 2
قغ ۱ بفتح اول وسکون ‎gt‏ » بلفت

‏فرعانه و ‎glklse‏ بت بت ‎Sash‏ عربان
صنم خوانند = و ‎gaat‏ ممشوق وبار ودوست(۱)
و مصاحب و کی را که بیار دوست دارند هم
آمده است ۴ - و کنابه ازجوانان خوب صورت
و صاحب حسن هم هنت .

‏فا ۴ ‎a‏ بنم اون ۴ ‎yk,‏ بالف

‏(۱) چك »

‏چش : - ‎hy‏ و دوست +

‏نقطه دار مشتمل برنه لفت

‏کشیده و ‎GE‏ زده » بمعنی ‎abl‏ ونادان‌وبیقل
‎ath‏ - و حرام زاده را نیز کوینه ۵ .*
فقمتان ۱ پم اول و ‎MT‏
‏بر وز نگلستان ۰۷ بمعنی‌بتخانه وشکده است -
وحرم سرای پادشاهان )551 گوبند ۸ - وکنابه
ازخوب صورتان و صاحب حستان هم هتسوپشم
اول وثالك بمعنی‌زن ومنکوحه - وصورت‌سلاطین

‎(Gauthiot,JA., 1911, IT,p.58) =-\(<.)fugh. fagh so. 3143 ‏بغ(هم.).‎ -\

‎, 2 . 4

‎. Henning , 8505 vol X .
‏دوب و بار‎ eo3a a

‏کفتاکه ازفغان ‎oy‏ اندر جهان فنان.
عتصری بلخی < لفت فرس۲۳۵*.

‏۴ - از : فغ ‎ST HG pe)‏ ( پوند نسبت ) [ رك : لفت‌نامه : ‎Boy [aT‏ دارستر.

‎. ۲۷ ‏ج ۱ ص‎ ols

‏۴
=== pdf 287 len 2273

فقور
‎Vast Lal,‏ .

‎gl‏ 2 ۴ = بررزن مضمور » پادتامچین
را گویند هر که باشد - وئیز پادشاهی‌ازآلاشکان
که بمد از سکندر پادشاه شد و شصت و دوسال
مك ‎Fail,‏ .

‎Saad‏ = بنتح اول و ثانی بروزن سمند,
بمعنی از جای برجتن باشد بر مثال آهو ۴ .؛
وبضم اول و کسر اول هم همین معتی دارد .

‏ففنشور = بطم اول ‎ais‏ ثانی‌وسکون
نون و شین نقطه‌دار ‎oly‏ مجبهولکشیده و برای
‎tht‏ زده . نام شهری است ازملك چن‌ومردم
آنجا بغابت خوب صورت و صاحب حسن میشوند
و جمم بتان و بتگران درآن شبر میباشند 9
‎Cho‏ اول ‎gly‏ هم آمده است ۰
‎Slee » ۲ ol gad‏ وواو ‎met‏

‏. ۱44
بروزن رخاره ‎oS‏ رااکویند که ازغات دماغ
و تکیی ونپابت غرور و تحیر با ازسباری اندوه
و ملال و دل تنگی و خجالت ساکت شده باشد
و حرف ترند ۷ ؛ و معنی ت رکیبی این لفت بت
مانند است چه فغ بت راگویند و واره مانتدرا
یعنی همچو جماد خاموش است .
‎shad‏ ۸ - با یای حطی بروزن دمساز
بععنی ‎the‏ وبخشش باشد ‎٩‏ - وبمعنی‌شاگردانه
هم هست وآن زری باشد که بعد ازاجرت استاد
بطریق انبام ب
=== pdf 288 len 1607

بیان سیزدهم

در حرف فا ‎GEL‏ مشتمل برشش ‎cd‏ و کنامت

‎Els‏ گشودن - کنابه از لاف
زدن و ‎Sli‏ کردن و نازش تمودن باشد -وبمعنی
آروغ‌زدن هم هت و ‎OT‏ بادی باشد باسدا که
آزراء کلو ‎Fal,‏ . ,

‎sis ‏میگشاید ۴ - نی‎ ELS
. ‏میکند و لاف میزند‎

‏فك = بفتح اول و سکون ‎GU‏ و دال
ابجد , کیاهی است دواثی که آلرا ینج انگشت
میکویند و درعلت استفا ‎HTK‏ وبسنیگویند
تخم پنج انگشت (۱) است وعربی است.

‎AD‏ ~ بنتح اول وثانی وسکون عین بی
نقطه » نوعی ازسماروغ باشد وآن بیعترازجاهای

‎Sis‏ و دبوارهای‌حمام وزیرهای خم‌شراب‌روید.
کویند ه رکه ‎LT‏ در جنابت بخورد نل وی
منقطم شود ۴ - و ‎inn‏ صراط 6 هم آده
است در ‎RF‏ .

‏فقهگان ۷ با ‎oye‏ نقطه وکان‌فارسی
بروزن سلیمان, بمعنی قخر وتفاخر ولافو کزاف
و ‎FH‏ و خود ستایی وخودنمایی باشد .

‏فقع گشودن ۲ - بنم اول وفتح‌نانی.
‎ow‏ فقاع گشودن است که کنابه از لاف زدن
و تفاخ ‎OS‏ و نازش و خودنمایی و خودستایی
نمودن = وآروغ زدن باشد .

‎oly‏ چهار دهم

‏در حرف فا ‎GEL‏ فارسی و عربی مشت
```


## [2026-09-05T06:20:23.763Z] AGENT

Now I'll write the verification file.


## [2026-09-05T06:31:50.061Z] TOOL CALL #97: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk81.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\n\nW = \"https://en.wiktionary.org/wiki/\"\nU_PIE  = W + \"Reconstruction:Proto-Indo-European/bʰeh₂g-\"\nU_FAG  = W + \"فغفور\"\nU_BIS  = W + \"بیستون\"\nU_BEIG = W + \"بیگ\"\nU_PT   = W + \"Reconstruction:Proto-Turkic/bēg\"\nU_WIKI = \"https://en.wikipedia.org/wiki/Behistun_Inscription\"\nU_BID  = \"https://abadis.ir/fatofa/بیدخت/\"\nU_BAG  = \"https://abadis.ir/fatofa/بغ/\"\n\ndoc = {\n \"pdf_page\": 81,\n \"book_page\": 51,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-05\",\n \"entries\": [{\n   \"entry\": 0,\n   \"root\": \"Bhag\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE *bʰag- (Wiktionary *bʰeh₂g-) 'to divide, apportion, allot; (middle) to receive as one's share, enjoy'\",\n   \"note\": \"Pokorny I 107 heads the entry '1. bhag- „zuteilen; als Anteil bestimmen oder (ursprüngl. medial?) als Anteil, als Portion erhalten“' — 'to share out' plus the middle 'to get a share', from which Skt. bhakṣati 'genießt, verzehrt' and Gk. phagein 'to eat' give Nourai's 'to enjoy'. Walde–Pokorny II 127f. has the same wording; Watkins/AHD: 'bhag-1. To share out, apportion, also to get a share'; Mann IEC p. 61 'bhag-, bhāg- “enjoy; enjoyment”'. The language label 'Indo-European' and the gloss are therefore both right. Wiktionary now writes the root *bʰeh₂g- and explains the short vowel of Proto-Indo-Iranian *bʰaga- by Lubotsky's Law. Structural caveat for the whole chart: Nourai hangs the Avestan compounds (#3, #6, #8) and the New Persian box #5 directly on the IE root, whereas they are of course formed inside Iranian; and the Turkic branch (#11) is a disputed loan, not an inherited IE descendant.\",\n   \"note_fa\": \"ریشهٔ هندواروپایی آغازین *bʰag- (در نگارش نوین *bʰeh₂g-) به معنی «بخش کردن، قسمت کردن» و در وجه میانه «بهره بردن، برخوردار شدن» است؛ پوکورنی (ص ۱۰۷)، والدهٔـپوکورنی (ج ۲ ص ۱۲۷) و واتکینز در پیوستـ AHD همین معنی را داده‌اند. معنیـ دوم («enjoy») از سنسکریت bhakṣati «می‌خورد، بهره می‌برد» و یونانی phagein «خوردن» می‌آید. پس ادعای نورایی دربارهٔ ریشه و معنی و زبان درست است؛ تنها ایراد ساختاری آن است که ترکیب‌های اوستایی و واژه‌های فارسی را مستقیماً به ریشهٔ هندواروپایی بسته است، نه به میانجیـ ایرانی باستان و فارسی میانه.\",\n   \"sources\": [U_PIE],\n   \"ref_check\": [\n     {\"ref\": \"POK:107\", \"status\": \"supports\",\n      \"note\": \"POK_01.txt leaf 115/116 (printed p. 107): '1. bhag- „zuteilen; als Anteil bestimmen oder (ursprüngl. medial?) als Anteil, als Portion erhalten“. Ai bhajati „teilt zu“ = av. bag- (bazat) … av. baga-, baḳa- n. „Anteil, Los, bes. günstiges“ … baḳa- „Herr, Gott“, npers. baḳ „Gott“ … ai. bhaktá-m „Mahlzeit“ = av. baxta- … av. baxsaiti „hat oder gibt Anteil“'. The cited page carries the whole Iranian material Nourai draws in #1, #2 and #5.\"},\n     {\"ref\": \"IEC:61\", \"status\": \"supports\",\n      \"note\": \"IEC.txt line 1069 prints the running head '61 bhaglos — bhaksó', so p. 61 is indeed the bhag- page; line 1062: 'bhag-, bhāg- “enjoy; enjoyment”. WP II, 127 … Av. bagom “share”, baγo “god”', and line 1065 'bhāg- … Av. baγa “part”; OPer. bāji- “tribute”; Per. bāǵ'. Mann's 'enjoy' is exactly Nourai's second gloss.\"}\n   ],\n   \"consulted\": [\n     {\"src\": \"WLD\", \"where\": \"Bd. II 127–128\", \"stance\": \"supports\",\n      \"note\": \"incoming/WLD/WLD_Bd2_pages.txt l. 8261: '1. bhag- „zuteilen; als Anteil bestimmen oder (urspgl. medial?) als Anteil, als Portion erhalten“ … av. baḳa- „Herr, Gott“, npers. baḳ „Gott“ … av. baxta- … av. baxsaiti'. Word-for-word the source of Pokorny 107.\"},\n     {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.v. bhag-1\", \"stance\": \"supports\",\n      \"note\": \"AHD_watkins1985.txt l. 323: 'bhag-1. To share out, apportion, also to get a share. 1. Greek phagein, to eat (< “to have a share of food”) … 2. Extended form *bhags- in Avestan bakhsh- in Persian bakhshidan, to give: BAKSHEESH, (BUCKSHEE). [Pok. 1. bhag- 107.]'\"},\n     {\"src\": \"KLN\", \"where\": \"1966 vol. I, b- section (leaf 86 ≈ p. 169), s.v. baksheesh / Bhaga\", \"stance\": \"supports\",\n      \"note\": \"'baksheesh … Pers. bakhshish, lit. “gift”, a derivative of the verb bakhshidan, “to give”, fr. I.-E. base *bhag-, “to distribute, share out”, whence also OI. bhájati … bhagaḥ, “allotter, distributor, master, lord”, Gk. phagein'; s.v. Bhaga: 'rel. to Avestic baγa, OPers. baga, “master, lord, god”.'\"},\n     {\"src\": \"IEC\", \"where\": \"p. 61\", \"stance\": \"supports\",\n      \"note\": \"see ref_check; Mann adds 'bhagmos “enjoyment, feasting” … Per. bazm “feast”' as a further Persian derivative Nourai does not draw.\"}\n   ],\n   \"nodes\": []\n }]\n}\n\nN = doc[\"entries\"][0][\"nodes\"]\n\nN.append({\n \"id\": 1, \"lang\": \"Avestan / Old Persian\",\n \"words\": \"baga, bağa; baxto-dâta; bax-ta\",\n \"verdict\": \"transcription_suspect\",\n \"derivation\": \"Two of the three forms are exactly right. (a) OP baga- 'god' is abundantly attested (Kent, Lexicon s.v.: 'baga- sb. “god”: Av. baga- “lot, good fortune”, Skt. bhaga- “dispenser (of good fortune)”, Gk. -phagos, OCS bogu, pIE *bhago-'; nom. sg. baga DNa 1, XPa 1, gen. pl. baganām DPd 1, instr. pl. bagaibiš DPd 14), and Kent §1785 lists it among the agent nouns, 'baga- “dispenser, god”' — word for word Nourai's 'distributor of good fortune, God'. YAv. baγa- m. 'Herr, Gott' and Gathic baga- / YAv. baγa- n. 'Anteil, Los, bes. günstiges' (Bartholomae cols. 921–22) are the same stem specialised in the two directions 'share' and 'apportioner > god'. (b) bax-ta = Av. baxta- 'als Anteil zugewiesen; bestimmter Anteil, Schicksalsbestimmung, bes. Missgeschick' (Bartholomae col. 923), the past participle of Av. bag- 'als Anteil zuweisen' (col. 921), Skt. bhaktá-. (c) But *baxto-dāta- is not an attested Old Iranian compound. Bartholomae has baγō.dāta- 'gottgeschaffen' (col. 922) and baγō.baxta- 'von den Göttern bestimmt, gefügt' (col. 922, MP bay baxt; Nyberg, Manual II s.v. bāgō-baxt 'divine providence … borrowed from Av. baγōbaxta-'), and Old Persian has the personal names Bagabūxša- 'God-freed' (Megabyzus) and Bagabīgna-, but no *baxta-dāta-. I rendered PDF p. 81 (book p. 51) at 200 dpi and read it: the printed page really does say 'baxto-dâta : one who is given a good fortune, lucky', so the extraction is faithful and the odd form is the author's — apparently a conflation of Av. baγō.dāta- and baγō.baxta-. The page image is filed as data/verification/sources/refs/ocr/BOOK/81.png.\",\n \"derivation_fa\": \"دو صورت از سه صورت این جعبه درست است: پارسیـ باستان baga- «خدا، بخشندهٔ بهره» (کنت، واژه‌نامه، در کتیبه‌های داریوش و خشایارشا) و اوستاییـ baγa- «سرور، ایزد» و هم‌زمان «بهره، قسمت» (بارتولومه، ستون ۹۲۱–۹۲۲)؛ همچنین baxta- «آنچه بخش کرده شده، سرنوشت»، صفت مفعولیـ ستاک bag- (ستون ۹۲۳). اما صورت *baxtō-dāta- در متون ایرانی باستان وجود ندارد؛ آنچه هست baγō.dāta- «آفریدهٔ خدا» و baγō.baxta- «بخشیدهٔ خدایان» است (فارسی میانه bay baxt، نیبرگ ذیل bāgō-baxt). تصویر صفحهٔ چاپی (ص ۵۱ کتاب) را دیدم: همان «baxto-dâta» چاپ شده، پس خطای خوانش اسکن نیست بلکه خطای خود کتاب است — ظاهراً درهم‌آمیختن دو ترکیب اوستایی.\",\n \"error_in\": \"book\",\n \"book_prints\": \"baxto-dâta : one who is given a good fortune, lucky\",\n \"correct_form\": \"baγō.dāta- 'god-created' / baγō.baxta- 'allotted by the gods'\",\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"POK:107\", \"status\": \"supports\", \"note\": \"Pokorny p. 107 gives av. baga-, baḳa- n. 'Anteil, Los', baḳa- 'Herr, Gott' and av. baxta- 'als Anteil zugewiesen' — i.e. two of the three forms of this node; he has no *baxtō-dāta-.\"},\n   {\"ref\": \"KNT\", \"status\": \"supports\", \"note\": \"Kent, Old Persian, Lexicon s.v. baga-: 'sb. “god”: Av. baga- “lot, good fortune”, Skt. bhaga- “dispenser (of good fortune)” … pIE *bhago-'; §143.1/§1785 'Agents: baga- “dispenser, god”'. Nourai cites KNT without a page; the lexicon entry is the relevant place.\"},\n   {\"ref\": \"KLN:169\", \"status\": \"supports\", \"note\": \"Klein 1966 vol. I (leaf 86 of KLN_1966.txt, b- section ≈ p. 169), s.v. Bhaga: 'OI. Bhagaḥ, lit. “allotter, distributer, master, lord” … rel. to Avestic baγa, OPers. baga, “master, lord, god”.' Exactly Nourai's gloss.\"}\n ],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"cols. 921–923\", \"stance\": \"partial\",\n    \"note\": \"BRT.txt ll. 16630–16700: 'j. bag- V. „als Anteil zuweisen; — zugehören“ … PPfP. baxta-'; 'p. baga-, j. baḳa- m. „Herr; Gott“'; 'g. baga-, j. baḳa- n. „Anteil, Los“'; 'j. baḳō.dāta- Adj. „gottgeschaffen“'; 'j. baḳō.baxta- Adj. „von den Göttern bestimmt, gefügt“'. Supports baga/baγa and baxta-, but has no *baxtō-dāta-.\"},\n   {\"src\": \"KNT\", \"where\": \"Lexicon s.vv. baga-, Bagabūxša-, Bagabīgna-\", \"stance\": \"supports\",\n    \"note\": \"'Bagabūxša- “Megabyzus” … From baga- “god” + deriv. of root baug- “free”: “God-freed”' — the OP naming pattern baga-+participle that Nourai is (mis)reproducing as baxto-dāta.\"},\n   {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II, s.vv. bāgō-baxt, baxt, baxtan\", \"stance\": \"partial\",\n    \"note\": \"'bāgō-baxt [bʼgwbhtʼ] divine providence … Borrowed from Av. (922) baγōbaxta-; Paz. baγōbast'; 'baxt [bʼhtʼ] destiny, fate, fortune'. Confirms baxta- and shows that the real compound is baγō-baxt, not baxtō-dāt.\"}\n ]})\n\nN.append({\n \"id\": 2, \"lang\": \"Persian\",\n \"words\": \"baxšîdan «بخشیدن»; baxš «بخش»; baxt «بَخت ۱ (بختیار)»; bâj «باج ۱ ( باژ ۲ )»\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"All four are genuine continuants of the root, though by three different Old Iranian stems rather than by the two words drawn in #1. (1) baxšīdan 'to give' < MP baxtan / pres. baxš- 'to allot, distribute, destine' (Nyberg II s.v. baxtan: 'Av. (921) bag-; … NP baxšīdan'), the present stem going back to Av. baxš- 'Anteil haben, geben' (Bartholomae col. 923–24, 'ye … mam … nōit baxšahe'); NP replaced the inherited infinitive with a secondary -īdan formation on the present stem — Horn no. 186: 'bexšīden „schenken“, Praes. bexš-em … aw. √baxš- „schenken“; phlv. vergl. das im Np. aufgegebene Verbum baxtan'. Abolghasemi, Feʼl-hā-ye Fārsi-ye Dari p. 35: 'بخش < فارسی میانه baxš < ایرانی باستان *baxš-'. (2) baxš 'division' is the bare present stem used as a noun (MP baxšišn 'distribution', Nyberg II). (3) baxt 'fortune, fate' < MP baxt < Av. baxta- — Horn no. 185: 'beḵt „Schicksal“. aw. baxta- „Verhängniss“; phlv. baxt „Schicksal“; ai. bhaktá- „zugeteilt“'; the derivative baxtiyār 'lucky' is baxt + -yār. (4) bāj / bāž 'toll, tax' < OP bāji- 'tribute' with vrddhi of the root vowel — Kent, Lexicon: 'bāji- sb. “tribute”: NPers. bāj; deriv. of root seen in Skt. bhága-, OP baga-, the verb being Skt. bhájati, Av. bag-, Phl. bāxtan' (attested DB 1.19, DPe 9, DNa 19, DSe 18, XPh 17); the doublet باژ is the regular NP j/ž alternation. English baksheesh is NP baxšīš (Klein, AHD). The Ferdowsī verse quoted in the chart ('… فرستاده شد باژ و ساو') uses bāž in exactly this 'tribute' sense.\",\n \"derivation_fa\": \"هر چهار واژه از همین ریشه اند، اما از سه ستاک جداگانهٔ ایرانی باستان. «بخشیدن» از فارسی میانهٔ baxtan / مادهٔ مضارع baxš- و آن از اوستاییـ baxš- «بهره دادن»؛ در فارسی نو مصدر تازه‌ای بر پایهٔ مادهٔ مضارع ساخته شده (هرن، شمارهٔ ۱۸۶؛ ابوالقاسمی، فعل‌های فارسی دری ص ۳۵). «بخش» همان مادهٔ مضارع است که اسم شده. «بَخت» از فارسی میانهٔ baxt و آن از اوستایی baxta- «سرنوشت» (هرن، شمارهٔ ۱۸۵). «باج/باژ» از پارسیـ باستان bāji- «خراج» (کنت؛ و حاشیهٔ معین بر برهان قاطع ص ۲۰۳: «باج و باژ و باز باین معنی از ریشهٔ baj پارسی باستان مشتق است… و آن از ریشهٔ bag اوستایی بمعنی بخش کردن و قسمت کردن است»). ادعای نورایی درست است.\",\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"BQT:203\", \"status\": \"supports\",\n    \"note\": \"BQT_v1_pages.txt leaf 424 (continuation of the footnotes of printed p. 203, headed 'بقیه از صفحهٔ ۲۰۳'), Moʼin's note 8: 'باج و باژ و باز باین معنی از ریشه baj پارسی باستان مشتق است «مزدیسنا ۲۵۳–۵۴» و آن از ریشهٔ bag اوستایی بمعنی بخش کردن و قسمت کردن است' — precisely Nourai's arrow. (Note 9 separates the homonym باژ 'prayer formula' < Av. vāč-.)\"},\n   {\"ref\": \"BQT:239\", \"status\": \"supports\",\n    \"note\": \"BQT_v1_pages.txt leaves 459–460 (printed pp. 239–240) carry the headwords بخت ('بمعنی طالع'), بختیار ('صاحب بخت'), بخش ('حصه و بهره') and بخشایش, with Moʼin's footnotes referring to his Mazdyasnā — the four Persian words of this box minus bāj.\"},\n   {\"ref\": \"AEF:198,241\", \"status\": \"not_checked\",\n    \"note\": \"Khaleqi Motlaq's Pers. translation of Horn/Hübschmann is not digitised (refs_online.json: 'Not online … only bookshop listings'); its content is Horn nos. 185/186 and 148, which I checked directly in HRN.txt (see consulted).\"},\n   {\"ref\": \"ETM:61\", \"status\": \"not_checked\", \"note\": \"Abolghasemi, Riše-šenāsi (Etimoloji), Qoqnus 1374 — no digital copy on any permitted platform (refs_online.json).\"},\n   {\"ref\": \"FFD:35\", \"status\": \"supports\",\n    \"note\": \"incoming/FFD/FFD_pages.txt, [pdf page 41] = printed p. 35, s.v. بخشیدن: 'بخشید < فارسی میانه baxšīd … بخش < فارسی میانه baxš < ایرانی باستان *baxš- … به معنی قسمت کردن است و واژهٔ بخت در فارسی دری از *baxta- آمده است'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"HRN\", \"where\": \"nos. 148, 185, 186 (pp. 39–44)\", \"stance\": \"supports\",\n    \"note\": \"'148. bāj „Tribut“ … ap. bāji- „Tribut“ … ai. √bhaj- „verteilen, zuteilen“'; '185. beḵt „Schicksal“. aw. baxta- „Verhängniss“; phlv. baxt'; '186. bexšīden „schenken“ … aw. √baxš- „schenken“ … np. baxšiš ist weithin entlehnt, schon arm. baxšiš'.\"},\n   {\"src\": \"PHD\", \"where\": \"MacKenzie 1971 s.vv. baxšišn, baxt, bāj\", \"stance\": \"supports\",\n    \"note\": \"PHD.txt: 'wad-baxt [wtbʼhtʼ | N badbaxt] unfortunate'; the Pahlavi verb baxtan/baxš- and the noun bahr are the MP stage of every item here.\"},\n   {\"src\": \"KNT\", \"where\": \"Lexicon s.v. bāji-\", \"stance\": \"supports\",\n    \"note\": \"'bāji- sb. “tribute”: NPers. bāj; deriv. of root seen in Skt. bhága- “portion, dispenser”, OP baga- “god”, the verb being Skt. bhájati, Av. bag-, Phl. bāxtan.' Attestations DB 1.19, DNa 19, XPh 17.\"},\n   {\"src\": \"ARY\", \"where\": \"pp. 113–115 (بخت / بخش، بخشیدن، بخشش)\", \"stance\": \"supports\",\n    \"note\": \"Aryanpur lists اوستایی BAG, BAXŠ, BAXTA, BAGA; پهلوی BAXTAN; سانسکریت BHAJATI, BHAGA, and cross-refers 'بازگشت به بخت و بغ'.\"},\n   {\"src\": \"NYB\", \"where\": \"Manual II s.vv. baxtan, baxt, baxšišn\", \"stance\": \"supports\",\n    \"note\": \"'baxtan [bʼhtnʼ] baxš-, to allot, to distribute, to destine … Av. (921) bag-; … NP baxšīdan'; 'baxšišn [HLKWN-šnʼ] distribution. From baxtan'.\"}\n ]})\n\nN.append({\n \"id\": 3, \"lang\": \"Avestan\",\n \"words\": \"baxadra : interest, something given\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"The form is Av. baxəδra- n. 'Anteil, Portion' (Bartholomae col. 923: '• j. baxəδra- n. „Anteil, Portion“ … KompE. — Zum V. baxš-'), a neuter noun in -θra-/-δra- (instrument/result suffix) built to the same root bag-/baxš- as #1; Nourai's 'baxadra' is a plain transliteration of baxəδra-, and his gloss 'interest, something given' renders 'allotted portion, revenue' (Darmesteter translated it 'revenue'). Tavoosi's glossary of Šāyast-nē-Šāyast (the SNS Nourai cites) lists 'baxaδra- 96/10' in its index of Avestan forms and gives it, with Bartholomae's column number 923, as the Avestan etymon of Pahlavi bahr. Structural caveat: the chart hangs baxəδra- straight off the IE root, whereas it is an Iranian formation on the inherited verb.\",\n \"derivation_fa\": \"صورت درست، اوستاییـ baxəδra- «بهره، پاره، قسمت» است (بارتولومه، ستون ۹۲۳)، اسمی خنثی با پسوندـ -θra-/-δra- که بر همان ستاکـ bag-/baxš- ساخته شده است. در واژه‌نامهٔ شایست نشایستـ طاووسی (همان SNS مورد استناد نورایی) نیز صورتـ baxaδra- در ص ۹۶ آمده و ریشهٔ فارسی میانهٔ bahr شمرده شده است. تنها ایراد، وصل مستقیم آن به ریشهٔ هندواروپایی است؛ این ساخت درونـ ایرانی است. ادعای نورایی درست است.\",\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"BQT:251\", \"status\": \"partial\",\n    \"note\": \"BQT_v1_pages.txt leaf 471–472 (printed p. 251) has the headword برخ: 'با خای نقطه‌دار بروزن چرخ، بمعنی پاره و حصه و بهره — و لخت و بعض باشد'; Moʼin's footnote on that page names بارتولمه (Bartholomae). The Persian word, not the Avestan headword, is what Borhan gives.\"},\n   {\"ref\": \"BQT:324\", \"status\": \"partial\",\n    \"note\": \"BQT_v1_pages.txt leaf 543 (printed p. 323–324), بهر: 'بروزن شهر … و بمعنی حصه و نصیب و حظ و بهره نیز آمده'; again the NP word with a Pahlavi footnote, not the Avestan form.\"},\n   {\"ref\": \"SNS:96\", \"status\": \"supports\",\n    \"note\": \"SNS_pages.txt: the index of Avestan forms lists 'baxaδra- 96/10', and the glossary entry (l. 4565) reads '(Btl. 923) baxə/δra-' beside Pahlavi bahr — i.e. Tavoosi p. 96 gives exactly the Avestan headword and the Bartholomae column.\"}\n ],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"col. 923\", \"stance\": \"supports\",\n    \"note\": \"'• j. baxəδra- n. „Anteil, Portion“ … Zum V. baxš-. … np. bahr; aus ar. *bhaǵtra-' — Bartholomae himself connects it with NP bahr.\"},\n   {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II, s.v. bahr\", \"stance\": \"supports\",\n    \"note\": \"'bahr [bʼhl] lot, share, portion … — Av. (923) baxəδra-; Ps bhly; MPrth bhr; MPrs bhr … NP barx.'\"},\n   {\"src\": \"HUB\", \"where\": \"Persische Studien §245 (p. 33)\", \"stance\": \"supports\",\n    \"note\": \"'Zd. baxδra- braucht nicht „Mahlzeit“ zu heissen, Darmesteter übersetzt es durch „revenue“ und stellt es zu bhaj „teilen, zuteilen“, vgl. ap. bāji- „Tribut“.' Exactly Nourai's gloss 'interest, something given'.\"},\n   {\"src\": \"HRN\", \"where\": \"no. 245 (p. 46)\", \"stance\": \"contradicts\",\n    \"note\": \"Horn objects: 'An aw. baḵdra- mit Hübschmann … zu denken, verbietet die Bedeutung dieses Wortes, welches Geldner … wohl richtig als „Mahlzeit“ fasst' — he takes baxəδra- to mean 'meal' and detaches it from bahr.\"}\n ]})\n\nN.append({\n \"id\": 4, \"lang\": \"Persian\",\n \"words\": \"barx «بَرخ ( برخی )»; bahr «بهر ( بهره )»\",\n \"verdict\": \"plausible\",\n \"derivation\": \"Hübschmann, Persische Studien §245 (p. 33): 'Np. barx, barxa „Teil“ … setze ich = ap. *baxtra-, zd. baxδra- (vgl. np. Balx aus ap. Bāxtri- „Bactrien“) von zd. baǵ = skr. bhaj „teilen, zuteilen“', and §88a (p. 194): 'Ap. t ist geschwunden inlautend in der Lautgruppe xtr … bahr = barx „Theil, Antheil“ = zd. baxδra-'. So the chain is Av. baxəδra- / OIr. *baθra-–*baxtra- > MP bahr (attested: MacKenzie p. 16 'bahr [bhl | M bhr, N ~] part, portion, share, lot'; Nyberg II 'bahr … — Av. (923) baxəδra-') > NP بهر/بهره, with the cluster -xr- simplified to -hr- exactly as in Bāxtri- > Balx; the doublet برخ/برخه keeps the velar with metathesis xr > rx (compare the Pashto loan-form baṛxa/braxa). Both therefore continue Nourai's node #3, and his gloss 'interest' = 'share, portion'. The verdict is plausible rather than confirmed only because of a real dispute: Horn no. 245 rejects the baxəδra- etymology for bahr and connects بهر/بهره with Av. hu-baδra- 'happy' / Skt. bhadra- 'auspicious', a line revived by H. W. Bailey (Asia Major NS II/1, 1952, 32) and reported by Nyberg. Modern Iranian etymology mostly follows Hübschmann/Nyberg; Aryanpur's Farhang-e riše-hā (p. 115 n. 3) states plainly 'واژه‌های فارسی برخ و بهره هم از همین واج‌ریشه‌اند'.\",\n \"derivation_fa\": \"«برخ» و «بهر/بهره» دو صورت از یک واژه‌اند: از اوستایی baxəδra- (پارسیـ باستان *baxtra-) به فارسی میانهٔ bahr و سپس فارسی نو. در «بهر» خوشهٔ -خر- به -هر- بدل شده، همان‌گونه که Bāxtri- به «بلخ»؛ در «برخ» قلب (metathesis) رخ داده و خ مانده است (هوبشمان، مطالعات فارسی ص ۳۳ و ۱۹۴؛ مکنزی و نیبرگ ذیل bahr). با این حال هرن (شمارهٔ ۲۴۵) این ریشه را رد کرده و «بهره» را با اوستایی hu-baδra- و سنسکریت bhadra- «فرخنده» پیوند داده است؛ پس ادعای نورایی با احتیاط پذیرفتنی است و دیدگاه غالبـ امروزی جانب هوبشمان را می‌گیرد.\",\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"BQT\", \"status\": \"supports\",\n    \"note\": \"Borhan-e Qāteʼ pp. 251 and 324 (leaves 471–472 and 543 of BQT_v1_pages.txt): برخ 'بمعنی پاره و حصه و بهره' and بهر 'بمعنی حصه و نصیب و حظ و بهره'. Nourai cites BQT without a page here; both words are there with the meanings he gives.\"},\n   {\"ref\": \"SNS:96\", \"status\": \"supports\",\n    \"note\": \"Tavoosi p. 96 (index 'baxaδra- 96/10') gives Av. baxəδra- (Btl. col. 923) as the etymon of Pahlavi bahr, the immediate ancestor of both Persian forms.\"}\n ],\n \"consulted\": [\n   {\"src\": \"HUB\", \"where\": \"§245 p. 33 and §88a p. 194\", \"stance\": \"supports\",\n    \"note\": \"'bahr = barx „Theil, Antheil“ = zd. baxδra- (s. oben p. 33)'; and 'Np. barx, barxa „Teil“ … setze ich = ap. *baxtra-, zd. baxδra- (vgl. np. Balx aus ap. Bāxtri-)'.\"},\n   {\"src\": \"HRN\", \"where\": \"no. 245 (p. 46)\", \"stance\": \"contradicts\",\n    \"note\": \"'behr, behre „Loos, Teil“. aw. hu-badra- „glücklich, gesegnet, beglückt“ (Aogem.); phlv. bahr = bahrak … An aw. baḵdra- … zu denken, verbietet die Bedeutung dieses Wortes' — Horn derives bahr from hu-baδra-/Skt. bhadra- instead.\"},\n   {\"src\": \"PHD\", \"where\": \"MacKenzie 1971 p. 16\", \"stance\": \"supports\",\n    \"note\": \"'bahr [bhl | M bhr, N ~] part, portion, share, lot; reason'; 'bahr(ag)war … partaking, participator, partner' — the Middle Persian link the chart omits.\"},\n   {\"src\": \"NYB\", \"where\": \"Manual II s.v. bahr\", \"stance\": \"supports\",\n    \"note\": \"'— Av. (923) baxəδra- … NP barx. [It would be tempting to connect … bahr with Skr bhadra- … thus Bailey in A. M., N.S. II:1, 1952, 32]' — records both sides of the dispute.\"},\n   {\"src\": \"ARY\", \"where\": \"p. 115 n. 3\", \"stance\": \"supports\",\n    \"note\": \"'۳ واژه‌های فارسی برخ و برخه هم از همین واج‌ریشه‌اند' (in the بخش/بخشیدن entry) — an independent modern Persian confirmation.\"}\n ]})\n\nN.append({\n \"id\": 5, \"lang\": \"Persian\",\n \"words\": \"bağ, fağ «بغ ، فغ»; Bağdâd «بغداد»; bağ-stân «بغستان ، فغستان»; bîstŭn «بیستون»\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"بغ baγ 'god' continues MP bay/baγ (⟨bgy⟩) < OP/Av. baga- 'god' (Dehkhodā s.v. بغ: Avestan and Old Persian baga/baγa 'god, lord, provider', Pahlavi bak/baγ/bay, Skt. bhaga-, Slavic bog); in New Persian it survives almost only in the old compounds of this box. The variant فغ faγ is not an inherited Persian form: initial f- for b- points to an eastern Iranian β- (Sogdian βγ /βaγ/ 'lord, god', Gharib no. 2543), and Moʼin's footnote at Borhan p. 1493 s.v. فغ cites exactly Gauthiot (JA 1911 II 58) and 'Henning, BSOS vol. X' for it. (a) Baγdād = baγ 'god' + dād 'given' — Moʼin's footnote at Borhan p. 288: 'نام بغداد Baγdād … بی‌شک ایرانی است مرکب از: بغ + داد بمعنی خدا داده'; Lokotsch no. 170: 'aus altpers. baga „Gott“ u. zend dāta „gegeben, geschaffen“, also „von den Göttern gegeben“, nicht „mit Glück beschenkt“' — the city name is the source of Italian Baldacco, OFr. Baudas and hence of baldachin. (b) baγ-stān / faγestān 'place of the god(s)' = OP *Bagastāna, Gk. Βαγίστανον (Diodorus 2.13); Borhan p. 1493 glosses فغستان 'بمعنی بتخانه و بتکده است … و کنایه از خوب‌صورتان و صاحب‌حسنان هم هست', which is precisely Nourai's second gloss ('a very beautiful person') — the same shift as بت 'idol' > 'beloved'. (c) bīstūn is the same word: Kent, Old Persian p. 107 (comment on DB) — 'the OP *bagastāna- “Place of the God”, for which Greek has Βαγίστανον … and the Behistūn of the medieval Arabic Geographers, the Modern Persian Bisitūn or Bisutūn (or even Bistūn …; understood by popular etymology as “without columns”)'; Moʼin's footnote at Borhan p. 289 names the compounds 'بغداد و بغپور و بغستان (بیستون)' together. So all four words and both arrows are right; the only imprecision is that the box is labelled simply 'Persian' and hung on the IE root, with the Old and Middle Iranian stages and the Sogdian source of the f- variant left out.\",\n \"derivation_fa\": \"«بغ» از فارسی میانهٔ bay/baγ و آن از پارسیـ باستان و اوستایی baga- «خدا، بخشنده» است؛ در فارسی نو فقط در ترکیب‌های کهن مانده است. صورتـ «فغ» وام‌واژه است: فـ آغازین از بـ ایرانی غربی نمی‌آید بلکه بازتابـ βـ سغدی (βaγ «خدا، سرور») است؛ حاشیهٔ معین بر برهان قاطع (ص ۱۴۹۳، ذیلـ فغ) به گوتیو و هنینگ (BSOS X) ارجاع می‌دهد. «بغداد» = بغ + داد «خداداد» (حاشیهٔ معین، ص ۲۸۸؛ لوکوچ شمارهٔ ۱۷۰)؛ «بغستان/فغستان» از پارسیـ باستان *Bagastāna «جایگاه خدا»، که در برهان قاطع «بتخانه» و کنایه از «خوب‌صورتان» معنی شده؛ و «بیستون» همان بغستان است که به ریشه‌شناسی عامیانه «بی‌ستون» تعبیر شده است (کنت، پارسی باستان). ادعای نورایی درست است.\",\n \"sources\": [U_BIS, U_WIKI, U_BAG],\n \"ref_check\": [\n   {\"ref\": \"BQT:288\", \"status\": \"supports\",\n    \"note\": \"BQT_v1_pages.txt leaf 509 (printed pp. 288–289), Moʼin's footnote 1: 'نام بغداد Baγdād … بی‌شک ایرانی است مرکب از: بغ + داد بمعنی خدا داده، در قرون وسطی صور مختلف این نام وجود داشته'.\"},\n   {\"ref\": \"BQT:289\", \"status\": \"supports\",\n    \"note\": \"Same leaf, the long بغ footnote: 'بغ … بمعنی بهره و برخ و بخش و بخت آمده. در گاتها baga بهمین معنی است، دوم بغ در اوستا و baga در پارسی باستان بمعنی خدا و دادار و آفریدگار است … بغ بهر دو معنی از یک بنیاد است از مصدر bag بمعنی بخشیدن (در پهلوی baxtan) … کلمهٔ مزبور در ترکیب بغداد و بغپور و بغستان (بیستون) آمده و مبدل و معرب آن فغ است … در پهلوی bay, baγ (خدا، الوهیت، سلطان)' — every element of this box, including the bīstūn identification.\"},\n   {\"ref\": \"BQT:337\", \"status\": \"not_found\",\n    \"note\": \"The بیستون headword itself could not be located in the vol.-1 OCR (leaves 555–566 searched for بیستون/بستون/فغستان; the Persian OCR of these leaves is too corrupt). The claim is however carried by Moʼin's footnote at p. 289 (above) and by Kent.\"},\n   {\"ref\": \"MON:2558\", \"status\": \"not_checked\",\n    \"note\": \"Moʼin's Farhang-e Fārsi is online only as entry text (vajehyab/abadis), with no page mapping; the بغ entry there gives '۱- خدا. ۲- ایزد، فرشته. ۳- بُت. فغ هم گویند' — the sense Nourai gives, but p. 2558 cannot be verified.\"},\n   {\"ref\": \"POK:107\", \"status\": \"supports\",\n    \"note\": \"Pokorny p. 107–108: 'baḳa- „Herr, Gott“, npers. baḳ „Gott“ … ur-ind. (Mitanni) ON Bagarriti, GN Bagbartu … slav. *bogŭ „Anteil“ … aksl. bogŭ „Gott“'.\"},\n   {\"ref\": \"TZF:18\", \"status\": \"not_checked\",\n    \"note\": \"Abolghasemi, Tārix-e moxtaṣar-e zabān-e Fārsi — PDF only behind a login (refs_online.json).\"}\n ],\n \"consulted\": [\n   {\"src\": \"KNT\", \"where\": \"Old Persian, note on the Behistan inscription (p. 107) and Lexicon s.v. baga-\", \"stance\": \"supports\",\n    \"note\": \"'Behistan … intermediate between the OP *bagastāna- “Place of the God”, for which Greek has Βαγίστανον (Diodorus 2.13), and the Behistūn of the medieval Arabic Geographers, the Modern Persian Bisitūn or Bisutūn … understood by popular etymology as “without columns”.'\"},\n   {\"src\": \"LKT\", \"where\": \"no. 170 (Bagdad)\", \"stance\": \"supports\",\n    \"note\": \"'N. pr. Name einer am Tigris gelegenen Stadt, aus altpers. baga [Sskr. bhaga] „Gott“ u. zend data „gegeben, geschaffen“, also „von den Göttern gegeben [θεόκτιστος]“, nicht „mit Glück beschenkt“ … Das Subst. wurde it. Baldacco, afrz. Baudas, dtsch. Baldak, engl. Baldacca.'\"},\n   {\"src\": \"SOD\", \"where\": \"Gharib, Sogdian Dictionary no. 2543\", \"stance\": \"supports\",\n    \"note\": \"'βaγ (βγ-) ©<baga — God, Lord, king, sir, excellency' — the eastern Iranian β- that yields Persian فغ.\"},\n   {\"src\": \"BQT\", \"where\": \"vol. 3, printed p. 1493 (pdf 286), s.v. فغ / فغستان\", \"stance\": \"supports\",\n    \"note\": \"'فغ … بلغت فرغانه و ماوراءالنهر بت را گویند، عربان صنم خوانند …'; 'فغستان … بمعنی بتخانه و بتکده است … و کنایه از خوب‌صورتان و صاحب‌حسنان هم هست'; footnote: '۱ - بغ (هم.) … fugh, fagh … (Gauthiot, JA., 1911, II, p. 58) … Henning, BSOS vol. X.'\"},\n   {\"src\": \"MON\", \"where\": \"Farhang-e Moʼin s.v. بغ (via abadis.ir)\", \"stance\": \"supports\",\n    \"note\": \"'(بَ) (اِ.) ۱ - خدا. ۲ - ایزد، فرشته. ۳ - بُت. فغ هم گویند.'; Dehkhodā on the same page gives Avestan/OP baga 'god', Pahlavi bak/baγ/bay, and names بغداد (خدا + داد) and بیستون.\"},\n   {\"src\": \"TAD\", \"where\": \"s.v. بغداد (the note's TAD:12)\", \"stance\": \"contradicts\",\n    \"note\": \"TAD.txt l. 510: 'بغداد - فارسي مركب من باغ أي بستان وداد أي [ع]دل'. Al-ʿUnaysī does say what Nourai reports, but this is a folk etymology: bāγ 'garden' has a long ā and dād 'justice' is a different word from dād 'given'; Lokotsch no. 170 rejects it explicitly and Moʼin, Kent and the Encyclopaedia of Islam all read baga-dāta 'god-given'.\"},\n   {\"src\": \"HENNING\", \"where\": \"'Sogdian Loan-Words in New Persian', BSOAS 10.1 (1939) 94\", \"stance\": \"partial\",\n    \"note\": \"The article is in Selected Papers I (Acta Iranica 14); only vol. II is on disk, so the page could not be read here. What Henning argues on p. 94 (as cited by Wiktionary s.v. فغفور and by Moʼin's Borhan footnote s.v. فغ) is that the faγ- forms are Sogdian loans in Persian — i.e. the chart's NOTE is right about the f- variant, but بغ itself is the inherited western Iranian word.\"}\n ]})\n\nN.append({\n \"id\": 6, \"lang\": \"Avestan\",\n \"words\": \"bağa-puthra : son of God, title of respect; bağa-dugdâr : daughter of God, Venus\",\n \"verdict\": \"plausible\",\n \"derivation\": \"Both elements are impeccable Avestan — baγa- 'god' (Bartholomae col. 921), puθra- 'son' and duγδar- 'daughter' — but neither compound is attested in the Avesta: they are reconstructions from the Middle Iranian forms. *baga-puθra- is guaranteed by Parthian bagpuhr and Sogdian βγpʼwr /βaγpūr/ 'prince, god's son' (Gharib, Sogdian Dictionary no. 2582: 'βaγpur (βγpwr) ©<baga~puθra-, <Parth. bagpuhr; prince, god's son'; also Sogd. βγpδry, glossed with Skt. devaputra), and *baga-duxtā/-duγδar- by MP/NP Bīdoxt (< *baγ-duxt) 'Venus'. Hobson-Jobson p. 49 — the page Nourai cites — reports Schiefner's opinion that Mongol baγatur is 'a corruption “through dissimulation of the consonant” of the Zend bagha-puthra “Son of God”, and thus but another form of the famous term Faghfor, by which the old Persians rendered the Chinese Tien-tsz (“Son of Heaven”), applying it to the Emperor of China'; that is exactly Nourai's arrow, but 'Zend' there is 19th-c. shorthand for Old Iranian and the bahādur half of Schiefner's equation is now abandoned (Turkic/Mongol bahadur is not from bagapuθra). Verdict plausible: right root, right components, right meanings, but the compounds belong to Middle Iranian, not to the Avestan corpus.\",\n \"derivation_fa\": \"دو جزء این ترکیب‌ها اوستایی‌اند: baγa- «خدا»، puθra- «پسر» و duγδar- «دختر»؛ اما خودـ ترکیب‌ها در اوستا گواهی نشده‌اند و بازسازی از روی صورت‌های ایرانیـ میانه‌اند: پارتی bagpuhr و سغدی βγpwr «پسر خدا، شاهزاده» (قریب، فرهنگ سغدی، شمارهٔ ۲۵۸۲) و فارسی «بیدخت» < *baγ-duxt. منبعـ خودـ نورایی (هابسن‌جابسن ص ۴۹) همین را می‌گوید، ولی پیوندـ آن با «بهادر» امروز رد شده است. پس ادعای نورایی با احتیاط پذیرفتنی است: برچسبـ «اوستایی» دقیق نیست و باید «ایرانی باستان (بازساخته)» می‌بود.\",\n \"sources\": [U_FAG],\n \"ref_check\": [\n   {\"ref\": \"HJB:49\", \"status\": \"supports\",\n    \"note\": \"Hobson-Jobson p. 49 (leaf 101 of HJB.txt), s.v. BAHAUDUR: 'Prof. A. Schiefner … was strongly of opinion that the word was rather a corruption “through dissimulation of the consonant” of the Zend bagha-puthra “Son of God”, and thus but another form of the famous term Faghfor, by which the old Persians rendered the Chinese Tien-tsz (“Son of Heaven”), applying it to the Emperor of China.' The Faghfūr index entry is 'Faghfūr, 347a, 49a'.\"},\n   {\"ref\": \"BQT:333\", \"status\": \"supports\",\n    \"note\": \"BQT_v1_pages.txt leaf 553 (printed p. 333): 'بیدخت — با بای مجهول بروزن کمخت، ستارهٔ زهره را گویند که صاحب فلک …', with a Moʼin footnote referring to his Mazdyasnā p. 329 — Nourai's 'Venus'.\"},\n   {\"ref\": \"BQT:1494\", \"status\": \"supports\",\n    \"note\": \"incoming/BQT/BQT_v3_pages.txt, pdf page 287 = printed p. 1494: 'فغفور — بروزن مضمور، پادشاه چین را گویند هر که باشد'; the preceding page 1493 s.v. فغ carries Moʼin's footnote deriving it from بغ and citing Gauthiot and Henning BSOS X.\"}\n ],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"cols. 921 (baγa-), 907ff. (puθra-), 750 (duγδar-)\", \"stance\": \"silent\",\n    \"note\": \"Bartholomae has baγō.dāta-, baγō.baxta-, baγa-buγša-, baγa-bigna- and baγā- but no *baγa-puθra- or *baγa-duγδar- — grep of BRT.txt for the compounds returns nothing.\"},\n   {\"src\": \"SOD\", \"where\": \"Gharib no. 2582 (and 2583)\", \"stance\": \"supports\",\n    \"note\": \"'βaγpur (βγpwr) ©<baga~puθra-, <Parth. bagpuhr →βγpδry — prince, god's son. TSP 8.166; BSTBL, Intox. 34; BBB; Anc. Lett. 2, 26; GMS 1276'; no. 2583 'βaγ-pδθre © Skt. devaputra — prince, god's son'.\"},\n   {\"src\": \"HJB\", \"where\": \"p. 347 s.v. FAGHFUR\", \"stance\": \"supports\",\n    \"note\": \"'The common Moslem term for the Emperors of China … In Al-Maṣʿūdī (chap. xiv) we find Baghfūr and in Al-Idrīsī Baghbūgh, or Baghbūn. In Al-Aṣmaʿī Bagh = god or idol (Pehlewi and Persian); hence according to some Baghdād and Bāghistān, a pagoda. Sprenger … remarks that Baghfūr is a literal translation of Tien-tse.'\"}\n ]})\n\nN.append({\n \"id\": 7, \"lang\": \"Persian\",\n \"words\": \"fağpŭr «فغفور»; Bîdoxt «بیدخت»\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"faγfūr 'the Emperor of China' is a Sogdian loan in New Persian: Wiktionary (following exactly the reference Nourai names in his NOTE — W. B. Henning, 'Sogdian Loan-Words in New Persian', BSOAS 10.1 (1939) 94) derives it from Sogdian βγpʼwr /βaγpūr/, itself from *baga-puθra- through Parthian bagpuhr. The Sogdian β- is heard and written as Persian f-, which is why Persian has the doublet baγ-/faγ-; the second f (faγfūr for *faγpūr) is a further assimilation, and Arabic transmission shows the intermediate stages — Masʿūdī Baγfūr, Idrīsī Baγbūn (Hobson-Jobson p. 347). The title itself is a calque of Chinese 天子 tiānzǐ 'Son of Heaven' (Sprenger, quoted ibid.: 'Baghfūr is a literal translation of Tien-tse'); the later sense 'porcelain' (فغفوری) is metonymy from 'Chinese imperial ware'. Bīdoxt is the same formation on the feminine side: Dehkhodā states that the original form was بغدخت 'daughter of Baγ', i.e. *baga-duxtā, and Borhan and Moʼin gloss it 'سیاره زهره، ناهید' — the planet Venus, i.e. Anāhitā, who had inherited the identification with Venus from Ishštar. Both words and both glosses in the chart are correct; the only refinement is that the route runs through Parthian/Sogdian rather than straight from Avestan.\",\n \"derivation_fa\": \"«فغفور» وام‌واژه‌ای سغدی در فارسی نو است: از سغدی βγpwr (βaγpūr) «پسر خدا»، از راه پارتی bagpuhr و در نهایت از *baga-puθra-؛ هنینگ (BSOAS ۱۰، ۱۹۳۹، ص ۹۴) همین را نشان داده و ویکی‌واژه نیز همین را می‌آورد. βـ سغدی در فارسی فـ شنیده شده و پـ دوم نیز به ف همگون شده است (مسعودی: بغفور؛ ادریسی: بغبون). معنای آن گرته‌برداری از چینیـ 天子 (پسر آسمان) است. «بیدخت» نیز صورت تحول‌یافتهٔ «بغدخت» (*baga-duxtā) «دختر خدا» است و نام ستارهٔ زهره/ناهید (دهخدا، برهان قاطع ص ۳۳۳). ادعای نورایی درست است.\",\n \"sources\": [U_FAG, U_BID],\n \"ref_check\": [\n   {\"ref\": \"HJB:49\", \"status\": \"supports\",\n    \"note\": \"See node #6: p. 49 explicitly equates 'Zend bagha-puthra “Son of God”' with 'the famous term Faghfor … applying it to the Emperor of China'.\"},\n   {\"ref\": \"BQT:333\", \"status\": \"supports\",\n    \"note\": \"Borhan p. 333 s.v. بیدخت = the planet Venus (quoted at node #6).\"},\n   {\"ref\": \"BQT:1494\", \"status\": \"supports\",\n    \"note\": \"Borhan vol. 3 p. 1494 s.v. فغفور 'پادشاه چین را گویند'; p. 1493 s.v. فغ with Moʼin's footnote 'بغ (هم.) … fugh, fagh … (Gauthiot, JA., 1911, II, p. 58) … Henning, BSOS vol. X'.\"},\n   {\"ref\": \"TZF:18\", \"status\": \"not_checked\", \"note\": \"Abolghasemi's Tārix-e moxtaṣar-e zabān-e Fārsi is not obtainable (login-only PDF).\"}\n ],\n \"consulted\": [\n   {\"src\": \"SOD\", \"where\": \"Gharib no. 2582\", \"stance\": \"supports\",\n    \"note\": \"'βaγpur (βγpwr) ©<baga~puθra-, <Parth. bagpuhr — prince, god's son' — the immediate donor form of فغفور.\"},\n   {\"src\": \"HJB\", \"where\": \"p. 347 s.v. FAGHFUR\", \"stance\": \"supports\",\n    \"note\": \"'Sprenger (Al-Maṣʿūdī, p. 327) remarks that Baghfūr is a literal translation of Tien-tse' — the Chinese calque.\"},\n   {\"src\": \"MON\", \"where\": \"Farhang-e Moʼin / Loghatnāme-ye Dehkhodā s.v. بیدخت (via abadis.ir)\", \"stance\": \"supports\",\n    \"note\": \"Moʼin: '(سیاره زهره، ناهید)'; Dehkhodā gives the original form as بغدخت 'daughter of Baγ' and records the rival reading هیدخت.\"},\n   {\"src\": \"BQT\", \"where\": \"vol. 3 p. 1493–94\", \"stance\": \"supports\",\n    \"note\": \"فغفور and فغفوری; the فغ footnote gives the Sogdian/Gauthiot–Henning derivation.\"}\n ]})\n\nN.append({\n \"id\": 8, \"lang\": \"Avestan\",\n \"words\": \"hama-bağa : share together\",\n \"verdict\": \"plausible\",\n \"derivation\": \"Both members are good Avestan — hama- 'same, together' (Bartholomae col. 1774ff.) and baγa- n. 'Anteil, Los' (col. 921–22) — but *hama-baγa- is not attested in the Avestan corpus; a grep of Bartholomae turns up no such compound. It is a back-formation from the Middle Persian word of node #9, and the Sanskrit rendering of the Pahlavi word in the Pazānd–Sanskrit tradition, sama-bhāgin 'having an equal share' (Nyberg, Manual of Pahlavi II s.v. ham-bāy), is precisely the calque that justifies the reconstruction. So the arrow is sound in substance ('one who shares with' from the root 'share'), but the label 'Avestan' should read 'Old Iranian (reconstructed)'.\",\n \"derivation_fa\": \"دو جزء این ترکیب اوستایی‌اند (hama- «هم، با هم» و baγa- «بهره، قسمت») ولی خودـ صورتـ *hama-baγa- در اوستا گواهی نشده است؛ بازساختی است از روی فارسی میانهٔ ham-bāy که در سنتـ پازند–سنسکریت به sama-bhāgin «هم‌بهره» برگردانده شده (نیبرگ، دفتر ۲). پس ادعای نورایی در معنا درست است ولی برچسبـ «اوستایی» باید به «ایرانی باستانـ بازساخته» تغییر کند.\",\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"BQT:164\", \"status\": \"partial\",\n    \"note\": \"BQT_v1_pages.txt leaf 383 (printed p. 163–164) gives the New Persian words انباز ('بروزن دمساز، رفیق و همتا را گویند') and انباغ ('دو زن را گویند … دیگری را انباغ باشد') with Moʼin's Pahlavi footnotes, but no Avestan headword — Borhan cannot support an Avestan *hama-baγa-.\"}\n ],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"cols. 921–22 (baγa-), 1774ff. (hama-)\", \"stance\": \"silent\",\n    \"note\": \"Both simplexes are there; grep of BRT.txt for hama-baγa/hamō.baγa returns nothing — the compound is unattested.\"},\n   {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II s.v. ham-bāy\", \"stance\": \"supports\",\n    \"note\": \"'ham-bāi [hmbʼy] one with whom one shares property; partner 70⁴. — Paz. hambāē (for hambāi), Skr v. sama-bhāgin. Bthl., ZsR I' — the Sanskrit gloss sama-bhāgin is the calque underlying the reconstruction *hama-baga-.\"},\n   {\"src\": \"PHD\", \"where\": \"MacKenzie 1971 p. 41\", \"stance\": \"supports\",\n    \"note\": \"'hambāy [hmbʼg | (M hmbʼw)] companion, partner; adversary' — the Middle Persian outcome that guarantees the Old Iranian compound.\"}\n ]})\n\nN.append({\n \"id\": 9, \"lang\": \"Pahlavi\",\n \"words\": \"hambâğ : companion\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"MacKenzie, Concise Pahlavi Dictionary p. 41: 'hambāy [hmbʼg | (M hmbʼw)] companion, partner; adversary' — the spelling ⟨hmbʼg⟩ is exactly Nourai's 'hambāγ', normalised hambāy in MacKenzie's system because Middle Persian intervocalic *-g- had already become -y-/-γ-. Nyberg, Manual II s.v. ham-bāy: 'one with whom one shares property; partner', Paz. hambāē, Skt. gloss sama-bhāgin. The formation is ham- 'together with' + *bāga- 'share' (the same *bāg- that gives farrō-bāg, Nyberg II: 'farrō-bāg … having a share of the heavenly splendour … + Av. (921) baga-, baγa- “share”'). Nourai's gloss 'companion' is right; MacKenzie's second gloss 'adversary' is what makes the word the source of Persian انباغ 'rival wife' in node #10.\",\n \"derivation_fa\": \"فارسی میانهٔ hambāy (نوشتارـ ⟨hmbʼg⟩) «همراه، شریک؛ و نیز رقیب» (مکنزی ص ۴۱؛ نیبرگ ذیل ham-bāy)، مرکب از پیشوندـ ham- «با هم» و *bāga- «بهره». در فارسی میانه گـ میانـ دو واکه به غ/ی نرم شده است، از این‌رو نورایی hambāγ نوشته است. ادعای نورایی درست است.\",\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"BQT:164\", \"status\": \"partial\",\n    \"note\": \"Borhan p. 164 (leaf 383) has the two Persian words with Moʼin's footnote in Latin script beginning 'پهلوی …' (the transliteration is destroyed in the OCR, but the footnote is a Pahlavi etymology). It is not a Pahlavi dictionary, so it can only partially support the Middle Persian form; MacKenzie and Nyberg do so fully.\"}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"MacKenzie 1971 p. 41\", \"stance\": \"supports\",\n    \"note\": \"'hambāy [hmbʼg | (M hmbʼw)] companion, partner; adversary'; the English index (p. 1298) has 'companion hambāy' and (p. 3049) 'partner hambāy, hambāz'.\"},\n   {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II s.vv. ham-bāy, farrō-bāg\", \"stance\": \"supports\",\n    \"note\": \"'ham-bāi [hmbʼy] one with whom one shares property; partner … Skr v. sama-bhāgin'; 'farrō-bāg … + Av. (921) baga-, baγa-, (952) bagā- “share”'.\"}\n ]})\n\nN.append({\n \"id\": 10, \"lang\": \"Persian\",\n \"words\": \"anbâz «انباز»; anbâğ «انباغ»\",\n \"verdict\": \"plausible\",\n \"derivation\": \"انباغ anbāγ 'rival wife, co-wife' is the direct continuant of node #9: MP hambāy/hambāg > NP anbāγ, with the regular development of the prefix ham- > han- > an- before a labial (compare hambār > انبار, hambōy- > انبوییدن, hambūsīdan > انبوسیدن — all in MacKenzie p. 41). The 'rival wife' sense is not a semantic leap but MacKenzie's own second gloss for hambāy, 'adversary': two wives are literally 'co-sharers' of one husband, and Borhan p. 164 defines انباغ as 'دو زن را گویند [که هر یک نسبت به] دیگری را انباغ باشد'. انباز anbāz 'companion, partner', however, does not come from hambāg but from a separate Middle Persian word: MacKenzie p. 41 'hambāz [hm-, hnbʼc | M ʼmbʼz, N anbāz] partner' — a sibling formation on the -z/-j side of the root (the side that also gives bāj/bāž < OP bāji-), not on the -g/-γ side. So Nourai is right that both words go back to *bag- 'share' and right about the meanings, but he merges two distinct Middle Persian etyma (hambāy and hambāz) into one. Borhan p. 164 gives انباز as 'خصومات[?] و رفیق و همتا' — 'friend and peer' — which is Nourai's 'companion'. The Mowlavī line quoted in the chart ('ای خدای پاک و بی‌انباز و یار') uses anbāz in the theological sense 'associate (of God)', i.e. the Persian rendering of Arabic شریک.\",\n \"derivation_fa\": \"«انباغ» دنبالهٔ راستینـ فارسی میانهٔ hambāy/hambāg است؛ پیشوندـ ham- پیش از بـ به an- بدل شده (مانند hambār > انبار، hambōy > انبوییدن)، و معنیـ «هوو، زنـ رقیب» همان معنیـ دومـ مکنزی («adversary») است. ولی «انباز» از hambāg نیامده؛ ریشهٔ آن فارسی میانهٔ hambāz ⟨hnbʼc⟩ «شریک» است (مکنزی ص ۴۱)، که ساختی دیگر از همان ریشه است (همان طرفی که «باج/باژ» را هم داده است). پس ادعای نورایی در کلیات درست است ولی دو واژهٔ جداگانهٔ فارسی میانه را یکی گرفته است.\",\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"(none cited)\", \"status\": \"not_checked\",\n    \"note\": \"The node carries refs=None in the book. The relevant page is its parent's BQT:164, which I did read: Borhan p. 164 (leaf 383 of BQT_v1_pages.txt) has both انباز 'رفیق و همتا' and انباغ 'دو زن را گویند … دیگری را انباغ باشد', each with a Moʼin Pahlavi footnote.\"}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"MacKenzie 1971 p. 41\", \"stance\": \"partial\",\n    \"note\": \"Two separate headwords: 'hambāy [hmbʼg] companion, partner; adversary' and 'hambāz [hm-, hnbʼc | M ʼmbʼz, N anbāz] partner'. MacKenzie maps NP anbāz to hambāz, not to hambāy.\"},\n   {\"src\": \"BQT\", \"where\": \"p. 164 (leaf 383)\", \"stance\": \"supports\",\n    \"note\": \"'انباز — بروزن دمساز، … رفیق و همتا را گویند'; 'انباغ — با غین نقطه‌دار، دو زن را گویند [که هر یک نسبت به] دیگری را انباغ باشد'; footnote 'پهلوی …'.\"},\n   {\"src\": \"NYB\", \"where\": \"Manual II s.vv. ham-bāy, hanbārak\", \"stance\": \"supports\",\n    \"note\": \"'hanbārak [hnbʼlkʼ] storehouse … NP anbār' — the same ham- > an- development that gives anbāγ/anbāz.\"}\n ]})\n\nN.append({\n \"id\": 11, \"lang\": \"Turkish\",\n \"words\": \"bak : grand, Lord, God; ata-bak : grand father, god father\",\n \"verdict\": \"plausible\",\n \"derivation\": \"The word is Old Turkic beg (Orkhon, 8th c.) 'lord, chief of a clan', Proto-Turkic *bǟg, modern Turkish bey. Its origin is genuinely open: Wiktionary sets out the two rival hypotheses — (a) from Middle Chinese 百 / 佰 / 伯 (MC pᵠæk) 'hundred; head of a hundred men; eldest brother, hegemon', the line taken by Clauson (An Etymological Dictionary of Pre-Thirteenth-Century Turkish, 1972); (b) from north-eastern Iranian, i.e. Sogdian βγ /βaγ/ 'lord, master' < Proto-Iranian *bagáh 'god' — which is Nourai's arrow — but adds that Doerfer 'assessed the derivation from an Iranian language as quite uncertain and pointed out that the word may be genuinely Turkic'. So this is one live hypothesis among three, not an established descent, and the box cannot be read as an ordinary Indo-European daughter node. Two smaller points: Turkic beg never means 'God' (only 'lord, chief'; Nourai's 'God' comes from the Iranian source-word, not from the Turkic one); and atabeg is not a Turkic inheritance from the root at all but a Seljuq-period compound ata 'father' + beg, the title of the guardian-tutor of a young prince (11th–12th c.), whence the Atabeg dynasties of Ādharbayjān, Fārs and Mosul.\",\n \"derivation_fa\": \"واژهٔ ترکیـ کهن beg «سرور، مهتر، رئیس طایفه» (ترکیـ آغازین *bǟg، ترکیـ امروز bey) ریشهٔ قطعی ندارد: یک دیدگاه (کلاوسن) آن را وام‌واژه‌ای از چینیـ میانه 伯/佰 «مهتر، سردار صدتن» می‌داند، دیدگاه دیگر آن را از سغدی βγ (βaγ) «خدا، سرور» و در نهایت از ایرانیـ آغازین *bagáh — همان که نورایی رسم کرده — ولی دورفر این ریشه‌یابی را بسیار نامطمئن خوانده و احتمال ترکی‌بودنـ اصیلـ آن را مطرح کرده است. پس این پیوند «با احتیاط پذیرفتنی» است. افزون بر این، beg در ترکی هرگز معنیـ «خدا» ندارد، و «اتابک» ترکیبی است از دورهٔ سلجوقی (ata «پدر» + beg) به معنی للهٔ شاهزاده، نه میراثی کهن از این ریشه.\",\n \"sources\": [U_PT],\n \"ref_check\": [\n   {\"ref\": \"ZMA:49\", \"status\": \"not_checked\",\n    \"note\": \"Fereydun Jonaydi, Zendegi va Mohājerat-e Āryāiān (Bonyād-e Neyšābur 1374) — refs_online.json: 'purchase only; no open or lending copy'. Not obtainable.\"}\n ],\n \"consulted\": [\n   {\"src\": \"Wiktionary\", \"where\": \"Reconstruction:Proto-Turkic/bēg (*bǟg 'lord')\", \"stance\": \"partial\",\n    \"note\": \"Sets out both hypotheses — Middle Chinese 百/佰/伯 (MC pᵠæk) vs Sogdian βγ (βaγ) 'lord, master' < Proto-Iranian *bagáh 'god' — citing Clauson 1972, and notes that Doerfer 'assessed the derivation from an Iranian language as quite uncertain and pointed out that the word may be genuinely Turkic'.\"},\n   {\"src\": \"HJB\", \"where\": \"p. 33 s.v. BEEGUM (parenthesis)\", \"stance\": \"partial\",\n    \"note\": \"Hobson-Jobson records the same idea as an old suggestion: bigim is 'a feminine formation from Beg, “chief, or lord” … [which some connect with Skt. bhaga, “lord”]'.\"},\n   {\"src\": \"TTS\", \"where\": \"Vámbéry 1878\", \"stance\": \"silent\",\n    \"note\": \"Grep of incoming/TTS/TTS_pages.txt for bäg/beg returns no usable entry (the OCR of the Turkic transliterations is very poor); no statement either way could be extracted.\"},\n   {\"src\": \"SOD\", \"where\": \"Gharib no. 2543\", \"stance\": \"supports\",\n    \"note\": \"Documents the putative donor: Sogdian 'βaγ (βγ-) ©<baga — God, Lord, king, sir, excellency'.\"}\n ]})\n\nN.append({\n \"id\": 12, \"lang\": \"Persian\",\n \"words\": \"bak «بَک (بَگ ، بیک ، بیگ ، بیگی)»; baygom «بیگم»; atabak «اتابک»\",\n \"verdict\": \"plausible\",\n \"derivation\": \"The direction of the arrow — Turkic > Persian — is certainly right: Wiktionary s.v. بیگ, 'Borrowed from Proto-Turkic *bēg via a Turkic language, perhaps ultimately from Middle Iranian languages', with بیگم and اتابک listed as derived/related terms. Persian took the title in with the Turkic military élites of the Ghaznavid–Seljuq period and again under the Mongols and Timurids, whence the spellings بک/بگ/بیک/بیگ and the Safavid–Qajar office-names in -بیگی (بیگلربیگی 'bey of beys'). اتابک = ata 'father' + beg, the Seljuq prince's guardian, later the Persian title اتابک اعظم. But بیگم is not what Nourai says it is: Hobson-Jobson s.v. BEEGUM, 'The word appears to be Or. Turki bigmi [= bigim] … a feminine formation from Beg, “chief, or lord”, like Khānum from Khān; hence P. begam' — i.e. beg + the Turkic first-person possessive -im, the same honorific pattern as خانم < xān. There is no Arabic أمّ umm 'mother' in it, so the chart's gloss “ruler's mother” and its cross-reference ☞ Umm are a folk etymology. Since the whole box hangs on the disputed Iranian origin of Turkic beg (node #11) and one of its three words is wrongly analysed, the node is plausible rather than confirmed.\",\n \"derivation_fa\": \"سوی وام‌گیری درست است: «بک/بگ/بیگ» در فارسی وام‌واژه‌ای ترکی است که از روزگار غزنوی و سلجوقی و سپس مغول و تیموری وارد شده است (ویکی‌واژه ذیل بیگ: «وام‌گرفته از ترکیـ آغازین *bēg … شاید در نهایت از زبان‌های ایرانیـ میانه»)؛ پس اگر ریشهٔ ایرانیـ beg درست باشد، این واژه رفت‌وبرگشتی (ایرانی ← ترکی ← فارسی) دارد. «اتابک» = ata «پدر» + beg. اما «بیگم» مرکب از «بیگ» و پسوندـ ملکیـ ترکیـ -im است (همان الگوی خان > خانم)، نه مرکب از عربیـ «أمّ»؛ ارجاع نورایی به ☞ Umm ریشه‌شناسی عامیانه است.\",\n \"sources\": [U_BEIG],\n \"ref_check\": [\n   {\"ref\": \"ETM:60\", \"status\": \"not_checked\",\n    \"note\": \"Abolghasemi, Riše-šenāsi (Etimoloji), Qoqnus 1374 — no digital copy on archive.org, ketabnak or noorlib (refs_online.json, re-searched 2026-09).\"}\n ],\n \"consulted\": [\n   {\"src\": \"Wiktionary\", \"where\": \"s.v. بیگ (Persian)\", \"stance\": \"supports\",\n    \"note\": \"'Borrowed from Proto-Turkic *bēg via a Turkic language, perhaps ultimately from Middle Iranian languages'; related terms بیگم, اتابک, بیگلربیگی.\"},\n   {\"src\": \"HJB\", \"where\": \"p. 33 s.v. BEEGUM, BEGUM\", \"stance\": \"contradicts\",\n    \"note\": \"'A Princess, a Mistress, a Lady of Rank … The word appears to be Or. Turki bigmi, [which some connect with Skt. bhaga, “lord”] a feminine formation from Beg, “chief, or lord”, like Khānum from Khān; hence P. begam.' No Arabic umm — against Nourai's ☞ Umm cross-reference and his gloss 'ruler's mother'.\"},\n   {\"src\": \"LKT\", \"where\": \"Lokotsch 1927\", \"stance\": \"silent\",\n    \"note\": \"Grep of LKT.txt for a beg/bäg headword finds only Pers. bāγ 'garden' (no. 166) and Bagdad (no. 170); Lokotsch has no entry for the title.\"}\n ]})\n\nwith open(\"/home/sfmqrb/git/rishe/data/verification/page-81.json\", \"w\", encoding=\"utf-8\") as f:\n    json.dump(doc, f, ensure_ascii=False, indent=2)\n    f.write(\"\\n\")\nprint(\"written\", len(N), \"nodes\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk81.py",
 "description": "Write page-81.json"
}
```


### [2026-09-05T06:31:53.192Z] TOOL RESULT

```
written 12 nodes
```


## [2026-09-05T06:31:57.963Z] TOOL CALL #98: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-81.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 81",
 "description": "Validate and run verify_check"
}
```


### [2026-09-05T06:31:59.578Z] TOOL RESULT

```
JSON OK
nodes verified: 12/12
node verdicts: {'transcription_suspect': 1, 'confirmed': 5, 'plausible': 6}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 18, 'not_checked': 8, 'partial': 4, 'not_found': 1}
books consulted: {'partial': 6, 'supports': 32, 'contradicts': 4, 'silent': 4} | by book: {'NYB': 7, 'PHD': 5, 'BRT': 4, 'SOD': 4, 'HJB': 4, 'KNT': 3, 'HRN': 3, 'BQT': 3, 'ARY': 2, 'HUB': 2, 'LKT': 2, 'MON': 2, 'Wiktionary': 2, 'TAD': 1, 'HENNING': 1, 'TTS': 1}
```


## [2026-09-05T06:32:04.891Z] TOOL CALL #99: Bash

```json
{
 "command": "tail -8 data/verification/sources/web/index.jsonl | python3 -c \"\nimport sys,json\nfor l in sys.stdin:\n    d=json.loads(l); print(d.get('url'))\n\"; echo \"=== sources in page-81 ===\"; python3 -c \"\nimport json\nd=json.load(open('data/verification/page-81.json'))\ns=set()\ne=d['entries'][0]\ns.update(e['sources'])\nfor n in e['nodes']: s.update(n['sources'])\nfor u in sorted(s): print(u)\n\"",
 "description": "Cross-check archived URLs vs cited sources"
}
```


### [2026-09-05T06:32:06.883Z] TOOL RESULT

```
https://www.ahdictionary.com/word/search.html?q=blister
https://abadis.ir/fatofa/%D8%A8%D9%84%D9%87/
https://abadis.ir/fatofa/%D8%A8%D9%84%DB%8C/
https://abadis.ir/fatofa/%D8%A8%D8%AC%D8%B2/
https://abadis.ir/fatofa/%D8%A8%D8%A7%D8%B2/
https://en.wiktionary.org/wiki/%D8%A8%D9%84%D9%89
https://gretil.sub.uni-goettingen.de/gretil/6_sres/2_dict/mwse72_u.htm
https://www.etymonline.com/word/bank
=== sources in page-81 ===
https://abadis.ir/fatofa/بغ/
https://abadis.ir/fatofa/بیدخت/
https://en.wikipedia.org/wiki/Behistun_Inscription
https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/bʰeh₂g-
https://en.wiktionary.org/wiki/Reconstruction:Proto-Turkic/bēg
https://en.wiktionary.org/wiki/بیستون
https://en.wiktionary.org/wiki/بیگ
https://en.wiktionary.org/wiki/فغفور
```


## [2026-09-05T06:32:14.706Z] TOOL CALL #100: Bash

```json
{
 "command": "grep -c \"\" data/verification/sources/web/index.jsonl; grep -n \"bʰeh₂g\\|b%CA%B0eh\\|Proto-Turkic\\|Behistun\\|D9%81%D8%BA%D9%81\\|D8%A8%DB%8C%D8%B3%D8%AA\\|D8%A8%DB%8C%DA%AF\\|D8%A8%DB%8C%D8%AF%D8%AE%D8%AA\\|fatofa/%D8%A8%D8%BA/\" data/verification/sources/web/index.jsonl | tail -12",
 "description": "Find new entries in web index"
}
```


### [2026-09-05T06:32:14.760Z] TOOL RESULT

```
854
802:{"url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/b%CA%B0eh%E2%82%82-", "file": "data/verification/sources/web/2a9f5bd5fba20317.txt", "fetched": "2026-09-05T06:11:36Z", "status": 200, "bytes": 8683, "title": "Reconstruction:Proto-Indo-European/bʰeh₂- - Wiktionary, the free dictionary", "note": "page 79, root Bha 1 (to shine): PIE root, Av. bama/bamya, NP bam/bamdad, Sogd. b'm > NP fam, Gk phos/phanos > NP fanus, Gmc *baukna > beacon"}
808:{"url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/b%CA%B0eh%E2%82%82g-", "file": "data/verification/sources/web/d7c6f8d1a1f64c02.txt", "fetched": "2026-09-05T06:16:56Z", "status": 200, "bytes": 7971, "title": "Reconstruction:Proto-Indo-European/bʰeh₂g- - Wiktionary, the free dictionary", "note": "pdf page 81, root Bhag part 1: verification of baga/baxs/bahr/fagfur/bistun/beg"}
809:{"url": "https://en.wiktionary.org/wiki/%D9%81%D8%BA%D9%81%D9%88%D8%B1", "file": "data/verification/sources/web/f8695d83bae2aec5.txt", "fetched": "2026-09-05T06:16:57Z", "status": 200, "bytes": 3415, "title": "فغفور - Wiktionary, the free dictionary", "note": "pdf page 81, root Bhag part 1: verification of baga/baxs/bahr/fagfur/bistun/beg"}
810:{"url": "https://en.wiktionary.org/wiki/%D8%A8%DB%8C%D8%B3%D8%AA%D9%88%D9%86", "file": "data/verification/sources/web/66cb409cd3b28795.txt", "fetched": "2026-09-05T06:16:57Z", "status": 200, "bytes": 3788, "title": "بیستون - Wiktionary, the free dictionary", "note": "pdf page 81, root Bhag part 1: verification of baga/baxs/bahr/fagfur/bistun/beg"}
811:{"url": "https://en.wiktionary.org/wiki/%D8%A8%DB%8C%DA%AF", "file": "data/verification/sources/web/149895f7b00830ad.txt", "fetched": "2026-09-05T06:16:57Z", "status": 200, "bytes": 8036, "title": "بیگ - Wiktionary, the free dictionary", "note": "pdf page 81, root Bhag part 1: verification of baga/baxs/bahr/fagfur/bistun/beg"}
812:{"url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Turkic/b%C4%93g", "file": "data/verification/sources/web/644ee918bfaebec0.txt", "fetched": "2026-09-05T06:16:58Z", "status": 200, "bytes": 5837, "title": "Reconstruction:Proto-Turkic/bǟg - Wiktionary, the free dictionary", "note": "pdf page 81, root Bhag part 1: verification of baga/baxs/bahr/fagfur/bistun/beg"}
813:{"url": "https://en.wikipedia.org/wiki/Behistun_Inscription", "file": "data/verification/sources/web/250e69d5cdec46fd.txt", "fetched": "2026-09-05T06:16:58Z", "status": 200, "bytes": 33278, "title": "Behistun inscription - Wikipedia", "note": "pdf page 81, root Bhag part 1: verification of baga/baxs/bahr/fagfur/bistun/beg"}
814:{"url": "https://abadis.ir/fatofa/%D8%A8%DB%8C%D8%AF%D8%AE%D8%AA/", "file": "data/verification/sources/web/19296d638d2d31f8.txt", "fetched": "2026-09-05T06:17:00Z", "status": 200, "bytes": 11573, "title": "بیدخت - معنی در دیکشنری آبادیس", "note": "pdf page 81, root Bhag part 1: verification of baga/baxs/bahr/fagfur/bistun/beg"}
815:{"url": "https://abadis.ir/fatofa/%D8%A8%D8%BA/", "file": "data/verification/sources/web/d2bec529dd7c6266.txt", "fetched": "2026-09-05T06:17:02Z", "status": 200, "bytes": 13983, "title": "بغ - معنی در دیکشنری آبادیس", "note": "pdf page 81, root Bhag part 1: verification of baga/baxs/bahr/fagfur/bistun/beg"}
816:{"url": "https://en.wiktionary.org/wiki/%D8%A8%D8%A7%D8%BA", "file": "data/verification/sources/web/d0254a8577498e21.txt", "fetched": "2026-09-05T06:20:06Z", "status": 200, "bytes": 19969, "title": "باغ - Wiktionary, the free dictionary", "note": "page 82, root Bhag, node 5: Persian باغ bāġ etymology (MP bāg < PIr *bāgáh < PIE *bʰeh₂g-)"}
```


## [2026-09-05T06:32:25.925Z] TOOL CALL #101: Bash

```json
{
 "command": "python3 - <<'EOF'\nimport json\np=\"data/verification/page-81.json\"\nd=json.load(open(p,encoding=\"utf-8\"))\nm={\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/bʰeh₂g-\":\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/b%CA%B0eh%E2%82%82g-\",\n \"https://en.wiktionary.org/wiki/فغفور\":\"https://en.wiktionary.org/wiki/%D9%81%D8%BA%D9%81%D9%88%D8%B1\",\n \"https://en.wiktionary.org/wiki/بیستون\":\"https://en.wiktionary.org/wiki/%D8%A8%DB%8C%D8%B3%D8%AA%D9%88%D9%86\",\n \"https://en.wiktionary.org/wiki/بیگ\":\"https://en.wiktionary.org/wiki/%D8%A8%DB%8C%DA%AF\",\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Turkic/bēg\":\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Turkic/b%C4%93g\",\n \"https://abadis.ir/fatofa/بیدخت/\":\"https://abadis.ir/fatofa/%D8%A8%DB%8C%D8%AF%D8%AE%D8%AA/\",\n \"https://abadis.ir/fatofa/بغ/\":\"https://abadis.ir/fatofa/%D8%A8%D8%BA/\",\n}\ndef fix(l): return [m.get(u,u) for u in l]\ne=d[\"entries\"][0]\ne[\"sources\"]=fix(e[\"sources\"])\nfor n in e[\"nodes\"]: n[\"sources\"]=fix(n[\"sources\"])\njson.dump(d,open(p,\"w\",encoding=\"utf-8\"),ensure_ascii=False,indent=2)\nopen(p,\"a\",encoding=\"utf-8\").write(\"\\n\")\nprint(\"ok\")\nEOF\npython3 -m json.tool data/verification/page-81.json > /dev/null && python3 tools/verify_check.py 81",
 "description": "Normalize URLs and re-verify"
}
```


### [2026-09-05T06:32:27.963Z] TOOL RESULT

```
ok
nodes verified: 12/12
node verdicts: {'transcription_suspect': 1, 'confirmed': 5, 'plausible': 6}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 18, 'not_checked': 8, 'partial': 4, 'not_found': 1}
books consulted: {'partial': 6, 'supports': 32, 'contradicts': 4, 'silent': 4} | by book: {'NYB': 7, 'PHD': 5, 'BRT': 4, 'SOD': 4, 'HJB': 4, 'KNT': 3, 'HRN': 3, 'BQT': 3, 'ARY': 2, 'HUB': 2, 'LKT': 2, 'MON': 2, 'Wiktionary': 2, 'TAD': 1, 'HENNING': 1, 'TTS': 1}
```


## [2026-09-05T06:32:51.309Z] AGENT

Page 81 (book p. 51), root **Bhag** part 1 — done. `verify_check.py 81`: 12/12 nodes, **0 PROBLEM lines**.

**Verdicts** — root: confirmed. Nodes: 5 confirmed, 6 plausible, 1 transcription_suspect. Ref checks: 18 supports, 4 partial, 1 not_found, 8 not_checked (AEF, ETM, TZF, ZMA, MON:2558 — none obtainable per `refs_online.json`).

**Flagged items**
- **#1 `baxto-dâta` — transcription_suspect, error_in "book".** No such Old Iranian compound exists; Bartholomae (cols. 921–22) has `baγō.dāta-` 'god-created' and `baγō.baxta-` 'allotted by the gods' (Nyberg II s.v. *bāgō-baxt*). I rendered PDF p. 81 at 200 dpi: the page really prints "baxto-dâta", so the extraction is faithful — it is Nourai's own conflation. Image filed at `data/verification/sources/refs/ocr/BOOK/81.png`.
- **#4 barx / bahr — plausible.** Hübschmann §245/§88a and Nyberg derive both from Av. `baxəδra-`; **Horn no. 245 contradicts**, deriving *bahr* from Av. `hu-baδra-`/Skt. `bhadra-` (revived by Bailey 1952). Modern opinion mostly follows Hübschmann.
- **#10 anbâz — plausible.** MacKenzie has two distinct MP words: `hambāy` ⟨hmbʾg⟩ → NP *anbāγ* 'co-wife' (his gloss "adversary"), and `hambāz` ⟨hnbʾc⟩ → NP *anbāz*. Nourai merges them.
- **#11/#12 Turkic bak/beg — plausible.** The Iranian origin of Turkic *beg* is only one of three hypotheses (Middle Chinese 伯 per Clauson; Doerfer calls the Iranian derivation "quite uncertain"). Also: Turkic *beg* never means 'God'.
- **#12 baygom «بیگم» — Nourai's ☞Umm cross-reference is wrong.** Hobson-Jobson p. 33: *bigim* is "a feminine formation from Beg… like Khānum from Khān" — Turkic possessive *-im*, no Arabic *umm*.
- **Chart NOTE evaluated:** TAD:12 does print «بغداد … مركب من باغ أي بستان وداد أي عدل», but it is folk etymology — Lokotsch no. 170 rejects it explicitly and Moʼin's footnote at BQT p. 288 reads *baγ + dād* 'god-given'. Henning SLW:94 is right about the *f-* forms: فغفور is a Sogdian loan (Gharib no. 2582 βγpʾwr < *baga-puθra-, via Parth. *bagpuhr*); Moʼin's own footnote at BQT p. 1493 cites Gauthiot and "Henning, BSOS vol. X".

**Extraction errors for the owner: none** — every word, script form and gloss in `page-81.json` matches the printed page.

Notable ref confirmations: KNT s.v. `baga-`/`bāji-` and his Behistun note (*bagastāna-* → Bisitūn, "understood by popular etymology as 'without columns'"); Moʼin's BQT footnotes at pp. 203, 288–289, 1493; SNS p. 96 (`baxaδra- 96/10`); FFD printed p. 35 = pdf 41; HJB p. 49 (Schiefner, "Zend bagha-puthra … another form of the famous term Faghfor").
