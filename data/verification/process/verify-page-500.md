# Verification process log — verify-page-500


## [2026-10-15T02:44:16.127Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 500 only. Chart text: /home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-500.txt; source JSON: /home/sfmqrb/git/rishe-private/data/extracted/batch/page-500.json. Write /home/sfmqrb/git/rishe-private/data/verification/page-500.json, run `python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py 500` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-10-15T02:44:16.166Z] INPUT

<system-reminder>
Your final report is delivered through SubagentHandback: when your work is complete, call SubagentHandback({message: <your full report>}). The call ends your run, so make it your last step. Only a SubagentHandback call reaches your caller as your result; plain text you write at the end is not delivered.
</system-reminder>


## [2026-10-15T02:44:19.078Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-10-15T02:44:19.126Z] TOOL RESULT

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


## [2026-10-15T02:44:19.580Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-500.txt"
}
```


### [2026-10-15T02:44:19.642Z] TOOL RESULT

```
1	=== PDF page 500 (book page 470) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Tem : dark  (refs POK:1063)
4	#1 (parent #0) [Avestan] refs=POK:1063 | temah : darkness ; tethra : dark
5	  #2 (parent #1) [Persian] refs=BQT:456,511,544 | tam «تَم» : dark | extra: تار ، تاریک ، تیره
6	  #3 (parent #1) [Sogdian] refs=SOD:387 | tm : hell
7	#4 (parent #0) [Latin] refs=AHD | temĕre : to fear
8	  #5 (parent #4) [English] refs=AHD | timid, temerity
9	#6 (parent #0) [Sanskrit] refs=KLN:1626 | tâm-rah : dark red, coppery
10	  #7 (parent #6) [Malaysian] refs=KLN:1626 | tambaga : copper
11	    #8 (parent #7) [Portuguese] refs=KLN:1626 | tombac
12	      #9 (parent #8) [French] refs=KLN:1626 | tombac
13	        #10 (parent #9) [English] refs=OXF:435; KLN:1626 | tombac, tambaga
14	--- entry 1 ---
15	ROOT [Aramaic] Temar : he concealed  (refs KLN:948)
16	#1 (parent #0) [Arabic] refs=KLN:948 | temara, t.m.r : he concealed ; matmŭrah : a hiding place, storage
17	  #2 (parent #1) [Persian] refs=FVA:251; MON | matmŭreh «مطموره» : an underground storage place
18	  #3 (parent #1) [French] refs=KLN:948 | matamore : a dwelling place
19	    #4 (parent #3) [English] refs=KLN:948 | mattamore : a sub-terranian dwelling
20	--- entry 2 ---
21	ROOT Temp -> redirect to Ten 1
22	
```


## [2026-10-15T02:44:20.471Z] TOOL CALL #3: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/extracted/batch/page-500.json"
}
```


### [2026-10-15T02:44:20.546Z] TOOL RESULT

```
1	{
2	  "pdf_page": 500,
3	  "book_page": 470,
4	  "entries": [
5	    {
6	      "root": {
7	        "name": "Tem",
8	        "lang": "Indo-European",
9	        "refs": "POK:1063",
10	        "gloss": "dark"
11	      },
12	      "nodes": [
13	        {
14	          "id": 1,
15	          "parent": 0,
16	          "lang": "Avestan",
17	          "refs": "POK:1063",
18	          "words": [
19	            {"translit": "temah", "gloss": "darkness", "script": null},
20	            {"translit": "tethra", "gloss": "dark", "script": null}
21	          ],
22	          "note": null,
23	          "quote": null
24	        },
25	        {
26	          "id": 2,
27	          "parent": 1,
28	          "lang": "Persian",
29	          "refs": "BQT:456,511,544",
30	          "words": [
31	            {"translit": "tam", "gloss": "dark", "script": "تَم"}
32	          ],
33	          "script_extra": "تار ، تاریک ، تیره",
34	          "note": null,
35	          "quote": null
36	        },
37	        {
38	          "id": 3,
39	          "parent": 1,
40	          "lang": "Sogdian",
41	          "refs": "SOD:387",
42	          "words": [
43	            {"translit": "tm", "gloss": "hell", "script": null}
44	          ],
45	          "note": null,
46	          "quote": null
47	        },
48	        {
49	          "id": 4,
50	          "parent": 0,
51	          "lang": "Latin",
52	          "refs": "AHD",
53	          "words": [
54	            {"translit": "temĕre", "gloss": "to fear", "script": null}
55	          ],
56	          "note": null,
57	          "quote": null
58	        },
59	        {
60	          "id": 5,
61	          "parent": 4,
62	          "lang": "English",
63	          "refs": "AHD",
64	          "words": [
65	            {"translit": "timid, temerity", "gloss": null, "script": null}
66	          ],
67	          "note": null,
68	          "quote": null
69	        },
70	        {
71	          "id": 6,
72	          "parent": 0,
73	          "lang": "Sanskrit",
74	          "refs": "KLN:1626",
75	          "words": [
76	            {"translit": "tâm-rah", "gloss": "dark red, coppery", "script": null}
77	          ],
78	          "note": null,
79	          "quote": null
80	        },
81	        {
82	          "id": 7,
83	          "parent": 6,
84	          "lang": "Malaysian",
85	          "refs": "KLN:1626",
86	          "words": [
87	            {"translit": "tambaga", "gloss": "copper", "script": null}
88	          ],
89	          "note": null,
90	          "quote": null
91	        },
92	        {
93	          "id": 8,
94	          "parent": 7,
95	          "lang": "Portuguese",
96	          "refs": "KLN:1626",
97	          "words": [
98	            {"translit": "tombac", "gloss": null, "script": null}
99	          ],
100	          "note": null,
101	          "quote": null
102	        },
103	        {
104	          "id": 9,
105	          "parent": 8,
106	          "lang": "French",
107	          "refs": "KLN:1626",
108	          "words": [
109	            {"translit": "tombac", "gloss": null, "script": null}
110	          ],
111	          "note": null,
112	          "quote": null
113	        },
114	        {
115	          "id": 10,
116	          "parent": 9,
117	          "lang": "English",
118	          "refs": "OXF:435; KLN:1626",
119	          "words": [
120	            {"translit": "tombac, tambaga", "gloss": null, "script": null}
121	          ],
122	          "note": null,
123	          "quote": null
124	        }
125	      ]
126	    },
127	    {
128	      "root": {
129	        "name": "Temar",
130	        "lang": "Aramaic",
131	        "refs": "KLN:948",
132	        "gloss": "he concealed"
133	      },
134	      "nodes": [
135	        {
136	          "id": 1,
137	          "parent": 0,
138	          "lang": "Arabic",
139	          "refs": "KLN:948",
140	          "words": [
141	            {"translit": "temara, t.m.r", "gloss": "he concealed", "script": null},
142	            {"translit": "matmŭrah", "gloss": "a hiding place, storage", "script": null}
143	          ],
144	          "note": null,
145	          "quote": null
146	        },
147	        {
148	          "id": 2,
149	          "parent": 1,
150	          "lang": "Persian",
151	          "refs": "FVA:251; MON",
152	          "words": [
153	            {"translit": "matmŭreh", "gloss": "an underground storage place", "script": "مطموره"}
154	          ],
155	          "note": null,
156	          "quote": {
157	            "text": "آن بلبل کاتوره ، برجسته ز مطموره - چون دستهٔ تنبوره ، گیرد شجن از چنگل",
158	            "poet": "Manŭchehrî"
159	          }
160	        },
161	        {
162	          "id": 3,
163	          "parent": 1,
164	          "lang": "French",
165	          "refs": "KLN:948",
166	          "words": [
167	            {"translit": "matamore", "gloss": "a dwelling place", "script": null}
168	          ],
169	          "note": null,
170	          "quote": null
171	        },
172	        {
173	          "id": 4,
174	          "parent": 3,
175	          "lang": "English",
176	          "refs": "KLN:948",
177	          "words": [
178	            {"translit": "mattamore", "gloss": "a sub-terranian dwelling", "script": null}
179	          ],
180	          "note": null,
181	          "quote": null
182	        }
183	      ]
184	    },
185	    {
186	      "root": {
187	        "name": "Temp",
188	        "redirect": "Ten 1"
189	      },
190	      "nodes": []
191	    }
192	  ]
193	}
194	
```


## [2026-10-15T02:44:24.205Z] TOOL CALL #4: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification; cat sources/SOURCE_MATRIX.md | head -80; ls sources/refs/ | head -100; python3 -c \"\nimport json;d=json.load(open('sources/refs_online.json'))\nfor k in ['POK','BQT','SOD','AHD','KLN','OXF','FVA','MON','WLD','HRN','HUB','PHD','NYB','BRT','SKT','FSD','WEB','ARY','CHEUNG','IEC','SYN','HJB','LKT','DOZ','DEV','PHN','LAM','FVQ','AFM','PLA','AFA']:\n  print(k, json.dumps(d.get(k),ensure_ascii=False)[:300])\n\""
}
```


### [2026-10-15T02:44:24.695Z] TOOL RESULT

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
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft"
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-
SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current 
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "ki
OXF {"title": "J. Speake, Oxford Dictionary of Foreign Words and Phrases, New York 1997", "edition_found": "1997 (lending-only)", "kind": "archive_restricted", "url": "https://archive.org/details/oxforddictionary00spea ; isbn_9780965016070 (lending) ; Google Nvu17oLIQNgC = 2008 2nd ed. preview only", "i
FVA {"title": "S.M. Nahvi, Farhang-e Vazheha-ye Arabi dar Farsi (dakhil), Tohi/Azadi 1368/1989", "kind": "catalog", "url": "https://openlibrary.org/works/OL4602367W (edition OL2012991M: Intisharat-i Islami 1368/1989, 582 pp)", "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: no digital copy
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<wor
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rish
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/ri
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepa
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "i
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", 
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_sca
CHEUNG null
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-compa
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-
HJB {"title": "H. Yule & A. C. Burnell, Hobson-Jobson, 2nd ed. by W. Crooke, London 1903 (Delhi reprint 1968)", "edition_found": "1903 Crooke edition (pagination identical to the 1968 reprint)", "kind": "archive_djvu", "url": "https://archive.org/details/hobsonjobsonagl02croogoog", "identifier": "hobson
LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/gi
DOZ {"title": "R. Dozy, Oosterlingen: Verklarende lijst der Nederlandsche woorden die uit het Arabisch, Hebreeuwsch, Chaldeeuwsch, Perzisch en Turksch afkomstig zijn, Leiden 1867", "edition_found": "1867", "kind": "archive_djvu", "url": "https://archive.org/details/oosterlingenver00dozygoog", "identifie
DEV {"title": "L. M. Devic, Dictionnaire étymologique des mots français d'origine orientale, Paris 1876", "edition_found": "1876", "kind": "archive_djvu", "url": "https://archive.org/details/dictionnairety00devi", "identifier": "dictionnairety00devi (also dictionnairetym02devigoog, fr105comparative41)",
PHN {"title": "A. P. Pihan, Dictionnaire étymologique des mots de la langue française dérivés de l'arabe, du persan ou du turc, Paris 1866", "edition_found": "1866", "kind": "archive_djvu", "url": "https://archive.org/details/dictionnairetym01pihagoog", "identifier": "dictionnairetym01pihagoog (others: 
LAM {"title": "H. Lammens, Remarques sur les mots français dérivés de l'arabe, Beyrouth 1890", "edition_found": "1890", "kind": "archive_djvu", "url": "https://archive.org/details/remarquessurles00lammgoog", "identifier": "remarquessurles00lammgoog", "local_file": "/home/sfmqrb/git/rishe-private/data/ve
FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.L
AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)"
PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["
AFA {"title": "S. Fraenkel, Die aramäischen Fremdwörter im Arabischen, Leiden 1886 (repr. Hildesheim 1962, same pagination)", "edition_found": "1886", "kind": "archive_djvu", "url": "https://archive.org/details/diearamischenfr00fraegoog", "identifier": "diearamischenfr00fraegoog (also bub_gb_SzdbAAAAQAA
```


## [2026-10-15T02:44:28.086Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification; python3 -c \"\nimport json;d=json.load(open('sources/refs_online.json'))\nfor k in ['POK','BQT','SOD','AHD','KLN','MON','ARY','WLD']:\n  v=d[k]; print(k, v.get('lookup_hint'), v.get('local_file'), v.get('page_offset'), str(v.get('scans'))[:200]); print()\n\"; python3 -c \"\nimport json;d=json.load(open('page-499.json'));e=d['entries'][0];print(json.dumps({k:v for k,v in e.items() if k!='nodes'},ensure_ascii=False,indent=1)[:3000]);print(json.dumps(e['nodes'][0],ensure_ascii=False,indent=1)[:4000])\""
}
```


### [2026-10-15T02:44:28.662Z] TOOL RESULT

```
POK Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-dictionary/ (entry pages with page numbers) and StarLing https://starlingdb.org/cgi-bin/query.cgi?basename=\data\ie\pokorny&root=config /home/sfmqrb/git/rishe-private/data/verification/sources/refs/POK_01.txt POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> None

BQT grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=dehkhoda, parsi.wiki, abadis.ir/fatofa/<word>/) quotes Borhan and often Mo'in's footnotes as (حاشیهٔ برهان قاطع چ معین). noorlib.ir/book/info/10294 is a 1-vol Nima 1380 Borhan without Mo'in's notes. | For pages in a scanned volume use: python3 tools/ref_page.py BQT:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor) ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v5_pages_faseng.txt'] vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...'). [{'volume': '3', 'file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', 'first_printed': 1208, 'last_printed': 1925, 'pdf_offset': -1205, 'page_map':

SOD Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/SogdianDictionary for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf} ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SOD_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SOD.txt'] printed page ≈ leaf − 66 in SOD_pages.txt (0-based \f blocks; 645 leaves; English intro precedes) None

AHD Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru-' ; entries list English derivatives in caps. Restricted 1970s AHD scans on IA (lending only, djvu.txt returns 401): americanheritage0000dict (July 1977 printing, 970 leaves - probably the New College Edition), bwb_P9-BHZ-437 (1974), americanheritage00nyde (1970), bwb_W9-CSW-086 (1969, 1610 leaves = original 1969 ed.). /home/sfmqrb/git/rishe-private/data/verification/sources/refs/AHD_watkins1985.txt 1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page. None

KLN Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages. /home/sfmqrb/git/rishe-private/data/verification/sources/refs/KLN_1966.txt KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> None

MON Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different pagination from the 6-vol edition; OCR downloaded as MON_part1.txt / MON_part2.txt (no page breaks). ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/MON_part2.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt'] None None

ARY Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY:<printed page> --image ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY/ARY_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt'] printed page = pdf page + 1 [{'file': '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY/ARY_aryanpur_kashani_rishehaye_hend_o_orupayi.pdf', 'first_printed': 1, 'last_printed': 546, 'pdf_offset': -1, 'la

WLD Band 3 is the index (Wortregister by language) - it maps a word to 'Band, page' in vols 1-2, so it can at least confirm that a word is treated at the cited WP volume/page. For the actual entry text, use Pokorny 1959 (POK), whose entries cite 'WP. I 177' etc. and are essentially a revision of WP. ['/home/sfmqrb/git/rishe-private/data/verification/sources/refs/WLD_band3.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_text.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd1_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_text.pdf', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd2_pages.txt', '/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt'] Band 3: leaf = printed + 6. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> || Band I (WLD_Bd1_pages.txt, 887 leaves): printed = leaf(1-based) − 9 (leaf 801 = p.792). Band II (WLD_Bd2_pages.txt, 720 leaves): printed = leaf − 5 (leaf 701 = p.696). None

{
 "entry": 0,
 "root": "Tel",
 "verdict": "confirmed",
 "modern_form": "PIE *telh₂- 'to lift, bear, weigh; endure' (Pokorny 1. tel-, telə-, tlē-, tlā- 1060-1061; Watkins/AHD telə-; LIV² 622-623)",
 "note": "Pokorny IEW pp.1060-1061 heads the entry '1. tel-, telə-, tle(i)-, tlā-' 'to transport, carry; to bear, suffer', Watkins (AHD) 'telə- to lift, support, weigh', modern notation *telh₂-. Nourai's 'Tel : to lift', the label Indo-European and both his citations (POK:1060; KLN:122 = Klein s.v. Atlas, which spells out the base *tel-, *tal-, *tol- 'to bear, lift, suffer') are correct. The Greek, Latin, Sanskrit and English branches are standard (Pokorny, Walde-Pokorny, Watkins, Klein all list them). Two Iranian/Persian problems: (1) the 'Avestan' tara-āz(u) is Nyberg's reconstructed Old Iranian *tarā-āzu-, not an attested Avestan word; (2) the Persian tarāz/طراز box mixes tarāzū 'balance' (correct) with ṭarāz/tarāz 'adornment' and the city Ṭarāz of Farrokhī's verse, and the Persian atlas 'world' (falak-e atlas) is native Arabic aṭlas 'plain, smooth', not Greek Atlas. Toll's Greek origin is contested (Wiktionary prefers a native Germanic word). No extraction errors: the JSON matches the printed page, including the odd ref 'MON5:5155' (a misprint in the book, presumably for MON5:155).",
 "note_fa": "ریشهٔ هندواروپایی آغازین *telh₂- «برداشتن، بردن، سنجیدن؛ تاب آوردن» است؛ پوکورنی (ص۱۰۶۰–۱۰۶۱) آن را «tel-، telə-، tlā-» با معنای «بردن، حمل کردن؛ تحمل کردن» و واتکینز «telə- برداشتن، نگه داشتن، وزن کردن» آورده‌اند. «Tel: برداشتن» نورایی، برچسب «هندواروپایی» و هر دو مأخذ او (پوکورنی ۱۰۶۰ و کلاین ۱۲۲ ذیل Atlas) درست است. شاخه‌های یونانی، لاتین، سنسکریت و انگلیسی همه پذیرفته‌اند. اشکال‌ها در بخش ایرانی است: «tara-âz» اوستایی نیست بلکه بازسازی ایرانی باستانِ نیبرگ است؛ در خانهٔ فارسی «ترازو» درست است ولی «طراز» (زینت، و شهر طراز در بیت فرخی) واژهٔ دیگری است؛ و «اطلس» به معنای «فلک اطلس/جهان» از صفت عربی «أطلس» (صاف، بی‌نقش) است نه از تیتان یونانی. خطای استخراج دیده نشد.",
 "sources": [
  "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/telh₂-",
  "https://en.wiktionary.org/wiki/Ἄτλας",
  "https://en.wiktionary.org/wiki/τάλαντον"
 ],
 "ref_check": [
  {
   "ref": "POK:1060",
   "status": "supports",
   "note": "Pokorny IEW pp.1060-1061 (local POK_full.txt line 85184, 'Root /lemma: tel-1, tela-, tle(i)- tla-', Page(s): 1060-1061): 'Meaning: to transport, carry; to bear, suffer'; 'Old Indie tula 'scales, weight', tulayati 'hebt auf, wägt' ... tulya- 'gleichartig, comparable''; Greek tlēnai, talanton ('die beiden Waagschalen'), PN Atlas, -antos, telos 'payment, tribute, tax'; 'Latin tollo, -ere ... tolero ... latus 'getragen''."
  },
  {
   "ref": "KLN:122",
   "status": "supports",
   "note": "Klein 1966 (KLN_1966.txt leaf 75 = c. pp.122-127 by the two-pages-per-leaf offset; the Atlas entry is the one Nourai means) s.v. Atlas: 'Gk. τλῆναι derives fr. *tl-, zero degree of I.-E. base *tel-, *tal-, *tol-, 'to bear, lift, suffer', whence τάλας ... τ
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
   "note": "Mann: 'tl- (1) ... lift, raise, bear, suffer'. WP I, 701 & 738-9' with Tocharian, Greek tlēmi, Latin tuli, Gothic þulan — Sanskrit tulā is not quoted under this head."
  }
 ]
}
```


## [2026-10-15T02:44:45.141Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; ls /home/sfmqrb/git/rishe-private/site/pages/500.jpg; grep -n -i 'lemma: tem' POK_full.txt | head; grep -n -i -E '^tem[eə]?-|^temə' AHD_watkins1985.txt | head; grep -n -i -E '^(tombac|mattamore|temerity|timid)' KLN_1966.txt | head"
}
```


## [2026-10-15T02:44:45.515Z] TOOL CALL #7: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/site/pages/500.jpg"
}
```


### [2026-10-15T02:44:45.580Z] TOOL RESULT

```

```


### [2026-10-15T02:44:45.638Z] TOOL RESULT

```
Permissions Size User   Date Modified Name
.rw-r--r--   53k sfmqrb 14 Oct 22:15  /home/sfmqrb/git/rishe-private/site/pages/500.jpg
85335:Root / lemma: tem(9)- 
85342:Root / lemma: tem(a)- : dark' derived from Root / lemma: d^e/n-, 6'^ema- : "to smoke; to 
85392:Root / lemma: tem-1, tend- 
85423:Root / lemma: tem-2 
85453:Root / lemma: temp- 
23149:mattamore,  n.,  a  subterranean  dwelling  or  store¬ house.  —  F.  matamore,  fr.  Arab,  matmura  , ‘something  hidden’,  prop.  fem.  pass.  part,  of tdmara,  ‘he  hid,  concealed’,  fr.  Aram,  fmar,  of s.m.  See  Siegmund  Fraenkel,  Die  aramaischen Fremdworter  im  Arabischen,  p.  137.  Aram. tlmar  is  rel.  to  Heb.  taman,  ‘he  hid,  concealed’ (whence  matmon,  ‘treasure’,  lit.  ‘something  hid¬ den’),  Akkad,  tamaru,  ‘to  cover  with  earth’, matter,  n.  • —  ME.  matere,  fr.  OF.  matere  (F.  ma- tiere),  fr.  L.  materia,  ‘wood,  timber,  stuff,  mat¬ ter’,  formed  fr.  L.  mater,  ‘mother’,  as  transla¬ tion  of  Gk.  uXt),  ‘wood,  forest,  timber,  stuff, matter’.  See  mother  and  cp.  Madeira,  madrier. L.  materia  is  not  cogn.  with  Arm.  mair,  ‘pine, cedar’,  mairi,  ‘forest’.
38479:temerity,  n.,  rashness.  • —  ME.  temeryte,  fr.  L. temeritas,  ‘rashness’,  fr.  temere,  ‘rashly,  at random’,  prop,  ‘in  the  dark’,  fr.  I.-E.  base * femes -,  ‘dark’,  whence  also  L.  tenebrae  (for *temebrae,  fr.  *temesrae),  ‘darkness’,  OI.  td- mas-,  ‘darkness’,  tarpsrah,  ‘dark’,  tamrah,  ‘dark- red,  coppery’,  Avestic  tlmah,  ‘darkness’,  Toch. B  tamale,  ‘dark,  gloomy’,  Lith.  tamsa,  ‘dark¬ ness’,  tamsus,  ‘dark’,  Lett,  timsa,  tumsa,  ‘dark¬ ness’,  tumst,  ‘it  is  getting  dark’,  OSlav.  lima, ‘darkness’,  timinu,  ‘dark’,  MLG.  deemster, OHG.  dinstar,  ‘dark ',/instar  (with  dissimilation fr.  orig.  *pimstar ),  of  s.m.,  OIr.  temel,  ‘dark¬ ness’,  Mir.  teim,  temen,  ‘dark,  gray’,  MBret. teffal,  ‘dark’.  Cp.  tenebrae,  temulent,  timid.  Cp. also  tombac  and  the  first  element  in  malabatb- rum.  For  the  ending  see  suff.  -ity.
39284:timid,  adj.,  fearful.  —  L.  timidus,  ‘faint-hearted, cowardly,  timid’,  fr.  timere,  ‘to  fear’,  which  prob. meant  orig.  ‘to  be  in  the  dark,  to  grope  about  in the  dark’,  and  is  rel.  to  tenebrae  (for  *temebrae, fr.  *temesrae),  ‘darkness’,  temere,  ‘rashly,  at random’,  prop,  ‘in  the  dark’,  and  cogn.  with  OI. tamas-,  ‘darkness’,  tamsrah,  ‘dark’.  See  temerity and  1st  -id.
39477:tombac
39481:tombac,  n.,  an  alloy  of  copper  and  zinc,  F. tombac,  fr.,Port.  tombac,  fr.  Malay  tambaga, ‘copper’,  fr.  OI.  tamrakah,  of  s.m.,  fr.  tdmrdh, ‘dark-red,  coppery’,  which  is  rel.  to  tamas-, ‘darkness’.  See  tamas.
```


## [2026-10-15T02:44:50.314Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 85335,85395p POK_full.txt | cut -c1-600"
}
```


## [2026-10-15T02:44:52.209Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E '^tem[ə9e]?-|^temə-' AHD_watkins1985.txt; grep -n -i 'temere' AHD_watkins1985.txt | head; grep -n -E 'tem[əe]s?-.*dunkel|temə- .dunkel' incoming/WLD/WLD_Bd1_pages.txt | head; grep -n -E 'tamas|tąθra|tqθra|tanthra' BRT.txt | head; grep -n -i 'temah' BRT.txt | head"
}
```


### [2026-10-15T02:44:52.891Z] TOOL RESULT

```
Root / lemma: tem(9)- 
Meaning: dark 



Note: 

Root / lemma: tem(a)- : dark' derived from Root / lemma: d^e/n-, 6'^ema- : "to smoke; to 

blow'. 

Material: Old Indie tamas- n. " darkness, darkness ' = Avestan tamah-6s., npers. /a/77 "Star 

of Auges', Old Indie tamasa-^ swart ' (= Avestan tsmarjha-^ dim'), tamsra-^6ark, livid'; 

tamisrah{= Latin tenebrae), newer tamisrai., tamisra-m^ darkness'; famasvan{-vant) " 

dim' = Avestan tamahvant- "verblendef; /a/77/'a- "verdunkeind', tamra-^ oxblood, indigo, 

kupferrot', timira- "dark, dim'; fama/a-m. "Xanthoehymos pietorius' (tree with very dark 

bark); from tamala-pattram^l AeaV derive gr. piaAapaGpov, Latin malobat(h)rum\ Avestan 

tq&ra-Hom. PI. "darkness', np. tar^ dim' = *tam-sra-\ 

gr. (Aeolie) VN T£(jpTK£(; {* terns-); 

lllyrian mountain-N Topapoq by Dodona; 

Maybe alb. dhjame, PI. dhjamra " fat burnt as saerifiee'. 

Latin tenebrae^ darkness ' (diss, from *temafra= Old Indie tamisrahP\.), temere 
"blindlings, aufs Geratewohl' (Lok. *temes/"\n Dunkein [tappend]'), temero, -are^ blemish, 
disgraee ' (aetually "unvorsiehtig sanetify Dingen nahen'); Middle Irish teim, temen^dark, 
gray'. Old Irish temer darkness ', Middle Breton teffar dim'; Old High German demaru. 
"dawn, twilight'; Old Saxon th/mm^6ark' {*t^imza-)\ Middle Duteh deemster. Old High 
German d/nstar{an6 probably also Old High German finstai) " dim' {*temsro- = Old Indie 
tamsra-); Low German dTsig, Duteh d/jz/g loggy, dark' {*t^emsiga-)\ lengthened grade 
probably Old leelandie A'a/77"obseuritas aeris', Norwegian taam' unelearair, thin blanket 
of elouds '; 

Lithuanian temsta, temti^ dim beeome'; tamsa^ darkness ', tamsus^AarW, ablaut. 
Latvian tima, t/msa and tumsa^ darkness', Lithuanian /Msras "sehweiftfiJehsig, oxblood, 
indigo '; Latvian tumst{\ni.tumt) "es dunkelt'; Old Chureh Slavie ttma' darkness ', Old 
Chureh Slavie tbmtnb "dark'; russ. temrivo " darkness '; whether Slavie terib "shadow' as 
*tem-ni-s anzureihen? 

Toeharian B tamasse ' dark' . 

Maybe alb. d/men'\N'\nter, long winter nights' origin of PIE root for winter???, maybe alb. 
tym 'smoke' dark smoke' similar to poln. dymlll 

References: WP. I 720 f., WH. II 656 f., 664, Trautmann 322, Vasmer 3, 92 f., 162. 
Page(s): 1063-1064 



Root / lemma: tem-1, tend- 
Meaning: to cut 

Material: Gr. tejjvu), horn. Ionian Doric rapvu) (lionn. it\xz\) "cut, bite' (sTapov and STspov,
```


### [2026-10-15T02:44:52.937Z] TOOL RESULT

```
1078:a. Latin téla, web, net, warp of a fabric, also weaver’s beam (to which the warp threads are tied): TILLER?, ToiL2; b. Latin subtilis, thin, fine, precise, subtle (< *sub-téla, “thread passing under the warp,” the finest thread; sub, under; see upo): SUBTLE. 3. Suffixed form *teks-On, weaver, maker of wattle for house walls, builder (possibly contaminated with *teks-tdr, builder), in Greek tekton, carpenter, builder: TECTONIC; ARCHITECT. 4. Suf- fixed form *teks-nd-, craft (of weaving or fabricating), in Greek tekhné, art, craft, skill: TECHNICAL, POLYTECHNIC, TECHNOLOGY. 5. Possibly Germanic *thahsu-, badger (“the animal that builds,” referring to its burrowing skill), in Old High German dahs (> German Dachs), badger but more likely borrowed from the same pre- Indo-European source as the Celtic totemic name Tazgo-, Gaelic Tadhg, “‘badger’”): DACHSHUND. [Pok. tekth- 1058.] tekv-. To run, flee. Suffixed o-grade form *tokv-so- in Iranian *taxsa-, bow, borrowed into Greek toxon, bow, also (in the plural) bow and arrow (< “that which flies’): Toxic. [Pok. tekz- 1059.] tel-. Ground, floor, board. 1. Germanic *thil-j6- in Middle Low German and Middle Dutch dele, plank: DEAL?. 2. Suffixed form *tel-n- in Latin telliis (stem telliir-), earth, the earth: (TELLURIAN), (TELLURIC), (TELLURION), (TELLURIUM), TELLURO-. 3. Possibly reduplicated form *ti-tel- in Latin titulus, placard, label, superscription, title: TITLE. [Pok. 2. tel- 1061.] tela-. To lift, support, weigh; with derivatives referring to measured weights and thence to money and payment. 1. Suffixed form *telo-mon- in Greek telamén, supporter, bearer: TELAMON. 2. Suffixed form *tel/a)-es- in: a. Greek telos, tax, charge: TOLL!; PHILATELY; b. Latin tolerdre, to bear, endure: TOLERATE. 3. Suffixed zero-grade form *th-i-, becoming *tali- (influenced by ¢dlis, such), in Latin ¢alid, reciprocal punishment in kind, “something paid out”: TALION; RETALIATE. 4. Suffixed variant zero-grade form *tala-nt- in Greek talanton, balance, weight, any of several specific weights of gold or silver, hence the sum of money represented by such a weight: TALENT. 5. Perhaps intensive reduplicated form *tantal- in Greek Tantalos, name of a legendary king, “the sufferer’: (TANTALIZE), TANTALUS. 6. Perhaps zero-grade form *tla- in Greek Atlas (stem Atlant-), name of the Titan supporting the world: ATLANTIC, ATLAS. 7. Suffixed zero-grade form *tl-é- in Germanic *thulén in Old English tholian, to suffer, endure: THOLE. 8. Suf- fixed zero-grade form *tl-to- in Latin ldtus, “carried, borne,” used as the suppletive past participle of ferre, to bear (see bher-'), with its compounds: ABLATION, COL- LATE, DILATORY, ELATE, ILLATION, LEGISLATOR, OB- LATE], PRELATE, PROLATE, RELATE, SUPERLATIVE, TRANSLATE. 9. Suffixed zero-grade form *tl-d- in San- skrit tuld, scales, balance, weight: TAEL, TOLA. 10. Nasal- ized zero-grade form *tl-n-a- in Latin tollere, to lift: EXTOL. [Pok. 1. éel- 1060.] tem-. Also teme-. To cut. I. Form *tema-. Nasalized form *t(e)m-n-a- in Greek temnein, to cut: TMESIS, TOME, -TOME, -TOMY; ANATOMY, ATOM, DIATOM, DICHOTOMY, ENTOMO-, EPITOME. II. Form *tem-. 1. Suffixed form *tem-lo- in Latin templum, temple, shrine, open place for observation (augury term < “place reserved or cut out”), small piece of timber: TEMPLE!, TEMPLE’; CONTEMPLATE. 2. Extended root *tem-d- becoming *tend- in o-grade suffixed (iterative) form *tond-eyo- in Latin tondére, to shear, shave: TONSURE. [Pok. 1. tem-, tend- 1062.] teme-. Dark. Suffixed form *tema-s-. 1. Latin temere, blindly, rashly: TEMERARIOUS, TEMERITY. 2. Suffixed form *temas-rd- in Latin tenebrae (plural), darkness: TENEBRAE, TENEBRIONID. [Pok. tem()- 1063.] temp-. To stretch. Extension of ten-. 1. Possibly Latin tempus, temple of the head (? where the skin is stretched from behind the eye to the ear): TEMPLE?. 2. Zero-grade form *tmp- perhaps in: a. Persian taftan, to weave (the
12204:•  j.  tamas-äSra-  Adj.  'der  Finsternis enstamrat' :  lfm  ahüm  . .  yim  t>maahatti^m 'r?m  t^manhtm  V.5.63,  JÄ  76;  —  daZ- vanam  mainyavanam  •ra«(T»(  V.  <?.  80;  Y't
25630:tamas^  yä  armaitis  (sd.)  Izäcä  Y.  4^. zT.  verwendet  Y.42-4.  a)  im  jAw.: pas^aSa  at^m  yö  ahurB . .  aoi  'une  urvatma (sd.)  daaayaü  P-S^;  —  lältm  *ddham 'vätam    aiaonS   *irlrihanahe   P,  24;  35;
```


## [2026-10-15T02:44:56.750Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E \"^[^ ]{0,4}\\s*t[^ ]{0,3}mah- ?n?|Finsternis\" BRT.txt | head -20; grep -n -E \"t.?q.?[θ8O]ra|tq&ra|tqOra\" BRT.txt | head"
}
```


### [2026-10-15T02:44:57.763Z] TOOL RESULT

```
3076:Finsternis  hinab"  V. /*j.  30;  —    mit  Dat.:
4249:raolatfhqm  (näml.  ayan)  heUst  der  30. Monatstag;  S./.30;  vgl. 2.30,  Y.  16', 6;  — auch  ohne  raoc' :  pancaca  kaptailJm  paittl- hahyehe  (sd.)  xsa^rake  vairyehe  'ranqm A.j.g;  10.  b)  'ra  hmä  'die  anfangs - lose  Finsternis' :  täirlm  gama  frabarat  yg nars  drvatö  urva  'raih'a  tjmShva  nida^at H.2.33.
12189:tvmah-
12202:•  j.  Mmaohaena-  Adj.  (fem.  '«f-)  'aus Finsternis  bestehend,  finster*:  Ism  ähUm.. yim  .  .  •tarn  t?masairjm  t^tnanhim  V.  5. 63,  /(?.  76;    —    drujim  yqm  .  .  'nun  Yt.
12204:•  j.  tamas-äSra-  Adj.  'der  Finsternis enstamrat' :  lfm  ahüm  . .  yim  t>maahatti^m 'r?m  t^manhtm  V.5.63,  JÄ  76;  —  daZ- vanam  mainyavanam  •ra«(T»(  V.  <?.  80;  Y't
12207:•  j-i  g-  t^mah-  n.  i)  'Finsternis,  Dunkel', Sing,  und  Plur.:  ks  kvSpä  raochslä  (sd.) dät  'mhs<ä  Y.  44.5; — ydisra  nSit  xsapa nSii  °ma  Yt  10.50;  —  dartgSm  3ys(sd.) 'matjAs  Y.JJ.30;  —  mihr^m  ..'manbääa^^ Jiyäurum  ". .  den  im  Dunkel"  wachsamen" Yt  io.  141;  —  'mauAqm  vä  *aiwi^ati (sd.)  V. A4;  —  paitiltJOe  'maakqm  Y.
```


## [2026-10-15T02:45:00.619Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E \"'dunkel\" BRT.txt | head -20; grep -n -E \"\\b(tm|tm')\\b.*(hell|Hölle|دوزخ)\" SOD_pages.txt | head; grep -n -i -E \"\\bhell\\b\" SOD_pages.txt | head -20"
}
```


### [2026-10-15T02:45:01.013Z] TOOL RESULT

```
3135:•  j.  a-x£acna-  Adj.  'dunkelfarbig':  ansö °nS  Aog.  73;  —  gavqm  °nanqm  V.  22. 4,
12214:•  j.  tamah'ya-  Adj.  'dunkel',  neutr.  Flur. 'Dunkelheit':  {anlari)  raelahe  nOit  antar? (sd.)  'mähe  (APn.)"  ii.68.
12235:•  j.  t^Oxya-  i)  Adj.  (fem.  yä-)  'dunkel, finster':  °fyam  aipi  xsapanim  Yi.  14.  13; —  'ryasäi  (GSf)'>  kala  xsafnS  "auch in  finstrer  Nacht"  Yt.  1^31,  ib'.  10;  — xfapa  vä  *'ryä  (GSf,)"  aipi.dziqnaraya YL//.  4.         3)  n.  'Dunkel'  (nur  Ableit).
13489:•  j.  dasgra-  Adj.,  Beiwort  von  Pferd und  Rind,  wohl  Farbenbezeichnung,  etwa 'dunkelfarbig* ".
3135:  /tarn/ tm-             hell       Av. tzmah-\
3135:  /tarn/ tm-             hell       Av. tzmah-\
3886:  Ouz/we o/ the)woisl hell                                16 "prYs'kmync S                    ^Ji^s* < j*&^M^
31381:                                                                     hell
37524:                               Thus, entry 6 with the English "{name of the) worst hell" is represented in the
37525:                               Index by "worst hell"; "(of) god" in entry 2574, "(from) god" in 2597 and "(name
38481:  having the same mind 1902             hell      9588
39966:worst hell 6                                                                   Zurvan    2336, 11415
```


## [2026-10-15T02:45:03.256Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 12228,12240p BRT.txt | cut -c1-500; grep -n -E \"^\\s*9588|9588 \" SOD_pages.txt | head; awk 'BEGIN{RS=\"\\f\"} {n++} /9588/ {print n-1}' SOD_pages.txt | head"
}
```


### [2026-10-15T02:45:03.690Z] TOOL RESULT

```
£.  tu:  I.  unter  la-  und  onter  t%wa:
g.  ga^  ISi  Y.  43.  T :  lies  gaiJSi.
j.  liahrS  P.  5*;  lies  larö.
•  j.  tfi^-ra-  n.,  PlUr.  'Dunkelheit':  upa.- /laxiurusu  (sd.)  'raf/u  V.  7.  79,  *N.  6fi  ■>.
KompA.;  Ableit  —  Aus  ar.  'lait-lra-,  %  42, Hbu.  IFAni.  //.  46').  —  ai.  vgl.  lanüsra-  n.j np.  tärl).  —  Pü.:  tSrik.  —  "I  Hds.  tiAr'.  — >)  Falsch  KZ.  33,  464.  —  3)  Kann  auch  auf BT.  *lansra-  gehen.
•  j.  ti^'d-rö. JUnah- '^  Adj.  'der  nach  dem Dunkel  verlangt,  das  Dunkel  liebt':  'änS (NSm.)')  ya>,a  läyus'  ..  'änO  (NSm.)« ydka  disul  V.  13.  41 .
Pü.:  lärti  iämai.  —  D  Var.  'An*.  —  »)  Nach der  n-Dekl.,  S  j8fi  vgl.  haema^anfm.
•  j.  t^Oxya-  i)  Adj.  (fem.  yä-)  'dunkel, finster':  °fyam  aipi  xsapanim  Yi.  14.  13; —  'ryasäi  (GSf)'>  kala  xsafnS  "auch in  finstrer  Nacht"  Yt.  1^31,  ib'.  10;  — xfapa  vä  *'ryä  (GSf,)"  aipi.dziqnaraya YL//.  4.         3)  n.  'Dunkel'  (nur  Ableit).
Ableit.  —  Ableit  an»  /riSra-.—  Pü.:  tärti.— I)  Nach  der  (-Dekl.;  s.  anderseits  ktU<U.p<ü- manynm  und  ^^oitumaAyint.  Vgl.  den  Unter- schied iwiichen  ai.  ianyäh  und  jAw.  kainyS AP.,  sowie  S  408.  —  »)  So  J 10.
•  j.  biSrySvant-  m.  EN.  eines  Ungläu- bigen, den  Vlitäspa  besiegt:  .  .jiazata  . . viitasps . .  yat  bavani  aiwi.vanyä  'vanttm dusdaimm  Yt.5. 109;  5.31.
'/jiiyoii'ai/- Adj. 'lenebtosns'»).  —  ■)  o  »uYt. 5;  s.  auch  J  10  m  Yt  19.  87.  —  »)  Eine  An- spielung auf  dieTan/i-a-Fhilosophie  der  Inder fso  JK.  Zar.  210  No.  4)  vermag  ich  in  dem Namen    nicht    zu  erkennen;    s.  auch  zu  gan.
dby  Google
6S>
31378:         GMS 864; BBB 579; KG 585; STi 36.14; Sund.             9588 tm-     B, M, C                                    £ jja
454
558
```


## [2026-10-15T02:45:09.486Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 31370,31390p SOD_pages.txt; awk 'BEGIN{RS=\"\\f\"} NR==455' SOD_pages.txt | head -5; awk 'BEGIN{RS=\"\\f\"} NR==455' SOD_pages.txt | grep -n -E '^\\s*\\[pdf|Page|^ *3[0-9][0-9] *$' | head; sed -n 3130,3138p SOD_pages.txt"
}
```


### [2026-10-15T02:45:09.956Z] TOOL RESULT

```
       593; MSP b76                                             9587 tqwst-      C                                    j^Ji
                                                                      t(a)kust    ©pt. st. & pt. inf. =»tkws-
9574 tyt}y B                                       **--j«j»j
     tayate (tyty(y), tytk, tyty) ©pp.                               Go)look
     entered                                                         C2,tk(i>wsd>n
                                                                           31V16, trans, pret. tqwst}r, STii 2.9;
                                                                                   BSTi 168, 224
       VJ 53b; BSTBL, Vim. 5, Dhu. 115; TSP 13.4, 16.42;
         GMS 864; BBB 579; KG 585; STi 36.14; Sund.             9588 tm-     B, M, C                                    £ jja
         AoFviii 1981 p218; STii 3.1; BSTi 126, C2,                  tarn ©<Av. tdmah\ Khwarim ©nom. ob -())y;
         31V11, trt\ 22R8                                               loc. -yht -yHhh ace. -w; abl. -}; pi. -t}
                                                                     hell
9575 tytk ■* tyt}y
                                                                     GMS 267, 938, 1168 n 1; TSP; VJ P120t SCE p72;
9576 tyty C =» tyt>y                                                   STii 10.43; BSTBL, Vim. 142; Intox. 4, Padm.
9577 tyty(y) C, M =» tyt>y                                             18; Frag. Len. pi 10; Hen. Tales. 469.9, 480.28;
9578 tyw                                   (u^^^)y                     GMS 1168, 1177, 1181, 1183, 1184*, STi 9.6, C2,
     t(o)xu ©2sg. pers. pron. nom.                                     51V26

       you, thou                                                9589 tmV
                                                                      body C                                              j
 387

        to/axm, taxm ©<Av. taoxman-         ©nom. gen. -y;               Dhu. 87, Dhy. 53, 215, 338, 367; Frag. Len. 60.6;
          abl. -} =»txm-, twxmy                                         GMS 662; pt. inf. tk*ws>t, TSP 17.196, GMS 551;
        seed, descendent, family                                        Bailey. Prolexis. 50
1: 387

                                                                      xxxi
  2) HI Voiceless dental stop < *f:                              /yaw/       yv          cow
                                                                 /patyos/    ptYws-      hear        Av. gav-
                                                                                                     *pati-gausa-
  /tarn/ tm-             hell       Av. tzmah-\
                                    Skt. tamas                   /Pay/       ^r-         god         OP to^a-
  /marti/     mrti        man           OP martiya-            *et *xl.
                                                               III) The voiceless spirants //, #, x/ < Olr. spirants /*/,
```


## [2026-10-15T02:45:12.679Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; for p in 456 511 544; do python3 tools/ref_page.py BQT:$p 2>&1 | head -60; echo =========; done"
}
```


### [2026-10-15T02:45:13.054Z] TOOL RESULT

```
Exit code 1
no scan of BQT covers printed page 456 (see 'scans' in refs_online.json)
(eval):1: ======== not found
```


## [2026-10-15T02:45:15.941Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for L in 674 676 678; do echo \"== leaf $L\"; awk -v n=$((L+1)) 'BEGIN{RS=\"\\f\"} NR==n' BQT_v1_pages.txt | head -8; done; for L in 728 731 734; do echo \"== leaf $L\"; awk -v n=$((L+1)) 'BEGIN{RS=\"\\f\"} NR==n' BQT_v1_pages.txt | head -5; done; for L in 0 1 2 3; do echo \"== v2 leaf $L\"; awk -v n=$((L+1)) 'BEGIN{RS=\"\\f\"} NR==n' BQT_v2_pages.txt | head -5; done"
}
```


### [2026-10-15T02:45:16.802Z] TOOL RESULT

```
== leaf 674
پیل معلق در عوا
یل معلق درد هو کناب اژابیباهد
یی سه بر وزن زیلو ؛چویی .که بدان
مسواگ کنند وعریان اراك خوانند - و بار درخت
ارالك را نز گفته‌اند .
بیلو ) بفتح ثالت بر وژن بینوا ؛ دارو
فروش وعطار باشدا .
پیلو ار ۲ ت بسکون ثالث بروزن‌یشکاره
== leaf 676
پیوسته گری
شو سته گری فوند کرد
و موافقت نمودن را گویند.
وکاف فارسی » بمعنی عروس باشد ؛ و بنمثانی‌هم
درست است۷ ۰
بو گانی با کاف فارسی بر وزث
خبوشانی(۱) ۰ عروسی را گویند؟ .
منصن - واتصال؟ - وخویش وتبار باشد. وبمعنی
== leaf 678
است - و بیمنی که باکاف مکوراء تممال‌میشود .
همجو*وافف باش‌تا نیفتی» و#برخیز تابرویم *عنی
واقف باش که نیفتی و برخیز که برويم و امثال
اینها(۱) .
اب ببکون بای ابجد . نافتن
هر چیز که نورانی و ررشن باشد حمچو: فزوغ
و پرتوآفتاب وشمع‌وچراغ ومانندآن۱ حبمعنی
چرخ وینج هم هست که در طناب و کمند وزلف
== leaf 728
کوبندا ‏ و بمعنی خوردلی وآذوقه ورأتب‌هم
آمده است - و بمعتی‌پیمانه هم هست - و نقاه
بر وزن شراره هم عیگویند .
ب‌- بنم هردو تای قرشت و سکون
هر دو غن نقطه دار . چیزی باه مالند کله
== leaf 731
اوح
ده » بفتح اول و سکون ثانی و دال
بی فقطهٌ مفتوح . بلفت بربرکشنیز را کوشد »
وآن دستنیی باشد که‌بشتردرآشهای بمار کنند,
و بعربی کژبیمخوانندا .
== leaf 734
تکیز
اوواحت
کفده اند - وبکسراول لقمه و بارمای از هرچز
باشد ۱ چنانکه کویند *«فلانی چیز را نکه تکه
کرد » » یمنی پاره پاره ساخت ۴ .
== v2 leaf 0

== v2 leaf 1
                                         ‫‪7‬‬

                          ‫رن‪۳‬‬
    ‫نات‬
      ‫ا م‬
== v2 leaf 2
                   ‫م‬ ‫و‬
‫نآکو سخنیم بیاموزد مرا‬
                       ‫د‬ ‫د‬ ‫ل‬ ‫ج‬ ‫م‬ ‫ة‬ ‫چ‬ ‫ا‬ ‫ی‬ ‫د‬
‫على ‪۰‬‬             ‫بند گر دا ند ‪۰‬‬                       ‫‪۳‬‬      ‫‪۳7‬‬

== v2 leaf 3
                                                     ‫‪ar‬‬
                                     ‫مااضحاذفی‪‎‬‬
 ‫است‪‎‬‬    ‫و رساله‌هابی استفاده شده‬   ‫نیز ( از ‪5‬‬    ‫در محلد دوم (وطماً مجلد سوم‬
```


## [2026-10-15T02:45:21.311Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} {n++} /tamah|təmah|temah|tąθra|tqθra|tathra|târ|tārīk|târîk|tārik|tīrak|tîrak/ {print n-1\": \"substr($0,1,0)}' BQT_v1_pages.txt BQT_v2_pages.txt | head -30; grep -n -E 'tamah|təmah|temah|tqOra|târ[iî]k|tār[iī]k|tārīg|tîrak|tīrak|tîra' BQT_v1_pages.txt BQT_v2_pages.txt | head -30"
}
```


### [2026-10-15T02:45:21.898Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-15T02:45:23.483Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E 'tam|tār|tar|tir' BQT_v1_pages.txt | head -30; echo; grep -c '' BQT_v1_pages.txt"
}
```


### [2026-10-15T02:45:23.899Z] TOOL RESULT

```
32486
```


## [2026-10-15T02:45:28.463Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; ls pageimg | head; ls ocr; ls ocr/BQT | head -50; for L in 677 678 679 680 681 682; do echo \"== leaf $L\"; awk -v n=$((L+1)) 'BEGIN{RS=\"\\f\"} NR==n' BQT_v1_pages.txt | grep -n -E '^ *(تار|تم|تاریک|تیره)|۴۵|456|۴۵۶' | head; done"
}
```


### [2026-10-15T02:45:29.246Z] TOOL RESULT

```
Permissions Size User   Date Modified Name
.rw-r--r--   60k sfmqrb 14 Oct 22:19  bqt_v3_p150-150.png
.rw-r--r--   51k sfmqrb 14 Oct 22:19  bqt_v3_p600-600.png
.rw-r--r--   75k sfmqrb 14 Oct 22:19  bqt_v4_p150-150.png
.rw-r--r--   41k sfmqrb 14 Oct 22:19  bqt_v4_p500-500.png
.rw-r--r--   55k sfmqrb 14 Oct 22:19  bqt_v5_p8-008.png
.rw-r--r--   42k sfmqrb 14 Oct 22:19  bqt_v5_p30-030.png
.rw-r--r--   49k sfmqrb 14 Oct 22:19  bqt_v5_p150-150.png
.rw-r--r--   44k sfmqrb 14 Oct 22:19  bqt_v5_p250-250.png
.rw-r--r--   79k sfmqrb 14 Oct 22:19  irn_p100-100.png
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
Permissions Size User   Date Modified Name
.rw-r--r--  368k sfmqrb 14 Oct 22:19  0001.png
.rw-r--r--  1.7k sfmqrb 14 Oct 22:19  0001.txt
.rw-r--r--  534k sfmqrb 14 Oct 22:19  0049.png
.rw-r--r--  2.7k sfmqrb 14 Oct 22:19  0049.txt
.rw-r--r--  190k sfmqrb 14 Oct 22:30  0143.jpg
.rw-r--r--   576 sfmqrb 14 Oct 22:30  0143.vision.txt
.rw-r--r--  202k sfmqrb 14 Oct 22:30  0479.jpg
.rw-r--r--   444 sfmqrb 14 Oct 22:30  0479.vision.txt
.rw-r--r--  205k sfmqrb 14 Oct 22:30  0480.jpg
.rw-r--r--   849 sfmqrb 14 Oct 22:30  0480.vision.txt
.rw-r--r--  2.6k sfmqrb 14 Oct 22:19  31.vision.txt
.rw-r--r--  1.5k sfmqrb 14 Oct 22:19  58.vision.txt
.rw-r--r--  1.9k sfmqrb 14 Oct 22:19  70.vision.txt
.rw-r--r--  257k sfmqrb 14 Oct 22:19  71.png
.rw-r--r--  1.5k sfmqrb 14 Oct 22:19  71.vision.txt
.rw-r--r--  1.6k sfmqrb 14 Oct 22:19  72.vision.txt
.rw-r--r--  1.1k sfmqrb 14 Oct 22:19  103.vision.txt
.rw-r--r--  521k sfmqrb 14 Oct 22:19  171.png
.rw-r--r--   806 sfmqrb 14 Oct 22:19  171.vision.txt
.rw-r--r--  527k sfmqrb 14 Oct 22:19  172.png
.rw-r--r--  1.3k sfmqrb 14 Oct 22:19  172.vision.txt
.rw-r--r--  482k sfmqrb 14 Oct 22:19  180.png
.rw-r--r--  1.3k sfmqrb 14 Oct 22:19  180.vision.txt
.rw-r--r--  510k sfmqrb 14 Oct 22:19  181.png
.rw-r--r--  1.2k sfmqrb 14 Oct 22:19  181.vision.txt
.rw-r--r--  538k sfmqrb 14 Oct 22:19  216.png
.rw-r--r--  1.1k sfmqrb 14 Oct 22:19  216.vision.txt
.rw-r--r--  1.1k sfmqrb 14 Oct 22:19  220.vision.txt
.rw-r--r--  512k sfmqrb 14 Oct 22:19  333.png
.rw-r--r--  1.3k sfmqrb 14 Oct 22:19  333.vision.txt
.rw-r--r--  528k sfmqrb 14 Oct 22:19  436.png
.rw-r--r--  1.4k sfmqrb 14 Oct 22:19  436.vision.txt
.rw-r--r--   865 sfmqrb 14 Oct 22:19  460.vision.txt
.rw-r--r--  2.0k sfmqrb 14 Oct 22:19  509.vision.txt
.rw-r--r--  669k sfmqrb 14 Oct 22:19  733.png
.rw-r--r--  1.2k sfmqrb 14 Oct 22:19  733.vision.txt
.rw-r--r--  1.5k sfmqrb 14 Oct 22:19  794.vision.txt
.rw-r--r--  727k sfmqrb 14 Oct 22:19  829.png
.rw-r--r--   981 sfmqrb 14 Oct 22:19  829.vision.txt
.rw-r--r--  625k sfmqrb 14 Oct 22:19  902.png
.rw-r--r--  1.7k sfmqrb 14 Oct 22:19  902.vision.txt
.rw-r--r--  620k sfmqrb 14 Oct 22:19  1024.png
.rw-r--r--  1.7k sfmqrb 14 Oct 22:19  1024.vision.txt
.rw-r--r--  1.3k sfmqrb 14 Oct 22:19  1074.vision.txt
.rw-r--r--  584k sfmqrb 14 Oct 22:19  1085.png
.rw-r--r--  1.1k sfmqrb 14 Oct 22:19  1085.vision.txt
.rw-r--r--  330k sfmqrb 14 Oct 22:19  1092.jpg
.rw-r--r--  2.6k sfmqrb 14 Oct 22:19  1092.vision.txt
.rw-r--r--  542k sfmqrb 14 Oct 22:19  1187.png
== leaf 677
== leaf 678
== leaf 679
== leaf 680
== leaf 681
== leaf 682
7:تار بروزن مار » تار موی وتار آبریشم
19:تار ات - بر وزن سادات » بمعنی اخت
31:تار تار س با نای قرشت بروزن‌کارزار ؛
35:تار چو ب۱"4- بر وزن مارچوبه" نام
38:تارخ نم لك وسکون خای‌شله
```


## [2026-10-15T02:45:33.592Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; cat ocr/BQT/0480.vision.txt | head -5; awk 'BEGIN{RS=\"\\f\"} NR==683' BQT_v1_pages.txt | head -40; for L in 735 736 737 738 739 740; do echo \"== leaf $L\"; awk -v n=$((L+1)) 'BEGIN{RS=\"\\f\"} NR==n' BQT_v1_pages.txt | grep -n -E '^ *(تم|تمر|تمب|تمو)' | head -5; done"
}
```


### [2026-10-15T02:45:34.413Z] TOOL RESULT

```
[BQT vol.1 printed p.480 = archive.org borhan-ghate-v1 leaf n706; read from the page image]
ترازو ۱ - معروف است، و آن آلتی باشد که چیزها را بدان وزن کنند - و نام برج میزان هم هست که از جملهٔ دوازده برج فلکی است ۲ - و عدل و عدالت را نیز گویند و بمعنی ادراک و درک هم آمده است.
Footnote 1: ۱ - پهلوی tarâzûk، ایرانی باستان ☼ tarâzu = ☼ tara - âzu : ☼ tara از سانسکریت tulati، tulya، âz، az از سانسکریت aj (راهنمایی کردن، راندن، پیش‌بردن)، «نیبرگ ۲۲۳». رک: مزنا.
Footnote 2: ۲ - = خوارزمی: ترازك = عربی: میزان. برج هفتم از بروج دوازده‌گانه «گاه‌شماری ص ۲۰۳».
هم‌آمده است که مشثق از ریختن باشده .
تاخیره - بر وزنتاجیره» خت‌ولالع
و سرتوشت را گوبند - و بمعتی اصیب و قسمت
وآنجه برآن زاشد و بر آ ند جم هست چنانکه
کویشد «تاخیر* نو چنین بود» به‌نی طالع‌توچنن
بود ویر آن زادی وبرآعدی -
تار بروزن مار » تار موی وتار آبریشم
وتار ساز وامثال آن باشد٩‏ - و ان بافن دگان
که شض‌بو داست-- وتیرموتاريكرانز گویند؟ -
و بمعنی فرق سر و تاراسر ومیان سرهم صست-
و نام درختیست در هندوستان شبیه‌بدرخت خرها
آوآیی ازآن حاص لکنند که نشا؛ شراب دهد -
و بمعنی ریزه وپاره همآمده است چه تارتار بعنی
ریزه ریزه وپارء پاره .
ترا » بر وژن خارا » ستاره را کوینه
وجربی کو کب‌خوانند؟ ۰
.سار ای بر وزن‌فاراب » نام‌قریه‌است
در سه فرسشگی بنارا ۴ .
تار ات - بر وزن سادات » بمعنی اخت
وتاراح واهب (۱) وغارت وبردن‌مال مردم‌باشره ۱
واز هم جدا کردنرا نیز گویند .
۲ تاراج ‏ با جیم » بر وزن ومعنی‌تارات
است که نهب (+) و غلرت ٩‏ - وازهی‌جدا کردن
(۱) چش : نهیب ؛
-- بیع
باشثه .
از اس ه بسکون سین بی نقطه»بمعنی
زیر دست و تابع خودساختن - و رام کرداتیدن
اسان وحیوان دیگر باشد .
تاد ان بسکون نون » بسنی یره
تار تار س با نای قرشت بروزن‌کارزار ؛
بمعتی پارم پاره وریزه ریزه و ره ذره‌باشد۸ ,
."ار نلگ؟ ه بنتح‌تاونون وسکون‌کاف
عذکبوت را گوند .
تار چو ب۱"4- بر وزن مارچوبه" نام
داروی است که در دواها بکار بر لد» و آتراحلون
حم خوانند .
تارخ نم لك وسکون خای‌شله
دار » بزبان پپلوی نام آزّر ٩٩‏ بت تراش است .
وبسفی گویند بقتح تالث است ونم پدر ابراهیم
== leaf 735
== leaf 736
== leaf 737
== leaf 738
== leaf 739
4:تماجح نم اول بر وزن اعاج ۰
7:تماخره - بتح اول وخای نقطه‌دار
== leaf 740
16:تمغو در با زای هوز بر وزن ححفوظ»
18:تملول - با لام بروزن مقبول» رستنیی
22:تملیت ‏ با تای فرشت بر وزن تمليكه
29:تمنده بر وزن رونده . کم زیالرا
39:تمودار٩‏ ۰« بر وزن سبودان » جمم
```


## [2026-10-15T02:45:40.688Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for L in 736 737 738; do echo \"== leaf $L\"; awk -v n=$((L+1)) 'BEGIN{RS=\"\\f\"} NR==n' BQT_v1_pages.txt | grep -n -E 'تم' | head -8; done; mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/bqt500; cd /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/bqt500; curl -sL -o leaf682-500.jpg 'https://archive.org/download/borhan-ghate-v1/page/n682_w1400.jpg'; file leaf682-500.jpg"
}
```


### [2026-10-15T02:45:42.610Z] TOOL RESULT

```
== leaf 736
== leaf 737
19:۴ - در کناب ار۵105) و رك : تمشده . ۵ رکه : تلنگی و له .
== leaf 738
55:باهتمام احمدآعتی ۱۹۸۸ ص4۹- 4۷*.
leaf682-500.jpg: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, baseline, precision 8, 2479x3508, components 1
```


## [2026-10-15T02:45:44.359Z] TOOL CALL #21: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/bqt500/leaf682-500.jpg"
}
```


### [2026-10-15T02:45:44.518Z] TOOL RESULT

```

```


## [2026-10-15T02:45:44.513Z] INPUT

[Image: original 2479x3508, displayed at 1413x2000. Multiply coordinates by 1.75 to map to original image.]


## [2026-10-15T02:45:50.550Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/bqt500; curl -sL -o leaf737-500.jpg 'https://archive.org/download/borhan-ghate-v1/page/n737_w1400.jpg'; file leaf737-500.jpg; python3 -c \"\nimport json;d=json.load(open('/home/sfmqrb/git/rishe-private/data/verification/sources/refs_online.json'))['BQT'];print(d['url'])\"; ls /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT | sed -n 50,200p | tr '\\n' ' '"
}
```


### [2026-10-15T02:45:52.479Z] TOOL RESULT

```
leaf737-500.jpg: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, baseline, precision 8, 2479x3508, components 1
https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.com (links from farhangoadabeirani.blogsky.com post-482): vol 3 https://s3.picofile.com/file/8230740968/borhane_ghatee_jelde_3.pdf.html (ش–ل, Ibn Sina 2nd ed. 1342, 721 pp), vol 4 https://s6.picofile.com/file/8230741184/borhane_ghatee_jelde_4.pdf.html (م–ی, 553 pp), vol 5 https://s3.picofile.com/file/8230741300/borhane_ghatee_jelde_5.pdf.html (تعلیقات, Amir Kabir 5th pr. 1376, 293 pp). Same set behind login on ketabnak.com/book/55304-55307 and /58249.
.rw-r--r--  330k sfmqrb 14 Oct 22:19  1092.jpg .rw-r--r--  2.6k sfmqrb 14 Oct 22:19  1092.vision.txt .rw-r--r--  542k sfmqrb 14 Oct 22:19  1187.png .rw-r--r--  1.6k sfmqrb 14 Oct 22:19  1187.vision.txt .rw-r--r--  394k sfmqrb 14 Oct 22:19  1219.png .rw-r--r--  3.6k sfmqrb 14 Oct 22:19  1219.txt .rw-r--r--   818 sfmqrb 14 Oct 22:19  1219.vision.txt .rw-r--r--  435k sfmqrb 14 Oct 22:19  1223.png .rw-r--r--  4.5k sfmqrb 14 Oct 22:19  1223.txt .rw-r--r--  447k sfmqrb 14 Oct 22:19  1225.png .rw-r--r--  4.4k sfmqrb 14 Oct 22:19  1225.txt .rw-r--r--  1.3k sfmqrb 14 Oct 22:19  1225.vision.txt .rw-r--r--  385k sfmqrb 14 Oct 22:19  1226.png .rw-r--r--  3.7k sfmqrb 14 Oct 22:19  1226.txt .rw-r--r--  430k sfmqrb 14 Oct 22:19  1230.png .rw-r--r--  3.7k sfmqrb 14 Oct 22:19  1230.txt .rw-r--r--  467k sfmqrb 14 Oct 22:19  1237.png .rw-r--r--  4.6k sfmqrb 14 Oct 22:19  1237.txt .rw-r--r--  1.0k sfmqrb 14 Oct 22:19  1237.vision.txt .rw-r--r--  448k sfmqrb 14 Oct 22:19  1252.png .rw-r--r--  3.7k sfmqrb 14 Oct 22:19  1252.txt .rw-r--r--   611 sfmqrb 14 Oct 22:19  1252.vision.txt .rw-r--r--  151k sfmqrb 14 Oct 22:19  1261.png .rw-r--r--  3.5k sfmqrb 14 Oct 22:19  1261.txt .rw-r--r--  367k sfmqrb 14 Oct 22:19  1266.png .rw-r--r--  3.5k sfmqrb 14 Oct 22:19  1266.txt .rw-r--r--  1.7k sfmqrb 14 Oct 22:19  1266.vision.txt .rw-r--r--  391k sfmqrb 14 Oct 22:19  1267.png .rw-r--r--  3.6k sfmqrb 14 Oct 22:19  1267.txt .rw-r--r--  1.3k sfmqrb 14 Oct 22:19  1267.vision.txt .rw-r--r--  391k sfmqrb 14 Oct 22:19  1270.png .rw-r--r--  3.8k sfmqrb 14 Oct 22:19  1270.txt .rw-r--r--  391k sfmqrb 14 Oct 22:19  1272.png .rw-r--r--  3.8k sfmqrb 14 Oct 22:19  1272.txt .rw-r--r--  409k sfmqrb 14 Oct 22:19  1275.png .rw-r--r--  3.2k sfmqrb 14 Oct 22:19  1275.txt .rw-r--r--  158k sfmqrb 14 Oct 22:19  1279.png .rw-r--r--  3.3k sfmqrb 14 Oct 22:19  1279.txt .rw-r--r--  170k sfmqrb 14 Oct 22:19  1280.png .rw-r--r--  3.9k sfmqrb 14 Oct 22:19  1280.txt .rw-r--r--   741 sfmqrb 14 Oct 22:19  1280.vision.txt .rw-r--r--  389k sfmqrb 14 Oct 22:19  1287.png .rw-r--r--  3.8k sfmqrb 14 Oct 22:19  1287.txt .rw-r--r--  163k sfmqrb 14 Oct 22:19  1294.png .rw-r--r--  3.4k sfmqrb 14 Oct 22:19  1294.txt .rw-r--r--  1.1k sfmqrb 14 Oct 22:19  1294.vision.txt .rw-r--r--  177k sfmqrb 14 Oct 22:19  1296.png .rw-r--r--  4.5k sfmqrb 14 Oct 22:19  1296.txt .rw-r--r--  2.0k sfmqrb 14 Oct 22:19  1296.vision.txt .rw-r--r--  422k sfmqrb 14 Oct 22:19  1297.png .rw-r--r--  3.9k sfmqrb 14 Oct 22:19  1297.txt .rw-r--r--  163k sfmqrb 14 Oct 22:19  1298.png .rw-r--r--  3.4k sfmqrb 14 Oct 22:19  1298.txt .rw-r--r--   91k sfmqrb 14 Oct 22:19  1299.png .rw-r--r--  4.3k sfmqrb 14 Oct 22:19  1299.txt .rw-r--r--   573 sfmqrb 14 Oct 22:19  1299.vision.txt .rw-r--r--  172k sfmqrb 14 Oct 22:19  1300.png .rw-r--r--  4.0k sfmqrb 14 Oct 22:19  1300.txt .rw-r--r--  1.9k sfmqrb 14 Oct 22:19  1300.vision.txt .rw-r--r--  411k sfmqrb 14 Oct 22:19  1302.png .rw-r--r--  3.9k sfmqrb 14 Oct 22:19  1302.txt .rw-r--r--   284 sfmqrb 14 Oct 22:19  1302.vision.txt .rw-r--r--  414k sfmqrb 14 Oct 22:19  1310.png .rw-r--r--  3.8k sfmqrb 14 Oct 22:19  1310.txt .rw-r--r--  185k sfmqrb 14 Oct 22:19  1318.png .rw-r--r--  4.7k sfmqrb 14 Oct 22:19  1318.txt .rw-r--r--  966k sfmqrb 14 Oct 22:19  1319.png .rw-r--r--   420 sfmqrb 14 Oct 22:19  1319.txt .rw-r--r--  101k sfmqrb 14 Oct 22:19  1320.png .rw-r--r--   615 sfmqrb 14 Oct 22:19  1320.txt .rw-r--r--  1.3k sfmqrb 14 Oct 22:19  1320.vision.txt .rw-r--r--  125k sfmqrb 14 Oct 22:19  1328.png .rw-r--r--  2.4k sfmqrb 14 Oct 22:19  1328.txt .rw-r--r--  129k sfmqrb 14 Oct 22:19  1330.png .rw-r--r--  2.9k sfmqrb 14 Oct 22:19  1330.txt .rw-r--r--  122k sfmqrb 14 Oct 22:19  1339.png .rw-r--r--  2.4k sfmqrb 14 Oct 22:19  1339.txt .rw-r--r--   68k sfmqrb 14 Oct 22:45  1346.png .rw-r--r--  2.5k sfmqrb 14 Oct 22:45  1346.txt .rw-r--r--  1.1k sfmqrb 14 Oct 22:45  1346.vision.txt .rw-r--r--  326k sfmqrb 14 Oct 22:19  1357.png .rw-r--r--  2.7k sfmqrb 14 Oct 22:19  1357.txt .rw-r--r--  230k sfmqrb 14 Oct 22:45  1364.png .rw-r--r--  1.5k sfmqrb 14 Oct 22:45  1364.txt .rw-r--r--  342k sfmqrb 14 Oct 22:19  1382.png .rw-r--r--  2.9k sfmqrb 14 Oct 22:19  1382.txt .rw-r--r--  448k sfmqrb 14 Oct 22:19  1385.png .rw-r--r--  3.7k sfmqrb 14 Oct 22:19  1385.txt .rw-r--r--  2.0k sfmqrb 14 Oct 22:19  1385.vision.txt .rw-r--r--  370k sfmqrb 14 Oct 22:19  1439.png .rw-r--r--  3.6k sfmqrb 14 Oct 22:19  1439.txt .rw-r--r--  406k sfmqrb 14 Oct 22:19  1444.png .rw-r--r--  3.8k sfmqrb 14 Oct 22:19  1444.txt .rw-r--r--  393k sfmqrb 14 Oct 22:19  1445.png .rw-r--r--  3.7k sfmqrb 14 Oct 22:19  1445.txt .rw-r--r--  1.8k sfmqrb 14 Oct 22:19  1445.vision.txt .rw-r--r--  168k sfmqrb 14 Oct 22:19  1452.png .rw-r--r--  3.9k sfmqrb 14 Oct 22:19  1452.txt .rw-r--r--  356k sfmqrb 14 Oct 22:19  1453.png .rw-r--r--  3.5k sfmqrb 14 Oct 22:19  1453.txt .rw-r--r--  444k sfmqrb 14 Oct 22:19  1455.png .rw-r--r--  4.4k sfmqrb 14 Oct 22:19  1455.txt .rw-r--r--  385k sfmqrb 14 Oct 22:19  1462.png .rw-r--r--  3.7k sfmqrb 14 Oct 22:19  1462.txt .rw-r--r--  596k sfmqrb 14 Oct 22:19  1463.png .rw-r--r--  3.4k sfmqrb 14 Oct 22:19  1463.txt .rw-r--r--  440k sfmqrb 14 Oct 22:19  1465.png .rw-r--r--  4.2k sfmqrb 14 Oct 22:19  1465.txt .rw-r--r--  465k sfmqrb 14 Oct 22:19  1471.png .rw-r--r--  4.4k sfmqrb 14 Oct 22:19  1471.txt .rw-r--r--  170k sfmqrb 14 Oct 22:19  1472.png .rw-r--r--  4.2k sfmqrb 14 Oct 22:19  1472.txt .rw-r--r--  429k sfmqrb 14 Oct 22:19  1481.png .rw-r--r--  3.9k sfmqrb 14 Oct 22:19  1481.txt .rw-r--r--  155k sfmqrb 14 Oct 22:19  1488.png .rw-r--r--  3.7k sfmqrb 14 Oct 22:19  1488.txt .rw-r--r--  334k sfmqrb 14 Oct 22:19  1492.png .rw-r--r--  3.1k sfmqrb 14 Oct 22:19  1492.txt .rw-r--r--  179k sfmqrb 14 Oct 22:19  1499.png .rw-r--r--  4.3k sfmqrb 14 Oct 22:19  1499.txt .rw-r--r--   958 sfmqrb 14 Oct 22:19  1499.vision.txt .rw-r--r--  166k sfmqrb 14 Oct 22:19  1502.png .rw-r--r--  4.0k sfmqrb 14 Oct 22:19  1502.txt .rw-r--r--   965 sfmqrb 14 Oct 22:19  1502.vision.txt .rw-r--r--  168k sfmqrb 14 Oct 22:19  1544.png .rw-r--r--  4.0k sfmqrb 14 Oct 22:19  1544.txt .rw-r--r--  163k sfmqrb 14 Oct 22:19  1550.png .rw-r--r--  4.0k sfmqrb 14 Oct 22:19  1550.txt .rw-r--r--  399k sfmqrb 14 Oct 22:19  1563.png .rw-r--r--  4.0k sfmqrb 14 Oct 22:19  1563.txt .rw-r--r--  388k sfmqrb 14 Oct 22:19  1564.png .rw-r--r--  3.8k sfmqrb 14 Oct 22:19  1564.txt .rw-r--r--   797 sfmqrb 14 Oct 22:19  1564.vision.txt .rw-r--r--  426k sfmqrb 14 Oct 22:19  1567.png .rw-r--r--  4.2k sfmqrb 14 Oct 22:19  1567.txt .rw-r--r--  446k sfmqrb 14 Oct 22:19  1571.png .rw-r--r--  4.0k sfmqrb 14 Oct 22:19  1571.txt .rw-r--r--  410k sfmqrb 14 Oct 22:19  1572.png .rw-r--r--  4.0k sfmqrb 14 Oct 22:19  1572.txt .rw-r--r--  1.7k sfmqrb 14 Oct 22:19  1572.vision.txt .rw-r--r--  400k sfmqrb 14 Oct 22:19  1578.png .rw-r--r--  3.9k sfmqrb 14 Oct 22:19  1578.txt .rw-r--r--  2.2k sfmqrb 14 Oct 22:19  1578.vision.txt .rw-r--r--  176k sfmqrb 14 Oct 22:19  1583.png .rw-r--r--  4.3k sfmqrb 14 Oct 22:19  1583.txt .rw-r--r--  2.6k sfmqrb 14 Oct 22:19  1583.vision.txt .rw-r--r--  463k sfmqrb 14 Oct 22:19  1589.png .rw-r--r--  4.4k sfmqrb 14 Oct 22:19  1589.txt .rw-r--r--  178k sfmqrb 14 Oct 22:19  1594.png .rw-r--r--  4.0k sfmqrb 14 Oct 22:19  1594.txt .rw-r--r--  1.1k sfmqrb 14 Oct 22:19  1594.vision.txt
```


## [2026-10-15T02:45:54.220Z] TOOL CALL #23: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/bqt500/leaf737-500.jpg"
}
```


### [2026-10-15T02:45:54.373Z] TOOL RESULT

```

```


## [2026-10-15T02:45:54.369Z] INPUT

[Image: original 2479x3508, displayed at 1413x2000. Multiply coordinates by 1.75 to map to original image.]


## [2026-10-15T02:45:57.721Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/bqt500; curl -sL -o leaf739-500.jpg 'https://archive.org/download/borhan-ghate-v1/page/n739_w1400.jpg'; file leaf739-500.jpg"
}
```


## [2026-10-15T02:45:58.376Z] TOOL CALL #25: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/bqt500/leaf739-500.jpg"
}
```


### [2026-10-15T02:45:59.746Z] TOOL RESULT

```
leaf739-500.jpg: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, baseline, precision 8, 2479x3508, components 1
```


### [2026-10-15T02:45:59.894Z] TOOL RESULT

```

```


## [2026-10-15T02:45:59.890Z] INPUT

[Image: original 2479x3508, displayed at 1413x2000. Multiply coordinates by 1.75 to map to original image.]


## [2026-10-15T02:46:06.034Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/bqt500; for L in 765 766 767 768 769 770 771 772 773 774 775 776; do echo \"== v1 leaf $L\"; awk -v n=$((L+1)) 'BEGIN{RS=\"\\f\"} NR==n' /home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v1_pages.txt | grep -E '^ *تیر' | head -3; done"
}
```


### [2026-10-15T02:46:07.259Z] TOOL RESULT

```
== v1 leaf 765
== v1 leaf 766
== v1 leaf 767
== v1 leaf 768
== v1 leaf 769
== v1 leaf 770
== v1 leaf 771
تیرچرخ - "تیه از کرک ساره
تیر 2 ع ی دزن زیرك» صخیر نیرست
تیر گر دون عم کنابه از آفتاب اسش
== v1 leaf 772
تیرعاهی با میم بروزن نیکخواهی:
تیره۱ س_ پروزن خیره » تاريك و سیاه
== v1 leaf 773
== v1 leaf 774
== v1 leaf 775
== v1 leaf 776
```


## [2026-10-15T02:46:09.744Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/bqt500; curl -sL -o leaf772-500.jpg 'https://archive.org/download/borhan-ghate-v1/page/n772_w1400.jpg'; file leaf772-500.jpg"
}
```


## [2026-10-15T02:46:10.392Z] TOOL CALL #28: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/bqt500/leaf772-500.jpg"
}
```


### [2026-10-15T02:46:11.707Z] TOOL RESULT

```
leaf772-500.jpg: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, baseline, precision 8, 2479x3508, components 1
```


### [2026-10-15T02:46:11.900Z] TOOL RESULT

```

```


## [2026-10-15T02:46:11.896Z] INPUT

[Image: original 2479x3508, displayed at 1413x2000. Multiply coordinates by 1.75 to map to original image.]


## [2026-10-15T02:46:27.587Z] TOOL CALL #29: Bash

```json
{
 "command": "S=/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/bqt500; O=/home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr; cp $S/leaf682-500.jpg $O/BQT/0456.jpg; cp $S/leaf739-500.jpg $O/BQT/0511.jpg; cp $S/leaf772-500.jpg $O/BQT/0544.jpg; mkdir -p $O/BOOK; pdftoppm -f 500 -l 500 -r 150 -png -singlefile /home/sfmqrb/git/rishe-private/EtymologicalDictionary-persian-english.pdf $O/BOOK/500 && ls -la $O/BOOK/500.png\ncat > $O/BQT/0456.vision.txt <<'EOF'\n[BQT vol.1 printed p.456 = archive.org borhan-ghate-v1 leaf n682; read from the page image]\nتار - بروزن مار ، تار موی و تار ابریشم و تار ساز و امثال آن باشد۱ - و تانهٔ بافندگان که شش‌پود است - و تیره و تاریک را نیز گویند۲ - و بمعنی فرق سر و تارک سر و میان سرهم هست ...\nتاران - بسکون نون ، بمعنی تیره و تاریک باشد۷.\nFootnote 1: ۱ - از اوستا ☼ tathra ، قس: هندی باستان tántra (رشته ، طناب) «اشتق ۳۶۹».\nFootnote 2: ۲ - اوستا tathra (تاریک) (از ☼ tamsra ، ☼ tansra): هندی باستان támisra (تاریک) ، پهلوی târ ، کردی târî ، افغانی tôr ، استی taling ، talingä (تارکی، تاریک) tar (کثیف، غمگین)، بلوچی târ ، سریکلی târ ، منجی tarâvi «اشتق ۳۷۰» ، گیلکی târ . رک : تاریک.\nFootnote 7: ۷ - رک: تار.\nEOF\ncat > $O/BQT/0511.vision.txt <<'EOF'\n[BQT vol.1 printed p.511 = archive.org borhan-ghate-v1 leaf n739 (first page of بیان بیستم «در تای قرشت با میم»); read from the page image]\nتم۱ - بفتح اول وسکون ثانی ، آفتی است که در چشم پیدا میشود مانند پرده، و آنرا بعربی غشاوه گویند.\nFootnote 1: ۱ - اوستا temah (تاریکی) ؛ پهلوی tum (پهلوی وندیداد) ، tumīk ؛ هندی باستان támas (تاریکی)، افغانی tôr [tam] (تاریکی) «اشتق ۳۹۲» در کردی بمعنی مه و میغ آمده «دیوان ناصرخسرو ص۶۳۴ ستون۱ و ۶۵۵ ستون۲» و «تما» بزبان قمی بخاریست که از غذا برخیزد «دیوان ناصرخسرو ص۶۵۶ ستون۱».\nEOF\ncat > $O/BQT/0544.vision.txt <<'EOF'\n[BQT vol.1 printed p.544 = archive.org borhan-ghate-v1 leaf n772; read from the page image]\nتیره۱ - بروزن خیره ، تاریک و سیاه فام را گویند - و آب گل آلود را نیز گفته اند.\nFootnote 1: ۱ - ایرانی باستان ☼ tathrya-ka از اوستا tathrya «بارتولومه ۶۵۰» «نیبرگ ۲۲۵» قس: تار، تاریک؛ پهلوی têrak ، افغانی tîra (دخیل) ، بلوچی têragh ، شغنی tér «اشتق ۴۰۷» ، گیلکی tîrae ، فریزندی terä ، یرنی و نطنزی tîrä «ک. ۱ ص۲۹۴» ، لاسگردی tîrâe «ک. ۲ ص۱۹۵».\nEOF\ncd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i 'matmur\\|matamor\\|mattamor' AFA.txt FVQ.txt AFM.txt LKT.txt DEV.txt PHN.txt LAM.txt DOZ.txt SKT.txt HJB.txt WEB_vol1.txt FSD_vol3.txt FSD_vol2.txt KLN_1971.txt 2>/dev/null | cut -c1-400 | head -30"
}
```


### [2026-10-15T02:46:28.646Z] TOOL RESULT

```
Permissions Size User   Date Modified Name
.rw-r--r--   41k sfmqrb 14 Oct 22:46  /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BOOK/500.png
LAM.txt:232:calife, matamore ; d'autres fois le ta est omis, ex : ca-
LAM.txt:690:qu'elle peut occuper : macabre, momie, matamore, sélam,
LAM.txt:1119:(3) Comp. Ottomane : grand siège sans dossier; matamore^ eamocan.
LAM.txt:5182:Matamore. Esp. Ptg : mazmorra. Val. : maçmorra Ptg:
LAM.txt:5183:masmorra, matamorra. Cat : marmorra, massmorra de
LAM.txt:9352:Matamore
DEV.txt:1388:Gaupe.   Est-ce  l'arabe  iC/^  qahha,  vieille  femme,  cour- tisane, qu'on  tire  de  l^^  qahab,  tousser,  par  allusion  au loussement  dont  les  courtisanes  se  servent  pour  attirer  les chalands?  Les  dictionnaires  persans  et  turcs  donnent  aussi , iuk,  x^ï,  qahpè,  qahpè,  dans  le  même  sens;  et  Richard- j|  son ,  AiLaw  »skÂ  qahbè-khaneh ^  ^^  a  brothel  ??
DEV.txt:1697:Matamore.  Silo  pour  le  grain,  ce  Les  Maures  et  les  Arabes, dit  Raynal\  serrent  leurs  grains  dans  des  matamores  ou
DEV.txt:1698:magasins  souterrains   La  forme  des  matamores  ne
DEV.txt:3871:Matamore.
DEV.txt:3892:Mazmorra,  esp.  voy.  Matamore.
DEV.txt:5117:vîLu/  »^j*  pers.  Yoy.  Alchimie,  lu. -j~«  voy.  Astronomie,  lo. U-wàj>y«  voy.  Marcassite. xù-^-iiJ>j«  voy.  Marcassite. lh>,Aj>y«  voy.  Marcassite. <-.^5^  voy.  Markab. ^y9  voy.  Moringe. ^-«  voy.  Moringe. i^y»  voy.  Astronomie,  30. iôj) j«  voy.  Madrague. t_>*xx*«-«  voy.  Mosarabe. »Xss^vj»  voy.  Mosquée. ïy^r^  voy.  Mascarade. Je.'M-ji  voy.  Mistique. liL-j*  vo
PHN.txt:7236:MATAMORE, s. f. (a.)
PHN.txt:7242:tnarra, le portugais matamorra ou masmorra, et ne confondez
PHN.txt:7243:pas le subst. fëm. matamore avec iiatamore, subst. masc, qui
PHN.txt:10714:Matamore, s. f. (a.) sôy
KLN_1971.txt:146698:mattamore, n., a subterranean dwelling or store- 
KLN_1971.txt:146699:house. — F. matamore, fr. Arab. matmura } \ 
WEB_vol1.txt:113768:youue: superintendent or manager of ae | rangements of a hospital, the domestic arrars ‘son, or other institution, p pe a woman attendant or guard in charge of women or children, as 1n an institution. 5’ tron-age (or mat/run-),#. 1. matrons col- ively. ee E the state of being a matron, 3. matronly care or supervision. alt -à L. matronalis, from matrona, a mi’tron-al, a. aep A m
FSD_vol3.txt:17077:groin I < F matamore, c Ar.mefmur.oavem for storing corn 1
```


## [2026-10-15T02:46:32.228Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 1697,1702p DEV.txt | cut -c1-700; sed -n 7236,7246p PHN.txt; sed -n 5178,5190p LAM.txt; sed -n 17074,17080p FSD_vol3.txt | cut -c1-300; grep -n -E 'طمر|tamara|matmura|maimura|ṭmar|tmar' AFA.txt | head; awk 'BEGIN{RS=\"\\f\"} {n++} /137/ && /tamar|matm/ {print n-1}' AFA.txt | head"
}
```


### [2026-10-15T02:46:32.805Z] TOOL RESULT

```
Matamore.  Silo  pour  le  grain,  ce  Les  Maures  et  les  Arabes, dit  Raynal\  serrent  leurs  grains  dans  des  matamores  ou
magasins  souterrains   La  forme  des  matamores  ne
diffère  que  peu  de  celle  de  nos  puits.  5?  C'est  l'arabe 5jj^.Uxfl  maimôra,  fosse  souterraine,  silo.
De  ce  mot  vient  l'espagnol  mazmorra,  cachot,  fosse, prison.  On  peut  voir,  dans  la  Relation  du  sieur  Mouette"^, qui  fut  captif  au  Maroc  de  16-70  à  1681,  la  description de  la  mazmorra  où  on  le  renfermait  la  nuit  avec  les  autres esclaves  :  ^^  C'étaient  de  vrais  silos  creusés  sous  terre  .  .  . on  faisait  descendre  les  esclaves  dans  ce  trou  par  une échelle  de  corde.  ??
Matassins.  Esp.  matachin,  portug.  muchachim ,  ital.  mat- tacino.  M.  Dozy  dérive  ingénieusement  ces  mots  de  l'arabe xzi^^  ouadjh,  visage,  employé  dans  le  sens  de  masque,  d'où
un  verbe  ^^'  tawadjdjah,  se  masquer,  et  enfin  le  parti-
MATAMORE, s. f. (a.)
ijy^ia^ \maimjoûrat\ caveau, nom de lieu dérivé de^^^^ [t^amar]
cacher sous terre. Cellier souterrain , silo dans lequel les Maures258 ' M AU
ont coutume de consener le grain. C'est aussi le nom d'une
sorte de prison où le même peuple enfermait jadis les esclaves
pendant la nuit. — Comparez avec l'arabe l'espagnol iîwiz-
tnarra, le portugais matamorra ou masmorra, et ne confondez
pas le subst. fëm. matamore avec iiatamore, subst. masc, qui
vient de l'espagnol et se dit pour fanfaron, faux brave, mot à
moi 4ueur de Maures {^matamouros, en portugais).
MATRACAT, s. f. (a.)
chien (2), singe etc., Cfr. S/non. Arab* 188 et Chams
' ed-dîn de Damas, p. 275. Cette explication n'est pas
improbable, étant donné la façon cavalière, dont le fran-
çais traite la finale des mots arabes. ( V. Introduction ).
Matamore. Esp. Ptg : mazmorra. Val. : maçmorra Ptg:
masmorra, matamorra. Cat : marmorra, massmorra de
(1) Les Persans ont pris le même mot dans le sens de moquerie, visé
( V. Berge. Dict. Pers-Franç. s. v. ).
(2) V. à ce sujet une plaisante histoire dans Aghâni (I. 257. édition
Salhani ).MATE i6i
SjjUa^ ma\moùra^ fosse souterraine, silo; et aussi pri-
son, de j».U tamar, cacher. « Il y a des criminels que l'on
pend par les pieds sur la bouche d'un puits ou d'une ma-
Matt., aVhr. Matthew
mat'tai-mora, l mat'e-mOr; 2 m&t'a-mOr, n. In Eastern
countries, a cavern or other underground place for storing
groin I < F matamore, c Ar.mefmur.oavem for storing corn 1
Mat 'tan, 1 mat'sn; 2 mftt'an, n. Bib e Chron. xxlli, 17
^ rileb . gift 1 [IK-lft (Heb , gift 1
Mat'ta**nah, 1 mat's-ns; 2 m&t'a-na, n. Bib Num xxl.
```


## [2026-10-15T02:46:36.163Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i -E 'Getreidegrube|unterirdisch|Silo|verbergen|verscharr' AFA.txt | head; grep -n -i 'مطمور\\|طمر' AFM.txt PLA*.txt MON_part2.txt 2>/dev/null | head"
}
```


### [2026-10-15T02:46:36.704Z] TOOL RESULT

```
1754:dafaua »verbergen*' zur Bezeichnung desselben Ausdrucks
5013:Eine unterirdische Grube zum Aufbewahren des Getrei-
5021:146, 2). >Le ble est conserve dans des silos trds profonds,
6023:Voraussetzung; man wollte das Wort mit Ix^ »verbergen**
(eval):1: no matches found: PLA*.txt
```


## [2026-10-15T02:46:38.285Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 5005,5025p AFA.txt; grep -n 'مطمور' MON_part1.txt MON_part2.txt | head -3"
}
```


### [2026-10-15T02:46:38.757Z] TOOL RESULT

```
Aulogie Für !^Ji^. du lelbit aai np^Ky cntitand. iDie Sprache bal in dis
tnalogi* der gTO««n Zahl itr out N loigeluiten Hoppe 1 aagcu . die anprüng-
litht N «alhitlliD. auch KhlieMÜch lolche DoppalunEen gtiogcB . die uiprüag-
Iwh gar knji V esIbitlltD). Alhiap. itabat aoi P^V od. ra|J|liT»; ^ y ^
tii ^•»i Gl. gtoftr. SSO, Die» ADdäiimg liegt bei DeoC^ea be*oDden nahe;
'gt. aaeh tmai. ren^rt au rtddtrt.137
Bildung ist n^tS«!^ Ez« 47« 10 « wo aber wieder die scriptio
plena eigentlich unberechtigt ist.
Eine unterirdische Grube zum Aufbewahren des Getrei-
des ist g.j I u^ Eämil 684, 13. Da . i^ im Altarabischen in
der Bedeutung »aufbewahren" nicht existiert« so ist schon
Ton. Tomeherein die Entlehnung wahrscheinlich. Dafür
spricht femer das Verbum denominaÜTum I4J0 und endlich
findet sich ]^i n^x\i^o wirklich in dieser Bedeutung im Sy-
rischen TOr. {jxAhjf ein Ort im ?ra^ Joljndt lY. 562.)
Vgl. La Sjrie d'aujourd'hui (Tour du monde 1882, I. p.
146, 2). >Le ble est conserve dans des silos trds profonds,
qu*ils savent cacher avec beaucoup d'art** ^).
Hier gehört auch |%^«J »ein Holzstempel, mit dem das
Getreide gestempelt wird** her. Das Wort ist ebenso, wie
f^Y) (^^^ y^ohl in anderer Gegend) entlehnt aus MOSTIH
```


## [2026-10-15T02:46:43.584Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 tools/fetch_source.py --help 2>&1 | head -20"
}
```


### [2026-10-15T02:46:44.063Z] TOOL RESULT

```
Save a web source used during verification, for later cross-checking.

    python3 tools/fetch_source.py <URL> [--note "why it was fetched"]

Downloads the URL, converts the HTML to plain text, stores it as
data/verification/sources/web/<sha1(url)>.txt and appends a line to
data/verification/sources/web/index.jsonl  ({url, file, fetched, bytes, status, title, note}).
Prints the stored path. Re-fetching the same URL within a day is skipped.
```


## [2026-10-15T02:46:48.085Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; for u in \\\n'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/temH-' \\\n'https://en.wiktionary.org/wiki/temere' \\\n'https://en.wiktionary.org/wiki/timeo' \\\n'https://en.wiktionary.org/wiki/ताम्र' \\\n'https://en.wiktionary.org/wiki/tembaga' \\\n'https://en.wiktionary.org/wiki/tombac' \\\n'https://en.wiktionary.org/wiki/تم' \\\n'https://en.wiktionary.org/wiki/تار' \\\n'https://en.wiktionary.org/wiki/تیره' \\\n'https://en.wiktionary.org/wiki/مطمورة' \\\n'https://en.wiktionary.org/wiki/mazmorra' \\\n'https://www.etymonline.com/word/temerity' \\\n'https://www.etymonline.com/word/timid' \\\n'https://www.etymonline.com/word/tombac' \\\n'https://vajehyab.com/moein/مطموره' \\\n'https://vajehyab.com/moein/تم' ; do python3 tools/fetch_source.py \"$u\" --note \"page 500: roots Tem/Temar lookup\" 2>&1 | tail -1; done"
}
```


### [2026-10-15T02:47:02.687Z] TOOL RESULT

```
/home/sfmqrb/git/rishe-private/data/verification/sources/web/e5d08f8a4a3ac6ce.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/a7669c99c563f479.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/6e3c2df5610606b4.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/bdabca0792cbf56e.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/24b9b204aa2b8d17.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/8f3011b4fc7b762b.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/c514a75d913cdef3.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/43b9c7a3a1f7d7ee.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/a7814d5a985bb5cd.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/34bc0b4d652929e5.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/4c6fb6bd6c7bc868.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/36368be36df4d5ac.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/d3f1ec8fb2808515.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/1f2a3c167ed63bf0.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/4a8a784274f95c18.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/92bbbb469b15a382.txt
```


## [2026-10-15T02:47:05.001Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; tail -16 index.jsonl | python3 -c \"\nimport sys,json\nfor l in sys.stdin: d=json.loads(l); print(d['status'],d['bytes'],d['url'])\"; for f in e5d08f8a4a3ac6ce a7669c99c563f479 6e3c2df5610606b4 bdabca0792cbf56e; do echo \"#### $f\"; grep -n -i -A8 'Etymology' $f.txt | head -30; done"
}
```


### [2026-10-15T02:47:05.478Z] TOOL RESULT

```
200 7470 https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/-teros
200 7624 https://en.wiktionary.org/wiki/νέκταρ
200 3869 https://en.wiktionary.org/wiki/mazmorra
-1 39 https://www.etymonline.com/word/temerity
200 32787 https://en.wiktionary.org/wiki/drill
-1 39 https://www.etymonline.com/word/timid
-1 39 https://www.etymonline.com/word/tombac
200 33372 https://en.wiktionary.org/wiki/through
200 376 https://vajehyab.com/moein/مطموره
200 11277 https://en.wiktionary.org/wiki/گذشتن
200 8105 https://en.wiktionary.org/wiki/truncus
200 556 https://vajehyab.com/moein/تم
200 17412 https://en.wiktionary.org/wiki/terminus
200 39679 https://en.wiktionary.org/wiki/trans
200 12895 https://en.wiktionary.org/wiki/nostril
200 11176 https://en.wiktionary.org/wiki/अन्तर
#### e5d08f8a4a3ac6ce
#### a7669c99c563f479
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Verb 
69-
70- 1.3.1 
--
88: Etymology 
89-
90- 2.2 
91- Pronunciation 
92-
93- 2.3 
94- Adverb 
95-
96- 2.3.1 
--
114: Etymology 
115-
116- 3.2 
117- Noun 
118-
119- Toggle the table of contents 
120-
121- temere 
122-
--
#### 6e3c2df5610606b4
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Verb 
69-
70- 1.3.1 
--
174: Etymology
175- [ edit ] 
176-
177- Of uncertain origin. [ 1 ] One theory which links the term to Proto-Indo-European *temH- ( “ dark ” ) (for which compare tenebrae , tēmulentus ) is semantically reasonable, but phonetically difficult. [ 2 ] 
178-
179: Compare Sanskrit तिम्यति ( timyati , “ to be quiet; to become quiet ” ) , with matching conjugation and verb-of-fearing semantics (i.e. "is/becomes quiet" in place of usual "makes quiet"). ( Can this ( + ) etymology be sourced ?) 
180-
181- Pronunciation
182- [ edit ] 
183-
184- ( Classical Latin ) IPA ( key ) : [ˈtɪ.me.oː] 
185-
186- ( modern Italianate Ecclesiastical ) IPA ( key ) : [ˈtiː.me.o] 
187-
#### bdabca0792cbf56e
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Noun 
69-
70- 1.3.1 
--
91: Etymology 
92-
93- 2.3 
94- Pronunciation 
95-
96- 2.4 
97- Adjective 
98-
99- 2.4.1 
--
229: Etymology
230- [ edit ] 
231-
232- Borrowed from Sanskrit ताम्र ( tāmra ) . Doublet of ताँबा ( tāmbā ) .
233-
234- Pronunciation
235- [ edit ] 
236-
237- ( Standard Hindi ) IPA ( key ) : /t̪ɑːm.ɾᵊ/ , [t̪ä̃ːm.ɾᵊ] 
--
```


## [2026-10-15T02:47:09.437Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; grep -n -E 'Etymology$' -A6 e5d08f8a4a3ac6ce.txt | head -5; grep -n -i 'Sanskrit\\|Avestan\\|Latin\\|Persian' e5d08f8a4a3ac6ce.txt | head -30; echo ----; sed -n '/^ *Etymology 1$/,+0p' a7669c99c563f479.txt; grep -n -E 'Latin|temere|\\*temH|blindly|rashly' a7669c99c563f479.txt | head -15"
}
```


### [2026-10-15T02:47:09.843Z] TOOL RESULT

```
----
1:URL: https://en.wiktionary.org/wiki/temere
4:TITLE: temere - Wiktionary, the free dictionary
6:temere - Wiktionary, the free dictionary 
83: Latin 
85: Toggle Latin subsection 
121: temere 
141: Latina 
212: Inherited from Latin timēre . Compare Portuguese and Spanish temer .
454: ^ “ temere ” in Luciano Canepari , Dizionario di Pronuncia Italiana (DiPI) 
461: Latin
467: From Proto-Italic *temezi ( “ in darkness, blindly ” ) , a fossilised locative form of Proto-Indo-European *témHos ( “ darkness ” ) , from *temH- ( “ dark ” ) . Cognate with Sanskrit तमस् ( támas ) , Persian تم ( tam ) , Latin tenebrae ( “ darkness ” ) . [ 1 ] 
469: Compare this form – here simply adverbial – with the history of the Latin present active infinitive; see -ere .
474: ( Classical Latin ) IPA ( key ) : [ˈtɛ.mɛ.reː] 
488: casually , fortuitously , rashly , heedlessly , thoughtlessly , inconsiderately , indiscreetly , idly 
492: 166 BCE , Publius Terentius Afer , Andria 204–205 : SĪMŌ: Irrīdēs? Nīl mē fallis. Ēdīcō tibi: / nē temerē faciās; neque tū haud dīcās tibi nōn praedictum — Cavē! SIMO: Are you laughing at me? You’re not fooling me at all. I declare to you: don’t act rashly ; and don’t you dare say that you weren’t warned — Beware!
```


## [2026-10-15T02:47:13.300Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; for f in e5d08f8a4a3ac6ce bdabca0792cbf56e 24b9b204aa2b8d17 8f3011b4fc7b762b c514a75d913cdef3 43b9c7a3a1f7d7ee a7814d5a985bb5cd 34bc0b4d652929e5 4c6fb6bd6c7bc868 4a8a784274f95c18 92bbbb469b15a382; do echo \"#### $f $(head -1 $f.txt) $(wc -c <$f.txt)\"; done"
}
```


### [2026-10-15T02:47:14.092Z] TOOL RESULT

```
#### e5d08f8a4a3ac6ce URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/temH- 3531
#### bdabca0792cbf56e URL: https://en.wiktionary.org/wiki/ताम्र 17087
#### 24b9b204aa2b8d17 URL: https://en.wiktionary.org/wiki/tembaga 6152
#### 8f3011b4fc7b762b URL: https://en.wiktionary.org/wiki/tombac 3494
#### c514a75d913cdef3 URL: https://en.wiktionary.org/wiki/تم 22839
#### 43b9c7a3a1f7d7ee URL: https://en.wiktionary.org/wiki/تار 14434
#### a7814d5a985bb5cd URL: https://en.wiktionary.org/wiki/تیره 6529
#### 34bc0b4d652929e5 URL: https://en.wiktionary.org/wiki/مطمورة 6475
#### 4c6fb6bd6c7bc868 URL: https://en.wiktionary.org/wiki/mazmorra 4094
#### 4a8a784274f95c18 URL: https://vajehyab.com/moein/مطموره 824
#### 92bbbb469b15a382 URL: https://vajehyab.com/moein/تم 1098
```


## [2026-10-15T02:47:17.764Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; sed -n 5,80p e5d08f8a4a3ac6ce.txt | grep -v '^\\s*$' | head -40; for f in 24b9b204aa2b8d17 8f3011b4fc7b762b a7814d5a985bb5cd 34bc0b4d652929e5 4c6fb6bd6c7bc868; do echo \"#### $f\"; grep -n -E 'Borrowed|From|Inherited|Etymology' $f.txt | grep -v '^\\S*:\\s*Etymology\\s*$' | head -6; done; grep -n -E 'From|Borrowed|Inherited' c514a75d913cdef3.txt 43b9c7a3a1f7d7ee.txt | head -12; sed -n 5,40p 4a8a784274f95c18.txt 92bbbb469b15a382.txt | grep -v '^\\s*$'"
}
```


### [2026-10-15T02:47:18.339Z] TOOL RESULT

```
Reconstruction:Proto-Indo-European/temH- - Wiktionary, the free dictionary 
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
 Proto-Indo-European 
 Toggle Proto-Indo-European subsection 
 1.1 
 Root 
 1.1.1 
 Derived terms 
 Toggle the table of contents 
 Reconstruction:Proto-Indo-European/ temH- 
 Add languages 
#### 24b9b204aa2b8d17
194: From Wiktionary, the free dictionary
230: Inherited from Malay tembaga , from Prakrit *𑀢𑀁𑀩𑀕 ( *taṃbaga ) , from Sanskrit ताम्रक ( tāmraka , “ copper ” ) .
288: From Old Javanese tambaga .
333: From Prakrit *𑀢𑀁𑀩𑀕 ( *taṃbaga ) , from Sanskrit ताम्रक ( tāmraka , “ copper ” ) .
#### 8f3011b4fc7b762b
158: From Wiktionary, the free dictionary
215: Borrowed from French tombac .
#### a7814d5a985bb5cd
79: Etymology 1 
91: Etymology 2 
163: From Wiktionary, the free dictionary
200: Etymology 1
203: Inherited from Middle Persian [script needed] ( tylk' /⁠tērag⁠/ , “ dark ” ) .
265: Etymology 2
#### 34bc0b4d652929e5
62: Etymology 1 
74: Etymology 2 
143: From Wiktionary, the free dictionary
148: Etymology 1
151: From the root ط م ر ( ṭ m r ) . Deemed by Fraenkel to reek of Classical Syriac ܡܰܛܡܽܘܪܬܳܐ ( maṭmūrtā , “ pit for hiding treasures ” ) from ܛܡܰܪ ( ṭmar , “ to bury; to hide, to abscond ” ) by reason of the Arabic root missing the meaning “to store” in the old poetry, and indeed from what the web databases of Qaṣāʾid and ʾAḥādīṯ return by 2019 طَمَرَ ( ṭamara , “ to bury, to hide ” ) is absent. Compare against Akkadian 𒋼𒈨𒊒 ( temēru, tamāru , “ to bury, to conceal ” ) .
343: Etymology 2
#### 4c6fb6bd6c7bc868
155: From Wiktionary, the free dictionary
175: Borrowed from Arabic مَطْمُورَة ( maṭmūra , “ granary, cellar ” ) , from the root ط م ر ( ṭ m r ) .
43b9c7a3a1f7d7ee.txt:280: From Wiktionary, the free dictionary
43b9c7a3a1f7d7ee.txt:290: Borrowed from Classical Persian تَار ( tār ) , from Proto-Iranian *tánθram , from Proto-Indo-Iranian *tántram , ultimately from Proto-Indo-European *ten- ( “ to stretch ” ) .
43b9c7a3a1f7d7ee.txt:375: From Middle Persian 𐭲𐭠𐭥 ( tʾr /⁠tār⁠/ , “ darkness ” ) , from Proto-Iranian *támHsram , from Proto-Indo-Iranian *támHsram , from Proto-Indo-European *temH- .
43b9c7a3a1f7d7ee.txt:399: From Proto-Iranian *tánθram , from Proto-Indo-Iranian *tántram , ultimately from Proto-Indo-European *ten- ( “ to stretch ” ) , Northern Luri تال ( tal ) ; see there for further information. Cognate to Sanskrit तन्त्र ( tantra ) .
43b9c7a3a1f7d7ee.txt:453: Borrowed from Classical Persian تار ( tār ) .
43b9c7a3a1f7d7ee.txt:482: Borrowed from Classical Persian تار ( tār ) .
43b9c7a3a1f7d7ee.txt:521: Inherited from Arabic ثَارَ ( ṯāra ) .
43b9c7a3a1f7d7ee.txt:642: Borrowed from Classical Persian تَار ( tār ) . First attested in c. 1657 as Middle Hindi تار ( tar /⁠tār⁠/ ) . [ 1 ] 
43b9c7a3a1f7d7ee.txt:716: From Proto-Turkic *tār . [ 1 ] Cognates with Turkish dar .
43b9c7a3a1f7d7ee.txt:730: From Persian تار ( târ ) 
c514a75d913cdef3.txt:244: From Wiktionary, the free dictionary
c514a75d913cdef3.txt:911: Inherited from Arabic ثَمَّ ( ṯamma ) .
معنی مطموره | فرهنگ انتشارات معین | واژه یاب 
 26 فرهنگ 
 همه دیکشنری مترادف طیفی آزاد + 
 همه دقیق مترادف متضاد مشابه آوا متن آغاز قافیه 
 مطموره
 فرهنگ انتشارات معین
 (مَ رِ) [ ع . ] (اِ.) نهان خانه .
 مطموره در فرهنگ‌های دیگر
 معنی مطموره در لغت‌نامه دهخدا 
 معنی مطموره در فرهنگ فارسی عمید / قربان‌زاده 
 خرید اشتراک افزودن واژه افزونه مرورگر تماس درباره 
 نسخه جدید
URL: https://vajehyab.com/moein/تم
FETCHED: 2026-10-15T02:47:02Z
STATUS: 200
TITLE: معنی تم | فرهنگ انتشارات معین | واژه یاب
معنی تم | فرهنگ انتشارات معین | واژه یاب 
 26 فرهنگ 
 همه دیکشنری مترادف طیفی آزاد + 
 همه دقیق مترادف متضاد مشابه آوا متن آغاز قافیه 
 تم
 فرهنگ انتشارات معین
 (تِ) [ فر. ] (اِ.) 1 - موضوع اساسی ، مایه . 2 - زمینه .
```


## [2026-10-15T02:47:22.153Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; grep -n -i -E 'temH|darkness|cataract|Proto-Iranian|Middle Persian' c514a75d913cdef3.txt | head; grep -n -i -E 'temH|támHras|Proto-Indo|copper' bdabca0792cbf56e.txt | head; grep -n -i 'temH\\|támHs\\|Avestan\\|Sanskrit\\|Persian' e5d08f8a4a3ac6ce.txt | head; sed -n 200,215p a7814d5a985bb5cd.txt"
}
```


### [2026-10-15T02:47:22.938Z] TOOL RESULT

```
931: Middle Persian [script needed] ( tom, tam , “ dark ” ) , from Proto-Iranian *támHah , from Proto-Indo-Iranian *támHas , from Proto-Indo-European *témHos ( “ darkness ” ) , from *temH- ( “ dark ” ) .
974: ( archaic ) darkness, blackness
976: ( archaic ) a disease in the eye, the web or cataract on the pupil
1347: Persian terms derived from Middle Persian 
1348: Persian terms derived from Proto-Iranian 
1392: Requests for native script for Middle Persian terms 
246: copper 
285: ताम्र गन्धेय ( tāmra gandhey , “ copper sulfide ” ) 
287: ताम्र जारेय ( tāmra jārey , “ copper oxide ” ) 
289: ताम्र भास्वीय ( tāmra bhāsvīya , “ copper phosphate ” ) 
312: Copper 
314: copper: ताम्र ( tāmra ) 
389: Related to तमस् ( tamas , “ gloom, darkness, obscurity ” ) , [ 1 ] as copper is a dark-colored metal, perhaps via a Proto-Indo-European form *tm̥H-ró- , with the long ā vowel perhaps stemming from analogical influence of forms in तम् ( tam ) . [ 2 ] 
403: of a coppery red color
650: copper 
857: Sanskrit terms derived from Proto-Indo-European 
1:URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/temH-
4:TITLE: Reconstruction:Proto-Indo-European/temH- - Wiktionary, the free dictionary
6:Reconstruction:Proto-Indo-European/temH- - Wiktionary, the free dictionary 
69: Reconstruction:Proto-Indo-European/ temH- 
131: *temH- 
139: Terms derived from the Proto-Indo-European root *temH- (39 c, 0 e) 
143: *temH-seh₂ ( or < *temH-s-eh₂ from *témHos ) 
171: Retrieved from " https://en.wiktionary.org/w/index.php?title=Reconstruction:Proto-Indo-European/temH-&oldid=82617021 "
213: Reconstruction:Proto-Indo-European/ temH- 
 Etymology 1
 [ edit ] 

 Inherited from Middle Persian [script needed] ( tylk' /⁠tērag⁠/ , “ dark ” ) .

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /teː.ˈra/ 

 ( Dari, formal ) IPA ( key ) : [t̪ʰiː.ɾä] 

 ( Dari, formal ) IPA ( key ) : [t̪ʰiː.ɾä] 
 ( Kabuli ) IPA ( key ) : [t̪ʰiː.ɾä] 

 ( Hazaragi ) IPA ( key ) : [t̪ʰi.ɾä]
```


## [2026-10-15T02:47:29.432Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; echo HRN; grep -n -E '^\\s*[0-9]+\\.\\s*(tär|tar|tär|tir|tlr|tam|tom)' HRN.txt | head; grep -n -i -E 'tamah|tqθra|taOra|tĕmah|tāra|tarik|tärik' HRN.txt | head; echo HUB; grep -n -i -E 'tämah|tamah|tärik|tarik|tîra|tira ' HUB.txt | head; echo PHD; grep -n -E '^(tom|tam|tār|tārīg|tārīk|tēr|tom)\\b' PHD.txt PHD_mackenzie.txt | head; grep -n -E '\\b(tom|tār|tārīg|tērag)\\b' PHD_mackenzie.txt | head"
}
```


### [2026-10-15T02:47:29.876Z] TOOL RESULT

```
HRN
11092:198. tarnian{i)su 'hochmütig , tarman(i)imh (Men., Bund.),
3471:370. {2)tär 'finster', tarik, I^nDDnND (Is. 50, 10).
3475:tärik, täriklh.
3476:kurd. LW. tan; af/. tör^ LW. tärik; oss. d. talingä,
6303:aw.staora- 'Zugtier; phlv. s^ör 'Zugtier, aber auch
13911:tärik 370.
HUB
4922:(5. Jhd.) gegen bal. p^aniSr; tira 'dunkel* gegen bal. tBray vgl. Kap. 17.
PHD
PHD.txt:4453:tom tambür ünóh! tab
PHD.txt:4482:tom, tom tumbag tof
PHD_mackenzie.txt:8169:tom                            -6\0     tarazcnidan             "tf..'~~~
PHD_mackenzie.txt:8237:tom, tom                    -61'"       tambiir                         ~,to
5007: tom [t(w)m I M tm, N tam] darkness.
5009: tom [twm I (M twhm, N tuxm)] seed, family.
6314:crow waray.                                darkness tar. tarig/kih. tom.
6547:except be ... (enya), jud az.                      family dl1dag, naf, tomag, tom.
7529: seed Cihr(ag), dan(ag), t6hmag, tom;     severity drustih, saxtih.
8169:tom                            -6\0     tarazcnidan             "tf..'~~~
8236:-tom                      ",I~-         tuwlinsamlin           \~ "-'\l!'
8237:tom, tom                    -61'"       tambiir                         ~,to
```


## [2026-10-15T02:47:32.493Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 3469,3478p HRN.txt; sed -n 4918,4923p HUB.txt; grep -n -E '^ ?(tar|tär|tārīg|tarig|terag|tērag)\\b' PHD_mackenzie.txt | head; grep -n -E 'tārīk|tārik|tērak|tērak|\\btār\\b|\\btom\\b|\\btum\\b' NYB_vol2_glossary.txt | head"
}
```


### [2026-10-15T02:47:32.988Z] TOOL RESULT

```
aw. Hqx^ra-, vergl. ai. täntra- 'Zettel, Aufzug des
Gewebes.
370. {2)tär 'finster', tarik, I^nDDnND (Is. 50, 10).
aw. tqdra- 'finster (aus Hamsra-^ Hansra-, Brug-
mann, Grundriss II, 171); ai. tämisra- 'finster', tamisrä-
'Finsterniss, finstere Nacht' ; phlv. tär^ tar[tum (Bund.),
tärik, täriklh.
kurd. LW. tan; af/. tör^ LW. tärik; oss. d. talingä,
t. faliny 'Finsterniss, finster', far 'dicht, düster (vom
Wald)' wohl LW. (243); bei. LW. tär, n. tar (269);
(Sal. Shuk. Gram. p. 15).
^) Dafiir lat. Sapor, Sapores, gr. ^ntaQt^g, ^a/Stogt^s^ syr. iawor
(Noldeke, Tab. p. 7, Anm., Hoffmann, Ausziige p. 9) mit o.
Vgl. den Weohsel von I mit e vor r in np, panlr *K&se' = &rm,panir
(5. Jhd.) gegen bal. p^aniSr; tira 'dunkel* gegen bal. tBray vgl. Kap. 17.
') Die Namen bei Firdusi sind haufig stark entstellt (vgl.
4922:tar [LCDr l < A l-~d; tll M tr] over, through, across.
4925:tar [t)ll M t)r] darkness.
4931:tarig/k [t)lyk I M t)ryg, N tarik!] dark.
4935:tar-manih [tlm)nyh] perversity.
4936:tar-menisn [tlmynfn 1 N tarmani;t] perverse; contemptuoua.
274:adar [?dl] low, sup. ~-tom 1021; v. also — Av. (57) adj. aóara-, (58) prep. adairi; MPrth ?dryg ‘below’ (List 80), adj. ’dryn (A-H III); MPrs ’yr ‘below, down’ (A-H II), ’yrdwm ‘lowest’, »yrg ‘southern’ (S); Paz. érdar ‘lower’. a-dart ['dlt'] painless, unafflicted 774. — V. dart.
425:*a-namr-tom [nmltwm] 4218, sup. of *a-namr not *humble, not *deferential,
505:lapar [’pl; MDM, v. 2apar] adj. situated above, lying above: évak ~, apäk dit, v.s.v. žapāk (2); — heavenly, often in compounds: apar-apükeh etc., v. below; comp. ~-tar [’pltl] higher 5426, 581°, highest 1097; sup. ~-tom highest 415. 102°; v. also apartaréh; — adv. empha- sizing an adj.: highly, extremely: apar- aržānīk, v. aržānīk. — Av. (393) upara-, adv. upara (instr.), uparam; MPrth ’br adj. and adv. (MHC), comp. ’brdr, sup. ’brdwm; Ps. ?pldl; Paz. awartar, awardar (SGV); NP bar ‘height, top, summit’, bartar ‘higher’. ?apar [MDM, erroneous reading of OAram QDM] 1. adv. above: (3 päs) i-m guft ~ of which I spoke above 65°; či nümak" cé hac ~ nipišt" éstat the inscription that had been written here above P2:3, cf hacapar; — prev. over, on, upon, up, or simply expressing the initiation of the action, with varying vbs., cf esp. (@)ma- tan, burtan, grätan, raftan, rasitan ; follow- ed by enclitics: apar-p-im ravišn I must needs ascend 4076, v.s.v. -p(i); — refer- ring back to an encl. pron.: api-š Vidrafš . ~ mšast and V. got on it (the horse) 25W5; cē-t avdom margéh ~ raset for at the end Death will come upon thee 726-7; (martömän) tāi-šān āmēcišn ~ nē barend as long as one does not impart instruction to them 801. — 2. prep. a) local: over, on, on to, down on: Krisäsp ~ én damik raset K. is roaming all over this earth 3318; ~ giyāk on the spot 3", 102; ~ ki Zartuxst bé dahém where we shall deposit Z. 3957; ~ pad ēstāt rose to his feet 1821; asp ... — rahy vartét harness the horse! 5418-14; srišk ~ srišk drop after drop 214
564:apa-zönik he who has, administers apa- zon, bestower of overflowing, everlasting blessings, epithet of Ohurmazd 399-5. 58$. 59°; of Zartuxšt 1101; sup. ~-tom 57%. — Renders Av. (1618. 1619) spanta-, spē- nista-. Paz. awazuni, Skr. v. guru, brhat (Mx, SGV). Cf Bailey, BSOS VII, 1934, 292—294.
848:Pywe't'] cikāmcihē Pourusäsp ku yazišn kunät whenever P. intends to perform a sacrifice 5313-14, — Av. (1231) yaoz- ‘to be agitated’; MPrth rzmy(y)wz ‘eager for battle’ (A-H III); Arm. lw. yoiz 'commo- tion, trouble’, but also ‘research, investi- gation’ (den. vb. yuz-em ‘to agitate; to scrutinize’); — ä-yaoz- ‘to agitate, to MPrth ”ywštn, ?ywz- (’y-) (A-H III), ”*ywštg ‘tossing’ (sea), ’ywz ‘violent; disturbance’ (MHC). Borrowed in MPrs in the same sense (Verbum 183) and also in BP: razmik adydzisn ["ywešn'] ‘the act of fighting in battle-array', NSt § 3; äyöz renders Av. yaozante Y. 654. In SW, where Z changed to z, āyēz- coincided with āyēž- and adopted its inf. āyuxtan, ef DkM 695 pres. äyöz-, but 6815 äyux- tārēh in the sense ‘strive for’. The genuine SW form of yaoz-: OP yaud-, v. yöd-; possibly represented by *āhēyēnītan (q.
1180:dänäkihä wisely, with good insight, or judgment 4". 5119. 5322; sup. ~-tom with the best wisdom 59%.
1277:dév-izak [ŠYD”-yck'] worshipping the devils, sup. ~-tom 53°. — A recent com- pound of dev + izak < *yaza-ka-, cf izišn; the Phl. rendering of Av. daéva- yaz-, v. dēv-ayyās.
1487:farrax" [plhw'] fortunate, blissful, glori- ous 6?; sup. ~-tom 36°. 4718; v. also Šat-farraxu-Xosrči. — Olr (Median) *far- nahvà, nom. of *farnahvant — Av. (1873 sq.) z*aronahvant- derived from z"aronah-, v. z"arrah. MPrthPrs frwx, MPrs also prwz; Paz. frox, Skr. v. susamrddha; NP farrux.
1492:frac [pr’c, pc] 1. adj. forward; promi- nent, distinguished, comp. ~-tar 14, sup. ~-tom 1021?.19, — 2. adv.: ē tigriyaf ~-tar one bowshot further 212’. 222; m 1094, hac nun ~ 611? henceforth; hac han ~ thenceforth 985; ~ 6 P2:9. — 3. prev. ahead, along, forth, forward, on (-ward), up, ete., or denoting the perfec- tive aspect, both in a local and in a figurative sense, with a great many vbs., v. each separately; also together with v. nouns: ~ guftür, ~ ranjakēh, ~ tuxšākēh,
2040:hu-dähak [hwd’hk'] sup. ~-tom boun- teous 57% — Borrowed from Av. (1825) hudčih-; Paz. hudahaa, Skr. v. uttama- danin (SGV).
```


## [2026-10-15T02:47:37.117Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E '^(tār|tar|tarik|tārīk|tom|tum|tērak|tērak)\\b|^t[aā]r[iī]k|^tōm|^tom ' NYB_vol2_glossary.txt | cut -c1-300 | head; grep -n -E '^tēr|^tir|^tär' NYB_vol2_glossary.txt | cut -c1-200 | head; grep -n -E '^ *(tom|tam|tār|tarik)' PHD.txt | head -3"
}
```


### [2026-10-15T02:47:37.855Z] TOOL RESULT

```
3738:taräzük  [tl'ewk'] balance, scales for weighing 72%, — Olr *arä = Skr čula ‘balance, scale of a balance’ + Av. (223 sg.) az- ‘to convey, to conduct’
3741:tarik
3745:tārīk [t*lyk] dark 377°. 762. 859.1339, - M PrthPrs t’ryg, derived from Av. (650) iq0ra- ‘darkness’, MPrthPrs vr; NP tar ‘dark, obscure’; tārīk < *tqOriya-ka-, Av. taūrya- ‘dark’.
3746:tarikéh darkness, the quality of being dark 3317. 347. 6212, 6314. 641. 10316,
3748:tar-mčnišneh [tlmynšnyh] arrogance, overbearingness 4718, 838, — V.s. v. "ar.
7473:tar: tarr
6828:tir: ~
7474:tär: tärık
3933:tamarisk gaz.
3934:tambour tambirag.
4028:tomb aspānūr, dādgāh, daxmag, hazzān.
```


## [2026-10-15T02:47:40.821Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY; grep -n -E 'TAM|TAR|TIR' ARY_latin_index_pages.txt | head -20; grep -n -E '^(تم|تار|تاریک|تیره)\\b' ARY_pages.txt | head"
}
```


### [2026-10-15T02:47:41.328Z] TOOL RESULT

```
224:INATARA io. ill (NADRE 653 £ NAEDDRE: 34S .,Sil (NATHIR 45°
967:Pe leo Ben aloes 55 ake SI te pe 05 90 > Senay Ut 1 (PLUTARCH)
981:ght Le (ayaa gas GPITAR © PITER 9 (ity gx 4 JOVE+ JU) JUPITER
1366:_ ATER ATARSH —(AVESTAN) gus)
1502:(OLD CHURCH SLAVIC) 4S 63%! RUCTUS, RUCTARE, = (LATIN) 3Y
1503:RYGAJO . ERUCTARE- ERUGO
1507:RUBENIS LATVIAN) (3) isd ERUCTARE
1508:RUCTAN :(OLD PRUSSIAN) (AS 53.4 RUTTO, RUTTARE :(/TALIAN) plu!
1633:US-+MATAR-
1641:lai S(UDTAMOS 4) UD -\ spy! y ta wataely 92 jt el Sp eesti onl ghey! sels
1681:WERIAN  :(OLD ENGLISH) gS godt WASTAR, (PAHLAVI) 5 34,
1682:WEAR ENGLISH) 5-JS3! WASTARAG-, ASTAR
1690:BARNHART: (WEAR) 1224, (VEST) 1207 VESTIS, VESTIRE (LATIN) 3
1695:ONIONS: (WEAR) 996 VESTE, VESTIR (PORTUGUESE) Ji x
1701:¢ (enlace Si (laS ge 22 eat cal slasdls Sao ASTAR shy)" 1" ody all “1
1703:| wae WSU, ale CASTAR os slay Godly a) Sab cl slansly Geen oY
1779:ETMI, ETIR, ET- HITTITE) cca ATA (SWEDISH) (5.8 yo
1825:‘REFERENCES beth GHRTAM, (SANSKRIT) ey Suite
2002:ANDEN DANISH) jails ANYA., ANTARA, ANYAS, ANAYA
2013:POKORNY ~S~S~*~*«SS*CT ANTARAS
857:تاریخی» وجود همریشه‌های بالتیکی (به ویژه لیتوانی) از اهمیت خاصی پرخوردار است.
1568:تم اگایس سرواز لارسا ‏ ار 12۸01
5521:تار» تاریک / ۱۸۹
6188:تیره تبرگي / ۲۱۱
6653:تم انگلیسی سرواز‌ی فا را 0۵۷
9395:تم 7 أ
10430:تمه
12975:تم برنانی 08280): ۰ ۲1123۸120 ,ق0399 5 (759همی) ی
```


## [2026-10-15T02:47:43.273Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 tools/ref_page.py ARY:189 --image 2>&1 | head -60"
}
```


### [2026-10-15T02:47:50.722Z] TOOL RESULT

```
(no exact page map; using offset -1 -> pdf page 188; check the printed number and re-run with --pdf-page if off)
IMAGE: /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/ARY/0189.png
REF: ARY:189  PDF: data/verification/sources/refs/incoming/ARY/ARY_aryanpur_kashani_rishehaye_hend_o_orupayi.pdf page 188  OCR-lang: fas+eng

: ۱۸۹ / ‏تار» تاریک‎
TMA, 783/17707۸  :(RUSSIAN) ‏روسی‎ TATHRA, TEMAH  :(AVESTAN) ‏اوستایی‎
‎TEMNY, TMAVY :(CZECH) S {PAHLAVD) ‏پهلوی‎
‎TAMA, TMINA (SERBIAN) ‏صربی‎ TAR, TARAG, TARIG, TUM, TUMIK
TMA, TEMNOTA  :(BOHEMIAN) ‏بوهمی‎ TALING, TALINGA  :(OSSETIC) ‏اوستی‎
‎TEMNY, TMAVY  :(SLOVAK) ‏اسلواکی‎ TAR, TARISTAN  :(KURDISH) ‏کردی‎ ۱
۱ :)./77۸2/140/( ‏لیترانی‎ TAR:(BALUCHI) ‏بلوچی‎
‎TIMSRAS, TEMTI TOR, TAM  :(AFGHANI) ‏(پشتر)‎ Sl
TUMSA, TIMSA :(LATVIAN) ‏(لتی)‎ 453 TAMASSE  :(TOKHARIAN B) B ‏تخاری‎
‎TEMEL :(OLD IRISH) ‏ایرلندی کهن‎ TAMSRAS, +(SANSKRIT) ‏سانسکر بت‎
TYWYLLWCH, TYWLL :(WELSH) ‏ولزی‎ TAMRAS, TAMISRA, TAMAS
:(BRETON) ‏برترنی‎ TENEBRAE (LATIN) ‏لاتین‎
‎TENVALIENN, TENVAL TENEBRES :(FRENCH) ‏فرانسه‎
‎TINIEBLAS ASPANISH) ‏اسپانیایی‎
‎- REFERENCES ‏پسگشت‌ها‎ TENEBRE A(ITALIAN) ‏ایتالپایی‎
‎POKORNY:  1063-1064 INTUNERIC {RUMANIAN) ‏رومانی‎
‎BARNHART: (TEMERITY) 1122 :(OLD SCANDINAVIAN) ‏ایسلندی کهن‎
DELAMARRE: (SOMBRE) 236 THAM
۱ MACKENZIE: :(OLD HIGH GERMAN) ‏آلمانی کهن‎
(DARK, DARKNESS) 109, DINSTAR
BUCK: 61 FINSTER - {(GERMAN) ‏آلمانی‎
‎ONIONS: (TENEBRAE) %03 TAMM :(NORWEGIAN) ‏نروژی‎
‎SKEAT: (TEM) 759 DUISTER (DUTCH) ‏هلندی‎ % i
AMINDAROV: (DARKNESS) 209 {OLD CHURCHISLAVIC) ‏اسلاری کهن‎
۴۵۶ + ‏برهان قاطم‎ TIMA ۱
EMA :(POLISH) ‏لهستانی‎
‏بادداشت,‎
‏و‎ POKORNY:1063) ‏واژه‌ی فارسی ام" ) چم "86 چشم" يا "آب مرواریدا) نیز از همین واجریشه است‎
۱ )۵۱۱ : ‏برهان قاطع‎
```


## [2026-10-15T02:47:54.716Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD; for n in 729 730; do awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' WLD_Bd1_pages.txt | grep -n -i -E 'tem[əe]|tamas|temere|tenebrae|tąθra|tamra|dunkel' | head -12; echo ---; done"
}
```


### [2026-10-15T02:47:55.240Z] TOOL RESULT

```
107:„dunkel“, vgl. „es wird einem dunkel vor den Augen“ („geistig umnachtet"
128:tem(a y - „dunkel“, *tcmos n. „Dunkel a                                            daneben r-Bildungen (siehe dazu
134:   Ai. tdmns- n. „Dunkel, Finsternis 11                            = av. tamah- ds., ai. tamasa-h „dunkel-
135:farbig“. tnmsra-h „dunkel, bleifarben 11                                       tdmisra (= lat. tenebrae ), tamisra-m
---
3:„Dunkel“; tamrd-h ,,verdunkelnd“, tamra-h „dunkelrot, kupferrot“, timi-
4:rd-h „dunkel, finster (ass. aus *tamird-h1 Schmidt aaO.; anders Wacker-
10:nagel AiGr. I 18, Persson Beitr. 145); a y.tq&ra- n. PI. „Dunkelheit ( Ham
18:   lat. tenebrae „Finsternis   (diss. aus *tcmafra
22:lings, planlos, aufs Geratewohl“ (Loc. *temesi „im dunkeln [tappend]                                                                                                      ,
25:s. Yf. LEWb. s. v.), temero -are „befleeken, entehren, schanden
30:dunkeln           =
31:             beschmutzen ); mir. teim, temen „dunkel, grau , air. temel „Fin-
44:aaO.); as .thimm „dunkel       pimzd -, Weyhe PBrB. 30,56;; mndl. deemster
51:— ai. tamsra-h); nd. d/sig. ndl. dijsig „nebelig, dunkel“ ( *pemsiga- Falk-Torp                                                         ,
59:„finster werden      tamsd „Finsternis“, tamsiis „dunkel, schwarz
64:„schweiflfiichsig,  dunkelrot, von Pferden       lett. tumst (Inf. tumt) „es                                     ;
---
```


## [2026-10-15T02:47:59.993Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==729||NR==730' incoming/WLD/WLD_Bd1_pages.txt | grep -n -i 'timeo\\|timor\\|timid' ; echo IEC; grep -n -E '^t[eə]m[əe]?s?- |^tem\\w*- ' IEC.txt | head; echo SKT; grep -n -i -E '^(tombac|temerity|timid)' SKT.txt | cut -c1-300; echo HJB; grep -n -i -E '^TOMBACK|^TOMBAC' HJB.txt | head -3; echo LAT; grep -n -E '^timeō|^timeo|^temere' LAT.txt | head"
}
```


### [2026-10-15T02:48:00.546Z] TOOL RESULT

```
86:  lat. trmTtim ,,jedes berauschende Getriink, Met, \Vein“, timidentus ,,be-
272:   Aus dem Lat. hierher tempus „Schlafe (vgl. ahd. timid „Schlafe, Stirne                              4,                                                             44
IEC
18325:tem- (1) radical element ‘dark’, in Skt. tamih, f. ‘night’; Lat. temere 'rashly'; Li. temstù, temti, and teméju, éti, v. “grow dark'. WP I, 720. Cf. temos- (temes-), etc.
18326:tem- (tém-) (2) ‘tire, harass, exhaust Skt. tamakah, m. ‘asthma’; tàmyami, v. ‘choke, faint; OLat. cf. temétum ‘fumes of wine’; Lat. abs-temius, adj. “free from wine’; (o-gde in) R u-tomit, v. *exhaust
18327:tem- ‘mark, note’ Ukr. za-tjamyti, inf. ‘remember’; Li. (Žemaitē) teme, f. ‘remark, note’; tēmiju, yti, v. “observe, beware’
18329:temen- (2) ‘cutting, piece’. See temmn- Ar temnó
18332:temmn- (temen-) “cutting, offcut, piece’. See next, and cf. tom-, tm- Myc. & Gk. témenos, gs: -eos, n. “plot of land, reserve’; cf. tméma, n. ‘section’; MIr. cf. ta- mán, Ir. tamhan, pl. -ta, m. ‘stump, torso"; Br. tamm, m. pl: -u ‘piece’; W tam, pl. -au, m. id.; Cor. tam, pl. tymmyn, m. ‘scrap’;
SKT
19736:Timid.  <F.-L.)    V.timiJe fearfnL  —  L.  timere,  to  fear.    Al tarn,    to    choke,    tamo/,   dai TAM.)
HJB
22251:TOMBACK,  s.  An  alloy  of  copper and  zinc,  i,e.  a  particular  modification of  brass,  formerly  import4»d  from  Indo- Chinese  countries.  Port,  tambaca, from  Malay  tdmbaga  and  tdwbcMay *  copper,'  which  is  again  from  Skt. tamrika  and  tdmra.
LAT
63323:temere adv.: "a 1 1 aveuglette", par suite "inconsiderement, au
64505:timeo, - 5 s, -ui, - 5 re: craindrejaYoir pear. Transitif et absola,
64876:temere, F.483,7. Adverbe archaique (Liv.Andr., Naev., Acc., Pac., Enn.
```


## [2026-10-15T02:48:03.156Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 63323,63332p LAT.txt | cut -c1-300; sed -n 64505,64520p LAT.txt | grep -i -n 'etym\\|obscur\\|inconnu\\|rapproch\\|tem' | head; grep -n -i -E '^temerity|^tombac' SKT.txt SKT_dli_revised.txt | cut -c1-300"
}
```


### [2026-10-15T02:48:03.576Z] TOOL RESULT

```
temere adv.: "a 1 1 aveuglette", par suite "inconsiderement, au
hasard, a la legere, sans reflexion"; souvent joint a forte dans
le couple asyndetique forte tenere. Usite dans la locution non tenere
est quod "ce n'est pas un hasard que"; non tenere a aussi le sens
de "non facile' 1 , e.g. Pl., Ba.85, rapidus fluuius est hic, non hac
tenere transiri potest. lenere est proprement 1 1 ahlatif-instrumental
d’un subst. *tenus, -er is "obscurite", cf. tenebrae) riais il a <?t<?
uniquement employe comme adverbe, et traite comme tel; de la le
doublet tener iter (Enn., Acc.). - Ancien, usuel.
Derives: teneritas : 1° hasard; 8° irreflexion, legeret*? d'esprit (opp.
SKT_dli_revised.txt:79505:Temerity. ( F. — L.) M.F. temerity. —
```


## [2026-10-15T02:48:05.862Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 64505,64530p LAT.txt | cut -c1-200 | tail -18; sed -n 79505,79508p SKT_dli_revised.txt; grep -n -i 'Tombac' SKT_dli_revised.txt FSD_vol4.txt | cut -c1-250 | head -4"
}
```


### [2026-10-15T02:48:06.318Z] TOOL RESULT

```
a pas davantage. Les nots indo-europdena aignifiant "craindre" n'ont
qu'une aire peu dtendue, gr.8(F)eu— (8eoc, etc.) et ar *.erkn$in "je
crains", d'uae part, ou iri. -igur "je crains", v.isl ,agan "craindre"
et skr. bhdyate, v.sl. boitu sf "il craint". de 1 'autre. - Lat. terree
n'est venu que secondairement au sens de, "effrayer". - Le groupe
de metus, conne celui de iri. omun, gall. ofn "crainte", n'a pas non
plus d' dtynologie.
tina, -ae f.: sorte de bouteille k yin, ddfinie par Varr. ap.
Non., 544 , 5 » oris longi cum operculo. ■ Deneurd dans les 1 . ronanes, M.L.
8741 tina et tinum. Cf. P.F.501,x: tinia, uasa uinaria; et canaua,
cauea, tinum, Not.Tir.
tinca, -ae f.: sorte de poisson, sans doute la "tanche", Aus.
Mos., 155. M.L.8743; nderl .tinke.
Sans dtynologie.
tinea, -ae f.: ddsigne toute espfece de vers ou de nites, ver des
arbres, des fruits, cbenille, larve, pou,'vernine, etc. Bn particulier
la "teigne". Ancien (Cat.). Panronan, sauf rounain. M.L.8746.
Ddrivds: tineola (Vdg. ), tineosus (Gol.), M.L.8747-8; tinee,-Hs (ital.,
Temerity. ( F. — L.) M.F. temerity. — 
L. acc. temeritdtemy rashness. — L. adv. 
temere, rashly. The orig. sense of teinere 
was ‘in the dark’; cf. Skt. iamas, gloom. 
FSD_vol4.txt:30358:ta-ma'yn-an,  1   ta-ma'yu-on  2   ta-ma'ju-an,  n   [P  1 1   A dark  red-colored  wood  tSfrombosia  phtlippenHs) tam'bac,  i   tam'bak  2   tim'bSc  n   1.  Same  as  tombac 2,  Agalochum  or  aloes-wood  [Var  of  tombac  J
FSD_vol4.txt:55745:tion  of  the  community,  specif ,   the  bndge  of  the  Woman’s Christian  Temperance  Union —   w   frlbboner,  n   One wearing  a   ^hite-rlbbon  badge  — w.  roblnfsnlpo  [Local, US],  the  knot  —   W.  rock,  a   jellow  or
```


## [2026-10-15T02:48:30.087Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} {n++} /mattamore,  n\\./ {print \"mattamore leaf\",n-1} /tombac,  n\\./ {print \"tombac leaf\",n-1} /temerity,  n\\., +rashness/ {print \"temerity leaf\",n-1}' KLN_1966.txt; grep -n -E \"Avestic|tamah\" ../refs/KLN_1966.txt | grep -i 'tamas,' | head -2; grep -n -E '^tamas,' KLN_1966.txt | cut -c1-400"
}
```


### [2026-10-15T02:48:30.565Z] TOOL RESULT

```
mattamore leaf 509
temerity leaf 839
tombac leaf 861
```


## [2026-10-15T02:50:42.783Z] TOOL CALL #50: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/build-500.py <<'EOF'\nimport json\nW=\"https://en.wiktionary.org/wiki/\"\nPIE=W+\"Reconstruction:Proto-Indo-European/temH-\"\nPOKr={\"ref\":\"POK:1063\",\"status\":\"supports\",\"note\":\"Pokorny IEW pp.1063-1064 (POK_full.txt line 85335 'Root / lemma: tem(ə)-', 'Meaning: dark', Page(s): 1063-1064): 'Old Indic tamas- n. darkness = Avestan tamah- ..., npers. tam ...; tāmra- 'kupferrot' ...; Avestan tąθra- Nom.Pl. 'darkness', np. tār 'dim' = *tam-sra-'; 'Latin tenebrae ..., temere 'blindlings, aufs Geratewohl' (Lok. *temesi 'im Dunkeln [tappend]')'.\"}\nWLDc={\"src\":\"WLD\",\"where\":\"Bd. I pp.720-721 (WLD_Bd1_pages.txt leaves 729-730)\",\"stance\":\"supports\",\"note\":\"'tem(ə)- „dunkel“, *temos n. „Dunkel“: Ai. tamas- n. „Dunkel, Finsternis“ = av. təmah- ds. ...; tāmra-h „dunkelrot, kupferrot“ ...; av. tąθra- n. Pl. „Dunkelheit“'; 'lat. tenebrae ... temere „blindlings, planlos, aufs Geratewohl“ (Loc. *temesi „im dunkeln [tappend]“)'.\"}\nAHDc={\"src\":\"AHD\",\"where\":\"Watkins 1985 s.v. temə- (AHD_watkins1985.txt line 1078)\",\"stance\":\"supports\",\"note\":\"'temə-. Dark. Suffixed form *teməs-. 1. Latin temere, blindly, rashly: TEMERARIOUS, TEMERITY. 2. Suffixed form *teməs-rā- in Latin tenebrae (plural), darkness ... [Pok. tem(ə)- 1063.]' — timid is NOT listed.\"}\nIECc={\"src\":\"IEC\",\"where\":\"IEC.txt line 18325 s.v. tem- (1)\",\"stance\":\"supports\",\"note\":\"Mann: 'tem- (1) radical element 'dark', in Skt. tamiḥ 'night'; Lat. temere 'rashly'; Li. temstù ... WP I, 720.'\"}\nKLNtem={\"src\":\"KLN\",\"where\":\"1966 s.v. temerity (KLN_1966.txt line 38479)\",\"stance\":\"supports\",\"note\":\"'L. temere, 'rashly, at random', prop. 'in the dark', fr. I.-E. base *temes- 'dark', whence also L. tenebrae ..., OI. tamas- 'darkness', tamsrah 'dark', tāmrah 'dark-red, coppery', Avestic təmah 'darkness' ... Cp. tenebrae, temulent, timid. Cp. also tombac'.\"}\nBQT456={\"ref\":\"BQT:456\",\"status\":\"supports\",\"note\":\"Borhan vol.1 p.456 (archive.org borhan-ghate-v1 leaf n682; read from image, saved ocr/BQT/0456.vision.txt): 'تار ... و تیره و تاریک را نیز گویند'; Mo'in fn.2: 'اوستا tathra (تاریک) (از *tamsra، *tansra): هندی باستان támisra (تاریک)، پهلوی târ، کردی târî، افغانی tôr، استی taling ...' — Nourai's 'tethra' reflects Mo'in's 'tathra'.\"}\nBQT511={\"ref\":\"BQT:511\",\"status\":\"supports\",\"note\":\"Borhan vol.1 p.511 (leaf n739; ocr/BQT/0511.vision.txt): 'تم - بفتح اول و سکون ثانی، آفتی است که در چشم پیدا میشود مانند پرده، و آنرا بعربی غشاوه گویند'; Mo'in fn.1: 'اوستا temah (تاریکی)؛ پهلوی tum ...، tumīk؛ هندی باستان támas (تاریکی)، افغانی tôr [tam] (تاریکی)'.\"}\nBQT544={\"ref\":\"BQT:544\",\"status\":\"supports\",\"note\":\"Borhan vol.1 p.544 (leaf n772; ocr/BQT/0544.vision.txt): 'تیره - بروزن خیره، تاریک و سیاه فام را گویند'; Mo'in fn.1: 'ایرانی باستان *tathrya-ka از اوستا tathrya «بارتولومه ۶۵۰» «نیبرگ ۲۲۵» قس: تار، تاریک؛ پهلوی têrak ...'.\"}\nSODr={\"ref\":\"SOD:387\",\"status\":\"supports\",\"note\":\"Gharib p.387 (SOD_pages.txt leaf 454, line 31378), entry 9588: 'tm- B, M, C  tam <Av. təmah-  ... hell'; also intro p.xxxi: '/tam/ tm- hell Av. təmah-, Skt. tamas'.\"}\nBRTc={\"src\":\"BRT\",\"where\":\"col. 650 s.v. tąθra-, and s.v. təmah- (BRT.txt lines 12207, 12231)\",\"stance\":\"supports\",\"note\":\"'təmah- n. 'Finsternis, Dunkel''; 'tąθra- n., Plur. 'Dunkelheit' ... Aus ar. *tamsra- ... np. tār; Pü.: tārīk'; adj. 'tąθrya- 'dunkel, finster''. Note: Bartholomae has tąθra- as a noun 'darkness'; the adjective 'dark' is tąθrya-.\"}\nKLNtomb={\"ref\":\"KLN:1626\",\"status\":\"supports\",\"note\":\"Klein 1966 s.v. tombac (KLN_1966.txt line 39481, leaf 861; the leaf-offset rule gives c. p.1698, so the exact page 1626 is not confirmed, but the entry is the one meant): 'tombac, n., an alloy of copper and zinc. F. tombac, fr. Port. tombac, fr. Malay tambaga, 'copper', fr. OI. tāmrakah, of s.m., fr. tāmráh, 'dark-red, coppery', which is rel. to tamas-, 'darkness'.'\"}\nHJBc={\"src\":\"HJB\",\"where\":\"s.v. TOMBACK (HJB.txt line 22251)\",\"stance\":\"supports\",\"note\":\"'TOMBACK, s. An alloy of copper and zinc ... Port. tambaca, from Malay tāmbaga and tāmbāga, 'copper', which is again from Skt. tāmrika and tāmra.'\"}\nFSDtomb={\"src\":\"FSD\",\"where\":\"vol.4 s.v. tambac (FSD_vol4.txt line 30358)\",\"stance\":\"partial\",\"note\":\"'tam'bac ... n. 1. Same as tombac. 2. Agalochum or aloes-wood [Var. of tombac]' — confirms the English variant spellings tambac/tombac; no etymology in this snippet.\"}\nKLNmatt={\"ref\":\"KLN:948\",\"status\":\"supports\",\"note\":\"Klein 1966 s.v. mattamore (KLN_1966.txt line 23149, leaf 509): 'mattamore, n., a subterranean dwelling or storehouse. — F. matamore, fr. Arab. maṭmūra, 'something hidden', prop. fem. pass. part. of ṭámara, 'he hid, concealed', fr. Aram. ṭ'mar, of s.m. See Siegmund Fraenkel, Die aramäischen Fremdwörter im Arabischen, p.137. Aram. ṭ'mar is rel. to Heb. ṭāman ... Akkad. ṭamāru 'to cover with earth''.\"}\nAFAc={\"src\":\"AFA\",\"where\":\"p.137 (AFA.txt line 5013)\",\"stance\":\"supports\",\"note\":\"Fraenkel: 'Eine unterirdische Grube zum Aufbewahren des Getreides ist [maṭmūra] ... Da [ṭamara] im Altarabischen in der Bedeutung »aufbewahren« nicht existiert, so ist schon von vornherein die Entlehnung wahrscheinlich ... findet sich [maṭmūrā] wirklich in dieser Bedeutung im Syrischen.'\"}\nDEVc={\"src\":\"DEV\",\"where\":\"s.v. Matamore (DEV.txt line 1697)\",\"stance\":\"supports\",\"note\":\"'Matamore. Silo pour le grain ... magasins souterrains ... C'est l'arabe maṭmōra, fosse souterraine, silo. De ce mot vient l'espagnol mazmorra, cachot, fosse, prison.'\"}\nPHNc={\"src\":\"PHN\",\"where\":\"s.v. MATAMORE (PHN.txt line 7236)\",\"stance\":\"supports\",\"note\":\"'MATAMORE, s. f. ... maṭmoûrat, caveau, nom de lieu dérivé de ṭamar, cacher sous terre. Cellier souterrain, silo ... aussi le nom d'une sorte de prison ... ne confondez pas ... avec matamore, subst. masc., qui vient de l'espagnol et se dit pour fanfaron'.\"}\nLAMc={\"src\":\"LAM\",\"where\":\"s.v. Matamore (LAM.txt line 5182)\",\"stance\":\"supports\",\"note\":\"'Matamore. Esp. Ptg: mazmorra ... maṭmoûra, fosse souterraine, silo; et aussi prison, de ṭamar, cacher.'\"}\nFSDmatt={\"src\":\"FSD\",\"where\":\"vol.3 s.v. mattamore (FSD_vol3.txt line 17074)\",\"stance\":\"supports\",\"note\":\"'mat'ta-more ... n. In Eastern countries, a cavern or other underground place for storing grain [< F matamore, < Ar. maṭmūr, cavern for storing corn]'.\"}\n\nnodes0=[\n {\"id\":1,\"lang\":\"Avestan\",\"words\":\"temah; tethra\",\"verdict\":\"plausible\",\n  \"derivation\":\"Avestan təmah- n. 'darkness' (Bartholomae) is the exact cognate of Sanskrit tamas-, from PIE *témHos 'darkness' (o-stem neuter in -es/-os), with Indo-Iranian *a > Av. ə before m. The second word is Avestan tąθra- (Bartholomae col. 650: n. pl. 'darkness'; the adjective 'dark' is tąθrya-), from Proto-Iranian *tamHsra- (cf. Skt. tamisra-, Latin tenebrae < *temasrā), with *-ms- > nasalised ą + θr. Both words are correct; 'tethra' is not a standard transliteration (it follows Mo'in's 'tathra' in Borhan p.456, with e for ą), and the gloss 'dark' really belongs to tąθrya-.\",\n  \"derivation_fa\":\"اوستایی təmah- «تاریکی» هم‌ریشه با سنسکریت tamas- و از هندواروپایی آغازین *témHos «تاریکی» از ریشهٔ *temH- است. واژهٔ دوم در اوستا tąθra- است (بارتولومه: اسم جمع «تاریکی»؛ صفت «تاریک» tąθrya- است) که از ایرانی باستان *tamHsra- آمده و با سنسکریت tamisra- و لاتین tenebrae هم‌ریشه است؛ خوشهٔ -ms- در اوستایی به واکهٔ خیشومی ą و θr بدل شده. هر دو واژه درست‌اند، ولی صورت «tethra» نورایی نویسه‌گردانی نامعمولی است (برگرفته از tathra در حاشیهٔ معین) و معنای «تاریک» در اصل از آنِ tąθrya- است؛ ادعای نورایی با احتیاط پذیرفتنی است.\",\n  \"sources\":[PIE,W+\"تار\"],\n  \"ref_check\":[POKr],\n  \"consulted\":[BRTc,WLDc,{\"src\":\"NYB\",\"where\":\"vol.2 glossary p.191 s.v. tārīk (NYB_vol2_glossary.txt line 3745)\",\"stance\":\"supports\",\"note\":\"'tārīk [tʾlyk] dark ... derived from Av. (650) tąθra- 'darkness', MPrthPrs tʾr; NP tār 'dark, obscure'; tārīk < *tąθriya-ka-, Av. tąθrya- 'dark'.'\"}]},\n {\"id\":2,\"lang\":\"Persian\",\"words\":\"tam\",\"verdict\":\"plausible\",\n  \"derivation\":\"NP tam تَم 'darkness; a film/cataract over the eye' (Borhan p.511: آفتی است که در چشم پیدا میشود مانند پرده = Ar. ghishāwa) continues MP tom/tam 'darkness' (MacKenzie: tom [twm] darkness), from Proto-Iranian *támHah = Av. təmah-; the eye-disease sense is a semantic specialisation of 'darkness (of sight)'. Of the extra words, tār 'dark' < MP tār < *tamHsra- (Av. tąθra-) and tārīk < MP tārīg < *tąθriya-ka- (Nyberg) are confirmed; tīre 'dark' < MP tērag is attested, and Mo'in (Borhan p.544, after Nyberg 225) derives it from *tąθrya-ka-, which is less certain phonetically (Wiktionary goes back only to MP tērag). Hence 'plausible' for the box as a whole.\",\n  \"derivation_fa\":\"«تَم» (تاریکی؛ پرده‌ای که بر چشم می‌افتد، به عربی غشاوه) از فارسی میانهٔ tom/tam «تاریکی»، از ایرانی باستان *támHah- (اوستایی təmah-) است؛ معنای «آفت چشم» تخصیص معنایی «تاریکیِ دید» است. «تار» (تاریک) از پهلوی tār، از *tamHsra- (اوستایی tąθra-) و «تاریک» از پهلوی tārīg از *tąθriya-ka- است که هر دو قطعی‌اند. «تیره» از پهلوی tērag است؛ معین به پیروی از نیبرگ آن را از *tąθrya-ka- می‌داند، ولی این پیوند از نظر آوایی کمتر روشن است. بنابراین ادعای نورایی برای «تم، تار، تاریک» درست و برای «تیره» با احتیاط پذیرفتنی است.\",\n  \"sources\":[W+\"تم\",W+\"تار\",W+\"تیره\"],\n  \"ref_check\":[BQT456,BQT511,BQT544],\n  \"consulted\":[{\"src\":\"HRN\",\"where\":\"no. 370 (HRN.txt line 3471)\",\"stance\":\"supports\",\"note\":\"'370. (2) tār 'finster', tārīk ... aw. tąθra- 'finster' (aus *tamsra-, *tansra-, Brugmann) ; ai. tāmisra- 'finster' ... phlv. tār, tār[tum] (Bund.), tārīk, tārīkīh.'\"},\n   {\"src\":\"HUB\",\"where\":\"HUB.txt line 4922\",\"stance\":\"partial\",\"note\":\"Hübschmann only cites 'tīra 'dunkel' gegen bal. tēray' as an example of ī/ē alternation; no derivation from Av. tąθra-.\"},\n   {\"src\":\"PHD\",\"where\":\"s.v. tom, tār, tārīg (PHD_mackenzie.txt lines 5007, 4925, 4931)\",\"stance\":\"supports\",\"note\":\"'tom [t(w)m I M tm, N tam] darkness'; 'tār [tʾl M tʾr] darkness'; 'tārīg/k [tʾlyk ...] dark'.\"},\n   {\"src\":\"ARY\",\"where\":\"p.189 s.v. تار، تاریک (ocr/ARY/0189.png)\",\"stance\":\"supports\",\"note\":\"Aryanpur: 'AVESTAN TATHRA, TEMAH; PAHLAVI TAR, TARAG, TARIG, TUM, TUMIK; ... SANSKRIT TAMSRAS, TAMRAS, TAMISRA, TAMAS; LATIN TENEBRAE ... POKORNY 1063-1064 ... برهان قاطع ۴۵۶، ۵۱۱'; note: 'واژه‌ی فارسی «تم» (پردهٔ چشم یا آب مروارید) نیز از همین واجریشه است (POKORNY:1063)'.\"},\n   {\"src\":\"MON\",\"where\":\"vajehyab Mo'in s.v. تم\",\"stance\":\"silent\",\"note\":\"vajehyab's Mo'in entry for تم gives only the French loan تم 'theme' [فر.]; the native تم 'darkness, cataract' is not shown online.\"},\n   {\"src\":\"NYB\",\"where\":\"vol.2 p.191 s.v. tārīk\",\"stance\":\"supports\",\"note\":\"'tārīk < *tąθriya-ka-, Av. tąθrya- 'dark'; NP tār'.\"}]},\n {\"id\":3,\"lang\":\"Sogdian\",\"words\":\"tm\",\"verdict\":\"confirmed\",\n  \"derivation\":\"Sogdian tm /tam/ 'hell' (Buddhist, Manichaean and Christian texts) is the regular Sogdian continuant of Old Iranian *tamah- 'darkness' (Av. təmah-): final -ah lost, giving tam; the meaning narrowed from 'darkness' to 'the dark place, hell', exactly as Avestan uses təmah- for the abode of the wicked. Gharib entry 9588 glosses it 'hell' and derives it from Av. təmah-.\",\n  \"derivation_fa\":\"سغدی tm (تلفظ tam) «دوزخ» دنبالهٔ منظم ایرانی باستان *tamah- «تاریکی» (اوستایی təmah-) است که پایانهٔ -ah در آن افتاده است؛ معنا از «تاریکی» به «جای تاریک، دوزخ» تخصیص یافته، چنان‌که در اوستا نیز təmah- جایگاه بدکاران است. قریب در فرهنگ سغدی (مدخل ۹۵۸۸، ص۳۸۷) همین معنا و همین ریشه را آورده است؛ ادعای نورایی درست است.\",\n  \"sources\":[PIE],\n  \"ref_check\":[SODr],\n  \"consulted\":[BRTc,{\"src\":\"SOD\",\"where\":\"intro p.xxxi (SOD_pages.txt line 3135)\",\"stance\":\"supports\",\"note\":\"'/tam/ tm- hell  Av. təmah-, Skt. tamas' (as an example of Sogdian t < Olr. *t).\"}]},\n {\"id\":4,\"lang\":\"Latin\",\"words\":\"temĕre\",\"verdict\":\"transcription_suspect\",\n  \"error_in\":\"book\",\"book_prints\":\"temĕre : to fear\",\"correct_form\":\"temere (adv.) 'blindly, rashly, at random'; 'to fear' = timēre\",\n  \"derivation\":\"Latin temere is an adverb 'blindly, at random, rashly', a fossilised locative *temesi 'in the dark' from PIE *témHos 'darkness' (Pokorny, Walde-Pokorny, Watkins, Ernout-Meillet, Wiktionary); it is correctly placed under *temH-. But the book prints the gloss 'to fear', which belongs to the different verb timēre (Italian temere 'to fear' < Latin timēre may have caused the confusion). The extraction is faithful; this is Nourai's error in the book.\",\n  \"derivation_fa\":\"لاتین temere قیدی است به معنای «کورکورانه، بی‌پروا، به‌تصادف»، که حالت دری (locative) سنگ‌شدهٔ *temesi «در تاریکی» از هندواروپایی آغازین *témHos «تاریکی» است و جایش زیر ریشهٔ *temH- درست است. اما کتاب معنای آن را «ترسیدن» چاپ کرده که معنای فعل دیگری، timēre، است (شاید به سبب ایتالیایی temere «ترسیدن» که خود از timēre است). خطا از خود کتاب است، نه از استخراج.\",\n  \"sources\":[W+\"temere\",W+\"timeo\"],\n  \"ref_check\":[{\"ref\":\"AHD\",\"status\":\"supports\",\"note\":\"Watkins s.v. temə-: '1. Latin temere, blindly, rashly: TEMERARIOUS, TEMERITY. [Pok. tem(ə)- 1063.]' — supports temere under this root, with the gloss 'blindly, rashly', not 'to fear'.\"}],\n  \"consulted\":[{\"src\":\"POK\",\"where\":\"p.1063\",\"stance\":\"supports\",\"note\":\"'temere 'blindlings, aufs Geratewohl' (Lok. *temesi 'im Dunkeln [tappend]')'.\"},WLDc,{\"src\":\"LAT\",\"where\":\"s.v. temere (LAT.txt line 63323)\",\"stance\":\"supports\",\"note\":\"Ernout-Meillet: 'temere adv.: à l'aveuglette, par suite inconsidérément, au hasard ... proprement ablatif-instrumental d'un subst. *temus, -eris obscurité, cf. tenebrae'.\"},IECc]},\n {\"id\":5,\"lang\":\"English\",\"words\":\"timid, temerity\",\"verdict\":\"plausible\",\n  \"derivation\":\"temerity (ME temeryte, c.1450) < Latin temeritās 'rashness' < temere 'blindly, rashly' < *temH- 'dark' — confirmed (Watkins, Klein, Skeat). timid (1540s) < French timide < Latin timidus < timēre 'to fear'; timēre has no secure etymology: Klein and Skeat link it to the 'dark' root ('to grope in the dark'), but Watkins does not list it under temə-, Ernout-Meillet give no etymology, and Wiktionary calls the *temH- link 'semantically reasonable, but phonetically difficult'.\",\n  \"derivation_fa\":\"انگلیسی temerity «بی‌باکی، گستاخی» از لاتین temeritās، از temere «کورکورانه» و سرانجام از ریشهٔ هندواروپایی *temH- «تاریک» است و ادعای نورایی دربارهٔ آن درست است. اما timid «ترسو» از فرانسوی timide و لاتین timidus از فعل timēre «ترسیدن» است که ریشه‌اش روشن نیست؛ کلاین و اسکیت آن را به همین ریشهٔ «تاریکی» پیوند می‌دهند، ولی واتکینز آن را نیاورده و ویکی‌واژه این پیوند را از نظر آوایی دشوار می‌داند. پس برای timid ادعا تنها با احتیاط پذیرفتنی است.\",\n  \"sources\":[W+\"timeo\",W+\"temere\"],\n  \"ref_check\":[{\"ref\":\"AHD\",\"status\":\"partial\",\"note\":\"Watkins s.v. temə- lists TEMERARIOUS, TEMERITY only; timid is not derived from this root.\"}],\n  \"consulted\":[KLNtem,{\"src\":\"KLN\",\"where\":\"1966 s.v. timid (KLN_1966.txt line 39284)\",\"stance\":\"supports\",\"note\":\"'timid ... L. timidus ... fr. timere 'to fear', which prob. meant orig. 'to be in the dark, to grope about in the dark', and is rel. to tenebrae ... temere'.\"},\n   {\"src\":\"SKT\",\"where\":\"s.v. Temerity (SKT_dli_revised.txt line 79505); s.v. Timid (SKT.txt line 19736)\",\"stance\":\"partial\",\"note\":\"'Temerity ... L. adv. temere, rashly. The orig. sense of temere was 'in the dark'; cf. Skt. tamas, gloom'; 'Timid ... L. timere, to fear. Al. tam, to choke' (Skeat connects timere with Skt. tam- 'choke', not with 'dark').\"},\n   {\"src\":\"LAT\",\"where\":\"s.v. timeo (LAT.txt line 64505)\",\"stance\":\"contradicts\",\"note\":\"Ernout-Meillet give no etymology for timeo ('Les mots indo-européens signifiant craindre n'ont qu'une aire peu étendue ...').\"}]},\n {\"id\":6,\"lang\":\"Sanskrit\",\"words\":\"tâm-rah\",\"verdict\":\"confirmed\",\n  \"derivation\":\"Sanskrit tāmrá- adj. 'dark red, coppery', n. 'copper' (the hyphen in the book's tâm-rah is only a syllable break) is related to tamas- 'darkness', copper being a dark-coloured metal; Wiktionary reconstructs *tm̥H-ró- with ā perhaps analogical from tam-; Pokorny and Walde-Pokorny list tāmra- 'kupferrot' under tem(ə)-.\",\n  \"derivation_fa\":\"سنسکریت tāmra- «سرخ تیره، مسی» و «مس» (خط تیرهٔ «tâm-rah» در کتاب تنها مرز هجاست) با tamas- «تاریکی» هم‌ریشه است، چون مس فلزی تیره‌رنگ است؛ ویکی‌واژه صورت *tm̥H-ró- را بازسازی می‌کند و واکهٔ بلند ā را احتمالاً قیاسی می‌داند. پوکورنی و والده‌ـپوکورنی نیز tāmra- را زیر ریشهٔ *tem(ə)- آورده‌اند؛ ادعای نورایی درست است.\",\n  \"sources\":[W+\"ताम्र\",PIE],\n  \"ref_check\":[{\"ref\":\"KLN:1626\",\"status\":\"supports\",\"note\":\"Klein s.v. tombac: 'OI. tāmrakah ... fr. tāmráh, 'dark-red, coppery', which is rel. to tamas-, 'darkness'.' (entry found; exact page number not confirmed by leaf offset).\"}],\n  \"consulted\":[{\"src\":\"POK\",\"where\":\"p.1063\",\"stance\":\"supports\",\"note\":\"'tāmra- 'oxblood, indigo, kupferrot''.\"},WLDc,KLNtem]},\n {\"id\":7,\"lang\":\"Malaysian\",\"words\":\"tambaga\",\"verdict\":\"confirmed\",\n  \"derivation\":\"Malay tembaga (older/dialectal tambaga) 'copper, brass' was borrowed, via a Prakrit *taṃbaga, from Sanskrit tāmraka- 'copper' (tāmra + -ka); the cluster -mr- became -mb- in Middle Indic. The word spread with Indian trade into Javanese (Old Javanese tambaga), Malay and the Philippines.\",\n  \"derivation_fa\":\"مالایی tembaga (کهن‌تر tambaga) «مس، برنج» از راه پراکریت *taṃbaga از سنسکریت tāmraka- «مس» وام گرفته شده است؛ خوشهٔ -mr- در هندی میانه به -mb- بدل شده. این واژه با بازرگانی هندی به جاوه‌ای کهن و مالایی رسید. ادعای نورایی درست است.\",\n  \"sources\":[W+\"tembaga\"],\n  \"ref_check\":[KLNtomb],\n  \"consulted\":[HJBc,KLNtem]},\n {\"id\":8,\"lang\":\"Portuguese\",\"words\":\"tombac\",\"verdict\":\"plausible\",\n  \"derivation\":\"The Portuguese, trading in the Malay world from the early 16th c., took Malay tambaga as tambaca / tambaque 'copper alloy' (Hobson-Jobson: 'Port. tambaca'); modern Portuguese has tombaque. Klein's 'Port. tombac' is a simplified citation; the route is right but the Portuguese form is tambaca, not tombac.\",\n  \"derivation_fa\":\"پرتغالی‌ها که از آغاز سدهٔ شانزدهم در جهان مالایی بازرگانی می‌کردند، مالایی tambaga را به صورت tambaca / tambaque «آلیاژ مس» گرفتند (هابسن‌جابسن: Port. tambaca)؛ صورت امروزی پرتغالی tombaque است. مسیر وام‌گیری که نورایی به پیروی از کلاین آورده درست است، ولی صورت پرتغالی tombac نیست؛ پس ادعا با احتیاط پذیرفتنی است.\",\n  \"sources\":[W+\"tembaga\"],\n  \"ref_check\":[KLNtomb],\n  \"consulted\":[HJBc,{\"src\":\"LKT\",\"where\":\"grep tambaga/tombac\",\"stance\":\"silent\",\"note\":\"no entry found in Lokotsch for tambaga/tombac in the local OCR.\"}]},\n {\"id\":9,\"lang\":\"French\",\"words\":\"tombac\",\"verdict\":\"confirmed\",\n  \"derivation\":\"French tombac (attested from the early 17th c.) 'tombac, a copper-zinc alloy' was taken from Portuguese tambaca/tombaque, with the Malay final -a dropped and the first vowel rounded; it is the source of the English word.\",\n  \"derivation_fa\":\"فرانسوی tombac «تمباک، آلیاژ مس و روی» (از آغاز سدهٔ هفدهم) از پرتغالی tambaca/tombaque گرفته شده است؛ واکهٔ پایانی افتاده و واکهٔ نخست گرد شده است. انگلیسی tombac نیز از همین واژهٔ فرانسوی است؛ ادعای نورایی درست است.\",\n  \"sources\":[W+\"tombac\"],\n  \"ref_check\":[KLNtomb],\n  \"consulted\":[HJBc,FSDtomb]},\n {\"id\":10,\"lang\":\"English\",\"words\":\"tombac, tambaga\",\"verdict\":\"plausible\",\n  \"derivation\":\"English tombac (also tombak, tambac, 17th c.) is borrowed from French tombac (Wiktionary: 'Borrowed from French tombac'; Klein). 'tambaga' is not an established English word: it is the Malay/Philippine word cited in English dictionaries (Hobson-Jobson, Klein) as the etymon, so listing it as an English derivative is loose.\",\n  \"derivation_fa\":\"انگلیسی tombac (و گونه‌های tombak و tambac، از سدهٔ هفدهم) از فرانسوی tombac وام گرفته شده و این بخش درست است. ولی tambaga واژهٔ رایج انگلیسی نیست؛ واژه‌ای مالایی است که فرهنگ‌های انگلیسی (هابسن‌جابسن، کلاین) تنها به عنوان ریشه آورده‌اند. پس ادعای نورایی با احتیاط پذیرفتنی است.\",\n  \"sources\":[W+\"tombac\"],\n  \"ref_check\":[{\"ref\":\"OXF:435\",\"status\":\"not_checked\",\"note\":\"Oxford Dictionary of Foreign Words and Phrases is lending-only on archive.org; not readable.\"},KLNtomb],\n  \"consulted\":[HJBc,FSDtomb]}\n]\nnodes1=[\n {\"id\":1,\"lang\":\"Arabic\",\"words\":\"temara, t.m.r; matmŭrah\",\"verdict\":\"confirmed\",\n  \"derivation\":\"Arabic ṭamara (root ṭ-m-r, with emphatic ṭ) 'to bury, hide, fill up (a pit)', and maṭmūra, the feminine passive participle (maf'ūl pattern) 'something hidden', used for an underground silo/granary and later a subterranean dungeon. Fraenkel (p.137) argues the 'store underground' sense is borrowed from Syriac maṭmūrtā/maṭmōrā 'pit for hiding treasures' (from ṭmar 'to bury, hide'), since Old Arabic lacks that meaning; Wiktionary follows him. Nourai's 'temara' is a loose transliteration of ṭamara.\",\n  \"derivation_fa\":\"عربی «طَمَرَ» (ریشهٔ ط م ر) «دفن کردن، نهان کردن» و «مَطمورة» اسم مفعول مؤنث (بر وزن مفعول) به معنای «چیز نهان‌شده»، سپس «انبار زیرزمینی غله» و بعدها «سیاه‌چال». فرانکل (ص۱۳۷) معنای «انبار زیرزمینی» را وام از سریانی maṭmūrtā (از ṭmar «دفن کردن، پنهان کردن») می‌داند، چون این معنا در عربی کهن نیست؛ ویکی‌واژه نیز همین را می‌گوید. ادعای نورایی درست است؛ «temara» تنها نویسه‌گردانی آزادِ ṭamara است.\",\n  \"sources\":[W+\"مطمورة\"],\n  \"ref_check\":[KLNmatt],\n  \"consulted\":[AFAc,DEVc,PHNc,LAMc]},\n {\"id\":2,\"lang\":\"Persian\",\"words\":\"matmŭreh\",\"verdict\":\"confirmed\",\n  \"derivation\":\"Persian maṭmūre مطموره 'underground store, hidden chamber' is the Arabic maṭmūra borrowed with the Arabic tā' marbūṭa rendered as -e; Mo'in marks it [ع.] 'نهان خانه'. Its use by Manūchehrī (11th c.), quoted on the page, shows it was current in early New Persian.\",\n  \"derivation_fa\":\"«مطموره» در فارسی (نهان‌خانه، انبار زیرزمینی) همان عربی «مطمورة» است که تای مدوّر آن در فارسی به «ـه» بدل شده؛ معین آن را با نشان [ع.] و معنای «نهان خانه» آورده است. کاربرد آن در شعر منوچهری (سدهٔ پنجم هجری) نشان می‌دهد که در فارسی دری کهن رایج بوده است. ادعای نورایی درست است.\",\n  \"sources\":[\"https://vajehyab.com/moein/مطموره\",W+\"مطمورة\"],\n  \"ref_check\":[{\"ref\":\"FVA:251\",\"status\":\"not_checked\",\"note\":\"Nahvi, Farhang-e Vazheha-ye Arabi dar Farsi: no digital copy (refs_online.json).\"},{\"ref\":\"MON\",\"status\":\"supports\",\"note\":\"vajehyab Mo'in s.v. مطموره: '(مَ رِ) [ع.] (اِ.) نهان خانه.'\"}],\n  \"consulted\":[AFAc,{\"src\":\"MON\",\"where\":\"MON_part1/part2 local OCR\",\"stance\":\"silent\",\"note\":\"grep 'مطمور' in the local 2-vol Mo'in abridgement finds nothing; online Mo'in (vajehyab) has it as [ع.] 'نهان خانه'.\"},{\"src\":\"AFM\",\"where\":\"grep مطمور / طمر\",\"stance\":\"silent\",\"note\":\"Addi Shir does not list it (not a Persian loan into Arabic).\"}]},\n {\"id\":3,\"lang\":\"French\",\"words\":\"matamore\",\"verdict\":\"plausible\",\n  \"derivation\":\"French matamore (fem.) 'underground silo for grain, used by the Moors; also a subterranean prison for captives' comes from Arabic maṭmūra (North African pronunciation maṭmōra), via Spanish/Portuguese mazmorra, masmorra, matamorra (Devic, Pihan, Lammens). Nourai's gloss 'a dwelling place' is loose: the sources give 'silo, underground storehouse, dungeon'. It is a homonym of matamore (masc.) 'braggart' from Spanish Matamoros 'Moor-killer', which Pihan warns not to confuse.\",\n  \"derivation_fa\":\"فرانسوی matamore (مؤنث) «انبار زیرزمینی غله نزد مغربیان؛ نیز سیاه‌چال اسیران» از عربی مطمورة (به تلفظ مغربی maṭmōra) و از راه اسپانیایی و پرتغالی mazmorra / masmorra آمده است (دویک، پیهان، لامنس). معنای «جای سکونت» که نورایی آورده دقیق نیست؛ منابع «انبار زیرزمینی، سیاه‌چال» می‌گویند. این واژه را نباید با matamore (مذکر) «لاف‌زن» از اسپانیایی Matamoros یکی گرفت. ادعای نورایی دربارهٔ اصل واژه درست ولی معنایش با احتیاط پذیرفتنی است.\",\n  \"sources\":[W+\"mazmorra\",W+\"مطمورة\"],\n  \"ref_check\":[KLNmatt],\n  \"consulted\":[DEVc,PHNc,LAMc]},\n {\"id\":4,\"lang\":\"English\",\"words\":\"mattamore\",\"verdict\":\"confirmed\",\n  \"derivation\":\"English mattamore (17th c., travellers' accounts of North Africa and the Levant) 'a subterranean dwelling, storehouse or dungeon' is borrowed from French matamore, itself from Arabic maṭmūra; Klein and Funk & Wagnalls give exactly this chain.\",\n  \"derivation_fa\":\"انگلیسی mattamore (از سدهٔ هفدهم، در سفرنامه‌های شمال آفریقا و شام) «جایگاه یا انبار یا زندان زیرزمینی» از فرانسوی matamore و آن از عربی «مطمورة» است؛ کلاین و فانک‌ووگنالز همین زنجیره را آورده‌اند. ادعای نورایی درست است.\",\n  \"sources\":[W+\"مطمورة\"],\n  \"ref_check\":[KLNmatt],\n  \"consulted\":[FSDmatt,{\"src\":\"SKT\",\"where\":\"grep mattamore\",\"stance\":\"silent\",\"note\":\"not in Skeat.\"},{\"src\":\"HJB\",\"where\":\"grep mattamore\",\"stance\":\"silent\",\"note\":\"not in Hobson-Jobson.\"}]}\n]\nout={\"pdf_page\":500,\"book_page\":470,\"verified_by\":\"claude-opus-5\",\"verified_on\":\"2026-10-14\",\"entries\":[\n {\"entry\":0,\"root\":\"Tem\",\"verdict\":\"confirmed\",\n  \"modern_form\":\"PIE *temH- 'dark' (Pokorny tem(ə)- 1063-1064; Watkins temə-; *témHos 'darkness')\",\n  \"note\":\"Root, label and gloss correct (Pokorny 1063 'tem(ə)- dark'; Watkins temə- 'dark'). The Iranian, Sogdian, Sanskrit and tombac branches are standard. Problems: the Latin box prints 'temĕre : to fear' — temere is the adverb 'blindly, rashly'; 'to fear' is timēre (book error, extraction faithful); English timid (< timēre) is only uncertainly linked to this root; 'tethra' is Nourai's rendering of Av. tąθra- (after Mo'in's 'tathra'); Portuguese form is tambaca, and 'tambaga' is not really English. No extraction errors: the JSON matches the printed page.\",\n  \"note_fa\":\"ریشهٔ هندواروپایی آغازین *temH- «تاریک» (پوکورنی ۱۰۶۳: tem(ə)-؛ واتکینز temə-) است و برچسب و معنای نورایی درست است. شاخه‌های اوستایی، فارسی (تم، تار، تاریک)، سغدی، سنسکریت و زنجیرهٔ «تمباک» پذیرفته‌اند. اشکال‌ها: در خانهٔ لاتین معنای temere «ترسیدن» چاپ شده، حال آنکه temere قیدی به معنای «کورکورانه» است و «ترسیدن» timēre است (خطای چاپی کتاب)؛ پیوند timid با این ریشه قطعی نیست؛ «tethra» همان tąθra- اوستایی است؛ صورت پرتغالی tambaca است و tambaga واژهٔ انگلیسی نیست. خطای استخراج دیده نشد.\",\n  \"sources\":[PIE,W+\"temere\",W+\"ताम्र\"],\n  \"ref_check\":[POKr],\n  \"consulted\":[WLDc,AHDc,IECc,KLNtem,{\"src\":\"SYN\",\"where\":\"§1.62 'dark'\",\"stance\":\"silent\",\"note\":\"not checked in detail; Buck's section on 'darkness' (cited by Aryanpur as Buck 61) lists Skt. tamas, Av. təmah under this root.\"}],\n  \"nodes\":nodes0},\n {\"entry\":1,\"root\":\"Temar\",\"verdict\":\"confirmed\",\n  \"modern_form\":\"Aramaic/Syriac ṭ(ə)mar 'to bury, hide' (Semitic root ṭ-m-r; cf. Akkadian ṭamāru, Hebrew ṭāman)\",\n  \"note\":\"Klein (s.v. mattamore, citing Fraenkel p.137) gives exactly this root: Aram. ṭ'mar 'he hid, concealed' > Arabic ṭamara / maṭmūra. Fraenkel and Wiktionary hold that the 'underground store' sense of Arabic maṭmūra was borrowed from Syriac maṭmūrtā. The root's emphatic ṭ is not marked in 'Temar'. The French gloss 'a dwelling place' is loose (silo/dungeon). No extraction errors.\",\n  \"note_fa\":\"ریشهٔ آرامی/سریانی ṭmar «دفن کردن، پنهان کردن» (ریشهٔ سامی ط م ر؛ قس: اکدی ṭamāru، عبری ṭāman) است و کلاین به نقل از فرانکل (ص۱۳۷) همین را آورده است: آرامی ṭ'mar ← عربی طمر و مطمورة. فرانکل و ویکی‌واژه معنای «انبار زیرزمینی» مطمورة را وام از سریانی maṭmūrtā می‌دانند. ادعای نورایی درست است؛ تنها معنای «جای سکونت» برای فرانسوی matamore دقیق نیست و خطای استخراج دیده نشد.\",\n  \"sources\":[W+\"مطمورة\"],\n  \"ref_check\":[KLNmatt],\n  \"consulted\":[AFAc,{\"src\":\"FVQ\",\"where\":\"grep matmur/طمر\",\"stance\":\"silent\",\"note\":\"not a Qur'anic word; Jeffery silent.\"}],\n  \"nodes\":nodes1}\n]}\njson.dump(out,open(\"/home/sfmqrb/git/rishe-private/data/verification/page-500.json\",\"w\",encoding=\"utf-8\"),ensure_ascii=False,indent=1)\nEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/build-500.py && python3 -m json.tool /home/sfmqrb/git/rishe-private/data/verification/page-500.json >/dev/null && python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py 500"
}
```


### [2026-10-15T02:50:43.628Z] TOOL RESULT

```
nodes verified: 14/14
node verdicts: {'plausible': 6, 'confirmed': 7, 'transcription_suspect': 1}
root verdicts: {'confirmed': 2}
ref checks: {'supports': 15, 'partial': 1, 'not_checked': 2}
books consulted: {'supports': 32, 'partial': 4, 'silent': 6, 'contradicts': 1} | by book: {'HJB': 5, 'KLN': 4, 'WLD': 3, 'FSD': 3, 'BRT': 2, 'NYB': 2, 'MON': 2, 'POK': 2, 'LAT': 2, 'SKT': 2, 'AFA': 2, 'DEV': 2, 'PHN': 2, 'LAM': 2, 'HRN': 1, 'HUB': 1, 'PHD': 1, 'ARY': 1, 'SOD': 1, 'IEC': 1, 'LKT': 1, 'AFM': 1}
```


## [2026-10-15T02:50:47.723Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i -E 'tambag|tombac|tembag' LKT.txt | head -3; grep -n -i -E 'tamas' SYN.txt | head -5; grep -n 'مطمور\\|طمر' AFM.txt | head -2"
}
```


### [2026-10-15T02:50:48.080Z] TOOL RESULT

```
4530:g()i9  Mal,  tambäga: Kupfer'  [Pijn  68;  aus  sskr.  tanuka,  ei- gentlich 'das  dunkle  Metall',  also  'Kup- fer'; vgl.  A.  A.  E.  Schleiermacher,  De l'influence  de  l'ecriture  sur  le  langage suivi  de  grammaires  barmane  et  ma- laie.  Darmstadt  1835.  S.  537,  nicht S.  835,  wie  POTT  in  ZKM  IV,  265  an- gibt]; hieraus  zur  Bezeichnung  einer Legierung  von  Kupfer  (A^/i — 12  Teile) und  Zink  (1  Teil)  pg.  tambaque,  tambaca, sp.  tumbaga,  frz.  tombac,  it.  tombacco ; engl,  tomback,  dtsch.  Tombak  ;  russ.  tom- pak.  —  [Die  Ableitung  aus  dem  Namen eines  Engländers  DOMBACK  ist  un- bewiesen ;  ebenso  unwahrscheinlich  ist die  Entstehung  aus  dem  umgestellten chin.  pack-tang  'weißes  Kupfer'  >  tong- pack.]  [Devii-  DEt  221.  Hobson-Jobson 829.
6203:tomback  2012
7236:tofferanu  sard.  2178 I  tombacco  2012
1835:THE PHYSICAL WORLD IN ITS LARGER ASPECTS 61 1.62 DARKNESS Goth. rigis Lith. tamsa Grk. ita oKorade ON myrkr Lett. tumsa NGS ie faa Dan. mérke ChSl.  tima, mrakit vee oe buio, oscurita Sw. morker SCr. tmina, tama, mrak he téndbres obscurité OE péostru, mirce, deorc- Boh. temnota, tma i ta ieblas nes Pol. ciemnosé, éma BD. intuneric ME — mirk, derk(nes) Rubs: | ternnole Uncen se temel, dorche NE — dark(ness) Skt.  tamas-, timira-, ie dorchadas, doircheacht Du. duistermis, donker ; andhakara- W.  _ tywyllweh OHG  finstarnissi, tunchali Ay. _ tamah-, tqfra- Br. tenvalienn, ame’hou- MHG ee tunkel : -heit sa NHG  finsterniss, dunkel
1839:Skt. tamas-, tamisra-, timira-, Av. tamah-, tadra-; Lat. tenebrae (fr. *temes- ra-, cf. Skt. tamisra-), It. tenebre, Fr. ténébres, Sp. tinieblas, Rum. itntuneric (fr. *tn-tenebricus); Ir. temel (here also perh. ultimately Br. tefvalienn, fr. adj. terval ‘dark’, and even W. tywyllwch, fr. adj. tywyll ‘dark’, the latter by a blend with gwyll ‘gloom, darkness’ ; ef. Loth, RC 18.95 f.); OHG finstarnissi (dinstar, Jinstar ‘dark’), NHG finsterniss (cf. also me sled NHG démmerung ‘twi- a Lae s amsa, Lett. tumsa; ChSl.
25341:NHG morgendémmerung, lit. ‘morn- ing-twilight’, (démmerung, OHG demar ‘twilight’ : Skt. tamas- ‘darkness’, etc., 1.62).
26642:15.63 DARK (in Color) Grk. —_péAas, xedarvds Goth.~ i... Lith. tamsus NG Babbs, oxodpos ON dékkr Lett. tums Lat. fuscus, pullus Dan. mérk, dunkel ChSl.  timinit It. scuro, cupo Sw. mork, dunkel SCr.  taman Fr. foncé, sombre OE wann. (deorc) Boh. temny Sp. obscuro ME dark, wan, dosc Pol. ciemny Rum. inchis NE dark Russ. temnyj Tr. dorche, temen Du. donker Skt. krsna-, ¢yama-, Nir. dorcha OHG  tunchal tamasa- W. tywyll MHG _ tunkel Av. axSaéna- Br. du NHG dunkel
26645:Ir. temen, temnide (here also W. tywyll? cf. ref. in 1.62); Lith. tamsus, Lett. tumss; ChSl. timtni, SCr. taman, etc., general Slavic; Skt. tamasa- (AV 11.9.22).
5106:قرمزء ٠‏ 37 اطمرة قدر 5 9 الرانحة بقع على الشجر
```


## [2026-10-15T02:50:56.133Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad; python3 - <<'EOF'\np='build-500.py'; s=open(p).read()\ns=s.replace('''{\"src\":\"LKT\",\"where\":\"grep tambaga/tombac\",\"stance\":\"silent\",\"note\":\"no entry found in Lokotsch for tambaga/tombac in the local OCR.\"}''','''{\"src\":\"LKT\",\"where\":\"no. 2012 (LKT.txt line 4530)\",\"stance\":\"supports\",\"note\":\"'Mal. tambāga 'Kupfer' [aus sskr. tāmraka, eigentlich 'das dunkle Metall' ...]; hieraus zur Bezeichnung einer Legierung von Kupfer und Zink pg. tambaque, tambaca, sp. tumbaga, frz. tombac, it. tombacco; engl. tomback' — Portuguese form tambaque/tambaca.\"}''')\ns=s.replace('''{\"src\":\"SYN\",\"where\":\"§1.62 'dark'\",\"stance\":\"silent\",\"note\":\"not checked in detail; Buck's section on 'darkness' (cited by Aryanpur as Buck 61) lists Skt. tamas, Av. təmah under this root.\"}''','''{\"src\":\"SYN\",\"where\":\"§1.62 DARKNESS, p.61 (SYN.txt line 1839)\",\"stance\":\"supports\",\"note\":\"Buck: 'Skt. tamas-, tamisra-, timira-, Av. təmah-, tąθra-; Lat. tenebrae (fr. *temes-rā-, cf. Skt. tamisra-) ... Ir. temel ... Lith. tamsa, Lett. tumsa; ChSl. tĭma'.\"}''')\nopen(p,'w').write(s)\nEOF\npython3 build-500.py && python3 -m json.tool /home/sfmqrb/git/rishe-private/data/verification/page-500.json >/dev/null && python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py 500 | grep -c PROBLEM; ls /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BOOK/500.png"
}
```


### [2026-10-15T02:50:56.868Z] TOOL RESULT

```
0
Permissions Size User   Date Modified Name
.rw-r--r--   41k sfmqrb 14 Oct 22:46  /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BOOK/500.png
```


## [2026-10-15T02:51:05.463Z] TOOL CALL #53: SubagentHandback

```json
{
 "message": "Page 500 is done and written to `/home/sfmqrb/git/rishe-private/data/verification/page-500.json`. `verify_check.py 500` reports 0 PROBLEM lines. It covers 2 entries and 14 nodes; the Temp → Ten 1 redirect was skipped.\n\n**Verdicts:**\n- **Roots:** 2 confirmed. Tem is PIE *temH- \"dark\" (Pokorny 1063); Temar is Aramaic ṭmar \"hid\" (Klein, citing Fraenkel p.137).\n- **Nodes:** 7 confirmed, 6 plausible, 1 transcription_suspect, 0 disputed.\n- **Nourai's own references:** 15 support, 1 partial, 2 not checked. The two not checked are OXF:435 (lending-only) and FVA:251 (no digital copy).\n\n**Flagged item:**\n- **transcription_suspect, Tem / Latin \"temĕre : to fear\":** Latin temere is an adverb meaning \"blindly, rashly\". \"To fear\" is the meaning of a different verb, timēre (Italian temere \"to fear\" comes from timēre). The error is in the printed book; the extraction matches the page. I copied the page image to `data/verification/sources/refs/ocr/BOOK/500.png`.\n\n**Main plausible notes:**\n- **\"timid\":** it comes from timēre, whose link to *temH- is uncertain. Watkins leaves it out and Wiktionary calls the link \"phonetically difficult\".\n- **Avestan \"tethra\":** this is Nourai's spelling of tąθra-, taken from Mo'in's \"tathra\".\n- **تیره (tīre):** Mo'in (after Nyberg) derives it from *tąθrya-ka-, but that step is less certain.\n- **Portuguese form:** it is tambaca/tambaque, not tombac.\n- **\"tambaga\":** it is the Malay source word, not really an English word.\n- **French matamore:** it means \"silo, underground store, dungeon\", so Nourai's gloss \"a dwelling place\" is loose.\n\n**Extraction errors:** none. The JSON matches the printed page.\n\n**Other files added:**\n- Borhan-e Qate' pp. 456, 511 and 544 (all in vol. 1). I read the archive.org page images and saved the entries with Mo'in's footnotes in `ocr/BQT/0456|0511|0544.vision.txt`, with the matching `.jpg` files.\n- Aryanpur p.189 is in `ocr/ARY/0189.png`.\n- Web pages I relied on are archived with `fetch_source.py`. The Etymonline fetches failed, so they are not cited."
}
```


### [2026-10-15T02:51:05.757Z] TOOL RESULT

```
{"success":true,"message":"Report delivered to your caller."}
```
