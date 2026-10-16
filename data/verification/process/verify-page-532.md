# Verification process log — verify-page-532


## [2026-10-16T05:13:01.968Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 532 only. Chart text: /home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-532.txt; source JSON: /home/sfmqrb/git/rishe-private/data/extracted/batch/page-532.json. Write /home/sfmqrb/git/rishe-private/data/verification/page-532.json, run `python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py 532` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-10-16T05:13:02.035Z] INPUT

<system-reminder>
Your final report is delivered through SubagentHandback: when your work is complete, call SubagentHandback({message: <your full report>}). The call ends your run, so make it your last step. Only a SubagentHandback call reaches your caller as your result; plain text you write at the end is not delivered.
</system-reminder>


## [2026-10-16T05:13:06.098Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-10-16T05:13:06.117Z] TOOL RESULT

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


## [2026-10-16T05:13:06.632Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-532.txt"
}
```


### [2026-10-16T05:13:06.787Z] TOOL RESULT

```
1	=== PDF page 532 (book page 502) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Wegwh, Ewegwh, Euegh : to speak solemnly  (refs POK:348)
4	#1 (parent #0) [Old Persian] refs=TZF:29 | aok : to speak ; paiti-aok : counter speech, response ☞Per 3 | NOTE: Connection to this root is doubtful
5	  #2 (parent #1) [Persian] refs=TZF:29 | pâsox «پاسخ» : response | NOTE: See Root "Kâs 2" for another possible derivation
6	#3 (parent #0) [Avestan] refs=POK:348; KLN:1722; SYN:1256; AVG:237 | aog, aoj, aox : to speak ; aojaiti, aoxia, aogeda ; duš-uxta : ill-spoken ☞Dus
7	#4 (parent #0) [Latin] refs=AHD | vověre : to pledge
8	  #5 (parent #4) [English] refs=None | vote, devote, vow
9	--- entry 1 ---
10	ROOT [Indo-European] Wei 1 : to bend, turn, twist  (refs POK:1120)
11	#1 (parent #0) [Avestan] refs=KLN:1749; ISS:42 | vay 3 : twist ; vaěiti : willow tree ; varaša : tree
12	  #2 (parent #1) [Pahlavi] refs=MON:58; SNS:287; BQT:338; ISS:42 | vět : willow ; vîsag, vîsak : wooded area
13	    #3 (parent #2) [Persian] refs=BQT:332,338; SNS:287; ISS:42 | běd «بید» : willow tree ; bîšeh «بیشه» : grove, woods
14	#4 (parent #0) [Germanic] refs=AHD | wi-ra
15	  #5 (parent #4) [English] refs=None | wire
16	#6 (parent #0) [Greek] refs=AHD | iris : rainbow
17	  #7 (parent #6) [English] refs=None | iris
18	
```


## [2026-10-16T05:13:07.278Z] TOOL CALL #3: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/extracted/batch/page-532.json"
}
```


### [2026-10-16T05:13:07.380Z] TOOL RESULT

```
1	{
2	  "pdf_page": 532,
3	  "book_page": 502,
4	  "entries": [
5	    {
6	      "root": {
7	        "name": "Wegwh, Ewegwh, Eueguh",
8	        "lang": "Indo-European",
9	        "refs": "POK:348",
10	        "gloss": "to speak solemnly"
11	      },
12	      "nodes": [
13	        {
14	          "id": 1,
15	          "parent": 0,
16	          "lang": "Old Persian",
17	          "refs": "TZF:29",
18	          "words": [
19	            {
20	              "translit": "aok",
21	              "gloss": "to speak",
22	              "script": null
23	            },
24	            {
25	              "translit": "paiti-aok",
26	              "gloss": "counter speech, response",
27	              "script": null,
28	              "see": [
29	                "Per 3"
30	              ]
31	            }
32	          ],
33	          "note": "Connection to this root is doubtful",
34	          "quote": null
35	        },
36	        {
37	          "id": 2,
38	          "parent": 1,
39	          "lang": "Persian",
40	          "refs": "TZF:29",
41	          "words": [
42	            {
43	              "translit": "pâsox",
44	              "gloss": "response",
45	              "script": "پاسخ"
46	            }
47	          ],
48	          "note": "See Root \"Kâs 2\" for another possible derivation",
49	          "quote": null
50	        },
51	        {
52	          "id": 3,
53	          "parent": 0,
54	          "lang": "Avestan",
55	          "refs": "POK:348; KLN:1722; SYN:1256; AVG:237",
56	          "words": [
57	            {
58	              "translit": "aog, aoj, aox",
59	              "gloss": "to speak",
60	              "script": null
61	            },
62	            {
63	              "translit": "aojaiti, aoxia, aogeda",
64	              "gloss": null,
65	              "script": null
66	            },
67	            {
68	              "translit": "duš-uxta",
69	              "gloss": "ill-spoken",
70	              "script": null,
71	              "see": [
72	                "Dus"
73	              ]
74	            }
75	          ],
76	          "note": null,
77	          "quote": null
78	        },
79	        {
80	          "id": 4,
81	          "parent": 0,
82	          "lang": "Latin",
83	          "refs": "AHD",
84	          "words": [
85	            {
86	              "translit": "vověre",
87	              "gloss": "to pledge",
88	              "script": null
89	            }
90	          ],
91	          "note": null,
92	          "quote": null
93	        },
94	        {
95	          "id": 5,
96	          "parent": 4,
97	          "lang": "English",
98	          "refs": null,
99	          "words": [
100	            {
101	              "translit": "vote, devote, vow",
102	              "gloss": null,
103	              "script": null
104	            }
105	          ],
106	          "note": null,
107	          "quote": null
108	        }
109	      ]
110	    },
111	    {
112	      "root": {
113	        "name": "Wei 1",
114	        "lang": "Indo-European",
115	        "refs": "POK:1120",
116	        "gloss": "to bend, turn, twist"
117	      },
118	      "nodes": [
119	        {
120	          "id": 1,
121	          "parent": 0,
122	          "lang": "Avestan",
123	          "refs": "KLN:1749; ISS:42",
124	          "words": [
125	            {
126	              "translit": "vay 3",
127	              "gloss": "twist",
128	              "script": null
129	            },
130	            {
131	              "translit": "vaěiti",
132	              "gloss": "willow tree",
133	              "script": null
134	            },
135	            {
136	              "translit": "varaša",
137	              "gloss": "tree",
138	              "script": null
139	            }
140	          ],
141	          "note": null,
142	          "quote": null
143	        },
144	        {
145	          "id": 2,
146	          "parent": 1,
147	          "lang": "Pahlavi",
148	          "refs": "MON:58; SNS:287; BQT:338; ISS:42",
149	          "words": [
150	            {
151	              "translit": "vět",
152	              "gloss": "willow",
153	              "script": null
154	            },
155	            {
156	              "translit": "vîsag, vîsak",
157	              "gloss": "wooded area",
158	              "script": null
159	            }
160	          ],
161	          "note": null,
162	          "quote": null
163	        },
164	        {
165	          "id": 3,
166	          "parent": 2,
167	          "lang": "Persian",
168	          "refs": "BQT:332,338; SNS:287; ISS:42",
169	          "words": [
170	            {
171	              "translit": "běd",
172	              "gloss": "willow tree",
173	              "script": "بید"
174	            },
175	            {
176	              "translit": "bîšeh",
177	              "gloss": "grove, woods",
178	              "script": "بیشه"
179	            }
180	          ],
181	          "note": null,
182	          "quote": {
183	            "text": "دل صنوبریم همچو بید لرزانست - زحسرت قد و بالای چون صنوبر دوست",
184	            "poet": "Hâfez"
185	          }
186	        },
187	        {
188	          "id": 4,
189	          "parent": 0,
190	          "lang": "Germanic",
191	          "refs": "AHD",
192	          "words": [
193	            {
194	              "translit": "wi-ra",
195	              "gloss": null,
196	              "script": null
197	            }
198	          ],
199	          "note": null,
200	          "quote": null
201	        },
202	        {
203	          "id": 5,
204	          "parent": 4,
205	          "lang": "English",
206	          "refs": null,
207	          "words": [
208	            {
209	              "translit": "wire",
210	              "gloss": null,
211	              "script": null
212	            }
213	          ],
214	          "note": null,
215	          "quote": null
216	        },
217	        {
218	          "id": 6,
219	          "parent": 0,
220	          "lang": "Greek",
221	          "refs": "AHD",
222	          "words": [
223	            {
224	              "translit": "iris",
225	              "gloss": "rainbow",
226	              "script": null
227	            }
228	          ],
229	          "note": null,
230	          "quote": null
231	        },
232	        {
233	          "id": 7,
234	          "parent": 6,
235	          "lang": "English",
236	          "refs": null,
237	          "words": [
238	            {
239	              "translit": "iris",
240	              "gloss": null,
241	              "script": null
242	            }
243	          ],
244	          "note": null,
245	          "quote": null
246	        }
247	      ]
248	    }
249	  ]
250	}
```


## [2026-10-16T05:13:11.821Z] TOOL CALL #4: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification; ls | tail -5; cat sources/SOURCE_MATRIX.md | head -80; python3 -c \"\nimport json;d=json.load(open('sources/refs_online.json'))\nfor k in ['POK','WLD','AHD','IEC','SYN','BRT','KNT','PHD','NYB','HRN','HUB','CHEUNG','BQT','MON','ARY','KLN','SKT','TZF','AVG','ISS','SNS','ISS_alt_DKS','FSD','WEB']:\n  print(k, json.dumps(d.get(k),ensure_ascii=False)[:400])\n\"; ls sources/refs/"
}
```


### [2026-10-16T05:13:12.275Z] TOOL RESULT

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
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/source
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe-private/data/verifica
KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "loca
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe-private/data
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 
CHEUNG null
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
TZF {"title": "Mohsen Abolghasemi, Tarikh-e Mokhtasar-e Zaban-e Farsi, Bonyad-e Andisheh-ye Eslami 1373/1994", "kind": "website", "url": "https://ketabnak.com/book/81646 (142 pp. PDF; login) ; https://farhangoadabeirani.blogsky.com/1395/07/20/post-1048/ (download post)", "lookup_hint": "Not on archive.org (only his دستور تاریخی زبان فارسی: archive.org/details/20220417_20220417_2237, and تاریخ زبان فار
AVG {"title": "A. V. W. Jackson, An Avesta Grammar in Comparison with Sanskrit, Part I, Stuttgart 1892", "edition_found": "1892", "kind": "archive_djvu", "url": "https://archive.org/details/pt1avestagrammar00jackuoft", "identifier": "pt1avestagrammar00jackuoft (also an-avesta-grammar-in-comparison-with-sanskrit, in.ernet.dli.2015.47742)", "local_file": "/home/sfmqrb/git/rishe-private/data/verification
ISS {"title": "H. W. Bailey, Indo-Scythian Studies: Khotanese Texts VI (Prolexis to the Book of Zambasta), Cambridge 1967", "edition_found": "not found; Bailey's Dictionary of Khotan Saka (1979) downloaded as the closest substitute", "kind": "google_books_preview+archive_restricted", "url": "https://books.google.com/books?id=4upthUgWo9YC (CUP 2009 reprint, partial preview) ; HathiTrust mdp.39015034317
SNS {"title": "Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/VajnameShayest", "lookup_hint": "grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php
ISS_alt_DKS null
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-D
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-di
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
```


## [2026-10-16T05:13:15.435Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; ls data/verification/page-5*.json | tail; sed -n 1,200p tools/verify_check.py | grep -n -i -E \"problem|warn|require|consulted|sources\" | head -60"
}
```


## [2026-10-16T05:13:16.104Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 -c \"\nimport json;d=json.load(open('data/verification/page-531.json'))\nprint(json.dumps(d['entries'][0],ensure_ascii=False,indent=1)[:5000])\""
}
```


### [2026-10-16T05:13:16.394Z] TOOL RESULT

```
.rw-r--r--   54k sfmqrb 14 Oct 22:55  data/verification/page-509.json
.rw-r--r--   33k sfmqrb 14 Oct 22:50  data/verification/page-510.json
.rw-r--r--   73k sfmqrb 14 Oct 22:57  data/verification/page-511.json
.rw-r--r--   47k sfmqrb 14 Oct 22:50  data/verification/page-512.json
.rw-r--r--   56k sfmqrb 14 Oct 22:53  data/verification/page-513.json
.rw-r--r--   40k sfmqrb 14 Oct 22:50  data/verification/page-514.json
.rw-r--r--   22k sfmqrb 14 Oct 22:47  data/verification/page-515.json
.rw-r--r--   36k sfmqrb 14 Oct 22:51  data/verification/page-516.json
.rw-r--r--   32k sfmqrb 14 Oct 22:48  data/verification/page-517.json
.rw-r--r--   20k sfmqrb 14 Oct 22:48  data/verification/page-518.json
22:    missing_pages, problems = [], []
46:            problems.append(f"page {pg}: invalid JSON ({ex})")
52:                problems.append(f"page {pg}: entry {i} ({e['root']['name']}) missing")
56:                problems.append(f"page {pg}: entry {i} root verdict {rv!r} invalid")
65:                    problems.append(f"page {pg}: entry {i} ({e['root']['name']}) node #{n['id']} missing")
69:                    problems.append(f"page {pg}: entry {i} node #{n['id']} verdict {nv!r} invalid")
74:                    problems.append(f"page {pg}: entry {i} node #{n['id']} has no derivation")
79:                for c in vn.get("consulted") or []:
86:    print("books consulted:", dict(con_tally), "| by book:", dict(con_books.most_common(40)))
89:    for p in problems:
90:        print("PROBLEM:", p)
94:    return 1 if problems else 0
```


### [2026-10-16T05:13:16.513Z] TOOL RESULT

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 2, in <module>
    import json;d=json.load(open('data/verification/page-531.json'))
                            ~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: 'data/verification/page-531.json'
```


## [2026-10-16T05:13:18.917Z] AGENT

Now the research. Starting with Pokorny and the local IE books.


## [2026-10-16T05:13:21.123Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E \"eu̯egʷh|euegh|eu̯eg|uegʷh|u̯egʷh\" POK_full.txt | head -20; echo ---; grep -n -E \"^ *(\\S*)?u̯ei-1|u̯ei- *1|wei-1\" POK_full.txt | head; echo ---AHD; grep -n -E \"^ *wegwh|^ *wei-|wegʷh|egwh\" AHD_watkins1985.txt | head"
}
```


### [2026-10-16T05:13:21.515Z] TOOL RESULT

```
---
---AHD
668:legwh-. Light, having little weight. 1. Suffixed form *legeh-t- in Germanic */iht()az in: a. Old English Jiht, léoht, light: LicHT?; b. Old English /ihtan, to lighten: LIGHTER?. 2. Suffixed form *legvh-u-i- in Latin levis (> Old French Jeger), light, with its derivative levdre, to lighten, raise: LEAVEN, LEVER, LEVITY; ALLEVIATE, CARNIVAL, ELEVATE, LEGERDEMAIN, LEVIGATE, (MEZZO-RELIEVO), RELIEVE. 3. Variant form *lagvh- in Old Irish /i-, small: LEPRECHAUN. 4. Nasalized form *l(e)ngeh- in Germanic *lung- in Old English lungen, lungs (from their lightness): LUNG. 5. Attributed by some to this root is Latin oblivisci, to forget, which is more likely from lei-. [Pok. legzh- 660.]
776:sively, very (< *ne-mi-s, “not little”; *mi-, little; see mei-2): NIMIETY. 4. Latin nihilum, nothing (< *nehilum, “not a whit, nothing at all”; hilum, a thing, trifle; origin unknown), contracted to nihil, nil, nothing: NIHILISM, (NIHILITY), NIL; ANNIHILATE. 5. Latin non, not (< *ne-oinom, “not one thing”; *oino-, one; see oi-no-): Non-. 6. Italic *nek, not, in: a. Latin prefix neg-, not: NEGLECT, (NEGLIGEE), NEGOTIATE; b. Latin negdre, to deny: NEGATE; ABNEGATE, DENY, RENEGADE, (RENEGE). 7. Greek né-, not: NEPENTHE. 8. Zero-grade combining form *n- in: a. Germanic *un- in Old English wn-, not: uN-!; b,. Latin in-, not: IN-1; c. Greek a-, an-, not: A-}, (AN-); d. Sanskrit a-, an-, not: AHIMSA, AMRITA. [Pok. ne 756.] nebh-. Cloud. 1. Suffixed form *nebh-lo- in Germanic *nibla- probably in Old Norse nifl-, “mist” or “dark”: NIFLHEIM. 2. Suffixed form *nebh-eld- in: a. Latin nebula, cloud: NEBULA, NEBULOUS; b. Greek nephelé, cloud: NEPHELINE; NEPHELOMETER. 3. Suffixed form *nebh-es- in Greek nephos, cloud: NEPHOLOGY. 4. Nasal- ized form *ne-m-bh- in Latin nimbus, rain, cloud, aura: NIMBUS. See ombhro-. [Pok. (enebh-) 315.] ned-. To bind, tie. 1. O-grade form *nod- in: a. Germanic *nati- in Old English ne¢(t), a net: NET!; b. Germanic *nat-ilo, a nettle (nettles or plants of closely related genera such as hemp were used as a source of fiber), in Old English netel(e), netle, nettle: NETTLE; c. Germanic *nat-sk- in Anglo-Norman nouch, brooch: OUCH?. 2. Lengthened o-grade form *nédo- in Latin nédus, a knot: NODE, NODULE, NODUS; DENOUEMENT. 3. Re-for- mation of the root in Latin nectere (past participle nexus), to tie, bind, connect: NEXUS; (ADNEXA), ANNEX, CONNECT [Pok. 1. ned- 758.] negwh-ro-. Kidney. Greek nephros, kidney: NEPHRO-; MESONEPHROS, METANEPHROS, PERINEPHRIUM, PRO- NEPHROS. [In Pok. eng¥- 319.] negw-ro-. Adjective denoting various colors; with deriva- tives like Greek nebros, “fawn.” Latin niger, black: NEGRO, NIELLO, NIGRESCENCE, NIGRITUDE; DENIGRATE, NECROMANCY, NIGROSINE, [néhw-iz. Near. Germanic root. Old English néah, near: NEAR, NEIGHBOR, NEXT, NIGH.] nei-. To be excited, shine. 1. Suffixed form “nei-to- in Germanic *nitha-, animosity, in Old Norse nidh, scorn (> nidhingr, villain): NIDDERING. 2. Suffixed zero-grade form *ni-to- in Latin nitére, to shine: NEAT!, (NET?). 3. Possibly Persian nil, indigo: ANIL, LILAC. [Pok. 2. nei- 760.) neie-. To lead. Sanskrit nayati, he leads: NAINSOOK. [Pok. 1. nei- 760.] neig’-. To wash. Germanic *nikwiz, *nikuz in Old High German nihhus, river monster, water spirit: NIx!. [Pok. neigt- 761.] nek-', Death. 1. Latin nex (stem nec-), death: PERNI- cious. 2. Latin necdre, to kill: INTERNECINE. 3. Suffixed (causative) o-grade form *nok-eyo- in Latin nocére, to injure, harm: NOCENT, NOCUOUS, NUISANCE; INNOCENT, INNOCUOUS. 4. Suffixed o-grade form *nok-s- in Latin noxa, injury, hurt, damage: NOXIOUS; OBNOXIOUS. 5. Suffixed full-grade form *nek-ro- in Greek nekros, corpse: NECRO-, NECROSIS; NECROMANCY. 6. Greek nek- tar, the drink of the gods, “overcoming death” (*tar-, overcoming; see ter@-2): NECTAR, (NECTARINE). [Pok. nek- 762.] nek-?. To reach, attain. I. O-grade form *nok- in Ger- manic *ga-nah- (*ga-, intensive prefix; see kom), “satis- fies,” forming *gandga-, sufficient, in Old English gendg, enough: ENOUGH. II. Variant form “enk-. 1. Redupli- cated in Greek enenkein, to carry, whence onkos, a burden, mass, hence a tumor: ONCOGENESIS, ONCOLOGY. 2. Compound root *bhrenk- (see bher-'). [Pok. enek- 316.] nekw-t-. Night. O-grade form *nokv-t-. 1. Germanic *naht- in Old English niht, neaht, night: NIGHT. 2. Latin
1739:LEAGUER! legh- LEAK leg-2 LEAN! klei- LEAP klou- LEARN leis-1 LEASING leu-! LEAST leis-2 LEATHER letro- LEAVE! leip- LEAVE? §leubh- LEAVEN legWh- LECHER leigh- LECTERN leg-1 LECTION leg-1 LECTURE leg-' LEDGE legh- LEDGER legh- LEE kele-1 LEECH! feg-1 LEECH? leig-1 LEEK leug-! LEER kleu-! LEES legh- LEGACY leg-1 LEGAL leg-1 LEGATE leg-1 LEGATO leig-1 LEGEND leg-1 LEGERDEMAIN leg¥h- LEGIBLE leg-1 LEGION leg-1 LEGISLATOR leg-1, tele- LEGIST leg-1 LEGITIMATE leg-1 LEITMOTIF leit-2 LEMAN leubh- LEMMA! (s)lag¥- LEMMA? lep-t LEMURES_ lem-2 LEND leikw- LENGTH del-1 LENIENT [6-2 LENIS [6-2 LENITIVE |@-2 LENITY 16-2 LENT del-1 LENTO lento-, lep-1. LEPIDO- lep-1 LEPIDOTE lep-1 LEPRECHAUN kWrep-, legwh- -LEPSY (s)lag¥- LEPTO- lep-1 LEPTON! lep-1
1748:LIFT leup- LIGASE leig-1 LIGATE leig-1 LIGHT! = leuk- LIGHT2 legwh-
1750:LIGHTER? legwh- LIGNEOUS  leg-! LIGNI- leg-1 LIGNUM VITAE gWei- LIGULE dngha LIKE! [ik- LIKE? [ik- LIKELY lik- LILAC nei- LIMACINE  lei- LIME = lei- LIMICOLINE lei- LIMN leuk- LIMP kel-1, leb-1 LINDEN _ lento- LINE! lino- LINE? fino- LINEN fino- Linc! del-1 LING? lenk- LINGER del-1 LINGERIE lino- LINGO dnghi LINGUA dnghd LINGUIST dngha LINIMENT lei- LININ lino- LINK! kleng- LINK? Jeuk- LINKS kleng- LINNET fino- _ LINOLEIC ACID [ino- LINSEED lino- LINT Tino-
2136:PRO-2 per? PROBABLE per! PROBE pert PROBITY per! PROBLEM gWele-1 PROBOSCIS g¥6- PROCEED ked- PROCLAIM kele-2 PROcLITIC § klei- PROCLIVITY klei- PROCREATE ker-3 PROCTITIS prdkto- PROCTOLOGY prdkto- PROCTOR cura PROCTOSCOPE prdkto- PROCUMBENT keu-2 PROCURATOR cura PROCURE cura PROCYON kwon- PRODIGAL ag- PRODIGY ég- PRODROME der-1 PRODUCE deuk- PROFANE dhés- PROFESS bha-2 PROFESSOR reg-! PROFFER bher-1 PROFICIENT dhé-1 PROFILE gWhi- PROFIT dhé-1 PROFLIGATE bhiig- PROFOUND bhudh- PROFUSE gheu- PROGENITOR gene- PROGENY gene- PROGLOTTID glégh- PROGNOSIS gnd- PROGRAM gerbh- PROGRESS ghredh- PROHIBIT ghabh- PROJECT yée- PROLAN al-3 PROLAPSE leb-1 PROLATE tele- PROLEGOMENON leg-! PROLEPSIS (s)lag¥- PROLETARIAN al-3 PROLIFEROUS _al-3 PROLIFIC al-3 PROLIX wleik- PROLOCUTOR tolkw- PROLOGUE leg-1 PROLONG del-1 PROLUSION leid- PROMENADE men-2 PROMINENT men-2 PROMISCUOUS meik- PROMISE (s)meit(e)- PROMOTE meue- PROMPT em- PRONE per! PRONEPHROS _ negwh-ro- PRONOUN no-men- PRONOUNCE neu-! PROOF per! PROPAGATE pag- PROPEL pel-6 PROPEND (8)pen- PROPER pert PROPERTY per? PROPHET bha-2 PROPHYLACTIC phulax PROPINQUITY per? PROPIONIC ACID peie- PROPITIOUS pet- PROPOLIS pele-3 PROPORTION pere-2 PROPOSE apo- PROPRIOCEPTION per! PROPRIOCEPTOR per? PROPTOSIS pet- PROPYLAEUM pulé PROPYLON pulé PROROGUE reg-1 PROS- pert PROSCRIBE skribh- PROSE wer-3 PROSECUTE sekw-1 PROSELYTE leudh-1 PROSOMA teue- PROSOPOPEIA kWwel-2, per! PROSPECT spek- PROSPER spé-1 PROSTATE sta- PROSTHESIS dhé-1 PROSTITUTE sta- PROSTOMIUM ste-men-
```


## [2026-10-16T05:13:25.907Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E \"VOW|VOTE|DEVOTE|WIRE|IRIS\" AHD_watkins1985.txt | head; grep -n -o -E \".{0,30}(egwh|eg¥h|egvh)-\\. .{0,500}\" AHD_watkins1985.txt | grep -i -E \"pledge|vow|speak\" | head; grep -n -o -E \"wei-[1l!]?\\. .{0,900}\" AHD_watkins1985.txt | head -3"
}
```


### [2026-10-16T05:13:28.672Z] TOOL RESULT

```
608:Germanic *hal6n, to call, in: a. Dutch halen, to haul, pull (2? < “to call together, summon”): KEELHAUL; b. Old French haler, to haul: HALE?, HAUL. ITI. Zero-grade form *klo- (> *kal-). 1. Suffixed form *kal-yo- in Latin conct- lium, a meeting, gathering (< “a calling together”; con-, together; see kom): CONCILIATE, COUNCIL. 2. Suffixed form *kal-énd- in Latin kalendae, the calends, the first day of the month, when it was publicly announced on which days the nones and ides of that month would fall: CALENDAR, CALENDS. 3. Suffixed form *kal-e- in Greek kalein (variant klé-), to call: ECcLESIA, PARACLETE. 4. Suffixed form *kal-d- in Latin caldre, to call, call out: INTERCALATE, NOMENCLATOR. 5. Suffixed form *klp-ro- or suffixed variant form *klaa-ro- contracted to *kld-ro- in Latin clarus, bright, clear: CLEAR, GLAIR; CHIARO- SCURO, CLAIRVOYANCE, DECLARE, ECLAIR, ECLAIRISSE- MENT. IV. Possibly extended zero-grade form *kid-, becoming *klad- in suffixed form *klad-ti- in Latin classis, summons, division of citizens for military draft, hence army, fleet, also class in general: cLAss. [Pok. 6. kel- 548.] kelp-. To hold, grasp. O-grade form *kolp- in Germanic *halb- in: a. Old English hielfe, handle: HELVE; b. suf- fixed form *halb-ma- in (i) Old English helma, rudder, tiller: HELM! (ii) Middle High German helm, handle: HALBERD; C. suffixed form *half-tra- in Old English helftre, halter: HALTER}. [In Pok. 1. (s)kel- 923.] kem-1, Hornless. 1. Germanic *skamm- in Old Norse skammr, “hornless,” short: SCANT. 2. Suffixed form *kem-tydé in Germanic *hinthj6 in Old English hind, doe: HIND?, [Pok. 2. kem- 556.] kem-?. To compress. Germanic *hamjam, a compressing, hence a doubling, in Old English hem/(m), a doubling over, a hem: HEMI, [Pok. 1. kem- 555.] kem-3. To hum. Germanic *hum- in Middle English hummen, to hum: HUM. [Pok. 2. kem- 556.] keme-. To be tired, to tire. Suffixed lengthened o-grade form *kém-n proposed by some as the preform of Greek k6ma, deep sleep, which is more likely of obscure origin: coma}. [Pok. 4. kem(g)- 557.] ken-'. To be active. 1. Suffixed o-grade form *kon-o- in Greek diakonos, servant, attendant (dia-, thoroughly): DEACON. 2. Lengthened o-grade form *kdén-d- in Latin condari, to endeavor: CONATION. [Pok. 4. ken- 564.] ken-2. Hypothetical base of a number of loosely related Germanic words referring to pinching, closing the eyes, and other obscurely associated notions. 1. Old English hnappian, to doze, nap: NAP!. 2. Old English népfléd, neap tide (fléd, tide; see pleu-): NEAP TIDE. 3. Middle Dutch nipen, to bite: n1P!. 4. Old Norse hnéggr, miserly, akin to the Scandinavian source of Middle English nigard, miser: NIGGARD. 5. Middle Dutch noppe, pile: NAP?. 6. Low German nibbein, to nibble: NIBBLE. 7. Mid- dle High German notten, to nod, perhaps akin to Middle English nodden, to nod: Nop. [Pok. 2. ken- 559.] ken-3, Fresh, new, young. 1. Suffixed form *ken-t- in Latin recens, young, fresh, new (re-, again; see re-): RECENT. 2. Suffixed zero-grade form kn-yo- in Greek kainos, new, fresh (> kainotés, newness): -CENE; CAINO- TOPHOBIA, CENOGENESIS, CENOZOIC, KAINITE. [Pok. 3. ken- 563.] ken-4, Empty. Suffixed form *ken-wo- in Greek kenos (< *kenwos), empty: KENOSIS; CENOTAPH. [Pok. ken- 564.] ken-5, Hypothetical base of several roots associated with the notions “to compress,” “something compressed.” 1. Germanic root *hnekk-, “neck” (a narrow or com- pressed part), in: a. Old English hnecca, neck: NECK; b. Old Norse hnakkur, saddle, and Old Norse hnakki, back of the neck, perhaps akin to the source of KNACKER. 2. Root *knu-, nut (< “small hard object”), in: a. extend- ed form *knud- in Old English hnutu, nut: NUT; b. ex- tended form *knuk- in Latin nux, nut: NEWEL, NOUGAT, NUCELLUS, NUCLEUS. 3. Germanic root *hnukk-, sharp projection, tip, in: a. Middle Dutch nocke, tip of a bow,
823:peie-. Also pei-. To be fat, swell. 1. Extended o-grade form *poid- in Germanic *faitaz, plump, fat, in derivative Germanic verb *faitjan, to fatten, whence Germanic past participle *faitidaz, fattened, in Old English f#t/t), fat: FAT. 2. Possibly suffixed zero-grade form *pi-tu- in Latin pituita, moisture exuded from trees, gum, phlegm: PIP 5, PITUITARY, PITUITOUS. 3. Possibly suffixed zero-grade form “pi-nu- in Latin pinus, pine tree (yielding a resin): PINE!, PINEAL, PINON, PINNACE; PINA CLOTH. 4. Suffixed zero-grade form *pi-won- in Greek pidn, fat: PROPIONIC ACID. 5. Suffixed zero-grade form *pi-wer-, “fat, fertile,” in: a. *Iwer-ii, the prehistoric Celtic name for Ireland, in Old English Jras, the Irish: (ERSE), IRISH; b. * Piwer-id in Greek Pieria, a region of Macedonia: PIERIAN SPRING. [Pok. pei()- 793.]
1132:form *weg-slo- in Latin vélum, a sail, curtain, veil: VEIL, VELUM, VEXILLUM, VOILE; REVEAL. [Pok. weg- 1117.] weg-2. To be strong, be lively. 1. Suffixed o-grade form *wog-é- in Germanic *wakén in Old English *wacan, to wake up, arise, and wacian, to be awake: WAKE}. 2. Suf- fixed o-grade form *wog-no- in Germanic *waknan in Old English wecnan, wecnian, to awake: WAKEN. 3. Germanic *wakjan in Old English weccan, to be awake: WATCH. 4. Germanic *wahtwo in Old High Ger- man wahta, watch, vigil, in dialectal German beiwacht, supplementary night watch: BIvouac. 5. Germanic *waht- in: a. Old North French waitier, to watch: WAIT; b. Middle Low German wachten, to watch, guard: WAFT. 6. Suffixed (causative) o-grade form *wog-eyo- in Latin vegére, to be lively: VEGETABLE. 7. Suffixed (stative) form *weg-é- in Latin vigére, to be lively: vicor. 8. Suf- fixed form *weg-eli- in Latin vigil, watchful, awake (> vigilare, to watch, be awake): VEDETTE, VIGIL, (VIGI- LANT), VIGILANTE; REVEILLE, SURVEILLANT. 9. Suffixed form *weg-slo- in Latin véldx, fast, “lively”: VELOCITY. [Pok. weg- 1117.] wegh-. To go, transport in a vehicle. 1. Germanic *wegan in Old English wegan, to carry, balance in a scale: WEIGH}. 2. Germanic lengthened form *wég-6 in Old English wég(e), weight, unit of weight: WEE. 3. Suffixed form *wegh-ti- in Germanic *wihti- in Old English wiht, gewiht, weight: WEIGHT. 4. Germanic *wegaz, course of travel, way, in Old English weg, way: WAY; ALWAYS, (Away). 5. Suffixed form *wogh-no- in Germanic *wag- naz, vehicle, in: a. Old English we(g)n, wagon: WAIN; b. Middle Dutch wagen, wagon: WAGON. 6. Suffixed o-grade form *wogh-lo- in: a. Germanic *waglaz in Old Norse vagl, chicken roost, perch, beam: WALLEYED; b. Greek okhlos, populace, mob (< “moving mass’): OCHLOCRACY, OCHLOPHOBIA. 7. Distantly related to this root are: a. Germanic *wag-, “to move about,” in (i) possibly Middle English waggen, to wag: wac! (ii) Old High German waggo, wacko, boulder rolling on a river- bed (> German Wacke, boulder): GRAYWACKE; b. Ger- manic *wéga-, water in motion, in Old Italian vogare, to row: VOGUE; c. Germanic *wig- in (i) Old English wicga, insect (< “thing that moves quickly”): EARWIG (ii) Middle Dutch and Middle Low German wiggelen, to move back and forth, wag: WIGGLE. 8. Basic form *wegh- in Latin vehere (past participle vectus), to carry: VECTOR, VEHICLE; ADVECTION, CONVECTION, EVECTION, INVEIGH. 9. Suffixed basic form *wegh-yd in Latin via, way, road: FOY, VIA, VOYAGE; CONVEY, DEVIATE, DEVIOUS, (ENVOI), ENVOY!, OBVIOUS, PERVIOUS, PREVIOUS, (TRIVIAL), TRIV- IUM, (vIADUCT). 10. Suffixed form *wegh-s- in Latin vexdre, to agitate (< “to set in motion”): VEX. 11. Prob- ably suffixed form *wegh-so- in Latin convexus, “carried or drawn together (to a point),” convex (com-, together; see kom): CONVEX. [Pok. vegh- 1118.] weg-. Wet. 1. Germanic *wakw-6 in Old Norse vdk, a crack in ice (< “wet spot’): WAKE?. 2. Suffixed zero-grade form *ug’-sm- in: a. Latin (hjiimére, to be wet: HUMECTANT, HUMID; b. Latin (hj)iimor, fluid: HU- mor. 3. Suffixed zero-grade form *ug’-ro- in Greek hugros, wet, liquid: HYGRO-. 4. Regarded by some as an extended form of this root (with the meaning “the impregnator”), but probably a distinct Indo-European word, is *uk”s-en-, bull, ox, in Germanic *uhs6dn- in: a. Old English oxa, ox: 0x; b. Old High German ohso, ox, in German Aurochs, aurochs: AUROCHS. [Pok. uweg#- 1118.] weg”h-, Also eug’h-. To preach, speak solemnly. Suf- fixed o-grade form *wog’h-eyo- in Latin vovére, to pledge, vow: VOTARY, VOTE, (VOTIVE), VOW; DEVOTE, (DEvouT). [Pok. ewegvh- 348.] wei-'. Also weie-. To turn, twist; with derivatives refer- ring to suppleness or binding. I. Form *wei-. 1. Germanic suffixed form *wi-ra-, *wé-ra- in Old English wir, wire: WIRE. 2. Probably suffixed Germanic form *wai-ra- in
1135:Old English war, seaweed: SEAWARE. 3. Suffixed zero-grade form *wi-ria- in Latin (of Celtic origin) viriae, bracelets: FERRULE. 4. Suffixed form *wei-ti- in Ger- manic *with- willow, in Old English withig, wiry: wITHY. 5. Suffixed zero-grade form *wi-t- in Germanic withj6n- in Old English withthe, supple twig: wITHE. II. Form *weia-, zero-grade *wi- (< *wia-). 1. Suffixed form *wi-ti- in Latin vitis, vine: VISE; VITICULTURE. 2. Suffixed form *wi-td- becoming *wittd in Latin vitta, headband: viTTA. 3. Suffixed form *wi-ri- probably in Greek iris, rainbow, and Iris, rainbow goddess: (IRIDACEOUS), IRIDO-, IRIS, IRIS; (IRIDIUM), (IRISITIS). 4. Suffixed form *wi-n- per- haps in Greek is (genitive inos), sinew: EXINE, INOSITOL, INOTROPIC. [Pok. 1. wei- 1120.] wei-?. To go after something. Suffixed o-grade form in Germanic *wai-thj6-, “pursuit,” with denominative *waithanjan, to hunt, plunder, in Old French gaaignier, gaigner, to obtain: GAIN}; ROWEN. [Pok. 3. wei- 1123.] wei-%. To wither. Extended form *weis- in Germanic *wis- in suffixed form *wis-n-6n in Old English wisnian, to wither, shrivel, shrink: wizEN. [Pok. 2. wei- 1123.] wei-*. Vice, fault, guilt. 1. Suffixed zero-grade form *wi-tio- in Latin vitium, fault, vice: vICE1, vICcIoUs, VITIATE. 2. Suffixed form “wi-tu- in: a. Latin vitiligo, tetter (< “blemish”): vITILIGO; b. Latin vituperdre, to abuse (perhaps formed after Latin recuperdre, to regain; see kap-): VITUPERATE. [Pok. 1. wi- 1175.] weid-. To see. I. Full-grade form *weid-. 1. Germanic *witan, to look after, guard, ascribe to, reproach, in: a. Old English witan, to reproach: Twit; b. Old Proven- gal guida, a guide: GUIDE; c. Germanic derivative noun *witi- in Old English wite, fine, penalty: WITE!. 2. Suf- fixed form *weid-to- in Germanic *wissaz in: a. Old English wis, wise: WISE!; b. Old English wisdém, learn- ing, wisdom (-d6ém, abstract suffix; see dhé-'): WISDOM; c. Old High German wissago, seer, prophet: WISEACRE; d. Germanic *wissdén-, appearance, form, manner, in (i) Old English wise, wis, manner: WISE? (ii) Old French guise, manner: GUISE. 3. Suffixed form *weid-es- in Greek eidos, form, shape: EIDETIC, EIDOLON, IDOL, IDYLL, -OID; IDOCRASE, KALEIDOSCOPE. 4. Perhaps Greek Haidés (also Aidés), the underworld, perhaps “the invisi- ble” (> French Hadés): HADAL, Hangs. II. Zero-grade form *wid-. 1.Germanic *wit- in: a. Old English wit, witt, knowledge, intelligence: wit}; b. Old English wita (genitive plural witena), wise man, councilor: WITENAGE- MOT. 2. Germanic *witan in Old English witan, to know: WIT2; UNWITTING. 3. Suffixed form *wid-to- in Germanic *wissaz, known, in Old English gewis, gewiss, certain, sure: IWIS. 4. Form *wid-é- (with participial form *weid-to-) in Latin vidére (past participle visus), to see, look: VIDE, VIEW, VISA, VISAGE, VISION, VISTA, VOYEUR; ADVICE, (ADVISE), BELVEDERE, CLAIRVOYANCE, ENVY, EVIDENT, INTERVIEW, PREVISE, PROVIDE, REVIEW, SU- PERVISE, SURVEY. 5. Suffixed form *wid-es-ya in Greek idea, appearance, form, idea: IDEA, IDEO-. 6. Suffixed form *wid-tor- in Greek histdr, wise, learned, learned man: HISTORY, (STORY!); POLYHISTOR. 7. Suffixed nasal- ized form *wi-n-d-no- in: a. Irish fionn, white (< “clearly visible”): COLCANNON; b. Welsh gwyn, gwynn, white: PENGUIN. 8. Celtic compound *dru-wid-, ““knower of trees” (*dru-, tree; see deru-). III. Suffixed o-grade form *woid-o- in Sanskrit vedah, knowledge: VEDA; RicG- VepaA. [Pok. 2. ufe)di- 1125.] weidh-. To divide, separate. 1. Suffixed zero-grade form *widh-ewo-, “bereft,” feminine *widh-ewd-, “woman separated (from her husband by death),” in Germanic *widuw6 in Old English widuwe, widow: wiDow. 2. Zero-grade form *widh- in Latin dividere, to separate (dis-, intensive prefix): DEVISE, DIVIDE, POINT-DEVICE. [Pok. weidh- 1127.] weie-. Vital force. Perhaps related to wi-ro-. Zero-grade form *wi- (< *wia-) in Latin vis, force, with irregular
1140:for strong-smelling animals. 1. Germanic *wisulén- in Old English wesle, weosule, weasel: WEASEL. 2. Suffixed form *wis-onto- in Germanic *wisand-, *wisunt-, Euro- pean bison (which emits a musky smell in the rutting season), in: a. Old High German wisunt, bison: WISENT; b. Latin bisdn (plural bisontés), bison: BISON. [Pok. 3. ueis- 1134.] weit(a)-. To speak, adjudge. Extended o-grade form *woito- in Russian véti, council (see sem-'). wekti-. Thing, creature. Germanic *wihti- in Old English wiht, person, thing: WIGHT!; (AUGHT?), NAUGHT, NOT. [Pok. wek-ti- 1136.] = wekv-. To speak. 1. O-grade form *wokv- in: a. Latin vox (stem vdc-), voice: VOCAL, VOICE, VOWEL; EQUIVOCAL, UNIVOCAL; b. Greek ops, voice: CALLIOPE. 2. Suffixed o-grade form *wok-d- in Latin vocdre, to call: VOCABLE, VOCATION, VOUCH; ADVOCATE, AVOCATION, CONVOKE, EQUIVOCAL, EVOKE, INVOKE, PROVOKE, REVOKE. 3. Suf- fixed form *wek-es- in Greek epos, song, word: EPIC, EPOS. [Pok. uekz- 1135.] wel-'. To see. 1. Suffixed zero-grade form *wl-id- in Germanic *wlituz, appearance, in Old Norse litr, appear- ance, color, dye, akin to the source of Litmus. 2. Suffixed form *wel-uno- perhaps in Sanskrit Varunah, “seer, wise one,” sovereign god: VARUNA. [Pok. 1. wel- 1136.] wel-2, To wish, will. 1. Germanic *wel- in Old English wel, well (< “according to one’s wish”): WELL?. 2. Germanic *welon- in Old English wela, weola, well-being, riches: WEAL!, WEALTH. 3. Germanic *wiljén- in Old English willa, desire, will power: WILL. 4. Germanic *wil(Ijan in Old English wyllan, willan, to desire: WILL?; NILL. 5. Ger- manic compound *wil-kumon- (see g¥a-). 6. O-grade form *wol- in Germanic *wal- in Old French galloper and Old North French waloper, to gallop: GALLOP, WALLOP. 7. Basic form *wel- in Latin velle (present stem vol-), to wish, will: VELLEITY, VOLITION, VOLUNTARY; BENEVO- LENT, MALEVOLENT. 8. Suffixed form *wel-up- in Latin voluptds, pleasure: VOLUPTUARY, VOLUPTUOUS. [Pok. 2. uel- 1137.] wel-3, To turn, roll; with derivatives referring to curved, enclosing objects. 1. Germanic *walt- in: a. Old High German wailzan, to roll, waltz: wALTz; b. Middle Dutch welteren, to roll: WELTER. 2. Germanic *weluka- in Old English weoluc, weoloc, mollusk (having a spiral shell), whelk: WHELK!. 3. Perhaps Germanic *wel- in Old Eng- lish welig, willow (with flexible twigs): wILLOw. 4. Per- haps Germanic *welk- in Old English wealcan, to roll, toss, and wealcian, to muffle up: WALK. 5. O-grade form *wol- in Germanic *wall- in: a. Old English wiella, wella, a well (< “rolling or bubbling water,” “spring”): WELL; b. Old High German waillén, to roam: GABERDINE. 6. Perhaps suffixed o-grade form *wol-d- in Germanic *walé in: a. Old English walu, streak on the skin, weal, welt: WALE; b. Old High German *-walu, a roll, round stem, in *wurzwalu, rootstock (see wrad-). 7. Extended form *welw- in: a. Germanic *walw6n in Old English wealwian, to roll (in mud): WALLOW; b. Latin volvere, to roll: VAULT!, VAULT2, (VOLT2), VOLUBLE, VOLUME, VO- LUTE, VOLUTIN, VOLVOX, VOUSSOIR; CIRCUMVOLVE, CON- VOLVE, DEVOLVE, EVOLVE, INVOLVE, OBVOLUTE, REVOLVE; C. suffixed o-grade form *wolw-d- in Latin vulva, volva, covering, womb: VOLVA, VULVA; d. suffixed zero-grade form *wlw-d- in Latin valva, leaf of a door (< “that which turns”): VALVE; e. suffixed form *welu-tro- in Greek elutron, sheath, cover: ELYTRON. 8. Suffixed form *wel-n- in Greek eilein (< *welnein), to turn: ILEUS; NEURILEMMA. 9. Perhaps variant *wall- in Latin vallés, vallis, valley (< “that which is surrounded by hills”): VAIL!, VALE!, VALLEY. 10. Suffixed form *wel-end, possi- bly identical with the Greek name Helené (earliest form Welend), Helen, in Greek helenion, elecampane: ELECAM- PANE, INULIN. 11. Suffixed form *wel-ik- in Greek helix, spiral object: HELIX. 12. Suffixed form *wel-mi-nth- in Greek helmis, helmins (stem helminth-), parasitic worm:
1424:DEVANAGARI deiw- DEVASTATE eu-2 DEVEST wes-4 DEvi deiw- DEVIATE wegh- DEVIL gWele-! DEVIOUS wegh- DEVISE weidh- DEVOID eu-2 DEVOIR ghabh- DEVOLVE wel-3 DEVOTE weg¥h- DEVOUR gWera-4 DEVOUT weg*h- DEW dheu-2 DEXTER deks- DEXTERITY deks- DEXTRO- deks- DEXTRORSE_ wer-3 DHARMA dher-2 DI-!_ dwo- DIABASE gWa- DIABETES gWa- DIABOLIC gWela-1 DIACRITICAL krel- DIADEM dé- DIAGNOSIS gnd- DIAGONAL genu-! DIAGRAM gerbh- DIAL deiw- DIALECT leg-1 DIALOGUE leg-1 DIALYsIs_leu-1 DIAMETER mé-2 DIAMOND deme-2 Diana deiw- DIANTHUS andh- DIAPASON pant- DIAPAUSE paus- DIAPEDESIS ped-1 DIAPHANOUS bha-1 DIAPHORESIS bher-1 DIAPHRAGM bhrekw- DIAPHYsIS bheue- DIARRHEA sreu- DIARTHROSIS ar- DIARY deiw- Diaspora sper-4 DIASTASIS sta- DIASTOLE stel- DIASTROPHISM_streb(h)- DIATESSARON kWetwer- DIATHESIS dhé-1 DIATOM tem- DIATRIBE tere-1 DIAZO = gWei- DICAST deik- DICENTRA kent- DICHASIUM dwo- DICHO- dwo- DICHOTOMY tem- DICKER dekm DICLINOUS  klei- DICROTISM kret-2 DICTATE deik- DICTION deik- DICTUM deik- DIDACTIC dens-! DIDAPPER dub- DIDYMIUM dwo- DIDYMOUS dwo- DIE! dheu-3 DIE? dé-
1441:EsLis gWela-1 EBULLIENCE beu-! ECBOLIC gWele-1 ECCENTRIC kent- ECCHYMOSIS gheu- ECCLESIA kela-2 ECCRINE krei- ECEsIsS weik-1 ECHARD segh- ECHELON skand- ECHIDNA ang¥hi- ECHINO- ang¥hi- ECHINUS angVhi- ECHO (s)wagh- ECHOLALIA 1a- ECLAIR kelo-2 ECLAIRISSEMENT kelo-2 ECLAMPSIA [ap- ECLECTIC leg-! ECLIPSE leikw- ECLOSION kleu-3 ECOLOGY weik-1 ECONOMY weik-1 ECRU kreue-1 ECSTASY sta- ECTO- eghs ECTOSARC twerk- ECU skei- ECUMENICAL welk-1 ECZEMA yes- EDACIOUS ed- EDAPHIC sed-! EDDY eti EDELWEISS _athal-, kweit- EDEMA oid- EDENTATE dent- EDGE ak-
1690:IRISH peie- IRISITIS _ wei-1 IRON eis-1 IRONY wer-6 IRREMEABLE mei-1 IRRIGATE reg-2 IRRUPT reup-
2457:VOILE weg-! VOIR DIRE wéro- VOLANT gWel-2 VOLATILE gWel-2 VOLE! welt- VOLE? gWel-2 VOLITANT gWel-2 VOLITION wel-2 VOLKSLIED léu-2 VOLLEY gWel-2 VOLT? wel-3 VOLUBLE wel-3 VOLUME wel-3 VOLUNTARY wel-2 VOLUPTUARY wel-2 VOLUPTUOUS wel-2 VOLUTE wel-3 VOLUTIN wel-3 VOLVA wel-3 VOLVOx wel-3 VOMER wogWh-ni- VOMIT weme- VORACIOUS gWere-4 VORLACE legh-, per! -VOROUS gWere-4 VORTEX wer-3 VOTARY wegh- VOTE wegWh-
2458:VOTE
412:wei-. To fear. 1. Suffixed form *dwei-ro- in Latin dirus, fearful, horrible (originally a dialectal form): DIRE. 2. Suffixed form *dwey-eno- in Greek deinos, fearful, monstrous: DINOSAUR, DINOTHERE. (This root originally meant “to be in doubt, be of two minds,” and is related to dwo-.) [Pok. dyei- 227.]
650:wei-. To hiss, whistle. Imitative root. Germanic *hwi-n- and *hwis- in: a. Old English hwinan, to whine: WHINE; b. Old English Awisprian, to whisper: WHISPER; Cc. Old English hAwistlian, to whistle: WHISTLE. [Pok. 2. kuei- 628.] kvei-'. To pay, atone, compensate. Suffixed o-grade form *koi-néd in Greek poiné, fine, penalty, borrowed into Latin as poena, penalty: PAIN, PENAL, (PENALTY), PINE?, PUNISH; IMPUNITY, PENOLOGY, (PUNITORY), (REPINE), SUBPOENA. [Pok. k#ei-t- 636.] kwei-2. To pile up, build, make. O-grade form *koi- in: a. Sanskrit kayah, body: CHEETAH; b. suffixed form *koi-wo-, making, in denominative verb *k“oiw-eyo- in Greek poiein, to make, create: POEM, POESY, POET, POETIC, -POIESIS, -POIETIC; MYTHOPOEIC, ONOMATO- POEIA, PHARMACOPOEIA, PROSOPOPEIA. [Pok. 2. kyei- 637.] kweia-'. To value, honor. Suffixed zero-grade form *kvi-ma (< *kvia-md) in Greek timé, honor, worth: TImocrAcy. [I
1096:wei-. To agitate, shake, toss. 1. Extended form *tweid- in Germanic *thwit- in: a. Old English thwitan, to strike, whittle down: WHITTLE; b. Middle Dutch duit, a small coin (? < “piece cut or tossed off”): DorT. 2. Extended form *tweis- in Greek seiein, to shake: SEISM, SISTRUM. [Pok. 2. tuei- 1099.] twengh-. To press in on. Germanic *thwang- in: a. Old English thwong, thwang, thong, band (< “constraint”): THONG; b. by-form *twangjan in Old English twengan, to pinch: TWINGE. [Pok. twengh- 1099.] twer-', To turn, whirl. Zero-grade *tur-. I. Variant form *stur-. 1. Suffixed form *stur-mo- in Germanic *sturmaz, storm (< “whirlwind”), in Old English storm, storm: STORM. 2. Germanic *sturjan in Old English styrian, to move, agitate: STIR!. II. Suffixed form *tur-bd in Greek turbé, tumult, disorder (> Latin turba, disorder, turbé, spinning top, and turbdre, to confuse, disorder): (TROU-
```


## [2026-10-16T05:13:35.349Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E \"vovē|vove|aojaiti|aog-\" POK_full.txt | head -20; echo; grep -n -E \"vaēti|vaēiti|wiry|Weide\" POK_full.txt | head -20; head -c 1500 POK_full.txt"
}
```


### [2026-10-16T05:13:35.676Z] TOOL RESULT

```
13606:Note: after Kretschmer (Gl. 30, 138) to b^eug(h)-2 {fKvesian baog-\n the intransitive 
13640:Material: Avestan baog-, bunja- "loosen, escape, they escape before' {bunja/nt/" re\ease, 
29044:Latin voved, -ere, vovT, votum (this at first from *vdve-vai, -turn) " to vow, promise 
29051:eug^h-: Avestan aog- {aojaite, aoxta, aogada) " announce, declare, say, speak, esp. in 
91325:{va/varas, vaivarys) "male of polecat or marten', vaivere, vovere^ squirrel '; Latvian vavere, 

24588:russ. -Church Slavic iva, Serbo-Croatian Tva{= Latvian leva), russ. /Va'Weide', Old 
46263:Lithuanian kirnai. " Strauchband aus Weiden ', k/rn/s' swamp, marsh'. Old Prussian k/rno 
46527:weave ', Czech krutfna'6s.; convolution: cradle ', poln. skrgtka' Weidenseil '; 
65735:German fel(a)wa. Modern High German F(9/fc'e/''Weidenbaum' (as 'Sumpfbaum'), and 
68787:piemud), noi|jr|v 'herd', noipaivw 'treibe auf die Weide, hijte; ziehe auf; -nG)\xa {po-mn) 
75884:Norwegian hork{0\6 Icelandic *hgrkt) " Weidenband ', dial, also " wrinkled woman', 
89472:diminutive to Old Saxon *wTga, westfal. tv/aja'Weidenbaum', ablaut. Old Frisian Old 
89487:English ty//re/'"Weidengerte'; Middle Low German wTkm., wTkei. "Entweichen, escape'. 
89677:"Rohrstab, duct, tube, pipe', Avestan vaeiti^ willow, Weidengerte'; participle Old Indie vTta- 
89680:gr. irsa " willow '; oiaur), oiauov 'eine Weidenart' (*Foituo-, -ua), olaoc; m. 'Dotterweide', 
89701:y^r'gedrehtes band, strap', v/d/a6s. = Old English n/zid'de 'Weidenband', Old High German 
89708:Lithuanian Inf. vyti, vytis {Akk. vytj) 'Weidengerte', ablaut. zil-vUis 'Grauweide'; Latvian 
89709:i//7e" tendril ', vftuols^ willow ', Old Prussian n/y/n/a/? "Weide', apewitwo'\}\ev^e\6€ (: Ttu-(;); 
89809:"food, Weide, hunt (Waidwerk), Fischerei', also "Fahrt, journey'. Middle High German 
91527:*vrbba^ willow ', russ. i/eAi&a "Weidenzweig' (with the accentuation of Akk. Sg.; russ. dial. 
91854:ere 'laugh'; Old English wrgestan^iuru, bend', Norwegian dial. (i^re/s/'Weidenring; 
List of language abbreviations in tlie lED 



Abbreviation Language name 


Aeq. 




Aequian 


Akk. 




Akkadian 


Alan. 




Alanian (=Old Ossetic) 


Alb. 




Albanian 


Anat. 




Anatolian 


Ang. 




Anglian 


AngN 




Anglo-Norman 


Aram.- 


■Iran 


Aramaeo-lranian 


Ash. 




Ashkun 


Ass. 




Assyrian 


Auk. 




Aukshtaitian 


Bactr. 




Bactrian 


Bel. 




Belorussian 


Br. 




British 


Bret. 




Breton 


BVan. 




Bas-Vannetais 


CCI. 




Continental Celtic 


Chak. 




Chakavian 


Chor. 




Chorasmian 


Clb. 




Celtiberian 


Class. 


Skt. 


Classical Sanskrit 


Co. 




Cornish 


Corn. 




Cornouillais 


Dae. 




Dacian 


Dan. 




Danish 


Dard. 




Dardic 


Dzuk. 




Dzukian 


EBI. 




East Baltic 


EGm. 




East Germanic 


EGmRun. 


East-Germanic Runic 


El. 




Elymian 


Elam. 




Elamite 


Elam.- 


Iran. 


Elamo-lranian 



EMoBret. 


Early Modern Breton 


EMolr. 


Early Modern Irish 


EMoW 


Early Modern Welsh 


ESI. 


East Slavic 


Faer. 


Faeroese 


FriRun. 


Frisian Runic 


Gal. 


Galindian 


Gallo-Gk. 


Gallo-Gk. (in Gk. authors) 


Gallo-Lat. 


Gallo-Latin (in Lat. authors) 


Gaul. 


Gaulish 


GaulG 


Gaulish in Greek letters 


GaulL 


Gaulish in Lat. letters 


Go. 


Gothic 


Gr. 


Greek 


Hebr. 


Hebrew 


Hell. 


Hellenistic 


Hi. 


Hindi 


HVan. 


Haut-Vannetais 


IE 


Indo-European 


Mr. 


Indo-lranian 


InsCI. 


Insular Celtic 


Iran. 


Iranian
```


## [2026-10-16T05:13:38.078Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 29030,29065p POK_full.txt; echo ======; sed -n 89640,89720p POK_full.txt"
}
```


### [2026-10-16T05:13:38.394Z] TOOL RESULT

```
Exit code 1
Root / lemma: eueg^h-i* huehueg^h-) 

Meaning: to praise, worship 

Material: ueg^h-. Old Indie ved. {*gvaghat) vaghat-^ the vowing, worshiper, organizer of a 

sacrifice ', Avestan rastare-vaysnti- EN; 

Armenian gog "say!', gogces " you can say '; 

The origin of labialized Old laryngeals: 

common Armenian Celtic * hue- > gw- > g-, u-; Old Indie gw- > v-, Latin gw- > v-, u-. 

Latin voved, -ere, vovT, votum (this at first from *vdve-vai, -turn) " to vow, promise 
solemnly, engage religiously, pledge, devote, dedicate, consecrate ', Umbrian vufetes (= 
Latin votTs) " a promise to a god, solemn pledge, religious engagement, vow, to dedicate, 
devote, offer as sacred, consecrate ', vufru^ of a vow, promised by a vow, given under a 
vow, votive ', Vufiune, Uofione^ a promise to a god, solemn pledge, religious engagement, 
vow '. 

eug^h-: Avestan aog- {aojaite, aoxta, aogada) " announce, declare, say, speak, esp. in 
ceremonious way ', wherefore Old Indie Shate^ praises, vaunts, boasts '; 



and presumably Armenian uzem'\ wish, lil<e ', y-uzem'\ searcli, seek'; 

The origin of labialized Old laryngeals: 

common Armenian Celtic *hue- > gw- > u-. 

gr. Euxojjai " I promised, prayed, wished, praised ', athemat. Impf. sukto (= gath.- 
Avestan aogada, j.-av. aoxta^ spoke, talked, conversed ') to a present *eugh-tai 
(Schwyzer Gr. Gr. I 679); suxoq n, " thing prayed for, object of prayer, boast, vaunt, vow, 
votive offering ', suxn " profession, declaration, prayer, request, imploration'; in addition 
(eval):1: ===== not found
```


## [2026-10-16T05:13:40.342Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 29065,29085p POK_full.txt; echo ======; sed -n 89650,89715p POK_full.txt"
}
```


### [2026-10-16T05:13:40.638Z] TOOL RESULT

```
Exit code 1
votive offering ', suxn " profession, declaration, prayer, request, imploration'; in addition 
perhaps also auxsw 'boast, brag, vaunt, boast', abstracted from K£V£-auxn<; " the empty 
boasting ' (*K£V£-£uxn<;, Bechtel Lexilogus 192). 

References: WP. I 110. 
Page(s): 348 

Root / lemma: e 1, 6 

Meaning: a kind of adverbial/ nominal particle 

Note: out of Aryan and partially also already in this in the meaning coloring, in Germanic 
as sense ' under, after, behind, back, again, away ' extended cognitional with Pron.-stem 
e-, 0-, either as its originator or, what is obvious esp. for the long vowels e, 6, therefrom as 
an Instrumental formation. 

Material: Old Indie a, Avestan Old pers. 5" in, to there ', e.g. a-gam-^ near to, draw near, 
get near, come close ', as postposition with Akk. "to - toward ', with Lok. "on, in, to - toward 
', with Abl. "from - away '; with Old Indie a-da^ receive (in) ', a-da- " receiving; getting in 
possession ' compare Old Indie dayada- rr\. " hereditary receiver' (o'sya- "inheritance'), gr. 
Xnpwairiq " wer ledig gewordenen Besitz (to XHPOv) zu eigener Nutzung oder zur 
(eval):1: ===== not found
```


## [2026-10-16T05:13:43.099Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 89640,89715p POK_full.txt"
}
```


### [2026-10-16T05:13:43.451Z] TOOL RESULT

```
E. With /^formant: 

Gr. !(;, \yoc, "sinew' (*Fi-v-: Czech K/>7e/r"band, strap, headband ' or *Fia-v- zur root form 
ueis-2)\ Old Church Slavic i/e/7i.C6 "Kranz'; probably Old English wine-wincia {bes\6es 
pTne-wincle) "Uferschnecke', w/>7/>7^ "bandage'; about gr. \c, compare Schwyzer Gr. Gr. 1, 
5702; 

barely here the name of Weins: gr. oTvoc; (myk. vo-no-) "wine ', oivr) " grapevine ', o\ydc„ 
-aboc, ' grapevine, vine, wine ', Armenian g/n/^mne ', ( *uoi-nJom), alb. vene, Tosc vere 
"wine ' {*uoina), Latin vTnum, latter is not bare die wellspring from Old Irish ffn, cymr. gwin 
and from Gothic wein. Old High German Old Saxon Old English Old Church Slavic vTn 
(from which again Old Church Slavic v/no and from dem Slavic Lithuanian vynas), but 
probably also die from Faliscan Volscan uinu, Umbrian vinu, uinu, da the Pontus the 



originator of tlie Weinkultur war, liandelt es sich wobi urn ein vorderasiat. word; compare 
Proto Semitic *wa/nu {arab. athiop. wa/n, hebr.jaj/n, assyr. Ihu) and Hittite wi-ja-na-a-, 
Hieroglyphic-Hittite wa(i)ana-, Luvian dial, win-, s. lastly Laroche BSL 51, XXXIII, A. 
Kammenhuber Munch, stem f. Spr. 6, 53 f. 

F. With /--formant: 

Gr. Tpic; ' rainbow ' (FTpi(;) = 'IpK; and ETpi(; (eFTpK;) "the as Gotterbotin personified 
rainbow '; Old English nw-'Metalldraht, gewundener jewellery'. Middle Low German wTre 
"Metalldrahf, Late Old Icelandic i//?a-K//'/r/ "work from Metaldraht'; besides Germanic wTra-, 
das because of gr. FTpi(; probably auf Indo Germanic *uT-ro qoes back, stands Germanic 
Ve/Aa-from *uei-ro- in Old High German mara'go\6- or Silberdraht'; Old Irish f/ar^s\ant, 
skew', cymr. gwyr\ecur\/us, limus', {*ueiro-), bret. goar, gwar^ courbe"; Latin viriae^a kind 
of Armschmuck' is Celtic loanword; 

Lithuanian /-i/a//Y/5"tortuosus, mannigfaltig, verschiedenartig'. 

G. With dormant: 

Old Indie veta-, vetasa-m. 'rankendes Wassergewachs, reed, horsewhip', vetra-m. 
"Rohrstab, duct, tube, pipe', Avestan vaeiti^ willow, Weidengerte'; participle Old Indie vTta- 
(see above); 

gr. irsa " willow '; oiaur), oiauov 'eine Weidenart' (*Foituo-, -ua), olaoc; m. 'Dotterweide', 
olaov 'rope'; itu(;, -\joc„ Aeolic Firuq f. " rim of the wheel, Schildrand, willow ' (= Latin vitus); 

Latin k/?///s" twiddled, twisted, rotated, revved, revolved ', i//7/5"vine' (= Lithuanian vytis); 
vTtex, -/ic/s'Keuschlamm, (ein tree)', vitusi. " rim of the wheel ' (gr. loanword??), vitta 
'bandage' (from *vTta, dem Fem. of participle *uTtos, through consonant increase); 

Maybe alb. vetuir eyebrow '. 

Old Irish feithi. 'fibra' {*veiti-), cymr. gwdenirom * gwyden {* ueitina) 'vinculum, ligamen, 
virga contorta'; Middle Irish fe/th/enn 'Epbeu' (?); but cymr. gwyth'i'en, corn, gwyth, abret. 
gu/thennou \e\n{n)' are loanword from Latin v/tta; 

Old Icelandic v/d/r' willow ', Old English wTdig^ willow ' (see above Latin vTtexeic), 
Middle Low German wTde, Old High German wTda^ willow ' (in addition ograde as gr. 
oiaua : Norwegian dial, veid^ willow, Wicken'), Old English n/ede/'bandage'; Modern High 
German Eingeweide, Middle High German (In)geweide: 0\6 High German wic^i) 'rope from 



gedrehten Reisern', kuna-w/th ' r(\anac\e' , Gothic kuna-w/da ' vnanac\e' , Old Icelandic v/'d, - 
y^r'gedrehtes band, strap', v/d/a6s. = Old English n/zid'de 'Weidenband', Old High German 
m'tta' bandage', Old English w/do-, w/de-w/nde ' conyoWu\us' , Middle Low German wede- 
w/nde'6s., ivy, Geiftblatt', Old English w/du-w/nde ^Ge\Q>b\att', Old Icelandic vid-vindill 6s:, 
also (compare Gothic inwinds^ inverted ', //7M///7£y/^a'Ungerechtigkeit' to windan) Old 
Saxon //7by/b'" malice, TiJcke', Old English inwidd' wicked, heimtiJckisch', Old Icelandic 
Tvidgjarn " wicked '; 

Lithuanian Inf. vyti, vytis {Akk. vytj) 'Weidengerte', ablaut. zil-vUis 'Grauweide'; Latvian 
i//7e" tendril ', vftuols^ willow ', Old Prussian n/y/n/a/? "Weide', apewitwo'\}\ev^e\6€ (: Ttu-(;); 
ablaut. Old Church Slavic vetvb "twig, branch'; 

Old Church Slavic Inf. vit'r, vitb (= Lithuanian vytis) 'res torta in modum funis', pavitb ' 
tendril ', sb-i///b/rb '(book)rolle', russ. i///i///7a"twig, branch, rod, horsewhip', sloven, vitika 
"ring'.
```


## [2026-10-16T05:13:47.182Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'NR>=89400 && NR<=89900 && /Page\\(s\\)|Root \\/ lemma|npers|Persian|bed/' POK_full.txt | head -30"
}
```


### [2026-10-16T05:13:47.484Z] TOOL RESULT

```
Page(s): 1128-1129 
Root / lemma: ueik-3 
Page(s):1129 
Root / lemma: ueik-4, ueig- 
"Anprall, blow, knock, prank', nivixta- "herabgeschwungen, herabgeschleudert', npers. 
Page(s): 1130-1131 
Root / lemma: ueiR-, uiR-, uoiRo-{* duei- ksayatlj 
Page(s):1131 
Root / lemma: uei-1, ueia- : uT- 
Page(s): 1120-1122 
Root / lemma: uei-2, ueie- : u7- 
Page(s):1123 
Root / lemma: uei-3, ueia- : uT- 
Page(s): 1123-1124 
Root / lemma: ueip- ueib-
```


## [2026-10-16T05:13:59.955Z] TOOL CALL #14: ToolSearch

```json
{
 "query": "select:WebFetch",
 "max_results": 1
}
```


### [2026-10-16T05:13:59.969Z] TOOL RESULT

```

```


## [2026-10-16T05:14:03.305Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 tools/fetch_source.py --help 2>&1 | head -20"
}
```


### [2026-10-16T05:14:03.968Z] TOOL RESULT

```
Save a web source used during verification, for later cross-checking.

    python3 tools/fetch_source.py <URL> [--note "why it was fetched"]

Downloads the URL, converts the HTML to plain text, stores it as
data/verification/sources/web/<sha1(url)>.txt and appends a line to
data/verification/sources/web/index.jsonl  ({url, file, fetched, bytes, status, title, note}).
Prints the stored path. Re-fetching the same URL within a day is skipped.
```


## [2026-10-16T05:14:08.997Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; for u in 'https://en.wiktionary.org/wiki/%D9%BE%D8%A7%D8%B3%D8%AE' 'https://en.wiktionary.org/wiki/%D8%A8%DB%8C%D8%AF' 'https://en.wiktionary.org/wiki/%D8%A8%DB%8C%D8%B4%D9%87' 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%81weg%CA%B7%CA%B0-' 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/wyeh%E2%82%81-' 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/weh%E2%82%81y-' 'https://www.etymonline.com/word/vow' 'https://www.etymonline.com/word/vote' 'https://www.etymonline.com/word/devote' 'https://www.etymonline.com/word/wire' 'https://www.etymonline.com/word/iris' 'https://en.wiktionary.org/wiki/vove%C5%8D'; do python3 tools/fetch_source.py \"$u\" --note \"page 532: Wegwh/Wei 1 verification\"; done"
}
```


### [2026-10-16T05:14:13.880Z] TOOL RESULT

```
Exit code 1
/home/sfmqrb/git/rishe-private/data/verification/sources/web/010682aa738991b5.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/9dd552061f6d124c.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/94e2efba69ba7aef.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/d7be8c2555333bee.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/7760434ea991797e.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/ff1829269965680b.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/1a8388802c5f38c2.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/b79aacf482aeae9a.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/5e6ce69faa33aef7.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/1e44db52451f0585.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/66dd2a9203c6b4e8.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/68f489bba362f115.txt
```


## [2026-10-16T05:14:16.209Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; for f in 010682aa738991b5 9dd552061f6d124c 94e2efba69ba7aef; do echo \"## $f\"; wc -c $f.txt; grep -n -A12 -E \"^Etymology\" $f.txt | head -45; done"
}
```


### [2026-10-16T05:14:16.711Z] TOOL RESULT

```
## 010682aa738991b5
4513 010682aa738991b5.txt
## 9dd552061f6d124c
9833 9dd552061f6d124c.txt
## 94e2efba69ba7aef
4601 94e2efba69ba7aef.txt
```


## [2026-10-16T05:14:19.424Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; grep -v '^\\s*$' 010682aa738991b5.txt | sed -n 1,60p | cut -c1-300; echo; grep -i -n -E \"inherited|from|ety\" 9dd552061f6d124c.txt | head -20; grep -i -n -E \"from|ety\" 94e2efba69ba7aef.txt | head"
}
```


### [2026-10-16T05:14:19.778Z] TOOL RESULT

```
URL: https://en.wiktionary.org/wiki/%D9%BE%D8%A7%D8%B3%D8%AE
FETCHED: 2026-10-16T05:14:09Z
STATUS: 200
TITLE: پاسخ - Wiktionary, the free dictionary
پاسخ - Wiktionary, the free dictionary 
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
 Etymology 
 1.2 
 Pronunciation 
 1.3 
 Noun 
 1.3.1 
 Derived terms 
 1.3.2 
 Descendants 
 Toggle the table of contents 
 پاسخ 
 12 languages 
 فارسی 
 Na Vosa Vakaviti 
 Français 
 Magyar 
 Bahasa Indonesia 
 Kurdî 
 Malagasy 
 Polski 
 پښتو 
 Русский 

62: Etymology 1 
77: Etymology 2 
92: Etymology 3 
104: Etymology 4 
121: Etymology 
201: From Wiktionary, the free dictionary
210: Etymology 1
217: From Middle Persian [script needed] ( wyt /⁠wēd⁠/ ) , from Proto-Indo-Iranian *waytaháh , from Proto-Iranian *waytasás , from Proto-Indo-European *wéh₁itis .
275: Etymology 2
282: Unknown, perhaps from Proto-Indo-European *bʰeyd- ( “ to split ” ) , in reference to the harmful activities of these insects.
314: Etymology 3
317: Borrowed from Urdu بید ( bed ) / Hindi बेद ( bed ) , from Sanskrit वेद ( veda ) .
338: Etymology 4
358: Vullers, Johann August ( 1855 ), “ بید ”, in Lexicon Persico-Latinum etymologicum cum linguis maxime cognatis Sanscrita et Zendica et Pehlevica comparatum, e lexicis persice scriptis Borhâni Qâtiu, Haft Qulzum et Bahâri agam et persico-turcico Farhangi-Shuûrî confectum, adhibitis etiam Castelli, Meninski, Richardson et aliorum operibus et auctoritate scriptorum Persicorum adauctum ‎ [1] (in Latin), volume I, Gießen: J. Ricker, pages 294b–295a 
363: Etymology
366: Semi-learned borrowing from Sanskrit वैद्य ( vaidya ) .
427: Retrieved from " https://en.wiktionary.org/w/index.php?title=بید&oldid=92378991 "
429: Categories : Persian terms inherited from Middle Persian 
430: Persian terms derived from Middle Persian 
431: Persian terms inherited from Proto-Indo-Iranian 
62: Etymology 
146: From Wiktionary, the free dictionary
153: Etymology
156: From Middle Persian [script needed] ( wyšk' /⁠wēšag⁠/ ) . Cognate to Central Kurdish بیشە ( bîşe , “ forest ” ) and Northern Kurdish bîşe ( “ forest ” ) , Related to Latvian mežs ( “ forest ” ) , Proto-Slavic *meďà ( “ boundary of a field ” ) and the borrowed Proto-Finnic *meccä ( “ forest ” ) , Ottoman Turkish میشه ( meşä , “ forest ” ) , Azerbaijani meşə ( “ forest ” ) , ultimately going back to Proto-Indo-European *médʰyos ( “ middle ” , adjective ) . For the variation b ⇌ m in the onset compare Middle Persian wnpšk' ( wanafšag ) some of the descendants of which point to a byform *manafšak . This etymology is incomplete. You can help Wiktionary by elaborating on the origins of this term. .
225: Retrieved from " https://en.wiktionary.org/w/index.php?title=بیشه&oldid=90260794 "
227: Categories : Persian terms inherited from Middle Persian 
228: Persian terms derived from Middle Persian 
229: Persian terms derived from Proto-Indo-European 
237: Requests for expansion of etymologies in Persian entries 
251: Legal & safety contacts
```


## [2026-10-16T05:14:23.458Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; grep -v '^\\s*$' 010682aa738991b5.txt | sed -n 60,110p | cut -c1-400; for f in d7be8c2555333bee 7760434ea991797e ff1829269965680b 68f489bba362f115; do echo \"## $f\"; head -4 $f.txt|tail -2; grep -n -i -E \"Indo-Iranian|Avestan|Persian|Greek|Latin|wire|Etymology|meaning\" $f.txt | head -25 | cut -c1-400; done"
}
```


### [2026-10-16T05:14:23.758Z] TOOL RESULT

```
 Русский 
 Sängö 
 中文 
 Entry 
 Discussion 
 English 
 Read 
 Edit 
 View history 
 Tools 
 Tools
 move to sidebar 
 hide 
 Actions
 Read 
 Edit 
 View history 
 General
 What links here 
 Related changes 
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
 Persian
 [ edit ] 
 Etymology
 [ edit ] 
 From Middle Persian [script needed] ( pshw' /⁠passox⁠/ ) , [script needed] ( pʾshw' /⁠pāsox⁠/ ) , 𐫛𐫘𐫇𐫟 ( pswx /⁠passox⁠/ ) , from Proto-Iranian *paticahwaH , derived from Proto-Iranian *cánhati , ultimately from Proto-Indo-European *ḱens- . Cognate to Sanskrit शंसति ( śaṃsati ) , Latin cēnseō .
 Pronunciation
 [ edit ] 
 ( Classical Persian ) IPA ( key ) : /paː.ˈsux/ 
 ( Dari, formal ) IPA ( key ) : [pʰɑː.sʊx] 
 ( Dari, formal ) IPA ( key ) : [pʰɑː.sʊx] 
 ( Kabuli ) IPA ( key ) : [pʰɑː.sʊx] 
 ( Hazaragi ) IPA ( key ) : [pʰɔː.sux] 
 ( Iran, formal ) IPA ( key ) : [pʰɒː.sox] 
 ( Tajik, formal ) IPA ( key ) : [pʰɔ.suχ] 
 Rhymes: -ux 
 Readings
 Classical reading ? 
## d7be8c2555333bee
STATUS: 200
TITLE: Reconstruction:Proto-Indo-European/h₁wegʷʰ- - Wiktionary, the free dictionary
166: Mycenaean Greek: 𐀁𐀄𐀐𐀵 ( e-u-ke-to ) 
168: Ancient Greek: εὔχομαι ( eúkhomai ) → Greek: εύχομαι ( éfchomai ) ( learned ) 
170: Proto-Indo-Iranian: *HáHugdʰay ( see there for further descendants )
178: Proto-Indo-Iranian: 
181: Proto-Indo-Iranian: *Hwāgʰát 
187: Ancient Greek: εὖχος ( eûkhos ) 
189: Proto-Indo-Iranian: *HáHuǰʰas 
194: Proto-Indo-Iranian: *HáHuǰʰtas 
196: Avestan: 𐬀𐬊𐬑𐬙𐬀 ( aoxta , “ spoken, said; vowed ” ) 
199: Proto-Indo-Iranian: *HáHuǰʰyas 
201: Avestan: 𐬀𐬊𐬘𐬌𐬌𐬀 ( aojiia , “ of speaking, saying; vowing ” ) 
210: ^ De Vaan, Michiel ( 2008 ), “ voveō ”, in Etymological Dictionary of Latin and the other Italic Languages (Leiden Indo-European Etymological Dictionary Series; 7), Leiden, Boston: Brill, →ISBN , page 691 
## 7760434ea991797e
STATUS: -1
TITLE: 
## ff1829269965680b
STATUS: 200
TITLE: Reconstruction:Proto-Indo-European/weh₁y- - Wiktionary, the free dictionary
156: Proto-Indo-Iranian: *uHyáyati 
161: Latin: vieō ( “ to bind, plait, weave ” ) ( see there for further descendants )
176: Proto-Indo-Iranian: *wináHti 
198: Ancient Greek: ὑιήν ( huiḗn , “ grapevine ” ) [ 8 ] 
227: Ancient Greek: ἴτῠς ( ítŭs , “ felloe ” ) 
228: Aeolic Greek: ϝῐ́τῠς ( wĭ́tŭs ) 
231: Latin: vitus ( “ felloe ” ) 
237: Proto-Germanic: *wīraz ( “ wire ” ) ( see there for further descendants )
248: Proto-Indo-Iranian: *waHyáH 
280: ^ Jasanoff, Jay H. ( 2021 ), “Vedic dháya -, citáya - and an Indo-Iranian sound law”, in Historische Sprachforschung ‎ [2] , volume 134 , number 1, Vandendhoeck & Ruprecht, page 169 of 166-185 
282: ↑ 7.0 7.1 De Vaan, Michiel ( 2008 ), “ vieō ”, in Etymological Dictionary of Latin and the other Italic Languages (Leiden Indo-European Etymological Dictionary Series; 7), Leiden, Boston: Brill, →ISBN , page 677 : “ *u̯h₁i-éie ” 
286: ^ Beekes, Robert S. P. ( 2010 ), “ ἴτυς ”, in Etymological Dictionary of Greek (Leiden Indo-European Etymological Dictionary Series; 10 ), volume I, with the assistance of Lucien van Beek, Leiden, Boston: Brill, →ISBN , page 605 
## 68f489bba362f115
STATUS: -1
TITLE:
```


## [2026-10-16T05:14:28.645Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; sed -n 140,260p ff1829269965680b.txt | grep -v '^\\s*$' | cut -c1-200; sed -n 160,205p d7be8c2555333bee.txt | grep -v '^\\s*$'"
}
```


### [2026-10-16T05:14:28.949Z] TOOL RESULT

```
 to wrap , enclose , cover 
 Alternative reconstructions
 [ edit ] 
 *wyeh₁- [ 3 ] 
 *weyh₁- [ 4 ] [ 5 ] [ 6 ] 
 Derived terms
 [ edit ] 
 Terms derived from the Proto-Indo-European root *weh₁y- (81 c, 0 e) 
 *uh₁y-éye-ti ( “ to wrap, plait ” , eye-present ) [ 7 ] 
 Proto-Indo-Iranian: *uHyáyati 
 Proto-Indo-Aryan: *uHyáyati 
 Sanskrit: व्यय॑ति ( vyáyati ) 
 Proto-Italic: *wieō [ 7 ] 
 Latin: vieō ( “ to bind, plait, weave ” ) ( see there for further descendants )
 *wéh₁y-ti 
 Proto-Balto-Slavic: *wīˀtei ~ *weiˀtei 
 Lithuanian: vyti 
 Latvian: vīt (i)
 Latgalian: veit ʲ(i)
 Proto-Slavic: *vìti ( see there for further descendants )
 *wi-né-h₁-ti [ 3 ] ( or *uh₁i-néH-ti )
 Proto-Celtic: *winīti ( “ to bend, enclose ” ) [ 4 ] ( or *winati ) ( see there for further descendants )
 Proto-Indo-Iranian: *wináHti 
 Proto-Indo-Aryan: *wináHti 
 Pali: vināti 
 Prakrit: *𑀯𑀺𑀡𑀇 ( *viṇaï ) , *𑀯𑀼𑀡𑀇 ( *vuṇaï , “ weaves ” ) 
 Bengali: বুনা ( buna ) 
 Gujarati: વણવું ( vaṇvũ ) 
 Hindi: बुनना ( bunnā ) 
 Marathi: विणणे ( viṇṇe ) 
 Punjabi: ਬੁਨਣਾ ( bunṇā ) 
 ⇒ Prakrit: 𑀯𑀺𑀡𑀡   n ( viṇaṇa ) , 𑀯𑀼𑀡𑀡   n ( vuṇaṇa , “ weaving ” ) , 𑀯𑀼𑀡𑀺𑀬 ( vuṇiya , “ woven ” ) 
 *uh₁i-t ( zero-grade root aorist ) 
 Proto-Balto-Slavic: *wīˀtei [ 1 ] ( see there for further descendants )
 *uh₁y-ḗn ( possibly ) 
 Proto-Hellenic: *uyḗn 
 Ancient Greek: ὑιήν ( huiḗn , “ grapevine ” ) [ 8 ] 
 *uh₁i-tó-s 
 Proto-Celtic: *witos 
 Old Irish: fithe ( “ woven, plaited ” ) 
 *wéh₁i-ko-s ( “ enclosed ” ) 
 ⇒ Proto-Germanic: *waigaz ( “ wall ” ) ( substantivation ) 
 Proto-West Germanic: *waig ( see there for further descendants )
 *wéh₁i-mn̥ ~ *uh₁i-mén-s ( see there for further descendants )
 *weh₁i-s- [ 1 ] 
 Proto-Balto-Slavic: *weiˀš- 
 ⇒ Proto-Balto-Slavic: *weiˀšā́ˀtei 
 Proto-Slavic: *vixati 
 ⇒ Proto-Balto-Slavic: *weiˀšuras , *weiˀšulas ( “ whirlwind ” ) [ 1 ] ( see there for further descendants )
 *wéh₁i-ti-s ~ *uh₁i-téy-s ( see there for further descendants )
 *wéh₁i-tu-s ~ *uh₁i-téw-s [ 9 ] 
 Proto-Balto-Slavic: 
 Proto-Baltic: 
 Old Prussian: witwan [ 10 ] 
 Proto-Slavic: *větvь ( see there for further descendants )
 Proto-Hellenic: *wítus 
 Ancient Greek: ἴτῠς ( ítŭs , “ felloe ” ) 
 Aeolic Greek: ϝῐ́τῠς ( wĭ́tŭs ) 
 Proto-Italic: *witus 
 Latin: vitus ( “ felloe ” ) 
 *wéh₁y-r̥ ~ *wih₁-n-és 
 ⇒ *weh₁ir-o-s ( “ turned, twisted ” ) [ 1 ] [ 4 ] 
 Proto-Celtic: *weiros ( “ crooked ” ) [ 4 ] ( see there for further descendants )
 Proto-Germanic: *wīraz ( “ wire ” ) ( see there for further descendants )
 *wéh₁y-u-s ~ *uh₁y-éw-s 
 Proto-Germanic: *wajjuz ( “ a wall ” ) ( see there for further descendants )
 *wéyh₁-ō ~ *wih₁-n-és ( “ wine ” ) ( possibly ) ( see there for further descendants )
 *woh₁y-éh₂ ( “ branch, twig ” ) [ 1 ] 
 Proto-Balto-Slavic: *wejā́ˀ [ 1 ] 
 Proto-Slavic: *věja ( see there for further descendants )
 Proto-Indo-Iranian: *waHyáH 
 Proto-Indo-Aryan: *waHyáH 
 Sanskrit: व॒या ( vayā́ ) 
 *woyh₁-n- 
 Proto-Balto-Slavic: *waiˀn- 
 ⇒ Proto-Balto-Slavic: *waiˀníkas ( see there for further descendants )
 ⇒ Proto-Balto-Slavic: *waiˀnukas 
 Latgalian: vaiņuks 
 Latvian: vaîņuks ( dialectal ) 
 [ edit ] 
 Terms derived from the Proto-Indo-European root *h₁wegʷʰ- (26 c, 0 e) 
 *h₁é-h₁ugʰ-tor ( deponent reduplicated present ) 
 Proto-Hellenic: *eukʰomai ( thematized ) 
 Mycenaean Greek: 𐀁𐀄𐀐𐀵 ( e-u-ke-to ) 
 Ancient Greek: εὔχομαι ( eúkhomai ) → Greek: εύχομαι ( éfchomai ) ( learned ) 
 Proto-Indo-Iranian: *HáHugdʰay ( see there for further descendants )
 *h₁wogʷʰ-éye-ti ( éye-iterative ) 
 Proto-Italic: *woɣʷeō ( see there for further descendants )
 Proto-Armenian: 
 Old Armenian: գոգեմ ( gogem , “ to say ” ) 
 Proto-Indo-Iranian: 
 *h₁wogʷʰ-et- ~ *h₁wogʷʰ-n̥t- [ 5 ] 
 Proto-Indo-Iranian: *Hwāgʰát 
 Proto-Indo-Aryan: *Hwāgʰát 
 Sanskrit: वाघत् ( vāghát ) 
 *h₁é-h₁ugʰ-os [ 5 ] 
 Proto-Hellenic: *éukʰos 
 Ancient Greek: εὖχος ( eûkhos ) 
 Proto-Indo-Iranian: *HáHuǰʰas 
 Proto-Indo-Aryan: *HáHuźʰas 
 Sanskrit: ओहस् ( óhas ) 
 *h₁é-h₁ugʰ-tós 
 Proto-Indo-Iranian: *HáHuǰʰtas 
 Proto-Iranian: *Hauxtah 
 Avestan: 𐬀𐬊𐬑𐬙𐬀 ( aoxta , “ spoken, said; vowed ” ) 
 *h₁é-h₁ugʰ-yós 
 Proto-Indo-Iranian: *HáHuǰʰyas 
 Proto-Iranian: *Hauǰʰyah 
 Avestan: 𐬀𐬊𐬘𐬌𐬌𐬀 ( aojiia , “ of speaking, saying; vowing ” ) 
 Unsorted formations 
 Proto-Anatolian: 
 > ? Luwian: [script needed] ( ow- , “ to proclaim ” ) [ 6 ]
```


## [2026-10-16T05:14:34.678Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; for u in 'https://en.wiktionary.org/wiki/%E1%BC%B6%CF%81%CE%B9%CF%82' 'https://en.wiktionary.org/wiki/wire' 'https://en.wiktionary.org/wiki/vow' 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/w%C3%A9h%E2%82%81itis' 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/c%C3%A1nhati'; do python3 tools/fetch_source.py \"$u\" --note \"page 532: Wegwh/Wei 1 verification\"; done 2>&1"
}
```


### [2026-10-16T05:14:37.579Z] TOOL RESULT

```
/home/sfmqrb/git/rishe-private/data/verification/sources/web/55d97d4ec4040839.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/fbab5610f51b6e2b.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/0297d011a9fcad27.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/52d635a6c74ceb83.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/2584fc8d278b8c2e.txt
```


## [2026-10-16T05:14:41.323Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; for f in 55d97d4ec4040839 fbab5610f51b6e2b 0297d011a9fcad27 52d635a6c74ceb83 2584fc8d278b8c2e; do echo \"## $f $(sed -n 3p $f.txt)\"; grep -n -A3 -E \"^ *Etymology\" $f.txt | grep -v -E \"^\\S*-\\s*$|edit\" | head -12 | cut -c1-600; done; grep -n -E \"Avestan|Persian\" 52d635a6c74ceb83.txt 2584fc8d278b8c2e.txt | head"
}
```


### [2026-10-16T05:14:41.761Z] TOOL RESULT

```
## 55d97d4ec4040839 STATUS: 200
65: Etymology 
67- 1.3 
68- Pronunciation 
166: Etymology
169- From Proto-Hellenic *wī́ris ; further origin uncertain. The traditional etymology, from Proto-Indo-European *wih₁-r- ( “ twist; thread; cord; wire ” ) (compare English wire , Swedish vira ( “ to twist ” ) , Welsh gŵyr ( “ bent ” ) ), from *weyh₁- ( “ to turn, twist, weave, plait ” ) , is suspicious on account of the irregular variation between ⟨ ε ⟩ and ⟨ ι ⟩ , as well as the suffix -ῐς ( -ĭs ) , -ῐδος ( -ĭdos ) . Furthermore, even the derivation of ϝῖρ- ( wîr- ) seems phonetically improbable, given the modern reconstruction of the root as *weh₁-y- . Thus, Furnée and Beekes argue for Pre-
## fbab5610f51b6e2b STATUS: 200
62: Etymology 
64- 1.2 
65- Pronunciation 
126: Etymology 
128- 3.2 
129- Pronunciation 
290: Etymology
293- From Middle English wir , wyr , from Old English wīr ( “ wire, metal thread, wire-ornament ” ) , from Proto-Germanic *wīraz ( “ wire ” ) , from Proto-Indo-European *weh₁iros ( “ a twist, thread, cord, wire ” ) , from *weh₁y- ( “ to turn, twist, weave, plait ” ) .
1239: Etymology
1242- From Proto-Oceanic *waiʀ .
## 0297d011a9fcad27 STATUS: 200
62: Etymology 
64- 1.2 
65- Pronunciation 
103: Etymology 
105- 2.2 
106- Interjection 
210: Etymology
213- Inherited from Middle English vowe , voue , that from Old French vut , in turn from Latin vōtum ( “ a promise, dedication, vow ” ) , from vovēre ( “ to promise, vow ” ) . Not related to avow . Doublet of vote .
580: Etymology
583- Probably originally imitative . [ 1 ] Compare wow .
## 52d635a6c74ceb83 STATUS: 200
62: Etymology 
64- 1.2 
65- Noun 
140: Etymology
143- From *weh₁y- ( “ to twine, wind ” ) +‎ *-tis ( abstract or action suffix ) .
## 2584fc8d278b8c2e STATUS: 200
62: Etymology 
64- 1.2 
65- Verb 
140: Etymology
143- From Proto-Indo-Iranian *ćánsati , from Proto-Indo-European *ḱéns-e-ti , from *ḱens- ( “ to announce, proclaim ” ) +‎ *-eti . Cognate with Sanskrit शंसति ( śáṃsati , “ to declare ” ) , Latin cēnseō and perhaps Ancient Greek κῶμος ( kômos ) .
2584fc8d278b8c2e.txt:442: Middle Persian: 
2584fc8d278b8c2e.txt:445: Classical Persian: پاسخ ( pāsux ) Tajik: посух ( posux ) 
2584fc8d278b8c2e.txt:452: Younger Avestan: 𐬞𐬀𐬌𐬙𐬌𐬯𐬀𐬢𐬵 ( pa i tisaŋh , “ to call up, invoke ” ) 
2584fc8d278b8c2e.txt:455: Old Avestan: 𐬯𐬇𐬧𐬖𐬎 ( sə̄ṇγu ) 
2584fc8d278b8c2e.txt:461: Middle Persian: (/saxwan/ "word, speech")
2584fc8d278b8c2e.txt:464: Classical Persian: سخن ( suxan ) , سخون ( saxūn ) 
2584fc8d278b8c2e.txt:481: Old Avestan: 𐬯𐬇𐬧𐬖𐬀𐬌𐬙𐬍 ( sə̄ṇγa i tī ) 
2584fc8d278b8c2e.txt:491: Old Persian: 𐎰𐎠𐎫𐎡𐎹 ( θ-a-t-i-y /⁠θatiy⁠/ ) 
2584fc8d278b8c2e.txt:522: Middle Persian terms with redundant script codes 
2584fc8d278b8c2e.txt:523: Requests for Book Pahlavi script for Middle Persian terms
```


## [2026-10-16T05:14:49.443Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E \"^ *aog-|aogaḍa|aogəd|aojaitē|^ *3?\\.? *vaēiti|vaētay|^ *varəša|varasa-|^ *3\\. *vay-\" BRT.txt | head -20; echo ---KNT; grep -n -i -E \"pāsox|pasox|aug-|aog-|paity-?aog\" KNT_full.txt | head"
}
```


### [2026-10-16T05:14:49.884Z] TOOL RESULT

```
22991:•  j.  varasa-  ■>  m.,  n.  'Haar*  der  Menschen und  Tiere,  meist  Kopfhaar '>i  Sing,  auch kollektiv;  a)  der  Menschen:  *JiourusS {iA.) asti  "sS  V.7.57;  —  maüstna  .  ,  yaHbyS äste  nasukaia  frasnayante  °taica  tanümla V.  Ä  1 1 ;  —  'Sftn  vä  ianUm  vä  Vd.  4;  — *x''alpaiä,ya{%^)ca  -ja  V,  15.46;  F. jb; — astssca  's3saiYt.io.T2i  —  astqmca  °sqmca (GP.)  V.(),7,  2g; — yalißm..'s3sca'  *Äqm.- razayaiaha  . .  ''pairUrinattAa  "wenn  du  dir die  Haare  geordnet  ..  verschnitten  hast"^ V.  i7.  4;  2;  —  yat  Al  .  .  -jo  (NPq.)  Aiku bavax  "bis  dass  seine  Haare  trocken  wer- den" V.  i5',38;  —  avava^  ..ya%a  *sar?ma 'sanqm  barami  "soviel  als  ich  Haare  auf dem  Kopf  trage"  Ytj.  77.  b)  der Tiere:  aspalm  'am  Yt/4. 31,  i6.\o;  — ^us  vä  aspaht  vä  •sa*''  Vd,^,  S;  ^.^S, Vd.  iJ,  ^,  lO;  —  °iäi  Aaomö.anAanzäHäi (sd.)  Vr.jo.2.
---KNT
5823:pIE *aug-, *ueg- ‘increase’, Lt. auge. etc.; with 
5837:pAr. *haug- ‘free’, in Av. илат ‘they rescue’ 
5841:Baga-burSu- (see Lex.); *baug-s-na-, becoming 
11707:baug- ‘free’, seen in Av. pouru-baorsna-; in OP 
23190:misfortune’ + pass. pte. of d-baug- ‘to free’ ($248) 
26386:daug- vb., see hadugà-. 
26750:duruj- vb. ‘lie, deceive’: Av. druj- ‘le’ (draog-, 
26835:draug- vb., see duruj- and draujiya-. 
27737:. baug- vb. ‘free’: Av. baog-, NPers. boxtén; in 
27781:‘sod’ + deriv. of root baug- ‘free’ ($102, §151):
```


## [2026-10-16T05:14:54.417Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -o -E \"^.{0,10}(aog|a\\.og)-.{0,250}\" BRT.txt | head -8; echo; grep -n -o -E \"^.{0,10}va[eē]iti-.{0,300}\" BRT.txt | head -5; echo; grep -n -o -E \"^.{0,12}var[əa3]s[aä]-.{0,200}\" BRT.txt | head -10; grep -n -o -E \".{0,10}3\\. *vay-.{0,200}\" BRT.txt | head"
}
```


### [2026-10-16T05:14:56.263Z] TOOL RESULT

```
2862:37    aog-
16272:Zum  V.  baog-^).  —  Vgl.  *ä%i}'Sbaustia:  — Pü. :  /iff-  bSUsn,  erl. :  i^äslai  kt  nraiakih  vas hol  ai.  —  ')  Verbindung  von  DS.  und  GS. wie  öfters.  —  ")  Es  liegt  nahe,  vielmehr  an ai.  ikuttäkH  lu  denken  und  da.E  Adj.  'reich an  GenQs
16501:baog-
16544:baog-
20927:yaog-
21838:Zum  V.  yaog-,  —  ai.  vgl-  yuktay-  f.  —  Pü-  (lu F.):  äyBosn,  (luY.);  mä  bav/ arvandän  Sydxlär (lies  'xtan).  —  ')  Vgl.  zKonstr,  Bthl.  IF.  io, iSg  und  joii^  K.
21849:Zum  V.  yaog-  (FPfP.  mit  iha-,  %  sog.  8).  — Npfl.  r  äyüxtäi;  erl. :  ßs  raflär.  —  1)  Gdn.  3Yt. 65;  'kampfbereit',  Dst.  ZA.  2.  566:  'rapide'.


22991:•  j.  varasa-  ■>  m.,  n.  'Haar*  der  Menschen und  Tiere,  meist  Kopfhaar '>i  Sing,  auch kollektiv;  a)  der  Menschen:  *JiourusS {iA.) asti  "sS  V.7.57;  —  maüstna  .  ,  yaHbyS äste  nasukaia  frasnaya
```


## [2026-10-16T05:14:58.677Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 2855,2880p BRT.txt | cut -c1-500; grep -n -E \"va[eē]iti|vaetay|vaHtt|Weide\" BRT.txt | head; grep -n -E \"Baum\" BRT.txt | grep -i \"var\" | head"
}
```


### [2026-10-16T05:14:59.234Z] TOOL RESULT

```
\'.-2'i.i;4\7:  —  r.lisg.tmi.ini.':iiai.xS.j  >  -  ^i-—  -    -    ■  -  '.-  <-=j-  "v=  -.;
(sd.i  v-».;/ rf:.'j  Y.4J.Jo;~i,7  ö'a/.vrj-  •  j-  aoi.buta  Inf. 'hinrjgelangen  rurn^Z ^;.M  v«.-!«  rar^n  .sd.t  rJm^m'i  \.4;.  '^-^  Ziel  zu  erreichen:  ^>--tf  .-v.- 4.  A>  als  />J<^a*':  -liar.?«  ..  »v  ■nämL  /j-j/«;.'  -ob  die  Sprüche  ■ Jr^.-Jt^ti  'fm^m  r-lj-lyri:  ". .  der  den  ^'-el  erreichen  werden?"  Y.O^^g. .J.  sammt  den /Jnc^enoisen  rjri;ck>[ossc''  ^cm  V.  '^-.  —  Fi.:  .7,-.'-:  ,- :.-  i  :'.:r  .-; Y-J«*.!;  —  />V  sl^ditl  A.:ni.;:stir,'  isd.)  ~.'' 
dr^nili  yl  ^./üji^n  ■>d.^  .:.:J«f  <h-t;
.j-Jir  /■.jj-
.  aok-  V.  -sprechen".    Praei  33  -Itei
mt  V.  i".a5;  —  "«!.■  j'ii--".-        'sprechen  n  -,  anreden':
dby  Google
37    aog-
(stalt  Dat?J  aocayata  ..  afiurö  mazdh  "za N.  sprach  AhM."  V.  a:i.  7.
Vgl.  'ritf-.  —  Vgl.  gol,  aukjön  ■lärmen',  nserb.
uka  'Geschrei'?    S.  Hirt  Ablaut  132.  —  Vll.
ist  atiayala  eine  Neubildung  in  r/xta-,  wobei
iwxta-   (lu   a^i'')   untersiütiend  mitwirkie.  —
Pü. ;  J  netyötang  gii/l.
•  ]*.,  g.  aog-  V.  'praedicare'.  Praes. laog-  [,  22  flö/ffa]').—  PPfP.aox/a-,  PFP. aejya-.
Nur  Med.  i)  'verkünden,  sagen,  sprechen' (bes.  in  feierlicher  Form),  mit  Dat  der Person;  a)  mit  Akk,  alsObj.:  yS  paoiryo .  .  vJcim  aoxta  (sSPr.)  vidöyum  Yt.  13. 90.  b)  mit  Instr.  '(sprechen)  von  — ,
über  — ':  aat  masia  yimö  ku^a  .  .  var>m  : hr?naväne  yii  ml  aoxta  ahurä  V,  2, 31.  c)  mit  folgender  dir.  Rede:   äat
aoxta  zaraiiuitrö:  mmö  /taomifi  "drauf, sprach  Z.:  'Verehrung  dem  .ff.'"  Y.(j.i6, 3,  /£>.  17;  -1.2,  Az.  I,  Yl  /.  5,  21,  j.  2, 5.83,  91,  95,  i<.io,  77.54.  V.  2.  40,  42,' 3.  26,  Vyt  24,  54,  Vd.  12,  20;  —  ,7a/! Aim  aoxta  p»r>sö  yö  narl  asaonö  un'a:\ as.'a  ..  "und  es  sagte,  ihn  fragend  ..: 'Und  wer  ..'"  H.  2. 10;  —  äal  aoxta  akurö  \ ..  yimii:  yima  srira  "und  es  sprach  Ah.^ zu  y.:  'y.  . .'"  V.2.22; — yö  naire  aoxte (3SP0.-  M  ml
girfsaite  akur.li ..  uiti  aojanö  Yt/0.53; — yö  aoxta  a/iiiräi  ..uity aojanö''  Yt.  Ä 10;  J0.73,_V.2.io,j.2o;  —  fravasayö  .  .^ uityaojana^'  \\,tj.(>(>;  —  uifyaojana (NPm.)'>  mi>rHi  Yt.ro.41;  —  ätar! . . uiti  vacibii  aojanö  Yt.  19. 49;  5.76;  — ; aus. .uiti  vaülns  aojana  Yt/7.17;  22;i —  bulyqsta  . ,  uiti  aej^mna  uiti  daomna FrW.  10.  42.  2)  'verkünden,  nennen, bezeichnen  ab  — ,  wovon  sprechen  als  — ', mit  dopp.  Akk.:  ratavö  .  .  y5i  (als  AP.) aox
aoga  z  dastvma-
38
(7ö/iKfr(3PP.)V.;7.3.  a)  refl. 'sich  nennen, bezeichnen  als  — ,  heissen',  mit  praed.  Nom. : at  v3  staoil  aojJi^''  mazdä  anAScii  "euer Lobsänger,  o  M.,  will  ich  heissen  und sein"  Y.  jo.  1 1 ;  —  Tbwöi  staotaras^ä  .  . aogtmadascä^''  usftnaAiciJ (sd.)  vTsamada?c<l Y.  4/.$;    ziL    Aog.  7.  3)    'ansprechen,
anrufen';  aoxtö  rattis  aoxtö  sraoiävarjzö ci'iqm  frä^wfrisaiti  (sd.)  "der  (zu  dem Zweck)  angerufene  R.  .."  V.  7.  7 1 ;  5.  26'; —  yezi  .  .  apsrmSyukö  .  .  aoxtö  vä  Ae aoxte  '^wat  pairi.^auAa  "wenn  .  .  das Kind  .,  oder  angerufen  zu  ihm  sagt:  Ich will  dich  begleiten'"  N.  7;  7(?).  *aojaite V.  Ä'.8oPüZ.(?).  .
mit  avi  dnwS.  2,  mit  dopp.  Akk.:  pairi- AaySi,.yl  duiyäitya  nqma  yam  masyäka avi  duzvalanAö  Auyairyatn  natna  aojaite (3PP.)  YtÄ  51 ;  V.  13.  2,6.  '  a)  wie  2  a: m>r>y3  .  .  yim  malyska  avt  duivaear)hö kaArAatas  nqtna  aojaite  V. /A 15.
mit  S  dwnS.  i  er  a  dim  aoxta  ptnsö .  .  Aa>a  ..  H.2.16.
mitpaiti  'antworten',  mit  Dat  der  Person und  folg.  dir.  Rede:  äat  hi  mraom  . .  Hat ml  asm  pailyaoxta  .  .  nöti  dtltö  aAmi  V. 2.3;  Y.5.  2,  H,  2.  II  (paiti  aoxta),  Vyt. /,  6.  <V,  10,  12,  24,  2<V,  3j,  40,  43;  — paiti  ii  aoxta  a/iurö  H.i.2,T,  A.4.6,¥tW. 10.40,  *P.2j^\  Nik.2.
3806:•  p.  abi-cariS-''  n. 'Weide,  Weideland' {?)'*: äyaäanä  .  .  niyäyärayam  kära/iyä  °ris gafyamäi  mäniyamca  .  .  lyädis  gaumSla'' . .  adiR^  Bh.  1. 14.
7976:*)  Vgl.  Bd.  32.  y.  ha/i-äsir  äsraz-än  ml  mav patan  mavpat  iül,  IQO  säl  fas  (Aar)  den  lilarl. Eig.  'nach  Weiden  verlangend'.    —    ')  Hds. $al.v';  vgl.  Bd.  ja   10.
9856:•  j.  gao-yaotay-  f,  'Weideland,  Flur": ima  asiifa  Isdrasia  yaoitlffa  Y.  2.  16; —  xS  .  .  asBjiiihräsäi  'yagitisca  ätacinils (sd.)  Yt.<?.42; — aahqm  asanhqmca  sSiira- nqmca  yaoitinqmcaY.i.\6.  '  a)'Wcide': frayana  (sd,)  . .  pa'kanä  Jafrh  'tse  Ytio.
10177:•  j.  gavästrya-  Adj.  'was  sich  auf  die Weide  des  Rinds  bezieht',  sva.  'landwirt- schaftlich, bäuerlich':  a(tät..°yit<a  vartiriä ^vinsjnti  "..  und  verrichten  landwirtschaft- liche Arbeiten"  N.  60;  —  *°yaca  '>  vanmii N.  53;  —  °ya  *var3s>iä  N.  iV,.
11209:•  j.  Öanra-Dhak-  Adj.  (auch  fem.)  "was mit  der  Weide  zusammen,  auf  der  (zuge- wiesenen) Weide  heimisch  ist,  von  den domestizirten  Landtieren*';  gäus  yä  'äxs Yt/0.38;  —  ratavö  'Sca  (AP.)  Vr.2.1; —  vTspqmca  gqm . .  ravanaratamia  'ä^asca "all  Getier,  . .  das  in  der  Freiheit  haust, und  die  auf  der  Weide  heimischen  (Tiere)" Y.  71. 9;  —  ratavS  'äcqm  Vr.  /.  i ;  —  ururtJ .  .  'ä(qm  YL  y.  74.
11211:Komp.  mit  ''iat:  —  "tam-a-  m.  'Weide'  (an» ir.  ^eahra-,  %3ä6\i);  vgL  mp.  /.wa*')  'Weide', np.  MriddH')  'weiden';  s.Ji;5TiBd.  iiS,  DST. ZA.  /.  444,  Gdn.  KZ.  ?£401.  —  Pü.:  ratai ariänli  'suitable  for  ßrating'  (West).  —  >>  Re- gulär wäre  i-ar*;  es  haben  sich  wohl  im  Mp. Air'  'nmhergehen'  (sbaL  catafi  und  *Är*  "wei- den' vermischt  und  ansgeglichen.
12112:•  j.  taurvaetay-'>  m.  EN.  eines  Gläubigen ; /räcyeke  °tBis  aiaons  Yt  jy.  115,
14847:Et.?  —  Pü-i  afar  e  an  i  hart  man.  —  ')  Ir Ställea;  et  huidelt  sich  um  Stallvieh  im GegCDiali  mm  Airo-  and  Weidevieh,  wovon luvor  die  Rede  ist
16293:•  j,  pouru.västra-  Adj,  (fem.  °rä-)  'reich an  Weideiiächen':  garayasca  ySt..  °ränhs afintö  Yt.  y,  9;  10.  I4J  —  urvam  (sd.) 'ram  V.  /.  10;  —  urvai^a  (sd.)  ''ra  (NSf,) Yt.  1$.  67.
17759:•  j.  frayana-  n.  'Weg,  Bahn':  äiiri  mi- %rahe  'nä  .  .pähanä  jafrä  gaoyaotse  "klar sind  M.%  Wege  . .  weit  und  tief  zur  Weide" Ytio.  112.
8471:'  'um  "ranqm  uzuxfyenlinam  srlranqm zairi^aoiianqm  vaxsA  (sd.)  apayasaite  V. /Ä63;  Yt. /Ä6;  —  at  aRyäi  (näml.  dem Rind)  mazdä.  'rä  vaxiaj  (sd.)  Y.4S.6;  — avi  racynyq/H  varauhmt  azuitlmca  'ranam Yt.  ^2.3;  —  nima  'vaire  (VS.)  varMhi masdaöäte  asaone'V.  ig.ii;  Vyt.22,  N.7/, f)7.  a)  Plut.,  im  Gegens.  zu  alxa-  Plur., 'pflanzenbewachsener Boden';  ahond  una 'rlhuca  paiti  *baooisca  vTdtnanmnS  saoa- yäti  . .  ärvatS  urva  *aexahuea  (sd.) . .  "der Seele  des  Gläubigen  ist  es  so,  als  ob  sie auf  Wiesengiund  (stehe)  und  Wohlgerüche empfinde,  .."H.  2. 7— 25.  b)  sva, 'Baum', a)  im  Gegens.  zu  var^ä-.  pairi  van>'>iJ- byasca  'räbyas^a  atsmaiibyS  (sd.)  V.  16. s.  ß)  sonst:  v3r»ynahe  . .  yS  .  .  sainif marisat  'ranqm  ". .  der ..  im  Flug  der  Bäume Wipfel  streift'"  Yt./.4.2i''.  c)  'Pflanzen- Stengel,  Reis':  yavat  akmUi  paitinqm •ranqm  aetavat . .  "so  viel  es  ihm  einzelne Reiser  gibt,  (als  ob)  er  so  viel  .  ."  V.  iV. 86,  a)  bes.    der   zum  Barisman    ge-
9772:•  j.  gaeiSya-,  gae*ya-'>  Adj.  (fem.  ya-)  sehen  Baums*>:  ma  attmyöahurs  masäa 'stofflich  lebendig,  materiell'«:  vlspqm  ^urvarA  baSsasyä  uz^artm  paoirls  . .  dyum asaom  stm  ..  mainynnmca  '>yamc<i  Y.  '■„im  pairiyi.20.i,;  —  'mm  sünm  mazda- J5.1;  —  asmawm  ..  '■'ihm  ''i^yayn  r^jfy^  Yt.j.30,  S.a.  7;  —  'noAe  sarahe si5is'  Vr.  7.  4;    —    zaraiuitnm  .  .  -är«  I  mazdmätahe  Yt.  i.  30,  S.  /.  7.
22917:Vg\.'  vatpdu:  —  ai.  vgl.  avradanta  "tie  wur- den weich,  mürbe'  RV.  3.  14.  3.  —  Pö.: narm.  —  '>  Vgl.  varidutma-  —  ")  Pü.  fuhrt als  wcichholiigen  Baum  an:  vit  ('Weide')  1 «aß  ('feucht'?),  —  J)  Hds.  vtrid-.
23059:•  j.  varväa-  m.  'Baum':  °s»m  avt  spmtB.- /rasnä  (sd.)  V,22. 19.
23060:KompA.;  Ab1eit.(?].  —  ai.  vfiiä-  ta.  'Baum' (Bthl.  IF.  p.  273);  oosa.  ialäs  'Baum';  np. vgl.  variän  'Waldtaube'  (? ;  FrMOlibr  WZKM. 10.  375). —  Pü.:  veiaii-)  'Wald'.  ^ ')  Dessen Gleichsetiung  mit  variia-  bei  Salemann  GlrPh- T.  297  balle  ich  nicht  für  zulässig.
23062:KompE,  —  Ob  eig.  'was  dem  Baum  Leben gibt'  (IF.  g.  273)?  -  Pü.  (iü  V.  7/);  tiiok. Im  N.  p*):  buH-,  (lu  Y.  /o):  undeutlich,  SQ.: skanähalf.  —  ')  Im  Y.  vari'  geschr.  —  ')  Falsch Gdn.  KZ.  35.  559,  dem  Mills  folgt.
24514:•  }.  vispö.biä-  f.  Name  eines  mythischen Baums:  upa  avqm  vanqm  yqm  salnake yä  hiiittiie  maiilm  zrayatths  vpurukasahe yä  kubil'  }r^jwS.Us  yä  vaoce  'bis  (NS.) nqma  yqm  upairi  urvaranqm  vUpanqm taoxma  nilayat  "auf  jenem  Baum  des Adlers,  der  inmitten  des  Sees  V.  steht, der  gute,  kräftige  Heilmittel  birgt,  der  K
27000:gairJm  avi  'frasttä  (GD.)  varihm  avi 'framä  "zum  Berg  auf  dem,  zum  Baum, unter  dem  die  beiden  (näml.  AhM.  und Zflr.)  die  heiligen  Unterredungen  führen"
```


## [2026-10-16T05:15:07.428Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 23055,23061p BRT.txt | cut -c1-400; grep -n -E \"^ *•? *j?\\.? *va[eē][iï]?t[iï]\" BRT.txt | head; grep -n -E \"vaeti|vaüti|vaHti\" BRT.txt | head -5; grep -n -E \"^\\s*[0-9]+\\s*$\" BRT.txt | awk -F: '$1>22800 && $1<23100' | head"
}
```


### [2026-10-16T05:15:08.088Z] TOOL RESULT

```
Zum  V,  '■iiarn:  —  Vü.:  fa  an  i  Shrmazd  x'a- iiiJA  varälSr  i  amik  daJie.  —  i)  NA.  11»«- t/nyi,  s.  aber  Prol,  XXVK  a.  —  »)  Vgl-  iSt. Gdn.  GlrPh.r.  31.  Docli  können  Zeile  c  und d  der  Strophe  keine  Gegenüberstellung  ent- halten, da  son»l  itatt  nä  die  nichtenklitische Form  stehen  mülsle.     iKonstr.  a.  Sp.  715  m.
•  j.  varflzya-  n,  'Betätigung*:  man%rfmia 'ilmia  damayh  vanhuyi  mäzdayastßUX. 22.3.
Znm  V.  variz-.  —  Pü. :  varvstüh.
j.  giBiä  varis  N.  18:  lies  gmiSstrymiariS.
•  j.  varväa-  m.  'Baum':  °s»m  avt  spmtB.- /rasnä  (sd.)  V,22. 19.
KompA.;  Ab1eit.(?].  —  ai.  vfiiä-  ta.  'Baum' (Bthl.  IF.  p.  273);  oosa.  ialäs  'Baum';  np. vgl.  variän  'Waldtaube'  (? ;  FrMOlibr  WZKM. 10.  375). —  Pü.:  veiaii-)  'Wald'.  ^ ')  Dessen Gleichsetiung  mit  variia-  bei  Salemann  GlrPh- T.  297  balle  ich  nicht  für  zulässig.
•  j.  var«äa-gay- ■'  m.  'Wurzel"':  vupSsca paiti  'Jxi  Y.  /o.  5 ;  —  a  -jii  umaranqm .  .  vaxiyenie  {sA.)  YtÄ43;  —  uruhmJifa paiti  •jiica  "an  Schossen  und  Wurzeln" ¥.77.9.
20853:vaoiä  (sd.)  ys  Im  dät  "novi  (cum)  qiii .  ■" Y.45-4;  ö,  31.  19;  —  *malni/(sd.)  ys dngvaiU  xsä^rfm  Aun{iiil(sd.)  . .  yS  nöii jyUtam  (sd)  vlnastl  .  .  "poena  (eius)  qui . ,  eius  qui . ."  Y.JJ.  15;  —  rumanhä  (Sp. 1068  u.)  y!  . .  cista  yS  .  ,  dasdl  "respec- tuosus  (ei)  qui.."  Y-Jl-Sf.;  8; — yekya {zu  3)  iavS  isänii  . .  ySi  . .  *a»haricä dvaHti(ßd.yä  ". .  (ei)  qui  . ."  Y.  45. 7;  — yeAy3  . .  vahiibm  . .  valäs  maidä  . .  ySi äaharfcä  htnücä  "cuius  .  .  (eonim)  qui fuerunt  et  sunt"  Y.j/.  aa;  —  pirisä  ySi pi^yeitUI  (sd.)  "interrogo  (eps)  qui  . ."  Y. 44.  JO;  —  ä  vS  *gSus.ä  ÄsmyarUa  ySi  . . sännti  .  .  yassqm  ta  .  .  fradaxlts  akl ". .  (cum  üs)  qui  . .  quorum . ."  Y.5J.  3;
22883:1369
22886:1370
23018:1377
23069:1380
```


## [2026-10-16T05:15:13.045Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E \"Weidengerte|Weidenrute|Rute\" BRT.txt | head -8; sed -n 22910,22918p BRT.txt | cut -c1-300"
}
```


### [2026-10-16T05:15:13.595Z] TOOL RESULT

```
22000:•  j.  vaetÄy-  f.  'Weide;  Weidengerte': nava  'tayS  (als  AP.)  barat  (nämL  airyama) "neiui    Weidengerten    brachte    (A.)"    V.
22002:np.  bed,  äff.  vala;  ai.  vgL  vtlasä-  m.  'Rute'. —  Pü.:  lät  i  viU
22435:np,  bär  'Zweig'  (rfoRN  GlrPh.  /  b,  170);  gol. vgl,  wandus  'Rute'.  —  ■)  So  nach  JusTI  ZDMG. 50.  663,  53.  9z,  GIrPh.  2.  426.  Dagegen neuerdings  Fov  ZDMG.  54.  356,  55.  509.
•  j.  varaJbmna-  Adj.,  PPM.:  s.var^d-,
•  j.  varadusma-  n.  'weicher  Erdboden': matiySi  paitistane  (sd.)  xrüidisme  ma&)ysi narl  'sme  V.  Ä8;  — ■  aat  a%ra  mar/fm ava.kan5is  dlitlm  xrüiäisme  vUastIm  'sme ".  .  ein  Loch  . .,  eine  D.  tief  in  hartem, eine  V.   tief  in   weichem   Erdboden"  V,
'7-  5-
Ableil.  aus  'var>du-iam-  "was  aus  weicher Erde  besteht'.  *var>dav-  Adj.  sva.  vatidva-; vgl.  ai.  fbhiv-  und  j-bhvä-  Adj.,  yakäs-  und yaki/ä-  Adj.  —  Pü. :  mim  tamtk.
•  g.  varadamam  Inf.  'gross  zu  machen, zu  mehren':  ya%ra  .  .  x/ahrvm  ya'hrä mazdä  V  iaHtt  ahurö  "wo  das  Reich  . ., wo  MAh.  wohnt,  um  es  zu  mehren"  Y. ^.  i6'>.
Zum  V.  varid-,  s.  Bthl.  IF.  ro.  10.  —  ai. vgl.  vardhman-  D.  —  PQ.:  /a  kämak  (fiir vati)  andar  dm  n  n  (Sü.!  sthäne;  s.  nmäna- No.  7).  —  1)  S.  lu  Y.  3S.  3.
•  j.  varadva-  Adj.  (fem.  *va-)  'weich', vom  Holz  (und  der  Erde'*):  i!H.mass (sd.,  näml.  däuru)  xraoidvahe  bis  aeiavaiB 'dvahe  V.  /j.  30;  —  upa  tqm  vanqm vasaite  xraozdvanqtnÜa  (sd.)  'dvanqmia** V.  5.  I ;  —  aismanqm  xraoidvanqm  .  . •dvanqm  Y.14.2U  7.31;  —  *'dvS  F
Vg\.'  vatpdu:  —  ai.  vgl.  avradanta  "tie  wur- den weich,  mürbe'  RV.  3.  14.  3.  —  Pö.: narm.  —  '>  Vgl.  varidutma-  —  ")  Pü.  fuhrt als  wcichholiigen  Baum  an:  vit  ('Weide')  1 «aß  ('feucht'?),  —  J)  Hds.  vtrid-.
•  J.var93"a-  m.  'Verteidigungswaffe,  Wehr':
```


## [2026-10-16T05:15:16.444Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 21998,22003p BRT.txt | cut -c1-300; awk 'NR<22000 && /^\\s*1[0-9]{3}\\s*$/{l=$0} END{}; NR==22000{print \"col\",l}' BRT.txt; grep -n -E \"^ *•? *[0-9]?\\.? *vay-\" BRT.txt | head; "
}
```


### [2026-10-16T05:15:17.086Z] TOOL RESULT

```
3g.  12  grenzt  Erän  Vii  an  Aturpätakän [pa  iusiai  i  äiurpälaiän).  Es  ist  nicht  lu  be- stimmen, wohin  man  es  verlegt  hat.  Der  Ge- danke an  Arrän  [heute  JCarata-j  in  Armenien, dem  grossen  Bogen  des  Arat),  der  snletct 1  DsT.  ZA.  2.  5,  SBE.  4*-  2,  3  und  Gdn. GlrPh
Eig-  Bed.?  Die  Übersetzung 'germe  de»  Wiy"*'. 'the  Iranian  secd'  fusst  auf  der  falschen  Ver- bindung von  vaijah-  mit  np.  blj  'Same''); vgL  nba!.  hij,  ai.  bijam,  die  ar.  Ä*  erweisen, S  14.  ~  i)  Them.  —  »)  Nach  HoRK  NpEt. XIX  exislirt  das  Wort  überhaupt  nicht.
•  j.  vaetÄy-  f.  'Weide;  Weidengerte': nava  'tayS  (als  AP.)  barat  (nämL  airyama) "neiui    Weidengerten    brachte    (A.)"    V.
22.  30.
np.  bed,  äff.  vala;  ai.  vgL  vtlasä-  m.  'Rute'. —  Pü.:  lät  i  viU
•  j-.  g*  'vaed-,  j.  'vaeö'-''  V.  'kennen lernen'.  Praes.  i  vaid-'^,  30  (Kaus.)  vae- daya-,  Ta^aya-;  J-Aor.  i^'  vaB-'^ :  vis-; Perf.  3  va^d-'\  vaf^- :  vtd-,  »rä-.  — PPfP.  vista-,  PFP.  'va^ayania-,  InC "vlsiayaica,  valifysi,  vjduyl,  vidvansi, vSizäySi.
col 1309
```


## [2026-10-16T05:15:21.389Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E \"vay-.{0,60}(drehen|wickeln|weben|winden)\" BRT.txt | head -5; echo ---PHD; grep -n -i -E \"^ *(wēd|wed|wēšag|wesag|passox|pasox|pāsox)\\b\" PHD_mackenzie.txt PHD.txt | head; grep -n -i -E \"wyt|wyšk|pshw\" PHD_mackenzie.txt | head"
}
```


### [2026-10-16T05:15:22.011Z] TOOL RESULT

```
---PHD
PHD.txt:5203:wēšagīg wēšag wēšagestān zanī zanīhī wēd wīdwar wīdwarīh nidom bay! winah wināhīdan
PHD_mackenzie.txt:4085:pasox [p)shw I N --] = passox.
PHD_mackenzie.txt:4100:passox [pshw 1M pswx, N pasux] answer.
PHD_mackenzie.txt:5307:wed [wyt I N bed] willow.
PHD_mackenzie.txt:10182:wed                        \M,) \      I1t:mroz
1938:1dawidan, daw- [LHTWN-tn l < A"'; rh,; dwytn', dwb- I M dw-, N -]
3070: Jawed [y'wyt l I (P y'wyd), N ....,] eternal.
3072:JawedAn [LOLMN < A l-<lmn; y)wyt)n l I (P y)wyd)n, Mpyd)n), N--]
4100:passox [pshw 1M pswx, N pasux] answer.
5138:waydan [wyt'n l = Av. waySana-] head (ahuric).
5307:wed [wyt I N bed] willow.
5365:• widwar [wytwl] contented, resigned, consoled.
5662:xwed [hwyt' I M xwyd, N ......] moist, fresh.
5664:xwedodah [hwytw(k)ds, -d't' = Av. xV aetwada8a-] kin-marriage.
```


## [2026-10-16T05:15:25.701Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i -E \"^ *.?w[eē]šag|wysk|wyšk\" PHD_mackenzie.txt | head -5; echo ---NYB; grep -n -E \"^ *(vēt|wēt|vēšak|wēšak|passox|pasaxv|pa[ss]+axv|pāsax)\" NYB_vol2_glossary.txt | head; grep -n -E \"vēšak|wēšak|pasaxv|passaxv|vēt\\b\" NYB_vol2_glossary.txt | head"
}
```


### [2026-10-16T05:15:26.040Z] TOOL RESULT

```
5670:xwM-kar [hwysk)l] dutiful.
---NYB
4100:vēt-varēh
671:aržānīkēnītan [~-ynytn'] to consider a p. worthy, governing a subordinated clause without an introducing particle, 5318 in a very complicated passage 5317-21, which only seems possible to understand on the following suppositions: a) kū-t bahr hac man bé burt l. 19 is not a gloss, as I have marked it, but is governed by anak tč bavat l. 17 ‘it shall be unhappy for thee that thou hast bereft ...'; b) the clause kē ... aržānīkēnīt hom 1.17-19 is loosely attached to tē l.17; c) for MNW-t L<y> (MS very clearly MNWtl) read MNW kw) LY» = kē tē man, to man being the exact counterpart of LK ^NH = tč an (v. žan) 1. 19 and both signifying ‘thou and I’; d) YBLWN-m l. 18 and 20, and HWH'-m 1. 19, are the Ist. p. pl. coinciding with the Ist p. sg.; e) there is a wordplay between *š = dé ‘food’ l. 18 and ’$ = as (demonic) eye’ 1. 20 (as burtan 'to have a vision', v. 'aš; bahr ‘ministry’, v. this w.). Text: anàk tč bavat, marak, ke t(0» man fratom hac ax" i astomand andar Rdg u Notar hac bahr barišneh āš barom frac aržānīkēnīt hom, kū-t bakr hac man bē burt. niin-ip tē an pat apar-barišneh aš barom u et bavēt kū-t dušcašmiha al zänak nikēram i-t nest ‘unhappy shall it be for thee, little scoundrel, (that thou) — as thou and I first of all men in the material world between Räg and Notar have been found worthy of earning food by perfor- mance of ministry — that thou hast bereft me of the ministry. Now thou and I shall be enraptured in an ecstatic vision, and then it will happen that I shall see thee evil-minded in another house that is not thine’. The passage is the immediate continuation of the incident related in 537-15, Zsprm XII, 7 epitomizes 5316-21 as follows: dwlyslwb BR’ L zltwšt gwpt' "VK cygwnt pltwm HWH'-m b’hl wlweyk BR’ ’pknd HWH'-m ZK tw "NH KR?
854:ayyaritan [’dyb’lytn'] to dare, to venture; governing a subordinate clause without conj.: kas nč ayydrit frac šavēt 164; frac ö peš ne ayyārīt šavēt 25%. — As to the ligature ayyd- v. I, 136. - NP ydridan ‘to be able’.
888:bägö-baxt [b'gwbht'] divine providence 777118. cf the definition Mx ch. 249-77: äsn baxt han bavēt i hac fratomeh bat Estet, u bagdbaxt hàn i dit-ic baxsend “innate bazt is that which has been allotted from the very beginning, and ~ is that which they
948:bavētān [YEIWWN-yt'n'] pl. cas. obl. of bavēt ‘he will be’ (v. bütan) used as a
950:subst. ‘he who will be’ = the future, coming man: har hastän butan bavētān all those who are, who have been, and who will be 5518, — Cf the use of Jv as a subst. in Apocal. 1:4.8 ó àv x«i 6 Av xal ó čpy0- uevoc.
972:the v. n. and the pt.: bé tacét, bé tacitan, bé tacióneh (e.g. 564); be šutan to go away, to disappear, bē šutak gone, van- ished 5?; etc. — b) denoting the per- fective aspect of the act, viz. that it comes to an end, or has its limit: with the pret. it gives it the sense of an act completed in the past, as in French the passé défini or in Lat. the perfectum historicum; with the pres. it denotes the completion of the aet in the future (Milr. has no special future tense); it is very often put before an imp., giving the order a peremptory force; also used in other expressions implying an act of will, cf apdyistan and framūtan; in this sense it does not stand together with an inf., or with a pt., nor with a negation, nor with other preverbs (which themselves give a_ perfective sense): be bavét he will be, but nē bavēt he will not be. The functions a) and b) are often difficult to keep apart. — 3. prep. a) except, but: hec zvandak apdc bà nē mānēt be hàn i ēvak Arjāsp no one but A. alone 2926-27; 2415-16; 964; cärak be man an kas xYāstan nē tuvān it is not possible to request a means from any other than me 34?; followed by a sub- ordinate clause: nisem nē vindät bē ka
1061:become, to occur, to happen, to come true; to arise, to come into existence, to grow, to originate; to exist, to be, passim; héc ké büt hénd u héc ké bavénd u héc ké hend 6417-18, cf bütün, hame-buteh, hame- baveteh, bavētān ; dané ku fratäk rēc ce bavet thou knowest what will happen to-mor- row 21°; apdyet butan, v. apčiyistan; būt i zivist u būt i murt hend there were some who survived, and there were some who died 95?” sg.; būt dastavar ké-§ guft there was a certain Dastur who said 1018; būt kē-š guft there was someone who said, erat gut diceret 103?9; h&c kas nē būt ke ... dänist there was nobody
1064:nē būt 675-26; bavēt... Zartuxst it must be Z. 6023; nē yatük: [YHWWN-#'] bavat he cannot possibly be a sorcerer 3774, v. Grammar 53. — 3. In the 3d p., together with a subst. virtually in dat., or with a pron. in cas.obl., it expresses the notion ‘to have’, e.g. õi kē-š zan nē būt he who did not have a wife 101!; amdvandéh ... i-m būt the vigour which I had 341; -t dānākēh bavét wisdom will be allotted to thee 595; duxtar i varzēkarān én hunar ... i to hast ne bavet a farmer's daughter cannot have such an ability as thou hast 18520-21; with rád as in NP: Pdpak ràd hec fradand nē but P. had no child 19-7. — 4. Together with verbal or other nouns it forms periphrastic verbal expressions: (7) matār būt hēnd who used to go 61”; nikeräi (g. v.) bavét 8214; tō . . . ästisn ne but hah thou wouldst not have subsisted 3515-16, 3421-22; _$ hàm zan... ayyät bit he remembered that woman 1111-12; 123-4; -§ vat hayyär bavét the wind helps him 25; Ohurmazd ziyān ne bavēt O. will suffer no harm 7727; v. also äkasi, hangir- tikeh. — 5. With preverbs: andar ~, v. andar; — apäc ~ to become again 7714-15, 10021-22, 12025; to come into existence again, to be restored to life 46°. 10416-26; to be left, to remain 39277. 4416; — apäk m = apāc ~ 3423; as to 161-7, 2426-27, v, apäk; — apar ~ to be imparted to 80%; — fräc ~ to recover (hac from) 5419.12, 6022; — 6 ~ to approach, to come on 65; to pass into 4216-17; — 6 ham ~ to be put together, to be formed (from different elements) 4317; v. also hambavisneh. — 6. As an auxiliary vb. added to the pt. pret., būt forms the pluperf. in dependent clauses, as against ēstāt in independent sentences: pas hac han + Artaxser han kirm ēzat būt after A. had slain this
1427:46 Py; HN?], old ev [yw], particle de- noting the opt. 1. ev: ~ HNHTWN. HajB:13 (v. nihätan); ču ŠDYTN ibd. 14 (v. vistan); ev ‘BYDWN F:5 (v. kartan); év göbet 128? (v. guftan). — 2. € Dy]: frāc & yazēt 539; ē nikecet 60%; han ē bavēt 1095. — 3. HN’: bē ē raset 604. — 4. encl. and written HWHw-yd = (h)e 61: āyēnd ~ they would cover (a distance of ...), ef the yäy-i Sart and the yày-i tamannā in early NP. — Av. (22) aēvā; Paz. č (SGV).
1952:hast PYT'] 1. pres. 3d p. sg. of h-, g. v. — 2. as subst. pl. hastän those who exist 578; 5518 v. bavētān. — 3. abstr. subst. existence, mode of existence 312. 4218, frac hac ~ raft he disappeared 501,
```


## [2026-10-16T05:15:29.826Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 4098,4102p NYB_vol2_glossary.txt | cut -c1-300; grep -n -o -E \".{0,80}(wyšk|vēšak|wēšag|vēšag).{0,120}\" PHD_mackenzie.txt NYB_vol2_glossary.txt | head -5; grep -n -o -E \"^.{0,5}(wešag|weš[ao]g|wesag|westag).{0,120}\" PHD_mackenzie.txt | head"
}
```


### [2026-10-16T05:15:32.863Z] TOOL RESULT

```
*vét-varéh [wytwlyh] "(the act of) heal- ing; comfort, consolation 66°. — Abstr. of vét-var; the form bytwlyh PT 154”, reflecting the later (but probably fairly early) development of initial v- > b- (cf bahän), eliminates the reading nyt- proposed by G. Ito (JLSJ 14, 1949, 28— 29). This w. and its d
www.parsianjoman.org ol wrk
vēt-varēh
Dhabhar vētvar, without etymology, in the sense of ‘contented, contentment, forbearance, patient, consoling oneself (‘consoling’ already West), resigned to the will of God’ (~ dätan ‘to console’); Hormazdyar with the same etymology as Bailey, but giving the same senses as Dhabhar (‘one who endures g
14 Nyberg
ugrep: error: error at position 108
ag|vēšag)(?:[^\n\x80-\xbf][\x80-\xbf]*){0,120}
                 exceeds complexity limits___/
```


## [2026-10-16T05:15:35.876Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E \"wyšk|wysk'|wešag|wēšag|wešak\" PHD_mackenzie.txt | head -5; grep -n -E \"wyšk|vēšak|wēšak\" NYB_vol2_glossary.txt | head -3 | cut -c1-300; grep -n -E \"pasaxv|passaxv|pasax\" NYB_vol2_glossary.txt | head -3 | cut -c1-300"
}
```


### [2026-10-16T05:15:36.199Z] TOOL RESULT

```
4097:včšak [wyšk'] reed, bunch of reeds 93°”. — NP besah.
4387:xučš-karčh [hwyšk'lyh] 1. the perfor- mance of one’s own work: one’s task, mission, function 4718.776. 815-12-14, — 2. the performance of the proper, right and righteous work: the whole system of religious duties incumbent on a Mazda- yasnian, the moral law 378; it comprises numerous different 
7063:bēšah: vēšak
6769:patmoxtan pašsār: patisär padvazed: pat-vac- padyavand- patiyavand pšč: pad paēdā, paidà: paitäk pačma(n): patman pačvand: patvand pačvastan: patvastan pahalim, pahlum : pahlom paharčxtan, paharčž-: pahrčxtan parastidan: paristätan pardazašn: pardaxtan pasand: passand pasaxt: passaxt päsux: pas
```


## [2026-10-16T05:15:40.091Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E \"^ *[0-9]+\\. *(bed|bes|päs|pas)\" HRN.txt | head -20; grep -n -E \"pāsux|päsux|päsuh|päsox\" HRN.txt HUB.txt | head"
}
```


### [2026-10-16T05:15:40.461Z] TOOL RESULT

```
2292:219. besten 'binden', Praes. bend-em., bend,
2315:222. beskärT ^Bestellung des Feldes.
2328:225. besäten (büsöden) 'Bösewicht'.
2716:274. päs 'Schutz*, pasban^ päsTden,
2724:275. päsu% 'Antwort'.
10248:49. bes *Leid, Unheil* (Men.), hesitan, hns{i)sn, beSttar (aw.
10848:155. pasta/n (der Infinitiv kommt nicht vor) 'fliegen , mit
```


## [2026-10-16T05:15:42.750Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 2724,2735p HRN.txt; grep -n -E \"^ *2[0-9][0-9]\\. *b[eé]\" HRN.txt | head -30"
}
```


### [2026-10-16T05:15:43.225Z] TOOL RESULT

```
275. päsu% 'Antwort'.
aw. ^paitisahva- [paiti + [/'safih- hat zwar im Awesta
nur die Bedeutung 'beschwören') ; phlv. pasu/ ; arm.
patas/ani 'Antwort*.
276. päSne 'Ferse'.
aw. päsna- 'Ferse'; phlv. päsnak*^ ai. pdrsni-,
kurd. päsüne, päm, päme (ZDMG. 38, 55), päm (JJ.);
af/. pünda ; bei. pünzig, ptnz, n. pTz, pid (306) ; wa/.
päsna, sar. pu/nä 'Ferse'.
syr. LW. j^li/^B 'der Bimstein, mit welchem man
sich im Bade die Fersen reibt', de Lagarde, Ges.
Abh. 73.
2150:200. berseiu 'Barsomzweig' (Sahn.).
2175:204. bevf/er 'Glück'.
2179:205. bergustuwän 'Panzer, Pferdepanzer'.
2185:206. bern 'Egge'.
2219:209. bemT 'Gefäss* (unbelegt).
2224:210. bervär *Sommerlusthaus*, nn^X, nxnDN (Talmud).
2229:211. berre, bere 'Lamm*.
2270:215. bezni *Fest'.
2273:216. beze 'Sünde, Unrecht', bezegär ^Sünder*.
2292:219. besten 'binden', Praes. bend-em., bend,
2306:221. beS-, bis-, Praefix, s-; vergl. usnäti (No. 89).
2315:222. beskärT ^Bestellung des Feldes.
2328:225. besäten (büsöden) 'Bösewicht'.
2336:226. bet *Ente ; xer]bet Idiot'.
2383:230. bende *Sklave, Diener'.
2476:242. behä 'Wert'.
2495:243. behär Trühling .
2501:244. behäne Torwand'.
2505:245. behVy hehre Xoos, Teil'.
2523:247. be, ehe 'ohne'.
2575:252. berun 'aussen, heraus, blrün, |J<*)'»2, Ps. 68, 7,8
2580:253. beSe, wez^ weze Vein, lauter, edel', NTÖ (Is. 59, 7),
2592:255. beS, bester mehr .
2648:262. bever 'tausend'.
2651:263. beve Wittwe'.
2657:264. beyoj^beyök 'Braut*, :V2 (Jer. 16, 9).
```


## [2026-10-16T05:15:46.760Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E \"Weide|Wald|Gebüsch|Dickicht\" HRN.txt | head; grep -n -E \"Weide|Wald|Dickicht|päsux|pasux\" HUB.txt | head"
}
```


### [2026-10-16T05:15:47.103Z] TOOL RESULT

```
2355:Wald'.
2356:af/. vana 'Baum'; oss. d. ^bun, t. -bin *Wald' (67);
2568:251. hed Weide i), h(i)Öe (AM. 182 Zeile 2 v. u.), baraq4
2571:äw. vaeiti^^\ *Weide' ; phlv. vet ; ai. vergl. vetasd-
2603:)6. bese 'Wald, Dickicht', jüd.-pers. |NnDn:r^2 (Is. 2, 13).
2605:aw. varesa- *Wald'; phlv. vesaJc; ai. tjksd- *Bauin';
3478:Wald)' wohl LW. (243); bei. LW. tär, n. tar (269);
4060:arm. LW. carak 'Weide', carakem; ai. [/car-, cdrati
8473:Hörn, ZDMG. 43, 51)^); ai. mrgd- 'Waldtiej-; Vogel*.
10535:oss. d. yädä, t. qäd 'Baum, Balken, Holz, Wald' (?)
1031:(also — *im Walde wachsend). Mir nicht wahrschein-
1110:251. Dazu afgh. vala 'Weide* (nach Geiger), als Lehn-
1111:wort afgh. bSd *Weide'.
1126:256. Np. heSa *Wald* (= ap. *vaisa') kann ich mit zd. varesa-
1206:p. 103) ist nach np. und paz. pasux (Shk. 263, Min.
1787:439. Phi. 6arah ^Weide bei West, PT. I, 374. Fuge
4398:zd. nava^); ausl. -ux aus -axv: pasux 'Antwort* = phi.
4670:gift*, paz. pad(a)zah(a)r Shk. 261 ; np. paz. pasux *Antwort*,
5468:gvat gecag Xuft zufacheln ; bsd *Weide' = zd. vaeiti-^ bal.
5469:ged^; besa 'Wald' = phi. vSSak; bes mehr' = paz. vBs Min.
```


## [2026-10-16T05:15:50.313Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 2603,2610p HRN.txt; sed -n 1124,1132p HUB.txt; sed -n 4396,4400p HUB.txt; sed -n 1204,1208p HUB.txt"
}
```


### [2026-10-16T05:15:50.747Z] TOOL RESULT

```
)6. bese 'Wald, Dickicht', jüd.-pers. |NnDn:r^2 (Is. 2, 13).
Käs. Visa; mäz. täl. vtsi.
aw. varesa- *Wald'; phlv. vesaJc; ai. tjksd- *Bauin';
dazu gr. älaog (Bartholomae, briefl. Mitteilung),
kurd. vise (H.-Sch.).
37. bei ^Grabscheit* ^).
Käs. 6ör, böl, bäl^ berd.
Zu aw. [/^bray- schneiden' (de Lagarde, Ges. Abh.
ware. Jedenfalls setzt bal. gBs ein iran. *oais^ voraus,
auf das auch np. bes zuriickgehen muss.
256. Np. heSa *Wald* (= ap. *vaisa') kann ich mit zd. varesa-
{= np. *5a5 oder *bus) lautlich nicht vereinigen. Die
Entstehung von gr. ciXaog aus *fal}iaog (Bartholomae)
ist ganz unsicher.
257. Ich kann np. bel, bll *Spaten' (nach Vullers auch =
remus', nach Rosen, Np.Sprachf. p. 50 = *Schaufer),^)
belca *Hacke, Spaten nicht mit den Dialectformen bal
bavdt = ap. bavatiy); nuvad^) neunzig' = zd. navaiti; nuh
*neun' aus *w^< (mit h nach dah zehn') fiir *nuv = *nav,
zd. nava^); ausl. -ux aus -axv: pasux 'Antwort* = phi.
pasaxv (oben p. 36, Pandnama Gl. p. 99) ; farrux 'gliicklich'
= phi. fairaxv; suxtin ^= suxan *Wort', paz. saxun aus
entstanden sein, wie pasCtxt aus patsCixt,
275. Neben dem gewohnlichen phi. pasaxv (61. and Ind.
p. 103) ist nach np. und paz. pasux (Shk. 263, Min.
haufig) ein phi. *pasaxv anzusetzen, jenes aus *patsaxv,
dieses aus *patsaQcv (vgl. Sirm, patasxani 'Antwort').
```


## [2026-10-16T05:15:57.256Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources; python3 -c \"\nimport json;d=json.load(open('refs_online.json'))\nfor k in ['BQT','MON','ARY','SNS','ISS','TZF','AVG','KLN','SYN','IEC','WLD']: print(k, json.dumps({x:d[k].get(x) for x in ['page_offset','lookup_hint','local_file']},ensure_ascii=False)[:600]); print()\n\""
}
```


### [2026-10-16T05:15:57.731Z] TOOL RESULT

```
BQT {"page_offset": "vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209

MON {"page_offset": null, "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different pagination fr

ARY {"page_offset": "printed page = pdf page + 1", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY:<printed page> --image", "local_file": ["/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY/ARY_pages.txt", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt"]}

SNS {"page_offset": "242 leaves; page offset not determined (OCR too poor to read printed numbers) — locate by transliteration then read the page image", "lookup_hint": "grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php search (see BQT) for better hit-to-leaf mapping.", "local_file": ["/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SNS_pages.txt", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SNS.txt"]}

ISS {"page_offset": "DKS: leaf = printed + 17..19 (e.g. leaf 158 = p.139). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Khotanese Texts VI itself is not online. Nourai's ISS page numbers cannot be checked directly; the Dictionary of Khotan Saka (headword at line start, Khotanese in transliteration, with 'Pok.' refs) covers the same etymological material and can verify the substance of a claim.", "local_file": null}

TZF {"page_offset": null, "lookup_hint": "Not on archive.org (only his دستور تاریخی زبان فارسی: archive.org/details/20220417_20220417_2237, and تاریخ زبان فارسی on samta.samt.ac.ir / library.tebyan.net/f/Viewer/Pdf/168187 which overlap in content).", "local_file": null}

AVG {"page_offset": "leaf = printed + 54 (e.g. leaf 61 = p.7). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Grammar by numbered §; grep the § number or Avestan word.", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/AVG.txt"}

KLN {"page_offset": "KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.", "local_file": "/home/sfmqrb

SYN {"page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the concept heading (all caps English word) or a printed page number line.", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/SYN.txt"}

IEC {"page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root.", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/IEC.txt"}

WLD {"page_offset": "Band 3: leaf = printed + 6. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> || Band I (WLD_Bd1_pages.txt, 887 leaves): printed = leaf(1-based) − 9 (leaf 801 = p.792). Band II (WLD_Bd2_pages.txt, 720 leaves): printed = leaf − 5 (leaf 701 = p.696).", "lookup_hint": "Band 3 is the index (Wortregister by language) - it maps a word to 'Band, page' in vols 1-2, so it can at least confirm that a word is treated at the cited WP volume/page. For the actual entry text, use Pokorn
```


## [2026-10-16T05:16:03.015Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E \"\\[pdf page (54[5-9]|55[0-9]|560)\\]\" BQT_v1_pages.txt | head -20; grep -n -i -E \"vaēti|vaeiti|vêt|vēt\\b|vêšak|vēšak|vešak|varəša|varesa\" BQT_v1_pages.txt | head"
}
```


### [2026-10-16T05:16:03.347Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-16T05:16:05.921Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; head -c 600 BQT_v1_pages.txt; echo; grep -c $'\\f' BQT_v1_pages.txt; grep -n -E \"بیشه|بید \" BQT_v1_pages.txt | head -20"
}
```


### [2026-10-16T05:16:06.262Z] TOOL RESULT

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
‌ ۰ م�
766
2065:القبایل هرسه تا یف ابوعبید قاسم بن سلام هروی متوفی در ۲۲۳ و کتاب
3544:شیمای بیشه ۱۴ (ذیل : تميشه ).
3563:نیز ربا. کیلکی  :۲6۷۷‏ ۱ مولف ذیل «ن‌یشه» گوید: نام بیشه‌ایست درنواحی شهرآمل
5859:آ یب س بسکون بای ابید . ممر‌وف است
9405:شاد نهادن‌شپراسکتدریه 1 آبرا باسکندر مقدونی نسست میدادند» آ بیشهرا نیز بدواهماب‌دادند :
11841:ابید هم بنظی آعده است » و بامقاط تالف ۳
12878:نوعی ازحرشفاس تکه بفارسی‌بید گیا و کزماز که
14208:آثدر خو دك هه بنکون داز ابید .
16145:بروشت کوسفندان بچنبید » پی حد آندوزشاطی
16541:پار ید ۱ د بت بای ابید رسکون‌دال
17271:باشد که بعربی‌حصین‌البان گوبند - و «شك بید را
17875:که آنرا بید گیا خوانند. وآن نوعی از کنگر
18435:سبز شد وروبید - وبمعنی درغشب شدوقپر آ لوده
20337:کریزکاه - و جنگل و بیشه هم آمده است -
22286:بید خت ؟ - با بای مجهول بر وزن
22296:بیك‌ طبر ی « نوعی از بید باشد وبعضی
22298:پید موله را کویند که بید مجنون باشد .
22310:بقیه ازصفحهٌ ۳۳۲بید کیا
22311:بید گیا - بکر کاف فارسی و نحتانی
22320:و سایر اسلحه بچوب_بید با چوب دیگر که
```


## [2026-10-16T05:16:08.876Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 tools/ref_page.py BQT:332 --image 2>&1 | tail -60"
}
```


### [2026-10-16T05:16:09.339Z] TOOL RESULT

```
no scan of BQT covers printed page 332 (see 'scans' in refs_online.json)
```


## [2026-10-16T05:16:12.892Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk -v RS='\\f' '/بید خت/ {print NR}' BQT_v1_pages.txt; awk -v RS='\\f' 'NR==552' BQT_v1_pages.txt | head -150"
}
```


### [2026-10-16T05:16:13.615Z] TOOL RESULT

```
554
بجوم
آب با بخون ۱ .
باآب یا بخون ۱ .
نی خساند و ق م کرد - و آحیخت و سرشت
آب و با پفون و چرك ٩‏ .
‌ بباغالیدن بالام بروزن طلامالیدن:
بمعنی تحريك‌نمودن وتحر صکردن بلشد ۴ .
لیاغشت « بکر رابعم و سکون شین
و تای قرشت: بمعنی بیافاشت است؛یعنی‌خیسانید
وم کرد وآمیخت وسرشت؟ .
یا فك - یکی اول وسکون کاف‌بروزن
صیات ء کیاهی باشد که اژآن بورما بافند .
بیا نه » بفتح اول بر وزن زمانه » نام
شهرست در هندوستان که نیل ازآنجا خیزد ۰
و آن چیزی باند که بدان چیزها رنگه
۳
بیاواد ع بفتح اول بر وزن حزاوار »
بمعتی شفل و کار و عمل باشد .
لیاه - بکر اول بر وژن سیاه » نم
رودخانه ایست بسیار بزر که در نولحی لاهور .
بی بالگ » بمعنی ی قری و هطقن
(۱) چك : ژند و پاژند .
۱ _ رف : آغاردن وآختتن .
چه با بمعنی تری و شمع‌آمده ابت- وکنابه
یی هر ۵ - بمعنی بن اصیب و قسمت
و کنابه از کدا ودروش و پربشان و می چیز
پاشد . ۱ ۱
یی یی" - بکسرهردو با وسکون هردو
با . زن لیکو و خاتون خانه راگونند -
فیت" - با اول بثانی رسیده و فوفالیبالف
کشیده » بلفت زند ویازند (۱) بعشی خانه است
که بعربی میت خوانند .
تفه با فوقایی ؛ مر وزن و معنی
ییگانه است که شیض" آشنا باشد بلقت زد
و بازند (۱) .
یت فراغ » کنابه از متوخاست که
آدیخانه باشد ۰
بیحاد - با ا: ی مجهول بر وزن اسحاد .
قعت خلی: ات ی وم
کوند ییجاده آست که پر مرغ "را جذب
کف
یجاذه - با ثالی‌مجهول بروزن بی‌باده»
بیجاده نومی ار بافوت است ۷ .
تر کی شرقی است
۴ - هز , 0102 . پپلوی 18202 :
۵ هز» 8 , پهلوی
۷ ره : بسجاده,
رین فیزوزه طشت آزخون چشمم
```


## [2026-10-16T05:16:16.985Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk -v RS='\\f' 'NR>=553 && NR<=554' BQT_v1_pages.txt | grep -n -E \"بید|vet|vêt|Weide|willow|salix|پهلوی|اوستا\" | head -30"
}
```


### [2026-10-16T05:16:17.459Z] TOOL RESULT

```
41:۴ - بایراییان کفت بیدار بد
52:بید‌ار مقر - کنابه از هردم عافل
55:از پیکان تبر باشد شبیه ببر که بید.
56:بیدخج ه بفتح اول بر وزن برزخ» اسب
61:بید خت ؟ - با بای مجهول بر وزن
71:بیك‌ طبر ی « نوعی از بید باشد وبعضی
73:پید موله را کویند که بید مجنون باشد .
```


## [2026-10-16T05:16:20.575Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk -v RS='\\f' 'NR==553' BQT_v1_pages.txt | sed -n 1,60p"
}
```


### [2026-10-16T05:16:20.997Z] TOOL RESULT

```
که پس رکیوین کودرز باشد .
یحو هر - کنابه از مردم بی هنرویی
عفل و هیچمکاره باشد .
کنابه ازگوشت است که بتازی لحم کوند .9
لیکستن « بکر اول بروزن دلبستن»
بمعنی درماندن و عاجز شدن باشد .
و عاجز شده - و محبوس و بندیرا گویند.
بیکشت مه بنتح اول وضم ثالث بر وزن
زردشت » هر چیز کهآ نرا از یخ بر کنده باشند
ماشد درخت و امثال‌آن » ومجای شین قطه دار
صین ی نقطه هم آمده استه وف ورست ات
چه در فارسی هر دو بهم تبدیل می‌بابند چنانکه
ور فواید گذشت .
بیخ کوهی - بر کاف بواو رسیده
شو کران باشد و آنرا بیونانی نودربون کوشده
و بپترین آنرا از تفت آورند و تفت از اعمال
بزد است .
(۱) چك : خا.
( رن
۱۳۳ ت
ی خویش ه با واو ممدوله‌پروزن
بی دیش ؛ بی خود و بی‌هوش را کوبند .
لی خی لسن با :ای فرشت » بمعنی
ی خیله » با خای نقطه دار بر وزن بی
حیله . خرفه را کونند و جربی بقلة الحمقا
خوانند .
فيك بکسر ارل و سکون ثانی ودال»
نام درختی است مشهور و آنر! بعر ی صفصافی
خوانند ۴ - و تام دیوی بوده در مازسران که
رستم او را کشت - و بمعنی «باشید» و «بوید»
ضت؟ - و کرهکی را نیز گویند که کاغذ
وجاههای شمین‌را
و تباه مازد؟ -
و بمنی ببهوده
و می فایده و نا
سودمند باشد یه
وفتی که مرادف بادباشدچت‌انکه گونند «بادویید»
بمنی بی فایده و ناسودمند - و بزبان حندی تلم
کتایی است6 مشثمل‌براحکام‌دین حندوان وباعتقاد
ص ۷۲۹ ۰ .
۴ - بایراییان کفت بیدار بد
۴ - رف : بت (یکسر اول).
زییکار دشمن عشوار ببد. فر دوسی‌طوسی.
قبه در سفحه ۳۳۳
```


## [2026-10-16T05:16:23.887Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 22300,22330p BQT_v1_pages.txt"
}
```


### [2026-10-16T05:16:24.342Z] TOOL RESULT

```
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
بقیه ازصفحهٌ ۳۳۲بید کیا
بید گیا - بکر کاف فارسی و نحتانی
بالف کشیده . نوعی از حرشف است که کنگی
باشد. سرد دخشك است در اول. جراحتهای‌نازمرا
غافع باشد .
ثيل لا - پکس اول وئالث وسکون‌نانی
مجپول و لام بالف کشیده . سخنان بی ربط
و حذبانرا گونند .
بیدمال - با میم کشیده بر وزن تيك
فال » با کردن زنگه باشدازرو ی آیینه وشمشیر
و سایر اسلحه بچوب_بید با چوب دیگر که
این کار را شایف.
دیل مشاث - نوعی ازیید است که بهار
آن عنی شکوفه‌آن بغایت خوشبوی هبباشد (۱)
و عرق را یجهت نفریح دل و تبرید
باشامند ۷ .
نید موش « بروزن فبل گوش, بععنی
بیدمشك‌باشد وآنراکرية بید هم میگوند.
لیدواد - با ثانی مجهول بر وزن
یشواز. نام کوهی است از ولات ماوراد النهر.
بیلو فك - با واو بروزن ربشخند » نام
```


## [2026-10-16T05:16:28.209Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; ls pageimg | head; ls ocr; ls ocr/BQT 2>/dev/null | head; python3 -c \"\nimport json;d=json.load(open('../refs_online.json'));print(json.dumps(d['BQT'],ensure_ascii=False)[600:2500])\""
}
```


### [2026-10-16T05:16:28.638Z] TOOL RESULT

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
drwxr-xr-x     - sfmqrb 14 Oct 22:47  ARY
drwxr-xr-x     - sfmqrb 14 Oct 22:19  BLY
drwxr-xr-x     - sfmqrb 14 Oct 22:50  BOOK
drwxr-xr-x     - sfmqrb 16 Oct 01:16  BQT
drwxr-xr-x     - sfmqrb 14 Oct 22:48  FFD
drwxr-xr-x     - sfmqrb 14 Oct 22:19  HRN
drwxr-xr-x     - sfmqrb 14 Oct 22:19  IRN
drwxr-xr-x     - sfmqrb 14 Oct 22:27  PLA
drwxr-xr-x     - sfmqrb 14 Oct 22:48  SNS
drwxr-xr-x     - sfmqrb 14 Oct 22:19  SOD
drwxr-xr-x     - sfmqrb 14 Oct 22:19  TAD
Permissions Size User   Date Modified Name
.rw-r--r--  368k sfmqrb 14 Oct 22:19  0001.png
.rw-r--r--  1.7k sfmqrb 14 Oct 22:19  0001.txt
.rw-r--r--  534k sfmqrb 14 Oct 22:19  0049.png
.rw-r--r--  2.7k sfmqrb 14 Oct 22:19  0049.txt
.rw-r--r--  190k sfmqrb 14 Oct 22:30  0143.jpg
.rw-r--r--   576 sfmqrb 14 Oct 22:30  0143.vision.txt
.rw-r--r--  472k sfmqrb 14 Oct 22:45  0339.jpg
.rw-r--r--   849 sfmqrb 14 Oct 22:45  0339.vision.txt
.rw-r--r--  221k sfmqrb 16 Oct 01:15  0342.jpg
596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.com (links from farhangoadabeirani.blogsky.com post-482): vol 3 https://s3.picofile.com/file/8230740968/borhane_ghatee_jelde_3.pdf.html (ش–ل, Ibn Sina 2nd ed. 1342, 721 pp), vol 4 https://s6.picofile.com/file/8230741184/borhane_ghatee_jelde_4.pdf.html (م–ی, 553 pp), vol 5 https://s3.picofile.com/file/8230741300/borhane_ghatee_jelde_5.pdf.html (تعلیقات, Amir Kabir 5th pr. 1376, 293 pp). Same set behind login on ketabnak.com/book/55304-55307 and /58249.", "lookup_hint": "grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \\f; leaf N = N-th \\f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=dehkhoda, parsi.wiki, abadis.ir/fatofa/<word>/) quotes Borhan and often Mo'in's footnotes as (حاشیهٔ برهان قاطع چ معین). noorlib.ir/book/info/10294 is a 1-vol Nima 1380 Borhan without Mo'in's notes. | For pages in a scanned volume use: python3 tools/ref_page.py BQT:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)", "local_file": ["/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v1_pages.txt", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v2_pages.txt", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)", "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/BQT_v2.txt (raw)", "/home/sfmqrb/
```


## [2026-10-16T05:16:38.906Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT; cat 0339.vision.txt | head -5; for n in 552 558; do curl -sL -o /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/bqt-532-n$n.jpg \"https://archive.org/download/borhan-ghate-v1/page/n${n}_w1600.jpg\"; done; file /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/bqt-532-n*.jpg"
}
```


### [2026-10-16T05:16:42.188Z] TOOL RESULT

```
[BQT vol. 1, printed p. 339 (archive.org borhan-ghate-v1, leaf n559); read from image]
بیکم - بفتح اول و کاف تازی و سکون ثانی و میم، صفه و ایوانرا گویند. *
...
footnotes (Mo'in):
* بیک - ترکی beg، عثمانی bey، قرقیزی bî یا biy؛ عنوانی است که بشاهزادگان و نجباء داده میشد، امیر قبیله‌ای کوچک (در برابر خاقان یا خان که رئیس قبیله‌ای بزرگ بود) - رؤسای سپاه. «دائرة‌المعارف اسلام».
/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/bqt-532-n552.jpg: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, baseline, precision 8, 2479x3508, components 1
/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/bqt-532-n558.jpg: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, baseline, precision 8, 2479x3508, components 1
```


## [2026-10-16T05:16:45.061Z] TOOL CALL #47: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/bqt-532-n552.jpg"
}
```


### [2026-10-16T05:16:45.213Z] TOOL RESULT

```

```


## [2026-10-16T05:16:45.208Z] INPUT

[Image: original 2479x3508, displayed at 1413x2000. Multiply coordinates by 1.75 to map to original image.]


## [2026-10-16T05:16:47.511Z] TOOL CALL #48: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/bqt-532-n558.jpg"
}
```


### [2026-10-16T05:16:47.661Z] TOOL RESULT

```

```


## [2026-10-16T05:16:47.658Z] INPUT

[Image: original 2479x3508, displayed at 1413x2000. Multiply coordinates by 1.75 to map to original image.]


## [2026-10-16T05:16:59.120Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT; S=/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad; ls 0332* 0338* 2>/dev/null; cp $S/bqt-532-n552.jpg 0332.jpg; cp $S/bqt-532-n558.jpg 0338.jpg\ncat > 0332.vision.txt <<'EOF'\n[BQT vol. 1, printed p. 332 (archive.org borhan-ghate-v1, leaf n552); read from image]\nبید - بکسر اول و سکون ثانی ودال، نام درختی است مشهور و آنرا بعربی صفصاف خوانند ۲ - و نام دیوی بوده در مازندران که رستم او را کشت - و بمعنی «باشید» و «بوید» هم هست ۳ - و کرمکی را نیز گویند که کاغذ وجامهای پشمین‌را ضایع کند و تباه سازد ۴ - و بمعنی بیهوده و بی فایده و ناسودمند باشد ...\nfootnotes (Mo'in):\n۲ - بید Salix از تیرهٔ بیدها وجنس‌های بسیار دارد مانند بید سفید وبید زرد وبید معلق ... رك : فرهنگ روستایی ۲۶۰ : در گیلکی bid ، فریزنی vej ، یرنی vê ، نطنزی vî «ك. ۱ ص ۲۸۶» ، سمنانی viã ، سنگسری و سرخهٔ ولاسگردی vî ، شهمیرزادی bîd «ك. ۲ ص ۱۸۱» ، طبری fîk ، مازندرانی کنونی fek «واژه نامه ۵۲۱» ، پهلوی vêt ، اوستا vaêiti «اسفا ۱ : ۲ ص ۷۶».\nEOF\ncat > 0338.vision.txt <<'EOF'\n[BQT vol. 1, printed p. 338 (archive.org borhan-ghate-v1, leaf n558); read from image]\nبیشه - بر وزن ریشه جنگل و نیستانرا گویند و بعربی اجم خوانند ۲ - وسازی هم هست از نی که شبانان نوازند، و بعضی گویند سازیست شبیه بچنگ، و بعضی دیگر گویند شبیه است برباب.\nfootnotes (Mo'in):\n۲ - اوستا varəsha (جنگل) ، سانسکریت vrkshá (درخت) «اسفا ۱: ۲ ص ۸۸» ، پهلوی vishak «بندهش ۱۸۹» ، سغدی vîshâk «گوتیو ۱۱۸» ، طبری vesha ، مازندرانی کنونی vîsha «واژه نامه ۷۹۶» ، اورامانی wêshâ «ك. اورامان ۱۲۷».\nEOF\nls"
}
```


### [2026-10-16T05:18:59.618Z] TOOL RESULT

```
Command did not complete within its 120s timeout and was moved to the background (ID: bejbi48g0). Output is being written to: /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/tasks/bejbi48g0.output. You will be notified when it completes. To check interim output, use Read on that file path.
Session cwd remains /home/sfmqrb/git/rishe-private; directory changes made by the backgrounded command do not apply to subsequent commands.
```


## [2026-10-16T05:19:02.594Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT; /bin/ls -la 0332* 0338*; cat /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/tasks/bejbi48g0.output | head"
}
```


### [2026-10-16T05:19:03.239Z] TOOL RESULT

```
-rw-r--r-- 1 sfmqrb sfmqrb 495268 Oct 16 01:16 0332.jpg
-rw-r--r-- 1 sfmqrb sfmqrb   1160 Oct 16 01:16 0332.vision.txt
-rw-r--r-- 1 sfmqrb sfmqrb 502351 Oct 16 01:16 0338.jpg
-rw-r--r-- 1 sfmqrb sfmqrb    734 Oct 16 01:16 0338.vision.txt
(eval):1: no matches found: 0332*
```


## [2026-10-16T05:19:07.261Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT; date; cat 0332.vision.txt; cat 0338.vision.txt; /bin/ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/"
}
```


### [2026-10-16T05:19:07.626Z] TOOL RESULT

```
Fri Oct 16 01:19:07 AM EDT 2026
[BQT vol. 1, printed p. 332 (archive.org borhan-ghate-v1, leaf n552); read from image]
بید - بکسر اول و سکون ثانی ودال، نام درختی است مشهور و آنرا بعربی صفصاف خوانند ۲ - و نام دیوی بوده در مازندران که رستم او را کشت - و بمعنی «باشید» و «بوید» هم هست ۳ - و کرمکی را نیز گویند که کاغذ وجامهای پشمین‌را ضایع کند و تباه سازد ۴ - و بمعنی بیهوده و بی فایده و ناسودمند باشد ...
footnotes (Mo'in):
۲ - بید Salix از تیرهٔ بیدها وجنس‌های بسیار دارد مانند بید سفید وبید زرد وبید معلق ... رك : فرهنگ روستایی ۲۶۰ : در گیلکی bid ، فریزنی vej ، یرنی vê ، نطنزی vî «ك. ۱ ص ۲۸۶» ، سمنانی viã ، سنگسری و سرخهٔ ولاسگردی vî ، شهمیرزادی bîd «ك. ۲ ص ۱۸۱» ، طبری fîk ، مازندرانی کنونی fek «واژه نامه ۵۲۱» ، پهلوی vêt ، اوستا vaêiti «اسفا ۱ : ۲ ص ۷۶».
[BQT vol. 1, printed p. 338 (archive.org borhan-ghate-v1, leaf n558); read from image]
بیشه - بر وزن ریشه جنگل و نیستانرا گویند و بعربی اجم خوانند ۲ - وسازی هم هست از نی که شبانان نوازند، و بعضی گویند سازیست شبیه بچنگ، و بعضی دیگر گویند شبیه است برباب.
footnotes (Mo'in):
۲ - اوستا varəsha (جنگل) ، سانسکریت vrkshá (درخت) «اسفا ۱: ۲ ص ۸۸» ، پهلوی vishak «بندهش ۱۸۹» ، سغدی vîshâk «گوتیو ۱۱۸» ، طبری vesha ، مازندرانی کنونی vîsha «واژه نامه ۷۹۶» ، اورامانی wêshâ «ك. اورامان ۱۲۷».
total 9052
drwx------ 5 sfmqrb sfmqrb   1300 Oct 16 01:19 .
drwx------ 4 sfmqrb sfmqrb     80 Oct 16 01:12 ..
-rw-r--r-- 1 sfmqrb sfmqrb    440 Oct 16 01:13 agents.txt
-rw-r--r-- 1 sfmqrb sfmqrb 225677 Oct 16 01:15 bqt213-523-foot.png
-rw-r--r-- 1 sfmqrb sfmqrb  23700 Oct 16 01:15 bqt213-523-head.png
-rw-r--r-- 1 sfmqrb sfmqrb 519404 Oct 16 01:15 bqt213-523.jpg
-rw-r--r-- 1 sfmqrb sfmqrb 241141 Oct 16 01:15 bqt253-523-foot.png
-rw-r--r-- 1 sfmqrb sfmqrb    387 Oct 16 01:15 bqt253-523-head.png
-rw-r--r-- 1 sfmqrb sfmqrb 542982 Oct 16 01:15 bqt253-523.jpg
-rw-r--r-- 1 sfmqrb sfmqrb 228186 Oct 16 01:15 bqt522-n480.jpg
-rw-r--r-- 1 sfmqrb sfmqrb 218139 Oct 16 01:15 bqt522-n481.jpg
-rw-r--r-- 1 sfmqrb sfmqrb 219378 Oct 16 01:14 bqt522-n561.jpg
-rw-r--r-- 1 sfmqrb sfmqrb 221215 Oct 16 01:14 bqt522-n562.jpg
-rw-r--r-- 1 sfmqrb sfmqrb   2167 Oct 16 01:16 bqt526-380.txt
-rw-r--r-- 1 sfmqrb sfmqrb   3655 Oct 16 01:16 bqt526-381.txt
-rw-r--r-- 1 sfmqrb sfmqrb   2666 Oct 16 01:16 bqt526-382.txt
-rw-r--r-- 1 sfmqrb sfmqrb   3053 Oct 16 01:16 bqt526-383.txt
-rw-r--r-- 1 sfmqrb sfmqrb   2679 Oct 16 01:16 bqt526-384.txt
-rw-r--r-- 1 sfmqrb sfmqrb   3040 Oct 16 01:16 bqt526-385.txt
-rw-r--r-- 1 sfmqrb sfmqrb   2363 Oct 16 01:16 bqt526-386.txt
-rw-r--r-- 1 sfmqrb sfmqrb   3489 Oct 16 01:16 bqt526-387.txt
-rw-r--r-- 1 sfmqrb sfmqrb   2579 Oct 16 01:16 bqt526-388.txt
-rw-r--r-- 1 sfmqrb sfmqrb   2623 Oct 16 01:16 bqt526-389.txt
-rw-r--r-- 1 sfmqrb sfmqrb   2738 Oct 16 01:16 bqt526-390.txt
-rw-r--r-- 1 sfmqrb sfmqrb   3726 Oct 16 01:16 bqt526-391.txt
-rw-r--r-- 1 sfmqrb sfmqrb   2536 Oct 16 01:16 bqt526-392.txt
-rw-r--r-- 1 sfmqrb sfmqrb   2905 Oct 16 01:16 bqt526-393.txt
-rw-r--r-- 1 sfmqrb sfmqrb   2592 Oct 16 01:16 bqt526-394.txt
-rw-r--r-- 1 sfmqrb sfmqrb   2900 Oct 16 01:16 bqt526-395.txt
-rw-r--r-- 1 sfmqrb sfmqrb   2996 Oct 16 01:16 bqt526-396.txt
-rw-r--r-- 1 sfmqrb sfmqrb 265885 Oct 16 01:17 bqt526-n388-bot.png
-rw-r--r-- 1 sfmqrb sfmqrb 529778 Oct 16 01:17 bqt526-n388.jpg
-rw-r--r-- 1 sfmqrb sfmqrb 268616 Oct 16 01:17 bqt526-n388-top.png
-rw-r--r-- 1 sfmqrb sfmqrb 242385 Oct 16 01:18 bqt526-n425-bot.png
-rw-r--r-- 1 sfmqrb sfmqrb 532793 Oct 16 01:18 bqt526-n425.jpg
-rw-r--r-- 1 sfmqrb sfmqrb 283219 Oct 16 01:18 bqt526-n425-top.png
-rw-r--r-- 1 sfmqrb sfmqrb 217965 Oct 16 01:18 bqt526-n426-bot.png
-rw-r--r-- 1 sfmqrb sfmqrb 504059 Oct 16 01:18 bqt526-n426.jpg
-rw-r--r-- 1 sfmqrb sfmqrb 275048 Oct 16 01:18 bqt526-n426-top.png
-rw-r--r-- 1 sfmqrb sfmqrb 232098 Oct 16 01:17 bqt526-n427-bot.png
-rw-r--r-- 1 sfmqrb sfmqrb 541375 Oct 16 01:17 bqt526-n427.jpg
-rw-r--r-- 1 sfmqrb sfmqrb 293028 Oct 16 01:17 bqt526-n427-top.png
-rw-r--r-- 1 sfmqrb sfmqrb 236525 Oct 16 01:17 bqt526-n428-bot.png
-rw-r--r-- 1 sfmqrb sfmqrb 535615 Oct 16 01:17 bqt526-n428.jpg
-rw-r--r-- 1 sfmqrb sfmqrb 289288 Oct 16 01:17 bqt526-n428-top.png
-rw-r--r-- 1 sfmqrb sfmqrb   3536 Oct 16 01:16 bqt-530-494.txt
-rw-r--r-- 1 sfmqrb sfmqrb   2849 Oct 16 01:16 bqt-530-495.txt
-rw-r--r-- 1 sfmqrb sfmqrb   2683 Oct 16 01:16 bqt-530-496.txt
-rw-r--r-- 1 sfmqrb sfmqrb   3123 Oct 16 01:16 bqt-530-497.txt
-rw-r--r-- 1 sfmqrb sfmqrb 495268 Oct 16 01:16 bqt-532-n552.jpg
-rw-r--r-- 1 sfmqrb sfmqrb 502351 Oct 16 01:16 bqt-532-n558.jpg
-rw-r--r-- 1 sfmqrb sfmqrb  21671 Oct 16 01:18 bqt-538.txt
-rw-r--r-- 1 sfmqrb sfmqrb  28733 Oct 16 01:19 build-523.py
-rw-r--r-- 1 sfmqrb sfmqrb  25490 Oct 16 01:18 build-524.py
-rw-r--r-- 1 sfmqrb sfmqrb  21531 Oct 16 01:18 build-525.py
-rw-r--r-- 1 sfmqrb sfmqrb  23688 Oct 16 01:18 build-536.py
drwxr-xr-x 2 sfmqrb sfmqrb     60 Oct 16 01:13 p524
drwxr-xr-x 2 sfmqrb sfmqrb     60 Oct 16 01:14 p528
drwxr-xr-x 2 sfmqrb sfmqrb    120 Oct 16 01:18 p533
-rw-r--r-- 1 sfmqrb sfmqrb  72215 Oct 16 01:17 pg520.png
-rw-r--r-- 1 sfmqrb sfmqrb  48975 Oct 16 01:16 pg521.png
-rw-r--r-- 1 sfmqrb sfmqrb  48394 Oct 16 01:13 pg522.png
-rw-r--r-- 1 sfmqrb sfmqrb  54622 Oct 16 01:15 pg523.png
-rw-r--r-- 1 sfmqrb sfmqrb  62716 Oct 16 01:16 pg535.jpg
-rw-r--r-- 1 sfmqrb sfmqrb   3426 Oct 16 01:14 urls-526.txt
```


## [2026-10-16T05:19:09.669Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; /bin/ls -la site/pages/532.jpg"
}
```


### [2026-10-16T05:19:09.996Z] TOOL RESULT

```
-rw-r--r-- 1 sfmqrb sfmqrb 55866 Oct 14 22:15 site/pages/532.jpg
```


## [2026-10-16T05:19:11.241Z] TOOL CALL #53: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/site/pages/532.jpg"
}
```


### [2026-10-16T05:19:11.276Z] TOOL RESULT

```

```


## [2026-10-16T05:19:20.473Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for w in vow vote devote wire iris; do echo \"== KLN $w\"; grep -n -m2 -E \"^$w,? \" KLN_1966.txt | cut -c1-400; done; for w in VOW VOTE WIRE IRIS; do echo \"== SKT $w\"; grep -n -m1 -E \"^$w,\" SKT.txt | cut -c1-400; done"
}
```


### [2026-10-16T05:19:20.873Z] TOOL RESULT

```
== KLN vow
== KLN vote
== KLN devote
11169:devote,  tr.  v.  —  L.  devours,  pp.  of  devovere,  ‘to vow,  to  devote  (to  a  deity),  to  sacrifice  oneself, to  promise  solemnly",  fr.  de-  and  vovere,  ‘to vow'.  See  vote,  vow  and  cp.  devont. Derivatives:  devot-ed,  adj.,  devoted-ly,  adv., devoted-ness,  n.,  devot-ee,  devole-ment,  n., devot-er,  n.,  devotion  (q.v.) devotion,  n.  —  OF.  (F.  devotion),  fr.  L. 
== KLN wire
== KLN iris
19892:iris,  n.,  1)  the  rainbow;  2)  the  colored  portion  of the  eye.  —  L.  iris,  fr.  Gk.  Ipie,  ‘the  rainbow’, orig.  form  *fTpt?,  lit.  ‘something  bent  or  curved’, fr.  I.-E.  base  *wei-,  ‘to  bend,  twist’,  whence  also Gk.  Ixuc,,  Aeol.  ‘the  edge  or  rim  of  any¬
== SKT VOW
21062:VOW,  sb.  (F.-L.)    M- E.  cvw.  VM. —
== SKT VOTE
== SKT WIRE
== SKT IRIS
```


## [2026-10-16T05:19:23.444Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -m3 -E \"(^| )(vow|vote|wire), +(n|v|tr)\" KLN_1966.txt | cut -c1-500; grep -n -m3 -E \"Avest. aojaiti|aojaiti\" KLN_1966.txt | cut -c1-300; sed -n 21062,21066p SKT.txt | cut -c1-300; grep -n -m2 -E \"^WIRE|^IRIS|^VOTE\" SKT.txt | cut -c1-300"
}
```


### [2026-10-16T05:19:23.868Z] TOOL RESULT

```
11169:devote,  tr.  v.  —  L.  devours,  pp.  of  devovere,  ‘to vow,  to  devote  (to  a  deity),  to  sacrifice  oneself, to  promise  solemnly",  fr.  de-  and  vovere,  ‘to vow'.  See  vote,  vow  and  cp.  devont. Derivatives:  devot-ed,  adj.,  devoted-ly,  adv., devoted-ness,  n.,  devot-ee,  devole-ment,  n., devot-er,  n.,  devotion  (q.v.) devotion,  n.  —  OF.  (F.  devotion),  fr.  L.  devolio- nem,  ace.  of  devotio,  ‘a  devoting,  consecrating; devotion’,  fr.  devotus,  pp.  of 
VOW,  sb.  (F.-L.)    M- E.  cvw.  VM. —
0.  F.  xH>u,  V0  (F.  fieu),  a  vow.  — L,  uafHM,
a  vow  (aboveV     ^  H«ice  the  M.  E.  ottfw,
sb  ,  common  in  the  sense  of  '  vow/  Chancer.
C.  T.  aJ39.  1416  ;  and  hence  the  verb  tffWfv,
```


## [2026-10-16T05:19:26.715Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -m4 -E \"vovere,? ?.{0,40}(vow|pledge)\" KLN_1966.txt | cut -c1-600; grep -n -m3 -E \"OE\\. wir|O\\.?E\\. w[iī]r,\" KLN_1966.txt | cut -c1-400; grep -n -m3 -E \"vaeiti|vaēiti|Avest\\. va\" KLN_1966.txt | grep -i -E \"willow|vaeit\" | cut -c1-300"
}
```


### [2026-10-16T05:19:27.056Z] TOOL RESULT

```
11169:devote,  tr.  v.  —  L.  devours,  pp.  of  devovere,  ‘to vow,  to  devote  (to  a  deity),  to  sacrifice  oneself, to  promise  solemnly",  fr.  de-  and  vovere,  ‘to vow'.  See  vote,  vow  and  cp.  devont. Derivatives:  devot-ed,  adj.,  devoted-ly,  adv., devoted-ness,  n.,  devot-ee,  devole-ment,  n., devot-er,  n.,  devotion  (q.v.) devotion,  n.  —  OF.  (F.  devotion),  fr.  L.  devolio- nem,  ace.  of  devotio,  ‘a  devoting,  consecrating; devotion’,  fr.  devotus,  pp.  of  devovere.  See  de¬ vote  and  -ion.
11171:devout,  adj.  —  ME.  devot,  devout,  fr.  OF.  devot (fern,  devote),  fr.  L.  devotus,  pp.  of  devovere,  ‘to vow,  devote’.  See  devote.
13769:Euchite,  n.,  one  of  a  medieval  sect  that  flourished in  the  4th  cent.,  whose  members  believed  in  the saving  power  of  perpetual  prayer;  applied  also to  various  other  sects  that  shared  this  belief.  — Eccles.  L.  euchita,  fr.  Gk.  eu/-/;,  ‘vow,  wish, prayer’,  which  is  cogn.  with  OI.  vaghdt-,  ‘one who  Offers  a  sacrifice’,  L.  vovere,  ‘to  vow’.  See vote  and  cp.  next  word.
```


## [2026-10-16T05:19:29.850Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E \"^(vote|vow|wire|withe|withy)[,.]\" KLN_1966.txt | head; grep -n -E \"Avest\\. aog|aojaiti|aogedha|aoxta\" KLN_1966.txt | cut -c1-500 | head -3"
}
```


### [2026-10-16T05:19:30.324Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-10-16T05:19:32.581Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -o -E \".{0,10}(vote|wire|withe),  (n|v|tr)\\..{0,600}\" KLN_1966.txt | head -5; grep -n -o -E \".{0,200}(aog|aoj)-.{0,200}\" KLN_1966.txt | head -3"
}
```


### [2026-10-16T05:19:36.726Z] TOOL RESULT

```
11169:devote,  tr.  v.  —  L.  devours,  pp.  of  devovere,  ‘to vow,  to  devote  (to  a  deity),  to  sacrifice  oneself, to  promise  solemnly",  fr.  de-  and  vovere,  ‘to vow'.  See  vote,  vow  and  cp.  devont. Derivatives:  devot-ed,  adj.,  devoted-ly,  adv., devoted-ness,  n.,  devot-ee,  devole-ment,  n., devot-er,  n.,  devotion  (q.v.) devotion,  n.  —  OF.  (F.  devotion),  fr.  L.  devolio- nem,  ace.  of  devotio,  ‘a  devoting,  consecrating; devotion’,  fr.  devotus,  pp.  of  devovere.  See  de¬ vote  and  -ion.
ugrep: error: error at position 88
80-\xbf][\x80-\xbf]*){0,200}
                            \___exceeds complexity limits
```


## [2026-10-16T05:19:39.108Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; tail -c 400 KLN_1966.txt; echo; grep -n -E \"^(vote|vow|wire),\" KLN_1971.txt | head; grep -n -E \"aojaiti|aoxta\" KLN_1971.txt | cut -c1-500 | head -3"
}
```


### [2026-10-16T05:19:39.425Z] TOOL RESULT

```
e  (resp.  -in), veratrine,  n.,  also  veratrin,  veratrina,  veratria,  a poisonous  mixture  of  alkaloids  obtained  from sabadilla  seeds,  used  in  medicine  in  the  treat¬ ment  of  rheumatism,  neuralgia,  etc.  —  F.  vera¬ trine,  fr.  ModL.  veratrina,  fr.  L.  verdtrum,  ‘helle¬ bore’,  fr.  verare ,  ‘to  tell  the  truth’,  fr.  verus, ‘true’;  so  called  because
69781:vow, to devote (to a deity), to sacrifice oneself, 
69805:vow, devote’. See devote. 
96918:vote, — ME., fr. OF. franchise, ‘freedom’, fr. 
236275:vote, assent, support’, prop, ‘shout of approv- 
263998:vote, n. — ME., fr. L. votum (for *vovetom ), ‘a 
264032:vow, n. — ME. vou , vowe, vow , fr. OF. vou, vowe 
264035:vow, tr. and intr. v. — MF. vouer, vower , fr. OF., 
267547:wire, n. — ME. wyre, wir, fr. OE. wir, rel. to ON. 
133885:L. Laocoon , fr. Gk. Aaoxtaiv, compounded of
```


## [2026-10-16T05:19:40.869Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 263998,264012p KLN_1971.txt; echo ...; sed -n 267547,267560p KLN_1971.txt"
}
```


### [2026-10-16T05:19:41.229Z] TOOL RESULT

```
vote, n. — ME., fr. L. votum (for *vovetom ), ‘a 
vow’, prop. neut. pp. of vovere , ‘to vow’, used 
as a noun; rel. to Umbr. vufru , ‘pertaining to a 
vow’, and cogn. with OI. vaghdt-, ‘one who 
offers a sacrifice’, Avestic aog s da, ‘he said’. Arm. 
gog, ‘say ’ Gk. enyv), ‘vow, wish’, etixop-ou, ‘I 
pray’, perh. also with OE. wdgian , ‘to woo’. 
Cp. vow, avow, devote, devout. Cp. also Euchite, 
euchology. Cp. also woo. 

Derivatives: vote , intr. and tr. v., vot-er , n., 
vote-less , adj., vot-ing , n., votive (q.v.) 
votive, adj., dedicated or given in fulfillment of a 
vow. — L. votivus, ‘pertaining to a vow, given 
in the consequence of a vow’, fr. votum. See 
...
wire, n. — ME. wyre, wir, fr. OE. wir, rel. to ON. 
* virr in viravirki, ‘filigree work’, Swed. vira, ‘to 
twist’, OHG. wiara , ‘fine gold work’, and cogn. 
with Olr. fiar, W. gwyr, ‘bent, crooked’, fr. I.-E. 
base *wei-, ‘to bend, twist’, whence also L. viere , 
‘to bend, twist’. See withy. Cp. L. viriae , ‘arm- 
let, bracelet’, which is a Celtic loan word and 
ult. derives fr. I.-E. base *wei-. Cp. also ferrule. 
Derivatives: wire , tr. and intr. v., wir-ed, adj., 
wire-less , adj. and n., wir-er, n., wir -ring, n., 
wir-y, adj., wir-i-ly, adv., wir -i- ness, n. 
wis, tr. v., to know (archaic). — Back formation 
fr. ME. i-wis, ‘certainly’, misinterpreted as / wis 
(= / wist, I wit), ‘I know’. For the etymology of
```


## [2026-10-16T05:19:43.575Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; n=$(grep -n -m1 -E \"^withy,\" KLN_1971.txt | cut -d: -f1); sed -n \"${n},$((n+12))p\" KLN_1971.txt"
}
```


## [2026-10-16T05:19:44.912Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i -E \"^ *1[3-9]\\.[0-9]+ .*(SPEAK|SAY)|ANSWER\" SYN.txt | head; grep -n -i -E \"WILLOW|FOREST|WIRE\" SYN.txt | head"
}
```


### [2026-10-16T05:19:45.372Z] TOOL RESULT

```
withy, which is cogn. with L. viere, ‘to bend, 
twist’. 

Derivatives: willow, tr. v., willo w-y, adj. 
willy-nilly, adv. — Contraction of will I, nilll, or 
will he, nlll he, or will ye, niU ye. See will, v., and 
nill. 

wilt, v. — 2nd pers. sing, of will, 
wilt, intr. v., to fade, wither; tr. v., to cause to 
fade. — Prob. alter, of wilk , a dial. var. of welk 
(q.v.)
```


### [2026-10-16T05:19:45.504Z] TOOL RESULT

```
72:The history of ideas is embodied in the history of the words used to ex- press them. Whether the ‘idea’, ‘notion’, ‘concept’, or ‘mental image’ (I shall commonly use the innocuous ‘notion’) is, as many believe, only an abstraction (the concrete object or the uttered and heard sound of the word being the only realities), or whether it corresponds to some reality in the brain (as an eminent neurologist has assured me he thinks quite tenable), need not concern us. For its close dependence upon its verbal ex- pression is beyond dispute. It is a pattern of reaction answering to a given stimulus, which (apart from the actual perception of an individual concrete object, which also suggests the general notion) is normally the word or group of words. It is this pattern of reaction which constitutes the mean- ing of a word. A word means what it refers to, in a given context or situa- tion. The meaning of a word as a whole may ne a composite of various allied applications.
109:Words not only change in meaning, they may be lost outright, displaced by others. Why? There is no one answer. Of the various alleged causes, each has some validity as a factor but is likely to be exaggerated by one whose attention is riveted on it in a hunt for examples. The existence of homonyms may favor the loss of one of them, as the verb let ‘hinder’ (cf. the noun in the old phrase let or hindrance and let in tennis) vs. let ‘permit’. Phonetic changes which have left little body to the word no doubt favored the partial displacement of Lat. dare, diés, apis, avis by donare, diurnum, apicula, avicellus in the evolution of the Romance words. But the great number of homonyms in English, and monosyllabic at that, shows that neither of these factors is a compelling cause.
129:The principal Indo-European languages are covered. Some of the minor Indo-European languages, as Albanian, Armenian, and all modern forms of Indie and Iranian, are excluded from the survey, except for incidental men- tion, since to include them systematically would increase the labor out of all proportion to the results added. Danish, with which Norwegian agrees in large measure, and Swedish are taken as representative of the modern Scandinavian languages, though thus one may miss certain interesting divergences in word preference between Danish and Norwegian and the more frequent persistence of the Old Norse words in Modern Icelandic. Of the Romance languages, Portuguese is omitted as generally going with Span- ish in vocabulary, though here, too, occasional differences are missed or only incidentally noted. There is no room to follow out the chronological and geographical distribution of Romance words on the elaborate scale which is customary and fitting in monographs in that field. Of the impor- tant Slavic languages, the (modern) Bulgarian is omitted, the words general- ly going with those quoted under either Church Slavic or Serbo-Croatian. Under Church Slavie are given preference the genuine Old Church Slavic (Old Bulgarian) words, especially from the Gospels, where such are quotable, but not to the exclusion of others which are (in part accidentally) quotable only from later times. The latter are sometimes marked “late”, but prob- ably without consistency. As is well known, Miklosich’s Lexicon is full of late forms that are merely Serbian, etc. in Church Slavic dress, and con- versely fails sometimes to give early quotations for words occurring in the best records. In this regard, Jagié’s Entstehungsgeschichte der kirchen- slavischen Sprache, with its indexes, is of inestimable value, though even this at times fails to answer the questions that arise. Since the quotable Old Irish vocabulary is too limited to serve, Old and Middle Irish forms are generally given without distinction and both marked as Ir. (as in Peder- sen’s Vergleichende Grammatik der keltischen Sprachen and elsewhere), while the modern forms are marked NIr. But under Welsh and Breton are given the modern forms, with special designation of the Old or Middle. Cornish words, which generally go with the Breton or Welsh or both, are not included in the list but often in the discussion, especially those quotable from the old Latin-Cornish vocabulary.
179:Craigie, while in Chicago, was always generous in opening his store of knowl- edge of the Old Norse and English vocabulary. For the Romance languages I have pestered with queries virtually all my colleagues, past and present, in that field—Altrocchi, Borgese, Bullock, Castillo, David, Jenkins, Kenis- ton, Korominas, Merrill, Norman, Parmenter, Rowland, Trevifio, Vigneron, and Wartburg; also Professor Siever (a Rumanian, formerly a graduate stu- dent in our Romance department) for Rumanian. For Sanskrit, Professor Clark (in the first chapter) and later Professor Bobrinskoy have assisted. Father J. G. O’Neil, now of Maynooth College, Ireland, formerly a graduate student here in the Department of Classics, originally supplied the Modern Trish words, which were further revised by his colleague Professor O’Nolan; and through Father O’Neil’s interest in the matter arrangements were made for the listing of the Old Irish words by Miss E. Knott under the supervision of her teacher, Professor O. Bergin. These Irish lists have been of great serv- ice in a difficult field, but it is only fair to say that (partly owing to changes or refinements in the headings themselves) many changes have been made and that much of the critical work on Irish, as for Celtic in general, has been done by Professor G. 8. Lane. Professors T. P. Cross and Myles Dillon have also been consulted on some questions of Irish usage. For Slavic, beside other informants, my past or present colleagues, Bobrinskoy, Nykl, Spinka, and Gelb, have been consulted for Russian, Bohemian, and Polish respec- tively. Professor Senn has answered many special inquiries on Lithuanian, often giving the precise history of neologisms in more detail than could be repeated here. That I have also, on occasion, consulted my colleagues in the departments of Greek, Latin, and the Germanic languages goes with- out saying.
1955:The present differentiation of NE mist, fog, and haze cannot be matched in the other languages, where with some eX- ceptions the same word answers roughly to all three. Many of the words are cop- nate with some of those for ‘cloud’. Others are from such diverse notions as ‘vapor’, ‘dim’, ‘gray’, ‘wet’, ‘winter’, etc.
9799:Again, ‘be ome ‘be clothed in, cloths pay garment a ad npn ! > wertan, NE wear, 9s re ached in’ and answer- a ie use elsewhere of ves Pi 1D : . Q © hoa! ag NHG kleider tragen, #r. porter earn NG gop& potxa.
11524:‘House’ is understood here as ‘dwell- ing house’, There is overlapping, on the one hand, with ‘building’ in general, on the other, with ‘dwelling’, ‘home’. The former notion is more dominant ety- mologically, the majority of the words reflecting the notion of ‘build’, ‘cover’, or some other feature of the construction. But some come from ‘remain, rest, stand, dwell’, etc. Regardless of their etymology, words for ‘house’ may also be used for ‘building’, but still more gen- erally for ‘home’ and for ‘household, family’. They commonly supply the phrases answering to NE at home, as Gr. otxo:, NGr. o76 ovirt, It. a casa, Fr. chez moi, etc. (chez fr. Lat. casa), NHG zu hause, Lith. namie, Russ. doma, etc. Hence the common dictionary definition ‘house, home’ for most of the words list- ed here. But they do not correspond to NE home in its widest sense. Cf. below 7.122. Words for ‘dwelling’, derived from the verbs for ‘dwell’ (7.11), though they cover ‘dwelling house’, like Lat. habitatio, Rum. locuinjé, NHG wohnung, NE dwelling, Skt. vegman-, etc. are not included in the list, unless they are the common words for ‘house’, as Grk. ofxos.
14231:Fr, briser, fr. a Gallic form answering to Ir. brissim ‘break? (below, 3). REW ey : Gamillscheg 150, Wartburg
22892:{inctive opposite of straight. But many of the words listed as such opposites are terms that answer to both crooked and nmed, that is, they are used without differentiation (except in technical lan- guage) as to whether the deflection 1s in the form of a curve or one or more sharp angles. They are derived from a variety
23622:Besides the words listed, there are others that answer more nearly to NE suficient (fr. pres. pple. of Lat. sufficere ‘nut into, make take the place of’, and soalso ‘suffice’), which with reference to quantity or number is only a less collo- qual equivalent of enough but which carries the notion of ‘adequate’ and is wed in many phrases where enough could not be substituted.
678:River; Stream; Broox Sprive; WELL Woops, Forest TREE
961:The association between a (bare, rugged) ‘mountain’ and ‘rock’ shows it- self in the frequent relationship between words for ‘mountain’ and ‘rock, stone’ (1.44) in which now one, now the other, meaning is the earlier. Again, associa- tion between the (wooded) ‘mountain’ and ‘woods, forest’ (1.41) shows itself in a similar relationship, a word for ‘moun- tain’ coming to mean ‘woods’ or some- times conversely.
1002:6. ChSl. gora, etc., general Slavic for ‘mountain’ (in some regions ‘forest’, as always Lith. gire, 1.41) : Skt. giri-, Av. gairi- ‘mountain’, and prob. Alb. gur ‘stone’. Walde-P. 1.682. Berneker 329. Further connection with Skt. guru-, Grk. Bapis ‘heavy’, through the notion of ‘heavy, solid mass’ (Thumb, IF 9.299) is plausible. Cf. Skt. acala- ‘mountain’ fr. adj. acala- ‘immovable’.
1007:Bulg. planina ‘mountain’ (the usual word, gora being ‘forest’), SCr. planina
1487:141 WOODS, FOREST
1491:It. selva, bosco, foresta Sw. — skog SCr. Suma
1493:Sp. selva, bosque, monte ME __ wode, forest Pol. las
1494:Rum. pddure NE woods, forest Russ. les
1497:The difference between NE woods, the more generic and popular term, and forest, applied only to the larger tracts, will be ignored here. To avoid am- biguity, ‘woods’ (not ‘wood’ as ina wood) will be used in this sense, and ‘wood’ only in the sense of material.
1504:MLat. boscus (>It. bosco, Fr. bois, Sp. bosque) was used esp., like Lat. saltus, for ‘woodland pasture’ (cf. unusquisque liber homo agistet boscum suum in foresta ‘every free man may let out his pasture
```


## [2026-10-16T05:19:47.897Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 1487,1540p SYN.txt | grep -n -i -E \"Av\\.|varə|vares|NPers|willow\" | cut -c1-500; grep -n -E \"PRAY|VOW|SPEAK, TALK|^ *18\\.21|18\\.22\" SYN.txt | head"
}
```


### [2026-10-16T05:19:48.217Z] TOOL RESULT

```
9:i. caill, fid, fidbad, ross Du. woud Skt. _ vana-, aranya-, atavi- Nir. coil OHG  wald, holz Av. razura-~
45:7. Skt. vana- ‘woods, tree, wood’, Av. vana- ‘tree’, etym.? Walde-P. 1.259.
48:Av. razura- ‘woods’ and ‘pit to catch animals’: Av. razah-, Skt. rahas- ‘re- moteness, loneliness’. The development assumed by Barth:, s.v., namely ‘woods’ from the trees used to cover the pit, is less likely than ‘woods’ from ‘remote- ness’, as in Skt. aranya-.
49:142 TREE Grk.  dé5pov Goth. bagms Lith. medis NG ba Spov ON tré, badmr (poet.) Lett. kuoks Lat. arbor Dan. ire t ChSl. drévo, dqbit It. albero Sw. irdd SCr.  drvo Fr. arbre OE tréow, béam Boh. strom Sp. Grbol ME ttre Pol. drzewo Rum. —arbore, copac NE tree Russ. derevo Ir. crann, fid Du. boom Skt. urkga-, vana-, dru- NIr.  crann OHG boum ma-, etc. W. coeden, pren MHG boum Av. vand- (varasa-?) Br. gwezenn NHG baum
15982:(18.22). Hence ‘subject matter’ and further generalization. Brickner 475.
16098:atk ee Meringer, IF 18.220. tajaga a aba, fr. vb. vajadzét, this fr. Recesgn : pet in vajaga (ir) ‘is
23187:racuus ‘empty’ (18.22). Cf. Sp. hueco
23334:2. Lat. signum (> Romance words), generally taken as orig. ‘cut mark’ fr. the root of secare ‘cut’ (so Walde-P. 2.478, Ernout-M. 939), but much more probably fr. the root of in-seque ‘say’ In its earlier sense of ‘point out’ (18.22).
29371:Lett. pateikSana, fr. pateikti ‘say, re- late’ and esp. ‘thank’, cpd. of teikt ‘say’ (18.22). Mithl.-Endz. 3.120, 4.156 f.
29949:Russ. poricanie, fr. poricat’ ‘blame, reprove’, cf. otrekat', otricat’ ‘deny’ : ChSl. rekq, resti, ORuss. rku, reci ‘say’ (18.22), ChSl. réé% ‘accusation’, etc. Miklosich 274 f.
29978:Lett. teikSana, fr. teikt ‘say’ (18.22) and ‘praise’. Miuhl.-~Endz. 4.156 f.
31429:SING A Spout, CRY OuT 18.14 VaRrrous CRIES 18,21 SPEAK, TALK 18.22 Say 18,23 Be SILENT 18.24 LANGUAGE 18.25 DIALECT 18,26 WorD 18.27 DicTIONARY 18.28 NAME 18.31 Asx! (Question, Inquire) 18.32 ANSWER (vb.) 18.33 ApMiT, CONFESS 18.34 Deny 18.35 Asx?, REQUEST 18.36 Promise (vb.) 18.37 RerusE 18.38 Forbip
31487:‘sing a song’). Semantic development through ‘take up’ the song = ‘begin to sing’. Cf. the parallel development of ‘bring forth’ to ‘say’ in Ir. asbiur (18.22), NE utter, and Skt. epds. of hy- ‘bring’ (ud-G-, vy-d-).
31563:vyocAL UTTERANCE, SPEECH; READING AND WRITING 1253 18.21 SPEAK, TALK Grk. deve (aor. enor, fut. Goth. rddjan, mapljan Lith. kalbéti ; toa, etc.), ayopebw, ON mala, reéa, tala Lett. rundat Nard Dan. tale, snakke ChSl. glagolati, vétali
```


## [2026-10-16T05:19:49.957Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 31563,31700p SYN.txt | grep -n -i -E \"aog|Av\\.|NPers|pasux|pasox\" | cut -c1-500 | head"
}
```


### [2026-10-16T05:19:50.263Z] TOOL RESULT

```
2:NG BArd < Sw. tala, sprdka SCr.  govoriti ot. logue, fart OE  sprecan, m@lan,map- Boh.  mluwviti i,  parlare lan Pol.  méwié Tr. parler ME _ speke, mele, talk(i)e, Russ. govorit’ Sp. hablar, tal(i)e Skt.  vac-, bri-, vad-, bhas- Rum. vorbi, grat, cuvinta NE speak, talk Av. vat-, mri-, aoj- Ir. labrur, radim Du. spreken, praten
16:Skt. vac-, Av. vaé- ‘speak, say’; Grk. aor. drov, ela ‘spoke, said’ (NG elra mostly ‘said’) by dissim. fr. *é-e-vrov = Skt. aor. avocam. Cf. Skt. vacas-, Av. vatah-, Grk. ros (féros) ‘word’, Skt. vac-, Lat. véz, etc., ‘voice’ (18.11), Lat. vocare ‘call’, OPruss. wackis ‘cry’, etc.
24:Grk. fut. é&, perf. etpnxa, aor. pass. éppnOnv (pres. etpw Hom., but not com- mon), common in Hom. and later supple- menting déyw in both senses, beside de- rivs. sy7wp ‘public speaker’, piua ‘word, saying’, py7pa ‘agreement, covenant’, fr. Fep-, Fen- (cf. Arg. refpnuévos, El. cparpa, etc.), IE *wer- seen elsewhere in derivs. as Lat. verbum, OE word, etc. ‘word’, Av. urvata- ‘command’, Skt. vrata- ‘com- mand, vow’, etc. Walde-P. 1.283 f. Ernout-M. 1088f. Here also Hitt. weriya- ‘call, summon’
64:Boh. mluviti, Pol. méwié = Russ molvit’ ‘ater’, ChSl. mliiviti ‘make a dis. turbance’, beside sbs. Boh. mluva ‘speech’, etc., ChSl. mltiva ‘tumult? prob. : Skt. bra-, Av. mra- ‘speak, say’, but disputed (see below, 8).
66:8. Skt. vac-, Av. vaé-, above, 1.
67:Skt. bra-, Av. mra-, disputed whether fr. IE *mreu- with dub. connections or fr. *mleu- and connected with ChSI. mliva ‘tumult’, Boh. mluviti ‘speak’, etc. (above, 7). Walde-P. 2.313.
70:Av. aoj-, esp. 3sg. pret. mid. aozta (Gath. aogada) ‘spoke, said’ (esp. in a formal, solemn sense) : Skt. wh- ‘ob- serve, regard, consider’, Grk. ebxouae ‘pray, vow, boast’, Lat. vovére ‘vow’, etc. Walde-P. 1.110. Barth. 37f. Ernout- M. 1135.
114:‘know’, ete. (17.17). Cf. Skt. vedaya (caus.) ‘tell’, Ir. ad-fiadat ‘they tell’, ; SCr. kazati, Russ. s-kazaj’ = Chs] kazati ‘show’ (15.55), Boh. kdzati, Po} kazaé ‘preach’. Berneker 497, Boh. praviti (Pol. prawié ‘talk, prate’ = Ch8&l. praviti ‘set right, direct, guide’ deriv. of pravit ‘straight? (12.73). Spe. cialization to speech West-Slavic. 8. Skt. and Av. words, see 18.21. OPers. @ah- regular verb for ‘say? (e.g. Odtiy Darayavaus ‘saith Darius’, cistiy Bastanaiy pariy Gaumdtam ‘say an
122:Ir. ar-tuaissi, toaim Du. zwijgen Skt. tuignim bhi- Nir. taim im’thost OHG  swigén, dagén Av. (tuSni- ‘silently’) W. lewi MHG $swigen
131:whence MI. toaim ‘be silent’, », tost ‘silence’ (in phrase NIr. tdim im at jit, ‘I am in my silence’, cf. MIr. boi C uchulaind ina thost ‘C. was silent’, Windisch 842), W. tewi, Br. tevel (derivs. of sbs. W. tau, Br. tao ‘silence’) ; Skt. jagnim adv. ‘silently, in silence’, with phii- ‘be OF become silent’ (vb. tus- ‘be- come calm, be satisfied, etc.’), Av. tusni- in tugni-Sad ‘sitting silently’, etc.; OPruss. ‘er schweige’, tusnan
```


## [2026-10-16T05:19:54.192Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E \"^(e?u̯?egʷh|eugh|euguh|ueguh|wegwh|ewegwh)\" IEC.txt | head; grep -n -m5 -E \"vovē|voveo|vovere\" IEC.txt | cut -c1-300; grep -n -m5 -E \"vaēiti|vaeiti|wīra|wira\" IEC.txt | cut -c1-300"
}
```


### [2026-10-16T05:19:54.552Z] TOOL RESULT

```
3755:eugh- (ügh-) (rage, curse, swear, vow, im- precate'. WP I, 110 Skt. cf. ühami 'expiate'; ogháh, augháh "eur. ge’; Av. uz- ('eulogize'. w. prepalatalisation); Myc. cf. euketoi ‘he praises’; Gk. eükhomai *vow, beseech, promise, exult, boast'; eükhos ‘vow, offering’; ON cf. ýgjast, refl. ‘go mad, rage’. (Arm. ogem ‘utter’ isambig. Cf. SEM: A & IE: $ 56: IE eu-: Arm. o-, but cf. *sogheið: OHG sagén)
5340:guoueió ‘vow, declare’ Gk. cf. bou-lë (if for *guou-lēų ‘taking of re- solution’, cf. léu-) Lat. voveo; Li. gaviü, eti (‘fasť, lit. vow"); Latv. gaveju, et, id.
19677:refd. to aeiro) (?); OCS cf. véverica, f. (“squir- rel, weasel, stoat’ etc.) beside Li. vovere, f., voveris, f. ('squirrel', but cf. uiuera); OLi. vaivaras, m. ((squirrel', vocalism obscure); Latv. vaivari, mpl. ‘marsh rosemary’ beside vaveraji, id.; Li. vaivara, f. 'speedwell"; Latv. vāvere, 
19792:(uåueriə, see uluerà. Thus in Li. vovere, f. ‘squirrel’; Latv vāvere, f. id.)
20450:uluerá, is ‘squirrel’. Cf. ultio. WP I, 264, 287 Lat. (Pliny) viverra, f. (‘ferret or sim.); Ir. cf. fear-óg, Gael, feor-ág 'squirre; W gwiwer, pl. -od, m. id:; Br. gwinver, pl. -ed, m. id.; beside gwiber, id.; OE cf. àc-weorna, wm. id.; Cz. dim. vever-ka, id.; Pol. wiewiórka, id.; Li. cf. (va
20379:uiruos, is, io ‘twist, twine, gut, string, spiral. Cf. uir- (2), ueru- (2) and WP II, 499. (Variant of type wir- in Per. Tokh. Arm. See uir- (2). Gk. ambig.). Cf. uiior- Per. cf. girah *knot; Tokh. cf. wiralom (?) 'zedoary'; Arm. cf. gir, gs: gro, ab. s. grov
```


## [2026-10-16T05:19:57.938Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E \"^u[iī]+t|^uei-?t|willow\" IEC.txt | head -8 | cut -c1-400; grep -n -E \"rainbow\" IEC.txt | head -3 | cut -c1-300; grep -n -E \"^[0-9]+ *$\" IEC.txt | head -0"
}
```


### [2026-10-16T05:19:58.308Z] TOOL RESULT

```
3485:eiuos, à (iuos, à) (an unidentified tree: ‘yew, ground pine, sallow??) Gallo-Lat. (alleged) ivus ‘yew’; iva ‘ground pine (Fr. if, ive, id.); MIr. & Ir. eo ‘yew’; W yw, Cor. ew ‘yews’; Br. ivin, sg. & coll. ‘yew, yews’; OHG rwa, MHG we "be id.; OE iw, 60w; ON yr, id.; OCS iva ‘sallow’; Srb. iva ‘willow’; Slo- vene iva, jiva, id., beside ivje, n. ‘witches broom’. (For Li. Latv. ieva, see oiuo)
6189:-iiə (-iia, -io) collective extension of a sim- plex Skt. gavya ‘kine’; $Sunya “pack of dogs’; Av. cf. jonayo "of women’; Arm. majri (forest: majr “pine”); uri (^willow*: ur *vine-tendril); Gk. oikía ‘household’; Lat. familia, cüria; Ir. bráithre ('kinsmen": bráthair ‘brother’); luibh ‘herb’; W adein, adenydd “wings”, fr. *potonio, *peteniieo: adan, sg. ‘wing; OBr. mined ‘mines’; modreped ‘au
8278:kudos, is, io “shelter, hut Hes. cf. Kodar ‘tomb’; küdaros, op. m. n. ‘boat’; W (ambig.) cwdd, m. ‘cavity; shelter but cf. kudh-); SWG Hutte ‘willow basket beside MHG hotze ‘cradle’ and Frankish G Hotte ((back-basket, whence Fr. hotte, id. (but EMDu. hodde ‘basket, E hod derive from a type *kudh-. Du. hut 'cottage, hut, cabin' appears to be from HG, cf. OHG hutta, id. and hence to type *kudh-
9423:laĝ- ‘wind, creep; twist, winding object, creeper’ Per. raz ‘grapevine, vineyard’; OCS loza, Blg. lozà ‘vine’; Ukr. loza, f. ‘willow’; R lozà, f. ‘branch’; Norw. cf. (?) lakke ‘draw near’
12666:peluà (a tree: ‘sallow’ or ‘alder’) Oss. fürwe ‘alder; OHG félawa, f., MHG vëlwe, s. & wf. ‘willow’; G. cf. Felber ‘white willow’
14204:quorquol- (quorquol-) (1) ‘twist, turn, curl, coil, wicker, weave’. Cf. qur-quol and the e-/o- gde simplex quel-/quol- Alb. (z-gde) kurkulloj, v. ‘nestle, curl up, lurk’; Lat. curculio, gs: -onis, m. (1) *corn-weevil'; ME wharwyl, wharwhil ‘whorl, swivel, pulley’; Li. kafklas, m. ‘sallow, willow’; karkles, pl. ‘wicker’; Latv. karkls, m. ‘scrub willow’. Vari-
14984:saliK- (saloKa) ‘willow, sallow-tree'. Cf. selos. WP IL, 453 Oss. xàárís, Dig. xàrwes, s. ‘willow’; Lat. salix, gs: -icis, f. id.; Ir. saileach, saileog, f. id.; Br. halek, m. coll. id.; W helyg, Cor. helyk, coll. id.; Gaul. salico- (in names); OHG salaha, MHG salhe, OE sealh, ON & Norw. selja, Sw. sälg, f. id.; (LW in) Finn. salava, id. (Gk. helíke ‘willow’ is due to the influence of the vo
19590:ursis (ursis) *wickerwork, basket, withy’ Per. više (1) ‘ivy, woodbine’; Arm. uf, o-st. ‘vine-shoot’; uri, gs: -vo, ab. s. -eav, s. ‘willow’; Gk. hurrís, gs: -ídos, f. ‘basket’; Cz. vrš, f. *fish-basket, creel’; Pol. wiersza, f. id.; R vér3a, f. id. (Isophonic: Alb. urrë, f. 'sapwood")
709:arkus, arkuos /bownet, bow with string(s), bow, bend'. Cf. WP I, 81 Lat. arcus, gs. üs (also OL gs arqui *bow); arquus ‘rainbow’; cf. arqui-tenens “holding a bow’; OE earh, earwe ‘arrow’; ON or, pl. orvar, id.; Go. cf. arhvazna ‘arrow’; OCz. cf. roky-ta, Srb. rakita ‘sallow tree’ (?). Other con
3007:dhonguhos, à, us “covering: cover, arch. Cf. dhenguho (1) OCS doga (and comm. SI. rainbow); R dugà ‘arch’; Li. dangà “cover, roof; garment’; dan- güs ‘sky’. Cf. WP I, 852 and dhnguho-
17816:sül- (2) (variant of type sáuel-, sául-) “sun, light, eye Skt. sárab, m. “sun? beside süryab, id.; Oss. xur, Dig. xor, id.; Per. cf. nu-hür, s. “eye, sight, look, scowP (fr. *ni-^); Scyth. cf. oitó- suros, m. (epithet of Apollo); Alb. cf. yl-ber (rainbow, if fr. *suli-bher$- cf. ON sól-bjartr
```


## [2026-10-16T05:20:02.059Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD; grep -n -m5 -E \"vov[eē]re|aogəd|aogada|aojaite\" WLD_Bd1_pages.txt | cut -c1-300; grep -n -m6 -E \"va[eē]iti|Iris|wīr|wir \" WLD_Bd1_pages.txt | cut -c1-300; grep -n -E \"\\[pdf page\" WLD_Bd1_pages.txt | head -2"
}
```


### [2026-10-16T05:20:02.412Z] TOOL RESULT

```
27264:rniverr , vovere ..Eichborn";
27266:              vovere,
619:erste groBe Eisenzeit Europas, die Hallstadtkultur, verdanken wir bekannt-
1706:miliert sein (vielleicht unter Mitwirkung von v'edu „wir zwei“, da von zwei
5619:„mogen wir rfisten“ liegt in der Bed. ab; nnaiia RY. 8, 45, 5 ist unklar);
8343:J. Schmidt aaO., daB wir es mit einem Dentalstamm zu tun haben, der
18957: 39,65. Fraser, Eriu V 15ff.j. Am meisten fur sich hat fur das Irische dieAn-
20239:lie-    „wir            .
```


## [2026-10-16T05:20:05.186Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD; for n in 118 119 120; do awk -v RS='\\f' -v n=$n 'NR==n' WLD_Bd1_pages.txt | grep -n -i -E \"eug|vov|aog|ευχ|voto|gelob\" | head -5; echo \"--$n\"; done"
}
```


### [2026-10-16T05:20:05.790Z] TOOL RESULT

```
39:haut, Gebirnhaut“ (Lit. bei Vf. LEWb. 2 s. v.; nieht iiberzeugend von Peters-
62:mann Apr. s. v. „ledernes Kopfzeug des Pferdes zum halten"), lit. aiitas
--118
35:euegSli- „feierlich, riihmend, prahlend sprechen, auch bes. religios geloben,
37:      Ai. ved. vd jhdt- „der Gelobende, Beter, Yeranstalter eines Opfers“, av.
42:102) gug „sage!“, gogres „du kannst sagen“; lat. voveo, -ere, vovt, votum
43:(diese zuniichst aus *vove-vai, -turn, Solmsen KZ. 37, 3f., Stud. 88 f.) „ge-
48:vutts) „votis, consecratis“, vnfru „votivum“, Yufiune Uofione „deo votorum“              ,
--119
33:zeugend mit der Bed. unserer \Yz. zu vereinigen; auch do-uccim, tucu
--120
```


## [2026-10-16T05:20:07.467Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD; awk -v RS='\\f' 'NR==119' WLD_Bd1_pages.txt | sed -n 33,70p"
}
```


### [2026-10-16T05:20:07.811Z] TOOL RESULT

```
euegSli- „feierlich, riihmend, prahlend sprechen, auch bes. religios geloben,
     preisen"; eny^h-, vsrjih-.
      Ai. ved. vd jhdt- „der Gelobende, Beter, Yeranstalter eines Opfers“, av.
(s.Bartholomae Airan. Wb. 1527) rastarj-vaysnti- EN. arm. (Meillet Esq.                      ;



102) gug „sage!“, gogres „du kannst sagen“; lat. voveo, -ere, vovt, votum
(diese zuniichst aus *vove-vai, -turn, Solmsen KZ. 37, 3f., Stud. 88 f.) „ge-
                                                                                 1
loben,         feierlich    versprechen;   wunschen'  umbr. vufdes (= lat.
                                                         erflehen,                   ,

vutts) „votis, consecratis“, vnfru „votivum“, Yufiune Uofione „deo votorum“              ,


(v. Planta I 450, Osthoff MU. 5, 82 Anm.).

   Aber air. tongu „schwore“, cymr. tyngu nicht als *to-fo(n)g- hierher
(Zimmer KZ. 24, 2 6 f.) sondern zu einer Wz. to(n)g-, teg-, s. Yendryes
                                1
                                          ,


Gramm. 239 f. m. Lit., Pedersen KG. II, 652f.
  Ablautstufe cug'ih- av. aoq- (gojaite, aTixta, adgdda „verkimden, sagen,
                                    :

                                T
sprechen, bes. in feierlicher Yl eise“, wozu (s. Curtius 702 m. Lit., Baunack
KZ.        500 f., Bartholomae AF. I, 11, Geldner Yed. St. Ill, 59, wo aus-
            35,
fiihrl.             ai. dhate „lobt, rtihmt, prahlt“, und vermutlich (s. Pedersen
              zur Bed.)
KZ. 40, 210) arm. uze.m „ich will“, lj-uzem „ich suche“;
   gr. tvyo/iai ,,gelobe, bete, wiinsche, rilhme mich“, evyog n. „wessen man
```


## [2026-10-16T05:20:10.964Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD; awk -v RS='\\f' '/Weidengerte|Regenbogen/ {print NR\": \"substr($0,1,80)}' WLD_Bd1_pages.txt | head; "
}
```


### [2026-10-16T05:20:11.283Z] TOOL RESULT

```
234:                                          :            }                         
235: 226                                                 uei-



wohl ags. icine-wind
238:                                                                              uei
244:                                                                                 
273: 264                                                                             
800:
```


## [2026-10-16T05:20:13.685Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD; for n in 235 238; do awk -v RS='\\f' -v n=$n 'NR==n' WLD_Bd1_pages.txt | grep -n -E \"Weidengerte|Regenbogen|av\\.|np\\.|ags\\. w\" | head -6 | cut -c1-250; echo \"--$n\"; done"
}
```


### [2026-10-16T05:20:14.147Z] TOOL RESULT

```
18:vino und aus dem Slav. lit. vf/nas), sondern wohl auch die von falisk. volsk.
60:      Gr. iotg „Regenbogen“ (fToig        .
65: personifizierte Regenbogen“ (Lit. unter *uci- „auf etwas losgehn“): ags. icTr
71: lautend ags. wilr ds. (oder mit r aus ,r zur Wzform ucis-, s. d., oder zu
--235
8:av. vaenaiti „sieht“  eher auf den Begrift’ „sehnsiichtig wonach schauen“
48:   Aber Tgi; „Regenbogen“ nicht als „farbiger Streifen oder StraBe am
--238
```


## [2026-10-16T05:20:17.216Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs/incoming/WLD; for n in 235 236; do awk -v RS='\\f' -v n=$n 'NR==n' WLD_Bd1_pages.txt | grep -n -i -E \"weide|vaet|vait|bed\" | head -6 | cut -c1-250; echo \"--$n\"; done; awk -v RS='\\f' 'NR==235' WLD_Bd1_pages.txt | sed -n 58,68p"
}
```


### [2026-10-16T05:20:17.572Z] TOOL RESULT

```
67:virv-virhi „Arbeit aus Metalldraht" (vgl. zur Bed. lit. vie-ld „Eisendraht“).
68: woneben        anderer Bedeutungswendung (nach Falk-Torp u. vire) viel-
--235
--236

      Mit r-Formantien
      Gr. iotg „Regenbogen“ (fToig        .
                                              = Igig undEiotg ey 7oig) „der als Gotterbotin
                                                r


 personifizierte Regenbogen“ (Lit. unter *uci- „auf etwas losgehn“): ags. icTr
,,Metalldraht, gewundener Schmuck“, mnd. wire „Metalldraht“, spat, anord.
virv-virhi „Arbeit aus Metalldraht" (vgl. zur Bed. lit. vie-ld „Eisendraht“).
 woneben        anderer Bedeutungswendung (nach Falk-Torp u. vire) viel-
```


## [2026-10-16T05:20:20.945Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E \"PASOX|PĀSOX|PASUX|BID\\b|BĪD|BED\\b|BISHE|BIŠE|BIŠEH\" incoming/ARY/ARY_latin_index_pages.txt | head; grep -n -E \"^(پاسخ|بید|بیشه)\" incoming/ARY/ARY_pages.txt | head; ls incoming/ARY | head"
}
```


### [2026-10-16T05:20:21.262Z] TOOL RESULT

```
4031:BARNHART: (BID) 92 BIDDA, OLD FRISIAN) AS 523
4033:ONIONS: (BID) 93 (OLD HIGH GERMAN) 5 galt
4034:SKEAT:  (BHEUDH) 752, (BID) 59 BIOTAN, BITTEN
10238:SPASOX, PASSOX :aT 5) cel vst SS "gre! y "3h" lat aly 5I feel” pos Godly “A
11958:HLAVA (BOHEMIAN) gan y HOBID — (OLD SAXON) ef iy-Ste
12867:KUVEN (NORWEGIAN) (5535 GUMBED KURDISH) 3,6
Permissions Size User   Date Modified Name
.rw-r--r--  8.1M sfmqrb 14 Oct 22:19  ARY_aryanpur_kashani_rishehaye_hend_o_orupayi.pdf
.rw-r--r--  586k sfmqrb 14 Oct 22:19  ARY_latin_index_pages.txt
.rw-r--r--  960k sfmqrb 14 Oct 22:19  ARY_pages.txt
```


## [2026-10-16T05:20:23.587Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'NR<=10238 && /\\[pdf page/ {p=$0} NR==10238{print p}' incoming/ARY/ARY_latin_index_pages.txt; sed -n 10230,10245p incoming/ARY/ARY_latin_index_pages.txt | cut -c1-200; grep -n -E \"پاسخ|بیشه\" incoming/ARY/ARY_pages.txt | head"
}
```


### [2026-10-16T05:20:24.022Z] TOOL RESULT

```
[pdf page 352]
BARNHART: (SAY) 961 SIGE DANISH) Sails
DELAMARRE: (DIRE) 279 SAGA. SWEDISH) «528 yo
‘MACKENZIE: (SPEECH) 134 SEGGEN, ZEGGEN (DUTCH) 5.
BUCK: 1256-1258 OLD CHURCH SLAVIC) 95.5 93e\
ONINOS: (SAY) 792 SOCHITI
SKEAT: (SAY) 536 OSOKA POLISH) ging)
Wes seb oly SKAZAT (RUSSIAN) guy
. ieetlaay
SPASOX, PASSOX :aT 5) cel vst SS "gre! y "3h" lat aly 5I feel” pos Godly “A
APATASXANT, 2 | BERSIV: 5525
BSS YoY pS alle
Ale 2yldi gladly omg gel Gata - Gilal Glasly coed gi! Glaajly cul Aw ONIONS 1"
Maal ge Sealy bp UY ea 239) Coad cal Baa~ ipl clad pa beh,
opleazaT (ule)
ae
SAR HBALUCHI) gx sh SARAH- HAVESTAN) gles}
219:و پوست سفید تجسم می‌کنند (5663 ,01۸-1-07؟ فعلاً برای این پرسش‌ها پاسخ قاطعی در
10449:۱ واژه‌ی فارسی "پاسخ" از واجربشه‌های "پاد" و "سخن" تشکیل شده است» (پهلری آن: ۳۸880 ,(۳80
14867:۲- چم اين واژه در یونانی و لاتین؛ بیشه‌ی مقدس» چراگاه, ۰ ۵ و
```


## [2026-10-16T05:20:27.277Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E \"WILLOW|VAETI|WEIT|FOREST|WOOD\" incoming/ARY/ARY_latin_index_pages.txt | head; sed -n 10440,10452p incoming/ARY/ARY_pages.txt | cut -c1-250"
}
```


### [2026-10-16T05:20:27.583Z] TOOL RESULT

```
290:€53,) 9 BEE) 14 45538 9 (OAK) «gin 5 (WILLOW) gp 5 (SALMON) al3T gal
4003:BARNHART: (WILLOW) 1237 WIDIG, {OLD ENGLISH) apf 5 AS
4005:‘MACKENZIE: (WILLOW) 140 WILLOW ENGLISH) AS
4007:SKEAT: (WILLOW) 716 WILG (DUTCH) gate
8359:DULIOS, DUI-TOS ZWEIT GERMAN) glaT
9953:Sandal LITHUANIAN) «gh WHEITS, HWEITS (GOTHIC) 3
9955:KVITU ALATVIAN) (8) 3 HWEITI, HWITR
15679:‘MACKENZIE: (FIREWOOD) 114 ‘REFERENCES both,
انگلیسی (5ل870): هی 397 ین
دانمارکی (0۸0/184): 508 1 (8۸) ی مین اس
سوئدی (31720/50): ۵6۸ 9 (0188) ما۸5
ملدی (ثن۵07: 2860680 ,8860801 4 (8۳8503) ات دی هم
اسلاری کهن (۲10با5 )نان 0ا0): ناش تلا
1 هن 2 (8۸9) :0/05
لهستانی (۳03): ه6ا050 6 (8۸9) 37
روسی (551۸1): هد برهان قاطع : 11:۶
یادداشت: :
۱ واژه‌ی فارسی "پاسخ" از واجربشه‌های "پاد" و "سخن" تشکیل شده است» (پهلری آن: ۳۸880 ,(۳80
کردی: 315881۷ ارمنی:۳۸7۸87۸۷1).
۲- چم این واژه در لانین: به ترتیب گفتن.
۳- 03110188 معتقد است که واژه‌های این فهرست با واژه‌های ایرانی - هندی این فهرست رابطه‌ای ندارد. سایر
```


## [2026-10-16T05:20:30.508Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E \"^\\*?(H?aug|Haug|aug)[ -]|\\*Haug\" CHEUNG.txt | head -5; grep -n -E \"pāsox|pāsux|pasux|pasox\" CHEUNG.txt | head -5; grep -n -E \"\\*ca[nŋ]h|\\*sah\" CHEUNG.txt | head -5"
}
```


### [2026-10-16T05:20:30.863Z] TOOL RESULT

```
21898:*pati-) MMP pswx, BMP pshw /passox/, p’shw /pasox/ ‘answer’? = DMMPP: 311, 
35471:/pasox/, 334 
41313:pasux, 334
```


## [2026-10-16T05:20:32.515Z] TOOL CALL #77: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 21870,21905p CHEUNG.txt"
}
```


### [2026-10-16T05:20:32.835Z] TOOL RESULT

```
2002: 124 


*sanh ‘to declare, explain’ 

*AVESTAN: songh- (ѕарһ-) ‘to declare, explain’ || (+ *abi-) ‘to call names, curse’ || (+ 
*pati-) ‘to call up, invoke’ = Liste: 62 

Pres. them.: IND. 15р. YAv. paiti.sayhämi (V 20.7), 3sg. OAv. songhaiti (Y 43.6), med. 3sg. OAv. 
songhaite (Y 32.7), YAv. sanhaite (V 18.1), 1р1. OAv. songhamahi (Y 31.1), INJ. 3sg. YAv. sanhat (V 
22.8, V 22.13 f£), SUBJ. 1sg. OAv. sanghani (Y 46.17), Y Av. saghani (Vyt 13), OPT. 25р. YAv. sanhöis 
(V 22.7), med. 2sg. YAv. paiti.sanhaéSa (Yt 14.35); Aor. athem.: OPT. 3sg. OAv. saxiiat (Y 44.1, Y 
44.9); Partic.: perf. pass. YAv. aißi.sasta- (Yt 14.34); Inf.: aor. OAv. sasté (Y 30.8, Y 46.12), ? OAv. 
sazdiiai (Y 30.2, Y 51.16); Intens.: impf. IND. 3sg. ? YAv. asasat (V 19.15, V 19.35), SUBJ. 3р1. ? YAv. 
sasanhan (V 2.16). 0 OAv. sazdiiai may have a different etymology, viz. from *sand. 

*OLD PERSIAN: Oa" h- ‘to declare, say’. Ф According to Kuiper 1960: 159 ff., OP 0atiy 
is derived from a separate root, but see also Hoffmann (apud Goto 1987: 303, fn. 
721). = Kent: 188a 

Pres. them. {1}: impf. IND. 1sg. аба"ћат «a-0-h-m» (DB 2.30, DB 2.50, DB 2.83, etc.), «[a]-[0]-h-m» 
(DB 2.20), Zeg. a6a"ha «a-0-h» (DB 1.75, DB 2.15, DB 2.80, etc.); Pres. athem. (2): IND. 2sg. Өяһу 
«0-a-h-y» (DB 4.55, DB 4.58), 3sg. Oätiy «0-a-t-i-y» (DB 1.6, DB 1.8, DB 1.11, etc.), IMPV. 2sg. ? 
“@adiy (DB 4.54); Pass.: pres. IND. Ipl. 0ahyamahy «0-h-y-a-m-h-y» (DB 1.7), «0-[h]-y-a-m-h-y» (DBa 
10), impf. 3sg. adahya <а-0-һ-у> (DB 1.20, DNa 20), <a-0-h-y> (DB 1.23); Inf.: 0astanaiy <0-s-t-n-i-y> 
(DB 1.53) 

*MIDDLE PERSIAN: MMP sxwn, ВМР shwn (MR Y?) /saxwan/ ‘word, speech’ || (+ 
*pati-) MMP pswx, BMP pshw /passox/, p’shw /pasox/ ‘answer’? = DMMPP: 311, 
284a 

*PARTHIAN: sxwn ‘word, saying, utterance’ || (+ *pati-) pswx ‘answer’ = DMMPP: 
311, 284a 

*KHOTANESE: samja- ‘document’
```


## [2026-10-16T05:20:35.254Z] TOOL CALL #78: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; for w in پاسخ بید بیشه; do python3 tools/fetch_source.py \"https://vajehyab.com/moein/$w\" --note \"page 532: Mo'in entry for $w\"; done; "
}
```


### [2026-10-16T05:20:36.900Z] TOOL RESULT

```
/home/sfmqrb/git/rishe-private/data/verification/sources/web/c18ede8b5910f9bc.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/1a915ba63e5c00c8.txt
/home/sfmqrb/git/rishe-private/data/verification/sources/web/6398f419a02fb631.txt
```


## [2026-10-16T05:20:39.048Z] TOOL CALL #79: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; for f in c18ede8b5910f9bc 1a915ba63e5c00c8 6398f419a02fb631; do sed -n 1,4p $f.txt; grep -n -E \"معین|\\[ ?په|\\(اِ\\.\\)|\\( ?اِ ?\\)\" $f.txt | head -5 | cut -c1-300; done"
}
```


### [2026-10-16T05:20:39.393Z] TOOL RESULT

```
URL: https://vajehyab.com/moein/پاسخ
FETCHED: 2026-10-16T05:20:36Z
STATUS: 200
TITLE: معنی پاسخ | فرهنگ انتشارات معین | واژه یاب
4:TITLE: معنی پاسخ | فرهنگ انتشارات معین | واژه یاب
6:معنی پاسخ | فرهنگ انتشارات معین | واژه یاب 
16: فرهنگ انتشارات معین
17: (سُ) [ په . ] ( اِ.) 1 - جواب . مق . سؤال . 2 - اطاعت . 3 - پذیرفتگی . 4 - کیفر، مکافات . 5 - عوض ، پاداش . 6 - تعبیر خواب ، گزارش رویا.
URL: https://vajehyab.com/moein/بید
FETCHED: 2026-10-16T05:20:36Z
STATUS: 200
TITLE: معنی بید | فرهنگ انتشارات معین | واژه یاب
4:TITLE: معنی بید | فرهنگ انتشارات معین | واژه یاب
6:معنی بید | فرهنگ انتشارات معین | واژه یاب 
16: فرهنگ انتشارات معین
17: [ په . ] ( اِ.) درختی است از تیرة بیدها، بی میوه ، سایه دار، دارای شاخه های مستقیم و بلند. چوبش کم دوام است از پوست آن ماده ای به نام سالیسین به دست می آید که تب بُر است .
URL: https://vajehyab.com/moein/بیشه
FETCHED: 2026-10-16T05:20:36Z
STATUS: 200
TITLE: معنی بیشه | فرهنگ انتشارات معین | واژه یاب
4:TITLE: معنی بیشه | فرهنگ انتشارات معین | واژه یاب
6:معنی بیشه | فرهنگ انتشارات معین | واژه یاب 
16: فرهنگ انتشارات معین
17: (ش ِ) [ په . ] ( اِ.) 1 - نیزار، نیستان . 2 - جنگل کوچک .
```


## [2026-10-16T05:20:43.488Z] TOOL CALL #80: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E \"\\bw[eē]t\\b|\\bv[eē]t\\b|wyt|w[eē]šag|wyšk\" SNS_pages.txt | head -8 | cut -c1-250; echo ---AVG; awk -v RS='\\f' 'NR==292' AVG.txt | grep -n -E \"aog|aoj|aox\" | head -5 | cut -c1-250; echo ---DKS; grep -n -m5 -E \"vaēiti|vaeiti|vēt|vaētay\" ISS_alt_DKS.txt | cut -c1-300"
}
```


### [2026-10-16T05:20:43.865Z] TOOL RESULT

```
11705:                                                sn:>»:tpwyt>
---AVG
5:From  tf-stem:  Av.  amavatit-  adj.  'strong'  =  Skt. dmavant-;  Av.  pupravan_t-  'having  a  son'  =  Skt.  /«• travdnt-;  Av.  haomavan^t-  'having  haoma'  =  Skt.  soma- vant~.  —  From  /-stem:  Kv .  fraza^tivarit-  'having  off- spring' ;
---DKS
5212:bi ‘willow’, Sid. 1or2, BS vanjala-, Tib. lčan-ma. See alio banījäm ‘bark of oak or willow’. То Av. vazti- ‘willow’: Vid. 22:20 nava vaētayð barat ‘he carried nine withies’, gloss Zor.P. tak т v&t 'branch of willow’, N.Pers. bëd, Pašto wala, Orm. wula, Parāčīi yi, Suyni, 'Sangle&i wed, Yidya wi
```


## [2026-10-16T05:20:47.625Z] TOOL CALL #81: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E \"aog|aoj|aox\" AVG.txt | head -10 | cut -c1-250; awk -v RS='\\f' 'NR==292' AVG.txt | head -5 | cut -c1-200; sed -n 5205,5214p ISS_alt_DKS.txt | cut -c1-200 | head -3; awk -v RS='\\f' 'NR<=1 {}' ISS_alt_DKS.txt; grep -n -c $'\\f' ISS_alt_DKS.txt"
}
```


### [2026-10-16T05:20:47.980Z] TOOL RESULT

```
174:§  56.  In  its  p  h  o  n  o  1  o  g  y  the  Avesta  agrees  with  the  Sanskrit  in its  vowels  in  general,  but  the  Avesta  shows  a  greater  variety  in  using  e-  and <>-sounds  instead  of  a.  Final  vowels ,  except  6,  are  sho
597:Av.  ddmohu  (beside  ddmahvd)  'among  creatures' =  Skt.  dhdmasu;  GAv.  gH^odum  'may  ye  hear',  be- side GAv.gujjahvd  'hear  thou* ;  GAv.  vtr'zyotu  'let  him do',  beside  Av.  var'zyanto. — Av.  asto.vidotus  'Bone- divider',  beside 
632:(a)  Av.vyano  'pursued'  (|/"vf-)  =  Skt.  vyanas ;  Av.  ^ayehi  'thou rulest'  (]ffl$i-)',  Av.  viddyum  'anti-demoniac'  (daeva-,  on  oi  =  ae  §  56) ; uifyaojano  'thus  speaking'  beside  u'ti  aj>jand ;  pa'tyaptm  'up  stream' (pa*ti
660:Av.  aojo  'strength'  =  Skt.  6jas;  Av.  raod*nti  'they grow*  =  Skt.  rohanti;   Av.  tdyaof  'of  a  thief*  =  Skt.
808:Av.  tyratus  'wisdom'  =  Skt.  krdtus;  Av.  irinafyti 'he  lets  go,  drives'  =  Skt.  ritf,dkti;  Av.  taofyma  'seed' =  Skt.  tokma;  Av.  ty§apr*m  'rule,  kingdom'  =  Skt. k$atrdm. — YAv.  syaopndis,  GAv.  jyaoj^ndis  'by  deeds' =  Sk
841:§  82  a.  Observe  in  connection  with  this  rule  §  82  that the  sonant  spirants  appear  before  z:  cf.  §  180.  GAv.  aojzd 't*1  i  spakest' ;  diwzcedydi.— *$>£.£.  §  89  Bartholomae's  Law.
878:YAv.  jvantym,  GAv.  jvantd  'living'  =  Skt.  jivan- tam,  etc.  (§  68  Note  2) ;  YAv.  jajnvm  'having  smitten' =  Skt.jaghnivdn; — YAv.  jym  'bowstrings'  =  Skt.  jyds; GAv.  jydtSus  'of  life',  cf.  Skt.  jlvdtos;  also  GYAv. aojis
888:GAv.  aog>da  'he  spake'  to  "\faugji  -j-  ending  ta,  cf.  Gk.  su/ojiai, Skt.  ohati;  GAv.  cag»do  'they  two  grant'  to  Yk^ig^h  -f-  -tas.  —  GYAv. vtr'zda-  'grown  great,  mighty',  to  ~\[vardh  -f-  -ta-,  cf.  Skt.  v^ddha-; GA
890:YAv.  aofyta  'he  spake',  to  ~\faug^i  -\-  ending  ta,  beside  GAv. aog»da;  YAv.  drufyto  'deceived',  to  "\fdraugJi-\--ta-,  =  Skt.  drugdhds. —YAv.  daste  'he  makes',  to  ~\[dha-,  pres.  stem  dadh  -\-  tl ,  beside GAv.  dazdl ; 
975:Av.  d&raythi  'thou  holdest  fast'  =  Skt.  dh&rdyasi ;  Av.  jaidyeki 'thou  askest' ;  Av.  sadayeki  'thou  appearest'  =  Skt.  chaddyasi ;  Av. aojyehJj  'more  strong'  (ace.  pi.  fern.)  =  Skt.  ojlyasfs.
'ri)  =  Skt.  -van,  (f.  -vari\  Whitney,  §  1 234. §  855.     A  few  secondary  derivatives    are   made  with the  suffix  -van.    They  show  also  a  corresponding  feminine -valri.     Exa
Av.  ajavan-  adj.  m.,  afava'ri-  (beside  afaont-)  adj.  f.  'righteous* =  Skt.  ftavan-  (f.  -vart);  Av.  apravan-  m.  'priest'  =  Skt.  dtharv an-; Av.  hapto.karjyan-  n.  'seven  karshvar
29.  Av.  -vana  =  Skt.  -vana  (Whitney,  §   1245  1). §  856.     This   suffix   arises   apparently    by    transfer   of  the  preceding -van  to  the  a-inflection.    It  bears  also  a  rel
30.  Av.  -vant  =  Skt.  -vant  (Whitney,  §  1233). §  857.  The  suffix  -vatit  is  closely  akin  to  the  suffix -man.t,  and  like  the  latter  it  is  used  in  making  a  large number  of  p
From  tf-stem:  Av.  amavatit-  adj.  'strong'  =  Skt. dmavant-;  Av.  pupravan_t-  'having  a  son'  =  Skt.  /«• travdnt-;  Av.  haomavan^t-  'having  haoma'  =  Skt.  soma- vant~.  —  From  /-stem
bästa- 'conducted', participle to bëy-. See also їп 83:19 büsta-.
bàsta- 'stuffed', разѓа-, Z 2:13 kye ggisa baste kye grüske ‘some ate grasses, some husks’; Z 24:169 ce geisa baste 'some ate grasses’; parallel to Pali tiya-bhakkha- (Digha- niküya 1166); Manj. 19 ha
bāljsakyau — bimga 279
573
```


## [2026-10-16T05:20:51.496Z] TOOL CALL #82: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 880,888p AVG.txt | grep -o -E \"§ +[0-9]+\" | tail -2; awk 'NR<=888' AVG.txt | grep -c $'\\f'; awk 'NR<=5212' ISS_alt_DKS.txt | grep -c $'\\f'"
}
```


### [2026-10-16T05:20:51.903Z] TOOL RESULT

```
§  82
§  90
83
317
```


## [2026-10-16T05:20:57.373Z] TOOL CALL #83: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; n=$(grep -n -m1 -E \"^withy, n\" KLN_1971.txt | cut -d: -f1); echo $n; sed -n \"${n},$((n+10))p\" KLN_1971.txt"
}
```


### [2026-10-16T05:20:57.751Z] TOOL RESULT

```
267869
withy, n. — ME. wit hi, fr. OE. widig, ‘willow, 
willow twig’, rel. to OE. widde, ‘withe’, ON. 
vidir, ‘willow’, Swed. vide , Dan. vidje, ‘willow’, 
OHG. wida, MHG. wide, G. Wetde, ‘willow’, 
and cogn. with Avestic vaeiti-, ‘osier’, Gk. vtia 
(prob. for *Fenr!a), ‘willow’, tru?, Aeol. 
ftTU?, ‘the edge or rim of anything round’, 
oiauT), otauov (for •FoitFut), *Fokfuov), ‘a 
kind of willow’, olcro<; (for ‘withy’, 

L. vitis, ‘vine’, vitex, ‘the chaste tree’, Lett.
```


## [2026-10-16T05:21:17.978Z] TOOL CALL #84: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/wekʷ-' --note 'page 532: Av. duš-ūxta- / hūxta- from vac- (*wekw-), not aog-'; f=$(python3 -c \"import hashlib;print(hashlib.sha1('https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/wekʷ-'.encode()).hexdigest()[:16])\"); grep -n -i -E \"xta|ukta\" data/verification/sources/web/*.txt 2>/dev/null | grep -i \"wek\" | head -3; cd data/verification/sources/refs; grep -n -o -E \"^.{0,8}du[sšž]+[uü]xta-.{0,200}\" BRT.txt | head -3"
}
```


### [2026-10-16T05:21:18.649Z] TOOL RESULT

```
/home/sfmqrb/git/rishe-private/data/verification/sources/web/0898c1b35e41e61a.txt
data/verification/sources/web/369f221e7c9a84f0.txt:171: Inherited from Middle Persian plwhtn' ( frōxtan , “ to sell ” ) , from Proto-Iranian *fra- ( “ toward, pro- ” ) + *vaxš- ( “ to grow, increase ” ) , the latter from Proto-Indo-European *h₂weks- . [ 1 ] Alternative theories link the second component to Proto-Iranian *wā́xš , from Proto-Indo-Iranian *wā́kš ( “ voice ” ) (whence آواز ( âvâz , “ voice ” ) ), taking the original meaning as "to cry out".
```


## [2026-10-16T05:21:21.261Z] TOOL CALL #85: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources; grep -n -i -E \"xta|ukt\" web/0898c1b35e41e61a.txt | head -8 | cut -c1-200; grep -n -E \"u[sšž]+[uü]xta|dusüxta|dujüxta|duzüxta|dui[uü]xta\" refs/BRT.txt | head -5 | cut -c1-300"
}
```


### [2026-10-16T05:21:21.700Z] TOOL RESULT

```
171: Proto-Indo-Iranian: *uktíš ( see there for further descendants )
200: Proto-Indo-Iranian: *uktás ( see there for further descendants )
210: Proto-Indo-Iranian: *uktʰám 
211: Proto-Indo-Aryan: *uktʰám 
212: Sanskrit: उक्थ ( ukthá ) 
22358:asavatum  .  .  yd  anhat  °/j  arsvacH  (sd.) V.  ^.  2;  —  sonst  nur  neben  manah- (zum  Wortlaut  der  Stellen  s.  Sp.  11 39 unter  o)  und  ^aohna-:  yänJm  manö  .  , •CS  ,  .  ^ae%p>m  zar^uitrahe  Y.  i8.  o; V.7.  51',  Äioo,  Yty.  83; — ma  apama .  .  mä  manaaha  .  .  'canha
30166:•  ].,  g.  hüxta-  Adj.  'gut  gesagt,  ge- sprochen'; stets  neben  humata-  und  kvarsla- (Stverz.):  humaUm  matte  .  .  't>m  vacS  .  . hvaritim  Iyaoia'i?tn  Y.  12.  8;  usw.;  — im  Gegensats  zu  duiüxta-:  humataheca mananhs  'iahe'a  vacanhs  hvaritahe^a Syaohnahe  .  .  dusmatahe
30705:duimüta-,  duiaxla-):  aibigairyä  (sd.)  dathi vispa  kumatäcä  hüxtäcä  't3cä  paitiricyä daikl  vlspä  dmmatacä  duiüxtäeä  dui- varlt3(a  Y. //.  17;  —  frastavattö  huma- taea  huxtala  °taca  niibanmnS  dusmalaca duiüxtaca  duävarstaca  H.  J.  7 ;  —  mä  hra- yqm  vaAUtanam  aiwi^yS
```


## [2026-10-16T05:21:24.637Z] TOOL CALL #86: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 30167,30170p BRT.txt | cut -c1-300; awk 'NR<30166 && /^\\s*1[0-9]{3}\\s*$/{l=$0} NR==30166{print \"col\",l}' BRT.txt; awk 'NR<2862 && /^\\s*[0-9]{2,3}\\s*$/{l=$0} NR==2862{print \"col\",l}' BRT.txt"
}
```


### [2026-10-16T05:21:25.049Z] TOOL RESULT

```
Komp. :  hu'  +ux/a:  —  »i.  lüild-  Adj.  —  Pü, : Aüxl  (Transsltr.).
•  j.  hüxtay-  £  'gutes  Sprechen':  mana- tahasca  *humaiti  hisvasca  **ti'^  tastayasca *lwarM  'ra%wyS.var!ii  (sd.)  P.  28.
Komp.:  hu^ -^-uxlay:  —  li.  sükiay-  f.  —  Pü.: ASxl.  —  ')  Hds.  Am/o.
•  j.,  g.  hu-xratav-  Adj.  'des  Einsicht  gut ist,  ems  ich  tsvoll':  haomö ..  •tus\.g,  23;  — fratanmät  lg  (näml.  haomahe)  havamm  . . 'tvSiyS.)  Y.10.2;  3; —  vastryö ^ao^anäii snsvS  hqs  'tul  ntmanhä  (Sp.  1068  u.)  Y.
col 1816
col 34
```


## [2026-10-16T05:23:56.841Z] TOOL CALL #87: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/build-532.py <<'PYEOF'\nimport json\nW_pasox='https://en.wiktionary.org/wiki/%D9%BE%D8%A7%D8%B3%D8%AE'\nW_bid='https://en.wiktionary.org/wiki/%D8%A8%DB%8C%D8%AF'\nW_bishe='https://en.wiktionary.org/wiki/%D8%A8%DB%8C%D8%B4%D9%87'\nW_h1wegwh='https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%81weg%CA%B7%CA%B0-'\nW_weh1y='https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/weh%E2%82%81y-'\nW_irisgk='https://en.wiktionary.org/wiki/%E1%BC%B6%CF%81%CE%B9%CF%82'\nW_wire='https://en.wiktionary.org/wiki/wire'\nW_vow='https://en.wiktionary.org/wiki/vow'\nW_weh1itis='https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/w%C3%A9h%E2%82%81itis'\nW_canhati='https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/c%C3%A1nhati'\nW_wekw='https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/wekʷ-'\nM_pasox='https://vajehyab.com/moein/پاسخ'\nM_bid='https://vajehyab.com/moein/بید'\nM_bishe='https://vajehyab.com/moein/بیشه'\n\nPOK348={\"src\":\"POK\",\"where\":\"p. 348, s.v. eu̯egʷh- (POK_full.txt l.29030-29069)\",\"stance\":\"supports\",\"note\":\"'Meaning: to praise, worship ... Latin voveō, -ēre, vōvī, vōtum \\\"to vow, promise solemnly ... devote\\\" ... eug^h-: Avestan aog- (aojaite, aoxta, aogəδa) \\\"announce, declare, say, speak, esp. in ceremonious way\\\"'\"}\nWLD110={\"src\":\"WLD\",\"where\":\"Bd. I p. 110 (WLD_Bd1_pages.txt leaf 119)\",\"stance\":\"supports\",\"note\":\"'eu̯egʷh- „feierlich, rühmend, prahlend sprechen, auch bes. religiös geloben\\\" ... lat. voveo, -ere, vovī, votum ... Ablautstufe eugʷh- av. aog- (aojaite, aoxta, aogədā) „verkünden, sagen, sprechen, bes. in feierlicher Weise\\\"'\"}\nAHD_wegwh={\"src\":\"AHD\",\"where\":\"Watkins 1985 s.v. wegʷh- (AHD_watkins1985.txt l.1132)\",\"stance\":\"supports\",\"note\":\"'wegʷh-. Also eugʷh-. To preach, speak solemnly. Suffixed o-grade form *wogʷh-eyo- in Latin vovēre, to pledge, vow: VOTARY, VOTE, (VOTIVE), VOW; DEVOTE, (DEVOUT). [Pok. euegʷh- 348.]'\"}\nIEC_eugh={\"src\":\"IEC\",\"where\":\"s.v. eugh- (IEC.txt l.3755) and guoueiō (l.5340)\",\"stance\":\"partial\",\"note\":\"Mann lists 'eugh- (ūgh-) rage, curse, swear, vow' with Gk. eukhomai, but puts Lat. voveō under a separate *gʷoueiō 'vow, declare' (with Lith. gavėti 'fast') — i.e. he separates the Latin verb from the Greek/Indo-Iranian group.\"}\nSYN1256={\"src\":\"SYN\",\"where\":\"18.21 SPEAK, TALK, p. 1253-1256 (SYN.txt l.31563ff)\",\"stance\":\"supports\",\"note\":\"'Av. aoj-, esp. 3sg. pret. mid. aoxta (Gath. aogədā) \\\"spoke, said\\\" (esp. in a formal, solemn sense) : Skt. ūh-, Grk. eukhomai \\\"pray, vow, boast\\\", Lat. vovēre \\\"vow\\\", etc. Walde-P. 1.110. Barth. 37f.'\"}\nBRT37={\"src\":\"BRT\",\"where\":\"cols. 37-38 s.v. aog-\",\"stance\":\"supports\",\"note\":\"'aog- V. praedicare ... PPfP. aoxta-, PFP. aojya-. Nur Med. 1) \\\"verkünden, sagen, sprechen\\\" (bes. in feierlicher Form)' ... 'mit paiti \\\"antworten\\\" ... paityaoxta' — Avestan only.\"}\n\ndef node(**k): return k\n\ne0_nodes=[\n node(id=1,lang=\"Old Persian\",words=\"aok; paiti-aok\",verdict=\"plausible\",\n  derivation=\"The forms belong to Avestan, not Old Persian: Av. aog- (pres. aojaite, pret. aoxta, Gath. aogədā) 'to speak solemnly', and paiti + aog- 'to answer' (paityaoxta, V. 2.3), Bartholomae cols. 37-38. Old Persian attests only θah- 'to say' (Kent; Cheung) and no aog-. The Indo-Iranian verb *Hawǰʰ- (Skt. ohate) is the regular reflex of PIE *h₁wegʷʰ-/*h₁eugʷʰ- (labiovelar > Iranian g/j, zero/full grade *h₁eugʷʰ- > aog-), so the connection to the root is in fact secure (contrary to Nourai's 'doubtful' note); only the language label and the use of 'paiti-aok' as the source of Persian pāsox are wrong.\",\n  derivation_fa=\"فعل aog- «با شکوه و رسمی سخن گفتن» و paiti + aog- «پاسخ دادن» در اوستایی گواهی شده‌اند (بارتولومه، ستون ۳۷–۳۸)، نه در پارسی باستان؛ پارسی باستان برای «گفتن» تنها θah- دارد. پیوند aog- با ریشهٔ هندواروپایی *h₁wegʷʰ- (هم‌ریشه با سنسکریت ohate، یونانی eúkhomai و لاتین vovēre) امروز پذیرفته است، پس یادداشت «پیوند مشکوک» نورایی بی‌جاست؛ اما برچسب «پارسی باستان» نادرست است.\",\n  sources=[W_h1wegwh],\n  ref_check=[{\"ref\":\"TZF:29\",\"status\":\"not_checked\",\"note\":\"Abolghasemi, Tarikh-e mokhtasar-e zaban-e farsi: no online/local copy (refs_online.json: login-only ketabnak PDF).\"}],\n  consulted=[BRT37,\n   {\"src\":\"KNT\",\"where\":\"lexicon (KNT_full.txt grep 'aug-|aog-')\",\"stance\":\"silent\",\"note\":\"Kent's Old Persian lexicon has no aog-/aug- 'speak'; only baug- 'free', draug- 'lie', etc. — the verb is not Old Persian.\"},\n   {\"src\":\"CHEUNG\",\"where\":\"p. 334 s.v. *sanh\",\"stance\":\"contradicts\",\"note\":\"'OLD PERSIAN: θanh- \\\"to declare, say\\\"' — Cheung's OP verb of saying is θah-, not aog-.\"},\n   SYN1256]),\n node(id=2,lang=\"Persian\",words=\"pâsox\",verdict=\"disputed\",\n  derivation=\"NP pāsox/pāsux 'answer' < MP passox/pasox (Book Pahl. pshw, Manichaean pswx; Parthian pswx) < Old Iranian *pati-sahwa- / *pati-saxʷa-, i.e. *pati- 'back, against' + *sah- / *cánh- 'to declare' (Av. saŋh-, paiti.saŋh- 'invoke'; OP θah-), from PIE *ḱens- 'proclaim' (Skt. śáṃsati, Lat. cēnseō); the same stem gives saxwan > soxan 'word'. Phonetically *-ahw- > MP -ox (cf. farrox < *farnahvant-), *-ts- > -ss-. It cannot come from Av. aog-/paiti-aog-, which would not yield -s-. Nourai's own alternative ('see root Kâs 2') is the one modern scholarship accepts (Horn 275, Hübschmann, Cheung, Wiktionary, Aryanpur).\",\n  derivation_fa=\"«پاسخ» از فارسی میانهٔ passox / pasox (پهلوی pshw، مانوی pswx) و آن از ایرانی باستان *pati-sahwa- است: پیشوند *pati- «باز، در برابر» + ستاک *sah- «گفتن، اعلام کردن» (اوستایی saŋh-، پارسی باستان θah-) از هندواروپایی آغازین *ḱens-؛ «سخن» نیز از همین ریشه است. هرن، هوبشمان، چونگ و آریان‌پور همه همین را می‌گویند. پس پیوند «پاسخ» با اوستایی aog- که نورایی کشیده نادرست است و اشتقاق دیگری که خود او پیشنهاد کرده (ریشهٔ Kâs 2) درست است.\",\n  sources=[W_pasox,W_canhati,M_pasox],\n  ref_check=[{\"ref\":\"TZF:29\",\"status\":\"not_checked\",\"note\":\"Abolghasemi's Tarikh-e mokhtasar not accessible locally or online without login.\"}],\n  consulted=[\n   {\"src\":\"HRN\",\"where\":\"no. 275, p. 64\",\"stance\":\"contradicts\",\"note\":\"'275. pāsux \\\"Antwort\\\". aw. *paitisahva- [paiti + √sah-, hat zwar im Awesta nur die Bedeutung \\\"beschwören\\\"]; phlv. pasux; arm. patasxani \\\"Antwort\\\".'\"},\n   {\"src\":\"HUB\",\"where\":\"no. 275 and p. 'ausl. -ux aus -axv' (HUB.txt l.1204-1208, 4398)\",\"stance\":\"contradicts\",\"note\":\"'Neben dem gewöhnlichen phl. pasaxv ... ein phl. *pasaxv anzusetzen, jenes aus *patsaxv ... (vgl. arm. patasxani \\\"Antwort\\\")'; 'ausl. -ux aus -axv: pasux \\\"Antwort\\\" = phl. pasaxv'.\"},\n   {\"src\":\"CHEUNG\",\"where\":\"p. 334 s.v. *sanh 'to declare, explain'\",\"stance\":\"contradicts\",\"note\":\"'MIDDLE PERSIAN: MMP sxwn, BMP shwn /saxwan/ \\\"word, speech\\\" || (+ *pati-) MMP pswx, BMP pshw /passox/, p’shw /pasox/ \\\"answer\\\"'.\"},\n   {\"src\":\"PHD\",\"where\":\"p. 64 (PHD_mackenzie.txt l.4085, 4100)\",\"stance\":\"silent\",\"note\":\"'passox [pshw, M pswx, N pasux] answer'; 'pasox = passox' — no etymology, but the form has -ss- < *-ts-, consistent with *pati-sahwa-.\"},\n   {\"src\":\"NYB\",\"where\":\"glossary NP index (NYB_vol2_glossary.txt l.6769)\",\"stance\":\"silent\",\"note\":\"'pāsux: pas[saxv]' — cross-reference only, no etymology.\"},\n   {\"src\":\"ARY\",\"where\":\"pdf page 352 (printed 353), entry SPASOX, PASSOX\",\"stance\":\"contradicts\",\"note\":\"Aryanpur files pāsox under PIE 'say' (cognates with Eng. say, OCS sočiti) and notes: 'واژه‌ی فارسی \\\"پاسخ\\\" از واجریشه‌های \\\"پاد\\\" و \\\"سخن\\\" تشکیل شده است' — pād + soxan, not aog-.\"},\n   {\"src\":\"MON\",\"where\":\"vajehyab.com/moein/پاسخ\",\"stance\":\"silent\",\"note\":\"'(سُ) [په.] (اِ.) ۱- جواب ...' — Mo'in only tags it as Pahlavi.\"}]),\n node(id=3,lang=\"Avestan\",words=\"aog, aoj, aox; aojaiti, aoxia, aogeda; duš-uxta\",verdict=\"disputed\",\n  derivation=\"Av. aog-/aoj-/aox- (allomorphs before vowels, palatals and t) 'to speak solemnly' with pres. aojaite (Nourai's 'aojaiti'), gerundive aojiia- (his 'aoxia'), Gathic pret. aogədā and YAv. aoxta are genuine and regularly continue PIE *h₁(e)ugʷʰ- (zero/full grade of *h₁wegʷʰ-; cf. Skt. ohate, Gk. eukhomai), so these are confirmed. But duš-uxta- (dužūxta- 'ill-spoken', opposite of hūxta- in humata hūxta hvaršta) contains ūxta-, the past participle of vac- 'to speak' (Proto-Indo-Iranian *uktá- < PIE *wekʷ-, Skt. ukta-, sūkta-), not of aog- (whose participle is aoxta-). That word belongs under *wekʷ-, so the node is partly wrong.\",\n  derivation_fa=\"فعل اوستایی aog- / aoj- / aox- «با سخن رسمی و آیینی گفتن» (aojaite، aojiia-، گاهانی aogədā، اوستای نو aoxta) به‌درستی از هندواروپایی آغازین *h₁wegʷʰ- است (هم‌ریشه با سنسکریت ohate و یونانی eúkhomai). اما duš-ūxta- «بد گفته» (در برابر hūxta- در «اندیشهٔ نیک، گفتار نیک، کردار نیک») از ستاک ūxta- است که صفت مفعولی فعل vac- «گفتن» (هندواروپایی *wekʷ-) است، نه از aog-؛ پس این بخش از ادعای نورایی نادرست است.\",\n  sources=[W_h1wegwh,W_wekw],\n  ref_check=[\n   {\"ref\":\"POK:348\",\"status\":\"supports\",\"note\":\"POK p. 348: 'eug^h-: Avestan aog- (aojaite, aoxta, aogada) \\\"announce, declare, say, speak, esp. in ceremonious way\\\"' (POK_full.txt l.29051). Pokorny does not list duš-ūxta.\"},\n   {\"ref\":\"KLN:1722\",\"status\":\"supports\",\"note\":\"KLN s.v. vote (1971 ed. l.263998; p. 1722 of the 1966 ed., not in the truncated 1966 OCR): 'vovere \\\"to vow\\\" ... cogn. with OI. vāghát- \\\"one who offers a sacrifice\\\", Avestic aogəda, \\\"he said\\\", Arm. gog \\\"say\\\", Gk. eukhē \\\"vow, wish\\\"'.\"},\n   {\"ref\":\"SYN:1256\",\"status\":\"supports\",\"note\":\"Buck 18.21: 'Av. aoj-, esp. 3sg. pret. mid. aoxta (Gath. aogədā) \\\"spoke, said\\\" (esp. in a formal, solemn sense) : ... Lat. vovēre \\\"vow\\\"'.\"},\n   {\"ref\":\"AVG:237\",\"status\":\"not_found\",\"note\":\"AVG leaf 291 (p. 237) treats the suffix -vant; aog- is discussed at p. 29 §90 (leaf 83): 'GAv. aogədā \\\"he spake\\\" to √augh + ending ta, cf. Gk. eukhomai, Skt. ohati' — supports the form but not at the cited page.\"}],\n  consulted=[BRT37,\n   {\"src\":\"BRT\",\"where\":\"col. ~1838 s.v. hūxta- / dužūxta-\",\"stance\":\"contradicts\",\"note\":\"'hūxta- Adj. \\\"gut gesagt, gesprochen\\\" ... im Gegensatz zu dužūxta-' ; 'Komp.: hu + uxta: — ai. sūkta-' — uxta- = Skt. ukta-, pp. of vac-, not of aog-.\"},\n   POK348,WLD110,SYN1256]),\n node(id=4,lang=\"Latin\",words=\"vověre\",verdict=\"confirmed\",\n  derivation=\"Lat. vovēre (voveō, vōvī, vōtum) 'to vow, pledge, devote' < Proto-Italic *woɣʷeō < PIE o-grade causative/iterative *h₁wogʷʰ-éye-ti (initial laryngeal lost, *gʷʰ > Italic *ɣʷ > Lat. v between vowels); cognate Umbrian vufru 'votive'. The book prints 'vověre' with a háček-like mark for the long ē of vovēre (a typographic quirk, faithfully extracted). Mann alone separates it as *gʷoueiō, a minority view.\",\n  derivation_fa=\"لاتین vovēre «نذر کردن، پیمان بستن، وقف کردن» از ایتالیک آغازین *woɣʷeō و آن از صورت بالانده (o-grade) *h₁wogʷʰ-éye- از ریشهٔ *h₁wegʷʰ- است؛ اومبری vufru «نذری» هم‌ریشهٔ آن است. پوکورنی، والده‌ـ‌پوکورنی، واتکینز و دو وان همین را می‌گویند؛ ادعای نورایی درست است (علامت روی ě در کتاب نشانهٔ کشش ē است).\",\n  sources=[W_h1wegwh,W_vow],\n  ref_check=[{\"ref\":\"AHD\",\"status\":\"supports\",\"note\":\"Watkins s.v. wegʷh-: 'Suffixed o-grade form *wogʷh-eyo- in Latin vovēre, to pledge, vow' (AHD_watkins1985.txt l.1132).\"}],\n  consulted=[POK348,WLD110,IEC_eugh,\n   {\"src\":\"KLN\",\"where\":\"s.v. devote (KLN_1966 l.11169)\",\"stance\":\"supports\",\"note\":\"'L. devotus, pp. of devovere, \\\"to vow, to devote ...\\\", fr. de- and vovere, \\\"to vow\\\". See vote, vow'.\"}]),\n node(id=5,lang=\"English\",words=\"vote, devote, vow\",verdict=\"confirmed\",\n  derivation=\"vote (15th c.) < Lat. vōtum 'vow, wish' (neuter pp. of vovēre); vow (c. 1300) < Anglo-French/Old French vou, vo < Lat. vōtum — vote and vow are doublets; devote (1580s) < Lat. dēvōtus, pp. of dēvovēre 'to vow away, consecrate' (dē- + vovēre).\",\n  derivation_fa=\"انگلیسی vote از لاتین vōtum «نذر، آرزو» (صفت مفعولی vovēre)، vow از فرانسوی کهن vou / vo از همان vōtum (این دو واژه دوگانه‌اند)، و devote از لاتین dēvōtus، صفت مفعولی dēvovēre «وقف کردن». ادعای نورایی درست است.\",\n  sources=[W_vow],\n  ref_check=[{\"ref\":\"None\",\"status\":\"not_checked\",\"note\":\"Nourai gives no reference for this node.\"}],\n  consulted=[\n   {\"src\":\"KLN\",\"where\":\"s.v. vote, vow (KLN_1971 l.263998, 264032)\",\"stance\":\"supports\",\"note\":\"'vote, n. — ME., fr. L. votum (for *vovetom), \\\"a vow\\\", prop. neut. pp. of vovere'; 'vow, n. — ME. vou, vowe, fr. OF. vou'.\"},\n   {\"src\":\"SKT\",\"where\":\"s.v. VOW (SKT.txt l.21062)\",\"stance\":\"supports\",\"note\":\"'VOW, sb. (F.-L.) M.E. vou. — O.F. vou, vo (F. vœu), a vow. — L. uōtum, a vow'.\"}])]\n\ne1_nodes=[\n node(id=1,lang=\"Avestan\",words=\"vay 3; vaěiti; varaša\",verdict=\"disputed\",\n  derivation=\"Av. vaēiti- f. 'willow, withy' (V. 22.20 nava vaētayō 'nine withies') < Proto-Iranian *waitiš < PIE *wéh₁i-ti-s 'twisting, pliant (twig)' from *weh₁y- 'to twist, plait' — confirmed (cf. Lat. vītis 'vine', OE wīþig 'withy'). 'vay 3: twist' as an Avestan verb could not be found in Bartholomae; the Indo-Iranian verb is Skt. vyayati 'wraps'. Av. varəša- m. 'tree' (Pahl. gloss vēšag 'forest') is NOT from *wei-: it matches Skt. vṛkṣá- 'tree', and Hübschmann rejects even its link with NP bīše; so including varəša- under 'bend, twist' is wrong.\",\n  derivation_fa=\"اوستایی vaēiti- «بید، ترکهٔ بید» از ایرانی آغازین *waitiš و آن از هندواروپایی *wéh₁i-ti- «ترکهٔ نرم و پیچیدنی» از ریشهٔ *weh₁y- «پیچاندن، بافتن» است و درست است. اما varəša- «درخت» با سنسکریت vṛkṣá- هم‌ریشه است و به ریشهٔ «پیچاندن» ربطی ندارد؛ «vay 3» به معنای «پیچاندن» هم در بارتولومه یافت نشد. پس این گره بخشی درست و بخشی نادرست است.\",\n  sources=[W_bid,W_weh1itis,W_weh1y],\n  ref_check=[\n   {\"ref\":\"KLN:1749\",\"status\":\"supports\",\"note\":\"KLN s.v. withy (1971 ed. l.267869; p.1749 of 1966 ed., beyond the truncated 1966 OCR): 'OE. wīðig \\\"willow, willow twig\\\" ... and cogn. with Avestic vaēiti-, \\\"osier\\\", Gk. itéa \\\"willow\\\" ... L. vitis \\\"vine\\\"' — supports vaēiti- only.\"},\n   {\"ref\":\"ISS:42\",\"status\":\"not_checked\",\"note\":\"Khotanese Texts VI not available; substitute DKS (Bailey, Dictionary of Khotan Saka) leaf 317 s.v. bī 'willow': 'To Av. vaēiti- \\\"willow\\\": Vid. 22.20 nava vaētayō barat ... N.Pers. bēd' — supports vaēiti-.\"}],\n  consulted=[\n   {\"src\":\"BRT\",\"where\":\"col. 1309 s.v. vaētay-\",\"stance\":\"supports\",\"note\":\"'vaētay- f. \\\"Weide; Weidengerte\\\": nava vaētayō barat ... np. bēd, afg. vala; ai. vgl. vetasá- \\\"Rute\\\"'.\"},\n   {\"src\":\"BRT\",\"where\":\"col. 1379-1380 s.v. varəša-\",\"stance\":\"contradicts\",\"note\":\"'varəša- m. \\\"Baum\\\" ... ai. vṛkṣá- m. \\\"Baum\\\" ... Pü.: vēšak \\\"Wald\\\"' — cognate with Skt. vṛkṣá, not a *wei- derivative.\"},\n   {\"src\":\"POK\",\"where\":\"p. 1120-1122 s.v. u̯ei-1 (POK_full.txt l.89677)\",\"stance\":\"supports\",\"note\":\"'Avestan vaēiti- \\\"willow, Weidengerte\\\"' listed under the t-formant of u̯ei-1; no varəša-.\"},\n   {\"src\":\"WLD\",\"where\":\"Bd. I p. 226ff s.v. u̯ei- (leaf 235)\",\"stance\":\"supports\",\"note\":\"u̯ei- 'drehen, winden' with r- and t-formants (iris, wīr, vītis); no varəša-.\"},\n   {\"src\":\"AHD\",\"where\":\"s.v. wei-1 (l.1132-1135)\",\"stance\":\"partial\",\"note\":\"'wei-1. Also weiə-. To turn, twist ... Suffixed form *wei-ti- in Germanic *withi-, willow' — Iranian not cited.\"}]),\n node(id=2,lang=\"Pahlavi\",words=\"vět; vîsag, vîsak\",verdict=\"disputed\",\n  derivation=\"MP wēd [wyt] 'willow' (MacKenzie; Pahlavi gloss vēt for Av. vaēiti-) regularly continues *waiti- (intervocalic/final *t > d) — confirmed. MP wēšag [wyšk'] 'forest; reed-bed' (Nyberg 'reed, bunch of reeds — NP bēšah'; Mo'in: Pahl. vīšak, Sogd. vyšʾk) is real and is the source of NP bīše, but its derivation is unknown: Horn linked it to Av. varəša-, Hübschmann rejected that phonetically (positing OP *vaiša-), and Wiktionary leaves it open. No source connects it with *wei- 'twist', so the arrow from the root is unsupported.\",\n  derivation_fa=\"پهلوی wēd «بید» از *waiti- ایرانی باستان است (t پایانی در فارسی میانه به d بدل شده) و درست است. پهلوی wēšag «بیشه، نیزار» (سغدی vyšʾk) واژه‌ای واقعی و ریشهٔ «بیشه» است، اما ریشهٔ آن روشن نیست: هرن آن را با اوستایی varəša- سنجیده و هوبشمان از نظر آوایی رد کرده است؛ هیچ منبعی آن را به ریشهٔ *wei- «پیچاندن» نمی‌رساند. پس نیمی از ادعای نورایی درست و نیمی بی‌پشتوانه است.\",\n  sources=[W_bid,W_bishe],\n  ref_check=[\n   {\"ref\":\"BQT:338\",\"status\":\"partial\",\"note\":\"Mo'in's footnote 2 on بیشه, BQT p. 338 (leaf n558, vision file ocr/BQT/0338.vision.txt): 'اوستا varəsha (جنگل)، سانسکریت vrkshá (درخت) ... پهلوی vishak «بندهش ۱۸۹»، سغدی vîshâk ...' — gives the Pahlavi form and Av. varəša, but no link to a root 'twist'.\"},\n   {\"ref\":\"MON:58\",\"status\":\"not_checked\",\"note\":\"Print page of Mo'in's Farhang not mappable online; vajehyab entry for بید/بیشه only tags [په.].\"},\n   {\"ref\":\"SNS:287\",\"status\":\"not_found\",\"note\":\"SNS_pages.txt grep for wēd/wyt/wēšag/wyšk found no usable hit (OCR poor, page offset undetermined).\"},\n   {\"ref\":\"ISS:42\",\"status\":\"not_checked\",\"note\":\"Khotanese Texts VI not available; DKS s.v. bī cites 'Zor.P. ... vēt \\\"branch of willow\\\"' for the willow word only.\"}],\n  consulted=[\n   {\"src\":\"PHD\",\"where\":\"p. 90 (PHD_mackenzie.txt l.5307)\",\"stance\":\"supports\",\"note\":\"'wēd [wyt, N bēd] willow.'\"},\n   {\"src\":\"NYB\",\"where\":\"glossary (NYB_vol2_glossary.txt l.4097)\",\"stance\":\"partial\",\"note\":\"'vēšak [wyšk'] reed, bunch of reeds 93. — NP bēšah' — form confirmed, no etymology.\"},\n   {\"src\":\"HUB\",\"where\":\"no. 256 (HUB.txt l.1126)\",\"stance\":\"contradicts\",\"note\":\"'Np. bēša \\\"Wald\\\" (= ap. *vaiša) kann ich mit zd. varəša- ... lautlich nicht vereinigen.'\"},\n   {\"src\":\"HRN\",\"where\":\"no. 256 (HRN.txt l.2603-2607)\",\"stance\":\"partial\",\"note\":\"'bēše \\\"Wald, Dickicht\\\" ... aw. varəša- \\\"Wald\\\"; phlv. vēšak; ai. vṛkṣá- \\\"Baum\\\"' — Horn links to varəša-/vṛkṣá-, not to *wei-.\"}]),\n node(id=3,lang=\"Persian\",words=\"běd; bîšeh\",verdict=\"disputed\",\n  derivation=\"NP bēd/bīd بید 'willow' < MP wēd < Av. vaēiti- < PIE *wéh₁itis (initial w- > b- in New Persian, as in wād > bād; majhul ē > ī in Iranian Persian); dialect forms Gilaki bid, Natanzi vī, Mazandarani fek (Mo'in) — confirmed. NP bīše بیشه 'grove, thicket, reed-bed' < MP wēšag (with the same w- > b-), but its ultimate etymology is uncertain (Horn: Av. varəša-, Skt. vṛkṣá; Hübschmann: OP *vaiša-, rejecting varəša-; Wiktionary: possibly an areal word linked to Latvian mežs) and nothing ties it to *wei- 'twist' — disputed. The Hāfez verse quoted (دل صنوبریم همچو بید لرزانست) illustrates bēd only.\",\n  derivation_fa=\"«بید» از فارسی میانهٔ wēd و اوستایی vaēiti- و هندواروپایی *wéh₁itis «ترکهٔ پیچیدنی» است؛ w آغازین در فارسی نو به b بدل شده (چنان‌که در «باد») و گویش‌ها صورت‌های vī و bid و fek دارند (معین، حاشیهٔ برهان). این بخش درست است. «بیشه» از پهلوی wēšag است، ولی ریشهٔ دورترش روشن نیست (هرن آن را به اوستایی varəša- «درخت، جنگل» می‌رساند و هوبشمان رد می‌کند) و هیچ پیوندی با ریشهٔ «پیچاندن» ندارد؛ پس این بخش از ادعای نورایی پذیرفتنی نیست.\",\n  sources=[W_bid,W_bishe,W_weh1itis,M_bid,M_bishe],\n  ref_check=[\n   {\"ref\":\"BQT:332\",\"status\":\"supports\",\"note\":\"BQT p. 332 (leaf n552; ocr/BQT/0332.vision.txt), Mo'in's footnote 2 on بید: 'گیلکی bid ... نطنزی vî ... مازندرانی کنونی fek ... پهلوی vêt، اوستا vaêiti «اسفا ۱: ۲ ص ۷۶»'.\"},\n   {\"ref\":\"BQT:338\",\"status\":\"partial\",\"note\":\"BQT p. 338 (leaf n558; ocr/BQT/0338.vision.txt), footnote 2 on بیشه: 'اوستا varəsha (جنگل)، سانسکریت vrkshá (درخت) ... پهلوی vishak' — links bīše to varəša-/vṛkṣá-, not to a root 'twist'.\"},\n   {\"ref\":\"SNS:287\",\"status\":\"not_found\",\"note\":\"No hit for wēd/wēšag in SNS_pages.txt OCR.\"},\n   {\"ref\":\"ISS:42\",\"status\":\"not_checked\",\"note\":\"Khotanese Texts VI not available; DKS s.v. bī: 'To Av. vaēiti- \\\"willow\\\" ... N.Pers. bēd, Pašto wala' (ISS_alt_DKS.txt l.5212) supports bēd.\"}],\n  consulted=[\n   {\"src\":\"HRN\",\"where\":\"no. 251 (HRN.txt l.2568-2571)\",\"stance\":\"supports\",\"note\":\"'251. bēd Weide ... aw. vaēiti- \\\"Weide\\\"; phlv. vēt; ai. vergl. vetasá-'.\"},\n   {\"src\":\"HRN\",\"where\":\"no. 256 (HRN.txt l.2603)\",\"stance\":\"partial\",\"note\":\"'bēše \\\"Wald, Dickicht\\\" ... aw. varəsa- \\\"Wald\\\"; phlv. vēšak; ai. vṛkṣá- \\\"Baum\\\"'.\"},\n   {\"src\":\"HUB\",\"where\":\"nos. 251, 256 and p. 'bēd = zd. vaēiti-' (HUB.txt l.1110, 1126, 5468)\",\"stance\":\"partial\",\"note\":\"'bēd \\\"Weide\\\" = zd. vaēiti-'; but 'Np. bēša \\\"Wald\\\" (= ap. *vaiša) kann ich mit zd. varəša- lautlich nicht vereinigen'.\"},\n   {\"src\":\"BQT\",\"where\":\"pp. 332, 338\",\"stance\":\"partial\",\"note\":\"bēd < Pahl. vêt, Av. vaêiti; bīše with Av. varəša, Pahl. vishak — see ref_check.\"},\n   {\"src\":\"MON\",\"where\":\"vajehyab.com/moein/بید ; /بیشه\",\"stance\":\"silent\",\"note\":\"'بید [په.] (اِ.) درختی است از تیرة بیدها'; 'بیشه (ش ِ) [په.] (اِ.) ۱- نیزار، نیستان ۲- جنگل کوچک' — Pahlavi origin only.\"},\n   {\"src\":\"ARY\",\"where\":\"ARY_latin_index_pages.txt / ARY_pages.txt grep WILLOW, بید, بیشه\",\"stance\":\"silent\",\"note\":\"No Aryanpur entry for بید or بیشه found.\"},\n   {\"src\":\"PHD\",\"where\":\"p. 90\",\"stance\":\"supports\",\"note\":\"'wēd [wyt, N bēd] willow.'\"}]),\n node(id=4,lang=\"Germanic\",words=\"wi-ra\",verdict=\"confirmed\",\n  derivation=\"Proto-Germanic *wīra- 'wire, twisted metal thread' < PIE *wih₁-ro- / *weh₁i-ro- 'something twisted' from *weh₁y- 'to twist' (r-formant; cf. OIr. fiar, Welsh gŵyr 'bent, crooked'); continued in OE wīr, MLG wīre, Old Norse víra-virki 'filigree'.\",\n  derivation_fa=\"ژرمنی آغازین *wīra- «مفتول، رشتهٔ تابیده» از هندواروپایی *wih₁-ro- «چیز تابیده» از ریشهٔ *weh₁y- «پیچاندن» است (با پسوند r-؛ هم‌ریشه با ایرلندی کهن fiar «کج»). ادعای نورایی درست است.\",\n  sources=[W_weh1y,W_wire],\n  ref_check=[{\"ref\":\"AHD\",\"status\":\"supports\",\"note\":\"Watkins s.v. wei-1: 'Germanic suffixed form *wi-ra-, *wei-ra- in Old English wīr, wire: WIRE.'\"}],\n  consulted=[\n   {\"src\":\"POK\",\"where\":\"p. 1122, u̯ei-1 F. 'With r-formant' (POK_full.txt l.89661ff)\",\"stance\":\"supports\",\"note\":\"'Old English wīr \\\"Metalldraht, gewundener Schmuck\\\" ... Germanic wīra-, das wegen gr. Fῖρις wohl auf idg. *u̯ī-ro- zurückgeht'.\"},\n   {\"src\":\"WLD\",\"where\":\"Bd. I p. 226 (leaf 235)\",\"stance\":\"supports\",\"note\":\"'Mit r-Formantien: Gr. ἶρις „Regenbogen\\\" ... ags. wīr „Metalldraht, gewundener Schmuck\\\", mnd. wīre „Metalldraht\\\"'.\"},\n   {\"src\":\"KLN\",\"where\":\"s.v. wire (KLN_1971 l.267547)\",\"stance\":\"supports\",\"note\":\"'fr. OE. wīr, rel. to ON. *vīrr in vīravirki ... fr. I.-E. base *wei-, \\\"to bend, twist\\\"'.\"}]),\n node(id=5,lang=\"English\",words=\"wire\",verdict=\"confirmed\",\n  derivation=\"English wire < Middle English wir, wyre < Old English wīr 'wire, metal thread, wire ornament' < Proto-Germanic *wīraz; the long ī was diphthongised in the Great Vowel Shift (wīr > wire /waɪə/).\",\n  derivation_fa=\"انگلیسی wire از انگلیسی میانه wir و انگلیسی کهن wīr «مفتول، زیور مفتولی» از ژرمنی *wīraz است؛ ī کشیده در دگرگونی بزرگ واکه‌ها به ai بدل شده است. درست است.\",\n  sources=[W_wire],\n  ref_check=[{\"ref\":\"None\",\"status\":\"not_checked\",\"note\":\"Nourai gives no reference for this node.\"}],\n  consulted=[\n   {\"src\":\"KLN\",\"where\":\"s.v. wire (KLN_1971 l.267547)\",\"stance\":\"supports\",\"note\":\"'wire, n. — ME. wyre, wir, fr. OE. wir'.\"},\n   {\"src\":\"AHD\",\"where\":\"s.v. wei-1\",\"stance\":\"supports\",\"note\":\"'Old English wīr, wire: WIRE'.\"}]),\n node(id=6,lang=\"Greek\",words=\"iris\",verdict=\"plausible\",\n  derivation=\"Gk. ἶρις (Aeolic/inscriptional Ϝῖρις, gen. ἴριδος) 'rainbow', personified as the goddess Iris, has traditionally been derived from *wī-ri- 'something bent/twisted' (bow-shaped) from *wei- (Pokorny, Walde-Pokorny, Klein, AHD 'probably'), cognate with Germanic *wīra-. Beekes and Furnée object that the root is *weh₁y- (which should not give *wīr-), that the ε/ι variation and the -ιδ- stem look Pre-Greek, and treat it as a substrate word; so the link is traditional but not secure.\",\n  derivation_fa=\"یونانی ἶρις (Ϝῖρις) «رنگین‌کمان» و نام ایزدبانوی پیام‌رسان، در ریشه‌شناسی سنتی (پوکورنی، کلاین، واتکینز) از *wī-ri- «چیز خمیده» از ریشهٔ *wei- «خم کردن، پیچاندن» دانسته شده است. اما بیکس و فورنه به دلایل آوایی (صورت امروزی ریشه *weh₁y- و نوسان ε/ι و ستاک -ιδ-) آن را واژه‌ای پیشایونانی می‌دانند؛ پس ادعای نورایی با احتیاط پذیرفتنی است.\",\n  sources=[W_irisgk,W_weh1y],\n  ref_check=[{\"ref\":\"AHD\",\"status\":\"supports\",\"note\":\"Watkins s.v. wei-1: 'Suffixed form *wi-ri- probably in Greek iris, rainbow, and Iris, rainbow goddess' (note 'probably').\"}],\n  consulted=[\n   {\"src\":\"POK\",\"where\":\"p. 1122 (POK_full.txt l.89659)\",\"stance\":\"supports\",\"note\":\"'Gr. ἶρις \\\"rainbow\\\" (Fῖρις) = Ἶρις and Εἶρις ... the as messenger of the gods personified rainbow'.\"},\n   {\"src\":\"WLD\",\"where\":\"Bd. I p. 226 (leaf 235)\",\"stance\":\"supports\",\"note\":\"'Gr. ἶρις „Regenbogen\\\" (Fῖρις = Ἶρις und Εἶρις)' under u̯ei- with r-formant.\"},\n   {\"src\":\"KLN\",\"where\":\"s.v. iris (KLN_1966 l.19892)\",\"stance\":\"supports\",\"note\":\"'L. iris, fr. Gk. ἶρις, \\\"the rainbow\\\", orig. form *Fῖρις, lit. \\\"something bent or curved\\\", fr. I.-E. base *wei-, \\\"to bend, twist\\\"'.\"}]),\n node(id=7,lang=\"English\",words=\"iris\",verdict=\"confirmed\",\n  derivation=\"English iris (late 14th c., the plant; 1520s, the eye membrane, named for its colours) < Latin īris < Greek ἶρις 'rainbow'; the Greek→English link via Latin is certain whatever the ultimate origin of the Greek word.\",\n  derivation_fa=\"انگلیسی iris (گل زنبق و عنبیهٔ چشم، به سبب رنگارنگی) از لاتین īris و آن از یونانی ἶρις «رنگین‌کمان» گرفته شده است؛ این وام‌گیری مسلم است، هرچند ریشهٔ دور واژهٔ یونانی محل بحث است.\",\n  sources=[W_irisgk],\n  ref_check=[{\"ref\":\"None\",\"status\":\"not_checked\",\"note\":\"Nourai gives no reference for this node.\"}],\n  consulted=[\n   {\"src\":\"KLN\",\"where\":\"s.v. iris (KLN_1966 l.19892)\",\"stance\":\"supports\",\"note\":\"'iris, n., 1) the rainbow; 2) the colored portion of the eye. — L. iris, fr. Gk. ἶρις'.\"},\n   {\"src\":\"AHD\",\"where\":\"s.v. wei-1\",\"stance\":\"supports\",\"note\":\"'Greek iris, rainbow ... IRIS'.\"}])]\n\nout={\"pdf_page\":532,\"book_page\":502,\"verified_by\":\"claude-opus-5\",\"verified_on\":\"2026-10-16\",\"entries\":[\n {\"entry\":0,\"root\":\"Wegwh, Ewegwh, Eueguh\",\"verdict\":\"confirmed\",\n  \"modern_form\":\"PIE *h₁wegʷʰ- (zero/full grade *h₁(e)ugʷʰ-) 'to speak solemnly, vow, pray'\",\n  \"note\":\"Pokorny 348 eu̯egʷh- 'feierlich sprechen, geloben'; Watkins wegʷh- (also eugʷh-) 'to preach, speak solemnly'. Root, label and gloss correct. The book prints 'Eueguh' (= Euegʷh with superscript w rendered as u); the chart text's 'Euegh' is just a shortening. Within the entry: Av. aog- and Lat. vovēre are correct descendants (Nourai's 'connection doubtful' note on aog- is unnecessary), but the forms he labels Old Persian are Avestan, Persian pāsox belongs to *pati-sahwa- (*ḱens-, his own alternative 'Kâs 2'), and Av. duš-ūxta- belongs to vac- (*wekʷ-). The Avestan box in the book also has an arrow to an empty box (nothing to verify).\",\n  \"note_fa\":\"ریشهٔ هندواروپایی آغازین *h₁wegʷʰ- «با سخن رسمی و آیینی گفتن، نذر کردن» (پوکورنی ۳۴۸؛ واتکینز) درست است و اوستایی aog- و لاتین vovēre (و از آن انگلیسی vow، vote، devote) از آن‌اند. اما «پاسخ» از این ریشه نیست و از *pati-sahwa- (ریشهٔ *ḱens- «اعلام کردن») است، صورت‌هایی که نورایی «پارسی باستان» خوانده در واقع اوستایی‌اند، و duš-ūxta- «بد گفته» از فعل vac- «گفتن» است.\",\n  \"sources\":[W_h1wegwh,W_vow],\n  \"ref_check\":[{\"ref\":\"POK:348\",\"status\":\"supports\",\"note\":\"POK p. 348 (POK_full.txt l.29030-29069): 'Root / lemma: eu̯egʷh- ... Meaning: to praise, worship ... Latin voveō ... eug^h-: Avestan aog- ... Page(s): 348'.\"}],\n  \"consulted\":[WLD110,AHD_wegwh,IEC_eugh,SYN1256],\n  \"nodes\":e0_nodes},\n {\"entry\":1,\"root\":\"Wei 1\",\"verdict\":\"confirmed\",\n  \"modern_form\":\"PIE *weh₁y- (older *wei-1, *u̯ei-) 'to turn, twist, plait'\",\n  \"note\":\"Pokorny 1120-1122 u̯ei-1 'drehen, biegen' with Av. vaēiti-, Gk. ἶρις, Germ. *wīra-; Watkins wei-1 'to turn, twist'. Root confirmed. Problems within the entry: Av. varəša- 'tree' (= Skt. vṛkṣá) and MP wēšag / NP bīše 'forest, thicket' have no established link with this root (Hübschmann even rejects varəša- > bīše); 'vay 3: twist' is not found as an Avestan verb in Bartholomae. Greek iris is the traditional but contested (Beekes: Pre-Greek) member.\",\n  \"note_fa\":\"ریشهٔ هندواروپایی آغازین *weh₁y- (*wei- در پوکورنی ۱۱۲۰) «پیچاندن، تابیدن، بافتن» درست است و اوستایی vaēiti-، پهلوی wēd و فارسی «بید»، ژرمنی *wīra- (انگلیسی wire) از آن‌اند؛ یونانی iris در ریشه‌شناسی سنتی از همین ریشه است ولی بیکس آن را پیشایونانی می‌داند. اما «بیشه» و پهلوی wēšag و اوستایی varəša- «درخت» به این ریشه ربطی ندارند.\",\n  \"sources\":[W_weh1y,W_weh1itis],\n  \"ref_check\":[{\"ref\":\"POK:1120\",\"status\":\"supports\",\"note\":\"POK 'Root / lemma: u̯ei-1, u̯eiə- : u̯ī- ... Page(s): 1120-1122' with 'Avestan vaēiti- willow', 'Gr. ἶρις rainbow', 'OE wīr' (POK_full.txt l.89640-89715).\"}],\n  \"consulted\":[\n   {\"src\":\"WLD\",\"where\":\"Bd. I p. 226ff (leaf 235)\",\"stance\":\"supports\",\"note\":\"u̯ei- with r-formants: 'Gr. ἶρις „Regenbogen\\\" ... ags. wīr „Metalldraht, gewundener Schmuck\\\"'.\"},\n   {\"src\":\"AHD\",\"where\":\"s.v. wei-1 (AHD_watkins1985.txt l.1132-1135)\",\"stance\":\"supports\",\"note\":\"'wei-1. Also weiə-. To turn, twist; with derivatives referring to suppleness or binding ... [Pok. 1. wei- 1120.]'\"},\n   {\"src\":\"KLN\",\"where\":\"s.v. withy, wire\",\"stance\":\"supports\",\"note\":\"'I.-E. base *wei-, \\\"to bend, twist\\\"' with Avestic vaēiti- 'osier'.\"}],\n  \"nodes\":e1_nodes}]}\njson.dump(out,open('/home/sfmqrb/git/rishe-private/data/verification/page-532.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)\nPYEOF\ncd /home/sfmqrb/git/rishe-private && python3 /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/build-532.py && python3 -m json.tool data/verification/page-532.json >/dev/null && python3 tools/verify_check.py 532"
}
```


### [2026-10-16T05:23:57.373Z] TOOL RESULT

```
nodes verified: 12/12
node verdicts: {'plausible': 2, 'disputed': 5, 'confirmed': 5}
root verdicts: {'confirmed': 2}
ref checks: {'not_checked': 9, 'supports': 8, 'not_found': 3, 'partial': 2}
books consulted: {'supports': 27, 'silent': 6, 'contradicts': 8, 'partial': 7} | by book: {'KLN': 6, 'BRT': 5, 'POK': 5, 'WLD': 5, 'HRN': 4, 'HUB': 3, 'PHD': 3, 'AHD': 3, 'CHEUNG': 2, 'SYN': 2, 'NYB': 2, 'ARY': 2, 'MON': 2, 'KNT': 1, 'IEC': 1, 'SKT': 1, 'BQT': 1}
```


## [2026-10-16T05:24:03.517Z] TOOL CALL #88: Bash

```json
{
 "command": "S=/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/build-532.py && sed -i -e 's/\"where\":\"p\\. 64 (PHD_mackenzie/\"where\":\"(PHD_mackenzie/' -e 's/\"where\":\"p\\. 90 (PHD_mackenzie/\"where\":\"(PHD_mackenzie/' -e 's/\"where\":\"p\\. 90\"/\"where\":\"PHD_mackenzie.txt l.5307\"/' -e 's/\"where\":\"no\\. 275, p\\. 64\"/\"where\":\"no. 275 (HRN.txt l.2724)\"/' -e 's/col\\. ~1838 s\\.v\\./col. ~1817 s.v./' $S && python3 $S && python3 tools/verify_check.py 532 | grep -c PROBLEM"
}
```


### [2026-10-16T05:24:04.005Z] TOOL RESULT

```
0
```


## [2026-10-16T05:24:14.558Z] TOOL CALL #89: SubagentHandback

```json
{
 "message": "Page 532 (book page 502) is verified. I wrote `/home/sfmqrb/git/rishe-private/data/verification/page-532.json`; `python3 tools/verify_check.py 532` reports 12/12 nodes and 0 PROBLEM lines.\n\n**Verdicts:** both roots are confirmed (Wegwh = PIE *h₁wegʷʰ-, Pokorny 348; Wei 1 = PIE *weh₁y-, Pokorny 1120). Nodes: 5 confirmed, 2 plausible, 5 disputed, 0 transcription_suspect.\n\n**Disputed:**\n- **Wegwh #2, pâsox پاسخ:** it comes from Middle Persian passox, from *pati-sahwa- (Avestan saŋh-, PIE *ḱens- \"proclaim\"), not from Avestan aog-. Horn 275, Hübschmann, Cheung p.334, Aryanpur and Wiktionary all say this. Nourai's own alternative (\"see Root Kâs 2\") is the right one.\n- **Wegwh #3, duš-uxta:** Avestan dužūxta-/hūxta- is built on uxta-, the past participle of vac- (PIE *wekʷ-), not of aog-. The aog-/aojaite/aogədā forms themselves are confirmed.\n- **Wei 1 #1, varaša:** Avestan varəša- \"tree\" matches Sanskrit vṛkṣá (Bartholomae) and has nothing to do with *wei- \"twist\". \"vay 3: twist\" was not found in Bartholomae. vaēiti- \"willow\" is confirmed.\n- **Wei 1 #2, vîsag (Middle Persian wēšag):** the word is real (Nyberg, Mo'in), but no source links it to *wei-, and Hübschmann rejects varəša- as its source. vět (wēd) is confirmed.\n- **Wei 1 #3, bîšeh بیشه:** same problem; its origin is uncertain and unconnected to *wei-. běd بید is confirmed (Mo'in's note in Borhan-e Qate' p.332, Horn 251, MacKenzie).\n\n**Plausible:**\n- **Wegwh #1:** the forms \"aok / paiti-aok\" are Avestan (Bartholomae cols. 37–38), not Old Persian, which has only θah- \"to say\". Their link to the root is actually secure, so Nourai's \"connection doubtful\" note is unnecessary.\n- **Wei 1 #6, Greek iris:** the derivation from *wei- is the traditional view, but Beekes and Furnée treat the word as Pre-Greek.\n\n**Extraction errors:** none. The printed page shows \"Eueguh\", which the JSON copies faithfully; the chart text's \"Euegh\" is just a shortened form. The book prints \"vověre\" for Latin vovēre (a typographic quirk, extracted faithfully). The book also draws an arrow from the Avestan box to an empty box, so there was nothing to verify there.\n\n**Files added during the check:**\n- Borhan-e Qate' vol. 1 pages 332 and 338, read from the images: `/home/sfmqrb/git/rishe-private/data/verification/sources/refs/ocr/BQT/0332.jpg`, `0332.vision.txt`, `0338.jpg`, `0338.vision.txt`.\n- Wiktionary and vajehyab (Mo'in) pages, archived with `fetch_source.py`. The Etymonline fetches failed, so I did not cite them."
}
```


### [2026-10-16T05:24:14.998Z] TOOL RESULT

```
{"success":true,"message":"Report delivered to your caller."}
```
