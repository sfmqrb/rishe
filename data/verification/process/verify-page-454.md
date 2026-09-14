# Verification process log — verify-page-454


## [2026-09-14T01:56:21.399Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 454 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-454.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-454.json. Write /home/sfmqrb/git/rishe/data/verification/page-454.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 454` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-14T01:56:22.665Z] AGENT

I'll start by reading the instructions.


## [2026-09-14T01:56:23.452Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-14T01:56:23.467Z] TOOL RESULT

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
226	Several agents run at the same time and share the scratchpad and `/tmp`, so every temporary
227	file you create must carry your page number in its name (e.g. `e0-363.json`, `pg363.png`,
228	`draft-363.json`), never a bare `e0.json` or `entry.json` — another agent will overwrite it.
229	
230	```json
231	{
232	  "pdf_page": 126,
233	  "book_page": 96,
234	  "verified_by": "claude-opus-5",
235	  "verified_on": "2026-09-05",
236	  "entries": [
237	    {
238	      "entry": 0,
239	      "root": "Dheigh, Dhigha",
240	      "verdict": "confirmed",
241	      "modern_form": "PIE *dʰeyǵʰ- 'to knead, form (clay)'",
242	      "note": "Pokorny 244 dheiĝh-; AHD dheigh-. Root, language label and gloss all correct.",
243	      "note_fa": "ریشهٔ هندواروپایی آغازین *dʰeyǵʰ- «خمیر کردن، شکل دادن (گِل)» … ادعای نورایی درست است.",
244	      "sources": ["https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/dʰeyǵʰ-"],
245	      "ref_check": [{"ref": "POK:244", "status": "supports", "note": "…"}],
246	      "consulted": [{"src": "WLD", "where": "Bd. I 833", "stance": "supports", "note": "…"}],
247	      "nodes": [
248	        {
249	          "id": 6,
250	          "lang": "Avestan",
251	          "words": "pairi-daeza",
252	          "verdict": "confirmed",
253	          "derivation": "Av. pairi-daēza- 'walled enclosure' = pairi 'around' (PIE *per-) + daēza- 'wall' …",
254	          "derivation_fa": "«پردیس» … اوستایی pairi-daēza- «دیوارکشیده، باغِ محصور» از pairi «پیرامون» و daēza- «دیوار» …",
255	          "sources": ["https://en.wiktionary.org/wiki/pairidaēza"],
256	          "ref_check": [{"ref": "POK:244", "status": "supports", "note": "…"}],
257	          "consulted": [{"src": "BRT", "where": "col. 866", "stance": "supports", "note": "…"}]
258	        }
259	      ]
260	    }
261	  ]
262	}
263	```
264	
265	Rules:
266	- Include EVERY node of every non-redirect entry on the page (even empty-word pass-through
267	  nodes like `[Latin] refs=None |` — give them a one-line derivation and a verdict).
268	- `words` = the transliterations of the node joined by "; " (copy from the chart).
269	- `derivation` must be specific: forms, sound changes, dates/eras, texts or peoples,
270	  semantic shifts. 1–5 sentences. No hand-waving like "derived regularly".
271	- Keep `note` on the entry for root-level comments and for anything cross-cutting.
272	- If a node lists several words, cover each word; if they differ in verdict, use the worst
273	  verdict for the node and explain per word in `derivation`.
274	- Where the chart's own NOTE already records a dispute, evaluate it: say which side modern
275	  scholarship takes.
276	- Every node has `ref_check` (array, may contain a single `not_checked` item) AND `consulted`
277	  (array) AND `derivation_fa` (string); every entry has `note_fa`.
278	- Valid JSON only. Test it with `python3 -m json.tool` before finishing, then run
279	  `python3 /home/sfmqrb/git/rishe/tools/verify_check.py <pdf page>` — it must show 0 PROBLEM lines.
280	- When done, reply with a SHORT summary (≤ 15 lines): counts of verdicts per page, and a
281	  bullet per `disputed` / `transcription_suspect` item (root, word, one-line reason), plus
282	  any extraction errors (JSON differs from the printed page) the owner must fix.
283	  Do not paste the JSON back into your reply.
284	
```


## [2026-09-14T01:56:23.956Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-454.txt"
}
```


### [2026-09-14T01:56:23.985Z] TOOL RESULT

```
1	=== PDF page 454 (book page 424) ===
2	--- entry 0 ---
3	ROOT Skep -> redirect to Sek
4	--- entry 1 ---
5	ROOT [Indo-European] Sker 1 : to turn, bend  (refs POK:935)
6	#1 (parent #0) [Indo-European] refs=POK:935; IEC:535 | Kor-ôna : bent
7	  #2 (parent #1) [Avestan / Old Persian] refs=SYN:857; BRT:46,451 | Karana : end, edge
8	    #3 (parent #2) [Pahlavi] refs=BQT:1611,1699; HRN:189 | kanâr : edge, side
9	      #4 (parent #3) [Persian] refs=BRT:451; SYN:857; IEC:535 | karân «کران» : edge | extra: کرانه، کنار، کناره
10	    #5 (parent #2) [Avestan / Old Persian] refs=BRT:46 | a-karana : endless ☞Ne 1
11	  #6 (parent #1) [Greek] refs=IEC:535; POK:935 | koeônos : curved
12	    #7 (parent #6) [English] refs=AHD | crown, corona
13	#8 (parent #0) [Indo-European] refs=POK:935 | Kur-wo : bent, curly
14	  #9 (parent #8) [Old Persian] refs=FAF:513; KNT:180 | Kŭru : "curly hair", name of the founder of Persian empire who was born in 559 BC ; Kŭruš, Kŭrauš, Kŭ-raš, Kŭ-ra-aš
15	    #10 (parent #9) [Persian] refs=BQT; KNT:180 | Kŭrosh «کورش، کوروش» : "sun", a male name
16	    #11 (parent #9) [Greek] refs=FSD:644 | Kuros
17	      #12 (parent #11) [Persian] refs=FAF:513 |  | extra: کوروس، سیروس
18	      #13 (parent #11) [English] refs=FSD:644 | Cyrus
19	  #14 (parent #8) [Latin] refs=POK:935 | curvus : bent ; crista : crest ; crispus : curly
20	    #15 (parent #14) [English] refs=AHD | curve, curb, curvature ; crest ; crisp, crepe
21	  #16 (parent #8) [Greek] refs=POK:935 | krikos : ring
22	    #17 (parent #16) [Latin] refs=POK:935 | circus : circle
23	      #18 (parent #17) [English] refs=AHD | circus, circle, search
24	  #19 (parent #8) [Germanic] refs=POK:935 | skrink : to shrivel up ; hringaz : circle ; hrugjaz : edge
25	    #20 (parent #19) [English] refs=AHD | shrink ; ring, ranch, range, rink, arrange, derange, ribbon ; ridge
26	--- entry 2 ---
27	ROOT Sker 2 -> redirect to Sek
28	
```


## [2026-09-14T01:56:26.285Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-454.json | head -200",
 "description": "Read source JSON for page 454"
}
```


### [2026-09-14T01:56:26.330Z] TOOL RESULT

```
{
  "pdf_page": 454,
  "book_page": 424,
  "entries": [
    {
      "root": {
        "name": "Skep",
        "redirect": "Sek"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Sker 1",
        "lang": "Indo-European",
        "refs": "POK:935",
        "gloss": "to turn, bend"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Indo-European",
          "refs": "POK:935; IEC:535",
          "words": [
            {
              "translit": "Kor-ôna",
              "gloss": "bent",
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
          "lang": "Avestan / Old Persian",
          "refs": "SYN:857; BRT:46,451",
          "words": [
            {
              "translit": "Karana",
              "gloss": "end, edge",
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Pahlavi",
          "refs": "BQT:1611,1699; HRN:189",
          "words": [
            {
              "translit": "kanâr",
              "gloss": "edge, side",
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
          "refs": "BRT:451; SYN:857; IEC:535",
          "words": [
            {
              "translit": "karân",
              "gloss": "edge",
              "script": "کران"
            }
          ],
          "script_extra": "کرانه، کنار، کناره",
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 2,
          "lang": "Avestan / Old Persian",
          "refs": "BRT:46",
          "words": [
            {
              "translit": "a-karana",
              "gloss": "endless",
              "script": null,
              "see": ["Ne 1"]
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 1,
          "lang": "Greek",
          "refs": "IEC:535; POK:935",
          "words": [
            {
              "translit": "koeônos",
              "gloss": "curved",
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {
              "translit": "crown, corona",
              "gloss": null,
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 0,
          "lang": "Indo-European",
          "refs": "POK:935",
          "words": [
            {
              "translit": "Kur-wo",
              "gloss": "bent, curly",
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "Old Persian",
          "refs": "FAF:513; KNT:180",
          "words": [
            {
              "translit": "Kŭru",
              "gloss": "\"curly hair\", name of the founder of Persian empire who was born in 559 BC",
              "script": null
            },
            {
              "translit": "Kŭruš, Kŭrauš, Kŭ-raš, Kŭ-ra-aš",
              "gloss": null,
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
          "refs": "BQT; KNT:180",
          "words": [
            {
              "translit": "Kŭrosh",
              "gloss": "\"sun\", a male name",
              "script": "کورش، کوروش"
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 9,
          "lang": "Greek",
          "refs": "FSD:644",
          "words": [
            {
              "translit": "Kuros",
              "gloss": null,
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
```


## [2026-09-14T01:56:27.109Z] TOOL CALL #4: Bash

```json
{
 "command": "sed -n 1,120p data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-14T01:56:27.266Z] TOOL RESULT

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
```


## [2026-09-14T01:56:31.403Z] TOOL CALL #5: Bash

```json
{
 "command": "sed -n 200,400p data/extracted/batch/page-454.json; echo ===; sed -n 120,200p data/verification/sources/SOURCE_MATRIX.md",
 "description": "Rest of source JSON and matrix"
}
```


### [2026-09-14T01:56:31.463Z] TOOL RESULT

```
Exit code 1
          "quote": null
        },
        {
          "id": 12,
          "parent": 11,
          "lang": "Persian",
          "refs": "FAF:513",
          "words": [],
          "script_extra": "کوروس، سیروس",
          "note": null,
          "quote": null
        },
        {
          "id": 13,
          "parent": 11,
          "lang": "English",
          "refs": "FSD:644",
          "words": [
            {
              "translit": "Cyrus",
              "gloss": null,
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 14,
          "parent": 8,
          "lang": "Latin",
          "refs": "POK:935",
          "words": [
            {
              "translit": "curvus",
              "gloss": "bent",
              "script": null
            },
            {
              "translit": "crista",
              "gloss": "crest",
              "script": null
            },
            {
              "translit": "crispus",
              "gloss": "curly",
              "script": null
            }
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
            {
              "translit": "curve, curb, curvature",
              "gloss": null,
              "script": null
            },
            {
              "translit": "crest",
              "gloss": null,
              "script": null
            },
            {
              "translit": "crisp, crepe",
              "gloss": null,
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 16,
          "parent": 8,
          "lang": "Greek",
          "refs": "POK:935",
          "words": [
            {
              "translit": "krikos",
              "gloss": "ring",
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 17,
          "parent": 16,
          "lang": "Latin",
          "refs": "POK:935",
          "words": [
            {
              "translit": "circus",
              "gloss": "circle",
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 18,
          "parent": 17,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {
              "translit": "circus, circle, search",
              "gloss": null,
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 19,
          "parent": 8,
          "lang": "Germanic",
          "refs": "POK:935",
          "words": [
            {
              "translit": "skrink",
              "gloss": "to shrivel up",
              "script": null
            },
            {
              "translit": "hringaz",
              "gloss": "circle",
              "script": null
            },
            {
              "translit": "hrugjaz",
              "gloss": "edge",
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 20,
          "parent": 19,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {
              "translit": "shrink",
              "gloss": null,
              "script": null
            },
            {
              "translit": "ring, ranch, range, rink, arrange, derange, ribbon",
              "gloss": null,
              "script": null
            },
            {
              "translit": "ridge",
              "gloss": null,
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Sker 2",
        "redirect": "Sek"
      },
      "nodes": []
    }
  ]
}
(eval):1: == not found
```


## [2026-09-14T01:56:32.768Z] TOOL CALL #6: Bash

```json
{
 "command": "ls data/verification/ | head -30; echo ===; python3 -c \"\nimport json\nd=json.load(open('data/verification/page-385.json'))\nprint(json.dumps(d['entries'][0],ensure_ascii=False,indent=1)[:3000])\n\"",
 "description": "Look at a prior verification file"
}
```


### [2026-09-14T01:56:33.848Z] TOOL RESULT

```
Exit code 1
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
(eval):1: == not found
```


## [2026-09-14T01:56:38.246Z] TOOL CALL #7: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/page-385.json'))\ne=d['entries'][0]\nprint(json.dumps({k:v for k,v in e.items() if k!='nodes'},ensure_ascii=False,indent=1))\nprint(json.dumps(e['nodes'][0],ensure_ascii=False,indent=1))\n\"",
 "description": "Prior verification file format"
}
```


### [2026-09-14T01:56:39.525Z] TOOL RESULT

```
{
 "entry": 0,
 "root": "Peg",
 "verdict": "plausible",
 "modern_form": "PIE *peg- / *pōg-, *pōk-s- 'armpit, hip, loin, side' (Pokorny 792); Watkins/AHD lists the same root as *peg- 'breast'",
 "note": "Pokorny 792 prints the headword as '(peg-:) pog-: pōg-, pōk-s-' and glosses it 'Achsel, Hufte, Lende, Seite' (armpit, hip, loin, side) — the full-grade *peg- is only a bracketed, inferred variant. Nourai's headword 'Peg' with the gloss 'breast' is copied verbatim from the AHD (Watkins) appendix, which prints 'peg-. Breast.' The 'breast' sense in fact rests only on Latin pectus and Tocharian A pässäṃ / B pāścane 'the two breasts'; Sanskrit pakṣa- and Latvian paksis point to 'side, flank'. Modern scholarship (de Vaan via Wiktionary) further doubts that Lat. pectus and Skt. pakṣa- belong together at all. Root is real and the language label is right; the gloss is a one-sided simplification.",
 "note_fa": "ریشهٔ هندواروپایی آغازین که نورایی آن را Peg با معنای «سینه» آورده، در فرهنگ پوکورنی (ص ۷۹۲) با سرواژهٔ «(peg-:) pog-: pōg-, pōk-s-» و معنای «زیربغل، ران، پهلو» ثبت شده است؛ صورت *peg- تنها گونه‌ای بازسازی‌شده و درون‌کمانک است. معنای «سینه» را نورایی از پیوست ریشه‌های هندواروپایی فرهنگ AHD (واتکینز) گرفته که همان‌جا «Breast» نوشته است، ولی این معنا فقط بر پایهٔ pectus لاتین و pāścane تخاری است، حال آنکه pakṣa- سنسکریت و paksis لتونیایی بر معنای «پهلو، سو» دلالت دارند. افزون بر این، پژوهش امروزی (دِ ڤان، به نقل ویکی‌واژه) در پیوند pectus لاتین با pakṣa- سنسکریت تردید می‌کند. پس: ریشه واقعی است و برچسب زبانی درست، اما معنای داده‌شده یک‌سویه و ساده‌سازانه است — ادعای نورایی با احتیاط پذیرفتنی است.",
 "sources": [
  "https://en.wiktionary.org/wiki/%E0%A4%AA%E0%A4%95%E0%A5%8D%E0%A4%B7",
  "https://en.wiktionary.org/wiki/pectus"
 ],
 "ref_check": [
  {
   "ref": "POK:792",
   "status": "partial",
   "note": "Pokorny IEW p.792 (local POK_03.txt, form-feed leaf 25) reads: '(peg-:) pog-: pōg-, pŏk-s- \"Achsel, Hufte, Lende, Seite\". Ai. pákṣa- m. \"Schulter, Flugel\" und \"Seitenpfosten\", pákṣas- n. \"Seite\"; lat. pectus \"Brust\"; lett. paksis \"Hausecke\"; toch. A pässäṃ, B päścane \"die beiden Bruste\" ... WP. II 3 f., WH. II 270.' The page number is exact; the gloss is not 'breast'."
  }
 ],
 "consulted": [
  {
   "src": "AHD",
   "where": "Watkins 1985, s.v. peg-",
   "stance": "supports",
   "note": "'peg-. Breast. 1. Suffixed variant form *pek-tos- in Latin pectus, breast: PECTORAL; EXPECTORATE, PARAPET. 2. Possibly suffixed variant form *pek-so- in Sanskrit paksah, wing: PUNKA. [Pok. (peg-), pog- 792.]' — this is verbatim Nourai's chart (grep '^peg-' AHD_watkins1985.txt line 820)."
  },
  {
   "src": "WLD",
   "where": "Walde-Pokorny II 3-4 (WLD_Bd2_pages.txt leaf 8)",
   "stance": "partial",
   "note": "Entry headed 'pag-' (their spelling) with 'ai. pajasyá- n. Bauchgegend, Weichen, russ. pachu \"Leistengegend\", pacha \"Achselhohle\" ... ein io-St. *pagio- in cech. paze \"Arm\"' — again 'flank/armpit', no 'breast'."
  },
  {
   "src": "IEC",
   "where": "Mann, alphabetical",
   "stance": "silent",
   "note": "grep of IEC.txt for 'peg-', 'pokso-', 'pektos' returns no headword for this root."
  }
 ]
}
{
 "id": 1,
 "lang": "Sanskrit",
 "words": "pakša",
 "verdict": "plausible",
 "derivation": "Sanskrit पक्ष (pakṣá-) m. is real and old (RV), but its meanings are 'wing, feather; side, flank; half (of a month); party, faction' — not 'breast'. Monier-Williams and Wiktionary give no 'breast' sense; the chart's 'breast' is imported from Nourai's root gloss. Formally pakṣa- goes back to Proto-Indo-Iranian *pakšás 'side, flank' < PIE *peg-/*pok-s-, with the regular Indo-Aryan treatment of *-ks- > -kṣ-; the Iranian cognate is Ossetic fæxs 'side'. So the arrow root -> Sanskrit is sound; only the gloss 'breast' is wrong.",
 "derivation_fa": "واژهٔ سنسکریت pakṣá- «بال، پر؛ پهلو، سو؛ نیمه (ماه)؛ دسته» از ریگ‌ودا به‌بعد گواهی شده است، اما معنای «سینه» برای آن ثبت نشده و نورایی آن را از معنای ریشه به این گره تسری داده است. از دید آوایی pakṣá- بازماندهٔ هندوایرانی آغازین *pakšás «پهلو، سو» است (خوشهٔ *-ks- در هندوآریایی به -kṣ- بدل می‌شود) و هم‌ریشهٔ آن در ایرانی، fæxs آسی به معنی «پهلو» است. بنابراین پیکان «ریشه ← سنسکریت» درست است و تنها معنای «سینه» نادرست است.",
 "sources": [
  "https://en.wiktionary.org/wiki/%E0%A4%AA%E0%A4%95%E0%A5%8D%E0%A4%B7"
 ],
 "ref_check": [
  {
   "ref": "AHD",
   "status": "partial",
   "note": "Watkins 1985 s.v. peg-: '2. Possibly suffixed variant form *pek-so- in Sanskrit paksah, wing: PUNKA.' Watkins glosses the Sanskrit word 'wing' only, and marks the connection 'possibly'."
  }
 ],
 "consulted": [
  {
   "src": "POK",
   "where": "IEW 792 (POK_03 leaf 25)",
   "stance": "partial",
   "note": "'Ai. pákṣa- m. \"Schulter, Flugel\" und \"Seitenpfosten\", pákṣas- n. \"Seite\"' — shoulder/wing/side, not breast."
  },
  {
   "src": "KLN",
   "where": "1966 ed. p.1272 s.v. punka (leaf 678)",
   "stance": "partial",
   "note": "'fr. OI. pakṣaḥ, pákṣas, \"wing, side, half\", which is possibly cogn. with Lett. paksis, \"corner of a house\", Russ. pach, \"flank\".' Klein too has no 'breast'."
  },
  {
   "src": "WLD",
   "where": "WP II 3-4",
   "stance": "partial",
   "note": "lists ai. pajasyá- 'Bauchgegend, Weichen' beside the pakṣa- family; gloss 'flank'."
  }
 ]
}
```


## [2026-09-14T01:56:40.871Z] TOOL CALL #8: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','IEC','SYN','BRT','KNT','FAF','FSD','AHD','BQT','HRN','MON','ARY','WLD','KLN','SKT','PHD','NYB','HUB']:\n    v=d.get(k)\n    print(k, json.dumps(v,ensure_ascii=False)[:400])\n    print()\n\"",
 "description": "Refs online info"
}
```


### [2026-09-14T01:56:42.004Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 

IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I

SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in

BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sou

KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "loca

FAF {"title": "A. Daneshgar, Farhang-e A'lam-e Farsi, Hafez Novin 1370/1991", "kind": "none", "url": null, "lookup_hint": "Not found.", "local_file": null, "page_offset": null, "covers_etymology": false, "notes": "none online. || RE-SEARCH 2026-09: nothing digitised on any permitted platform (archive.org, Google Books, Persian libraries/ebook stores). Check opac.nlai.ir manually / buy second-hand."}

FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-D

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a

ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 

WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-

SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158

PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac

NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verific

HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1
```


## [2026-09-14T01:57:23.190Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls | head -60; python3 -c \"\nimport json\nd=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'))\nfor k in ['POK','IEC','SYN','BRT','KNT','FSD','AHD','HRN']:\n    v=d[k]; print(k, v.get('page_offset'), '|', v.get('lookup_hint'))\n\"",
 "description": "List refs dir and page offsets"
}
```


### [2026-09-14T01:57:24.363Z] TOOL RESULT

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
POK POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-dictionary/ (entry pages with page numbers) and StarLing https://starlingdb.org/cgi-bin/query.cgi?basename=\data\ie\pokorny&root=config
IEC TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root.
SYN leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the concept heading (all caps English word) or a printed page number line.
BRT Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Nourai's BRT numbers are Bartholomae's COLUMN numbers. Headwords are Avestan/OP in transliteration in bold at line start; OCR of the special transliteration is noisy - grep on a distinctive Latin gloss or the German meaning in quotes. Column numbers appear as standalone numbers at leaf tops.
KNT leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Lexicon (Part III, pp. 164 ff.) headwords are transliterated OP words at line start followed by part of speech, e.g. grep -n '^apadana-' ; section refs like '$147'. Nourai's page numbers should fall in 164-215 for lexicon citations.
FSD vol1: leaf = p + 41..56 (drifts; e.g. leaf 87 = p.46, leaf 612 = p.556); vol3: leaf = p - 1466 (e.g. leaf 215 = p.1681); vol4: leaf = p - 2144..2148 (e.g. leaf 229 = p.2373); vol2 offset not reliably detected (pages ~ 700-1640) - grep the headword. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Headword in bold at line start with pronunciation; etymology in brackets at entry end '[< L. ...]'. Very large OCR (16 MB per vol); grep -n '^word' vol file.
AHD 1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page. | Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru-' ; entries list English derivatives in caps. Restricted 1970s AHD scans on IA (lending only, djvu.txt returns 401): americanheritage0000dict (July 1977 printing, 970 leaves - probably the New College Edition), bwb_P9-BHZ-437 (1974), americanheritage00nyde (1970), bwb_W9-CSW-086 (1969, 1610 leaves = original 1969 ed.).
HRN leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.
```


## [2026-09-14T01:57:27.739Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Page(s): 93[3-9]\" POK_full.txt | head -20",
 "description": "Find Pokorny entries near p.935"
}
```


### [2026-09-14T01:57:27.819Z] TOOL RESULT

```
75730:Page(s): 933 
75820:Page(s): 933-935 
76019:Page(s): 935-938 
76550:Page(s): 938-947
```


## [2026-09-14T01:57:30.065Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '75990,76030p' POK_full.txt",
 "description": "Pokorny entry header at 935"
}
```


### [2026-09-14T01:57:30.122Z] TOOL RESULT

```
stalk from Schlingflanzen, tendril '. 

C. ^/-basis (s)kreu-: 



compare above S. 935 to gr. Kopoovoq; acymr. crunn, mcymr. crwnn, fern, cronn, 
(common Celtic -ns-, -nt- > -nn-), abret. cron^ round ', Middle Irish cruind^ round ', zur 
basic form *krundi, compare gr. KOKpuv-5aKoi KuAAoi; 

sloven, krulitr mutilate, rings behacken', serb. /rm^5i/"lame, crippled ', poln. krolic {^or 
km lid} " furrow '; 

compare also Old Indie karu-kara-m. "whirl of Halses and RiJckgrates'; 

Ar-extension (s)kreu-k-: 0\6 Indie /rm/7C5//(Dhatup.) 'krijmmt sich'; Latin CAWA-'Marterholz' 
(originally "round picket, pole'); Irish cruachi. "heap, barn, haystack, hill', gall. *krouka^ 
acme, apex ', worfrom *krdkka, kruk(k)a^s. (v. Wartburg FEW. 2, 1367), cymr. crugvn. 
"cippus, tumulus', corn, abret. cruc^\\\\\\ nbret. crug, abrit.-Latin Penno-cruciumPH.; Old 
Icelandic /7/y(g^/'"backbone, spine'. Old English hrycg. Old Saxon hruggi. Old High German 
(h)rukki 'back\ Old Icelandic hrugat "heap', hraukr' heap', Old English /7/'eac"Kornhaufe', 
Dutch rook6s., changing through ablaut Old English cornhryccei. "Korndieme', engl. rick 
ds.; Lithuanian/r/7a^A/e"Meerschnecke', kriaukias^ rib '; Latvian krukneV writhed, crooked, 
humped sit'; 

A ^extension seems /r/'J/-"Korperwolbung' above S. 624. 

References: WP. II 568 ff., WH. I 220 f., 233 f., 279 f., 317 f., 293, 296 f., Trautmann 140 
f.,267f.. Loth RC. 43, 416 f. 
Page(s): 935-938 

Root / lemma: (s)ker-4, (s)kera-, (s)kre- 
Meaning: to cut 

Material: I. A. Old Indie ava-, apa-skara-^ excrement (Ausscheidung)'; krnati, krnoti^ 
injures, slays ' (lex.), ^/A/?/7a-'ausgeschnitten, eingeritzt', s5/77i//A/?/75-"durchbohrt'; Old 
Indie carman-, Avestan caraman-^ieW, fur, skin'; presumably Old Indie /ri//- (unbel.) "ein 
Webergerat' (: russ. dial. cen/B "sickle', Lithuanian A/?i//s"axe' (?); 

Armenian k'orem^\ scratch', /r'e/ie/T? "scratch, scrape ';
```


## [2026-09-14T01:57:34.915Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^Root / lemma: (s)ker\" POK_full.txt | head; echo \"---\"; sed -n '75824,75900p' POK_full.txt",
 "description": "Pokorny sker lemmas"
}
```


### [2026-09-14T01:57:35.032Z] TOOL RESULT

```
75544:Root / lemma: (s)kert)(h)-, (s)kreb(h)-, nasalized (s)kremb- 
75683:Root / lemma: (s)ker-1 
75732:Root / lemma: (s)ker-2, skera- : skre- 
75822:Root / lemma: (s)ker-3 
76021:Root / lemma: (s)ker-4, (s)kera-, (s)kre- 
76554:Root / lemma: (s)ker-5 
76561:Root / lemma: (s)kert-s- 
---
Meaning: to turn, bend 

Note: (see also 1. (s)ker-^ shrivel, shrink due to excess dryness, wrinkle up ' and 2. (s)ker- 

'spring') 

Material: A. Avestan skarana- ' round ', skarayal-ra&a- EN., actually "the den chariot 

kreisen allows'; 

alb. perhaps kerrus, kumis^beuge, bend'; 

gr. KupT6(; "crooked' (old u- coloring, compare russ. kortocki, as well as Church Slavic 
sz>-AAbc///"pull together' etc.); Kopwvoc; " writhed, crooked, humped '; Kopcbvn "allerlei 
GekriJmmtes, Gebogenes etc' (Latin loanword corona), perhaps as *kord[u]-no-s zw u- 
basis *{s)kereu-\ 

Latin ci/Ai/i/s "crooked, writhed, crooked, humped, arched' (forms -uo-)\ cort/ha'round 
vessel, kettle; the Dreifuft Apollos with dem kettle darauf; Himmelswolbung'; from a 
participle *kr-to-' twiddled, twisted, rotated, revved, revolved ' derived; 

Middle Irish cor, Akk. PI. curu'Kre\se', cymr. cor-wynt, bret. cor- i/e/?/" turbo'; 

russ. k6rtockiP\. f. "crouching, cowering position ', kir. kortaty sa^sich durchhelfen, 
rackern' (if "* crook oneself '? compare gr. Kuprot;). 

a) guttural extensions: 

ker-k-, besides A/ir-Ar- (from redupl. *ki-kro-) and {s)krek-: 

Doubtful Old Indie krkafa-n. " neck joint ', krka-m. (uncovered) "larynx'; 

Maybe alb. gryke " throat ' (common alb. k- >p'- common gutturals Celtic Baltic). 

gr. KipKoq m. "ring' (KipKow ' tie with a ring'), usually (from Homer) KpiKoq (in addition 
K\po6q, Kp\oo6q, Doric Kpi^oq m. Poll. Hes. "Krampfader' as "vortretende Aderringe'); Latin 
c/rcus "Zirkellinie, circle in the Astronomie; esp. the (round) racecourse ', preposition 



c//r^/77 "rihgsumner etc', circa (after supra, extra); the Umbrian name of a month kurglasiu 
as " circulario '?; 

(s)krek-\K\ Low German schrege, schrage. Middle High German schrsege^ slantwise ', 
Middle Low German Middle High German schrage^ kreuzweisestehende Holzfufle '; kir. 
korkusm. " nape ', korkosiP\. " underarms, armpits ', Czech krk^ neck ' etc. (compare 
above Old Indie krka-)\ Church Slavic sb-A/Tbd///"pull together', russ. korcu, -itb ds., " face 
cut ', korca, /ro/r "cramp', o/ro/ra "crooked part of sledge', Czech dial. Ar/ros/ra "knag in 
wood', Ar/ri/a "wrinkle, crease ' etc.; also wruss. /ro/r/7 "fist' etc. from *khrk-so-l\ 

nasalized ^5y>Are/7Ar-; presumably russ. krjakatb " take another turn ', krjac^ wood toggle ', 
krjacitb " fasten '; Church Slavic krucina ( *krgcina) "xoAepa, epilepsia', sloven, u-kroknem, - 
nitr crook oneself, u-krociti6s., Czech krucina ^brooxr\\ poln. krgcz {* krgcb) " turn one's 
head, rotate one's head; confuse, whirl one's head around, dizziness, giddiness; swindle; 
(old) tetanus '; 

with -g-\ (s)ker-g-. 



Norwegian hork{0\6 Icelandic *hgrkt) " Weidenband ', dial, also " wrinkled woman', 
fierkja^We together', /7^/'^/"bumpiness, knag', harkal^ gnarled '; russ. korga^ crippled tree 
', /rc»/'zai/jy'"verschrumpft, withered, hard' (etc.); 

nasalized (s)kreng-:0\6 Icelandic hr0kkva {hrgkk) "sich krausein, crook, shrivel up, 
shrink' ( *firenkwan), Kaus. fir0kkva^b\v\6, wrap, frill, friz ' ( *krankwjan), Danish rynke " 
furrow ', Old Icelandic firukka. Middle High German /'i//7/re "wrinkle'; m. aniaut sk-0\6 
Icelandic skrukka^ wrinkled woman', Norwegian s/rm/r/r "wrinkle', Swedish skrynka^ furrow 
', Old English scrincan^ shrink up, verschrumpfen, wither'. Middle Low German schrinken^ 
shrink up '; Gaelic s^/iea/?^ "wrinkle' is perhaps Old English loanword; 

as "verquerte, kreuzweis gestellte Latten': Middle Low German Middle High German 
schrank(e)^ Qi\i\.QX , fence, lock ', Modern High German Schrank, Sciiranke, Middle Low 
German Middle High German sc/7/'e/7/re/7"verschranken, beschranken, hinder'; Old High 
German 5C/'5/7c "deceit', screnchan'to collapse bringen'. Old English screncan'e\n leg 
place, cheat, deceive';
```


## [2026-09-14T01:57:40.822Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '75900,75992p' POK_full.txt",
 "description": "Rest of Pokorny (s)ker-3"
}
```


### [2026-09-14T01:57:40.893Z] TOOL RESULT

```
(sjkregh-, nasalized: {s)krengh-\ 

Umbrian cringatro, krenkatrum, krikatru^ a girding ';urg em. *firengaz\v\ Finnish rengas. 
Old Icelandic firingr. Old English Old Saxon Old High German iiring'nng', Old Icelandic 
iir/ngJa'smaW round vessel' and "clasp, hairpin ' = Old High German r/nka, Old English 



hr/nge'c\asp, hairpin ', Old Higli German Old Saxon hr/ngon'nnge\n, einen circle build '; in 
addition probably as "Rundstab', Gothic hrugga'staW, Old English hrungi. " rung, 
horizontal step on a ladder, Speiche', engl. rung^ rung, horizontal step on a ladder'. 
Middle Low German Middle High German /ic//7^e''Wagenrunge'; Old Church Slavic krggi, " 
circle ', Church Slavic kruglh, okruglh ' round ' etc.; 

(3) Dental extension Ae/f-'turn', see above S. 584 f. 

Y) Labial extensions (s)kereb(h)-, (s)kremb-\.uxx\' see below esp. headword. 

B. Abasis (s)krei-: 



Latin 5g/y/7/^/77' rollenformige Kapsel , shrine' (*round container); 

Lithuanian skrieju{ior *skreju), skr/ef/^\n Kreise bewegen, fly in circle ', Latvian skrienu 
{skreju), skriet'run, fly'. Old Lithuanian skre//s' wing ', Old Church Slavic krilo {* kn-dio) n. 
"wing'; Lithuanian Are/Vas "winded, slant, skew'. East Lithuanian Ara/Vas "slant, skew', apy- 
kraivis^ writhed, crooked, humped ', ablaut. /r/vV/s "schief gewachsener Mensch'; Old 
Prussian greiwa-kaulin kVk. " rib ' ("krummer bone'; dissim. from kreiwa-kaulin), russ. (etc.) 
Ar/V "crooked'. Old Church Slavic razkriviti^ crooW; Latvian krails^ bent, curved, writhed, 
crooked, humped '; Latvian /r/'e/7/s"Linkhand', A-eZr/s (dissim. from *kreiris) ds., Lithuanian 
kairys6s. (dissim. from *krairys)\ Old Church Slavic krin/ca \esse\, crock, pitcher', okr/nb " 
paten ', russ. kr/n/ca'Kuie, stream, brook, wellspring'; 

a) With Dentalen: 

{sjkre/-t-: Latin cnso, -are "with den Schenkein wackein (beim Beischlaf; from the wife, 
woman)', *creitsdor *cntsd\ Middle Irish cr/th'Z\ttern, fever', cymr. cryd^ cradle, fever', 
with 5-: ysgryd, bret. sA/'>ya"vor fear tremble'; Old Icelandic hndi. " attack, storm; 
Zwischenzeit, period (of time) ', Old English hnt^i. "storm'. Old High German {h)nddn 
"tremble', ablaut, (hjr/fffjo lever' , Old English hr/d lever', Old Icelandic hreidrr\. "nest' 
("*wickerwork'); from dem concept the bogenformigen Bewegung is verstandlich Old 
Icelandic sknda^sich langsam vorwarts bewegen, grovel, truckle, creep ' (from WiJrmern), 
Old English scrTt^an, Old Saxon scnthan ar\d skrTdan, Old High German scntan^ march, 
step, stride, strut'. Old High German scrit^ footstep ', Old Icelandic skridrl\}r\, flow, 
Vorwartsschreiten', Old English scnPe, scridem. "run, flow', skridr\. " cart '; Latvian kraitat 
"lurch'; Lithuanian skrieciu, skr/est/ lurr\, slue in circle ', skryt/s' rim of the wheel ', Old 
Prussian scr/tay/e6s., Lithuanian apskritus^ round ', skritulys^ circle, kneecap ', Latvian 
skritu//s'\Nhee\', Lithuanian skr/t/nys 'baW, Globus'. 



(s)kreid-: 

Lithuanian skrindu, skr/st/l\y, l<reisen', skr/d/net/" kre'\sen (from birds)', skrydaut/"\n 
Kreise gehn', skriedziu, skriesti^i\)/\ skraidau, -y//"hin and her in circle fly', s/r/'s/io'i/s "quick, 
fast'; Latvian sAra/iofe/e/'umherlaufen', sknedinaV set in motion '. 

p) With Labialen: (s)kreip-: 

Old Icelandic hreifem. "wrist', hre/fa's\N\ng'; Lithuanian kreipiu, kreiptr turn ', kraipali, - 
yti. Iter, krypstu, /r/yp//"sich drehen'; Old Church Slavic sAre/T/a'suTpairsAia, scurrilitas' 
{*skroipnia)\ Slavic *kre(p)s'b {*kroip-so-) in Old Church Slavic vi^z-kresg, -///"auferstehen 
let (from den Toten)', Church Slavic kresi) m. "rponn, temporum mutatio', serb. kr'ijes^ 
bohannisfeuer '; ablaut. Old Church Slavic i/b5-/r/'65/7p//"auferstehen'. 

(s)kreib-: 0\6 Icelandic hripu. " wooden vessel'. Middle English /vp 'creel'. Old High 
German href pannier '(originally ' the twisted '); Latvian kribasP\. 'netting in sled '. 

s-extension (s)krei-s-, esp. from 'vibrierender Bewegung, (oneself) shake'. 

Middle Irish cressaim^ shake, swing, brandish' {*kristd)\ 

Gothic af-, us-hrisjan^ab-, ausschijtteln'. Old English Old Saxon hrissan^io shake, 
tremble'; Old Icelandic hnsu. ' shrubbery, rod'. Old English hnsu. 'twig, branch, rod'. Old 
High German /7/7s'rod, rod, deadwood, shrubbery, bush'; Norwegian /7s/a'bush, twig, 
branch, treetop eines Baumes; ear', Swedish /'e5S/7a'(Hopfen)ranke', ressn^Docke 
gehechelten Flachses' etc.; Latin c/w/s'hair, esp. hair of the head ' {*crisnis, compare:) 
c/7s-/s'the comb am Kopfe the animal'. Old Icelandic /7/75/a 'shake'. Middle Low German 
risten 'flax, wattle, braid'; Old High German nsta. Modern High German Reiste 
'zusammengedrehter tussock, bundle generally '; with f. Low German riste, r/sse6s., 
Dutch riste {an6 rijste) also 'Traubenkamm, Rispe, row'; Old Prussian craysi^ stem ', crays 
■hay'; 

here as >c?-derivative also: Latin crispus^ frizzy, sich krauseind, vibrierend', crispo, -are^ 
frill, friz, swing', intr. 'tremble', gall. PN. Crixos, cymr. crych' frizzy ', bret. crech6s.\ Middle 
High German rispen' frill, friz ', rispeln^s., rispe ^Qez\Ne\Q, shrubbery ', Old High German 
/7/7S/Oa/7/"virgultum', Modern High German R/spe' deadwood, Buschwerk, bundle, 
biJschliger BliJtenstand', in the Weberei 'eine gewisse Lage the Faden', engl. dial, risp' 
stalk from Schlingflanzen, tendril '. 

C. ^/-basis (s)kreu-:
```


## [2026-09-14T01:57:55.544Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^koron\\|^korōn\\|koron-\\|korona\" IEC.txt | head -20; echo \"-----\"; awk 'BEGIN{RS=\"\\f\"} NR==283||NR==282' IEC.txt | grep -n \"koro\\|kor-\" | head -20",
 "description": "IEC korona lookup"
}
```


### [2026-09-14T01:57:56.689Z] TOOL RESULT

```
7651:kor- “bend, curve; bent, curved'. Cf. kuruos, kur- (1), koron-. (The Celt. evidence is ambig.) Arm. kor (‘curved, round, bent’; s. *curve?); Myc. & Gk. cf. kor-oónós, id. beside kor-óné "book handle’ (LW in Lat. corona); MIr. cor, ap. curu, Ir. cor, pl. coir, m. (2) ‘turn, twist beside corann ‘crown, garland’; W côr, pl. corau, m. & f. “circle? beside coryn “crown of head"
7670:koron-, see koróon-
7696:korono- 'curve-'; Mir cf. corann, Ir. corann, f. ‘crown, garland’; W cf. coryn “crown of head" beside caran, f. id.
13978:517. Cf. kur- (6). WP I, 517 Skt. cf. karómi, dual & pl. st. kur-, beside z- gde krnómi, v. id.; cf. kurvat, act. pt. doing": Av. cf. koronaomi, v. id.; Myc. cf. qeroi (dual & pl. m. queried: ‘shaper, shaping-tool. Ambig. SL or *-r-); (the z-gde in Gk. kár- dopos, f. ‘kneading-trough’ suggests *kr- not *qur-); W peru, v. ‘cause, actuate; bid; main- tain’; Li. kerù, éti & keréju, Eti, v. ‘thrive’ be- side keriü, čti, v. ‘bewitch’. Noun-types in Skt. (o-gde) káras, n. *deed'; Av. Caranom, n. ‘tool’; cara, f. ‘means, remedy’; Per. Car id.; Care, s. ‘means’; (o-gde) kär, s. ‘business’; Gk. téras, gs: -atos, n. ‘omen, wonder’; W peri, m. “cause”; periant, m. ( ‘machine’, fr. *queriont-); OCS. čara, f. ‘spell, magic; OCz. čara, f. ‘barter’; Cáry, fpl. ‘magic’; Li. kéras, m. (2) ‘charm, spell; Latv. (?) ceras, fpl. ‘reverence, emotion’; cf. Skt. (o-gde); kártram, n. 'spell'. Cf. qur- and cpds.
-----
15:kerp-, kerep- (korp-, korop-; kereps-) 'skull, tile, pan, ladle, bowl, potsherd’ Skt. cf. karparah ‘skull, potsherd’; Arm. Serep, i-st ‘ladle? beside karapn & karap, gs. karapin ‘skull’; Ligurian substr. in Rumansch (?) creppa ‘skull’; OCS érépü (tile, also **ladle' in view of Crépiti, v. ‘draw water); R cérep ‘skull’; Cerepók, dim. ‘potsherd’; Cz. střep, id.; z-gde in OCS Crüpljo, érüpati ‘draw water’;
30:kersno- (1) «transversal; thwart; crosspiece, middle'. See next & kersos Hes. kérnai, kérna *spondyls, vertebral spurs’; Alb. qerr (coronet', vet.); Cz. cf. Cercha *cross- line’; Ir. cearn “angle, corner’; OCS cf. érěslo ‘groin’; R éresla, OCz. třiesla ‘loins’. (The con- sonantism of Skt. karásnah ‘forearm’, if re- lated, points to *koros-)
```


## [2026-09-14T01:58:02.746Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR<=7700{n+=gsub(/\\f/,\"\")} END{print \"leaf idx up to 7700:\",n}' IEC.txt; sed -n '7640,7700p' IEC.txt",
 "description": "IEC leaf index and context"
}
```


### [2026-09-14T01:58:03.802Z] TOOL RESULT

```
leaf idx up to 7700: 306
532
com. Sl.) kopije, kopí ‘spear’; Li. kapas; Latv. kaps ‘grave’. Cf. (long-grade in) OE hof, Du. hoef (“hooP and com. Gmc.) and (short vowel in) OCS, etc. kopyto ‘hoof. Long-gde also in Finn. LW kuoppa ‘pit
kopos, å (2) ‘heap’. Cf. WP I, 344 & 373 and next. Cf. kop- Alb. (ambig.) kapë (in place-names: ‘peak’. Cf. koup-); R kopà, Pol. kopa ‘heap’; cf. also Pol. kopny, adj. “snowed-under?
kopos, à “mass, lump’. Variant of kopos (2). Cf. kópios Gk. kópé “hilt'; ON hóf ‘feast’; Eng. hoove ‘flatulence in animals"; OCS cf. kapija Cheap’: Lat. copia ‘plenty’), Li. kúopa ‘mass; crowd’; Latv. kopa, id.
kopsó, eið, ið ‘cut, strike’. Cf. kop- Arm. kopem, id.; Gk. kópso ‘will cut, will strike’; Cz. kosit ‘cut, mow; crop; cross-har- row’; Ir. cf. cuise ‘grass’. (Isophonic: Br. kof, kov ‘belly’: W coff ‘belly; hollow treetrunk’; Skt. kaphah ‘froth’; Av. kafo, id. but Skt. kaphin ‘elephant’; kaph-anih ‘elbow’)
koptos ‘cut, mown; cutting, lopping, mow- ing; cut; cutter’. See kop- Arm. kut'K, gp. kt'Koc ‘crop’; kt'kem, v. ‘mow’; Gk. koptós ‘cut, bruised’ beside koptë ‘kind of cake’; Ir. cot “billhook'; Cor. kot ‘short’; W cot ‘stumpy tail, stump’; Cz. kot ‘lopping’; kopit, v. “lop, cut’; Latv. cf. iz-kapts ‘scythe’; Li. kapstas ‘mattock’
koquios, io (koquius) “head, knob, topknot, tuft, crest. Cf. WP I, 384 Skt. kacah “head of hair’; cf. kačuh, kacvih (an edible root:colocasia); Arm. koč 'knuckle- bone; ankle; block; name of various plants'; Gk. kóttos 'gaming-die'; kótte “head”; cf. synth. cpd. kóssuphos, kótt- ‘blackbird’; ksu- ló-kotta ‘woodcock’; Mod. Gk. kótsos 'chig- non”; kótsi ‘ankle’; kotsáni “stem, trunk’; Alb. kacé 'corncob', kaga-, in various cpd. names of creatures; Ir. coc ‘tuft, crest, headdress’; W cob, f. ‘tuft beside cop, m. ‘summit’; cobyn ‘tuft, branch’; Pol. kok ‘chignon’; Blg. kok ‘plait’; OCS cf. vrů-koči ‘chignon, plait’; Pol. war-kocz, Cz. vr-koč, id. (see urKs-); Big. koc ‘ankle’; R cf. kocan, kócení “head of cab- bage’. (Note: the Mod. Gk. forms and those of
533
Blg. coincide, but the direction of borrowing, if any, is obscure. Cf. kok-). Cret. kósmos ‘magisterial bench? equates w. W cobyn ‘tuft as a form *koquimos/koquinos of adjectival Origin.
koquiubhos, à 'tuft, topknot'. Cf. koquios and WP I, 384 Gk. kóttuphos ‘knot, topknot, tasse; Alb. kagubé ‘tuft, clump, bush’; Pol. kociuba *sweeping-brush'
koquros ‘dung’. Cf. WP I, 336 & 381 Gk. kópros, id.; Alb. kakér-, in cpds. id.; Arm. cf. kakor, o-st. ‘dried cowdung'
kor- “bend, curve; bent, curved'. Cf. kuruos, kur- (1), koron-. (The Celt. evidence is ambig.) Arm. kor (‘curved, round, bent’; s. *curve?); Myc. & Gk. cf. kor-oónós, id. beside kor-óné "book handle’ (LW in Lat. corona); MIr. cor, ap. curu, Ir. cor, pl. coir, m. (2) ‘turn, twist beside corann ‘crown, garland’; W côr, pl. corau, m. & f. “circle? beside coryn “crown of head"
korā, koriom ‘skin, leather’. Cf. koros (1) Av. cf. kar-, v. ‘cut, divide’; Lat. corium ‘leather’, cf. cor-tex, gs -ticis “outer shell’; OCS (and com. Sl.) kora ‘skin, leather’; Cz. cf. kof-ist ‘booty’
korb- (1) (korbis, os, à, kreb-, krb- ?) ‘wicker, basket". Cf. korbio Lat. corbis "basket, cf. corbita 'bumboat; Ir. corb, m. ‘cart, boat": Sw. harpa, v. ‘to sift w. a wire sieve’; R kórob “box, hamper’; cf. Cz. krabice ‘box’; Li. karbas *horse-basket'; Latv. karba “fishing boat; oval wooden case; con- tainer of bark'. (Note. Gk. kárabos “light ship” is thought to be Macedonian or Illyrian > a LW in OCS korabí *boat"). Variant: MHG réf, gs réffes 'back-frame for basket; ON hrip Cpunnet, basket is thought to rest on a form *krib- in view of Latv. kribas, fpl. ‘wicker bed of sledge’. Cf. Maced. kárabos “gate? Hes.)
korb- (2) “ridge, furrow? Cz. krab ‘groove’; Li. karbas (2) ‘notch, kerf
(korbàa, a possible fig. extn. of type korb- (1) in Gmc., cf. OHG harapha, harfa ‘harp’; OE hearpe; ON harpa, id. ON harpa (2) “razor- fish" has an apparent parallel in Gk. kàrabos *crayfish"). Cf. WP II, 589
koquiubhos, à — korio (koreio)
15
20
25
30
35
40
45
534
korbið (?) “bend, twist, deprave, distort, shrink Ir. corbaim ‘deprave’ (ambig. cf. koruos (2)); Icel. herpast, intr. ‘contract, shrink’; R koróbit ‘bend’; Cz. krabit ‘pucker’
kordhos, us ‘rough, hard, harsh; rough sur- face”. Arm. kord, i, av “rough, fallow'; kord, o-st. (cleared land”. Ani); Go. hardus (and com. Gmc.) ‘hard, severe; MHG hart, id.; sm. *sandbed, crust of snow; rough pasture’. (Iso- phonic: OHG bart, hartin 'shoulderblade'; OFris. herde ‘shoulder’; Icel. herðar, fpl. ‘shoulders’)
korəb-, see korb- (1)
korəbhos ‘a black bird(?), crow, raven’. Cf. WP I, 413 Hes. kóraphos “an unidentified bird’; It. corbo ‘crow’; ON cf. hrafn, and com. Gmc. ‘raven’; Finn. LW korppi ‘raven’
(korok-, possible variant of kornk-, q.v. in view of Latv. karaks ‘jackdaw’)
koron-, see koróon-
korguos (variant of krguos, q.v.) fa raucous bird". Cf. WP I, 413 Per. kalay ‘crow’; Lat. (ambig.) corvus, id.; Blg. cf. krag-uj 'sparrow-hawk'; Cz. krah-ujec, id.
kor- “harsh, hard; torture, torment’ Skt. kárjami ‘torment’; Oss. karz, adj. ‘strict’; Alb. cf. n-gardh, v. ‘stigmatize, brand’; ngardhë, f. ‘stigma’; Arm. korcem, kocem, v. (1) ‘beat; ON harka ‘harshness, hardness’; mod. harki ‘dearth’; harka, v. ‘rack, torment’; Du. cf. harkerig ‘stiff, awkward’. (Isophonic are: ON harka (1) ‘scrape’; Sw. harka ‘rake’; Du. (and G fr. LG) barken, v. id. ON also herkja ‘drag oneself along’; Norw. harke, v. ‘hawk, cough’)
koris ‘itch, scab, ringworm; biting insect". WP II, 576 Gk. kóris, gs eos, m. & f. ‘bug’; R kori, f., Ukr. kir ‘moth, measles’
korið (koreið) (1) ‘annoy, tire, abuse’. Cf. karinaio & WP I, 353 Ir. coirim, coraim ‘tire, annoy’; OHG harjon ‘harry’; OE hergian, ON herja, id.; OCS korjo, iti “abuse; Cz. kofit ‘humiliate’; Pol. korzyc, id. W ceryddu, v. inf. ‘to reprove’ is ambig.
535
Cf. kar-
korio (2) ‘give, put-. (Variants: koreió, kortið) Hitt. kariyami “yield; gratify’; Ir. cuirim ‘put’; OBr. cf. hebcorim, s. (privation'. See seque); W heb-gor, -gori, inf. ‘set aside’
koriom, see koros (1)
korios (1) ‘troop, band, flock, host. WP I, 462. Cf. kort-, korst- OPer. cf. kara- people, host; Hitt. cf. kuri- wanas (LW? 'governor"); Cypro-Minoan (que- ried) koiro- ‘flock’; Gk. cf. koíranos ‘captain’; Mir cuire ‘band, troop’; Gaul. (in names) corio-, Tri-, Petru-corii; Romanized Gmc. cha- rio-; Go. harjis ‘army’; OHG hari, heri, OE here, ON her, pl. herjar, id.; cf. also MHG harst, harsch “band, crowd’; Li. kare, f., kã- rias, m. ‘army’; Latv. karš, id.; OPr. kans ‘troop’
kork- (?) ‘scotch, scotched', etc. (kark-?) Arm. karkem ‘baffle; silence’; MHG hargen limp, hobble’; Li. cf. karksóti, inf. “hang around, be disconsolate, mope’
korkoros (variant of karkor-, q.v.) Gk. (Hes.) kórkora “a raucous bird’; (Cz. krá- kor ‘crowing, cackle’, etc. ambig. See karkor-)
korkos (1) ‘filth’. Cf. kurguos (1) Skt. kalkah, id.; Arm. (ambig.) kork, i-st.; MIr. cf. corc-ach ‘marsh’
korkos (korok-) (2) (demon, monster’. Cf. kark- Scythian cf. kórakos ‘demon’; Alb. cf. kark- in kark-zogé, usu. kaké-zogé *blindworm, slowworm'; Cz. krak *sea-monster'. (Skt. kar- kah, m. ‘crab’ is ambig. Cf. kark-)
korn- (kornt-) (?) *prickle? Skt. cf. kantah ‘thorn’; Romani karno, kanro, karo, id..; Arm. karn, Let ‘cardoon thistle’; Gk. (Sicilian) kórnos *butcher's broom’
kornks ‘crow’. Cf. korok- Gk. kórax, id.; Lat. cornix, gp cornicum, id.; Umb. curnaco, acc. sg. id. Cf. variants: Skt. karatah ‘crow’; Latv. karaks “jackdaw”; karnis ‘heron’
korðn-, korən- “edge, rim, border’. Cf. kor- and WP I, 413, II, 591 Per. karán, id.; Gk. koróne, id. (and ‘curve, crown’. LW in Lat. corona); Myc. cf. (queried)
thwart, cripple; be
korió — korsos
20
23
30
35
40
45
536
korono- 'curve-'; Mir cf. corann, Ir. corann, f. ‘crown, garland’; W cf. coryn “crown of head" beside caran, f. id.
korops-, korpor-, cf. kerp- (kerep-) and krp- Skt. cf. karparah ‘skull, tortoise-shell; cup, bowl; Arm. karap and karapn, gs karapin ‘skull
koros (1) ‘skin, hide’. See korā Skt. cf. karkarah (queried, redup: “leather strap’); Lat. corius “leather whip, tawse, thong’; corium ‘hide; husk’; W cwr, pl. cy- roedd, m. ‘skin’, fr. *koros, -es-?); OCS kor, kora (shell, crust, rind', and com. SL); Li. kara ‘lime-bark’; LW in Finn. kuoria ‘shell, peel, husk’
koros (2) ‘arrogance, rudeness, bullying, fighting’. (SI. & Balt. ambig. w. influence of type kar-, q.v.) Gk. kóros ‘arrogance’; OCS korü ‘contumely’; Cz. cf. kory ‘stiff; Li. káras ‘war’; Latv. cf. karš, id.
(koros (3), see koris. Ambiguous W. Cor. cor "little; dwarf")
```


## [2026-09-14T01:58:12.624Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==882' SYN.txt | head -60",
 "description": "Buck p.857"
}
```


### [2026-09-14T01:58:13.687Z] TOOL RESULT

```
, Mots lat. 182.
W. rhentu, also ‘lease’ (11.75).
Br. feurmi, also ‘lease’ (11.75).
4. ON leiga, Dan. leje ‘rent, hire’ (but Sw. lega mostly of persons) : ON [ja,
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Goth. lethwan ‘lend’, etc. (11.61). Falk- Torp 632.
OE hyrian ‘hire’ a person, in 13th, cent. also ‘hire’ a ship, a mare, ME hire (also a house, ete.), NE hire (still mostly persons, but also a horse, carriage, etc.), Du. huren, Sw. hyra ‘hire’ and ‘rent’, see under ‘hire’ (11.77).
NE. rent, lease, both also ‘lease’ (11.75).
OHG (g2)miaten, MHG, NHG mieten, earlier (and so mostly in OHG) ‘pay, bribe, take into one’s pay’, fr. OHG miata, miete (NHG miete) ‘pay’ (11.78).
5. Lith. pasamdyti, epd. of samdyli ‘lease’ (11.75).
Lett. zré, fr. MLG hiren ‘hire’ (11.77). Miuihl.-Endz. 1.837.
Lett. nuomdt, fr. nwoma (sb.) ‘rent’ : nemt (dial. beside n’emt) ‘take’ (11.13). Miihl.-Endz. 2.818, 815.
6. SCr. najmiti, etc., general Slavic words (but ChSI. najeti in Gospels only of hiring persons), epds. of Chl. jelt, etc. ‘take, seize’ (11.13).
Digitized by Arya Samaj Foundation Chennai and eGangotri
possESSION, PRO
PERTY, COMMERCE 813
11.77 HIRE (vb., a Person)
Lith. pasamdyti
leat Lett.  derét oop ON poe leie ChSl.  najetz ork er gine Dan. hyre, SC te NG acer oh Sw.  hyra, lega De iat cam dere ga servizt0, OE hyrian Boh. najmoult ip : Pol. najaé t. E hire ui pee ; wn engose a hire Russ. nanjat’, rjadit fr. alquilar Du. huren oe 8 tecmi se pall OHG  (gi)miaten (gileiten) Rum (gaidim ar faicht ) MHG mieten, dingen a ja paar NHG mieten, dingen Vie eel pr pre : 5 7 . sche for ‘hire’ With reference to per- W. hurio, fr. NE hire. . ; Verbs ostly used also in the sense Br. gopra, fr. gopr ‘wages, pay’, m ry vat ot objects and have been cme (11.78). re ” ich are use ae p Pec). Afew, waa 4, OE (@hgrian, ME, NE hire, MLG te in the former sense-or belong s entirely 10 ' miduseed here haren (> Dan. hyre, Sw. hyra), Du. here primarily, are cu ’ huren (MHG hiren ‘hire’ a horse and
1, NG proddv, in form fr. Grk. po- fis ‘lease’ (11.75), but semantically as ta new deriv. of ueodds ‘wages’, and used mostly for ‘hire’ (persons). ;
2, It. prendere a servizio (used of hir- ing servants, etc.), lit. ‘take in service’.
It. fissare, lit. ‘fix’, hence also ‘come toan agreement, engage, hire’, fr. VLat. ‘firre, fr, fizus pple. of figere ‘fix, fasten’. REW 8335.
Ir. engager, fr. gage(s) ‘wages’ (11.78).
Rum. locmi, lit. ‘bring to order, agree, stipulate’ fr, Slavic, ChSl. ttikiimiti compare, liken’, Tiktin 1619. ae ga
```


## [2026-09-14T01:58:18.628Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"12\\.35 END\\|12\\.36 \\|EDGE, BORDER\\|12\\.353\" SYN.txt | head -20",
 "description": "Buck END/EDGE sections"
}
```


### [2026-09-14T01:58:18.722Z] TOOL RESULT

```
1172:Fr. bord ‘edge, side’ and ‘bank, shore’, loanword fr. Gme. bord ‘edge’ (12.353), REW 1215.
1211:ChSI. krajé (beside brégi for alytanos; Jagié, Entstehungsgesch. 328), SCr. kraj (also sometimes ‘shore’, cf. Rjeénik Akad. s.v.), generally ‘edge, border’ (12.353). Berneker 605 f.
10082:Boh. krajky (pl.), dim. of kraj, ChSl. krajt ‘edge’ (12.353). Cf. NE edging sometimes ‘lace’ (NED s.v. 4).
16240:Ir, oiremain, oiremnach, NIr. oireamh- nach, fr. oirim “fit, suit’, this denom. fr. or ‘border, edge’ (12.353)?
21176:CHAPTER 12 spATIAL RE b) 12.51 41 Puace (S- 12.52 fa. Por (Place, Seb “ae 12.58 013. 51 12.54 yi Lie ae 12.55 ois Stan (VD: ae 12.56 yo16 REMAIN, uaa Pere) 12.57 in17 pees 12.58 12.18 Lea : 12.59 1919 Quiet (adi) ie ; : 991 COLLECT, GATHER . ms 12.62 122 Jow, UNITE ake 1293 SEPARATE (vb-) ; 12232 DiviDE 12.64 1224 Oren (vb.) 12.65 1225 Snur, CLosE (vb.) 12.66 12.26 Cover (vb.) 12.67 1227 Hin, ConcesL 12.68 1231 Hicw 12.71 1232 Low 12.72 1233 Tor 12.73 1234 Borrot 12.74 1235 Eyp 12.75 ae Por 12.76 ee 12.77 12.36 Stop 237 Mux (adj.) Teale 12.38 CENTER 12.81 12, < 78 Ricur (adj; vs. Left) yore aa ler (adj. vs, Right) 12.83 nay Aoi (adv) 12.84 pas oe adv.) 12.85 45 Easn 9 12.46 Wesr 12.91 247 Nonny 12.92 248 Sonne 12.93 12.94 829
21939:12.353 EDGE (Of a Knife, Sword, etc.; of a Table, Forest, etc.) Grk.  dxuiys xpaoredov, Goth. ....; (skaut) Lith. a&mens; kra3tas, xethos ON egg; rond briauna
22036:12.36 SIDE Grk. — wAevpai Goth. féra Lith. Sonas, pusé NG se pepia ON sida Lett. sans, puse Lat. latus, costa Dan. side ChSl.  (rebra, strana) It. lato, canto Sw. sida SCr. strana, bok Fy. cété Or side Boh. strana, bok Sp. lado, costado ME side Pol. strona, bok Rum. parte NE side Russ.  storona, bok Ir. toib, sliss, leth Du. = zijde Skt. pargva-, paksa-, NIr. _—_taobh, slios, leath OHG - sit(t)a, fiara ardha- W. ystlys, tu MHG ssite Av. araéa- Br. kostez, tu NHG seite
22975:It. canto, cantone, also ‘edge, side’, see 12.353,
22998:(12.353).
23010:ChSl. kutdt for *katt, SCr., Russ. kut Boh. kout, Pol. kat, prob. connected, aig cognate or loanword, with the group Lat. canthus, It. canto, etc. (12.353). Walde- P. 1.351. Meillet, Etudes 226, Other. wise (: Grk. xovrés ‘pole, pike’) Berne- ker 602 f.
23109:W. cant, Br. kant, prob. : Gallo-Lat. cant(h)us ‘iron rim of a wheel’, etc. (see 12.353). Walde-P. 1.351 f.
32940:Rum. margine ‘edge’ (12.353), used also for ‘boundary’. Tiktin 953.
32950:ME bordure, NE border, fr. OF r. bor- dure, deriv., through vb., of bord ‘edge’ (12.353). NED s.v.
32960:SCr., Pol., Russ. granica, Boh. hrani- ca, deriv. of word seen in ChSl. grant ‘chapter’, Russ. gran’ ‘facet, side’, Boh. hrana ‘edge’ (12.353), etc. Berneker 346. Briickner 155.
```


## [2026-09-14T01:58:24.090Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"karana\\|karān\\|karan \" SYN.txt | head -20; echo \"----\"; sed -n '21850,21870p' SYN.txt",
 "description": "Buck karana"
}
```


### [2026-09-14T01:58:24.165Z] TOOL RESULT

```
5892:| Fr. oreille OL are Boh.  ucho Sp. oreja, oido ME sere Pol. —-ucho Rum. ureche NE ear Russ. ucho Ir. au, cliias Du. oor Skt. karna- Nir. cluas OHG ara Av. gaosa-, karana-, W. clust MHG ar(e) u& (dual) Br. skouarn NHG ohr
5903:4, Skt. karna-, Av. karana- (of evil beings), etym.? Walde-P, 1.412, 495.
8182:4.95 DEAF Grk. — xwdds Goth. baufss Lith. kurtias, kurtinas NG xougds ON daufr Lett. kurls, kurns Lat.  surdus Dan. dv ChSl. gluchit It. sordo Sw. dév SCr. gluh Fr. sourd OE déaf Boh. = hluchy Sp. sordo ME deaf Pol. gluchy Rum. surd NE deaf Russ. gluchoj Ir. bodar Du. doof Skt. badhira- Nir. —_ bodhar OHG  toub (tumb) Av. karana-, asrut-gaoka- W. byddar MHG toup Br. bouzar NHG taub
8194:TS oF THE BUD AR suet ‘dumb’, and ‘blind’. 6. ChSl. glucht, etc., general Slavic, words £08 a: Falk-Torp 179. outside connections? Berneker 308, 309. rate? Fie kurtinas, Lett. kurls, Briickner 145 (unconvincing). 5, Lith. 1 Jriinit ‘having a mutilated urn”) (of. also Russ. kur-guzyj 7. Skt. badhira- : Ir. bodar (above, 3). eat oF n08e" Uke. kur-nosyj ‘snub- Av. karana- (so NPers. kar ‘deaf’), see tailed’, ‘deaf’ ighort- ob. also Av. karana- ‘deaf’, | above, 5 and Barth., IF 3.169. nosed’), PF tghort-eared’, all with com- Av. asrut-gao8a-, lit. ‘having unhearing Skt. kara of mutilated and presumably | ears’ (cpd. of a- privative with sru- ‘paler ‘out’. Mil. -Fndz. 2.323. | ‘hear’ and gaoga- ‘ear’). Barth. 223. fr. UE Berneker 6 4.96 DUMB ‘ Goth. dumbs, baufs Lith. nebylys, beZadis Grk. a ori ON  dumbr Lett. méms NG oie Dan. stum ChSl. némit Lat. muto, mutolo Sw. stum SCr. nijem Be et OE dumb Boh.  némy s, —imudo ME = dumb Pol. — niemy a mut NE dumb Russ. nemoj it * amlabar, balb Du. stom Skt.  miika- Nir. balbh OHG _ stum (tumb) Av. afravaota- W. mud MHG stum (tump) Br. = mud NHG  stumm
12034:Russ. dymovaja truba ‘smoke-pipe’ or pyadenee of ee actual chimney) lit, R commonly iruba ‘pipe, trumpet’ used smoke-outlet’, epd. of dhiima- ‘smoke? ie alone for ‘chimney’ : ChSl. traba ‘pipe, | and nirgama- ‘outgoing’. N T 7.41 FURNITURE dl Grk. mda Goth. Lith. baldai, rakandai se NG éxtrda ON _hiisbiinadr, -biiningr Lett. istabas lietas, mebele Io Lat. _supellex Dan. mébler, husgeraad Chsk 2.52 It. mobili, supellettile Sw. mobler, husgerdd SCr. — namjeStaj, pokuésivo Fr. meubles OE idisc, inorf Boh.  nabytek h Sp. muebles ME _(houshold, mobles) Pol. mebel, sprzet Rum. mobile NE furniture Russ. mebel’, obstanovka Ir. intreb, fointreb Du. _—meubelen, huisraad Skt. (upakaranani) pr NIr. _ troscan OHG § (giziugalz, gizawi) Av. ee be W. dodrefn MHG hisrdt, hisgerate Br. annez, arrebeuri NHG miédbel, hausgérat er ‘Furniture’ is understood here in the | plurals of It. mobile, Fr. meuble, ete, pl now prevailing sense of NE furniture ‘piece of furniture’, fr. Lat. mobile i (NED s.v., 7), that is as ‘house furni- ‘movable’ (cf. mébilia ‘movable goods, ty ture’. Some of the words are connected chattels’), deriv. of movére ‘move’. mi with those for ‘house, dwelling’. But 3. Ir. intreb, fointreb, (NIr. intreabh fr the majority had originally, and some ‘property, wealth), epds. of ind- in’, fo- N still have, a wider Scope, covering all | ‘under’, and treb ‘dwelling’ (7.11). sorts of movable property, equipment, NIr. troscan ‘implements, baggage, su utensils, etc. clothes’ (Gael. trusgan ‘clothes’) and (N The words are partly plural, partly | ‘furniture’ (or more specifically troscan le Singular forms used collectively. lighe ‘furniture of the house’), loan- 1 1. Grk. émmda (also ‘utensils, fittings’, | word fr. ME trusse ‘bundle, baggage’, Gi but usually not so general as oxebn) : | with added suffix. Macbain 378. 12 erurohi surface’, érurédatos ‘on the sur- W. dodrefn, MW deodreven, cpd. of dy- th face (cf. Cret. tmmédara xphuare = tm- | ‘to’ (often intensive), go ‘sub’, and trefn fu wage émméhouat ‘come upon’, ete., IE ‘arrangement, order, system’. Keel-. Walde-P. 1.514 f. Br. annez fr. MBr. anhez ‘dwelling’, 90
12063:7. Skt. upakaranadni, mostly ‘uten- sils’, fr. wpa-kr- ‘bring near, prepare’.
13603:8. Skt. kr- (krnoti, karoti, krta-, etc.), Av. kara-(karanaoiti, karata-, etc.), OPers. kar- (akunavam, karta-, etc.), general Indo-Iranian (still the common word in modern Indic and Iranian languages), perh. : W. pert ‘cause’, Ir. cruth ‘form’, Lith. kurti ‘build’. Walde-P. 1.517 f. Uhlenbeck 63.
14794:9.422 TOOL ‘ a adelov, Spyavor Gophie ys $i ani Lith.  inagis, irankis Tiegh ah lea ON | {al (pl.) Lott. ike Lat. instriimentum Dan. verkidj, redskab ChSI. (orqdtje) It. ordigno, utensili (pl.) Sw. verktyg, redskap SCr. orude, alat Fr. outil, instrument OE t6l Boh. ndiin, néslroj Sp. herramienta ME tole Pol. narzedzie Rum. unealtd NE tool Russ. orudie Ir. airnisi (pl.) Du. werktuig. Skt... karana- NIr. — wirlis, oirnéis, acra OHG  giztuc ‘ Av. WwW. arf MHG ztuc, wercziuc Br. benveg NHG_~ werkzeug
14823:7. Skt. karana- (neut.), mostly act of ‘doing, making’, fr. kr- ‘do, make’ (9.11),
21873:Russ. konec, kraj Skt. _ anta-, pranta- Ay. karana-
21898:Av. karana- (also in special senses ‘border, shore’, etc.; NPers. karan ‘shore, side’), etym.? Barth. 451.
21947:it poeta a MHG scher(p)fe, snide, ecke Skt. a¢ri-, dhara-; pranta- ae se ritach, NHG | schneide, schdrfe; Av. dara-; karana-
22035:Av. karana- ‘end’ (12.35), also ‘edge, shore’. Barth. 451.
22900:o It. curvo, Fr. courbe, * Grk. kuprés ‘humped, ‘ Cor ‘circle’, Av. skarana-
23037:Crk. rerprywvov Goth? os. Lith. keturkampis, ketvir- NG rerp&yuvo ON ferskeyttr, _ ferhyrndr tainis lat. quadralum, quadrum (adjs.) Lett.  Ceirstiris It.  quadrato, quadro Dan. firkant C@hSliveeeriee Fr. _carré Sw. Syrkant SCr.  éetverokut Sp.  cuadrado, cuadro OE féowerscijte (adj.) Boh.  lverec, civerhran Rum. pdtrat ME square, fourhuyrned Pol. czworokat, czworobok I. celharchoir, cetharuil- (adj.) Russ. éetyreugol’ntk lech (adjs.) NE square Skt. caturagra- Nir. cearnach, cearnog Du vierhoek Av. éadru.karana- (adj.)
23068:Av. éa6ru.karana-, adj., epd. of éa@war- ‘four’ and karana- ‘end, border, wing (of an army).’ Barth. 578.
23070:Grk. — orpoyyidos Goth. Lith. apvalus, apskritas NG oTpoyyuns ON sivalr, kringlatir Lett. apal’s Lat. rolundus Dan. rund ChSl.  (o)kruglit It. tondo, rotondo Sw. rund SCr. okrugao Fr. rond OE sin-wealt, -trendel, Boh. okrouhly, kulaty Sp. redondo -hwerfel Pol. — okragly Rum. rotund ME round Russ. kruglyj Ir. cruind NE round Skt. vartula- Nir. cruinn Du. rond Ay. skarana- W. crwn OHG © sinwel, sinhwerbal Br. krenn MHG sinwel, runt NHG rund
23094:Av. skarana- : Ir. cruind, ete. (above, 3). Barth. 1587.
25001:Grk,  7édos, reAcvTHT Goth. andeis Lith. galas, (pa)baiga NG rédos ON endi, lok Lett. gals, beigas Ist, _finis Dan.  ende, slutning ChSl. kontéina, konict . fine Sw. dnde, slut SCr. _konac, svrSetak Ir, _ fin, bout OE ende Boh. _konec Sp. fin ME ende Pol. = koniec Rum. sfirgit NE end Russ. konec ,  cend, dered, deod Du. einde, slot Skt.  anta-, pranta- Nir. detreadh, crioch OHG enti Av. Graosli-, dwarasah-, W.  diwedd MHG ende karana- Br diwez NHG  ende, schluss Nouns for ‘end’ in the temporal sense, | Walde-P. 1.832. Ernout-M. 363. the opposite of ‘beginning’, are in large | Walde-H. 1.503. measure the same as those used for ‘end’ Rum. sfirgit: vb. sfirgi_ ‘finish’ Ma spatial sense, for which see 12.35. (14.27).
25016:Temporal use of Av. karana- (12.35) attested only in epds. Barth. 451.
----
12.34 BOTTOM
is NG sino. Goth. Lith. dugnas lat, fundus ON _botn, grunnr Lett. dibens i fondo Dan. bund ChSl. diino a fond Sw. botten SCr. dno a fondo OE botm, grund Boh. dno fund Me anu grounde Pol. dno Mr" jottom Russ. dno V. bun Du. bodem Skt.  budhna- Br. cae (bon) He bodam, grunt Av. biina-
Oueled nee Boaetrs boden
oden
CC-O0. In Public Domain. Gurukul Kangri Collection, Haridwar
| | |
856 SELECTED INDO-EUROPEAN SYNONYMS
Most of the words for ‘bottom’ belong to an inherited group common to Grk., Lat., Gmc. and Indo-Iranian, or to an- other group common to Balto-Slavic.
1. IE *bhu(n)d(h)- with various suf- fixes, Walde-P. 2.190. Ernout-M. 401 f. Walde-H. 1.564 f.
Grk. rv§uqv; Lat. fundus (> Romance words); ON boin, OE botm, etc., general Gme.; Skt. budhna-, Av. buna-; Ir. bond ‘sole of the foot’.
2. NG pop. wézos, fr. class. Grk. razos ‘path’ (10.72), through the Byz. meaning ‘floor’ (7.26).
3. Ir. bun, W. bon (both also ‘trunk’ or ‘stump’ of a tree), perh. orig. ‘blow’ (cf. W. bonclust ‘box on the ear’), fr. root *bhen- in Goth. banja ‘blow, wound’ (Walde-P. 2.149), with semantic devel- opment ‘blow’ > ‘club’ > ‘stock, trunk of a tree’ > ‘bottom’. Cf. Fr. bout ‘end’, orig. ‘blow’ (12.35). G.S. Lane, Lan- guage 13.22 f.
12.35
Grk.  axpos adj., axpov, Goth. andeis
axpa, mépas ON endi NG &xpa, &xpn Dan.  ende Lat. ezirémus adj., extré- Sw. anda
mum 0} 0) ende It. capo, eslremo, etc. ME _ ende Fr. bout } NE end Sp. cabo, exiremo, etc. Du. einde Rum. capdt OHG enti Ir (for)cenn MHG ende Nir. _deireadh NHG ende W. pen Br. penn
‘End’ is understood here, of course, in the spatial sense, not in the temporal, though the latter is to a large extent ex- pressed by the same words (14.26), nor in the frequent secondary sense of ‘pur- pose’. In Greek and Latin ‘end? is often expressed by adjectives in agreement with nouns denoting the object referred to.
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
W. gwaelod, Br. goueled : W. gwael ‘low, base’, Ir. fael ‘evil’, further nae nections dub. Stokes 259 (: Lat. a but cf. Walde-P. 1.214). :
4. ON grunnr (only ‘bottom’ of the sea), OF grund, ME grounde ‘bottom’ and ‘surface of earth, ground’ (NE ground), OHG grunt (gl. Lat. fundus) MHG grunt ‘bottom, abyss’, etc, (NHG grund), ef. Goth. grundu-waddjus ‘foun- dation wall’, root connection dub, Walde-P. 1.656. Falk-Torp 3524. Feist 222.
5. Lith. dugnas (*dubnas), Lett. (*du- bens >) dibens, ChS]. dino (*diibno), etc., general Slavic = Gall. dubno-, dumno- ‘world’ (in Dubno-rix) : Lith. dubus ‘deep, hollow’, Goth. diups, etc. ‘deep’, W. dwn, Ir. domain ‘deep’, etc. Walde- P. 1.848. Miihl.-Endz. 1.465. Berne- ker 245 f.
```


## [2026-09-14T01:58:30.411Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '21871,21905p' SYN.txt",
 "description": "Buck 12.35 END discussion"
}
```


### [2026-09-14T01:58:30.463Z] TOOL RESULT

```
END Lith. galas Lett. gals ChSl. kontct
SCr. kona, kraj Boh. _ konec, kraj Pol. koniec
Russ. konec, kraj Skt. _ anta-, pranta- Ay. karana-
1. Grk. &akpos ‘at the farthest point, uttermost’ (also ‘highest’, whence its use for ‘top’, 12.33), e.g. axpn xelp ‘end of the arm’ = ‘hand’ (Hom.), am’ éxpa? obpavay éws &xpwy abrGy ‘from one end of heaven to the other’ (NT). Hence also as sbs. éxpov and dxpa, NG pop. &xpt-
Grk. zépas, Hom. zefpap, fr. *atprap : arépav ‘on the other side’, Skt. para- far,
Digitized by Arya Samaj Foundation Chennai and eGangotri a 4
31.
: a, TEPHOYs Lat. terminus
Grk. nit only rarely for more d
pound eet fr. the root of Lat. trans
’ oss’, etc. generiC t,t ‘pass over, Cr ’ ae 733, Exnout-M. 1082 Walde-* +“ termost’, e.g.
¢ emus ou lk Lat. Be the end of the bridge’,
z ie 5 ‘at the end of the book’. in exlremo labr' irémum (> It. estremo, Hence also sb. 5 r'
10, etc.). : se at, fnis, which though orig. @
Hal notion is in actual use ‘border, ini and ‘end’ only as ‘purpose’ or
1
mporal, see 14.26. é S e Bnd Sp. cabo, fr. Lat. caput ‘head’ ; sl, capila > Rum. capele, hence new sg. capal. : 3 In Italian and Spanish various other words are used for ‘end’ in particular comections, as fondo ‘bottom’ (12.34) for ‘lower end’ or simply ‘end’ of a room, garden, etc., punta ‘point, tip’ for the end of astick, etc., It. coda ‘tail’ for the end of a rope, a train, etc.
I. bout (OFr. also ‘blow’, hence ‘end’ as ‘striking end’?), back-formation fr. OFt. bower ‘strike, thrust’, this fr. Prank, *batan, cf. OG bozan, OE béatan strike, beat’, REW 1228¢. Wartburg 1459 f,
3.1, cend, cenn, W. pen, Br. penn all lit, head’ (4.99 ‘ 7a ), esp. as ‘end? also Ir. tlh don th Sor ‘on, upon’.  @areadh (used in most of the eg Ir. dered ‘remains, (temporal, as ‘end
Digitized by Arya Samaj Foundation Chennai and eGangotri
TIONS: PLACE, FORM, SIZE 857
of the world’, Wb. 10b8), fr. di-rethim ‘run out, off’, epd. of rethim ‘run’. Pedersen 2.598.
4. Goth. andeis, OE ende, etc., gen- eral Gme. : Skt. anta- ‘end’, epd. pranta- (pra-anta-), and prob. related ultimately to Skt. anti adv. ‘opposite, before, near’, Goth. and ‘on, over, along’, Lat. ante ‘before’, Grk. ayvzi ‘opposite, for’, etc. Walde-P. 1.67. Falk-Torp 193. Feist 49.
5. Lith. galas, Lett. gals, prob. through ‘point, prick’ : Lith. gelti ‘sting’, gelia ‘it hurts’, ChSl. zalt ‘pain’, OE cwelan, Ir. at-baill ‘die’. Walde-P. 1.690. Miihl.-Endz. 1.595.
6. ChSl. konict, etc., general Slavic, also and orig. ‘end’ temporal, deriv. of Slavic *koni% in Russ. kon ‘beginning’, SCr. od kona do kona ‘from beginning to end’, Boh. do-kona ‘to the end, com- pletely’ : ChSl. na-éeti, Russ. nacat’, etc. ‘begin’, Ir. cinim ‘spring from, be born’, Skt. kanina- ‘young’, etc. Peculiar de- velopment fr. ‘beginning’ as one of the ends. Berneker 560 f. (otherwise on se- mantic relation).
SCr. kraj, etc., used more or less in certain connections for ‘end’, but the regular Slavic word for ‘border, edge’ (12.3853), ChSl. krajt ‘border, shore’ (1.27).
7. Skt. anta-, pranta- : Goth. andeis, above, 4.
Av. karana- (also in special senses ‘border, shore’, etc.; NPers. karan ‘shore, side’), etym.? Barth. 451.
CC-O0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
858 SELECTED INDO-EUROPEAN SYNONYMS
12.352 POINT
Grk. xy, axis, etc. Goth. Lith. galas NG (axis, etc.), pop. pity ON oddr Lett. gals Lat.  cuspis, mucré Dan. _ spids, od Chsi” ce. It. punta Sw. — spels, udd SCr. Siljak Fr. pointe OE ord Boh. _hrot, Spitka Sp. punta ME point Pol. _—_koniec Rum. virf NE point Russ. konec Ir. rind Du. spits, punt Skt. agra- Nir. rinn OHG - spizza, spizzi, ort Av. i , W. pwynt, blaen MHG spitze
Br. beg NHG  spiize
Words for ‘point’ (here intended as ‘sharp end’) are in several cases, as might be expected, cognate with words for ‘sharp’ or names of particular sharp- pointed objects. Some are the usual words for ‘end’, used also for ‘point’, with or without a distinguishing adj. for ‘sharp’. Or, since the ‘top’ of an up- right object may also be a ‘point’, a word for ‘top’ may also cover ‘point? (Rum. virf), as conversely NHG spitze is used for the ‘top’ (of a mountain, etc.).
```


## [2026-09-14T01:58:34.722Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"karana\" BRT.txt | head -40",
 "description": "Bartholomae karana"
}
```


### [2026-09-14T01:58:34.778Z] TOOL RESULT

```
3211:'sagen':  äla  (sSPfA.)  F.-K;  —  mit ui/i  is±):  aöaica  (iSPfM.)"'  uiti  V.4.47, N._J7.  a)  Pass.  'genannt  werden,  heissen', mit  dopp.  Nom. :  yäia  . .  akarana  anayra asaonö  sfif  aili  Yt.Ä48.
4247:uranfinglich' :  akarana  'ra  asaonS  sUs^sA.) YtÄ48;  F.  7.  a)  'ra  raocä  (iA.)  "die!
5607:■iPiMf  VL/5.57;  —  'VB  nama  ahmt  'mS:'  j-  arazo.suta-  Adj.  'der  zur  Schlacht iwoM  (7/tffi»  Yt  75.46,         *  I  ausgezogen    ist':    vispe    karana    rasmatiü
8453:•  g.uba-,  j.  uva-'l,  uva-",  ava-»,  ^^•''^  aspa.vJraja  Yt./O.ior;  —  *.vayt  l.\Df.) Adj.  (fem.  -3-).  Du.  'beide':  V«  «afiwa  I  p.  2b«';  —  ub5ya(^)  F.:.'b»  c)  Plur N.p9";  —  7'a^<i«afl«aft>vrtV.y.3i-37  adjektivisch  'beiderseitig,  beiderlei':  sai/^e PüZ.'';  —  uva  karana  aiMä^  z»mS  Yt  10.  .  .  ;i<i/„^a  .n-afi  (APn.)  xsudrä  'kam.- 95;  5-131.  19-^9'  —  -vayäi'  maimvä  rac'^wayäti  mazdayastianamca  daiiäyas- dämqn  Ytij.76;  —  uvaHl^a  nö  ahubya  nanamca  "wes  ..  Frau  beiderlei  Samen nipayä  aluca  auhius  ys  astvats yasca  asii  durcheinandermengt  . ."  N./i. manahyö    Y.57.2S;    25,    YL/0.93';     —       Ableit  ans  bAi..  —  «L  i^^lJja-  Adj.  —   Pü.;
9242:•  j.  'karana-  m.  'Ende';  i)  räumlich:  "des  gläubigen  H.,  (aus  der  Familie)  der 'Grenze,  Rand;  Ufer;  Flügel  (des  Heeres)';  A'."  YL/j.ia?.
9256:.  j.  »karana-  n.  ein  Kleidungsstück  mite- '  f '■^'''«■'  "^  ^^^^t""  =  k>nnv-'\  12b lererGrösse, 'Hose'');  v«.«.r?y^.^«..««^,,r'f''-'«-'':  9+^4  -f^^«va-,  n  k.r.>ya-i\ "eine  Hose,  die  die  beiden  Schenkel  be-'~  \^[^-°'''.^f"^'-     .  ,    .    -,      .
9332:•  j.    'karana-  m.    Ohr',   uzw.  rfnÄ^ischer       haben;  vgl.  Yt.  ,0.  125.-»)  Anders  freilich Wesen":    lai  drvalö   drvatyiisca    asi    usi ■     Dk.  /.  4.  44  (SBE.  47.  59). 'na{Kp.)gava*dvari>mzafar»..pairi.-\^    .     ^^^3-    V.    'ausschütten'.    Praes.    2 urvalit^m  (sd.)  Yt.//.2.  ,_(.^„^._  _  pp^p^  ^^„y^._
9573:•  j,  karanavant- Adj.,  PPA.;  s.'kar-Tati\kairy3  yava  gaestis  gaöavarS  Y.g.io;  — No.  S.  kshrptm    .  .  yam   sämake  (sd.)    'pake   Yt
9771:_^  _     •  j.  gao'karana-  m.  Name  eines  raythi-
11172:•  ).  £adTu.karana-  Adj,  mit  vier  Ecken, Kanten':  gaosävara  "«a  Yt.  j.  127,  /7.10,
13700:•  j.  dürae-karana-  Adj.  'des  Enden  in der  Feme  liegen,  fembegrenzt":  asmati>m
15539:hin's';  a)  räumlich:  yat  barata  annm mainyüm  framitim  (sd.)  . ,  mva  'ri  Z3m3 karana  YL/p.  29;  —  yeähe  tat  jfar»w isat  .  .  Jraarase  vlspäU  avi  Harlan  .  .; •ri  yäii  (als  Akk.)  hapta  karlvqn . .  apatat Ytig.Si.  b)  zeitlich:  apqm..yh  para ahmät  Atslmta  . .  hamaya  gätv&  äar^yimät 'ri  zrvarum  Yt.  ;^.  53;  —  aat  d^ra  vT- car»nti  {j&nA.  frara^ayf)  dasa  "ri  xsafnö ".  .  decem  per  noctes"  Yt  13. 49.  Un- deutlich: yat  'ri  bansma  hanjasante  N. tf2*>.  2)  mit  Lok.,  nurgAw.  'in,  bei  -'»:
17547:\.  fraiarana  Yt,  13.  39:  X\ts  frä  karana.
20797:—  avaf  yät  (statt  NSn.)  hvarS  aväcl  Y. ^6.  6.  zu  3) :  viävA  avqm  (nämL  •« jf nftw)  yä  (NSf.)  Jm  anhat' apima  (sd.)  Y. 44- 19;  —  avat  xlääir>m  hyat  .  .  vokü vaxsat{%d^  manaiahä  Y.^i.6;  —  x/a- %nmäJ  avat  ya  (IS.)  huitUU .  .  dst  Y. 2g.  10;  —  av3is  urvatais  i&A.)  ya  (APn.) ia..dJd>riiS  H.44~\%-  ß)  adjektivisch wie  bei  e  (Sp.  1204  m.):  avä  yä  da  asts (Sp.  241  u.)  dngväit^ . .  Y.  43-  4-  B)  im jAw.;  das  Relativ  ist  a)  substantivisch aom  asmatum  yS  usca  raoxlnS  .  .  y3 imqm  zqm  äca  patrica  bväva  ..yö  histaite ..yim  vasle..yaAmäi  tiSii-.  Ytl^.sL; aom  ,.  *aurvantim  y3  ha^/tayä  ..urvalsayat karana  Ytj.131;  131,14.58;  —  *avaiti hat  jahikayäi  yä  . .  pu^nm  . .  patke  upa. baraitiisd.)  Yt  17.  58;  Ä  51,  V.io.  17';  - aomca  süksm  yim  baraiti  karö  Ytr4'29;
21017:1 )  'in  Aufregung  geraten,  sich  aufregen", '  •  K"  Y^^^'^y'  ^  'R"*|ng'^«t.  Emsigkeif vom  Wasser:  yaoz»,iti  vupt  ka,-an!>  zrayä  ('«  religiösen  Dmgen);_PIur.  m  Verbmdung vouruias'aya  Y.Öß.r,  —  „a,  ««^j,„,«  mit  ß3- usw.,  Plur.:  ^^^<I  ^^?  **i;/r<7- (AD.)  karana  (sd.)  ^r^^«  vmruJ-aü.y.r  «"«^^  ■  ■  ,Jf"  "'«V^  »»s  ■"*■)  ^f^^'-^f YL5.38;  -  sonst:  ÄJ>f,S  ya^z^ji/i  tisUlm  '''^"fy^  (Sp-  335  "■)  ■  -  yäzama.dl    Y.
22690:•j. 'vayav-, 'vaya- ''m. 'Luft,  Atmosphäre', als  Gottheit'*':  'yus  bä  nqma  ahmt . .  avat •yus  .  .yat  «va  dqma  vayemi  yasca  äa%al sp»nts  mainyui yasca  da'^at  anrS  matnyus Yt.  1$.  43 ;  —  'yusys  upar5.kairy5  Yl  75. 4, 2 1 ;  3  (als  Vok.) ;  —  'yus  aurvS  *usiäj *yasts  d>r3ii.yaox3ürS ..\t.is.^^;  —  °yaos uparS-katryiiu  tarähätö  anyäts  dämqn  Y. 22.24,  Ytij.  o;  —  %wasahe  3^diätahe trvanaht  akaranahe  'yaos  upareJkairyeAe V./P.13;  S.J.21;  —  aaai  ti  -yö  (Vok.) yazamaidt  yat  tl  asti  sp>ntS.mainyaem  Y. Äj.  5 ;  —  '^  aurva . .  'yS  taxma  Yt.  15.11; —  t9m  yazai . .  uynm  vaim  (Akk.)  uparS.' iairlm  Yl/J.  5;  —  valm  aiavamm  .. valm  uparS.kairim  .  .  tardhättm  anyüis dämqn    Y.  25.  5,  S.  2.  2i;    Yt/J.  1';    —  .
25217:•»(a«ff(GS.)  amSJütahe  YtJO.36;  — yä 'manB  . .  *jra  *karana  sSnäayänti  Yt  13.
25555:machen, fugare':_c?^ittW(yii..»i/a  urvaisa- yat  karana  Yt.j.  131.  ß)  'abwenden,
26467:•  j.  skarana-  Adj.  (fem.  'na-)  'rund': aiibAa  z^ms  yal  pa%anayä  (sd.)  *nayS dBraiparayä  Yt.  10.  95;  5.  38,  J7, 19,
26561:—  asmamm  ..  *gaä^Im  *gaH&yayä  stSis Vr.  7. 4.  a)  mit  GS.  aiaone{^^.  251  u.): yaca  upairi  (sd.)  iS  akarana  anayra  a^acnS Sil/  aSi  Yt.  Ä",  48;  —  ^antim  trvamm mainyava  stx/*asaonS data  .w(Sp.a76ni.) V.  2.  igPüZ.  et)  mit  vlspa--.  vTspqm asaenS  stim  .  .  mainynfm/ä  gaihyqmcä Y.  3S.i;Vt.  16. 1 ;-- vlspqm  asaons'stXm haitlmca  bavairUlmca  büsydntlmca  Y.  ip.g;
26928:mit  frä  Med,  'sich  womit  (Akk.)  breit, augenfällig  machen,  womit  Staat  machen, etwas  prunkend  zur  Schau  tragen'; vantäiahs  .  .  frä  gaosävara  sispimna (NPm.)  cä^ru.karana  minu(sd.ya  zaranyS.- pisi  ". .  ein  vierkantiges  Ohrgehänge  zum Staat  tragend  und  .  ."  Vtij.  10;  —  */ra *gaosävara  sXsp^mnaQiSf.)  ü^ruJtarana .  .  ar»dvX  YL5.  127;  —  andvT  .  .  frä srTra  *'zus  sispata  *urvaiH  basujtaoyehi '^A.  .  .  herrliche  Sachen  trägt  sie  zur Schau,  die  anmutige,  ■ ,"  Ytj.  7.
28774:•  j.  haoya-'*  Adj.  (fem.  'yä-)  link':  *'ys dai'i»sF.3g;  —  'yäj  *ir  *naimäi (sd.)  H- 7p;  — frahntars  {iA.)  ,  .  *Aaoyqm'^  apa iraxtim  N.  7p;  —  'yqm  sup/Tm  V.Ä47, 48;  56.  57,  5- '7'.  so.  ai,  y.33;  — V'?* (APm.)  angustqm  V.Ä71';  —  AavSya^'' zasfa  nyils?mnff  y. ig.  ig ;  —  hävSya^ (la)  bäzvSi.^)  daiinaca  daiina  bmö *hävayaca^'^^  V.j.15;  —  AaiHayä.. uva  ..  karana  Aöyümca^^  äasimm'a  daS- tumca  AeyamM^^YtSi3i;  —  höyUmla'''' detänm  Y.  i/.  4;  —   hsyum^  gaesrnn"^.
30030:•  j.  fravaiay!^  .  ,  y&  rastnanS  "ha^m.- Stätäe'*  *frä  *karana  sHndayeinü  Yt. ^3-  39-
30044:•  j.  hikarana- Adj.  'rund,  bauschig';  ä/r?.- vaiarum  (sd.)  °nfm  V.  14.  7.
```


## [2026-09-14T01:58:42.575Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('BRT.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\n# find leaf containing line 9242 content\nfor i,l in enumerate(leaves):\n    if \"karana-  m.  'Ende'\" in l or \"karana- m. 'Ende'\" in l:\n        print(\"LEAF\",i)\n        nums=re.findall(r'(?m)^\\s*(\\d{2,4})\\s*$',l)\n        print(\"standalone nums:\",nums[:20])\n        break\nEOF",
 "description": "Locate BRT karana leaf"
}
```


### [2026-09-14T01:58:43.725Z] TOOL RESULT

```
LEAF 273
standalone nums: []
```


## [2026-09-14T01:58:47.139Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('BRT.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i in (272,273,274):\n    l=leaves[i]\n    print(\"=== leaf\",i, \"head:\", l[:200].replace('\\n',' | '))\n    print(\"nums:\", re.findall(r'\\b(4[0-9]{2})\\b', l[:600]))\nEOF",
 "description": "BRT leaf column numbers"
}
```


### [2026-09-14T01:58:48.316Z] TOOL RESULT

```
=== leaf 272 head:   206  zu  aiulä  verwiesen  ist)").  —  i)  Tbem. —  6)  Zuletit  iF.  Fov  KZ.  ^7.  540,  —  7)  Ortho- grapbiscb  verunglückte  Wörter.  Anders  FüV KZ  35.  56  f.  Ich  halte  das  troti  IF.  /
nums: []
=== leaf 273 head: e  (3DPM.)  "und  seine vairyii  pairi.ianm  pairi-kSrayiis  "mit ;  (des  Landes)  Tiere  und  Menschen  be- einem  Metallstiick  sollst  du  einen  ringsum  wegen  sich  frei  einher"  Yt  io.  112-
nums: []
=== leaf 274 head: a-m.  (eine | 12.  ao;  —  «va  -iia'>  ai^hä  2?m9  Vt.  lO.  95;  '^^  Rebhul.n.  auch  als)  EN, | /p,  19; — ya~ia  VIS.,  yahmäi  nsitcahmäi  •   j,    kahrkäsa-   m,  'Geier':    '53  zannu- | nalmanq
nums: []
```


## [2026-09-14T01:58:56.937Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"akarana-\\|a-karana\\|akarana\" BRT.txt | head -20",
 "description": "BRT akarana entry"
}
```


### [2026-09-14T01:58:57.002Z] TOOL RESULT

```
3211:'sagen':  äla  (sSPfA.)  F.-K;  —  mit ui/i  is±):  aöaica  (iSPfM.)"'  uiti  V.4.47, N._J7.  a)  Pass.  'genannt  werden,  heissen', mit  dopp.  Nom. :  yäia  . .  akarana  anayra asaonö  sfif  aili  Yt.Ä48.
4247:uranfinglich' :  akarana  'ra  asaonS  sUs^sA.) YtÄ48;  F.  7.  a)  'ra  raocä  (iA.)  "die!
22690:•j. 'vayav-, 'vaya- ''m. 'Luft,  Atmosphäre', als  Gottheit'*':  'yus  bä  nqma  ahmt . .  avat •yus  .  .yat  «va  dqma  vayemi  yasca  äa%al sp»nts  mainyui yasca  da'^at  anrS  matnyus Yt.  1$.  43 ;  —  'yusys  upar5.kairy5  Yl  75. 4, 2 1 ;  3  (als  Vok.) ;  —  'yus  aurvS  *usiäj *yasts  d>r3ii.yaox3ürS ..\t.is.^^;  —  °yaos uparS-katryiiu  tarähätö  anyäts  dämqn  Y. 22.24,  Ytij.  o;  —  %wasahe  3^diätahe trvanaht  akaranahe  'yaos  upareJkairyeAe V./P.13;  S.J.21;  —  aaai  ti  -yö  (Vok.) yazamaidt  yat  tl  asti  sp>ntS.mainyaem  Y. Äj.  5 ;  —  '^  aurva . .  'yS  taxma  Yt.  15.11; —  t9m  yazai . .  uynm  vaim  (Akk.)  uparS.' iairlm  Yl/J.  5;  —  valm  aiavamm  .. valm  uparS.kairim  .  .  tardhättm  anyüis dämqn    Y.  25.  5,  S.  2.  2i;    Yt/J.  1';    —  .
26561:—  asmamm  ..  *gaä^Im  *gaH&yayä  stSis Vr.  7. 4.  a)  mit  GS.  aiaone{^^.  251  u.): yaca  upairi  (sd.)  iS  akarana  anayra  a^acnS Sil/  aSi  Yt.  Ä",  48;  —  ^antim  trvamm mainyava  stx/*asaonS data  .w(Sp.a76ni.) V.  2.  igPüZ.  et)  mit  vlspa--.  vTspqm asaenS  stim  .  .  mainynfm/ä  gaihyqmcä Y.  3S.i;Vt.  16. 1 ;-- vlspqm  asaons'stXm haitlmca  bavairUlmca  büsydntlmca  Y.  ip.g;
```


## [2026-09-14T01:59:01.651Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '4238,4256p' BRT.txt; echo \"---LEAFIDX---\"; python3 -c \"\nt=open('BRT.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\npre='\\n'.join(lines[:4250])\nprint('leaf', pre.count('\\f'))\n\"",
 "description": "BRT akarana context"
}
```


### [2026-09-14T01:59:02.819Z] TOOL RESULT

```
*)  Näml.  des  MaulähAk.  und  AaraMaiHyav am  Ende  der  Welt;  vgL  YL  79.96,  Bd.  30.19 und    PüEri. :    ia    rufän    afäc    ö  lau  dahend.     S.
•  j.  "anaomo  mananhe  kya  vTsäi  kaia kia  parö"  FrD.  (i.
Vgl,  West  SEE.  J.  356.
•  j.  an-aoäa-  Adj.  'dem  kein  Verderben droht,  unsterblich':  aurvantö .  .  mainyus.- ii^ar?^a  'shihs  Yt  70.125.
np.  vgl.   iiBs   'Unsterblichkeitstiank' }   s.  dazu Hbm.  PSt.  19,  AGr.  /.  99.
•  j.  an-ayra-  Adj.  (fem.  'rä-)  'anfangstos,
dby  Google
anaiSün
anaiwi.9r9tv5.gatav-
uranfinglich' :  akarana  'ra  asaonS  sUs^sA.) YtÄ48;  F.  7.  a)  'ra  raocä  (iA.)  "die!
anfangslosenLeuchten,  der  anC  Lichtraum":' vTspa  'ra  raocä-  usca  usraocayeitiY.2.^o\ PÜZ.;  —  "rd  raocä  x^aoJtä  V.  75.35;  J/.i, 2,  10,  P.j^,  Yt./2.35,  Y./6.6,  77.9, G.J.  6,  S.  2.30;  —  i/ram  mäuhe  hürS •ranqm  raocaukam  Y.  f.  i6|  Yt  ij.57;  — 'ralsra  raocShva  H.  2.  15.  a)  "ranqm
raolatfhqm  (näml.  ayan)  heUst  der  30. Monatstag;  S./.30;  vgl. 2.30,  Y.  16', 6;  — auch  ohne  raoc' :  pancaca  kaptailJm  paittl- hahyehe  (sd.)  xsa^rake  vairyehe  'ranqm A.j.g;  10.  b)  'ra  hmä  'die  anfangs - lose  Finsternis' :  täirlm  gama  frabarat  yg nars  drvatö  urva  'raih'a  tjmShva  nida^at H.2.33.
Pü.;  aiar;  (zu  »«);  aaerätt'},  s.  unter  'raorah'. —  >)  GelW. }.  BHOxtÖ  N,  ^ :  lies  anakaxli.
•  j.  anaiKm  Adv.  'in  der  Quere':  cvat. . äps  yat  frätal,car}tayä  .  .  druxi .  .  /ras- naoilit .  .  ^rigäim  nyäpim  navagaim  pait- ySp}m  xsvas^aim  an'  ".  .  drei  Schritte stromabwärts,  neun  stromaufwärts,  sechs quer  über  den  Strom"  V.  tf.40.
Ob  AbleiL  aus  anaf     Sf.  Komm.  /.  199.  — Pü. :  Aal  killt  bilät.
j,  aitadya  N.  56:  lies  a^a.
•  j.  anaiSyä-  f.  'Bann,  Interdikt':  cvanl>m drajS  zrviln^m  aitiha  z^mS  (%t~,  3  b)  'ya (NS.)^a/  ahmt  .  .  V.6.1;  i.
Et.?— ~PQ.]  at,r./Üä>,{?\  crU  fit  ci  SnlitSm^
•  j.  ana  parö  adv.-artigcVerb.  'vordem'(?); &!/  ana  parö  dus.hr?la  (sd.)  aat  ana par3  ma'^^rö  spmtd  S.2i.^(^).
---LEAFIDX---
leaf 99
```


## [2026-09-14T01:59:12.352Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"endlos\\|unbegrenzt\\|ohne  Ende\\|ohne Ende\" BRT.txt | head -20",
 "description": "BRT endlos"
}
```


### [2026-09-14T01:59:12.439Z] TOOL RESULT

```
3013:m^„a«il,  ymg  äB,',ng  -iata  «ain,«,-..  'I-  «rl;"«"«-  Adj.  (fem.  -M-)  'endlos';
28347:%warStai  'rant  (DS.)  Yt  5.129;  — ^warstahe  'rä''>  ayu  (sd.)  Yt  8. 1 1.  a)  in der  Gerichtssprache  'Zeit  der  Verhandlung, Termin':  galumca  *varas{si.)ia  'rvatamca F.  4c,  2)  'Zeitabschnitt':  J  rapihwin^m 'rvaium  "um  die  Mittagszeit"  Y.g.  11, YLÄiSj  —  vtspfm  aOim  paiti  'rvän^m attanm  urva  iä/ayäj  {sd.)  P.J7; — yavat aSahmya  *tru'>  staotanqrn''>  yesnyanqm dädräjdil  "bis  dass  du  im  Lauf  dieser Zeit  die  StY.  auswendig  gelernt  hast" N.  J2.  3)  'Zeitdauer':  Üvantim  'rvarum mainyazia  stii  . .  data  as  (Sp.  276  m.)  "wie lange  ist  es,  dass . ."  V,  2. 1 9  PilZ.;  7. 3 ;  — cvantpm  dr3jB  (sd.)  'rvänim  aiiihä  %3mB (Sp.  1664  u.)  anaiiya  V.  6.  i;  7.  45; —  :^ar?nil  . .  yat  upatthalat  haofyani^m .  ,  danffmcii  aipi  sruSium  Yt  ig,  26; y.  53,  Y.  62.  3;  —  da%al  sptntS  matnyus da^at  'rUne  (LS.)^'  akarane  ". .  in  der unbegrenzten   Zeit"    V.  ig.  9.  A)    als
```


## [2026-09-14T01:59:16.407Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '3008,3020p' BRT.txt; python3 -c \"\nt=open('BRT.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nprint('leaf', '\\n'.join(lines[:3013]).count('\\f'))\nt2='\\n'.join(lines[:9242]); print('leaf karana', t2.count('\\f'))\n\"",
 "description": "BRT a-karana- entry"
}
```


### [2026-09-14T01:59:17.640Z] TOOL RESULT

```
•  j.  akana-  n.  'Behälter',  bes.  der  Pfeile, 'Köcher":  ta?n3u/(sd.)  maj  'na  maj  ^risqs ayS.aynli/  V.  14. 9.
itip.  (Pü.)  ia/ißr  d.  i.  Tfeilbehäller';  s.  dazu G<;r.  SBayrAW.  /Sgo.  2.  51,  Dst.  ZA.  2, 215,  HOKN  NpEt.  2S2.  In  der  FüErl.  zu  Yt. 6.  5  wird  iattlir  vom  Behält«  der  Keule  ge- braucht (Dst.  £llr.  3.  288).
•  j.  akayaSa-  m.  £N.  eines  Gläubigen: 'üahe  puöanqm  aSaonö  \t,  ij.iij.
Ob  a-iayaia-  (sd.)f
"aber   ihr    seid    dem   schlechlen  Denken :  •   j-  »tav-   m.  'Scheere,   scheerenartige entsprossen,  ihr  Z>a^t■a  alle,  und  er,  der  . .,   Waffe' :    nött   dtm  .  .  avasy/tl  notl    'Aavo und   der   Lüge   und   der  Hoffart"  Y.js.KNP.)  nSil  ..  Yt.I.iS. 3').         A  a)  mit  mainyav  m.  'der  bösei     ?';'  -?•■•*»•'/.  ^p«--  »»**.  "!•:  *''« Geist,  sva.  anra- matnyav:  hyat  vä  aka\      .       ,  ,  ■,.    ,r  ■,!>,,
m^„a«il,  ymg  äB,',ng  -iata  «ain,«,-..  'I-  «rl;"«"«-  Adj.  (fem.  -M-)  'endlos';
auch    ohne   ™/.,w-:    /,/>»»/ (sd.)    ■i.l\'"'^"'''  l"'''   "'■■H'l.    Y./J.-i    -
,S.    "    Ab)mit.,»»»i.n.'Denken'^&,  f «■'"''  ''f. ^'V*«!:  "  <">"'"">  •'!"• Ma^aA.  Name  eine.  DaKa,  Gegners  des  |  «»«  A^f.) "  Vr.  ,*.  2.  ,)   raumhch,
r>iuM^,„i:  är,ivi  ..  ah,ä  ^^«J^,.«.'!  ^S»'  •'»"  »'»  *''''■  >"«•   »»  a"™  Ecken
'ist  *a  iyqsi^d.)  manaJiho  Y.47,  5J';-
I  und  Enden,  überall,  über  und  über'  (ni
-«ji      «    »yai\r,\i.)    munav/iir    i.ii.i.\-, —  \  Ttr  i-  j   ■       s
.A;./^-   mainyus-  a^t>m  fra^har^tayat   ^0- ^"Zlll.  i'^l'l^^TaZTri'l'.V^
leaf 62
leaf karana 273
```


## [2026-09-14T01:59:34.614Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('BRT.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i in range(58,68):\n    l=leaves[i].strip()\n    nums=re.findall(r'\\b\\d{1,4}\\b', l[:300])\n    print(i, '|', ' '.join(l.split())[:150])\n    print('   nums:',nums[:12])\nEOF",
 "description": "BRT leaves 58-67 heads"
}
```


### [2026-09-14T01:59:35.774Z] TOOL RESULT

```
58 | — tf/ 'jitum Ä>t- '■ j ■ '-'"■:'•'- 'J- "H- »"» .. - ■ dr^nili yl ^./üji^n ■>d.^ .:.:J«f <h-t; .j-Jir /■.jj- . aok- V. -sprechen". Praei 33 -Itei mt V
   nums: ['33', '37']
59 | PÖ.: öi, Sü,: ialam. DST. ZA. r. 328 meint: "siaolä aojäi 'j'ai force comme cbnntre'". — 5) Pü.: apat rasllan. — 6) Hds. uxla. '). aogar- n. 'Kraft, S
   nums: ['328', '5', '6', '13', '13']
60 | � 'jönghval Y.4!j.i6. ai. djasvant- Adj. — Pfl.: Siämand. — i) VgL asi.asjah-. — ») So Fl, Mfl, vgl. PI4, NA. 'jaakvanitm. • j. aojamna- Adj. (fem. °«
   nums: ['4']
61 | 128; 129—132*, ASn. aus tava: — 0 Vgl. toa mit No. 3. • j. aoman-" Adj. 'helfend, beistehend': tä nS . . %räy?nle . . 'mtta (IS.) ahura mazda sraoiaea
   nums: ['128', '129', '132', '0', '3', '146', '0', '2', '5']
62 | ��^^ ^ _ „ Vgi. SBE. 4y. 13. Er war der beraten sich über meinen Untergang" V., Kanzler des Kavay Vsan, 19-i'y S.-Js'PÜZ.i?) A) als Da^'a: ktm \. aifs
   nums: ['13', '19', '10']
63 | Y./J.-i - ,S. " Ab)mit.,»»»i.n.'Denken'^&, f «■'"'' ''f. ^'V*«!: " <">"'""> •'!"• Ma^aA. Name eine. DaKa, Gegners des | «»« A^f.) " Vr. ,*. 2. ,) raum
   nums: ['2']
64 | farl aesmtm N. /OJ, Pü.: fehlL • j. aj-a- i) Adj. (fem. -ya-') 'schlecht, böse, schlimm'; a) von Lebenden: vJsp?n crf>m tbisyantpm A./. 10; — aivaAe *
   nums: ['10', '7', '11', '37']
65 | jrya- Adj. (fem. ya-) 'der erste' an Qualität (usw.): nit»n>m . . maö^mjtn rim stagr»m (sd.) arijö V, 7. 41; 43'; — uitraAe k?hrpa °yehe P.^2; — aspah
   nums: ['7', '41', '43', '2', '9', '37', '37']
66 | gestellten Sinn besänftigt er durch M." Yt. /o. log, PPfP. einer Basis jJJJfl'j-, s- Erneilcrung (/-Aorist, vgl. xlnaosta, xiiiaosiii) des \'. ilnav-.
   nums: []
67 | �� a-Jyätay- £ 'Nichtleben': hyat ti him mainya )asa:t>m (sd.) paourvJm dazdi gannlä 'yiiltmin ydiilal . . apimtm . . ". . da setzten sie fürs erste d
   nums: ['4']
```


## [2026-09-14T01:59:52.108Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"kanâr\\|kanār\\|kanar\\|karân\\|karān\\|karan \" HRN.txt | head -30",
 "description": "Horn kanar/karan"
}
```


### [2026-09-14T01:59:52.161Z] TOOL RESULT

```
7379:a\kanarak.
```


## [2026-09-14T01:59:55.124Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '7360,7400p' HRN.txt; echo \"=LEAF=\"; python3 -c \"\nt=open('HRN.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n'); print('leaf',' '.join([]) or '\\n'.join(lines[:7379]).count('\\f'))\n\"",
 "description": "Horn kanarak context"
}
```


### [2026-09-14T01:59:56.503Z] TOOL RESULT

```
32, 721; 'd\. karnd- 'mit verstümmelten (gestutzten)
Ohren' (Geldner, Vedische Studien I, 138).
kurd. LW. ker 'taub'; af/. künr; oss. kurmafä 'die
Tauben' (Matth. 11, 5, Hübschmann, No. 164); bei.
*) Sogar Mass*, z. B. Vis und Rämln 67, Vers 2.
^) Das u ist jung, vergl. ai. katamä-^ mäz. kadänu
*j Das II kann auch erst neupersisch sein , vergl. phlv. katär^
aw. kafära-,
*) Käs. V. Ä-e, Q. kiyd^ kl etc. (s. v. ;^äMe) haben das bereits
neupersische d noch in y verwandelt. Solche zweite Lautverschiebung
findet sich auch sonst. Ein Beispiel für viele: Käs. tnelä, mele 'Büffel-
ochs* (s. V. kel) geht auf np. merde zurück (hier ist rd noch nach-
träglich zu l verschoben).
^) So bekanntlich im Türkischen immer geschrieben, aber k'ai/a
gesprochen.- 189 -
LW. karr, Jcar, n. l^ar (120); w^./. LW. kar^ sar. ctum,
la/ni. kannä.
). keräu Ufer, Seite, Ende', keräne, meist kenür^ keyiüre.
aw. karana- 'Seite, Knde*; phlv, kaiiär, kanärak,
a\kanarak.
oss. Mro« Endo' (155); LW. kurd. af/. kinür,
7. kerden 'tun , inaclien', Praes. kun-ent , kuj/dnlden 0,
kunis, kunist (»Sahn. II, 048 Anm. 11, (/alc), kunisn
(Wörterbücher).
ap. y'kctr-, kiinavahy *tnn , maclien'; aw. K/kar-,
kerenaoiti] yihlv. kartan, kartär, kunäk (vergl. Justi,
ZDMG. 40, 287), kun(i)sn, päz. knnom; ai. l^/:ar-, k^ntdi.
kurd. Ä:2?7w, Praes. A-em 'machen'; oss. d. känmi,
t. /'ä/?//* (152); bei. kanag, n. XVi//a/ (185); wa;^. rar-
am, siyn. kin-am, sar. kan-am.
Die np. Dialekte haben den J^-aesensstamm Aim-
nicht (vergl. aber gel. /j«f/e« (Inf.) neben kei\hn).
Vax V^kar- 'machen* gehört auch Kns. Q. ha\ugör(leii,
d. i. vi \-kar', in der Bedeutung von slkä/foK
8. fcei* 'Huhn' (AM. S. 203 Zeile (>), kurg 'nicht mehr
legendes, geiles Huhn *^).
Kas. karg, kerk (s. v. mi(ry).
aw. *kahrka- in kahrkam- *Hühn«»rfresser (OtMor)';
phlv. kark; ai. kfka\mku' 'Hahn'.
kurd. kurk 'Huhn'; afy. cirg; oss. /•«;•/• 'Ih'nno,
Huhn (154); wa;^. kork,
=LEAF=
leaf 210
```


## [2026-09-14T02:00:06.181Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"kanārag\\|kanarag\\|kanār\\|kanar\" PHD.txt PHD_mackenzie.txt NYB_vol2_glossary.txt | head -20",
 "description": "MacKenzie/Nyberg kanarag"
}
```


### [2026-09-14T02:00:06.239Z] TOOL RESULT

```
PHD.txt:189:áhüg [TYBA < A ру; ”hwk! | MQyhwg, N āhū] gazelle. ahunawar [hnw!] the holiest prayer, beginning Yadā ahū wairyē. a-hunsand [Phwnsnd] dissatisfied. ^h : dissatisfaction. ahy [KZ Y < А k-zy | М hy] soon(est), first. ajģahān [>20/?л! | М ieikin, N azgahan] lazy, indolent. “АҺ: laziness, indolence. ak P! | N dk] evil, harm. -ak LIN ~] diminutive suffix. a-kámagómand [k mk’ wmnd] unwilling. a-kanārag ['kr?]k! | M ?qn’rg] unlimited, boundless. ~ih: boundlessness. a-kard Pārt! | (M °gyrd)] not done, undone. Akoman ['kwmn! | М ?qwmn] Evil Thought, an arch-demon, akómand ["£wmnd] evil, harmful. alā [Py] oh! alas! Аар [STLA, STRA < A £t ;?lk! | (М rel side. alálag PPH! | N lala] anemone. ālāy-, v. ālūdan. Aleksandar Piksndl | M *Ixsyndr, N Iskandar] Alexander (of Macedon). almās(t) Pim?s(t') | (M ?rm?s), N almas] steel; diamond. аадар [?/wtk'] defiled, polluted. АҺ: defilement. ālūdan, ālāy- Photn!, *Pd- | (M ?rwd), N ~] defile, pollute. Aluh Plwh | M "If, N ~] eagle. Xum [lum] millet. N~ amā [LNE < A l-nh | М ?*°h, N má] we, us. Amadan, āy- [Y ATWN-tn! < А y twn, V*th | M?mdn,?y-, N ~] come. amahraspand [?mhrsbnd | M (?)mhr’spnd] a Holy Immortal, a-mar [ml] countless, innumerable. amar [ml | N ~] reckoning, consideration. āmār- [?m?1-] reckon, calculate. ~išn: reckoning. a-marag [mlk') countless. amaraģān [?mlk’n'] generality, commonalty. ~ig [-yk'] general. ~iha [-yh’] in general, generally. a-marg [mig] deathless, undying. ~ih: deathlessness, immortality. ámárgar [?m’lgl | N ~] reckoner. amāwand [?m'wnd] powerful, strong.
PHD.txt:424:kaman [kin’n' | = M, N ~] bow. 5; 7 ~dar [-d'] | N ~] archer, bowman. ha er mae 4 ba kamar [kml | N —] waist; belt, girdle. ~-band [-bnd | N ~] belt. kāmģār [Emil | P k?*mg?*r, N ~] powerful, absolute. kamist [Amyst'] least. —jh: pad ~ih, at least. kāmistan, kām- [YCBEN-stn' < A ysbh, V shh; k*m-(y)stnt M k*m-yst] want, desire. kám|-rawág [km izvb*k! | N ~rawa] successful. ~-Z1(w)isn [-zywsn'] free, independent. kam-zór [kmzwl | N ~] weak. ~ih: weakness. kan-, v. kandan, kanar [kwl | N ~] side, edge; embrace. ~ag [-k' | M kr?rg, N ~a] edge, limit, boundary. --agómand [-k’wmnd | M -gwmnd] limited, finite. kandan, kan- [HPLWN-tn! < А V hpr; kn-dn', -tn! | M knd, N ~] dig; raze, destroy. kanig [knyk! | M knyg] girl, maid. kanizag [knyck! | M knycg, N kaniz(ak)] — kanig. kantigr [kntgl] quiver. kāpūr [ро | Ar. kāfūr] camphor. kar-, v. kardan. 1Kar [21 | M Pr, N ~] work, deed, affair. ~ framüdan: put to use. 2kàr [%'7], pl. —àn: (other) people. зкаг [%'/] butter. kār-, v. kištan. karafs [klips | N ~] celery. kār-āgāh [РА | N ~] skilled, experienced. ~ih: skill, experience. karak [krk! | N ~] quail. karan [kľn' | P bein, N ~] side, edge, end, limit. kārawān [%?/zv?x! | P k*rw'n, N kārwān] caravan, military column. ~ig [-yk! | N ~7] caravaneer, traveller. karb [klp] priest hostile to Zoroaster. karbāš [5/0 | N karbas, etc.] lizard. karbunag [k/pnk!, klbnk'] lizard. kard [krt! | M kyrd, N ~] action; matter, affair. кага [SK YN A < A skyn’; Kit! | N ~] knife. ikardag [kltk!] division, section, portion. *kardag [krtk!, kltk! | N karda] action. kārdāg [k'/d?k'] traveller, wanderer, migrant. kardaģān [Art-, Rlt&?n! | M kyrdg”n) action. kardagàár [Artk?l | M kyrdg’r, № ~] mighty. C 6084 E
PHD.txt:1053:boundary kanārag, wimand,
PHD.txt:1055:boundless akanārag.
PHD.txt:1734:edge kanar(ag), karán; sharp — téx.
PHD.txt:1753:embrace āgēš, kanar.
PHD.txt:2637:limit kanarag, karan, saman, wim- and.
PHD.txt:5037:kan- har(w)! kanār, kennir kanāragūmand kanārag kennārsrāy kóx&- kūxšīdan kox&isnig kóxXi&n kawādak köv
PHD_mackenzie.txt:970: a-kanara~ ['kn'lk l I M 'qn'rg] unlimited, boundless.
PHD_mackenzie.txt:3187:kanar [kn'll N --] side, edge; embrace.
PHD_mackenzie.txt:6092:boundary kanarag, marz, saman,         broad pahn, wehm.
PHD_mackenzie.txt:6096:boundless akanarag.                    bronze brin}; hrinJen.
PHD_mackenzie.txt:6097:boundlessness akanaragih.              broom gyag-rob.
PHD_mackenzie.txt:6479:edge kanar(ag), karan; sharp""", tex.        entrails rodigan.
PHD_mackenzie.txt:6498:embrace agos, kanar.                         especial madagwar; v. special.
PHD_mackenzie.txt:6994:limit kanarag, karan, saman, wim-        lucerne aspast.
PHD_mackenzie.txt:6996:limited brin, kanaragomand, wiman-       lunch cast.
PHD_mackenzie.txt:7842:tyrannous sezd(en), staft.               unlimited akanarag.
PHD_mackenzie.txt:9613:kanar, kennar                   \....,~        kayak                       \~,
PHD_mackenzie.txt:9615:kanaragomand          're;,..,~,~              ker                        ~,
```


## [2026-09-14T02:00:12.697Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"kanārak\\|kanarak\\|kanār\\|karān\\b\" NYB_vol2_glossary.txt | head -10; echo \"---HUB---\"; grep -n \"kanār\\|kanar\\|karān\\|keran\" HUB.txt | head -10",
 "description": "Nyberg + Hübschmann kanar"
}
```


### [2026-09-14T02:00:12.784Z] TOOL RESULT

```
347:a-kanārakēh boundlessness, endlessness, of Ohurmazd 637-28,
1064:nē būt 675-26; bavēt... Zartuxst it must be Z. 6023; nē yatük: [YHWWN-#'] bavat he cannot possibly be a sorcerer 3774, v. Grammar 53. — 3. In the 3d p., together with a subst. virtually in dat., or with a pron. in cas.obl., it expresses the notion ‘to have’, e.g. õi kē-š zan nē būt he who did not have a wife 101!; amdvandéh ... i-m būt the vigour which I had 341; -t dānākēh bavét wisdom will be allotted to thee 595; duxtar i varzēkarān én hunar ... i to hast ne bavet a farmer's daughter cannot have such an ability as thou hast 18520-21; with rád as in NP: Pdpak ràd hec fradand nē but P. had no child 19-7. — 4. Together with verbal or other nouns it forms periphrastic verbal expressions: (7) matār būt hēnd who used to go 61”; nikeräi (g. v.) bavét 8214; tō . . . ästisn ne but hah thou wouldst not have subsisted 3515-16, 3421-22; _$ hàm zan... ayyät bit he remembered that woman 1111-12; 123-4; -§ vat hayyär bavét the wind helps him 25; Ohurmazd ziyān ne bavēt O. will suffer no harm 7727; v. also äkasi, hangir- tikeh. — 5. With preverbs: andar ~, v. andar; — apäc ~ to become again 7714-15, 10021-22, 12025; to come into existence again, to be restored to life 46°. 10416-26; to be left, to remain 39277. 4416; — apäk m = apāc ~ 3423; as to 161-7, 2426-27, v, apäk; — apar ~ to be imparted to 80%; — fräc ~ to recover (hac from) 5419.12, 6022; — 6 ~ to approach, to come on 65; to pass into 4216-17; — 6 ham ~ to be put together, to be formed (from different elements) 4317; v. also hambavisneh. — 6. As an auxiliary vb. added to the pt. pret., būt forms the pluperf. in dependent clauses, as against ēstāt in independent sentences: pas hac han + Artaxser han kirm ēzat būt after A. had slain this
1709:griftar [glpt’]] a p. who "catches”, i.e. incurs, liability: 1. ku pat dat 1 dévan ~ né bavé lest thou shouldst be subject to the law of the demons 6916-17; [ruvan pat ménoyan pat kunišn aržānīkēh ~ kunénd in the heavenly world they (the gods) call the soul to account according to the value of her deeds Mx ch. 382-6 (~ kunénd = girénd 65°, v. griftan)]. — 2. condemned to (šahrē-karān, v. s. v. kar) 92; prisoner: ~ kartan to imprison, to capture 615; [more general, to catch hold of: api-§ — kunēt u apāc 6 rah i yazdān āvarēt Mx ch. 1525]. — Cf NP gér?ftàr; v. also a-griftär.
1808:ham-biitan to be together with, to follow: či kanārak i... apar hambüt [hmbwt'] hom I kept on together (with him) all
2193:kanürak [kn'lk'; ŠTL”] boundary 512’. 529.11, — MPrs kn’rg ‘side’; Paz. kanāra; NP kanärah ‘side, shore’.
2556:mihr [mtr'] 1. n. pr. the Aryan god Mitra, Av. Midra: ~u Srēš u Rasn 1215; ~ u Zurvān i akanārak u menčyč datistan 77-12, ~ zg"'"atài névak, Dahman Afrin 9213, ~ yazét u x"aršet 961! ; atur burzen ~ the third of the three imperial fires 11%. 2°, symbolizing the class of the cattle- breeders and farmers 2° (cf Av. [1430] Midrē yö vouru.gaoyaotiš); — existing in all animal beings 965-%; — Dadv pat ~ the name of the 15th day of the month 9715-16, — 2. the sun 78. 317. 7913-18, — 3. abstr. friendship, loyalty: — u došaram i apāk čišan 87°; ~ + amāh 98; ~ i čvak 6 dit 119; vehän ... ~ däst u dosteh varzit 5526-27, — Av. (1183 sqq.) midra-.
7233:kālbad, kālbud: kalpaš kāmīdan: kāmistan kanār, karān: kanār kanārah: kanārak kanīzah: kanīcak karavah: *karbēk kārd: kārt
---HUB---
9575:p. 244 vermuthet; kanar , kanara neben karan, karana
9577:schon paz. kanara 'border' Min. Gl. 116, Shk. 258 und phi.
9578:kanaruk, akanarak Gl. and Ind. 31; hizisk, bijisk 'Arzt',
```


## [2026-09-14T02:00:18.207Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '9565,9585p' HUB.txt; python3 -c \"\nt=open('HUB.txt',encoding='utf-8',errors='replace').read(); lines=t.split('\\n')\nprint('leaf','\\n'.join(lines[:9575]).count('\\f'))\"",
 "description": "Hübschmann kanar context"
}
```


### [2026-09-14T02:00:19.386Z] TOOL RESULT

```
Ueber hi aus rt und r& (= iran. rd^ und rs) s. § 89,
97, 102.
Die iibrigen Lautgruppen, bestehend aus r mit fol-
gendem Konsonanten, bleiben: marr/ *Mann ^^ ap. war%a- ;
marg *Tod* = zd. mahrka-, curb 'fett' = phi. carp-, nmry
Vogel' = zd. mereya-] warz 'Mark*, vgl. arm. marzpan
*Markgraf', carm *Feir = zd. careman- u. s. w.
Umstellung von Konsonanten verschiedener Silben hat
stattgefunden in: hargiz jemals* neben alterem hagirz, phi.
hakarc, wohl mit Anlehnung an har jeder , wie Horn
p. 244 vermuthet; kanar , kanara neben karan, karana
(Fird. I, 247, 71; 251, 132) 'Ufer, Ende = zd. karana-,
schon paz. kanara 'border' Min. Gl. 116, Shk. 258 und phi.
kanaruk, akanarak Gl. and Ind. 31; hizisk, bijisk 'Arzt',
arm. bmk aus "^bisizk, skr. bhi§aj-.
Kapitel 33: Abfall der aniautenden Silbe.
§ 164. Die anlautende Silbe ist abgefallen in: dar
hinein, in' -— andar, ap. aniar, dazu darun = andarun;
darx^'ar = andarx^ar (oben p. 60); digar = dadigar
anderer', ap. diivitiyam -[- *A:ar«m H. 595; Partikel me ■=
/ta/w^Sal. Shuk. Gr. p. 61, H. 1104. oben p. 106.
leaf 277
```


## [2026-09-14T02:00:31.722Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Kuru\\|Kūru\\|Ku-u-ra\\|Cyrus\" KNT.txt | head -30",
 "description": "Kent Kurus"
}
```


### [2026-09-14T02:00:31.782Z] TOOL RESULT

```
306:C = Cyrus the Great D = Darius the Great
358:67. Тнк Mepran Рглгест was the language of the great Median Empire, which at the death of Cyaxares in 594 extended from the Indus to the Aegean Sea; the last Median ruler was Astyages, son of Cyaxares, who in' 559 was conquered and deposed by his grandson Cyrus, son of Cambyses King of Persis and of Mandane daughter of Astyages. The new ruler naturally took over the Median chancellery and the Median royal titles, and their influence is still seen in the language of the OP inscriptions of Darius and his followers.
424:Grotefend recognized correctly that the names of two different kings were followed by titles, ‘great king, king of kings’, and then a third simi- lar title in the one which was lacking in the other; that then followed the name of the king’s father, who was the same person in one inscrip- tion as the king in the other, and that in the other the father did not bear the title king. He decided upon Dartus, whose father Hystaspes had not been king, rather than upon Cyrus, since Cyrus and his father Cambyses had names be- ginning with the same letter! whereas the cor- responding two names in the inscriptions began with different characters; he thought the name of Artaxerxes to be too long. Thus he saw in the three names Hystaspes, Darius, Xerxes, in the transliteration of which he used the later Iranian pronunciations:
426:Thus he had identified, for all but the inherent a, the characters а, и, z (his kh), i, d, p, 7, s, $ (his sch), and elsewhere he identified f. But his reliance on the later pronunciations misled him sorely, and of the 22 different signs in DPa and XPe he got only 10 correctly, and even for two of these he admitted two values each (a and e, p and b). Apart from the three names, ‘king’ and 'great were the only words which he identified correctly; later (1815) he identified the name ‘Cyrus’ in CMa. But the remainder of his read-
427:1 As it happens, Cyrus and Cambyses do not begin with the same letter in OP, but with k” and ke respec- tively; but Grotefend could have dismissed the Cyrus line on the ground that Cyrus’s father and Cyrus’s son were both named Cambyses, but the first and the third of the dynasty in these inscriptions bore different names.
471:Tt is uncertain also when this Old Persian system of writing was invented. The extant in- scriptions are largely those of Darius I and of Xerxes, and it is tempting to ascribe the inven- tion to the orders of Darius when he wished to record the events of his accession, on the Rock of Behistan; but there are three inscriptions of Cyrus, as well as one each purporting to be of Ariaramnes and of Arsames. These last two may have been set up as labels to small monuments or other objects of a later period;? the orthography
472:1 For a critique of these theories, see Wb. KIA 1у-1х. 2 Ariaramnes was great-uncle of Cyrus and great-grand- father of Darius 1; Arsames was son of Áriaramnes and grandfather of Darius. Note that the two inscriptions are both on gold tablets and found at or near Ecbatana
473:points to approximately the time of Artaxerxes П? Of the inscriptions of Cyrus, one is very fragmentary, and the other two are brief labels; yet as they were inscribed in the palace which belonged to Cyrus,‘ at Pasargadae (Murghab), they show that the OP cuneiform syllabary existed and was in use in Cyrus’s time!
477:(Hamadan) in Media; though the two kings are spoken of in them only as ‘king in Parsa = Persis’, which was quite distinct from Media. They may have been set up in the time of Artaxerxes П as part of an anti-Cyrus propaganda, since Cyrus the Great had dethroned Arsames, and Cyrus the Younger came very near de- feating and killing Artaxerxes II at Cunaxa (cf. JAOS 66.206-12). The gold tablet A?Hc may have been a third in the same series; all three are in Old Persian only. *Cf. especially Schaeder, SbPAW 1931.636-42. 4 They are hardly to be ascribed to Cyrus the Younger, despite Wb. ZDMG 48.653-65 (cf. also KIA lxvii-bax) on CMa, which alone was known to him; for the opposing view, cf. Hz. Klio 8.1 ff. * Though perhaps not much used by him. The other three known inscriptions of Cyrus the Great are in Akkadian; but Strabo 15.3.7-8 (page 730), on the authority of Onesicritus, states that the tomb of Cyrus at Pasargadae bore at least two inscriptions, one being bilingual, Greek and Persian. We need attach no importance to the identification of the languages by Onesicritus, but the account indicates that Cyrus had inscriptions engraved in more than one language; in which case it is unlikely that his own vernacular was omitted. Cf. JAOS 66.206-12; but also Hinz, ZDMG 96.343-9.
3048:S909. Тнк POSITION or THE GENITIVE. A geni- tive used as a genitive (not in a dative use), and depending upon a noun or adjective, precedes that noun or adjective, unless the genitive 18 attached to its noun by the article, in which instance it fol- lows: DB 1.4 mana pitä ‘my father’, but DB 2.27 kara hya тапа ‘my army’. The exception is only seeming in DB 1.9f VIII manā taumáyà tyaty paruam zšāyaðiyā аһа ‘eight (there were) of our family, who were kings before’; for amézam tau- туӣ is an appositive, equal to ‘(members) of our family’, cf. DB 1.28 Kabüjiya пата Kiraus puça amüxam taumdya ‘Cambyses by name, a son of Cyrus, (а member) of our family".
3291:CMa = Cyrus, MunGHAB a: 5 ог more copies of a trilingual inscription, OP two lines, Elam. and Akk. one line each, on columns and pillars of the palace. Wb. ZDMG 48.653-65 (1894), KIA xxvii-xxix, Ixvii-lxix, 126-7 (1911); Hz. Klio 8.00 (1906); Jn. Persia Past and Present 281-2 (1908); Tm. Lex. 55-6 (1908); Sen, OPI 1 (1941); КО Кеп, JAOS 66.209 (1946).
3292:CMb = Cyrus, Мувонав в: A number of
3294:CMc = Cyrus, Мовонав c: А trilingual inserip- tion, each version in one line, on the folds of the king’s garments in three doorways of the palace; the OP text now entirely destroyed. Hz. AMI 1.14-6 (1929); ApI 2 No. 2 and Plate 1 fig. 2 (1938); RGKent, JAOS 66.209 (1946).
3450:CMa = Cyrus, MunaHAB (PASARGADAR) А, 1 adam : Kürus : xSaya 2 уа : Haxamanisiya TRANSLATION or CMa: I am Cyrus the King, an Achaemenian.
3451:CMb = Cyrus, Мовонав в. 1 Kūruš : xSdyabiya : vazraka : Kabijiya 2 hyd : zšāyaðiyahyā : puça : Hazdmani siya : З айу : уада... 4... ... akutà ...
3454:TRANSLATION oF CMb: Cyrus the Great King, son of Cambyses the King, an Achaemenian. He says: When ... made ...
3456:TRANSLATION or CMe: Cyrus the Great King,
3568:610. 1.26-35. Saith Darius the King: This is what was done by me after that I became king. A son of Cyrus, Cambyses by name, of our family— he was king here. Of that Cambyses there was a brother, Smerdis by name, having the same mother and the same father as Cambyses. After- wards, Cambyses slew that Smerdis. When Cambyses slew Smerdis, it did not becomeknown to the people that Smerdis had been slain. After- wards, Cambyses went to Egypt. When Cambyses. had gone off to Egypt, after that the people be- came evil. After that the Lie waxed great in the country, both in Persia and in Media and in the other provinces,
3570:$11. 135-48. Saith Darius the King: After- wards, there was one man, a Magian, Gaumata by name; herose up from Paishiyauvada. À mountain by name Arakadri—from there XIV days of the month Viyakhna were past when he rose up. He lied to the people thus: “I am Smerdis, the son of Cyrus, brother of Cambyses." After that, all the people became rebellious from Cambyses, (and) went over to him, both Persia and Media and the other provinces. He seized the kingdom; of the month Garmapada ІХ days were past, then he seized the kingdom. After that, Cambyses died by his own hand.
3572:$13. 1.48-61. Saith Darius the King: There was not a man, neither a Persian nor a Mede nor anyone of our family, who might make that Gaumata the Magian deprived of the kingdom. The people feared him greatly, (thinking that) he would slay in numbers the people who previously had known Smerdis; for this reason he would slay the people, “lest they know me, that I am not Smerdis the son of Cyrus." Not anyone dared say anything about Gaumata the Magian, until 1 came. After that I besought help of Ahuramazda; Ahuramazda bore me aid; of the month Bagayadi X days were past, then I with a few men slew that Gaumata the Magian; and those who were his foremost followers. А fortress by name Sikayauvati, a district by name Nisaya, in Media — there I slew him. I took the kingdom from him. By the favor of Ahuramazda 1 became king; Ahuramazda bestowed the kingdom upon me.
3786:son of Cyrus." Thereupon the Persian army which (was) in the palace, (having come) from Anshan previously—it became rebellious from me, went over to that Vahyazdata. He became king in Persia.
3906:and the same year after that I became king. XIX battles I fought; by the favor of Ahuramazda I smote them and took prisoner IX. kings. One was Gaumata by name, a Magian; he lied; thus he said: ^I am Smerdis, the son of Cyrus;" he made Persia rebellious. One, Agina by name, an Elamite; he lied; thus he said: “I am king in Elam;" he made Elam rebellious. One, Nidintu- Bel by name, а Babylonian; he lied; thus he said: “Т am Nebuchadrezzar, the son of Nabonidus;" he made Babylon rebellious. One, Martiya by name, a Persian; he lied; thus he said: "I am Imanish, king in Elam;" he made Elam rebellious. One, Phraortes by name, à Mede; he lied; thus he said: "I am Khshathrita, of the family of Cyaxares;" he made Media rebelhous. One, Cicantakhma by name, a Sagartian; he lied; thus he said: "I am king in Sagartia, of the family of Cyaxares;” he made Sagartia rebellious. Опе, Frada by name, a Margian; he lied; thus he said: “I am king in Margiana;" he made Margiana rebellious. One, Vahyazdata by name, a Persian; he lied; thus he said: “I am Smerdis, the son of Cyrus;” he made Persia rebellious. One, Arkha by name, an Armenian; he lied; thus he said: “T am Nebuchadrezzar, the son of Nabonidus;” he made Babylon rebellious.
4823:| | Cyrus THE GREAT* Hystaspes*
4831:SOGDIANUS Darius II Norgus* 425-4 424 424-05 po pes | Cyrus the Younger Artostes d. 401 | Arsames
4838:a, States that there had been eight kings in their family before him, and that he was the ninth in order. We must count them thus: 1 Achaemenes, 2 Teispes, 3 Cyrus, 4 Cambyses, 5 Cyrus the Great, 6 Cambyses, 7 Ariaramnes, 8 Arsames, 9 Darius. The last three belong to the younger line of Áriaramnes, while Nos. 3 to 6 belong to the line of Teispes' older son. Hystaspes father of Darius is not included in the count, because he nowhere receives the title of King, even when mentioned as father of Darius—whereas the other kings all give to their fathers the title King in statements of parentage.
4839:Herodotus 7.11, however, gives Darius’ line thus: Achaemenes, Teispes, Cambyses, Cyrus, Teispes, Ariaramnes, Arsames, Hystaspes, Darius: in which Darius is the ninth. But Darius surely knew his own genealogy better than did Hero- dotus. Herodotus either has a dittographie error made in copying from a list covering both branches, or erroneously looked upon Cambyses and Cyrus as ancestors of Darius and inserted Teispes the second time to make the list agree with the known fact that the father of Ariaramnes was named Teispes.
4840:There are other accounts also, different in im- portant respects. Thus Nicolaus Damascenus, who is supposed to have used the Persica of Ctesias, states that Cyrus the Great was not an Achae- menian by birth, but a person of lowly origin who gained favor with Cambyses and eventually re- belled against him and overthrew him; see
4843:Ail the accounts, literary and inseriptional, are presented and evaluated by Weissbach in PW, Suppl.-Bd. 4.1132~44, s.v. Kyros. His conelusions are as follows: Of the sons of Teispes, Ariaramnes was king in Persis (then called Parsua) and Cyrus I was king in the city (or district?) Anshan, lymg between Persis and Elam, or possibly farther north, between Persis and Media. On coming to the throne of Anshan, Cyrus IT found Arsames ruling in Parsua, and shortly deposed him, him- self becoming now king in Parsua, later called Ратѕа. Arsames, however, was not put to death, but (as the OP inscriptions tell us) lived on until after his grandson Darius got the throne of the Persian Empire. Thus Hystaspes never was king, and is not counted among the nine Achaemenian kings. Cyrus II thereafter conquered Media and added it to his dominions, and then extended his conquests in all directions. But he did belong by ancestry to the Achaemenian line; one can hardly brand him as a rank outsider.
4844:Possibly Ctesias’ story, as repeated by Nicolaus Damascenus, originated in the line of Darius as a means of discrediting the line of Cyrus and of. justifying Darius in his seizure of the imperial power. The particular occasion might well be the unsuccessful revolt of Cyrus the Younger against his brother Artaxerxes IT, whom Ctesias served as personal physieian. Cf. JAOS 66.211 (1946).
4846:According to Behistan 510-513, Cambyses son of Cyrus killed his full-brother Smerdis, with such secrecy that his death was not known to the people; he then invaded Egypt. While he was on this expedition, rebellions developed in Persia and in Media and elsewhere. Notably a Magian named Gaumata headed the rebels, claiming to be Smerdis son of Cyrus, and he gained the kingship in all the rebellious territory. Cambyses, still in Egypt, committed suicide.
```


## [2026-09-14T02:00:36.144Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Kūruš\\|Kuru§\\|Küru\\|Kürus\" KNT.txt | sed -n '1,20p'",
 "description": "Kent lexicon Kurus"
}
```


### [2026-09-14T02:00:36.228Z] TOOL RESULT

```
489:OP и is similarly represented; wa = k"ur*ub = Kürui pug = pua.
1940:a. Names of the Achaemenian dynasty: Ari- ? ydramna-, Árlaxíaga-, Aríüma-, Uvarstra- (M), Kabüjiya-, Küru-, XSayarSan-, Gaubaruva-, Cifpi-, Darayavau-, Bardiya-, Vistüspa- (M).
1957:V. Uncertain names: Cišpi- (or Самур); Küru-; Datuvahya-; Атха-, name of an Armenian, of unknown meaning, and probably belonging under III or IV.
2156:Nom. Sg. Masc.: magus, piruš, sikabrus, ад). ш@татйун$; names of kings, Dérayava'us, Kürus; place-names, Abirddus, Kud"ru&, Qata- gus, Babiru’, Māļruļš, Margus, Hindu.
3450:CMa = Cyrus, MunaHAB (PASARGADAR) А, 1 adam : Kürus : xSaya 2 уа : Haxamanisiya TRANSLATION or CMa: I am Cyrus the King, an Achaemenian.
3451:CMb = Cyrus, Мовонав в. 1 Kūruš : xSdyabiya : vazraka : Kabijiya 2 hyd : zšāyaðiyahyā : puça : Hazdmani siya : З айу : уада... 4... ... akutà ...
5294:Küru- sb. ‘Cyrus’, founder of the Persian Empire: Elam. ku-rag, АКК. ku-ra-a$, Gk. Коро; (§164.V). Küru$ пэт. CMa 1; CMb 1; CMe.
```


## [2026-09-14T02:00:44.889Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nt=open('KNT.txt',encoding='utf-8',errors='replace').read(); lines=t.split('\\n')\nprint('leaf 5294:','\\n'.join(lines[:5294]).count('\\f'))\nprint('leaf 1957:','\\n'.join(lines[:1957]).count('\\f'))\n\"; sed -n '1950,1960p' KNT.txt",
 "description": "Kent leaf numbers"
}
```


### [2026-09-14T02:00:45.944Z] TOOL RESULT

```
leaf 5294: 203
leaf 1957: 71
NOUN STEMS 55
ably = Artazáaga), Vasdasaka, Vahyav'Sdapaya, Hadaxaya.
$164. PERSONAL Names or IRANIANS are of the usual IE types.
1, The typical IE name consisted of a com- pound of two stems; such names have mostly been interpreted in §160-§162. To these must be added the following, which are of uncertain interpreta- tion: Kabijiya-, Gaumata- (see Lex. s.vv.).
II. Compounds of which the prior part is an in- separable or a prepositional prefix are the follow- ing: ^U-vazstra-, Vi-darna-, Vi-vana-, Fra-varti-, perhaps *U-tdna-. It is possible that some of these are only shortenings of longer compounds of which these were the prior part, and that they belong under III.
III. Hypocoristies or nicknames were formed in pIE by limiting the compound name to approx- imately its prior part, to which there might or might not be added a suffix. There are the follow- ing probable examples in the OP names: Guzra-, Bard-1ya-, Vahau-ka-, ArSa-ka-, XSaór-ita, Fràda-, Martiya-
IV. Still other names are appellatives indicat- ing the qualities of the persons, like the redupli- cated Dé-dar- ‘Bold’. Possibly *U-vazstra-, Vi- darna-, Vi-vàna- (given under П) also belong here. Or names may denote occupations, as per- haps in the adjectival derivative, possibly pa- tronymie, Mardun-iya- ‘Vintner’s son’.
V. Uncertain names: Cišpi- (or Самур); Küru-; Datuvahya-; Атха-, name of an Armenian, of unknown meaning, and probably belonging under III or IV.
§165. Names or Monrus in OP are adjectives, or substantives as adjectives, modifying the word ‘month’; the phrase is always in the genitive! All are compounds of two stems or of prefix + stem, and some end in an adjectival suffix.
With vriddhi in first part: @digarci- (etymology uncertain); perhaps in Adwkanaiía- (etymol- ogy uncertain), A-ndma-ka-.
With vriddhi in both parts: Baga-yadi-.
```


## [2026-09-14T02:00:54.782Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KNT.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i in range(200,206):\n    print(i,'|',' '.join(leaves[i].split())[:180])\nEOF",
 "description": "Kent leaves around Kuru"
}
```


### [2026-09-14T02:00:55.847Z] TOOL RESULT

```
200 | B Gr. $144, §286, $298 (Bv. takes uvd- as instr. and not vriddhied), and by H. H. Schacder, Nachrich- ten d. Ak. d. Wiss. in Gottingen, phil.-hist. Kl. 19046-7.24-30. wdmarsiyus ns
201 | to the wall alongside it (König, - Burgbau 32n; Hz. AMI 3.54-5, Ар! 224). katam nsn. DSf 25. Katpatuka- sb. ‘Cappadocia’, a province of the Persian Empire; also, as adj., ‘Cappadoc
202 | om ã + kart- ‘cut’; but see Kent, Lg. 18.81-2). акша aor. mid. ($66.1, §218.11, §235.11) CMb 4; DB 1.47. akunavayalà imf. pass. (§220, $235.IT) DB 1.20, 24. akariya imf. pass. (585
203 | ted by the OP writing. регу. of Iran. root *kas- (89.V, §87, $126, §146.II), = Skt. kaś- ‘be visible, appear, shine’ (so König, Burgbau 61; not to Skt. Ёйс@- ‘crystal, quartz’, des
204 | , 66, 70f, 78f, 80, 91, 92; 3.1, 9, 11, 20, 21, 181 28, 29, 40f, 49f, 53, 54, 64, 69, 75, 76f, 83, 83f; 4.1, 3, 5, 11, 17, 21f, 25, 31, 33, 36f, 37, 40, 43f, 45f, 50, 53, 57, 59, 6
205 | sg. subj. (8212, $227.1) DNa 42. xindsdtiy subj. ($02, $97, 5110, $122) DB 1.52. azinav- vb. ‘hear, satisfy’ ($96): cf. Av. zšnav- ‘Genüge haben an’, adj. zínav- ‘Genüge leistend’,
```


## [2026-09-14T02:01:02.785Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Cyrus\" FSD_vol1.txt | head -20",
 "description": "FSD Cyrus"
}
```


### [2026-09-14T02:01:02.848Z] TOOL RESULT

```
489:Cyrus  Adler,  Ph.D.,
6427:dlate  predecessors  of  Cyrus,  In  the  Gth  century  B.  C.,  and  A-cIiet'l-dte,  1   a-ket'i-dl;  2   a-cCt'l-de,  n.  pl._  Entom.  The came  to  an  end  with  the  conquest  of  Alexander  (330  B.  C.).  Gryllidx.  Ach'e-ta,  n.  (t.  g.)  [L.,  <   Gr.  echetls,  singing. The  discovery  of  the  alphabet,  the  language,  tho  grammar,  and  <   ichS,  flOUnd.J the  meaning  of  the  (cuneiform]  inscriptions  of  tho  Achxmenian  Ach"6-tl'naf  1   ftk'l-tal'na;  2   UC'C-tl'na,  ft.  pi .   Entom.  A dynasty  deserves  to  bo  classed  with  the  discoveries  of  u   Kepler,  s   group  Of  Orthoptera the  crickets.  [<  ACHETA.]
6431:Ach"£C-men'l-d2c,  1   ak'tonenVdl;  2   &c’e-m£n'l-dS,  n.  vl.  A-ckl'as,  l   o-kai'ss;  2   n-cl'as,  n.  B(6  (Apocrypha).  1   Esd.  i,  2. An  ancient  Persian  dynasty  to  which  Cyrus,  Cambyses,  a-chfcvc',  (1  o-dhlv';  2   a-chev\  v.  [a-ciiieved',  a- Darius  Hystaspes,  and  Xerxes  belonged.  a-chlcv'p,  )   chievd'8;  a-chiev'ino.)  I.  t.  1.  To  accom-
7776:Ad'ler,  1   ad'ler;  2   ad'ler,  n.  1,  Cyrus  (»/i*lS63-  ),  an
11685:.l^oFo-glst.  aUgm-oro-gy,  n.  Improper  spellings  of  al'geous,  a.  Same  as  algous. ai'eal  la  Of  or  pertaining  to  alga*;  due  to  algie,  as  the  Al'ger,  l   al']sr;  2   fi'ger.  n.  1.  Cyrus  (l> rnntamlnation  of  water-supplies.  II.  n.  An  alga.  an  American  inventor  and  metallurgist.
15544:An'a-bas,  1   an'e-bas;  2   an'a-bfis,  n.  Ich.  A   genus  typical of  Anabantldx.  See  climbing-fish.  [<  Gr.  anabas,  2d aor.  p.  of  anabalnb ,   <   ana,  up,  +   batnb ,   go.} a-nab'a-sls,  1   e-nab'o-sls;  2   a-nfib'a-sls,  n.  [Gr.]  1.  (1)  A going  up;  an  expedition  up;  a   military  advance,  especially that  of  Cyrus  the  Younger.  401  B.  C.  (2)  [A-J  The  work In  which  Xenophon  narrated  the  story  of  this  expedition. .   Hearty  devotion  to  his  [Xenophon’sl  work.  .   .   .   gives  .   .   - li/c  and  spirit  to  the  details  of  the  Anabasis.  It-  W,  Bbowne Hist.  Classical  Lit.  bk.  ii,  ch.  13,  p.  352.  Is.  a   co.  1852.]
25582:Ar^fax-erx'es,  1   Sr’tng-zurk'slx;  2   ar't5g-zerk'se«,  n.  1.  I. Longlmanus  (died  425  B.C.).  king  of  Persia;  conqueror  of Egypt.  2.  II.  Mnemon  (4507-362  B.  C.),  a   Persian  king, who  defeated  Cyrus  at  Cunaxa.
27720:As-ty'a-ges,  l   as-tai-a-JIz;  2   &s-ty'a~6es,n.  Last  king  of  Media (584-560  B.  C.),  dethroned  by  his  grandson,  Cyrus  the  Great. As-ty'a-nax,  1   as-tai'o-naks;  2   &s-ty'a-n5ks,  n.  Myth.  The son  of  Hector  and  Andromache.  He  figures  in  the  Iliad, and  after  the  fall  of  Troy  the  Greeks  hurled  him  from  the walls  of  the  city,  that  the  prophecy  or  Calchas,  that  Astya- nax  would  restore  the  kingdom,  might  not  be  fulfilled.  In Racine’s  Andromaque,  Astyanax  goes  with  his  mother  to Epirus  arid  becomes  king  of  that  country.
33242:—   Babylonian  architecture,  the  architectural  style  de- veloped in  Babylon  during  the  period  of  Babylonian  art mentioned  below:  characterized  (1)  by  massive  structures of  sun-dried  brick,  (2)  by  painted  plaster  surfaces  In  inte- riors, and  (3)  by  enameled  tiles  forming  patterns.  Its  tem- ples were  stepped  In  terraces  colored  to  contrast  with  one another.  See  Mesopotamian.— B.  art,  that  branch  of Mesopotamian  art  developed  at  Babylon  before  1000  B.  C. and  also  practised  after  600  B.C.  Its  lapidary  art  and  Its metal-work,  textile  fabrics,  and  pottery  were  of  great  merit. Compare  Assyrian  art,  under  Assyrian.— B.  or  Baby- lonish captivity.  1.  The  seventy  years*  captivity  of  tho Jews  In  Babylon,  ending  with  Cyrus,  536  B.  C.  2.  Ch. Hist.  The  period  (1309-1377)  when  the  papal  court  was  at Avignon.— B.  cosmogony,  sec  Creation  epic.— B.  or Babylonish  dialect,  speech  In  which  there  is  confusion  of tongues.  —   B.  era,  the  “era  of  Nabonassar/’  which  was assumed  to  begin  Feb.  26,  747  B.  C.
39700:d_elKited_and  slain  by  Cyrus.  2.  BaWcm.  HUt .   The  son  Funen  island  and  the  mainland.
55780:Dry  stalks  of  dead  plants.  H.  Did.  cam'bockt. Cara-by'ses,  1   kam-bai'slz:  2   cfim-bjr's5§,  n.  King  of Persia.  529-522  B.  C.;  son  of  Cyrus.  Kam-by'sesi  IGr.]. Cam 'den,  l   kam'den;  2   cSm'd§n,  n.  1.  Earl  of  (1714- 4/isl794),  Charles  Pratt,  an.  English  statesman;  Lord Chancellor;  opposed  Lord  North's  policy  in  America.  2. William  (5/:1551-11/sil623),  an  English  antiquary;  his- torian: founded  the  Camden  professorship  of  history  at Oxford;  Annals  of  the  Reign  of  Elizabeth.  3.  A   county In  Georgia;  718  sq.  m.;  county-seat,  St.  Mary’s.  4.  A county  In  Missouri;  702  sq.  m.;  county-seat,  Creek.  5. A   county  In  New  Jersey;  222  sq.  m.  6.  its  county-seat. 7.  A   county  In  North  Carolina;  218  sq.  m.;  county-seat, Camden  Court  House.  8.  A   town,  county-seat  of  Kershaw county,  S.  C.  9.  A   city,  county-seat  of  Ouachita  county, Ark.  10.’  A   village  in  Oneida  county,  N.  Y.  11.  A   village In  Knox  county,  Me.  [gland.
57159:a-dS'shl-a,  n.  An  ancient  province  In  15th  century, Asia  Minor;  subdued  by  the  Persians  a   Capote, under  Cyrus:  reduced  to  a   Roman  province  by  Tiberius. Kap"pa-do-kI'at[Gr.].—  Cap"pa-do'cIan,  a.&  n. cap'*pa"per,  n.  See  under  cap1,  n.
66254:If  the  course  of  events  and  the  destiny  of  nations  were  foverned by  no  law  .   .   .   there  could  be  no  science  of  history,  but  only chronicles.  F.  H.  Hedge  Ways  of  the  Spirit  p.  7.  in.  unos.  J8'8.J [<  F.  chronique,  <   L.  chronica,  <   chronicus;  eee chronic,  a.]  Syn~  see  archives;  history.— Books  of Chronicles,  a   portion  of  the  Old  Testament  Scripture  — forming  only  one  book  In  the  Hebrew  canon,  but  divided by  the  Greek  translators  Into  two  —   setting  forth  a   history of  the  covenant  from  the  death  of  King  Saul  to  the  decree of  Cyrus  for  the  rebuilding  of  the  temple.—  chronicle  his- tory (Drama),  a   historical  play,  generally  based  on  En- glish chronicles,  as  Shakespeare’s  Richard  III.  and  Henry  i . chron 'i-con,  1   kren'i-ken;  2   crdn'l-cdn,  n.  [-ca,  pl. ]   lGr.J A   chronicle.
66594:2.  [C-  T-]  A   sect  formed  by  George  Jacob  Schweinfurtb, who  claimed  to  be  the  "Christ  of  the  Second  Coming”; belief  in  this  claim  qualifies  for  membership  or  the  sect.  3. [C-  T-]  A   communistic  sect  founded  by  Cyrus  Teed,  with  a view  of  reestablishing  church  and  state  on  the  grounds  of divine  fellowship  —   c.  universal,  see  under  church,  def.  5, above  —   church'wo"man,  n.  1.  A   woman  devoted  in  at- tendance on  church  services,  and  In  church  activities.  2.  A woman  who  worships  according  to  the  rites  of  the  Church of  England.—  c.  work,  work  in  some  branch  or  branches of  the  activities  of  a   church,  such  as  clubs,  gilds,  Sunday- school,  etc.,  in  a   modern  institutional  parish.—  c.  work- er.— cowrit,  n.  [Eng.]  An  order  of  an  ecclesiastical  court. —   Eastern  C.,  see  Greek  Church.— English  C.,  see Church  of  England  — established  c.,  a   church  estab- lished, and  at  least  In  part  supported,  by  the  state  —   hall  c., the  church  whose  architecture  is  characterized  by  three  or more  parallel  divisions,  all  of  which  are  of  equal  height.— law  C., -the  established  Church  of  England— round  c.,  a church  of  circular  construction  built  around  a   memorial,  sa- cred relic,  or  monument;  a   polygonal  church  or  one  radiat- ing from  a   common  center.— state  c.,  see  established church.—  visible  c.,  the  whole  body  of  Christ's  professed followers  on  earth.—  Western  C.,  the  medieval  church  of the  Western  Roman  Empire,  now  the  Roman  Catholic Church:  opposed  to  the  church  of  the  Eastern  Empire,  now the  Greek  Church.
82912:the  Gth  century  B.  C.;  defeated  and  dethroned  by  Cyrus.  cr.inks.1
86390:Cyrus.  Anna  of  Butler.
```


## [2026-09-14T02:01:07.298Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Cy'rus\\|Cy’rus\\|Cy\\\"rus\\|Ky'ros\\|Kyros\" FSD_vol1.txt | head -10",
 "description": "FSD Cyrus headword"
}
```


### [2026-09-14T02:01:07.364Z] TOOL RESULT

```
85568:Cy"re-na'Ic,  n.^  1.  A   disciple  of  the  hedonistic  school of  post-Socratic  philosophy  founded  by  Aristippus  of  cy^ 'rus*  *1  sal'rus;  2   cS'^rfis  n. Cyrene:  called  hedonistic  because  it  makes  pleasure  the  Cy'rus*,  l   sarrus;  2   cy'rOs’.  n.
```


## [2026-09-14T02:01:10.049Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '85560,85600p' FSD_vol1.txt; python3 -c \"\nt=open('FSD_vol1.txt',encoding='utf-8',errors='replace').read(); lines=t.split('\\n')\nprint('leaf','\\n'.join(lines[:85568]).count('\\f'))\"",
 "description": "FSD Cyrus entry"
}
```


### [2026-09-14T02:01:11.448Z] TOOL RESULT

```
Cyp'se-lus,  n.  (t.  g.)  [L.,<  Gr.  typselos, a   swift.]— cyp'se-lld,  n.— cyp'se-H- form,  a.  Having  the  torm  of  a   swift; cypselomorphfc.—  Cyp"se-lI-ror'mes, n.  pi.  Ornlth.  The  Cypsclomorphx.—
Cyp"se-H'na»,  n.  pi.  Ornlth.  The  Micro-  a,  com-
podlnx.—  cyp'se-Ilne.  Ornlth.  I.  a.  Of  plot©;  t>,m  section, or  pertaining  to  the  Cypselinx  or  Cypseli.  II.  n.  One  of the- Cypselinx.—  cyp'se-Iold,  a.  Ornlth .   Of  or  pertaining to  the  Cypseltdx.
Cyp"se-loI'des,  l   slp'si-lel'dlz;  2   c^P'se-lol'dffa,  n.  pi.  Or- nllh.  The  Cypsclomorphx.  [<  Gr.  kypselos,  a   swift,  4- -OID.]
Cyp"se-Io-mor'phre,  1   slp'si-lo-mer'fl;  2   c^P’se-lo-mGrTG, n.  pi.  Ornlth.  A   division  of  seglthognathous  birds  In- cluding the  swifts,  humming-birds,  and  goatsuckers.  [   <
Gr.  kypselos,  a   swift,  4-  morph? ,   form.]  —   ryp'se-Io-morpb, n.—  cyp"sc-Io-mor'phIc,  a.  Cypscllform;  of  or  pertaining to  the  Cypselomorphx.
Cy"re-na'ic,  1   sai'n-ne'ik;  2   py're-na'ic,  a.  1.  Of  or relating  to  Cyrene,  the  capital  of  Cyrenaica,  on  the north  coast  of  Africa.  2.  Belonging  to  or  characteristic of  the  school  of  philosophers  called  Cyrenaics.  f   <   L.
Cyrenaicus ,   <   Gr.  Kyrenalkos,  <   Kyrene,  Cyrene.]
Cy"re-na'Ic,  n.^  1.  A   disciple  of  the  hedonistic  school of  post-Socratic  philosophy  founded  by  Aristippus  of  cy^ 'rus*  *1  sal'rus;  2   cS'^rfis  n. Cyrene:  called  hedonistic  because  it  makes  pleasure  the  Cy'rus*,  l   sarrus;  2   cy'rOs’.  n.
chief  good.  See  hedonism.  Unlike  the  Epicureans,  the founder  taught  that  positive  pleasures  are  to  be  preferred to  negative,  or  tranquil  enjoyment.  Aristippus  recognized, however,  differences  among  pleasures,  and  held  that prudence,  or  practical  philosophy,  which  discerns  these differences,  is  the  guide  to  tne  right  conuuct  of  life.  “ native  or  inhabitant  of  Cyrenaica;  a   Cyrenlan.
Cy"rc-na  'l-ca,  1   sai'ri-nS'i-ka;  2   cS^re-nS'l-ca,  n.  An  ancient Greek  colony  in  Africa;  annexed  to  Italy  in  1912.
Cy"rc-na'I-clsra,  1   sai'ri-tor  sirVJno'i-sizm;  2   cp're-Jor Cyr*e-]na'i-sTsm,  n.  The  doctrines  of  the  Cyrenaics, especially  the  doctrine  that  pleasure  is  the  only  rational aim  of  human  conduct.
Cy-re'ne,  l   sal-rt'nl;  2   c?-rS'n6,  «•  Myth.  A   nymph, mother  of  Arlstanis.  by  Apollo,  who  carried  her  from  Mt. Pellon  to  Libya.  2.  A   Greek  city  in  N.  Africa,  between Alexandria  and  Carthage,  capital  of  the  Greek  colony  of Cyrenaica;  now  a   desert.
Cy'^c-nel'll-d®,  1   sol’n-Iw  str’i-lncl'l-dl;  2   cy're-for  c?r'e4 nSl'1-de,  n.  pi.  Conch.  A   family  of  veneracean  bivalves having  long  united  siphons,  a   clavlform  foot,  and  a   roundish shell  with  3   cardinal  teeth  in  the  right  and  2   In  the  left valve,  and  entire  palllal  line.  Cy'^e-ncna,  «.  (t.  g.) [Dim.  of  CYRENA.l  —   cy"re-ncnid,  n.—  cy"re-ncHo!d,  n.
Cy-re'nl-an,  1   si-rl'm-en;  2   cy-re'ni-an.  I.  a.  Cyrenaic. H.  n.  A   native  or  permanent  resident  of  Cyrene.
Cy-ren 'I-dac,  X   ei-ren'l-dl;  2   cy-rfin'J-de,  n.  pi.  Conch.  A family  of  conchacean  bivalves,  especially  those  having  2 short  siphons  nnd  a   trigonal  or  oval  shell  with  antemedlan umbones,  2   or  3   cardinal  and  anterior  and  posterior  lateral teeth,  and  external  ligament;  Corbiculidx.  Cy-re'na,  n. (t.  g.)  [   <   L.  Cyrene.  <   Gr.  Kyrln ?,  nymph's  name.]  —
cy-re'nid,  n.—  cy-re'nold,  a.
Cy-re'nl-us,  n.  Bib.  Same  as  QtmuNTB,  n.,  2.
Cy-rc'nus,  1   sal-rl'nus;  2   cy-rC'nlls,  n.  Hit.  (Doual).
Cjt'Ic,  Saint.  Patron  of  sailors;  St.  Elmo,
skull  having  a   hump-like  convexity  upon  the  top.—  cyr"- to-cer'a-cone,  n.  A   shell  of  the  genus  Cyrtoccras,—  Cyr"- to-cer-at'l-dae,  n.  pi.  Conch.  A   Paleozoic  family  of  nautl- Joldean  cephaJopods  having  a   curved  shell  with  a   simple aperture.  Cyr-toc'cr-as,  n.  (t.  g.)  —   Cyr"to-cer'a-tld,  n.
—   cyr"to-ccr'a-to!d,  a.—  cyr"to-cer'a-tltc,  n.  A   fossil  of a   cyrtoceratold  cephalopod.— cyr"to-cer'ra-tlt'lc,o.  Hav- ing a   curved  shell;  of  or  pertaining  to  a   cyrtoceratite.  cyr"- toe'er-anf.— cyr^to-coele-an,  a.  Having  a   vertebra  whose centrum  is  convexo-concave.—  cyr'to-cone,  a   form  of  shell taking  the  place  of  an  earlier  formation  In  nautiloid  cephal- opoda.— Cyr"to-don'tI-da?,  n.  -pi.  Conch.  A   Paleozoic family  of  arcacean  bivalves  with  a   Bbort  convex  shell,  small hinge  area,  cardinal  teeth  curved  or  horizontal,  and  lateral teeth  elongate  and  curved  or  oblique.  Cyr"to-don'ta,  n. (t.  g.)  —   cyr"to-don't!d,  a.  «fc  n.—  cyr'to-graph,  n.  Same as  cyrtometer.—  cyr'told,  a.  With  a   hump  on  the  back; humpbacked.—  Cyr-tol'dp-a,  n.  pi.  Proioz.  A   suborder  or family  of  nassellarlan  radlolarlans  with  a   complete  lattice- shell  exhibiting  a   simple  or  reduced  cephalis.  Cyr'tl-da}.
—   cyr-toi'de-an,  a.  &   n.—  Cyr-tol'dl-da,  n.  pi.  An  or- der of  radlolarlans  comprising  the  families  Podocampldx, Anthocyrtldx, etc.—  cyr'to-llte.n.  Mineral.  Altered  zircon.
—   Cyr"to-li'tes,  n.  Paleon.  A   genus  found  In  the  Silurian stratifications  consisting  of  mollusks  of  the  gastropod  type and  belonging  to  the  Bellerophontldx.—  cyr-tom'e-ter,  n. 1.  An  Instrument  for  measuring  the  circumference  of  the chest  or  for  tracing  the  exact  cross-section  of  the  chest  on  a chart.  2.  A   device  by  means  of  which  the  form  and  di- mensions of  the  head  are  measured.— Cyr"to-no'tus,  n. Paleon.  A   genus  of  fossil  pelecypods  having  one  tooth on  each  valve,  found  In  Devonian  strata.—  cjT-fo'pI-a#  «. Crust.  The  larval  stage  at  which  the  antenna;  are  trans- formed and  no  longer  serve  for  locomotion,  as  In  schlzopods.
—   cyr"to-pla'ty-an,  a.  With  or  having  a   convexo-plane vertebral  centrum.—  cyr-to'sis,  n.  Pathol.  Curvature,  espe- cially' of  the  spine.—  Cyr'to-spa'1'dlx,  n.  Bot.  A   genus  of tropical  American  herbaceous  perennials  belonging  to  the family  Araccx.  The  cultivated  species  and  varieties  have beautifully  marked  leaves.—  cyr'to-stylc,  n.  A   portico  of circular  shape  projecting  from  a   house.
[Anglo-Ind.1  A   crane.
1.  A   masculine  personal  name.
F.  Cyprus',  1   sITU',  2   cV TU':  G.  Cy #rus,  1   tsi'rus,  2   tsjl'rus; It.  Cl'ro,  1   tihi'ro,  2   chITo;  Sp.  Cl'ro,  1   thl'ro,  2   thl'ro.  2. “The  Great”  (   -V-528  B.  C,),  king  of  Persia:  founder  of
the  Persian  empire.  3.  “The  Younger”  (4247-401  B. C.),
-   second  son  of  Darius  Notus,  king  of  Persia.  [Per.,  the  sun.)
A   cyst,  1   sist;  2   c^st,  n.  1.  Anat.  Any  membranous  sao or  vesicle;  as,  the  biliary  cyst;  the  urinary  cyst.  2. Pathol.  Any  abnormal  sac  or  vesicle  in  which  morbid matter  may  be  collected  and  retained.  3.  Zool.  (1)  A bladder-like  sac,  as  that  with  which  an  embryonic  tape- worm surrounds  itself.
‘Cyst’  is  applied  to  completely  dosed  investments  .   .   .   which are  temporarily  produced  either  as  a   protection  against  adverse external  conditions  or  during  tho  breaking  up  of  the  parent-cell into  apores.  Lankbsteu  in  Encyc.  Brit.  9th  od..  vol.  xix,  p.  834. (2)  A   bladder-worm.  4.  Bot.  (1)  A   receptacle  for  oil in  the  rind  of  the  orange  and  like  fruits,  (2)  A   cell  or cavity  containing  reproductive  bodies  in  certain  cryp- togams. (3)  The  spore-case  of  a   seaweed.  t<Gr.  kys- ‘   tls,  bladder,  <   kyO,  contain.]  —   cys'tal,  a.
—   dentigerous  cyst,  a   dcrmatold  cyst  containing  teeth.  . piliferous  c.t>— Meibomian  c.,  same  as  chalazion. cj'st-ad"c-no'raa,  n.  Pathol.  An  adenoma  having  cysts.  * cys"to-ad"e-no'mat.—  cys-taPgl-a,  n.  Neuralgia  of  the bladder.— cys-tat'ro-phy,  n.  Pathol.  A   wasting  of  tho bladder.  cys"ta-tro'phi-at.—  cys"tau-clic-nl't!s,  n. Pathol.  Inflammation  of  tho  neck  of  the  bladder.— rys- tec'ta-sy,  n.  Surg.  An  operation  for  extracting  calculus from  the  bladder  by  dividing  the  membranous  portion  of the  urethra  and  then  dilating  tho  neck  of  tho  bladder.— cys-tec'to-my,  n.  Surg.  1.  Anoperatlontorcmovoa  cyst.
2.  Removal  of  the  gall-bladder.—  cyst'cd,  a.  Enclosed  In  a sac;  encysted;  as,  a   cysled  tumor. cys'te«!n,  11  sls'ti-ln,  -In  or  -In;  2   c^s'te-In,  -In  or  -In,  n. cys'ttslnc,  /   Chem.  A   substance  (CjHjOsNS)  produced  by the  decomposition  of  protelds.—  cys"tc-in'lc,  a.
eyr'U,  1   sir'll;  2   car'll  n.  1.  A   masculine  personal  name  cys'tel-mtnth,  n.  An  encysted  worm.-  cys-tcn'chy-ma, Dan.  D.  C>-rIl  lus,  i   Bt-ril  us,  2   PV-rll  us.  F.  C>  rllle  *   1   n.  Spong.  A   parenchymatous  tissue  beneath  the  skin  of
Spong.  A   parenchymatous  tissue  beneath  the  skin  < certain  sponges,  composed  of  cyst-Ilko  cells,  cys'ten- cbymef.—  cys"(cn-chym/a-tousf  a.—  cys'fen-cyfe.  n. A   large  bladder-cell  in  the  cyatcnchyma.— Cys"tc-ol'da,t n.  pi.  Echln,  The  Cystoidea.—  cys"te-oI'I-thus,  n.  Pa- thol. 1.  Stone  In  the  bladder;  urinary  calculus.  2.  An agent  or  medicine  used  to  break  or  dissolve  a   calculus.
From
arm'.  2   cy'ril':  G.  Cy'rlll,  I   tsi'rll,  2   tslTIl;  Gr.  Ky'rll-los;
It.  Cl-rll'Io,  1   tfhl-rjl'lo,  2   chl-ril'Io;  L.  Cy-rll'Jus,  1   sj- rll'us,  2   cy-rll'Gs;  Sp.  Cl-rllo,  1   thl-rl'lo,  2   thl-ri'lo.  2.
Saint  (315-386),  a   Greek  Father,  bishop  of  Jerusalem;
Lectures  to  Catechumens,  etc.  3.  Saint  (370  ?-444),  arch- bishop of  Alexandria:  a   father  of  tho  church:  instigated
leaf 706
```


## [2026-09-14T02:01:25.873Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^sker-\" AHD_watkins1985.txt | head; echo \"---\"; awk '/^sker-2/,/^sker-3/' AHD_watkins1985.txt | head -60",
 "description": "Watkins sker- roots"
}
```


### [2026-09-14T02:01:27.137Z] TOOL RESULT

```
<persisted-output>
Output too large (37.4KB). Full output saved to: /home/sfmqrb/.claude/projects/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/tool-results/b19uieoam.txt

Preview (first 2KB):
937:sker-'
939:sker-2
---
sker-2
*skerb(h)-, *skreb(h)-. 1. Germanic *skarpaz, cutting, sharp, in: a. Old English scearp, sharp: SHARP; b. Gothic skarp6, pointed object, akin to the possible Germanic source of Italian scarpa, embankment: scarp. 2. Ger- manic *skrap- in: a. Old Norse skrap, “pieces,” remains: SCRAP!; b. Old Norse skrapa, to scratch: SCRAPE. 3. Ger- manic skrab- in: a. Middle Dutch schrabben, to scrape: SCRABBLE; b. Middle Dutch schrobben, to scrape: SCRUB!. 4, Germanic *skrub- in Old English scrybb, shrub (< “rough plant”): SHRUB. 5. Latin scrobis, trench, ditch: SCROBICULATE. 6. Latin scrdfa, a sow (< “rooter, digger”): SCREW, SCROFULA. [Pok. 4. sker-, Section I. 938.] sker-2. To leap, jump about. Perhaps same root as sker-3. 1. Extended form “skerd- in Germanic *skert- in Middle High German scherzen, to leap with joy: SCHERZO. 2. O-grade variant form *kor- in Latin coruscdre, to vibrate, glisten, glitter: coRUSCATE. [Pok. 2. (s)ker- 933.] sker-3. Also ker-. To turn, bend. Presumed base of a number of distantly related derivatives. 1. Extended form *(s)kreg- in nasalized form *(s)kre-n-g- in: a. Ger- manic *skrink- in Old English scrincan, to wither, shrivel up: SHRINK; b. variant *kre-n-g- in Germanic *hrunk- in (i) Old Norse hrukka, a crease, fold: RUCK? (ii) Frankish *hrunkjan, to wrinkle (> Old French fronce, pleat): FLOUNCE!, 2, Extended form *(s)kregh- in nasalized form *skre-n-gh- in Germanic *hringaz, something curved, circle, in: a. Old English Aring, a ring: RING!; b. Old French renc, reng, line, row: RANCH, RANGE, RANK}, RINK; ARRANGE, DERANGE; C. Middle Dutch rinc (com- bining form ring-), a ring: RINGHALS. 3. Extended form *kreuk- in Germanic “*hrugjaz in: a. Old English hrycg, spine, ridge: RIDGE; b. Old High German hrukki, back: RUCKSACK. 4. Suffixed variant form *kur-wo- in Latin curvus, bent, curved: CURB, CURVATURE, CURVE, CUR- vET. 5. Suffixed extended form kris-ni- in Latin crinis (< *crisnis), hair: CRINITE; CRINOLINE. 6. Suffi
...
</persisted-output>
```


## [2026-09-14T02:01:30.096Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk '/^sker-3\\. Also ker-/,0' AHD_watkins1985.txt | head -c 3000",
 "description": "Watkins sker-3 full"
}
```


### [2026-09-14T02:01:31.896Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T02:01:34.794Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('AHD_watkins1985.txt',encoding='utf-8',errors='replace').read()\ni=t.find('sker-3. Also ker-')\nprint(t[i:i+3000])\nEOF",
 "description": "Watkins sker-3 text"
}
```


### [2026-09-14T02:01:35.997Z] TOOL RESULT

```
sker-3. Also ker-. To turn, bend. Presumed base of a number of distantly related derivatives. 1. Extended form *(s)kreg- in nasalized form *(s)kre-n-g- in: a. Ger- manic *skrink- in Old English scrincan, to wither, shrivel up: SHRINK; b. variant *kre-n-g- in Germanic *hrunk- in (i) Old Norse hrukka, a crease, fold: RUCK? (ii) Frankish *hrunkjan, to wrinkle (> Old French fronce, pleat): FLOUNCE!, 2, Extended form *(s)kregh- in nasalized form *skre-n-gh- in Germanic *hringaz, something curved, circle, in: a. Old English Aring, a ring: RING!; b. Old French renc, reng, line, row: RANCH, RANGE, RANK}, RINK; ARRANGE, DERANGE; C. Middle Dutch rinc (com- bining form ring-), a ring: RINGHALS. 3. Extended form *kreuk- in Germanic “*hrugjaz in: a. Old English hrycg, spine, ridge: RIDGE; b. Old High German hrukki, back: RUCKSACK. 4. Suffixed variant form *kur-wo- in Latin curvus, bent, curved: CURB, CURVATURE, CURVE, CUR- vET. 5. Suffixed extended form kris-ni- in Latin crinis (< *crisnis), hair: CRINITE; CRINOLINE. 6. Suffixed ex- tended form *kris-td- in Latin crista, tuft, crest: CREST, CRISTA, CRISTATE. 7. Suffixed extended form *krip-so- in Latin crispus (metathesized from *cripsus), curly: CREPE, CRISP, CRISPATE. 8. Extended expressive form *kriss- in Latin crisdre, (of women) to wiggle the hips during copulation: crissuM. 9. Perhaps reduplicated form *ki-kr-o- metathesized into Greek krikos, a ring (> Latin circus, ring, circle): CIRCA, CIRCLE, CIRCUM-, SEARCH; CRICOID. 10. Suffixed o-grade form *kor-6no- in Greek kordnos, curved: (CORONA), CROWN; CORONOID. 11. Suffixed variant form *kur-to- in Greek kurtos, bent: KURTOSIS. [Pok. 3. (s)ker- 935.] sker-4. Excrement, dung. Extension of sek-, “to cut, separate,” hence “to void excrement.” 1. Form *sk-6r- in Greek skdr (genitive skatos < *sk-nt-), dung: SCATO-, SCORIA, SKATOLE. 2. Extended form “skert- in taboo metathesis *sterk-os- in: a. Latin stercus, dung: STERCO- RACEOUsS; b. variant forms *(s)terg-, *(s)treg- in Germanic *threkka- in Middle High German dréc, dung: DRECK. [Pok. sker-d- 947; 8. (s)ter- 1031.] skerbh-. Also skerb-. To turn, bend. Extension of sker-3. 1. Variant form *skreb- in Germanic *skrip- in Old Norse skreppa, to slip, and derivative Old Norse skorpna, to shrink, be shriveled, akin to the probable Scandinavian source of Middle English scorchen, to scorch: SCORCH. 2. Nasalized variant form *(s)kre-m-b- in: a. Germanic *hrimp-, *hrump- in (i) Old English hrympel, wrinkle, fold: RIMPLE (ii) Middle Dutch rom- pelen, to wrinkle: RUMPLE (iii) Old French ramper, to climb, rear up: RAMP?; b. Germanic *skrimp- in (i) Mid- dle Low German schrempen, to shrink, wrinkle, perhaps akin to the possible Low German source of Middle English shrimp, pygmy, shrimp: SHRIMP (ii) Swedish skrympa, to shrink, perhaps akin to the possible Scandi- navian source of SCRIMP. 3. Variant form *kramb- in Greek krambé, cabbage (having wrinkled, shrunken
skeup-
leaves): CRAMBO. 4. Perhaps Celtic *krumb-i- in Welsh
```


## [2026-09-14T02:01:51.741Z] TOOL CALL #43: Bash

```json
{
 "command": "pdftoppm -f 454 -l 454 -r 300 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg454 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg454.png",
 "description": "Render PDF page 454"
}
```


### [2026-09-14T02:01:53.979Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 74797 Sep 13 22:01 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg454.png
```


## [2026-09-14T02:01:55.720Z] TOOL CALL #44: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg454.png"
}
```


### [2026-09-14T02:01:56.573Z] TOOL RESULT

```

```


## [2026-09-14T02:01:56.562Z] INPUT

[Image: original 2550x3300, displayed at 1546x2000. Multiply coordinates by 1.65 to map to original image.]


## [2026-09-14T02:02:15.711Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && grep -n \"\\[pdf page\" BQT_v3_pages.txt | head -3; echo \"...\"; grep -c \"\" BQT_v3_pages.txt; echo \"---search کنار---\"; grep -n \"کنار\" BQT_v3_pages.txt | head -10",
 "description": "BQT v3 pages check"
}
```


### [2026-09-14T02:02:15.844Z] TOOL RESULT

```
1:[pdf page 1]
3:[pdf page 2]
24:[pdf page 3]
...
51425
---search کنار---
1353:‏بر اثر او برفتند بکنار چاهی رسیدند . مار بر
1354:کنار چاء حلقه زد (۱) ‎AIT.‏ بدرون رفت وبر
1503:‏ازتیرث نزديك بکو کناربان, دارای کلهای نامنظم وب رکپای‌بربده است که چون بادست لرم کنند
2379:پیشتر در صحراها وکنارهای جوبها رود ‎Ky,‏
3060:فرشت»بهنی کنار و گوشه و طرف باشد ۷ نودر
3077:1 , کناره ‎cel ۷ . ۸۵ Sy?‏ (ه.م ) . توعی ازچاریابان پستاندار
6381:‏۴ - کر آهوئی بتا و کنار منت حرم ‎gly)‏ کنار مت حرم .
6899:افعالزیل است : عبری 52026 لا زکاز کنار رفت, استراحت کرد) ؛ سربالی ‎shbat‏ (استراحت
7269:پیچیده در کناری گذارند .
9930:کنارخوانندبضمکاف وبعربی ثمرةالدر ۴ خوانند
```


## [2026-09-14T02:02:21.578Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && awk 'NR<=3080 && /^\\[pdf page/ {p=$0} END{print p}' BQT_v3_pages.txt; sed -n '3050,3085p' BQT_v3_pages.txt",
 "description": "BQT v3 kanar context"
}
```


### [2026-09-14T02:02:22.729Z] TOOL RESULT

```
[pdf page 1]
‏شتر به ۸ = ‎pty‏ اول و ‎HN‏ بس وزن
‎as te‏ ام کاوی است که بتزوبر ‎MS‏ که‌بدمنه
موسوم است‌فریفته شد وبا شیرجنگه کرد و کشته
شد » و این حکایتبت در ‎ABT‏ ودمنه.

‏شتر ‎IE‏ » نام نوعی از خار ‎ath‏ که
شتر آنرا برغبت تمام خورد .

‏آمده است (۲) که آب ورزی و شناوری باشد.
شتر - بقتح اول و ‎os‏ ثالی و رای
فرشت»بهنی کنار و گوشه و طرف باشد ۷ نودر

‏عربی مممنی قطع است اعم از بربدن نا شکستن

‏- و بهندی دشمن را کویند - و بقتح اوژوثانی

‏شتردل ‎oe‏ بد دل و کینه‌ور باشد
- وبر بی‌چگر وبیدل و نامرد هم اطلاق کرده‌اند

‏(۱) چك: ژند ‎(y) . Fay‏ چك: -

‏۱ = ستاغ ‎(pod‏ ۴ - ر: ستال .

‏۴ رك: لفت فری ۲۸۰ (شاهد ازحکاك عرغزی) . ۴ - مصحف «شنتان؛جمع
عزوارشی شنة 522821 ‎oe)‏ عربی) ۰ آرامی 540208 ‎jbo?‏ ۲5۹ .

‏8 - ممحت «دناء» ‎She‏ آشنا (هم) . ‎pet‏ مق( + پهلوی
1 , کناره ‎cel ۷ . ۸۵ Sy?‏ (ه.م ) . توعی ازچاریابان پستاندار
وشخوار کننده که ‎dh‏ بادو کوهان درپشت داراد ‎sles‏ پاهاو کردن: ‎eine on‏ باروواری
بکار میروند . 4 - درفرهنگه رشیدی «شنزبه» (یس‌آزشن : : تون وزا ( آمده و ‎ae‏ :

‏« بسنی ‎ge‏ شین وسکون تای فرشت وفتح رای مهمله خوانده‌اند وآن غلط است چتانکه ازسخج
‎Line‏ ودمنه معلوم شده» و در «فرهشکه نظام» لیزبهمین املاء خبط شده و شرحی درباب
تصحیف کلمه آمده‌است ۰

‏* شتااتی- بکسراول‌وقتح پنجم ‎bode)‏ مر کزی). پیلوی ۵511621120 (عجله کردن)
```


## [2026-09-14T02:02:27.648Z] TOOL CALL #47: Bash

```json
{
 "command": "python3 tools/ref_page.py BQT:1611 2>&1 | head -60",
 "description": "Fetch BQT page 1611"
}
```


### [2026-09-14T02:02:35.628Z] TOOL RESULT

```
REF: BQT:1611  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 404  OCR-lang: fas

-۹۱۱- کراه
کرام ۱ « بم اول بر وزن سراغ . | اول وفتح کاف زاغ وکلاخ هردو راکوبند۴ .
کیاهی باشد که بازوی فرود آمده و استخوان‌از کراك - بفتح اول بروزن امان؛ بممتی
جای بدر رفته را بدان بندند . کنار باشد ‎٩‏ که در مقابل میان است -وبمعنی
کرالك ۴ - بفتح اول بر وزن علاك . | اشپا هم هن که.در مقابل ابدا است - و کرانه
نام پرنده‌است کبود و سفید و دم درا ز که بر لب وگوشه کرفتن و دوری کزیدن را نیز گفته‌اند -
آبها شیند و دم خود را بجنباند"و آنرا بعریی | و بضم اول اسبیرا میگوبند که رنگه او مايين
صموه گوبند ؛ و بعی عکه راگفته‌اند ؛ و باین | زرد و بور باشد ؛ و باین معنی بحذف الف هم
معنی شم اول هم آمده است ؛ و بعضی کوبند آمده است و(۱) کوبند ترکی‌است.
کرك است که بودنه باشد وآن پرنده‌ایست‌پرخط کرانه - بروزن زماله » بمعنی کران
وخال از تیه و کوچکتر که بعر بی سلوی وبتر کی باشد که کنار است ‎٩‏ - ومرغیرا نیز گفته‌اندسیاه
بلدرچین خوانند . رنگك وبطی, السیربعنی تند قواند پرید۷ .
کراکا ؟ - بفتح اول بر وزن سراپا: کراوش - بکر اول و ضم همزه بر
بمعنی کراك است وبسنی عکه وبسنی صموه‌وبسنی | وزن بیپوش » چرخ روغنگری راکوبند .
بلدرچین کوبند واسح آنست که پرنده‌ای باشد دم کر او یا < بممتی کراوبه است که زبره
درا ز که پیوسته درکنارآب نشیند ودم جنباند. رومی باشد وآنرا بانخواه نیز کوبند .
کر ا کر - بفتح‌اولوکاف بروزن سراسر, کراه ۸ ه بر وزن تباه ۰ بمعنی کار
زاغ راکوند وان پرادده‌است معروف ؛ و بخم واشها ونهات باشد .

(۷) چك » چش : - و . ۱

۸3-۱ در قرابادینها لیاقتم . عجب است که اکزاغ با زاء ( منقوطه ) را هم بهمین معنی
شبط کرده (جهانگیری) » « فرهنگه نظام > . ۴ - «کراکه » مرغیست دم درازسیاه‌وسپید
و درکنار رودها بود . دقیقی (طوسی) کوید :

چنان اندشد او از دشمن خوش چو باز تیز چنگال از کرا6 . »
« لغت فری ۰۲۵۲۹
« جهانگیری کراکک را عفعق داسته و رشیدی صموه » اما هیچکدام با بیان لغت‌الفری مطایق
نمی‌سازد .> « فرهنگه نظام > لغة با «کر کت > تجانس دارد . ۴ - اصل «کراکه ؛است.
لفت. نوبان الف اطلاق آخر بیت دقیقی را ( رك : ح» ) اصلی پنداشته‌اند 1.

۴ - «کراکر اسم شقراق (کلاغ پیسه) است » «محیطاعظم» جهانگیری « کرا که > را
را بهمین معنی نوشته «فرهنگه نظام» . اظ . مصحف « کراکه > است. .

9 * کرانه (ه.م.) << کنار < کناره ( هم. ) ؛ اوستا - 52۲888 ( جاب ؛ طرف »
اشها ) ؛ پهلوی 1۳208۴ ۰ 152288۴ . استی 8708 ( انشا ) ؛کردی ع » افقانی‌ع 1087
« اسشق ۸4۹ *. ‎٩‏ - رك :کران . ۷ - مسحف «کرایه» (ه.م.).

۸ - ظ. مسحف «کران > و «کرانه » (۸.م.) .
```


## [2026-09-14T02:02:44.953Z] TOOL CALL #48: Bash

```json
{
 "command": "python3 tools/ref_page.py BQT:1699 2>&1 | head -50",
 "description": "Fetch BQT page 1699"
}
```


### [2026-09-14T02:02:53.217Z] TOOL RESULT

```
REF: BQT:1699  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 492  OCR-lang: fas

-۱۹۹۹- .کبده
و باین معنی با زای نقطه دار هم آمده ات - گویند که برآن چیزها آویزند۹ - ودواسطلاج
و میوه ای باشد که آنرا موز میگوبند -ونقیض | قلاب راخصوصاً قلابیکه تسابان برآن گوشت‌بند
میان هم هت - و بکر اول بمعنی آغوش | کنند .
باشد ‎٩‏ - وبمعتی جدایی هم کفته‌اند ۴ . کناز ۷ - بفتح اول بر وزن تما ۰ بن

کنار نگ ۴ - بنم اور و قح رای وبیخ خوشةٌ خرما راگوبند ‏
قرشت وسکون نون وکاف فارسی » والی وحاکم کناغ < جم اول بروزن مراغء بمعی
و شحنةٌ ولایت او خداوند زمین باشد که او دا [ کرم پیله باشد بیمای کرمیکه برابريشم می‌تند ۸
مرزبان کوبند ۱ چه کنابممنی زمین ورنگه‌بممتی - و بمعنی تار رسمان و تار آبرشم ‎٩‏ و بار
والی وخداوند هم آمده است وبقّح اول‌نیزدرست عنکبوت همهت - ویمعنی طرف وجللب وکتار
است ۴ . هم بنظرآمده است .
کنا 2 - بفتح اول بروزن هزاره,بممنی کناك - بفتح اول پروزن‌مغاد. پیجش
کنارهرچیز باشد ‎٩‏ - وقلابآهنین رانیز کوبند شکم راکوبند و بعربی زحیرخوانند *۹-ویمعتی
ومعرب آن قناره است و قناره دزلغت هرچیزبرا هرد شکم لیز کفته‌اند .
‎٩‏ - نیز بمعنی ساحل » بغردومعتی :
با زر بهر دودست کند خواجه درکنار با موج روزّی افکندش مرده‌ب رکناز.
«کلسان س ۳۸
۴ - بمعانی اخیر * کران (ه.م.) «اسشق ص۱۹۳ ۳ کناره ** کرانه ؛ کردی 861087
(کنار , جانب » ساحل ) ۰ ۷64۵۲6 ( جدا) » زازا 16۲۵۲ « ژابا صس ۳4۳ >. دارمستش
کوید :کنار از ربشة اوستایی 1۳2۳288 (کنار) » پهلوی ۳284۴ است « تنبعات ج ٩ص‏ ۱۱۵
۴ - پپلوی ۴۸8۹2۲۵8 ( بنقل پونانی 328273808069 ۰ بربانی 0288780)
وآن در عهد ساسانی عنوان مخصوص مرزبان ناحيةٌ « ابرشهر » ات که کرسی آن نیشاپور بود -
کریتنن . ساسان ص ۱*۸ .
۴ - «کنارنگ » صاحب طرف بود و هرزبانش نیز کویند . فردوسی گوید :
ازین هر دو هر کز انگشتی جدا کنارنگك بودند و او پادشا . »
« هت فرص ۰
۵ << کرانه , پهلوی 122721 » اوستایی ۳8۳882 « دارمستتر . تبعات ج چص
۹ رك :کنار »کران + کرانه . ‎٩‏ - قتاره , جمع قنانر 66۴ 46 ۳۳1061361 ( فر )
« دزی ج ۲ص 5۱۱ . ۷ از » (وم.) ‏ کنز(هم.) .
۸ - گرنه بهر خزانهٌ تو بود ند رعته از لعاب کناعغ .
مد همگر « رشیدی > .
‎٩‏ - «کناغ » تاری که از آن بیرم با دیبا بافند . منجيك (ترمذی) کوید :
ز سیمین فغی من چو زرین کناغ زتابان مهی هن چو سوزان چراغ .>
لت قری ۲۳۸ 6 -
۶ عارضش چوشودکناك وتبودصادق میدان که پنزديك ظبیب صادق
از خوردن معجون بنفج کردد بر ماده مرض طبیمت فایق .
بوسفی طبیب « فرهنک نظام ‎ »‏
```


## [2026-09-14T02:03:02.976Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && grep -n \"کورش\\|کوروش\" BQT_v3_pages.txt BQT_v4_pages.txt BQT_v5_pages.txt 2>/dev/null | head -20",
 "description": "BQT Kurosh"
}
```


### [2026-09-14T02:03:03.034Z] TOOL RESULT

```
BQT_v4_pages.txt:515:پدست کوروش هغامنشی منقرض شد ( ایران باستان ج۱ ص ۱۹۸ بیعد ). - و سکن این قوم
BQT_v4_pages.txt:2970:آنمونهٌ آثر! آزامگاه کوروش در پازارکاد ( پارس ه کرد ) معرفی میکند « 118 مه
BQT_v4_pages.txt:4096:کمانا که باسم بردیا برادر کبوجیه و پسکوروش سلطنت هغامنشیان را سب کرده خود را پادشاه
BQT_v4_pages.txt:16180:هخامنشی(ه.م.) وجد اعلای کورش ودارپوش امت .
BQT_v4_pages.txt:16184:4۶ مللة هغامنشی » از زمان جلوی کوروش بزر که (0۵۰ ق م.) تافوت داربوش سوم
BQT_v4_pages.txt:17782:درآن مندرج است . مطالبی دیده میشودکه متعلق بحکایت کوروش کبیر است . حتی کشتن‌اردشیر
BQT_v4_pages.txt:18244:شهپر کشوده و در سر نیز بلندی بسرافراشته بهمه نمودار بود . کزافون در کورشنامه
BQT_v4_pages.txt:18245:(4 ,7 3۲0803010 ) در لشکر کشی کورش بسوی بابل مینوسد : « درف پادشاهی ابران
BQT_v3_pages.txt:6299:و شمیده باشد ۱۱ ‎om‏ که مذ کورشد ودریم
BQT_v3_pages.txt:18034:کزنفون ( در « کورش‌نامه » وه انباز ‎Ce‏ و پلوتارخس مینوبسند درختان آنبوه وتناور داشتندوآب
BQT_v3_pages.txt:29314:۴ - رود کر ( کوروش) » در کتب ‎Olay Jie‏ اسلامی‌کر ( بضم اول و تشدید دوم )
BQT_v3_pages.txt:29321:۴ - رود کر (کوروش) ییکی از رودهای فارس است که در
BQT_v3_pages.txt:34401:دولت‌در۵۳۹ ق.م. بدست کوروش‌شپربار هضامنتی ابران منقرضکردید ( تاریخ ‎Me‏ شرق‌ویونان.
BQT_v3_pages.txt:38230:‎gly Meee‏ ۲5 ۱۷- کوروش
BQT_v3_pages.txt:38233:‏حالت‌فاعلی کوروش 07558 . ودرصیغهةمفرددن کر حالت‌اضافی(مضاف‌الیه)
BQT_v3_pages.txt:38239:‏کوروش ‎ET ye‏ )004 -۵۲۹ ق . م. ) پسرچیش پش, سردودمان
BQT_v3_pages.txt:38244:و فریگیا را ضمیمةٌ ابران کرد . کوروش بهودبانی را که در بابل ‎pel‏
BQT_v3_pages.txt:38247:بنا کرد. وازسوی مشرق وجنوب تا رود سند ‎CEU‏ . کوروش در زدوخورد
BQT_v3_pages.txt:38252:‏کوروش درمیان اشخاص تاربخی‌نهد قدیم » یکی ازرجالکم نظیر
BQT_v3_pages.txt:38255:ذ کر میشود : کوروش » اسکندر وقیصر (ژول‌سزار) . اشتهار اودرمیان‌ملل
```


## [2026-09-14T02:03:06.053Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT && sed -n '38225,38270p' BQT_v3_pages.txt",
 "description": "BQT Kurosh entry"
}
```


### [2026-09-14T02:03:06.129Z] TOOL RESULT

```
‎. ‏کل‌ميخ » رد : کرمیخ‎ eT ‏-ظ‎ ٩

‎CoS ALS - ‏کوربا‎ ۷
[pdf page 520]
‎gly Meee‏ ۲5 ۱۷- کوروش
‎H‏ کود وش - درپارسی‌باستان کورو - ۰1607۷ درصيفةٌ مفرد مف کر

‏حالت‌فاعلی کوروش 07558 . ودرصیغهةمفرددن کر حالت‌اضافی(مضاف‌الیه)
‎Kéraush‏ ۰ این تام در کتببه‌های عبلامی 1-29 ؛ ودر ‎Gea‏ بابلی

‎: ‏ودریونانی 5 آمده . رل‎ , 1-2-6
( Kent, Old Persian, p. 180).

‏کوروش ‎ET ye‏ )004 -۵۲۹ ق . م. ) پسرچیش پش, سردودمان
هخامنشی است که بر آ خرین ‎oltol‏ ماد موسوم به ایشتوو 9 ‎Ishtuvigu‏
‏خروج کرد؛ وپادشاهی‌را ازقوم ماد بقوم‌پارسی‌منتقل‌ساخت. وی ارمستان
را مطیع کرد و با بابلیان جنگید » ‎Job‏ ولودیا ( لیدی ) را تسخیر نمود
و پادشاه کشور اخیر کرزوی را اسبر ( ولی او را ءورد عفو قرار داد )
و فریگیا را ضمیمةٌ ابران کرد . کوروش بهودبانی را که در بابل ‎pel‏
‏بودند آزاد کرد و ‎Bibel‏ رجعت به بیت المقدس داد - وی از طرف شمال
شرقیتا رودسبحون ‎(bie pes)‏ بیش رفت ودر کنارآن رود شهری باسم خود
بنا کرد. وازسوی مشرق وجنوب تا رود سند ‎CEU‏ . کوروش در زدوخورد
باییکی از قبایل سکایی در شمال ابران زخم برداشته کشته شد » و بقول
دیگر در پاری بمرلك طبیعی در گذشت . آرامگاه وی در مشهد مرغاب
(فارسی) است .

‏کوروش درمیان اشخاص تاربخی‌نهد قدیم » یکی ازرجالکم نظیر
‎cul‏ که نامشان در آذهان ملل عهدهای مختلف ‎SL‏ مانده است » حتی
میتوان ‎CAT‏ که ازین‌حیث‌اوبکی‌ازسه مردیس تکه بترتیب‌تاریخ‌اسمشان
ذ کر میشود : کوروش » اسکندر وقیصر (ژول‌سزار) . اشتهار اودرمیان‌ملل
زنده‌چند ‎oye‏ دارد: نخست‌باید گفت که پیامبران‌بنی‌اسرائیل اورابسیار

‏ستوده‌ ند وپیروان مذاهنی که توربة را مقدس میدانند » از کود کی اسم
[pdf page 521]
آرامگاه کوروش - مشهد مرغاب ( فاری )

کوروش
[pdf page 522]
‎wre‏ کوروش
کوروش‌را ‎att‏ وبا ‎ry OT‏ شده اين شاه‌را محترم میشمارند ‏ ثاناً
کوروش را مورخان عبد قدیم و ‎war‏ باتفاق ‎Gh‏ دولتی میدانتد که از
حیث وسعت سابقه نداثت ‏ واز سیحون تادربایمفرب واحمر «متدبود.
ولی ‎Sl‏ قدریدقیق‌شويم » روشن‌است که‌شنون کوروش از جهانگیر بهای
اونیست,زیرا قبل ازاوهصرباپل و آسورپادشاهان عظیمالشن وجهانگیران
تامی داشتند . اهمیت کوروش از طرز سلوك ورفتاری است که در مشرق
```


## [2026-09-14T02:03:20.889Z] TOOL CALL #51: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 5
}
```


### [2026-09-14T02:03:20.895Z] TOOL RESULT

```


```


## [2026-09-14T02:03:24.684Z] TOOL CALL #52: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%DA%A9%D8%B1%D8%A7%D9%86",
 "prompt": "Give the Persian entry for کران (karān): meaning and full etymology (Middle Persian, Avestan, Proto-Iranian forms), and any related forms کرانه, کنار, کناره."
}
```


## [2026-09-14T02:03:26.488Z] TOOL CALL #53: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%DA%A9%D9%86%D8%A7%D8%B1",
 "prompt": "Give the Persian entry for کنار (kanâr): meaning and full etymology — Middle Persian kanārag, Avestan karana-, Proto-Iranian, metathesis/dissimilation notes, and Hasandust or other citations."
}
```


### [2026-09-14T02:03:30.776Z] TOOL RESULT

```
# Persian Entry: کران (karān)

## Meaning
Border, edge, bound, or boundary.

## Etymology
The word descends from Middle Persian (klʾn' /karān/), ultimately from Proto-Iranian *karana- ("edge, border, limit"). Scholars believe this derives from either Proto-Iranian *kar- ("to draw a line, furrow") or *kar- ("to cut, carve").

The first root traces to Proto-Indo-European *kʷel- ("to move, revolve"), while the second connects to *((s)ker- ("to turn, bend").

## Related Forms
- **بیکران** (bikarān): "boundless, unbounded" — a derived term meaning without limits or boundaries
- **کنار** (kenâr): Listed as "a metathesized form" in the etymological discussion, representing a variant development of the same root

## Cognate Evidence
The etymology notes parallels in Avestan karan ("border, edge") and Ancient Greek korōnós ("curved, crooked"), supporting the ancient pedigree of this word across Indo-European languages.
```


### [2026-09-14T02:03:33.858Z] TOOL RESULT

```
# Persian Entry: کنار (kanâr)

## Meaning
The word کنار has two distinct etymologies in Persian:

**Etymology 1** encompasses the primary meanings:
- Side; edge, limit, or boundary
- Shore or coast
- In poetic usage: embrace, hug, or metonymically, chest/bosom

**Etymology 2** refers to a botanical term:
- *Ziziphus* genus plants, particularly *Ziziphus spina-christi*

The term also functions as a preposition meaning "next to" or "besides," and as an adverb meaning "aside."

## Full Etymology

**Etymology 1** derives "from Middle Persian" with the notation "[script needed]" (knʾl /⁠kanār⁠/, "side, edge"). The source involved "a metathesis of _کران_ (karân, 'border, edge')."

**Etymology 2** was "inherited from Middle Persian" [Book Pahlavi needed] (kunār), with comparative forms cited in Classical Syriac, Old Armenian, and Late Koine Greek—all identified as "Iranian borrowings."

The cited reference sources include etymological dictionaries by Edelʹman (2011) and Nourai (2011), plus Monchi-Zadeh's work on Xurāsān vocabulary.
```


## [2026-09-14T02:03:41.183Z] TOOL CALL #54: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%CE%BA%CE%BF%CF%81%CF%8E%CE%BD%CE%B7",
 "prompt": "Ancient Greek κορώνη: meanings and etymology; also any mention of κορωνός (korōnós) \"curved\" and the Latin borrowing corona."
}
```


## [2026-09-14T02:03:43.129Z] TOOL CALL #55: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Cyrus",
 "prompt": "Etymology of the name Cyrus: Old Persian Kūruš, Greek Kyros, Elamite, and what modern scholars say about its origin (Elamite? Iranian? meaning 'sun'? 'young'?). Quote citations."
}
```


### [2026-09-14T02:03:46.968Z] TOOL RESULT

```
# κορώνη: Ancient Greek Word Analysis

## Primary Meanings

The Ancient Greek term **κορώνη** (korṓnē) encompasses multiple senses:

1. **Avian references**: A seabird (possibly a shearwater) and a crow
2. **Curved objects**: Door handles, the tip of a bow, ship sterns, and plow-beam tips
3. **Anatomical**: The coronoid process of the ulna
4. **Figurative**: End, tip, point, culmination (especially of festivals)
5. **Other**: Nightingale, types of crowns

## Etymology

The word derives from Proto-Indo-European *ḱorh₂- meaning "crow" or "raven," with similar formations across Indo-European languages. Scholars note it shares roots with Latin *cornīx* ("crow"). The term likely has onomatopoetic origins. Interestingly, while some linguists historically separated the "curved object" senses from the "crow" sense, they probably share a common origin through semantic extension—the curved appearance resembling "a crow's beak or claws."

## Latin Connection

The word eventually entered Latin as **corōna**, which itself spawned numerous descendants across Romance languages and influenced English "corona."
```


### [2026-09-14T02:03:48.534Z] TOOL RESULT

```
# Etymology of Cyrus

Based on the Wiktionary entry, here's what scholars identify about the name's origin:

## Primary Etymology Path

The name traces back through: Old Persian **kuruš** → Ancient Greek **Kûros** → Latin **Cȳrus** → English **Cyrus**

## Proposed Origins

The entry presents two competing etymological theories:

**Theory 1 (Primary):** Direct Old Persian descent from *kuruš*, with the Greek form borrowed from Persian sources.

**Theory 2 (Alternative):** A possible connection to Urartian *KURqu-ri-a-ni* (Quriani), referring to a land in the upper Kura river region, suggesting a geographical rather than personal origin.

## Folk Etymology

The entry notes: "As a saints' name it has been identified by folk etymology with Ancient Greek *kúrios* ('lord')."

## Modern Scholarship

The Wiktionary article doesn't provide extensive modern scholarly commentary on the name's ultimate meaning. It documents the attested linguistic pathway but doesn't definitively confirm whether the original Persian term meant "sun," "young," or other proposed meanings that scholars have suggested.
```


## [2026-09-14T02:03:55.120Z] TOOL CALL #56: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%CE%BA%CE%BF%CF%81%CF%89%CE%BD%CF%8C%CF%82",
 "prompt": "Ancient Greek κορωνός (korōnós): meaning and etymology. Is it derived from PIE *(s)ker- 'to turn, bend'? What does it say about related κορώνη and Latin corona?"
}
```


## [2026-09-14T02:03:56.922Z] TOOL CALL #57: WebFetch

```json
{
 "url": "https://www.iranicaonline.org/articles/cyrus-i-name",
 "prompt": "Encyclopaedia Iranica entry on the name Cyrus (Kuruš): what does Rüdiger Schmitt say about its etymology and meaning? Elamite? Iranian? 'sun'? Quote the key sentences."
}
```


### [2026-09-14T02:03:58.016Z] TOOL RESULT

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-14T02:04:00.860Z] TOOL RESULT

```
# κορωνός: Etymology and Meaning

**Meaning:** The Ancient Greek adjective κορωνός (korōnós) means "curved" or "crooked."

**Etymology:** According to the Wiktionary entry, it derives from Proto-Indo-European *(s)ker-, which means "to turn, bend." The document notes that "Cognates include Latin curvus, Old Irish cruind, and Proto-Slavic *krivъ."

**Related Terms:** The entry mentions κορώνη (korṓnē) as a related form, though the page notes "See also κορώνη." This suggests a connection between the two terms, though the specific relationship isn't elaborated in the provided content. Notably, the Latin cognate "curvus" (curved) shares this common root, illustrating how the sense of curvature or bending was preserved across Indo-European languages.

The word itself is an oxytone adjective following first and second declension patterns in Attic Greek, with derived forms including the adverb κορωνῶς and comparative/superlative formations.
```


## [2026-09-14T02:04:04.538Z] TOOL CALL #58: WebSearch

```json
{
 "query": "Schmitt Encyclopaedia Iranica \"Cyrus\" name etymology Kuruš Elamite \"humiliator of the enemy\""
}
```


### [2026-09-14T02:04:10.887Z] TOOL RESULT

```
Web search results for query: "Schmitt Encyclopaedia Iranica "Cyrus" name etymology Kuruš Elamite "humiliator of the enemy""

Links: [{"title":"Schmitt, Rüdiger - Encyclopaedia Iranica","url":"https://www.iranicaonline.org/scholar/rudiger-schmitt/"},{"title":"CYRUS i. The Name - Encyclopaedia Iranica","url":"https://www.iranicaonline.org/articles/cyrus-i-name/"},{"title":"CYRUS — Brill","url":"https://referenceworks.brillonline.com/entries/encyclopaedia-iranica-online/*-COM_7908"},{"title":"Iranians in Neo-Elamite Texts 211 2.3.3. Pseudo-Iranica 2.3.3.1. Personal Names","url":"http://www.historycy.org/index.php?act=Attach&type=post&id=21893"},{"title":"IRAN vii. NON-IRANIAN LANGUAGES (1) Overview - Encyclopaedia Iranica","url":"https://www.iranicaonline.org/articles/iran-vii1-non-iranian-languages-overview-/"},{"title":"Cyrus","url":"https://en.wikipedia.org/wiki/Cyrus"},{"title":"Cyrus Name Meaning: Gender, Variations & Popularity","url":"https://momlovesbest.com/cyrus-name-meaning"},{"title":"Kourosh","url":"https://en.wikipedia.org/wiki/Kourosh"}]

Based on the search results, I found relevant information from Schmitt's Encyclopaedia Iranica article on the name Cyrus:

The name Cyrus (Latin form of Greek Kûros, later also Kóros) comes from Old Persian Kuruš [spelled ku-u-ru-u-š], reflected in Elamite Ku-raš.

The etymology of the name, which may be connected with Old Indian Kúru-, remains in dispute. Although sometimes given as "young, child, adolescent," it is more likely to be understood as "humiliator of the enemy in verbal contest" (proposed by Karl Hoffmann).

The search successfully located Schmitt's entry in Encyclopaedia Iranica discussing the etymology of Cyrus/Kuruš and its Elamite form, including the interpretation as "humiliator of the enemy in verbal contest."


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-14T02:04:16.684Z] TOOL CALL #59: WebFetch

```json
{
 "url": "https://en.wikipedia.org/wiki/Cyrus",
 "prompt": "Etymology of the name Cyrus / Kūruš: what scholars (Schmitt, Hoffmann, Tavernier) propose; Elamite Kuraš; Ctesias/Plutarch claim that it means 'sun'. Quote key sentences with citations."
}
```


## [2026-09-14T02:04:17.847Z] TOOL CALL #60: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/ribbon",
 "prompt": "Etymology of 'ribbon': Old French riban, Middle Dutch ringband; is it connected to Germanic *hringaz 'ring'?"
}
```


### [2026-09-14T02:04:22.107Z] TOOL RESULT

```
# Etymology of Cyrus/Kūruš

## Scholarly Proposals

**Schmitt and Hoffmann** propose that the Persian *Kuruš* may derive from Indo-European roots. Hoffmann specifically suggests it connects to the IE root *\*(s)kau* meaning "to humiliate," making *kuruš* mean "humiliator (of the enemy in verbal contest)."

**Tavernier** argues that the Elamite *kuraš* represents "the original form" and means "to bestow care," viewing it as an Elamite rather than purely Persian name.

**Harmatta** connects the name to "the common Iranian root 'kur-' (be born)," concluding that *Kūruš* means "young, youth."

## Classical Claims About "Sun"

Ancient sources offered different interpretations. **Plutarch** asserted that "the sun, which, in the Persian language, is called Cyrus." Similarly, **Ctesias** wrote in his *Persica* that "the name Cyrus is from the Persian word 'Khur' (the sun)."

However, modern scholars reject these classical etymologies. The Wikipedia article notes: "These are, however, not accepted by modern scholars."
```


### [2026-09-14T02:04:22.682Z] TOOL RESULT

```
# Etymology of "Ribbon" and Possible Ring Connection

Based on the provided source, the etymology of "ribbon" does not establish a connection to Germanic *hringaz ('ring').

The Online Etymology Dictionary states that ribbon comes from "Anglo-French _rubain_, Old French _riban_" with "a word of unknown origin, possibly from a Germanic compound whose second element is related to band (n.1); compare Middle Dutch _ringhband_ 'necklace.'"

The source mentions a Middle Dutch term that includes "ringh-" (which could relate to ring), but this appears only as a speculative comparison for the *band* component of "ringhband," not as a confirmed etymological root for ribbon itself. The dictionary explicitly notes the origin remains uncertain, offering only a tentative hypothesis rather than confirming any ring-related connection.

To definitively answer whether ribbon connects to *hringaz would require etymological sources beyond this page.
```


## [2026-09-14T02:04:30.664Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nfor w in ['ribbon, riband','ribbon,','riband, ribbon']:\n    i=t.find(w)\n    print(w, i)\nfor m in re.finditer(r'ribbon', t):\n    s=t[max(0,m.start()-200):m.start()+500]\n    if 'OF.' in s or 'F. ruban' in s or 'riban' in s:\n        print('---'); print(' '.join(s.split())[:700]); break\nEOF",
 "description": "Klein ribbon"
}
```


### [2026-09-14T02:04:32.010Z] TOOL RESULT

```
ribbon, riband -1
ribbon, 923590
riband, ribbon -1
---
‘bracelet’ ; F. bande, ‘band’, is a Teut. loan word. See bind and cp. bend, bond. Cp. also bandage, bandanna, bandhava, bandhu, bandoleer, and the second element in ribband, ribbon, roband, seerband. Derivatives: band, tr. and intr. v., band-ed, adj., band-er, n., band-ing, n. band, n„ troop. — F. bande, fr. OProven?. banda, fr. Goth, bandwa, bandwo, ‘sign, signal’. See banner and cp. disband. bandage, n. — F„ fr. bande, fr. OF. bende, fr. ML. benda, ‘a band’, fr. Goth. *binda, which is rel. to E. band, ‘tie’ (q.v.) For the ending see suff. -age. Derivatives: bandage, tr. v., bandag-er, n., bandag-ist, n.
```


## [2026-09-14T02:04:34.655Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\ni=t.find('ribbon,',920000)\nprint(' '.join(t[i-300:i+900].split()))\nEOF",
 "description": "Klein ribbon entry"
}
```


### [2026-09-14T02:04:35.793Z] TOOL RESULT

```
-, ‘to bind’, whence also OI. bandhdh, ‘a tying, fastening; band, bandage’, Mir. bainna, ‘bracelet’ ; F. bande, ‘band’, is a Teut. loan word. See bind and cp. bend, bond. Cp. also bandage, bandanna, bandhava, bandhu, bandoleer, and the second element in ribband, ribbon, roband, seerband. Derivatives: band, tr. and intr. v., band-ed, adj., band-er, n., band-ing, n. band, n„ troop. — F. bande, fr. OProven?. banda, fr. Goth, bandwa, bandwo, ‘sign, signal’. See banner and cp. disband. bandage, n. — F„ fr. bande, fr. OF. bende, fr. ML. benda, ‘a band’, fr. Goth. *binda, which is rel. to E. band, ‘tie’ (q.v.) For the ending see suff. -age. Derivatives: bandage, tr. v., bandag-er, n., bandag-ist, n. bandanna, bandana, n., a colored and spotted handkerchief. — Hind, bandhnu, ‘a mode of dyeing in which the cloth is tied in various places to prevent these places from receiving the dye’, rel. to bandhdh, ‘a tying, fastening; band, bandage’. See bind and cp. band, ‘tie’. Cp. also bandhu, pandal. bandeau, n., a narrow band, fillet. — F., fr. earli
```


## [2026-09-14T02:04:39.526Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nfor f in ['KLN_1966.txt','KLN_1971.txt']:\n    t=open(f,encoding='utf-8',errors='replace').read()\n    for m in re.finditer(r'rib+[ao]nd?,? n\\.|ribbon, n\\.|riband, n\\.', t):\n        print(f, m.group(0))\n        print(' '.join(t[m.start():m.start()+600].split()))\n        print()\nEOF",
 "description": "Klein riband/ribbon headword"
}
```


### [2026-09-14T02:04:40.828Z] TOOL RESULT

```
KLN_1971.txt riband, n.
riband, n., a ribbon (archaic). — Older spelling of ribbon, with excrescent -d. Derivative: riband-ed, adj. (cp. ribboned). ribband, n. (naut.) — Compounded of rib and band, n. Derivative: ribband, tr. v. ribbon, also riband, n. — ME. riban(d), fr. OF. riban , var. of ruban (F. ruban), fr. MDu. ringh- band, ‘necklace’. The first element of this com- pound is rel. to E. ring, n., the second to E. band, ‘a tie’. Derivatives: ribbon-ed , adj., ribbon-y , adj. Ribes, n., a genus of shrubs, the currant. — ML., fr. Arab, ribas , ‘sorrel’, fr. Pers. revas. riboflavin, n., a factor of

KLN_1971.txt ribband, n.
ribband, n. (naut.) — Compounded of rib and band, n. Derivative: ribband, tr. v. ribbon, also riband, n. — ME. riban(d), fr. OF. riban , var. of ruban (F. ruban), fr. MDu. ringh- band, ‘necklace’. The first element of this com- pound is rel. to E. ring, n., the second to E. band, ‘a tie’. Derivatives: ribbon-ed , adj., ribbon-y , adj. Ribes, n., a genus of shrubs, the currant. — ML., fr. Arab, ribas , ‘sorrel’, fr. Pers. revas. riboflavin, n., a factor of the vitamin. B complex C 17 H 20 O 6 N r — Coined fr. ribose and flavin. ribose, n., a pentose sugar. — Formed with subst. s

KLN_1971.txt riband, n.
riband, n. — ME. riban(d), fr. OF. riban , var. of ruban (F. ruban), fr. MDu. ringh- band, ‘necklace’. The first element of this com- pound is rel. to E. ring, n., the second to E. band, ‘a tie’. Derivatives: ribbon-ed , adj., ribbon-y , adj. Ribes, n., a genus of shrubs, the currant. — ML., fr. Arab, ribas , ‘sorrel’, fr. Pers. revas. riboflavin, n., a factor of the vitamin. B complex C 17 H 20 O 6 N r — Coined fr. ribose and flavin. ribose, n., a pentose sugar. — Formed with subst. suff. -ose fr. G. Ribon(saure ), a tetrahydroxy acid, whose first element is an alteration of E.
```


## [2026-09-14T02:04:49.567Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('KLN_1971.txt',encoding='utf-8',errors='replace').read()\nfor pat in [r'crown, n\\.', r'corona, n\\.', r'ridge, n\\.', r'\\bring, n\\.', r'shrink, intr', r'circus, n\\.', r'search, tr', r'curve, tr', r'crest, n\\.', r'crisp, adj', r'range, n\\.']:\n    m=re.search(pat,t)\n    if m:\n        print('>>>', m.group(0))\n        print(' '.join(t[m.start():m.start()+560].split()))\n        print()\nEOF",
 "description": "Klein English derivatives"
}
```


### [2026-09-14T02:04:51.178Z] TOOL RESULT

```
>>> crown, n.
crown, n., and cp. rote, ‘a musical instrument’. crowd, intr. and tr. v., to press. — ME. cruden , crouden, fr. OE. crucian, ‘to press, push’, rel. to MDu. cruden, later kruyden, kruyen, Du. kruien, ‘to push’, MHG. kroten , ‘to press, op- press’. Cp. cord. Derivatives : crowd, n., multitude, crowd-ed, adj., crowd-ed-ly, adv., crowd-ed-ness, n., crowder (q.v.) crowder, n., one who or that which crowds. — Formed fr. prec. word with agential suff. -er. crowder, n., one who plays on a crowd (archaic). — Formed fr. crowd, ‘a musical instrument

>>> corona, n.
corona, n., a crown. — L. corona, ‘garland, wreath, crown’, fr. Gk.xopcov^, ‘anything curved ; a wreath, garland’. See crown, coronach, n., a dirge. — Gael, corranach, fr. Mir. com-, ‘with’ (see com-), and ranach, ‘a roaring, weeping’, fr. ran , ‘to roar, weep’, coronal, adj., pertaining to a crown. — L. coro- na l is, ‘pertaining to a crown’, fr. corona. See corona and adj. suff. -aL Derivative : coronal-ly, adv. coronal, n., circlet, diadem. — L. corondlis, ‘per- taining to a crown’. See coronal, adj. coronary, adj., 1) pertaining to a crow

>>> ridge, n.
ridge, n., structure spanning a river, etc. — ME. brigge , brig, etc., fr. OE. brycg, bricg, rel. to OS. bruggia, ON. bryggja, bru, Dan. bro, Swed. brygga , OFris. brigge , bregge, Du. brug, OHG. brucca , G. Briicke; prob. orig. ‘bridge of beams’, and derived fr. I.-E. base *bhru-, *bhreu ‘beam, log’, whence also Gaulish briva, ‘bridge’, OSlav. bruvuno , ‘beam’, Serb, brv, ‘footbridge’. Derivatives: bridge, tr. v., bridg-ed, adj., bridg- ing, n. bridge, n., a card game resembling whist. — First mentioned as Biritch or Russian Whist; of un- k

>>> ring, n.
ring, n. earl, n., a title of nobility. — ME. erl, fr. OE. eorl, ‘man, warrior, chief, nobleman’, rel. to ON. jar l, ‘chief, nobleman', OS., OHG. erl, ‘man’. Cp. Jarl. earl, tr. v., to pledge (Scot.) — Rel. to ME. erles, erres, ‘earnest money’, fr. OF. erres, fr. L. arra. See earnest, ‘pledge’, and cp. words there re- ferred to. earldom, n. — ME. erldotn, fr. OE. eorldom, fr. eorl. See prec. word and -dom. early, adv. — ME. erliche, erli, fr. OE. xrltce, ‘early’, compounded of xr, ‘before’, and suff. -lice. See ere and adv. suff. -ly. D

>>> shrink, intr
shrink, intr. and tr. v. — ME. schrinken, shrinken, fr. OE. scrincan , rel. to MDu. schrinken and prob. to Dan. skrumpe, Swed. skrympa, ‘to shrink’, Norw. skrumpa , ‘a meager cow’, MDu. scrompelen , Du. schrompelen, G. schrumpfen, ‘to shrink’, and to OE. scrimman, ‘to bend, writhe, dry up, shrink’. See shrimp and cp. scrag. Derivatives: shrink-age, n., shrink-ing, n., shrink-ing-ly , adv. shrive, tr. v. — ME. schriven, shriven, fr. OE. 'scrifan, ‘to impose penance; to decree; to shrive’, fr. L. scribere , ‘to write’, whence also OS. scriba

>>> circus, n.
circus, n. — L. circus, ‘a circle, ring, a round enclosure for games’, more prob. borrowed from, than cogn. with Gk. xtpxo;, xpixo?, ‘a ring’, fr. I.-E. base *qri-q -, enlargement of base *qer~, 10 turn, twist’, whence L. curve, ‘bent, curved’. See curve and cp. cirque, search, cricoid, cirque, n., circus. — F., fr. L. circus. See prec. word. cirrhosis, n., a disease of the liver (med.) — Medi- cal L., coined by the French physician Ren6- ThSophile-Hyacinthe Laennec (1781-1826) fr. Gk. xtp p<k, ‘orange tawny’, which is of un- certain origin;

>>> search, tr
search, tr. and intr. v, — ME. serchen, fr. OF. cerchier , fr. L. drear e , ‘to go round’, fr. circum, ‘around’. F. chercher (fr. OF. cerchier) is due to assimilation. See circum- and cp. circa, circle, circus. Cp. also research. Derivatives: search, n,, search-able, adj., search-er , n., search-ing, adj., searck-ing-ly , adv., search-ing-ness, n. season, n. — ME. sesoun, fr. OF. seson, seison, saison (F. saison ), fr. L. satidnem , acc. of sat id, ‘a sowing’, in VL., ‘sowing time, sowing season’, fr. satus, pp. of serere, ‘to sow, plant’,

>>> curve, tr
curve, tr. v. — L. curvdre , ‘to crook, bend, twist’, fr. curvus. See curve, n. Derivatives: curv-ed, adj., curv-ed-ly, adv., curv - ed-ness, n., curv-er, n. curvet, n., a leap. — It. corvetta, dimin. of corvo (now curvo ), ‘a curve’, fr. L. curvus. See curve, n., and cp. cavort. curvet, intr. and tr. v., to leap, bound. — It. cor- vettare, fr. corvetta. See curvet, n. curvi-, combining form meaning ‘curved, bent’. — Fr. L. curvus. See curve, n. curvilineal, curvilinear, adj., consisting of, bound- ed by, curved lines. Compounded of edrvi-

>>> crest, n.
crest, n. — ME., fr. OF. creste (F. Crete), fr. L. crista, ‘tuft on the head of animals, cock’s comb’, which is cogn. with Mir. cressaim, ‘I shake, swing’, ON. hrista, ‘to shake’, OHG. rista, MHG. riste, G. Reiste , ‘bundle’. These words derive from a -/-enlargement of I.-E. base *qreis-, whence OPruss. craysi, ‘blade, stalk’, crays (pi.), ‘hay’, Goth, af-hrisjan, us-hrisjan, ‘to shake off’, OE. hrisian, OS. hrissan , ‘to rattle, creak’, OE., OS., ON., OFris., OHG. hr is, later ris, MHG. ris, G. Reis, Dan., Swed. ris, MDu., Du. rijs, ‘twig, sp

>>> crisp, adj
crisp, adj., 1) brittle; 2) lively; 3) fresh; 4) curly. — OE., fr. L. crispus, ‘curly’, which is cogn. with W. crych, Bret, crech, of s.m., fr. I.-E. base *(s)qreis~, whence also L. crinis (for *crisnis), ‘hair’, and crista, ‘tuft on the head of animals, cock's comb’. See crest and cp. words there referred to. Cp. also Crispin. Derivatives: crisp, tr. and intr. v., crispate , adj. (q.v.), crisp-ly, adv., crisp-ness , n., cn'sp-y, adj. crispate, adj., of a curly appearance. — L. cw* patus, pp. of crispdre, ‘to curl, wave’, fr. crispus. See pre

>>> range, n.
range, n. — ME., fr. OF. (= F.) grange, fr. VL. *granica, fr. L. granum, ‘grain’. See grain, ‘seed, com’. granger, n., a farm steward. — OF. grangier, fr. grange. See grange and -er (representing OF. -ier). grangerism, n., the practice of grangerizing. — See next word and -ism. grangerize, tr. v„ to illustrate a book by the ad- dition of prints, engravings, etc. — Lit. ‘to il- lustrate a book in the manner in which James Granger's ‘Biographical History of England’ (1769) was illustrated. Derivatives : grangeriz-ation, n., grangeriz-er , n
```


## [2026-09-14T02:05:05.765Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^kuruos\\|kuruos\\b\" IEC.txt | head -5",
 "description": "Mann kuruos"
}
```


### [2026-09-14T02:05:05.817Z] TOOL RESULT

```
7651:kor- “bend, curve; bent, curved'. Cf. kuruos, kur- (1), koron-. (The Celt. evidence is ambig.) Arm. kor (‘curved, round, bent’; s. *curve?); Myc. & Gk. cf. kor-oónós, id. beside kor-óné "book handle’ (LW in Lat. corona); MIr. cor, ap. curu, Ir. cor, pl. coir, m. (2) ‘turn, twist beside corann ‘crown, garland’; W côr, pl. corau, m. & f. “circle? beside coryn “crown of head"
8417:kur- (1) ‘round, curved’. Cf. kuruos, kor-. WP II, 568 Arm. (ambig.) kor (fcurved, bent; curve’. Cf. kor-); Gk. kur-tós, id. (Aeolic alleged ‘kurpós’ is a misspelling for kurtós); Ir. (ambig.) cor, m. (bend, turn’. See kor-); W côr, m. & f. (‘circle’. See kor-)
8455:(kuruos ‘bent, round’. Assumed for Latin only, cf. kor-) (WP II, 568)
```


## [2026-09-14T02:05:11.922Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nt=open('IEC.txt',encoding='utf-8',errors='replace').read(); lines=t.split('\\n')\nfor n in (8417,8455,7651):\n    print(n,'leaf','\\n'.join(lines[:n]).count('\\f'))\n\"; awk 'BEGIN{RS=\"\\f\"} NR==313' IEC.txt | grep -n \"^5[0-9][0-9]$\\|^ *[0-9]\\{3\\} *$\" | head",
 "description": "IEC leaf for kuruos"
}
```


### [2026-09-14T02:05:13.074Z] TOOL RESULT

```
8417 leaf 335
8455 leaf 336
7651 leaf 304
13:548
23:549
```


## [2026-09-14T02:05:21.549Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY && grep -n \"کران\\|کناره\" ARY_pages.txt | head -15",
 "description": "Aryanpur karan"
}
```


### [2026-09-14T02:05:21.610Z] TOOL RESULT

```
655:(5۸۸/۸71۸07) نه تنها در کرانه‌های رود دانوب کوج نشین شدند پلکه در قرن دوم میلادی برای
```


## [2026-09-14T02:05:24.300Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY && grep -n \"KARAN\\|KENAR\\|KANAR\\|KORUSH\\|KURUSH\" ARY_latin_index_pages.txt | head -15",
 "description": "Aryanpur latin index"
}
```


### [2026-09-14T02:05:24.377Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T02:05:29.876Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && grep -n \"curvus\" WLD_Bd2_pages.txt | head -10",
 "description": "Walde-Pokorny curvus"
}
```


### [2026-09-14T02:05:30.250Z] TOOL RESULT

```
37744:   lat. curvus „krumm, gekriimmt, gewolbt" (Formans -no- oder allenfalls
37871:schief“ (Form aus no- wie in lat. curvus), ostlit. kralvas „schief", apy-
```


## [2026-09-14T02:05:33.652Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && sed -n '37720,37760p' WLD_Bd2_pages.txt; echo \"=== page tag ===\"; awk 'NR<=37744 && /\\[pdf page/ {p=$0} END{print p}' WLD_Bd2_pages.txt",
 "description": "WP II sker entry"
}
```


### [2026-09-14T02:05:34.798Z] TOOL RESULT

```
. (s)q[er- „drehe]i,           biegen'*     (s.   auch sqer~ „einschrumpfen“          imd   sqer-
       „springen“).
   Ygl. im allgem. (auch zu den Erweiterungen) bes. Curtius® 158, Persson
Wzerw. 30, 106, 165 f., Beitr. 864 f. Anm. 2.
  Av. skarma- „rund“, skdrayai-ra'da- EN., eigen tlich „der den Streit-
wagen kreisen laBt'^ (nicht zu gr. oqxuqa^ s. Pick I^ 142, 332, Persson
Beitr. 417 Anm. 1, Boisacq 926 gegen Barth olomae IF. 10, 199, Airan.
Wb. 1587): vielleicht ai. kundti „zieht sich zusammen, schrumpft ein“ (wenn
aus ^q^Td-no-', Persson Beitr, 753, 775, 864 Anm. 2), kfmita-h „zsgezogen
(Ader), zugeknifiPen (Auge)“, kunika „Horn“ (wenn „gekrummt“ und wohl
kuta-m „Pallstrick, Falle, Betrug“, kuta-h „trugerisch, yerfalscht^ (Peters-
son Fort. Regel. 78 f.), die aber eher zu {s)q€h „drehen“ (s. o. Peters-
son aaO.);
  alb. vielleicht keftiSy kurtis „beuge, biege“ (G. Meyer Alb. Wb. 190 zw.);
   gr. GHaiQoy        ^f^drehe mich) tanze, hiipfe, springe''          (s.   genaueres u. sqer-
„springen");
   gr.   y.vQxog      „krumm“       (alte   w-Farbung,
                                                 russ. kortocki^ sowie ksL
                                                            vgl.
s^-kr^6iti „zusammenziehen“ usw.; iiber         wie xElXog und lat. coluber
s. u. sqel- „drehen“), xoQcovog „gekrummt'’; xoQcbv7] „allerlei gekriimmtes,

gebogenes usw," (lat. Lw. corona^ vielleicht als ^koro[ii\-no-s zur w-Basis
*{s)qereu -)
   lat. curvus „krumm, gekriimmt, gewolbt" (Formans -no- oder allenfalls

von der ee-Basis); corUna „rundes Ge^B, Kessel; der DreifuB Apollos mit
dem Kessel darauf; Wolbung zwischen Himmel und Erde; cavum theatri"
s. Marstrander ZfcPh. 7, 381 Anm., Falk-Torp u. gardin^ wonach mit -ma von

einem Ptc, *qr-to „gedreht“ abgeleitet; nicht besser Fay Cl. Rev. 11, 298,
Yf. LEWb.2 s. V., wo gegen Yerbindung mit anord. huerr usw. „Schusser');
mir. cor, Acc. pi. curu „Kreise", cymr. cor-tvynf, bret. cor-uent „turbo" (s. auch
. kwrp’);
  russ. kortolki        PL f. „hockende, kauernde Stellung", klr. kortdiy sa „8ich
durchhelfen, rackern" (wenn „*sich                  krummen"? Berneker          671   zw.; vgl.
gr. HVQTog).

  Erweiterungen: (vieles im flgd. nicht aufgenommene aus dem Germ,
bei Schroeder          PBrB. 29, 489—515, 530, 532).
                                             (s)qer-                            569
=== page tag ===
```


## [2026-09-14T02:05:46.046Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '9240,9258p' BRT.txt",
 "description": "BRT karana entry full"
}
```


### [2026-09-14T02:05:46.104Z] TOOL RESULT

```
(fem-  Vi-).  ^  j    kahrkana-  m.  Name  einer  gläubigen
•  j.  "narate  (sd.)  karaiain"  N.p;.  Familie:      hufraväxs     'kananqm      asaonS
•  j.  'karana-  m.  'Ende';  i)  räumlich:  "des  gläubigen  H.,  (aus  der  Familie)  der 'Grenze,  Rand;  Ufer;  Flügel  (des  Heeres)';  A'."  YL/j.ia?.
dalinsm   upa   '■Tum   airihä  ziiiHi  YtiO.99;'  Ableit.  aus  Va^rin-,— ai,  vgl.  :*/-.<'ai?a-m.  (eine
12.  ao;  —  «va  -iia'>  ai^hä  2?m9  Vt.  lO.  95;  '^^  Rebhul.n.  auch  als)  EN,
/p,  19; — ya~ia  VIS.,  yahmäi  nsitcahmäi  •   j,    kahrkäsa-   m,  'Geier':    '53  zannu-
nalmanqm  "na'^  pairi.vasnöiie  ". .  bei  dem  mainil  (sd.)    YL  i4-  33;    —    msrrjahe  . ,
nicht   Anfang    noch    Ende    zu    gewahren  -sähe    Yt,  5,  61;    —    as.^ar}limaabyS  .  .
sind"  YLi^,3;  —  upa yaozsnta  -na''  zraya  dämattam*k?r>fi.:^arqttt  k:-r?ß paiti  nisri-
vouru.kaSaya  "an  den  wogenden  Ufern . ,"  ttuyjl  vayqm  'sam  V.J.  20.
Vt.5.  38;    —     yaoZiflli    vUpe    °n3    (NP,)''         KompA.'—     I^omp.;     *ta/iria-\-*.lia;     eig.
srayä  voumkaiaya  Y,  65. 4;  —  ys  haaiay-j  S/-'^v^'^'jU^'ond''zD"'"w',/irLter ...va  uruassayat  '«o»  Yt,5.  131;  —  ^-i  HriÄ^-^  No^T).  -  mp,  fl'ü.  Tu  V.'s  49" rasmanS  hqm.ststse  (sd.)  ^5  ^'na  ">  J'  karkäi,  vgl.  np.  (Npa,)  kargas. iHndayänti  Yt,  jj.  39;  —  yaoz)nH  »aA'«j.*kahrkäs5.parana-"  Adj. 'mit  Federn •«ff  (NP.)'>  rasmans  Ytio.36.  2)  zeitlich  ^  des  (Vogels)  Kakrklsa  versehen':  isunqm (nur  Komp.).  ^-paranum'^  Yt/o.isg.
KompE.  — np.^j«H,ianär4).~PÜ.;^a«fl™^,|       "»af"«J.:    %.  fiariiia..    —    D  NA.  kortii-irt    in
_,)ND.-')U<.them..vgl.flJfl««fl.No,i,-'      4,-,„J„,
3)  Hds. /M/fli-axrt.  —  41  Kaum  lu  ai.  *<j/(i- f.  .      ,     '  ,,      ,     .       -j      .     t.
(ZupiTEA  Germ,  Gmt.  107).  •    J-    •'^'■»t-    V.     schneiden'    Praes.    9
.  j.  »karana-  n.  ein  Kleidungsstück  mite- '  f '■^'''«■'  "^  ^^^^t""  =  k>nnv-'\  12b lererGrösse, 'Hose'');  v«.«.r?y^.^«..««^,,r'f''-'«-'':  9+^4  -f^^«va-,  n  k.r.>ya-i\ "eine  Hose,  die  die  beiden  Schenkel  be-'~  \^[^-°'''.^f"^'-     .  ,    .    -,      .
deckt"  V*  24  '■^    'schneiden,    mit    pqstd.fra^anlam
PQ.:  ti«fin-'\  —  n  Genauer  wohl  das,  was   Adv.     sva.     'schinden';     ya>a     yat     hl
```


## [2026-09-14T02:05:56.651Z] TOOL CALL #72: WebSearch

```json
{
 "query": "سیروس نام از فرانسه Cyrus کوروش وام‌واژه"
}
```


### [2026-09-14T02:06:04.254Z] TOOL RESULT

```
Web search results for query: "سیروس نام از فرانسه Cyrus کوروش وام‌واژه"

Links: [{"title":"Meaning of the name Cyro","url":"https://www.wisdomlib.org/names/cyro"},{"title":"Cyrus","url":"https://en.wikipedia.org/wiki/Cyrus"},{"title":"CYRUS i. The Name - Encyclopaedia Iranica","url":"https://www.iranicaonline.org/articles/cyrus-i-name/"},{"title":"Cyrus - Etymology, Origin & Meaning of the Name","url":"https://www.etymonline.com/word/Cyrus"},{"title":"Cyrus Name Guide: Meaning, Origin & Popularity In 2025","url":"https://www.momjunction.com/baby-names/cyrus/"},{"title":"Kourosh","url":"https://en.wikipedia.org/wiki/Kourosh"},{"title":"Cyrus - Baby Name Meaning, Origin and Popularity","url":"https://www.thebump.com/b/cyrus-baby-name"},{"title":"Meaning, origin and history of the name Cyrus - Behind the Name","url":"https://www.behindthename.com/name/cyrus"},{"title":"Cyrus: Name Meaning and Origin - SheKnows","url":"https://www.sheknows.com/baby-names/name/cyrus/"}]

Based on the search results, here's information about the name Cyrus and its Persian origins:

Cyrus (Persian: کوروش) is a Persian-language masculine given name. It is the Latinized form of Greek Kyros, from Old Persian Kurush, a name of unknown etymology.

Regarding the etymology, the Old Persian name "kuruš" has been interpreted in various forms such as "the Sun", "like Sun", "young", "hero," and "humiliator of the enemy in verbal contest." More specifically, Kourosh is composed of kouro- [sun] + -sh - [proprietorial suffix], meaning "Lord of the sun".

It is historically best known as the name of several Persian kings, most notably Cyrus the Great, who founded the Achaemenid Empire in 550 BC. The modern Persian form of the name is Kūroš.

The name traveled through languages: according to the inscriptions, the name is reflected in Elamite Kuraš, Babylonian Ku(r)-raš/-ra-áš and Imperial Aramaic kwrš. It was then adopted into Greek as Kyros and subsequently into Latin as Cyrus, which is how it entered into European languages.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-14T02:06:10.506Z] TOOL CALL #73: WebFetch

```json
{
 "url": "https://fa.wikipedia.org/wiki/%D8%B3%DB%8C%D8%B1%D9%88%D8%B3",
 "prompt": "Is سیروس a Persian male name borrowed from the European/French form of Cyrus (Grec Kyros / Latin Cyrus), i.e. a re-borrowing of کوروش? Quote what the page says about its origin."
}
```


### [2026-09-14T02:06:13.837Z] TOOL RESULT

```
# Response

Yes, according to the page, Cyrus is indeed a re-borrowing. The article states:

"سیروس یونانی شدهٔ نام فارسی کوروش است"

Translated, this means: "Sirius is the Hellenized form of the Persian name Kourosh." The page explicitly identifies it as the Greek adaptation of the original Persian name کوروش (Kourosh/Cyrus).
```


## [2026-09-14T02:06:20.762Z] TOOL CALL #74: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/hringaz",
 "prompt": "Proto-Germanic *hringaz: meaning, PIE source root, descendants (Old English hring, Frankish > Old French renc), and any note on Latin/Romance borrowings like rank/range."
}
```


## [2026-09-14T02:06:22.072Z] TOOL CALL #75: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/hrugjaz",
 "prompt": "Proto-Germanic *hrugjaz: meaning and PIE source; descendants (Old English hrycg 'ridge, back', Old High German hrukki)."
}
```


### [2026-09-14T02:06:26.444Z] TOOL RESULT

```
# Proto-Germanic *hringaz Overview

**Primary Meaning:** According to Etymology 1, this word denoted a "ring" or "circle," with an alternative sense of "curve."

**PIE Source:** The entry traces it to Proto-Indo-European *(s)krengʰ-* meaning "ring, circle." This root appears connected to an extended nasalized form of PIE *(s)ker-* ("to turn, bend").

**Key Descendants:**
- **English:** ring (via Old English hring)
- **Germanic languages:** German Ring, Dutch ring, Swedish ring, Danish ring, Icelandic hringur
- **Romance languages:** The Gothic form led to Italian aringo/arringa, which produced Old French harangue and English harangue
- **Other languages:** The word also influenced Finnic languages through borrowing

**Etymology 2 Note:** A secondary sense meaning "sound" or "ring" (the noise) exists with uncertain origins, possibly onomatopoetic or connected to different PIE roots relating to caws and croaks.

The word spread widely across Germanic and Romance languages, demonstrating significant historical linguistic influence across language families.
```


### [2026-09-14T02:06:27.721Z] TOOL RESULT

```
# Proto-Germanic *hrugjaz

This Wiktionary entry documents a reconstructed Proto-Germanic noun meaning "back," "spine," or "ridge."

## Key Information

**Meaning:** The word refers to the back of the body, the spine, or a ridge-like formation.

**Etymology:** The origin is uncertain but "appears to stem from a Proto-Indo-European" root, possibly *(s)krewk-* meaning "heap, hill; back, spine?" The connection remains "highly speculative."

**Pronunciation:** /ˈxruɣ.jɑz/

## Linguistic Descendants

The term produced numerous descendants across Germanic languages:

- **English:** ridge, rig (Northern dialect)
- **German:** Rücke (via Middle High German)
- **Dutch:** rug
- **Scandinavian languages:** rygg (Swedish, Norwegian, Danish)
- **Icelandic:** hryggur
- **Old English:** hryċġ, hriċġ

The word is classified as a masculine ja-stem noun, typical of Proto-Germanic declension patterns. Its widespread presence across modern Germanic languages demonstrates its ancient lineage within the language family.
```


## [2026-09-14T02:06:37.430Z] TOOL CALL #76: Bash

```json
{
 "command": "for u in \\\n 'https://en.wiktionary.org/wiki/%DA%A9%D8%B1%D8%A7%D9%86' \\\n 'https://en.wiktionary.org/wiki/%DA%A9%D9%86%D8%A7%D8%B1' \\\n 'https://en.wiktionary.org/wiki/%CE%BA%CE%BF%CF%81%CF%8E%CE%BD%CE%B7' \\\n 'https://en.wiktionary.org/wiki/%CE%BA%CE%BF%CF%81%CF%89%CE%BD%CF%8C%CF%82' \\\n 'https://en.wiktionary.org/wiki/Cyrus' \\\n 'https://en.wikipedia.org/wiki/Cyrus' \\\n 'https://www.etymonline.com/word/ribbon' \\\n 'https://fa.wikipedia.org/wiki/%D8%B3%DB%8C%D8%B1%D9%88%D8%B3' \\\n 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/hringaz' \\\n 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/hrugjaz' ; do\n python3 tools/fetch_source.py \"$u\" --note 'page 454, root Sker 1 (Kor-ona / Kur-wo): karan/kanar, korone/koronos, Cyrus/Kurus, ribbon, hringaz, hrugjaz' 2>&1 | tail -2\ndone",
 "description": "Archive web sources"
}
```


### [2026-09-14T02:06:43.907Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/bf2487156b74de2b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/9f370ecf5b20b363.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ea5bf3559b436559.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/1d80f614eaf394af.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/05785ac69e00e1a5.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f3b85897f3388dc8.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/5931f14e9fb938e1.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/af2dd24fa4af5da2.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/8f6e21dbb1258b96.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f5d90e33f12794c5.txt
```


## [2026-09-14T02:06:51.050Z] TOOL CALL #77: Bash

```json
{
 "command": "mkdir -p data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg454.png data/verification/sources/refs/ocr/BOOK/454.png && ls -la data/verification/sources/refs/ocr/BOOK/454.png",
 "description": "Copy page image for audit"
}
```


### [2026-09-14T02:06:51.124Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 74797 Sep 13 22:06 data/verification/sources/refs/ocr/BOOK/454.png
```


## [2026-09-14T02:06:53.943Z] TOOL CALL #78: Bash

```json
{
 "command": "sed -n '1,120p' tools/verify_check.py",
 "description": "Read verify_check"
}
```


### [2026-09-14T02:06:54.022Z] TOOL RESULT

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


## [2026-09-14T02:07:17.619Z] TOOL CALL #79: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"karana\" KNT.txt | head -10",
 "description": "Kent karana"
}
```


### [2026-09-14T02:07:17.683Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T02:09:17.946Z] TOOL CALL #80: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('SKT.txt',encoding='utf-8',errors='replace').read()\nfor pat in [r'\\bRIDGE\\b', r'\\bRING\\b,? *\\(1\\)|RING,', r'\\bSEARCH\\b', r'\\bCROWN\\b', r'\\bRANGE\\b', r'\\bSHRINK\\b', r'\\bCIRCUS\\b']:\n    for m in re.finditer(pat,t):\n        s=' '.join(t[m.start():m.start()+330].split())\n        if len(s)>60 and ('AS.' in s or 'F.' in s or 'L.' in s or 'Du.' in s or 'Icel.' in s):\n            print('>>>',s); print(); break\nEOF",
 "description": "Skeat entries"
}
```


### [2026-09-14T02:09:20.039Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T02:09:22.694Z] TOOL CALL #81: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"^ridge\\|^ring (\\|^ring,\\|^search\" SKT.txt | head -10; echo \"---\"; grep -n -i \"ridge\" SKT.txt | head -5",
 "description": "Skeat ridge"
}
```


### [2026-09-14T02:09:22.767Z] TOOL RESULT

```
1024:search.     (V  IS.  ISK.  to  search.)
3471:search,  to  explore.  (F.  -  L.)  M.  £. ttrtken,  cerckm.^O.  F.  certhtr  (F.  <k*r^ eher).  —  L.  cirxart,  to  go  round  ;  hence,  to explore. —  L.  circus^  a  nng  labovo).
3785:ridge.4*  Da.  Aam^  Icel.  kambr,  Dan.  Swed. kam  ;  G.  kavtm.
16757:Search;  see  Circle      Der.  rt-seanh,
23270:ridge-rig  <3). rod — rood.
---
54:TttK  present  work  is  not  a  mere  abridgement  of  my  larger  Etymo- lopcal  Dictionary,  such  as  might  have  been  compiled  by  a  diligent book-maker,  but  has  been  entirely  rewritten  by  myself;  and  1  have Coand  that  the  experience  gained  by  writing  the  larger  work  has  been of  considerable  assistance  to  me  in  making  occasional  slight  improve- ments. My  object  has  been  to  produce  a  convenient  hand-book  for tbe  o«e  of  thai  increasing  number  of  students  who  wish  to  learn the  bistoTT  of  the  English  language,  and  who  naturally  desire  to  have Anglo-Saion  and  Icelandic  forms  presented  to  iliem  rightly  spelt  and ftOOcnniAted,  a  point  which  seldom  receives  sufficient  attention.
55:'*--  *  "inguishing  feature  of  this  abridgement,  as  well  as  of  my la  -nary,  is  that  all  the  forms  cited  can  actually  be  found  in
62:I  do  not,  in  general,  give  the  history  of  the  use  of  the  word  under dtaconioo,  unless  there  is  some  special  point  which  is  necessary  to  be kuowu  for  the  sake  of  the  etymology.  Kor  such  histor)*,  accompanied fay  flhitfntlve  comments,  references,  and  discussions,  I  must  refer ■Bhients  to  the  unabridged  work.
63:In  the  course  of  writing  this  abridgement,  I  have  taken  occasion U  several  corrections,  which,  in  the  larger  work,  are  only  to
146:Mannale  (abridged  from  Ducangc)
```


## [2026-09-14T02:09:28.156Z] TOOL CALL #82: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"ridge,  a  raised\\|ridge, a raised\\|ring,  a  circle\\|ring, a circle\\|crown,  a\\|crown, a\" SKT.txt | head; echo \"---\"; grep -n \"hrycg\\|hrieg\\|AS\\.  hrycg\" SKT.txt | head -5; echo \"---circus---\"; grep -n \"circus,\" SKT.txt | head -3",
 "description": "Skeat ridge ring crown"
}
```


### [2026-09-14T02:09:28.244Z] TOOL RESULT

```
---
---circus---
3468:circus,  a  ri'ig-  (L.)    L.  fircus  (above).
16106:Bind.  (E.)  M.E.  ritni.  rimie,  AS. rimii,  bnrk  of  a  tree,  crust  (of  bread). + O.  Du.  and  G.  rttuit,  bark. Ring  (i).  a  circle.  (E.)  M.E.  ring. A  S.  An'rtf.+Du.  rimg.  Low  G.  ring,  rink, Icel.  An'ftrr,  Swcd.  Dan.  G.  ring,  O.  H.  G. Mrimc;  Gk.  xpimot,  KipKoi,  L.  circus,  Kusa. Jkrug' ;  Skt.  chaJkra,  a  wheel,  ring.
16111:people,   an   arena,  circus,  listi. with  A.  S.  Aring,  a  ring.
```


## [2026-09-14T02:09:34.498Z] TOOL CALL #83: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"crispus\" LEW_1910.txt LAT.txt | head -6; echo \"---crista---\"; grep -n \"crista\" LEW_1910.txt LAT.txt | head -6",
 "description": "LEW crispus crista"
}
```


### [2026-09-14T02:09:34.581Z] TOOL RESULT

```
LAT.txt:14694:crispus, -a, -um: frisA. Se dit de la chevelure, puis de tout objet
LAT.txt:14700:6oupe Tivaoowv. A 1 'Apoque iapAriale, crispus se dit aAtaphoriqueaent
LAT.txt:67930:oso); donc lat .uespa reposer sur uopsa (cf., pour la ndtathbse, crispus).
---crista---
LAT.txt:11633:britt. Christ, cristaun. De la christiSnitds . De Christus ont eti formes
LAT.txt:14683:V. crista.
LAT.txt:14713:crista, -ae f. : crete (des gallinacee), pnis "huppe, aigrette";
LAT.txt:14718:Derives et conposes: cristatus M.L.3331; cristula f. (Coi.); cristiger.
LAT.txt:42075:comme deinceps , a'est cristallise dans 1'emploi adverbial avec le
LAT.txt:42967:Plin. 7 , 300 : ocreas et cristas inuenere Cares. Sert 4gal ement de surnoa.
```


## [2026-09-14T02:09:37.527Z] TOOL CALL #84: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '14690,14725p' LAT.txt; echo \"=== curvus ===\"; grep -n \"^curuus\\|curuus, -a\" LAT.txt | head -3",
 "description": "Ernout-Meillet crispus/crista"
}
```


### [2026-09-14T02:09:37.618Z] TOOL RESULT

```
les priapAes; la forae k gA ainAe est expressi re: cf. fello et felo.
Le gr. xpk^to "grincer, crisser" est loin pour le sens.
crispiS, -Is, -Ire: caqueter (de la poule). SuAt. Terae expressif
en -io, cf. drindrio, mintrio, etc.
crispus, -a, -um: frisA. Se dit de la chevelure, puis de tout objet
dont le dessin rappelle une chevelure frisA e: abies crispa, brassica
crispa. Du sens de "ondulA, crApu" on passe A celui de "qui ondule"
avec idAe de aouveaent, ainsi dans Pacuvius 336, linguae bi suit .s actu
crispo fulgere, nuance qui s'est dAveloppAe dans le dAnoainatif crispare,
e.g. Vg., Ae.1,313, bino manu lato crispans hastilia ferro = gr. 6uo
6oupe Tivaoowv. A 1 'Apoque iapAriale, crispus se dit aAtaphoriqueaent
d'un discours "bien peignA, soignA". AttestA de tout teaps. M.L.3339.
Gera.: v.h.a .chrisp, etc.
DArivAs et coaposAs: crispd, -Ss: friser (trans, et abs.), faire onduler,
brandir M.L.3337 a > crispico (Geli.); crispitudo (Arn.); crispulus
• M.L.3338 8- ; crispicapillus : ouXoGpil- (Gloss.); crispisulcSns ; incrispS-
tiS.
Ancien *hripsos (pour la aAtathbse, cf .uespa), qui se retrouve seu-
leaent en celtique: gall. crych "frisA, crApu" et le noa propre gaulois871
crudelis
Crixos-, lnt. Crispus aert aasai de no» propre.
crlsson et crlssonus: creaaon (Gloss.). Non latin, aans doute ger-
nanique •
crista, -ae f. : crete (des gallinacee), pnis "huppe, aigrette";
et tont objet qui rappelle nne crete par sa forne on sa position;
aigrette de casque, dentelnres de fenille, sauge-verveine (piante),
cr£te d'un nont; clitoris (dans Juv 4 nal 6,488)*Menes sens dans gr.
AocpoC. — Aftest 4 depuis Varr. et Lucr.; nsnel. Fanronan. M.L.3330
Derives et conposes: cristatus M.L.3331; cristula f. (Coi.); cristiger.
Cf. crinis. Les rapprocbements d'autres nots sont aventures.
croceus: croc; uncinus crocus uel aspidiscus. CGL V 634,43* Sans
doute gernanique.
crocio (croccio), - is, -ire: croasser. Anci en (pl ante). D' oh cro-
citus,-us n.: croassenent, A cote duquel 1 'abrege de Festus signale
une forne crocStio "coruorun uocis appellatio ", P.F.46,11 qui suppose
un verbe *crocdre (cf. craco). Fr6quentatif: crocito,-as, M.L.8336.
=== curvus ===
15537:curuus
15582:curuus, -a, -un; courbe, courb£ (oppos 4 A rectus). Attest^ k toute
```


## [2026-09-14T02:09:43.350Z] TOOL CALL #85: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '15582,15600p' LAT.txt; echo \"=== circus ===\"; grep -n \"^circus, -I\\|circus, -i\" LAT.txt | head -3",
 "description": "Ernout-Meillet curvus, circus"
}
```


### [2026-09-14T02:09:43.429Z] TOOL RESULT

```
curuus, -a, -un; courbe, courb£ (oppos 4 A rectus). Attest^ k toute
epoque. M.L.3423.
Derives et conpos^s: curuo,-ds : courber, M.L. 3423; curudbilis, cur-
uamen, curudtid, curudtura; curuitds, curuedS (tardif); curuesco,
— is; concurud M 0 L.2ii9; incuruG M.L .43 06 ; pro~,re—curuo; incuruus ;
procuruus; recuruus; incuruesco,-is (arch.); incurudtio,-bilis; incu-
ruiceruicus (Pacu.) d'aprbs le gr. xupTau)(T|V? *curuia, M.L.3433 a .CUSColiUH
388
Meae vocalisae qne dans gr. xuproc "conrbe" et dans iri. cor "cir-
cnit", gall. cor-uynt "tonrbillon (de vent)". L' elargisseaent -u- qni
expliqne ce vocalisae radical apparait dans lat .curvus, «ais aussi
dans iri. cruind, gall.crwnn "rond", La racine, sans -u- , apparait
dans gr. xopwvoc "reconrbe", et dans des 4 largisseaents en *-ei- ayec
*-uo-: lit. kreivas, v.sl .krivu "conrbe". De plus, cf. circus. Ponr le
suffixe, cf. prauus.
cuscolium, -I n . (cuscul iui ): graine de kermbs (Pline). M.L.3334.
cuspis, -idls f.: pointe de lance (lisse, par opposition i sp t-
culu* "pointe barbel^e"); puis 1'arae tout entifere: javelot,'lance,
et tont objet pointn: trident, etc. Attest^ depnis Poaponins. Conserve
=== circus ===
11978:circus, -I m. : sens premier 'Jcercle", mais a et 4 remplac 4 dans
```


## [2026-09-14T02:09:48.838Z] TOOL CALL #86: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '11978,11998p' LAT.txt",
 "description": "Ernout-Meillet circus"
}
```


### [2026-09-14T02:09:48.912Z] TOOL RESULT

```
circus, -I m. : sens premier 'Jcercle", mais a et 4 remplac 4 dans
cette acception par le diminntif circulus, et a tendn a ne plus desi¬
gner que le "cirque"; cf.Dub.Nom.V 573,4, circos antiqui, nunc circulos
dicendum ; le nom est rest 4 attacti aux b&timents dn cirque, m$me quand
ceux-ci cessaient d'avoir la forme circulaire. A ce sens se rattache
le deyive circensis. M.L.1948; v.h.a .chirch; britt .cyrch.
De circus "cercie" la langue a tir 4 divers adverbes et prepositions;
circum, circo (dans idcirco d'aprbs ideo\ circa, circiter-, circumcirca.
Circum, acc.de circus (cf.gr.xuxXtp) est sans doute la forme la plus
ancienne, et s'emploie seulement au sens propre "en cercie, autour,
autour de"; circa est form 4 sur le modele des autres adverbes de lien
en -a: extrd, intrd, infra, suprd. Circum est la seule forme que con-
naissent Ennius, Plaute, Caton, Terence; circa n’apparait qu'A partir
de la Lex Repetund. (133 av.J.-C.), et 1 'usage ne s'en repand qu*A
l' 4 poque de Ciceron (4 ex.de circS contre 33 de circum dans Cic:, 1 ex.
de circa contre 30 de circum dans Cesar; 6 ex. de circa contre 97 <fe
circum dans Vg.). Par contre dans T.L.j les proportions sont renversees;
411 ex.de circa contre 8 de circum-, et a 1'epoque imperiale circa prend
1 'avantage sur circum-, cf.Thes.III 1079,6sqq. Circa a d 4 veloppe le sens
figure "autour de", c.-A-d. "A propos de, relativement a", comme gr.
Ttepl, sens qui n'apparait pas dans circum-, cf. quocirca, et en osque
```


## [2026-09-14T02:09:52.439Z] AGENT

Now I'll write the verification file.


## [2026-09-14T02:18:34.145Z] TOOL CALL #87: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-454.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW = \"https://en.wiktionary.org/wiki/\"\nS_KORONOS = W + \"%CE%BA%CE%BF%CF%81%CF%89%CE%BD%CF%8C%CF%82\"\nS_KORONE  = W + \"%CE%BA%CE%BF%CF%81%CF%8E%CE%BD%CE%B7\"\nS_KARAN   = W + \"%DA%A9%D8%B1%D8%A7%D9%86\"\nS_KANAR   = W + \"%DA%A9%D9%86%D8%A7%D8%B1\"\nS_CYRUS_W = W + \"Cyrus\"\nS_CYRUS_P = \"https://en.wikipedia.org/wiki/Cyrus\"\nS_SIRUS   = \"https://fa.wikipedia.org/wiki/%D8%B3%DB%8C%D8%B1%D9%88%D8%B3\"\nS_RIBBON  = \"https://www.etymonline.com/word/ribbon\"\nS_HRINGAZ = W + \"Reconstruction:Proto-Germanic/hringaz\"\nS_HRUGJAZ = W + \"Reconstruction:Proto-Germanic/hrugjaz\"\n\nnodes = []\n\ndef N(i, lang, words, verdict, deriv, deriv_fa, sources, refs, cons, extra=None):\n    d = {\"id\": i, \"lang\": lang, \"words\": words, \"verdict\": verdict,\n         \"derivation\": deriv, \"derivation_fa\": deriv_fa,\n         \"sources\": sources, \"ref_check\": refs, \"consulted\": cons}\n    if extra:\n        d.update(extra)\n    nodes.append(d)\n\nN(1, \"Indo-European\", \"Kor-ôna\", \"plausible\",\n  \"The starred *kor-ōna of the chart is Watkins's 'Suffixed o-grade form *kor-ó-no- in Greek korōnos, curved' (AHD appendix s.v. sker-3, §10) and Pokorny's 'κορωνός \\\"gekrümmt\\\"; κορώνη \\\"allerlei Gekrümmtes, Gebogenes etc.\\\" (Latin loanword corona), perhaps as *kor[u]-no-s to the u-basis *(s)kereu-' (IEW 935). An o-grade *kor- of *(s)ker- enlarged with -no-/-ōno- is therefore genuine, and the gloss 'bent' fits the Greek adjective. Two reservations: (a) the shape written 'Kor-ôna' with final -a reproduces the Greek feminine κορώνη rather than a neutral IE stem; (b) the second reference Nourai gives, Mann IEC 535, is not a lemma meaning 'bent' at all — p. 535 has 'korōn-, korən- \\\"edge, rim, border\\\". Cf. kor- and WP I, 413, II, 591 — Per. karán, id.; Gk. korṓnē, id. (and \\\"curve, crown\\\". LW in Lat. corona)', while Mann's 'curve' lemmas stand on pp. 533 (kor- 'bend, curve') and 536 (korono- 'curve-'). Nourai has fused Mann's 'edge' root (which is what the Iranian branch below needs) with Pokorny's 'curved' root into a single box.\",\n  \"صورت بازسازی‌شدهٔ *kor-ōna در این نمودار همان چیزی است که واتکینز در پیوست ریشه‌های هندواروپایی فرهنگ AHD زیر sker-3 آورده است: «صورت پسوندی درجهٔ o یعنی *kor-ó-no- در یونانی korōnós «خمیده»»؛ پوکورنی نیز در ص ۹۳۵ همین را با κορωνός «خمیده» و κορώνη «هر چیز خمیده و کمانی» (که وام‌واژهٔ لاتینی corona از آن است) ثبت کرده. پس ستاک درجهٔ o از ریشهٔ *(s)ker- با پسوند -no-/-ōno- واقعی است و معنای «خمیده» درست. اما دو نکته: نخست آنکه املای Kor-ôna با -a پایانی در واقع صورت مؤنث یونانی κορώνη است نه ستاک هندواروپایی؛ دوم آنکه مأخذ دوم نورایی، مان (IEC) ص ۵۳۵، اصلاً سرواژه‌ای به معنای «خمیده» ندارد بلکه *korōn-/korən- «کناره، لبه، مرز» است و همان‌جا «فارسی karān» را می‌آورد. نورایی دو ریشهٔ جدا (یکی «خمیده» و یکی «کناره») را در یک جعبه درآمیخته است؛ بنابراین ادعا با احتیاط پذیرفتنی است.\",\n  [S_KORONOS, S_KORONE],\n  [{\"ref\": \"POK:935\", \"status\": \"supports\",\n    \"note\": \"IEW 935 (POK_full.txt, lemma '(s)ker-3', Page(s) 935-938): 'gr. κυρτός \\\"crooked\\\" ... Κορωνος \\\" writhed, crooked, humped \\\"; Κορωνη \\\"allerlei GekriJmmtes, Gebogenes etc\\\" (Latin loanword corona), perhaps as *kord[u]-no-s zw u-basis *(s)kereu-'.\"},\n   {\"ref\": \"IEC:535\", \"status\": \"partial\",\n    \"note\": \"Mann, IEC p. 535 (leaf ~306, the printed '535' appears in the OCR): 'korōn-, korən- \\\"edge, rim, border\\\". Cf. kor- and WP I, 413, II, 591 Per. karán, id.; Gk. korṓnē, id. (and \\\"curve, crown\\\". LW in Lat. corona)'. Gloss is 'edge, rim, border', not 'bent'; the 'curve' lemmas are kor- (p.533) and korono- (p.536).\"}],\n  [{\"src\": \"WLD\", \"where\": \"Walde-Pokorny II 568 (WLD_Bd2_pages.txt, entry '(s)q[er- \\\"drehen, biegen\\\"')\", \"stance\": \"supports\",\n    \"note\": \"'gr. κυρτός \\\"krumm\\\" (alte u-Färbung ...), κορωνός \\\"gekrümmt\\\"; κορώνη \\\"allerlei gekrümmtes, gebogenes usw.\\\" (lat. Lw. corona, vielleicht als *koro[u]-no-s zur u-Basis *(s)qereu-)'.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. sker-3, §10\", \"stance\": \"supports\",\n    \"note\": \"'10. Suffixed o-grade form *kor-óno- in Greek korōnos, curved: (CORONA), CROWN; CORONOID.'\"},\n   {\"src\": \"SYN\", \"where\": \"Buck 12.35 / 12.353\", \"stance\": \"silent\",\n    \"note\": \"Buck has no IE root box; he lists the Avestan/Persian words for 'end, edge' and writes 'etym.?' (p. 857).\"}])\n\nN(2, \"Avestan / Old Persian\", \"Karana\", \"plausible\",\n  \"Avestan karana- is real and exactly as glossed: Bartholomae, AiW col. 451, 'j. karana- m. \\\"Ende\\\"; 1) räumlich: \\\"Grenze, Rand; Ufer; Flügel (des Heeres)\\\"' (uva karana aŋhå zəmō Yt.10.95 'both ends of this earth'; upa yaozəṇta karana zrayå vouru.kaṣ̌aya Yt.5.38 'on the surging shores [of Lake Vourukaṣ̌a]'), the temporal sense 'end' only in compounds; Bartholomae's KompE. note already adds 'np. kanār, kanāra'. Two problems with the chart. (a) The label 'Old Persian' is unsupported: Kent's Old Persian lexicon has no karana- (a grep of KNT.txt returns nothing); the word is Avestan (with Middle and New Iranian continuants), and Nourai's own two references, Bartholomae and Buck, are both Avestan. (b) The arrow from *kor-ōna 'bent' is not established. Buck, the very page cited, writes 'Av. karana- (also in special senses \\\"border, shore\\\", etc.; NPers. karan \\\"shore, side\\\"), etym.?' (SYN 857) — i.e. he declines to give it a root. Walde-Pokorny and Pokorny list under (s)ker- 'turn, bend' only Avestan skarəna- 'round', never karana-. Modern Wiktionary derives Proto-Iranian *karana- 'edge, border, limit' from a root *kar- 'to draw a line, furrow' or *kar- 'to cut' (i.e. Pokorny's (s)ker-4 'cut', p. 938), with *(s)ker- 'bend' only one of the possibilities.\",\n  \"واژهٔ اوستایی karana- در فرهنگ بارتولومه (ستون ۴۵۱) چنین آمده است: «karana- مذکر «پایان»؛ ۱) مکانی: «مرز، لبه، کرانهٔ آب، جناح سپاه»»، و خود بارتولومه در پایان مدخل «فارسی نو kanār، kanāra» را می‌افزاید. دو ایراد بر نمودار وارد است: نخست آنکه برچسب «پارسی باستان» پشتوانه ندارد؛ در واژه‌نامهٔ پارسی باستان کنت چنین واژه‌ای نیست و این واژه فقط اوستایی است. دوم آنکه پیوند آن با *kor-ōna «خمیده» قطعی نیست؛ باک در همان صفحه‌ای که نورایی ارجاع می‌دهد (ص ۸۵۷) می‌نویسد «اوستایی karana- ... ریشه‌شناسی؟» یعنی ریشه‌ای برای آن قائل نمی‌شود، و والده-پوکورنی زیر ریشهٔ «پیچیدن، خمیدن» تنها skarəna- اوستایی «گرد» را می‌آورد نه karana- را. ویکی‌واژه نیز *karana- ایرانی آغازین را به *kar- «خط کشیدن» یا *kar- «بریدن» بازمی‌گرداند. پس: با احتیاط پذیرفتنی است.\",\n  [S_KARAN],\n  [{\"ref\": \"BRT:451\", \"status\": \"supports\",\n    \"note\": \"AiW col. 451 (BRT.txt leaf 273): 'j. karana- m. \\\"Ende\\\"; i) räumlich: \\\"Grenze, Rand; Ufer; Flügel (des Heeres)\\\" ... KompE. — np. kanār, kanāra'. Buck cites the same column for the word.\"},\n   {\"ref\": \"SYN:857\", \"status\": \"partial\",\n    \"note\": \"Buck, Selected Synonyms, §12.35 END, p. 857 (SYN.txt line 21898): 'Av. karana- (also in special senses \\\"border, shore\\\", etc.; NPers. karan \\\"shore, side\\\"), etym.? Barth. 451.' The word and gloss are there; the etymology is explicitly left open.\"},\n   {\"ref\": \"BRT:46\", \"status\": \"supports\",\n    \"note\": \"col. 46 carries the privative compound a-karana- 'endlos' (node #5), which presupposes this karana-.\"}],\n  [{\"src\": \"KNT\", \"where\": \"Kent, Old Persian, Lexicon pp. 164-215\", \"stance\": \"silent\",\n    \"note\": \"grep -n 'karana' KNT.txt returns nothing: there is no Old Persian karana-, so the chart's 'Old Persian' label has no support.\"},\n   {\"src\": \"WLD\", \"where\": \"WP II 568\", \"stance\": \"contradicts\",\n    \"note\": \"Under '(s)qer- \\\"drehen, biegen\\\"' the only Iranian item is 'Av. skarəna- \\\"rund\\\", skarayat̰-raθa- EN.' — karana- 'end, border' is not in the entry.\"},\n   {\"src\": \"IEC\", \"where\": \"Mann p. 535 s.v. korōn-, korən-\", \"stance\": \"supports\",\n    \"note\": \"'korōn-, korən- \\\"edge, rim, border\\\" ... Per. karán, id.; Gk. korṓnē, id.' — Mann does group the Iranian 'edge' word with Greek korṓnē, which is Nourai's claim.\"}])\n\nN(3, \"Pahlavi\", \"kanâr\", \"confirmed\",\n  \"Middle Persian kanār [kn'l] 'side, edge; embrace' and its -ag derivative kanārag [kn'lk'] 'edge, limit, boundary' are both in MacKenzie's Concise Pahlavi Dictionary (p. 49-50), with Manichaean MP kn'rg and the privative a-kanārag 'unlimited, boundless'; Nyberg's glossary has 'kanārak [kn'lk'; ŠTL'] boundary ... MPrs kn'rg \\\"side\\\"; Paz. kanāra; NP kanārah \\\"side, shore\\\"'. The -n- where Avestan karana- has -r- is Hübschmann's 'Umstellung von Konsonanten verschiedener Silben' (Persische Studien p. 267), the same dissimilatory transposition as hargiz beside older hagirz and bižišk/hižišk: karana- > *kanār beside the regularly inherited karān, with loss of the final vowel and lengthening in the open second syllable giving MP -ār. Horn, Grundriss p. 189, states the chain exactly as the chart draws it: 'aw. karana- \\\"Seite, Ende\\\"; phlv. kanār, kanārak'. Moʿin's footnote in Borhān-e Qāṭeʿ p. 1699 s.v. کنار cites Darmesteter to the same effect.\",\n  \"فارسی میانه (پهلوی) kanār «سو، کناره؛ آغوش» و مشتق آن kanārag «لبه، مرز، حد» هر دو در فرهنگ مکنزی (ص ۴۹–۵۰) ثبت‌اند، همراه با صورت پارتی/مانوی kn'rg و صورت منفی a-kanārag «بی‌کران»؛ نیبرگ نیز kanārak را با معنی «مرز» آورده و آن را با «kanāra پازند» و «کنارهٔ فارسی نو» می‌سنجد. تبدیل r… r به n… r در این واژه همان چیزی است که هوبشمان آن را «جابه‌جایی همخوان‌های دو هجا» (قلب) می‌نامد (پژوهش‌های فارسی، ص ۲۶۷) و آن را در کنار hargiz/hagirz و بزشک/هزشک می‌گذارد: از اوستایی karana- هم karān (بی‌قلب) و هم kanār (با قلب) به دست آمده است. هرن در ص ۱۸۹ همین زنجیره را می‌آورد و معین نیز در حاشیهٔ برهان قاطع ص ۱۶۹۹ به نقل از دارمستتر همین را می‌گوید. ادعای نورایی درست است.\",\n  [S_KANAR],\n  [{\"ref\": \"HRN:189\", \"status\": \"supports\",\n    \"note\": \"Horn, Grundriss der neupersischen Etymologie p. 189 (HRN.txt leaf 210, entry 6): 'kerān \\\"Ufer, Seite, Ende\\\", kerāne, meist kenār, kenāre. aw. karana- \\\"Seite, Ende\\\"; phlv. kanār, kanārak, a[rm]. kanarak. oss. kiron \\\"Ende\\\" (155); LW. kurd. afγ. kinūr.'\"},\n   {\"ref\": \"BQT:1699\", \"status\": \"supports\",\n    \"note\": \"Borhān-e Qāṭeʿ p. 1699 (v3 pdf p. 492, fetched with tools/ref_page.py), Moʿin's footnote 2 to کنار: «دارمستتر گوید: کنار از ریشهٔ اوستایی karana (کنار)، پهلوی kanār است «تتبعات ج ۹ ص ۱۱۵»»; footnote 5 to کناره: «<< کرانه، پهلوی kanārak، اوستایی karana».\"},\n   {\"ref\": \"BQT:1611\", \"status\": \"supports\",\n    \"note\": \"Borhān-e Qāṭeʿ p. 1611 (v3 pdf p. 404), Moʿin's footnote to کرانه: «کرانه (ه.م.) << کنار < کناره؛ اوستا karana (کنار، طرف، انتها)؛ پهلوی kanār، kanārak؛ آسی kiron (انتها)؛ کردی، افغانی kinūr».\"}],\n  [{\"src\": \"PHD\", \"where\": \"MacKenzie 1971 pp. 49-50\", \"stance\": \"supports\",\n    \"note\": \"'kanār [kn'l | N ~] side, edge; embrace. ~ag [-k' | M kn'rg, N ~a] edge, limit, boundary. ~agōmand [-k'wmnd | M -gwmnd] limited, finite.' and p. 50 'a-kanārag [\\\\'kn\\\\'lk\\\\' | M ʾqnʾrg] unlimited, boundless.'\"},\n   {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II (glossary), s.v. kanārak\", \"stance\": \"supports\",\n    \"note\": \"'kanārak [kn\\\\'lk\\\\'; ŠTL\\\"] boundary 512^7, 529.11. — MPrs kn\\\\'rg \\\"side\\\"; Paz. kanāra; NP kanārah \\\"side, shore\\\".' Also 'a-kanārakēh boundlessness, endlessness, of Ohurmazd 637-28'.\"},\n   {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien p. 267 (HUB.txt leaf 277)\", \"stance\": \"supports\",\n    \"note\": \"'Umstellung von Konsonanten verschiedener Silben hat stattgefunden in: hargiz ... kanar, kanara neben karan, karana (Fird. I, 247, 71; 251, 132) \\\"Ufer, Ende\\\" = zd. karana-, schon paz. kanara \\\"border\\\" ... und phl. kanaruk, akanarak.'\"}])\n\nN(4, \"Persian\", \"karân «کران» (extra: کرانه، کنار، کناره)\", \"plausible\",\n  \"All four Persian words are real and current: کران karān 'edge, border, limit', کرانه karāna 'shore, margin', کنار kanār 'side, shore; embrace', کناره kanāra 'edge, shore'. But the chart's chain Pahlavi kanār -> Persian karān is inverted for karān itself. New Persian karān continues Middle Persian karan [kl'n'] 'side, edge, end, limit' (MacKenzie 1971: 49), the regular, untransposed descendant of Avestan karana- (final -a lost, the stressed second syllable lengthened to -ān); کنار/کناره are the doublets that came down through the transposed MP kanār(ag). Wiktionary s.v. کران says just that — 'from Middle Persian klʾn' /karān/, from Proto-Iranian *karana-' — and files کنار as 'a metathesized form' of it; Wiktionary s.v. کنار likewise: 'from Middle Persian knʾl /kanār/ ... a metathesis of کران (karân)'. Horn p. 189 lists the whole set side by side without making either the parent of the other. So karān and kanār are siblings, not parent and child; کرانه and کناره are the -a extensions of each.\",\n  \"هر چهار صورت «کران، کرانه، کنار، کناره» واژه‌های اصیل فارسی‌اند، اما زنجیرهٔ نمودار (پهلوی kanār ← فارسی کران) وارونه است. «کران» دنبالهٔ فارسی میانهٔ karan «سو، لبه، پایان، حد» (مکنزی ص ۴۹) است که خود بازماندهٔ بی‌قلبِ اوستایی karana- است: واکهٔ پایانی افتاده و هجای دوم کشیده شده (karana- > karān). در برابر، «کنار» و «کناره» از صورت مقلوبِ پهلوی kanār/kanārag آمده‌اند. ویکی‌واژه ذیل «کران» می‌نویسد: «از فارسی میانهٔ karān، از ایرانی آغازین *karana-» و «کنار» را «صورت مقلوب کران» می‌خواند. هرن نیز در ص ۱۸۹ هر دو دسته را در کنار هم و هم‌ردیف می‌آورد. پس «کران» فرزند «کنار» نیست بلکه خواهر آن است؛ ادعای نورایی با این تصحیح پذیرفتنی است.\",\n  [S_KARAN, S_KANAR],\n  [{\"ref\": \"BRT:451\", \"status\": \"supports\",\n    \"note\": \"AiW 451 s.v. karana- ends 'KompE. — np. kanār, kanāra' — Bartholomae himself derives the New Persian forms from the Avestan word.\"},\n   {\"ref\": \"SYN:857\", \"status\": \"partial\",\n    \"note\": \"Buck p. 857: 'NPers. karan \\\"shore, side\\\"' — the word and sense are confirmed, but Buck adds 'etym.?'.\"},\n   {\"ref\": \"IEC:535\", \"status\": \"supports\",\n    \"note\": \"Mann p. 535: 'korōn-, korən- \\\"edge, rim, border\\\" ... Per. karán, id.' — the Persian form is cited with exactly the chart's gloss.\"}],\n  [{\"src\": \"HRN\", \"where\": \"Horn, Grundriss p. 189 no. 6\", \"stance\": \"supports\",\n    \"note\": \"'kerān \\\"Ufer, Seite, Ende\\\", kerāne, meist kenār, kenāre. aw. karana- ...; phlv. kanār, kanārak' — the complete set of the chart's four Persian words, all from Av. karana-.\"},\n   {\"src\": \"PHD\", \"where\": \"MacKenzie 1971 p. 49\", \"stance\": \"partial\",\n    \"note\": \"'karan [kl\\\\'n\\\\' | P kl\\\\'n, N ~] side, edge, end, limit' stands beside 'kanār ... side, edge' — Middle Persian has BOTH forms, so NP karān need not come through kanār.\"},\n   {\"src\": \"BQT\", \"where\": \"Borhān-e Qāṭeʿ p. 1611 and p. 1699, Moʿin's footnotes\", \"stance\": \"supports\",\n    \"note\": \"p.1611 on کرانه: «کرانه << کنار < کناره؛ اوستا karana؛ پهلوی kanār، kanārak»; p.1699 on کنار quotes Darmesteter for Av. karana- > Pahl. kanār.\"},\n   {\"src\": \"ARY\", \"where\": \"Aryanpur, Farhang-e riše-hā-ye hend-o-orupāyi\", \"stance\": \"silent\",\n    \"note\": \"grep of ARY_pages.txt / ARY_latin_index_pages.txt for کران، کناره، KARAN finds no headword.\"}])\n\nN(5, \"Avestan / Old Persian\", \"a-karana\", \"confirmed\",\n  \"Avestan a-karana- adj. (fem. -nā-) 'endlos' is Bartholomae AiW col. 46 (BRT.txt leaf 62), a bahuvrihi of the privative prefix a- (PIE *n̥-, the chart's cross-reference 'Ne 1') with karana- 'end'. It is the standing epithet of boundless time and boundless light in the Younger Avesta: zrvan- akarana- 'Unbegrenzte Zeit' (V.19.9, AiW quoting 'in der unbegrenzten Zeit'), and akarana anaγra asaonō stiš (Yt.13.48) 'the endless, beginningless creation of the Righteous One'. The compound is continued unbroken into Middle Persian a-kanārag 'unlimited, boundless' (MacKenzie p.50) and akanārakēh 'boundlessness ... of Ohrmazd' (Nyberg), and into New Persian بی‌کران. As for Old Persian, the word is not attested there either (see node #2).\",\n  \"صفت اوستایی a-karana- «بی‌پایان» در فرهنگ بارتولومه ستون ۴۶ آمده است و ترکیبی است از پیشوند نفی a- (از *n̥- هندواروپایی، همان ریشه‌ای که نورایی با ارجاع «Ne 1» بدان اشاره می‌کند) با karana- «پایان». این صفت در اوستای نو صفت ثابت «زمان بی‌کرانه» (zrvan- akarana-، وندیداد ۱۹٫۹) و «روشنایی بی‌آغاز و بی‌کران» (یشت ۱۳٫۴۸) است. همین ترکیب بی‌گسست در فارسی میانه به a-kanārag «بی‌کران» (مکنزی ص ۵۰) و akanārakēh «بی‌کرانگی، صفت اورمزد» (نیبرگ) و در فارسی نو به «بی‌کران» رسیده است. ادعای نورایی درست است؛ تنها برچسب «پارسی باستان» مانند گرهٔ پیشین بی‌پشتوانه است.\",\n  [],\n  [{\"ref\": \"BRT:46\", \"status\": \"supports\",\n    \"note\": \"AiW col. 46 (BRT.txt line 3013, leaf 62): 'j. a-karana- Adj. (fem. -nā-) \\\"endlos\\\"'; the entry is quoted again at AiW s.v. zrvan-: 'dahat̰ spəntō mainyuš dahat̰ ... zrvāne (LS.) akarane \\\"... in der unbegrenzten Zeit\\\" V.19.9'.\"}],\n  [{\"src\": \"PHD\", \"where\": \"MacKenzie 1971 p. 50\", \"stance\": \"supports\",\n    \"note\": \"'a-kanārag [\\\\'kn\\\\'lk\\\\' | M ʾqnʾrg] unlimited, boundless. ~īh: boundlessness.' — the direct Middle Persian continuant.\"},\n   {\"src\": \"NYB\", \"where\": \"Nyberg II, glossary\", \"stance\": \"supports\",\n    \"note\": \"'a-kanārakēh boundlessness, endlessness, of Ohurmazd 637-28'; also 'Zurvān i akanārak' s.v. mihr.\"},\n   {\"src\": \"BRT\", \"where\": \"AiW cols. 46 and 451\", \"stance\": \"supports\",\n    \"note\": \"the privative compound and its base stand in the same dictionary, confirming the a- + karana- analysis.\"}])\n\nN(6, \"Greek\", \"koeônos\", \"transcription_suspect\",\n  \"There is no Greek word koeônos. The word meant is κορωνός (korōnós) 'curved, crooked' — Pokorny IEW 935 'Κορωνος \\\"writhed, crooked\\\"', Walde-Pokorny II 568 'κορωνός \\\"gekrümmt\\\"', Watkins sker-3 §10 '*kor-óno- in Greek korōnos, curved', Ernout-Meillet s.v. curuus 'La racine, sans -u-, apparaît dans gr. κορωνός \\\"recourbé\\\"'. I rendered pdf page 454 at 300 dpi (copy saved to data/verification/sources/refs/ocr/BOOK/454.png) and the printed page itself reads 'koeônos : curved', so the extraction is faithful and the error is Nourai's own misprint — an r misread as e somewhere in his copying (compare Mann's OCR-friendly spelling 'kor-oōnós'). With the spelling corrected the arrow is sound: Wiktionary derives κορωνός from PIE *(s)ker- 'to turn, bend', cognate with Latin curvus, Old Irish cruind and Proto-Slavic *krivъ.\",\n  \"واژه‌ای به شکل koeônos در یونانی وجود ندارد؛ صورت درست κορωνός (korōnós) «خمیده، کج» است که پوکورنی (ص ۹۳۵)، والده-پوکورنی (ج ۲ ص ۵۶۸)، واتکینز (زیر sker-3) و ارنو-مِیه (ذیل curuus) همه آن را ثبت کرده‌اند. صفحهٔ چاپی کتاب (برگ ۴۵۴ پی‌دی‌اف، صفحهٔ ۴۲۴ کتاب) را با تفکیک ۳۰۰ نقطه بازنمایی کردم و در خود کتاب نیز «koeônos» چاپ شده است؛ پس خطای خوانش اسکن نیست بلکه خطای چاپی خود کتاب است (بدل شدن r به e). با تصحیح املا، پیکان درست است: ویکی‌واژه κορωνός را از ریشهٔ هندواروپایی *(s)ker- «پیچیدن، خمیدن» می‌گیرد و آن را هم‌ریشهٔ curvus لاتین و cruind ایرلندی کهن می‌داند.\",\n  [S_KORONOS],\n  [{\"ref\": \"POK:935\", \"status\": \"supports\",\n    \"note\": \"IEW 935, lemma (s)ker-3: 'Κορωνος \\\" writhed, crooked, humped \\\"' (the OCR of κορωνός) — the page is right, the spelling in the chart is not.\"},\n   {\"ref\": \"IEC:535\", \"status\": \"partial\",\n    \"note\": \"Mann p. 535 has korṓnē under 'korōn-, korən- \\\"edge, rim, border\\\"'; the adjective korōnós is on p. 533 s.v. 'kor- \\\"bend, curve; bent, curved\\\" ... Myc. & Gk. cf. kor-oōnós, id. beside kor-óné \\\"book handle\\\" (LW in Lat. corona)'.\"}],\n  [{\"src\": \"WLD\", \"where\": \"WP II 568\", \"stance\": \"supports\",\n    \"note\": \"'κορωνός \\\"gekrümmt\\\"; κορώνη \\\"allerlei gekrümmtes, gebogenes usw.\\\"'.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. sker-3 §10\", \"stance\": \"supports\",\n    \"note\": \"'*kor-óno- in Greek korōnos, curved'.\"},\n   {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. curuus\", \"stance\": \"supports\",\n    \"note\": \"'La racine, sans -u-, apparaît dans gr. κορωνός \\\"recourbé\\\", et dans des élargissements en *-ei- avec *-uo-: lit. kreivas, v.sl. krivŭ \\\"courbe\\\".'\"}],\n  {\"error_in\": \"book\", \"book_prints\": \"koeônos\", \"correct_form\": \"korōnós (κορωνός)\"})\n\nN(7, \"English\", \"crown, corona\", \"plausible\",\n  \"The transmission itself is textbook: Latin corōna 'garland, wreath, crown' is an early borrowing of Greek κορώνη, which Klein states plainly ('corona, n., a crown. — L. corona, \\\"garland, wreath, crown\\\", fr. Gk. κορώνη, \\\"anything curved; a wreath, garland\\\"'); from Latin came Old French corone/curune, Anglo-Norman corune, Middle English coroune, whence crown (in English from c.1200, with the Norman monarchy, and applied to the coin from 1526); corona was re-borrowed straight from Latin as a learned term (architectural member, 16th c.; the halo of the sun, 1809). Two qualifications keep this from 'confirmed'. (a) The immediate Greek source is the feminine noun κορώνη, not the adjective κορωνός drawn as its parent — they are related but distinct words. (b) The deeper tie to *(s)ker- is now contested: Beekes, followed by Wiktionary, derives κορώνη from PIE *ḱorh₂- 'crow, raven' (whence Latin cornix), the 'curved object' senses arising secondarily from the crow's beak; on that view crown/corona drop out of this root altogether. Watkins still lists CORONA, CROWN under sker-3.\",\n  \"زنجیرهٔ انتقال روشن است: corōna لاتین «تاج گل، حلقه، تاج» وام‌واژهٔ یونانی κορώνη است — کلاین: «corona لاتین ... از یونانی κορώνη «هر چیز خمیده؛ حلقهٔ گل»» — و از لاتین به فرانسهٔ کهن corone/curune و انگلیسی میانهٔ coroune و سپس crown رسیده است؛ corona نیز در سدهٔ شانزدهم مستقیماً از لاتین به‌عنوان اصطلاح فنی وام گرفته شد و از ۱۸۰۹ به «هالهٔ خورشید» اطلاق شد. دو نکته اما مانع تأیید کامل است: نخست آنکه مأخذ بی‌واسطهٔ این واژه‌ها κορώνη (اسم مؤنث) است نه κορωνός (صفت) که در نمودار پدر آن نشان داده شده؛ دوم آنکه ریشه‌شناسی امروزی (بیکس و به تبع او ویکی‌واژه) κορώνη را از *ḱorh₂- «کلاغ» می‌گیرد و معناهای «خمیده» را ثانوی می‌داند، که در آن صورت این شاخه از ریشهٔ «پیچیدن» جدا می‌شود. واتکینز هنوز CROWN و CORONA را زیر sker-3 نگه داشته است. پس: با احتیاط پذیرفتنی.\",\n  [S_KORONE, S_KORONOS],\n  [{\"ref\": \"AHD\", \"status\": \"supports\",\n    \"note\": \"Watkins 1985 s.v. sker-3 §10: '*kor-óno- in Greek korōnos, curved: (CORONA), CROWN; CORONOID.' The parentheses round CORONA mark it as the Latin-mediated member.\"}],\n  [{\"src\": \"KLN\", \"where\": \"Klein s.v. corona\", \"stance\": \"supports\",\n    \"note\": \"'corona, n., a crown. — L. corona, \\\"garland, wreath, crown\\\", fr. Gk. κορώνη, \\\"anything curved; a wreath, garland\\\". See crown.'\"},\n   {\"src\": \"POK\", \"where\": \"IEW 935\", \"stance\": \"supports\",\n    \"note\": \"'Κορωνη \\\"allerlei GekriJmmtes, Gebogenes etc\\\" (Latin loanword corona)' — Pokorny explicitly calls Latin corona a loan from Greek.\"},\n   {\"src\": \"WLD\", \"where\": \"WP II 568\", \"stance\": \"supports\",\n    \"note\": \"'κορώνη ... (lat. Lw. corona)'.\"}])\n\nN(8, \"Indo-European\", \"Kur-wo\", \"plausible\",\n  \"*kur-wo- is Watkins's reconstruction, taken over verbatim: 'sker-3 ... 4. Suffixed variant form *kur-wo- in Latin curvus, bent, curved: CURB, CURVATURE, CURVE, CURVET.' Pokorny (935) gives only the Latin word with the parenthesis '(forms -uo-)', and Mann is blunter still: '(kuruos \\\"bent, round\\\". Assumed for Latin only, cf. kor-)'. So a zero-grade *kur- with a -wo- suffix is a legitimate inference for curvus (and, without the suffix, for Greek kyrtós, Ernout-Meillet s.v. curuus 'Même vocalisme que dans gr. κυρτός'), but it is a Latin-internal reconstruction, not an inherited IE stem with a wide progeny. The chart nevertheless hangs on it Old Persian Kūru-, Greek krikos, Latin crista/crispus and the whole Germanic group — none of which come from *kur-wo- in any of Nourai's own sources: Watkins derives them from *ki-kr-o- (krikos), *kris-tā- (crista), *krip-so- (crispus), *(s)kre-n-g- (shrink), *(s)kre-n-gh- (*hringaz) and *kreuk- (*hrugjaz). The added gloss 'curly' is imported from crispus. Read as a cover label for the *kur-/*kr- side of the root the box is harmless; read as a node it overstates.\",\n  \"صورت *kur-wo- را نورایی عیناً از واتکینز گرفته است: «sker-3 ... ۴. صورت پسوندی *kur-wo- در curvus لاتین «خمیده»: CURB، CURVATURE، CURVE، CURVET». پوکورنی (ص ۹۳۵) تنها واژهٔ لاتینی را با یادداشت «(با پسوند -uo-)» می‌آورد و مان صریح‌تر است: «(kuruos «خمیده، گرد». فقط برای لاتین فرض شده است)». پس ستاک درجهٔ صفر *kur- با پسوند -wo- برای curvus بازسازی موجهی است، اما بازسازی‌ای درون‌لاتینی است نه ستاکی موروثی با فرزندان فراوان. با این حال نورایی پارسی باستان Kūru-، یونانی krikos، لاتین crista و crispus و تمام گروه ژرمنی را زیر آن آورده، حال آنکه در خود مأخذ او (واتکینز) هر یک از گسترش‌های دیگری می‌آیند: *ki-kr-o-، *kris-tā-، *krip-so-، *(s)kre-n-g-، *(s)kre-n-gh- و *kreuk-. معنای افزودهٔ «مجعد» نیز از crispus به این جعبه سرایت کرده است. با احتیاط پذیرفتنی است.\",\n  [],\n  [{\"ref\": \"POK:935\", \"status\": \"partial\",\n    \"note\": \"IEW 935 has 'Latin curvus \\\"crooked, writhed, ... arched\\\" (forms -uo-)' but prints no headword *kur-wo-; the starred stem is Watkins's, not Pokorny's, and the other children of this box are on pp. 936-938 under different extensions.\"}],\n  [{\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. sker-3 §4\", \"stance\": \"supports\",\n    \"note\": \"'Suffixed variant form *kur-wo- in Latin curvus, bent, curved: CURB, CURVATURE, CURVE, CURVET.'\"},\n   {\"src\": \"IEC\", \"where\": \"Mann s.v. kuruos (p. ~595) and kur- (1)\", \"stance\": \"partial\",\n    \"note\": \"'(kuruos \\\"bent, round\\\". Assumed for Latin only, cf. kor-) (WP II, 568)'; and 'kur- (1) \\\"round, curved\\\" ... Gk. kur-tós, id.'\"},\n   {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. curuus\", \"stance\": \"supports\",\n    \"note\": \"'Même vocalisme que dans gr. κυρτός \\\"courbe\\\" ... L'élargissement -u- qui explique ce vocalisme radical apparaît dans lat. curvus, mais aussi dans irl. cruind, gall. crwnn \\\"rond\\\".'\"}])\n\nN(9, \"Old Persian\", \"Kŭru; Kŭruš, Kŭrauš, Kŭ-raš, Kŭ-ra-aš\", \"disputed\",\n  \"The FORMS are exactly right and are lifted, with the KNT:180 reference, from Moʿin: the Old Persian stem is Kūru-, nominative singular Kūruš (CMa 1 adam Kūruš xšāyaθiya 'I am Cyrus the King'), genitive singular Kūrauš (DB 1.28 Kabūjiya nāma Kūrauš puça 'Cambyses by name, a son of Cyrus'), beside Elamite Ku-raš and Babylonian Ku-ra-aš — Kent, Old Persian p. 180: 'Kūru- sb. \\\"Cyrus\\\", founder of the Persian Empire: Elam. ku-raš, Akk. ku-ra-aš, Gk. Κῦρος (§164.V).' (Nourai's '559 BC' is the traditional date of Cyrus II's accession in Anšan, not his birth.) The MEANING is where the node fails. Kent files the name under §164.V 'Uncertain names: Čišpi-; Kūru-; Dātuvahya-; Arxa-', i.e. he expressly gives it no etymology; and no standard authority reads it as 'curly hair'. Rüdiger Schmitt (Enc. Iranica, 'Cyrus i. The Name') says the etymology 'remains in dispute' and prefers Karl Hoffmann's *kuru- 'humiliator of the enemy in verbal contest' (to a root *(s)kau-); J. Harmatta took it to an Iranian kur- 'be born', hence 'young one'; J. Tavernier regards Elamite Kuraš as primary, 'to bestow care'; Wiktionary adds a possible Urartian toponym Quriani (the upper Kura). 'Curly hair' from *kur-wo- is a modern popular etymology built on Latin curvus/crispus and rests only on FAF:513, which is not accessible.\",\n  \"صورت‌های آوردهٔ نورایی کاملاً درست‌اند و — همراه با ارجاع Kent:180 — از حاشیهٔ معین گرفته شده‌اند: ستاک پارسی باستان Kūru-، حالت فاعلی مفرد Kūruš (کتیبهٔ CMa: adam Kūruš xšāyaθiya «من کوروش شاه»)، حالت اضافی Kūrauš (بیستون ۱٫۲۸: Kabūjiya nāma Kūrauš puça «کمبوجیه نام، پسر کوروش»)، در کنار Ku-raš عیلامی و Ku-ra-aš بابلی. سال ۵۵۹ پ.م. نیز سال جلوس است نه زادروز. اما معنا نادرست است: کنت خودِ نام را در بند ۱۶۴.V زیر عنوان «نام‌های با ریشه‌شناسی نامعلوم» جای می‌دهد و هیچ معنایی برای آن قائل نیست. ریشه‌شناسی امروزی نیز «موی مجعد» را نمی‌پذیرد: اشمیت (ایرانیکا) ریشه‌شناسی این نام را «همچنان محل اختلاف» می‌داند و پیشنهاد کارل هوفمان، یعنی *kuru- «خوارکنندهٔ دشمن در مشاعره»، را ترجیح می‌دهد؛ هارماتا آن را از kur- «زاده شدن» به معنی «جوان» گرفته و تاوِرنیه صورت عیلامی Kuraš را اصلی می‌داند. معنای «موی مجعد» ریشه‌شناسی عامیانه‌ای است که تنها بر مأخذ دسترس‌ناپذیر FAF:513 تکیه دارد؛ پژوهش امروزی آن را رد می‌کند.\",\n  [S_CYRUS_W, S_CYRUS_P],\n  [{\"ref\": \"KNT:180\", \"status\": \"partial\",\n    \"note\": \"Kent, Old Persian, Lexicon p. 180 (KNT.txt line 5294, leaf 203, the neighbouring leaf carries the printed '181'): 'Kūru- sb. \\\"Cyrus\\\", founder of the Persian Empire: Elam. ku-raš, Akk. ku-ra-aš, Gk. Κῦρος (§164.V). Kūruš nom. CMa 1; CMb 1; CMc.' The forms are confirmed; but §164.V (p. 55) reads 'V. Uncertain names: Čišpi- (or Čaišpi-); Kūru-; Dātuvahya-; Arxa- ...' — Kent gives the name NO meaning, so he cannot support 'curly hair'.\"},\n   {\"ref\": \"FAF:513\", \"status\": \"not_checked\",\n    \"note\": \"A. Daneshgar, Farhang-e Aʿlām-e Fārsi (Hafez Novin 1370) — refs_online.json records 'none online ... nothing digitised on any permitted platform'. This is the only reference Nourai offers for the 'curly hair' gloss.\"}],\n  [{\"src\": \"BQT\", \"where\": \"Borhān-e Qāṭeʿ, Moʿin's aʿlām supplement, s.v. کوروش (vol. 3, pdf p. 520 = printed p. ~1727)\", \"stance\": \"partial\",\n    \"note\": \"«کوروش — در پارسی باستان کورو Kūru، در صیغهٔ مفرد مذکر حالت فاعلی کوروش Kūruš، و در صیغهٔ مفرد مذکر حالت اضافی (مضاف‌الیه) Kūrauš. این نام در کتیبه‌های عیلامی Ku-raš، و در [کتیبه‌های] بابلی Ku-ra-aš، و در یونانی Κῦρος آمده. رک (Kent, Old Persian, p. 180)». This is Nourai's source for the four forms — and it offers no etymology whatever.\"},\n   {\"src\": \"KNT\", \"where\": \"Kent §164.V, p. 55\", \"stance\": \"contradicts\",\n    \"note\": \"'V. Uncertain names: ... Kūru- ...' — the very authority cited declares the name's interpretation unknown.\"}])\n\nN(10, \"Persian\", \"Kŭrosh «کورش، کوروش»\", \"disputed\",\n  \"The Persian name کوروش Kuruš/Kūroš is not an unbroken inheritance: the Achaemenid name left no trace in Middle or Classical New Persian (Ferdowsi's Šāhnāma has no Cyrus), and the modern form is a nineteenth/twentieth-century restoration read off the cuneiform after Rawlinson's decipherment — which is exactly why Moʿin's entry is a transliteration exercise citing Kent rather than a lexical article. کورش beside کوروش is merely the spelling with and without the waw for OP -u-. The gloss '\\\"sun\\\"' is not modern scholarship but Ctesias': Plutarch, Artaxerxes 1.3, reports 'Cyrus' as named after 'the sun, which in the Persian language is called Cyrus' (an association with Old Iranian hvar / New Persian خور 'sun'). Nourai takes it from Funk & Wagnalls, which prints '[Per., the sun.]' at the end of its Cyrus entry. Modern scholars reject it outright (see node #9); the phonetics do not work, since hvar- gives NP xor/xvar, not kur-. So the arrow OP Kūru- > NP کوروش is right in substance but modern and learned, and the gloss is a classical folk etymology.\",\n  \"نام فارسی «کوروش» میراث پیوستهٔ زبانی نیست: این نام در فارسی میانه و فارسی دری کلاسیک هیچ نشانی ندارد (در شاهنامه نیامده) و صورت امروزی آن بازسازی‌ای است که پس از رمزگشایی خط میخی در سدهٔ سیزدهم/نوزدهم از روی کتیبه‌ها ساخته شد؛ به همین سبب است که مدخل معین بیشتر آوانگاری صورت‌های کتیبه‌ای و ارجاع به کنت است تا مدخلی واژگانی. «کورش» و «کوروش» تنها دو املای یک نام‌اند (با واو و بی‌واو برای u پارسی باستان). اما معنای «خورشید» از پژوهش امروزی نیست، بلکه از کتزیاس است: پلوتارک در «اردشیر» ۱٫۳ می‌گوید نام کوروش از «خورشید» گرفته شده که «در زبان پارسی کوروش خوانده می‌شود» — یعنی پیوند با hvar ایرانی باستان و «خور» فارسی. نورایی این معنا را از فرهنگ فانک و واگنالز گرفته که در پایان مدخل Cyrus می‌نویسد «[فارسی: خورشید]». ریشه‌شناسی امروزی این را رد می‌کند و از نظر آوایی نیز نادرست است، زیرا hvar- در فارسی «خور/خُر» می‌دهد نه «کور». پس پیکان درست است ولی معنا ریشه‌شناسی عامیانهٔ کهن است.\",\n  [S_CYRUS_P],\n  [{\"ref\": \"BQT\", \"status\": \"partial\",\n    \"note\": \"Borhān-e Qāṭeʿ, Moʿin's aʿlām entry کوروش (v3 pdf p. 520): gives the Old Persian, Elamite, Babylonian and Greek forms and refers to Kent p. 180, but offers no etymology and never says 'sun'.\"},\n   {\"ref\": \"KNT:180\", \"status\": \"partial\",\n    \"note\": \"Kent p. 180 s.v. Kūru- lists the forms; §164.V classes the name as of uncertain interpretation. No 'sun'.\"}],\n  [{\"src\": \"FSD\", \"where\": \"Funk & Wagnalls New Standard Dictionary, vol. I s.v. Cyrus (~p. 644-648, FSD_vol1.txt leaf 706)\", \"stance\": \"partial\",\n    \"note\": \"'Cyrus ... 1. A masculine personal name. ... 2. \\\"The Great\\\" (?-528 B.C.), king of Persia: founder of the Persian empire. 3. \\\"The Younger\\\" ... [Per., the sun.]' — this is where Nourai's gloss comes from; it is a 1913 repetition of Ctesias.\"},\n   {\"src\": \"MON\", \"where\": \"Moʿin, aʿlām (as printed with Borhān-e Qāṭeʿ)\", \"stance\": \"silent\",\n    \"note\": \"the entry is purely historical/epigraphic; no etymology is proposed.\"}])\n\nN(11, \"Greek\", \"Kuros\", \"confirmed\",\n  \"Greek Κῦρος is the regular Hellenisation of Old Persian Kūruš: the Persian nominative ending -š is dropped and replaced by the Greek masculine o-stem ending -ος, the long ū being written υ. It is in use from the first half of the fifth century BCE — Aeschylus, Persians 768, and throughout Herodotus I — i.e. contemporary with the Achaemenids, so a direct oral borrowing, not a literary one; the later itacistic variant Κόρος also occurs. Kent lists 'Gk. Κῦρος' among the reflexes of Kūru- at the page Nourai cites for the parent node, and Moʿin's entry repeats it. Funk & Wagnalls, Nourai's reference here, gives the name and its Romance/Germanic equivalents (F. Cyrus, G. Cyrus, It. Ciro, Sp. Ciro); only its bracketed gloss '[Per., the sun.]' is obsolete.\",\n  \"صورت یونانی Κῦρος آوانویسی قاعده‌مند Kūruš پارسی باستان است: پایانهٔ فاعلی -š ایرانی می‌افتد و پایانهٔ مذکر یونانی -ος جای آن را می‌گیرد و ū کشیده با υ نوشته می‌شود. این نام از نیمهٔ نخست سدهٔ پنجم پیش از میلاد در متون یونانی هست — «پارسیان» آیسخولوس بیت ۷۶۸ و سراسر کتاب یکم هرودوت — یعنی هم‌روزگار هخامنشیان؛ پس وام‌گیری شفاهی و مستقیم است نه ادبی. صورت متأخر Κόρος نیز دیده می‌شود. کنت در همان صفحه‌ای که نورایی برای گرهٔ بالادست ارجاع می‌دهد «یونانی Κῦρος» را در شمار بازتاب‌های Kūru- می‌آورد و معین نیز همان را تکرار می‌کند. ادعای نورایی درست است.\",\n  [S_CYRUS_W],\n  [{\"ref\": \"FSD:644\", \"status\": \"supports\",\n    \"note\": \"Funk & Wagnalls vol. I s.v. Cyrus (FSD_vol1.txt leaf 706, printed page in the 644-650 range): the headword with 'F. Cyrus; G. Cyrus; It. Ciro; Sp. Ciro' and the two Persian kings — the entry Nourai is citing for both this node and node #13.\"}],\n  [{\"src\": \"KNT\", \"where\": \"Kent, Old Persian p. 180\", \"stance\": \"supports\",\n    \"note\": \"'Kūru- sb. \\\"Cyrus\\\" ... Gk. Κῦρος (§164.V).'\"},\n   {\"src\": \"BQT\", \"where\": \"Moʿin, aʿlām s.v. کوروش\", \"stance\": \"supports\",\n    \"note\": \"«و در یونانی Κῦρος آمده» — Moʿin lists the Greek form in the same series as the Elamite and Babylonian.\"}])\n\nN(12, \"Persian\", \"(no transliteration in the book) «کوروس، سیروس»\", \"plausible\",\n  \"An empty-word node: the book gives only the two Persian spellings. Both are re-borrowings of the Western form of the name back into Persian, so the arrow Greek > Persian is right in substance but the route is modern and European, not an ancient Greek loan into Persian. کوروس Kūrūs simply transliterates Greek Κῦρος / Latin Cyrus. سیروس Sīrus renders the FRENCH pronunciation of Cyrus, [siʁys], and entered Persian as a given name in the late Qajar / early Pahlavi period, alongside the restored کوروش; Persian Wikipedia s.v. سیروس says «سیروس یونانی‌شدهٔ نام فارسی کوروش است» ('Sirus is the Hellenised form of the Persian name Kuruš'). The pair کوروش ~ سیروس is thus a doublet of exactly the same kind as پارس ~ فارس or مهرداد ~ Mithridates: the native form and its Europeanised return.\",\n  \"این گره در کتاب هیچ آوانویسی ندارد و تنها دو املای فارسی در آن آمده است. هر دو صورت، وام‌گیری دوبارهٔ شکل غربی نام به فارسی‌اند؛ پس پیکان «یونانی ← فارسی» در اصل درست است اما مسیر آن نو و اروپایی است، نه وام‌گیری کهن از یونانی. «کوروس» صرفاً آوانویسی Κῦρος یونانی / Cyrus لاتین است و «سیروس» تلفظ فرانسوی Cyrus یعنی [siʁys] را بازمی‌نماید که در اواخر دورهٔ قاجار و آغاز پهلوی در کنار «کوروشِ» بازسازی‌شده به‌عنوان نام کوچک رایج شد؛ ویکی‌پدیای فارسی ذیل «سیروس» می‌نویسد: «سیروس یونانی‌شدهٔ نام فارسی کوروش است». پس «کوروش» و «سیروس» دوگانه‌ای (doublet) از همان گونه‌اند که «پارس/فارس» یا «مهرداد/Mithridates». با احتیاط پذیرفتنی است.\",\n  [S_SIRUS, S_CYRUS_P],\n  [{\"ref\": \"FAF:513\", \"status\": \"not_checked\",\n    \"note\": \"Daneshgar, Farhang-e Aʿlām-e Fārsi — refs_online.json: 'none online ... nothing digitised on any permitted platform'.\"}],\n  [{\"src\": \"MON\", \"where\": \"Moʿin, aʿlām s.v. کوروش (BQT v3 pdf p. 520)\", \"stance\": \"silent\",\n    \"note\": \"Moʿin gives only کوروش and the epigraphic forms; neither کوروس nor سیروس appears in the entry.\"},\n   {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls s.v. Cyrus\", \"stance\": \"partial\",\n    \"note\": \"the entry's list of European equivalents ('F. Cyrus, 1 sīrü', 2 cy'rü'; G. Cyrus; It. Ciro; Sp. Ciro') documents precisely the French pronunciation that Persian سیروس reproduces.\"}])\n\nN(13, \"English\", \"Cyrus\", \"confirmed\",\n  \"English Cyrus comes through Latin Cȳrus (Cicero, De divinatione; the Vulgate of Isaiah 44-45, Ezra 1, Daniel 1) from Greek Κῦρος, with the regular Latin transcription of υ as y and of the Greek -ος as -us. It is not a learned modern borrowing from the cuneiform but a Bible name: the Wycliffite and then the Geneva and King James versions carry it, and it became a common English (especially Puritan and later American) given name from the seventeenth century, whence Cyrus McCormick, Cyrus Field and the like. Funk & Wagnalls p. 644 has exactly this entry ('Cyrus ... 1. A masculine personal name ... 2. \\\"The Great\\\" ... king of Persia: founder of the Persian empire'); only its closing gloss '[Per., the sun.]' is the obsolete Ctesian etymology discussed at node #10. The chain drawn — Old Persian > Greek > English — is right, with Latin as the unnamed intermediate.\",\n  \"صورت انگلیسی Cyrus از راه Cȳrus لاتین (سیسرون؛ ترجمهٔ ولگات در اشعیا ۴۴–۴۵، عزرا ۱ و دانیال ۱) از Κῦρος یونانی آمده است، با تبدیل قاعده‌مند υ یونانی به y و پایانهٔ -ος به -us در لاتین. این نام وام‌گیری نوِ عالمانه از کتیبه‌های میخی نیست بلکه نامی کتاب‌مقدسی است: از ترجمهٔ ویکلیف و سپس ترجمه‌های ژنو و شاه جیمز به انگلیسی رسید و از سدهٔ هفدهم به بعد (به‌ویژه نزد پیوریتن‌ها و سپس در آمریکا) نام کوچک رایجی شد. فرهنگ فانک و واگنالز در ص ۶۴۴ همین مدخل را دارد؛ تنها یادداشت پایانی آن «[فارسی: خورشید]» ریشه‌شناسی منسوخ کتزیاسی است که در گرهٔ ۱۰ بحث شد. زنجیرهٔ نمودار (پارسی باستان ← یونانی ← انگلیسی) درست است و تنها حلقهٔ لاتین در آن نامبرده نشده است.\",\n  [S_CYRUS_W],\n  [{\"ref\": \"FSD:644\", \"status\": \"supports\",\n    \"note\": \"Funk & Wagnalls vol. I s.v. Cyrus (FSD_vol1.txt leaf 706): 'Cy'rus, 1 sai'rus; 2 cy'rus, n. 1. A masculine personal name. ... 2. \\\"The Great\\\" (?-528 B.C.), king of Persia: founder of the Persian empire. 3. \\\"The Younger\\\" (424?-401 B.C.) ... [Per., the sun.]'\"}],\n  [{\"src\": \"KNT\", \"where\": \"Kent p. 180\", \"stance\": \"supports\",\n    \"note\": \"gives Gk. Κῦρος as the reflex of OP Kūru-, the link on which the Latin and English forms depend.\"},\n   {\"src\": \"KLN\", \"where\": \"Klein, Comprehensive Etymological Dictionary\", \"stance\": \"silent\",\n    \"note\": \"Klein has no headword 'Cyrus' (personal names are largely outside his scope); a grep of KLN_1966/KLN_1971 finds no entry.\"}])\n\nN(14, \"Latin\", \"curvus; crista; crispus\", \"confirmed\",\n  \"All three Latin words, meanings and root are right, though they sit in different branches of the entry. curvus 'crooked, bent, arched' is at IEW 935 with the note '(forms -uo-)', i.e. from *kur- + -wo-; Ernout-Meillet: 'Même vocalisme que dans gr. κυρτός \\\"courbe\\\" ... De plus, cf. circus.' crista 'the comb/tuft on an animal's head, crest' and crispus 'frizzy, curling' stand together at IEW 937 under the s-extension *(s)krei-s-, beside crīnis 'hair' (< *crisnis): 'Latin crinis \\\"hair\\\" (*crisnis, compare:) cris-ta \\\"the comb am Kopfe the animal\\\" ... here as *-do-derivative also: Latin crispus \\\"frizzy, sich kräuselnd\\\"'. Watkins reconstructs them as *kris-tā- and *krip-so- ('metathesized from *cripsus'), and Ernout-Meillet confirms the metathesis independently: 'Ancien *krip-sos (pour la métathèse, cf. uespa), qui se retrouve seulement en celtique: gall. crych \\\"frisé\\\"'. The only slip is structural: crista and crispus descend from the *krei-s- extension, not from the *kur-wo- box drawn as their parent.\",\n  \"هر سه واژهٔ لاتین، معنای آن‌ها و پیوندشان با این ریشه درست است، هرچند هر یک به شاخه‌ای جداگانه تعلق دارد. curvus «کج، خمیده، قوسی» در پوکورنی ص ۹۳۵ با یادداشت «(با پسوند -uo-)» آمده است، یعنی از *kur- + -wo-؛ ارنو-مِیه می‌نویسد: «همان واکه‌آرایی که در κυρτός یونانی هست ... و نیز بنگرید به circus». crista «تاج و کاکل پرندگان» و crispus «مجعد» با هم در ص ۹۳۷ زیر گسترشِ s‑دار *(s)krei-s- و در کنار crīnis «مو» (از *crisnis) آمده‌اند. واتکینز آن‌ها را *kris-tā- و *krip-so- («با قلب از *cripsus») بازمی‌سازد و ارنو-مِیه نیز همین قلب را مستقلاً تأیید می‌کند: «*krip-sos کهن (برای قلب، uespa را بنگرید) که تنها در سلتی بازمانده است: ولزی crych «مجعد»». تنها ایراد ساختاری است: crista و crispus از گسترشِ *krei-s- می‌آیند نه از جعبهٔ *kur-wo- که در نمودار پدر آن‌ها نشان داده شده است. ادعای نورایی در اصل درست است.\",\n  [],\n  [{\"ref\": \"POK:935\", \"status\": \"supports\",\n    \"note\": \"IEW 935: 'Latin curvus \\\"crooked, writhed, crooked, humped, arched\\\" (forms -uo-)'; IEW 937 (same lemma, which runs 935-938): 'Latin crinis \\\"hair, esp. hair of the head\\\" (*crisnis, compare:) cris-ta \\\"the comb am Kopfe the animal\\\" ... here as *-do-derivative also: Latin crispus \\\"frizzy, sich krauseind, vibrierend\\\", crispo, -are \\\"frill, friz, swing\\\"'.\"}],\n  [{\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. sker-3 §§4, 6, 7\", \"stance\": \"supports\",\n    \"note\": \"'*kur-wo- in Latin curvus'; '*kris-tā- in Latin crista, tuft, crest'; '*krip-so- in Latin crispus (metathesized from *cripsus), curly'.\"},\n   {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.vv. curuus, crispus, crista\", \"stance\": \"partial\",\n    \"note\": \"curuus and crispus are linked to the family ('Ancien *krip-sos ... gall. crych'), but of crista they write 'Cf. crinis. Les rapprochements d'autres mots sont aventurés' — i.e. crista goes with crinis and further comparisons are risky.\"},\n   {\"src\": \"KLN\", \"where\": \"Klein s.vv. crest, crisp\", \"stance\": \"supports\",\n    \"note\": \"'crest ... fr. L. crista ... a -t-enlargement of I.-E. base *qreis-'; 'crisp ... fr. L. crispus \\\"curly\\\" ... fr. I.-E. base *(s)qreis-, whence also L. crinis (for *crisnis) and crista'.\"}])\n\nN(15, \"English\", \"curve, curb, curvature; crest; crisp, crepe\", \"confirmed\",\n  \"Watkins lists exactly this set under sker-3: '§4 ... Latin curvus ...: CURB, CURVATURE, CURVE, CURVET'; '§6 ... Latin crista ...: CREST, CRISTA, CRISTATE'; '§7 ... Latin crispus ...: CREPE, CRISP, CRISPATE'. Routes: curve is Latin curvāre taken into English as a verb in the fifteenth century (the noun 1690s); curb is Old French courber 'to bend' < curvāre, into Middle English as a horse's chin-strap, then 'restrain', then the stone edging of a pavement; curvature is Latin curvātūra, sixteenth century. crest is Middle English creste < Old French creste (modern crête) < Latin crista (Klein s.v. crest). crisp is the oldest of them: it was borrowed straight into Old English from Latin crispus and meant 'curly' for a thousand years before the modern 'brittle' sense took over (Klein: 'crisp, adj. — OE., fr. L. crispus \\\"curly\\\"'); crepe is French crêpe, feminine of crêp(e) < Latin crispus, 'crinkled silk gauze', borrowed in the eighteenth century, so crisp and crepe are doublets.\",\n  \"واتکینز دقیقاً همین مجموعه را زیر sker-3 آورده است: از curvus لاتین CURB، CURVATURE، CURVE و CURVET؛ از crista واژه‌های CREST، CRISTA و CRISTATE؛ و از crispus واژه‌های CREPE، CRISP و CRISPATE. مسیرها چنین است: curve همان فعل لاتینی curvāre است که در سدهٔ پانزدهم به انگلیسی راه یافت؛ curb از فرانسهٔ کهن courber «خم کردن» (از curvāre) است که نخست به معنی زنجیر زیر چانهٔ اسب و سپس «مهار کردن» و سرانجام «جدول سنگی پیاده‌رو» به کار رفت؛ curvature از curvātūra لاتین است. crest از فرانسهٔ کهن creste و آن از crista لاتین است (کلاین). crisp کهن‌ترین آن‌هاست: در انگلیسی باستان مستقیماً از crispus لاتین وام گرفته شد و هزار سال به معنی «مجعد» بود پیش از آنکه معنای امروزی «تُرد» بر آن چیره شود؛ crepe نیز از crêpe فرانسوی و در نهایت از همان crispus است، پس crisp و crepe دوگانه (doublet) یکدیگرند. ادعای نورایی درست است.\",\n  [],\n  [{\"ref\": \"AHD\", \"status\": \"supports\",\n    \"note\": \"Watkins 1985 s.v. sker-3: §4 'CURB, CURVATURE, CURVE, CURVET'; §6 'CREST, CRISTA, CRISTATE'; §7 'CREPE, CRISP, CRISPATE'. Every English word in the box is in the appendix under this root.\"}],\n  [{\"src\": \"KLN\", \"where\": \"Klein s.vv. curve, curvet, crest, crisp\", \"stance\": \"supports\",\n    \"note\": \"'curve, tr. v. — L. curvāre, \\\"to crook, bend, twist\\\", fr. curvus'; 'crest, n. — ME., fr. OF. creste (F. crête), fr. L. crista'; 'crisp, adj. ... — OE., fr. L. crispus, \\\"curly\\\"'.\"},\n   {\"src\": \"POK\", \"where\": \"IEW 935, 937\", \"stance\": \"supports\",\n    \"note\": \"the Latin etyma of all six English words (curvus, crista, crispus) are in the (s)ker-3 entry.\"}])\n\nN(16, \"Greek\", \"krikos\", \"confirmed\",\n  \"Greek κρίκος 'ring' is real and the gloss exact. Pokorny 936, under the guttural extension ker-k-/kir-k-/(s)krek-, prints 'gr. κίρκος m. \\\"Ring\\\" (κιρκόω \\\"tie with a ring\\\"), usually (from Homer) κρίκος' — i.e. κίρκος is the older shape and κρίκος the metathesised one that prevails from Homer on (Il. 24.272, of the ring on a chariot yoke). Watkins accounts for it as 'Perhaps reduplicated form *ki-kr-o- metathesized into Greek krikos, a ring'. Klein s.v. circus takes the same view of the family: 'Gk. κίρκος, κρίκος, \\\"a ring\\\", fr. I.-E. base *qri-q-, enlargement of base *qer-, \\\"to turn, twist\\\", whence L. curvus'. Nourai's only structural slip is again the parent: κρίκος does not come from *kur-wo- but from the k-extension of the same root.\",\n  \"واژهٔ یونانی κρίκος «حلقه» واقعی است و معنای آن در نمودار دقیق. پوکورنی در ص ۹۳۶ زیر گسترشِ گلوگاهی ker-k-/kir-k- می‌نویسد: «یونانی κίρκος مذکر «حلقه» (κιρκόω «با حلقه بستن»)، و معمولاً (از هومر به بعد) κρίκος» — یعنی κίρκος صورت کهن‌تر است و κρίκος صورت مقلوب که از هومر به بعد غالب می‌شود (ایلیاد ۲۴٫۲۷۲، دربارهٔ حلقهٔ یوغ ارابه). واتکینز آن را چنین توضیح می‌دهد: «شاید صورت مضاعف *ki-kr-o- که در یونانی به krikos قلب شده است». کلاین نیز ذیل circus همین را می‌گوید: «یونانی κίρκος، κρίκος «حلقه»، از پایهٔ هندواروپایی *qri-q-، گسترشِ پایهٔ *qer- «پیچیدن، تابیدن» که curvus لاتین نیز از آن است». تنها ایراد نورایی باز هم پدرِ نادرست است: κρίκος نه از *kur-wo- بلکه از گسترشِ k‑دارِ همان ریشه می‌آید. ادعا در اصل درست است.\",\n  [],\n  [{\"ref\": \"POK:935\", \"status\": \"supports\",\n    \"note\": \"IEW 935-936, lemma (s)ker-3, sub-section 'a) guttural extensions: ker-k-, besides kir-k- (from redupl. *ki-kro-) and (s)krek-': 'gr. κίρκος m. \\\"Ring\\\" (κιρκόω \\\"tie with a ring\\\"), usually (from Homer) κρίκος ... Latin circus'.\"}],\n  [{\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. sker-3 §9\", \"stance\": \"supports\",\n    \"note\": \"'Perhaps reduplicated form *ki-kr-o- metathesized into Greek krikos, a ring (> Latin circus, ring, circle): CIRCA, CIRCLE, CIRCUM-, SEARCH; CRICOID.'\"},\n   {\"src\": \"KLN\", \"where\": \"Klein s.v. circus\", \"stance\": \"supports\",\n    \"note\": \"'Gk. κίρκος, κρίκος, \\\"a ring\\\", fr. I.-E. base *qri-q-, enlargement of base *qer-, \\\"to turn, twist\\\", whence L. curvus.'\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat s.v. Ring (1)\", \"stance\": \"supports\",\n    \"note\": \"'Ring (1), a circle. (E.) M.E. ring. A.S. hring. + Du. ring ... Gk. κρίκος, κίρκος, L. circus, Russ. krug' — Skeat puts krikos, circus and hring in one family, as the chart does.\"}])\n\nN(17, \"Latin\", \"circus\", \"confirmed\",\n  \"Latin circus 'ring, circular line; the (round) racecourse' is at IEW 936 in the same paragraph as Greek κίρκος/κρίκος. The arrow Greek > Latin is a borrowing, and that is how the standard handbooks take it: Klein, 'L. circus, \\\"a circle, ring, a round enclosure for games\\\", more prob. borrowed from, than cogn. with Gk. κίρκος, κρίκος, \\\"a ring\\\"' — the loan will have come with the Greek hippodrome vocabulary of Magna Graecia in the third century BCE. Ernout-Meillet note that the original sense was simply 'cercle', which was then taken over by the diminutive circulus, leaving circus attached to the building ('sens premier \\\"cercle\\\", mais a été remplacé dans cette acception par le diminutif circulus, et a tendu à ne plus désigner que le \\\"cirque\\\"'). So the chart's gloss 'circle' is the primary Latin meaning, correctly given.\",\n  \"واژهٔ لاتین circus «حلقه، دایره؛ میدان گرد اسب‌دوانی» در پوکورنی ص ۹۳۶ در همان بند یونانی κίρκος/κρίκος آمده است. پیکان «یونانی ← لاتین» پیکان وام‌گیری است و فرهنگ‌های معیار نیز آن را چنین می‌بینند: کلاین می‌نویسد «circus لاتین ... به احتمال بیشتر از یونانی κίρκος، κρίκος وام گرفته شده تا آنکه هم‌ریشهٔ آن باشد»؛ این وام‌گیری احتمالاً همراه با واژگان اسب‌دوانی یونانیِ جنوب ایتالیا در سدهٔ سوم پیش از میلاد وارد لاتین شده است. ارنو-مِیه یادآور می‌شوند که معنای نخستین آن صرفاً «دایره» بوده که سپس به مصغّرِ circulus واگذار شد و circus تنها بر بنای میدان باقی ماند. پس معنای «دایره» که نورایی آورده معنای نخستینِ درست است. ادعای نورایی درست است.\",\n  [],\n  [{\"ref\": \"POK:935\", \"status\": \"supports\",\n    \"note\": \"IEW 936 (lemma (s)ker-3, pp. 935-938): 'Latin circus \\\"Zirkellinie, circle in the Astronomie; esp. the (round) racecourse\\\", preposition circum \\\"ringsumher\\\" etc., circa'.\"}],\n  [{\"src\": \"KLN\", \"where\": \"Klein s.v. circus\", \"stance\": \"supports\",\n    \"note\": \"'circus, n. — L. circus, \\\"a circle, ring, a round enclosure for games\\\", more prob. borrowed from, than cogn. with Gk. κίρκος, κρίκος, \\\"a ring\\\".'\"},\n   {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. circus\", \"stance\": \"supports\",\n    \"note\": \"'circus, -ī m.: sens premier \\\"cercle\\\", mais a été remplacé dans cette acception par le diminutif circulus, et a tendu à ne plus désigner que le \\\"cirque\\\".'\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins s.v. sker-3 §9\", \"stance\": \"supports\",\n    \"note\": \"'Greek krikos, a ring (> Latin circus, ring, circle)' — the '>' marks the borrowing.\"}])\n\nN(18, \"English\", \"circus, circle, search\", \"confirmed\",\n  \"Watkins gives the three together: 'Greek krikos ... (> Latin circus, ring, circle): CIRCA, CIRCLE, CIRCUM-, SEARCH'. circus is the Latin noun taken over unchanged — in English from the late fourteenth century of the Roman arena, and from 1791 of Astley's Royal Circus in London, whence the modern travelling show; circle is Middle English cercle from Old French cercle from Latin circulus, the diminutive of circus (so it reaches English through French, not directly); search is the least obvious member and the best attested — Middle English serchen from Old French cerchier (modern chercher) from Late Latin circāre 'to go round (hence, to explore)', a denominative of circus. Klein: 'search ... — ME. serchen, fr. OF. cerchier, fr. L. circāre, \\\"to go round\\\", fr. circum, \\\"around\\\". See circum- and cp. circa, circle, circus.' Skeat says the same in one line: 'search, to explore. (F. - L.) M.E. serchen, cerchen. - O.F. cerchier. - L. circāre, to go round; hence, to explore. - L. circus, a ring.'\",\n  \"واتکینز هر سه واژه را با هم می‌آورد: «یونانی krikos ... (> لاتین circus «حلقه، دایره»): CIRCA، CIRCLE، CIRCUM-، SEARCH». واژهٔ circus همان اسم لاتین است که بی‌تغییر به انگلیسی رفت — از اواخر سدهٔ چهاردهم به معنی میدان رومی و از ۱۷۹۱ به معنی «سیرک» (از نام «سیرک سلطنتی» اَستلی در لندن). واژهٔ circle از cercle فرانسهٔ کهن و آن از circulus لاتین، مصغّرِ circus، است؛ پس از راه فرانسه به انگلیسی رسیده نه مستقیم. واژهٔ search ناآشکارترین و در عین حال مستندترین عضو این خانواده است: انگلیسی میانه serchen از فرانسهٔ کهن cerchier و آن از circāre لاتین متأخر «گرد چیزی گشتن، پس جست‌وجو کردن» که فعلی است ساخته‌شده از circus. کلاین و اسکیت هر دو همین را می‌گویند. ادعای نورایی درست است.\",\n  [],\n  [{\"ref\": \"AHD\", \"status\": \"supports\",\n    \"note\": \"Watkins 1985 s.v. sker-3 §9: 'CIRCA, CIRCLE, CIRCUM-, SEARCH; CRICOID.'\"}],\n  [{\"src\": \"KLN\", \"where\": \"Klein s.vv. search, circus\", \"stance\": \"supports\",\n    \"note\": \"'search, tr. and intr. v. — ME. serchen, fr. OF. cerchier, fr. L. circāre, \\\"to go round\\\", fr. circum, \\\"around\\\". See circum- and cp. circa, circle, circus.'\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat s.vv. search, circus\", \"stance\": \"supports\",\n    \"note\": \"'search, to explore. (F. - L.) M.E. serchen, cerchen. - O.F. cerchier (F. chercher). - L. circāre, to go round; hence, to explore. - L. circus, a ring (above).' and 'circus, a ring. (L.) L. circus (above).'\"}])\n\nN(19, \"Germanic\", \"skrink; hringaz; hrugjaz\", \"plausible\",\n  \"All three Germanic stems are genuinely in Pokorny's entry, but they belong to three different extensions and one gloss is wrong. (a) *skrink- : IEW 936, nasalized (s)kreng-, 'Old English scrincan \\\"shrink up, verschrumpfen, wither\\\", Middle Low German schrinken'; Watkins writes it 'Germanic *skrink-'. 'To shrivel up' is a fair gloss. (b) *hringaz : IEW 936, (s)kregh-/(s)krengh-, 'urgerm. *hrengaz in Finnish rengas [a loan], Old Icelandic hringr, Old English, Old Saxon, Old High German hring \\\"ring\\\"'; Wiktionary reconstructs *hringaz 'ring, circle' < PIE *(s)krengʰ-. The gloss 'circle' is acceptable. (c) *hrugjaz : IEW 937-938 puts Old Icelandic hryggr 'backbone, spine', Old English hrycg, Old Saxon hruggi, Old High German (h)rukki 'back' under the k-extension (s)kreu-k-, and Watkins under '*kreuk- in Germanic *hrugjaz'. Its meaning is 'back, spine, ridge', NOT 'edge' as the chart prints — Wiktionary glosses the reconstruction 'back, spine, ridge' and adds that the PIE connection is 'highly speculative'. So: forms and root right, one gloss wrong, and the common parent *kur-wo- wrong for all three.\",\n  \"هر سه ستاک ژرمنی به‌راستی در مدخل پوکورنی هستند، اما به سه گسترشِ متفاوت تعلق دارند و معنای یکی از آن‌ها نادرست است. نخست *skrink-: پوکورنی ص ۹۳۶ زیر صورت خیشومی‌شدهٔ (s)kreng- «انگلیسی باستان scrincan «چروکیده و پژمرده شدن»» را می‌آورد و واتکینز آن را *skrink- ژرمنی می‌نویسد؛ معنای «چروکیده شدن» درست است. دوم *hringaz: پوکورنی ص ۹۳۶ زیر (s)krengh- «ژرمنی آغازین *hrengaz در ایسلندی کهن hringr و انگلیسی/ساکسونی/آلمانی علیای باستان hring «حلقه»» و ویکی‌واژه آن را از *(s)krengʰ- هندواروپایی می‌گیرد؛ معنای «دایره» پذیرفتنی است. سوم *hrugjaz: پوکورنی در ص ۹۳۷–۹۳۸ ایسلندی کهن hryggr «ستون فقرات» و انگلیسی باستان hrycg و آلمانی علیای باستان (h)rukki «پشت» را زیر گسترشِ (s)kreu-k- جای می‌دهد؛ معنای این ستاک «پشت، ستون فقرات، ستیغ» است نه «لبه» که در کتاب چاپ شده، و ویکی‌واژه پیوند آن با ریشهٔ هندواروپایی را «بسیار حدسی» می‌خواند. پس صورت‌ها و ریشه درست‌اند، یک معنا نادرست است، و پدرِ مشترکِ *kur-wo- برای هر سه نادرست است.\",\n  [S_HRINGAZ, S_HRUGJAZ],\n  [{\"ref\": \"POK:935\", \"status\": \"partial\",\n    \"note\": \"IEW 936 has 'Old English scrincan \\\"shrink up, verschrumpfen, wither\\\"' and 'urgerm. *hrengaz ... Old Icelandic hringr, Old English Old Saxon Old High German hring \\\"ring\\\"'; IEW 937-938 has 'Old Icelandic hryggr \\\"backbone, spine\\\", Old English hrycg, Old Saxon hruggi, Old High German (h)rukki \\\"back\\\"'. The page is right and the forms are right, but the gloss 'edge' for hrugjaz is not Pokorny's ('backbone, spine, back').\"}],\n  [{\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. sker-3 §§1a, 2, 3\", \"stance\": \"partial\",\n    \"note\": \"'Germanic *skrink- in Old English scrincan, to wither, shrivel up: SHRINK'; 'Extended form *(s)kregh- in nasalized form *skre-n-gh- in Germanic *hringaz, something curved, circle'; 'Extended form *kreuk- in Germanic *hrugjaz in: a. Old English hrycg, spine, ridge ... b. Old High German hrukki, back'. Watkins glosses *hrugjaz 'spine, ridge', never 'edge'.\"},\n   {\"src\": \"WLD\", \"where\": \"WP II 568 ff. ('(s)qer- drehen, biegen', Erweiterungen)\", \"stance\": \"supports\",\n    \"note\": \"the Germanic material of these three extensions is collected there (Walde-Pokorny is Pokorny's own source for the section, cited by him as 'WP. II 568 ff.').\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat s.v. Ring (1)\", \"stance\": \"supports\",\n    \"note\": \"'M.E. ring. A.S. hring. + Du. ring, Low G. ring, rink, Icel. hringr, Swed. Dan. G. ring, O.H.G. hrinc; Gk. κρίκος, κίρκος, L. circus.'\"}])\n\nN(20, \"English\", \"shrink; ring, ranch, range, rink, arrange, derange, ribbon; ridge\", \"plausible\",\n  \"Eight of the nine English words are in Watkins under sker-3, in exactly Nourai's groupings: 'Germanic *skrink- in Old English scrincan ...: SHRINK'; '*hringaz ... a. Old English hring, a ring: RING; b. Old French renc, reng, line, row: RANCH, RANGE, RANK, RINK; ARRANGE, DERANGE'; '*hrugjaz ... Old English hrycg, spine, ridge: RIDGE'. The Romance group goes back to Frankish *hring 'circle (of men drawn up)', borrowed into Gallo-Romance as renc/ranc 'row, rank', whence Old French rangier/arengier > arrange, desrengier > derange, and Spanish rancho 'group messing together' > ranch; rink is the Scots form of the same Old French renc. ribbon is the one item Watkins does not list, and Etymonline calls it 'a word of unknown origin, possibly from a Germanic compound whose second element is related to band; compare Middle Dutch ringhband \\\"necklace\\\"'. Klein states the same derivation positively — 'ribbon, also riband, n. — ME. riban(d), fr. OF. riban, var. of ruban (F. ruban), fr. MDu. ringh-band, \\\"necklace\\\". The first element of this compound is rel. to E. ring' — and that is presumably Nourai's warrant. So ribbon belongs here only on Klein's (possible but unproved) etymology; everything else is confirmed.\",\n  \"هشت واژه از نُه واژهٔ این جعبه، با همان دسته‌بندی نورایی، در پیوست واتکینز زیر sker-3 آمده‌اند: از *skrink- ژرمنی و scrincan انگلیسی باستان واژهٔ SHRINK؛ از *hringaz واژه‌های RING (از hring انگلیسی باستان) و RANCH، RANGE، RANK، RINK، ARRANGE و DERANGE (از renc/reng فرانسهٔ کهن)؛ و از *hrugjaz واژهٔ RIDGE. گروه رومی از *hring فرانکی «حلقهٔ مردان صف‌کشیده» می‌آید که به گالو-رومی وام داده شد و renc/ranc «صف، رده» را داد؛ از آن arengier > arrange و desrengier > derange، و در اسپانیایی rancho «گروه هم‌خوراک» > ranch؛ rink نیز صورت اسکاتلندی همان renc است. تنها واژهٔ ribbon در فهرست واتکینز نیست: اتیمآنلاین آن را «واژه‌ای با خاستگاه نامعلوم» می‌خواند که «شاید از ترکیبی ژرمنی باشد که جزء دوم آن با band خویشاوند است؛ ringhband هلندی میانه «گردنبند» را بسنجید»، در حالی که کلاین همین ریشه‌شناسی را با قطعیت می‌آورد و جزء نخست آن را با ring انگلیسی یکی می‌داند — که ظاهراً مستند نورایی است. پس ribbon تنها بر پایهٔ نظر کلاین در اینجا جای می‌گیرد؛ باقی واژه‌ها تأیید می‌شوند. با احتیاط پذیرفتنی است.\",\n  [S_RIBBON, S_HRINGAZ],\n  [{\"ref\": \"AHD\", \"status\": \"partial\",\n    \"note\": \"Watkins 1985 s.v. sker-3: '1a ... SHRINK'; '2a ... RING'; '2b Old French renc, reng, line, row: RANCH, RANGE, RANK, RINK; ARRANGE, DERANGE'; '3a Old English hrycg, spine, ridge: RIDGE'. RIBBON does not appear anywhere in the entry.\"}],\n  [{\"src\": \"KLN\", \"where\": \"Klein s.v. ribbon\", \"stance\": \"supports\",\n    \"note\": \"'ribbon, also riband, n. — ME. riban(d), fr. OF. riban, var. of ruban (F. ruban), fr. MDu. ringh-band, \\\"necklace\\\". The first element of this compound is rel. to E. ring, n., the second to E. band, \\\"a tie\\\".'\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat s.v. Ring (1)\", \"stance\": \"supports\",\n    \"note\": \"'Ring (1), a circle. (E.) M.E. ring. A.S. hring.' — the native English member of the group.\"},\n   {\"src\": \"POK\", \"where\": \"IEW 936, 937-938\", \"stance\": \"supports\",\n    \"note\": \"the Germanic etyma of shrink, ring and ridge (scrincan, hring, hrycg) are all printed in the (s)ker-3 entry.\"}])\n\nentry = {\n    \"entry\": 1,\n    \"root\": \"Sker 1\",\n    \"verdict\": \"confirmed\",\n    \"modern_form\": \"PIE *(s)ker- 'to turn, bend' (Pokorny's 3. (s)ker-, IEW 935-938; Watkins/AHD sker-3)\",\n    \"note\": \"Root, language label, gloss and page are all right. Pokorny IEW 935-938 heads the lemma '(s)ker-3', Meaning: 'to turn, bend', with the note '(see also 1. (s)ker- \\\"shrivel, shrink\\\" and 2. (s)ker- \\\"spring\\\")'; Walde-Pokorny II 568 ff. print it as '(s)qer- \\\"drehen, biegen\\\"'; Watkins closes his sker-3 entry '[Pok. 3. (s)ker- 935.]'. Nourai's numbering 'Sker 1 / Sker 2' is his own and does not match Pokorny's (Nourai's Sker 2 is a redirect to Sek). Two cautions that colour the whole page: (i) Watkins himself calls this the 'presumed base of a number of distantly related derivatives' — it is a bundle of guttural, dental and labial extensions rather than one tight family, and Nourai's two intermediate boxes (*Kor-ōna, *Kur-wo) are made to carry children that in his own sources hang from quite different extensions; (ii) the Iranian branch (Av. karana- 'end, edge' > Pahl. kanār > NP karān/kanār) is attached to this root on Mann's authority alone — Buck, at the page Nourai cites, writes 'etym.?', and Pokorny/Walde-Pokorny list under this root only Avestan skarəna- 'round', not karana-.\",\n    \"note_fa\": \"ریشه، برچسب زبانی، معنا و شمارهٔ صفحه همگی درست‌اند: پوکورنی در صفحات ۹۳۵ تا ۹۳۸ سرواژهٔ «(s)ker-3» را با معنای «پیچیدن، خمیدن» آورده و یادآور شده که آن را با «(s)ker- ۱ (چروکیدن)» و «(s)ker- ۲ (جهیدن)» اشتباه نگیرند؛ والده-پوکورنی (ج ۲ ص ۵۶۸ به بعد) همان را با املای «(s)qer- «drehen, biegen»» ثبت کرده‌اند و واتکینز نیز مدخل sker-3 خود را با «[پوکورنی ۳. (s)ker- ص ۹۳۵]» به پایان می‌برد. شماره‌گذاری «Sker 1 / Sker 2» از آنِ خود نورایی است و با شماره‌گذاری پوکورنی نمی‌خواند. دو هشدار که بر کل این صفحه سایه می‌افکند: نخست آنکه خود واتکینز این را «پایهٔ مفروض شماری مشتقات دورخویشاوند» می‌خواند، یعنی مجموعه‌ای از گسترش‌های گوناگون است نه یک خانوادهٔ فشرده؛ و نورایی دو جعبهٔ میانی خود (*Kor-ōna و *Kur-wo) را وادار کرده فرزندانی را بپذیرند که در مأخذ خودِ او از گسترش‌های دیگری می‌آیند. دوم آنکه شاخهٔ ایرانی (اوستایی karana- «کرانه» ← پهلوی kanār ← فارسی کران/کنار) تنها بر پایهٔ مان به این ریشه بسته شده است؛ باک در همان صفحه‌ای که نورایی ارجاع می‌دهد می‌نویسد «ریشه‌شناسی؟» و پوکورنی و والده-پوکورنی زیر این ریشه تنها skarəna- اوستایی «گرد» را می‌آورند نه karana- را.\",\n    \"sources\": [S_KORONOS, S_KARAN],\n    \"ref_check\": [\n        {\"ref\": \"POK:935\", \"status\": \"supports\",\n         \"note\": \"POK_full.txt: 'Root / lemma: (s)ker-3 / Meaning: to turn, bend / Note: (see also 1. (s)ker- \\\"shrivel, shrink due to excess dryness, wrinkle up\\\" and 2. (s)ker- \\\"spring\\\") / Material: A. Avestan skarana- \\\"round\\\" ... gr. κυρτός \\\"crooked\\\" ... κορωνός ... Latin curvus ... References: WP. II 568 ff., WH. I 220 f. ... Page(s): 935-938'. The page number is exact and the gloss is verbatim.\"}],\n    \"consulted\": [\n        {\"src\": \"WLD\", \"where\": \"Walde-Pokorny II 568-569\", \"stance\": \"supports\",\n         \"note\": \"'(s)q[er- \\\"drehe]n, biegen\\\" (s. auch sqer- \\\"einschrumpfen\\\" und sqer- \\\"springen\\\"). ... Av. skarəna- \\\"rund\\\" ... gr. κυρτός \\\"krumm\\\" ... κορωνός \\\"gekrümmt\\\" ... lat. curvus \\\"krumm, gekrümmt, gewölbt\\\" (Formans -no- oder allenfalls von der eu-Basis)'.\"},\n        {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. sker-3\", \"stance\": \"supports\",\n         \"note\": \"'sker-3. Also ker-. To turn, bend. Presumed base of a number of distantly related derivatives. ... [Pok. 3. (s)ker- 935.]' — the whole of Nourai's page 424 is an expansion of this single appendix entry plus the Iranian branch.\"},\n        {\"src\": \"IEC\", \"where\": \"Mann, pp. 533, 535, 536, ~595\", \"stance\": \"partial\",\n         \"note\": \"Mann does not have one root but four adjacent lemmas: 'kor- \\\"bend, curve; bent, curved\\\"' (p.533), 'korōn-, korən- \\\"edge, rim, border\\\"' (p.535), 'korono- \\\"curve-\\\"' (p.536) and '(kuruos \\\"bent, round\\\". Assumed for Latin only)'. Nourai's two intermediate boxes conflate them.\"},\n        {\"src\": \"SYN\", \"where\": \"Buck 12.35 END, p. 857\", \"stance\": \"partial\",\n         \"note\": \"'Av. karana- (also in special senses \\\"border, shore\\\", etc.; NPers. karan \\\"shore, side\\\"), etym.? Barth. 451.' — Buck supplies the Iranian words but declines to assign them a root.\"}],\n    \"nodes\": nodes,\n}\n\ndoc = {\n    \"pdf_page\": 454,\n    \"book_page\": 424,\n    \"verified_by\": \"claude-opus-5\",\n    \"verified_on\": \"2026-09-13\",\n    \"entries\": [entry],\n}\n\nwith io.open(\"/home/sfmqrb/git/rishe/data/verification/page-454.json\", \"w\", encoding=\"utf-8\") as f:\n    json.dump(doc, f, ensure_ascii=False, indent=1)\n    f.write(\"\\n\")\nprint(\"written\", len(nodes), \"nodes\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-454.py",
 "description": "Build page-454.json"
}
```


### [2026-09-14T02:18:35.489Z] TOOL RESULT

```
written 20 nodes
```


## [2026-09-14T02:18:39.887Z] TOOL CALL #88: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-454.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 454",
 "description": "Validate and run verify_check"
}
```


### [2026-09-14T02:18:41.095Z] TOOL RESULT

```
JSON OK
nodes verified: 20/20
node verdicts: {'plausible': 8, 'confirmed': 9, 'transcription_suspect': 1, 'disputed': 2}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 18, 'partial': 10, 'not_checked': 2}
books consulted: {'supports': 39, 'silent': 6, 'contradicts': 2, 'partial': 7} | by book: {'KLN': 8, 'AHD': 7, 'WLD': 5, 'KNT': 4, 'LAT': 4, 'SKT': 4, 'PHD': 3, 'BQT': 3, 'POK': 3, 'IEC': 2, 'NYB': 2, 'FSD': 2, 'MON': 2, 'SYN': 1, 'HUB': 1, 'HRN': 1, 'ARY': 1, 'BRT': 1}
```


## [2026-09-14T02:18:46.285Z] TOOL CALL #89: Bash

```json
{
 "command": "head -c 3 data/verification/page-454.json | xxd | head -1; python3 -c \"\nimport json;d=json.load(open('data/verification/page-454.json'))\ne=d['entries'][0]\nprint(e['root'], e['verdict'], len(e['nodes']))\nn=[x for x in e['nodes'] if x['id']==6][0]\nprint(n['error_in'], n['book_prints'], n['correct_form'])\nprint(all(x.get('derivation_fa') for x in e['nodes']), bool(e.get('note_fa')))\n\"",
 "description": "Final sanity check"
}
```


### [2026-09-14T02:18:47.603Z] TOOL RESULT

```
00000000: 7b0a 20                                  {. 
Sker 1 confirmed 20
book koeônos korōnós (κορωνός)
True True
```


## [2026-09-14T02:19:07.955Z] AGENT

Page 454 (book p. 424) verified. One chart only — `Skep` and `Sker 2` are redirects and were skipped.

**Counts** — root: 1 confirmed. Nodes (20/20): 9 confirmed, 8 plausible, 2 disputed, 1 transcription_suspect. Ref checks: 18 supports, 10 partial, 2 not_checked. 0 PROBLEM lines.

**Disputed**
- `#9 Old Persian Kŭru "curly hair"` — forms (Kūru-, Kūruš, gen. Kūrauš, Elam. Ku-raš, Bab. Ku-ra-aš) are exact and come straight from Moʿin's aʿlām entry کوروش, which cites Kent p. 180. But Kent files Kūru- under §164.V "Uncertain names"; Schmitt (Iranica) calls the etymology disputed and prefers Hoffmann's "humiliator of the enemy"; Harmatta "young", Tavernier Elamite. "Curly hair" rests only on FAF:513 (not digitised anywhere).
- `#10 Persian Kŭrosh "sun"` — the "sun" gloss is Ctesias/Plutarch, taken by Nourai from Funk & Wagnalls' "[Per., the sun.]"; rejected by modern scholarship and phonetically impossible (hvar- → xor, not kur-). Also the modern name is a post-decipherment restoration, not an inherited form.

**transcription_suspect**
- `#6 Greek "koeônos"` → `error_in: book`. No such Greek word; it is κορωνός korōnós "curved" (POK 935, WP II 568, Watkins sker-3 §10). I rendered pdf p. 454 at 300 dpi — the printed page itself reads "koeônos", so the extraction is faithful and the misprint is Nourai's. Page image saved to `data/verification/sources/refs/ocr/BOOK/454.png`.

**Other substantive findings (recorded as `plausible`)**
- `#3→#4`: the chain Pahlavi kanâr → Persian karân is inverted. MP has both karan and kanār (MacKenzie 49); NP karān continues karan directly, and کنار is the metathesized doublet (Hübschmann PSt. 267; Wiktionary s.v. کران/کنار). Mo'in's footnotes at BQT 1611 and 1699 and Horn p. 189 support the Avestan → Pahlavi part exactly as cited.
- `#2`: "Old Persian" label unsupported — Kent's lexicon has no karana-; and Buck, at the cited p. 857, writes "etym.?", while Pokorny/WP list only Av. skarəna- "round" under this root.
- `#8 *Kur-wo`: Mann says flatly "(kuruos 'bent, round'. Assumed for Latin only)"; krikos, crista, crispus, *hringaz, *hrugjaz all come from other extensions in Nourai's own sources.
- `#19 hrugjaz : edge` — gloss wrong; it means "back, spine, ridge" (Pokorny, Watkins, Wiktionary).
- `#20 ribbon` — not in Watkins; supported only by Klein (MDu ringhband), called "unknown origin" by Etymonline.

**For the owner (extraction, not verdicts)**: the printed page has an **empty box** to the right of `a-karana : endless ☞Ne 1` (an arrow leading to a blank node) that has no counterpart in `data/extracted/batch/page-454.json`. Everything else in the JSON matches the printed page verbatim, including "koeônos" and "Kŭrauš" (the latter is a genuine OP genitive singular, not an error).
