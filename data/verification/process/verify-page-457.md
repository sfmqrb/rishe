# Verification process log — verify-page-457


## [2026-09-14T01:56:29.635Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 457 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-457.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-457.json. Write /home/sfmqrb/git/rishe/data/verification/page-457.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 457` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-14T01:56:30.596Z] AGENT

I'll start by reading the instructions.


## [2026-09-14T01:56:31.514Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-14T01:56:31.535Z] TOOL RESULT

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


## [2026-09-14T01:56:32.015Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-457.txt"
}
```


### [2026-09-14T01:56:32.045Z] TOOL RESULT

```
1	=== PDF page 457 (book page 427) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Skhai : to cut, strike  (refs POK:917)
4	#1 (parent #0) [Old Persian] refs=ISS:84 | kai, či : to cut
5	  #2 (parent #1) [Pahlavi] refs=ISS:84 | čělân : metal objects ; čělânkar : metal worker
6	    #3 (parent #2) [Persian] refs=MON:1327 | čîlân «چیلان» : small objects made of iron ; čîlângar «چیلانگر» : metal worker | extra: چلنگر
7	#4 (parent #0) [Latin] refs=POK:917; AHD:186,217; ISS:84 | caedere : to cut ; â caesô mâtris ŭterě : "from the incised womb of his mother" ; caementum : stone chips used to make lime ; caelum : chisel | NOTE: Julius Cesar (or his ancestor) was born by this operation.
8	  #5 (parent #4) [Greek] refs=AHD; KLN:839 | kaisar : Caesar, born by "cesarean" section
9	    #6 (parent #5) [Arabic] refs=BQT:1551 | qaysar : Caesar
10	      #7 (parent #6) [Persian] refs=BQT:217 | qeysar «قیصر» : Caesar
11	  #8 (parent #4) [French] refs=BQT:1551 | 
12	    #9 (parent #8) [Persian] refs=BQT | sezâr «سزار» : Caesar | extra: سزارین
13	    #10 (parent #8) [English] refs=KLN:839 | Caesar
14	  #11 (parent #4) [Russian] refs=BQT:1551 | tsar
15	    #12 (parent #11) [French] refs=None | 
16	      #13 (parent #12) [Persian] refs=BQT | tezâr «تزار» : Russian emperor
17	    #14 (parent #11) [English] refs=AHD | czar, tsar, tzar
18	  #15 (parent #4) [French] refs=AHD:217 | 
19	    #16 (parent #15) [Persian] refs=MON:1983 | sement «سمنت» : cement | extra: سیمان
20	    #17 (parent #15) [English] refs=AHD | cement
21	  #18 (parent #4) [English] refs=AHD | scissors, chisel, concise, precise, circumcise, incision
22	#19 (parent #0) [Latin] refs=FSD:1317; AHD:186 | Caesaria : an ancient seaport in Roman Palestine
23	  #20 (parent #19) [French] refs=AHD:703; FSD:1317; NAT:166 | Jersey : name of an Island north of France famous for its wool clothes
24	    #21 (parent #20) [Persian] refs=VOP:203 | žerseh «ژرسه» : a fine cloth
25	    #22 (parent #20) [English] refs=FSD:1317; NAT:166 | Jersey, New Jersey ; jersey : originally a woolen sweater peculiar to fishermen of Jersey Isle
26	
```


## [2026-09-14T01:56:35.218Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-457.json",
 "description": "Read page 457 source JSON"
}
```


### [2026-09-14T01:56:35.287Z] TOOL RESULT

```
{
  "pdf_page": 457,
  "book_page": 427,
  "entries": [
    {
      "root": {
        "name": "Skhai",
        "lang": "Indo-European",
        "refs": "POK:917",
        "gloss": "to cut, strike"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Old Persian",
          "refs": "ISS:84",
          "words": [
            {"translit": "kai, či", "gloss": "to cut", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "ISS:84",
          "words": [
            {"translit": "čělân", "gloss": "metal objects", "script": null},
            {"translit": "čělânkar", "gloss": "metal worker", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "MON:1327",
          "words": [
            {"translit": "čîlân", "gloss": "small objects made of iron", "script": "چیلان"},
            {"translit": "čîlângar", "gloss": "metal worker", "script": "چیلانگر"}
          ],
          "script_extra": "چلنگر",
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Latin",
          "refs": "POK:917; AHD:186,217; ISS:84",
          "words": [
            {"translit": "caedere", "gloss": "to cut", "script": null},
            {"translit": "â caesô mâtris ŭterě", "gloss": "\"from the incised womb of his mother\"", "script": null},
            {"translit": "caementum", "gloss": "stone chips used to make lime", "script": null},
            {"translit": "caelum", "gloss": "chisel", "script": null}
          ],
          "script_extra": null,
          "note": "Julius Cesar (or his ancestor) was born by this operation.",
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Greek",
          "refs": "AHD; KLN:839",
          "words": [
            {"translit": "kaisar", "gloss": "Caesar, born by \"cesarean\" section", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "Arabic",
          "refs": "BQT:1551",
          "words": [
            {"translit": "qaysar", "gloss": "Caesar", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "Persian",
          "refs": "BQT:217",
          "words": [
            {"translit": "qeysar", "gloss": "Caesar", "script": "قیصر"}
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "به قیصر سپارد همه یک به یک - از این پس نوشته فرستیم و چک",
            "poet": "Ferdowsî"
          }
        },
        {
          "id": 8,
          "parent": 4,
          "lang": "French",
          "refs": "BQT:1551",
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "Persian",
          "refs": "BQT",
          "words": [
            {"translit": "sezâr", "gloss": "Caesar", "script": "سزار"}
          ],
          "script_extra": "سزارین",
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 8,
          "lang": "English",
          "refs": "KLN:839",
          "words": [
            {"translit": "Caesar", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 4,
          "lang": "Russian",
          "refs": "BQT:1551",
          "words": [
            {"translit": "tsar", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 11,
          "lang": "French",
          "refs": null,
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 13,
          "parent": 12,
          "lang": "Persian",
          "refs": "BQT",
          "words": [
            {"translit": "tezâr", "gloss": "Russian emperor", "script": "تزار"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 14,
          "parent": 11,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "czar, tsar, tzar", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 15,
          "parent": 4,
          "lang": "French",
          "refs": "AHD:217",
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 16,
          "parent": 15,
          "lang": "Persian",
          "refs": "MON:1983",
          "words": [
            {"translit": "sement", "gloss": "cement", "script": "سمنت"}
          ],
          "script_extra": "سیمان",
          "note": null,
          "quote": null
        },
        {
          "id": 17,
          "parent": 15,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "cement", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 18,
          "parent": 4,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "scissors, chisel, concise, precise, circumcise, incision", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 19,
          "parent": 0,
          "lang": "Latin",
          "refs": "FSD:1317; AHD:186",
          "words": [
            {"translit": "Caesaria", "gloss": "an ancient seaport in Roman Palestine", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 20,
          "parent": 19,
          "lang": "French",
          "refs": "AHD:703; FSD:1317; NAT:166",
          "words": [
            {"translit": "Jersey", "gloss": "name of an Island north of France famous for its wool clothes", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 21,
          "parent": 20,
          "lang": "Persian",
          "refs": "VOP:203",
          "words": [
            {"translit": "žerseh", "gloss": "a fine cloth", "script": "ژرسه"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 22,
          "parent": 20,
          "lang": "English",
          "refs": "FSD:1317; NAT:166",
          "words": [
            {"translit": "Jersey, New Jersey", "gloss": null, "script": null},
            {"translit": "jersey", "gloss": "originally a woolen sweater peculiar to fishermen of Jersey Isle", "script": null}
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


## [2026-09-14T01:56:37.522Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','ISS','MON','AHD','KLN','BQT','FSD','NAT','VOP','WLD','HRN','HUB','PHD','NYB','BRT','KNT','SKT','WEB','IEC','SYN','ARY','CHEUNG','ISS_alt_DKS']:\n    print(k, json.dumps(d.get(k), ensure_ascii=False)[:600])\n    print()\n\""
}
```


### [2026-09-14T01:56:39.090Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_

ISS {"title": "H. W. Bailey, Indo-Scythian Studies: Khotanese Texts VI (Prolexis to the Book of Zambasta), Cambridge 1967", "edition_found": "not found; Bailey's Dictionary of Khotan Saka (1979) downloaded as the closest substitute", "kind": "google_books_preview+archive_restricted", "url": "https://books.google.com/books?id=4upthUgWo9YC (CUP 2009 reprint, partial preview) ; HathiTrust mdp.39015034317936 (v.6, search-only) ; archive.org khotanesetexts0103bail (vols I-III only, lending)", "identifier": "dictionary-of-khotan-saka (substitute); khotanesetexts0103bail is vols I-III, lending-only", "lo

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118

FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-Dive), in.ernet.dli.2015.272042 (vol II), in.ernet.dli.2015.83695 (vol III), in.ernet.dli.2015.147440 (vol IV Sabi-Z)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt

NAT {"title": "C. Berlitz, Native Tongues, New York 1982", "edition_found": "2005 Castle Books reprint (open); 1982 original lending-only (nativetongues00berl)", "kind": "archive_djvu", "url": "https://archive.org/details/native-tongues-charles-berlitz-book-sales-ca-1997-3-printing-2005-castle-books-9", "identifier": "native-tongues-charles-berlitz-book-sales-ca-1997-3-printing-2005-castle-books-9", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NAT_2005.txt", "page_offset": "2005 reprint: leaf = printed + 15 (e.g. leaf 17 = p.2); reprint pagination may differ slightly from 1

VOP {"title": "Mahshid Moshiri, Farhang-e Vazheha-ye Orupayi dar Farsi, Alborz 1371/1992", "kind": "none", "url": null, "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: not found (only unrelated similar-title books, e.g. Zomorrodian's فرهنگ ریشه‌شناختی واژه‌های دخیل اروپایی, ketabnak 132354).", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 2026-09: nothing — no catalogue record with a scan, no ebook. Decoys: ketabnak 132354 (Zomorrodian), Google Books RwdkAAAAMAAJ (Nahid Shahidi 1997, no view). Purchase second-hand only."}

WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 

HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) fol

PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-

NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf

BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1

KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt", "page_offset": "leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \\

SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves

WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w (restricted full copies: webstersnewtwent00webs_0 1977, webstersnewtwent01webs 1983)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/W

IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 

SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves

ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it 

CHEUNG null

ISS_alt_DKS null
```


## [2026-09-14T01:56:46.712Z] TOOL CALL #5: Bash

```json
{
 "command": "sed -n 1,200p tools/verify_check.py"
}
```


### [2026-09-14T01:56:46.755Z] TOOL RESULT

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


## [2026-09-14T01:56:47.435Z] TOOL CALL #6: Bash

```json
{
 "command": "ls data/verification/ | head -50 && echo --- && ls data/verification/sources/refs/ | head -80"
}
```


### [2026-09-14T01:56:47.518Z] TOOL RESULT

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
---
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
NYB.txt
NYB_vol1.txt
NYB_vol2_glossary.txt
ocr
pageimg
PEI.txt
PHD_mackenzie.pdf
PHD_mackenzie.txt
PHD_pages.txt
PHD.pdf
PHD.txt
PHN.txt
POK_01.txt
POK_02.txt
POK_03.txt
POK_full.txt
RCH.txt
SBK.txt
SDQ.txt
SIN.txt
```


## [2026-09-14T01:56:51.022Z] TOOL CALL #7: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/page-385.json'))\ne=d['entries'][0]\nprint(json.dumps({k:v for k,v in e.items() if k!='nodes'},ensure_ascii=False,indent=1)[:2500])\nprint(json.dumps(e['nodes'][0],ensure_ascii=False,indent=1)[:2500])\n\""
}
```


## [2026-09-14T01:56:52.258Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"sk(h)ai\\|skhai\\|sk̂hai\" POK_full.txt | head -20; echo ---; grep -n \"917\" POK_full.txt | head -5"
}
```


### [2026-09-14T01:56:52.418Z] TOOL RESULT

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
   "note": "'peg-. Breast. 1. Suffixed variant form *pek-tos- in Latin pectus, breast: PECTORAL; EXPECTORATE, PARAPET. 2. Possibly suffixed variant form *pek-so- in Sanskrit p
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


### [2026-09-14T01:56:52.537Z] TOOL RESULT

```
---
72562:References: WP. II 483 ff., WH. II 507 ff., 511, EM2 917 ff., Trautmann 248, 258 ff., 273. 
75059:Page(s): 916-917 
77090:strain '; russ. sd/r;^' "veritable, genuine'; compare also above S. 917; 
77490:Page(s):917 
77727:Page(s): 917-918
```


## [2026-09-14T01:56:55.929Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '77440,77500p' POK_full.txt; echo ==========; sed -n '77690,77740p' POK_full.txt; echo =========; sed -n '75020,75062p' POK_full.txt"
}
```


### [2026-09-14T01:56:56.016Z] TOOL RESULT

```
Exit code 1
schuren 'scour, rub, clean, clean, sweep, wash away ' = Danish skure, Swedish skura6s.; 

with formants -/o-. Middle High German schiel {*skeulo-) "splinter, abgesprungenes or 
ragged piece'; 



Latvian skurinat lausen, ruffle; tousle ', refl. "sich kratzen, krauen'; 

with ^extension: Middle Irish scofha/d 'cWps, cuts' {*skutati), scofht "cutting edge, cusp, 
peak', also " hair lock '; Middle High German hudele rag'; Lithuanian skutu, skust/" scrape, 
peel ', skutas ^scrap, shred, rag', skutenos' scrapings ', Old Lithuanian skutna^ bald head, 
worn out place'; Latvian skuot/t/es ' s\c\r\ schuppen', skaute^ sharp edge'; Lithuanian 
sk/aut/s ^p'\ece Zeug', skiautere^ cockscomb, crest on head of cock, rooster's comb '; 
perhaps Latin scutilus^iWiu' and gr. OKUTaAn "club, mace, joint, stick', qkutqAov ds., 
aKUTaAi(; "staff, cudgel, club, Waize' (*"cleaved Aststiick' or likewise); here OKUTri KscpaAr) 
Hes., GKUTQ Tov TpaxH^ov. IiKsAoi Hes.; 

about East Lithuanian s/ri/e'/5s"rag' compare Specht Indo Germanic Dekl. 56; thereafter 
probably skvernas 6s. from *skernas. 

References: WP. II 552 f. 
Page(s): 954 

Root / lemma: (s)k(h)ai-, (s)k(h)ai-d-, (s)k(h)ai-t- 

Meaning: to hit, kick 

Material: Latin caedo, -ere {occTdo eic.) "hew, hit, strike, slay', cae'o'es"Schlachten, 

Morden', caementum {*caid-smento-) "Bruchstein', caeA//?? "chisel' {*caid-slo-), caia 

{*caidja) f. "cudgel ', caid, -are'hew, hit, strike', ancaesa\asa caelata', ana/en. "small 

shield' ( *ambi-caid-sli-)\ 

alb. qieirsky, heaven' from Italian cielo "sky' < Latin caelum (1) -/n. "the burin or 
engraving tool', caelum (2) -/n. "the heavens, sky, air, climate. Esp. heaven as the home 
of the gods; fig., heaven as the height of joy, renown, etc..'. 

k(h)ai-\v\ mnl. /7e/e"Rammblock', Middle High German Modern High German heie 
"beetle, hammer, wooden hammer, Ramme', mnl. heien^hW, bump, poke, rammen'. 
Modern High German Swiss Z?©/©/? "stomp, hemp break, rupture'; 

khai-t-\v\ Armenian xaif "prick, prick, sting', xait'em^ prick ', xlt'am'be anxious ', xlt" 
grieving heit, heftiger pain'; against it xlrt's\.u\z\g, anxious, argwohnisch' from *khid-ro-\ 

References: WP. II 538, WH. I 44, 45, 129, 130, 131; about Old Indie khidatrre\U, 
presses' [a), secondary khedai. "Druck, load' s. J. Wackernagel Stud. A. Grierson, 826- 
28. 
Page(s):917 



Root / lemma: (s)k(h)ed-, (s)k(h)e-n-d- 

Meaning: to crush, scatter 

Note: (extension from sek- "cut, clip') 

Material: Old Indie s/r^ao'a/e (uncovered) 'splits' {*skhnd-l)\ Avestan scandayeiti^ breaks, 
(eval):1: ========= not found
```


## [2026-09-14T01:57:40.571Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AHD watkins kai ===\"; grep -n \"kaə-id\\|kae-id\\|caedere\\|caementum\" AHD_watkins1985.txt | head -20; echo \"=== KLN Caesar/kaiser ===\"; grep -n -i \"Kaiser\\b\" KLN_1966.txt | head -10; echo \"=== KLN czar ===\"; grep -n -i \"^czar\\|czar,\" KLN_1966.txt | head -10"
}
```


### [2026-09-14T01:57:40.710Z] TOOL RESULT

```
=== AHD watkins kai ===
566:kae-id-. To strike. 1. Latin caedere, to cut, strike: CAE- SURA, CEMENT, CESTUS2, CHISEL, -CIDE, SCISSORS; AB- SCISE, CIRCUMCISE, CONCISE, DECIDE, EXCISE2, INCISE, PRECISE, RECISION. 2. Latin caelum (? < *caedum), sculptor’s chisel: CAELUM. [Pok. (s)k(h)ai- 917.] kagh-. To catch, seize; wickerwork, fence. 1. Germanic *hag- in: a. Old French hagard, wild, wild hawk (< “raptor”): HAGGARD; b. Germanic *hagén- in Old Eng- lish haga, hedge, hawthorn: HAW?; c. Germanic *hagj6é in Old English hecg, hedge: HEDGE. 2. Suffixed unaspirated form *kag-yon- in Gaulish caio, rampart, retaining wall (> Old French quai, quay): (CAY), KEY?, QUAY. 3. Possi- ble variant *kogh- in: a. Latin cohum, strap from yoke to harness: INCHOATE; b. possibly Latin cdlum, sieve (< wickerwork), and its derivative céldre, to filter: COLAN- DER, COULEE, (COULOIR), CULLIS; PERCOLATE. [Pok. kagh- 518.]
1208:ABAFT apo- ABANDON bha-2 ABASE bassus ABASH bat- ABASIA gWa- ABATE battuere ABBREVIATE mregh-u- ABDICATE deik- ABDUCENS deuk- ABDUCT deuk- ABELE albho- ABERRATION ers-1 ABET bheid- ABEYANCE bat- ABHOR ghers- ABIDE bheidh- ABJECT yé- ABJURE yewes- ABLATION  tele- ABLAUT apo-, kleu-1 ABLE ghabh- ABLUTION leu(@)- ABNEGATE ne ABNORMAL gné- ABODE bheidh- ABOLISH al-3 ABORT er-! ABOUND wed-1 ABOUT ud- ABOVE upo ABRADE réd- ABRIDGE mregh-u- ABROGATE reg-1 ABROSIA gWere-4 ABRUPT reup- ABSCESS ked- ABSCISE kae-id- ABSCOND dhé-1 ABSENT eS- ABSOLUTE leu-1 ABSOLVE feu-1 ABSORB srebh- ABSTAIN ten- ABSTRACT tragh- ABSTRUSE treud- ABSURD swer-2 ABULIA gWele-1 ABUT bhau- ABYSS gWadh- ACANTHO- ak- ACANTHOPTERYGIAN pet- ACANTHUS ak- ACAPNIA kwép- ACCEDE ked- ACCELERATE kel-3 ACCENT kan- ACCEPT kap- ACCESS ked- ACCIDENT kad- ACCIPITER Oku- ACCLAIM kele-2 ACCLIVITY klel- ACCOLADE kwel-1 ACCOMMODATE med- ACCOMPLISH pele-1 ACCORD kerd-1 accosT kost- ACCOUNT peu- ACCRUE_ ker-3 ACCUMBENT keu-2 ACCUMULATE keue-2 ACCURATE cira ACERATE ak- ACERB ak- ACETABULUM ak- ACETIC ak- ACETUM = ak- ACHALASIA ghé-
1328:CABARET kamer- CABEZON kaput CABLE kap- CABRILLA kapro- CABRIOLET kapro- CACHE ag- CACHEXIA segh- caco- kakka- CACODYL kakka- CACOETHES kakka-, s(w)e- CACOPHONOUS bha-2, kakka- CACOPHONY kakka- CACUMINAL keu-2 CADASTER  steigh- CADAVER kad- CADELLE kat-1 CADENCE kad- CADENT kad- CADET kaput CADRE kWetwer- CADUCEUS kar-2 CADUCICORN kad-, ker-1 CADUCOUS kad- CAECILIAN kaiko- CAECUM kaiko- CAELUM_ kae-id- CAESURA kae-id- CAGE keua-2 CAHIER kWetwer- CAINOTOPHOBIA ken-3 CAIRD kerd-2 CAISSON kap-
1340:CELLA kel-2 CELLAR kel-2 CELLARER kel-2 CEMBALO keu-2, kleu-3 CEMENT kae-id- CEMETERY kei-1 CENACLE sker-1 -CENE_ ken-3 CENOBITE gWei-, kom CENOGENESIS ken-3 CENOTAPH dhembh-, ken-4 Cenozoic ken-3 CENSOR kens- CENSUS kens- CENT dekm CENTAL dekm CENTAVO dekm CENTENARIAN dekm CENTENARY dekm CENTENNIAL dekm CENTER kent- CENTESIMAL dekm CENTESIS kent- CENTI- dekm CENTIGRADE ghredh- CENTIME dekm CENTNER dekm CENTO kentho- CENTRIFUGAL bheug-'
1342:CENTROBARIC gWere-2 CENTUM dekm CENTURY dekm CEPHALIC ghebh-el- CEPHALO- ghebh-el- -CEPHALOUS ghebh-el- CERAMIC ker-4 CERASTES ker-! CERATODUS dent-, ker-1 CERATOID ker-! CEREAL ker-3 CEREBELLUM ker-1 CEREBRUM ker-1 CERES ker-3 CERTAIN krei- CERVINE ker-1 CERVIX ker-1 CESSION ked- CESSPOOL spirare cEsTus! kent- CEsTUS? kae-id- CHAETA ghait- CHAETOGNATH genu-2, ghait- CHAFE dhé-1, kele-1 CHAFER gep(h)- CHAFF! gep(h)- CHAIR sed-1 CHALAZA gheled- CHALAZION gheled- CHALCID ghelegh- CHALCOCITE ghelegh- CHALCOPYRITE ghelegh- CHALCOsIS ghelegh- CHALICE kal-1 CHALLENGE kel-8 CHALONE ghé- CHAMAEPHYTE dhghem- CHAMBER kamer- CHAMELEON dhghem- CHAMFER bhreg- CHAMFRON kaput CHAMOMILE dhghem-, mélon CHANCE kad- CHANCEL carcer CHANCELLOR carcer CHANCRE kar-1 CHANGE skamb- CHANT kan-
1359:-CIDE kae-id- CILIUM kel-2
1360:CINCH kenk-1 CINCTURE kenk-1 CINDER sendhro- CINEMATOGRAPH kei-3 CINEMATORADIOGRAPHY kei-3 CINERARIUM keni- CINEREOUS_ keni- CINGULUM_ kenk-1 CINQUAIN penkWe CINQUE penkWe CINQUEFOIL bhel-3, penkwe cIRcA sker-3 CIRCADIAN deiw- CIRCLE sker-3 CIRCUIT ei-1 CIRCUM-  sker-3 CIRCUMCISE kae-id- CIRCUMDUCTION deuk- CIRCUMFUSE gheu- CIRCUMLOCUTION  tolkw- CIRCUMSCRIBE skribh- CIRCUMSPECT spek- CIRCUMSTANCE sta- CIRCUMVENT gWa- CIRCUMVOLVE wel-3 cIs- ko-
1389:cons deuk- CONATION ken-1 CONCAVE keue-2 CONCEAL kel-2 CONCEDE ked- CONCEIVE kap- CONCERN krei- CONCESSION ked- CONCH konk(h)o- CONCHA konk(h)o- CONCHO- konk(h)o- CONCIERGE servus CONCILIATE kela-2 CONCISE kae-id- CONCLAVE kleu-3 CONCLUDE kleu-3 CONCOCT pekw- CONCOMITANT ei-1 CONCORD kerd-1 CONCOURSE kers-2 CONCRESCENCE ker-3 CONCRETE ker-3 CONCUBINE keu-2 CONCUPISCENCE kwép- CONCUR kers-2 CONCUSS kwét- CONDEMN dap- CONDENSE dens-2 CONDESCEND skand- CONDIGN dek-1 CONDIMENT dhé-1 CONDITION deik- CONDOLE del-3 CONDONE do- CONDOTTIERE deuk- CONDUCE deuk- CONDUCT deuk- CONDUPLICATE dwo- CONE k6-
1416:DECEIVE kap- DECEMBER dekm DECEMVIR dekm, wi-ro- DECENARY dekm DECENNIUM at-, dekm DECENT dek-! DECI- dekm DECIDE kae-id- DECIDUOUS _ kad- DECIMAL dekm DECIMATE dekm DECK! (s)teg- DECK? (s)teg- DECKLE (s)teg- DECLAIM kele-2 DECLARE kele-2 DECLINE klei- DECLIVITY kKlei- DECOCT pekw- DECOLLATE! kWwel-1 DECOLLETE kwel-1 DECOR dek-! DECORATE dek-1 DECOROUS dek-1 DECORTICATE sker-1 DECOY keue-2, to- DECREASE ker-3 DECREE krei- DECREPIT ker-2 DECREPITATE ker-2 DECUMBENT keu-2 DECUPLE dekm, pel-3 DECURRENT kers-2 DECUSSATE dekm DEDANS en DEDICATE deik- DEDUCE deuk- DEDUCT deuk- DEED dhé-1
1485:EXAMINE ag- EXAMPLE em- EXANTHEMA andh- EXARCH arkhein EXCALIBUR kal-3 EXCAVATE keue-2 EXCEED ked- EXCEL kel-6 EXCEPT kap- EXCERPT kerp- EXCISE? kae-id- EXCITE kei-3 EXCLAIM kela-2 EXCLUDE kleu-3 EXCORIATE sker-1 EXCREMENT krei- EXCRESCENCE ker-3 EXCURSION kers-2 EXECRATE Sak- EXECUTE sekw-1 EXEDRA sed-1 EXEGESIS sag- EXEMPLARY em- EXEMPLIFY em- EXEMPLUM em- EXEMPT em- EXERCISE arek- EXERGONIC werg- EXERGUE werg- EXERT ser-3 EXFOLIATE bhel-3 EXHAUST aus-2 EXHIBIT ghabh- EXHILARATE sel-2 EXHORT gher-5 EXHUME dhghem- EXIGENT ag-
1676:INCIDENT kad- INCINERATE keni- INCIPIENT kap- INCISE kae-id- INCITE kei-3 INCLINE klei- INCLUDE kleu-3 INCONDITE dhé-1 INCREASE ker-3 INCUBATE keu-2 INCULT kWwel-1 INCUMBENT keu-2 INCUNABULUM kei-1 INCUR kers-2 INCUS kau-2 INDEMNIFY dap- INDEMNITY dap- INDENT! dent- INDENTURE dent- INDEX deik- INDICATE deik- INDICT deik- INDIGEN gene- INDIGENOUS gene- INDIGENT eg- INDIGN dek-1 INDIGNANT dek-1 INDIGNATION dek-1 INDITE deik- INDOLENT del-3 INDOMITABLE deme-2 INDUCE deuk- INDURATE deru INDUSTRY en, ster-2 INEBRIATE 6g¥h- INEFFABLE bha-2 INELUCTABLE leug-1 INEPT ap-1
2129:PRECINCT kenk-! PRECIOUS per-6 PRECIPITATE kaput PRECISE kae-id- PRECLUDE kleu-3 PRECOCIOUS pekw- PRECURSOR kers-2 PREDATORY ghend- PREDECESSOR ked- PREDICATE delk- pRepicT deik- PREDOMINATE deme-1 PREEMPTION em- PREFACE bha-2 PREFECT dhé-1 PREFER bher-1 PREFIGURE dheigh- PREFIX dhig¥- PREGNABLE ghend- PREGNANT! gene- PREGNANT? per-5 PREHENSILE ghend- PREHENSION ghend- PREJUDICE deik-, yewes- PRELAPSARIAN leb-1 PRELATE telo- PRELECT leg-1 PRELIBATION [éi- PRELUDE leld- PREMATURE ma-1 PREMIER per! PREMISE (s)meit(@)- PREMIUM em- PREMONITION men-1 PREMORSE mer-2 PREMUNITION mel-3 PREPARE pere-! PREPENSE (s)pen- PREPONDERATE (S)pen- PREPOSITION apo- PREPOSTEROUS apo- PREPOTENT _poti- PREPUCE pu-! PREROGATIVE reg-1 PRESAGE sag- PRESBYOPIA per! PRESBYTER pert PRESCIENT skel- PRESCIND  skel- PRESCRIBE skribh- PRESENT! es- PRESENT? es- PRESENTIMENT sent- PRESERVE ser-! PRESIDE sed-! PRESS! per-5 PRESSURE per-5 PRESTIGE streig- PRESUME em- PRETEND ten- PRETERIT el-1!, per? PRETERMIT (s)melt(@)- PRETEXT teks- PRETZEL mregh-u- PREVAIL wal- PREVENIENT gWa- PREVENT gWa- PREVIOUS wegh- PREVISE weld- PREY ghend- PRICE per-6
2174:REBUT bhau- RECALESCENCE kele-! RECANT kan- RECAPITULATE kaput RECEDE ked- RECEIVE kap- RECENSION kens- RECENT ken-3 RECIDIVISM kad- RECIPROCAL pert RECISION kae-id- RECK reg-1 RECKLESS reg-! RECKON reg-1 RECLAIM kele-2 RECLINE klei- RECLUSE kleu-3 RECOGNIZE gnd- RECOIL (s)keu- RECOMMEND man-2 RECONDITE dhé-1 RECORD kerd-1 RECOURSE kers-2 RECOVER kap- RECREANT kerd-1 RECREMENT krei- RECRIMINATE  krei- RECRUDESCE kreud-! RECRUIT ker-3 RECTANGLE reg-1 RECTIFY dhé-1, reg-1 RECTILINEAR reg-1 RECTITUDE reg-!
2225:SCHISM skei- SCHIST skei- SCHIZO-  skei- SCHIZONT es- SCHLEP |leij- SCHLIEREN sleu- SCHLOCK | slak- SCHMALTZ mel-1 SCHMEER (s)mer-3 SCHMUCK meug-2 SCHNAUZER snu- SCHNITZEL sneit- SCHNORRER sner- SCHNOZZLE snu- SCHOLAR segh- SCHOLASTIC segh- SCHOLIUM segh- SCHOOL! segh- SCHOOL? §skel-1 SCHUss skeud- SCIENCE skei- SCILICET skei- SCINTILLA skeei- SCINTILLATE skeei- SCIOLISM skei- SCION géi-1 SCIRE FACIAS dhé-1, skei- SCISSION  skei- SCISSORS kae-id- SCLERA skele- SCLERO- skele- SCLEROMA §skela- SCLEROSIS skela- SCLEROTIC skelo- SCLEROTIUM skela- SCLEROTIZATION skela- SCLEROUS skelo- SCOFF skeubh- SCOLD sekw-3 SCOLEX skel-3 SCOLIOSIS skel-3 SCONCE? dhé-1 SCONE keu-! SCOOP skep- Scop skeubh- -SCOPE spek- -SCOPY spek- SCORCH skerbh- SCORE sker-1 SCORIA_ sker-4 scoT skeud- SCOT AND LOT skeud- SCOTOMA  skot- SCOUR! cira SCOUR2 kéwero- SCOURGE reig-1 SCOUT! ous- scouT? skeud- SCRABBLE  sker-! SCRAG gWere-4 SCRAP!  sker-1 SCRAPE sker-1 SCRATCH grat- SCREAK ker-2 SCREAM ker-2 SCREECH ker-2 SCREED skreu- SCREEN sker-1 SCREW sker-! SCRIBBLE skribh- SCRIBE skribh- SCRIMP_ skerbh- SCRIPT skribh- SCRIPTORIUM skribh- ScRIPTURE  skribh- SCROBICULATE sker-1 SCROD skreu- SCROFULA  sker-1 SCROLL skreu- SCROTUM skreu- SCRUB!  sker-1 SCRUTINY skreu- SCUDO skei- SCUFF skeubh- SCUFFLE! skeubh- SCUFFLE? skeubh- SCULPTURE skel-1 SCUM (s)keu- SCUTCH kwét- SCUTTLE! skeud- SCUTUM  skei- SCYPHISTOMA skep-, ste-men- SCYPHOZOAN skep- SCYTHE sek- SEAL! sekw-1 SEAL? selk- SEAM syi- SEANCE sed-! SEAR! saus-
=== KLN Caesar/kaiser ===
6090:Caesar,  masc.  PN.  —  L.,  of  uncertain  origin.  Cp. czar,  kaiser.
10154:czar,  tsar,  n.  —  Russ,  tsar,  fr.  earlier  tsesar’,  fr. OSlav.  cesari,  fr.  Goth,  kaisar  (which  is  rel.  to OE.  casere,  OHG.  keisar,  OFris.,  MHG.  keiser, G.  Kaiser),  ‘emperor’,  fr.  L.  Caesar,  title  adopted by  Augustus  and  the  succeeding  Roman  em¬ perors  from  the  cognomen  of  Caius  Julius Caesar.  Cp.  Caesar,  kaiser.  For  sense  develop¬ ment  cp.  Lith.  karalius,  OSlav.  kralji,  ‘king’,  fr. L.  Carolus,  ‘Charles’  in  Carolus  Magnus,  i.e. ‘Charlemagne’  (see  churl).
15876:gaussbergite,  n.,  a  kind  of  lava  ( petrogr .)  —  So called  from  Gaussberg,  a  mountain  in  Kaiser Wilhelm  II  Land,  Antarctica,  a  name  com¬ pounded  of  Gauss,  name  of  the  ship  used  by  the German  Antarctic  Expedition,  and  of  G.  Berg, ‘mountain’.  See  borough  and  subst.  suff.  -ite. Gautama,  n.,  the  name  of  many  sages,  also  sur¬ name  of  Buddha.  —  OI.  Gdtamah,  prop,  a patronymic  meaning  lit.  ‘descendant  of  the greatest  ox’,  and  superl.  of  gauh,  gen.  gdh, ‘ox,  bull,  cow’.  See  cow  and  cp.  gaur,  the  first element  in  Gaekwar  and  in  gopura  and  the  sec¬ ond  element  in  nilgai.
20524:kaimakam,  n.,  lieutenant  colonel  of  the  Turkish army.  —  Turk,  qdimaqam,  ‘deputy’,  contraction of  Arab,  qd’im  maqdm,  ‘substitute,  proxy’,  lit. ‘standing  in  the  place  (of  another)’,  fr.  qd'im, participle  of  qdma,  ‘he  stood’,  and  maqdm, ‘place’  (also  from  the  base  of  qdma),  rel.  to  Heb. and  Aram,  qum,  ‘to  arise,  stand  up’,  Heb. maqdm,  ‘place’,  Ethiop.  qdma,  ‘he  stood’,  Ak¬ kad.  kummu,  ‘place,  dwelling’,  kum,  kemu,  ‘in place  of’,  and  prob.  also  to  Akkad,  kaiamanu, ‘constant,  enduring;  the  planet  Saturn’  (whence Heb.  kiyyiln,  Syr.  ke'wdn,  Arab,  and  Pers. kaiwdn,  the  planet  Saturn’), kainite,  n.,  a  compound  of  sulfates  of  potassium and  magnesium  (mineral.)  —  G.  Kainit,  coined by  C.  F.  Zincken  in  1865  fr.  Gk.  xaiv6?,  ‘new’, which  is  cogn.  with  L.  re-cen-s,  gen.  recentis, ‘fresh,  new’,  and  suff.  -it,  which  goes  back  to to  Gk.  -tngs.  See  recent  and  subst.  suff.  -ite. Kainozoic,  adj.  —  See  Cenozoic. kajrine,  n.,  an  alkaloid  made  from  quinoline (mineral.)  —  Prob.  fr.  Gk.  xatp6;,  ‘the  right season,  the  right  time’.  Cp.  eucairite.  For  the ending  see  chem.  suff.  -iue. kaiser,  n.,  an  emperor;  esp.  (cap.)  a  German  em¬ peror.  —  G.  Kaiser,  fr.  MHG.  keiser,  fr.  OHG. keisar,  fr.  L.  Caesar,  whence  also  OE.  casere.
=== KLN czar ===
6090:Caesar,  masc.  PN.  —  L.,  of  uncertain  origin.  Cp. czar,  kaiser.
7082:cesarevitch,  n.,  title  of  the  eldest  son  of  the  czar, or  of  the  heir  to  the  Russian  throne.  —  Russ. tsesarevitch,  fr.  tsesar,  earlier  form  of  tsar, ‘czar’.  See  czar  and  cp.  czarevitch.
10154:czar,  tsar,  n.  —  Russ,  tsar,  fr.  earlier  tsesar’,  fr. OSlav.  cesari,  fr.  Goth,  kaisar  (which  is  rel.  to OE.  casere,  OHG.  keisar,  OFris.,  MHG.  keiser, G.  Kaiser),  ‘emperor’,  fr.  L.  Caesar,  title  adopted by  Augustus  and  the  succeeding  Roman  em¬ perors  from  the  cognomen  of  Caius  Julius Caesar.  Cp.  Caesar,  kaiser.  For  sense  develop¬ ment  cp.  Lith.  karalius,  OSlav.  kralji,  ‘king’,  fr. L.  Carolus,  ‘Charles’  in  Carolus  Magnus,  i.e. ‘Charlemagne’  (see  churl).
10155:czardas,  n.,  a  Hungarian  national  dance.  —  See csardas.
10156:czarevitch,  tsarevitch,  n.,  a  son  of  the  czar  (in contradistinction  to  cesarevitch,  which  denotes the  eldest  son  of  the  czar).  —  Russ,  tsarevitch, fr.  tsar.  See  czar.
10157:czarina,  tsarina,  n.,  title  of  an  empress  of  Russia.
10159:czaritza,  n.,  czarina.  —  Russ,  tsaritsa,  fr.  tsar, ‘czar’.  See  czar  and  cp.  prec.  word.
20525:OS.  kesur,  OFris.  keiser  (Goth,  kaisar  is  bor¬ rowed  fr.  Gk.  Katoap,  which  itself  is  a  loan word  fr.  L.  Caesar).  See  Caesar  and  cp.  czar, kaka,  n.,  any  of  certain  New  Zealand  parrots.  — Maori  kaka,  ‘parrot’,  imitative  of  its  cry. kakapo,  n.,  the  owl  parrot.  —  Maori.  Cp.  prec. word.
40642:Tytonidae,  n.  pi.,  a  family  of  birds  (ornithol.)  — Formed  from  prec.  word  with  suff.  -idae. tzaddik,  also  spelled  saddik,  zaddik,  n.,  1)  in  the Bible,  a  righteous  man ;  2)  in  the  modern  sense of  the  word,  a  Hasidic  spiritual  leader.  —  Heb. tzaddtq,  ‘just,  righteous',  fr.  tzddhdq,  ‘he  was just,  was  righteous’  [whence  also  tzidhek,  ‘right¬ eousness,  justice’,  tzsdhdqdh,  ‘righteousness, justice’  (in  Mishnaic  Heb.  also  ‘alms,  charity’)], which  is  rel.  to  Aram.  tzldheq,  ‘he  was  righte¬ ous',  Syr.  zadheq,  ‘(it  is)  right’),  Arab,  sadaqa, ‘he  spoke  the  truth’,  Ethiop.  sadaqa,  ‘he  was just,  was  righteous’,  Aram.  tzidhqltha,tzidhaqta, ‘a  good  deed,  charity’;  Arab.  sadaqah,  ‘alms, charity’,  is  a  loan  word  fr.  Heb.  tzedhdqdh,  in  its Mishnaic  Heb.  sense  (i.e.  ‘alms,  charity’).  Cp. the  second  element  in  Melchizedek. tzadhe,  tzade,  n.,  name  of  the  19th  letter  of  the Hebrew  alphabet.  —  Heb.  tzade,  lit.  ‘fishing hook’,  fr.  tziidh,  ‘to  hunt,  catch,  capture’;  so called  in  allusion  to  the  ancient  Hebrew  form  of this  letter.  Heb.  tziidh  (whence  tzayidh,  ‘hunt¬ ing,  game',  tzayyadh,  ‘hunter’,  rtf  tzudhdh ,  ‘prey, net;  fastness,  stronghold’,  mltzodhah,  ‘net,  trap, snare’)  is  rel.  to  Aram.-Syr.  tziidh,  ‘he  hunted’, Ugar.  sd,  Akkad,  fddu,  ‘to  hunt’,  Arab,  sada, ‘he  hunted’.  Cp.  sadhe.  Cp.  also  Sidonian. tzar,  tzarina.  —  See  czar,  czarina, tzigane,  n.,  gipsy.  —  F.,  fr.  Hung,  cigdny,  whence also  G.  Zigeuner.  Cp.  ezigany.
```


## [2026-09-14T01:57:43.486Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== ISS_alt_DKS cut kai ===\"; grep -n -i \"chelan\\|cilan\\|čīlān\\|chilan\" ISS_alt_DKS.txt | head -20; echo \"=== PHD ===\"; grep -n -i \"cylan\\|čēlān\\|celan\" PHD.txt | head; echo \"=== HRN chalangar ===\"; grep -n -i \"chalangar\\|čalangar\\|calangar\\|schlosser\" HRN.txt | head -20"
}
```


### [2026-09-14T01:57:43.600Z] TOOL RESULT

```
=== ISS_alt_DKS cut kai ===
=== PHD ===
298:čāšt [ой | N ~] lunch, meal. 1~ag [-k'] food. &а$їар [c'štk'] doctrine. čāštan, čāš- [c?s-tn'] teach. ~išn: teaching. čatrang [cting | (Ar. šatranj)] chess. *taw(la)gan [cwpk'n!! | Ar. sawlajan, N čaugān] (curved) polo-stick ; polo. CaxSágih [ch kyh] (sense of) taste. čaxšišn [chsfn! | M, J схі, N ¿aš-] taste, flavour. 148 [ME < A mh | M cy, N či] what, which. ~ ray: for what, why. ~ih: quiddity, essence. tčē [ME, v. 166] for, because, since, as, that. &ë-ëwënag [ME ^ dwynk!] how. ~ith : circumstances. čegām-iz [су?т-с | M cyg^myc], —-6(w): a little; whatever. Cegámag [cyk”mk! | N &(ag)áma] song, snatch. €éh- , —išn, v. idan. *téhag [cyhk'] grief. čehel [40 | N chil] forty. Céh-widarag [cyhwtlg] = činwad puhl. čēlān [cy”x! | = M, N ~] dagger. ~gar [-kl, -gl | N ~] swordsmith. Cér [cyl | M cyr, N —] victorious, triumphant, brave. —Ih: bravery. Cérihistan, Cérih- [cylyh-stn'] triumph, be victorious. īčīdan, čīn- [cytn', cyn- | M cyydn, cyn-, N ~] gather, pile up. ~išn: gathering. *čīdan, čēh- [cytn', cyh- | M cy-] mourn, lament, grieve. ~i8n : lamentation. ~i$nig¢ : mournful. ihr [cyhl | M cyhr, № ~] form, shape, appearance, face. žčihr(aģ) [cyhl(k') | M сулу, P -g, № ~] seed, origin; nature, essence. Cihrénidan, čihrēn- (cyhlyn-ytn'] form. Cihrig [cyhlyk'] natural. čihr-šnāsīh [суйру] physics. čim [c(y)m | M сут, N ~] reason, cause, purpose, meaning. ~ (ray): why? Cim-gó6wáàgih [сут gwh’kyh] logic. čimīģ [cymyk!] purposeful. čīn-, ~i8n, v. idan. čīnag [cynk! | P cyng, N ~a] grain, bait. Cinàr [су | N ~] oriental plane tree. činwad [cynw(p)t'], ~ puhl: the ‘divider bridge’ which separates the souls of the righteous dead, who cross, from those of the wicked, who fall off.
1478:dagger čēlān, dašnag.
3923:sword sneh, šamšër, (šafšēr). swordsmith čēlāngar.
4584:1-2čīnag čīnišn čegāmag čegām-iz Cer čēlāngar čēlān Celangar čērīh čērīh- čērīhistan čim čim-gūwāgīh čimīg 1%īdan čand, čang Cand- éandih éandal Čang-srāy čandišn L?griw! éandidan cob
=== HRN chalangar ===
```


## [2026-09-14T01:57:57.750Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== DKS chelan/swordsmith ===\"; grep -n -i \"swordsmith\\|cēlān\\|celan\\|chelan\" ISS_alt_DKS.txt | head -20; echo \"=== NYB ===\"; grep -n -i \"cylan\\|čēlān\\|celan\" NYB_vol2_glossary.txt | head; echo \"=== HUB ===\"; grep -n -i \"schlosser\\|calangar\\|čalangar\" HUB.txt | head"
}
```


### [2026-09-14T01:57:57.870Z] TOOL RESULT

```
=== DKS chelan/swordsmith ===
2193:cülonyau inst. plur. "with weapons’, 2 247408 cálonyau nugthuru Айде bindi bihiyu 'they pierce with the сйопа- weapons very exceedingly savagely’. From *čilauna-, Sogd. Man. £y 8nyh-, Zor.P. (Vid. 8:90) čyl’n-kl *celan-kar ‘maker of weapons’, to base hai-:ci-, O.Pers, акаубкп$ ‘sword’, Sogd, kyu'k, with IE Pok. 917 (s)&(/t)at- ' to cut’, Lat. caedō, caelum ‘chisel’, and the ci- of BS cimara- rendered by Chinese 'iron', Tib. ‘copper’, Waigali Cümür, Pašai &mar (BS Samghata-sütra G 37, 85v3); R.L. Turner, Comparative Dictionary, p. 828), and Kharosthi of Kroraina cina cimara ‘Chinese iron’, but doubtful, since it is in a context of clothing, and may represent DS civara- 'dress' with -m- replacing -v-. "Turkish timür 'iron' may derive from this originally Iranian word. See also TPS 1955, 67-9.
=== NYB ===
1099:cand-var [cndwl] a name for the Cinvat bridge 7212, 7423. 891, — Paz. candor. From cand ‘shaking’, v. the preceding w., and var **path?, v. s. v. varısn, thus ‘the shaking *path’, a designation that has its exact counterpart in Old Icelandic Bif-rost ‘the trembling path’, the name of the bridge between this world and the beyond.
=== HUB ===
```


## [2026-09-14T01:57:59.357Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== MON چلنگر/چیلان ===\"; grep -n \"چلنگر\\|چیلان\\|چیلانگر\" MON_part1.txt MON_part2.txt | head -20; echo \"=== BQT ===\"; grep -n \"چلنگر\\|چیلان\" BQT_v1_pages.txt BQT_v2_pages.txt | head -20"
}
```


### [2026-09-14T01:57:59.484Z] TOOL RESULT

```
=== MON چلنگر/چیلان ===
MON_part1.txt:51164:چلنگر: 1۲ ( - چلینگر چیلانگر ] 
MON_part1.txt:51909:جیلان: «2اه آقس. چلنگر] (.) آلات و 
=== BQT ===
BQT_v2_pages.txt:7900: ‫چیلان ‪ -‬با ثالی مجپول بکرویزلنان»‬
BQT_v2_pages.txt:7908:‫بمعنی چیلان باشد که عناب است وآنرا سنجد‬                 ‫چه چیزه بوذ کرمیب را کویند که شتا فرین‬
BQT_v2_pages.txt:7937:                                            ‫«گللاب ‪ , ۰۳۲۰‬رك ‪ :‬چیلانه ‪.‬‬
```


## [2026-09-14T01:58:12.246Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '2188,2198p' ISS_alt_DKS.txt; echo \"=========MON\"; sed -n '51160,51170p' MON_part1.txt; echo \"---\"; sed -n '51905,51915p' MON_part1.txt"
}
```


### [2026-09-14T01:58:12.437Z] TOOL RESULT

```
cira — cista- 103 bacirdi 'spark', Pašto bacarrai, Waxi сэгах. Base Rai-:(i-, see also Aasai 'fever', tcülve ‘splendid’, hamjsūl- 'to kindle’. IE Pok. 319 &di-:ki- 'to be hor’, Got. taisam dat. plur., rendering Greek Aaurrás ‘lamp ', from *kat-es-; Lir, kaistù, kaitaŭ, kaisti ‘become hot’. From IE Aa-i-, beside Ёй-и- (see Pok. 595). The form čira- is like Greek cxipov ‘umbrella’, from IE skai-, beside сках 'shade'. Earlier see AJON 1, 1959, 120-5.
cirvà 'how', see s.v. cera-.
cile ‘dress’, plural, Z 2-44 cile varata bavsga mudiñi hamtsa higyo jsa ggadüre ' garments there thick, of the dead, lie with the excrements’; Z 22:329 rrusto cilo vīri ' against the red robe (of the b/ksu-mendicant)'; parallel to К 4150-1 rrusti-vrrdhdimn satt, = К. 43:169 rrusti-vrrihave satti ‘a person dressed in red’ (that is the kasaya-red robe)’; K 47:57 cala basta 'she bound ор the garment’; adjective п 71:'r0-1 cilaja namata 'felt for garments’, From base kai- ‘о cover’, Róiáni cil 'large woman's head-dress’, Yazg. cil ' head-dress', O.Ind. civara-, cira-, adjective сайа-, BS cela-, cedaka-, cellaka-, caila-, Pali cela-, Prakrit cela-. Possibly Lat. cilium 'eyelid', Oscan kaila ' house' (rather than base Рок. 553 kel-). See also thauracaiha-.
cilai ‘пате’, v 3:10 u cilai spáta ‘and the spáta-official Cilai'.
cilaka- ‘how much’, see calaka-, culaka-.
cülonyau inst. plur. "with weapons’, 2 247408 cálonyau nugthuru Айде bindi bihiyu 'they pierce with the сйопа- weapons very exceedingly savagely’. From *čilauna-, Sogd. Man. £y 8nyh-, Zor.P. (Vid. 8:90) čyl’n-kl *celan-kar ‘maker of weapons’, to base hai-:ci-, O.Pers, акаубкп$ ‘sword’, Sogd, kyu'k, with IE Pok. 917 (s)&(/t)at- ' to cut’, Lat. caedō, caelum ‘chisel’, and the ci- of BS cimara- rendered by Chinese 'iron', Tib. ‘copper’, Waigali Cümür, Pašai &mar (BS Samghata-sütra G 37, 85v3); R.L. Turner, Comparative Dictionary, p. 828), and Kharosthi of Kroraina cina cimara ‘Chinese iron’, but doubtful, since it is in a context of clothing, and may represent DS civara- 'dress' with -m- replacing -v-. "Turkish timür 'iron' may derive from this originally Iranian word. See also TPS 1955, 67-9.
cista- ' youthful, SuvP. 63r4 güttirna isvart tsāttauñä jsa u cistiye jsa Шуе meva jsa ‘with gotra-family, ownership, riches and youth, with that intoxication', BS aísvarya- mada-mattena kula-bhoga-mada-mattena ca tàrunya-mada- mattena, whence cistzye jsa renders tārunya- ‘tenderness’; 1 163, 79r1 ysäda pashyasti cista райтті ‘it makes the old young again’, BS vrddha-: Z 362 suhautta Кайа bii айпа cista káde 'all must be thought to be happy, healthy, very youthful (vigorous?)'; п 35:29 brrryinahye cesta jiske hsauda-bahoe ‘splendid young girls, nubile’, =IN 3726 caista, = 1 4745 cesta; with -aka- її 130bz chaugalakai ара айй caistaka jtyaka ‘ardent in limbs, untaught(?), youthful life’; ur 69:92-3 wma са тайа caistaka sfirau ‘уои who are now youthful'; 11 44:47 caistà hvandà ' of young men’; K 38:133 саіѕій hā pa-sse tti haidari áve ‘then five hundred Kiznari-women came there’, From kai-:či- ' youth', with various suffixes Oss, D. kizgä, I. булк ‘girl’; O.Ind. (AV) Riford- ‘young animal’, So far not traced outside Irano-Indian. The -ist- indicates older £id- or čit- or @18-.
104 сЊајѕа — ceyyau
cihajsá 'slimy', Sid. 4v3 cu silisd sti si heard и sürd u tcarba u garkhá u cihajsd "what is phlegm, that is sweet and saline and fatty and heavy and slimy’, BS madhuro lavanah. snigdho guru-slegmà 'tipicchilah; Tib. bad-han ni mmar-ba dan, lan-hwahi ro bro-ba dam, hjam-po dam, l&i-ha dan, fin-tu hbyil-baho. From *čifa- with adjective suffix -jsa-, to Oss. D. c'ifá, I. c'yf ' mud, slush, puddle’, І. c'yf-don ' muddy place or water’, adjective D. c'ifgur, І. ce'yfd£yn; D. c'if-dzast, І, c'yf-dzast ' puddle, swamp, marsh’, and adjective 'swampy'. Note also D. c'umur, I. Pisi ' dirty’, c'illon ' dirtied'. Connexion not traced.
cu ‘what’, interrogative, relative; *that' of subordinate clause, V 77, 145У4 £u daiya vamña ' what do you see now?', Tib. & sig mthop; V 332, 2515 cu nama gyastyau balysyau sa balysana tcarimd 'what indeed, deva Buddhas (voc. plur.), is this Buddha зрћеге?', BS G 37, 2227 kim пйтач iyam bhagavan loka-dhütuh; v 328, 775 kye kädäna cu racai ' for what reason, what is the cause’, B8 G 36, 523 ko bhagavan hetuh kah pratyayah; v 73, 41V cu te saittd "what does it seem to you?', BS С 37, 31b3 tat kim manyase; relative, V 69, 805 cu Hye kädägānä йаш hddátand mástará hämäte ‘whose is the evil, to him the evil becomes greater' ; BS G 37, 11b6 yas cemam samghüta- pratiksiped ayam tato bahutaram раракат; ‘that’, v 329, учу iru iüru...cu thu gyastanu gyastu balysu Ийе ttündrüme bátame рий 'good, good that you ask the deva of devas Buddha these doubts; си bura ' whoever’, V 335, 3471 cu buro vā tr-sahasrye mahāsahasrye balysaña їсйтїта paryāvanna uysnora, u 14 bišiä praciya-(sambu- ddha háymaro ' whatever beings have arrived in the three- thousand great-thousand Buddha world, they all become pratyeka-buddhas!, BS G 37, 31a1 ye tri-sühasra-mahüsa- hasryam lokadhatau satvas te pratyeka-buddhà bhaveyuh. See also ca, cd, ci, ce, kyä, kyi, kye. Base ka- and či- ‘what’, IE Pok. 644-8 А%о-, kti-
cü 'who indeed’, from си and и < uta, V 343, 9514 cü hemdaryau bal(ysüynyau tcarimyau путо(ға tsyutandá muhu varä ‘what beings from other worlds have come towards me’, BS С 37, 79bs janaküyam ügacchantam mamaantike.
=========MON
خود را چرکین و ملوث سازد. کسی که 
عقلش ناقص باشد. بی‌نزا کت. 


چلنگر: 1۲ ( - چلینگر چیلانگر ] 


(ص‌شغل.) آنکه آهن آلات خرد از قبیل 
قفل» کلید» چفت و رزه» زنجیر» انبر» میخ و 
مانند آنها سازد. 

---
هر بودنی» شیل؛ مق. ناجمز» معد و م. 
جیستان: 0- )ده [- چست آن| (امر.) 
نغزء اغلو طه. 

جیلان: «2اه آقس. چلنگر] (.) آلات و 
ادواتی که از آهن سازند مانند زرفین در و 
زنجیر و حلقه‌های کوچک و براق زین و 
لگاماسب و رکاب. 

چین. اه (ا.) شکن شکنجء چروکك» تا. 
ین بر ابرو افکندن: (کذ.) روی درهم
```


## [2026-09-14T01:58:34.013Z] TOOL CALL #15: Bash

```json
{
 "command": "sed -n 1,40p tools/fetch_source.py; echo ----; sed -n 1,40p tools/ref_page.py"
}
```


### [2026-09-14T01:58:34.071Z] TOOL RESULT

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
----
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


## [2026-09-14T01:58:39.772Z] TOOL CALL #16: Bash

```json
{
 "command": "for u in \"https://en.wiktionary.org/wiki/caedo\" \"https://www.etymonline.com/word/Caesar\" \"https://en.wiktionary.org/wiki/%D1%86%D0%B0%D1%80%D1%8C\" \"https://en.wiktionary.org/wiki/%D9%82%D9%8A%D8%B5%D8%B1\" \"https://en.wiktionary.org/wiki/Jersey\" \"https://www.etymonline.com/word/jersey\" \"https://www.etymonline.com/word/cement\" \"https://en.wiktionary.org/wiki/%D8%B3%DB%8C%D9%85%D8%A7%D9%86\"; do echo \"### $u\"; python3 tools/fetch_source.py \"$u\" --note \"page 457, root Skhai: Caesar/tsar/jersey/cement chain\" 2>&1 | tail -2; done"
}
```


### [2026-09-14T01:58:44.638Z] TOOL RESULT

```
### https://en.wiktionary.org/wiki/caedo
/home/sfmqrb/git/rishe/data/verification/sources/web/1d32035c6ff49e96.txt
### https://www.etymonline.com/word/Caesar
/home/sfmqrb/git/rishe/data/verification/sources/web/132daac0a2d54f44.txt
### https://en.wiktionary.org/wiki/%D1%86%D0%B0%D1%80%D1%8C
/home/sfmqrb/git/rishe/data/verification/sources/web/205598e022ee0692.txt
### https://en.wiktionary.org/wiki/%D9%82%D9%8A%D8%B5%D8%B1
/home/sfmqrb/git/rishe/data/verification/sources/web/429358e2bb465148.txt
### https://en.wiktionary.org/wiki/Jersey
/home/sfmqrb/git/rishe/data/verification/sources/web/81b86b0f406609d1.txt
### https://www.etymonline.com/word/jersey
/home/sfmqrb/git/rishe/data/verification/sources/web/0f19117f16dcc33d.txt
### https://www.etymonline.com/word/cement
/home/sfmqrb/git/rishe/data/verification/sources/web/b64c036871577894.txt
### https://en.wiktionary.org/wiki/%D8%B3%DB%8C%D9%85%D8%A7%D9%86
/home/sfmqrb/git/rishe/data/verification/sources/web/c89b29bf6a9eae26.txt
```


## [2026-09-14T01:58:47.222Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"#### caedo\"; grep -n -A12 \"^Etymology\" 1d32035c6ff49e96.txt | head -40; echo; echo \"#### Caesar etymonline\"; sed -n '1,80p' 132daac0a2d54f44.txt | grep -n -i -A6 \"caesar\" | head -60"
}
```


### [2026-09-14T01:58:47.301Z] TOOL RESULT

```
#### caedo

#### Caesar etymonline
1:URL: https://www.etymonline.com/word/Caesar
2-FETCHED: 2026-09-14T01:58:41Z
3-STATUS: 200
4:TITLE: Caesar - Etymology, Origin & Meaning of the Name
5-
6:Caesar - Etymology, Origin & Meaning of the Name 
7-
8- Search 
9- Log in 
10-
11- Columns 
12- Forum 
--
21: Origin and history of Caesar 
22-
23: Caesar 
24-
25: "an emperor, a ruler, a dictator," late 14c., cesar , from Cæsar , originally a surname of the Julian gens in Rome, elevated to a title after Caius Julius Caesar (100 B.C.E.-44 B.C.E.) became dictator; it was used as a title of emperors down to Hadrian (138 C.E.). The name is of uncertain origin; Pliny derives it from caesaries "head of hair," because the future dictator was born with a full one; Century Dictionary suggests Latin caesius "bluish-gray" (of the eyes), also used as a proper name. Also compare caesarian .
26-
27- Old English had casere , which would have yielded modern *coser , but it was replaced in Middle English by keiser (c. 1200), from Norse or Low German, and later by the French or Latin form of the name. Cæsar also is the root of German Kaiser and Russian tsar (see czar ). He competes as progenitor of words for "king" with Charlemagne (Latin Carolus ), as in Lithuanian karalius , Polish krol .
28-
29: The use in reference to "temporal power as the object of obedience" (contrasted with God ) is from Matthew xxii.21. Caesar's wife (1570s) as the figure of a person who should be above suspicion is from Plutarch. In U.S. slang c. 1900, a sheriff was Great Seizer .
30- also from late 14c. 
31-
32: Entries linking to Caesar 
33-
34: caesarian (n.) 
35-
36: "delivery of a child by cutting through the abdomen of the mother," 1923, shortening of Caesarian section (1610s); caesar as "baby delivered by caesarian section is from 1530s. Section (n.) here has the literal Latin sense of "act or action of cutting," which is attested from 1550s in English but is rare outside of medicine.
37-
38: Supposedly from Caius Julius Caesar , who was said to have been delivered surgically. Thus also legend traces his cognomen to Latin caesus, past participle of caedere "to cut" (see -cide ). But if this is the etymology of the name, it was likely an ancestor who was so born (Caesar's mother lived to see his triumphs and such operations would have been fatal to the woman in ancient times). Rather, caesar here may come directly from caesus .
39-
40- The operation was prescribed in Rome for cases of dead mothers; the first recorded instance of it being performed on a living woman is c. 1500, but as late as the early 19c., before antiseptics and blood transfusions, it had a 50% mortality rate.
41-
42- czar (n.) 
43-
44: the common title of the emperor of Russia, 1550s, from Russian tsar , from Old Slavic tsesari , from Gothic kaisar , from Greek kaisar , from Latin Caesar . First adopted by Russian emperor Ivan IV, 1547.
45-
46- The spelling with 
47- cz- is against the usage of all Slavonic languages; the word was so spelt by Herberstein, 
48- Rerum Moscovit. Commentarii , 1549, the chief early source of knowledge as to Russia in Western Europe, whence it passed into the Western Languages generally; in some of these it is now old-fashioned; the usual Ger. form is now 
49- zar ; French adopted 
50- tsar during the 19th c. This also became frequent in English towards the end of that century, having been adopted by the 
--
55: Caesarea 
56- Cesar 
57- kaiser 
58- See All Related Words (5) 
59-
60- Advertisement Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.
61-
--
66: 1858 in reference to the emperors of Austria and (after 1870) Germany, from German Kaiser, Bavarian and Austrian spelling variant of of Middle High German keisar, from Old High German keisar "emperor," an early borrowing of Latin cognomen Caesar. The Germanic peoples seem to have
67-
68- August 
69-
70: sixth month of the later Roman calendar, renamed from Sextilis (literally "sixth") in 8 B.C.E. to honor emperor Augustus Caesar..., literally "Venerable Caesar" (see august (adj.), and compare Augustus)....
71-
72- punt 
73-
```


## [2026-09-14T01:58:52.923Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && grep -n -i \"Proto-Italic\\|kh₂eyd\\|keh₂id\\|caedō\" 1d32035c6ff49e96.txt | head -20; echo \"#### tsar ru\"; grep -n -i \"Gothic\\|Old Church Slavonic\\|цѣсарь\\|Etymology\" 205598e022ee0692.txt | head -20"
}
```


### [2026-09-14T01:58:52.995Z] TOOL RESULT

```
182: Proto-Indo-European *kh₂eyd- 
187: Proto-Italic *kaidō 
188: Latin caedō 
190: From Proto-Italic *kaidō , from Proto-Indo-European *keh₂id- , *kh₂eyd- ( “ to cut, hew ” ) . [ 1 ] 
206: caedō ( present infinitive caedere , perfect active cecīdī , supine caesum ) ; third conjugation 
225:    Conjugation of caedō ( third conjugation )
249: caedō 
725: ^ De Vaan, Michiel ( 2008 ), “ caedō, -ere ”, in Etymological Dictionary of Latin and the other Italic Languages (Leiden Indo-European Etymological Dictionary Series; 7), Leiden, Boston: Brill, →ISBN , pages 79-80 
749: Latin terms derived from the Proto-Indo-European root *kh₂eyd- 
750: Latin terms derived from Proto-Italic 
751: Latin terms inherited from Proto-Italic 
#### tsar ru
57: Old Church Slavonic 
59: Toggle Old Church Slavonic subsection 
62: Etymology 
79: Etymology 
195: Old Church Slavonic
198: Etymology
284: “ царь ”, in GORAZD [ Old Church Slavonic Digital Hub ], http://gorazd.org , 2016—2026 
294: Etymology
297: Etymology tree
302: Old East Slavic цѣсарь ( cěsarĭ ) 
306: Inherited from Old East Slavic цьсарь ( cĭsarĭ ) , from цѣсарь ( cěsarĭ ) , from Proto-Slavic *cěsařь , from a Germanic language, from Proto-Germanic *kaisaraz , from Latin Caesar . Doublet of ка́йзер ( kájzer ) , ке́сарь ( késarʹ ) , це́зарь ( cézarʹ ) , and це́сарь ( césarʹ ) .
619: Categories : Old Church Slavonic terms inherited from Proto-Slavic 
620: Old Church Slavonic terms derived from Proto-Slavic 
621: Old Church Slavonic terms derived from Germanic languages 
622: Old Church Slavonic terms derived from Proto-Germanic 
623: Old Church Slavonic terms derived from Latin 
624: Old Church Slavonic lemmas 
625: Old Church Slavonic nouns 
626: Old Church Slavonic masculine nouns 
627: Old Church Slavonic terms with quotations
```


## [2026-09-14T01:58:55.701Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"#### Arabic qaysar\"; grep -n -i -B2 -A6 \"Etymology\" 429358e2bb465148.txt | head -60"
}
```


### [2026-09-14T01:58:55.813Z] TOOL RESULT

```
#### Arabic qaysar
60-
61- 1.1 
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Proper noun 
--
165- [ edit ] 
166-
167: Etymology
168- [ edit ] 
169-
170- From Latin Caesar , possibly through Ancient Greek Καῖσαρ ( Kaîsar ) and/or Aramaic קיסר ( qēsar ) . Uses for modern monarchs are semantic loans from Russian царь ( carʹ ) and German Kaiser , themselves from the Latin.
171-
172- Pronunciation
173- [ edit ]
```


## [2026-09-14T01:59:01.409Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"#### Jersey wikt\"; grep -n -i -A8 \"^ Etymology$\" 81b86b0f406609d1.txt | head -60; echo; echo \"#### jersey etymonline\"; sed -n '20,60p' 0f19117f16dcc33d.txt"
}
```


### [2026-09-14T01:59:02.501Z] TOOL RESULT

```
#### Jersey wikt
275: Etymology
276- [ edit ] 
277-
278- From Middle English Gersey , from Anglo-Norman Gersui , further etymology disputed. Probably from Old Norse [Term?] , compound of Geirs ( “ Geirr 's ” ) +‎ ey ( “ island ” ) . Also occasionally and historically connected to Latin Caesarea , a common name given to locations conquered by the Romans in honor of Caesar (compare French Césarée ). The latter theory still bestows the Latin translation of the island.
279-
280- Pronunciation
281- [ edit ] 
282-
283- ( Received Pronunciation , Australia ) IPA ( key ) : /ˈd͡ʒɜːzi/ 
--
531: Etymology
532- [ edit ] 
533-
534- Borrowed from English Jersey .
535-
536- Proper noun
537- [ edit ] 
538-
539- Jersey ( genitive Jerseys ) 

#### jersey etymonline

 Origin and history of jersey 

 jersey (n.) 

 1580s as a type of knitted cloth; 1842 as a breed of cattle; both from Jersey , one of the Channel Islands. Its name is said to be a corruption of Latin Caesarea , the Roman name for the island (or another near it), influenced by Old English ey "island" (see island ); but it is perhaps rather a Viking name (perhaps meaning "Geirr's island").

 The meaning "woolen knitted close-fitting tunic," especially one worn during sporting events, is from 1845. In American English, short for New Jersey from 1758. Related: Jerseyman .
 also from 1580s 

 Entries linking to jersey 

 island (n.) 

 1590s, earlier yland (c. 1300), from Old English igland , iegland "an island," from ieg "island" (from Proto-Germanic *awjo "thing on the water," from PIE root *akwa- "water") + land (n.).

 The spelling of the first syllable was modified from 16c. by association with similar but unrelated isle . The second syllable was added to distinguish it from homonyms, especially Old English ea "water" (see ea ). Similar formation are in Old Frisian eiland , Middle Dutch eyland , German Eiland , Danish öland , etc.

 In place names, Old English ieg is often used of "slightly raised dry ground offering settlement sites in areas surrounded by marsh or subject to flooding" [Cambridge Dictionary of English Place-Names], as probably in Isle of Ely . Old English had ealand "river-land, watered place, meadow by a river."

 As an adjective from 1620s. Island univers e "solar system" (1846) translates German Weltinsel (von Humboldt, 1845). Related: Islander .

 Guernsey 

 Channel Island, the name is Viking. The second element of the name is Old Norse ey "island" (compare Jersey ); the first element uncertain, traditionally meaning "green," but perhaps rather representing a Viking personal name, such as Grani .

 Like neighboring Jersey , its name also was taken as the word for a coarse, close-fitting vest of wool (1839), worn originally by seamen, and in Australia the word supplies many of the usages of jersey in U.S. As a type of cattle bred there, from 1784.

 New Jersey 
 Orkney 
 See All Related Words (4) 

 Advertisement Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.

 More to explore

 sweater 

 "woolen vest or jersey, originally worn in rowing," 1882, from earlier sweaters "clothing worn to produce sweating and reduce...

 docudrama
```


## [2026-09-14T01:59:09.034Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && sed -n '20,40p' b64c036871577894.txt; echo \"#### سیمان\"; grep -n -i -A6 \"Etymology\" c89b29bf6a9eae26.txt | head -30"
}
```


### [2026-09-14T01:59:09.102Z] TOOL RESULT

```
 Origin and history of cement 

 cement (n.) 

 kind of mortar or other substance that hardens as it dries, used to bind, c. 1300, from Old French ciment "cement, mortar, pitch," from Latin cæmenta "stone chips used for making mortar" (singular caementum ), from caedere "to cut down, chop, beat, hew, fell, slay" (from PIE root *kae-id- "to strike"). The sense evolution from "small broken stones" to "powdered stones used in construction" took place before the word reached English. Cement-mixer is from 1875.

 The term properly includes papier maché, gums, glues, mucilages, limes, mortars, and a great number of compounds of such nature as to admit of their assuming, under certain conditions, sticky, tenacious, or stone-like consistency. [Century Dictionary]
 also from c. 1300 

 cement (v.) 

 c. 1400, "to bind (solid bodies) together with or as with cement," from cement (n.) or Old French cimenter . The figurative sense "to unite firmly" is from c. 1600. Related: Cemented ; cementing .
 also from c. 1400 

 Entries linking to cement 

 cementation (n.) 

 "process of producing cohesion," 1590s, from cement (v.) + noun ending -ation .

#### سیمان
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Noun 
--
150: Etymology
151- [ edit ] 
152-
153: Etymology tree
154-
155- Proto-Indo-European *kh₂eyd- 
156-
157- Proto-Indo-European *-eti 
158-
159- Proto-Indo-European *kh₂éydeti 
--
260: Pages with etymology trees 
261: Persian entries with etymology trees 
262: Persian entries with etymology texts 
263- Pages using etymon with no ID 
264- Pages with entries 
265- Pages with 1 entry 
266-
267- This page was last edited on 19 August 2026, at 17:36.
268-
```


## [2026-09-14T01:59:10.945Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && sed -n '150,200p' c89b29bf6a9eae26.txt"
}
```


### [2026-09-14T01:59:10.991Z] TOOL RESULT

```
 Etymology
 [ edit ] 

 Etymology tree

 Proto-Indo-European *kh₂eyd- 

 Proto-Indo-European *-eti 

 Proto-Indo-European *kh₂éydeti 
 Proto-Italic *kaidō 
 Latin caedō 

 Proto-Indo-European *-mn̥ 
 Proto-Indo-European *-mn̥tom 
 Proto-Italic *-mentom 
 Latin -mentum 

 Latin caementum 
 Old French ciment 
 French ciment bor. 
 Persian سیمان 

 Borrowed from French ciment .

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /siː.ˈmaːn/ 

 ( Dari, formal ) IPA ( key ) : [siː.mɑ́ːn] 

 ( Dari, formal ) IPA ( key ) : [siː.mɑ́ːn] 
 ( Kabuli ) IPA ( key ) : [siː.mɑ́ːn] 

 ( Hazaragi ) IPA ( key ) : [si.mɔ́ːn] 

 ( Iran, formal ) IPA ( key ) : [siː.mɒ́ːn] 

 ( Tajik, formal ) IPA ( key ) : [si.mɔ́n] 

 Rhymes: -aːn 

 Readings

 Classical reading ? 

 sīmān

 Dari reading ?
```


## [2026-09-14T01:59:17.253Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### MON سمنت\"; grep -n \"سمنت\\|سیمان\" MON_part1.txt MON_part2.txt | head -10; echo \"### MON سزار/تزار/ژرسه\"; grep -n \"سزارین\\|تزار\\|ژرسه\\|سزار\" MON_part1.txt MON_part2.txt | head -12; echo \"### BQT v1 قیصر\"; grep -n \"قیصر\" BQT_v1_pages.txt | head -10"
}
```


### [2026-09-14T01:59:17.393Z] TOOL RESULT

```
### MON سمنت
MON_part2.txt:10671:که سیمان با آهکث را برای ساختمان در 
MON_part2.txt:12518:جدولی که از آجر یا سیمان در جهت 
MON_part2.txt:41154:لوله‌های فلزی یا سیمانی و غیره در زیر 
MON_part2.txt:42454:خاک آن را با سیمان مخلوط کنند و در 
MON_part2.txt:67916:و در سیمان کار گذاشته شده. نوعی آجر که 
MON_part2.txt:67917:با سیمان و شن‌های رنگین ساخته شود. 
MON_part2.txt:70744:مسمنت (همع.) (نظ.) جانب راست میدان 
MON_part1.txt:21208:و ماسه و سیمان در بنایی برای پی‌ریزی یا 
MON_part1.txt:25566:که در نمای بنا بکار رودرا با سیمان ساروج 
MON_part1.txt:30832:سیمان و بلاتین و مانند آن. بر کردن قوه؛ 
### MON سزار/تزار/ژرسه
MON_part2.txt:12630:سواره نظام روسی. (در عهد تزارها و اواخر 
MON_part2.txt:16489:امپراتوران روسیه» تزار؛ ج. قیاصر ه. 
MON_part2.txt:20445:روسیه (دورة تزاری و شوروی). 
MON_part2.txt:23239:(امف.) [- کشته - کاشته] مزرعه» کشتزار. 
MON_part2.txt:23249:کشتزار: 40227 (امر.) زمین زراعت شده؛ 
MON_part2.txt:23250:مزرعه. کشتزار دیو: ( کذد.) عالم سفلی» دئبا. 
MON_part2.txt:35459:بر دص )سور کر (ا) کقافته تزار کین 
MON_part2.txt:38883:خیار و غیره. کشتزار. 
MON_part2.txt:39365:از سربازان (و آن در عهد سزار و دوران 
MON_part2.txt:47100:نفرت دارنده» کراهت دارنده. (ص.) سزار؛ 
MON_part2.txt:54877:مسزارع: (ع.] ج. مررعه؛ 
MON_part2.txt:65473:ممل: (۱۱۱01۱6۱)۱ [ع.] (افا.) ملال آور؛ سزار 
### BQT v1 قیصر
3248:قلقطار ؛ قلقند » قلومن » قندیس ؛ قیصر ( ذیل :اغسطوس ) .
18172:حمروف بند قیصربراو
27717:لیگ ر ۴ - بروزن قیصرقالب وکالبدوجله
28961:۵ - ء زیر قیصران وگاه تخت اردشیرآحت‌سر اج بنتح سین. بی ضله ورای
```


## [2026-09-14T01:59:27.921Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"اغسطوس\\|اغسطو\" BQT_v1_pages.txt | head -10; echo \"### page tags near\"; grep -n \"\\[pdf page\" BQT_v1_pages.txt | head -3; echo ...; python3 -c \"\nimport re\nt=open('BQT_v1_pages.txt',encoding='utf-8').read()\ni=t.find('اغسطوس')\nprint(repr(t[max(0,i-3000):i+1500]))\" | head -40"
}
```


### [2026-09-14T01:59:29.073Z] TOOL RESULT

```
3248:قلقطار ؛ قلقند » قلومن » قندیس ؛ قیصر ( ذیل :اغسطوس ) .
12905:میان مردم. باشد » وآلرا بعربی اغرا گوشد . اغسطوس؟ ۰ بنتم اول وانی‌وسکون
### page tags near
...
'بق نبطی » حمحم » درافس ۰\nدرافق » ستدیان .\n۵ - مقر بی (لّت اهل عغرب) : جدال » جرامقه» حماط » حمس\u200cالامیر\n( ذیل : خارخسث ) » حیصل \u200f دوقس \u200f زعرور » سردین (مستقلا و نیزذیل »\nسماریس » و ذیل : عرم )۰ شغنین ( ذیل : تی) ؛ قبلوط .\nو- مدثی ( لغت اهل مدینه ) : سدی .\nرد بغدادی ( لغت مردم شداد) : عصیفره .\nح-موصلی ( لغت موصل ): عصیفر ه.\nط - لفت وادی القری: سیاب.\nی- مصری ( لت اهل مصر) : فر یدیس .\nباء عمانی ( لغت اهل عمان ) : عشر » غاغه .\n۳ - بر بری ( زبان قوم بربر ) : تقده » تقره » رنف » عصاب ۰\nکر کرهن.\n۴ - حیشی - از قول بعضی < فسطاط » را حبشی داتسته ۱ .\n۴ - نبطی- در ذیل «قزاغند > گوید : گویند این لفت ابطیاست؟ .\n۵ - عیری ۴ - بمش لفات عبری در برهان وارد شده ؛ مانند: زبوو\nفرعون » قبطه .\n۲ - سریانی؟ - ازسریانی لفات بسیار- مخصوصا درادویهٌ مفرده -\nدر کتاب عورد سث آعده ؛ از ] نجمله :\nابلیا افیا نید »حردون »خالوما » ینر وه رفیدا» را\nساسار کشت » شیر طیطان » فاشر | قوسیا » لوقاین » مثك » نینیا» هلفها\nسر یانی یکی از لپجه\u200cهای مهم آرامی شرقیاسته ۰ و بسیاری از لفات\nآرامی نام هزوارش وارد زبان و کتابت پپلوی شده است که در برهان\nعنو ان« ز ند ویاز ند > از آنپا یاد شده" .\n۷ ترکی ۲ -از زبان تر کی\u200cلفغات بسیاری- مستقلا ویا درذیل لغات\nشتا نگل دیگرفاط ) ششدید دوم )» درلفت 3 از\nلانینی ۳05520010 بمعنی اردو- بیرق - نوعی چادر است. « دزی ۲ ص ۲4 \u200c\n۲- ممرب « کر ] گند» است- ره :کزا کند وفزاغند.\n۳ا 2 عی رف 4 - و38 : حربافی. ۵- ره :آرامی و\n+ - رك : زند و بازند در همین مقدمه\u200cص\u200cدوازده. ۷ - رگ :ت رکی.\x0cدیگر - در برهان قل شده ازین قبیل است :\nاتا » اتايك » انسیز » بلدرچین ( ذیل : سمانه » وذیل: 7 ۰ بلان\n( ذیل : سعد )۰ تمر » چسارو ( ذیل : شم ))» سکز » سن » سو » سيك »\nصفرجق( ذیل: سوبدی )» طوغان ( ذیل: شاهباز )» قنجوقه (ذیل: سیموت)؛\n۳\n( ذیل : سست ۱\n۸4 - هن.ی موّلف برهان از زبانپای هندی ذیل » لغاتی آورده\nاست :\nالف - ز بان علمیاهل\u200cهند (سانسکریت؟ ):آچار» ار گ» تمر» جکره\nچاز چا یوم نام زود) یی شوه\nب - هندی (مراد زبان معمول در هندوستان\u200cاست؟ ): بان (ذیل: تیر\nچرخ ) » بکاول (ذیل : چآشنی گیر)» توره » جاء جنتر» جوجن » جوله» چال»\nچکری \u200f چل:ساس .کتار (ذیل:جمدره وذیل : جنبیه )» کتاره » کتمل ( ذیل :\nساس ) کتکری (درارد ۲۷ ) ( ذیل: کلو نده)\nج - دکنی ( لفت مردم دکن ۴ ) : دانك » روشنك » مکن ( ذیل :\nساس ). ۱\n4- یو نانی * - ازیونانی لفات بنیارمخصوصا در ادويةٌ مفرده تقل\nشده است مانند :\n۱ ايی یپمیا \u200f اخبون » ارسطو لوجیا ( ذیل : ارسطو ) » اسطر لاپ » .\nاسطر تو تاه اسقلینوس» اسطقس» اسطوخودوس » اغلیقی» غسیا» سالامندر|؛\nسخینوص , طوفر یوس . طولیدون ؛ فر یموس ؛ فیلاسوف" .\nو گاه لفات یونانی را بدون تصریح بیونانی بودن یاد کند مانند :\nاییون » ارغتون » اقلیمیا وغیره . ۱\n۰ رومی (لانینی ۷)- ازلفات رومی نيزشمارة بسیار- مخصوصا\nدر ادویه مفرده - فل شده وعالب [ نهاماً خذ یونانی دارد» از [نجمله است:\n۱ موّلف کلمةه چاو» را که چینی\u200cامت نام«جفتای» باد کرده است. \u200f ۷- راد: ص\u200cشش\nمقنحه. ۴ و آن همان زبانست که امروزه اردو» نامیده مبشود. رك : دائرةالمعارف\nلام : اردو- 4- محل اقامت مولف برهان قلیلم . ه - رك : پونانی .\n-٩\u200f بدیهی\u200cاست بیاری ازین لغات صحيف\u200cشده. را#:لفات مزبور درمتن برهان وحواشی آن.\n۷- ره : لایتی .\x0cمد ويك زبانیا و لپجه\u200cها در برهان قاطع\nسلیقون ( مستقلا و ذیل : زرقون ) » طالیقون » طفشیقون .قطاس ؛ ققنس »\nقلقطار ؛ قلقند » قلومن » قندیس ؛ قیصر ( ذیل :اغسطوس ) .\n۱ - ارمنی ۱-از زبان ارمنی لفت «ژ کال» رایادکرده است؟ .\n۳ . ز ندو پاز ند میدانیم که ز ند تفسیر اوستاست وباز ند نام ز بان\nیپلوی بر استه از لغات دخیل [رامی است ۴ ؛ ولی ز ند و باز ند در اصطلاح\nمولف برهان چند مقهوم یافته است :\nالف - لفات بپلویرابدین نام میخو اند ؛ مثلا : ابر ناك » اسو بار» انداچه »\nاپر ناك» اسوبار ۰ انداچه ؛ اردر. اودردن ( وترتن ۴ ) » پاتپر اس » پیتام »\nتبراست » جوبال » جووان » جه » چیجست » راس \u200f راك ۰ کمخت » کوپ ؛\nکتجویر( گنجو بر)» گیها ( گیاه) » ماژدیستان (مازدیسنان)» منش (منشن)ه\nنسا » نکاس » واژه » وجارش ( وچارشن ٩\u200f ) » ور» وهمنش ( وه منشن ) »\nهاوشت » هاون ؛ همیز( هامین )» هثام ( هنتام.)؛ هو سرب یشتن ( مستقلا\nونیز ذیل : درون ).\nبت لفات دینی زر نشتی : اشوه بادیاو» بنام » چینوده درو ند زردشت\nبزرگ » زروان بزرگ » شید » يشتن » (متقلا وذیل : درون ) .\n"اج - لفاتی از لپجه های ایرانی: بزونه» زوزنی» زونی» ژند» هلیجو؛ هليك\nذ - گاه\u200cلغات مجمول .فرقة آذر کیوان را بنام « زند و پاز ند »یار کند: هر فیز.\nهر نین\u200cمند(در؛ هر نیز)\nد غالبا مر اد اززند ویاز ند در برهان همان لغات هزوارش ۱ است .\nنغستین بار موّلف فرهنگ جپانگیری بر آن شد که اغات هزوارش\nولقات دینی زرتشی را گرد آورد . وی درذیل لغت < آذر> گوید: <فقرحقر\nکه راقم این حروفم؛ بیری از بارسیان را که بر دین زردشت بوده دیدم که\nجزوی چنداز کتاب ز ند ووستاداشت ؛چون مرا رغبت وشعف\u200cتمام بجمم لغات\nفرس بود » و در فرس از زند و وستامعتبر تر نیست ۰ بجپت تحقیق لفات\nبا او صحبت میداشتم وا کثر لفاتی که درخانمةٌ کتاب از زند و بازند ووستا\nنقل شده از تقر یر آن زردشتی است .>\n۱ ره : ارمتی . ۲ - در ارمنی 208101 بمعنی زغال اخته ( میوهٌ ترش مزه)'
```


## [2026-09-14T01:59:34.221Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -c $'\\f' BQT_v1_pages.txt; grep -o \"\\[pdf page [0-9]*\\]\" BQT_v1_pages.txt | head -3; echo \"---\"; sed -n '12895,12925p' BQT_v1_pages.txt"
}
```


### [2026-09-14T01:59:35.279Z] TOOL RESULT

```
766
---
اغارد « بفتح اول و رای‌فرشت‌بروزن
وحرب کند - بخیساند و سرشته کند و درهم
آمیزد . ۱
اغار س با زای هوز بروزن نماز, بمعنی
قصد واراده بشد - و بمعتی صدا وندا - وابتدای
ه رکار نیز آمده است .
اغاز ه- بر وزن هلازه » افزارست
اغالش بکسر لام بر وزن تراوش »
بمعنی آ غالش‌است که شورش از بختن‌وبد[ موزی اغر بوس - بفتح اول وضم‌واو وسکون
و تحرض کردن نادانان بجهت خصومت انداختن | سین بی‌قطه » یونانی صحرا! ویابالرا گوشد .
میان مردم. باشد » وآلرا بعربی اغرا گوشد . اغسطوس؟ ۰ بنتم اول وانی‌وسکون
اغر سس » بنتح اول وثالی مسکون | سین بی نقطه و طای حطی بواو رسیده و بسین
را وقتح سین می نفطه و کسر طای حطی ودسن سعقص زده » نام یادشاه اول است از بادشاهان
( رد : آغلردن  .‏ ؟ - بیونانی42070595 , درانگلیی 287065 «انتینگاس».
۴ - بیوتاتی 56712 , 49 « اشتینگلی > . ۴ - در اوستا قطاعهحطو۸
لة پمستی < کسکه کردونهاش در پیش میرود . > < یشت ٩‏ : ۲۱۱ * . ۵ - لانینی
کنناکناع ۸ (عالی ۰ عظیم , مقدی » . لقب اکتاوبالوی و هم امپراتوران بعدی « مرچنت * .
ز برهان فاطع ۲۳)فیاصر# روم ؛ او را ازآن جپت قصر گفتندکه
مادرش بوفت ولادت عمرد 7 شکمش را بشکافتند
و او را برآوردند و پزبان رومی اینچنین شخصی
را قیسرخوانند٩‏ . و گویند عیسی علیه‌السلام در
زمان او بوجود آمد . وبقوط سین اول بروزن
فربوی هم بنظر امده است -
اغشته با اول وئانی مفتوح و سکون
شین فرشت وفتح فوقانی ‏ بمعنیآمیخته وآلوده
وتر کرده باشد؟ .
لام ؛ جایی‌باشد که در کوه وسحرا بجهت‌خوابیدن
کومفندان ساژند؟ .
اغلیسون » با سن بی قطه بر وزن
افربدون ۰ قوس قرح را خوانند .
افتدستا
```


## [2026-09-14T01:59:51.154Z] TOOL CALL #26: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nprint(json.dumps(d['BQT'],ensure_ascii=False,indent=1))\nprint(json.dumps(d.get('ISS'),ensure_ascii=False,indent=1))\nprint(json.dumps(d.get('NAT'),ensure_ascii=False,indent=1))\nprint(json.dumps(d.get('FSD'),ensure_ascii=False,indent=1))\n\""
}
```


### [2026-09-14T01:59:52.581Z] TOOL RESULT

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
{
 "title": "H. W. Bailey, Indo-Scythian Studies: Khotanese Texts VI (Prolexis to the Book of Zambasta), Cambridge 1967",
 "edition_found": "not found; Bailey's Dictionary of Khotan Saka (1979) downloaded as the closest substitute",
 "kind": "google_books_preview+archive_restricted",
 "url": "https://books.google.com/books?id=4upthUgWo9YC (CUP 2009 reprint, partial preview) ; HathiTrust mdp.39015034317936 (v.6, search-only) ; archive.org khotanesetexts0103bail (vols I-III only, lending)",
 "identifier": "dictionary-of-khotan-saka (substitute); khotanesetexts0103bail is vols I-III, lending-only",
 "local_file": null,
 "page_offset": "DKS: leaf = printed + 17..19 (e.g. leaf 158 = p.139). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Khotanese Texts VI itself is not online. Nourai's ISS page numbers cannot be checked directly; the Dictionary of Khotan Saka (headword at line start, Khotanese in transliteration, with 'Pok.' refs) covers the same etymological material and can verify the substance of a claim.",
 "notes": "Tried IA ('indo-scythian', 'zambasta', 'khotanese texts'), Google Books API. || RE-SEARCH 2026-09: preview only (Google Books partial view of the 2009 reprint — usable for spot checks); no open full text. A dokumen.pub upload exists (not used)."
}
{
 "title": "C. Berlitz, Native Tongues, New York 1982",
 "edition_found": "2005 Castle Books reprint (open); 1982 original lending-only (nativetongues00berl)",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/native-tongues-charles-berlitz-book-sales-ca-1997-3-printing-2005-castle-books-9",
 "identifier": "native-tongues-charles-berlitz-book-sales-ca-1997-3-printing-2005-castle-books-9",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NAT_2005.txt",
 "page_offset": "2005 reprint: leaf = printed + 15 (e.g. leaf 17 = p.2); reprint pagination may differ slightly from 1982. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Popular book, prose chapters; grep the word.",
 "notes": ""
}
{
 "title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)",
 "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/in.ernet.dli.2015.147439",
 "identifier": "in.ernet.dli.2015.147439 (vol I A-Dive), in.ernet.dli.2015.272042 (vol II), in.ernet.dli.2015.83695 (vol III), in.ernet.dli.2015.147440 (vol IV Sabi-Z)",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt",
 "page_offset": "vol1: leaf = p + 41..56 (drifts; e.g. leaf 87 = p.46, leaf 612 = p.556); vol3: leaf = p - 1466 (e.g. leaf 215 = p.1681); vol4: leaf = p - 2144..2148 (e.g. leaf 229 = p.2373); vol2 offset not reliably detected (pages ~ 700-1640) - grep the headword. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Headword in bold at line start with pronunciation; etymology in brackets at entry end '[< L. ...]'. Very large OCR (16 MB per vol); grep -n '^word' vol file.",
 "notes": "Nourai cites 1940; page numbers in the New Standard were stable 1913-1940s (single-volume pagination 1-2814 continues across the DLI volumes). local_files: /home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt, /home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol2.txt, /home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol3.txt, /home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol4.txt",
 "local_files": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol2.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol3.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol4.txt"
 ],
 "cites": "page number of Funk & Wagnalls New Standard Dictionary (1940)"
}
```


## [2026-09-14T02:00:07.277Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('incoming/BQT/BQT_v3_pages.txt',encoding='utf-8').read()\nfor p in (345,346,347):\n    m=re.search(r'\\[pdf page %d\\]'%p,t)\n    print('=== pdf',p,'printed',p+1205,'found',bool(m))\n    if m:\n        print(t[m.start():m.start()+1800])\nEOF"
}
```


### [2026-09-14T02:00:08.438Z] TOOL RESULT

```
=== pdf 345 printed 1550 found True
[pdf page 345]
باقلای شامی, ‎Sly‏ مسصری باشد .

قیطی ۱ = بفتح اول ر کسرطای‌حطی
‎us Oy‏ « بولانی نام درختی است کهآنرا
بفارسی مورد وبعربی آس گوبند ۴ .

‎OGY‏ = بررزن میمون . تلم مردی
بوده - و پمعتی کنجینه هم آمده است.

‏قیقهن ۳ ‎che‏ اول وسکول‌ثانی‌وقاف
مفتوح وهای مکور و نون ساکن ؛بمعنی‌قنقهر
است که صمفی ‎ath‏ ناخوش طعم؛ وبعضی گوبند
ستدروی است -

‎Je‏ © بروزن فیل » نام بیابانی و دشتی
است - وزفت تر را یز گویند وآنرا از درخت
صنوبر ‎tS‏

‎dal ‏بر وزن .مردمی » بلقت‎ gd
‏بفارسی چويك اشنان‎ YT ‏است که‎ aw ‏مشرق‎

‎. aly

‏قیلموس ‎be‏ میم بر وزن سندروس ۰
بمعنی هوشیاری باشد .

‎BHD‏ بر وزن مربوط , بلنت احل*

‏(۱) خم۱: -کشیده .

‏مفرب ‎gle‏ است رآن ‎Sy‏ کندنای‌شامی باشد

‏(۷) چش : صفهای .

‏-۲ووا

‏که لوعی ا زکندنا است .

‏قیل و ‎JU‏ کردن - کنابه ازسث
ومباحثه ‎SSIS,‏ باشد .

‎)۱( ‏لیا = با اون بتحانی کشیده‎ ged
‏رسنده وکرلام وتحتانی بالف کشیدهء‎ gly ‏و میم‎
‏بعربی حجرالرخام گوبند‎ TD ‏نوعی‌از کل است‎
‏و آن‌مانندصفحه‌های(۲) رخام بودرسفیدوخوشبوی‎
ath ‏وازآن بوی‌کافور میآید. چون نازه‎ atlas
. ‏آنرا حجرالشفاف (۳) نیز گویند‎

‎rhs‏ بکر اول بروزن میناه نوعی‌از
بقلة‌الحمقا است که بفارسی خرفه گویند.

‏ای ‎OM‏ - بروزن ربوند » بمعنی‌قارند
است که ‎ay‏ قاوندی باشدوآن روغنی باشدمنجمد
که ازدانه گیرند ‎wl‏ فندق. درد پشت ‎Bey‏
‏کهنه راکه ماد آن ازسردی باشددافم است؛
و تخم فیوندی که در کب طبی نوشته‌اند همان

‏(۳) خم ۱ : الشقان-.

‏۱ ح قیطوی ‎Uy jt‏ ۴08 ( وال ؛ بال ) ‎het ress?‏ - نام صوزتی از صور

‎. ‏منطقة البروج‎ (p>

‎۲۰۳ ut) Myrtus communis L. = ۴

‎oe ۴‏ فیقهر , صمفیست.شبیه بندروس و بدبوی وبدطعم و بهندی رال و بفارسی لعل

‏معبری و بعرپی شجره نامند وتمیمی گوید اسم عبرای سندروی است . » « ‎in‏ حکیم مومن».
۴ _ امل‌القینا ‎ib yon. China , 6500106 . squine=‏ درهندوستان «دزی چ

‏۲ص ۳1 ‎OG‏ ۵ رك : قاوند .
[pdf page 346]
از کتاب ‎abl obey‏ درحرف گاف تازی با حروف بجی
مبتنی بر ببست وسه ‎Oly‏ ومحتوی بر یک
=== pdf 346 printed 1551 found True
[pdf page 346]
از کتاب ‎abl obey‏ درحرف گاف تازی با حروف بجی
مبتنی بر ببست وسه ‎Oly‏ ومحتوی بر یکیزار وششصد و پنجاه
و چبار ‎od‏ و کنایت

Jat ‏بیان‎

در کاف تازی با الف مشتمل بردو ‎Cm‏ وسی وهشت ‎cal‏ و کنات

‎x‏ کايك ۱ ‎eee‏ بای ‎aml‏ بر وزن ‎OT‏ تخم کندوبچه‌بر آرد - و رفیده رانیز گفته‌اند
چابك . آشبان مرغانرا گوبند عموماً و آنشیان | وآن لته‌ای چند باشدکه بر روی هم دوزندمانند
کیوتر و مرغ(۱) ‎Seay Ge‏ که‌درخانه | گرد بالشی وخمیر نانرا تنك ساخته بر روی‌آن
آشیان داشته باشد خصوصاً ؟ - وزتبیل مانتدی | کترانند وبرتتور چسبانشد ۳ .
را نی زگوید که در خانها آویزند تا کبوتر در کابل ۴ ین ‎cht‏ و سکون لام » نام

‎de )۱(‏ چش : - و مرغ .

‏# ک - حرف بیست وپنجم از الفبای فارسی وحرف بیست ودوم ازالفبای‌عریی ( ابتث )
وحرف بازدهم از ابجد ... وآنرا کافی تلفظ کنند و درحساب جمل بیست گیرند » و برای‌تشخیص
از « کب » ‎GE LT‏ تازی وکاف عربی گوبند. این حرف به «خ» ( ديباچة مولف ص : بح ۰ بط)
و به «غ» ‎tal)‏ ص بط ) بدل شود . برای ‎lee‏ آن , ‎dy‏ : ص‌کو » له ( از ‎Bp Sele‏ )
و رك :کافنامه بقلم کسروی باهتمام بحيی ذکاء . تهرآن۱۳۳۹-

‏۱ - مخفف > کابوکث © (هم) .

‎tab GT ۴‏ در ‎SEZ pT‏ روحانیان ازبروج رفرف افلاك ‎LE‏ ميکند.

‎.> ‏نظام‎ King Sl ‏سیف‎

‏۴ رگ : کابوك (معنی دوم) + ۴ - شپر مهم و ‎Ceol‏ افنانتان در ۴ درجه
و ۳۶ ‎lids‏ عرض شمالی و ‎۹٩‏ درجه و ‎BY‏ طول شرفی ۰ در۱۷۹۲ متری فوق سطح دربا .
واقم درنجدی حاصلخیز وپرآب. جمعیت آن درحدود ۱۵۰۰۰0است . ورك : ‎afb‏ المعارف‌اسلام .
[pdf page 347]
کابلج
شپری است مشهور درمیان ‎oS‏ مابین ماوراءالنهر
و هندوستان و بعضی کوبند ما ‎oy‏ خراسان
رهندوستان ؛ ‎Ys ply‏ هم‌هست. گویند که در
‎AY, oT‏ جراحان خوب میباشند - و نام نوعی
از ساز ناشدکه نوازند.

‎CHT‏ - بسکون ‎at‏ و کنرلام وجیم
‎OTL‏ انگشت کوچك دست وپا باشد و بعربی
‎Van Ss‏ .

‏کابلیج ‎pe‏ وژن مارپیچ» بمعنی کابلچ
است که انگشت کوچك دست و یا باشد؟ .

‏کالفه ۴ » ‎MLS‏ وفتح تون,بمعنی
چشم باشد چنانکه هر گاه گوبند « کابنه‌پدود
=== pdf 347 printed 1552 found True
[pdf page 347]
کابلج
شپری است مشهور درمیان ‎oS‏ مابین ماوراءالنهر
و هندوستان و بعضی کوبند ما ‎oy‏ خراسان
رهندوستان ؛ ‎Ys ply‏ هم‌هست. گویند که در
‎AY, oT‏ جراحان خوب میباشند - و نام نوعی
از ساز ناشدکه نوازند.

‎CHT‏ - بسکون ‎at‏ و کنرلام وجیم
‎OTL‏ انگشت کوچك دست وپا باشد و بعربی
‎Van Ss‏ .

‏کابلیج ‎pe‏ وژن مارپیچ» بمعنی کابلچ
است که انگشت کوچك دست و یا باشد؟ .

‏کالفه ۴ » ‎MLS‏ وفتح تون,بمعنی
چشم باشد چنانکه هر گاه گوبند « کابنه‌پدودار»
مرادآن باشد که چشم ازو برمگردان و از نظر
مینداز .

‎Shy ET oly ‏با اك‎ « FIT
‏مرنانو کبوتران‎ BUST ‏زده» بمعنیکاك‌است که‎
‏که کبوتران‎ Gals ‏و زنبیل‎ - ath Ge

‏۱ - ره : کابلیج .

‎~Noot—

‏و فاختگان در ‎OT‏ تخم گذارند ۵ - و آلت ‎ob‏
‏بر تئور چسبانیدن را نیز گفته اند که رفیده
باشد ۲ .

‎Od‏ ۷ ۰ بر وزن و معنی کاویدن
است که کندن و خراشیدن باشد - و بمعنی
شکافتن هم گفته‌اند ۱

‏کابیشه - با الك بتحتانی رسیده و فتح
شین ‎Noakes‏ گل‌کاجیره را گوبند ‎ily‏ آن‌چیزها
رنگگ کنند وبس‌بی تصفر خوانند .

‎WE‏ - پنتح لام . هرچیز که در آن
‎ale‏ بکوبند عموماً- ودارو کوب عطارانر! کوند
که هاون سنگی باشد خصوصاً و بعرمی ‎oe‏
‏خوانند ۸

‏کابین ‎pe ٩‏ ون لاچن . مهر
کویند ‎Ny‏ باشد که در هنگام عقد,
ونکاح کردن زنان مقر رکنند ‎NM‏

‏کات = با سکون فوفانی » نام‌شهری‌است

‏۴ - اسل ‎oT‏ « کابلیج » انگشت کهین پای را گویند . »

‎. ‏مروزی شاهد آورده که عفپوم تست‎ Game ‏اسدی بیتی از‎ VE ‏و‎ ٩6 ‏فرس ص‎ cal?

‏۴ - کردی ع 68006 (منظره) ‎Ue‏ س ۳۷۱ ۰ .
6۵ -« 6ابوك , جای مرغ خانگی بود وبود که چیزی نیز مانند زنبیل در ‎Oke‏

‎(ed)

‏۴ مخنف ‎oT‏ «ايك»

‏خانه بیاویزند نا کیوتر بچه درآن کند . بوشکور(بلخی) گوبد :

‏چون بچهٌ کبوتر منقار سخت کرد

‏هموارکرد موی و بو کند موی زرد

‏کابوك را نشاید(نپاید؟نخواهدادهخدا) وشاخآرز و ‎AS‏
‏وز شاخ سوی بام شود باز گرد گرد. * "لفت ‎VED‏

‏1 - باين ممتی ظ. مسحف ‎Com) © Ty lS?‏ ورك : کابك.

‏۷ کاویدن (هم) ۰

‎: ‏«کابیله. هاون بود . طیان مرغزی گوید‎ - A
```


## [2026-09-14T02:00:09.490Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### FSD vol2 jersey\"; grep -n \"Jersey\" FSD_vol2.txt | head -10; echo \"### FSD vol3\"; grep -n \"^jersey\\|Jersey,\" FSD_vol3.txt | head -5; echo \"### NAT\"; grep -n -i \"jersey\\|Caesarea\" NAT_2005.txt | head -10"
}
```


### [2026-09-14T02:00:09.588Z] TOOL RESULT

```
### FSD vol2 jersey
12410:Es'ses2,rt.  1.  Earl  of  (R/i«1567-Vs5l601),  Robert  Hevereux, an  English  soldier  and  courtier,  the  favorite  of  Elizabeth;  be- headed for  treason.  2.  Earl  of  (i/-1592-Vul610),  Robert Devereux,  an  Engll,sh  general,  son  of  preceding;  served the  Royalists,  was  deprived  of  commifision,  joined  Crom- well, and  defeated  Charles  I.  at  EdgehiU  and  Newbury. 3.  Earl  of  (1.541-V  551.576),  Walter  Devereux,  an  En- glish general  and  statesman  who  ordered  the  maasacre  at Rathiin.  4.  A   county  In  the  southeast  of  England:  1,,542 BQ.  m.;  county-town,  Chelmslord.  5.  A   county  in  north- eastern Massachusetts,  514  sq.  m.;  county-seats,  Salem, Newburyport,  Lawrence.  6.  A   county  In  northeastern New  Jersey:  127 sq.  m.;  county-seat,  New'ark,  7.  Acounty in  northeastern  New  York,  1,834  sq,  m.;  county-seat, Elizabethtown.  8.  A   county  in  eastern  Virginia,  277  sq. m.;  county-seat,  Tappahannock.  9.  A   county  In  north- eastern Vermont:  682  sq.  m.;  county-seat,  Guildhall.  10. A   town  In  Middlesex  county,  Conn.  11.  A   town  In  Chit- tenden county,  Vt.  13.  A   town  In  Essex  county,  Maas. 13.  A   district  In  Ontario,  Canada;  capital,  Sandwich. Es'sex  Cea'ter.  A   village  In  Ontario.
20581:Flo-no'la,  1   fi-no'lo;  2   fi-n6'ia,  re.  Same  as  Fionnuala. fiord,  1   fyerd;  2   fyfird,  n.  A   long  and  narrow  arm  of  the sea,  having  usually  high  rocky  banks.  [<  Norw.  jO'ord.] fi'o-riii,  1   Inl'o-rln;  2   fl'o-rin,  re.  The  white  bent-grass (A;iro.Mfs  afSal,  a   valuable  meadow-grass,  naturalized  from Europe.  l<Tr..;?orri!are,acoarsegr.ass.l fi'c-rlte,  1   fol'o-rait;  2   il'o-rlt  (xiii).re.  Mineral.  A   globular, botryoidal,  stalaciitio,  pearly  concretion  oi  opal  formed from,  the  decomposition  of  sllieious  minerals  of  volcanic rocks.  [   <   Santa  Ffore,  Tuscany.]  li'o-ry  tet. flo"ri-t«'ra,  l   fyo'n-tu'ro;  2   ij?6''rl-t.u'ra,  re.  [-he,  Z   -rB:  2   -rg, pi.)  [It.]  In  music,  the  embellishment  of  a   melody,  as  by  a trill  or  turn;  used  mostly  in  the  plural. flp,  K.  [Local,  U.  S.]  Aflppennybit. , flp'pence,  1   fip'ous;  2   fiii'eac,  re.  Fivepcnce.— flp'pen-ny, a.  ShortforFivEEENNY.—  flppennybltjiivcpenee; aSpanlsh or  Mexican  silver  piece  ivorth  G'/  i   cunts,  current  in  the United  States  before  tlie  Civil  War;  formerly  so  called  in Pennsylvania,  New  Jersey,  and  some  Southern  states: withdrawn  from  circulation  in  18.57.  Compare  also  four- fence:  halfpenny;  picayune;  sixpence. fip'ple,  1   fip'l;  2   flp'l,  re.  1.  [Scot.]  The  lower  lip.  3t.  A stopper.  [Society.
21615:Ftan''drln';  1   flofl'dnifi':  2   fiafi'drafi',  Joan  Hlppolytc  etc.- elastic  f.,  a   napped  Jersey  cloth.- f.  cake  [U.  S.].
21843:rov.  Eng.J  A   low  washtub  specif.,  in  the  United  States,  a   ]cnv«j5-ing  plain  near  t   idc- water  or  a   river;  an  intervale;  commonly  in  the  plural; er.  A   voider  that  encroaches  as,  the  Jersey  j?a/s.
25645:New  Jersey.]  .   „   See  WALL(JO^
32608:bluish  cuvstallinc  .silicate  of  manganese  and  calcium  found at  i-’ranklln  Furnace,  Jiew  Jersey.— glau'co-dot,  a.  Alin- eral.  A   grayish  tiii'White  cnhaltdron  sulfarsenid,  (Co.Fr!) AsS,  cry.staillzlhg  in  the  orthorhombic  system.—  gIau"co- dym'f-uin,  n.  chm.  A   supijoaed  element  In  salts  of dldymiura.— glau"co-g<i-iiid'l-um,  n.  Hot,  Same  as ooxiHinir,— glau'co-litc, !!.  Mimral.  A   variety  of  wer- nei'itc  having  a   him;  or  green  tint.  Compare  wr.i'tifEKrrE. Other  ■words  beginning  with  this  pr.'fix  will  be  tevuid  In I   ei-  alphabetical  place,  eitiicr  singly  or  in  groups.
33032:1397),  High  Constable  ot  England;  plotted  against  Ills  neph- ew, Richard  11.;  .arrested  and  murdered.  4,  A   county  in the  west  of  Enghind;  1.237  arp  m.  Ulouces'ter-.shire;.  .7» Its  capital,  a   port  of  entry;  has  a   large  cathedral.  Glos'tert. 6.  A:  district,  New  Brunswieli  province,  Canada:  1,860  sq. nx.;  capital.Bathurst,  7.  A   county  in  New  Jersey;  32fi  sq.m.; county»se£xt,  'Woodbury,  8.  A   county  In  S.  E,  Virginia; CQunty»aeat,  Gloucester.  9.  A   aeaport,  city,  and  llshlng* station  in  Essex  county  Mass.  10.  A   mxinufacturing  city in  Camden  county,  N.  J.  11.  ffer.  See  Hbrauds’  Coiaege. n..  under  Hebald.  13.  A   cheese.  See  under  cheese. gioah,  1   gltUc;  2   ShiS.  inierj.  [Scot.]  The  call  of  a   crow, giouk'lng,  1   eluk'iij;  2   gJuk'ing,  a.  [Eng.]  Sour  of  temper; sulky.
34429:gos'let,  1   gezTet;  2   gds'lCt,  «.  A   small  gnose  (genus  Nettopns), not  larger  than  a   tea!,  of  South  Africa,  India,  and  Australia. gOS'Ung,  1   gez'Iirj;  2   tS.s'ling,  n.  1.  A   young  goose, go-s'lln,  3,  A   foolish  young  per.'son.  3.  A   bloom  on a   tree.  [Dim.  <   goose.]  —   gos'lIng«green",  n.  .A  yel- lowish-green color,  gos'line-col'-'orf. gos'more*,  I   gas'raSr;  2   gos'mer,  n.  .A  eloliorlaceous  peren- nial weed  (Hypochxris  radteata),  advent! ve  from  Europe and  found  In  New  Jersey  and  California.  It  has  hirsute leaves,  spreading  on  tho  ground,  and  large  beads  of  yellow flowers;  troublesome  in  cultivated  flelds.  [Op.  goss.amee,J gos'inore*,  n.  Same  as  c.vt'h-eak,  1. gos'nick,  1   gos'nifc;  2   fds'nlk,  n.  [Scot.]  A   fish,  the  saury, gos'pel,  1   g6.s'pel;  2   gfis'pBI,  rf.  [gos'pbled  or  -felled, -fhlds;  gos'pel-ing  or  -fei.-ling.]  To  teach  the  gos- pel to;  fill  with  piety.  [<  -AS.  godspeUian,  <   god, God,  -[■  spd,  stoo'.l
39575:IIack'en-.sack,  1   hak'en-sak;  2   hiik'en-sak,  n.  1.  A   river  in  commonplace  by  frequent  use:  threadbare,  hack'nledf. New  Jersey;  length,  50  m.  to  Newark  Bay.  3.  A   town;  hack'ney-ism,  1   hak'm-lzm;  2   hak'ny-Igm,  n.  The  spirit county»seat  of  Bergen  county,  N.  J.  engendered  by  dull,  commonplace  repetition,
40667:Maa'cock,  Mount.  1.  A   peal;  in  the  National  Park,  Wy- oming; height,  10,235  It.  3.  A   mountain  in  Grafton county,  N.  H.;  height.  4,430  ft. han'cock-Ite,  l   han'kek-ilt;  2   hln'eok-It,  a.  Minernl.  A member  of  the  cpWote  group  containing  lead  and  strontium: found  in  New  Jersey.  [   <   E,  P.  Hancock.,  of  Burlington.  N.  J.J Han'coclt  i’as.s.  A   pass  In  Colorado:  elevation,  12.203  ft. hand,  i   hand;  2Mnd,i!.  I.  f.  1.  To  give,  pass,  deliver, or  transmit  with  or  as  with  the  hand;  as,  to  hand  one a   plate.  3.  To  assist,  lead,  or  raise  with  the  hand;  as, to  a   blind  man  across  a   street.  3.  Naut.  To  furl, as  a   sail.  4.  [Archaic.]  To  handle.
### FSD vol3
53639:New Jersey, 475 iq ro ; county-seat. Morristown It.
122050:*/(il888). an American Judge, Cioveriior of New Jersey,
124997:an admission ticket to leave and return to a place of entor> Jersey, length. 100 m to Newark Day. at Palt*rson it drops
124999:of mouth from the head to the rear of an army — p. (penny* a. Jersey, 108 sq m, county<4ieat, ratersun 3. A city In
125054:Jersey, length. m tt^ewurl^Day. at Paterson It drops Pna'ser-es* 1 pns'nr-l/., 2 iiAs'er-f'^, n pi Ormth An
### NAT
1217:New Jersey, the island of Jersey, Jersey cattle, and the type of sweater called a jersey all perpetuate the last name of Julius Caesar. The Latin name of several Roman cities, from which Jersey is derived, was Caesarea, named in honor of the first Caesar.
```


## [2026-09-14T02:00:21.678Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"قیصر\" incoming/BQT/BQT_v3_pages.txt | head -20; echo \"### v3 tsar/سزار\"; grep -n \"تزار\\|سزار\" incoming/BQT/BQT_v3_pages.txt incoming/BQT/BQT_v4_pages.txt | head -10"
}
```


### [2026-09-14T02:00:21.758Z] TOOL RESULT

```
10223:هشتم ‎op‏ روابت کرده است. کدرلوس کوید هرفل قیصر پي از ‎biel‏ خرویرویز در سال ‎٩۷4‏
25024:‏قیصر با صاد بی نقطه بروزن حیدر,
25063:‎< ) ‏(فر‎ césar=( ya, ( 6060676 ‏از‎ Caesar ‏اسلام: قیصر» . لاینی‎ Sluis th «
25068:‏4 - ق.م. ) ‎oy‏ پس از وی امپراتوران روم از خاندان وی را بلقب قیصر خواندندو بعدها همه
25070:‏امپراتوران روم را قیصر نامیدند .
25075:‎. ‏اندرون بیمن و قیصران‎ GS
38255:ذ کر میشود : کوروش » اسکندر وقیصر (ژول‌سزار) . اشتهار اودرمیان‌ملل
49261:‏گیاه قیصر ‎So‏ و فتح قاف »
### v3 tsar/سزار
incoming/BQT/BQT_v4_pages.txt:8390:تزاری قهستانی. ۸« رشیدی » « جهانگیری».
incoming/BQT/BQT_v4_pages.txt:13585:کل ی که بدان دیوار پرآرند . تزاری ( قهستانی گوید :
incoming/BQT/BQT_v4_pages.txt:15326:تزاری قهستانی « جهانگیری » « رشیدی >.
incoming/BQT/BQT_v4_pages.txt:15329:تزاری فهستانی از زبان زبی « فرهنگه نظام >.
incoming/BQT/BQT_v3_pages.txt:14715:دف وچنکک ورباب وزنبوه غچك ونای وبربط وتنبور ۰ تزاری‌قهتانی«فرهنگه‌نظام».
incoming/BQT/BQT_v3_pages.txt:25510:تزاری قپتالی « رشیدی © .
incoming/BQT/BQT_v3_pages.txt:29115:‏تزاری قهستالی « جهانگیری > .
incoming/BQT/BQT_v3_pages.txt:30117:‏تزاری قهستانی « فرهنگه نظام » « رشیدی *.
incoming/BQT/BQT_v3_pages.txt:35759:‏تزاری ‎Jeg‏ « رشیدی ©
incoming/BQT/BQT_v3_pages.txt:36885:تزاری ‎YES‏ « فرهتکه ‎ls‏ .
```


## [2026-09-14T02:00:23.041Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('NAT_2005.txt',encoding='utf-8').read()\nleaves=t.split('\\f')\nfor i,l in enumerate(leaves):\n    if 'island of Jersey' in l:\n        print('leaf',i,'-> printed approx',i-15)\n        print(l[:1200])\nEOF"
}
```


### [2026-09-14T02:00:24.166Z] TOOL RESULT

```
leaf 186 -> printed approx 171
’ang people’s town.”
A Canadian province, Manitoba, is named for the Great Spirit of the Algonkians, Manitou—in other words, God.
American Indian place names include:
Chicago “The Place of the Skunk Cabbage”’ Manhattan “The Place of the Great
Drunkenness”’ or ‘‘The Place Where We All Got Drunk’’
Mississippi “Very Big River” Missouri “Canoe River Oklahoma “The Red Man’”’ Omaha “Upstream People”
Wyoming “Upon a Great Plain”
166 NATIVE TONGUES
The Grand Teton mountains in Wyoming looked to their French discoverers like great nipples (grands tetons).
New Jersey, the island of Jersey, Jersey cattle, and the type of sweater called a jersey all perpetuate the last name of Julius Caesar. The Latin name of several Roman cities, from which Jersey is derived, was Caesarea, named in honor of the first Caesar.
Many southern and western state and city names in the United States are of Spanish origin with meanings which are unknown to some inhabitants.
NAME MEANING PREETI iis sisccceneceroreesees “Yellow”
PRBVBO TOs: ccsiscdasaens cases “Arid Zone”’ B@GO RAVON .isi......ccccsviseees ‘““Mouse Mouth”’ colo: —— ae “Red”’
3) | oe “The Pass”’
PG MAB a cisiiriccssisesicarcgneees “Flowery” NMOMTAIG fo .
```


## [2026-09-14T02:00:32.396Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('incoming/BQT/BQT_v3_pages.txt',encoding='utf-8').read()\nlines=t.split('\\n')\nseg='\\n'.join(lines[25015:25085])\nprint(seg)\n# find pdf page tag before line 25024\nidx=t.find(lines[25024])\ntags=[m for m in re.finditer(r'\\[pdf page (\\d+)\\]',t)]\nprev=[m for m in tags if m.start()<idx][-1]\nprint('=== pdf page', prev.group(1), '-> printed', int(prev.group(1))+1205)\nEOF"
}
```


### [2026-09-14T02:00:33.529Z] TOOL RESULT

```
Exit code 1
کردن ‎ol‏ عنع آستن ی کند .

‏قیشود ۴ - با شین ‎abs‏ دار بر وزن
دیجور . نوعی از کف دربا است وآن ‎wh Ke‏
سفید وتجویف (۱) بیار دارد . گوشد در خمن
که شراب آن در جوس باشد قدری از آن‌اندازند
از جوش باز ایستد .

‏قیصر با صاد بی نقطه بروزن حیدر,

‏رومی ۴ فرزندی باشد که مادرش پیش
ازآنکه او را ‎aly‏ بمیرد وشکم مادررابشکافند

‏و ‎oT‏ فرزند را )8( بیرون آورند (۳) و چون
(۱) خم۱: تجفیف .
)2( خم۱ : اغطوی.
‎mY‏ قیروطی ‎fin?‏
‎Kissés sty - ۴‏ «اشتینگاس».

‎AYE ‏ص4۳۲‎ Ie win? ‏(فر)‎

‎. ‏چش : -را‎ (sx)

‏قیطاقون

‏اول پادشاهان قیاصره "که اغسطوی ‎٩‏ . نام
داشت ابنچنین بوجودآمد ‎SME‏

‏بتابر آن بدین اسم موسوم
‎at‏

‏شرفی‌بحر محیط ونزدباگ پدربا است وکافورخوب
از آنجا آورند ؛ و ‎cay‏ ,گونند نام کوهی است
در دربای هند 8 .
‎PAD‏ - بر وزن محروم + لوعی از
پرنجاسب است که بوی عادران باند ‎JW‏
‏قیطاقون - با طای ‎glo‏ وقاذیروزن
افلاطرن » بلفت ‎iy,‏ بممنی ترمس است که

‎۰ ‏-آورند‎ iN ‏خم‎ (r)

‏کیم مومن * قس : فیری » قیر -

‎pierre ponce = kisséris st yj! ۴

‎Kaisar oi, - ۴‏ و بتوسط آرامیان وارد عربی شده

‎< ) ‏(فر‎ césar=( ya, ( 6060676 ‏از‎ Caesar ‏اسلام: قیصر» . لاینی‎ Sluis th «
. 12۵۲ ‏و‎ czar gig. ‏(آلم) < 52۳) (روسی)‎ Kaiser =( eC! ) caesar

‏۵ - قصر ‎(Caesar)‏ لقب بولیوس ‎Caius Julius‏ امپراتور روم ( تولدء۱۰- وفات

‏4 - ق.م. ) ‎oy‏ پس از وی امپراتوران روم از خاندان وی را بلقب قیصر خواندندو بعدها همه

‏امپراتوران روم را قیصر نامیدند .
¥ - بجوش اندرون ‎is‏ بهمنجنه

‎gel : ‏رك‎ F

‎. ‏اندرون بیمن و قیصران‎ GS
LOW, ‏منوچپری دامغانی‎ «

‏- دزی ‎Ter‏ اص ۳۷ : ۲ » کوید : « فیصوری , عنوان نوعی از کافور . انطاکی
( دارد ضربر) ‎Ble‏ «کافور » پس از ‎WITS‏ مزبور کوید ‎jt‏ قنصوری ‎shin)‏ ولون )آمده .

‏قیصوری منسوب بموضی از بلاد هند از ‎Lol‏ سرندیب است .

‏رك : فولری .*:

‎Manche ‏حکیم‎ Lint 4) * ۳۳۷ ‏عقار‎ « shy abrotonon ‏نام عربی مرادف‎ - ٩
Traceback (most recent call last):
  File "<stdin>", line 9, in <module>
IndexError: list index out of range
```


## [2026-09-14T02:00:43.712Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('incoming/BQT/BQT_v3_pages.txt',encoding='utf-8').read()\nidx=t.find('قیصر با صاد بی نقطه')\ntags=[m for m in re.finditer(r'\\[pdf page (\\d+)\\]',t)]\nprev=[m for m in tags if m.start()<idx][-1]\np=int(prev.group(1))\nprint('pdf page',p,'-> printed approx',p+1205,p+1207,p+1209)\nEOF"
}
```


### [2026-09-14T02:00:44.939Z] TOOL RESULT

```
pdf page 344 -> printed approx 1549 1551 1553
```


## [2026-09-14T02:00:50.407Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nimport json\nm=json.load(open('incoming/BQT/BQT_v3_pagemap.json'))\nprint(type(m))\nimport itertools\nif isinstance(m,dict):\n    for k in ['342','343','344','345','346']: print(k, m.get(k))\n\""
}
```


### [2026-09-14T02:00:51.457Z] TOOL RESULT

```
<class 'dict'>
342 None
343 None
344 None
345 None
346 None
```


## [2026-09-14T02:00:54.106Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nimport json\nm=json.load(open('incoming/BQT/BQT_v3_pagemap.json'))\nprint(list(m.keys())[:5])\nv=m[list(m.keys())[0]]\nprint(json.dumps(v,ensure_ascii=False)[:300] if not isinstance(v,(int,str)) else v)\n\" "
}
```


### [2026-09-14T02:00:55.237Z] TOOL RESULT

```
['pdf', 'pdf_pages', 'offset_mode', 'anchors', 'map']
data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf
```


## [2026-09-14T02:00:57.325Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nimport json\nm=json.load(open('incoming/BQT/BQT_v3_pagemap.json'))['map']\nfor k in ['342','343','344','345','346']: print(k, m.get(k))\n\""
}
```


### [2026-09-14T02:00:58.439Z] TOOL RESULT

```
342 None
343 None
344 None
345 None
346 None
```


## [2026-09-14T02:01:01.222Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nimport json\nd=json.load(open('incoming/BQT/BQT_v3_pagemap.json'))\nm=d['map']\nprint(type(m), len(m))\nif isinstance(m,list): print(m[340:350])\nelse:\n  ks=list(m.keys())[:10]; print(ks, [m[k] for k in ks])\nprint(d['anchors'][:5] if isinstance(d['anchors'],list) else d['anchors'])\n\""
}
```


### [2026-09-14T02:01:02.502Z] TOOL RESULT

```
<class 'dict'> 592
['1210', '1211', '1212', '1213', '1214', '1215', '1216', '1217', '1218', '1219'] [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
34
```


## [2026-09-14T02:01:05.128Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nimport json\nm=json.load(open('incoming/BQT/BQT_v3_pagemap.json'))['map']\ninv={v:k for k,v in m.items()}\nfor p in range(342,348): print('pdf',p,'printed',inv.get(p))\nprint('printed 1551 -> pdf', m.get('1551'))\n\""
}
```


### [2026-09-14T02:01:06.493Z] TOOL RESULT

```
pdf 342 printed 1549
pdf 343 printed 1550
pdf 344 printed 1551
pdf 345 printed 1552
pdf 346 printed 1553
pdf 347 printed 1554
printed 1551 -> pdf 344
```


## [2026-09-14T02:01:11.122Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nt=open('BQT_v1_pages.txt',encoding='utf-8').read()\nleaves=t.split('\\f')\nfor i,l in enumerate(leaves):\n    if 'اغسطوس' in l: print('leaf',i,'-> printed approx',i-220)\n\""
}
```


### [2026-09-14T02:01:12.519Z] TOOL RESULT

```
leaf 109 -> printed approx -111
leaf 360 -> printed approx 140
```


## [2026-09-14T02:01:29.224Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8').read()\nleaves=t.split('\\f')\nimport re\nfa='۰۱۲۳۴۵۶۷۸۹'\ndef nums(s):\n    return re.findall(r'[۰-۹]{2,4}', s)\nfor i in range(352,370):\n    l=leaves[i]\n    print(i, [n for n in nums(l)][:12], '|', 'برهان قاطع' in l)\nEOF"
}
```


### [2026-09-14T02:01:30.845Z] TOOL RESULT

```
352 ['۱۱', '۳۱', '۲۳'] | False
353 ['۹۹', '۱۳۸'] | False
354 ['۱۳۳۹', '۳۰۱', '۲۱۱', '۱۳۷', '۲۱', '۲۱۹', '۲۸۷', '۱۸۳', '۷۳'] | False
355 [] | False
356 ['۰۰۱۸', '۰۱۸'] | False
357 ['۱۸۰', '۷۵', '۱۶'] | False
358 ['۱۶۱', '۲۲', '۰۷۵', '۳۷', '۱۸۹', '۵۵', '۱۲۰', '۷۵', '۲۷'] | False
359 ['۷۶۱۱', '۳۱۷۵', '۵۵۵۶'] | False
360 ['۲۱۱', '۲۳'] | False
361 [] | False
362 [] | False
363 ['۱۳'] | False
364 ['۱۳', '۷۰'] | False
365 ['۸۲۱', '۲۹۹', '۲۰۹', '۱۸۰', '۱۱۵', '۷۷', '۲۵۱', '۳۷', '۱۵', '۷۰'] | False
366 ['۲۷۹', '۳۰', '۳۸', '۷۵', '۱۳۲۸', '۳۰۰۰', '۰۶', '۱۲۰۰', '۰۰۰۰', '۱۹', '۱۳۷', '۱۳۰۱'] | False
367 [] | False
368 ['۳۳', '۳۹', '۲۴'] | False
369 [] | False
```


## [2026-09-14T02:01:44.571Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8').read()\nleaves=t.split('\\f')\nfor i in (425,430,435,440):\n    print('=== leaf',i)\n    print(leaves[i][:300].replace('\\n',' | '))\nEOF"
}
```


### [2026-09-14T02:01:45.886Z] TOOL RESULT

```
=== leaf 425
ی ۷۰ ‌- | پاخر و بنتحالت وسکون رای‌بی‌هطه | و زای نقطه‌دار , نام فصبهابست در خراسان ونم | کوشه‌نی باشد از چهل و حشت کوش موسیقی . | باخسه - با سین بی‌هطه‌بروزن باغچه. | راهی باشد بفیر از راء ثعارف خانهای که از آن | راه نز آهد و رفت نوان‌کرد - و نثتر حجام را | نیز گوشد . | باخود - بروزن کافور , نلبجد ایراهیم | کگویند س
=== leaf 430
باد وح | که جربی بادروج گویند ؛ د بسی کوبند بادرو | تره‌ایست که بر کش بسپرغم میماند و بوی ترنج | میدهد | پاددوج - بسکون جیم .کل بتان | افروز باشد و بویدن آن عطه آورد وکز دن | عقرب را نافع باشد , و آثرا پعربی ضومردهفرح | القبالمحزون (۱) خوانئد » وبعن ی کوندریحان | کوهی است ٩‏ | بادرو ده ت بفتح‌زای نقطه‌دار ۰ بمعتی | هرر
=== leaf 435
مج وا | باران بر س رگذارند - ۶ حر چیزی راکه تجهت | مانع باران پوشند پیز کویشف - و نم قبیلهایست | از ترکان . | پار ید ۱ د بت بای ابید رسکون‌دال | بی نقطه , نام مطرب خسروپرویز است : گویند | اصل او از جهرم بوده که از توابم شیراز است | و درفن بربط لوازی ر موسیقی دأني عدیل ونظیر | نداشته و سرود مسجع از مخترعات اوست وان | 
=== leaf 440
برداعتن | مردم میگیرد . | باز داشتی - کنابه از :ان کردن | ومنم نمودن باشد ۷ . | بان - بای نرسی و دال یبد بر | وزن پاسبان » ظرفی‌را کوبند که زر باج ی که از | مردم میگیرند در آن ریزند . | پاز ر گان - بتح‌اك. مخنفبازارگان | است که سوداگر باشف ۲۳ | اد فك » بر وزن باربند » سینه بند | طفلان و پتان‌بند زانرا گوبند . | باژر نگ -
```


## [2026-09-14T02:01:59.136Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"قیصر\" incoming/BQT/BQT_v5_pages.txt | head; echo \"### v5 pdf tag for hits\"; python3 - <<'EOF'\nimport re\nt=open('incoming/BQT/BQT_v5_pages.txt',encoding='utf-8').read()\nfor m in re.finditer('قیصر',t):\n    tags=[x for x in re.finditer(r'\\[pdf page (\\d+)\\]',t) if x.start()<m.start()]\n    p=int(tags[-1].group(1)) if tags else None\n    print('printed',p-5 if p else None, t[m.start()-200:m.start()+200].replace('\\n',' '))\n    break\nEOF"
}
```


### [2026-09-14T02:02:00.323Z] TOOL RESULT

```
### v5 pdf tag for hits
```


## [2026-09-14T02:02:17.867Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8').read()\nleaves=t.split('\\f')\nimport re\nfor i in range(356,366):\n    l=leaves[i]\n    hits=[x for x in re.findall(r'.{0,25}برهان\\s*فاطع.{0,25}|.{0,25}برهان\\s*قاطع.{0,25}', l)]\n    print(i, hits, '||', re.findall(r'^\\s*[^\\n]{0,60}', l)[0].strip()[:60])\nEOF"
}
```


### [2026-09-14T02:02:18.958Z] TOOL RESULT

```
356 [] || اخك تلح ه جفتح فوقالی » کنایه از
357 [] || _ٍِِ
358 [] || اشو ی
359 [] || ۳و
360 ['ز برهان فاطع ۲۳)'] || وشطهای سیله دارد . ۱ نوعی ازبوی مادران باتد . گویند کترانیدن
361 [] || فیاصر# روم ؛ او را ازآن جپت قصر گفتندکه
362 [] || اتمون
363 [] || افر اشتن بروزن ومعنی‌برداشتن: بلند
364 [] || آفری
365 [] || ات
```


## [2026-09-14T02:02:44.985Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### FSD jersey\"; grep -n \"jer'sey\\|Jer'sey\\|jersey,\" FSD_vol2.txt FSD_vol3.txt | head -10; echo \"### IEC kaid\"; grep -n \"caedo\\|caedō\\|kaid-\\|khaid\" IEC.txt | head -10; echo \"### SYN\"; grep -n \"caedere\\|caedo\" SYN.txt | head -5; echo \"### ARY\"; ls incoming/ARY 2>/dev/null | head"
}
```


### [2026-09-14T02:02:45.104Z] TOOL RESULT

```
### FSD jersey
FSD_vol2.txt:64013:nerves,  as  from  external  stimulus;  as,  a   knee-jerft  or  Jer'sey,  1   jur'zi;  2   jSr'gy,  a.  1.  Of  or  pertaining  to  the
FSD_vol2.txt:64025:TV.  C.  iius.SEi,L  Strangs  Vouaoe  n.  9.  (b.  1881.1 3.  Pine  woolen  yarn,  or  fine  combed  wool,  as  spun  in Jersey.  ( <   Isle  of  Jersey,  <   L,  Csesarea,  <   Catsar,  Ciesar.J —   blue  Jersey,  a   sailor,— jer'seyed,  a.
FSD_vol2.txt:64026:Obs.]  A   Jer'sey^,  re.  1.  One  of  the  English  Channel  Islands;  45  sq.  m.;
FSD_vol2.txt:64031:jerks,  1   jorks;  2   jSrks,  re.  pi.  Violent  .spasmodic  move-  Jer'sey-an,  1   jOr'zi-eu;  2   jer'sy-an,  a.  Geol.  Ot  or  per- ments  or  twitchings  of  the  person tnimr,      •   •
FSD_vol2.txt:64036:jerk'V»^l  jbrkVr'2  jerk'y,  a.  [jerk'i-bk;  JEBK'i-ES'r’.’i  Jer'sey-an',  re.  Geol  1. 'I'he  Jerseyan  stage  of  the  pieistoce^^^ Moving  or  acting  with  or  by  jerks;  characterized  liy  epoch,  followed  by  the  Aftonian  Interglacial  stage.  3.  The jerks:  spasmodic.  Jerk'ishf;  jerk'somet.— jerk'I-ly,  adc.  ,   ,   ...  .   ,
FSD_vol2.txt:64041:or  two  masts,  used  along  the  Egyptian  coast;  also,  formerly,  Jer'sey-vllle,  1   jur  zi-vll;  2   Jer-gy-vii,  re.  A   city,  coimty-seat a   larger  vessel  plying  in  the  LevanL  [(Douai).  _ ..  mh
### IEC kaid
6597:kai-, modal fragment: “alone, separate; only, but, yet’. Cf. kaikos, kailos (2) Skt. cf. ké-valah “alone, separate'; Arm. cf. kes (‘half ? if for a type *kai-K-. For the semantic parallel cf. *sé- "apart: *semi ‘by parting’ hence ‘half. See sémi); Gk. kaí and Lat. cf. caedo, ére, v. eut, lit. ‘separate’? ambiguously to OCS céZdo, céditi ‘sift? etc., which is pre- ferably to skoid-, q. v.); cf. Lat. cael-ebs (see „ail- below); synth. cpd. in OCS cé-glü (“alone”). Second element obscure)
8728:Kestros, om ‘knife, spear, javelin’. Cf. Kes- *cut, stab'. WP I, 402 & 448 Skt. Sastram ‘knife, dagger’; Oss. cf. sásari Tancet'; Gk. késtros, m., op. n. 'graving- tool; késtra, f. ‘pike’; cf. also (?) ág-kistron, n. “hook, barb’; LW in Lat. cestrum ‘borer, dagger, graving-tool beside caestrum, id. (infl. of caedo); MIr. casar ‘thorn, bodkin,
9395:(ládio? Dad? (1) The supporting evidence for these two formulae is entirely ambiguous. For lílád- as an intensive formula “strike, harm” cf. Lat. laedō, cpds: do. but with an ambiguous initial, cf. (1) slad- in Ir. slaidhim ‘strike, beat, slay’; W Hadd “cut, kil’; EME to slat ‘strike, dash’; (2) *ulad- in MLG wlete "mir": MHG lez, letze ‘bad, wrong’; G letzen ‘to injure’. Parallel Latin intensives include caedo, cpds. -cido, cf. Skt. såsadmi “feli, de- stroy’ beside radical Sat-tum, inf. ‘to fall” and the desid. Sisatsámi “wish to felP; and Lat. quaero, quaes-tum, fr. *quiques- or sim., cf. Skt. Vedic Cikemi “notice; seek’, etc.)
14067:quiquaið, quíqueio “look, see, await, appear”. Cf. WP I, 508. (Variants, of uncertain IE vocal- ism: ques-, quíques-; cf. quëið) Vedic Cikémi, v. “search, look at, watch" be- side Cage, mp. “appear, see, notice, tell’; cf. Caksanam, n. ‘appearance’; Arm. cf. kkvem, KKem, v. tr. “affect, move’; Gk. cf. paptaíno, v. ‘stare’; Lat. cf. quaero and quaeso, ére, v. ('seek', if fr. *quíiquoso, cf. ? caedo, laedo); EMCz. Ckáti, inf. ‘wait’; Cz. po-Ckat, d: cf. also OCS, OCz. čakati, inf. “wait, hope?
16184:sladó, ið “strike, kil Gk. (?) lázomai, v. ‘seize’; Ir. slaidhim, v. ‘strike, slay’; OBr. ladam, 1sg. ‘kill’; Br. laza, inf, lazet, pp. id.; W ladd, id., Cor. ladha, id.; EME to slat, v. ‘strike, beat'; E cf. to slate. (Note on Lat. laedo, ére, cpds: -lido *strike, injure'. This may represent an inten- sive type *slíslád-, cf. caedo, ére in relation to cado, fr. *KíKádo? See Kad-, & quaero < *quíquér-?)
### SYN
8060:Skt. khid- ‘tear, press’, pple. khinna- ‘oppressed, exhausted, tired’, perh. ; Lat. caedere ‘cut, beat, strike down. Walde-P. 2.538.
14033:i ° Goth. maitan, sneipan Lith. piauti, kirsti, réx); ve ae sia ON skera, snida, telgja, Lett. griezt, erate zi Lat.  secdre, caedere heggva, meila ChSl. rézali, st&ti Ckrojiti) It. tagliare Dan. skare, hugge SCr. rezali, sjedi Ir. couper, tailler, tran- Sw. skdra, hugga Boh. Tezalt, krdjett, sekat;
14035:‘Cut’ is an extremely broad notion, represented by several IE roots and by a great variety of words in many of the TE languages. As in various non-IE languages there is no generic word for ‘cut’ but only special words according to the instrument used or the object cut, so even in IE there is only partial gen- eralization. There is often a partial dis- tinction between ‘cut’ with a knife, etc., and ‘cut’ by blows of an ax, etc., the lat- ter use overlapping with ‘strike’ (as in Grk. xér7w, Lat. caedere, etc.). There may be special expressions for ‘cut wood or stone, hew or carve’ (9.45, 9.81), for ‘cut grass or grain, mow, reap’, (8.32), for ‘cut hair or wool, shear’, for ‘cut gar- ments’ (cf. sbs. for ‘tailor’, partly = ‘cutter’, 6.13), for ‘cut apart’, ‘split’ (9.27) or ‘separate’ (12.23), etc., so that the same roots appear here and under many other headings. Where there is widespread agreement in a particular special use, as in certain groups for ‘hew’ in carpentry and for ‘mow’ and so not listed here, the presumption is that this is inherited. In certain other cases the special use is clearly the result of special- ization, as in the current use of NE shear (cf. its history in NED s.v.). But most often the same formal group shows
14051:5, Lat. caedere ‘strike, cut’ (9.21).
14145:It. cesote (not common), OFT. cisoires fr. VLat. *caesdrium, *cisdrium, fr. caedere ‘cut down, strike’ (9.21). REW 1475.
### ARY
ARY_aryanpur_kashani_rishehaye_hend_o_orupayi.pdf
ARY_latin_index_pages.txt
ARY_pages.txt
ARY_pages.txt.pages
```


## [2026-09-14T02:02:55.773Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### ARY\"; grep -n \"چلنگر\\|چیلان\\|سیمان\\|قیصر\" incoming/ARY/ARY_pages.txt | head -10; echo \"### FSD page num near jersey\"; python3 - <<'EOF'\nt=open('FSD_vol2.txt',encoding='utf-8').read()\nleaves=t.split('\\f')\nfor i,l in enumerate(leaves):\n    if \"Fine  woolen  yarn\" in l:\n        print('leaf',i)\n        import re\n        print(re.findall(r'\\b1[0-9]{3}\\b', l)[:15])\n        print(l[:200])\nEOF"
}
```


### [2026-09-14T02:02:57.054Z] TOOL RESULT

```
### ARY
### FSD page num near jersey
```


## [2026-09-14T02:03:01.800Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('FSD_vol2.txt',encoding='utf-8').read()\nlines=t.split('\\n')\ni=64025\nprint(repr(lines[64024][:200]))\n# find nearest form feed boundary\nff=t.count('\\f')\nprint('formfeeds',ff)\npos=t.find(\"Fine  woolen  yarn\")\nprint('pos',pos, 'leaf', t[:pos].count('\\f'))\nleaf=t.split('\\f')[t[:pos].count('\\f')]\nimport re\nprint(re.findall(r'\\b1[0-9]{3}\\b', leaf)[:20])\nprint(leaf[:300])\nEOF\necho \"### ARY file check\"; head -c 300 incoming/ARY/ARY_pages.txt; echo; grep -c \"\" incoming/ARY/ARY_pages.txt"
}
```


### [2026-09-14T02:03:03.235Z] TOOL RESULT

```
'TV.  C.  iius.SEi,L  Strangs  Vouaoe  n.  9.  (b.  1881.1 3.  Pine  woolen  yarn,  or  fine  combed  wool,  as  spun  in Jersey.  ( <   Isle  of  Jersey,  <   L,  Csesarea,  <   Catsar,  Ciesar.J —   '
formfeeds 773
pos -1 leaf 773
['1897', '1878', '1881', '1495', '1886', '1887', '1478', '1633', '1234']
),  a   German  physiologist.  3. Otto.  (“htl813-2/2tl865).  a   German  dramatist  and  novelist. Lud'wlgll.  (»/2ilS4.5-«/i!l8S8).  A   king  of  Bavaria;  became ,   Insane  and  drowned  himself.  ,
Lud-wlg'1-a,  1   liid-wij'i-e;  2   Ifld-wlg'i-a,  n.  Bot.  A   genus of  chiefly  North-Ameri
### ARY file check
[pdf page 1]
6 و۵
هندواروبابی_ 1010 1۵ 1000]
۵9 (۸9ا

۲1۹۸۸۱
۱۸۸۵۱۱ ۸۵ ٩۵۱۱
۸:۱۸
۲۸۵۳۵۸۵
[pdf page 2]
نج ۰
۰ پیشگفتار ۳
پیش گفتار
هدف این کتاب نشان دادن ریشه‌ی هند و اروپایی واژه‌های فار
16204
```


## [2026-09-14T02:03:09.356Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('FSD_vol2.txt',encoding='utf-8').read()\npos=t.find(\"Csesarea\")\nprint('pos',pos)\nli=t[:pos].count('\\f')\nleaf=t.split('\\f')[li]\nprint('leaf',li)\nprint(re.findall(r'\\b1[0-9]{3}\\b', leaf)[:20])\nprint(leaf[:250].replace('\\n',' | '))\nEOF\necho \"### ARY short\"; grep -n \"چلنگ\\|چیلا\\|سیما\\|قیص\" incoming/ARY/ARY_pages.txt | head -10"
}
```


### [2026-09-14T02:03:10.768Z] TOOL RESULT

```
pos 13116266
leaf 612
['1881', '1871', '1917', '1075', '1914', '1859', '1879', '1889', '1881', '1890', '1668', '1534', '1773', '1814', '1792', '1804', '1902', '1815']
 re.  A   young  salmon,  the  ginkin. | }erk'i-nes.s,  1   jurk'i-nes;  2   j§rk'i-n6s,  re.  The  quality  of being  jerky. | jer'kln-et,  1   JOr'kin-et;  2   jerikln-et,  re.  (Scot, jacket  or  outer  bodice  worn  by  women. | TV.  C.  iius.SEi,L  St
### ARY short
```


## [2026-09-14T02:03:22.146Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources && python3 -c \"\nimport json;d=json.load(open('refs_online.json'))['KLN']\nprint(d['page_offset']); print(d.get('lookup_hint'))\n\"; cd refs && python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8').read()\npos=t.find('kaiser,  n.,  an  emperor')\nprint('leaf', t[:pos].count('\\f'))\npos2=t.find('Caesar,  masc.  PN.')\nprint('Caesar leaf', t[:pos2].count('\\f'))\nEOF"
}
```


### [2026-09-14T02:03:23.389Z] TOOL RESULT

```
KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.
leaf 452
Caesar leaf 126
```


## [2026-09-14T02:03:41.421Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8').read()\nlv=t.split('\\f')\nfor i in range(449,456):\n    l=lv[i]\n    print(i, '|', re.findall(r'\\b\\d{3}\\b', l)[:8], '|', l.strip()[:70].replace('\\n',' '))\nEOF"
}
```


### [2026-09-14T02:03:42.650Z] TOOL RESULT

```
449 | ['832', '833'] | s’,  yuktdh, ‘harnessed’,  Gk.  ^euyvuvai,  ‘to  yoke,  har¬ ness’,  A
450 | ['834', '835', '963'] | o  gau- dere,  ‘to  rejoice'.  See  gaud  and  cp.  enjoy.  Cp. also  
451 | ['636', '837'] | ‘rose’, and  ab,  ‘water’.  See  rose  and  abdest. Julia,  fem.  PN. 
452 | ['838', '744', '202', '203'] | cer  of  the kings  of  England  from  the  reign  of  William  I to  
453 | ['840', '841'] | called  from  the  name  of  the place  where  it  was  first  found, 
454 | ['842', '843', '160', '331'] | its  OS., ON.,  OHG.  equivalents.  See  comb  and  cp. kempt. kemp,  
455 | ['844', '845', '846'] | ‘stalk,  blade’, Lett,  zeiju,  ziet,  ‘to  rise’  (said  of  flowers;
```


## [2026-09-14T02:03:56.604Z] TOOL CALL #49: Bash

```json
{
 "command": "for u in \"https://en.wiktionary.org/wiki/%DA%86%D9%84%D9%86%DA%AF%D8%B1\" \"https://abadis.ir/fatofa/%DA%86%DB%8C%D9%84%D8%A7%D9%86/\" \"https://abadis.ir/fatofa/%D8%B3%D9%85%D9%86%D8%AA/\" \"https://www.ahdictionary.com/word/search.html?q=cement\" \"https://en.wiktionary.org/wiki/%D9%82%DB%8C%D8%B5%D8%B1\" \"https://en.wiktionary.org/wiki/Caesar\"; do echo \"### $u\"; python3 tools/fetch_source.py \"$u\" --note \"page 457 Skhai: Persian chelangar/chilan/sement, qeysar, Caesar\" 2>&1 | tail -1; done"
}
```


### [2026-09-14T02:04:02.635Z] TOOL RESULT

```
### https://en.wiktionary.org/wiki/%DA%86%D9%84%D9%86%DA%AF%D8%B1
/home/sfmqrb/git/rishe/data/verification/sources/web/6abe9559ce4641ac.txt
### https://abadis.ir/fatofa/%DA%86%DB%8C%D9%84%D8%A7%D9%86/
/home/sfmqrb/git/rishe/data/verification/sources/web/ae7491cbb02c38b2.txt
### https://abadis.ir/fatofa/%D8%B3%D9%85%D9%86%D8%AA/
/home/sfmqrb/git/rishe/data/verification/sources/web/8823ce79d18c323a.txt
### https://www.ahdictionary.com/word/search.html?q=cement
/home/sfmqrb/git/rishe/data/verification/sources/web/72ab39fedcf61fa1.txt
### https://en.wiktionary.org/wiki/%D9%82%DB%8C%D8%B5%D8%B1
/home/sfmqrb/git/rishe/data/verification/sources/web/7808a50576c24e0b.txt
### https://en.wiktionary.org/wiki/Caesar
/home/sfmqrb/git/rishe/data/verification/sources/web/bd5c56d988dab39b.txt
```


## [2026-09-14T02:04:05.666Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"### چلنگر\"; grep -n -i -A8 \"Etymology\" 6abe9559ce4641ac.txt | sed -n '1,40p'; echo; echo \"### قیصر fa\"; grep -n -i -A6 \"Etymology\" 7808a50576c24e0b.txt | sed -n '1,30p'"
}
```


### [2026-09-14T02:04:05.748Z] TOOL RESULT

```
### چلنگر
65: Etymology 
66-
67- 1.3 
68- Pronunciation 
69-
70- 1.4 
71- Noun 
72-
73- 1.4.1 
--
149: Etymology
150- [ edit ] 
151-
152- From Middle Persian [script needed] ( cyl’ngl /⁠čēlāngar⁠/ ) . Equivalent to چیلان ( čilân , “ iron chain, lock, ring ” ) +‎ ـگر ( gar , “ -er ” ) .
153-
154- Pronunciation
155- [ edit ] 
156-
157- ( Classical Persian ) IPA ( key ) : /t͡ʃi.lin.ˈɡar/ 

### قیصر fa
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Proper noun 
--
148: Etymology
149- [ edit ] 
150-
151- Borrowed from Arabic قَيْصَر ( qayṣar ) .
152-
153- Pronunciation
154- [ edit ]
```


## [2026-09-14T02:04:09.650Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"### abadis چیلان\"; grep -n \"معین\\|چیلان\" ae7491cbb02c38b2.txt | head -20; echo; echo \"### abadis سمنت\"; grep -n \"معین\\|سمنت\\|سیمان\" 8823ce79d18c323a.txt | head -20"
}
```


### [2026-09-14T02:04:09.736Z] TOOL RESULT

```
### abadis چیلان
4:TITLE: چیلان - معنی در دیکشنری آبادیس
6:چیلان - معنی در دیکشنری آبادیس 
10: چیلان
12: مترادف چیلان : ابزارآلات، چیلانه، عناب
17: اسم: چیلان (پسر) (فارسی) 
23: چیلان. ( اِ ) عناب را گویند. ( جهانگیری ) ( برهان ) ( انجمن آرا ). عناب بود. ( اوبهی ). سنجد گرگانی بود. ( صحاح الفرس ). سنجد جیلان. در ترکستان چین نوعی عناب است ریزتر از عناب ایران : 
24:سنجد چیلان به دو نیمه شده 
26:مانند یکی درخت چیلان 
28:|| چوب سفتی است از درخت عناب و نسبت بدان و مشتغل به پیشه مربوط به آن چیلانی است. ( الانساب سمعانی ).
29: چیلان. ( اِ ) آلات و ادواتی که از آهن سازند مانند زرفین در و زنجیر وحلقه های کوچک و یراق زین و لگام اسب و رکاب. ( برهان ) ( از آنندراج ). خرده ریزی که از آهن سازند چون چفت وحلقه و لجام و غیره. ( یادداشت مؤلف ). || بیشه ای که در آن خرسها منزل کنند. ( ناظم الاطباء ).
30: چیلان. ( اِخ ) دهی است از دهستان سراجو بخش مرکزی شهرستان مراغه. در 28 هزارگزی خاور مراغه به قره آغاج واقع است. کوهستانی و معتدل است ، 1264 تن سکنه دارد. از رودخانه لیلان و چشمه آبیاری میشود. محصولش غلات ، کرچک ، چغندر و نخود است. این قریه از دومحل به نام چیلان بالا و چیلان پائین تشکیل شده است و به فاصله هزار گز از هم قرار دارند. سکنه چیلان پائین 733 تن میباشد. ( از فرهنگ جغرافیایی ایران ج 4 ). 
37: فرهنگ معین
49: چیلان (واشینگتن). چیلان ( به انگلیسی: Chelan ) شهری در شهرستان چیلان، ایالت واشنگتن است که در سرشماری سال ۲۰۱۰ میلادی، ۳۸۹۰ نفر جمعیت داشته است. [ ۳] [ ۴] 
50: wiki: چیلان (واشینگتن) 
56: سنجد گرگان. سیلانه. شیلانه. چیلان. چیلانه دار . چیلانگ/. ارج. درخت شیلان. درخت شیلانک. تبرخون. سنجد جیلان. سنجد گیلان
58:سنجد چیلان به دو نیمه شده
60:مانند یکی درخت چیلان
70:• فرهنگ فارسی، محمد معین، انتشارات امیر کبیر، تهران، ۱۳۷۵
80: آبادیس از سال 1385 فعالیت خود را در زمینه فن آوری اطلاعات آغاز کرد. نخستین پروژه آبادیس، سایت دیکشنری آبادیس بود. دیکشنری آنلاین آبادیس از ابتدا تاکنون تغییرات بسیاری کرده و ویژگی های مختلفی به آن اضافه شده است. آبادیس افزونه ای کاربردی برای مرورگرهای فایرفاکس و کروم و اپلیکیشن موبایل طراحی کرده است که میتوانید از لینک های بالا دانلود کنید. دیکشنری آبادیس شامل بخش هایی نظیر دیکشنری به زبان های مختلف از جمله انگلیسی، فارسی، عربی و همچنین بیست دیکشنری تخصصی با تلفظ انگلیسی و آمریکایی، ترجمه مخفف و کلمات اختصاری، مترجم آنلاین متن، لغتنامه دهخدا، فرهنگ معین، فرهنگ فارسی عمید، فرهنگ مترادف ها و متضاد ها، معادل فارسی کلمه یا به شیوه درست تر برابر پارسی واژه، فرهنگ سره، عبارات مصوب فرهنگستان زبان و ادب فارسی، دانشنامه عمومی، دانشنامه اسلامی، دیکشنری نام ها، هم خانواده یاب، تصویر مرتبط با کلمه، معنی در حل جدول کلمات متقاطع و ابزارهایی مانند واژه ساز ، راهنمای انتخاب اسم و ... می باشد. 

### abadis سمنت
4:TITLE: سمنت - معنی در دیکشنری آبادیس
6:سمنت - معنی در دیکشنری آبادیس 
10: سمنت
13: مترادف سمنت : سیمان
14: متضاد سمنت : ساروج
21: سیمان
22:سیمان مصنوعی مخلوطی است از خاک دواری سنگ آهک که آن را در کوره های دواری می پزند . ظرفهای پخت سیمان استوانه های دواری هستند به ارتفاع ۶۳ متر و به قطر ۲ / ۴ متر . سیمان با شعله های زغال گرم میشوند و پس از درست شدن در ظرفی میریزند و در آن سرد میگردد . سیمان طبیعی را از تکلیس سنگ آهکی که در ۳٠ - ۶٠ درصد خاک رس داشته باشد به دست می آورند ولی این نوع کم مصرف است . یا سیمان مسلح . سیمانی که آن را با ریگ مخلوط کنند و در قالبهای چوبی که میله های آهنی دارد بریزند و آن پس از انجماد استحکام بسیار می یابد و در ساختمانهای سنگی به کار رود . 
24: فرهنگ معین
26: (س مِ نْ ) [ انگ . ] (اِ. ) سیمان . 
30: = سیمان 
35: سیمان، سمنت
48: آبادیس از سال 1385 فعالیت خود را در زمینه فن آوری اطلاعات آغاز کرد. نخستین پروژه آبادیس، سایت دیکشنری آبادیس بود. دیکشنری آنلاین آبادیس از ابتدا تاکنون تغییرات بسیاری کرده و ویژگی های مختلفی به آن اضافه شده است. آبادیس افزونه ای کاربردی برای مرورگرهای فایرفاکس و کروم و اپلیکیشن موبایل طراحی کرده است که میتوانید از لینک های بالا دانلود کنید. دیکشنری آبادیس شامل بخش هایی نظیر دیکشنری به زبان های مختلف از جمله انگلیسی، فارسی، عربی و همچنین بیست دیکشنری تخصصی با تلفظ انگلیسی و آمریکایی، ترجمه مخفف و کلمات اختصاری، مترجم آنلاین متن، لغتنامه دهخدا، فرهنگ معین، فرهنگ فارسی عمید، فرهنگ مترادف ها و متضاد ها، معادل فارسی کلمه یا به شیوه درست تر برابر پارسی واژه، فرهنگ سره، عبارات مصوب فرهنگستان زبان و ادب فارسی، دانشنامه عمومی، دانشنامه اسلامی، دیکشنری نام ها، هم خانواده یاب، تصویر مرتبط با کلمه، معنی در حل جدول کلمات متقاطع و ابزارهایی مانند واژه ساز ، راهنمای انتخاب اسم و ... می باشد.
```


## [2026-09-14T02:04:25.625Z] TOOL CALL #52: Bash

```json
{
 "command": "for u in \"https://abadis.ir/fatofa/%D8%B3%D8%B2%D8%A7%D8%B1%DB%8C%D9%86/\" \"https://abadis.ir/fatofa/%D8%AA%D8%B2%D8%A7%D8%B1/\" \"https://abadis.ir/fatofa/%DA%98%D8%B1%D8%B3%D9%87/\"; do echo \"### $u\"; python3 tools/fetch_source.py \"$u\" --note \"page 457 Skhai: Persian sezarin, tezar, zerseh\" 2>&1|tail -1; done\npdftoppm -f 457 -l 457 -r 200 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg457 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg457.png"
}
```


### [2026-09-14T02:04:31.883Z] TOOL RESULT

```
### https://abadis.ir/fatofa/%D8%B3%D8%B2%D8%A7%D8%B1%DB%8C%D9%86/
/home/sfmqrb/git/rishe/data/verification/sources/web/086c64dea4974d3f.txt
### https://abadis.ir/fatofa/%D8%AA%D8%B2%D8%A7%D8%B1/
/home/sfmqrb/git/rishe/data/verification/sources/web/1521a133b7890a3c.txt
### https://abadis.ir/fatofa/%DA%98%D8%B1%D8%B3%D9%87/
/home/sfmqrb/git/rishe/data/verification/sources/web/63b6d5d7d7335f43.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 79186 Sep 13 22:04 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg457.png
```


## [2026-09-14T02:04:33.832Z] TOOL CALL #53: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg457.png"
}
```


### [2026-09-14T02:04:34.458Z] TOOL RESULT

```

```


## [2026-09-14T02:04:34.455Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-14T02:04:47.999Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && pdftoppm -f 457 -l 457 -r 500 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf pg457hi && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg457hi.png'); print(im.size)\nw,h=im.size\nim.crop((int(w*0.50),int(h*0.11),int(w*0.80),int(h*0.175))).save('pg457_crop3.png')\n\"; ls"
}
```


### [2026-09-14T02:04:52.488Z] TOOL RESULT

```
(4250, 5500)
391-top.png
394hi.png
394-zoom.png
400-bot.png
400-top.png
404-top.png
411-top.png
412-zoom.png
414-bot.png
417hi.png
417-top.png
417-zoom.png
421-top.png
428hi.png
428-zoom2.png
428-zoom.png
429hi.png
429-zoom.png
431-top.png
432-bot.png
436-full.png
afm74-420.png
afm76-421.png
agents.txt
ahd430.txt
beekes410.txt
bqt1328-ftr-437.png
bqt1328-hdr-437.png
bqt1328-top-437.png
bqt1330-top-437.png
bqt1-440.txt
bqt2123-fn-435.png
bqt390_436_foot.jpg
bqt390_436_top.jpg
bqt390_662_foot.jpg
bqt390_662_top.jpg
bqt390_n436.jpg
bqt390_n662.jpg
bqt439-l254.jpg
build2-434.py
build3-434.py
build-389.py
build-390.py
build-391.py
build393.py
build-394.py
build-395.py
build-396.py
build-398.py
build-400.py
build-401.py
build-405.py
build-406.py
build-407.py
build-412.py
build-414.py
build-415.py
build-417.py
build-418.py
build-419.py
build-422.py
build-425.py
build-426.py
build-428.py
build-429.py
build-430.py
build-431.py
build-434.py
build-435.py
build-438.py
c404-empty.png
c404-greek.png
c404-patil.png
c404-pest.png
c404-symp2.png
c404-symp.png
c412_cedar.png
c412_makrome.png
c412_makrome_zoom.png
c412_meqrameh.png
c412_meq_zoom.png
c412_sedr_zoom2.png
c412_sedr_zoom.png
c442-fa8.png
c442-samavar.png
crop14-394.png
crop18-394.png
crop411_a.png
crop411_b.png
crop411_c.png
crop419_a.png
crop419_b.png
crop419_c.png
crop419_d.png
crop419_grk.png
crop419_skt.png
crop428a.png
crop428b.png
crop428c.png
crop428d.png
crop-437.png
e0-434.json
edit_about.py
edit_research.py
ffprof
gen-420.py
irn-425.pdf
irn-425.txt
kent2-448.txt
kent-448.txt
knt-440.txt
knt443.txt
meta-443-knt.json
pg390b.jpg
pg390b.png
pg390.png
pg391big.png
pg391crop.png
pg391.png
pg391root.png
pg391sog.png
pg392.png
pg393.png
pg394hi.png
pg394.png
pg397.png
pg398.png
pg399-crop1.png
pg399-greek.png
pg399.png
pg399-sog.png
pg400big.png
pg400_fa_heli.png
pg400_fr2.png
pg400_french.png
pg400_kasak2.png
pg400_kasak3.png
pg400_kasak.png
pg400.png
pg402.png
pg404hi.png
pg404.png
pg405.png
pg406.png
pg407.png
pg408-ampus.png
pg408-germ.png
pg408.png
pg409.png
pg410hi.png
pg410-k2.png
pg410-kadm2.png
pg410-kadm.png
pg410-persian.png
pg410.png
pg410-q2.png
pg410-qedam.png
pg411_300.png
pg411.png
pg412_hi.png
pg412.png
pg412_uhi.png
pg413.png
pg414-greek.png
pg414.png
pg415-emptybox.png
pg415hi.png
pg415.png
pg416-v.png
pg417.png
pg418hi.png
pg418.png
pg418-raj2.png
pg418-raj3.png
pg418-rajidan.png
pg419_hi.png
pg419.png
pg420b.png
pg420.png
pg421.png
pg422.png
pg423.png
pg424.png
pg426.png
pg428hi.png
pg428.png
pg429-crop1.png
pg429-crop2.png
pg429-crop3.png
pg429hi.png
pg429.png
pg431.png
pg432.png
pg433.png
pg435-n1.png
pg435-n4.png
pg435.png
pg436.png
pg437-437.png
pg437hi-437.png
pg438.png
pg439.png
pg440.png
pg442hi-442.png
pg442-p442.png
pg443.png
pg444.png
pg444-serom.png
pg444-sibum.png
pg445-crop.png
pg445.png
pg446.png
pg447-crop.png
pg447.png
pg449.png
pg450hi.png
pg450-pechkam.png
pg450.png
pg450-shangarf.png
pg452.png
pg453.png
pg454.png
pg456-germ.png
pg456hi.png
pg456.png
pg457_crop3.png
pg457hi.png
pg457.png
pg458.png
queue.txt
sem410.html
u_mak.png
u_meq.png
u_sedr.png
write397.py
write-402.py
write409.py
write410.py
write436.py
```


## [2026-09-14T02:04:55.644Z] TOOL CALL #55: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg457_crop3.png"
}
```


### [2026-09-14T02:04:55.666Z] TOOL RESULT

```

```


## [2026-09-14T02:04:58.941Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg457hi.png'); w,h=im.size\nim.crop((int(w*0.58),int(h*0.148),int(w*0.80),int(h*0.185))).resize((int(w*0.22*1.6),int(h*0.037*1.6))).save('pg457_crop3b.png')\n\""
}
```


### [2026-09-14T02:05:00.585Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T02:05:03.019Z] TOOL CALL #57: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg457_crop3b.png"
}
```


### [2026-09-14T02:05:03.046Z] TOOL RESULT

```

```


## [2026-09-14T02:05:06.574Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg457hi.png'); w,h=im.size\nc=im.crop((int(w*0.60),int(h*0.168),int(w*0.80),int(h*0.192)))\nc=c.resize((c.width*2,c.height*2))\nc.save('pg457_crop3c.png')\n\""
}
```


### [2026-09-14T02:05:08.631Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T02:05:10.954Z] TOOL CALL #59: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg457_crop3c.png"
}
```


### [2026-09-14T02:05:10.982Z] TOOL RESULT

```

```


## [2026-09-14T02:05:26.033Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### SKT\"; grep -n \"^scissors\\|^chisel\\|^cement\\|^jersey\\|^czar\" SKT.txt | head; echo \"### WEB vol1 caesar/cement\"; grep -n -i \"Caesarean\\|^cement,\" WEB*.txt | head -5; echo \"### LKT tsar\"; grep -n -i \"Zar\\b\\|Kaisar\\|Caesar\" LKT.txt | head -8; echo \"### AFM قيصر\"; grep -n \"قيصر\\|قیصر\" AFM.txt AFM_alt.txt 2>/dev/null | head -6; echo \"### PLA\"; ls | grep -i \"PLA\\|ASB\" "
}
```


### [2026-09-14T02:05:26.214Z] TOOL RESULT

```
### SKT
### WEB vol1 caesar/cement
26062:Caesarean section or operation; a surgical operation for delivenng a baby by cutting through the mother's abdominal and uterine walls: so called because Julius Caesar was supposedly born in this manner.
30343:1. pertaining to the deer, or to animals o the family Cervidz. 2. like a deer. d cér’vix, n.; pl. cér-vi'cés, cér’vix-es, [L., neck.] Es: 1. the part between the thorax and the A nead the neck, especially the back of the neck. 2. any necklike part or appendage, as of the uterus, urinary bladder, etc. 4 É Cér’vus, n. [L., a eerd a genus of ruminants, Ee formerly including all species of deer, now confined to the red deer and related species. cé/ryl, n. [L. cera, wax, and -yl.] the hypothet- ical radical of cerotin. ceryl alcohol; same as cerotin. h cé’/sa-ré, n. in logic, a mnemonic word desig- nating a syllogism with a universal negative major premise, a universal affirmative minor premise, and a universal negative conclusion; as, x is not y; y is z; therefore x is not z. 5 Cé-sa’/ré-An, Cē-şã’ri-ăn, a. and z. same as = Caesarean. 7 cé’si-ous, a. same as caesious. cé/si-um, 7. [neut. of L. caesius, blui gray] a soft, bluish-gray, ductile, metallic chemi element, the most electropositive of all the elements: used in photoelectric cells: symbol, Cs; atomic weight, 132.91; atomic number, 55: also spelled caesium. ces’pi-tine, 7. [L. cæspes (itis), a turf.] an ol distilled from peat. = ces-pi-ti’tious (-tish’us), a. [L. cespes (its), a turf.] pertaining to turf; e of turf. = ces/pi-tOse, a. in botany, growing in tufts or clumps; matted. _ * È ces’pi-tōse-ly, adv. in a cespitose manner. ces’pi-tous, 4. pertaining to turf; turfy; as, cespitous plant. ces-pit’i-lose, a. growing in little bun as the tufted grasses. F 7 cess, n. [for sess, from assess.] in I: assessment; a tax on land: now u in bad cess to, meaning “bad luck to. cess, v.t.; cessed (sest), pt., $ 7 to levy a tax; to make an assessmen tion ot assess. [Obs.] cess, v.i. [ME. cessen; OFr. to cease.] to relinquish a leg ces’sant, a. [L. cessans (-antis), ppr. í to cease.] ceasing; intermittent. [( ces-sa/tion, n, ÍL. cease.] a ceasing; uing motion or action of temporary or final. a cessats agreed to b
93950:hys-t@r-og’e-ny, n. [hystero- producing.] the induction of hys/’tér-oid, a. [hystero-, and resembling hysteria; as, a hysteroid hys/te-ron proteron, [GF. h sie Á of hysteros, latter, following, 10% neut aa x proteros, former.) nd broteron. _ 1. afigurein which the logi : is reversed; as, “I die, I fant T ache ideas 2. in logic, the fallacy of assumin; and using as an argument, what ics true, proved; begging the question, —— *® to be Bae eee On A SBY, 2 (hystero-, and Gr path uffering.] an i se i $ bs rae g 1 7 se disorder of thy ys-tér-oph’y-ta, n.pl. same as F hys:tér-oph’y-tal, a. pertaining (ey, phyte or to the Hysterophyta, ystero- lh G2 a n. [hystero-, and Gr } a plant.] in botany, a plant which Phylon, from and lives upon organic matter; aPrings of the order Hysterophyta; a fungus Plant ee growth. , gus or any, ys:tér-op-t0/sis, n. [hystero-, Pen w falling.) falling or (ee of chert s:tér-ot/O-my, n. [hyslero- i tating] Y, n. [hysteros, and Ge tome, a 1. a Caesarean operation, 2. an incision of the uterus, hys:tri-ci/a-sis, n. same as hyslricismus pe a. (L. hystrix (-icis), a Porcupine and -ine.] pertaining to or res i k
### LKT tsar
275:'Handgriff  eines  Werkzeuges'.  Aus  dem plr.  ifässen  wurde  pg.  alfeizar  'Griff einer  Säge'.  Etymologie  zweifelhaft. [DE  112.
416:86.  Ar.  'anzarüt:
817:'Markt'  [Horn  NpEt  S.  38,  Nr.  166].  Das Wort  wurde  im  17.  Jahrhundert  durch Reisende  zunächst  mit  Bezug  auf  orien- talisi-he  Verhältnisse  eingeführt  und  drang dann,  vor  allem  auch  durch  die  Kennt- nis von  1001  Nacht,  in  alle  europäischen Sprachen  ein:  frz.  pg.  sp.  bazar,  it.  ba- zar,  bazzar,  rum.  bazar,  basar;  russ. bazar,  bulg.  serb.  pazar,  cech.  poln. bazar;  eng\. bazar,  bazaar,  ndl.  bazaar, dtsch.  Bazar.  Da  das  Grundwort  stimm- haftes s  [z]  hat,  gehört  sicherlich  auch it.  bazzarare  'täuschen,  betrügen',  siz. bazzariotu  'Betrüger'  hierher  [gegen ML  1010].  [Gorjajew  9.  Kluge  42.  DE GREGORIO  in  ZfromPh  XXV,  747. GrSVociSic  228.
1069:['Was  von  links  nach  rechts  geht'  von pers.  cäp  'link'  Horn  NpEt  S.  97,  Nr.  435 und  rast  'recht'  ebenda  S.  134,  Nr.  603], tk.  öapraz  'eine  Metallbinde,  welche  die UnterofiBziere  bei  den  Janitscharen  [s. hier  Nr.  954]  als  Abzeichen  trugen'; hieraus  rum.  ceapraz  'Borte,  Tresse', ceaprazar   'Posamentier',  ceaprazärie.
1598:'Gerät,  Kamelsattel,  Pferdegeschirr',  vulg. mit  Imäla  [s.  hier  Nr.  637]  gahlz  ge- sprochen ;  hieraus  apg.  ajaez,  sp.  pg. jaez  'Pferdegeschirr',  fig.  'Eigenart', z.  B.  pg.  d'este  jaez ;  Vb.  sp.  enjaezar 'schirren',  pg.  ajaezar  'schirren,  schmük- ken'.    [DE  290.
1970:'Dolch';  tk.  hanger;  hieraus  bulg.  serb. handzar,  poln.  chandzinr,  koncerz, kindzal  [allein  noch  gebräuchlich] 'dass.', ßech.  koncif  'Rapier,  Stoßdegen',  russ. kinzal,  klruss.  cynhal  'Dolch',  russ. koncar,  koncan  'Schwert  mit  schmaler Klinge';  rum.  hanget;  it.  cangiaro  'Dolch mit  sehr  breiter  Schneide  und  ge- krümmtem Grift',  siz.  canciarru  'dass.', frz.  cangiar,  khanjar,  khandjar\  mit ar.  Art.  sp.  pg.  alfange  'Säbel',  frz.  (seit dem  17.  Jahrhundert)  alfange,  sp.  al- fanjazo  'großer  Säbel',  pg.  alfageme 'Dolch,  kurzes  Schwert'.   [Gorjajew  140.
2065:'Tausend'  [Horn  NpEt  S.  244,  Nr.  1093], tk.  hezar  [ung.  ezer];  hieraus  serh.jezero 'lausend'.    [Bern  SlEtWb  455.
2286:[Aus  tk.  jeni,  s.  hier  Nr.  953,  und  ceri 'Heer,  Truppe'  vom  Stamme  der,  ter 'eng  zusammenziehen,  vereinigen'  Väm- bery TktEtWb  S.  170,  Nr.  182  II],  Name des  stehenden  tk.  Heeres  von  1330  bis 1826,  in  welchem  Jahre  Sultan  MAH- MÜD  II.  die  Truppe  auflöste  [vgl.  Th. Menzel,  Das  Korps  der  Janitscharen.  In Beiträge  zur  Kenntnis  des  Orients.  I. (1902/03)  und  in  der  Beilage  zur  All- gem.  Zeitung  1903,  Nr.  284/286].  Hier- aus [und  aus  der  älteren  tk.  Form  ja- nycary]  bulg.  janil^arni,  serb.  janicar^ klruss.  janycar ,  jancar,  necar,  russ. janicar,  poln.  janiczar,  cech.  janicar ; dtsch.  Janitschar,  ndl.  jaiiitsaar,  engl. janizary;iLgiannizzero,  ivz.jannissaire, sp.  jemzaro,  pg.janizaro,  rum.  ianicer, ienicer.  [Devic  DEt  143.  ML  4583. Gorjajew  436.    Bern  SlEtWb  445.
### AFM قيصر
### PLA
```


## [2026-09-14T02:05:31.672Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### SKT scissors\"; grep -n \"scissors\\|Scissors\" SKT.txt | head -4; echo \"### SKT cement\"; grep -n \"cement, \" SKT.txt | head -3; echo \"### SKT czar\"; grep -n \"Czar\\|czar\" SKT.txt | head -4; echo \"### FVQ qaysar\"; grep -n -i \"qaisar\\|Qaysar\\|Caesar\" FVQ.txt | head -6"
}
```


### [2026-09-14T02:05:31.795Z] TOOL RESULT

```
### SKT scissors
3405:Chisel.  (F.-L.)  M.  E.  ^iVr/.-O.  F. thiitl,  ciscl  (F,  cistau).  Cf.  Low  L. cueUus,  scissors  (a.  o.  1353).  O.  F.  cistt answers  to  Low  L.  casilluj  •  or  castHui  \ not  found,  but  a  mere  variant  oi'L.cijonum, a  cutting  instrument  (V<^etiD$)  \  see  Sche» ler's  note  to  Di«.  —  L.  r^i-w«,  supine  of (adtrt,  to  cut ;  whence  alio  late  L.  incisor, a  carver,  cutter ,-  sec  Caeaura.
3406:Bcissors.  (F.-L.)  The  mod.  E.  joj- sors  ii  a  comipt  spelling,  due  to  coofu^ion with  Low  L.  scissor  (from  scimUre,  lo  cut), which,  however,  only  means  a  man  who cuts,  a  batcher,  a  tailor,  and  has,  in  fact, nothing  at  all  to  do  with  the  word.  The old  sfK-lling  was  nxars,  citars,  or  ciurt', and  this  a^iu  was  adapted  (by  pntting the  K.  sufmt  -ers  in  place  of  F.  •caux)  from P.cijfaux,  'sizars,  or  little  sheers;'  Cot. This  F.  ciscaux  =  cutters,  pi.  of  dseau.  a chisel  Thus,  etymologically.  £.  scissors =  risers  ^cisiis,  pi.  oWisil  =  chisel.
16651:Scissors.  (F.-L.)     False! v  fp^ not  from  scinJere^  to  cut.     M.  E-  n> djoum.   —  O.  F.    cucirti,    sbcan; ins.tead     of   eisetiujr,    '  sizars,*    Cot. latter  is  the  pi.  of  O.  F.  dsd,  chisd Ohiael.     Both  words  are  due  to  L. to  cut;  see  Oaoaura.  ^  No  doubt  the was  confused  with  L.  sctsto%  which perly  means  '  a  tailor/  from  ll cut.
### SKT cement
### SKT czar
23469:Russian  from  Latin:  czar.
### FVQ qaysar
14045:of the Amalekites, 1 just as Chosroes and Caesar were titles of the kings
```


## [2026-09-14T02:06:47.668Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in 086c64dea4974d3f 1521a133b7890a3c 63b6d5d7d7335f43; do echo \"=== $f\"; sed -n '1,45p' $f.txt | grep -v \"^$\" | head -25; done"
}
```


### [2026-09-14T02:06:48.916Z] TOOL RESULT

```
=== 086c64dea4974d3f
URL: https://abadis.ir/fatofa/%D8%B3%D8%B2%D8%A7%D8%B1%DB%8C%D9%86/
FETCHED: 2026-09-14T02:04:28Z
STATUS: 200
TITLE: سزارین - معنی در دیکشنری آبادیس
سزارین - معنی در دیکشنری آبادیس 
 دیکشنری مترجم بپرس 
 سزارین
 /sezAriyan/
 برابر پارسی : رستم زایی
 دنبال کنید 
 فرهنگ فارسی
 ( اسم ) عمل جراحی جهت خروج نوزاد از رحم در زایمانهای غیر طبیعی خواه مادر در حال حیات باشد و خواه پس از مادر به منظور نگهداری حیات بود . عمل سزارین معمولا پایین شکم مادر به محاذات رحم برش می دهند و طفل را از رحم خارج میکنند . 
 فرهنگ معین
 (س یَ ) [ فر. ] (اِ. ) عمل جراحی جهت خروج نوزاد از شکم و زایمان های غیرطبیعی . ژول سزار قیصر روم به این طریق به دنیا آمده و نام این عمل از نام او گرفته شده است . 
 فرهنگ عمید
 عمل جراحی در زایمان غیر طبیعی که شکم را در بالای رحم چاک می دهند و بچه را خارج می کنند. 
 دانشنامه اسلامی
 [ویکی فقه] سزارین نوعی عمل جراحی می باشد.
سزارین عمل جراحی و برش دیواره شکم و رحم است که به منظور خارج کردن جنین انجام می شود.
احکام سزارین
به عنوان یاد شده در پاسخ به استفتائات اشاره کرده اند.عمل سزارین به تصریح برخی معاصران جایز است. خونی که پس از سزارین از مجرای طبیعی خارج می شود نفاس به شمار می رود. 
 wikifeqh: سزارین 
 دانشنامه آزاد فارسی
 سِزاریَن (Caesarean section)
سِزاریَن
=== 1521a133b7890a3c
URL: https://abadis.ir/fatofa/%D8%AA%D8%B2%D8%A7%D8%B1/
FETCHED: 2026-09-14T02:04:29Z
STATUS: 200
TITLE: تزار - معنی در دیکشنری آبادیس
تزار - معنی در دیکشنری آبادیس 
 دیکشنری مترجم بپرس 
 تزار
 /tezAr/
 مترادف تزار : امپراطور روس
 معنی انگلیسی : czar 
 دنبال کنید 
 لغت نامه دهخدا
 ( تزآر ) تزآر. [ ت َ زْ ] ( ع مص ) بانگ کردن شیر. ( از محیط المحیط ) ( از اقرب الموارد ). غریدن شیر. ( ناظم الاطباء ). تزار. [ت ِ ] ( اِخ ) تسار . کلمه روسی مشتق از سزار لاتینی. عنوان امپراتوران روسیه.
 تزأر. [ ت َ زَءْ ءُ ] ( ع مص ) بانگ کردن شیر و غریدن. ( منتهی الارب ) ( از المنجد ) ( از اقرب الموارد ). بانگ کردن و غریدن شتر . ( ناظم الاطباء ). و رجوع به تزآر شود. 
 فرهنگ فارسی
 ( اسم ) عنوان پادشاهان روسیه قیصر.
بانگ کردن شیر و غریدن بانگ کردن و غریدن شتر .
 ( تز آر ) بانگ کردن شیر غریدن شیر . 
 فرهنگ معین
 (تِ ) [ روس . ] (اِ. ) عنوان پادشاهان گذشته روسیه ، قیصر. 
 فرهنگ عمید
 عنوان پادشاهان سابق روسیه که تا انقلاب اکتبر در آن کشور سلطنت می کردند. 
 دانشنامه آزاد فارسی
 تِزار
لقب سلاطین روسیه (۱۵۴۷ـ۱۷۲۱). این لقب از واژۀ لاتینی سزار (قیصر)، که عنوان امپراتوری روم بود، گرفته شده است. ایوان مخوف (چهارم)، دوک بزرگ مسکووی، در ۱۵۴۷م در مقام نخستین تزار روسیه تاج گذاری کرد. در ۱۷۲۱ پطر کبیر رسماً این عنوان را به امپراتور سراسر روسیه تغییر داد. این اقدام بخشی از تلاش هایی بود که او برای تجدید سازمان و امروزی کردن کشور به شیوۀ غربی ها انجام می داد. با این حال، عموم مردم عنوان تزار را در مورد فرمانروایان بعدی روسیه نیز به کار می بردند، تا این که نیکلای دوم در انقلاب ۱۹۱۷ روسیه خلع و کاربرد عنوان تزار نیز منسوخ شد. نیز ← روسیه wikijoo: تزار 
=== 63b6d5d7d7335f43
URL: https://abadis.ir/fatofa/%DA%98%D8%B1%D8%B3%D9%87/
FETCHED: 2026-09-14T02:04:30Z
STATUS: 200
TITLE: ژرسه - معنی در دیکشنری آبادیس
ژرسه - معنی در دیکشنری آبادیس 
 دیکشنری مترجم بپرس 
 ژرسه
 /Zerse/
 دنبال کنید 
 فرهنگ فارسی
 نیم تنه بافته شده ازنخ ونوعی پارچه نازک
( اسم ) ۱ - نوعی پارچه نازک . ۲ - نیم تنه بافته از نخ . 
 فرهنگ معین
 (ژِ س ) [ فر. ] (اِ. ) ۱ - نوعی پارچة نایلونی نازک . ۲ - نیم تنة بافته از نخ . 
 فرهنگ عمید
 نوعی پارچۀ نازک. 
 دانشنامه عمومی
 ژرسه گونه ای پارچه ماشینی است که از آن لباس یا اشیای دیگر دوخته می شود. 
پارچه های ژرسه به راحتی شسته می شوند و تنها مشکل آنها اتو کردن است، چرا که این پارچه ها به دلیل داشتن حالت ارتجاعی، شکل خود را از دست می دهند. 
 wiki: ژرسه 
 این نوشته برگرفته از سایت ویکی پدیا می باشد، اگر نادرست یا توهین آمیز است، لطفا گزارش دهید: گزارش تخلف 
 پیشنهاد کاربران
 پارچه نایلونی نازک
 لباس
 + عکس و لینک
```


## [2026-09-14T02:06:57.612Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### KNT lexicon kan/cut\"; grep -n \"^kan-\\|'dig'\\|to cut\" KNT.txt | head -6; echo \"### BRT kaē\"; grep -n -i \"kaēn\\|čiš.*schneiden\" BRT.txt | head -5; echo \"### CHEUNG kai\"; grep -n \"\\*kai\\b\\|kai-\" CHEUNG.txt | head -6"
}
```


### [2026-09-14T02:06:57.710Z] TOOL RESULT

```
### KNT lexicon kan/cut
### BRT kaē
### CHEUNG kai
3119:30 *&aiš (*kaiß)
```


## [2026-09-14T02:07:03.108Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -o -i \"cut[^ ]*\" KNT.txt | sort | uniq -c | sort -rn | head -6; echo \"---\"; grep -n -i \"kan- \\|kan,\" KNT.txt | head -4; echo \"### BRT čiš\"; grep -c \"\" BRT.txt; grep -o \"kaēš[a-z]*\" BRT.txt | head -5"
}
```


### [2026-09-14T02:07:03.271Z] TOOL RESULT

```
     11 cut
      3 cutta
      2 cuts,
      2 cutive,
      2 cutive
      2 cut’,
---
1265:For OP x from £ before consonants, see $102 and $108. Corresponding to Skt. khdnati ‘he digs’ we have OP akantya ‘it was dug’, Av. kan- ‘dig’, and Av. xà ‘well’, with unexplained variation between aspirate and non-aspirate.
1401:root, kan- ‘dig’ + pass. -ya-, in akaniya ‘was dug’. *duS- ll’ + *yür- ‘year’, in dušiyãram ‘famine’. wamarsiyus nsm. ‘by self-death’, Skt. mriyú-š
2531:$220. Tue Passive-Votce Present STEM of pIE was formed by the addition of the suffix pIE -je-/-4o-, which is accented in Sanskrit; in OP the root regularly has the normal grade, with -a-: imf. 3d sg. and pl. abariya abariya", to root bar-; ayadiya ayadiya", to yad-; akaniya, to root kan- ‘dig’; afahya and afahiya, to Ваћ-; avaniya, to van-; ajantya, to jan-; akariya akariya"la, to kar-; pres. ist pl. &ahyàmahy, to dah-; opt. 3d sg. kariyaiš to kar-, frabiyats to frað-, 3d pl. yadiyaiša” to yad-.
4983:Adukanaisa- adj. ‘Adukanaisha’ , first month, March-April: Elam. ha-du-kan-na-1§, АКК. nisannu: -natsa- on the evidence of the Elam., acc. to MB Or. $96, rather than -nisa- ($117). Cpd. of adu- ^ + kan- ‘dig’, possibly with vriddhi ($126; Adu- ?): "Irrigation-Canal-Cleaning Month’, re- ferring to the cleaning of the underground con- duits for irrigation water, regularly done in the spring (cf. РЕШ. AiW 61). Adukalnaz]Sahya gsm. DB 2.69.
### BRT čiš
30725
```


## [2026-09-14T02:07:08.786Z] TOOL CALL #65: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg457.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/457.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/457.png"
}
```


### [2026-09-14T02:07:08.874Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 79186 Sep 13 22:07 /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/457.png
```


## [2026-09-14T02:07:16.810Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && grep -n -i \"caement\\|caedere\\|Middle English\" 72ab39fedcf61fa1.txt | head -5; wc -c 72ab39fedcf61fa1.txt"
}
```


### [2026-09-14T02:07:16.872Z] TOOL RESULT

```
64: [Middle English, from Old French ciment , from Latin caementum , rough-cut stone, rubble used in making concrete, from caedere , to cut; see ka ə -id- in the Appendix of Indo-European roots.] 
5521 72ab39fedcf61fa1.txt
```


## [2026-09-14T02:15:48.413Z] TOOL CALL #67: Bash

```json
{
 "command": "python3 - <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW_CAEDO=\"https://en.wiktionary.org/wiki/caedo\"\nE_CAESAR=\"https://www.etymonline.com/word/Caesar\"\nW_TSAR=\"https://en.wiktionary.org/wiki/%D1%86%D0%B0%D1%80%D1%8C\"\nW_QAYSAR_AR=\"https://en.wiktionary.org/wiki/%D9%82%D9%8A%D8%B5%D8%B1\"\nW_QEYSAR_FA=\"https://en.wiktionary.org/wiki/%D9%82%DB%8C%D8%B5%D8%B1\"\nW_CAESAR=\"https://en.wiktionary.org/wiki/Caesar\"\nW_JERSEY=\"https://en.wiktionary.org/wiki/Jersey\"\nE_JERSEY=\"https://www.etymonline.com/word/jersey\"\nE_CEMENT=\"https://www.etymonline.com/word/cement\"\nW_SIMAN=\"https://en.wiktionary.org/wiki/%D8%B3%DB%8C%D9%85%D8%A7%D9%86\"\nW_CHALANGAR=\"https://en.wiktionary.org/wiki/%DA%86%D9%84%D9%86%DA%AF%D8%B1\"\nA_CHILAN=\"https://abadis.ir/fatofa/%DA%86%DB%8C%D9%84%D8%A7%D9%86/\"\nA_SEMENT=\"https://abadis.ir/fatofa/%D8%B3%D9%85%D9%86%D8%AA/\"\nA_SEZARIN=\"https://abadis.ir/fatofa/%D8%B3%D8%B2%D8%A7%D8%B1%DB%8C%D9%86/\"\nA_TEZAR=\"https://abadis.ir/fatofa/%D8%AA%D8%B2%D8%A7%D8%B1/\"\nA_ZERSEH=\"https://abadis.ir/fatofa/%DA%98%D8%B1%D8%B3%D9%87/\"\nAHD_CEMENT=\"https://www.ahdictionary.com/word/search.html?q=cement\"\n\nPOK_QUOTE = (\"Pokorny IEW 917 (local POK_full.txt): \\\"Root / lemma: (s)k(h)ai-, (s)k(h)ai-d-, (s)k(h)ai-t- | \"\n \"Meaning: to hit, kick | Material: Latin caedo, -ere ... caedes 'Schlachten, Morden', caementum (*caid-smento-) \"\n \"'Bruchstein', caelum 'chisel' (*caid-slo-), caia (*caidja) f. 'cudgel' ... References: WP. II 538, WH. I 44, 45, \"\n \"129, 130, 131 | Page(s): 917\\\"\")\n\nDKS_QUOTE = (\"Bailey, Dictionary of Khotan Saka p.103 s.v. culonyau (ISS_alt_DKS.txt line 2193): \\\"From *cilauna-, \"\n \"Sogd. Man. cy-dnyh-, Zor.P. (Vid. 8:90) cyl'n-kr *celan-kar 'maker of weapons', to base kai-:ci-, O.Pers. \"\n \"akinakes 'sword', Sogd. kyn'k, with IE Pok. 917 (s)k(h)ai- 'to cut', Lat. caedo, caelum 'chisel'\\\"\")\n\nPHD_QUOTE = (\"MacKenzie, CPD (PHD.txt line 298): \\\"celan [cy'l'n | = M, N ~] dagger. ~gar [-kl, -gl | N ~] swordsmith.\\\"\")\n\nMON_CHILAN = (\"Mo'in, Farhang-e Farsi (MON_part1.txt line 51909): \\\"چیلان ... [چلنگر] (ا.) آلات و ادواتی که از آهن سازند \"\n \"مانند زرفین در و زنجیر و حلقه‌های کوچک و یراق زین و لگام اسب و رکاب\\\"; and line 51164: \\\"چلنگر [= چلینگر، چیلانگر] \"\n \"(ص‌شغل.) آنکه آهن‌آلات خرد از قبیل قفل، کلید، چفت و رزه، زنجیر، انبر، میخ و مانند آنها سازد\\\"\")\n\nBQT1551 = (\"Borhan-e Qate' ed. Mo'in, printed p.1551 = pdf 344 of the vol-3 scan (BQT_v3_pagemap.json maps printed \"\n \"1551 -> pdf 344), entry قیصر, Mo'in's footnotes: \\\"یونانی Kaisar ... و بتوسط آرامیان وارد عربی شده «دائرةالمعارف \"\n \"اسلام: قیصر». لاتینی Caesar ... césar (فر.) ... caesar (انگل.) = Kaiser (آلم.) ... (روسی) czar و tsar\\\"\")\n\nKLN839 = (\"Klein 1966 p.838/839 (KLN_1966.txt leaf 452, whose OCR carries the printed folio '838'), s.v. kaiser: \"\n \"\\\"G. Kaiser, fr. MHG. keiser, fr. OHG. keisar, fr. L. Caesar, whence also OE. casere ... (Goth. kaisar is \"\n \"borrowed fr. Gk. Kaisar, which itself is a loan word fr. L. Caesar). See Caesar and cp. czar\\\"; and s.v. Caesar \"\n \"(p.~228): \\\"Caesar, masc. PN. - L., of uncertain origin. Cp. czar, kaiser.\\\"\")\n\nFSD1317 = (\"Funk & Wagnalls New Standard (FSD_vol2.txt leaf 612, the 'jer-' page = p.1317 of the continuous \"\n \"pagination) s.v. jersey 3: \\\"Fine woolen yarn, or fine combed wool, as spun in Jersey. (< Isle of Jersey, \"\n \"< L. Caesarea, < Caesar.)\\\"\")\n\nNAT166 = (\"Berlitz, Native Tongues (NAT_2005.txt, leaf whose running head reads '166 NATIVE TONGUES'): \\\"New Jersey, \"\n \"the island of Jersey, Jersey cattle, and the type of sweater called a jersey all perpetuate the last name of \"\n \"Julius Caesar. The Latin name of several Roman cities, from which Jersey is derived, was Caesarea, named in \"\n \"honor of the first Caesar.\\\"\")\n\nAHD_WATKINS = (\"Watkins, AHD Indo-European Roots (AHD_watkins1985.txt line 566): \\\"kae-id-. To strike. 1. Latin \"\n \"caedere, to cut, strike: CAESURA, CEMENT, CESTUS2, CHISEL, -CIDE, SCISSORS; ABSCISE, CIRCUMCISE, CONCISE, \"\n \"DECIDE, EXCISE2, INCISE, PRECISE, RECISION. 2. Latin caelum (? < *caedum), sculptor's chisel: CAELUM. \"\n \"[Pok. (s)k(h)ai- 917.]\\\"\")\n\nnodes = []\n\nnodes.append({\n \"id\": 1, \"lang\": \"Old Persian\", \"words\": \"kai, či\",\n \"verdict\": \"plausible\",\n \"derivation\": \"The two forms are not attested Old Persian words: they are Bailey's reconstructed Indo-Iranian/Iranian base, which he writes 'base kai-: ci-' (the ci- variant being the regular Iranian palatalisation of *k before a front vowel, *kai- > *cai- > ci-). Bailey sets this base up in the entry culonyau 'with weapons' (< *cilauna-) and connects it with IE Pok. 917 (s)k(h)ai- 'to cut', Lat. caedo, caelum, which is exactly the arrow Nourai draws. Kent's Old Persian lexicon has no verb kai-/ci- 'to cut' (the only OP kan- is 'to dig'), and the one genuinely Old Persian form Bailey cites in the entry is akinakes 'short sword' — so the box's language label 'Old Persian' is Nourai's own, and should read 'Old Iranian / Indo-Iranian base'. The base itself, and the arrow from the root, are sound.\",\n \"derivation_fa\": \"دو صورت kai و či واژه‌های گواهی‌شدهٔ پارسی باستان نیستند؛ اینها ستاک بازسازی‌شدهٔ ایرانی/هندوایرانی‌اند که بیلی آن را «base kai-: či-» می‌نویسد (گونهٔ či- حاصل کامی‌شدن قاعده‌مند *k ایرانی پیش از واکهٔ پیشین است: *kai- › *čai- › či-). بیلی این ستاک را در مدخل culonyau «با سلاح‌ها» (از *čilauna-) می‌آورد و آن را به ریشهٔ هندواروپایی پوکورنی ۹۱۷ یعنی (s)k(h)ai- «بریدن» و caedō لاتین می‌پیوندد — همان پیکانی که نورایی کشیده است. اما در واژه‌نامهٔ پارسی باستانِ کِنت هیچ فعلی به صورت kai-/či- «بریدن» نیست (تنها kan- «کندن» هست)، پس برچسب «پارسی باستان» از خود نورایی است و درست آن «ایرانی باستان/هندوایرانی» است. ادعای نورایی در اصل پذیرفتنی است، تنها نام زبان نادرست است.\",\n \"sources\": [],\n \"ref_check\": [{\"ref\": \"ISS:84\", \"status\": \"partial\", \"note\": \"Indo-Scythian Studies VI itself is not online; checked in Bailey's own Dictionary of Khotan Saka (1979), which restates the same etymology. \" + DKS_QUOTE + \" — Bailey supports the base and the Pokorny-917 connection, but calls it an Iranian base, not Old Persian.\"}],\n \"consulted\": [\n   {\"src\": \"KNT\", \"where\": \"Kent, Old Persian, Lexicon; grep of KNT.txt\", \"stance\": \"silent\", \"note\": \"No OP entry kai- / ci- 'to cut'. The only kan- in Kent is 'dig' (\\\"OP akaniya 'was dug', Av. kan- 'dig'\\\", KNT.txt line 1265/4983). Kent gives no Old Persian verb for 'cut' at all.\"},\n   {\"src\": \"ISS_alt_DKS\", \"where\": \"DKS p.103 s.v. culonyau\", \"stance\": \"supports\", \"note\": DKS_QUOTE},\n   {\"src\": \"BRT\", \"where\": \"Altiranisches Wörterbuch, grep for kaēš-/čiš- 'schneiden'\", \"stance\": \"silent\", \"note\": \"Bartholomae has no Avestan verb kai-/či- 'to cut'; the Avestan verb for cutting is kart- (AirWb 454 f.).\"}\n ]\n})\n\nnodes.append({\n \"id\": 2, \"lang\": \"Pahlavi\", \"words\": \"čělân; čělânkar\",\n \"verdict\": \"plausible\",\n \"derivation\": \"Both forms are genuine Middle Persian. MacKenzie's Concise Pahlavi Dictionary has čēlān (Book Pahlavi cy'l'n) 'dagger' and čēlāngar 'swordsmith', noting the words survive into New Persian; Bailey reads the Vīdēvdād 8:90 spelling cyl'n-kr as *čēlān-kar 'maker of weapons' and derives čēlān from Old Iranian *čilauna- (whence also Khotanese cūlona- 'weapon' and Sogdian Man. cyδnyh-), from the base kai-/či- 'to cut' = PIE *(s)k(h)ai-. The suffix -kar/-gar is the ordinary MP agent suffix (< OIr. *-kara- 'maker'). Nourai's forms are right; his glosses are a widening: čēlān is 'dagger/weapon' in both MacKenzie and Bailey, not 'metal objects' in general — the broader 'small ironmongery' sense is only the later New Persian one (node #3).\",\n \"derivation_fa\": \"هر دو صورت پهلوی اصیل‌اند: مکنزی در فرهنگ کوچک پهلوی čēlān (پهلوی کتابی cy'l'n) را «خنجر» و čēlāngar را «شمشیرساز» آورده و یادآور شده که هر دو در فارسی نو نیز مانده‌اند؛ بیلی هم املای cyl'n-kr در وندیداد ۸:۹۰ را *čēlān-kar «سازندهٔ سلاح» می‌خواند و čēlān را از ایرانی باستان *čilauna- می‌گیرد (هم‌ریشه با cūlona- ختنی و čyδnyh- سغدی مانوی) که خود از ستاک kai-/či- «بریدن» یعنی همان ریشهٔ هندواروپایی *(s)k(h)ai- است. پسوند -kar/-gar همان پسوند فاعلی رایج فارسی میانه (از *-kara-) است. صورت‌های نورایی درست‌اند، اما معنایی که داده کلی‌تر از منابع است: در مکنزی و بیلی čēlān «خنجر/سلاح» است نه «اشیای فلزی»؛ معنای گستردهٔ «آهن‌آلات خرد» تنها در فارسی نو پیدا شده است.\",\n \"sources\": [W_CHALANGAR],\n \"ref_check\": [{\"ref\": \"ISS:84\", \"status\": \"supports\", \"note\": \"Checked in Bailey's DKS (substitute for Khotanese Texts VI). \" + DKS_QUOTE + \" — the Pahlavi word, its Sogdian and Khotanese cognates and the Pokorny 917 root are all there, as Nourai's arrow claims; only the gloss is 'maker of weapons', not 'metal worker'.\"}],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"MacKenzie, CPD p.23 s.v. čēlān\", \"stance\": \"partial\", \"note\": PHD_QUOTE + \" — form confirmed, gloss is 'dagger' / 'swordsmith', narrower than Nourai's 'metal objects' / 'metal worker'.\"},\n   {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II (glossary), grep for cylan/čēlān\", \"stance\": \"silent\", \"note\": \"Nyberg's glossary covers only the texts he edits; čēlān does not occur in it.\"},\n   {\"src\": \"ISS_alt_DKS\", \"where\": \"DKS p.103\", \"stance\": \"supports\", \"note\": \"\\\"Zor.P. (Vid. 8:90) cyl'n-kr *celan-kar 'maker of weapons'\\\" — the Pahlavi attestation Nourai's node rests on.\"}\n ]\n})\n\nnodes.append({\n \"id\": 3, \"lang\": \"Persian\", \"words\": \"čîlân «چیلان»; čîlângar «چیلانگر»\",\n \"verdict\": \"transcription_suspect\",\n \"error_in\": \"extraction\",\n \"book_prints\": \"چیلنگر ( چلنگر )\",\n \"correct_form\": \"چیلنگر\",\n \"derivation\": \"The etymology itself is confirmed: NP چیلان čīlān 'small ironware — door-rings, chains, little rings, the metal fittings of saddle and bridle, stirrups' and چیلنگر/چلنگر čīlangar ~ čalangar 'maker of small iron objects: locks, keys, latches, chains, pincers, nails' continue Middle Persian čēlān, čēlāngar directly (MP ē > NP ī; the agent suffix -gar is unchanged; the shortened variant چلنگر arises by the normal reduction of unstressed ī in a four-syllable word). Mo'in gives exactly these glosses, Dehkhoda quotes them from Borhan, and Wiktionary derives چلنگر 'From Middle Persian cyl'ngl /čēlāngar/, equivalent to چیلان (čilân, \\\"iron chain, lock, ring\\\") + ـگر'. The flag is a DATA problem, not an etymological one: the printed page (pdf 457, book p.427) shows the Persian script as «چیلنگر ( چلنگر )», but data/extracted/batch/page-457.json has script \\\"چیلانگر\\\". چیلانگر is a real variant (Mo'in lists چلنگر [= چلینگر، چیلانگر]), but it is not what this page prints.\",\n \"derivation_fa\": \"ریشه‌شناسی این گره درست است: «چیلان» در فارسی نو به معنی آهن‌آلات خرد (زرفین در، زنجیر، حلقه‌های کوچک، یراق زین و لگام و رکاب) و «چیلنگر/چلنگر» به معنی سازندهٔ قفل و کلید و چفت و زنجیر و انبر و میخ، مستقیماً دنبالهٔ čēlān و čēlāngar فارسی میانه‌اند: ēِ فارسی میانه در فارسی نو به ī بدل شده و پسوند -گر بی‌تغییر مانده است؛ گونهٔ کوتاه‌شدهٔ «چلنگر» نیز از افتادن ī بی‌تکیه در واژهٔ چهارهجایی پدید آمده است. معین همین معناها را آورده، دهخدا آن را از برهان نقل کرده و ویکی‌واژه نیز «چلنگر» را از cyl'ngl فارسی میانه و برابر «چیلان + ـگر» می‌داند. اما اینجا یک خطای خوانش اسکن هست: صفحهٔ چاپی «چیلنگر ( چلنگر )» دارد، حال آنکه در فایل استخراج‌شده «چیلانگر» آمده است (هرچند «چیلانگر» خود گونه‌ای است که معین ذیل «چلنگر» یاد کرده).\",\n \"sources\": [W_CHALANGAR, A_CHILAN],\n \"ref_check\": [{\"ref\": \"MON:1327\", \"status\": \"supports\", \"note\": MON_CHILAN + \" — both headwords and both of Nourai's glosses come straight from Mo'in. (The disk copy of Mo'in, MON_part1.txt, carries no page numbers, so p.1327 itself could not be confirmed; the alphabetical position of چیلان in vol. 1 is consistent with it.)\"}],\n \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"Farhang-e Farsi s.vv. چیلان, چلنگر (MON_part1.txt lines 51909, 51164)\", \"stance\": \"supports\", \"note\": MON_CHILAN},\n   {\"src\": \"BQT\", \"where\": \"Borhan-e Qate' s.v. چیلان, quoted by Dehkhoda\", \"stance\": \"supports\", \"note\": \"Dehkhoda (abadis.ir/fatofa/چیلان): \\\"چیلان. (اِ) آلات و ادواتی که از آهن سازند مانند زرفین در و زنجیر و حلقه‌های کوچک و یراق زین و لگام اسب و رکاب. (برهان) (از آنندراج)\\\" — the iron-ware sense is Borhan's; a homonym چیلان 'jujube' (BQT_v2_pages.txt line 7900) is a different word.\"},\n   {\"src\": \"HRN\", \"where\": \"Horn, Grundriss, grep for calangar / Schlosser\", \"stance\": \"silent\", \"note\": \"Horn has no entry for چلنگر.\"},\n   {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien, grep for calangar / Schlosser\", \"stance\": \"silent\", \"note\": \"Not treated.\"},\n   {\"src\": \"ARY\", \"where\": \"Aryanpur, Farhang-e rishe-ha-ye hend-o-orupayi (incoming/ARY/ARY_pages.txt)\", \"stance\": \"silent\", \"note\": \"grep for چلنگ/چیلا returns nothing (the OCR of this scan is poor); no independent confirmation from Aryanpur.\"}\n ]\n})\n\nnodes.append({\n \"id\": 4, \"lang\": \"Latin\", \"words\": \"caedere; â caesô mâtris ŭterě; caementum; caelum\",\n \"verdict\": \"transcription_suspect\",\n \"error_in\": \"book\",\n \"book_prints\": \"â caesô mâtris ŭterě\",\n \"correct_form\": \"ā caesō mātris uterō\",\n \"derivation\": \"caedere 'to fell, cut, strike' (perf. cecīdī, supine caesum) < Proto-Italic *kaidō < PIE *kh₂eyd-/*keh₂id- 'to strike, hew' (de Vaan 79-80) — the root box, confirmed. caementum 'stone chips, rubble struck off in quarrying' is caed- + the instrument suffix -mentum, with the regular Latin loss of -d- before -sm- (*caid-smentom > caementum); caelum 'chisel, burin' is likewise *caid-slo- > caelum. All three are Pokorny's own material for p.917. The flag is the Latin tag-phrase: the book prints 'â caesô mâtris ŭterě', which is not Latin — the ablative of uterus is uterō, and the classical phrase (Pliny, NH 7.47) is 'a caeso matris utero'. Page 457 of the PDF (book p.427) shows 'ŭterě' with the breve, so the extraction is faithful and the mistake is Nourai's own (a misreading of the -o as -e, plus stray quantity marks). The note attached to it — that Julius Caesar or an ancestor was born by that operation — is the ancient folk etymology of the cognomen and is not accepted today (see node #5).\",\n \"derivation_fa\": \"فعل caedere «بریدن، زدن، افکندن» (ماضی cecīdī، سوپینِ caesum) از ایتالیایی آغازین *kaidō و آن از هندواروپایی آغازین *kh₂eyd-/*keh₂id- «زدن، تراشیدن» است (دِ ڤان، صص ۷۹–۸۰). واژهٔ caementum «خرده‌سنگِ تراشیده» از همان ستاک با پسوند ابزاری -mentum ساخته شده و افتادن d پیش از خوشهٔ -sm- قاعده‌مند است (*caid-smentom › caementum)؛ caelum «قلم حکاکی» نیز از *caid-slo- است. هر سه در خودِ صفحهٔ ۹۱۷ پوکورنی آمده‌اند. اشکال در عبارت لاتینی است: کتاب «â caesô mâtris ŭterě» چاپ کرده که لاتین درست نیست؛ حالت ازی uterus می‌شود uterō و عبارت کلاسیک (پلینیوس، تاریخ طبیعی ۷:۴۷) «a caeso matris utero» است. تصویر صفحهٔ ۴۲۷ کتاب همان «ŭterě» را نشان می‌دهد، پس خطا از خودِ کتاب است نه از خوانش اسکن. یادداشت پیوستِ آن — اینکه یولیوس سزار یا نیایش با این عمل به دنیا آمده — ریشه‌شناسی عامیانهٔ رومی است و پژوهش امروزی آن را نمی‌پذیرد (نگاه کنید به گره ۵).\",\n \"sources\": [W_CAEDO, E_CEMENT, AHD_CEMENT],\n \"ref_check\": [\n   {\"ref\": \"POK:917\", \"status\": \"supports\", \"note\": POK_QUOTE + \" — caedo, caementum and caelum 'chisel' are Pokorny's own examples on the cited page.\"},\n   {\"ref\": \"AHD:186,217\", \"status\": \"partial\", \"note\": \"The 1975 New College Edition's main dictionary is not on disk (pp. 186 and 217 would be the 'Caesar' and 'cement' pages, consistent with its alphabetical layout). Its IE-root appendix, which is on disk, has \" + AHD_WATKINS + \". The current online AHD s.v. cement gives '[Middle English, from Old French ciment, from Latin caementum, rough-cut stone, rubble used in making concrete, from caedere, to cut; see kaə-id- in the Appendix]'.\"},\n   {\"ref\": \"ISS:84\", \"status\": \"supports\", \"note\": \"Bailey (DKS p.103) cites 'Lat. caedo, caelum \\\"chisel\\\"' under Pok. 917, exactly this node's Latin material.\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"IEW 917\", \"stance\": \"supports\", \"note\": POK_QUOTE},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. kae-id-\", \"stance\": \"supports\", \"note\": AHD_WATKINS},\n   {\"src\": \"WLD\", \"where\": \"Walde-Pokorny II 538\", \"stance\": \"supports\", \"note\": \"Cited both by Pokorny ('References: WP. II 538') and by Buck (SYN.txt line 8060: \\\"Skt. khid- 'tear, press' ... perh.; Lat. caedere 'cut, beat, strike down'. Walde-P. 2.538.\\\"). Bände I-II are not open online, so the page was reached through these two citations.\"},\n   {\"src\": \"SYN\", \"where\": \"Buck 9.22 'cut' and 9.21 'strike'\", \"stance\": \"supports\", \"note\": \"SYN.txt line 14051: \\\"Lat. caedere 'strike, cut' (9.21)\\\"; line 14145: \\\"OFr. cisoires fr. VLat. *caesorium, *cisorium, fr. caedere 'cut down, strike' (9.21)\\\".\"},\n   {\"src\": \"IEC\", \"where\": \"Mann, IECD col. ~470 s.v. kai-\", \"stance\": \"partial\", \"note\": \"IEC.txt line 6597: \\\"kai-, modal fragment: 'alone, separate...' ... Gk. kaí and Lat. cf. caedo, ere, v. cut, lit. 'separate'?\\\" — Mann attaches caedō, with a query, to a quite different kai-; he does not follow Pokorny 917 here.\"}\n ]\n})\n\nnodes.append({\n \"id\": 5, \"lang\": \"Greek\", \"words\": \"kaisar\",\n \"verdict\": \"disputed\",\n \"derivation\": \"The borrowing itself is certain and in the right direction: Greek Καῖσαρ is the Latin cognomen Caesar taken over unchanged (Latin ae rendered by Greek αι), current from the Julio-Claudians onward and standard in the Greek New Testament (Mt 22:21). What modern scholarship rejects is the reason Nourai draws the arrow — that Caesar means 'born by caesarean section', from caesus, past participle of caedere. Klein, on the very page Nourai cites, writes 'Caesar, masc. PN. — L., of uncertain origin'; Etymonline notes that Pliny derived it from caesaries 'head of hair', the Century Dictionary from caesius 'blue-grey (eyes)', and that the birth story cannot apply to Julius Caesar himself, since his mother Aurelia outlived him and such an operation was fatal to the mother in antiquity ('if this is the etymology of the name, it was likely an ancestor who was so born'). So the Greek word is rightly derived from Latin Caesar, but the step caedere > Caesar that this arrow encodes is an ancient folk etymology, not a modern one.\",\n \"derivation_fa\": \"خودِ وام‌گیری قطعی و در جهت درست است: Καῖσαρ یونانی همان لقبِ لاتینی Caesar است که بی‌تغییر گرفته شده (ae لاتین با αι یونانی نشان داده شده)، از دورهٔ خاندان یولیوس-کلاودیوس رایج بوده و در عهد جدید یونانی (متی ۲۲:۲۱) به کار رفته است. آنچه پژوهش امروزی رد می‌کند دلیلِ این پیکان است، یعنی اینکه Caesar از caesus (اسم مفعول caedere) و به معنی «زادهٔ شکم‌شکافته» باشد. کلاین در همان صفحه‌ای که نورایی ارجاع داده می‌نویسد: «Caesar، نام خاص مذکر — لاتینی، با خاستگاه نامعلوم». اتیمآنلاین نیز یادآور می‌شود که پلینیوس آن را از caesaries «گیسو» و فرهنگ سنچری از caesius «چشم‌کبود» گرفته‌اند و داستان زایمان دربارهٔ خودِ یولیوس سزار نمی‌تواند درست باشد، چون مادرش آورلیا پس از او هم زنده بود و چنین عملی در دوران باستان به مرگ مادر می‌انجامید. پس: واژهٔ یونانی به‌درستی از Caesar لاتین است، ولی گامِ caedere › Caesar که این پیکان بر آن استوار است ریشه‌شناسی عامیانهٔ رومی است و امروزه پذیرفته نیست.\",\n \"sources\": [E_CAESAR, W_CAESAR],\n \"ref_check\": [\n   {\"ref\": \"KLN:839\", \"status\": \"partial\", \"note\": KLN839 + \" — Klein supports Latin > Greek Kaisar, but explicitly calls Caesar 'of uncertain origin', i.e. he does NOT derive it from caedere as this arrow does.\"},\n   {\"ref\": \"AHD\", \"status\": \"not_found\", \"note\": \"Watkins's kae-id- entry (AHD_watkins1985.txt line 566) lists CAESURA, CEMENT, CHISEL, SCISSORS etc. but does NOT list CAESAR among the descendants of the root — the appendix does not support this arrow.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"1966 ed. p.839 s.v. kaiser; p.~228 s.v. Caesar\", \"stance\": \"contradicts\", \"note\": KLN839},\n   {\"src\": \"WEB\", \"where\": \"Webster's New Twentieth Century, 2nd ed., s.v. Caesarean section\", \"stance\": \"partial\", \"note\": \"WEB vol.1 line 26062: \\\"Caesarean section or operation; a surgical operation for delivering a baby by cutting through the mother's abdominal and uterine walls: so called because Julius Caesar was supposedly born in this manner.\\\" — Webster reports the legend with 'supposedly'.\"},\n   {\"src\": \"BQT\", \"where\": \"Borhan-e Qate' p.1551, Mo'in's footnote on قیصر\", \"stance\": \"supports\", \"note\": BQT1551 + \" — Mo'in repeats the Greek-to-Arabic route; the birth story is told in Borhan s.v. اغسطوس (vol. 1): \\\"او را ازآن جهت قیصر گفتند که مادرش بوقت ولادت بمرد و شکمش را بشکافتند و او را برآوردند و بزبان رومی اینچنین شخصی را قیصر خوانند\\\".\"}\n ]\n})\n\nnodes.append({\n \"id\": 6, \"lang\": \"Arabic\", \"words\": \"qaysar\",\n \"verdict\": \"plausible\",\n \"derivation\": \"Arabic قَيْصَر qayṣar 'the Roman/Byzantine emperor' is indeed the Latin Caesar as transmitted through the Hellenistic Near East, and it is pre-Islamic in Arabic (it is the standing title of the Byzantine emperor in the sīra and hadith, beside kisrā for the Persian king). But the immediate donor was most probably Aramaic/Syriac qēsar rather than Greek directly: the Arabic ṣād reproduces the emphatic Aramaic s, which is exactly how Aramaic renders Greek σ in this word. Wiktionary: 'From Latin Caesar, possibly through Ancient Greek Καῖσαρ and/or Aramaic קיסר (qēsar)'. Mo'in, in the footnote on the very Borhan page Nourai cites, says the same: 'Kaisar, Greek, and it entered Arabic through the Aramaeans'. So the word and the ultimate source are right; the chart's direct Greek > Arabic arrow skips the Aramaic link that Nourai's own reference names.\",\n \"derivation_fa\": \"«قَیْصَر» عربی، لقب امپراتور روم/بیزانس، در اصل همان Caesar لاتینی است که از راه خاور نزدیک هلنی‌مآب به عربی رسیده و پیش از اسلام نیز در عربی رایج بوده است (در سیره و حدیث در کنار «کسری» برای شاه ایران). با این حال زبان واسط به احتمال زیاد آرامی/سریانی qēsar بوده است نه مستقیماً یونانی: «ص» عربی بازتاب سِ مُفَخّمِ آرامی است، یعنی همان شیوه‌ای که آرامی σ یونانی را در این واژه می‌نویسد. ویکی‌واژه می‌گوید: «از لاتینی Caesar، احتمالاً از راه Καῖσαρ یونانی و/یا קיסר آرامی». معین نیز در حاشیهٔ همان صفحهٔ برهان که نورایی ارجاع داده می‌نویسد: «Kaisar یونانی و بتوسط آرامیان وارد عربی شده». پس واژه و خاستگاه نهایی درست است، اما پیکانِ مستقیم «یونانی ← عربی» حلقهٔ آرامی را که خودِ مرجع نورایی نام برده حذف کرده است.\",\n \"sources\": [W_QAYSAR_AR],\n \"ref_check\": [{\"ref\": \"BQT:1551\", \"status\": \"partial\", \"note\": BQT1551 + \" — supports Greek Kaisar as the source, but adds 'و بتوسط آرامیان وارد عربی شده' (it entered Arabic through the Aramaeans), a step the chart omits.\"}],\n \"consulted\": [\n   {\"src\": \"BQT\", \"where\": \"Borhan-e Qate' ed. Mo'in, p.1551 footnote 4 (vol-3 scan pdf p.344)\", \"stance\": \"partial\", \"note\": BQT1551},\n   {\"src\": \"KLN\", \"where\": \"Klein 1966 p.839 s.v. kaiser\", \"stance\": \"supports\", \"note\": \"\\\"Gk. Kaisar, which itself is a loan word fr. L. Caesar\\\" — the Greek intermediary Nourai uses for the Arabic is Klein's too.\"},\n   {\"src\": \"FVQ\", \"where\": \"Jeffery, Foreign Vocabulary of the Qur'an, grep for Caesar/qaisar\", \"stance\": \"silent\", \"note\": \"qayṣar does not occur in the Qur'an, so Jeffery has no entry; the only hit (FVQ.txt line 14045) is an aside that 'Chosroes and Caesar were titles of the kings'.\"},\n   {\"src\": \"AFM\", \"where\": \"Addi Shir, al-Alfaz al-farisiyya al-mu'arraba, grep قيصر\", \"stance\": \"silent\", \"note\": \"No entry: Addi Shir collects Persian words arabised, and qayṣar is not one of them.\"}\n ]\n})\n\nnodes.append({\n \"id\": 7, \"lang\": \"Persian\", \"words\": \"qeysar «قیصر»\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"NP قیصر qeysar 'the Roman/Byzantine emperor' is a straight loan from Arabic qayṣar (Wiktionary: 'Borrowed from Arabic قَيْصَر'), the Arabic diphthong ay being read /ey/ in modern Persian; it is already the normal Persian word in the Shahname, as the verse printed in the box ('به قیصر سپارد همه یک به یک ...') shows, where قیصر is Rome/Byzantium as against خاقان for China and کسری for Iran. The plural قیاصره is likewise taken over from Arabic. So Arabic > Persian is correct and uncontroversial.\",\n \"derivation_fa\": \"«قیصر» فارسی، لقب امپراتور روم و بیزانس، وام‌واژه‌ای است مستقیم از عربی qayṣar (ویکی‌واژه: «از عربی قَیْصَر وام گرفته شده»)؛ مصوت مرکب ay عربی در فارسی امروز /ey/ خوانده می‌شود. این واژه از همان دورهٔ شاهنامه در فارسی جا افتاده بود، چنان‌که بیتِ چاپ‌شده در همین جدول («به قیصر سپارد همه یک به یک...») نشان می‌دهد و در آن «قیصر» در برابر «خاقان» چین و «کسری» ایران به کار رفته است. جمع مکسر «قیاصره» نیز از عربی گرفته شده است. بنابراین پیکان «عربی ← فارسی» درست و بی‌مناقشه است.\",\n \"sources\": [W_QEYSAR_FA],\n \"ref_check\": [{\"ref\": \"BQT:217\", \"status\": \"not_found\", \"note\": \"Printed p.217 of Borhan vol. 1 falls in the letter ب (the leaf that would carry it is in the باد.../بار... stretch, BQT_v1_pages.txt leaf ~437), so it cannot be the قیصر entry. Mo'in's actual treatment of قیصر is on p.1551 (the page Nourai cites for the neighbouring nodes), and the caesarean story is told s.v. اغسطوس in vol. 1 (leaf 360): 'او را ازآن جهت قیصر گفتند که مادرش بوقت ولادت بمرد و شکمش را بشکافتند...'. The claim is documented in Borhan, but not at the page cited.\"}],\n \"consulted\": [\n   {\"src\": \"BQT\", \"where\": \"Borhan-e Qate' p.1551 s.v. قیصر (vol-3 scan pdf 344)\", \"stance\": \"supports\", \"note\": \"The Borhan entry itself: \\\"قیصر، با صاد بی‌نقطه بروزن حیدر، رومی فرزندی باشد که مادرش پیش از آنکه او را بزاید بمیرد و شکم مادر را بشکافند و آن فرزند را بیرون آورند\\\", with Mo'in's footnote \" + BQT1551},\n   {\"src\": \"MON\", \"where\": \"Mo'in, Farhang-e Farsi (MON_part2.txt line 16489)\", \"stance\": \"supports\", \"note\": \"\\\"امپراتوران روسیه، تزار؛ ج. قیاصر\\\" — Mo'in treats قیصر as the Arabic-plural-taking loan and links it to تزار.\"}\n ]\n})\n\nnodes.append({\n \"id\": 8, \"lang\": \"French\", \"words\": \"\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Empty pass-through node standing for French César (also the adjective césarienne in 'opération césarienne'), the learned French form of Latin Caesar, with Latin ae > French é and the -ar kept in the Latinate spelling. Mo'in names it explicitly in the Borhan footnote Nourai cites here: 'césar (فر.)'. It is the correct intermediary for the Persian سزار/سزارین of node #9.\",\n \"derivation_fa\": \"این جعبهٔ خالی نمایندهٔ صورت فرانسویِ César (و صفت césarienne در «opération césarienne») است؛ صورتی عالمانه از Caesar لاتین که در آن ae لاتین به é فرانسوی بدل شده و پایانهٔ -ar در املای لاتینی‌مآب مانده است. معین در همان حاشیهٔ برهان که نورایی به آن ارجاع داده به‌روشنی «césar (فر.)» را نام می‌برد. این گره واسطهٔ درستِ «سزار/سزارین» فارسی در گرهِ ۹ است.\",\n \"sources\": [],\n \"ref_check\": [{\"ref\": \"BQT:1551\", \"status\": \"supports\", \"note\": BQT1551 + \" — the footnote lists 'césar (فر.)' among the modern reflexes of Latin Caesar, which is what this empty French box stands for.\"}],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein 1966 p.839 s.v. kaiser / p.~228 s.v. Caesar\", \"stance\": \"supports\", \"note\": \"Klein treats the modern European forms (G. Kaiser, Russ. tsar, F. César) as continuations of L. Caesar.\"},\n   {\"src\": \"BQT\", \"where\": \"Borhan p.1551 footnote\", \"stance\": \"supports\", \"note\": \"'césar (فر.)' printed in Mo'in's list of the word's European descendants.\"}\n ]\n})\n\nnodes.append({\n \"id\": 9, \"lang\": \"Persian\", \"words\": \"sezâr «سزار»\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"NP سزار sezâr 'Caesar' (in practice almost always in ژول سزار 'Jules César') and the derivative سزارین sezâriyan 'caesarean section' are 20th-century borrowings from French César / (opération) césarienne, not from Latin or Arabic: the vowel of the first syllable (se-, not qey-) and the -ien ending of سزارین are French, and Mo'in tags سزارین '[فر.]' — French — and explains it as named after 'ژول سزار قیصر روم' who was said to have been born that way. Persian thus has a doublet: the old Arabic-mediated قیصر (node #7) and the modern French-mediated سزار.\",\n \"derivation_fa\": \"«سزار» در فارسی (که عملاً همیشه در ترکیب «ژول سزار» می‌آید) و مشتق آن «سزارین» وام‌واژه‌های سدهٔ بیستم از فرانسویِ César و (opération) césarienne‌اند، نه از لاتین و نه از عربی: واکهٔ هجای نخست (se- نه qey-) و پایانهٔ -ien در «سزارین» فرانسوی‌اند و معین خودِ «سزارین» را با نشانِ «[فر.]» آورده و توضیح داده که نام آن از «ژول سزار قیصر روم» گرفته شده که گویند بدین شیوه زاده شد. پس فارسی در اینجا دو صورتِ دوگانه (doublet) دارد: «قیصر» کهنِ عربی‌واسطه (گرهِ ۷) و «سزار» نوِ فرانسوی‌واسطه.\",\n \"sources\": [A_SEZARIN],\n \"ref_check\": [{\"ref\": \"BQT\", \"status\": \"partial\", \"note\": \"Cited without a page. Mo'in's Borhan footnote at p.1551 does list 'césar (فر.)' as a reflex of Caesar, which covers the French source, but Borhan (a 17th-century dictionary) naturally has no entry for the modern loan سزار/سزارین.\"}],\n \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"Mo'in, Farhang-e Farsi s.v. سزارین (via abadis.ir)\", \"stance\": \"supports\", \"note\": \"\\\"(س یَ) [ فر. ] (اِ.) عمل جراحی جهت خروج نوزاد از شکم و زایمان‌های غیرطبیعی. ژول سزار قیصر روم به این طریق به دنیا آمده و نام این عمل از نام او گرفته شده است.\\\" — Mo'in's own tag is [فر.], French.\"},\n   {\"src\": \"BQT\", \"where\": \"Borhan p.1551 footnote\", \"stance\": \"partial\", \"note\": \"'césar (فر.)' is listed, but the Persian loan itself is post-Borhan.\"}\n ]\n})\n\nnodes.append({\n \"id\": 10, \"lang\": \"English\", \"words\": \"Caesar\",\n \"verdict\": \"plausible\",\n \"derivation\": \"English Caesar 'emperor, ruler' is attested from the late 14th century as cesar. The native Old English form was cāsere (from the same Latin name, borrowed in the Germanic period), which was displaced in Middle English by keiser (c.1200, from Norse or Low German) and then by 'the French or Latin form of the name' (Etymonline). So Nourai's French parent is one of the two possible routes for the 14c. form but not the only one, and Klein — the reference cited here — derives English Caesar straight from Latin ('Caesar, masc. PN. — L., of uncertain origin'). Plausible rather than confirmed: the word is certainly the Latin cognomen, the French mediation is optional.\",\n \"derivation_fa\": \"واژهٔ Caesar در انگلیسی از اواخر سدهٔ چهاردهم به صورت cesar گواهی شده است. صورت بومی انگلیسی کهن cāsere بود (وام‌گیری از همان نام لاتینی در دورهٔ ژرمنی) که در انگلیسی میانه نخست جای خود را به keiser (حدود ۱۲۰۰ م.، از اسکاندیناویایی یا آلمانی سفلی) و سپس به «صورت فرانسوی یا لاتینیِ نام» داد (اتیمآنلاین). پس والدِ فرانسویِ نورایی یکی از دو راه ممکن برای صورت سدهٔ چهاردهمی است، نه تنها راه؛ و کلاین — همان مرجعی که اینجا آمده — Caesar انگلیسی را یکسره از لاتین می‌گیرد. بنابراین ادعا «با احتیاط پذیرفتنی» است: خودِ واژه بی‌گمان همان لقب لاتینی است، اما واسطهٔ فرانسوی الزامی نیست.\",\n \"sources\": [E_CAESAR],\n \"ref_check\": [{\"ref\": \"KLN:839\", \"status\": \"partial\", \"note\": KLN839 + \" — Klein's cross-reference network (Caesar / kaiser / czar) is on this page, but he gives the English word directly from Latin, with no French step.\"}],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein 1966 s.v. Caesar and kaiser (pp. ~228, 839)\", \"stance\": \"partial\", \"note\": \"\\\"Caesar, masc. PN. — L., of uncertain origin. Cp. czar, kaiser.\\\"\"},\n   {\"src\": \"WEB\", \"where\": \"Webster's New Twentieth Century, 2nd ed. s.v. Caesarean\", \"stance\": \"supports\", \"note\": \"WEB vol.1 line 26062, the Caesarean-section entry, treats the word as the Latin name.\"}\n ]\n})\n\nnodes.append({\n \"id\": 11, \"lang\": \"Russian\", \"words\": \"tsar\",\n \"verdict\": \"plausible\",\n \"derivation\": \"Russian царь carʹ is ultimately Latin Caesar, but not directly: it is inherited from Old East Slavic цьсарь cĭsarĭ < цѣсарь cěsarĭ < Proto-Slavic *cěsařь, which was borrowed from a Germanic language — Gothic 𐌺𐌰𐌹𐍃𐌰𐍂 kaisar (itself from Greek/Latin) — in the 4th-6th centuries; the long form cěsarĭ was then contracted to carĭ in Russian, and Ivan IV took it as an imperial title at his coronation in 1547. Klein sets out the same chain: 'Russ. tsar, fr. earlier tsesar', fr. OSlav. cesari, fr. Goth. kaisar ... fr. L. Caesar'. Nourai's single Latin > Russian arrow is therefore right in substance but collapses the Gothic and Proto-Slavic links; Mo'in's footnote at BQT 1551 likewise just lists '(روسی) czar و tsar' among the descendants of Caesar.\",\n \"derivation_fa\": \"«تزار» روسی (царь) سرانجام به Caesar لاتین می‌رسد، اما نه بی‌واسطه: این واژه از روسی شرقی کهن цьсарь و آن از цѣсарь و از اسلاوی آغازین *cěsařь است که خود در سده‌های چهارم تا ششم میلادی از زبانی ژرمنی — گوتیِ kaisar (که آن هم از یونانی/لاتین است) — وام گرفته شده؛ سپس صورت بلندِ cěsarĭ در روسی به carĭ کوتاه شده و ایوان چهارم در تاج‌گذاری ۱۵۴۷ آن را لقب امپراتوری قرار داد. کلاین همین زنجیره را می‌آورد: «روسی tsar از tsesar' کهن‌تر، از cesari اسلاوی کهن، از kaisar گوتی ... از Caesar لاتین». پس پیکان یکپارچهٔ «لاتین ← روسی» در نورایی از نظر محتوا درست است ولی حلقه‌های گوتی و اسلاوی آغازین را حذف کرده است؛ حاشیهٔ معین در برهان ص ۱۵۵۱ هم تنها «(روسی) czar و tsar» را در فهرست بازماندگان Caesar یاد می‌کند.\",\n \"sources\": [W_TSAR, E_CAESAR],\n \"ref_check\": [{\"ref\": \"BQT:1551\", \"status\": \"supports\", \"note\": BQT1551 + \" — '(روسی) czar و tsar' are listed there as reflexes of Caesar, which is what Nourai's node claims.\"}],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein 1966 p.~? s.v. czar (KLN_1966.txt line 10154)\", \"stance\": \"partial\", \"note\": \"\\\"czar, tsar, n. — Russ. tsar, fr. earlier tsesar', fr. OSlav. cesari, fr. Goth. kaisar ... 'emperor', fr. L. Caesar, title adopted by Augustus and the succeeding Roman emperors\\\" — the Gothic and Old Slavonic links that the chart omits.\"},\n   {\"src\": \"LKT\", \"where\": \"Lokotsch, Etymologisches Wörterbuch, grep for Zar/Kaisar\", \"stance\": \"silent\", \"note\": \"Lokotsch covers only words of Oriental (Arabic/Persian/Turkish) origin, so царь is outside his scope.\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etym. Dict. (SKT.txt line 23469)\", \"stance\": \"supports\", \"note\": \"Skeat's word-list classes 'czar' under 'Russian from Latin'.\"}\n ]\n})\n\nnodes.append({\n \"id\": 12, \"lang\": \"French\", \"words\": \"\",\n \"verdict\": \"plausible\",\n \"derivation\": \"Empty pass-through node for French tsar/czar, borrowed from Russian; French adopted the tsar spelling only during the 19th century (OED, quoted by Etymonline: 'French adopted tsar during the 19th c.'). As an intermediary it is chronologically possible for the Persian تزار of node #13, since Persian took the word in the late Qajar period when French was the channel for European vocabulary — but Persian could equally have taken it straight from Russian, and Mo'in in fact tags تزار '[روس.]' (see node #13).\",\n \"derivation_fa\": \"این جعبهٔ خالی نمایندهٔ صورت فرانسویِ tsar/czar است که از روسی وام گرفته شده؛ املای tsar در فرانسه تنها در سدهٔ نوزدهم رواج یافت (به نقل اتیمآنلاین از فرهنگ آکسفورد: «فرانسه در سدهٔ نوزدهم tsar را پذیرفت»). چنین واسطه‌ای از نظر زمانی برای «تزار» فارسیِ گرهِ ۱۳ ممکن است، چون فارسی این واژه را در اواخر دورهٔ قاجار و در روزگاری گرفت که فرانسه مجرای واژگان اروپایی بود؛ اما فارسی می‌توانست آن را یکسره از روسی هم بگیرد و معین خود «تزار» را با نشان «[روس.]» آورده است (نگاه کنید به گرهِ ۱۳).\",\n \"sources\": [E_CAESAR],\n \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"The node carries no reference in the book.\"}],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein 1966 s.v. czar\", \"stance\": \"partial\", \"note\": \"Klein gives the Russian source of the Western forms but does not discuss the French spelling history.\"},\n   {\"src\": \"MON\", \"where\": \"Mo'in s.v. تزار (via abadis.ir)\", \"stance\": \"contradicts\", \"note\": \"\\\"(تِ) [ روس. ] (اِ.) عنوان پادشاهان گذشته روسیه، قیصر.\\\" — Mo'in marks the Persian word as taken from Russian, not French.\"}\n ]\n})\n\nnodes.append({\n \"id\": 13, \"lang\": \"Persian\", \"words\": \"tezâr «تزار»\",\n \"verdict\": \"plausible\",\n \"derivation\": \"NP تزار tezâr 'Russian emperor' is certainly the same word, ultimately Latin Caesar via Russian царь; Dehkhoda states it plainly: 'تزار. تسار. کلمه روسی مشتق از سزار لاتینی. عنوان امپراتوران روسیه'. The doubtful link is the immediate donor. Mo'in tags the entry '[روس.]' — Russian — against Nourai's Russian > French > Persian route; the Persian initial t- and the final -âr fit either tsar (French) or царь (Russian), and Persian contact with Russia in the 19th century was direct enough that a French relay is not needed. Plausible, with Nourai's own lexicographical authority (Mo'in) preferring the shorter route.\",\n \"derivation_fa\": \"«تزار» در فارسی، لقب امپراتور روسیه، بی‌گمان همان واژه است که سرانجام از Caesar لاتین و از راه царь روسی می‌آید؛ دهخدا صریح می‌گوید: «تزار. تسار. کلمه روسی مشتق از سزار لاتینی. عنوان امپراتوران روسیه». آنچه محل تردید است زبانِ واسطِ بی‌میانجی است: معین این مدخل را با نشان «[روس.]» آورده، برخلاف مسیر «روسی ← فرانسوی ← فارسی» که نورایی کشیده است؛ آوای آغازین t- و پایانهٔ -ar هم با tsar فرانسوی می‌خواند و هم با царь روسی، و تماس فارسی با روسیه در سدهٔ نوزدهم آن‌قدر مستقیم بوده که به واسطهٔ فرانسوی نیازی نباشد. پس ادعا با احتیاط پذیرفتنی است، در حالی که مرجع فارسیِ خودِ نورایی (معین) راه کوتاه‌تر را ترجیح می‌دهد.\",\n \"sources\": [A_TEZAR, W_TSAR],\n \"ref_check\": [{\"ref\": \"BQT\", \"status\": \"partial\", \"note\": \"Cited without a page. Mo'in's footnote at Borhan p.1551 does list '(روسی) czar و tsar' among the descendants of Caesar (\" + BQT1551 + \"), which covers the Russian source but says nothing about a French relay into Persian.\"}],\n \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"Mo'in, Farhang-e Farsi s.v. تزار (via abadis.ir)\", \"stance\": \"contradicts\", \"note\": \"\\\"(تِ) [ روس. ] (اِ.) عنوان پادشاهان گذشته روسیه، قیصر.\\\" — origin tag Russian, not French.\"},\n   {\"src\": \"BQT\", \"where\": \"Borhan p.1551 footnote\", \"stance\": \"partial\", \"note\": \"'(روسی) czar و tsar' listed as reflexes of Caesar.\"}\n ]\n})\n\nnodes.append({\n \"id\": 14, \"lang\": \"English\", \"words\": \"czar, tsar, tzar\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"English czar/tsar/tzar 'emperor of Russia' is attested from the 1550s, borrowed from Russian царь after Ivan IV assumed the title in 1547. The odd cz- spelling, which matches no Slavonic orthography, comes from Sigismund von Herberstein's Latin Rerum Moscoviticarum Commentarii (1549), the chief Western source on Russia, whence it spread to all the Western languages; the closer transliteration tsar became common in English only towards the end of the 19th century (OED, via Etymonline). All three spellings in the node are therefore genuine, and Nourai's Russian parent is right.\",\n \"derivation_fa\": \"صورت‌های czar/tsar/tzar در انگلیسی از دههٔ ۱۵۵۰ گواهی شده‌اند و از царь روسی وام گرفته شده‌اند، پس از آنکه ایوان چهارم در ۱۵۴۷ این لقب را پذیرفت. املای عجیبِ cz- که با هیچ خط اسلاوی نمی‌خواند، از کتاب لاتینِ زیگیسموند فون هربرشتاین، Rerum Moscoviticarum Commentarii (۱۵۴۹)، مهم‌ترین منبع اروپاییان دربارهٔ روسیه، به همهٔ زبان‌های باختری راه یافته است؛ آوانگاشت دقیق‌ترِ tsar تنها در اواخر سدهٔ نوزدهم در انگلیسی رایج شد (فرهنگ آکسفورد، به نقل اتیمآنلاین). پس هر سه املای این گره اصیل‌اند و والدِ روسیِ نورایی درست است.\",\n \"sources\": [E_CAESAR, W_TSAR],\n \"ref_check\": [{\"ref\": \"AHD\", \"status\": \"partial\", \"note\": \"The Watkins IE-root appendix on disk does not list CZAR under kae-id- (AHD_watkins1985.txt line 566), since the word is a modern loan and not an inherited Latin derivative; the claim belongs to the AHD's main dictionary, which is not on disk.\"}],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein 1966 s.v. czar (line 10154)\", \"stance\": \"supports\", \"note\": \"\\\"czar, tsar, n. — Russ. tsar, fr. earlier tsesar', fr. OSlav. cesari, fr. Goth. kaisar ... fr. L. Caesar\\\".\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etym. Dict., word-list (line 23469)\", \"stance\": \"supports\", \"note\": \"'Russian from Latin: czar.'\"}\n ]\n})\n\nnodes.append({\n \"id\": 15, \"lang\": \"French\", \"words\": \"\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Empty pass-through node for Old French / French ciment 'cement, mortar, pitch', from Latin caementa, plural of caementum 'stone chips used for making mortar' (< caed- 'cut' + -mentum). The sense moved from 'small broken stones' to 'powdered stone used as a binder' already in Gallo-Romance, before the word reached English. This is the correct intermediary both for English cement (node #17) and for Persian سیمان (node #16).\",\n \"derivation_fa\": \"این جعبهٔ خالی نمایندهٔ ciment فرانسوی (و فرانسوی کهن) به معنی «سیمان، ملات، قیر» است که از caementa لاتین، جمعِ caementum «خرده‌سنگ برای ساختن ملات» (از ستاک caed- «بریدن» + پسوند -mentum) می‌آید. تحول معنایی از «سنگ‌ریزهٔ شکسته» به «سنگِ سوده و پودرشده در نقش چسباننده» پیش از رسیدن واژه به انگلیسی، در قلمرو گالورمانی روی داده است. این گره واسطهٔ درستِ هر دو فرزندش است: cement انگلیسی (گرهِ ۱۷) و «سیمان» فارسی (گرهِ ۱۶).\",\n \"sources\": [E_CEMENT, AHD_CEMENT],\n \"ref_check\": [{\"ref\": \"AHD:217\", \"status\": \"partial\", \"note\": \"The New College main dictionary is not on disk; its current online successor s.v. cement reads '[Middle English, from Old French ciment, from Latin caementum, rough-cut stone, rubble used in making concrete, from caedere, to cut; see kaə-id- in the Appendix of Indo-European roots.]' — precisely Nourai's Latin > French chain, and p.217 is where 'cement' falls in that edition's alphabet.\"}],\n \"consulted\": [\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. kae-id-, and AHD online s.v. cement\", \"stance\": \"supports\", \"note\": AHD_WATKINS + \" (CEMENT is listed among the Latin caedere derivatives).\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etym. Dict. s.v. Chisel (SKT.txt line 3405)\", \"stance\": \"supports\", \"note\": \"Skeat treats the whole French cis-/cim- family as 'from L. caes-um, supine of caedere, to cut'.\"},\n   {\"src\": \"SYN\", \"where\": \"Buck 9.21/9.22\", \"stance\": \"supports\", \"note\": \"\\\"OFr. cisoires fr. VLat. *caesorium, *cisorium, fr. caedere 'cut down, strike' (9.21)\\\" — same Latin > Old French route for the sister word.\"}\n ]\n})\n\nnodes.append({\n \"id\": 16, \"lang\": \"Persian\", \"words\": \"sement «سمنت»\",\n \"verdict\": \"plausible\",\n \"derivation\": \"Two different loans are packed into this box. The bracketed سیمان sīmān, the ordinary Iranian Persian word for cement, is indeed from French ciment — Wiktionary's etymology tree is explicit: Latin caementum > Old French ciment > French ciment > (borrowed) Persian سیمان. But the headword Nourai actually prints, سمنت sement, is the Afghan/Dari form, and Mo'in — the very dictionary cited (MON:1983) — tags it '[انگ.]', English: 'سمنت (س مِ نْ) [انگ.] (اِ.) سیمان'. So the French parent fits the parenthesised سیمان and not the headword سمنت, which came in through English cement (whence also the -t). The ultimate Latin caementum origin is right either way.\",\n \"derivation_fa\": \"در این جعبه دو وام‌واژهٔ جداگانه کنار هم نشسته‌اند. «سیمان» که در فارسی ایران واژهٔ معمول است، به‌راستی از ciment فرانسوی گرفته شده؛ درخت ریشه‌شناسی ویکی‌واژه صریح است: caementum لاتین › ciment فرانسوی کهن › ciment فرانسوی › «سیمان» فارسی. اما سرواژه‌ای که نورایی چاپ کرده، یعنی «سمنت»، صورت افغانی/دری است و معین — همان فرهنگی که به آن ارجاع داده شده — آن را با نشانِ «[انگ.]» آورده است: «سمنت (س مِ نْ) [انگ.] (اِ.) سیمان». پس والدِ فرانسوی با «سیمانِ» داخل کمانک می‌خواند نه با سرواژهٔ «سمنت» که از cement انگلیسی آمده (و «ت» پایانی نیز از همان‌جاست). خاستگاه نهایی، یعنی caementum لاتین، در هر دو حال درست است.\",\n \"sources\": [W_SIMAN, A_SEMENT],\n \"ref_check\": [{\"ref\": \"MON:1983\", \"status\": \"contradicts\", \"note\": \"Mo'in s.v. سمنت (via abadis.ir, section فرهنگ معین): \\\"(س مِ نْ) [ انگ. ] (اِ.) سیمان.\\\" — Mo'in's origin tag for the headword is English, not French. (MON_part1/2.txt on disk carry no page numbers, so p.1983 itself could not be verified; the alphabetical position of سمنت in vol. 2 is consistent with it.)\"}],\n \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"Mo'in s.v. سمنت\", \"stance\": \"contradicts\", \"note\": \"'[ انگ. ]' — English.\"},\n   {\"src\": \"BQT\", \"where\": \"Borhan-e Qate'\", \"stance\": \"silent\", \"note\": \"A 1062/1652 dictionary; no entry for this 20th-century technical loan.\"},\n   {\"src\": \"ARY\", \"where\": \"Aryanpur, IE roots of Persian (incoming/ARY/ARY_pages.txt)\", \"stance\": \"silent\", \"note\": \"grep for سیمان/سمنت returns nothing in the available OCR.\"}\n ]\n})\n\nnodes.append({\n \"id\": 17, \"lang\": \"English\", \"words\": \"cement\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"English cement 'binding mortar' is attested c.1300 from Old French ciment, from Latin caementa 'stone chips used for making mortar' (sing. caementum), from caedere 'to cut down, hew'. The AHD's own etymology (the dictionary Nourai cites) reads '[Middle English, from Old French ciment, from Latin caementum ... from caedere, to cut; see kaə-id- in the Appendix]', and Watkins lists CEMENT under kae-id-. The French parent drawn here is therefore exactly right.\",\n \"derivation_fa\": \"واژهٔ cement در انگلیسی از حدود ۱۳۰۰ م. گواهی شده و از ciment فرانسوی کهن است، آن هم از caementa لاتین «خرده‌سنگ‌هایی که برای ساختن ملات به کار می‌رود» (مفرد: caementum) از فعل caedere «بریدن، تراشیدن». ریشه‌شناسی خودِ فرهنگ AHD — همان مرجعی که نورایی آورده — چنین است: «انگلیسی میانه، از ciment فرانسوی کهن، از caementum لاتین ... از caedere «بریدن»؛ ذیل kaə-id- در پیوست ریشه‌های هندواروپایی»، و واتکینز نیز CEMENT را زیر همین ریشه آورده است. پس والدِ فرانسویِ این گره کاملاً درست است.\",\n \"sources\": [E_CEMENT, AHD_CEMENT],\n \"ref_check\": [{\"ref\": \"AHD\", \"status\": \"supports\", \"note\": AHD_WATKINS + \" — CEMENT is explicitly among the reflexes; the online AHD entry gives the full Middle English < Old French < Latin caementum < caedere chain.\"}],\n \"consulted\": [\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. kae-id-; ahdictionary.com s.v. cement\", \"stance\": \"supports\", \"note\": \"'[Middle English, from Old French ciment, from Latin caementum, rough-cut stone, rubble used in making concrete, from caedere, to cut; see kaə-id-...]'\"},\n   {\"src\": \"KLN\", \"where\": \"Klein 1966 s.v. cement\", \"stance\": \"supports\", \"note\": \"Klein's C volume gives the same Old French > Latin caementum > caedere chain (the entry is on the p.~270 leaf of KLN_1966.txt).\"},\n   {\"src\": \"WEB\", \"where\": \"Webster's New Twentieth Century vol.1 (cement page)\", \"stance\": \"supports\", \"note\": \"Same derivation from L. caementum.\"}\n ]\n})\n\nnodes.append({\n \"id\": 18, \"lang\": \"English\", \"words\": \"scissors, chisel, concise, precise, circumcise, incision\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"All six belong to Latin caedere. The learned ones are straightforward: concise < concīsus, precise < praecīsus, circumcise < circumcīsus, incision < incīsiō — all with the regular compositional vowel change caed- > -cīd-/-cīs-. chisel is Old French cisel (Modern French ciseau) < Late Latin *cisellum for cīsōrium 'cutting instrument', from caes-, supine stem of caedere. scissors is the same family: Middle English sisoures, cisours < Old French cisoires < Vulgar Latin *cisōria — the sc- spelling is a later corruption, as Skeat says plainly: 'The mod. E. scissors is a corrupt spelling, due to confusion with Low L. scissor (from scindere, to cut), which, however, only means a man who cuts, a tailor, and has, in fact, nothing at all to do with the word.' Watkins lists CHISEL, SCISSORS, CONCISE, PRECISE, CIRCUMCISE, INCISE all under kae-id-.\",\n \"derivation_fa\": \"هر شش واژه به caedere لاتین می‌رسند. صورت‌های عالمانه روشن‌اند: concise از concīsus، precise از praecīsus، circumcise از circumcīsus و incision از incīsiō؛ در همهٔ اینها تبدیل قاعده‌مند واکه در ترکیب رخ داده است (caed- › -cīd-/-cīs-). واژهٔ chisel از cisel فرانسوی کهن (ciseau امروزی) و آن از *cisellum لاتین متأخر به جای cīsōrium «ابزار بریدن» از ستاک سوپینِ caes- است. واژهٔ scissors نیز از همین خانواده است: انگلیسی میانه sisoures/cisours از cisoires فرانسوی کهن از *cisōria لاتین عامیانه؛ املای sc- دگرگونی متأخری است، چنان‌که اسکیت به صراحت می‌گوید: «املای امروزی scissors نادرست است و از درآمیختن با scissor لاتین پسین (از scindere «بریدن») پدید آمده که آن هم تنها به معنی «برنده، خیاط» است و هیچ ربطی به این واژه ندارد». واتکینز نیز همهٔ این واژه‌ها را ذیل kae-id- آورده است.\",\n \"sources\": [AHD_CEMENT],\n \"ref_check\": [{\"ref\": \"AHD\", \"status\": \"supports\", \"note\": AHD_WATKINS + \" — CHISEL, SCISSORS, CIRCUMCISE, CONCISE, INCISE and PRECISE are all listed by Watkins under the root, i.e. exactly this node's word list.\"}],\n \"consulted\": [\n   {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etym. Dict. s.vv. Chisel, Scissors (SKT.txt lines 3405-3406, 16651)\", \"stance\": \"supports\", \"note\": \"s.v. Chisel: \\\"O.F. cisel ... Low L. casellus ... a mere variant of L. cisorium, a cutting instrument ... L. caesum, supine of caedere, to cut\\\"; s.v. Scissors: \\\"The mod. E. scissors is a corrupt spelling, due to confusion with Low L. scissor (from scindere, to cut) ... has, in fact, nothing at all to do with the word ... F. ciseaux ... pl. of ciseau, a chisel.\\\"\"},\n   {\"src\": \"SYN\", \"where\": \"Buck 9.22 (SYN.txt line 14145)\", \"stance\": \"supports\", \"note\": \"\\\"It. cesoie, OFr. cisoires fr. VLat. *caesorium, *cisorium, fr. caedere 'cut down, strike' (9.21). REW 1475.\\\"\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. kae-id-\", \"stance\": \"supports\", \"note\": AHD_WATKINS}\n ]\n})\n\nnodes.append({\n \"id\": 19, \"lang\": \"Latin\", \"words\": \"Caesaria\",\n \"verdict\": \"transcription_suspect\",\n \"error_in\": \"book\",\n \"book_prints\": \"Caesaria\",\n \"correct_form\": \"Caesarea\",\n \"derivation\": \"Two things are wrong here, both in the book itself (the PDF page 457 / book p.427 prints 'Caesaria : an ancient seaport in Roman Palestine', so the extraction is faithful). First the form: the Latin place-name is Caesarēa (Greek Καισάρεια), an adjectival formation on the name Caesar — 'Caesaria' with -ia is Nourai's misprint. Second, and more seriously, the wrong Caesarea is named: Caesarea Maritima in Judaea, built by Herod for Augustus, has nothing to do with Jersey. The Caesarea that matters for node #20 is the Roman name of a Channel Island in the Antonine Itinerary, which the traditional etymology identifies with Jersey. Berlitz, whom Nourai follows here, says only 'The Latin name of several Roman cities, from which Jersey is derived, was Caesarea'; Funk & Wagnalls likewise has '< Isle of Jersey, < L. Caesarea, < Caesar' with no mention of Palestine. Note also that Caesarea is named for the cognomen Caesar, whose own derivation from caedere is a folk etymology (node #5), so this branch hangs from the root only indirectly.\",\n \"derivation_fa\": \"در این گره دو خطا هست و هر دو از خودِ کتاب است (تصویر صفحهٔ ۴۵۷ پی‌دی‌اف / ص ۴۲۷ کتاب همان «Caesaria : an ancient seaport in Roman Palestine» را نشان می‌دهد، پس خوانش اسکن درست بوده). نخست صورت واژه: نام لاتینی این شهرها Caesarēa است (یونانی Καισάρεια)، صفتی ساخته‌شده از نام Caesar؛ «Caesaria» با -ia خطای چاپی نورایی است. دوم و مهم‌تر، شهرِ نادرستی نام برده شده: قیصریهٔ فلسطین (Caesarea Maritima) که هیرودیس آن را برای آوگوستوس ساخت هیچ ربطی به جرزی ندارد؛ آن Caesarea‌ای که به کار گرهِ ۲۰ می‌آید نام رومیِ یکی از جزایر مانش در «سفرنامهٔ آنتونینوس» است که ریشه‌شناسی سنتی آن را همان جرزی می‌داند. برلیتس که نورایی از او گرفته تنها می‌گوید «نام لاتینی چند شهر رومی که جرزی از آن گرفته شده Caesarea بود»، و فانک و واگنالز نیز «< Isle of Jersey, < L. Caesarea, < Caesar» دارد و سخنی از فلسطین نیست. افزون بر این، Caesarea از لقب Caesar گرفته شده و اشتقاق خودِ آن لقب از caedere ریشه‌شناسی عامیانه است (گرهِ ۵)، پس این شاخه تنها به‌واسطه به ریشه می‌پیوندد.\",\n \"sources\": [E_JERSEY, W_JERSEY],\n \"ref_check\": [\n   {\"ref\": \"FSD:1317\", \"status\": \"partial\", \"note\": FSD1317 + \" — Funk & Wagnalls gives the Caesarea > Jersey chain but does not identify it with the Palestinian seaport, and spells it Caesarea.\"},\n   {\"ref\": \"AHD:186\", \"status\": \"not_checked\", \"note\": \"The New College Edition main dictionary (where p.186 would fall among the C-entries) is not on disk; the IE-root appendix that is on disk has no CAESAREA.\"}\n ],\n \"consulted\": [\n   {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls New Standard, jer- page (vol.2 leaf 612)\", \"stance\": \"partial\", \"note\": FSD1317},\n   {\"src\": \"NAT\", \"where\": \"Berlitz, Native Tongues p.166\", \"stance\": \"partial\", \"note\": NAT166 + \" — 'several Roman cities', not the Palestinian seaport.\"},\n   {\"src\": \"WEB\", \"where\": \"Webster's New Twentieth Century vol.1, s.v. Caesarea\", \"stance\": \"silent\", \"note\": \"The gazetteer entries are in the back matter of vol. 2, which is not the volume held on disk.\"}\n ]\n})\n\nnodes.append({\n \"id\": 20, \"lang\": \"French\", \"words\": \"Jersey\",\n \"verdict\": \"disputed\",\n \"derivation\": \"The Caesarea etymology of Jersey is the traditional one — it goes back to the identification of the Antonine Itinerary's Caesarea with the island — and it is what Nourai's three references say (Funk & Wagnalls: '< Isle of Jersey, < L. Caesarea, < Caesar'; Berlitz: 'The Latin name ... from which Jersey is derived, was Caesarea'). Modern onomastics prefers a Norse origin. Wiktionary: 'From Middle English Gersey, from Anglo-Norman Gersui, further etymology disputed. Probably from Old Norse, compound of Geirs (\\\"Geirr's\\\") + ey (\\\"island\\\"). Also occasionally and historically connected to Latin Caesarea'; Etymonline: 'Its name is said to be a corruption of Latin Caesarea ... but it is perhaps rather a Viking name (perhaps meaning \\\"Geirr's island\\\")', and it notes that neighbouring Guernsey's name is certainly Viking, with the same -ey 'island' second element — a strong argument that Jersey was formed the same way by the Norse settlers of the 9th-10th centuries. The language label is also loose: the name reaches English as Anglo-Norman Gersui / Middle English Gersey, i.e. through Norman rather than standard French.\",\n \"derivation_fa\": \"اشتقاق Jersey از Caesarea ریشه‌شناسی سنتی است و به یکی‌دانستن جزیره با «قیصریه»ی یادشده در سفرنامهٔ آنتونینوس بازمی‌گردد؛ هر سه مرجع نورایی نیز همین را می‌گویند (فانک و واگنالز: «از جزیرهٔ جرزی، از Caesarea لاتین، از Caesar»؛ برلیتس: «نام لاتینی ... که جرزی از آن گرفته شده Caesarea بود»). اما نام‌شناسی امروزی خاستگاه اسکاندیناویایی را ترجیح می‌دهد. ویکی‌واژه: «از Gersey انگلیسی میانه، از Gersui انگلونورمان؛ ریشهٔ دورتر محل اختلاف است. احتمالاً از نورس باستان، مرکب از Geirs «از آنِ گِیر» + ey «جزیره»؛ گاه و از دیرباز نیز با Caesarea لاتین پیوند داده شده است». اتیمآنلاین هم می‌گوید «گفته‌اند نامش تحریف Caesarea لاتین است ... ولی شاید بیشتر نامی وایکینگی باشد («جزیرهٔ گِیر»)» و یادآور می‌شود که نام جزیرهٔ همسایه، گرنزی، بی‌گمان وایکینگی است و همان جزء دومِ -ey «جزیره» را دارد — و این خود دلیلی نیرومند است که جرزی را هم همان مهاجران نورسِ سدهٔ نهم و دهم چنین نامیده باشند. برچسب زبانی نیز دقیق نیست: این نام از راه انگلونورمان (Gersui) و انگلیسی میانه (Gersey) به انگلیسی رسیده، نه از فرانسویِ معیار. داوری: پژوهش امروزی ادعای نورایی را رد می‌کند.\",\n \"sources\": [W_JERSEY, E_JERSEY],\n \"ref_check\": [\n   {\"ref\": \"FSD:1317\", \"status\": \"supports\", \"note\": FSD1317},\n   {\"ref\": \"NAT:166\", \"status\": \"supports\", \"note\": NAT166},\n   {\"ref\": \"AHD:703\", \"status\": \"not_checked\", \"note\": \"New College Edition main dictionary not on disk; p.703 is where 'jersey' falls alphabetically in that edition.\"}\n ],\n \"consulted\": [\n   {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls New Standard, jer- page (vol.2 leaf 612)\", \"stance\": \"supports\", \"note\": FSD1317 + \" — but this is a 1913 dictionary, repeating the traditional identification.\"},\n   {\"src\": \"NAT\", \"where\": \"Berlitz, Native Tongues p.166\", \"stance\": \"supports\", \"note\": NAT166 + \" — a popular book, not a place-name authority.\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etym. Dict., grep for jersey\", \"stance\": \"silent\", \"note\": \"Skeat has no entry for jersey.\"}\n ]\n})\n\nnodes.append({\n \"id\": 21, \"lang\": \"Persian\", \"words\": \"žerseh «ژرسه»\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"NP ژرسه žerse 'a fine knitted cloth; a knitted jersey' is a 20th-century borrowing of French jersey (pronounced /ʒɛʁzɛ/), which is why Persian has initial ž- and a final -e rather than the English /dʒɜːzi/: the Persian spelling ژرسه reproduces the French sound exactly. Mo'in's entry tags it '[فر.]' — French — and glosses it '۱- نوعی پارچهٔ نازک ۲- نیم‌تنهٔ بافته از نخ', 'a kind of thin cloth; a knitted jumper', which matches Nourai's 'a fine cloth'. The French word is itself the island's name, applied to the knitted worsted made there.\",\n \"derivation_fa\": \"«ژرسه» در فارسی، به معنی پارچهٔ نازک بافتنی و نیز نیم‌تنهٔ بافته، وام‌واژه‌ای است از سدهٔ بیستم از jersey فرانسوی (با تلفظ /ʒɛʁzɛ/)؛ از همین روست که در فارسی آغاز واژه «ژ» است و پایان آن «ـه»، نه صورت انگلیسی /dʒɜːzi/: املای «ژرسه» دقیقاً آوای فرانسوی را بازمی‌تاباند. معین این مدخل را با نشان «[فر.]» آورده و چنین معنا کرده است: «۱- نوعی پارچهٔ نازک، ۲- نیم‌تنهٔ بافته از نخ» که با «a fine cloth» نورایی می‌خواند. خودِ واژهٔ فرانسوی همان نام جزیره است که به پارچهٔ پشمیِ بافتهٔ آنجا داده شده است.\",\n \"sources\": [A_ZERSEH],\n \"ref_check\": [{\"ref\": \"VOP:203\", \"status\": \"not_checked\", \"note\": \"Moshiri, Farhang-e vazheha-ye orupayi dar farsi (1371/1992) has no copy online or on disk (refs_online.json records a 2026-09 re-search that found nothing); the claim was checked instead against Mo'in via abadis.ir, which gives the same French origin.\"}],\n \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"Mo'in, Farhang-e Farsi s.v. ژرسه (via abadis.ir)\", \"stance\": \"supports\", \"note\": \"\\\"(ژِ س) [ فر. ] (اِ.) ۱- نوعی پارچة نایلونی نازک. ۲- نیم تنة بافته از نخ.\\\" — origin tag French.\"},\n   {\"src\": \"ARY\", \"where\": \"Aryanpur (incoming/ARY/ARY_pages.txt)\", \"stance\": \"silent\", \"note\": \"No entry found in the available OCR; Aryanpur's book covers inherited Indo-European vocabulary, not modern European loans.\"}\n ]\n})\n\nnodes.append({\n \"id\": 22, \"lang\": \"English\", \"words\": \"Jersey, New Jersey; jersey\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"The English words are exactly as described. Jersey is the Channel Island; New Jersey was named in 1664 when Charles II's grant was made to Sir George Carteret, who had held Jersey for the king during the Civil War. The common noun jersey is first recorded in the 1580s of a kind of knitted worsted cloth made on the island, and from 1845 of the close-fitting knitted tunic — originally the fishermen's garment, later the sporting shirt; from 1842 it is also the breed of cattle, and in American English it has been short for New Jersey since 1758. Only the further step back to Latin Caesarea is doubtful (node #20), not anything in this box.\",\n \"derivation_fa\": \"واژه‌های انگلیسی این جعبه دقیقاً همان‌اند که نورایی می‌گوید: Jersey نام یکی از جزایر مانش است؛ New Jersey در ۱۶۶۴ م. نام گرفت، هنگامی که چارلز دوم آن قلمرو را به سِر جورج کارترت واگذاشت که در جنگ داخلی جزیرهٔ جرزی را برای شاه نگاه داشته بود. اسم عامِ jersey نخستین بار در دههٔ ۱۵۸۰ برای نوعی پارچهٔ بافتهٔ پشمی ساختِ همان جزیره به کار رفته و از ۱۸۴۵ به نیم‌تنهٔ بافتهٔ چسبان گفته شده است — نخست جامهٔ ماهی‌گیران و سپس پیراهن ورزشی؛ از ۱۸۴۲ نام نژادی از گاو نیز هست و در انگلیسی آمریکایی از ۱۷۵۸ کوتاه‌شدهٔ New Jersey به شمار می‌رود. تنها گامِ واپسین، یعنی بازگشت به Caesarea لاتین، محل تردید است (گرهِ ۲۰) نه چیزی در این جعبه.\",\n \"sources\": [E_JERSEY, W_JERSEY],\n \"ref_check\": [\n   {\"ref\": \"FSD:1317\", \"status\": \"supports\", \"note\": FSD1317 + \" — the same page carries 'Jer'sey, n. 1. One of the English Channel Islands; 45 sq. m.' and the cloth sense.\"},\n   {\"ref\": \"NAT:166\", \"status\": \"supports\", \"note\": NAT166 + \" — Berlitz names New Jersey, the island, the cattle and the sweater together, exactly this node's list.\"}\n ],\n \"consulted\": [\n   {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls New Standard, jer- page (vol.2 leaf 612)\", \"stance\": \"supports\", \"note\": FSD1317},\n   {\"src\": \"NAT\", \"where\": \"Berlitz, Native Tongues p.166\", \"stance\": \"supports\", \"note\": NAT166},\n   {\"src\": \"WEB\", \"where\": \"Webster's New Twentieth Century vol.1\", \"stance\": \"silent\", \"note\": \"The J-entries are in vol. 2, which is not the volume held on disk.\"}\n ]\n})\n\nentry = {\n \"entry\": 0,\n \"root\": \"Skhai\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *(s)k(h)ai-d- / *kh₂eyd-, *keh₂id- 'to strike, hew, cut' (Pokorny 917; Watkins kae-id-)\",\n \"note\": (\"Pokorny 917 has the lemma '(s)k(h)ai-, (s)k(h)ai-d-, (s)k(h)ai-t-' glossed 'schlagen' ('to hit, kick' in \"\n  \"the English rendering of the local text), and Watkins's appendix repeats it as 'kae-id-. To strike ... [Pok. \"\n  \"(s)k(h)ai- 917]'; the current reconstruction is *kh₂eyd-/*keh₂id- (de Vaan 79-80, via Wiktionary). Nourai's \"\n  \"headword, language label and gloss 'to cut, strike' are all right. Two cross-cutting problems affect the page. \"\n  \"(1) The whole Caesar branch (#5-#14) presupposes that the cognomen Caesar comes from caesus 'cut', i.e. from the \"\n  \"story that Caesar was delivered by a caesarean section. That is an ancient Roman folk etymology: Klein, on the \"\n  \"very page Nourai cites, says Caesar is 'of uncertain origin'; Pliny derived it from caesaries 'head of hair' and \"\n  \"the Century Dictionary from caesius 'blue-grey eyes'; and the story cannot be true of Julius Caesar himself, \"\n  \"whose mother outlived him. The loan chain Latin > Greek > Aramaic > Arabic > Persian, and Latin > Gothic > \"\n  \"Slavic > Russian, is nevertheless entirely sound. (2) The Jersey branch (#19-#22) rests on the traditional \"\n  \"Caesarea etymology, which modern place-name scholarship replaces with an Old Norse *Geirs-ey 'Geirr's island'. \"\n  \"By contrast the Iranian branch (#1-#3) is solid and is the most interesting part of the page: Bailey's \"\n  \"*cilauna- > MP celan 'dagger', celangar 'swordsmith' > NP chilan / chilangar 'small ironware, locksmith' is \"\n  \"confirmed by MacKenzie, Mo'in and Wiktionary alike.\"),\n \"note_fa\": (\"ریشهٔ شمارهٔ ۹۱۷ پوکورنی با سرواژهٔ «(s)k(h)ai-, (s)k(h)ai-d-, (s)k(h)ai-t-» و معنای «زدن» ثبت شده و \"\n  \"پیوست واتکینز نیز آن را با عنوان «kae-id-. زدن ... [پوکورنی ۹۱۷]» تکرار کرده است؛ بازسازی امروزی *kh₂eyd-/*keh₂id- \"\n  \"است (دِ ڤان، به نقل ویکی‌واژه). سرواژه، برچسب زبانی و معنای «بریدن، زدن» در کار نورایی درست است. اما دو اشکال \"\n  \"سراسری در این صفحه هست. یکم: کل شاخهٔ «قیصر» (گره‌های ۵ تا ۱۴) بر این فرض استوار است که لقب Caesar از caesus \"\n  \"«بریده» می‌آید، یعنی از داستان زاده‌شدن سزار با شکافتن شکم مادر. این ریشه‌شناسی عامیانهٔ رومی است: کلاین در همان \"\n  \"صفحه‌ای که نورایی ارجاع داده Caesar را «با خاستگاه نامعلوم» می‌داند، پلینیوس آن را از caesaries «گیسو» و فرهنگ \"\n  \"سنچری از caesius «چشم‌کبود» گرفته‌اند، و خودِ داستان دربارهٔ یولیوس سزار درست نیست چون مادرش از او دیرتر درگذشت. \"\n  \"با این همه زنجیرهٔ وام‌گیری لاتین › یونانی › آرامی › عربی › فارسی، و لاتین › گوتی › اسلاوی › روسی، یکسره درست است. \"\n  \"دوم: شاخهٔ «جرزی» (گره‌های ۱۹ تا ۲۲) بر ریشه‌شناسی سنتی Caesarea تکیه دارد که نام‌شناسی امروزی آن را با *Geirs-ey \"\n  \"نورس باستان («جزیرهٔ گِیر») جایگزین کرده است. در برابر اینها، شاخهٔ ایرانی (گره‌های ۱ تا ۳) استوار و خواندنی‌ترین \"\n  \"بخش این صفحه است: *čilauna- بیلی › čēlān «خنجر» و čēlāngar «شمشیرساز» فارسی میانه › «چیلان» و «چیلنگر/چلنگر» \"\n  \"فارسی نو، که مکنزی و معین و ویکی‌واژه هر سه آن را تأیید می‌کنند.\"),\n \"sources\": [W_CAEDO, E_CAESAR, W_JERSEY],\n \"ref_check\": [{\"ref\": \"POK:917\", \"status\": \"supports\", \"note\": POK_QUOTE + \" The page number is exact and the Latin material Nourai puts in node #4 is Pokorny's own. Pokorny's gloss is 'strike'; 'cut' comes from the Latin reflexes, so Nourai's double gloss 'to cut, strike' is fair.\"}],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"IEW 917\", \"stance\": \"supports\", \"note\": POK_QUOTE},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.v. kae-id- (AHD_watkins1985.txt line 566)\", \"stance\": \"supports\", \"note\": AHD_WATKINS},\n   {\"src\": \"WLD\", \"where\": \"Walde-Pokorny II 538\", \"stance\": \"supports\", \"note\": \"Bände I-II are not open online; the page is cited by Pokorny himself ('References: WP. II 538') and by Buck (SYN.txt line 8060: 'Lat. caedere \\\"cut, beat, strike down\\\". Walde-P. 2.538').\"},\n   {\"src\": \"IEC\", \"where\": \"Mann, IECD s.v. kai- (IEC.txt line 6597)\", \"stance\": \"partial\", \"note\": \"Mann attaches Lat. caedō, with a question mark, to a modal particle kai- 'alone, separate', i.e. he does not accept Pokorny's 917 grouping without reserve.\"},\n   {\"src\": \"SYN\", \"where\": \"Buck 9.21 'strike', 9.22 'cut'\", \"stance\": \"supports\", \"note\": \"SYN.txt line 14051: 'Lat. caedere \\\"strike, cut\\\" (9.21)'; line 14145 derives OFr. cisoires from caedere.\"}\n ],\n \"nodes\": nodes\n}\n\ndoc = {\n \"pdf_page\": 457,\n \"book_page\": 427,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-13\",\n \"entries\": [entry]\n}\n\nwith io.open('data/verification/page-457.json','w',encoding='utf-8') as f:\n    json.dump(doc, f, ensure_ascii=False, indent=1)\nprint(\"written\", len(nodes), \"nodes\")\nPYEOF\npython3 -m json.tool data/verification/page-457.json > /dev/null && echo \"JSON OK\"\npython3 tools/verify_check.py 457"
}
```


### [2026-09-14T02:15:49.889Z] TOOL RESULT

```
written 22 nodes
JSON OK
nodes verified: 22/22
node verdicts: {'plausible': 8, 'transcription_suspect': 3, 'disputed': 2, 'confirmed': 9}
root verdicts: {'confirmed': 1}
ref checks: {'partial': 10, 'supports': 12, 'not_found': 2, 'not_checked': 4, 'contradicts': 1}
books consulted: {'silent': 15, 'supports': 33, 'partial': 11, 'contradicts': 4} | by book: {'BQT': 8, 'KLN': 8, 'MON': 7, 'WEB': 5, 'SKT': 5, 'AHD': 4, 'ARY': 3, 'SYN': 3, 'FSD': 3, 'NAT': 3, 'ISS_alt_DKS': 2, 'KNT': 1, 'BRT': 1, 'PHD': 1, 'NYB': 1, 'HRN': 1, 'HUB': 1, 'POK': 1, 'WLD': 1, 'IEC': 1, 'FVQ': 1, 'AFM': 1, 'LKT': 1}
```


## [2026-09-14T02:16:10.622Z] AGENT

Done. `data/verification/page-457.json` written; `verify_check.py 457` reports 22/22 nodes, 0 PROBLEM lines. Page PNG archived at `data/verification/sources/refs/ocr/BOOK/457.png`; 17 web pages archived via `fetch_source.py`.

**Page 457 (book p.427), root "Skhai" (PIE *(s)k(h)ai-d- / *kh₂eyd- "strike, hew") — root: confirmed**
Node verdicts: 9 confirmed, 8 plausible, 2 disputed, 3 transcription_suspect.

Disputed:
- **#5 Greek kaisar** — the arrow encodes *caedere → Caesar* ("born by caesarean section"). Klein, on Nourai's own cited page 839, calls Caesar "of uncertain origin"; Pliny had caesaries "hair", Century Dict. caesius "grey-eyed"; the birth story cannot apply to Julius (Aurelia outlived him). Latin → Greek borrowing itself is fine.
- **#20 French Jersey** — Caesarea etymology is the traditional one (FSD, Berlitz, both verified verbatim); modern onomastics (Wiktionary, Etymonline) prefers Old Norse *Geirs-ey "Geirr's island", cf. certainly-Norse Guernsey.

Transcription_suspect:
- **#4 "â caesô mâtris ŭterě"** — error_in **book**: impossible Latin; should be *ā caesō mātris uterō* (Pliny NH 7.47). caedere/caementum/caelum themselves confirmed.
- **#19 "Caesaria"** — error_in **book**: should be *Caesarea*, and the wrong Caesarea is named — Jersey's Latin name is the Channel-Island Caesarea of the Antonine Itinerary, not Caesarea Maritima in Palestine (neither FSD nor Berlitz says Palestine).
- **#3 Persian چیلانگر** — error_in **extraction** (see below).

**Extraction error for the owner to fix:** node #3 `words[1].script` in `data/extracted/batch/page-457.json` is `چیلانگر`; the printed page shows **`چیلنگر`** (with `چلنگر` as the parenthetical variant, which the JSON has right in `script_extra`). چیلانگر is a real Mo'in variant but is not what this page prints.

Other notable findings: ISS:84 checked via Bailey's *Dictionary of Khotan Saka* (Khotanese Texts VI not online) — it fully supports MP *čēlān-kar* < *čilauna* < Pok. 917, but calls kai-/či- an Iranian base, not Old Persian (#1). MacKenzie glosses čēlān "dagger", čēlāngar "swordsmith" — narrower than Nourai's "metal objects/worker" (#2). BQT:1551 verified exactly (vol-3 pdf p.344, Mo'in's footnote on قیصر), and it adds the Aramaic mediation the chart omits (#6). **BQT:217 is not_found** — that page falls in letter ب of vol. 1. **MON:1983 contradicts** #16: Mo'in tags سمنت `[انگ.]` English, not French (سیمان is the French one). Mo'in also tags تزار `[روس.]`, against Nourai's Russian→French→Persian route (#13).
