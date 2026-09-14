# Verification process log — verify-page-392


## [2026-09-14T00:49:35.658Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 392 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-392.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-392.json. Write /home/sfmqrb/git/rishe/data/verification/page-392.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 392` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-14T00:49:36.660Z] AGENT

I'll start by reading the instructions.


## [2026-09-14T00:49:37.433Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-14T00:49:37.466Z] TOOL RESULT

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


## [2026-09-14T00:49:37.935Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-392.txt"
}
```


### [2026-09-14T00:49:37.947Z] TOOL RESULT

```
1	=== PDF page 392 (book page 362) ===
2	--- entry 0 ---
3	ROOT Pend -> redirect to Spen
4	--- entry 1 ---
5	ROOT [Indo-European] Penkwe : five  (refs POK:808)
6	#1 (parent #0) [Avestan] refs=POK:808 | panca : five ; pancâsas : fifty
7	  #2 (parent #1) [Sogdian] refs=SOD:276 | pncw, pnz, pnc : five ; pnc`s : fifty
8	  #3 (parent #1) [Persian] refs=BQT:419; MON | panj «پنج» : five ; panjeh «پنجه» : hand (five fingers) ; pânzdah «پانزده» : fifteen ☞Dekm ; pânsad «پانصد» : five hundred ☞Dekm | extra: پنجگان ، پنجمین ، پنجم ، پنجاب
9	پنجک ، پنجول
10	#4 (parent #0) [Sanskrit] refs=AHD | panca : five
11	  #5 (parent #4) [English] refs=AHD | punch : drink ; Punjab ☞Ab 1
12	    #6 (parent #5) [Persian] refs=MON:822 | pânč «پانچ» : a drink made of several (five) fruits | extra: پُنچ
13	#7 (parent #0) [Germanic] refs=AHD | finfi : five ; fingwraz : one of the five, finger ; funh-stiz : five fingers, fist
14	  #8 (parent #7) [English] refs=AHD | five, fifty, fifteen ; finger ; fist
15	#9 (parent #0) [Greek] refs=AHD | pente : five
16	  #10 (parent #9) [English] refs=AHD | penta-, pentagon
17	--- entry 2 ---
18	ROOT [Indo-European] Pent : to go, pass  (refs POK:808)
19	#1 (parent #0) [Avestan / Old Persian] refs=POK:808; KNT:195 | pant, panta, path, pathi, pathâ : way, path, advice
20	  #2 (parent #1) [Persian] refs=BQT:422 | pand «پند» : advice
21	  #3 (parent #1) [Scythian] refs=AHD:1533 | 
22	    #4 (parent #3) [Germanic] refs=AHD:1533; KLN:1139 | patha : way
23	      #5 (parent #4) [English] refs=None | path
24	#6 (parent #0) [Germanic] refs=AHD | finthan : to discover
25	  #7 (parent #6) [English] refs=None | find
26	#8 (parent #0) [Latin] refs=AHD | pont : bridge, path over water
27	  #9 (parent #8) [English] refs=None | pontoon
28	#10 (parent #0) [Russian] refs=AHD | put : way
29	  #11 (parent #10) [English] refs=None | Sputnik
30	
```


## [2026-09-14T00:49:41.534Z] TOOL CALL #3: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/extracted/batch/page-392.json'))\nprint(json.dumps(d,ensure_ascii=False,indent=1)[:6000])\n\"",
 "description": "Print source JSON for page 392"
}
```


### [2026-09-14T00:49:42.635Z] TOOL RESULT

```
{
 "pdf_page": 392,
 "book_page": 362,
 "entries": [
  {
   "root": {
    "name": "Pend",
    "redirect": "Spen"
   },
   "nodes": []
  },
  {
   "root": {
    "name": "Penkwe",
    "lang": "Indo-European",
    "refs": "POK:808",
    "gloss": "five"
   },
   "nodes": [
    {
     "id": 1,
     "parent": 0,
     "lang": "Avestan",
     "refs": "POK:808",
     "words": [
      {
       "translit": "panca",
       "gloss": "five",
       "script": null
      },
      {
       "translit": "pancâsas",
       "gloss": "fifty",
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
     "lang": "Sogdian",
     "refs": "SOD:276",
     "words": [
      {
       "translit": "pncw, pnz, pnc",
       "gloss": "five",
       "script": null
      },
      {
       "translit": "pnc`s",
       "gloss": "fifty",
       "script": null
      }
     ],
     "script_extra": null,
     "note": null,
     "quote": null
    },
    {
     "id": 3,
     "parent": 1,
     "lang": "Persian",
     "refs": "BQT:419; MON",
     "words": [
      {
       "translit": "panj",
       "gloss": "five",
       "script": "پنج"
      },
      {
       "translit": "panjeh",
       "gloss": "hand (five fingers)",
       "script": "پنجه"
      },
      {
       "translit": "pânzdah",
       "gloss": "fifteen",
       "script": "پانزده",
       "see": [
        "Dekm"
       ]
      },
      {
       "translit": "pânsad",
       "gloss": "five hundred",
       "script": "پانصد",
       "see": [
        "Dekm"
       ]
      }
     ],
     "script_extra": "پنجگان ، پنجمین ، پنجم ، پنجاب\nپنجک ، پنجول",
     "note": null,
     "quote": null
    },
    {
     "id": 4,
     "parent": 0,
     "lang": "Sanskrit",
     "refs": "AHD",
     "words": [
      {
       "translit": "panca",
       "gloss": "five",
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
     "lang": "English",
     "refs": "AHD",
     "words": [
      {
       "translit": "punch",
       "gloss": "drink",
       "script": null
      },
      {
       "translit": "Punjab",
       "gloss": null,
       "script": null,
       "see": [
        "Ab 1"
       ]
      }
     ],
     "script_extra": null,
     "note": null,
     "quote": null
    },
    {
     "id": 6,
     "parent": 5,
     "lang": "Persian",
     "refs": "MON:822",
     "words": [
      {
       "translit": "pânč",
       "gloss": "a drink made of several (five) fruits",
       "script": "پانچ"
      }
     ],
     "script_extra": "پُنچ",
     "note": null,
     "quote": null
    },
    {
     "id": 7,
     "parent": 0,
     "lang": "Germanic",
     "refs": "AHD",
     "words": [
      {
       "translit": "finfi",
       "gloss": "five",
       "script": null
      },
      {
       "translit": "fingwraz",
       "gloss": "one of the five, finger",
       "script": null
      },
      {
       "translit": "funh-stiz",
       "gloss": "five fingers, fist",
       "script": null
      }
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
      {
       "translit": "five, fifty, fifteen",
       "gloss": null,
       "script": null
      },
      {
       "translit": "finger",
       "gloss": null,
       "script": null
      },
      {
       "translit": "fist",
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
     "lang": "Greek",
     "refs": "AHD",
     "words": [
      {
       "translit": "pente",
       "gloss": "five",
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
     "lang": "English",
     "refs": "AHD",
     "words": [
      {
       "translit": "penta-, pentagon",
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
    "name": "Pent",
    "lang": "Indo-European",
    "refs": "POK:808",
    "gloss": "to go, pass"
   },
   "nodes": [
    {
     "id": 1,
     "parent": 0,
     "lang": "Avestan / Old Persian",
     "refs": "POK:808; KNT:195",
     "words": [
      {
       "translit": "pant, panta, path, pathi, pathâ",
       "gloss": "way, path, advice",
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
     "refs": "BQT:422",
     "words": [
      {
       "translit": "pand",
       "gloss": "advice",
       "script": "پند"
      }
     ],
     "script_extra": null,
     "note": null,
     "quote": {
      "text": "دندانهٔ هر قصری پندی دهدت نو نو - پند سر دندانه بشنو زبن دندان",
      "poet": "Khâqânî"
     }
    },
    {
     "id": 3,
     "parent": 1,
     "lang": "Scythian",
     "refs": "AHD:1533",
     "words": [],
     "script_extra": null,
     "note": null,
     "quote": null
    },
    {
     "id": 4,
     "parent": 3,
     "lang": "Germanic",
     "refs": "AHD:1533; KLN:1139",
     "words": [
      {
       "translit": "patha",
       "gloss": "way",
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
     "lang": "English",
     "refs": null,
     "words": [
      {
       "translit": "path",
       "gloss": null,
       "script": null
      }
     ],
     "script_extra": null,
     "note": null,
     "quote": null
    },
    {
     "id": 6,
     "parent": 0,
     "lang": "Germanic",
     "refs": "AHD",
     "words": [
      {
       "translit": "finthan",
       "gloss": "to discover",
       "script": null
      }
     ],
     "script_e
```


## [2026-09-14T00:49:43.986Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','SOD','BQT','MON','AHD','KNT','KLN','HRN','HUB','PHD','NYB','WLD','IEC','SYN','BRT','ARY','SKT','FSD','WEB','CHEUNG']:\n    v=d.get(k)\n    print(k, json.dumps(v,ensure_ascii=False)[:400])\n\"",
 "description": "Show relevant reference entries"
}
```


### [2026-09-14T00:49:45.064Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in 
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "loca
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verific
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sou
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-D
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-di
CHEUNG null
```


## [2026-09-14T00:50:01.630Z] TOOL CALL #5: Bash

```json
{
 "command": "sed -n '/\"id\": 6/,$p' data/extracted/batch/page-392.json | python3 -c \"import sys;print(sys.stdin.read())\" | tail -120; echo ===; ls data/verification/sources/refs/ | head -60"
}
```


## [2026-09-14T00:50:02.223Z] TOOL CALL #6: Bash

```json
{
 "command": "sed -n '1,80p' data/verification/sources/SOURCE_MATRIX.md"
}
```


### [2026-09-14T00:50:02.613Z] TOOL RESULT

```
Exit code 1
            {"translit": "pand", "gloss": "advice", "script": "پند"}
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "دندانهٔ هر قصری پندی دهدت نو نو - پند سر دندانه بشنو زبن دندان",
            "poet": "Khâqânî"
          }
        },
        {
          "id": 3,
          "parent": 1,
          "lang": "Scythian",
          "refs": "AHD:1533",
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Germanic",
          "refs": "AHD:1533; KLN:1139",
          "words": [
            {"translit": "patha", "gloss": "way", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "path", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "finthan", "gloss": "to discover", "script": null}
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
            {"translit": "find", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "pont", "gloss": "bridge, path over water", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "pontoon", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 0,
          "lang": "Russian",
          "refs": "AHD",
          "words": [
            {"translit": "put", "gloss": "way", "script": null}
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
            {"translit": "Sputnik", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    }
  ]
}

(eval):1: == not found
```


### [2026-09-14T00:50:03.011Z] TOOL RESULT

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
```


## [2026-09-14T00:50:07.086Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"penk\" POK_full.txt | head -20\necho \"=== pent\"\ngrep -n \"^pent-\\|pent-, pont-\\|pent-,pont\" POK_full.txt | head -20"
}
```


### [2026-09-14T00:50:07.161Z] TOOL RESULT

```
66156:Root / lemma: penk^e 
66177:D. ordinals penk'ios:0\6 Indie paktiia-, Avestan pux5a- (after *kturtiia " the fourth ', 
66182:Lithuanian penktas. Old Bulgarian p§tb, Tocharian A pant, B pinkce; *penk''etos:0\6 Indie 
66190:*penk"'rds). 
66242:Irish e/ic/7e "salmon' {*penk-TnJo-); zero grade -/^/^oderivative *furjxW)3-'\r\ Old High 
68601:Note: Obviously Root/ lemma: ppksti-i\s\! derived from penk^eixve (fingers)' 
68605:See also: to Germanic farjxan {pak- and pag-, S. 788) or to penk^e^\\ynf . 
76698:armor', y05/77s^-/rJ/a-"Lumpenkleid the buddhist. Monche'; 
=== pent
```


## [2026-09-14T00:50:08.505Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -i \"penkwe\\|pen-kwe\\|five\" AHD_watkins1985.txt | head -20\necho \"=== pent\"\ngrep -n -i \"^pent-\\|pent- To tread\\|To tread, go\" AHD_watkins1985.txt | head -20"
}
```


### [2026-09-14T00:50:08.588Z] TOOL RESULT

```
50:Jones was content with the assertion of a common original language, without exploring the details. Others took up the cause, notably the German philosopher Friedrich von Schle- gel, to whom is principally due the popular diffusion of the long-lived misconception that the European languages were in some sense derived from Sanskrit. But it remained for another German, Franz Bopp, to found the new science of comparative grammar, with the publication in 1816 of his work On the conjugational system of the Sanskrit lan- guage, in comparison with that of the Greek, Latin, Persian, and Germanic languages. He was twenty-five when it appeared.
92:With the exception of the numbers five to ten and a group of particles including certain conjunctions and quasi-adverbial forms, all Indo-European words underwent inflection. The structure of all inflected words, regard- less of part of speech, was the same: root plus one or more suffixes plus ending. Thus the
834:*pld-ru- in Germanic *fléruz, floor, in Old English flor, floor: FLOOR; b. suffixed form *p/d-no- in Latin planus, flat, level, even, plain, clear: LLANO, PIANO?, PLAIN, PLANARIAN, PLANE!, PLANE2, PLANE, PLANISH, PLANO-, PLANULA; AIRPLANE, EXPLAIN. 4. Suffixed zero-grade form *pb-ma in Latin palma (< *palama), palm of the hand: PALM!, PALM2. 5. Possibly extended variant form *plan- in: a. Greek planasthai, to wander (< “to spread out”): PLANET; APLANATIC; b. possibly Germanic *flan- in Old Norse flana, to wander aimlessly, akin to the Germanic source of French fléner, to walk the streets idly: FLANEUR. 6. Suffixed zero-grade form *pl-dh- in Greek plassein (< *plath-yein), to mold, “spread out”: -PLASIA, PLASMA, -PLAST, PLASTER, PLASTIC, PLASTID, -PLASTY; DYSPLASIA, METAPLASM, (TOXOPLASMA). 7. O-grade form *pols- in: a. Russian polyi, open: POLYN- Ya; b. Slavic polje, broad flat land, field, in Polish Polak, Pole: PoLACK, POLKA. See also extensions plak-' and plat-. [Pok. pels- 805.] pele-%, Citadel, fortified high place. Greek polis, city: POLICE, (POLICY!), POLIS, POLITIC, (POLITY); ACROPOLIS, COSMOPOLITE, MEGALOPOLIS, METROPOLIS, NECROPOLIS, POLICLINIC, PROPOLIS. [In Pok. 1. pel- 798.] pelis-. Also pels-. Rock, cliff. Germanic *felzam, rock, in Old Norse fjall, fell, rock, barren plateau: FJELD. [Pok. peli-s- 807.] pen-. Swamp. Suffixed o-grade form *pon-yo- in Ger- manic *fanjam, swamp, marsh, in Old English fenn, marsh: FEN. [Pok. 2. pen- 807.] penkve. Five. I. Basic form *penke. 1. Assimilated form *pempe in Germanic *fimf in: a. Old English fif, five: FIVE; b. Old High German finf, funf, five: FIN2. 2. Ger- manic compound “*fimftehun, fifteen (*tehun, ten; see dekm), in: a. Old English fifténe, fifteen: FIFTEEN; b. Old Norse fimmtdn, fifteen: FEMTO-. 3. Assimilated form *kvenke in: a. Latin quinque, five: CINQUAIN, CINQUE, QUINQUE-; CINQUEFOIL, QUINCUNX; b. Latin distributive quini, five each: KENO, QUINATE; C. Latin compound quindecim, fifteen (decem, ten; see dekm): QUINDECENNIAL. 4. Greek pente, five: PENTA-, PENTAD; PENTACLE, PENTADACTYL, PENTAGON, PENTAMETER, PENTARCHY, PENTASTICH, PENTATEUCH, PENTATHLON. 5. Sanskrit pavica, five: PUNCH’; PACHISI. II. Compound *penke-(d)konta, “five tens,” fifty (*-(d)konta, group of ten; see dekm). 1. Latin quinqudginta, fifty: QUINQUA- GENARIAN, QUINQUAGESIMA. 2. Greek pentékonta, fifty: Pentecost. III. Ordinal adjective *penk-to-. 1. Ger- manic “fimftdn- in Old English fifta, fifth: FIFTH. 2. Latin quintus (< *quinc-tos), feminine quinta, fifth: QUINT!, QUINTAIN, QUINTET, QUINTILE; QUINTESSENCE, QUINTILLION, QUINTUPLE. IV. Suffixed form *penkv-ro- in Germanic *fingwraz, finger (< “one of five”), in Old English finger, finger: FINGER. V. Suffixed reduced zero-grade form *pnk-sti- in Germanic *fii(nh)stiz in: a. Old English fyst, fist: Fist; b. Dutch vuist, fist: FOIST. [Pok. penkve 808, pnksti- 839.] pent-. To tread, go. 1. Germanic *finthan, to come upon, discover, in Old English findan, to find: FIND. 2. Suffixed o-grade form *pont-i- in: a. Latin pdns (stem pont-), bridge (earliest meaning, “way, passage,” preserved in the priestly title pontifex, “he who prepares the way”; -fex, maker; see dhé-1): PONS, PONTIFEX, PONTIFF, PON- TINE, PONTOON, PUNT}; (TRANSPONTINE); b. Russian put’, path, way, in sputnik, fellow traveler: SPUTNIK. 3. Zero-grade form *pnt- in Greek patein, to tread, walk: PERIPATETIC. 4. Suffixed zero-grade form *pnt-o- in Iranian *path-, probably borrowed (? via Scythian) into Germanic as *patha-, way, path, in: a. Old English peth, path: paTH; b. Middle Dutch pad, way, path: FOOTPAD. [Pok. pent- 808.] per’. Base of prepositions and preverbs with the basic meanings of “forward,” “through,” and a wide range of extended senses such as “in front of,” “before,” “early,” “first,” “chief,” “toward,” “against,” “near,” “at,”
1360:CINCH kenk-1 CINCTURE kenk-1 CINDER sendhro- CINEMATOGRAPH kei-3 CINEMATORADIOGRAPHY kei-3 CINERARIUM keni- CINEREOUS_ keni- CINGULUM_ kenk-1 CINQUAIN penkWe CINQUE penkWe CINQUEFOIL bhel-3, penkwe cIRcA sker-3 CIRCADIAN deiw- CIRCLE sker-3 CIRCUIT ei-1 CIRCUM-  sker-3 CIRCUMCISE kae-id- CIRCUMDUCTION deuk- CIRCUMFUSE gheu- CIRCUMLOCUTION  tolkw- CIRCUMSCRIBE skribh- CIRCUMSPECT spek- CIRCUMSTANCE sta- CIRCUMVENT gWa- CIRCUMVOLVE wel-3 cIs- ko-
1505:FEIGN dheigh- FEINT dheigh- FEIST pezd- FELDSPAR pele-2 FELICIFIC dhé(i)- FELICITATE dhé(i)- FELICITY dhé(i)- FELL! p(h)ol- FELL? pel-4 FELLATIO dhé(i)- FELLOW legh-, peku- FELO-DE-SE s(w)e- FELON2 ghel-2 FELT! pel-6 FEMALE dh@(i)- FEMININE dhé(i)- FEMTO- penkwe FEN pen-
1509:FicHu dhig¥- FICKLE pelg-2 FICTILE dheigh- FicTION dheigh- -FID_ bheid- FIDELITY bheidh- FIDUCIAL  bheidh- FIDUCIARY bheidh- FIELD pele-2 FIELDFARE wer-4 FIEND pé@(i)- FIERCE ghwer- Fiesta dhés- FIFE pipp- FIFTEEN penkWe FIFTH penkwe FIGHT pek-2 FIGMENT dheigh- FIGURE dheigh- FILAMENT gWhi- FILAR gWhi- FILARIA gWhi- FILE! gWhi- FILE? peig-1 FILES pu-2 FILIAL dh@(i)- FILIATE dhé(i)- FILIBUSTER pri- FILIFORM gWhi- FILIGREE gre-no-, g¥hi- FILL pele-1 FILLET gWhi- FILLY pau-
1511:FIN2 penkwe FINCH sping- FIND pent- FINGER penkWe FINOCHIO dh@(i)- FIR. perku-
1515:FISH peisk- Fissi- bheid- FISSILE bheid- FISSION bheid- FISSURE bheid- FIST penkwe FIVE penkYe
1525:FOIL? bhel-3 FOISON gheu- FOIST penkwe
1711:KEEL’ gel-3 KEELHAUL kele-2 KEELSON ku- KEESHOND kwon- KEN gno- KENNEL! kwon- KENNING gno- KENO penkwe KENOSIS ken-4 KERATIN ker-! KERATO- ker-1 KERCHIEF kaput KERF gerbh- KERMES k*rmi- KERN! kat-2 KERNEL gre-no- KEVEL kleu-3 KEY? kagh-
2031:PACHISI penkwe, wikmti PACHYDERM bhengh- PACHYSANDRA bhengh- PACIFIC pag- PACIFY pag-
2075:PENNA pet- PENNATE pet- PENNON pet- PENOLOGY kvej-1 PENSILE (s)pen- PENSION! (S)pen- PENSIVE (s)pen- PENSTEMON sta- PENTA- penkWe PENTACLE penkwe PENTAD penkve PENTADACTYL penkve PENTAGON penkwe PENTAMETER penkwe PENTARCHY penkWe PENTASTICH penkwe PENTATEUCH dheugh-, penkwe PENTATHLON penkWe PENTECOST dekm, penkwe PENTHOUSE (Ss)pen- PENUCHE pa-
2154:QUINATE penkWe QUINCUNX  oi-no-, penkwe QUINDECENNIAL at-, penkWe QUINQUAGENARIAN penkWe QUINQUAGESIMA penkWe QUINQUE- penkWe QUINQUENNIUM at- QUINSY angh-, kwon- QUINT! penkve QUINTAIN penkwe QUINTESSENCE es-, penkwe QUINTET penkwe QUINTILE penkwe QUINTILLION penkwe QUINTUPLE penkwe, plek- QuIP k¥o-
=== pent
834:*pld-ru- in Germanic *fléruz, floor, in Old English flor, floor: FLOOR; b. suffixed form *p/d-no- in Latin planus, flat, level, even, plain, clear: LLANO, PIANO?, PLAIN, PLANARIAN, PLANE!, PLANE2, PLANE, PLANISH, PLANO-, PLANULA; AIRPLANE, EXPLAIN. 4. Suffixed zero-grade form *pb-ma in Latin palma (< *palama), palm of the hand: PALM!, PALM2. 5. Possibly extended variant form *plan- in: a. Greek planasthai, to wander (< “to spread out”): PLANET; APLANATIC; b. possibly Germanic *flan- in Old Norse flana, to wander aimlessly, akin to the Germanic source of French fléner, to walk the streets idly: FLANEUR. 6. Suffixed zero-grade form *pl-dh- in Greek plassein (< *plath-yein), to mold, “spread out”: -PLASIA, PLASMA, -PLAST, PLASTER, PLASTIC, PLASTID, -PLASTY; DYSPLASIA, METAPLASM, (TOXOPLASMA). 7. O-grade form *pols- in: a. Russian polyi, open: POLYN- Ya; b. Slavic polje, broad flat land, field, in Polish Polak, Pole: PoLACK, POLKA. See also extensions plak-' and plat-. [Pok. pels- 805.] pele-%, Citadel, fortified high place. Greek polis, city: POLICE, (POLICY!), POLIS, POLITIC, (POLITY); ACROPOLIS, COSMOPOLITE, MEGALOPOLIS, METROPOLIS, NECROPOLIS, POLICLINIC, PROPOLIS. [In Pok. 1. pel- 798.] pelis-. Also pels-. Rock, cliff. Germanic *felzam, rock, in Old Norse fjall, fell, rock, barren plateau: FJELD. [Pok. peli-s- 807.] pen-. Swamp. Suffixed o-grade form *pon-yo- in Ger- manic *fanjam, swamp, marsh, in Old English fenn, marsh: FEN. [Pok. 2. pen- 807.] penkve. Five. I. Basic form *penke. 1. Assimilated form *pempe in Germanic *fimf in: a. Old English fif, five: FIVE; b. Old High German finf, funf, five: FIN2. 2. Ger- manic compound “*fimftehun, fifteen (*tehun, ten; see dekm), in: a. Old English fifténe, fifteen: FIFTEEN; b. Old Norse fimmtdn, fifteen: FEMTO-. 3. Assimilated form *kvenke in: a. Latin quinque, five: CINQUAIN, CINQUE, QUINQUE-; CINQUEFOIL, QUINCUNX; b. Latin distributive quini, five each: KENO, QUINATE; C. Latin compound quindecim, fifteen (decem, ten; see dekm): QUINDECENNIAL. 4. Greek pente, five: PENTA-, PENTAD; PENTACLE, PENTADACTYL, PENTAGON, PENTAMETER, PENTARCHY, PENTASTICH, PENTATEUCH, PENTATHLON. 5. Sanskrit pavica, five: PUNCH’; PACHISI. II. Compound *penke-(d)konta, “five tens,” fifty (*-(d)konta, group of ten; see dekm). 1. Latin quinqudginta, fifty: QUINQUA- GENARIAN, QUINQUAGESIMA. 2. Greek pentékonta, fifty: Pentecost. III. Ordinal adjective *penk-to-. 1. Ger- manic “fimftdn- in Old English fifta, fifth: FIFTH. 2. Latin quintus (< *quinc-tos), feminine quinta, fifth: QUINT!, QUINTAIN, QUINTET, QUINTILE; QUINTESSENCE, QUINTILLION, QUINTUPLE. IV. Suffixed form *penkv-ro- in Germanic *fingwraz, finger (< “one of five”), in Old English finger, finger: FINGER. V. Suffixed reduced zero-grade form *pnk-sti- in Germanic *fii(nh)stiz in: a. Old English fyst, fist: Fist; b. Dutch vuist, fist: FOIST. [Pok. penkve 808, pnksti- 839.] pent-. To tread, go. 1. Germanic *finthan, to come upon, discover, in Old English findan, to find: FIND. 2. Suffixed o-grade form *pont-i- in: a. Latin pdns (stem pont-), bridge (earliest meaning, “way, passage,” preserved in the priestly title pontifex, “he who prepares the way”; -fex, maker; see dhé-1): PONS, PONTIFEX, PONTIFF, PON- TINE, PONTOON, PUNT}; (TRANSPONTINE); b. Russian put’, path, way, in sputnik, fellow traveler: SPUTNIK. 3. Zero-grade form *pnt- in Greek patein, to tread, walk: PERIPATETIC. 4. Suffixed zero-grade form *pnt-o- in Iranian *path-, probably borrowed (? via Scythian) into Germanic as *patha-, way, path, in: a. Old English peth, path: paTH; b. Middle Dutch pad, way, path: FOOTPAD. [Pok. pent- 808.] per’. Base of prepositions and preverbs with the basic meanings of “forward,” “through,” and a wide range of extended senses such as “in front of,” “before,” “early,” “first,” “chief,” “toward,” “against,” “near,” “at,”
```


## [2026-09-14T00:50:13.620Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '66150,66200p' POK_full.txt"
}
```


### [2026-09-14T00:50:13.666Z] TOOL RESULT

```
(Lex.) "house' ("Bretterbude'), Latin yC>^/yO//^/r7"Brettergerust as stage or Tribune'. 

References: WP. II 66. 

Page(s): 807 

Root / lemma: penk^e 
Meaning: five 

Material: A. Old Indie panca, Avestan panda; Armenian hing, gr. ttsvte, Aeolic -nt\mz\ 
nspna^siv "an den 5 Fingern zahlen' (: bret. pempat'd'\e Garben [to 5] fold, plait, fold up, 
merge '); alb. pese, Geg p§se {*perjk"tia)\ LaWnquFnque {Faiter quTn(c)tus), Oscan-Umbrian 
*yOO/r7yC>e (compare Oscan pumperias, Umbrian pumpenas 'quincuriae); Old Irish coic, 
acymr. pimp, mcymr. nc. pump, corn, pymp, bret. pemp, gall. nspnsSouAa "nsvracpuAAov'; 
Gothic fimf. Old Icelandic fimm. Old High German fimf, finf. Old Saxon Old English fff 
(schwab. fuchze 15 after sechze; das ^ these forms as well as Old High German funf, 
funfzich and of Ord. Old High German funfto point at not auf Indo Germanic n); Lithuanian 
pe/7/r/ (inflectional); Old Church Slavic yO^/i. 5 (/from /r/ after dem ordinals; originally 
collective = Old Indie /Oa/7/r//-"Funfzahr, Old Icelandic fimti. "number from fijnf; also 
Umbrian puntes if "quiniones'); Tocharian A pen, B pis, here.-Hittite pa"ta. 

B. 15: Old \n6\c parJca-dasaf, Avestan pancadasa, Armenian hnge-tasan, gr. 
n£VT£(Kai)5£Ka, Gothic fimftaihun. Old High German finfzeiian. 

C. 50: paHcasat, Avestan pancasat, Armenian yisun (from *iiingisun), gr. nsviriKOVTa, 
Latin quinquaginta {aiter quadraginta). Old Irish coTco {\n\Vc\ diphthong). 

D. ordinals penk'ios:0\6 Indie paktiia-, Avestan pux5a- (after *kturtiia " the fourth ', 
compare pai7/a/7Ka-"Funfter); gr. n£pnTO(;, Latin quTntus, Oscan *yC>c»/7/c»5 (compare above 
Puntiis, V\o\xu\zc„ Paelignian Ponties 'Quinctius'= Latin Quinctius, also Oscan pomptis 
"quinquies'; -/77- after dem Kardinale, as also das /7from Quinctius and quinctus); Old High 
German fimfto, finfto. Old Saxon fffto. Old Icelandic fim{m)ti, Gothic (in compound) fimfta-, 
Lithuanian penktas. Old Bulgarian p§tb, Tocharian A pant, B pinkce; *penk''etos:0\6 Indie 
pancattia- {qe^'6\\y\\\c\\ex pancama- aiiex saptama-), alb. ipesete, ipeste, gall, pinpetos. 
Old Irish coiced, acymr. pimpiiet eic; with A-forms Armenian iiinger-ord^\he fijnfte'; 



compare perhaps Old Irish co/cer' number from fijnf and Gothic f/ggrs, Old Icelandic f/ngr, 
Old English f/nger, Old High German Old Saxon f/'ngar l\r\ger' {*f/nj"'raz, Indo Germanic 
*penk"'rds). 

References: WP. II 25 f., WH. II 407 f., Trautmann 213 f. 
Page(s): 808 

Root / lemma: pen-1 

Meaning: to feed 

Material: Latin penus, -orisn. and penus, -usm. "Mundvorraf, also "the interior of Hauses'
```


## [2026-09-14T00:50:14.219Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"pent-\" POK_full.txt | head -30"
}
```


### [2026-09-14T00:50:14.270Z] TOOL RESULT

```
66250:Root / lemma: pent- 
85845:Old Irish /e'hot', PI. teit {* tepent- = Old Indie participle tapant-); ten and tene. Gen. -ed
```


## [2026-09-14T00:50:17.560Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '66250,66300p' POK_full.txt"
}
```


### [2026-09-14T00:50:17.639Z] TOOL RESULT

```
Root / lemma: pent- 

Meaning: to go, walk; way 

Note: (in Aryan with //?) 

Material: Old Indie panthah (= Avestan panti), Akk. Sg. pantham (= pantqm), and 

panthanam {= Avestan pantansm), Instr. Sg. patha{= pa^a); /-stem in Instr. PI. pathibhih 

(Avestan padsbTS), Old pers. Akk. Sg. pa^/'m; Avesian panta a\so 'room, place', as in 

ablaut. Old Indie /?a//7as-n. "plaee, homeland'; 

Armenian hun, Gen. /7/7/"ford, way' {*pont)\ 

Maybe alb. {*hu-) hynf enter ' 

gr. novTOc; m. "Meerespfad, sea', zero grade naroq m. " path, traek, step, tread; kiek, 
strike or blow delivered by the foot; footprint, traek ', naTSw 'trete'; anarau) ' deeeive ' 
(*aTTo-TTaTaoo 'bringe vom Wege ab'), anarn " deception, deceit'; 

Lithuanian pons, -//s'PriJgelweg through SiJmpfe, bridge'; yOO/T/z/feA-'Oberpriester', 
originally "BriJckenmacher'; 

Germanic *pal=>a-\v\ Old English psed^ path, track, way' (engl. path). Old High German 
Modern High German pfad 6er\yes probably from an Iran. Mundart, compare Avestan pa&- 



Gothic f/nf^anl'md, learn'. Old Icelandic f/nnads., (under the influence of common Celtic 
-ns-, -nt- > -nn-). Old English findan. Old Saxon fTthan and findan. Old High German 
findan, f/ntan stem V. 'find, learn, erfinden'; Old Saxon fath/n. "the going' {*fant^io-)\ Old 
High German fend(e)o^Vu^i^av\i^er\ Middle High German Ke/7o'e'Fuftganger, young lad, 
young boy'. Old English fedam. "troop, multitude, crowd, Fuftvolk' {*fant^jan-)\ Old High 
German fanddn= Old English fandian^ examine '; Middle High German vanden 
"besuchen'. Modern High German fahnden. Old Saxon fundon ' s\c\r\ aufmachen after, 
strive, go, hurry' = Old English fund/an ds., Old High German funden ds.. Old Icelandic 
fuss^ willing, inclined, willing'. Old Saxon Old English /Js "quick, fast, keen, eager, willing', 
Old High German /^/75 "willing, ready, willing' {*fund-sa-), Norwegian fJ55 "quick, fast run'; 

maybe alb. fus, M'insert, thrust in, plant, put in'. 

Old Church Slavic pgtb etc. m. "way' ( *pontis), zero grade Old Prussian pintisds. 



References: WP. II 26 f., WH. II 336 f., Trautmann 205 f.; Wackernagel KZ 55, 104 ff., Old 
Indie Gr. 3, 1,306f. 
Page(s): 808-809
```


## [2026-09-14T00:50:19.109Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KNT p195 pa0i / pathi\"; grep -n \"pathi\\|paθi\\|pa0i-\\|pathim\" KNT.txt | head -20"
}
```


### [2026-09-14T00:50:19.184Z] TOOL RESULT

```
=== KNT p195 pa0i / pathi
2145:III. It is not always possible to determine whether the feminine common nouns are -f- stems or -2- stems; etymological comparison is necessary The short vowel seems assured in aršti-, Skt. rstí- ‘spear’; palim, Skt. stem pathi- in some case-forms;
4188:DNd: Aspathines has a heavy bow, or a bowcase, slung over his left shoulder, and holds a battle-ax in his hand; ef. JNES 4.233.
4191:DNd: Aspathines, bowbearer, holds the battle-ax of Darius the King.
4859:Gaubaruva son of Mardunitya ^ Gobryas Vidarna son of Bagübigna Hydarnes Bagabuxsa son of Détuvahya ^ Megabyzus Ardumamé son of Vahauka Aspathines
5121:Aspacanah- sb. ‘Aspathines’, bow-bearer of Darius: Elam. a§-ba-za-na, Akk. as-pa-[si-nal, Gk. ‘Aoraftens; aspa- ‘horse’ (59.11, §9.n2, $90) + canah- ‘desire’, Av. -Cinah-, Skt. cénas-; ‘Lover of Horses’ (§161.[a, $168.10). Азрасапа пзш. (156.11, $185.11) DNd 1.
```


## [2026-09-14T00:50:26.986Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"‘way’\\|'way'\\|way, road\\|road’\" KNT.txt | head -30\necho \"--- pa entries\"\ngrep -n \"^pa[0θtb][a-z]*-\\? *sb\\.\\|pa0i-\\|paθi-\" KNT.txt | head -20"
}
```


### [2026-09-14T00:50:27.061Z] TOOL RESULT

```
--- pa entries
5632:patikara- sb. ‘picture, (sculptured) likeness’: .
```


## [2026-09-14T00:50:28.879Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '5620,5650p' KNT.txt"
}
```


### [2026-09-14T00:50:28.924Z] TOOL RESULT

```
paišiyā- sb. ‘script, written text’: deriv. of pai- (§89, §144.V). See also Parsiyduvada-. ри nsf. DB 4.91 (conj. of Kent, JAOS 62.268).
PaiSiyd'uvdda- sb. ‘Paishtyauvada’: АКК. pi- &-"-hu-ma-du. Perhaps, with Justi, IFA 17.107, ‘Pasargadae’, from paisiyd- ‘writing’ + "wüdá- ‘abode’ (572, §89, §126, $127, $142, §166, 5160.1): ‘Home of the Archives and Sacred Writings’ (on Pasargadae, ef. also Kónig, RuID 66; but Hz. ApI 275-6, modifying his view ш AMI 1.86n, takes prior element to be pati-, pati- becoming pa&-, with epenthesis; Bthl. AiW 907-8 normal- izes Piši- after the Akk., but gives no etymology). Paisiydwddim asf. DB 3.42. Parsilydluvadayd absf. DB 1.36f.
pa|camàm] adj. ‘fifth’, asf.: wrong restoration of Wb. at DB 5.8 (ef. Kent, JNES 2.109).
pal- vb. ‘fly’: Av. pat-aiti, Skt. pát-ati, Gk. vérerat, Lt. рені ‘seeks’, pIE *pet-.
ud- + pat- ‘rise up, rebel’ (cf. Ву. TPS 1945.64-
66): udapalatà imf. mid. (§84, 8213, 5285.П) DB 1.36, 38, 74, 78; 2.10, 14f; 3.24, 79.
patiy adv., prep., prefix ($140.I, $1911): Av. рай, Gk. (dial.) rori, pIE *poti, cf. pIE *proti in Skt. prát, Gk. Hom. троті, classical rpés (cf. Lg. 20.9-10).
(1) Adv. ‘thereto, again’: DB 2.37, 48, 57; 3.04, 71. pati-maty ($186) DNb 32f.  nai-pati-mà ($133, 5186) DNb 20. yadi-patiy (8136) DNa 38. (ya-patiy XPa 15; XPf 40f.
(2) Prep. (8271) with ace.: DB 52 ‘during’; DNb 22 ‘against? (Hz. ApI 273 reads par[slaiy ‘in court’, sb. to root fraé-); postposed DB 2.62 ‘on’. Encl., with ace. ‘during’ DB 1.20 (8133, $136); with inst. ‘near, at’ DB 2.16°, 3.26; with loc. ‘on, upon’ DB 2.76, 91; 3.52, 92. Ву. BSLP 42.2.70 takes all these as adverbs except DB 2.62, DNb 22.
(3) Prefix with verbs avahya-, ay-, ziay-, jan-, рӣ-, fraf-, d-bar-, zbü-; prior element in nouns palikara-, Patigraband-, perhaps Pátisuvari- and
"* 2 - -
also patiš, patisam.
patikara- sb. ‘picture, (sculptured) likeness’: .
РМ. patkar-, NPers. pátkür-;.pati- + kara- to root
as sata jeu iit И ЗАК
pores agent iain ee Seeman Re NE SS a cet ras ЧЕК ЧАС ve NEMPE
LEXICON 195
kar- ($143.V). patikaram asm. DSn 1°. palikara apm. DB 4.71, 78, 77; DNa 41.
Patigraband- sb. ‘Patigrabana’, a town in Parthia: Elam. pat-t-ig-rdb-ba-na; from pati- + root grab- + suffix (833, $103.IV, §147.1). Pati- graband nsf. DB 3.4f.
Я patipadam phrasal adv. ($191.17) ‘on its base, in its own place’: pati- ($186, $1401) + aec. padam (see pada-; 76.111, $122). DB 1.62.
palis prep. with acc. ‘against’: pati- + adv. -s, ef. Lt. ex, abs, ops- in os-lendó, sups- in sus-tined, Skt. nt and nis, Gk. ато iy, audi audis. See also patisam. DB 1.93; 2.33, 38, 43f, 52f, 58, 67; 3.36, 43, 65.
patisam adv. ‘in addition’: extension of patiš, ef. for formation Ose. per-um ‘without’ to (Lt.) per, and for meaning Gk. трд ё ‘and besides’, Lit. atque from *ad-que ‘and thereto’ (OP patiy, Gk. тро, Lt. ad agree in marking something as an ad- dition). patišam DB 4.89 (p* probable but not certain KT); (раат DB 4.90 (restoration of Konig, Klotho 4.45; see also Kent, JAOS 62.267- 8).
Pàtiwvari- adj. ‘Patischorian’ ($167): Elam. ba-ul-ti-i$-mar-ri4$, АКК. pa-id-di-if-hu-ri-i$, Gk. (рі) llaracxopes. Perhaps pAr. *pati-, with vriddhi ($126), + *suára- ‘(of the plain) before the Hvara Mts.’ ($117), with combination (8$140.VI) of sandhi forms (so Hz. ApI 183-4, who however disregards the d in the penult of the OP). Ран паті nsm. DNe 1.
. раві- sb. ‘path, way’ (676.1, §152.1, $179. III): Av. pab- patá-, Skt. panthan- path-. райт asf. DNa 58.
pad- sb. ‘foot’: Av. Skt. pad-, Gk. roô-, Lt. ped- ($142); in mipadiy, cf. also pada-, páda-, pasti-.
pada- sb. 'footing, step, station': Av. paóa- ‘foot (as measure)’, Skt. padd- ‘step, footstep, place’, Gk. aé&ov ‘ground’; extension of pad- ($143.- П). In Garmapada-, patipadam; see also pad-, рӣйо-.
рӣйа- sb. ‘foot’: LAv. páóa- ‘step, pace’, Skt. pida- ‘foot’, Gt. fotu-, extension of stem in pIE nom. *pdd-s, acc. *pod-m, seen in Gk. Dor. тах ($76.11, §122, $126, $148.П). Cf. also pad-, pada-. püdaibiyà idm. ($189) DNb 41.
par- vb. ‘communicate’: Av. *par- ‘hindureh-, hintibergehen’ (ВЕ. AYW 851), Gk. weipw ‘I pierce (as with a spit)’, Gt. faran ‘to travel’. рамо[т- іаїу| nsn. past pte. pass. ($242.1) DNb 54 (dubious con]. of Kent, Lg. 15.167, 178-4).
ipara- adj. ‘later’, possibly in hyáparam (q.v.) : Av. para- ‘farther’, Skt. pára- ‘distant’, Gk. qépav ‘beyond’.
nara prep. with acc. ‘beyond’ (§32, $63.1): Av. pard ‘before’, Skt. purds ‘before’, Gk. таро ‘before’; DPe 15; DPh 5; DH 4, See also para- dayadàm, paradraya.
parü postpos. with acc. ‘along’, and verbal prefix ‘forth’ ($132.3): Av. ?pará ‘before’, Skt. purá ‘before, formerly’, Gk. rapá ‘alongside’: in avapard and with ay-, ar-, gam-, bar-.
```


## [2026-09-14T00:50:37.702Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT panca\"; grep -n \"panca\\b\\|pañca\\|panca-\" BRT.txt | head -20\necho \"=== BRT pantan/panta\"; grep -n \"pantå\\|paṇtā\\|pantan\\|pantąm\\|paθ-\\|pantā\" BRT.txt | head -20"
}
```


### [2026-09-14T00:50:37.774Z] TOOL RESULT

```
=== BRT panca
2899:•  j.,  g.  'ao}ah-  n.  '(physische)  Kraft,  Stärke': asistim  narl  alaotw  °Jö  Y.  60. 3;  —yakmi niyne  nars  'Jartha  Y.  /o.  a ;  —  ai-avaia '}arfka  yaia  yal  panca  narS  "mit  solcher Kraft,  als  wären  es  fünf  Männer"  V.  jj. loPaZ.;  Yt,2.i2,  14;  —  usla  U yd  ä"j 'jaiika  vasöjciairä  ahi  haoma  Y.9.25; —  kacaiti  dim  aspahe  "Jö  uitrahe  °Jö vlrahe  °j<>  Yt.  it).(i&;  8.2^^;  —  "jö  tanvö vispaya  Yt/.^.29;  —  -jö  vJspdMnüM  Y. 5.17;  —  drfahela  paiti  °)arakö  Yt,  i_j. 134;  ~-  y~'  itfsfro)  arinam  ..  matilüm 'jö  abaraiii  \t  14.12;  —  apa  .  .  buei'ä- °}5  , .  barahi  apa  pä',ayä  sävar»  Yt.  10. 23;  62;  —  haomö  asibil  yöi  ..  zävari "jssca  baxhili  Y.  9. 22; —  °Jasca  nn- S«)Wf'a..Y.  77.8,  yi.j.22,y.i,Y.  72.6;  — yS  nü  asSif  °janAil  vandayaÜJ  (sd.)  ., gae^am  Y.50,3.  a)  AS.  °jö  als  Adv,
3455:atcit  . .  "wenn  auch  .  .,  so  doch  . ."  Yt s)  einen  selbständigen  Satz  ein- leitend, vor  Konj.,  unübersetzbar:  a/cTt aAmäi  .  .  ankaiti  Y.50.3.  3)  einen Satzteil  anschliessend;  a)  'und  zwar" :  panca- ahmi  .  .  ajcij  ahmäl  ya^a  .  .  av/ia^ niväitisisd.)^.  10.16.  b)  'aber':  agustJ (sd.)  . .  aäbyl  ySi  . .  atlu  a^bya  vakiltä  Y. 31.1.
4796:mit  avi  'herzugehen  zu  —  (Akk.),  (ihn)  an- kommen': nars  . .  panca.dasatfhs  . .  laaa ayaos  ya'ha  paeirlm  vtrsm  avi  ams  (sd.) flÄÄ'  YtÄi4.
5117:sükaya  (sd.)  bräZ3m  Yt  14.  33;  33;  — jainü  mqm  ahuna  vairya  "vata  snai>isa ya%a  asma  . .  YtZ/.ao;  P.22;  —  kthrpa 'vatS  (GS.)  *sraya  (sd.)  ya%a  dämqii sralstail'^.2.^;  —  ifkrpa  "vatqm  sraya ydka  di'iayatqm  zaosS  (sd.)  Yt  17. 1 1 ;  — st»r)naoili  aria  *°vat  starim  .  .  ya'ia  .  . P.25(?).  a)  substantivisch  'Wntum',  mit Gen.  part:  yat  mS  'va(  daüvayasnanqm ni/atitn  ydka  .  .  Yt  J.77;  —  upa  .  .  'vat siWi/  (sd.)  urva  *isaiti  yd^a  .  .  H.  2. 2.  b)  mit  Akk.  der  Beziehung:  andern .  .  y3  asti  'vaiti  masö  yd^a  vJspa  ima äpS  Y.  65. 3 ;  — yash  . .  "vant^m  (als  ASn.) mass  vikilnayät  ya'ia  hi  tanus  atphat  V. 7.51.  a)  mit  ya'i:a  yat  'wie  wenn,  als ob':  °vaia  aejanha  yd^a  yat  panca  narS "mit  solcher  Kraft,  als  ob  es  fiinf  Männer wären"  V.  75. 10  PiiZ.  2)  'dass':  asti  sl
8421:•  j.  upäzana-  n.  'was  Jemandem  als  Busse zudiktirt  wird,  körperliche  Abstrafung, Hieb':  ka  hs  asti  (li-al  .  .  panca  'na aspahe  aSttaya  panca  sraosJ.caranaya ".  .  fünf  Hiebe  mit  der  Pferdepeitsche, fünf  mit  dem  Zuchtriemen"  V. 4. 18;  18, 18  ("10,  15  Hiebe");  —  ^risat^m  'nanqm upäzsit  (sd.)  aspahe  astraya  'irisatim sraosS.caranaya  ". .  30  Hiebe  . ."  V.^.19; 19,  19.  19-20,11,  6.21,^.36,4.12,13, Mi  15.  J'37,  H--i  {dRn.  "50,  70,  90,  200,
8997:V.g.  54,  2)  'ob  wohl?',  frageeinleitend: "Ort  airyti  dairikävö  huyäiryh  öavänti  Yt 5.36,  3)  'wie?'(?)":  "<!«  ns'^  .  .  ioa agatJ  N .  ig.  ^i.  4)  'wie  lang?'  *k'^'> mii  uxsyäli  V'J*  mä  rum/saitit  panca.- dasa  mä  uxsyeiti  .  .  Yt.7. 2.
9201:•  j.  'kar-  V.  'einfurchen'.  Praes.  30  (Iter.)  wandeln':  panca.dasa  /ra/arSii^iiDPiiS..) kSraya'.  ^ptta  puiras'a  raor,aSh'a  kalarasät  Y. p. 5  ;
10318:•  j.  gäSS-  f.  'Lied'  uzw.  religiösen  Inhalts; 1)  insbes.  von  den  fünf  Hymnen,  bez. Hymnensammtungen,  die  in  Y.  28—34, 43—51,  59  erhalten  sind*':  sraobm  .  .  y5 paoiryd  "^.J  frasrävayatya panca  . .  zara- iu/traAe  *a/smaimvan  (sd.)  vacastastivaf malMzaintls  mal.paiti./rasä  Y.57,8;  7/. 6, G.  7.6;  —  akunavaitlm  (Stverz.)  °'i:qm aiaonlm  .  .  mai.afsmanam  mat.vaüäslallim map.äzaintim  matpjnsvlm  mat.paiti.p?r>s- Vlm  map  varfiibyjca  *pa^?byasca  kufra- mtrttqm  . .  küfrayaslqm  . .  Vr.  14.  o  f.;  usw.; — ahunafalca{^A.)  'Lariam  ^.46;  —  uita- vaitya  (Stverz.)  '"^aya  handatä  ya^amaide . .  haitiPca  afsmans^a  vacasca  vacaslal- llmca  /rasraa'knmca  ..'Vj.iS.y,  usw.;  — sp)ni:1.mainyBm  (Stverz.)  '"^qm  asaonzm  . . Vüiuxsa'irqm  (Stverz.)  '^qm  ..vaAisISistim (Stverz.)  'iqm\x.2.Zl;m-»i.  2)Bezeich- nung  für  alle  (anscheinend)**'  im  Gä^ä- dialekt  verfassten  Stücke  des  Awesta,  d.  s.  — ausser  den  eigentlichen  0<i>äs  —  AtxYHapt. und  die  vier  heiligen  Gebete  (V.  27. 13— 15, 54.  i  )'*'>;  nur  Plur-,  womit  entweder  die Gesammtheit  dieser  Li  tteratur  oder  einzelne Abschnitte  daraus  gemeint  sind  (s.  auch  A): imäsf  tg  haoma  °^ii  imä  h^nti  staomsyS'^. /0. 18;  — farS  amisä  sp>nta  ''ka  gJurvJin Y.2S.0;  —  tipma  vi  0(7  dcflö«/"/ Y.2(V.o, 430,  47-o,5io,S3°''  —  '"i'^byS  spintäbyd ratuxsa^räbyS  (Stverz.)  alaonibyö  Y.55.  i ; usw.;  —  tä  713  hmti  °äi7  har^'iravaitista
11187:•  j.  £a9Tu.piätra-  Adj.  'vier  Stände  ent- ' haltend,  umfassend'  '• :  aUaica  vacS . .  '^ri.-  i afsnum  (sd.)  'nm  panca.ralu  Y.  75.16.
13109:—  izitu/  nämä"  'Ayätts  a%uräyi^  Bh.2, 10.  11)  im  Atw.:  Uta  at^m  nijanäni RyaonXnqm  'hyunqm  pancasayriäi  .  .  Yt j?.  3 1 ;  —  Uta  azmt  fraourvaisayeni  kumaya (sd.)  *väri'ikanatn  hyaonya  (sd.)  haca 'itihävBiOß.  statt  AblS.)  Ytp.si  \~ydka aztm  nijanäni  tüiryanqm  'hyunqm  panca- saynäi  . .  Yl  5.  54;  /,?-'i43'.  V.J.  42  PüZ., 5. 38PÜZ.;  —  airyanqm*  'Ryunqm*  .. sairimanqm'  'hyunqm'  . .  säininqm'  'hyu- nqm' ..  dählnqm'  'hyunqm''  ..  Dlspanqm* 'hyunqm*  Yt  i^.  i43ff.;  —  kä'ia  airyi' -irihävö  huyäiryh  bat'inti  Yt  8.  36;  56, 58 j;  —  nsit  .  .  airyä  'itihävö  (als  AP.) Art/ (sd.)  hyäi  hama  Yt  8.  56;  —  mi^rtm .  .  huiayamm  atryäbyö  'i^hubyB  Yt.  fo.4;
14739:jAw.  allgemein:  zara%ustrahe  vanmmca 'simca  Y,  iG.  2 ;  —yävaranS  as  zara\ultr5 .  .  tä  var^näcä  'säcä  mazdayastiB  akmJ .^.12.^;  —  aparimla  'hm  yasamaide  "Atu zweiten  Teil'*  der  Glaubenslehre  . ."  G. 9.7,  a)mita^Ärij)'- Adj.  'die  aA«nsche, d.  i.  von  AA.  erteilte  Lehre,  Belehrung': ahairiS  frams  (sd.)  ,  .  ahairis  'sö  Y.  57. 24;  60.  3;  —  ähUirTm  frasmm  . .  ähüirlm •um  Y.  7/.  13;  Vr.  2. 1 1 ;  —  ahurBtl  f ras- nahe . .  sAurSi/  °idAe  Vi.  /.  9.  2)  'Einzel- lehre, Lehrsatz;  Dogma'J',  nur  jAw, ^rayff  •/«  Y.  20.  3,  2/.  2;  —  panca  'l Y.7p.i4;  —  aka  's"?m  *jray«/(  (Sp.  448  u.) Y.  20.  1;  —  vaaAiui  tha  hriilm Sdnnjayati  {sä..)  Y./^.  13.  3)  'richter-
14853:i)  'fliegen,  sich  im  Flug  stürzen  auf-'  v.j.  11.  2)  in  -/arischer  Art 'einher- {Jaiü  mit  Lok.):  kazanrim  iiunqm  .  .  gehen'<>:  yat  nä  \Jahika\  pasca  panca- mainyavasä  patinti  katiurile  patH  daeva-  1  jasTm  sarn^m  frapalaitii''  anaiwyästa (ad.) t1qmYt.10.119.  2) 'fallen,  hinabstUrzenlj,^  anabdäts  vä  "wenn  ein  Mann  [ein (s.  auch  4):  pairikä  .  .  yü  starö  hnma  Weib]  nach  (vollendetem)  fünfzehnten  Jahr (sd.)  patmOi  aniar»  tarn  asmammca   Yt  !  ^\^Yia  geht  ohne  .  ."  V.  18.  54.  3)  in
15262:j.  pan^-sant- *>  fem.  Zw.  'fünfzig': paitica  hl  anya  dva  vä  nara  anhiti  panca vü  'sahm  (als  Nom.)''  va  V.  5.  27;  — aivam  va  avi  x^apamm  duyS  pJ  'satim (als'Akk.)')  va  YtÄii.  a)  mit  Gen.: ^  pasca  'satitn  sar^qm  V.  7,  48;  —  'sat»m \iitr?.saokanqm  V.S.gx;  4, 19',  6'.  13',  12.9, F. /o.  a)  adjekt  gebraucht:  ha^ra.. ^yazataiibyS  . .  'satblsca  sataista  . .  Vr.  Ä  i, I  KompA. ;  Ableit  —  ai.  fonoiiäl-  f.,  np. /on- I  jäh  i).  —  Pü.  i  SO.  —  »  Mit  fl  lu  F.  und  Vr. —  ')  Vgl.  lu  %titanl:  —  3)  S  ^ro  udW.
16985:—  sraostm  . ,  yS  paoirys  'ma  frastn-mata %ryaxstlli!a  panca.yaxltT^a  Aapta.yaxällca nava.yaxitii^a  ox^nosca  mathydi.patti^tä- nasca  Y.5J.6; — yaj  'ma  a^.dräjS yave.- frä^S  .  .  yat  masyS  aBakmät  °ma  N.  70;
18672:3  airySma  (sd.)  .  .  jantü  mnbyasiä HäiribyascS  zara%uslrakl  Y.54.  i;  FrW. i.\;  —  narasca  *tiairTsla  Vyt.30;  — rtaram  näirinamca  V,  2.  27,  30;  8.  12,13, Vd.3,  Y.(?Än*;  —  in  Verbindung  mit alavan-  (s.  auch  Sp.  1050  o.):  aiaunqm .  .  urunS  .  .  kiidö.taianqmltt  narqmcä näirinqmlä  Y.J9.2;  J7-3,  -i'.?,  8,  10, Yz.iS.  2,Yt./j,  143-145^  A)näirika-. nar 3m  vä  *nSirikqm  vä  FrB.;  Az.  I,  Vyt. /,  Vd.  7j,  Nik-i-j^;  —  hala  nä  (statt Abi.)  paiti.irisi5  haca  näirika  paitiSriste V,  iO.  s ;  —  in  Verbindung  mit  aSavan- (s.  auch  Sp.  1050  o.):  nanm  asavamm .  .  näiriiqm  asaonim  V.p,33,  42,  ig.  12, 26,  71.1,  3,  7,  10  (statt  Abi.);  Vr.^.  4, G.4.9.  a)  jahikä-:  narS  (tiS.)''>  pai- ristä.xsu%rS  . .  Jahika  paraJax^ta  Yt  J7. 54.  f)  vantav-:  yaisa  nä  fryS  fryäi vantaoe{sA.)  ..  pu%r»m  ..  avi  avii.baraili ^- 3-  *S-  g)  pu'^ra-.  nanm  vä  .. puhnm  vä  FrB.;  Az.  /,  Vyt  7,  Nik. I.  h),  i)  aptnnäyBka-,  kainikä-:  na- ramHa  .  .  apmnäyükanamca  kainika- nqm!a  Y.  68.12;  26.  8 f.'  2)  sonst: nar/^  k?hrpa  panca.dasanlüs  YtÄi3, i4~^T,  Vdiy;  —  niUmactt  ..  stärqm {sA)  ya%a  nars  matmyehe  v(r/han>m    F.
18701:Aus  dem  Zusammenhang  gerissene,  un- deudiche,  verderbte  oder  wertlose  Stellen mit  nar-.  «flr/(GS.)  ..  nara  (ND.)  .. «(jr?(NP.)  F.  2e;  —  «3  Fsd;  — nanm ..sar>t)m  V.^.  14  PüZ'J»;  N.52"';  — panca  narB  V.  75.  loPüZ.;  Vyt.  42,  Vd 13,15;  —  dva  nar^FiB.; — para  "iafah- mät(sd.)  n»r>t  (AblS.)  V.  j.  42  PÜZ.;  — aBsqmia  naram  V.  5.  gPUZ.;  —  ham.- tapiibyB  aiwys  caxrart  (sd)  n^r^byB  V. 4. 4  7 ;  I  o  PiiZ. ;  —  tl  ^narsS paitismarmitm Vy^  52;  —  nöil  dim  "nara  . .  avasyil  Yt /.  aS;  — ya'ia  na  ttäifyaY.  20.  2;  Yyt  28, 30.  narSm  nartm  als  Adv.  sbes.  [N. 301  streiche  «a.J
21386:gleicher  Bedeutung  auch  ohne  kapf**'*: *srao%ra  *nä  gä^anqm  ratufrU  paiti.- asti(sii.)ca  'nake*aoa  fs'BfS  mq%rahe^.22-, 22  2.  St.  (s.  gleich);  —  vlspaZcS  panca gä'hä  . .  vispfmca  'mm  Y.  77. 6 ;  ^  in  Ver- bindung mit  dem  V.  yaz-  'den  YH.  beten': gä%ä  srävayS  'mm  yazmttm  paitistäiH (sd.)  vTspanqm  \_ga%anqm\  ratufris  -n^m *yazäiti  gä'hanqm  srävayamnanqm  paitiM (sd.)  'nake  a?t/ake(sd.)  ratufris  aratufris gä'i:anqm  "(wer)  die  G.s  au&agend  einem zur  Seite  steht,  der  den  Y.  betet,  ist  für alles  r. ;  (wer)  den  K  betet,  indem  er  sich zur  Seite  stellt,  wo  die  G.s  aufgesagt  werden, ist  nur  für  den  Y.  r.  .."  N.22; — yffi  hl.. frasräTOyamnakei^A.)  vä  upa.srunvanii*yai 1  ^yazimnahe  N.  20;  24.  B)  mit
22362:fraoxtö  .  .  spanvanii  H. ;.  4;  —  yasca  .  . imat  uxtpm  'tB  fravaocat  YL 11. 4;  — ..  anye.**cäsca^^  */ramravainH gavSstryäfa vartinä  vjnunti  N.  ö'o;  —  imai  uxorm '^ /ramruyä  Yt.ii.6;  VyL  20,  22,  26,  28, 55;  —  aha  zl  mraot  akurS . .  zarähuftrSi raprhwinahe  ra%wö  uxb?m  'cB  A.  4-  3;  Yt J.  a ;  —  altalca  'cS  mazdaoxt»m  ^ri.a/itrDm iahrupistrim  panca.ratu  Y.  75. 16;  FrW. g.i;  —  vTspam  'cff  fravä&im  (sd.)  kaurum 'CS  ahurake  mazdä  Y.ig.14;  —  yesntm °lB  .  .  zarahusirahe  Y.  21.  1;  2;  —  _/9a staottm  'CS  yesnlm  , .  mrtgiä  FrW.  /.  i ;  — *kahmäi ..aivakmi  paiti  v^(LS.?)  vtspa- nqm  voAunqm  . .  fraväk^m  H.  /.  i ;  —  Aa druxs  avästryäte  kamcit  vä  'ÜanAqm  V. 5.  13;  —  srTra  uxha  'ca  sqsanhqm  V. 2,  10  PiiZ.;  —  ar^uxianqmca  'iargAqm sravanAqmca  Vr.  12.  3;  —  »r^iuxbaAe 'canhs^^ yat/radatgai^ahe  S.J,  18;  Yt.12. 38;  —  tqmyatata  vistaurui  ..  ?riiuxoäl \paiti  'latfhat   Yt.5.  76.  3)   'Wort'  im
24278:KompA.,  E.;  Ableit.j  s.  noch  No.  3.  —  vX. virä-  m.;  mp.  vir,  PDy.  vir.  —  Pü.!  vh-,  (im Komp.  aoch);  mari.  —  ")  Der  Mann  als  Mass- einheit; s.  Komp.  und  V.  4.  52.  —  ')  S.  da- gegen Yt.   14.   17;  nari  kihtfa  panca.dasaahS.
25321:Freigebigkeit  (Vj/(J>-)  geschieht"  (?):  aBai^a va^  mazdaoxtim  %ri.afsmfm  cä^rv.pistnm panca.ratu  '"him  Y.  ip.'iö,
=== BRT pantan/panta
```


## [2026-09-14T00:50:38.528Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SOD pnc\"; grep -n \"pnc\\|pncw\\|pnz\" SOD.txt | head -30"
}
```


### [2026-09-14T00:50:38.584Z] TOOL RESULT

```
=== SOD pnc
18117:(o)spanc   ©loc.  -yh  =^spnc,  sp'nc,  >spn- 
18244:(o)spanst,  spanst  ?  ^sp'nch,  >spnc 
18337:1628  *spnc   M  ^^  <  I^-OW9 
18344:1965,  244nl>  pi.  "sp'ynsu  GMS  260;  >spncu 
23505:(o)spinc,  osponc   =Vspnc 
26442:2855  *bt*st  =>  bt'st-pnc's-nwmyq 
26444:2856  bt'st-pnc's-nwmyq   C  ^j«b*jjju*iA 
53447:6791  p8pnz  =*  p5p»nz 
53938:6875  pn'c's   C  =4  pnc*s 
53955:pnc 
53967:6878  pnc  ^ 
53968:panc/j  ©<Av.  panca  ©ace.  -w;  ob.  -y  =*pnz 
53974:6879  pnc,m   S 
53975:pancam   ©ob.  -y  =»pncmy 
53983:pancas   ©<Av.  pancasqs  ^stw-pnc^ 
53989:6881  pncV   C=#  yw  pnc>s> 
53991:6882  *pnc,snw   B 
53996:6883  pnc's-nwmyq   C 
54004:panjac,  pancats  =»pnc5s 
54008:6885  pnc5s   B 
54009:panc-5as,  pancats  ©<*panca-dasa  «»pncc, 
54051:panc-tas  =^pnc8s 
54058:panc(u)  ©nom.  =^pnc 
54072:6892  pncwY'Sh   S  (jklf)jf^ 
54079:6893  pncykn8h   S 
54084:6894  pncyxz'n  M 
54094:6896  pnczng*n   M 
54095:panc-zangan  (-y)  (pncznk'n) 
54099:6897  pncznk'n  =»  pnezng'n 
54112:panjmik   =»pncmyk
```


## [2026-09-14T00:50:44.131Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '53955,54015p' SOD.txt\necho \"=== pnz\"\ngrep -n \"^6[89][0-9][0-9] pnz\\|pnz \" SOD.txt | head"
}
```


### [2026-09-14T00:50:44.194Z] TOOL RESULT

```
pnc 


276 


r*H 


TSP  2.401,  319,  1070,  6.55;  S  W,  IIJ  1976,  67, 
Frag.  23.1 

6878  pnc  ^ 
panc/j  ©<Av.  panca  ©ace.  -w;  ob.  -y  =*pnz 
five 

GMS  255,  1316;  BSTBL;  TSP;  SCE;  KG;  BBB;  C2 
gloss. 

6879  pnc,m   S 
pancam   ©ob.  -y  =»pncmy 
fifth 

Anc.  Lett.  3.7;  TSP  2.1094,  112a,  SCE  265;  GMS 
1095;  W-Li  68 

6880  pne's  C  *b~ 

pancas   ©<Av.  pancasqs  ^stw-pnc^ 
fifty 

GMS  1316,  1323,  958;  STi  43.10;  BSTii:  C2, 
13R27 

6881  pncV   C=#  yw  pnc>s> 

6882  *pnc,snw   B 
pancas-naw,  50nw 
fifty  nine 
TSP  5.3 

6883  pnc's-nwmyq   C 

panfias-numik 

fifty  ninth 
C2,  1R8 

6884  pnee  C 
panjac,  pancats  =»pnc5s 
fifteen 
S  W,  CLI  185 

6885  pnc5s   B 
panc-5as,  pancats  ©<*panca-dasa  «»pncc, 

pnets 
fifteen 
TSP  8.167 

6886  pnemy   B,  C 
=== pnz
53447:6791  p8pnz  =*  p5p»nz 
53968:panc/j  ©<Av.  panca  ©ace.  -w;  ob.  -y  =*pnz 
54266:6921  pnz   M  ^
```


## [2026-09-14T00:50:45.377Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"\\[pdf page\" SOD_pages.txt | sed -n '270,290p'\necho \"=== find pnc in pages file\"\ngrep -n \"6878 pnc\" SOD_pages.txt"
}
```


### [2026-09-14T00:50:45.446Z] TOOL RESULT

```
=== find pnc in pages file
23466:6878 pnc                                         ^                       panc-tas =^pnc8s
```


## [2026-09-14T00:50:49.592Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '54260,54280p' SOD.txt"
}
```


### [2026-09-14T00:50:49.637Z] TOOL RESULT

```
6920  pnyst-   B  dJ&*jk 
panist   ©pt.  st. 

(fo)perish 
TSP  12.38 

6921  pnz   M  ^ 
panj  =»pnc 

five 
GMS  67 

6922  pr  (0>>  ^~>  j^ijlji1**1!**^ 
par  ©<*uparh  Yaghn.  pan  Khwar.  pr  ©prep. 

+  ace.  -»prw\  prm1,  pr'yw,  pr'P,  pr'nKk), 

prym'nt,  prywy6 
to,  on,  at,  in,  for,  upon 
GMS  96,  1625ff
```


## [2026-09-14T00:50:51.010Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD panj\"; grep -n \"panz\\|panj\\|pnz\\b\" PHD.txt | head -20\necho \"=== PHD pand\"; grep -n \"pand \\|pand,\" PHD.txt | head -20"
}
```


### [2026-09-14T00:50:51.073Z] TOOL RESULT

```
=== PHD panj
219:āsn [?sn'], ~ xrad: innate wisdom. ásnidag [snytk'] = āsnūdaģ. asnüd(ag) [^snwt(k)'] cleansed, purified; pure, noble. a-sohisn [Pswhšn') unfeeling. Я asp [SW.SY A < A swsy’; sb | N ~] horse; (chess) knight. Ha 5Р7 aspánür [sp nwl] tomb. a-spās [’sp’s] ungrateful. aspast ["spst! | N ~] clover, lucerne. NM aspinj [^spnc | P “рулу, N sipanj] hospitality; inn. ШУ "Sy Me asprés [?splys | N ~] race-course. asré Pslwk! = Av. Gbrawa] priest. ~th : priestly office. Asré-kerpa [slzv(k)!klpk = Av. ādrē kahrp-] the form of fire. asrón Pslwn! = Av. āfrawan-) priest. last [AY T! < A?yty | M °st, N <] is, exists. ~ih : existence. *ast(ag) [*st(k)! | M ’st(g), N hasta] bone; (fruit) stone. astānaģ [s??nk!] need, misfortune. ~Smand [-wmnd] needy. āstār [s] | M ?sbr] sin. āstārēnīdan, āstārēn- (^s? ]yn-ytn!] cause to sin. āstawān [*stwb'n', ?stwp^n! | M ”stw?n] confessing, professing. ~th: confession, belief. astódàn [?stw(k)d’n' | M ?stwd^?n] sepulchre, ossuary. astómand [?st?zomnd] corporeal, material. ~th: corporeality. astux4n [sth(w)’n' | N ustux"án] bone. astwand ['stwnd | — M] — astómand. Astwihād [?stwyd’t'] the demon of death. āsūdan, āsāy- [*swtn!, ^? d- | N ~} rest, repose. —išn: rest, peace.
518:6 [OL < А Ч; ?w | M ’w] to, at; v. also 6h. ~ gird ámadan: gather, collect (intr.). — ham kardan: gather (tr.). ~ ham madan: gather (¿ntr.); come to an end. *óbad-, v. bastan, *óftadan. Obārdan, bär- Dwf?l-tn! | M ?wb’rd] swallow, devour. Obastan, *dbad- [NPLWN-stn! < A У npl; ^wpstn!, ^wpt- (if not Oft-, q.v.) | M ?wbyst, J ^wfst-] fall. *oftadan, Oft- Pwpt- | M *wpt'd, N uft~] fall. Gear Pwk’l] ebb. ogardan, ógàr- Pwk’l-tn'] remove, expel. *брга ['wgPy] declination, dip. Sh [KN < A kn | Mwh] so, thus; (with verbs, giving a sense of uncertainty) may, perhaps. Ohrmazd Pwhrmgd | M ^whrm(y)zd, N Hórmuzd] Ahura Mazda; astr. Jupiter; cal. 1st day of the month. -om [-wm | = M, N ~] suffix forming ordinal numbers from panjom onwards. -mand [-’wmnd | M -wmnd, N -mand] suffix forming adjectives of quality. *óréb(ih) [wlyp(yh)] disappointment. Dron ['cwlwn! | Mwrwn] hither. ад... ~: since. osán- Pws*n- | = M] throw down. óspurdan, ӧѕраг- [”zospl-tn!] tread, trample. 051°, v. awest^. Ost [220511] firm, reliable. ostigàn Pwstyk’n! | M Iwstyg^n, N ustuwàn?] firm, strong, sure, reliable. ~ih: reliability. lēš [wf | = M, N Ads] consciousness, intelligence. mih: = 68. 268 [wf | = M] death.
540:pahikēftan, pahikob- [ptkwp-tn'] strike. pahlawig [*p’hlwbyk' | (M phlwnyg), N paklaw(ān)i] Parthian; Pahlavi. pāhlom [phlwm] excellent, best, foremost. ~ih: excellence. pahlüg [p'Aok! | N pahli] side, rib. pahn [p?An! | N ~] wide, broad. сау [2d | N —à] width, breadth. lpahrextan, pahrēz- [phlyhtn', p'hlyc- | M phryz-, ] ~, N parhéxtan, parhéz-] abstain, refrain, avoid. *pahréxtan, pahrēz- [p’hlyhtn', p'hlyc- | M (phrystn), phryz-] care for, tend, protect. pahréz [Аус | N parhéz] defence, care. *pahrmāh- [ptimwh- | (N parmds-)] touch. ~арфіһ [Pkyh], ~i$n: touch, feeling. pak [DKY A < A аку; рк | = M, N ~] clean, pure, holy. ~ih: purity, holiness. pākīzaģ [p’kyck' | N ~a] pure. palang [ping | N ~] leopard. —-mušk [-mwsk' | N ~] speckled basil. pálüdag [p'Iwtk! | N ~a] starch jelly, flummery. pālūdan, pālāy- [p’lwtn', pPd- | (M p’rwdn, p’r’y-), N ~] strain, filter, purify. pambag [pmbk' | N panba] cotton. —ën [-yn'] (made of) cotton. pānāģ [p’n(’)k' | M p’ng] guard, protector; shepherd. ~th: protection. panāh [рт | = M, N ~] protector; refuge. pad ~ griftan: take refuge with. ~ih: protection. pand [pnd | = M, N ~] path; counsel, advice. panir [pnyl | N ~] cheese. panj [pnc | P рту, (M pnz), N ~] five. ~ag [-k! | N —a] pentad; hand, paw. ~аһ [h | N ~] fifty. panzdah [p’ncdh | M p’nzdh, N ~] fifteen. ірагаб [p?/k! | N para] piece, part, portion. ?párag [p?/k! | M p’rg, N para] gift, offering, bribe. paráhóm [pP?hwm = Av. para.haoma-] consecrated drink (the infusion in holy water of pounded лот and pomegranate twigs, sometimes with milk added). pardag [pitk! | N parda] veil, curtain. pardaxtan, pardaz- [pldhin', pldc- | M prdxt, N ~}, ~ az: be done with, freed of. ^ 6: set about, undertake. ~išn: freedom; undertaking. pardāxtan, pardaz- [pld’htn', pld?c- | N ~] accomplish.
1926:fifteen panzdah.
1927:fifty panjāh.
1961:five panj.
2194:hand dast, panjag; (daevic) gaw; right ~ dašn.
3060:paw panjag.
3079:pentad panjag.
4704:purrmāh Ku purrsardag 15 Qa» yes dahint roe to pusyān V 10 pusar ND 10 póstén V yen 10) póst we» 105 рап}, poz So panjah ay S ya) panjag, pēzag 13619 pos- = 74010 pūšīdan Wres“O ve pēšišn VUV puštībānīh «U ye) 43 «650105 pustiban т^” оу S ANA pušt VOU 199 puštag 1100010) püdagih ^t 5120
5499:suft suftan sanj-, sūz- sozag sózan sozisnig sozián sug südomand sūdabgār sūd sūdan sūdagīh sūdag sūdmand panjāhx geg
=== PHD pand
189:áhüg [TYBA < A ру; ”hwk! | MQyhwg, N āhū] gazelle. ahunawar [hnw!] the holiest prayer, beginning Yadā ahū wairyē. a-hunsand [Phwnsnd] dissatisfied. ^h : dissatisfaction. ahy [KZ Y < А k-zy | М hy] soon(est), first. ajģahān [>20/?л! | М ieikin, N azgahan] lazy, indolent. “АҺ: laziness, indolence. ak P! | N dk] evil, harm. -ak LIN ~] diminutive suffix. a-kámagómand [k mk’ wmnd] unwilling. a-kanārag ['kr?]k! | M ?qn’rg] unlimited, boundless. ~ih: boundlessness. a-kard Pārt! | (M °gyrd)] not done, undone. Akoman ['kwmn! | М ?qwmn] Evil Thought, an arch-demon, akómand ["£wmnd] evil, harmful. alā [Py] oh! alas! Аар [STLA, STRA < A £t ;?lk! | (М rel side. alálag PPH! | N lala] anemone. ālāy-, v. ālūdan. Aleksandar Piksndl | M *Ixsyndr, N Iskandar] Alexander (of Macedon). almās(t) Pim?s(t') | (M ?rm?s), N almas] steel; diamond. аадар [?/wtk'] defiled, polluted. АҺ: defilement. ālūdan, ālāy- Photn!, *Pd- | (M ?rwd), N ~] defile, pollute. Aluh Plwh | M "If, N ~] eagle. Xum [lum] millet. N~ amā [LNE < A l-nh | М ?*°h, N má] we, us. Amadan, āy- [Y ATWN-tn! < А y twn, V*th | M?mdn,?y-, N ~] come. amahraspand [?mhrsbnd | M (?)mhr’spnd] a Holy Immortal, a-mar [ml] countless, innumerable. amar [ml | N ~] reckoning, consideration. āmār- [?m?1-] reckon, calculate. ~išn: reckoning. a-marag [mlk') countless. amaraģān [?mlk’n'] generality, commonalty. ~ig [-yk'] general. ~iha [-yh’] in general, generally. a-marg [mig] deathless, undying. ~ih: deathlessness, immortality. ámárgar [?m’lgl | N ~] reckoner. amāwand [?m'wnd] powerful, strong.
191:amāwandīh: power, strength. ambag [’mbk' | N anbajat] a preserve, conserve. ambar [mbl, ?nbl | Аг. ‘праг ambergris. ambarag [?mblk! | N anbara] hairless (animal). Р amburdan [h/^mbwultn! | Р ?mPr-] = hambārīdan. a-menīdār [^mynyt!l] unthinking. āmēxtan, āmēz- Pmyhtn', ?тус- | M *myxtn, ?myz-, N ~] mix. ~išn: mixture; element. āmiz [^myc] side dish, vegetables. āmēxtan, āmēz-, read hammóxtan, hammoóz-. Amurdād [?m(w)rdt' | N murdád] Immortality, the sixth Amahraspand, guardian of plants and food; cal. sth month; 7th day. āmurzīdan, āmurz- [mewlc-ytn! | M?mwrz-yd, N ~) forgive, pity, have mercy on. ~išn: mercy, forgiveness. Р amwaštan [h|mwstn! | P ?mwst] gather, collect. an- Pn- | M ’n-] prevocalic privative prefix, un-, -less. ап [ZK < A zk;?n! | M Ап, N ~] that, he. ~ 1: that of; with a qualifier preceding a noun, equivalent to a following 1 e.g. ап i ahlawàn ruwān = ruwan i ahlawān, the souls of the righteous. -ап [2s! | M An N ~] suffix forming (i) present participles, (ii) adverbs, (iii) plurals. ānāb-, —išn, v. ānāftan. an-ābādān Ppp’ rn'] uncultivated. an-abaxšāwand [m ph} wnd] unrepentant. ~ih: unrepentance. an-abāy Pr’ Pd) unfitting, improper. an-abēdān [”7?5yt?x'] useless, unwanted. ~th: uselessness. anübublag [9 fwhlk' = Av. anüpers0a-] inexpiable, unatonable; the highest degree of sin. an-abzār Pwi] unskilled, incapable. ~th: inability. an-ādān [*77:?x!] insolvent. ^h : insolvency. an-ádüg [tk] incapable. an-afsēnišn [”77?syx$n!] indestructible. ānāftan, ānāb- [77ftn',*775- | M ?w pt, Qn m-)] avert, reject, frustrate. ~išn: avoidance, warding off. anág [77 k! | M >ре} evil. ~th: evil, harm. an-ügàh и: | N ndgah] unaware, unwitting. anüg-kardàr [RU АРД, -kunisn [-kwnšn'] evil-doer, maleficent. anagr Pngl) infinite. ~an [”x! | M?nyr^n] Infinite Light; cal. 30th day.
214:a-pus [' BRE] without a son, childless. ár-, v. árdan. 5 āranj "Inc | N ~] elbow.. 9-43. "Ant *a-rāst Prst'] untruth. ārāstan, ārāy- [Pstn!,^Pd- | N ~] prepare, arrange, adorn. ~ién: arrangement, adornment. a-rawüg [”/wbk!] immobile. Ard р | M?yrd, N ~] a goddess; cal. 25th day. ard [KHM A < А gm; п | N ~] flour. агаа [py | (M rd?w)] righteous, truthful. ardan, ār- [THNN-tn' < А V thn; ?l-tn'] grind, mill. ardāyīh ['i?dyh | M?rd?yyh] righteousness, rectitude. ardig [/tyk! | M ?rdyg] battle. ardikkar рук], -kl | M?rdyqr] warlike, warrior. ~ith: doing battle. arduš [”ldwš = Av. aroduš-] a degree of sin. Ardwahišt Prtwhst' | M ?rdywhyst, (N urdībihist)] Right, the second Amahraspand, guardian of fire; cal. 2nd month; 3rd day. arešk [lysk' | M ()rysk, N rašk] envy, jealousy. ~én [-yn'] envious, jealous. ārešn Pim! | M ”7ysn-, N (a)rif] cubit. aryand [?/епа | N ~] horrible. arģawān [*/gwk'*n! | N aryawān] purple. armēšt ["/myst'] inactive, infirm. ~ih: infirmity. armēšt-ģāh [-g’s] secluded place for the infirm. агбуї&п [/wdšn'] growth. ~ig [-y&!] growing, vegetable. ars Dis | M?rs, N ~] tear (drop). artēštār УЯ? | N artēšdār!] warrior. „īh: warriorhood. arus [2/00] white. arwand [wnd] swift, valiant; river Orontes. ~ih: swiftness, valour. arwés [lwys | M ?rwys, N ~] rope. arz [KSP! < А Ар; с | N ~] worth, value. Arzah [Iz h == Av. arazahi-] the eastern continent of the earth. arzan [PE < А prg’; len! | N <) millet. arzàn Plen | M *rz'n, N ~] valuable, worthy. ~ig [-yk'] worthy. ~igih: value, worth, worthiness. arzidan, arz- [?/с-уїп! | N ~] be worth. ~išn: value, worth. arziz (сус | M ?rzyz, N ~] tin, lead. —ën [-yn'] tin, leaden. ārzōg Picwk! | M'wrzwg, N àrzó] desire, lust,
382:*g5k4n [gwk’n'] details. Lc um ~ig [-yk'] detailed; precisely. (sassa tu) ģūmēz [gwmyc | N giméz] bull's urine (as ritual purifier). ģgūmēz- [gwmyc- | N giméz-] urinate. gön [gwa' | N gün] colour, complexion. ~ag [-k' | M geng, N güna] = gön ; sort, kind, form. gor [gwl | N ~] onager, wild ass. göspand [K YNA < А апу ? ; gwspnd | N ~] (small) cattle, sheep. ~-tihrag [-cyhlk'] holding the seed of cattle. ģūstān [gwst^n!] cattle-stall, cowshed. 1858 [gws | = M, N ~J ear. *GÓ68 [guš | N ~] cal. 14th day. tūšag [gwsk' | N ~a] corner. ģēošūsrūd [rwi^wslwt! = Av. gaošū.srūta-| acquired, learnt. 5051 [BSLYA < A bsr’; рой! | N ~] meat, flesh. ģūšwār [gwštw] | N ~] ear-ring. ģūw-, ~išn, v. ģuftan. gowag [swb k! | М gw'g, N goya] speaking, eloquent; speaker. *ģoūwizār [gwwc'[] explicit, in detail. göy [gwd | N ~] ball. göz [gwc | N ~] walnut. ~énag [gwzynk! | N gózina) a walnut sweetmeat. Gözihr [gwcyhl | Ar. jawzahr] astr. the Dragon. ~ dumb: the descending node of the moon. ~ sar: the ascending node of the moon. grab [22р | P grb] womb. grāmag [gľmk! | P gr’mg] possessions, wealth. grāmig [gľmyk! | M grmyg, N girāmī] treasured, dear. ~ih: affection, respect. 1$raw [giwb! | P grww] cane. *ģraw [glwb' | N giraw] pledge, security. ~ih, ~(a)g4n [glwk’n' | M grug*n, N giraugān] = *graw. grayidan, gray- [gl?d-yin' | P gry-, N gtráy-] lean, incline; intend, desire. ģriftan, gir- [OHDWN-tn' < A V?hd; glptn!, gyl- | M grypt, gyr-, N giriftan, ~] take, hold, restrain. «išnīģ : tangible. griftār [gipt?l | N gir~] held, taken; captive. ~Omand [-'wmnd) tangible. grih [glyh | N girth] knot. lgriw [CWLE < A swr-h; glyw'] neck, throat. ?0riw [CWLE, glyw' | M gryw] self, soul. sgriw [glyw! | P gryw, N girī(b)] a grain measure, modius, peck. griwag [glywk!' | N giriwa] hill, ridge. ģrīwbān [g/ywp?n! | N girībān] neck-guard, gorget. griyistan, griy- [BK YWN-stn'< A У bky; gld-stn! | M gryy-stn, N giristan, giry-] weep, cry.
398:P hd [Aw' | = P] that, he. Hóm [kwm | N ~] the sacred plant Haoma (ephedra). homānāģ [h(w)m’rk' | N hamana, J xumana], 6 .. . ~: like. ~th: likeness. hómast [hwn'st!] various series of prayers. hómyjén, -ïg [hwmyn!, -yk'] of Haoma. ~ӧтапа [-'wmnd] prepared with Haoma. Ногааа [hwrdt' | M hrwd'd, N Xurdād] Perfection, the fifth Amahra- spand, guardian of water; cal. 3rd month; 6th day. hdsag [hwsk' | М лое, N xēša] ear of corn, cluster; astr. Spica, Virgo. hēšēnīdan, hoSen- [hwsyn-ytn'] (cause to) wither. hēšīdan, hēš- [hws-ytn' | M hwi-, N x~] dry up, wither. héy(ag) [hwy, -k! | M hwy] left(-hand). Hróm [hlwm | M hrwm, N Рат] Byzantium, Rome. ~ayig [-dyk'] Greek, Byzantine, Roman. hu- [hw- | = M] good-, well-. ~ih: good, goodness. hu-bóy [hwbwd] sweet-smelling, fragrant. ~th: fragrance. hu-čašm [hwesm] unenvious, benevolent. ~ih: benevolence. hu-čihr [hweyhl | M hweyhr, (N xujir)] fair, beautiful. hudà(ha)g [hwa?(h)k' = Av. hudàáh-] good, beneficent. ~th: beneficence. hu-|-dast [hwdst'] skilful. ~-dén [-dyn'] of good (i.e. Mazdean) religion. ~-ddsSag [-dušk'] very pleasing. m-ēwāz [-"yw'c] of good speech, affable. —-ëwàzih : affability. ~-fraward [-plwit'] blessed, the late. hugar [hwgl] easy; beneficent. hu-|-&ówisn [hwgwbsn'] of good speech. ~-gugar [-gwk’l] easily digestible. ~-kunign [-kwnsn'] of good behaviour. „-mānīh [-m’nyh] good-mindedness, benevolence. humat [hwmt' = Av. humata-] good thought. humāy [hwm’y | N ~] a bird of good omen; eagle. hu-menišn [hwmynsn'] of good thought. hu-murwāģ [Awmwlw’k'] auspicious. hunar [hwal | M hwnr, N ~] virtue, ability, skill. hunarāwand [kwn wnd | M hwnr'wynd] skilled, virtuous. ~th: skill, virtue. hunarómand [kwn wmnd | N hunarmand] = hunarāwand. hunidan [kwnytn'] extract, express (juice). huniyág [/sonyd?k! | N xunyá] delightful. ~th: delight, entertainment.
455:mand [mnd | = M] house. miindag [m?ndk! | M m'ndg, N ~a] tired; remiss; fault, sin. “Аһ: tiredness. māndan, !màn- [K TLWN-tn! < A У ktr | M mnd, N ~] stay, remain; v. also % *mán-. mang [mng] henbane. mänig [mnyk'] household member. mānistan [{KTLWNstn'] = mandan. māništ [m?nyst!] abode, dwelling. ~ag [-k'] sedentary, settled. mānsār [mnsl = Av. ma0ra-] (holy) word, spell. -~-bar [-b/] priest. ~spand [-spnd = Av. spanta-] holy word; v. máraspand. imar [ml | M mr, N ~] number, reckoning, account; class. *mar [m/] scoundrel, felon. таг [ml | N ~] snake. mār-, —išn, v. mārdan., тагар [mik!] number. тпагар [mPk!] perceptive, sensitive. Māraspand [mrspnd | N ~] (= máns?rspand), cal. 29th day. *martabuk [mic”5wk'] brave, valiant. ~ith: bravery, valour. mard [GBRA < A gbr; mlt' | M m(y)rd, N ~) man. mārdan, màr- [ml-tn'] perceive, notice, feel. ~i$n: perception. „išnūmaud [-£rwmnd] perceptive. mardanag [mit?nk! | N ~a] manly, brave. ~ih: manliness, bravery. mardóm [ANŠWTA < A?niwt?; mltwm | M mrdwhm, N mardum] man, mankind, people. ~th: humanity, humanness. mardóm-zàádag [mltwm 2tk' | N mardum-zād] human being. ~ih: humanity. marģ [mlg | M mrg, N ~] death. ~-arzan [-lc’n'] deserving death. ~ih: = marg. --0mand [-”wmnd] mortal. mārīģ [m'Lyk! | M mryg-] word, spell. marw [mlw! | M mrw, N —, (mary)] herb. marz [mlc | M mrz, N ~] boundary, march; astr. term. marzanģēūš [mlengws | N ~] marjoram. marzidan, marz- [mlc-ytn! | М mrzyst, mrz-] copulate. išn(īh): copulation, fornication. marz(o)bàn [mlcp’n' | № ~] margrave, warden of the marches. -masāy [-ms'd] suffix, -sized. mast [mst! | = M, N ~] bemused, intoxicated.
540:pahikēftan, pahikob- [ptkwp-tn'] strike. pahlawig [*p’hlwbyk' | (M phlwnyg), N paklaw(ān)i] Parthian; Pahlavi. pāhlom [phlwm] excellent, best, foremost. ~ih: excellence. pahlüg [p'Aok! | N pahli] side, rib. pahn [p?An! | N ~] wide, broad. сау [2d | N —à] width, breadth. lpahrextan, pahrēz- [phlyhtn', p'hlyc- | M phryz-, ] ~, N parhéxtan, parhéz-] abstain, refrain, avoid. *pahréxtan, pahrēz- [p’hlyhtn', p'hlyc- | M (phrystn), phryz-] care for, tend, protect. pahréz [Аус | N parhéz] defence, care. *pahrmāh- [ptimwh- | (N parmds-)] touch. ~арфіһ [Pkyh], ~i$n: touch, feeling. pak [DKY A < A аку; рк | = M, N ~] clean, pure, holy. ~ih: purity, holiness. pākīzaģ [p’kyck' | N ~a] pure. palang [ping | N ~] leopard. —-mušk [-mwsk' | N ~] speckled basil. pálüdag [p'Iwtk! | N ~a] starch jelly, flummery. pālūdan, pālāy- [p’lwtn', pPd- | (M p’rwdn, p’r’y-), N ~] strain, filter, purify. pambag [pmbk' | N panba] cotton. —ën [-yn'] (made of) cotton. pānāģ [p’n(’)k' | M p’ng] guard, protector; shepherd. ~th: protection. panāh [рт | = M, N ~] protector; refuge. pad ~ griftan: take refuge with. ~ih: protection. pand [pnd | = M, N ~] path; counsel, advice. panir [pnyl | N ~] cheese. panj [pnc | P рту, (M pnz), N ~] five. ~ag [-k! | N —a] pentad; hand, paw. ~аһ [h | N ~] fifty. panzdah [p’ncdh | M p’nzdh, N ~] fifteen. ірагаб [p?/k! | N para] piece, part, portion. ?párag [p?/k! | M p’rg, N para] gift, offering, bribe. paráhóm [pP?hwm = Av. para.haoma-] consecrated drink (the infusion in holy water of pounded лот and pomegranate twigs, sometimes with milk added). pardag [pitk! | N parda] veil, curtain. pardaxtan, pardaz- [pldhin', pldc- | M prdxt, N ~}, ~ az: be done with, freed of. ^ 6: set about, undertake. ~išn: freedom; undertaking. pardāxtan, pardaz- [pld’htn', pld?c- | N ~] accomplish.
566:se-pay [3-p'd | N sipá] three-legged. sēr, v. Sagr. se-Sabag [3-spk!] three-night-long, trinoctial. seyom [зит | N ~] -third (in compound numerals). sëzd [s(y)zd | P syzd, (N séz/agi?)] might, tyranny; tyrannous. sézdah [sycdh | M syzdh, N ~] thirteen. sézdén [s(y)zdyn! | P syzdyn] mighty, tyrannous. si [sy] goose. sidig(ar) [styk', -kl | M sdyg, N sidigar] third. sih [30 | M syh, N si] thirty. ~om [-wm] thirtieth. sik [HLYA < А hP; sk | N ~] vinegar. sisimbar [sysymbl, -nbl | N sisambar] sisymbrium, wild-thyme. *Skandar [swkndl | N sikandar) = Aleksandar. snāh [sph] blow, strike, violence. sneh [snyh] sword. snéxr [snyhl] snow. snézag [snyck!] snow. snóy [snwd] (rain-, snow-)cloud. sófistà [swkpst’k'] sophist. 1s68 [swk'] use, profit, advantage. 25806 [swk!'] burning, combustion. 3806 [swk! | N só(y)] side, direction. sógand [swknd | M swgnd, N saugand] oath. ~ XWardan: take, swear an oath. sóhistan, sóh- [swh-stn'] touch, feel. ~iSn: feeling, sense. ~iSnig : feeling, sensitive. sēr [sz] salty. ~ag [-k!] salt (land). ѕӧзап [swsn! | N ~] lily. Só&yans [swkšydns = Av. saošyās] saviour (especially the final Saviour who will bring about the frašagird). sóxtan, sūz- [swhtn!, swe- | М swxt, swc-, N ~] burn. ~išn: burning, combustion. ~išnīg: burning, flaming. sūzāg [swo k! | М swe'gyn, N séza] burning. sózan [swen' | N ~] needle. spāh [sp’h | N sipah] army. ~bed [-pt! | N -bud] general, commander. spandān [spnd”x! | N sip~] mustard seed. Spandarmad [spndrmt'] N isfandármuó] Holy Thought, the fourth Amahraspand, earth goddess; cal. 12th month; sth day. spar [spl | M ‘spr, N sipar] shield. spar-, v. spurdan. spas [sp’s | M ?s-, “р>, N sipas] service, gratitude, thanks.
583:šāh [MLKA < A mlk’; th | M £h, N <] king. „ān šāh [MLK Ап MLKA | N ~] king of kings. 7--balüt [shbiwt' | N ~] chestnut. ~-дапар [-d’nk' | N —dàna] hemp-seed. ~-esprahm [-splhm | N ~isparam] basil royal. Sahigan [#hyhk'n' | M Phyg^n] palace. šahr [štr' | M £r, N ~] land, country; city. ~estan [MDYNA < A mdyn’; Str'st?n' | M #šhrs Pn, N ~] province; capital, city. Sahrewar [štrywr | N ~] Best Rule, the third Amahraspand, guardian of metals; cal. 6th month; 4th day. šahryār [ftr'd?] | M shry’r, № ~] lord, sovereign, ruler. ~ih ; dominion, reign, sovereignty. šāhwār [š%w?/ | P ?hw’r, N ~] royal, kingly. Sakar [fA] | M šgr, N ~] sugar. salwar [ilw] | N ~] trousers. šām [Pm | = P, N ~] evening meal, supper. Sambalidag [smblytk' | N šambalīd, -lila] fenugreek. šamšēr [smsyl | N ~] sword. бап [in' | N ~] hemp. &ünag [P?^nk! | N ~a] 1. comb; 2. pitchfork; 3. shoulder-blade. šanēn [snyn'] hempen. šarm [т | M #m, N ~] shame. ~-gah [-g*s | N ~] pudenda. ~gén [-k(y)n! | N ~gin] ashamed. &asab [р | (P Shrb)] satrap. ^Agàn [-yk’n'] satrapal. šast [60| M šst, N ~] sixty. šaš [STA < A st | M f, N ~] six. šaw-, v. Sudan. *Sawag [swb’k'] bat, flittermouse. šāyendaģ [^ dyndk!] able, worthy. ~ih: ability, worthiness. šāyistan, šāy- [P?d-stn! | M P?y-, N ~] be able; be worthy. šāyēd [P?(d)yt! | N šāyad] one can, it is possible. šāzdah [cdh | М ?zdh, N sanzdah] sixteen. бер [ғур | N ~] declivity. šēb- [šyp- | M syb, N ~] move quickly; be confused. ~&g [PR' | N —à] swift, nimble; viper. ~išn: confusion. šēd [у | N ~] bright; sorrel (horse). *šēdā [угу] bliss. šēr, v. Sagr. šēwan [£fywn! | N ~] lament. šiftālūg [spi?lwk! | (P šyft ‘milk’), N šaftālū] peach. šiftēnaģ [šp:ynk! | (P £yftyn ‘sweet’)] a sweetmeat.
605:wad-baxt [wtP ht! | N badbaxt] unfortunate. wad-dil [wtdyl | M wddyl, N baddil] coward(ly). wadgarih [wtglyh] evil-doing. wād-ģirdaģ [w° tgltk' | (N gird-bād)] whirlwind. wad-góhr [wtgwhl | N bad-gauhar] ill-, low-born. wad-kamag [wtk’mk'] malevolent. ~ih: malevolence. wadrang [w’ ting | N bādrang] citron. cc Dë [-bwd | N -bóya] lemon balm. wad|-tóhm [wttwhm] = wad-góhr. ~-wazag [-w’ck! | (N gawāža)] abuse. --.Xém [-hym] ill-natured. waf- [wp- | Р wf-, (N bàf-)] weave. ~išn: weaving. wafr [wp! | M wpr, N barf] snow. ~énag [-ynk!] а sweetmeat. waydān [wy?n! = Av. waybana-] head (ahuric). wahāg [wP?k! | M тор, N baha] trading; value. — burdan: value, estimate. wahār [wh], (bj?l) | M wkr, № bahar] spring. ~ig [-уЁ! | N -z] spring, vernal. wahig [ZZLA < A Semi (?); whyk' | M whyg, N *bahi] kid; astr. Capricorn. wahist [ол | M whyst, N bihist] paradise. ~Ig [-yk! | N -1] (worthy) of paradise. Wahman [whwmn' | M whmn, N bahman] Good Mind, the first Amahra- spand, guardian of cattle; cal. 11th month; 2nd day. wāhmān [*w-n! = whmn' | MOw^hmn, J whmn, N bahman] so-and-so. Wahrām [wlhl?’n', whPm | M whr’m, N bahram] god of war, victory; astr. Mars; cal. zoth day. ātaxš 1~: a major sacred fire. wak [wk! | N bak] frog. wālan [zo n! | (IN barzan)] settlement, community walg [wlg] = warg. walidan, wāl- [w]-ytn! | N bdlidan] grow, increase, prosper. ~išn: growth. wümidan, wam- [w’m-yin'] vomit. wan [wn' | N bun] tree; stock, stem. ~ i $urgünig : pistachio tree. ~ 1 was-téhmag: the Tree of Many Seeds. wān-, ~išn, v. wanidan. wanafšag [zvnpšk! | N bunafša) violet. Wanand [wnnd] astr. Vega. wandaģ [wndk'] rope, cord. wang [KALA < А ql’; wng | = M, N bang] voice, cry. wānīdan, wan- [wn-ytn! | M w’n-yst] conquer, overcome, destroy.
1173:cattle gēspand, stör.
3056:path pand, widarag.
4422:23 Day pad Dén 27 Asman 24 Dén 28 Zamyad 25 Ard (Ahrišwang) 29 Māraspand 26 Aštād зо Anagran (v) Gāhs Hawan—morning Ēbsrūsrim—sunset to midnight Rapihwin—afternoon Ušahin--midnight to dawn Uzérin—evening
4891:jām mānsīr māns*rbar mānsšrspand māraspand mānbān mānbed mānišn māzanīg māzandar māzdēsnīh māzdēsn fradagt mar
```


## [2026-09-14T00:51:02.829Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BQT v1 pages with پنج\"; grep -n \"پنج\" BQT_v1_pages.txt | head -20\necho \"=== BQT v1 پند\"; grep -n \"پند\" BQT_v1_pages.txt | head -20\necho \"=== page tags near\"; grep -n \"\\[pdf page\" BQT_v1_pages.txt | head -3"
}
```


### [2026-09-14T00:51:02.917Z] TOOL RESULT

```
=== BQT v1 pages with پنج
220:اژ پر تو کوشش صدو پنجاه سالهً دانشمندان دیگر امروژه ازهرجهت از زبان
278:نمونه ای ازین لپحه در پنج سرودگانها ( اهتود - اشتود - سنتمد بت
344:پنجم پیش ازمسیح هیز بست .
442:پنجمين پادشاه ساسانی بجای مانده است . بیشتر سنکنبشتهای بادشاهان‌اولی
1049:بدان زبان بود» واين لفتی است منسوب خهله* » و آن نامی است که بر پنج
1069:الف - زبان پارسی را شامل پنج یا هفت زبان دانسته‌اند که یکی از
1222:اقب ۱سی ویپنج ۱ زبائهای ایرانی
1356:۵-فر بز ندی ۲۵۲1227001 درفر یز ند((دهکده‌ای‌در پنج‌فرسنگی
1376:( مقدمة بر هان قاطع. پنجم )چپل زيك لبجه‌های ایرانی
1453:خراسان وزپر خویش را فرمو دکه مردانی از پنج کورةاصلی خراسان گرد
1633:۱۳۰۱-۳۶ ص۱۶٩‏ ۲- دبوان ناصر خسرو .مقدمه پنجاه
1664:مدل‌آن بنداشته‌اند ۱ ۴۰پنجاه ويك ‏ تصرف کاتبان
1696:دساتیر بشرح سخن رفته است .پنجاه و سه دساثیر
1741:وخشور خویش ساسان‌پنجم فرمود» نامه پیغمبران را بز بان‌روزگار خودت
1742:بگردان .ساسان پنجم نیز چنین کرد» بسخنان‌شانزده وخشور که‌نامهٌ خودش‌هم
1748:ساسان پنجم پنج کلمة متن‌را درصد وهفتاد وشش کلمه‌دیگر شرح‌داده است.
1751:دیگر ايران باستان باشدیعنی زبانی که درهز ار وسیصد و پنجاه‌سال پیش‌از
1752:اين‌در جایی‌از انران‌زمف رواج داشته باشد» زیرا ساسان‌پنجم عفر دساتر
1757:شباهتی بز بان ساسان پنجم ندارد.
1758:ز بان فسیر دساتیر فارسیاست‌اما چه فارسیی؛پارسی‌سره» درهر جا کهپنجاه وپنح دساتیر
=== BQT v1 پند
224:معروف بپند واروپایی بشماره‌یرود .
1110:« بر تخت نشستن‌شیرویه واندرز کردن وفرستادن‌سران‌نزد بدرپندویوزش»
1113:ولیکن مرا شاء ايران قباد ۸ بی ادرین پند و اندرز داد
1688:ممجزه لفت براز نده‌ای پنداشنه ودرمدح بیغمبر گفته:
1734:است [نرا ز بان آن‌سامان پنداریم» يااينکه بگوییم مردنیر نگ بازی‌درهمین
1760:است که پارسی درست پنداشته شده‌ودر بر هان‌قاطع وانجن آرای‌ناصری
1785:کتاب مقدس وصعيفةً آسمانی میخو |ند*] نچنان که درابران پنداشتند حقيقة
1880:بدستیاری‌ملا فیروز انتشار یافته بود . رضا قلی‌خان مانند صدها نو پند گان
1881:همزمان‌خود[ نر| از نامه های دینی ایران باستان پنداشته » در یاد کردن
2029:مان دو تن در گرفت و هر دو پنداشتند که آن نسخه منحصر فرد
2749:بپندوستان رفته‌ودر بار شاهجپان رادریافته و مد در راه‌مکه در گذشته‌است.
2780:۴سر مه دراصفپان متو لدشده؟ ودر سال ۱۰۱۵ بپندوستان
2833:با 2 فرهنک پندهشن 6 که پوستی]آنرا بط م دسالیده ) بود» است ( - م.)مقدمه هشتاد وهشت
2978:قدیم» وصاحب برهان هردو کلمه رابایکدیگر تر کیپ نوده ویکی پنداشنه
4332:۸ه‌دد خجان جنگلی ایر ان . مپندس حییب نله تایتی. از انتشارات
4462:۵ - گیاه‌شناسی (تشریح عومی نبانات). مپندس‌حبیب‌ابله ثابتی.از
6323:و نم سپند و خمیر خشكث شده و سر که سازند
6570:بيك هفته بر پیش بزدان بدلد مپندار کاش پرستان بدند
6958:دیگر ). آتوریات مارسپندان ( آ نریاد مهرسیندان ) یکی از فوبدان بز رکه عصر علسالی است که
7426:یز کنته اند - و بمعنی حمانا و پنداری وگمان
=== page tags near
```


## [2026-09-14T00:51:03.656Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nls | grep -i mon\necho \"---\"\ngrep -c \"\" MON_part1.txt 2>/dev/null"
}
```


### [2026-09-14T00:51:03.729Z] TOOL RESULT

```
MON_part1.txt
MON_part2.txt
---
99339
```


## [2026-09-14T00:51:11.123Z] TOOL CALL #23: Bash

```json
{
 "command": "sed -n '1,60p' tools/ref_page.py"
}
```


### [2026-09-14T00:51:11.189Z] TOOL RESULT

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


## [2026-09-14T00:51:13.019Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint(len(pages))\n# find pages containing پنجه\nfor i,p in enumerate(pages):\n    if 'پنجه' in p and 'پنجم' in p:\n        print('IDX',i, p[:200].replace('\\n',' | '))\nEOF"
}
```


### [2026-09-14T00:51:14.174Z] TOOL RESULT

```
777
IDX 647 بنحك - یشم اول بروزث اردك» کل له | ِنبهٌ حلاج ی کرده باشد- وبفتح اول کیاهی است | و آن ینج شاخ «یباشد و مانئد عشقه پر درخت | بت | نج گنج باکاف فارسی بروزن ینج‌پنج, | کنابه از حوای خصسه است ت که سامعه و باصره | وذا
```


## [2026-09-14T00:51:18.139Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in (646,647,648):\n    print('======= IDX',i)\n    print(pages[i][:2500])\nEOF"
}
```


### [2026-09-14T00:51:19.188Z] TOOL RESULT

```
======= IDX 646
یتجاب
پنجاب. بر وزن کنجاب » ولابتی
است از ندوستان. که لاهود و توابع آن
باشد ٩‏ . 2
دوچت انگشت ه معروف است- و نام
نبانی هم مت که آن‌ا دلاشوب خوانند و بوته
و درخت آن در کار رودخانه ها روید و ب رگ
آن ماتنه ب رک شاهدانه باشد و آن را عربی
دو خمة اوراق و ذوخمسة اسابع خوانند و تخم .
آن را حب الققد کوبند و در علت اسشت بکار
مرند؟ - واشثان را نز گفتداس ونام موضنءی‌هم
هست تزدباگ بمراة تبربز» و بحذف همزه هم
بنطی آمده است که ننجد
آن فنجکشت است . اکر شهوت برزنان غلبه
کند قدری ازآن در زین آبدان دود کنند در
حال نشفاند. #۶
بنحاهه بروزن‌نکم‌اهه. مدت‌اعتکاف
صاری است و آن پنجاء روز می باشد چنانکه
چله‌اهل اسلام چهل‌روز است ؟.
پنجیا- با بای فارسی
خرچنکه را کویند. و آن
جانوریست که در آب و در
خشکی هسر دو می باشد
و بعربی سرطان خوانند -
وبرح‌چهارم است ازدوازده عنجپا
- آمروز بها کستان تعلق‌دارد ۰
تب باشد و «عرب
بالف کشیده »
۴ - یی از چندین چله درعهد می‌سال
وا
بنحبا پكث ‌ بفتحتحتانی وسکون کاف»
بممتی بنجیاست که -رطان باشد.
پنجپایه - بنتجبای حطی, بممنی‌پنم-
پايك است که سرطان باشد- ونام برحچهارم ات
از فلك .
پنج پیچا
گونند نی حل و مغتری و مریخ و زهره
و عطارد .
سره بر وزن سنجر » مخفف پنجره
ات و هرچزی که‌مشك وشنکه داو داشد 5
بنحر ود کنابه از مدت اندك باشد
چنانکه گوبند * دنیا پنج روز است * و تخصص
به‌پنج روزاز آنست که آدمی در بك روز از ایام
هفته بدنبا می‌آید و در مك روز اژ دنا میرود
وباقی پنج روز هیداند که ابامنهیش آوست۵ .*
پنحر هٌ لاجورث « کنابه‌از آسمان
پنجش» بکس اول بر وزن دلکش »
کلولهٌ بثبةٌ حلاج ی کرده را کویند.
بنج شقبه - کنابه از حوای خمثناهر
است که آن -اممه و باصره ر لامسه و ذابقه
وشامه باشد .
وگ
۴ بو پنجیجد.
نجاه -
افنانی ۵10165 «
. کیل؟
که
معرب آنن < بنجره» است. «تفی» .
======= IDX 647
بنحك - یشم اول بروزث اردك» کل له
ِنبهٌ حلاج ی کرده باشد- وبفتح اول کیاهی است
و آن ینج شاخ «یباشد و مانئد عشقه پر درخت
بت
نج گنج باکاف فارسی بروزن ینج‌پنج,
کنابه از حوای خصسه است ت که سامعه و باصره
وذایقه و لامه وشاهه باشد - تصا از مت ۱۶
نیز گوبند که پنجوفت نماز باشد ٩‏ .4
پنجم رو اق- کنابه از آسمان پنجم
بنج نوش ۰ بروزن رنج نوش حعجولی
باشد مر کب از پنج چیز که بجهت تقوت دل
خورند؛ ومعرب آن فنجنوش است.
له - بنتح اول و خفای آخر بر وزن
کنجه » ممروف است که پنم انکشت با کب
۵ ست‌و دا اشف ازاتان وحبوانات
دیگر ۴ - ورضی‌را نیز کویند
وی و یک‌دیگر را >
گرفته باهي رقص کنند و هعراب ۳
آن فنزح است ۴ - و کلوله
رس نف پنجه
برای جنکه نا ان - و سنگه عنجنیق را
۳ 5 7 بر درخت بحجد و آن را
عشقه خوانند, و باین معنی بکر اول هم آمده
است - و بفتح اول و ظهور آخر مخفف پنجاه
؟ وان ید ای 2 فا
۳۴ پنجه عر کب استار:
پنجهة کبك موی
.است که عدد معلوم باشد ۴ - و ماهی - و دام
و قلاب و شست شت ماعی را هم کفته‌اند چه ماهی
انار و است" از حروف تهبجي
شست ماهی باعتبار پنجه که حصب عد<د شصت
ه‌. ۲
1
و
کته و موی یز گفته اند که از سرزلف
ببرند وآن‌را پیچدخم داده برییشانی گذارند .
بنحه بر دوی‌ددن- کنابه ازروسیاه
کردن باش .
پنچه نل- بنم اول و فتح جیم فارسی
وبای ابسد بروزن مستمند » پیشانی‌بند را گویند
که بعربی عصابه خوانند .
پنحة بیچاره - کنامه از کراکب
وعطارد است
بنحة دزدیده. ترجبة خنة
مسترقه است؛ وآن ب پنج روزی بباشد که درآخر
تقویمها نویستد. و ی تمیه بدژدیده از آن
جهت شده است که وزیر یکی از بادشاهان
عجم حاصل این ینج روز را از ثمام مالك او
همیشه از مان میبرده و بصاب در لمی‌آورده
4
پنحة کيكك درک نارلحن عت‌است
ازسی لحن باربد بقول بسنی .
؟ - باین‌معنی‌در موی « تاوادیا
۴ ره :
است! ماهی را دد عربی نون 0 نون
۴ ره : رنجاه - حمله مخدرش ۱
بحساب خمل ینجاه است و
۷ - رك : بپترك () .
> ۸ 5
تقبه ه ۰
======= IDX 648
کوند وآن دا گربه نز خوانند .
نج هر لم» کیهی باشد خوشبوی
باندام پنج انگشت - کویند مریم مادر عیسی
علیه السلام در هنگام وضع حمل بر آن کیاء
چسسلده بود*
بنج یو ۱۵۵ - با تحنانی و واو مجهور
و دال بر وزن نج روزه : ینعی ضف عشر
است چه ده بوده ۴ عثر را گویندکه ده يك
باشد .
نك بفتح او وسکون ثانی ودال ابجد,
آنت که بعربی صیحت کوبند ۴ - و بممنی
زغن و غلواج هم‌احده است - وم اول كلولهةٌ
نبة حلاجی کرده‌باشد وبااول مکورزه نشتکاهرا
گوشد و مری مفعد خوانند 5
پند ار - بکسر اول بر وزن بیار »
تکیر و ععحب را گویشب وامر بدشمعتی هم‌هست-
(۱) چك: ژند ویاژند.
در اد
ویممنی فکر وخیال و تصور - و خود را بز رکه
پتداشتن ثیز آهده است.
بدنی آخر یندار است که فکر و خیال و تخل
پنداشتن ٩‏ - مک اول اش بزنن
مگذاشتن » بمعتی گمان بردن و ور کردن
باشد و بمعنی عجب و نکیر نمودن هم آمده
است . 4
ندش منم اول و فتح الث بروزن
کس کش کلولة ثبةٌ حلاجی کرده را کوشد.
باشك .
بلفت زند و بازند ۱ .
قنك ۵ ع بکس اول و سکون انی و فتح
. ظ , ینجوبه . رگ: الفهرست سص ۳۳۸ ۱۹ ۶« ششویبه» بجای «ینجوبه»‎ - ٩
۳ - رنده‌بوده. و ۳ پهلروی۳21001.]برانیباستان 2۸ (راء) «بارتولمه ۸۷ بارسی
باستان! 311 (راء), سااسکربت 4)1980, ارمنی10119, استی1300 (میلء آرزر) <ا-عق۰۳۳۰
«نیب رک ٩۲۹یس‏ اصللا پندیممنی راء است و مجازاً پنددادن بمعثی نشان دادن راه و دوش اینتی
4 وراوستا بمعنی بیراهه‌است. «فاب ۱ : 2۵٩‏ . ۴ اسم‌از پنداشتن (ه .م).
۵ پپلوی 25420 620 2 « اسنق۳۳۱ 6« نبر که ۵۲*سعنی چنن فرض کردن!
تر کیب‌اسم وفمل. ازضمیر نظیر دارد [ُرك : زنهاره وتبعات ابرانی. دار هستتر ص۲۰۸ ».بنداشتن
در ادبیات فارسی درست بمعتی لغوی خود سنی فرش کردن وانگاشتن ۳۹ خیام گوید:
چون نیست زهرچه صست جزباد بدست چون هست بپرچه هست تتصان و شکست
انگار که هرچه هست در عا کت پندار که هرچه نیست در عالم هست.
« [ کنیز جمفید پس از نوشیدن شراب] سر بربالین نهاد و بکثبانه دوز بخفت * همه
پنداشتند که کاراو باخر رسید» چون‌از خواب درآمد ازدرد شفیفه هیج‌اثری‌نیافت.» «نفابس‌الفنون
قم اول‌در علوم اواخر ص۲۶۰۱» خواجه عبدالله اضاری کوید : خدایا ! پنداشتم که ترا شناختم »
اکنون پئدار را در آب‌انداختم .» سعدی در گلستان؛
ته‌ییند مدعی جز خویشتن را که دارد پرده پندار در پیش .
٩‏ - هز ۳200200 , پهلوی ۳228740 , فرزند « بوتکر ۱۷۰ 4 ۰
0 پنداوسی ‏ رك : پیداوسی .
```


## [2026-09-14T00:51:42.359Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfirst=None\nfor i,p in enumerate(pages):\n    if p.count('بر وزن')+p.count('بروزن')>=3:\n        first=i; break\nprint('first dict page idx',first, pages[first][:300].replace('\\n',' | '))\nEOF"
}
```


### [2026-09-14T00:51:43.517Z] TOOL RESULT

```
first dict page idx 99 نود ويك عایس برهان | چنانکه خوداودرهقدمه میبگوید که فصدداشته است کتاب‌خودرا بطری‌ایجاز | بنویسد « و آن بپیچوجه صورت نمی بست مگر باسقاط شواهد و زواید ؛ | بنابر این از آن هردو دیده پوشیده بلفات و معانی آن اکتفا و اختصار | #نمود...» ۱ | اينك از هريك ازانواع اشتباهات وافلاط فوق ی و | میشوده با نقل‌عون عبارت برهان»
```


## [2026-09-14T00:51:47.194Z] TOOL CALL #27: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))['BQT'];print(json.dumps(d,ensure_ascii=False,indent=1))\""
}
```


### [2026-09-14T00:51:48.247Z] TOOL RESULT

```
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
 "notes": "Persian OCR is mediocre: headwords and Mo'in's footnotes (e.g. '۱ - رك: ابر کوه', Pahlavi/Avestan Latin forms) are mostly readable but with many character errors; search with short substrings and tolerate errors. BQT_v1_pages.txt was built from the djvu.xml; BQT_v2_pages.txt from pdftotext -layout of the _text.pdf. Volumes 3–5 (roughly ح/خ–ی and the تعلیقات volume) are not online in full text; for those use Dehkhoda quotations of Borhan/Mo'in via vajehyab/abadis/parsi.wiki, or page images on noorlib (different edition). | Vols 3-5 scans (image only) in incoming/BQT; vols 1-2 have OCR text files BQT_v1_pages.txt / BQT_v2_pages.txt. Offsets verified by eye at several pages (v3 drifts by ~4 pages; page_map gives exact positions once built). || UPDATE: vols 3-5 now downloaded (image-only PDFs, verified as Mo'in's edition from title pages and the Latin footnotes) and OCRed locally. Image-only scan OCRed locally with tesseract 5 (fas.traineddata from github.com/tesseract-ocr/tessdata_fast, stored in incoming/_tessdata). *_pages.txt = 'fas' model (best for Persian); *_pages_faseng.txt = 'fas+eng' model (better for the Latin-script Pahlavi/Avestan etyma, worse for Persian). Pages separated by \\f; leaf N = N-th \\f-block 0-based = PDF page N+1. Search with short substrings and tolerate OCR errors. Provenance caveat: picofile is a general file host, the uploads are not from a library; treat as a grey copy (the book is in copyright in Iran). | vol 4 (م–ی) OCR text, tesseract fas+eng, pages tagged [pdf page N], printed = pdf+1917 | vol 5 (ta'liqat) OCR text, printed = pdf-5 | vol 3 (ش–ل) OCR text (689/721 pages), printed ≈ pdf+1203..1209 | BQT_v2_pages.txt: printed page = leaf + 540 (verified by catch-lines at pp. 838-855, 869, 904); earlier estimate +543 was 3 pages off.",
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


## [2026-09-14T00:52:00.218Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i in range(642,647):\n    print('======= IDX',i)\n    print(pages[i][:900])\nEOF"
}
```


### [2026-09-14T00:52:01.255Z] TOOL RESULT

```
======= IDX 642
پلاث - بنتح اول و انی بروزن قلك ؛
پلك چشم را گویند- و بمنی آوبخته هم آمده
است, وبفتح و کسر اول و سکون ثانی هم بمعنی
اول است و آن‌ر! لحاف چثم‌نیزمی گوینده ودربی
حفن خوانند . #
پلکه - بنم اول و نانی و فتح کاف »
بمعنی طعنه وسرزنش و مخنان درشت نا قیمده
گفتن باشد - و سخنان کناید آمی ز که استتباط
ممانی بد از آن توان کرد بکسی گفتن » وپلکن
هم‌بنظر آهده است که بجای ها نون باشد.
بلم بفتح‌اول وسکون انی‌وميم. خالرا
گویند . و عربی تراب خوانند .
پلمس > بروزن کر کس, :مهد یضرا
شدن ودست و با گم کردن - و ءتهم ساختن -
ودرو غ گفتن باشد ۷ .
پلمسه بروزن وصوسه ؛ «معئی بلمی
۱ تر مضطرب شدن و دست و یاکم کردن -
وحتهم ساختن- و دروغ گفتن باق . ۲
‌ غ ک ۳ آن نوسند تا اطفال بخوانند -
ویممتی دروع غم گفتن و بهانه کردن- وتهمت‌نمودن
و متهم ساختن - ودست و پا کم کردن هم شظن
امه ای ۳ ۰
بلنگ بفتح اول بر ون خدنگه ۰
از رنگي
جانوری است معروف ۴ - و توعی
کیوتر باشد -
وجانوری‌هم هت
دشمن شیر
است ۴ -وجانوری
که‌آن,ا زرافه هم
میگوند ۵ و
======= IDX 643
اطراف زمینی را گویند که در میان آن زراعت
کرده باشند و مزارعان بربالای آن اعد و شد
۱ زراعت پانمال نگردد ۲ رععتی ی کنو
آن پل مانتداست ی و رت وی
آمده | حت حد بشتوارءٌ کامر | ند کو تن
وم سس » بروزن فلوس, مخغف چاپلوس
است که فر دادن سمرب زبائی باشد .
پلو لك - بنتم اول و تانی بواو عجهول
رسیده و بکاف زده, غرفه و مخارجه و تالاری که
۳2 ی
ام راف زمن 2 1
پلو نده هبروزن شرمنده» بته قماش‌را
کومند وجربی رزمه خوانند .
یله بنتح اول و انی مخفف » بر وزن
ومعنی فله است که شیر حبوان نوزاییده باشد -
و نام درختی است خودرو که بر کش
آدمی و کلش بناخن شیر میماند » و بیخ آن
۹ سیاه و ب رکه آن تارنجی میشود ؛ و در
جنگلهای هندوستان بیار است- وبیعنی بناعت
فلیل واندك هم‌هست - وموی اطراف سر را نیز
گویند. وچوبکی که ربسمان بر کمر آن بندند
و کفة ترازو را هم گفته‌اند - و بکسر اول و فتح
ثانی‌مضفف بروزن صله» ابرشم بود- وأنجه کرم
ابرشم برخود تنیده باشد ؟ - ودرخت بیدی که
۱ -ر4 : یلوان. ۴ - راد: پله.
0 هم فریزندی و برنی 06118 « 4
و
======= IDX 644
بیان هیجد هم (۱)
در بای فارسی با نون مشتمل بر شصت ودو لت و کنات
واعمالی که بجهت دفم چشم زخم کنند- وبمعنی
پوشیده و پنهان هم آعده است و بلغت زند
وپازند (۲) پارچه ای باشد چهار کوشه که در دو
کوشة آن دود دوژند ومتابعمان زردشت دروقت
خواندن زند و پازنه (۲) و اوستا آن را برروی
لین « بفتح اول وسکون ثانی» بمعنی اما
وبممنی لیکن باذد.
لنأث « بروزن سواد ؛ بمعنی هوا باشد
وزمن کرده است . خود ندند ۷ .
ودبیر و نوسنیه را گوبشد - وتار ابریشم را ثبز ورخت را گوشة .
گفته اند - و بضه مانندی باشد از رسمان
خش که دور دوك بچیده شود - و ماشوره را
نیز کوبند.
بنام بفتح أول بروزن کلام ۰ تعویذی
ناه ۴ - بفتح اول و الی بالف کشیده
و بهاء زده» بمعنی حمایت باشد- وسابة دیوار را
نیز پئاء گوبند - و امر بدیین ععنی هم هست
یعنی یناه ببر وپناه بخ
ناهد - باها ودالابجد بروزن‌صباحت.
0 در اوستا 8202 - ۳2101 , در هازی 0 , 024۳70201 و 27110 . در
کرد بان بشت مسمعنی جامه‌ای که درزیر زره دوشند» آمده؛ در لگ د4 وندید اد بند ٩‏
ینام جزواساحه 
======= IDX 645
کردیدن. و ا زکسی بی‌موجب برربدن‌هم؛ 9
نبه کر دن هد کنابه از گررشتن -
و آریزایدن- وپرشان وپرا کنده ساختن‌ومتفرق
گردانیدن باشد - و کنایه از خاموش کردن -
و دقم و محو لمودن - و منکر شدن- و علجز
نعتی دنام هی آور ‌ ۱ ۰
بناهنده؟ بی وزن پرا کنده» بمعنی 1
پتاه گر نده باشد.
بناهیك » بررزن دوانید , یعنی یکی
یناه آورد +
پناهیده- بر وزن جفا پیشه ۰ بمه‌نی گرریدن هم هس .
داب زوا هکره پنبه کی - بنم کاف امر است ‏ یعنی
محو کن- ومنکرشو - و خاموش باشسوبگویز .
پنبه بز » بنتح اول و بای ابجد بروزن
کنده‌یز ۳ حلاج و تداف وشه ژترا گوینث.
پنبه در گوش کنابه ازمیدم‌غافل
وسخن لاشئو باشد .
بنبه در گوش نهادن. , پبه در
"وش افکندن ,پنبه در گوش گردت؛حر‌يك
ممتی دارد که کنابه از غفلت داشتن و سخن
ناشنوون باشد . ۱
فنبه‌دن - بازای هوز بروزنک رکدن,
حلاح ونداف را گوشد ِ
نب ششان «بمنی‌نرم وساف‌وسفیدشدن
باشد - و کنابه از گربختن وعتفرق و پرشان
پنبه نهادن - کنایه از فرب دادن
باشد و کنایه ازراضی ساختن کسی را در امری.-
بابجابی روانه ک
======= IDX 646
یتجاب
پنجاب. بر وزن کنجاب » ولابتی
است از ندوستان. که لاهود و توابع آن
باشد ٩‏ . 2
دوچت انگشت ه معروف است- و نام
نبانی هم مت که آن‌ا دلاشوب خوانند و بوته
و درخت آن در کار رودخانه ها روید و ب رگ
آن ماتنه ب رک شاهدانه باشد و آن را عربی
دو خمة اوراق و ذوخمسة اسابع خوانند و تخم .
آن را حب الققد کوبند و در علت اسشت بکار
مرند؟ - واشثان را نز گفتداس ونام موضنءی‌هم
هست تزدباگ بمراة تبربز» و بحذف همزه هم
بنطی آمده است که ننجد
آن فنجکشت است . اکر شهوت برزنان غلبه
کند قدری ازآن در زین آبدان دود کنند در
حال نشفاند. #۶
بنحاهه بروزن‌نکم‌اهه. مدت‌اعتکاف
صاری است و آن پنجاء روز می باشد چنانکه
چله‌اهل اسلام چهل‌روز است ؟.
پنجیا- با بای فارسی
خرچنکه را کویند. و آن
جانوریست که در آب و در
خشکی هسر دو می باشد
و بعربی سرطان خوانند -
وبرح‌چهارم است ازدوازده عنجپا
- آمروز بها کستان تعلق‌دارد ۰
تب باشد و «عرب
بالف کشیده »
۴ - یی از چندین چله درعهد می‌سال
وا
بنحبا پكث ‌ بفتحتحتانی وسکون کاف»
بممتی بنجیاست که -رطا
```


## [2026-09-14T00:52:37.121Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\np=pages[648]\ni=p.find('پنداوسی')\nprint(p[-1400:])\nEOF"
}
```


### [2026-09-14T00:52:38.302Z] TOOL RESULT

```
خیال و تخل
پنداشتن ٩‏ - مک اول اش بزنن
مگذاشتن » بمعتی گمان بردن و ور کردن
باشد و بمعنی عجب و نکیر نمودن هم آمده
است . 4
ندش منم اول و فتح الث بروزن
کس کش کلولة ثبةٌ حلاجی کرده را کوشد.
باشك .
بلفت زند و بازند ۱ .
قنك ۵ ع بکس اول و سکون انی و فتح
. ظ , ینجوبه . رگ: الفهرست سص ۳۳۸ ۱۹ ۶« ششویبه» بجای «ینجوبه»‎ - ٩
۳ - رنده‌بوده. و ۳ پهلروی۳21001.]برانیباستان 2۸ (راء) «بارتولمه ۸۷ بارسی
باستان! 311 (راء), سااسکربت 4)1980, ارمنی10119, استی1300 (میلء آرزر) <ا-عق۰۳۳۰
«نیب رک ٩۲۹یس‏ اصللا پندیممنی راء است و مجازاً پنددادن بمعثی نشان دادن راه و دوش اینتی
4 وراوستا بمعنی بیراهه‌است. «فاب ۱ : 2۵٩‏ . ۴ اسم‌از پنداشتن (ه .م).
۵ پپلوی 25420 620 2 « اسنق۳۳۱ 6« نبر که ۵۲*سعنی چنن فرض کردن!
تر کیب‌اسم وفمل. ازضمیر نظیر دارد [ُرك : زنهاره وتبعات ابرانی. دار هستتر ص۲۰۸ ».بنداشتن
در ادبیات فارسی درست بمعتی لغوی خود سنی فرش کردن وانگاشتن ۳۹ خیام گوید:
چون نیست زهرچه صست جزباد بدست چون هست بپرچه هست تتصان و شکست
انگار که هرچه هست در عا کت پندار که هرچه نیست در عالم هست.
« [ کنیز جمفید پس از نوشیدن شراب] سر بربالین نهاد و بکثبانه دوز بخفت * همه
پنداشتند که کاراو باخر رسید» چون‌از خواب درآمد ازدرد شفیفه هیج‌اثری‌نیافت.» «نفابس‌الفنون
قم اول‌در علوم اواخر ص۲۶۰۱» خواجه عبدالله اضاری کوید : خدایا ! پنداشتم که ترا شناختم »
اکنون پئدار را در آب‌انداختم .» سعدی در گلستان؛
ته‌ییند مدعی جز خویشتن را که دارد پرده پندار در پیش .
٩‏ - هز ۳200200 , پهلوی ۳228740 , فرزند « بوتکر ۱۷۰ 4 ۰
0 پنداوسی ‏ رك : پیداوسی .
```


## [2026-09-14T00:52:38.664Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN panj/pand\"; grep -n -i \"panǧ\\|pang\\b\\|pand\\b\\|pañǰ\" HRN.txt | head -20\necho \"=== NYB pand\"; grep -n \"pand\" NYB_vol2_glossary.txt | head -20"
}
```


### [2026-09-14T00:52:38.733Z] TOOL RESULT

```
=== HRN panj/pand
286:pand auf qand^ was man kaum damals qend aussprach, zu
1135:aw. spenta- heilig ; phlv. spand, arm. LW. spand
9194:ap. aw. nyäka- *Grossvater , vergl. ap. apangäka'
17860:pand- 176.
=== NYB pand
375:amahraspand [^mhrspnd] the circle of the six divinities Vahuman, Art-/Urt-/vahišt,
378:darmat surrounding Ohurmazd, himself reckoned as the seventh and the sum and substance of the group (enumerated 3919): 1. sg., of an individual divinity: cigón =--ē [~+1] as an Amahraspand, of Zartuxšt 382”; Vahuman ~ 561. — 2. pl. a) cas. rect.: amahraspand hem 39°; with enel. copula 2nd p. pl. —-& 58’; subj. of an intrans. pret.: raft hénd ~ 5812; —
380:639. 742. (after hämöden). 8922, 919. 992.5; — the agent of a pret. pass. 3822, 3919.21; — dir. obj. of an inf. 857-11, of a trans. pret. pass. (mixed act. and pass. construc- tion) 7621, 772; — governed by a prep. 1222, 3918, 43? ete.; — for the cas. rect. pl., be- ing the subj. of a vb. in pres. 104%. — Av. (145 sq.) amasa- sponta-; Paz. amešāspand (or similar forms), Skr. v. transliterates, or translates amara-guru; MPrs ’mhrspnd’n ‘the elements of Light’; as to -š-: -hr- v.s.v. ahlav; Av. amoša- < *a-mrta-.
406:Amurdat [’mwrdt'] one of the Amahras- pands (g. v.) 391%. 6919. — Av. (143 sq.) Amearatat. Paz. Amerdid, NP Murdād, the name of the šth month of the year and the 7th day of the month.
410:B. an(ē) combined with a pers. or dem. pron. or referring to the subj. implied in a verbal form has a partly distinctive, partly emphasizing sense: an man né Zartuxst fröt barišneh sahet to me it does not seem convenient to send down Z. 3911; 57%; tō dānē kë anē amahraspand
413:Amahraspands 397-8; an amäh u Pw!] Gi 6 ham tuxšem [this reading should. be restored] andar äp, andar damik, andar urvar, andar gospand we and he will labour jointly in water, soil, plants, cattle 3915-16; an-ip to ... fräc vēnēnd for thee (dat. ethicus: thou mayest know:) they prophesy ... 51% (v. tē and -p); an 6 amäh asp vāzēnēt you there, bring the horse here to us 541° (cf Spanish nosotros, vosotros); an či gäv that (re- markable) bull 427. 49?-5-18-19; ang [ZK-y] či asp that (remarkable) horse 491’; an če that very man 5419; an alone for the Ist p. sg., v. the next w. — Av. (135 sqq.) anya-, ainya-, OP aniya-; MPrth ny; MPrs ^», "ny ‘another’ (also = 2an); Paz. han, with -c: hanica. In J-Prs hm, ’ny emphasizing a pron. as described above, v. Mackenzie, An early Jewish Persian argument (BSOAS XXXI, 1968, 249-269), L, 1. 14 (p. 262): whny "wy dd dyh ‘and He is the lawgiver’ (hesitatingly combined. with ^ny by M. p. 254); Utas, The Jewish- Persian fragment from Dandàn-Uliq, Or. Su. XVII, 1968 (1969), 129, 1. 13: ny man simply = ‘T, Ll 4: ny mr = anë mara ‘for me’. — Cf also änöd and. enyä.
491:?apak [LWTH] 1. a) adv. together: (ka- nicak virtual dat.) andar ham Sap ~ bit in that same night he was together with the girl 16!-?; referring back to an encl. pron.: sih (restore the reading “30”, v. 28th) 4-$ ~ pat asp which was with him on the horse 8? (v.s.v. i and ef andar); Sih-& ... —-aš pat asp nišast estat 89: as prepositions do not govern an encl. pron. ~ must be the adv., and -aš refer to the following pat asp or to the whole sentence. — b) prep. together with, with, in all its senses, passim; in spite of 118; ~ man 5?*; ~ amäh 19, ~ smäh 1918, ~ disin 82; ēvak ~ dit with each other 7818. 799. 1071, — 2. adj. prostrate, knocked down, lying on one’s back: čvak apar, ~ dit, apar ēstūt hend o en kar they set about this act (making coition), the one above, the other lying on her back 4314-4; ka Ahriman ~ A. being knocked down (lying senseless) 914 (the enel. -4 after ~ belongs to the following, taking up the preceding subj. Ohurmazd which begins the period), a wordplay — not understood by the Pazandist — with — hämöden yazdan u amahraspandän |. 5—6, the first
558:apa-zär [’pz’l] 1. adj. mighty: —-góspand whose cattle is powerful 588-13, 6014. — 2. subst. power, predominance 84°; cos- mic, heavenly force 89?7, 922. 1061; mili- tary forces 121157; — ~ u frahang power and teaching powerful teaching 108!%-!!; nök- having new force, renew- ed 1122-12, — < *upa- (or api-, v. apa-) züvar, v. zävar and zor; MPrs ’bz’r, hw?bzr *very mighty'. Often confounded with the late form avzār < apacār (g. v.), hence the erroneous Skr. renderings by Sastra ‘arms’ (Mx, SGV, but 845 sädhana). — FrP, Cod. P, fol. 7^, with the NP gl. qudrat.
570:äp-eihrak [’p'-cyhlk'] containing the seed of the waters 87°; àp- u damik- u urvar- u gospand-cihrak containing the seed of the waters, the earth, the plants and the cattle 8711. — Av. (103 sq.) af$-cidra-; v. cihr and -cihrak.
655:Art-vahišt [?rtwhšt'] 402; Urt-vahiSt Pwrtwhst'] 39%,  A&a-vahist [?šwhšt'] 394-5, 401-4, 589. 593, 9727 one of the Amahraspands (g.v.). — art, urt < OlrSkr rta- ‘the right cosmic order, the divine law’, Av. (192) arata-, (349) orota-, (229 sqq.) aša- + vahista- (v. vahišt) 'the best, the heavenly law'. Asa-vahist is directly borrowed from Av. (233 sgg.); also the name of the 2nd month of the year and the 3d day of the month; MPrs ’rdywh<yst> Sogd. 2771; NP ardi- (urdi-)bihišt. Cf ahlav, ahläi, artči; Arta-xšahr "he whose dominion is (de- termined) by the divine law’.
1123:cigon [cygwn] adv. and conj. A. interrog. adv. how? 1. direct interrogation: nun ~ kunom ?] 272; asmān ~? 921; exclama- tory: how...! 614. — 2. indirect inter- rogation: äkäh hom ku ~ hän 571; vēnēt ki Bastvar kārēcār ~ nev kunēt saw how valiantly B. fought 2815-16; ~ 6, 6 ham pursem 57°, andar Garodman dätistän ~, api-m nē dit 527-3; ete. — B. rel. adv. so as: l. har 3 šap x"amn ~ dit Estät ... guft such as he had seen it 2%; 215, 48, 520, 4527, ete.; introducing quotations: ~ den göbet 387, ~... paitāk ku 4571-5, etc. passim; parenthetic, e.g. 7718, 818%; — with a demonstr. antecedent: hamgönak hast ~-am guft 1216-17; šmāh bat ētūn m to gobeh 2329; 4524-25, 782.4, etc. — 2. with- out a clause, used prepositionally: as, as (for instance), as it were, like: ~ agäh aköc martom 2678-27; ~~ martom kë šarm 43913; 12813; varcāvandān i ~ Yam u Frétón ... 45°; hàn 4 ~ én such a th. 438; namely 1078; — with a demonstr. antecedent: &ön ~ āluh-ē 9%; eton ~ to 1516; ét6n but ~ amahraspand-ē 38°”; — čton, or ógón, homänäk (a. v.) ~ 69%, ete.; mänäk(k)äi (g. v.) i õi ~ ke pus... bare (opt.) 418. — C. conj. 1. causal be- cause: ~~... hdn mazantom bit 613-4; 1081. 11812; almost as a rel. pron. with a sec- ondary causal sense (as in Lat. quippe qui): 6 xuähar i x*"e$, ~ zan 4 Artaxsér būt, nämak nipišt 822; 718%, 7916. 116%. 11819; — hac han ~ in view of the fact that, considering that 38. — 2. temporal as soon as: 6°. 15°. 44°, more emphatically ham-~ 1317. - 3. ~ ka as if 11214.17, 10120722 — 4. almost = that 8722. — MPrth cw'gwn; MPrs ewn (read ci'on < *ciwön <
1130:-cihrak [cyhlk'] = cihr used as the last element of an adj. compound, v. dp-~, damik-~, gospand-—, mart6m-~,urvar-~. Cihrāzātān [cyhl’c’t’n'] patron. 116". — From n. pr. C?hrāzāt, ci āzāt.
1645:giv [TWR”; g’w'] bull, cow, with the indef. art. —-č [TWR’-+1 458]: passim; ~ 4 ēvdāt (g. v.) 10418; öisän ~ these cows, dir. obj. 42%; pl. cas. obl. —-ān [TWR?--n'] gen. 482%. 4911, 861, 899. 905.6; gen. part.: dian ~-dn 2 425; —-din u gēspandān ... ēvakē vak 80?-3; dir. obj. 4825-26; instead of cas. rect. 495 (gl.); — ~ [TWR>] póstihà 107°, ~ [g’w'] pöstiyänihä ox-hides 110%, v. these ws. — Last element of proper names: Bér-~ Gafr-, Kartar-, Névak-, Purr-, Ramak-,
1655:gēhān [gyh’n'] pl. and coll., the world of creatures, men and animals, esp. the world of man: astömandän ~ 3913; han 4 mänisnömand (q.v.) göspandömand ~ 5714-15; herds of grazing animals 4913; — the material world in general: 21. 418 etc. passim. — < *gaidānām, gen. pl. of Av. (476 sqq.) gaēdā-; OP gai0à- “live-stock’; Aram. lw. (Targ, Talm) gyty ‘herds’; MPrth gyh (< gaia) ‘world’, pl. gyh?n ‘worlds’; Paz. geha; NP gehän, gihän, jihän. Cf gétah.
1698:göspand [gwspnd; KYN?] cattle in gen- eral, but esp. small cattle, sheep and goats, as distinguished from horses and cows, coll. 381%. 3916 ete., pl. cas. rect. 9417.20, 10416; pl. cas. obl. —-än 1” [KYN^-n'] 45%. 802. 861%, 893. 905-6, 943. 9724. 981, 1028; — apazär-göspand v. apazür. — Av. (506) gaospenta-; Paz. gospand, NP gospand, gosfand.
1699:gospand-cihrak [~-cyhlk'] containing the seed of cattle 879, — V. cihr, cihrak: cf ap-cihrak, gö-cihr.
1700:göspandömand [gwspnd’wmnd] posses- sing abundant cattle 57%,
1750:h- (HWH- ; 3d p. sg. "YT', neg. L'YT', inser. and Ps. ^Y TY, L'YTY 2nd p. pl. enel. -ét in amahraspand-é 58"; forms v. I, 175] to be, only in the pres. ind., subju. and opt., other forms from bütan (q. v ): l. as an independent vb. in the 3d p.: exist(s), e.g. hast hàn ke ahlayeh the One who is Righteousness exists 57°; héc ke but hénd u hec ke bavénd u h&c ke hend all who have been, and all who will be, and all who exist (now) 6417-18, cf subst. hast and nesteh; im roc 7 mähakän hast tdi ... to-day it is seven months since 1011-12. kë hast ke ...? who is there who ...? 257-7; andar Ērān-šahr asvār-ē nest ke ... in Eran-shahr there is no horseman who ... 15; hast 4-8 ... u hast 1-§ ... u hast i .. . there is some (of it) that ... and there is some (of it) ... and there is some (of it) that... = part of it... part of it... ete. 9317-18.26; hast kč-š veš, hast ké-§ kam some have more, others less 96°; astömandän mar- tömän (gen. part.) hast i ... of earthly men there are some who 10519; hast <a> šāhān šāh, hast <i> kesar some belong to the King of Kings, others to the Emperor 11519-20; nē hast kū there is no place where, nowhere 611°; hast (i) ka there is a time when, sometimes, at times 7725-26, 8122, 12018-1?; — with prev.: šusr i Gayomart cis andar hast there is some part of the sperm of G. in it 9422-23; kū-š ataxš andar nést where there is no fire 3721, — 2. copula, with a noun, a pron., or a prep. -- subst. as its complement, pas- sim; the 3d p. sg. ‘is’ is very often not
1766:could come 41-12; (Hutös) ke ... 30 ~ zāt estet H. of whom 30 children were born 2423; xrafstr + pat došaxu ~ xtartan dahénd noxious animals of which they give them to eat in Hell 769-19; 4 dmécisn kē martóm ~ the four '(complexions" of which man consists 1200-11. 4 A of which (are the following facts), “inter alia" 11012-13, — 2. replaces hac + the 3d p. pron.: Artaxsér ~ zat A. was born of her 272; 148. 164. 192. 489.14, 49%, 685. 742. 10819. 109%. 1125; ~ ... ~ part of it... part of it 11022-28; with a generic reference: 100?" (of women). 95! (from the plants). 1028-? (referring to the pl. göspandän); v. also haciš-kas, haciš-mas; — rarely, through full association with the encl. pron., hac-išan 5418 (heš?n'). 1018 (MN-š'n', text uncertain). - In BP haciš coincides graphically with api-š; all haciš found in this book are listed above. A certain confusion occurs: apt-š written MN-S (instances v. s. v. āvēntšn); in Paz. often azaš for api-š and awaš for haciš.
1842:ham-karpéh [hmklpyh] the quality, or state, of being of the same form, or shape, as another: pat ~ % amahraspan- dàn as being of the same shape as the Amahraspands 38?6, with the gl. kū etón būt cigon amahraspand-ē. — V. karp.
```


## [2026-09-14T00:52:48.360Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"### HRN around pand\"; grep -n \"pand\" HRN.txt | head -20\necho \"### HUB panj/pand\"; grep -n \"panǰ\\|panj\\|pang\\|pand\" HUB.txt | head -25"
}
```


### [2026-09-14T00:52:48.465Z] TOOL RESULT

```
### HRN around pand
286:pand auf qand^ was man kaum damals qend aussprach, zu
1135:aw. spenta- heilig ; phlv. spand, arm. LW. spand
17860:pand- 176.
### HUB panj/pand
361:80. Zu aspand *Raute' vgl. afgh. LW. spanda the wild
1796:kleben (daspanda *klebrig , Gazoplyl. s. v. viscose) =
2884:pr. 3. pi. Osnupand (lies dsnavand) Gl. and Ind. p. 30
3765:ayar *Helfer 2). Zu np. Isfandyar vgl. phi. Spand-
3770:173, Dink art V, 19, arm. Spandiat Sebeos 30,
3771:Aspandiat Mos. Kalank. I, 372, 378, 382—384 .-=
4299:hfandydd = phi. Spandydt, arm. Spandiat^ zd. spenfoddta-
4318:paz. phi. Maraspand^ arm. Maraspand^ zd. mqdrem spentem;
4385:im Pehlevi: np. panjum *der fiinfte*, paz. panjum Min. Gl.
4386:155, phi. panjum Gl. and Ind. 107 = zd. pancama-; haftum
4554:vor h und r. Ausserdem: Spandaramet (fiir gr. /liowaoQ)
4555:= zd. speflta CLrmaiti, np. sipanddrmaS, syr. Ispanddrmed
4630:np.yaw/ *fiinf, zd. pandadasa 'fiinfzehn*; pOr *das vergangene
4651:Np. paz. phi. Maraspand (Noldeke, Tab. 362, Shk.
4652:258, Gl. and Ind. 209), arm. Maraspand (Mos. Kal. I, 258)
6042:braue', skr. bhrU'\ aspand (isfand) *Raute', arm. spand, zd.
6131:axsa^na-; s/jdow/ 'Ruheplatz, Gasthaus*, phi. aspanj^ arm.
6155:anl. sp, st, sk etc. geblieben ist 2) (vgl. Spandaramet, Span-
6156:daratj Spandiat^ Spram, Stahr u. s. w.); pazend durust
6223:p. 224) ; dastvdna — dastbdna 'Armspange' JRAS. 1894, p. 461 ;
6228:Vein*, phi. apecak oder apejak; abranfan *Spange* = avranjan
6289:pand *Raute* H. 80, gospand Kleinvieh' H. 942 ; supar Tflug
6293:siparl Vollendet' H. 703, oben p. 73; sipanj *Ruheplatz'
6739:'Zaum* (= Zahn-band) ; aspand Raute' = phi. spand Bdh.
6740:p. 28, Z. 12, arm. spand, zd. spenta- ; gospand Kleinvieh'
```


## [2026-09-14T00:52:54.256Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"^176\\.\\|^ *176\\.\" HRN.txt | head\necho \"---context\"\ngrep -n \"Rath\\|Rat,\" HRN.txt | head -5"
}
```


### [2026-09-14T00:52:54.317Z] TOOL RESULT

```
1935:176. {7)~hän *Herr*), -hütend, -schützend (Comp.)', -wan,
10976:176. sar^mr 'Helm'.
---context
4941:Wahrscheinlich gehört np. enderz 'Rat, Ermahnung*
6343:aw. sax'Ore (Y. 29, 4), säx^em (y. 53, 5) ('Plan, Rat,
```


## [2026-09-14T00:53:00.586Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('HRN.txt',encoding='utf-8',errors='replace').read()\np=t.split('\\f')\nprint('pages',len(p))\nif len(p)>197:\n    print(p[197][:1500])\nEOF"
}
```


### [2026-09-14T00:53:01.715Z] TOOL RESULT

```
pages 412
— 176 —
790. suma 'ihr.
aw. ynsmäka-, gä»*^. /smäka- euer; päz. suma; ai.
yuämdka-; arm. yer 'euer (H. No. 176).
oss. d. sinaxy t. suma/ ihr, euch' (225); bei. savä-
"\\\v\ saraiy 'euer (365).
791. stifnar *Zahl, Anzahl', summden (mit her- erzählen*).
g. simärtmün; Kä§. V. veresmörtdn , Q. öresmärdeff^
K. esmördemün, Z. veresmdrt^),
aw. I/"r/?ar-, märay^iti 'bemerken, sieh merken*
(y. 32, 6); phlv. sVmär (vd. 9 (132) Gl.), vergl.
ösmartan^ ösmar (Bund.), anösmär 'ungezählt' (Men. 49,
22); ai. {^smar- gedenken'.
kurd. azmardin (H.-Sch.), zimärtin zählen'.
np. sumurden (gegenüber ämär^ mer) ist aw. aim-r-
mar- {aiwisrnaretö), das allerdings yt. 14, 34 eine ganz
andere Bedeutung hat; np. nehmür 'zahllos hat die
ursprüngliche Form der Wurzel, smor-, am Besten
erhalten. Wegen phlv. ösmartan darf bei sumurdmi
nicht Entstehung im Satzsandhi angenommen werden.
792. sinä, sinäh 'Schwimmen', sinär, sinärlden.
aw. l^snClr, US snayaeta 'sich waschen'; ai. l^snä-,
sndii- 'sich baden.
oss. t. nähi 'baden', d. a^snun^ t. a^snin 'waschen*
(196).
Die Nebenformen sinäb^ sinäv, sinävtden erklären
sich entweder wie deryäw (No. 561) oder sie gehen
auf [/^S7iav' {gi\ vsio 'schwimmen', äol. raa», vavftt
'fliessen') zurück.
np. s ist im Satzsandhi oder durch Übertragung
entstanden.
793. Hnäyiten 'erkennen', Praes. sinäs-efn, shuls.
ap. /snäsatiy 'solle kennen'; phlv. snäxtav, sfinaPf,
snäsüntän.
kurd. 7fäfiin 'erkennen*, ez dinäsim.
Gehört zur arischen [/'San- (wie ap. adma, np.
*) Nirgends findet s
```


## [2026-09-14T00:53:10.034Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"pend\\b\\|pend \" HRN.txt | head -20\necho \"=== index context 17850-17870\"\nsed -n '17850,17870p' HRN.txt"
}
```


### [2026-09-14T00:53:10.098Z] TOOL RESULT

```
1134:80. espend 'Raute', esfend, isfend, spend,
3131:330. pend *Rat\
3630:pend-l tu büved düröy ü ter/end
4803:aw. düiiiö.^karsa' 'körnerschleppend'; phlv. dänak;
12403:yöspend 942.
=== index context 17850-17870
päAÄadOQa 280.
paAcäaät 329.
l/po(-, ndtaii läS.
iMffi- 188.
-pa(.'- 188.
pithan- 33a
jMfd- 346.
jHKiif- 346.
padaii- 847.
;ii'[id^fA:a- 847. '
pand- 176.
parn- 158, 271.
[- 342.
r ;- 276, 1070 Am
parxikii- 277,
päcO' 87.
piidr. 286.
piti -- --
p^foa-
par- + ud 697.
+ M». 111.
```


## [2026-09-14T00:53:15.334Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '3110,3160p' HRN.txt"
}
```


### [2026-09-14T00:53:15.412Z] TOOL RESULT

```
Bartholomae stützt diese Erklärung brieflich
*) Das Wort ist nicht allzu gut beglaubigt. Die anderen Wörter-
bücher belegen es gar nicht, nur der FR hat folgenden Vers Leblbl's
(Metr. Muteqärib) mit der Aussprache bis^ :
be^enjer heme tens^ enjlde end
ber an /äk^ /üues bisetijlde end
2j Nie pul gesprochen oder geschrieben (Vullers), das nur
•Geld' bedeutet.
^) Felis pardus L. (Blanford, S. 34).7:^
durch den Hinweis auf ai. dhäna- zu dhä-^ aw. frena-
zu prä'^ aw. frä/snenem (KZ. 30, 330) zu (ai.) jüa-,
328. penj 'fünf*, penjum 'fünfter , peNje Taust'.
Kä§. hen^tö.
aw. panöa *fünf ' ; phlv. panCf pancuni^ pancdk Taust' ;
ai. pdnca ; arm. hing (H. No. 169).
kurd. panj^ penj; afy. pinja; oss. /o/y, fo'^^j *fünf',
t. fänjäm 'fünfter (292) ; wa/. j:>ä;«<e , sar. sijn. p///^,
sangl. paw2^, minj. panc.
329. penjäh 'fünfzig'.
aw. pancäsata-; phlv. pancdh; ai. pancä^dt-,
kurd. LW. penjä; af;'. panjös,
330. pend *Rat\
ap. j^at^e- 'Weg' ; aw. pantan- ; ai. pdthan- ; phlv.
/;awfZ *Rat'; arm. vergl. Aw«, didßaöig (? H. No. 172).
oss. d. /ä/K/ 'Wunsch', t. 'Plan, Rat' (273) ; bei. pant-
dea(j 'belehren, unterrichten' (282).
Vergl. Bartholomae, ZDMG. 44, 553.
831. pindUSten 'glauben, dafür halten', Praes. pindärem.
phlv. pa m dästan (ni^NI NiD pD bezw. PiliDn'« NOn p?
y. 45, 5, 6)^); Nöldeke, Kärnämak 49, Note 2.
332. penhän, pinhän Verborgen'.
phlv. pa (pO) nihan (s. No. 1058) ; Nöldeke, Kärnämak
67, Note 2.
Np. pendm bedeutet ebenfalls Verborgen, bedeckt';
es wird von den Wörterbüchern als aus penhän con-
trahirt angesehen (zu m für n vergl. bam, bau 'Dach') ^) ;
mit parsisch penäm (jpenöm)^ aw. paiti.däna-, phlv.
padäm, wird np. penäm Verborgen' nichts zu thun
*) loh orgreife diese Gelegenheit, um den BB. XVII, 261 Note 2
begangenen Irrtum zu berichtigen, dass ich auch Darmesteter die
unmögliche Erklärung des Wortes aus sem. p^ + dästen zugeschrieben
habe. Sie bleibt vielmehr Fr. Müller allein reservirt.
^) FJ und FR belegen es durch folgenden Vers Kemal Isma'll's
(Metrum: Xeflf):
bä ekäbir heniejlis ü ^elvet
guft ü göy'l penäm^ mex^ähem.74 -
haben (die Wörterbücher erklären allierdings das
erstere durch das letztere).
333. inipü, püpe, püpek 'Wiedehopf; auch hühü etc.
Lat. upüpa 'Wiedehopf; gr. snoifj.
kurd. papü (H.-Sch.), päpü (JJ.).
```


## [2026-09-14T00:53:28.502Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"### BRT panta\"; grep -n \"pantan-\\|paṇtan\\|pafltan\\|pan^an\\|panta-\" BRT.txt | head -10\necho \"### BRT 'Weg'\"; grep -n \"^• *j\\. *pa.*'Weg'\" BRT.txt | head -10"
}
```


### [2026-09-14T00:53:28.565Z] TOOL RESULT

```
### BRT panta
15668:•  j,  parat- V. 'certare'.  Praes.  2panta-'\ ^pgrvta-''',  7  (Jnt) päptni-,  iih px'ana-'\ I  s  hpffftiä-  -.ppnn-^^.      [Vgl.  noch  "parfttH
26972:•  j.,  g.  spanta-  Adj.  (fem.  'tä-)  Tieilig, sanctus';  a)  im  gAw.  (ohne  YHapt); i)  von  Göttern;  a)  von  AkM.:  yqm  ctstJm (sd.)  asa  mantä  'ts  masdä  ahurS  Y.  51.16; 2p.  7,  4S.  3;  —  'f^m  at  'kwn  mazda  m7nghl (Sp.  1173  o.)  ahurä  \.43-  5!  4;  —  ya%a %wa . .  »»jw?Ar(Sp.  43  m.)  fyao^anSi  °t»m ahurim  alavansm  ^.46.');  —  ahyll  *main- yfui  tvSm  ahl  tu  (Sp.  905  m.)  't5  Y.  47. 3 ;
### BRT 'Weg'
```


## [2026-09-14T00:53:29.238Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"### KLN punch\"; grep -n \"punch\" KLN_1966.txt | head -20"
}
```


### [2026-09-14T00:53:29.313Z] TOOL RESULT

```
### KLN punch
14805:B  pic,  Arm.  hing  (in  sense  of  the  phonetic  law according  to  which  k  preceded  by  a  nasal  sound becomes  g),  Gk.  robrre,  Aeol.  mSpre,  L.  quinque (with  assimilation  of  initial  p  in  the  first  syllable to  initial  qw  in  the  following  syllable  (see  quin- que-).  Alb.  pess,  Gheg  p?se,  OSlav.  pfti,  Lith. penki,  OW.  pimp,  OIr.  coic  (with  assimilation as  in  L.  quinque).  Cp.  cinq(ue),  kantar,  keno, Panchatantra,  panchayat,  penta-,  punch,  ‘a beverage’,  quinary,  quinque-.  Cp.  also  finger, fives,  n.,  a  ball  game  played  by  two  or  four  per¬ sons.  —  PI.  of  five.
24354:montbretia,  n.,  a  plant  of  the  genus  Tritonia (bot.)  —  ModL.,  named  after  Antoine-Fran- qois-Ernest  Coquebert  de  Montbret  (1781-1801), official  botanist  of  Napoleon’s  expedition  to Egypt.  For  the  ending  see  1st  suff.  -ia. mont-de-piete,  n.,  a  public  pawnshop  in  France. —  F.,  fr.  It.  monte  di  pieta,  lit.  ‘credit  of  pity’  (in Olt.,  monte  had  also  the  meaning  of  ‘money due’).  It.  monte  derives  fr.  L.  montem,  acc.  of motts,  ‘mountain’;  see  mount  ‘hill,  mountain’. It.  di  comes  fr.  L.  de,  ‘from,  away  from’ ;  see  de-. It.  pieta  derives  fr.  L.  pietatem,  acc.  of  pietas, ‘dutiful  conduct’;  see  piety  and  cp.  pity, monte,  n.,  a  gambling  game  of  cards.  —  Sp. monte,  ‘mountain ;  a  pile  of  cards  left  after  the first  deal;  a  game  of  cards’,  fr.  L.  montem ,  acc. of  mons,  ‘mountain’.  See  mount,  ‘hill,  moun¬ tain',  and  cp.  prec.  word, monteith,  n.,  a  large  bowl  for  punch,  usually  of silver.  —  Named  after  Monteith  or  Monteigh,  a Scot,  who  lived  in  the  17th  cent.
29235:pluriaxial,  adj.,  having  more  than  one  axis.  — Compounded  of  pluri-  and  axial, plus,  prep,  adj.,  and  n.  —  L.  plus,  gen.  pluris, ‘more’,  w’hence plurimus,  ‘most’;  cogn.  with  OI. purvi,  punch,  ‘much’,  prayah,  ‘mostly’,  OPers. paru,  Gk.  iroXtiq,  ‘much,  many’,  TtXsiojv,  tt>,£- cov,  ‘more’,  nXetctTO?,  ‘most’,  TroXXaxL?,  ‘often’, OIr.  it,  ‘much’,  ilar,  ‘crowd’,  W.  elu,  ‘much’, Lith.  pilus,  ‘abundance’,  Goth .  filu,  OHG.  filu, MHG.  vil,  G.  vie/,  ODu.  vilo,  OFris.  felo,fel(e), ON.  fjdl-  (only  in  compounds),  OS.  filu,  OE. fela,  feala,  feola,  ‘much,  many’.  All  these  words derive  fr.  I.-E.  base  *ple-,  ‘to  fill’.  See  full,  adj., and  cp.  pleio-,  poly-.
29854:pounce,  n.,  1)  claw  of  a  hawk  or  of  another  bird of  prey;  2)  (dial.)  a  punch;  3)  (obsol.)  a  hole made  by  punching  —  Prob.  shortened  fr.  ME. ponson,  ponchon,  ‘pointed  tool'.  See  puncheon, ‘stamp’.
29856:Derivative:  pounce,  n.,  a  sudden  swoop, pounce,  tr.  v.,  1)  to  emboss  (metal)  by  punching designs  on  the  reverse  side;  2)  to  perforate.  — Prob.  partly  fr.  F.  poin(onner,  ‘to  punch,  stamp’, fr.  poinpon,  ‘awl,  bodkin,  punch,  stamp’  (see
29857:puncheon,  ‘stamp’),  partly  fr.  pounce,  ‘claw  of  a hawk ;  a  punch’.
30997:puna,  n.,  a  desert  region.  —  Sp.,  fr.  Quechua. punch,  n.,  a  tool.  —  Shortened  fr.  puncheon. Derivatives:  punch,  v.  (q.v.),  punch-y,  adj., punch-i-ness,  n.
30998:punch,  tr.  v.,  to  perforate.  —  Either  derived  fr. punch,  ‘a  tool’,  or  a  collateral  form  of  pounce, ‘to  emboss’.
30999:Derivatives:  punch-able,  adj.,  punch-ed,  adj., punch-er,  n.,  punch-ing,  n.
31000:punch,  n.,  a  short,  thick -set  person;  anything short  and  thick.  —  Prob.  fr.  the  PN.  Punch  (q.v.) punch,  n.,  a  beverage.  —  Hind,  punch,  fr.  OI. pahca,  ‘five’,  which  is  cogn.  with  Gk.  news,  L. quinque,  Goth,  fimf,  OE.  fif  (see  five  and  cp. Panchatantra,  panchayat) ;  so  called  because orig.  the  punch  was  composed  of  five  ingre¬ dients.
31001:punch,  tr.  v.,  to  strike,  to  thrust.  —  Prob.  a  col¬ lateral  form  of  pounce,  ‘to  swoop  down,  to  at¬ tack’,  and  influenced  in  form  by  the  verb  punish. Derivative:  punch,  n.,  a  thrust.
31002:Punch,  n.,  the  hero  of  the  puppet  show  Punch  and Judy.  —  Abbreviation  of  Punchinello, puncheon,  n.,  a  stamp  or  die.  —  ME.  ponchon , ponson,  punson,  ‘pointed  tool’,  fr.  OF.  poinchon , poinpon,  ponfon  (F.  point;. on),  ‘awl,  bodkin’,  fr. L.  punctionem,  acc.  of  piinctid,  ‘a  pricking,  pierc¬ ing’,  used  in  the  concrete  sense  of  ‘a  piercing  or perforating  instrument’.  L.  piinctid  is  formed  fr. punctus,  pp.  of  pungere,  ‘to  prick,  pierce’.  See point,  v.,  and  cp.  punch,  ‘a  tool'.  Cp.  also  pounce, ‘claw  of  a  hawk’,  pounce,  ‘to  emboss', puncheon,  n.,  a  large  cask.  —  ME.  poncion,  fr. OF.  poinchon,  poinpon,  ponpon,  ‘wine  vessel’.  It is  probable  that  the  original  meaning  of  the OF.  word  was  ‘a  perforated  vessel’,  and  that, accordingly,  puncheon,  ‘cask’,  and  puncheon, ‘die,  stamp’,  are  of  the  same  origin.
31003:Punchinello,  n.,  1)  the  prototype  of  Punch;  2)  a buffoon.  —  Corruption  of  PolichineUo,  fr.  Nea¬ politan  Polecenella,  corresponding  to  literary  It. Pulcinella,  dimin.  of pulcina ,  ‘chicken’,  fr.  L.  pul- licena,  pullicina,  fem.  of  pullicenus,  pullicinus,  ‘a young  bird,  chicken’,  fr.  pullus,  ‘a  young  animal, young  bird’.  See  pullet  and  cp.  Punch,  punch,  ‘a short  person’,  Polichinelle. punctate,  adj.,  dotted.  —  MedL. punctatus,  pp.  of punctare,  ‘to  mark  by  points’,  freq.  of  L. pungere, pp.  punctus,  ‘to  pierce’.  See  pungent  and  cp. punctum.  For  the  ending  see  adj.  suff.  -ate. Derivative:  punctat-ed,  adj. punctation,  n.,  the  action  of  making  punctate.  — Formed  with  suff.  -ion  fr.  MedL.  punctatus,  pp. of  punctare.  See  prec.  word, punctilio,  n.,  1)  a  nice  point  in  behavior;  2)  exact observance  of  formalities.  —  Fr.  It.  puntiglio  or Sp.  puntillo,  diminutives  formed  fr.  L.  punctum, ‘point’.  See  point,  n.,  and  cp.  pun.  The  spelling punctilio  shows  the  influence  of  L.  punctum. punctilious,  adj.,  attentive  to  punctilios.  —  Form¬ ed  fr.  prec.  word  on  analogy  of  It.  puntiglioso, Sp.  puntilloso,  F.  pointilleux.  For  the  ending  see -ous.
31015:pungent,  adj.,  sharp,  piercing.  —  L.  pungens,  gen. -ends,  pres.  part,  of  pungere,  ‘to  pierce,  sting, bite’,  from  a  nasalized  form  of  I.-E.  base  *peug-, ‘to  stick,  stab’,  whence  L.  pugnus ,  ‘fist’.  See pugnacious  and  cp.  poignant,  which  is  a  doublet of  pungent.  Cp.  also  appoint,  disappoint,  com¬ punction,  counterpane,  embonpoint,  expugn,  ex- punction,  expunge,  impugn,  inexpugnable,  inter- punction,  oppugn,  point,  n.  and  v.,  poniard,  pun, puncheon,  ‘a  die  or  stamp’,  puncheon,  ‘a  large cask’,  punctate,  punctation,  punctilio,  punction, punctual,  punctum,  puncture,  puneca,  punt,  ‘to gamble’,  punty,  spontoon.
38109:tammy,  n.  —  Short  for  tam-o’-shanter, tam-o’-shanter,  n.,  a  kind  of  woolen  cap.  — Named  after  Tam  o'Shanter,  the  hero  of  Robert Burn’s  poem  of  this  name, tamp,  tr.  v.,  to  pound,  ram.  —  Back  formation fr.  F.  etamper,  ‘to  stamp,  punch’,  fr.  OF.  es- tamper,  fr.  Frankish  *stampdn,  which  is  rel.  to Du.  stampen,  OHG.  stampfon,  ‘to  pound’.  See stamp,  v.  and  cp.  tampon.
```


## [2026-09-14T00:53:43.477Z] TOOL CALL #38: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 5
}
```


### [2026-09-14T00:53:43.485Z] TOOL RESULT

```


```


## [2026-09-14T00:53:45.960Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"### KLN path\"; grep -n \"^path,  n\\.\\|path,  n\\.\" KLN_1966.txt | head -5\necho \"### KLN pontoon\"; grep -n \"pontoon\" KLN_1966.txt | head -5\necho \"### KLN find\"; grep -n \"^find,  tr\\|find,  tr\\. and  intr\\.\" KLN_1966.txt | head -5\necho \"### KLN fist\"; grep -n \"fist,  n\\.\" KLN_1966.txt | head -5"
}
```


### [2026-09-14T00:53:46.064Z] TOOL RESULT

```
### KLN path
2293:allopath,  n.  —  Back  formation  fr.  allopathy, allopathy,  n.,  treatment  of  disease  by  remedies that  produce  effects  opposite  to  those  caused
17971:homeopath,  homoeopath,  n.,  homeopathist.  — Back  formation  fr.  homeopathy, homeopathy,  homoeopathy,  n.,  a  system  of  healing based  on  the  theory  that  a  disease  can  be  cured by  medicines  which  in  a  healthy  person  would, produce  symptoms  similar  to  those  of  the  dis¬ ease  treated.  —  G.  Homdopathie,  coined  by  the German  physician  Samuel  Hahnemann  (i755_ 1843),  the  founder  of  homeopathy,  fr.  Gk. 6poto7raf>eia,  ‘likeness  in  feeling,  likeness  in suffering’,  fr.  opoiop,  ‘like’,  and  -7taffeia,  ‘feel¬ ing,  suffering’.  See  homeo-  and  -pathy  and  cp. allopathy.
18368:hydropath,  n.,  a  hydropathist.  —  Back  formation fr.  hydropathy.
25038:naturopath,  n.,  naturopathist.  —  Back  formation fr.  naturopathy.
25328:Derivative:  neuron-ic,  adj. neuropath,  n.  1)  one  who  suffers  from  nervous disease;  2)  a  neuropathist.  —  Compounded  of neuro-  and  Gk.  -radr,;,  fr.  TraSoc.  ‘suffering’.
### KLN pontoon
14754:rel.  to  OS.  findan,  fithan,  ON.,  Svted.finna,  Dan. finde,  MDu.,  Du.  vinden,  OHG.  findan,  fintan, MHG.  vinden,  G.  finden,  Goth,  fin  fan.  The  orig. meaning  of  these  words  was  ‘to  come  upon’,  fr. I.-E.  base  *pent-,  ‘to  go,  pass;  path,  bridge’, whence  also  OHG.  fendeo,  ‘pedestrian’,  OI. panthab,  ‘path,  way’,  A vestic,  pantd,  ‘way’.  Arm. hun,  gen.  hni  (for  *ponti),  ‘way,  ford’,  Gk. ttovtcx;,  ‘open  sea’,  roxxoi;  (for  *pt}tos),  ‘trodden way,  path’,  tocte&j,  ‘I  step’,  L.  pons,  gen.  pontis, ‘bridge’,  OSlav.  pQti,  ‘path \pgta,  ‘heel’,  OPruss. pint  is,  ‘way,  road’.  For  sense  development  cp. Hitt,  wemiya,  ‘to  find’,  lit.  ‘to  come  upon’, OSlav.  na-iti,  ‘to  find’,  fr.  iti,  ‘to  go’,  and  L.  in¬ venire,  ‘to  find’,  lit.  ‘to  come  upon’,  fr.  in,  ‘in, on’,  and  venire,  ‘to  come’.  Cp.  pad,  ‘road’, paddle,  path.  Cp.  also  peripatetic,  pons,  ponceau, ‘culvert’,  pontifex,  pontiff,  pontoon,  punt,  ‘river boat’.  Cp.  also  sputnik.
29604:ponton,  n.,  pontoon.  —  F.  ponton.  See  pontoon.
29605:pontonier,  n.  —  F.  pontonnier.  See  pontoon  and -ier.
29606:pontoon,  n.,  a  boat  used  to  support  a  temporary bridge.  —  F.  ponton,  fr.  L.  pontonem,  acc.  of ponto,  ‘punt;  floating  bridge’,  a  derivative  of pons,  gen.  pontis,  ‘bridge’.  See  pons  and  -oon and  cp.  punt.
29607:Derivative:  pontoon,  tr.  v.,  pontoon-ing,  n.
### KLN find
### KLN fist
14793:fist,  n.  —  ME.  fust,  fist,  fr.  OE .fyst,  rel.  to  OS., OHG.,  MHG.  fust,  OFris.  fest,  MDu.  vuust, Du.  vuist,  G.  Faust,  and  cogn.  with  OSlav. pgsti,  Russ,  piasti,  ‘fist’.  Cp.  foist.
26893:pacificatory,  adj.,  tending  to  pacify.  —  L.  pacifi- catorius,  ‘peace-making’,  fr.  pacificatus,  pp.  of pdcificare.  See  pacify  and  adj.  suff.  -ory. pacifism,  n.  —  Contraction  of  pacificism,  which  is formed  fr.  pacific  with  suff.  -ism.  For  the  short¬ ening  of  pacificism  into  pacifism  see  haplology. pacifist,  n.  and  adj.  —  Contraction  of  pacificist. See  pacific  and  -ist  and  cp.  prec.  word.  For  the shortening  of pacificist  into  pacifist  see  haplology. Derivative:  pacifist-ic,  adj. pacify,  tr.  v.  —  ME.  pacifien,  fr.  OF.  (=  F.) pacifier,  fr.  1..  pdcificare,  ‘to  make  peace’,  fr.  pax, gen.  pads,  ‘peace’,  and  -ficere,  unstressed  form of  facere,  ‘to  make,  do’.  See  pax  and  -fy  and  cp. pacificate.
```


## [2026-09-14T00:53:55.074Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"### KLN path main\"; grep -n \"OE\\. *pæd\\|OE  \\.pæd\\|pcep\\|paed,  ‘path\\|path,  n\\.\" KLN_1966.txt | head -10\necho \"### grep 'Iranian' near path\"; grep -n \"Scythian\" KLN_1966.txt | head -10\necho \"### KLN finger\"; grep -n \"finger,  n\\.\" KLN_1966.txt | head -5\necho \"### KLN five\"; grep -n \"^five,  adj\\|five,  adj\\.\" KLN_1966.txt | head -5"
}
```


### [2026-09-14T00:53:55.189Z] TOOL RESULT

```
### KLN path main
2293:allopath,  n.  —  Back  formation  fr.  allopathy, allopathy,  n.,  treatment  of  disease  by  remedies that  produce  effects  opposite  to  those  caused
17971:homeopath,  homoeopath,  n.,  homeopathist.  — Back  formation  fr.  homeopathy, homeopathy,  homoeopathy,  n.,  a  system  of  healing based  on  the  theory  that  a  disease  can  be  cured by  medicines  which  in  a  healthy  person  would, produce  symptoms  similar  to  those  of  the  dis¬ ease  treated.  —  G.  Homdopathie,  coined  by  the German  physician  Samuel  Hahnemann  (i755_ 1843),  the  founder  of  homeopathy,  fr.  Gk. 6poto7raf>eia,  ‘likeness  in  feeling,  likeness  in suffering’,  fr.  opoiop,  ‘like’,  and  -7taffeia,  ‘feel¬ ing,  suffering’.  See  homeo-  and  -pathy  and  cp. allopathy.
18368:hydropath,  n.,  a  hydropathist.  —  Back  formation fr.  hydropathy.
25038:naturopath,  n.,  naturopathist.  —  Back  formation fr.  naturopathy.
25328:Derivative:  neuron-ic,  adj. neuropath,  n.  1)  one  who  suffers  from  nervous disease;  2)  a  neuropathist.  —  Compounded  of neuro-  and  Gk.  -radr,;,  fr.  TraSoc.  ‘suffering’.
26709:Derivative:  osteomyelit-ic,  adj. osteopath,  n.,  one  who  practices  osteopathy.  — Back  formation  fr.  osteopathy.  See  -path, osteopathist,  n.,  an  osteopath.  —  Formed  from next  word  with  suff.  -ist. osteopathy,  n.,  system  of  treating  ailments  by  the manipulation  of  bones  (med.)  —  Compounded of  osteo-  and  Gk.  -ncc^eta,  fr.  na&oc,  ‘suffer¬ ing’.  See  -pathy.
27666:path,  n.  —  ME.,  fr.  OE.  pxj?,  rel.  to  OFris.  path, MDu.  pat,  Du.  pad,  OHG.  pfad,  MHG. pfat,  G. Pfad,  ‘path’.  These  Teut.  words  are  prob.  of  Ira¬ nian  origin;  cp.  Avestic  pa&a,  ‘way  ,  and  see find.  Cp.  also  pad,  ‘road’,  paddle,  pons. Derivatives :  path-ed,  path-less,  adjs. path-,  form  of  patho-  before  a  vowel.
30834:ments  induced  by  mental  processes.  —  Com¬ pounded  of  psycho-  and  motor, psychopath,  n.,  one  suffering  from  mental  disease. —  Compounded  of  psycho-  and  Gk.  -mx ■&(]?, ‘suffering’.  See  -path.
### grep 'Iranian' near path
6830:Caucasian,  adj.  and  n.  —  Formed  with  suff.  -ian fr.  L.  Caucasus,  fr.  Gk.  Kauxaau;,  fr.  Scythian Kpoo-xxcu.?,  ‘Caucasus’,  a  compound  meaning lit.  ‘(the  mountain)  shining  with  ice’;  see  Walde- Hofmann,  LEW.,  I,  pp.  295-96,  s.v.  criista.  The first  element  of  this  compound  is  a  derivative  of I.-E.  base  *qreu-,  ‘to  be  icy’.  For  derivatives  of *qrus-,  an  enlarged  form  of  base  *qreu-  see crust,  crystal.  The  second  element  is  rel.  to  Gk. y.odsiv  (for  "xifieiv),  ‘to  burn’ ;  see  caustic, cauchemar,  n.,  incubus.  —  F.,  a  hybrid  coined from  the  blend  of  OF.  chaucer  and  Picard  cau- quer,  ‘to  trample’  (both  derived  fr.  L.  calcare, of  s.m.,  fr.  calx,  gen.  calcis,' heel'),  and  fr.  MDu. marc,  incubus'.  See  Calceolaria  and  mare,  ‘in¬ cubus',  and  cp.  the  first  element  in  caltrop, caucus,  n.,  private  meeting  of  the  leaders  of  a  poli¬ tical  party.  —  A  word  of  Algonquian  origin,  lit. meaning  ‘counselor’.
10300:Danaiis,  n.,  a  king  of  Argos,  who  commanded  his fifty  daughters,  the  Danaides,  to  murder  their husbands  on  the  wedding  night  ( Greek  mylhol.) —  L.  Danaus,  fr.  Gk.  Aavaop  (whence  the  pi. Aavaoi, ‘theDanaans’,  i.e.  ‘descendants  or  sub¬ jects  of  Danaiis’,  whence  ‘the  Greeks’,  in  gen¬ eral),  which  prob.  derives  fr.  Heb.-Phoen.  Dan, and  lit.  means  ‘one  who  judges’;  see  Dan,  PN., and  cp.  Danae,  Danaides.  This  etymol.  is  cor¬ roborated  by  the  fact  that  the  myth  of  Belus and  the  Danaides  “records  the  early  arrival  in Greece  of  Helladic  colonists  from  Palestine” (quoted  from  Robert  Graves,  ‘The  Greek Myths’,  I,  p.203.  Penguin  Books).  For  other Greek  mythological  names  of  Hebrew  origin cp.  Cadmus,  Niobe.  —  According  to  Kretsch¬ mer,  Glotta  24,  15  fT.,  the  Danaans  are  identical with  the  men  of  Tanaus,  king  of  the  Scythians, who  allegedly  came  to  Argos  in  the  15th  cent. B.C.E.  and  became  blended  with  the  Greeks. Kretschmer  also  assumes  that  there  is  a  relation¬ ship  between  Tanaus  and  the  river  names  Tanais and  L.  Danubius  (whence  F.  and  E.  Danube), and  Ddnu-,  name  of  an  Indo-Iranian  people. See  Frisk,  GEW.,  I,  p.347  s.v.  Aavaot  and  cp. Albert  Camoy,  Dictionnaire  etymologique  de la  mythologie  greco-romaine,  p.42  s.v.  *Da- naos.  —  Cp.  Danae,  Danaides.
17558:hemostat,  haemostat,  n.,  anything  that  stops hemorrhage;  specif.,  an  instrument  used  to compress  a  bleeding  vessel.  —  Fr.  hemostatic, hemostatic,  haemostatic,  adj.,  serving  to  stop hemorrhage;  styptic.  —  Compounded  of  hemo- and  Gk.  oxaxixoe;,  ‘causing  to  stand’.  See  static, hemp,  n.  —  ME.,  fr.  OE.  hsnep,  henep,  rel.  to OS.  hanap,  ON.  hampr,  Swed.  hampa,  Dan. hamp,  MDu.,  Du.  hennep,  OHG.  hanaf,  MHG. hanef,  hanf  G.  Hanf(—  Teut.  *hanap).  Cp.  Gk. xawotfki;  (whence  L.  cannabis),  Arm.  kanap‘. Alb.  kanep,  Russ.-Church  Slav.  konoplja(  whence Lith.  kanapes),  ‘hemp’.  All  these  words  are loan  words  from  a  foreign,  possibly  Scythian, language.  Cp.  canvas,  canvass.  Cp.  also  sunn. Derivative:  hemp-en,  adj.
18299:hyal-,  form  of  hyalo-  before  a  vowel, hyalin,  n.  — -  See  hyaline,  n. hyaline,  adj.,  glassy;  transparent.  —  L.  hyalinus, fr.  Gk.  udXtvo;,  ‘glassy’,  fr.  oaXo;,  ‘alabaster, crystal,  amber’,  prop,  ‘a  transparent  stone’,  later ‘glass’,  which  prob.  stands  for  *sualo-.  Cp.  L. suali-ternicum,  ‘a  kind  of  reddish  amber’,  which, according  to  Pliny  37,  33,  »s  of  Scythian,  i.e. North  European,  origin.  See  Boisacq,  DELG., p,996,  s.v.  uaXo;,  and  Walde-Hofmann,  LEW, II,  61 1,  s.v.  sualiternicum.  For  the  ending  see suff.  -ine  (representing  Gk.  -ivo;). hyaline,  n.,  1)  something  glassy,  as  the  smooth sea  or  the  clear  sky;  2)  (in  this  sense  spelled  also hyalin)  a  substance  forming  the  walls  of  hydatid cysts.  —  See  hyaline,  adj.
32823:rhombus,  n.,  an  oblique-angled  equilateral  paral¬ lelogram.  —  L.  See  rhomb, rhoncial,  also  rhonchal,  adj.,  pertaining  to  arhon- chus.  See  next  word  and  adj.  suff.  -al. rhonchus,  n.,  a  whistling  sound  heard  on  the auscultation  of  the  chest.  —  L.,  ‘a  snoring’,  fr. Gk.  poy-/_o;,  which  is  rel.  to  (56yxo;,  friyyoq, ply xo;,  of  s.m.  plyysiv,  peyxEtv,  ‘to  snore’; prob.  of  imitative  origin, rhotacism,  n.,  mispronunciation  of  the  letter  r.  — ModL.  rhotacismus,  fr.  Gk.  ptoTaxiopoc,  fr. pwraxlqEiv.  See  next  word  and  -ism. rhotacize,  intr.  v.,  to  mispronounce  the  letter  r. — Gk.  ptoTaxi^Eiv,  ‘to  use  the  letter  r  excessive¬ ly’,  fr.  p<7>,  name  of  the  letter  r.  See  rho  and  -ize. rhubarb,  n.,  a  garden  plant  with  large  leaves  and edible  leaf  stalks.  —  ME.  rubarbe,  fr.  MF.  reu- barbe,  rubarbe  (F.  rhubarbe),  fr.  ML.  rheubar- barum.  The  first  element  in  ML.  rheubarbarum derives  fr.  L.  rheum,  fr.  Gk.  ptjov,  ultimately  fr. Pers.  rewend,  ‘rhubarb’  (whence  also  Russ. reven).  Cp.  the  ML.  form  rhabarbarum,  which comes  fr.  Gk.  pec  fSxppapov,  lit. ‘foreign  rhubarb’ ; px,  ‘rhubarb’,  is  a  blend  of  pvjov,  ‘rhubarb’,  with 'Pa,  the  Scythian  name  of  the  Volga;  see  roric. The  second  word  in  pa  |3xp!3xpov  refers  to  the foreign  origin  of  the  plant.  It.  rabarbaro  (whence G.  Rhabarber)  derives  fr.  Gk.  pa  |3dpj3xpov.  Cp. rhapontic,  rheum.
33106:roric,  adj.,  pertaining  to  dew.  —  Formed  with suff.  -ic  fr.  L.  ros,  gen.  roris,  ‘dew’,  which  is  cogn. with  Lith.  rasa,  OSlav.  rosa,  ‘dew’,  Ol.  rasah, ‘sap,  juice,  fluid,  essence’,  rasa,  ‘moisture’,  Rasa, name  of  a  mythic  river  (=  Avestic  Rahha), aryati,  ‘flows',  rsabhdh,  ‘bull,  steer’,  Avestic  and OPers.  arshan,  ‘man’,  Hitt,  arszi,  ‘flows’,  Gk. Sp  ary,  jipp  tjv.  ‘male,  masculine’,  prob.  also  'Pa, Scythian  name  of  the  Volga,  fr.  I.-E.  base  *ras-, *eras-,  *eres-,  *ers-,  ‘to  flow,  wet,  moisten’.  Cp. rasa,  romerillo,  rosemary,  rosolio,  rouse,  ‘to pickle'.  Cp.  also  the  first  element  in  rhubarb  and the  second  element  in  Ahasuerus  and  in  Xerxes, rorqual,  n.,  any  whale  of  the  genus  of  large  whales, the  Balaenoptera.  —  F.,  fr.  Norw.  reyrhval,  fr. ON.  reydarhvalr,  fr.  reydr,  ‘rorqual’  (fr.  raudr, ‘red"),  and  hvalr,  ‘whale’.  See  red  and  whale. Rosa,  1)  fern.  PN.;  2)  a  genus  of  plants,  the  rose (bot.)  —  L.  rosa,  ‘rose’.  See  rose.
34326:Scythian,  adj.  and  n.  —  Formed  with  suff.  -an  fr. L.  Scythia,  fr.  Gk.  SxulKix,  ‘the  country  of  the Scythians',  fr.  2x6&r(?,  ‘a  Scythian’, se-,  pref.  —  L.  se-,  a  collateral  form  of  sed-,  ‘aside, apart’,  rel.  to  the  prep,  sed,  se,  ‘without’,  and to  the  conjunction  sed,  ‘but’,  fr.  I.-E.  reflexive base  *swe-,  *se-,  whence  also  OSlav.  svg-ne, svd-ni,  ‘without’.  See  secret,  sedition,  sedulous, select,  separate,  severus,  solve.  See  also  ebriety, sober,  idio-.  See  also  zenith.  For  an  enlarged form  of  the  above  base  see  sine  and  prep, sunder.
38333:Taxus,  n.,  a  genus  of  plants,  the  yew  (bot.)  —  L., ‘yew’,  a  Scythian  loan  word.  Gk.  Tot;ov,  ‘bow’, is  of  the  same  origin  (see  toxic).  For  sense  devel¬ opment  cp.  ON.  yr,  which  unites  the  meanings ‘yew’  and  ‘bow’.  See  Hehn,  Kulturpflanzen  und Haustiere,  8th  edition,  p.  621.
39724:toxic,  adj.,  pertaining  to  poison.  —  ML.  toxicus, fr.  L.  toxicum,  ‘poison’,  fr.  Gk.  xoEixov  (scil. <pap|jtaxov),  ‘arrow  poison’,  neut.  of  the  adjec¬ tive  toEix6?,  ‘pertaining  to  a  bow  or  arrow’, fr.  x6 Eov,  ‘a  bow  or  arrow’,  fr.  Scythian *taxsha-,  whence  also  L.  taxus,  ‘yew’.  Cp.  taxus.
### KLN finger
14761:Derivative :  finesse,  intr.  and  tr.  v. finger,  n.  —  OE.,  rel.  to  OS.,  OHG.  fingar,  ON. fingr,  Du.,  MHG.  vinger,  G.  Finger,  Goth. figgrs;  prob.  rel.  to  five  and  cogn.  with  Arm. hinger-ord,  ‘the  fifth’.  See  A.  Meillet  in  Bulletin de  la  societd  de  linguistique,  1928,  29,  36. Derivatives:  finger,  tr.  and  intr.  v.,  finger-ed, adj.,  -finger-ed,  combining  form,  fingering  (q.v.), finger-less,  adj.,  fingerling  (q.v.),  finger-y,  adj. fingering,  n.,  the  act  of  using  the  fingers  (esp. mus.)  —  Formed  fr.  finger,  v.  (see  prec.  word) with  -ing’,  suff.  forming  verbal  nouns, fingering,  n.,  a  fine  woolen  yarn.  —  Earlier  fin- gram,  corrupted  fr.  F.fin  grain,  lit.  ‘fine  grain’. See  fine,  adj.,  and  grain.  For  a  similar  cor¬ ruption  cp.  grogram.
### KLN five
14804:Fitz-,  first  element  in  PNs.,  and  meaning  ‘son’ (esp.  of  illegitimate  descendants).  —  AF.,  fr. OF.  fiz  (pronounced  fits),  fr.  earlier  fils  (cp.  F. fils),  fr.  L.  filius,  ‘son’.  See  filial, five,  adj.  and  n.  —  ME.  fif,  fr.  OE.  fif,  rel.  to OS.  fif,  ON.  fimm,  Dan.,  Swed.,  Norw.  fem, OHG.  funf  finfi  MHG.,  G.  fiinf  Goth,  fimf, fr.  I.-E.  *penqwe  (with  assimilation  of  qw  to initial  p);  cogn.  with  OI.  pahea,  Toch.  A  pan,
```


## [2026-09-14T00:54:05.161Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"### MON پانچ\"; grep -n \"پانچ\" MON_part1.txt MON_part2.txt | head -20\necho \"### MON پنچ\"; grep -n \"پُنچ\\|پنچ \" MON_part1.txt MON_part2.txt | head -10\necho \"### page tags\"; grep -n \"\\[pdf page\" MON_part1.txt | head -3; grep -c \"\\f\" MON_part1.txt"
}
```


### [2026-09-14T00:54:05.265Z] TOOL RESULT

```
### MON پانچ
MON_part1.txt:37714:بصورت زنند؛ تپانچه» طبانچه. 
MON_part1.txt:37779:تبانچه: م۳5۰۵ [- طپانچه - طبانجه. معر.) 
MON_part1.txt:92376:تپانچه خوردن] (مصل.) سیلی خوردن» 
MON_part1.txt:93065:طماچه: (۵)م۱::۵ [قس. تسپانچه] (.) 
MON_part2.txt:7497:انواع تپانچه) بکار رود. 
MON_part2.txt:14259:تفنگ (تپانچه). ضح.- گاه باشد که تفنگ يا 
MON_part2.txt:38530:لست" 0 (۱.) سیلی. تپانچه کاج. 
MON_part2.txt:39492:آسیب رسانیدن. تپانچه زدن بر رخسار و بر 
### MON پنچ
MON_part2.txt:51153:پنچ گوشه و دارای پنج ضلع. . آنچه پنج پنج 
### page tags
0
```


## [2026-09-14T00:54:13.620Z] TOOL CALL #42: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/punch",
 "prompt": "Give the full etymology entries for \"punch\" — especially punch (n.) the beverage: is it from Hindi panch / Sanskrit pancha \"five\" (five ingredients), and what doubts does the entry record (e.g. puncheon, OED objections, dates)?"
}
```


## [2026-09-14T00:54:15.268Z] TOOL CALL #43: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%BE%D9%86%D8%AF",
 "prompt": "Give the Persian entry for پند (pand): etymology (Middle Persian, Proto-Iranian, Avestan/Old Persian forms), meaning, and any cited sources (Hasandust, MacKenzie, Cheung)."
}
```


### [2026-09-14T00:54:20.290Z] TOOL RESULT

```
# Etymology of "Punch" (the beverage)

## The Hindi Origin Theory

The commonly cited explanation traces punch (n.2) to Hindi *panch* meaning "five," referring to the drink's five ingredients: citrus juice, water, spirits, sugar, and spice. This theory originates from John Fryer's 1698 account.

## Recorded Doubts

The entry documents significant skepticism about this etymology:

**Historical problems:** "There is no evidence of a drink called *panch* in India, or elsewhere, before the English word; and the English word is now known to have been in use before the English became regular traders to the Indies or attempted settlements in India."

**Phonetic concerns:** Lexicographers have identified "phonetic and historical difficulties" with the Hindi derivation.

## Alternative Theories

The entry proposes the name may reference **the serving vessel** rather than ingredients. A connection to *puncheon* (a ~70-gallon liquor cask from c. 1400) is noted: "the name may have been a sailors' shortening of puncheon, as that to which sailors would look for their allowance of liquor."

The entry also suggests possible influence from *paunch* based on older spelling variants (*paunche pot*).

## Conclusion

The five-ingredient etymology persists in popular usage, but the entry indicates scholarly consensus remains uncertain about punch's true origin.
```


### [2026-09-14T00:54:21.871Z] TOOL RESULT

```
# Persian Entry for پند (pand)

## Etymology

**Etymology 1** traces to Middle Persian *pnd* (pand, "path; counsel, advice"), deriving from Proto-Iranian *\*pántaHs* ("path, road") and Proto-Indo-Iranian *\*pántaHs* ("path"). The entry notes cognates including Old Armenian *hun*, Ancient Greek *pátos* and *póntos*, Latin *pons*, and Old Church Slavonic *pǫtĭ*.

**Etymology 2** lacks complete documentation but suggests "a semantic shift from Etymology 1 above, as tricks are a special form of guidance to achieve effective results."

## Meanings

1. **Etymology 1**: Advice, counsel, guidance
2. **Etymology 2** (archaic): Knack, trick, gimmick

## Cited Sources

The entry references:
- **Edelʹman, D. I.** (2020) - *Etimologičeskij slovarʹ iranskix jazykov* [Etymological Dictionary of Iranian Languages]
- **Dehkhoda, Ali-Akbar** (1931–) - *Dehkhoda Dictionary*
- **MacKenzie, D. N.** (1971) - *A concise Pahlavi dictionary*
- **Durkin-Meisterernst, Desmond** (2004) - *A Dictionary of Manichaean Middle Persian and Parthian*

No Hasandust or Cheung sources appear in this entry.
```


## [2026-09-14T00:54:27.227Z] TOOL CALL #44: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%BE%D9%86%D8%AC",
 "prompt": "Persian entry پنج (panj): etymology chain (Middle Persian, Proto-Iranian, Proto-Indo-Iranian, PIE), and also list any derived terms like پنجه, پانزده, پانصد. Also give the Persian entry for پنجه if linked."
}
```


## [2026-09-14T00:54:30.598Z] TOOL CALL #45: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/p%C3%A9nk%CA%B7e",
 "prompt": "Give the reconstructed PIE form, meaning, and the descendants in Indo-Iranian (Sanskrit, Avestan), Germanic (*fimf, *fingraz, *funhstiz), Greek (pente), Latin (quinque). Also note the derived terms *penkʷe-dḱomt- 'fifty' and *pn̥kʷsti- 'fist'."
}
```


### [2026-09-14T00:54:34.373Z] TOOL RESULT

```
# Persian Entry: پنج (panj)

## Etymology Chain

The word پنج traces through multiple linguistic layers:

**Middle Persian** → pnc /panǰ/ → **Proto-Iranian** *pánča* → **Proto-Indo-Iranian** *pánča* → **Proto-Indo-European** *pénkʷe*

## Derived Terms

The entry lists these related words:
- پنجاب (panjāb / panjâb)
- پنجشیر (panjšēr / panjšir)

## Related Terms

- پنجه (panja / panje) — this word relates to the cardinal number

## Additional Context

The page notes that پنج means "five" and appears as a cardinal numeral across multiple Indo-Iranian languages. The Persian numeral representation is **۵**, while the Tajik spelling is **панҷ**.

The Wiktionary entry confirms this number shares cognates with Northern Kurdish *pênc*, Sanskrit *páñca*, and English "five," demonstrating deep etymological connections across Indo-European languages.
```


### [2026-09-14T00:54:35.992Z] TOOL RESULT

```
# Proto-Indo-European *pénkʷe (Five)

## Reconstructed Form and Meaning

The PIE form **\*pénkʷe** means "five" and secondarily "hand" (in older usage).

## Etymology

The term likely derives from words for "fist" and "finger," though scholars debate whether the verbal stem meaning "to take in hand" or the concrete meanings are primary.

## Key Descendants

**Indo-Iranian:** Proto-Indo-Iranian \*pánča (leading to Sanskrit and Avestan forms)

**Germanic:** \*fimf; related to \*fingraz ("finger") and \*funhstiz ("fist")

**Greek:** Proto-Hellenic \*pénkʷe

**Latin:** Through Proto-Italic \*kʷenkʷe, resulting in quinque

**Other branches:** Armenian hing, Balto-Slavic \*pénki, Celtic \*kʷenkʷe, Tocharian \*p'ä́ñćä

## Derived Terms

- **\*pénkʷedḱomth₂** ("fifty")
- **\*pn̥kʷsti-s** ("fist")
```


## [2026-09-14T00:54:41.237Z] TOOL CALL #46: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/p%C3%A9nt-o-h%E2%82%82s",
 "prompt": "Give the reconstructed form, meaning ('path'), the root it belongs to (*pent-), and descendants: Proto-Indo-Iranian, Sanskrit pánthās, Avestan paṇtā, Old Persian paθi-, Latin pons, Greek pontos/patos, Proto-Germanic *finþaną and *paþaz, Slavic pǫtь / Russian put'."
}
```


### [2026-09-14T00:54:42.577Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-14T00:54:43.063Z] TOOL CALL #47: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/path",
 "prompt": "Full etymology of \"path\": Old English pæþ, West Germanic *patha-, and what the entry says about the proposed Iranian/Scythian source (Avestan paθ-, Persian path), and any alternative proposals."
}
```


### [2026-09-14T00:54:49.110Z] TOOL RESULT

```
# Etymology of "Path"

**Old English Origins:**
The word derives from Old English *paþ* or *pæþ*, meaning "a narrow passageway or route across land, a track worn by the feet of people or animals treading it."

**Germanic Roots:**
It comes from West Germanic *\*patha-*, which appears in related forms across Germanic languages: Old Frisian *path*, Middle Dutch *pat*, Dutch *pad*, Old High German *pfad*, and German *Pfad*.

**The Etymological Puzzle:**
The initial *p* sound is problematic for linguists. Don Ringe proposes it as "an obvious loan from Iranian" after Grimm's Law. Watkins suggests the word was "probably borrowed (? via Scythian) from Iranian *\*path-*," ultimately tracing to the Proto-Indo-European root *\*pent-* meaning "to tread, go, pass" (evident in Avestan *patha* "way").

**Scholarly Debate:**
However, this Iranian connection remains disputed. The OED and other sources are skeptical of this explanation, regarding it as "too much of a stretch." The word's true origin remains uncertain, as it's not attested in Old Norse or Gothic.

**Regional Usage:**
In Scotland and Northern England, "path" commonly denotes a steep hillside ascent or road incline.
```


## [2026-09-14T00:54:54.201Z] TOOL CALL #48: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/pent-",
 "prompt": "Give the PIE root *pent-: meaning, and its derived terms/descendants (Germanic *finþaną 'to find', noun *póntoh1s 'path', Latin pons, Greek patos/pontos, Slavic pǫtь, Indo-Iranian *pántaHs)."
}
```


## [2026-09-14T00:54:55.634Z] TOOL CALL #49: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/Punjab",
 "prompt": "Etymology of Punjab: is it from Persian panj 'five' + ab 'water' (five rivers)? Give the details and dates."
}
```


### [2026-09-14T00:54:59.812Z] TOOL RESULT

```
# PIE Root *pent- Overview

## Meaning
According to Wiktionary, the Proto-Indo-European root *pent- carries two related senses: **"to pass"** and **"path."**

## Key Derived Terms

The root generated several important descendants across Indo-European languages:

**Germanic branch:**
- *\*finþaną* ("to find") - the thematic present form
- *\*funsaz* - a variant with epenthetic -s-

**Nominal derivative:**
- *\*póntoh₁s* ("path, road") - which produced extensive descendants

**Celtic branch:**
- Old Irish *áitt* ("place"), yielding modern Irish *áit* and Scottish Gaelic *àite*

The Wiktionary article notes that the Celtic connection through *\*pōntH-* is "probably spurious," indicating scholarly debate about certain etymological links. The root demonstrates the typical Indo-European pattern of verbal roots generating both action meanings ("pass") and concrete noun meanings ("path"), reflecting the semantic relationship between movement and the route traveled.
```


### [2026-09-14T00:55:00.024Z] TOOL RESULT

```
# Etymology of Punjab

Yes, the name derives from Persian elements meaning "five waters." According to the Online Etymology Dictionary:

The term comes "from Hindi _Panjab_, etymologically 'the country of five waters,' from Persian _panj_ 'five'...+ _ab_ 'water.'" The source notes it was "so called for its five rivers."

**Etymological breakdown:**
- **Persian _panj_** = "five" (traced to Proto-Indo-European *penkwe-)
- **Iranian _ab_** = "water" (from Proto-Indo-European *ap-)

**Related term:** _Punjabi_ derives from the same root.

The document provides no specific date for when this name was applied to the region, only explaining the linguistic components and their origins through historical language families.
```


## [2026-09-14T00:55:06.269Z] TOOL CALL #50: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D9%BE%D8%A7%D9%86%DA%86/",
 "prompt": "What does the فرهنگ معین (Mo'in) or دهخدا section say about پانچ? Give the entry text and any etymological note (e.g. from English punch, a drink of five ingredients)."
}
```


## [2026-09-14T00:55:08.018Z] TOOL CALL #51: WebFetch

```json
{
 "url": "https://vajehyab.com/moein/%D9%BE%D8%A7%D9%86%DA%86",
 "prompt": "Give the Mo'in (فرهنگ معین) dictionary entry for پانچ, including any bracketed source-language note (e.g. [انگ.] or [فر.]) and the definition."
}
```


### [2026-09-14T00:55:11.481Z] TOOL RESULT

```
# Mo'in Dictionary Entry for پانچ

**Source Language Note:** [انگ.] (English)

**Definitions:**

1. "دستگاه یا وسیله ای که کاغذها را با آن سوراخ و باطل کنند، منگنه" — A device or tool for perforating papers; a punch or hole-maker.

2. "ایجاد کردن سوراخ هایی که اطلاعاتی را نمایش می دهند بر روی کارت یا نوار کاغذی برای وارد کردن آن اطلاعات به کامپیوتر" — The process of creating holes on cards or paper tape to display data for computer input.
```


### [2026-09-14T00:55:13.283Z] TOOL RESULT

```
# پانچ (Mo'in Dictionary Entry)

According to the **فرهنگ معین** section on this page, پانچ has two definitions:

1. "دستگاه یا وسیله ای که کاغذها را با آن سوراخ و باطل کنند، منگنه" — a device or tool for perforating papers, also called a punch or hole-maker.

2. The creation of holes on cards or paper tape to input data into computers.

The entry notes the term is from English (انگ.).

## Etymological Notes

The dictionary content includes an etymological discussion under the beverage section: the word پانچ may derive from Hindi *āñć (pāñć)* meaning "five," since the drink traditionally contained five ingredients (alcohol, sugar, lime/lemon juice, water, and spices).
```


## [2026-09-14T00:55:22.615Z] TOOL CALL #52: WebFetch

```json
{
 "url": "https://vajehyab.com/dehkhoda/%D9%BE%D8%A7%D9%86%DA%86",
 "prompt": "Give the Dehkhoda entry for پانچ — is it a drink (شرابی مرکب از پنج چیز)? Quote the definition and any note on its origin (English punch / Hindi panj)."
}
```


### [2026-09-14T00:55:23.780Z] TOOL RESULT

```
The server returned HTTP 500 Internal Server Error.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-14T00:55:25.797Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"### SYN five\"; grep -n \"FIVE\\b\" SYN.txt | head -10\necho \"### SYN road/way\"; grep -n \"ROAD, WAY\\|WAY, ROAD\\|13.1 ROAD\" SYN.txt | head -10\necho \"### IEC penkwe\"; grep -n \"penqe\\|penkʷe\\|penq^e\\|penkve\" IEC.txt | head -10\necho \"### IEC pontos\"; grep -n \"pontos\\|pontis\\|pntos\" IEC.txt | head -10"
}
```


### [2026-09-14T00:55:25.946Z] TOOL RESULT

```
### SYN five
### SYN road/way
### IEC penkwe
### IEC pontos
13368:pontos, is, à (ponth-) “crossing, passage’. WP II, 26 Skt. cf. panthah, A mf. ‘path’; Av. panto, panta, mf. id.; Oss. (dim. type) fándag, pl. fándágta ‘road’; Arm. hun, s. “ford, strait’; Gk. póntos, m. ‘high seas, the main’; Alb. péndé, f. ‘weir, dam’ (if not a LW?); Lat. pons, gs pontis, gp pontium, m. ‘bridge’; OS foói, faói, io-st. (going, gait'; G cf. fahnden, v. (^sleuth, stalk’, but see pondheio); Icel. cf. fans, m. ‘gang’; OCS (and com. SI.) poti, gs: poti, m. “road, highway’; Latv. pants, m. “line of verse?
```


## [2026-09-14T00:55:30.390Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"### SYN five\"; grep -n -i \"^13.* five\\|five.*quinque\\|quinque\" SYN.txt | head -10\necho \"### SYN way\"; grep -n -i \"road, way\\|10.71\" SYN.txt | head -10\necho \"### IEC five\"; grep -n \"penqe\\|penqu\\|penk\\^e\\|‘five’\" IEC.txt | head -15"
}
```


### [2026-09-14T00:55:30.524Z] TOOL RESULT

```
### SYN five
13318:ea jn quinque fr. *penk”e, etc.) : OHG fereh-eth, Langob. fereha, NHG
22173:2. Lat. prope, prob. fr. *pro-que (cf. proximus), with opposite assimilation to that seen in quinque fr. *penque. Se- mantic development through ‘in front of? or ‘forwards to’? Walde-P. 2.47. Ernout-M, 815.
31743:18.25. Dialect. The distinction be- tween 2 Janguage’ and a subordinate dialect’ was not observed in early times, when the words for ‘language’ (18.24) covered also what we now call a ‘dia- lect’. Thus Grk. ’Arrixy yA@ooa, ’Arriky guvt, Lat. lingua with reference to Greek dialects (Crassus quinque Graeci sermonis differentias sic tenuit ut, qua quisque apud eum lingua postulasset, etc. Quint.), and Skt. bhasa- used esp. of the Prakrit dialects.
### SYN way
1258:Grk. wévros, poet. or of a special sea (wévros  Etitevvos, Tlévros) : Skt. path-, nom. panthds ‘road, way’, ete. (10.71). Specialization of ‘way’ to ‘seaway’, like kehevOos ‘way’ in Hom. bypa xKédevOa, ixBudevra Kédevda, etc. Walde-P. 2.26.
16545:trond’ (10.71), also ‘way, Bess Gloss. 174). re also and orig. pppoe. :
16550:Dan. set, Sw. sdit (Dan. in phrases, Sw. usual word) : Dan. sette, Sw. sdtte set with development through ‘how a thing is set, arrangement’. Cf. NE set of a garment, ete. Falk-Torp 1231. es NE wey (OF wep i ai orig. ‘road’ (10.71).
16624:M wb.) 10.54 OverTAKE oll pen Gb.) 10.55 Arrive, REACH 10.12 ae AROUND 10.56 APPRoAcH (vb.) 40.18 Wino, WRAP (vb.) 10.57 ENTER 10.14 Ron (7b.) 10.61 Carry (BEaR) 10,15 rairb.) 10.62 Brine re Russe, LIFT 10.63 SEND 10. vb.) 10.64 Leap (vb.) Ce se Tigui 10.65 D 1024 Dror (sb., of Liquid) : RIVE (vb. trans.) 1025 THROW (vb.) 10.66 Rive (vb.) 1098 SHAKE (vb. trans.) 10.67 Pusu, Sov (vb.) 1031 Bor (vb. intr.) 10.71 Roan 10.33 Smvx (vb.) 10.73 Street 10.34 Fuoat (vb.) 10.74 Brmwce 10.35 Sw (vb.) 10.75 Carrtace, Wacon, Cart 1036 Satz (vb.) 10.76 WHEEL 1037 Fuy (vb.) 10.77 AXLE 10.38 Brow (vb. intr.) 10.78 Yoxs 1041 Creer, CRAWL 10.81 Sup 1042 Ste, Sur (vb.) 10.82 Sartor 1043 Jump, Leap (vb.) 1044 Dancz (vb.) ee meee 1045 Watx (vb.) i 10.46 Run (vb.) 10.85 Oar 1047 Go 10.852 Row (vb.) 1048 Come 10.86 RuppER 1049 Go Away, Depart 10.87 Masr a Tze 10.88 Sar (sb.) 10.53 peso 10.89 AncHoR
17884:‘travel’, deriv. of via ‘road’ (10.71), REW 9295. :
18107:Ok x 10.71 ROAD © B98 ; : NG oe Goth. wigs Lith. kelias st a oH vegr, braut, gata Lett. cel’ t. atrada, camming. yf an.  vej ChSl. pat, césta F. chemin nae ie Sw. vag SCr. put, cesta 8. camino, vig Si OE — weg, street Boh. cesta = rum, cale ME _ weéie, strete, gate Pol. droga *  tlige, set, ray NE road (way) Russ. doroga, put’ Bithar OAT, «= Du = Ni 4g thar OHG RECO. ve. Skt.  path-, marga-, V thar, rod, bealach weg, straza adhvan- R verde MHG wee, straze Av. pas-, advan-, ; ent NHG weg, sirasse frayana-
18160:1, Gtk. méros: ChSl. pati ‘road, ret Skt. path-, Av. paé- ‘way, road, me ete. (10.71). Hence Byz. povo- ee NG povorar, cpd. with pévos alone, single’, G ia ie fe ‘tame Hom. éraprés, lit. ‘trod- ee 2 on of 4-cop. and the root of ‘ruth ia grapes’ : Russ. trepat’
18170:Ir. conar, see under ‘road’ (10.71).
18180:WGume. loanword of either Grk, (470s) or Iran. (cf. Av. paé-, 10.71) origin Other etymologies unconvincing, Wal. de-P. 2.26 f. Weigand-H. 2.401. Kluge G. 488. Franck-vy. W. 485.
18185:7. Skt. Av. words for ‘path’, see under ‘road’ (10.71).
### IEC five
12677:penque ‘five’; penqutis ‘group of five Sk. pañča; Av. pañča; Per. panj (pang); OPer. cf. pa(n)Ca-; Oss. fondz; Tokh. A pä, B pàn-; Arm. hing, gs: hngi, i-st.; Myc. (?) pe(n)gato- (said of a chariot); Gk. pénte, cpds. penta-; Cypr. peísei; Alb. péns, pesë; Lat. quinque (w. assimilated conss.); Osc. pump-; Gaul. pinpe- (in pinpe-donum ‘cinquefoil’, for *pimpe- dulon, beside pinpe-tos "DÉI pempe-, id.; Mir cóic, Ir. cúic, cúig (with assim. conss.); OBr. pimp; Br. pemp; W pump; Cor. pymp; Go. Dmt OE fif; OHG fimf, finf; Du. vijf; ON fimm beside fimt, f. col. ‘fivesome’; OCS cf. peti (and com. Sl.) (*fivesome', hence *five); Li. penki; Latv. pieci, id. WP IT, 25ff.
12678:penqueros 'fivesome'. Cf. penque Arm. cf. hinger-ord ‘fifth’; Osc. pumperias, fpl.; Gall-Lat. *pe(m)peracium Ca shrub’ (?). Misspelt peper-?); MIr. cóicer, m.; Ir. cúigear, m.; OHG (and com. Gmc.) fingar (finger. Here?); Li. penkeri (fivesome'; OCS cf. pẹ- torü, id. (fr. *penqutero-) beside petero, id.
12679:penqutis ‘set of five’. Cf. penque, etc. Skt. panktíh, £.; Osc. cf. pomtis, adv. 'quin- quies’; ON fimt, f.; OCS peti (and com. SI. "Deet: Li. cf. penkti, adj. f. “fifth” beside pen- ketas, m. 'fivesome
12680:penqutos “fifth” S kt. cf. pacata, f. 'fivesome'; Tokh. B pinkte, pinkce “fifth”; Gk. pémptos, id.; Alb. i pésté, id.; OLat. quinctus, Lat. quintus, id.; MIr. coíced id.; Ir. cf. cüigeadh, m. “fifth, as a frac- tion’; OBr. pimphet; W pummed; Br. pemped, pempved; Cor. pumpes, id.; Go. fimfta-, cpds.
13281:(pnqutos, zero-gde of type penqutos, q.v. only in Av. pux0o ‘fifth’; OHG funfto, id. and com. Gmc.)
```


## [2026-09-14T00:55:41.118Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"### SYN 13.13\"; grep -n \"13\\.13\" SYN.txt | head -5\necho \"### ARY پنج\"; grep -n \"پنج\" incoming/ARY/ARY_pages.txt | head -15\necho \"### ARY پند\"; grep -n \"پند\" incoming/ARY/ARY_pages.txt | head -15"
}
```


### [2026-09-14T00:55:41.195Z] TOOL RESULT

```
### SYN 13.13
23353:13.13 WHOLE
23429:13.13 WHOLE
28759:Goth. aljan (renders fos as ‘jeal- ousy’, Rom. 13.13, otherwise ‘zeal’) = ON eljan ‘energy, endurance’, OE ellen ‘strength, vigor, courage’, OHG ellen ‘zeal, strength’, etc., etym. dub., perh. : Lat. alacer ‘lively, eager, glad’. Walde- P. 1.156. Falk-Torp 188. Feist 38. Walde-H. 1.25.
### ARY پنج
52:تبایل ترکك زبان (از حدود سده‌ی پنج میلادی به بعد) موجب از میان رفتن آن زبانهای محلی گردیده
632:سانسکریت) اهمیت ویژه دارد. ضمناً امروزه دهها زبان (اردو» هندی» گجراتی» بنگالی؛ پنجابی»
796:58]) در قرن پنجم میلادی از شمال آلمان و دانمارک به انگلستان هجوم بردند و ظرف چندین
814:کهن ترین متن به زبان ارمنی ترجمه‌ی انجیل است که در سده‌ی پنجم میلادی انجام شده است.
815:امروزه ارمنی‌ها که شمار آنها بیش از پنج میلیون نفر است در جمهوری ارمنستان زندگی می‌کنند
845:انشعاب زبانهای نوین اسلاوی از زبان اسلاوی کهن» فرن پنجم میلادی یعنی همان دورانی است که.
1194:قاطع که به اهتمام مرحوم دکتر معین در سال ۵ در پنج جلد چاپ شد نمونه‌ی خوبی از اینگونه
4540:بازگشت به: پنج؛ ده.
5116:پنجاه / ۱۷۵
5131:۲ بازگمت به: پنجم.
5153:بازگلت به: پنج و ده ۰
5178:۸ پنجه / ۱۷۷
5181:۱ بازگشت به: پنج.
6678:۱- چم این واژه در برهان قاطع : چنین است: قلاب» کجکه (قلابی که با آن فبل را رانند)» پنجه و انگشتان مردم»
### ARY پند
537:پندارهای قدیمی در مورد سرچشمه‌ی زبانها را متزلزل کرد. جنبشی که در دانش زبانشناسی ایجاد شد
880:ِ تقسیم پندی زبانهای هند و اروپایی از نظر مکان جغرافیانی
1387:۵ آیا هسانی آشکار معنایی و آوایی واژه‌های «پندار» و «پنداشتن» با واژه‌هنای لاتین.
1463:معنی این واژه در زبان‌های آلمانی و اسکاندیناوی و اسلاوی: پند دادن.
1493:۲- 13۸۶۷13۸7 واژه‌های ژُرمئی این فهرست را از یک ریشه‌ی ناشناخته می‌پندارد. ی
1614:را برای واژه‌های ,آل۸ و غیره می‌دهد. به پندار من این دو واجريشه یکی هستند ولی رای مزید اطمینان جلو
1929:پندار نویسنده‌ی کتاب حاضر این است که این واژه‌ها به احتمال زیاد همه از یک واجریشه‌اند ولی برای آگاهی
3681:معنی این واژه در لاتین: گوسپنداخته شده,
6543:چم اين واژه در بونانی و ایرلندی کهن و لیترانی و زبان‌های ژرمنی: (پشم گوسپند را) بریدن» قطع کردن» خراشیدن,
9070:اروپایی 33۳۰ می‌داند و آن را با واژه‌ی لاتین 3380 همريشه می‌پندارد (برهان قاطم: ۹۵۵).
9892:ز(زره اسب)؛ 2581287/۸0 (هشیار بیدار). به پندار من واژه‌ی "زندان" (پهلوی:2:)(210۸7
10532:چم این واژه در ازبان‌های ژرمنی: گله» دسته‌ی گوسپند یاگاو» گروه.
```


## [2026-09-14T00:55:46.189Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '5100,5200p' incoming/ARY/ARY_pages.txt"
}
```


### [2026-09-14T00:55:46.252Z] TOOL RESULT

```
اوستی (ع/05587): 0۳7 1
کردی (8.015): ۰ ۳8۲۵ ,۴8 ,8۸17 نورس کهن (۸08۵8 010): 1
افغانی (پشتر) (۸۳0[7۸(1): ۳7۸ ساکسونی کهن (/54240 ص01): 7
تخاری ۸ (۸ (۵ل702۸5): 2 فریزی کهن (لفا5ل7# ا0): لاد
تخاری 8 (8 [4ل۸ل-ل705): 215 آلمانی کهن (0222140 لوط صتم): ۲138
سانسکربت (5۸۸/۹/7) :۳۸۷۸ ,8۸۲17۸ آلمانی (/ف/ل027): لاد
ارمنی (۸04871۸4۸): 116 انگلیسی کهن (5لا80/0 صا0): داد
پونانی (07550): 8 ,۳8۲35 ۰ انگلیسی (4ل8ل8(/02): لد رد1
لاتین (4710)+ 00 دانمارکی ([0۸(۷15): ۳
فرانسه (۳857): زن اه سرئدی (8150154): 1 1
اسپانیایی (5۳۸۸/1513): ۰0 نروژی (1۵۸ ۰۵/0۳۳0 ۳
ایتالیایی (4(۷ال7۸): آذرارن اه هلندی (7ل776ا0): ۷۳
رومانی (14(/140۷(ن): شاه اسلاوی کهن (ع۲ما؟ 028677 طا0):
پرتغالی (25ن۳07101): یداه 7 با281
[pdf page 174]
۹
پنجاه / ۱۷۵
لهستانی (ب5ا۳0): ۰ ۳186100 ,7180
روسی (/55140): لا با پسگشت‌ها 5
چکه (ع22)): پا ید۱ 8 ۲0500
اسلوا کی (07/۸/4.-51): ۱ 6 (۴7۷8) + 8/7
لیتوانی (۸140لاب2): الا 2 (00) قلقملنم هط
ایرندی کهن (لولها 01): 1 4 (38) ات شاد ها
گالی (بقلاناهه): داد نا 9952 اه
ولزی (قا78): 7 ,۳1۸/۳5 8 (۲3۷8) :005
برتونی (88870(7): ۰ ۳838۳ ,8811۳۸7 25 67۷8 دزد
کورن والی (007//8): ان 25 ری و0۱
آلبانی (/۸0اللمهلم: دنا برهان قاطع + ۴1۹
هتیت. (7177775): ۳۸۸
بادداشت:
۱- بازگشت به: پانزده.
۲ بازگمت به: پنجم.
چم انکلسی سرواژهی ارس سر 1353
سس ی 0۸
اوستایی (4887۸27): نک نا پرتغالی (۳077701238): ۰ ۲1۳۲۹8۲3۸
پارسی باستان (۳878147 0ا0): ابسلندی کهن (0//۸(1/ش9 صا0):
۲۸۲۵۲۸۵۲ : دی ره ۱۱|
پهلری (1/الزه): 1 فریزی کهن (/(4ا9ل7۶ صا0): 71۳71073
کردی (0134): ۳7۸ آلمانی کهن (057۵/9 بان !۷( هان):
اففغانی (پشتو) (//(لام چم 05 زا انا نا
ساسکریت (۰:4(/9/7 ۳۸۱۷۲۵۸7 آلمانی (/(/057): ۳6
آرمنی (7ل4(481714): لزان انگلیسی کهن (#لکلا20/0 ۰:2 ۲1۳316
برنانی 078870): انز نداد اناد ۱ انگلیسی (8لا8(/0): ۳
لانین (7100ما): خ 000 هلندی (07674): ناب ابا
فرانسه (ح/۳762): ای انا رانا نی لهستانی (۳0/3): 818607135۸7
اسپانیایی (5۳۸۸//5[4): اناد اشنا چک (25804): 57
ایتالیایی (9۷لل7/): ادا ی اسلوا کي (481.0770): ۳20۳51۸7
[pdf page 175]
پسگشت‌ها هرد ۲ (14 ۳1۳3۷) :60/28 ۸۸
8 و برهان قاطع ۳۳۰
1 (51۳۳0) وی ان رو
2 تب
یادداشت:
بازگلت به: پنج و ده ۰
پهلری (/۳۸۸۲): ۳۸۲۲0۸۸ ,۳۸۲۳۲۸4 انگلیسی کهن (8۸058 ۰:00 ۲1۳۳۸
تخاری ۸ (۸ (70807۸7): ۳ انگلیسی (8(/01311): ۳7
تخاری 8 (8 ۸ م7ل707). لد اف لا با دانمارکی (0۸4//5/7):-۳۳۸875031 ,7:17
سانسکریت (54(/587): ,۳۸۲۲۸77۸8 نروژی ((۰۸/07۳۷8014 ۳8۸/087
۳۸۸۸ ,۳۸۸7 رکف ۸5 ۳
ارمنی (۸۷/827۷): ند ید۱۱ هلندی (007): ۷0
یونانی (07828): را بدا ندرا اسلاوی کهن (۲/0ها5 تلع #لاتل صزه):
لاتین (/112ل): 018 زت بدا
فرانسه (ل/(۳۸): آا اد رانا ی لینوانی (۸(/1/21ل727/ )+ دای برد
اسپانیایی (4ل5۳۸۷]8): 010 ایرلندی کهن (تلدل] طام).
ایتالیایی (/(4لل7): 010 ,۲01۳80
رومانی (۸(/14/(): 070 گالی (نلولانام0): نا انا
پرتغالی (۳070010852): نیدیاااره گالیک (0/اقه0): تالایا با
گوتیک (007710): ید۱۱ آلبانی (۸18۸(2م: اد و ید |
ایسلندیکهن ((010/۸/7/(ی5 صاه):
انا پسگشت‌ها دشر رد ]
تررس کهن (۸0788 صا0): 1 808 لش یی
ساکسونی کهن (542:00 0.ا0): 0 41 (۲1۳71) ی
فریزی کهن (/5142ل۲۶ صان): 7۸ نان ماه
آلمانی کهن (0870/00 0۲ات صاه): 8 (۲1۳7) :005
0 برهان قاطم + ۴۳۱
آلمانی (057/0۷): اد لا
[pdf page 176]
یی .
۸ پنجه / ۱۷۷
یادداشت:

۱ بازگشت به: پنج.
| مانگلیی سوای رن ۱385۳۸۷
پهلری (1ماتلهه): ۸6 دانمارکی (0۸071814): 207
لاتین (4710ا)(شاید) دنا هلندی (0767): ۷37
فرانسه (۳۸2۸/74)(شاید) 2016 اسلاوی کهن (۲12ا5 64نابل) 010):
اسپانبایی (5۳۸۸/52)(شاید) ۳/۹0 ۳71
ایتالیایی (/۸4ا.لا17)(شاید) یدنا روسی (514(7لا): تدای را
پرتغالی (۳07701252)(شاید) ‏ ۴۸330
ساکسرنی کهن (543400 010): اند پسگشت‌ها 5
فریزی کهن (//۲۶۷94 صا۵): اند ۳
آلمانی کهن (02821۸(1 04اب ۵ا۵): 7187 5 (5181) تلهم
آلمانی (0524۸): 7 6 (۳۸۷) دس دی هه
انگلیسی کهن (50لا800 صا0): ۰ ۳۷۶۳ 8 (8181) :0۸/105
انگلیسی ([8لا8(/0). زان نز برهان قاطع : . ۴۳۱
بادداشت:
این واجريشه با واجریشه‌ای که واژه‌ی 8181067/8 از آن آمده خویشی نزدیکك دارد (پسگشت: 808 :۳01607779
,383-384 (۲13683) :7 0۸31۸)
اوستایی (1]55700۷ < بلرچی (81لناءا8۸): 0
1 ,7 ,8۸7710 سانسکربت (54۸/5777): 2۸78
پارسی باستان (۳8۴۵14۸ 010): آرمنی (4/۸45214/7): 1 ,808
```


## [2026-09-14T00:55:56.947Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"پند /\\|پند ‌/\\|/ ۱۷\\|پنج /\" incoming/ARY/ARY_pages.txt | head -20\necho \"=== latin index PANJ/PAND\"; grep -n -i \"PANJ\\|PAND\\b\" incoming/ARY/ARY_latin_index_pages.txt | head -20"
}
```


### [2026-09-14T00:55:57.006Z] TOOL RESULT

```
390:دیباچه / ۱۷
4991:پشم / ۱۷۱ ِ
5050:پٌک (به چم / ۱۷۳
5116:پنجاه / ۱۷۵
5178:۸ پنجه / ۱۷۷
=== latin index PANJ/PAND
447:O— panj | cing funf vif fem
4425:FIMFTAIHUN GOTHIC) Si F PANJALAS —(AFGHANI) (2+) «gil |
4977:FIMM OLD NORSE) pS 335 PANJ, PEJ, PENC (KURDISH) 53,5
5012:FIFTICH = (OLD FRISIAN) iS 52.3 PANJAH PAHLAVI) 5 shy
5014:FIMFZUG PANJOS HAEGHAND, (3%) iil
5057:POTE DANISH) Sylaila PANJAG PAHLAVI) 5 she
5072:PAND ABALUCHI) gz yo > JYAVESTAN) gle yh
5076:PONS, PONTIS HLATIN) ot PAND PAHLAVI) «5 shy
5086:(PAND) 64, (ADVICE) 101 PELD {OLD ENGLISH) ep 5J&i
```


## [2026-09-14T00:56:17.142Z] TOOL CALL #58: Bash

```json
{
 "command": "ls site/pages/392.jpg 2>/dev/null; pdftoppm -f 392 -l 392 -r 200 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg392 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg392.png"
}
```


### [2026-09-14T00:56:18.812Z] TOOL RESULT

```
site/pages/392.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb 75438 Sep 13 20:56 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg392.png
```


## [2026-09-14T00:56:20.945Z] TOOL CALL #59: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg392.png"
}
```


### [2026-09-14T00:56:21.453Z] TOOL RESULT

```

```


## [2026-09-14T00:56:21.444Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-14T00:56:42.742Z] TOOL CALL #60: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/sputnik",
 "prompt": "Etymology of sputnik: Russian s- 'with' + put' 'path, way' + -nik; what PIE root does it give for put'?"
}
```


## [2026-09-14T00:56:43.943Z] TOOL CALL #61: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/five",
 "prompt": "Etymology of \"five\": Old English fif, Proto-Germanic *fimfe, PIE *penkwe; what related English words does it list (finger, fist, fifteen, fifty)?"
}
```


### [2026-09-14T00:56:46.380Z] TOOL RESULT

```
# PIE Root for "put'"

Based on the etymology provided, the Proto-Indo-European root underlying Russian *put'* ("path, way") is **\*pent-**, meaning "to tread, go."

The source material explains: "from Old Church Slavonic _poti_, from PIE _\*pent-_ 'to tread, go'" and notes this root is "source also of Old High German _fendeo_ 'pedestrian,' Sanskrit _panthah_ 'path, way,' Greek _pontos_ 'open sea,' Latin _pons_ 'bridge.'"
```


### [2026-09-14T00:56:48.903Z] TOOL RESULT

```
# Related Words to "Five"

Based on the etymology page, the listed related English words are:

- **fiver** - a five-dollar or five-pound note
- **high-five** - a celebratory gesture
- **pentameter** - "consisting of five metrical feet" (from Greek pente "five")
- **fivefold** - occurring in five parts or to five times the degree

The page also mentions several other words derived from the PIE root *penkwe- "five," including:

- **cinque** - "a group of five, five units treated as one"
- **quincunx** - an arrangement of five objects (one at each corner and one in the middle)
- **quinquennial** - "lasting five years"
- **quint** - "group or set of five"
- **punch** - the drink, traditionally said to derive from Hindi *panch* "five" (referring to five original ingredients)

However, the page does **not** list finger, fist, fifteen, or fifty as related words despite their obvious numerical connection to five.
```


## [2026-09-14T00:56:50.527Z] AGENT

Now let me archive all the web sources.


## [2026-09-14T00:56:53.128Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \\\n 'https://www.etymonline.com/word/punch' \\\n 'https://www.etymonline.com/word/path' \\\n 'https://www.etymonline.com/word/Punjab' \\\n 'https://www.etymonline.com/word/sputnik' \\\n 'https://www.etymonline.com/word/five' ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 392, roots Penkwe/Pent: English-side chains (punch, path, Punjab, sputnik, five)\" 2>&1 | tail -2\ndone"
}
```


### [2026-09-14T00:56:55.403Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/12f528be22d753c9.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/fd4ea9ed6d10780c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e0758f3bf4923d28.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/8ffca7c51e952723.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/1760a2811f5e87a3.txt
```


## [2026-09-14T00:57:01.195Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \\\n 'https://en.wiktionary.org/wiki/%D9%BE%D9%86%D8%AF' \\\n 'https://en.wiktionary.org/wiki/%D9%BE%D9%86%D8%AC' \\\n 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/p%C3%A9nk%CA%B7e' \\\n 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/pent-' \\\n 'https://abadis.ir/fatofa/%D9%BE%D8%A7%D9%86%DA%86/' \\\n 'https://vajehyab.com/moein/%D9%BE%D8%A7%D9%86%DA%86' ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 392, roots Penkwe/Pent: Persian/PIE side (panj, pand, penkwe, pent, panch)\" 2>&1 | tail -2\ndone"
}
```


### [2026-09-14T00:57:05.439Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/6689cb384fd5a194.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c9358e3c3aa6bee2.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/1823b2e72ec2c79b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c88846135d78d08f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/4ef9d08dd4eb00fd.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/8da5f05417566cc6.txt
```


## [2026-09-14T00:57:08.281Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; sed -n '1,120p' tools/verify_check.py"
}
```


### [2026-09-14T00:57:08.319Z] TOOL RESULT

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


## [2026-09-14T00:57:21.143Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 -c \"\nimport json;d=json.load(open('data/verification/page-385.json'));e=d['entries'][0];print(json.dumps({k:v for k,v in e.items() if k!='nodes'},ensure_ascii=False,indent=1)[:2000]);print(json.dumps(e['nodes'][1],ensure_ascii=False,indent=1)[:2500])\""
}
```


### [2026-09-14T00:57:22.265Z] TOOL RESULT

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
   "note": "Pokorny IEW p.792 (local POK_03.txt, form-feed leaf 25) reads: '(peg-:) pog-: pōg-, pŏk-s- \"Achsel, Hufte, Lende, Seite\". Ai. pákṣa- m. \"Schulter, Flugel\" und \"Seite
{
 "id": 2,
 "lang": "Hindustani",
 "words": "pankâ",
 "verdict": "transcription_suspect",
 "error_in": "book",
 "book_prints": "pankâ",
 "correct_form": "pankhā",
 "derivation": "The Hindustani word is पंखा / پنکھا paṅkhā 'fan', with an aspirated -kh-, not 'pankâ'. The printed page (pdf 385, image saved as data/verification/sources/refs/ocr/BOOK/385.png) does read 'pankâ', so this is Nourai's own misprint, not an extraction error: the JSON is faithful to the book. Klein, whom Nourai cites here, spells it 'pankha'. The history: Sanskrit pakṣá- 'wing' > pakṣaka- (with -ka- suffix) > Sauraseni Prakrit pakkha- > Hindi paṅkh 'feather, wing', whence paṅkhā 'fan' (the -kh- is the Middle Indo-Aryan reflex of -kṣ-, and the nasal is an anusvara developed before the cluster). Its basic sense is simply 'fan' (originally a palmyra-leaf hand fan); the 'curtain hung from the ceiling and pulled by a servant' that Nourai glosses is the Anglo-Indian specialisation of the word from the 17th c. on, not the Hindustani meaning.",
 "derivation_fa": "صورت درست واژهٔ هندوستانی paṅkhā «بادبزن» است (با کاف دمیده -kh-)، نه «pankâ». تصویر صفحهٔ چاپی (pdf ۳۸۵) نشان می‌دهد که خودِ کتاب «pankâ» چاپ کرده است؛ پس این خطای چاپی نورایی است نه خطای خوانش اسکن. کلاین که نورایی به او ارجاع می‌دهد، «pankha» نوشته است. راه تحول چنین است: pakṣá- سنسکریت «بال» ← pakṣaka- (با پسوند -ka-) ← pakkha- در پراکریت شورسنی ← paṅkh هندی «پر، بال» و از آن paṅkhā «بادبزن»؛ خوشهٔ -kṣ- در هندوآریایی میانه به -kh- بدل می‌شود و پیش از آن غنّه (انوسوارَه) پدید می‌آید. معنای پایهٔ واژه همان «بادبزن» است؛ معنای «پردهٔ آویخته از سقف که خدمتکار می‌کشد» تخصیص انگلیسی‌ـ‌هندی واژه از سدهٔ هفدهم به بعد است.",
 "sources": [
  "https://en.wiktionary.org/wiki/%E0%A4%AA%E0%A4%82%E0%A4%96%E0%A4%BE",
  "https://en.wiktionary.org/wiki/punkah"
 ],
 "ref_check": [
  {
   "ref": "KLN:1272",
   "status": "partial",
   "note": "Klein 1966 p.1272 (leaf 678): 'punka, punkah, n., a large curtain serving to fan a room. — Hind. pankha, \"a fan\", fr. pankh, \"feather, wing\", fr. OI. pakṣaḥ, pákṣas, \"wing, side, half\"...' — the derivation is Nourai's, but Klein spells the Hindi word pankha and glosses it 'a fan'."
  },
  {
   "ref": "AHD",
   "status": "supports",
   "note": "Watkins 1985 s.v. peg- routes Sanskrit pakṣaḥ to English PUNKA, i.e. the same Sanskrit -> Hindustani -> English chain."
  }
 ],
 "consulted": [
  {
   "src": "HJB",
   "where": "Hobson-Jobson p.742 s.v. PUNKAH",
   "stance": "partial",
   "note": "'PUNKAH, s. Hind.
```


## [2026-09-14T00:57:32.692Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD\nls\necho \"=== penqe\"; grep -n \"penq\\^e\\|penque\\|penkʷe\\|pénkʷe\" WLD_Bd2_pages.txt | head -10\necho \"=== pent\"; grep -n \"pent-, pont-\\|pent-:\\|^pent-\" WLD_Bd2_pages.txt | head -10"
}
```


### [2026-09-14T00:57:32.799Z] TOOL RESULT

```
WLD_Bd1_1930_dli_70244_djvu.txt
WLD_Bd1_1930_dli_70244_text.pdf
WLD_Bd1_pages.txt
WLD_Bd2_1927_dli_106624_djvu.txt
WLD_Bd2_1927_dli_106624_text.pdf
WLD_Bd2_pages.txt
=== penqe
5569:wagt man eiuerseits unter Ankniipfung an penq^e „funf” („die geschlossenen
=== pent
1726:pent- (im Ar. mit th) „treten, gehen worauf treten, dazugelangen = antreffen,
```


## [2026-09-14T00:57:36.313Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD\nsed -n '1726,1780p' WLD_Bd2_pages.txt\necho \"#### 5560-5585\"\nsed -n '5555,5590p' WLD_Bd2_pages.txt\necho \"#### find WP II 25 penkwe\"\ngrep -n \"penq^e\\|penq\\^e\\|funf.“\\|„funf\" WLD_Bd2_pages.txt | head -20"
}
```


### [2026-09-14T00:57:36.439Z] TOOL RESULT

```
pent- (im Ar. mit th) „treten, gehen worauf treten, dazugelangen = antreffen,
                                                        ;


    finden“ (vgl. venire mvenire) nominal „Pfad, Weg"‘, mehrfach von iiber
                                 ;
                                                    \


    nassesGrelande oder Wasser fiihrendenPfaden, ,,Prugelweg durch Siimpfe,
    Furt, Steg, Brucke“ (s. zum Sachlichen Meringer WuS. 1, 192 f.).
     A\. pdntha==^ 2^Y.pania,acc. sg. pdnthani = av. pantqm und pdnthanam
=      pantan9m^      patha ^      pa'da^ i.    ,
                                                 pathibhih „Pfad, Weg^^ (zur
Flexion zuletzt Bezzenberger KZ. 42, 384, der als Grundlage der Flexion
den «-St. '^pa{n)ihi = lat. ponti-^ slav. pqt^ zu erweisen sucht, der auch in
Zs., so pathi-krt^ erscheint; ap. acc. pa§im), av, zweimal auch „Raum,
Stelle“ (eigentlich „wo man FuB fa6t“), wie ai. pathas-          pathi-h „Ort,
Sitz, Wasser; Luft- und Himmelspfad'" (zur Bed. s. Oldenberg ZdmG. 54,
599 gegen Sieg Gurupujakaumudi 97).
   Letztere hochst auffellig durch die Abwesenheit des Nasals, da fur sog.
       =ai. a hier kein Raum ist; ihr Alter folgt w^ohl aus Pedersens (KG. I

161) ansprechender Herleitung von mir. edit, ait „Ort, Stelle‘‘ aus gleich-
artigem "^poth-ni-
   Lat. pons, -tis ,,Prugelweg durch Siimpfe, Brucke** (fiir Zuriickfiihrung
auf einen o-St.         =
                    jiovrog, Ciardi- Dupre BB. 26, 222, liegt kein AnlaB vor.
Gber pontifexs.zxA^ixt HerbigKZ.47, 21                              1   ff.;   daB osk. pun it ram „Brucke'‘
bedeutet,       ist    nicht ganz           sicher), aksl. path                ,,Weg‘',   tiefstufig apr. pintis
„Weg‘‘ (kann auch o-St. = gr. ndrog sein), arm. him ,,Furt, Weg^^ (Hiibsch-
mann Arm. St. I 39, Arm. Gr. I 468, Pedersen KZ. 39, 366; auf den i-St.
^p07itd^ zuruckfiihrbar, also eine ebenso schwache Stiitze fur einen Kons.
St.         wie die ar. Kasus vom St. path-) als o-St. gr. jidvrog ,,Meeres-
pfad, MeeP^ {7t6j*rog dXog jtoXiijg, vgl. auch vygd y.eXev^a ^), tiefstufig
Tidjog     m.   ,,Pfad, Tritt^* (jiarioy ..trete”).
  Umstritten ist die Herkunft von ags. j)ced „Pfad. Weg‘* (engl. path),,
ahd. vdiA.pfad (Lit. bei Falk-Torp 1525); kaum nach Loewe IF. 10. 81
eine fruhe mittelbare Entlehnung aus gr. Tidrog, sondern aus einer
                                                                   iran.


      9 novjog nicht nach Ehrlich KZ. 40, 359, A. 1 mit                            .Tora.«oV   und cioxsidd^cov   als
*q^O‘n4os zu verbinden.
                                                                                               ;   ^




                                                        per-                                                       27


Mundart, vgL av.             denkt Kluge Wb. an speziell skythischen.
                                          u. zw.
Much AfdA. 27, 124 an jazygischen Ursprung.
#### 5560-5585
                                                                                          6*
84                                              pulo-    — ptel(e)ia
 pulo- jjSteifes Haar'',
      Ai. pulahy puJaka-h „das Strauben                      der Harchen      am Korper‘‘, piilarU-h
^schlichtes      Hauptbaar tragend“.
      GT.nvXiyyeg’ at ev rfj edga rgiyeg' xai YovXoi, ^ootqvxoi, ^iTavvoiHes,;
air.    ulcJia „Bart'*', ulfota „langbartig“,                Ulaid „die Ulsterleute^ {aus ^^UUdi),
vielleicbt   auch gall, Triulaitl YN. ..^laTiQOJzcoycovsg'^".
      Bezzenberger-Fick BB. 6, 239, Fick       487, 11^ 55, Pedersen KG. I 47,
— Lat. pilus           8.   u.   *pilo- „Haar“.


pnsti- (oder pnqsti-, pnq^sti-?) „Faust'^
   AhA, fust^ ags. fi/st=sihg. pesh „Faust“. Einstigen Gutt.nach n ev-
wagt man eiuerseits unter Ankniipfung an penq^e „funf” („die geschlossenen
funf Finger“ ganz fraglich) und das ebenfalls an die Fiinfzabl angeknupfte
                 ;


germ. Finger, andrerseits wegen lit. kiimsie ,,Faust'‘ aus "^kumpste, das aus
^punkste umgestellt sei, wobei ti entweder aus dm^cli die labiale Umgebung
bedingter zi-Farbigkeit des n oder durch alte Entlehnung aus dem Germ,
erklart wird letzteres besonders unwahrscheinlich, aber auch ersteres wegen
                 ;


des Gegensatzes zur slav. Yokalisierung mindestens ganz unsicher; ich
verbinde kum(*p)ste lieber mit kumpas ,,krumm“ s. qamp- ,,biegen‘'. Ygl.
Saussure Msl. 7, 93, J. Schmidt Yoc. I 167 f., Fick   4S4, Kluge \Yb. ^ s. v.
Sabeer KZ. 31, 279, Brugmann        410, 586, 875,  II^   438, Medermann
IF. 26, 45.
  Yerlust eines Gutt. nimmt auch Persson Beitr. 245 an unter unbefriedi-
gendem AnschluB an aksl. paciti, lat. pamis (s. pang „schwellen“).

prso- „Lauch“.
  Gr. jigdoov „Lauch“              =
#### find WP II 25 penkwe
1667:perjq^le „funf‘‘.
5569:wagt man eiuerseits unter Ankniipfung an penq^e „funf” („die geschlossenen
```


## [2026-09-14T00:57:45.723Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD\nsed -n '1660,1700p' WLD_Bd2_pages.txt"
}
```


### [2026-09-14T00:57:45.863Z] TOOL RESULT

```
thimus) fenea, finja „Polenta‘' (s. Gundermann ZfdtAYtf. 8, 116f.) und (nach
Pick I^ 135, 655) die von Athenaeus aus dor. Komikern angefuhrten navia
^.7t7.riopovrf^, ndvia ^Ttkrjopia'^'y die an          „Mangel“ (wohl rhythm.
Dehnung aus "^dnavia. s. u.           .,weh tun“) auch eine jon. oder att, Ent-
sprechung zu haben scheinen, so daB kaum illyrisch (trotz des Anklanges
an messap. navvg ,.panis'", s. u. poi-y pd- „A^ieh huten‘*).

perjq^le „funf‘‘.
    Ai. panca, av. panca\ arm. king (der alte Ausl. bewahrt in hnge-tasan
 „15“; Hubschmann Arm. Gr. I 467, Pedersen KZ. 39, 395 f.); gr. jteite,
 aol. TiEpjiE {7tEVTd>p0A0Vy TtEvrdg neben lautges. TZEpndy^oloVj nEpnag          toch.
                                                                                     ) ;


B.^/^; dS\y.pesEy geg.^f’5£(auf*2;c«^^“t/fl zuruckgefuhrt von G. Meyer Wb. 329,
auf "^peifKpie mit Palatalisierung des (pi zu s durch das foigende e von
Pedersen KZ. 36, 307); lat. qumque (7 nach (pil7i{c)tuSy Thurneysen KZ. 30,
 50 If. gegen W. Meyer ibd. 343 f.). osk.-umbr ^pompe (vgl. o. pumperias,
u. pumperias yyCpiinciiriae^^)     air. coic^ acymr. pimp^ me. nc. p^rng). corn.
pympy hret, pemp^            ^ruTiE-Sovka yjTZEvjdcfvAXov^^ got. fimf^ aisl. fimm^
ftiUy ahd. fimfy finp as. ags. fjf (der Gutt. noch in schwab. fuckze 15,

fiiclizh 50, Zupitza Gutt. 7; zum u dieser Formen, sowie ahd. fiinfy funf-
zicliy nhd, mdartl. fufzen. fufzich und des Ord. ahd. funftOy schwab. fuft

s. Brugmann II^ 2, 55 m. Lit.);       lit. penlci (flektiert);  2dog,pqihb {t aus          U
nach dem Ordinale ursprgl. kollektiv
                            ;
                                                     =
                                                  ai. pa^akti-h ,.Punfzahl*% aisl. fmt

f. „Anzahl     von fiinf**; auch umbr. punies wenn ..quiniones*^ woruber s.
hnen- ,,feiern”j.
    15: dl. panca-daqat, diY. pancadar a, arm. Imge-iasayi. gv. 7iEvzE{yMi)dEyMy
got. fimftaikun^ ahd. finfzehan.         50    ai. paned^af,
                                                 :             av. p)ancasaf»ni (acc.),
arm. yisim (Lit. zur Form bei Brugmann II^ 2, 33 f.), gr. jiEvigxovTa, lat.
quinquagintd (nach quadragintd)^ air. coica,
    Ordinale: "^penq^tos: Ely. puxda- (t^d.i. lu wohl nach '^(k)turtka- „vierter'‘,
s. Brugmann IP
                    2, 55 m. Lit.; y^\. payatakva- ..Funftek’)       gr. nipjtcogy lat.
```


## [2026-09-14T00:59:12.043Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"### SKT path\"; grep -n \"^Path,\\|Path, a way\\|Punch, a beverage\\|Punch (2)\\|Find, to\" SKT.txt | head -10\necho \"### SKT grep path\"; grep -n \"PATH, a way\\|Pfad\" SKT.txt | head -10\necho \"### LAT pons\"; grep -n \"pons, -tis\\|pons,\" LAT.txt | head -6\necho \"### LEW pons\"; grep -n \"pons,\" LEW_1910.txt | head -6"
}
```


### [2026-09-14T00:59:12.124Z] TOOL RESULT

```
### SKT path
### SKT grep path
### LAT pons
48785:pons, pontis m.: pont; passerelle. Atteste de tout temps. Pan-
48817:les anci ens comme un compos 4 de pons, cf. Varr., L.L. 5,83: pontufices...
48825:blance - qu'il y avait dans pons, pontifex un souvenir de la civili-
60054:spons, spontis f,: substantif usite seulement au gin.spontis
### LEW pons
```


## [2026-09-14T00:59:14.095Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '48785,48840p' LAT.txt"
}
```


### [2026-09-14T00:59:14.184Z] TOOL RESULT

```
pons, pontis m.: pont; passerelle. Atteste de tout temps. Pan-
roman. M. L.6649, et celt.: bri tt. pont-, quelques formes romanes sont
feminines, comme ont tendu a le devenir les mots en —is, ce qui
suppose sans doute un nominatif *pontis.
Derives et composes: ponticulus m.,M.L.665o; ponto,-onis m.: bac,
pont de bateau, ponton, M ; L.66ssi; pontilis,-e (Veg.); pontonium
(Isid., Or. 19,1); depontant: -i senes... qui sexagenarii de ponte
deficiebantur, ¥.F. 66 ,$ 1 ,.; et deponto,-as (Varr.); pontdrius = yecpupo-
pctTqC (Gloss.); pontarchus (inscr.).
Les langues indo-europeennes orientales ont pour "chemin" un mot
dont le vedique montre bien la flexiori singuliere: ion.sing. panthdh
~ ^v.panta, acc.s g.panthSm = a.v.pantam', gen. sing. pathdh = a v.paQS,
instr. pl. pathibhih et loc.pl. pathisw, le v.perse a pa&im ; le slave
et le 'vi.eux prussien ont normalise, le premi er avec vocalisme radical
0: poti, et le second avec vocalisme zero: pintis. Le mot ne se
retrouve clairement nulle part: l'armenien a hun "gue »; le grec
n f a que des formes th^matiques: toxtoc "chemin 11 et peut-etre 7iovxo£
"mer"(au sens de "lieu de passage"); le sens de osq. punttram est
douteux. Pour la forme, lat. pons serait superposable a Y.sl.ppti
(masc.); mais le sens fait difficulte. Les noms du "pont" varient
d'une langue a 1’autre, et meme a 1'interieur d'une merae langue,
comme on le voit par les formes grecques: att. yetpupct, beot. (Becpupa,
cr^t^Sscfopa, lac. Supoupa, et meme chez Hesychius j 3 ou<f> 6 pa£' yeepupac.
De meme en germanique v.isl.brM (cf. peut-^tre gaul.brtvo "pont")
ne concorde pas avec la forme elargie v.h.a .brucca, v.angi. brycg.
pontlcus, -a, -um: du Pont; adjectif derive de Pontus, applique
a des objets originaires de cette region: ponticae nuces "sorte de
noisettes", mus ponticus "hermine", etc. Est demeur£ dans ces acceptions
dans certains dialectes italiens, cf.M.L.6651; cf. aussi
sous pantex,
panticanus,
pontifex (pontufex), - ficis m.: pretre, pontife. - Considi par
les anci ens comme un compos 4 de pons, cf. Varr., L.L. 5,83: pontufices...
a ponte arbitror: nam ab his sublicius est factus primum ut restitutus
saepe, cum ideo sacra et uls et cis Tiberim non mediocri ritu fiant.
La securis (secespita ) qui fait partie des insignes du grand pontife
rappelle peut-etre leur preniore fonction: Rome est la "ville du
Pont"; c'est le point par ori normalement communique 1 'Italie du Nord
avec 1 'It alie du Sud, et le pont sur le Tibre est la raison d'etre
initiale de la ville. M. Bonfante a suppose — sans grande vraisem—
blance - qu'il y avait dans pons, pontifex un souvenir de la civili-
sation des palafittes; v. article cit (5 p.843. Plus tard le mot a
designe un membre du principal collbge des pretres romadns qui avait
la surveillance du culte officiel et public, et dont le chef (Stait
le pontifex maximus. Ancien terme du rituel, conserve par la langue- ga 3 - populus
r eligi eu se et offidelle. Non roman (sauf dans des formes sarutes;
de meme iri .pontific).
Ddrivds: pontificius ; pontificalis ; pontificatus,-as•, pontificium
(cf.Ldf stedt, Eranos XLIV 343)*
V. pVns.
pontus, -I ner; vague. Emprunt au gr.TiovTOC; attestd depuis
Ennius; uniquement podtique. Conposd: pontiuagus (Anti»Lat.).
popa, -ae n.: prfctre infdrieur, chargd de conduire la victime
k 1'autel et de 1'abattre avec un aaillet ou avec le cStd non tran-
chant de la hache (diffdrent du cultrSrius qui 1 'achevait arec le
couteau), et prdposd aussi k 1'entretien du feu, de 1'encens, etc.
```


## [2026-09-14T00:59:20.845Z] TOOL CALL #71: WebFetch

```json
{
 "url": "https://vajehyab.com/moein/%D9%BE%D9%86%D8%AC",
 "prompt": "Give the Mo'in (فرهنگ معین) entry for پنج: definition and any bracketed etymological note (e.g. [په.] پهلوی panǰ)."
}
```


### [2026-09-14T00:59:24.336Z] TOOL RESULT

```
# Mo'in Dictionary Entry for پنج

According to the Moein Dictionary (فرهنگ انتشارات معین) shown on this page, the entry states:

"و شش (پَ جُ ش ِ) (اِمر.) حواس پنجگانه و جهات شش گانه"

This indicates that پنج relates to the five senses (حواس پنجگانه) and is presented alongside شش (six), in reference to the six directions. The phonetic notation shows the Persian pronunciation, and the label (اِمر.) appears to mark it as imperative or related to command/awareness.
```


## [2026-09-14T00:59:31.099Z] TOOL CALL #72: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg392.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/392.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/392.png"
}
```


### [2026-09-14T00:59:31.164Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 75438 Sep 13 20:59 /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/392.png
```


## [2026-09-14T01:07:47.991Z] TOOL CALL #73: Write

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/page-392.json",
 "content": "{\n  \"pdf_page\": 392,\n  \"book_page\": 362,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-13\",\n  \"entries\": [\n    {\n      \"entry\": 1,\n      \"root\": \"Penkwe\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *pénkʷe 'five'\",\n      \"note\": \"Pokorny IEW p. 808 heads the entry 'Root/lemma: penk^e — Meaning: five', with the material Old Indic panca, Avestan panca, Armenian hing, Gk. πέντε, Lat. quinque, Goth. fimf … and the sub-sections B '15', C '50', D ordinals. Watkins/AHD prints 'penkve. Five.' and refers back to '[Pok. penkve 808, pnksti- 839.]'. Nourai's headword spelling 'Penkwe' is simply his Latin-letter rendering of *penkʷe; the language label 'Indo-European' and the gloss 'five' are both correct. The only reservation on the page concerns two of the Germanic derivatives (fist, and to a lesser degree finger), which Walde-Pokorny treats as an uncertain attachment to the numeral, and the English drink-word 'punch', whose received 'five ingredients' story modern lexicography rejects.\",\n      \"note_fa\": \"ریشهٔ هندواروپایی آغازین *pénkʷe «پنج» واقعی است و برچسب زبانی و معنای آن در نمودار درست است: پوکورنی در صفحهٔ ۸۰۸ فرهنگ ریشه‌شناسی هندواروپایی سرواژهٔ penkʷe را با معنای «پنج» آورده و شواهد سنسکریت panca، اوستایی panca، ارمنی hing، یونانی pente، لاتین quinque و گوتی fimf را برشمرده است؛ واتکینز (AHD) نیز همین ریشه را با ارجاع به پوکورنی ۸۰۸ ثبت کرده است. املای «Penkwe» صرفاً صورت لاتین‌نویسی نورایی از *pénkʷe است. تنها دو نکتهٔ محل تردید در این صفحه، پیوند واژه‌های ژرمنی «مشت» و «انگشت» با شمارهٔ پنج است — که والده‌ـ‌پوکورنی آن را «کاملاً مشکوک» می‌خواند — و ریشهٔ واژهٔ انگلیسی punch «نوشابه» که فرهنگ‌نویسی امروزی داستان «پنج ماده» را نمی‌پذیرد.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/p%C3%A9nk%CA%B7e\",\n        \"https://www.etymonline.com/word/five\"\n      ],\n      \"ref_check\": [\n        {\n          \"ref\": \"POK:808\",\n          \"status\": \"supports\",\n          \"note\": \"POK_full.txt line 66155 ff.: 'Root / lemma: penk^e | Meaning: five | Material: A. Old Indie panca, Avestan panda [= panca]; Armenian hing, gr. πεντε … Gothic fimf … References: WP. II 25 f., WH. II 407 f., Trautmann 213 f. | Page(s): 808.' Exactly the root, label and gloss Nourai prints.\"\n        }\n      ],\n      \"consulted\": [\n        {\n          \"src\": \"WLD\",\n          \"where\": \"Bd. II 25 f. (incoming/WLD/WLD_Bd2_pages.txt line 1667)\",\n          \"stance\": \"supports\",\n          \"note\": \"'penqʷe „fünf“. Ai. panca, av. panca; arm. hing …; gr. πεντε, aol. πεμπε …; lat. quinque …; got. fimf, aisl. fimm, ahd. fimf, finf, as. ags. fīf …' — with '15: ai. panca-daçat, av. pancadasa …' and '50: ai. pañcāśat, av. pancasatəm (acc.)'.\"\n        },\n        {\n          \"src\": \"AHD\",\n          \"where\": \"Watkins 1985 s.v. penkve (AHD_watkins1985.txt line 834)\",\n          \"stance\": \"supports\",\n          \"note\": \"'penkve. Five. I. Basic form *penke … 3. Assimilated form *kvenke in: a. Latin quinque … 4. Greek pente, five … 5. Sanskrit pañca, five: PUNCH¹; PACHISI. [Pok. penkve 808, pnksti- 839.]'\"\n        },\n        {\n          \"src\": \"IEC\",\n          \"where\": \"Mann col. s.v. penque (IEC.txt line 12677)\",\n          \"stance\": \"supports\",\n          \"note\": \"'penque \\\"five\\\"; penqutis \\\"group of five\\\" — Sk. pañca; Av. pañca; Per. panj (pang); OPer. cf. pa(n)ca-; Oss. fondz; … Go. fimf; OE fif; OHG fimf, finf … WP II, 25ff.'\"\n        }\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan\",\n          \"words\": \"panca; pancâsas\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Avestan panca 'five' is the regular Old Iranian continuation of PIE *pénkʷe: the labiovelar *kʷ was palatalised to Indo-Iranian *č before the front vowel *e (PII *pánča), giving Av. panca = Sanskrit páñca, while the final *-e became -a. 'Fifty' is the compound *pénkʷe-dḱomt- 'five tens' (see Nourai's root Dekm): Avestan pancāsat-, whose nominative singular is pancasą̊s — this is exactly the form Nourai prints as 'pancâsas', and it is the form Gharib quotes as the source of Sogdian pnc's. Pokorny gives the accusative pancasatəm; Bartholomae lists the stem as pancasant- 'fünfzig'.\",\n          \"derivation_fa\": \"واژهٔ اوستایی panca «پنج» دنبالهٔ منظم *pénkʷe هندواروپایی آغازین است: واک‌ لبی‌ـ‌کامی *kʷ پیش از واکهٔ پیشین *e در ایرانی‌ـ‌هندی به *č کامی شده و *pánča به دست آمده است (همان páñca سنسکریت). «پنجاه» ترکیب *pénkʷe-dḱomt- «پنج دَه» است که در اوستایی pancāsat- شده؛ صورت نهادی مفرد آن pancasą̊s است و همین صورت است که نورایی «pancâsas» نوشته و قریب نیز آن را خاستگاه pnc's سغدی دانسته است. پوکورنی صورت رایی pancasatəm و بارتولمه ستاک pancasant- «پنجاه» را ثبت کرده‌اند. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/p%C3%A9nk%CA%B7e\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"POK:808\",\n              \"status\": \"supports\",\n              \"note\": \"POK_full.txt p. 808: 'Old Indie panca, Avestan panca' and 'C. 50: pañcāśat, Avestan pancasat …' — both of Nourai's Avestan words stand on the cited page.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"BRT\",\n              \"where\": \"Altiranisches Wb. s.v. panca-sant- (BRT.txt line 15262)\",\n              \"stance\": \"supports\",\n              \"note\": \"'j. panca-sant- fem. Zw. \\\"fünfzig\\\": paitica hi anya dva vā nara aŋhaiti panca vā °satəm …; Ableit. — ai. pañcāśát- f., np. panjāh.' Bartholomae's own note connects it to NP panjāh. Av. panca 'fünf' is quoted passim (e.g. 'panca narš \\\"fünf Männer\\\" V. 13.10', BRT.txt line 2899).\"\n            },\n            {\n              \"src\": \"WLD\",\n              \"where\": \"Bd. II 25 f.\",\n              \"stance\": \"supports\",\n              \"note\": \"'Ai. panca, av. panca' and '50: ai. pañcāśat, av. pancasatəm (acc.)'.\"\n            },\n            {\n              \"src\": \"AHD\",\n              \"where\": \"Watkins 1985 s.v. penkve\",\n              \"stance\": \"partial\",\n              \"note\": \"Watkins gives 'Compound *penke-(d)konta, \\\"five tens,\\\" fifty' but cites only the Latin and Greek reflexes (quinquāgintā, pentēkonta); the Avestan forms he leaves to Pokorny.\"\n            }\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Sogdian\",\n          \"words\": \"pncw, pnz, pnc; pnc`s\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"The Sogdian forms are exactly right. Gharib's dictionary, entry 6878 (on the cited page 276), reads 'pnc — panč/panǰ — <Av. panca — acc. -w; ob. -y — five', i.e. the Buddhist/Christian spelling pnc, the accusative pncw and (entry 6921) the Manichaean spelling pnz /panǰ/; entry 6880 'pnc's — pancas — <Av. pancasą̊s — fifty'. The reservation is about the arrow, not the forms: Sogdian is not descended from Avestan but is a sister Middle Iranian language, so pnc /panč/ continues Proto-Iranian *panča directly; Gharib's '<Av. panca' is her way of citing the Old Iranian cognate, and Nourai's chart (like the book's convention elsewhere) lets the Avestan box stand proxy for Old Iranian. The -z of Manichaean pnz shows the Sogdian voicing/affricate spelling of č > ǰ, the same development as Middle Persian pnz beside pnc.\",\n          \"derivation_fa\": \"صورت‌های سغدی درست‌اند: در فرهنگ سغدی بدرالزمان قریب، مدخل ۶۸۷۸ در همان صفحهٔ ۲۷۶ که نورایی ارجاع داده آمده است «pnc — panč/panǰ — <اوستایی panca — رایی: -w، غیرمستقیم: -y — پنج»، و مدخل ۶۹۲۱ صورت مانوی pnz، و مدخل ۶۸۸۰ «pnc's — pancas — <اوستایی pancasą̊s — پنجاه». نکتهٔ محل احتیاط خودِ پیکان است نه صورت‌ها: سغدی از اوستایی نیامده، بلکه زبانی ایرانی میانه و خواهرِ آن است و panč سغدی مستقیماً دنبالهٔ ایرانی آغازین *panča است؛ نشانهٔ «<Av.» در فرهنگ قریب تنها اشاره به هم‌ریشهٔ ایرانی باستان است. در نمودار نورایی، مانند دیگر جاهای کتاب، جعبهٔ «اوستایی» جانشین «ایرانی باستان» شده است. -z در صورت مانوی pnz نمایندهٔ واک‌دار شدن č > ǰ است، همان تحولی که در فارسی میانه نیز pnz در کنار pnc دیده می‌شود.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D9%BE%D9%86%D8%AC\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"SOD:276\",\n              \"status\": \"supports\",\n              \"note\": \"SOD.txt, the form-feed block whose running head is 'pnc | 276', carries entries 6878 pnc 'panč/panǰ ©<Av. panca ©acc. -w; ob. -y ⇒pnz — five', 6879 pnc'm 'pancam — fifth', 6880 pnc's 'pancas ©<Av. pancasą̊s — fifty', 6885 pnc5s 'panc-δas ©<*panca-dasa — fifteen'. The cited page number is exact.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"SOD\",\n              \"where\": \"Gharib nos. 6878, 6880, 6921\",\n              \"stance\": \"supports\",\n              \"note\": \"no. 6921 'pnz M — panj ⇒pnc — five — GMS 67' gives the Manichaean variant Nourai lists as 'pnz'.\"\n            },\n            {\n              \"src\": \"PHD\",\n              \"where\": \"MacKenzie p. 63 s.v. panj\",\n              \"stance\": \"supports\",\n              \"note\": \"'panj [pnc | P pnyz, (M pnz), N ~] five' — the same Middle Iranian spelling pattern (Book Pahlavi pnc, Manichaean pnz) as in Sogdian, confirming that pnc/pnz are two orthographies of one word.\"\n            },\n            {\n              \"src\": \"IEC\",\n              \"where\": \"Mann s.v. penque\",\n              \"stance\": \"silent\",\n              \"note\": \"Mann lists Skt., Av., Persian and Ossetic but no Sogdian form.\"\n            }\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Persian\",\n          \"words\": \"panj «پنج»; panjeh «پنجه»; pânzdah «پانزده»; pânsad «پانصد»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"پنج panj continues Middle Persian panj (Book Pahlavi pnc, Manichaean pnz) < Proto-Iranian *panča < PIE *pénkʷe; MacKenzie s.v. 'panj [pnc | P pnyz, (M pnz), N ~] five'. پنجه panja/panje is MP panjag [pnck'] 'pentad; hand, paw' with the regular loss of final -g/-ag > NP -a/-e; Horn no. 328 gives 'penje \\\"Faust\\\" … phlv. pančak \\\"Faust\\\"', so the gloss 'hand (five fingers)' is right (hand/paw/claw, hence also پنجول 'claw'). پانزده pānzdah is MP panzdah [p'ncdh] < Av. pancadasa 'five-ten' (see Nourai's Dekm), the ā of the first syllable arising from compensatory lengthening when the nasal was lost before the cluster -zd-; پانصد pānsad is the same pān- (compositional form of panj) + sad 'hundred'. The Persian-script extras the book adds are all transparent derivatives: پنجگان، پنجم، پنجمین (ordinals in -om/-omin), پنجاب (panj + āb 'five waters'), پنجک، پنجول.\",\n          \"derivation_fa\": \"«پنج» دنبالهٔ فارسی میانهٔ panj (پهلوی کتابی pnc، مانوی pnz) است، از ایرانی آغازین *panča و آن از *pénkʷe هندواروپایی؛ مکنزی ذیل panj می‌نویسد «panj [pnc | P pnyz, (M pnz), N ~] پنج». «پنجه» از panjag پهلوی [pnck'] «پنج‌تایی؛ دست، چنگال» است که -ag پایانی طبق قاعده در فارسی نو به -ه بدل شده؛ هرن در شمارهٔ ۳۲۸ صورت penje «مشت» را با اصل پهلوی pančak آورده است، پس معنای «دست (پنج انگشت)» درست است (و از همین‌جاست «پنجول»). «پانزده» از panzdah پهلوی [p'ncdh] و آن از pancadasa اوستایی «پنج‌ده» است؛ الفِ کشیدهٔ آغاز از افتادن غنّه پیش از خوشهٔ -zd- و کشش جبرانی پدید آمده است. «پانصد» نیز همان صورت ترکیبی pān- + «صد» است. افزوده‌های فارسی کتاب (پنجگان، پنجم، پنجمین، پنجاب، پنجک، پنجول) همگی مشتق‌های آشکار همین واژه‌اند. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D9%BE%D9%86%D8%AC\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"BQT:419\",\n              \"status\": \"supports\",\n              \"note\": \"Borhan-e Qate' vol. 1 (BQT_v1_pages.txt, form-feed leaf 646-647, printed p. ≈419-422 by the file's offset table) is the پنج section: headwords پنجاب، پنج‌انگشت («… معروف است و نام نباتی هم هست که آن را دلاشوب خوانند … و آن را عربی ذو خمسة اوراق و ذو خمسة اصابع خوانند»)، پنجاهه، پنجه («بفتح اول و خفای آخر بر وزن گنجه، معروف است که پنج انگشت با کف دست است»). Independent corroboration of the page number: Aryanpur's پنج entry (ARY_pages.txt, printed p. 175) closes with the citation «برهان قاطع: ۴۱۹».\"\n            },\n            {\n              \"ref\": \"MON\",\n              \"status\": \"not_checked\",\n              \"note\": \"Nourai gives no page for Mo'in here; the local MON_part1/2 OCR does not contain the پنج headword block and vajehyab's Mo'in query for پنج returns only compounds (پنج و شش), so the citation could not be pinned to a page.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"PHD\",\n              \"where\": \"MacKenzie p. 63 s.vv. panj, panjag, panjāh, panzdah\",\n              \"stance\": \"supports\",\n              \"note\": \"'panj [pnc | P pnyz, (M pnz), N ~] five. ~ag [-k' | N ~a] pentad; hand, paw. ~āh [-h | N ~] fifty. panzdah [p'ncdh | M p'nzdh, N ~] fifteen.' — every one of Nourai's four Persian words has its Middle Persian antecedent here.\"\n            },\n            {\n              \"src\": \"HRN\",\n              \"where\": \"Horn, Grundriss no. 328 (p. 73)\",\n              \"stance\": \"supports\",\n              \"note\": \"'328. penj \\\"fünf\\\", penjum \\\"fünfter\\\", penje \\\"Faust\\\". — aw. panča \\\"fünf\\\"; phlv. panč, pančum, pančak \\\"Faust\\\"; ai. páñca; arm. hing.' No. 329: 'penjāh \\\"fünfzig\\\" — aw. pancāsata-; phlv. pancāh.'\"\n            },\n            {\n              \"src\": \"HUB\",\n              \"where\": \"Hübschmann, Persische Studien (HUB.txt lines 4385, 4630)\",\n              \"stance\": \"supports\",\n              \"note\": \"'np. panjum \\\"der fünfte\\\", paz. panjum …, phl. panjum = zd. pancama-' and 'np. panj \\\"fünf\\\", zd. pancadasa \\\"fünfzehn\\\"'.\"\n            },\n            {\n              \"src\": \"ARY\",\n              \"where\": \"Aryanpur, Farhang-e Rishe-ha, printed pp. 175-177 (پنجاه، پنجه)\",\n              \"stance\": \"supports\",\n              \"note\": \"Aryanpur files پنج/پنجاه/پنجه under one PIE root with Avestan, Old Persian, Pahlavi, Sanskrit, Greek, Latin and Germanic cognates, and cross-refers پنجه and پانزده back to پنج ('بازگشت به: پنج'; 'بازگشت به: پنج و ده').\"\n            }\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Sanskrit\",\n          \"words\": \"panca\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Sanskrit páñca 'five' (Rigvedic) is the Indo-Aryan twin of Avestan panca: PIE *pénkʷe > PII *pánča by the satem palatalisation of *kʷ before *e. It is the immediate source of Prakrit pañca and of the modern Indo-Aryan forms (Hindi pāñc), which are what actually reach English in the words listed below.\",\n          \"derivation_fa\": \"páñca سنسکریت «پنج» (از ریگ‌ودا) همتای هندوآریایی panca اوستایی است: *pénkʷe هندواروپایی در شاخهٔ ایرانی‌ـ‌هندی با کامی‌شدن *kʷ پیش از *e به *pánča بدل شده است. همین صورت است که در پراکریت pañca و در زبان‌های نوین هندوآریایی (هندی pāñc) دنباله یافته و در واقع از راه هندی به انگلیسی رسیده است، نه یکراست از سنسکریت.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/p%C3%A9nk%CA%B7e\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"AHD\",\n              \"status\": \"supports\",\n              \"note\": \"Watkins 1985 s.v. penkve, I.5: 'Sanskrit pañca, five: PUNCH¹; PACHISI.' — exactly the branch Nourai draws.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"POK\",\n              \"where\": \"IEW 808\",\n              \"stance\": \"supports\",\n              \"note\": \"'Material: A. Old Indie panca, Avestan panca …'\"\n            },\n            {\n              \"src\": \"WLD\",\n              \"where\": \"Bd. II 25\",\n              \"stance\": \"supports\",\n              \"note\": \"'Ai. panca, av. panca'.\"\n            },\n            {\n              \"src\": \"IEC\",\n              \"where\": \"Mann s.v. penque\",\n              \"stance\": \"supports\",\n              \"note\": \"'Sk. pañca; Av. pañca; Per. panj (pang)'.\"\n            }\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"English\",\n          \"words\": \"punch; Punjab\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"Both words in this box are misdrawn, in different degrees. (a) punch 'the beverage': the chart follows the standard 19th-20th c. account — Hindi pāñč (< Skt. páñca) 'five', because the drink had five ingredients (spirit, sugar, lemon, water, spice) — which is what Klein and Watkins print. But this is the one etymology on the page that modern lexicography rejects: the OED and Etymonline record that no drink called *panch is attested in India (or anywhere) before the English word, that English 'punch' is attested before the English were regular traders in the Indies, and that there are phonetic and historical difficulties; the five-ingredient story goes back only to John Fryer's account of 1698. The favoured alternative is a sailors' shortening of puncheon, the c. 70-gallon liquor cask (ME poncion, from OF poinçon), possibly crossed with paunch (older spelling 'paunche pot'). (b) Punjab is not from Sanskrit at all: it is Hindi/Urdu Panjāb, borrowed from Persian panj-āb 'five waters' (the five rivers of the Indus system), i.e. from node #3 of this same chart, not from the Sanskrit box it hangs under; Nourai's own cross-reference ☞Ab 1 shows he knew the second element was Persian āb.\",\n          \"derivation_fa\": \"هر دو واژهٔ این جعبه نادرست جای گرفته‌اند. نخست punch «نوشابه»: نمودار روایت رایج سدهٔ نوزدهم و بیستم را آورده است — از pāñč هندی (< páñca سنسکریت) «پنج»، چون نوشابه پنج ماده داشت — همان‌که کلاین و واتکینز نیز نوشته‌اند؛ اما پژوهش امروزی (فرهنگ آکسفورد و اتیمآنلاین) آن را رد می‌کند: هیچ نوشابه‌ای به نام panch پیش از پیدایش واژهٔ انگلیسی در هند گواهی نشده، واژهٔ انگلیسی پیش از آغاز دادوستد منظم انگلیسی‌ها با هند به کار رفته، و اشکال‌های آوایی و تاریخی دارد؛ داستان «پنج ماده» تنها به گزارش جان فرایر در ۱۶۹۸ بازمی‌گردد. جانشین محتمل‌تر، کوتاه‌شدهٔ دریانوردانهٔ puncheon «خمرهٔ حدود هفتاد گالنی» است. دوم Punjab: این نام اصلاً سنسکریتی نیست، بلکه Panjāb هندی/اردو و وام‌گرفته از «پنج‌آب» فارسی است (پنج رود سند)، یعنی از جعبهٔ شمارهٔ ۳ همین نمودار، نه از جعبهٔ سنسکریت؛ ارجاع خودِ نورایی به ریشهٔ «آب» نشان می‌دهد که جزء دوم را فارسی می‌دانسته است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/punch\",\n            \"https://www.etymonline.com/word/Punjab\",\n            \"https://www.etymonline.com/word/five\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"AHD\",\n              \"status\": \"partial\",\n              \"note\": \"Watkins 1985 s.v. penkve routes 'Sanskrit pañca, five' to PUNCH¹ (and PACHISI) — so the reference does support the punch arrow as drawn, but it says nothing about Punjab, and it states the traditional etymology without the OED's caveats.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein 1966 s.v. punch 'a beverage' (KLN_1966.txt line 31000)\",\n              \"stance\": \"supports\",\n              \"note\": \"'punch, n., a beverage. — Hind. pañch, fr. OI. pañca, \\\"five\\\", which is cogn. with Gk. πέντε, L. quinque, Goth. fimf, OE. fīf (see five …); so called because orig. the punch was composed of five ingredients.' Note that Klein, unlike the chart, inserts Hindi between Sanskrit and English.\"\n            },\n            {\n              \"src\": \"WEB\",\n              \"where\": \"Etymonline s.v. punch (n.2) [online, archived]\",\n              \"stance\": \"contradicts\",\n              \"note\": \"'There is no evidence of a drink called panch in India, or elsewhere, before the English word; and the English word is now known to have been in use before the English became regular traders to the Indies …' — the modern view; the beverage may instead be named from the cask (puncheon).\"\n            },\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein 1966 s.v. puncheon 'a large cask'\",\n              \"stance\": \"partial\",\n              \"note\": \"'puncheon, n., a large cask. — ME. poncion, fr. OF. poinchon, poinçon, ponçon, \\\"wine vessel\\\".' This is the word modern lexicographers propose as the real source of the drink-name.\"\n            }\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"Persian\",\n          \"words\": \"pânč «پانچ»\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"پانچ (also spelt پُنچ) is a modern re-borrowing into Persian of the English word punch, so the round trip drawn here — Indo-Aryan pāñč > English punch > Persian pānč — is real as a route of borrowing, and Mo'in marks the headword [انگ.] 'English'. Two qualifications. First, what Mo'in's own entry for پانچ actually defines is the other English 'punch', the perforating tool («دستگاه یا وسیله‌ای که کاغذها را با آن سوراخ و باطل کنند، منگنه») and the computing sense of punched cards; the beverage sense with the 'five fruits' explanation is the one carried by Dehkhoda and the compiled dictionary sites, so Nourai's gloss is attested but not obviously on the page he cites. Second, the 'five' etymology inside the English word is itself doubted (see node #5), so the semantic motive Nourai gives ('a drink made of several (five) fruits') is folk-etymological rather than established.\",\n          \"derivation_fa\": \"«پانچ» (و صورت «پُنچ») وام‌واژه‌ای نو از punch انگلیسی است؛ پس رفت‌وبرگشتی که نمودار می‌کشد — pāñč هندوآریایی ← punch انگلیسی ← «پانچ» فارسی — از نظر مسیر وام‌گیری درست است و معین هم سرواژه را با نشانهٔ [انگ.] آورده است. دو نکته: نخست آنکه آنچه در متن معین ذیل «پانچ» تعریف شده، معنای دیگر punch یعنی «منگنه/سوراخ‌کن کاغذ» و کارت‌های پانچ رایانه‌ای است؛ معنای نوشابه و توضیح «پنج میوه» را دهخدا و فرهنگ‌های گردآوری‌شده آورده‌اند، پس معنای مورد نظر نورایی گواهی دارد ولی روشن نیست که در همان صفحهٔ ارجاع‌شده باشد. دوم آنکه پیوند خودِ واژهٔ انگلیسی با «پنج» امروزه مشکوک است (نگاه کنید به گرهٔ ۵)، پس انگیزهٔ معنایی «نوشابه‌ای از پنج میوه» بیشتر ریشه‌شناسی عامیانه است تا واقعیت تاریخی.\",\n          \"sources\": [\n            \"https://vajehyab.com/moein/%D9%BE%D8%A7%D9%86%DA%86\",\n            \"https://abadis.ir/fatofa/%D9%BE%D8%A7%D9%86%DA%86/\",\n            \"https://www.etymonline.com/word/punch\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"MON:822\",\n              \"status\": \"partial\",\n              \"note\": \"Mo'in's پانچ is confirmed to exist and to be marked [انگ.] (vajehyab.com/moein/پانچ), but the text returned there gives only the senses 'منگنه / سوراخ‌کردن کارت' — the perforator, not the drink. The beverage sense with the five-ingredient note appears in the Dehkhoda material aggregated at abadis.ir. The volume/page 822 could not be checked directly: the local MON OCR files do not contain the پانچ block.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"MON\",\n              \"where\": \"Farhang-e Mo'in s.v. پانچ (via vajehyab)\",\n              \"stance\": \"partial\",\n              \"note\": \"'[انگ.] دستگاه یا وسیله‌ای که کاغذها را با آن سوراخ و باطل کنند، منگنه' — the English origin is confirmed, the gloss differs from Nourai's.\"\n            },\n            {\n              \"src\": \"ARY\",\n              \"where\": \"Aryanpur, Farhang-e Rishe-ha (grep پانچ/پنچ)\",\n              \"stance\": \"silent\",\n              \"note\": \"No entry for پانچ; Aryanpur covers only inherited Persian vocabulary.\"\n            },\n            {\n              \"src\": \"WEB\",\n              \"where\": \"Etymonline s.v. punch (n.2)\",\n              \"stance\": \"partial\",\n              \"note\": \"Confirms that the word Persian borrowed is the English drink-name, while rejecting its supposed Indic 'five' origin.\"\n            }\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"Germanic\",\n          \"words\": \"finfi; fingwraz; funh-stiz\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"The three forms are taken straight from the AHD appendix, but only the first is uncontroversial. (a) 'finfi': the numeral is Proto-Germanic *fimf, from *pempe, an assimilated form of *pénkʷe (initial p- > f- by Grimm's law, medial *-kʷ- assimilated to the initial nasal); Nourai's spelling with -n- reproduces the Old High German variant finf (beside fimf), and the -i is the Watkins/Pokorny way of writing the final vowel. (b) *fingwraz 'finger' is Watkins's reconstruction of a suffixed *penkʷ-ro- 'one of the five' (Goth. figgrs, OE finger); Pokorny already writes '*fingʷraz, Indo-Germanic *penkʷrós' but prefixes it with 'compare perhaps'. (c) *funh-stiz 'fist' is *pn̥kʷ-sti- (OE fȳst, OHG fūst, cogn. OCS pęstь). Walde-Pokorny treats this last attachment as distinctly shaky: under 'pnsti- (oder pnqsti-, pnqʷsti-?) \\\"Faust\\\"' they say the former guttural after the nasal is weighed 'unter Anknüpfung an penqʷe \\\"fünf\\\" (\\\"die geschlossenen fünf Finger\\\" ganz fraglich)'. So: numeral certain, finger likely, fist uncertain.\",\n          \"derivation_fa\": \"هر سه صورت از پیوست ریشه‌های هندواروپایی AHD گرفته شده‌اند، اما تنها نخستین آن‌ها بی‌چون‌وچراست. «finfi»: صورت ژرمنی آغازین *fimf است از *pempe، گونهٔ همگون‌شدهٔ *pénkʷe (پِ آغازین بر پایهٔ قانون گریم به f بدل شده و *-kʷ- میانی با غنّهٔ آغازین همگون شده)؛ املای نورایی با -n- همان گونهٔ آلمانی علیای باستان finf در کنار fimf است. «fingwraz» بازسازی واتکینز از *penkʷ-ro- «یکی از پنج» است (گوتی figgrs، انگلیسی باستان finger) که پوکورنی هم آن را با قید «شاید» می‌آورد. «funh-stiz» از *pn̥kʷ-sti- «مشت» است (انگلیسی باستان fȳst، آلمانی باستان fūst، هم‌ریشه با pęstь اسلاوی کهن)؛ ولی والده‌ـ‌پوکورنی این پیوند را «کاملاً مشکوک» (ganz fraglich) می‌خواند. پس: عدد قطعی، «انگشت» محتمل، و «مشت» نامطمئن است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/p%C3%A9nk%CA%B7e\",\n            \"https://www.etymonline.com/word/five\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"AHD\",\n              \"status\": \"supports\",\n              \"note\": \"Watkins 1985 s.v. penkve: 'Assimilated form *pempe in Germanic *fimf … IV. Suffixed form *penkv-ro- in Germanic *fingwraz, finger (< \\\"one of five\\\") … V. Suffixed reduced zero-grade form *pnk-sti- in Germanic *fu(nh)stiz.' Nourai's three forms are Watkins's three forms verbatim, apart from finf(i)/fimf.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"POK\",\n              \"where\": \"IEW 808 (penk^e) and 839 (pn̥ksti-)\",\n              \"stance\": \"partial\",\n              \"note\": \"p. 808: 'Gothic fimf, Old Icelandic fimm, Old High German fimf, finf …' and, for the finger, 'compare perhaps Old Irish coicer \\\"number from five\\\" and Gothic figgrs, Old Icelandic fingr, Old English finger … (*fingʷraz, Indo Germanic *penkʷrós)' — note Pokorny's 'compare perhaps'.\"\n            },\n            {\n              \"src\": \"WLD\",\n              \"where\": \"Bd. II 84 s.v. pnsti- (incoming/WLD/WLD_Bd2_pages.txt line 5565 ff.)\",\n              \"stance\": \"contradicts\",\n              \"note\": \"'pnsti- (oder pnqsti-, pnqʷsti-?) \\\"Faust\\\". Ahd. fūst, ags. fȳst = abg. pęstь \\\"Faust\\\". Einstigen Gutt. nach n erwägt man einerseits unter Anknüpfung an penqʷe \\\"fünf\\\" (\\\"die geschlossenen fünf Finger\\\" ganz fraglich); und das ebenfalls an die Fünfzahl angeknüpfte germ. Finger …' — Walde-Pokorny doubt the fist-from-five link.\"\n            },\n            {\n              \"src\": \"IEC\",\n              \"where\": \"Mann s.v. penqueros (IEC.txt line 12678)\",\n              \"stance\": \"partial\",\n              \"note\": \"'penqueros \\\"fivesome\\\" … OHG (and com. Gmc.) fingar (finger. Here?)' — Mann too marks the finger with a query.\"\n            }\n          ]\n        },\n        {\n          \"id\": 8,\n          \"lang\": \"English\",\n          \"words\": \"five, fifty, fifteen; finger; fist\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"five < ME fif < OE fīf < PGmc *fimf (the nasal was lost before the fricative with compensatory lengthening, the West Germanic 'Ingvaeonic nasal spirant law'); fifteen < OE fīftīene (*fimf + *tehun 'ten', see Dekm); fifty < OE fīftig. finger < OE finger, PGmc *fingraz, referred by Watkins to *penkʷ-ro- 'one of the five' — Klein records the same idea more cautiously: 'prob. rel. to five and cogn. with Arm. hinger-ord, \\\"the fifth\\\" (see A. Meillet, BSL 1928)'. fist < OE fȳst, PGmc *fūsti- < *funhsti-, cognate with OCS pęstь, Russ. piastʹ; its derivation from the numeral is what Walde-Pokorny call 'ganz fraglich', and Klein's fist entry lists the Slavic cognates without mentioning five at all. Hence the node as a whole is only plausible: the numerals and (probably) finger are secure, fist is not.\",\n          \"derivation_fa\": \"five از ME fif و OE fīf و ژرمنی آغازین *fimf است (غنّه پیش از سایشی افتاده و واکه کشیده شده — همان «قانون سایشی‌ـ‌غنّه‌ای» ژرمنی غربی)؛ fifteen از fīftīene انگلیسی باستان (*fimf + *tehun «ده») و fifty از fīftig. finger از finger انگلیسی باستان و *fingraz ژرمنی است که واتکینز آن را به *penkʷ-ro- «یکی از پنج» بازمی‌گرداند؛ کلاین محتاطانه‌تر می‌نویسد «احتمالاً مربوط به five و هم‌ریشه با hinger-ord ارمنی \\\"پنجم\\\" (میه، ۱۹۲۸)». fist از fȳst انگلیسی باستان و *fūsti- < *funhsti- است، هم‌ریشه با pęstь اسلاوی کهن؛ ولی پیوند آن با عدد پنج را والده‌ـ‌پوکورنی «کاملاً مشکوک» خوانده و کلاین نیز در مدخل fist هیچ اشاره‌ای به «پنج» نکرده است. از این رو کل این گره «با احتیاط پذیرفتنی» است: اعداد و (به احتمال زیاد) «انگشت» استوارند، «مشت» نه.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/five\",\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/p%C3%A9nk%CA%B7e\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"AHD\",\n              \"status\": \"supports\",\n              \"note\": \"Watkins 1985 s.v. penkve routes FIVE, FIFTEEN, FIFTH, FINGER, FIST (and FOIST) to this root; the index confirms 'FIVE penkYe', 'FIFTEEN penkWe', 'FINGER penkWe', 'FIST penkwe'.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein 1966 s.vv. five, finger, fist (KLN_1966.txt lines 14804, 14761, 14793)\",\n              \"stance\": \"partial\",\n              \"note\": \"five: 'ME. fif, fr. OE. fīf … fr. I.-E. *penqwe (with assimilation of qw to initial p)'; finger: 'prob. rel. to five and cogn. with Arm. hinger-ord, \\\"the fifth\\\"'; fist: 'ME. fust, fist, fr. OE. fȳst, rel. to OS., OHG. fūst … and cogn. with OSlav. pęstь, Russ. piastʹ, \\\"fist\\\"' — no mention of 'five' in the fist entry.\"\n            },\n            {\n              \"src\": \"WLD\",\n              \"where\": \"Bd. II 84 s.v. pnsti-\",\n              \"stance\": \"contradicts\",\n              \"note\": \"The fist-from-five connection is called 'ganz fraglich'.\"\n            },\n            {\n              \"src\": \"IEC\",\n              \"where\": \"Mann s.vv. penque, penqueros\",\n              \"stance\": \"supports\",\n              \"note\": \"'Go. fimf; OE fif; OHG fimf, finf; Du. vijf; ON fimm …' and, for the finger, 'OHG (and com. Gmc.) fingar (finger. Here?)'.\"\n            }\n          ]\n        },\n        {\n          \"id\": 9,\n          \"lang\": \"Greek\",\n          \"words\": \"pente\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Greek πέντε 'five' is the direct Attic-Ionic reflex of *pénkʷe: the labiovelar *kʷ became a dental t before the front vowel *e (the regular Greek treatment), while the Aeolic dialect assimilated it to the initial labial, giving πέμπε. The numeral appears in the compound πεντήκοντα 'fifty' and in the combining form πεντα-.\",\n          \"derivation_fa\": \"πέντε یونانی «پنج» بازتاب مستقیم *pénkʷe است: واک لبی‌ـ‌کامی *kʷ پیش از واکهٔ پیشین *e طبق قاعدهٔ یونانی به t دندانی بدل شده، حال آنکه در گویش آیولی با لبیِ آغازین همگون شده و πέμπε داده است. همین عدد در ترکیب πεντήκοντα «پنجاه» و در صورت ترکیبی -πεντα دیده می‌شود. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/p%C3%A9nk%CA%B7e\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"AHD\",\n              \"status\": \"supports\",\n              \"note\": \"Watkins 1985 s.v. penkve I.4: 'Greek pente, five: PENTA-, PENTAD; PENTACLE, PENTADACTYL, PENTAGON, PENTAMETER …'\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"POK\",\n              \"where\": \"IEW 808\",\n              \"stance\": \"supports\",\n              \"note\": \"'gr. πεντε, Aeolic πεμπε; πεμπαζειν \\\"an den 5 Fingern zählen\\\"'.\"\n            },\n            {\n              \"src\": \"WLD\",\n              \"where\": \"Bd. II 25\",\n              \"stance\": \"supports\",\n              \"note\": \"'gr. πεντε, aol. πεμπε (πενταωβολον, πενταϛ neben lautges. πεμπαμφολον, πεμπαϛ)'.\"\n            },\n            {\n              \"src\": \"IEC\",\n              \"where\": \"Mann s.v. penque\",\n              \"stance\": \"supports\",\n              \"note\": \"'Gk. pénte, cpds. penta-'.\"\n            }\n          ]\n        },\n        {\n          \"id\": 10,\n          \"lang\": \"English\",\n          \"words\": \"penta-, pentagon\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"penta- is the Greek combining form πεντα- taken into English learned vocabulary through Latin; pentagon is Greek πεντάγωνον 'five-angled (figure)' (πεντα- + γωνία 'angle'), borrowed through Middle French pentagone into English in the 1560s. These are learned borrowings, not inherited forms, so no sound changes intervene.\",\n          \"derivation_fa\": \"«-penta» همان صورت ترکیبی یونانی πεντα- است که از راه لاتین به واژگان علمی انگلیسی راه یافته، و pentagon از πεντάγωνον یونانی «پنج‌گوشه» (πεντα- + γωνία «زاویه») است که از راه فرانسهٔ میانه در سدهٔ شانزدهم وارد انگلیسی شده است. این‌ها وام‌واژه‌های عالمانه‌اند نه صورت‌های موروثی، پس دگرگونی آوایی در کار نیست. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/five\",\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/p%C3%A9nk%CA%B7e\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"AHD\",\n              \"status\": \"supports\",\n              \"note\": \"Watkins 1985 s.v. penkve I.4 lists PENTA-, PENTAD, PENTACLE, PENTAGON … under Greek pente; the AHD index line reads 'PENTA- penkWe PENTAGON penkwe'.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein 1966 s.v. penta- (KLN_1966.txt line 14805)\",\n              \"stance\": \"supports\",\n              \"note\": \"Klein's five/penta- cross-reference block: 'Cp. cinq(ue), kantar, keno, Panchatantra, panchayat, penta-, punch, \\\"a beverage\\\", quinary, quinque-.'\"\n            },\n            {\n              \"src\": \"IEC\",\n              \"where\": \"Mann s.v. penque\",\n              \"stance\": \"supports\",\n              \"note\": \"'Gk. pénte, cpds. penta-'.\"\n            }\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 2,\n      \"root\": \"Pent\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *pent- 'to tread, go; (nominal) path, way'\",\n      \"note\": \"Pokorny IEW 808-809 prints 'Root/lemma: pent- — Meaning: to go, walk; way — Note: (in Aryan with th)'; Walde-Pokorny II 26 has the fuller gloss 'treten, gehen, worauf treten, dazugelangen = antreffen, finden (vgl. venire : invenire); nominal \\\"Pfad, Weg\\\"', noting that the nominal derivative is often used of ways over wet ground — 'Prügelweg durch Sümpfe, Furt, Steg, Brücke'. Watkins/AHD: 'pent-. To tread, go.' Nourai's root, language label and gloss 'to go, pass' are all correct; the chart's only weak links are the Scythian mediation of Germanic *paþa- (see nodes #3-#4), which is a much-debated hypothesis, and the inclusion of 'advice' in the gloss of the Old Iranian box (node #1), which belongs to Middle Persian, not to Avestan or Old Persian.\",\n      \"note_fa\": \"ریشهٔ هندواروپایی آغازین *pent- «گام نهادن، رفتن؛ و در صورت اسمی: راه، گذر» واقعی است. پوکورنی در صفحه‌های ۸۰۸ـ۸۰۹ سرواژهٔ pent- را با معنای «رفتن، گام برداشتن؛ راه» و این یادداشت آورده است که «در آریایی با th». والده‌ـ‌پوکورنی (جلد دوم، ص ۲۶) معنای گسترده‌تری می‌دهد: «گام نهادن، رفتن، بر چیزی پا گذاشتن، به جایی رسیدن = برخوردن، یافتن (مانند venire : invenire)؛ و در کاربرد اسمی: راه، گذرگاه»، و می‌افزاید که صورت اسمی بیشتر دربارهٔ گذر از زمین‌های آبگیر به کار می‌رفته: «گذرگاه چوبی در باتلاق، گدار، پل». واتکینز نیز می‌نویسد «pent-. گام نهادن، رفتن». ریشه، برچسب زبانی و معنای نمودار درست است؛ تنها دو حلقهٔ سست، یکی میانجیگری سکایی در راهیابی واژه به ژرمنی است و دیگری افزودن معنای «پند» به جعبهٔ ایرانی باستان که در حقیقت تحولی فارسی میانه است.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/pent-\",\n        \"https://www.etymonline.com/word/path\"\n      ],\n      \"ref_check\": [\n        {\n          \"ref\": \"POK:808\",\n          \"status\": \"supports\",\n          \"note\": \"POK_full.txt line 66250 ff.: 'Root / lemma: pent- | Meaning: to go, walk; way | Note: (in Aryan with th) | Material: Old Indie panthāḥ (= Avestan pantā̊), Akk. Sg. panthām (= pantąm) … Old pers. Akk. Sg. paθim … References: WP. II 26 f., WH. II 336 f. … Page(s): 808-809.' The page number Nourai cites is exact.\"\n        }\n      ],\n      \"consulted\": [\n        {\n          \"src\": \"WLD\",\n          \"where\": \"Bd. II 26-27 s.v. pent- (incoming/WLD/WLD_Bd2_pages.txt line 1726 ff.)\",\n          \"stance\": \"supports\",\n          \"note\": \"'pent- (im Ar. mit th) „treten, gehen, worauf treten, dazugelangen = antreffen, finden“ (vgl. venire : invenire); nominal „Pfad, Weg“, mehrfach von über nasses Gelände oder Wasser führenden Pfaden, „Prügelweg durch Sümpfe, Furt, Steg, Brücke“.'\"\n        },\n        {\n          \"src\": \"AHD\",\n          \"where\": \"Watkins 1985 s.v. pent- (AHD_watkins1985.txt line 834)\",\n          \"stance\": \"supports\",\n          \"note\": \"'pent-. To tread, go. 1. Germanic *finthan, to come upon, discover … 2. Suffixed o-grade form *pont-i- in: a. Latin pōns (stem pont-), bridge … b. Russian putʹ, path, way, in sputnik … 3. Zero-grade form *pnt- in Greek patein … 4. Suffixed zero-grade form *pnt-o- in Iranian *path- … [Pok. pent- 808.]'\"\n        },\n        {\n          \"src\": \"IEC\",\n          \"where\": \"Mann s.v. pontos (IEC.txt line 13368)\",\n          \"stance\": \"supports\",\n          \"note\": \"'pontos, is, ā (ponth-) \\\"crossing, passage\\\". WP II, 26. Skt. cf. panthāḥ … Av. pantā̊, pantā … Oss. fándag … Arm. hun … Gk. póntos … Lat. pons, gs pontis … OCS pǫtь … '\"\n        },\n        {\n          \"src\": \"SYN\",\n          \"where\": \"Buck 10.71 ROAD (SYN.txt line 18107)\",\n          \"stance\": \"supports\",\n          \"note\": \"Buck's ROAD table lists 'ChSl. pǫtь', 'SCr. put', 'Russ. putʹ', 'Skt. path-', 'Av. paθ-' as one etymological group.\"\n        }\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan / Old Persian\",\n          \"words\": \"pant, panta, path, pathi, pathâ\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"The forms are right but the gloss over-reaches. Old Iranian inherited the same heteroclitic paradigm as Vedic: Avestan nom. sg. pantā̊ (Nourai's 'panta'), acc. pantąm / pantanəm (his 'pant'), weak-stem paθ- with instr. sg. paθa (his 'pathâ') and the i-stem in the plural, Old Persian acc. sg. paθim — Kent's lexicon, on the page Nourai cites, has 'paθi- sb. \\\"path, way\\\": Av. paθ- patā-, Skt. panthan- path-. paθim asf. DNa 58.' The stem alternation pant- : paθ- is the regular Indo-Iranian one (PIE *pont-h₂-s : zero-grade *pn̥t-h₂-, with *t > θ before a consonant). What is not Old Iranian is the third gloss, 'advice': in Avestan and Old Persian the word means only 'way, path' (Avestan twice also 'room, place'). The 'counsel' sense is a Middle Persian development, and Nourai has read it back into the parent box.\",\n          \"derivation_fa\": \"صورت‌ها درست‌اند ولی معنا فراتر از گواهی رفته است. ایرانی باستان همان صرف ناهمگون ودایی را به ارث برده است: اوستایی نهادی pantā̊ («panta» در نمودار)، رایی pantąm/pantanəm («pant»)، ستاک ضعیف paθ- با بایی paθa («pathâ»)، و صورت i-ستاکی در جمع؛ فارسی باستان رایی paθim. کنت در همان صفحهٔ ۱۹۵ که نورایی ارجاع داده می‌نویسد: «paθi- اسم \\\"راه، گذر\\\": اوستایی paθ-، سنسکریت panthan- path-؛ paθim در کتیبهٔ نقش رستم». جابه‌جایی ستاک pant- : paθ- قاعدهٔ ایرانی‌ـ‌هندی است (*pont-h₂-s در برابر صفرْدرجهٔ *pn̥t-h₂-، با بدل شدن t به θ پیش از همخوان). آنچه ایرانی باستان نیست، معنای سوم یعنی «پند» است: در اوستایی و فارسی باستان این واژه تنها «راه» معنی می‌دهد (و دو بار در اوستا «جا، مکان»). معنای «اندرز» تحولی در فارسی میانه است که نورایی آن را به جعبهٔ مادر بازتابانده است. پس ادعای نورایی با احتیاط پذیرفتنی است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/pent-\",\n            \"https://en.wiktionary.org/wiki/%D9%BE%D9%86%D8%AF\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"POK:808\",\n              \"status\": \"supports\",\n              \"note\": \"IEW 808: 'Old Indie panthāḥ (= Avestan pantā̊), Akk. Sg. panthām (= pantąm) and panthānam (= pantanəm), Instr. Sg. pathā (= paθa); i-stem in Instr. Pl. pathibhiḥ (Avestan paδəbīš), Old pers. Akk. Sg. paθim; Avestan pantā also \\\"room, place\\\"' — all five of Nourai's forms, and no 'advice'.\"\n            },\n            {\n              \"ref\": \"KNT:195\",\n              \"status\": \"supports\",\n              \"note\": \"KNT.txt, the block headed 'LEXICON 195': 'paθi- sb. \\\"path, way\\\" (§76.I, §152.I, §179.III): Av. paθ- patā-, Skt. panthan- path-. paθim asf. DNa 58.' Kent's page 195 is exactly right; Kent likewise gives only 'path, way'.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"BRT\",\n              \"where\": \"Altiranisches Wörterbuch s.v. paṇtan- / paθ- (cols. 847-848)\",\n              \"stance\": \"supports\",\n              \"note\": \"Bartholomae's paṇtā- 'Weg' is the authority both Horn ('Vergl. Bartholomae, ZDMG. 44, 553') and Mo'in's Borhan footnote («ایران باستان *panθā (راه) «بارتولمه»») cite for this word; the local BRT OCR renders the headword too poorly to quote verbatim (searches for 'pantan-', 'paṇtā' return only citation lines).\"\n            },\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein 1966 s.v. find (KLN_1966.txt line 14754)\",\n              \"stance\": \"supports\",\n              \"note\": \"'… fr. I.-E. base *pent-, \\\"to go, pass; path, bridge\\\", whence also OHG. fendeo, \\\"pedestrian\\\", OI. panthāḥ, \\\"path, way\\\", Avestic pantā, \\\"way\\\", Arm. hun, gen. hni (for *ponti), \\\"way, ford\\\" …'\"\n            },\n            {\n              \"src\": \"LAT\",\n              \"where\": \"Ernout-Meillet s.v. pons (LAT.txt line 48795 ff.)\",\n              \"stance\": \"supports\",\n              \"note\": \"'Les langues indo-européennes orientales ont pour \\\"chemin\\\" un mot dont le védique montre bien la flexion singulière: nom. sing. panthāḥ = av. pantā̊, acc. sg. panthām = av. pantąm; gen. sing. pathaḥ = av. paθō, instr. pl. pathibhiḥ …; le v. perse a paθim.'\"\n            }\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"pand «پند»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Persian پند pand 'advice, counsel' continues Middle Persian pand, written pnd in Book Pahlavi and identical in Manichaean Middle Persian; MacKenzie glosses it in one line that contains the whole history: 'pand [pnd | = M, N ~] path; counsel, advice', and his English-Pahlavi index has 'path — pand, widarag'. The word goes back to Old Iranian *pantā- 'way' (the node above), the sense 'road' shifting metaphorically to 'the way to go' > 'guidance, counsel' — the shift is explicit in Mo'in's own footnote in Borhan-e Qate': «اصلاً پند بمعنی راه است و مجازاً پنددادن بمعنی نشان دادن راه و روش»; the same development is visible in Ossetic fænd 'wish; plan, counsel' and Balochi pant-deag 'to instruct'. Wiktionary, following Edelʹman's Etymological Dictionary of the Iranian Languages (2020), derives پند from MP pand < Proto-Iranian *pántaHs 'path, road'. The Khāqānī couplet the book quotes («دندانهٔ هر قصری پندی دهدت نو نو …») is a genuine 12th-c. attestation of the word.\",\n          \"derivation_fa\": \"«پند» فارسی دنبالهٔ pand فارسی میانه است که در پهلوی کتابی pnd نوشته می‌شود و در فارسی میانهٔ مانوی نیز همان است؛ مکنزی در یک سطر تمام تاریخ واژه را می‌آورد: «pand [pnd | = M, N ~] راه؛ اندرز، پند»، و در نمایهٔ انگلیسی‌ـ‌پهلوی خود می‌نویسد «path — pand, widarag». واژه به *pantā- ایرانی باستان «راه» بازمی‌گردد و تحول معنایی آن از «راه» به «راه نمودن» و سپس «اندرز» است؛ همین نکته را معین در حاشیهٔ برهان قاطع به صراحت گفته است: «اصلاً پند بمعنی راه است و مجازاً پنددادن بمعنی نشان دادن راه و روش». همین تحول در «fænd» اُسی «آرزو؛ نقشه، تدبیر» و «pant-deag» بلوچی «آموختن» نیز دیده می‌شود. ویکی‌واژه به پیروی از فرهنگ ریشه‌شناسی زبان‌های ایرانی ادلمان (۲۰۲۰) «پند» را از pand فارسی میانه و آن را از *pántaHs ایرانی آغازین می‌داند. بیت خاقانی که کتاب نقل کرده، گواهی راستین سدهٔ ششم برای این واژه است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D9%BE%D9%86%D8%AF\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"BQT:422\",\n              \"status\": \"supports\",\n              \"note\": \"Borhan-e Qate' vol. 1, the leaf carrying پند / پندار / پنداشتن (BQT_v1_pages.txt form-feed leaf 648, printed p. ≈422-424 by the file's own offset table). The entry reads «پند … بفتح اول و سکون ثانی و دال ابجد، آنست که بعربی نصیحت گویند»، and Mo'in's etymological footnote to it gives: «پهلوی pand، ایران باستان *panθā (راه) «بارتولمه»، پارسی باستان paθi (راه)، سانسکریت pathi، ارمنی hun، اسی fænd … «نیبرگ» … اصلاً پند بمعنی راه است و مجازاً پنددادن بمعنی نشان دادن راه و روش … و در اوستا بمعنی بیراهه است». That is precisely the arrow Nourai draws.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"PHD\",\n              \"where\": \"MacKenzie p. 63 s.v. pand; index 'path'\",\n              \"stance\": \"supports\",\n              \"note\": \"'pand [pnd | = M, N ~] path; counsel, advice'; English-Pahlavi index: 'path — pand, widarag'. MacKenzie's double gloss is the pivot of the semantic shift.\"\n            },\n            {\n              \"src\": \"HRN\",\n              \"where\": \"Horn, Grundriss no. 330 (p. 73)\",\n              \"stance\": \"supports\",\n              \"note\": \"'330. pend \\\"Rat\\\". — ap. paθi- \\\"Weg\\\"; aw. pantan-; ai. páthan-; phlv. pand \\\"Rat\\\"; … oss. d. fænd \\\"Wunsch\\\", t. \\\"Plan, Rat\\\"; bal. pant-deag \\\"belehren, unterrichten\\\". Vergl. Bartholomae, ZDMG. 44, 553.'\"\n            },\n            {\n              \"src\": \"NYB\",\n              \"where\": \"Nyberg, Manual of Pahlavi II (glossary)\",\n              \"stance\": \"silent\",\n              \"note\": \"grep 'pand' in NYB_vol2_glossary.txt returns only amahraspand, göspand, Māraspand etc.; the Bundahišn/Kārnāmag glossary has no independent pand entry. (Mo'in's Borhan footnote cites 'Nyberg 152' — a page of his Hilfsbuch, a different work from the Manual held locally.)\"\n            },\n            {\n              \"src\": \"HUB\",\n              \"where\": \"Hübschmann, Persische Studien\",\n              \"stance\": \"silent\",\n              \"note\": \"grep 'pand' returns only spand/aspand 'rue' and gospand; Hübschmann does not treat پند.\"\n            }\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Scythian\",\n          \"words\": \"\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"An empty pass-through box in the book too: no Scythian form is quoted, and none is attested — Scythian is known almost only from names in Greek sources. The box stands for the hypothesis that the Germanic word for 'path' was borrowed from a North-Iranian (Scythian/Sarmatian) dialect, which is exactly how Watkins words it: 'Suffixed zero-grade form *pnt-o- in Iranian *path-, probably borrowed (? via Scythian) into Germanic as *patha-'. Walde-Pokorny (II 26 f.) attribute the idea to Kluge, who thought specifically of Scythian, and to Much, who preferred Jazygian — i.e. the mediating dialect was already disputed in 1927. The motive for positing a loan at all is phonological: inherited PIE *p- must give Germanic f- by Grimm's law, so a Germanic word beginning p- and meaning 'path' cannot be inherited.\",\n          \"derivation_fa\": \"این جعبه در خودِ کتاب هم تهی است: هیچ صورت سکایی نقل نشده و در واقع هم چیزی گواهی نشده است، زیرا از سکایی جز نام‌هایی در منابع یونانی بر جای نمانده. این جعبه نمایندهٔ فرضیه‌ای است که واژهٔ ژرمنی «راه» را وام‌گرفته از گویشی ایرانی شمالی (سکایی/سرمتی) می‌داند؛ واتکینز دقیقاً چنین می‌نویسد: «صورت پسوندی صفرْدرجهٔ *pnt-o- در ایرانی *path-، که احتمالاً (؟ از راه سکایی) به ژرمنی *patha- وام داده شده». والده‌ـ‌پوکورنی (جلد ۲، ص ۲۶ـ۲۷) این اندیشه را به کلوگه نسبت می‌دهند که گویش میانجی را سکایی می‌دانست، و به موخ که آن را یازیگی می‌دانست — یعنی گویش واسطه از همان ۱۹۲۷ محل اختلاف بوده است. انگیزهٔ اصلِ فرض وام‌گیری آوایی است: *p- هندواروپایی بر پایهٔ قانون گریم باید در ژرمنی f- شود، پس واژه‌ای ژرمنی با p- آغازین نمی‌تواند موروثی باشد.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/path\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"AHD:1533\",\n              \"status\": \"supports\",\n              \"note\": \"Watkins 1985 s.v. pent-, §4: 'Suffixed zero-grade form *pnt-o- in Iranian *path-, probably borrowed (? via Scythian) into Germanic as *patha-, way, path, in: a. Old English peth, path: PATH; b. Middle Dutch pad, way, path: FOOTPAD.' The page number 1533 is consistent with the 1975 AHD appendix (pp. 1505-1550, alphabetical: pent- falls in the p-range).\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"WLD\",\n              \"where\": \"Bd. II 26-27 (WLD_Bd2_pages.txt line 1770 ff.)\",\n              \"stance\": \"supports\",\n              \"note\": \"'Umstritten ist die Herkunft von ags. pæd \\\"Pfad, Weg\\\" (engl. path), ahd. pfad … kaum nach Loewe IF. 10, 81 eine frühe mittelbare Entlehnung aus gr. πάτος, sondern aus einer iran. Mundart, vgl. av. paθ-; u. zw. denkt Kluge Wb. an speziell skythischen, Much AfdA. 27, 124 an jazygischen Ursprung.' — the Scythian mediation named, but the whole question flagged 'umstritten'.\"\n            },\n            {\n              \"src\": \"SYN\",\n              \"where\": \"Buck 10.72 PATH (SYN.txt line 18180)\",\n              \"stance\": \"partial\",\n              \"note\": \"'WGmc. loanword of either Grk. (πάτος) or Iran. (cf. Av. paθ-, 10.71) origin. Other etymologies unconvincing. Walde-P. 2.26 f., Weigand-H. 2.401, Kluge-G. 488, Franck-v.W. 485.' Buck accepts a loan but leaves the donor open between Greek and Iranian.\"\n            },\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein 1966 s.v. path\",\n              \"stance\": \"partial\",\n              \"note\": \"'These Teut. words are prob. of Iranian origin; cp. Avestic paθa, \\\"way\\\"' — Iranian, but Klein names no Scythian intermediary.\"\n            }\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Germanic\",\n          \"words\": \"patha\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"West Germanic *paþa- 'path' (OE pæþ/paþ, OFris. path, MDu. pat, Du. pad, OHG pfad, G. Pfad) is real, but note that it is West Germanic only: there is no Gothic or Old Norse cognate, which is itself an argument for a late areal borrowing rather than inheritance. Its p- cannot come from PIE *p- (Grimm's law would give f-, as it does in *finþaną, node #6 of this same chart), so it must be a loan; the Iranian *paθ- source, mediated by Scythian, is the standard proposal (Kluge, Watkins, Ringe, who calls it 'an obvious loan from Iranian' postdating Grimm's law). The OED and others regard the Iranian route as too much of a stretch and leave the word's origin open, so the arrow is a well-supported hypothesis rather than an established fact. Nourai's spelling 'patha' is the AHD/Klein transliteration of *paþa-.\",\n          \"derivation_fa\": \"صورت ژرمنی غربی *paþa- «راه» (انگلیسی باستان pæþ، فریزی باستان path، هلندی میانه pat، آلمانی باستان pfad) واقعی است، اما باید توجه داشت که تنها ژرمنی غربی است: در گوتی و نورس باستان هم‌ریشه‌ای ندارد و همین خود نشانهٔ وام‌گیری دیرهنگام ناحیه‌ای است نه میراث. پِ آغازین آن نمی‌تواند از *p هندواروپایی آمده باشد، چون قانون گریم آن را به f بدل می‌کرد (چنان‌که در *finþaną در همین نمودار)، پس ناگزیر وام‌واژه است؛ خاستگاه ایرانی *paθ- با میانجی سکایی پیشنهاد استاندارد است (کلوگه، واتکینز، و رینگه که آن را «وام‌واژه‌ای آشکار از ایرانی» پس از قانون گریم می‌داند). در برابر، فرهنگ آکسفورد این مسیر ایرانی را دور از ذهن می‌شمارد و خاستگاه واژه را نامعلوم می‌گذارد. پس این پیکان فرضیه‌ای نیرومند است، نه واقعیتی مسلّم. املای «patha» همان آوانویسی AHD و کلاین از *paþa- است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/path\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"AHD:1533\",\n              \"status\": \"supports\",\n              \"note\": \"Watkins 1985 s.v. pent-: '… borrowed (? via Scythian) into Germanic as *patha-, way, path, in: a. Old English peth, path: PATH.'\"\n            },\n            {\n              \"ref\": \"KLN:1139\",\n              \"status\": \"supports\",\n              \"note\": \"Klein 1966 s.v. path (KLN_1966.txt line 27666): 'path, n. — ME., fr. OE. pæþ, rel. to OFris. path, MDu. pat, Du. pad, OHG. pfad, MHG. pfat, G. Pfad, \\\"path\\\". These Teut. words are prob. of Iranian origin; cp. Avestic paθa, \\\"way\\\", and see find.' The alphabetic position (pa- in a 1776-page work) fits the cited p. 1139.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"WLD\",\n              \"where\": \"Bd. II 26-27\",\n              \"stance\": \"partial\",\n              \"note\": \"'Umstritten ist die Herkunft von ags. pæd \\\"Pfad, Weg\\\" (engl. path), ahd. pfad … sondern aus einer iran. Mundart, vgl. av. paθ-' — supports the Iranian source while calling the question disputed.\"\n            },\n            {\n              \"src\": \"SYN\",\n              \"where\": \"Buck 10.72 PATH\",\n              \"stance\": \"partial\",\n              \"note\": \"'WGmc. loanword of either Grk. or Iran. origin. Other etymologies unconvincing.'\"\n            },\n            {\n              \"src\": \"WEB\",\n              \"where\": \"Etymonline s.v. path (n.) [archived]\",\n              \"stance\": \"partial\",\n              \"note\": \"'Watkins suggests the word was \\\"probably borrowed (? via Scythian) from Iranian *path-\\\" … However the OED and others are skeptical, regarding it as too much of a stretch; the word is not attested in Old Norse or Gothic.'\"\n            }\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"English\",\n          \"words\": \"path\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"The last step is beyond doubt: Old English pæþ / paþ 'narrow way, track worn by feet' > Middle English path > modern path, with the regular Old English þ retained as th and the front vowel æ raised to a. The uncertainty on this branch is entirely upstream, in how *paþa- got into Germanic (nodes #3-#4); no one doubts that English path is the direct continuation of the Old English word. Nourai gives no reference for this box, which is reasonable for a chain this well known.\",\n          \"derivation_fa\": \"واپسین گام بی‌هیچ تردیدی است: pæþ/paþ انگلیسی باستان «گذرگاه باریک، رَدِ پا» به path انگلیسی میانه و سپس path امروزی رسیده است، با نگه‌داشتِ منظم þ به‌صورت th و برافراشته‌شدن واکهٔ پیشین æ به a. تردیدِ این شاخه یکسره در بالادست است، یعنی در چگونگی راهیابی *paþa- به ژرمنی (گره‌های ۳ و ۴)؛ هیچ‌کس در اینکه path انگلیسی دنبالهٔ مستقیم واژهٔ انگلیسی باستان است شک ندارد. نورایی برای این جعبه ارجاعی نداده که برای زنجیره‌ای چنین شناخته‌شده پذیرفتنی است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/path\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"None\",\n              \"status\": \"not_checked\",\n              \"note\": \"The box carries no reference in the book; the chain OE pæþ > ME path > NE path is covered by Klein s.v. path and by Etymonline, both consulted below.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein 1966 s.v. path\",\n              \"stance\": \"supports\",\n              \"note\": \"'path, n. — ME., fr. OE. pæþ …'\"\n            },\n            {\n              \"src\": \"WEB\",\n              \"where\": \"Etymonline s.v. path (n.) [archived]\",\n              \"stance\": \"supports\",\n              \"note\": \"'Old English paþ, pæþ \\\"a narrow passageway or route across land, a track worn by the feet of people or animals treading it\\\", from West Germanic *patha-.'\"\n            }\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"Germanic\",\n          \"words\": \"finthan\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Proto-Germanic *finþaną 'to come upon, discover' is the inherited verbal reflex of *pent-: PIE *p- > Gmc. f- and *-t- > *-þ- by Grimm's law, with the nasal infix/present stem giving *finþ-. It is attested as Gothic finþan 'to find out, learn', Old Saxon fīthan/findan, Old High German findan/fintan, Old English findan (the -nd- forms show the common Germanic *-nþ- > *-nd- shift). The semantic step 'go, tread' > 'come upon' > 'find' is the same one Latin makes in in-venīre and Old Church Slavonic in na-iti (from iti 'to go'); Klein makes exactly this point. Nourai's 'finthan' is the AHD spelling of *finþaną.\",\n          \"derivation_fa\": \"فعل ژرمنی آغازین *finþaną «برخوردن، یافتن» بازتاب موروثی *pent- است: *p هندواروپایی بر پایهٔ قانون گریم به f و *t به þ بدل شده و ستاک حالِ غنّه‌دار *finþ- به دست آمده است. گواهی‌ها: گوتی finþan «دریافتن، آموختن»، ساکسونی باستان fīthan/findan، آلمانی باستان findan/fintan، انگلیسی باستان findan (صورت‌های -nd- نشانهٔ تحول همگانی ژرمنی *-nþ- > *-nd- است). گام معنایی «رفتن، گام نهادن» ← «برخوردن» ← «یافتن» همان است که لاتین در in-venīre و اسلاوی کهن در na-iti (از iti «رفتن») برداشته‌اند؛ کلاین هم دقیقاً به همین نکته اشاره می‌کند. املای «finthan» صورت AHD از *finþaną است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/pent-\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"AHD\",\n              \"status\": \"supports\",\n              \"note\": \"Watkins 1985 s.v. pent-, §1: 'Germanic *finthan, to come upon, discover, in Old English findan, to find: FIND.' Word for word what the box says.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"POK\",\n              \"where\": \"IEW 808-809\",\n              \"stance\": \"supports\",\n              \"note\": \"'Gothic finþan \\\"find, learn\\\", Old Icelandic finna ds. (under the influence of common Celtic -ns-, -nt- > -nn-), Old English findan, Old Saxon fīthan and findan, Old High German findan, fintan …'\"\n            },\n            {\n              \"src\": \"WLD\",\n              \"where\": \"Bd. II 26\",\n              \"stance\": \"supports\",\n              \"note\": \"The head-gloss itself contains the semantic argument: 'dazugelangen = antreffen, finden (vgl. venire : invenire)'.\"\n            },\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein 1966 s.v. find (KLN_1966.txt line 14754)\",\n              \"stance\": \"supports\",\n              \"note\": \"'… rel. to OS. findan, fithan, ON., Swed. finna, Dan. finde, MDu., Du. vinden, OHG. findan, fintan … Goth. finþan. The orig. meaning of these words was \\\"to come upon\\\", fr. I.-E. base *pent- … For sense development cp. Hitt. wemiya, \\\"to find\\\", lit. \\\"to come upon\\\", OSlav. na-iti, \\\"to find\\\", fr. iti, \\\"to go\\\", and L. invenire.'\"\n            }\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"English\",\n          \"words\": \"find\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Old English findan (class III strong verb, past fand, pp. funden) > Middle English finden > modern find; the modern past found continues the OE plural preterite fundon with the rounding of u before the nasal. No reference is given in the book, and none is needed: the step is the plain continuation of node #6.\",\n          \"derivation_fa\": \"findan انگلیسی باستان (فعل قوی ردهٔ سوم، گذشته fand، اسم مفعول funden) به finden انگلیسی میانه و سپس find امروزی رسیده است؛ گذشتهٔ امروزی found دنبالهٔ صورت جمع گذشتهٔ انگلیسی باستان fundon است با گردشدن u پیش از غنّه. کتاب برای این جعبه ارجاعی نداده و نیازی هم نیست: این گام ادامهٔ ساده و بی‌ابهام گرهٔ پیشین است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/pent-\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"None\",\n              \"status\": \"not_checked\",\n              \"note\": \"No reference printed in the book for this box; covered by Klein s.v. find and by Watkins s.v. pent- (both cited on node #6).\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein 1966 s.v. find\",\n              \"stance\": \"supports\",\n              \"note\": \"Klein's find entry (quoted at node #6) heads exactly this chain, OE findan > E find.\"\n            },\n            {\n              \"src\": \"AHD\",\n              \"where\": \"Watkins 1985 s.v. pent- and index 'FIND pent-'\",\n              \"stance\": \"supports\",\n              \"note\": \"The AHD index line reads 'FIND pent-'.\"\n            }\n          ]\n        },\n        {\n          \"id\": 8,\n          \"lang\": \"Latin\",\n          \"words\": \"pont\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Latin pōns, gen. pontis 'bridge' — Nourai's headword 'pont' is the oblique stem — is the o-grade *pont-i- of this root, formally the same formation as Old Church Slavonic pǫtь 'way'. Nourai's gloss 'bridge, path over water' captures precisely the point the comparatists make: the Latin sense 'bridge' is a narrowing of an older 'way, passage', which survives in the priestly title pontifex, literally 'way-maker' (Varro, LL 5.83, already derives it a ponte). Ernout-Meillet note that Latin pons and OCS pǫtь match formally but 'le sens fait difficulté', i.e. the sense-shift 'way' > 'bridge' is the Latin innovation. Walde-Pokorny gloss the Latin word itself as 'Prügelweg durch Sümpfe, Brücke' — a causeway over marsh before it is a bridge.\",\n          \"derivation_fa\": \"لاتین pōns با ستاک غیرمستقیم pont- («pont» در نمودار) «پل» صورت o-درجهٔ *pont-i- همین ریشه است، از نظر ساخت همان چیزی که در pǫtь اسلاوی کهن «راه» دیده می‌شود. معنایی که نورایی داده — «پل، راهِ روی آب» — دقیقاً همان نکته‌ای است که تطبیق‌گران بر آن انگشت می‌نهند: معنای «پل» در لاتین تنگ‌شدهٔ معنای کهن‌تر «راه، گذرگاه» است که در عنوان pontifex «راه‌ساز» بر جای مانده (وارو در ۵.۸۳ آن را از pons می‌داند). ارنو و مه‌یه یادآور می‌شوند که pons لاتین و pǫtь اسلاوی از نظر صورت بر هم منطبق‌اند ولی «معنا مشکل‌ساز است»، یعنی تحول «راه» به «پل» نوآوری لاتین است. والده‌ـ‌پوکورنی خود واژهٔ لاتین را «گذرگاه چوبی در باتلاق، پل» معنی می‌کنند. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/pent-\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"AHD\",\n              \"status\": \"supports\",\n              \"note\": \"Watkins 1985 s.v. pent-, §2a: 'Latin pōns (stem pont-), bridge (earliest meaning, \\\"way, passage\\\", preserved in the priestly title pontifex, \\\"he who prepares the way\\\"): PONS, PONTIFEX, PONTIFF, PONTINE, PONTOON, PUNT.' Nourai's gloss is a paraphrase of Watkins's parenthesis.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"POK\",\n              \"where\": \"IEW 808-809\",\n              \"stance\": \"supports\",\n              \"note\": \"'Lithuanian [recte Latin] pons, -tis \\\"Prügelweg durch Sümpfe, bridge\\\"; pontifex \\\"Oberpriester\\\", originally \\\"Brückenmacher\\\".'\"\n            },\n            {\n              \"src\": \"LAT\",\n              \"where\": \"Ernout-Meillet s.v. pons (LAT.txt line 48785 ff.)\",\n              \"stance\": \"supports\",\n              \"note\": \"'pons, pontis m.: pont; passerelle. Attesté de tout temps … Pour la forme, lat. pons serait superposable à v.sl. pǫtь (masc.); mais le sens fait difficulté.'\"\n            },\n            {\n              \"src\": \"IEC\",\n              \"where\": \"Mann s.v. pontos (IEC.txt line 13368)\",\n              \"stance\": \"supports\",\n              \"note\": \"'Lat. pons, gs pontis, gp pontium, m. \\\"bridge\\\"' listed with Skt. panthāḥ, Av. pantā̊, Gk. póntos and OCS pǫtь under 'pontos … \\\"crossing, passage\\\"'.\"\n            }\n          ]\n        },\n        {\n          \"id\": 9,\n          \"lang\": \"English\",\n          \"words\": \"pontoon\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English pontoon is French ponton, from Latin pontōnem, accusative of pontō 'punt, flat-bottomed boat; floating bridge', a derivative of pōns with the -ō/-ōn- suffix; the word entered English in the 17th century in the military sense 'boat supporting a temporary bridge'. Ernout-Meillet list the derivative explicitly under pons: 'ponto, -onis m.: bac, pont de bateau, ponton'. The doublet punt comes from the same Latin word by a different route.\",\n          \"derivation_fa\": \"pontoon انگلیسی از ponton فرانسه است و آن از pontōnem لاتین، رایی pontō «قایق ته‌صاف؛ پل شناور»، که با پسوند -ō/-ōn- از pōns ساخته شده؛ واژه در سدهٔ هفدهم با معنای نظامی «قایقی که پل موقت را نگه می‌دارد» وارد انگلیسی شد. ارنو و مه‌یه این مشتق را صریحاً ذیل pons آورده‌اند: «ponto, -onis: کرجی، پلِ قایقی، پونتون». واژهٔ punt نیز دوگانهٔ همین واژهٔ لاتین است که از راهی دیگر به انگلیسی رسیده است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/pent-\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"None\",\n              \"status\": \"not_checked\",\n              \"note\": \"No reference printed in the book for this box; covered by Klein s.v. pontoon and Ernout-Meillet s.v. pons, both consulted below.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein 1966 s.v. pontoon (KLN_1966.txt line 29606)\",\n              \"stance\": \"supports\",\n              \"note\": \"'pontoon, n., a boat used to support a temporary bridge. — F. ponton, fr. L. pontonem, acc. of ponto, \\\"punt; floating bridge\\\", a derivative of pons, gen. pontis, \\\"bridge\\\".'\"\n            },\n            {\n              \"src\": \"LAT\",\n              \"where\": \"Ernout-Meillet s.v. pons, 'Dérivés et composés'\",\n              \"stance\": \"supports\",\n              \"note\": \"'ponto, -onis m.: bac, pont de bateau, ponton, M.L. 6651.'\"\n            },\n            {\n              \"src\": \"AHD\",\n              \"where\": \"Watkins 1985 s.v. pent-\",\n              \"stance\": \"supports\",\n              \"note\": \"PONTOON is listed among the Latin pōns derivatives of this root.\"\n            }\n          ]\n        },\n        {\n          \"id\": 10,\n          \"lang\": \"Russian\",\n          \"words\": \"put\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Russian путь putʹ 'way, path, journey' continues Old Church Slavonic pǫtь, from Proto-Slavic *pǫtь < *pontis, the same i-stem *pont-i- as Latin pons; the Slavic nasal vowel ǫ is the regular outcome of *-on- before a consonant, and it denasalised to u in East Slavic. Old Prussian pintis 'way' shows the zero-grade beside it.\",\n          \"derivation_fa\": \"путь روسی «راه، سفر» دنبالهٔ pǫtь اسلاوی کهن است، از اسلاوی آغازین *pǫtь و آن از *pontis، یعنی همان i-ستاکِ *pont-i- که در pons لاتین دیده می‌شود؛ واکهٔ خیشومی ǫ در اسلاوی برایند قاعده‌مند *-on- پیش از همخوان است که در اسلاوی شرقی خیشومی‌زدایی شده و به u بدل گشته است. صورت pintis پروسی باستان «راه» نیز صفرْدرجهٔ همین ریشه است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/sputnik\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"AHD\",\n              \"status\": \"supports\",\n              \"note\": \"Watkins 1985 s.v. pent-, §2b: 'Russian putʹ, path, way, in sputnik, fellow traveler: SPUTNIK.'\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"POK\",\n              \"where\": \"IEW 808-809\",\n              \"stance\": \"supports\",\n              \"note\": \"'Old Church Slavic pǫtь etc. m. \\\"way\\\" (*pontis), zero grade Old Prussian pintis ds.'\"\n            },\n            {\n              \"src\": \"SYN\",\n              \"where\": \"Buck 10.71 ROAD\",\n              \"stance\": \"supports\",\n              \"note\": \"Buck's ROAD table gives 'ChSl. pǫtь … Russ. doroga, putʹ' in the same etymological set as Skt. path-, Av. paθ-.\"\n            },\n            {\n              \"src\": \"IEC\",\n              \"where\": \"Mann s.v. pontos\",\n              \"stance\": \"supports\",\n              \"note\": \"'OCS (and com. Sl.) pǫtь, gs pǫti, m. \\\"road, highway\\\"'.\"\n            }\n          ]\n        },\n        {\n          \"id\": 11,\n          \"lang\": \"English\",\n          \"words\": \"Sputnik\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Sputnik entered English in October 1957 as the name of the first artificial satellite. Russian спутник sputnik literally means 'travelling companion, fellow traveller' — s- (< sŭ- 'with, together') + putʹ 'way' + the agent suffix -nik — and had already been used in Russian astronomy for a 'satellite' of a planet, i.e. a body that travels along with another. English borrowed the word unchanged.\",\n          \"derivation_fa\": \"«Sputnik» در مهر ۱۹۵۷ به‌عنوان نام نخستین ماهوارهٔ مصنوعی وارد انگلیسی شد. спутник روسی تحت‌اللفظ «همسفر، همراه» است: پیشوند s- (از sŭ- «با، هم») + putʹ «راه» + پسوند فاعلی -nik؛ این واژه پیش‌تر در اخترشناسی روسی به معنای «قمرِ» یک سیاره به کار می‌رفت، یعنی جرمی که همراه جرم دیگر می‌رود. انگلیسی آن را بی‌هیچ دگرگونی وام گرفت. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/sputnik\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"None\",\n              \"status\": \"not_checked\",\n              \"note\": \"No reference printed in the book for this box; the AHD entry cited on node #10 ('Russian putʹ, path, way, in sputnik, fellow traveler: SPUTNIK') and Etymonline cover it.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"WEB\",\n              \"where\": \"Etymonline s.v. sputnik [archived]\",\n              \"stance\": \"supports\",\n              \"note\": \"'from Old Church Slavonic pǫtь, from PIE *pent- \\\"to tread, go\\\" (source also of Old High German fendeo \\\"pedestrian\\\", Sanskrit panthāḥ \\\"path, way\\\", Greek pontos \\\"open sea\\\", Latin pons \\\"bridge\\\")'.\"\n            },\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein 1966 s.v. find (cross-references)\",\n              \"stance\": \"supports\",\n              \"note\": \"Klein's *pent- cross-reference list ends 'Cp. also sputnik.'\"\n            }\n          ]\n        }\n      ]\n    }\n  ]\n}\n"
}
```


### [2026-09-14T01:07:48.034Z] TOOL RESULT

```
File created successfully at: /home/sfmqrb/git/rishe/data/verification/page-392.json (file state is current in your context — no need to Read it back)
```


## [2026-09-14T01:07:51.707Z] TOOL CALL #74: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-392.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 392"
}
```


### [2026-09-14T01:07:53.097Z] TOOL RESULT

```
JSON OK
nodes verified: 21/21
node verdicts: {'confirmed': 13, 'plausible': 7, 'disputed': 1}
root verdicts: {'confirmed': 2}
ref checks: {'supports': 17, 'not_checked': 5, 'partial': 2}
books consulted: {'supports': 42, 'partial': 12, 'silent': 4, 'contradicts': 3} | by book: {'KLN': 11, 'WLD': 8, 'IEC': 8, 'POK': 6, 'WEB': 5, 'AHD': 3, 'PHD': 3, 'LAT': 3, 'SYN': 3, 'BRT': 2, 'HRN': 2, 'HUB': 2, 'ARY': 2, 'SOD': 1, 'MON': 1, 'NYB': 1}
```


## [2026-09-14T01:08:11.281Z] AGENT

Done — `data/verification/page-392.json` written, valid JSON, `verify_check.py 392` reports 21/21 nodes and **0 PROBLEM lines**.

**Page 392 (book p. 362), 2 charts (`Pend → Spen` is a redirect, skipped):**
- Roots: 2 `confirmed` (PIE *pénkʷe "five" = Pokorny 808; PIE *pent- "to go, pass" = Pokorny 808-809 — both page citations exact)
- Nodes: 13 `confirmed`, 7 `plausible`, 1 `disputed`
- Ref checks: 17 supports, 2 partial, 5 not_checked (boxes the book prints with no reference)

**Disputed**
- *Penkwe* #5 [English] **punch; Punjab** — the "five ingredients" etymology of the drink is rejected by OED/Etymonline (no *panch* attested in India before the English word; English word predates regular India trade; likely a sailors' shortening of *puncheon*, the cask). Separately, **Punjab** is Persian *panj-āb* "five waters" via Hindi, i.e. it belongs under the Persian box #3, not the Sanskrit one.

**Notable `plausible` calls**
- #2 Sogdian: forms exact (Gharib p. 276 = entries 6878/6880, verbatim), but Sogdian is Avestan's sister, not its daughter.
- #7/#8 Germanic/English *funh-stiz* > **fist**: Walde-Pokorny II 84 calls the link to "five" *ganz fraglich*; Klein's *fist* entry never mentions five.
- Pent #1: forms right (Kent p. 195 quoted verbatim), but "advice" is a Middle Persian sense read back into Avestan/Old Persian.
- Pent #3/#4 Scythian → Gmc *paþa-: Watkins's own "(? via Scythian)"; WLD flags it *umstritten*, OED skeptical.

**No transcription_suspect nodes and no extraction errors** — I rendered pdf page 392 (copy saved at `data/verification/sources/refs/ocr/BOOK/392.png`) and the JSON matches the printed chart, including `finfi`, `pancâsas`, `pnc\`s` and the Khāqānī couplet.

**Page-number notes for the owner:** BQT:419 (پنج) is independently corroborated — Aryanpur's پنج entry cites «برهان قاطع: ۴۱۹». BQT:422 (پند) lands on BQT_v1_pages.txt leaf 648, which the offset table puts at printed ≈422-424; the entry and Mo'in's footnote («اصلاً پند بمعنی راه است…») are there. MON:822 could only be partly checked: Mo'in's پانچ is real and marked [انگ.], but the text online gives the "hole-punch" sense, not Nourai's "drink of five fruits" (that gloss is Dehkhoda's).
