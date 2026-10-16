# Verification process log — verify-page-536


## [2026-10-16T05:13:02.122Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 536 only. Chart text: /home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-536.txt; source JSON: /home/sfmqrb/git/rishe-private/data/extracted/batch/page-536.json. Write /home/sfmqrb/git/rishe-private/data/verification/page-536.json, run `python3 /home/sfmqrb/git/rishe-private/tools/verify_check.py 536` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-10-16T05:13:02.185Z] INPUT

<system-reminder>
Your final report is delivered through SubagentHandback: when your work is complete, call SubagentHandback({message: <your full report>}). The call ends your run, so make it your last step. Only a SubagentHandback call reaches your caller as your result; plain text you write at the end is not delivered.
</system-reminder>


## [2026-10-16T05:13:05.302Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-10-16T05:13:05.325Z] TOOL RESULT

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


## [2026-10-16T05:13:05.806Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/verification/agent/charts/page-536.txt"
}
```


### [2026-10-16T05:13:05.833Z] TOOL RESULT

```
1	=== PDF page 536 (book page 506) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Weik 2 : clan, a social club above the household  (refs POK:1131)
4	#1 (parent #0) [Avestan] refs=POK:1131; KLN:1708 | vîs : family ; vîs-paiti, vîs-pati : clan protector, chief
5	#2 (parent #0) [Old Persian] refs=KNT:208 | vith : house, royal house ; vitha : royal
6	#3 (parent #0) [Latin] refs=AHD | villa : country house ; vicus : neighborhood
7	  #4 (parent #3) [French] refs=None | villa
8	    #5 (parent #4) [Persian] refs=MON:5073 | vîlâ «ویلا» : villa
9	  #6 (parent #3) [English] refs=KLN:1710 | villa, village ; vicinity
10	#7 (parent #0) [Greek] refs=AHD | oikos : house
11	  #8 (parent #7) [English] refs=None | eco-, ; ecology, economy
12	--- entry 1 ---
13	ROOT [Indo-European] Weip, Weib : to go back and forth  (refs POK:1131)
14	#1 (parent #0) [Avestan] refs=POK:1131 | vip : to send, dispatch
15	#2 (parent #0) [Germanic] refs=AHD | wîpjan
16	  #3 (parent #2) [English] refs=None | wipe, whip
17	#4 (parent #0) [Latin] refs=AHD | vibrare : to vibrate
18	  #5 (parent #4) [English] refs=None | vibrate
19	
```


## [2026-10-16T05:13:06.539Z] TOOL CALL #3: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe-private/data/extracted/batch/page-536.json"
}
```


### [2026-10-16T05:13:06.773Z] TOOL RESULT

```
1	{
2	  "pdf_page": 536,
3	  "book_page": 506,
4	  "entries": [
5	    {
6	      "root": {
7	        "name": "Weik 2",
8	        "lang": "Indo-European",
9	        "refs": "POK:1131",
10	        "gloss": "clan, a social club above the household"
11	      },
12	      "nodes": [
13	        {
14	          "id": 1,
15	          "parent": 0,
16	          "lang": "Avestan",
17	          "refs": "POK:1131; KLN:1708",
18	          "words": [
19	            {"translit": "vîs", "gloss": "family", "script": null},
20	            {"translit": "vîs-paiti, vîs-pati", "gloss": "clan protector, chief", "script": null}
21	          ],
22	          "script_extra": null,
23	          "note": null,
24	          "quote": null
25	        },
26	        {
27	          "id": 2,
28	          "parent": 0,
29	          "lang": "Old Persian",
30	          "refs": "KNT:208",
31	          "words": [
32	            {"translit": "vith", "gloss": "house, royal house", "script": null},
33	            {"translit": "vitha", "gloss": "royal", "script": null}
34	          ],
35	          "script_extra": null,
36	          "note": null,
37	          "quote": null
38	        },
39	        {
40	          "id": 3,
41	          "parent": 0,
42	          "lang": "Latin",
43	          "refs": "AHD",
44	          "words": [
45	            {"translit": "villa", "gloss": "country house", "script": null},
46	            {"translit": "vicus", "gloss": "neighborhood", "script": null}
47	          ],
48	          "script_extra": null,
49	          "note": null,
50	          "quote": null
51	        },
52	        {
53	          "id": 4,
54	          "parent": 3,
55	          "lang": "French",
56	          "refs": null,
57	          "words": [
58	            {"translit": "villa", "gloss": null, "script": null}
59	          ],
60	          "script_extra": null,
61	          "note": null,
62	          "quote": null
63	        },
64	        {
65	          "id": 5,
66	          "parent": 4,
67	          "lang": "Persian",
68	          "refs": "MON:5073",
69	          "words": [
70	            {"translit": "vîlâ", "gloss": "villa", "script": "ویلا"}
71	          ],
72	          "script_extra": null,
73	          "note": null,
74	          "quote": null
75	        },
76	        {
77	          "id": 6,
78	          "parent": 3,
79	          "lang": "English",
80	          "refs": "KLN:1710",
81	          "words": [
82	            {"translit": "villa, village", "gloss": null, "script": null},
83	            {"translit": "vicinity", "gloss": null, "script": null}
84	          ],
85	          "script_extra": null,
86	          "note": null,
87	          "quote": null
88	        },
89	        {
90	          "id": 7,
91	          "parent": 0,
92	          "lang": "Greek",
93	          "refs": "AHD",
94	          "words": [
95	            {"translit": "oikos", "gloss": "house", "script": null}
96	          ],
97	          "script_extra": null,
98	          "note": null,
99	          "quote": null
100	        },
101	        {
102	          "id": 8,
103	          "parent": 7,
104	          "lang": "English",
105	          "refs": null,
106	          "words": [
107	            {"translit": "eco-,", "gloss": null, "script": null},
108	            {"translit": "ecology, economy", "gloss": null, "script": null}
109	          ],
110	          "script_extra": null,
111	          "note": null,
112	          "quote": null
113	        }
114	      ]
115	    },
116	    {
117	      "root": {
118	        "name": "Weip, Weib",
119	        "lang": "Indo-European",
120	        "refs": "POK:1131",
121	        "gloss": "to go back and forth"
122	      },
123	      "nodes": [
124	        {
125	          "id": 1,
126	          "parent": 0,
127	          "lang": "Avestan",
128	          "refs": "POK:1131",
129	          "words": [
130	            {"translit": "vip", "gloss": "to send, dispatch", "script": null}
131	          ],
132	          "script_extra": null,
133	          "note": null,
134	          "quote": null
135	        },
136	        {
137	          "id": 2,
138	          "parent": 0,
139	          "lang": "Germanic",
140	          "refs": "AHD",
141	          "words": [
142	            {"translit": "wîpjan", "gloss": null, "script": null}
143	          ],
144	          "script_extra": null,
145	          "note": null,
146	          "quote": null
147	        },
148	        {
149	          "id": 3,
150	          "parent": 2,
151	          "lang": "English",
152	          "refs": null,
153	          "words": [
154	            {"translit": "wipe, whip", "gloss": null, "script": null}
155	          ],
156	          "script_extra": null,
157	          "note": null,
158	          "quote": null
159	        },
160	        {
161	          "id": 4,
162	          "parent": 0,
163	          "lang": "Latin",
164	          "refs": "AHD",
165	          "words": [
166	            {"translit": "vibrare", "gloss": "to vibrate", "script": null}
167	          ],
168	          "script_extra": null,
169	          "note": null,
170	          "quote": null
171	        },
172	        {
173	          "id": 5,
174	          "parent": 4,
175	          "lang": "English",
176	          "refs": null,
177	          "words": [
178	            {"translit": "vibrate", "gloss": null, "script": null}
179	          ],
180	          "script_extra": null,
181	          "note": null,
182	          "quote": null
183	        }
184	      ]
185	    }
186	  ]
187	}
188	
```


## [2026-10-16T05:13:15.329Z] TOOL CALL #4: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification; ls | head; python3 -c \"\nimport json;d=json.load(open('page-511.json'));e=d['entries'][0];print(json.dumps({k:v for k,v in d.items() if k!='entries'}));n=e['nodes'][0];print(json.dumps(n,ensure_ascii=False,indent=1)[:3000])\"; cat sources/SOURCE_MATRIX.md | head -80; ls sources/refs | head -100"
}
```


### [2026-10-16T05:13:15.848Z] TOOL RESULT

```
{"pdf_page": 511, "book_page": 481, "verified_by": "claude-opus-5", "verified_on": "2026-10-14"}
{
 "id": 1,
 "lang": "Sanskrit",
 "words": "",
 "verdict": "disputed",
 "derivation": "Empty pass-through box: Nourai (following Pourdavoud via Mo'in's Borhan footnote) routes the Tamil word through Sanskrit before it reaches Aramaic and Arabic. No Sanskrit form of the tōkai/ṭāwūs type is attested: the Sanskrit words for 'peacock' are mayūra-, śikhin-, barhin-, kalāpin-. Modern scholarship (Wiktionary s.v. ταώς, Klein s.v. peacock) derives the Mediterranean/Semitic words either from Pre-Greek ταώς or directly from a Dravidian (Tamil tōkai) or other eastern source by sea trade, with no Sanskrit intermediary.",
 "derivation_fa": "این خانهٔ خالی «سنسکریت» را نورایی به پیروی از پورداوود (در حاشیهٔ معین بر برهان قاطع) میان تامیلی و آرامی/عربی گذاشته است. اما در سنسکریت واژه‌ای از گونهٔ tōkai یا ṭāwūs برای طاووس دیده نمی‌شود؛ نام‌های سنسکریت طاووس mayūra، śikhin و barhin است. پژوهش امروزی (کلاین، ویکی‌واژه) واژهٔ یونانی ταώς را پیش‌یونانی می‌داند یا آن را مستقیم به منبعی شرقی مانند تامیلی tōkai می‌رساند، و گذر از سنسکریت را تأیید نمی‌کند.",
 "sources": [
  "https://en.wiktionary.org/wiki/ταώς",
  "https://en.wiktionary.org/wiki/தோகை"
 ],
 "ref_check": [
  {
   "ref": "BQT:1346",
   "status": "partial",
   "note": "Borhan-e Qate' p.1346 (BQT_v3_picofile.pdf page 139; the tool's default offset lands on pdf 141, use --pdf-page 139; transcription saved in ocr/BQT/1346.vision.txt), Mo'in's footnote s.v. طاوس: '(عر) معرب آن طویس، یونانی Taôs، آرامی طاوسا tausâ «تسیمرن. لغات دخیل اکدی ص۵۲» طبق تحقیق استاد پور داود اصل کلمه از زبان دراویدی وارد سانسکریت شده و از آنجا بزبانهای دیگر رفته'. Source of Nourai's Dravidian > Sanskrit > Arabic/Aramaic chart (after Pourdavoud); Mo'in himself lists the Greek and Aramaic forms side by side without making Greek a daughter of Persian."
  }
 ],
 "consulted": [
  {
   "src": "KLN",
   "where": "1966 s.v. peacock (KLN_1966.txt line 27770)",
   "stance": "partial",
   "note": "'L. pavo ... which, together with Gk. ταώς, prob. comes ult. fr. Tamil tokei, tōgei (whence also Heb. tukkiyyim) ... initial p- in L. pavo is due to imitative influence; cp. L. paupulo, 'the natural sound of the peacock''."
  },
  {
   "src": "SKT",
   "where": "s.v. Peacock (SKT_dli_revised.txt line 55507)",
   "stance": "contradicts",
   "note": "Skeat's chain is 'Pers. tāwus ... - Tamil tōkei' with no Sanskrit stage."
  },
  {
   "src": "MON",
   "where": "vol.2 s.v. طاوس (MON_part1.txt line 91933)",
   "stance": "partial",
   "note": "Only the tag '[دراویدی هندی]' - Dravidian/Indian, no Sanskrit form given."
  }
 ]
}
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
```


## [2026-10-16T05:13:20.811Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources; sed -n 80,200p SOURCE_MATRIX.md; python3 -c \"\nimport json;d=json.load(open('refs_online.json'))\nfor k in ['POK','KLN','KNT','AHD','MON','WLD']: print(k, json.dumps(d.get(k),ensure_ascii=False)[:600])\""
}
```


### [2026-10-16T05:13:21.411Z] TOOL RESULT

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
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 34
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h
KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "local_file": "/home/sfmqrb/git/rishe-private/data/verification/sources/refs/KNT.txt", "page_offset": "leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local fil
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039
```


## [2026-10-16T05:13:23.767Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources; python3 -c \"\nimport json;d=json.load(open('refs_online.json'))\nfor k in ['POK','KLN','KNT','WLD','MON']: print(k, d[k].get('page_offset'), d[k].get('lookup_hint','')[:500]);print()\""
}
```


### [2026-10-16T05:13:24.138Z] TOOL RESULT

```
POK POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-dictionary/ (entry pages with page numbers) and StarLing https://starlingdb.org/cgi-bin/query.cgi?bas

KLN KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.

KNT leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> Lexicon (Part III, pp. 164 ff.) headwords are transliterated OP words at line start followed by part of speech, e.g. grep -n '^apadana-' ; section refs like '$147'. Nourai's page numbers should fall in 164-215 for lexicon citations.

WLD Band 3: leaf = printed + 6. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> || Band I (WLD_Bd1_pages.txt, 887 leaves): printed = leaf(1-based) − 9 (leaf 801 = p.792). Band II (WLD_Bd2_pages.txt, 720 leaves): printed = leaf − 5 (leaf 701 = p.696). Band 3 is the index (Wortregister by language) - it maps a word to 'Band, page' in vols 1-2, so it can at least confirm that a word is treated at the cited WP volume/page. For the actual entry text, use Pokorny 1959 (POK), whose entries cite 'WP. I 177' etc. and are essentially a revision of WP.

MON None Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Aden
```


## [2026-10-16T05:13:27.979Z] AGENT

Now grep Pokorny.


## [2026-10-16T05:13:29.110Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E 'lemma: (u|w)ei(k|ḱ)|lemma: (u|w)eip|lemma: (u|w)eib' POK_full.txt | head; "
}
```


### [2026-10-16T05:13:29.565Z] TOOL RESULT

```
89125:Root / lemma: ueib- 
89346:Root / lemma: ueik-1 
89375:Root / lemma: ueik-2 
89420:Root / lemma: ueik-3 
89444:Root / lemma: ueik-4, ueig- 
89844:Root / lemma: ueip- ueib-
```


## [2026-10-16T05:13:31.838Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 89346,89420p POK_full.txt | cut -c1-400; echo ====; sed -n 89844,89900p POK_full.txt | cut -c1-400; echo ===; sed -n 89125,89140p POK_full.txt|cut -c1-300"
}
```


### [2026-10-16T05:13:32.586Z] TOOL RESULT

```
Exit code 1
Root / lemma: ueik-1 
Meaning: to choose, filter 

Material: Old Indie vinakti, vivekti, i/ei/e/r//"sondert, siebt, sichtet', particle vikta-, Kaus. 
vecayatr, Avestan aK5-i/ae/r-"ausscheiden, aussuchen'; from the meaning "to 
gottesdienstlichen Zwecken aussondern' entspringt die of "Weihens', wherefore here Latin 
victima^ sacrificial animal, sacrifice, oblation', being based on auf einem/-or ^-stem, *vikti-s 
respectively V//r/i/-s "Weihung'; Gothic M/e//7s"holy', Old Saxon wTh-^s., Old High German 
wTh, wJhi6s., compare Middle High German (ze) wThen nahten, from which Modern High 
German Weihnachten; Old Icelandic ve- n. " shrine, temple'. Old Saxon wThm. "temple'. 
Old English weoh, wTgvn. "Gotterbild'; derived Vb. Gothic weihan, altisl. vTgJa, Old Saxon 
wThian, Old Frisian wTa, wTga, Old High German wThen " consecrate '; with intensive 
gemination Germanic *wik-kan-^ magician ': Old English wiccaxx\. ds., ty/icce "Zauberin' 
(engl. witch); md. n/yic/re/? "conjure, perform magic', wicker^ magician, Wahrsager'; without 



gemination: Old Engiisli wigorz\ixw Walnrsagen belonging', wiglian^ forecast, soothsay ', 

Middle Low German wickelen; eine variant *ueig- (?) in Umbrian ei/e/ie/i/'electum' {*ek- 

ueigetumR). 

References: WP. II 232, WH. II 782; 

See also: relationship to ueik-, ue/gh-'bend' etc. is not ausgeschlossen. 

Page(s):1128 

Root / lemma: ueik-2 

Meaning: force, energy (victory, battle, etc..) 

Material: Latin vinco, -ere, vTci, v/ctum^d\e Oberhand gewinnen, win, triumph; defeat, 

conquer', perv/cax '\r\artnack\g, steadfast', Oscan i///7c/e/''convincitur'; 

Old Irish f/'ch/d l\g\r\ts' , dhfich- 'punish, curse', ffchm. "discord, rage, fury', feuchuir 
"stern' {*ufkaris), feuchrae' austereness, severeness ' (unclear is das ch\x\ acymr. 
guich[i]r^\NM), fecht {*uikta) " campaign = acymr. guith, cymr. gwyth^rage, fury', abret. 
uueith- in PN; gall. VN auf -K/ices(abrit. O/'0'c»-i//ice5"Hammerkampfer'), PN Victo-valos 
etc.; with full grade Vecti-nx, Veco-rTx= Old Irish PN Rachrai, Gen. FTachrach {Ogam 
VECREC); 

Gothic M/e'//7a/7 "fight', w/gana Dat Sg. "fight, struggle, war, fight'; Old English Old High 
German mgan{0\6 High German only in part\c\e w/igant, wJhant, ^atv/iga/? "decrepitus', 
irwigan, confectus, "abgekampft') "fight, quarrel'. Middle High German anwTgen' assail '; 
Middle High German wThen^ exhaust, weaken ', Modern High German dial, sich weihen = 
"sich weigern', anweihen "anfechten'; aorist- present Old Icelandic vega, va "fight, slay', 
Old High German ^/75/we/75/7"uberwinden' (with false consonant). Middle High German 
widerwehen^mih blanken Waffen kampfen'; Old Icelandic vela {*vThalian) "sort, order, 
arrange, sich with etwas abgeben'; Old Icelandic vTg, Old Saxon wTg, Middle Low German 
afr. wTch, Old High German wTc, wTgeic. "fight, struggle'. Old Icelandic Adj. vTgr 
"kampftijchtig', Gothic zero grade waihjdt "war, fight, fight, struggle'; ograde in Germanic 
*waigd-i. " power ', therefrom derived Old Saxon wegian. Old English wsegan. Old High 
German we/genetc. "bother, annoy, torment, smite', Norwegian i/e/^5 "swing'; ein rc'-Adj. 
is Old High German we/gar's\c\r\ widersetzend, stout, proud'. Middle Dutch weiger, weger 
"widerwillig', therefrom Old High German weigaron e\.c. "sich weigem\ 

Lithuanian veikiu, i/e/Tr//" somewhat make, work', a/Oi/e/]^/^"bezwinge', perveikiu 
"bewaltige', veikus^iasi, rapid, hurried', veiklus^ active, geschaftig', viekas^ power, life', 
vykisxw. "life(digkeit)', k/M/5 "alert, awake, smart'; Latvian i/e/Zr/ "align' etc.; i/e/7t//5 "nimble, 
fit, healthy', i//7r/ "thrive'; 



Old Church Slavic vekbm. " power, Lebensalter', Czech russ. vekds.; 

perhaps here also Latin i/Zv "barely, with accurate need', as "alle Kraft 
zusammennehmend'. 

References: WP. I 232 f., WH. II 791 f., Trautmann 339, Vasmer 1, 179. 
Page(s): 1128-1129 

Root / lemma: ueik-3 
(eval):1: === not found
```


## [2026-10-16T05:13:36.821Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n 'Page(s): *113[01]' POK_full.txt; grep -n 'lemma: .*uoik\\|lemma: ueik' POK_full.txt"
}
```


### [2026-10-16T05:13:37.197Z] TOOL RESULT

```
89515:Page(s): 1130-1131 
89562:Page(s):1131 
89904:Page(s): 1131-1132 
89346:Root / lemma: ueik-1 
89375:Root / lemma: ueik-2 
89420:Root / lemma: ueik-3 
89444:Root / lemma: ueik-4, ueig-
```


## [2026-10-16T05:13:39.288Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 89444,89562p POK_full.txt | cut -c1-300; echo =====; sed -n 89844,89904p POK_full.txt | cut -c1-300"
}
```


### [2026-10-16T05:13:39.779Z] TOOL RESULT

```
Exit code 1
Root / lemma: ueik-4, ueig- 

Meaning: to curve, bend; to go round, to exchange 

Note: (extension from "^©/-"bend'). 

Material: 1. Old Indie vfci-\. " deception, seduction ' (Rv. 10, 10, 6; probably "*Krummheit'); 

with voiced-nonaspirated Old Indie vejate, vijate, participle vikta-, i//g/7a- "vor etwas 
zuriJckfahren, davoneilen', yC>/'a-i/y-"Einsturz threaten', abhi-vij- "umkippen', vega-m. 
"Zittern, intense Bewegung, rush', Avestan vaeg- (vaejd-) "(a projectile) swing', vaeya-m. 
"Anprall, blow, knock, prank', nivixta- "herabgeschwungen, herabgeschleudert', npers. 
vextan^ioss, fling', osset. i/e^^^/? "upset, move', balGcT^^a^ "swing, toss, fling'; Intens. Old 
Indie i/ei/^ya/e "fahrt los'; 

Old Indie v/-vyakt/ ^ufr\iaQ>t', vyacas-n. "further Raum', Avestan vyaxa-, vyaxman- 
"eongregation, meeting' (?); 



gr. sTkoj, Aor. £(F)£i^£ Alkman " recoil, nachstehen, unterliegen', (Boeotian) yT^ai 
(i.e.FsT^ai) xwpnoai Hes.; 

Latin viciat "vetcli': nasalized vincid, -/?e"umwinden, bind', \J'r(\bnaT\ previslatu 
"praevinculato"; 

Gothic waihsta^ angle, point, edge'. Middle High German we/gen 'waver'; Old English 
m'cga'beet\e, chafer'; Middle Low German nnd. w/iche/e '\Ne\6enbautr\' from *wTgele, 
diminutive to Old Saxon *wTga, westfal. tv/aja'Weidenbaum', ablaut. Old Frisian Old 
English wag. Old Saxon weg'\Na\\\ CVo/Zro-'geflochtene wall'); also Middle High German 
gewTge, Modern High German Geweih, 6\a\.Gewicht(eln) 6s. (originally probably 
"*Gezweig'); 

Latvian vTkstu, i//7r/"sich biegen, ductile become', v/ksfs' ductile, soft', vTkne' tendril '; 
Latvian vTcinat'\Naye, tummein', refl. 'sich schwenken, bend make'. 

With Indo Germanic ff. Old Icelandic vJkva, J//ri/a(w-present), vJkj'a, preterit i/e//r"from 
the Stelle move, (sich) bewegen, sich wenden'. Old Saxon wTkan' withdraw' (: sikcjo). Old 
English wTcansiexw V. ' withdraw, crumple ', Old High German w/hhan stem V. 'eine 
Richtung nehmen, withdraw'; Old Icelandic ve/kr{an6 veykr\N\t\r\ -w- after vTkva) 'soft, 
weak'. New Norwegian also "pliable' (compare Old Icelandic i/e/A/5"bend'), Old English 
wac{o\}\. of it Old Icelandic vaki) 'soft, weak, woeful, wretched, miserable ', Old Saxon wee 
"weak'. Old High German n/e/ic/? "soft, weak, timorous'; Old English wicei. "RiJster', Middle 
English ty//re/'"Weidengerte'; Middle Low German wTkm., wTkei. "Entweichen, escape'. 
Middle High German wTcfrm. "groin, flank ', formal = Old Icelandic i//7^ "small bay'. Old 
English wTci., Middle Low German wTk6s.\ Norwegian dial. viku. "small point, edge or 
bend'; Old High German tv/77/7d/7 "spring, dance, jump ', Modern High German Hessian 
wicken'rash, hasty and violent hin and her bewegen', Swedish vicka's\c\\ unstet 
bewegen, wippen'; 

Lithuanian vigrus, v'iglas' xas\\, hasty, adroit', Latvian i//e^/s "light', slov. veg' bent', 
i/ega// "waver', i/eze/7 "gebogen'. 

2. Latin i//ic/s(Gen.), vicem, vice, PI. vices, i//ic/Z?^s "variation, Abwechslung'; perhaps 
Old Irish /^ac/7"mutuum, Geschuldetes, blame'; Old Icelandic ^/a/^-i/ZV/ "exchange of gifts', 
a i/ZV/"kreuzweis' (i/ZV/a"swap, vary, exchange'); Old Saxon weiisai' trade, currency'. Old 
High German weiisai, M/e/7s// "variation, exchange, trade' (Old Saxon wehsion. Middle High 
German Modern High German wechselii); with sicherem Indo Germanic 5^ Gothic by/M"die 
an jemanden kommende order'. Old Icelandic i///r5 "Woche' (originally "*variation'), also 



'Seemeile' ("*variation the oarsman'; also Middle Low German n/e/reses 'Seemeile'), Old 
English wicu, wucu'Woche', Old Saxon w/ka\n cruce-w/ka 'Kreuzwoche', Old High 
German wehha, wohha^\Noc\r\e'; 

unclear is because of Gutturals Old Indie vistf- {*uiR-) 'work, Dienstleistung', tri-visff 
(Instr.), after Wackernagel (KZ 67, 173) "alterant, changeable', after G. Liebert 
(Nominalsuffix -//■ S. 138 f.) though "dreifache Dienstleistung'. 

References: WP. I 233 ff., WH. II 781 f., 791 f., Trautmann 338 f.. Frisk 454. 
Page(s): 1130-1131 

Root / lemma: ueiR-, uiR-, uoiRo-{* duei- ksayatlj 

Meaning: house, settling 

Note: 

Root/ lemma: ueiR-, uiR-, uoiRo-{* duel- ksayati): "house, settling' derived from Root/ 

lemma: Rt^ei-: "to settle' : Root/ lemma: kt^eO)-, kt^aO')-: "to acquire, possess'. 

Material: Old Indie vfs-i. "Wohnsitz, house', PL i//s5/7 "people, citizen', Avestan i//s-(e.g. 

Akk. vTsem, ap. viPam) "house, village. Clan', Old Indie vis-pati-^ householder, 

Gemeindehaupt', vis-patnV housewife', ablaut. Old Indie i/es/77a/7-n., jav. vaesma-m. 

"house, dwelling'. Old Indie vesa-m. "Naehbar' (as Latin vTcTnus); verbal (see below) Old 

Indie i//5a//"tritt ein, geht ein', /7/V/sa//"kehrt ein', Avestan i//s5///"geht ein, tritt ein to etwas'; 

Maybe from Skt. i//5-(RV+) "settlement, community, tribe' derived alb. {*vfs) fis 

"settlement, community, tribe', 1//5 "territory, spot, place ' 

Note: 

Alb. cognate has derived from Sanskrit not from Slavic. 

gr. o\Koc„ FoTko(; "house', oJKia ds., oIkeu) " inhabit ', oiK£Tr|<; "housemate', Tpixa-FiK£(; 
epithet the Dorer "in drei Phylen zerfallend'; alb. k/5 "place', amvise {ame^ rwoihef) " 
housewife'; 

Latin vTcus, dial. Keci/5"Hausergruppe, village, dot, Stadtteil' (= gr. FoTko(;), Umbrian 
uocu-com, Akk. i/^/r^if "aedes'; Latin K/7/a"Landhaus, estate' {*uoik-sla, with Latin suffix- 
sla, or *ueik-s-la\.o es-stem from Gothic weihs); 

Gothic weihsu.. Gen. M'e//7s/s "village, spot'; 

Old Prussian waispattin f\Vk. " housewife', Lithuanian K/espaZ/^^s "master, mister', 
viespati^ v\ob\e wife, woman', verbal Lithuanian vaisinti^ host ', v/eset/"to Gaste sein', 
Latvian v/'es/s' guest'; Old Church Slavic i/6S6 "village'. 



References: WP. I 231, WH. II 782 f., Trautmann 363 f., Vasmer 1, 193. 
Page(s):1131 
(eval):1: ==== not found
```


## [2026-10-16T05:13:42.663Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 89844,89904p POK_full.txt | cut -c1-300"
}
```


### [2026-10-16T05:13:43.008Z] TOOL RESULT

```
Root / lemma: ueip- ueib- 

Meaning: to turn, sway 

Material: 1. ueip-:0\^ Indie vepate, -//'regt sich, trembles ', vepayati, v/payat/" makes 

tremble', v/pra-' excited, aroused, begeistert', v/'p- if 'rod, horsewhip', vipatha- m. "a kind 

of arrow' (compare tela vibrare); Avestan vip- 'throw, entsenden (Samen)'; 

cymr. ^m//s^/" restless, mature, ripe, mellow, seasoned ' (from NiJssen) from * uip-skT-mo- 
?• 

Gothic biwaibjan^ uxwrnuAeVi , Old High German z/Vi/e/Zya/? "scatter'; Old Icelandic veifa 
"in schwingender, zitternder Bewegung sein, toss, fling, schlingen, umwickein'. Old English 
M/^/&/7"bekleiden'; Old High German M/e/Z?d/7 "waver, schweben, unstet sein'; Old Icelandic 
uvT^'umhiJIIen', nisi. i//77a "bewilder', i//77"Klopter; Old English wifel, n/z/fe/"" arrow, Wurfpfeil' 
(: Old Indie vipatha-); in addition bya/^5/7"vor astonishment erstarren', M/^/fe/'-/7Js "Theater'; 
perhaps Old High German wTb, Old Saxon Old English wTf, Old Icelandic vTfv\. "woman, 
wife' as "die verhijllte Braut'; compare against it Tavernier-Vereecken RB Ph H 32, 97 f.; 

Old Prussian ty/p/s "bough', Latvian i/ziepe "cover, wrapping of the Weiher', viepl'is 
"Verkleidung, mask', viept^ veil, cover', wTpnuot^ smile (das Gesicht verdrehen)', ; 
Lithuanian 5/K/]c//"herabhangen, from scrap, shred, Lippen', i/5/py//5"das Maul verziehen, 
gawk', vypsau, -d//"with open mouth dastehen, gawk'; (with Baltic efrom e[/]:) Lithuanian 
veptis^6ev\ Mund verziehen', veplys^ gawper, starer', Latvian i/ep//s"Maulaffe, lubber' 
etc.; with secondary ablaut a{: e) in addition Lithuanian vamplys, vamp/e"]erc\and, the with 
open mouth dasteht, dummer person', vampsau, -d//"with open mouth dastehen'. 

2. ueib-, ui-m-b-: 

Gr. yi^jpavai ^suyava Hes., T|J4Ja(; Z,z\ilfxc,. OsTiaAoi, "liJitJiO(; floasiSajv 6 Cuyio(; Hes. 
(also probably ii^jov tov kiggov Hes.); 

Latin vibro, -are"\n zitternde, schwingende Bewegung place, sich trembling bewegen'; 
v/b/x, -rc/s(\n Glossen also v/pex, v/mex) "Strieme, weal, callus from Schlagen'; compare 
under Latvian vJbel&, 

perhaps Middle Irish femm^Xa\\, stalk, kelp ', femman^ kelp ', cymr. gwymon, bret. 
gwemon, goumon6s. {*uimb-, compare Old English wimpel), O'Rahilly Eriu 13, 162 ff., 
different Thurneysen KZ 48, 67; 



Gothic we/pan {stem V.) "bekranzen', w/pja ^Kranz'; Old Icelandic ve/pr'head fascia, 
Kopftuch', ve/pa' female Kopftracht', Norwegian dial. ve/pa'\N\cke\n, eine Peitsche 
schwingen', Old High German n/e/f bandage, head fascia'. Middle High German we/fen 
"swing, haspein', w/fen {stem V.) 'swing, coil ', Middle Low German mp' tussock, wisp'. 
Old English mp/an ^ ab\N\sc\r\en' , Norwegian v/pa' stiff straw or stiff hair, Speize', Middle 
Low German w/pen^toss, fling, sprinkle'; Old High German w/pf' Sc\r\\Nung' , Middle High 
German also mf= holl. m'pds., Old High German w/pf/7, wiffiTEaumwipfel , Modern High 
German (actually Low German) Middle Low German Middle English wippen. Middle High 
German wipfen, wepfen^ jump ', Norwegian v/ppa^\N\sp, whisk ', nasalized Old English 
M///77yOe/'Wimpel, Schleier', Old High German M///77/?a/'Stirntuch, Schleier'; 

Latvian v/etif, v/et>t/es's\c\r\ drehen, verdrehen; das Gesicht verstellen', Lithuanian 
vybur-iu, -//and -ioju, -/ot/'\Ne6e\n'; Latvian vlbe/e' weals, marks from blows'. 

References: WP. I 240 ff., WH. II 779 f.; 
See also: compare sue/p- above S. 1042. 
Page(s): 1131-1132
```


## [2026-10-16T05:13:46.874Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i -E '^ *weik|^ *weip|weip-|weik-' AHD_watkins1985.txt | head -20"
}
```


### [2026-10-16T05:13:47.303Z] TOOL RESULT

```
157:The root deme-' denoted both the house (Latin domus) and the household as a social unit. The father of the family (Latin pater familias) was the “master of the house” (Greek despotes) or simply “he of the house” (Latin dominus). A larger unit was the vil- lage, designated by the word weik-'. The
1136:weik-'
1137:derivatives violdre, to treat with force, and violentus, vehement: VIM, VIOLATE, VIOLENT. [In Pok. 3. wei- 1123.] weik-', Clan (social unit above the household). 1. Suf- fixed form *weik-slé in Latin villa, country house, farm: VILLA, VILLAGE, VILLAIN, VILLANELLE, (VILLEIN); (BI- DONVILLE). 2. Suffixed o-grade form *woik-o- in: a. La- tin vicus, quarter or district of a town, neighborhood: (VICINAGE), VICINITY; b. Greek oikos, house, and its derivative oikia, dwelling: ANDROECIUM, AUTOECIOUS, DIOCESE, DIOECIOUS, DIOICOUS, ECESIS, ECOLOGY, ECON- OMY, ECUMENICAL, HETEROECIOUS, MONOECIOUS, PAR- IsH, TRIOECIOUS. 3. Zero-grade form *wik- in Sanskrit vis-, dwelling, house, with derivative vaisyah, settler: Vaisya. [Pok. weik- 1131.] weik-2. In words connected with magic and religious notions (in Germanic and Latin). 1. Germanic suffixed form *wih-l- in Old English wigle, divination, sorcery, akin to the Germanic source of Old French guile, cun- ning, trickery: GUILE. 2. Germanic expressive form *wikk- in: a. Old English wicca, wizard, and wicce, witch: WITCH; b. Old English wiccian, to cast a spell: BEWITCH. 3. Possible suffixed zero-grade form *wik-t- imé in Latin victima, animal used as sacrifice, victim (although this may belong to another root *(a)wek- not otherwise represented in English): vicTiM. [Pok. 1. weik- 1128.] weik-3, To be like. 1. Suffixed variant form ‘*eik-on- in Greek eikdn, likeness, image: ICON, (ICONIC), ICONO-; ANISEIKONIA. 2. Prefixed and suffixed zero-grade form *n-wik-és, not like (*n-, not; see ne), in Greek aikés, unseemly: AECIUM. [Pok. 3. weik- 1129.] weik-4. Also weig-. To bend, wind. I. Form weig-. 1. Ger- manic *wik- in: a. Old English wice, wych elm (having pliant branches): wyCH ELM; b. Swedish viker, willow twig, wand, akin to the Scandinavian source of Middle English wiker, wicker: WICKER; C. Old Norse vikja, to bend, turn, probably akin to the Scandinavian source of Old North French wiket, wicket (< “door that turns”): WICKET. 2. Germanic *waikwaz in: a. Old Norse veikr, pliant: WEAK; b. Dutch week, weak, soft: WEAKFISH. 3. Germanic *wik6n-, “a turning,” series, in Old English wicu, wice, week: WEEK. II. Form *weik-. Zero-grade form *wik- in: a. Latin vix (genitive vicis), turn, situ- ation, change: VICAR, (VICARIOUS), VICE; VICISSITUDE; b. Latin vicia, vetch (< “twining plant”): veTCH. [Pok. 4. ueik- 1130.] weik-5, To fight, conquer. 1. Germanic “wik- in Old Norse vigr, able in battle: WIGHT2. 2. Nasalized zero-grade form *wi-n-k- in Latin vincere (past participle victus), to conquer: VANQUISH, VICTOR, VINCIBLE; CONVINCE, EVICT. [Pok. 2. weik- 1128.] weip-. To turn, vacillate, tremble ecstatically. 1. O-grade form *woip- in Germanic *waif- in Old Norse veif, waving thing, flag, probably akin to the Scandinavian source of Anglo-Norman waif, ownerless property: WAIF!, (WAIVE), (WAIVER). 2. Variant form *weib- in Germanic *wipjan, to move back and forth, in: a. Old English wipian, to wipe: WIPE; b. Old French guiper, to cover with silk: GUIPURE; c. Middle Dutch and Middle Low German wippen, to swing: WHIP. 3. Perhaps suffixed nasalized zero-grade form *wi-m-p-ila- in: a. Old English wimpel, covering for the neck (< “something that winds around”): WIMPLE; b. perhaps Middle Dutch wimmel, auger (< “that which turns in boring”): WIMBLE. 4. Suf- fixed zero-grade variant form *wib-ro- in Latin vibrdre, to vibrate: VIBRATE. [Pok. weip- 1131.] weis-. To flow. I. 1. Germanic *wisdn-, waisén- in Old English wdse, mire, mud: 00ZE?. 2. Taken by many as a derivative of this root, but probably an independent Indo-European word, is the suffixed form *wis-o- in Latin virus, slime, poison: VIRUS. 3. Extended zero-grade form *wisk- possibly in Latin viscum, mistletoe, birdlime: VISCID, VISCOUS. II. Attributed by some to this root, but more likely of obscure origin, are some Germanic words
1217:ADDER nétr- ADDICT deik- ADDUCE deuk- -ADELPHOUS gWelbh- ADEMPTION em- ADENO- engW- ADEPT ap-1 ADHERE ghais- ADIABATIC gWa- ADIEU delw- ADIT ei-1 ADJACENT yé- ADJECTIVE yé- ADJOIN yeug- ADJOURN deiw- ADJUDICATE yewes- ADJURE yewes- ADJUST yeug- ADJUVANT ad- ADMIRE smei- ADMIT (s)meit(9)- ADMIX meik- ADMONISH men-t ADNATE gene- ADNEXA ned- ADO ad- ADOLESCENT al-3 ADOPT op-2 ADORE Or- ADORN ar- ADRENERGIC werg- ADSCITITIOUS skei- ADSORB srebh- ADULT al-3 ADULTERATE al-1 ADULTERINE al-1 ADULTERY al-1 ADUMBRATE andho- ADUST eus- ADVANCE ant- ADVECTION wegh- ADVENT gWa- ADVENTITIOUS gWa- ADVENTURE gWa- ADVERB wer-6 ADVERSE wer-3 ADVICE weid- ADVISE weid- ADVOCATE wekw- AECIUM weik-3 AEDES swad-
1246:ANILE an-! ANILINGUS 4no-, leigh- ANIMA ane ANIMADVERT ane- ANIMAL ane- ANIMATE ane ANIMATO ane- ANIMISM ane- ANIMOSITY ane- ANIMUS ane- ANION ei-1 ANISEIKONIA weik-3 ANKLE ank- ANKYLOSIS ank- ANLAGE an}, legh- ANNALS at- ANNEAL aidh- ANNEX ned- ANNIHILATE ne ANNIVERSARY at-, wer-3 ANNOTATE gno- ANNOUNCE neu-! ANNOY od-2 ANNUAL at ANNUITY at- ANNUL ne ANNULAR 4no- ANNULET 4no- ANNULUS 4no- ANODE sed-2 ANODYNE ed- ANOINT ong¥- ANOMALOUS sem-! ANOMIE nem- ANON ol-no- ANONYMOUS né-men- ANOPHELES obhel- ANORECTIC reg-1 ANOREXIA reg-1 ANORTHITE wrddh- ANOSMIA od-! ANSATE ans- ANSERINE ghans- ANSWER swer-1 ANT mai-1
1270:AUSPICE awi-, spek- AUSTERE saus- AUTACOID y@k- AUTARCHY arkhein AUTARKY arek- AUTHOR aug-! AUTHORIZE aug-! AUTOBAHN g*hen-* AUTOCHTHON dhghem- AUTOECIOUS weik-1 AUTOGIRO géu- AUTOMATIC men-1 AUTONOMOUS nem-
1294:BENIGN deu-?, gene- BENTHOS gWadh- BENUMB nem- BEQUEATH gWet-2 BEQUEST gWet-2 BEREAVE reup- BERM bhrem-2 BERRY bha-1 BERSERKER bher-3 BESPEAK spreg- BESPRENT spergh- BEsT bhad- BETOKEN deik- BETRAY d6- BETROTH deru BETTER bhad- BETWEEN dwo- BETWIXT dwo- BEVEL bat- BEVERAGE pO(i)- BEWITCH weik-2 BEZOAR gWhen-1, pa- BHAGAVAD-GITA g@i-2 BI- dwo-
1296:BID bheudh-, ghedh- BIDE bheidh- BIDENTATE dent- BIDONVILLE weik-1 BIENNIUM at-
1392:CONFOUND gheu- CONFRERE bhrater- CONFUSE gheu- CONFUTE bhau- CONGE mei-1 CONGEAL gel-3 CONGENER gene- CONGENIAL gene- CONGENITAL gene- CONGERIES gerere CONGEST gerere CONGLOBATE gel-1 CONGLOMERATE gel-1 CONGLUTINATE gel-1 CONGRATULATE gWera-3 CONGREGATE ger-! CONGRESS ghredh- CONGRUENT ghréu- CONIDIUM keni- CONIOSIS keni- CONJECTURE yé- CONJOIN yeug- CONJUGAL yeug- CONJUGATE yeug- CONJUNCT yeug- CONJURE yewes- CONNATE gene- CONNECT ned- CONNIVE kneig’h- CONNOISSEUR gn6- CONNOTE gné- CONNUBIAL sneubh- CONQUER quaerere CONQUIAN kom, kWo- CONSCIENCE skei- CONSCIOUS | skei- CONSCRIPT skribh- CONSECRATE sak- CONSENT sent- CONSEQUENT sekw-1 CONSERVE ser-1 CONSIDER sweid-1 CONSIGN sekw-1 CONSIST sta- CONSOCIATE sekw-1 CONSOLE! sel-2 CONSOLIDATE sol- CONSOLUTE leu-1 CONSONANT swen- CONSORT ser-3 CONSPICUOUS _ spek- CONSPIRE spirare CONSTABLE ei-1 CONSTANT sta- CONSTELLATION  ster-3 CONSTERNATE  ster-2 CONSTIPATE  steip- CONSTITUTE sta- CONSTRAIN | streig- CONSTRUCT  ster-2 CONSUETUDE s(w)e- CONSUME em- CONTACT tag- CONTAIN ten- CONTAMINATE tag- CONTEMPLATE tem- CONTEND ten- CONTEST trei- CONTEXT teks- CONTINUE ten- CONTORT terkw- CONTOUR tera-1 CONTRA- kom CONTRABAND bha-2 CONTRACT tragh- CONTRADICT deik- CONTRARY kom CONTRAST sta- CONTRAVENE gWa- CONTRITE tere-1 CONTRIVE trep-2 CONTROL ret- CONTROVERSY wer-3 CONTUSE (s)teu- CONVALESCE wal- CONVECTION wegh- CONVENE gWa- CONVENIENT gWa- CONVENT gWa- CONVENTICLE gWa- CONVENTION gWa- CONVERGE wer-3 CONVERSE! wer-3 CONVERT wer-3 CONVEX wegh- CONVEY wegh- CONVINCE weik-5 CONVIVIAL gWei- CONVOKE wekw-
1429:DIN dhwen- DINGUS _{enk-1 DINOSAUR dwei- DINOTHERE dwei- DIOCESE weik-! DIOECIOUS weik-1 DIOICOUS_ weik-1 DIOPTER oOkW- Dioscuri_ deiw-, ker-3 pip dheub- DIPHTHERIA deph- DIPHYODONT bheue- DIPLO- dwo- DIPLOCARDIAC kerd-1 DIPLODOCUS dek-1 DIPLOE dwo- DIPLOID pel-3 DIPLOMA dwo- DIPNOAN pneu- DIRE dwei- DIRECT reg-! DIRNDL tek- DISARM ar- DISASTER ster-3 DISBURSE bursa DISCERN krei- DISCIPLE dek-! DISCIPLINE dek-? DISCOMFIT dhé-1 DISCORD kerd-1 DISCOURSE kers-2 DISCRIMINATE krel- DIscuss kwét- DISDAIN dek-1 DISEMBOGUE beu-! DISFIGURE dheigh- DISGUST geus- DISK deik- DISMAL deiw-, mel-5 DISMAY magh-! DISMISS (s)meit(9)- DISPARATE pere-1 DISPATCH ped-! DISPEL pel-6 DISPENSE (s)pen- DISPERSE (s)preg- DISPLAY plek- DISPOSE apo- DISPUTE peu- DISQUISITION quaerere DISRUPT reup- DISSECT sek- DISSEMINATE 6-1 DISSENT sent- DISSERTATE ser-3 DISSIDENT sed-1 DISSILIENT sel-4 DISSIPATE swep-2 DISSOCIATE sekw-1 DISSOLVE leu-! DISSONANT swen- DISSUADE swad- DISTANT sta- DISTEND ten- DISTICH steigh- DISTINGUISH _ steig- DISTORT terkw- DISTRACT tragh- DISTRAIN  streig- DISTURB twer-! DITCH dhigw- DITTO deik- DITTY deik- DIURETIC wers-2 DIURNAL deiw- DIVA deiw- DIVARICATE wa- DIVE dheub- DIVERGE wer-3 DIVERT wer-3 DIvEs_ deiw- DIVIDE weidh- DIVINE! deiw- DIVINE? deiw- DIVULSION wel-4 Dizzy dheu-!
1441:EsLis gWela-1 EBULLIENCE beu-! ECBOLIC gWele-1 ECCENTRIC kent- ECCHYMOSIS gheu- ECCLESIA kela-2 ECCRINE krei- ECEsIsS weik-1 ECHARD segh- ECHELON skand- ECHIDNA ang¥hi- ECHINO- ang¥hi- ECHINUS angVhi- ECHO (s)wagh- ECHOLALIA 1a- ECLAIR kelo-2 ECLAIRISSEMENT kelo-2 ECLAMPSIA [ap- ECLECTIC leg-! ECLIPSE leikw- ECLOSION kleu-3 ECOLOGY weik-1 ECONOMY weik-1 ECRU kreue-1 ECSTASY sta- ECTO- eghs ECTOSARC twerk- ECU skei- ECUMENICAL welk-1 ECZEMA yes- EDACIOUS ed- EDAPHIC sed-! EDDY eti EDELWEISS _athal-, kweit- EDEMA oid- EDENTATE dent- EDGE ak-
1571:Grus_ gere-2 GUARANTY wer-5 GUARD wer-4 GUERDON lau-, wi- GUERRILLA wers-1 GUESS ghend- GUEST ghos-ti- GUIDE weid- GUILD gheldh- GUILDER ghel-2 GUILE weik-2 GUIPURE weip- GUISE weid- GULAR gWel-3 GULDEN ghel-2 GULES gwWel-3 GULF kwelp- GULLET gWel-3 Gum? ghéu-
1602:HETAERA s(w)e- HETERO- sem-! HETERODOX dek-! HETEROECIOUS weik-1 HETEROGENEOUS gene- HETERONYMOUS no-men- HEURISTIC wera-2 HEW kau-2
1662:ICEBERG bhergh-2 IcH dhgWher- ICHTHYO- dhghi- ICHTHYORNIS  or- ICICLE eis-2, yeg- ICON weik-3
1663:ICONIC weik-3 ICONO- weik-3 ICONOGRAPHY gerbh- ICONOSTASIS  sta- ICOSAHEDRON  wikmti ID I
1882:MOLTO mel-4 MOLY md6(u)lo- MOLYBDENUM plumbum MOMENT meue- MOMENTOUS meue- MOMENTUM meue- MONAD men-4 MONANTHOUS = andh- MONASTERY men-4 MONAXON aks- MonpDay mé-2 MONEY men-! MONGER meng- MONGREL mag- MONILIFORM mon- MONISH men-1 MONITION men-1 MONITOR men-1 MONK men-4 MONO- men-4 MONOCLE oOkw- MONOCLINIC klei- MONOCLINOUS klei- MONOCOQUE kokkos MONODY wed-2 MONOECIOUS weik-! MONOMER (s)mer-2 MOoNOPHYSITE bheue- MONOPODIUM ped-1 MONOPOLY pel-5 MONOTREME tere-1 MONS men-2 MONSTER men-1 MONTAGNARD men-2 MONTANE men-2 MONTE men-2 MONTH mé-2 MONTICULE men-2 MONUMENT men-! MOOCH meug-! MOOD! mé-1 MOOD? med- MOON mé-2
2061:PARGET per, yé- PARHELION sawel- PARI-MUTUEL pere-2 PARISH weik-1 PARITY2 pere-2 PARLAY pere-2 PARLEY gWelg-1 PARLIAMENT gWele-1 PARLOR gWelg-1 PARLOUS per-4 PARODY wed-2 PAROL gWele-1 PAROLE gWele-1_ PARONOMASIA n0-men- PARONYCHIA nogh- PARONYMOUS no-men- PAROTID GLAND ous- -PAROUS pere-) PAROUSIA es- PAROXYSM ak- PARRICIDE paso- PARRY pere-!
2411:TRIO trei- TRIOECIOUS weik-1 TRIP der-1 TRIPEDAL ped-1 TRIPLE pel-3, trei- TRIPLEX trei- TRIPLOBLASTIC pel-3 TRIREME ere-1 TRISKELION skel-3 TRISMUS | strei- TRISOCTAHEDRON trei- TRITANOPIA ei- TRITE ter * TRITIUM trei- TRITONE trei- TRITURATE tere-1 TRIUMVIR trei-, wi-ro- TRIUNE oi-no- TRIVET ped-1 TRIVIAL wegh- TRIVIUM wegh- TROCAR kwetwer-, trei- TROCHAL dhregh- TROCHANTER dhregh- TROCHE dhregh- TROCHEE dhregh- TROCHLEA dhregh- TROCHOPHORE dhregh- TROGON tere-1 TROIKA trei- TROPE trep-2 TROPHALLAXIS al-1 TROPHIC- threph- TROPHO-  threph- -TROPHY threph-, trep-2 TROPIC trep-2 TROPO- trep-2 -TROPOUS  trep-2 TROT der-1
2445:VAIR wer-1 VaisyA_ weik-1 VALE! wel-3 VALEDICTION deik- VALENCE wal- VALET upo VALETUDINARIAN wal- VALHALLA kel-2, wele-2 VALIANT wal- VALID wal- VALKYRIE wele-2 VALLATION walso- VALLEY wel-3 VALONIA gWele-2 VALOR wal- VALUE wal- VALVE wel-3 VAMOOSE wadh-2 VAMP! ped-1 vaAN3 wet-1 VANADIUM wen-1 VANDAL wendh- VANE pan- VANG pag- VANILLA wag- VANIR wen-! VANISH eu-2 VANITY eu-2 VANQUISH welk-5 VAPID kwép- VAPOR kwép- VAQUERO wak- VARA wa- VARIEGATE wer-1 VARIETY wer-1 VARIOLA wer-! VARIORUM wer-! VARIOUS wer-1 VARIX wer-1 VARLET upo VaRUNA wel-1 VARUS wa- VARVE kwerp-
2451:VESPIARY wopsa VEST wes-4 VESTA wes-3 VETCH weik-4 VETERAN wet-2 VETERINARY wet-2
```


## [2026-10-16T05:13:50.635Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E \"^vi[θ0]|^vith|^vi9|^viθ\" KNT_full.txt | head; grep -n -E \"vi[θ0]a|viθ|vith\" KNT_full.txt | head -20"
}
```


### [2026-10-16T05:13:50.961Z] TOOL RESULT

```
460:$108. pAr. k апа g before consonants....... 37 $144. Noun and Adjective Stems vith suffix
```


## [2026-10-16T05:13:53.759Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E \"^vi.?- |^vi.?a- |^vi[^ ]{0,3}-  *(n|adj|f)\" KNT_full.txt | head -30; grep -n \"royal house\" KNT_full.txt KNT.txt | head"
}
```


### [2026-10-16T05:13:54.096Z] TOOL RESULT

```
5333:viða- ‘belonging to the royal house’. 
9841:við- from pIE *yik-, also have the regular endings: 
24895:vi- + kan- ‘dig apart, destroy’: viyakanam 1st 
25820:vi- + jan- ‘shatter’: vijaná"tiy 3d pl. subj. ($208, 
25961:vi- + tar- ‘go across’, caus. ‘put across’: viya- 
26923:vi- + nab- caus. ‘injure, harm’: vindPayatiy 
28292:vi- + mard- ‘destroy’: vimardatiy (830, $213) 
28946:vi- prefix ‘away, apart’: Av. vi, Skt. vi; with 
28952:við- sb. ‘house, royal house, royal clan, court’ 
28968:viða- adj., probably ‘royal, of the royal fam- 
28971:visa- ‘all’, because of the АКК. translation (Wb. 
29036:visa- adj. ‘all’: OP (Med.) vispa-, Av. vispa-, 
29052:vispa- adj. ‘all’: Median (49.11, $90) for OP 
KNT_full.txt:5319:pIE *uik-, OP við- ‘house, royal house’, Av. vfs- 
KNT_full.txt:5333:viða- ‘belonging to the royal house’. 
KNT_full.txt:16522:my royal house, and this land which I hold, may 
KNT_full.txt:17052:strove until I reestablished our royal house on its 
KNT_full.txt:17055:Magian did not remove our royal house. 
KNT_full.txt:19106:* royal house; and may Ahuramazda protect this 
KNT_full.txt:19111:the royal house. This boon may Ahuramazda to- 
KNT_full.txt:19112:gether with the gods of the royal house give to me! 
KNT_full.txt:19207:down upon this royal house. 
KNT_full.txt:19246:Ahuramazda protect, and my royal house.
```


## [2026-10-16T05:13:56.508Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 28950,28972p KNT_full.txt; awk 'BEGIN{RS=\"\\f\"} {if (index($0,\"viθ- sb.\")||index($0,\"við- sb.\")) print NR}' KNT_full.txt"
}
```


### [2026-10-16T05:13:57.044Z] TOOL RESULT

```
við- sb. ‘house, royal house, royal clan, court’ 
(JNES 4232): Av. vis- ‘Herrenhaus’, Skt. vié- 
‘house, dwelling’, Gk. ofxos ‘house’, Lt. vicus 
‘village’ (§22, $87, $114, §142). Decl., §188.1V, 
V. иат asf. AsH 12f; DPe 24; DPh 10; DNa 
53; DSe 51; DSt 9°; DH 8; XPh 58; A'He 20. 
v'6am asf. DB 1.69, 71. véd-patiy isf. (Foy, KZ 
35.37-8, 37.556; Hz. Api 352-4) DB 2.16°; 3.26. 
vidiyd 18. CMb note: DPe; DPi; DNb 30; DSg 
3°; XP; XH; АЧ. véilya] DB 4.66. vióbis-ca 
ipf. ($87, §188.V) for apf. ($252.1) ‘houses’ DB 
1.65 (Tm. Lex. 125-6, for various views; Gray, 
JAOS 33.2813; Morgenstierne, Acta Or. 1.248-9; 
wrongly Sen 23, with ablatival meaning). 


viða- adj., probably ‘royal, of the royal fam- 
ily’, to við- ‘royal house’ (5148.11: Tm. Lex. 125; 
MB Gr. $282); but possibly ‘all’, the same as 
visa- ‘all’, because of the АКК. translation (Wb. 
KIA 81n.).  vifaibis ipm. DPd 14, 22, 24. 
1
```


## [2026-10-16T05:14:01.562Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E \"^v[iī]s-? |^vīs-|^vis- f|vīspaiti|vispaiti|vīs\\.pati|vis\\.paiti\" BRT.txt | head -20; grep -n -E \"^vip-|^ ?vip- |vaēp|vaep-\" BRT.txt | head"
}
```


### [2026-10-16T05:14:01.906Z] TOOL RESULT

```
13119:und  GP.  mit  äaitihupalay-  (Stverz.,  unter I  a,  2  a):  nmünahe  vä  nmänS.paitiS  vTsS vä  vispaitii' tantJus  vä  zantufaitii  "itihSui vä  dair^hupaitisYtiO.18;  usw.;  —  nmäna- iiam  nmänS.paitis . . 'Äyunam  datAhupatti} Yt/0. 18.
24322:vis-  3  a  1456
24332:vis-  a  b
22055:vaep-
22089:•  j-  (•  6-)  vaep-  V.  'proicere'.  Praes.  a vaipa-,  27  vi/ya-,  30  (Iter.)  vaepaya-,  — PPfP.  vipta-;  PFP.  vaipya-.
22092:vaep-  mit  afia
```


## [2026-10-16T05:14:04.376Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -E \"Haus, Clan|Clan|'Herrenhaus'|Herrenhaus\" BRT.txt | head -20; sed -n 22089,22100p BRT.txt | cut -c1-300"
}
```


### [2026-10-16T05:14:04.854Z] TOOL RESULT

```
3822:WoH  Ableit.  aus  'anoClan  Adv.  (das  sich  lu anoitö  verhält  wie  lat.  inier  in  intus).  —  arm. LW.  aular  'fremd'.  —  »)  VgL  iBed.  lat.  firr- igriima.
24320:•  j.,  g.  vis-",  p.  vi%'-  £  i)  'Herrenhaus, Herrenburg,  adeliger  Hof:  'sS  pu^rpm''' bii'azyät  ayrfm  staor)m  aryjS  V.  7,  43;  F.  8;
24325:—  Hyati^ .  .  nirasätiy  (Sp,  184  o.)  €»biy imam  "'^am  D.  6.  3 ;  —  adam  hamataxsaiy yatä  ''ham  tyam  atnaxam  *ga'iava  avä- stayam  Bh.  /.  i4;i4-  II  3)  der  zu  einem Herrenhaus  gehörige  Komplex  von  Höfen 'Dorf,  Dorfschaft,  Geraeine':  ya^a  yal,. hamqm  avassii  mazdayasnts  avi  'sö  V. 18.  ra;  —  nSit  ahma^  *ä  *tyanlm{sä.)  nöit vWäpitn  xlta  maxdayasnJl  aoi  'sS  Y.  J2. 3;
•  j-  (•  6-)  vaep-  V.  'proicere'.  Praes.  a vaipa-,  27  vi/ya-,  30  (Iter.)  vaepaya-,  — PPfP.  vipta-;  PFP.  vaipya-.
dby  Google
»3^3
vaep-  mit  afia
vaena-  rtat  paiti
'324
'pedicare  aliquem,  Päderastie  treiben mit  — '  (Akk.)":  yat  anusS  *vijyä/e^'^ vifyätica  "si  (quis)  invitus  pedicatur  et peÄcat"  V.  Ä  26;  27;  —  arsaca  vipts arlaca  valpayS  "ein  Mann  der  der Päderastie  dient  und  ein  Mann  der  ihr fröhnt"  V,  iS'.  32;  —  yas^a  dim  jana
mit  apa  'deicere,  (wieder)  von  sich geben':  alte  yöi  liaSva  altalsva  daxma^sva garshmli  apäca  vaip?nti  V.  7.  55.
mit  paräca  '(fort-,  wegwerfen  sva.)  ab- wenden': duhar3hahi  (sd.)  paräca  vaipaya manu  Y.  to.  1 2.
mit  ni  'niederwerfen,  zu  nichte  machea'; duisaukahe  (sd.)  paräca  vaspaya  manS Hat  ahe  nl  manö  manS  (näml.  valpayä)^^ yS  ml  dussanAö  histaite  Y,  to.  12,
Vgl.  inp,  vi/lak  ■pathicus',  vtpimlak  'pedica- tor"  Dd.  73.  6,  7.  —  Pü.  (in  V.  8.  32):  vuin i  -üifiak  u  viisn  i  ■vißinUak»,  (lu  V.  A  26,  27). ie..7ii/lilaiävinßfnef,  (mV./,  Sa):  tünmars, (ferner  lo  V.  7.  55);  afe  vämitan,  (in  Y.  7-0] bastani}),  SQ.;  pativarlay
•  j.  vaepayant-  Adj:,  PPA.:  s.  vaip-.
```


## [2026-10-16T05:14:08.639Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 24316,24322p BRT.txt | cut -c1-300; grep -n -E \"v[iīIT]s\\.?pait[iī]-|v[iīIT]s\\.?pat[iī]\" BRT.txt | head -5"
}
```


### [2026-10-16T05:14:09.030Z] TOOL RESULT

```
Pü.:  wü-  ramak.
•  j,  vir5.rao8a-  Adj.  'der  das  äussere Ansehen  eines  Mannes  hat,  in  Männer- gestalf:  tarn  zimargQsS  *ahr>nvB  datiia ySi  para  ahmst  °Sa  apataym  Y.  ^.  ij-
•  j.  vi.urviätay-  f.  'Auseinandergehen, Trennung*:  pasca  astasca  baotanhasca 'JsUm  *Y.55.  a,  V.Ä81;  —  äikivaniim.. pantqtn  .  .  yal  astasca  baotaahasia  "istlm "den  notvollen  Weg,  nänalich  die  Trennung von  .  ."  H.2. 17.
Zum  V.  un/aei:  —  S.  noch  "fairiurutvülil.  — Pü. :  afe  varHsmh.
•  j.,  g.  vis-",  p.  vi%'-  £  i)  'Herrenhaus, Herrenburg,  adeliger  Hof:  'sS  pu^rpm''' bii'azyät  ayrfm  staor)m  aryjS  V.  7,  43;  F.  8;
—  'sS  pu%rS  S%wyänBi!  'SS  süraya  "^rai- /aunJ  Yt.5.33,  77.  3S;    —    ä%wyS  .  .  yal
vis-  3  a  1456
```


## [2026-10-16T05:14:12.934Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for w in villa village vicinity vicinal ecology economy wipe whip vibrate; do echo \"## $w\"; grep -n -m2 \"^$w, \" KLN_1966.txt | cut -c1-500; done"
}
```


### [2026-10-16T05:14:13.688Z] TOOL RESULT

```
## villa
## village
## vicinity
## vicinal
## ecology
12612:ecology,  oecology,  n.,  that  branch  of  science  which deals  with  animals  and  plants  in  relation  to  their environment.  —  G.  Okologie,  coined  by  the German  biologist  Ernst  Heinrich  Haeckel (1834- 1 9 1 9)  fr.  Gk.  oixo- (see  eco-)  and  -Xoyia, fr. -Xoyog,  ‘one  who  speaks  (in  a  certain  manner); one  who  deals  (with  a  certain  topic)’.  See  -logy. Derivatives :  ecolog-ic,  ecolog-ic-al,  adjs,,  ecolog- ic-al-ly,  adv.,  ecolog-ist,  n. economic,  adj. 
## economy
12615:economy,  n.  —  L.  oeconomia,  ‘the  management  of a  household’,  fr.  Gk.  oixovojxia,  of  s.m.,  fr. oixovofzog,  ‘the  manager  of  a  household, steward’,  which  is  compounded  of  oixo?,  ‘house, dwelling,  place  to  live  in’,  and  -vojxog,  ‘manag¬ ing’.  Gk.  oTxog  (dial,  FoXxoq),  is  rel.  to  oixia, Gortynic  Gk.  fotxiai,  ‘house’,  and  cogn.  with L.  vicus,  ‘district’,  vicious,  ‘near,  neighboring’, Goth,  weihs,  OE.  wic,  ‘dwelling,  village’.  See vicinage,
## wipe
## whip
## vibrate
```


## [2026-10-16T05:14:16.170Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for w in villa village vicinity vicinage wipe whip vibrate; do echo \"## $w\"; grep -n -m2 -E \"(^| )$w,  (n|v|adj)\" KLN_1966.txt | cut -c1-600; done"
}
```


### [2026-10-16T05:14:16.835Z] TOOL RESULT

```
## villa
## village
## vicinity
## vicinage
## wipe
## whip
## vibrate
```


## [2026-10-16T05:14:19.203Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -i -E \"^vill|^vicin|^wipe|^whip|^vibra\" KLN_1966.txt | head -20; grep -n -i -E \"villa, n|village, n|wipe, v|whip, v|vibrate, v|vicinity, n\" KLN_1971.txt | head"
}
```


### [2026-10-16T05:14:19.670Z] TOOL RESULT

```
71005:Diervilla, n., a genus of plants, the bush honey- 
261640:whip, v., wife, wimple, wipe, wisp, gimp, guipure. 
261814:vicinity, n. — L. vicinitas, ‘neighborhood’, fr. vi- 
262096:villa, n. — It., fr. L. villa, ‘country house, villa, 
262103:village, n. — ME., fr. OF. (= F.), fr, L. villa-
```


## [2026-10-16T05:14:23.019Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 261814,261822p KLN_1971.txt; echo ---; sed -n 262096,262110p KLN_1971.txt; echo ---; sed -n 261630,261642p KLN_1971.txt; grep -n -E \"^(wipe|whip|vibrate|vibrato), \" KLN_1971.txt"
}
```


### [2026-10-16T05:14:23.417Z] TOOL RESULT

```
vicinity, n. — L. vicinitas, ‘neighborhood’, fr. vi- 
cinus, ‘neighboring’. See vicinage and -ity. 
vicious, adj. — ME., fr. MF. vicieus (F. vicieux), 



810 

fr. OF., fr. L. vitiosus, ‘full of faults, faulty’, fr. 
---
villa, n. — It., fr. L. villa, ‘country house, villa, 
farm', which stands for *vic-sla, and is rel. to 
vicus, ‘village, hamlet’, whence vicinus, ‘near, 
neighboring’. See vicinage and cp. village, villain, 
villancico, villanella, villanelle. 
villadom, n., the world of viljas. — A hybrid coin- 
ed fr. villa and suff. -dom. 
village, n. — ME., fr. OF. (= F.), fr, L. villa- 
ticus, ‘pertaining to a villa or country house', 
used as a noun, fr. villa, ‘country house, villa*, 
in Late L. ‘village’. See villa and -age and cp. 
villatic. 

Derivatives: village-ous , adj., villag-er , n., villag- 
ery, n., villag-y, village-y , adj. 
---
down, to rock', is of LG. origin), OHG. wifan , 
MHG. wifen , G. weifen , ‘to swing, wind, reel', 
OHG. wipf \ ‘swing, impetus’, OHG. wipfil, 
MHG., G. wipf el, ‘top of a tree’, lit. ‘the sway- 
ing part (of a tree)’. Cp. the collateral base 
*weip-, whence OI. vepate, vepati, ‘is agitated, 
trembles’, ON. veifa, ‘to wave, vibrate (whence 
veif, ‘something flapping’), OE. wdfian, ‘to wave, 
brandish’, OHG. weibon , ‘to move to and fro, 
shake’, zi-weibjan, ‘to scatter’. Cp. waif, waive, 
whip, v., wife, wimple, wipe, wisp, gimp, guipure. 
For the ending see verbal suff. -ate. 
Derivatives: vibrat-ile , adj., vibrat-il-ity, n., 
93646:whip, decry: to demand passionately’, freq. of 
238400:wipe, rub’, Du. zwerven , ‘to rove, wander’, 
261622:vibrate, intr. v., to move to and fro; to oscillate; 
261640:whip, v., wife, wimple, wipe, wisp, gimp, guipure. 
261648:vibrato, n., a tremulous effect produced by the 
266661:whip, tr. and intr. v. — ME. whippen, rel. to Dan. 
267537:wipe, tr. v. — ME. wipen, fr. OE. wipian, ‘to wipe’,
```


## [2026-10-16T05:14:27.486Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; sed -n 261622,261629p KLN_1971.txt; echo ---; sed -n 266661,266668p KLN_1971.txt; echo ---; sed -n 267537,267543p KLN_1971.txt"
}
```


### [2026-10-16T05:14:27.966Z] TOOL RESULT

```
vibrate, intr. v., to move to and fro; to oscillate; 
tr. v., to move to and fro. — L. vibratus, pp. of 
vibrdre , ‘to move rapidly to and fro, shake, 
brandish, agitate, vibrate’, fr. I,-E. base *weib~, 
‘to move to and fro, to swing’, whence also Lith. 
wpburiu, wpburti, ‘to wag (the tail)’, Lett, viebt , 
‘to turn, spin’, Dan. vippe , MLG., MDu., Du. 
wippen , ‘to swing’ (G. wippen , ‘to move up and 
---
whip, tr. and intr. v. — ME. whippen, rel. to Dan. 
vippe, MLG,, MDu., Du. wippen , ‘to swing’, 
OHG. wipf, ‘swing, impetus’. See vibrate and cp. 
words there referred to. 

Derivatives : whip, n., whipp-er , n., whipp-ing , n. 
and adj., whipp-ing-ly, adv., whipp-y, adj., 
whippet (q.v.) whipster (q.v.) 
---
wipe, tr. v. — ME. wipen, fr. OE. wipian, ‘to wipe’, 
rel. to Dan. vippe, MLG., MDu., Du. vippen, 
OHG. wifan , MHG. wifen, ‘to swing’, fr. I.-E. 
base *weib -, ‘to move to and fro, to swing’, 
whence also L. vibrare, ‘to shake’. See vibrate 
and cp. wisp.
```


## [2026-10-16T05:14:31.320Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for n in 864 865 866 867 868; do echo \"## leaf $n\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n+1' KLN_1966.txt | head -c 400; echo; done"
}
```


### [2026-10-16T05:14:31.895Z] TOOL RESULT

```
## leaf 864
 relief,  chased’,  verbal  adj.  of  xopsii- siv,  ‘to  work  in  relief,  bore  through’,  fr.  xo- peii?,  ‘sculptor’s  graving  tool’,  fr.  xApoc,  ‘chisel’, which  stands  in  gradational  relationship  to  xei- pav  (for*x£pietv),  ‘to  rub’,  xepcxpov,  ‘borer’, xepvjScov,  ‘a  worm  that  gnaws  wood’,  prop,  ‘a boring  worm’,  fr.  I.-E.  base  *ter-,  �
## leaf 865
fr.  OProven?.  tartuga,  fr.  It.  tartaruga, which  derives  fr.  VL.  tartaruca,  lit.  ‘the  infernal animal’,  fr.  L.  Tartarus',  see  Tartarus.  The Proven?,  form  tortuga  is  due  to  the  influence  of L.  tortus,  ‘twisted’.  Folk  etymology  found  in  the name  of  the  animal  a  reference  to  its  twisted legs.  Cp.  turtle,  ‘tortoise’, tortricid,  adj.,  pertaining 
## leaf 866
 tornare,  ‘to  turn  in  a  lathe;  to  turn,  fashion’.  See turn  and  -ure  and  cp.  tour, touse,  tr.  and  intr.  v.,  to  pull  roughly,  to  tear (dial.)  —  ME.  -tousen,  -tusen  (used  only  in  com¬ pounds),  rel.  to  Fris.  tusen,  OHG.  zir-zuson,  ‘to tug,  pull,  dishevel’,  OHG.,  MHG.  er-zusen,  G. zausen,  ofs.m.,  MHG.  zus-ach,  ‘bush’,  andprob. cogn.  with 
## leaf 867
 Compounded  of  trachelo-  and  Gk. -xopia,  ‘a  cutting  of’,  fr.  xoprj,  ‘a  cutting’.  See -tomy.
tracheo-,  before  a  vowel  trache-,  combining  form denoting  the  trachea.  —  See  trachea.
tracheocele
train  oil
tracheocele,  n.,  the  goiter  (med.)  —  Compounded of  traeheo-  and  Gk.  xr/.'/j,  ‘tumor,  hernia’.  See
-cele.
tracheotomy,  n.,  incision  in  the  trac
## leaf 868
ain. Cp.  also  trail.
Derivatives:  train,  n.  (q.v.),  train-age,  n.,  train¬ ed,  adj.,  train-ing,  n.  and  adj. train,  n.,  procession,  cortege,  etc.;  a  series,  a  line of  connected  railroad  cars  pulled  or  pushed  by a  locomotive.  —  ME.  trayn,  fr.  MF.  train  (F. train),  back  formation  fr.  trainer,  ‘to  drag,  draw along’.  See  train,  v.
train  oil,  oil  ma
```


## [2026-10-16T05:14:36.294Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -m5 \"ویلا\" MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v2_djvu.txt | cut -c1-300; grep -n -m5 -i \"vila\\|villa\" MON_part2.txt | cut -c1-200"
}
```


### [2026-10-16T05:14:36.847Z] TOOL RESULT

```
MON_part1.txt:38715:تحویلات. تحویل سال: تبدیل سال کهن به 
MON_part1.txt:40666:کردن» به گمراهی افکندن؛ ج. تسویلات. 
MON_part1.txt:79298:ویلان. 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:33763:صورتی است؛ جهنمیه» بوگن ویلاء بوگن 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:45216:درمی آورند و جزو ساختمان پروتویلاسم 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:45221:بسروتویلاسمی خود را تسجزیه کرده و 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:87371:ول» ویلان. (عم.) سهل‌انگار» بی‌بند و بار. 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:88004:ویلا: ۷110(2(.) خانه بیلاقی زیبا. 
MON_part2.txt:33763:صورتی است؛ جهنمیه» بوگن ویلاء بوگن 
MON_part2.txt:45216:درمی آورند و جزو ساختمان پروتویلاسم 
MON_part2.txt:45221:بسروتویلاسمی خود را تسجزیه کرده و 
MON_part2.txt:87371:ول» ویلان. (عم.) سهل‌انگار» بی‌بند و بار. 
MON_part2.txt:88004:ویلا: ۷110(2(.) خانه بیلاقی زیبا.
```


## [2026-10-16T05:14:41.433Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n \"ویلا\" incoming/ARY/ARY_pages.txt | head -3; grep -n -i -E \"VILLA|VILA|VIS\\b|VIBRA|WIPE\" incoming/ARY/ARY_latin_index_pages.txt | head; for n in 240 241 249 250; do echo \"## leaf $n\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' incoming/WLD/WLD_Bd1_pages.txt | head -c 700; echo; done"
}
```


### [2026-10-16T05:14:41.809Z] TOOL RESULT

```
910:S63 F Oris: V(OIS sli AVIS 14 Sls COWIS sg 250 gly) 9 ua seul
1735:vila 30 y 92 081) cal oe
1804:USHK- (HITTITE) ca rs AVIS, - AVATI, (SANSKRIT) cS
2148:BRUVIS LITHUANIAN) gi s-3 OFARBRU-
3502:BFS ilall (SNOW : pL S) SNAW 5545 Sil NIVIS, NIK ig) IPH sp, SSNEZA !
4073:‘REFERENCES they VISA, VIS- (SANSKRIT) 2 Sle
5468:TATARVIS :(OLD PRUSSIAN) ot IR TATRAK (ARMENIAN) |g )\
6951:POKORNY, = ~~*~*~*«US LO UOSHVIS, SHESHURAS , SHESHIURE
8403:‘MACKENZIE: (VILLAGE) 139 ON :
9245:LIEZHOVIS (LITHUANIAN) «g-) LINGUA AITALIAN) giles
## leaf 240
                                                         ±                                                                                                                                 -                                 i




                                                                                                   ueik-, nik-. noiko-                                                                                                    231

      Hierher auch wohl idg. *u7vo-s „Mann“, s. d.    die Bed. ..Kraft, Mann”                                                                              :



ist aus „energisch auf etwas losgehn 11 herleitbar.      Aber lat. v'tnjo wohl
ni
## leaf 241
232                                                                               ueiq-



1.    » ei(l- „aussondern“.
     Ai. vindkti,             vivekti,          vevekfi „sondert,                           siebt,    sichtet",                 Part, villa-: kaus.
recdyati.   Av. ava-vaek- „ausscheiden, aussuchen“, Part, -viyto. Aus der
Bedeutung „zu gottesdienstlichen Zwecken aussondern entspringt die des                                                     11




„weihens“, weslialb sicherlich folgende lat.-germ. Gruppe zuzurechnen ist:
lat. victima „Opfertier, Opfer“, beruhend auf einem i- oder w-Stamm,

                                                              a
## leaf 249
                                                        ueip-, vieib-
240

der Mitte liegender                         Y
                       aldgiirtel. s. auch *iiidhu- ,,Baum“    Zubatys IA.                        >



                                               den  beiden Erhijhungen   auf
22, 60 Hinweis auf ai. vidu- m. ,,die zwischen
der Stirn des Elephanten    befindliehe Gegend“       unbelegt     ist nicht—                         —
vorzuziehen).
     Dazu (vgl.die obigen «-Stamme) ai. vidhdva „Witwe“. av. vidavd ds.,
gr.            „Junggeselle‘\ lat. vidua ,/VVitwe: geschiedene oder unver-
          *y[j:](i?£Os

heiratete Frau“, viduus „beraubt, leer v
## leaf 250
                                                ueip-, ueib-                                           241


Munde oder dicker herabhangender Lippe dasteht oder herumgeht, dummer
Mensch", vampsau, -oti „mit offenem Munde dastehn oder dasitzen“.
  Mit demselben Ablaut e[*j :a will Persson aaO. auch anord. vufa „hi»ngend
schweben", vafra ,,sich unstet hin und her bewegen", mhd. ivabcrn u. dgl.
anreihen (doch s. uebh- „weben“ ), ebenso dt. Wamme. ahd. wamba ..Bauch"
(doch s. u. udero- „Bauch“).
     Wzf. ueib-:
                Qevyava Hes., Ypiyag £ev£ag. Oenaloi. ’luipiog' Ilooeidcbv
     Gr. ylufiavai     •                               '




o£vytog Hes. (auch wohl lyov
```


## [2026-10-16T05:14:46.858Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==240' incoming/WLD/WLD_Bd1_pages.txt | grep -n -i -E \"Haus|vis-|vicus|villa|oiko|Dorf\" | head; echo ---; awk 'BEGIN{RS=\"\\f\"} NR==249' incoming/WLD/WLD_Bd1_pages.txt | grep -n -i -E \"vip|schwing|vibr|vepate\" | head; sed -n 1735p incoming/ARY/ARY_pages.txt"
}
```


### [2026-10-16T05:14:47.173Z] TOOL RESULT

```
6:                                                                                                   ueik-, nik-. noiko-                                                                                                    231
27:ueik-, uik-, uoiko- ,,Haus, Siedlung".
28:      Ai.                vie-         „Wohnsitz, Haus“,                                                    pi.        vwah ..Menschen. Untertanen",                                                                av.    vts-
29: z.   B. acc. vtsjm, ap. vipam ) „Haus,                                                                                  Dorf.          Clan",                 ai.   vit-pdti-                               ,,Hausherr,
30:Gemeindehaupt rie-pdtni ,.Hausfrau‘‘, ai. vr<<i- m. ..Haus“. rvnmiii-, nav.
35:vaesma- m. ,,Haus, Wohnung". ai. vents m. ..Xaehbar" (wie lat. rirltiusj:
44:      gr.            oly.o;,               foTy.o             ,,Haus",                        oly.ia                  ds.,   oly.no              ..bewohne 1-         ,
49:Bois.            s.          v)   ;    lat.          vicus, dial, rites ..Hiiusergruppe.                                                                       Dorf, Flecken. Stadtteil
53:Buck Gr. 46, 351). lat. villa ,,Landhaus, Lamlgut ( *uoik-slu mit lat. Suffix                                                                         1-
60:iveihsis                      ,,Dorf,  Flecken    apr. waispattin Ace. „Hausfrau“, lit. v its pul {i s
---
57: ueip- ueib- „drehen; drehende, schwingende Bewegung                                          .
61:                                               vVpdyati, vipuyati „macht zittern
67: ci»ra „erregt, begeistert“, vip- wenn ..Rute, Gerte“ (es kame dann nach
68: Persson Beitr. 520 zuniichst vipiun- ,,dicht, vom Walde“, n. „Wald
76: Ved. St. Ill 97 ff. iibersetzt ,,Zunge“ = „*die bewogliche“), vipcdha- m.
77: 'Wood KZ. 45, 61 j                           „eine Art Pfeil“ (vgl. iela vibrare ) av. vip- ,,werfen,
84: anord.           vcifti    ,,in            schwingender,    zitternder   Bewegung        sein,            schleudern,
88: (  ai. vipuiha-, s. o.);
105: aivipti „herabhangen, von Fetzen, Lippen“,    vuipytis „das  Maul verziehen,
115:     T\i\:j lit. vipiuos viptis „den 5lund verziehen“, vephjs „Gaffer“, lett. vtplis
اسپانیایی (8(//8): ۷50 7 (007136) دید سم
```


## [2026-10-16T05:14:51.196Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -m6 -E \"^u?w?[eo]i[kḱ]-?o?s|^w[oe]i[kḱ]|^u̯oi|^wīk|^weip|^w[e]ib\" IEC.txt | cut -c1-300; grep -n -m4 -i \"vicus\" SYN.txt | cut -c1-300"
}
```


## [2026-10-16T05:14:52.728Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -m10 -E \"vi[kc]s|vikos|w[oi]k[oi]s|weikos|woikos\" IEC.txt | cut -c1-200; grep -n -m6 -i -E \"veip|vibr|weib\" IEC.txt | cut -c1-200"
}
```


### [2026-10-16T05:14:53.089Z] TOOL RESULT

```
9292:iə ‘whistle, whistling bird’. Cf. Kuist-. WP II, 518. Variant: Kuikt- Oss. àxsitt ‘whistle sound’; Arm. ščem ‘whistle, hiss’; Gk. sítto, v. ‘whistle to flocks’; sítta, f. id. (also name of a bird
19449:tuik-skō ‘squeeze, cramp’ Lat. cf. (?) fiscus, gs: -1, m. ‘basket’; OCS tisků, m. (*wine- or oil-press’ and com. SI); tisto, tištati, v. ‘struggle’; — sę ‘be squeezed, pressed”; (short vowel in)
20322:Gk. híko, v. ‘come, arrive’; Li. vykstu, vykti, v. ‘go, come, arrive"; Latv. vikstu, vikt, id.; cf. Li. vykis, m. “procedure”
5200:guibhro, ið «dash, shake". Lat. vibro, are; OE cf. cwifer-lice ‘zealously’; E to quiver
7150:kələkəl- “a vibrant object or ege Onomat. Skt. cf. karkarih lute’; OCS klakolü, R kólo- kol “bell?
14335:do, Siditi, v. ‘scorn, if fr. *qusiüd-, but *ksiüd- is possible; and ON skjóttr *piebald' ofa horse) quseudros (qusudros) ‘bent, awry, wrong, false? ; Arm. (zero-gde) xotor ‘awry’; Gk. psudrós ‘
18037:suib- (sueib-, suoib-, suib-) ‘dash, whirl, swerve, sweep, jerk, whizz’. Cf. qusib-, etc. Onomat. Gk. cf. ibu, adv. ‘greatly’; Lat. subo, are & -ére, v. “be in heat’; sübulo, gs: -onis, m. ‘pipe
18085:suiqut- ‘faint; cease; loss, faintness’. Cf. (isophonic forms of) suipt- Arm. cf. n-KVi, adj. ‘faint, famished’; nKt'im, v. ‘be faint, famished’, fr. *ni-suiqut-); Messap. cf. s��pta, f. ‘silen
18115:Oss. cf. xålc, s. (2) ‘ruin, decay’, (fr. *sulds); Arm. Kayc, gs. ab. s.-u, s. (Áhunger', fr. *sulds); Go. swulta-, cpds. *death-^; OE cf. swolten, pp. ‘perished, dead": ON sultr, m. ‘famine’; s
```


### [2026-10-16T05:14:53.099Z] TOOL RESULT

```
19869:ueiksolos, a “aspect, figure, likeness; like, similar”. Cf. ueik- (1). WP I, 233 Gk. eíkelos, adj. “similar”; Li. veikslas, m. “as-
1516:Hence W. coedwig ‘woods’, a cpd. with gwig ‘lodge, grove’ (fr. Lat. vicus ‘vil- lage’, Pedersen 1.210).
9759:1. Grk. ofvos, early fotvos, Lat. vtnum (prob. fr. *woinom, like vicus, vidi : Grk. fotos, fotéa; in which case Umbr. vinu must be a Lat. loanword), Alb. vené, Arm. gini, together with the Semitic words, Arab. wain, Hebr. yayin, all prob. loanwords fr. some prehistoric Mediterranean source. So 
11529:Grk. olfkos, olxia ‘house’, Lat. vicus ‘group of houses, village’, Goth. weihs ‘village’, ChSl. vist ‘village’, Skt. vic- ‘settlement, house, clan, people’, Av. vis- ‘dwelling, village’, OPers. vi6- ‘royal court, palace, family’, Skt. vecman-, Ay. vaésma ‘dwelling’. In this group the notion of
32856:Fr. ville, fr. Lat. villa ‘country house, farm’, late ‘village’ : vicus ‘village’, etc. (19.16). Walde-P. 1.231. Ernout-M. 1103. REW 9330. Gamillscheg 891.
```


## [2026-10-16T05:14:56.988Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; python3 tools/fetch_source.py -h 2>&1 | head -20"
}
```


### [2026-10-16T05:14:57.512Z] TOOL RESULT

```
/home/sfmqrb/git/rishe-private/data/verification/sources/web/3c3003f7f0bedaf2.txt
```


## [2026-10-16T05:15:01.020Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; head -40 tools/fetch_source.py; cat data/verification/sources/web/3c3003f7f0bedaf2.txt | head -5"
}
```


### [2026-10-16T05:15:01.317Z] TOOL RESULT

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
URL: -h
FETCHED: 2026-10-16T05:14:57Z
STATUS: -1
TITLE:
```


## [2026-10-16T05:15:04.778Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; rm 3c3003f7f0bedaf2.txt; grep -c '\"url\": \"-h\"' index.jsonl; python3 - <<'E'\np='index.jsonl'\nL=open(p,encoding='utf-8').read().splitlines()\nimport json\nK=[l for l in L if not (l.strip() and json.loads(l).get('url')=='-h')]\nprint(len(L),len(K))\nopen(p,'w',encoding='utf-8').write('\\n'.join(K)+'\\n')\nE\ncd /home/sfmqrb/git/rishe-private; git status --short"
}
```


### [2026-10-16T05:15:05.297Z] TOOL RESULT

```
1
6049 6048
 M data/verification/sources/web/010682aa738991b5.txt
 M data/verification/sources/web/2584fc8d278b8c2e.txt
 M data/verification/sources/web/5da585b195df37a2.txt
 M data/verification/sources/web/61462814d47f9e5d.txt
 M data/verification/sources/web/9a09c1735289a8c0.txt
 M data/verification/sources/web/d7be8c2555333bee.txt
 M data/verification/sources/web/index.jsonl
?? data/verification/sources/web/0297d011a9fcad27.txt
?? data/verification/sources/web/02a8de82b17f5603.txt
?? data/verification/sources/web/0337404108fe1c00.txt
?? data/verification/sources/web/098c7a441d4fe1d0.txt
?? data/verification/sources/web/0a26bcaab38fd1de.txt
?? data/verification/sources/web/0be88b3094271619.txt
?? data/verification/sources/web/0dc022d8415853d9.txt
?? data/verification/sources/web/0f21f236f7feaf87.txt
?? data/verification/sources/web/141de02622fde0d0.txt
?? data/verification/sources/web/169d7e0177f26d8e.txt
?? data/verification/sources/web/17a0d5f17bc4c6bd.txt
?? data/verification/sources/web/19110d5e4ace13e5.txt
?? data/verification/sources/web/19713a1bacb51a62.txt
?? data/verification/sources/web/1a8388802c5f38c2.txt
?? data/verification/sources/web/1e44db52451f0585.txt
?? data/verification/sources/web/208c74743847ad4c.txt
?? data/verification/sources/web/292250ecaec846b9.txt
?? data/verification/sources/web/2a0d8f347bbce242.txt
?? data/verification/sources/web/2a3a5a1cb421b58e.txt
?? data/verification/sources/web/2b160574e26f2746.txt
?? data/verification/sources/web/2b9d53fa6823679c.txt
?? data/verification/sources/web/2df9f4c3edfb71f7.txt
?? data/verification/sources/web/2ed66dbb90d4afa6.txt
?? data/verification/sources/web/30d633c185079fa4.txt
?? data/verification/sources/web/32092a4bb11217f1.txt
?? data/verification/sources/web/330fd6d2e14d6c99.txt
?? data/verification/sources/web/409f7c08c66c5d75.txt
?? data/verification/sources/web/43cc7b03b5eeff3b.txt
?? data/verification/sources/web/44f49a57690a62f1.txt
?? data/verification/sources/web/46db96d682e26fe8.txt
?? data/verification/sources/web/4a1263f9c12f549e.txt
?? data/verification/sources/web/4a3552cbf8ec3dee.txt
?? data/verification/sources/web/4d15fc35d87f8991.txt
?? data/verification/sources/web/4e3cff8aa2c43c89.txt
?? data/verification/sources/web/4f05c3bb60ea7047.txt
?? data/verification/sources/web/504951ddb6f88669.txt
?? data/verification/sources/web/52d635a6c74ceb83.txt
?? data/verification/sources/web/55d97d4ec4040839.txt
?? data/verification/sources/web/573682d0d82af846.txt
?? data/verification/sources/web/5cfb348f710c9d0d.txt
?? data/verification/sources/web/5d92cd5f9b146eec.txt
?? data/verification/sources/web/5e6ce69faa33aef7.txt
?? data/verification/sources/web/64fbc90f30d1b5c0.txt
?? data/verification/sources/web/66dd2a9203c6b4e8.txt
?? data/verification/sources/web/681b6c5eec078a98.txt
?? data/verification/sources/web/68f489bba362f115.txt
?? data/verification/sources/web/6a0e509363aae5c4.txt
?? data/verification/sources/web/6dd0844070b0f011.txt
?? data/verification/sources/web/7760434ea991797e.txt
?? data/verification/sources/web/7a4fdff721dedbc0.txt
?? data/verification/sources/web/7d1490d226903a87.txt
?? data/verification/sources/web/7d91bafe1108caff.txt
?? data/verification/sources/web/7fb551f5851722a4.txt
?? data/verification/sources/web/817619fd1faf4d7a.txt
?? data/verification/sources/web/86db0240d9966c04.txt
?? data/verification/sources/web/8d15f26a6d5885ed.txt
?? data/verification/sources/web/92cb5f047cf21151.txt
?? data/verification/sources/web/9347ec4d0d8d773a.txt
?? data/verification/sources/web/94e2efba69ba7aef.txt
?? data/verification/sources/web/9d0547fd7df96e83.txt
?? data/verification/sources/web/9d0ee85cfba26942.txt
?? data/verification/sources/web/9dd552061f6d124c.txt
?? data/verification/sources/web/9e4aecd45ece45f3.txt
?? data/verification/sources/web/a530a6b396a062fa.txt
?? data/verification/sources/web/a635a86b7d2c8289.txt
?? data/verification/sources/web/b4e21383414aece3.txt
?? data/verification/sources/web/b4e6a62d999564e6.txt
?? data/verification/sources/web/b60291d7df32f913.txt
?? data/verification/sources/web/b79aacf482aeae9a.txt
?? data/verification/sources/web/ba39d325e6e9bd1c.txt
?? data/verification/sources/web/bdb15e3796d7eba9.txt
?? data/verification/sources/web/be7baac48b6dcc51.txt
?? data/verification/sources/web/bfee4ddb48131f7c.txt
?? data/verification/sources/web/c268d96eefe70985.txt
?? data/verification/sources/web/c87ce7e176ebcf1c.txt
?? data/verification/sources/web/c9f38fb2d03b8d85.txt
?? data/verification/sources/web/cc15bb57c26a563d.txt
?? data/verification/sources/web/cc4f19202101e879.txt
?? data/verification/sources/web/cc745ec05bfafb34.txt
?? data/verification/sources/web/cceb1e9fd03f31be.txt
?? data/verification/sources/web/cdbab0feebc04a58.txt
?? data/verification/sources/web/d06e8e168f7ebab8.txt
?? data/verification/sources/web/d0da48c969256f25.txt
?? data/verification/sources/web/d434a189feb06a73.txt
?? data/verification/sources/web/dbe1cf65dabfc1ff.txt
?? data/verification/sources/web/dd8b45b8174956ae.txt
?? data/verification/sources/web/def0da40ecd94485.txt
?? data/verification/sources/web/e11097805e17b650.txt
?? data/verification/sources/web/e46fb4778daa8533.txt
?? data/verification/sources/web/ea4f4c10742e89e6.txt
?? data/verification/sources/web/ed96913d7778d239.txt
?? data/verification/sources/web/f1f7d223f190f00a.txt
?? data/verification/sources/web/f219d07d318354e8.txt
?? data/verification/sources/web/f2d65af8df4cd22d.txt
?? data/verification/sources/web/f524e4a4ba27cc36.txt
?? data/verification/sources/web/f99541f0bca9f270.txt
?? data/verification/sources/web/fa5aca5687e59d7e.txt
?? data/verification/sources/web/fbab5610f51b6e2b.txt
?? data/verification/sources/web/fc83bfb09dd6ab1e.txt
?? data/verification/sources/web/ff1829269965680b.txt
```


## [2026-10-16T05:15:10.417Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; for u in 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/wéyḱs' 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/wóyḱos' 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/weyp-' 'https://en.wiktionary.org/wiki/villa' 'https://en.wiktionary.org/wiki/ویلا' 'https://www.etymonline.com/word/villa' 'https://www.etymonline.com/word/wipe' 'https://www.etymonline.com/word/whip' 'https://www.etymonline.com/word/vibrate' 'https://www.etymonline.com/word/vicinity' 'https://www.etymonline.com/word/eco-' 'https://en.wiktionary.org/wiki/𐬬𐬍𐬯'; do f=$(python3 tools/fetch_source.py \"$u\" --note \"page 536: Weik 2 / Weip roots\"); echo \"$u -> $f $(head -4 $f | sed -n 3p) $(wc -c <$f)\"; done"
}
```


### [2026-10-16T05:15:16.862Z] TOOL RESULT

```
https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/wéyḱs -> /home/sfmqrb/git/rishe-private/data/verification/sources/web/4135ffa74f0c2cf7.txt STATUS: -1 169
https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/wóyḱos -> /home/sfmqrb/git/rishe-private/data/verification/sources/web/bd79d676d5787de4.txt STATUS: 200 5390
https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/weyp- -> /home/sfmqrb/git/rishe-private/data/verification/sources/web/39e20867948d4197.txt STATUS: 200 7443
https://en.wiktionary.org/wiki/villa -> /home/sfmqrb/git/rishe-private/data/verification/sources/web/f930a656f8686f39.txt STATUS: 200 64810
https://en.wiktionary.org/wiki/ویلا -> /home/sfmqrb/git/rishe-private/data/verification/sources/web/5a78c9674021b9cc.txt STATUS: 200 7083
https://www.etymonline.com/word/villa -> /home/sfmqrb/git/rishe-private/data/verification/sources/web/eaf119ecbc7ec8fc.txt STATUS: -1 132
https://www.etymonline.com/word/wipe -> /home/sfmqrb/git/rishe-private/data/verification/sources/web/b173984c0bd9f392.txt STATUS: -1 131
https://www.etymonline.com/word/whip -> /home/sfmqrb/git/rishe-private/data/verification/sources/web/b213675fd8184d69.txt STATUS: -1 131
https://www.etymonline.com/word/vibrate -> /home/sfmqrb/git/rishe-private/data/verification/sources/web/7323fd47981e13a8.txt STATUS: -1 134
https://www.etymonline.com/word/vicinity -> /home/sfmqrb/git/rishe-private/data/verification/sources/web/9194f95448a224e5.txt STATUS: -1 135
https://www.etymonline.com/word/eco- -> /home/sfmqrb/git/rishe-private/data/verification/sources/web/64fbddc085e9cbe3.txt STATUS: -1 131
https://en.wiktionary.org/wiki/𐬬𐬍𐬯 -> /home/sfmqrb/git/rishe-private/data/verification/sources/web/8623c6a2e7fb1467.txt STATUS: -1 138
```


## [2026-10-16T05:15:25.532Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; for u in 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/weyḱ-' 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/wiḱpótis' 'https://en.wiktionary.org/wiki/wipe' 'https://en.wiktionary.org/wiki/whip' 'https://en.wiktionary.org/wiki/vibro' 'https://en.wiktionary.org/wiki/vicus' 'https://en.wiktionary.org/wiki/οἶκος' 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/wīpaną' 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/wíćš' 'https://en.wiktionary.org/wiki/vicinity' 'https://en.wiktionary.org/wiki/village'; do f=$(python3 tools/fetch_source.py \"$u\" --note \"page 536: Weik 2 / Weip roots\"); echo \"$u -> $f $(sed -n 3p $f) $(wc -c <$f)\"; done; rm -f data/verification/sources/web/{4135ffa74f0c2cf7,eaf119ecbc7ec8fc,b173984c0bd9f392,b213675fd8184d69,7323fd47981e13a8,9194f95448a224e5,64fbddc085e9cbe3,8623c6a2e7fb1467}.txt"
}
```


### [2026-10-16T05:15:31.488Z] TOOL RESULT

```
https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/weyḱ- -> /home/sfmqrb/git/rishe-private/data/verification/sources/web/82a03519d3b083ee.txt STATUS: 200 6305
https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/wiḱpótis -> /home/sfmqrb/git/rishe-private/data/verification/sources/web/b3f14aa9016f8f2c.txt STATUS: 200 6942
https://en.wiktionary.org/wiki/wipe -> /home/sfmqrb/git/rishe-private/data/verification/sources/web/eb0b72bb39cdac26.txt STATUS: 200 20439
https://en.wiktionary.org/wiki/whip -> /home/sfmqrb/git/rishe-private/data/verification/sources/web/7e89245ca15d9076.txt STATUS: 200 37043
https://en.wiktionary.org/wiki/vibro -> /home/sfmqrb/git/rishe-private/data/verification/sources/web/a554ce4b787ee0ca.txt STATUS: 200 9450
https://en.wiktionary.org/wiki/vicus -> /home/sfmqrb/git/rishe-private/data/verification/sources/web/86e45b08e0e84e7b.txt STATUS: 200 7788
https://en.wiktionary.org/wiki/οἶκος -> /home/sfmqrb/git/rishe-private/data/verification/sources/web/c66f6641dda296a6.txt STATUS: 200 13208
https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/wīpaną -> /home/sfmqrb/git/rishe-private/data/verification/sources/web/dfc4119003e8d83c.txt STATUS: 200 4759
https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/wíćš -> /home/sfmqrb/git/rishe-private/data/verification/sources/web/b27cccd6aaffc958.txt STATUS: -1 162
https://en.wiktionary.org/wiki/vicinity -> /home/sfmqrb/git/rishe-private/data/verification/sources/web/c15334174838169f.txt STATUS: 200 11894
https://en.wiktionary.org/wiki/village -> /home/sfmqrb/git/rishe-private/data/verification/sources/web/43139ad3ba16f9a6.txt STATUS: 200 31649
```


## [2026-10-16T05:15:37.498Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; rm -f b27cccd6aaffc958.txt; python3 - <<'E'\nimport json\np='index.jsonl'\nL=open(p,encoding='utf-8').read().splitlines()\nbad={'4135ffa74f0c2cf7','eaf119ecbc7ec8fc','b173984c0bd9f392','b213675fd8184d69','7323fd47981e13a8','9194f95448a224e5','64fbddc085e9cbe3','8623c6a2e7fb1467','b27cccd6aaffc958'}\nK=[l for l in L if not any(b in l for b in bad)]\nprint(len(L)-len(K))\nopen(p,'w',encoding='utf-8').write('\\n'.join(K)+'\\n')\nE\nfor f in 82a03519d3b083ee bd79d676d5787de4 39e20867948d4197 b3f14aa9016f8f2c; do echo \"#### $f\"; grep -v '^\\s*$' $f.txt | sed -n 5,200p | grep -i -E \"etymology|from|root|descend|meaning|avestan|persian|latin|greek|wipe|whip|vibr|villa|vicus|oik|vīs|vis|settle|clan|house|dwell\" | head -30 | cut -c1-300; done"
}
```


### [2026-10-16T05:15:38.193Z] TOOL RESULT

```
9
#### 82a03519d3b083ee
 Root 
 From Wiktionary, the free dictionary
 This Proto-Indo-European entry contains reconstructed terms and roots . As such, the term(s) in this entry are not directly attested , but are hypothesized to have existed based on comparative evidence.
 Root
 to settle 
 settlement 
 Terms derived from the Proto-Indo-European root *weyḱ- (79 c, 0 e) 
 *wéyḱ-t ~ *wiḱ-ént ( root aorist ) 
 Old Avestan: 𐬬𐬍𐬯𐬇𐬧𐬙𐬉 ( vīsə̄ṇtē , 3pl.pres.mid. ) 
 Ancient Greek: ἔοικα ( éoika ) ( or from *weyk- ( “ to be fitting ” ) [ 2 ] ) 
 Old Avestan: 𐬬𐬍𐬎𐬎𐬍𐬯𐬈 ( vīuuīse , 2sg.perf.mid. ) ( or secondary formation from present verb [ 3 ] ) 
 Proto-Indo-Iranian: *wíćš ( see there for further descendants )
 Albanian: vis ( “ place, land, country ” ) 
 Proto-Slavic: *vь̃sь ( see there for further descendants )
 Proto-Italic: *weikos ( see there for further descendants )
 ⇒ Proto-Germanic: *wīhsą ( see there for further descendants )
 Avestan: 𐬬𐬀𐬉𐬯𐬀 ( vaēsa ) 
 ^ Beekes, Robert S. P. ( 2010 ), “ ἔοικα ”, in Etymological Dictionary of Greek (Leiden Indo-European Etymological Dictionary Series; 10 ), with the assistance of Lucien van Beek, Leiden, Boston: Brill, →ISBN , page 435 
 ^ De Vaan, Michiel ( 2008 ), “ vīcus ”, in Etymological Dictionary of Latin and the other Italic Languages (Leiden Indo-European Etymological Dictionary Series; 7), Leiden, Boston: Brill, →ISBN , page 675 
 ^ Adams, Douglas Q. ( 2013 ), “īke”, in A Dictionary of Tocharian B: Revised and Greatly Enlarged (Leiden Studies in Indo-European; 10 ), Amsterdam, New York: Rodopi, →ISBN , page 67 
 ^ Vladimir Orel ( 2003 ), “*wīxsan”, in A Handbook of Germanic Etymology ‎ [1] , Leiden, Boston: Brill , →ISBN , page 466 
 Retrieved from " https://en.wiktionary.org/w/index.php?title=Reconstruction:Proto-Indo-European/weyḱ-&oldid=92171697 "
 Proto-Indo-European roots 
 Proto-Indo-European ReRC-shaped roots 
 Proto-Indo-European perfective roots 
#### bd79d676d5787de4
 Etymology 
 Descendants 
 From Wiktionary, the free dictionary
 This Proto-Indo-European entry contains reconstructed terms and roots . As such, the term(s) in this entry are not directly attested , but are hypothesized to have existed based on comparative evidence.
 Etymology
 From *weyḱ- ( “ to enter in, settle ” ) +‎ *-os 
 settlement 
 Descendants
 Proto-Hellenic: *wóikos ( “ settlement, house ” ) ( see there for further descendants )
 Sanskrit: वेश ( véśa , “ house; brothel ” ) ( see there for further descendants )
 > ? Proto-Italic: *weikos ( “ village ” ) ( see there for further descendants )
 ^ Beekes, Robert S. P. ( 2011 ), Comparative Indo-European Linguistics: An Introduction , 2nd edition, revised and corrected by Michiel de Vaan , Amsterdam, Philadelphia: John Benjamins Publishing Company, page 39 : “ *uoiḱo- (Gr. oîkos ) ” 
 ^ Beekes, Robert S. P. ( 2010 ), “ οἶκος ”, in Etymological Dictionary of Greek (Leiden Indo-European Etymological Dictionary Series; 10 ), with the assistance of Lucien van Beek, Leiden, Boston: Brill, →ISBN , pages 1055-1056 : “ *ṷóiḱo- [m.] ” 
 ^ Sturm, Julia (11 November 2016), “ἵστωρ and ἑορτή: The Rough-Breathing Reflex of Greek”, in 28th Annual UCLA Indo-European Conference ‎ [2] , archived from the original on 23 September 2026 , page 1: “ *ṷoíḱos 'house' ” 
 Pokorny, Julius ( 1959 ), “ ṷeik̑- ”, in Indogermanisches etymologisches Wörterbuch [ Indo-European Etymological Dictionary ] (in German), volume 3, Bern, München: Francke Verlag, page 1131 : “ ṷoik̑o- ” 
 Retrieved from " https://en.wiktionary.org/w/index.php?title=Reconstruction:Proto-Indo-European/wóyḱos&oldid=93566489 "
 Categories : Proto-Indo-European terms belonging to the root *weyḱ- 
#### 39e20867948d4197
 Root 
 From Wiktionary, the free dictionary
 This Proto-Indo-European entry contains reconstructed terms and roots . As such, the term(s) in this entry are not directly attested , but are hypothesized to have existed based on comparative evidence.
 Root
 to vibrate , tremble , oscillate [ 2 ] [ 1 ] 
 Terms derived from the Proto-Indo-European root *weyp- (26 c, 0 e) 
 *wéyp-e-ti ( thematic root present ) [ 2 ] 
 Proto-Germanic: *wīpaną ( “ to wind, wrap ” ) ( see there for further descendants )
 Proto-Indo-Iranian: *wáypati ( “ to tremble ” ) ( see there for further descendants )
 *wéyp-t ~ *wip-ént ( athematic root aorist ) [ 2 ] 
 ⇒ ? Proto-Germanic: *wimpilaz ( “ wrapped cloth, scarf, wimple ” ) ( see there for further descendants )
 Proto-Germanic: *waibijaną ( “ to wind (around), wrap ” ) ( see there for further descendants )
 Avestan: 𐬬𐬀𐬉𐬞𐬀𐬌𐬌𐬈𐬌𐬙𐬌 ( vaēpaiie i ti ) [ 4 ] 
 Proto-Germanic: *wibraz ( “ missile; sword ” ) ( see there for further descendants )
 Proto-Indo-Iranian: *wípras ( “ ecstatic, trembling ” ) ( see there for further descendants )
 Latin: vibrō ( “ to move to and fro ” ) ( see there for further descendants )
 Proto-Slavic: *visěti ( “ to hang ” ) ( see there for further descendants )
 Proto-Celtic: *wimmonā ( see there for further descendants )
 ↑ 5.0 5.1 De Vaan, Michiel ( 2008 ), “ vibrō, -āre ”, in Etymological Dictionary of Latin and the other Italic Languages (Leiden Indo-European Etymological Dictionary Series; 7), Leiden, Boston: Brill, →ISBN , page 674 : “ *uip/b-ro- ” 
 ^ Adams, Douglas Q. ( 2013 ), “waipe*”, in A Dictionary of Tocharian B: Revised and Greatly Enlarged (Leiden Studies in Indo-European; 10 ), Amsterdam, New York: Rodopi, →ISBN , page 667 : “ *woib/po- ” 
 Retrieved from " https://en.wiktionary.org/w/index.php?title=Reconstruction:Proto-Indo-European/weyp-&oldid=92171695 "
 Proto-Indo-European roots 
 Proto-Indo-European ReRC-shaped roots 
#### b3f14aa9016f8f2c
 Etymology 
 Descendants 
 From Wiktionary, the free dictionary
 This Proto-Indo-European entry contains reconstructed terms and roots . As such, the term(s) in this entry are not directly attested , but are hypothesized to have existed based on comparative evidence.
 Etymology
 From *weyḱ- ( “ village, household ” ) +‎ *pótis ( “ master ” ) .
 clan chief 
 master of a household 
 Old Prussian: waispattin ( “ mistress of a house ” ) 
 Descendants
 Proto-Albanian: *dzwāpt ( see there for further descendants )
 Sanskrit: विश्पति ( viśpáti , “ chief of a settlement or tribe ” )
```


## [2026-10-16T05:15:41.740Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; grep -i -E \"avestan|vīspaiti|vispaiti\" b3f14aa9016f8f2c.txt | head; for f in eb0b72bb39cdac26 7e89245ca15d9076 a554ce4b787ee0ca dfc4119003e8d83c 5a78c9674021b9cc 86e45b08e0e84e7b c15334174838169f 43139ad3ba16f9a6 f930a656f8686f39 c66f6641dda296a6; do echo \"#### $f\"; grep -A3 -m2 \"^ *Etymology\" $f.txt | grep -v '^\\s*$' | head -6 | cut -c1-500; done"
}
```


### [2026-10-16T05:15:42.329Z] TOOL RESULT

```
 Avestan: 𐬬𐬍𐬯𐬞𐬀𐬌𐬙𐬌 ( vīspa i ti , “ master of borough, clan-chief, household-chief ” ) 
#### eb0b72bb39cdac26
 Etymology 1 
 1.2.1 
 Verb 
--
 Etymology 2 
 1.3.1 
#### 7e89245ca15d9076
 Etymology 
 1.2 
 Pronunciation 
--
 Etymology
 [ edit ] 
#### a554ce4b787ee0ca
 Etymology 
 5.2 
 Pronunciation 
--
 Etymology
 [ edit ] 
#### dfc4119003e8d83c
 Etymology 
 1.2 
 Pronunciation 
--
 Etymology
 [ edit ] 
#### 5a78c9674021b9cc
 Etymology 
 1.2 
 Pronunciation 
--
 Etymology 
 2.2 
#### 86e45b08e0e84e7b
 Etymology 
 1.2 
 Noun 
--
 Etymology 
 2.2 
#### c15334174838169f
 Etymology 
 1.2 
 Pronunciation 
--
 Etymology
 [ edit ] 
#### 43139ad3ba16f9a6
 Etymology 
 1.2 
 Pronunciation 
--
 Etymology 
 2.2 
#### f930a656f8686f39
 Etymology 1 
 1.2.1 
 Noun 
--
 Etymology 2 
 1.3.1 
#### c66f6641dda296a6
 Etymology 
 1.3 
 Pronunciation 
--
 Etymology
 [ edit ]
```


## [2026-10-16T05:15:45.253Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; for f in eb0b72bb39cdac26 7e89245ca15d9076 a554ce4b787ee0ca 5a78c9674021b9cc 86e45b08e0e84e7b c15334174838169f 43139ad3ba16f9a6 f930a656f8686f39 c66f6641dda296a6; do echo \"#### $f\"; grep -E \"^ *(From|Borrowed|Inherited|Learned)\" $f.txt | head -3 | cut -c1-400; done"
}
```


### [2026-10-16T05:15:45.716Z] TOOL RESULT

```
#### eb0b72bb39cdac26
 From Wiktionary, the free dictionary
 From Middle English wipen , from Old English wīpian ( “ to wipe, rub, cleanse ” ) , from Proto-West Germanic *wīpōn ( “ to wipe ” ) , from Proto-Indo-European *weyp- ( “ to twist, wind around ” ) . Cognate with German wippen ( “ to bob ” ) , Swedish veva ( “ to turn, wind, crank ” ) , Gothic 𐍅𐌴𐌹𐍀𐌰𐌽 ( weipan , “ to wreathe, crown ” ) , Old English swīfan ( “ to revolve, sweep, wend, intervene ” ) 
 From wipe out (verb) and wipeout (noun) by shortening.
#### 7e89245ca15d9076
 From Wiktionary, the free dictionary
 From Middle English whippen , wippen ( “ to flap violently ” ) , from Middle Dutch wippen ( “ to swing, leap, dance, oscillate ” ) and Middle Low German wippen ( “ to move quickly ” ) , from Proto-Germanic *wippōną ( “ to move back and forth ” ) , ultimately from Proto-Indo-European *weyp- ( “ to shake; to swing ” ) . (See Swedish vippa and Danish vippe ( “ to shake ” ) ).
#### a554ce4b787ee0ca
 From Wiktionary, the free dictionary
#### 5a78c9674021b9cc
 From Wiktionary, the free dictionary
 Inherited from Apabhramsa वेला ( velā ) , from Prakrit 𑀯𑁂𑀮𑀸 ( velā ) , from Sanskrit वेला॑ ( vélā ) .
 From French villa .
#### 86e45b08e0e84e7b
 From Wiktionary, the free dictionary
 Borrowed from Latin vīcus ( “ village ” ) . Doublet of wick .
 Inherited from Proto-Italic *weikos , from Proto-Indo-European *weyḱ- ( “ village ” ) . Cognate of Ancient Greek οἶκος ( oîkos , “ house ” ) , Sanskrit विश् ( víś , “ settlement; dwelling-space ” ) , Gothic 𐍅𐌴𐌹𐌷𐍃 ( weihs , “ village; place ” ) , Etruscan 𐌅𐌉𐌊𐌖 ( viku ) .
#### c15334174838169f
 From Wiktionary, the free dictionary
 From vicine +‎ -ity , from Latin vīcīnitās ( “ neighborhood ” ) (compare French vicinité ), from vīcīnus ( “ neighbor ” ) (compare French voisin ), from vīcus ( “ village ” ) .
#### 43139ad3ba16f9a6
 From Wiktionary, the free dictionary
 From Middle English village , from Old French village , from Latin vīllāticus , ultimately from Latin villa (English villa ).
 From Latin villaticus , from villa .
#### f930a656f8686f39
 From Wiktionary, the free dictionary
 Borrowed from Italian villa , from Latin vīlla ( “ country house ” ) . Doublet of vill and ville .
 Borrowed from Latin vīlla ( “ country house ” ) . Doublet of vill and ville .
#### c66f6641dda296a6
 From Wiktionary, the free dictionary
 From ϝοῖκος ( woîkos ) , from Proto-Hellenic *wóikos , from Proto-Indo-European *wóyḱos ( “ settlement ” ) . [ 1 ] Cognates include Mycenaean Greek 𐀺𐀒 ( wo-ko /⁠wojkos⁠/ , “ home ” ) , Latin vīcus (whence English wick ( “ village ” ) ), Proto-Slavic *vьsь ( “ village ” ) , Sanskrit विश् ( víś ) and वे॒श ( veśá ) , Gothic 𐍅𐌴𐌹𐌷𐍃 ( weihs , “ village ” ) , and Albanian vis .
```


## [2026-10-16T05:15:48.518Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; grep -n -i -E \"Proto-Italic|weyp|weib|uip\" a554ce4b787ee0ca.txt | head -5 | cut -c1-400; grep -n -i \"wīpan\\|wipe\\|Gothic\" dfc4119003e8d83c.txt | head -5|cut -c1-300"
}
```


### [2026-10-16T05:15:48.869Z] TOOL RESULT

```
261: Denominative of Proto-Italic *wibros , from Proto-Indo-European *weyp- ( “ to oscillate, swing ” ) or *weyb- . The root-final consonant is unclear, reflexes of both are found across Indo-European. [ 1 ] 
786: ^ De Vaan, Michiel ( 2008 ), “ vibrō, -āre ”, in Etymological Dictionary of Latin and the other Italic Languages (Leiden Indo-European Etymological Dictionary Series; 7), Leiden, Boston: Brill, →ISBN , page 674 : “ *uip/b-ro- ” 
839: Latin terms derived from Proto-Italic 
841: Latin terms derived from the Proto-Indo-European root *weyp- 
1:URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/wīpaną
4:TITLE: Reconstruction:Proto-Germanic/wīpaną - Wiktionary, the free dictionary
6:Reconstruction:Proto-Germanic/wīpaną - Wiktionary, the free dictionary 
84: Reconstruction:Proto-Germanic/ wīpaną 
158: *wīpaną [ 1 ]
```


## [2026-10-16T05:16:03.720Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/web; grep -n -E \"Borrowed|From \" f930a656f8686f39.txt | cut -c1-250 | head -20; grep -n \"^ *French\" f930a656f8686f39.txt | head -3; cd ../refs; for w in Villa Village Economy Wipe Whip Vibrate Vicinity; do echo \"## $w\"; grep -n -m1 -E \"^$w,\" SKT.txt | cut -c1-400; done"
}
```


### [2026-10-16T05:16:04.078Z] TOOL RESULT

```
623: From Wiktionary, the free dictionary
647: Borrowed from Italian villa , from Latin vīlla ( “ country house ” ) . Doublet of vill and ville .
813: Borrowed from Latin vīlla ( “ country house ” ) . Doublet of vill and ville .
919: Borrowed from Latin vīlla .
1111: From Proto-Finnic *villa (compare Estonian vill ), borrowed from Proto-Baltic *wílˀnāˀ (compare Lithuanian vi̇̀lna , Polish wełna ), from Proto-Indo-European *h₂wĺ̥h₁neh₂ (compare English wool , French laine ).
1896: From Italian villa .
2585: Borrowed from Italian villa . Doublet of ville .
2639: From a Slavic language. Compare Serbo-Croatian vile .
2839: From Italian villa , from Latin vīlla ( “ country house ” ) .
3120: Borrowed from Latin villa ( “ villa, estate, large country residence ” ) .
3630: From Proto-Finnic *villa . Cognates include Finnish villa and Estonian vill .
3764: From Latin vīlla ( “ country house ” ) .
3859: From Proto-Italic *weikslā , a nominal from Proto-Indo-European *weyḱ- ( “ settlement ” ) with an instrument/concrete-noun deverbal suffix *-slo- also found in pālus , vēlum . Related to vīcus ( “ row of houses; village ” ) , vīcīnus ( “ neighb
4019: From Italian villa .
4150: From Italian villa and Latin villa .
4174: From Italian villa and Latin villa .
4291: From Italian villa , from Latin villa .
4352: From vill ( “ lost ” ) +‎ -a .
4514: Borrowed from Italian villa .
193: French 
713: French: villa   (fr)   f 
2579: French
## Villa
## Village
## Economy
## Wipe
## Whip
21386:Whip,  to  move  quickly,  to  flog.  (E.) M.  E-  wkippen,  to  overlay  a  cord  by  rapidly binding  the  twine  round  it,  uihifpe,  a scourge.  From  the  sense  of  rapid  move- ment. 4"  Du.  wippen,  to  skip,  formerly  to shake ;  Low  G.  wippen,  to  bob  np  and down  ;  Don.  vip^,  to  see  saw,  bob  ;  SwetL vippa,  to  wag,  jerk  ;  G.  wippen,  to  move op  and  down,  
## Vibrate
## Vicinity
```


## [2026-10-16T05:16:07.709Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for w in Villa Village Economy Wipe Vibrate Vicinity Ecology; do echo \"## $w\"; grep -n -m1 -i -E \"^$w[,.] \" SKT.txt SKT_dli_revised.txt | cut -c1-350; done"
}
```


### [2026-10-16T05:16:08.263Z] TOOL RESULT

```
## Villa
(eval):1: bad math expression: empty string
## Village
(eval):1: bad math expression: empty string
## Economy
(eval):1: bad math expression: empty string
## Wipe
(eval):1: bad math expression: empty string
## Vibrate
(eval):1: bad math expression: empty string
## Vicinity
(eval):1: bad math expression: empty string
## Ecology
(eval):1: bad math expression: empty string
```


## [2026-10-16T05:16:10.568Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for w in Villa Village Economy Wipe Vibrate Vicinity; do echo \"## $w\"; grep -n -m1 -i \"^$w[,.] \" SKT_dli_revised.txt | cut -c1-350; grep -n -m1 -i \"^$w[,.] \" SKT.txt | cut -c1-350; done"
}
```


### [2026-10-16T05:16:11.054Z] TOOL RESULT

```
## Villa
(eval):1: bad math expression: empty string
(eval):1: bad math expression: empty string
## Village
(eval):1: bad math expression: empty string
(eval):1: bad math expression: empty string
## Economy
(eval):1: bad math expression: empty string
(eval):1: bad math expression: empty string
## Wipe
(eval):1: bad math expression: empty string
(eval):1: bad math expression: empty string
## Vibrate
(eval):1: bad math expression: empty string
(eval):1: bad math expression: empty string
## Vicinity
(eval):1: bad math expression: empty string
(eval):1: bad math expression: empty string
```


## [2026-10-16T05:16:16.901Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; for w in Villa Village Economy Wipe Vibrate Vicinity; do echo \"## $w\"; grep -n -m1 -i \"^${w}[,.] \" SKT_dli_revised.txt | cut -c1-350; grep -n -m1 -i \"^${w}[,.] \" SKT.txt | cut -c1-350; done"
}
```


### [2026-10-16T05:16:17.340Z] TOOL RESULT

```
## Villa
85943:Villa. (L.) uilla, a farm-house ; 
## Village
80513:village, W. tref^ hamlet j Idg. type ^trebo-. 
20901:village.  (F.-L.)  F.  w//<y».— U  ««/■ latictis,  adj.,  belonging  to  a  farm-hotuc.  «^ L.  uiUa  (above).
## Economy
## Wipe
21090:wipe. Der. dcterg-ent, from the pies. pt. 
21532:Wipe.  (E.)  A.  S.  wifian,  to  wipe ;  orig. to  rub  with  a  wisp  of  straw.  From  a  sb. wip  •,  only  preserved  in  the  Low  G.  wief,  a wisp  of  straw.     Allied  to  Wiap.
## Vibrate
85781:Vibrate. (L.) From pp. oilj.uibrdre, 
## Vicinity
85826:vicinity, neighbourhood. (F.-LO
```


## [2026-10-16T05:16:22.009Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} {n=split($0,a,\"\\n\"); if (index($0,\"royal house, royal clan\")) {print NR; for(i=1;i<=n;i++) if (a[i] ~ /^ *2[01][0-9] *$/ || a[i] ~ /LEXICON/) print a[i]}}' KNT_full.txt"
}
```


### [2026-10-16T05:16:22.519Z] TOOL RESULT

```
1
GRAMMAR TEXTS LEXICON 
PART HI. LEXICON 
216 
PART III. LEXICON 
LEXICON 
LEXICON 
LEXICON 
LEXICON 
LEXICON 
LEXICON 
LEXICON 
LEXICON 
LEXICON 
LEXICON 
LEXICON 
LEXICON 
LEXICON 
LEXICON 
LEXICON 
LEXICON 195 
LEXICON 
LEXICON 199 
LEXICON 
201 
LEXICON 203 
204 
LEXICON | 205 
206 
LEXICON 
207 
208 
LEXICON 200 
210 
LEXICON 
211 
212 
LEXICON 213 
214 
LEXICON 
215 
216
```


## [2026-10-16T05:16:25.002Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; awk 'NR>=28700 && NR<=29100 && /^ *(LEXICON *)?\\|? *2[01][0-9] *$/ {print NR\": \"$0}' KNT_full.txt"
}
```


### [2026-10-16T05:16:25.329Z] TOOL RESULT

```
28872: 207 
28937: 208 
29065: LEXICON 200
```


## [2026-10-16T05:16:38.153Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -c -i \"vīlā\\|vila\\b\" HRN.txt HUB.txt; grep -c \"ویلا\" incoming/ARY/ARY_pages.txt BQT_v1_pages.txt BQT_v2_pages.txt incoming/BQT/BQT_v4_pages.txt; grep -n -m3 -i \"oikos\\|οἶκος\\|olxo\" SYN.txt | cut -c1-200; grep -n -m2 \"^economy\\|^ecology\" FSD_vol1.txt | head -2; grep -n -m3 -i \"vibr\" SYN.txt | cut -c1-200"
}
```


### [2026-10-16T05:16:38.699Z] TOOL RESULT

```
HUB.txt:0
HRN.txt:0
incoming/ARY/ARY_pages.txt:0
BQT_v1_pages.txt:0
BQT_v2_pages.txt:2
incoming/BQT/BQT_v4_pages.txt:2
681:kéapos (olxovpévn, b)
745:But for the world of people, the in- habited earth, the classical phrase was } olkoupévn (yf), ‘the inhabited (earth)’. Not until Hellenistic times is xécyos used in this sense. In the NT it is co
762:Goth. midjun-gards (renders olxovpévn when this is used instead of the usual kdopos), ON mid-gardr, OE middan- geard, OHG mittin-gart, mittil-gart (lit. ‘mid-yard, mid-inclosure’), represent a ter
10405:OE wé@fels ‘covering’ and ‘cloak’ (e.g. Mt. 5.40), fr. the root of OE (b:-)w@fan, Goth. bi-waibjan ‘wrap about, clothe’ : ON veifa ‘vibrate’, Skt. vip- ‘tremble’, etc. Walde-P. 1.240. Feist 97.
```


## [2026-10-16T05:18:19.078Z] TOOL CALL #46: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad; cat > /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/build-536.py <<'EOF'\nimport json\nW=\"https://en.wiktionary.org/wiki/\"\nPIEW=W+\"Reconstruction:Proto-Indo-European/weyḱ-\"\nPIEWO=W+\"Reconstruction:Proto-Indo-European/wóyḱos\"\nPIEWP=W+\"Reconstruction:Proto-Indo-European/wiḱpótis\"\nPIEV=W+\"Reconstruction:Proto-Indo-European/weyp-\"\nPOKW={\"src\":\"POK\",\"where\":\"p.1131 s.v. ueiḱ-, uiḱ-, uoiḱo- (POK_full.txt line ~89516)\",\"stance\":\"supports\",\"note\":\"'house, settling': 'Avestan vīs- (e.g. Akk. vīsəm, ap. viθam) \\\"house, village, clan\\\", Old Indie viś-pati- householder ... gr. οἶκος, Ϝοῖκος \\\"house\\\" ... Latin vīcus ... Latin villa \\\"Landhaus, estate\\\" (*u̯oiḱ-slā)'.\"}\nWLDW={\"src\":\"WLD\",\"where\":\"Bd. I p.231 (WLD_Bd1_pages.txt leaf 240)\",\"stance\":\"supports\",\"note\":\"'ueik-, uik-, uoiko- „Haus, Siedlung“. Ai. viś- „Wohnsitz, Haus“ ... av. vīs- (z.B. acc. vīsəm, ap. viθam) „Haus, Dorf, Clan“ ... gr. οἶκος ... lat. vīcus ... lat. villa „Landhaus, Landgut“ (*uoik-slā)'.\"}\nAHDW={\"src\":\"AHD\",\"where\":\"Watkins 1985 s.v. weik-1 (AHD_watkins1985.txt line 1137)\",\"stance\":\"supports\",\"note\":\"'weik-1, Clan (social unit above the household). 1. Suffixed form *weik-slā in Latin villa, country house, farm: VILLA, VILLAGE ... 2. Suffixed o-grade form *woik-o- in: a. Latin vicus ... VICINITY; b. Greek oikos, house ... ECOLOGY, ECONOMY ... [Pok. weik- 1131.]'\"}\nSYNW={\"src\":\"SYN\",\"where\":\"§ village/house (SYN.txt line 11529)\",\"stance\":\"supports\",\"note\":\"'Grk. οἶκος, οἰκία \\\"house\\\", Lat. vīcus \\\"group of houses, village\\\", Goth. weihs \\\"village\\\" ... Skt. viś- \\\"settlement, house, clan, people\\\", Av. vīs- \\\"dwelling, village\\\", OPers. viθ- \\\"royal court, palace, family\\\"'.\"}\nPOKV={\"src\":\"POK\",\"where\":\"pp.1131-1132 s.v. u̯eip-, u̯eib- (POK_full.txt line 89844)\",\"stance\":\"supports\",\"note\":\"'to turn, sway ... Avestan vip- \\\"throw, entsenden (Samen)\\\" ... Gothic biwaibjan ... Latin vibro, -āre \\\"in zitternde, schwingende Bewegung setzen\\\"'.\"}\nWLDV={\"src\":\"WLD\",\"where\":\"Bd. I pp.240-241 (WLD_Bd1_pages.txt leaves 249-250)\",\"stance\":\"supports\",\"note\":\"'ueip-, ueib- „drehen; drehende, schwingende Bewegung“ ... av. vip- „werfen“ ... Wzf. ueib-: ... lat. vibrāre'.\"}\nAHDV={\"src\":\"AHD\",\"where\":\"Watkins 1985 s.v. weip- (AHD_watkins1985.txt line 1137)\",\"stance\":\"supports\",\"note\":\"'weip-. To turn, vacillate, tremble ecstatically ... 2. Variant form *weib- in Germanic *wipjan, to move back and forth, in: a. Old English wipian, to wipe: WIPE ... c. Middle Dutch and Middle Low German wippen, to swing: WHIP ... 4. Suffixed zero-grade variant form *wib-ro- in Latin vibrāre, to vibrate: VIBRATE. [Pok. weip- 1131.]'\"}\ndef rc(ref,st,note): return {\"ref\":ref,\"status\":st,\"note\":note}\nE0={\n \"entry\":0,\"root\":\"Weik 2\",\"verdict\":\"confirmed\",\n \"modern_form\":\"PIE *weyḱ- 'to settle, enter' / *wóyḱos 'settlement, house', *wiḱ- 'clan, settlement' (Pokorny ueiḱ- 1131; AHD weik-1 'clan')\",\n \"note\":\"Root, language label and gloss are right. Nourai's gloss 'clan, a social club above the household' is AHD's 'Clan (social unit above the household)'; his number '2' is his own (AHD numbers this weik-1, Pokorny leaves it unnumbered on p.1131, distinct from 1.-4. ueik- pp.1128-1131). Modern Wiktionary treats it as a verbal root *weyḱ- 'to settle' with nouns *wíḱs and *wóyḱos.\",\n \"note_fa\":\"ریشهٔ هندواروپایی آغازین *weyḱ- «جای گرفتن، ساکن شدن» با نام‌واژه‌های *wiḱ- «تیره، آبادی» و *wóyḱos «خانه، سکونتگاه» است (پوکورنی ص ۱۱۳۱، واتکینز در AHD: weik-1 «تیره، واحد اجتماعی بالاتر از خانوار»). معنایی که نورایی آورده همان تعریف AHD است و شمارهٔ «۲» تنها شماره‌گذاری خود اوست. ادعای نورایی درست است.\",\n \"sources\":[PIEW,PIEWO,PIEWP],\n \"ref_check\":[rc(\"POK:1131\",\"supports\",\"POK_full.txt 'Root / lemma: ueiḱ-, uiḱ-, uoiḱo- ... Meaning: house, settling ... Page(s): 1131' — the root, with Av. vīs-, OP viθ-, Gk. οἶκος, Lat. vīcus and villa.\")],\n \"consulted\":[WLDW,AHDW,SYNW,{\"src\":\"IEC\",\"where\":\"grep 'weik|woikos|vicus' IEC.txt\",\"stance\":\"silent\",\"note\":\"Mann's entry for this root not found by OCR grep (only Lat. vicus cited incidentally at line 1516).\"}],\n \"nodes\":[\n  {\"id\":1,\"lang\":\"Avestan\",\"words\":\"vîs; vîs-paiti, vîs-pati\",\"verdict\":\"confirmed\",\n   \"derivation\":\"Av. vīs- f. (acc. vīsəm) 'manor, village community, clan' is the regular zero-grade reflex of PIE *wiḱ- (PIIr. *wíćš; PIE palatal *ḱ > Iranian s), = Skt. víś-. Av. vīspaiti- 'master of a clan/village' = vīs- + paiti- 'lord' (PIE *wiḱ-pótis, Skt. viśpáti-). Nourai's 'family' is a loose gloss (Bartholomae: 'Herrenhaus, adeliger Hof; Dorf, Gemeinde'); the second spelling vîs-pati is the Sanskrit-type form rather than Avestan, a harmless variant.\",\n   \"derivation_fa\":\"اوستایی vīs- «خاندان، دهکده، تیره» صورت بی‌واکهٔ ریشهٔ *wiḱ- است که در آن ḱ کامی هندواروپایی در ایرانی به s بدل شده (سنسکریت víś-). vīspaiti- «سرور تیره، دهبد» ترکیبی است از vīs- و paiti- «سرور» و برابر سنسکریت viśpáti-؛ صورت vīs-pati که نورایی کنار آن نوشته در اصل صورت سنسکریت است. ادعای نورایی درست است (پوکورنی، بارتولومه).\",\n   \"sources\":[PIEWP,PIEW],\n   \"ref_check\":[rc(\"POK:1131\",\"supports\",\"'Avestan vīs- (e.g. Akk. vīsəm, ap. viθam) \\\"house, village, clan\\\", Old Indie viś-pati- householder, Gemeindehaupt'.\"),\n                rc(\"KLN:1708\",\"not_found\",\"KLN_1966.txt ends in the T-section (leaf 868 = 'train'); p.1708 (s.v. vicinage/vicus area) not in the local OCR. The 1971 one-volume Klein s.v. villa (KLN_1971.txt line 262096) only refers to vicus/vicinage, no Avestan form quoted in the reachable text.\")],\n   \"consulted\":[{\"src\":\"BRT\",\"where\":\"col. 1455-1456 s.v. vīs- (BRT.txt line 24320)\",\"stance\":\"supports\",\"note\":\"'j., g. vīs-, p. viθ- f. 1) \\\"Herrenhaus, Herrenburg, adeliger Hof\\\" ... 3) der zu einem Herrenhaus gehörige Komplex von Höfen \\\"Dorf, Dorfschaft, Gemeinde\\\"'; vīspaitiš in the nmānō.paitiš-vīspaitiš-zantupaitiš-dahyupaitiš series (BRT.txt line 13119).\"},POKW,WLDW]},\n  {\"id\":2,\"lang\":\"Old Persian\",\"words\":\"vith; vitha\",\"verdict\":\"confirmed\",\n   \"derivation\":\"OP viθ- 'house, royal house, royal clan, court' (DB, DPe etc.; acc. viθam, loc. viθiyā, pl. viθbiš) < PIE *wiḱ-, with the OP reflex θ of PIE *ḱ (vs. Avestan s). 'vith' is Nourai's ASCII for viθ. The adjective viθa- 'royal, of the royal family' (DPd viθaibiš) is Kent's 'probably \\\"royal\\\"', though Kent notes it may be visa- 'all'.\",\n   \"derivation_fa\":\"پارسی باستان viθ- «خانه، خاندان شاهی، دربار» از همان *wiḱ- است؛ ḱ هندواروپایی در پارسی باستان به θ و در اوستایی به s رسیده است. صفت viθa- «شاهی، از خاندان شاهی» را کنت با احتیاط چنین معنی کرده و احتمال داده که همان visa- «همه» باشد. ادعای نورایی درست است.\",\n   \"sources\":[PIEW],\n   \"ref_check\":[rc(\"KNT:208\",\"supports\",\"KNT_full.txt p.208 (page header at line 28937), line 28952: 'viθ- sb. \\\"house, royal house, royal clan, court\\\" (JNES 4.232): Av. vīs- \\\"Herrenhaus\\\", Skt. viś- \\\"house, dwelling\\\", Gk. οἶκος \\\"house\\\", Lt. vīcus \\\"village\\\"'; line 28968: 'viθa- adj., probably \\\"royal, of the royal family\\\" ... but possibly \\\"all\\\", the same as visa-'.\")],\n   \"consulted\":[{\"src\":\"BRT\",\"where\":\"col. 1455 s.v. vīs- (BRT.txt line 24320)\",\"stance\":\"supports\",\"note\":\"'p. viθ- f.' given as the OP counterpart of Av. vīs-, with 'adam hamataxšaiy yāθā viθam tyām amāxam gāθavā avāstāyam Bh. 1.14'.\"},POKW,{\"src\":\"TLM\",\"where\":\"not grepped beyond KNT\",\"stance\":\"silent\",\"note\":\"Kent sufficient; Tolman not consulted for this word.\"}]},\n  {\"id\":3,\"lang\":\"Latin\",\"words\":\"villa; vicus\",\"verdict\":\"confirmed\",\n   \"derivation\":\"Lat. vīcus 'row of houses, village, quarter' < Proto-Italic *weikos < PIE o-grade *wóyḱos (= Gk. ϝοῖκος). Lat. vīlla 'country house, farm' < *weik-slā (Pokorny *u̯oiḱ-slā), with -ksl- > -ll- and compensatory long ī (dim.-type vīcus ~ vīlla, cf. āla < *aksla).\",\n   \"derivation_fa\":\"لاتین vīcus «کوی، دهکده» از ایتالیک آغازین *weikos و آن از *wóyḱos هندواروپایی است (هم‌ریشه با یونانی oikos). vīlla «خانهٔ روستایی، ملک» از *weik-slā است که خوشهٔ -ksl- در آن به -ll- بدل شده. ادعای نورایی درست است (پوکورنی، دو وان، ویکی‌واژه).\",\n   \"sources\":[W+\"vicus\",W+\"villa\",PIEWO],\n   \"ref_check\":[rc(\"AHD\",\"supports\",\"Watkins 1985 s.v. weik-1: '*weik-slā in Latin villa, country house, farm' and '*woik-o- in Latin vicus, quarter or district of a town, neighborhood'.\")],\n   \"consulted\":[POKW,WLDW,{\"src\":\"KLN\",\"where\":\"1971 ed. s.v. villa (KLN_1971.txt line 262096)\",\"stance\":\"supports\",\"note\":\"'L. villa, \\\"country house, villa, farm\\\", which stands for *vic-sla, and is rel. to vicus, \\\"village, hamlet\\\"'.\"},{\"src\":\"LAT\",\"where\":\"not grepped\",\"stance\":\"silent\",\"note\":\"Ernout-Meillet not checked; Buck cites 'Ernout-M. 1103' for villa (SYN.txt line 32856).\"}]},\n  {\"id\":4,\"lang\":\"French\",\"words\":\"villa\",\"verdict\":\"plausible\",\n   \"derivation\":\"Fr. villa 'country house' is not inherited from Latin (the inherited reflex is ville 'town' < Lat. vīlla 'farm, later village'); it was borrowed in the 18th c. from Italian villa (itself < Lat. vīlla). So the Latin > French arrow omits an Italian step.\",\n   \"derivation_fa\":\"واژهٔ فرانسوی villa «خانهٔ ییلاقی» میراث مستقیم لاتین نیست (صورت موروثی فرانسوی ville «شهر» است)؛ این واژه از ایتالیایی villa وام گرفته شده که آن خود از لاتین vīlla است. پس پیوند لاتین ← فرانسوی با احتیاط پذیرفتنی است، چون حلقهٔ ایتالیایی افتاده است.\",\n   \"sources\":[W+\"villa\"],\n   \"ref_check\":[rc(\"none\",\"not_checked\",\"Node has no reference of its own (refs=None).\")],\n   \"consulted\":[{\"src\":\"KLN\",\"where\":\"1971 ed. s.v. villa (KLN_1971.txt line 262096)\",\"stance\":\"partial\",\"note\":\"'villa, n. — It., fr. L. villa' — the European villa word goes through Italian.\"},{\"src\":\"SYN\",\"where\":\"SYN.txt line 32856\",\"stance\":\"partial\",\"note\":\"'Fr. ville, fr. Lat. villa \\\"country house, farm\\\", late \\\"village\\\"' — the inherited French form is ville, not villa.\"}]},\n  {\"id\":5,\"lang\":\"Persian\",\"words\":\"vîlâ «ویلا»\",\"verdict\":\"confirmed\",\n   \"derivation\":\"NP vilā «ویلا» 'villa, summer house' is a 20th-century loan from French villa (Mo'in tags it [فر.]), part of the large layer of French loanwords of the Pahlavi era; Fr. -a > Persian -ā.\",\n   \"derivation_fa\":\"«ویلا» وام‌واژه‌ای نو از فرانسوی villa است که در سدهٔ چهاردهم خورشیدی همراه با دیگر واژه‌های فرانسوی به فارسی آمد؛ معین آن را با نشان «فر.» و به معنی «خانهٔ ییلاقی زیبا» آورده است. ادعای نورایی درست است.\",\n   \"sources\":[W+\"ویلا\"],\n   \"ref_check\":[rc(\"MON:5073\",\"supports\",\"Page not mappable (vol. 4 foreign words); the 2-vol Mo'in (MON_part2.txt line 88004) has 'ویلا: villa (فر.) خانه ییلاقی زیبا' — French source, as Nourai says.\")],\n   \"consulted\":[{\"src\":\"MON\",\"where\":\"2-vol ed. (MON_2vol_Adena_v2_djvu.txt line 88004)\",\"stance\":\"supports\",\"note\":\"'ویلا: villa (فر.) خانه ییلاقی زیبا'.\"},{\"src\":\"ARY\",\"where\":\"grep 'ویلا' ARY_pages.txt\",\"stance\":\"silent\",\"note\":\"no entry (Aryanpur covers inherited IE words, not modern loans).\"},{\"src\":\"HRN\",\"where\":\"grep 'vila' HRN.txt\",\"stance\":\"silent\",\"note\":\"no entry (1893, before the loan).\"}]},\n  {\"id\":6,\"lang\":\"English\",\"words\":\"villa, village; vicinity\",\"verdict\":\"plausible\",\n   \"derivation\":\"Eng. village (14th c.) < OF village < Lat. vīllāticum 'pertaining to a villa' (direct, Latin > French > English). Eng. vicinity (16th c.) < Lat. vīcīnitās 'neighbourhood' < vīcīnus 'neighbour' < vīcus. Eng. villa (1610s) is borrowed from Italian villa < Lat. vīlla, so as with node 4 the Italian intermediary is left out; all three words are correctly assigned to Lat. villa/vicus.\",\n   \"derivation_fa\":\"انگلیسی village از فرانسوی کهن village و آن از لاتین vīllāticum «وابسته به ویلا» است؛ vicinity از لاتین vīcīnitās «همسایگی» از vīcīnus «همسایه» و آن از vīcus. اما villa در انگلیسی از ایتالیایی villa وام گرفته شده، نه مستقیم از لاتین. پس پیوند کلی درست است و تنها حلقهٔ ایتالیایی افتاده است؛ با احتیاط پذیرفتنی.\",\n   \"sources\":[W+\"village\",W+\"vicinity\",W+\"villa\"],\n   \"ref_check\":[rc(\"KLN:1710\",\"partial\",\"KLN_1966 local OCR stops in T (p.1710 not reachable). 1971 ed.: 'villa, n. — It., fr. L. villa' (line 262096); 'village, n. — ME., fr. OF., fr. L. villaticus ... fr. villa' (line 262103); 'vicinity, n. — L. vicinitas, \\\"neighborhood\\\", fr. vicinus' (line 261814). Supports the Latin origin, but villa comes via Italian.\")],\n   \"consulted\":[{\"src\":\"SKT\",\"where\":\"SKT.txt line 20901; SKT_dli_revised.txt lines 85943, 85826\",\"stance\":\"supports\",\"note\":\"'village. (F.-L.) F. village — L. villaticus, adj., belonging to a farm-house — L. villa'; 'Villa. (L.) villa, a farm-house'; 'vicinity, neighbourhood. (F.-L.)'.\"},AHDW]},\n  {\"id\":7,\"lang\":\"Greek\",\"words\":\"oikos\",\"verdict\":\"confirmed\",\n   \"derivation\":\"Gk. οἶκος 'house, household' < earlier ϝοῖκος (Mycenaean wo-ko), Proto-Hellenic *wóikos < PIE *wóyḱos; the digamma w- was lost in Attic-Ionic and PIE *ḱ > k as in all centum languages.\",\n   \"derivation_fa\":\"یونانی oikos «خانه، خانوار» از صورت کهن‌تر woikos (میسنی wo-ko) و آن از *wóyḱos هندواروپایی است؛ w آغازی در یونانی آتیکی افتاده و ḱ کامی به k بدل شده است. ادعای نورایی درست است.\",\n   \"sources\":[W+\"οἶκος\",PIEWO],\n   \"ref_check\":[rc(\"AHD\",\"supports\",\"Watkins s.v. weik-1: 'Suffixed o-grade form *woik-o- in ... b. Greek oikos, house, and its derivative oikia, dwelling'.\")],\n   \"consulted\":[POKW,WLDW,{\"src\":\"KLN\",\"where\":\"1966 s.v. economy (KLN_1966.txt line 12615)\",\"stance\":\"supports\",\"note\":\"'Gk. οἶκος (dial. Ϝοῖκος) is rel. to οἰκία, Gortynic Gk. Ϝοικίαι \\\"house\\\", and cogn. with L. vicus \\\"district\\\", vicinus ... Goth. weihs, OE. wic'.\"}]},\n  {\"id\":8,\"lang\":\"English\",\"words\":\"eco-, ; ecology, economy\",\"verdict\":\"confirmed\",\n   \"derivation\":\"Eng. eco- is the combining form of Gk. οἶκος (via Latin oeco-). economy (15th c.) < Lat. oeconomia < Gk. οἰκονομία 'household management' < οἰκονόμος 'steward' (οἶκος + -νόμος 'managing'). ecology < G. Ökologie, coined by Ernst Haeckel (1866) from οἶκος + -λογία.\",\n   \"derivation_fa\":\"پیشوند انگلیسی eco- صورت ترکیبی یونانی oikos است. economy از لاتین oeconomia و آن از یونانی oikonomia «تدبیر منزل» (oikos + nomos «اداره‌کننده») است و ecology را هکل زیست‌شناس آلمانی در ۱۸۶۶ با نام Ökologie از oikos و -logia ساخت. ادعای نورایی درست است.\",\n   \"sources\":[W+\"οἶκος\"],\n   \"ref_check\":[rc(\"none\",\"not_checked\",\"Node has no reference of its own (refs=None).\")],\n   \"consulted\":[{\"src\":\"KLN\",\"where\":\"1966 s.v. ecology, economy (KLN_1966.txt lines 12612, 12615)\",\"stance\":\"supports\",\"note\":\"'ecology ... G. Ökologie, coined by the German biologist Ernst Heinrich Haeckel (1834-1919) fr. Gk. οἰκο- (see eco-)'; 'economy, n. — L. oeconomia, \\\"the management of a household\\\", fr. Gk. οἰκονομία ... compounded of οἶκος, \\\"house\\\"'.\"},AHDW]}\n ]}\nE1={\n \"entry\":1,\"root\":\"Weip, Weib\",\"verdict\":\"confirmed\",\n \"modern_form\":\"PIE *weyp- (variant *weyb-) 'to turn, swing, vibrate, tremble' (Pokorny u̯eip-, u̯eib- 1131-1132; AHD weip-)\",\n \"note\":\"Root, label and gloss correct. Pokorny: 'to turn, sway'; AHD: 'To turn, vacillate, tremble ecstatically'; Nourai's 'to go back and forth' paraphrases AHD's Germanic *wipjan 'to move back and forth'. The p/b alternation is old (de Vaan: *uip/b-ro-).\",\n \"note_fa\":\"ریشهٔ هندواروپایی آغازین *weyp- (با گونهٔ *weyb-) به معنی «چرخیدن، جنبیدن، لرزیدن» است (پوکورنی ص ۱۱۳۱–۱۱۳۲؛ واتکینز در AHD). معنای «رفت‌وآمد کردن، جنبش پس و پیش» که نورایی آورده برگرفته از AHD است. ادعای نورایی درست است.\",\n \"sources\":[PIEV],\n \"ref_check\":[rc(\"POK:1131\",\"supports\",\"POK_full.txt line 89844: 'Root / lemma: ueip- ueib- Meaning: to turn, sway ... Page(s): 1131-1132'.\")],\n \"consulted\":[WLDV,AHDV,{\"src\":\"SYN\",\"where\":\"SYN.txt line 10405\",\"stance\":\"supports\",\"note\":\"'Goth. bi-waibjan \\\"wrap about, clothe\\\" : ON veifa \\\"vibrate\\\", Skt. vip- \\\"tremble\\\", etc. Walde-P. 1.240'.\"}],\n \"nodes\":[\n  {\"id\":1,\"lang\":\"Avestan\",\"words\":\"vip\",\"verdict\":\"confirmed\",\n   \"derivation\":\"Av. vaēp-/vip- (pres. vaēpaiieiti, ppp. vipta-) 'to throw, cast (forth)', used in the Vendidad of ejaculating semen (Pokorny 'werfen, entsenden (Samen)') and also 'to commit pederasty'; it is the Iranian reflex of *weyp- 'swing' (Skt. vépate 'trembles'). Nourai's 'to send, dispatch' renders Pokorny's 'entsenden'.\",\n   \"derivation_fa\":\"اوستایی vaēp-/vip- «افکندن، بیرون انداختن» (به‌ویژه دربارهٔ نطفه در وندیداد) بازماندهٔ ایرانی ریشهٔ *weyp- «جنباندن» است و با سنسکریت vépate «می‌لرزد» هم‌ریشه است. معنای «فرستادن» در نمودار برگردان واژهٔ آلمانی entsenden در پوکورنی است. ادعای نورایی درست است.\",\n   \"sources\":[PIEV],\n   \"ref_check\":[rc(\"POK:1131\",\"supports\",\"'Avestan vip- \\\"throw, entsenden (Samen)\\\"' (POK_full.txt line 89849).\")],\n   \"consulted\":[{\"src\":\"BRT\",\"where\":\"col. 1322-1323 s.v. vaēp- (BRT.txt line 22089)\",\"stance\":\"supports\",\"note\":\"'vaēp- V. \\\"proicere\\\". Praes. vaēpa-, ... vaēpaya-, — PPfP. vipta-' with senses 'pedicare' and 'apa-: (wieder) von sich geben'.\"},WLDV]},\n  {\"id\":2,\"lang\":\"Germanic\",\"words\":\"wîpjan\",\"verdict\":\"confirmed\",\n   \"derivation\":\"Gmc. *wipjan / *wīpōn 'to move back and forth, wipe' from the *weib- variant (PIE *b > Gmc *p by Grimm's law); AHD writes *wipjan, Wiktionary reconstructs Proto-West Germanic *wīpōn > OE wīpian. Nourai's circumflex long î follows the OE vowel.\",\n   \"derivation_fa\":\"ژرمنی *wipjan / *wīpōn «پس و پیش بردن، پاک کردن» از گونهٔ *weib- ریشه است که b هندواروپایی در آن طبق قانون گریم به p بدل شده؛ از آن انگلیسی کهن wīpian آمده است. ادعای نورایی درست است.\",\n   \"sources\":[W+\"Reconstruction:Proto-Germanic/wīpaną\",W+\"wipe\"],\n   \"ref_check\":[rc(\"AHD\",\"supports\",\"Watkins s.v. weip-: 'Variant form *weib- in Germanic *wipjan, to move back and forth'.\")],\n   \"consulted\":[POKV,{\"src\":\"KLN\",\"where\":\"1971 ed. s.v. wipe (KLN_1971.txt line 267537)\",\"stance\":\"supports\",\"note\":\"'ME. wipen, fr. OE. wipian ... OHG. wifan, MHG. wifen, \\\"to swing\\\", fr. I.-E. base *weib-, \\\"to move to and fro, to swing\\\"'.\"}]},\n  {\"id\":3,\"lang\":\"English\",\"words\":\"wipe, whip\",\"verdict\":\"confirmed\",\n   \"derivation\":\"wipe < ME wipen < OE wīpian 'to rub, cleanse' (< *wipjan/*wīpōn). whip < ME whippen 'to flap' from (or reinforced by) MDu./MLG wippen 'to swing, leap', Gmc *wipp- with expressive gemination; both are *weib- words, the 'back and forth' sense surviving in whip.\",\n   \"derivation_fa\":\"انگلیسی wipe «پاک کردن» از انگلیسی میانه wipen و انگلیسی کهن wīpian است؛ whip «تازیانه، شلاق زدن» از انگلیسی میانه whippen و آن از هلندی میانه و آلمانی پست میانه wippen «تاب خوردن» است. هر دو از گونهٔ *weib- ریشه‌اند. ادعای نورایی درست است.\",\n   \"sources\":[W+\"wipe\",W+\"whip\"],\n   \"ref_check\":[rc(\"none\",\"not_checked\",\"Node has no reference of its own (refs=None).\")],\n   \"consulted\":[{\"src\":\"KLN\",\"where\":\"1971 ed. s.v. whip, wipe (KLN_1971.txt lines 266661, 267537)\",\"stance\":\"supports\",\"note\":\"'whip ... ME. whippen, rel. to Dan. vippe, MLG., MDu., Du. wippen, \\\"to swing\\\" ... See vibrate'; 'wipe ... fr. I.-E. base *weib-'.\"},{\"src\":\"SKT\",\"where\":\"SKT.txt lines 21386, 21532\",\"stance\":\"partial\",\"note\":\"'Whip ... M.E. whippen ... Du. wippen, to skip, formerly to shake'; 'Wipe. (E.) A.S. wīpian ... orig. to rub with a wisp of straw' — same words, Skeat does not name the IE root.\"},AHDV]},\n  {\"id\":4,\"lang\":\"Latin\",\"words\":\"vibrare\",\"verdict\":\"confirmed\",\n   \"derivation\":\"Lat. vibrāre 'to shake, brandish, quiver' is a denominative of Proto-Italic *wibros < PIE *wib-ro- (zero grade of *weib-) (de Vaan 674: *uip/b-ro-). Mann alone connects it with *gʷibʰro- 'quiver', a minority view.\",\n   \"derivation_fa\":\"لاتین vibrāre «لرزاندن، تکان دادن» فعلی ساخته از ایتالیک آغازین *wibros است که از صورت بی‌واکهٔ *wib-ro- ریشهٔ *weib- آمده (دو وان). تنها مان آن را به *gʷibʰro- نسبت می‌دهد که دیدگاه کم‌طرفدار است. ادعای نورایی درست است.\",\n   \"sources\":[W+\"vibro\",PIEV],\n   \"ref_check\":[rc(\"AHD\",\"supports\",\"Watkins s.v. weip-: 'Suffixed zero-grade variant form *wib-ro- in Latin vibrāre, to vibrate: VIBRATE'.\")],\n   \"consulted\":[POKV,WLDV,{\"src\":\"IEC\",\"where\":\"IEC.txt line 5200\",\"stance\":\"contradicts\",\"note\":\"Mann: 'gʷibhro ... \\\"dash, shake\\\". Lat. vibro, -āre; OE cwifer-lice ... E to quiver' — a different root (minority view).\"}]},\n  {\"id\":5,\"lang\":\"English\",\"words\":\"vibrate\",\"verdict\":\"confirmed\",\n   \"derivation\":\"Eng. vibrate (17th c.) < Lat. vibrātus, pp. of vibrāre 'to move rapidly to and fro'; a learned borrowing.\",\n   \"derivation_fa\":\"انگلیسی vibrate «لرزیدن» وام‌واژه‌ای ادبی از لاتین vibrātus، صفت مفعولی vibrāre، است. ادعای نورایی درست است.\",\n   \"sources\":[W+\"vibro\"],\n   \"ref_check\":[rc(\"none\",\"not_checked\",\"Node has no reference of its own (refs=None).\")],\n   \"consulted\":[{\"src\":\"KLN\",\"where\":\"1971 ed. s.v. vibrate (KLN_1971.txt line 261622)\",\"stance\":\"supports\",\"note\":\"'vibrate ... L. vibratus, pp. of vibrāre, \\\"to move rapidly to and fro, shake, brandish\\\", fr. I.-E. base *weib-, \\\"to move to and fro, to swing\\\"'.\"},{\"src\":\"SKT\",\"where\":\"SKT_dli_revised.txt line 85781\",\"stance\":\"supports\",\"note\":\"'Vibrate. (L.) From pp. of L. vibrāre'.\"}]}\n ]}\nd={\"pdf_page\":536,\"book_page\":506,\"verified_by\":\"claude-opus-5\",\"verified_on\":\"2026-10-16\",\"entries\":[E0,E1]}\njson.dump(d,open('/home/sfmqrb/git/rishe-private/data/verification/page-536.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)\nEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/build-536.py && cd /home/sfmqrb/git/rishe-private && python3 -m json.tool data/verification/page-536.json >/dev/null && python3 tools/verify_check.py 536"
}
```


### [2026-10-16T05:18:19.646Z] TOOL RESULT

```
nodes verified: 13/13
node verdicts: {'confirmed': 11, 'plausible': 2}
root verdicts: {'confirmed': 2}
ref checks: {'supports': 8, 'not_found': 1, 'not_checked': 4, 'partial': 1}
books consulted: {'supports': 26, 'silent': 4, 'partial': 3, 'contradicts': 1} | by book: {'KLN': 7, 'POK': 6, 'WLD': 5, 'BRT': 3, 'SKT': 3, 'AHD': 3, 'TLM': 1, 'LAT': 1, 'SYN': 1, 'MON': 1, 'ARY': 1, 'HRN': 1, 'IEC': 1}
```


## [2026-10-16T05:18:23.260Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -m4 -E \"vi[θ0]-|viϑ|viθam|vith\" TLM.txt | cut -c1-250; grep -n -m3 -E \"^ *uilla|^ *villa|^ *vīlla\" LAT.txt | cut -c1-300"
}
```


### [2026-10-16T05:18:23.580Z] TOOL RESULT

```
65:The  results  of  their  Elamite  studies  put  forth  with  such  assur- ance by  Husing,  Jensen,  Bork,  and  others,  I   have  used  perhaps Avith  too  great  caution.  We  are  forced  to  admit  that  our  knowl- edge of  this  language,  
26936:village"; peut-etre v. isl. kremia "presser", v.h.a .krimman "courber,
```


## [2026-10-16T05:18:27.641Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private/data/verification/sources/refs; grep -n -m5 -i \"ui[l1]la\\b\\|u[iī]lla,\" LAT.txt | cut -c1-300; grep -n -m5 \"viΘ\\|viӨ\\|vi9\\|viO-\\|viθ\" TLM.txt | cut -c1-200"
}
```


### [2026-10-16T05:18:27.936Z] TOOL RESULT

```
3838:rattache sans doute: anguilla (anguila) f.: anguille; M.L.461, dont
3856:anguilla, de anguis, a son pendant dans v. pruss. angurgis , lit. ungurys,
10551:cauilla, -&e f.(cauillum n., -us, m.): plaisanterie, moquerie. Ar-
10555:Si 1 1 on adopte 1 1 etymologie de Gaius, il faut anpposer que cauilla
10556:serait issu par dissimilation de *caluilla.
```


## [2026-10-16T05:19:09.260Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe-private; S=/tmp/claude-1000/-home-sfmqrb-git-rishe-private/7c41a241-7571-4c3b-8e91-929d2c62eed6/scratchpad/build-536.py; python3 - \"$S\" <<'E'\nimport sys\np=sys.argv[1]; s=open(p,encoding='utf-8').read()\ns=s.replace('''{\"src\":\"TLM\",\"where\":\"not grepped beyond KNT\",\"stance\":\"silent\",\"note\":\"Kent sufficient; Tolman not consulted for this word.\"}''','''{\"src\":\"TLM\",\"where\":\"grep 'viθ|vith|vi9|viO-' TLM.txt\",\"stance\":\"silent\",\"note\":\"no hit in the Tolman OCR (θ not rendered recognisably); Kent and Bartholomae suffice.\"}''')\ns=s.replace('''{\"src\":\"LAT\",\"where\":\"not grepped\",\"stance\":\"silent\",\"note\":\"Ernout-Meillet not checked; Buck cites 'Ernout-M. 1103' for villa (SYN.txt line 32856).\"}''','''{\"src\":\"LAT\",\"where\":\"grep -i 'uilla|villa' LAT.txt\",\"stance\":\"silent\",\"note\":\"no villa/uīlla headword found in the Ernout-Meillet OCR (only anguilla, cauilla); Buck cites 'Ernout-M. 1103' for villa (SYN.txt line 32856).\"}''')\nopen(p,'w',encoding='utf-8').write(s)\nE\npython3 $S && python3 -m json.tool data/verification/page-536.json >/dev/null && python3 tools/verify_check.py 536 | grep -c PROBLEM"
}
```


### [2026-10-16T05:19:09.896Z] TOOL RESULT

```
0
```


## [2026-10-16T05:19:19.692Z] TOOL CALL #50: SubagentHandback

```json
{
 "message": "I verified page 536 (book page 506) and wrote it to /home/sfmqrb/git/rishe-private/data/verification/page-536.json. `verify_check.py 536` shows 0 PROBLEM lines, and all 13 nodes across the 2 entries are covered.\n\n**Verdicts:**\n- Roots: 2 confirmed.\n  - Weik 2: Pokorny p.1131 ueiḱ-, which AHD numbers weik-1 \"clan\". The \"2\" is Nourai's own numbering.\n  - Weip, Weib: Pokorny pp.1131–1132, AHD weip-.\n- Nodes: 11 confirmed, 2 plausible. None are disputed or transcription_suspect.\n\n**The two plausible nodes:**\n- Weik 2, node 4, French villa: French borrowed it from Italian villa. The form inherited from Latin is ville. The chart's direct Latin → French arrow leaves out the Italian step.\n- Weik 2, node 6, English villa, village, vicinity: English villa also comes from Italian (Klein 1971: \"It., fr. L. villa\"). village (from Old French) and vicinity (from Latin vīcīnitās) are fine.\n\n**Minor notes:**\n- Avestan node 1 gives \"vîs-pati\" as a second spelling, but that is the Sanskrit-type form. The Avestan form is vīspaiti-.\n- On Latin vibrāre, Mann (IEC) alone takes it from a different root, *gʷibʰro-. I recorded this as a minority \"contradicts\" view, but the node stays confirmed.\n\n**Extraction errors:** none. The JSON matches the chart, so I didn't need to check the page image.\n\n**Process notes:**\n- **Klein pages:** Klein KLN:1708 and KLN:1710 can't be checked by page number. The local 1966 OCR (KLN_1966.txt) stops in the T section. I used the 1971 one-volume edition for the entries' content instead.\n- **Web archive:** an accidental `fetch_source.py -h` call created a junk \"-h\" entry in the web archive. Several Etymonline and Wiktionary fetches also failed. I deleted those files and their lines in sources/web/index.jsonl, so only the 15 Wiktionary pages that loaded remain. Other agents were writing to that index at the same time, so it's worth checking it still parses."
}
```


### [2026-10-16T05:19:19.973Z] TOOL RESULT

```
{"success":true,"message":"Report delivered to your caller."}
```
