# Verification process log — verify-page-509


## [2026-10-15T02:44:16.388Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 509 only. Chart text: /home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-509.txt; source JSON: /home/sfmqrb/git/rishe-private/data/extracted/batch/page-509.json. Write /home/sfmqrb/git/rishe-private/data/verification/page-509.json, run `python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py 509` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-10-15T02:44:16.461Z] INPUT

<system-reminder>
Your final report is delivered through SubagentHandback: when your work is complete, call SubagentHandback({message: <your full report>}). The call ends your run, so make it your last step. Only a SubagentHandback call reaches your caller as your result; plain text you write at the end is not delivered.
</system-reminder>


## [2026-10-15T02:44:19.066Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-10-15T02:44:19.118Z] TOOL RESULT

```
1	# Etymology verification task — instructions
2	
3	You are verifying the etymological derivations from Ali Nourai's *An Etymological
4	Dictionary of Persian, English and other Indo-European Languages* (1999), which this
5	repository (`/home/sfmqrb/git/rishe-private`) turned into JSON (`data/extracted/batch/page-<pdf>.json`).
6	Compact text renderings of the charts are in
7	`/home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-<pdf>.txt`.
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
52	  offsets and lookup hints: `/home/sfmqrb/git/rishe-private/data/verification/sources/refs_online.json`
53	  (keys = abbreviations; `kind`, `url`, `lookup_hint`, `local_file`, `page_offset`, `scans`, `cites`).
54	- If `local_file` is set, the OCR text of that book is on disk under
55	  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/`: grep it for the headword (try
56	  several spellings — OCR of diacritics is noisy; e.g. `grep -n -i 'barak' …`) and, if a page
57	  offset is given, locate the cited page (pages are separated by form-feeds; `_pages.txt`
58	  files also carry `[pdf page N]` tags; use `awk 'BEGIN{RS="\f"} NR==<n>' file` to print one
59	  page). Read the entry and judge whether it actually says what Nourai's arrow says.
60	- **Scanned references without full OCR text** (Borhan-e Qate' vols 3–5 = BQT pages
61	  ~1208–2475, Farahvashi's Iranvij = IRN, Aryanpur = ARY, any entry with a `scans` list): do
62	  NOT OCR whole books. Fetch only the cited page:
63	  `python3 /home/sfmqrb/git/rishe-private/tools/ref_page.py BQT:918 --image`
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
103	`/home/sfmqrb/git/rishe-private/data/verification/sources/SOURCE_MATRIX.md`. Minimum per node:
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
140	with `pdftoppm -f <pdf page> -l <pdf page> -r 300 -png -singlefile /home/sfmqrb/git/rishe-private/EtymologicalDictionary-persian-english.pdf /tmp/pg<pdf page>`
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
187	  `python3 /home/sfmqrb/git/rishe-private/tools/fetch_source.py '<URL>' --note '<page N, root X, what you used it for>'`
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
224	Write `/home/sfmqrb/git/rishe-private/data/verification/page-<pdf>.json` (UTF-8, no BOM):
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
279	  `python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py <pdf page>` — it must show 0 PROBLEM lines.
280	- When done, reply with a SHORT summary (≤ 15 lines): counts of verdicts per page, and a
281	  bullet per `disputed` / `transcription_suspect` item (root, word, one-line reason), plus
282	  any extraction errors (JSON differs from the printed page) the owner must fix.
283	  Do not paste the JSON back into your reply.
284	
```


## [2026-10-15T02:44:19.574Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-509.txt"
}
```


### [2026-10-15T02:44:19.639Z] TOOL RESULT

```
1	=== PDF page 509 (book page 479) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Tex, Text, Teks, Teku 2 : to build from wood, to build  (refs POK:1058)
4	#1 (parent #0) [Avestan] refs=KLN; HRN; POK:1058 | taš : to cut, carve ; taša : ax ; tašta : cup
5	  #2 (parent #1) [Persian] refs=IEC:1374,1409; MON | tîšeh «تیشه» : hatchet ; taxteh «تخته» : board, plank, lumber ; tašt «تشت» : a flat wash tub ; tâs «طاس» : cup | extra: تاس
6	    #3 (parent #2) [Arabic] refs=None | 
7	      #4 (parent #3) [French] refs=None | 
8	        #5 (parent #4) [English] refs=KLN:1575 | tass : cup
9	#6 (parent #0) [Avestan] refs=FFD:46; MON:1060 | traš 2, trâš 2 : to cut
10	  #7 (parent #6) [Persian] refs=FFD:46 | tarâšîdan «تراشیدن» : to cut, shave, scrape | extra: تراش
11	#8 (parent #0) [Sogdian] refs=SOD:384 | t`š : to cut, tablet
12	#9 (parent #0) [Greek] refs=AHD | texně : art ; tektôn : carpenter ; arxi-tektôn : master builder ☞Arxein
13	  #10 (parent #9) [French] refs=AHD | 
14	    #11 (parent #10) [Persian] refs=AMD:25; MON:1128 | âršîtekt «آرشیتکت» : "master builder" ; teknîk «تکنیک» : technique
15	    #12 (parent #10) [English] refs=AHD:68,1321 | architect, technique
16	#13 (parent #0) [Latin] refs=AHD | texere : to weave ; testum : pot
17	  #14 (parent #13) [English] refs=None | context, test, text, textile, tissue
18	--- entry 1 ---
19	ROOT Text -> redirect to Tex
20	--- entry 2 ---
21	ROOT [Indo-European] Tiegu : to approach shyly  (refs POK:1086)
22	#1 (parent #0) [Avestan] refs=POK:1086 | ithyajah, ithyejah : abandonment
23	  #2 (parent #1) [Pahlavi] refs=SNS:314 | sěj : trouble, pain
24	    #3 (parent #2) [Persian] refs=SNS:314; BQT:1202 | sîj «سیج» : suffering, pain | extra: سیجمند
25	
```


## [2026-10-15T02:44:20.356Z] TOOL CALL #3: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/extracted/batch/page-509.json"
}
```


### [2026-10-15T02:44:20.391Z] TOOL RESULT

```
1	{
2	  "pdf_page": 509,
3	  "book_page": 479,
4	  "entries": [
5	    {
6	      "root": {
7	        "name": "Tex, Text, Teks, Teku 2",
8	        "lang": "Indo-European",
9	        "refs": "POK:1058",
10	        "gloss": "to build from wood, to build"
11	      },
12	      "nodes": [
13	        {
14	          "id": 1,
15	          "parent": 0,
16	          "lang": "Avestan",
17	          "refs": "KLN; HRN; POK:1058",
18	          "words": [
19	            {"translit": "taš", "gloss": "to cut, carve", "script": null},
20	            {"translit": "taša", "gloss": "ax", "script": null},
21	            {"translit": "tašta", "gloss": "cup", "script": null}
22	          ],
23	          "note": null,
24	          "quote": null
25	        },
26	        {
27	          "id": 2,
28	          "parent": 1,
29	          "lang": "Persian",
30	          "refs": "IEC:1374,1409; MON",
31	          "words": [
32	            {"translit": "tîšeh", "gloss": "hatchet", "script": "تیشه"},
33	            {"translit": "taxteh", "gloss": "board, plank, lumber", "script": "تخته"},
34	            {"translit": "tašt", "gloss": "a flat wash tub", "script": "تشت"},
35	            {"translit": "tâs", "gloss": "cup", "script": "طاس"}
36	          ],
37	          "script_extra": "تاس",
38	          "note": null,
39	          "quote": {"text": "همچو فرهاد بود کوه کنی پیشهٔ ما - سنگ ما سینهٔ ما ، ناخن ما تیشهٔ ما", "poet": "Zahîroddoleh"}
40	        },
41	        {
42	          "id": 3,
43	          "parent": 2,
44	          "lang": "Arabic",
45	          "refs": null,
46	          "words": [],
47	          "note": null,
48	          "quote": null
49	        },
50	        {
51	          "id": 4,
52	          "parent": 3,
53	          "lang": "French",
54	          "refs": null,
55	          "words": [],
56	          "note": null,
57	          "quote": null
58	        },
59	        {
60	          "id": 5,
61	          "parent": 4,
62	          "lang": "English",
63	          "refs": "KLN:1575",
64	          "words": [
65	            {"translit": "tass", "gloss": "cup", "script": null}
66	          ],
67	          "note": null,
68	          "quote": null
69	        },
70	        {
71	          "id": 6,
72	          "parent": 0,
73	          "lang": "Avestan",
74	          "refs": "FFD:46; MON:1060",
75	          "words": [
76	            {"translit": "traš 2, trâš 2", "gloss": "to cut", "script": null}
77	          ],
78	          "note": null,
79	          "quote": null
80	        },
81	        {
82	          "id": 7,
83	          "parent": 6,
84	          "lang": "Persian",
85	          "refs": "FFD:46",
86	          "words": [
87	            {"translit": "tarâšîdan", "gloss": "to cut, shave, scrape", "script": "تراشیدن"}
88	          ],
89	          "script_extra": "تراش",
90	          "note": null,
91	          "quote": null
92	        },
93	        {
94	          "id": 8,
95	          "parent": 0,
96	          "lang": "Sogdian",
97	          "refs": "SOD:384",
98	          "words": [
99	            {"translit": "t`š", "gloss": "to cut, tablet", "script": null}
100	          ],
101	          "note": null,
102	          "quote": null
103	        },
104	        {
105	          "id": 9,
106	          "parent": 0,
107	          "lang": "Greek",
108	          "refs": "AHD",
109	          "words": [
110	            {"translit": "texně", "gloss": "art", "script": null},
111	            {"translit": "tektôn", "gloss": "carpenter", "script": null},
112	            {"translit": "arxi-tektôn", "gloss": "master builder", "script": null, "see": ["Arxein"]}
113	          ],
114	          "note": null,
115	          "quote": null
116	        },
117	        {
118	          "id": 10,
119	          "parent": 9,
120	          "lang": "French",
121	          "refs": "AHD",
122	          "words": [],
123	          "note": null,
124	          "quote": null
125	        },
126	        {
127	          "id": 11,
128	          "parent": 10,
129	          "lang": "Persian",
130	          "refs": "AMD:25; MON:1128",
131	          "words": [
132	            {"translit": "âršîtekt", "gloss": "\"master builder\"", "script": "آرشیتکت"},
133	            {"translit": "teknîk", "gloss": "technique", "script": "تکنیک"}
134	          ],
135	          "note": null,
136	          "quote": null
137	        },
138	        {
139	          "id": 12,
140	          "parent": 10,
141	          "lang": "English",
142	          "refs": "AHD:68,1321",
143	          "words": [
144	            {"translit": "architect, technique", "gloss": null, "script": null}
145	          ],
146	          "note": null,
147	          "quote": null
148	        },
149	        {
150	          "id": 13,
151	          "parent": 0,
152	          "lang": "Latin",
153	          "refs": "AHD",
154	          "words": [
155	            {"translit": "texere", "gloss": "to weave", "script": null},
156	            {"translit": "testum", "gloss": "pot", "script": null}
157	          ],
158	          "note": null,
159	          "quote": null
160	        },
161	        {
162	          "id": 14,
163	          "parent": 13,
164	          "lang": "English",
165	          "refs": null,
166	          "words": [
167	            {"translit": "context, test, text, textile, tissue", "gloss": null, "script": null}
168	          ],
169	          "note": null,
170	          "quote": null
171	        }
172	      ]
173	    },
174	    {
175	      "root": {
176	        "name": "Text",
177	        "redirect": "Tex"
178	      },
179	      "nodes": []
180	    },
181	    {
182	      "root": {
183	        "name": "Tiegu",
184	        "lang": "Indo-European",
185	        "refs": "POK:1086",
186	        "gloss": "to approach shyly"
187	      },
188	      "nodes": [
189	        {
190	          "id": 1,
191	          "parent": 0,
192	          "lang": "Avestan",
193	          "refs": "POK:1086",
194	          "words": [
195	            {"translit": "ithyajah, ithyejah", "gloss": "abandonment", "script": null}
196	          ],
197	          "note": null,
198	          "quote": null
199	        },
200	        {
201	          "id": 2,
202	          "parent": 1,
203	          "lang": "Pahlavi",
204	          "refs": "SNS:314",
205	          "words": [
206	            {"translit": "sěj", "gloss": "trouble, pain", "script": null}
207	          ],
208	          "note": null,
209	          "quote": null
210	        },
211	        {
212	          "id": 3,
213	          "parent": 2,
214	          "lang": "Persian",
215	          "refs": "SNS:314; BQT:1202",
216	          "words": [
217	            {"translit": "sîj", "gloss": "suffering, pain", "script": "سیج"}
218	          ],
219	          "script_extra": "سیجمند",
220	          "note": null,
221	          "quote": {"text": "جهان سیجمند و پر انائی - که او را پیشه باشد بیوفائی", "poet": "Ardâvîrâf-Nâmeh"}
222	        }
223	      ]
224	    }
225	  ]
226	}
227	
```


## [2026-10-15T02:44:23.182Z] TOOL CALL #4: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification; cat sources/SOURCE_MATRIX.md | head -80; ls sources/refs/ | head -100; ls page-5*.json | head"
}
```


### [2026-10-15T02:44:23.618Z] TOOL RESULT

```
# Source matrix — which local books to grep for each kind of node

All files are OCR text; pages are separated by form-feeds (`\f`) and, in the `_pages.txt` files, tagged `[pdf page N]`. Print one page with `awk 'BEGIN{RS="\f"} NR==<n>' file`. Grep several spellings (OCR of diacritics is noisy; Persian OCR is rough — try short substrings). Full titles, page offsets and what a cited number means: data/verification/sources/refs_online.json.

ARY (Aryanpur) is alphabetical by Persian headword; grep the Persian word in ARY_pages.txt or the Latin-caps transliteration in ARY_latin_index_pages.txt, note the [pdf page N] tag, and quote from that page (printed page = pdf page + 1).


## Indo-European roots (any IE node, root boxes)

- **POK** — J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/POK_01.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/POK_02.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/POK_03.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/POK_full.txt`
- **WLD** — A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-3
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/WLD_band3.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_text.pdf`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd1_pages.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_text.pdf`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd2_pages.txt`
- **AHD** — W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appe
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/AHD_watkins1985.txt`
- **IEC** — S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/IEC.txt`
- **SYN** — C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SYN.txt`
- **KLN** — E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KLN_1966.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KLN_1971.txt`
- **SKT** — W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SKT.txt`
- **LEW** — A. Walde (& J. B. Hofmann), Lateinisches etymologisches Wörterbuch, 3rd ed., Heidelberg 1938-56
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/LEW_1910.txt`
- **LAT** — A. Ernout & A. Meillet, Dictionnaire étymologique de la langue latine, 3rd ed., Paris 1951
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/LAT.txt`
- **ARY** — Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپای
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY/ARY_pages.txt`

## Iranian: Avestan / Old Persian / Pahlavi / Sogdian / Khotanese / New Persian

- **BRT** — C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BRT.txt`
- **KNT** — R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KNT.txt` (truncated before the lexicon's h–z section, ~p. 208 on)
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KNT_full.txt` (complete archive.org djvu text — use this for lexicon pages 208–215: haumavarga-, siyamam, etc.)
- **PHD** — D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/PHD.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/PHD_mackenzie.txt`
- **NYB** — H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/NYB_vol1.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/NYB_vol2_glossary.txt`
- **HRN** — P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HRN.txt`
- **HUB** — H. Hübschmann, Persische Studien, Strassburg 1895
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HUB.txt`
- **CHEUNG** — CHEUNG
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/CHEUNG.txt`
- **SOD** — Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SOD.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SOD_pages.txt`
- **SNS** — Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SNS.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SNS_pages.txt`
- **BQT** — Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/19
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_alt_v1.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_dli_part1.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v1.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v1_pages.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v2.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v2_pages.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf`
- **MON** — Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols
Permissions Size User   Date Modified Name
drwxr-xr-x     - sfmqrb 14 Oct 22:19  incoming
drwxr-xr-x     - sfmqrb 14 Oct 22:19  ocr
drwxr-xr-x     - sfmqrb 14 Oct 22:19  pageimg
drwxr-xr-x     - sfmqrb 14 Oct 22:25  tessdata
.rw-r--r--  600k sfmqrb 14 Oct 22:19  AFA.txt
.rw-r--r--   15M sfmqrb 14 Oct 22:19  AFM.pdf
.rw-r--r--  355k sfmqrb 14 Oct 22:19  AFM.txt
.rw-r--r--  384k sfmqrb 14 Oct 22:19  AFM_alt.txt
.rw-r--r--  342k sfmqrb 14 Oct 22:19  AFM_pages.txt
.rw-r--r--  850k sfmqrb 14 Oct 22:19  AHD_watkins1985.txt
.rw-r--r--  825k sfmqrb 14 Oct 22:19  AHM.txt
.rw-r--r--  1.2M sfmqrb 14 Oct 22:19  AID.txt
.rw-r--r--  240k sfmqrb 14 Oct 22:19  AIN.txt
.rw-r--r--  256k sfmqrb 14 Oct 22:19  AKD.txt
.rw-r--r--  285k sfmqrb 14 Oct 22:19  ARB_abdulraheem.txt
.rw-r--r--  1.3M sfmqrb 14 Oct 22:19  ARB_mo3rb.txt
.rw-r--r--  744k sfmqrb 14 Oct 22:19  ARP.txt
.rw-r--r--  633k sfmqrb 14 Oct 22:19  AVG.txt
.rw-r--r--  2.6M sfmqrb 14 Oct 22:19  BQT_alt_v1.txt
.rw-r--r--   139 sfmqrb 14 Oct 22:19  BQT_dli_part1.txt
.rw-r--r--  2.6M sfmqrb 14 Oct 22:19  BQT_v1.txt
.rw-r--r--   26M sfmqrb 14 Oct 22:19  BQT_v1_djvu.xml
.rw-r--r--  2.2M sfmqrb 14 Oct 22:19  BQT_v1_pages.txt
.rw-r--r--  2.4M sfmqrb 14 Oct 22:19  BQT_v2.txt
.rw-r--r--  4.3M sfmqrb 14 Oct 22:19  BQT_v2_pages.txt
.rw-r--r--  4.8M sfmqrb 14 Oct 22:19  BRT.txt
.rw-r--r--  656k sfmqrb 14 Oct 22:19  BST.txt
.rw-r--r--  1.8M sfmqrb 14 Oct 22:19  CHEUNG.txt
.rw-r--r--  593k sfmqrb 14 Oct 22:19  DEV.txt
.rw-r--r--  144k sfmqrb 14 Oct 22:19  DOZ.txt
.rw-r--r--  1.5M sfmqrb 14 Oct 22:19  DRM.txt
.rw-r--r--  560k sfmqrb 14 Oct 22:19  EAV_studies.txt
.rw-r--r--  891k sfmqrb 14 Oct 22:19  FRS.txt
.rw-r--r--  1.6M sfmqrb 14 Oct 22:19  FRS_pages.txt
.rw-r--r--   16M sfmqrb 14 Oct 22:19  FSD_vol1.txt
.rw-r--r--   17M sfmqrb 14 Oct 22:19  FSD_vol2.txt
.rw-r--r--   13M sfmqrb 14 Oct 22:19  FSD_vol3.txt
.rw-r--r--   17M sfmqrb 14 Oct 22:19  FSD_vol4.txt
.rw-r--r--  1.2M sfmqrb 14 Oct 22:19  FSF.txt
.rw-r--r--  2.2M sfmqrb 14 Oct 22:19  FSF_pages.txt
.rw-r--r--  650k sfmqrb 14 Oct 22:19  FVQ.txt
.rw-r--r--  628k sfmqrb 14 Oct 22:19  FVQ_pages.txt
.rw-r--r--  573k sfmqrb 14 Oct 22:19  GPL.txt
.rw-r--r--  1.6M sfmqrb 14 Oct 22:19  HENNING_selected_papers.txt
.rw-r--r--  449k sfmqrb 14 Oct 22:19  HID.txt
.rw-r--r--  5.6M sfmqrb 14 Oct 22:19  HJB.txt
.rw-r--r--  688k sfmqrb 14 Oct 22:19  HRN.txt
.rw-r--r--  527k sfmqrb 14 Oct 22:19  HUB.txt
.rw-r--r--  3.3M sfmqrb 14 Oct 22:19  IEC.txt
.rw-r--r--  3.4M sfmqrb 14 Oct 22:19  ISS_alt_DKS.txt
.rw-r--r--  1.3M sfmqrb 14 Oct 22:19  KFL.txt
.rw-r--r--   11M sfmqrb 14 Oct 22:19  KLN_1966.txt
.rw-r--r--   10M sfmqrb 14 Oct 22:19  KLN_1971.txt
.rw-r--r--  874k sfmqrb 14 Oct 22:19  KNT.txt
.rw-r--r--  944k sfmqrb 14 Oct 22:19  KNT_full.txt
.rw-r--r--  488k sfmqrb 14 Oct 22:19  LAM.txt
.rw-r--r--  4.6M sfmqrb 14 Oct 22:19  LAT.txt
.rw-r--r--  627k sfmqrb 14 Oct 22:19  LEW_1910.txt
.rw-r--r--  1.1M sfmqrb 14 Oct 22:19  LKT.txt
.rw-r--r--   62k sfmqrb 14 Oct 22:19  LST.txt
.rw-r--r--  4.4M sfmqrb 14 Oct 22:19  MON_part1.txt
.rw-r--r--  4.3M sfmqrb 14 Oct 22:19  MON_part2.txt
.rw-r--r--  373k sfmqrb 14 Oct 22:19  MPP.txt
.rw-r--r--  470k sfmqrb 14 Oct 22:19  NAT_2005.txt
.rw-r--r--   139 sfmqrb 14 Oct 22:19  NYB.txt
.rw-r--r--  505k sfmqrb 14 Oct 22:19  NYB_vol1.txt
.rw-r--r--  920k sfmqrb 14 Oct 22:19  NYB_vol2_glossary.txt
.rw-r--r--  664k sfmqrb 14 Oct 22:19  PEI.txt
.rw-r--r--  8.4M sfmqrb 14 Oct 22:19  PHD.pdf
.rw-r--r--  341k sfmqrb 14 Oct 22:19  PHD.txt
.rw-r--r--  8.4M sfmqrb 14 Oct 22:19  PHD_mackenzie.pdf
.rw-r--r--  609k sfmqrb 14 Oct 22:19  PHD_mackenzie.txt
.rw-r--r--  609k sfmqrb 14 Oct 22:19  PHD_pages.txt
.rw-r--r--  604k sfmqrb 14 Oct 22:19  PHN.txt
.rw-r--r--  982k sfmqrb 14 Oct 22:19  POK_01.txt
.rw-r--r--  1.1M sfmqrb 14 Oct 22:19  POK_02.txt
.rw-r--r--  1.2M sfmqrb 14 Oct 22:19  POK_03.txt
.rw-r--r--  4.0M sfmqrb 14 Oct 22:19  POK_full.txt
.rw-r--r--  9.8M sfmqrb 14 Oct 22:19  RCH.txt
.rw-r--r--  1.3M sfmqrb 14 Oct 22:19  SBK.txt
.rw-r--r--  226k sfmqrb 14 Oct 22:19  SDQ.txt
.rw-r--r--  1.4M sfmqrb 14 Oct 22:19  SIN.txt
.rw-r--r--  2.7M sfmqrb 14 Oct 22:19  SKT.txt
.rw-r--r--  3.0M sfmqrb 14 Oct 22:19  SKT_dli_revised.txt
.rw-r--r--  326k sfmqrb 14 Oct 22:19  SNS.txt
.rw-r--r--  1.3M sfmqrb 14 Oct 22:19  SNS_pages.txt
.rw-r--r--  1.8M sfmqrb 14 Oct 22:19  SOD.txt
.rw-r--r--  3.7M sfmqrb 14 Oct 22:19  SOD_pages.txt
.rw-r--r--  466k sfmqrb 14 Oct 22:19  SPG_keilinschriften1881.txt
.rw-r--r--  4.5M sfmqrb 14 Oct 22:19  SYN.txt
.rw-r--r--  152k sfmqrb 14 Oct 22:19  TAD.txt
.rw-r--r--  243k sfmqrb 14 Oct 22:19  TAD_pages.txt
.rw-r--r--  313k sfmqrb 14 Oct 22:19  TLM.txt
.rw-r--r--   89k sfmqrb 14 Oct 22:19  UNV.txt
.rw-r--r--   12M sfmqrb 14 Oct 22:19  WEB_vol1.txt
.rw-r--r--  317k sfmqrb 14 Oct 22:19  WLD_band3.txt
.rw-r--r--  549k sfmqrb 14 Oct 22:19  ZAP.txt
Permissions Size User   Date Modified Name
.rw-r--r--   69k sfmqrb 14 Oct 22:14  page-50.json
.rw-r--r--   99k sfmqrb 14 Oct 22:14  page-51.json
.rw-r--r--   50k sfmqrb 14 Oct 22:14  page-52.json
.rw-r--r--   53k sfmqrb 14 Oct 22:14  page-53.json
.rw-r--r--   84k sfmqrb 14 Oct 22:14  page-54.json
.rw-r--r--   60k sfmqrb 14 Oct 22:14  page-55.json
.rw-r--r--   84k sfmqrb 14 Oct 22:14  page-56.json
.rw-r--r--   58k sfmqrb 14 Oct 22:14  page-57.json
.rw-r--r--   79k sfmqrb 14 Oct 22:14  page-58.json
```


## [2026-10-15T02:44:26.841Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification; sed -n 80,200p sources/SOURCE_MATRIX.md; cat /home/sfmqrb/git/rishe-private/tools/verify_check.py | head -150; python3 -c \"\nimport json;d=json.load(open('sources/refs_online.json'))\nfor k in ['POK','KLN','HRN','IEC','MON','FFD','SOD','AHD','AMD','SNS','BQT','WLD','PHD','NYB','BRT','CHEUNG','ARY','HUB']:\n  v=d.get(k); print(k, json.dumps(v,ensure_ascii=False)[:600] if v else None)\n\""
}
```


### [2026-10-15T02:44:27.255Z] TOOL RESULT

```
- **MON** — Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part1.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part2.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt`
- **FRS** — Asadi Tusi, Loghat-e Fors, ed. Mojtaba'i & Sadeqi, Kharazmi 1365/1986
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FRS.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FRS_pages.txt`
- **FSF** — Abdolhossein Noushin, Vazhe-namak: Farhang-e Vazheha-ye Doshvar-e Shahnameh (Farhang-e Shahnameh), Donya 1363/
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FSF.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FSF_pages.txt`
- **HENNING** — HENNING
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HENNING_selected_papers.txt`
- **EAV** — J. Duchesne-Guillemin, 'Etymologies avestiques', BSOAS 9.4 (1939) pp. 861-869
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/EAV_studies.txt`
- **ISS** — H. W. Bailey, Indo-Scythian Studies: Khotanese Texts VI (Prolexis to the Book of Zambasta), Cambridge 1967
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/ISS_alt_DKS.txt`
- **AHM** — I. Gershevitch, The Avestan Hymn to Mithra, Cambridge 1959
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/AHM.txt`
- **ARY** — Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپای
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY/ARY_pages.txt`
- **FFD** — Mohsen Abolghasemi, Fe'l-ha-ye Farsi-ye Dari, Qoqnus, Tehran 1374/1995
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/FFD/FFD_asmaneketab.pdf`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/FFD/FFD_pages.txt`
- **IRN** — Bahram Farahvashi, Iranvij, Tehran University Press 1368/1989
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/IRN/IRN_eliteraturebook.pdf`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/IRN/IRN_pages.txt`
- **AVG** — A. V. W. Jackson, An Avesta Grammar in Comparison with Sanskrit, Part I, Stuttgart 1892
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/AVG.txt`
- **HID** — C. Bartholomae, Handbuch der altiranischen Dialekte, Leipzig 1883
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HID.txt`
- **ZAW** — C. Bartholomae, Zum altiranischen Wörterbuch: Nacharbeiten und Vorarbeiten (Beiheft zu IF XIX), Strassburg 190
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ZAW/ZAW_bartholomae_1906_gb_agDP0HdEssEC.pdf`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ZAW/ZAW_pages.txt`
- **TLM** — H. C. Tolman, Ancient Persian Lexicon and the Texts of the Achaemenidan Inscriptions, Vanderbilt Oriental Seri
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/TLM.txt`
- **UNV** — J. M. Unvala, King Husrav and his Boy: Pahlavi text and glossary, Paris (Geuthner) 1963 [orig. 'Der Pahlavi-Te
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/UNV.txt`
- **SBK** — M.T. Bahar, Sabk-shenasi, vol. I, Tehran 1321/1942
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SBK.txt`

## Semitic / Arabic loans in either direction

- **KLN** — E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KLN_1966.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KLN_1971.txt`
- **FVQ** — Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FVQ.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FVQ_pages.txt`
- **AFM** — Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprin
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/AFM.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/AFM_pages.txt`
- **PLA** — A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/PLA/PLA_pages.txt`
- **AFA** — S. Fraenkel, Die aramäischen Fremdwörter im Arabischen, Leiden 1886 (repr. Hildesheim 1962, same pagination)
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/AFA.txt`
- **TAD** — Tobia al-Unaysi (طوبيا العنيسي), Tafsir al-alfaz al-dakhila fi al-lugha al-'arabiyya ma'a dhikr asliha bi-huru
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/TAD.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/TAD_pages.txt`
- **ARB** — al-Jawaliqi, al-Mu'arrab min al-kalam al-a'jami, Tehran 1966 (reprint of Ahmad M. Shakir's Cairo 1361/1942 edi
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/ARB_abdulraheem.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/ARB_mo3rb.txt`
- **KFL** — Tha'alebi, Fiqh al-lugha (wa-sirr al-'arabiyya), Beirut 1885
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KFL.txt`
- **LKT** — K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/LKT.txt`
- **PHN** — A. P. Pihan, Dictionnaire étymologique des mots de la langue française dérivés de l'arabe, du persan ou du tur
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/PHN.txt`
- **DEV** — L. M. Devic, Dictionnaire étymologique des mots français d'origine orientale, Paris 1876
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/DEV.txt`
- **LAM** — H. Lammens, Remarques sur les mots français dérivés de l'arabe, Beyrouth 1890
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/LAM.txt`
- **DOZ** — R. Dozy, Oosterlingen: Verklarende lijst der Nederlandsche woorden die uit het Arabisch, Hebreeuwsch, Chaldeeu
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/DOZ.txt`
- **AKD** — H. Zimmern, Akkadische Fremdwörter als Beweis für babylonischen Kultureinfluss, Leipzig 1917 (2nd ed.)
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/AKD.txt`
- **SIN** — B. Laufer, Sino-Iranica, Chicago 1919 (Field Museum Anthr. Ser. XV.3, pp. 185-630)
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SIN.txt`
- **MON** — Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part1.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part2.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt`
- **BQT** — Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/19
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_alt_v1.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_dli_part1.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v1.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v1_pages.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v2.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v2_pages.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf`

## English / Romance / Germanic

- **KLN** — E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KLN_1966.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KLN_1971.txt`
- **SKT** — W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SKT.txt`
- **FSD** — Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913,
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FSD_vol1.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FSD_vol2.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FSD_vol3.txt`
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/FSD_vol4.txt`
- **WEB** — Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/WEB_vol1.txt`
- **AHD** — W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appe
  `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/AHD_watkins1985.txt`
- **HJB** — H. Yule & A. C. Burnell, Hobson-Jobson, 2nd ed. by W. Crooke, London 1903 (Delhi reprint 1968)
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
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 34
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په
FFD {"title": "Mohsen Abolghasemi, Fe'l-ha-ye Farsi-ye Dari, Qoqnus, Tehran 1374/1995", "kind": "local_scan_ocr", "url": "https://asmaneketab.ir/product/کتاب-ماده-های-فعلهای-فارسی-دری-محسن-اب/ -> https://dl.eliteraturebook.com/app/public/attachments/6925d29630b83.PDF (free PDF site; grey)", "lookup_hint": "Searched archive.org (Persian/Latin titles, author), ketabnak, noorlib, general web (pdf/download): nothing; only a related paid e-book 'واژگان زبان فارسی دری' (fidibo). ketabnak.com/book/45024 is a different book (فهرست فعلهای فارسی).", "local_file": ["/home/sfmqrb/git/rishe-private/data/verifi
SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id=
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,
AMD {"title": "Hasan Amid, Farhang-e Farsi-ye Amid, 2 vols, Amir Kabir 1369/1990", "kind": "website", "url": "https://vajehyab.com/?q=<word>&d=amid ; https://abadis.ir/fatofa/<word>/ (فرهنگ عمید) ; scan on noorlib: https://noorlib.ir/book/view/28973?pageNumber=<N>&viewType=pdf", "lookup_hint": "Entry text online with origin tags ([پهلوی], [عربی]...); page numbers of the 2-vol 1369 print not mappable.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "Entry-level verification only."}
SNS {"title": "Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/VajnameShayest", "lookup_hint": "grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php search (see BQT) for better hit-to-leaf mapping.", "local_file": ["/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SNS_pages.txt", "/home/sfmqrb/git/rishe-private/data/verification/sour
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between le
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); ope
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603
CHEUNG None
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it 
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-
```


## [2026-10-15T02:44:30.501Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification; ls page-49*.json page-50*.json page-51*.json 2>/dev/null; python3 -c \"\nimport json;d=json.load(open('page-499.json'));e=d['entries'][0]\nprint(json.dumps({k:v for k,v in d.items() if k!='entries'}))\nprint(json.dumps(e['nodes'][0],ensure_ascii=False,indent=1)[:3000])\""
}
```


### [2026-10-15T02:44:30.826Z] TOOL RESULT

```
Permissions Size User   Date Modified Name
.rw-r--r--   68k sfmqrb 14 Oct 22:14  page-49.json
.rw-r--r--   69k sfmqrb 14 Oct 22:14  page-50.json
.rw-r--r--   99k sfmqrb 14 Oct 22:14  page-51.json
.rw-r--r--   64k sfmqrb 14 Oct 22:14  page-490.json
.rw-r--r--   55k sfmqrb 14 Oct 22:14  page-491.json
.rw-r--r--   70k sfmqrb 14 Oct 22:14  page-492.json
.rw-r--r--   68k sfmqrb 14 Oct 22:14  page-493.json
.rw-r--r--   62k sfmqrb 14 Oct 22:14  page-494.json
.rw-r--r--   60k sfmqrb 14 Oct 22:14  page-495.json
.rw-r--r--   66k sfmqrb 14 Oct 22:14  page-496.json
.rw-r--r--   35k sfmqrb 14 Oct 22:14  page-497.json
.rw-r--r--   64k sfmqrb 14 Oct 22:14  page-498.json
.rw-r--r--   49k sfmqrb 14 Oct 22:33  page-499.json
{"pdf_page": 499, "book_page": 469, "verified_by": "claude-opus-5", "verified_on": "2026-10-14"}
{
 "id": 1,
 "lang": "Sanskrit",
 "words": "tulâ, tulya",
 "verdict": "confirmed",
 "derivation": "Sanskrit tulā́ f. 'balance, scales; weight' continues the zero grade *tl̥h₂-éh₂ of PIE *telh₂- 'to lift, weigh, bear': syllabic *l̥ before the laryngeal gives Indo-Aryan ul (the l is the dialectal Indo-Aryan reflex of *l, the u the coloured vowel of the syllabic liquid). tulya- 'equal in weight, comparable, equivalent' is the -ya- derivative of tulā (Wiktionary: from tulā + -ya), and the verb tulayati 'lifts, weighs' belongs here. Nourai's gloss 'balance weight' fits tulā exactly; for tulya the precise sense is 'of equal weight, comparable', a natural derivative.",
 "derivation_fa": "سنسکریت tulā «ترازو، کفهٔ ترازو، وزن» از پایهٔ ضعیف *tl̥h₂-éh₂ ریشهٔ هندواروپایی آغازین *telh₂- «برداشتن، وزن کردن، تحمل کردن» است؛ l هجایی پیش از همخوان حلقی در هندی باستان به ul بدل شده است. tulya «هم‌وزن، همسنگ، همانند» صفتی است که با پسوند -ya از همین tulā ساخته شده و فعل tulayati «برمی‌دارد، می‌سنجد» نیز از همین ریشه است. ادعای نورایی درست است (پوکورنی ۱۰۶۰، واتکینز، والده‌ـپوکورنی، کلاین، ویکی‌واژه).",
 "sources": [
  "https://en.wiktionary.org/wiki/तुला",
  "https://en.wiktionary.org/wiki/तुल्य",
  "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/telh₂-"
 ],
 "ref_check": [
  {
   "ref": "POK:1060",
   "status": "supports",
   "note": "Pokorny IEW pp.1060-1061 (local POK_full.txt line 85184, 'Root /lemma: tel-1, tela-, tle(i)- tla-', Page(s): 1060-1061): 'Meaning: to transport, carry; to bear, suffer'; 'Old Indie tula 'scales, weight', tulayati 'hebt auf, wägt' ... tulya- 'gleichartig, comparable''; Greek tlēnai, talanton ('die beiden Waagschalen'), PN Atlas, -antos, telos 'payment, tribute, tax'; 'Latin tollo, -ere ... tolero ... latus 'getragen''."
  },
  {
   "ref": "AHD",
   "status": "supports",
   "note": "Watkins AHD Roots s.v. telə- item 9: 'Suffixed zero-grade form *tl-ā- in Sanskrit tulā, scales, balance, weight: TAEL, TOLA.'"
  }
 ],
 "consulted": [
  {
   "src": "WLD",
   "where": "Bd. I p.738 s.v. 1. tel-",
   "stance": "supports",
   "note": "Walde-Pokorny Bd. I pp.738-740 (local WLD_Bd1_pages.txt leaves 747-749) '1. tel- „aufheben, z. T. wägend, z. T. sich aufladend; tragen; ertragen, dulden“: Ai. tulā „Waage, Waagbalken“, tulayati „hebt auf, wägt“' ... 'τάλαντον ... eig. „die beiden Waagschalen“', 'Ἄτλας, -αντος', 'lat. tollo ... tolero ... lātus'."
  },
  {
   "src": "KLN",
   "where": "1966 s.v. tolerate / talent",
   "stance": "supports",
   "note": "Klein 1966 s.v. tolerate (KLN_1966.txt line 39457): 'L. tolerare ... from the stem of tollere ... cogn. with ... ταλάντον 'balance', ''A-τλας 'the Bearer (scil. of Heaven)', L. lātus (for *tlatos) 'borne', OI. tulā 'balance', tulayati 'lifts up, weighs' ... All these words derive fr. I.-E. base *tel-, *tol-, *tal-, *tl- 'to bear, carry, endure, suffer'.'"
  },
  {
   "src": "IEC",
   "where": "s.v. tl- (1) (IEC.txt line 18624)",
   "stance": "silent",
   "note": "Mann: 'tl- (1) ..
```


## [2026-10-15T02:44:52.330Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i \"teks-\\|tekþ\" POK_full.txt | head -20; grep -n \"tieg\\|tie[gĝ]\" POK_full.txt | head"
}
```


### [2026-10-15T02:44:52.901Z] TOOL RESULT

```
26108:Albanian: Albanian nje, Gtieg (Qosaj) n'a, Tosl< (i\4andritsa)u\, Armenian: +Classical 
73861:shtate, Gtieg (Qosaj) shtat, 7"o5/r ^A^a/7o'/7/say)shtate, Armenian: +Classical Armenian 
81616:Icelandic st/g/'m. 'Stiege, ladder', st/'gn. " footstep, grade'. Old English st/ge'das Hinauf- 
81617:or Herabsteigen', Old High German stega^grade, stairs, ladder' (Old High German stiega. 
81618:Modern High German Stiege W\Vc\ e^, also probably from *steigha)\ Old English staegeri. 
86829:Root / lemma: tieg"-
```


## [2026-10-15T02:44:54.982Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"Root / lemma: tek\" POK_full.txt; sed -n 86825,86860p POK_full.txt"
}
```


### [2026-10-15T02:44:55.548Z] TOOL RESULT

```
84963:Root / lemma: tek-1 
84986:Root / lemma: tek-2 
85013:Root / lemma: tek-3 
85088:Root / lemma: tek"- 
References: WP. I 742, WH. II 686, Mayrhofer 1 , 457. 

Page(s): 1 086 

Root / lemma: tieg"- 

Meaning: to retreat in fear 

Material: Old Indie tyajati{= gr. oEpu)) 'verlaftt, stands from etwas back', with /?/■ ' scare, 

frighten, verdrangen', with /7/5-'hinaustreiben, verjagen', participle tyakta-{= gr. a£nT6(;), 

noun agentis tyaktar-{= gr. GsoasnTwp 'Anbeterthe divinity'), Kaus. tyajayati^vmkes 

zuriJcktreten', tyajas-n. 'Verlassenheit' = Avestan i^yajah-, i&yejah-u. ds.; Old Indie 

tyaga-m. 'Hingabe, Freigebigkeit' etc.; 

gr. aspu) (only present and Impf.), oEpopai hom. '(die gods) scheuen', nachhom. '(die 
gods) worship, honour', Gfuioq, '(venerates =) venerable, holy', at^aq,, PI. aspn n. hom. 
'fromme fear, shyness, Ehrfurcht', nachhom. ' holiness, majesty ', hom. OEpaaaaTO 
'scheute ehrfijrchtig', az\xv6c, (*a£(3vo(;) 'admirable, venerable, convex, elevated, holy; 



gravitatisch, einherstolzierend, prunkend', aopsw "tue etwas from mirweg, entferne quick, 
fast, drive out'; intr. 'go eilig, stolziere einher', aopap6(; "rash, hasty, quick, fast; 
hochfahrend, prunkend', oo^aq, -a5o(;f. 'violent, vain', aopn "Pferdeschwanz'. Note: 
common lllyrian g"'- > b-. 

References: WP. I 746, Mayrhofer 1 , 529. 
Page(s): 1 086 

Root / lemma: to-1, ta-, tio- 

Meaning: that, he (demonstr. base)
```


## [2026-10-15T02:44:58.803Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 85086,85140p POK_full.txt"
}
```


## [2026-10-15T02:44:59.332Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"^teks-\\|^teks\\b\\|teks-\\.\" AHD_watkins1985.txt | head; grep -n -i \"^tyegw\\|tyeg\" AHD_watkins1985.txt | head"
}
```


### [2026-10-15T02:44:59.674Z] TOOL RESULT

```
Page(s): 1058-1059 

Root / lemma: tek"- 

Meaning: to run; to flow 

Material: Old Indie takti^ hurries, schieftt dahin', takta-, /a/r^- "hurrying, rash, hasty', takva- 

ds.; aKa//r^-"herabflieftend'; Avestan tacaiti' running, hurries; flows ', participle -taxta-, np. 

taxtan'run', hantac/na- ^zusamrr\eni\\eQ>end' (= Lithuanian tekinas^ running '), Avestan vi- 

taxt'h f. "das Zerflieften, Schmelzen' (= Inf. Slavic *tekti)\ here perhaps as 



'dahinschieftend': iran. (skyth.) *tahsa- {npers. taxs) "arrow, bow', from which gr. to^ov ds., 
Latin taxus^ yew' (Benveniste Mel. Boisacq 1, 37 ff., Mayrhofer 1, 467 f.); 

Avestan taka- m., np. /a/r'run, flow' (= Lithuanian takas, Slavic tokh); Avestan tacar- n. 
"run, flow, pathway', /5da/7- "hurrying'; /ad/'-ap- "running water (containing)', iran. *tahra- 
"quick, fast'; 

alb. /7oye/r" pursue'; 

Maybe alb. ndjej^ smell, perceive, feel (the hunt?)', ndjenje^ feeling '.' 

Old Irish techid^ flees ' (Perf. o-grade taich), ateoch^ beg ' {*ad-tek"'d^{ake meine 
Zuflucht'); brit. PN Vo-tepo-rTx, mcymr. ^oo'ep "Zufluchf, /©it'e/ "escape'; bret. tec'hetl\ee', 
mcymr. 3. Sg. Konj. /7y/y-o'e'c/7c»'wer nicht flieht' (brit. c/7from ks, s-Subjunktivstamm); 
Irish intechu. "way' ( *enitek"om, compare Old Church Slavic tekh "run, flow'); 

Gothic A'/^s "servant, farmhand' (= Old Indie takva-, actually " runner', compare Latvian 
teksn/s ^ Auiwarter, Bedienter'), Proto Norse A'eM/5/?"Lehensmann', Old English deofiA^), 
Old High German deo^ farmhand, servant', Fem. Gothic f^/m, Old Icelandic Ay, f^Ir, Old 
Saxon fh/m, thiu. Old English deowu, deowe{n). Old High German diu, diuwa' bondmaid, 
maid ' ( *tek-uT, development moviertes Fem. to *teku6-s, or to *tek'u-s. Old Indie taku-)\ 
with derivative as Gothic widuwairna^ orphan ' *t^ewerndn\v\ Old Icelandic ^erna' slave ', 
Old Saxon thiorna. Old High German diorna "virgin'. Modern High German Dime; n- 
extension in Old English deowen' bondmaid ', Old Icelandic ^yo/7/7 "servant', whereof 
*l=>ewandn^ serve ' in Old Icelandic t^ena, t^jdna. Old High German dionon, dionen^ serve 
'; Gothic a/7aA'/M/5/7 "subjugate, zum Sklaven machen'. Old English deowian. Old Icelandic 
Pjads.; lengthened gradees collective Gothic t^ewisau. PI. "servant, Knechte' {*tekueso-)\ 

Lithuanian teku, -et/^run, flow, rinnen; aufgehen (from the sun); marry (from the wife, 
woman)', Latvian teku, tecet \un'; Old Prussian tackelis, Lithuanian tekelas, Latvian teciels 
m. "grindstone, whetstone'; Lithuanian /e/r/77e"wellspring, river', //o/ra " estuary'; Latvian 
teksn/sm. "Bedienter'; Old Church Slavic tekg, test/" rpexeiv ', serb. tecem, /ec/"flow', etc.; 
Lithuanian takas^ path, track ', Latvian taks6s., Lithuanian Jtakas' estuary '; Old Church 
Slavic tokb ' puaiq ', potokh " x£iMC(PPO<; '; Tocharian B cake "river'; Hittite ua-tku-zi 
"springf. 

References: WP. I 715 f., Trautmann 316 f., Vasmer3, 89, 113 f., Mayrhofer 1, 466 f. 
Page(s): 1059-1060
```


### [2026-10-15T02:44:59.684Z] TOOL RESULT

```
1074:teks-. To weave; also to fabricate, especially with an ax; also to make wicker or wattle fabric for (mud-covered) house walls. 1. Latin texere, to weave, fabricate: TEXT,
```


## [2026-10-15T02:45:02.888Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"Root / lemma\" POK_full.txt | awk -F: '$1>85010 && $1<85090'; sed -n 85040,85086p POK_full.txt; sed -n 1074,1076p AHD_watkins1985.txt"
}
```


### [2026-10-15T02:45:03.400Z] TOOL RESULT

```
85013:Root / lemma: tek-3 
85033:Root / lemma: te/ct^- 
85056:Tocharian - Greek -g"h- > -kt-: -tk- see Root / lemma: ghdem-, ghdom-. Gen.- ablative 
85088:Root / lemma: tek"- 

and tasta-; also tasta- n. " cup, bowl'; Old Indie taksan- m. 'carpenter' (= Avestan tasan- 

"molder, creator, god', gr. tsktcjov), fem. taksnT{: gr. TSKiaiva), /as/a/"- 'carpenter' (compare 

Latin textor^ weaver '); 

Avestan /asa/if/ "zimmert, cuts, slices to, verfertigt', tasa-m. 'axe', np. tas6s., mp. 
tasfdan'do carpentry, do woodwork ', ap. us-tasana^ staircase' (*'construction'); 

maybe alb. /as 'deep bowl' 



gr. TSKTOov 'carpenter', fern. TSKiaiva, rsKpap, -cop "mark, token, sign', texvp) " handwork, 
art, artifice' (*T£^va from alterem *T£KT[£]ava); common Old Indie -g"h- > -ks- : Anatolian - 
Tocharian - Greek -g"h- > -kt-: -tk- see Root / lemma: ghdem-, ghdom-. Gen.- ablative 
gh(d)m-es\ earth' 

Latin texo, -ere, -u/-tuml\ax, wattle, braid, to weave', gelegentlich "to build', textor, -oris 
" weaver'; fe/a^ texture ' {*teks/a= Slavic fes/a, Old High German dehsala), subtTlis{*- 
texlis) "fine, thin, tender; feinfijhlig, sharp witted, shrewd', si/i6'/e/77e/7"Einschlag, Eintrag in 
texture; texture '; testat "Platte, shard, bowl', therefrom tes/Jo'd "turtle, tortoise' (compare 
above Avestan tasta-), perhaps also /eA//77"Fernwaffe, missile ' (as "kundig zugeschnitzt, 
gearbeitet'); 

Maybe alb. {*texere) fjerrl\ax, wattle, braid' 

Old Irish tar axe' {*tdks/o-); 

Old High German dehsa, dehsa/a 'Queraxt, hatchet, hack, mattock, hoe'. Old Icelandic 
l=>exlai. "Queraxf; Middle High German derisenl\ax break, rupture', dehse^ spindle'. Old 
English deoA- "spear, javelin'; Germanic *f^ahsu-\n Old High German daris, Norwegian 
svin-toks 'Dachs = badger ! 



Lithuanian tasau -ytr\\e\N' (originally iterative); Latvian tesu {* teks/o) and tesu{*teks/d), 
testand /es/"hew'; Old Church Slavic tesg, tesat/'hew', russ. -Church Slavic tes/a'axe', 
Czech /es"Zimmerholz', russ. /es"gesagte Bretter'; 

Hittite taks-, takkes- " piece together a jigsaw puzzle, fit together, unternehmen'. 

References: WP. I 717, WH. II 655, 656, 678 f., Trautmann 319 f., Vasmer 3, 99 f., 
Mayrhofer 468, 491, Durante, Ricerche lingunder 1, 234 ff., Pedersen Hittitisch 141 Anm. 
1; Specht Indo Germanic Dekl. 239 f., Leumann Kratylos 1, 29. 
Page(s): 1058-1059 
teks-. To weave; also to fabricate, especially with an ax; also to make wicker or wattle fabric for (mud-covered) house walls. 1. Latin texere, to weave, fabricate: TEXT,
TISSUE; CONTEXT, PRETEXT. 2. Suffixed form *teks-/é in:
69
```


## [2026-10-15T02:45:05.756Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 85033,85040p POK_full.txt; sed -n 1076,1085p AHD_watkins1985.txt; grep -n -i \"testa\\b\\|^test\\b\\|ters-\\.\" AHD_watkins1985.txt | head"
}
```


### [2026-10-15T02:45:06.127Z] TOOL RESULT

```
Root / lemma: te/ct^- 

Meaning: to plait; woodwork; carpenter 

Material: Old Indie taksat/ ^behaut, bearbeitet, zimmert, verfertigt', lengthened grade tast/ 

ds., participle tasfa-, common Old Indie -gh- > -ks- : Avestan -gh- > -xs-, -s- Avestan fasta- 

69
temp-
a. Latin téla, web, net, warp of a fabric, also weaver’s beam (to which the warp threads are tied): TILLER?, ToiL2; b. Latin subtilis, thin, fine, precise, subtle (< *sub-téla, “thread passing under the warp,” the finest thread; sub, under; see upo): SUBTLE. 3. Suffixed form *teks-On, weaver, maker of wattle for house walls, builder (possibly contaminated with *teks-tdr, builder), in Greek tekton, carpenter, builder: TECTONIC; ARCHITECT. 4. Suf- fixed form *teks-nd-, craft (of weaving or fabricating), in Greek tekhné, art, craft, skill: TECHNICAL, POLYTECHNIC, TECHNOLOGY. 5. Possibly Germanic *thahsu-, badger (“the animal that builds,” referring to its burrowing skill), in Old High German dahs (> German Dachs), badger but more likely borrowed from the same pre- Indo-European source as the Celtic totemic name Tazgo-, Gaelic Tadhg, “‘badger’”): DACHSHUND. [Pok. tekth- 1058.] tekv-. To run, flee. Suffixed o-grade form *tokv-so- in Iranian *taxsa-, bow, borrowed into Greek toxon, bow, also (in the plural) bow and arrow (< “that which flies’): Toxic. [Pok. tekz- 1059.] tel-. Ground, floor, board. 1. Germanic *thil-j6- in Middle Low German and Middle Dutch dele, plank: DEAL?. 2. Suffixed form *tel-n- in Latin telliis (stem telliir-), earth, the earth: (TELLURIAN), (TELLURIC), (TELLURION), (TELLURIUM), TELLURO-. 3. Possibly reduplicated form *ti-tel- in Latin titulus, placard, label, superscription, title: TITLE. [Pok. 2. tel- 1061.] tela-. To lift, support, weigh; with derivatives referring to measured weights and thence to money and payment. 1. Suffixed form *telo-mon- in Greek telamén, supporter, bearer: TELAMON. 2. Suffixed form *tel/a)-es- in: a. Greek telos, tax, charge: TOLL!; PHILATELY; b. Latin tolerdre, to bear, endure: TOLERATE. 3. Suffixed zero-grade form *th-i-, becoming *tali- (influenced by ¢dlis, such), in Latin ¢alid, reciprocal punishment in kind, “something paid out”: TALION; RETALIATE. 4. Suffixed variant zero-grade form *tala-nt- in Greek talanton, balance, weight, any of several specific weights of gold or silver, hence the sum of money represented by such a weight: TALENT. 5. Perhaps intensive reduplicated form *tantal- in Greek Tantalos, name of a legendary king, “the sufferer’: (TANTALIZE), TANTALUS. 6. Perhaps zero-grade form *tla- in Greek Atlas (stem Atlant-), name of the Titan supporting the world: ATLANTIC, ATLAS. 7. Suffixed zero-grade form *tl-é- in Germanic *thulén in Old English tholian, to suffer, endure: THOLE. 8. Suf- fixed zero-grade form *tl-to- in Latin ldtus, “carried, borne,” used as the suppletive past participle of ferre, to bear (see bher-'), with its compounds: ABLATION, COL- LATE, DILATORY, ELATE, ILLATION, LEGISLATOR, OB- LATE], PRELATE, PROLATE, RELATE, SUPERLATIVE, TRANSLATE. 9. Suffixed zero-grade form *tl-d- in San- skrit tuld, scales, balance, weight: TAEL, TOLA. 10. Nasal- ized zero-grade form *tl-n-a- in Latin tollere, to lift: EXTOL. [Pok. 1. éel- 1060.] tem-. Also teme-. To cut. I. Form *tema-. Nasalized form *t(e)m-n-a- in Greek temnein, to cut: TMESIS, TOME, -TOME, -TOMY; ANATOMY, ATOM, DIATOM, DICHOTOMY, ENTOMO-, EPITOME. II. Form *tem-. 1. Suffixed form *tem-lo- in Latin templum, temple, shrine, open place for observation (augury term < “place reserved or cut out”), small piece of timber: TEMPLE!, TEMPLE’; CONTEMPLATE. 2. Extended root *tem-d- becoming *tend- in o-grade suffixed (iterative) form *tond-eyo- in Latin tondére, to shear, shave: TONSURE. [Pok. 1. tem-, tend- 1062.] teme-. Dark. Suffixed form *tema-s-. 1. Latin temere, blindly, rashly: TEMERARIOUS, TEMERITY. 2. Suffixed form *temas-rd- in Latin tenebrae (plural), darkness: TENEBRAE, TENEBRIONID. [Pok. tem()- 1063.] temp-. To stretch. Extension of ten-. 1. Possibly Latin tempus, temple of the head (? where the skin is stretched from behind the eye to the ear): TEMPLE?. 2. Zero-grade form *tmp- perhaps in: a. Persian taftan, to weave (the
ten-
warp threads are stretched on the loom): TAFFETA; b. Iranian *tap-, “carpet,” in Greek tapés, carpet: TAPES- TRY. [Pok. temp- 1064.] ten-. To stretch. I. Derivatives with the basic meaning. 1. Suffixed form “ten-do- in: a. Latin tendere, to stretch, extend: TEND!, TENDER?, TENDON, TENSE!, TENT!; AT- TEND, CONTEND, DETENT, DISTEND, EXTEND, INTEND, OSTENSIBLE, PRETEND, SUBTEND; b. Latin portendere, “to stretch out before” (por-, variant of pro-, before; see per’), a technical term in augury, “to indicate, presage, foretell”: PORTEND. 2. Suffixed form *ten-yo- in Greek teinein, to stretch: TENESMUS; BRONCHIECTASIS, EPITA- SIS, HYPOTENUSE, PERITONEUM, PROTASIS, TELANGIEC- TASIA. 3. Suffixed zero-grade form *tn-nu- in Sanskrit tandéti, he stretches or weaves, with suffixed (instrumen- tal) derivative *ten-tro- in tantam, loom: TANTRA. 4. Suf- fixed form *ten-tro- in Persian ¢tdr, string: SITAR. 5. Basic form (with stative suffix) *ten-é- in Latin ten��re, to hold, keep, maintain (< “to cause to endure or con- tinue, hold on to”): TENABLE, TENACIOUS, TENACULUM, TENANT, TENEMENT, TENET, TENON, TENOR, TENURE, TENUTO; ABSTAIN, CONTAIN, CONTINUE, DETAIN, ENTER- TAIN, LIEUTENANT, MAINTAIN, OBTAIN, PERTAIN, PERTI- NACIOUS, RETAIN, (RETINACULUM), SUSTAIN. II. Derivatives meaning ‘‘stretched,” hence “thin.” 1. Suffixed zero-grade form *tn-u- in Germanic *thunw-, whence *thunniz in Old English thynne, thin: THIN. 2. Suffixed full-grade form *ten-u- in Latin tenuis, thin, rare, fine: TENUOUS; ATTENUATE, EXTENUATE. 3. Suf- fixed full-grade form *ten-ero- in Latin tener, tender, delicate: TENDER!, TENDRIL. III. Derivatives meaning “something stretched or capable of being stretched, a string.” 1. Suffixed form *ten-dn- in Greek tenén, ten- don: TENO-. 2. Suffixed o-grade form *ton-o- in Greek tonos, string, hence sound, pitch: TONE; TONOPLAST. 3. Suffixed zero-grade form *tn-ya- in Greek tainia, band, ribbon: TAENIA; POLYTENE. [Pok. 1. ten- 1065.] teng-. To soak. 1. Latin tingere, to moisten, soak, dye: TAINT, TINCT, TINGE, TINT; INTINCTION, STAIN. 2. Zero-grade form *tng- in Germanic *thunk- in Old High German thunk6n, dunk6n, to soak: punk. [Pok. 1. teng- 1067.] tenk-'. To stretch. Extension of ten-. Perhaps Germanic *thingam in: a. Old English thing, assembly, (legal) case, thing: THING; b. Old Norse thing, assembly: HUSTINGS; c. Old High German thing, ding (> German Ding), thing: DINGUS. [Pok. 1. tenk- 1067.] tenk-2, To become firm, curdle, thicken. 1. Suffixed form *tenk-to-, thickened, in Germanic *thinhtaz in Old Norse théttr, dense, watertight, akin to the Scandinavian source of Middle English thight, dense: TIGHT. 2. Possibly suffixed o-grade form *tonk-lo- in Germanic *thangul- in Old Norse théngull, seaweed (? < “thick mass”), akin to the source of TANGLE?. [Pok. 2. tenk- 1068.] tens-. To stretch, draw. Extension of ten-. Suffixed zero-grade form *tns-ero- in Sanskrit tasaram, shuttle: TussAH. [Pok. tens- 1068.] tep-. To be warm. Suffixed (stative) form *tep-é- in Latin tepére, to be warm: TEPID. [Pok. tep- 1069.] ter-. Base of derivatives meaning peg, post, boundary marker, goal. 1. Suffixed form *ter-men-, boundary marker, in Latin terminus, boundary, limit: TERM, TER- MINATE, TERMINUS; DETERMINE, EXTERMINATE. 2. Suf- fixed zero-grade form *tr-m- in Germanic *thrum- in Old English thrum, broken-off end (attested only in tungeth- rum, the ligament of the tongue): THRUM2. [Pok. 4. ter- 1074.] tera-1, To rub, turn; with some derivatives referring to twisting, boring, drilling, and piercing; and others refer- ring to the rubbing of cereal grain to remove the husks, and thence to the process of threshing either by the trampling of oxen or by flailing with flails. Variant *tré-, contracted from “*trea-. I. Full-grade form *ter@)-. 1. a. Latin terere (past participle tritus), to rub away,
70
ters-
thresh, tread, wear out: TRITE, TRITURATE; ATTRITION, CONTRITE, DETRIMENT; b. Greek teréddn, a kind of biting worm: TEREDO. 2. Suffixed form *ter-et- in Latin teres (stem feret-), rounded, smooth: TERETE. 3. Suffixed form *ter-sko- in Germanic *therskan, *threskan, to thresh, tread, in: a. Old English therscan, to thresh: (THRASH), THRESH; b. Old English therscold, threscold, sill of a door (over which one treads; second element obscure): THRESHOLD. II. O-grade form *tor(a)-. 1. Greek toreus, a boring tool: TOREUTICS. 2. Suffixed form *tor(e)-mo-, hole, in Germanic *tharma in Old High German darm, gut: DERMA2. 3. Suffixed form *tor(g)-no- in Greek tornos, tool for drawing a circle, circle, lathe (> Latin tornus, lathe): TURN; (ATTORN), CONTOUR, (DE- TOUR), (RETURN). III. Zero-grade form *tr- in Germanic *thr- in Dutch drillen, to drill: DRILL’. IV. Variant form *tré-. 1.Germanic *thréw- in Old English thrdwan, to turn, twist: THROW. 2. Greek tréma, perforation: MONO- TREME, TREMATODE. 3. Suffixed form *tré-tu- in Ger- manic *thrédu-, twisted yarn, in Old English thréd, thread: THREAD. V. Extended form tri- (< “trig-). 1. Suf- fixed form *tri-dn-, probably in Latin tid, plow ox: SEPTENTRION. 2. Suffixed form *tri-dhlo- in Latin tribu- lum, a threshing sledge: TRIBULATION. VI. Various ex- tended forms. 1. Forms *tré-, *trau- in Greek trauma, hurt, wound: TRAUMA. 2. Form *tru- in Greek truma, trumé, hole: TRYMA. 3. Form *érib- in Greek tribein, to rub, thresh, pound, wear out (> ¢ripsis, a rubbing): DIATRIBE, TRIBOELECTRICITY, TRIBOLOGY, TRYPSIN. 4. Form *trdg- in Greek trégein, to gnaw: TROGON. 5. Form *¢rup- in Greek trupé, hole (> trupanon, auger): TREPAN!; TRYPANOSOME. 6. Form *trig- possibly in Old French truant, beggar: TRUANT. [Pok. 3. ter- 1071.] tera-2. To cross over, pass through, overcome. Variant *trd-, contracted from “traa-. I. Zero-grade form “*tr()-. 1. Germanic suffixed form *thur-ila- in Old English thyr(e)l, thyrel, a hole (< “a boring through”): THRILL; NOSTRIL. 2. Suffixed form *tra-kve in Germanic *thurh in Old English thurh, thuruh, through: THOROUGH, THROUGH. 3. Greek nek-tar, overcoming death ‘(see nek-'). 4, Zero-grade form *tre- and full-grade form *ter(a)- in Sanskrit tirati, tarati, he crosses over: AVATAR. Il. Variant form ‘*trd-. 1. Latin trans, across, over, be- yond, through (perhaps originally the present participle of a verb *trdre, to cross over): TRANS-, TRANSIENT, (TRANSOM). 2. Suffixed form *trd-yo- in Iranian thrdaya-, to protect, in Middle Persian srdyidhan, to protect, in Persian sardi, inn: CARAVANSARY. III. Extended form *tru-. 1. Suffixed form *tru-k- in Latin trux (stem truc-), savage, fierce, grim (< “overcoming,” “powerful,” “pene- trating”): TRUCULENT. 2. Suffixed nasalized form *tru-n-k-o- in Latin truncus, deprived of branches or limbs, mutilated, hence trunk (? < “overcome, maimed”): TRENCH, TRUNCATE, TRUNK. [Pok. 5. ter- 1075.] terkw-. To twist. Extension of tera-'. 1. Possible variant form *twjerk- in Germanic *thwerh-, twisted, oblique, in Old Norse thverr, transverse: THWART. 2. Suffixed (caus- ative) o-grade form *tork’-eyo- in Latin torquére, to twist: TORCH, TORMENT, TORQUE}, TORQUE?, TORSADE, TORT, TORTUOUS; CONTORT, DISTORT, EXTORT, NASTUR- TIUM, RETORT!, TORTICOLLIS. [Pok. terk- 1077.] terp-. To satisfy oneself. Greek terpein, to delight, cheer: TERPSICHORE. [Pok. terp- 1077.] ters-. To dry. 1. Suffixed zero-grade form *trs-t- in Germanic *thurs- in: a. suffixed form *thurs-tu- in Old English thurst, dryness, thirst: THIRST; b. Old Norse thorskr, cod (< “dried fish”), whence Norwegian torsk, tosk, cod, with dialectal variant tusk, cod, stockfish: cusk. 2. Suffixed form *ters-d- in Latin terra, “dry land,” earth (> French and Old French terre, earth, ground): TERRACE, (TERRAIN), TERRAN, TERRENE, TER- RESTRIAL, TERRIER, TERRITORY, TUREEN; FUMITORY, INTER, MEDITERRANEAN, PARTERRE, SUBTERRANEAN, TERRAQUEOUS, TERREPLEIN, TERRE-VERTE, TERRICO-
teu-
LOUS, TERRIGENOUS, VERDITER. 3. Suffixed o-grade form *tors-eyo- in Latin torrére, to dry, parch, burn: TOAST!, TORRENT, TORRID. 4. Suffixed zero-grade form *trs-o- in Greek tarsos, frame of wickerwork (originally for drying cheese), hence a flat surface, sole of the foot, ankle: TaRSUS. [Pok. ters- 1078.]
1083:thresh, tread, wear out: TRITE, TRITURATE; ATTRITION, CONTRITE, DETRIMENT; b. Greek teréddn, a kind of biting worm: TEREDO. 2. Suffixed form *ter-et- in Latin teres (stem feret-), rounded, smooth: TERETE. 3. Suffixed form *ter-sko- in Germanic *therskan, *threskan, to thresh, tread, in: a. Old English therscan, to thresh: (THRASH), THRESH; b. Old English therscold, threscold, sill of a door (over which one treads; second element obscure): THRESHOLD. II. O-grade form *tor(a)-. 1. Greek toreus, a boring tool: TOREUTICS. 2. Suffixed form *tor(e)-mo-, hole, in Germanic *tharma in Old High German darm, gut: DERMA2. 3. Suffixed form *tor(g)-no- in Greek tornos, tool for drawing a circle, circle, lathe (> Latin tornus, lathe): TURN; (ATTORN), CONTOUR, (DE- TOUR), (RETURN). III. Zero-grade form *tr- in Germanic *thr- in Dutch drillen, to drill: DRILL’. IV. Variant form *tré-. 1.Germanic *thréw- in Old English thrdwan, to turn, twist: THROW. 2. Greek tréma, perforation: MONO- TREME, TREMATODE. 3. Suffixed form *tré-tu- in Ger- manic *thrédu-, twisted yarn, in Old English thréd, thread: THREAD. V. Extended form tri- (< “trig-). 1. Suf- fixed form *tri-dn-, probably in Latin tid, plow ox: SEPTENTRION. 2. Suffixed form *tri-dhlo- in Latin tribu- lum, a threshing sledge: TRIBULATION. VI. Various ex- tended forms. 1. Forms *tré-, *trau- in Greek trauma, hurt, wound: TRAUMA. 2. Form *tru- in Greek truma, trumé, hole: TRYMA. 3. Form *érib- in Greek tribein, to rub, thresh, pound, wear out (> ¢ripsis, a rubbing): DIATRIBE, TRIBOELECTRICITY, TRIBOLOGY, TRYPSIN. 4. Form *trdg- in Greek trégein, to gnaw: TROGON. 5. Form *¢rup- in Greek trupé, hole (> trupanon, auger): TREPAN!; TRYPANOSOME. 6. Form *trig- possibly in Old French truant, beggar: TRUANT. [Pok. 3. ter- 1071.] tera-2. To cross over, pass through, overcome. Variant *trd-, contracted from “traa-. I. Zero-grade form “*tr()-. 1. Germanic suffixed form *thur-ila- in Old English thyr(e)l, thyrel, a hole (< “a boring through”): THRILL; NOSTRIL. 2. Suffixed form *tra-kve in Germanic *thurh in Old English thurh, thuruh, through: THOROUGH, THROUGH. 3. Greek nek-tar, overcoming death ‘(see nek-'). 4, Zero-grade form *tre- and full-grade form *ter(a)- in Sanskrit tirati, tarati, he crosses over: AVATAR. Il. Variant form ‘*trd-. 1. Latin trans, across, over, be- yond, through (perhaps originally the present participle of a verb *trdre, to cross over): TRANS-, TRANSIENT, (TRANSOM). 2. Suffixed form *trd-yo- in Iranian thrdaya-, to protect, in Middle Persian srdyidhan, to protect, in Persian sardi, inn: CARAVANSARY. III. Extended form *tru-. 1. Suffixed form *tru-k- in Latin trux (stem truc-), savage, fierce, grim (< “overcoming,” “powerful,” “pene- trating”): TRUCULENT. 2. Suffixed nasalized form *tru-n-k-o- in Latin truncus, deprived of branches or limbs, mutilated, hence trunk (? < “overcome, maimed”): TRENCH, TRUNCATE, TRUNK. [Pok. 5. ter- 1075.] terkw-. To twist. Extension of tera-'. 1. Possible variant form *twjerk- in Germanic *thwerh-, twisted, oblique, in Old Norse thverr, transverse: THWART. 2. Suffixed (caus- ative) o-grade form *tork’-eyo- in Latin torquére, to twist: TORCH, TORMENT, TORQUE}, TORQUE?, TORSADE, TORT, TORTUOUS; CONTORT, DISTORT, EXTORT, NASTUR- TIUM, RETORT!, TORTICOLLIS. [Pok. terk- 1077.] terp-. To satisfy oneself. Greek terpein, to delight, cheer: TERPSICHORE. [Pok. terp- 1077.] ters-. To dry. 1. Suffixed zero-grade form *trs-t- in Germanic *thurs- in: a. suffixed form *thurs-tu- in Old English thurst, dryness, thirst: THIRST; b. Old Norse thorskr, cod (< “dried fish”), whence Norwegian torsk, tosk, cod, with dialectal variant tusk, cod, stockfish: cusk. 2. Suffixed form *ters-d- in Latin terra, “dry land,” earth (> French and Old French terre, earth, ground): TERRACE, (TERRAIN), TERRAN, TERRENE, TER- RESTRIAL, TERRIER, TERRITORY, TUREEN; FUMITORY, INTER, MEDITERRANEAN, PARTERRE, SUBTERRANEAN, TERRAQUEOUS, TERREPLEIN, TERRE-VERTE, TERRICO-
```


## [2026-10-15T02:45:11.466Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"^ *tasta-\\|^ *taša-\\|^ *tašta-\\|^ *tasa- \\|^ *taš-\\|^ *1. taš\\|^ *2. taš\" BRT.txt | head -20; grep -n \"iOyejah\\|iϑyejah\\|iθyejah\\|iSyejah\\|i&yejah\\|yejah\\|yajah\" BRT.txt | head"
}
```


### [2026-10-15T02:45:11.891Z] TOOL RESULT

```
3402:aiUyajah-  66
3431:•  j.  a-i!)yejahivajit-  Adj.  'ungefährdet': iüiyeJanuAatai  hala  anhaot  'jaisfmnt^m  avi aküm  H.2. 16.
5828:•  j,  astvat^rsta-  m.  EN.  des  dritten  der drei  Söhne  Zara^ustras,  die  aus  dessen; im  See  Kasaoya  aufbewahrten  Samen hervorgehen  sollen '' " :  uxsyatjtylahe  .  . uxsyai.mmanhs . .  'Iahe  aiaota  Yt  13. 1 28; HO,  117;  —  yttt  'lö /raxstäile  haca  apat kasaoyät  asts  mazdä  ahurahe  vjspa.taur- v'ayä  (sd.)  pu^rif  Yt.i5.92;  —  Aaxayif.. Hahe  vjrihrayne  Ytig.^s;  —  {'laAe)  ys atiAai  sao^as  (sd.)  vtrüraja  nama  'fasca iiqma  . .  ava'ha  'tS  ya%a  astva  kam  usfa- nava  (sd.)  astval  *aihyejahim  paitisät  Yt. JJ.129.
14454:•  j,,  g.  iSyajah-,  iS'yeJah-''  n.  'Not, Gefahr" ;  yS  nanm  .  .  apa  qzankal . .  apa 'ajat)hat  baraiti  YL/0.  aa;  —  ayh  'ejä vöiinä  Y.  57.  14;  —  tbaiA  ..  'eja  .. •e/ä  Y.  65. 8.  a)  mit  Dat.  'fUr -':  täis' .  .  ^ao%anJis  ,  .  yaiiü  as  pairJ  pountbyö (sd.)  -ejs  "..,  in  denen  für  viele  Gefahr  liegt" Y,J4.8.  A)  insbes.mitffiarj-W«?'*GS. und  mit  marsaona-'^  Adj.:  'ejö  mariao- tum  V.  ig.  I,  2,  43;  —  'ejanhs  mars'ath nahe  Yt6'.  4;  —  -ajaftkasca  marsaonahe^ Ytrj,i3o;  —  °ejä  marlaonS  V.iS.S.        I
```


## [2026-10-15T02:45:15.644Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 14450,14460p BRT.txt | cut -c1-600; grep -n \"tasta-\\|tašta-\\|'Schale\\|Napf\" BRT.txt | head -20"
}
```


### [2026-10-15T02:45:16.040Z] TOOL RESULT

```
Super),  in  '%wyaHl-  Adj.,  PPA.  lum  V.  %'uiay-. —  PO.:  timakeittar.  —  >l  Es  sind  die  ebe  aen Sand-  und  SalzwQsten  im  Gegensati  zu  den Bergen  und  Tälern  gemeini.  Pü.  führt  als Beispiel«  für  die  beieichneten  drei  Örtlich- keiten der  Reibe  nach  an:  spähän,  afiärsen, äräsiänlf).     Vgl.  Dst.  ZA.  2.  15-
•  j.  aetahe  "9«asat"  tbisamiAa  V.  7.  52 PüZ.
')  Nach  JN.  JAOS.  16.  cxxvm  sva.  sHa%al, 35.;  aber  die  gegebene  Obersetiung  itt  un- möglich.
•  j.  Snätö   F.  2^:   -?-. Pü. :  faßrisH.
•  j,,  g.  iSyajah-,  iS'yeJah-''  n.  'Not, Gefahr" ;  yS  nanm  .  .  apa  qzankal . .  apa 'ajat)hat  baraiti  YL/0.  aa;  —  ayh  'ejä vöiinä  Y.  57.  14;  —  tbaiA  ..  'eja  .. •e/ä  Y.  65. 8.  a)  mit  Dat.  'fUr -':  täis' .  .  ^ao%anJis  ,  .  yaiiü  as  pairJ  pountbyö (sd.)  -ejs  "..,  in  denen  für  viele  Gefahr  liegt" Y,J4.8.  A)  insbes.mitffiarj-W«?'*GS. und  mit  marsaona-'^  Adj.:  'ejö  mariao- tum  V.  ig.  I,  2,  43;  —  'ejanhs  mars'ath nahe  Yt6'.  4;  —  -ajaftkasca  marsaonahe^ Ytrj,i3o;  —  °ejä  marlaonS  V.iS.S.        I
KompE. ;  Ableiu  —  ai.  lyd/as-  n.  (woiu  ZDMG. JJ.aSi).  —  Pü.:  lii  (s.  d«iu  HB«.  PSl.  iio), Sa.:  mj'lyuii.  —  ')  J  ajrf.  i.  —  a)  Sd.
•  j.  iS-yeJah'vant-  Adj.  (fem.  °vaiti-)  'ge- fahrvoll, mit  Gefaliren  umgeben':  'Javu- hatat  a>9haof  ai^yejavhuntim  avi  Bhum H.2. 16;  V.  7.  52,  75.31  (beide  Male  'jar^ katat);    —    tanvö  •jaauhaiti  (VSf)  Aog.
25-2*'^.
KompE.  —  Pü.:  asHömatui,  Sü.:  vinälai'än.
•  j.  draetaona-  m.  £N.  eines  Helden der    iranischen    Sage,    Fariäün'^:    *mm
idswyilHim  FrW.  2.  i ;  —  'naAe  ithwyanBif Vt./j.i3i,  *FrW.2.i,  3i  —  vm pu'^rff ähwyanSi!  vXsS  sarayä  'nö  Yt.5, 33,  17. 35;  —  vartnfm  yim  cahrugaospm  yakmäi tayata  'nB  Janta  aSsis  i/aAäiät  V. /.  17; —  'rur  yS  janal  aiim  äahäk^m  Y.g.jt; Yt.  j^  40,  lg.  9a ;  —  'ftSyat  äs  masyanqm ..  wrüravastimö  ..  Yt/9.36;  Az.2;  — päurvö  (sd.)  .  .  yal  dim  usca  usdvanayaj Vfrf%rajä  taxtnS  'ne  Vtj.  öi;  —  tl  ySi pü^ra  'nahe  F.4C
9788:•  j.gao-dana,  °jiana-  n.  1)  'Milchgeföss': frä  tl  Aasaanm  xam  aam  . .  frasnaymi ''.an?m  avi  hatUaiinh  ya^  asti  puirake >rims"^e  tausend  Quellen,  die  zum  Milch- gefiss  zusammenfliessen,  das  die  Nahrung des  Kindes  ist"  V.  21. 7  ".  s)  überh. 'Gcfäss,  Napf,  Schüssel'  (nur  Komp.,  s. N.  64).
25530:•  j.  urunya-  m,  'Gefäss';  i)  für  den Myazda,  'Schale,  Schüssel':  yailam  taya- nqm  aiaurune  . .  °ya  rai^wis.6ajina  , . V./4.8.  2)  Du.  die  beiden  Gefässe, 'Eimer'  od.  dgl.,  in  denen  den  Rossen Wasser  und  Futter  gereicht  wicd(?):  äpe urvaire  yazamaide  aourvatqm  •/w(AD.)" asavantm     asahe     ratum    yazamaide    G.
30240:•  j.  hu-täita-  Adj.:  s.  unter  hutasta-
```


## [2026-10-15T02:45:19.517Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"zimmer\\|'Axt\\|Beil\" BRT.txt | head -20 | cut -c1-400; grep -n \"Ovarss\\|Svaras\\|^\\S*  *\\S*varas-\\|9warss\\|^•  j.  [^ ]*waras\" BRT.txt | head | cut -c1-300"
}
```


### [2026-10-15T02:45:20.054Z] TOOL RESULT

```
4467:Durch  Haplol.  (Sjoff)  aiis*d«-ini('>>;  s.  unter intay.—  Vgl.  ainila:  —  Pü.  (in  l):  akimh^\ (102):  akin.  —  ')  Anders  Leumahn  EtWb.  34, —  »}  Für  aimlöii  hat  Pü. :  dak  n  aa,  erl. :  ax^äsla- kih  mit  Npü.  gaili  'Beiller';  s.  dazu  Haug ZPGl.  59,  PPGl,  an.
6774:—  4)Pü.;  i'i/;Sn  ojc' iämat.tiV:  eigön  öhi-maid  (doch  %.  Yl.  3.  S).  Es  gehört  lu  den  i'on  13- kämak;  s.  SBE,J7. 6.  — i)  Es  itt  anscheinend  %niiämriila,  s.  V.  /o.  11,  N.  jtf,  Y.  5,  14-  Seine von  Ml^ra  die  Rede.  Ich  halte  die  Stelle  '  21  Worte  wurden  später  mit  den  zi  Teilen  i>. für  verschleppt.  —  *)  Mit  'a' ;  falsch  Bn.  Stud. '  naikö.'
10878:Bed.  nach  Sü.,  Npü.  —  Durch  HapluL  (S.?o(5} aus  *xU.\va'vanl-y\  s.  xHäTjahtya-.  —  Et? Wertlos  oder  falsch  Gdn.  Stud.  /.  159,  Gg«. OK.  189.  ZUBATY  BB.  18. 247,  J"STi  NB.  176 (nach  DBLagarde  Beilr.  43)").  —  Pü.:  fehlt, Sil.;  lakfiaivän,  Npü.:  nur  diranda.  —  >)  Vgl. irimani:  —  ')  Das  v  in  np.  sitäv  geht  auf ir.  /,  E.  arm.  LW.  i/u/.
12138:•  j.  ta^-  ra,  'Axt'; inütfm  V.  14. 7.
12297:•  j,  tizi^nüta-  Adj.  'scharfgeschliffen,  j scharfkantig':  iasm  ('Axt')  HnJitr?m  °t?m  ■ va/bm  ('Keil')  ttöiMnm  'hm  ^.i4.T.      1
17199:Wn.  Venn.BeilT.z.griech.Spr.  9.
25983:KompE.  —  Vgl.  gr-  «-ivr^-miir-a  :  bL  faiicä- Idi-ah.  —  zEt  (Ableit.  aus  daia)  %.  Beil.  Gidi.
26855:EL?  ah  steht  für  ng,  vgl.  ta  'haoha-  Es stellt  »ich  somit  sp'  seiner  Bildung  nach  zu ai.  ^Ä^B-  n.  (woiu  Johansson  Beilr.  13,  IF. a.  24.  Bthi,-  IF.  3.  j68).  —  Fa.:  ha^aiar  i dandän,  übers,  mit  np.  :;>  i  dandan  'unter- halb der  Zähne'.
28909:KompA.  {Anxä',  haii'\  E.  —  ai.  tdUay-  m-  — iFlex.  i.  S  406.  —  EL?  Vgl.  Beil.  GrCr.3 183.  —  Ffi.;  äSsl;  hamträliak),  erL:  träS  i döst.   —   ■)  S  (pO.  3  a.
11156:•  j.  £a9-warasata-  Adj.  'der  vierzigste': °t3tn  gaosfm  fräyasämaide  N.  6$  (?).
```


## [2026-10-15T02:45:22.047Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 12125,12145p BRT.txt | cut -c1-500"
}
```


### [2026-10-15T02:45:22.344Z] TOOL RESULT

```
•  j.,  g.  taä-  V.  'zuschneiden'.  Praes. 2  tasa-,  15  tat-;  j-Aor.  i  t3y-;  Y^tL 1   iaias-,  PfPr.  iaiaia-.  —  PPfP.  iaita-^
dby  Google
«45
'zuschneiden,     zurcchtschneiden',     mit'^ai'°jW(iiäml.aj'a/^)hetsstderi4.Monats-
Messer  oder  Axt:  tas'tpin  däuru  (sd.)  V. y-  30-  a)  insbes.  'schnitzen   sva.  ver-
fertigeD,  gestalten,  schaffen';  daidx  möi  y5 gqm  tasö  apaslä  urvarascä  .  .  "gib  mir, der  du  das  Rind  geschaffen  hast  und  die Wasser  und  die  Pflanzen . ."  Y. si.j;  44.6;
—  ahurahe ..  yS  ns  dala  yS  tatasa  {^SPiA.) yS  tu^ruyl  Y.  /.  i;  Yt  ig.  52;    —    at  ti
"iwä  (nUml.  gam)  fsuyantaicä  . .  ^wsnsta (sd.)  latasä  Y.  2Q.  6;  —  Ayat  . .  galiäsca taiS  (2S.)  dainascä  (sd.)  Y.  j;.  11;  — ö*i  äzüiBis  (sd.)  ahurö  mq^r^m  tasat  Y. 2p,  7;  I,  ¥.j8;  —  aumanUm  %w3  (näml. Aoomm)  . .  bayn  iatala/  (PfPr.)  Y.  10.  10;
—  kj  bfTPXoqm  täst  xsairä  mal  ärmaüTm "wer  schuf  sammt  dem  Xs'.  die  geschätzte Ärm.r'  Y.44T,  —  /singhyö  (sd.)  suyS taitS'^  Y.  417.9.
mit  avi  '(Holz)  in  Scheite  zerlegen'.": avi  dim  (näml.  vanqm)  janaiti  avi  dim %w^r3saiti  avi  dim  täiti  "er  fällt  ihn  (den Baum),  zerlegt  ihn  in  Blöcke  und  weiter in  Scheite"  V.5.  i.
mit  harn  dnwS.3:  yasäi  ham.tastim {väsim?)  Yt/o.  143;  —  yS  ahmäi  gqm *ränys.sk)riitlm    (sd.)    hSmJaM    Y.47. 3;
—  yS  driyaosca  . .  amavat  nmän^m  Äqm.- tästi  Y.57. 10;  —  ariduTm  .  .  yeiihe  (LS. statt  DS.?)  ^diwilrS  arsäna  hqm.t3sat ahurs  Yt5,  lao;  —  'hqmjalta'.
si.  läisali,  täjü,  ia/äkfa;  la^ldi;  mp.  (PU.) /äji". /an.  —  ')  i  20g.  7  No.  II.  —  ')  Pü.:  JÜ/ A'äj/är  (St.);  lül  läSlär  (MttLS),  «ber  Sü.r läbham    abhilätaiya,    —    31  Pü. :    tat  isk  afar
•  j.  ta^-  ra,  'Axt'; inütfm  V.  14. 7.
Zum  V.  las-.  —  np.  1
(  aSi.därym  tizi.-
tag'*' ;  gSus  -sne  gSul  u
*)  Über  die  Bedeutung  dieser  Gottheit,  bin- sichtlich  deren  die  Tradition  sicher  irrt  (s.  unten), vgl.  Bthl.  AF.  j.  25,  Bn.  Stud.  /.  383,  JusTi PrJ.  88.  77.  TlKLE  Godsdienst^  3.  125  kommt zu  Unrecht  Mf  Hauo»  Ansichten,  Essays"  147 luiück.  Die  Tradition  versteht  zu  Y.  sg  (,  31, 46t)  unter  GT.  Atn  AHM.,  sonst  den  Leib  des Rinds  im  Gegensatz  zu  g/u!  titvan-;  vgl.  DsT. ZA.  I.  g,  215.  —  **)  Im  Mp.  gi!  genannt.  An den  mit  S.  /.  14
Zum  V.  las..  —  ai.  läifan-  m.  —   Pü,  (zu  Y.
^9.  3ft  46) '■    gäspand   täSitär,    zu  Y.  3g    erl.:
äkrmaid,  sonst  göspand  tan.  —  >)  S.  zSt,  Gdw.
```


## [2026-10-15T02:45:28.487Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i \"tarā[sš]\\|taras\\b\\|tarash\\|tarāš\" CHEUNG.txt | head -20; grep -n \"warHs\\|warš\\|wars-\\|ϑwar\\|θwar\\|Owar\" CHEUNG.txt | head -20"
}
```


### [2026-10-15T02:45:29.030Z] TOOL RESULT

```
25572:*AVESTAN: YAv. Oränh- (taras-) ‘to fear’ || (+ *abi-) caus.‘to scare hither’ || (+
```


## [2026-10-15T02:45:32.180Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"Owar\\|0war\\|Bwar\\|Ouar\\|Owor\\|Owaras\" CHEUNG.txt | head -20; grep -n -i \"tara[sš]-\\|tarās\\|tarash\\|trāš\\|tras-\" CHEUNG.txt | head"
}
```


### [2026-10-15T02:45:32.746Z] TOOL RESULT

```
25931:*Ouar/tur ‘to hurry, hasten’ 
25987:ology, proposed by Bailey, DKS: 149b, for Khot. thurs-, viz. from root *Ouars, is 
25072:*NWIR: NP tirasidan/tiras- ‘to shave’, Bal. trast, trasit/tras- ‘to mend, chip, cut, 
25106:Steblin-kamenskij 1999: 368 Ё; Lecoq 2002: 122, 129 (passim); МЕУР: 81; Shahbakhsh: s.v. tras-; Korn 
25572:*AVESTAN: YAv. Oränh- (taras-) ‘to fear’ || (+ *abi-) caus.‘to scare hither’ || (+ 
42105:trast, trasit/tras-, 385
```


## [2026-10-15T02:45:34.890Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 25055,25110p CHEUNG.txt; sed -n 25980,25995p CHEUNG.txt"
}
```


### [2026-10-15T02:45:35.292Z] TOOL RESULT

```
"MIDDLE PERSIAN: ВМР t’s- /tas-/ ‘to cut, cleave; create’ 

Partic.: perf. pass. BMP t’sytk /tasidag/, ВМР гу /tasid/ 

*KHOTANESE: OKh. ttäs- ‘to cut [tr. © SGS: 38 


*tau ? 385 


*SOGDIAN: BSogd. t’s, MSogd. t^s ‘to cut’ 
Pres.: IND. 3sg. BSogd. t’st, SUBJ. 3sg. BSogd. t’s’t, 3pl. BSogd. t'$^nt; Impf.: IND. 3sg. BSogd. t'$ 
(L37.3(23)), 3р1. MSogd. "t'ándskwn 


*CHORESMIAN: (+ *upa-) b’d- ‘to build; cut’ = Samadi: 14 

*NWIR: NP tirasidan/tiras- ‘to shave’, Bal. trast, trasit/tras- ‘to mend, chip, cut, 
shave’ (< Pers.), Kurd. (Sor.) täsin/täs- ‘to hew; to shave’, Awrom. tašáy/taš-, Qohr. 
tasada/tas-, Tr. taSaya/tas- ‘to shave’, NP tas ‘hatchet, adze’, Bal. tas ‘adze’ (< NP?). 
© The intrusion of -r- in NP tirasidan/tiras- points to contamination with NP 
xiraSidan/xiras- ‘to scratch (a wound)’, v. *xrà&. || The -r- in Bal. trast, träsit/träs- 
suggests borrowing from Persian (rather than a parallel development). The 
borrowing must have occurred quite early, considering the absence of anaptyxis in 
the initial consonant cluster, which is a typical feature of New Persian. 

*NEIR: (?) Oss. I. dasyn/dast, D. dasun/dast ‘to shave’, Yghn. tos-/tásta ‘to hew, to 
shave (off); to scratch, scrape (off); to shear’, Sh. täX-, Rosh. töw-/tüxt, Bart. töX-, 
Sariq. tux, Yzgh. taw-/text ‘to cut, whittle, shave, prepare’, Yghn. tos-, M. tiZ-/toyd, 
Yi. tiZ- ‘to shear’, Wa. tsrš-/tošt ‘to cleave; to shave, shear’, Pash. tog- ‘to shave, 
plane’, Pash. tiyaso (Ё) "plough-share' || (+ *ham-) ? Oss. I. zntysyn/entyst, D. 
æntæsun/æntæst ‘to succeed in’ (sec. prefixation). Ф The initial d- of Oss. I. dasyn, 
D. dasun is from compounds, e.g. serdasen ‘razor, v. EVP: 83, no. 378. 

*MISC: Par. thä- ‘to cut, shave’, Arm. (LW) tasem ‘to cut’ 

*SANSKRIT: taks ‘to form (by cutting), to prepare, build, carpenter’ (RV+), taksan- 
‘carpenter’ = EWAia I: 612 

© The root of the OP forms shows contamination with *@uaxš (tuxš), which is 
attested in Av. in the middle voice only. 

«PIE *tetK- ‘to construct, build by cutting’ = LIV: 638 f. | Pok.: 1058 f. 

*IE COGNATES: Gr. тёктоу ‘carpenter’, OCS teSo (tesati) ‘I cut, hack’, Lith. tasau 
(tasyti) ‘I cut, carve’ 

*REFERENCES: EVP: 83, 85; IFL I: 293a; Abaev, Slovar’ I: 167; Andreev — Реёќегеуа: 338a f; 
MacKenzie 1966: 110; EVS: 82; Nyberg II: 192b; DKS: 129b f.; Werba 1997: 189; Cabolov 1997: 72; 


Steblin-kamenskij 1999: 368 Ё; Lecoq 2002: 122, 129 (passim); МЕУР: 81; Shahbakhsh: s.v. tras-; Korn 
2005: 92, 216, 365 


*tau ? ‘to throw, spread, sow’ 
*SANSKRIT: tvastar- PN (god of creation, Creator) = EWAia I: 685 f. 


400 *Quaxs (tuxš) 


9 Av. @Baras- is isolated in Iranian: no other correspondences are attested. The etym- 
ology, proposed by Bailey, DKS: 149b, for Khot. thurs-, viz. from root *Ouars, is 
untenable, on which see SVK II: 54 ff. As for an IE origin, no verbal corres- 
pondences can be cited. The nominal forms frequently cited as cognate, Gr. сарё, 
(Aeol.) съркес̧ (pl.) ‘(pieces of) meat’, ? Olrish turc (m.) ‘boar’, are semantically 
possible, but not very informative with regard to morphology and derivation. 

«PIE? > LIV: 656 | Pok.: 1102
```


## [2026-10-15T02:45:41.035Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/FFD; grep -n \"تراش\" FFD_pages.txt | head; grep -n \"pdf page\" FFD_pages.txt | head -3"
}
```


### [2026-10-15T02:45:41.605Z] TOOL RESULT

```
1282:تراشیدن
1283:«تراشید» مادهٌ ماضی جعلی است. از مادهٌ مضارع ساخته شده است.
1284:تراش < پهلوی اشکانی 1۶385 < ایرانی باستان ۸۲33-2*. برای ۵ -> آرای. 8735 صورت
1:[pdf page 1]
24:[pdf page 2]
59:[pdf page 3]
```


## [2026-10-15T02:45:44.297Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/FFD; awk 'NR<1282 && /pdf page/ {p=$0} END{}; NR==1282{print p}' FFD_pages.txt; sed -n 1270,1300p FFD_pages.txt; grep -n \"تاشیدن\\|تاش\" FFD_pages.txt | head"
}
```


### [2026-10-15T02:45:44.818Z] TOOL RESULT

```
[pdf page 51]
اصلی 13 است» 1 پیش از 1 به بدل شده است. 13 صورت بالاندةٌ 18 است» ريشهٌ 18
به معنی «دویدنْ» است و 131 به معنی «دوانیدن».
در فارسی میانه 133122 به معنی «دواندن» است.
تاز < فارسی میانه 132 < ایرانی باستان 130-۵*.برای 2 -> آرای. #به‌جای ‏ آمده است.
[pdf page 51]
وا فعلهای فارسی دری
تافتن
تافت < فارسی میانه 1 گرم کردن < ایرانی باستان ۴13۳-12 برای 18 -> آراست.
۱ 0 صورت اصاٍ است. « پیش از ۲ به 1 بدل شده است. 150 صورت بالاندة 1۸0
است» 130 به معنم «گرم‌شدن» است و 130 به معن «گرم کردن». «تفتن) از 130 آمده
است -> تفتن» تفسیدن.
تاب < فارسی میانه 130 < ایرانی باستان 130-8*. برای 2 -> آرای.
تراشیدن
«تراشید» مادهٌ ماضی جعلی است. از مادهٌ مضارع ساخته شده است.
تراش < پهلوی اشکانی 1۶385 < ایرانی باستان ۸۲33-2*. برای ۵ -> آرای. 8735 صورت
بالاندةٌ ریشهٌ 1525 است. 1728 و 5 هر دو «بریدن» معنی می‌دهند.
ترسیدن
«ترسید) ماده ماضی جعلی است. از مادهٌ مضارع ساختة شده است.
ترس < فارسی میانه 1158 + ایرانی باستان 1782 < 178-8-4. برای 2 > آرای. 5 برای
ساختن مادةٌ آغازی از ريشه به کار می‌رفته است. 17 صورت اصلی 178 است» « پیش از ‎٩‏
‏به 9 بدل و در 5 ادغام شده است. «هراسیدن» هم از 158 آمده است. -> هراسیدن.
تفتن
تفت < فارسی میانه 12 < ایرانی باستان 1۵۳-4*. برای 18 -> آراست. 1۸0 صورت
اصلی 1۶ است. 0 پیش از 1به ۶ بدل شده است.
تب < فارسی میانه 120 < ایرانی باستان 1۵0-2*. برای 2 -> آرای. «تأافتن» از ريشهٌ
130 به معنی «گرم‌شدن» آمده است. -> تافن و تفسیدن.
تفسیدن
(رتفسید) ماد ماضی جعلی استء از ماده مضارع ساخته شده است.
[pdf page 52]
ماده‌های ماضی و مضارع فارسی دری شش ۴۷
تفس « ایرانی باستان 12۳8-8*. برای 2 > آرای. 8 نشانه‌ای بوده که برای ساختن
```


## [2026-10-15T02:45:48.259Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 tools/ref_page.py FFD:46 --image 2>&1 | tail -15"
}
```


### [2026-10-15T02:45:49.171Z] TOOL RESULT

```
no scan of FFD covers printed page 46 (see 'scans' in refs_online.json)
```


## [2026-10-15T02:45:53.639Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/FFD; mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/p509; pdftoppm -f 51 -l 51 -r 200 -png -singlefile FFD_asmaneketab.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/p509/ffd51-509; ls /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/p509/"
}
```


### [2026-10-15T02:45:54.623Z] TOOL RESULT

```
Permissions Size User   Date Modified Name
.rw-r--r--   77k sfmqrb 14 Oct 22:45  ffd51-509.png
```


## [2026-10-15T02:45:56.958Z] TOOL CALL #24: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/p509/ffd51-509.png"
}
```


### [2026-10-15T02:45:56.971Z] TOOL RESULT

```

```


## [2026-10-15T02:46:01.931Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; ls ocr | head -30; grep -n \"t'š\\|tʾš\\|t’š\\|t's \\|t'sh\" SOD_pages.txt | head -20"
}
```


### [2026-10-15T02:46:02.461Z] TOOL RESULT

```
Permissions Size User   Date Modified Name
drwxr-xr-x     - sfmqrb 14 Oct 22:19  AFM
drwxr-xr-x     - sfmqrb 14 Oct 22:19  ARY
drwxr-xr-x     - sfmqrb 14 Oct 22:19  BLY
drwxr-xr-x     - sfmqrb 14 Oct 22:19  BOOK
drwxr-xr-x     - sfmqrb 14 Oct 22:45  BQT
drwxr-xr-x     - sfmqrb 14 Oct 22:19  FFD
drwxr-xr-x     - sfmqrb 14 Oct 22:19  HRN
drwxr-xr-x     - sfmqrb 14 Oct 22:19  IRN
drwxr-xr-x     - sfmqrb 14 Oct 22:27  PLA
drwxr-xr-x     - sfmqrb 14 Oct 22:19  SNS
drwxr-xr-x     - sfmqrb 14 Oct 22:19  SOD
drwxr-xr-x     - sfmqrb 14 Oct 22:19  TAD
3695:Locust's Leg. Henning, W. B. (ed). A Locust's Leg;                Seminar on the Religio-Historical Character of
11008:          sufficient                                                         VJ 1092; Gersh. Locust's leg 83
18550:                                                                          wish jcv/G\(heart's wish)
31181:9499 t's M                                            *>.y
37244:                                                                     TSP 13.22 n p228, 14.10; Gersh. Locust's leg
38518:heart's wish 5212                     highest rank 8941                       horse armour      1623
```


## [2026-10-15T02:46:04.901Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; ls ocr/FFD ocr/SOD | head; sed -n 31160,31215p SOD_pages.txt; awk 'NR<31181 && /pdf page/ {p=$0} NR==31181{print p}' SOD_pages.txt"
}
```


### [2026-10-15T02:46:05.574Z] TOOL RESULT

```
ocr/FFD:
Permissions Size User   Date Modified Name
.rw-r--r--   72k sfmqrb 14 Oct 22:19  50.png
.rw-r--r--  1.2k sfmqrb 14 Oct 22:19  50.vision.txt
.rw-r--r--   73k sfmqrb 14 Oct 22:19  51.png
.rw-r--r--   831 sfmqrb 14 Oct 22:19  51.vision.txt
.rw-r--r--   61k sfmqrb 14 Oct 22:19  77.png
.rw-r--r--   405 sfmqrb 14 Oct 22:19  77.vision.txt

ocr/SOD:
                                                             9507 strong
                                                                  t»wnc C                                           Uly
       Hen. Tales. 481.35; GMS 1285A; Frag. Len. 35b2              tawanc ©f. adj. -^wnty*
9494 tVy     C -* t)r)k
                                                                   BSTii 891.62: C2, 60V31
9495 tVyck      S =* t>r>k
                                                             9508 t'wnd M «* t>w>nt(t)
9496 t'rymync C                                     JLj;
     tare-menc -^t'r'k                                       9509 t'wndqy* M                                 j^^'y
     dark
                                                                  tawandakya -^t'wnty'
       STii 2.21; GMS 1103                                        power, strength
                                                                  GMS 985; Hen. BSAOS 12, 307.57
9497 t»ryy(h)     M =¥ t>r>k
9498 Vs}6 M                         (OJL~.b «*£)<*/ «=_».    9510 t'wnd/t     M, C ^ t>w>nt(t)
     tasaS ©pp.
                                                             9511 t}wndy(y)     M                           ju^j<Ufy
     tired
                                                                  tawande (tWnty) ©pi. -r ^wnty*
      BBB 714; GMS 1636                                           powerful, strong
                                                                  SCE 10; Hen. Tales. 472.30; BSOAS 12, 307.58;
9499 t's M                                            *>.y
     tas ©Av. taszm-daru                                            GMS 1068, 1641; STii 5.13, 6.16; BSTi 170;
     tablet                                                         Hen. BSOAS 11.702; STSC 133.24; Frag. Len.
     BBB 527                                                        98a 1; MSP b30; BSTii 858.13, 882.5, 827.45: C2

9500 t>s- B, M                                                      gloss. p227; ace. t>wntw, C2, 69 R22
                                           0*~*Ji&u>.
     tas=*ts
           ©<Av. tas; Pahl. tasidam% Khot. ttds              9512 tNvnt C =» t>w>nt(t)
             ycq
                                                             9513 tVnty* C                                  j^^y
      (to)cut                                                     tawandy* (t'w'nty) ^tVndyfy), t}wnc, t}wndqy}
      TSP 2.116, 514, 537, 538; GMS 637; Frag. Len.
        37.7                                                      STii 4.10
                                                                  power
                                                             9514 tV B, M                                     jju. oj>
9501 t*s- M                        ojS i&J'klj loXji
     tas,tes ? =»t}s-, ts-                                        tay
     (ro)cut, 0o)dig                                              thief ©<Av. tayu ©pi. -f; ob. pi. -ty =»t>yh, ty3
     Sund. Man. Lett. 305.19; GMS 637                             TSP 2.1113, 7.138, 24.2; Hen. Tales. 478.2.30,
385

        478.6; Mack. BSOAS 1984, 534                           9528 8b>r C                                            -uja
                                                                                                                   8brt-
9515 ty B, S      • JL*. j& ttsJj*- ^>*jjj -'j <>■**                 OPar ©ob. -y ^Ob^qy*, 8p>r
     tay ©Skt. ayatana ©pi. -t                                       gift, giving
     entrance(/c»r sense organs)                                     C2, 51V28
     TSP 2.1043 etc.; Frag. Len. 103R2; Mack. BSTBL,           9529 8b»r ywz C                           \jf «£ju> jl=J ^
       Notes pl5.15                                                  G^r-xoz
                                                                     asking for alms, beggar
9516 tywny      B, S                           cJ^<^>
                                                                     STi 42.4; GMS 57 n 1, 921; Gersh. Sogd. Cpds.
      tayune, tayoni (t}ywnyy, t}ywny)                                 1945, 144.5
      theft
      TSP 9.15; BBB plOO e 6, GMS 1087; Frag. Len.             9530 BbVqy* C                      ^Sia^ijjl**
```


## [2026-10-15T02:46:10.321Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i \"sēj\\|s[eē]j \\|sēǰ\\|sej\\b\" PHD.txt PHD_mackenzie.txt | head; grep -n -i \"sēč\\|sēj\\|sec\\b.*danger\\|sej\" NYB_vol2_glossary.txt | head; grep -n -i \"sēj\\|sej\\b\\|sēǰ\\|sejomand\\|sēč\" SNS_pages.txt | head"
}
```


### [2026-10-15T02:46:10.864Z] TOOL RESULT

```
PHD.txt:217:arzómand [le wmnd | (N arjumand)] valuable, worthy. ~ih: value, worth. Arzür []zwl] a demon; a mountain at the mouth of hell. a-sag [?s?*k! | M *s?g] innumerable, countless. азап Pon! | N ~] at rest, easy, peaceful. “АП: rest, ease, peace. a-sar Dell endless. āsāy-, ~išn, v. āsūdan. a-sazāģ ["sc? k!] unfitting, unsuitable. a-sazisn|ig Dscfn-yk'] imperishable, permanent. ~ih: imperishability, permanence. a-sēj [Psyc] free from danger.
PHD.txt:564:sang [KYPA < A kyp’; CCA (in error); sng | (P?sng), N ~] stone, rock. -~sar [-s?1] stony place. sanj-, v. saxtan. sanwar [snwl = Av. 0anwar-] bow. sar [LOYŠE < A r'šh; sl | M sr, N ~] head; top, summit; end, begin- ning. | sarāsar [s?s] | N ~] from end to end. sard [s/t! | M srd, N ~] cold. ^Àh: coldness. sardag [sltk' = Av. sarada- | (M s’rg), J srdg] sort, kind. sardsér [s/tsyl | N ~] cold region, uplands. sārēnīdan, sárén- [s’/yn-ytn'] provoke. sargen [slgyn' | N sargin] dung, manure. sarmāģ [s/m?k! | N затта] coldness. sarw [slw(b)' | M srw, N ~] cypress. sas [ss | N ~] bug. sāstār [s”st”7 | P s?s?r] commander; tyrant. ~ih: tyranny. Sawah [sw’h = Av. sawahi-] the western continent of the earth. saxt [sQ)At! | N ~] strong, hard, severe(ly); very. “Аһ: strength, severity. saxtag [shtk! | (N saxtiyán)] morocco leather. saxtan, ѕапј- [s’htn', snc- | N ~] weigh. sāxtan, sáz- [s*htm!, ?c- | (P s?*c-), N ~] make, prepare; tolerate. sāxtārīh [Pht yh] toleration, forbearance. saxwan [МРУА < А mly’; shwn' | М sxwn, N suxan] word, speech. say-, v. südan. sayag [sg dk! | M ғур, N sáya] shade, shadow. lsaz- [sc- | M sz-, N ~] be fitting, proper, worthy. --i$n(ih): fitness, worthiness. 26а2-, —išn, v. sazistan, saz-, v, sáxtan. sazāģ [sk | N sazá] fitting, worthy. ~th: fitness, worthiness. ~ ~war [-w/ | N sazāwār] = затар. sazistan, *saz- [sc-stn'] pass. ~išn: passing, transience. ~iSnig : transient, perishable, mortal. sé [3; TLTA < А tl? | M sh, N si] three. sëb [syf | N ~] apple. sēj [sye = Av. 'Gyejah- | N ~) danger, trouble. --ómand [-”zvmnd | N —mand] dangerous. sel [si | N —] spear, javelin. sém [sym | N —] — asém. !sén(ag) [syn(k)! | N sina] breast, chest. *sén murw [synmzlw | (N simury)] a fabulous bird.
PHD.txt:1487:danger sēj; free from ~ asēj.
PHD.txt:4102:ranj, sēj,
PHD.txt:4788:seb, sej scjomand sezdah sezd sezdén Кага sagen deg, ?sag, sik sar
PHD_mackenzie.txt:4537:seJ [sye = Av. i8yeJah- I N -..] danger, trouble.
PHD_mackenzie.txt:7808:tooth dad, dandan.                       trouble (n.) dus(x)warih, ranJ, sej,
```


## [2026-10-15T02:46:14.794Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} /sye = Av/ {print NR-1}' PHD_mackenzie.txt; grep -n \"syc\\b\\|sēč\\|sec\\b\" NYB_vol2_glossary.txt | head; grep -n \"syc\\|sycwmnd\\|sēč\\|sēj\" SNS_pages.txt | head"
}
```


### [2026-10-15T02:46:15.288Z] TOOL RESULT

```
95
689:a-sēž [’syc'] incorruptible, imperishable 743. — Paz. asčž. V. sēž.
1123:cigon [cygwn] adv. and conj. A. interrog. adv. how? 1. direct interrogation: nun ~ kunom ?] 272; asmān ~? 921; exclama- tory: how...! 614. — 2. indirect inter- rogation: äkäh hom ku ~ hän 571; vēnēt ki Bastvar kārēcār ~ nev kunēt saw how valiantly B. fought 2815-16; ~ 6, 6 ham pursem 57°, andar Garodman dätistän ~, api-m nē dit 527-3; ete. — B. rel. adv. so as: l. har 3 šap x"amn ~ dit Estät ... guft such as he had seen it 2%; 215, 48, 520, 4527, ete.; introducing quotations: ~ den göbet 387, ~... paitāk ku 4571-5, etc. passim; parenthetic, e.g. 7718, 818%; — with a demonstr. antecedent: hamgönak hast ~-am guft 1216-17; šmāh bat ētūn m to gobeh 2329; 4524-25, 782.4, etc. — 2. with- out a clause, used prepositionally: as, as (for instance), as it were, like: ~ agäh aköc martom 2678-27; ~~ martom kë šarm 43913; 12813; varcāvandān i ~ Yam u Frétón ... 45°; hàn 4 ~ én such a th. 438; namely 1078; — with a demonstr. antecedent: &ön ~ āluh-ē 9%; eton ~ to 1516; ét6n but ~ amahraspand-ē 38°”; — čton, or ógón, homänäk (a. v.) ~ 69%, ete.; mänäk(k)äi (g. v.) i õi ~ ke pus... bare (opt.) 418. — C. conj. 1. causal be- cause: ~~... hdn mazantom bit 613-4; 1081. 11812; almost as a rel. pron. with a sec- ondary causal sense (as in Lat. quippe qui): 6 xuähar i x*"e$, ~ zan 4 Artaxsér būt, nämak nipišt 822; 718%, 7916. 116%. 11819; — hac han ~ in view of the fact that, considering that 38. — 2. temporal as soon as: 6°. 15°. 44°, more emphatically ham-~ 1317. - 3. ~ ka as if 11214.17, 10120722 — 4. almost = that 8722. — MPrth cw'gwn; MPrs ewn (read ci'on < *ciwön <
3182:pus [BRH; pws 2218. 2615, 277] son, cas. rect. and cas. obl., passim; secondary cas. obl. pusar [BRH-1] 5115.21.24, 523.9; pl. cas. obl. pusän (BRH-'n'] 188, sec- ondary form pusarän [pwsPn'] in the enumeration apāk pusarān brätarän (ete.) 185, 21°. 241-5. — < OP puca-, SW form of pudra- (v. ‘puhr); MPrs pws (cas. rect.), pwsr (cas. obl.). — pusar is modelled on the pattern of pttar, brätar, mātar, duxtar; NP pus (old), pusar; modern pisar influenced by pidar.
3425:sēž [syc'] distress, embarrassment 3712, 442. 1037. — Borrowed from Av. (799) wyajah-, i0yejah- (i- epenthetic).
```


## [2026-10-15T02:46:18.878Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} /sēž \\[syc/ {print NR-1}' NYB_vol2_glossary.txt; grep -n -i \"seyz\\|sēž\\|sej\\|syc\" SNS.txt | head; grep -n \"pdf page\" SNS_pages.txt | head -2"
}
```


### [2026-10-15T02:46:19.304Z] TOOL RESULT

```
191
```


## [2026-10-15T02:46:22.471Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; head -c 1500 SNS_pages.txt; grep -n \"سیج\" SNS_pages.txt SNS.txt | head; ls ocr/SNS"
}
```


### [2026-10-15T02:46:23.266Z] TOOL RESULT

```
    A
>l»>'i




 O^t'

        /
« *>&
                              Shiraz University Publication




     A GLOSSARY OF
SAYIST NE SAYIST
 A pahlavi persian Glossary
             -




       and Six indexes

         '




                      By

        Mahmood Tavoossi




                 * Z 2 2 7 7 6 O*
U*'^ J^»t ^Sj (jl3T v U». ^jb.1^ ^jjt



 tr-w^-r




                                               DP



                                        c-IAjU-vW^
      ^L-tf-JU- o-*i


          4,
                                                      ,la^
          *j                                                  UmUj
        •*jl                            <,-> * U ***>» atf

       "A*                              ^jU tfU ^>i «/
        •Art                    ^U       c»k>   *   ^         J fr**

      t »**#*                ^u-tfV^j** j-fcX.,^^
,w>
                                                      —
                 'Jt*-



          TTt     fc i   1   u»J*

           «                   b           \        "?
          m                    b         \?
                                                     O
          »tt                   b        \\t
                                                          4




          16T                   b        \tk         1"


          1>1                   b        \&&
                                                     4"
          m                     b        m
          ivr           Permissions Size User   Date Modified Name
.rw-r--r--  1.2k sfmqrb 14 Oct 22:19  6.vision.txt
.rw-r--r--  113k sfmqrb 14 Oct 22:19  11.png
.rw-r--r--  1.2k sfmqrb 14 Oct 22:19  11.vision.txt
.rw-r--r--  1.4k sfmqrb 14 Oct 22:19  14.vision.txt
.rw-r--r--  1.0M sfmqrb 14 Oct 22:19  74.png
.rw-r--r--  1.4k sfmqrb 14 Oct 22:19  74.vision.txt
.rw-r--r--  130k sfmqrb 14 Oct 22:19  282.png
.rw-r--r--  1.1k sfmqrb 14 Oct 22:19  282.vision.txt
.rw-r--r--  411k sfmqrb 14 Oct 22:19  299.png
.rw-r--r--  1.3k sfmqrb 14 Oct 22:19  299.vision.txt
```


## [2026-10-15T02:46:25.141Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 tools/ref_page.py SNS:314 --image 2>&1 | tail -30"
}
```


### [2026-10-15T02:46:25.559Z] TOOL RESULT

```
no scan of SNS covers printed page 314 (see 'scans' in refs_online.json)
```


## [2026-10-15T02:46:28.037Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))['SNS'];print(json.dumps(d,ensure_ascii=False,indent=1))\"; cat data/verification/sources/refs/ocr/SNS/299.vision.txt | head -20"
}
```


### [2026-10-15T02:46:28.498Z] TOOL RESULT

```
{
 "title": "Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1986",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/VajnameShayest",
 "lookup_hint": "grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php search (see BQT) for better hit-to-leaf mapping.",
 "local_file": [
  "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SNS_pages.txt",
  "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SNS.txt"
 ],
 "page_offset": "242 leaves; page offset not determined (OCR too poor to read printed numbers) — locate by transliteration then read the page image",
 "covers_etymology": true,
 "notes": "OCR quality is POOR: Persian text mostly garbage, Latin transliterations partially readable. Verification will usually need the page image."
}
[Tavoosi, Vazhe-name-ye Shayast ne Shayast, printed page 299 (archive.org VajnameShayest leaf n167,
 left-hand page of the spread; the right-hand page carries the printed number ۲۹۸).
 Read from the page image saved as data/verification/sources/refs/ocr/SNS/299.png.]

Entry (verbatim, middle of the left column):

  yākand: یاکند، یاقوت. «یاکند یاقوت باشد، شاکر بخاری گفت:
     کجا تو باشی گردند بی‌خطر خوبان / جمست را چه خطر هر کجا بود یاکند»
  (لغت‌فرس) این واژه اصلاً یونانی: hyakinthos و لاتین: hyacinthus
  به معنی نوعی زهر است، یاقوت معرّب یاکند فارسی است که گوهری زینتی و سرخ‌رنگ
  و درخشان و پربها است. ک۱۶/۲

Two points relevant to Nourai p.193 (pdf 223):
 1. SNS:299 does say the Greek/Latin word means «نوعی زهر» = "a kind of poison" — so Nourai's
    root note reports SNS correctly. (The claim itself is wrong: Gk. ὑάκινθος is a flower.)
 2. SNS:299 says «یاقوت معرّب یاکند فارسی است» = "Arabic yāqūt is the arabicised form of
    Persian yākand" — this is Nourai's authority for the Persian → Arabic arrow.
```


## [2026-10-15T02:46:32.711Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==176' SNS_pages.txt | grep -n -i \"s[eēé]\" | head -30"
}
```


### [2026-10-15T02:46:33.184Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-15T02:46:35.958Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} END{print NR}' SNS_pages.txt; grep -c \"pdf page\" SNS_pages.txt; grep -n -i \"sez\\|sēz\\|s[eē][jžz]omand\\|sejo\\|sez[oō]\" SNS_pages.txt | head"
}
```


### [2026-10-15T02:46:36.616Z] TOOL RESULT

```
242
0
```


## [2026-10-15T02:46:39.028Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for n in 174 175 176; do echo \"== leaf $n\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n+1' SNS_pages.txt | grep -E \"[a-z]{3,}\" | head -15; done"
}
```


### [2026-10-15T02:46:39.488Z] TOOL RESULT

```
== leaf 174
                                           o-^U *.b«jl 5                                                                                        cu_^Uj c-,b «*b *jlj
                                     lij
                                 yezI.syaQais :j^-*S:yezI:                     —?S*                                            •   X/\&'S           tfSt&hn pifrmi         & -yazfim: &0
                                                                                                dSgha-                  L diha- icaSj^m daja-: t-
                                                   .o-i-fo :Iast, 60:                 <J 3                                                                   tv/ta^* -{GNPE 117)           cin:
                      (Jackson. 106) sastl-              :    *-   xsvasti-:    fc-
                                                                                                        (o*** !*&       gac:                        ;>*      ^^— c-i-j^^f igacSn:
                •A1/1T^ .^jo-A.ff:                sast ud sas, 66:_^>*M>»
                                                                                                              •*/i£3<"»/iAf(|3 :yast:                           yZBHWN, t       :   >*:        V^if*
f/T^. EUJo T v^- (GAPE. 132) dfpyatS, /dlp-ti^tf-**
                                                                                                (        yeyv :*£:) >AAiV*«iAh tyaziln:                                     P Insj»:          go^ii*
    .{Henning, JBAS 1942, p.                       235             :&)<&** 'vWj
          f/lf^ (AiWb. 748)distay-: ^t5-*iB disti- ttm    i
                                                                                               fMU^J^.jlli^^^.Ai,,^ :yaz5n:                                                   ,m:>»       :   -6>£j5j
                             •^A-     (ojjj -^)^: sag:
== leaf 175
                                                                                                        -iiiS'l^.1^^,^ ,             4^ ^jfauS Ijfl'ob^ :yastar3n:                              *•*-*» itJO*
                                                                      .^:yak:                3j                                                                                            til
                                                                                                                                     •>** o ^-* dastan: •   1         :                             *f    >Oo J
                                                                                                                   •   lA^f-M-.VY-4/T'*  U*JK>. 676) daxlta-                                        :   £.
.*/Yl^     .,/«(    :yak-5:        -»-»3l>   (*^.i)A-*/Y^ (**<***>)
                   .*,/•<)£       {^h              yak:                           -*£_>"
                                                                    .jSV:jagar;              ia>                                                                                           W>
                                                                                                            (jO'JIj         '•**»)     ^^'fiMJJ                     isU,       dastan:           »*-*>o->
£kto.l282)yakrt               :    ^j^- ySkara -/ySkar-                           :    fc-
-.oibjl^^t^l :5stad: yK^MNN-^t                                  :   >•:           V^"^ ^     1
                                                                                                       j=jjj *;U- Jo"^>fc*. a£ lJl»*. .^U_*;Lij             :dastanistan:                 it^ioju t^iouJ
      .^L.-jli^ljgstadag:                               ,   tk:>*:            JW^nrti^j                                                                                                     •YA/Y^
ituoW^^'^vTsab 1 6stadag:Jt«rtivtr»A> »mJ*                                                             ^j^^u-U^o^^ .jU-^y <4*l> c^ :yast jaraag:                                            J_eu          >e>u*
u£J>«J     -u^-J^-.) j*u*l(i):SstSnd:                       ._..,   nd:!^ :           sym;\ju
                                                                                                                                                       -*/^U.o^ ryastan:                            »i«o*          ,   A
== leaf 176
                                                                                                                                           li:      e—^b *.bfljt3
                                       ^^4.tQ'j                                                                                                                                                             xma
                                                                     xer                                                            .   .ii-J       :ested:..              -.,yt: >»:            ^fcfcJJU
                                                                                                                                                •   ra-n-rv-i t-a/r^                  loo-ay-u
                                                                                            U/T*5 ij^jlji           '^ ;abaz.                            SstSd:            \0)vt»JJ         Ju*t-i
                                                                                        ,ff /X*S       Ai-rfljl^     -»>i   aiji»:abaz SstSd:                              >oi\#j*j        ^-o^O
                                                                                        .       jj^jljiajliiwl Jj^candar                  kar ested:                       y" »****»*» v?
                                                       Ijljj-.drahnaty) :
                                                                            ~" v   "*       .   o>i Jjii* jK a- :andar                  3 kar Sstfid: >a»irf>J* \^3 1)                               &
                                                                               ^                                                                     .   ^ pak DKy
                                                   t   T/   ,^ .«/T^ -UA-lol
                               \   .   *a   -.-a. . ^-,15;qrantar:
                                                                            V^                       \A/r^        .^yf^L,^^ rpakih:
                           *v. *w •**-«*-                                                                                                                .AJj/.i/ftJi ,*£ ./:gar:                           Jj
                                                                                        IY/V14        (4iJ/fc. Ill, 513-14) giray-offSj-^                                         gairi-: £»                      Xo
```


## [2026-10-15T02:46:44.623Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} {n=NR-1; if (match($0,/:s[eēéë3S5][jzžiJ][^a-z]/)) print n\": \"substr($0,RSTART-80,160)}' SNS_pages.txt | head -20"
}
```


### [2026-10-15T02:46:44.960Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-15T02:46:47.998Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -o \".\\{60\\}:s[a-zA-Z0-9]\\{1,6\\}:.\\{60\\}\" SNS_pages.txt | awk -F: '{print $1}' | head -3; awk 'BEGIN{RS=\"\\f\"} {n=NR-1; c=gsub(/:s[a-zA-Z35]{1,5}:/,\"&\"); if(c>2) print n, c}' SNS_pages.txt | head -40"
}
```


### [2026-10-15T02:46:48.378Z] TOOL RESULT

```
7256
7405
12371
103 5
108 3
```


## [2026-10-15T02:46:51.118Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for n in 101 102 103 104 105 106 107 108; do echo \"== leaf $n\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n+1' SNS_pages.txt | grep -o \":[a-zA-Z35ē]\\{2,10\\}:\" | head -12 | tr '\\n' ' '; echo; done"
}
```


### [2026-10-15T02:46:51.923Z] TOOL RESULT

```
== leaf 101
:ziyan: :zin: :zlvad: 
== leaf 102
:sig3nag: :s3xt: :sSxtag: 
== leaf 103
:sast5r: :spas: :sar: :salag: :saligSn: :s3rlgar: :s5yag: 
== leaf 104
:spitaman: :spurz: :stayidar: :stahmbag: 
== leaf 105
:star: :stahraag: :st5yisn: 
== leaf 106
:stotgar: :st5r: :stur: 
== leaf 107
:53: :d5r: :glrand: 
== leaf 108
:sros: :srQv: :srudan:
```


## [2026-10-15T02:46:58.023Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/p509; for n in 107 175; do curl -sL -o sns$n-509.jpg \"https://archive.org/download/VajnameShayest/page/n${n}_w1200.jpg\"; done; ls -la; file *.jpg"
}
```


### [2026-10-15T02:47:02.426Z] TOOL RESULT

```
sns107-509.jpg: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, baseline, precision 8, 1094x804, components 1
sns175-509.jpg: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, baseline, precision 8, 1079x804, components 1
```


## [2026-10-15T02:47:04.821Z] TOOL CALL #40: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/p509/sns175-509.jpg"
}
```


### [2026-10-15T02:47:04.932Z] TOOL RESULT

```

```


## [2026-10-15T02:47:11.887Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/p509; curl -sL -o sns174-509.jpg \"https://archive.org/download/VajnameShayest/page/n174_w1600.jpg\"; file sns174-509.jpg"
}
```


### [2026-10-15T02:47:13.253Z] TOOL RESULT

```
sns174-509.jpg: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, baseline, precision 8, 1094x804, components 1
```


## [2026-10-15T02:47:15.631Z] TOOL CALL #42: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/p509/sns174-509.jpg"
}
```


### [2026-10-15T02:47:15.657Z] TOOL RESULT

```

```


## [2026-10-15T02:47:25.547Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 tools/ref_page.py BQT:1202 2>&1 | grep -n -B2 -A8 \"سیج\" | head -60"
}
```


### [2026-10-15T02:47:26.023Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-15T02:47:27.893Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 tools/ref_page.py BQT:1202 --image 2>&1 | head -60"
}
```


### [2026-10-15T02:47:28.325Z] TOOL RESULT

```
no scan of BQT covers printed page 1202 (see 'scans' in refs_online.json)
```


## [2026-10-15T02:47:30.794Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"سیج\" BQT_v2_pages.txt incoming/BQT/BQT_v3_pages.txt | head; python3 -c \"\nimport json;d=json.load(open('../refs_online.json'))['BQT'];print(json.dumps(d,ensure_ascii=False,indent=1)[:3000])\""
}
```


### [2026-10-15T02:47:31.489Z] TOOL RESULT

```
incoming/BQT/BQT_v3_pages.txt:2777:کلپایگان ‎OT petty‏ سبجه«ضی» وسیجه *ابن دربد» .
incoming/BQT/BQT_v3_pages.txt:10744:‏مجلس نزهت بسیج وچپرژ معشوق بن
incoming/BQT/BQT_v3_pages.txt:28082:دمسیجه (۳) بيز گوبند . برلب آب نشیند ودم
incoming/BQT/BQT_v3_pages.txt:38923:‎leas - ٩‏ فاخ رکرده روان زهرسو ‏ ۰ ‎e‏ وسیج و کمخا , ک و کوز وسای ساده.
BQT_v2_pages.txt:17154:  ‫کاری گفتن » یا پس انداختن‌کار » « سبك شناسیج ‪ ۲‬ص ‪ * 6۱۲‬ونيز بمعنی چشم پوشیدن‪,‬بدور‬
BQT_v2_pages.txt:32261: ‫سیج = بفتح اول والی و سکون جیم »‬                  ‫و بکاف زده » بمعنی کبوتر امت و بعریی حمام‬
BQT_v2_pages.txt:40149: ‫» یمعنی‬    ‫بروزن چهد ود‌ن‬    ‫‌‬   ‫‪۸‬‬   ‫سیجیدن‬               ‫ه با فوقانی بواو کشیده‬         ‫وی‬
BQT_v2_pages.txt:40166:                                             ‫بمشی قسیب كوچك» ‪ .‬رك ‪ :‬داثرةالمعارف اسلام ‪ :‬سیجوبهی‪.‬‬
BQT_v2_pages.txt:40167:    ‫‪ - ۴‬سیجمند بمعتی دارنده رنج ‪۰‬‬                  ‫‪ ( 600۵5‬فر ) « لك ‪ ۲‬ص ‪۱۱۳٩‬‏ ‪.‬‬          ‫‪= ۴‬‬
BQT_v2_pages.txt:40189:   ‫_ ‪ 085620‬از ‪٩ 212025120 -‬‏ کوید ل‪:‬ازم است بادآور شوبم که « سیجیدن » ازنحلیل غلط‬
{
 "title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)",
 "kind": "archive_djvu+local_scan_ocr",
 "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.com (links from farhangoadabeirani.blogsky.com post-482): vol 3 https://s3.picofile.com/file/8230740968/borhane_ghatee_jelde_3.pdf.html (ش–ل, Ibn Sina 2nd ed. 1342, 721 pp), vol 4 https://s6.picofile.com/file/8230741184/borhane_ghatee_jelde_4.pdf.html (م–ی, 553 pp), vol 5 https://s3.picofile.com/file/8230741300/borhane_ghatee_jelde_5.pdf.html (تعلیقات, Amir Kabir 5th pr. 1376, 293 pp). Same set behind login on ketabnak.com/book/55304-55307 and /58249.",
 "lookup_hint": "grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \\f; leaf N = N-th \\f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=dehkhoda, parsi.wiki, abadis.ir/fatofa/<word>/) quotes Borhan and often Mo'in's footnotes as (حاشیهٔ برهان قاطع چ معین). noorlib.ir/book/info/10294 is a 1-vol Nima 1380 Borhan without Mo'in's notes. | For pages in a scanned volume use: python3 tools/ref_page.py BQT:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)",
 "local_file": [
  "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v1_pages.txt",
  "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v2_pages.txt",
  "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)",
  "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v2.txt (raw)",
  "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf",
  "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt",
  "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt",
  "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf",
  "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt",
```


## [2026-10-15T02:47:33.652Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} /سیجمند بمعتی/ {print NR-1}' BQT_v2_pages.txt; sed -n 40140,40195p BQT_v2_pages.txt"
}
```


### [2026-10-15T02:47:34.458Z] TOOL RESULT

```
666
                                                                                             ‫با‬
‫سیحقنه ‪ - ۷‬با اول بثالی رسیده وضم‬                                                            ‫عربی است ‪۰‬‬
 ‫جيم فارسی" وفتح غین لشقطه‌دار (‪ )۲‬ونون ؛یمعنی‬             ‫بای ابجد (‪ )۱‬بر وزن‬     ‫سیییا ه بکر‬
 ‫باشه باشد » وآن یرلده‌امت شکاری ازجنس‌زرد‬                 ‫سرباای نوعی از ماهی باشد ‪۴‬‬        ‫لغ»ت‬
                                                                                                ‫بمیا‬
                                                                                                   ‫کی‬
‫وبمعنی صعوه هم‌آهده است ؛ و بفتح‬            ‫چشم ‪- ۷‬‬        ‫در لاحیةٌ بیت‌المقدس و در بعضی ازسواحل‌مفرب‬
                              ‫م فارسی همگفته‌اند ‪.‬‬
                                                 ‫یم‬‫جی‬                                        ‫یز مت‪.‬‬
 ‫» یمعنی‬    ‫بروزن چهد ود‌ن‬    ‫‌‬   ‫‪۸‬‬   ‫سیجیدن‬               ‫ه با فوقانی بواو کشیده‬         ‫وی‬
                                                                                           ‫سی‬
                                           ‫قطه دار ‪.‬‬     ‫(‪ )۲‬چك‪-:‬‬             ‫(‪ )۱‬چك ‪ :‬بکریا‪.‬‬

    ‫ا‪-‬بوبشر عمرو بن عثمان بن فنبره (با) أبن قنبر فارسی بیضاوی وسپی عرأفی بصری‬
    ‫سیبویه»‬      ‫ا«ب‬
                   ‫ت‪.‬و‬
                     ‫ک‪ ۶‬ه‬
                        ‫بال ‪ ۲۹۱‬وبقولی ‪۸۱‬‬               ‫تزووفی‬
                                                             ‫مرا‬
                                                               ‫متولد دریضاء ازقرای شی‬           ‫ی‬
                                  ‫مشپور به«الکتاب »> درتحو آزوست ‪ ۶‬ممجم المطبوعات ج‪ ۱‬ستون *‪.۷۶۱‬‬
    ‫منه‬     ‫‪۴‬‏ ‪١ -‬سيبوبه لفقابرسی » معناه بالعريية رائحة الفاح و فيل كیانشم‬
   ‫اما‬      ‫رائحة‌الطب بذلك سمی‪ .‬وقیل‪ .‬كان بعتادشم الفاح ‪٩‬‏ « ممجم المطبوعات ح ‪ ۲‬ستون ‪۰۷۰۱۰‬‬
   ‫قلبول نداردو کوید ‪ :‬رهکز این‌ککمه را بداب“ مشدد تلفظ نکرده‌اند‬   ‫‪ ۴.‬اریناقو‬     ‫‪7‬‬
      ‫ش‪8‬د‬ ‫‪0۰ ۶‬‬‫بدا‬‫و پیب مشابپت این نامباعد بسیار از ناءهای ابرالی قدیم ‪ ,‬هجای آخرکلمه باب‬
    ‫وبنابراین باحتمال اقوی موان کت که لفط کلمه ‪ 66588‬ات وآن اصطلاحی محبت آمیز بود‬
                                             ‫بمشی قسیب كوچك» ‪ .‬رك ‪ :‬داثرةالمعارف اسلام ‪ :‬سیجوبهی‪.‬‬
    ‫‪ - ۴‬سیجمند بمعتی دارنده رنج ‪۰‬‬                  ‫‪ ( 600۵5‬فر ) « لك ‪ ۲‬ص ‪۱۱۳٩‬‏ ‪.‬‬          ‫‪= ۴‬‬
                                                                                    ‫‪:‬‬    ‫نوت‬‫حنج‬
                                                                                              ‫مل ر‬
                                                                                                 ‫مح‬
                    ‫که او را پیشه باشد بیوفائی‪.‬‬                     ‫جهان سدجه‌ند ویر انائی‬
         ‫‪۵‬ا*ص‪.‬‬
             ‫زرتشت بهرام «ار‪.‬داوبر افنامه چاپ جاماس اس‬
    ‫‪ - ۱‬فرهنگه نظام بنقل از فرهنکه ت رکی اطفری‬                            ‫‪.‬‬      ‫جكی‪:‬دن‬
                                                                                      ‫س ر‬
                                                                                        ‫‪۵‬‬
                                                       ‫«سجیلفنه» را بمعنی کلنکه آورده کهشکاری نیست‪.‬‬
                ‫از دبدة صحفنه کند دانه مهیا‪.‬‬              ‫ادره عدلی که زاصاف نو نبهو‬     ‫ای‬
                                                                                          ‫‪۷‬‬
         ‫ع«میجد لهوباکنیگ‪.‬یری»‪.‬‬
    ‫؛ بهلوی ‪natîcês‬‏‬          ‫مسدری )‬       ‫ند‬
                                             ‫پنو(‬
                                                ‫=یج ‪ +‬بد‬
                                                       ‫‪۸‬یتچیمدد‪1‬ن از س‪:‬يج س‬
                                                                          ‫س‬
    ‫‪, 6 6*50‬‬
           ‫«وادیا ‪ ۵۹۱4۰‬استاد هئینکه پس از کر « پسیچیدن » و ارتباط آن بساغدی _‬
                                                                             ‫تا‬
   ‫_ ‪ 085620‬از ‪٩ 212025120 -‬‏ کوید ل‪:‬ازم است بادآور شوبم که « سیجیدن » ازنحلیل غلط‬
                                      ‫تلفط خطای سیچ ‪cêsib -‬‏ ناشی شده و درحقیفت وجود نداشته است‬
    ‫‏‪Henning , Sogdian loan - words...,BSOS.,X.1,p.104.‬‬
  ‫ی‬                                                                                                ‫ات‪۷‬‬
                                                                                                     ‫‪۳۵‬‬

‫سیخگاه یافقن ‪ -‬مراد از آست که‬                                 ‫مهيا ساختن وترئیب دادن کاری باشد ‪.‬‬
```


## [2026-10-15T02:47:38.859Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} /سیج = بفتح اول/ {print NR-1}' BQT_v2_pages.txt; sed -n 32255,32270p BQT_v2_pages.txt; awk 'BEGIN{RS=\"\\f\"} NR==667' BQT_v2_pages.txt | grep -n \"سیج\\|رنج\\|درد\" | head"
}
```


### [2026-10-15T02:47:39.963Z] TOOL RESULT

```
542
  ‫سباع = بکر اول بروزن چراغ؛بمنی‬                   ‫وآن‌سنگی است معروف که‬             ‫ستیادهاست»‬   ‫مخفف‬


         ‫نایخورش است و معرب آن صباغ باشد‪.‬‬           ‫ازآن فان سازند وحکاکان‌نگین ادگشتری‌وامثال‬
  ‫سبایل = بر وزن فبایل > دارالملك‬
                           ‫قندهار رگاوشد ‪.‬‬
 ‫سیج = بفتح اول والی و سکون جیم »‬                  ‫و بکاف زده » بمعنی کبوتر امت و بعریی حمام‬
                                                                                                  ‫خواشد‬
‫معرب شبه است ‪ , ۸‬وآن سنکی باشدسیامو لرم‬
 ‫که ازآن نگن انگکسی وچیزهای‌دیگرساز ند‪.‬‬           ‫سیاری = یک اول بروزن شکاری » ‪.‬‬

       ‫ره(‪۳‬دارنده) رك ‪ :‬سابه‪. ‎‬‬
                              ‫از‪:‬دسااب‬        ‫‪۴‬‬          ‫‪ = ١‬لاال «تایتی‪. ٩۸٩ ‎‬‬
                       ‫رك ‪ :‬سابه ‪.‬‬    ‫‪۴‬‬           ‫‪ - ۴‬چه میکن‪۲‬تند ‪ :‬السلطان لل ا‪/‬له ‪.‬‬
     ‫زمینی یمن «وشهر آن «مارب» وبین‌آن وه‌عاو سه روزه راه بود‪«.‬مصجم‌البلدان»‬              ‫‏‪e‬‬

7: ‫و بکسر اول پمعنی رنج و محنت و مشقت ‪- ۴‬‬                    ‫‪.‬وبند چون هردورخارة‬
21: ‫» یمعنی‬    ‫بروزن چهد ود‌ن‬    ‫‌‬   ‫‪۸‬‬   ‫سیجیدن‬               ‫ه با فوقانی بواو کشیده‬         ‫وی‬
38:                                             ‫بمشی قسیب كوچك» ‪ .‬رك ‪ :‬داثرةالمعارف اسلام ‪ :‬سیجوبهی‪.‬‬
39:    ‫‪ - ۴‬سیجمند بمعتی دارنده رنج ‪۰‬‬                  ‫‪ ( 600۵5‬فر ) « لك ‪ ۲‬ص ‪۱۱۳٩‬‏ ‪.‬‬          ‫‪= ۴‬‬
61:   ‫_ ‪ 085620‬از ‪٩ 212025120 -‬‏ کوید ل‪:‬ازم است بادآور شوبم که « سیجیدن » ازنحلیل غلط‬
```


## [2026-10-15T02:47:44.060Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/p509; curl -sL -o bqt666-509.jpg \"https://archive.org/download/borhan-ghate-v2/page/n666_w1400.jpg\"; file bqt666-509.jpg"
}
```


### [2026-10-15T02:47:46.051Z] TOOL RESULT

```
bqt666-509.jpg: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, baseline, precision 8, 2569x3970, components 1
```


## [2026-10-15T02:47:49.398Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/p509; python3 -c \"\nfrom PIL import Image\nim=Image.open('bqt666-509.jpg'); w,h=im.size\nim.crop((0,0,w,int(h*0.5))).resize((int(w*0.55),int(h*0.5*0.55))).save('bqt666top-509.png')\nim.crop((0,int(h*0.5),w,h)).resize((int(w*0.55),int(h*0.5*0.55))).save('bqt666bot-509.png')\n\""
}
```


### [2026-10-15T02:47:49.892Z] TOOL RESULT

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 2, in <module>
    from PIL import Image
ModuleNotFoundError: No module named 'PIL'
```


## [2026-10-15T02:47:52.883Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/p509; which magick convert vips 2>/dev/null; magick bqt666-509.jpg -crop 2569x1985+0+0 -resize 60% bqt666top-509.png && magick bqt666-509.jpg -crop 2569x1985+0+1985 -resize 60% bqt666bot-509.png; ls"
}
```


### [2026-10-15T02:47:54.456Z] TOOL RESULT

```
/usr/bin/magick
/usr/bin/convert
/usr/bin/vips
```


## [2026-10-15T02:47:56.754Z] TOOL CALL #51: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/p509/bqt666top-509.png"
}
```


### [2026-10-15T02:47:56.773Z] TOOL RESULT

```

```


## [2026-10-15T02:47:58.290Z] AGENT

Page 1202 confirmed. Now the footnote 4.


## [2026-10-15T02:47:59.353Z] TOOL CALL #52: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/p509/bqt666bot-509.png"
}
```


### [2026-10-15T02:47:59.383Z] TOOL RESULT

```

```


## [2026-10-15T02:48:02.840Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr; cat FFD/51.vision.txt; ls BQT | grep 1202"
}
```


### [2026-10-15T02:48:03.254Z] TOOL RESULT

```
FFD (Abolghasemi, Fe'l-hā-ye Fārsi-ye Dari), printed p. 51 = PDF page 56, read from the page image
(pdftoppm -f 56 of FFD_asmaneketab.pdf), section «خواستن»:

خواستن
خواست ← فارسی میانه xwāst ← ایرانی باستان *xwās-ta. برای ta ← آراست. xwād صورت اصلی
xwās است، d پیش از t به s بدل شده است. xwād به معنی «خواستن» است.
خواه ← فارسی میانه xwāh ← ایرانی باستان *xwād-a. برای a ← آرای.

(immediately above, same page:)
خند ← فارسی میانه xand ← ایرانی باستان *xand. xand در فارسی میانه و ایرانی باستان «خندیدن» معنی می‌دهد.

Used for: page 489 (book p. 459), root Swâd, node #1 (Avestan xwâs, xwâd 'to desire').
```


## [2026-10-15T02:48:15.451Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr; S=/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/p509; cp $S/ffd51-509.png FFD/46.png; cp $S/bqt666-509.jpg BQT/1202.jpg; mkdir -p SNS; cp $S/sns174-509.jpg SNS/312-313.jpg; cp $S/sns175-509.jpg SNS/316-317.jpg\ncat > FFD/46.vision.txt <<'EOF'\nFFD (Abolghasemi, Fe'l-hā-ye Fārsi-ye Dari), printed p. 46 = PDF page 51 of FFD_asmaneketab.pdf, read from the page image\n(pdftoppm -f 51 -l 51 -r 200), section «تراشیدن»:\n\nتراشیدن\n«تراشید» مادهٔ ماضی جعلی است، از مادهٔ مضارع ساخته شده است.\nتراش ← پهلوی اشکانی trāš ← ایرانی باستان *trāš-a. برای a ← آرای. trāš صورت\nبالاندهٔ ریشهٔ traš است. traš و trāš هر دو «بریدن» معنی می‌دهند.\n\n(same page, above: تافتن / تاب; below: ترسیدن, تفتن)\n\nUsed for: page 509 (book p. 479), root Tex/Teks, nodes #6 (Avestan traš, trâš) and #7 (Persian tarâšîdan).\nNote: Abolghasemi labels traš/trāš \"Old Iranian\" (ایرانی باستان) and the intermediate form Parthian, not Avestan.\nEOF\ncat > BQT/1202.vision.txt <<'EOF'\nBorhan-e Qate' ed. Mo'in, vol. 2, printed p. 1202 (archive.org borhan-ghate-v2 leaf n666), read from the page image\n(saved as BQT/1202.jpg). Headword column (left):\n\nسیج - بفتح اول وسکون ثانی و جیم، بمعنی مویز است که انگور خشک شده باشد - و بکسر اول بمعنی رنج و محنت و مشقت ۴ -\nو باجیم فارسی هم باین معنی وهم بمعنی ترتیب دادن و ساز کردن ومهیا ساختن‌کاری باشد ۵ .\n\nFootnote 4 (Mo'in):\n۴ - سیجمند بمعنی دارندهٔ رنج، محل رنج و محنت :\n   جهان سیجمند و پر انائی        که او را پیشه باشد بیوفائی.\nزرتشت بهرام. «ارداویرافنامه چاپ جاماسب اسا ص ۵».\nFootnote 5: رك : سیچیدن.\nFootnote 8 (s.v. سیچیدن): سیچیدن از : سیچ + یدن ؛ پهلوی sêcîtan ... Henning ... «سیچیدن» از تحلیل غلط تلفظ خطای بسیچ bisêc ناشی شده (Henning, Sogdian loan-words, BSOS X.1 p.104).\n\nUsed for: page 509 (book p. 479), root Tiegu, node #3 (Persian sîj, سیجمند). Mo'in gives the meaning and the\nArdā Wirāz-nāma verse quoted by Nourai, but no Pahlavi/Avestan etymology for سیج itself.\nEOF\nls FFD BQT | tail -5"
}
```


### [2026-10-15T02:48:15.940Z] TOOL RESULT

```
.rw-r--r--  3.6k sfmqrb 14 Oct 22:19  2420.txt
.rw-r--r--  2.0k sfmqrb 14 Oct 22:19  2420.vision.txt
.rw-r--r--  154k sfmqrb 14 Oct 22:19  2427.png
.rw-r--r--  3.4k sfmqrb 14 Oct 22:19  2427.txt
.rw-r--r--  1.8k sfmqrb 14 Oct 22:19  2427.vision.txt
```


## [2026-10-15T02:48:20.301Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i \"tesa\\b\\|teśa\\|tēša\\|tlša\\|tesah\\|tisa\\b\\|taxta\\b\\|taxt \\|tast\\b\\|tašt\\|tas\\b\\|tasidan\\|tarāš\\|tarasidan\" HRN.txt | head -30"
}
```


## [2026-10-15T02:48:21.610Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i \"tesa\\b\\|tēša\\|tēšah\\|taxta\\b\\|tašt\\b\\|tast\\b\\|tās\\b\\|tarāš\\|tarašidan\" HUB.txt | head -20; grep -n \"taxtag\\|tašt\\b\\|tēšag\\|tāšīdan\\|tašīdan\" PHD_mackenzie.txt | head"
}
```


### [2026-10-15T02:48:22.178Z] TOOL RESULT

```
524:r aw. atars; phlv. ätas (geschrieben 'k^Tinx).
2069:aw. vltasti- 'Spanne'; phlv. v(i)tast; skr. vitasti-
2727:patas/ani 'Antwort*.
3369:ganz unsicher sei: yt. 12, 3 habe Geldner paitisa gedruckt, yt. 5, 62
3370:sei mit Fl Pt 1 P 13 ebenfalls paitisa zu lesen (die überschüssige
3371:Silbe besagt nichts); es bleibe also nur yt. 3, 4. Er fasst paitisa als
3462:afy. tast\edal, tasal bezw. taxt\edal, ta/al 'fliehen,
3654:aw. tasta^ Schaale, Tasse'; phlv. tast, arm. LW.
3656:afy. LW. tust, bei. LW. ^äs (270), aus arab. tas^);
3671:*) Hieraus auch arm. tas, ital. tazza, franz. lasse, nhd. Tasse
4550:ai. svdtas,
4682:daöäiti); phlv. ddt, dätastän, arm. LW. dat, datastan^
5442:') Aus *ral (Trunipp, Graramar of the Tastö § 7); //är,
5577:sr6tas- 'Strömung, Strombett, Strom, Fluss'.
7310:(vergl. Geldner, »5 Yasht, 77) ; lit. kopustas 'Kohlkopf,
7356:{ätas).
7406:karkatas 'Geier scheint nach aw. kahrkatas- repristinirt
9620:herpatastän, herputlh bezw. erpat,
11101:aw. \/^taS' 'zimmern*; ai. [/^tak^-, tdksati 'zurecht
14732:(kiteSa- 880 u Anm.
14939:paitisa 356 Anm.
22927:kopustas 840W9.
```


### [2026-10-15T02:48:22.194Z] TOOL RESULT

```
995:phi. vitast, bistar ■= g. vistara und unten Nr. 786.
8420:*Beir = zd. ^cisa-, arm. tasem 'behaue'; tast 'Becken' = zd.
6070:benevolence hu~asmih, humanih.              board taxtag.
7251: perfume boyenidan.                         planll taxtag.
7741: tablet taxtag.                           then i, did, eg, had, pas.
8262:                        _.~ ,,~      taxtag
```


## [2026-10-15T02:48:25.432Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 3645,3675p HRN.txt; sed -n 11090,11110p HRN.txt; sed -n 8410,8425p HUB.txt; awk 'BEGIN{RS=\"\\f\"} /aw. tasta\\^ Schaale/ {print \"HRN leaf\",NR-1} /\\/\\^taS. .zimmern/ {print \"HRN leaf2\", NR-1}' HRN.txt"
}
```


### [2026-10-15T02:48:25.919Z] TOOL RESULT

```
(AM. 40 Zeile 10), INDOnJl^^^D 'Wüste (Is. 13, 21).
g. tasne,
aw. tarsna- 'Durst*; phlv. tisn , tisnak, tisncfklh;
ai. tfsna-; arm. vergl. farsamim welken', anfarsam
nicht verwelkend* (H. No. 111).
kurd. ti, tmi; afy. tami; bei. tminacj, tünag, n. ftmi
'durstig, fun 'Durst' (396); wa/. tax, ^^'/^j sar. tür^
tiirt, si/n. täsna, täsnagl, yidg. triisna.
389. fest 'Becken, Untertasse*, teste, arab. LW. ^as^
aw. tasta^ Schaale, Tasse'; phlv. tast, arm. LW.
tust, tastak,
afy. LW. tust, bei. LW. ^äs (270), aus arab. tas^);
§i/n. sar. tödö (^tastaka-),
390. fü/ 'Speichel*, tufek{'% dehen)^ tiifke (Gazoph. s. v.
saliva), tufü, tuh, tuhü,
ai. i/^sthlv-, sthivati (vergl. Bartholomae, Ar.Forsch.
III, 34; Studien II, 42); got. speivan; arm. tüiß 'Speichel';
lat. spuö; gr. nzvo).
kurd. tef 'Speichel', tiw, tuw^ tu, tiik 'Spucken,
Speichel*; afy. tu, tük, tükal spucken*; oss. ft* (251);
wa;^. tuf cerak, sar. tu ceigao 'spucken'.
891. tek 'schnell, Lauf, tekiden, tekT,
aw. taka^ 'Lauf "'^) ; zu V^tak-, tac- wie ta/ten (No. 368).
(Metr. Hezej)
juz medh-^ fU terhencU büved Iierci nüvesem
her dem qel^i ez yäfe ü terkende sUceste Sözenl.
*) Hieraus auch arm. tas, ital. tazza, franz. lasse, nhd. Tasse
(Hübsohmann, ZDMG. 35, 129).
') Ap. takabara- etwa wie assahara- durch *auf schneUen (sc.
Rossen) reitend' zu erklären, verbietet die assyrische Version, über
welche mir Prof. Jensen freundlich das Folgende mitteilt:
aw. tanupereSa- bezw. unäpere&a',
np. tenäfür erscheint nur in Pärsenschriften.
198. tarnian{i)su 'hochmütig , tarman(i)imh (Men., Bund.),
vergl. Tarmat (Bund.).
aw. tarö.maiti' 'Hochmut'.
199. Uirvtnltan 'tiberwinden , peinigen (AW.-Komm.,
Bund.).
aw. l^tarv-, taurvay^iti 'überwinden; ai. [/^tffrv-,
türvati 'besiegen'.
200. tästtan bezw. ta/sUan 'zimmern (AW.-Komm., Men.),
tOäUär bezw. tayßUä/r,
aw. \/^taS' 'zimmern*; ai. [/^tak^-, tdksati 'zurecht
richten, behauen'; lit. taszaü^ taszyti; ksl. tesq, tesati
'behauen.
ap. hamata/saiyy hamata/satä stellt Bartholomae,
Studien II, 22 Anm. 1 zu V^tvaks-,— 295 —
u.
201. urvav 'Pflanze.
aw. urvard- 'Pflanze*; ai. urodrä- 'Fruchtland.
Kommt neupersi«ch nur in Pärsenschriften (z. B.
Sed der) vor.
das Verhaltniss von zd. fstdna- zu np. pistan 'Brust', siehe
oben p. 41.
§ 128. Idg. pk^ —^ zd. fs -^- arm. np. s im Anlaut:
subcLn 'Hirt' = zd. "^fsupCLna-, arm. spet *Hirt' = zd.
*fsupaiti' von zd. fsu- 'Vieh' in Kompos. (= idg. ph^u-) ^=
selbstandigem pasu- (idg. pek^u-).
M Vgl. tran»oxanisch ixseS bei N o 1 d e k e , mand. Gram. Einl. p.l3.— 236 —
§ 129. Idg. kh = iran. ap. s = np. s:
kas 'AchselhQhle' = zd. kasa-, skr. kaksa-: sas *sechs'
zd. xsvaSf idg. svek^s ; s^wa *Kamm* = gr. xra^ ; ^'^^
*Beir = zd. ^cisa-, arm. tasem 'behaue'; tast 'Becken' = zd.
tasta- ; neS 'Spitze, Stachel', nestar *Lanzette*, skr. neksana- ;
casm 'Auge* = zd. dasman-, skr. caksus ; arm. LW. sahapet
'Schutzgeist* (5. Jhd.) = zd. soid-rapaiti- ; sen *Dorf * =
zd. -say ana, Wrzl. k^si wohnen'.
Dazu auch as 'Bruhe' H. 29, Osam *Trank' H. 30,
HRN leaf 108
HRN leaf2 315
```


## [2026-10-15T02:48:31.948Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} /tasem .behaue/ {print \"HUB leaf\",NR-1}' HUB.txt; grep -n -i \"tax ta\\b\\|taxta\\|taxt\\b\" HRN.txt | head; grep -n -i \"^ *taxtag\\|taxtag \\[\" PHD_mackenzie.txt | head -3; grep -n -i \"taxtak\\|tašt\\b\\|tast\\b\\|tēšak\\|tašitan\\|tāšītan\" NYB_vol2_glossary.txt | head"
}
```


### [2026-10-15T02:48:32.396Z] TOOL RESULT

```
HUB leaf 246
3462:afy. tast\edal, tasal bezw. taxt\edal, ta/al 'fliehen,
2726:nikčrai [nkyl’y] he who denies his respon- sibility for a th. (whether he has assumed this responsibility by himself, or it rests upon him for other reasons), breaker of an engagement or an obligation 8213, — A juridical term, opp. xtastük ‘he who acknowledges such responsibility’, v. Bthl, ZsR II, 37-40. Cf BdA p. 184!?sga.: Akataš dev druž i nikērāyēh hac dāmān: hac cis i frärön nikeräi kunēt; cigdn göbet ku: ke ciš 6 an tan dahét, ke martom hac crs i frarön nikērāi dārēt, adak-iš Akataš dev šnayenit bavét ‘the dev A. is the evil spirit of breach of engagements with created beings: he makes (them) evade (a lawful thing =) what is legally agreed upon; as it is said: suppose a man gives something to another individual, if he persists in denying to (this) man the thing legally given he will have satisfied the dev A.’ In a general sense SGV XIV, 80: ke nigerde tē awāž-dādg ez in gavešni aš [= hän-as] rā gavešni-āzād dasture bad [West emends arbitrarily nigérde of the MSS to *nigaräe; tē: MSS u, a very common fault, v.s. v. u] ‘for him who
3353:rötastäk [lwtst’k], rostak [lwst’k] district, province 377. 8618. — In FrP 2 it is the first subdivision under šahr ‘dominion, kingdom’, and placed above déh ‘village’ and zänak ‘house’, cf Nyberg, Byzantion XXXVILI, 1968, 114-115. — MPrth rwdyst’g (A-H III); Paz. röstä, pl. rostčiga ; NP rēstā(i) ‘any inhabited place; a market-town, a village’; Arab. lw. rustäg, ruzdäg ‘arable land’.
3762:tašitan to create 3811. 7621; 6 ham ~ to create by putting together the different elements of a p. or a th. 3823. 3919. — Av. (644 sq.) taš-; Paz. tāšīdan.
3763:tat [tšt'] bowl 5312. 6013.19. — Av. (646) tašta-; NP tašt; Arab. lw. fast; Fr tasse = German Tasse; Telegdi 245.
3768:taxtak [t’htk'] tablet, pl. —-iha 113!; board for the game of tric-trac 1202-15, — NP tazxtah.
4240:vitartan [wtltn'], viturtan [wtwltn'], vi- taštan [wtštn'], vitir- [wtyl-] to pass: andar dašt bē vitart passed over the plain 318; pat kustak + deh vitart passed outside the village 619-17; to pass by 7!1.15.22; bē vitast drove ahead 71’; to cross a bridge 7225.27; to go through a stream 101%. 10323; kë vitīrēndv the passers-by 12815; — pt. vitart, viturt deceased: vitart coll. the deceased 837. 8413; viturtān martūmān 10517. — Av. (640) vi-tar- = OP; MPrth w(y)drdn w(y)dr- (S, MHC); MPrs pres. wdyr- (S); Ps. pt. wilty, pres. wtyl-, wtl-; Paz. vadardan vadirdan, pres. vadar-, va- der-, vadir-; NP guöastan guóar-. Verbum 206, Ghilain 57.
5392:tap-, tapa-, tapaya-: taftan (vi-)tar-: vitartan tarasca: turist tarsna-: tisnak taro: !tar, turist taš-: tašitan tašta-: tašt taOra-: tārīk taOrya-: tàrik tauruna-: tarr tav-: tuvan (pati-)!tav-: pattài, pattàn tavah-: stob tiyri-: tigr | Tird.nakaOwa-: Tir Tištrya-: Tistr tiži-: tēž tkaēša-: kēš tõi, to: -t türa-: Tur Tusa-: Tiis tušni-: tušn (fra)-Oang-: frahaxtan Oračtaona-: Fréton Orah-: sahm Orah-, terosa-: tarsitan Orisant-: !sih Orišva-: srišvātak Orita-: Srit Orita-: Oritak Oritya-: sitikar Owa-: to Owaxš-: tuxšitan
6785:röstä, röstägg: rötastäk rosnidari: roečnitarčh rövihed: rustan
```


## [2026-10-15T02:48:37.146Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} /tat \\[tšt.\\] bowl/ {print \"NYB leaf\",NR-1}' NYB_vol2_glossary.txt; grep -n \"taxtag \\[\\|tašt \\[\\|tāšīdan\\|tāšidan\\|tāš-\\|tēšag\\|tasidan\\|tašidan\" PHD.txt | head; grep -o \"tašt[^.]*\\.\\|taxtag[^.]*\\.\\|tāšīdan[^.]*\\.\\|t[eē]šag[^.]*\\.\" PHD.txt | head"
}
```


### [2026-10-15T02:48:37.531Z] TOOL RESULT

```
NYB leaf 209
593:tan-bahr [żn'Þ’ hl] physique. tand [tnd | = P] faint, languishing. ~ih: faintness, langour. | tan-drust [tn'drw(y)st! | N ~] healthy, whole. ~ih: health. tang [ing | = M, N ~] narrow, tight. ~ih: narrowness; distress. tanig [tn'yk! | N tani] bodily, corporal. tanigard(ig) [tnykrt(yk)! | M inygyrd] corporeal. ` tanīhā [tn'y/? | M tnyP?, N tanha] alone. tanómand [tn wmnd | N ~] corporeal. “АҺ: corporeality. tan-tdhmag [tn'twhmk'] (sap) of plants. tanuk [tnwk! | N ~] thin, shallow, tanür [tnw] | M tnwr, N ~] oven. tar [LCDr! < A l-sd; tl | M tr] over, through, across. ~ kardan, ~ menidan: abuse, despise. -tar [-z# | (M -dr), N ~] suffix forming comparative adjectives. tar [2] | M гу] darkness. tarāzēnīdan, tarāzēn- [tcyn-ytn!] weigh. tarázüg [tPcwk! | (P tPzwg), N tarazü] balance, scales; astr. Libra. targ [tlg | N ~] helmet. tarģumān [tigm?n! | M trgwmn] interpreter. tarig/k [PIyk! | M гуур, N tárik!] dark. ~th: darkness. tarist [¢/st'] = tar. tar-mānīh [t/m’nyh] perversity. tar-menišn [tImynin! | N tarmanist] perverse; contemptuous. 7h : perversity; contempt. tarr [t/, LC Dr (in error, v. tar) | N —] moist, fresh. ~ag [tik! | N ~a] vegetable. tars [2/5 | M trs, N ~] fear, respect. tarság [ts k! | M trs’g, N tarsā] Christian. tarsāģāh [15(?)/?5] respectful, reverent. ~ih: respect, reverence. tarsidan, tars- [tls-ytn' | (M tyrs??dn), N ~] fear, be afraid. tarwénidan, tarwēn- [t/zvyn-ytn! | M trw-] overcome, conquer. tas [25 | N ~] die (for gaming). tasum [tswm | = M] fourth. tāšīdan, tāš- [O i-ytn!'] cut, cleave; create. taSkanag [tšknk!] under-shirt. tašt [tšt' | N ~] bowl. tāšt [021] *certainty. ~ig [-yk'] certain. tāwān [1?(d)w’n' | N ~] compensation, obligation. taxl [t?% | (M thr), P txl, N talx] bitter.
1251:cleave tāšīdan.
1436:create af(u)ridan, (frāz) brēhēnīdan, dādan, tāšīdan; (daevic) kirrén- idan.
1475:cut (v.) b(u)ridan, tāšīdan. cutting (a.) burāg.
4515:1 tag tir tarig/kih tātīg/k rūbāh' t��b-, tāz- tāzānag 1tūzīg tābīdan tābag tābestān tābišn tāftan tas- tāšīdan
tāšīdan, tāš- [O i-ytn!'] cut, cleave; create.
tašt [tšt' | N ~] bowl.
taxtag.
tašt.
tāšīdan.
tāšīdan; (daevic) kirrén- idan.
tāšīdan.
taxtag.
taxtag.
```


## [2026-10-15T02:48:41.462Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} /tasum/ {print \"PHD leaf\",NR-1} /taxtag \\[/ {print \"taxtag leaf\", NR-1}' PHD_mackenzie.txt; grep -n \"taxtag \\[\" PHD_mackenzie.txt; grep -n \"تیشه\\|تخته\\|تشت\\b\\|طاس\" incoming/ARY/ARY_pages.txt | head"
}
```


### [2026-10-15T02:48:41.802Z] TOOL RESULT

```
PHD leaf 103
PHD leaf 136
PHD leaf 169
713:را وابسته به خود زرتشت می‌دانند و تاریخ حدود ۹۰۰ سال پیش از میلاد را برای زرتشت و کتابش
967:۱-روحانیون زرتشتی ۲- جنگاوران ۳- دهگانان.
1144:زرتشتی است. بخش قدیمی‌تر آن (گاتها) در سده‌های پازدهم تا ششم پیش از میلاد یعنی دوران کوج
4447:,7۸۸0۸ ,ات۸ 0تشتق۲ 0
6441:هلف باتشتف باآمعف فرهنگ معین : ۱۳۸۳
8747:۲- هلت دگرگرنی چم این واژه در زبان‌های ایرانی این است که پس از ظهور زرتشت و آئین او "آهورامزدا" مورد
9693:زوت» زوتر زاوتر (به چم "موبد زرتشتی مامور تهیه کردن آب مقدس") / ۳۲۹
9732:۱ واژه‌ی زور" به چم "آب مقدس که در مراسم زرتشتی پاشیده می‌شود" نیز از همین واجریشه است
13646:.ایرلندی کهن (7اکلقا صا0): 9 (متختهمی) :00/5
14101:۱- چم این واژه در زبان‌های ایرانی: روحانی زرتشتی,
```


## [2026-10-15T02:48:45.092Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY; grep -n -i \"teks\\|tash\\|TISHE\\|TAKHT\\|TARASH\" ARY_latin_index_pages.txt | head -20; grep -n \"teks\\|tekth\\|tieg\\|tyeg\" ARY_pages.txt | head"
}
```


### [2026-10-15T02:48:45.523Z] TOOL RESULT

```
1370:MACKENZIE: (FIRE) 114 EDHOS, HUTASH u<o5
5352:TeKO LITHUANIAN) «i p) TAGHT, TASHAL, Ossett) pis)"
5354:TACKELIS :(OLD PRUSSIAN) 5 53.4 ‘TACAG, TASHAG, TAVAG
5356:TECHIM, TECHID TASHT., TSAHAL
5429:TESE (RUMANIAN) lay) TASHAITI, AVESTAN) (yoy)
5433:TKAC, TKACTWO. ‘TUDSHAK, TASH-, (PAHLAVI) 5
5436:| reatt SERBIAN) og po ‘TASHTI, TAKSHAN-, TAKSH .
5438:‘TASHYTI (LITHUANIAN) gl ¢3 TEXO, TEXERE (LATIN) 3
5744:‘TEKSINIS HLATVIAN) (3) gi93 TAG PAHLAVD 15344
5779:‘REFERENCES ecethag ‘TASHYAH., TANCHISHTA
5986:TUSHCHIAS —(LITHUANIAN) 53 TASH HAFGHAND) (24) gi}
```


## [2026-10-15T02:48:48.379Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY; awk 'NR<=5438 && /pdf page/ {p=$0} NR==5438{print p}' ARY_latin_index_pages.txt; sed -n 5420,5445p ARY_latin_index_pages.txt; grep -n \"تراش\\|تاشیدن\\|تیشه\" ARY_pages.txt | head"
}
```


### [2026-10-15T02:48:48.728Z] TOOL RESULT

```
[pdf page 189]
‘REFERENCES both, TAXUS (LATIN) 3
POKORNY, —=SS*~*~*~*~*~*«dD OLD SCANDINAVIAN) 4 5-41
BUCK: 1388 THEXLA
FYO-FYF tabi oby (OLD HIGH GERMAN) 4 gilt
leetloal
gt y Sty Hi
(lace gg OS y 3 OT SNS) sla ete PY 9 By GLUE) 22 I'd ole
enh oA Mj 2g a5 DUS 22 OS ool Oe
Cogslaigs 9 cancun” pe a) gdlahdd «jaaAS Las (PERSIAN) yuh
TESE (RUMANIAN) lay) TASHAITI, AVESTAN) (yoy)
OLD CHURCH SLAVIC) 45 i535! ‘TWAXSHA, TWAXSH, TUXSHA
TESATI, TUKATI, TESHO (OLD PERSIAN) sol, go
(POLISH) ie) HAMATAXSHTA, HAMATAXSHAIY
TKAC, TKACTWO. ‘TUDSHAK, TASH-, (PAHLAVI) 5
TESLA, TKAT AARUSSIAN) 35 ‘TUXSHIH, TUXSHIDAN, TUXSHISHN
TKAT (CZECH) So ‘TAKSHATI (SANSKRIT) Sy Sile
| reatt SERBIAN) og po ‘TASHTI, TAKSHAN-, TAKSH .
TKATI, TKAT — (BOHEMIAN) aa.» TEKTON, TECHNO- (GREEK) oli,
‘TASHYTI (LITHUANIAN) gl ¢3 TEXO, TEXERE (LATIN) 3
‘TESHU LATVIAN) (.g3) sl TISSER (FRENCH) wil
TEJER SPANISH) glilya\
SESERE SUTALIAN) gids!
[pdf page 190]
FT os
M1 So
BUCK: 410 REFERENCES oot ~
325:در درون گور ساخته شده از سنگه‌های تراشیده شده قرار دارند و روی گور تپه‌ی کوچکی
8074:۲ چم بیشتر واژه‌های غیر ایرانی این فهرست: بریدن؛ تراشیدن.
10295:تراشیدن نیز از همین واجریشه‌اند. ً
11688:چم اين واژه در زبان‌های ژرمنی: قاشت» (در آغاز) قاشت چوبی» تراشه‌ی چوب.
```


## [2026-10-15T02:48:51.554Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY; awk 'NR<=8074 && /pdf page/ {p=$0} NR==8074{print p}' ARY_pages.txt; sed -n 8040,8080p ARY_pages.txt; awk 'NR<=10295 && /pdf page/ {p=$0} NR==10295{print p}' ARY_pages.txt; sed -n 10280,10297p ARY_pages.txt"
}
```


### [2026-10-15T02:48:51.923Z] TOOL RESULT

```
[pdf page 274]
آلمانی (۷لم4لقن): 1۸6 3 ناه
انگلیسی کهن (8[1ا8(/0 صاه): 6 (0(6)) :00/5

۸07 ,106 +57
انگلیسی لیبق 106 2 (0136838 ,347 (6مت)
دانمارکی (0۸(718): 16 0۵05 :۸45 بل مت تمه
سرئدی (5501577): ۱۳ برهان قاطع : ۸۴۱
نروژی (0۷ف۵/0737201. 16
هلندی (00707): 01 ,3۸86

َ اپرلندی کهن (تلدلم[ صاه). 10۴
یادداشت,
۱- واجریشه‌ی هند و اروپایی این ریشه در اصل همان واجریشه‌ای است که واژه‌ی «دراز» از آن ناشی شده
است.
۲ بازگلست به: دراز
چم این واژه در زبانهای اوستایی و پهلوی: طولانی» پایدار,
۴ چم این وأژه در زبانهای رومانس (ناشی از لاتین) و ژرمنی: دراز» طولانی
ا
[pdf page 274]
6666
دروء درودن» درویدن ] ۲۷۵
پهلری (۲7مالل۸): 0310۸07 لیترانی (771۸(/49۷):
کردی (82[57): تلود نی ۱زا 2811 ,ا3الت28 ,تا+057 :
تخاری ۸ (۸ ۰:70 18075
سانسکریت (85(/5777): پسگشت‌ها 5
7 ,0۸3 +034 زر ۳
یرنانی (07530): 58 ,0830 6 (1۸35) ی
اسلاوی کهن (ع1ماد 63 تال صان): 9 (۸5۸8) :2406212
8۸ ,0880 507 ک ان
روسی (۷ل75514چ): 0 برهان قاطع + ۸۴۱
چک (25301): ت08 لفت‌نامه دهخدا: ۷ و ۱۰۶۹۵
صربی (587814/۷7): 1 اد ۷۱۱
بادداشت,
۱ این واژه با واژه‌ی "دریدن" همریشه است. بازگشت به: دریدن. ۰
۲ چم بیشتر واژه‌های غیر ایرانی این فهرست: بریدن؛ تراشیدن.
‌
| تواکلس سوزی اش ی هد
اوستایی (۸887427): 7 ,0306 ,0۸306
او ابفت08۸06 ,08028۸37 020 افغانی (پشتو) (/4۸۳0/7۸/۷):
پارسی باستاً(0(ما دا رم : 7 0۸3361 ۱
۸ ,08۸6۸ سانسکریت (5۸(/587):
[pdf page 347]
ا فرائسه (/۳88/6): - ند اد دنم پسگشت‌ها 5
ٍ اسپانیایی (5۶۸(/1524): نا 1
[ اه ایبایای (ملم: 8 ون 6 ات78 2/7
پرتغانی (۳:077618892 3818811 5 ای نامام
گرتیک (007[716): ید ان 8 (۲3ت975) :0/705
ایسلندی کهن (/0104/1۸2/(ی50 صا0): 2 (878۴-۲۵) یا
871871۸ برهان قاطع : ۰
آلمانی کهن (057214(0 0[7اتز صزه): لفت‌نامه دهخدا : ۶ رو ۲۸۴۸
زد دی فرهنگ معین + ۳۳
[pdf page 347]
۸ | ستنبه» ستمبه (به چم *مرد درشت و قوی و دلیر")
یادداشت:
۱ فقدان واژه‌های همریشه در زبان‌های اوستایی و پهلوی و دیگر زبان‌های ایرانی وابستگی "سترون" يا واجریشه‌ی
هند و اروپایی 8781۰ را نامسجّل می‌کند و بهمین دلیل در جلو واجریشه‌ی مندارلاییای (شاید) آورده‌ام.
به احتمال زباد واژه‌های "استر" (به چم "قاط" که جانوری" مقطوع اللسل است) و سترون" (به چم" پا کر د(وارييي.
تراشیدن نیز از همین واجریشه‌اند. ً
فارسی ((۳28814): استنبه, ستمبه (به چم آمرد درشت و قوی و دلیر) 5
اوستایی (/4837۸2): 338۸1۸ آرمنی (4ل842(14): 87۸/8۸
```


## [2026-10-15T02:48:57.005Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY; awk '/\\[pdf page 18[89]\\]/{f=1} /\\[pdf page 190\\]/{f=0} f' ARY_pages.txt | head -80"
}
```


### [2026-10-15T02:48:57.372Z] TOOL RESULT

```
[pdf page 188]
تار» تاریک / ۱۸۹
اوستایی (478287:400): 1ل753/۸ ,7۸711 روسی (/40ا855): 18213107۸ بش۳۸
پهلری (7/شالل۸): چکه (2801): ۸ ,78/8

4 بلق 7 ,1226 ,هام1 بقق71 صربی (/58881۸2): 11۸ ,7۸31۸
اوستی (0558710): 1۸1136۸ ,7۸11816 بوهبی ((807181/14): 183/707۸ بش77
: کردی (008015/7): ۰ 1۸1137۸۸۲ ,72 اسلواکی (510142): ۰ 738۸8 ,۳8۸/075
بلوچی (7122:)2۸671 لیتوانی (174۸21۸24ل): :
اففانی (پشتر) (/۸۳0۸7: 7۸6 ب7107 1 ,قف 71158
تخاری 8 (8 ((فلتل70): 7۸/2855 لترنی (لتی) (701۵(۷شا): 71318۸ ,77۸18۸
سانسکر یت (84/570707): ,7۸/5۳۸5 ایرلندی کهن (54لم1 صاه): 1۳
۸8 1۸/153 ,گف/7۸3 ولزی (لکاظ): 1۲۷۲ ,۳۷۷۷27073
لانین (110/0هل): ای[ لاد با برترنی (/88870):
فرانسه (3ل)57چ۳): 75 182۷۸ ,12۸۷۸3350۷2
اسپانیایی (5۳۸(۷187): +۸ اند انا
ایتالیایی (/42ا7۸): زد اد ندید با پسگشت‌ها 35 :
روماتی (لفالنفات‌: 1۷1038816 ان کت 0 را
ایسلندی کهن (/(010۸/۵(ن5 ضان): 2 ۲818333 +8۸2
1 6 (80/858) :ما02
آلمانی کهن ((0572/4 7ل0ابز صان): :نز
20۸ ۰ (3۸3331885 ب0۸3)
آلمانی (05/۸7): ۰ - 3 اد نداد ان ناه
نروژی (0۷80۵/): 7 3 (5ف18828) :07005
یس هلندی (0070): لدات ۱۱۱۱۱ 9 (78) :7
اسلاوی کهن قاری صله): 9 (0۸3555) 0
7۸ برهان قاطم + ۳۵۶
لهستانی (تلقلا0): خ11۸
بادداشت,
واژه‌ی فارسی ام" (به چم "تاری چشم" با "آب مروارید") نیز از همین واجریشه است (301۳0143۲۷:1063 و
برهان قاطع : ۵۱۱) َ
[pdf page 189]
۰ _تخش (به چم
پارسی پاستان (۳۶8۶1۷ صا0): ۹۳۸37511۸ 8۸ق981پین
سانسکریت (54(/58217)(شاید) 7۸68130 انگلیسی کهن (افلساه۵ صرم: 080
بونانی 078810): 71007 1
لاتین (710مل): 15 پسگشت‌ها انش گرد دنر
ایسلندی کهن (50/01249 صا۵): 1
7۴۸ 1388 ناه
آلمانی کهن ((4/ل087 ۲/04 صا0): برهان قاطع + ۴۷۵-۶
بادداشت:
۱ بازگشت به: تک و تاختن.
۲- چم اين واژه در زبان‌های یونانی و لاتین: درخت سرخدار (که از آن تیر وکمان می‌ساختند!)
چم این واژه در زبان ژُرمنی: نیزه» تبر زین.
فارسی (۶88514۷): تخشا, تخشیدن, تخشایی (به چم اصنعت و کوشایی)
اوستایی (۸۲874۸۷)+ ,1۸871۸171 رومانی (1۷/(م۸۸4). 7۹
ب,لا8 7۷۷۸3 ,1۸38۸ اسلاری کهن (12ماد لل6اناتل صام:
پارسی باستان (/۳8۵1۸۸ صرا0): 0 ,71۸3 ,7185۸77
1۸31۸7۸381712 لپستانی (5اءا۳0۵):
پهلری (1اماتقم۳): +7۸8 بلقتا۳005 0 فل7
1 ,71281110۸ ,7آ3[ق02ا7 روسی (/(#1(991۸): 7 ,شآ788
سانسکریت (5758077): ایا نها چکه (28270): 747
۱ ۸67 +اج۸ت1قل7۸ ,اتاقرچ صربی ((4ا6278: 1
یونانی 082810): ۰ -78011310 ,7826700 برهمی (۷ل80778//14). 5شل1 ,7843
لاتین (4710مل): ,7830 لیتوانی (۸ا7هلا77ار): اوران ۷
فرانسه ([ج/(۳88): ادن لتونی (لتی) (1ف71م): 11
آسپانپایی (8۸۸//3/7): 3 ندال
ایتالیایی ((اله17): اد ی لد نان
```


## [2026-10-15T02:49:01.711Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"^tass\\b\\|^tass,\\|^tassie\" KLN_1966.txt | head; grep -n \"^tass\\|^tassie\" SKT.txt | head; grep -n \"^architect\\|^technique\\|^text,\\|^text\\b\\|^tissue\\|^test,\\|^test\\b\\|^context\" KLN_1966.txt | head -20"
}
```


### [2026-10-15T02:49:02.097Z] TOOL RESULT

```
38270:tass,  n. ,  a  drinking  cup ;  a  small  draft.— M  F.  ( =  F.) tasse,  ‘cup’,  fr.  OF.,  fr.  Arab.  tassah,  tass,  fr. Pers.  tdsht,  ’cup,  saucer’.  Cp.  OProveng.  tassa, It.  tazza,  Sp.  taza,  ‘cup’,  which  are  of  the  same origin.  Cp.  also  tazza.
536:architecture
30197:text.
38728:test
38729:test,  n.,  a  cupel  for  refining  or  trying  metals; examination,  trial.  —  ME.,  fr.  MF.,  fr.  OF.,  fr.
38804:text,  n.  —  ME.,  fr.  MF.  (=  F.)  texte,  fr.  OF.,  fr. L.  textus,  ‘texture,  structure;  context’,  from  tex- tus,  pp.  of  texere,  ‘to  weave,  plait,  fit  together’, which  is  cogn.  with  OI.  tdkgati,  ‘he  fashions, constructs’,  taksan,  ‘carpenter’,  Avestic  task-,  ‘to cut,  carve’,  tasha,  ‘ax,  hatchet’,  Gk.  xbcxov, ‘carpenter’,  xsyvr,  (for  *teks-nd-),  ‘art’,  OSlav. tesla,  ‘ax,  hatchet’,  tesp,  tesati,  ‘to  hew,  fell,  cut down’,  tesu,  ‘beam’,  Lith.  taiau,  taSyti,  ‘to  cut, carve’,  OIr.  tal  (for  *tdkslo-),  ‘cooper’s  ax,  ma¬ son’s  ax',  Arm.  t‘ek‘em,  ‘I  turn,  wind,  twist’, OHG.,  MHG.  dahs,  G.  Dachs,  Du.  das,  ‘badger’
39339:tissue,  n.  —  ME.  tissu,  fr.  OF.  (=  F.)  tissu, ‘woven  fabric’,  pp.  of  tistre  (F.  litre,  tisser),  fr. L.  texere,  ‘to  weave’;  introduced  into  medical terminology  by  the  French  anatomist  and  phy¬ siologist  Marie-Francois-Xavier  Bichal  (1771- 1802)  about  the  year  1800.  See  text  and  cp. words  there  referred  to.
```


## [2026-10-15T02:49:04.957Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 38729,38732p KLN_1966.txt; sed -n 38804,38808p KLN_1966.txt | cut -c1-1500; grep -n \"^architect\" KLN_1966.txt; sed -n 530,540p KLN_1966.txt | cut -c1-600; grep -n \"^technique\\|^technic\" KLN_1966.txt"
}
```


### [2026-10-15T02:49:05.458Z] TOOL RESULT

```
test,  n.,  a  cupel  for  refining  or  trying  metals; examination,  trial.  —  ME.,  fr.  MF.,  fr.  OF.,  fr.
L.  testu,  testum,  "vessel,  earthen  vessel,  pot', which  is  rel.  to  testa,  ‘piece  of  burnt  clay,  pot¬ sherd,  shell,  scale",  and  prob.  cogn.  with  Avestic tashta-,  ‘cup",  Lith.  list  as,  ‘vessel  made  of  willow twigs",  and  with  L.  texere,  ‘to  weave",  fr.  I.-E. base  *tekth-,  'to  weave".  See  text  and  cp.  testudo. Cp.  also  tester,  ‘canopy".
Derivatives;  test,  tr.  v.,  to  refine  in  a  cupel;  to put  to  the  test;  to  try,  examine,  testable  (q.v.), tester  (q.v.),  test-ing,  adj.,  test-ing-ly,  adv. test,  n.,  the  hard  shell  of  many  invertebrates  ( zoal .) —  L.  testa,  ‘shell’.  See  test,  ‘cupel’, testable,  adj.,  capable  of  being  tested.  —  Formed with  suff.  -able  fr.  test,  ‘to  try".  See  test,  ‘cupel’, testable,  adj.,  capable  of  being  disposed  of  by will  (law.)  —  L.  testabilis,  ‘that  has  a  right  to give  testimony",  fr.  testdri.  See  testament  and -able.
Testacea,  n.  pi.,  an  order  of  invertebrates  covered with  shells.  ( zoo! .)  —  ModL.,  fr.  L.  testaceus, ‘covered  with  a  shell".  See  testaceous, testacean,  adj.,  any  of  the  Testacea.  —  See  prec. word  and  -an.
text,  n.  —  ME.,  fr.  MF.  (=  F.)  texte,  fr.  OF.,  fr. L.  textus,  ‘texture,  structure;  context’,  from  tex- tus,  pp.  of  texere,  ‘to  weave,  plait,  fit  together’, which  is  cogn.  with  OI.  tdkgati,  ‘he  fashions, constructs’,  taksan,  ‘carpenter’,  Avestic  task-,  ‘to cut,  carve’,  tasha,  ‘ax,  hatchet’,  Gk.  xbcxov, ‘carpenter’,  xsyvr,  (for  *teks-nd-),  ‘art’,  OSlav. tesla,  ‘ax,  hatchet’,  tesp,  tesati,  ‘to  hew,  fell,  cut down’,  tesu,  ‘beam’,  Lith.  taiau,  taSyti,  ‘to  cut, carve’,  OIr.  tal  (for  *tdkslo-),  ‘cooper’s  ax,  ma¬ son’s  ax',  Arm.  t‘ek‘em,  ‘I  turn,  wind,  twist’, OHG.,  MHG.  dahs,  G.  Dachs,  Du.  das,  ‘badger’
[ML.  taxus,  taxo,  It.  tasso,  F.  taisson,  Sp. texon  (now  spelled  tejdri),  ‘badger’,  are  Teut. loan  words],  lit.  ‘the  builder’,  ON.  pattr,  ‘thread, wick’.  Cp.  also  Hitt,  taksh-,  ‘to  join,  unite, build’,  takshan,  ‘together’.  All  these  words  de¬ rive  fr.  I.-E.  base  *tekht-,  *tekh-,  ‘to  build  (of wood),  carpenter;  to  weave’.  The  original  mean¬ ing  of  this  base  prob.  was  ‘to  plait,  twist’.  Cp. architect,  context,  dachshund,  pretext,  subtle, Taxidea,  technic,  tecto-,  ‘builder’,  Tectona,  tec¬ tonic,  tela,  telary,  tessitura,  test,  ‘cupel’,  textile, thixle,  tiller,  tissue,  toil,  ‘net’.
textile,  adj.  —  L.  textilis,  ‘woven’,  fr.  textus,  pp. of  texere.  See  text  and  suff.  -ile.
Derivative:  textile,  n.
textlet,  n.,  a  little  text.  —  Formed  fr.  text  with the  dimin.  suff.  -let.
536:architecture
compare
archaeol.
archaeology
Cret.
Cretan
archit.
architecture
crystallogr.
crystallography
Arm.
Armenian
1032:technical,  technology
```


## [2026-10-15T02:49:08.822Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"^architect,\\|^technique,\\|^technic,\\|^context,\" KLN_1966.txt | head; grep -n \"^ARCHITECT\\|^TECHNIQUE\\|^TASS\\b\" SKT.txt | head"
}
```


### [2026-10-15T02:49:09.330Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-15T02:49:11.754Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"architect, *n\\|technique, *n\\|context, *n\" KLN_1966.txt | head; grep -n -i \"^architect\\|^technique\\|^tass\\|^tissue\\|^text\" SKT.txt | head"
}
```


### [2026-10-15T02:49:12.120Z] TOOL RESULT

```
3347:Archimedean,  adj.,  pertaining  to  Archimedes.  — Formed  with  suff.  -an  fr.  L.  Archimedeus,  ‘of  Ar¬ chimedes’,  fr.  Gk.  ’Apxip.flSr)?,  Archimedes,  the celebrated  mathematician  (2877-212  B.C.E.). archipelago,  n.,  1)  the  Aegean  Sea;  2)  a  sea  stud¬ ded  with  many  islands;  3)  a  group  of  islands.  — It.  arcipelago,  lit.  ‘the  chief  sea’,  compounded  of arci-,  ‘chief’,  fr.  Gk.  dpyi-  (see  archi-),  and  Gk. TziXayoQ,  ‘sea’  (see  pelagic).  In  ancient  and  me¬ diaeval  Greek,  the  word  apxrneXayor  does  not occur,  in  modern  Greek  it  is  an  Italian  loanword. The  fact  that  archipelago  orig.  denoted  the  Aege¬ an  Sea  may  help  us  find  the  origin  of  this  word, which  is  a  real  crux  etymologorum.  It.  arcipelago very  probably  arose  from  a  mistaking  of  Gk. Atyaiov  TtfXayo:,  ‘the  Aegean  Sea’,  for  dpy.- TrsXayo;,  ‘the  chief  sea’,  a  confusion  suggested  by the  numerous  Greek  words  beginning  with  dpyi- . archiplasm,  n.,  1)  primitive  protoplasm;  2)  ar- choplasm. — Compounded  of  archi-  and  -plasm. Derivative:  archiplasm-ic,  adj. architect,  n.  —  F.  architecte,  fr.  L.  architectus,  fr. Gk.  ap/enberav,  ‘master  builder’,  fr.  dp/t-, ‘chief’,  and  text<ov,  ‘carpenter,  builder’,  which is  rel.  to  ttiyyT,,  ‘art,  skill,  craft’.  See  archi-  and text  and  cp.  technic,  tectonic, architectonic,  adj.  —  L.  architectonicus ,  fr.  Gk, dpXiTExxovixog,  ‘pertaining  to  a  master  builder’, fr.  dpxiTEXTtnv.  See  prec.  word  and  -ic. architectonics,  n.  —  See  prec.  word  and  -ics. architecture,  n.  —  F.,  fr.  L.  architectiira,  fr.  ar¬ chitectus.  See  architect  and  -ure.
8949:L.  contestdri.  See  prec.  word  and  -ant. contestation,  n.  —  F.,  fr.  L.  contestationem,  acc. of  contestdtio,  ‘an  attesting,  testimony’,  fr.  con- testatus,  pp.  of  contestdri.  See  contest  and  -ation and  cp.  attestation,  detestation, context,  n.  —  L.  contextus,  ‘a  joining  together, connection’,  fr.  contextus,  pp.  of  contexere,  ‘to weave,  join  together,  interweave,  unite’,  fr.  con- and  texere,  ‘to  weave’.  See  text, contextual,  adj.  —  Formed  fr.  prec.  word  with adj.  suff.  -al;  first  used  by  Coleridge.  Cp. textual.
38360:Derivatives:  technic-al,  adj.,  technic-al-ism,  n., technic-al-ity,  n.,  technic-al-ly,  adv.,  technic-ian, n.,  technic-ism,  n.,  technic-ist,  n. technicon,  n.,  a  device  for  exercising  the  hands  of a  pianist.  —  Gk.  te-/vix6v,  neut.  of  te/vixoc, ‘pertaining  to  art’.  See  prec.  word, technique,  n.,  method  or  skill  in  performance.  — F.,  fr.  the  Greek  adjective  te/vixo;,  ‘pertaining to  art’,  used  as  a  noun.  See  technic, techno-,  combining  form  meaning  ‘art,  skill’.  — Gk.  tsxvo-,  fr.  reyvrj .  See  technic, technocracy,  n.,  government  of  society  by  tech¬ nicians.  —  Compounded  of  techno-  and  Gk. -xpa-rfa,  ‘rule  of’,  fr.  xpaxog,  ‘strength,  power, rule’.  See  -cracy.
19220:Tassel  (i),  a  bunch  of  silk,  ftc, ornament  (F.  —  L.)  M,  E.  tojtel^ tassei,  an  ornament,  clasp :  also  a  pi< square  staff  (cf.  Ital.  tastelh,  a  aqai collar  of  a  cloak).  —  L.  taxiUum^  1 taxillus,  a  small  die;  dimin.  of  M knuckle-bone,  a  die  made  of  a  kn bone.  Ttilus  »  tax-lui*,  as  shrwa  I dimin.  taxiUus,  and  means  a  bone  1 squared ;  cf,  Skt  taksh,  to  hew,  pr make.  (VTAK.)  f  The  appliottl a  tassel  is  curious ;  a  wood-cut  at  ] of  Guillim'ft  Display  of  Heraldry  ( shews  a  tassel  ornamented  with  stiioj dots:  these  strings  divide  it  into  sq each  of  whicb  (having  a  dot  hi  them resembles  an  Me  cit  a  dit.
19265:architect.  (F.  ->  L.  «  Gk.)  F.  artkt- tt<tt.  —  L.  architectuj,  the  same  as  anc*> /^r/tfH.  — Gk.  dpxiW«Taft%  a  chief  builder  Of artificer.  —  Gk.  'ip^i-,  chief  vsec  Arolu-); W«ra>f,  a  carpenter,  bulkier.  ^Scc  alsu Text.)
19471:text  of  a  book.  *-  L.  textus,  woven,  pp.  of
19480:textile.  (L.)  L.  ttxtitis^  woven.  —  L. textus,  pp.  of  Uxrrt,  to  weave.
19481:texture.  (F.-L.)  F,  texture,  'a  tex- ture, web ; '  Col.  —  L.  textura^  a  web.  —  L. textus,  pp,  of  texere,  to  weave.
19765:Tissue ;  sec  Text.
```


## [2026-10-15T02:49:17.041Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for w in \"تیشه\" \"تشت\" \"تخته\" \"طاس\" \"تراشیدن\" \"آرشیتکت\" \"تکنیک\" \"سیج\"; do echo \"== $w\"; grep -n \"^$w\\b\\|^$w \" MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v*_djvu.txt 2>/dev/null | head -3 | cut -c1-300; done"
}
```


### [2026-10-15T02:49:17.543Z] TOOL RESULT

```
== تیشه
incoming/MON/MON_2vol_Adena_v2_djvu.txt:37031:تیشه شکستن: خرد و به قطعات کردن گوهر 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:45620:تیشه: (0-)«۱15 (.) افزار آهنی نجاران. افزار 
MON_part2.txt:37031:تیشه شکستن: خرد و به قطعات کردن گوهر 
== تشت
MON_part2.txt:29598:تشتا کرد دارد و شاخ‌هایش درازتر از 
MON_part2.txt:46407:تشتتا کنر بل 
MON_part2.txt:75931:تشته ال ۱ [ع. ۱( ج. امراة (بر 
== تخته
incoming/MON/MON_2vol_Adena_v2_djvu.txt:25915:تخته‌ای به بلندی حروف میخ‌کوبی کرده 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:38878:تخته‌های مستطیلی که در بعضص نقاط گبلان و 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:40792:تخته‌ای که بر آن حروف کلمات را نو یسند 
== طاس
incoming/MON/MON_2vol_Adena_v2_djvu.txt:23789:طاس. (رض.) عددی که دو بار در نفس خود 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:60759:طاس‌بازی کنند. (مد.) (عم.) از دحام مردم 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:69457:طاس افکندن (انداختن). مهره در ششدر 
== تراشیدن
MON_part1.txt:39589:تراشیدن: «رمل[-۱2۵1 (مسص م.) ستردن 
MON_part1.txt:81443:تراشیدن فلز را ندارد. سوهان روح: (کن.) 
MON_part1.txt:90519:تراشیدن. 
== آرشیتکت
== تکنیک
incoming/MON/MON_2vol_Adena_v1_djvu.txt:42999:تکنیک: *[:۱6 (ص‌نسه.) فنی. کار فنی. 
MON_part1.txt:42999:تکنیک: *[:۱6 (ص‌نسه.) فنی. کار فنی. 
== سیج
incoming/MON/MON_2vol_Adena_v1_djvu.txt:26741:سیجاره: (0-)0-022 (ص‌مر.) عاجز» 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:38251:سیجیدن (سپاهیان)؛ ج. تجهیزات. تجهیز 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:82129:سیج: (لبویلردء (ا.) انگور خشک شده؟
```


## [2026-10-15T02:49:20.854Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; f=incoming/MON/MON_2vol_Adena_v1_djvu.txt; sed -n 45620,45624p $f; sed -n 39589,39592p MON_part1.txt; sed -n 42999,43001p MON_part1.txt; sed -n 82129,82134p $f; grep -n \"^تشت:\\|^تشت \\|^طاس:\\|^تخته:\\|^آرشیتکت\\|^ارشیتکت\" $f incoming/MON/MON_2vol_Adena_v2_djvu.txt | head"
}
```


### [2026-10-15T02:49:21.355Z] TOOL RESULT

```
تیشه: (0-)«۱15 (.) افزار آهنی نجاران. افزار 
آهنی بتکم اسان . تشه بر بای خود زدن: 
(کد.) برهم زدن کار و بار خود» ضایم کردن 
کار خویش. تيشه بسوی خود زدن: (کن.) 
حریص بودن» طمع داشتن. تبشه فرهاد تیز 
تراشیدن: «رمل[-۱2۵1 (مسص م.) ستردن 
موی به وسیلة تیغ از بدن. خراشیدن و پاک 
کردن چیزی. رنده کردن به وسیله سوهان یا 
چر ح. حکك کردن. خراطی کردن. صاف 
تکنیک: *[:۱6 (ص‌نسه.) فنی. کار فنی. 
() فن. 

سیج: (لبویلردء (ا.) انگور خشک شده؟ 
زد 

سیج: له (ا.) رنج» محنت» مشقت. 
سجحمنك. وه [ - سیج] (ص‌مر.) 
دارندهً درد و رنج. محل رنج و محنت. 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:38829:تخته: (0-)۱2:2 (۰.) قطعه چوب پهن و 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:40761:تشت: ۱8 (۷.) ظرفی فلزی بزرگ و پهن و 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:40763:تشت کسی از بام افتادن: رسوا شدن او» 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:67313:تشت اد جاح [- رستاد| (.) و ظیفه راتبه» 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:91564:طاس: :۱2 (معر. تاس] (.) طشت کلان. 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:91596:طاس: عقّا [- تاس ] (ص.) سری که موی
```


## [2026-10-15T02:49:27.793Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; sed -n 1,40p tools/fetch_source.py | grep -i \"usage\\|argv\\|def \\|out\" | head"
}
```


### [2026-10-15T02:49:28.164Z] TOOL RESULT

```
def html_to_text(s):
def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if "--note" in sys.argv:
        note = sys.argv[sys.argv.index("--note") + 1]
```


## [2026-10-15T02:49:34.891Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; N='page 509'; for u in \\\n\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/teḱs-|root Tex: PIE teks-\" \\\n\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/tyegʷ-|root Tiegu: PIE tyegw-\" \\\n\"https://en.wiktionary.org/wiki/تشت|root Tex #2 tasht\" \\\n\"https://en.wiktionary.org/wiki/تیشه|root Tex #2 tishe\" \\\n\"https://en.wiktionary.org/wiki/تخته|root Tex #2 taxte\" \\\n\"https://en.wiktionary.org/wiki/طاس|root Tex #2/#3 tas\" \\\n\"https://en.wiktionary.org/wiki/تراشیدن|root Tex #6/#7 tarashidan\" \\\n\"https://en.wiktionary.org/wiki/سیج|root Tiegu #3 sij\" \\\n\"https://en.wiktionary.org/wiki/testum|root Tex #13 testum\" \\\n\"https://www.etymonline.com/word/tass|root Tex #5 tass\" \\\n\"https://www.etymonline.com/word/test|root Tex #13/#14 test\" \\\n\"https://www.etymonline.com/word/architect|root Tex #9/#12 architect\" \\\n\"https://www.etymonline.com/word/technique|root Tex #9/#12 technique\" \\\n\"https://www.etymonline.com/word/text|root Tex #13/#14 text\" \\\n\"https://www.etymonline.com/word/tissue|root Tex #14 tissue\" \\\n\"https://en.wiktionary.org/wiki/آرشیتکت|root Tex #11 arshitekt\" \\\n; do url=\"${u%%|*}\"; note=\"${u##*|}\"; echo \"### $url\"; python3 tools/fetch_source.py \"$url\" --note \"$N, $note\" 2>&1 | tail -2; done"
}
```


### [2026-10-15T02:49:39.522Z] TOOL RESULT

```
### https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/teḱs-
/home/sfmqrb/git/rishe-private/data/verification/sources/web/81278cc75ebe524a.txt
### https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/tyegʷ-
/home/sfmqrb/git/rishe-private/data/verification/sources/web/c54e804475c8c0e5.txt
### https://en.wiktionary.org/wiki/تشت
/home/sfmqrb/git/rishe-private/data/verification/sources/web/b4c1368a67787c66.txt
### https://en.wiktionary.org/wiki/تیشه
/home/sfmqrb/git/rishe-private/data/verification/sources/web/deda039d01e8aacd.txt
### https://en.wiktionary.org/wiki/تخته
/home/sfmqrb/git/rishe-private/data/verification/sources/web/15bc46cc1068c67f.txt
### https://en.wiktionary.org/wiki/طاس
/home/sfmqrb/git/rishe-private/data/verification/sources/web/97b710c758c5031b.txt
### https://en.wiktionary.org/wiki/تراشیدن
/home/sfmqrb/git/rishe-private/data/verification/sources/web/d0fc74304ea36d44.txt
### https://en.wiktionary.org/wiki/سیج
/home/sfmqrb/git/rishe-private/data/verification/sources/web/2ecbdfde52a07732.txt
### https://en.wiktionary.org/wiki/testum
/home/sfmqrb/git/rishe-private/data/verification/sources/web/c5d41015a28f7d02.txt
### https://www.etymonline.com/word/tass
/home/sfmqrb/git/rishe-private/data/verification/sources/web/bae13ccb0ca90d8c.txt
### https://www.etymonline.com/word/test
/home/sfmqrb/git/rishe-private/data/verification/sources/web/77d9f6eba65c4ee1.txt
### https://www.etymonline.com/word/architect
/home/sfmqrb/git/rishe-private/data/verification/sources/web/b29d7e690d00cb0a.txt
### https://www.etymonline.com/word/technique
/home/sfmqrb/git/rishe-private/data/verification/sources/web/4cfe72023ac836bd.txt
### https://www.etymonline.com/word/text
/home/sfmqrb/git/rishe-private/data/verification/sources/web/bdeca73d2abb2ad2.txt
### https://www.etymonline.com/word/tissue
/home/sfmqrb/git/rishe-private/data/verification/sources/web/9c200e2bb393e5be.txt
### https://en.wiktionary.org/wiki/آرشیتکت
/home/sfmqrb/git/rishe-private/data/verification/sources/web/444ba3384e24af5f.txt
```


## [2026-10-15T02:49:42.558Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; for f in b4c1368a67787c66 deda039d01e8aacd 15bc46cc1068c67f 97b710c758c5031b d0fc74304ea36d44 2ecbdfde52a07732 444ba3384e24af5f; do echo \"=== $f\"; wc -c < $f.txt; grep -i -A6 \"^Etymology\\|Etymology\" $f.txt | head -14; done"
}
```


### [2026-10-15T02:49:42.982Z] TOOL RESULT

```
=== b4c1368a67787c66
2890
 Etymology 1 

 1.1.1 
 Verb 

 1.2 
 Etymology 2 

 1.2.1 
 Verb 

 Toggle the table of contents 

--
=== deda039d01e8aacd
3092
=== 15bc46cc1068c67f
12747
 Etymology 

 2.2 
 Noun 

 2.2.1 
 Derived terms 
--
 Etymology 

 3.2 
 Pronunciation 

 3.3 
=== 97b710c758c5031b
15003
 Etymology 

 1.3 
 Noun 

 1.3.1 
 Declension 
--
 Etymology 

 2.2 
 Noun 

 2.2.1 
=== d0fc74304ea36d44
11870
 Etymology 

 1.3 
 Pronunciation 

 1.4 
 Verb 
--
 Etymology
 [ edit ] 

 From Middle Persian [script needed] ( tʾšytn /⁠tāšīdan⁠/ , “ to cut, cleave ” ) , Northern Luri تاشنیێ ( taşnyı ) , with intrusive -r- from contamination with خراشیدن ( xarâšidan , “ to scratch ” ) , from Proto-Iranian *tā́šti ( “ to cut ” ) , from Proto-Indo-Iranian *tā́ćšti , from Proto-Indo-European *tetḱ- ( “ to create; to cut ” ) . Cognate with Sanskrit ताष्टि ( tāṣṭi , “ to cut; to carve ” ) , Russian теса́ть ( tesátʹ , “ to cut; to hew ” ) , Latin texō ( “ to pleat; to weave ” ) , Ancient Greek τέχνη ( tékhnē , “ art, craft ” ) . [ 1 ] 

 Pronunciation
=== 2ecbdfde52a07732
6273
 Etymology 

 1.2 
 Pronunciation 

 1.3 
 Noun 
--
 Etymology 

 2.2 
 Pronunciation 

 2.3 
=== 444ba3384e24af5f
140
```


## [2026-10-15T02:49:48.147Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; for f in b4c1368a67787c66 deda039d01e8aacd 444ba3384e24af5f; do echo \"=== $f\"; sed -n 1,200p $f.txt | grep -v \"^\\s*$\" | head -40; done"
}
```


### [2026-10-15T02:49:48.523Z] TOOL RESULT

```
=== b4c1368a67787c66
URL: https://en.wiktionary.org/wiki/تشت
FETCHED: 2026-10-12T18:40:10Z
STATUS: 200
TITLE: تشت - Wiktionary, the free dictionary
تشت - Wiktionary, the free dictionary 
 Jump to content 
 Main menu 
 Main menu
 move to sidebar 
 hide 
 Navigation
 Main page 
 Community portal 
 Requested entries 
 Recent changes 
 Random entry 
 Help 
 Glossary 
 Contact us 
 Special pages 
 Search 
 Search 
 Appearance 
 Donations 
 Create account 
 Log in 
 Personal tools 
 Donations 
 Create account 
 Log in 
 Contents
 move to sidebar 
 hide 
 Beginning
 1 
 Arabic 
 Toggle Arabic subsection 
 1.1 
 Etymology 1 
 1.1.1 
=== deda039d01e8aacd
URL: https://en.wiktionary.org/wiki/تیشه
FETCHED: 2026-10-12T18:40:10Z
STATUS: 200
TITLE: تیشه - Wiktionary, the free dictionary
تیشه - Wiktionary, the free dictionary 
 Jump to content 
 Main menu 
 Main menu
 move to sidebar 
 hide 
 Navigation
 Main page 
 Community portal 
 Requested entries 
 Recent changes 
 Random entry 
 Help 
 Glossary 
 Contact us 
 Special pages 
 Search 
 Search 
 Appearance 
 Donations 
 Create account 
 Log in 
 Personal tools 
 Donations 
 Create account 
 Log in 
 Contents
 move to sidebar 
 hide 
 Beginning
 1 
 Persian 
 Toggle Persian subsection 
 1.1 
 Pronunciation 
 1.2 
=== 444ba3384e24af5f
URL: https://en.wiktionary.org/wiki/آرشیتکت
FETCHED: 2026-10-15T02:49:39Z
STATUS: -1
TITLE: 
FETCH FAILED: HTTP Error 404: Not Found
```


## [2026-10-15T02:49:52.336Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; for f in 97b710c758c5031b 15bc46cc1068c67f 2ecbdfde52a07732; do echo \"=== $f\"; grep -A3 \"^ Etymology$\" $f.txt | grep -v \"^\\s*$\\|edit\\|Etymology\" | head -6; done; grep -i \"From\\|Iranian\\|Avestan\\|Persian\" c54e804475c8c0e5.txt | head -20"
}
```


### [2026-10-15T02:49:52.747Z] TOOL RESULT

```
=== 97b710c758c5031b
 Shortening of طَسْت ( ṭast ) , from Middle Persian tšt' ( tašt ) , ultimately from the past participle of the Proto-Iranian verb *taš- ( “ to make, construct; to cut ” ) , from Proto-Indo-Iranian *tā́ćšti , from Proto-Indo-European *tḗtḱ-ti ~ *tétḱ-n̥ti , from *tetḱ- ( “ to create ” ) . Doublet of طَشْت ( ṭašt ) and طَسْت ( ṭast ) .
--
 Borrowed from Arabic طَاس ( ṭās , “ bowl, cup ” ) .
=== 15bc46cc1068c67f
--
 From Middle Persian tʾhtk' ( taxtag , “ tablet, plank, (chess) board ” ) , from tʾht' ( taxt , “ throne ” ) and the suffix -k' ( -ag ) . Compare Old Armenian տախտակ ( taxtak ) , Aghwan 𐔳𐔰𐕀𐕜𐔰𐕄 ( daxṭaḳ ) , and Arabic تَخْتَج ( taḵtaj ) , Middle Iranian borrowings.
=== 2ecbdfde52a07732
 From Middle Persian [script needed] ( syc /⁠sēj⁠/ , “ danger, trouble ” ) , compare Avestan 𐬌𐬚𐬌𐬌𐬈𐬘𐬀𐬵 ( i θiiejah ) .
--
 From Wiktionary, the free dictionary
 Terms derived from the Proto-Indo-European root *tyegʷ- (20 c, 0 e) 
 Proto-Indo-Iranian: *tyáǰatay 
 Proto-Indo-Iranian: *tyáǰati 
 Proto-Indo-Iranian: *tityā́ǰa 
 Proto-Indo-Iranian: *tyāǰáyati 
 Proto-Indo-Iranian: *tyáǰas ( see there for further descendants )
 Proto-Indo-Iranian: 
 ^ Cheung, Johnny ( 2007 ), “ *θi̯aǰ (*ti(n)ǰ²) ”, in Etymological Dictionary of the Iranian Verb (Leiden Indo-European Etymological Dictionary Series; 2), Leiden, Boston: Brill, →ISBN , pages 392-393 
 Retrieved from " https://en.wiktionary.org/w/index.php?title=Reconstruction:Proto-Indo-European/tyegʷ-&oldid=92151828 "
```


## [2026-10-15T02:49:59.348Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/تخت\" --note \"page 509, root Tex #2 taxt (base of taxte)\" | tail -1; f=$(python3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/تخت\" --note \"page 509, root Tex #2 taxt\" | tail -1); grep -A3 \"^ Etymology\" $f | grep -v \"^\\s*$\" | head -12; grep -n \"Ойаў\\|Oiaj\\|θi̯aǰ\\|Oiag\\|ti(n)\" data/verification/sources/refs/CHEUNG.txt | head"
}
```


### [2026-10-15T02:50:02.002Z] TOOL RESULT

```
/home/sfmqrb/git/rishe-private/data/verification/sources/web/cc36ebc3f350537d.txt
 Etymology 
 1.2 
 Pronunciation 
--
 Etymology 
 3.2 
 Noun 
--
 Etymology 
 4.2 
 Noun 
--
25318:*ti(n)jl 389 
25365:*ti(n)f! ‘to sharpen’ 
25390:The root *ti(n)j’ is etymologically related to *staif. For *ti(n) see *0jaj. 
25492:392 *0jaj (*ti(n)j2) 
25542:*Өіај (*ti(n)j’) ‘to come to a halt, want to leave (from an awkward situation ?), 
57805:*ti(n)f , *xšnau!
```


## [2026-10-15T02:50:04.593Z] TOOL CALL #77: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification; sed -n 25542,25570p sources/refs/CHEUNG.txt; grep -B2 -A4 \"Middle Persian\" sources/web/cc36ebc3f350537d.txt | grep -v \"^\\s*$\" | head -20"
}
```


### [2026-10-15T02:50:04.989Z] TOOL RESULT

```
*Өіај (*ti(n)j’) ‘to come to a halt, want to leave (from an awkward situation ?), 
embarrasser’ 


*Өгаһ (*trs) 393 


*AVESTAN: ОАу. i@tiejah- [п] ‘abandonment (?)’ (Y 34,8), YAv. iðiiajah-, i0iiejah- 
(n.) ‘abandonment CV (Yt 10.22), ? YAv. tinja ‘to stop, lo!’ (Yt 19.50). 0 On ҮАУ. 
tinja cf. Sims-Williams 1989: 263, but the precise meaning of this interjection is 
uncertain. 

*CHORESMIAN: tynk- ‘to come to a standstill, stop’, (intr./inch.) tx- ‘to stammer, 
speak haltingly’ = Samadi: 206 

*NEIR: ? Oss. I. (rarely) tigyn, D. tegun/tigd ‘to sieve (flour through a sieve)’, ? Wa. 
іыс-Йосі- ‘to stop, stick into (?)’ 

*SANSKRIT: tyaj ‘to leave, dismiss, abandon’ (RV+) = EWAia I: 673 f. 

© It is uncertain whether all these Ir. forms cited here are related to each other. Some 
of them may be indeed related to tyaj ‘to leave, dismiss, abandon’ (R V+), EWAia I: 


673 f. 
*REFERENCES: Abaev, Slovar’ III: 292 f.; Steblin-Kamenskij 1999: 367 


*Orah (*trs) ‘to shake, tremble; to fear; to flee’ 
 Proto-Indo-Iranian *táktas 
 Proto-Iranian *táxtah 
 Middle Persian tʾht' ( /⁠taxt⁠/ ) 
 Classical Persian تخت ( taxt ) bor. 
 Arabic تخت 
 Borrowed from Classical Persian تخت ( taxt ) .
--
 Proto-Indo-Iranian *táktas 
 Proto-Iranian *táxtah 
 Middle Persian tʾht' ( /⁠taxt⁠/ ) 
 Classical Persian تخت ( taxt ) bor. 
 Arabic تَخْت ( taḵt ) 
 North Levantine Arabic تخت 
--
 Proto-Indo-Iranian *táktas 
 Proto-Iranian *táxtah 
 Middle Persian tʾht' ( /⁠taxt⁠/ ) 
 Classical Persian تخت ( taxt ) bor. 
 Ottoman Turkish تخت 
 Borrowed from Classical Persian تخت ( taxt ) .
```


## [2026-10-15T02:50:07.882Z] TOOL CALL #78: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification; grep -n \"Proto-Indo-European\\|Proto-Indo-Iranian \\*\" sources/web/cc36ebc3f350537d.txt | head -8; grep -i \"From\\|Iranian\\|Avestan\\|Persian\\|Sogdian\" sources/web/81278cc75ebe524a.txt | head -30"
}
```


### [2026-10-15T02:50:08.395Z] TOOL RESULT

```
331: Proto-Indo-European *(s)teg- 
332: Proto-Indo-Iranian *táktas 
1054: Proto-Indo-European *(s)teg- 
1055: Proto-Indo-Iranian *táktas 
1084: Proto-Indo-European *(s)teg- 
1085: Proto-Indo-Iranian *táktas 
1146: Proto-Indo-European *(s)teg- 
1147: Proto-Indo-Iranian *táktas
```


## [2026-10-15T02:50:11.347Z] TOOL CALL #79: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification; sed -n 300,335p sources/web/cc36ebc3f350537d.txt | grep -v \"^\\s*$\"; head -5 sources/web/81278cc75ebe524a.txt; grep -c . sources/web/81278cc75ebe524a.txt"
}
```


### [2026-10-15T02:50:11.891Z] TOOL RESULT

```
 Upload file 
 Permanent link 
 Page information 
 Cite this page 
 Get shortened URL 
 Print/export
 Create a book 
 Download as PDF 
 Printable version 
 In other projects
 Appearance
 move to sidebar 
 hide 
 From Wiktionary, the free dictionary
 See also: بخت , بحت , تجب , تحب , بحث , تحت , and ب ح ث 
 Arabic
 [ edit ] 
 Etymology
 [ edit ] 
 Etymology tree
 Proto-Indo-European *(s)teg- 
 Proto-Indo-Iranian *táktas 
 Proto-Iranian *táxtah 
 Middle Persian tʾht' ( /⁠taxt⁠/ ) 
 Classical Persian تخت ( taxt ) bor. 
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/teḱs-
FETCHED: 2026-10-12T18:40:13Z
STATUS: -1
TITLE: 

5
```


## [2026-10-15T02:50:15.973Z] TOOL CALL #80: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; f=$(python3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/tetḱ-\" --note \"page 509, root Tex: PIE *tetḱ- (= Pokorny teks-), descendants Av. taš-, tašta-, NP tašt\" | tail -1); echo $f; head -4 $f; grep -i \"Avestan\\|Persian\\|Sogdian\\|Latin\\|Greek\\|taxt\\|tašt\\|tēš\" $f | head -40"
}
```


### [2026-10-15T02:50:16.840Z] TOOL RESULT

```
/home/sfmqrb/git/rishe-private/data/verification/sources/web/5a3974f806ef2176.txt
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/tetḱ-
FETCHED: 2026-10-15T02:50:16Z
STATUS: 200
TITLE: Reconstruction:Proto-Indo-European/tetḱ- - Wiktionary, the free dictionary
 Latin: tēla , tēlum (or from Proto-Indo-European *tend- )
 Ancient Greek: τέχνη ( tékhnē ) ( see there for further descendants )
 Proto-Iranian: *taštáh 
 Avestan: 𐬙𐬀𐬱𐬙𐬀 ( tašta ) 
 Middle Persian: tšt' ( tašt ) , [script needed] ( tʾšytk /⁠tāšīdag⁠/ ) ( see there for further descendants )
 → Persian: طاس ( tâs ) ( see there for further descendants )
 > ? Latin: testa ( see there for further descendants )
 ^ Beekes, Robert S. P. ( 2010 ), “ τέκτων ”, in Etymological Dictionary of Greek (Leiden Indo-European Etymological Dictionary Series; 10 ), volume II, with the assistance of Lucien van Beek, Leiden, Boston: Brill, →ISBN , page 1460 
 ^ De Vaan, Michiel ( 2008 ), “ texō, -ere ”, in Etymological Dictionary of Latin and the other Italic Languages (Leiden Indo-European Etymological Dictionary Series; 7), Leiden, Boston: Brill, →ISBN , page 619 
 Requests for native script for Middle Persian terms
```


## [2026-10-15T02:50:19.241Z] TOOL CALL #81: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; grep -v \"^\\s*$\" data/verification/sources/web/5a3974f806ef2176.txt | sed -n '/Proto-Indo-European root/,/References/p' | head -80 | cut -c1-200"
}
```


### [2026-10-15T02:50:19.639Z] TOOL RESULT

```
 Terms derived from the Proto-Indo-European root *tetḱ- (61 c, 0 e) 
 *tḗtḱ-ti ~ *tétḱ-n̥ti ( Narten imperfective ) 
 *totḱ-éye-ti ( causative ) 
 Proto-Balto-Slavic: 
 > ? Lithuanian: tašýti 
 *tétḱ-ō ~ *tḱ-nés ( “ carpenter ” ) ( see there for further descendants )
 *tetḱ-(dʰ)lo- ( “ adze ” ) 
 Proto-Balto-Slavic: 
 Proto-Slavic: *tesla , *teslò ( see there for further descendants )
 Proto-Celtic: *tāxslos ( see there for further descendants )
 Proto-Germanic: *þehslō ( see there for further descendants )
 Proto-Italic: 
 Latin: tēla , tēlum (or from Proto-Indo-European *tend- )
 *tetḱ-eh₂ 
 Proto-Germanic: *þehsō 
 Old English: þeox 
 Old High German: dehsa 
 Middle High German: dehse 
 German: Dechse 
 *tetḱ-sneh₂ 
 Proto-Hellenic: 
 Ancient Greek: τέχνη ( tékhnē ) ( see there for further descendants )
 *tetḱ-t-o- 
 Proto-Indo-Iranian: *taćšṭás 
 Proto-Indo-Aryan: *taṭṣṭás 
 Sanskrit: तष्ट ( taṣṭá ) 
 Proto-Iranian: *taštáh 
 Avestan: 𐬙𐬀𐬱𐬙𐬀 ( tašta ) 
 Middle Persian: tšt' ( tašt ) , [script needed] ( tʾšytk /⁠tāšīdag⁠/ ) ( see there for further descendants )
 Parthian: [script needed] ( tʾst /⁠tāst⁠/ ) , [script needed] ( tʾstg /⁠tāstag⁠/ ) 
 → Persian: طاس ( tâs ) ( see there for further descendants )
 → Old Armenian: տաշեմ ( tašem ) ( see there for further descendants )
 Proto-Italic: *testā ( from *tetḱ- teh₂ ) 
 > ? Latin: testa ( see there for further descendants )
 Unsorted formations 
 Proto-Germanic: *þēhtuz [ 11 ] 
 Proto-Albanian: *tēkslā [ 12 ] 
 Proto-Albanian: *tāslā 
 Albanian: tollë 
 Proto-Albanian: *taksjā [ 13 ] 
 Albanian: teshë 
 Northern Kurdish: teşe ( “ form ” ) 
 Zazaki: toşe ( “ form ” ) 
 References
 Proto-Indo-European roots 
 Proto-Indo-European irregularly shaped roots 
 Proto-Indo-European imperfective roots 
 Hidden categories: Pages with etymon 
 Proto-Indo-European entries with etymon 
 Pages with entries 
 Pages with 1 entry 
 Sanskrit terms with non-redundant manual transliterations 
 Requests for native script for Middle Persian terms 
 Requests for native script for Parthian terms 
 This page was last edited on 12 September 2026, at 14:24.
 Definitions and other text are available under the Creative Commons Attribution-ShareAlike License ; additional terms may apply. By using this site, you agree to the Terms of Use and Privacy Policy. 
 Privacy policy 
 About Wiktionary 
 Disclaimers 
 Legal & safety contacts 
 Code of Conduct 
 Developers 
 Statistics 
 Cookie statement 
 Mobile view 
 Search 
 Search 
 Toggle the table of contents 
 Reconstruction:Proto-Indo-European/ tetḱ- 
 Add languages 
 Add topic
```


## [2026-10-15T02:50:24.417Z] TOOL CALL #82: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"Beil'\\|'Beil\\|Axt'\\|'Axt\" HRN.txt | head; grep -n \"teše\\|tese\\b\\|tēše\\|tlse\\|t[eē][sš]e\\b\" HRN.txt HUB.txt | head"
}
```


### [2026-10-15T02:50:24.792Z] TOOL RESULT

```
3534:374. teber, tewer 'Beil', arab. LW. tabar,
3638:387. tes'Axt\
3841:scharfer Schneide'^); phlv. tej (päz. ^öi), ^es 'Axt'
HRN.txt:3838:408. f^;s: *scharf, heftig; schnell', tej 'PfeiF; tese *Axt*2).
HRN.txt:4915:kisver (No. 858), np. tese (No. 408) — phlv. vskar
```


## [2026-10-15T02:50:27.642Z] TOOL CALL #83: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 3636,3644p HRN.txt; sed -n 3836,3856p HRN.txt; awk 'BEGIN{RS=\"\\f\"} /387. tes.Axt/ {print \"leaf387\",NR-1} /408. f\\^;s/ {print \"leaf408\",NR-1}' HRN.txt"
}
```


### [2026-10-15T02:50:28.002Z] TOOL RESULT

```
^J Daneben giebt es auch ein up. terkend^ ierkeude mit gleicher
Bedeutung. FJ (fehlerhaft), FR:— 87 —
387. tes'Axt\
ap. vergl. us^tasana- *Bau; aw. tasa- *Axt*; phlv.
täsltan, tOsUar bezw. taxs° (vergl. aw. 'tmta-), syr.
LW. :it^NlO"nü *Zimmermannsaxt' (de Lagarde, Ges.
Abb. 49); ai. [/^taks^.
V
388. tis *Durst\ tisne {tesne Sahn. I, 59, 481), tisnegl, tesnegi
aw. *tq3ri/a-, vergl. tar, tank (No. 370) ; phlv. terak,
LW. afy. ttra; bei. n. feray (274); siyn. t4r,
408. f^;s: *scharf, heftig; schnell', tej 'PfeiF; tese *Axt*2).
g. ^f/ 'scharf; mäz. tTjf,
ap. vergl. ^i5rra[/a?*rfa-; aw. bröi&rö.]tapJa^ mit
scharfer Schneide'^); phlv. tej (päz. ^öi), ^es 'Axt'
(vd. 14 (24)); ai. [/'tej-, tejati schärfen, scharf sein,
tejas-,
kurd. tt£, tizT; bei. tes: (275); afy. LW. tez, tezal; sar.
teiz, wa;K. tiz,
409. tey *spitz, Schwert', % (nicht belegt).
aw. bi.]taeya- 'zweischneidig'; arm. LW. teg.
kurd. tJ 'Degen ; bei. LW. n. tey 'scharf, schnell;
Schwert' (889).
phlv. HTl (oder wie man transcribiren mag) — vd.
3 (121) == aw. tiyra-y und häufig im Bund. — soll
vielleicht tey sein. Np. tey 'Berggipfel, Höhe', oss. fty,
d. feyä 'Bergrücken (250) gehören ebenfalls hierher
(spezialisirte Bedeutung: Spitze eines Berges).
J.
410. JädU 'Zauberer, Jadül.
leaf387 108
leaf408 113
```


## [2026-10-15T02:50:35.571Z] TOOL CALL #84: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"^taxt \\[\\|^taxt\\b\" NYB_vol2_glossary.txt | head -3; sed -n 3768,3770p NYB_vol2_glossary.txt | cut -c1-600; grep -n \"taxt \\[\" PHD.txt | head -2; grep -o \"taxt \\[[^]]*\\][^.]*\\.\" PHD.txt | head; grep -n \"Thron\" HRN.txt | head -5"
}
```


### [2026-10-15T02:50:36.075Z] TOOL RESULT

```
taxtak [t’htk'] tablet, pl. —-iha 113!; board for the game of tric-trac 1202-15, — NP tazxtah.
täxtan [t’htn'] tāc- [t’c-] to run 319. 2819, 9817. — Av. täcaya- intens. of tak-, v. tacitan; NP tartan tüz-; v. also vitāxtan.
täyitan [t?dytn'] to be capable, to suffice: api-m-isdn nē täyit zor (and as-to-me-for- them power did not suffice —) they did not prevail against me 1286-7, a literal translation of Syr w-la ’etm'siw hail(i) (Barr) — täy- < tāv-, ci MPrth Pwg ‘mighty’; alternating with tahé- in tahé- kar (g. v.); v. further pattàhik and s. v. pattān.
595:~ih: bitterness. taxt [2А | N ~] throne. ~ag [-#! | N ~a] tablet, plank, (chess) board. taxtan, taz- [Phtn', tc- | M rem, tz-] run, flow. išnīh : flow. tāxtan, taz- [?Аїп!, Pc- | M Рс-, N ~] cause to run, flow; chase; pour. taxt-gàh [?hig’h | N <] couch. taz-, —išnih, v. taxtan. táz-, v. tāxtan, tazāģ [tc’k'] flowing, running. tāzānaģ [P enh | N tāz(y)āna] whip. tazënidan, tazën- [tcyn-ytn'] = tāxtan. tazidan, taz- [tc-ytn'] = taxtan. Itázig [Pcyk! | N tázi] swift, fast. "Táüzig [Pcyk! | N tāzi] Arab. tēmār [tym] | M tym’r, N ~] sorrow, grief, care. ltërag [tylk' | N tēra] dark, turbid. *térag [tylk'] (mountain) peak, summit. téx [tyh | N téy] sharp edge, ridge; ray. Mēz [tye | M tyz, N ~] quick. ~ih: speed. *téz [tye | (P tyj), N ~] sharp. ~ih: sharpness. *tidag [tytk' | (N dida)] pupil (of eye). tigr [HTY A < А Шу; tgl | M tygr, N tir] arrow. *tihóg [tyh:wk! | N tihi] small grey partridge. tir, v. tigr. Tir [tyl | M tyr, N ~] a god (confused with Tištar); astr. Mercury; cal. 4th month; 13th day. tis [MNDOM < А mnd‘m; ts | M, J tys] thing, affair. «iz [-c | M -yc] (with a negative) по... at all. tišn [tyšn!] thirst. tišnag [tyfnk! | M tyšng, N ~a] thirsty. ~th: thirst. Tištar [гуй | № ~] astr. Sirius. të [LK < A l-k | M tw, N tu] thou, thee. *tóf [twp | N to] layer. tóhmag [twhmk' | M twhmg, N tuxma] seed; stock, family. tom [t(w)m | M tm, N tam] darkness. -tom [-twm | (M. -dwm)] suffix forming superlative adjectives. tóm [twm | (M twhm, N tuxm)] seed, family. tórag [twlk' | N tora] jackal. tūšag [twšk! | N tófa] provisions. tóxtan, töz- [twhtn', twc- | M twz-, N ~] atone, expiate. ~išn: atonement, expiation. tóz [twe | N ~] bark, skin.
taxt [2А | N ~] throne.
1575:V. u.); Thron*.
7736:889. ffäh *Ort (in Comp.) ; Thron*.
7737:ap. gä&U' 'Ort; Thron', vergl. /7afja(>[}/«(5(</ ; aw. gätn-
7738:Ort; Thron'; phlv. gas\ ai. gütü- 'Gang, Bahn, Kaum*,
9516:sieben Throne* erklärt.
```


## [2026-10-15T02:50:44.316Z] TOOL CALL #85: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; for f in bae13ccb0ca90d8c 77d9f6eba65c4ee1 b29d7e690d00cb0a 4cfe72023ac836bd bdeca73d2abb2ad2 9c200e2bb393e5be c5d41015a28f7d02; do echo \"=== $f $(sed -n 3p $f.txt)\"; grep -i -m3 \"from\\b.*\\(Arabic\\|Persian\\|Latin\\|Greek\\|French\\)\" $f.txt | cut -c1-500; done"
}
```


### [2026-10-15T02:50:44.971Z] TOOL RESULT

```
=== bae13ccb0ca90d8c STATUS: -1
=== 77d9f6eba65c4ee1 STATUS: -1
=== b29d7e690d00cb0a STATUS: 200
 "person skilled in the art of building, one who plans and designs buildings and supervises their construction," 1560s, from French architecte , from Latin architectus , from Greek arkhitekton "master builder, director of works," from arkhi- "chief" (see archon ) + tekton "builder, carpenter" (from PIE root *teks- "to weave," also "to fabricate").
 one of the nine chief magistrates of ancient Athens, 1650s, from Greek arkhon "ruler, commander, chief, captain," noun use of present participle of arkhein "be the first," thence "to begin, begin from or with, make preparation for;" also "to rule, lead the way, govern, rule over, be leader of," a word of uncertain origin.
 1640s ( architectonical is from 1590s), "pertaining to architecture," from Latin architectonicus , from Greek arkhitektonikos "pertaining to a master builder," from arkhitekton "chief workman" (see architect ). The metaphysical sense, "pertaining to systematization of knowledge," is from 1801.
=== 4cfe72023ac836bd STATUS: -1
=== bdeca73d2abb2ad2 STATUS: -1
=== 9c200e2bb393e5be STATUS: -1
=== c5d41015a28f7d02 STATUS: 200
```


## [2026-10-15T02:50:48.106Z] TOOL CALL #86: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; grep -n \"force\\|exists\" tools/fetch_source.py | head; sed -n 1,8p data/verification/sources/web/bae13ccb0ca90d8c.txt"
}
```


### [2026-10-15T02:50:48.462Z] TOOL RESULT

```
46:    if os.path.exists(path) and time.time() - os.path.getmtime(path) < 86400:
URL: https://www.etymonline.com/word/tass
FETCHED: 2026-10-15T02:49:38Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 403: Forbidden
```


## [2026-10-15T02:50:52.624Z] TOOL CALL #87: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; for w in tass test technique text tissue tasse \"تکنیک\"; do f=$(python3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/$w\" --note \"page 509, root Tex, English/French/Persian $w\" | tail -1); echo \"=== $w $(sed -n 3p $f)\"; grep -A2 \"^ Etymology\" $f | grep -v \"^\\s*$\\|Etymology\\|edit\\|^ [0-9.]* $\" | head -3 | cut -c1-500; done"
}
```


### [2026-10-15T02:51:03.456Z] TOOL RESULT

```
=== tass STATUS: 200
--
--
--
=== test STATUS: 200
--
--
--
=== technique STATUS: 200
--
--
--
=== text STATUS: 200
--
--
--
=== tissue STATUS: 200
--
=== tasse STATUS: 200
--
--
--
=== تکنیک STATUS: 200
--
```


## [2026-10-15T02:51:06.063Z] TOOL CALL #88: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; for w in tass test technique text tissue tasse \"تکنیک\"; do f=$(grep -l \"^URL: https://en.wiktionary.org/wiki/$w$\" *.txt | head -1); echo \"=== $w $f\"; grep -m4 \"From\\|Borrowed from\\|from Middle\" $f | cut -c1-400; done"
}
```


### [2026-10-15T02:51:07.244Z] TOOL RESULT

```
=== tass 0b8ce3a33a4fb287.txt
 From Wiktionary, the free dictionary
 Partly from Middle English tas ( “ heap ” ) , from Old French tas ( “ heap ” ) , from Frankish *tas ( “ mass, pile ” ) ; and partly from Middle English taas ( “ heap, mow of corn ” ) , from Old English tas ( “ heap, mow of grain ” ) ; both from Proto-Germanic *tasaz , *tassaz ( “ heap, mow, stack ” ) , from Proto-Indo-European *deh₂y- ( “ to divide, split, section, part, separate ” ) . 
 From Middle English *tasse , from Old French tasse (Modern French tasse ( “ cup, cupful ” ) ). Cognate with Dutch tas ( “ cup ” ) , German Tasse ( “ mug ” ) . Doublet of tazza .
 From Middle English tasse , tache , from Old French tasse , tasche ( “ purse; pouch ” ) , from Frankish *taskā ( “ pouch ” ) , from Proto-Germanic *taskǭ , cognate with Old High German tasca ( “ pouch ” ) , German Tasche ( “ pocket; pouch ” ) .
=== test 4a33b4ca40159923.txt
 From Wiktionary, the free dictionary
 From Middle English test , teste , from Old French test , teste ( “ an earthen vessel, especially a pot in which metals were tried ” ) , from Latin testum ( “ the lid of an earthen vessel, an earthen vessel, an earthen pot ” ) , from *terstus , past participle of the root *tersa ( “ dry land ” ) . See terra , thirst . The examination sense came via metaphor of the metallurgical sense: the way a m
 From Middle English teste , from Old French teste , test and Latin testis ( “ one who attests, a witness ” ) .
 Borrowed from English test .
=== technique 27b8ba3689cbd856.txt
 From Wiktionary, the free dictionary
 Borrowed from French technique ( “ technicality; branch of knowledge ” ) , noun use of technique ( “ technical ” ) , from Ancient Greek τεχνικός ( tekhnikós , “ of or pertaining to art, artistic, skilful ” ) , from τέχνη ( tékhnē , “ art, handicraft ” ) . Doublet of technic .
 Borrowed from Ancient Greek τεχνικός ( tekhnikós , “ relating to art, artistic, skilful ” ) , from τέχνη ( tékhnē , “ art, handicraft ” ) .
=== text ab6b00e325bf7cae.txt
 From Wiktionary, the free dictionary
 From Middle English text , from Old French texte , from Medieval Latin textus , from Latin textus ( “ style or texture of a work ” ) , perfect passive participle of texō ( “ to weave ” ) . Cognate to texture .
 Borrowed from Medieval Latin textus ( “ text ” ) , from Latin textus , perfect passive participle of texō ( “ weave ” ) . First attested in the 14th century. [ 1 ] 
 From Persian تخت ( taxt ) .
=== tissue a591de1b67c5acdd.txt
 From Wiktionary, the free dictionary
 From Middle English tissu , from Old French tissu ( “ woven ” ) , past participle of tistre ( “ to weave ” ) , from Latin texō ( “ to weave ” ) .
 Categories : English terms inherited from Middle English 
 English terms derived from Middle English 
=== tasse 25236ece04b2ef9c.txt
 From Wiktionary, the free dictionary
 Inherited from Middle English tasse ( “ armor plate protecting the hip ” ) , derived from Old French tasse , tasche ( “ purse; pouch ” ) , derived from Frankish *taskā ( “ pouch ” ) , derived from Proto-Germanic *taskǭ . Cognate with Old High German tasca ( “ pouch ” ) , German Tasche ( “ pocket; pouch; bag ” ) , Dutch tas ( “ bag ” ) .
 From Middle French tasse (14th c.), from Arabic طَاس ( ṭās ) (a shortening of طَسْت ( ṭast ) ), from Middle Persian tšt' ( tašt ) , ultimately from the past participle of the Proto-Iranian verb *taš- ( “ to make, construct; to cut ” ) , from Proto-Indo-Iranian *tā́ćšti , from Proto-Indo-European *tḗtḱ-ti ~ *tétḱ-n̥ti , from *tetḱ- ( “ to create ” ) .
 Categories : English terms inherited from Middle English 
=== تکنیک f49f283d37e27ae1.txt
 From Wiktionary, the free dictionary
 Borrowed from French technique .
```


## [2026-10-15T02:51:24.583Z] TOOL CALL #89: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD; grep -n \"tekp\\|tekþ\\|teks-\\|tek\\^-\\|tekth\" WLD_Bd1_pages.txt | head; grep -n \"tieg\\|tyeg\\|tjeg\" WLD_Bd1_pages.txt | head"
}
```


### [2026-10-15T02:51:25.012Z] TOOL RESULT

```
67613:Wz. oder der Wz tekp- .,zimmern                                                     '    anzuschlieBen.
67717:(*teks- „zimmern“) den Namen haben •wird, ist wahrscheinlich „fett“ von
68692:     tekp-
2301:         (          :   ueg-, altest atieg-) „Kochtopf,             Warmepfanne“.
3555:tiegel“       ist       nach Solmsen Unters. 46 a 1          als   rgyavov mifiverstandenes           x g-
4634:ibuks, ippihhon stellt Brugmann II 2 1, 507 f. wieder got. xb-dalja m. ,Abstieg“ und —
9375:„Abstieg“,         ijanetn            (Aor. s)               „herabkommen,                       herabsteigen“,                 ijaranlc         pi.
11098:stieg,    Abhang“,                                         eofnt eofot „Schuld“
23335:   Air. fen „Art Wagen" {* tiegh-no-     vgl. ai. vahana- und ahd. tvagan)
56802:247, Falk-Torp   u, knikke s. krok-; iiber ahd. kriiscl „Schmelztiegel" usw.
63014:                              ging, bestieg" einzusetzendes pgooezo
70571:746                                                        tiegj-      — tuaq-, tuenq-
70585:tiegS- „scheu vor etwas zuriicktreten oder auffahren".
```


## [2026-10-15T02:51:28.036Z] TOOL CALL #90: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD; sed -n 68690,68720p WLD_Bd1_pages.txt | cut -c1-200; sed -n 70585,70595p WLD_Bd1_pages.txt | cut -c1-220; awk 'NR<=68692 && /pdf page|leaf/ {p=$0} NR==68692{print p}' WLD_Bd1_pages.txt"
}
```


### [2026-10-15T02:51:28.741Z] TOOL RESULT

```
s.      „zimmern") kann auch * tend-slom sein, wie auch tensa „Art Wagen
     tekp-
oder Schleife, Prozessions- oder Gotterwagen" das subst. Fem. des Ptc.
tcnsus; auch temo, -on is „Deichsel“ kann auf * lens-mo- oder *ten(d)-smo-
beruhen (vgl. pr. teansis), freilich aber allenfalls auch zu tondeo revdco          ,


gehoren (vgl. o. zu tonsa; noch anders Curtius 219, Zup. G. 188, zw. Hart-
mann Gl. 4, 159ff: zu texo, ai. tdksati „behaut, schnitzt" usw.).
1.   ter- „zappeln, zittern".
     Ai. tarald-h „zitternd. zuckend, unstet"; alb. (Jokl. SBAkWien           168, I 90)
tartalis      „zapple“   (aus redupl. *tar-tav-is\.      Als Erw. aus idg.   ter-       diirfen
728                                                                   ter-



tr-cm -, tr-es- (Kombinationsform *trems -), tr-ep- „trippeln, zittern“ gelten,
s. Persson Wzerw. 51, 68, Beitr. 556, 572, 584.



2. ter-          „zart,       schwach"              (zu   ter- „reiben“,             s.   d. ;       als   „ab-,        aufgerieben,
        geschwacht"; anders iiber die Bed.-Entw. Trautmann BB. 29, 309 ff.).
     Gr.       t EQt]v   ,,zart“,        sabin.      terenum          ,,molle“,       lat.   (mit nacb              tennis         festge-
wordener Umstellung)                         tencr, -a,            -uni „zart, weich“.                 Yon     der M-Basis gr.
r egv ao&sveg, Xenzov Hes.,                           zegveg t'nnoi „abgetriebene Pferde" (zegvoxero
Izelgszo Hes.: ztgv                  = uedvoxo)               :   i.ndr ;    s.   Bgm. II 2 1, 182), zsgvvi)?                  •   rergtp-
uf.vog dvog, xai yegcov, i/ dvaavaXynzog yegcov Hes., ai. tdruna-h „jung,
zart" (m. f. „Jiingling, Madchen, n. SchoBling, Halm“, ay. taurima- ,.jung",
osset. tar in „Knabe" (Ws. Miller Spr. d. Oss. 19); sebr unsicher wird lat.
tiegS- „scheu vor etwas zuriicktreten oder auffahren".
     Ai. tyajati            (= gr. aefico) „begibt sieh weg von etwas, verlaBt, steht von
etwas zuriick",                       mit ni- „verscheuchen, verdrangen",                                  mit nis-       „hinaus-
treiben, verjagen", ptc. tyakta- (= gr. aemog , nom. ag. tyaktar- (= gr. dso-
asnrcoQ             „Anbeter                der       Gottheit"),          kaus. tijdjdyati „macht zuriicktreten",
tydjas-    „das n.                    Imstichlassen,                Not,       Gefahr"    = av. idyajah-, rdytjah-                n.

..Not, Gefahr";                       ai.     fydga-h          ,,das    Verlassen, VerstoBen, Meiden; Hingabe,
Freigebigkeit".
  Gr. oipico (act. nur praes. und impf.), oefPoyai horn. „(die Gotter) scheuen",
nacbhom. „(die Gotter) verehren, ehren", oemog „(verehrt =) ehrwiirdig,
  Arm. cov, aisl. leaf „Meer"? s. u. gep(]i)-, geb(h)~ ..Kiefer".
```


## [2026-10-15T02:51:32.748Z] TOOL CALL #91: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD; grep -n \"^ *tekp-\\|tekp- „\\|tekp-  *„\\|tekþ\" WLD_Bd1_pages.txt | head; grep -n \"Axt\\b.*tasa\\|tasa- .*Axt\\|tasta-\\|taSta\\|tasta\\b\" WLD_Bd1_pages.txt | head -5"
}
```


### [2026-10-15T02:51:33.126Z] TOOL RESULT

```
68692:     tekp-
67620:Bsl. Wb. 319f.),           Ptc tasta-h
67621:                                 .      tasta- und ta'sta- Ptc.; aueh tasta- n.
67632:staltet“,      m. „Axt“, np. tas ds., rnp. tasltan ,,zimmern“, ap. us-tasana
67653:Yf. LEWb. 2 s. v. und vgl. oben av. tasta-), vielleicht auch telum „Fern-
```


## [2026-10-15T02:51:35.335Z] TOOL CALL #92: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD; sed -n 67608,67660p WLD_Bd1_pages.txt | cut -c1-220"
}
```


### [2026-10-15T02:51:35.689Z] TOOL RESULT

```
                                                                   '




Wz. oder der Wz tekp- .,zimmern                                                     '    anzuschlieBen.
                                             tekf       teg-, tag-                                             717

tek|>- „zimmern,               Holz behauen und damit bauen“.
  Ai. taksati „behaut, bearbeitet, zimmert, verfertigt mit Kunst“, tdsti ds.
fdehnstufig          wie   lett.    neben tesu, test. Btbl. IF. 3, 53. Trautmann
                                     tesu, test
Bsl. Wb. 319f.),           Ptc tasta-h
                                 .      tasta- und ta'sta- Ptc.; aueh tasta- n.
                                              (av.
„Tasse, Schale“, s. Bthl. Wb. 646 m. Lit., Vf. LEWb. 2 u. testa lat. textus,                      ;


wenn nicbt aus *t exit os), ai. taksan- m. „Zimmermann“ (= av. tasan- „Bildner,
Schopfer    11
                 ,
                     gr. text an’), fem. Ink hit        (:   gr. xey.xaiva), tastar-         „Zimmermann“
(= lat. textor)
  av. tasaiti „zimmert, schneidet mit Messer oder Axt zu, verfertigt, ge-
staltet“,      m. „Axt“, np. tas ds., rnp. tasltan ,,zimmern“, ap. us-tasana
            taka-
„Treppenhaus“ (*„Aufbau“).
  Gr. xexxcov „Zimmermann“, fem. xexxaiva, xtyvi] „Handwerk, Kunst / List“
(*xe£va aus alterem *t£*t[«] a-va, s. Bechtel Lex. 311); lat. texo, -ere, -ui -turn
„weben, flechten“, gelegentlich „bauen“ (s. aucb Persson Beitr. 477 die Bed.                          ;


„weben, flechten“ wohl durch Aufsaugung eines zu teq- „weben“ gehorigen
Wortes; Hartmann Gl. 4, 1 59 ff. sucht die Yermittlung unterm Begriff der
Kunstfertigkeit im               allgemeinen, vgl. gr. xiyyr]), tela              „Gewebe“ t*teksld —
slav.   tesla,       ahd. dehsala),        subtilis   ( *-tvxlis     „fein,   diinn,     zart;        feinfiihlig,
scharfsinnig",subtemen „Einschlag, Eintrag im Gewebe Gewebe“ (kaum                   ;



hierher aber als „zubehauen“, term „Deicbsel“, s. u. *tens- „dehnen“; iiber
tignurn „Bauholz, Balken“ s. u. *steg- „Stange“)    testa „Geschirr“ (siehe
                                                                          ;


Yf. LEWb. 2 s. v. und vgl. oben av. tasta-), vielleicht auch telum „Fern-
waffe, WurfgeschoS“ (als „kundig zugeschnitzt, gearbeitet, gedrecbselt“
oder eher aktiv als ursprgl. „zum Holzarbeiten verwendbarer Schaber“;
s. Curtius 219, Hartmann Gl. 4, 1 59 ff. 6, 346               ;
                                                                         =
                                                    Wood Cl. Phil. 7, 331;
gr. Tofor „Bogen“, ibd., ware hochstens als r OKx{e)a-ov oder *xoy.xiov
mit dem y.x von xey.xcov in Einklang zu bringen. Fur telum erinnert
```


## [2026-10-15T02:54:34.803Z] TOOL CALL #93: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/p509; cat > /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/p509/build-509.py <<'PYEOF'\nimport json\nW=\"https://en.wiktionary.org/wiki/\"\nTETK=W+\"Reconstruction:Proto-Indo-European/tetḱ-\"\nTYEG=W+\"Reconstruction:Proto-Indo-European/tyegʷ-\"\nPOK_TEKS={\"src\":\"POK\",\"where\":\"pp.1058-1059 s.v. tek̂þ- (POK_full.txt line 85033)\",\"stance\":\"supports\",\"note\":\"'Meaning: to plait; woodwork; carpenter' ... 'Avestan tašaiti 'zimmert, cuts, slices to, verfertigt', taša- m. 'axe', np. taš ds., mp. tāšīdan ... ap. us-tašana 'staircase'' ... 'tašta- n. cup, bowl' ... 'gr. tektōn carpenter ... technē handwork, art' ... 'Latin texo, -ere ... testa 'Platte, shard, bowl' ... (compare above Avestan tašta-)'.\"}\nWLD_TEKS={\"src\":\"WLD\",\"where\":\"Bd. I p.717 s.v. tekþ- (WLD_Bd1_pages.txt line 67614)\",\"stance\":\"supports\",\"note\":\"'tekþ- „zimmern, Holz behauen und damit bauen“. Ai. takṣati ... av. tašta- n. „Tasse, Schale“, s. Bthl. Wb. 646 ... av. tašaiti „zimmert, schneidet mit Messer oder Axt zu“, taša- m. „Axt“, np. taš ds., mp. tāšītan „zimmern“ ... Gr. tektōn, technē; lat. texo „weben, flechten“, gelegentlich „bauen“ ... testa „Geschirr“ (vgl. oben av. tašta-)'.\"}\nAHD_TEKS={\"src\":\"AHD\",\"where\":\"Watkins 1985 p.69 s.v. teks- (AHD_watkins1985.txt line 1074)\",\"stance\":\"supports\",\"note\":\"'teks-. To weave; also to fabricate, especially with an ax ... 1. Latin texere, to weave, fabricate: TEXT, TISSUE; CONTEXT, PRETEXT ... 3. *teks-on- ... Greek tektōn, carpenter, builder: TECTONIC; ARCHITECT. 4. *teks-nā- ... Greek tekhnē, art, craft, skill: TECHNICAL ... [Pok. tekþ- 1058.]' (no Iranian items, no TEST).\"}\nKLN_TEXT={\"src\":\"KLN\",\"where\":\"1966 s.v. text (KLN_1966.txt line 38804)\",\"stance\":\"supports\",\"note\":\"'L. textus ... texere, to weave, plait, fit together, which is cogn. with OI. takṣati ... Avestic taš-, to cut, carve, tasha, ax, hatchet, Gk. tektōn carpenter, technē (for *teks-nā) art ... All these words derive fr. I.-E. base *tekþ-, *tekh-, to build (of wood), carpenter; to weave'.\"}\ne0nodes=[]\ndef N(id,lang,words,verdict,der,derfa,sources,ref_check,consulted,**kw):\n    d={\"id\":id,\"lang\":lang,\"words\":words,\"verdict\":verdict,\"derivation\":der,\"derivation_fa\":derfa,\"sources\":sources,\"ref_check\":ref_check,\"consulted\":consulted}\n    d.update(kw); return d\n\ne0nodes.append(N(1,\"Avestan\",\"taš; taša; tašta\",\"confirmed\",\n \"Avestan taš- 'to cut to shape, carve (with knife or axe); fashion, create' (Bartholomae col. 645: Praes. taša-, PPP tašta-) continues Proto-Iranian *taš- < Proto-Indo-Iranian *tā́ćšti < PIE *tetḱ-/*teks- (the cluster *tḱ/*kþ gives Indic kṣ, Iranian š); taša- m. 'axe' (Vd 14.7) is the thematic agent noun 'cutter', and tašta- n. 'bowl, cup' (Bartholomae 646) is the substantivised past participle 'something fashioned/hollowed out'. Cheung 2007 (*taš) and Wiktionary list exactly these Avestan forms under PIE *tetḱ-.\",\n \"اوستایی taš- «بریدن و تراشیدن با کارد یا تبر، ساختن، آفریدن» از ریشهٔ ایرانی باستان *taš- و هندواروپایی آغازین *tetḱ- (teks- پوکورنی) است؛ خوشهٔ همخوانی *tḱ در ایرانی به š بدل شده است. taša- «تبر» نام‌ابزارِ «بُرنده» از همین ریشه است و tašta- «تشت، کاسه» در اصل صفت مفعولی «تراشیده، ساخته‌شده» است. ادعای نورایی درست است (بارتولومه، پوکورنی، والده‌ـپوکورنی، کلاین، چونگ).\",\n [TETK],\n [{\"ref\":\"POK:1058\",\"status\":\"supports\",\"note\":\"POK_full.txt line 85033ff.: 'Avestan tašaiti 'zimmert, cuts, slices to, verfertigt', taša- m. 'axe' ... tašta-; also tašta- n. 'cup, bowl''.\"},\n  {\"ref\":\"KLN\",\"status\":\"supports\",\"note\":\"Klein 1966 s.v. text (line 38804): 'Avestic taš-, to cut, carve, tasha, ax, hatchet'; s.v. test (line 38729): 'prob. cogn. with Avestic tashta-, cup'.\"},\n  {\"ref\":\"HRN\",\"status\":\"supports\",\"note\":\"Horn no. 387 (p.87, leaf 108): 'taš 'Axt' ... aw. taša- 'Axt'; phlv. tāšītan'; no. 389: 'tašt 'Becken' ... aw. tašta- 'Schaale, Tasse''.\"}],\n [{\"src\":\"BRT\",\"where\":\"col. 645 s.v. taš- / taša- (BRT.txt lines 12125-12138)\",\"stance\":\"supports\",\"note\":\"'taš- V. 'zuschneiden' ... mit Messer oder Axt ... insbes. 'schnitzen sva. verfertigen, gestalten, schaffen'' ; 'taša- m. 'Axt': V.14.7. Zum V. taš-. — np. taš'.\"},\n  WLD_TEKS,\n  {\"src\":\"CHEUNG\",\"where\":\"pp.384-385 s.v. *taš (CHEUNG.txt line 25055ff.)\",\"stance\":\"supports\",\"note\":\"'MIDDLE PERSIAN: BMP t'š- /tāš-/ to cut, cleave; create ... SOGDIAN: t'š to cut ... PIE *tetK- to construct, build by cutting = LIV 638 f. | Pok.: 1058 f.'\"}]))\n\ne0nodes.append(N(2,\"Persian\",\"tîšeh; taxteh; tašt; tâs\",\"disputed\",\n \"tašt 'basin, wash-tub' is secure: Av. tašta- 'bowl' > MP tašt [tšt'] 'bowl' (MacKenzie p.82; Nyberg p.201) > NP tašt, with no sound change but loss of the final vowel. tâs (طاس/تاس) 'cup, bowl' belongs here too, but indirectly: Arabic ṭast/ṭašt was borrowed from MP tašt and shortened to ṭās, which Persian borrowed back (Mo'in: «طاس: معرب تاس»; Wiktionary طاس: 'shortening of ṭast, from Middle Persian tašt'); Wiktionary also lists a Parthian tāst as the direct source of Persian tās. tîšeh 'adze, hatchet' is only plausibly from this root: no MP *tēšag is recorded, a derivation from Av. taša- 'axe' would need an unexplained ā/a > ē/ī, and Horn (no. 408) instead puts tēša 'Axt' with tēz 'sharp' (PIE *(s)teig-), citing Pahlavi tēš 'Axt'. taxteh 'board, plank' is MP taxtag 'tablet, plank, board' (MacKenzie, Nyberg), a -ag derivative of taxt 'throne'; *taš-ta- would have given tašt (as tašt itself shows), not taxt, and Wiktionary derives taxt from Proto-Iranian *táxtah < PIE *(s)teg-, not from *tetḱ-. So taxteh does not belong to this root, and the node is disputed on that word.\",\n \"«تشت» از فارسی میانه tašt «کاسه» و اوستایی tašta- (صفت مفعولی «تراشیده») است و ادعای نورایی دربارهٔ آن درست است. «طاس/تاس» نیز به همین ریشه می‌رسد، اما از راه عربی: عربی طَست/طشت از tašt پهلوی گرفته و به طاس کوتاه شده و فارسی دوباره آن را گرفته است (معین: «طاس معرّب تاس»). پیوند «تیشه» با اوستایی taša- «تبر» با احتیاط پذیرفتنی است، زیرا صورت پهلوی آن ثبت نشده و هرن آن را با «تیز» هم‌ریشه می‌داند. «تخته» از فارسی میانه taxtag و آن از taxt «تخت» است؛ از *taš-ta- صورت tašt («تشت») به دست می‌آید نه taxt، پس پژوهش امروزی «تخته» را از این ریشه نمی‌داند.\",\n [W+\"تخته\",W+\"تخت\",W+\"طاس\",TETK],\n [{\"ref\":\"IEC:1374,1409\",\"status\":\"not_checked\",\"note\":\"Mann's IEC is alphabetical by PIE root; pages 1374/1409 were not located in the local IEC.txt (two printed pages per leaf, OCR noisy), so this ref was not verified for the Persian words.\"},\n  {\"ref\":\"MON\",\"status\":\"partial\",\"note\":\"Mo'in (MON_2vol_Adena_v1_djvu.txt): 'تیشه: ... افزار آهنی نجاران' (line 45620); 'تشت: ... ظرفی فلزی بزرگ و پهن' (line 40761); 'تخته: ... قطعه چوب پهن' (line 38829); 'طاس: [معر. تاس] طشت کلان' (line 91564). Meanings confirmed and طاس marked as an Arabicised تاس; the entry text gives no Old Iranian etymon for the others.\"}],\n [{\"src\":\"HRN\",\"where\":\"no. 389, p.87 (leaf 108)\",\"stance\":\"supports\",\"note\":\"'389. tašt 'Becken, Untertasse', tašte, arab. LW. ṭast; aw. tašta- 'Schaale, Tasse'; phlv. tašt ... bel. LW. tās (aus arab. ṭās)'; footnote: 'Hieraus auch arm. tas, ital. tazza, franz. tasse, nhd. Tasse'.\"},\n  {\"src\":\"HRN\",\"where\":\"no. 408, p.92 (leaf 113)\",\"stance\":\"contradicts\",\"note\":\"'408. tēz 'scharf ...', tēj 'Pfeil'; tēše 'Axt' ... phlv. tēj, tēš 'Axt' (vd. 14)': Horn puts tēše with tēz 'sharp', not with Av. taša-.\"},\n  {\"src\":\"HUB\",\"where\":\"§129, p.236 (leaf 246)\",\"stance\":\"supports\",\"note\":\"'tēša 'Beil' = zd. taša-, arm. tašem 'behaue'; tašt 'Becken' = zd. tašta-': Hübschmann does derive tēša from taša- (and tašt from tašta-).\"},\n  {\"src\":\"PHD\",\"where\":\"p.82 (leaf 103)\",\"stance\":\"partial\",\"note\":\"'tašt [tšt' | N ~] bowl'; 'taxt [... | N ~] throne. ~ag [... | N ~a] tablet, plank, (chess) board'; 'tāšīdan, tāš- cut, cleave; create'. No *tēšag is listed.\"},\n  {\"src\":\"NYB\",\"where\":\"Part II p.201 (leaf 209)\",\"stance\":\"partial\",\"note\":\"'tašt [tšt'] bowl — Av. (646) tašta-; NP tašt; Arab. lw. ṭast; Fr tasse = German Tasse'; 'taxtak [t'htk'] tablet ... board for the game of tric-trac — NP taxtah' (no etymology linking taxt to taš-).\"},\n  {\"src\":\"CHEUNG\",\"where\":\"p.385 s.v. *taš\",\"stance\":\"partial\",\"note\":\"Lists 'NP tāš 'hatchet, adze'' under *taš but neither tīše nor taxt.\"},\n  {\"src\":\"ARY\",\"where\":\"pdf page 189 (printed 190), headword تخشا/تخشیدن (ARY_latin_index_pages.txt line 5420ff.)\",\"stance\":\"silent\",\"note\":\"Aryanpur files the teks- cognates (Av. TASHAITI, Pahl. TASH-, Gk. TEKTON, Lat. TEXO/TEXERE, Fr. TISSER) under تخشیدن; no entry for تیشه/تخته/تشت was found in the OCR.\"},\n  {\"src\":\"BQT\",\"where\":\"not located\",\"stance\":\"silent\",\"note\":\"Persian-script grep of the BQT OCR for تیشه/تشت/تخته was unusable (OCR merges columns); no footnote was found.\"}]))\n\ne0nodes.append(N(3,\"Arabic\",\"\",\"confirmed\",\n \"Pass-through node for Arabic ṭast / ṭašt 'basin, bowl', borrowed from Middle Persian tašt with emphatic ṭ, and its shortened form ṭās (pl. ṭāsāt) 'cup, drinking bowl'. Arabic ṭās is the form that reached the Romance languages in the Middle Ages.\",\n \"این گره نمایندهٔ عربی طَست/طَشت «تشت» است که از tašt پهلوی وام گرفته شده و با ط نوشته می‌شود، و صورت کوتاه‌شدهٔ آن طاس «جام، کاسه». همین طاس عربی در سده‌های میانه به زبان‌های رومیایی رسید. ادعای نورایی درست است (هرن، نیبرگ، ویکی‌واژه).\",\n [W+\"طاس\",W+\"tasse\"],\n [{\"ref\":\"(none)\",\"status\":\"not_checked\",\"note\":\"node carries no reference of its own\"}],\n [{\"src\":\"HRN\",\"where\":\"no. 389, p.87\",\"stance\":\"supports\",\"note\":\"'arab. LW. ṭast ... (aus arab. ṭās)'.\"},\n  {\"src\":\"NYB\",\"where\":\"Part II p.201\",\"stance\":\"supports\",\"note\":\"'tašt ... Arab. lw. ṭast; Fr tasse = German Tasse'.\"},\n  {\"src\":\"KLN\",\"where\":\"1966 s.v. tass (line 38270)\",\"stance\":\"supports\",\"note\":\"'F. tasse ... fr. Arab. tassah, tass, fr. Pers. tasht, cup, saucer'.\"}]))\n\ne0nodes.append(N(4,\"French\",\"\",\"confirmed\",\n \"Pass-through node for (Middle) French tasse 'cup' (14th c.), from Arabic ṭās(a); its cognates Old Provençal tassa, Italian tazza and Spanish taza came by the same Arabic route, through Sicily, Spain and Mediterranean trade.\",\n \"این گره نمایندهٔ فرانسوی tasse «فنجان» (سدهٔ چهاردهم) است که از عربی طاس گرفته شده؛ ایتالیایی tazza و اسپانیایی taza نیز از همین راه آمده‌اند. ادعای نورایی درست است (کلاین، هرن، ویکی‌واژه).\",\n [W+\"tasse\"],\n [{\"ref\":\"(none)\",\"status\":\"not_checked\",\"note\":\"node carries no reference of its own\"}],\n [{\"src\":\"KLN\",\"where\":\"1966 s.v. tass (line 38270)\",\"stance\":\"supports\",\"note\":\"'MF. (= F.) tasse, cup, fr. OF., fr. Arab. tassah, tass, fr. Pers. tasht ... Cp. OProvençal tassa, It. tazza, Sp. taza'.\"},\n  {\"src\":\"HRN\",\"where\":\"no. 389 footnote, p.87\",\"stance\":\"supports\",\"note\":\"'Hieraus auch arm. tas, ital. tazza, franz. tasse, nhd. Tasse (Hübschmann, ZDMG. 35, 129)'.\"}]))\n\ne0nodes.append(N(5,\"English\",\"tass\",\"confirmed\",\n \"English tass 'small cup, drinking cup; a small draught' (Scots also tassie) comes from Middle English *tasse < Old/Middle French tasse < Arabic ṭās < Middle Persian tašt < Avestan tašta- 'fashioned (bowl)', ultimately from PIE *tetḱ-.\",\n \"انگلیسی tass «جام کوچک، فنجان» از فرانسوی tasse، آن از عربی طاس، آن از پهلوی tašt و سرانجام از اوستایی tašta- «کاسه» است؛ پس واژه‌ای ایرانی است که از راه عربی و فرانسوی به انگلیسی رسیده. ادعای نورایی درست است (کلاین، ویکی‌واژه).\",\n [W+\"tass\",W+\"tasse\"],\n [{\"ref\":\"KLN:1575\",\"status\":\"supports\",\"note\":\"Klein 1966 s.v. tass (KLN_1966.txt line 38270): 'tass, n., a drinking cup; a small draft. — MF. (= F.) tasse, cup, fr. OF., fr. Arab. tassah, tass, fr. Pers. tasht, cup, saucer'.\"}],\n [{\"src\":\"SKT\",\"where\":\"s.v. tass\",\"stance\":\"silent\",\"note\":\"grep '^tass' in SKT.txt found only Tassel (from L. taxillus); no tass entry.\"},\n  {\"src\":\"HRN\",\"where\":\"no. 389 footnote\",\"stance\":\"supports\",\"note\":\"franz. tasse, nhd. Tasse from Arabic ṭās < Persian tašt.\"}]))\n\ne0nodes.append(N(6,\"Avestan\",\"traš 2, trâš 2\",\"disputed\",\n \"No Avestan verb traš-/trāš- 'to cut' is attested. Nourai's form comes from Abolghasemi (FFD p.46), who reconstructs an Old Iranian (not Avestan) root *traš- with vṛddhi *trāš-a- and a Parthian trāš, and does not link it to PIE *teks-. The only Avestan look-alike is θwarəs- 'to cut, hew' (Vd 5.1 avi dim θwarəsaiti). Cheung calls it isolated in Iranian, and it cannot give tarāš- (Av. θw- gives NP t-, but the vowel and sibilant do not match). Modern scholarship (Cheung 2007 s.v. *taš; Wiktionary تراشیدن) derives NP tarāšīdan/tarāš- from MP tāšīdan 'to cut, cleave' (root *taš- < PIE *tetḱ-), with an intrusive -r- from xarāšīdan 'to scratch'. So the root is right but this Avestan intermediate does not exist.\",\n \"در اوستا فعلی به صورت traš-/trāš- «بریدن» ثبت نشده است. نورایی این صورت را از ابوالقاسمی (فعل‌های فارسی دری، ص ۴۶) گرفته، که آن را ریشه‌ای ایرانی باستانِ بازسازی‌شده (*traš و صورت بالاندهٔ *trāš-a-) و صورت پارتی trāš می‌داند، نه اوستایی، و آن را به teks- هندواروپایی پیوند نمی‌دهد. اوستایی θwarəs- «بریدن» ریشه‌ای جداست که چونگ آن را بی‌همتا می‌خواند. پژوهش امروزی (چونگ، ویکی‌واژه) «تراشیدن» را از فارسی میانه tāšīdan و ریشهٔ *taš- می‌داند و r آن را افزوده‌ای از «خراشیدن» می‌شمارد. پس ریشه درست است، ولی این گرهٔ اوستایی پذیرفتنی نیست.\",\n [W+\"تراشیدن\"],\n [{\"ref\":\"FFD:46\",\"status\":\"partial\",\"note\":\"Abolghasemi p.46 (PDF p.51, read from image; saved ocr/FFD/46.vision.txt + 46.png): «تراش ← پهلوی اشکانی trāš ← ایرانی باستان *trāš-a ... trāš صورت بالاندهٔ ریشهٔ traš است. traš و trāš هر دو «بریدن» معنی می‌دهند». The forms and the meaning match the chart, but they are labelled Old Iranian/Parthian, not Avestan, and are not tied to PIE teks-.\"},\n  {\"ref\":\"MON:1060\",\"status\":\"partial\",\"note\":\"Mo'in s.v. تراشیدن (MON_part1.txt line 39589): 'ستردن موی به وسیلهٔ تیغ از بدن، خراشیدن و پاک کردن چیزی، رنده کردن ...'. The meaning is confirmed, but the online/OCR text has no Avestan form (the Latin-script Pahlavi tags of the print edition are lost in the OCR).\"}],\n [{\"src\":\"CHEUNG\",\"where\":\"pp.384-385 s.v. *taš (line 25072ff.)\",\"stance\":\"contradicts\",\"note\":\"'NP tarāšīdan/tarāš- to shave ... The intrusion of -r- in NP tarāšīdan/tarāš- points to contamination with NP xarāšīdan/xarāš- to scratch (a wound), v. *xrā̆š'. The root is *taš-, not *traš-.\"},\n  {\"src\":\"CHEUNG\",\"where\":\"p.400 s.v. *θwarš (line 25985)\",\"stance\":\"contradicts\",\"note\":\"'Av. θβarəs- is isolated in Iranian: no other correspondences are attested'.\"},\n  {\"src\":\"BRT\",\"where\":\"col. 645 s.v. taš- (Vd 5.1)\",\"stance\":\"silent\",\"note\":\"In the cited passage 'avi dim θwarəsaiti avi dim tāšti' the cutting verbs are θwarəs- and taš-; Bartholomae has no traš-/trāš-.\"},\n  {\"src\":\"ARY\",\"where\":\"pdf page 347 (ARY_pages.txt line 10295)\",\"stance\":\"contradicts\",\"note\":\"Aryanpur, under ستنبه/سترون (PIE *ster-): «به احتمال زیاد واژه‌های استر ... و سترون ... تراشیدن نیز از همین واجریشه‌اند». This is a third, different derivation.\"}]))\n\ne0nodes.append(N(7,\"Persian\",\"tarâšîdan\",\"plausible\",\n \"NP tarāšīdan, present stem tarāš- 'to shave, scrape, whittle' (with an analogical past stem 'tarāšīd', as FFD notes) is accepted as a reflex of the *taš-/*tetḱ- root: MP tāšīdan, tāš- 'to cut, cleave' (MacKenzie p.82) < Proto-Iranian *tā́šti, with an -r- taken over from the near-synonym xarāšīdan 'to scratch' (Cheung 2007; Wiktionary). It is cognate with Northern Luri tāšnyı 'to cut' and Kurdish tāšīn 'to hew, shave'. The root assignment is right, but the chart's route through an Avestan *traš-/trāš- (node #6) is not supported (see #6), hence 'plausible'.\",\n \"«تراشیدن» (مادهٔ مضارع «تراش»؛ مادهٔ ماضی «تراشید» جعلی و ساخته از مادهٔ مضارع است) از فارسی میانه tāšīdan «بریدن، شکافتن» و ریشهٔ ایرانی باستان *taš- (هندواروپایی *tetḱ-) است. r میانی آن به گمان چونگ از هم‌آمیزی با «خراشیدن» آمده است. پس هم‌ریشگی با «تیشه، تشت» و یونانی tekhnē پذیرفتنی است، ولی گذر از صورتی اوستایی به نام traš/trāš که نورایی آورده تأیید نمی‌شود. ادعا با احتیاط پذیرفتنی است.\",\n [W+\"تراشیدن\",TETK],\n [{\"ref\":\"FFD:46\",\"status\":\"supports\",\"note\":\"FFD p.46: «تراشیدن: «تراشید» مادهٔ ماضی جعلی است، از مادهٔ مضارع ساخته شده است. تراش ← پهلوی اشکانی trāš ← ایرانی باستان *trāš-a» (ocr/FFD/46.vision.txt). It supports Nourai's arrow from traš/trāš, but that intermediate is Abolghasemi's own reconstruction.\"}],\n [{\"src\":\"CHEUNG\",\"where\":\"p.385 s.v. *taš\",\"stance\":\"partial\",\"note\":\"Same root (*taš, PIE *tetK-, Pok. 1058), with the -r- explained as contamination from xarāšīdan.\"},\n  {\"src\":\"PHD\",\"where\":\"p.82\",\"stance\":\"partial\",\"note\":\"'tāšīdan, tāš- [t'š-ytn'] cut, cleave; create'. There is no MP *tarāš-.\"},\n  {\"src\":\"HRN\",\"where\":\"no. 387 / Pahlavi no. 200\",\"stance\":\"silent\",\"note\":\"Horn lists phlv. tāšītan 'zimmern' (no. 200, p.294) but no NP tarāšīdan entry was found.\"},\n  {\"src\":\"ARY\",\"where\":\"pdf page 347\",\"stance\":\"contradicts\",\"note\":\"Aryanpur tentatively ties تراشیدن to PIE *ster- (with سترون, استر).\"},\n  {\"src\":\"MON\",\"where\":\"s.v. تراشیدن (MON_part1.txt line 39589)\",\"stance\":\"silent\",\"note\":\"Gives the meanings only.\"}]))\n\ne0nodes.append(N(8,\"Sogdian\",\"t`š\",\"confirmed\",\n \"Sogdian t'š- /tāš-/ 'to cut' (Buddhist and Manichaean Sogdian; pres. 3sg t'št) is the regular Sogdian reflex of Proto-Iranian *taš-/*tāš-, with the same lengthened grade as Skt tāṣṭi and MP tāš-. Manichaean Sogdian t'š /taš/ 'tablet' (BBB 527), which Gharib compares with Avestan tašəm-dāru, is a noun from the same verb, 'a cut, planed (board)'. Both glosses in the chart are right.\",\n \"سغدی t'š (تاش) «بریدن» دنبالهٔ منظم ریشهٔ ایرانی باستان *taš- است، با همان پایهٔ کشیده که در سنسکریت tāṣṭi و پهلوی tāš- دیده می‌شود. سغدی مانوی t'š به معنی «لوح، تخته» نیز از همین فعل است، یعنی «چوبِ تراشیده». ادعای نورایی درست است (قریب، چونگ).\",\n [TETK],\n [{\"ref\":\"SOD:384\",\"status\":\"supports\",\"note\":\"Gharib, Sogdian Dictionary p.384 (SOD_pages.txt line 31181): '9499 t's M taš cf. Av. tašəm-dāru, tablet, BBB 527'; '9500 t's- B, M taš cf. Av. taš; Pahl. tāšīdan, Khot. ttāś, (to) cut, TSP 2.116 ...'.\"}],\n [{\"src\":\"CHEUNG\",\"where\":\"p.385 s.v. *taš\",\"stance\":\"supports\",\"note\":\"'SOGDIAN: BSogd. t'š, MSogd. t'š to cut. Pres.: IND. 3sg. BSogd. t'št'.\"},\n  {\"src\":\"ISS_alt_DKS\",\"where\":\"(via Cheung: DKS 129b f.)\",\"stance\":\"silent\",\"note\":\"Bailey's Khotanese ttāś- 'to cut' is cited in Cheung and Gharib; not regrepped in the OCR.\"}]))\n\ne0nodes.append(N(9,\"Greek\",\"texně; tektôn; arxi-tektôn\",\"confirmed\",\n \"Greek tékhnē 'art, craft, skill' < *tetḱ-sneh₂ (with *-ks- before n reduced, Beekes), tektōn 'carpenter, builder' < *tétḱ-ō(n) (the *tḱ cluster metathesised to Greek kt), and arkhitéktōn 'master builder' = arkhi- 'chief' (arkhein 'to begin, rule') + tektōn, all from PIE *tetḱ-/*teks- 'to fashion, build (with an axe)'.\",\n \"یونانی tekhnē «فن، هنر، مهارت» و tektōn «درودگر، سازنده» از ریشهٔ هندواروپایی *tetḱ-/teks- اند؛ در tektōn خوشهٔ *tḱ به kt دگرگون (قلب) شده است. arkhitektōn «سرمعمار» از arkhi- «سر، مهتر» و tektōn ساخته شده است. ادعای نورایی درست است (پوکورنی، واتکینز، والده‌ـپوکورنی، کلاین).\",\n [TETK,\"https://www.etymonline.com/word/architect\"],\n [{\"ref\":\"AHD\",\"status\":\"supports\",\"note\":\"Watkins teks- 3: '*teks-on- ... in Greek tektōn, carpenter, builder: TECTONIC; ARCHITECT'; 4: '*teks-nā- ... Greek tekhnē, art, craft, skill'.\"}],\n [POK_TEKS,WLD_TEKS,KLN_TEXT,\n  {\"src\":\"KLN\",\"where\":\"1966 s.v. architect (line 3347)\",\"stance\":\"supports\",\"note\":\"'architect — F. architecte, fr. L. architectus, fr. Gk. arkhitektōn, master builder, fr. arkhi-, chief, and tektōn, carpenter, builder, which is rel. to technē, art, skill, craft'.\"}]))\n\ne0nodes.append(N(10,\"French\",\"\",\"confirmed\",\n \"Pass-through node for French architecte (Latin architectus < Greek arkhitektōn) and technique (18th c.: noun use of the adjective technique < Greek tekhnikós 'of art' < tékhnē). These French words are the direct sources of the Persian and English forms in #11 and #12.\",\n \"این گره نمایندهٔ فرانسوی architecte (از لاتین architectus و یونانی arkhitektōn) و technique (از یونانی tekhnikos «هنری، فنی» از tekhnē) است که سرچشمهٔ مستقیم واژه‌های فارسی و انگلیسی گره‌های ۱۱ و ۱۲‌اند. ادعای نورایی درست است.\",\n [W+\"technique\",\"https://www.etymonline.com/word/architect\"],\n [{\"ref\":\"AHD\",\"status\":\"supports\",\"note\":\"Watkins teks- items 3-4 list ARCHITECT and TECHNICAL (English), via French/Latin.\"}],\n [{\"src\":\"KLN\",\"where\":\"1966 s.v. architect / technique (lines 3347, 38360)\",\"stance\":\"supports\",\"note\":\"'architect — F. architecte, fr. L. architectus, fr. Gk.'; 'technique — F., fr. the Greek adjective tekhnikos, pertaining to art, used as a noun'.\"},\n  {\"src\":\"SKT\",\"where\":\"s.v. architect (SKT.txt line 19265)\",\"stance\":\"supports\",\"note\":\"'architect. (F. — L. — Gk.) F. architecte. — L. architectus — Gk. arkhitektōn, a chief builder'.\"}]))\n\ne0nodes.append(N(11,\"Persian\",\"âršîtekt; teknîk\",\"confirmed\",\n \"Modern Persian âršitekt 'architect' and teknik 'technique' are 20th-century loans from French architecte and technique (French ch = [ʃ] gives Persian š in ârši-; initial a- written آ). Mo'in marks تکنیک as French. The native Persian equivalent of âršitekt is me'mâr.\",\n \"«آرشیتکت» و «تکنیک» وام‌واژه‌های سدهٔ بیستم از فرانسوی architecte و technique‌اند؛ ch فرانسوی که «ش» خوانده می‌شود در فارسی «ش» شده است. معین «تکنیک» را فرانسوی می‌داند. ادعای نورایی درست است.\",\n [W+\"تکنیک\"],\n [{\"ref\":\"AMD:25\",\"status\":\"not_checked\",\"note\":\"Amid's 1369 print pages cannot be mapped (refs_online.json); online entry text was not fetched.\"},\n  {\"ref\":\"MON:1128\",\"status\":\"supports\",\"note\":\"Mo'in s.v. تکنیک (MON_part1.txt line 42999): 'تکنیک: [فر.] (ص نسب.) فنی. کار فنی. (ا.) فن.' (the origin tag is garbled in the OCR as '*[:۱6'). No آرشیتکت headword was found in the OCR.\"}],\n [{\"src\":\"MON\",\"where\":\"s.v. تکنیک\",\"stance\":\"supports\",\"note\":\"'فنی. کار فنی ... فن'.\"},\n  {\"src\":\"KLN\",\"where\":\"1966 s.v. technique\",\"stance\":\"supports\",\"note\":\"Gives the French source form technique < Gk. tekhnikos.\"}]))\n\ne0nodes.append(N(12,\"English\",\"architect, technique\",\"confirmed\",\n \"English architect (1560s, < French architecte < Latin architectus < Greek arkhitektōn) and technique (1817, < French technique < Greek tekhnikós < tékhnē) both go back to PIE *teks-, as Watkins lists them (ARCHITECT, TECHNICAL).\",\n \"انگلیسی architect (سدهٔ شانزدهم، از فرانسوی و لاتین و یونانی arkhitektōn) و technique (سدهٔ نوزدهم، از فرانسوی technique و یونانی tekhnikos) هر دو سرانجام به ریشهٔ هندواروپایی teks- می‌رسند. ادعای نورایی درست است (واتکینز، کلاین، اسکیت).\",\n [\"https://www.etymonline.com/word/architect\",W+\"technique\"],\n [{\"ref\":\"AHD:68,1321\",\"status\":\"supports\",\"note\":\"Watkins 1985 s.v. teks- (p.69 of the standalone ed.; AHD 1975 appendix p.1546): ARCHITECT under item 3, TECHNICAL under item 4. Page 68 of the AHD main text (architect) was not checked separately.\"}],\n [{\"src\":\"KLN\",\"where\":\"1966 s.v. architect, technique\",\"stance\":\"supports\",\"note\":\"See #10.\"},\n  {\"src\":\"SKT\",\"where\":\"s.v. architect\",\"stance\":\"supports\",\"note\":\"'Gk. arkhitektōn, a chief builder ... (See also Text.)'\"}]))\n\ne0nodes.append(N(13,\"Latin\",\"texere; testum\",\"plausible\",\n \"Latin texō, texere 'to weave, plait; (occasionally) to build' is a secure reflex of PIE *tetḱ-/*teks- (de Vaan 2008: 619; Pokorny, Walde-Pokorny, Watkins). testum 'earthenware lid, pot' (with testa 'baked clay, potsherd, shell') is linked to the same root only by Pokorny, Walde-Pokorny and Klein ('prob. cogn. with Avestic tashta- cup'). Wiktionary derives testum from *ters-to- 'dried (clay)' (PIE *ters- 'dry'); Watkins does not list it under teks-; and Wiktionary's tetḱ- page has testa only with a query ('> ? Latin testa'). The texere half is confirmed and the testum half is disputed among scholars, so the node is plausible.\",\n \"لاتین texere «بافتن، به هم بافتن، گاه ساختن» بی‌گمان از ریشهٔ teks-/tetḱ- است. اما پیوند testum «سرپوش و ظرف سفالی» با این ریشه را تنها پوکورنی، والده‌ـپوکورنی و کلاین (به قیاس با اوستایی tašta- «تشت») آورده‌اند. ویکی‌واژه آن را از *ters- «خشک» («گِلِ خشکیده») می‌داند و واتکینز آن را زیر teks- نمی‌آورد. پس بخش texere درست است و بخش testum با احتیاط پذیرفتنی است.\",\n [TETK,W+\"testum\",W+\"test\"],\n [{\"ref\":\"AHD\",\"status\":\"partial\",\"note\":\"Watkins teks- 1: 'Latin texere, to weave, fabricate: TEXT, TISSUE; CONTEXT, PRETEXT'. testum/TEST is not listed under teks-.\"}],\n [POK_TEKS,WLD_TEKS,\n  {\"src\":\"KLN\",\"where\":\"1966 s.v. test (line 38729)\",\"stance\":\"supports\",\"note\":\"'L. testu, testum, vessel, earthen vessel, pot, which is rel. to testa ... and prob. cogn. with Avestic tashta-, cup ... and with L. texere, to weave, fr. I.-E. base *tekþ-'.\"},\n  {\"src\":\"LAT\",\"where\":\"s.v. texo / testa\",\"stance\":\"silent\",\"note\":\"Not regrepped (Ernout-Meillet OCR); de Vaan via Wiktionary used instead.\"}]))\n\ne0nodes.append(N(14,\"English\",\"context, test, text, textile, tissue\",\"plausible\",\n \"text (ME < OF texte < Latin textus 'woven fabric, style', ppp. of texere), context (Latin contextus < contexere 'to weave together'), textile (Latin textilis 'woven') and tissue (ME tissu < OF tissu, ppp. of tistre < Latin texere) are all secure. test (ME 'cupel for assaying metals' < OF test < Latin testum 'earthen pot'; the sense 'trial' comes from the assayer's pot) depends on node #13's disputed testum (Wiktionary: < *ters- 'dry'). So four of the five words are confirmed and test is plausible.\",\n \"انگلیسی text، context، textile و tissue (از فرانسوی کهن tissu، صفت مفعولی tistre «بافتن») همه بی‌گمان از لاتین texere و ریشهٔ teks-‌اند. test «بوتهٔ سفالی عیارگیری فلز» و سپس «آزمون» از لاتین testum است که پیوندش با این ریشه مورد اختلاف است (ویکی‌واژه آن را از *ters- «خشک» می‌داند). پس بیشتر این گره درست است و test با احتیاط پذیرفتنی است.\",\n [W+\"text\",W+\"tissue\",W+\"test\"],\n [{\"ref\":\"(none)\",\"status\":\"not_checked\",\"note\":\"node carries no reference of its own; checked against AHD teks- (TEXT, TISSUE, CONTEXT) instead.\"}],\n [AHD_TEKS,\n  {\"src\":\"KLN\",\"where\":\"1966 s.v. text / tissue / context / test\",\"stance\":\"supports\",\"note\":\"'tissue — ME. tissu, fr. OF. tissu, woven fabric, pp. of tistre ... fr. L. texere'; 'context — L. contextus ... contexere, to weave'; s.v. text 'Cp. ... test, cupel, textile ... tissue'.\"},\n  {\"src\":\"SKT\",\"where\":\"s.v. text, textile, tissue (SKT.txt lines 19471-19765)\",\"stance\":\"supports\",\"note\":\"'textile. (L.) L. textilis, woven. — L. textus, pp. of texere, to weave'; 'Tissue; see Text'.\"}]))\n\ne0={\"entry\":0,\"root\":\"Tex, Text, Teks, Teku 2\",\"verdict\":\"confirmed\",\n \"modern_form\":\"PIE *tetḱ- (Pokorny *tek̂þ-, Watkins *teks-) 'to fashion, build (of wood, with an axe); to weave'\",\n \"note\":\"Pokorny 1058-1059 tek̂þ- 'flechten; Holzbearbeitung, Zimmermann'; Walde-Pokorny I 717 tekþ- 'zimmern, Holz behauen und damit bauen'; Watkins teks- 'to weave; also to fabricate, especially with an ax'; Klein *tekþ- 'to build (of wood), carpenter; to weave'. Nourai's gloss 'to build from wood' matches Walde-Pokorny and Klein. The root and the Avestan, Greek, Latin and Sogdian branches are confirmed. Problems: (1) Persian taxteh belongs to taxt 'throne' (< *(s)teg-?), not to this root; *taš-ta- gives tašt. (2) The Avestan 'traš, trāš' (#6) is not attested; it is Abolghasemi's Old Iranian reconstruction, and tarāšīdan is now explained as taš- plus an intrusive -r-. (3) Latin testum (and English test) is attributed to *teks- only by Pokorny and Klein; Wiktionary prefers *ters- 'dry'. (4) Persian tīše is uncertain (Horn: with tēz 'sharp').\",\n \"note_fa\":\"ریشهٔ هندواروپایی آغازین *tetḱ- (در پوکورنی tek̂þ-، در واتکینز teks-) به معنی «تراشیدن و ساختن با تبر، درودگری؛ بافتن» است و معنایی که نورایی آورده («ساختن از چوب») با والده‌ـپوکورنی و کلاین می‌خواند. شاخه‌های اوستایی (taš-، taša-، tašta-)، سغدی، یونانی و لاتین texere درست‌اند و «تشت» و «طاس» و انگلیسی tass نیز از همین ریشه‌اند. اما «تخته» از taxt «تخت» است و به این ریشه نمی‌رسد. صورت اوستایی traš/trāš ثبت نشده و پژوهش امروزی «تراشیدن» را از tāš- با r افزوده می‌داند. پیوند لاتین testum (و انگلیسی test) نیز مورد اختلاف است.\",\n \"sources\":[TETK,W+\"تراشیدن\",W+\"طاس\",W+\"tasse\"],\n \"ref_check\":[{\"ref\":\"POK:1058\",\"status\":\"supports\",\"note\":\"POK_full.txt line 85033: 'Root / lemma: tek̂þ- ; Meaning: to plait; woodwork; carpenter ... Page(s): 1058-1059' with Old Indic takṣati, Avestan tašaiti, taša-, tašta-, Greek tektōn, technē, Latin texo, testa.\"}],\n \"consulted\":[WLD_TEKS,AHD_TEKS,KLN_TEXT,\n  {\"src\":\"CHEUNG\",\"where\":\"p.384 s.v. *taš\",\"stance\":\"supports\",\"note\":\"'PIE *tetK- to construct, build by cutting = LIV: 638 f. | Pok.: 1058 f.'\"},\n  {\"src\":\"ARY\",\"where\":\"pdf page 189 (printed 190), headword تخشا/تخشیدن\",\"stance\":\"partial\",\"note\":\"Aryanpur puts the teks- set (Av. TASHAITI, Pahl. TASH-, Gk. TEKTON, Lat. TEXO, Fr. TISSER) under Persian تخشیدن 'to strive'.\"}],\n \"nodes\":e0nodes}\n\n# entry 2\ne2nodes=[]\ne2nodes.append(N(1,\"Avestan\",\"ithyajah, ithyejah\",\"plausible\",\n \"Avestan iθyajah-, iθyejah- n. (OAv. Y 34.8; YAv. Vd, Yt) is a real word with an epenthetic i-, < *θyaj-ah-, the exact match of Sanskrit tyájas- n. (< PIE *tyégʷ-os). Bartholomae and Walde-Pokorny gloss it 'Not, Gefahr' ('need, danger'). Pokorny's 'Verlassenheit' ('abandonment') is really the gloss of Sanskrit tyajas, though Cheung also renders the Avestan word 'abandonment (?)'. Nourai's gloss is therefore defensible but not the usual one. The link to PIE *tyegʷ- is standard (Pokorny 1086, Wiktionary), but Cheung (*θi̯aǰ, pp.392-393) warns that 'it is uncertain whether all these Ir. forms are related' to Skt tyaj.\",\n \"اوستایی iθyajah-/iθyejah- (با i- افزودهٔ آغازین) واژه‌ای واقعی و برابر دقیق سنسکریت tyajas- است، از ریشهٔ هندواروپایی *tyegʷ-. بارتولومه و والده‌ـپوکورنی معنای آن را «تنگنا، خطر» می‌دانند. «رهاشدگی» که نورایی آورده در اصل معنای واژهٔ سنسکریت است، هرچند چونگ نیز با تردید «رهاکردن» را پیشنهاد می‌کند. پیوند با ریشهٔ *tyegʷ- پذیرفته است، اما چونگ دربارهٔ هم‌ریشگی همهٔ صورت‌های ایرانی تردید دارد. پس ادعا با احتیاط پذیرفتنی است.\",\n [TYEG,W+\"سیج\"],\n [{\"ref\":\"POK:1086\",\"status\":\"supports\",\"note\":\"POK_full.txt line 86829: 'Root / lemma: tieg̯ʷ- ; Meaning: to retreat in fear; Material: Old Indie tyajati ... tyajas- n. 'Verlassenheit' = Avestan iθyajah-, iθyejah- n. ds.'\"}],\n [{\"src\":\"BRT\",\"where\":\"s.v. iθyajah- (BRT.txt line 14454)\",\"stance\":\"supports\",\"note\":\"'iθyajah-, iθyejah- n. 'Not, Gefahr' ... Y.10.22 ... yaēšu as pairi pourubyō -ejō \\\"in denen für viele Gefahr liegt\\\" Y.34.8 ... — ai. tyájas- n.'\"},\n  {\"src\":\"WLD\",\"where\":\"Bd. I p.746 s.v. tieg̯ʷ- (WLD_Bd1_pages.txt line 70585)\",\"stance\":\"supports\",\"note\":\"'tieg̯ʷ- „scheu vor etwas zurücktreten oder auffahren“ ... tyájas- n. „das Imstichlassen, Not, Gefahr“ = av. iθyajah-, iθyejah- n. „Not, Gefahr“'.\"},\n  {\"src\":\"CHEUNG\",\"where\":\"p.392 s.v. *θi̯aǰ (CHEUNG.txt line 25542)\",\"stance\":\"partial\",\"note\":\"'AVESTAN: OAv. iθiiejah- [n] abandonment (?) (Y 34,8), YAv. iθiiajah-, iθiiejah- ... SANSKRIT: tyaj to leave, dismiss, abandon ... It is uncertain whether all these Ir. forms cited here are related to each other'.\"}]))\n\ne2nodes.append(N(2,\"Pahlavi\",\"sěj\",\"confirmed\",\n \"Zoroastrian Middle Persian sēj [syc] 'danger, trouble, distress' (with sējōmand 'dangerous' and a-sēj 'free from danger, imperishable') corresponds to Av. iθyejah-: the epenthetic i- is lost, and *θy gives MP s (as in *θyāva- > siyāh). MacKenzie writes '= Av. iθyejah-', and Nyberg treats the word as borrowed from (learned) Avestan. Both agree on the Avestan source.\",\n \"پهلوی sēj «خطر، رنج، گرفتاری» (و sējōmand «پرخطر» و a-sēj «بی‌گزند») برابر اوستایی iθyejah- است؛ i- آغازی افتاده و *θy ایرانی باستان در فارسی میانه به s بدل شده است. مکنزی آن را «= اوستایی iθyejah-» می‌نویسد و نیبرگ آن را وامی دانشورانه از اوستا می‌داند. ادعای نورایی درست است.\",\n [W+\"سیج\"],\n [{\"ref\":\"SNS:314\",\"status\":\"not_found\",\"note\":\"Tavoosi's glossary (archive.org VajnameShayest): leaf n174 = printed pp.312/313 (p.313 ends with sēb 'apple', where sēj [syc] would follow) and leaf n175 = pp.316/317, so printed pp.314-315 seem to be missing from the scan. The images were saved as ocr/SNS/312-313.jpg and 316-317.jpg, and the entry could not be read.\"}],\n [{\"src\":\"PHD\",\"where\":\"p.74 (PHD_mackenzie.txt line 4537)\",\"stance\":\"supports\",\"note\":\"'sēj [syc = Av. iθyejah- | N ~] danger, trouble. ~ōmand [-'wmnd | N ~mand] dangerous'; also 'a-sēj [ʾsyc] free from danger'.\"},\n  {\"src\":\"NYB\",\"where\":\"Part II p.183 (leaf 191; line 3425)\",\"stance\":\"supports\",\"note\":\"'sēž [syc'] distress, embarrassment 37¹², 44²... — Borrowed from Av. (79⁹) iθyajah-, iθyejah- (i- epenthetic)'; also 'a-sēž [ʾsyc'] incorruptible, imperishable'.\"}]))\n\ne2nodes.append(N(3,\"Persian\",\"sîj\",\"confirmed\",\n \"Early New Persian sīj (سیج, with kasra; Borhan: 'رنج و محنت و مشقت') 'pain, suffering, hardship' and sījmand 'full of pain' continue MP sēj, sējōmand (MP ē > NP ī). Mo'in's footnote quotes the Zartosht-e Bahram Ardā-Wirāz-nāma verse «جهان سیجمند و پر انائی - که او را پیشه باشد بیوفائی», the same verse Nourai prints. This is a rare word, mainly in Zoroastrian Persian. Wiktionary سیج: 'From Middle Persian syc /sēj/ danger, trouble, compare Avestan iθiiejah'.\",\n \"«سیج» (به کسر سین) «رنج، محنت، مشقت» و «سیجمند» «رنج‌آلود» دنبالهٔ پهلوی sēj و sējōmand‌اند؛ ē فارسی میانه در فارسی نو به ī بدل شده است. معین در حاشیهٔ برهان قاطع همان بیت ارداویرافنامهٔ زرتشت بهرام را آورده که نورایی نقل کرده است: «جهان سیجمند و پر انائی…». واژه کمیاب و بیشتر زرتشتی است. ادعای نورایی درست است (برهان قاطع، معین، مکنزی، ویکی‌واژه).\",\n [W+\"سیج\"],\n [{\"ref\":\"BQT:1202\",\"status\":\"supports\",\"note\":\"Borhan vol. 2 p.1202 (archive.org borhan-ghate-v2 leaf n666; read from image, saved ocr/BQT/1202.vision.txt + 1202.jpg): «سیج - ... و بکسر اول بمعنی رنج و محنت و مشقت ۴»; fn. 4 (Mo'in): «سیجمند بمعنی دارندهٔ رنج، محل رنج و محنت: جهان سیجمند و پر انائی / که او را پیشه باشد بیوفائی. زرتشت بهرام، ارداویرافنامه چاپ جاماسب اسا ص ۵». This gives the meaning and Nourai's verse but no Pahlavi etymon.\"},\n  {\"ref\":\"SNS:314\",\"status\":\"not_found\",\"note\":\"See node #2: printed p.314 is not in the archive.org scan (leaves n174 = pp.312/313, n175 = pp.316/317).\"}],\n [{\"src\":\"MON\",\"where\":\"s.v. سیج (MON_2vol_Adena_v1_djvu.txt line 82129)\",\"stance\":\"supports\",\"note\":\"'سیج: (ا.) انگور خشک شده' and 'سیج: (ا.) رنج، محنت، مشقت. سیجمند [- سیج] (ص مر.) دارندهٔ درد و رنج. محل رنج و محنت'.\"},\n  {\"src\":\"PHD\",\"where\":\"p.74\",\"stance\":\"supports\",\"note\":\"'sēj ... | N ~ ... ~ōmand | N ~mand': MacKenzie gives the NP continuants sīj, sījmand.\"},\n  {\"src\":\"HRN\",\"where\":\"grep 'sij', 'sēj'\",\"stance\":\"silent\",\"note\":\"No entry.\"}]))\n\ne2={\"entry\":2,\"root\":\"Tiegu\",\"verdict\":\"plausible\",\n \"modern_form\":\"PIE *tyegʷ- 'to give way, withdraw (in awe/fear), abandon' (Pokorny tieg̯ʷ- 'to retreat in fear')\",\n \"note\":\"The root is real (Pokorny 1086; Walde-Pokorny I 746 'scheu vor etwas zurücktreten oder auffahren'; LIV *ti̯egʷ-; reflexes Skt tyajati 'abandons', Greek sébomai 'revere'), and the Indo-European label is right. Nourai's gloss 'to approach shyly' mistranslates the German 'scheu zurücktreten': the meaning is to draw BACK in awe or fear, not to approach. The Avestan, Pahlavi and Persian chain (iθyejah- > sēj > sīj) is confirmed by MacKenzie, Nyberg, Bartholomae, Borhan/Mo'in and Wiktionary. Cheung doubts that all the Iranian forms belong with Skt tyaj.\",\n \"note_fa\":\"ریشهٔ هندواروپایی آغازین *tyegʷ- به معنی «از سرِ ترس یا حرمت پس کشیدن، کنار رفتن، رها کردن» است (پوکورنی ۱۰۸۶؛ سنسکریت tyajati «رها می‌کند»، یونانی sebomai «حرمت می‌نهد»). معنایی که نورایی آورده («با شرم نزدیک شدن») ترجمهٔ نادرستِ «scheu zurücktreten» آلمانیِ پوکورنی است، زیرا معنا «پس کشیدن» است نه «نزدیک شدن». زنجیرهٔ اوستایی iθyejah- ← پهلوی sēj ← فارسی «سیج» درست است، ولی چونگ دربارهٔ پیوند همهٔ صورت‌های ایرانی با سنسکریت tyaj تردید دارد. پس ریشه با احتیاط پذیرفتنی است.\",\n \"sources\":[TYEG,W+\"سیج\"],\n \"ref_check\":[{\"ref\":\"POK:1086\",\"status\":\"supports\",\"note\":\"POK_full.txt line 86829: 'tieg̯ʷ- ; Meaning: to retreat in fear ... Page(s): 1086'. Pokorny's meaning is 'retreat', not 'approach'.\"}],\n \"consulted\":[{\"src\":\"WLD\",\"where\":\"Bd. I p.746\",\"stance\":\"supports\",\"note\":\"'tieg̯ʷ- „scheu vor etwas zurücktreten oder auffahren“'.\"},\n  {\"src\":\"AHD\",\"where\":\"Watkins 1985\",\"stance\":\"silent\",\"note\":\"grep 'tyegw'/'tyeg' in AHD_watkins1985.txt: no entry (no English reflex).\"},\n  {\"src\":\"CHEUNG\",\"where\":\"pp.392-393 s.v. *θi̯aǰ\",\"stance\":\"partial\",\"note\":\"'It is uncertain whether all these Ir. forms cited here are related to each other. Some of them may be indeed related to tyaj to leave, dismiss, abandon'.\"}],\n \"nodes\":e2nodes}\n\nout={\"pdf_page\":509,\"book_page\":479,\"verified_by\":\"claude-opus-5\",\"verified_on\":\"2026-10-14\",\"entries\":[e0,e2]}\njson.dump(out,open(\"/home/sfmqrb/git/rishe-private/data/verification/page-509.json\",\"w\"),ensure_ascii=False,indent=1)\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/p509/build-509.py && python3 -m json.tool /home/sfmqrb/git/rishe-private/data/verification/page-509.json >/dev/null && python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py 509"
}
```


### [2026-10-15T02:54:35.456Z] TOOL RESULT

```
nodes verified: 17/17
node verdicts: {'confirmed': 11, 'disputed': 2, 'plausible': 4}
root verdicts: {'confirmed': 1, 'plausible': 1}
ref checks: {'supports': 12, 'not_checked': 5, 'partial': 4, 'not_found': 2}
books consulted: {'supports': 34, 'contradicts': 5, 'partial': 6, 'silent': 9} | by book: {'KLN': 9, 'CHEUNG': 7, 'HRN': 7, 'WLD': 4, 'PHD': 4, 'SKT': 4, 'BRT': 3, 'NYB': 3, 'ARY': 3, 'MON': 3, 'POK': 2, 'HUB': 1, 'BQT': 1, 'ISS_alt_DKS': 1, 'LAT': 1, 'AHD': 1}
```


## [2026-10-15T02:54:44.097Z] TOOL CALL #94: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification; python3 - <<'EOF'\nimport json\np='page-509.json'; d=json.load(open(p))\nc=d['entries'][1]['nodes'][0]['consulted'][0]\nc['note']=\"'iθyajah-, iθyejah- n. 'Not, Gefahr' ... a) mit Dat. 'für -': ... yaēšū as pairī pourubyō -ejō \\\"..., in denen für viele Gefahr liegt\\\" Y.34.8 ... — ai. tyájas- n.' (OCR garbled; key gloss and the Skt comparison are legible).\"\nn6=d['entries'][0]['nodes'][5]\nn6['derivation']=n6['derivation'].replace(\" Cheung calls it isolated in Iranian, and it cannot give tarāš- (Av. θw- gives NP t-, but the vowel and sibilant do not match).\",\" Cheung calls it isolated in Iranian, and its s does not match the š of tarāš-.\")\njson.dump(d,open(p,'w'),ensure_ascii=False,indent=1)\nEOF\npython3 -m json.tool page-509.json >/dev/null && python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py 509 | grep -c PROBLEM"
}
```


### [2026-10-15T02:54:44.794Z] TOOL RESULT

```
0
```


## [2026-10-15T02:54:54.849Z] TOOL CALL #95: SubagentHandback

```json
{
 "message": "I verified page 509 (book page 479) and wrote `/home/sfmqrb/git/rishe-private/data/verification/page-509.json`. JSON validates and `verify_check.py 509` shows 17/17 nodes verified and 0 PROBLEM lines.\n\n**Verdicts:**\n- **Roots (2):** Tex/Teks is confirmed. Tiegu is plausible: Nourai's gloss \"to approach shyly\" mistranslates Pokorny's \"retreat in fear\".\n- **Nodes (17):** 11 confirmed, 4 plausible, 2 disputed, 0 transcription_suspect.\n\n**Disputed:**\n- **Tex #2, Persian tîšeh; taxteh; tašt; tâs.** taxteh comes from MP taxtag, built on taxt \"throne\", so it is not from *taš-. The past participle *taš-ta- gives tašt, not taxt. tîšeh is only plausible: no MP form is recorded, and Horn puts it with tēz \"sharp\". tašt and tâs are confirmed.\n- **Tex #6, Avestan traš 2, trâš 2.** No such Avestan verb exists. The form is Abolghasemi's (FFD p.46) reconstructed Old Iranian *traš/*trāš (with a Parthian trāš), not Avestan. Cheung and Wiktionary derive tarāšīdan from MP tāšīdan (root *taš-), with an -r- borrowed from xarāšīdan. Because of this, #7 tarâšîdan is only plausible: the root is right, the route is not.\n\n**Other plausible nodes:** Latin testum and English test (#13, #14) are tied to *teks- only by Pokorny and Klein; Wiktionary prefers *ters- \"dry\". Avestan iθyajah-/iθyejah- (Tiegu #1) usually means \"need, danger\" (Bartholomae), not \"abandonment\".\n\n**Extraction errors:** none found. I checked the JSON against the chart text but did not compare it with the printed page image.\n\n**Reference notes:**\n- SNS:314 could not be read: the archive.org scan jumps from leaf n174 (pp. 312/313) to n175 (pp. 316/317), so pp. 314–315 appear to be missing.\n- BQT:1202 confirms سیج, its footnote on سیجمند, and the Ardā Wirāz verse Nourai quotes.\n- I saved what I read from the page images to `data/verification/sources/refs/ocr/FFD/46.vision.txt` (with `46.png`) and `ocr/BQT/1202.vision.txt` (with `1202.jpg`), plus the SNS leaves as `ocr/SNS/312-313.jpg` and `316-317.jpg`.\n- Etymonline now returns 403. Its architect page was already archived, so I cite it; for the other English words I used the archived Wiktionary pages."
}
```


### [2026-10-15T02:54:55.176Z] TOOL RESULT

```
{"success":true,"message":"Report delivered to your caller."}
```
